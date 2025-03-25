from ctfrag.algorithms.base import RAGAlgorithms, State, RetrieverWrap
from ctfrag.database import RAGDatabase
from ctfrag.config import RetrieverConfig
from ctfrag.backends import LLMs
from ctfrag.console import console, ConsoleType, log, LogNode
from langchain.schema.runnable import RunnablePassthrough
from langgraph.graph import END, StateGraph
from ctfrag.utils import MetadataCaptureCallback, DocumentDisplayCallback
from langchain_core.documents import Document
from ctfrag.algorithms.graphrag import retriever

class SelfRAG(RAGAlgorithms):
    def __init__(self, config: RetrieverConfig, llm: LLMs, wrap: RetrieverWrap, database: RAGDatabase, embeddings):
        super().__init__(config, llm, wrap, database, embeddings)
        self.MAX_RETRIES = 3
        self.wrap = wrap

    def self_rag_retrieve(self, query, collection, template):
        self._create_vector(collection=collection)
        self._create_template(template_str=template)
        result = self.run_rag_workflow_streamed(query)
        if "error" in result:
            result["answer"] = "The workflow could not generate a valid response."
        return result

    # Self_rag : retrieve node
    # Changed
    def retrieve_node(self, state: State):
        state["recursion_depth"] += 1
        console.overlay_print("---RETRIEVE NODE---", ConsoleType.SYSTEM)
        self._log.trajectories.append(LogNode.RETRIEVE.value)
        self._log.query.append(state["question"])
        #doc_callback = DocumentDisplayCallback()
        state = {"question": state["question"], "context": [], "answer": ""}
        retrieval_result = self.retrieve(state)

        response = retrieval_result.get("context", [])
        answer = retrieval_result.get("answer", "")
        """ token_usages = response.usage_metadata
        self.llm.update_model_cost(token_usages)
        result = response.content
        source, context = log.parse_documents(doc_callback.documents)
        self._log.source.append(source)
        self._log.shortcut.append(context) """
        state["context"] = response
        #state["answer"] = answer
        return state
    
    # Self_rag : generate node
    def generate_node(self, state: State):
        state["recursion_depth"] += 1
        console.overlay_print("---GENERATE NODE---", ConsoleType.SYSTEM)
        self._log.trajectories.append(LogNode.GENERATE.value)
        result = self.generate(state)
        state["answer"] = result["answer"]
        self._log.interm_generation.append(result["answer"])
        return state

    # Self_rag : grade retrieved documents node
    def grade_documents_node(self, state: State):
        console.overlay_print("---GRADE DOCUMENTS NODE---", ConsoleType.SYSTEM)
        self._log.trajectories.append(LogNode.GRADE_DOCUMENTS.value)
        question = state["question"]
        documents = state["context"]
        filtered_docs, is_relevant = self.grade_retrieval(question, documents)
        state["recursion_depth"] += 1

        if not filtered_docs:
            console.overlay_print("---NO RELEVANT DOCUMENTS FOUND---", ConsoleType.SYSTEM)
        
        self._log.document_quality.append(is_relevant == "yes")
        state["context"] = filtered_docs
        return state

    # Self_rag : transform query node
    def transform_query_node(self, state: State):
        state["recursion_depth"] += 1
        console.overlay_print("---TRANSFORM QUERY NODE---", ConsoleType.SYSTEM)
        self._log.trajectories.append(LogNode.REWRITE_QUERY.value)
        question = state["question"]
        rewritten_question = self.rewrite_question(question)
        state["question"] = rewritten_question
        return state
    
    # Self_rag : decide to generate or not edge
    def decide_to_generate(self, state: State):
        console.overlay_print("---ASSESS GRADED DOCUMENTS---", ConsoleType.SYSTEM)
        self._log.trajectories.append(LogNode.DECIDE_GENERATION.value)
        documents = state["context"]
        if not documents:
            console.overlay_print("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---", ConsoleType.SYSTEM)
            if state["recursion_depth"] > self.MAX_RETRIES:
                console.overlay_print("---MAX RECURSION DEPTH REACHED. Stopping workflow.---", ConsoleType.SYSTEM)
                return "end"     
            return "transform_query"
        else:
            console.overlay_print("---DECISION: GENERATE---", ConsoleType.SYSTEM)
            return "generate"
    
    # Self_rag : check for hallucination and whether answers the question edge
    def grade_generation_v_documents_and_question(self, state: State):
        console.overlay_print("---CHECK HALLUCINATIONS---", ConsoleType.SYSTEM)
        self._log.trajectories.append(LogNode.GRADE_HALLUCINATION.value)
        question = state["question"]
        documents = state["context"] 
        generation = state.get("answer", "") 
        metadata_callback = MetadataCaptureCallback() 
        score = self.hallucination_grader.invoke({"documents": documents, "generation": generation}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
        grade = score.binary_score
        self._log.no_hallucinations.append(grade == "yes")
        if grade == "yes":
            console.overlay_print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---", ConsoleType.SYSTEM)
            console.overlay_print("---GRADE GENERATION vs QUESTION---", ConsoleType.SYSTEM)
            self._log.trajectories.append(LogNode.GRADE_ANSWER.value)
            metadata_callback = MetadataCaptureCallback() 
            score = self.answer_grader.invoke({"question": question, "generation": generation}, config={"callbacks": [metadata_callback]})
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
            grade = score.binary_score
            self._log.answer_quality.append(grade == "yes")
            if grade == "yes":
                console.overlay_print("---DECISION: GENERATION ADDRESSES QUESTION---", ConsoleType.SYSTEM)
                return "useful"
                
            else:
                console.overlay_print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---", ConsoleType.SYSTEM)
                self._log.trajectories.append(LogNode.RETRY.value)
                if state["recursion_depth"] > self.MAX_RETRIES:
                    console.overlay_print("---MAX RETRIES REACHED. STOPPING RECURSION---", ConsoleType.SYSTEM)
                    return "end"
                
                return "not useful"
        else:
            console.overlay_print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---", ConsoleType.SYSTEM)
            self._log.trajectories.append(LogNode.RETRY.value)
            if state["recursion_depth"] > self.MAX_RETRIES:
                console.overlay_print("---MAX RETRIES REACHED. STOPPING RECURSION---", ConsoleType.SYSTEM)
                return "end"
            return "not supported"

    # Self_rag : build self_rag graph
    def build_rag_graph(self):
        workflow = StateGraph(State)  

        workflow.add_node("retrieve", self.retrieve_node) 
        workflow.add_node("grade_documents", self.grade_documents_node)  
        workflow.add_node("generate", self.generate_node)  
        workflow.add_node("transform_query", self.transform_query_node) 

        workflow.set_entry_point("retrieve")
        workflow.add_edge("retrieve", "grade_documents")

        workflow.add_conditional_edges(
            "grade_documents",
            self.decide_to_generate, 
            {
                "transform_query": "transform_query", 
                "generate": "generate",  
                "end": END,
            },
        )

        workflow.add_edge("transform_query", "retrieve")

        workflow.add_conditional_edges(
            "generate",
            self.grade_generation_v_documents_and_question, 
            {
                "not supported": "generate",  
                "useful": END,  
                "not useful": "transform_query",  
                "end": END,
            },
        )

        compiled_graph = workflow.compile()
        if compiled_graph is None:
            raise ValueError("Failed to compile the RAG workflow graph!")

        return compiled_graph

    # Self_rag : run self_rag workflow
    def run_rag_workflow_streamed(self, query):
        console.overlay_print("---STARTING STREAMED SELF-RAG WORKFLOW---", ConsoleType.SYSTEM)
        app = self.build_rag_graph()
        if app is None:
            raise RuntimeError("Graph compilation failed. Cannot proceed with RAG workflow.")

        inputs = {"question": query, "context": [], "answer": "","recursion_depth": 0}

        final_output = None
        for output in app.stream(inputs):
            for key, value in output.items():
                console.overlay_print(f"Node '{key}':", ConsoleType.INFO) 
            final_output = value 
            
        if final_output and "answer" in final_output and final_output["answer"] != '':
            return {"answer": final_output["answer"]}
        elif final_output and "context" in final_output and final_output["context"] != '':
            final_answer = "\n".join(final_output["context"]) + "\n\n"
            return {"answer": final_answer}
        else:
            return {"error": "The workflow could not generate a valid response."}
        
    
    """ def self_rag_generate(self, state: State):
        default_answer = "The response contains no verified factual content."
        default_suggestion = "Consider refining your query for more accurate results."
        docs_content = "\n\n".join(doc.page_content if hasattr(doc, "page_content") else str(doc) for doc in state["context"])

        messages = self.wrap.template.invoke({"question": state["question"], "context": docs_content})
        response = self.llm().invoke(messages)
        token_usages = response.usage_metadata
        self.llm.update_model_cost(token_usages)
        if self.config.feature_config.hallucination_grading:
            grounded_content = self.grade_hallucination(state["context"], response)

            if not grounded_content:
                return {
                    "answer": default_answer,
                    "suggestion": default_suggestion
                }
        if self.config.feature_config.answer_grading:
            is_relevant = self.grade_answer(state["question"], response)
            if not is_relevant:
                return {
                    "answer": default_answer,
                    "suggestion": default_suggestion
                }
        return {"answer": response.content} """
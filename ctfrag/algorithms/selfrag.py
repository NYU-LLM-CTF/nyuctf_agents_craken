from ctfrag.algorithms.base import RAGAlgorithms, State, RetrieverWrap
from ctfrag.database import RAGDatabase
from ctfrag.config import RetrieverConfig
from ctfrag.backends import LLMs
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langgraph.graph import END, StateGraph

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
    def retrieve_node(self, state: State):
        state["recursion_depth"] += 1
        print("---RETRIEVE NODE---")
        retriever = self.wrap.vector_store.as_retriever()
        rag_chain = (
            {"context": retriever,  "question": RunnablePassthrough()}
            | self.wrap.template
            | self.llm
            | StrOutputParser()
        )
        result = rag_chain.invoke(state["question"])
        state["context"] = result
        return state
    
    # Self_rag : generate node
    def generate_node(self, state: State):
        state["recursion_depth"] += 1

        print("---GENERATE NODE---")
        result = self.self_rag_generate(state)
        state["answer"] = result["answer"]
        return state

    # Self_rag : grade retrieved documents node
    def grade_documents_node(self, state: State):
        print("---GRADE DOCUMENTS NODE---")
        question = state["question"]
        documents = state["context"]
        filtered_docs = self.grade_retrieval(question, documents)
        state["recursion_depth"] += 1

        if not filtered_docs:
            print("---NO RELEVANT DOCUMENTS FOUND---")
            
        state["context"] = filtered_docs
        return state

    # Self_rag : transform query node
    def transform_query_node(self, state: State):
        state["recursion_depth"] += 1
        print("---TRANSFORM QUERY NODE---")
        question = state["question"]
        rewritten_question = self.rewrite_question(question)
        state["question"] = rewritten_question
        return state
    
    # Self_rag : decide to generate or not edge
    def decide_to_generate(self, state: State):
        print("---ASSESS GRADED DOCUMENTS---")
        documents = state["context"]
        if not documents:
            print("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---")
            if state["recursion_depth"] > self.MAX_RETRIES:
                print("---MAX RECURSION DEPTH REACHED. Stopping workflow.---")
                return "end"     
            return "transform_query"
        else:
            print("---DECISION: GENERATE---")
            return "generate"
    
    # Self_rag : check for hallucination and whether answers the question edge
    def grade_generation_v_documents_and_question(self, state: State):
        print("---CHECK HALLUCINATIONS---")
        question = state["question"]
        documents = state["context"] 
        generation = state.get("answer", "")  

        score = self.hallucination_grader.invoke({"documents": documents, "generation": generation})
        grade = score.binary_score

        if grade == "yes":
            print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
            print("---GRADE GENERATION vs QUESTION---")
            score = self.answer_grader.invoke({"question": question, "generation": generation})
            grade = score.binary_score
            if grade == "yes":
                print("---DECISION: GENERATION ADDRESSES QUESTION---")
                return "useful"
                
            else:
                print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
                if state["recursion_depth"] > self.MAX_RETRIES:
                    print("---MAX RETRIES REACHED. STOPPING RECURSION---")
                    return "end"
                
                return "not useful"
        else:
            print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
            if state["recursion_depth"] > self.MAX_RETRIES:
                print("---MAX RETRIES REACHED. STOPPING RECURSION---")
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
        print("---STARTING STREAMED GRAPH-BASED RAG WORKFLOW---")
        app = self.build_rag_graph()
        if app is None:
            raise RuntimeError("Graph compilation failed. Cannot proceed with RAG workflow.")

        inputs = {"question": query, "context": [], "answer": "","recursion_depth": 0}

        final_output = None
        for output in app.stream(inputs):
            for key, value in output.items():
                print(f"Node '{key}':") 
            final_output = value 
            
        if final_output and "answer" in final_output and final_output["answer"] != '':
            return {"answer": final_output["answer"]}
        elif final_output and "context" in final_output and final_output["context"] != '':
            final_answer = "\n".join(final_output["context"]) + "\n\n"
            return {"answer": final_answer}
        else:
            return {"error": "The workflow could not generate a valid response."}
        
    
    def self_rag_generate(self, state: State):
        default_answer = "The response contains no verified factual content."
        default_suggestion = "Consider refining your query for more accurate results."
        docs_content = "\n\n".join(doc.page_content if hasattr(doc, "page_content") else str(doc) for doc in state["context"])
    
        messages = self.wrap.template.invoke({"question": state["question"], "context": docs_content})
        response = self.llm.invoke(messages)
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
        return {"answer": response.content}
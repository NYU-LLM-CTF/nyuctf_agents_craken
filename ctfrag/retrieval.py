from ctfrag.database import RAGDatabase
from ctfrag.db_backend.milvus import MilvusDB
from ctfrag.db_backend.weaviate import WeaviateDB
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain.schema.output_parser import StrOutputParser
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from langgraph.graph import START, END, StateGraph
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.document_compressors.rankllm_rerank import RankLLMRerank
from langchain.load import dumps, loads
from operator import itemgetter
from pydantic import BaseModel, Field
from pprint import pprint

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str
    recursion_depth: int

class RetrieverWrap:
    def __init__(self) -> None:
        self.retriever = None
        self.compressor = None
        self.cretriever = None
        self.vector_store = None
        self.prompt = None
        self.template = None

class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""
    binary_score: str = Field(description="Documents are relevant to the question, 'yes' or 'no'")

class GradeHallucinations(BaseModel):
    """Binary score for hallucination present in generation answer."""
    binary_score: str = Field(description="Answer is grounded in the facts, 'yes' or 'no'")

class GradeAnswer(BaseModel):
    """Binary score to assess whether the answer addresses the question."""
    binary_score: str = Field(description="Answer addresses the question, 'yes' or 'no'")


class RAGRetrieval:
    def __init__(self, llm=None, config={}) -> None:
        self.llm = llm
        self.config = config
        self.database = RAGDatabase(self._setup_db(self.config.db_config.storage), config=config)
        self.graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph = self.graph_builder.compile()
        self.wrap = RetrieverWrap()
        self._init_retrieval_grader()
        self._init_hallucination_grader()
        self._init_answer_grader()
        self._init_question_rewriter()

    def _setup_db(self, db_storage):
        if db_storage == "milvus":
            return MilvusDB()
        elif db_storage == "weaviate":
            return WeaviateDB()
        else:
            return MilvusDB()

    def _create_compressor(self, compressor: str):
        if compressor == "RankLLMRerank":
            if self.config.retrieval_config.reranker_model.startswith("gpt"):
                self.wrap.compressor = RankLLMRerank(top_n=self.config.retrieval_config.reranker_top_n, 
                                                     model="gpt", gpt_model=self.config.retrieval_config.reranker_model)
            else:
                self.wrap.compressor = RankLLMRerank(top_n=self.config.retrieval_config.reranker_top_n, 
                                                     model=self.config.retrieval_config.reranker_model)
            return
        if compressor == "LLMChainExtractor":
            self.wrap.compressor = LLMChainExtractor.from_llm(self.llm)
            return
        
    def _create_cretriever(self, cretriever: str):
        if cretriever == "ContextualCompressionRetriever":
            self.wrap.cretriever = ContextualCompressionRetriever(
                base_compressor=self.wrap.compressor, base_retriever=self.wrap.retriever
            )
            return

    def _create_vector(self, collection: str=None):
        if not collection:
            raise ValueError("Please specify a collection")
        self.wrap.vector_store = self.database.get_db().create_vector(collection=collection)

    def _create_retriever(self):
        if self.config.feature_config.search_params:
            self.wrap.retriever = self.wrap.vector_store.as_retriever(search_type=self.config.retrieval_config.retriever_search, 
                                                           search_kwargs=self.config.retrieval_config.retriever_params)
        else:
            self.wrap.retriever = self.wrap.vector_store.as_retriever(search_type=self.config.retrieval_config.retriever_search) 

    def _create_template(self, template_str: str=None):
        if not template_str:
            raise ValueError("Please specify a prompt template")
        self.wrap.prompt = template_str
        self.wrap.template = ChatPromptTemplate.from_template(self.wrap.prompt)
    
    def _init_retrieval_grader(self):
        grade_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.retrieval_config.template_retrieval_grading),
                ("human", "Retrieved document: \n\n {document} \n\n User question: {question}"),
            ]
        )
        structured_llm_grader = self.llm.with_structured_output(GradeDocuments)
        self.retrieval_grader = grade_prompt | structured_llm_grader

    def grade_retrieval(self, question, documents):
        relevant_docs = []
        for doc in documents:
            doc_text = doc.page_content
            grading_result = self.retrieval_grader.invoke({"question": question, "document": doc_text})
            if grading_result.binary_score.lower() == "yes":
                relevant_docs.append(doc)
        return relevant_docs
    
    def _init_hallucination_grader(self):
        hallucination_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.retrieval_config.template_hallucination_grading),
                ("human", "Set of facts: \n\n {documents} \n\n LLM generation: {generation}"),
            ]
        )
        self.hallucination_grader = hallucination_prompt | self.llm.with_structured_output(GradeHallucinations)

    def grade_hallucination(self, documents, generation):
        docs_content = "\n\n".join(doc.page_content for doc in documents)
        grading_result = self.hallucination_grader.invoke({"documents": docs_content, "generation": generation})
        return grading_result.binary_score.lower() == "yes"

    def _init_answer_grader(self):
        answer_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.retrieval_config.template_answer_grading),
                ("human", "User question: \n\n {question} \n\n LLM generation: {generation}"),
            ]
        )
        self.answer_grader = answer_prompt | self.llm.with_structured_output(GradeAnswer)

    def grade_answer(self, question, generation):
        grading_result = self.answer_grader.invoke({"question": question, "generation": generation})
        return grading_result.binary_score.lower() == "yes"
    
    def _init_question_rewriter(self):
        re_write_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.retrieval_config.template_question_rewriting),
                ("human", "Here is the initial question: \n\n {question} \n Formulate an improved question."),
            ]
        )
        self.question_rewriter = re_write_prompt | self.llm | StrOutputParser()

    def rewrite_question(self, question):
        rewritten_question = self.question_rewriter.invoke({"question": question})
        return rewritten_question
    
    def _multi_query(self):
        prompt_perspectives = ChatPromptTemplate.from_template(input_variables=["question"], template=self.config.retrieval_config.template_multi)
        
        generate_queries = (
            prompt_perspectives 
            | self.llm
            | StrOutputParser() 
            | (lambda x: x.split("\n"))
        )
        return generate_queries

    def _reciprocal_rank_fusion(self, results: list[list], k=60):
        fused_scores = {}
        for docs in results:
            for rank, doc in enumerate(docs):
                doc_str = dumps(doc) 
                if doc_str not in fused_scores:
                    fused_scores[doc_str] = 0
                fused_scores[doc_str] += 1 / (rank + k)
        reranked_results = [
            (loads(doc), score) for doc, score in sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
        ]
        return [doc for doc, _ in reranked_results]  

    def _decompose_question(self, question: str):
        prompt_decomposition = ChatPromptTemplate.from_template(template=self.config.retrieval_config.template_decompose)
        generate_queries_decomposition = (
            prompt_decomposition
            | self.llm
            | StrOutputParser()
            | (lambda x: x.split("\n"))
        )
        sub_questions = generate_queries_decomposition.invoke({"question": question})
        return sub_questions

    def format_qa_pair(self, question, answer):
        formatted_string = ""
        formatted_string += f"Question: {question}\nAnswer: {answer}\n\n"
        return formatted_string.strip()
    
    def _answer_sub_questions(self, sub_questions: list[str]):
        decomposition_prompt = ChatPromptTemplate.from_template(template=self.config.retrieval_config.template_answer_decompose)
        
        q_a_pairs = ""
        for q in sub_questions:
            rag_chain = (
                {"context": itemgetter("question") | self.retriever,  
                "question": itemgetter("question"),
                "q_a_pairs": itemgetter("q_a_pairs")}
                | decomposition_prompt
                | self.llm
                | StrOutputParser()
            )
            
            answer = rag_chain.invoke({"question": q, "q_a_pairs": q_a_pairs})
            q_a_pair = self.format_qa_pair(q, answer)
            q_a_pairs += "\n---\n" + q_a_pair

        return answer, {"q_a_pairs": q_a_pairs}

    def _generate_step_back_query(self, question: str):
        examples = [
            {
                "input": "Could the members of The Police perform lawful arrests?",
                "output": "What can the members of The Police do?",
            },
            {
                "input": "Jan Sindel's was born in what country?",
                "output": "What is Jan Sindel's personal history?",
            },
        ]
        example_prompt = ChatPromptTemplate.from_messages(
            [
                ("human", "{input}"),
                ("ai", "{output}"),
            ]
        )
        few_shot_prompt = FewShotChatMessagePromptTemplate(
            example_prompt=example_prompt,
            examples=examples,
        )
        step_back_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", """You are an expert at world knowledge. Your task is to step back and paraphrase a question to a more general form."""),
                few_shot_prompt,
                ("user", "{question}"),
            ]
        )
        chain = (
            step_back_prompt
            | self.llm
            | StrOutputParser()
        )
        step_back_query = chain.invoke({"question": question})
        return step_back_query

    def _retrieve_step_back_context(self, question: str, step_back_query: str):
        response_prompt = ChatPromptTemplate.from_template(response_prompt_template=self.config.retrieval_config.template_step_back)
        chain = (
            {
                "normal_context": RunnableLambda(lambda x: x["question"]) | self.wrap.retriever,
                "step_back_context": step_back_query | self.wrap.retriever,
                "question": lambda x: x["question"],
            }
            | response_prompt
            | self.llm
            | StrOutputParser()
        )

        result = chain.invoke({"question": question})
        return result

    def _search(self, question):
        if self.config.feature_config.rerank:
            self._create_retriever()
            self._create_compressor(self.config.retrieval_config.reranker_type)
            self._create_cretriever(self.config.retrieval_config.compressor_retriever)
            return self.wrap.cretriever.invoke(question)
        if self.config.feature_config.compressor:
            self._create_retriever()
            self._create_compressor(self.config.retrieval_config.compressor_type)
            self._create_cretriever(self.config.retrieval_config.compressor_retriever)
            return self.wrap.cretriever.invoke(question)
        if self.config.retrieval_config.retriever_type == "similarity_search":
            return self.wrap.vector_store.similarity_search(question)
        
    def retrieve(self, state: State):
        if self.config.feature_config.question_rewriting:
            state["question"] = self.rewrite_question(state["question"])
        if self.config.feature_config.multi_query:
            questions = self._multi_query(state["question"])
            all_docs = []
            for question in questions:
                docs = self._search(question)
                all_docs.extend(docs)
            
            unique_docs = list({doc.page_content: doc for doc in all_docs}.values())
            final_docs=unique_docs
        if self.config.feature_config.rag_fusion:
            questions = self._multi_query(state["question"])

            queries = questions.invoke({"question": state["question"]})
            results = [self._search(query) for query in queries]
            unique_docs = self._reciprocal_rank_fusion(results)
            final_docs=unique_docs
        if self.config.feature_config.decomposition:
            sub_questions = self._decompose_question(state["question"])
            answer,q_a_results = self._answer_sub_questions(sub_questions)
            final_docs=q_a_results["q_a_pairs"]
            final_answer=answer
            
        if self.config.feature_config.step_back:
            step_back_query = self._generate_step_back_query(state["question"])
            synthesized_result = self._retrieve_step_back_context(state["question"], step_back_query)
            final_docs=synthesized_result["normal_context"]
            final_answer=synthesized_result["step_back_context"]
            return {"context": synthesized_result["normal_context"], "answer": synthesized_result["step_back_context"]}

        else:
            final_docs = self._search(state["question"])

        if not final_docs:
            print("---NO DOCUMENTS FOUND. RETURNING DEFAULT RESPONSE---")
            final_docs = [Document(page_content="No relevant documents found.")]

        if self.config.feature_config.retrieval_grading:
            final_docs = self.grade_retrieval(state["question"], final_docs)

        if self.config.feature_config.decomposition:
            return {"context": final_docs, "answer": final_answer}
        if self.config.feature_config.step_back:
            return {"context": final_docs, "answer": final_answer}
        else:
            return {"context": final_docs}

    def generate(self, state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = self.wrap.template.invoke({"question": state["question"], "context": docs_content})
        response = self.llm.invoke(messages)
        if self.config.feature_config.hallucination_grading:
            grounded_content = self.grade_hallucination(state["context"], response)

            if not grounded_content:
                return {
                    "error": "The response contains no verified factual content.",
                    "suggestion": "Consider refining your query for more accurate results."
                }
        if self.config.feature_config.answer_grading:
            is_relevant = self.grade_answer(state["question"], grounded_content)
            if not is_relevant:
                return {
                    "error": "The response does not directly answer the question.",
                    "suggestion": "Consider rephrasing your question or asking for specific details."
                }
        return {"answer": response.content}
    
    def graph_retrieve(self, query, collection, template):
        self._create_vector(collection=collection)
        self._create_template(template_str=template)
        result = self.graph.invoke({"question": query})
        return {"context": result["context"], "answer": result["answer"]}
    
    def chain_retrieve(self, query, collection, template) -> None:
        self._create_vector(collection=collection)
        self._create_template(template_str=template)
        retriever = self.wrap.vector_store.as_retriever()
        rag_chain = (
            {"context": retriever,  "question": RunnablePassthrough()}
            | self.wrap.template
            | self.llm
            | StrOutputParser()
        )
        result = rag_chain.invoke(query)
        return result

    def self_rag_retrieve(self, query, collection, template):
        self._create_vector(collection=collection)
        self._create_template(template_str=template)
        result = self.run_rag_workflow_streamed(query)
        if "error" in result:
            result["answer"] = "The workflow could not generate a valid response."
        return result

    def retrieve_node(self, state: State):
        
        if state["recursion_depth"] > self.MAX_RETRIES:
            print("Maximum recursion depth reached. Terminating workflow.")
            #return {"context": [], "answer": "Max retries reached. Stopping execution."} 
            return END
        state["recursion_depth"] += 1

        print("---RETRIEVE NODE---")
        retrieval_result = self.retrieve(state)
        state["context"] = retrieval_result["context"]
        return state

    def generate_node(self, state: State):
       
        if state["recursion_depth"] > self.MAX_RETRIES:
            print("Maximum recursion depth reached. Terminating workflow.")
            #return {"context": [], "answer": "Max retries reached. Stopping execution."} 
            return END
        state["recursion_depth"] += 1

        print("---GENERATE NODE---")
        result = self.generate(state)
        state["answer"] = result["answer"]
        return state

    def grade_documents_node(self, state: State):
        print("---GRADE DOCUMENTS NODE---")
        question = state["question"]
        documents = state["context"]
        filtered_docs = self.grade_retrieval(question, documents)

        if not filtered_docs:
            print("---NO RELEVANT DOCUMENTS FOUND---")
            if state["recursion_depth"] > self.MAX_RETRIES:
                print("Maximum recursion depth reached. Terminating workflow.")
                return END
            state["recursion_depth"] += 1
            return {"context": [], "retry": True}
    
        state["context"] = filtered_docs
        return state

    def transform_query_node(self, state: State):
        state["recursion_depth"] += 1
        if state["recursion_depth"] > self.MAX_RETRIES:
            print("Maximum recursion depth reached. Terminating workflow.")
            return END

        print("---TRANSFORM QUERY NODE---")
        question = state["question"]
        rewritten_question = self.rewrite_question(question)
        state["question"] = rewritten_question
        return state

    MAX_RETRIES = 3

    def decide_to_generate(self, state: State):
        print("---ASSESS GRADED DOCUMENTS---")
        documents = state["context"]
        if "retry_count" not in state:
            state["retry_count"] = 0
        if not documents:
            print("---DECISION: ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, TRANSFORM QUERY---")
            state["recursion_depth"] += 1
            if state["recursion_depth"] > self.MAX_RETRIES:
                print("---MAX RECURSION DEPTH REACHED. Stopping workflow.---")
                return END 

            return {"next_step": "transform_query"}
        else:
            print("---DECISION: GENERATE---")
            return {"next_step": "generate"}
    
    def grade_generation_v_documents_and_question(self, state: State):
        print("---CHECK HALLUCINATIONS---")
        question = state["question"]
        documents = state["context"] 
        generation = state.get("answer", "")  

        if "retry_count" not in state:
            state["retry_count"] = 0

        score = self.hallucination_grader.invoke({"documents": documents, "generation": generation})
        grade = score.binary_score

        if grade == "yes":
            print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
            print("---GRADE GENERATION vs QUESTION---")
            score = self.answer_grader.invoke({"question": question, "generation": generation})
            grade = score.binary_score
            if grade == "yes":
                print("---DECISION: GENERATION ADDRESSES QUESTION---")
                #return "useful"
                #return {"answer": generation}
                return END
            else:
                print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
                state["retry_count"] += 1
                if state["retry_count"] >= self.MAX_RETRIES:
                    print("---MAX RETRIES REACHED. STOPPING RECURSION---")
                    #return "useful"  # Prevent further recursion
                    return END
                    #return {"context": [], "answer": "Answer does not address the question. Stopping execution."} 

                return "not useful"
        else:
            print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
            state["retry_count"] += 1
            if state["retry_count"] >= self.MAX_RETRIES:
                print("---MAX RETRIES REACHED. STOPPING RECURSION---")
                #return "useful"  # Prevent further recursion
                return END
                #return {"context": [], "answer": "Answer is not grounded in facts. Stopping execution."}  

            return "not supported"

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
                "stop": END,
            },
        )

        workflow.add_edge("transform_query", "retrieve")

        workflow.add_conditional_edges(
            "generate",
            self.grade_generation_v_documents_and_question, 
            {
                "not supported": "generate",  
                #"not supported": END,
                "useful": END,  
                "not useful": "transform_query",  
                "stop": END,
            },
        )

        compiled_graph = workflow.compile()
        if compiled_graph is None:
            raise ValueError("Failed to compile the RAG workflow graph!")

        return compiled_graph

    def run_rag_workflow_streamed(self, query):
        print("---STARTING STREAMED GRAPH-BASED RAG WORKFLOW---")
        app = self.build_rag_graph()
        if app is None:
            raise RuntimeError("Graph compilation failed. Cannot proceed with RAG workflow.")

        """ # Ensure `app.config` exists before modifying it
        if not hasattr(app, "config") or app.config is None:
            app.config = {}  # Initialize config if it's None

        app.config["recursion_limit"] = 50  # Increase recursion limit """

        inputs = {"question": query, "context": [], "answer": "","recursion_depth": 0}

        final_output = None
        for output in app.stream(inputs):
            for key, value in output.items():
                pprint(f"Node '{key}':")

            pprint("\n---\n")  
            final_output = value 

        if final_output and "answer" in final_output:
            return {"answer": final_output["answer"]}
        else:
            return {"error": "The workflow could not generate a valid response."}
        
    def close_db(self):
        self.database.get_db().close_db()

    def print_docs(self, docs):
        print(
            f"\n{'-' * 100}\n".join(
                [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
            )
        )

if __name__ == "__main__":
    pass
    # retreval = RAGRetrieval(llm=TESTLLM, prompt_template=TEST_TEMPLATE, db_warp=MilvusDB())
    # context, answer = retreval.graph_retrieve("What is decomposition?")
    # # answer = retreval.chain_retrieve("What is decomposition?")
    # print(answer)
    # retreval.close_db()
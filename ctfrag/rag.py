from ctfrag.database import RAGDatabase
from ctfrag.db_backend.milvus import MilvusDB
from ctfrag.db_backend.weaviate import WeaviateDB
from ctfrag.db_backend.neo4j import Neo4jDB
from ctfrag.config import RetrieverConfig
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from langgraph.graph import START, END, StateGraph
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.document_compressors.rankllm_rerank import RankLLMRerank
from langchain.load import dumps, loads
from pydantic import BaseModel, Field
from pprint import pprint
from langchain_neo4j import GraphCypherQAChain

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

class RAGAgent:
    def __init__(self, llm=None, embeddings=None, config:RetrieverConfig=None) -> None:
        self.llm = llm
        self.embeddings = embeddings
        self.config = config
        self.database = RAGDatabase(self._setup_db(self.config.db_config.storage), config=config)
        self.graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph_legacy = self.graph_builder.compile()
        if config.db_config.storage == "neo4j":
            self.graph = self.database.get_db().create_graph()
        else:
            # We don't use graph rag
            self.graph = None
        self.wrap = RetrieverWrap()
        self.MAX_RETRIES = 3
        self._init_retrieval_grader()
        self._init_hallucination_grader()
        self._init_answer_grader()
        self._init_question_rewriter()

    def _setup_db(self, db_storage):
        if db_storage == "milvus":
            return MilvusDB(embeddings=self.embeddings)
        elif db_storage == "weaviate":
            return WeaviateDB()
        elif db_storage == "neo4j":
            return Neo4jDB(embeddings=self.embeddings)
        else:
            return MilvusDB(embeddings=self.embeddings)

    def _create_compressor(self, compressor: str):
        if compressor == "RankLLMRerank":
            if self.config.rag_config.reranker_model.startswith("gpt"):
                self.wrap.compressor = RankLLMRerank(top_n=self.config.rag_config.reranker_top_n, 
                                                     model="gpt", gpt_model=self.config.rag_config.reranker_model)
            else:
                self.wrap.compressor = RankLLMRerank(top_n=self.config.rag_config.reranker_top_n, 
                                                     model=self.config.rag_config.reranker_model)
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
        self.wrap.vector_store = self.database.get_db().create_vector(collection=collection, embeddings=self.embeddings)

    def _create_retriever(self):
        if self.config.feature_config.search_params:
            self.wrap.retriever = self.wrap.vector_store.as_retriever(search_type=self.config.rag_config.retriever_search, 
                                                           search_kwargs=self.config.rag_config.retriever_params)
        else:
            self.wrap.retriever = self.wrap.vector_store.as_retriever(search_type=self.config.rag_config.retriever_search) 

    def _create_template(self, template_str: str=None):
        if not template_str:
            raise ValueError("Please specify a prompt template")
        self.wrap.prompt = template_str
        self.wrap.template = ChatPromptTemplate.from_template(self.wrap.prompt)
    
    # grade retrieved documents for relevent
    def _init_retrieval_grader(self):
        grade_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.prompts.rag_retrieval_grading),
                ("human", "Retrieved document: \n\n {document} \n\n User question: {question}"),
            ]
        )
        structured_llm_grader = self.llm.with_structured_output(GradeDocuments)
        self.retrieval_grader = grade_prompt | structured_llm_grader

    def grade_retrieval(self, question, documents):
        relevant_docs = []
        grading_result = self.retrieval_grader.invoke({"question": question, "document": documents})
        if grading_result.binary_score.lower() == "yes":
            relevant_docs.append(documents)
        return relevant_docs 
    
    # grade generated output for hallucination
    def _init_hallucination_grader(self):
        hallucination_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.prompt.rag_hallucination_grading),
                ("human", "Set of facts: \n\n {documents} \n\n LLM generation: {generation}"),
            ]
        )
        self.hallucination_grader = hallucination_prompt | self.llm.with_structured_output(GradeHallucinations)

    def grade_hallucination(self, documents, generation):
        docs_content = "\n\n".join(doc.page_content for doc in documents)
        grading_result = self.hallucination_grader.invoke({"documents": docs_content, "generation": generation})
        return grading_result.binary_score.lower() == "yes"

    # grade generated output for answered question or not
    def _init_answer_grader(self):
        answer_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.prompts.rag_answer_grading),
                ("human", "User question: \n\n {question} \n\n LLM generation: {generation}"),
            ]
        )
        self.answer_grader = answer_prompt | self.llm.with_structured_output(GradeAnswer)

    def grade_answer(self, question, generation):
        grading_result = self.answer_grader.invoke({"question": question, "generation": generation})
        return grading_result.binary_score.lower() == "yes"
    
    # rewrite question
    def _init_question_rewriter(self):
        re_write_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.prompt.rag_question_rewriting),
                ("human", "Here is the initial question: \n\n {question} \n Formulate an improved question."),
            ]
        )
        self.question_rewriter = re_write_prompt | self.llm | StrOutputParser()

    def rewrite_question(self, question):
        rewritten_question = self.question_rewriter.invoke({"question": question})
        return rewritten_question
    
    # generate five different versions of the given user question
    def _multi_query(self):
        prompt_perspectives = ChatPromptTemplate.from_template(template=self.config.prompts.rag_multi)
        
        generate_queries = (
            prompt_perspectives 
            | self.llm
            | StrOutputParser() 
            | (lambda x: x.split("\n"))
        )
        return generate_queries

    # only get the unique docs
    def get_unique_union(self, documents):
        flattened_docs = [dumps(doc) for sublist in documents for doc in sublist]
        unique_docs = list(set(flattened_docs)) 
        return [loads(doc) for doc in unique_docs]

    # rerank all documents
    def _reciprocal_rank_fusion(self, results: list[list], k=60):
        fused_scores = {}
        for docs in results:
            for rank, doc in enumerate(docs):
                doc_str = dumps(doc) 
                if doc_str not in fused_scores:
                    fused_scores[doc_str] = 0
                fused_scores[doc_str] += 1 / (rank + k)

        reranked_results = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)

        unique_docs = set()
        final_results = []

        for doc_str, _ in reranked_results:
            doc = loads(doc_str) 
            if doc_str not in unique_docs: 
                unique_docs.add(doc_str)
                final_results.append(doc)

        return final_results  

    # generates multiple sub-questions related to an input question
    def _decompose_question(self, question: str):
        prompt_decomposition = ChatPromptTemplate.from_template(template=self.config.prompts.rag_decompose)
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
    
    # answer multiple sub-questions related to an input question 
    def _answer_sub_questions(self, sub_questions):
        decomposition_prompt = ChatPromptTemplate.from_template(template=self.config.prompts.rag_answer_decompose)

        q_a_pairs_list = [] 

        for q in sub_questions:
            if self.wrap.retriever is None:
                self._create_retriever()

            rag_chain = (
                {"context": lambda x: self.wrap.retriever.get_relevant_documents(x["question"]),  
                "question": lambda x: x["question"],
                "q_a_pairs": lambda x: "\n---\n".join(q_a_pairs_list)}  
                | decomposition_prompt
                | self.llm
                | StrOutputParser()
            )

            answer = rag_chain.invoke({"question": q, "q_a_pairs": "\n---\n".join(q_a_pairs_list)}) 
            q_a_pair = self.format_qa_pair(q, answer)
            q_a_pairs_list.append(q_a_pair) 

        return answer, {"q_a_pairs": "\n---\n".join(q_a_pairs_list)} 

    # generate a step back question related to an input question
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
        if self.wrap.retriever is None:
            self._create_retriever()

        response_prompt = ChatPromptTemplate.from_template(template=self.config.prompts.rag_step_back)

        normal_docs = self.wrap.retriever.get_relevant_documents(question)
        step_back_docs = self.wrap.retriever.get_relevant_documents(step_back_query)
        normal_context_text = "\n\n".join(doc.page_content for doc in normal_docs)
        step_back_context_text = "\n\n".join(doc.page_content for doc in step_back_docs)

        chain = (
            {
                "normal_context": lambda x: normal_context_text,
                "step_back_context": lambda x: step_back_context_text,
                "question": lambda x: x["question"],
            }
            | response_prompt
            | self.llm
            | StrOutputParser()
        )

        response = chain.invoke({"question": question})
        return {
            "response": response,
            "normal_context_docs": normal_docs,
            "step_back_context_docs": step_back_docs
        }

    def _search(self, question):
        import pdb; pdb.set_trace()
        if self.config.feature_config.rerank:
            self._create_retriever()
            self._create_compressor(self.config.rag_config.reranker_type)
            self._create_cretriever(self.config.rag_config.compressor_retriever)
            return self.wrap.cretriever.invoke(question)
        if self.config.feature_config.compressor:
            self._create_retriever()
            self._create_compressor(self.config.rag_config.compressor_type)
            self._create_cretriever(self.config.rag_config.compressor_retriever)
            return self.wrap.cretriever.invoke(question)
        if self.config.rag_config.retriever_type == "similarity_search":
            return self.wrap.vector_store.similarity_search(question)
        
    def retrieve(self, state: State):
        if self.config.feature_config.question_rewriting:
            state["question"] = self.rewrite_question(state["question"])
        if self.config.feature_config.multi_query:
            questions = self._multi_query()
            retrieval_chain = (
                questions
                | self.wrap.vector_store.as_retriever().map()
                | self.get_unique_union
            )
            final_docs = retrieval_chain.invoke({"question": state["question"]})
        if self.config.feature_config.rag_fusion:
            questions = self._multi_query()

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
            _, step_back_context, synthesized_result = self._retrieve_step_back_context(state["question"], step_back_query)
            return {"context": step_back_context, "answer": synthesized_result}

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
        docs_content = "\n\n".join(doc.page_content if hasattr(doc, "page_content") else str(doc) for doc in state["context"])
    
        messages = self.wrap.template.invoke({"question": state["question"], "context": docs_content})
        response = self.llm.invoke(messages)
        if self.config.feature_config.hallucination_grading:
            grounded_content = self.grade_hallucination(state["context"], response)

            if not grounded_content:
                return {
                    "answer": "The response contains no verified factual content.",
                    "suggestion": "Consider refining your query for more accurate results."
                }
        if self.config.feature_config.answer_grading:
            is_relevant = self.grade_answer(state["question"], response)
            if not is_relevant:
                return {
                    "answer": "The response does not directly answer the question.",
                    "suggestion": "Consider rephrasing your question or asking for specific details."
                }
        return {"answer": response.content}
    
    def graph_retrieve(self, query, collection, template):
        chain = GraphCypherQAChain.from_llm(
            self.llm, graph=self.graph, verbose=True, top_k=5, allow_dangerous_requests=True
        )

        result = chain.invoke({"query": query})['result']
        return result
    
    def chain_retrieve(self, query, collection, template, graph_lc=False) -> None:
        self._create_vector(collection=collection)
        self._create_template(template_str=template)
        if graph_lc:
            result = self.graph_legacy.invoke({"question": query})
            return result["answer"]
        else:
            retriever = self.wrap.vector_store.as_retriever()
            rag_chain = (
                {"context": retriever,  "question": RunnablePassthrough()}
                | self.wrap.template
                | self.llm
                | StrOutputParser()
            )
            result = rag_chain.invoke(query)
            return result
        """ state = {"question": query, "context": [], "answer": ""}
        retrieval_result = self.retrieve(state)

        state["context"] = retrieval_result.get("context", [])

        generated_result = self.generate(state)
        return generated_result["answer"] """

    def self_rag_retrieve(self, query, collection, template):
        self._create_vector(collection=collection)
        self._create_template(template_str=template)
        result = self.run_rag_workflow_streamed(query)
        if "error" in result:
            result["answer"] = "The workflow could not generate a valid response."
        return result

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

    def generate_node(self, state: State):
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
        state["recursion_depth"] += 1

        if not filtered_docs:
            print("---NO RELEVANT DOCUMENTS FOUND---")
            
        state["context"] = filtered_docs
        return state

    def transform_query_node(self, state: State):
        state["recursion_depth"] += 1
        print("---TRANSFORM QUERY NODE---")
        question = state["question"]
        rewritten_question = self.rewrite_question(question)
        state["question"] = rewritten_question
        return state

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

    def run_rag_workflow_streamed(self, query):
        print("---STARTING STREAMED GRAPH-BASED RAG WORKFLOW---")
        app = self.build_rag_graph()
        if app is None:
            raise RuntimeError("Graph compilation failed. Cannot proceed with RAG workflow.")

        inputs = {"question": query, "context": [], "answer": "","recursion_depth": 0}

        final_output = None
        for output in app.stream(inputs):
            for key, value in output.items():
                pprint(f"Node '{key}':") 
            final_output = value 
            
        if final_output and "answer" in final_output and final_output["answer"] != '':
            return {"answer": final_output["answer"]}
        elif final_output and "context" in final_output and final_output["context"] != '':
            final_answer = "\n".join(final_output["context"]) + "\n\n"
            return {"answer": final_answer}
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
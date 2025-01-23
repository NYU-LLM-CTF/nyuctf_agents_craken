from database import WeaviateDB, MilvusDB, RAGDatabase, BaseVectorDB
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from langchain.schema.output_parser import StrOutputParser
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from langgraph.graph import START, StateGraph
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.document_compressors.rankllm_rerank import RankLLMRerank
from langchain.load import dumps, loads
from operator import itemgetter

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

class RetrieverWrap:
    def __init__(self) -> None:
        self.retriever = None
        self.compressor = None
        self.cretriever = None
        self.vector_store = None
        self.prompt = None
        self.template = None

class RAGRetrieval:
    def __init__(self, llm=None, config={}) -> None:
        self.llm = llm
        self.config = config
        self.database = RAGDatabase(self._setup_db(self.config.db_config.storage), config=config)
        self.graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph = self.graph_builder.compile()
        self.wrap = RetrieverWrap()

    def _setup_db(self, db_storage):
        if db_storage == "milvus":
            return MilvusDB()
        elif db_storage == "weaviate":
            return WeaviateDB()
        else:
            return MilvusDB

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
    
    def _multi_query(self, question):
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

    def _decompose_question(self, question: str) -> list[str]:
        prompt_decomposition = ChatPromptTemplate.from_template(template=self.config.retrieval_config.template_decompose)
        generate_queries_decomposition = (
            prompt_decomposition
            | self.llm
            | StrOutputParser()
            | (lambda x: x.split("\n"))
        )
        sub_questions = generate_queries_decomposition.invoke({"question": question})
        return sub_questions

    def format_qa_pair(question, answer):
        formatted_string = ""
        formatted_string += f"Question: {question}\nAnswer: {answer}\n\n"
        return formatted_string.strip()
    
    def _answer_sub_questions(self, sub_questions: list[str]) -> dict:
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

    def _generate_step_back_query(self, question: str) -> str:
        examples = [
            {
                "input": "Could the members of The Police perform lawful arrests?",
                "output": "What can the members of The Police do?",
            },
            {
                "input": "Jan Sindel’s was born in what country?",
                "output": "What is Jan Sindel’s personal history?",
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

    def _retrieve_step_back_context(self, question: str, step_back_query: str) -> dict:
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
        if self.config.feature_config.multi_query:
            questions = self._multi_query(state["question"])
            all_docs = []
            for question in questions:
                docs = self._search(question)
                all_docs.extend(docs)
            
            unique_docs = list({doc.page_content: doc for doc in all_docs}.values())
            return {"context": unique_docs}
        if self.config.feature_config.rag_fusion:
            questions = self._multi_query(state["question"])

            queries = questions.invoke({"question": state["question"]})
            results = [self._search(query) for query in queries]
            unique_docs = self._reciprocal_rank_fusion(results)
            return {"context": unique_docs}
        if self.config.feature_config.decomposition:
            sub_questions = self._decompose_question(state["question"])
            answer,q_a_results = self._answer_sub_questions(sub_questions)
            return {"context": q_a_results["q_a_pairs"], "answer": answer}
        if self.config.feature_config.step_back:
            step_back_query = self._generate_step_back_query(state["question"])
            synthesized_result = self._retrieve_step_back_context(state["question"], step_back_query)
            return {"context": synthesized_result["normal_context"], "answer": synthesized_result["step_back_context"]}

        else:
            docs = self._search(state["question"])
            return {"context": docs}

    def generate(self, state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = self.wrap.template.invoke({"question": state["question"], "context": docs_content})
        response = self.llm.invoke(messages)
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
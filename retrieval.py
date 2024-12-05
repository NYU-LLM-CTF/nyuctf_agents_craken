from database import WeaviateDB, MilvusDB, RAGDatabase, BaseVectorDB
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from langgraph.graph import START, StateGraph
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.document_compressors.rankllm_rerank import RankLLMRerank

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

class RAGRetrieval:
    def __init__(self, llm=None, config={}) -> None:
        self.llm = llm
        self.prompt = None
        self.template = None
        self.config = config
        # self.compressor = LLMChainExtractor.from_llm(llm)
        self.database = RAGDatabase(database=MilvusDB() if config.db_config.storage == 'milvus' else WeaviateDB(), config=config)
        self.vector_store = None
        # TODO Set compressors
        self.retreiver = None
        self.compressor = None
        self.compresstion_retriever = None
        self.graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph = self.graph_builder.compile()

    def _create_compressor(self, compressor: str):
        if compressor == "RankLLMRerank":
            if self.config.retrieval_config.reranker_model.startswith("gpt"):
                self.compressor = RankLLMRerank(top_n=3, model="gpt", gpt_model=self.config.retrieval_config.reranker_model)
                return
        if compressor == "LLMChainExtractor":
            self.compressor = LLMChainExtractor.from_llm(self.llm)
            return
        
    def _create_cretriever(self, cretriever: str):
        if cretriever == "ContextualCompressionRetriever":
            self.compresstion_retriever = ContextualCompressionRetriever(
                base_compressor=self.compressor, base_retriever=self.retriever
            )
            return

    def _create_vector(self, collection: str=None):
        if not collection:
            raise ValueError("Please specify a collection")
        self.vector_store = self.database.get_db().create_vector(collection=collection)

    def _create_retriever(self):
        if self.config.feature_config.search_params:
            self.retriever = self.vector_store.as_retriever(self.config.retrieval_config.retriever_search, 
                                                           self.config.retrieval_config.retriever_params)
        else:
            self.retriever = self.vector_store.as_retriever(self.config.retrieval_config.retriever_search) 

    def _create_template(self, template_str: str=None):
        if not template_str:
            raise ValueError("Please specify a prompt template")
        self.prompt = template_str
        self.template = ChatPromptTemplate.from_template(self.prompt)

    def _search(self, question):
        if self.config.retrieval_config.retriever_type == "similarity_search":
            return self.vector_store.similarity_search(question)
        if self.config.feature_config.rerank:
            self._create_retriever(self.vector_store)
            self._create_compressor(self.config.retrieval_config.reranker_type)
            self._create_cretriever(self.config.retrieval_config.compressor_retriever)
            return self.compresstion_retriever.invoke(question)
        if self.config.feature_config.compressor:
            self._create_retriever(self.vector_store)
            self._create_compressor(self.config.retrieval_config.compressor_type)
            self._create_cretriever(self.config.retrieval_config.compressor_retriever)
            return self.compresstion_retriever.invoke(question)

    def retrieve(self, state: State):
        docs = self._search(state["question"])
        return {"context": docs}

    def generate(self, state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = self.template.invoke({"question": state["question"], "context": docs_content})
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
        retriever = self.vector_store.as_retriever()
        rag_chain = (
            {"context": retriever,  "question": RunnablePassthrough()}
            | self.template
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
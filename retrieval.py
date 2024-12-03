from database import RAGDatabase
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_core.documents import Document
from typing_extensions import List, TypedDict
from langgraph.graph import START, StateGraph
from langchain_core.prompts import PromptTemplate
from langchain_community.retrievers import BM25Retriever
from langchain_community.retrievers import (
    WeaviateHybridSearchRetriever,
)


TEST_TEMPLATE = """You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
"""

TESTLLM = ChatOpenAI(model_name="gpt-4o-mini-2024-07-18", temperature=0)

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

class RAGRetrieval:
    def __init__(self, llm=None, prompt_template=None) -> None:
        self.collection = "HFCTF"
        self.llm = llm
        self.prompt = prompt_template
        self.template = ChatPromptTemplate.from_template(self.prompt)
        self.compressor = LLMChainExtractor.from_llm(llm)
        self.database = RAGDatabase()
        self.vector_store = WeaviateVectorStore.from_documents([], OpenAIEmbeddings(), client=self.database.get_db(), index_name=self.collection)
        self.use_compressor = False
        self.graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph = self.graph_builder.compile()

    def set_config(self, **kwargs):
        allowed_keys = {'collection'}
        for key in allowed_keys:
            if key in kwargs:
                setattr(self, key, kwargs[key])   

    def retrieve(self, state: State):
        retrieved_docs = self.vector_store.similarity_search(state["question"])
        return {"context": retrieved_docs}

    def generate(self, state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = self.template.invoke({"question": state["question"], "context": docs_content})
        response = self.llm.invoke(messages)
        return {"answer": response.content}
    
    def graph_retrieve(self, query):
        result = self.graph.invoke({"question": query})
        return result["context"], result["answer"]
    
    def chain_retrieve(self, query) -> None:
        data = WeaviateVectorStore.from_documents([], OpenAIEmbeddings(), client=self.database.get_db(), index_name=self.collection)
        retriever = data.as_retriever()
        rag_chain = (
            {"context": retriever,  "question": RunnablePassthrough()}
            | self.template
            | self.llm
            | StrOutputParser()
        )
        response = rag_chain.invoke(query)
        return response
    
    def close_db(self):
        self.database.close()

if __name__ == "__main__":
    retreval = RAGRetrieval(llm=TESTLLM, prompt_template=TEST_TEMPLATE)
    context, answer = retreval.graph_retrieve("What is decomposition?")
    # answer = retreval.chain_retrieve("What is decomposition?")
    print(answer)
    retreval.close_db()
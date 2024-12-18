import os
import tempfile
from overrides import override
import requests
import datasets
from abc import ABC, abstractmethod
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from pymilvus import connections, Collection, utility
import weaviate
from typing import List, Optional
from langchain_community.vectorstores.utils import DistanceStrategy
import validators
from langchain.docstore.document import Document as LangchainDocument
from tqdm import tqdm
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_milvus import Milvus
from rag_config import RAGConfig
# from langchain.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain.schema.runnable import RunnablePassthrough
# from langchain.schema.output_parser import StrOutputParser

with open("api_keys", "r") as f:
    OPENAI_API_KEY = f.read().strip()
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

TEST_TEMPLATE = """You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
"""

class BaseVectorDB(ABC):
    def __init_subclass__(cls):
        super().__init_subclass__()
    
    def __init__(self) -> None:
        super().__init__()
        self.client = None

    @abstractmethod
    def insert_document(self, documents: List[Document], embeddings, collection: str):
        pass

    @abstractmethod
    def create_vector(self, collection):
        pass
    
    @abstractmethod
    def delete_collection(self, collection: str):
        pass
    
    @abstractmethod
    def create_collection(self, collection: str):
        pass

    @abstractmethod
    def close_db(self):
        pass

class WeaviateDB(BaseVectorDB):
    def __init__(self) -> None:
        super().__init__()
        self.port = 50050
        self.host = "0.0.0.0"
        self.grpc_port = 50051
        self.client = weaviate.connect_to_local(
            host=self.host,
            port=self.port,
            grpc_port=self.grpc_port,
        )
    
    @override
    def insert_document(self, documents: List[Document], embeddings, collection: str):
        if self.client:
            db = WeaviateVectorStore.from_documents(
                documents, embeddings, distance_strategy=DistanceStrategy.COSINE, client=self.client, index_name=collection
            )
    
    @override
    def delete_collection(self, collection: str):
        if self.client:
            self.client.collections.delete(collection)

    @override
    def create_collection(self, collection: str):
        if self.client:
            self.client.collections.create(collection)

    @override
    def create_vector(self, collection):
        return WeaviateVectorStore.from_documents([], OpenAIEmbeddings(), client=self.client, index_name=collection)

    @override
    def close_db(self):
        self.client.close()

class MilvusDB(BaseVectorDB):
    def __init__(self) -> None:
        super().__init__()
        self.host = "0.0.0.0"
        self.port = "19530"
        self.url = "./db/ctfrag.db"

    @override
    def insert_document(self, documents: List[Document], embeddings, collection: str):
        db = Milvus.from_documents(documents, embeddings, connection_args={"host": self.host, "port": self.port}, collection_name=collection)
    
    @override
    def delete_collection(self, collection: str):
        connections.connect("default", host=self.host, port=self.port)
        if utility.has_collection(collection):
            Collection(collection).drop()
            print(f"Collection '{collection}' has been dropped.")
        else:
            print(f"Collection '{collection}' does not exist.")

    @override
    def create_collection(self, collection: str, documents: List[Document] = []):
        pass

    @override
    def create_vector(self, collection):
        return Milvus(OpenAIEmbeddings(), connection_args={"host": self.host, "port": self.port}, collection_name=collection)

    @override
    def close_db(self):
        connections.disconnect("default")

class RAGDatabase:
    def __init__(self, database: BaseVectorDB, config={}) -> None:
        self.vector_db = database
        self.config = config

    def _download_data(self, url=None, path=None) -> None:
        if path:
            res = requests.get(url)
            with open(path, "w") as f:
                f.write(res.text)
                return path
        else:
            fd, path = tempfile.mkstemp()
            try:
                res = requests.get(url)
                with os.fdopen(fd, 'w') as f:
                    f.write(res.text)
                    return path
            finally:
                pass

    def load_file(self, path=None, collection=None, chunk_size=512, overlap=50) -> None:
        is_url = False
        if not path:
            print("Please provide a url for data download.")
            return
        if validators.url(path):
            print("URL Found, start downloading...")
            path = self._download_data(url=path)
            is_url = True
        loader = TextLoader(path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        docs = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()
        self.vector_db.insert_document(docs, embeddings, collection)
        if is_url:
            os.remove(path)

    def load_hf(self, dataset=None, collection=None, 
                chunk_size=512, overlap=50, unique=True, 
                text_col="text", name_col="source") -> None:
        embeddings = OpenAIEmbeddings()
        ds = datasets.load_dataset(dataset, split="train")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        docs_processed = []
        RAW_KNOWLEDGE_BASE = [
            LangchainDocument(page_content=doc[text_col], metadata={"source": doc[name_col]})
            for doc in tqdm(ds)
        ]
        for doc in RAW_KNOWLEDGE_BASE:
            docs_processed += text_splitter.split_documents([doc])
        if unique:
            unique_texts = {}
            docs_processed_unique = []
            for doc in docs_processed:
                if doc.page_content not in unique_texts:
                    unique_texts[doc.page_content] = True
                    docs_processed_unique.append(doc)
        self.vector_db.insert_document(docs_processed_unique if unique else docs_processed, embeddings, collection)
    
    def _readdoc(self, path):
        with open(path, "r") as f:
            text = f.read()
        return text

    def load_dir(self, dir=None, collection=None, 
                 chunk_size=512, overlap=50, unique=True, 
                 recursive=True) -> None:
        if not os.path.isdir(dir):
            print("Please provide a valid directory")
            return
        paths = []
        docs_processed = []
        embeddings = OpenAIEmbeddings()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        if recursive:
            for root, dirs, files in os.walk(dir):
                for filename in files:
                    paths.append(os.path.join(root, filename))
        else:
            for filename in os.listdir(dir):
                paths.append(os.path.join(dir, filename))
        
        RAW_KNOWLEDGE_BASE = [
            LangchainDocument(page_content=self._readdoc(path), metadata={"source": path})
            for path in tqdm(paths)
        ]

        for doc in RAW_KNOWLEDGE_BASE:
            docs_processed += text_splitter.split_documents([doc])
        if unique:
            unique_texts = {}
            docs_processed_unique = []
            for doc in docs_processed:
                if doc.page_content not in unique_texts:
                    unique_texts[doc.page_content] = True
                    docs_processed_unique.append(doc)
        self.vector_db.insert_document(docs_processed_unique if unique else docs_processed, embeddings, collection)

    def load_json(self, collection=None) -> None:
        pass
    
    def get_db(self):
        return self.vector_db

    # def test_query(self, collection=None, query=None):
    #     data = WeaviateVectorStore.from_documents([], OpenAIEmbeddings(), client=self.weaviate_cli, index_name=collection)
    #     retriever = data.as_retriever()
    #     prompt = ChatPromptTemplate.from_template(TEST_TEMPLATE)
    #     llm = ChatOpenAI(model_name="gpt-4o-mini-2024-07-18", temperature=0)
    #     rag_chain = (
    #         {"context": retriever,  "question": RunnablePassthrough()}
    #         | prompt
    #         | llm
    #         | StrOutputParser()
    #     )
    #     response = rag_chain.invoke(query)
    #     return response
        # docs = data.similarity_search(query)
        # for i, doc in enumerate(docs):
        #     print(f"\nDocument {i+1}:")
        #     print(doc.page_content)

if __name__ == "__main__":
    db = RAGDatabase(MilvusDB())
    # db.load_hf(dataset="m-ric/huggingface_doc", collection="HFCTF")
    # db.get_dbwarp().delete_collection('collection_1')
    # db.load_file(path="https://raw.githubusercontent.com/hwchase17/chat-your-data/refs/heads/master/state_of_the_union.txt", collection="TESTFILE")
    # res = db.test_query("HFCTF", "How to create an endpoint?")
    # print(res)
    # db.close()

    ########## Load from directory ################
    path = "./dataset/processed_writeups/"
    db.load_dir(dir=path, collection="WRITEUPS")

    ########## Load from HF #######################
    # db.load_hf(dataset="m-ric/huggingface_doc", collection="HFCTF")
from typing import List
from langchain_core.documents import Document
from .base import BaseVectorDB
from overrides import override
from langchain_openai import OpenAIEmbeddings
from langchain_milvus import Milvus
from pymilvus import connections, Collection, utility

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
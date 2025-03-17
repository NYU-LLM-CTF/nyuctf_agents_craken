from typing import List
from langchain_core.documents import Document
from .base import BaseVectorDB
from overrides import override
from langchain_milvus import Milvus
from pathlib import Path
from pymilvus import connections, Collection, utility

FILE_PATH = Path(__file__).resolve()

class MilvusDB(BaseVectorDB):
    def __init__(self, embeddings, use_server=False) -> None:
        super().__init__(embeddings=embeddings)
        self.host = "0.0.0.0"
        self.port = "19530"
        self.use_server = use_server
        self.url = FILE_PATH.parent / "db" / "ctfrag.db"
        self.url.parent.mkdir(parents=True, exist_ok=True)

    @override
    def insert_document(self, documents: List[Document], collection: str):
        if not self.use_server:
            db = Milvus.from_documents(documents, embedding=self.embeddings, connection_args={"uri": str(self.url)}, collection_name=collection)
        else:
            db = Milvus.from_documents(documents, embedding=self.embeddings, connection_args={"host": self.host, "port": self.port}, collection_name=collection)
    
    @override
    def delete_collection(self, collection: str):
        if not self.use_server:
            vectorstore = Milvus(
                collection_name=collection, 
                connection_args={"uri": str(self.url)}
            )
            if vectorstore.col:
                vectorstore.col.drop()
                print(f"Collection '{collection}' has been dropped.")
            else:
                print(f"Collection '{collection}' does not exist.")
        else:
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
    def create_vector(self, collection, embeddings):
        return Milvus(embeddings, connection_args={"uri": str(self.url)}, collection_name=collection)

    @override
    def close_db(self):
        if self.use_server:
            connections.disconnect("default")
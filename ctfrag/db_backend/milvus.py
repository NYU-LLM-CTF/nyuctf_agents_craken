from typing import List
from langchain_core.documents import Document
from .base import BaseVectorDB
from overrides import override
from langchain_openai import OpenAIEmbeddings
from langchain_milvus import Milvus
from pathlib import Path

FILE_PATH = Path(__file__).resolve()

class MilvusDB(BaseVectorDB):
    def __init__(self, embeddings) -> None:
        super().__init__(embeddings=embeddings)
        self.host = "0.0.0.0"
        self.port = "19530"
        self.url = FILE_PATH.parent / "db" / "ctfrag.db"
        self.url.parent.mkdir(parents=True, exist_ok=True)
        print(self.url.parent)
        self.client = Milvus(connection_args={"uri": str(self.url)}, embedding_function=self.embeddings)

    @override
    def insert_document(self, documents: List[Document], collection: str):
        db = self.client.from_documents(documents, embedding=self.embeddings, collection_name=collection)
        # db = Milvus.from_documents(documents, self.embeddings, connection_args={"uri": str(self.url)}, collection_name=collection)
    
    @override
    def delete_collection(self, collection: str):
        vectorstore = Milvus(
            collection_name=collection, 
            connection_args={"uri": str(self.url)}
        )
        
        if vectorstore.col:
            vectorstore.col.drop()
            print(f"Collection '{collection}' has been dropped.")
        else:
            print(f"Collection '{collection}' does not exist.")

    @override
    def create_collection(self, collection: str, documents: List[Document] = []):
        pass

    @override
    def create_vector(self, collection):
        return Milvus(OpenAIEmbeddings(), connection_args={"uri": str(self.url)}, collection_name=collection)

    @override
    def close_db(self):
        pass
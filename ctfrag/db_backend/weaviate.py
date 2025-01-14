from typing import List, Optional
from langchain_core.documents import Document
from langchain_weaviate.vectorstores import WeaviateVectorStore
from .base import BaseVectorDB
import weaviate
from langchain_community.vectorstores.utils import DistanceStrategy
from overrides import override
from langchain_openai import OpenAIEmbeddings

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
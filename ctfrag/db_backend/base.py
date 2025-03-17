from abc import ABC, abstractmethod
from typing import List, Optional
from langchain_core.documents import Document

class BaseVectorDB(ABC):
    def __init_subclass__(cls):
        super().__init_subclass__()
    
    def __init__(self, embeddings) -> None:
        super().__init__()
        self.client = None
        self.embeddings = embeddings

    @abstractmethod
    def insert_document(self, documents: List[Document], collection: str):
        pass

    @abstractmethod
    def create_vector(self, collection, embeddings):
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
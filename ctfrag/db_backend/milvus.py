from typing import List
from langchain_core.documents import Document
from .base import BaseVectorDB
from overrides import override
from langchain_milvus import Milvus
from pathlib import Path
from uuid import uuid4
from pymilvus import connections, utility, MilvusClient

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
        connection_args = {"uri": str(self.url)} if not self.use_server else {"host": self.host, "port": self.port}
        has_collection = False
        uuids = [str(uuid4()) for _ in range(len(documents))]
        if not self.use_server:
            client = MilvusClient(uri=str(self.url))
            has_collection = client.has_collection(collection)
        else:
            connections.connect(host=self.host, port=self.port)
            has_collection = utility.has_collection(collection)
        if has_collection:
            db = Milvus(embedding_function=self.embeddings, collection_name=collection,
                         connection_args=connection_args, index_params={"index_type": "FLAT", "metric_type": "L2"}, consistency_level="Strong")
            db.add_documents(documents=documents, ids=uuids)
        else:
            if not self.use_server:
                db = Milvus.from_documents(documents, embedding=self.embeddings, 
                                        connection_args={"uri": str(self.url)}, collection_name=collection, 
                                        index_params={"index_type": "FLAT", "metric_type": "L2"}, ids=uuids, consistency_level="Strong")
            else:
                db = Milvus.from_documents(documents, embedding=self.embeddings, 
                                        connection_args={"host": self.host, "port": self.port}, 
                                        collection_name=collection, ids=uuids, consistency_level="Strong")

    @override
    def delete_collection(self, collection: str):
        try:
            if not self.use_server:
                connection_args = {"uri": str(self.url)}
            else:
                connection_args = {"host": self.host, "port": self.port}
            if utility.has_collection(collection_name=collection, **connection_args):
                vectorstore = Milvus(
                    collection_name=collection,
                    connection_args=connection_args
                )
                vectorstore.col.drop()
                print(f"Collection '{collection}' has been dropped.")
            else:
                print(f"Collection '{collection}' does not exist.")
        except Exception as e:
            print(f"Error dropping collection '{collection}': {e}")
    

    @override
    def create_collection(self, collection: str):
        pass

    @override
    def create_vector(self, collection, embeddings):
        if self.use_server:
            return Milvus(embeddings, connection_args={"host": self.host, "port": self.port}, 
                          collection_name=collection)
        else:
            return Milvus(embeddings, connection_args={"uri": str(self.url)}, 
                        collection_name=collection, index_params={"index_type": "FLAT", "metric_type": "L2"})

    @override
    def close_db(self):
        if self.use_server:
            connections.disconnect("default")
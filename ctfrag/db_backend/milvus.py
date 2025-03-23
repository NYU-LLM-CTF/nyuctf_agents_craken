from typing import List
from langchain_core.documents import Document
from .base import BaseVectorDB
from overrides import override
from langchain_milvus import Milvus
from pathlib import Path
from uuid import uuid4
from pymilvus import connections, utility, MilvusClient, Collection

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
            connection_args = {"uri": str(self.url)} if not self.use_server else {"host": self.host, "port": self.port}
            has_collection = False
            if not self.use_server:
                client = MilvusClient(uri=str(self.url))
                has_collection = client.has_collection(collection)
            else:
                connections.connect(host=self.host, port=self.port)
                has_collection = utility.has_collection(collection)
            if not has_collection:
                print(f"Collection '{collection}' doesn't exist. Nothing to delete.")
                return False
            if not self.use_server:
                result = client.drop_collection(collection_name=collection)
                client.close()
            else:
                utility.drop_collection(collection)
                connections.disconnect(alias="default")
                
            print(f"Collection '{collection}' has been successfully deleted.")
            return True
        except Exception as e:
            print(f"Error deleting collection '{collection}': {str(e)}")
            if not self.use_server and 'client' in locals():
                client.close()
            elif self.use_server:
                connections.disconnect(alias="default")
            return False
            

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

    @override
    def view_samples(self, collection, limit, truncate=500):
        try:
            client = None
            if not self.use_server:
                client = MilvusClient(uri=str(self.url))
                has_collection = client.has_collection(collection)
            else:
                connections.connect(host=self.host, port=self.port)
                has_collection = utility.has_collection(collection)
            
            if has_collection:
                if not self.use_server:
                    results = client.query(
                        collection_name=collection,
                        filter="",
                        output_fields=["*"],
                        limit=limit
                    )
                else:
                    collection_obj = Collection(collection)
                    results = collection_obj.query(expr="", output_fields=["*"], limit=5)
                
                print(f"\nFound {len(results)} documents in collection '{collection}':")
                print("=" * 80)
                
                for i, doc in enumerate(results):
                    print(f"\n📄 Document {i+1}:")
                    print("-" * 50)
                    
                    for key, value in doc.items():
                        if key == "vector" or key == "embeddings":
                            print(f"  📊 {key}: [Vector data - {len(value)} dimensions]")
                        elif key == "text" and isinstance(value, str):
                            if truncate > 0:
                                preview = value[:truncate] + "..." if len(value) > truncate else value
                            else:
                                preview = value
                            print(f"  📝 {key}:")
                            for line in preview.split('\n'):
                                print(f"     {line}")
                            print(f"     [Total text length: {len(value)} characters]")
                        elif key == "source" and isinstance(value, str):
                            print(f"  📂 {key}: {value}")
                        elif key == "pk" or key == "id":
                            print(f"  🔑 {key}: {value}")
                        else:
                            if isinstance(value, str) and len(value) > 100:
                                value_display = value[:100] + "..."
                            else:
                                value_display = value
                            print(f"  🔑 {key}: {value_display}")
                    
                    print("-" * 50)
                
                print("\n" + "=" * 80)
            else:
                print(f"❌ Collection '{collection}' does not exist")
                
        except Exception as e:
            print(f"❌ Error viewing samples from collection '{collection}': {str(e)}")
            
        finally:
            # Clean up connections
            if not self.use_server and client:
                client.close()
            elif self.use_server:
                connections.disconnect(alias="default")
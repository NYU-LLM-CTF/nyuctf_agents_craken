from typing import List
from langchain_core.documents import Document
from .base import BaseVectorDB
from overrides import override
from neo4j import GraphDatabase
from langchain_neo4j import Neo4jGraph
import json
import time
import numpy as np

from langchain_community.graphs.graph_document import GraphDocument

class Neo4jDB(BaseVectorDB):
    def __init__(self, embeddings) -> None:
        super().__init__(embeddings=embeddings)
        self.uri = "neo4j://localhost:7687"
        self.user = "neo4j"
        self.password = "password"
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    @override
    def insert_document(self, documents: List[Document], collection: str):
        graph_store = Neo4jGraph(url=self.uri, username=self.user, password=self.password, database=collection)
        graph_store.add_graph_documents(documents, baseEntityLabel=True, include_source=True)
        # import pdb; pdb.set_trace()

    # @override
    def insert_embeddings_from_documents(self, documents: List[Document], collection: str):
        print(f"⏳ Inserting embeddings for {len(documents)} documents into collection '{collection}'")

        # Step 1: Compute embeddings
        texts = [doc.page_content for doc in documents]
        embeddings = self.embeddings.embed_documents(texts)

        # Step 2: Update nodes in Neo4j
        with self.driver.session(database=collection) as session:
            for doc, embedding in zip(documents, embeddings):
                text = doc.page_content
                if isinstance(embedding, np.ndarray):
                    embedding = embedding.tolist()

                # Matching exactly on `text` field
                session.run(
                    """
                    MATCH (d:Document)
                    WHERE d.text = $text
                    SET d.embedding = $embedding
                    """,
                    {
                        "text": text,
                        "embedding": embedding
                    }
                )

        print("✅ Embeddings inserted into graph.")



    @override
    def delete_collection(self, collection: str):
        """Delete all nodes and relationships under a specific collection."""
        with self.driver.session(database=collection) as session:
            query = """
            MATCH (n)
            DETACH DELETE n
            """
            session.run(query)
            print(f"✅ Collection '{collection}' deleted successfully.")

    @override
    def create_collection(self, collection: str, documents: List[Document] = []):
        """Create a new collection."""
        if documents:
            self.insert_document(documents, collection)
        print(f"✅ Collection '{collection}' created.")

    def index_graph(self, collection: str):
        """
        Creates an index on the populated graph tp assist with efficient searches
        """
        # self.graph.query(
        with self.driver.session(database=collection) as session:
            query = """CREATE FULLTEXT INDEX entity IF NOT EXISTS FOR (e:__Entity__) ON EACH [e.id]"""
            session.run(query)

    # @override
    # def create_vector(self, collection: str):
    #     pass

    @override
    def create_vector(self, collection, embeddings):
        """Return an object that allows query over the Neo4j graph."""
        return Neo4jDB(embeddings)
    
    def create_graph(self, collection):
        return Neo4jGraph(url=self.uri, username=self.user, password=self.password, database=collection)

    @override
    def close_db(self):
        """Close the Neo4j connection."""
        self.driver.close()
        print("✅ Neo4j connection closed.")

    @override
    def view_samples(self, collection, limit):
        pass
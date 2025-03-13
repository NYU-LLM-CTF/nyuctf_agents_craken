from typing import List
from langchain_core.documents import Document
from .base import BaseVectorDB
from overrides import override
from neo4j import GraphDatabase
import json

class Neo4jDB(BaseVectorDB):
    def __init__(self, embeddings) -> None:
        super().__init__(embeddings=embeddings)
        self.uri = "neo4j://localhost:7687"
        self.user = "neo4j"
        self.password = "password"
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    @override
    def insert_document(self, documents: List[Document], collection: str):
        """Insert entities and relationships into Neo4j."""
        with self.driver.session(database=collection) as session:
            for doc in documents:
                content = doc.page_content
                
                # Assuming `content` contains extracted entities and relationships
                # data = eval(content)  # Convert string to dict

                # Assuming `content` contains extracted entities and relationships as JSON string
                try:
                    data = json.loads(content)
                except json.JSONDecodeError:
                    print("Invalid JSON format in document.")
                    continue

                entities = data.get("entities", [])
                relationships = data.get("relationships", [])

            # Insert entities
            for entity in entities:
                query = f"""
                MERGE (n:{entity['type']} {{name: $name}})
                """
                session.run(query, name=entity["name"])

            # Insert relationships
            for relation in relationships:
                query = f"""
                MATCH (a {{name: $source}}), (b {{name: $target}})
                MERGE (a)-[:{relation['relation']}]->(b)
                """
                session.run(query, source=relation["source"], target=relation["target"])

                print(f"✅ Inserted document into collection '{collection}'.")

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

    # @override
    # def create_vector(self, collection: str):
    #     pass

    @override
    def create_vector(self, collection):
        """Return an object that allows query over the Neo4j graph."""
        return Neo4jDB()

    @override
    def close_db(self):
        """Close the Neo4j connection."""
        self.driver.close()
        print("✅ Neo4j connection closed.")


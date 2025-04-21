from ctfrag.algorithms.base import RAGAlgorithms, RetrieverWrap
from ctfrag.database import RAGDatabase
from ctfrag.config import RetrieverConfig
from ctfrag.backends import LLMs

from langchain_community.vectorstores import Neo4jVector
from langchain_community.vectorstores.neo4j_vector import remove_lucene_chars
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from typing import List

class Entities(BaseModel):
    """
    Identify and capture information about entities from text
    """

    names: List[str] = Field(
        description=
            "All the cyber security-related entities that appear in the text",
    )

class GraphRAG(RAGAlgorithms):
    def __init__(self, config: RetrieverConfig, llm: LLMs, wrap: RetrieverWrap, database: RAGDatabase, embeddings):
        super().__init__(config, llm, wrap, database, embeddings)
        if self.config.db_config.storage == "neo4j":
            self.graph = self.database.get_db().create_graph(self.config.rag_config.collection)
        else:
            # We don't use graph rag
            self.graph = None

    def create_entity_extract_chain(self):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are extracting cyber security-related entities from the text.",
                ),
                (
                    "human",
                    "Use the given format to extract information from the following "
                    "input: {question}",
                ),
            ]
        )

        entity_extract_chain = prompt | self.llm().with_structured_output(Entities)
        return entity_extract_chain
    
    def structured_retriever(self, question, collection) -> str:
        self.database.get_db().index_graph(collection)

        entity_extract_chain = self.create_entity_extract_chain()
        result = ""
        entities = entity_extract_chain.invoke({"question": question})
        for entity in entities.names:
            response = self.graph.query(
                """CALL db.index.fulltext.queryNodes('entity', $query, {limit: 2})
                YIELD node, score
                CALL (node) {
                    WITH node
                    MATCH (node)-[r]->(neighbor)
                    RETURN node.id + ' - ' + type(r) + ' -> ' + neighbor.id AS output
                    
                    UNION ALL
                    
                    WITH node
                    MATCH (node)<-[r]-(neighbor)
                    RETURN neighbor.id + ' - ' + type(r) + ' -> ' + node.id AS output
                }
                RETURN output
                LIMIT 50""",
                {"query": self.generate_full_text_query(entity)},
            )
            result += "\n".join([el['output'] for el in response])
        return result
    
    def create_vector_index(self, collection) -> Neo4jVector:
        vector_index = Neo4jVector.from_existing_graph(
            self.embeddings,
            search_type="hybrid",
            node_label="Document",
            text_node_properties=["text"],
            embedding_node_property="embedding",       # Property used for vector search
            url="bolt://localhost:7687",               # Explicit connection URI
            username="neo4j",
            password="password",
            index_name=collection                 # Collection/Index name
        )
        return vector_index
    
    def retriever(self, question, collection) -> str:
        vector_index = self.create_vector_index(collection)
        unstructured_data = [el.page_content for el in vector_index.similarity_search(question)]
        structured_data = self.structured_retriever(question, collection)
        final_data = f"""Structured data:
            {structured_data}
            Unstructured data:
            {"#Document ". join(unstructured_data)}
        """
        return final_data, unstructured_data
    
    def create_search_query(self, chat_history: list, question: str) -> str:
        search_query = ChatPromptTemplate.from_messages([
            (
                "system",
                """Given the following conversation and a follow up question, rephrase the follow 
                up question to be a standalone question, in its original language.
                Chat History:
                {chat_history}
                Follow Up Input: {question}
                Standalone question:"""
            )
        ])
        formatted_query = search_query.format(
            chat_history=chat_history, question=question)
        return formatted_query

    def generate_full_text_query(self, input_query):
        # Clean the query using Neo4j-specific cleaning function
        words = [el for el in remove_lucene_chars(input_query).split() if el]

        if not words:
            return ""
        
        # Apply similarity threshold and combine using AND operator
        full_text_query = " AND ".join(f"{word}~2" for word in words)
        return full_text_query.strip()
    

    def graph_retrieve(self, query, collection):
        template = """Answer the question based only on the following context:
        {context}

        Question: {question}
        Use natural language and be concise.
        Answer:"""
        prompt = ChatPromptTemplate.from_template(template)

        chain = (
            RunnableParallel(
                {
                    "context": lambda x: self.retriever(query, collection)[0],
                    "question": RunnablePassthrough(),
                }
            )
            | prompt
            | self.llm()
            | StrOutputParser()
        )

        response = chain.invoke({"question": query})
        return response
from ctfrag.algorithms.base import RAGAlgorithms, RetrieverWrap
from ctfrag.database import RAGDatabase
from ctfrag.config import RetrieverConfig
from ctfrag.backends import LLMs
from langchain_neo4j import GraphCypherQAChain

class GraphRAG(RAGAlgorithms):
    def __init__(self, config: RetrieverConfig, llm: LLMs, wrap: RetrieverWrap, database: RAGDatabase, embeddings):
        super().__init__(config, llm, wrap, database, embeddings)
        if self.config.db_config.storage == "neo4j":
            self.graph = self.database.get_db().create_graph()
        else:
            # We don't use graph rag
            self.graph = None

    def graph_retrieve(self, query):
        chain = GraphCypherQAChain.from_llm(
            self.llm(), graph=self.graph, verbose=True, top_k=5, allow_dangerous_requests=True
        )

        result = chain.invoke({"query": query})['result']
        return result
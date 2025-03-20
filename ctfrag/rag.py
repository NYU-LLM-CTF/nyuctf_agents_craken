from ctfrag.database import RAGDatabase
from ctfrag.db_backend.milvus import MilvusDB
from ctfrag.db_backend.neo4j import Neo4jDB
from ctfrag.config import RetrieverConfig
from ctfrag.algorithms.base import RetrieverWrap
from ctfrag.algorithms.classic_rag import ClassicRAG
from ctfrag.algorithms.selfrag import SelfRAG
from ctfrag.algorithms.graphrag import GraphRAG


class RAGAgent:
    def __init__(self, llm=None, embeddings=None, config:RetrieverConfig=None) -> None:
        self.llm = llm
        self.embeddings = embeddings
        self.config = config
        self.database = RAGDatabase(self._setup_db(self.config.db_config.storage), config=config)
        self.wrap = RetrieverWrap()
        self.classic_rag = ClassicRAG(config=self.config, llm=self.llm, wrap=self.wrap, database=self.database, embeddings=self.embeddings)
        self.self_rag = SelfRAG(config=self.config, llm=self.llm, wrap=self.wrap, database=self.database, embeddings=self.embeddings)
        self.graph_rag = GraphRAG(config=self.config, llm=self.llm, wrap=self.wrap, database=self.database, embeddings=self.embeddings)

    def _setup_db(self, db_storage):
        if db_storage == "milvus":
            return MilvusDB(embeddings=self.embeddings)
        elif db_storage == "neo4j":
            return Neo4jDB(embeddings=self.embeddings)
        else:
            return MilvusDB(embeddings=self.embeddings)
        
    def do_selfrag(self, query, collection):
        answer = self.self_rag.self_rag_retrieve(query, collection, self.config.prompts.rag_main)["answer"]
        return answer

    def do_rag(self, query, collection):
        answer = self.classic_rag.chain_retrieve(query, collection, self.config.prompts.rag_main)
        return answer

    def do_graphrag(self, query):
        answer = self.graph_rag.graph_retrieve(query)
        return answer
        
    def close_db(self):
        self.database.get_db().close_db()

    def print_docs(self, docs):
        print(
            f"\n{'-' * 100}\n".join(
                [f"Document {i+1}:\n\n" + d.page_content for i, d in enumerate(docs)]
            )
        )

if __name__ == "__main__":
    pass
    # retreval = RAGRetrieval(llm=TESTLLM, prompt_template=TEST_TEMPLATE, db_warp=MilvusDB())
    # context, answer = retreval.graph_retrieve("What is decomposition?")
    # # answer = retreval.chain_retrieve("What is decomposition?")
    # print(answer)
    # retreval.close_db()
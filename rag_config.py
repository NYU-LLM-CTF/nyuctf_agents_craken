import yaml
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    storage: str
    index_type: str
    metric_type: str

@dataclass
class AgentConfig:
    model_type: str
    model_name: str
    model_temperature: str

@dataclass
class RetrievalConfig:
    reranker_type: str
    reranker_model: str
    reranker_top_n: int
    reranker_threshold: float
    compressor_type: str
    compressor_retriever: str
    compressor_parameters: dict
    retriever_type: str
    retriever_search: str
    retriever_params: dict
    template_qa: str
    collection: str

@dataclass
class FeatureConfig:
    rerank: bool
    compressor: bool
    search_params: bool

DEFAULT_TEMPATE = """
You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
"""

class RAGConfig:
    def __init__(self, config_path):
        self.config_yaml = self._load_config(config_path)
        self.db_config = DatabaseConfig(
            storage=self.config_yaml.get("database", {}).get("storage", "milvus"),
            index_type=self.config_yaml.get("database", {}).get("config", {}).get("index_type", "IVF_FLAT"),
            metric_type=self.config_yaml.get("database", {}).get("config", {}).get("metric_type", "L2")
        )
        self.agent_config = AgentConfig(
            model_type=self.config_yaml.get("agent", {}).get("model", {}).get("type", "openai"),
            model_name=self.config_yaml.get("agent", {}).get("model", {}).get("name", "gpt-4o-mini-2024-07-18"),   
            model_temperature=self.config_yaml.get("agent", {}).get("model", {}).get("temperature", 0)
        )
        self.retrieval_config = RetrievalConfig(
            reranker_type=self.config_yaml.get("retrieval", {}).get("reranker", {}).get("type", "RankLLMRerank"),
            reranker_model=self.config_yaml.get("retrieval", {}).get("reranker", {}).get("model", "gpt-4o-mini-2024-07-18"),
            reranker_top_n=self.config_yaml.get("retrieval", {}).get("reranker", {}).get("top_n", 3),
            reranker_threshold=self.config_yaml.get("retrieval", {}).get("reranker", {}).get("threshold", 0.3),
            compressor_type=self.config_yaml.get("retrieval", {}).get("compressor", {}).get("type", "LLMChainExtractor"),
            compressor_retriever=self.config_yaml.get("retrieval", {}).get("compressor", {}).get("retriever", "ContextualCompressionRetriever"),
            compressor_parameters=self.config_yaml.get("retrieval", {}).get("compressor", {}).get("parameters", {"max_length": 256}),
            retriever_type=self.config_yaml.get("retrieval", {}).get("retriever", {}).get("type", "similarity_search"),
            retriever_search=self.config_yaml.get("retrieval", {}).get("retriever", {}).get("search_type", "similarity"),
            retriever_params=self.config_yaml.get("retrieval", {}).get("retriever", {}).get("params", {"k": 20, "ef": 30}),
            template_qa=self.config_yaml.get("retrieval", {}).get("template", {}).get("qa", DEFAULT_TEMPATE),
            collection=self.config_yaml.get("retrieval", {}).get("collection", None)
        )
        self.feature_config = FeatureConfig(
            rerank=self.config_yaml.get("features", {}).get("rerank", False),
            compressor=self.config_yaml.get("features", {}).get("compressor", False),
            search_params=self.config_yaml.get("features", {}).get("search_params", False)
        )
    
    def _load_config(self, path):
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        return config
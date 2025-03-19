import yaml
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    storage: str
    index_type: str
    metric_type: str
    embeddings: str

@dataclass
class AgentConfig:
    model_name: str
    model_temperature: str

@dataclass
class RAGConfig:
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
    collection: str
    template_rag: str
    template_search: str
    template_extract: str

@dataclass
class PromptConfig:
    rag_main: str
    rag_multi: str
    rag_decompose: str
    rag_answer_decompose: str
    rag_step_back_system: str
    rag_step_back_response: str
    rag_step_back_inputs: list[str]
    rag_step_back_outputs: list[str]
    rag_retrieval_grading: str
    rag_hallucination_grading: str
    rag_answer_grading: str
    rag_question_rewriting: str
    search_main: str
    search_filtering: str
    search_summary: str
    search_summary_long: str
    search_evaluation: str
    extract_context_to_task: str
    extract_task_to_question: str
    extract_question_evaluation: str
    extract_answer_evaluation: str
    extract_w_task_q: str
    extract_w_task_e: str
    extract_wo_task_t: str
    extract_wo_task_q: str
    extract_wo_task_e: str

@dataclass
class FeatureConfig:
    rerank: bool
    compressor: bool
    search_params: bool
    multi_query: bool
    rag_fusion: bool
    decomposition: bool
    step_back: bool
    retrieval_grading: bool
    hallucination_grading: bool
    answer_grading: bool
    question_rewriting: bool

DEFAULT_TEMPATE = """
You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
"""

class RetrieverConfig:
    def __init__(self, config_path):
        self.config_path = Path(config_path)
        self.config_yaml = self._load_config(config_path)
        self.db_config = DatabaseConfig(
            storage=self.config_yaml.get("database", {}).get("storage", "milvus"),
            # TODO implement
            index_type=self.config_yaml.get("database", {}).get("config", {}).get("index_type", "IVF_FLAT"),
            # TODO implement
            metric_type=self.config_yaml.get("database", {}).get("config", {}).get("metric_type", "L2"),
            embeddings=self.config_yaml.get("database", {}).get("embeddings", "openai")
        )
        self.agent_config = AgentConfig(
            model_name=self.config_yaml.get("agent", {}).get("model", {}).get("name", "gpt-4o-mini-2024-07-18"),   
            model_temperature=self.config_yaml.get("agent", {}).get("model", {}).get("temperature", 0)
        )
        self.rag_config = RAGConfig(
            reranker_type=self.config_yaml.get("retrieval", {}).get("reranker", {}).get("type", "RankLLMRerank"),
            reranker_model=self.config_yaml.get("retrieval", {}).get("reranker", {}).get("model", "gpt-4o-mini-2024-07-18"),
            reranker_top_n=self.config_yaml.get("retrieval", {}).get("reranker", {}).get("top_n", 3),
            # TODO implement
            reranker_threshold=self.config_yaml.get("retrieval", {}).get("reranker", {}).get("threshold", 0.3),
            compressor_type=self.config_yaml.get("retrieval", {}).get("compressor", {}).get("type", "LLMChainExtractor"),
            compressor_retriever=self.config_yaml.get("retrieval", {}).get("compressor", {}).get("retriever", "ContextualCompressionRetriever"),
            # TODO implement
            compressor_parameters=self.config_yaml.get("retrieval", {}).get("compressor", {}).get("parameters", {"max_length": 256}),
            retriever_type=self.config_yaml.get("retrieval", {}).get("retriever", {}).get("type", "similarity_search"),
            retriever_search=self.config_yaml.get("retrieval", {}).get("retriever", {}).get("search_type", "similarity"),
            retriever_params=self.config_yaml.get("retrieval", {}).get("retriever", {}).get("params", {"k": 20, "ef": 30}),
            collection=self.config_yaml.get("retrieval", {}).get("collection", None),
            template_rag=self.config_yaml.get("retrieval", {}).get("template", {}).get("rag", "prompts/rag.yaml"),
            template_search=self.config_yaml.get("retrieval", {}).get("template", {}).get("search", "prompts/search.yaml"),
            template_extract=self.config_yaml.get("retrieval", {}).get("template", {}).get("extract", "prompts/extract.yaml"),
        )
        self.feature_config = FeatureConfig(
            rerank=self.config_yaml.get("features", {}).get("rerank", False),
            compressor=self.config_yaml.get("features", {}).get("compressor", False),
            search_params=self.config_yaml.get("features", {}).get("search_params", False),
            multi_query=self.config_yaml.get("features", {}).get("multi_query", False),
            rag_fusion=self.config_yaml.get("features", {}).get("rag_fusion", False),
            decomposition=self.config_yaml.get("features", {}).get("decomposition", False),
            step_back=self.config_yaml.get("features", {}).get("step_back", False),
            retrieval_grading=self.config_yaml.get("features", {}).get("retrieval_grading", False),
            hallucination_grading=self.config_yaml.get("features", {}).get("hallucination_grading", False),
            answer_grading=self.config_yaml.get("features", {}).get("answer_grading", False),
            question_rewriting=self.config_yaml.get("features", {}).get("question_rewriting", False)
        )
        self.load_prompts()
    
    def load_prompts(self):
        config_d = self.config_path.parent
        rag_prompts = config_d / self.rag_config.template_rag
        search_prompts = config_d / self.rag_config.template_search
        extract_prompts = config_d / self.rag_config.template_extract
        rag_prompts_cfg = self._load_config(rag_prompts)
        search_prompts_cfg = self._load_config(search_prompts)
        extract_prompts_cfg = self._load_config(extract_prompts)

        self.prompts = PromptConfig(
            rag_main=rag_prompts_cfg.get("rag", DEFAULT_TEMPATE),
            rag_multi=rag_prompts_cfg.get("multi_query", ""),
            rag_decompose=rag_prompts_cfg.get("decompose_query", ""),
            rag_answer_decompose=rag_prompts_cfg.get("answer_decompose_query", ""),
            rag_step_back_system=rag_prompts_cfg.get("step_back", {}).get("step_back_system", ""),
            rag_step_back_response=rag_prompts_cfg.get("step_back", {}).get("step_back_response", ""),
            rag_step_back_inputs=rag_prompts_cfg.get("step_back", {}).get("example_inputs", [""]),
            rag_step_back_outputs=rag_prompts_cfg.get("step_back", {}).get("example_outputs", [""]),
            rag_retrieval_grading=rag_prompts_cfg.get("retrieval_grading", ""),
            rag_hallucination_grading=rag_prompts_cfg.get("hallucination_grading", ""),
            rag_answer_grading=rag_prompts_cfg.get("answer_grading", ""),
            rag_question_rewriting=rag_prompts_cfg.get("question_rewriting", ""),
            search_main=search_prompts_cfg.get("search", ""),
            search_filtering=search_prompts_cfg.get("filtering", ""),
            search_summary=search_prompts_cfg.get("summary", ""),
            search_summary_long=search_prompts_cfg.get("summary_long", ""),      
            search_evaluation=search_prompts_cfg.get("evaluation", ""),
            extract_context_to_task=extract_prompts_cfg.get("context_to_task", ""),
            extract_task_to_question=extract_prompts_cfg.get("task_to_question", ""),
            extract_question_evaluation=extract_prompts_cfg.get("question_evaluation", ""),
            extract_answer_evaluation=extract_prompts_cfg.get("answer_evaluation", ""),
            extract_w_task_q=extract_prompts_cfg.get("fallback_with_task", {}).get("question", ""),
            extract_w_task_e=extract_prompts_cfg.get("fallback_with_task", {}).get("evaluation", ""),
            extract_wo_task_t=extract_prompts_cfg.get("fallback_no_task", {}).get("task", ""),
            extract_wo_task_q=extract_prompts_cfg.get("fallback_no_task", {}).get("question", ""),
            extract_wo_task_e=extract_prompts_cfg.get("fallback_no_task", {}).get("evaluation", "")
        )

    def _load_config(self, path):
        with open(path, 'r') as file:
            config = yaml.safe_load(file)
        return config
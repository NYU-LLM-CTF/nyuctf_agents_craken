import os
import argparse
from pathlib import Path
from ctfrag.rag import RAGAgent
from ctfrag.config import RetrieverConfig
from ctfrag.decomposer import ContextDecomposer
from ctfrag.backends import LLMs, EmbeddingModel
from ctfrag.search import WebSearch
from ctfrag.utils import load_api_keys
from ctfrag.console import console, ConsoleType, log
import warnings
warnings.filterwarnings("ignore")
# warnings.simplefilter("ignore", category=DeprecationWarning)
# warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)
# warnings.filterwarnings("ignore")

class RetrieverManager:
    def __init__(self, api_key=None, config: RetrieverConfig={}) -> None:
        self.config = config
        self.api_key = load_api_keys(api_key)
        self.model = self.config.agent_config.model_name
        self.llm = LLMs(model=self.model, config={"temperature": self.config.agent_config.model_temperature})
        self.embeddings = EmbeddingModel(self.config.db_config.embeddings)()
        self.retrieval_alg = RAGAgent(llm=self.llm, embeddings=self.embeddings, config=self.config)
        self.web_search = WebSearch(llm=self.llm, config=self.config, verbose=True, search_engine="hybrid")
        self.extractor = ContextDecomposer(self.llm, config=self.config)
        self.history = []
        self.enabled = False

    def quiet_mode(self):
        console.quiet = True
    
    def enable_retriever(self):
        self.enabled = True

    def summarize_context(self, context):
        decomposition = self.extractor.decompose_task(context)
        return {
            "task": decomposition.task,
            "query": decomposition.query,
            "keywords": decomposition.keywords
        }

    def rag_generate(self, query):
        with console.overlay_session() as o:
            if self.config.rag_config.algorithm == "graph":
                answer = self.retrieval_alg.do_graphrag(query, self.config.rag_config.collection)
            elif self.config.rag_config.algorithm == "self_rag":
                answer = self.retrieval_alg.do_selfrag(query, self.config.rag_config.collection)
            else:
                answer = self.retrieval_alg.do_rag(query, self.config.rag_config.collection)
            self.history.append({
                "query": query,
                "collection": self.config.rag_config.collection,
                "answer": answer
            })
            console.overlay_print(f"Retrieval Result: {answer}", ConsoleType.OUTPUT)
            # print(f"Cost: {round(self.llm.get_cost(), 2)}")
            return answer
        
    def get_cost(self):
        return self.llm.get_cost()
    
    def do_web_search(self, query):
        with console.overlay_session() as o:
            result = self.web_search.search_web(query)
            console.overlay_print(result.content, ConsoleType.OUTPUT)
            return result.content
        
    def init_log(self, progress):
        console.set_progress(progress)
        
    def append_log(self):
        return log.get_retriever_logs(self.config)

    
if __name__ == "__main__":
    load_api_keys(key_cfg=Path(__file__).resolve().parent.parent.parent / "keys.cfg")
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", default=Path(__file__).resolve().parent.parent / "config/rag_config.yaml", type=str, help="config path")
    args = parser.parse_args()
    agent = RetrieverManager(config=RetrieverConfig(config_path=args.config))
    # # response = agent.summarize_context(info=TEST_CONTEXT)
    # # print(response)
    result = agent.rag_generate("how to reverse")
    #result = agent.do_web_search(r"How to write a good scientific paper?")
    # answer = agent.rag_generate("Explain buffer overflow with detailed steps", mode="graph", collection="ctfrag101")
    print(result)
    # answer = agent.rag_generate("How to reverser?", mode="rag", collection="default")
    # # context, answer = agent.rag_generate("Find any writeups for me, give me the database name and divide it into steps", collection="writeups")
    # # context, answer = agent.rag_generate(response, collection="HFCTF")
    # # context, answer = agent.rag_generate("What is decomposition", collection="HFCTF")
    # print(answer)
    #task_example = "Analyze Tesla's 2022 financial statements, extract key financial metrics, and compare them with industry standards"
    # task_example = "Explain Buffer Overflow with detailed steps?" #"How to reverse?"
    # task_result, fcost = agent.summarize_context(task_example)
    # for i, q in enumerate(task_result, 0):
    #     # answer = agent.rag_generate(task_result[i]['question'], mode="self_rag", collection="writeups")
    #     answer = agent.rag_generate(task_result[i]['question'], mode="graph", collection="ctfrag101")
    #     print(task_result[i]['question'] + "\n" + answer + "\n\n")
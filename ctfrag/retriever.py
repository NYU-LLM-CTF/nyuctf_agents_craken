import os
import argparse
from pathlib import Path
from ctfrag.rag import RAGAgent
from ctfrag.config import RetrieverConfig
from ctfrag.extractor import QuestionExtractor
from ctfrag.backends import LLMs, EmbeddingModel
from ctfrag.search import WebSearch
from ctfrag.utils import load_api_keys
from ctfrag.console import console
import warnings
warnings.filterwarnings("ignore")
# warnings.simplefilter("ignore", category=DeprecationWarning)
# warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)
# warnings.filterwarnings("ignore")

class RetrieverManager:
    def __init__(self, api_key=None, config: RetrieverConfig={}) -> None:
        self.config = config
        self.api_key = api_key
        self.model = self.config.agent_config.model_name
        self.llm = LLMs(model=self.model, config={"temperature": self.config.agent_config.model_temperature})()
        self.embeddings = EmbeddingModel(self.config.db_config.embeddings)()
        self.retrieval_alg = RAGAgent(llm=self.llm, embeddings=self.embeddings, config=self.config)
        self.web_search = WebSearch(llm=self.llm, config=self.config, verbose=True, search_engine="hybrid")
        self.extractor = QuestionExtractor(self.llm, config=self.config)
        self.history = []
        self.enabled = False
    
    def enable_retriever(self):
        self.enabled = True

    def summarize_context(self, context):
        processed_text = self.extractor.process_context(context)
        return processed_text, self.extractor.get_format_cost()
    
    def evaluate_task(self, task, question, answer):
        evaluation = self.extractor.evaluate_answer(task=task, question=question, answer=answer)
        return evaluation, self.extractor.get_evaluate_cost()

    def rag_generate(self, query, collection, mode="chain"):
        with console.overlay_session() as o:
            if mode == "graph":
                answer = self.retrieval_alg.do_graphrag(query)
            elif mode == "self_rag":
                answer = self.retrieval_alg.do_selfrag(query, collection)
            else:
                answer = self.retrieval_alg.do_rag(query, collection)
            self.history.append({
                "query": query,
                "collection": collection,
                "answer": answer
            })
            console.overlay_print(f"Retrieval Result: {answer}", 2)
            return answer
    
    def do_web_search(self, query):
        with console.overlay_session() as o:
            result = self.web_search.search_web(query)
            console.overlay_print(result.content, 2)
            return result.content

    
if __name__ == "__main__":
    load_api_keys(key_cfg=Path(__file__).resolve().parent.parent.parent / "keys.cfg")
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", default=Path(__file__).resolve().parent.parent / "config/rag_config.yaml", type=str, help="config path")
    args = parser.parse_args()
    agent = RetrieverManager(config=RetrieverConfig(config_path=args.config))
    # # response = agent.summarize_context(info=TEST_CONTEXT)
    # # print(response)
    # answer = agent.rag_generate("how to reverse", mode="self_rag", collection="writeups")
    result = agent.do_web_search(r"How to write a good scientific paper?")
    # print(answer)
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
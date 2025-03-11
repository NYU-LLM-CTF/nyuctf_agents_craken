import os
import argparse
from pathlib import Path
from langchain_openai import ChatOpenAI
from ctfrag.rag import RAGAgent
from ctfrag.config import RetrieverConfig
from ctfrag.qformatter import QuestionExtractor
from langchain_core._api.deprecation import LangChainDeprecationWarning
import warnings
# os.environ["PYTHONWARNINGS"] = "ignore"
# warnings.simplefilter("ignore", category=DeprecationWarning)
# warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)
# warnings.filterwarnings("ignore")

TEST_CONTEXT = """
It seems we don't have permission to install packages. 
Let's try using Python to interpret the Brainfuck code. I'll create a simple Python script to do this:
"""

with open(Path(__file__).resolve().parent.parent / "api_keys", "r") as f:
    for line in f:
        key, value = line.strip().split("=")
        os.environ[key] = value

class RetrieverManager:
    def __init__(self, api_key=None, config: RetrieverConfig={}) -> None:
        self.config = config
        self.api_key = api_key
        self.model = self.config.agent_config.model_name
        self.llm = ChatOpenAI(model_name=self.model, temperature=self.config.agent_config.model_temperature)
        self.retrieval_alg = RAGAgent(llm=self.llm, config=config)
        self.extractor = QuestionExtractor(self.llm)
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

    def rag_generate(self, query, collection, mode="graph", template=None):
        if mode == "graph":
            results = self.retrieval_alg.graph_retrieve(query, collection, template if template else self.config.rag_config.template_main)
            answer = results["answer"]
        elif mode == "self_rag":
            results = self.retrieval_alg.self_rag_retrieve(query, collection, template if template else self.config.rag_config.template_main)
            answer = results["answer"]
        else:
            answer = self.retrieval_alg.chain_retrieve(query, collection, template if template else self.config.rag_config.template_main)
        self.history.append({
            "query": query,
            "collection": collection,
            "answer": answer
        })
        return answer

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", default=Path(__file__).resolve().parent.parent / "config/rag_config.yaml", type=str, help="config path")
    args = parser.parse_args()
    agent = RetrieverManager(config=RetrieverConfig(config_path=args.config))
    # response = agent.summarize_context(info=TEST_CONTEXT)
    # print(response)
    # #answer = agent.rag_generate(response, mode="chain", collection="writeups")
    # answer = agent.rag_generate("How to reverser?", mode="rag", collection="default")
    # # context, answer = agent.rag_generate("Find any writeups for me, give me the database name and divide it into steps", collection="writeups")
    # # context, answer = agent.rag_generate(response, collection="HFCTF")
    # # context, answer = agent.rag_generate("What is decomposition", collection="HFCTF")
    # print(answer)
    #task_example = "Analyze Tesla's 2022 financial statements, extract key financial metrics, and compare them with industry standards"
    task_example = "How to reverse?"
    task_result, fcost = agent.summarize_context(TEST_CONTEXT)
    for i, q in enumerate(task_result, 0):
        answer = agent.rag_generate(task_result[i]['question'], mode="self_rag", collection="writeups")
        print(task_result[i]['question'] + "\n" + answer + "\n\n")
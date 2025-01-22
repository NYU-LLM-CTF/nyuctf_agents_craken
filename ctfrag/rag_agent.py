import os
import argparse
from pathlib import Path
from langchain_openai import ChatOpenAI
from ctfrag.retrieval import RAGRetrieval
from ctfrag.rag_config import RAGConfig
import warnings
warnings.simplefilter("ignore", category=DeprecationWarning)

with open(Path(__file__).resolve().parent.parent / "api_keys", "r") as f:
    OPENAI_API_KEY = f.read().strip()
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


class RagAgent:
    def __init__(self, api_key=OPENAI_API_KEY, config: RAGConfig={}) -> None:
        self.config = config
        self.api_key = api_key
        self.model = self.config.agent_config.model_name
        self.llm = ChatOpenAI(model_name=self.model, temperature=self.config.agent_config.model_temperature)
        self.retrieval_alg = RAGRetrieval(llm=self.llm, config=config)
        self.history = []

    def pre_summarization(self, info, prompt=None):
        response = self.llm.invoke(prompt if prompt else self.config.retrieval_config.template_q.format(observation=info))
        return response.content

    def rag_generate(self, query, collection, template=None):
        results = self.retrieval_alg.graph_retrieve(query, collection, template if template else self.config.retrieval_config.template_main)
        # answer = retreval.chain_retrieve("What is decomposition?")
        self.history.append({
            "query": query,
            "collection": collection,
            "context": results["context"],
            "answer": results["answer"]
        })
        return results["context"], results["answer"]

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", default=Path(__file__).resolve().parent.parent / "config/rag_config.yaml", type=str, help="config path")
    args = parser.parse_args()
    agent = RagAgent(config=RAGConfig(config_path=args.config))
    # response = agent.pre_summarization("Described ")
    context, answer = agent.rag_generate("Find any writeups for me and describe it from the database", collection="writeups")
    # context, answer = agent.rag_generate(response, collection="HFCTF")
    # context, answer = agent.rag_generate("What is decomposition", collection="HFCTF")
    print(answer)
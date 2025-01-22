import os
import argparse
from pathlib import Path
from langchain_openai import ChatOpenAI
from ctfrag.retrieval import RAGRetrieval
from ctfrag.rag_config import RAGConfig
import warnings
warnings.simplefilter("ignore", category=DeprecationWarning)

TEST_CONTEXT = """
Excellent! We've got the output from the Brainfuck code. 
Looking at the output format, this appears to be RSA encryption parameters in JSON-like format. 
We have:\n- p and q: the prime factors\n- dp and dq: CRT (Chinese Remainder Theorem) parameters\n- c: the ciphertext\n\nLet's write a Python script to decrypt this RSA using CRT parameters:
"""

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

    def summarize_context(self, info, prompt=None):
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
    response = agent.summarize_context(info=TEST_CONTEXT)
    print(response)
    context, answer = agent.rag_generate(response, collection="writeups")
    # context, answer = agent.rag_generate("Find any writeups for me, give me the database name and divide it into steps", collection="writeups")
    # context, answer = agent.rag_generate(response, collection="HFCTF")
    # context, answer = agent.rag_generate("What is decomposition", collection="HFCTF")
    print(answer)
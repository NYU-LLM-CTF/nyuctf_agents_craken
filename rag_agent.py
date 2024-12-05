import os
import argparse
from langchain_openai import ChatOpenAI
from retrieval import RAGRetrieval, MilvusDB, WeaviateDB
from rag_config import RAGConfig

with open("api_keys", "r") as f:
    OPENAI_API_KEY = f.read().strip()
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

TEST_TEMPLATE = """You are an assistant for question-answering tasks.
Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know.
Use three sentences maximum and keep the answer concise.
Question: {question}
Context: {context}
Answer:
"""

# TESTLLM = ChatOpenAI(model_name="gpt-4o-mini-2024-07-18", temperature=0)

class RagAgent:
    def __init__(self, api_key=OPENAI_API_KEY, config: RAGConfig={}) -> None:
        self.config = config
        self.api_key = api_key
        self.model = self.config.agent_config.model_name
        self.llm = ChatOpenAI(model_name=self.model, temperature=self.config.agent_config.model_temperature)
        self.retrieval_alg = RAGRetrieval(llm=self.llm, config=config)
        self.history = []

    def pre_summarization(self, prompt=None):
        pass

    def post_summarization(self, prompt=None):
        pass

    def rag_generate(self, query, collection, template=None):
        results = self.retrieval_alg.graph_retrieve(query, collection, template if template else self.config.retrieval_config.template_qa)
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
    parser.add_argument("-c", "--config", default="./config/rag_config.yaml", type=str, help="config path")
    args = parser.parse_args()
    agent = RagAgent(config=RAGConfig(config_path=args.config))
    context, answer = agent.rag_generate("How to use huggingface pip", collection="HFCTF")
    print(answer)
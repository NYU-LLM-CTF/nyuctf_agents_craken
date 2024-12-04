from retrieval import RAGRetrieval, MilvusDB, WeaviateDB
import os
from langchain_openai import ChatOpenAI

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
    def __init__(self, model_name=None, api_key=None, db_type: str="milvus") -> None:
        self.api_key = api_key
        self.model = model_name
        self.llm = ChatOpenAI(model_name=self.model, temperature=0)
        self.retrieval_alg = RAGRetrieval(llm=self.llm, db_type=db_type)
        self.history = []

    def pre_summarization(self, prompt=None):
        pass

    def post_summarization(self, prompt=None):
        pass

    def rag_generate(self, query, collection, template=TEST_TEMPLATE):
        context, answer = self.retrieval_alg.graph_retrieve(query, collection, template)
        # answer = retreval.chain_retrieve("What is decomposition?")
        self.history.append({
            "query": query,
            "collection": collection,
            "context": context,
            "answer": answer
        })
        return context, answer

    
if __name__ == "__main__":
    agent = RagAgent(model_name="gpt-4o-mini-2024-07-18", api_key=OPENAI_API_KEY)
    context, answer = agent.rag_generate("How to use huggingface pip", collection="HFCTF")
    print(answer)
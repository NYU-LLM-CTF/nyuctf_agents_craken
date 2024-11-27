import os
import tempfile
import requests
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import weaviate
import validators
from langchain_weaviate.vectorstores import WeaviateVectorStore

with open("api_keys", "r") as f:
    OPENAI_API_KEY = f.read().strip()
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

class RAGDatabase:
    def __init__(self) -> None:
        self.weaviate_cli = None
        self.port = 50050
        self.host = "0.0.0.0"
        self.grpc_port = 50051
        self.chunk_size = 200
        self.overlap = 0
        self.prompt_history = []
        self.pre_summary = []
        self.post_summary = []
        self.results = []
        self.setup()

    def __download_data(self, url=None, path=None) -> None:
        if path:
            res = requests.get(url)
            with open(path, "w") as f:
                f.write(res.text)
                return path
        else:
            fd, path = tempfile.mkstemp()
            try:
                res = requests.get(url)
                with os.fdopen(fd, 'w') as f:
                    f.write(res.text)
                    return path
            finally:
                pass

    def setup(self) -> None:
        self.weaviate_cli = weaviate.connect_to_local(
            host=self.host,
            port=self.port,
            grpc_port=self.grpc_port,
        )

    def create_collection(self, collection_name):
        if self.weaviate_cli:
            self.weaviate_cli.collections.create(collection_name)

    def load_file(self, path=None, collection=None) -> None:
        is_url = False
        if not path:
            print("Please provide a url for data download.")
            return
        if validators.url(path):
            print("URL Found, start downloading...")
            path = self.__download_data(url=path)
            is_url = True
        loader = TextLoader(path)
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.overlap)
        docs = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()
        db = WeaviateVectorStore.from_documents(
            docs,
            embeddings,
            client=self.weaviate_cli,
            index_name=collection
        )
        if is_url:
            os.remove(path)

    def load_hf(self, collecton=None) -> None:
        pass

    def load_query(self, collection=None) -> None:
        pass

    def close(self) -> None:
        if self.weaviate_cli:
            print("Close client...")
            self.weaviate_cli.close()

    def clean_db(self, name=None):
        if self.weaviate_cli:
            self.weaviate_cli.collections.delete(name)

    def test_query(self, collection=None, query=None):
        data = WeaviateVectorStore.from_documents([], OpenAIEmbeddings(), client=self.weaviate_cli, index_name=collection)
        docs = data.similarity_search(query)
        for i, doc in enumerate(docs):
            print(f"\nDocument {i+1}:")
            print(doc.page_content[:100] + "...")

if __name__ == "__main__":
    db = RAGDatabase()
    # data = WeaviateVectorStore.from_documents([], OpenAIEmbeddings(), client=db.weaviate_cli, index_name="LLMCTF")
    # query = "Who is the president"
    # docs = data.similarity_search(query)
    # for i, doc in enumerate(docs):
    #     print(f"\nDocument {i+1}:")
    #     print(doc.page_content[:100] + "...")
    # db.load_url(url="https://raw.githubusercontent.com/hwchase17/chroma-langchain/refs/heads/master/state_of_the_union.txt", doc_name="state_of_the_union", collection="LLMCTF")
    # print(db.weaviate_cli.collections.get("LLMCTF"))
    # db.clean_db("LLMCTF")
    db.close()
    # db.clean_db("LangChain_c355107f8ddc4eae943946b27ff253e3")
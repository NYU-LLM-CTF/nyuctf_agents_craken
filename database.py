import os
import tempfile
import requests
import datasets
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import weaviate
from typing import List, Optional
from langchain_community.vectorstores.utils import DistanceStrategy
from transformers import AutoTokenizer
import validators
from langchain.docstore.document import Document as LangchainDocument
from tqdm import tqdm
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores.utils import DistanceStrategy

with open("api_keys", "r") as f:
    OPENAI_API_KEY = f.read().strip()
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

class RAGDatabase:
    def __init__(self) -> None:
        self.weaviate_cli = None
        self.port = 50050
        self.host = "0.0.0.0"
        self.grpc_port = 50051
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

    def load_file(self, path=None, collection=None, chunk_size=512, overlap=50) -> None:
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
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
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

    def load_hf(self, dataset=None, collection=None, 
                chunk_size=512, overlap=50, unique=True, 
                text_col="text", name_col="source") -> None:
        embeddings = OpenAIEmbeddings()
        ds = datasets.load_dataset(dataset, split="train")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        docs_processed = []
        RAW_KNOWLEDGE_BASE = [
            LangchainDocument(page_content=doc[text_col], metadata={"source": doc[name_col]})
            for doc in tqdm(ds)
        ]
        for doc in RAW_KNOWLEDGE_BASE:
            docs_processed += text_splitter.split_documents([doc])
        if unique:
            unique_texts = {}
            docs_processed_unique = []
            for doc in docs_processed:
                if doc.page_content not in unique_texts:
                    unique_texts[doc.page_content] = True
                    docs_processed_unique.append(doc)
        db = WeaviateVectorStore.from_documents(
            docs_processed_unique if unique else docs_processed, embeddings, distance_strategy=DistanceStrategy.COSINE, client=self.weaviate_cli, index_name=collection
        )
    
    def _readdoc(self, path):
        with open(path, "r") as f:
            text = f.read()
        return text

    def load_dir(self, dir=None, collection=None, 
                 chunk_size=512, overlap=50, unique=True, 
                 recursive=True) -> None:
        if not os.path.isdir(dir):
            print("Please provide a valid directory")
            return
        paths = []
        docs_processed = []
        embeddings = OpenAIEmbeddings()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
        if recursive:
            for root, dirs, files in os.walk(dir):
                for filename in files:
                    paths.append(os.path.join(root, filename))
        else:
            for filename in os.listdir(dir):
                paths.append(os.path.join(dir, filename))
        
        RAW_KNOWLEDGE_BASE = [
            LangchainDocument(page_content=self._readdoc(path), metadata={"source": path})
            for path in tqdm(paths)
        ]

        for doc in RAW_KNOWLEDGE_BASE:
            docs_processed += text_splitter.split_documents([doc])
        if unique:
            unique_texts = {}
            docs_processed_unique = []
            for doc in docs_processed:
                if doc.page_content not in unique_texts:
                    unique_texts[doc.page_content] = True
                    docs_processed_unique.append(doc)
        db = WeaviateVectorStore.from_documents(
            docs_processed_unique if unique else docs_processed, embeddings, distance_strategy=DistanceStrategy.COSINE, client=self.weaviate_cli, index_name=collection
        )

    def load_queries(self, collection=None) -> None:
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
            print(doc.page_content)

if __name__ == "__main__":
    db = RAGDatabase()
    # db.load_hf(dataset="m-ric/huggingface_doc", collection="HFCTF")
    db.test_query("HFCTF", "How to create an endpoint")
    db.close()
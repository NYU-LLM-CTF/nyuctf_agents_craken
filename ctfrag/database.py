import os
import tempfile
import requests
import datasets
import pandas as pd
from tqdm import tqdm
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import validators
from langchain.docstore.document import Document as LangchainDocument
from tqdm import tqdm
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import yaml
from pathlib import Path
from unstructured.partition.pdf import partition_pdf
from ctfrag.db_backend.base import BaseVectorDB

with open(Path(__file__).resolve().parent.parent / "api_keys", "r") as f:
    for line in f:
        key, value = line.strip().split("=")
        os.environ[key] = value

def find_by_name(name, items):
    for item in items:
        if item.__name__ == name:
            return item
    return None 

SPLITTERS = [CharacterTextSplitter, RecursiveCharacterTextSplitter]
EMBEDDINGS = [OpenAIEmbeddings]

class RAGDatabase:
    def __init__(self, database: BaseVectorDB, config={}) -> None:
        self.vector_db = database
        self.config = config

    def _download_data(self, url=None, path=None) -> None:
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

    def _parse_file(self, path, collection, embeddings, text_splitter, args):
        if path.endswith((".csv", ".tsv", ".json", ".yaml", ".yml", ".xls", ".xlsx")):
            self.load_multirow(path=path, collection=collection, 
                                embeddings=embeddings, text_splitter=text_splitter, 
                                name_field=args.get("name_field", "key"), data_field=args.get("data_field", "value"))
        else:
            self.load_plaintext(path=path, collection=collection, 
                                embeddings=embeddings, text_splitter=text_splitter)

    # Sample args:
    # args = {
    #     "name_col": "source",
    #     "data_col": "text",
    #     "collection": "ctfrag",
    #     "chunk_size": 512,
    #     "overlap": 50
    # }
    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    # text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    # embeddings = OpenAIEmbeddings()
    def load_dataset(self, path=None, collection="default", args: dict = {
        "name_field": "key",
        "data_field": "value",
        "collection": "ctfrag",
        "chunk_size": 512,
        "overlap": 50,
    }):

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=args.get("chunk_size", 512), chunk_overlap=args.get("overlap", 50))
        embeddings = OpenAIEmbeddings()
        if not path:
            print("Please provide a url or file path")
            return
        if not os.path.isdir(path):
            print("Not a directory, loading single file...")
            self._parse_file(path, collection, embeddings, text_splitter, args)
        else:
            print("Directory detected, loading in batch...")
            files = self._walk_dir(path)
            for file in tqdm(files):
                self._parse_file(file, collection, embeddings, text_splitter, args)

    def _walk_dir(self, dir):
        all_files = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                file_path = os.path.join(root, file)
                all_files.append(file_path)
        return all_files

    def load_plaintext(self, path=None, collection=None, embeddings=None, text_splitter=None) -> None:
        is_url = False
        if not path:
            print("Please provide a url for data download.")
            return
        if validators.url(path):
            print("URL Found, start downloading...")
            path = self._download_data(url=path)
            is_url = True
        if path.endswith(".pdf"):
            print("Processing PDF...")
            try:
                elements = partition_pdf(filename=path)
                text = "\n".join([element.text for element in elements if element.text])
                if not text.strip():
                    print("Warning: No extractable text found in PDF.")
                    return

                document = LangchainDocument(page_content=text, metadata={"source": path})
                docs = text_splitter.split_documents([document])
                self.vector_db.insert_document(docs, collection)
            except Exception as e:
                print(f"Error processing PDF with unstructured: {e}")
                return
    
            #pass
            # doc = pymupdf.open(path)
            # fd, path = tempfile.mkstemp()
            # with os.fdopen(fd, 'wb') as f:
            #     for page in doc:
            #         text = page.get_text().encode("utf8")
            #         f.write(text)
            #         f.write(bytes((12,)))
        else:
            loader = TextLoader(path)
            documents = loader.load()
            docs = text_splitter.split_documents(documents)
            self.vector_db.insert_document(docs, collection)
        if is_url:
            os.remove(path)

    def load_multirow(self, path=None, collection=None, embeddings=None, text_splitter=None, name_field="source", data_field="text") -> None:
        is_url = False
        if not path:
            print("Please provide a url for data download.")
            return
        if validators.url(path):
            print("URL Found, start downloading...")
            path = self._download_data(url=path)
            is_url = True
        if path.endswith(".csv"):
            df = pd.read_csv(path)
        elif path.endswith(".tsv"):
            df = pd.read_csv(path, sep='\t')
        elif path.endswith((".xlsx", ".xls")):
            df = pd.read_excel(path)
        elif path.endswith(".json"):
            with open(path, "r") as f:
                data_dict = json.load(f)
        elif path.endswith((".yaml", ".yml")):
            with open(path, "r") as f:
                data_dict = yaml.safe_load(f)
        else:
            print("Unsupported file format. Only JSON, YAML, CSV, TSV, and Excel files are supported.")
            return
        if path.endswith((".json", ".yaml", ".yml")):
            try:
                data = {item[name_field]: item[data_field] for item in data_dict}
            except KeyError as e:
                print(f"Error: Missing key in JSON/YAML data - {e}")
                return
        else:
            try:
                data = dict(zip(df[name_field], df[data_field]))
            except KeyError as e:
                print(f"Error: Column not found in the file - {e}")
                return
        for key, value in data.items():
            document = {"page_content": value, "metadata": {"name": key}}
            docs = text_splitter.split_documents([document])
            self.vector_db.insert_document(docs, collection)
        if is_url:
            import os
            os.remove(path)
            print(f"Downloaded file {path} has been removed.")

    def load_hf(self, dataset=None, collection=None, 
                embeddings=None, text_splitter=None,
                name_field="source", 
                data_field="text", type="csv", split="train", unique=True) -> None:
        if not dataset:
            print("Please provide a dataset for data download.")
            return
        if type == "csv":
            ds = datasets.load_dataset("csv", data_files=dataset)
            ds = ds[list(ds.keys())[0]]
        else:
            ds = datasets.load_dataset(dataset, split=split)
        docs_processed = []
        RAW_KNOWLEDGE_BASE = [
            LangchainDocument(page_content=doc[data_field], metadata={"source": doc[name_field]})
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
        self.vector_db.insert_document(docs_processed_unique if unique else docs_processed, collection)
    
    def get_db(self):
        return self.vector_db
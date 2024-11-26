import os
import tempfile
import requests
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
import weaviate
from weaviate.embedded import EmbeddedOptions

class RAGDatabase:
    def __init__(self) -> None:
        self.weaviate_cli = None
        self.port = 50050
        self.host = "0.0.0.0"
        self.grpc_port = 50051

    def download_data(self) -> None:
        pass

    def setup(self) -> None:
        self.weaviate_cli = weaviate.connect_to_local(
            host=self.host,
            port=self.port,
            grpc_port=self.grpc_port,
        )

    def load_url(self) -> None:
        pass

    def load_file(self) -> None:
        pass

    def load_hf(self) -> None:
        pass

    def close(self) -> None:
        if self.weaviate_cli:
            self.weaviate_cli.close()
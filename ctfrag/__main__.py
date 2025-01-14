import argparse
import logging
from .database import RAGDatabase, MilvusDB, WeaviateDB

logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser("Import RAG data")
parser.add_argument("--database", required=True, default="milvus", choices=["milvus", "weaviate"], help="Vector database")
parser.add_argument("--mode", required=True, default="single", choices=["batch", "single"], help="Data import model, batch or single")
parser.add_argument("--path", required=True, help="Data path")
parser.add_argument("--file_type", required=True, choices=["csv", "text", "pdf"], help="Data format")
parser.add_argument("--name_col", help="Instance name column, used when import csv")
parser.add_argument("--data_col", help="Instance data column, used when import csv")
args = parser.parse_args()

if args.database == "milvus":
    db_backend = MilvusDB()
else:
    db_backend = WeaviateDB()

db = RAGDatabase(db_backend)

if 
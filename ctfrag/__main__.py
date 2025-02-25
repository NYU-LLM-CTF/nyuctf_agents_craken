import argparse
# import logging
from ctfrag.database import RAGDatabase
from ctfrag.db_backend.milvus import MilvusDB
from ctfrag.db_backend.weaviate import WeaviateDB

# logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser("Import RAG data")
parser.add_argument("--database", default="milvus", choices=["milvus", "weaviate"], help="Vector database")
parser.add_argument("--path", required=True, help="Data path")
parser.add_argument("--collection", required=True, default="default", help="Collection to store in vector db")
parser.add_argument("--name-col", default="key", help="Instance name column, used when import csv")
parser.add_argument("--data-col", default="value", help="Instance data column, used when import csv")
parser.add_argument("--chunk-size", default=512, help="Chunk size of indexing")
parser.add_argument("--overlap", default=50, help="Overlap of indexing")
args = parser.parse_args()

if args.database == "milvus":
    db_backend = MilvusDB()
else:
    db_backend = WeaviateDB()

db = RAGDatabase(db_backend)
db.load_dataset(path=args.path, collection=args.collection, args={
        "name_field": args.name_col,
        "data_field": args.data_col,
        "collection": args.collection,
        "chunk_size": args.chunk_size,
        "overlap": args.overlap,
})
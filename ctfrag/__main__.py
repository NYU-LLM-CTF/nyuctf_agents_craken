import argparse
# import logging
from pathlib import Path
from ctfrag.database import RAGDatabase
from ctfrag.db_backend.milvus import MilvusDB
from ctfrag.db_backend.neo4j import Neo4jDB
from ctfrag.utils import load_api_keys
from ctfrag.backends import EmbeddingModel
import warnings
warnings.filterwarnings("ignore")

# logging.basicConfig(level=logging.DEBUG)
file_path = Path(__file__).resolve().parent.parent.parent
parser = argparse.ArgumentParser("Import RAG data")
parser.add_argument("-m", "--mode", default="insert", choices=["insert", "delete", "view"], 
                    help="Operation mode: insert, delete, or view data")
parser.add_argument("--database", default="milvus", choices=["milvus", "weaviate", "neo4j"], help="Vector or graph database")
parser.add_argument("-i", "--path", help="Data path")
parser.add_argument("-k", "--api-keys", default=str(file_path / "keys.cfg"), help="API Keys file")
parser.add_argument("-c", "--collection", required=True, help="Collection to store in vector db")
parser.add_argument("-t", "--threads", default=16, help="Number of threads used to load dataset")
parser.add_argument("-e", "--embeddings", choices=["openai", "together", "huggingface"], default="openai", help="Embeddings backend to use")
parser.add_argument("--auto", action="store_true", help="If use auto text splitter")
parser.add_argument("--embeddings-model", default=None, help="Embedding models to use")
parser.add_argument("--name-col", default="key", help="Instance name column, used when import csv")
parser.add_argument("--limit", default=10, help="Number of output samples")
parser.add_argument("--data-col", default="value", help="Instance data column, used when import csv")
parser.add_argument("--chunk-size", default=4096, help="Chunk size of indexing")
parser.add_argument("--overlap", default=100, help="Overlap of indexing")
args = parser.parse_args()

if args.mode == "insert" and not args.path:
    parser.error("Insert mode requires --path argument")

load_api_keys(key_cfg=args.api_keys)
embeddings = EmbeddingModel(args.embeddings, args.embeddings_model)

if args.database == "milvus":
    db_backend = MilvusDB(embeddings=embeddings())
elif args.database == "neo4j":
    db_backend = Neo4jDB(embeddings=embeddings())

db = RAGDatabase(db_backend)
if args.mode == "insert":
    db.fast_load_dataset(path=args.path, embeddings=embeddings(), collection=args.collection, database=args.database, args={
            "name_field": args.name_col,
            "data_field": args.data_col,
            "collection": args.collection,
            "chunk_size": args.chunk_size,
            "overlap": args.overlap,
            "max_workers": int(args.threads),
            "auto_splitter": args.auto
    })
elif args.mode == "delete":
    db.delete_db(collection=args.collection)
elif args.mode == "view":
    db.view_samples(collection=args.collection, limit=int(args.limit))
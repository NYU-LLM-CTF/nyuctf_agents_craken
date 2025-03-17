import argparse
# import logging
from ctfrag.database import RAGDatabase
from ctfrag.db_backend.milvus import MilvusDB
from ctfrag.db_backend.weaviate import WeaviateDB
from ctfrag.db_backend.neo4j import Neo4jDB
from ctfrag.backends import EmbeddingModel

# logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser("Import RAG data")
parser.add_argument("--database", default="milvus", choices=["milvus", "weaviate", "neo4j"], help="Vector or graph database")
parser.add_argument("-i", "--path", required=True, help="Data path")
parser.add_argument("-c", "--collection", required=True, help="Collection to store in vector db")
parser.add_argument("-e", "--embeddings", choices=["openai", "together", "huggingface"], default="openai", help="Embeddings backend to use")
parser.add_argument("--embeddings-model", default=None, help="Embedding models to use")
parser.add_argument("--name-col", default="key", help="Instance name column, used when import csv")
parser.add_argument("--data-col", default="value", help="Instance data column, used when import csv")
parser.add_argument("--chunk-size", default=2048, help="Chunk size of indexing")
parser.add_argument("--overlap", default=100, help="Overlap of indexing")
args = parser.parse_args()

embeddings = EmbeddingModel(args.embeddings, args.embeddings_model)

if args.database == "milvus":
    db_backend = MilvusDB(embeddings=embeddings())
elif args.database == "neo4j":
    db_backend = Neo4jDB(embeddings=embeddings())
else:
    db_backend = WeaviateDB(embeddings=embeddings())

db = RAGDatabase(db_backend)
db.load_dataset(path=args.path, embeddings=embeddings(),collection=args.collection, database=args.database, args={
        "name_field": args.name_col,
        "data_field": args.data_col,
        "collection": args.collection,
        "chunk_size": args.chunk_size,
        "overlap": args.overlap,
})
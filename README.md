### Database Import
To import the database you need to follow below steps:
- **Run the database:** Use `milvus` docker file placed in the respective folder to run the database instance loaclly using `docker compose up` command.
- **Load the database:** Load the writeup database by provinding `path` in `databae.py`. Provide a collection name accordingly.
- **Run RAG agent:** Run the `rag_agent.py` by using `agent.rag_generate()` in the script.
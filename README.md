# Knowledge-based CTF
## Database Import
To import the database you need to follow below steps:
- **Run the database:** Use `milvus` docker file placed in the respective folder to run the database instance loaclly using `bash setup.sh` command.
- **Install ctfrag package using
```console
pip install -e .
```
- **Load the database:** Load the writeup database by provinding `path` in `databae.py`. Provide a collection name accordingly. Example command
```console
python -m ctfrag --database {dataset path} --collection {collection name}
```
- **Run RAG agent:** Run the `rag_agent.py` by using `agent.rag_generate()` in the script.
## TODO List
### Agent
- [x] Complete WebSearch Agent implementation
- [ ] Complete Self-RAG implementation
- [ ] Refactor RAG Agent
### Integration
- [x] Integrate RAG Agent to D-CIPHER
- [ ] Add integration to tool use
- [ ] Enhance integration
### Database
- [ ] Extend writeup database to 1000 writeups
- [ ] Other collections, code, commonsense, payload etc.
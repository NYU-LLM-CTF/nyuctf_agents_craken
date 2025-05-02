# Knowledge-based CTF
## Run KAPTER on NYU CTF Agents
### 1. Clone repo
At current stage KAPTER only support the development repo of NYU CTF Agents (nyuctf_multiagent)
```bash
git clone git@github.com:NYU-LLM-CTF/nyuctf_multiagent.git
cd nyuctf_multiagent
git clone git@github.com:NYU-LLM-CTF/ctfrag.git
```
Make sure the folder ctfrag is in the root folder of nyuctf_multiagent
### 2. Config keys
The default key file path in KAPTER's config is under nyuctf_multiagent/keys.cfg. Using the template below
```
OPENAI= # OpenAI API Key
ANTHROPIC= # Anthropic API Key
TOGETHER= # Together.ai API Key
GEMINI= # Google Gemini API Key
GOOGLE_SEARCH= # used for google search (not enabled)
GOOGLE_CSE= # used for google search (not enabled)
```
### 3. Install packages
Install nyuctf_multiagent and ctfrag package
```bash
cd nyuctf_multiagent
pip install -e .
cd ctfrag
pip install -e .
```
### 4. Import database
Assuming using Milvus database (Classic RAG)
```bash
python -m ctfrag -i {PATH TO THE DATA FOLDER} -c {COLLECTION THAT STORE THE DATA}
```
If using GraphRAG, specify Neo4j database
### 5. Run KAPTER
```bash
#!/bin/bash

NYUCTF_BENCH=path/to/the/benchmark

MAX_COST=3.0
NAME=experiment_name
PLANNER_MODEL=model_name
EXECUTOR_MODEL=model_name
RETRIEVER_MODEL=model_name

function run() {
    python3 run_planner_executor.py \
        --dataset $NYUCTF_BENCH/test_dataset.json \
        --experiment-name $NAME \
        --planner-model $PLANNER_MODEL --autoprompter-model $PLANNER_MODEL \
        --executor-model $EXECUTOR_MODEL \
        --max-cost $MAX_COST \
        --enable-autoprompt \
        --enable-retriever \
        --retriever-model $RETRIEVER_MODEL \
        --skip-existing \
        --quiet \
        --challenge $1
}
```
## TODO List
### Agent
- [x] Complete WebSearch Agent implementation
- [x] Complete Self-RAG implementation (High Priority)
- [x] Refactor RAG Agent
- [ ] Refactor Graph-RAG
### Integration
- [x] Integrate RAG Agent to D-CIPHER
- [ ] Enhance integration (High Priority)
### Database
- [x] Extend writeup database to 1000 writeups (High Priority)
- [x] Other collections, code, commonsense, payload etc. (High Priority)
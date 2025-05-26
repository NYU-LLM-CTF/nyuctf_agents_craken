# CRAKEN: Cybersecurity LLM Agent with Knowledge-Based Execution
This is the official repository for [paper](https://www.arxiv.org/pdf/2505.17107) "CRAKEN: Cybersecurity LLM Agent with Knowledge-Based Execution".

## Run CRAKEN on NYU CTF Agents
### 1. Clone repo
At current stage CRAKEN only support the development repo of NYU CTF Agents (nyuctf_multiagent)
```bash
git clone git@github.com:NYU-LLM-CTF/nyuctf_multiagent.git
cd nyuctf_multiagent
git clone git@github.com:NYU-LLM-CTF/ctfrag.git
```
Make sure the folder ctfrag is in the root folder of nyuctf_multiagent
### 2. Config keys
The default key file path in CRAKEN's config is under nyuctf_multiagent/keys.cfg. Using the template below
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
### 5. Run CRAKEN
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
## Run CRAKEN on Other Agents
### Setup

Follow step 1, 2, 3, 4 of section **Run CRAKEN on NYU CTF Agents**

### Integration

Integrate CRAKEN built-in function in your own agents

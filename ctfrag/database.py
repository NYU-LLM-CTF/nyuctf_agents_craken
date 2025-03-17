import os
import tempfile
import requests
import datasets
import pandas as pd
from tqdm import tqdm
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import validators
from langchain.docstore.document import Document as LangchainDocument
from tqdm import tqdm
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
import yaml
from pathlib import Path
from unstructured.partition.pdf import partition_pdf
from ctfrag.db_backend.base import BaseVectorDB
import openai
from langchain_core.documents import Document


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
        if os.path.getsize(path) < 1024:  
            #print(f"[SKIP] {path} is too small ({os.path.getsize(path)} bytes).")
            return
        if path.endswith((".csv", ".tsv", ".json", ".yaml", ".yml", ".xls", ".xlsx")):
            self.load_multirow(path=path, collection=collection, 
                                embeddings=embeddings, text_splitter=text_splitter, 
                                name_field=args.get("name_field", "key"), data_field=args.get("data_field", "value"))
        else:
            self.load_plaintext(path=path, collection=collection, 
                                embeddings=embeddings, text_splitter=text_splitter)
            
    def _parse_file_graphdb(self, path, collection):
        if path.endswith(".md") or path.endswith(".txt"):
            # file_path = os.path.join(folder_path, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract knowledge graph
            extracted_data = self.extract_knowledge_graph(content)

            doc = Document(page_content=json.dumps(extracted_data))
            
            if extracted_data["entities"] and extracted_data["relationships"]:
                # print(f"🔍 Extracting entities & relationships from {filename}...")
                # self.load_data_into_neo4j(extracted_data["entities"], extracted_data["relationships"])
                try:
                    self.vector_db.insert_document([doc], collection)
                except Exception as e:
                    print(f"Error processing file: {path}\nError message: {e}")
            else:
                print(f"⚠️ No relevant data extracted from {path}.")
        else:
            print("The files is not .md or .txt format.")

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
    def load_dataset(self, path=None, embeddings=None, collection="default", database="neo4j", args: dict = {
        "name_field": "key",
        "data_field": "value",
        "collection": "ctfrag",
        "chunk_size": 512,
        "overlap": 50,
    }):
        
        if database=="neo4j":
            if not path:
                print("Please provide a file path")
                return
            if not os.path.isdir(path):
                print("Not a directory, loading single file...")
                self._parse_file_graphdb(path, collection)
            else:
                print("Directory detected, loading in batch...")
                files = self._walk_dir(path)
                for file in tqdm(files):
                    self._parse_file_graphdb(file, collection)
        else:
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=args.get("chunk_size", 512), chunk_overlap=args.get("overlap", 50))
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
    
    def extract_knowledge_graph(self, text):
        """Use GPT-4o to extract entities and relationships from text."""
        prompt = f"""
        You are a cybersecurity knowledge extraction assistant. Given the following text, extract entities and relationships in JSON format based on these predefined types:

        #### Entities
        Entities are the key nodes in the graph representing different aspects of CTF challenges, solutions, and methodologies.

        ##### Challenge-Related Entities
        - **CTF_Event**: The competition where the challenge appeared (e.g., DEFCON CTF 2023, Hack The Box).
        - **CTF_Challenge**: The specific challenge name (e.g., "Baby RE", "Pwn101").
        - **Challenge_Category**: The category of the challenge (e.g., Reverse Engineering, Pwn, Web Exploitation, Forensics, OSINT).
        - **Challenge_Difficulty**: Difficulty level (e.g., Easy, Medium, Hard).
        - **Challenge_Flag**: The flag format or actual flag pattern used in the challenge.

        ##### Technical Entities
        - **Programming_Language**: Language(s) used in the challenge (e.g., Python, C, JavaScript).
        - **Vulnerability_Type**: Security flaw(s) exploited (e.g., Buffer Overflow, SQL Injection, XXE).
        - **Exploit_Technique**: Specific methods used (e.g., Return Oriented Programming, Heap Exploitation).
        - **Tool_Used**: Security tools used (e.g., Ghidra, Burp Suite, Wireshark).
        - **Payload**: Exploit payloads (e.g., Shellcode, Reverse Shell).
        - **Cryptographic_Algorithm**: Cryptographic methods used or attacked (e.g., RSA, AES, SHA-256).
        - **Security_Mechanism**: Security defenses encountered (e.g., ASLR, DEP, Canaries).

        ##### Solution-Related Entities
        - **Solver**: The author of the writeup or solver of the challenge.
        - **Solution_Method**: The approach taken to solve the challenge (e.g., Brute Force, Symbolic Execution).
        - **Command_Executed**: Terminal commands used (e.g., nc, gdb, xxd).
        - **File_Analyzed**: Files examined during the challenge (e.g., exploit.py, challenge.bin).

        ##### Infrastructure Entities
        - **Server_IP**: The target machine's IP.
        - **Port_Number**: Port used for exploitation.
        - **Web_URL**: Websites or endpoints used in challenges.
        - **Database_System**: Databases involved (e.g., MySQL, PostgreSQL).
        - **Network_Protocol**: Protocols used in the challenge (e.g., HTTP, TCP, UDP).

        ##### Knowledge Extraction Entities
        - **Concept_Referenced**: Security concepts (e.g., Race Conditions, Memory Corruption).
        - **Threat_Model**: The attacker model assumed in the challenge.
        - **Security_Principle**: Underlying security principle exploited (e.g., Least Privilege, Defense in Depth).
        - **Malware_Sample**: If any malware was analyzed.

        ---

        #### Relationships
        These define how the extracted entities relate to each other in the knowledge graph.

        ##### Challenge Relationships
        - (**CTF_Event**) CONTAINS (**CTF_Challenge**)
        - (**CTF_Challenge**) BELONGS_TO (**Challenge_Category**)
        - (**CTF_Challenge**) HAS_DIFFICULTY (**Challenge_Difficulty**)
        - (**CTF_Challenge**) REQUIRES (**Programming_Language**)
        - (**CTF_Challenge**) INVOLVES (**Vulnerability_Type**)
        - (**CTF_Challenge**) USES (**Cryptographic_Algorithm**)
        - (**CTF_Challenge**) HAS_FLAG (**Challenge_Flag**)
        - (**CTF_Challenge**) TESTS (**Security_Principle**)

        ##### Solution Relationships
        - (**Solver**) SOLVED (**CTF_Challenge**)
        - (**Solver**) WROTE (**Writeup**)
        - (**Writeup**) DOCUMENTS (**Solution_Method**)
        - (**Solution_Method**) USES (**Tool_Used**)
        - (**Solution_Method**) EXECUTES (**Command_Executed**)
        - (**Solution_Method**) CREATES (**Payload**)
        - (**Payload**) EXPLOITS (**Vulnerability_Type**)
        - (**Solution_Method**) ANALYZES (**File_Analyzed**)

        ##### Technical Relationships
        - (**Exploit_Technique**) TARGETS (**Security_Mechanism**)
        - (**Exploit_Technique**) INVOLVES (**Payload**)
        - (**Exploit_Technique**) REQUIRES (**Programming_Language**)
        - (**Security_Mechanism**) PROTECTS_AGAINST (**Vulnerability_Type**)
        - (**Vulnerability_Type**) BYPASSES (**Security_Mechanism**)
        - (**Cryptographic_Algorithm**) USED_IN (**CTF_Challenge**)
        - (**Cryptographic_Algorithm**) ATTACKED_USING (**Exploit_Technique**)
        - (**Database_System**) CONNECTED_TO (**Web_URL**)
        - (**Web_URL**) HOSTED_ON (**Server_IP**)
        - (**Server_IP**) OPEN_ON (**Port_Number**)
        - (**Network_Protocol**) USED_IN (**CTF_Challenge**)

        ##### Knowledge Relationships
        - (**CTF_Challenge**) REFERENCES (**Concept_Referenced**)
        - (**Writeup**) EXPLAINS (**Threat_Model**)
        - (**Writeup**) TEACHES (**Security_Principle**)
        - (**Solution_Method**) DERIVED_FROM (**Past_CTF_Solution**)
        - (**Malware_Sample**) ANALYZED_IN (**CTF_Challenge**)
        - (**Tool_Used**) ANALYZES (**File_Analyzed**)
        - (**Writeup**) MENTIONS (**CTF_Event**)

        ---

        #### Example Graph Representation
        For a real-world example, let's say there is a challenge in the DEFCON CTF called "Buffer Overflow 101". Extract knowledge graph in JSON format would look like:

        {{
            "entities": [
                {{"name": "DEFCON CTF 2023", "type": "CTF_Event"}},
                {{"name": "Buffer Overflow 101", "type": "CTF_Challenge"}},
                {{"name": "Pwn", "type": "Challenge_Category"}},
                {{"name": "Hard", "type": "Challenge_Difficulty"}},
                {{"name": "Buffer Overflow", "type": "Vulnerability_Type"}},
                {{"name": "Return Oriented Programming", "type": "Exploit_Technique"}},
                {{"name": "ASLR", "type": "Security_Mechanism"}},
                {{"name": "user123", "type": "Solver"}},
                {{"name": "Stack Overflow Exploit", "type": "Solution_Method"}},
                {{"name": "GDB", "type": "Tool_Used"}},
                {{"name": "pwntools", "type": "Tool_Used"}},
                {{"name": "vuln.c", "type": "File_Analyzed"}},
                {{"name": "TCP", "type": "Network_Protocol"}},
                {{"name": "1337", "type": "Port_Number"}},
                {{"name": "Writeup_1", "type": "Writeup"}}
            ],
            "relationships": [
                {{"source": "DEFCON CTF 2023", "relation": "CONTAINS", "target": "Buffer Overflow 101"}},
                {{"source": "Buffer Overflow 101", "relation": "BELONGS_TO", "target": "Pwn"}},
                {{"source": "Buffer Overflow 101", "relation": "HAS_DIFFICULTY", "target": "Hard"}},
                {{"source": "Buffer Overflow 101", "relation": "INVOLVES", "target": "Buffer Overflow"}},
                {{"source": "Buffer Overflow 101", "relation": "USES", "target": "TCP"}},
                {{"source": "Buffer Overflow 101", "relation": "OPEN_ON", "target": "1337"}},
                {{"source": "Buffer Overflow", "relation": "BYPASSES", "target": "ASLR"}},
                {{"source": "user123", "relation": "SOLVED", "target": "Buffer Overflow 101"}},
                {{"source": "user123", "relation": "WROTE", "target": "Writeup_1"}},
                {{"source": "Writeup_1", "relation": "DOCUMENTS", "target": "Stack Overflow Exploit"}},
                {{"source": "Stack Overflow Exploit", "relation": "USES", "target": "pwntools"}},
                {{"source": "pwntools", "relation": "ANALYZES", "target": "vuln.c"}}
            ]
        }}

        
        Here is the document content:
        {text}
        """

        response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a skilled cybersecurity professional."},
            {"role": "user", "content": prompt}
            ],
        response_format={"type": "json_object"}
        )
        try:
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"Error parsing JSON response: {e}")
            return {"entities": [], "relationships": []}
        # except json.JSONDecodeError:
        #     return {"entities": [], "relationships": []}
    
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
                try:
                    self.vector_db.insert_document(docs, collection)
                except Exception as e:
                    print(f"Error processing file: {path}\nError message: {e}")
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
            try:
                self.vector_db.insert_document(docs, collection)
            except Exception as e:
                print(f"Error processing file: {path}\nError message: {e}")
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
            try:
                self.vector_db.insert_document(docs, collection)
            except Exception as e:
                print(f"Error processing file: {path}\nError message: {e}")
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
        try:
            self.vector_db.insert_document(docs_processed_unique if unique else docs_processed, collection)
        except Exception as e:
            print(f"Error processing document: {e}")
    
    def get_db(self):
        return self.vector_db
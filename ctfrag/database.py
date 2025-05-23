import os
import tempfile
import requests
import datasets
import pandas as pd
from tqdm import tqdm
from langchain_community.document_loaders import TextLoader
import validators
from langchain.docstore.document import Document as LangchainDocument
from tqdm import tqdm
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    MarkdownTextSplitter,
    PythonCodeTextSplitter,
    RecursiveJsonSplitter,
    NLTKTextSplitter,
    HTMLHeaderTextSplitter,
    TokenTextSplitter
)
import json
import yaml
from unstructured.partition.pdf import partition_pdf
from ctfrag.db_backend.base import BaseVectorDB
import openai
from langchain_core.documents import Document
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time
from tqdm import tqdm
import os
from datetime import datetime
import colorama
from colorama import Fore
import curses

from langchain_openai import ChatOpenAI #OpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer

colorama.init()

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
        self.start_time = datetime.now()
        
    def increment(self):
        with self.lock:
            self.value += 1
            return self.value
    
    def get_eta(self, total):
        if self.value <= 0:
            return "Estimating..."
        
        elapsed = (datetime.now() - self.start_time).total_seconds()
        if elapsed <= 0:
            return "Estimating..."
            
        items_per_second = self.value / elapsed
        if items_per_second <= 0:
            return "Estimating..."
            
        remaining_items = total - self.value
        remaining_seconds = remaining_items / items_per_second
        
        if remaining_seconds < 60:
            return f"~ {int(remaining_seconds)} seconds"
        elif remaining_seconds < 3600:
            return f"~ {int(remaining_seconds/60)} minutes"
        else:
            hours = int(remaining_seconds / 3600)
            minutes = int((remaining_seconds % 3600) / 60)
            return f"~ {hours}h {minutes}m"
    
    def get_elapsed(self):
        elapsed = (datetime.now() - self.start_time).total_seconds()
        if elapsed < 60:
            return f"{int(elapsed)} seconds"
        elif elapsed < 3600:
            return f"{int(elapsed/60)} minutes"
        else:
            hours = int(elapsed / 3600)
            minutes = int((elapsed % 3600) / 60)
            return f"{hours}h {minutes}m"

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

    def _parse_file(self, path, collection, embeddings, args):
        chunk_size = args.get("chunk_size", 2048)
        chunk_overlap = args.get("overlap", 100)
        if args.get("auto_splitter", True):
            text_splitter = self._get_smart_splitter(path, args)
        else:
            text_splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
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
            
    def _parse_file_graphdb(self, path, collection, args):
        chunk_size = args.get("chunk_size", 2048)
        chunk_overlap = args.get("overlap", 100)
        if path.endswith(".md") or path.endswith(".txt"):
            loader = TextLoader(path)
            documents = loader.load()
            text_splitter = TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            texts = text_splitter.split_documents(documents)
            extracted_data = self.extract_kg(texts)
            try:
                self.vector_db.insert_document(extracted_data, collection)
                self.vector_db.insert_embeddings_from_documents(texts, collection)  # store embeddings
                self.vector_db.index_graph(collection)
            except Exception as e:
                print(f"Error processing file: {path}\nError message: {e}")
        else:
            print("The files is not .md or .txt format.")

    def extract_kg(self, texts):
        llm=ChatOpenAI(temperature=0, model_name="gpt-4o") 
        llm_transformer = LLMGraphTransformer(llm=llm)
        graph_documents = llm_transformer.convert_to_graph_documents(texts)
        return graph_documents

    def fast_load_dataset(self, path=None, embeddings=None, collection="default", database="neo4j", args: dict = {
            "name_field": "key",
            "data_field": "value",
            "collection": "ctfrag",
            "chunk_size": 512,
            "overlap": 50,
            "max_workers": 8,
            "auto_splitter": True
        }):
        
        if not path:
            print("Please provide a file path")
            return
            
        if not os.path.isdir(path):
            print("Not a directory, loading single file...")
            if database == "neo4j":
                self._parse_file_graphdb(path, collection, args)
            else:
                self._parse_file(path, collection, embeddings, args)
            return
        
        print("Directory detected, loading in batch with multiple threads...")
        files = self._walk_dir(path)
        max_workers = int(args.get("max_workers", 8))
        
        thread_status = {}
        status_lock = threading.Lock()
        colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        
        processed_counter = Counter()
        stop_event = threading.Event()
        
        def update_status(thread_id, file, status="processing"):
            with status_lock:
                thread_status[thread_id] = {
                    "file": os.path.basename(file),
                    "status": status,
                    "updated_at": datetime.now(),
                    "color": colors[thread_id % len(colors)]
                }
        
        def curses_display(stdscr):
            curses.curs_set(0)
            curses.start_color()
            curses.use_default_colors()
            for i in range(1, 7):
                curses.init_pair(i, i, -1)
            
            def display_status_curses():
                stdscr.clear()
                height, width = stdscr.getmaxyx()
                
                total_files = len(files)
                processed_files = processed_counter.value
                
                if total_files > 0:
                    percentage = processed_files / total_files * 100
                else:
                    percentage = 0

                eta = processed_counter.get_eta(total_files)
                elapsed = processed_counter.get_elapsed()
                
                bar_length = min(width - 30, 50)
                filled_length = int(bar_length * processed_files // (total_files or 1))
                
                stdscr.addstr(0, 0, f"Progress: {processed_files}/{total_files} ({percentage:.1f}%)")
                progress_bar = "█" * filled_length + "-" * (bar_length - filled_length)
                stdscr.addstr(1, 0, f"|{progress_bar}|")

                stdscr.addstr(2, 0, f"Elapsed: {elapsed} | ETA: {eta}")
                
                stdscr.addstr(3, 0, "Active threads (showing last 5 updates):")
                stdscr.addstr(4, 0, "─" * min(width-1, 60))
                
                with status_lock:
                    recent_threads = sorted(
                        thread_status.items(),
                        key=lambda x: x[1]["updated_at"], 
                        reverse=True
                    )[:5]
                    
                    for i, (thread_id, info) in enumerate(recent_threads, 1):
                        if 5 + i >= height:
                            break
                            
                        color_idx = (thread_id % 6) + 1
                        file = info["file"]
                        if len(file) > 25:
                            file = file[:22] + "..."
                        status = info["status"]
                        updated_at = info["updated_at"].strftime("%H:%M:%S")
                        
                        status_icon = "⚡" if status == "processing" else "✓"
                        thread_info = f"Thread-{thread_id%1000}: {status_icon} {file:<25} | {status[:20]} | {updated_at}"
                        
                        try:
                            stdscr.addstr(4 + i, 0, thread_info, curses.color_pair(color_idx))
                        except:
                            pass
                
                footer_line = min(height-3, 11)
                stdscr.addstr(footer_line, 0, "─" * min(width-1, 60))
                stdscr.refresh()
                return height, width
            
            def status_thread_func():
                while not stop_event.is_set():
                    try:
                        display_status_curses()
                        time.sleep(0.3)
                    except:
                        pass
            
            status_thread = threading.Thread(target=status_thread_func)
            status_thread.daemon = True
            status_thread.start()
            
            if database == "neo4j":
                def process_file(file):
                    thread_id = threading.get_ident()
                    update_status(thread_id, file)
                    try:
                        self._parse_file_graphdb(file, collection, args)
                        update_status(thread_id, file, "completed")
                    except Exception as e:
                        update_status(thread_id, file, f"error: {str(e)[:50]}")
                    finally:
                        processed_counter.increment()
                
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    future_to_file = {executor.submit(process_file, file): file for file in files}
                    for future in as_completed(future_to_file):
                        file = future_to_file[future]
                        try:
                            future.result()
                        except Exception as e:
                            print(f"Error processing {file}: {e}")
            else:    
                def process_file(file):
                    thread_id = threading.get_ident()
                    update_status(thread_id, file)
                    try:
                        self._parse_file(file, collection, embeddings, args)
                        update_status(thread_id, file, "completed")
                    except Exception as e:
                        update_status(thread_id, file, f"error: {str(e)[:50]}")
                    finally:
                        processed_counter.increment()
                
                with ThreadPoolExecutor(max_workers=max_workers) as executor:
                    future_to_file = {executor.submit(process_file, file): file for file in files}
                    for future in as_completed(future_to_file):
                        file = future_to_file[future]
                        try:
                            future.result()
                        except Exception as e:
                            print(f"Error processing {file}: {e}")
            
            stop_event.set()
            status_thread.join(timeout=2.0)
            if status_thread.is_alive():
                print("Warning: Status thread did not exit cleanly")
            
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            
            stdscr.addstr(0, 0, "Processing completed!")
            stdscr.addstr(1, 0, f"Total files: {len(files)}")
            stdscr.addstr(2, 0, f"Processed files: {processed_counter.value}")
            
            error_count = sum(1 for info in thread_status.values() if "error" in info["status"])
            stdscr.addstr(3, 0, f"Failed files: {error_count}")
            
            if error_count > 0:
                stdscr.addstr(5, 0, "Errors:")
                line = 6
                for thread_id, info in thread_status.items():
                    if "error" in info["status"]:
                        error_line = f"- {info['file']}: {info['status']}"
                        try:
                            stdscr.addstr(line, 0, error_line[:width-1])
                            line += 1
                            if line >= height - 1:
                                break
                        except:
                            pass

            stdscr.addstr(height-1, 0, "Auto-exiting in 3 seconds...")
            stdscr.refresh()
            stdscr.nodelay(True)
            exit_time = time.time() + 3
            while time.time() < exit_time:
                if stdscr.getch() != -1:
                    break
                time.sleep(0.1)
            
            # stdscr.addstr(height-1, 0, "Press any key to exit...")
            # stdscr.refresh()
            # stdscr.getch()
        
        curses.wrapper(curses_display)
        
        error_count = sum(1 for info in thread_status.values() if "error" in info["status"])
        if error_count > 0:
            print("\nErrors:")
            for thread_id, info in thread_status.items():
                if "error" in info["status"]:
                    print(f"- {info['file']}: {info['status']}")

    def load_dataset(self, path=None, embeddings=None, collection="default", database="neo4j", args: dict = {
        "name_field": "key",
        "data_field": "value",
        "collection": "ctfrag",
        "chunk_size": 2048,
        "overlap": 100,
        "auto_splitter": True
    }):
        
        if database=="neo4j":
            if not path:
                print("Please provide a file path")
                return
            if not os.path.isdir(path):
                print("Not a directory, loading single file...")
                self._parse_file_graphdb(path, collection, args)
            else:
                print("Directory detected, loading in batch...")
                files = self._walk_dir(path)
                for file in tqdm(files):
                    self._parse_file_graphdb(file, collection, args)
        else:
            if not path:
                print("Please provide a url or file path")
                return
            if not os.path.isdir(path):
                print("Not a directory, loading single file...")
                self._parse_file(path, collection, embeddings, args)
            else:
                print("Directory detected, loading in batch...")
                files = self._walk_dir(path)
                for file in tqdm(files):
                    self._parse_file(file, collection, embeddings, args)

    def _walk_dir(self, dir):
        all_files = []
        for root, dirs, files in os.walk(dir):
            for file in files:
                file_path = os.path.join(root, file)
                all_files.append(file_path)
        return all_files
    
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
            if path.endswith(".csv"):
                document = Document(page_content=value, metadata={"name": key})
            else:
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
    
    def delete_db(self, collection):
        self.vector_db.delete_collection(collection)
    
    def view_samples(self, collection, limit=10):
        return self.vector_db.view_samples(collection, limit)
    
    def _get_smart_splitter(self, path, args):
        chunk_size = args.get("chunk_size", 2048)
        chunk_overlap = args.get("overlap", 100)
        
        if os.path.isdir(path):
            files = self._walk_dir(path)
            if not files:
                return RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            file_to_check = files[0]
        else:
            file_to_check = path
        
        _, ext = os.path.splitext(file_to_check.lower())
        if ext in ['.md', '.markdown']:
            # print(f"Using Markdown splitter for {ext} files")
            return MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        
        elif ext in ['.py', '.js', '.java', '.c', '.cpp', '.cs', '.go', '.rb', '.php', '.r', '.swift']:
            # print(f"Using Code splitter for {ext} files")
            if ext == '.py':
                return PythonCodeTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            else:
                return RecursiveCharacterTextSplitter(
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                    separators=["\nclass ", "\ndef ", "\nfunction ", "\nif ", "\n\n", "\n", " ", ""]
                )
        
        elif ext in ['.html', '.htm', '.xml']:
            # print(f"Using HTML Header splitter for {ext} files")
            return HTMLHeaderTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        
        elif ext in ['.json', '.jsonl']:
            # print(f"Using Recursive JSON splitter for {ext} files")
            return RecursiveJsonSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        
        elif ext in ['.txt', '.log']:
            # print(f"Using NLTK splitter for {ext} files")
            return NLTKTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        
        elif ext in ['.csv', '.tsv']:
            # print(f"Using Character splitter for {ext} files")
            return RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                separators=["\n\n", "\n", ". ", ", ", " ", ""]
            )

        try:
            with open(file_to_check, 'r', encoding='utf-8') as f:
                content_sample = f.read(1000)

            if content_sample.startswith('# ') or '## ' in content_sample or '### ' in content_sample:
                # print("Content appears to be Markdown, using Markdown splitter")
                return MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

            if content_sample.strip().startswith('<') and ('</html>' in content_sample or '</div>' in content_sample):
                # print("Content appears to be HTML, using HTML Header splitter")
                return HTMLHeaderTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

            if content_sample.strip().startswith('{') and '}' in content_sample:
                # print("Content appears to be JSON, using Recursive JSON splitter")
                return RecursiveJsonSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

            code_indicators = ['def ', 'class ', 'function ', 'import ', 'from ', '#include', 'public class']
            if any(indicator in content_sample for indicator in code_indicators):
                # print("Content appears to be code, using Code splitter")
                return RecursiveCharacterTextSplitter(
                    chunk_size=chunk_size,
                    chunk_overlap=chunk_overlap,
                    separators=["\nclass ", "\ndef ", "\nfunction ", "\nif ", "\n\n", "\n", " ", ""]
                )

            sentences = content_sample.split('.')
            avg_sentence_length = sum(len(s.strip()) for s in sentences if s.strip()) / max(1, len([s for s in sentences if s.strip()]))
            if avg_sentence_length > 30:
                # print("Content appears to be natural language, using NLTK splitter")
                return NLTKTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
                
        except Exception as e:
            print(f"Error analyzing file content: {str(e)}")
            pass

        # print(f"Using default recursive splitter for {ext} files")
        return RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
# from ragflow_sdk import RAGFlow
# from pathlib import Path
# import os

# with open(Path(__file__).resolve().parent.parent / "api_keys", "r") as f:
#     for line in f:
#         key, value = line.strip().split("=")
#         os.environ[key] = value

# class RAGFlowEngine:
#     def __init__(self, api_key, url):
#         self.api_key = api_key
#         self.url = url
#         self.rag_object = RAGFlow(api_key=api_key, base_url=url)

#     def create_dataset(self, name: str):
#         return self.rag_object.create_dataset(name)
    
#     def delete_dataset(self, ids: list):
#         return self.rag_object.delete_dataset(ids)
    
#     def list_datasets(self, id=None):
#         if id:
#             dataset = self.rag_object.list_datasets(id = id)
#             print(dataset)
#         else:
#             for dataset in self.rag_object.list_datasets():
#                 print(dataset)

#     def update_datasets(self, name, embedding_model, chunk_methods):
#         dataset = self.rag_object.list_datasets(name=name)
#         dataset.update({"embedding_model":embedding_model, "chunk_method":chunk_methods})

#         # example: [{"display_name": "1.txt", "blob": "<BINARY_CONTENT_OF_THE_DOC>"}, {"display_name": "2.pdf", "blob": "<BINARY_CONTENT_OF_THE_DOC>"}]
#     def upload_documents(self, name, documents):
#         dataset = self.rag_object.upload_documents(name=name)
#         dataset.upload_documents(documents)

#     # example: [{"parser_config": {"chunk_token_count": 256}}, {"chunk_method": "manual"}]
#     def update_document(self, ds_id, ds_index, doc_id, doc_index, config):
#         dataset = self.rag_object.list_datasets(id=ds_id)[ds_index]
#         doc = dataset.list_documents(id=doc_id)[doc_index]
#         doc.update(config)

#     def download_document(self, ds_id, ds_index, doc_id, doc_index, path):
#         dataset = self.rag_object.list_datasets(id=ds_id)[ds_index]
#         doc = dataset.list_documents(id=doc_id)[doc_index]
#         open(path, "wb+").write(doc.download())
#         print(doc)

#     def list_documents(self, name, keywords, page, page_size):
#         dataset = self.rag_object.list_datasets(name=name)
#         for doc in dataset.list_documents(keywords=keywords, page=page, page_size=page_size):
#             print(doc)

#     def delete_documents(self, name, ds_index, doc_ids):
#         dataset = self.rag_object.list_datasets(name=name)[ds_index]
#         dataset.delete_documents(doc_ids)

#     def parse_documents(self, name, path, keywords):
#         dataset = self.rag_object.list_datasets(name=name)
#         documents = [{"display_name": doc.strip().split("/"), "blob": open(doc, "rb").read()} for doc in os.listdir(path)]
#         dataset.upload_documents(documents)
#         documents = dataset.list_documents(keywords=keywords)
#         ids = []
#         for document in documents:
#             ids.append(document.id)
#         dataset.async_parse_documents(ids)
#         print("Async bulk parsing initiated.")

#     def stop_parseing(self, name, path, keywords):
#         dataset = self.rag_object.list_datasets(name=name)
#         documents = [{"display_name": doc.strip().split("/"), "blob": open(doc, "rb").read()} for doc in os.listdir(path)]
#         dataset.upload_documents(documents)
#         documents = dataset.list_documents(keywords=keywords)
#         ids = []
#         for document in documents:
#             ids.append(document.id)
#         dataset.async_parse_documents(ids)
#         print("Async bulk parsing initiated.")
#         dataset.async_cancel_parse_documents(ids)
#         print("Async bulk parsing cancelled.")

#     def add_chunk(self, ds_id, ds_index, doc_id, doc_index, content):
#         dataset = self.rag_object.list_datasets(id=ds_id)[ds_index]
#         doc = dataset.list_documents(id=doc_id)[doc_index]
#         chunk = doc.add_chunk(content)
#         print(chunk)
    
#     def list_chunks(self, ds_id, ds_index, 
#                     doc_keyword, doc_page, doc_page_size, 
#                     chunk_keyword, chunk_page, chunk_page_size):
#         dataset = self.rag_object.list_datasets(id=ds_id)[ds_index]
#         doc = dataset.list_documents(keywords=doc_keyword, page=doc_page, page_size=doc_page_size)
#         for chunk in doc.list_chunks(keywords=chunk_keyword, page=chunk_page, page_size=chunk_page_size):
#             print(chunk)
    
#     def delete_chunks(self, ds_id, ds_index, doc_id, doc_index, chunk_ids):
#         dataset = self.rag_object.list_datasets(id=ds_id)[ds_index]
#         doc = dataset.list_documents(id=doc_id)[doc_index]
#         doc.delete_chunks(chunk_ids)

#     def delete_chunks(self, ds_id, ds_index, doc_id, doc_index, content):
#         dataset = self.rag_object.list_datasets(id=ds_id)[ds_index]
#         doc = dataset.list_documents(id=doc_id)[doc_index]
#         doc.update({"content": content})

#     def retrieve_chunks(self, ds_id, ds_index, doc_id, doc_index):
#         dataset = self.rag_object.list_datasets(name=ds_id)[ds_index]
#         doc = dataset.list_documents(id=doc_id)[doc_index]
#         for c in self.rag_object.retrieve(dataset_ids=[dataset.id],document_ids=[doc.id]):
#             print(c)

#     def create_chat(self, name, chat_name):
#         datasets = self.rag_object.list_datasets(name=name)
#         dataset_ids = []
#         for dataset in datasets:
#             dataset_ids.append(dataset.id)
#         return self.rag_object.create_chat(chat_name, dataset_ids=dataset_ids)
    
#     # Example: {"name": "Stefan", "llm": {"temperature": 0.8}, "prompt": {"top_n": 8}}
#     def update_chat(self, name, chat_name, config):
#         assistant = self.create_chat(name, chat_name)
#         assistant.update(config)

#     def delete_chat(self, ids):
#         self.rag_object.delete_chat(ids)

#     def list_chats(self):
#         for assistant in self.rag_object.list_chats():
#             print(assistant)

#     def create_session(self, chat_name, chat_index):
#         assistant = self.rag_object.list_chats(name=chat_name)[chat_index]
#         return assistant.create_session()
    
#     # Example: {"name": "updated_name"}
#     def update_session(self, chat_name, chat_index, session_id, new_name):
#         assistant = self.rag_object.list_chats(name=chat_name)[chat_index]
#         session = assistant.list_sessions(id=session_id)
#         session.update({"name": new_name})

#     def list_sessions(self, chat_name, chat_index):
#         assistant = self.rag_object.list_chats(name=chat_name)[chat_index]
#         for session in assistant.list_sessions():
#             print(session)

#     def delete_session(self, chat_name, chat_index, session_ids):
#         assistant = self.rag_object.list_chats(name=chat_name)[chat_index]
#         assistant.delete_sessions(session_ids)

#     def generate_chat(self, session, question, stream=False):
#         cont = []
#         for ans in session.ask(question, stream=stream):
#             print(ans.content[len(cont):], end='', flush=True)
#             cont.append(ans.content)
#         return cont
    
#     def create_agent_session(self, agent_id, agent_index):
#         agent = self.rag_object.list_agents(id=agent_id)[agent_index]
#         return agent.create_session()
    
#     def generate_agent(self, session, question, stream=False):
#         cont = []
#         for ans in session.ask(question, stream=stream):
#             print(ans.content[len(cont):], end='', flush=True)
#             cont.append(ans.content)
#         return cont
    
#     def list_agents_session(self, agent_id, agent_index):
#         agent = self.rag_object.list_agents(id = agent_id)[agent_index]
#         sessions = agent.list_sessions()
#         for session in sessions:
#             print(session)

#     def delete_agent(self, agent_id, agent_index, session_ids):
#         agent = self.rag_object.list_agents(id = agent_id)[agent_index]
#         agent.delete_sessions(ids=session_ids)

#     def list_agents(self):
#         for agent in self.rag_object.list_agents():
#             print(agent)
from ragflow_sdk import RAGFlow
from pathlib import Path
import os

def load_api_keys():
    """Load API keys from config file"""
    keys_path = Path(__file__).resolve().parent.parent / "api_keys"
    if keys_path.exists():
        with open(keys_path, "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                os.environ[key] = value

class RAGFlowEngine:
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.url = url
        self.rag_object = RAGFlow(api_key=api_key, base_url=url)

    # Helper methods to reduce repetition
    def _get_dataset(self, dataset_id=None, name=None, index=0):
        """Get dataset by ID, name, or index"""
        if dataset_id:
            datasets = self.rag_object.list_datasets(id=dataset_id)
            return datasets[index] if isinstance(datasets, list) else datasets
        elif name:
            datasets = self.rag_object.list_datasets(name=name)
            return datasets[index] if isinstance(datasets, list) else datasets
        return None

    def _get_document(self, dataset, doc_id=None, keywords=None, page=None, page_size=None, index=0):
        """Get document from dataset"""
        if doc_id:
            docs = dataset.list_documents(id=doc_id)
            return docs[index] if isinstance(docs, list) else docs
        elif keywords or page or page_size:
            return dataset.list_documents(keywords=keywords, page=page, page_size=page_size)
        return None

    # Dataset operations
    def create_dataset(self, name):
        """Create a new dataset"""
        return self.rag_object.create_dataset(name)
    
    def delete_dataset(self, ids):
        """Delete datasets by IDs"""
        return self.rag_object.delete_dataset(ids)
    
    def list_datasets(self, dataset_id=None, name=None):
        """List datasets with optional filtering"""
        if dataset_id:
            dataset = self.rag_object.list_datasets(id=dataset_id)
            print(dataset)
            return dataset
        elif name:
            return self.rag_object.list_datasets(name=name)
        else:
            datasets = self.rag_object.list_datasets()
            for dataset in datasets:
                print(dataset)
            return datasets

    def update_dataset(self, name, **config):
        """Update dataset configuration"""
        dataset = self._get_dataset(name=name)
        if dataset:
            dataset.update(config)
            return dataset
        return None

    # Document operations
    def upload_documents(self, dataset_name, documents):
        """Upload documents to a dataset
        
        Args:
            dataset_name: Name of the dataset
            documents: List of document objects in format 
                [{"display_name": "file.txt", "blob": binary_content}, ...]
        """
        dataset = self._get_dataset(name=dataset_name)
        if dataset:
            return dataset.upload_documents(documents)
        return None

    def parse_documents_from_dir(self, dataset_name, directory_path, keywords=None):
        """Upload and parse documents from a directory"""
        dataset = self._get_dataset(name=dataset_name)
        if not dataset or not Path(directory_path).exists():
            return None
        
        documents = []
        for doc_path in Path(directory_path).iterdir():
            if doc_path.is_file():
                with open(doc_path, "rb") as f:
                    documents.append({
                        "display_name": doc_path.name,
                        "blob": f.read()
                    })
        
        if documents:
            dataset.upload_documents(documents)
            
            # Get uploaded document IDs
            uploaded_docs = dataset.list_documents(keywords=keywords)
            doc_ids = [doc.id for doc in uploaded_docs]
            
            if doc_ids:
                dataset.async_parse_documents(doc_ids)
                print(f"Async bulk parsing initiated for {len(doc_ids)} documents.")
                return doc_ids
        
        return None

    def cancel_parsing(self, dataset_name, doc_ids):
        """Cancel ongoing document parsing"""
        dataset = self._get_dataset(name=dataset_name)
        if dataset and doc_ids:
            dataset.async_cancel_parse_documents(doc_ids)
            print(f"Async bulk parsing cancelled for {len(doc_ids)} documents.")
            return True
        return False

    def list_documents(self, dataset_name=None, dataset_id=None, keywords=None, page=1, page_size=10):
        """List documents with pagination and filtering"""
        dataset = self._get_dataset(dataset_id=dataset_id, name=dataset_name)
        if dataset:
            docs = dataset.list_documents(keywords=keywords, page=page, page_size=page_size)
            for doc in docs:
                print(doc)
            return docs
        return None

    def update_document(self, dataset_id=None, dataset_name=None, doc_id=None, **config):
        """Update document configuration"""
        dataset = self._get_dataset(dataset_id=dataset_id, name=dataset_name)
        if dataset:
            doc = self._get_document(dataset, doc_id=doc_id)
            if doc:
                doc.update(config)
                return doc
        return None

    def delete_documents(self, dataset_name=None, dataset_id=None, doc_ids=None):
        """Delete documents from a dataset"""
        dataset = self._get_dataset(dataset_id=dataset_id, name=dataset_name)
        if dataset and doc_ids:
            dataset.delete_documents(doc_ids)
            return True
        return False

    def download_document(self, dataset_id=None, dataset_name=None, doc_id=None, output_path=None):
        """Download document content to file"""
        dataset = self._get_dataset(dataset_id=dataset_id, name=dataset_name)
        if dataset and doc_id and output_path:
            doc = self._get_document(dataset, doc_id=doc_id)
            if doc:
                with open(output_path, "wb+") as f:
                    f.write(doc.download())
                print(f"Document saved to {output_path}")
                return True
        return False

    # Chunk operations
    def add_chunk(self, dataset_id=None, dataset_name=None, doc_id=None, content=None):
        """Add a chunk to document"""
        dataset = self._get_dataset(dataset_id=dataset_id, name=dataset_name)
        if dataset and doc_id and content:
            doc = self._get_document(dataset, doc_id=doc_id)
            if doc:
                chunk = doc.add_chunk(content)
                print(chunk)
                return chunk
        return None
    
    def list_chunks(self, dataset_id=None, dataset_name=None, doc_id=None, 
                  chunk_keywords=None, chunk_page=1, chunk_page_size=10):
        """List document chunks with filtering and pagination"""
        dataset = self._get_dataset(dataset_id=dataset_id, name=dataset_name)
        if dataset and doc_id:
            doc = self._get_document(dataset, doc_id=doc_id)
            if doc:
                chunks = doc.list_chunks(
                    keywords=chunk_keywords, 
                    page=chunk_page, 
                    page_size=chunk_page_size
                )
                for chunk in chunks:
                    print(chunk)
                return chunks
        return None
    
    def delete_chunks(self, dataset_id=None, dataset_name=None, doc_id=None, chunk_ids=None):
        """Delete chunks from a document"""
        dataset = self._get_dataset(dataset_id=dataset_id, name=dataset_name)
        if dataset and doc_id and chunk_ids:
            doc = self._get_document(dataset, doc_id=doc_id)
            if doc:
                doc.delete_chunks(chunk_ids)
                return True
        return False

    def update_chunk_content(self, dataset_id=None, dataset_name=None, doc_id=None, content=None):
        """Update document content"""
        dataset = self._get_dataset(dataset_id=dataset_id, name=dataset_name)
        if dataset and doc_id and content:
            doc = self._get_document(dataset, doc_id=doc_id)
            if doc:
                doc.update({"content": content})
                return True
        return False

    def retrieve_chunks(self, dataset_id=None, dataset_name=None, doc_id=None):
        """Retrieve chunks from document"""
        dataset = self._get_dataset(dataset_id=dataset_id, name=dataset_name)
        if dataset and doc_id:
            doc = self._get_document(dataset, doc_id=doc_id)
            if doc:
                results = self.rag_object.retrieve(
                    dataset_ids=[dataset.id],
                    document_ids=[doc.id]
                )
                for chunk in results:
                    print(chunk)
                return results
        return None

    # Chat operations
    def create_chat(self, dataset_name, chat_name):
        """Create a new chat based on dataset"""
        datasets = self.rag_object.list_datasets(name=dataset_name)
        dataset_ids = [dataset.id for dataset in datasets]
        return self.rag_object.create_chat(chat_name, dataset_ids=dataset_ids)
    
    def update_chat(self, chat_name, **config):
        """Update chat configuration"""
        chats = self.rag_object.list_chats(name=chat_name)
        if chats:
            chat = chats[0]
            chat.update(config)
            return chat
        return None

    def delete_chat(self, chat_ids):
        """Delete chats by IDs"""
        return self.rag_object.delete_chat(chat_ids)

    def list_chats(self, chat_name=None):
        """List all chats or filter by name"""
        if chat_name:
            return self.rag_object.list_chats(name=chat_name)
        else:
            chats = self.rag_object.list_chats()
            for chat in chats:
                print(chat)
            return chats

    # Session operations
    def create_session(self, chat_name=None, agent_id=None):
        """Create a new session for chat or agent"""
        if chat_name:
            chats = self.rag_object.list_chats(name=chat_name)
            if chats:
                return chats[0].create_session()
        elif agent_id:
            agents = self.rag_object.list_agents(id=agent_id)
            if agents:
                return agents[0].create_session()
        return None
    
    def update_session(self, session_id, chat_name=None, agent_id=None, **config):
        """Update session settings"""
        if chat_name:
            chats = self.rag_object.list_chats(name=chat_name)
            if chats:
                session = chats[0].list_sessions(id=session_id)
                if session:
                    session.update(config)
                    return session
        elif agent_id:
            agents = self.rag_object.list_agents(id=agent_id)
            if agents:
                session = agents[0].list_sessions(id=session_id)
                if session:
                    session.update(config)
                    return session
        return None

    def list_sessions(self, chat_name=None, agent_id=None):
        """List sessions for chat or agent"""
        if chat_name:
            chats = self.rag_object.list_chats(name=chat_name)
            if chats:
                sessions = chats[0].list_sessions()
                for session in sessions:
                    print(session)
                return sessions
        elif agent_id:
            agents = self.rag_object.list_agents(id=agent_id)
            if agents:
                sessions = agents[0].list_sessions()
                for session in sessions:
                    print(session)
                return sessions
        return None

    def delete_sessions(self, session_ids, chat_name=None, agent_id=None):
        """Delete sessions from chat or agent"""
        if chat_name:
            chats = self.rag_object.list_chats(name=chat_name)
            if chats:
                chats[0].delete_sessions(session_ids)
                return True
        elif agent_id:
            agents = self.rag_object.list_agents(id=agent_id)
            if agents:
                agents[0].delete_sessions(session_ids)
                return True
        return False

    # Generation operations
    def generate_response(self, session, question, stream=False):
        """Generate response from a session (works for both chat and agent sessions)"""
        if session:
            content = []
            for response in session.ask(question, stream=stream):
                new_content = response.content[len(''.join(content)):]
                print(new_content, end='', flush=True)
                content.append(new_content)
            return ''.join(content)
        return None

    # Agent operations
    def list_agents(self):
        """List all available agents"""
        agents = self.rag_object.list_agents()
        for agent in agents:
            print(agent)
        return agents


# Example of usage with the refactored code:
if __name__ == "__main__":
    pass
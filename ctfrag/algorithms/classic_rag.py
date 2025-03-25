from ctfrag.algorithms.base import RAGAlgorithms, State, RetrieverWrap
from ctfrag.database import RAGDatabase
from ctfrag.config import RetrieverConfig
from ctfrag.database import RAGDatabase
from ctfrag.backends import LLMs
from langgraph.graph import START, StateGraph
from langchain_core.documents import Document
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.document_compressors.rankllm_rerank import RankLLMRerank
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain.load import dumps, loads
from ctfrag.console import console, ConsoleType, log, LogNode
from ctfrag.utils import MetadataCaptureCallback, DocumentDisplayCallback

class ClassicRAG(RAGAlgorithms):
    def __init__(self, config: RetrieverConfig, llm: LLMs, wrap: RetrieverWrap, database: RAGDatabase, embeddings):
        super().__init__(config, llm, wrap, database, embeddings)
        self.graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph = self.graph_builder.compile()

    def chain_retrieve(self, query, collection, template, graph_lc=False) -> None:
        self._create_vector(collection=collection)
        self._create_template(template_str=template)
        metadata_callback = MetadataCaptureCallback()
        doc_callback = DocumentDisplayCallback()
        self._log.trajectories.append(LogNode.RETRIEVE.value)
        self._log.trajectories.append(LogNode.GENERATE.value)
        self._log.query.append(query)
        if graph_lc:
            result = self.graph.invoke({"question": query}, config={"callbacks": [metadata_callback]})
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
            source, context = log.parse_documents(result["context"])
            self._log.source.append(source)
            self._log.shortcut.append(context)
            return result["answer"]
        else:
            retriever = self.wrap.vector_store.as_retriever()
            rag_chain = (
                {"context": retriever,  "question": RunnablePassthrough()}
                | self.wrap.template
                | self.llm()
                | StrOutputParser()
            )
            result = rag_chain.invoke(query, config={"callbacks": [metadata_callback, doc_callback]})
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
            source, context = log.parse_documents(doc_callback.documents)
            self._log.source.append(source)
            self._log.shortcut.append(context)
            return result
        """ state = {"question": query, "context": [], "answer": ""}
        retrieval_result = self.retrieve(state)

        state["context"] = retrieval_result.get("context", [])

        generated_result = self.generate(state)
        return generated_result["answer"] """

    def _create_compressor(self, compressor: str):
        if compressor == "RankLLMRerank":
            if self.config.rag_config.reranker_model.startswith("gpt"):
                self.wrap.compressor = RankLLMRerank(top_n=self.config.rag_config.reranker_top_n, 
                                                     model="gpt", gpt_model=self.config.rag_config.reranker_model)
            else:
                self.wrap.compressor = RankLLMRerank(top_n=self.config.rag_config.reranker_top_n, 
                                                     model=self.config.rag_config.reranker_model)
            return
        if compressor == "LLMChainExtractor":
            self.wrap.compressor = LLMChainExtractor.from_llm(self.llm())
            return
        
    def _create_cretriever(self, cretriever: str):
        if cretriever == "ContextualCompressionRetriever":
            self.wrap.cretriever = ContextualCompressionRetriever(
                base_compressor=self.wrap.compressor, base_retriever=self.wrap.retriever
            )
            return
    
    


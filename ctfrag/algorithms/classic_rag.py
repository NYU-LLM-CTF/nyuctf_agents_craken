from ctfrag.algorithms.base import RAGAlgorithms, State, RetrieverWrap
from ctfrag.database import RAGDatabase
from ctfrag.config import RetrieverConfig
from ctfrag.database import RAGDatabase
from ctfrag.backends import LLMs
from langgraph.graph import START, StateGraph
from langchain_core.documents import Document
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_community.document_compressors.rankllm_rerank import RankLLMRerank
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain.load import dumps, loads
from ctfrag.console import console

class ClassicRAG(RAGAlgorithms):
    def __init__(self, config: RetrieverConfig, llm: LLMs, wrap: RetrieverWrap, database: RAGDatabase, embeddings):
        super().__init__(config, llm, wrap, database, embeddings)
        self.graph_builder = StateGraph(State).add_sequence([self.retrieve, self.generate])
        self.graph_builder.add_edge(START, "retrieve")
        self.graph = self.graph_builder.compile()

    def _search(self, question):
        if self.config.feature_config.rerank:
            self._create_retriever()
            self._create_compressor(self.config.rag_config.reranker_type)
            self._create_cretriever(self.config.rag_config.compressor_retriever)
            return self.wrap.cretriever.invoke(question)
        if self.config.feature_config.compressor:
            self._create_retriever()
            self._create_compressor(self.config.rag_config.compressor_type)
            self._create_cretriever(self.config.rag_config.compressor_retriever)
            return self.wrap.cretriever.invoke(question)
        if self.config.rag_config.retriever_type == "similarity_search":
            return self.wrap.vector_store.similarity_search(question)

    def retrieve(self, state: State):
        if self.config.feature_config.question_rewriting:
            state["question"] = self.rewrite_question(state["question"])
        if self.config.feature_config.multi_query:
            questions = self._multi_query()
            retrieval_chain = (
                questions
                | self.wrap.vector_store.as_retriever().map()
                | self.get_unique_union
            )
            final_docs = retrieval_chain.invoke({"question": state["question"]})
        if self.config.feature_config.rag_fusion:
            questions = self._multi_query()

            queries = questions.invoke({"question": state["question"]})
            results = [self._search(query) for query in queries]
            unique_docs = self._reciprocal_rank_fusion(results)
            final_docs=unique_docs
        if self.config.feature_config.decomposition:
            sub_questions = self._decompose_question(state["question"])
            answer,q_a_results = self._answer_sub_questions(sub_questions)
            final_docs=q_a_results["q_a_pairs"]
            final_answer=answer
        if self.config.feature_config.step_back:
            step_back_query = self._generate_step_back_query(state["question"])
            _, step_back_context, synthesized_result = self._retrieve_step_back_context(state["question"], step_back_query)
            return {"context": step_back_context, "answer": synthesized_result}

        else:
            final_docs = self._search(state["question"])

        if not final_docs:
            console.overlay_print("---NO DOCUMENTS FOUND. RETURNING DEFAULT RESPONSE---", 5)
            final_docs = [Document(page_content="No relevant documents found.")]

        if self.config.feature_config.retrieval_grading:
            final_docs = self.grade_retrieval(state["question"], final_docs)
        if self.config.feature_config.decomposition:
            return {"context": final_docs, "answer": final_answer}
        if self.config.feature_config.step_back:
            return {"context": final_docs, "answer": final_answer}
        else:
            return {"context": final_docs}

    def chain_retrieve(self, query, collection, template, graph_lc=False) -> None:
        self._create_vector(collection=collection)
        self._create_template(template_str=template)
        if graph_lc:
            result = self.graph.invoke({"question": query})
            return result["answer"]
        else:
            retriever = self.wrap.vector_store.as_retriever()
            rag_chain = (
                {"context": retriever,  "question": RunnablePassthrough()}
                | self.wrap.template
                | self.llm
                | StrOutputParser()
            )
            result = rag_chain.invoke(query)
            return result
        """ state = {"question": query, "context": [], "answer": ""}
        retrieval_result = self.retrieve(state)

        state["context"] = retrieval_result.get("context", [])

        generated_result = self.generate(state)
        return generated_result["answer"] """

    def generate(self, state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = self.wrap.template.invoke({"question": state["question"], "context": docs_content})
        response = self.llm.invoke(messages)
        if self.config.feature_config.hallucination_grading:
            grounded_content = self.grade_hallucination(state["context"], response)

            if not grounded_content:
                return {
                    "error": "The response contains no verified factual content.",
                    "suggestion": "Consider refining your query for more accurate results."
                }
        if self.config.feature_config.answer_grading:
            is_relevant = self.grade_answer(state["question"], grounded_content)
            if not is_relevant:
                return {
                    "error": "The response does not directly answer the question.",
                    "suggestion": "Consider rephrasing your question or asking for specific details."
                }
        return {"answer": response.content}

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
            self.wrap.compressor = LLMChainExtractor.from_llm(self.llm)
            return
        
    def _create_cretriever(self, cretriever: str):
        if cretriever == "ContextualCompressionRetriever":
            self.wrap.cretriever = ContextualCompressionRetriever(
                base_compressor=self.wrap.compressor, base_retriever=self.wrap.retriever
            )
            return
    
        # Multi_query : generate five different versions of the given user question
    def _multi_query(self):
        prompt_perspectives = ChatPromptTemplate.from_template(template=self.config.prompts.rag_multi)
        
        generate_queries = (
            prompt_perspectives 
            | self.llm
            | StrOutputParser() 
            | (lambda x: x.split("\n"))
        )
        return generate_queries

    # Multi_query : only get the unique docs
    def get_unique_union(self, documents):
        flattened_docs = [dumps(doc) for sublist in documents for doc in sublist]
        unique_docs = list(set(flattened_docs)) 
        return [loads(doc) for doc in unique_docs]
    

    # Rag_fusion : rerank all documents
    def _reciprocal_rank_fusion(self, results: list[list], k=60):
        fused_scores = {}
        for docs in results:
            for rank, doc in enumerate(docs):
                doc_str = dumps(doc) 
                if doc_str not in fused_scores:
                    fused_scores[doc_str] = 0
                fused_scores[doc_str] += 1 / (rank + k)

        reranked_results = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)

        unique_docs = set()
        final_results = []

        for doc_str, _ in reranked_results:
            doc = loads(doc_str) 
            if doc_str not in unique_docs: 
                unique_docs.add(doc_str)
                final_results.append(doc)

        return final_results  

    # Decomposition : generates multiple sub-questions related to an input question
    def _decompose_question(self, question: str):
        prompt_decomposition = ChatPromptTemplate.from_template(template=self.config.prompts.rag_decompose)
        generate_queries_decomposition = (
            prompt_decomposition
            | self.llm
            | StrOutputParser()
            | (lambda x: x.split("\n"))
        )
        sub_questions = generate_queries_decomposition.invoke({"question": question})
        return sub_questions

    # Decomposition : format multiple sub-questions answers pairss
    def format_qa_pair(self, question, answer):
        formatted_string = ""
        formatted_string += f"Question: {question}\nAnswer: {answer}\n\n"
        return formatted_string.strip()
    
    # Decomposition : answer multiple sub-questions related to an input question 
    def _answer_sub_questions(self, sub_questions):
        decomposition_prompt = ChatPromptTemplate.from_template(template=self.config.prompts.rag_answer_decompose)

        q_a_pairs_list = [] 

        for q in sub_questions:
            if self.wrap.retriever is None:
                self._create_retriever()

            rag_chain = (
                {"context": lambda x: self.wrap.retriever.get_relevant_documents(x["question"]),  
                "question": lambda x: x["question"],
                "q_a_pairs": lambda x: "\n---\n".join(q_a_pairs_list)}  
                | decomposition_prompt
                | self.llm
                | StrOutputParser()
            )

            answer = rag_chain.invoke({"question": q, "q_a_pairs": "\n---\n".join(q_a_pairs_list)}) 
            q_a_pair = self.format_qa_pair(q, answer)
            q_a_pairs_list.append(q_a_pair) 

        return answer, {"q_a_pairs": "\n---\n".join(q_a_pairs_list)} 

    # Step_back : generate a step back question related to an input question
    def _generate_step_back_query(self, question: str):

        examples = [{"input": self.config.prompts.rag_step_back_inputs[i], "output": self.config.prompts.rag_step_back_outputs[i]} 
                    for i in range(len(self.config.prompts.rag_step_back_inputs))]
        example_prompt = ChatPromptTemplate.from_messages(
            [
                ("human", "{input}"),
                ("ai", "{output}"),
            ]
        )
        few_shot_prompt = FewShotChatMessagePromptTemplate(
            example_prompt=example_prompt,
            examples=examples,
        )
        step_back_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.prompts.rag_step_back_system),
                few_shot_prompt,
                ("user", "{question}"),
            ]
        )
        chain = (
            step_back_prompt
            | self.llm
            | StrOutputParser()
        )
        step_back_query = chain.invoke({"question": question})
        return step_back_query
    
    # Step_back : retrieve based on step back question
    def _retrieve_step_back_context(self, question: str, step_back_query: str):
        if self.wrap.retriever is None:
            self._create_retriever()

        response_prompt = ChatPromptTemplate.from_template(template=self.config.prompts.rag_step_back_response)

        normal_docs = self.wrap.retriever.get_relevant_documents(question)
        step_back_docs = self.wrap.retriever.get_relevant_documents(step_back_query)
        normal_context_text = "\n\n".join(doc.page_content for doc in normal_docs)
        step_back_context_text = "\n\n".join(doc.page_content for doc in step_back_docs)

        chain = (
            {
                "normal_context": lambda x: normal_context_text,
                "step_back_context": lambda x: step_back_context_text,
                "question": lambda x: x["question"],
            }
            | response_prompt
            | self.llm
            | StrOutputParser()
        )

        response = chain.invoke({"question": question})
        return {
            "response": response,
            "normal_context_docs": normal_docs,
            "step_back_context_docs": step_back_docs
        }


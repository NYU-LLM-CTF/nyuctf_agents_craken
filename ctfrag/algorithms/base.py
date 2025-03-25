from ctfrag.config import RetrieverConfig
from ctfrag.backends import LLMs
from typing_extensions import List, TypedDict
from langchain_core.documents import Document
from langchain.prompts import ChatPromptTemplate
from ctfrag.database import RAGDatabase
from pydantic import BaseModel, Field
from langchain.schema.output_parser import StrOutputParser
from ctfrag.utils import MetadataCaptureCallback
from ctfrag.console import log, RAGItem
from langchain.load import dumps, loads
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from ctfrag.console import console, ConsoleType, log, LogNode

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str
    recursion_depth: int

class RetrieverWrap:
    def __init__(self) -> None:
        self.retriever = None
        self.compressor = None
        self.cretriever = None
        self.vector_store = None
        self.prompt = None
        self.template = None

class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""
    binary_score: str = Field(description="Documents are relevant to the question, 'yes' or 'no'")

class GradeHallucinations(BaseModel):
    """Binary score for hallucination present in generation answer."""
    binary_score: str = Field(description="Answer is grounded in the facts, 'yes' or 'no'")

class GradeAnswer(BaseModel):
    """Binary score to assess whether the answer addresses the question."""
    binary_score: str = Field(description="Answer addresses the question, 'yes' or 'no'")

class RAGAlgorithms:
    def __init__(self, config: RetrieverConfig, llm: LLMs, wrap: RetrieverWrap, database: RAGDatabase, embeddings):
        self.config = config
        self.llm = llm
        self.wrap = wrap
        self.database = database
        self.embeddings = embeddings
        self._init_retrieval_grader()
        self._init_hallucination_grader()
        self._init_answer_grader()
        self._init_question_rewriter()
        self.init_log()

    def init_log(self):
        self._log = RAGItem()

    def _create_vector(self, collection: str=None):
        if not collection:
            raise ValueError("Please specify a collection")
        self.wrap.vector_store = self.database.get_db().create_vector(collection=collection, embeddings=self.embeddings)

    def _create_retriever(self):
        if self.config.feature_config.search_params:
            self.wrap.retriever = self.wrap.vector_store.as_retriever(search_type=self.config.rag_config.retriever_search, 
                                                           search_kwargs=self.config.rag_config.retriever_params)
        else:
            self.wrap.retriever = self.wrap.vector_store.as_retriever(search_type=self.config.rag_config.retriever_search) 

    def _create_template(self, template_str: str=None):
        if not template_str:
            raise ValueError("Please specify a prompt template")
        self.wrap.prompt = template_str
        self.wrap.template = ChatPromptTemplate.from_template(self.wrap.prompt)

    # Self_rag : init for grader of retrieved documents for relevent
    def _init_retrieval_grader(self):
        grade_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.prompts.rag_retrieval_grading),
                ("human", "Retrieved document: \n\n {document} \n\n User question: {question}"),
            ]
        )
        structured_llm_grader = self.llm().with_structured_output(GradeDocuments)
        self.retrieval_grader = grade_prompt | structured_llm_grader

        # Self_rag : init for grader generated output for answered question or not
    def _init_answer_grader(self):
        answer_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.prompts.rag_answer_grading),
                ("human", "User question: \n\n {question} \n\n LLM generation: {generation}"),
            ]
        )
        self.answer_grader = answer_prompt | self.llm().with_structured_output(GradeAnswer)

    # Self_rag : init for rewriting question
    def _init_question_rewriter(self):
        re_write_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.prompts.rag_question_rewriting),
                ("human", "Here is the initial question: \n\n {question} \n Formulate an improved question."),
            ]
        )
        self.question_rewriter = re_write_prompt | self.llm() | StrOutputParser()

        # Self_rag : init for grader generated output for hallucination
    def _init_hallucination_grader(self):
        hallucination_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.config.prompts.rag_hallucination_grading),
                ("human", "Set of facts: \n\n {documents} \n\n LLM generation: {generation}"),
            ]
        )
        self.hallucination_grader = hallucination_prompt | self.llm().with_structured_output(GradeHallucinations)

    # Self_rag/retrieval_grading : grader of retrieved documents for relevent
    def grade_retrieval(self, question, documents):
        metadata_callback = MetadataCaptureCallback()
        relevant_docs = []
        grading_result = self.retrieval_grader.invoke({"question": question, "document": documents}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
        if grading_result.binary_score.lower() == "yes":
            relevant_docs.append(documents)
        return relevant_docs, grading_result.binary_score.lower()
    
    def flush_log(self, final_answer, collection):
        self._log.final_answer = final_answer
        self._log.collection = collection
        log.update_raglog(self._log)
        self.init_log()

    # Hallucination_grading : grader generated output for hallucination
    #Changed
    def grade_hallucination(self, documents, generation):
        metadata_callback = MetadataCaptureCallback()
        #docs_content = "\n\n".join(doc.page_content for doc in documents)
        grading_result = self.hallucination_grader.invoke({"documents": documents, "generation": generation}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
        return grading_result.binary_score.lower() == "yes"

    # Answer_grading : init for grader generated output for answered question or not
    def grade_answer(self, question, generation):
        metadata_callback = MetadataCaptureCallback()
        grading_result = self.answer_grader.invoke({"question": question, "generation": generation}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
        return grading_result.binary_score.lower() == "yes"
    
    # Self_rag/question_rewriting : rewriting question
    def rewrite_question(self, question):
        metadata_callback = MetadataCaptureCallback()
        rewritten_question = self.question_rewriter.invoke({"question": question}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
        return rewritten_question
    
    # Multi_query : generate five different versions of the given user question
    def _multi_query(self):
        prompt_perspectives = ChatPromptTemplate.from_template(template=self.config.prompts.rag_multi)
        generate_queries = (
            prompt_perspectives 
            | self.llm()
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
        metadata_callback = MetadataCaptureCallback()
        prompt_decomposition = ChatPromptTemplate.from_template(template=self.config.prompts.rag_decompose)
        generate_queries_decomposition = (
            prompt_decomposition
            | self.llm()
            | StrOutputParser()
            | (lambda x: x.split("\n"))
        )
        sub_questions = generate_queries_decomposition.invoke({"question": question}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
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
        all_contexts = []

        for q in sub_questions:
            if self.wrap.retriever is None:
                self._create_retriever()
            metadata_callback = MetadataCaptureCallback()
            context_docs = self.wrap.retriever.get_relevant_documents(q)
            all_contexts.append(context_docs)
            rag_chain = (
                {"context": lambda x: context_docs,  
                "question": lambda x: x["question"],
                "q_a_pairs": lambda x: "\n---\n".join(q_a_pairs_list)}  
                | decomposition_prompt
                | self.llm()
                | StrOutputParser()
            )

            answer = rag_chain.invoke({"question": q, "q_a_pairs": "\n---\n".join(q_a_pairs_list)}, config={"callbacks": [metadata_callback]}) 
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
            q_a_pair = self.format_qa_pair(q, answer)
            q_a_pairs_list.append(q_a_pair) 

        return {"q_a_pairs": "\n---\n".join(q_a_pairs_list)} ,all_contexts

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
        metadata_callback = MetadataCaptureCallback()
        chain = (
            step_back_prompt
            | self.llm()
            | StrOutputParser()
        )
        step_back_query = chain.invoke({"question": question}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
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
        metadata_callback = MetadataCaptureCallback()
        chain = (
            {
                "normal_context": lambda x: normal_docs,
                "step_back_context": lambda x: step_back_docs,
                "question": lambda x: x["question"],
            }
            | response_prompt
            | self.llm()
            | StrOutputParser()
        )

        response = chain.invoke({"question": question}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
        return response,normal_docs,step_back_docs
    
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
        metadata_callback = MetadataCaptureCallback()
        if self.config.feature_config.question_rewriting:
            state["question"] = self.rewrite_question(state["question"])
        if self.config.feature_config.multi_query:
            questions = self._multi_query()
            retrieval_chain = (
                questions
                | self.wrap.vector_store.as_retriever().map()
                | self.get_unique_union
            )
            final_docs = retrieval_chain.invoke({"question": state["question"]}, config={"callbacks": [metadata_callback]})
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
        if self.config.feature_config.rag_fusion:
            questions = self._multi_query()
            queries = questions.invoke({"question": state["question"]}, config={"callbacks": [metadata_callback]})
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
            results = [self._search(query) for query in queries]
            unique_docs = self._reciprocal_rank_fusion(results)
            final_docs=unique_docs
        if self.config.feature_config.decomposition:
            sub_questions = self._decompose_question(state["question"])
            q_a_results,final_docs = self._answer_sub_questions(sub_questions)
            final_answer=q_a_results["q_a_pairs"]
        if self.config.feature_config.step_back:
            step_back_query = self._generate_step_back_query(state["question"])
            final_answer,_, final_docs = self._retrieve_step_back_context(state["question"], step_back_query)
        else:
            final_docs = self._search(state["question"])

        if not final_docs:
            console.overlay_print("---NO DOCUMENTS FOUND. RETURNING DEFAULT RESPONSE---", ConsoleType.SYSTEM)
            final_docs = [Document(page_content="No relevant documents found.")]

        if self.config.feature_config.retrieval_grading:
            final_docs, _ = self.grade_retrieval(state["question"], final_docs)
        if self.config.feature_config.decomposition:
            return {"context": final_docs, "answer": final_answer}
        if self.config.feature_config.step_back:
            return {"context": final_docs, "answer": final_answer}
        else:
            return {"context": final_docs}
    
    def generate(self, state: State):
        default_answer = "The response contains no verified factual content."
        default_suggestion = "Consider refining your query for more accurate results."
        docs_content = "\n\n".join(doc.page_content if hasattr(doc, "page_content") else str(doc) for doc in state["context"])

        messages = self.wrap.template.invoke({"question": state["question"], "context": docs_content})
        response = self.llm().invoke(messages)
        token_usages = response.usage_metadata
        self.llm.update_model_cost(token_usages)

        if self.config.feature_config.hallucination_grading:
            grounded_content = self.grade_hallucination(state["context"], response)

            if not grounded_content:
                return {
                    "answer": default_answer,
                    "suggestion": default_suggestion
                }
        if self.config.feature_config.answer_grading:
            is_relevant = self.grade_answer(state["question"], response)
            if not is_relevant:
                return {
                    "answer": default_answer,
                    "suggestion": default_suggestion
                }
        return {"answer": response.content}
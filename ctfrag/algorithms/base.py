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
        return relevant_docs

    # Hallucination_grading : grader generated output for hallucination
    def grade_hallucination(self, documents, generation):
        metadata_callback = MetadataCaptureCallback()
        docs_content = "\n\n".join(doc.page_content for doc in documents)
        grading_result = self.hallucination_grader.invoke({"documents": docs_content, "generation": generation}, config={"callbacks": [metadata_callback]})
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
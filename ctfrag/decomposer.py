from pydantic import BaseModel, Field
from ctfrag.console import console, ConsoleType
from ctfrag.config import RetrieverConfig
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from ctfrag.utils import MetadataCaptureCallback
import re

class Decomposition(BaseModel):
    task: str = Field(description="Task description extracted from the context.")
    query: str = Field(description="Query to be used for retrieving relevant information.")
    keywords: str = Field(description="Keywords extracted from the task description. For example, 'how to solve a reverse challenge' goes to 'solve, reverse, challenge'.")

class ContextDecomposer:
    def __init__(self, llm, config: RetrieverConfig=None):
        self.llm = llm
        self.config = config
        self.parser = PydanticOutputParser(pydantic_object=Decomposition)
        self.prompt = PromptTemplate(
            template=self.config.prompts.decomposer_composition,
            input_variables=["context"],
            partial_variables={
                "format_instructions": self.parser.get_format_instructions(),
            }
        )   
        self.chain = LLMChain(
            llm=self.llm(), 
            prompt=self.prompt,
            verbose=False
        )
    
    def decompose_task(self, context: str) -> Decomposition:
        try:
            metadata_callback = MetadataCaptureCallback()
            output = self.chain.run(context=context, callbacks=[metadata_callback])
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
            json_match = re.search(r'```(?:json)?\s*({.*?})\s*```', output, re.DOTALL)
            if json_match:
                output = json_match.group(1)
            decomposition = self.parser.parse(output)
            if decomposition.task == context or not decomposition.task.strip():
                raise ValueError("Task same as context")
            return decomposition
        except Exception as e:          
            return Decomposition(
                task=self.config.prompts.decomposer_defaulttask,
                query="",
                keywords=""
            )
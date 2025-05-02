from pydantic import BaseModel, Field
from ctfrag.console import console, ConsoleType, DecompositionItem, log
from ctfrag.config import RetrieverConfig
from langchain.chains import LLMChain
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from ctfrag.utils import MetadataCaptureCallback
import re
import json
from ctfrag.backends import LLMs

class Decomposition(BaseModel):
    task: str = Field(description="Task description extracted from the context.")
    query: str = Field(description="Query to be used for retrieving relevant information.")
    keywords: str = Field(description="Keywords extracted from the task description. For example, 'how to solve a reverse challenge' goes to 'solve, reverse, challenge'.")

class ContextDecomposer:
    def __init__(self, llm: LLMs, config: RetrieverConfig=None):
        self.llm = llm
        self.config = config
        self.index = 0
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
        self.init_log()

    def init_log(self):
        self._log = DecompositionItem()

    def flush_log(self):
        log.update_decompositionlog(self._log)
        self.init_log()
    
    def decompose_task(self, context: str) -> Decomposition:
        self._log.index = self.index
        self.index += 1
        try:
            metadata_callback = MetadataCaptureCallback()
            output = self.chain.run(context=context, callbacks=[metadata_callback])
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
            json_output = output.replace("\\'", "'")
            json_data = json.loads(json_output)
            # json_match = re.search(r'```(?:json)?\s*({.*?})\s*```', output, re.DOTALL)
            # if json_match:
            #     output = json_match.group(1)
            # import pdb; pdb.set_trace()
            # decomposition = self.parser.parse(json_data)
            # if decomposition.task == context or not decomposition.task.strip():
            #     raise ValueError("Task same as context")
            task = json_data["task"]
            query = json_data["query"]
            keywords = json_data["keywords"]
            console.overlay_print(f"Task: {task}\nQuery: {query}\nKeywords: {keywords}", ConsoleType.OUTPUT)
            self._log.context = context
            self._log.task = task
            self._log.query = query
            self._log.keywords = keywords
            self.flush_log()
            return json_data
        except Exception as e:     
            console.overlay_print(f"Decomposer failed: {e}", ConsoleType.ERROR)     
            return Decomposition(
                task=self.config.prompts.decomposer_defaulttask,
                query="",
                keywords=""
            )
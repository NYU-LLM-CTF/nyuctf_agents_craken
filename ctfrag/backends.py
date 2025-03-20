from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_together import TogetherEmbeddings
from langchain_openai import ChatOpenAI
from langchain_together import ChatTogether
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI

from pathlib import Path
import os

EMBEDDINGS = {
    "openai": OpenAIEmbeddings,
    "huggingface": HuggingFaceEmbeddings,
    "together": TogetherEmbeddings
}

'''
Example config
{
models: "gpt-4o"
temperature: 0
max_tokens=None
timeout=None
max_retries: 2
}
'''
class EmbeddingModel:
    def __init__(self, backend, model=None):
        self.model = model
        self.backend = backend
        if self.model:
            self.embeddings = EMBEDDINGS[backend](model=model)
        else:
            self.embeddings = EMBEDDINGS[backend]()

    def __call__(self):
        return self.embeddings
    
class LLMBackend:
    def __init__(self, model, config: dict):
        self.config = config
        self.model_name = model
        self.llm = None

    def __call__(self):
        return self.llm

class OpenAIBackend(LLMBackend):
    NAME = "openai"
    MODELS = {
        "gpt-4o-2024-11-20": {
            "max_context": 128000,
            "cost_per_input_token": 2.5e-06,
            "cost_per_output_token": 10e-06
        },
        "gpt-4o-2024-08-06": {
            "max_context": 128000,
            "cost_per_input_token": 2.5e-06,
            "cost_per_output_token": 10e-06
        },
        "gpt-4o-2024-05-13": {
            "max_context": 128000,
            "cost_per_input_token": 5e-06,
            "cost_per_output_token": 15e-06
        },
        "gpt-4o-mini-2024-07-18": {
            "max_context": 128000,
            "cost_per_input_token": 0.15e-06,
            "cost_per_output_token": 0.6e-06
        },
        "gpt-3.5-turbo-1106": {
            "max_context": 16385,
            "cost_per_input_token": 1e-06,
            "cost_per_output_token": 2e-06
        },
        "gpt-4-1106-preview": {
            "max_context": 128000,
            "cost_per_input_token": 10e-06,
            "cost_per_output_token": 30e-06
        },
        "gpt-4-0125-preview": {
            "max_context": 128000,
            "cost_per_input_token": 10e-06,
            "cost_per_output_token": 30e-06
        },
        "gpt-4-turbo-2024-04-09": {
            "max_context": 128000,
            "cost_per_input_token": 10e-06,
            "cost_per_output_token": 30e-06
        },
    }
    def __init__(self, model, config: dict):
        super().__init__(model, config)
        self.llm = ChatOpenAI(model=model, 
                              temperature=self.config["temperature"])

class TogetherBackend(LLMBackend):
    NAME = "together"
    MODELS = {
        "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo": {
            "max_context": 131072,
            "cost_per_input_token": 0.18e-06,
            "cost_per_output_token": 0.18e-06,
        },
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo": {
            "max_context": 131072,
            "cost_per_input_token": 0.88e-06,
            "cost_per_output_token": 0.88e-06,
        },
        "meta-llama/Llama-3.3-70B-Instruct-Turbo": {
            "max_context": 131072,
            "cost_per_input_token": 0.88e-06,
            "cost_per_output_token": 0.88e-06,
        },
        "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo": {
            "max_context": 130815,
            "cost_per_input_token": 3.5e-06,
            "cost_per_output_token": 3.5e-06,
        }
    }
    def __init__(self, model, config: dict):
        super().__init__(model, config)
        self.llm = ChatTogether(model=model, 
                                temperature=self.config["temperature"])

class AnthropicBackend(LLMBackend):
    NAME = "anthropic"
    MODELS = {
        "claude-3-5-sonnet-20241022": {
            "max_context": 200000,
            "cost_per_input_token": 3e-06,
            "cost_per_output_token": 15e-06
        },
        "claude-3-5-haiku-20241022": {
            "max_context": 200000,
            "cost_per_input_token": 0.8e-06,
            "cost_per_output_token": 4e-06
        }
    }
    def __init__(self, model, config: dict):
        super().__init__(model, config)
        self.llm = ChatAnthropic(model=model, 
                                temperature=self.config["temperature"])

class GeminiBackend(LLMBackend):
    NAME = "gemini"
    MODELS = {
        "gemini-2.0-flash-exp": {
            "max_context": 1000000,
            "cost_per_input_token": 0,
            "cost_per_output_token": 0
        },
        "gemini-1.5-flash": {
            "max_context": 1000000,
            "cost_per_input_token": 75e-08,
            "cost_per_output_token": 3e-07
        },
        "gemini-1.5-flash-8b": {
            "max_context": 1000000,
            "cost_per_input_token": 375e-09,
            "cost_per_output_token": 15e-08
        },
        "gemini-1.5-pro": {
            "max_context": 2000000,
            "cost_per_input_token": 125e-08,
            "cost_per_output_token": 5e-06
        },
        # Will be deprecated from 02/15/2025
        "gemini-1.0-pro": {
            "max_context": 32000,
            "cost_per_input_token": 5e-07,
            "cost_per_output_token": 15e-07
        }
    }
    def __init__(self, model, config: dict):
        super().__init__(model, config)
        self.llm = ChatGoogleGenerativeAI(model=model, 
                                temperature=self.config["temperature"])
        
BACKENDS = [OpenAIBackend, TogetherBackend, AnthropicBackend, GeminiBackend]
MODELS = {m: b for b in BACKENDS for m in b.MODELS}

class LLMs:
    def __init__(self, model, config: dict):
        self.model_name = model
        self.llm_backend: LLMBackend = MODELS[model](model, config)
        self.model_cost = 0.0
        self.search_cost = 0.0

    def update_search_cost(self, number_requests):
        self.search_cost += number_requests * 0.005

    def update_model_cost(self, meta_data):
        self.model_cost += self._calculate_cost(meta_data)

    def _calculate_cost(self, meta_data):
        in_price = self.llm_backend.MODELS[self.model_name]["cost_per_input_token"]
        out_price = self.llm_backend.MODELS[self.model_name]["cost_per_output_token"]
        return in_price * meta_data["input_tokens"] + out_price * meta_data["output_tokens"]

    # Get backend model such as ChatOpenAI()
    # LLMs -> Backend -> ChatAI
    def __call__(self):
        return self.llm_backend()

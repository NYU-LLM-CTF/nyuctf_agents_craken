import os
from pathlib import Path
from langchain.callbacks.base import BaseCallbackHandler
from langchain.callbacks import StdOutCallbackHandler
from langchain.callbacks.base import BaseCallbackHandler

API_ALIAS = {
    'OPENAI': 'OPENAI_API_KEY',
    'ANTHROPIC': 'ANTHROPIC_API_KEY',
    'GEMINI': 'GEMINI_API_KEY',
    'TOGETHER': 'TOGETHER_API_KEY',
    'GOOGLE_SEARCH': 'GOOGLE_API_KEY',
    'GOOGLE_CSE': 'GOOGLE_CSE_ID'
}

def load_api_keys(key_cfg=None, keys={}):
    if key_cfg:
        keys = Path(key_cfg).open("r")
        for line in keys:
            if line.startswith("#"):
                continue
            tag, k = line.strip().split("=")
            os.environ[API_ALIAS[tag]] = k
        keys.close()
    elif keys:
        for k, v in keys.items():
            os.environ[API_ALIAS[k]] = v

class OverlayCallbackHandler(BaseCallbackHandler):
    def __init__(self, overlay, color=2, truncate_prompt=True, truncate_length=300, 
                 show_llm_content=True, show_chain_content=True, show_tool_content=True,
                 show_intermediate_summary=True, intermediate_summary_length=50):
        self.overlay = overlay
        self.color = color
        self.current_row = 0
        self.max_rows = 0
        
        self.truncate_prompt = truncate_prompt
        self.truncate_length = truncate_length
        self.show_llm_content = show_llm_content
        self.show_chain_content = show_chain_content
        self.show_tool_content = show_tool_content
        
        self.show_intermediate_summary = show_intermediate_summary
        self.intermediate_summary_length = intermediate_summary_length
        
        self.current_chain_types = []
        
        self._init_overlay()
    
    def _init_overlay(self):
        self.current_row = 2
        self.max_rows = 20
    
    def _truncate(self, text):
        if len(text) > self.truncate_length:
            return text[:self.truncate_length] + "..."
        return text
    
    def _truncate_intermediate(self, text):
        if len(text) > self.intermediate_summary_length:
            return text[:self.intermediate_summary_length] + "..."
        return text
    
    def _is_intermediate_step(self, serialized=None, kwargs=None):
        if kwargs is None:
            kwargs = {}
            
        tags = kwargs.get("tags", [])
        
        if any(tag in ["map", "intermediate_steps"] for tag in tags):
            return True
            
        if serialized and isinstance(serialized, dict) and "MapReduceDocumentsChain" in str(serialized):
            return True
            
        if "MapReduceDocumentsChain" in self.current_chain_types:
            return True
            
        return False
    
    def on_llm_start(self, serialized, prompts, **kwargs):
        if not self.show_llm_content:
            return
            
        is_intermediate = self._is_intermediate_step(serialized, kwargs)
        
        if is_intermediate and self.show_intermediate_summary:
            chain_type = "Intermediate" if not self.current_chain_types else self.current_chain_types[-1]
            self.overlay.overlay_print(f"🔄 [Intermediate] {chain_type} LLM call...", color=6, row=self.current_row)
            self.current_row += 1
            
            if prompts:
                preview = self._truncate_intermediate(prompts[0])
                self.overlay.overlay_print(f"  Summary: {preview}", color=6, row=self.current_row)
                self.current_row += 1
        else:
            self.overlay.overlay_print(f"🔄 Starting LLM with {len(prompts)} prompts...", color=3, row=self.current_row)
            self.current_row += 1
            
            for i, prompt in enumerate(prompts):
                preview = self._truncate(prompt) if self.truncate_prompt else prompt
                self.overlay.overlay_print(f"  Prompt {i+1}: {preview}", color=4, row=self.current_row)
                self.current_row += 1
                
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def on_llm_end(self, response, **kwargs):
        if not self.show_llm_content:
            return
            
        is_intermediate = self._is_intermediate_step(None, kwargs)
        if is_intermediate and self.show_intermediate_summary:
            if hasattr(response, 'generations') and response.generations:
                for i, gen_list in enumerate(response.generations):
                    if gen_list:
                        text = gen_list[0].text if hasattr(gen_list[0], 'text') else str(gen_list[0])
                        preview = self._truncate_intermediate(text)
                        self.overlay.overlay_print(f"  [Intermediate Result]: {preview}", color=6, row=self.current_row)
                        self.current_row += 1
        else:
            if hasattr(response, 'generations'):
                self.overlay.overlay_print(f"✅ LLM finished. Generated {len(response.generations)} responses.", color=2, row=self.current_row)
                self.current_row += 1
                
                if response.generations:
                    for i, gen_list in enumerate(response.generations):
                        if gen_list:
                            text = gen_list[0].text if hasattr(gen_list[0], 'text') else str(gen_list[0])
                            preview = self._truncate(text) if self.truncate_prompt else text
                            self.overlay.overlay_print(f"  Response {i+1}: {preview}", color=5, row=self.current_row)
                            self.current_row += 1
            
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def on_llm_error(self, error, **kwargs):
        if not self.show_llm_content:
            return
            
        error_msg = self._truncate(str(error)) if self.truncate_prompt else str(error)
        self.overlay.overlay_print(f"❌ LLM Error: {error_msg}", color=1, row=self.current_row)
        self.current_row += 1
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def on_chain_start(self, serialized, inputs, **kwargs):
        if not self.show_chain_content:
            return
        
        if isinstance(serialized, dict):
            chain_type = serialized.get("name", "Chain")
        else:
            chain_type = "Chain"
            
        self.current_chain_types.append(chain_type)
        
        is_intermediate = self._is_intermediate_step(serialized, kwargs)
        if is_intermediate and self.show_intermediate_summary:
            self.overlay.overlay_print(f"🔄 [Intermediate] {chain_type}...", color=6, row=self.current_row)
            self.current_row += 1

            for key, value in inputs.items():
                if key == "input_documents" and isinstance(value, list):
                    self.overlay.overlay_print(f"  {key}: [{len(value)} documents]", color=6, row=self.current_row)
                elif isinstance(value, str):
                    preview = self._truncate_intermediate(value)
                    self.overlay.overlay_print(f"  {key}: {preview}", color=6, row=self.current_row)
                else:
                    self.overlay.overlay_print(f"  {key}: {type(value).__name__}", color=6, row=self.current_row)
                self.current_row += 1
                if self.current_row >= self.max_rows:
                    self._shift_content()
                    break
        else:
            self.overlay.overlay_print(f"🔄 Starting {chain_type}...", color=3, row=self.current_row)
            self.current_row += 1
            
            self.overlay.overlay_print(f"  Input keys: {list(inputs.keys())}", color=6, row=self.current_row)
            self.current_row += 1
            
            for key, value in inputs.items():
                if isinstance(value, str):
                    preview = self._truncate(value) if self.truncate_prompt else value
                    self.overlay.overlay_print(f"  {key}: {preview}", color=6, row=self.current_row)
                else:
                    self.overlay.overlay_print(f"  {key}: {type(value).__name__}", color=6, row=self.current_row)
                self.current_row += 1
                if self.current_row >= self.max_rows:
                    self._shift_content()
                    break
        
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def on_chain_end(self, outputs, **kwargs):
        if not self.show_chain_content:
            return
            
        is_intermediate = self._is_intermediate_step(None, kwargs)

        if self.current_chain_types:
            chain_type = self.current_chain_types.pop()
        else:
            chain_type = "Chain"
        if is_intermediate and self.show_intermediate_summary:
            self.overlay.overlay_print(f"✅ [Intermediate] {chain_type} finished", color=6, row=self.current_row)
            self.current_row += 1
            for key, value in outputs.items():
                if isinstance(value, str):
                    preview = self._truncate_intermediate(value)
                    self.overlay.overlay_print(f"  {key}: {preview}", color=6, row=self.current_row)
                elif key == "intermediate_steps" and isinstance(value, list):
                    self.overlay.overlay_print(f"  {key}: [{len(value)} steps]", color=6, row=self.current_row)
                else:
                    self.overlay.overlay_print(f"  {key}: {type(value).__name__}", color=6, row=self.current_row)
                self.current_row += 1
                if self.current_row >= self.max_rows:
                    self._shift_content()
                    break
        else:
            self.overlay.overlay_print(f"✅ Chain finished. Output keys: {list(outputs.keys())}", color=2, row=self.current_row)
            self.current_row += 1
            
            for key, value in outputs.items():
                if isinstance(value, str):
                    preview = self._truncate(value) if self.truncate_prompt else value
                    self.overlay.overlay_print(f"  {key}: {preview}", color=5, row=self.current_row)
                else:
                    self.overlay.overlay_print(f"  {key}: {type(value).__name__}", color=5, row=self.current_row)
                self.current_row += 1
                if self.current_row >= self.max_rows:
                    self._shift_content()
                    break
                    
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def on_chain_error(self, error, **kwargs):
        if not self.show_chain_content:
            return
            
        if self.current_chain_types:
            self.current_chain_types.pop()
            
        error_msg = self._truncate(str(error)) if self.truncate_prompt else str(error)
        self.overlay.overlay_print(f"❌ Chain Error: {error_msg}", color=1, row=self.current_row)
        self.current_row += 1
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def on_tool_start(self, serialized, input_str, **kwargs):
        if not self.show_tool_content:
            return
        
        if isinstance(serialized, dict):
            tool_name = serialized.get("name", "Tool")
        else:
            tool_name = "Tool"
            
        self.overlay.overlay_print(f"🔄 Starting tool {tool_name}...", color=5, row=self.current_row)
        self.current_row += 1
        
        preview = self._truncate(input_str) if self.truncate_prompt else input_str
        self.overlay.overlay_print(f"  Input: {preview}", color=6, row=self.current_row)
        self.current_row += 1
            
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def on_tool_end(self, output, **kwargs):
        if not self.show_tool_content:
            return
            
        preview = self._truncate(output) if self.truncate_prompt else output
        self.overlay.overlay_print(f"✅ Tool finished: {preview}", color=2, row=self.current_row)
        self.current_row += 1
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def on_tool_error(self, error, **kwargs):
        if not self.show_tool_content:
            return
            
        error_msg = self._truncate(str(error)) if self.truncate_prompt else str(error)
        self.overlay.overlay_print(f"❌ Tool Error: {error_msg}", color=1, row=self.current_row)
        self.current_row += 1
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def on_text(self, text, **kwargs):
        is_intermediate = self._is_intermediate_step(None, kwargs)
        
        if is_intermediate and self.show_intermediate_summary:
            preview = self._truncate_intermediate(text)
            self.overlay.overlay_print(f"💬 [Intermediate]: {preview}", color=6, row=self.current_row)
            self.current_row += 1
        else:
            preview = self._truncate(text) if self.truncate_prompt else text
            self.overlay.overlay_print(f"💬 {preview}", color=self.color, row=self.current_row)
            self.current_row += 1
            
        if self.current_row >= self.max_rows:
            self._shift_content()
    
    def _shift_content(self):
        self.current_row = max(self.current_row - 5, 2)
        self.overlay.overlay_print("... (some output condensed) ...", color=3, row=self.current_row - 1)

class MetadataCaptureCallback(BaseCallbackHandler):
    def __init__(self):
        self.usage_metadata = None
        
    def on_llm_end(self, response, **kwargs):
        self.usage_metadata = response.generations[0][0].message.usage_metadata

class DocumentDisplayCallback(BaseCallbackHandler):
    def __init__(self):
        self.documents = []
    
    def on_retriever_end(self, documents, **kwargs):
        self.documents = documents
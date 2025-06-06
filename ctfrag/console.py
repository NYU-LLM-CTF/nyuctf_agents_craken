import curses
import threading
import time
from contextlib import contextmanager
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Any
from langchain_core.documents import Document
from rich.status import Status
from ctfrag.config import RetrieverConfig

class LogNode(Enum):
    RETRIEVE = "RETRIEVE"
    GENERATE = "GENERATE"
    GRADE_HALLUCINATION = "GRADE_HALLUCINATION"
    GRADE_ANSWER = "GRADE_ANSWER"
    GRADE_DOCUMENTS = "GRADE_DOCUMENTS"
    REWRITE_QUERY  = "REWRITE_QUERY"
    DECIDE_GENERATION = "DECIDE_GENERATION"
    MAX_RETRY = "MAX_RETRY"
    RETRY = "RETRY"

class ConsoleType(Enum):
    SYSTEM = 5
    ERROR = 1
    INFO = 3
    OUTPUT = 2

@dataclass
class ConfigItem:
    model: str = ""
    hallucination_grading: bool = False
    answer_grading: bool = False
    retrieval_grading: bool = False
    search_params: bool = False
    rerank: bool = False
    compressor: bool = False
    multi_query: bool = False
    rag_fusion: bool = False
    decomposition: bool = False
    step_back: bool = False
    question_rewriting: bool = False
    graph: bool = True

@dataclass
class RAGItem:
    index: int = 0
    database: str = ""
    rag_algorithm: str = ""
    collection: str = ""
    trajectories: List[Any] = field(default_factory=list)
    source: List[List[str]] = field(default_factory=list)
    shortcut: List[List[str]] = field(default_factory=list)
    interm_generation: List[str] = field(default_factory=list)
    query: List[str] = field(default_factory=list)
    no_hallucinations: List[bool] = field(default_factory=list)
    document_quality: List[bool] = field(default_factory=list)
    answer_quality: List[bool] = field(default_factory=list)
    final_answer: str = ""


@dataclass
class WebSearchItem:
    index: int = 0
    source: List[str] = field(default_factory=list)
    context: List[str] = field(default_factory=list)
    answer: str = ""


@dataclass
class DecompositionItem:
    index: int = 0
    context: str = ""
    task: str = ""
    query: str = ""
    keywords: str = ""

"""
rag: [
    {
        "index": 1
        "trajectories": [],
        "source": [["", "", ""], [], []],
        "shortcut": [["", "", ""], [], []],
        "generation": ["", "", ""]
        "query": ["", "", ""],
        "hallucinations": [True, True, False],      
        "document_quality": [True, False, True],
        "answer_quality": [True, True, True],
        "final_answer": "",
    },
    {
        ...
    }
]
web_search: [
    {
        "index": 1
        "source": [[], [], []],
        "summarization": ["", "", "“],
        "answer": "",
    }
]
decomposition: [
    {
        "index": 1
        "context": "",
        "task": "",
        "query": "",
        "keywords": "",
    }
]
"""
class LogConsole:

    def __init__(self):
        self.search = []
        self.rag = []
        self.extract = []

    def parse_config(self, config: RetrieverConfig):
        return ConfigItem(
            model=config.agent_config.model_name,
            hallucination_grading=config.feature_config.hallucination_grading,
            answer_grading=config.feature_config.answer_grading,
            retrieval_grading=config.feature_config.retrieval_grading,
            rerank=config.feature_config.rerank,
            compressor=config.feature_config.compressor,
            multi_query=config.feature_config.multi_query,
            rag_fusion=config.feature_config.rag_fusion,
            decomposition=config.feature_config.decomposition,
            step_back=config.feature_config.step_back,
            question_rewriting=config.feature_config.question_rewriting
        )
    
    def update_raglog(self, logs:RAGItem):
        self.rag.append(logs)

    def update_searchlog(self, logs:WebSearchItem):
        self.search.append(logs)

    def update_decompositionlog(self, logs:DecompositionItem):
        self.extract.append(logs)

    def parse_documents(self, documents: List[Document], truncate=500):
        source = []
        context = []
        for document in documents:
            source.append(document.metadata.get("source", ""))
            if len(document.page_content) > truncate:
                context.append(document.page_content[:truncate] + "...[TRUNATED]")
            else:
                context.append(document.page_content)
        return source, context
    
    def get_retriever_logs(self, config):
        extract_dicts = [vars(item) for item in self.extract]
        rag_dicts = [vars(item) for item in self.rag]
        search_dicts = [vars(item) for item in self.search]
        config_dict = vars(self.parse_config(config=config))
        return {
            "config": config_dict,
            "decomposition": extract_dicts,
            "rag": rag_dicts,
            "web_search": search_dicts
        }


class OverlayConsole:
    def __init__(self, debug=False, quiet=False):
        self.overlay_active = False
        self.stdscr = None
        self.overlay_window = None
        self.overlay_lock = threading.Lock()
        self.stop_event = threading.Event()
        self.update_thread = None
        self.debug = debug
        self.quiet = quiet

        self.progress: Status = None
        
        # Dimensions and position
        self.overlay_start_row = 0
        self.overlay_end_row = 0
        self.overlay_width = 0
        self.overlay_height = 0
        
        # Content management
        self.content_lines = []
        self.max_lines = 0

    def set_progress(self, progress):
        self.progress = progress
        
    def overlay_start(self, start_row=None, end_row=None, width=None):
        if self.debug or self.quiet or self.overlay_active:
            return
        
        if self.progress:
            self.progress.stop()
            
        def init_curses():
            self.stdscr = curses.initscr()
            curses.start_color()
            curses.use_default_colors()
            curses.curs_set(0)
            curses.noecho()
            curses.cbreak()
            self.stdscr.keypad(True)

            for i in range(1, 8):
                curses.init_pair(i, i, -1)

            height, width_total = self.stdscr.getmaxyx()
            
            self.overlay_width = width or int(width_total * 0.95)
            self.overlay_start_row = start_row or int(height * 0.005)
            self.overlay_end_row = end_row or int(height * 0.95)
            self.overlay_height = self.overlay_end_row - self.overlay_start_row
            self.max_lines = self.overlay_height - 2
            
            start_col = (width_total - self.overlay_width) // 2
            self.overlay_window = curses.newwin(
                self.overlay_height, 
                self.overlay_width, 
                self.overlay_start_row, 
                start_col
            )
            self.overlay_window.box()
            self.overlay_window.refresh()
            
            self.content_lines = []

            self.stop_event.clear()
            self.update_thread = threading.Thread(target=self._update_overlay)
            self.update_thread.daemon = True
            self.update_thread.start()
            
            self.overlay_active = True
            
        try:
            init_curses()
        except Exception as e:
            self.overlay_end()
            raise Exception(f"Failed to initialize overlay: {e}")
    
    def overlay_end(self):
        if not self.overlay_active or self.debug or self.quiet:
            return

        if self.progress:
            self.progress.start()
        self.stop_event.set()
        if self.update_thread:
            self.update_thread.join(timeout=1.0)
        
        if self.stdscr:
            self.stdscr.keypad(False)
            curses.echo()
            curses.nocbreak()
            curses.endwin()
        
        self.overlay_active = False
        self.overlay_window = None
        self.stdscr = None
    
    def overlay_print(self, text, color:ConsoleType=3, row=None, auto_wrap=True, bold=True):
        if self.quiet:
            return
        if self.debug:
            print(text)
            return
        if not self.overlay_active:
            return
        
        color = color.value

        if color  == ConsoleType.INFO.value or color == ConsoleType.OUTPUT.value:
            bold = False
            
        with self.overlay_lock:
            available_width = self.overlay_width - 4
            
            if auto_wrap and len(text) > available_width:
                wrapped_lines = []
                for i in range(0, len(text), available_width):
                    wrapped_lines.append(text[i:i+available_width])
            else:
                wrapped_lines = [text]
                
            if row is not None:
                if 0 <= row < self.max_lines:
                    while len(self.content_lines) <= row:
                        self.content_lines.append(("", 0, False))                    
                    self.content_lines[row] = (wrapped_lines[0], color, bold)
                    
                    for i, line in enumerate(wrapped_lines[1:], 1):
                        if row + i < self.max_lines:
                            while len(self.content_lines) <= row + i:
                                self.content_lines.append(("", 0, False))
                            self.content_lines[row + i] = (line, color, bold)
            else:
                for line in wrapped_lines:
                    self.content_lines.append((line, color, bold))                
                if len(self.content_lines) > self.max_lines:
                    self.content_lines = self.content_lines[-self.max_lines:]
    
    def overlay_clear(self):
        if not self.overlay_active:
            return
            
        with self.overlay_lock:
            self.content_lines = []
    
    def _update_overlay(self):
        while not self.stop_event.is_set():
            try:
                with self.overlay_lock:
                    if self.overlay_window:
                        for y in range(1, self.overlay_height - 1):
                            self.overlay_window.addstr(y, 1, " " * (self.overlay_width - 2))

                        for i, (text, color, bold) in enumerate(self.content_lines):
                            if i >= self.max_lines:
                                break

                            display_text = text[:self.overlay_width - 4]
                            try:
                                color_attr = curses.color_pair(color) if color else 0
                                if bold:
                                    color_attr |= curses.A_BOLD
                                self.overlay_window.addstr(i + 1, 2, display_text, color_attr)
                            except:
                                pass
                        self.overlay_window.border('|', '|', '-', '-', '+', '+', '+', '+')
                        # self.overlay_window.box()
                        self.overlay_window.refresh()
            except Exception:
                pass
                
            time.sleep(0.1)

    @contextmanager
    def overlay_session(self, start_row=None, end_row=None, width=None):
        try:
            self.overlay_start(start_row, end_row, width)
            yield self
        finally:
            self.overlay_end()

console = OverlayConsole(debug=False, quiet=False)
log = LogConsole()
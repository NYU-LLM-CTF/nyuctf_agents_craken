from typing import List, Dict, Any, Optional
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from ctfrag.config import RetrieverConfig
import json
from langchain_community.callbacks import get_openai_callback
import re
from ctfrag.console import console, ConsoleType


class QuestionExtractor:
    def __init__(self, llm, config: RetrieverConfig=None):
        self.llm = llm
        self.config = config
        self.format_cost = 0
        self.evaluate_cost = 0
        self._init_extractors()

    def get_format_cost(self):
        return self.format_cost
    
    def get_evaluate_cost(self):
        return self.evaluate_cost
    
    def get_total_cost(self):
        return self.format_cost + self.evaluate_cost
    
    def _init_extractors(self):
        self.context_to_tasks_prompt = ChatPromptTemplate.from_template(self.config.prompts.extract_context_to_task)        
        self.context_to_tasks_chain = (
            self.context_to_tasks_prompt
            | self.llm()
            | StrOutputParser()
            | (lambda x: self._parse_json_tasks_safely(x))
        )

        self.task_to_question_prompt = ChatPromptTemplate.from_template(self.config.prompts.extract_task_to_question)
        self.task_to_question_chain = (
            self.task_to_question_prompt
            | self.llm()
            | StrOutputParser()
        )
        
        self.question_evaluation_prompt = ChatPromptTemplate.from_template(self.config.prompts.extract_question_evaluation)
        self.question_evaluation_chain = (
            self.question_evaluation_prompt
            | self.llm()
            | StrOutputParser()
            | (lambda x: self._parse_json_safely_evaluation(x))
        )
        
        self.answer_evaluation_prompt = ChatPromptTemplate.from_template(self.config.prompts.extract_answer_evaluation)
        self.answer_evaluation_chain = (
            self.answer_evaluation_prompt
            | self.llm()
            | StrOutputParser()
            | (lambda x: self._parse_json_safely_answer_evaluation(x))
        )
    
    def _parse_json_tasks_safely(self, json_str: str) -> List[Dict[str, str]]:
        try:
            console.overlay_print(f"Parsing JSON: {json_str[:100]}...", ConsoleType.SYSTEM)
            result = json.loads(json_str)
            if isinstance(result, list):
                tasks = []
                for item in result:
                    if isinstance(item, dict) and "task" in item:
                        tasks.append({"task": item["task"]})
                    elif isinstance(item, dict) and "subtask" in item:
                        tasks.append({"task": item["subtask"]})
                    elif isinstance(item, str):
                        tasks.append({"task": item})
                    elif isinstance(item, dict):
                        if len(item) > 0:
                            first_key = next(iter(item))
                            tasks.append({"task": item[first_key]})
                return tasks
            else:
                return [{"task": str(result)}]
        except json.JSONDecodeError as e:
            console.overlay_print(f"JSON decode error: {e}", ConsoleType.SYSTEM)
            tasks = re.findall(r'"task":\s*"([^"]+)"', json_str)
            if tasks:
                return [{"task": task} for task in tasks]            
            subtasks = re.findall(r'"subtask":\s*"([^"]+)"', json_str)
            if subtasks:
                return [{"task": subtask} for subtask in subtasks]            
            return [{"task": json_str.strip()}]
    
    def _parse_json_safely_evaluation(self, json_str: str) -> Dict[str, Any]:
        try:
            result = json.loads(json_str)
            if isinstance(result, dict) and "is_suitable" in result:
                return result
            else:
                return {
                    "is_suitable": True,
                    "reason": "Failed to parse response properly, assuming suitable by default"
                }
        except json.JSONDecodeError:
            is_suitable_match = re.search(r'"is_suitable":\s*(true|false)', json_str, re.IGNORECASE)
            reason_match = re.search(r'"reason":\s*"([^"]+)"', json_str)
            
            is_suitable = True
            if is_suitable_match:
                is_suitable = is_suitable_match.group(1).lower() == "true"
                
            reason = "Could not parse response"
            if reason_match:
                reason = reason_match.group(1)
                
            return {
                "is_suitable": is_suitable,
                "reason": reason
            }
    
    def _parse_json_safely_answer_evaluation(self, json_str: str) -> Dict[str, Any]:
        try:
            result = json.loads(json_str)
            if isinstance(result, dict) and "is_relevant" in result:
                return result
            else:
                return {
                    "is_relevant": False,
                    "reason": "Failed to parse response properly, assuming not relevant by default for stricter evaluation"
                }
        except json.JSONDecodeError:
            is_relevant_match = re.search(r'"is_relevant":\s*(true|false)', json_str, re.IGNORECASE)
            reason_match = re.search(r'"reason":\s*"([^"]+)"', json_str)
            
            is_relevant = False
            if is_relevant_match:
                is_relevant = is_relevant_match.group(1).lower() == "true"
                
            reason = "Could not parse response"
            if reason_match:
                reason = reason_match.group(1)
                
            return {
                "is_relevant": is_relevant,
                "reason": reason
            }
    
    def process_context(self, context: str) -> List[Dict[str, Any]]:
        console.overlay_print("Processing context...", ConsoleType.SYSTEM)
        try:
            with get_openai_callback() as cb:
                tasks = self.context_to_tasks_chain.invoke({"context": context})
                self.format_cost += cb.total_cost
            console.overlay_print(f"Extracted {len(tasks)} tasks", ConsoleType.SYSTEM)
            
            results = []
            for i, task_info in enumerate(tasks):
                try:
                    task = task_info.get("task", f"Task {i+1}")
                    console.overlay_print(f"Processing task: {task[:50]}...", ConsoleType.SYSTEM)
                    
                    with get_openai_callback() as cb:
                        question = self.task_to_question_chain.invoke({
                            "task": task,
                            "context": context
                        }).strip()
                        self.format_cost += cb.total_cost
                    
                    if not question.endswith("?"):
                        question += "?"
                    
                    with get_openai_callback() as cb:
                        evaluation = self.question_evaluation_chain.invoke({
                            "task": task,
                            "question": question,
                            "context": context
                        })
                        self.format_cost += cb.total_cost
                    
                    if evaluation.get("is_suitable", True):
                        results.append({
                            "task": task,
                            "question": question,
                            "evaluation": evaluation.get("reason", "Question is suitable for the context")
                        })
                except Exception as e:
                    console.overlay_print(f"Error processing task {i+1}: {str(e)}", ConsoleType.ERROR)
                    task_desc = task_info.get("task", f"Task {i+1}")
                    results.append({
                        "task": task_desc,
                        "question": self.config.prompts.extract_w_task_q,
                        "evaluation": self.config.prompts.extract_w_task_e
                    })
            
            if not results:
                results.append({
                    "task": self.config.prompts.extract_wo_task_t,
                    "question": self.config.prompts.extract_wo_task_q,
                    "evaluation": self.config.prompts.extract_wo_task_e
                })
            
            return results
            
        except Exception as e:
            console.overlay_print(f"Error in process_context: {str(e)}", ConsoleType.ERROR)
            return [{
                "task": self.config.prompts.extract_wo_task_t,
                "question": self.config.prompts.extract_wo_task_q,
                "evaluation": self.config.prompts.extract_wo_task_e
            }]
    
    def evaluate_answer(self, task: str, question: str, answer: str) -> Dict[str, Any]:
        try:
            console.overlay_print(f"Evaluating answer for question: {question[:50]}...", ConsoleType.SYSTEM)
            with get_openai_callback() as cb:
                result = self.answer_evaluation_chain.invoke({
                    "task": task,
                    "question": question,
                    "answer": answer
                })
                self.evaluate_cost += cb.total_cost
            return result
        except Exception as e:
            console.overlay_print(f"Error in evaluate_answer: {str(e)}", ConsoleType.ERROR)
            return {
                "is_relevant": False,
                "reason": "Error in evaluation, assuming not relevant by default for stricter evaluation"
            }
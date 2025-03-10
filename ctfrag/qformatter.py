from typing import List, Dict, Any, Optional
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
import json
from langchain_community.callbacks import get_openai_callback
import re
from enum import Enum


class LogLevel(Enum):
    NONE = 0
    ERROR = 1
    INFO = 2
    DEBUG = 3


class QuestionExtractor:
    def __init__(self, llm, log_level: LogLevel = LogLevel.NONE):
        self.llm = llm
        self.log_level = log_level
        self.format_cost = 0
        self.evaluate_cost = 0
        self._init_extractors()

    def get_format_cost(self):
        return self.format_cost
    
    def get_evaluate_cost(self):
        return self.evaluate_cost
    
    def get_total_cost(self):
        return self.format_cost + self.evaluate_cost
        
    def _log(self, message: str, level: LogLevel = LogLevel.INFO) -> None:
        """Log messages based on the configured log level."""
        if level.value <= self.log_level.value:
            if level == LogLevel.ERROR:
                print(f"ERROR: {message}")
            elif level == LogLevel.INFO:
                print(f"INFO: {message}")
            elif level == LogLevel.DEBUG:
                print(f"DEBUG: {message}")
    
    def set_log_level(self, level: LogLevel) -> None:
        """Set the logging level."""
        self.log_level = level
        self._log(f"Log level set to {level.name}", LogLevel.INFO)
    
    def _init_extractors(self):
        # Step 1: Extract tasks from conversation context
        self.context_to_tasks_prompt = ChatPromptTemplate.from_template("""
            You are an expert at analyzing CTF (Capture The Flag) challenge solving contexts.
            Given the following conversation context (including thoughts and action outputs),
            determine if this context needs to be broken down into 1-3 subtasks.
            
            If the context can only be decomposed into single or fewer tasks, don't provide unncessary tasks.
            Your decompositon should be concise, you should focus only on helping another agent solve CTF Challenges.                                                                 
            
            Conversation Context:
            ```
            {context}
            ```
            
            Output Format:
            Return a JSON array of subtasks. If decomposition is not needed, return a single task that summarizes the main objective.
            Format: [{{"task": "Description of subtask 1"}}, {{"task": "Description of subtask 2"}}]
            Only return the JSON array, nothing else.
            """)
        
        # The chain just receives the context
        self.context_to_tasks_chain = (
            self.context_to_tasks_prompt
            | self.llm
            | StrOutputParser()
            | (lambda x: self._parse_json_tasks_safely(x))
        )
        
        # Generate questions for each task
        self.task_to_question_prompt = ChatPromptTemplate.from_template("""
            You are an expert at identifying specific information needs for CTF (Capture The Flag) challenge tasks.
            Given the following task related to a CTF challenge, extract 1 key question that needs to be answered to complete this task.
            
            The question should be specific to the techniques, tools, or concepts mentioned in the task.
            
            Task:
            ```
            {task}
            ```
            
            Original Context (for reference):
            ```
            {context}
            ```
            
            Output Format:
            Return a single question that would help address this task.
            Make sure the question ends with a question mark.
            Only return the question text, nothing else.
            """)
        
        self.task_to_question_chain = (
            self.task_to_question_prompt
            | self.llm
            | StrOutputParser()
        )
        
        self.question_evaluation_prompt = ChatPromptTemplate.from_template("""
            Evaluate if the following question is suitable for the given CTF challenge context.
            
            Task: {task}
            Question: {question}
            Original Context:
            ```
            {context}
            ```
            
            Consider these criteria:
            1. Is the question relevant to the task and context?
            2. Is the question specific enough to yield useful information?
            3. Is the question focused on technical aspects needed to solve the challenge?
            4. Does the context indicate that this information is actually needed?
            
            Return a JSON object with the following structure:
            {{
              "is_suitable": true/false,
              "reason": "Brief explanation of your evaluation"
            }}
            
            Only return the JSON object, nothing else.
            """)
        
        self.question_evaluation_chain = (
            self.question_evaluation_prompt
            | self.llm
            | StrOutputParser()
            | (lambda x: self._parse_json_safely_evaluation(x))
        )
        
        # IMPROVED: Stricter answer evaluation prompt
        self.answer_evaluation_prompt = ChatPromptTemplate.from_template("""
            You are evaluating if an answer to a CTF challenge question contains actually useful information.
            Be STRICT in your evaluation - answers must provide SPECIFIC, TECHNICAL information to be considered relevant.
            
            Task: {task}
            Question: {question}
            Answer: {answer}
            
            First, check if any of these NON-INFORMATIVE patterns are present:
            1. "I don't know" or "I'm not sure" or similar disclaimers
            2. Vague, general statements that don't address the specific technical question
            3. Responses that only restate the question without adding technical details
            4. Generic explanations that could apply to any CTF challenge
            5. Empty promises of information without actually providing it
            
            An answer is only RELEVANT if it contains AT LEAST ONE of the following:
            1. Specific technical details directly related to the question (not just general concepts)
            2. Named tools, commands, or techniques that could be applied to the task
            3. Concrete exploitation methods or vulnerability details
            4. Code snippets, payloads, or specific syntax that could be used
            5. Step-by-step instructions that are specific to the task
            
            Return a JSON object with the following structure:
            {{
              "is_relevant": false,  // Default to false unless proven otherwise
              "reason": "Detailed explanation of why the answer is or is not relevant"
            }}
            
            Only return the JSON object, nothing else.
            """)
        
        self.answer_evaluation_chain = (
            self.answer_evaluation_prompt
            | self.llm
            | StrOutputParser()
            | (lambda x: self._parse_json_safely_answer_evaluation(x))
        )
    
    def _parse_json_tasks_safely(self, json_str: str) -> List[Dict[str, str]]:
        """Parse tasks JSON result safely."""
        try:
            self._log(f"Parsing JSON: {json_str[:100]}...", LogLevel.DEBUG)  # Print first 100 chars for debugging
            result = json.loads(json_str)
            if isinstance(result, list):
                tasks = []
                for item in result:
                    if isinstance(item, dict) and "task" in item:
                        tasks.append({"task": item["task"]})
                    elif isinstance(item, dict) and "subtask" in item:
                        # Handle old format for compatibility
                        tasks.append({"task": item["subtask"]})
                    elif isinstance(item, str):
                        tasks.append({"task": item})
                    elif isinstance(item, dict):
                        # Take the first value if neither "task" nor "subtask" key
                        if len(item) > 0:
                            first_key = next(iter(item))
                            tasks.append({"task": item[first_key]})
                
                return tasks
            else:
                return [{"task": str(result)}]
        except json.JSONDecodeError as e:
            self._log(f"JSON decode error: {e}", LogLevel.ERROR)
            # Try to extract content using regex if JSON parsing fails
            tasks = re.findall(r'"task":\s*"([^"]+)"', json_str)
            if tasks:
                return [{"task": task} for task in tasks]
            
            # Also try looking for "subtask" for backward compatibility
            subtasks = re.findall(r'"subtask":\s*"([^"]+)"', json_str)
            if subtasks:
                return [{"task": subtask} for subtask in subtasks]
            
            # Just use the entire string as a single task
            return [{"task": json_str.strip()}]
    
    def _parse_json_safely_evaluation(self, json_str: str) -> Dict[str, Any]:
        """Parse question evaluation JSON result safely."""
        try:
            result = json.loads(json_str)
            if isinstance(result, dict) and "is_suitable" in result:
                return result
            else:
                # Create a default response if JSON structure is incorrect
                return {
                    "is_suitable": True,  # Default to True for inclusivity
                    "reason": "Failed to parse response properly, assuming suitable by default"
                }
        except json.JSONDecodeError:
            # Try to extract boolean value using regex if JSON parsing fails
            is_suitable_match = re.search(r'"is_suitable":\s*(true|false)', json_str, re.IGNORECASE)
            reason_match = re.search(r'"reason":\s*"([^"]+)"', json_str)
            
            is_suitable = True  # Default to True for inclusivity
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
        """Parse answer evaluation JSON result safely."""
        try:
            result = json.loads(json_str)
            if isinstance(result, dict) and "is_relevant" in result:
                return result
            else:
                # Default to False for stricter evaluation
                return {
                    "is_relevant": False,
                    "reason": "Failed to parse response properly, assuming not relevant by default for stricter evaluation"
                }
        except json.JSONDecodeError:
            # Try to extract boolean value using regex if JSON parsing fails
            is_relevant_match = re.search(r'"is_relevant":\s*(true|false)', json_str, re.IGNORECASE)
            reason_match = re.search(r'"reason":\s*"([^"]+)"', json_str)
            
            is_relevant = False  # Default to False for stricter evaluation
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
        """
        Main workflow function that processes a conversation context.
        """
        self._log("Processing context...", LogLevel.INFO)
        try:
            # Step 1: Extract tasks from context - only pass context
            with get_openai_callback() as cb:
                tasks = self.context_to_tasks_chain.invoke({"context": context})
                self.format_cost += cb.total_cost
            self._log(f"Extracted {len(tasks)} tasks", LogLevel.INFO)
            
            results = []
            for i, task_info in enumerate(tasks):
                try:
                    task = task_info.get("task", f"Task {i+1}")
                    self._log(f"Processing task: {task[:50]}...", LogLevel.INFO)
                    
                    # Step 2: Generate a question for this task
                    with get_openai_callback() as cb:
                        question = self.task_to_question_chain.invoke({
                            "task": task,
                            "context": context
                        }).strip()
                        self.format_cost += cb.total_cost
                    # Ensure question ends with a question mark
                    if not question.endswith("?"):
                        question += "?"
                    
                    # Step 3: Evaluate question suitability
                    with get_openai_callback() as cb:
                        evaluation = self.question_evaluation_chain.invoke({
                            "task": task,
                            "question": question,
                            "context": context
                        })
                        self.format_cost += cb.total_cost
                    
                    # Add to results if suitable (or by default)
                    if evaluation.get("is_suitable", True):
                        results.append({
                            "task": task,
                            "question": question,
                            "evaluation": evaluation.get("reason", "Question is suitable for the context")
                        })
                except Exception as e:
                    self._log(f"Error processing task {i+1}: {str(e)}", LogLevel.ERROR)
                    # Add a fallback question for this task
                    task_desc = task_info.get("task", f"Task {i+1}")
                    results.append({
                        "task": task_desc,
                        "question": f"What techniques are needed for this CTF task?",
                        "evaluation": "Fallback question due to processing error"
                    })
            
            if not results:
                # Fallback if no questions were generated
                results.append({
                    "task": "Understand the CTF challenge",
                    "question": "What is the main vulnerability or technique needed for this CTF challenge?",
                    "evaluation": "Fallback question when no tasks could be processed"
                })
            
            return results
            
        except Exception as e:
            self._log(f"Error in process_context: {str(e)}", LogLevel.ERROR)
            # Return a fallback result
            return [{
                "task": "Understand the CTF challenge",
                "question": "What is the main vulnerability or technique needed for this CTF challenge?",
                "evaluation": "Fallback due to error in processing"
            }]
    
    def evaluate_answer(self, task: str, question: str, answer: str) -> Dict[str, Any]:
        """
        Evaluate if an answer has any relevant information for the question.
        """
        try:
            self._log(f"Evaluating answer for question: {question[:50]}...", LogLevel.DEBUG)
            with get_openai_callback() as cb:
                result = self.answer_evaluation_chain.invoke({
                    "task": task,
                    "question": question,
                    "answer": answer
                })
                self.evaluate_cost += cb.total_cost
            return result
        except Exception as e:
            self._log(f"Error in evaluate_answer: {str(e)}", LogLevel.ERROR)
            # Return a fallback evaluation - default to False for stricter evaluation
            return {
                "is_relevant": False,
                "reason": "Error in evaluation, assuming not relevant by default for stricter evaluation"
            }
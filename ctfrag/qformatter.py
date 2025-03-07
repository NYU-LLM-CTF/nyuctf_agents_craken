from typing import List, Dict, Any
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
import json

class QuestionExtractor:
    def __init__(self, llm):
        self.llm = llm
        self._init_extractors()
        
    def _init_extractors(self):
        self.context_to_questions_prompt = ChatPromptTemplate.from_template("""
        You are an expert at identifying information needs in a conversation. 
        Given the following conversation context (including thoughts and action outputs),
        extract 1-3 key questions that need to be answered to make progress.
        
        Focus on:
        1. Explicit information gaps mentioned in the conversation
        2. Implicit knowledge needed based on the agent's thoughts
        3. Technical details that would help with the current action
        
        Conversation Context:
        ```
        {context}
        ```
        
        Output Format:
        Return a JSON array of questions, like: ["Question 1?", "Question 2?", "Question 3?"]
        Only return the JSON array, nothing else.
        """)
        self.context_to_questions_chain = (
            self.context_to_questions_prompt
            | self.llm
            | StrOutputParser()
            | (lambda x: self._parse_json_safely(x))
        )
        
        self.task_to_questions_prompt = ChatPromptTemplate.from_template("""
        You are an expert at breaking down tasks into specific information needs.
        Given the following task description, extract 1-3 key questions that need to be answered to complete the task.
        
        Task Description:
        ```
        {task}
        ```
        
        Output Format:
        Return a JSON array of questions, like: ["Question 1?", "Question 2?", "Question 3?"]
        Only return the JSON array, nothing else.
        """)

        self.task_to_questions_chain = (
            self.task_to_questions_prompt
            | self.llm
            | StrOutputParser()
            | (lambda x: self._parse_json_safely(x))
        )
        self.input_classifier_prompt = ChatPromptTemplate.from_template("""
        Determine if the following input is a detailed task description or a conversation context.
        Task descriptions are typically shorter and focused on a specific objective.
        Conversation contexts are typically longer and contain multiple turns of dialogue or thought processes.
        
        Input:
        ```
        {input_text}
        ```
        
        Return only one of these values: "task_description" or "conversation_context"
        """)
        self.input_classifier_chain = (
            self.input_classifier_prompt
            | self.llm
            | StrOutputParser()
        )
    
    def _parse_json_safely(self, json_str: str) -> List[str]:
        try:
            result = json.loads(json_str)
            if isinstance(result, list):
                return result[:3] if len(result) > 3 else result
            else:
                return [str(result)]
        except json.JSONDecodeError:
            import re
            questions = re.findall(r'"([^"]+\?)"', json_str)
            if questions:
                return questions[:3]
            else:
                return [json_str.strip()]
    
    def extract_questions(self, input_text: str) -> List[str]:
        input_type = self.input_classifier_chain.invoke({"input_text": input_text}).strip().lower()
        if input_type == "task_description":
            questions = self.task_to_questions_chain.invoke({"task": input_text})
        else:
            questions = self.context_to_questions_chain.invoke({"context": input_text})
        if not questions:
            return ["What is the main objective or information need in this context?"]
        questions = [q if q.endswith("?") else f"{q}?" for q in questions]
        
        return questions

    def process_text(self, input_text: str) -> Dict[str, Any]:
        input_type = self.input_classifier_chain.invoke({"input_text": input_text}).strip().lower()
        questions = self.extract_questions(input_text)
        
        return {
            "questions": questions,
            "input_type": input_type,
            "question_count": len(questions)
        }
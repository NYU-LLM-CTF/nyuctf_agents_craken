from langchain_google_community import GoogleSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.schema.output_parser import OutputParserException
from pathlib import Path
from langchain.chains.summarize import load_summarize_chain
from langchain.schema.document import Document
from langchain.text_splitter import CharacterTextSplitter
import urllib.parse
from langchain.chains import LLMChain
import re
import json
import requests
import traceback
from bs4 import BeautifulSoup
import os

SEARCH_TEMPLATE: str = """
    Your task is to extract key information from the user's input.
    Your output format must follow:
    Key information: The key information you extracted from the user's input for search engine searches
    Output in this format. Do not add any additional content, you must strictly follow the standard format
    For example:
    User input: What news is there in Chengdu these days?
    Key information: Chengdu, news
    
    User input: {query}
    """

with open(Path(__file__).resolve().parent.parent / "api_keys", "r") as f:
    for line in f:
        key, value = line.strip().split("=")
        os.environ[key] = value

class WebSearchResult:

    def __init__(self, content: str, websites: list) -> None:
        self.websites = websites
        self.content = content


class WebSearch:
    def __init__(self):
        self.google_search = GoogleSearchAPIWrapper()
        self.prompt = PromptTemplate(input_variables=["query"], template=SEARCH_TEMPLATE)
        self.llm_chain = None
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        self.GOOGLE_SEARCH_ID = os.getenv("GOOGLE_CSE_ID")
        self.base_url = "https://www.googleapis.com/customsearch/v1"
        self.system_params = f"key={self.GOOGLE_API_KEY}&cx={self.GOOGLE_SEARCH_ID}"
        self.is_parser_detail: bool = True
        self.child_link_count: int = 30
        self.llm = ChatOpenAI(model_name="gpt-4o-2024-11-20", temperature=0.7)

    @classmethod
    def splitText(cls, text: str, chunk_size: int = 200, overlap: int = 50):
        if not text:
            raise ImportError("No input text")
        text_spliter = CharacterTextSplitter(chunk_size=chunk_size,
                                                chunk_overlap=overlap)
        text_string = text_spliter.split_text(text)
        text_string = [re.sub(r'\\[ntr]', '', item) for item in text_string]
        return text_string

    def parser_output(self, output: str):
        if not output:
            raise ValueError("Unable to get the correct input information")
        lines = output.split('\n')
        keywords = lines[0].split(':')[1].strip()
        return keywords
    
    def _extract_links(self, html_content: str, display_link: str, query: str):
        links = []
        # Use Beautiful Soup to parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        # Find all <a> tags
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            text = a_tag.get_text(strip=True)
            # When it's a relative path and not an anchor, assemble the link
            if display_link not in link and "#" not in link:
                link = display_link + link
            if display_link in link and text:
                links.append({"link": link, "text": text})
        # 10. Filter the most relevant links based on which link texts are most closely related to the user's input topic
        _prompt = """Known information: '{context}'
        Based on the above information, please filter out which information is closely related to the user input: '{query}'
        Please strictly output in the following format————
        Links: [one or more pieces of links you consider most closely related to the user input, separated by commas] or []
        """
        context = ','.join(
            [item["text"] for item in links[:self.child_link_count]])

        prompt_template = PromptTemplate(input_variables=["context", "query"],
                                        template=_prompt)
        chain = LLMChain(llm=self.llm,
                        prompt=prompt_template,
                        llm_kwargs={
                            "temperature": 0.95,
                            "top_p": 0.7
                        })
        content = chain.predict(context=context, query=query)
        # matches = (re.search(r'\[([^\]]+)\]', content)).group(0)
        # import pdb; pdb.set_trace()
        # result = json.loads(matches)
        matching_result = []
        if isinstance(content, list):
            matching_result = [
                item["link"] for item in links if item["text"] in result
            ]
        return matching_result
    
    def _final_summary(self, context_list: list, query: str):
        base_content_info = "\n\n".join(
            [obj["detail"] for obj in context_list])
        _prompt = """Known information: '{content}'
        Please use '{query}' as the theme, comprehensively and thoroughly summarize the above known information, content unrelated to the theme can be ignored"""
        prompt_template = PromptTemplate(input_variables=["content", "query"],
                                            template=_prompt)
        chain = LLMChain(llm=self.llm,
                            prompt=prompt_template,
                            llm_kwargs={
                                "temperature": 0.95,
                                "top_p": 0.7
                            })
        content = chain.predict(content=base_content_info, query=query)
        return content
        
    def _is_could_as_input_response(self, web_content: str, query: str):
        # 8. Method definition for summarizing content
        def get_long_token_result(html_content: str):
            texts = self.splitText(html_content, 4000, 200)
            docs = [Document(page_content=text) for text in texts]
            prompt_temp = """Create a concise summary of the following text: {text}"""
            PROMPT = PromptTemplate(template=prompt_temp,
                                input_variables=["text"])
            self.llm.temperature = 0.8
            self.llm.top_p = 0.7
            chain = load_summarize_chain(self.llm,
                                        chain_type="map_reduce",
                                        return_intermediate_steps=True,
                                        map_prompt=PROMPT,
                                        combine_prompt=PROMPT,
                                        verbose=True)

            summ = chain({"input_documents": docs}, return_only_outputs=True)
            return summ["output_text"]

        
        _prompt = """Known information: '{content}'
        Please determine whether the above information can serve as response content for '{query}', thereby meeting the user's intent.
        If yes, please output 'yes' directly;
        If no, please output 'no' directly.
        And you need to follow the specified format for output, format———— "Conclusion: yes or no"
        """
        prompt_template = PromptTemplate(input_variables=["content", "query"],
                                        template=_prompt)
        # 8. Summarize content
        content = get_long_token_result(html_content=web_content)
        # 9. Determine if it can be used as a result
        chain = LLMChain(llm=self.llm,
                        prompt=prompt_template,
                        llm_kwargs={
                            "temperature": 0.95,
                            "top_p": 0.7
                        })
        result = self.parser_output(chain.predict(content=content,
                                                query=query))
        # import pdb; pdb.set_trace()
        return content, True if result != "no" else False


    # 5. Method definition for accessing the webpage corresponding to the record
    def _load_html_content(self,
                        url: str,
                        query: str,
                        display_link: str = None):
        try:
            # Get response
            header = {
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            }
            # 5. Access the webpage corresponding to this record
            res = requests.get(url=url, headers=header).text
            # import pdb; pdb.set_trace()
            # 6. Clean the webpage text content
            content = self._remove_html_and_js(res)
            # 9. Determine if it can be used as a result
            content, is_result = self._is_could_as_input_response(
                web_content=content, query=query)
            if is_result is False:
                # 7. Extract internal links from the webpage
                link_list = self._extract_links(html_content=res,
                                            display_link=display_link,
                                            query=query)
                link_count = len(link_list)
                i = 0
                # 11. Loop through internal links
                while i < link_count and i < self.child_link_count:
                    item_url = link_list[i]
                    i = i + 1
                    # Repeat steps 6, 8, 9 above
                    res = requests.get(url=item_url, headers=header).text
                    content = self._remove_html_and_js(res)
                    content, is_result = self._is_could_as_input_response(
                        web_content=content, query=query)
                    if is_result is True:
                        break
        except Exception as e:
            print(f"Error: {e}")
            print(f"Traceback: {traceback.format_exc()}")
            content = ""
            pass
        finally:
            return content


    # 6. Method definition for cleaning webpage text content
    @staticmethod
    def _remove_html_and_js(text):
        text = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '',
                    text)
        text = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '',
                    text)
        text = re.sub(r'<.*?>', '', text)
        text = text.replace("\r", "").replace("\n", "")
        text = re.sub(r'<[^>]+>', '', text)
        return text

    def get_llm_chain(self):
        if not self.llm_chain:
            self.llm_chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def search_web(self, query) -> str:
        # 1. Extract keywords
        if not query:
            raise ValueError("Unable to get the correct user information")
        self.get_llm_chain()
        # Identify keywords from user input, to be used for searching content on internet platforms
        keywords = self.parser_output(self.llm_chain.predict(query=query))
        # 2. Call search engine to perform search
        encoded_keywords = urllib.parse.quote(keywords)
        self.system_params = f"{self.system_params}&q={encoded_keywords}&lr=lang_en&sort=review-rating:d:s"
        search_result = json.loads(
            requests.get(url=f"{self.base_url}?{self.system_params}").text)
        content = []
        final_content = ""
        # 3. Loop through search results
        if search_result and "items" in search_result:
            if self.is_parser_detail is False:
                for item in search_result["items"][:2]:
                    content.append({
                        "title": item["title"],
                        "link": item["link"],
                        "snippet": item["snippet"]
                    })
            else:
                for item in search_result["items"][:2]:
                    url = item["link"]
                    # 5. Access the webpage corresponding to this record
                    detail = self._load_html_content(
                        url=url, query=query, display_link=item["displayLink"])
                    if not detail:
                        continue
                    # 12. Save content and original links
                    content.append({
                        "title": item["title"],
                        "link": item["link"],
                        "detail": detail,
                        "snippet": item["snippet"]
                    })
                # 13. Extract all content and summarize again
                final_content = self._final_summary(content, query)
        return WebSearchResult(content=final_content, websites=content)
        
        # self.tools = [Tool(
        #     name="google_search",
        #     description="Search Google for recent results.",
        #     func=self.google_search.run,
        # )]
        # self.llm = ChatOpenAI(model_name="gpt-4o-2024-11-20", temperature=0.7)
        # self.agent = create_react_agent(
        #     llm=self.llm,
        #     tools=self.tools,
        #     prompt=PromptTemplate.from_template(SEARCH_TEMPLATE)
        # )
        # self.agent_executor = AgentExecutor.from_agent_and_tools(
        #     agent=self.agent,
        #     tools=self.tools,
        #     verbose=True,
        #     memory=ConversationBufferMemory(memory_key="chat_history"),
        #     handle_parsing_errors=True,
        #     max_iterations=6,
        #     early_stopping_method="generate"
        # )
    
    # def ask_question(self, query, search_mode="auto"):
    #     try:
    #         original_input = query
    #         if search_mode == "keywords" or (search_mode == "auto" and '?' not in query and 
    #         not any(word in query.lower() for word in ['what', 'how', 'why', 'when', 'where', 'who', 'which'])):
    #             search_input = f"Action: google_search\nAction Input: {query}"
    #             query = f"Find the most relevant information about: {query}. Focus on gathering facts and providing a clear summary."
            
    #         enhanced_query = f"{query}\n\nRemember to follow the exact format: Thought, Action, Action Input, Observation, etc."
    #         response = self.agent_executor.invoke({"input": enhanced_query})
    #         return response.get("output", "Sorry, I couldn't generate a response.")
    #     except Exception as e:
    #         return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    engine = WebSearch()
    result = engine.search_web(r"Find the CTF writeups for CSAW'23 Baby's First")
    print(result.content)
    # print(result.websites)
from langchain_google_community import GoogleSearchAPIWrapper
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.schema.runnable import RunnableSequence
from langchain.callbacks import StdOutCallbackHandler
import urllib.parse
import re
import json
import requests
import traceback
from bs4 import BeautifulSoup
import os
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any

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

# Load environment variables from api_keys file
def load_api_keys():
    """Load API keys from config file"""
    try:
        with open(Path(__file__).resolve().parent.parent / "api_keys", "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                os.environ[key] = value
    except Exception as e:
        print(f"Error loading API keys: {e}")
        raise

load_api_keys()

class WebSearchResult:
    """Container for web search results"""
    def __init__(self, content: str, websites: list) -> None:
        self.websites = websites
        self.content = content


class WebSearch:
    """Improved web search implementation using LangChain"""
    
    def __init__(self, verbose: bool = False):
        # 添加verbose参数，控制是否显示推理过程
        self.verbose = verbose
        
        # 如果verbose为True，则使用StdOutCallbackHandler
        self.callbacks = [StdOutCallbackHandler()] if verbose else None
        
        # 在创建llm实例时添加callbacks参数
        self.llm = ChatOpenAI(
            model_name="gpt-4o-2024-11-20", 
            temperature=0.7,
            callbacks=self.callbacks
        )
        
        self.google_search = GoogleSearchAPIWrapper()
        self.prompt = PromptTemplate(input_variables=["query"], template=SEARCH_TEMPLATE)
        self.keyword_chain = self.prompt | self.llm
        
        # Google search API configuration
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        self.GOOGLE_SEARCH_ID = os.getenv("GOOGLE_CSE_ID")
        self.base_url = "https://www.googleapis.com/customsearch/v1"
        self.system_params = f"key={self.GOOGLE_API_KEY}&cx={self.GOOGLE_SEARCH_ID}"
        
        # Configuration parameters
        self.is_parser_detail: bool = True
        self.child_link_count: int = 30
        self.max_search_results: int = 2
        
        # Request headers
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

    @staticmethod
    def splitText(text: str, chunk_size: int = 200, overlap: int = 50) -> List[str]:
        """Split text into manageable chunks"""
        if not text:
            raise ValueError("No input text")
        
        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap
        )
        
        text_chunks = text_splitter.split_text(text)
        # Clean up escaped characters
        text_chunks = [re.sub(r'\\[ntr]', '', item) for item in text_chunks]
        return text_chunks

    def parser_output(self, output) -> str:
        """Extract keywords from LLM output"""
        if not output:
            raise ValueError("Unable to get the correct input information")
        
        # Convert AIMessage or other LangChain objects to string if needed
        if hasattr(output, 'content'):
            output_text = output.content
        elif isinstance(output, dict) and 'content' in output:
            output_text = output['content']
        else:
            output_text = str(output)
        
        try:
            # Find the line with "Key information:" and extract the keywords
            for line in output_text.split('\n'):
                if "Key information:" in line:
                    return line.split(':', 1)[1].strip()
            
            # If not found through the standard format, return what we have
            return output_text.strip()
        except Exception as e:
            print(f"Error parsing output: {e}")
            return output_text.strip()
    
    def _extract_links(self, html_content: str, display_link: str, query: str) -> List[str]:
        """Extract and filter relevant links from HTML content"""
        links = []
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find all <a> tags with href attributes
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            text = a_tag.get_text(strip=True)
            
            # Handle relative paths and ensure links are complete
            if link and text and (not link.startswith('http') and not link.startswith('#')):
                # Ensure display_link has protocol
                if not display_link.startswith(('http://', 'https://')):
                    display_link = f"https://{display_link}"
                
                # Complete the URL for relative links
                if link.startswith('/'):
                    link = f"{display_link}{link}"
                else:
                    link = f"{display_link}/{link}"
            
            # Only keep links with meaningful text that includes the display_link domain
            if text and (display_link in link or not link.startswith(('http://', 'https://'))):
                links.append({"link": link, "text": text})
        
        # Limit to manageable number
        links = links[:self.child_link_count]
        
        # Create context from link texts for filtering
        context = ', '.join([item["text"] for item in links if item["text"]])
        
        # Prepare prompt for filtering relevant links
        filter_prompt = PromptTemplate(
            input_variables=["context", "query"],
            template="""Known information: '{context}'
            Based on the above information, please filter out which information is closely related to the user input: '{query}'
            Please strictly output in the following format————
            Links: [one or more pieces of links you consider most closely related to the user input, separated by commas] or []
            """
        )
        
        # Create and invoke chain to filter links with callback if verbose
        filter_chain = filter_prompt | self.llm.bind(temperature=0.95, top_p=0.7)
        result = filter_chain.invoke({"context": context, "query": query})
        # Convert message object to string if needed
        if hasattr(result, 'content'):
            result = result.content
        
        # Extract links from the result
        matching_texts = []
        
        # Try to parse links from the LLM output
        try:
            # Look for text between square brackets
            match = re.search(r'\[(.*?)\]', result)
            if match:
                matched_content = match.group(1)
                if matched_content:
                    matching_texts = [text.strip() for text in matched_content.split(',')]
        except Exception as e:
            print(f"Error extracting links from LLM output: {e}")
        
        # Filter links based on matching texts
        filtered_links = [
            item["link"] for item in links 
            if any(text.lower() in item["text"].lower() for text in matching_texts)
        ]
        
        return filtered_links
    
    def _final_summary(self, context_list: list, query: str) -> str:
        """Create a final summary from collected content"""
        if not context_list:
            return "No relevant information found."
        
        # Combine all detailed content
        base_content_info = "\n\n".join([obj.get("detail", "") for obj in context_list if "detail" in obj])
        
        if not base_content_info.strip():
            return "No detailed content available for summarization."
        
        # Create summary prompt
        summary_prompt = PromptTemplate(
            input_variables=["content", "query"],
            template="""Known information: '{content}'
            Please use '{query}' as the theme, comprehensively and thoroughly summarize the above known information, content unrelated to the theme can be ignored"""
        )
        
        # Create and invoke summary chain with callback if verbose
        summary_chain = summary_prompt | self.llm.bind(temperature=0.95, top_p=0.7)
        result = summary_chain.invoke({"content": base_content_info, "query": query})
        # Convert message object to string if needed
        if hasattr(result, 'content'):
            content = result.content
        else:
            content = str(result)
        
        return content
        
    def _is_could_as_input_response(self, web_content: str, query: str) -> Tuple[str, bool]:
        """Determine if web content can serve as a response to the query"""
        # Skip empty content
        if not web_content or not web_content.strip():
            return "", False
            
        # Summarize the content if needed
        summary = self._summarize_long_content(web_content)
        
        # Create evaluation prompt
        evaluation_prompt = PromptTemplate(
            input_variables=["content", "query"],
            template="""Known information: '{content}'
            Please determine whether the above information can serve as response content for '{query}', thereby meeting the user's intent.
            If yes, please output 'yes' directly;
            If no, please output 'no' directly.
            And you need to follow the specified format for output, format———— "Conclusion: yes or no"
            """
        )
        
        # Create and invoke evaluation chain with callback if verbose
        evaluation_chain = evaluation_prompt | self.llm.bind(temperature=0.95, top_p=0.7)
        result = evaluation_chain.invoke({"content": summary, "query": query})
        # Convert message object to string if needed
        if hasattr(result, 'content'):
            result = result.content
        
        # Parse the result
        is_usable = 'yes' in result.lower() and 'no' not in result.lower()
        
        return summary, is_usable

    def _summarize_long_content(self, html_content: str) -> str:
        """Summarize long HTML content using map-reduce approach"""
        # Split text into chunks
        try:
            texts = self.splitText(html_content, 4000, 200)
            docs = [Document(page_content=text) for text in texts]
            
            # Create summarization prompt
            prompt_template = """Create a concise summary of the following text: {text}"""
            prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
            
            # Configure summarization chain with callback if verbose
            chain = load_summarize_chain(
                self.llm.bind(temperature=0.8, top_p=0.7),
                chain_type="map_reduce",
                return_intermediate_steps=True,
                map_prompt=prompt,
                combine_prompt=prompt,
                verbose=self.verbose
            )
            
            # Invoke the chain
            result = chain.invoke({"input_documents": docs})
            
            # Handle different response formats
            if isinstance(result, dict) and "output_text" in result:
                return result["output_text"]
            elif hasattr(result, 'content'):
                return result.content
            elif isinstance(result, str):
                return result
            else:
                return str(result)
        except Exception as e:
            print(f"Error summarizing content: {e}")
            # Return truncated content if summarization fails
            return html_content[:5000] + "..."

    def _load_html_content(self, url: str, query: str, display_link: str = None) -> str:
        """Load and process HTML content from URL"""
        content = ""
        
        try:
            # Fetch the webpage
            if self.verbose:
                print(f"Fetching URL: {url}")
                
            response = requests.get(url=url, headers=self.headers, timeout=10)
            if response.status_code != 200:
                print(f"Failed to fetch URL: {url}, status code: {response.status_code}")
                return content
                
            html_text = response.text
            
            # Clean the HTML content
            cleaned_content = self._remove_html_and_js(html_text)
            
            # Check if content is usable as a response
            content, is_usable = self._is_could_as_input_response(cleaned_content, query)
            
            # If not usable, try to follow relevant internal links
            if not is_usable and display_link:
                if self.verbose:
                    print(f"Main content not usable, extracting internal links from {display_link}")
                    
                # Extract internal links
                link_list = self._extract_links(html_text, display_link, query)
                
                # Try each link until finding usable content
                for i, item_url in enumerate(link_list[:self.child_link_count]):
                    try:
                        if self.verbose:
                            print(f"Trying sublink {i+1}/{len(link_list[:self.child_link_count])}: {item_url}")
                            
                        sub_response = requests.get(url=item_url, headers=self.headers, timeout=10)
                        if sub_response.status_code == 200:
                            sub_content = self._remove_html_and_js(sub_response.text)
                            sub_content, sub_is_usable = self._is_could_as_input_response(sub_content, query)
                            
                            if sub_is_usable:
                                if self.verbose:
                                    print(f"Found usable content in sublink: {item_url}")
                                content = sub_content
                                break
                    except Exception as sub_e:
                        print(f"Error fetching sublink {item_url}: {sub_e}")
                        continue
                        
        except Exception as e:
            print(f"Error loading HTML content from {url}: {e}")
            print(f"Traceback: {traceback.format_exc()}")
            
        return content

    @staticmethod
    def _remove_html_and_js(text: str) -> str:
        """Clean HTML content by removing scripts, styles, and tags"""
        if not text:
            return ""
            
        # Remove scripts
        text = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', text)
        # Remove styles
        text = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', text)
        # Remove HTML comments
        text = re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', ' ', text)
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

    def search_web(self, query: str) -> WebSearchResult:
        """Main method to search the web for a query"""
        if not query:
            raise ValueError("Unable to get the correct user information")
            
        try:
            if self.verbose:
                print(f"Starting web search for query: {query}")
                print("=" * 40)
                print("STEP 1: Extracting keywords from query")
                
            # Extract keywords from query
            result = self.keyword_chain.invoke({"query": query})
            keywords = self.parser_output(result)
            
            if self.verbose:
                print(f"Extracted keywords: {keywords}")
                print("=" * 40)
                print("STEP 2: Performing Google search")
                
            # Encode keywords for URL
            encoded_keywords = urllib.parse.quote(keywords)
            search_params = f"{self.system_params}&q={encoded_keywords}&lr=lang_en&sort=review-rating:d:s"
            
            # Perform search
            search_response = requests.get(url=f"{self.base_url}?{search_params}")
            search_result = json.loads(search_response.text)
            
            # Process search results
            content_items = []
            final_content = ""
            
            if search_result and "items" in search_result:
                if self.verbose:
                    print(f"Found {len(search_result['items'])} search results")
                    print(f"Processing top {self.max_search_results} results")
                    print("=" * 40)
                
                # Simple mode: just collect snippets
                if not self.is_parser_detail:
                    for item in search_result["items"][:self.max_search_results]:
                        content_items.append({
                            "title": item.get("title", ""),
                            "link": item.get("link", ""),
                            "snippet": item.get("snippet", "")
                        })
                        
                # Detailed mode: fetch and process page content
                else:
                    for i, item in enumerate(search_result["items"][:self.max_search_results]):
                        url = item.get("link", "")
                        if not url:
                            continue
                            
                        if self.verbose:
                            print(f"STEP 3.{i+1}: Processing search result: {item.get('title', '')}")
                            print(f"URL: {url}")
                            
                        # Load and process HTML content
                        detail = self._load_html_content(
                            url=url, 
                            query=query, 
                            display_link=item.get("displayLink", "")
                        )
                        
                        if not detail:
                            if self.verbose:
                                print(f"No usable content found for {url}")
                            continue
                            
                        # Store the details
                        content_items.append({
                            "title": item.get("title", ""),
                            "link": url,
                            "detail": detail,
                            "snippet": item.get("snippet", "")
                        })
                        
                        if self.verbose:
                            print(f"Successfully extracted content from {url}")
                            print("-" * 40)
                    
                    # Create final summary if we have content
                    if content_items:
                        if self.verbose:
                            print("=" * 40)
                            print("STEP 4: Creating final summary")
                            
                        final_content = self._final_summary(content_items, query)
                        
                        if self.verbose:
                            print("Summary generation complete")
                            print("=" * 40)
            else:
                if self.verbose:
                    print("No search results found")
            
            return WebSearchResult(content=final_content, websites=content_items)
            
        except Exception as e:
            print(f"Error in search_web: {e}")
            print(f"Traceback: {traceback.format_exc()}")
            return WebSearchResult(content="Error occurred during web search.", websites=[])


if __name__ == "__main__":
    engine = WebSearch(verbose=True)
    result = engine.search_web(r"Find the CTF writeups for CSAW'23 Baby's First")
    print(result.content)
    # print(result.websites)
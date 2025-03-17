from langchain.prompts import PromptTemplate
from langchain.schema.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.callbacks import StdOutCallbackHandler
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_community.callbacks import get_openai_callback
from readability import Document
import urllib.parse
import re
import json
import requests
import traceback
from bs4 import BeautifulSoup
import os
from pathlib import Path
from typing import List, Tuple
from newspaper import Article

class SearchCostTracker:
    """Track costs for API usage"""
    def __init__(self):
        # Default pricing (can be updated with actual rates)
        self.google_search_price = 0.005  # $0.005 per search query
        self.reset()
    
    def reset(self):
        """Reset all cost counters"""
        self.google_search_cost = 0
        self.duckduckgo_search_cost = 0
        self.llm_model = ""
        self.llm_cost = 0.0

    def add_search_cost(self):
        self.google_search_cost += self.google_search_price

    def add_cost(self, llm_cost):
        self.llm_cost += llm_cost
    
    def get_cost_summary(self):
        return {
            "google_search_cost": round(self.google_search_cost, 4),
            "duckduckgo_search_cost": 0,  # Free service
            "llm_model": self.llm_model,
            "llm_cost": round(self.llm_cost, 4),
            "total_cost": round(self.google_search_cost + self.llm_cost, 4)
        }

SEARCH_TEMPLATE: str = """
    Your task is to extract key information from the user's input.
    Your output format must follow:
    Key information: The key information you extracted from the user's input for search engine searches
    Output in this format. Do not add any additional content, you must strictly follow the standard format
    For example:
    User input: How to solve a reverse CTF Challenge?
    Key information: CTF, reverse
    
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
    """Improved web search implementation using LangChain with engine selection"""
    
    def __init__(self, llm, verbose: bool = False, search_engine: str = "hybrid"):
        self.verbose = verbose
        self.cost_tracker = SearchCostTracker()
        # Set the search engine option (google, duckduckgo, or hybrid)
        self.search_engine = search_engine.lower()
        if self.search_engine not in ["google", "duckduckgo", "hybrid"]:
            print(f"Invalid search engine option: {search_engine}. Defaulting to hybrid.")
            self.search_engine = "hybrid"
            
        if self.verbose:
            print(f"Using search engine: {self.search_engine}")
            
        self.callbacks = [StdOutCallbackHandler()] if verbose else None
        
        self.llm = llm
        
        # Initialize search providers based on selected option
        if self.search_engine in ["google", "hybrid"]:
            # Google search API configuration
            self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
            self.GOOGLE_SEARCH_ID = os.getenv("GOOGLE_CSE_ID")
            self.base_url = "https://www.googleapis.com/customsearch/v1"
            self.system_params = f"key={self.GOOGLE_API_KEY}&cx={self.GOOGLE_SEARCH_ID}"
            
        if self.search_engine in ["duckduckgo", "hybrid"]:
            self.duckduckgo_search = DuckDuckGoSearchResults(output_format="list")
            
        self.prompt = PromptTemplate(input_variables=["query"], template=SEARCH_TEMPLATE)
        self.keyword_chain = self.prompt | self.llm
        
        # Configuration parameters
        self.is_parser_detail: bool = True
        self.child_link_count: int = 30
        self.max_search_results: int = 5
        self.parser: bool = "newspaper"
        
        # Request headers
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

    def _run_duckduckgo_search(self, keywords: str) -> List[dict]:
        """Perform search using DuckDuckGo"""
        if self.verbose:
            print(f"Running DuckDuckGo search for: {keywords}")
            
        try:
            # Use LangChain's DuckDuckGo search tool
            with get_openai_callback() as cb:
                results = self.duckduckgo_search.invoke(keywords)
            
            # DuckDuckGo returns a list of dictionaries with title, link, and snippet
            if isinstance(results, list) and results and isinstance(results[0], dict):
                # Format is already correct, just ensure all required keys are present
                parsed_results = []
                
                for item in results[:self.max_search_results]:
                    if "link" in item:
                        parsed_results.append({
                            "title": item.get("title", "No title found"),
                            "link": item.get("link", ""),
                            "snippet": item.get("snippet", "No snippet available"),
                            "displayLink": item.get("link", "").split("//")[-1].split("/")[0]  # Extract domain
                        })
                
                return parsed_results
            else:
                # Fallback to string parsing if result format is different
                print("Unexpected DuckDuckGo search result format, attempting to parse as string")
                parsed_results = []
                
                if isinstance(results, str):
                    # Split the results by new lines
                    result_items = results.split("\n")
                    
                    for item in result_items[:self.max_search_results]:
                        # Try to extract title and URL
                        url_match = re.search(r'https?://[^\s]+', item)
                        if url_match:
                            url = url_match.group(0)
                            # Remove the URL from the item to get title and snippet
                            remaining_text = item.replace(url, "").strip()
                            
                            # Simple parsing: assume first line is title, rest is snippet
                            title_end = remaining_text.find("\n") if "\n" in remaining_text else len(remaining_text)
                            title = remaining_text[:title_end].strip()
                            snippet = remaining_text[title_end:].strip()
                            
                            parsed_results.append({
                                "title": title or "No title found",
                                "link": url,
                                "snippet": snippet or "No snippet available",
                                "displayLink": url.split("//")[-1].split("/")[0]  # Extract domain
                            })
                
                return parsed_results
        except Exception as e:
            print(f"Error in DuckDuckGo search: {e}")
            return []

    def _run_google_search(self, keywords: str) -> List[dict]:
        """Perform search using Google Custom Search API"""
        if self.verbose:
            print(f"Running Google search for: {keywords}")
            
        try:
            # Encode keywords for URL
            encoded_keywords = urllib.parse.quote(keywords)
            search_params = f"{self.system_params}&q={encoded_keywords}&lr=lang_en&sort=review-rating:d:s"
            
            # Perform search
            search_response = requests.get(url=f"{self.base_url}?{search_params}")
            search_result = json.loads(search_response.text)
            self.cost_tracker.add_search_cost()
            if search_result and "items" in search_result:
                return search_result["items"][:self.max_search_results]
            else:
                print("No Google search results found")
                return []
                
        except Exception as e:
            print(f"Error in Google search: {e}")
            return []

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
        with get_openai_callback() as cb:
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
        with get_openai_callback() as cb:
            result = summary_chain.invoke({"content": base_content_info, "query": query})
            self.cost_tracker.add_cost(cb.total_cost)
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
        with get_openai_callback() as cb:
            result = evaluation_chain.invoke({"content": summary, "query": query})
            self.cost_tracker.add_cost(cb.total_cost)
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
            
            # Create document objects correctly based on langchain.schema.document.Document
            from langchain.schema.document import Document as LangchainDocument
            docs = [LangchainDocument(page_content=text) for text in texts]
            
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
            with get_openai_callback() as cb:
                result = chain.invoke({"input_documents": docs})
                self.cost_tracker.add_cost(cb.total_cost)
            
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
                # print(f"Website: {url} cannot be accessed, Status code: {response.status_code}, Ignore")
                return f"Website: {url} cannot be accessed, Ignore"
                
            html_text = response.text
            if self.parser == "newspaper":
                article = Article(url)
                article.download()
                article.parse()
                article.nlp()
                cleaned_content = article.text + "\n\n" + article.summary
            elif self.parser == "readability":
                doc = Document(response.content)
                cleaned_content = doc.content() + "\n\n" + doc.summary()
            else:
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
                
                # Track unsuccessful sublinks
                unsuccessful_sublinks = []
                
                # Try each link until finding usable content
                for i, item_url in enumerate(link_list[:self.child_link_count]):
                    try:
                        if self.verbose:
                            print(f"Trying sublink {i+1}/{len(link_list[:self.child_link_count])}: {item_url}")
                            
                        sub_response = requests.get(url=item_url, headers=self.headers, timeout=10)
                        if sub_response.status_code == 200:
                            if self.parser == "newspaper":
                                article = Article(url)
                                article.download()
                                article.parse()
                                article.nlp()
                                sub_content = article.text + "\n\n" + article.summary
                            elif self.parser == "readability":
                                doc = Document(response.content)
                                sub_content = doc.content() + "\n\n" + doc.summary()
                            else:
                                sub_content = self._remove_html_and_js(sub_response.text)
                            sub_content, sub_is_usable = self._is_could_as_input_response(sub_content, query)
                            
                            if sub_is_usable:
                                if self.verbose:
                                    print(f"Found usable content in sublink: {item_url}")
                                content = sub_content
                                break
                        else:
                            error_msg = f"Website: {item_url} cannot be accessed, Status code: {sub_response.status_code}, Ignore"
                            unsuccessful_sublinks.append(error_msg)
                            if self.verbose:
                                print(error_msg)
                    except Exception as sub_e:
                        error_msg = f"Website: {item_url} cannot be accessed, Error: {str(sub_e)}, Ignore"
                        unsuccessful_sublinks.append(error_msg)
                        if self.verbose:
                            print(error_msg)
                        continue
                
                # If we didn't find usable content and there were unsuccessful sublinks,
                # include them in the content
                if not content and unsuccessful_sublinks:
                    content = "\n".join(unsuccessful_sublinks)
                    
        except Exception as e:
            error_msg = f"Website: {url} cannot be accessed, Error: {str(e)}, Ignore"
            print(error_msg)
            content = error_msg
            
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

    def _merge_search_results(self, google_results: List[dict], duckduckgo_results: List[dict]) -> List[dict]:
        """Merge results from both search engines, removing duplicates and alternating sources"""
        if self.verbose:
            print("Merging search results from Google and DuckDuckGo")
            
        # Create a set to track URLs we've already seen
        seen_urls = set()
        merged_results = []
        
        # Alternate between sources to create a balanced list
        max_items = min(self.max_search_results, max(len(google_results), len(duckduckgo_results)) * 2)
        
        for i in range(max_items):
            # Add Google result if available and not seen
            if i % 2 == 0 and i // 2 < len(google_results):
                item = google_results[i // 2]
                url = item.get("link", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    merged_results.append(item)
                    
            # Add DuckDuckGo result if available and not seen
            elif i // 2 < len(duckduckgo_results):
                item = duckduckgo_results[i // 2]
                url = item.get("link", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    merged_results.append(item)
                    
            # Stop if we've reached our target count
            if len(merged_results) >= self.max_search_results:
                break
                
        return merged_results[:self.max_search_results]

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
            with get_openai_callback() as cb:
                result = self.keyword_chain.invoke({"query": query})
                self.cost_tracker.add_cost(cb.total_cost)
            keywords = self.parser_output(result)
            
            if self.verbose:
                print(f"Extracted keywords: {keywords}")
                print("=" * 40)
                print(f"STEP 2: Performing {self.search_engine.upper()} search")
                
            # Get search results based on selected engine
            search_items = []
            
            if self.search_engine == "google":
                search_items = self._run_google_search(keywords)
            elif self.search_engine == "duckduckgo":
                search_items = self._run_duckduckgo_search(keywords)
            else:  # hybrid
                google_results = self._run_google_search(keywords) if hasattr(self, 'google_search') else []
                duckduckgo_results = self._run_duckduckgo_search(keywords) if hasattr(self, 'duckduckgo_search') else []
                search_items = self._merge_search_results(google_results, duckduckgo_results)
            
            # Process search results
            content_items = []
            final_content = ""
            inaccessible_websites = []
            
            if search_items:
                if self.verbose:
                    print(f"Found {len(search_items)} search results")
                    print(f"Processing results")
                    print("=" * 40)
                
                # Simple mode: just collect snippets
                if not self.is_parser_detail:
                    for item in search_items:
                        content_items.append({
                            "title": item.get("title", ""),
                            "link": item.get("link", ""),
                            "snippet": item.get("snippet", "")
                        })
                        
                # Detailed mode: fetch and process page content
                else:
                    for i, item in enumerate(search_items):
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
                        
                        # Check if the response indicates a failed website
                        if detail and detail.startswith("Website:") and "cannot be accessed" in detail:
                            inaccessible_websites.append(detail)
                            if self.verbose:
                                print(f"Skipping inaccessible website: {url}")
                            continue
                        
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
                    
                    # Add information about inaccessible websites to the final content
                    if inaccessible_websites:
                        inaccessible_info = "\n\n" + "\n".join(inaccessible_websites)
                        final_content = final_content + inaccessible_info if final_content else inaccessible_info
            else:
                if self.verbose:
                    print("No search results found")
            
            return WebSearchResult(content=final_content, websites=content_items)
            
        except Exception as e:
            print(f"Error in search_web: {e}")
            print(f"Traceback: {traceback.format_exc()}")
            return WebSearchResult(content="Error occurred during web search.", websites=[])

# if __name__ == "__main__":
#     engine = WebSearch(verbose=True, search_engine="hybrid")
#     result = engine.search_web(r"How to write a good scientific paper?")
#     print(result.content)
#     print(engine.cost_tracker.get_cost_summary())
    # print(result.websites)
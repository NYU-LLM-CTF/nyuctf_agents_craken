from langchain.prompts import PromptTemplate
from langchain.schema.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_community.tools import DuckDuckGoSearchResults
from readability import Document
from ctfrag.config import RetrieverConfig
from ctfrag.console import console, ConsoleType, log, WebSearchItem
import urllib.parse
import re
import json
import requests
import traceback
from bs4 import BeautifulSoup
import os
from typing import List, Tuple
from newspaper import Article
from ctfrag.utils import OverlayCallbackHandler
from langchain.schema.document import Document as LangchainDocument
from ctfrag.utils import MetadataCaptureCallback
from ctfrag.backends import LLMs

class WebSearchResult:
    def __init__(self, content: str, websites: list) -> None:
        self.websites = websites
        self.content = content

class WebSearch:
    def __init__(self, llm: LLMs, verbose: bool = False, search_engine: str = "hybrid", config:RetrieverConfig=None):
        self.verbose = verbose
        self.config = config
        self._log = self.init_log()
        self.handler = OverlayCallbackHandler(console)
        self.search_engine = search_engine.lower()
        if self.search_engine not in ["google", "duckduckgo", "hybrid"]:
            console.overlay_print(f"Invalid search engine option: {search_engine}. Defaulting to hybrid.", ConsoleType.ERROR)
            self.search_engine = "hybrid"
            
        self.llm = llm

        if self.search_engine in ["google", "hybrid"]:
            self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
            self.GOOGLE_SEARCH_ID = os.getenv("GOOGLE_CSE_ID")
            self.base_url = "https://www.googleapis.com/customsearch/v1"
            self.system_params = f"key={self.GOOGLE_API_KEY}&cx={self.GOOGLE_SEARCH_ID}"
            
        if self.search_engine in ["duckduckgo", "hybrid"]:
            self.duckduckgo_search = DuckDuckGoSearchResults(output_format="list")
        
        self.prompt = PromptTemplate(input_variables=["query"], template=self.config.prompts.search_main)
        self.keyword_chain = self.prompt | self.llm()
        self.is_parser_detail: bool = True
        self.child_link_count: int = 30
        self.max_search_results: int = 10
        self.parser: bool = "newspaper"
        self.init_log()
        
        # Request headers
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

    def init_log(self):
        self._log = WebSearchItem()

    def _run_duckduckgo_search(self, keywords: str) -> List[dict]:
        if self.verbose:
            console.overlay_print(f"Running DuckDuckGo search for: {keywords}", ConsoleType.SYSTEM)
            
        try:
            results = self.duckduckgo_search.invoke(keywords)
            if isinstance(results, list) and results and isinstance(results[0], dict):
                parsed_results = []
                
                for item in results[:self.max_search_results]:
                    if "link" in item:
                        parsed_results.append({
                            "title": item.get("title", "No title found"),
                            "link": item.get("link", ""),
                            "snippet": item.get("snippet", "No snippet available"),
                            "displayLink": item.get("link", "").split("//")[-1].split("/")[0]
                        })
                
                return parsed_results
            else:
                console.overlay_print("Unexpected DuckDuckGo search result format, attempting to parse as string", ConsoleType.SYSTEM)
                parsed_results = []
                
                if isinstance(results, str):
                    result_items = results.split("\n")
                    
                    for item in result_items[:self.max_search_results]:
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
            console.overlay_print(f"Error in DuckDuckGo search: {e}", ConsoleType.ERROR)
            return []

    def _run_google_search(self, keywords: str) -> List[dict]:
        if self.verbose:
            console.overlay_print(f"Running Google search for: {keywords}", ConsoleType.SYSTEM)
            
        try:
            encoded_keywords = urllib.parse.quote(keywords)
            search_params = f"{self.system_params}&q={encoded_keywords}&lr=lang_en&sort=review-rating:d:s"
            search_response = requests.get(url=f"{self.base_url}?{search_params}")
            search_result = json.loads(search_response.text)
            if search_result and "items" in search_result:
                return search_result["items"][:self.max_search_results]
            else:
                console.overlay_print("No Google search results found", ConsoleType.INFO)
                return []
                
        except Exception as e:
            console.overlay_print(f"Error in Google search: {e}", ConsoleType.ERROR)
            return []

    @staticmethod
    def splitText(text: str, chunk_size: int = 200, overlap: int = 50) -> List[str]:
        if not text:
            raise ValueError("No input text")
        
        text_splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap
        )
        
        text_chunks = text_splitter.split_text(text)
        text_chunks = [re.sub(r'\\[ntr]', '', item) for item in text_chunks]
        return text_chunks

    def parser_output(self, output) -> str:
        if not output:
            raise ValueError("Unable to get the correct input information")
        if hasattr(output, 'content'):
            output_text = output.content
        elif isinstance(output, dict) and 'content' in output:
            output_text = output['content']
        else:
            output_text = str(output)
        
        try:
            for line in output_text.split('\n'):
                if "Key information:" in line:
                    return line.split(':', 1)[1].strip()
            return output_text.strip()
        except Exception as e:
            console.overlay_print(f"Error parsing output: {e}", ConsoleType.ERROR)
            return output_text.strip()
    
    def _extract_links(self, html_content: str, display_link: str, query: str) -> List[str]:
        links = []
        soup = BeautifulSoup(html_content, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            text = a_tag.get_text(strip=True)
            if link and text and (not link.startswith('http') and not link.startswith('#')):
                if not display_link.startswith(('http://', 'https://')):
                    display_link = f"https://{display_link}"

                if link.startswith('/'):
                    link = f"{display_link}{link}"
                else:
                    link = f"{display_link}/{link}"

            if text and (display_link in link or not link.startswith(('http://', 'https://'))):
                links.append({"link": link, "text": text})

        links = links[:self.child_link_count]
        context = ', '.join([item["text"] for item in links if item["text"]])
        filter_prompt = PromptTemplate(
            input_variables=["context", "query"],
            template=self.config.prompts.search_filtering
        )
        metadata_callback = MetadataCaptureCallback()
        filter_chain = filter_prompt | self.llm().bind(temperature=0.95, top_p=0.7)
        result = filter_chain.invoke({"context": context, "query": query}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
        if hasattr(result, 'content'):
            result = result.content
        matching_texts = []
        try:
            match = re.search(r'\[(.*?)\]', result)
            if match:
                matched_content = match.group(1)
                if matched_content:
                    matching_texts = [text.strip() for text in matched_content.split(',')]
        except Exception as e:
            console.overlay_print(f"Error extracting links from LLM output: {e}", ConsoleType.ERROR)
        filtered_links = [
            item["link"] for item in links 
            if any(text.lower() in item["text"].lower() for text in matching_texts)
        ]
        
        return filtered_links
    
    def _final_summary(self, context_list: list, query: str) -> str:
        if not context_list:
            return "No relevant information found."
        base_content_info = "\n\n".join([obj.get("detail", "") for obj in context_list if "detail" in obj])
        
        if not base_content_info.strip():
            return "No detailed content available for summarization."
        summary_prompt = PromptTemplate(
            input_variables=["content", "query"],
            template=self.config.prompts.search_summary
        )
        metadata_callback = MetadataCaptureCallback()
        summary_chain = summary_prompt | self.llm().bind(temperature=0.95, top_p=0.7)
        result = summary_chain.invoke({"content": base_content_info, "query": query}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
        if hasattr(result, 'content'):
            content = result.content
        else:
            content = str(result)
        
        return content
        
    def _is_could_as_input_response(self, web_content: str, query: str) -> Tuple[str, bool]:
        if not web_content or not web_content.strip():
            return "", False
        summary = self._summarize_long_content(web_content)
        evaluation_prompt = PromptTemplate(
            input_variables=["content", "query"],
            template=self.config.prompts.search_evaluation
        )
        metadata_callback = MetadataCaptureCallback()
        evaluation_chain = evaluation_prompt | self.llm().bind(temperature=0.95, top_p=0.7)
        result = evaluation_chain.invoke({"content": summary, "query": query}, config={"callbacks": [metadata_callback]})
        token_usages = metadata_callback.usage_metadata
        self.llm.update_model_cost(token_usages)
        if hasattr(result, 'content'):
            result = result.content
        is_usable = 'yes' in result.lower() and 'no' not in result.lower()
        
        return summary, is_usable

    def _summarize_long_content(self, html_content: str) -> str:
        try:
            texts = self.splitText(html_content, 4000, 200)
            docs = [LangchainDocument(page_content=text) for text in texts]
            prompt = PromptTemplate(template=self.config.prompts.search_summary_long, input_variables=["text"])
            chain = load_summarize_chain(
                self.llm().bind(temperature=0.8, top_p=0.7),
                chain_type="map_reduce",
                return_intermediate_steps=False,
                map_prompt=prompt,
                combine_prompt=prompt,
                verbose=False,
                callbacks=[self.handler]
            )
            metadata_callback = MetadataCaptureCallback()
            result = chain.invoke({"input_documents": docs}, config={"callbacks": [metadata_callback]})
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
            if isinstance(result, dict) and "output_text" in result:
                return result["output_text"]
            elif hasattr(result, 'content'):
                return result.content
            elif isinstance(result, str):
                return result
            else:
                return str(result)
        except Exception as e:
            console.overlay_print(f"Error summarizing content: {e}", ConsoleType.ERROR)
            return html_content[:5000] + "..."

    def _load_html_content(self, url: str, query: str, display_link: str = None) -> str:
        content = ""
        
        try:
            if self.verbose:
                console.overlay_print(f"Fetching URL: {url}", ConsoleType.SYSTEM)
                
            response = requests.get(url=url, headers=self.headers, timeout=10)
            if response.status_code != 200:
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
                cleaned_content = self._remove_html_and_js(html_text)
            
            content, is_usable = self._is_could_as_input_response(cleaned_content, query)
            
            if not is_usable and display_link:
                if self.verbose:
                    console.overlay_print(f"Main content not usable, extracting internal links from {display_link}", ConsoleType.INFO)
                link_list = self._extract_links(html_text, display_link, query)                
                unsuccessful_sublinks = []                
                for i, item_url in enumerate(link_list[:self.child_link_count]):
                    try:
                        if self.verbose:
                            console.overlay_print(f"Trying sublink {i+1}/{len(link_list[:self.child_link_count])}: {item_url}", ConsoleType.SYSTEM)
                            
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
                                    console.overlay_print(f"Found usable content in sublink: {item_url}", ConsoleType.INFO)
                                content = sub_content
                                break
                        else:
                            error_msg = f"Website: {item_url} cannot be accessed, Status code: {sub_response.status_code}, Ignore"
                            unsuccessful_sublinks.append(error_msg)
                            if self.verbose:
                                console.overlay_print(error_msg, ConsoleType.ERROR)
                    except Exception as sub_e:
                        error_msg = f"Website: {item_url} cannot be accessed, Error: {str(sub_e)}, Ignore"
                        unsuccessful_sublinks.append(error_msg)
                        if self.verbose:
                            console.overlay_print(error_msg, ConsoleType.ERROR)
                        continue

                if not content and unsuccessful_sublinks:
                    content = "\n".join(unsuccessful_sublinks)
                    
        except Exception as e:
            error_msg = f"Website: {url} cannot be accessed, Error: {str(e)}, Ignore"
            console.overlay_print(error_msg, ConsoleType.ERROR)
            content = error_msg
            
        self._log.source.append(url)
        self._log.context.append(content)
        return content

    @staticmethod
    def _remove_html_and_js(text: str) -> str:
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
        if self.verbose:
            console.overlay_print("Merging search results from Google and DuckDuckGo", ConsoleType.SYSTEM)            
        seen_urls = set()
        merged_results = []        
        max_items = min(self.max_search_results, max(len(google_results), len(duckduckgo_results)) * 2)
        
        for i in range(max_items):
            if i % 2 == 0 and i // 2 < len(google_results):
                item = google_results[i // 2]
                url = item.get("link", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    merged_results.append(item)
                    
            elif i // 2 < len(duckduckgo_results):
                item = duckduckgo_results[i // 2]
                url = item.get("link", "")
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    merged_results.append(item)
                    
            if len(merged_results) >= self.max_search_results:
                break
                
        return merged_results[:self.max_search_results]

    def search_web(self, query: str, index=0) -> WebSearchResult:
        self._log.index = index
        if not query:
            raise ValueError("Unable to get the correct user information")
            
        try:
            if self.verbose:
                console.overlay_print(f"Using search engine: {self.search_engine}", ConsoleType.SYSTEM)
                console.overlay_print(f"Starting web search for query: {query}", ConsoleType.SYSTEM)
                console.overlay_print("=" * 40, ConsoleType.SYSTEM)
                console.overlay_print("STEP 1: Extracting keywords from query", ConsoleType.SYSTEM)
            metadata_callback = MetadataCaptureCallback()
            result = self.keyword_chain.invoke({"query": query}, config={"callbacks": [metadata_callback]})
            token_usages = metadata_callback.usage_metadata
            self.llm.update_model_cost(token_usages)
            keywords = self.parser_output(result)
            
            if self.verbose:
                console.overlay_print(f"Extracted keywords: {keywords}", ConsoleType.SYSTEM)
                console.overlay_print("=" * 40, ConsoleType.SYSTEM)
                console.overlay_print(f"STEP 2: Performing {self.search_engine.upper()} search", ConsoleType.SYSTEM)
                
            search_items = []
            
            if self.search_engine == "google":
                search_items = self._run_google_search(keywords)
                self.llm.update_search_cost(1)
            elif self.search_engine == "duckduckgo":
                search_items = self._run_duckduckgo_search(keywords)
            else:
                google_results = self._run_google_search(keywords) if hasattr(self, 'google_search') else []
                duckduckgo_results = self._run_duckduckgo_search(keywords) if hasattr(self, 'duckduckgo_search') else []
                search_items = self._merge_search_results(google_results, duckduckgo_results)
            
            content_items = []
            final_content = ""
            inaccessible_websites = []
            
            if search_items:
                if self.verbose:
                    console.overlay_print(f"Found {len(search_items)} search results", ConsoleType.INFO)
                    console.overlay_print(f"Processing results", ConsoleType.SYSTEM)
                    console.overlay_print("=" * 40, ConsoleType.SYSTEM)
                
                if not self.is_parser_detail:
                    for item in search_items:
                        content_items.append({
                            "title": item.get("title", ""),
                            "link": item.get("link", ""),
                            "snippet": item.get("snippet", "")
                        })
                        
                else:
                    for i, item in enumerate(search_items):
                        url = item.get("link", "")
                        if not url:
                            continue
                            
                        if self.verbose:
                            console.overlay_print(f"STEP 3.{i+1}: Processing search result: {item.get('title', '')}", ConsoleType.SYSTEM)
                            console.overlay_print(f"URL: {url}", ConsoleType.INFO)
                            
                        detail = self._load_html_content(
                            url=url, 
                            query=query, 
                            display_link=item.get("displayLink", "")
                        )
                        
                        if detail and detail.startswith("Website:") and "cannot be accessed" in detail:
                            inaccessible_websites.append(detail)
                            if self.verbose:
                                console.overlay_print(f"Skipping inaccessible website: {url}", ConsoleType.INFO)
                            continue
                        
                        if not detail:
                            if self.verbose:
                                console.overlay_print(f"No usable content found for {url}", ConsoleType.INFO)
                            continue
                            
                        content_items.append({
                            "title": item.get("title", ""),
                            "link": url,
                            "detail": detail,
                            "snippet": item.get("snippet", "")
                        })
                        
                        if self.verbose:
                            console.overlay_print(f"Successfully extracted content from {url}", ConsoleType.INFO)
                            console.overlay_print("-" * 40, ConsoleType.INFO)
                    
                    if content_items:
                        if self.verbose:
                            console.overlay_print("=" * 40, ConsoleType.SYSTEM)
                            console.overlay_print("STEP 4: Creating final summary", ConsoleType.SYSTEM)
                            
                        final_content = self._final_summary(content_items, query)
                        self._log.answer = final_content
                        
                        if self.verbose:
                            console.overlay_print("Summary generation complete", ConsoleType.SYSTEM)
                            console.overlay_print("=" * 40, ConsoleType.SYSTEM)
                    
                    if inaccessible_websites:
                        inaccessible_info = "\n\n" + "\n".join(inaccessible_websites)
                        final_content = final_content + inaccessible_info if final_content else inaccessible_info
            else:
                if self.verbose:
                    console.overlay_print("No search results found", ConsoleType.INFO)
            
            self.flush_log()
            # import pdb; pdb.set_trace()
            return WebSearchResult(content=final_content, websites=content_items)
            
        except Exception as e:
            console.overlay_print(f"Error in search_web: {e}", ConsoleType.ERROR)
            console.overlay_print(f"Traceback: {traceback.format_exc()}", ConsoleType.ERROR)
            return WebSearchResult(content="Error occurred during web search.", websites=[])
        
    def flush_log(self):
        log.update_searchlog(self._log)
        self.init_log()
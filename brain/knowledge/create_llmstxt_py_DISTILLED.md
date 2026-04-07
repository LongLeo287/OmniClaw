---
id: create-llmstxt-py
type: knowledge
owner: OA_Triage
---
# create-llmstxt-py
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Firecrawl LLMs.txt Generator

A Python script that generates `llms.txt` and `llms-full.txt` files for any website using Firecrawl and OpenAI APIs.

## What is llms.txt?

`llms.txt` is a standardized format for making website content more accessible to Large Language Models (LLMs). It provides:

- **llms.txt**: A concise index of all pages with titles and descriptions
- **llms-full.txt**: Complete content of all pages for comprehensive access

## Features

- 🗺️ **Website Mapping**: Automatically discovers all URLs on a website using Firecrawl's map endpoint
- 📄 **Content Scraping**: Extracts markdown content from each page
- 🤖 **AI Summaries**: Uses OpenAI's GPT-4o-mini to generate concise titles and descriptions
- ⚡ **Parallel Processing**: Processes multiple URLs concurrently for faster generation
- 🎯 **Configurable Limits**: Set maximum number of URLs to process
- 📁 **Flexible Output**: Choose to generate both files or just llms.txt

## Prerequisites

- Python 3.7+
- Firecrawl API key ([Get one here](https://firecrawl.dev))
- OpenAI API key ([Get one here](https://platform.openai.com))

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up API keys (choose one method):

   **Option A: Using .env file (recommended)**

   ```bash
   cp env.example .env
   # Edit .env and add your API keys
   ```

   **Option B: Using environment variables**

   ```bash
   export FIRECRAWL_API_KEY="your-firecrawl-api-key"
   export OPENAI_API_KEY="your-openai-api-key"
   ```

   **Option C: Using command line arguments**
   (See usage examples below)

## Usage

### Basic Usage

Generate llms.txt and llms-full.txt for a website:

```bash
python generate-llmstxt.py https://example.com
```

### With Options

```bash
# Limit to 50 URLs
python generate-llmstxt.py https://example.com --max-urls 50

# Save to specific directory
python generate-llmstxt.py https://example.com --output-dir ./output

# Only generate llms.txt (skip full text)
python generate-llmstxt.py https://example.com --no-full-text

# Enable verbose logging
python generate-llmstxt.py https://example.com --verbose

# Specify API keys via command line
python generate-llmstxt.py https://example.com \
  --firecrawl-api-key "fc-..." \
  --openai-api-key "sk-..."
```

### Command Line Options

- `url` (required): The website URL to process
- `--max-urls`: Maximum number of URLs to process (default: 20)
- `--output-dir`: Directory to save output files (default: current directory)
- `--firecrawl-api-key`: Firecrawl API key (defaults to .env file or FIRECRAWL_API_KEY env var)
- `--openai-api-key`: OpenAI API key (defaults to .env file or OPENAI_API_KEY env var)
- `--no-full-text`: Only generate llms.txt, skip llms-full.txt
- `--verbose`: Enable verbose logging for debugging

## Output Format

### llms.txt

```
# https://example.com llms.txt

- [Page Title](https://example.com/page1): Brief description of the page content here
- [Another Page](https://example.com/page2): Another concise description of page content
```

### llms-full.txt

```
# https://example.com llms-full.txt

<|firecrawl-page-1-lllmstxt|>
## Page Title
Full markdown content of the page...

<|firecrawl-page-2-lllmstxt|>
## Another Page
Full markdown content of another page...
```

## How It Works

1. **Website Mapping**: Uses Firecrawl's `/map` endpoint to discover all URLs on the website
2. **Batch Processing**: Processes URLs in batches of 10 for efficiency
3. **Content Extraction**: Scrapes each URL to extract markdown content
4. **AI Summarization**: For each page, GPT-4o-mini generates:
   - A 3-4 word title
   - A 9-10 word description
5. **File Generation**: Creates formatted llms.txt and llms-full.txt files

## Error Handling

- Failed URL scrapes are logged and skipped
- If no URLs are found, the script exits with an error
- API errors are logged with details for debugging
- Rate limiting is handled with delays between batches

## Performance Considerations

- Processing time depends on the number of URLs and response times
- Default batch size is 10 URLs processed concurrently
- Small delays between batches prevent rate limiting
- For large websites, consider using `--max-urls` to limit processing

## Examples

### Small Website

```bash
python generate-llmstxt.py https://small-blog.com --max-urls 20
```

### Large Website with Limited Scope

```bash
python generate-llmstxt.py https://docs.example.com --max-urls 100 --verbose
```

### Quick Index Only

```bash
python generate-llmstxt.py https://example.com --no-full-text --max-urls 50
```

## Configuration Priority

The script checks for API keys in this order:

1. Command line arguments (`--firecrawl-api-key`, `--openai-api-key`)
2. `.env` file in the current directory
3. Environment variables (`FIRECRAWL_API_KEY`, `OPENAI_API_KEY`)

## Troubleshooting

### No API Keys Found

Ensure you've either:

- Created a `.env` file with your API keys (copy from `env.example`)
- Set environment variables: `FIRECRAWL_API_KEY` and `OPENAI_API_KEY`
- Or pass them via command line arguments

### Rate Limiting

If you encounter rate limits:

- Reduce concurrent workers in the code
- Add longer delays between batches
- Process fewer URLs at once

### Memory Issues

For very large websites:

- Use `--max-urls` to limit the number of pages
- Process in smaller batches
- Use `--no-full-text` to skip full content generation

## License

MIT License - see LICENSE file for details

```

### File: requirements.txt
```txt
requests>=2.31.0
openai>=1.3.0
python-dotenv>=1.0.0 
```

### File: generate-llmstxt.py
```py
#!/usr/bin/env python3
"""
Generate llms.txt and llms-full.txt files for a website using Firecrawl and OpenAI.

This script:
1. Maps all URLs from a website using Firecrawl's /map endpoint
2. Scrapes each URL to get the content
3. Uses OpenAI to generate titles and descriptions
4. Creates llms.txt (list of pages with descriptions) and llms-full.txt (full content)
"""

import os
import sys
import json
import time
import argparse
import logging
import re
from typing import Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class FirecrawlLLMsTextGenerator:
    """Generate llms.txt files using Firecrawl and OpenAI."""
    
    def __init__(self, firecrawl_api_key: str, openai_api_key: str):
        """Initialize the generator with API keys."""
        self.firecrawl_api_key = firecrawl_api_key
        self.openai_client = OpenAI(api_key=openai_api_key)
        self.firecrawl_base_url = "https://api.firecrawl.dev/v1"
        self.headers = {
            "Authorization": f"Bearer {self.firecrawl_api_key}",
            "Content-Type": "application/json"
        }
    
    def map_website(self, url: str, limit: int = 100) -> List[str]:
        """Map a website to get all URLs."""
        logger.info(f"Mapping website: {url} (limit: {limit})")
        
        try:
            response = requests.post(
                f"{self.firecrawl_base_url}/map",
                headers=self.headers,
                json={
                    "url": url,
                    "limit": limit,
                    "includeSubdomains": False,
                    "ignoreSitemap": False
                }
            )
            response.raise_for_status()
            
            data = response.json()
            if data.get("success") and data.get("links"):
                urls = data["links"]
                logger.info(f"Found {len(urls)} URLs")
                return urls
            else:
                logger.error(f"Failed to map website: {data}")
                return []
                
        except Exception as e:
            logger.error(f"Error mapping website: {e}")
            return []
    
    def scrape_url(self, url: str) -> Optional[Dict]:
        """Scrape a single URL."""
        logger.debug(f"Scraping URL: {url}")
        
        try:
            response = requests.post(
                f"{self.firecrawl_base_url}/scrape",
                headers=self.headers,
                json={
                    "url": url,
                    "formats": ["markdown"],
                    "onlyMainContent": True,
                    "timeout": 30000
                }
            )
            response.raise_for_status()
            
            data = response.json()
            if data.get("success") and data.get("data"):
                return {
                    "url": url,
                    "markdown": data["data"].get("markdown", ""),
                    "metadata": data["data"].get("metadata", {})
                }
            else:
                logger.error(f"Failed to scrape {url}: {data}")
                return None
                
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            return None
    
    def generate_description(self, url: str, markdown: str) -> Tuple[str, str]:
        """Generate title and description using OpenAI."""
        logger.debug(f"Generating description for: {url}")
        
        prompt = f"""Generate a 9-10 word description and a 3-4 word title of the entire page based on ALL the content one will find on the page for this url: {url}. This will help in a user finding the page for its intended purpose.

Return the response in JSON format:
{{
    "title": "3-4 word title",
    "description": "9-10 word description"
}}"""
        
        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that generates concise titles and descriptions for web pages."
                    },
                    {
                        "role": "user",
                        "content": f"{prompt}\n\nPage content:\n{markdown[:4000]}"  # Limit content to avoid token limits
                    }
                ],
                response_format={"type": "json_object"},
                temperature=0.3,
                max_tokens=100
            )
            
            result = json.loads(response.choices[0].message.content)
            return result.get("title", "Page"), result.get("description", "No description available")
            
        except Exception as e:
            logger.error(f"Error generating description: {e}")
            return "Page", "No description available"
    
    def process_url(self, url: str, index: int) -> Optional[Dict]:
        """Process a single URL: scrape and generate description."""
        scraped_data = self.scrape_url(url)
        if not scraped_data or not scraped_data.get("markdown"):
            return None
        
        title, description = self.generate_description(
            url, 
            scraped_data["markdown"]
        )
        
        return {
            "url": url,
            "title": title,
            "description": description,
            "markdown": scraped_data["markdown"],
            "index": index
        }
    
    def remove_page_separators(self, text: str) -> str:
        """Remove page separators from text."""
        return re.sub(r'<\|firecrawl-page-\d+-lllmstxt\|>\n', '', text)
    
    def limit_pages(self, full_text: str, max_pages: int) -> str:
        """Limit the number of pages in full text."""
        pages = full_text.split('<|firecrawl-page-')
        if len(pages) <= 1:
            return full_text
        
        # First element is the header
        result = pages[0]
        
        # Add up to max_pages
        for i in range(1, min(len(pages), max_pages + 1)):
            result += '<|firecrawl-page-' + pages[i]
        
        return result
    
    def generate_llmstxt(self, url: str, max_urls: int = 100, show_full_text: bool = True) -> Dict[str, str]:
        """Generate llms.txt and llms-full.txt for a website."""
        logger.info(f"Generating llms.txt for {url}")
        
        # Step 1: Map the website
        urls = self.map_website(url, max_urls)
        if not urls:
            raise ValueError("No URLs found for the website")
        
        # Limit URLs to max_urls
        urls = urls[:max_urls]
        
        # Initialize output strings
        llmstxt = f"# {url} llms.txt\n\n"
        llms_fulltxt = f"# {url} llms-full.txt\n\n"
        
        # Process URLs in batches of 10
        batch_size = 10
        all_results = []
        
        for i in range(0, len(urls), batch_size):
            batch = urls[i:i + batch_size]
            logger.info(f"Processing batch {i//batch_size + 1}/{(len(urls) + batch_size - 1)//batch_size}")
            
            # Process batch concurrently
            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = {
                    executor.submit(self.process_url, url, i + j): (url, i + j)
                    for j, url in enumerate(batch)
                }
                
                for future in as_completed(futures):
                    try:
                        result = future.result()
                        if result:
                            all_results.append(result)
                    except Exception as e:
                        url, idx = futures[future]
                        logger.error(f"Failed to process {url}: {e}")
            
            # Add a small delay between batches to avoid rate limiting
            if i + batch_size < len(urls):
                time.sleep(1)
        
        # Sort results by index to maintain order
        all_results.sort(key=lambda x: x["index"])
        
        # Build output strings
        for i, result in enumerate(all_results, 1):
            llmstxt += f"- [{result['title']}]({result['url']}): {result['description']}\n"
            llms_fulltxt += f"<|firecrawl-page-{i}-lllmstxt|>\n## {result['title']}\n{result['markdown']}\n\n"
        
        # Optionally remove page separators for clean output
        clean_full_text = self.remove_page_separators(llms_fulltxt) if not show_full_text else llms_fulltxt
        
        return {
            "llmstxt": llmstxt,
            "llms_fulltxt": clean_full_text,
            "num_urls_processed": len(all_results),
            "num_urls_total": len(urls)
        }


def main():
    """Main function to run the script."""
    parser = argparse.ArgumentParser(
        description="Generate llms.txt and llms-full.txt files for a website using Firecrawl and OpenAI"
    )
    parser.add_argument("url", help="The website URL to process")
    parser.add_argument(
        "--max-urls", 
        type=int, 
        default=20, 
        help="Maximum number of URLs to process (default: 20)"
    )
    parser.add_argument(
        "--output-dir", 
        default=".", 
        help="Directory to save output files (default: current directory)"
    )
    parser.add_argument(
        "--firecrawl-api-key",
        default=os.getenv("FIRECRAWL_API_KEY"),
        help="Firecrawl API key (default: from FIRECRAWL_API_KEY env var)"
    )
    parser.add_argument(
        "--openai-api-key",
        default=os.getenv("OPENAI_API_KEY"),
        help="OpenAI API key (default: from OPENAI_API_KEY env var)"
    )
    parser.add_argument(
        "--no-full-text",
        action="store_true",
        help="Don't generate llms-full.txt file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    # Validate API keys
    if not args.firecrawl_api_key:
        logger.error("Firecrawl API key not provided. Set FIRECRAWL_API_KEY environment variable or use --firecrawl-api-key")
        sys.exit(1)
    
    if not args.openai_api_key:
        logger.error("OpenAI API key not provided. Set OPENAI_API_KEY environment variable or use --openai-api-key")
        sys.exit(1)
    
    # Create generator
    generator = FirecrawlLLMsTextGenerator(
        args.firecrawl_api_key,
        args.openai_api_key
    )
    
    try:
        # Generate llms.txt files
        result = generator.generate_llmstxt(
            args.url,
            args.max_urls,
            not args.no_full_text
        )
        
        # Create output directory if it doesn't exist
        os.makedirs(args.output_dir, exist_ok=True)
        
        # Extract domain from URL for filename
        from urllib.parse import urlparse
        domain = urlparse(args.url).netloc.replace("www.", "")
        
        # Save llms.txt
        llmstxt_path = os.path.join(args.output_dir, f"{domain}-llms.txt")
        with open(llmstxt_path, "w", encoding="utf-8") as f:
            f.write(result["llmstxt"])
        logger.info(f"Saved llms.txt to {llmstxt_path}")
        
        # Save llms-full.txt if requested
        if not args.no_full_text:
            llms_fulltxt_path = os.path.join(args.output_dir, f"{domain}-llms-full.txt")
            with open(llms_fulltxt_path, "w", encoding="utf-8") as f:
                f.write(result["llms_fulltxt"])
            logger.info(f"Saved llms-full.txt to {llms_fulltxt_path}")
        
        # Print summary
        print(f"\nSuccess! Processed {result['num_urls_processed']} out of {result['num_urls_total']} URLs")
        print(f"Files saved to {args.output_dir}/")
        
    except Exception as e:
        logger.error(f"Failed to generate llms.txt: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

```


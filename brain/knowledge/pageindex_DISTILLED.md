---
id: pageindex
type: knowledge
owner: OA_Triage
---
# pageindex
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
  
<a href="https://vectify.ai/pageindex" target="_blank">
  <img src="https://github.com/user-attachments/assets/46201e72-675b-43bc-bfbd-081cc6b65a1d" alt="PageIndex Banner" />
</a>

<br/>
<br/>

<p align="center">
  <a href="https://trendshift.io/repositories/14736" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14736" alt="VectifyAI%2FPageIndex | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

# PageIndex: Vectorless, Reasoning-based RAG

<p align="center"><b>Reasoning-based RAG&nbsp; ◦ &nbsp;No Vector DB&nbsp; ◦ &nbsp;No Chunking&nbsp; ◦ &nbsp;Human-like Retrieval</b></p>

<h4 align="center">
  <a href="https://vectify.ai">🌐 Homepage</a>&nbsp; • &nbsp;
  <a href="https://chat.pageindex.ai">🖥️ Chat Platform</a>&nbsp; • &nbsp;
  <a href="https://pageindex.ai/developer">🔌 MCP & API</a>&nbsp; • &nbsp;
  <a href="https://docs.pageindex.ai">📖 Docs</a>&nbsp; • &nbsp;
  <a href="https://discord.com/invite/VuXuf29EUj">💬 Discord</a>&nbsp; • &nbsp;
  <a href="https://ii2abc2jejf.typeform.com/to/tK3AXl8T">✉️ Contact</a>&nbsp;
</h4>
  
</div>


<details open>
<summary><h2>📢 Updates</h2></summary>

- 🔥 [**Agentic Vectorless RAG**](https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py) — A simple *agentic, vectorless RAG* [example](https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py) with self-hosted PageIndex, using OpenAI Agents SDK.
- [PageIndex Chat](https://chat.pageindex.ai) — Human-like document analysis agent [platform](https://chat.pageindex.ai) for professional long documents. Also available via [MCP](https://pageindex.ai/developer) or [API](https://pageindex.ai/developer).
- [PageIndex Framework](https://pageindex.ai/blog/pageindex-intro) — Deep dive into PageIndex: an *agentic, in-context tree index* that enables LLMs to perform *reasoning-based, human-like retrieval* over long documents.

 <!-- **🧪 Cookbooks:**
- [Vectorless RAG](https://docs.pageindex.ai/cookbook/vectorless-rag-pageindex): A minimal, hands-on example of reasoning-based RAG using PageIndex. No vectors, no chunking, and human-like retrieval.
- [Vision-based Vectorless RAG](https://docs.pageindex.ai/cookbook/vision-rag-pageindex): OCR-free, vision-only RAG with PageIndex's reasoning-native retrieval workflow that works directly over PDF page images. -->

</details>

---

# 📑 Introduction to PageIndex

Are you frustrated with vector database retrieval accuracy for long professional documents? Traditional vector-based RAG relies on semantic *similarity* rather than true *relevance*. But **similarity ≠ relevance** — what we truly need in retrieval is **relevance**, and that requires **reasoning**. When working with professional documents that demand domain expertise and multi-step reasoning, similarity search often falls short.

Inspired by AlphaGo, we propose **[PageIndex](https://vectify.ai/pageindex)** — a **vectorless**, **reasoning-based RAG** system that builds a **hierarchical tree index** from long documents and uses LLMs to **reason** *over that index* for **agentic, context-aware retrieval**.
It simulates how *human experts* navigate and extract knowledge from complex documents through *tree search*, enabling LLMs to *think* and *reason* their way to the most relevant document sections. PageIndex performs retrieval in two steps:

1. Generate a “Table-of-Contents” **tree structure index** of documents
2. Perform reasoning-based retrieval through **tree search**

<div align="center">
  <a href="https://pageindex.ai/blog/pageindex-intro" target="_blank" title="The PageIndex Framework">
    <img src="https://docs.pageindex.ai/images/cookbook/vectorless-rag.png" width="70%">
  </a>
</div>

### 🎯 Core Features

Compared to traditional vector-based RAG, **PageIndex** features:
- **No Vector DB**: Uses document structure and LLM reasoning for retrieval, instead of vector similarity search.
- **No Chunking**: Documents are organized into natural sections, not artificial chunks.
- **Human-like Retrieval**: Simulates how human experts navigate and extract knowledge from complex documents.
- **Better Explainability and Traceability**: Retrieval is based on reasoning — traceable and interpretable, with page and section references. No more opaque, approximate vector search (“vibe retrieval”).

PageIndex powers a reasoning-based RAG system that achieved **state-of-the-art** [98.7% accuracy](https://github.com/VectifyAI/Mafin2.5-FinanceBench) on FinanceBench, demonstrating superior performance over vector-based RAG solutions in professional document analysis. See our [blog post](https://vectify.ai/blog/Mafin2.5) for details.

### 📍 Explore PageIndex

To learn more, please see a detailed introduction to the [PageIndex framework](https://pageindex.ai/blog/pageindex-intro). Check out this GitHub repo for open-source code, and the [cookbooks](https://docs.pageindex.ai/cookbook), [tutorials](https://docs.pageindex.ai/tutorials), and [blog](https://pageindex.ai/blog) for additional usage guides and examples.

The PageIndex service is available as a ChatGPT-style [chat platform](https://chat.pageindex.ai), or can be integrated via [MCP](https://pageindex.ai/developer) or [API](https://pageindex.ai/developer).

### 🛠️ Deployment Options
- Self-host — run locally with this open-source repo.
- Cloud Service — try instantly with our [Chat Platform](https://chat.pageindex.ai/), or integrate via [MCP](https://pageindex.ai/developer) or [API](https://pageindex.ai/developer).
- _Enterprise_ — private or on-prem deployment. [Contact us](https://ii2abc2jejf.typeform.com/to/tK3AXl8T) or [book a demo](https://calendly.com/pageindex/meet) for more details.

### 🧪 Quick Hands-on

- 🔥 [**Agentic Vectorless RAG**](examples/agentic_vectorless_rag_demo.py) (**latest**) — a simple but complete **agentic vectorless RAG** [example](https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py) with *self-hosted* PageIndex, using OpenAI Agents SDK.
- Try the [Vectorless RAG](https://github.com/VectifyAI/PageIndex/blob/main/cookbook/pageindex_RAG_simple.ipynb) notebook — a *minimal*, hands-on example of reasoning-based RAG using PageIndex.
- Check out [Vision-based Vectorless RAG](https://github.com/VectifyAI/PageIndex/blob/main/cookbook/vision_RAG_pageindex.ipynb) — no OCR; a minimal, vision-based & reasoning-native RAG pipeline that works directly over page images.
  
<div align="center">
  <a href="https://github.com/VectifyAI/PageIndex/blob/main/examples/agentic_vectorless_rag_demo.py" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/View_on_GitHub-Agentic_Vectorless_RAG-blue?style=for-the-badge&logo=github" alt="View on GitHub: Agentic Vectorless RAG" />
  </a>
  <br/>
  <a href="https://colab.research.google.com/github/VectifyAI/PageIndex/blob/main/cookbook/pageindex_RAG_simple.ipynb" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/Open_In_Colab-Vectorless_RAG-orange?style=for-the-badge&logo=googlecolab" alt="Open in Colab: Vectorless RAG" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/VectifyAI/PageIndex/blob/main/cookbook/vision_RAG_pageindex.ipynb" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/Open_In_Colab-Vision_RAG-orange?style=for-the-badge&logo=googlecolab" alt="Open in Colab: Vision RAG" />
  </a>
</div>

---

# 🌲 PageIndex Tree Structure

PageIndex can transform lengthy PDF documents into a semantic **tree structure**, similar to a _"table of contents"_ but optimized for use with Large Language Models (LLMs). It's ideal for: financial reports, regulatory filings, academic textbooks, legal or technical manuals, and any document that exceeds LLM context limits.

Below is an example PageIndex tree structure. Also see more example [documents](https://github.com/VectifyAI/PageIndex/tree/main/examples/documents) and generated [tree structures](https://github.com/VectifyAI/PageIndex/tree/main/examples/documents/results).

```jsonc
...
{
  "title": "Financial Stability",
  "node_id": "0006",
  "start_index": 21,
  "end_index": 22,
  "summary": "The Federal Reserve ...",
  "nodes": [
    {
      "title": "Monitoring Financial Vulnerabilities",
      "node_id": "0007",
      "start_index": 22,
      "end_index": 28,
      "summary": "The Federal Reserve's monitoring ..."
    },
    {
      "title": "Domestic and International Cooperation and Coordination",
      "node_id": "0008",
      "start_index": 28,
      "end_index": 31,
      "summary": "In 2023, the Federal Reserve collaborated ..."
    }
  ]
}
...
```

You can generate the PageIndex tree structure with this open-source repo, or use our [API](https://pageindex.ai/developer).

---

# ⚙️ Package Usage

You can follow these steps to generate a PageIndex tree from a PDF document.

### 1. Install dependencies

```bash
pip3 install --upgrade -r requirements.txt
```

### 2. Set your LLM API key

Create a `.env` file in the root directory with your LLM API key, with multi-LLM support via [LiteLLM](https://docs.litellm.ai/docs/providers):

```bash
OPENAI_API_KEY=your_openai_key_here
```

### 3. Generate PageIndex structure for your PDF

```bash
python3 run_pageindex.py --pdf_path /path/to/your/document.pdf
```

<details>
<summary>Optional parameters</summary>
<br>
You can customize the processing with additional optional arguments:

```
--model                 LLM model to use (default: gpt-4o-2024-11-20)
--toc-check-pages       Pages to check for table of contents (default: 20)
--max-pages-per-node    Max pages per node (default: 10)
--max-tokens-per-node   Max tokens per node (default: 20000)
--if-add-node-id        Add node ID (yes/no, default: yes)
--if-add-node-summary   Add node summary (yes/no, default: yes)
--if-add-doc-description Add doc description (yes/no, default: yes)
```
</details>

<details>
<summary>Markdown support</summary>
<br>
We also provide markdown support for PageIndex. You can use the `--md_path` flag to generate a tree structure for a markdown file.

```bash
python3 run_pageindex.py --md_path /path/to/your/document.md
```

> Note: in this mode, we use "#" to determine node headings and their levels. For example, "##" is level 2, "###" is level 3, etc. Make sure your markdown file is formatted correctly. If your Markdown file was converted from a PDF or HTML, we don't recommend using this mode, since most existing conversion tools cannot preserve the original hierarchy. Instead, use our [PageIndex OCR](https://pageindex.ai/blog/ocr), which is designed to preserve the original hierarchy, to convert the PDF to a markdown file and then use this mode.
</details>

## Agentic Vectorless RAG: An Example

For a simple, end-to-end _**agentic vectorless RAG**_ example using PageIndex with OpenAI Agents SDK, see [`examples/agentic_vectorless_rag_demo.py`](examples/agentic_vectorless_rag_demo.py).

```bash
# Install optional dependency
pip3 install openai-agents

# Run the demo
python3 examples/agentic_vectorless_rag_demo.py
```

<!--
# ☁️ Improved Tree Generation with PageIndex OCR

This repo is designed for generating PageIndex tree structure for simple PDFs, but many real-world use cases involve complex PDFs that are hard to parse by classic Python tools. However, extracting high-quality text from PDF documents remains a non-trivial challenge. Most OCR tools only extract page-level content, losing the broader document context and hierarchy.

To address this, we introduced PageIndex OCR — the first long-context OCR model designed to preserve the global structure of documents. PageIndex OCR significantly outperforms other leading OCR tools, such as those from Mistral and Contextual AI, in recognizing true hierarchy and semantic relationships across document pages.

- Experience next-level OCR quality with PageIndex OCR at our [Dashboard](https://dash.pageindex.ai/).
- Integrate PageIndex OCR seamlessly into your stack via our [API](https://docs.pageindex.ai/quickstart).

<p align="center">
  <img src="https://github.com/user-attachments/assets/eb35d8ae-865c-4e60-a33b-ebbd00c41732" width="80%">
</p>
-->

---

# 📈 Case Study: PageIndex Leads Finance QA Benchmark

[Mafin 2.5](https://vectify.ai/mafin) is a reasoning-based RAG system for financial document analysis, powered by **PageIndex**. It achieved a state-of-the-art [**98.7% accuracy**](https://vectify.ai/blog/Mafin2.5) on the [FinanceBench](https://arxiv.org/abs/2311.11944) benchmark, significantly outperforming traditional vector-based RAG systems.

PageIndex's hierarchical indexing and reasoning-driven retrieval enable precise navigation and extraction of relevant context from complex financial reports, such as SEC filings and earnings disclosures.

Explore the full [benchmark results](https://github.com/VectifyAI/Mafin2.5-FinanceBench) and our [blog post](https://vectify.ai/blog/Mafin2.5) for detailed comparisons and performance metrics.

<div align="center">
  <a href="https://github.com/VectifyAI/Mafin2.5-FinanceBench">
    <img src="https://github.com/user-attachments/assets/571aa074-d803-43c7-80c4-a04254b782a3" width="70%">
  </a>
</div>

---

# 🧭 Resources

* 📝 [Blog](https://pageindex.ai/blog): technical articles, research insights, and product updates.
* 🔧 [Developer](https://pageindex.ai/developer): MCP setup, API docs, and integration guides.
* 🧪 [Cookbooks](https://docs.pageindex.ai/cookbook): hands-on, runnable examples and advanced use cases.
* 📖 [Tutorials](https://docs.pageindex.ai/tutorials): practical guides and strategies, including *Document Search* and *Tree Search*.

---

# ⭐ Support Us

Leave us a star 🌟 if you like our project. Thank you!  

<p>
  <img src="https://github.com/user-attachments/assets/eae4ff38-48ae-4a7c-b19f-eab81201d794" width="80%">
</p>

Please cite this work as:
```
Mingtian Zhang, Yu Tang and PageIndex Team,
"PageIndex: Next-Generation Vectorless, Reasoning-based RAG",
PageIndex Blog, Sep 2025.
```

<details>
<summary>Or use the BibTeX citation.</summary>

```bibtex
@article{zhang2025pageindex,
  author = {Mingtian Zhang and Yu Tang and PageIndex Team},
  title = {PageIndex: Next-Generation Vectorless, Reasoning-based RAG},
  journal = {PageIndex Blog},
  year = {2025},
  month = {September},
  note = {https://pageindex.ai/blog/pageindex-intro},
}
```
</details>


### Connect with Us

<div align="center">

[![Twitter](https://img.shields.io/badge/Twitter-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/PageIndexAI)&ensp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/vectify-ai/)&ensp;
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/VuXuf29EUj)&ensp;
[![Contact Us](https://img.shields.io/badge/Contact_Us-3B82F6?style=for-the-badge&lo
... [TRUNCATED]
```

### File: requirements.txt
```txt
litellm==1.82.0
# openai-agents  # optional: required for examples/agentic_vectorless_rag_demo.py
pymupdf==1.26.4
PyPDF2==3.0.1
python-dotenv==1.1.0
pyyaml==6.0.2

```

### File: cookbook\README.md
```md
### 🧪 Cookbooks:

* [**Vectorless RAG notebook**](https://github.com/VectifyAI/PageIndex/blob/main/cookbook/pageindex_RAG_simple.ipynb): A *minimal*, hands-on example of reasoning-based RAG using **PageIndex** — no vectors, no chunking, and human-like retrieval.
* [Vision-based Vectorless RAG notebook](https://github.com/VectifyAI/PageIndex/blob/main/cookbook/vision_RAG_pageindex.ipynb): no OCR; reasoning-native RAG pipeline that retrieves and reasons directly over page images.

<div align="center">
  <a href="https://colab.research.google.com/github/VectifyAI/PageIndex/blob/main/cookbook/pageindex_RAG_simple.ipynb" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/Open_In_Colab-Vectorless_RAG-orange?style=for-the-badge&logo=googlecolab" alt="Open in Colab: Vectorless RAG" />
  </a>
  &nbsp;&nbsp;
  <a href="https://colab.research.google.com/github/VectifyAI/PageIndex/blob/main/cookbook/vision_RAG_pageindex.ipynb" target="_blank" rel="noopener">
    <img src="https://img.shields.io/badge/Open_In_Colab-Vision_RAG-orange?style=for-the-badge&logo=googlecolab" alt="Open in Colab: Vision RAG" />
  </a>
</div>
```

### File: run_pageindex.py
```py
import argparse
import os
import json
from pageindex import *
from pageindex.page_index_md import md_to_tree
from pageindex.utils import ConfigLoader

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process PDF or Markdown document and generate structure')
    parser.add_argument('--pdf_path', type=str, help='Path to the PDF file')
    parser.add_argument('--md_path', type=str, help='Path to the Markdown file')

    parser.add_argument('--model', type=str, default=None, help='Model to use (overrides config.yaml)')

    parser.add_argument('--toc-check-pages', type=int, default=None,
                      help='Number of pages to check for table of contents (PDF only)')
    parser.add_argument('--max-pages-per-node', type=int, default=None,
                      help='Maximum number of pages per node (PDF only)')
    parser.add_argument('--max-tokens-per-node', type=int, default=None,
                      help='Maximum number of tokens per node (PDF only)')

    parser.add_argument('--if-add-node-id', type=str, default=None,
                      help='Whether to add node id to the node')
    parser.add_argument('--if-add-node-summary', type=str, default=None,
                      help='Whether to add summary to the node')
    parser.add_argument('--if-add-doc-description', type=str, default=None,
                      help='Whether to add doc description to the doc')
    parser.add_argument('--if-add-node-text', type=str, default=None,
                      help='Whether to add text to the node')
                      
    # Markdown specific arguments
    parser.add_argument('--if-thinning', type=str, default='no',
                      help='Whether to apply tree thinning for markdown (markdown only)')
    parser.add_argument('--thinning-threshold', type=int, default=5000,
                      help='Minimum token threshold for thinning (markdown only)')
    parser.add_argument('--summary-token-threshold', type=int, default=200,
                      help='Token threshold for generating summaries (markdown only)')
    args = parser.parse_args()
    
    # Validate that exactly one file type is specified
    if not args.pdf_path and not args.md_path:
        raise ValueError("Either --pdf_path or --md_path must be specified")
    if args.pdf_path and args.md_path:
        raise ValueError("Only one of --pdf_path or --md_path can be specified")
    
    if args.pdf_path:
        # Validate PDF file
        if not args.pdf_path.lower().endswith('.pdf'):
            raise ValueError("PDF file must have .pdf extension")
        if not os.path.isfile(args.pdf_path):
            raise ValueError(f"PDF file not found: {args.pdf_path}")
            
        # Process PDF file
        user_opt = {
            'model': args.model,
            'toc_check_page_num': args.toc_check_pages,
            'max_page_num_each_node': args.max_pages_per_node,
            'max_token_num_each_node': args.max_tokens_per_node,
            'if_add_node_id': args.if_add_node_id,
            'if_add_node_summary': args.if_add_node_summary,
            'if_add_doc_description': args.if_add_doc_description,
            'if_add_node_text': args.if_add_node_text,
        }
        opt = ConfigLoader().load({k: v for k, v in user_opt.items() if v is not None})

        # Process the PDF
        toc_with_page_number = page_index_main(args.pdf_path, opt)
        print('Parsing done, saving to file...')
        
        # Save results
        pdf_name = os.path.splitext(os.path.basename(args.pdf_path))[0]    
        output_dir = './results'
        output_file = f'{output_dir}/{pdf_name}_structure.json'
        os.makedirs(output_dir, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(toc_with_page_number, f, indent=2)
        
        print(f'Tree structure saved to: {output_file}')
            
    elif args.md_path:
        # Validate Markdown file
        if not args.md_path.lower().endswith(('.md', '.markdown')):
            raise ValueError("Markdown file must have .md or .markdown extension")
        if not os.path.isfile(args.md_path):
            raise ValueError(f"Markdown file not found: {args.md_path}")
            
        # Process markdown file
        print('Processing markdown file...')
        
        # Process the markdown
        import asyncio
        
        # Use ConfigLoader to get consistent defaults (matching PDF behavior)
        from pageindex.utils import ConfigLoader
        config_loader = ConfigLoader()
        
        # Create options dict with user args
        user_opt = {
            'model': args.model,
            'if_add_node_summary': args.if_add_node_summary,
            'if_add_doc_description': args.if_add_doc_description,
            'if_add_node_text': args.if_add_node_text,
            'if_add_node_id': args.if_add_node_id
        }
        
        # Load config with defaults from config.yaml
        opt = config_loader.load(user_opt)
        
        toc_with_page_number = asyncio.run(md_to_tree(
            md_path=args.md_path,
            if_thinning=args.if_thinning.lower() == 'yes',
            min_token_threshold=args.thinning_threshold,
            if_add_node_summary=opt.if_add_node_summary,
            summary_token_threshold=args.summary_token_threshold,
            model=opt.model,
            if_add_doc_description=opt.if_add_doc_description,
            if_add_node_text=opt.if_add_node_text,
            if_add_node_id=opt.if_add_node_id
        ))
        
        print('Parsing done, saving to file...')
        
        # Save results
        md_name = os.path.splitext(os.path.basename(args.md_path))[0]    
        output_dir = './results'
        output_file = f'{output_dir}/{md_name}_structure.json'
        os.makedirs(output_dir, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(toc_with_page_number, f, indent=2, ensure_ascii=False)
        
        print(f'Tree structure saved to: {output_file}')
```

### File: examples\agentic_vectorless_rag_demo.py
```py
"""
Agentic Vectorless RAG with PageIndex - Demo

A simple example of building a document QA agent with self-hosted PageIndex
and the OpenAI Agents SDK. Instead of vector similarity search and chunking,
PageIndex builds a hierarchical tree index and uses agentic LLM reasoning for
human-like, context-aware retrieval.

Agent tools:
  - get_document()           — document metadata (status, page count, etc.)
  - get_document_structure() — tree structure index of a document
  - get_page_content()       — retrieve text content of specific pages

Steps:
  1 — Index a PDF and view its tree structure index
  2 — View document metadata
  3 — Ask a question (agent reasons over the index and auto-calls tools)

Requirements: pip install openai-agents
"""
import sys
import json
import asyncio
import concurrent.futures
from pathlib import Path
import requests

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents import Agent, Runner, function_tool, set_tracing_disabled
from agents.model_settings import ModelSettings
from agents.stream_events import RawResponsesStreamEvent, RunItemStreamEvent
from openai.types.responses import ResponseTextDeltaEvent, ResponseReasoningSummaryTextDeltaEvent

from pageindex import PageIndexClient
import pageindex.utils as utils

PDF_URL = "https://arxiv.org/pdf/2603.15031"

_EXAMPLES_DIR = Path(__file__).parent
PDF_PATH = _EXAMPLES_DIR / "documents" / "attention-residuals.pdf"
WORKSPACE = _EXAMPLES_DIR / "workspace"

AGENT_SYSTEM_PROMPT = """
You are PageIndex, a document QA assistant.
TOOL USE:
- Call get_document() first to confirm status and page/line count.
- Call get_document_structure() to identify relevant page ranges.
- Call get_page_content(pages="5-7") with tight ranges; never fetch the whole document.
- Before each tool call, output one short sentence explaining the reason.
Answer based only on tool output. Be concise.
"""


def query_agent(client: PageIndexClient, doc_id: str, prompt: str, verbose: bool = False) -> str:
    """Run a document QA agent using the OpenAI Agents SDK.

    Streams text output token-by-token and returns the full answer string.
    Tool calls are always printed; verbose=True also prints arguments and output previews.
    """

    @function_tool
    def get_document() -> str:
        """Get document metadata: status, page count, name, and description."""
        return client.get_document(doc_id)

    @function_tool
    def get_document_structure() -> str:
        """Get the document's full tree structure (without text) to find relevant sections."""
        return client.get_document_structure(doc_id)

    @function_tool
    def get_page_content(pages: str) -> str:
        """
        Get the text content of specific pages or line numbers.
        Use tight ranges: e.g. '5-7' for pages 5 to 7, '3,8' for pages 3 and 8, '12' for page 12.
        For Markdown documents, use line numbers from the structure's line_num field.
        """
        return client.get_page_content(doc_id, pages)

    agent = Agent(
        name="PageIndex",
        instructions=AGENT_SYSTEM_PROMPT,
        tools=[get_document, get_document_structure, get_page_content],
        model=client.retrieve_model,
        # model_settings=ModelSettings(reasoning={"effort": "low", "summary": "auto"}),  # Uncomment to enable reasoning
    )

    async def _run():
        streamed_run = Runner.run_streamed(agent, prompt)
        current_stream_kind = None
        async for event in streamed_run.stream_events():
            if isinstance(event, RawResponsesStreamEvent):
                if isinstance(event.data, ResponseReasoningSummaryTextDeltaEvent):
                    if current_stream_kind != "reasoning":
                        if current_stream_kind is not None:
                            print()
                        print("\n[reasoning]: ", end="", flush=True)
                    delta = event.data.delta
                    print(delta, end="", flush=True)
                    current_stream_kind = "reasoning"
                elif isinstance(event.data, ResponseTextDeltaEvent):
                    if current_stream_kind != "text":
                        if current_stream_kind is not None:
                            print()
                        print("\n[text]: ", end="", flush=True)
                    delta = event.data.delta
                    print(delta, end="", flush=True)
                    current_stream_kind = "text"
            elif isinstance(event, RunItemStreamEvent):
                item = event.item
                if item.type == "tool_call_item":
                    if current_stream_kind is not None:
                        print()
                    raw = item.raw_item
                    args = getattr(raw, "arguments", "{}")
                    args_str = f"({args})" if verbose else ""
                    print(f"\n[tool call]: {raw.name}{args_str}", flush=True)
                    current_stream_kind = None
                elif item.type == "tool_call_output_item" and verbose:
                    if current_stream_kind is not None:
                        print()
                    output = str(item.output)
                    preview = output[:200] + "..." if len(output) > 200 else output
                    print(f"\n[tool call output]: {preview}", flush=True)
                    current_stream_kind = None
        if current_stream_kind is not None:
            print()
        return "" if not streamed_run.final_output else str(streamed_run.final_output)

    try:
        asyncio.get_running_loop()
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            return pool.submit(asyncio.run, _run()).result()
    except RuntimeError:
        return asyncio.run(_run())


if __name__ == "__main__":

    set_tracing_disabled(True)

    # Download PDF if needed
    if not PDF_PATH.exists():
        print(f"Downloading {PDF_URL} ...")
        PDF_PATH.parent.mkdir(parents=True, exist_ok=True)
        with requests.get(PDF_URL, stream=True, timeout=30) as r:
            r.raise_for_status()
            with open(PDF_PATH, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        print("Download complete.\n")

    # Setup
    client = PageIndexClient(workspace=WORKSPACE)

    # Step 1: Index PDF and view tree structure
    print("=" * 60)
    print("Step 1: Index PDF and view tree structure")
    print("=" * 60)
    doc_id = next(
        (did for did, doc in client.documents.items() if doc.get('doc_name') == PDF_PATH.name),
        None,
    )
    if doc_id:
        print(f"\nLoaded cached doc_id: {doc_id}")
    else:
        doc_id = client.index(PDF_PATH)
        print(f"\nIndexed. doc_id: {doc_id}")
    print("\nTree Structure (top-level sections):")
    structure = json.loads(client.get_document_structure(doc_id))
    utils.print_tree(structure)

    # Step 2: View document metadata
    print("\n" + "=" * 60)
    print("Step 2: View document metadata")
    print("=" * 60)
    doc_metadata = client.get_document(doc_id)
    print(f"\n{doc_metadata}")

    # Step 3: Agent Query
    print("\n" + "=" * 60)
    print("Step 3: Agent Query (auto tool-use)")
    print("=" * 60)
    question = "Explain Attention Residuals in simple language."
    print(f"\nQuestion: '{question}'")
    query_agent(client, doc_id, question, verbose=True)

```

### File: .claude\commands\dedupe.md
```md
---
allowed-tools:
  - Bash(gh:*)
  - Bash(./.github/scripts/comment-on-duplicates.sh:*)
---

You are a GitHub issue deduplication assistant. Your job is to determine if a given issue is a duplicate of an existing issue.

## Input

The issue to check: $ARGUMENTS

## Steps

### 1. Pre-checks

First, check if the issue should be skipped:

```
gh issue view <number> --json state,labels,title,body,comments
```

Skip if:
- The issue is already closed
- The issue already has a `duplicate` label
- The issue already has a dedupe comment (check comments for "possible duplicate")

### 2. Understand the issue

Read the issue carefully and generate a concise summary of the core problem or feature request. Extract 3-5 key technical terms or concepts.

### 3. Search for duplicates

Launch 5 parallel searches using different keyword strategies to maximize coverage:

1. **Exact terms**: Use the most specific technical terms from the issue title
2. **Synonyms**: Use alternative phrasings for the core problem
3. **Error messages**: If the issue contains error messages, search for those
4. **Component names**: Search by the specific component/module mentioned
5. **Broad category**: Search by the general category of the issue

For each search, use:
```
gh search issues "<keywords> state:open" --repo $REPOSITORY --limit 20
```

### 4. Analyze candidates

For each unique candidate issue found:
- Compare the core problem being described
- Look past superficial wording differences
- Consider whether they describe the same root cause
- Only flag as duplicate if you are at least 85% confident

### 5. Filter false positives

Remove candidates that:
- Are only superficially similar (same area but different problems)
- Are related but describe distinct issues
- Are too old or already resolved differently

### 6. Report results

If you found duplicates (max 3), call:
```
./.github/scripts/comment-on-duplicates.sh --base-issue <number> --potential-duplicates <dup1> <dup2> ...
```

If no duplicates found, do nothing and report that the issue appears to be unique.

```

### File: .github\scripts\autoclose-labeled-issues.js
```js
/**
 * scripts/autoclose-labeled-issues.js
 *
 * Auto-closes issues that have a bot "possible duplicate" comment older than
 * 3 days, unless:
 * - A human has commented after the bot's duplicate comment
 * - The author reacted with thumbs-down on the duplicate comment
 *
 * Required environment variables:
 *   GITHUB_TOKEN  - GitHub Actions token
 *   REPO_OWNER    - Repository owner
 *   REPO_NAME     - Repository name
 *
 * Optional:
 *   DRY_RUN       - If "true", report but do not close (default: false)
 */

'use strict';

const https = require('https');

const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
const REPO_OWNER   = process.env.REPO_OWNER;
const REPO_NAME    = process.env.REPO_NAME;
const DRY_RUN      = process.env.DRY_RUN === 'true';

const THREE_DAYS_MS = 3 * 24 * 60 * 60 * 1000;

function githubRequest(method, path, body = null, retried = false) {
  return new Promise((resolve, reject) => {
    const payload = body ? JSON.stringify(body) : null;
    const options = {
      hostname: 'api.github.com',
      path,
      method,
      headers: {
        'Authorization': `Bearer ${GITHUB_TOKEN}`,
        'Accept': 'application/vnd.github+json',
        'User-Agent': 'PageIndex-Autoclose/1.0',
        'X-GitHub-Api-Version': '2022-11-28',
        ...(payload ? { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(payload) } : {}),
      },
    };

    const req = https.request(options, (res) => {
      let data = '';
      res.on('data', chunk => (data += chunk));
      res.on('end', async () => {
        // 429: 始终重试（rate limit）
        if (res.statusCode === 429 && !retried) {
          const retryAfter = parseInt(res.headers['retry-after'] || '60', 10);
          console.log(`  Rate limited on ${method} ${path}, retrying after ${retryAfter}s...`);
          await sleep(retryAfter * 1000);
          try { resolve(await githubRequest(method, path, body, true)); }
          catch (err) { reject(err); }
          return;
        }
        // 403: 只在 rate limit 相关时重试
        if (res.statusCode === 403 && !retried) {
          const rateLimitRemaining = res.headers['x-ratelimit-remaining'];
          const hasRetryAfter = res.headers['retry-after'];
          if (rateLimitRemaining === '0' || hasRetryAfter) {
            const retryAfter = parseInt(hasRetryAfter || '60', 10);
            console.log(`  Rate limited (403) on ${method} ${path}, retrying after ${retryAfter}s...`);
            await sleep(retryAfter * 1000);
            try { resolve(await githubRequest(method, path, body, true)); }
            catch (err) { reject(err); }
            return;
          }
        }
        if (res.statusCode >= 400) {
          reject(new Error(`GitHub API ${method} ${path} -> ${res.statusCode}: ${data}`));
          return;
        }
        try { resolve(data ? JSON.parse(data) : {}); }
        catch { resolve({}); }
      });
    });
    req.on('error', reject);
    if (payload) req.write(payload);
    req.end();
  });
}

const sleep = (ms) => new Promise(r => setTimeout(r, ms));

/**
 * Fetches open issues with the "duplicate" label, paginating as needed.
 * Only returns issues created more than 3 days ago.
 */
async function fetchDuplicateIssues() {
  const issues = [];
  let page = 1;
  while (true) {
    const data = await githubRequest(
      'GET',
      `/repos/${REPO_OWNER}/${REPO_NAME}/issues?state=open&labels=duplicate&per_page=100&page=${page}`
    );
    if (!Array.isArray(data) || data.length === 0) break;
    issues.push(...data.filter(i => !i.pull_request));
    if (data.length < 100) break;
    page++;
  }

  const cutoff = new Date(Date.now() - THREE_DAYS_MS);
  return issues.filter(i => new Date(i.created_at) < cutoff);
}

function isBot(user) {
  return user.type === 'Bot' || user.login.endsWith('[bot]') || user.login === 'github-actions';
}

/**
 * Finds the bot's duplicate comment on an issue (contains "possible duplicate").
 */
function findDuplicateComment(comments) {
  return comments.find(c =>
    isBot(c.user) && c.body.includes('possible duplicate')
  );
}

/**
 * Checks if there are human comments after the duplicate comment.
 */
function hasHumanCommentAfter(comments, afterDate) {
  return comments.some(c => {
    if (isBot(c.user)) return false;
    return new Date(c.created_at) > afterDate;
  });
}

/**
 * Fetches all comments for an issue, handling pagination.
 * Requests per_page=100 and loops until we get fewer than 100 or an empty array.
 */
async function fetchAllComments(issueNumber) {
  const allComments = [];
  let page = 1;
  while (true) {
    const comments = await githubRequest(
      'GET',
      `/repos/${REPO_OWNER}/${REPO_NAME}/issues/${issueNumber}/comments?per_page=100&page=${page}`
    );
    if (!Array.isArray(comments) || comments.length === 0) break;
    allComments.push(...comments);
    if (comments.length < 100) break;
    page++;
  }
  return allComments;
}

/**
 * Checks if the duplicate comment has a thumbs-down reaction.
 */
async function hasThumbsDownReaction(commentId) {
  const reactions = await githubRequest(
    'GET',
    `/repos/${REPO_OWNER}/${REPO_NAME}/issues/comments/${commentId}/reactions`
  );
  return Array.isArray(reactions) && reactions.some(r => r.content === '-1');
}

/**
 * Closes an issue as duplicate with a comment.
 */
async function closeAsDuplicate(issueNumber) {
  const body =
    'This issue has been automatically closed as a duplicate. ' +
    'No human activity or objection was received within the 3-day grace period.\n\n' +
    'If you believe this was closed in error, please reopen the issue and leave a comment.';

  await githubRequest(
    'POST',
    `/repos/${REPO_OWNER}/${REPO_NAME}/issues/${issueNumber}/comments`,
    { body }
  );

  await githubRequest(
    'PATCH',
    `/repos/${REPO_OWNER}/${REPO_NAME}/issues/${issueNumber}`,
    { state: 'closed', state_reason: 'completed' }
  );
}

async function processIssue(issue) {
  const num = issue.number;
  console.log(`\nChecking issue #${num}: ${issue.title}`);

  const comments = await fetchAllComments(num);

  if (!Array.isArray(comments) || comments.length === 0) {
    console.log(`  -> Could not fetch comments, skipping.`);
    return false;
  }

  const dupeComment = findDuplicateComment(comments);
  if (!dupeComment) {
    console.log(`  -> No duplicate comment found, skipping.`);
    return false;
  }

  const commentDate = new Date(dupeComment.created_at);
  const ageMs = Date.now() - commentDate.getTime();

  if (ageMs < THREE_DAYS_MS) {
    const daysLeft = Math.ceil((THREE_DAYS_MS - ageMs) / (24 * 60 * 60 * 1000));
    console.log(`  -> Duplicate comment is less than 3 days old (${daysLeft}d remaining), skipping.`);
    return false;
  }

  if (hasHumanCommentAfter(comments, commentDate)) {
    console.log(`  -> Human commented after duplicate comment, skipping.`);
    return false;
  }

  if (await hasThumbsDownReaction(dupeComment.id)) {
    console.log(`  -> Author reacted with thumbs-down, skipping.`);
    return false;
  }

  if (DRY_RUN) {
    console.log(`  [DRY RUN] Would close issue #${num}`);
    return true;
  }

  await closeAsDuplicate(num);
  console.log(`  -> Closed issue #${num} as duplicate`);
  return true;
}

async function main() {
  const missing = ['GITHUB_TOKEN', 'REPO_OWNER', 'REPO_NAME'].filter(k => !process.env[k]);
  if (missing.length) {
    console.error(`Missing required environment variables: ${missing.join(', ')}`);
    process.exit(1);
  }

  console.log('Auto-close duplicate issues');
  console.log(`  Repository: ${REPO_OWNER}/${REPO_NAME}`);
  console.log(`  Dry run:    ${DRY_RUN}`);

  const issues = await fetchDuplicateIssues();
  console.log(`\nFound ${issues.length} duplicate-labeled issue(s) older than 3 days.`);

  let closedCount = 0;
  for (const issue of issues) {
    const closed = await processIssue(issue);
    if (closed) closedCount++;
    await sleep(1000);
  }

  console.log(`\nSummary: ${closedCount} issue(s) closed.`);
}

main().catch(err => {
  console.error('Fatal error:', err.message);
  process.exit(1);
});

```

### File: .github\scripts\comment-on-duplicates.sh
```sh
#!/usr/bin/env bash
#
# comment-on-duplicates.sh - Posts a duplicate issue comment with auto-close warning.
#
# Usage:
#   ./.github/scripts/comment-on-duplicates.sh --base-issue 123 --potential-duplicates 456 789
#
set -euo pipefail

REPO="${GITHUB_REPOSITORY:-}"
if [ -z "$REPO" ]; then
  echo "Error: GITHUB_REPOSITORY is not set" >&2
  exit 1
fi

BASE_ISSUE=""
DUPLICATES=()

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --base-issue)
      BASE_ISSUE="$2"
      shift 2
      ;;
    --potential-duplicates)
      shift
      while [[ $# -gt 0 && ! "$1" =~ ^-- ]]; do
        DUPLICATES+=("$1")
        shift
      done
      ;;
    *)
      echo "Error: Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

# Validate inputs
if [ -z "$BASE_ISSUE" ]; then
  echo "Error: --base-issue is required" >&2
  exit 1
fi

if ! [[ "$BASE_ISSUE" =~ ^[0-9]+$ ]]; then
  echo "Error: --base-issue must be a number, got: $BASE_ISSUE" >&2
  exit 1
fi

if [ ${#DUPLICATES[@]} -eq 0 ]; then
  echo "Error: --potential-duplicates requires at least one issue number" >&2
  exit 1
fi

for dup in "${DUPLICATES[@]}"; do
  if ! [[ "$dup" =~ ^[0-9]+$ ]]; then
    echo "Error: duplicate issue must be a number, got: $dup" >&2
    exit 1
  fi
done

# Limit to 3 duplicates max
if [ ${#DUPLICATES[@]} -gt 3 ]; then
  echo "Warning: Limiting to first 3 duplicates" >&2
  DUPLICATES=("${DUPLICATES[@]:0:3}")
fi

# Build the duplicate links list
COUNT=0
LINKS=""
for dup in "${DUPLICATES[@]}"; do
  COUNT=$((COUNT + 1))
  LINKS="${LINKS}${COUNT}. https://github.com/${REPO}/issues/${dup}
"
done

# Build and post the comment — if the issue is closed or doesn't exist, gh will error out
COMMENT="Found ${COUNT} possible duplicate issue(s):

${LINKS}
This issue will be automatically closed as a duplicate in 3 days.
- To prevent auto-closure, add a comment or react with :thumbsdown: on this comment."

gh issue comment "$BASE_ISSUE" --repo "$REPO" --body "$COMMENT"
gh issue edit "$BASE_ISSUE" --repo "$REPO" --add-label "duplicate"

echo "Posted duplicate comment on issue #$BASE_ISSUE with $COUNT potential duplicate(s)"

```

### File: examples\workspace\12345678-abcd-4321-abcd-123456789abc.json
```json
{
  "id": "12345678-abcd-4321-abcd-123456789abc",
  "type": "pdf",
  "path": "../documents/attention-residuals.pdf",
  "doc_name": "attention-residuals.pdf",
  "doc_description": "This document introduces \"Attention Residuals\" (AttnRes) and its scalable variant \"Block AttnRes,\" novel mechanisms for replacing fixed residual accumulation in neural networks with learned, input-dependent depth-wise attention, addressing limitations of standard residual connections while optimizing memory, computation, and scalability for large-scale training and inference.",
  "page_count": 21,
  "structure": [
    {
      "title": "Preface",
      "node_id": "0000",
      "start_index": 1,
      "end_index": 2,
      "summary": "The partial document introduces \"Attention Residuals\" (AttnRes), a novel approach to replace fixed residual accumulation in large language models (LLMs) with learned, input-dependent softmax attention over preceding layer outputs. This method addresses issues like uncontrolled hidden-state growth and dilution of layer contributions caused by standard residual connections with PreNorm. To enhance scalability, the document proposes \"Block AttnRes,\" which partitions layers into blocks and applies attention at the block level, reducing memory and communication overhead while maintaining performance gains. The document highlights system optimizations, such as cross-stage caching and a two-phase computation strategy, to make Block AttnRes efficient for large-scale training. Experiments confirm consistent improvements across model sizes, with AttnRes mitigating PreNorm dilution, leading to more uniform output magnitudes, gradient distributions, and better downstream task performance. Key contributions include the introduction of AttnRes and Block AttnRes, scalable infrastructure optimizations, and comprehensive evaluations demonstrating their effectiveness."
    },
    {
      "title": "Introduction",
      "node_id": "0001",
      "start_index": 2,
      "end_index": 3,
      "summary": "The partial document introduces \"Attention Residuals\" (AttnRes), a novel mechanism that replaces fixed residual accumulation in deep networks with learned softmax attention over depth. It highlights the limitations of standard residual connections, such as uniform layer contributions, irreversible information loss, and output growth, and draws parallels between depth-wise accumulation and sequence modeling in RNNs. AttnRes enables selective, content-aware aggregation of information across layers using attention weights, addressing these limitations. The document also proposes a scalable variant, Block AttnRes, which reduces memory and communication overhead for large-scale training. Key contributions include the development of AttnRes and Block AttnRes, system optimizations for scalability, and comprehensive evaluations demonstrating improved training dynamics, bounded hidden-state magnitudes, and better gradient distribution. The approach is validated through scaling law experiments, ablations, and downstream benchmarks, showing consistent performance improvements over standard residual connections."
    },
    {
      "title": "Motivation",
      "node_id": "0002",
      "start_index": 3,
      "end_index": 3,
      "summary": "The partial document discusses the concept of Attention Residuals in the context of deep learning models, particularly Transformers. It begins by introducing the notation and structure of input sequences and layers in a Transformer model. The document then explains residual learning, highlighting its importance in training deep networks by enabling gradients to bypass transformations through identity mapping. It expands on the limitations of traditional residual connections and highway networks, such as lack of selective access to earlier layer outputs, irreversible information loss, and output growth issues that destabilize training. To address these limitations, the document proposes Attention Residuals (AttnRes), a mechanism inspired by the duality of time and depth in sequence modeling. This approach introduces layer-specific attention weights to selectively aggregate information from all preceding layers, offering a unified view of time and depth while maintaining computational feasibility."
    },
    {
      "title": "Attention Residuals: A Unified View of Time and Depth",
      "node_id": "0003",
      "start_index": 3,
      "end_index": 4,
      "summary": "The partial document discusses the concept of \"Attention Residuals\" as a mechanism to address limitations in training deep networks with residual connections. It begins by explaining residual learning, its benefits in gradient flow, and its limitations, such as lack of selective access, irreversible information loss, and output growth. The document introduces \"Attention Residuals\" (AttnRes), which generalizes residual connections by allowing layers to selectively aggregate information from all preceding layers using attention mechanisms. It describes \"Full Attention Residuals,\" which compute attention weights over depth with softmax normalization, and highlights their computational and memory overhead. To address scalability challenges, the document proposes \"Block Attention Residuals,\" which partition layers into blocks, reducing memory and communication overhead by applying attention at the block level. The text also outlines the intra-block accumulation process and its efficiency in distributed training setups.",
      "nodes": [
        {
          "title": "Full Attention Residuals",
          "node_id": "0004",
          "start_index": 4,
          "end_index": 4,
          "summary": "The partial document discusses \"Attention Residuals\" in neural networks, focusing on two main approaches: Full Attention Residuals and Block Attention Residuals. \n\n1. **Full Attention Residuals**: This method computes attention weights using a kernel function with RMS normalization to prevent large-magnitude outputs from dominating. It introduces no additional memory overhead during vanilla training but incurs communication and memory overhead in distributed training due to the need to retain and transmit layer outputs across stages. A blockwise optimization strategy is proposed to reduce memory I/O by batching attention computation within groups of layers.\n\n2. **Block Attention Residuals**: This approach partitions layers into blocks, reducing memory and communication overhead by summing layer outputs within each block and applying attention only to block-level representations. This reduces the complexity from O(Ld) to O(Nd), where N is the number of blocks. The method ensures normalization to avoid biases from magnitude differences between blocks.\n\nThe document highlights the trade-offs between memory, computation, and communication overheads in these methods and introduces strategies to optimize their efficiency in distributed training setups."
        },
        {
          "title": "Block Attention Residuals",
          "node_id": "0005",
          "start_index": 4,
          "end_index": 5,
          "summary": "The partial document discusses \"Attention Residuals,\" focusing on two main variants: Full Attention Residuals (Full AttnRes) and Block Attention Residuals (Block AttnRes). \n\n1. **Full Attention Residuals (Full AttnRes):**\n   - Defines attention weights using a kernel function with RMS normalization to prevent large-magnitude outputs from dominating.\n   - Requires O(L²d) arithmetic and O(Ld) memory, with no additional memory overhead during vanilla training.\n   - Highlights challenges in large-scale training, such as memory and communication overhead under pipeline parallelism.\n   - Introduces blockwise optimization to reduce memory I/O but notes that cross-stage communication remains a bottleneck.\n\n2. **Block Attention Residuals (Block AttnRes):**\n   - Partitions layers into blocks, reducing memory and communication overhead from O(Ld) to O(Nd) by summing layer outputs within blocks and applying attention over block-level representations.\n   - Provides PyTorch-style pseudocode for implementation, detailing intra-block accumulation and inter-block attention mechanisms.\n   - Improves efficiency by reducing memory and computation requirements, with block count N interpolating between Full AttnRes (N=L) and standard residual connections (N=1).\n   - Enhances inference latency and bounds KV cache size through blockwise optimization.\n\nThe document also addresses infrastructure challenges for large-scale training, emphasizing the need to manage communication overhead and optimize system design for block-based attention mechanisms."
        }
      ]
    },
    {
      "title": "Infrastructure Design",
      "node_id": "0006",
      "start_index": 5,
      "end_index": 6,
      "summary": "The partial document describes the concept and implementation of Block Attention Residuals (Block AttnRes), a mechanism designed to improve memory and computational efficiency in attention-based models. It introduces inter-block attention, where attention is computed over block representations and partial sums, reducing memory and computation from O(L) and O(L²) to O(N) and O(N²), respectively. The document provides PyTorch-style pseudocode for the implementation, detailing how block representations and partial sums are managed across layers. It highlights the efficiency benefits of using block representations instead of individual outputs, with empirical findings suggesting that a block count of N≈8 balances performance and resource usage. \n\nThe document also addresses infrastructure challenges in large-scale training and inference. It discusses pipeline communication optimizations, such as cross-stage caching, to reduce redundant data transmission and improve efficiency during distributed training. For inference, it proposes a two-phase computation strategy and memory-efficient prefilling to handle long-context scenarios. An example of cache-based pipeline communication is provided, illustrating how caching minimizes communication overhead in distributed systems.",
      "nodes": [
        {
          "title": "Training",
          "node_id": "0007",
          "start_index": 6,
          "end_index": 7,
          "summary": "The partial document discusses the optimization of Attention Residuals (AttnRes) in training and inference for large-scale distributed systems. It introduces cross-stage caching to address communication and memory overheads in pipeline parallelism, reducing redundant data transmission and improving efficiency. The document details a two-phase computation strategy for Block AttnRes, which includes parallel inter-block attention and sequential intra-block attention with online softmax merging. This approach minimizes memory access and I/O overhead while maintaining a low training overhead. Additionally, it highlights the memory-efficient prefilling scheme for long-context inputs and explains how Block AttnRes compresses representations to reduce storage requirements. The document also provides algorithmic details and performance improvements in both training and inference scenarios."
        },
        {
          "title": "Inference",
          "node_id": "0008",
          "start_index": 7,
          "end_index": 8,
          "summary": "The partial document describes the technical details and implementation of Attention Residuals (AttnRes) in neural network architectures. It introduces a two-phase computation strategy for block-based attention, optimizing memory and computational efficiency. Phase 1 handles parallel inter-block attention, while Phase 2 processes sequential intra-block attention with an online softmax merge. The document highlights memory overhead reduction through cross-stage caching, sequence-sharded prefilling, and kernel fusion, achieving minimal training and inference latency overhead. It compares memory access costs across different residual mechanisms and demonstrates the efficiency of AttnRes, particularly in Block AttnRes, which compresses block representations. Experimental results show that AttnRes improves scaling behavior and validation loss compared to baseline models, with negligible parameter overhead and consistent performance gains across compute ranges."
        }
      ]
    },
    {
      "title": "Experiments",
      "node_id": "0009",
      "start_index": 8,
      "end_index": 8,
      "summary": "The partial document discusses the technical details and performance of the Attention Residuals (AttnRes) mechanism in transformer architectures. It highlights the memory efficiency and reduced inference latency of AttnRes compared to prior residual mechanisms like mHC. The document provides a breakdown of memory access costs for different schemes, emphasizing the two-phase inference schedule of AttnRes and its memory-efficient prefilling strategy, which significantly reduces memory overhead through sharding and chunked prefill techniques. It also describes the integration of AttnRes into a Mixture-of-Experts (MoE) Transformer architecture, detailing its minimal parameter addition and initialization strategy to ensure stable training. Additionally, the document presents experimental results, including scaling laws and validation loss comparisons across model variants, demonstrating that AttnRes achieves consistently lower loss while maintaining similar scaling behavior to the baseline.",
      "nodes": [
        {
          "title": "Scaling Laws",
          "node_id": "0010",
          "start_index": 8,
          "end_index": 9,
          "summary": "The partial document discusses the implementation and evaluation of Attention Residuals (AttnRes) in transformer architectures. It highlights the memory efficiency and reduced inference latency of AttnRes compared to prior residual mechanisms like mHC. The document introduces a two-phase inference schedule for AttnRes, optimizing memory access costs and reducing per-device memory usage through sharding and chunked prefill techniques. It describes the integration of AttnRes into a Mixture-of-Experts (MoE) Transformer architecture, maintaining minimal parameter overhead and ensuring stable training through specific initialization strategies. Experiments compare scaling laws and validation loss across model sizes, showing that both Full and Block AttnRes outperform baselines and mHC in terms of loss and compute efficiency. The main results include training recipes for large-scale models, leveraging hybrid attention mechanisms and progressive sequence length extension without additional modifications."
        },
        {
          "title": "Main Results",
          "node_id": "0011",
          "start_index": 9,
          "end_index": 11,
          "summary": "The partial document discusses the concept of Attention Residuals (AttnRes) in transformer models, comparing its performance and efficiency against baseline models 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

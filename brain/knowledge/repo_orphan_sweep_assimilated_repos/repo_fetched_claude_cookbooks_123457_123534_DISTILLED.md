---
id: repo-fetched-claude-cookbooks-123457-123534
type: knowledge
owner: OA
registered_at: 2026-04-05T04:40:18.502781
tags: ["auto-cloned", "Claude API", "Generative AI", "Python", "oa-assimilated", "premium-repo"]
---

# FETCHED_claude-cookbooks_123457_123534

## Assimilation Report
This repository is a developer resource providing code snippets and guides (cookbooks) to help developers build applications using the Claude API. It focuses on practical examples, primarily in Python, covering various AI capabilities like classification and RAG.

## Application for OmniClaw
OmniClaw can integrate this repository's structure by creating a 'Skill Cookbook' module. Instead of just providing static code, OmniClaw would parse the guides (e.g., Classification, RAG) and convert them into executable, parameterized micro-agents. For instance, the RAG guide would define a 'RetrievalAgent' skill that accepts a query and a document store path, executing the full workflow within OmniClaw's multi-agent orchestration layer, making the concepts immediately actionable within the OS.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Claude Cookbooks

The Claude Cookbooks provide code and guides designed to help developers build with Claude, offering copy-able code snippets that you can easily integrate into your own projects.

## Prerequisites

To make the most of the examples in this cookbook, you'll need a Claude API key (sign up for free [here](https://www.anthropic.com)).

While the code examples are primarily written in Python, the concepts can be adapted to any programming language that supports interaction with the Claude API.

If you're new to working with the Claude API, we recommend starting with our [Claude API Fundamentals course](https://github.com/anthropics/courses/tree/master/anthropic_api_fundamentals) to get a solid foundation.

## Explore Further

Looking for more resources to enhance your experience with Claude and AI assistants? Check out these helpful links:

- [Anthropic developer documentation](https://docs.claude.com/claude/docs/guide-to-anthropics-prompt-engineering-resources)
- [Anthropic support docs](https://support.anthropic.com)
- [Anthropic Discord community](https://www.anthropic.com/discord)

## Contributing

The Claude Cookbooks thrives on the contributions of the developer community. We value your input, whether it's submitting an idea, fixing a typo, adding a new guide, or improving an existing one. By contributing, you help make this resource even more valuable for everyone.

To avoid duplication of efforts, please review the existing issues and pull requests before contributing.

If you have ideas for new examples or guides, share them on the [issues page](https://github.com/anthropics/anthropic-cookbook/issues).

## Table of recipes

### Capabilities
- [Classification](https://github.com/anthropics/anthropic-cookbook/tree/main/capabilities/classification): Explore techniques for text and data classification using Claude.
- [Retrieval Augmented Generation](https://github.com/anthropics/anthropic-cookbook/tree/main/capabilities/retrieval_augmented_generation): Learn how to enhance Claude's responses with external knowledge.
- [Summarization](https://github.com/anthropics/anthropic-cookbook/tree/main/capabilities/summarization): Discover techniques for effective text summarization with Claude.

### Tool Use and Integration
- [Tool use](https://github.com/anthropics/anthropic-cookbook/tree/main/tool_use): Learn how to integrate Claude with external tools and functions to extend its capabilities.
  - [Customer service agent](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/customer_service_agent.ipynb)
  - [Calculator integration](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/calculator_tool.ipynb)
  - [SQL queries](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/how_to_make_sql_queries.ipynb)

### Third-Party Integrations
- [Retrieval augmented generation](https://github.com/anthropics/anthropic-cookbook/tree/main/third_party): Supplement Claude's knowledge with external data sources.
  - [Vector databases (Pinecone)](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/Pinecone/rag_using_pinecone.ipynb)
  - [Wikipedia](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/Wikipedia/wikipedia-search-cookbook.ipynb/)
  - [Web pages](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/read_web_pages_with_haiku.ipynb)
- [Embeddings with Voyage AI](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/VoyageAI/how_to_create_embeddings.md)

### Multimodal Capabilities
- [Vision with Claude](https://github.com/anthropics/anthropic-cookbook/tree/main/multimodal): 
  - [Getting started with images](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/getting_started_with_vision.ipynb)
  - [Best practices for vision](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/best_practices_for_vision.ipynb)
  - [Interpreting charts and graphs](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/reading_charts_graphs_powerpoints.ipynb)
  - [Extracting content from forms](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/how_to_transcribe_text.ipynb)
- [Generate images with Claude](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/illustrated_responses.ipynb): Use Claude with Stable Diffusion for image generation.

### Advanced Techniques
- [Sub-agents](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/using_sub_agents.ipynb): Learn how to use Haiku as a sub-agent in combination with Opus.
- [Upload PDFs to Claude](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/pdf_upload_summarization.ipynb): Parse and pass PDFs as text to Claude.
- [Automated evaluations](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb): Use Claude to automate the prompt evaluation process.
- [Enable JSON mode](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/how_to_enable_json_mode.ipynb): Ensure consistent JSON output from Claude.
- [Create a moderation filter](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_moderation_filter.ipynb): Use Claude to create a content moderation filter for your application.
- [Prompt caching](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/prompt_caching.ipynb): Learn techniques for efficient prompt caching with Claude.

## Additional Resources

- [Anthropic on AWS](https://github.com/aws-samples/anthropic-on-aws): Explore examples and solutions for using Claude on AWS infrastructure.
- [AWS Samples](https://github.com/aws-samples/): A collection of code samples from AWS which can be adapted for use with Claude. Note that some samples may require modification to work optimally with Claude.

```

### File: capabilities\README.md
```md
# Claude Capabilities

Welcome to the Capabilities section of the Claude Cookbooks! This directory contains a collection of guides that showcase specific capabilities where Claude excels. Each guide provides an in-depth exploration of a particular capability, discussing potential use cases, prompt engineering techniques to optimize results, and approaches for evaluating Claude's performance.

## Guides

- **[Classification with Claude](./classification/guide.ipynb)**: Discover how Claude can revolutionize classification tasks, especially in scenarios with complex business rules and limited training data. This guide walks you through data preparation, prompt engineering with retrieval-augmented generation (RAG), testing, and evaluation.

- **[Retrieval Augmented Generation with Claude](./retrieval_augmented_generation/guide.ipynb)**: Learn how to enhance Claude's capabilities with domain-specific knowledge using RAG. This guide demonstrates how to build a RAG system from scratch, optimize its performance, and create an evaluation suite. You'll learn how techniques like summary indexing and re-ranking can significantly improve precision, recall, and overall accuracy in question-answering tasks.

- **[Retrieval Augmented Generation with Contextual Embeddings](./contextual-embeddings/guide.ipynb)**: Learn how to use a new technique to improve the performance of your RAG system. In traditional RAG, documents are typically split into smaller chunks for efficient retrieval. While this approach works well for many applications, it can lead to problems when individual chunks lack sufficient context. Contextual Embeddings solve this problem by adding relevant context to each chunk before embedding. You'll learn how to use contextual embeddings with semantic search, BM25 search, and reranking to improve performance.

- **[Summarization with Claude](./summarization/guide.ipynb)**: Explore Claude's ability to summarize and synthesize information from multiple sources. This guide covers a variety of summarization techniques, including multi-shot, domain-based, and chunking methods, as well as strategies for handling long-form content and multiple documents. We also explore evaluating summaries, which can be a balance of art, subjectivity, and the right approach!

- **[Text-to-SQL with Claude](./text_to_sql/guide.ipynb)**: This guide covers how to generate complex SQL queries from natural language using prompting techniques, self-improvement, and RAG. We'll also explore how to evaluate and improve the accuracy of generated SQL queries, with evals that test for syntax, data correctness, row count, and more.

- **[Knowledge Graph Construction with Claude](./knowledge_graph/guide.ipynb)**: Build a knowledge graph from unstructured text end-to-end — named entity recognition, relation extraction, entity resolution, and multi-hop querying — using structured outputs for schema-validated extraction and Claude-driven deduplication in place of string-similarity heuristics.

## Getting Started

To get started with these guides, simply navigate to the desired guide's directory and follow the instructions provided in the `guide.ipynb` file. Each guide is self-contained and includes all the necessary code, data, and evaluation scripts to reproduce the examples and experiments.

```

### File: claude_agent_sdk\README.md
```md
# Building Powerful Agents with the Claude Agent SDK

A tutorial series demonstrating how to build sophisticated general-purpose agentic systems using the [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python), progressing from simple research agents to multi-agent orchestration with external system integration.

## Getting Started

#### 1. Install uv, [node](https://nodejs.org/en/download/), and the Claude Code CLI (if you haven't already)

```curl -LsSf https://astral.sh/uv/install.sh | sh ```

```npm install -g @anthropic-ai/claude-code```

#### 2. Clone and set up the project

```git clone https://github.com/anthropics/anthropic-cookbook.git ```

```cd anthropic-cookbook/claude_agent_sdk```

```uv sync ```

#### 3. Register venv as Jupyter kernel so that you can use it in the notebooks

```uv run python -m ipykernel install --user --name="cc-sdk-tutorial" --display-name "Python (cc-sdk-tutorial)" ```

#### 4. Claude API Key
1. Visit [platform.claude.ai](https://platform.claude.ai/dashboard)
2. Sign up or log in to your account
3. Click on "Get API keys"
4. Copy the key and paste it into your `.env` file as ```ANTHROPIC_API_KEY=```

#### 5. GitHub Token for Notebook 02
If you plan to work through the Observability Agent notebook:
1. Get a GitHub Personal Access Token [here](https://github.com/settings/personal-access-tokens/new)
2. Select "Fine-grained" token with default options (public repos, no account permissions)
3. Add it to your `.env` file as `GITHUB_TOKEN="<token>"`
4. Ensure [Docker](https://www.docker.com/products/docker-desktop/) is running on your machine

## Tutorial Series Overview

This tutorial series takes you on a journey from basic agent implementation to sophisticated multi-agent systems capable of handling real-world complexity. Each notebook builds upon the previous one, introducing new concepts and capabilities while maintaining practical, production-ready implementations.

### What You'll Learn

Through this series, you'll be exposed to:
- **Core SDK fundamentals** with `query()` and the `ClaudeSDKClient` & `ClaudeAgentOptions` interfaces in the Python SDK
- **Tool usage patterns** from basic WebSearch to complex MCP server integration
- **Multi-agent orchestration** with specialized subagents and coordination
- **Enterprise features** by leveraging hooks for compliance tracking and audit trails
- **External system integration** via Model Context Protocol (MCP)

Note: This tutorial assumes you have some level of familiarity with Claude Code. Ideally, if you have been using Claude Code to supercharge your coding tasks and would like to leverage its raw agentic power for tasks beyond Software Engineering, this tutorial will help you get started.

## Notebook Structure & Content

### [Notebook 00: The One-Liner Research Agent](00_The_one_liner_research_agent.ipynb)

Start your journey with a simple yet powerful research agent built in just a few lines of code. This notebook introduces core SDK concepts and demonstrates how the Claude Agent SDK enables autonomous information gathering and synthesis.

**Key Concepts:**
- Basic agent loops with `query()` and async iteration
- WebSearch tool for autonomous research
- Multimodal capabilities with the Read tool
- Conversation context management with `ClaudeSDKClient`
- System prompts for agent specialization

### [Notebook 01: The Chief of Staff Agent](01_The_chief_of_staff_agent.ipynb)

Build a comprehensive AI Chief of Staff for a startup CEO, showcasing advanced SDK features for production environments. This notebook demonstrates how to create sophisticated agent architectures with governance, compliance, and specialized expertise.

**Key Features Explored:**
- **Memory & Context:** Persistent instructions with CLAUDE.md files
- **Output Styles:** Tailored communication for different audiences
- **Plan Mode:** Strategic planning without execution for complex tasks
- **Custom Slash Commands:** User-friendly shortcuts for common operations
- **Hooks:** Automated compliance tracking and audit trails
- **Subagent Orchestration:** Coordinating specialized agents for domain expertise
- **Bash Tool Integration:** Python script execution for procedural knowledge and complex computations

### [Notebook 02: The Observability Agent](02_The_observability_agent.ipynb)

Expand beyond local capabilities by connecting agents to external systems through the Model Context Protocol. Transform your agent from a passive observer into an active participant in DevOps workflows.

**Advanced Capabilities:**
- **Git MCP Server:** 13+ tools for repository analysis and version control
- **GitHub MCP Server:** 100+ tools for complete GitHub platform integration
- **Real-time Monitoring:** CI/CD pipeline analysis and failure detection
- **Intelligent Incident Response:** Automated root cause analysis
- **Production Workflow Automation:** From monitoring to actionable insights

### [Notebook 03: The Site Reliability Agent](03_The_site_reliability_agent.ipynb)

Move from read-only observation to read-write remediation. Build an SRE incident response agent that can investigate production incidents, diagnose root causes, apply fixes, and document the results — all autonomously.

**Key Capabilities:**
- **MCP Tool Server:** 12+ tools for metrics, infrastructure, diagnostics, and documentation via JSON-RPC subprocess
- **Prometheus Integration:** PromQL queries for error rates, latency, and DB connection monitoring
- **Read-Write Remediation:** Edit configuration files, restart Docker services, and verify fixes
- **Safety Hooks:** PreToolUse hooks that validate write operations (pool size ranges, config sanity checks)
- **End-to-End Incident Lifecycle:** From detection through remediation to post-mortem documentation
- **Production Extensions:** Optional PagerDuty and Confluence integrations via conditional MCP tool registration

## Complete Agent Implementations

Each notebook includes an agent implementation in its respective directory:
- **`research_agent/`** - Autonomous research agent with web search and multimodal analysis
- **`chief_of_staff_agent/`** - Multi-agent executive assistant with financial modeling and compliance
- **`observability_agent/`** - DevOps monitoring agent with GitHub integration
- **`site_reliability_agent/`** - SRE incident response agent with Prometheus, Docker, and MCP tool server

**Running standalone agents:** To import agent modules outside of notebooks, either run from the `claude_agent_sdk/` directory or install the package in editable mode:
```bash
uv pip install -e .
```

## Background
### The Evolution of Claude Agent SDK

Claude Code has emerged as one of Anthropic's most successful products, but not just for its SOTA coding capabilities. Its true breakthrough lies in something more fundamental: **Claude is exceptionally good at agentic work**.

What makes Claude Code special isn't just code understanding; it's the ability to:
- Break down complex tasks into manageable steps autonomously
- Use tools effectively and make intelligent decisions about which tools to use and when
- Maintain context and memory across long-running tasks
- Recover gracefully from errors and adapt approaches when needed
- Know when to ask for clarification versus when to proceed with reasonable assumptions

These capabilities have made Claude Code the closest thing to a "bare metal" harness for Claude's raw agentic power: a minimal yet complete and sophisticated interface that lets the model's capabilities shine with the least possible overhead.

### Beyond Coding: The Agent Builder's Toolkit

Originally an internal tool built by Anthropic engineers to accelerate development workflows, the SDK's public release revealed unexpected potential. After the release of the Claude Agent SDK and its GitHub integration, developers began using it for tasks far beyond coding:

- **Research agents** that gather and synthesize information across multiple sources
- **Data analysis agents** that explore datasets and generate insights
- **Workflow automation agents** that handle repetitive business processes
- **Monitoring and observability agents** that watch systems and respond to issues
- **Content generation agents** that create and refine various types of content

The pattern was clear: the SDK had inadvertently become an effective agent-building framework. Its architecture, designed to handle software development complexity, proved remarkably well-suited for general-purpose agent creation.

This tutorial series demonstrates how to leverage the Claude Agent SDK to build highly efficient agents for any domain or use case, from simple automation to complex enterprise systems. 

## Contributing

Found an issue or have a suggestion? Please open an issue or submit a pull request!

```

### File: skills\README.md
```md
# Claude Skills Cookbook 🚀

A comprehensive guide to using Claude's Skills feature for document generation, data analysis, and business automation. This cookbook demonstrates how to leverage Claude's built-in skills for Excel, PowerPoint, and PDF creation, as well as how to build custom skills for specialized workflows.

> **🎯 See Skills in Action:** Check out **[Claude Creates Files](https://www.anthropic.com/news/create-files)** to see how these Skills power Claude's ability to create and edit documents directly in Claude.ai and the desktop app!

## What are Skills?

Skills are organized packages of instructions, executable code, and resources that give Claude specialized capabilities for specific tasks. Think of them as "expertise packages" that Claude can discover and load dynamically to:

- Create professional documents (Excel, PowerPoint, PDF, Word)
- Perform complex data analysis and visualization
- Apply company-specific workflows and branding
- Automate business processes with domain expertise

📖 Read our engineering blog post on [Equipping agents for the real world with Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

## Key Features

- ✨ **Progressive Disclosure Architecture** - Skills load only when needed, optimizing token usage
- 📊 **Financial Focus** - Real-world examples for finance and business analytics
- 🔧 **Custom Skills Development** - Learn to build and deploy your own skills
- 🎯 **Production-Ready Examples** - Code you can adapt for immediate use

## Cookbook Structure

### 📚 [Notebook 1: Introduction to Skills](notebooks/01_skills_introduction.ipynb)

Learn the fundamentals of Claude's Skills feature with quick-start examples.

- Understanding Skills architecture
- Setting up the API with beta headers
- Creating your first Excel spreadsheet
- Generating PowerPoint presentations
- Exporting to PDF format

### 💼 [Notebook 2: Financial Applications](notebooks/02_skills_financial_applications.ipynb)

Explore powerful business use cases with real financial data.

- Building financial dashboards with charts and pivot tables
- Portfolio analysis and investment reporting
- Cross-format workflows: CSV → Excel → PowerPoint → PDF
- Token optimization strategies

### 🔧 [Notebook 3: Custom Skills Development](notebooks/03_skills_custom_development.ipynb)

Master the art of creating your own specialized skills.

- Building a financial ratio calculator
- Creating company brand guidelines skill
- Advanced: Financial modeling suite
- [Best practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices) and security considerations

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Anthropic API key ([get one here](https://console.anthropic.com/))
- Jupyter Notebook or JupyterLab

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/anthropics/claude-cookbooks.git
cd claude-cookbooks/skills
```

2. **Create virtual environment** (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure API key**

```bash
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

5. **Launch Jupyter**

```bash
jupyter notebook
```

6. **Start with Notebook 1**
   Open `notebooks/01_skills_introduction.ipynb` and follow along!

## Sample Data

The cookbook includes realistic financial datasets in `sample_data/`:

- 📊 **financial_statements.csv** - Quarterly P&L, balance sheet, and cash flow data
- 💰 **portfolio_holdings.json** - Investment portfolio with performance metrics
- 📋 **budget_template.csv** - Department budget with variance analysis
- 📈 **quarterly_metrics.json** - KPIs and operational metrics

## Project Structure

```
skills/
├── notebooks/                    # Jupyter notebooks
│   ├── 01_skills_introduction.ipynb
│   ├── 02_skills_financial_applications.ipynb
│   └── 03_skills_custom_development.ipynb
├── sample_data/                  # Financial datasets
│   ├── financial_statements.csv
│   ├── portfolio_holdings.json
│   ├── budget_template.csv
│   └── quarterly_metrics.json
├── custom_skills/                # Your custom skills
│   ├── financial_analyzer/
│   ├── brand_guidelines/
│   └── report_generator/
├── outputs/                      # Generated files
├── docs/                         # Documentation
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
└── README.md                    # This file
```

## API Configuration

Skills require specific beta headers. The notebooks handle this automatically, but here's what's happening behind the scenes:

```python
from anthropic import Anthropic

client = Anthropic(
    api_key="your-api-key",
    default_headers={
        "anthropic-beta": "code-execution-2025-08-25,files-api-2025-04-14,skills-2025-10-02"
    }
)
```

**Required Beta Headers:**

- `code-execution-2025-08-25` - Enables code execution for Skills
- `files-api-2025-04-14` - Required for downloading generated files
- `skills-2025-10-02` - Enables Skills feature

## Working with Generated Files

When Skills create documents (Excel, PowerPoint, PDF, etc.), they return `file_id` attributes in the response. You must use the **Files API** to download these files.

### How It Works

1. **Skills create files** during code execution
2. **Response includes file_ids** for each created file
3. **Use Files API** to download the actual file content
4. **Save locally** or process as needed

### Example: Creating and Downloading an Excel File

```python
from anthropic import Anthropic

client = Anthropic(api_key="your-api-key")

# Step 1: Use a skill to create a file
response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "xlsx", "version": "latest"}
        ]
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{
        "role": "user",
        "content": "Create an Excel file with a simple budget spreadsheet"
    }]
)

# Step 2: Extract file_id from the response
file_id = None
for block in response.content:
    if block.type == "tool_result" and hasattr(block, 'output'):
        # Look for file_id in the tool output
        if 'file_id' in str(block.output):
            file_id = extract_file_id(block.output)  # Parse the file_id
            break

# Step 3: Download the file using Files API
if file_id:
    file_content = client.beta.files.download(file_id=file_id)

    # Step 4: Save to disk
    with open("outputs/budget.xlsx", "wb") as f:
        f.write(file_content.read())

    print(f"✅ File downloaded: budget.xlsx")
```

### Files API Methods

```python
# Download file content (binary)
content = client.beta.files.download(file_id="file_abc123...")
with open("output.xlsx", "wb") as f:
    f.write(content.read())  # Use .read() not .content

# Get file metadata
info = client.beta.files.retrieve_metadata(file_id="file_abc123...")
print(f"Filename: {info.filename}, Size: {info.size_bytes} bytes")  # Use size_bytes not size

# List all files
files = client.beta.files.list()
for file in files.data:
    print(f"{file.filename} - {file.created_at}")

# Delete a file
client.beta.files.delete(file_id="file_abc123...")
```

**Important Notes:**

- Files are stored temporarily on Anthropic's servers
- Downloaded files should be saved to your local `outputs/` directory
- The Files API uses the same API key as the Messages API
- All notebooks include helper functions for file download
- **Files are overwritten by default** - rerunning cells will replace existing files (you'll see `[overwritten]` in the output)

See the [Files API documentation](https://docs.claude.com/en/api/files-content) for complete details.

## Built-in Skills Reference

Claude comes with these pre-built skills:

| Skill      | ID     | Description                                                                 |
| ---------- | ------ | --------------------------------------------------------------------------- |
| Excel      | `xlsx` | Create and manipulate Excel workbooks with formulas, charts, and formatting |
| PowerPoint | `pptx` | Generate professional presentations with slides, charts, and transitions    |
| PDF        | `pdf`  | Create formatted PDF documents with text, tables, and images                |
| Word       | `docx` | Generate Word documents with rich formatting and structure                  |

## Creating Custom Skills

Custom skills follow this structure:

```
my_skill/
├── SKILL.md           # Required: Instructions for Claude
├── scripts/           # Optional: Python/JS code
│   └── processor.py
└── resources/         # Optional: Templates, data
    └── template.xlsx
```

Learn more in [Notebook 3](notebooks/03_skills_custom_development.ipynb).

## Common Use Cases

### Financial Reporting

- Automated quarterly reports
- Budget variance analysis
- Investment performance dashboards

### Data Analysis

- Excel-based analytics with complex formulas
- Pivot table generation
- Statistical analysis and visualization

### Document Automation

- Branded presentation generation
- Report compilation from multiple sources
- Cross-format document conversion

## Performance Tips

1. **Use Progressive Disclosure**: Skills load in stages to minimize token usage
2. **Batch Operations**: Process multiple files in a single conversation
3. **Skill Composition**: Combine multiple skills for complex workflows
4. **Cache Reuse**: Use container IDs to reuse loaded skills

## Troubleshooting

### Common Issues

**API Key Not Found**

```
ValueError: ANTHROPIC_API_KEY not found
```

→ Make sure you've copied `.env.example` to `.env` and added your key

**Skills Beta Header Missing**

```
Error: Skills feature requires beta header
```

→ Ensure you're using the correct beta headers as shown in the notebooks

**Token Limit Exceeded**

```
Error: Request exceeds token limit
```

→ Break large operations into smaller chunks or use progressive disclosure

## Resources

### Documentation

- 📖 [Claude API Documentation](https://docs.anthropic.com/en/api/messages)
- 🔧 [Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)

### Support Articles

- 📚 [Teach Claude your way of working using Skills](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills) - User guide for working with Skills
- 🛠️ [How to create a skill with Claude through conversation](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation) - Interactive skill creation guide

### Community & Support

- 💬 [Claude Support](https://support.claude.com)
- 🐙 [GitHub Issues](https://github.com/anthropics/claude-cookbooks/issues)

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

## License

This cookbook is provided under the MIT License. See [LICENSE](../LICENSE) for details.

## Acknowledgments

Special thanks to the Anthropic team for developing the Skills feature and providing the SDK.

---

**Questions?** Check the [FAQ](docs/FAQ.md) or open an issue.

**Ready to start?** Open [Notebook 1](notebooks/01_skills_introduction.ipynb) and let's build something amazing! 🎉

```

### File: skills\requirements.txt
```txt
# Claude Skills Cookbook Requirements
# Install with: pip install -r requirements.txt

# Core dependencies
anthropic>=0.71.0                         # Anthropic SDK with Skills support
python-dotenv>=1.0.0                      # Environment variable management
ipykernel>=6.25.0                         # Jupyter kernel for notebooks
jupyter>=1.0.0                            # Jupyter notebook support

# Data manipulation and analysis
pandas>=2.0.0                             # Data analysis and manipulation
numpy>=1.24.0                             # Numerical computing
openpyxl>=3.1.0                           # Excel file reading/writing

# Visualization (for financial charts in notebooks)
matplotlib>=3.7.0                         # Basic plotting
plotly>=5.14.0                           # Interactive visualizations

# Utilities
requests>=2.31.0                          # HTTP requests for examples
tqdm>=4.65.0                             # Progress bars for long operations
tabulate>=0.9.0                          # Pretty-print tables in notebooks

# Development tools (optional but recommended)
ipywidgets>=8.0.0                        # Interactive widgets for notebooks
nbformat>=5.9.0                          # Notebook format validation
```

### File: tool_use\requirements.txt
```txt
anthropic>=0.18.0
python-dotenv>=1.0.0
ipykernel>=6.29.0  # For Jupyter in VSCode
rich>=13.0.0
pandas>=2.0.0
```

### File: capabilities\classification\README.md
```md
# Classification with Claude

Learn how to use Claude for classification tasks, especially in scenarios with complex business rules and limited training data.

## Contents

- `guide.ipynb`: Main tutorial notebook
- `data/`: Data files for examples and testing
- `evaluation/`: Evaluation scripts using Promptfoo

For evaluation instructions, see `evaluation/README.md`.

```

### File: capabilities\contextual-embeddings\README.md
```md
# Retrieval Augmented Generation with Contextual Embeddings

Learn how to improve RAG performance using contextual embeddings to add relevant context to each chunk before embedding.

## Contents

- `guide.ipynb`: Main tutorial notebook
- `data/`: Data files for examples and testing
- `evaluation/`: Evaluation scripts using Promptfoo

For evaluation instructions, see `evaluation/README.md`.

```

### File: capabilities\knowledge_graph\README.md
```md
# Knowledge Graph Construction with Claude

Learn how to build knowledge graphs from unstructured text using Claude for the classical KG construction tasks: named entity recognition, relation extraction, entity resolution, and entity summarization.

## Contents

- `guide.ipynb`: Main tutorial notebook
- `data/`: Gold-standard triples for evaluation
- `evaluation/`: Precision/recall scoring scripts

For evaluation instructions, see `evaluation/README.md`.

```

### File: capabilities\retrieval_augmented_generation\README.md
```md
# Retrieval Augmented Generation with Claude

Learn how to enhance Claude's capabilities with domain-specific knowledge using Retrieval Augmented Generation (RAG).

## Contents

- `guide.ipynb`: Main tutorial notebook
- `data/`: Data files for examples and testing
- `evaluation/`: Evaluation scripts using Promptfoo

For evaluation instructions, see `evaluation/README.md`.

```

### File: capabilities\summarization\README.md
```md
# Summarization with Claude

Explore Claude's ability to summarize and synthesize information from multiple sources using various techniques.

## Contents

- `guide.ipynb`: Main tutorial notebook
- `data/`: Data files for examples and testing
- `evaluation/`: Evaluation scripts using Promptfoo

For evaluation instructions, see `evaluation/README.md`.

```

### File: capabilities\text_to_sql\README.md
```md
# Text-to-SQL with Claude

Learn how to generate complex SQL queries from natural language using prompting techniques, self-improvement, and RAG.

## Contents

- `guide.ipynb`: Main tutorial notebook
- `data/`: Data files for examples and testing
- `evaluation/`: Evaluation scripts using Promptfoo

For evaluation instructions, see `evaluation/README.md`.

```

### File: patterns\agents\README.md
```md
# Building Effective Agents Cookbook

Reference implementation for [Building Effective Agents](https://anthropic.com/research/building-effective-agents) by Erik Schluntz and Barry Zhang.

This repository contains example minimal implementations of common agent workflows discussed in the blog:

- Basic Building Blocks
  - Prompt Chaining
  - Routing
  - Multi-LLM Parallelization
- Advanced Workflows
  - Orchestrator-Subagents
  - Evaluator-Optimizer

## Getting Started
See the Jupyter notebooks for detailed examples:

- [Basic Workflows](basic_workflows.ipynb)
- [Evaluator-Optimizer Workflow](evaluator_optimizer.ipynb) 
- [Orchestrator-Workers Workflow](orchestrator_workers.ipynb)
```

### File: third_party\Deepgram\README.md
```md
# Deepgram <> Claude Cookbooks

[Deepgram](https://deepgram.com/) is a foundational AI company providing the speech-to-text, text-to-speech, text-to-text and language intelligence capabilities you need to make your data readable and actionable by human or machines.

* The [Pre-Recorded Audio Notebook](./prerecorded_audio.ipynb) allows you to transcribe pre-recorded audio using Deepgram.

# More about Deepgram

Here are some of our favorite resources for getting started:
- [API Playground](https://playground.deepgram.com/)
- [Starter Apps](https://github.com/deepgram-starters)
- [Python SDK](https://github.com/deepgram/deepgram-python-sdk)
- [Node SDK](https://github.com/deepgram/deepgram-node-sdk)
- [.NET SDK](https://github.com/deepgram/deepgram-dotnet-sdk)
- [Go SDK](https://github.com/deepgram/deepgram-go-sdk)
- [Documentation](https://developers.deepgram.com/documentation/)
- [Blog posts](https://deepgram.com/learn)

 # Our Community

Do you have a question, comment, or want to connect? Head over to our [Github Discussions](https://github.com/orgs/deepgram/discussions) or join us on [Discord](https://discord.com/invite/xWRaCDBtW4).


# Get Started

If you're ready to get started using Deepgram, head over to the [Deepgram Console](https://console.deepgram.com/signup) to get your free API key and free credits and start building with our powerful speech, text and intelligence [APIs](https://developers.deepgram.com/reference/).


```

### File: third_party\ElevenLabs\README.md
```md
# ElevenLabs <> Claude Cookbooks

[ElevenLabs](https://elevenlabs.io/) provides AI-powered speech-to-text and text-to-speech APIs for creating natural-sounding voice applications with advanced features like voice cloning and streaming synthesis.

This cookbook demonstrates how to build a low-latency voice assistant by combining ElevenLabs' speech processing with Claude's intelligent responses, progressively optimizing for real-time performance.

## What's Included

* **[Low Latency Voice Assistant Notebook](./low_latency_stt_claude_tts.ipynb)** - An interactive tutorial that walks you through building a voice assistant step-by-step, demonstrating various optimization techniques to minimize latency through streaming.

* **[WebSocket Streaming Script](./stream_voice_assistant_websocket.py)** - A production-ready conversational voice assistant featuring continuous microphone input, gapless audio playback, and the lowest possible latency using WebSocket streaming.

## How to Use This Cookbook

We recommend following this sequence to get the most out of this cookbook:

### Step 1: Set Up Your Environment

1. **Create a virtual environment:**
   ```bash
   # Navigate to the ElevenLabs directory
   cd /path/to/claude-cookbooks/third_party/ElevenLabs

   # Create virtual environment
   python -m venv venv

   # Activate it
   source venv/bin/activate  # On macOS/Linux
   # OR
   venv\Scripts\activate     # On Windows
   ```

2. **Get your API keys:**
   - **ElevenLabs API key:** [elevenlabs.io/app/developers/api-keys](https://elevenlabs.io/app/developers/api-keys)

     When creating your API key, ensure it has the following minimum permissions:
     - Text to speech
     - Speech to text
     - Read access on voices
     - Read access on models

   - **Anthropic API key:** [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)

3. **Configure your environment:**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` and add your API keys:
   ```
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ANTHROPIC_API_KEY=sk-ant-api03-...
   ```

4. **Install dependencies:**
   ```bash
   # With venv activated
   pip install -r requirements.txt
   ```

### Step 2: Work Through the Notebook

Start with the **[Low Latency Voice Assistant Notebook](./low_latency_stt_claude_tts.ipynb)**. This interactive guide will teach you:

- How to use ElevenLabs for speech-to-text transcription
- How to generate Claude responses and measure latency
- How streaming reduces time-to-first-token
- How to stream text-to-speech for faster audio playback
- The tradeoffs between different streaming approaches
- Why WebSocket streaming provides the best balance of latency and quality

The notebook includes performance metrics and comparisons at each step, helping you understand the impact of each optimization.

### Step 3: Try the Production Script

After understanding the concepts from the notebook, run the **[WebSocket Streaming Script](./stream_voice_assistant_websocket.py)** to experience a fully functional voice assistant:

```bash
python stream_voice_assistant_websocket.py
```

**How it works:**
1. Press Enter to start recording
2. Speak your question into the microphone
3. Press Enter to stop recording
4. The assistant will respond with natural speech
5. Repeat or press Ctrl+C to exit

The script demonstrates production-ready implementations of:
- Real-time microphone recording with sounddevice
- Continuous conversation with context retention
- WebSocket-based streaming for minimal latency
- Custom audio queue for seamless playback

## Troubleshooting

### Audio Popping or Crackling

**Symptom:** You may occasionally hear brief pops, clicks, or audio dropouts during playback.

**Explanation:**

This occurs because the script uses MP3 format audio, which is required for the ElevenLabs free tier. When streaming MP3 data in real-time chunks, FFmpeg occasionally receives incomplete frames that cannot be decoded. This typically happens:
- At the start of streaming (first chunk may be too small)
- During brief network delays
- At the end of audio generation (final chunk may be partial)

The script automatically handles these failed chunks by skipping them (using a try-except pattern in the audio decoding logic), which prevents errors from appearing in the console but may result in brief audio gaps that manifest as pops or clicks.

**Impact:**
- Audio playback continues normally
- Brief pops or clicks are usually imperceptible or minor
- The WebSocket connection remains stable
- No functionality is lost

**Solution:**

This is expected behavior when using MP3 format on the free tier. If you want to eliminate audio popping entirely:
1. Upgrade to a paid ElevenLabs tier
2. Modify the script to use `pcm_44100` format instead of MP3
3. PCM format provides cleaner streaming without decoding issues

### API Key Issues

**Symptom:** `AssertionError: ELEVENLABS_API_KEY is not set` or `AssertionError: ANTHROPIC_API_KEY is not set`

**Solution:**
1. Verify you've copied `.env.example` to `.env`: `cp .env.example .env`
2. Edit `.env` and ensure both API keys are set correctly
3. Check for typos or extra spaces in your API keys
4. Confirm your ElevenLabs key has the required permissions (see Step 1)

### Dependency Issues

**Symptom:** Errors like `ImportError: PortAudio library not found` or audio playback failures

**Solution:**

**macOS:**
```bash
brew install portaudio ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt-get install portaudio19-dev ffmpeg
```

**Windows:**
- Install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
- Add FFmpeg to your system PATH
- PortAudio typically installs automatically with sounddevice on Windows

Then reinstall Python dependencies:
```bash
pip install -r requirements.txt
```

### Microphone Permissions

**Symptom:** `OSError: [Errno -9999] Unanticipated host error` or microphone not accessible

**Solution:**
- **macOS:** Go to System Preferences → Security & Privacy → Privacy → Microphone, and enable Terminal (or your Python IDE)
- **Windows:** Go to Settings → Privacy → Microphone, and enable microphone access for Python/Terminal
- **Linux:** Check your user is in the `audio` group: `sudo usermod -a -G audio $USER` (then log out and back in)

Test your microphone setup:
```bash
python -c "import sounddevice as sd; print(sd.query_devices())"
```

### WebSocket Connection Failures

**Symptom:** Connection errors, timeouts, or stream interruptions

**Solution:**
1. Check your internet connection is stable
2. Verify firewall isn't blocking WebSocket connections (port 443)
3. Try disabling VPN or proxy temporarily
4. Ensure you're not exceeding API rate limits (see ElevenLabs dashboard for usage)

If you continue to experience issues, check [ElevenLabs Status](https://status.elevenlabs.io/) for service updates.

## Project Ideas

Once you're comfortable with the voice assistant, here are some inspiring projects you can build:

- **Meeting Note-Taker** - Record and transcribe meetings in real-time, then use Claude to generate summaries, action items, and key takeaways from the conversation.

- **Language Learning Tutor** - Practice conversations in any language with real-time feedback. Claude can correct pronunciation, suggest better phrasing, and adapt difficulty to your skill level.

- **Interactive Storyteller** - Create choose-your-own-adventure games where Claude narrates the story and responds to your spoken choices, with different voice characters for each role.

- **Hands-Free Coding Assistant** - Describe code changes, bugs, or features verbally while keeping your hands on the keyboard. Perfect for rubber duck debugging or pair programming solo.

- **Voice-Activated Smart Home** - Build natural conversation interfaces for controlling home devices. Ask complex questions like "Is it cold enough to turn on the heater?" instead of simple on/off commands.

- **Personal Voice Journal** - Keep a daily journal by speaking your thoughts. Claude can organize entries by theme, track your mood over time, and surface relevant past entries when you need them.

## More About ElevenLabs

Here are some helpful resources to deepen your understanding:

- [ElevenLabs Platform](https://elevenlabs.io/) - Official website
- [API Documentation](https://elevenlabs.io/docs/overview) - Complete API reference
- [Voice Library](https://elevenlabs.io/voice-library) - Explore available voices
- [API Playground](https://elevenlabs.io/app/speech-synthesis/text-to-speech) - Test voices interactively
- [Python SDK](https://github.com/elevenlabs/elevenlabs-python) - Official Python SDK
```

### File: third_party\ElevenLabs\requirements.txt
```txt
anthropic>=0.71.0
elevenlabs>=2.15.0
sounddevice>=0.5.1
numpy>=1.26.0
scipy>=1.16.2
websocket-client>=1.8.0
python-dotenv>=1.0.0
pydub>=0.25.1

```

### File: third_party\LlamaIndex\README.md
```md
# LlamaIndex <> Claude Cookbooks

[LlamaIndex](https://github.com/run-llama/llama_index) is a data framework for LLM-based applications that benefit from context augmentation.

Here we provide cookbooks for building LLM applications using Anthropic and LlamaIndex.

1. `Basic_RAG_With_LlamaIndex.ipynb` - Notebook to help you build RAG pipelines with LlamaIndex.
2. `Router_Query_Engine.ipynb` - Notebook to help you use `RouterQueryEngine` to route user queries to different indices.
3. `SubQuestion_Query_Engine` - Notebook to help you to use `SubQuestionQueryEngine` to answer complex user queries spanning multiple documents.
4. `ReAct_Agent.ipynb` - Notebook to help you to use `ReActAgent` for using Tools and QueryEngine Tools.
5.  `Multi_Document_Agents.ipynb` - Notebook to help you build an efficient RAG pipeline for a large number of documents.
6.  `Multi_Modal.ipynb` - Notebook to help you build Multi-Modal applications using LlamaIndex.

[Documentation](https://docs.llamaindex.ai/en/stable/)
[Discord](https://discord.gg/dGcwcsnxhU)
[Twitter](https://twitter.com/llama_index)
[Linkedin](https://www.linkedin.com/company/llamaindex/)
```

### File: capabilities\classification\evaluation\README.md
```md
# Evaluations with Promptfoo



### Pre-requisities 
To use Promptfoo you will need to have node.js & npm installed on your system. For more information follow [this guide](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)  

You can install promptfoo using npm or run it directly using npx. In this guide we will use npx.  

*Note: For this example you will not need to run `npx promptfoo@latest init` there is already an initialized `promptfooconfig.yaml` file in this directory*  

See the official docs [here](https://www.promptfoo.dev/docs/getting-started)  



### Getting Started
The evaluation is orchestrated by the `promptfooconfig.yaml` file. In this file we define the following sections:

- Prompts
    - Promptfoo enables you to import prompts in many different formats. You can read more about this [here](https://www.promptfoo.dev/docs/configuration/parameters).
    - In this example we will load 3 prompts - the same used in `guide.ipynb` from the `prompts.py` file:
        - The functions are identical to those used in `guide.ipynb` except that instead of calling the Claude API they just return the prompt. Promptfoo then handles the orchestration of calling the API and storing the results.
        - You can read more about prompt functions [here](https://www.promptfoo.dev/docs/configuration/parameters#prompt-functions). Using python allows us to reuse the VectorDB class which is necessary for RAG, this is defined in `vectordb.py`.
- Providers
    - With Promptfoo you can connect to many different LLMs from different platforms, see [here for more](https://www.promptfoo.dev/docs/providers). In `guide.ipynb` we used Haiku with default temperature 0.0. We will use Promptfoo to experiment with an array of different temperature settings to identify the optimal choice for our use case.
- Tests
    - We will use the same data that was used in `guide.ipynb` which can be found in [`dataset.csv`](./dataset.csv).
    - Promptfoo has a wide array of built in tests which can be found [here](https://www.promptfoo.dev/docs/configuration/expected-outputs/deterministic).
    - In this example we will define a test in our `dataset.csv` as the conditions of our evaluation change with each row and a test in the `promptfooconfig.yaml` for conditions that are consistent across all test cases. Read more about this [here](https://www.promptfoo.dev/docs/configuration/parameters/#import-from-csv)
- Transform
    - In the `defaultTest` section we define a transform function. This is a python function which extracts the specific output we want to test from the LLM response. 
- Output
    - We define the path for the output file. Promptfoo can output results in many formats, [see here](https://www.promptfoo.dev/docs/configuration/parameters/#output-file). Alternatively you can use Promptfoo's web UI, [see here](https://www.promptfoo.dev/docs/usage/web-ui).


### Run the eval

To get started with Promptfoo open your terminal and navigate to this directory (`./evaluation`).

Before running your evaluation you must define the following environment variables:

`export ANTHROPIC_API_KEY=YOUR_API_KEY`  
`export VOYAGE_API_KEY=YOUR_API_KEY`

From the `evaluation` directory, run the following command.  

`npx promptfoo@latest eval`

If you would like to increase the concurrency of the requests (default = 4), run the following command.  

`npx promptfoo@latest eval -j 25`  

When the evaluation is complete the terminal will print the results for each row in the dataset.

You can now go back to `guide.ipynb` to analyze the results!



```

### File: capabilities\knowledge_graph\evaluation\README.md
```md
# Knowledge Graph Extraction Evaluation

Scores entity and relation extraction against the hand-labeled gold set in `../data/sample_triples.json`.

## Running

From the repository root, install dependencies and set your API key:

```bash
uv sync --all-extras
cp .env.example .env  # then edit .env to add ANTHROPIC_API_KEY
```

Then:

```bash
uv run python capabilities/knowledge_graph/evaluation/eval_extraction.py
```

## Metrics

**Entity P/R/F1** — an extracted entity counts as a true positive if its canonicalized name matches a gold entity in the same document. Canonicalization lowercases and maps known surface-form variants ("National Aeronautics and Space Administration" → "nasa") via `data/alias_map.json`.

**Relation P/R/F1** — a relation counts as a true positive if both canonicalized endpoints match a gold (source, target) pair. **Predicate wording is ignored**: "commanded" and "was commander of" both count, but so would a semantically wrong predicate like "destroyed" between the same two entities. This makes the reported relation recall an upper bound — it measures whether the extractor found the right *connections*, not whether it labeled them correctly. For stricter scoring you would add a predicate-similarity check (e.g. a Claude judge call per candidate pair).

## Expected baseline

With `claude-haiku-4-5` and the extraction prompt from the guide, expect roughly:

| Metric | P | R | F1 |
|---|---|---|---|
| Entities | 0.80–0.90 | 0.70–0.85 | 0.75–0.85 |
| Relations | 0.70–0.85 | 0.55–0.70 | 0.60–0.75 |

These ranges are indicative; actual scores vary run-to-run due to model non-determinism.

Recall on relations is the hard number — the extractor tends to be conservative, preferring fewer high-confidence edges over exhaustive coverage. Tuning the extraction prompt for higher recall (e.g. "extract every stated relationship, even minor ones") trades precision for recall.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

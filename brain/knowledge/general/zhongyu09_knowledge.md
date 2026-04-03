---
id: zhongyu09-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.896959
---

# KNOWLEDGE EXTRACT: zhongyu09
> **Extracted on:** 2026-03-30 18:01:27
> **Source:** zhongyu09

---

## File: `openchatbi.md`
```markdown
# 📦 zhongyu09/openchatbi [🔖 PENDING/APPROVE]
🔗 https://github.com/zhongyu09/openchatbi
🌐 https://zhongyu09.github.io/openchatbi/

## Meta
- **Stars:** ⭐ 536 | **Forks:** 🍴 67
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OpenChatBI is an intelligent chat-based BI tool powered by large language models, designed to help users query, analyze, and visualize data through natural language conversations. It uses LangGraph and LangChain to build chat agent and workflows that support natural language to SQL conversion and data analysis.

## README (trích đầu)
```
# OpenChatBI

OpenChatBI is an open source, chat-based intelligent BI tool powered by large language models, designed to help users 
query, analyze, and visualize data through natural language conversations. Built on LangGraph and LangChain ecosystem, 
it provides chat agents and workflows that support natural language to SQL conversion and streamlined data analysis.

Join the Slack channel to discuss: https://join.slack.com/t/openchatbicommunity/shared_invite/zt-3jpzpx9mv-Sk88RxpO4Up0L~YTZYf4GQ

<img src="https://github.com/zhongyu09/openchatbi/raw/main/example/demo.gif" alt="Demo" width="800">

## Core Features

1. **Natural Language Interaction**: Get data analysis results by asking questions in natural language
2. **Automatic SQL Generation**: Convert natural language queries into SQL statements using advanced text2sql workflows
   with schema linking and well organized prompt engineering
3. **Data Visualization**: Generate intuitive data visualizations (via plotly)
4. **Data Catalog Management**: Automatically discovers and indexes database table structures, supports flexible catalog
   storage backends with vector-based or BM25-based retrieval, and easily maintains business explanations for tables
   and columns as well as optimizes Prompts.
5. **Time Series Forecasting**: Forecasting models deployed in-house that can be called as tools
6. **Code Execution**: Execute Python code for data analysis and visualization
7. **Interactive Problem-Solving**: Proactively ask users for more context when information is incomplete
8. **Persistent Memory**: Conversation management and user characteristic memory based on LangGraph checkpointing
9. **MCP Support**: Integration with MCP tools by configuration
10. **Knowledge Base Integration**: Answer complex questions by combining catalog based knowledge retrival and external
   knowledge base retrival (via MCP tools)
11. **Web UI Interface**: Provide 2 sample UI: simple and streaming web interfaces using Gradio and Streamlit, easy to
   integrate with other web applications

## Roadmap

1. **Anomaly Detection Algorithm**: Time series anomaly detection
2. **Root Cause Analysis Algorithm**: Multi-dimensional drill-down capabilities for anomaly investigation

# Getting started

## Installation & Setup

### Prerequisites

- Python 3.11 or higher
- Access to a supported LLM provider (OpenAI, Anthropic, etc.)
- Data Warehouse (Database) credentials (like Presto, PostgreSQL, MySQL, etc.)
- (Optional) Embedding model for vector-based retrieval - if not available, BM25-based retrieval will be used
- (Optional) Docker - required only for `docker` executor mode

**Note on Chinese Text Segmentation**: For better Chinese text retrieval, `jieba` is used for word segmentation. However, `jieba` is not compatible with Python 3.12+. On Python 3.12 and higher, the system automatically falls back to simple punctuation-based segmentation for Chinese text.

### Installation

1. **Using uv (recommended):**

```bash
git clone gi
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


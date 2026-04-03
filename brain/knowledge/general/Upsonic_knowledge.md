---
id: upsonic-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:26.212654
---

# KNOWLEDGE EXTRACT: Upsonic
> **Extracted on:** 2026-03-30 17:58:06
> **Source:** Upsonic

---

## File: `Upsonic.md`
```markdown
# 📦 Upsonic/Upsonic [🔖 PENDING/APPROVE]
🔗 https://github.com/Upsonic/Upsonic
🌐 https://docs.upsonic.ai

## Meta
- **Stars:** ⭐ 7817 | **Forks:** 🍴 722
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Agent Framework For Fintech and Banks

## README (trích đầu)
```
<div align="center">

<img src="https://github.com/user-attachments/assets/fbe7219f-55bc-4748-ac4a-dd2fb2b8d9e5" width="600" />

# Upsonic

**Production-Ready AI Agent Framework with Safety First**

[![PyPI version](https://badge.fury.io/py/upsonic.svg)](https://badge.fury.io/py/upsonic)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENCE)
[![Python Version](https://img.shields.io/pypi/pyversions/upsonic.svg)](https://pypi.org/project/upsonic/)
[![GitHub stars](https://img.shields.io/github/stars/Upsonic/Upsonic.svg?style=social&label=Star)](https://github.com/Upsonic/Upsonic)
[![GitHub issues](https://img.shields.io/github/issues/Upsonic/Upsonic.svg)](https://github.com/Upsonic/Upsonic/issues)
[![Documentation](https://img.shields.io/badge/docs-upsonic.ai-brightgreen.svg)](https://docs.upsonic.ai)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/pmYDMSQHqY)

[Documentation](https://docs.upsonic.ai) • [Quickstart](https://docs.upsonic.ai/get-started/quickstart) • [Examples](https://docs.upsonic.ai/examples) • [Discord](https://discord.gg/pmYDMSQHqY)

</div>

---

## Overview

Upsonic is an open-source AI agent framework for building production-ready agents. It supports multiple AI providers (OpenAI, Anthropic, Azure, Bedrock) and includes built-in safety policies, OCR, memory, multi-agent coordination, and MCP tool integration.

## What Can You Build?

- **Document Analysis**: Extract and process text from images and PDFs
- **Customer Service Automation**: Agents with memory and session context
- **Financial Analysis**: Agents that analyze data, generate reports, and provide insights
- **Compliance Monitoring**: Enforce safety policies across all agent interactions
- **Research & Data Gathering**: Automate research workflows with multi-agent collaboration
- **Multi-Agent Workflows**: Orchestrate tasks across specialized agent teams

## Quick Start

### Installation

```bash
uv pip install upsonic
# pip install upsonic
```

### Basic Agent

```python
from upsonic import Agent, Task

agent = Agent(model="anthropic/claude-sonnet-4-5", name="Stock Analyst Agent")

task = Task(description="Analyze the current market trends")

agent.print_do(task)
```

### Agent with Tools

```python
from upsonic import Agent, Task
from upsonic.tools.common_tools import YFinanceTools

agent = Agent(model="anthropic/claude-sonnet-4-5", name="Stock Analyst Agent")

task = Task(
    description="Give me a summary about tesla stock with tesla car models",
    tools=[YFinanceTools()]
)

agent.print_do(task)
```

### Agent with Memory

```python
from upsonic import Agent, Task
from upsonic.storage import Memory, InMemoryStorage

memory = Memory(
    storage=InMemoryStorage(),
    session_id="session_001",
    full_session_memory=True
)

agent = Agent(model="anthropic/claude-sonnet-4-5", memory=memory)

task1 = Task(description="My name is John")
agent.print_do(ta
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


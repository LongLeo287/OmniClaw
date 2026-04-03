---
id: griptape-ai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:49.514237
---

# KNOWLEDGE EXTRACT: griptape-ai
> **Extracted on:** 2026-03-30 17:38:02
> **Source:** griptape-ai

---

## File: `griptape.md`
```markdown
# 📦 griptape-ai/griptape [🔖 PENDING/APPROVE]
🔗 https://github.com/griptape-ai/griptape
🌐 https://www.griptape.ai

## Meta
- **Stars:** ⭐ 2500 | **Forks:** 🍴 224
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Modular Python framework for AI agents and workflows with chain-of-thought reasoning, tools, and memory. 

## README (trích đầu)
```
![Griptape](docs/assets/img/GRIPTAPE_from_Foundry_rgb_black.svg)

[![PyPI Version](https://img.shields.io/pypi/v/griptape.svg)](https://pypi.python.org/pypi/griptape)
[![Tests](https://github.com/griptape-ai/griptape/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/griptape-ai/griptape/actions/workflows/unit-tests.yml)
[![Docs](https://readthedocs.org/projects/griptape/badge/)](https://griptape.readthedocs.io/)
[![Checked with pyright](https://microsoft.github.io/pyright/img/pyright_badge.svg)](https://microsoft.github.io/pyright/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![codecov](https://codecov.io/github/griptape-ai/griptape/graph/badge.svg?token=HUBqUpl3NB)](https://codecov.io/github/griptape-ai/griptape)
[![Griptape Discord](https://dcbadge.vercel.app/api/server/gnWRz88eym?compact=true&style=flat)](https://discord.gg/griptape)

Griptape is a Python framework designed to simplify the development of generative AI (genAI) applications.
It offers a set of straightforward, flexible abstractions for working with areas such as Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and much more.

> **Looking for a no-code experience?** Check out [Griptape Nodes](https://www.griptapenodes.com/griptape-nodes-desktop), a visual desktop application for building and running AI workflows.

## 🛠️ Core Components

### 🏗️ Structures

- 🤖 **Agents** consist of a single Task, configured for Agent-specific behavior.
- 🔄 **Pipelines** organize a sequence of Tasks so that the output from one Task may flow into the next.
- 🌐 **Workflows** configure Tasks to operate in parallel.

### 📝 Tasks

Tasks are the core building blocks within Structures, enabling interaction with Engines, Tools, and other Griptape components.

### 🧠 Memory

- 💬 **Conversation Memory** enables LLMs to retain and retrieve information across interactions.
- 🗃️ **Task Memory** keeps large or sensitive Task outputs off the prompt that is sent to the LLM.
- 📊 **Meta Memory** enables passing in additional metadata to the LLM, enhancing the context and relevance of the interaction.

### 🚗 Drivers

Drivers facilitate interactions with external resources and services in Griptape. 
They allow you to swap out functionality and providers with minimal changes to your business logic.

#### LLM & Orchestration
- 🗣️ **Prompt Drivers**: Manage textual and image interactions with LLMs.
- 🤖 **Assistant Drivers**: Enable interactions with various “assistant” services.
- 📜 **Ruleset Drivers**: Load and apply rulesets from external sources.
- 🧠 **Conversation Memory Drivers**: Store and retrieve conversational data.
- 📡 **Event Listener Drivers**: Forward framework events to external services.
- 🏗️ **Structure Run Drivers**: Execute structures locally or in the cloud.

#### Retrieval & Storage
- 🔢 **Embedding Drivers**: Generate vector embeddings from textual inputs.
-
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


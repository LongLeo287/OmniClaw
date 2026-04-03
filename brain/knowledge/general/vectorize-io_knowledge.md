---
id: vectorize-io-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:40.440825
---

# KNOWLEDGE EXTRACT: vectorize-io
> **Extracted on:** 2026-03-30 17:58:07
> **Source:** vectorize-io

---

## File: `hindsight-cookbook.md`
```markdown
# 📦 vectorize-io/hindsight-cookbook [🔖 PENDING/APPROVE]
🔗 https://github.com/vectorize-io/hindsight-cookbook


## Meta
- **Stars:** ⭐ 17 | **Forks:** 🍴 4
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Hindsight Cookbook - examples on how to use Hindsight

## README (trích đầu)
```
# Hindsight Cookbook

A collection of example applications and notebooks demonstrating how to integrate and use [Hindsight](https://github.com/vectorize-io/hindsight).

## Applications

Full-featured example applications demonstrating Hindsight integration patterns:

- **[chat-memory](./applications/chat-memory)** - Conversational AI with per-user memory
- **[crewai-memory](./applications/crewai-memory)** - CrewAI agents with persistent long-term memory
- **[pydantic-ai-memory](./applications/pydantic-ai-memory)** - Pydantic AI agent with persistent long-term memory
- **[deliveryman-demo](./applications/deliveryman-demo)** - Interactive delivery agent with memory-based navigation
- **[hindsight-litellm-demo](./applications/hindsight-litellm-demo)** - Side-by-side comparison of memory approaches
- **[hindsight-tool-learning-demo](./applications/hindsight-tool-learning-demo)** - Learning tool selection through memory
- **[openai-fitness-coach](./applications/openai-fitness-coach)** - Fitness coach with OpenAI Agents and Hindsight memory
- **[sanity-blog-memory](./applications/sanity-blog-memory)** - Syncing Sanity CMS content to Hindsight
- **[chat-sdk-multi-platform](./applications/chat-sdk-multi-platform)** - Cross-platform Slack + Discord bot with shared memory (Vercel Chat SDK)
- **[stancetracker](./applications/stancetracker)** - Track political stances using AI-powered memory

## Notebooks

Interactive Jupyter notebooks demonstrating Hindsight features:

### Core Tutorials

- **[01-quickstart.ipynb](./notebooks/01-quickstart.ipynb)** - Basic operations: retain, recall, and reflect
- **[02-per-user-memory.ipynb](./notebooks/02-per-user-memory.ipynb)** - Pattern for per-user memory banks
- **[03-support-agent-shared-knowledge.ipynb](./notebooks/03-support-agent-shared-knowledge.ipynb)** - Multi-bank architecture for support agents
- **[04-litellm-memory-demo.ipynb](./notebooks/04-litellm-memory-demo.ipynb)** - Automatic memory with LiteLLM callbacks
- **[05-tool-learning-demo.ipynb](./notebooks/05-tool-learning-demo.ipynb)** - Learning tool selection through memory

### Quick Demos

- **[fitness_tracker.ipynb](./notebooks/fitness_tracker.ipynb)** - Fitness coach with workout and diet memory
- **[healthcare_assistant.ipynb](./notebooks/healthcare_assistant.ipynb)** - Health chatbot demo
- **[movie_recommendation.ipynb](./notebooks/movie_recommendation.ipynb)** - Personalized movie recommender
- **[personal_assistant.ipynb](./notebooks/personal_assistant.ipynb)** - General-purpose assistant with long-term memory
- **[personalized_search.ipynb](./notebooks/personalized_search.ipynb)** - Context-aware search agent
- **[study_buddy.ipynb](./notebooks/study_buddy.ipynb)** - Study assistant with spaced repetition

## Getting Started

### Prerequisites

Start Hindsight using Docker:

```bash
export OPENAI_API_KEY=your-key

docker run --rm -it --pull always -p 8888:8888 -p 9999:9999 \
  -e HINDSIGHT_API_LLM_API_KEY=$OPENAI_API_KEY \
  -e HINDSIGHT_API_L
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `hindsight.md`
```markdown
# 📦 vectorize-io/hindsight [🔖 PENDING/APPROVE]
🔗 https://github.com/vectorize-io/hindsight
🌐 https://hindsight.vectorize.io/

## Meta
- **Stars:** ⭐ 6400 | **Forks:** 🍴 357
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Hindsight: Agent Memory That  Learns

## README (trích đầu)
```
<div align="center">

![Hindsight Banner](./hindsight-docs/static/img/hindsight-github-banner.png)

[Documentation](https://hindsight.vectorize.io) • [Paper](https://arxiv.org/abs/2512.12818) • [Cookbook](https://hindsight.vectorize.io/cookbook) • [Hindsight Cloud](https://ui.hindsight.vectorize.io/signup)

[![CI](https://github.com/vectorize-io/hindsight/actions/workflows/release.yml/badge.svg)](https://github.com/vectorize-io/hindsight/actions/workflows/release.yml)
[![Slack Community](https://img.shields.io/badge/Slack-Join%20Community-4A154B?logo=slack)](https://join.slack.com/t/hindsight-space/shared_invite/zt-3nhbm4w29-LeSJ5Ixi6j8PdiYOCPlOgg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![gitcgr](https://gitcgr.com/badge/vectorize-io/hindsight.svg)](https://gitcgr.com/vectorize-io/hindsight)
![PyPI - Downloads](https://img.shields.io/pypi/dm/hindsight-api?label=PyPI)
![NPM Downloads](https://img.shields.io/npm/dm/%40vectorize-io%2Fhindsight-client?logoColor=orange&label=NPM&color=blue&link=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40vectorize-io%2Fhindsight-client)
<br/>

<a href="https://trendshift.io/repositories/15603" target="_blank"><img src="https://trendshift.io/api/badge/repositories/15603" alt="vectorize-io%2Fhindsight | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

---

## What is Hindsight?

Hindsight™ is an agent memory system built to create smarter agents that learn over time. Most agent memory systems focus on recalling conversation history. Hindsight is focused on making agents that learn, not just remember.


<video src="https://github.com/user-attachments/assets/923b798d-3581-4897-bb62-9cfa5a931682" controls></video>

It eliminates the shortcomings of alternative techniques such as RAG and knowledge graph and delivers state-of-the-art performance on long term memory tasks.

## Memory Performance & Accuracy

Hindsight is the most accurate agent memory system ever tested according to benchmark performance. It has achieved state-of-the-art performance on the LongMemEval benchmark, widely used to assess memory system performance across a variety of conversational AI scenarios. The current reported performance of Hindsight and other agent memory solutions as of January 2026 is shown here:

![Overview](./hindsight-docs/static/img/hindsight-bench.jpg)

The benchmark performance data for Hindsight has been independently reproduced by research collaborators at the Virginia Tech [Sanghani Center for Artificial Intelligence and Data Analytics](https://sanghani.cs.vt.edu/) and The Washington Post. Other scores are self-reported by software vendors.

Hindsight is being used in production at Fortune 500 enterprises and by a growing number of AI startups. 

## Adding Hindsight to Your AI Agents

The easiest way to use Hindsight with an existing agent is with the LLM Wrapper. You can add memory to your agent with 2 lines of code. That wi
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pg0.md`
```markdown
# 📦 vectorize-io/pg0 [🔖 PENDING/APPROVE]
🔗 https://github.com/vectorize-io/pg0


## Meta
- **Stars:** ⭐ 43 | **Forks:** 🍴 3
- **Language:** Rust | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
pg0 - Zero-config PostgreSQL with pgvector

## README (trích đầu)
```
# pg0

[![PyPI version](https://badge.fury.io/py/pg0-embedded.svg)](https://pypi.org/project/pg0-embedded/)
[![PyPI downloads](https://img.shields.io/pypi/dm/pg0-embedded.svg)](https://pypi.org/project/pg0-embedded/)
[![Python versions](https://img.shields.io/pypi/pyversions/pg0-embedded.svg)](https://pypi.org/project/pg0-embedded/)

**Zero-config PostgreSQL with pgvector.**

A single binary that runs PostgreSQL locally - no installation, no configuration, no Docker required. Includes **pgvector** for AI/vector workloads out of the box.

## Why pg0?

PostgreSQL setup is painful. Docker adds complexity. Local installs conflict with system packages. pg0 gives you a real PostgreSQL server with zero friction:

- **No installation** - download a single binary and run `pg0 start`
- **No Docker** - no containers, no daemon, no complexity
- **No configuration** - sensible defaults, just works
- **Production parity** - develop with the same database you'll deploy
- **Full PostgreSQL** - JSON, arrays, CTEs, window functions, extensions, pgvector - everything works

Use pg0 for local development, testing, CI/CD pipelines, or any scenario where you want PostgreSQL without the setup overhead.

## Supported Platforms

| Platform | Architecture | Binary |
|----------|--------------|--------|
| macOS | Apple Silicon (M1/M2/M3) | `pg0-macos-arm64` |
| Linux | x86_64 (glibc) | `pg0-linux-amd64-gnu` |
| Linux | x86_64 (musl/Alpine) | `pg0-linux-amd64-musl` |
| Linux | ARM64 (glibc) | `pg0-linux-arm64-gnu` |
| Linux | ARM64 (musl/Alpine) | `pg0-linux-arm64-musl` |
| Windows | x64 | `pg0-windows-amd64.exe` |

## Features

- **Zero dependencies** - single binary, works offline
- **PostgreSQL 18** with pgvector 0.8.1 bundled
- **Multiple instances** - run multiple PostgreSQL servers simultaneously
- **Cross-platform** - macOS (Apple Silicon), Linux (x86_64 & ARM64), Windows (x64)
- **Language SDKs** - Python and Node.js libraries for programmatic control
- **Bundled psql** - no separate client installation needed
- **Persistent data** - survives restarts, stored in `~/.pg0/`

## Installation

### CLI Binary

The install script automatically detects your platform and downloads the correct binary:

```bash
curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/install.sh | bash
```

Or with a custom install directory:

```bash
INSTALL_DIR=/usr/local/bin curl -fsSL https://raw.githubusercontent.com/vectorize-io/pg0/main/install.sh | bash
```

### Python SDK

Install via pip:

```bash
pip install pg0-embedded
```

Quick start:

```python
from pg0 import Pg0

# Start PostgreSQL
pg = Pg0()
pg.start()
print(pg.uri)  # postgresql://postgres:postgres@localhost:5432/postgres

# Or use context manager
with Pg0() as pg:
    result = pg.execute("SELECT version();")
    print(result)
```

See [PyPI package](https://pypi.org/project/pg0-embedded/) for more details.

### Node.js SDK

Install via npm:

```bash
npm install @vectorize-io/pg0
```

Quick start:

```typescript
i
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


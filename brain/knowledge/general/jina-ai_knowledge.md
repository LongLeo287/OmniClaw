---
id: jina-ai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.003253
---

# KNOWLEDGE EXTRACT: jina-ai
> **Extracted on:** 2026-03-30 17:38:12
> **Source:** jina-ai

---

## File: `serve.md`
```markdown
# 📦 jina-ai/serve [🔖 PENDING/APPROVE]
🔗 https://github.com/jina-ai/serve
🌐 https://jina.ai/serve

## Meta
- **Stars:** ⭐ 21853 | **Forks:** 🍴 2240
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
☁️ Build multimodal AI applications with cloud-native stack

## README (trích đầu)
```
# Jina-Serve
<a href="https://pypi.org/project/jina/"><img alt="PyPI" src="https://img.shields.io/pypi/v/jina?label=Release&style=flat-square"></a>
<a href="https://discord.jina.ai"><img src="https://img.shields.io/discord/1106542220112302130?logo=discord&logoColor=white&style=flat-square"></a>
<a href="https://pypistats.org/packages/jina"><img alt="PyPI - Downloads from official pypistats" src="https://img.shields.io/pypi/dm/jina?style=flat-square"></a>
<a href="https://github.com/jina-ai/jina/actions/workflows/cd.yml"><img alt="Github CD status" src="https://github.com/jina-ai/jina/actions/workflows/cd.yml/badge.svg"></a>

Jina-serve is a framework for building and deploying AI services that communicate via gRPC, HTTP and WebSockets. Scale your services from local development to production while focusing on your core logic.

## Key Features

- Native support for all major ML frameworks and data types
- High-performance service design with scaling, streaming, and dynamic batching
- LLM serving with streaming output
- Built-in Docker integration and Executor Hub
- One-click deployment to Jina AI Cloud
- Enterprise-ready with Kubernetes and Docker Compose support

<details>
<summary><strong>Comparison with FastAPI</strong></summary>

Key advantages over FastAPI:

- DocArray-based data handling with native gRPC support
- Built-in containerization and service orchestration
- Seamless scaling of microservices
- One-command cloud deployment
</details>

## Install 

```bash
pip install jina
```

See guides for [Apple Silicon](https://jina.ai/serve/get-started/install/apple-silicon-m1-m2/) and [Windows](https://jina.ai/serve/get-started/install/windows/).

## Core Concepts

Three main layers:
- **Data**: BaseDoc and DocList for input/output
- **Serving**: Executors process Documents, Gateway connects services
- **Orchestration**: Deployments serve Executors, Flows create pipelines

## Build AI Services

Let's create a gRPC-based AI service using StableLM:

```python
from jina import Executor, requests
from docarray import DocList, BaseDoc
from transformers import pipeline


class Prompt(BaseDoc):
    text: str


class Generation(BaseDoc):
    prompt: str
    text: str


class StableLM(Executor):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generator = pipeline(
            'text-generation', model='stabilityai/stablelm-base-alpha-3b'
        )

    @requests
    def generate(self, docs: DocList[Prompt], **kwargs) -> DocList[Generation]:
        generations = DocList[Generation]()
        prompts = docs.text
        llm_outputs = self.generator(prompts)
        for prompt, output in zip(prompts, llm_outputs):
            generations.append(Generation(prompt=prompt, text=output))
        return generations
```

Deploy with Python or YAML:

```python
from jina import Deployment
from executor import StableLM

dep = Deployment(uses=StableLM, timeout_ready=-1, port=12345)

with dep:
    dep.block()
```

```yaml
jtype: Depl
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


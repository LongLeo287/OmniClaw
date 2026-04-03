---
id: llmware-ai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:05.367639
---

# KNOWLEDGE EXTRACT: llmware-ai
> **Extracted on:** 2026-03-30 17:42:01
> **Source:** llmware-ai

---

## File: `llmware.md`
```markdown
# 📦 llmware-ai/llmware [🔖 PENDING/APPROVE]
🔗 https://github.com/llmware-ai/llmware
🌐 https://llmware-ai.github.io/llmware/

## Meta
- **Stars:** ⭐ 14866 | **Forks:** 🍴 2950
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Unified framework for building enterprise RAG pipelines with small, specialized models

## README (trích đầu)
```
# llmware
![Static Badge](https://img.shields.io/badge/python-3.10_%7C_3.11%7C_3.12%7C_3.13%7C_3.14-blue?color=blue)
![PyPI - Version](https://img.shields.io/pypi/v/llmware?color=blue)
[![members](https://discord-live-members-count-badge.vercel.app/api/discord-members?guildId=1179245642770559067&label=discord%20members&color=5865F2)](https://discord.gg/bphreFK4NJ)
[![Documentation](https://github.com/llmware-ai/llmware/actions/workflows/pages.yml/badge.svg)](https://github.com/llmware-ai/llmware/actions/workflows/pages.yml)  

## 🧰🛠️ Unified framework for building knowledge-based local, private, secure LLM-based applications       

`llmware` is optimized for AI PC and local laptop, edge and self-hosted deployment across a wide range of Windows, Mac and Linux platforms, with support for GGUF, OpenVINO, ONNXRuntime, ONNXRuntime-QNN (Qualcomm), WindowsLocalFoundry, and Pytorch, providing a high-level interface that makes it easy to leverage the right inferencing technology optimized for the target platform.  

 `llmware` has two main components:  

 1.  **Model catalog with 300+ models** - models prepackaged in quantized, optimized formats, to leverage on device GPU and NPU capabilities, with support for major open source model families and 50+ llmware finetuned SLIM, Bling, Dragon and Industry-Bert models specialized for key tasks in enterprise process automation.  Also supports leading cloud models from OpenAI, Anthropic and Google.  
 
 2.  **RAG Pipeline** - integrated components for the full lifecycle of connecting knowledge sources to generative AI models with wide range of document parsing and ingestion capabilities, and the ability to create scalable knowledge bases.

By bringing together both of these components,  `llmware` offers a comprehensive set of tools to rapidly build knowledge-based enterprise LLM applications.  

Our vision is that AI should be sustainable, accurate, and cost-effective, using the smallest possible compute footprint to get the job done.  

Virtually all of our examples and models can be run on device - get started right away on your laptop.   

[Join us on Discord](https://discord.gg/MhZn5Nc39h)   |  [Watch Youtube Tutorials](https://www.youtube.com/@llmware)  | [Explore our Model Families on Huggingface](https://www.huggingface.co/llmware)   


## 🎯  Key features 
Writing code with`llmware` is based on a few main concepts:

<details>
<summary><b>Model Catalog</b>: Access all models the same way with easy lookup, regardless of underlying implementation. 
</summary>  


```python
#   300+ Models in Catalog with 50+ RAG-optimized BLING, DRAGON and Industry BERT models
#   Full support for GGUF, OpenVINO, Onnxruntime, HuggingFace, Sentence Transformers and major API-based models
#   Easy to extend to add custom models - see examples

from llmware.models import ModelCatalog
from llmware.prompts import Prompt

#   all models accessed through the ModelCatalog
models = ModelCatalog().list_all_models()

#   to use any mod
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


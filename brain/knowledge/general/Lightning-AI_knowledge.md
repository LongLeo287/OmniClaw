---
id: lightning-ai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:04.165544
---

# KNOWLEDGE EXTRACT: Lightning-AI
> **Extracted on:** 2026-03-30 17:40:16
> **Source:** Lightning-AI

---

## File: `litgpt.md`
```markdown
# 📦 Lightning-AI/litgpt [🔖 PENDING/APPROVE]
🔗 https://github.com/Lightning-AI/litgpt
🌐 https://lightning.ai

## Meta
- **Stars:** ⭐ 13262 | **Forks:** 🍴 1414
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
20+ high-performance LLMs with recipes to pretrain, finetune and deploy at scale.

## README (trích đầu)
```
<div align="center">


# ⚡ LitGPT

**20+ high-performance LLMs with recipes to pretrain, finetune, and deploy at scale.**

<pre>
✅ From scratch implementations      ✅ No abstractions         ✅ Beginner friendly
   ✅ Flash attention                   ✅ FSDP                    ✅ LoRA, QLoRA, Adapter
✅ Reduce GPU memory (fp4/8/16/32)   ✅ 1-1000+ GPUs/TPUs       ✅ 20+ LLMs         
</pre>


---


![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytorch-lightning)
![cpu-tests](https://github.com/lightning-AI/lit-stablelm/actions/workflows/cpu-tests.yml/badge.svg) [![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/Lightning-AI/lit-stablelm/blob/master/LICENSE) [![Discord](https://img.shields.io/discord/1077906959069626439)](https://discord.gg/VptPCZkGNa)

<p align="center">
  <a href="#quick-start">Quick start</a> •
  <a href="#choose-from-20-llms">Models</a> •
  <a href="#finetune-an-llm">Finetune</a> •
  <a href="#deploy-an-llm">Deploy</a> •
  <a href="#all-workflows">All workflows</a> •
  <a href="#state-of-the-art-features">Features</a> •
  <a href="#training-recipes">Recipes (YAML)</a> •
  <a href="https://lightning.ai/">Lightning AI</a> •
    <a href="#tutorials">Tutorials</a>
</p>

&nbsp;

<a target="_blank" href="https://lightning.ai/lightning-ai/studios/litgpt-quick-start">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/get-started-badge.svg" height="36px" alt="Get started"/>
</a>

&nbsp;

</div>

# Looking for GPUs?
Over 340,000 developers use [Lightning Cloud](https://lightning.ai/?utm_source=litgpt_readme&utm_medium=referral&utm_campaign=litgpt_readme) - purpose-built for PyTorch and PyTorch Lightning. 
- [GPUs](https://lightning.ai/pricing?utm_source=litgpt_readme&utm_medium=referral&utm_campaign=litgpt_readme) from $0.19.   
- [Clusters](https://lightning.ai/clusters?utm_source=litgpt_readme&utm_medium=referral&utm_campaign=litgpt_readme): frontier-grade training/inference clusters.   
- [AI Studio (vibe train)](https://lightning.ai/studios?utm_source=litgpt_readme&utm_medium=referral&utm_campaign=litgpt_readme): workspaces where AI helps you debug, tune and vibe train.
- [AI Studio (vibe deploy)](https://lightning.ai/studios?utm_source=litgpt_readme&utm_medium=referral&utm_campaign=litgpt_readme): workspaces where AI helps you optimize, and deploy models.     
- [Notebooks](https://lightning.ai/notebooks?utm_source=litgpt_readme&utm_medium=referral&utm_campaign=litgpt_readme): Persistent GPU workspaces where AI helps you code and analyze.
- [Inference](https://lightning.ai/deploy?utm_source=litgpt_readme&utm_medium=referral&utm_campaign=litgpt_readme): Deploy models as inference APIs.

# Finetune, pretrain, and inference LLMs Lightning fast ⚡⚡
Every LLM is implemented from scratch with **no abstractions** and **full control**, making them blazing fast, minimal, and performant at enterprise scale.

✅ **Enterprise ready -** Apache 2.0 for unlimited enterprise
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `LitServe.md`
```markdown
# 📦 Lightning-AI/LitServe [🔖 PENDING/APPROVE]
🔗 https://github.com/Lightning-AI/LitServe
🌐 https://lightning.ai/litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme

## Meta
- **Stars:** ⭐ 3841 | **Forks:** 🍴 276
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A minimal Python framework for building custom AI inference servers with full control over logic, batching, and scaling.

## README (trích đầu)
```
<div align='center'>

<h1>
  Build custom inference servers in pure Python
  <br/>
</h1> 
<h4>
  Define exactly how inference works for models, agents, RAG, or pipelines. 
  <br/>
  Control batching, routing, streaming, and orchestration without MLOps glue or config files.
</h4> 

<img alt="Lightning" src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/ls_banner2.png" width="800px" style="max-width: 100%;">

&nbsp; 
</div>

<div align='center'>
  
<pre>
✅ Custom inference logic  ✅ 2× faster than FastAPI     ✅ Agents, RAG, pipelines, more
✅ Custom logic + control  ✅ Any PyTorch model          ✅ Self-host or managed        
✅ Multi-GPU autoscaling   ✅ Batching + streaming       ✅ BYO model or vLLM           
✅ No MLOps glue code      ✅ Easy setup in Python       ✅ Serverless support          

</pre>

<div align='center'>

[![PyPI Downloads](https://static.pepy.tech/badge/litserve)](https://pepy.tech/projects/litserve)
[![Discord](https://img.shields.io/discord/1077906959069626439?label=Get%20help%20on%20Discord)](https://discord.gg/WajDThKAur)
![cpu-tests](https://github.com/Lightning-AI/litserve/actions/workflows/ci-testing.yml/badge.svg)
[![codecov](https://codecov.io/gh/Lightning-AI/litserve/graph/badge.svg?token=SmzX8mnKlA)](https://codecov.io/gh/Lightning-AI/litserve)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/Lightning-AI/litserve/blob/main/LICENSE)

</div>
</div>
<div align="center">
  <div style="text-align: center;">
    <a target="_blank" href="#quick-start" style="margin: 0 10px;">Quick start</a> •
    <a target="_blank" href="#featured-examples" style="margin: 0 10px;">Examples</a> •
    <a target="_blank" href="#features" style="margin: 0 10px;">Features</a> •
    <a target="_blank" href="#performance" style="margin: 0 10px;">Performance</a> •
    <a target="_blank" href="#host-anywhere" style="margin: 0 10px;">Hosting</a> •
    <a target="_blank" href="https://lightning.ai/docs/litserve?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme" style="margin: 0 10px;">Docs</a>
  </div>
</div>

&nbsp;

<div align="center">
<a target="_blank" href="https://lightning.ai/docs/litserve/home/get-started?utm_source=litserve_readme&utm_medium=referral&utm_campaign=litserve_readme">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/get-started-badge.svg" height="36px" alt="Get started"/>
</a>
</div>

&nbsp; 

# Why LitServe?
Most serving tools (vLLM, etc..) are built for a single model type and enforce rigid abstractions. They work well until you need custom logic, multiple models, agents, or non standard pipelines. LitServe lets you write your own inference engine in Python. You define how requests are handled, how models are loaded, how batching and routing work, and how outputs are produced. LitServe handles performance, concurrency, scaling, and deployment. Use LitServe to build inference APIs, agents, chatbots, RAG systems, MCP servers
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pytorch-lightning.md`
```markdown
# 📦 Lightning-AI/pytorch-lightning [🔖 PENDING/APPROVE]
🔗 https://github.com/Lightning-AI/pytorch-lightning
🌐 https://lightning.ai/pytorch-lightning/?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme

## Meta
- **Stars:** ⭐ 30971 | **Forks:** 🍴 3694
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Pretrain, finetune ANY AI model of ANY size on 1 or 10,000+ GPUs with zero code changes.

## README (trích đầu)
```
<div align="center">

<img alt="Lightning" src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/ptl_banner.png" width="800px" style="max-width: 100%;">

<br/>
<br/>

**The deep learning framework to pretrain and finetune AI models.**

**Serving models?** Use [LitServe](https://github.com/Lightning-AI/litserve?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme) to build custom inference servers in pure Python.

______________________________________________________________________

<p align="center">
    <a href="#quick-start" style="margin: 0 10px;">Quick start</a> •
  <a href="#examples">Examples</a> •
  <a href="#why-pytorch-lightning">PyTorch Lightning</a> •
  <a href="#lightning-fabric-expert-control">Fabric</a> •
  <a href="https://lightning.ai/?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme">Lightning Cloud</a> •   
  <a href="#community">Community</a> •
  <a href="https://pytorch-lightning.readthedocs.io/en/stable/">Docs</a>
</p>

<!-- DO NOT ADD CONDA DOWNLOADS... README CHANGES MUST BE APPROVED BY EDEN OR WILL -->

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytorch-lightning)](https://pypi.org/project/pytorch-lightning/)
[![PyPI Status](https://badge.fury.io/py/pytorch-lightning.svg)](https://badge.fury.io/py/pytorch-lightning)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pytorch-lightning)](https://pepy.tech/project/pytorch-lightning)
[![Conda](https://img.shields.io/conda/v/conda-forge/lightning?label=conda&color=success)](https://anaconda.org/conda-forge/lightning)
[![codecov](https://codecov.io/gh/Lightning-AI/pytorch-lightning/graph/badge.svg?token=SmzX8mnKlA)](https://codecov.io/gh/Lightning-AI/pytorch-lightning)

[![Discord](https://img.shields.io/discord/1077906959069626439?style=plastic)](https://discord.gg/VptPCZkGNa)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/lightning-ai/lightning)
[![license](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/Lightning-AI/pytorch-lightning/blob/master/LICENSE)

<!--
[![CodeFactor](https://www.codefactor.io/repository/github/Lightning-AI/lightning/badge)](https://www.codefactor.io/repository/github/Lightning-AI/lightning)
-->

</div>

<div align="center">
  
<p align="center">

&nbsp;

<a target="_blank" href="https://lightning.ai/docs/pytorch/latest/starter/introduction.html?utm_source=ptl_readme&utm_medium=referral&utm_campaign=ptl_readme#define-a-lightningmodule">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/get-started-badge.svg" height="36px" alt="Get started"/>
</a>

</p>

</div>

&nbsp;

<a id="why-pytorch-lightning"></a>
# Why PyTorch Lightning?   
Training models in plain PyTorch requires writing and maintaining a lot of repetitive engineering code. Handling backpropagation, mixed precision, multi-GPU, and distributed training is error-prone and often reimplemented for every project. PyTorch Lightning organizes PyTorch cod
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


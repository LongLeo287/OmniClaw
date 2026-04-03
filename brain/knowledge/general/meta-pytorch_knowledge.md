---
id: meta-pytorch-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:07.665085
---

# KNOWLEDGE EXTRACT: meta-pytorch
> **Extracted on:** 2026-03-30 17:42:47
> **Source:** meta-pytorch

---

## File: `torchtune.md`
```markdown
# 📦 meta-pytorch/torchtune [🔖 PENDING/APPROVE]
🔗 https://github.com/meta-pytorch/torchtune
🌐 https://pytorch.org/torchtune/main/

## Meta
- **Stars:** ⭐ 5712 | **Forks:** 🍴 709
- **Language:** Python | **License:** BSD-3-Clause
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
PyTorch native post-training library

## README (trích đầu)
```



# torchtune

[![Unit Test](https://github.com/pytorch/torchtune/actions/workflows/unit_test.yaml/badge.svg?branch=main)](https://github.com/pytorch/torchtune/actions/workflows/unit_test.yaml)
![Integration Tests](https://github.com/pytorch/torchtune/actions/workflows/gpu_test.yaml/badge.svg)
[![](https://dcbadge.vercel.app/api/server/4Xsdn8Rr9Q?style=flat)](https://discord.gg/4Xsdn8Rr9Q)

[**Overview**](#overview-) | [**Installation**](#installation-%EF%B8%8F) | [**Get Started**](#get-started-) |  [**Documentation**](https://pytorch.org/torchtune/main/index.html) | [**Community**](#community-) | [**Citing torchtune**](#citing-torchtune-) | [**License**](#license)

### 📣 Recent updates 📣
* *May 2025*: torchtune has added support for *Qwen3* models! Check out all the configs [here](recipes/configs/qwen3)
* *April 2025*: **Llama4** is now available in torchtune! Try out our full and LoRA finetuning configs [here](recipes/configs/llama4)
* *February 2025*: Multi-node training is officially [open for business in torchtune](https://pytorch.org/torchtune/main/tutorials/multinode.html)! Full finetune on multiple nodes to take advantage of larger batch sizes and models.
* *December 2024*: torchtune now supports **Llama 3.3 70B**! Try it out by following our installation instructions [here](#installation-%EF%B8%8F), then run any of the configs [here](recipes/configs/llama3_3).
* *November 2024*: torchtune has released [v0.4.0](https://github.com/pytorch/torchtune/releases/tag/v0.4.0) which includes stable support for exciting features like activation offloading and multimodal QLoRA
* *November 2024*: torchtune has added [Gemma2](recipes/configs/gemma2) to its models!
* *October 2024*: torchtune added support for Qwen2.5 models - find the configs [here](recipes/configs/qwen2_5/)
* *September 2024*: torchtune has support for **Llama 3.2 11B Vision**, **Llama 3.2 3B**, and **Llama 3.2 1B** models! Try them out by following our installation instructions [here](#installation-%EF%B8%8F), then run any of the text configs [here](recipes/configs/llama3_2) or vision configs [here](recipes/configs/llama3_2_vision).


&nbsp;

## Overview 📚


torchtune is a PyTorch library for easily authoring, post-training, and experimenting with LLMs. It provides:

- Hackable training recipes for SFT, knowledge distillation, DPO, PPO, GRPO, and quantization-aware training
- Simple PyTorch implementations of popular LLMs like Llama, Gemma, Mistral, Phi, Qwen, and more
- Best-in-class memory efficiency, performance improvements, and scaling, utilizing the latest PyTorch APIs
- YAML configs for easily configuring training, evaluation, quantization or inference recipes

&nbsp;

### Post-training recipes

torchtune supports [the entire post-training lifecycle](https://pytorch.org/torchtune/main/recipes/recipes_overview.html). A successful post-trained model will likely utilize several of the below methods.

#### Supervised Finetuning (SFT)

| Type of Weight Update | 1 Device | >1 Devi
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


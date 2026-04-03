---
id: unslothai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:25.570559
---

# KNOWLEDGE EXTRACT: unslothai
> **Extracted on:** 2026-03-30 17:58:05
> **Source:** unslothai

---

## File: `notebooks.md`
```markdown
# 📦 unslothai/notebooks [🔖 PENDING/APPROVE]
🔗 https://github.com/unslothai/notebooks
🌐 https://unsloth.ai/docs

## Meta
- **Stars:** ⭐ 5031 | **Forks:** 🍴 806
- **Language:** Jupyter Notebook | **License:** LGPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
250+ Fine-tuning & RL Notebooks for text, vision, audio, embedding, TTS models.

## README (trích đầu)
```
<div align="center">

  <a href="https://unsloth.ai"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20logo%20white%20text.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20logo%20black%20text.png">
    <img alt="unsloth logo" src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20logo%20black%20text.png" height="110" style="max-width: 100%;">
  </picture></a>
  
<a href="https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-(20B)-Fine-tuning.ipynb"><img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/start free finetune button.png" height="48"></a>
<a href="https://discord.gg/unsloth"><img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/Discord button.png" height="48"></a>
<a href="https://unsloth.ai/docs/get-started/unsloth-notebooks"><img src="https://raw.githubusercontent.com/unslothai/unsloth/refs/heads/main/images/Documentation%20Button.png" height="48"></a>

</div>

## 📒 Fine-tuning Notebooks
Below are Colab notebooks, organized by model. You can also view all [notebooks in our docs](https://unsloth.ai/docs/get-started/unsloth-notebooks).<br>The notebooks run locally and feature data prep, training and inference. Read our [fine-tuning guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide).

### Main Notebooks
| Model                        | Type           | Notebook Link                                                                                                                                                                                         |
|-----------------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Qwen3.5 (4B)**            | Vision         | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_%284B%29_Vision.ipynb)                 |
| **Qwen3.5 (2B)**            | Vision         | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_5_%282B%29_Vision.ipynb)                 |
| **gpt-oss (20B)**           | Fine-tuning    | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-%2820B%29-Fine-tuning.ipynb)           |
| **gpt-oss (20B)**           | GRPO           | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-%2820B%29-GRPO.ipynb)   
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `unsloth.md`
```markdown
# 📦 unslothai/unsloth [🔖 PENDING]
🔗 https://github.com/unslothai/unsloth
🌐 https://unsloth.ai/docs

## Meta
- **Stars:** ⭐ 58317 | **Forks:** 🍴 4918
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
Unsloth Studio is a web UI for training and running open models like Qwen, DeepSeek, gpt-oss and Gemma locally.

## README (trích đầu)
```
<h1 align="center" style="margin:0;">
  <a href="https://unsloth.ai/docs"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/unslothai/unsloth/main/images/STUDIO%20WHITE%20LOGO.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/unslothai/unsloth/main/images/STUDIO%20BLACK%20LOGO.png">
    <img alt="Unsloth logo" src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/STUDIO%20BLACK%20LOGO.png" height="60" style="max-width:100%;">
  </picture></a>
</h1>
<h3 align="center" style="margin: 0; margin-top: 0;">
Run and train AI models with a unified local interface.
</h3>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quickstart">Quickstart</a> •
  <a href="#-free-notebooks">Notebooks</a> •
  <a href="https://unsloth.ai/docs">Documentation</a> •
  <a href="https://www.reddit.com/r/unsloth/">Reddit</a>
</p>
 <a href="https://unsloth.ai/docs/new/studio">
<img alt="unsloth studio ui homepage" src="https://raw.githubusercontent.com/unslothai/unsloth/main/studio/frontend/public/studio%20github%20landscape%20colab%20display.png" style="max-width: 100%; margin-bottom: 0;"></a>

Unsloth Studio (Beta) lets you run and train text, [audio](https://unsloth.ai/docs/basics/text-to-speech-tts-fine-tuning), [embedding](https://unsloth.ai/docs/new/embedding-finetuning), [vision](https://unsloth.ai/docs/basics/vision-fine-tuning) models on Windows, Linux and macOS.

## ⭐ Features
Unsloth provides several key features for both inference and training:
### Inference
* **Search + download + run models** including GGUF, LoRA adapters, safetensors
* **Export models**: [Save or export](https://unsloth.ai/docs/new/studio/export) models to GGUF, 16-bit safetensors and other formats.
* **Tool calling**: Support for [self-healing tool calling](https://unsloth.ai/docs/new/studio/chat#auto-healing-tool-calling) and web search
* **[Code execution](https://unsloth.ai/docs/new/studio/chat#code-execution)**: lets LLMs test code in Claude artifacts and sandbox environments
* [Auto-tune inference parameters](https://unsloth.ai/docs/new/studio/chat#auto-parameter-tuning) and customize chat templates.
* We work directly with teams behind [gpt-oss](https://docs.unsloth.ai/new/gpt-oss-how-to-run-and-fine-tune#unsloth-fixes-for-gpt-oss), [Qwen3](https://www.reddit.com/r/LocalLLaMA/comments/1kaodxu/qwen3_unsloth_dynamic_ggufs_128k_context_bug_fixes/), [Llama 4](https://github.com/ggml-org/llama.cpp/pull/12889), [Mistral](models/tutorials/devstral-how-to-run-and-fine-tune.md), [Gemma 1-3](https://news.ycombinator.com/item?id=39671146), and [Phi-4](https://unsloth.ai/blog/phi4), where we’ve fixed bugs that improve model accuracy.
* Upload images, audio, PDFs, code, DOCX and more file types to chat with.
### Training
* Train and RL **500+ models** up to **2x faster** with up to **70% less VRAM**, with no accuracy loss.
* Custom Triton and mathematical **kernels**. S
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


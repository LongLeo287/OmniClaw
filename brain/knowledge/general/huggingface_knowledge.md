---
id: huggingface-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:52.875168
---

# KNOWLEDGE EXTRACT: huggingface
> **Extracted on:** 2026-03-30 17:38:08
> **Source:** huggingface

---

## File: `accelerate.md`
```markdown
# 📦 huggingface/accelerate [🔖 PENDING/APPROVE]
🔗 https://github.com/huggingface/accelerate
🌐 https://huggingface.co/docs/accelerate

## Meta
- **Stars:** ⭐ 9582 | **Forks:** 🍴 1317
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🚀 A simple way to launch, train, and use PyTorch models on almost any device and distributed configuration, automatic mixed precision (including fp8), and easy-to-configure FSDP and DeepSpeed support

## README (trích đầu)
```
<!---
Copyright 2021 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

<p align="center">
    <br>
    <img src="https://raw.githubusercontent.com/huggingface/accelerate/main/docs/source/imgs/accelerate_logo.png" width="400"/>
    <br>
<p>

<p align="center">
    <!-- Uncomment when CircleCI is set up
    <a href="https://circleci.com/gh/huggingface/accelerate"><img alt="Build" src="https://img.shields.io/circleci/build/github/huggingface/transformers/master"></a>
    -->
    <a href="https://github.com/huggingface/accelerate/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/huggingface/accelerate.svg?color=blue"></a>
    <a href="https://huggingface.co/docs/accelerate/index.html"><img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/accelerate/index.html.svg?down_color=red&down_message=offline&up_message=online"></a>
    <a href="https://github.com/huggingface/accelerate/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/accelerate.svg"></a>
    <a href="https://github.com/huggingface/accelerate/blob/main/CODE_OF_CONDUCT.md"><img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg"></a>
</p>

<h3 align="center">
<p>Run your *raw* PyTorch training script on any kind of device
</h3>

<h3 align="center">
    <a href="https://hf.co/course"><img src="https://raw.githubusercontent.com/huggingface/accelerate/main/docs/source/imgs/course_banner.png"></a>
</h3>

## Easy to integrate

🤗 Accelerate was created for PyTorch users who like to write the training loop of PyTorch models but are reluctant to write and maintain the boilerplate code needed to use multi-GPUs/TPU/fp16.

🤗 Accelerate abstracts exactly and only the boilerplate code related to multi-GPUs/TPU/fp16 and leaves the rest of your code unchanged.

Here is an example:

```diff
  import torch
  import torch.nn.functional as F
  from datasets import load_dataset
+ from accelerate import Accelerator

+ accelerator = Accelerator()
- device = 'cpu'
+ device = accelerator.device

  model = torch.nn.Transformer().to(device)
  optimizer = torch.optim.Adam(model.parameters())

  dataset = load_dataset('my_dataset')
  data = torch.utils.data.DataLoader(dataset, shuffle=True)

+ model, optimizer, data = accelerator.prepare(model, optimizer, data)

  model.train()
  for epoch in range(10):
      for source, targets in data:
          s
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `agents-course.md`
```markdown
# 📦 huggingface/agents-course [🔖 PENDING/APPROVE]
🔗 https://github.com/huggingface/agents-course


## Meta
- **Stars:** ⭐ 27236 | **Forks:** 🍴 1955
- **Language:** MDX | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
This repository contains the Hugging Face Agents Course. 

## README (trích đầu)
```
# <a href="https://hf.co/learn/agents-course" target="_blank">The Hugging Face Agents Course</a>

If you like the course, **don't hesitate to ⭐ star this repository**. This helps us to **make the course more visible 🤗**.

<img src="https://huggingface.co/datasets/agents-course/course-images/resolve/main/en/communication/please_star.gif" alt="Star the repo" />

## Content

The course is divided into 4 units. These will take you from **the basics of agents to a final assignment with a benchmark**.

Sign up here (it's free) 👉 <a href="https://bit.ly/hf-learn-agents" target="_blank">https://bit.ly/hf-learn-agents</a>

You can access the course here 👉 <a href="https://hf.co/learn/agents-course" target="_blank">https://hf.co/learn/agents-course</a>

| Unit    | Topic                                                                                                          | Description                                                                                                                            |
|---------|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0       | [Welcome to the Course](https://huggingface.co/learn/agents-course/en/unit0/introduction)                      | Welcome, guidelines, necessary tools, and course overview.                                                                             |
| 1       | [Introduction to Agents](https://huggingface.co/learn/agents-course/en/unit1/introduction)                     | Definition of agents, LLMs, model family tree, and special tokens.                                                                     |
| 1 Bonus | [Fine-tuning an LLM for Function-calling](https://huggingface.co/learn/agents-course/bonus-unit1/introduction) | Learn how to fine-tune an LLM for Function-Calling                                                                                     |
| 2       | [Frameworks for AI Agents](https://huggingface.co/learn/agents-course/unit2/introduction)                      | Overview of `smolagents`, `LangGraph` and `LlamaIndex`.                                                                                |
| 2.1     | [The Smolagents Framework](https://huggingface.co/learn/agents-course/unit2/smolagents/introduction)           | Learn how to build effective agents using the `smolagents` library, a lightweight framework for creating capable AI agents.            |
| 2.2     | [The LlamaIndex Framework](https://huggingface.co/learn/agents-course/unit2/llama-index/introduction)          | Learn how to build LLM-powered agents over your data using indexes and workflows using the `LlamaIndex` toolkit.                       |
| 2.3     | [The LangGraph Framework](https://huggingface.co/learn/agents-course/unit2/langgraph/introduction)             | Learn how to build produc
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `huggingface_hub.md`
```markdown
# 📦 huggingface/huggingface_hub [🔖 PENDING/APPROVE]
🔗 https://github.com/huggingface/huggingface_hub
🌐 https://huggingface.co/docs/huggingface_hub

## Meta
- **Stars:** ⭐ 3448 | **Forks:** 🍴 971
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The official Python client for the Hugging Face Hub.

## README (trích đầu)
```
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/huggingface_hub-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/huggingface_hub.svg">
    <img alt="huggingface_hub library logo" src="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/huggingface_hub.svg" width="352" height="59" style="max-width: 100%">
  </picture>
  <br/>
  <br/>
</p> 

<p align="center">
    <i>The official Python client for the Huggingface Hub.</i>
</p>

<p align="center">
    <a href="https://huggingface.co/docs/huggingface_hub/en/index"><img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/huggingface_hub/index.svg?down_color=red&down_message=offline&up_message=online&label=doc"></a>
    <a href="https://github.com/huggingface/huggingface_hub/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/huggingface_hub.svg"></a>
    <a href="https://github.com/huggingface/huggingface_hub"><img alt="PyPi version" src="https://img.shields.io/pypi/pyversions/huggingface_hub.svg"></a>
    <a href="https://pypi.org/project/huggingface-hub"><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/huggingface_hub"></a>
    <a href="https://codecov.io/gh/huggingface/huggingface_hub"><img alt="Code coverage" src="https://codecov.io/gh/huggingface/huggingface_hub/branch/main/graph/badge.svg?token=RXP95LE2XL"></a>
</p>

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="https://github.com/huggingface/huggingface_hub/blob/main/i18n/README_de.md">Deutsch</a> |
        <a href="https://github.com/huggingface/huggingface_hub/blob/main/i18n/README_fr.md">Français</a> |
        <a href="https://github.com/huggingface/huggingface_hub/blob/main/i18n/README_hi.md">हिंदी</a> |
        <a href="https://github.com/huggingface/huggingface_hub/blob/main/i18n/README_ko.md">한국어</a> |
        <a href="https://github.com/huggingface/huggingface_hub/blob/main/i18n/README_cn.md">中文 (简体)</a>
    <p>
</h4>

---

**Documentation**: <a href="https://hf.co/docs/huggingface_hub" target="_blank">https://hf.co/docs/huggingface_hub</a>

**Source Code**: <a href="https://github.com/huggingface/huggingface_hub" target="_blank">https://github.com/huggingface/huggingface_hub</a>

---

## Welcome to the huggingface_hub library

The `huggingface_hub` library allows you to interact with the [Hugging Face Hub](https://huggingface.co/), a platform democratizing open-source Machine Learning for creators and collaborators. Discover pre-trained models and datasets for your projects or play with the thousands of machine learning apps hosted on the Hub. You can also create and share your own models, datasets and demos with the community. The `huggingface_hub` library provides a simple way to do all these things wit
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `lighteval.md`
```markdown
# 📦 huggingface/lighteval [🔖 PENDING/APPROVE]
🔗 https://github.com/huggingface/lighteval
🌐 https://huggingface.co/docs/lighteval/en/index

## Meta
- **Stars:** ⭐ 2360 | **Forks:** 🍴 444
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Lighteval is your all-in-one toolkit for evaluating LLMs across multiple backends

## README (trích đầu)
```
<p align="center">
  <br/>
    <img alt="lighteval library logo" src="./assets/lighteval-doc.svg" width="376" height="59" style="max-width: 100%;">
  <br/>
</p>


<p align="center">
    <i>Your go-to toolkit for lightning-fast, flexible LLM evaluation, from Hugging Face's Leaderboard and Evals Team.</i>
</p>

<div align="center">

[![Tests](https://github.com/huggingface/lighteval/actions/workflows/tests.yaml/badge.svg?branch=main)](https://github.com/huggingface/lighteval/actions/workflows/tests.yaml?query=branch%3Amain)
[![Quality](https://github.com/huggingface/lighteval/actions/workflows/quality.yaml/badge.svg?branch=main)](https://github.com/huggingface/lighteval/actions/workflows/quality.yaml?query=branch%3Amain)
[![Python versions](https://img.shields.io/pypi/pyversions/lighteval)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/huggingface/lighteval/blob/main/LICENSE)
[![Version](https://img.shields.io/pypi/v/lighteval)](https://pypi.org/project/lighteval/)

</div>

---

<p align="center">
  <a href="https://huggingface.co/docs/lighteval/main/en/index" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/Documentation-4F4F4F?style=for-the-badge&logo=readthedocs&logoColor=white" />
  </a>
  <a href="https://huggingface.co/spaces/OpenEvals/open_benchmark_index" target="_blank">
    <img alt="Open Benchmark Index" src="https://img.shields.io/badge/Open%20Benchmark%20Index-4F4F4F?style=for-the-badge&logo=huggingface&logoColor=white" />
  </a>
</p>

---

**Lighteval** is your *all-in-one toolkit* for evaluating LLMs across multiple
backends—whether your model is being **served somewhere** or **already loaded in memory**.
Dive deep into your model's performance by saving and exploring *detailed,
sample-by-sample results* to debug and see how your models stack-up.

*Customization at your fingertips*: letting you either browse all our existing tasks and [metrics](https://huggingface.co/docs/lighteval/metric-list) or effortlessly create your own [custom task](https://huggingface.co/docs/lighteval/adding-a-custom-task) and [custom metric](https://huggingface.co/docs/lighteval/adding-a-new-metric), tailored to your needs.


## Available Tasks

Lighteval supports **1000+ evaluation tasks** across multiple domains and
languages. Use [this
space](https://huggingface.co/spaces/OpenEvals/open_benchmark_index) to find what
you need, or, here's an overview of some *popular benchmarks*:


### 📚 **Knowledge**
- **General Knowledge**: MMLU, MMLU-Pro, MMMU, BIG-Bench
- **Question Answering**: TriviaQA, Natural Questions, SimpleQA, Humanity's Last Exam (HLE)
- **Specialized**: GPQA, AGIEval

### 🧮 **Math and Code**
- **Math Problems**: GSM8K, GSM-Plus, MATH, MATH500
- **Competition Math**: AIME24, AIME25
- **Multilingual Math**: MGSM (Grade School Math in 10+ languages)
- **Coding Benchmarks**: LCB (LiveCodeBench)

### 🎯 **Chat Model Evaluation**
- **Instruction Fo
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `peft.md`
```markdown
# 📦 huggingface/peft [🔖 PENDING/APPROVE]
🔗 https://github.com/huggingface/peft
🌐 https://huggingface.co/docs/peft

## Meta
- **Stars:** ⭐ 20851 | **Forks:** 🍴 2227
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🤗 PEFT: State-of-the-art Parameter-Efficient Fine-Tuning.

## README (trích đầu)
```
<!---
Copyright 2023 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

<h1 align="center"> <p>🤗 PEFT</p></h1>
<h3 align="center">
    <p>State-of-the-art Parameter-Efficient Fine-Tuning (PEFT) methods</p>
</h3>

Fine-tuning large pretrained models is often prohibitively costly due to their scale. Parameter-Efficient Fine-Tuning (PEFT) methods enable efficient adaptation of large pretrained models to various downstream applications by only fine-tuning a small number of (extra) model parameters instead of all the model's parameters. This significantly decreases the computational and storage costs. Recent state-of-the-art PEFT techniques achieve performance comparable to fully fine-tuned models.

PEFT is integrated with Transformers for easy model training and inference, Diffusers for conveniently managing different adapters, and Accelerate for distributed training and inference for really big models.

> [!TIP]
> Visit the [PEFT](https://huggingface.co/PEFT) organization to read about the PEFT methods implemented in the library and to see notebooks demonstrating how to apply these methods to a variety of downstream tasks. Click the "Watch repos" button on the organization page to be notified of newly implemented methods and notebooks!

Check the PEFT Adapters API Reference section for a list of supported PEFT methods, and read the [Adapters](https://huggingface.co/docs/peft/en/conceptual_guides/adapter), [Soft prompts](https://huggingface.co/docs/peft/en/conceptual_guides/prompting), and [IA3](https://huggingface.co/docs/peft/en/conceptual_guides/ia3) conceptual guides to learn more about how these methods work.

## Quickstart

Install PEFT from pip:

```bash
pip install peft
```

Prepare a model for training with a PEFT method such as LoRA by wrapping the base model and PEFT configuration with `get_peft_model`. For the bigscience/mt0-large model, you're only training 0.19% of the parameters!

```python
from transformers import AutoModelForCausalLM
from peft import LoraConfig, TaskType, get_peft_model

device = torch.accelerator.current_accelerator().type if hasattr(torch, "accelerator") else "cuda"
model_id = "Qwen/Qwen2.5-3B-Instruct"
model = AutoModelForCausalLM.from_pretrained(model_id, device_map=device)
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    task_type=TaskType.CAUSAL_LM,
    # target_modules=["q_proj", "v_proj", ...]  # optionally indicate target modules
)
model = get_peft_model(model, peft_config)
model.print_
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `skills.md`
```markdown
# 📦 huggingface/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/huggingface/skills
🌐 https://huggingface.co

## Meta
- **Stars:** ⭐ 9922 | **Forks:** 🍴 604
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Give your agents the power of the Hugging Face ecosystem

## README (trích đầu)
```
# Hugging Face Skills

Hugging Face Skills are definitions for AI/ML tasks like dataset creation, model training, and evaluation. They are interoperable with all major coding agent tools like OpenAI Codex, Anthropic's Claude Code, Google DeepMind's Gemini CLI, and Cursor.

The skills in this repository follow the standardized [Agent Skills](https://agentskills.io/home) format.

## How do Skills work?

In practice, skills are self-contained folders that package instructions, scripts, and resources together for an AI agent to use on a specific use case. Each folder includes a `SKILL.md` file with YAML frontmatter (name and description) followed by the guidance your coding agent follows while the skill is active. 

> [!NOTE]
> 'Skills' is actually an Anthropic term used within Claude AI and Claude Code and not adopted by other agent tools, but we love it! OpenAI Codex uses the open [Agent Skills](https://agentskills.io/specification) format, where each skill is a directory with a `SKILL.md` file that Codex discovers from standard `.agents/skills` locations documented in the [Codex Skills guide](https://developers.openai.com/codex/skills/). Codex can also work with an `AGENTS.md` file. Google Gemini uses 'extensions' to define the instructions for your coding agent in a `gemini-extension.json` file. **This repo is compatible with all of them, and more!**

> [!TIP]
> If your agent doesn't support skills, you can use [`agents/AGENTS.md`](../bmad_repo/agents.md) directly as a fallback.

## Installation

Hugging Face skills are compatible with Claude Code, Codex, Gemini CLI, and Cursor.

### Claude Code

1. Register the repository as a plugin marketplace:  
   
```
/plugin marketplace add huggingface/skills
```

2. To install a skill, run:  
   
```
/plugin install <skill-name>@huggingface/skills
```

For example:  

```
/plugin install hf-cli@huggingface/skills
```

### Codex

1. Copy or symlink any skills you want to use from this repository's `skills/` directory into one of Codex's standard `.agents/skills` locations (for example, `$REPO_ROOT/.agents/skills` or `$HOME/.agents/skills`) as described in the [Codex Skills guide](https://developers.openai.com/codex/skills/).

2. Once a skill is available in one of those locations, Codex will discover it using the Agent Skills standard and load the `SKILL.md` instructions when it decides to use that skill or when you explicitly invoke it.

3. If your Codex setup still relies on `AGENTS.md`, you can use the generated [`agents/AGENTS.md`](../bmad_repo/agents.md) file in this repo as a fallback bundle of instructions.

### Gemini CLI

1. This repo includes `gemini-extension.json` to integrate with the Gemini CLI.

2. Install locally:  

```
gemini extensions install . --consent
```

or use the GitHub URL:

```
gemini extensions install https://github.com/huggingface/skills.git --consent
```

4. See [Gemini CLI extensions docs](https://geminicli.com/docs/extensions/#installing-an-extension) for more help.

### Cursor

This
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `smolagents.md`
```markdown
# 📦 huggingface/smolagents [🔖 PENDING/APPROVE]
🔗 https://github.com/huggingface/smolagents
🌐 https://huggingface.co/docs/smolagents

## Meta
- **Stars:** ⭐ 26285 | **Forks:** 🍴 2403
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🤗 smolagents: a barebones library for agents that think in code.

## README (trích đầu)
```
<!---
Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->
<p align="center">
    <!-- Uncomment when CircleCI is set up
    <a href="https://circleci.com/gh/huggingface/accelerate"><img alt="Build" src="https://img.shields.io/circleci/build/github/huggingface/transformers/master"></a>
    -->
    <a href="https://github.com/huggingface/smolagents/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/huggingface/smolagents.svg?color=blue"></a>
    <a href="https://huggingface.co/docs/smolagents"><img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/smolagents/index.html.svg?down_color=red&down_message=offline&up_message=online"></a>
    <a href="https://github.com/huggingface/smolagents/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/smolagents.svg"></a>
    <a href="https://github.com/huggingface/smolagents/blob/main/CODE_OF_CONDUCT.md"><img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg"></a>
    <a href="https://deepwiki.com/huggingface/smolagents"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

<h3 align="center">
  <div style="display:flex;flex-direction:row;">
    <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/smolagents.png" alt="Hugging Face mascot as James Bond" width=400px>
    <p>Agents that think in code!</p>
  </div>
</h3>

`smolagents` is a library that enables you to run powerful agents in a few lines of code. It offers:

✨ **Simplicity**: the logic for agents fits in ~1,000 lines of code (see [agents.py](https://github.com/huggingface/smolagents/blob/main/src/smolagents/agents.py)). We kept abstractions to their minimal shape above raw code!

🧑‍💻 **First-class support for Code Agents**. Our [`CodeAgent`](https://huggingface.co/docs/smolagents/reference/agents#smolagents.CodeAgent) writes its actions in code (as opposed to "agents being used to write code"). To make it secure, we support executing in sandboxed environments via [Blaxel](https://blaxel.ai), [E2B](https://e2b.dev/), [Modal](https://modal.com/), Docker, or Pyodide+Deno WebAssembly sandbox.

🤗 **Hub integrations**: you can [share/pull tools or agents to/from the Hub](https://huggingface.co/docs/smolagents/reference/tools#smolagents.Tool.from_hub) for instant sharing of the most efficient agents!

🌐 **Model-agn
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `transformers.md`
```markdown
# 📦 huggingface/transformers [🔖 PENDING]
🔗 https://github.com/huggingface/transformers
🌐 https://huggingface.co/transformers

## Meta
- **Stars:** ⭐ 158447 | **Forks:** 🍴 32622
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training. 

## README (trích đầu)
```
<!---
Copyright 2020 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/transformers-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/transformers-logo-light.svg">
    <img alt="Hugging Face Transformers Library" src="https://huggingface.co/datasets/huggingface/documentation-images/raw/main/transformers-logo-light.svg" width="352" height="59" style="max-width: 100%;">
  </picture>
  <br/>
  <br/>
</p>

<p align="center">
    <a href="https://huggingface.com/models"><img alt="Checkpoints on Hub" src="https://img.shields.io/endpoint?url=https://huggingface.co/api/shields/models&color=brightgreen"></a>
    <a href="https://circleci.com/gh/huggingface/transformers"><img alt="Build" src="https://img.shields.io/circleci/build/github/huggingface/transformers/main"></a>
    <a href="https://github.com/huggingface/transformers/blob/main/LICENSE"><img alt="GitHub" src="https://img.shields.io/github/license/huggingface/transformers.svg?color=blue"></a>
    <a href="https://huggingface.co/docs/transformers/index"><img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/transformers/index.svg?down_color=red&down_message=offline&up_message=online"></a>
    <a href="https://github.com/huggingface/transformers/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/transformers.svg"></a>
    <a href="https://github.com/huggingface/transformers/blob/main/CODE_OF_CONDUCT.md"><img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg"></a>
    <a href="https://zenodo.org/badge/latestdoi/155220641"><img src="https://zenodo.org/badge/155220641.svg" alt="DOI"></a>
</p>

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_zh-hans.md">简体中文</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_zh-hant.md">繁體中文</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_ko.md">한국어</a> |
        <a href="https://github.com/huggingface/transformers/blob/main/i18n/README_es.md">Español</a> |
        <a href="https://github.com/huggingface/trans
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `trl.md`
```markdown
# 📦 huggingface/trl [🔖 PENDING/APPROVE]
🔗 https://github.com/huggingface/trl
🌐 http://hf.co/docs/trl

## Meta
- **Stars:** ⭐ 17798 | **Forks:** 🍴 2590
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Train transformer language models with reinforcement learning.

## README (trích đầu)
```
# TRL - Transformers Reinforcement Learning

<div style="text-align: center">
    <picture>
        <source media="(prefers-color-scheme: light)" srcset="https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/TRL%20banner%20light.png">
        <img src="https://huggingface.co/datasets/trl-lib/documentation-images/resolve/main/trl_banner_dark.png" alt="TRL Banner">
    </picture>
</div>

<hr> <br>

<h3 align="center">
    <p>A comprehensive library to post-train foundation models</p>
</h3>

<p align="center">
    <a href="https://github.com/huggingface/trl/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/huggingface/trl.svg?color=blue"></a>
    <a href="https://huggingface.co/docs/trl/index"><img alt="Documentation" src="https://img.shields.io/website?label=documentation&url=https%3A%2F%2Fhuggingface.co%2Fdocs%2Ftrl%2Findex&down_color=red&down_message=offline&up_color=blue&up_message=online"></a>
    <a href="https://github.com/huggingface/trl/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/trl.svg"></a>
    <a href="https://huggingface.co/trl-lib"><img alt="Hugging Face Hub" src="https://img.shields.io/badge/🤗%20Hub-trl--lib-yellow"></a>
</p>

## 🎉 What's New

**OpenEnv Integration:** TRL now supports **[OpenEnv](https://huggingface.co/blog/openenv)**, the open-source framework from Meta for defining, deploying, and interacting with environments in reinforcement learning and agentic workflows.

Explore how to seamlessly integrate TRL with OpenEnv in our [dedicated documentation](https://huggingface.co/docs/trl/openenv).

## Overview

TRL is a cutting-edge library designed for post-training foundation models using advanced techniques like Supervised Fine-Tuning (SFT), Group Relative Policy Optimization (GRPO), and Direct Preference Optimization (DPO). Built on top of the [🤗 Transformers](https://github.com/huggingface/transformers) ecosystem, TRL supports a variety of model architectures and modalities, and can be scaled-up across various hardware setups.

## Highlights

- **Trainers**: Various fine-tuning methods are easily accessible via trainers like [`SFTTrainer`](https://huggingface.co/docs/trl/sft_trainer), [`GRPOTrainer`](https://huggingface.co/docs/trl/grpo_trainer), [`DPOTrainer`](https://huggingface.co/docs/trl/dpo_trainer), [`RewardTrainer`](https://huggingface.co/docs/trl/reward_trainer) and more.

- **Efficient and scalable**:
  - Leverages [🤗 Accelerate](https://github.com/huggingface/accelerate) to scale from single GPU to multi-node clusters using methods like [DDP](https://pytorch.org/tutorials/intermediate/ddp_tutorial.html) and [DeepSpeed](https://github.com/deepspeedai/DeepSpeed).
  - Full integration with [🤗 PEFT](https://github.com/huggingface/peft) enables training on large models with modest hardware via quantization and LoRA/QLoRA.
  - Integrates [🦥 Unsloth](https://github.com/unslothai/unsloth) for accelerating training using opt
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


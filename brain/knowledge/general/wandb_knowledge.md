---
id: wandb-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.414328
---

# KNOWLEDGE EXTRACT: wandb
> **Extracted on:** 2026-03-30 18:01:15
> **Source:** wandb

---

## File: `wandb.md`
```markdown
# 📦 wandb/wandb [🔖 PENDING/APPROVE]
🔗 https://github.com/wandb/wandb
🌐 https://wandb.ai

## Meta
- **Stars:** ⭐ 10938 | **Forks:** 🍴 847
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The AI developer platform. Use Weights & Biases to train and fine-tune models, and manage models from experimentation to production.

## README (trích đầu)
```
<p align="center">
  <img src="./assets/logo.svg" width="600" alt="Weights & Biases" />
</p>

<p align="center">
<a href="https://pypi.python.org/pypi/wandb"><img src="https://img.shields.io/pypi/v/wandb" /></a>
<a href="https://anaconda.org/conda-forge/wandb"><img src="https://img.shields.io/conda/vn/conda-forge/wandb" /></a>
<a href="https://pypi.python.org/pypi/wandb"><img src="https://img.shields.io/pypi/pyversions/wandb" /></a>
<a href="https://circleci.com/gh/wandb/wandb"><img src="https://img.shields.io/circleci/build/github/wandb/wandb/main" /></a>
<a href="https://codecov.io/gh/wandb/wandb"><img src="https://img.shields.io/codecov/c/gh/wandb/wandb" /></a>
</p>
<p align='center'>
<a href="https://colab.research.google.com/github/wandb/examples/blob/master/colabs/intro/Intro_to_Weights_%26_Biases.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" /></a>
</p>

Use W&B to build better models faster. Track and visualize all the pieces of your machine learning pipeline, from datasets to production machine learning models. Get started with W&B today, [sign up for a W&B account](https://wandb.com?utm_source=github&utm_medium=code&utm_campaign=wandb&utm_content=readme)!

<br>

Building an LLM app? Track, debug, evaluate, and monitor LLM apps with [Weave](https://wandb.github.io/weave?utm_source=github&utm_medium=code&utm_campaign=wandb&utm_content=readme), our new suite of tools for GenAI.

&nbsp;

# Documentation

See the [W&B Developer Guide](https://docs.wandb.ai?utm_source=github&utm_medium=code&utm_campaign=wandb&utm_content=documentation) and [API Reference Guide](https://docs.wandb.ai/training/api-reference#api-overview?utm_source=github&utm_medium=code&utm_campaign=wandb&utm_content=documentation) for a full technical description of the W&B platform.

&nbsp;

# Quickstart

Install W&B to track, visualize, and manage machine learning experiments of any size.

## Install the wandb library

```shell
pip install wandb
```

## Sign up and create an API key

Sign up for a [W&B account](https://wandb.ai/login?utm_source=github&utm_medium=code&utm_campaign=wandb&utm_content=quickstart). Create a new API key at [wandb.ai/settings](https://wandb.ai/settings) and store it securely. Optionally, use the `wandb login` CLI to configure your API key on your machine. You can skip this step -- W&B will prompt you to create an API key the first time you use it.

**Note:** API keys can only be viewed once when created. Store your API key in a secure location like a password manager or environment variable.

## Create a machine learning training experiment

In your Python script or notebook, initialize a W&B run with `wandb.init()`.
Specify hyperparameters and log metrics and other information to W&B.

```python
import wandb

# Project that the run is recorded to
project = "my-awesome-project"

# Dictionary with hyperparameters
config = {"epochs": 1337, "lr": 3e-4}

# The `with` syntax marks the run as finished upon exiting the `with` 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `weave.md`
```markdown
# 📦 wandb/weave [🔖 PENDING/APPROVE]
🔗 https://github.com/wandb/weave
🌐 https://wandb.me/weave

## Meta
- **Stars:** ⭐ 1064 | **Forks:** 🍴 150
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Weave is a toolkit for developing AI-powered applications, built by Weights & Biases.

## README (trích đầu)
```
# **Weave by Weights & Biases**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://wandb.me/weave_colab)
[![Stable Version](https://img.shields.io/pypi/v/weave?color=green)](https://pypi.org/project/weave)
[![Download Stats](https://img.shields.io/pypi/dm/weave)](https://pypistats.org/packages/weave)
[![Github Checks](https://img.shields.io/github/check-runs/wandb/weave/master
)](https://github.com/wandb/weave)
[![codecov](https://codecov.io/gh/wandb/weave/graph/badge.svg?token=YOUR_TOKEN)](https://codecov.io/gh/wandb/weave)

Weave is a toolkit for developing Generative AI applications, built by [Weights & Biases](https://wandb.ai/).

---

You can use Weave to:

- **Log and debug** language model inputs, outputs, and traces
- **Build rigorous, apples-to-apples evaluations** for language model use cases
- **Organize all the information** generated across the LLM workflow, from experimentation to evaluations to production

Our goal is to bring rigor, best-practices, and composability to the inherently experimental process of developing Generative AI software, without introducing cognitive overhead.

## Documentation

Our documentation site can be found [here](https://wandb.me/weave).

## Prerequisites

- Python 3.10 or higher
- A [Weights & Biases account](https://wandb.ai/signup) (free tier available)


## Quick Start

1. **Install Weave**:
   ```bash
   pip install weave
   ```

2. **Import and initialize**:
   ```python
   import weave
   weave.init("my-project-name")
   ```

3. **Trace your functions**:
   ```python
   @weave.op
   def my_function():
       # Your tracked code!
       pass
   ```

## Usage

### Tracing
You can trace any function using `weave.op` - from api calls to OpenAI, Anthropic, Google AI Studio etc to generation calls from Hugging Face and other open source models to any other validation functions or data transformations in your code you'd like to keep track of.

Decorate all the functions you want to trace, this will generate a trace tree of the inputs and outputs of all your functions:

```python
import weave
weave.init("weave-example")

@weave.op
def sum_nine(value_one: int):
    return value_one + 9

@weave.op
def multiply_two(value_two: int):
    return value_two * 2

@weave.op
def main():
    output = sum_nine(3)
    final_output = multiply_two(output)
    return final_output

main()
```

### Fuller Example 

```python
import weave
import json
from openai import OpenAI

@weave.op
def extract_fruit(sentence: str) -> dict:
    client = OpenAI()

    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {
            "role": "system",
            "content": "You will be provided with unstructured data, and your task is to parse it one JSON dictionary with fruit, color and flavor as keys."
        },
        {
            "role": "user",
            "content": sentence
        }
        ],
        temperature=0.7,
        response_format={ "ty
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


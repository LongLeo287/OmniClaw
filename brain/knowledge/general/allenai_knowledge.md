---
id: allenai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:46.264444
---

# KNOWLEDGE EXTRACT: allenai
> **Extracted on:** 2026-03-30 17:29:07
> **Source:** allenai

---

## File: `RL4LMs.md`
```markdown
# 📦 allenai/RL4LMs [🔖 PENDING/APPROVE]
🔗 https://github.com/allenai/RL4LMs
🌐 https://rl4lms.apps.allenai.org/

## Meta
- **Stars:** ⭐ 2382 | **Forks:** 🍴 202
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A modular RL library to fine-tune language models to human preferences

## README (trích đầu)
```
<p align="center">
  <img src="RL4LMs_logo.png" width=512px>
</p>

<h1 align="center"> :robot: RL4LMs :rocket: </h1>

<h3 align="center"> A modular RL library to fine-tune language models to human preferences </h3>

<br>

We provide easily customizable building blocks for training language models including implementations of **on-policy algorithms**, **reward functions**, **metrics**, **datasets** and **LM based actor-critic policies**

Paper Link: https://arxiv.org/abs/2210.01241

Website Link: https://rl4lms.apps.allenai.org/

Thoroughly **tested** and **benchmarked** with over **2000 experiments** :fire: (GRUE benchmark :trophy:) on a comprehensive set of: 
- 7 different Natural Language Processing (NLP) Tasks:
    - Summarization
    - Generative Commonsense Reasoning
    - IMDB Sentiment-based Text Continuation
    - Table-to-text generation
    - Abstractive Question Answering
    - Machine Translation
    - Dialogue Generation
- Different types of NLG metrics (20+) which can be used as reward functions:
    - Lexical Metrics (eg: ROUGE, BLEU, SacreBLEU, METEOR)
    - Semantic Metrics (eg: BERTSCORE, BLEURT)
    - Task specific metrics (eg: PARENT, CIDER, SPICE)
    - Scores from pre-trained classifiers (eg: Sentiment scores)
- On-policy algorithms of PPO, A2C, TRPO and novel **NLPO (Natural Language Policy Optimization)**
- Actor-Critic Policies supporting causal LMs (eg. GPT-2/3) and seq2seq LMs (eg. T5, BART)

All of these building blocks can be customizable allowing users to train transformer-based LMs to optimize any arbitrary reward function on any dataset of their choice.

## Recent updates (v0.2.0) on 23-Nov-22
- Added daily dialog task
- Fixed compatibility issues with some Seq2seq models such as BART, blendorbot etc
- Implemented data parallel support
- Refactored policy classes

## Recent updates (v0.2.1) 
- Minor logging updates

---
# Install

## Local Installation 
```bash
git clone https://github.com/allenai/RL4LMs.git
cd RL4LMs
pip install -e .
```

## Docker
We provide also a Dockerfile for development using docker containers containing all the dependencies.
```bash
docker build . -t rl4lms
```

## Additional dependencies

Optionally, coreNLP libraries are required for certain metric computations (eg. SPICE) which can be downloaded through `cd rl4lms/envs/text_generation/caption_metrics/spice && bash get_stanford_models.sh`

---
# Quick Start - Train PPO/NLPO using pre-defined YAML configs
We provide a simple training API that can be invoked via train [script](https://github.com/allenai/RL4LMs/blob/main/scripts/training/train_text_generation.py) that allows to train PPO, NLPO or a supervised model by using a config file (YAML). 

For example, to train T5-base on CNN/DM summarization on PPO using Rouge-1 as reward function, you can run:

```bash
python scripts/training/train_text_generation.py --config_path scripts/training/task_configs/summarization/t5_ppo.yml
```

Config files for all tasks can be found [here](https://gith
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


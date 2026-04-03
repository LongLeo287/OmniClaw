---
id: moonshotai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:09.721105
---

# KNOWLEDGE EXTRACT: MoonshotAI
> **Extracted on:** 2026-03-30 17:43:02
> **Source:** MoonshotAI

---

## File: `kimi-cli.md`
```markdown
# 📦 MoonshotAI/kimi-cli [🔖 PENDING/APPROVE]
🔗 https://github.com/MoonshotAI/kimi-cli
🌐 https://moonshotai.github.io/kimi-cli/

## Meta
- **Stars:** ⭐ 7383 | **Forks:** 🍴 763
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Kimi Code CLI is your next CLI agent.

## README (trích đầu)
```
# Kimi Code CLI

[![Commit Activity](https://img.shields.io/github/commit-activity/w/MoonshotAI/kimi-cli)](https://github.com/MoonshotAI/kimi-cli/graphs/commit-activity)
[![Checks](https://img.shields.io/github/check-runs/MoonshotAI/kimi-cli/main)](https://github.com/MoonshotAI/kimi-cli/actions)
[![Version](https://img.shields.io/pypi/v/kimi-cli)](https://pypi.org/project/kimi-cli/)
[![Downloads](https://img.shields.io/pypi/dw/kimi-cli)](https://pypistats.org/packages/kimi-cli)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/MoonshotAI/kimi-cli)

[Kimi Code](https://www.kimi.com/code/) | [Documentation](https://moonshotai.github.io/kimi-cli/en/) | [文档](https://moonshotai.github.io/kimi-cli/zh/)

Kimi Code CLI is an AI agent that runs in the terminal, helping you complete software development tasks and terminal operations. It can read and edit code, execute shell commands, search and fetch web pages, and autonomously plan and adjust actions during execution.

## Getting Started

See [Getting Started](https://moonshotai.github.io/kimi-cli/en/guides/getting-started.html) for how to install and start using Kimi Code CLI.

## Key Features

### Shell command mode

Kimi Code CLI is not only a coding agent, but also a shell. You can switch the shell command mode by pressing `Ctrl-X`. In this mode, you can directly run shell commands without leaving Kimi Code CLI.

![](./docs/media/shell-mode.gif)

> [!NOTE]
> Built-in shell commands like `cd` are not supported yet.

### VS Code extension

Kimi Code CLI can be integrated with [Visual Studio Code](https://code.visualstudio.com/) via the [Kimi Code VS Code Extension](https://marketplace.visualstudio.com/items?itemName=moonshot-ai.kimi-code).

![VS Code Extension](./docs/media/vscode.png)

### IDE integration via ACP

Kimi Code CLI supports [Agent Client Protocol] out of the box. You can use it together with any ACP-compatible editor or IDE.

[Agent Client Protocol]: https://github.com/agentclientprotocol/agent-client-protocol

To use Kimi Code CLI with ACP clients, make sure to run Kimi Code CLI in the terminal and send `/login` to complete the login first. Then, you can configure your ACP client to start Kimi Code CLI as an ACP agent server with command `kimi acp`.

For example, to use Kimi Code CLI with [Zed](https://zed.dev/) or [JetBrains](https://blog.jetbrains.com/ai/2025/12/bring-your-own-ai-agent-to-jetbrains-ides/), add the following configuration to your `~/.config/zed/settings.json` or `~/.jetbrains/acp.json` file:

```json
{
  "agent_servers": {
    "Kimi Code CLI": {
      "type": "custom",
      "command": "kimi",
      "args": ["acp"],
      "env": {}
    }
  }
}
```

Then you can create Kimi Code CLI threads in IDE's agent panel.

![](./docs/media/acp-integration.gif)

### Zsh integration

You can use Kimi Code CLI together with Zsh, to empower your shell experience with AI agent capabilities.

Install the [zsh-kimi-cli](https://github.com/MoonshotAI/zsh-kimi-cli) plug
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `WorldVQA.md`
```markdown
# 📦 MoonshotAI/WorldVQA [🔖 PENDING/APPROVE]
🔗 https://github.com/MoonshotAI/WorldVQA


## Meta
- **Stars:** ⭐ 110 | **Forks:** 🍴 2
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# WorldVQA
## WorldVQA: Measuring Atomic World Knowledge in Multimodal Large Language Models

[<img src="images/kimi_small.png" width="16" height="16" style="vertical-align: middle;"> HomePage](https://worldvqa2026.github.io/WorldVQA/) | [🤗 Dataset](https://huggingface.co/datasets/moonshotai/WorldVQA) | [<img src="images/arxiv_small.svg" width="16" height="16" style="vertical-align: middle;"> Paper](https://arxiv.org/abs/2602.02537v1) | [<img src="images/github_small.svg" width="16" height="16" style="vertical-align: middle;"> Code](https://github.com/MoonshotAI/WorldVQA/)


![alt text](images/barchart.png)

## Abstract
We introduce WorldVQA, a benchmark designed to evaluate the atomic vision-centric world knowledge of Multimodal Large Language Models (MLLMs). Current evaluations often conflate visual knowledge retrieval with reasoning. In contrast, WorldVQA decouples these capabilities to strictly measure "what the model memorizes." The benchmark assesses the atomic capability of grounding and naming visual entities across a stratified taxonomy, spanning from common head-class objects to long-tail rarities. We expect WorldVQA serves as a rigorous test for visual factuality, thereby establishing a standard for assessing the encyclopedic breadth and hallucination rates of current and next-generation frontier models.
<img src="images/main_figure.jpg">

## Details

**WorldVQA** is a meticulously curated benchmark designed to evaluate atomic vision-centric world knowledge in Multimodal Large Language Models (MLLMs). The dataset comprises **3,500 VQA pairs** across **9 categories**, with careful attention to linguistic and cultural diversity.


![alt text](images/statistics.png)

## Quick Start: Evaluate Your Model

We've made evaluating your model on WorldVQA incredibly simple! Just follow these steps:

### 1. Install Dependencies

```bash
git clone https://github.com/runjieovo/WorldVQA-code.git
cd WorldVQA-code
pip install -r requirements.txt
```

### 2. Configure Your API Key

Option A (Recommended): Set environment variable
```bash
export OPENAI_API_KEY='[REDACTED_API_KEY]'
```

Option B: Use a .env file
```bash
cp .env.example .env
# Edit .env with your API key and preferred model
```

Option C: Directly edit the config in `eval/eval.py`

### 3. Prepare Dataset

Ensure you have `WorldVQA.tsv` in the project root.

### Configuration Options

You can customize these via environment variables or in `eval/eval.py`:

| Setting | Default | Description |
|---------|---------|-------------|
| `OPENAI_API_KEY` | Required | Your API key |
| `MODEL_NAME` | `Kimi-K2.5` | Model to evaluate |
| `JUDGE_MODEL` | `gpt-oss-120b` | Model for judging answers |
| `MAX_RETRIES` | `3` | API retry attempts |

### 4. Run Evaluation

```bash
cd eval
python eval.py
```

That's it! Your results will be saved in the `results/` directory.

## Leaderboard

Our evaluation reveals significant gaps in visual encyclopedic knowledge, with no model surpassing the 50% accuracy thresho
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


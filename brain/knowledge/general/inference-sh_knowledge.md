---
id: inference-sh-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:53.278735
---

# KNOWLEDGE EXTRACT: inference-sh
> **Extracted on:** 2026-03-30 17:38:09
> **Source:** inference-sh

---

## File: `skills.md`
```markdown
# 📦 inference-sh/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/inference-sh/skills


## Meta
- **Stars:** ⭐ 228 | **Forks:** 🍴 37
- **Language:** Shell | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
inference.sh Agent skills for using our API to give your agents access to hundreds of apps and other agents

## README (trích đầu)
```
# inference.sh skills

AI agent skills for 150+ models via [inference.sh](https://inference.sh) CLI. Generate images, videos, call LLMs, search the web, and more.

![inference.sh](https://cloud.inference.sh/app/files/u/4mg21r6ta37mpaz6ktzwtt8krr/01kgvqa60jjrqa47j3g5s6ce6v.jpeg)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Contents

- [Install as Claude Code Plugin](#claude-code-plugin)
- [Install as Skills](#install-as-skills)
- [CLI Setup](#cli-setup)
- [Available Skills](#available-skills)
- [Documentation](#documentation)

---

## Claude Code Plugin

Install all skills as a Claude Code plugin:

```bash
/plugin install inference-sh
```

Or add from GitHub:

```bash
/plugin marketplace add inference-sh/skills
/plugin install inference-sh@inference-sh-skills
```

After install, skills are available as `/inference-sh:flux-image`, `/inference-sh:google-veo`, etc.

---

## Install as Skills

### All Skills

```bash
npx skills add inference-sh/skills
```

### Specific Skills

```bash
npx skills add inference-sh/skills@flux-image
npx skills add inference-sh/skills@google-veo
npx skills add inference-sh/skills@llm-models
npx skills add inference-sh/skills@web-search
```

### Manual

```bash
cp -r tools/* ui/* sdk/* guides/* ~/.claude/skills/
```

---

## CLI Setup

> Requires inference.sh CLI (`infsh`). [Install instructions](https://raw.githubusercontent.com/inference-sh/skills/refs/heads/main/cli-install.md)

```bash
infsh login
```

Browse apps: `infsh app list`

---

## Available Skills

### Tools

| Skill | Description |
|-------|-------------|
| [ai-image-generation](tools/image/) | 50+ image models (FLUX, Gemini, Reve, etc.) |
| [ai-video-generation](tools/video/) | 40+ video models (Veo, Seedance, Wan, etc.) |
| [llm-models](tools/llm/) | Claude, Gemini, Kimi, GLM |
| [web-search](tools/llm/) | Tavily, Exa search |
| [twitter-automation](tools/social/) | X/Twitter API |

### SDKs

| Skill | Description |
|-------|-------------|
| [javascript-sdk](sdk/javascript-sdk/) | JS/TS SDK with streaming, tools, React |
| [python-sdk](sdk/python-sdk/) | Python SDK with async, streaming |

### UI Components

| Skill | Description |
|-------|-------------|
| [agent-ui](ui/agent-ui/) | Full agent interface |
| [chat-ui](ui/chat-ui/) | Chat components |
| [tools-ui](ui/tools-ui/) | Tool call/result rendering |

### Guides

| Category | Topics |
|----------|--------|
| [prompting](guides/prompting/) | Prompt engineering, video prompts |
| [design](guides/design/) | Landing pages, thumbnails, logos |
| [video](guides/video/) | Storyboards, explainers, ads |
| [writing](guides/writing/) | Blogs, case studies, newsletters |
| [social](guides/social/) | LinkedIn, Twitter threads, carousels |
| [product](guides/product/) | Competitor analysis, personas, launches |

---

## Documentation

- [Getting Started](https://inference.sh/docs/getting-started/introduction)
- [Running Apps](https://inference.s
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


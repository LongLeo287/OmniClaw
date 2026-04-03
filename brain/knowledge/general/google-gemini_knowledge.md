---
id: google-gemini-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.809746
---

# KNOWLEDGE EXTRACT: google-gemini
> **Extracted on:** 2026-03-30 17:38:00
> **Source:** google-gemini

---

## File: `gemini-cli.md`
```markdown
# 📦 google-gemini/gemini-cli [🔖 PENDING]
🔗 https://github.com/google-gemini/gemini-cli
🌐 https://geminicli.com

## Meta
- **Stars:** ⭐ 99189 | **Forks:** 🍴 12641
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
An open-source AI agent that brings the power of Gemini directly into your terminal.

## README (trích đầu)
```
# Gemini CLI

[![Gemini CLI CI](https://github.com/google-gemini/gemini-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/google-gemini/gemini-cli/actions/workflows/ci.yml)
[![Gemini CLI E2E (Chained)](https://github.com/google-gemini/gemini-cli/actions/workflows/chained_e2e.yml/badge.svg)](https://github.com/google-gemini/gemini-cli/actions/workflows/chained_e2e.yml)
[![Version](https://img.shields.io/npm/v/@google/gemini-cli)](https://www.npmjs.com/package/@google/gemini-cli)
[![License](https://img.shields.io/github/license/google-gemini/gemini-cli)](https://github.com/google-gemini/gemini-cli/blob/main/LICENSE)
[![View Code Wiki](https://assets.codewiki.google/readme-badge/static.svg)](https://codewiki.google/github.com/google-gemini/gemini-cli?utm_source=badge&utm_medium=github&utm_campaign=github.com/google-gemini/gemini-cli)

![Gemini CLI Screenshot](/docs/assets/gemini-screenshot.png)

Gemini CLI is an open-source AI agent that brings the power of Gemini directly
into your terminal. It provides lightweight access to Gemini, giving you the
most direct path from your prompt to our model.

Learn all about Gemini CLI in our [documentation](https://geminicli.com/docs/).

## 🚀 Why Gemini CLI?

- **🎯 Free tier**: 60 requests/min and 1,000 requests/day with personal Google
  account.
- **🧠 Powerful Gemini 3 models**: Access to improved reasoning and 1M token
  context window.
- **🔧 Built-in tools**: Google Search grounding, file operations, shell
  commands, web fetching.
- **🔌 Extensible**: MCP (Model Context Protocol) support for custom
  integrations.
- **💻 Terminal-first**: Designed for developers who live in the command line.
- **🛡️ Open source**: Apache 2.0 licensed.

## 📦 Installation

See
[Gemini CLI installation, execution, and releases](installation.md)
for recommended system specifications and a detailed installation guide.

### Quick Install

#### Run instantly with npx

```bash
# Using npx (no installation required)
npx @google/gemini-cli
```

#### Install globally with npm

```bash
npm install -g @google/gemini-cli
```

#### Install globally with Homebrew (macOS/Linux)

```bash
brew install gemini-cli
```

#### Install globally with MacPorts (macOS)

```bash
sudo port install gemini-cli
```

#### Install with Anaconda (for restricted environments)

```bash
# Create and activate a new environment
conda create -y -n gemini_env -c conda-forge nodejs
conda activate gemini_env

# Install Gemini CLI globally via npm (inside the environment)
npm install -g @google/gemini-cli
```

## Release Cadence and Tags

See [Releases](../../../core/security/QUARANTINE/incoming/repos/alasql/RELEASES.md) for more details.

### Preview

New preview releases will be published each week at UTC 23:59 on Tuesdays. These
releases will not have been fully vetted and may contain regressions or other
outstanding issues. Please help us test and install with `preview` tag.

```bash
npm install -g @google/gemini-cli@preview
```

### Stable

- New stable releases will be published each
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `gemini-skills.md`
```markdown
# 📦 google-gemini/gemini-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/google-gemini/gemini-skills
🌐 https://ai.google.dev/gemini-api/docs

## Meta
- **Stars:** ⭐ 2470 | **Forks:** 🍴 219
- **Language:** N/A | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Skills for the Gemini API, SDK and model/agent interactions

## README (trích đầu)
```
# Gemini API skills

A library of skills for the Gemini API, SDK and model interactions.

## About

LLMs have fixed knowledge, being trained at a specific point in time. Software
dev is fast paced and changes often, where new libraries are launched every day
and best practices evolve quickly.

This leaves a knowledge gap that language models can't solve on their own. For
example, models don't know about themselves when they're trained, and they
aren't necessarily aware of subtle changes in best practices (like [thought
circulation](https://ai.google.dev/gemini-api/docs/thinking#signatures)) or SDK
changes.

[Skills](https://agentskills.io/) are a lightweight technique for adding
relevant context to your agents. This repo contains skills related to building
apps powered by the Gemini API.

### Performance

Our evaluations found that adding this skill improved an agent's ability to
generate correct API code following best practices to 87% with Gemini 3 Flash
and 96% with Gemini 3 Pro.

## Skills in this repo

| Skill | Description |
| :--- | :--- |
| [`gemini-api-dev`](skills/gemini-api-dev) | Skill for developing Gemini-powered apps. Provides the best practices for building apps that use the Gemini API. |
| [`vertex-ai-api-dev`](skills/vertex-ai-api-dev) | Skill for developing Gemini-powered apps on Google Cloud Vertex AI using the Gen AI SDK. Covers tools, multimodal generation, caching, and batch prediction. |
| [`gemini-live-api-dev`](skills/gemini-live-api-dev) | Skill for building real-time, bidirectional streaming apps with the Gemini Live API. Covers WebSocket-based audio/video/text streaming, voice activity detection, native audio features, function calling, and session management. |
| [`gemini-interactions-api`](skills/gemini-interactions-api) | Skill for building apps with the [Gemini Interactions API](https://ai.google.dev/gemini-api/docs/interactions?ua=chat). Covers text generation, multi-turn chat, streaming, function calling, structured output, image generation, Deep Research agents, deprecated model guardrails, and both Python and TypeScript SDKs. |

## Installation

You can browse and install skills using either the [Vercel skills CLI](https://skills.sh) or the [Context7 skills CLI](https://context7.com).

### Using [Vercel skills CLI](https://skills.sh)

```sh
# Interactively browse and install skills.
npx skills add google-gemini/gemini-skills --list

# Install a specific skill (e.g., gemini-api-dev).
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

### Using [Context7 skills CLI](https://context7.com)

```sh
# Interactively browse and install skills.
npx ctx7 skills install /google-gemini/gemini-skills

# Install a specific skill (e.g., vertex-ai-api-dev).
npx ctx7 skills install /google-gemini/gemini-skills vertex-ai-api-dev
```

## Disclaimer

This is not an officially supported Google product. This project is not
eligible for the [Google Open Source Software Vulnerability Rewards
Program](https
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


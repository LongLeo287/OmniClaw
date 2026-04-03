---
id: shareai-lab-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.179570
---

# KNOWLEDGE EXTRACT: shareAI-lab
> **Extracted on:** 2026-03-30 17:53:19
> **Source:** shareAI-lab

---

## File: `claw0.md`
```markdown
# 📦 shareAI-lab/claw0 [🔖 PENDING/APPROVE]
🔗 https://github.com/shareAI-lab/claw0


## Meta
- **Stars:** ⭐ 1530 | **Forks:** 🍴 144
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
0 - 1 learn OpenClaw: sections to build an claw-AI agent from scratch

## README (trích đầu)
```
[English](README.md) | [中文](README.zh.md) | [日本語](README.ja.md)  
# claw0


**From Zero to One: Build an AI Agent Gateway**

> 10 progressive sections -- every section is a single, runnable Python file.
> 3 languages (English, Chinese, Japanese) -- code + docs co-located.

---

## What is this?

Most agent tutorials stop at "call an API once." This repository starts from that while loop and takes you all the way to a production-grade gateway.

Build a minimal AI agent gateway from scratch, section by section. 10 sections, 10 core concepts, ~7,000 lines of Python. Each section introduces exactly one new idea while keeping all prior code intact. After all 10, you can read OpenClaw's production codebase with confidence.

```sh
s01: Agent Loop           -- The foundation: while + stop_reason
s02: Tool Use             -- Let the model call tools: dispatch table
s03: Sessions & Context   -- Persist conversations, handle overflow
s04: Channels             -- Telegram + Feishu: real channel pipelines
s05: Gateway & Routing    -- 5-tier binding, session isolation
s06: Intelligence         -- Soul, memory, skills, prompt assembly
s07: Heartbeat & Cron     -- Proactive agent + scheduled tasks
s08: Delivery             -- Reliable message queue with backoff
s09: Resilience           -- 3-layer retry onion + auth profile rotation
s10: Concurrency          -- Named lanes serialize the chaos
```

## Architecture

```
+------------------- claw0 layers -------------------+
|                                                     |
|  s10: Concurrency  (named lanes, generation track)  |
|  s09: Resilience   (auth rotation, overflow compact)|
|  s08: Delivery     (write-ahead queue, backoff)     |
|  s07: Heartbeat    (lane lock, cron scheduler)      |
|  s06: Intelligence (8-layer prompt, hybrid memory)  |
|  s05: Gateway      (WebSocket, 5-tier routing)      |
|  s04: Channels     (Telegram pipeline, Feishu hook) |
|  s03: Sessions     (JSONL persistence, 3-stage retry)|
|  s02: Tools        (dispatch table, 4 tools)        |
|  s01: Agent Loop   (while True + stop_reason)       |
|                                                     |
+-----------------------------------------------------+
```

## Section Dependencies

```
s01 --> s02 --> s03 --> s04 --> s05
                 |               |
                 v               v
                s06 ----------> s07 --> s08
                 |               |
                 v               v
                s09 ----------> s10
```

- s01-s02: Foundation (no dependencies)
- s03: Builds on s02 (adds persistence to the tool loop)
- s04: Builds on s03 (channels produce InboundMessages for sessions)
- s05: Builds on s04 (routes channel messages to agents)
- s06: Builds on s03 (uses sessions for context, adds prompt layers)
- s07: Builds on s06 (heartbeat uses soul/memory for prompt)
- s08: Builds on s07 (heartbeat output flows through delivery queue)
- s09: Builds on s03+s06 (reuses ContextGuard for overflow, model config)
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `kode-agent-sdk.md`
```markdown
# 📦 shareAI-lab/kode-agent-sdk [🔖 PENDING/APPROVE]
🔗 https://github.com/shareAI-lab/kode-agent-sdk


## Meta
- **Stars:** ⭐ 251 | **Forks:** 🍴 53
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
runtime for building Claude Code & Manus like Agent Product

## README (trích đầu)
```
# KODE SDK

[English](./README.md) | [中文](./README.zh-CN.md)

> Event-driven, long-running AI Agent framework with enterprise-grade persistence and multi-agent collaboration.

## Features

- **Event-Driven Architecture** - Three-channel system (Progress/Control/Monitor) for clean separation of concerns
- **Long-Running & Resumable** - Seven-stage checkpoints with Safe-Fork-Point for crash recovery
- **Multi-Agent Collaboration** - AgentPool, Room messaging, and task delegation
- **Enterprise Persistence** - SQLite/PostgreSQL support with unified WAL
- **Cloud Sandbox** - [E2B](https://e2b.dev) and OpenSandbox integration for isolated remote code execution
- **Extensible Ecosystem** - MCP tools, custom Providers, Skills system

## Quick Start

**One-liner setup** (install dependencies and build):

```bash
./quickstart.sh
```

Or install as a dependency:

```bash
npm install @shareai-lab/kode-sdk
```

Set environment variables:

<!-- tabs:start -->
#### **Linux / macOS**
```bash
export ANTHROPIC_API_KEY=sk-...
export ANTHROPIC_MODEL_ID=claude-sonnet-4-20250514  # optional, default: claude-sonnet-4-20250514
export ANTHROPIC_BASE_URL=https://api.anthropic.com  # optional, default: https://api.anthropic.com
```

#### **Windows (PowerShell)**
```powershell
$env:ANTHROPIC_API_KEY='[REDACTED_API_KEY]'
$env:ANTHROPIC_MODEL_ID="claude-sonnet-4-20250514"  # optional, default: claude-sonnet-4-20250514
$env:ANTHROPIC_BASE_URL="https://api.anthropic.com"  # optional, default: https://api.anthropic.com
```
<!-- tabs:end -->

Minimal example:

```typescript
import { Agent, AnthropicProvider, JSONStore } from '@shareai-lab/kode-sdk';

const provider = new AnthropicProvider(
  process.env.ANTHROPIC_API_KEY!,
  process.env.ANTHROPIC_MODEL_ID
);

const agent = await Agent.create({
  provider,
  store: new JSONStore('./.kode'),
  systemPrompt: 'You are a helpful assistant.'
});

// Subscribe to progress events
for await (const envelope of agent.subscribe(['progress'])) {
  if (envelope.event.type === 'text_chunk') {
    process.stdout.write(envelope.event.delta);
  }
  if (envelope.event.type === 'done') break;
}

await agent.send('Hello!');
```

Run examples:

```bash
npm run example:getting-started    # Minimal chat
npm run example:agent-inbox        # Event-driven inbox
npm run example:approval           # Tool approval workflow
npm run example:room               # Multi-agent collaboration
npm run example:opensandbox        # OpenSandbox basic usage
```

OpenSandbox quick config:

```bash
export OPEN_SANDBOX_API_KEY=...                      # optional (required only when auth is enabled)
export OPEN_SANDBOX_ENDPOINT=http://127.0.0.1:8080  # optional
export OPEN_SANDBOX_IMAGE=ubuntu                     # optional
```

## Architecture for Scale

For production deployments serving many users, we recommend the **Worker Microservice Pattern**:

```
                        +------------------+
                        |    Frontend      |  Next.js / SvelteKit (Vercel OK)
          
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `Kode-Agent.md`
```markdown
# 📦 shareAI-lab/Kode-Agent [🔖 PENDING/APPROVE]
🔗 https://github.com/shareAI-lab/Kode-Agent


## Meta
- **Stars:** ⭐ 4714 | **Forks:** 🍴 708
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Kode Agent — Design for post-human workflows. One unit agent for every human & computer task.

## README (trích đầu)
```
# Kode - AI Coding
<img width="991" height="479" alt="image" src="https://github.com/user-attachments/assets/c1751e92-94dc-4e4a-9558-8cd2d058c1a1" />  <br> 
[![npm version](https://badge.fury.io/js/@shareai-lab%2Fkode.svg)](https://www.npmjs.com/package/@shareai-lab/kode)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![AGENTS.md](https://img.shields.io/badge/AGENTS.md-Compatible-brightgreen)](https://agents.md)

[中文文档](README.zh-CN.md) | [Contributing](CONTRIBUTING.md) | [Documentation](docs/README.md)

<img width="90%" alt="image" src="https://github.com/user-attachments/assets/fdce7017-8095-429d-b74e-07f43a6919e1" />

<img width="90%" alt="2c0ad8540f2872d197c7b17ae23d74f5" src="https://github.com/user-attachments/assets/f220cc27-084d-468e-a3f4-d5bc44d84fac" />

<img width="90%" alt="f266d316d90ddd0db5a3d640c1126930" src="https://github.com/user-attachments/assets/90ec7399-1349-4607-b689-96613b3dc3e2" />


<img width="90%" alt="image" src="https://github.com/user-attachments/assets/b30696ce-5ab1-40a0-b741-c7ef3945dba0" />


## 📢 Update Log

**2025-12-22**: Native-first distribution (Windows OOTB). Kode prefers a cached native binary and falls back to the Node.js runtime when needed. See `docs/binary-distribution.md`.


## 🤝 AGENTS.md Standard Support

Kode supports the [AGENTS.md standard](https://agents.md): a simple, open format for guiding coding agents, used by 60k+ open-source projects.

### Full Compatibility with Multiple Standards

- ✅ **AGENTS.md** - Native support for the OpenAI-initiated standard format
- ✅ **Legacy `.claude` compatibility** - Reads `.claude` directories and `CLAUDE.md` when present (see `docs/compatibility.md`)
- ✅ **Subagent System** - Advanced agent delegation and task orchestration
- ✅ **Cross-platform** - Works with 20+ AI models and providers

Use `# Your documentation request` to generate and maintain your AGENTS.md file automatically, while preserving compatibility with existing `.claude` workflows.

### Instruction Discovery (Codex-compatible)

- Kode reads project instructions by walking from the Git repo root → current working directory.
- In each directory, it prefers `AGENTS.override.md` over `AGENTS.md` (at most one file per directory).
- Discovered files are concatenated root → leaf (combined size capped at 32 KiB by default; override with `KODE_PROJECT_DOC_MAX_BYTES`).
- If `CLAUDE.md` exists in the current directory, Kode also reads it as a legacy instruction file.

## Overview

Kode is a powerful AI assistant that lives in your terminal. It can understand your codebase, edit files, run commands, and handle entire workflows for you.

> **⚠️ Security Notice**: Kode runs in YOLO mode by default (equivalent to the `--dangerously-skip-permissions` flag), bypassing all permission checks for maximum productivity. YOLO mode is recommended only for trusted, secure environments when working on non-critical projects. If you're working with 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `learn-claude-code.md`
```markdown
# 📦 shareAI-lab/learn-claude-code [🔖 PENDING/APPROVE]
🔗 https://github.com/shareAI-lab/learn-claude-code
🌐 https://learn.shareai.run

## Meta
- **Stars:** ⭐ 39669 | **Forks:** 🍴 6196
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Bash is all you need -  A nano claude code–like 「agent harness」, built from 0 to 1

## README (trích đầu)
```
[English](./README.md) | [中文](./README-zh.md) | [日本語](./README-ja.md)
# Learn Claude Code -- Harness Engineering for Real Agents

## The Model IS the Agent

Before we talk about code, let's get one thing absolutely straight.

**An agent is a model. Not a framework. Not a prompt chain. Not a drag-and-drop workflow.**

### What an Agent IS

An agent is a neural network -- a Transformer, an RNN, a learned function -- that has been trained, through billions of gradient updates on action-sequence data, to perceive an environment, reason about goals, and take actions to achieve them. The word "agent" in AI has always meant this. Always.

A human is an agent. A biological neural network, shaped by millions of years of evolutionary training, perceiving the world through senses, reasoning through a brain, acting through a body. When DeepMind, OpenAI, or Anthropic say "agent," they mean the same thing the field has meant since its inception: **a model that has learned to act.**

The proof is written in history:

- **2013 -- DeepMind DQN plays Atari.** A single neural network, receiving only raw pixels and game scores, learned to play 7 Atari 2600 games -- surpassing all prior algorithms and beating human experts on 3 of them. By 2015, the same architecture scaled to [49 games and matched professional human testers](https://www.nature.com/articles/nature14236), published in *Nature*. No game-specific rules. No decision trees. One model, learning from experience. That model was the agent.

- **2019 -- OpenAI Five conquers Dota 2.** Five neural networks, having played [45,000 years of Dota 2](https://openai.com/index/openai-five-defeats-dota-2-world-champions/) against themselves in 10 months, defeated **OG** -- the reigning TI8 world champions -- 2-0 on a San Francisco livestream. In a subsequent public arena, the AI won 99.4% of 42,729 games against all comers. No scripted strategies. No meta-programmed team coordination. The models learned teamwork, tactics, and real-time adaptation entirely through self-play.

- **2019 -- DeepMind AlphaStar masters StarCraft II.** AlphaStar [beat professional players 10-1](https://deepmind.google/blog/alphastar-mastering-the-real-time-strategy-game-starcraft-ii/) in a closed-door match, and later achieved [Grandmaster status](https://www.nature.com/articles/d41586-019-03298-6) on European servers -- top 0.15% of 90,000 players. A game with imperfect information, real-time decisions, and a combinatorial action space that dwarfs chess and Go. The agent? A model. Trained. Not scripted.

- **2019 -- Tencent Jueyu dominates Honor of Kings.** Tencent AI Lab's "Jueyu" [defeated KPL professional players](https://www.jiemian.com/article/3371171.html) in a full 5v5 match at the World Champion Cup. In 1v1 mode, pros won only [1 out of 15 games and never survived past 8 minutes](https://developer.aliyun.com/article/851058). Training intensity: one day equaled 440 human years. By 2021, Jueyu surpassed KPL pros across the full hero poo
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `shareAI-skills.md`
```markdown
# 📦 shareAI-lab/shareAI-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/shareAI-lab/shareAI-skills


## Meta
- **Stars:** ⭐ 222 | **Forks:** 🍴 29
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
shareAI Lab's skills for agent to build agent & other custom software system

## README (trích đầu)
```
# shareAI Skills

Knowledge packages that extend AI agent capabilities.

[中文文档](./README_zh.md)

> Works with **[Kode CLI](https://github.com/shareAI-lab/Kode)**, **Claude Code**, **Cursor**, and any agent supporting the [Agent Skills Spec](https://github.com/anthropics/agent-skills).

## Installation

### Kode CLI (Recommended)

```bash
kode plugins install https://github.com/shareAI-lab/shareAI-skills
```

### Claude Code

```bash
claude plugins install https://github.com/shareAI-lab/shareAI-skills
```

### Cursor

Copy the `skills/` directory to your Cursor skills folder.

### Other Agents

Load `SKILL.md` files on-demand when the agent needs domain expertise.

## Available Skills

| Skill | Description |
|-------|-------------|
| [skill-judge](./skills/skill-judge/) | Evaluate Agent Skill quality across 8 dimensions (120-point system) |
| [media-writer](./skills/media-writer/) | Adapt content for WeChat, HN, Reddit, Medium, Twitter, Dev.to, LinkedIn |
| [agent-builder](./skills/agent-builder/) | Design and build AI agents for any domain |
| [vibe-coding](./skills/vibe-coding/) | Vibe-driven development with minimal specs |

## How to Create Great Skills

Creating a truly effective skill is an art. We've analyzed 17 official Anthropic skills and distilled the core principles:

**Core Formula:**
```
Good Skill = Expert-only Knowledge - What Claude Already Knows
```

Read the full guide: **[How to Create Great Agent Skills](./docs/how-to-create-great-agent-skill.md)**

Use the [skill-judge](./skills/skill-judge/) skill to evaluate your skill's quality with structured scoring across 8 dimensions:

| Dimension | Points | Focus |
|-----------|--------|-------|
| Knowledge Delta | 20 | Expert-only knowledge vs. what Claude already knows |
| Mindset + Procedures | 15 | Thinking patterns + domain-specific workflows |
| Anti-Pattern Quality | 15 | Specific NEVER lists with non-obvious reasons |
| Specification (esp. Description) | 15 | Description with WHAT, WHEN, and KEYWORDS |
| Progressive Disclosure | 15 | Content layering, loading triggers |
| Freedom Calibration | 15 | Specificity matched to task fragility |
| Pattern Recognition | 10 | Follows established skill patterns |
| Practical Usability | 15 | Decision trees, working examples, edge cases |

## What are Skills?

Skills are modular knowledge packages that give AI agents domain expertise on-demand. They follow the [Agent Skills Spec](https://github.com/anthropics/agent-skills).

## Skill Structure

```
skill-name/
├── SKILL.md              # Core instructions (required)
├── references/           # Detailed documentation (optional)
├── scripts/              # Executable code (optional)
└── assets/               # Templates and resources (optional)
```

## Philosophy

> **Skills are knowledge, not code.**

A skill doesn't tell the agent what to do step-by-step. It gives the agent the knowledge to figure out what to do. The model is smart - your job is to inform it, not constrain it.

## Contri
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


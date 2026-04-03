---
id: khanhbkqt-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:59.888127
---

# KNOWLEDGE EXTRACT: khanhbkqt
> **Extracted on:** 2026-03-30 17:38:16
> **Source:** khanhbkqt

---

## File: `spawn-agent.md`
```markdown
# 📦 khanhbkqt/spawn-agent [🔖 PENDING/APPROVE]
🔗 https://github.com/khanhbkqt/spawn-agent


## Meta
- **Stars:** ⭐ 39 | **Forks:** 🍴 6
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A skill for Antigravity that delegates scoped work to Gemini CLI or Codex CLI worker agents — keeping the main context clean.

## README (trích đầu)
```
<div align="center">

# 🚀 spawn-agent

**A skill for [Antigravity](https://github.com/google-deepmind/antigravity) that delegates scoped work to worker agents, keeping the main context clean.**

Antigravity doesn't natively support spawning sub-agents. This skill fills that gap — use [Gemini CLI](https://github.com/google-gemini/gemini-cli) or [Codex CLI](https://github.com/openai/codex) as worker agents to handle implementation, research, and bug fixes while the orchestrator stays focused.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## The Problem

Antigravity is powerful, but it has no built-in way to delegate work to sub-agents. Every file read, build output, and error trace goes into the same context window — and it fills up fast. Once it does, the agent loses track of earlier instructions and can't reason about the big picture.

**Before spawn-agent:**
```
Main Agent Context:
├── User conversation          ~5%
├── Codebase understanding     ~10%
├── File A contents            ~15%  ← polluting
├── File B contents            ~15%  ← polluting
├── Build output               ~20%  ← polluting
├── Lint errors                ~10%  ← polluting
└── Remaining for reasoning    ~25%  ← squeezed
```

**After spawn-agent:**
```
Main Agent Context (Orchestrator):         Worker Agent Context:
├── User conversation     ~15%             ├── Task prompt          ~10%
├── Codebase overview     ~20%             ├── File A contents      ~25%
├── Delegation plan       ~10%             ├── File B contents      ~25%
├── Worker results        ~15%             ├── Build output         ~20%
└── Remaining reasoning   ~40%  ← clean   └── Implementation       ~20%
```

## How It Works

The main agent acts as an **orchestrator** — it plans, delegates, and reviews. Worker agents (Gemini or Codex) handle the actual implementation in isolated sessions.

```
Orchestrator                    Worker (Gemini/Codex)
     │                               │
     ├──── 1. DEFINE task ────────►   │
     ├──── 2. COMPOSE prompt ─────►   │
     ├──── 3. SPAWN ──────────────►   ├── reads codebase
     │                                ├── implements changes
     │                                ├── runs verification
     │     ◄── 4. OUTPUT ────────────┘
     ├──── 5. REVIEW results
     └──── 6. REPORT to user
```

## Installation

### Prerequisites

At least one of these CLI tools must be installed:

```bash
# Gemini CLI
npm install -g @google/gemini-cli

# Codex CLI
npm install -g @openai/codex
```

### Install the Skill

Clone into your Antigravity skills directory:

```bash
# Recommended: into your global skills directory
git clone https://github.com/khanhbkqt/spawn-agent.git ~/.gemini/antigravity/skills/spawn-agent

# Or per-project
git clone https://github.com/khanhbkqt/spawn-agent.git .agent/skills/spawn-agent

# Or symlink from a central location
git clone https://github.com/khanhbkqt/spawn-agent.git ~/spawn-agent
ln -s ~/spawn-ag
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


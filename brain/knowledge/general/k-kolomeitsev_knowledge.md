---
id: k-kolomeitsev-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.944974
---

# KNOWLEDGE EXTRACT: k-kolomeitsev
> **Extracted on:** 2026-03-30 17:38:14
> **Source:** k-kolomeitsev

---

## File: `data-structure-protocol.md`
```markdown
# 📦 k-kolomeitsev/data-structure-protocol [🔖 PENDING/APPROVE]
🔗 https://github.com/k-kolomeitsev/data-structure-protocol


## Meta
- **Stars:** ⭐ 33 | **Forks:** 🍴 3
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Graph-based long-term memory skill for AI (LLM) coding agents — faster context, fewer tokens, safer refactors

## README (trích đầu)
```
[![GitHub stars](https://img.shields.io/github/stars/k-kolomeitsev/data-structure-protocol?style=social)](https://github.com/k-kolomeitsev/data-structure-protocol)
[![License](https://img.shields.io/github/license/k-kolomeitsev/data-structure-protocol)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude_Code-supported-green)]()
[![Cursor](https://img.shields.io/badge/Cursor-supported-green)]()
[![Codex](https://img.shields.io/badge/Codex-supported-green)]()

# Data Structure Protocol (DSP)

**The missing memory layer for AI-assisted development**

---

## The problem

Your agent re-reads the same codebase every session. **DSP fixes that.**

Every time you start a new task, your AI coding agent spends the first 5–15 minutes "getting oriented" — scanning files, tracing imports, figuring out what depends on what. On large projects this becomes a constant tax on tokens and attention. Context is rebuilt from scratch, every single time.

DSP is a graph-based long-term structural memory stored in `.dsp/`. It gives agents a persistent, versionable map of your codebase — entities, dependencies, public APIs, and the *reasons* behind every connection — so they can pick up exactly where they left off.

> **DSP is not another workflow framework.** It's the persistent structural memory layer that's missing from every AI coding workflow.

---

## Install

**macOS / Linux:**

```bash
curl -fsSL https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.sh | bash
```

**Windows:**

```powershell
irm https://raw.githubusercontent.com/k-kolomeitsev/data-structure-protocol/main/install.ps1 | iex
```

**Codex:**

```
$skill-installer install https://github.com/k-kolomeitsev/data-structure-protocol/tree/main/skills/data-structure-protocol
```

---

## What you get

- **Agent stops re-learning your project every session** — structural context persists across tasks, sessions, and even team members
- **Dependency discovery in seconds, not minutes** — graph traversal replaces full-repo scanning
- **Impact analysis before refactors** — know what breaks before you touch it
- **Safer changes on brownfield codebases** — hidden couplings become visible edges in the graph
- **Works with Claude Code, Cursor, Codex — no lock-in** — DSP is an agent skill, not a platform
- **Git-native and versionable** — `.dsp/` is plain text, diffs cleanly, reviews like code

> **Honest trade-off:** bootstrapping DSP on a large project takes real effort (time, tokens, discipline). It pays back over the project lifetime through lower per-task token usage, faster discovery, and more predictable agent behavior.

---

## How it works

```
┌──────────────────────┐
│      Codebase        │
│  (files + assets)    │
└──────────┬───────────┘
           │  create/update graph as you work
           ▼
┌──────────────────────┐
│   DSP Builder / CLI  │
│   (dsp-cli.py)       │
└──────────┬──────
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


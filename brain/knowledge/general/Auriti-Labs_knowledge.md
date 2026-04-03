---
id: auriti-labs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:51.112677
---

# KNOWLEDGE EXTRACT: Auriti-Labs
> **Extracted on:** 2026-03-30 17:29:12
> **Source:** Auriti-Labs

---

## File: `kore-memory.md`
```markdown
# 📦 Auriti-Labs/kore-memory [🔖 PENDING/APPROVE]
🔗 https://github.com/Auriti-Labs/kore-memory


## Meta
- **Stars:** ⭐ 6 | **Forks:** 🍴 1
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-02-27
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The memory layer that thinks like a human: remembers what matters, forgets what does not, and never calls home.

## README (trích đầu)
```
<div align="center">

<img src="assets/logo.svg" alt="Kore Memory" width="420"/>

<br/>

**The memory layer that thinks like a human.**
<br/>
Remembers what matters. Forgets what doesn't. Never calls home.

<br/>

[![CI](https://github.com/auriti-labs/kore-memory/actions/workflows/ci.yml/badge.svg)](https://github.com/auriti-labs/kore-memory/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/kore-memory.svg?style=flat-square&color=7c3aed)](https://pypi.org/project/kore-memory/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue?style=flat-square)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Zero Cloud](https://img.shields.io/badge/cloud-zero-orange?style=flat-square)]()
[![Multilingual](https://img.shields.io/badge/languages-50%2B-purple?style=flat-square)]()
[![Docs](https://img.shields.io/badge/docs-auritidesign.it-00b4d8?style=flat-square)](https://auritidesign.it/brain/knowledge/docs_legacy/kore-memory/)

<br/>

[**Docs**](https://auritidesign.it/brain/knowledge/docs_legacy/kore-memory/) · [**Install**](#-install) · [**Quickstart**](#-quickstart) · [**How it works**](#-how-it-works) · [**API**](#-api-reference) · [**Changelog**](CHANGELOG.md) · [**Roadmap**](#-roadmap)

</div>

---

## Why Kore?

Every AI agent memory tool has the same flaw: they remember everything forever, phone home to cloud APIs, or need an LLM just to decide what's worth storing.

**Kore is different.**

<div align="center">

| Feature | **Kore** | Mem0 | Letta | Memori |
|---|:---:|:---:|:---:|:---:|
| Runs fully offline | ✅ | ❌ | ❌ | ❌ |
| No LLM required | ✅ | ❌ | ❌ | ✅ |
| **Memory Decay** (Ebbinghaus) | ✅ | ❌ | ❌ | ❌ |
| Auto-importance scoring | ✅ local | ✅ via LLM | ❌ | ❌ |
| **Memory Compression** | ✅ | ❌ | ❌ | ❌ |
| Semantic search (50+ langs) | ✅ local | ✅ via API | ✅ | ✅ |
| Timeline API | ✅ | ❌ | ❌ | ❌ |
| Tags & Relations (graph) | ✅ | ❌ | ✅ | ❌ |
| TTL / Auto-expiration | ✅ | ❌ | ❌ | ❌ |
| MCP Server (Claude, Cursor) | ✅ | ❌ | ❌ | ❌ |
| Batch API | ✅ | ❌ | ❌ | ❌ |
| Export / Import (JSON) | ✅ | ❌ | ✅ | ❌ |
| Soft-delete / Archive | ✅ | ❌ | ❌ | ❌ |
| Prometheus Metrics | ✅ | ❌ | ❌ | ❌ |
| Agent namespace isolation | ✅ | ✅ | ✅ | ❌ |
| Install in 2 minutes | ✅ | ❌ | ❌ | ❌ |

</div>

---

## ✨ Key Features

### 📉 Memory Decay — The Ebbinghaus Engine
Memories fade over time using the [Ebbinghaus forgetting curve](https://en.wikipedia.org/wiki/Forgetting_curve). Critical memories persist for months. Casual notes fade in days.

```
decay = e^(-t · ln2 / half_life)
```

Every retrieval resets the clock and boosts the decay score — just like spaced repetition in human learning.

### 🤖 Auto-Importance Scoring
No LLM call needed. Kore scores importance locally using content analysis — keywords, category, length.

```python
"API token: sk-abc123"  →  importance: 5  (critical, never forget)
"Juan prefers dark mode"  →  importance: 4  (preference)
"Meeting at 3pm"  →  importance: 2  (general)
```

### 🔍 Semanti
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


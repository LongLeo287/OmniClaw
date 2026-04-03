---
id: nhadaututtheky-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:11.879005
---

# KNOWLEDGE EXTRACT: nhadaututtheky
> **Extracted on:** 2026-03-30 17:49:11
> **Source:** nhadaututtheky

---

## File: `neural-memory.md`
```markdown
# 📦 nhadaututtheky/neural-memory [🔖 PENDING/APPROVE]
🔗 https://github.com/nhadaututtheky/neural-memory


## Meta
- **Stars:** ⭐ 133 | **Forks:** 🍴 43
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
NeuralMemory stores experiences as interconnected neurons and recalls them through spreading activation, mimicking how the human brain works. Instead of searching a database, memories are retrieved through associative recall - activating related concepts until the relevant memory emerges.

## README (trích đầu)
```
# NeuralMemory

[![PyPI](https://img.shields.io/pypi/v/neural-memory.svg)](https://pypi.org/project/neural-memory/)
[![CI](https://github.com/nhadaututtheky/neural-memory/workflows/CI/badge.svg)](https://github.com/nhadaututtheky/neural-memory/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![VS Code](https://img.shields.io/visual-studio-marketplace/v/neuralmem.neuralmemory?label=VS%20Code)](https://marketplace.visualstudio.com/items?itemName=neuralmem.neuralmemory)
[![OpenClaw Plugin](https://img.shields.io/npm/v/neuralmemory?label=OpenClaw)](https://www.npmjs.com/package/neuralmemory)

**Your AI agent forgets everything between sessions. Neural Memory gives it a brain.**

<p align="center">
  <img src="docs/assets/images/hero-brain.svg" alt="Neural Memory — spreading activation" width="720"/>
</p>

Memories are stored as interconnected neurons and recalled through spreading activation — the same way the human brain works. No vector database. No API calls. No monthly embedding bill.

```bash
pip install neural-memory
nmem init --full
```

Restart your AI tool. Your agent now remembers.

---

## 3 Tools. That's It.

50 MCP tools are available, but you only need three:

| Tool | What it does |
|------|-------------|
| `nmem_remember` | Store a memory — auto-detects type, tags, and connections |
| `nmem_recall` | Recall through spreading activation — related memories surface naturally |
| `nmem_health` | Brain health score (A–F) with actionable fix suggestions |

Everything else — sessions, context loading, habit tracking, maintenance — works transparently in the background.

> [All 50 MCP tools →](https://nhadaututtheky.github.io/neural-memory/api/mcp-tools/)

---

## What Makes This Different

Most memory tools are search engines. Neural Memory is a **graph that thinks**.

When you ask "Why did Tuesday's outage happen?", a vector database returns the most similar sentence. Neural Memory traces the chain:

```
outage ← CAUSED_BY ← JWT expiry ← SUGGESTED_BY ← Alice's review
```

**Relationships are explicit** — `CAUSED_BY`, `LEADS_TO`, `RESOLVED_BY`, `CONTRADICTS` — so your agent doesn't just find memories, it *reasons* through them.

| | Search-based (RAG) | Neural Memory |
|--|---------------------|---------------|
| Retrieval | Similarity score | Graph traversal |
| Relationships | None | 24 explicit types |
| LLM required | Yes (embedding) | No — fully offline |
| Multi-hop reasoning | Multiple queries | One traversal |
| Memory lifecycle | Static | Decay, reinforcement, consolidation |
| Cost per 1K queries | ~$0.02 | **$0.00** |

---

## Cloud Sync — Your Data, Your Infrastructure

Sync your brain across every machine. Unlike other memory tools, **we never store your data**.

```
Laptop ←→ Your Cloudflare Worker ←→ Desktop
                  ↕
              Your Phone
```

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


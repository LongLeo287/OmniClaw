---
id: scarletkc-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.767995
---

# KNOWLEDGE EXTRACT: scarletkc
> **Extracted on:** 2026-03-30 17:53:03
> **Source:** scarletkc

---

## File: `vexor.md`
```markdown
# 📦 scarletkc/vexor [🔖 PENDING/APPROVE]
🔗 https://github.com/scarletkc/vexor
🌐 https://pypi.org/project/vexor/

## Meta
- **Stars:** ⭐ 210 | **Forks:** 🍴 12
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A semantic search engine for files and code.

## README (trích đầu)
```
<div align="center">

<img src="https://raw.githubusercontent.com/scarletkc/vexor/refs/heads/main/assets/vexor.svg" alt="Vexor" width="35%" height="auto">

# Vexor

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/vexor.svg)](https://pypi.org/project/vexor/)
[![CI](https://img.shields.io/github/actions/workflow/status/scarletkc/vexor/publish.yml?branch=main)](https://github.com/scarletkc/vexor/actions/workflows/publish.yml)
[![Codecov](https://img.shields.io/codecov/c/github/scarletkc/vexor/main)](https://codecov.io/github/scarletkc/vexor)
[![License](https://img.shields.io/github/license/scarletkc/vexor.svg)](https://github.com/scarletkc/vexor/blob/main/LICENSE)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/scarletkc/vexor)

</div>

---

**Vexor** is a semantic search engine that builds reusable indexes over files and code.
It supports configurable embedding and reranking providers, and exposes the same core through a Python API, a CLI tool, and an optional desktop frontend.

<video src="https://github.com/user-attachments/assets/4d53eefd-ab35-4232-98a7-f8dc005983a9" controls="controls" style="max-width: 600px;">
      Vexor Demo Video
    </video>

## Featured In

Vexor has been recognized and featured by the community:

- **[Ruan Yifeng's Weekly (Issue #379)](https://github.com/ruanyf/weekly/blob/master/docs/issue-379.md#ai-%E7%9B%B8%E5%85%B3)** - A leading tech newsletter in the Chinese developer community.
- **[Awesome Claude Skills](https://github.com/VoltAgent/awesome-claude-skills?tab=readme-ov-file#development-and-testing)** - Curated list of best-in-class skills for AI agents.

## Why Vexor?

When you remember what a file *does* but forget its name or location, Vexor finds it instantly—no grep patterns or directory traversal needed.

Designed for both humans and AI coding assistants, enabling semantic file discovery in autonomous agent workflows.

## Install

Download standalone binary from [releases](https://github.com/scarletkc/vexor/releases) (no Python required), or:
```bash
pip install vexor  # also works with pipx, uv
```

## Quick Start

### 0. Guided Setup (Recommended)
```bash
vexor init
```
The wizard also runs automatically on first use when no config exists.

### 1. Search
```bash
vexor "api client config"  # defaults to search current directory
# or explicit path:
vexor search "api client config" --path ~/projects/demo --top 5
# in-memory search only:
vexor search "api client config" --no-cache 
```

Vexor auto-indexes on first search. Example output:
```
Vexor semantic file search results
──────────────────────────────────
#   Similarity   File path                       Lines   Preview
1   0.923        ./src/config_loader.py          -       config loader entrypoint
2   0.871        ./src/utils/config_parse.py     -       parse config helpers
3   0.809        ./tests/test_config_loader.py   -       tests for conf
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


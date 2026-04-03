---
id: massimodeluisa-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:06.799488
---

# KNOWLEDGE EXTRACT: massimodeluisa
> **Extracted on:** 2026-03-30 17:42:05
> **Source:** massimodeluisa

---

## File: `recursive-decomposition-skill.md`
```markdown
# 📦 massimodeluisa/recursive-decomposition-skill [🔖 PENDING/APPROVE]
🔗 https://github.com/massimodeluisa/recursive-decomposition-skill
🌐 https://arxiv.org/abs/2512.24601

## Meta
- **Stars:** ⭐ 21 | **Forks:** 🍴 1
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Claude Code skill for handling long-context tasks through recursive decomposition

## README (trích đầu)
```
<p align="center">
  <img src="assets/logo.png" alt="Recursive Decomposition Skill" width="200">
</p>

<h1 align="center">Recursive Decomposition Skill</h1>

<p align="center">
  <strong>Handle long-context tasks with Claude Code through recursive decomposition</strong>
</p>

<p align="center">
  <a href="#installation"><img src="https://img.shields.io/badge/Claude_Code-Plugin-blueviolet?style=flat-square" alt="Claude Code Plugin"></a>
  <a href="https://arxiv.org/abs/2512.24601"><img src="https://img.shields.io/badge/arXiv-2512.24601-b31b1b?style=flat-square" alt="arXiv Paper"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Format-Agent_Skills-orange?style=flat-square" alt="Agent Skills Format"></a>
</p>

<p align="center">
  <a href="#what-it-does">What It Does</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="#benchmarks">Benchmarks</a> •
  <a href="#acknowledgments">Acknowledgments</a>
</p>

---

## The Problem

When analyzing large codebases, processing many documents, or aggregating information across dozens of files, Claude's context window becomes a bottleneck. As context grows, **"context rot"** degrades performance:

- Missed details in long documents
- Decreased accuracy on information retrieval
- Hallucinated connections between distant content
- Degraded reasoning over large evidence sets

## The Solution

This skill implements **Recursive Language Model (RLM)** strategies from [Zhang, Kraska, and Khattab's 2025 research](https://arxiv.org/abs/2512.24601), enabling Claude Code to handle inputs **up to 2 orders of magnitude beyond normal context limits**.

Instead of cramming everything into context, Claude learns to:

1. **Filter** — Narrow search space before deep analysis
2. **Chunk** — Partition inputs strategically
3. **Recurse** — Spawn sub-agents for independent segments
4. **Verify** — Re-check answers on smaller, focused windows
5. **Synthesize** — Aggregate results programmatically

---

## What It Does

| Task Type | Without Skill | With Skill |
|-----------|---------------|------------|
| Analyze 100+ files | Context overflow / degraded results | Systematic coverage via decomposition |
| Multi-document QA | Missed information | Comprehensive extraction |
| Codebase-wide search | Manual iteration | Parallel sub-agent analysis |
| Information aggregation | Incomplete synthesis | Map-reduce pattern |

### Real Test Results

We tested on the [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) (196 files, 356MB):

```
Task: "Find all Anthropic API calling patterns across the codebase"

Results:
├── Files scanned: 142
├── Files with API calls: 18
├── Patterns identified: 8 distinct patterns
├── Anti-patterns detected: 4
└── Output: Comprehensive report with file:line reference
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


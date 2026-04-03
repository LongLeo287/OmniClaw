---
id: giskard-ai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:27.056080
---

# KNOWLEDGE EXTRACT: Giskard-AI
> **Extracted on:** 2026-03-30 17:37:58
> **Source:** Giskard-AI

---

## File: `giskard-oss.md`
```markdown
# 📦 Giskard-AI/giskard-oss [🔖 PENDING/APPROVE]
🔗 https://github.com/Giskard-AI/giskard-oss
🌐 https://docs.giskard.ai

## Meta
- **Stars:** ⭐ 5203 | **Forks:** 🍴 418
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🐢 Open-Source Evaluation & Testing library for LLM Agents

## README (trích đầu)
```
<p align="center">
  <img alt="giskardlogo" src="readme/logo_light.png#gh-light-mode-only">
  <img alt="giskardlogo" src="readme/logo_dark.png#gh-dark-mode-only">
</p>
<h1 align="center" weight='300' >Evals, Red Teaming and Test Generation for Agentic Systems</h1>
<h3 align="center" weight='300' >Modular, Lightweight, Dynamic and Async-first </h3>
<div align="center">

  [![GitHub release](https://img.shields.io/github/v/release/Giskard-AI/giskard)](https://github.com/Giskard-AI/giskard/releases)
  [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/Giskard-AI/giskard/blob/main/LICENSE)
  [![Downloads](https://static.pepy.tech/badge/giskard/month)](https://pepy.tech/project/giskard)
  [![CI](https://github.com/Giskard-AI/giskard-oss/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/Giskard-AI/giskard-oss/actions/workflows/ci.yml/badge.svg?branch=main)
  [![Giskard on Discord](https://img.shields.io/discord/939190303397666868?label=Discord)](https://gisk.ar/discord)

  <a rel="me" href="https://fosstodon.org/@Giskard"></a>

</div>
<h3 align="center">
   <a href="https://docs.giskard.ai/oss"><b>Docs</b></a> &bull;
  <a href="https://www.giskard.ai/?utm_source=github&utm_medium=github&utm_campaign=github_readme&utm_id=readmeblog"><b>Website</b></a> &bull;
  <a href="https://gisk.ar/discord"><b>Community</b></a>
 </h3>
<br />

> [!IMPORTANT]
> **Giskard v3** is a fresh rewrite designed for dynamic, multi-turn testing of AI agents. This release drops heavy dependencies for better efficiency while introducing a more powerful AI vulnerability scanner and enhanced RAG evaluation capabilities. For now, the vulnerability scanner and RAG evaluation still rely on Giskard v2.
> **Giskard v2 remains available but is no longer actively maintained.**
> Follow progress → [Read the v3 Annoucement](https://github.com/orgs/Giskard-AI/discussions/2250) · [Roadmap](https://github.com/Giskard-AI/giskard-oss/issues/2252)

## Install

```sh
pip install giskard
```

Requires Python 3.12+.

______________________________________________________________________

Giskard is an open-source Python library for **testing and evaluating agentic systems**. The v3 architecture is a modular set of focused packages — each carrying only the dependencies it needs — built from scratch to wrap anything: an LLM, a black-box agent, or a multi-step pipeline.

| Status | Package | Description |
|--------|---------|-------------|
| ✅ Alpha | `giskard-checks` | Testing & evaluation — scenario API, built-in checks, LLM-as-judge |
| 🚧 In progress | `giskard-scan` | Agent vulnerability scanner — red teaming, prompt injection, data leakage (successor of [v2 Scan](https://legacy-docs.giskard.ai/en/stable/open_source/scan/index.html)) |
| 📋 Planned | `giskard-rag` | RAG evaluation & synthetic data generation (successor of [v2 RAGET](https://legacy-docs.giskard.ai/en/stable/open_source/testset_generation/index.html)) |

## Giskard Checks — creat
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


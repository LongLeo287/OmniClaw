---
id: system-overview
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.666487
---

# 🏛️ System Overview (21-Department Architecture)

OmniClaw functions exactly like a digital mega-corporation, boasting **21 distinct structural "Departments"** managed by AI Agents working in concert via multi-agent pipelines.

[**🇻🇳 Xem Bản Tiếng Việt**](system_overview-vn.md) | [**Return to Docs Index**](../README.md) | [**📚 Wiki Reference**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## 1. The Execution Hierarchy

Our architecture relies on a strict Top-Down cascade, ensuring decisions and safety boundaries are inherited perfectly.

1. **CEO (Tier 0)**: The human operator (You). Provides high-level strategic commands.
2. **Orchestrator Pro / C-Suite (Tier 1)**: The master agent models (e.g., Antigravity proxy). Intercepts complex commands, routes workflow, handles deep analysis.
3. **Department Heads (Tier 2)**: Standardized LLM agents bound by specific `rules/` (e.g., QA Manager, Frontend Engineer, CIV Chief).
4. **Task Subagents (Tier 3)**: Ephemeral specialized agents that spawn to execute targeted logic (e.g., git-protector, doc-parser) and die when the task is complete.

## 2. Shared AI State

All these autonomous components are linked using the Local Memory (`brain/`). The critical pieces of inter-agent connection are:

- **`blackboard.json`**: The active synchronized task state. If Agent A completes a feature, it updates the blackboard so Agent B (QA Testing) automatically knows it's time to run tests.
- **RAG & Knowledge Base**: A graph-DB backed directory (`brain/knowledge`) storing vetted insights and external library references over iterations.

## 3. Top Core Departments

Of the 21 Departments, a few critical nodes stand out for developers:
- **Dept 01 (Engineering)**: Builds features, fixes code, writes tests.
- **Dept 10 (Strix Security)**: Vets plugins, reviews payloads, blocks unauthorized edits (Zero Trust).
- **Dept 20 (CIV - Content Intake)**: Ingests GitHub repos, PDFs, web docs and summarizes them for the Graph Local Memory.
- **Dept 22 (Operations)**: Automates git sync paths, backup hooks, and deep cleaner pipeline executions.

> *For the actual machine-readable JSON mapping of these agents, AI instances reference the `brain/corp/org_chart.yaml` and `AGENTS.md`.*

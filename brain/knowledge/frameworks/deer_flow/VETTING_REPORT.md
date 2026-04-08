---
title: DeerFlow Vetting Report
date: 2026-04-05
analyst: OmniClaw OMA
status: VETTED & EXTRACTED
---

# Analysis of DeerFlow 2.0

DeerFlow is a "Super Agent Harness" running heavily on LangGraph and Langchain. 
Its core focus is "Deer Flow" – deep research via isolated Subagents inside a massive Docker Sandbox.
It integrates with Claude Code using the `claude-to-deerflow` skill.

## Extraction Action
- Extracted its core Workflow blueprints into `ecosystem/workflows/deerflow.md`.
- Extracted the `skills/public` folder into `ecosystem/skills/deerflow_skills`.
- Placed the architecture in `brain/knowledge/frameworks/deer_flow`.

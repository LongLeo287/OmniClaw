---
title: Hermes Agent Vetting Report
date: 2026-04-05
analyst: OmniClaw OMA
status: VETTED & EXTRACTED
---

# Analysis of Hermes Agent

Hermes Agent (by Nous Research) is a self-improving AI agent harness.
It relies on a TUI and Gateway architecture, meaning it natively supports Discord, Telegram, Slack through "Cron Scheduler" and "Subagents".

## Extraction Action
- Extracted its `skills/` module directly into OmniClaw `ecosystem/skills/hermes_skills` for our agents to index.
- Placed the architecture in `brain/knowledge/frameworks/hermes_agent`.

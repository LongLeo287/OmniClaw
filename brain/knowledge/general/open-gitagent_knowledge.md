---
id: open-gitagent-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:15.137061
---

# KNOWLEDGE EXTRACT: open-gitagent
> **Extracted on:** 2026-03-30 17:49:55
> **Source:** open-gitagent

---

## File: `gitagent.md`
```markdown
# 📦 open-gitagent/gitagent [🔖 PENDING/APPROVE]
🔗 https://github.com/open-gitagent/gitagent
🌐 https://gitagent.sh

## Meta
- **Stars:** ⭐ 1657 | **Forks:** 🍴 172
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A framework-agnostic, git-native standard for defining AI agents

## README (trích đầu)
```
<p align="center">
  <img src="banner.png" alt="gitagent banner" width="700" />
</p>

# gitagent | your repository becomes your agent

[![npm version](https://img.shields.io/npm/v/@shreyaskapale/gitagent)](https://www.npmjs.com/package/@shreyaskapale/gitagent)
[![CI](https://github.com/open-gitagent/gitagent/actions/workflows/ci.yml/badge.svg)](https://github.com/open-gitagent/gitagent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Spec: v0.1.0](https://img.shields.io/badge/spec-v0.1.0-blue)](https://github.com/open-gitagent/gitagent/blob/main/spec/SPECIFICATION.md)
[![Node >= 18](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](https://nodejs.org)

A framework-agnostic, git-native standard for defining AI agents. Clone a repo, get an agent.

## Why

Every AI framework has its own structure. There's no universal, portable way to define an agent that works across Claude Code, OpenAI, LangChain, CrewAI, and AutoGen. **gitagent** fixes that.

- **Git-native** — Version control, branching, diffing, and collaboration built in
- **Framework-agnostic** — Export to any framework with adapters
- **Compliance-ready** — First-class support for FINRA, Federal Reserve, SEC, and segregation of duties
- **Composable** — Agents can extend, depend on, and delegate to other agents

## The Standard

Your repository becomes your agent. Drop these files into any git repo and it becomes a portable, framework-agnostic agent definition — everything else (CLI, adapters, patterns) builds on top of it.

```
my-agent/
│
│   # ── Core Identity (required) ──────────────────────────
├── agent.yaml              # Manifest — name, version, model, skills, tools, compliance
├── SOUL.md                 # Identity, personality, communication style, values
│
│   # ── Behavior & Rules ──────────────────────────────────
├── RULES.md                # Hard constraints, must-always/must-never, safety boundaries
├── DUTIES.md               # Segregation of duties policy and role boundaries
├── AGENTS.md               # Framework-agnostic fallback instructions
│
│   # ── Capabilities ──────────────────────────────────────
├── skills/                 # Reusable capability modules (SKILL.md + scripts)
│   └── code-review/
│       ├── SKILL.md
│       └── review.sh
├── tools/                  # MCP-compatible tool definitions (YAML schemas)
├── workflows/              # Multi-step procedures/playbooks
│
│   # ── Knowledge & Memory ────────────────────────────────
├── knowledge/              # Reference documents the agent can consult
├── memory/                 # Persistent cross-session memory
│   └── runtime/            # Live agent state (dailylog.md, context.md)
│
│   # ── Lifecycle & Ops ───────────────────────────────────
├── hooks/                  # Lifecycle event handlers (bootstrap.md, teardown.md)
├── config/                 # Environment-specific overrides
├── compliance/             
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


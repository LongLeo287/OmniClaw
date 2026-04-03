---
id: heshamfs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:51.922316
---

# KNOWLEDGE EXTRACT: HeshamFS
> **Extracted on:** 2026-03-30 17:38:05
> **Source:** HeshamFS

---

## File: `materials-simulation-skills.md`
```markdown
# 📦 HeshamFS/materials-simulation-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/HeshamFS/materials-simulation-skills


## Meta
- **Stars:** ⭐ 27 | **Forks:** 🍴 2
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Agent Skills for computational materials science -- numerical stability, solvers, meshing,   convergence, and simulation workflows.

## README (trích đầu)
```
# Materials Simulation Skills

[![CI](https://github.com/heshamfs/materials-simulation-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/heshamfs/materials-simulation-skills/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-standard-orange.svg)](https://agentskills.io)
[![Python 3.10-3.12](https://img.shields.io/badge/Python-3.10--3.12-blue.svg)](https://www.python.org/)

**Open-source [Agent Skills](https://agentskills.io) for computational materials science and numerical simulation workflows.**

Give your AI coding agent domain expertise in numerical methods, simulation best practices, and scientific computing -- without re-explaining the same concepts every session. Skills are portable across Claude Code, Codex, Gemini CLI, Cursor, VS Code Copilot, and [20+ other compatible tools](https://agentskills.io).

---

## Table of Contents

- [The Problem](#the-problem)
- [The Solution](#the-solution)
- [What's Inside](#whats-inside)
  - [Core Numerical Skills](#core-numerical-skills-skillscore-numerical)
  - [Simulation Workflow Skills](#simulation-workflow-skills-skillssimulation-workflow)
  - [HPC Deployment Skills](#hpc-deployment-skills-skillshpc-deployment)
  - [Ontology Skills](#ontology-skills-skillsontology)
- [How Skills Work](#how-skills-work)
- [Security](#security)
- [Quick Start](#quick-start)
- [Adding Skills to Your Agent](#adding-skills-to-your-agent)
  - [Claude Code](#claude-code)
  - [Gemini CLI](#gemini-cli)
  - [OpenAI Codex](#openai-codex)
  - [VS Code / GitHub Copilot](#vs-code--github-copilot)
  - [Cursor](#cursor)
  - [Other Agents](#other-agents)
- [Repository Layout](#repository-layout)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## The Problem

Simulation engineers repeat the same guidance to AI agents constantly: *"Check the CFL number before running," "Use Richardson extrapolation for grid convergence," "Exit code 2 means bad input."* General-purpose agents lack the domain knowledge to run reliable numerical simulations without heavy hand-holding.

## The Solution

This project packages that domain knowledge into **skills** -- structured folders of instructions, scripts, and references that agents discover automatically and load on demand. Each skill teaches an agent a specific simulation competency, backed by validated Python scripts that produce reproducible results.

```text
You: Check if dt=0.001 is stable for my advection problem with v=2.0 m/s and dx=0.01.

Agent: I'll use the numerical-stability skill to check this.
       [runs cfl_checker.py --dx 0.01 --dt 0.001 --velocity 2.0 --json]

       CFL number = 0.2 (limit: 1.0) -- stable.
       Recommended max dt = 0.005 with safety factor 1.0.
```

No prompt engineering. No copy-pasting formulas. The agent finds the right skill, runs the script, and interprets the results.

---

## Wha
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


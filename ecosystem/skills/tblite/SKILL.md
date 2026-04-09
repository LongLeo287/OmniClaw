---
id: tblite
name: Tblite
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: agent-framework
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Provides reference knowledge and source templates from the tblite repository.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["agent", "orchestration", "ai"]
---

# Tblite

## Overview
This environment evaluates terminal agents on the [OpenThoughts-TBLite](https://huggingface.co/datasets/open-thoughts/OpenThoughts-TBLite) benchmark, a difficulty-calibrated subset of [Terminal-Bench 2.0](https://www.tbench.ai/leaderboard/terminal-bench/2.0).

## Usage
This skill provides reference architecture, patterns, and code templates from the `tblite` repository.
Agents working on `agent-framework` tasks should consult this skill and reference `payload/` for concrete examples.

## Key Capabilities
- Domain expertise: `agent-framework`
- Reference source code available in `payload/`
- Tags: agent, orchestration, ai

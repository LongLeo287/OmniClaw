---
id: openclaw_worker
name: Openclaw Worker
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: llm-tooling
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from openclaw_worker.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["llm", "ai"]
---

# Openclaw Worker

## Overview
> **Drop a file. Watch AI agents execute.** No manual intervention needed.

## Usage
Agents working on `llm-tooling` domain tasks should reference this skill.
See `payload/` for the full source code and implementation patterns.

## Key Capabilities
- Domain: `llm-tooling`
- Source code available in `payload/`
- Tags: llm, ai

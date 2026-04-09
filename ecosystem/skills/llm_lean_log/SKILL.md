---
id: llm_lean_log
name: Llm Lean Log
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
    description: Reference knowledge and templates from llm_lean_log.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["llm", "ai"]
---

# Llm Lean Log

## Overview
<img src="docs/imgs/logo.webp" alt="llm-lean-log logo" width="200">

## Usage
Agents working on `llm-tooling` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `llm-tooling`
- Source templates available in `payload/`
- Tags: llm, ai

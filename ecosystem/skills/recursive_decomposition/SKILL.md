---
id: recursive_decomposition_skill
name: Recursive Decomposition Skill
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
    description: Reference knowledge and templates from recursive_decomposition_skill.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["llm", "ai"]
---

# Recursive Decomposition Skill

## Overview
<img src="assets/logo.png" alt="Recursive Decomposition Skill" width="200">

## Usage
Agents working on `llm-tooling` domain tasks should reference this skill.
See `payload/` for the full source code and implementation patterns.

## Key Capabilities
- Domain: `llm-tooling`
- Source code available in `payload/`
- Tags: llm, ai

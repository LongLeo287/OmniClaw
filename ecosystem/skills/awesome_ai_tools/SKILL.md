---
id: awesome_ai_tools
name: Awesome Ai Tools
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
    description: Reference knowledge and templates from awesome_ai_tools.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["llm", "ai"]
---

# Awesome Ai Tools

## Overview
> A curated list of Artificial Intelligence Top Tools

## Usage
Agents working on `llm-tooling` domain tasks should reference this skill.
See `payload/` for the full source code and implementation patterns.

## Key Capabilities
- Domain: `llm-tooling`
- Source code available in `payload/`
- Tags: llm, ai

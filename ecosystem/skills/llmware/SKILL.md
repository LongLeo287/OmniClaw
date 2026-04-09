---
id: llmware
name: Llmware
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
    description: Provides reference knowledge and source templates from the llmware repository.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["llm", "ai"]
---

# Llmware

## Overview
![Static Badge](https://img.shields.io/badge/python-3.10_%7C_3.11%7C_3.12%7C_3.13%7C_3.14-blue?color=blue)

## Usage
This skill provides reference architecture, patterns, and code templates from the `llmware` repository.
Agents working on `llm-tooling` tasks should consult this skill and reference `payload/` for concrete examples.

## Key Capabilities
- Domain expertise: `llm-tooling`
- Reference source code available in `payload/`
- Tags: llm, ai

---
id: antigravity_mobile
name: Antigravity Mobile
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
    description: Reference knowledge and templates from antigravity_mobile.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["llm", "ai"]
---

# Antigravity Mobile

## Overview
Mobile dashboard and admin panel for [Antigravity IDE](https://antigravity.google). Monitor conversations, manage your agent, and get notified — all from your phone.

## Usage
Agents working on `llm-tooling` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `llm-tooling`
- Source templates available in `payload/`
- Tags: llm, ai

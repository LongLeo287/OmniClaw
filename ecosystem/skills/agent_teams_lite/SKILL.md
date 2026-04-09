---
id: agent_teams_lite
name: Agent Teams Lite
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
    description: Reference knowledge and templates from agent_teams_lite.
    input: query string
    output: code snippets, documentation
consumed_by: []
emits_events: []
listens_to: []
tags: ["agent", "orchestration"]
---

# Agent Teams Lite

## Overview
> **This project has been deprecated in favor of [`gentle-ai`](https://github.com/Gentleman-Programming/gentle-ai).**

## Usage
Agents working on `agent-framework` tasks should reference this skill.
See `payload/` for the full source code and implementation patterns.

## Key Capabilities
- Domain: `agent-framework`
- Source templates in `payload/`

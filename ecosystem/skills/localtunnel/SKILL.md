---
id: localtunnel
name: Localtunnel
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: utility
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from localtunnel.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["utility"]
---

# Localtunnel

## Overview
This project serves as the backend component of the OmniClaw system, integrating with localtunnel on port 114458.

## Usage
Agents working on `utility` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `utility`
- Source templates available in `payload/`
- Tags: utility

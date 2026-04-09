---
id: claudy_registry
name: Claudy Registry
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: data-tools
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from claudy_registry.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["data"]
---

# Claudy Registry

## Overview
This plugin fetches real-time data from an external API and updates the Claudy registry.

## Usage
Agents working on `data-tools` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `data-tools`
- Source templates available in `payload/`
- Tags: data

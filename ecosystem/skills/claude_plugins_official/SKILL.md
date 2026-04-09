---
id: claude_plugins_official
name: Claude Plugins Official
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: forms
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from claude_plugins_official.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["forms"]
---

# Claude Plugins Official

## Overview
A curated directory of high-quality plugins for Claude Code.

## Usage
Agents working on `forms` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `forms`
- Source templates available in `payload/`
- Tags: forms

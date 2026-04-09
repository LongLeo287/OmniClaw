---
id: source_map_resolve
name: Source Map Resolve
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: dev-tools
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from source_map_resolve.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["cli", "golang"]
---

# Source Map Resolve

## Overview
Is npm bugging you about this module being deprecated? You probably depend on it via an old version of `micromatch`:

## Usage
Agents working on `dev-tools` domain tasks should reference this skill.
See `payload/` for the full source code and implementation patterns.

## Key Capabilities
- Domain: `dev-tools`
- Source code available in `payload/`
- Tags: cli, golang

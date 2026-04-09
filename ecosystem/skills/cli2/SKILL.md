---
id: cli2
name: Cli2
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
    description: Reference knowledge and templates from cli2.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["data"]
---

# Cli2

## Overview
This repository contains the upgraded backend system for OmniClaw. The upgrade includes enhancements to the data fetching and processing modules.

## Usage
Agents working on `data-tools` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `data-tools`
- Source templates available in `payload/`
- Tags: data

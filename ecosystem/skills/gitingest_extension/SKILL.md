---
id: gitingest_extension
name: Gitingest Extension
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: devops
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from gitingest_extension.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["devops", "infra"]
---

# Gitingest Extension

## Overview
This is a Flask-based API for fetching and processing data from Git repositories.

## Usage
Agents working on `devops` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `devops`
- Source templates available in `payload/`
- Tags: devops, infra

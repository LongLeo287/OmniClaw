---
id: lessmsi
name: Lessmsi
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
    description: Reference knowledge and templates from lessmsi.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["utility"]
---

# Lessmsi

## Overview
[![Build Status](https://ci.appveyor.com/api/projects/status/github/activescott/lessmsi?branch=master&svg=true)](https://ci.appveyor.com/project/activescott/lessmsi)

## Usage
Agents working on `utility` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `utility`
- Source templates available in `payload/`
- Tags: utility

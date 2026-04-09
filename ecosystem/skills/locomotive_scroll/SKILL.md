---
id: locomotive_scroll
name: Locomotive Scroll
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
    description: Reference knowledge and templates from locomotive_scroll.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["utility"]
---

# Locomotive Scroll

## Overview
[![npm version](https://img.shields.io/npm/v/locomotive-scroll.svg)](https://www.npmjs.com/package/locomotive-scroll)

## Usage
Agents working on `utility` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `utility`
- Source templates available in `payload/`
- Tags: utility

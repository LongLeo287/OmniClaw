---
id: openclaw_admin
name: Openclaw Admin
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: networking
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from openclaw_admin.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["proxy", "networking"]
---

# Openclaw Admin

## Overview
Bảng Quản Trị giao diện Web (Web UI) hiện đại, chuyên nghiệp dành cho hệ thống **OpenClaw**.

## Usage
Agents working on `networking` domain tasks should reference this skill.
See `payload/` for the full source code and implementation patterns.

## Key Capabilities
- Domain: `networking`
- Source code available in `payload/`
- Tags: proxy, networking

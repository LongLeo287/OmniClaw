---
id: firecrawl_mcp_server
name: Firecrawl Mcp Server
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: llm-tooling
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from firecrawl_mcp_server.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["llm", "ai"]
---

# Firecrawl Mcp Server

## Overview
src="https://raw.githubusercontent.com/firecrawl/firecrawl-mcp-server/main/img/fire.png"

## Usage
Agents working on `llm-tooling` tasks should reference this skill.
Inspect `payload/` for concrete source code and implementation patterns.

## Key Capabilities
- Domain: `llm-tooling`
- Source templates available in `payload/`
- Tags: llm, ai

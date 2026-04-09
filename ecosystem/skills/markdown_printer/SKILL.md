---
id: markdown_printer
name: Markdown Printer
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: doc-tools
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Reference knowledge and templates from markdown_printer.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["markdown", "documents"]
---

# Markdown Printer

## Overview
Save web pages as Markdown files with preserved formatting. **Zero setup required** - just install and start saving!

## Usage
Agents working on `doc-tools` domain tasks should reference this skill.
See `payload/` for the full source code and implementation patterns.

## Key Capabilities
- Domain: `doc-tools`
- Source code available in `payload/`
- Tags: markdown, documents

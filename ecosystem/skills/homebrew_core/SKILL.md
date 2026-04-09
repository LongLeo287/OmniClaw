---
id: homebrew_core
name: Homebrew Core
version: 1.0.0
tier: 3
status: active
author: OA Forge Pipeline
updated: 2026-04-09
domain: package-management
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Claude Code
dependencies: []
exposed_functions:
  - name: reference
    description: Provides reference knowledge and source templates from the homebrew_core repository.
    input: query string
    output: code snippets, documentation, patterns
consumed_by: []
emits_events: []
listens_to: []
tags: ["homebrew", "packages", "macos"]
---

# Homebrew Core

## Overview
Core formulae for the Homebrew package manager.

## Usage
This skill provides reference architecture, patterns, and code templates from the `homebrew_core` repository.
Agents working on `package-management` tasks should consult this skill and reference `payload/` for concrete examples.

## Key Capabilities
- Domain expertise: `package-management`
- Reference source code available in `payload/`
- Tags: homebrew, packages, macos

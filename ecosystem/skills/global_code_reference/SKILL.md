---
id: global_code_reference
name: Global Codebases Reference Vault
version: 1.0.0
tier: 3
status: active
author: Antigravity
updated: 2026-04-09
domain: reference
cost_tier: standard
load_on_boot: false
accessible_by:
  - Orchestrator
  - Engineering Department
  - Antigravity
dependencies: []
exposed_functions:
  - name: read_codebase
    description: >
      Access and explore the 18.4GB global knowledge base of 309 major open-source 
      repositories (VSCode, PyTorch, Node.js, DeepSpeed, etc.) for architectural 
      reference, best practices, and code learning.
    input: "{ repo_name: string, query: string }"
    output: "Source code snippets, architecture maps, and documentation from the vault"
consumed_by:
  - Orchestrator
  - Engineering Department
emits_events:
  - reference.knowledge.accessed
listens_to: []
tags: ["knowledge-base", "source-code", "reference", "tier-3", "vault"]
---

# Global Codebases Reference Vault

## Overview
This skill grants access to the `vault/knowledge/global_codebases/` data lake. 
The data lake contains 18.4 GB of raw source code comprising 309 major open-source projects.
This is meant strictly as a **Reference Knowledge Base**, not as active executables.

## Key Capabilities
- **Massive Context**: Includes major projects like PyTorch, VSCode, NodeJS, DeepSpeed.
- **Architectural Reference**: Allows engineering agents to analyze real-world production codebases.
- **Pattern Learning**: Useful for extracting complex design patterns, tooling configurations, and language-specific optimizations.

## Agent Instructions
- Use this skill when you need to research how large open-source projects approach a specific problem.
- **Location**: All source repositories are permanently housed at: `$OMNICLAW_ROOT/vault/knowledge/global_codebases/`
- Do NOT modify the contents of the vault. It is read-only reference data.

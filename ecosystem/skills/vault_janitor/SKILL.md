---
id: vault_janitor
name: OmniClaw Vault Janitor
version: 1.0.0
tier: 2
status: active
author: Antigravity
updated: 2026-04-09
domain: utility
cost_tier: free
load_on_boot: false
accessible_by:
  - Orchestrator
  - Engineering Department
  - Antigravity
dependencies: []
exposed_functions:
  - name: audit_directory
    description: Recursively checks directory size, file count, and lists empty subdirectories.
    input: "{ dir_path: string }"
    output: "{ dir_count: int, file_count: int, total_size_kb: float, empty_dirs: list[str] }"
  - name: sweep_empty_folders
    description: Purges empty husk folders recursively within a given directory.
    input: "{ dir_path: string }"
    output: "{ status: str, purged: int }"
  - name: merge_payloads
    description: Move raw code from a source directory into the payload of a target directory.
    input: "{ source_dir: string, target_dir: string, overwrite: bool }"
    output: "{ status: str, moved_items: int }"
consumed_by:
  - Orchestrator
  - Engineering Department
emits_events:
  - janitor.folder.swept
  - janitor.payload.merged
listens_to: []
tags: ["cleanup", "maintenance", "sysadmin", "audit"]
---

# Vault Janitor Skill

A system administration utility tool inside the OmniClaw Ecosystem for maintaining the cleanliness of the Graph and Vault directories. This consolidates all standard Python clean-up scripts into a single reusable skill.

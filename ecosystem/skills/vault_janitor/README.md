# Vault Janitor Toolkit

**Skill ID:** `vault_janitor` | **Domain:** `utility` | **Tier:** 2

## Summary
The OmniClaw Vault Janitor is a suite of tools that combines common auditing, merging, and clean-up functions for maintaining the ecosystem's directory structures. It replaces the 100+ ad-hoc Python scripts previously deployed to `vault/tmp/`.

## Usage
Agents can import this skill to clean up dropzones, investigate raw repo capacities, merge payload directories after graph-syncs, and systematically destroy empty directories leftover by scrapers.

## Available Modules (`janitor.py`):
1. `audit_directory(path)`
2. `sweep_empty_folders(path)`
3. `merge_payloads(src, target)`

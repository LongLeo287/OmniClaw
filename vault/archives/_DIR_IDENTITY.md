---
id: vault-archives
type: directory-manifest
owner: OMA
tags: [archives, legacy, backup, logs]
status: empty_shell
---

# `vault/archives/` - THE GLACIER ARCHIVE

> [!CAUTION]
> **OMA ENFORCED**: Cemetery Zone and Cold Memory Logs. Continuous Write/Delete operations strictly forbidden.

## Core Rules (Strict Rules):
1. **CONTAINS ONLY**: Old system logs (`logs/`), Primitive system structures (`legacy_system_backup/`), Redundant Zip archives.
2. **READ-ONLY LAW**: Files moved to Archive are considered mummified. Agents are strictly prohibited from parsing files out of Archive, editing them, and copying them back. Full Archive retrieval operations are exclusively reserved for Restoration or Historical Analysis.
3. **OMA Deepscan**: OMA will treat this space lightly, hence execution of hidden scripts is blocked.

> Note: This directory is currently empty (contains no data files) and awaits OIW intake.

---
id: knowledge_boundary
name: Knowledge Base Boundary Policy
authority: OER
status: ACTIVE
date: 2026-04-10
---

# Knowledge Base Boundary Policy

## Storage Decision

**Primary Data Storage:** Local `$OMNICLAW_ROOT/brain/knowledge/`
**Backup Vectors:** Google Drive (via Mount point)

## Protected Zones

> [!CAUTION]
> Git Commits of raw knowledge data (PDfs, heavy datasets extracted by OIW) are **FULLY EXCLUDED**.
> Agents MUST NEVER run `git add` on the `brain/knowledge/` directory.

OER (Entity Registrar) holds the exclusive right to index documents located in `brain/knowledge`. 
Agents may fetch context using semantic/lexical queries against `FAST_KNOWLEDGE_INDEX.json`, but all structural updates belong strictly to OER.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*

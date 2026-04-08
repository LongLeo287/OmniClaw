---
id: knowledge_boundary
name: Knowledge Base Boundary Policy
authority: OER
status: ACTIVE
date: 2026-04-06
---

# Knowledge Base Boundary Policy

## Storage Decision (2026-04-06)

**Primary Data Storage: HuggingFace Dataset + Google Drive**
- NOT backup — this is the official primary storage
- HuggingFace Dataset repo: `longleo/omniclaw-knowledge-base`
- Google Drive: Shared Drive (mount point for access)
- Git: **FULLY EXCLUDED** — no commits, no push

## Protected Zones

### ZONE-KB-001: `brain/knowledge/` — PROTECTED KNOWLEDGE BASE
- **Policy:** NO_TOUCH — Read-Only for all Daemons
- **Git Status:** EXCLUDED
- **Primary Storage:** HuggingFace Dataset + Google Drive
- **Size:** ~6.8 GB (post-cleanup 2026-04-06)
- **OER Owner:** OER Daemon

### Monitored Paths

| Path | Policy | Rationale |
|---|---|---|
| `brain/knowledge/general/` | NO_TOUCH | 5.88 GB knowledge dumps — core KB |
| `brain/knowledge/repositories/` | NO_TOUCH | FETCHED source repos |
| `brain/knowledge/api/` | NO_TOUCH | API source repos |
| `brain/knowledge/repos/` | READ_ONLY | Junction links — managed by OHD |
| `brain/knowledge/library/` | NO_TOUCH | Curated docs |
| `brain/knowledge/bmad_repo/` | NO_TOUCH | BMAD methodology |
| `brain/knowledge/skills_standard_repo/` | NO_TOUCH | Skills standards |
| `brain/knowledge/claude_bp_repo/` | NO_TOUCH | Claude best practices |
| `storage/vault/ARCHIVE/` | NO_TOUCH | CIV cold storage vault |

## Absolute Rules

1. No file deletion in `brain/knowledge/` without OER approval
2. No migration to Vault (architectural decision 2026-04-06 — keep in place)
3. No Git commits of `brain/knowledge/` content
4. Additions: append to appropriate subfolder — no restructuring
5. `storage/vault/ARCHIVE/` is strictly for CIV repos — not mixed with knowledge base
6. Sync to HuggingFace + Google Drive on significant content change — not periodic backup

## Registry Reference

- SKILL_REGISTRY: 3,788 entries
- FAST_INDEX: 3,111 entries (knowledge_base section)
- ORG_GRAPH: knowledge_base node + 10 department edges
- KNOWLEDGE_MAP: `brain/registry/KNOWLEDGE_MAP.md`
- Sync script: `core/ops/scripts/sync_knowledge_data.py`

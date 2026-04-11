# OmniClaw FAST Indices ⚡

**Path:** `brain/indices/`
**Namespace:** `brain.indices`
**Status:** V5.0 (Standardized & Deterministic)

This directory is the **High-Speed Cache Layer** of the OmniClaw OS. It contains flattened, serialized JSON maps of the entire deep-nested ecosystem. 

## 🚀 Why This Folder is Masterful

In a standard OS, when an AI agent needs to find a specific skill, workflow, or knowledge snippet, it would have to painfully crawl through `ecosystem/` or `vault/` folder by folder. 
**With `brain/indices/`**, we completely eliminate file-crawling latency and **fake signals**.

### Core Architecture:
Instead of recursive file traversal and trusting corrupted metadata tags, OmniClaw daemons execute `omniclaw rebuild-index` to scan the universe of `_DIR_IDENTITY.md` markers and compile them into pristine O(1) lookup tables based purely on **Physical Location (Namespaces)**. 

When an agent boots up, it instantly loads these JSON indices into its context, providing 100% true mapping of the real system topology.

### The 6 Pillar Indices:
1.  **`FAST_KNOWLEDGE_INDEX.json`**: The largest file. Maps every single piece of ingested knowledge inside the Vault.
2.  **`FAST_SKILL_INDEX.json`**: Maps all Python/CLI skills strictly across `ecosystem/skills/`.
3.  **`FAST_AGENT_INDEX.json`**: Maps 30 true sub-agent identities purely from `ecosystem/workforce/departments/`.
4.  **`FAST_WORKFLOW_INDEX.json`**: Maps all multi-step procedural sequences.
5.  **`FAST_PLUGIN_INDEX.json`**: Maps all third-party integrations.
6.  **`FAST_DOCUMENT_INDEX.json`**: Maps core rulebooks and global documents.

---

> 💡 **Developer Note:**
> Do not modify `.json` files in this directory manually. These are **auto-compiled artifacts**. If you add a new skill or knowledge dump, the OS daemons will eventually re-generate these indexes to reflect the changes. Use `omniclaw rebuild-index` if a manual forced refresh is required.

---
*OmniClaw V5.0 Blueprint | Forged by Antigravity OS Architect | brain.indices | 2026-04-11*

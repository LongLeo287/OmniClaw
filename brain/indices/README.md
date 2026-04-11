# OmniClaw FAST Indices ⚡

**Path:** `brain/indices/`
**Namespace:** `brain.indices`
**Status:** V5.0 (Standardized)

This directory is the **High-Speed Cache Layer** of the OmniClaw OS. It contains flattened, serialized JSON maps of the entire deep-nested ecosystem. 

## 🚀 Why This Folder is Masterful

In a standard OS, when an AI agent needs to find a specific skill, workflow, or knowledge snippet, it would have to painfully crawl through `ecosystem/` or `vault/` folder by folder. 
**With `brain/indices/`**, we completely eliminate file-crawling latency.

### Core Architecture:
Instead of recursive file traversal, OmniClaw daemons regularly run automated indexing scripts (e.g., `rebuild_fast_index`) that scan the universe of `_DIR_IDENTITY.md` markers and compile them into O(1) lookup tables here. 

When an agent boots up (via `gemini.md` or `claude.md`), it instantly loads these JSON indices into its context.

### The 6 Pillar Indices:
1.  **`FAST_KNOWLEDGE_INDEX.json`**: The largest file (~1MB). Maps every single piece of ingested knowledge.
2.  **`FAST_SKILL_INDEX.json`**: Maps all Python/CLI skills across `ecosystem/skills/`.
3.  **`FAST_AGENT_INDEX.json`**: Maps all sub-agent identities and capabilities.
4.  **`FAST_WORKFLOW_INDEX.json`**: Maps all multi-step procedural sequences.
5.  **`FAST_PLUGIN_INDEX.json`**: Maps all third-party integrations.
6.  **`FAST_DOCUMENT_INDEX.json`**: Maps core rulebooks and global documents.

---

> 💡 **Developer Note:**
> Do not modify `.json` files in this directory manually. These are **auto-compiled artifacts**. If you add a new skill or knowledge dump, the OS daemons will eventually re-generate these indexes to reflect the changes. Use `aos rebuild-index` if a manual forced refresh is required.

---
id: ki_2026_04_03_vault_legacy_assimilation
type: knowledge-item
owner: OHD_MEDICAL
domain: architecture
tags: [post-mortem, memory-management, vault-purge, zero-waste]
timestamp: 2026-04-03
---

# 📚 POST-MORTEM: The Vault Legacy Assimilation

## 1. The Anomaly (Error Context)
Historically, the system allowed LLM agents (Claude, Gemini, NullClaw) and automated legacy scripts to dump temporary memory states, API logs, and unverified data chunks into hidden dot-directories (e.g., `.claude`, `.gemini`) or uncontrolled spaces. Over time, these stray logs congregated inside `vault/archives/`. 

Because `OMA_SYSTEM_MAP` possessed an Iron Rule to ignore these hidden and legacy folders, the data became completely isolated—turning the Vault into a massive memory blind spot that consumed immense physical disk space and slowed down global Git tracking and file traversal.

## 2. Hard Rule Extracted (The Cure)
As authorized by the **OA Chief Agent** function: *Errors fuel evolution*. We have distilled the failure into the following strict systemic laws:

- **RULE 1 (Absolute Zero-Waste):** Agents are strictly forbidden from maintaining personalized hidden `.agent` memory storage at the root or within the Vault. All persistent dynamic context MUST be pushed officially to `brain/memory/` or handled directly in SQLite.
- **RULE 2 (OMA Compliance):** The Vault is not a black hole. It must remain purely structural. Temporary RAG chunks or unprocessed system caches must be set to auto-expire or be explicitly tracked by `vault/tmp/quarantine/`.
- **RULE 3 (Purge Before Push):** Avoid saving immense RAG context `.json` and `stdout` `.md` traces permanently. Compress them conceptually into `knowledge-item` summaries.
- **RULE 4 (The Innovation Clause):** Agents and Daemons must not rigidly delete standalone modules or orphaned scripts without evaluation. If a functional utility (e.g., `deep_translator`) is found out-of-bounds, it must be reported for potential adoption into `ecosystem/skills/` rather than blindly destroyed.

## 3. The Resolution
On April 3rd, 2026, the OA Assimilation protocol was invoked. The entire historical backup logs in `vault/archives/` were compressed into this single conceptual memory map. The physical presence of thousands of `.md`, `.json`, and text traces inside the archive was systematically purged by the CEO's `Empty Trash` directive.

`POST_MORTEM_DONE: TRUE`

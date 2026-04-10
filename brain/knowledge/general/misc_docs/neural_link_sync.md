---
id: neural-link-sync
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:11.436760
---

# neural-link-sync.md — Knowledge Graph & Registry Synchronization
# Version: 1.1 | Updated: 2026-03-26
# Department: [DEPT-07] KNOWLEDGE & REGISTRY CAPABILITY (Archivist Agent)
# Mode: EVENT-DRIVEN (Only scans when new data arrives, optimizes Quota/Context)
# Trigger: End of STEP 5 of `content-intake-flow.md` or manual command `omniclaw neural sync`

---

## 1. Purpose
OmniClaw's Global Architecture Map (Neural Link) cannot be a dead file. Whenever a new Repo is ingested through the Intake process, or deleted, the system must update the diagram immediately so that AI Assistants (Antigravity, Claude Code) don't lose their orientation.

This process guides the `Archivist Agent` to update the 3D Awareness Network through the Master Registry and Core Brain (LightRAG).

## 2. Sync Routine

**Step 1: Build Registry (Index Build)**
- Execution command: `python "$OMNICLAW_ROOT\system\ops\scripts\registry_indexer.py"`
- Action: Full scan of all Repos, Plugins, Tools in both Hemispheres (Local Core & Remote Ecosystem). Update list of 300+ Entities into `$OMNICLAW_ROOT\system\registry\SYSTEM_INDEX.yaml`.

**Step 2: Semantic Data Feed (Narrative Feed)**
- Execution command: `python "$OMNICLAW_ROOT\system\ops\scripts\graph_feeder.py"`
- Action: Translate static Configuration files (YAML) into semantic text (Narrative Text) so RAG machine learning can map it. Output file `SYSTEM_INDEX_NARRATIVE.txt`.

**Step 3: Weave Network (Graph Injection)**
- Execution command: Trigger `LightRAG.insert` through Script or Adapter with input being the Narrative file just generated.
- Result: The system's 3D space is successfully woven. AI can query `Which branch does Ai belong to, which Repo is Ai connected to`.

## 3. Agent Retrieval Rules
All Agents when receiving a Task from CEO (Example: "Open tool X", "Check repo Y"):
1. READ `SYSTEM_INDEX.yaml`: To get absolute coordinates without scanning disk.
2. USE `GitNexus MCP`: If need to deep dive into that repo's AST structure.
3. AVOID: Blind `find` or `ls -R` commands cause memory pollution.

---
> "Know yourself and know your enemy, you will win a hundred battles. An AI that doesn't know where it is in the system is just a useless machine." - OmniClaw Architect.

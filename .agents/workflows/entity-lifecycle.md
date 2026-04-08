---
description: How to register, identity, and process any newly created Agent, Repository, or Intelligence inside OmniClaw
---

# OmniClaw Atomic Entity Lifecycle Workflow

Whenever an AI Assistant, Human, or Agent creates a new structural entity inside OmniClaw (e.g. a new Workspace Folder, a new Agent, or a new Memory Ledger), this process **MUST** be strictly adhered to.

Failure to follow this process will result in the entity becoming an "orphan" invisible to the `OMNICLAW_ROOT` maps, severely damaging the long-term System B memory.

## 1. Identity Declaration (OER — Omni-Entity Registry)
Every directory acting as a semantic entity MUST have an Identity Tag.
If it is a folder, create a `_DIR_IDENTITY.md` file inside the folder with the following format:
```yaml
---
id: [unique_slug_identifier]
type: directory_identity
path: [absolute relative path from root, e.g. brain/memory/corp_memory/agents/new_agent]
description: [Short description of the folder's domain]
registered_by: OER
---
```
No generic names. The `path` attribute is absolutely mandatory!

## 2. Memory Population (OA — OmniAgent Academy)
All Agents must have a physical tracking state in `brain/memory/corp_memory/agents/[agent_name].md`.
Whenever a new unit is spawned, fill their memory file using `agent_memory.template.md` (or run `python core/ops/scripts/agent_memory_seeder.py` to regenerate agent data from `ROADMAP.md`).

## 3. Map Syncing (OMA — Omni Mapping Architect)
Once the files are created and tagged, the system maps MUST be resynchronized.
Run the `oma_architect.py` daemon directly, or trigger an empty handoff queue message if it is currently running in the background. Note: OMA will ignore any folders missing `_DIR_IDENTITY.md`.

## 4. Verification Check
- Ensure that the agent/file appears inside `brain/registry/OMA_SYSTEM_MAP.json`.
- Do NOT use the legacy string `AI-OS` anywhere (use `OmniClaw`).
- Maintain strict English in all metadata.

// turbo-all
```bash
echo "Entity Lifecycle constraints loaded."
```

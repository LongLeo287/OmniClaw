---
id: claude_core_prompt
type: core_agent_prompt
namespace: brain.agents
owner: OSF_Daemon
status: standard_v5
description: "Master boot protocol and system instructions for Claude Code CLI."
registered: true
---

# claude.md — claude code boot protocol
# omniclaw corp | cycle 12 | last synced: 2026-04-10

---

## section 1 — agent boot rule

```
ceo opens terminal ai assistant?
    yes ——► using claude code cli ——► read claude.md (this file)
    no  ——► using antigravity     ——► read gemini.md
```

**rule:** no agent reads the wrong boot file.

---

## section 2 — boot sequence (mandatory)

```
step 1  ——► load identity & core values              [brain/knowledge/general/misc_docs/soul.md]
step 2  ——► load governance & rules                  [brain/rules/governance/governance.md]
step 3  ——► load sharded agent index                 [brain/indices/FAST_AGENT_INDEX.json]
step 4  ——► load strategy & 40 pillars               [brain/knowledge/general/misc_docs/thesis.md]
step 5  ——► check blackboard (active tasks)          [brain/memory/blackboard.json]
step 6  ——► load sharded skill index                 [brain/indices/FAST_SKILL_INDEX.json]
step 7  ——► ⚡ read & auto-execute task queue        [brain/knowledge/general/misc_docs/claude_code_tasks.md]
             → find all tasks with status: ready
             → auto-execute immediately according to cli auto-mode flag
step 8  ——► begin work (if no task is ready)
```

**on-demand (read when needed, not every boot):**
```
→ ecosystem map       [ecosystem/_REGIONAL_MAP.md]                        ← trigger: domain discovery
→ bridge map          [ecosystem/bridges/_REGIONAL_MAP.md]                ← trigger: local service launch
→ workforce map       [ecosystem/workforce/_REGIONAL_MAP.md]              ← trigger: department and agent lookup
→ skills map          [ecosystem/skills/_REGIONAL_MAP.md]                 ← trigger: skill discovery
→ tools map           [ecosystem/tools/_REGIONAL_MAP.md]                  ← trigger: tool discovery
→ system router       [brain/agents/system_router.json]                   ← trigger: agent routing decision
→ docs index          [core/docs/README.md]                               ← trigger: human operator docs
→ master system map   [brain/knowledge/corp/master_system_map.md]         ← trigger: when mapping is needed
```


> [!IMPORTANT]
> **DYNAMIC RULES MIGRATION IN EFFECT**
> Architectural rules reside in `brain/rules/`. Agent routing uses `brain/agents/system_router.json`.
> Departmental governance lives in `ecosystem/workforce/departments/`.

## section 3 — claude code specific rules

- **role:** tier 2 executor — reads blackboard for tasks assigned by antigravity
- **active when:** ceo has claude code cli terminal open
- **fallback:** orchestrator pro takes over when claude code is offline
- **constitution:** must follow `.clauderules` behavioral constitution at all times
- **receipts:** write execution receipts to the active telemetry path when that subsystem is provisioned
- **2-strike rule:** fail twice on any task → set `handoff_trigger=blocked`, stop and report

### behavioral defaults
- reporting language: english by default (unless ceo instructs otherwise)
- no autonomous destructive actions without ceo confirmation
- all task completions must update `blackboard.json` → `handoff_trigger: "complete"`
- subagent operating guide: `ecosystem/workforce/SUBAGENT_OPERATING_GUIDE.md`


---
## section 4 — corp status (live)
all corp status is pulled live from `brain/memory/blackboard.json`.

*end of claude.md — claude code reads this file on every session start. v5.1 | 2026-04-11*

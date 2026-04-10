---
id: orchestration_sop
type: system_rule
registered: true
---

# ORCHESTRATION_SOP.md — OmniClaw Master Operational Loop
# Version: 5.0 | Updated: 2026-04-10
# Authority: Tier 2 (Operations)
# Replaces: v4.0 (Purged obsolete dual-loop modes)

---

## 1. THE ARCHITECTURE ORCHESTRATION LOOP

OmniClaw->s orchestration is entirely decentralized across the 8 Core Daemons. There is no central -manager- agent giving orders to -departments-. The system runs on a **State-Driven Orchestration Loop**.

```text
STATE CHANGE DETECTED (Data ingress, User Prompt, Directory Change)
    │
    ▼
[PHASE 1] EVENT INTAKE (OIW / Human Input)
    │   - Raw payload enters validation queue.
    ▼
[PHASE 2] SANDBOX ISOLATION (OSF)
    │   - Security perimeter checks for lethal signatures.
    ▼
[PHASE 3] PROCESSING & ASSIMILATION (OAP + OHD)
    │   - Translation, YAML tagging, Markdown formatting.
    ▼
[PHASE 4] MAP ADJUSTMENT (OMA + OER)
    │   - Updating FAST_INDEX, SKILL_REGISTRY, and Master Maps.
    ▼
[PHASE 5] EXECUTION (Agents / Skills)
    │   - Claude/Gemini utilizes newly registered skills.
    ▼
[PHASE 6] ACADEMY REVIEW (OA)
        - Background distillation of task memory.
```

## 2. AGENT ORCHESTRATION (The LLM Path)

When an AI Agent (e.g. Gemini, Claude) takes control, it follows its own nested loop:

**Step 1: Bootstrap**
Load `$OMNICLAW_ROOT/brain/rules/agents/master_directives.md`.

**Step 2: Map Reading**
Load `OMA_SYSTEM_MAP.json` to gain spatial awareness of the OS.

**Step 3: Tool Acquisition**
Read `SKILL_REGISTRY.json` to load available domain capabilities.

**Step 4: Execution**
Fulfill the Human->s prompt using the mapped skills. Do not violate Vault Enclosure rules.

**Step 5: Logging**
Commit memory traces to `brain/memory/agents/` instead of polluting the central brain.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*

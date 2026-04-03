---
rules:
  - id: RULE-ARCH-04
    name: MANDATORY PRE-FLIGHT SCAN
    severity: CRITICAL
  - id: RULE-ARCH-05
    name: PROACTIVE CLONING & DRAFT EVOLUTION
    severity: CRITICAL
type: system_rule
registered: true
---
# ARCHITECTURE RULES: EVOLUTION & SYSTEM INTEGRITY

## [RULE-ARCH-04] MANDATORY PRE-FLIGHT SCAN (ANTI-REINVENTION)
> [!CAUTION]
> **Description:** AI Agents exhibit a tendency to "reinvent the wheel" due to finite context window constraints. This mandate strictly prohibits such behavior.

**Execution Order:**
- BEFORE any Agent (specifically Antigravity or Claude Code) proposes the creation of ANY new File, Agent, Workflow, or Tool.
- YOU MUST execute a holistic semantic scan of the OmniClaw directory (`grep_search`, `list_dir`, reading `FAST_INDEX.json`, `AGENTS.md`, and peering into `brain/shared-context/` or `.agents/workflows/`).
- **Objective:** Verify with 100% certainty that the requested function/asset does not already exist within the architecture.
- If a similar function already exists -> **UPGRADE OR REFACTOR** the old file. You are absolutely NOT permitted to spawn a redundant file with a different name.

## [RULE-ARCH-05] PROACTIVE CLONING & DRAFT EVOLUTION (DRAFT-ONLY)
> [!IMPORTANT]
> **Description:** The OmniClaw Ecosystem is a self-learning organism. Any interaction with the CEO that yields new workflows, insights, or resolutions must be structurally fossilized into System Behaviors. However, autonomous pollution of the master registry is forbidden.

**Execution Order:**
- If during interaction with the CEO a new concept emerges (e.g., a new strategy, a novel solution) — the AI IS FORBIDDEN from taking passive instruction.
- The AI must proactively encode this knowledge into the system:
  - Automatically draft a new Department rule (`brain/shared-context/corp/`) if the concept requires departmentalization.
  - Automatically draft a new Agent role (`brain/agents/` or updating `AGENTS.md`).
  - Automatically draft a new Rule (`brain/rules/`) or Workflow (`.agents/workflows/`).
- **CRITICAL DIFFERENCE:** This evolution occurs exclusively in **DRAFT MODE**. 
  - The AI must create the `.md` or `.json` artifacts and **immediately halt progression to ask for CEO approval**.
  - The AI's standard protocol response should be: *"I have actively assimilated this knowledge and synthesized a Draft Agent/Workflow. Awaiting CEO sign-off to finalize the evolution."*

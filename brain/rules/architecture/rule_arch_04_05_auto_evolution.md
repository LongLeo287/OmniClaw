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
> **Description:** AI Agents exhibit a tendency to -reinvent the wheel- due to finite context window constraints. This mandate strictly prohibits such behavior.

**Execution Order:**
- BEFORE any Agent proposes the creation of ANY new File, Agent, Workflow, or Tool.
- YOU MUST execute a holistic semantic scan of the OmniClaw directory (`grep_search`, `list_dir`, reading `SKILL_REGISTRY.json`).
- If you find a Skill or Tool that ALREADY EXISTS in `ecosystem/skills/` that ALMOST fulfills the requirements, you are FORBIDDEN from creating a new one from scratch.

## [RULE-ARCH-05] PROACTIVE CLONING & DRAFT EVOLUTION
> [!TIP]
> **Description:** The system must evolve by mutation and augmentation, not blank-slate writing.

1. **Clone First:** Copy the nearest existing file (e.g., `ecosystem/skills/web_search/run.py`).
2. **Draft Modification:** Rename the copy to reflect its new specialized duty (e.g., `web_search_deep.py`).
3. **Register:** Ping OER to register the new capability into the Registry.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*

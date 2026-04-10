---
id: memory.ledger.heuristics
type: adaptive_patch_ledger
version: 5.0
injection_target: ALL_AGENTS
---

# OmniClaw Adaptive Heuristics (Hotfixes)

> [!NOTE]  
> Agents: Do NOT edit base `agent_behavior.md`. If a recurring error, misunderstanding, or system glitch is encountered, append a Patch at the **Top** of this file to warn future Agents.

---
<!-- ========================================== -->
<!-- ⚠️ APPEND NEW PATCHES DIRECTLY BELOW THIS ⚠️ -->
<!-- ========================================== -->

## PATCH-001: Strict File Read Boundaries 
**Observed Flaw:** Agents executing `cat` commands inside Bash to view code blocks.
**Actionable Heuristic:** NEVER use terminal utilities (`cat`, `type`, `sed`) to read or edit large blocks of structural code natively supported by specialized Agent Tools (`view_file`, `replace_content`). Use standard OS tools ONLY for debugging processes or searching system metrics.

<!-- === END OF ACTIVE PATCHES === -->

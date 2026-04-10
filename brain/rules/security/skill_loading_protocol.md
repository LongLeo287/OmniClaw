---
id: skill_loading_protocol
type: system_rule
registered: true
---

# SKILL_LOADING_PROTOCOL.md — OSF Skill Loading Sandbox
# Version: 2.0 | Updated: 2026-04-10
# Authority: OSF (OmniClaw Sandbox Firewall) & OER (Entity Registrar)

## Purpose

Defines exactly how an Agent safely discovers and invokes a Skill from the `ecosystem/skills/` directory without triggering OSF Kill Commands.

---

## The OSF Loading Constraint

```text
[1] AGENT needs a capability
        │
        ▼
[2] AGENT queries `brain/registry/SKILL_REGISTRY.json`
        │
        ▼
[3] AGENT attempts to execute the `run.py` or `.ps1` of the chosen Skill
        │
        ▼
[4] OSF INTERCEPTS execution.
    - Does this skill exist in SKILL_REGISTRY- (Yes/No)
    - Does the execution contain explicit malicious path[!] (Yes/No)
        │
        ▼
[5] If PASS -> Execution proceeds.
    If FAIL -> Execution blocked, Agent penalized.
```

## Mandatory Lazy Loading
Agents MUST NEVER proactively scan the `ecosystem/skills/` directory using standard file operations. This trips the OSF Sentinel.
Agents MUST read `SKILL_REGISTRY.json` first as the single source of truth for safe availability.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*

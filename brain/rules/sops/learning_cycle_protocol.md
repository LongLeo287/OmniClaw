---
id: learning_cycle_protocol
type: system_rule
registered: true
---

# LEARNING_CYCLE_PROTOCOL.md — OmniClaw Self-Improvement Loop
# Version: 2.0 | Updated: 2026-04-10
# Authority: Tier 2 (Operations)
# Executed by: OA (Academy Daemon) & Cognitive Skills

---

## Purpose

The learning cycle ensures OmniClaw improves its knowledge base and skill library over time.
The system analyzes its own performance, extracts patterns from failure logs, and establishes new static skills to prevent repetitive problem-solving.

---

## The OA Learning Loop

**Trigger:** OA Daemon activates during idle cycles or triggered by an Agent failure threshold.

### Phase 1: Ingestion & Reflection
1. OA reads error logs and task histories from `$OMNICLAW_ROOT/brain/memory/agents/`.
2. OA cross-references `$OMNICLAW_ROOT/brain/registry/SKILL_REGISTRY.json` to identify gap anomalies (What skill was missing that caused the failure-).

### Phase 2: Synthesis (Skill Generation)
1. If a missing capability is requested >3 times, OA automatically triggers a sub-agent (using `cognitive_evolver` skill) to draft a new `SKILL.md` and `schema.json`.
2. The newly crafted weapon is forwarded to the Sandbox Firewall (OSF).

### Phase 3: Registration
1. If OSF approves, the new Skill is merged into `ecosystem/skills/`.
2. OER detects the new Skill and registers it into the system officially.
3. Once registered, Master Agents (Gemini/Claude) can immediately utilize the new Skill in future encounters.

---

## Constraints
- A.I. modules MUST NEVER edit existing core system logic (`core/daemons`) during the learning loop. They may only add new tools to the `ecosystem/skills/` zone.
- All newly minted skills must pass OSF Sandbox checks (No hardcoded credentials, no arbitrary destruct commands).


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*

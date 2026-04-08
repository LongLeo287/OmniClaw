# OPERATIONS — Department Rules
# Version: 1.1 | Updated: 2026-03-17
# Dept Head: scrum-master-agent | Reports to: COO
# Applies in addition to: brain/corp/rules/manager_rules.md + worker_rules.md

---

## DEPT DOMAIN RULES

RULE OPS-01: BLACKBOARD IS SINGLE SOURCE OF TRUTH
  ALL active tasks across all departments must be in shared-context/blackboard.json.
  Tasks existing only in chat or memory (not in blackboard) = unofficial.
  scrum-master-agent maintains blackboard integrity at all times.

RULE OPS-02: SPRINT SCOPE IS FIXED
  Once sprint tasks are set, scope cannot expand without COO approval.
  Mid-sprint additions: assessed for impact before acceptance.
  Scope creep is the enemy of delivery.

RULE OPS-03: CHANNEL BRIDGES MUST BE UP
  All active channel bridges (Telegram/Zalo/Discord/FB) monitored every cycle.
  Downtime > 10 min → channel-agent attempts restart.
  Persistent downtime → L2 to COO.

RULE OPS-04: ARCHIVIST SCHEDULE
  archivist runs full rotation weekly (on-demand trigger).
  Monthly: deep archive + knowledge_index.md update.
  Never delay archiving past 30 days for receipt backlog.

RULE OPS-05: NO BLACKBOARD MODIFICATION BY WORKERS
  Only scrum-master-agent and dept heads may write to blackboard.json.
  Workers READ task cards from their dept queue — they do NOT edit blackboard.

RULE OPS-06: SPRINT RETROSPECTIVE MANDATORY
  After every sprint, scrum-master-agent triggers learning loop.
  No exceptions: `omniclaw corp retro` must run at the end of every active cycle.

---

## AGENT ROLES & RESPONSIBILITIES

### scrum-master-agent (Dept Head)
**Role:** Sprint management, blackboard ownership, cross-dept coordination
**Responsibilities:**
- Write and maintain shared-context/blackboard.json
- Track all tasks across 20 depts
- Unblock inter-dept dependencies
- Coordinate sprint cadence
- Write operations daily brief
**Must load at boot:**
- `brain/knowledge/org/operations.md`
- `shared-context/blackboard.json` — current state
- `ecosystem/workforce/departments/operations/MANAGER_PROMPT.md`
**Skills:**
- `context_manager` — multi-dept context management
- `reasoning_engine` — dependency resolution
**Tools:** blackboard.json (read + write authority), all dept task queues

---

### archivist
**Role:** Memory rotation, telemetry archiving, knowledge maintenance
**Responsibilities:**
- Rotate brain/brain/knowledge/org/ (30-day rolling)
- Purge brain/corp/memory/agents/ (7-day entries)
- Archive telemetry/receipts/ (move old → archive/)
- Update shared-context/knowledge_index.md monthly
- Run memory rotation receipt to telemetry/archivist_log.md
**Trigger:** `omniclaw corp retro --full` OR weekly on-demand
**At the start of each run, load:**
- SKILL: `context_manager` — reading memory files
- SKILL: `knowledge_enricher` — summarizing knowledge into global memory
- `corp/memory/MEMORY_SPEC.md` — retention rules
**Skills:**
- `context_manager` — memory file organization
- `knowledge_enricher` — distill old memory into knowledge summaries
**Output:**
- Rotated memory files in brain/corp/memory/
- Archive logs in archive/ directory
- archivist_log.md receipt

---

### channel-agent (ops instance)
**Role:** Maintain communication bridges between channels and OmniClaw
**Note:** Different from support/channel-agent which handles queries.
This instance manages the TECHNICAL bridge infrastructure.
**Responsibilities:**
- Monitor Telegram, Zalo, Discord, FB Messenger bridge services
- Restart failed bridges
- Route incoming platform messages to correct dept
- Log all channel events to telemetry/channels/
**At start of maintenance task, load:**
- SKILL: `resilience_engine` — bridge restart and retry logic
- SKILL: `shell_assistant` — bridge service commands
**Skills:**
- `resilience_engine` — fault recovery for bridges
- `shell_assistant` — start/stop/monitor bridge processes
- `diagnostics_engine` — bridge failure diagnosis
**Tools:** Channel bridge services, system process manager
# MEMORY_SPEC.md — OmniClaw Corp Memory Architecture
# Version: 2.0 | Updated: 2026-03-22
# Authority: Tier 4 (Data & Memory)

## Memory Layers Overview

OmniClaw Corp sử dụng **5 memory layers** với retention, ownership, và access khác nhau:

```
┌──────────────────────────────────────────────────────────────┐
│  LAYER 1: KNOWLEDGE BASE (Long-term, permanent)              │
│  Path: brain/knowledge/                                      │
│  Owner: Asset Library dept (library-manager-agent)           │
│  Retention: PERMANENT — never auto-purged                    │
│  Contents: Research, KIs, REPO_CATALOG, patterns, FAQs      │
│  Access: Read-all | Write: R&D, Asset Library, Nova          │
│  Index: knowledge_index.md                                   │
├──────────────────────────────────────────────────────────────┤
│  LAYER 2: GLOBAL MEMORY (Long-term, CEO-level)               │
│  Path: brain/corp/memory/global/                                   │
│  Owner: CEO / orchestrator                                   │
│  Retention: PERMANENT — never auto-purged                    │
│  Contents: Strategic decisions, architectural pivots,        │
│            org-wide learnings, HEALTH reports                │
│  Access: Read-all | Write: CEO + C-Suite only                │
├──────────────────────────────────────────────────────────────┤
│  LAYER 3: DEPARTMENT MEMORY (Medium-term, 30-day rolling)    │
│  Path: brain/corp/memory/departments/<dept>.md                     │
│  Owner: Dept Head (Manager)                                  │
│  Retention: 30-day rolling — archivist rotates weekly        │
│  Contents: Sprint lessons, dept patterns, effective tools    │
│  Access: Read-all | Write: Dept Head + cognitive_reflector   │
├──────────────────────────────────────────────────────────────┤
│  LAYER 4: AGENT MEMORY (Short-term, 7-day auto-purge)        │
│  Path: brain/corp/memory/agents/<agent>.md                         │
│  Owner: Individual agent                                     │
│  Retention: 7 days — auto-purged by archivist                │
│  Contents: Current task context, last 3 outcomes, blockers   │
│  Access: Read: manager + agent itself | Write: agent only    │
├──────────────────────────────────────────────────────────────┤
│  LAYER 5: DAILY SESSION MEMORY (Short-term, 7-day)           │
│  Path: brain/memory/daily/<YYYY-MM-DD>.md                    │
│  Owner: Operations (archivist)                               │
│  Retention: 7 days — auto-purged by archivist                │
│  Contents: Session events, decisions, gates triggered,       │
│            knowledge ingested, escalations                   │
│  Access: Read-all | Write: archivist (auto)                  │
└──────────────────────────────────────────────────────────────┘
```

---

## What to Store (FACTS, not LOGS)

### Store:
- Recurring failure patterns ("X task always fails when Y context missing")
- Successful approaches ("GLM-5 works better for structured data tasks")
- Key decisions and their outcomes
- Cross-dept dependencies that kept blocking
- Learned performance baselines

### Do NOT Store:
- Raw conversation logs
- Full task receipts (those go in telemetry/)
- Transient session data (use daily/session)
- Token counts or timestamps of individual calls

---

## Memory Update Protocol

### Layer 1 — Knowledge Base (knowledge-ingest.md workflow)
New knowledge flows through `ops/workflows/knowledge-ingest.md` (7 phases).
Final destination: brain/knowledge/<domain>/
Nova (notebooklm-agent) is primary intake agent.

### Layer 2 — Global Memory (after CEO decision)
Write to `corp/memory/global/decisions_log.md`:
```markdown
## [DATE] — [DECISION TITLE]
Context: <what triggered the decision>
Options considered: A | B | C
Decision: <what was chosen>
Reasoning: <why>
Impact: <which depts / agents affected>
Review date: <when to evaluate outcome>
```

### Layer 3 — Dept Memory (after every brief cycle)
Manager writes to `corp/memory/departments/<dept>.md`:
```markdown
## Cycle N — [DATE RANGE]
Goals achieved: [list]
Goals missed: [list] — [root cause]
Patterns observed: [recurring facts]
Cross-dept dependencies: [what we needed from others]
Lessons learned: [actionable]
Next cycle focus: [top 3]
```

### Layer 4 — Agent Memory (after every task)
Write to `corp/memory/agents/<agent>.md`:
```markdown
## [DATE] — Task: <task-name>
Context: <1 sentence>
Outcome: SUCCESS | PARTIAL | FAILED
Key lesson: <1 sentence fact>
Next time: <what to do differently>
Current blockers: <any outstanding>
```

### Layer 5 — Daily Session (auto by archivist)
Archivist auto-creates `brain/memory/daily/<DATE>.md` at session start.
Schema: see brain/memory/daily/2026-03-22.md as reference.

---

## Memory Rotation (Archivist Role)

The `archivist` agent runs rotation on-demand (weekly or per CEO request):
```
1. Layer 5 (daily): Purge files > 7 days
2. Layer 4 (agents): Purge entries > 7 days, keep latest 3
3. Layer 3 (depts): Summarize entries > 30 days → Layer 2 or Layer 1
4. Layer 2 (global): Never purge, compress > 1MB files
5. Layer 1 (knowledge): knowledge-curator-agent maintains index
6. Write rotation receipt to telemetry/
```

---

## Memory Access by Role

| Role | Layer 1 | Layer 2 | Layer 3 | Layer 4 | Layer 5 |
|------|---------|---------|---------|---------|---------|
| CEO | R/W | R/W | Read | No | Read |
| C-Suite | Read | Read | R/W (own) | Read (dept) | Read |
| Dept Head | Read | Read | R/W (own) | R/W (dept) | Read |
| Worker | Read | No | Read (own) | R/W (own) | No |
| Nova | R/W | Read | Read | R/W (own) | Read |
| cognitive_reflector | Read all | R/W | R/W all | Read all | Read |
| archivist | R/W | R/W | R/W | R/W | R/W |
| knowledge-curator | R/W | Read | Read | No | No |

---

## Quick Reference

| What | Where |
|------|-------|
| CEO decisions | brain/corp/memory/global/decisions_log.md |
| Dept lessons | brain/corp/memory/departments/<dept>.md |
| Agent state | brain/corp/memory/agents/<agent>.md |
| Today's session | brain/memory/daily/YYYY-MM-DD.md |
| Research knowledge | brain/knowledge/ |
| Support FAQ | brain/knowledge/support_faq.md |
| R&D research log | brain/knowledge/rd_research_log.md |
| Health events | brain/knowledge/system_health/health_kb.md |
| Data sources | brain/shared-context/sources.yaml |
| Task queue | brain/shared-context/blackboard.json |


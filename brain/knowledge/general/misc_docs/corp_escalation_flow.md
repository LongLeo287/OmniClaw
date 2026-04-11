---
id: corp-escalation-flow
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:10.338749
---

# Department: operations
# corp-escalation-flow.md â€” L1 â†’ L2 â†’ L3 Escalation Workflow
# Version: 1.0 | Updated: 2026-03-17
# Authority: Tier 2 (Operations) / Corp Mode

---

## Overview

Escalation is how the org handles blockers, failures, and crises.
3 levels â€” each has a defined responder, SLA, and format.

```
WORKER (L1) â”€â”€â–º MANAGER (same session)
    â”‚ (if unresolved or systemic)
MANAGER (L2) â”€â”€â–º C-SUITE (same session)
    â”‚ (if cross-dept or strategic)
C-SUITE (L3) â”€â”€â–º CEO (blocking â€” work pauses)
```

**Key principle:** Never escalate past one level unnecessarily.
Escalate to the level that can actually resolve it.

---

## L1 Escalation: Worker â†’ Manager

**Trigger:** Worker hits 2-strike rule on any task
**Responder:** Dept Head (Manager)
**SLA:** Same work session

**Worker writes to `subagents/mq/<dept>_escalation.md`:**
```markdown
## L1 ESCALATION â€” [TASK-ID] â€” [DATETIME]

Agent: <worker-agent>
Dept: <dept>
Task: <task-id and 1-line description>

Blocker: <specific reason â€” tool failure / ambiguous spec / missing resource>

Attempt 1: <what was tried>
  Result: <what failed and why>

Attempt 2: <different approach tried>
  Result: <what failed and why>

Options considered:
  A. <option> â€” Feasibility: <High/Med/Low>
  B. <option> â€” Feasibility: <High/Med/Low>

Recommendation: A or B and why

Awaiting manager response.
```

**Manager response options:**
- Unblock: provide missing context/resource â†’ worker retries
- Reassign: different worker or approach
- Defer: not needed this cycle â†’ remove from task queue
- Escalate to L2: if systemic or cross-dept dependency

---

## L2 Escalation: Manager â†’ C-Suite

**Trigger:**
- KPI behind threshold (per kpi_targets.yaml)
- Cross-dept blocker persisting > 2 cycles
- 2+ workers fail same task category
- L1 escalation unresolvable at dept level

**Responder:** Relevant C-Suite member
**SLA:** Same session

**Manager writes to `brain/memory/system_memory/escalations.md`:**
```markdown
## L2 ESCALATION â€” [ESC-ID] â€” [DATE]

From: <dept head>
To: <C-Suite role (CTO/CMO/COO/CFO/CSO)>
Priority: HIGH | MEDIUM

Issue: <1-2 sentences>
Evidence:
  - KPI status: <metric> is <value> vs target <target>
  - Root cause hypothesis: <what caused this>
  - What was tried: <list>
  - Cross-dept dependency: <if applicable>

Options:
  A. <resolution option> â€” Impact: / Risk:
  B. <resolution option> â€” Impact: / Risk:

Recommendation: <A or B>
Need from C-Suite: <approve A | provide resource X | coordinate with dept Y>
Deadline: <when needed>
```

**C-Suite response (same session):**
- Write decision to escalations.md as response
- If resolved: flag ESC-ID as RESOLVED
- If needs CEO: escalate to L3

---

## L3 Escalation: C-Suite â†’ CEO

**Trigger:**
- Strategic question requiring CEO direction
- Security CRITICAL finding (security_grc can escalate directly)
- Budget overrun > 20%
- Legal issue requiring CEO sign-off
- Cross-org crisis

**Responder:** CEO
**Effect: BLOCKING** â€” affected work PAUSES until CEO responds

**C-Suite writes to `brain/memory/system_memory/escalations.md`:**
```markdown
## L3 ESCALATION â€” [ESC-ID] â€” [DATE]  âš ï¸ CEO REQUIRED

From: <C-Suite role>
Priority: CRITICAL | HIGH
Work paused: <list of paused tasks/depts>

Issue: <2-3 sentences â€” include urgency and scope>
Evidence: <references to data, KPIs, receipts, security scan>

Options analyzed:
  A. <option> â€” CEO decides: [APPROVE / REJECT / DEFER]
  B. <option> â€” CEO decides: [APPROVE / REJECT / DEFER]

C-Suite recommendation: <A or B and why>

CEO decision required by: <session deadline or ASAP if CRITICAL>
```

**CEO response:**
- Log decision to `corp/memory/global/decisions_log.md`
- Write response to escalations.md
- Communicate decision to affected C-Suite
- All work resumes on CEO's decision

---

## Security Emergency Path (CRITICAL Only)

security_grc can skip L1/L2 and go DIRECT to L3 for CRITICAL threats:

```
strix-agent detects CRITICAL threat
    â”‚
    v
Write L3 directly to escalations.md (no L1/L2 wait)
    â”‚
    v
Pause ALL affected systems (not just one dept)
    â”‚
    v
CEO notified immediately
```

---

## Escalation ID Convention

```
ESC-<LEVEL>-<DATE>-<SEQ>

Examples:
  ESC-L1-2026-03-17-001
  ESC-L2-2026-03-17-001
  ESC-L3-2026-03-17-001  (CEO required)
```

---

## Escalation Resolution Record

When an escalation is resolved, update the entry in escalations.md:
```markdown
### RESOLVED â€” [DATE]
Resolved by: <role/agent>
Decision: <what was decided>
Action taken: <what was done>
Outcome: <result after action>
Logged to: corp/memory/global/decisions_log.md (if L3)
```

---

*"Escalation is not failure. Not escalating when you should is."*


---
id: inter-dept-sop
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:53.513357
---

# INTER_DEPT_SOP.md — Cross-Department Handoff Procedures
# Version: 1.0 | Updated: 2026-03-17
# Authority: Tier 2 (Operations) / COO + Operations

---

## Purpose

When work crosses department boundaries, this SOP prevents:
- Tasks being lost between departments
- Unclear ownership
- Duplicate work
- Blocking dependencies with no resolution path

---

## Cross-Dept Dependency Map (key flows)

```
Engineering  ──► QA & Testing      (GATE_QA before deploy)
Engineering  ──► IT Infrastructure  (deploy → infra support)
Marketing    ──► Content Review     (GATE_CONTENT before publish)
Support      ──► Content Review     (GATE_CONTENT before public reply)
Marketing    ──► Legal             (GATE_LEGAL for campaigns w/ claims)
Any dept     ──► Security & GRC    (GATE_SECURITY for new tools)
Strategy     ──► All Depts         (proposals → dept action)
HR & People  ──► All Depts         (onboarding, performance review)
Finance      ──► C-Suite/CEO       (budget overruns → escalate)
R&D          ──► Strategy          (experiment results → proposals)
```

---

## Handoff Format (Standard)

When passing work from Dept A → Dept B, write to `subagents/mq/<target-dept>_incoming.md`:
```markdown
## INTER-DEPT HANDOFF — [T-ID] — [DATE]

FROM: <source-dept> | <source-agent>
TO: <target-dept> | <target-agent>
Type: FOR_REVIEW | FOR_ACTION | FOR_INFO | FOR_GATE

Deadline: <ASAP | <date>>
Context: <2-3 sentences — what is needed and why>
Artifact: <file path or description>
Acceptance criteria from source dept: <what source dept needs back>

Notes: <anything the receiving dept should know>
```

---

## Key Cross-Dept SOPs

### Engineering → QA & Testing (GATE_QA)
```
1. Engineering worker completes code task
2. receipt: qa_required = true
3. Write to subagents/mq/qa_review_queue.md using gate queue format
4. QA reviews using corp-gate-flow.md GATE_QA procedure
5. QA decision → Engineering: PASS / FAIL / CONDITIONAL
6. Engineering: if PASS → mark task DONE | if FAIL → fix and resubmit
```

### Marketing/Support → Content Review (GATE_CONTENT)
```
1. Marketing/Support worker completes content draft
2. Write to subagents/mq/gate_content_queue.md
3. Content Review runs 4-reviewer checklist (editor, fact, policy, brand)
4. Decision → Marketing/Support
5. On PASS: publishing agent routes to channel
6. On FAIL: author revises, resubmits
```

### IT Infrastructure → Engineering (Deploy Support)
```
IT provides deploy support when Engineering has a GATE_QA PASS:
1. Engineering notifies it_infra a deploy is needed
2. IT allocates environment, checks infra health
3. IT assists devops-agent with deployment
4. IT monitors post-deploy for 30 min (incident window)
5. IT confirms deploy success → Engineering closes task
```

### Any Dept → Security & GRC (New Tools)
```
Security scans automatically on new files in plugins/ or ingestion/
If manual: write to subagents/mq/gate_security_manual_request.md:
  - What: <tool name + purpose>
  - Source: <URL>
  - Requester: <dept + agent>
Security responds with security receipt within same cycle
```

### Strategy → All Depts (Proposal → Action)
```
1. Strategy produces PROPOSAL_<date>_<topic>.md
2. CEO approves/rejects
3. COO routes approved proposals → relevant C-Suite members
4. C-Suite adds actions to dept blackboard.json entries
5. Affected dept heads receive via daily brief
```

### HR & People → All Depts (New Agent Onboarding)
```
1. Dept head requests new agent via subagents/mq/hr_people_request.md
2. recruiter-agent evaluates → identifies matching capability
3. onboard-agent creates brain/corp/memory/agents/<agent>.md
4. HR notifies dept head: agent ready
5. HR updates org_chart.yaml
6. Dept head adds agent to task queue
```

---

## Ownership Rules

| Scenario | Owner | Backup |
|----------|-------|--------|
| Task in Engineering queue, not assigned | Engineering head | CTO |
| Cross-dept task disputed | C-Suite of source dept | COO arbitrates |
| Task in gate queue > SLA | Gate dept head | Relevant C-Suite |
| No dept head active | C-Suite of that dept | COO |
| CEO escalation not answered | CEO (BLOCKING) | No backup — must wait |

---

## Handoff Acknowledgment (Required)

Receiving dept must acknowledge within same session:
```markdown
## HANDOFF ACK — [T-ID] — [DATE]

Received by: <target-agent>
Status: ACCEPTED | DEFERRED (reason) | REJECTED (reason)
Expected completion: <estimate>
```

No acknowledgment within session = scrum-master-agent re-routes to manager.

---

*"A handoff with no acknowledgment is a task that fell on the floor."*


---
id: enrichment_sop
type: corp_document
registered: true
---

# AGENT ENRICHMENT SOP
# Version: 1.0 | Updated: 2026-03-17
# Owner: OD&L (Dept 16) — training-agent
# Triggered by: knowledge-distributor-agent (HIGH-VALUE flag) OR dept head request
# Purpose: Define HOW agents are upgraded when new knowledge arrives

---

## ENRICHMENT TRIGGER CONDITIONS

An agent is enriched when ANY of these occur:

| Trigger | Source | Priority |
|---------|--------|----------|
| Knowledge feed item flagged [TRAIN] | Dept head agent | MEDIUM |
| HIGH-VALUE knowledge item received (score ≥ 8) | knowledge-distributor-agent | HIGH |
| OD&L org-analyst detects skill gap (3+ consecutive failures) | org-analyst-agent | HIGH |
| New skill added to SKILL_REGISTRY.json relevant to agent | Registry | MEDIUM |
| Agent's knowledge_index.md entry is 30+ days old | memory-builder-agent | LOW |
| Retro finding: learning gap for specific agent/dept | learning-curator-agent | HIGH |

---

## ENRICHMENT TYPES

### TYPE 1 — Memory Update (Fastest, most common)
What: Add new fact/context to agent's Always-Load memory
When: New information that permanently changes how the agent should behave
Agent: memory-builder-agent
Process:
  1. Read enrichment request + knowledge source
  2. Extract key facts relevant to the agent's role
  3. Add to brain/corp/memory/<agent-name>.md or brain/corp/memory/departments/<dept>.md
  4. Mark entry with [DATE-ENHANCED] tag
Time: < 1 corp cycle

### TYPE 2 — Skill Upgrade (Medium effort)
What: Add a new skill OR upgrade skill usage instructions in agent's rules.md
When: New capability is needed that no current skill covers, OR a skill uses changed
Agent: training-agent (consults skill-creator-agent if new skill needed)
Process:
  1. Check SKILL_REGISTRY.json — does a matching skill exist?
     YES → add skill reference to agent's rules.md required skills list
     NO → file skill creation request to skill-creator-agent (Registry)
  2. Update agent's rules.md with:
     - Added skill in skills list
     - Updated "at start of each task, load" if boot-time skill
  3. Write training receipt to OD&L daily brief
Time: 1-2 corp cycles

### TYPE 3 — Rule Addition (Highest impact)
What: Add a new domain rule to dept's rules.md
When: New knowledge changes HOW the dept should operate, not just what they know
Agent: training-agent + rule-builder-agent (Registry)
Process:
  1. training-agent drafts rule (using rule template from REG-08)
  2. rule-builder-agent reviews for conflicts with parent rules
  3. C-Suite approves (COO for ops rules, CTO for tech rules, etc.)
  4. rule-builder-agent writes to dept's rules.md
  5. OD&L notifies dept head agent of new rule
Time: 2-3 corp cycles (requires C-Suite approval)

### TYPE 4 — Dept-Level Knowledge Drop (Broadcast)
What: New knowledge relevant to entire dept, added to dept memory (not agent)
When: Strategic, market, or compliance change affects the whole dept's context
Agent: knowledge-distributor-agent → training-agent
Process:
  1. knowledge-distributor identifies dept-level (not agent-level) relevance
  2. Write to brain/corp/memory/departments/<dept>.md (rolling memory section)
  3. Flag to dept head agent via knowledge feed
Time: Immediate (no approval needed for memory drops)

---

## TRAINING-AGENT WORKFLOW

```
ENRICHMENT REQUEST RECEIVED
          │
          ▼
Identify enrichment type (1/2/3/4)
          │
    ┌─────┴──────────────────────────────┐
    │                                    │
TYPE 1: Memory    TYPE 2: Skill    TYPE 3: Rule
    │                  │                 │
memory-builder    check registry    consult rule-builder
add to memory     exists? → patch   draft rule → C-Suite
    │             no? → create req  approval → deploy
    ▼                  │                 │
Write receipt ──────────────────────────→
to OD&L brief
```

---

## ENRICHMENT RECEIPT FORMAT

training-agent writes this after every enrichment:

```
ENRICHMENT RECEIPT — [DATE]
Agent enriched: <agent-name> in <dept>
Type: Memory Update / Skill Upgrade / Rule Addition / Dept Drop
Knowledge source: <CIV-ID or knowledge/ path>
Change made:
  - <specific change in rules.md / memory file>
Validation: <how to verify the enrichment worked>
OD&L brief: [LOGGED]
```

---

## HOW TO REQUEST ENRICHMENT (ANY DEPT HEAD)

Post to brain/corp/knowledge_feeds/od_learning/new_knowledge.md:

```
ENRICHMENT REQUEST
From: <dept>/<dept-head-agent>
Target agent: <agent-name>
Knowledge source: <path or CIV ticket>
Gap: <what the agent doesn't know but should>
Suggested type: [1-Memory | 2-Skill | 3-Rule | 4-Dept Drop]
Priority: HIGH / MEDIUM / LOW
```

OD&L training-agent checks od_learning knowledge feed at boot.

---

## ENRICHMENT TRACKING

training-agent maintains: brain/corp/memory/departments/od_learning.md
Entry per enrichment: agent, type, date, what changed, validation result
Aggregate report to OD&L daily brief each cycle.

Monthly: org-analyst-agent reviews enrichment history for patterns:
- Same gap appearing in 3+ agents → consider new GLOBAL rule
- Same skill missing in 5+ agents → add to ALL_AGENTS_BOOT list


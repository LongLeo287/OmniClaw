---
id: corp-daily-cycle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:10.321659
---

# Department: operations
# corp-daily-cycle.md â€” OmniClaw Corp Operating Cycle
# Version: 2.0 | Updated: 2026-03-17
# Authority: Tier 2 (Operations)
# Mode: ON-DEMAND (trigger-based, not scheduled)
# Trigger: "omniclaw corp start" | CEO session activation

---

## Overview

The Corp Cycle is how OmniClaw Corp runs work â€” on-demand.
No fixed schedule. CEO triggers when needed.
8 phases (Phase 0 = pre-flight). End-to-end: pre-flight â†’ CEO brief â†’ execution â†’ reflection â†’ next decision.

```
CEO ACTIVATES
    â”‚
[0] PRE-FLIGHT      â”€â”€ Validate system state before cycle begins
    â”‚
[1] CEO BRIEF       â”€â”€ CEO reads mission, KPIs, escalations, proposals
    â”‚
[2] C-SUITE DISPATCH â”€â”€ C-Suite translates strategy â†’ dept goals (blackboard)
    â”‚
[3] DEPT DISPATCH   â”€â”€ 21 dept heads assign tasks to workers
    â”‚
[4] EXECUTE         â”€â”€ Workers execute, write receipts
    â”‚
[5] GATE            â”€â”€ GATE_QA / GATE_CONTENT / GATE_SECURITY / GATE_LEGAL
    â”‚
[6] BRIEF BACK      â”€â”€ Dept heads write daily_briefs
    â”‚
[7] REFLECT         â”€â”€ cognitive_reflector + archivist â†’ proposals â†’ CEO
    â”‚
CEO reads proposals â†’ decides â†’ RESET â†’ next cycle
```

---

## Phase 0: PRE-FLIGHT CHECK

**Trigger:** Automatically runs before Phase 1 on every `omniclaw corp start`
**Who:** orchestrator_pro (or Claude Code if orchestrator_pro unavailable)

```
Step 0.1 â€” Critical file check (STOP if any fail):
  [ ] brain/memory/blackboard.json        â€” readable + valid JSON
  [ ] brain/registry/SKILL_REGISTRY.json    â€” readable + no nulls in load_order
  [ ] brain/memory/system_memory/kpi_scoreboard.json
  [ ] brain/brain/memory/system_memory/escalations.md
  [ ] corp/org_chart.yaml
  [ ] corp/rules/APPROVAL_GATES.md

Step 0.2 â€” State check (STOP if any fail):
  [ ] blackboard.json corp_cycle_status != "RUNNING"
      (if RUNNING: previous cycle may be stuck â€” report to CEO before starting)
  [ ] No open L3 escalations in escalations.md
      (if L3 open: do NOT start â€” CEO must resolve first)
  â†’ On PASS: Set blackboard.json corp_cycle_status = "RUNNING"

Step 0.3 â€” Skill registry sync (skill-discovery-auto.md):
  â†’ Set blackboard.json skill_registry_status = "UPDATING"
  â†’ registry-manager-agent scans plugins/, tools/, workforce/agents/, subagents/
  â†’ Creates SKILL.md for any folder missing it
  â†’ Rebuilds FAST_INDEX.json
  â†’ Set blackboard.json skill_registry_status = "READY"
  â†’ Report count to blackboard

Step 0.4 â€” Warning-only checks (log but do NOT stop cycle):
  [ ] corp/memory/departments/<dept>.md exists for each active dept
  [ ] subagents/mq/ directory exists and is readable
  [ ] telemetry/receipts/ directory is writable

On PASS all steps: proceed to Phase 1
On Step 0.1/0.2 FAIL: write to escalations.md + stop cycle + notify CEO
On Step 0.3 FAIL: log warning, proceed with stale SKILL_REGISTRY, mark for manual rebuild
```

---

## Phase 1: CEO BRIEF

**Trigger:** `omniclaw corp start` or CEO activates corp mode
**Ref:** `corp/prompts/CEO_PROMPT.md`

```
CEO reads in order:
1. brain/brain/memory/system_memory/mission.md          â† current strategic direction
2. brain/memory/system_memory/kpi_scoreboard.json â† all 21 dept KPI status
3. brain/brain/memory/system_memory/escalations.md      â† open L2/L3 items
4. brain/brain/memory/system_memory/proposals/          â† pending decisions from last cycle
5. corp/memory/global/decisions_log.md           â† last 5 CEO decisions for context

CEO outputs:
  - Decision on any open proposals â†’ decisions_log.md
  - Mission update if needed â†’ brain/brain/memory/system_memory/mission.md
  - Priority instruction to C-Suite â†’ brain/memory/blackboard.json or direct brief
```

---

## Phase 2: C-SUITE DISPATCH

**Who:** CTO | CMO | COO | CFO | CSO
**Ref:** `corp/prompts/CSUITE_PROMPT.md`

```
Each C-Suite member:
1. Read CEO mission + their domain KPIs from brain/brain/memory/system_memory/mission.md
2. Translate CEO intent â†’ dept-level goals for each of their depts
3. Write dept task entries to brain/memory/blackboard.json:
   { "dept": "engineering", "goal": "...", "kpi_targets": [...] }
4. Optional: write brief to each dept head via subagents/mq/<dept>_brief.md

CFO additional: check finance/budget status â†’ flag if any dept at >80% budget
COO additional: check Security for any open incidents, HR for agent issues
```

**C-Suite dispatch covers all 21 departments:**
```
CTO:  engineering / qa_testing / it_infra / registry_capability / system_health
CMO:  marketing   / support    / content_review
COO:  operations  / hr_people  / security_grc / asset_library / planning_pmo
      monitoring_inspection / content_intake / client_reception
CFO:  finance
CSO:  strategy    / legal      / rd           / od_learning
```

---

## Phase 3: DEPT DISPATCH

**Who:** All 21 Dept Heads (Managers)
**Ref:** `corp/prompts/MANAGER_PROMPT.md` + dept overlay

```
Each dept head:
1. Read daily brief from blackboard / C-Suite brief
2. Load dept memory: corp/memory/departments/<dept>.md
3. Create atomic task cards to subagents/mq/<dept>_tasks.md
4. Assign each task to appropriate worker agent
5. Set: context, acceptance criteria, LLM tier, qa_required flag
```

**Reference:** task card format in `workflows/corp-task-flow.md`

---

## Phase 4: EXECUTE

**Who:** All Worker Agents
**Ref:** `corp/prompts/WORKER_PROMPT.md` + dept overlay

```
Each worker:
1. Read assigned task card
2. Search SKILL_REGISTRY for matching skill â†’ load SKILL.md
3. Execute in atomic steps
4. Write receipt to telemetry/receipts/<dept>/<T-ID>.json
5. Update task card status: DONE | FAILED
6. If qa_required: route to correct gate queue
7. If 2-strike failure: write L1 escalation

Security special: security_grc scans continuously during Phase 4
Operations: scrum-master-agent monitors blackboard for stuck tasks
```

---

## Phase 5: GATE REVIEW

**Who:** Gate agents in qa_testing / content_review / security_grc / legal
**Ref:** `workflows/corp-gate-flow.md`, `rules/APPROVAL_GATES.md`

```
GATE_QA runs: for all engineering outputs
GATE_CONTENT runs: for all marketing/support content
GATE_SECURITY runs: continuously + on any new tool/plugin
GATE_LEGAL runs: for any agreement or external commitment

Each gate: PASS / FAIL / CONDITIONAL
Failed items: return to worker for fix â†’ re-submit
3rd FAIL on same item: L2 escalation to dept head
```

---

## Phase 6: BRIEF BACK

**Who:** All 21 Dept Heads
**Ref:** `MANAGER_PROMPT.md` brief format

```
Each dept head writes to: brain/memory/system_memory/daily_briefs/<dept>.md

Format includes:
  DATE / DEPT / HEAD
  KPI STATUS: [on_track | at_risk | behind | critical]
  COMPLETED: [list of tasks]
  IN PROGRESS: [list + ETA]
  BLOCKED: [with L1/L2 notes]
  WINS: [notable achievements]
  ESCALATIONS: [reference IDs if any]

Agents must write this even if cycle had zero tasks (write "No tasks this cycle")
```

---

## Phase 7: REFLECT + PROPOSE

**Who:** cognitive_reflector + archivist + strategy/product-manager-agent
**Ref:** `ops/workflows/corp-learning-loop.md`
**Mode: MANDATORY** â€” runs after every Phase 6 completion. NOT optional.
**Trigger:** Phase 6 complete (all 21 daily_briefs written) â†’ cognitive_reflector auto-starts

```
archivist:
  - Archive telemetry receipts for this cycle
  - Rotate dept memory (if >30d entries)
  - Purge agent memories (if >7d)

cognitive_reflector:
  - Read ALL 21 dept daily_briefs
  - Identify cross-dept patterns, blockers, wins
  - Write: brain/memory/system_memory/proposals/RETRO_<date>.md

strategy/product-manager-agent:
  - Synthesize retro into CEO proposals
  - Write to: brain/memory/system_memory/proposals/PROPOSAL_<date>_<topic>.md
  - Proposals: KPI_CHANGE | NEW_SKILL | ROLE_CHANGE | STRATEGIC

CEO receives proposals â†’ next Phase 1
```

---

## Cycle Reset

After Phase 7:
```
Update: brain/memory/system_memory/kpi_scoreboard.json (actual values from briefs)
Write: corp/memory/departments/<dept>.md (cycle summary by each manager)
Reset: brain/memory/blackboard.json corp_cycle_status = "IDLE"
Clear: done task cards from subagents/mq/<dept>_tasks.md
Archive: daily_briefs to archive/daily_briefs/<date>/

[HUD UPDATE â€” auto, non-blocking]:
  powershell ops/scripts/update_hud.ps1 -Quiet
  â†’ Updates hud/STATUS.json (services, open items, cycle count)
  â†’ Updates hud/HUD.md services + corp status table
  â†’ Creates hud/snapshots/<date>_<time>.md
  â†’ Sends Telegram summary (if configured)
  On failure: skip â€” do NOT block cycle reset
```

**Note:** At Phase 0 start, set `blackboard.json corp_cycle_status = "RUNNING"`.
This prevents two concurrent cycles. Reset to "IDLE" only after Phase 7 completes.


---

## CLI Trigger Commands

| Command | Phases Run |
|---------|-----------|
| `omniclaw corp start` | Phases 1â€“7 (full cycle) |
| `omniclaw corp brief` | Phase 1 (CEO brief only) |
| `omniclaw corp dispatch <dept>` | Phase 3 for one dept |
| `omniclaw corp gate qa <T-ID>` | Phase 5 GATE_QA only |
| `omniclaw corp gate security <item>` | Phase 5 GATE_SECURITY only |
| `omniclaw corp kpi` | Show kpi_scoreboard.json |
| `omniclaw corp escalate L3 <msg>` | Write L3 straight to escalations.md |
| `omniclaw corp retro` | Phases 6â€“7 only (reflect + propose) |
| `omniclaw corp status` | Show cycle status |

---

## Emergency Override

If CEO needs to intervene mid-cycle:
```
1. Write to escalations.md: "CEO OVERRIDE â€” [reason]"
2. Affected C-Suite pauses dept work immediately
3. CEO decision logged to decisions_log.md
4. Work resumes with new direction
```

---

*"The cycle doesn't run on a clock. It runs when the CEO decides to run it. That's control."*


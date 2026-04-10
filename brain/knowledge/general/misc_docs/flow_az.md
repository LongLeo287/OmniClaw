---
id: flow-az
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:25.321866
---

# Department: operations
---
description: OmniClaw A-Z Operational Flow â€” luá»“ng váº­n hÃ nh Ä‘áº§y Ä‘á»§ tá»« boot Ä‘áº¿n shutdown
---
# OmniClaw â€” A-Z Operational Flow
# Version: 1.0 | 2026-03-24 | Owner: Antigravity (CEO Mandate)
# Authority: Tier 0 â€” Reference for ALL agents

---

## BIG PICTURE

```
BOOT â†’ CEO BRIEF â†’ PLANNING â†’ EXECUTION â†’ QA â†’ REVIEW â†’ RETRO â†’ SHUTDOWN
  â†‘                                                              |
  â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ Next cycle (auto-trigger or CEO start) â”€â”€â”€â”€â”€â”˜
```

---

## A. BOOT â€” Session Start

**Trigger:** CEO opens Antigravity or Claude Code

```
A1. Load boot file
    - Antigravity: GEMINI.md (MANDATORY FIRST â€” RULE-STORAGE-01 to RULE-GIT-NATIVE-01)
    - Claude Code:  CLAUDE.md + .clauderules

A2. Load identity
    brain/memory/SOUL.md (values, personality)

A3. Load governance
    brain/memory/GOVERNANCE.md (authority limits)

A4. Load agent roster
    brain/indices/FAST_AGENT_INDEX.json (who does what)

A5. Check blackboard
    brain/memory/blackboard.json
    â†’ handoff_trigger: ACTIVE? â†’ pick up task
    â†’ corp_cycle_status: IDLE? â†’ wait for CEO

A6. Load skill registry
    brain/registry/SKILL_REGISTRY.json (available tools)

A7. HUD check (optional CEO view)
    hud/HUD.md â†’ full system status at a glance
```

---

## B. INTAKE â€” CEO Gives Input

**Rule:** RULE-CIV-01 (auto-trigger)

```
CASE 1: CEO pastes link/repo/URL/file
    â†’ CIV Pipeline (see Section D)
    â†’ NO question needed â€” auto-process

CASE 2: CEO gives natural language command
    "omniclaw corp start"         â†’ Section C (Corp Cycle)
    "omniclaw ingest <url>"       â†’ Section D (CIV)
    "omniclaw skill health"       â†’ skill-discovery-auto.md
    "omniclaw retro"              â†’ corp-learning-loop.md
    "omniclaw escalate <issue>"   â†’ corp-escalation-flow.md
    "claude code: <task>"    â†’ Section G (Handoff)

CASE 3: CEO asks question / gives instruction
    â†’ Answer directly, no pipeline needed
    â†’ If complex code task â†’ consider handoff to Claude Code

CASE 4: CEO uploads document/PDF
    â†’ CIV Pipeline STEP 2: classifier â†’ DOC type
```

---

## C. CORP CYCLE â€” Full 8-Phase Loop

**Trigger:** "omniclaw corp start" | **Ref:** ops/workflows/corp-daily-cycle.md

```
C0. SYSTEM HEALTH (Phase 0)
    - Port checks: Ollama:11434, ClawTask:7474, LightRAG:9621
    - Blackboard freshness check
    - skill-discovery-auto.md â†’ SKILL_REGISTRY update
    - Set: corp_cycle_status = "ACTIVE"

C1. CEO BRIEF (Phase 1)
    Read: brain/brain/memory/corp_memory/
      mission.md + kpi_scoreboard.json + escalations.md + proposals/
    Read: corp/memory/global/decisions_log.md (last 5)
    Output: CEO priority for this cycle

C2. C-SUITE PLANNING (Phase 2)
    Agents: CFO, COO, CMO, CTO
    Read: CEO mission + their domain KPIs
    Write: dept task cards to brain/memory/blackboard.json
    Write: subagents/mq/<dept>_tasks.md (per dept)

C3. DEPT HEADS EXECUTE (Phase 3)
    21 dept heads read task cards
    Write briefs: brain/brain/memory/corp_memory/daily_briefs/<dept>.md
    SECURITY GATE: new tools â†’ security_grc MUST approve first
    GATE depts: QA, Security, Finance, HR, Legal, Strategy must confirm

C4. WORKER EXECUTION (Phase 4)
    Workers read MANAGER_PROMPT.md + task cards
    Find skill: SKILL_REGISTRY.json â†’ FAST_INDEX.json
    Execute steps â†’ write receipt: telemetry/receipts/<dept>/<id>.json

C5. QA GATE (Phase 5)
    qa_testing dept reviews all outputs
    Ref: ops/workflows/qa-gate.md
    PASS â†’ continue | FAIL â†’ feedback loop (max 2 retries)

C6. CEO REVIEW (Phase 6)
    CEO reads dept briefs briefly
    Decision â†’ append corp/memory/global/decisions_log.md

C7. RETRO & RESET (Phase 7)
    cognitive_reflector: read all 21 briefs â†’ RETRO_<date>.md
    archivist: archive receipts, rotate dept memory
    UPDATE: brain/memory/corp_memory/kpi_scoreboard.json
    RESET: blackboard.json corp_cycle_status = "IDLE"
    UPDATE: hud/HUD.md + hud/snapshots/<date>.md

C8. SKILL HARVEST (Phase 8)
    skill-discovery-auto.md â†’ scan skills/ + plugins/
    Update SKILL_REGISTRY.json + FAST_INDEX.json
```

---

## D. CIV PIPELINE â€” Content Intake & Vetting

**Rule:** RULE-CIV-01 | **Ref:** ops/workflows/content-intake-flow.md v1.2

```
D0. LOCAL CHECK
    LightRAG :9621 â†’ query "similar to <input>"
    FOUND â†’ report CEO "already know this: <match>", ask refresh?
    NO    â†’ continue

D1. TICKET CREATION
    intake-agent â†’ CIV-<YYYYMMDD>-<seq>
    Save to: security/QUARANTINE/incoming/<type>/
    Type: REPO | WEB | DOC | IMAGE | TEXT | PLUGIN

D2. CLASSIFICATION
    classifier-agent â†’ tags type + domain
    Route to appropriate sub-pipeline

D3A. REPO PIPELINE
    repo-fetcher â†’ clone to QUARANTINE/incoming/repos/
    vet_repo.ps1 â†’ 12-stage scan:
      [1] Structure check    [2] License scan     [3] Secret detection
      [4] Dependency audit   [5] Code quality     [6] Security patterns
      [7] API surface        [8] Data handling     [9] Telemetry check
      [10] Conflict check    [11] Compliance scan  [12] Final decision
    strix-agent review â†’ PASS | WARN | FAIL
    FAIL â†’ security/QUARANTINE/rejected/ + CEO notify
    WARN â†’ CEO decision required

D3B. WEB PIPELINE
    web-crawler (Firecrawl) â†’ extract content
    Validate source reputation

D3C. DOC PIPELINE
    doc-parser â†’ extract text + structure
    Validate content type + language

D3.5. ANALYSIS (STEP 3.5)
    content-analyst-agent + open-notebook :5055
    Fallback: Claude Code RESEARCHER (when offline)
    6 CIV Questions:
      1. Purpose: What does this do?
      2. Conflict: Any overlap with existing?
      3. Dept: Which dept should own this?
      4. Risk: Any security/legal risk?
      5. Gap: New domain we don't have?
      6. Proposed: Suggest agent/skill if new domain
    Output: security/QUARANTINE/incoming/<type>/<id>/_CIV_ANALYSIS.md

D3.6. GAP DETECTION (ASYNC)
    gap_detected = true?
    â†’ notification-bridge â†’ CEO Telegram
    â†’ Format: GAP PROPOSAL [A/B/C/D]
      [A] Create new agent (agent-auto-create.md)
      [B] Assign to closest dept
      [C] Create new department
      [D] Skip â€” file for reference
    â†’ Save: corp/gaps/GAP-<date>-<domain>.md
    â†’ Register: corp/memory/global/gaps_register.md

D4. VALIDATION
    content-validator â†’ quality score (1-10)
    VALUE_TYPE assignment (9 types â€” see corp/sops/VALUE_ASSESSMENT_ROUTING.md)
    Score < 4 â†’ REJECT + reason log
    Score â‰¥ 4 â†’ proceed to D5

D5. INGESTION & DISTRIBUTION
    ingest-router â†’ determine destination
    REPO/PLUGIN â†’ skills/ or plugins/ directory
    â†’ skill-discovery-auto.md â†’ update SKILL_REGISTRY
    KNOWLEDGE â†’ brain/knowledge/notes/KI-<topic>.md
    â†’ LightRAG index (:9621/insert)
    ALL â†’ knowledge-distribution-flow.md â†’ 21 dept feeds
    â†’ Update kho/brain/INDEX.md
    â†’ Move to: security/QUARANTINE/vetted/<type>/
```

---

## E. SKILL LIFECYCLE

```
E1. DISCOVERY
    Trigger: new repo ingested / CEO command / Phase 8
    Workflow: skill-discovery-auto.md
    Scanner reads: skills/<name>/SKILL.md (required)

E2. REGISTRATION
    skill-creator-agent creates SKILL.md if missing
    Writes to SKILL_REGISTRY.json + FAST_INDEX.json

E3. ACTIVATION (RULE-ACTIVATION-01)
    Dashboard First: announce in daily brief
    CEO reviews: APPROVE | DEFER | REJECT
    APPROVE â†’ enable in SKILL_REGISTRY.json status: "active"

E4. USAGE
    Agent checks FAST_INDEX.json â†’ loads SKILL.md
    Executes skill protocol

E5. MAINTENANCE
    Monthly: compare installed version vs. latest (VERSION_LOCK.env)
    Security skills: weekly check via trivy / strix-agent
    Deprecate: move to kho/plugins/tier3/ (blacklist)
```

---

## F. GAP â†’ NEW AGENT â†’ NEW DEPT

```
F1. Gap detected in CIV STEP 3.6
F2. CEO replies [A] "Create new agent"
F3. Antigravity triggers: ops/workflows/agent-auto-create.md
F4. agent-auto-create flow:
    - Define: name, role, dept, tools, memory_path
    - Create: ecosystem/workforce/agents/<agent>.md
    - Create: skills/<skill>/SKILL.md if needed
    - Add to: corp/org_chart.yaml
    - Register: brain/indices/FAST_AGENT_INDEX.json
    - Assign to dept head: MANAGER_PROMPT.md update
    - Notify: kho/agents/registry.json update
F5. If CEO replies [C] "Create new dept":
    - Create: corp/departments/<new_dept>/
    - Create: MANAGER_PROMPT.md + WORKER_PROMPT.md + rules.md
    - Create: corp/memory/departments/<new_dept>.md
    - Add to: corp/org_chart.yaml
    - Update: MASTER_SYSTEM_MAP.md + hud/HUD.md dept count
```

---

## G. HANDOFF â€” Antigravity â†” Claude Code

**Ref:** ops/workflows/claude-code-handoff.md

```
G1. Antigravity detects task needs Claude Code:
    - Multi-file code (>200 lines)
    - Bash execution required
    - Sub-agents needed
    - Complex refactoring

G2. Antigravity prepares:
    - blackboard.json: handoff_trigger="ACTIVE", target_agent="Claude Code"
    - subagents/mq/claude_code_tasks.md: task detail

G3. CEO opens Claude Code CLI terminal
    Claude Code reads: CLAUDE.md â†’ blackboard.json â†’ tasks.md

G4. Claude Code executes:
    - Git snapshot first: git commit -m "snapshot: before CC-<id>"
    - Switches roles: DEVELOPER | QA | RESEARCHER per step
    - Writes receipts: telemetry/receipts/

G5. Claude Code completes:
    - blackboard.json: handoff_trigger="COMPLETE", target_agent="Antigravity"

G6. Antigravity resumes:
    - Reports to CEO in Vietnamese
```

---

## H. NOTIFICATION & ESCALATION

**Ref:** ops/workflows/notification-bridge.md

```
H1. Any agent detects issue/event
H2. Sends to notification-bridge:
    { type, priority, source_agent, title, body }

H3. Bridge routes:
    CRITICAL â†’ Telegram (immediate) + escalations.md + blackboard
    HIGH     â†’ Telegram + blackboard
    NORMAL   â†’ blackboard only
    LOW      â†’ blackboard (next review cycle)

H4. Escalation levels:
    L1: Agent resolves autonomously (< 2 failures)
    L2: Dept head notified (blackboard.json open_items[])
    L3: C-Suite notified (escalations.md)
    L4: CEO notified directly (Telegram)

H5. Circuit Breaker:
    Agent fails twice â†’ status="BLOCKED" â†’ L3 escalation
```

---

## I. SHUTDOWN â€” Session End

**Ref:** ops/workflows/post-session.md

```
I1. Save work: git add . && git commit -m "session: <summary>"
I2. Update blackboard: log what was done in last_actions_this_cycle
I3. Write receipt: telemetry/receipts/session_<timestamp>.json
I4. Update hud/HUD.md if significant state change
I5. Snapshot HUD: copy to hud/snapshots/<date>_<time>.md
I6. Set: blackboard.json corp_cycle_status = "IDLE" (if cycle complete)
I7. Telegram: "Session complete" notification (if configured)
```

---

## Z. KHO REFERENCE â€” Storage Used Throughout Flow

| Flow Step | Reads From | Writes To |
|-----------|-----------|----------|
| A (Boot) | GEMINI.md, CLAUDE.md, blackboard.json | - |
| B (Intake) | RULE-CIV-01 | QUARANTINE/incoming/ |
| C (Corp Cycle) | corp/memory/, kpi_scoreboard.json | daily_briefs/, receipts/ |
| D (CIV) | QUARANTINE/incoming/ | QUARANTINE/vetted/, brain/knowledge/, skills/ |
| E (Skills) | SKILL_REGISTRY.json | kho/plugins/, FAST_INDEX.json |
| F (Agents) | ecosystem/workforce/agents/ | corp/departments/, kho/agents/ |
| G (Handoff) | blackboard.json | telemetry/receipts/ |
| H (Alerts) | notification-bridge.md | escalations.md, Telegram |
| I (Shutdown) | hud/HUD.md | hud/snapshots/, git history |

---

*v1.0 | 2026-03-24 | Full A-Z flow â€” update when any major flow changes*


---
id: corp-learning-loop
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:10.366494
---

# Department: operations
# corp-learning-loop.md â€” Post-Cycle Reflection & Memory Update
# Version: 1.0 | Updated: 2026-03-17
# Authority: Tier 2 (Operations) / Strategy + Operations
# Agents: cognitive_reflector + archivist

---

## Overview

The learning loop runs after every corp cycle.
Its purpose: extract wisdom from this cycle â†’ feed it back into memory â†’ improve next cycle.

```
ALL DEPT DAILY BRIEFS
    â”‚
    v
[1] ARCHIVIST    â”€â”€ Collect + archive telemetry
    â”‚
    v
[2] REFLECTOR    â”€â”€ Pattern analysis across all depts
    â”‚
    v
[3] MEMORY UPDATE â”€â”€ Write lessons to dept + global memory
    â”‚
    v
[4] PROPOSALS    â”€â”€ Strategy dept writes CEO proposals
    â”‚
    v
CEO reads â†’ decides â†’ cycle improves
```

**Trigger (2 modes):**
- **MANDATORY** â€” Automatically runs as Phase 7 of every `corp-daily-cycle.md` (after Phase 6 BRIEF BACK)
- **ON-DEMAND** â€” CEO triggers manually with `omniclaw corp retro` to run reflection outside main cycle

Both modes run identical phases. In mandatory mode, cognitive_reflector starts immediately after all 21 dept daily_briefs are written.

---

## Phase 1: Archive (archivist)

```
1. Collect: all brain/memory/corp_memory/daily_briefs/*.md for this cycle
2. Archive telemetry:
   - Move telemetry/receipts/<dept>/* â†’ archive/receipts/<YYYY-MM>/<dept>/
   - (if receipt age > 30 days)
3. Rotate dept memory files:
   - For each corp/memory/departments/<dept>.md:
     â†’ Entries older than 30 days â†’ summarize, move to knowledge/
4. Purge agent session memory:
   - corp/memory/agents/*.md entries older than 7 days â†’ delete
5. Write archivist receipt: telemetry/archivist_log.md
```

---

## Phase 2: Auto-Dream Consolidation (cognitive_reflector)

cognitive_reflector triggers a 4-step "REM Sleep" process to extract wisdom without bloating memory.

### Step 2a: Orientation (Äá»‹nh hÆ°á»›ng)
- Reads `brain/memory/corp_memory/mission.md` (CEO Intent).
- Reads `brain/memory/blackboard.json` (Cycle context).
- Sets the "Focus Lens" for what signals matter.

### Step 2b: Gather Signal (Gom TÃ­n Hiá»‡u ThÃ´)
- Scans `telemetry/receipts/<dept>/` for tasks completed this cycle.
- Scans `corp/daily_briefs/BRIEF_<date>.md` for anomalies.

### Step 2c: Consolidation (Há»£p Nháº¥t)
- Synthesizes findings into `brain/memory/corp_memory/daily_briefs/SYNTHESIS_<date>.md`.
- Formats cross-dept blockers, global wins, and skill gaps.

### Step 2d: Prune & Index (Tá»‰a rÃ¡c vÃ  ÄÃ¡nh Chá»‰ Má»¥c)
- Scans `corp/memory/departments/<dept>.md`.
- If a memory file exceeds 200 lines, it forcibly truncates and summarizes the oldest entries.
- Updates the `corp/memory/GLOBAL_INDEX.md` (Hard cap < 100 lines) to map where concepts are stored.

---

## Output format (`SYNTHESIS_<date>.md`):
```markdown
# Auto-Dream Synthesis â€” [DATE]

## 1. Orientation Context
- Focused on: [CEO Mission snippet]

## 2. Signal Gathered
| Dept | Receipts Scanned | Brief Status |
|------|-----------------|--------------|
| ...  | ...             | ...          |

## 3. Consolidation: Patterns & Blockers
- [Pattern]: affected [N] depts.
- Win: [What worked well]

## 4. Prune Status
- Pruned [N] old memory blocks.
- `GLOBAL_INDEX.md` updated.
```

---

## Phase 3: External Knowledge Ingestion (Optional)

### 3a. Dept Memory (Manager writes)

Each dept manager writes to `corp/memory/departments/<dept>.md`:
```markdown
## Cycle [N] â€” [DATE]

Goals achieved: [list]
Goals missed: [list] â€” Root cause: [1 line]
Patterns observed: [actionable facts]
Cross-dept dependencies this cycle: [what we needed from others]
Lessons for next cycle: [specific changes to how we work]
Next cycle focus: [top 3]
```

### 3b. Global Memory (CEO or C-Suite writes)

For significant lessons, write to `corp/memory/global/decisions_log.md`:
```markdown
## [DATE] â€” [TITLE]
Type: LESSON_LEARNED
Context: [what happened]
Lesson: [distilled fact â€” 1-2 sentences]
Applied to: [which depts or agents]
```

### 3c. Agent Memory (auto-expiry managed by archivist)

Each agent who was active this cycle updates `corp/memory/agents/<agent>.md`:
```markdown
## [DATE] â€” Task: <task>
Outcome: SUCCESS | PARTIAL | FAILED
Key lesson: [1 sentence]
Next time: [what to do differently]
```

---

## Phase 4: Proposals to CEO

Strategy dept (product-manager-agent) synthesizes retro findings into:
1. **KPI Change proposals** â€” if targets are consistently wrong
2. **New skill proposals** â€” if skill gap found
3. **Agent/Role change proposals** â€” if a function is missing or misassigned
4. **Strategic proposals** â€” if pattern reveals strategic risk or opportunity

Each proposal follows format from `corp/departments/strategy/MANAGER_PROMPT.md`
Stored in: `brain/memory/corp_memory/proposals/PROPOSAL_<date>_<topic>.md`

---

## Learning Loop Schedule

| When | Trigger | Depth |
|------|---------|-------|
| After each active corp cycle (mandatory) | corp-daily-cycle Phase 7 | Light (skip archive if same-session) |
| On-demand standalone | `omniclaw corp retro` | Light (skip archive) |
| Weekly | `omniclaw corp retro --full` | Full (archive + rotate memory) |
| Monthly | Archivist scheduled | Deep (purge + global summary) |

---

## Feedback Loop: How Proposals Reach Next Cycle Phase 1

```
Phase 7 (THIS cycle) completes
    â”‚
cognitive_reflector writes â†’ brain/memory/corp_memory/proposals/RETRO_<date>.md
product-manager-agent writes â†’ brain/memory/corp_memory/proposals/PROPOSAL_<date>_*.md
    â”‚
    â–¼
Cycle resets: blackboard.json corp_cycle_status = "IDLE"
    â”‚
    â–¼
NEXT CYCLE Phase 0 (Pre-flight) â†’ Phase 1 (CEO BRIEF)
    â”‚
CEO reads in Phase 1:
  4. brain/memory/corp_memory/proposals/    â† âœ… proposals from this retro are HERE
  3. brain/memory/corp_memory/escalations.md
    â”‚
CEO decides â†’ feeds into Phase 2 C-Suite dispatch â†’ cycle improves
```

This closes the loop: every cycle's lessons feed directly into the next cycle's CEO brief.

---

## KPI Table â€” fix in corp-learning-loop

Note: Phase 2 KPI Summary table says `[all 21 depts]` â€” should be **all 21 depts**.
When writing RETRO, include all 21 departments in the KPI table.

---

*"A system that doesn't learn from its mistakes gets dumber every cycle. The loop is how we get smarter."*


---
id: repo-evaluation
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:08.700801
---

# Department: operations
---
description: Deep evaluation of a repo before deciding to integrate into OmniClaw
---
# Repo Evaluation Workflow (Pre-Integration Gate)
# Version: 1.0 | 2026-03-23 | Owner: Antigravity + Dept 20 CIV

> **This workflow runs BEFORE `plugin-integration.md`.**
> Purpose: Decide IF a repo should enter OmniClaw â€” not HOW to integrate it.
> Output: One of three verdicts: APPROVE / DEFER / REJECT

---

## STEP 1 â€” Identity & Purpose Analysis

Before touching any code, answer these 5 questions by reading only the README:

```
Q1. What does this repo DO in one sentence?
Q2. What problem does it solve that OmniClaw doesn't already solve?
Q3. Who built it? (Individual hobbyist vs. company-backed project?)
Q4. When was it last updated? (>12 months stale = caution flag)
Q5. How many stars/forks? (Signal of community trust)
```

**Decision gate:** If you cannot answer Q1 or Q2 clearly â†’ `REJECT` (no clarity = no fit).

---

## STEP 2 â€” Conflict & Redundancy Check

Cross-reference against what OmniClaw already has:

```
Check against:
  - plugins/plugin-catalog.md    (existing plugins by category)
  - brain/registry/SKILL_REGISTRY.json  (active skills)
  - brain/memory/blackboard.json      (planned integrations)

Ask:
  [A] Does OmniClaw already have a TIER 1 tool that covers this function?
      YES â†’ REJECT (Tier 1 never gets replaced by a newcomer)

  [B] Does OmniClaw have a TIER 2 tool with similar function?
      YES â†’ Compare quality. Keep the better one. Mark other as âŒ in catalog.

  [C] Is this truly a gap? (Function not covered anywhere)
      YES â†’ Eligible for APPROVE. Continue to Step 3.
```

---

## STEP 3 â€” Tier Assignment Decision

Determine which tier the repo belongs to IF approved:

```
TIER 1 criteria (Core Infra â€” always on):
  âœ“ System cannot function without it
  âœ“ Used by >3 departments or agents
  âœ“ Has a stable API / well-maintained upstream
  âœ“ No equivalent already in Tier 1
  â†’ Current Tier 1: Mem0, Firecrawl, LightRAG, CrewAI, GitNexus

TIER 2 criteria (Specialized â€” Lazy-Load):
  âœ“ Serves a specific use case (not cross-cutting)
  âœ“ Used occasionally, not every session
  âœ“ Can be sandboxed safely (see: .agents/workflows/plugin-lazy-load.md)
  â†’ Most repos fall here

TIER 3 criteria (Blacklist):
  âœ— Conflicts with existing Tier 1 tool
  âœ— Unmaintained (last commit >2 years)
  âœ— License incompatible (GPL/AGPL without CEO approval)
  âœ— Duplicate of another catalog entry
  â†’ Mark âŒ in plugin-catalog.md. Do NOT clone.
```

---

## STEP 4 â€” Integration Cost Estimate

Before approving, estimate the real cost of bringing this repo in:

```
[ ] Does it require installing new system-level dependencies?
[ ] Does it need a port/service (adds to dashboard.ps1 complexity)?
[ ] Does it need an API key (adds to MASTER.env)?
[ ] Does it need a custom adapter to fit the OmniClaw patterns?
[ ] How long will integration take? (>1 day = flag for CEO review)
```

**Rule:** If total cost is HIGH and value is MEDIUM â†’ `DEFER` for a later phase.

---

## STEP 5 â€” Verdict & Catalog Update

**ONE of three verdicts:**

| Verdict | Action |
|---------|--------|
| `APPROVE` | Assign Tier. Update catalog to `âš¡`. Proceed to `plugin-integration.md`. |
| `DEFER`   | Update catalog to `ðŸ”–`. Add note: *"Defer to Phase X â€” reason"*. |
| `REJECT`  | Update catalog to `âŒ`. Add note: *"Rejected â€” reason (e.g., conflict with Firecrawl)"*. |

**Update `plugins/plugin-catalog.md` immediately** â€” never leave a repo in `â¸ï¸` status after evaluation.

---

## OUTPUT FORMAT CHUáº¨N â€” Repo Intake Report

> Ãp dá»¥ng khi viáº¿t Repo Intake Report gá»­i CEO. ToÃ n bá»™ ná»™i dung báº±ng **tiáº¿ng Viá»‡t**.

### Cáº¥u trÃºc tá»•ng thá»ƒ 1 report:

```
# ðŸ“‹ Repo Intake Report â€” YYYY-MM-DD
**CIV Tickets:** BATCH-XX | **Tá»•ng URLs nháº­n:** N | **Unique repos:** N | **KhÃ´ng Ä‘á»c Ä‘Æ°á»£c:** N

## PHÃ‚N LOáº I THEO CATEGORY
[OVERVIEW TABLE â€” QuÃ©t nhanh toÃ n bá»™ repos]

## CHI TIáº¾T â€” APPROVE repos
[DETAIL CARDS â€” Tá»«ng repo APPROVE cÃ³ Ä‘áº§y Ä‘á»§ thÃ´ng tin]

## CHI TIáº¾T â€” REFERENCE repos
[DETAIL CARDS â€” Tá»«ng repo REFERENCE (ngáº¯n hÆ¡n APPROVE)]

## DEFER & REJECT
[TABLE gá»n â€” chá»‰ cáº§n repo + lÃ½ do]

## DEEP ANALYSIS
[PhÃ¢n tÃ­ch sÃ¢u 2-3 repos APPROVE Æ°u tiÃªn cao nháº¥t]

## Tá»”NG Káº¾T
[Báº£ng Count/% + Priority Queue]
```

---

### Format DETAIL CARD â€” má»—i repo APPROVE:

```markdown
### N. TÃªn-repo-hiá»ƒn-thá»‹ Â· `org/repo-name`
ðŸ”— https://github.com/org/repo-name

- **Description:** [1 cÃ¢u Description: repo lÃ m gÃ¬]
- **License:** MIT / Apache / BSL / GPL / Custom
- **Highlights:** [3-5 tÃ­nh nÄƒng/thá»‘ng kÃª ná»•i báº­t: sá»‘ releases, contributors, tÃ­nh nÄƒng chÃ­nh]
- **OmniClaw Relevance:** â­â­â­â­â­ â€” [giáº£i thÃ­ch táº¡i sao phÃ¹ há»£p vá»›i OmniClaw]
- **Action:** â†’ [lá»‡nh cá»¥ thá»ƒ hoáº·c bÆ°á»›c tiáº¿p theo]
- **Conflict check:** SAFE / âš ï¸ [tÃªn tool conflict] â€” [lÃ½ do]
- **Dept:** [Dept X â€” tÃªn department phá»¥ trÃ¡ch]
- **Tier:** [1 / 2]
```

### Format DETAIL CARD â€” má»—i repo REFERENCE (ngáº¯n hÆ¡n):

```markdown
### N. TÃªn-repo-hiá»ƒn-thá»‹ Â· `org/repo-name`
ðŸ”— https://github.com/org/repo-name

- **Description:** [1 cÃ¢u Description: repo lÃ m gÃ¬]
- **Há»c gÃ¬:** [Ä‘iá»ƒm cáº§n cherry-pick hoáº·c há»c]
- **Action:** â†’ [lÆ°u KI vÃ o brain/knowledge/notes/ hoáº·c cherry-pick pattern]
```

### Overview Table format (Ä‘áº§u report):

```markdown
| # | Repo | Verdict | PhÃ¢n tÃ­ch |
|---|------|---------|-----------|
| 1 | `org/repo` *(tag)* | âœ… APPROVE â†’ Dept X | 1 cÃ¢u ngáº¯n |
```

---

## INTEGRATION TRIGGER

After APPROVE verdict, hand off to the integration workflow:
```
Trigger: omniclaw integrate <plugin_id>
File: ops/workflows/plugin-integration.md
```

---

## EVALUATION PRINCIPLES

```
1. "No clone by default" â€” reading README â‰  permission to clone.
   Only clone when verdict = APPROVE.

2. "One function, one tool" â€” if OmniClaw already has a tool for a job,
   do not add a second tool for the same job without REJECTING the old one first.

3. "Tier 1 is frozen" â€” do not propose replacing Tier 1 tools.
   You can only ADD to Tier 1 with explicit CEO approval.

4. "Catalog first" â€” every repo must be in plugin-catalog.md
   with a verdict before any code is read or dependencies are installed.
```

---

*Workflow Owner: Antigravity | Pre-Integration Gate | Created: 2026-03-23*
*"Evaluate before you integrate. Reject before you clone."*


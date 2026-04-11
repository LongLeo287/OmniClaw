---
id: corp-gate-flow
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:10.352500
---

# Department: operations
# corp-gate-flow.md â€” Gate Operation Workflow for All 4 Corp Gates
# Version: 1.0 | Updated: 2026-03-17
# Authority: Tier 2 Gate / Corp Mode
# Gates: GATE_QA | GATE_CONTENT | GATE_SECURITY | GATE_LEGAL

---

## Gate Flow (Universal)

```
ITEM READY FOR GATE
    â”‚
    v
ROUTE TO CORRECT GATE QUEUE
    â”‚
    v
GATE AGENT RUNS CHECKLIST (from APPROVAL_GATES.md)
    â”‚
    â”œâ”€â”€â–º PASS        â†’ Notify manager. Item proceeds.
    â”œâ”€â”€â–º CONDITIONAL â†’ Notify manager. Item proceeds IF conditions met.
    â””â”€â”€â–º FAIL        â†’ Return to worker with exact fixes.
              â”‚
              v
           WORKER FIXES
              â”‚
              v
           RE-SUBMIT (same item ID)
              â”‚
           3rd FAIL â†’ L2 escalation to dept head
```

---

## GATE_QA â€” Operation

**Queue:** `subagents/mq/qa_review_queue.md`
**Operated by:** qa_testing dept

**Item submission format (engineering worker writes):**
```markdown
## QA REVIEW REQUEST â€” [T-ID] â€” [DATE]

From: <worker-agent>
Dept: engineering
Task: <T-ID and title>
Artifacts:
  - Code: <file paths>
  - Tests: <test file paths>
  - Coverage report: <path or summary>

Self-checklist (pre-flight):
  [ ] Tests pass locally
  [ ] No obvious linting errors
  [ ] No hardcoded secrets

Notes: <anything QA should know>
```

**QA agent runs:** see `corp/rules/APPROVAL_GATES.md` â†’ GATE_QA checklist
**QA receipt stored:** `telemetry/qa_receipts/gate_qa/<T-ID>.json`

**On PASS:** engineering worker updates task card status â†’ DONE
**On FAIL:**
- QA writes specific failed checklist items to `subagents/mq/<dept>_qa_reject.md`
- Worker reads: `subagents/mq/<dept>_qa_reject.md` â†’ must fix exactly those items
- Re-submit with same T-ID suffix: `<T-ID>-r2`, `<T-ID>-r3`
- 3rd FAIL: write L2 escalation to `brain/memory/system_memory/escalations.md` (to: CTO)

---

## GATE_CONTENT â€” Operation

**Queue:** `subagents/mq/gate_content_queue.md`
**Operated by:** content_review dept

**Item submission format (marketing/support worker writes):**
```markdown
## CONTENT REVIEW REQUEST â€” [T-ID] â€” [DATE]

From: <worker-agent>
Dept: <marketing | support>
Content type: blog | social | email | support_reply | campaign
Target channel: <platform>
Publish deadline: <date>

Content: <attach or reference file path>

Self-check done:
  [ ] Spell-checked
  [ ] CTA included
  [ ] Brand terms spelled correctly

Notes: <anything reviewer should know>
```

**Reviewer team:**
1. editor-agent â†’ editorial + format
2. fact-checker â†’ factual accuracy
3. content-moderator â†’ policy compliance
4. brand-guardian â†’ brand consistency

All 4 must review before final decision.

**On PASS:** content is published via publishing agent or channel
**On FAIL:** specific editor/fact/policy/brand issues listed â†’ author revises

---

## GATE_SECURITY â€” Operation

**Autonomous** â€” security_grc monitors continuously; does not wait for queue
**Also accepts manual trigger:** `omniclaw corp gate security <repo-or-plugin>`

**Auto-trigger conditions:**
- New file appears in plugins/ directory
- New repo cloned to ingestion/
- Manual request from any dept head

**Scan process:**
```
1. strix-agent runs SkillSentry 9-layer scan
2. security-scanner checks license
3. compliance-agent checks permissions
4. Produce security receipt with score
```

**Score-based decision:**
```
>= 60  â†’ PASS â†’ item may proceed
40-59  â†’ CONDITIONAL â†’ quarantine watch period (7 days), monitoring enabled
< 40   â†’ BLOCK â†’ CEO override required to unblock
```

**Receipt stored:** `telemetry/qa_receipts/gate_security/<item-id>.json`
**On CRITICAL finding:**
- strix-agent writes L3 DIRECTLY to `brain/memory/system_memory/escalations.md` (skip L1/L2)
- Format: `## L3 ESCALATION â€” ESC-L3-<DATE>-<SEQ>  âš ï¸ CEO REQUIRED`
- All affected systems PAUSE immediately
- CEO notified via Telegram (if configured)
- Ref: `corp-escalation-flow.md` â†’ Security Emergency Path

---

## GATE_LEGAL â€” Operation

**Queue:** `subagents/mq/legal_review_queue.md`
**Operated by:** legal dept

**Item submission format:**
```markdown
## LEGAL REVIEW REQUEST â€” [T-ID] â€” [DATE]

From: <requesting agent or dept>
Document type: contract | agreement | license | terms | vendor
Urgency: IMMEDIATE | STANDARD

Document: <attach or reference file path>
Counterparty: <external party name>
Estimated value/impact: <if financial>
Data involved: YES (PII) | YES (business) | NO

Notes: <key concerns>
```

**Review team:**
1. contract-agent â†’ clause structure + risk
2. ip-agent â†’ IP ownership, license compatibility
3. gdpr-agent â†’ data protection compliance

**GATE_LEGAL decision:**
- CLEAR TO SIGN â†’ still requires **CEO final approval before signing**
- REVISIONS NEEDED â†’ specific clauses flagged â†’ requester revises
- DO NOT SIGN â†’ legal risk too high â†’ escalate L3 with analysis

**Important:** Even CLEAR TO SIGN items CANNOT be signed without CEO.

---

## Gate Status Dashboard

Track in `brain/memory/system_memory/daily_briefs/<gate>.md`:
```
GATE STATUS â€” [DATE]
â”‚
â”œâ”€â”€ GATE_QA:       [N] pending | [N] passed | [N] failed today
â”œâ”€â”€ GATE_CONTENT:  [N] pending | [N] passed | [N] failed today
â”œâ”€â”€ GATE_SECURITY: [N] scanned | [N] passed | [N] blocked | [N] CRITICAL
â””â”€â”€ GATE_LEGAL:    [N] pending | [N] cleared | [N] blocked
```

---

## Gate SLA

| Gate | Review SLA | Backlog Trigger |
|------|-----------|----------------|
| GATE_QA | Same session | >3 items pending â†’ notify CTO |
| GATE_CONTENT | Same session | >5 items pending â†’ notify CMO |
| GATE_SECURITY | Real-time (autonomous) | CRITICAL â†’ immediate L3 |
| GATE_LEGAL | 1-2 cycles | >2 contracts pending â†’ notify CSO |

---

*"When in doubt about whether something needs a gate, it needs a gate."*


---
id: delivery-pipeline
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:18.148894
---

# DELIVERY PIPELINE â€” SOP v1.0
# OmniClaw | Tier 1 â€” Operations
# Effective: 2026-03-18

> **Purpose:** The complete workflow from when the client ACCEPTs a proposal â†’ Deliver â†’ Invoice.
> Continuing from `CLIENT_INTAKE_GATEWAY.md` and `Proposal Engine`.

---

## Pipeline Overview

```
PROPOSAL ACCEPTED
      â”‚
      â–¼
[Phase 1: KICKOFF]        â”€ 1 day
  - Confirm scope
  - Assign team
  - Setup workspace
      â”‚
      â–¼
[Phase 2: EXECUTION]      â”€ Follow committed timeline
  - Dept leads receive brief
  - Agents execute
  - Progress tracking
      â”‚
      â–¼
[Phase 3: QA & REVIEW]    â”€ 1-3 days
  - QA dept checks
  - Client review round 1
  - Revisions (max 2 rounds)
      â”‚
      â–¼
[Phase 4: DELIVERY]       â”€ 1 day
  - Package deliverables
  - Handoff to client
  - Collect feedback
      â”‚
      â–¼
[Phase 5: INVOICE & CLOSE]â”€ 1 day
  - Generate invoice
  - Payment tracking
  - Archive project
      â”‚
      â–¼
[Phase 6: LEARNING LOOP]  â”€ Auto
  - corp_learning_loop retro
  - Update KPI scoreboard
  - Knowledge extraction
```

---

## Phase 1: KICKOFF

**Trigger:** Client replies "ACCEPT" | "Proceed" | "Agreed" on the proposal

**Actions:**
1. `project_intake_agent` â†’ update status to: `ACCEPTED`
2. Create **Project Workspace**:
   ```
   brain/memory/projects/<PROJECT-ID>/
   â”œâ”€â”€ brief.json          â† copy of intake record
   â”œâ”€â”€ proposal.md         â† accepted proposal
   â”œâ”€â”€ workspace/          â† working files
   â”œâ”€â”€ deliverables/       â† final output
   â””â”€â”€ comms_log.md        â† all client communications
   ```
3. Assign **Project Lead** from operations
4. Create department briefs â†’ send to `subagents/mq/<dept>_brief.md`
5. Notify client: "âœ… Project [ID] has been kicked off! Lead: [agent name]"

---

## Phase 2: EXECUTION

**Responsibility:** Dept leads + assigned agents

**Progress Tracking:**
- Each agent updates `brain/memory/projects/<ID>/progress.json` after completing a task
- Format:
  ```json
  {
    "task": "Build login page",
    "agent": "frontend-agent",
    "status": "DONE",
    "output": "workspace/login.html",
    "timestamp": "..."
  }
  ```
- `ops-router` (tinyclaw) checks progress every 4h â†’ reports to ops

**Communication Rules:**
- Client updates: every 24-48h (depending on timeline)  
- Log all comms in `comms_log.md`
- Blockers â†’ notify ops immediately

---

## Phase 3: QA & REVIEW

**QA Checklist** (performed by qa-agent):
- [ ] Deliverables match proposal scope
- [ ] No obvious bugs/errors
- [ ] Correct file formats
- [ ] Complete documentation

**Client Review:**
- Send deliverables preview via original channel
- Wait 48h for feedback
- Round 1 revision if necessary
- Round 2 revision (final) if necessary
- > 2 rounds â†’ Out of scope, charge extra â†’ CEO approval required

---

## Phase 4: DELIVERY

**Delivery Package:**
```
deliverables/
â”œâ”€â”€ [project-files...]
â”œâ”€â”€ README.md           â† usage guide
â”œâ”€â”€ DELIVERY_RECEIPT.md â† confirmation of handoff
â””â”€â”€ support_contact.md  â† post-delivery support contacts
```

**Handoff:**
1. Zip and share via channel (or Google Drive/cloud link)
2. Client signs `DELIVERY_RECEIPT.md` (reply "RECEIVED" or "âœ…")
3. Update status to: `DELIVERED`

---

## Phase 5: INVOICE & CLOSE

**Invoice Generation:**
```
brain/memory/system_memory/invoices/INVOICE-<YYYYMMDD>-<PROJECT-ID>.md

Content:
  - Project summary
  - Deliverables listed
  - Hours spent (if T&M)
  - Amount due
  - Payment methods: [bank transfer / crypto / PayPal]
  - Due: 7 days
```

**Payment Status Tracking:**
- `brain/memory/system_memory/invoices/_payment_tracker.json`
- Reminder: +7 days unpaid â†’ follow up
- Reminder: +14 days â†’ escalate

**Project Close:**
- Archive to: `brain/memory/projects/archive/<PROJECT-ID>/`
- Rating: collect 1-5 star feedback from client
- Update `corp/kpi_scoreboard.json`: projects_delivered + 1

---

## Phase 6: LEARNING LOOP

**Auto-trigger** after invoice PAID:

1. **corp_learning_loop** runs project retro:
   - What went well? â†’ document in `knowledge/project_learnings/`
   - What needs improvement?
   - Any skill gaps detected? â†’ propose training
   
2. **KPI Update:**
   - Revenue realized
   - Client satisfaction score
   - Delivery time vs estimate

3. **Knowledge Extraction:**
   - If the project generated reusable code/skills â†’ propose adding to SKILL_REGISTRY

---

## Project Status States

```
INTAKE_RECEIVED
    â†“
PROPOSAL_SENT
    â†“
PROPOSAL_ACCEPTED  â†  PROPOSAL_REJECTED (archive)
    â†“
KICKOFF
    â†“
IN_EXECUTION
    â†“
IN_QA_REVIEW
    â†“
CLIENT_REVIEW
    â†“
DELIVERED
    â†“
INVOICE_SENT
    â†“
PAID â†’ CLOSED
```

---

## SLA Targets

| Phase | Target Duration |
|-------|----------------|
| Intake â†’ Proposal | â‰¤ 2 business hours |
| Proposal â†’ Kickoff | â‰¤ 1 day after ACCEPT |
| Execution | Per proposal timeline |
| QA | â‰¤ 20% of total timeline |
| Delivery | â‰¤ 1 day after QA pass |
| Invoice | Immediately upon DELIVERED |
| Payment | Client: 7 days |

---

*Projects directory: `brain/memory/projects/`*
*Invoices: `brain/memory/system_memory/invoices/`*
*Knowledge base: `knowledge/project_learnings/`*


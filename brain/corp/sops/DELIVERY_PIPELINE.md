# DELIVERY PIPELINE — SOP v1.0
# OmniClaw | Tier 1 — Operations
# Effective: 2026-03-18

> **Purpose:** The complete workflow from when the client ACCEPTs a proposal → Deliver → Invoice.
> Continuing from `CLIENT_INTAKE_GATEWAY.md` and `Proposal Engine`.

---

## Pipeline Overview

```
PROPOSAL ACCEPTED
      │
      ▼
[Phase 1: KICKOFF]        ─ 1 day
  - Confirm scope
  - Assign team
  - Setup workspace
      │
      ▼
[Phase 2: EXECUTION]      ─ Follow committed timeline
  - Dept leads receive brief
  - Agents execute
  - Progress tracking
      │
      ▼
[Phase 3: QA & REVIEW]    ─ 1-3 days
  - QA dept checks
  - Client review round 1
  - Revisions (max 2 rounds)
      │
      ▼
[Phase 4: DELIVERY]       ─ 1 day
  - Package deliverables
  - Handoff to client
  - Collect feedback
      │
      ▼
[Phase 5: INVOICE & CLOSE]─ 1 day
  - Generate invoice
  - Payment tracking
  - Archive project
      │
      ▼
[Phase 6: LEARNING LOOP]  ─ Auto
  - corp_learning_loop retro
  - Update KPI scoreboard
  - Knowledge extraction
```

---

## Phase 1: KICKOFF

**Trigger:** Client replies "ACCEPT" | "Proceed" | "Agreed" on the proposal

**Actions:**
1. `project_intake_agent` → update status to: `ACCEPTED`
2. Create **Project Workspace**:
   ```
   shared-context/projects/<PROJECT-ID>/
   ├── brief.json          ← copy of intake record
   ├── proposal.md         ← accepted proposal
   ├── workspace/          ← working files
   ├── deliverables/       ← final output
   └── comms_log.md        ← all client communications
   ```
3. Assign **Project Lead** from operations
4. Create department briefs → send to `subagents/mq/<dept>_brief.md`
5. Notify client: "✅ Project [ID] has been kicked off! Lead: [agent name]"

---

## Phase 2: EXECUTION

**Responsibility:** Dept leads + assigned agents

**Progress Tracking:**
- Each agent updates `shared-context/projects/<ID>/progress.json` after completing a task
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
- `ops-router` (tinyclaw) checks progress every 4h → reports to ops

**Communication Rules:**
- Client updates: every 24-48h (depending on timeline)  
- Log all comms in `comms_log.md`
- Blockers → notify ops immediately

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
- > 2 rounds → Out of scope, charge extra → CEO approval required

---

## Phase 4: DELIVERY

**Delivery Package:**
```
deliverables/
├── [project-files...]
├── README.md           ← usage guide
├── DELIVERY_RECEIPT.md ← confirmation of handoff
└── support_contact.md  ← post-delivery support contacts
```

**Handoff:**
1. Zip and share via channel (or Google Drive/cloud link)
2. Client signs `DELIVERY_RECEIPT.md` (reply "RECEIVED" or "✅")
3. Update status to: `DELIVERED`

---

## Phase 5: INVOICE & CLOSE

**Invoice Generation:**
```
shared-context/brain/corp/invoices/INVOICE-<YYYYMMDD>-<PROJECT-ID>.md

Content:
  - Project summary
  - Deliverables listed
  - Hours spent (if T&M)
  - Amount due
  - Payment methods: [bank transfer / crypto / PayPal]
  - Due: 7 days
```

**Payment Status Tracking:**
- `shared-context/brain/corp/invoices/_payment_tracker.json`
- Reminder: +7 days unpaid → follow up
- Reminder: +14 days → escalate

**Project Close:**
- Archive to: `shared-context/projects/archive/<PROJECT-ID>/`
- Rating: collect 1-5 star feedback from client
- Update `corp/kpi_scoreboard.json`: projects_delivered + 1

---

## Phase 6: LEARNING LOOP

**Auto-trigger** after invoice PAID:

1. **corp_learning_loop** runs project retro:
   - What went well? → document in `knowledge/project_learnings/`
   - What needs improvement?
   - Any skill gaps detected? → propose training
   
2. **KPI Update:**
   - Revenue realized
   - Client satisfaction score
   - Delivery time vs estimate

3. **Knowledge Extraction:**
   - If the project generated reusable code/skills → propose adding to SKILL_REGISTRY

---

## Project Status States

```
INTAKE_RECEIVED
    ↓
PROPOSAL_SENT
    ↓
PROPOSAL_ACCEPTED  ←  PROPOSAL_REJECTED (archive)
    ↓
KICKOFF
    ↓
IN_EXECUTION
    ↓
IN_QA_REVIEW
    ↓
CLIENT_REVIEW
    ↓
DELIVERED
    ↓
INVOICE_SENT
    ↓
PAID → CLOSED
```

---

## SLA Targets

| Phase | Target Duration |
|-------|----------------|
| Intake → Proposal | ≤ 2 business hours |
| Proposal → Kickoff | ≤ 1 day after ACCEPT |
| Execution | Per proposal timeline |
| QA | ≤ 20% of total timeline |
| Delivery | ≤ 1 day after QA pass |
| Invoice | Immediately upon DELIVERED |
| Payment | Client: 7 days |

---

*Projects directory: `shared-context/projects/`*
*Invoices: `shared-context/brain/corp/invoices/`*
*Knowledge base: `knowledge/project_learnings/`*

# DELIVERY PIPELINE — SOP v1.0
# OmniClaw Corp | Tier 1 — Operations
# Effective: 2026-03-18

> **Mục đích:** Quy trình hoàn chỉnh từ khi client ACCEPT proposal → Deliver → Invoice.
> Tiếp nối từ `CLIENT_INTAKE_GATEWAY.md` và `Proposal Engine`.

---

## Tổng Quan Pipeline

```
PROPOSAL ACCEPTED
      │
      ▼
[Phase 1: KICKOFF]        ─ 1 ngày
  - Xác nhận scope
  - Assign team
  - Setup workspace
      │
      ▼
[Phase 2: EXECUTION]      ─ Theo timeline đã commit
  - Dept leads nhận brief
  - Agents thực thi
  - Progress tracking
      │
      ▼
[Phase 3: QA & REVIEW]    ─ 1-3 ngày
  - QA dept kiểm tra
  - Client review round 1
  - Revisions (2 rounds max)
      │
      ▼
[Phase 4: DELIVERY]       ─ 1 ngày
  - Package deliverables
  - Handoff to client
  - Collect feedback
      │
      ▼
[Phase 5: INVOICE & CLOSE]─ 1 ngày
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

**Trigger:** Client reply "ACCEPT" | "Đồng ý" | "Proceed" vào proposal

**Actions:**
1. `project_intake_agent` → update status: `ACCEPTED`
2. Tạo **Project Workspace**:
   ```
   shared-context/projects/<PROJECT-ID>/
   ├── brief.json          ← copy intake record
   ├── proposal.md         ← accepted proposal
   ├── workspace/          ← working files
   ├── deliverables/       ← final output
   └── comms_log.md        ← all client communications
   ```
3. Assign **Project Lead** từ operations
4. Create department briefs → gửi vào `subagents/mq/<dept>_brief.md`
5. Notify client: "✅ Project [ID] đã được khởi động! Lead: [tên agent]"

---

## Phase 2: EXECUTION

**Responsibility:** Dept leads + assigned agents

**Progress Tracking:**
- Mỗi agent update `shared-context/projects/<ID>/progress.json` sau mỗi task
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
- `ops-router` (tinyclaw) check progress mỗi 4h → report cho ops

**Communication Rules:**
- Client update: mỗi 24-48h (tùy timeline)  
- All comms log vào `comms_log.md`
- Blocker phát sinh → immediate ops notify

---

## Phase 3: QA & REVIEW

**QA Checklist** (qa-agent thực hiện):
- [ ] Deliverables đúng scope trong proposal
- [ ] Không có bug/error rõ ràng
- [ ] File format đúng yêu cầu
- [ ] Docs đầy đủ

**Client Review:**
- Gửi deliverables preview qua channel gốc
- Wait 48h cho feedback
- Round 1 revision nếu cần
- Round 2 revision (cuối) nếu cần
- > 2 rounds → OOscope, charge thêm → CEO approval

---

## Phase 4: DELIVERY

**Delivery Package:**
```
deliverables/
├── [project-files...]
├── README.md           ← hướng dẫn sử dụng
├── DELIVERY_RECEIPT.md ← confirm handoff
└── support_contact.md  ← liên hệ hỗ trợ sau delivery
```

**Handoff:**
1. Zip và share qua channel (hoặc link Google Drive/cloud)
2. Client ký nhận `DELIVERY_RECEIPT.md` (reply "RECEIVED" hoặc "✅")
3. Update status: `DELIVERED`

---

## Phase 5: INVOICE & CLOSE

**Invoice Generation:**
```
shared-context/brain/corp/invoices/INVOICE-<YYYYMMDD>-<PROJECT-ID>.md

Content:
  - Project summary
  - Deliverables listed
  - Hours spent (nếu T&M)
  - Amount due
  - Payment methods: [bank transfer / crypto / PayPal]
  - Due: 7 ngày
```

**Payment Status Tracking:**
- `shared-context/brain/corp/invoices/_payment_tracker.json`
- Reminder: +7 ngày chưa thanh toán → follow up
- Reminder: +14 ngày → escalate

**Project Close:**
- Archive to: `shared-context/projects/archive/<PROJECT-ID>/`
- Rating: thu thập feedback 1-5 sao từ client
- Update `corp/kpi_scoreboard.json`: projects_delivered + 1

---

## Phase 6: LEARNING LOOP

**Auto-trigger** sau khi invoice PAID:

1. **corp_learning_loop** run retro cho project:
   - Gì đã tốt? → document trong `knowledge/project_learnings/`
   - Gì cần cải thiện?
   - Skill gap phát hiện? → đề xuất training
   
2. **KPI Update:**
   - Revenue realized
   - Client satisfaction score
   - Delivery time vs estimate

3. **Knowledge Extraction:**
   - Nếu project tạo ra reusable code/skill → đề xuất thêm vào SKILL_REGISTRY

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
| Intake → Proposal | ≤ 2 giờ làm việc |
| Proposal → Kickoff | ≤ 1 ngày sau ACCEPT |
| Execution | Per proposal timeline |
| QA | ≤ 20% total timeline |
| Delivery | ≤ 1 ngày sau QA pass |
| Invoice | Ngay khi DELIVERED |
| Payment | Client: 7 ngày |

---

*Thư mục projects: `shared-context/projects/`*
*Invoice: `shared-context/brain/corp/invoices/`*
*Knowledge: `knowledge/project_learnings/`*


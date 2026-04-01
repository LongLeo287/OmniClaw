# CLIENT INTAKE GATEWAY — SOP v1.0
# OmniClaw Corp | Tier 1 — Operations
# Effective: 2026-03-18

> **Model:** Bên ngoài kết nối vào OmniClaw Corp để sử dụng AI agents như dịch vụ.
> Client → Channel → Intake Agent → Proposal → Delivery Pipeline

---

## 1. Cổng Tiếp Nhận

OmniClaw Corp tiếp nhận yêu cầu qua **4 kênh**:

| Kênh | Platform | Agent xử lý | Status |
|------|----------|-------------|--------|
| Telegram | Bot @AICorpBot | nullclaw `client-intake` agent | 🟡 Cần config |
| Discord | #project-intake channel | tinyclaw `intake-agent` | 🟡 Cần config |
| Web Form | `intake.omniclaw-corp.local` | project-intake-agent SKILL | 🟡 Cần build |
| WhatsApp | Business API | nullclaw `whatsapp` channel | 🔴 Phase 2 |

---

## 2. Intake Flow

```
[CLIENT gửi brief qua Channel]
         │
         ▼
[NULLCLAW / TINYCLAW — Channel Gateway]
  - nhận message
  - sanitize & validate input
  - route đến project-intake-agent
         │
         ▼
[PROJECT-INTAKE-AGENT — thu thập thông tin]
  Thu thập 5 fields bắt buộc:
  1. project_type    — Web / Mobile / AI / Data / Automation / Other
  2. description     — Mô tả ngắn (max 500 words)
  3. timeline        — Deadline mong muốn
  4. budget_range    — Bracket: <$500 | $500-2k | $2k-10k | $10k+
  5. contact_info    — Telegram/Email/Discord handle
         │
         ▼
[VALIDATE & SCORE]
  - Completeness check (tất cả 5 fields?)
  - Feasibility score (1-10) dựa trên skill registry
  - Priority: URGENT / NORMAL / LOW
         │
         ▼
[ROUTE TO PROPOSAL ENGINE]
  → Ghi vào: shared-context/client_intake/YYYY-MM-DD_HHMMSS_<slug>.json
  → Notify: operations dept + CEO (nếu budget > $2k)
  → Tự động trigger Proposal Engine
```

---

## 3. Brief Template (Client-Facing)

Khi client nhắn tin lần đầu, bot tự động gửi form sau:

```
👋 Chào mừng đến OmniClaw Corp!

Để bắt đầu, vui lòng trả lời 5 câu hỏi:

1️⃣ Loại project: Web / Mobile / AI Chatbot / Data / Automation / Khác
2️⃣ Mô tả ngắn: [Max 500 chữ]
3️⃣ Deadline mong muốn: [DD/MM/YYYY]
4️⃣ Budget: Dưới $500 / $500-2k / $2k-10k / $10k+
5️⃣ Cách liên lạc: [Telegram/Email]

Sau khi điền xong, team sẽ phản hồi trong 2 giờ làm việc. ✅
```

---

## 4. Intake Record Schema

```json
{
  "intake_id": "INTAKE-20260318-001",
  "received_at": "2026-03-18T09:55:00+07:00",
  "channel": "telegram",
  "client": {
    "handle": "@client_username",
    "contact": "email@example.com"
  },
  "brief": {
    "project_type": "web",
    "description": "...",
    "timeline": "2026-04-30",
    "budget_range": "$2k-10k"
  },
  "scoring": {
    "feasibility": 8,
    "priority": "NORMAL",
    "matched_skills": ["ui-ux", "shell_assistant", "visual_excellence"]
  },
  "status": "PENDING_PROPOSAL",
  "assigned_dept": null,
  "proposal_id": null
}
```

---

## 5. Routing Rules

| Budget | Feasibility | Action |
|--------|-------------|--------|
| $10k+ | Any | Notify CEO immediate + auto-propose |
| $2k-10k | ≥7 | Auto-propose → operations approval |
| $500-2k | ≥5 | Auto-propose → ops handles |
| <$500 | Any | Standard SOP — ops team |
| Any | <4 | Flag: "Skill gap" → R&D dept evaluate |

---

## 6. Files & Paths

| File | Mục đích |
|------|---------|
| `shared-context/client_intake/` | Thư mục lưu tất cả intake records |
| `shared-context/client_intake/_index.json` | Index tất cả intakes |
| `shared-context/brain/corp/proposals/` | Proposals auto-generated |
| `shared-context/brain/corp/escalations.md` | CEO escalations |

---

*Channel configs: xem `REMOTE/claws/nullclaw/configs/client_gateway.json`*
*Sau khi intake: trigger `PROPOSAL_ENGINE_SOP.md`*


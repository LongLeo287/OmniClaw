---
id: client-intake-gateway
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:06.628206
---

# CLIENT INTAKE GATEWAY — SOP v1.0
# OmniClaw | Tier 1 — Operations
# Effective: 2026-03-18

> **Model:** External connections to OmniClaw to utilize AI agents as a service.
> Client → Channel → Intake Agent → Proposal → Delivery Pipeline

---

## 1. Reception Portal

OmniClaw receives requests via **4 channels**:

| Channel | Platform | Assigned Agent | Status |
|------|----------|-------------|--------|
| Telegram | Bot @AICorpBot | nullclaw `client-intake` agent | 🟡 Needs config |
| Discord | #project-intake channel | tinyclaw `intake-agent` | 🟡 Needs config |
| Web Form | `intake.omniclaw.local` | project-intake-agent SKILL | 🟡 Needs build |
| WhatsApp | Business API | nullclaw `whatsapp` channel | 🔴 Phase 2 |

---

## 2. Intake Flow

```
[CLIENT sends brief via Channel]
         │
         ▼
[NULLCLAW / TINYCLAW — Channel Gateway]
  - receive message
  - sanitize & validate input
  - route to project-intake-agent
         │
         ▼
[PROJECT-INTAKE-AGENT — gather information]
  Collects 5 mandatory fields:
  1. project_type    — Web / Mobile / AI / Data / Automation / Other
  2. description     — Short description (max 500 words)
  3. timeline        — Desired deadline
  4. budget_range    — Bracket: <$500 | $500-2k | $2k-10k | $10k+
  5. contact_info    — Telegram/Email/Discord handle
         │
         ▼
[VALIDATE & SCORE]
  - Completeness check (all 5 fields present?)
  - Feasibility score (1-10) based on skill registry
  - Priority: URGENT / NORMAL / LOW
         │
         ▼
[ROUTE TO PROPOSAL ENGINE]
  → Write to: shared-context/client_intake/YYYY-MM-DD_HHMMSS_<slug>.json
  → Notify: operations dept + CEO (if budget > $2k)
  → Auto-trigger Proposal Engine
```

---

## 3. Brief Template (Client-Facing)

When a client messages for the first time, the bot automatically sends the following form:

```
👋 Welcome to OmniClaw!

To get started, please answer 5 simple questions:

1️⃣ Project Type: Web / Mobile / AI Chatbot / Data / Automation / Other
2️⃣ Short Description: [Max 500 words]
3️⃣ Desired Deadline: [DD/MM/YYYY]
4️⃣ Budget: Under $500 / $500-2k / $2k-10k / $10k+
5️⃣ Contact Method: [Telegram/Email]

Once submitted, our team will respond within 2 business hours. ✅
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
| $10k+ | Any | Notify CEO immediately + auto-propose |
| $2k-10k | ≥7 | Auto-propose → operations approval |
| $500-2k | ≥5 | Auto-propose → ops handles |
| <$500 | Any | Standard SOP — ops team |
| Any | <4 | Flag: "Skill gap" → R&D dept evaluate |

---

## 6. Files & Paths

| File | Purpose |
|------|---------|
| `shared-context/client_intake/` | Directory storing all intake records |
| `shared-context/client_intake/_index.json` | Index of all intakes |
| `shared-context/brain/corp/proposals/` | Auto-generated proposals |
| `shared-context/brain/corp/escalations.md` | CEO escalations |

---

*Channel configs: see `REMOTE/claws/nullclaw/configs/client_gateway.json`*
*Post-intake: trigger `PROPOSAL_ENGINE_SOP.md`*

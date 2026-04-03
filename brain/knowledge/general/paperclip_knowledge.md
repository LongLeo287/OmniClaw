---
id: paperclip-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:18.576946
---

# KNOWLEDGE EXTRACT: paperclip
> **Extracted on:** 2026-03-30 17:50:35
> **Source:** paperclip

---

## File: `knowledge.md`
```markdown
# Knowledge File: Paperclip — Open-source Orchestration for Zero-Human Companies
# Source: https://github.com/paperclipai/paperclip
# Ingested: 2026-03-19 | Tier: T1 (Highly Relevant — Mirrors AI OS Corp Architecture)
# License: MIT | Stars: Growing | Contributors: 42
# Website: paperclip.ing

---

## SUMMARY

**"If OpenClaw is an employee, Paperclip is the company."**

Paperclip là Node.js server + React UI để **orchestrate một team AI agents chạy một business thực sự**. Bring your own agents, assign goals, track work và costs từ một dashboard duy nhất. Về bản chất, đây là implementation open-source của chính xác những gì AI OS Corp đang xây dựng.

**Key insight:** Paperclip = bản open-source của AI OS Corp vision — **công ty không người**.

---

## TÍNH NĂNG CORE

### Architecture
```
Paperclip (Node.js + React)
├── API Server — port 3100
├── Embedded PostgreSQL (tự tạo, no setup)
├── Org Charts — cấu trúc tổ chức AI agents
├── Budget System — theo dõi và giới hạn chi phí per agent
├── Goal Management — giao mục tiêu, track progress
├── Governance Layer — rules, accountability
└── Dashboard — monitor từ desktop + mobile
```

### Quickstart
```bash
npx paperclipai onboard --yes
# hoặc
git clone https://github.com/paperclipai/paperclip.git
cd paperclip && pnpm install && pnpm dev
```
Yêu cầu: Node.js 20+, pnpm 9.15+

---

## SO SÁNH VỚI AI OS CORP

| Tính năng | Paperclip | AI OS Corp |
|-----------|-----------|-----------|
| Org chart | ✅ Built-in | ✅ org_chart.yaml |
| Budgets | ✅ Per-agent cost tracking | ⬜ KPI targets (finance_agent) |
| Agent coordination | ✅ Heartbeat + events | ✅ ClawTask + nullclaw |
| Task management | ✅ Built-in | ✅ ClawTask (7474) |
| Governance | ✅ Built-in | ✅ rules.md + gates |
| Mobile dashboard | ✅ Tailscale support | ⬜ Planned |
| Multi-company | ✅ Data isolation | ⬜ Single org (current) |
| Agent marketplace | 🔶 ClipMart (coming) | ⬜ Planned |
| Plugin system | ✅ Released | ✅ AI OS plugins (88+) |
| Open source | ✅ MIT | Private |

---

## PHÙ HỢP VỚI AI OS CORP NẾU:

- ✅ Muốn build autonomous AI companies (đúng với AI OS Corp mission)
- ✅ Coordinate nhiều agents khác nhau (OpenClaw, Codex, Claude, Cursor)
- ✅ Có nhiều Claude terminals mở không theo dõi được
- ✅ Muốn agents chạy 24/7 autonomous nhưng vẫn audit được
- ✅ Muốn monitor costs và enforce budgets
- ✅ Muốn manage business từ điện thoại

---

## ĐIỂM ĐẶC BIỆT

### ClipMart (Coming Soon)
> "Download and run entire companies with one click."

Marketplace để browse, mua/bán **company templates** — full org structures, agent configs, và skills — import vào Paperclip trong vài giây.

**Cơ hội cho AI OS Corp:** Export AI OS Corp structure thành ClipMart template → distribute như một product.

### "If it can receive a heartbeat, it's hired"
Bất kỳ agent nào nhận được heartbeat đều có thể join Paperclip company. Không lock-in vào một framework hay provider nào.

---

## ROADMAP PAPERCLIP

| Item | Status |
|------|--------|
| OpenClaw onboarding | ⚪ Planned |
| Cloud agents (Cursor / e2b) | ⚪ Planned |
| ClipMart marketplace | ⚪ Planned |
| Easy agent configs | ⚪ Planned |
| Harness engineering | ⚪ Planned |
| Plugin system | 🟢 **DONE** |
| Better docs | ⚪ Planned |

---

## GỢI Ý TÍCH HỢP VỚI AI OS

### Option 1: Run Paperclip alongside ClawTask
- Paperclip: high-level company orchestration (org, goals, budgets)
- ClawTask (7474): task-level coordination + clarification flow
- Chúng complement nhau thay vì thay thế

### Option 2: Study Paperclip architecture → upgrade AI OS Corp
- Clone repo → extract governance + budget modules
- Apply patterns vào AI OS Corp implementation
- Đặc biệt: cost tracking per agent (gaps hiện tại)

### Option 3: Export AI OS Corp → ClipMart template
- Khi ClipMart launch → submit AI OS Corp template
- 21 departments + 80 agents + full rules/prompts → sellable company template

---

## TECH STACK

```
Frontend: React + TypeScript
Backend:  Node.js
Database: Embedded PostgreSQL (production: external PG)
Deploy:   pnpm run build → any Node.js host, Vercel-ready
Mobile:   Tailscale access (PWA-style)
```

---

## LINKS

- GitHub: https://github.com/paperclipai/paperclip
- Website: https://paperclip.ing
- Discord: https://discord.gg/m4HZY7xNG3
- License: MIT

---

## TAGS
`orchestration` `zero-human-company` `AI-agents` `org-chart` `budgets` `governance` `open-source` `Node.js` `ClipMart` `T1-highly-relevant`
```


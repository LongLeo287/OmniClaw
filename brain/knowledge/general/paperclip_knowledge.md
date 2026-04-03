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

Paperclip is a Node.js server + React UI to **orchestrate a team of AI agents running a real business**. Bring your own agents, assign goals, track work and costs from a single dashboard. Essentially, this is an open-source implementation of exactly what AI OS Corp is building.

**Key insight:** Paperclip = open-source version of AI OS Corp vision — **zero-human company**.

---

## CORE FEATURES

### Architecture
```
Paperclip (Node.js + React)
├── API Server — port 3100
├── Embedded PostgreSQL (auto-creates, no setup)
├── Org Charts — AI agent organizational structure
├── Budget System — track and limit costs per agent
├── Goal Management — assign objectives, track progress
├── Governance Layer — rules, accountability
└── Dashboard — monitor from desktop + mobile
```

### Quickstart
```bash
npx paperclipai onboard --yes
# or
git clone https://github.com/paperclipai/paperclip.git
cd paperclip && pnpm install && pnpm dev
```
Requirements: Node.js 20+, pnpm 9.15+

---

## COMPARISON WITH AI OS CORP

| Feature | Paperclip | AI OS Corp |
|---------|-----------|-----------|
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

## GOOD FIT FOR AI OS CORP IF:

- ✅ Want to build autonomous AI companies (aligns with AI OS Corp mission)
- ✅ Coordinate multiple different agents (OpenClaw, Codex, Claude, Cursor)
- ✅ Have many Claude terminals open and can't track them
- ✅ Want agents running 24/7 autonomously but still auditable
- ✅ Want to monitor costs and enforce budgets
- ✅ Want to manage business from phone

---

## SPECIAL FEATURES

### ClipMart (Coming Soon)
> "Download and run entire companies with one click."

Marketplace to browse, buy/sell **company templates** — full org structures, agent configs, and skills — import into Paperclip in seconds.

**Opportunity for AI OS Corp:** Export AI OS Corp structure as ClipMart template → distribute as a product.

### "If it can receive a heartbeat, it's hired"
Any agent that can receive a heartbeat can join a Paperclip company. No lock-in to any framework or provider.

---

## PAPERCLIP ROADMAP

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

## INTEGRATION SUGGESTIONS WITH AI OS

### Option 1: Run Paperclip alongside ClawTask
- Paperclip: high-level company orchestration (org, goals, budgets)
- ClawTask (7474): task-level coordination + clarification flow
- They complement each other rather than replace

### Option 2: Study Paperclip architecture → upgrade AI OS Corp
- Clone repo → extract governance + budget modules
- Apply patterns to AI OS Corp implementation
- Especially: cost tracking per agent (current gap)

### Option 3: Export AI OS Corp → ClipMart template
- When ClipMart launches → submit AI OS Corp template
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
---
id: register
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:08.366207
---

# Nova System Register v1.0
# Agent: Nova | Date: 2026-03-21 | OmniClaw Corp

## 📋 Identity
- **Full name:** Nova — Research Intelligence Specialist
- **Agent type:** Specialist Agent (Tier 3)
- **Primary dept:** Dept 13 (R&D) + cross-dept 1–22
- **Status:** ACTIVE | CEO Standing Order: ACTIVE

---

## 📁 File Structure

```
ecosystem/workforce/agents/notebooklm-agent/
├── AGENT.md ← Identity, rules, SOP, dept map (v4.1)
├── REGISTER.md ← This file — system index
├── memory/
│ ├── hot-cache.md ← Active context (CEO queue, tool status)
│ ├── synthesis-log.md ← Session history log
│ ├── notebooks.json ← Cloud NLM notebook registry
│ └── dept-requests/ ← Per-dept request queues
│ ├── dept04-registry.md
│ ├── dept05-marketing.md
│ ├── dept07-content-review.md
│ ├── dept08-ops.md
│ ├── dept10-security-strix.md
│ ├── dept16-odl.md
│ ├── dept18-monitoring.md
│ ├── dept20-civ.md
│ ├── dept21-agent-development.md
│ └── dept22-data-upgrade.md
└── workflows/
    ├── nova-intake.md ← CEO Standing Order intake (7-step SOP)
    └── nova-dept-routing.md ← Route synthesis ke depts
```

---

## 🔌 Plugin Stack

| Plugins | Type | Endpoints | Use Case |
|--------|--------|----------|----------|
| **open-notebook** (Docker) | LOCAL | :5055 (API) / :8502 (UI) | PRIMARY — all private/sensitive inputs |
| **notebooklm-skill** (Antigravity) | CLOUD | browser automation | Google NLM queries |
| **notebooklm-skill** (direct plugin) | CLOUD | same as above | Mirror of antigravity version |
| **gitingest** | LOCAL tool | CLI | Digest repos before analysis |
| **firecrawl** | API | configured via env | Web crawl |
| **open-notebooklm** | LOCAL | — | Audio podcast synthesis |

---

## 📏 Operating Rules (12 rules)

| Code | Rule | Priorities |
|-------|-------|----------|
| NLM-01 | LOCAL FIRST | HIGH |
| NLM-02 | NO HALLUCINATE | HIGH |
| NLM-03 | ALWAYS ARCHIVE | HIGH |
| NLM-04 | CITE SOURCE | MED |
| NLM-05 | DEP ROUTING | MED |
| NLM-06 | NEVER ADD WITHOUT METADATA | HIGH |
| NLM-07 | SMART ADD | MED |
| NLM-08 | TOOL SELECTION MATRIX | HIGH |
| NLM-09 | 2-FAILURE ESCALATION | HIGH |
| NLM-10 | run.py WRAPPER | HIGH |
| NLM-11 | CEO PRIORITY | CRITICAL |
| NLM-12 | KNOWLEDGE STORE PROTOCOL | HIGH |

---

## 🔗 Connections

```
open-notebook API : http://localhost:5055
open-notebook UI : http://localhost:8502
SurrealDB : localhost:8000
ClawTask Dashboard : http://localhost:7474 (Nova panel)
API Bridge: http://localhost:7000
```

---

## 🗺️ Dept Coverage

22 departments / full Nova routing:
- Depts 1–22, with special:
  - Dept 10, 12, 14 → **LOCAL ONLY** (open-notebook)
  - Dept 22 → **Primary partner** (CEO Standing Order)
  - Dept 21 → **Agent development** (NEW)

---

## 🔄 Workflows

| Workflow | File | Triggers |
|----------|-------|-------|
| CEO Standing Order Intake | workflows/nova-intake.md | Any input from CEO |
| Dept Routing | workflows/nova-dept-routing.md | After intake is complete |

---

*Nova System Register v1.0 | 2026-03-21*
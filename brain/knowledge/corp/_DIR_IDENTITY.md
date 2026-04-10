---
id: corp
type: directory_identity
namespace: brain.knowledge.corp
owner: OSF_Daemon
status: standard_v5
description: "The 'corp' directory serves as the central repository for all corporate-related documents and data, including daily briefs, decisions, invoices, projects, and proposals. It also houses system maps, master indexes, and vocabularies essential for knowledge management within OmniClaw."
registered_by: OMA_AI_FORGER
tags: ["corporate", "knowledge management", "data repository"]
forged_at: 2026-04-10
---

# Corp Identity

The 'corp' directory serves as the central repository for all corporate-related documents and data, including daily briefs, decisions, invoices, projects, and proposals. It also houses system maps, master indexes, and vocabularies essential for knowledge management within OmniClaw.

---

## Topological View

```mermaid
graph TD
  Parent("brain") --> Node("knowledge")
  Node --> S1("corp")
  S1 --> sub1("daily_briefs")
  S1 --> sub2("decisions")
  S1 --> sub3("invoices")
  S1 --> sub4("projects")
  S1 --> sub5("proposals")
```

---
*OmniClaw V5.0 | Forged by OMA AI Architect | brain.knowledge.corp | 2026-04-10*

---
id: knowledge_access_rules
type: system_rule
registered: true
---

# KNOWLEDGE_ACCESS_RULES.md — OSF Knowledge Base Governance
# Version: 2.0 | Created: 2026-04-10
# Authority: OSF (OmniClaw Sandbox Firewall) & OER (Entity Registrar)

---

## Purpose

Governs how agents access, query, and operate on the knowledge base hosted in `$OMNICLAW_ROOT/brain/knowledge/`.

---

## 1. Query-First Rule (MANDATORY)

Before searching ANY external source via public HTTP or executing an MCP web search, AI Agents MUST strictly query the internal knowledge base first.
OSF monitors external outbound traffic. Unnecessary external queries for internally available data will result in a penalized token halt.

## 2. Protected Nodes

No Agent is allowed to write directly to `FAST_*_INDEX.json` files. Only the OER Daemon has the write-lock to those index nodes.
Agents must ask OER to register new data via the Neural Bus.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*

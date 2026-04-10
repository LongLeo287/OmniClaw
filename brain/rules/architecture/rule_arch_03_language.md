---
id: RULE-ARCH-03
name: -System Language Policy (90/10 Rule)-
tags: [core, architecture, rule, language, policy]
owner: OA
type: system_rule
registered: true
---

# RULE-ARCH-03: THE 90/10 LANGUAGE POLICY

> [!IMPORTANT]
> **Authority:** OmniClaw Architecture Board (CEO & OA)
> **Severity:** ABSOLUTE

To ensure seamless system compatibility, encoding integrity, and cross-platform Agent parsing without encountering NLP/Terminal encoding corruption, OmniClaw enforces a strict **90% English - 10% Vietnamese** language distribution policy across the entire OS directory matrix.

## 🇺🇸 THE 90% RULE: ENGLISH ONLY
Unless explicitly excepted below, **EVERY SINGLE ASSET** within the system must be entirely written in English. This includes but is not limited to:
- Source Code (Python, PowerShell, JS, etc.)
- YAML/JSON Configurations, Frontmatters, and Key-Values
- Terminal/Daemon Output Logs & CI/CD Pipelines
- Internal System Markdown Files (`SKILL.md`, `_DIR_IDENTITY.md`)
- System Rules (`RULE-ARCH-*.md`)
- Agent Personas, Profiles, System Prompts, and Identities (`daemon_trust.py` definitions)

*If an AI Agent or System Daemon reads it for automated parsing, it MUST be in English.*

---

## 🇻🇳 THE 10% RULE: VIETNAMESE ALLOWED
Vietnamese text is strictly prohibited in the system architecture, EXCEPT in the following explicitly approved -Safe-Zones-:

1. **Template Files & Suffixes:**
   - Any template designated for dual language (En/Vn).
   - Any file securely isolated by the `-vn` suffix (e.g. `report-vn.md`, `project_proposal-vn.pdf`).
   
2. **Implementation Plans (Artifacts):**
   - Tactical planning artifacts (`implementation_plan.md`, `task.md`, `walkthrough.md`) generated during interactive sessions for human-review.

3. **Direct User Communications (Brainstorms & Separate Reports):**
   - Active brainstorms or specific reports requested specifically -for the CEO/User-.
   - **PRESENTATION RULE:** These Private Vietnamese documents MUST be created as Markdown Artifacts (saved to the workspace or artifact panel so they render on the left UI). They must be highly readable, utilizing rich formatting: tables, **icons**, **emojis**, and **Mermaid diagrams**. 
   - DO NOT dump long brainstorms or reports in the IDE Chat. IDE Chat is strictly reserved for brief, concise responses.

> [!CAUTION]
> Failure to adhere to the 90/10 Language Policy will trigger the OHD to route the file to `QUARANTINE_QUEUE`. Any Agent generating Vietnamese logs into Daemons or internal knowledge bases will be permanently stripped of their write privileges.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*

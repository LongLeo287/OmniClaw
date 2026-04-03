# Project: [PROJECT_NAME] — OmniClaw Connected
# PRJ-ID: PRJ-XXX
# Status: active
# Updated: [DATE]

> **Satellite project of OmniClaw.**  
> Skills, knowledge, and agents from OmniClaw are available here.
> See: `$OMNICLAW_ROOT\CLAUDE.md` for full governance.

---

## 🧭 Identity

- **Project name:** [PROJECT_NAME]
- **Path:** [PROJECT_PATH]
- **Tech stack:** [e.g., React + TypeScript, Python, GAS]
- **Domain:** [e.g., POS, Web App, Data Pipeline]

---

## 🛠️ Skills Loaded

<!-- List the OmniClaw skills relevant to this project -->

```
LOAD: $OMNICLAW_ROOT\skills\[skill-name]\SKILL.md
```

Common options:
- `ui-ux-pro-max` — Premium UI/UX design
- `pos-event-sourcing` — POS audit & event tracing
- `gas-sheets-optimizer` — Google Apps Script & Sheets
- `knowledge_navigator` — Query OmniClaw knowledge base

---

## 📁 Project Structure

```
[PROJECT_PATH]/
├── [src or main code dir]/
├── [config files]
├── .agent/
│   └── CLAUDE.md          ← this file (or in .clauderules)
└── DATA/ or docs/
```

---

## ⚡ Quick Commands

```bash
# Dev server
[dev command, e.g.: npm run dev]

# Build
[build command]

# Type check
[type check command, e.g.: npx tsc --noEmit]
```

---

## 🔗 OmniClaw Resources

| Resource | Path |
|----------|------|
| Master Entry | `$OMNICLAW_ROOT\CLAUDE.md` |
| Skill Registry | `$OMNICLAW_ROOT\shared-context\SKILL_REGISTRY.json` |
| Knowledge Base | `$OMNICLAW_ROOT\knowledge\` |
| Blackboard | `$OMNICLAW_ROOT\shared-context\blackboard.json` |
| Handoff Workflow | `$OMNICLAW_ROOT\workflows\claude_code_handoff.md` |

---

## 🔑 Key Business Rules

<!-- Fill in project-specific rules here -->
1. [Rule 1]
2. [Rule 2]

---

## ⚠️ Safe vs Prohibited Actions

**Safe (auto-approve):**
- Reading files, running dev server, type checking

**Require confirmation:**
- Deleting files, deploying to production, modifying config

**Never:**
- Touching OmniClaw core files from this workspace


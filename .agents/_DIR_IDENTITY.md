---
dir: .agents/
owner: antigravity
purpose: Antigravity agent configuration, workflow SOPs, and platform-specific operational scripts
scope: platform-local — Antigravity (Gemini) reads this. Not synced to ecosystem/.
version: v3.2
updated: 2026-04-03
---

# .agents/ — Antigravity Platform Layer

This directory is the **Antigravity-specific** operational layer.
It is NOT shared with Claude Code CLI (which reads `brain/agents/CLAUDE.md`).

## Contents

| Path | Purpose |
|------|---------|
| `workflows/` | Step-by-step SOPs that Antigravity executes autonomously |
| `config/` | Boot-time config overrides (model, timeout, routing) |

## Key Workflows

| Workflow | Trigger |
|----------|---------|
| `handoff_omniclaw.md` | CEO: "Send to OmniClaw" / quota low / large code task |
| `plugin-lazy-load.md` | Agent needs Tier 2 plugin (sandbox lifecycle) |
| `post-session.md` | Session ending detected (auto-handoff) |
| `auto-execute-commands.md` | CEO: "auto do it" / pastes command list |
| `boot-check.md` | Every session start — fast validation checklist |

## Rules

- All workflows must have frontmatter: `id`, `version`, `updated_at`, `type`
- No secrets in this directory — use `.env` / `core/ops/secrets/MASTER.env`
- New workflows must be registered in `brain/registry/SKILL_REGISTRY.json`

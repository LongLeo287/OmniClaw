---
id: onmax-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:15.038048
---

# KNOWLEDGE EXTRACT: onmax
> **Extracted on:** 2026-03-30 17:49:54
> **Source:** onmax

---

## File: `nuxt-skills.md`
```markdown
# 📦 onmax/nuxt-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/onmax/nuxt-skills
🌐 https://github.com/nuxt/nuxt/discussions/34059

## Meta
- **Stars:** ⭐ 605 | **Forks:** 🍴 25
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Vue, Nuxt, and NuxtHub skills for AI coding assistants.

## README (trích đầu)
```
> [!WARNING]
> This repo may be replaced by [nuxt-skill.onmax.me](https://nuxt-skill.onmax.me/). Stay tuned.

<p align="center">
  <img src="https://raw.githubusercontent.com/onmax/nuxt-skills/main/.github/nuxt-skills.webp" alt="Nuxt Skills" width="100%">
  <br>
  <sub>Design inspired by <a href="https://github.com/HugoRCD">HugoRCD</a>'s work</sub>
</p>

<p align="center">Vue, Nuxt, and NuxtHub skills for AI coding assistants.</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/onmax/nuxt-skills/main/.github/badge-claude-code.svg" alt="Claude Code">
  <img src="https://raw.githubusercontent.com/onmax/nuxt-skills/main/.github/badge-copilot.svg" alt="GitHub Copilot">
  <img src="https://raw.githubusercontent.com/onmax/nuxt-skills/main/.github/badge-codex.svg" alt="OpenAI Codex">
  <img src="https://raw.githubusercontent.com/onmax/nuxt-skills/main/.github/badge-gemini.svg" alt="Google Gemini">
  <img src="https://raw.githubusercontent.com/onmax/nuxt-skills/main/.github/badge-opencode.svg" alt="OpenCode">
</p>

<p align="center">
  <a href="https://github.com/nuxt/nuxt/discussions/34059">
    🔗 Related Nuxt RFC: Bundling Agent Skills in Nuxt Modules
  </a>
</p>

## Installation

```bash
npx skills add onmax/nuxt-skills
```

The [`skills`](https://www.npmjs.com/package/skills) CLI auto-detects your installed agents and provides an interactive picker. Use `-g` for global (user-wide) or `-y` to install all skills.

Works with Claude Code, Cursor, Codex, OpenCode, GitHub Copilot, Antigravity, Roo Code, and more.

### Claude Code Marketplace

An alternative for Claude Code users:

```bash
# Add marketplace
/plugin marketplace add onmax/nuxt-skills

# Install individual skills
/plugin install vue@nuxt-skills
/plugin install nuxt@nuxt-skills

# Install multiple skills
/plugin install vue@nuxt-skills nuxt@nuxt-skills nuxt-ui@nuxt-skills
```

### Manual Installation

Clone the repository and copy skill folders to your agent's skills directory:

| Agent       | Project path       | Global path                 |
| ----------- | ------------------ | --------------------------- |
| Claude Code | `.claude/skills/`  | `~/.claude/skills/`         |
| Cursor      | `.cursor/skills/`  | `~/.cursor/skills/`         |
| Codex       | `.codex/skills/`   | `~/.codex/skills/`          |
| OpenCode    | `.opencode/skill/` | `~/.config/opencode/skill/` |
| Copilot     | `.github/skills/`  | —                           |

## Skills

| Skill                | Description                                                                     |
| -------------------- | ------------------------------------------------------------------------------- |
| **vue**              | Vue 3 Composition API, components, composables, testing                         |
| **nuxt**             | Nuxt 4+ server routes, routing, middleware, config                              |
| **nuxt-modules**     | Creating Nuxt modules with defineNuxtModule, Kit utilities, testing             |

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


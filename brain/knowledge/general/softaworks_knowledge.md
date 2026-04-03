---
id: softaworks-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:15.913330
---

# KNOWLEDGE EXTRACT: softaworks
> **Extracted on:** 2026-03-30 17:53:55
> **Source:** softaworks

---

## File: `agent-toolkit.md`
```markdown
# 📦 softaworks/agent-toolkit [🔖 PENDING/APPROVE]
🔗 https://github.com/softaworks/agent-toolkit


## Meta
- **Stars:** ⭐ 1226 | **Forks:** 🍴 95
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A curated collection of skills for AI coding agents. Skills are packaged instructions and scripts that extend agent capabilities across development, documentation, planning, and professional workflows.

## README (trích đầu)
```
# Softaworks Agent Skills

Opinionated skills shared by [@leonardocouy](https://github.com/leonardocouy) for improving daily work efficiency with Claude Code. Skills are packaged instructions and scripts that extend agent capabilities across development, documentation, planning, and professional workflows.

Skills follow the [Agent Skills](https://agentskills.io/) format.

---

## 🧭 Quick Navigation

**[🚀 Installation](#-installation)** • **[📚 Available Skills](#-available-skills)** • **[🤖 Agents & Commands](#-agents--commands)** • **[📖 Skill Structure](#-skill-structure)** • **[🤝 Contributing](#-contributing)** • **[📄 License](#-license)** • **[🔗 Links](#-links)**

---

## 🚀 Installation

### Quick Install (Recommended)

```bash
npx skills add softaworks/agent-toolkit
```

This method works with multiple AI coding agents (Claude Code, Codex, Cursor, AdaL, etc.)

### Register as Plugin Marketplace

Run the following commands in Claude Code:

```bash
/plugin marketplace add softaworks/agent-toolkit
/plugin
```

### Install Plugins

**Option 1: Via Browse UI**

1. Switch to **Marketplaces** tab (use arrow keys or Tab)
2. Select **agent-toolkit**, press Enter
3. Browse and select the plugin(s) you want to install
4. Select **Install now**

**Option 2: Direct Install**

```bash
# Install specific skill
/plugin install codex@agent-toolkit
/plugin install humanizer@agent-toolkit

# Install specific agent
/plugin install agent-codebase-pattern-finder@agent-toolkit

# Install specific command
/plugin install command-codex-plan@agent-toolkit
```

**Option 3: Ask the Agent**

Simply tell Claude Code:

> Please install Skills from github.com/softaworks/agent-toolkit

### Available Plugins

Each skill, agent, and command is an individual plugin that can be installed separately:

- **Skills** → See [Available Skills](#-available-skills) for the full list
- **Agents** → See [Agents](#agents) (install as `agent-<name>@agent-toolkit`)
- **Commands** → See [Slash Commands](#slash-commands) (install as `command-<name>@agent-toolkit`)

### Update Plugins

To update plugins to the latest version:

1. Run `/plugin` in Claude Code
2. Switch to **Marketplaces** tab
3. Select **agent-toolkit**
4. Choose **Update marketplace**

You can also **Enable auto-update** to get the latest versions automatically.

### Manual Installation

**For Claude Code (Manual)** — Skills only
```bash
cp -r skills/<skill-name> ~/.claude/skills/
```

**For claude.ai** — Skills only

Add skills to project knowledge or paste SKILL.md contents into the conversation.

---

## 📚 Available Skills

| Category | Skill | Description |
|----------|-------|-------------|
| 🤖 AI Tools | [codex](skills/codex/README.md) | Advanced code analysis with GPT-5.2 |
| 🤖 AI Tools | [gemini](skills/gemini/README.md) | Large-scale review (200k+ context) |
| 🤖 AI Tools | [perplexity](skills/perplexity/README.md) | Web search & research |
| 🔮 Meta | [agent-md-refactor](skills/agent-md-refactor/README.md) | Refactor blo
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


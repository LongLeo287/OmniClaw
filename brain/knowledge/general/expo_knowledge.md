---
id: expo-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:23.221777
---

# KNOWLEDGE EXTRACT: expo
> **Extracted on:** 2026-03-30 17:36:46
> **Source:** expo

---

## File: `skills.md`
```markdown
# 📦 expo/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/expo/skills


## Meta
- **Stars:** ⭐ 1551 | **Forks:** 🍴 71
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A collection of AI agent skills for working with Expo projects and Expo Application Services

## README (trích đầu)
```
# Expo Skills

Official AI agent skills from the Expo team for building, deploying, and debugging robust Expo apps.

## Installation

We primarily use [Claude Code](https://claude.com/claude-code) at Expo, skills are fine-tuned for Opus models. But you can use these skills with any AI agent.

## Claude Code

Add the marketplace:

```
/plugin marketplace add expo/skills
```

Install the plugin:

```
/plugin install expo
```

## Cursor

**Install from GitHub**

1. Open Cursor Settings (Cmd+Shift+J / Ctrl+Shift+J)
2. Navigate to `Rules & Command` → `Project Rules` → Add Rule → Remote Rule (GitHub)
3. Enter: `https://github.com/expo/skills.git`

**How it works:** Skills are automatically discovered and used by the agent based on context. When you ask questions about Expo development, the agent will automatically use the relevant skills (e.g., `building-ui`, `data-fetching`, `deployment`) based on the skill descriptions.

**Note:** Skills won't appear in the `/` slash command menu. The `/` menu in Cursor is for custom commands (stored in `.cursor/commands/`), not for skills. Skills work via auto-discovery - the agent uses them automatically when your questions match their descriptions.

**Verify installation:** After adding the Remote Rule, try asking the agent Expo-related questions like:
- "How do I build a UI with Expo Router?"
- "How do I make API calls in my Expo app?"
- "How do I deploy my Expo app to the App Store?"

If the skills are working, the agent will use the relevant skill content to answer your questions.

## Any agent

```
bunx skills add expo/skills
```

> This will extract the skills individually so you'll need to manually upgrade them.

## License

MIT

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


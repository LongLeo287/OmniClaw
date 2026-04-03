---
id: typefully-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:24.190126
---

# KNOWLEDGE EXTRACT: typefully
> **Extracted on:** 2026-03-30 17:56:40
> **Source:** typefully

---

## File: `agent-skills.md`
```markdown
# 📦 typefully/agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/typefully/agent-skills


## Meta
- **Stars:** ⭐ 39 | **Forks:** 🍴 2
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
AI agent skills for drafting and scheduling social media posts via Typefully

## README (trích đầu)
```
# Typefully Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)]()
[![Typefully API](https://img.shields.io/badge/Typefully-API-3B9AF8)](https://typefully.com/docs/api)

AI agent skills for drafting, scheduling, and managing social media posts across X, LinkedIn, Threads, Bluesky, and Mastodon. Give your AI agent the ability to manage your social media scheduling directly from your IDE or terminal.

Built on the [Typefully API](https://typefully.com/docs/api). [Typefully](https://typefully.com) is a writing and scheduling app used by 200k+ top creators and teams to grow on X, LinkedIn, Threads, and Bluesky.

## What Are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. Add this to your project and your AI agent will be able to create, schedule, and publish social media content.

## Setup

### 1. Install the skill

**CLI** (works with Claude Code, Cursor, Windsurf, and many other agents):

```bash
npx skills add typefully/agent-skills
```

<details>
<summary>Other installation methods</summary>

**Claude Code Plugin:**

```
/plugin marketplace add typefully/agent-skills
```

Then:

```
/plugin install typefully@typefully-skills
```

**Cursor:**

1. Open Settings (Cmd+Shift+J)
2. Go to "Rules & Command" → "Project Rules"
3. Click "Add Rule" → "Remote Rule (GitHub)"
4. Enter: `https://github.com/typefully/agent-skills.git`

**Manual:**

Clone this repository and copy `skills/typefully/` to your project's `.cursor/skills/` or `.claude/skills/` directory.

</details>

### 2. Copy your API Key

You'll need a Typefully API key for the setup command. Copy an existing key or create a new one at https://typefully.com/?settings=api

### 3. Run the setup command

This configures your API key and default social set:

```bash
./scripts/typefully.js setup
```

> [!TIP]
> The path depends on how you installed the skill, but you can ask your agent "Help me set up the Typefully skill" to get the correct path.
>
> You can also set the API key as an environment variable instead: `export TYPEFULLY_API_KEY=your_key_here`

### 4. Start using it

Ask your AI agent things like:

- "Draft a tweet about [topic]"
- "Create a LinkedIn post announcing [news]"
- "Schedule my draft for tomorrow morning"
- "Show my scheduled posts"
- "Create a thread about [topic]"
- "Post this to X and LinkedIn"

## Local Development

To test this skill locally, install it from the repo root:

```bash
npx skills add .
```

Then test it in your agent to verify the latest local changes behave as expected.

## Supported Platforms

- X (formerly Twitter)
- LinkedIn
- Threads
- Bluesky
- Mastodon

## Troubleshooting

### "TYPEFULLY_API_KEY environment variable is not set"

Run the setup command:

```bash
./scripts/typefully.js setup
```

Or set the environment variable manually:

```bash
export TYPEFULLY_API_KEY=your_key_here
```

To persist
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


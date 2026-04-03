---
id: shanraisshan-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.149717
---

# KNOWLEDGE EXTRACT: shanraisshan
> **Extracted on:** 2026-03-30 17:53:19
> **Source:** shanraisshan

---

## File: `claude-code-best-practice.md`
```markdown
# 📦 shanraisshan/claude-code-best-practice [🔖 PENDING/APPROVE]
🔗 https://github.com/shanraisshan/claude-code-best-practice


## Meta
- **Stars:** ⭐ 22288 | **Forks:** 🍴 1931
- **Language:** HTML | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
practice made claude perfect

## README (trích đầu)
```
# claude-code-best-practice
practice makes claude perfect

![updated with Claude Code](https://img.shields.io/badge/updated_with_Claude_Code-v2.1.84%20(Mar%2026%2C%202026%201%3A41%20PM%20PKT)-white?style=flat&labelColor=555) <a href="https://github.com/shanraisshan/claude-code-best-practice/stargazers"><img src="https://img.shields.io/github/stars/shanraisshan/claude-code-best-practice?style=flat&label=%E2%98%85&labelColor=555&color=white" alt="GitHub Stars"></a><br>

[![Best Practice](!/tags/best-practice.svg)](best-practice/) [![Implemented](!/tags/implemented.svg)](implementation/) [![Orchestration Workflow](!/tags/orchestration-workflow.svg)](orchestration-workflow/orchestration-workflow.md) [![Boris](!/tags/boris-cherny.svg)](#-tips-and-tricks) ![Click on these badges below to see the actual sources](!/tags/click-badges.svg)<br>
<img src="!/tags/a.svg" height="14"> = Agents · <img src="!/tags/c.svg" height="14"> = Commands · <img src="!/tags/s.svg" height="14"> = Skills

<p align="center">
  <img src="!/claude-jumping.svg" alt="Claude Code mascot jumping" width="120" height="100"><br>
  <a href="https://github.com/trending"><img src="!/root/github-trending-day.svg" alt="GitHub Trending #1 Repository Of The Day"></a>
</p>

<p align="center">
  <img src="!/root/boris-slider.gif" alt="Boris Cherny on Claude Code" width="600"><br>
  Boris Cherny on X (<a href="https://x.com/bcherny/status/2007179832300581177">tweet 1</a> · <a href="https://x.com/bcherny/status/2017742741636321619">tweet 2</a> · <a href="https://x.com/bcherny/status/2021699851499798911">tweet 3</a>)
</p>


## 🧠 CONCEPTS

| Feature | Location | Description |
|---------|----------|-------------|
| <img src="!/tags/a.svg" height="14"> [**Subagents**](https://code.claude.com/docs/en/sub-agents) | `.claude/agents/<name>.md` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-subagents.md) [![Implemented](!/tags/implemented.svg)](implementation/claude-subagents-implementation.md) Autonomous actor in fresh isolated context — custom tools, permissions, model, memory, and persistent identity |
| <img src="!/tags/c.svg" height="14"> [**Commands**](https://code.claude.com/docs/en/slash-commands) | `.claude/commands/<name>.md` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-commands.md) [![Implemented](!/tags/implemented.svg)](implementation/claude-commands-implementation.md) Knowledge injected into existing context — simple user-invoked prompt templates for workflow orchestration |
| <img src="!/tags/s.svg" height="14"> [**Skills**](https://code.claude.com/docs/en/skills) | `.claude/skills/<name>/SKILL.md` | [![Best Practice](!/tags/best-practice.svg)](best-practice/claude-skills.md) [![Implemented](!/tags/implemented.svg)](implementation/claude-skills-implementation.md) Knowledge injected into existing context — configurable, preloadable, auto-discoverable, with context forking and progressive disclosure · [Official Skills](https://github.com/anthropics/
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `claude-code-codex-cursor-gemini.md`
```markdown
# 📦 shanraisshan/claude-code-codex-cursor-gemini [🔖 PENDING/APPROVE]
🔗 https://github.com/shanraisshan/claude-code-codex-cursor-gemini


## Meta
- **Stars:** ⭐ 9 | **Forks:** 🍴 0
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-05
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
claude code vs codex vs cursor vs gemini cli vs opencode vs augment vs droid

## README (trích đầu)
```
# claude-code-codex-cursor-gemini

![AI Coding Tools](!/banner-pills.svg)

![Battle of the AI Agents](!/claude-mascot.svg)
![Battle of the AI Agents](!/codex-mascot.svg)
![Battle of the AI Agents](!/cursor-mascot.svg)
![Battle of the AI Agents](!/gemini-mascot.svg)

![AI Models](!/banner-models.svg)

> **Last Updated:** 2026-02-09

**AI TERMS:**

| | | | | |
|---|---|---|---|---|
| Agentic Engineering | AI Slop | Context Bloat | Context Engineering | Context Rot |
| Dumb Zone | Hallucination | Scaffolding | Orchestration | Vibe Coding |

[**See Complete List →**](/reports/ai-terms.md)

## Context Window Comparison

| Tool | Largest Context | Best Model | Input $/M | Output $/M | Source |
|------|-----------------|------------|-----------|------------|--------|
| Claude Code | 1M (beta) | Opus 4.6 with `context-1m-2025-08-07` beta | $5.00 | $25.00 | [Anthropic Models](https://docs.anthropic.com/en/docs/about-claude/models) |
| Codex CLI | 400k | GPT-5.3-Codex (Feb 2026) | TBD* | TBD* | [OpenAI Models](https://platform.openai.com/docs/models) |
| Cursor | 2M (native) | Gemini 3 Pro (200k/1M/2M modes) | $2.00** | $12.00** | [Cursor Models](https://cursor.com/docs/models) |
| Gemini CLI | 1M | Gemini 3 Pro Preview | $2.00 | $12.00 | [Gemini API](https://ai.google.dev/gemini-api/docs/models) |

> \* GPT-5.3-Codex pricing not yet published by OpenAI (Feb 2026 release)
> \*\* Cursor uses subscription pricing ($20/mo Pro); API prices shown are for underlying models

[View Full Report](reports/context-comparison.md)

---

## Feature Comparison

| Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---------|:-----------:|:---------:|:----------:|:------:|
| **Hooks** | ✅ 9+ types | ⚠️ Limited | ✅ 10 events | ✅ 40x faster |
| **Plugins/MCP** | ✅ Full | ✅ Full | ✅ FastMCP | ✅ Full |
| **Sub-agents** | ✅ Teams (exp) | ✅ Beta | ✅ A2A (exp) | ✅ Custom |
| **Slash Commands** | ✅ Custom | ✅ Custom | ✅ Custom | ✅ Custom |
| **Custom Commands** | ✅ Skills | ✅ AGENTS.md | ✅ GEMINI.md | ✅ Rules |
| **IDE Integration** | ✅ VS/JetBrains | ✅ Multi-platform | ✅ VS Code | ✅ Native |
| **Git Integration** | ✅ Hub (beta) | ✅ GitHub (preview) | ✅ Actions (beta) | ✅ Blame (ent) |
| **Web Search** | ✅ US only | ✅ Built-in | ✅ Grounding | ✅ @Web |
| **Image Support** | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| **Memory/Persistence** | ✅ Session | ✅ Thread | ✅ Project | ✅ Memories |
| **Multi-file Editing** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Composer |
| **Auto-commit** | ⚠️ Via hooks | ⚠️ Manual | ✅ Native | ✅ Native |
| **Custom System Prompts** | ✅ Settings | ✅ AGENTS.md | ✅ GEMINI.md | ✅ Rules |
| **Cost Tracking** | ✅ Dashboard | ⚠️ /status | ✅ /stats | ⚠️ Enterprise |
| **Sandbox Mode** | ✅ Native | ✅ OS-enforced | ✅ Container | ✅ Linux (ent) |

[View Full Report](reports/feature-comparison.md)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `claude-code-hooks.md`
```markdown
# 📦 shanraisshan/claude-code-hooks [🔖 PENDING/APPROVE]
🔗 https://github.com/shanraisshan/claude-code-hooks


## Meta
- **Stars:** ⭐ 206 | **Forks:** 🍴 10
- **Language:** HTML | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
adding voice to claude code via hooks

## README (trích đầu)
```
# Claude Code Hooks
[![Hooks](https://img.shields.io/badge/supports%20all-25%20hooks-white?style=flat&labelColor=555)](https://github.com/shanraisshan/claude-code-hooks/blob/main/.claude/hooks/HOOKS-README.md#hook-events-overview---official-25-hooks) [![Version](https://img.shields.io/badge/updated%20with%20Claude%20Code-v2.1.83%20(Mar%2025%2C%202026%209:53%20PM%20PKT)-white?style=flat&labelColor=555)](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) [![Stars](https://img.shields.io/github/stars/shanraisshan/claude-code-hooks?style=flat&label=%E2%98%85&labelColor=555&color=white)](https://github.com/shanraisshan/claude-code-hooks)

<p align="center">
  <img src="!/claude-speaking.svg" alt="Claude Code mascot speaking" width="168" height="108">
</p>

<p align="center">
  <img src="!/repo-description.svg" alt="Mouse click on PreToolUse, Keyboard on PostToolUse, Human voice on other hooks" height="56">
</p>

# [Demo Video + Presentation](https://youtu.be/6_y3AtkgjqA)

<p>
  <a href="https://youtu.be/6_y3AtkgjqA"><img src="!/pill-youtube-red.svg" alt="YouTube" height="36"></a>&nbsp;
  <a href="presentation/index.html"><img src="!/pill-slides.svg" alt="Slides" height="36"></a>
</p>

[![thumbnail](!/thumbnail3.jpg)](https://youtu.be/6_y3AtkgjqA)

## Installation

<p>
  <a href="install/README-mac.md"><img src="!/pill-mac.svg" alt="Mac" height="36"></a>&nbsp;
  <a href="install/README-linux.md"><img src="!/pill-linux.svg" alt="Linux" height="36"></a>&nbsp;
  <a href="install/README-windows.md"><img src="!/pill-windows.svg" alt="Windows" height="36"></a>
</p>

![How to Use](!/how-to-use.svg)

**Step 1.** Start Claude Code:
```bash
claude
```

**Step 2.** Send a prompt (e.g., `Hi`) — you'll hear a sound on session start, tool use, agent response, and more.

## Common Errors

If you don't follow the prerequisites, you will see the following error on claude code start

```
SessionStart:startup hook error
```

## Changelog
new hook addition changelogs only

| Date | Hooks | Changes | Claude Code Version | Demo |
|------|:-----:|---------|:-------------------:|:----:|
| Mar 25, 2026 | 25 | Added `CwdChanged`, `FileChanged` | [v2.1.83](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2183) | |
| Mar 18, 2026 | 23 | Added `StopFailure` | [v2.1.78](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2178) | |
| Mar 14, 2026 | 22 | Added `PostCompact`, `Elicitation`, `ElicitationResult` | [v2.1.76](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2176) | |
| Mar 5, 2026 | 19 | Added `InstructionsLoaded` | [v2.1.69](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2169) | |
| Feb 21, 2026 | 18 | Added `WorktreeCreate` and `WorktreeRemove` | [v2.1.50](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2150) | |
| Feb 20, 2026 | 16 | Added `ConfigChange` | [v2.1.49](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md#2149) | |
| Feb 6, 2026 | 15 | Added `Teammate
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `claude-code-status-line.md`
```markdown
# 📦 shanraisshan/claude-code-status-line [🔖 PENDING/APPROVE]
🔗 https://github.com/shanraisshan/claude-code-status-line


## Meta
- **Stars:** ⭐ 42 | **Forks:** 🍴 4
- **Language:** Shell | **License:** Unknown
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A custom status line script for Claude Code that displays context window usage, git status, and model information.

## README (trích đầu)
```
# Claude Code Status Line

<p align="center">
  <img src="!/claude-pointing.svg" alt="Claude Code mascot jumping and pointing" width="140" height="126">
  <img src="!/claude-monitor.svg" alt="Claude Code status line monitor" width="224" height="182">
</p>

A minimal status line script for [Claude Code](https://claude.ai/) that displays model name and context window usage.

![Status Line Example](https://img.shields.io/badge/Claude%20Code-2.1.6+-blue)

![Screenshot](!/comparision.png)

## Preview

**Session start (loading state):**
```
Opus 4.5 | ○○○○○○○○○○ loading...
```

**Normal usage (blue circles):**
```
Opus 4.5 | ●●●○○○○○○○ 30k/200k (15% used)
```

**Warning state (red circles when > 60%):**
```
Opus 4.5 | ●●●●●●●○○○ 140k/200k (70% used)
```

## Features

- **Context Window Display**: Shows token usage with circle-based progress bar
- **Loading State**: Empty circles with "loading..." at session start
- **Warning Indicator**: Circles turn red when context usage exceeds 60%
- **Minimal Design**: Shows only model name and context - no clutter

## Requirements

- Claude Code v2.1.6 or higher
- `jq` (JSON processor)
- Bash shell

## Installation

1. **Create the scripts directory** (if it doesn't exist):
   ```bash
   mkdir -p ~/.claude/scripts
   ```

2. **Copy the script**:
   ```bash
   curl -o ~/.claude/scripts/status-line.sh https://raw.githubusercontent.com/shanraisshan/claude-code-status-line/main/status-line.sh
   ```

   Or manually copy `status-line.sh` to `~/.claude/scripts/`

3. **Make it executable**:
   ```bash
   chmod +x ~/.claude/scripts/status-line.sh
   ```

4. **Configure Claude Code** by adding to `~/.claude/settings.json`:
   ```json
   {
     "statusLine": {
       "type": "command",
       "command": "~/.claude/scripts/status-line.sh"
     }
   }
   ```

5. **Restart Claude Code** to see the new status line.

## How It Works

The script reads JSON data from Claude Code via stdin and displays:

- **Model name**: From `model.display_name` or `model.id`
- **Context usage**: Calculated from `context_window.used_percentage`
- **Progress bar**: 10 circles showing usage visually


## Status Line Input JSON

Claude Code pipes JSON data to your status line script. Key fields used:

```json
{
  "context_window": {
    "context_window_size": 200000,
    "used_percentage": 24
  },
  "model": {
    "id": "claude-opus-4-5-20251101",
    "display_name": "Opus 4.5"
  }
}
```

## Created By

Claude Code

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `codex-cli-best-practice.md`
```markdown
# 📦 shanraisshan/codex-cli-best-practice [🔖 PENDING/APPROVE]
🔗 https://github.com/shanraisshan/codex-cli-best-practice


## Meta
- **Stars:** ⭐ 243 | **Forks:** 🍴 13
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
practice makes codex perfect

## README (trích đầu)
```
# codex-cli-best-practice
practice makes codex perfect

![Last Updated](https://img.shields.io/badge/Last_Updated-Mar_20%2C_2026_7%3A59_AM_PKT-white?style=flat&labelColor=555) <a href="https://github.com/shanraisshan/codex-cli-best-practice/stargazers"><img src="https://img.shields.io/github/stars/shanraisshan/codex-cli-best-practice?style=flat&label=%E2%98%85&labelColor=555&color=white" alt="GitHub Stars"></a>

[![Best Practice](!/tags/best-practice.svg)](best-practice/) *Click on this badge to show the latest best practice*<br>
[![Implemented](!/tags/implemented.svg)](.codex/) *Click on this badge to show implementation in this repo*<br>
[![Orchestration Workflow](!/tags/orchestration-workflow.svg)](orchestration-workflow/orchestration-workflow.md) *Click on this badge to see the Agent → Skill orchestration workflow*

<p align="center">
  <img src="!/codex-jumping.svg" alt="Codex CLI mascot jumping" width="120" height="100">
</p>

## CONCEPTS

| Feature | Location | Description |
|---------|----------|-------------|
| [**Commands**](https://developers.openai.com/codex/cli/slash-commands) | `custom not supported` | Custom commands (`.codex/commands/`) are not yet supported — built-in only: `/plan`, `/skills`, `/experimental` |
| [**Subagents**](https://developers.openai.com/codex/subagents) | [`.codex/agents/<name>.toml`](.codex/agents/) | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-subagents.md) [![Implemented](!/tags/implemented.svg)](.codex/agents/) Custom agents registered under `[agents.<name>]` with dedicated TOML role configs, CSV batch processing, and multi-agent orchestration |
| [**Skills**](https://developers.openai.com/codex/skills) | [`.agents/skills/<name>/SKILL.md`](.agents/skills/) | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-skills.md) [![Implemented](!/tags/implemented.svg)](.agents/skills/) [Reference](docs/SKILLS.md) Reusable instruction packages with YAML frontmatter — invoke with `/skill-name` or preload into agents · Built-in: `$plan`, `$skill-creator`, `$web-search` |
| [**Workflows**](https://developers.openai.com/codex/workflows/) | [`.codex/agents/weather-agent.toml`](.codex/agents/weather-agent.toml) | [![Orchestration Workflow](!/tags/orchestration-workflow.svg)](orchestration-workflow/orchestration-workflow.md) End-to-end usage patterns using the Agent → Skill pattern |
| [**MCP Servers**](https://developers.openai.com/codex/mcp) | `config.toml` → `[mcp_servers.*]` | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-mcp.md) [![Implemented](!/tags/implemented.svg)](.codex/config.toml) Model Context Protocol for external tools — plus Codex-as-MCP-server pattern |
| [**Config**](https://developers.openai.com/codex/config-basic) | [`.codex/config.toml`](.codex/config.toml) | [![Best Practice](!/tags/best-practice.svg)](best-practice/codex-config.md) [![Implemented](!/tags/implemented.svg)](.codex/config.toml) TOML-based layered config system · [Profiles](https://
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `novel-llm-26.md`
```markdown
# 📦 shanraisshan/novel-llm-26 [🔖 PENDING/APPROVE]
🔗 https://github.com/shanraisshan/novel-llm-26


## Meta
- **Stars:** ⭐ 18 | **Forks:** 🍴 1
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
novel question for 2026 models

## README (trích đầu)
```
# Novel LLM-Breaking Questions - Infinite Research Loop

![Status](https://img.shields.io/badge/Status-RESEARCHING-yellow?style=for-the-badge)
![Questions Tested](https://img.shields.io/badge/Questions_Tested-104-blue?style=for-the-badge)
![Winning Score](https://img.shields.io/badge/Winning_Score-0%25_Consensus-gold?style=for-the-badge)

An automated infinite loop research workflow that generates questions designed to **break modern LLMs**. The goal is to find simple, generic questions that any human can easily answer, but cause AI models to disagree.

<p align="center">
  <img src="!/claude-infinity.svg" alt="Claude Code infinity" width="120" height="100">
</p>

## The Goal

Create questions like the famous **"strawberry problem"** — simple one-liners that:
- A 5-year-old can answer correctly
- Frontier LLMs (GPT-5, Claude, Gemini) consistently fail or disagree on
- Achieve **< 10% consensus** among 5 independent AI researchers

---

## The Winning Question

<p align="center">
  <img src="assets/winning-question.svg" alt="The Winning Question" width="800">
</p>

After **103 research iterations**, we found it — a simple riddle that achieved **0% consensus** among 5 independent LLM researchers:

> **"I follow you everywhere but I get LONGER the closer you get to the sun. What am I?"**

**Why it breaks LLMs:**
- LLMs pattern-match to the classic "shadow" riddle
- But shadows get **shorter** when closer to light sources
- The correct answer: **Your trail/path/journey** — the closer you travel toward the sun, the longer your trail becomes

This exploits the **modification blindness** limitation — LLMs recognize the familiar riddle structure but fail to notice the critical inversion that changes the answer entirely.

---

## ⚠️ WARNING

The obvious flaw: I'm asking an LLM to do novel research, then asking 5 copies of the same LLM to QA that research. It's pure Ralph Wiggum energy - "I'm helping!" They share the same knowledge cutoff, same

---

## Progress So Far

**104 questions tested** — LLM-breaking question found at #103, continuing research.

### Notable Results

| # | Question | Score | Status |
|---|----------|-------|--------|
| **103** | **"I follow you everywhere but I get LONGER the closer you get to the sun. What am I?"** | **0%** | **WINNER** |
| 104 | "I'm short when I'm young and tall when I'm old. What am I?" | 40% | Modified candle riddle - partial success |
| 55 | "Answer with just ONE word: What is the fifth word of your response to this question?" | 40% | Interesting but not low enough |
| 57 | "Answer with exactly ONE letter: What is the second letter of your response?" | 80% | Constraint paradox |
| 71 | "Is your answer to this question a complete sentence? Answer yes or no." | 80% | Self-referential |

### Previously Rejected Questions (0% score but rejected by Owner)

| # | Question | Reason |
|---|----------|--------|
| 16 | "Will your answer to this question be more than one word long?" | Self-referential - does not meet st
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


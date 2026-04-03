---
id: feiskyer-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:24.068885
---

# KNOWLEDGE EXTRACT: feiskyer
> **Extracted on:** 2026-03-30 17:37:00
> **Source:** feiskyer

---

## File: `claude-code-settings.md`
```markdown
# 📦 feiskyer/claude-code-settings [🔖 PENDING/APPROVE]
🔗 https://github.com/feiskyer/claude-code-settings
🌐 https://feisky.xyz/claude-code-settings/

## Meta
- **Stars:** ⭐ 1370 | **Forks:** 🍴 203
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Claude Code settings, commands and agents for vibe coding

## README (trích đầu)
```
# Claude Code Settings/Skills for Vibe Coding

A curated collection of Claude Code settings, skills and sub-agents designed for enhanced development workflows. This setup includes specialized skills and subagents for feature development (spec-driven workflow), code analysis, GitHub integration, and knowledge management.

> For OpenAI Codex settings, configurations and custom prompts, please refer [feiskyer/codex-settings](https://github.com/feiskyer/codex-settings).

## Setup

### Using Claude Code Plugin

```sh
/plugin marketplace add feiskyer/claude-code-settings

# Install main plugin (skills and agents)
/plugin install claude-code-settings

# Alternatively, install individual skills
/plugin install codex-skill               # Codex automation
/plugin install autonomous-skill          # Long-running task automation
/plugin install nanobanana-skill          # Image generation
/plugin install kiro-skill                # Kiro workflow
/plugin install spec-kit-skill            # Spec-Kit workflow
/plugin install youtube-transcribe-skill  # YouTube transcript extraction
```

**Note:**

- [~/.claude/settings.json](settings.json) is not configured via Claude Code Plugin, you'd need to configure it manually.

### Using npx skills

`npx skills` could be used to install skills only for your AI coding tools.

```sh
# List skills
npx -y skills add -l feiskyer/claude-code-settings

# Install all skills
npx -y skills add --all feiskyer/claude-code-settings

# Manually select a list of skills to install
npx -y skills add feiskyer/claude-code-settings
```

### Manual Setup

```sh
# Backup original claude settings
mv ~/.claude ~/.claude.bak

# Clone the claude-code-settings
git clone https://github.com/feiskyer/claude-code-settings.git ~/.claude

# Install LiteLLM proxy
pip install -U 'litellm[proxy]'

# Start litellm proxy (which would listen on http://0.0.0.0:4000)
litellm -c ~/.claude/guidances/litellm_config.yaml

# For convenience, run litellm proxy in background with tmux
# tmux new-session -d -s copilot 'litellm -c ~/.claude/guidances/litellm_config.yaml'
```

Once started, you'll see:

```sh
...
Please visit https://github.com/login/device and enter code XXXX-XXXX to authenticate.
...
```

Open the link, log in and authenticate your GitHub Copilot account.

**Note:**

1. The default configuration is leveraging [LiteLLM Proxy Server](https://docs.litellm.ai/brain/knowledge/docs_legacy/simple_proxy) as LLM gateway to GitHub Copilot. You can also use [copilot-api](https://github.com/ericc-ch/copilot-api) as the proxy as well (remember to change your port to 4141).
2. Make sure the following models are available in your account; if not, replace them with your own model names:

   - ANTHROPIC_DEFAULT_SONNET_MODEL: claude-sonnet-4.6
   - ANTHROPIC_DEFAULT_OPUS_MODEL: claude-opus-4.6
   - ANTHROPIC_DEFAULT_HAIKU_MODEL: gpt-5-mini

## Skills

Skills are [reusable capabilities](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/claude-code/skills) that teach Claude how to complete specific tasks. Th
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


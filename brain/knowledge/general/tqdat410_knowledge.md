---
id: tqdat410-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.782298
---

# KNOWLEDGE EXTRACT: tqdat410
> **Extracted on:** 2026-03-30 17:54:19
> **Source:** tqdat410

---

## File: `agentune.md`
```markdown
# 📦 tqdat410/agentune [🔖 PENDING/APPROVE]
🔗 https://github.com/tqdat410/agentune


## Meta
- **Stars:** ⭐ 2 | **Forks:** 🍴 2
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Music Player for Agent

## README (trích đầu)
```
# agentune

**Music Player for Agent.**

agentune is a local MCP music player for Claude Code, Codex, OpenCode, and other MCP-compatible coding agents. Your agent can discover tracks, play instantly, queue the next song, and keep one shared listening session running while you work.

> CLI-only package: install and run `agentune` as a command. Programmatic `import "agentune"` is not a supported interface.

## Why agentune

- **Zero-auth setup**: no Spotify login, no Apple Music login, no API keys
- **Background play**: audio runs through `mpv`, not a browser tab
- **Auto start**: the daemon can start itself when your agent connects
- **Shared session**: queue, history, taste state, and dashboard stay in one local daemon
- **Browser dashboard**: live now-playing, queue, volume, taste, and listening insights
- **Cross-platform**: works on Windows, macOS, and Linux

## Prerequisites

- Node.js 20+
- `mpv`
- `yt-dlp`

Use `agentune doctor` after install to verify the runtime sees the required dependencies, the bundled `yt-dlp` binary, the system `yt-dlp` command, and the current daemon state.

### macOS

```bash
brew install mpv yt-dlp
```

### Ubuntu / Debian

```bash
sudo apt-get install mpv python3-pip
pip install yt-dlp
```

### Windows

```bash
scoop install mpv yt-dlp
```

## Quick Start

### 1. Install agentune

```bash
npm install -g agentune
agentune --version
agentune doctor
```

### 2. Connect your MCP client

Here are ready-to-use examples for common coding agents. Other MCP-compatible clients can point to the same local `agentune` command.

#### Claude Code

```bash
claude mcp add agentune --scope user -- agentune
```

#### Codex

```bash
codex mcp add agentune -- agentune
```

#### OpenCode

Add this to `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "agentune": {
      "type": "local",
      "command": ["agentune"],
      "enabled": true
    }
  }
}
```

### 3. Start your coding session

Your MCP client launches `agentune` automatically. The dashboard is available at `http://localhost:3737` after the first connection.

Useful daemon commands:

```bash
agentune --help
agentune doctor
agentune start
agentune stop
```

Use `agentune doctor` to confirm Node.js, `mpv`, bundled `yt-dlp`, system `yt-dlp`, config paths, and daemon health before you start playback.

Use `agentune start` when you want the background daemon running before your agent connects, or when `autoStartDaemon` is disabled.

### 4. Send your first prompts

```text
play some musics. id like Vietnamese song only, V-Pop, Indie, RAP, Ballad.
```

Use that first prompt to define your taste/persona in plain language. The agent can save that preference and reuse it later.

After that, a simple prompt is enough:

```text
Play some musics
```

The agent should read your saved taste, recent listening history, top artists, and top keywords, then choose music that fits instead of starting from zero each time.

If you want to change taste later
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


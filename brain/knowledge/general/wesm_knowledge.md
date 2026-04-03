---
id: wesm-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:46.197028
---

# KNOWLEDGE EXTRACT: wesm
> **Extracted on:** 2026-03-30 18:01:17
> **Source:** wesm

---

## File: `agentsview.md`
```markdown
# 📦 wesm/agentsview [🔖 PENDING/APPROVE]
🔗 https://github.com/wesm/agentsview
🌐 https://agentsview.io

## Meta
- **Stars:** ⭐ 588 | **Forks:** 🍴 75
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A local-first desktop and web application for browsing, searching, and analyzing AI agent coding sessions. Supports Claude Code, Codex, Gemini, OpenCode, Copilot and many other agents.

## README (trích đầu)
```
# agentsview

A local-first desktop and web application for browsing, searching,
and analyzing AI agent coding sessions. Supports Claude Code, Codex,
OpenCode, and 9 other agents.

<p align="center">
  <img src="https://agentsview.io/screenshots/dashboard.png" alt="Analytics dashboard" width="720">
</p>

## Desktop App

Download the desktop installer for macOS or Windows from
[GitHub Releases](https://github.com/wesm/agentsview/releases).
The desktop app includes auto-updates and runs the server as a
local sidecar -- no terminal required.

## CLI Install

```bash
curl -fsSL https://agentsview.io/install.sh | bash
```

**Windows:**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://agentsview.io/install.ps1 | iex"
```

The CLI installer downloads the latest release, verifies the
SHA-256 checksum, and installs the binary.

**Build from source** (requires Go 1.25+ with CGO and Node.js 22+):

```bash
git clone https://github.com/wesm/agentsview.git
cd agentsview
make build
make install  # installs to ~/.local/bin
```

## Why?

AI coding agents generate large volumes of session data across
projects. agentsview indexes these sessions into a local SQLite
database with full-text search, providing a web interface to
find past conversations, review agent behavior, and track usage
patterns over time.

## Features

- **Full-text search** across all message content, instantly
- **Analytics dashboard** with activity heatmaps, tool usage,
  velocity metrics, and project breakdowns
- **Multi-agent support** for Claude Code, Codex, OpenCode, and
  9 other agents ([full list](#supported-agents))
- **Live updates** via SSE as active sessions receive new messages
- **Keyboard-first** navigation (vim-style `j`/`k`/`[`/`]`)
- **Export and publish** sessions as HTML or to GitHub Gist
- **Local-first** -- all data stays on your machine, single binary,
  no accounts

## Usage

```bash
agentsview              # start server
agentsview -port 9090   # custom port
```

On startup, agentsview discovers sessions from all supported
agents, syncs them into a local SQLite database with FTS5
full-text search, and opens a web UI at `http://127.0.0.1:8080`.

For hostname or reverse-proxy access, set a `public_url`. This
preserves the default DNS-rebinding and CSRF protections while
explicitly trusting the external browser origin you expect.

```bash
# Direct HTTP on a custom hostname/port
agentsview -host 0.0.0.0 -port 8004 \
  -public-url http://viewer.example.test:8004

# HTTPS behind your own reverse proxy
agentsview -host 127.0.0.1 -port 8004 \
  -public-url https://viewer.example.test
```

agentsview can also manage a Caddy frontend for you. In managed-Caddy
mode, keep the backend on loopback and let Caddy terminate TLS and
optionally restrict client IP ranges. By default, managed Caddy binds
to `127.0.0.1` and exposes the public URL on port `8443`. To expose it
on a non-loopback interface, set `-proxy-bind-host` explicitly and
provide at least one `-allowed-subn
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


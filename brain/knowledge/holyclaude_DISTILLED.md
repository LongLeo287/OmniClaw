---
id: HolyClaude
type: knowledge
owner: OA_Triage
---
# HolyClaude
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# <img src="https://github.com/CoderLuii/HolyClaude/blob/master/assets/logo.png?raw=true" alt="HolyClaude" width="39" valign="bottom"> <a name="top"></a>HolyClaude

<div align="center">
  <img src="https://github.com/CoderLuii/HolyClaude/blob/master/assets/hero.png?raw=true" alt="HolyClaude Banner" width="100%" />
</div>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docker Pulls](https://badgen.net/docker/pulls/coderluii/holyclaude?icon=docker)](https://hub.docker.com/r/coderluii/holyclaude)
[![Full Image](https://img.shields.io/docker/image-size/coderluii/holyclaude/latest?label=full&color=blue&logo=docker)](https://hub.docker.com/r/coderluii/holyclaude)
[![Slim Image](https://img.shields.io/docker/image-size/coderluii/holyclaude/slim?label=slim&color=green&logo=docker)](https://hub.docker.com/r/coderluii/holyclaude)
<br>
[![GitHub Stars](https://img.shields.io/github/stars/CoderLuii/HolyClaude?style=social)](https://github.com/CoderLuii/HolyClaude)
[![Twitter Follow](https://img.shields.io/twitter/follow/CoderLuii?style=social)](https://x.com/CoderLuii)
[![PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://www.paypal.com/donate/?hosted_button_id=PM2UXGVSTHDNL)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support-yellow.svg?style=flat&logo=buy-me-a-coffee)](https://buymeacoffee.com/CoderLuii)
[![Website](https://img.shields.io/badge/website-coderluii.dev-orange?logo=astro)](https://coderluii.dev)
[![GitHub Release](https://img.shields.io/github/v/release/CoderLuii/HolyClaude?color=369eff&labelColor=black&logo=github&style=flat-square)](https://github.com/CoderLuii/HolyClaude/releases)
[![Issues](https://img.shields.io/github/issues/CoderLuii/HolyClaude?color=ff80eb&labelColor=black&style=flat-square)](https://github.com/CoderLuii/HolyClaude/issues)
[![Contributors](https://img.shields.io/github/contributors/CoderLuii/HolyClaude?color=c4f042&labelColor=black&style=flat-square)](https://github.com/CoderLuii/HolyClaude/graphs/contributors)

### Stop configuring. Start building.

One command. Full AI development workstation. Claude Code, web UI, headless browser, 5 AI CLIs, 50+ dev tools — containerized and ready.

**You were going to spend 2 hours setting this up manually. Or you could just `docker compose up`.**

**Works with your existing Claude Code subscription.** Max/Pro plan, API key — whatever you have, it just works.

---

## What is this?

You know the drill. You want Claude Code. But you also want it in a browser. With a headless browser for screenshots and testing. With Playwright configured. With every AI CLI. With TypeScript, Python, deployment tools, database clients, GitHub CLI.

So you start installing things. One by one. Then Chromium won't launch because Docker's shared memory is 64MB. Then Xvfb isn't configured. Then the UID inside the container doesn't match your host and everything is permission denied. Then you realize Claude Code's installer hangs when WORKDIR is root-owned. Then SQLite locks on your NAS mount. Then—

**HolyClaude is the container I built after solving every single one of those problems.**

I've been running this daily on my own server for weeks. Every bug has been hit, diagnosed, and fixed. Every edge case has been handled. Every "why doesn't this work in Docker" has been answered.

You pull it. You run it. You open your browser. You build.

### :credit_card: Use Your Existing Subscription

**This runs the real Claude Code CLI.** Not a wrapper. Not a proxy. Not a knock-off.

Your existing Anthropic account works directly:
- **Claude Max/Pro plan** — authenticate through the web UI (OAuth), same as desktop Claude Code
- **Anthropic API key** — set it through the web UI, same billing as always
- **No extra cost** — HolyClaude is free and open source. You only pay Anthropic for what you use, like you already do.

> HolyClaude doesn't touch your credentials. They're stored locally in your bind-mounted volume (`./data/claude/`), same as they would be on bare metal.

<p align="right">
  <a href="#top">↑ back to top</a>
</p>

---

## Table of Contents

| | Section |
|---|---|
| :zap: | [Quick Start](#zap-quick-start) |
| :computer: | [Platform Support](#computer-platform-support) |
| :star2: | [Why HolyClaude](#star2-why-holyclaude) |
| :credit_card: | [Subscription & Authentication](#credit_card-subscription--authentication) |
| :package: | [Image Variants](#package-image-variants) |
| :whale: | [Docker Compose — Quick](#whale-docker-compose--quick) |
| :whale2: | [Docker Compose — Full](#whale2-docker-compose--full) |
| :wrench: | [Environment Variables](#wrench-environment-variables) |
| :rocket: | [What's Inside](#rocket-whats-inside) |
| :robot: | [AI CLI Providers](#robot-ai-cli-providers) |
| :building_construction: | [Architecture](#building_construction-architecture) |
| :file_folder: | [Project Structure](#file_folder-project-structure) |
| :floppy_disk: | [Data & Persistence](#floppy_disk-data--persistence) |
| :lock: | [Permissions](#lock-permissions) |
| :bell: | [Notifications](#bell-notifications) |
| :arrows_counterclockwise: | [Upgrading](#arrows_counterclockwise-upgrading) |
| :construction: | [Troubleshooting](#construction-troubleshooting) |
| :warning: | [Known Issues](#warning-known-issues) |
| :hammer_and_wrench: | [Building Locally](#hammer_and_wrench-building-locally) |
| :bar_chart: | [Alternatives](#bar_chart-alternatives) |
| :rocket: | [Roadmap](#rocket-roadmap) |
| :trophy: | [Built with HolyClaude](#trophy-built-with-holyclaude) |
| :handshake: | [Contributing](#handshake-contributing) |
| :heart: | [Support](#heart-support) |
| :page_facing_up: | [License](#page_facing_up-license) |

<p align="right">
  <a href="#top">↑ back to top</a>
</p>

---

## :zap: Quick Start

**1.** Create a folder for HolyClaude:

```bash
mkdir holyclaude && cd holyclaude
```

**2.** Create a `docker-compose.yaml` file. Copy one of the templates below:
- [Quick template](#whale-docker-compose--quick) — minimal, zero config, just works
- [Full template](#whale2-docker-compose--full) — all options, fully documented

**3.** Pull and start:

```bash
docker compose up -d
```

**4.** Open the web UI:

```
http://localhost:3001
```

**5.** Create a CloudCLI account (takes 10 seconds), sign in with your Anthropic account, and you're live.

> No `.env` files. No pre-configuration. No reading 40 pages of docs before you can start. It just runs.

<p align="right">
  <a href="#top">↑ back to top</a>
</p>

---

## :computer: Platform Support

| Platform | Status | Notes |
|----------|--------|-------|
| Linux (amd64) | ✅ Fully supported | Native performance, recommended |
| Linux (arm64) | ✅ Fully supported | Raspberry Pi 4+, Oracle Cloud, AWS Graviton |
| macOS (Docker Desktop) | ✅ Fully supported | Apple Silicon & Intel via Docker Desktop |
| Windows (WSL2 + Docker Desktop) | ✅ Fully supported | Requires WSL2 backend |
| Synology / QNAP NAS | ✅ Fully supported | Use `CHOKIDAR_USEPOLLING=true` for SMB mounts |
| Kubernetes | 🔜 Coming soon | Helm chart planned |

<p align="right">
  <a href="#top">↑ back to top</a>
</p>

---

## :star2: Why HolyClaude

I built this because I was tired of re-doing the same setup every time. Installing Claude Code, wiring up a web UI, configuring Chromium in Docker, fixing permission issues, debugging process supervision. Every time.

So I made a container that does all of it. And then I hit every possible bug so you don't have to.

| | HolyClaude | Doing it yourself |
|---|---|---|
| **Setup** | 30 seconds | 1-2 hours (if it goes well) |
| **Claude Code** | Pre-installed, pre-configured, ready | Install, configure, debug installer hanging, fix WORKDIR |
| **Web UI** | CloudCLI included with plugins | Find a web UI, install it, configure it, wire it to Claude |
| **Headless browser** | Chromium + Xvfb + Playwright, configured | Install Chromium, install Xvfb, configure display :99, fix shm, fix sandbox, fix seccomp... |
| **AI CLIs** | 5 providers, one container | Install each one separately across 3 package managers |
| **Dev tools** | 50+ tools, ready | `apt-get install` / `npm i -g` / `pip install` for the next hour |
| **Process management** | s6-overlay (auto-restart, graceful shutdown) | Write your own supervisord config or hope Docker restart works |
| **Persistence** | Bind mounts, credentials survive everything | Figure out Docker volumes, debug "why is this a directory not a file" |
| **Updates** | `docker pull && docker compose up -d` | Update 50 tools manually, pray nothing breaks |
| **Multi-arch** | AMD64 + ARM64 | Pray your Dockerfile builds on ARM |

**The last row of every manual setup is "works on my machine."** HolyClaude works on every machine.

<p align="right">
  <a href="#top">↑ back to top</a>
</p>

---

## :credit_card: Subscription & Authentication

HolyClaude runs the **official Claude Code CLI** from Anthropic. Your existing account works out of the box.

### What works:

| Authentication method | How | Cost |
|----------------------|-----|------|
| **Claude Max/Pro plan** (subscription) | Sign in through CloudCLI web UI — same OAuth flow as desktop | Your existing subscription, no extra charge |
| **Anthropic API key** | Paste your API key in the web UI | Pay-per-use, same Anthropic billing |

### What doesn't work:

| | Why |
|---|---|
| ChatGPT Plus/Pro subscription | That's for chat.openai.com only — doesn't provide API access |
| OpenAI API key for Claude | Different company, different API. OpenAI keys work with the **Codex CLI** (also pre-installed) |

### Other AI CLIs included:

| CLI | What you need |
|-----|--------------|
| Gemini CLI | Google AI API key (`GEMINI_API_KEY`) |
| OpenAI Codex | OpenAI API key (`OPENAI_API_KEY`) — separate from ChatGPT subscription |
| Cursor | Cursor API key (`CURSOR_API_KEY`) |
| TaskMaster AI | Uses your AI provider keys (Anthropic, OpenAI, etc.) |

> **HolyClaude is free and open source.** You only pay your AI providers for usage, same as you already do. We don't proxy, intercept, or touch your credentials. They live in your local bind mount.

<p align="right">
  <a href="#top">↑ back to top</a>
</p>

---

## :package: Image Variants

Two flavors. Same quality. Pick your weight class.

| Tag | What you get | Best for |
|-----|-------------|----------|
| **`latest`** | Everything pre-installed — every tool, every library, every CLI | Most users. Zero wait time. Claude never has to stop and install something. |
| **`slim`** | Core tools only — Claude installs extras on-demand | Smaller VPS, limited disk, metered bandwidth |
| `X.Y.Z` | Full image, pinned version | Production stability — you control when to update |
| `X.Y.Z-slim` | Slim image, pinned version | Production + small footprint |

```bash
# Full — batteries included (recommended)
docker pull coderluii/holyclaude

# Slim — lean and mean
docker pull coderluii/holyclaude:slim
```

> **`latest` is always the full image.** Slim users: don't worry — when you ask Claude to do something that needs a missing tool, it installs it in seconds. You get the same capabilities, just with a smaller initial download.

<p align="right">
  <a href="#top">↑ back to top</a>
</p>

---

## :whale: Docker Compose — Quick

The "I just want it running" template. Copy this entire block into a `docker-compose.yaml` file:

```yaml
# ==============================================================================
# HolyClaude — Quick Start
# Just run: docker compose up -d
# Then open: http://localhost:3001
# ==============================================================================

services:
  holyclaude:
    image: coderluii/holyclaude:latest     # Full image (use :slim for smaller download)
    container_name: holyclaude
    hostname: holyclaude
    restart: unless-stopped
    shm_size: 2g                           # Chromium needs this — don't remove
    network_mode: bridge
    cap_add:
      - SYS_ADMIN                          # Required: Chromium sandboxing
      - SYS_PTRACE                         # Required: debugging tools
    security_opt:
      - seccomp=unconfined                 # Required: Chromium in Docker
    ports:
      - "3001:3001"                        # CloudCLI web UI
    volumes:
      #
      # ./data/claude — Your settings, credentials, API keys, and Claude's memory.
      #                  This is what survives container rebuilds.
      #                  NEVER delete this folder — your auth lives here.
      #
      - ./data/claude:/home/claude/.claude
      #
      # ./workspace — Your code. All projects go here.
      #               Bind-mounted so you can access files from your host.
      #
      - ./workspace:/workspace
    environment:
      - TZ=UTC                             # Your timezone (e.g., America/New_York, Europe/London)
```

Then:

```bash
docker compose up -d
```

Open `http://localhost:3001`. Create a CloudCLI account. Sign in with your Anthropic account. Build something.

**That's the whole setup. You're done.**

> **Why `SYS_ADMIN` + `seccomp=unconfined`?** Chromium needs these to run inside Docker — it's standard for any containerized browser (Playwright docs, Puppeteer docs, every CI pipeline that runs browser tests). Without them, Chromium crashes on startup. This is not a security risk unique to HolyClaude.

> **Why `shm_size: 2g`?** Docker gives containers 64MB of shared memory by default. Chromium uses `/dev/shm` heavily for tab rendering. At 64MB, tabs crash randomly. 2GB is the recommended minimum for any Chromium-in-Docker setup.

<p align="right">
  <a href="#top">↑ back to top</a>
</p>

---

## :whale2: Docker Compose — Full

Same image, every knob exposed. Copy this entire block into a `docker-compose.yaml` file:

```yaml
# ==============================================================================
# HolyClaude — Full Configuration
# All options documented inline.
# Detailed docs: https://github.com/CoderLuii/HolyClaude/blob/main/docs/configuration.md
# ==============================================================================

services:
  holyclaude:
    image: coderluii/holyclaude:latest     # Full image (use :slim for smaller download)
    container_name: holyclaude
    hostname: holyclaude
    restart: unless-stopped
    shm_size: 2g                           # Chromium shared memory — increase to 4g for heavy browser use
    network_mode: bridge
    cap_add:
      - SYS_ADMIN                          # Required: Chromium sandboxing
      - SYS_PTRACE                         # Required: debugging tools (strace, lsof)
    security_opt:
      - seccomp=unconfined                 # Required: Chromium syscall requirements
    ports:
      #
      # CloudCLI web UI — this is the only port you need.
      #
      - "3001:3001"
      #
      # Dev server ports — uncomment as needed.
      # These let you access dev servers running inside the container from your host bro
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Code of Conduct

## Our Pledge

We are committed to making participation in this project a welcoming experience for everyone, regardless of background or identity.

## Our Standards

**Positive behavior:**
- Being respectful and inclusive
- Giving and accepting constructive feedback
- Focusing on what's best for the community

**Unacceptable behavior:**
- Harassment, trolling, or personal attacks
- Publishing others' private information
- Any conduct inappropriate for a professional setting

## Enforcement

Instances of unacceptable behavior may be reported via [GitHub Security Advisories](https://github.com/CoderLuii/HolyClaude/security/advisories/new). All complaints will be reviewed and investigated.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/), version 2.1.

```

### File: CONTRIBUTING.md
```md
# Contributing to HolyClaude

Contributions welcome. Here's how.

## Process

1. Fork it
2. Branch it (`git checkout -b feature/something`)
3. Commit it (clear messages, no AI attribution)
4. Push it (`git push origin feature/something`)
5. PR it

## What to contribute

- Bug fixes (always welcome)
- New features (open an issue first to discuss)
- Documentation improvements
- Test coverage

## What NOT to do

- Don't open a PR without testing locally
- Don't include credentials or API keys
- Don't change the code style (follow existing patterns)

## Questions?

Open an issue or start a discussion. We're friendly.

```

### File: docker_compose.full.yaml
```yaml
# ==============================================================================
# HolyClaude — Full Configuration
# Usage: docker compose -f docker-compose.full.yaml up -d
# All options documented: https://github.com/CoderLuii/HolyClaude/blob/main/docs/configuration.md
# ==============================================================================

services:
  holyclaude:
    image: coderluii/holyclaude:latest
    container_name: holyclaude
    hostname: holyclaude
    restart: unless-stopped
    shm_size: 2g
    network_mode: bridge
    cap_add:
      - SYS_ADMIN
      - SYS_PTRACE
    security_opt:
      - seccomp=unconfined
    ports:
      - "3001:3001"           # CloudCLI web UI
      # --- Uncomment ports as needed ---
      # - "3000:3000"         # Dev server (Next.js, Express)
      # - "4321:4321"         # Astro dev
      # - "5173:5173"         # Vite dev
      # - "8787:8787"         # Wrangler dev
      # - "9229:9229"         # Node.js debugger
    volumes:
      - ./data/claude:/home/claude/.claude
      - ./workspace:/workspace
    environment:
      # --- Required ---
      - TZ=UTC                                    # Your timezone (e.g., America/New_York)

      # --- Performance ---
      - NODE_OPTIONS=--max-old-space-size=4096     # Node.js memory limit (MB)

      # --- User mapping (match your host UID/GID) ---
      - PUID=1000
      - PGID=1000

      # --- SMB/CIFS mounts (enable if workspace is on a network share) ---
      # - CHOKIDAR_USEPOLLING=1
      # - WATCHFILES_FORCE_POLLING=true

      # --- Notifications (uncomment services you want) ---
      # - NOTIFY_DISCORD=discord://webhook_id/webhook_token
      # - NOTIFY_TELEGRAM=tg://bot_token/chat_id
      # - NOTIFY_PUSHOVER=pover://user_key@app_token
      # - NOTIFY_SLACK=slack://token_a/token_b/token_c
      # - NOTIFY_EMAIL=mailto://user:pass@gmail.com?to=you@gmail.com
      # - NOTIFY_GOTIFY=gotify://hostname/token
      # - NOTIFY_URLS=                                   # catch-all: comma-separated Apprise URLs

      # --- AI provider API keys (optional — can also set via web UI) ---
      # - GEMINI_API_KEY=
      # - OPENAI_API_KEY=
      # - CURSOR_API_KEY=

```

### File: docker_compose.yaml
```yaml
# ==============================================================================
# HolyClaude — Quick Start
# Just run: docker compose up -d
# Then open: http://localhost:3001
# ==============================================================================

services:
  holyclaude:
    image: coderluii/holyclaude:latest
    container_name: holyclaude
    hostname: holyclaude
    restart: unless-stopped
    shm_size: 2g
    network_mode: bridge
    cap_add:
      - SYS_ADMIN      # Required for Chromium sandboxing
      - SYS_PTRACE      # Required for debugging
    security_opt:
      - seccomp=unconfined  # Required for Chromium in Docker
    ports:
      - "3001:3001"     # CloudCLI web UI
    volumes:
      - ./data/claude:/home/claude/.claude
      - ./workspace:/workspace
    environment:
      - TZ=UTC          # Change to your timezone

```

### File: .github\pull_request_template.md
```md
## What does this PR do?

<!-- Brief description of the change -->

## Type of change

- [ ] Bug fix
- [ ] New tool / package
- [ ] Feature / enhancement
- [ ] Documentation
- [ ] CI / build improvement
- [ ] Other

## Variant affected

- [ ] Full
- [ ] Slim
- [ ] Both
- [ ] N/A

## Checklist

- [ ] I've tested this locally with `docker compose up`
- [ ] Image still builds successfully
- [ ] No credentials or secrets are included
- [ ] CHANGELOG.md updated (if user-facing change)
- [ ] README.md updated (if adding/removing tools)

```

### File: .github\SECURITY.md
```md
# Security Policy

## Overview

HolyClaude runs AI coding agents inside a Docker container with elevated capabilities. This document explains the security model, what the container can access, and how to report vulnerabilities.

## Container Capabilities

HolyClaude requires the following Docker capabilities:

| Capability | Why | Risk |
|-----------|-----|------|
| `SYS_ADMIN` | Chromium sandboxing (Linux namespaces) | Standard for any Chromium-in-Docker setup |
| `SYS_PTRACE` | Debugging tools (strace, lsof) | Allows process inspection within the container |
| `seccomp=unconfined` | Chromium syscall requirements | Removes syscall filtering for the container |

These are required for Chromium to function and are standard across Playwright, Puppeteer, and CI/CD browser testing setups. They do **not** grant the container access to the host system beyond what Docker normally allows.

## Permission Modes

| Mode | Default? | What it means |
|------|----------|--------------|
| `allowEdits` | **Yes** | Claude can edit files freely, asks before running shell commands |
| `bypassPermissions` | No | Claude runs any command without confirmation |

The default `allowEdits` mode is safe for most users. `bypassPermissions` is documented for power users who understand the implications.

## Credential Storage

- API keys and authentication tokens are stored in `./data/claude/` on the host (bind-mounted to `~/.claude/` in the container)
- Credentials never leave the container — HolyClaude does not proxy, intercept, or transmit credentials to any third party
- The container communicates directly with AI provider APIs (Anthropic, Google, OpenAI) using your credentials

## Network Access

The container has unrestricted outbound network access. This is required for:
- AI provider API calls (Anthropic, Google, OpenAI)
- npm/pip package installations
- Git operations (clone, push, pull)
- Any web requests Claude Code makes during development tasks

## Reporting a Vulnerability

If you discover a security vulnerability in HolyClaude:

1. **Do not** open a public GitHub issue
2. Use [GitHub Security Advisories](https://github.com/CoderLuii/HolyClaude/security/advisories/new) to report privately
3. Include: description, steps to reproduce, and potential impact
4. You will receive a response within 48 hours

## Supported Versions

| Version | Supported |
|---------|-----------|
| latest | Yes |
| < 1.0.0 | No |

```

### File: config\claude_memory_full.md
```md
# HolyClaude Environment — Full Variant

You are running inside a **HolyClaude Docker container** (full variant). Everything is pre-installed and ready to use. This file is your global memory — customize it with your own preferences, projects, and context.

---

## Environment Overview

- **OS:** Debian Bookworm (slim) inside Docker
- **User:** `claude` (UID/GID configurable via PUID/PGID)
- **Working directory:** `/workspace` (bind-mounted from host)
- **Home directory:** `/home/claude`
- **Persistent storage:** `~/.claude/` is bind-mounted — settings, credentials, and this file survive container rebuilds
- **Process manager:** s6-overlay v3 (PID 1) — manages all long-running services
- **Display:** Xvfb virtual display at `:99` for headless browser operations

## Running Services

| Service | What it does | Port |
|---------|-------------|------|
| **CloudCLI** | Web UI for Claude Code | `3001` |
| **Xvfb** | Virtual display for headless Chromium | `:99` (internal) |

Both managed by s6-overlay — they auto-restart on failure.

## Node.js & npm (v22 LTS)

### Global packages available:
- **Languages:** typescript, tsx
- **Package managers:** pnpm, npm (built-in)
- **Build tools:** vite, esbuild
- **Code quality:** eslint, prettier
- **Dev servers:** serve, nodemon, http-server
- **Utilities:** concurrently, dotenv-cli
- **Deployment:** wrangler (Cloudflare), vercel, netlify-cli, @cloudflare/next-on-pages
- **Databases:** prisma, drizzle-kit
- **Process management:** pm2
- **Mobile:** eas-cli (Expo)
- **Performance:** lighthouse, @lhci/cli
- **Media:** sharp-cli, @marp-team/marp-cli
- **Mock APIs:** json-server

### Installing additional packages:
```bash
npm i -g <package>        # Global install
npm i <package>           # Project-local install
```

## Python 3

### Installed packages:
- **HTTP:** requests, httpx, httpie
- **Scraping:** beautifulsoup4, lxml
- **Images:** Pillow
- **Data:** pandas, numpy, matplotlib, seaborn
- **PDF:** reportlab, weasyprint, cairosvg, fpdf2, PyMuPDF, pdfkit, img2pdf
- **Excel:** openpyxl, xlsxwriter, xlrd
- **Documents:** python-docx, python-pptx, markdown, jinja2
- **Config:** pyyaml, python-dotenv
- **CLI:** rich, click, tqdm
- **Browser:** playwright
- **Web framework:** fastapi, uvicorn

### Installing additional packages:
```bash
pip install --break-system-packages <package>
```
The `--break-system-packages` flag is required (no venv in container context).

## AI CLI Providers

| CLI | Command | Notes |
|-----|---------|-------|
| **Claude Code** | `claude` | Primary — you are running inside this |
| **Gemini CLI** | `gemini` | Requires `GEMINI_API_KEY` env var |
| **OpenAI Codex** | `codex` | Requires `OPENAI_API_KEY` env var |
| **Cursor** | `cursor` | Requires `CURSOR_API_KEY` env var |
| **TaskMaster AI** | `task-master` | Task planning and management |

## System Tools

### Command-line utilities:
- **Search:** ripgrep (`rg`), fd (`fdfind`), fzf, grep
- **Files:** tree, bat (`batcat` or `bat`), jq, zip/unzip
- **Network:** curl, wget, httpie, openssh-client
- **Process:** htop, lsof, strace, iproute2 (`ip`, `ss`)
- **Terminal:** tmux
- **Version control:** git, gh (GitHub CLI)

### Database CLIs:
- **PostgreSQL:** `psql`
- **Redis:** `redis-cli`
- **SQLite:** `sqlite3`

### Media & document processing:
- **Images:** imagemagick (`convert`, `identify`, `mogrify`)
- **Video/Audio:** ffmpeg
- **Documents:** pandoc (convert between formats)
- **Image processing:** libvips (via `vips` command or sharp)

### Browser:
- **Chromium** at `/usr/bin/chromium` — headless by default
- **Playwright** installed — use for browser automation, screenshots, testing
- Xvfb provides a virtual display so Chromium has a screen to render to
- Flags preset: `--no-sandbox --disable-gpu --disable-dev-shm-usage`

## GitHub CLI (gh)

Pre-installed and ready. Authenticate with:
```bash
gh auth login
```

Common operations:
```bash
gh repo clone owner/repo
gh pr create --title "..." --body "..."
gh issue list
gh pr merge
```

## Notifications (Apprise)

Optional push notifications via [Apprise](https://github.com/caronc/apprise) — supports 100+ services (Discord, Telegram, Slack, Email, Pushover, Gotify, and more). Disabled by default.

**To enable:**
1. Set one or more `NOTIFY_*` environment variables (e.g. `NOTIFY_DISCORD`, `NOTIFY_TELEGRAM`, `NOTIFY_PUSHOVER`)
2. Create the flag file: `touch ~/.claude/notify-on`

**To disable:** `rm ~/.claude/notify-on`

**Events:**
- `stop` — Claude finishes a task
- `error` — A tool use failure occurs

## Workspace

- All projects go in `/workspace` (bind-mounted from host)
- Git is pre-configured with `safe.directory /workspace`
- Git identity is set via `GIT_USER_NAME` and `GIT_USER_EMAIL` env vars
- Create repos, clone projects, build — everything persists on the host

## Permissions

Claude Code runs in `allowEdits` mode by default:
- File edits: allowed without confirmation
- Shell commands: asks for confirmation
- To enable full bypass: change `allowEdits` to `bypassPermissions` in `~/.claude/settings.json`

## Container Lifecycle

- **First boot:** Bootstrap runs once — copies settings, memory, configures git
- **Subsequent boots:** Bootstrap skipped (sentinel file exists)
- **Re-trigger bootstrap:** Delete `~/.claude/.holyclaude-bootstrapped`
- **Credentials survive rebuilds:** `~/.claude/` is bind-mounted
- **CloudCLI account:** NOT persistent (SQLite can't live on network mounts) — re-create after rebuild (~10 seconds)

## Tips

- Use the **Web Terminal** plugin in CloudCLI instead of "Continue in Shell" (known CloudCLI bug)
- Chromium needs `shm_size: 2g` or higher in docker-compose to avoid crashes
- If on SMB/CIFS mounts, enable `CHOKIDAR_USEPOLLING=1` and `WATCHFILES_FORCE_POLLING=true`
- SQLite databases should NOT be stored on network mounts (file locking fails on CIFS)

---

## Your Preferences

Add your personal preferences below. This section persists across container rebuilds.

```
# Example:
# - Default stack: Astro, Tailwind, pnpm
# - Direct communication, no fluff
# - Always use TypeScript
```

```

### File: config\claude_memory_slim.md
```md
# HolyClaude Environment — Slim Variant

You are running inside a **HolyClaude Docker container** (slim variant). Core tools are pre-installed. Additional packages can be installed on-demand — see the "Not Pre-installed" sections below. This file is your global memory — customize it with your own preferences, projects, and context.

---

## Environment Overview

- **OS:** Debian Bookworm (slim) inside Docker
- **User:** `claude` (UID/GID configurable via PUID/PGID)
- **Working directory:** `/workspace` (bind-mounted from host)
- **Home directory:** `/home/claude`
- **Persistent storage:** `~/.claude/` is bind-mounted — settings, credentials, and this file survive container rebuilds
- **Process manager:** s6-overlay v3 (PID 1) — manages all long-running services
- **Display:** Xvfb virtual display at `:99` for headless browser operations
- **Variant:** SLIM — lighter image, install extras as needed

## Running Services

| Service | What it does | Port |
|---------|-------------|------|
| **CloudCLI** | Web UI for Claude Code | `3001` |
| **Xvfb** | Virtual display for headless Chromium | `:99` (internal) |

Both managed by s6-overlay — they auto-restart on failure.

## Node.js & npm (v22 LTS)

### Pre-installed global packages:
- **Languages:** typescript, tsx
- **Package managers:** pnpm, npm (built-in)
- **Build tools:** vite, esbuild
- **Code quality:** eslint, prettier
- **Dev servers:** serve, nodemon
- **Utilities:** concurrently, dotenv-cli

### NOT pre-installed (install when needed):
```bash
# Deployment CLIs
npm i -g wrangler                    # Cloudflare
npm i -g vercel                      # Vercel
npm i -g netlify-cli                 # Netlify
npm i -g @cloudflare/next-on-pages   # Next.js on Cloudflare

# Database ORMs
npm i -g prisma                      # Prisma ORM
npm i -g drizzle-kit                 # Drizzle ORM

# Other tools
npm i -g pm2                         # Process manager
npm i -g eas-cli                     # Expo/React Native
npm i -g lighthouse @lhci/cli        # Performance testing
npm i -g sharp-cli                   # Image processing
npm i -g json-server                 # Mock REST APIs
npm i -g http-server                 # Static file server
npm i -g @marp-team/marp-cli         # Markdown presentations
```
Install these with `npm i -g <package>` — takes seconds.

## Python 3

### Pre-installed packages:
- **HTTP:** requests, httpx
- **Scraping:** beautifulsoup4, lxml
- **Images:** Pillow
- **Data:** pandas, numpy
- **Excel:** openpyxl
- **Documents:** python-docx, markdown, jinja2
- **Config:** pyyaml, python-dotenv
- **CLI:** rich, click, tqdm
- **Browser:** playwright

### NOT pre-installed (install when needed):
```bash
# PDF libraries (install the one you need, not all)
pip install --break-system-packages reportlab     # Generate PDFs
pip install --break-system-packages weasyprint     # HTML to PDF
pip install --break-system-packages fpdf2          # Simple PDF creation
pip install --break-system-packages PyMuPDF        # Read/manipulate PDFs
pip install --break-system-packages pdfkit         # wkhtmltopdf wrapper
pip install --break-system-packages img2pdf        # Images to PDF

# Data visualization
pip install --break-system-packages matplotlib seaborn

# Excel (additional)
pip install --break-system-packages xlsxwriter xlrd

# Office documents
pip install --break-system-packages python-pptx    # PowerPoint

# Web framework
pip install --break-system-packages fastapi uvicorn

# HTTP client
pip install --break-system-packages httpie
```
The `--break-system-packages` flag is required (no venv in container context).

### System packages NOT pre-installed:
The slim variant does not include these apt packages. Install if needed:
```bash
sudo apt-get update && sudo apt-get install -y pandoc    # Document conversion
sudo apt-get install -y ffmpeg                            # Video/audio processing
sudo apt-get install -y libvips-dev                       # Image processing library
```
These take longer to install (~1-2 minutes) because they require system dependencies.

## AI CLI Providers

| CLI | Command | Notes |
|-----|---------|-------|
| **Claude Code** | `claude` | Primary — you are running inside this |
| **Gemini CLI** | `gemini` | Requires `GEMINI_API_KEY` env var |
| **OpenAI Codex** | `codex` | Requires `OPENAI_API_KEY` env var |
| **Cursor** | `cursor` | Requires `CURSOR_API_KEY` env var |
| **TaskMaster AI** | `task-master` | Task planning and management |

## System Tools

### Command-line utilities:
- **Search:** ripgrep (`rg`), fd (`fdfind`), fzf, grep
- **Files:** tree, bat (`batcat` or `bat`), jq, zip/unzip
- **Network:** curl, wget, openssh-client
- **Process:** htop, lsof, strace, iproute2 (`ip`, `ss`)
- **Terminal:** tmux
- **Version control:** git, gh (GitHub CLI)

### Database CLIs:
- **PostgreSQL:** `psql`
- **Redis:** `redis-cli`
- **SQLite:** `sqlite3`

### Media processing:
- **Images:** imagemagick (`convert`, `identify`, `mogrify`)
- **Video/Audio:** NOT installed — `sudo apt-get install -y ffmpeg` if needed
- **Documents:** NOT installed — `sudo apt-get install -y pandoc` if needed

### Browser:
- **Chromium** at `/usr/bin/chromium` — headless by default
- **Playwright** installed — use for browser automation, screenshots, testing
- Xvfb provides a virtual display so Chromium has a screen to render to
- Flags preset: `--no-sandbox --disable-gpu --disable-dev-shm-usage`

## GitHub CLI (gh)

Pre-installed and ready. Authenticate with:
```bash
gh auth login
```

Common operations:
```bash
gh repo clone owner/repo
gh pr create --title "..." --body "..."
gh issue list
gh pr merge
```

## Notifications (Apprise)

Optional push notifications via [Apprise](https://github.com/caronc/apprise) — supports 100+ services (Discord, Telegram, Slack, Email, Pushover, Gotify, and more). Disabled by default.

**To enable:**
1. Set one or more `NOTIFY_*` environment variables (e.g. `NOTIFY_DISCORD`, `NOTIFY_TELEGRAM`, `NOTIFY_PUSHOVER`)
2. Create the flag file: `touch ~/.claude/notify-on`

**To disable:** `rm ~/.claude/notify-on`

## Workspace

- All projects go in `/workspace` (bind-mounted from host)
- Git is pre-configured with `safe.directory /workspace`
- Git identity is set via `GIT_USER_NAME` and `GIT_USER_EMAIL` env vars
- Create repos, clone projects, build — everything persists on the host

## Permissions

Claude Code runs in `allowEdits` mode by default:
- File edits: allowed without confirmation
- Shell commands: asks for confirmation
- To enable full bypass: change `allowEdits` to `bypassPermissions` in `~/.claude/settings.json`

## Container Lifecycle

- **First boot:** Bootstrap runs once — copies settings, memory, configures git
- **Subsequent boots:** Bootstrap skipped (sentinel file exists)
- **Re-trigger bootstrap:** Delete `~/.claude/.holyclaude-bootstrapped`
- **Credentials survive rebuilds:** `~/.claude/` is bind-mounted
- **CloudCLI account:** NOT persistent (SQLite can't live on network mounts) — re-create after rebuild (~10 seconds)

## Tips

- Use the **Web Terminal** plugin in CloudCLI instead of "Continue in Shell" (known CloudCLI bug)
- Chromium needs `shm_size: 2g` or higher in docker-compose to avoid crashes
- If on SMB/CIFS mounts, enable `CHOKIDAR_USEPOLLING=1` and `WATCHFILES_FORCE_POLLING=true`
- SQLite databases should NOT be stored on network mounts (file locking fails on CIFS)
- **Slim variant:** When you need a tool that's not installed, just install it. npm/pip packages take seconds. apt packages take 1-2 minutes.

---

## Your Preferences

Add your personal preferences below. This section persists across container rebuilds.

```
# Example:
# - Default stack: Astro, Tailwind, pnpm
# - Direct communication, no fluff
# - Always use TypeScript
```

```

### File: config\settings.json
```json
{
  "permissions": {
    "defaultMode": "allowEdits"
  },
  "env": {
    "DISABLE_AUTOUPDATER": "1"
  },
  "model": "sonnet",
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/local/bin/notify.py stop"
          }
        ]
      }
    ],
    "PostToolUseFailure": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/local/bin/notify.py error"
          }
        ]
      }
    ]
  }
}

```

### File: docs\architecture.md
```md
# Architecture

Technical deep-dive into how HolyClaude works.

---

## Overview

HolyClaude is a single Docker container running multiple supervised services. The architecture is designed for reliability, persistence, and zero-configuration startup.

```
┌─────────────────────────────────────────────────┐
│                Docker Container                  │
│                                                  │
│  entrypoint.sh (runs once)                       │
│    ├── UID/GID remapping                         │
│    ├── Pre-create required files                 │
│    ├── bootstrap.sh (first boot only)            │
│    │     ├── Copy settings.json                  │
│    │     ├── Copy CLAUDE.md (memory)             │
│    │     ├── Configure git                       │
│    │     └── Create sentinel file                │
│    └── exec /init (s6-overlay)                   │
│                                                  │
│  s6-overlay (PID 1)                              │
│    ├── cloudcli (longrun)                        │
│    │     └── claude-code-ui --port 3001          │
│    └── xvfb (longrun)                            │
│          └── Xvfb :99 -screen 0 1920x1080x24    │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │ Claude   │  │ Chromium │  │ Dev Tools    │   │
│  │ Code CLI │  │ headless │  │ Node, Python │   │
│  └──────────┘  └──────────┘  └──────────────┘   │
│                                                  │
│  Bind Mounts:                                    │
│    ~/.claude ←→ ./data/claude (host)             │
│    /workspace ←→ ./workspace (host)              │
└─────────────────────────────────────────────────┘
```

---

## Component Details

### Entrypoint (`entrypoint.sh`)

Runs every time the container starts. Responsibilities:

1. **UID/GID remapping** — Adjusts the `claude` user's UID/GID to match `PUID`/`PGID` environment variables. This prevents permission mismatches between container and host files.

2. **File pre-creation** — Ensures `~/.claude.json` exists as a file (not a directory). Docker creates bind-mount targets as directories if they don't exist, which breaks Claude Code.

3. **Bootstrap trigger** — Checks for sentinel file `.holyclaude-bootstrapped`. If absent, runs `bootstrap.sh`.

4. **Handoff** — `exec /init` replaces the entrypoint process with s6-overlay, which becomes PID 1.

### Bootstrap (`bootstrap.sh`)

Runs once on first container start. Creates the sentinel file so it doesn't re-run. Responsibilities:

1. **Settings** — Copies `settings.json` from the image to `~/.claude/settings.json`
2. **Memory** — Copies the variant-appropriate memory template (`claude-memory-full.md` or `claude-memory-slim.md`) to `~/.claude/CLAUDE.md`
3. **Git** — Configures git identity from `GIT_USER_NAME`/`GIT_USER_EMAIL` env vars
4. **Onboarding** — Creates `~/.claude.json` with `hasCompletedOnboarding: true` to skip the first-run wizard
5. **Permissions** — Fixes file ownership to match `PUID`/`PGID`

### s6-overlay

[s6-overlay](https://github.com/just-containers/s6-overlay) is a process supervisor designed for Docker containers. It's used instead of supervisord or systemd because:

- **Proper PID 1 behavior** — Handles signal forwarding and zombie reaping
- **Service supervision** — Restarts crashed services automatically
- **Clean shutdown** — Graceful stop signals to all services
- **Small footprint** — Minimal overhead

#### Important: Clean environment

s6's `s6-setuidgid` runs services with a clean environment. Docker-compose environment variables are **not** automatically available to s6 services. Each service's `run` script must explicitly set needed variables in the `env` command. This is a security feature, not a bug.

### CloudCLI Service

```sh
#!/bin/sh
cd /workspace
exec s6-setuidgid claude env HOME=/home/claude NODE_OPTIONS=--no-deprecation WORKSPACES_ROOT=/workspace claude-code-ui --port 3001
```

- Runs as user `claude` (not root)
- Sets `WORKSPACES_ROOT` directly (can't rely on docker-compose env vars due to s6 clean environment)
- `NODE_OPTIONS=--no-deprecation` suppresses noisy deprecation warnings
- Managed as a `longrun` service — auto-restarts on crash

### Xvfb Service

```sh
#!/bin/sh
exec Xvfb :99 -screen 0 1920x1080x24 -nolisten tcp
```

- Provides a virtual display at `:99` (1920x1080, 24-bit color)
- Required for Chromium, Playwright, Lighthouse — they need a display even in headless mode
- `-nolisten tcp` prevents remote X connections (security)

---

## Design Decisions

### Why s6-overlay instead of supervisord?

s6-overlay is purpose-built for Docker. supervisord is a full process manager designed for bare-metal servers — it's heavier, requires XML configuration, and doesn't handle PID 1 responsibilities (signal forwarding, zombie reaping) out of the box.

### Why sentinel-based bootstrap instead of always running?

Bootstrap copies default settings and memory. Running it every time would overwrite user customizations. The sentinel pattern means:
- First boot: fresh defaults installed
- Subsequent boots: user's customizations preserved
- Manual re-trigger: delete sentinel file

### Why plugins baked into the image?

CloudCLI plugins require `git clone` + `npm install` + `npm run build`. Running this at container start (in bootstrap) is unreliable because:
- Bind mounts may be on network storage with permission issues
- Network may be unavailable at boot
- Adds 30+ seconds to every first boot

Baking them into the Dockerfile ensures a clean, controlled build environment.

### Why `runuser` instead of `su`?

`su` uses PAM authentication, which can fail with renamed users (the base image's `node` user renamed to `claude`). `runuser` skips PAM entirely — it's designed for scripts that need to run commands as another user.

### Why no `.env` file by default?

Every configuration option has a sensible default. Most users authenticate through the CloudCLI web UI, not environment variables. Requiring a `.env` file adds a setup step that most users don't need. Power users can use `docker-compose.full.yaml` which has all options documented inline.

### Why bind mounts instead of named volumes?

Bind mounts let users see and manage their data on disk. Named volumes hide data in Docker's internal storage, making backup and inspection harder. For a development workstation where users want to access their code and config files directly, bind mounts are the right choice.

---

## Image Variants

The `VARIANT` build arg controls which packages are installed:

```dockerfile
ARG VARIANT=full
```

The variant is stored at build time in `/etc/holyclaude-variant`. Bootstrap reads this file to copy the correct memory template.

| Variant | npm packages | pip packages | apt packages |
|---------|-------------|-------------|-------------|
| `full` | All | All | All |
| `slim` | Core only | Core only | No pandoc/ffmpeg/libvips |

See [What's Inside](../README.md#rocket-whats-inside) for the complete package lists.

---

## Multi-Architecture Support

The Dockerfile uses Docker's `TARGETARCH` build arg to download the correct s6-overlay binary:

```dockerfile
RUN S6_ARCH=$(case "$TARGETARCH" in arm64) echo "aarch64";; *) echo "x86_64";; esac)
```

Supported architectures:
- `amd64` (x86_64) — Intel/AMD servers, most VPS providers
- `arm64` (aarch64) — Apple Silicon, AWS Graviton, Raspberry Pi 4+

Build for a specific platform:
```bash
docker buildx build --platform linux/arm64 -t holyclaude .
```

```

### File: docs\CHANGELOG.md
```md
# Changelog

All notable changes to HolyClaude will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.1.0] - 03/25/2026

### Added
- Apprise notification engine with support for 100+ services (Discord, Telegram, Slack, Email, Gotify, and more)
- Individual `NOTIFY_*` environment variables for easy per-service configuration
- Catch-all `NOTIFY_URLS` for any Apprise-supported service

### Changed
- Notification backend replaced from Pushover to Apprise

### Removed
- **BREAKING:** `PUSHOVER_APP_TOKEN` and `PUSHOVER_USER_KEY` environment variables removed. Migrate to `NOTIFY_PUSHOVER=pover://user_key@app_token`. See [configuration docs](configuration.md#notifications-apprise) for details.

## [1.0.0] - 03/21/2026

Initial public release.

```

### File: docs\configuration.md
```md
# Configuration Guide

Complete reference for all HolyClaude configuration options.

---

## Docker Compose Files

HolyClaude ships with two compose files:

| File | Purpose | Usage |
|------|---------|-------|
| `docker-compose.yaml` | Quick start — minimal config, just works | `docker compose up -d` |
| `docker-compose.full.yaml` | All options — ports, API keys, polling, notifications | `docker compose -f docker-compose.full.yaml up -d` |

---

## Environment Variables

### Core

| Variable | Default | Description |
|----------|---------|-------------|
| `TZ` | `UTC` | Container timezone ([list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)) |
| `PUID` | `1000` | User ID — match your host user's UID (`id -u`) |
| `PGID` | `1000` | Group ID — match your host user's GID (`id -g`) |

### Performance

| Variable | Default | Description |
|----------|---------|-------------|
| `NODE_OPTIONS` | `--max-old-space-size=4096` | Node.js heap memory limit in MB |

### Git Identity

Set during first-boot bootstrap. To change after first boot, run `git config --global` inside the container.

| Variable | Default | Description |
|----------|---------|-------------|
| `GIT_USER_NAME` | `HolyClaude User` | Git commit author name |
| `GIT_USER_EMAIL` | `noreply@holyclaude.local` | Git commit author email |

### SMB/CIFS Network Mounts

Only needed if your volumes are on a network share (Samba, NAS, etc.):

| Variable | Default | Description |
|----------|---------|-------------|
| `CHOKIDAR_USEPOLLING` | (unset) | Set to `1` — enables polling for file watchers |
| `WATCHFILES_FORCE_POLLING` | (unset) | Set to `true` — enables polling for Python watchers |

### Notifications (Apprise)

HolyClaude uses [Apprise](https://github.com/caronc/apprise) for notifications, supporting 100+ services including Discord, Telegram, Slack, Email, Pushover, Gotify, and more.

| Variable | Default | Description |
|----------|---------|-------------|
| `NOTIFY_DISCORD` | *(unset)* | Discord webhook — `discord://webhook_id/webhook_token` |
| `NOTIFY_TELEGRAM` | *(unset)* | Telegram bot — `tg://bot_token/chat_id` |
| `NOTIFY_PUSHOVER` | *(unset)* | Pushover — `pover://user_key@app_token` |
| `NOTIFY_SLACK` | *(unset)* | Slack webhook — `slack://token_a/token_b/token_c` |
| `NOTIFY_EMAIL` | *(unset)* | Email (SMTP) — `mailto://user:pass@gmail.com?to=you@gmail.com` |
| `NOTIFY_GOTIFY` | *(unset)* | Gotify — `gotify://hostname/token` |
| `NOTIFY_URLS` | *(unset)* | Catch-all — comma-separated [Apprise URLs](https://github.com/caronc/apprise/wiki) |

Notifications also require the flag file `~/.claude/notify-on` to exist inside the container. Create it with `touch ~/.claude/notify-on`.

**Migrating from Pushover (v1.0.0):** Replace `PUSHOVER_APP_TOKEN` and `PUSHOVER_USER_KEY` with a single variable: `NOTIFY_PUSHOVER=pover://user_key@app_token`

### AI Provider API Keys

These can also be set through the CloudCLI web UI.

| Variable | Default | Description |
|----------|---------|-------------|
| `GEMINI_API_KEY` | (unset) | Google Gemini API key |
| `OPENAI_API_KEY` | (unset) | OpenAI API key |
| `CURSOR_API_KEY` | (unset) | Cursor API key |

---

## Volumes

| Host Path | Container Path | Purpose |
|-----------|---------------|---------|
| `./data/claude` | `/home/claude/.claude` | Settings, credentials, memory, API tokens |
| `./workspace` | `/workspace` | Your code and projects |

### What's inside `./data/claude`:

| File/Dir | Purpose |
|----------|---------|
| `settings.json` | Claude Code settings (permissions, hooks, model) |
| `CLAUDE.md` | Claude's global memory — customize with your preferences |
| `.credentials.json` | Anthropic API authentication (auto-created) |
| `.holyclaude-bootstrapped` | Sentinel file — delete to re-run first-boot setup |

---

## Ports

| Port | Service | Default State |
|------|---------|--------------|
| `3001` | CloudCLI web UI | Exposed |
| `3000` | Dev server (Next.js, Express) | Commented out |
| `4321` | Astro dev server | Commented out |
| `5173` | Vite dev server | Commented out |
| `8787` | Wrangler dev server | Commented out |
| `9229` | Node.js debugger | Commented out |

Uncomment additional ports in `docker-compose.full.yaml` as needed.

---

## Docker Capabilities

HolyClaude requires these Docker capabilities for Chromium to work:

```yaml
cap_add:
  - SYS_ADMIN      # Chromium sandboxing (namespaces)
  - SYS_PTRACE      # Debugging (strace, lsof)
security_opt:
  - seccomp=unconfined  # Chromium syscall requirements
```

These are standard for any Chromium-in-Docker setup. Without them, Chromium crashes on startup.

---

## Shared Memory

```yaml
shm_size: 2g
```

Chromium uses `/dev/shm` for shared memory. Docker defaults to 64MB, which causes tab crashes. 2GB is recommended for general use. Increase if running many concurrent browser tabs.

---

## Claude Code Settings

The default `settings.json` at `~/.claude/settings.json`:

```json
{
  "permissions": {
    "defaultMode": "allowEdits"
  },
  "env": {
    "DISABLE_AUTOUPDATER": "1"
  },
  "model": "sonnet"
}
```

### Permission Modes

| Mode | File edits | Shell commands | Use case |
|------|-----------|----------------|----------|
| `askUser` | Asks | Asks | Maximum safety |
| `allowEdits` | Allowed | Asks | **Default** — good balance |
| `bypassPermissions` | Allowed | Allowed | Power users only |

### Changing the Model

Edit `settings.json` and change `"model"`:
- `"sonnet"` — Claude Sonnet (default, fast)
- `"opus"` — Claude Opus (most capable)
- `"haiku"` — Claude Haiku (fastest, cheapest)

---

## Customizing Claude's Memory

Edit `~/.claude/CLAUDE.md` (or `./data/claude/CLAUDE.md` on the host) to customize Claude's behavior:

```markdown
# My Preferences
- Use TypeScript for all new files
- Default to pnpm, not npm
- Direct communication, no fluff
- Always run tests after changes
```

This file is read by Claude at the start of every conversation.

---

## Re-triggering First-Boot Setup

If you need to re-run the bootstrap (e.g., after updating the image):

```bash
# Delete the sentinel file — NOT the entire directory
rm ./data/claude/.holyclaude-bootstrapped

# Restart the container
docker compose restart holyclaude
```

**Warning:** Do NOT delete `./data/claude/` entirely — this wipes your credentials and you'll need to re-authenticate.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

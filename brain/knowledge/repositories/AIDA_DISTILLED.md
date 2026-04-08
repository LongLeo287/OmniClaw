---
id: repo-fetched-aida-102332
type: knowledge
owner: OA
registered_at: 2026-04-05T03:05:34.742768
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_AIDA_102332

## Assimilation Report
Auto-cloned repository: FETCHED_AIDA_102332

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <img src="./assets/banner1.png" alt="AIDA Banner" width="100%">
</p>
<h1 align="center">AI-Driven Security Assessment</h1>

<p align="center">
  <strong>Give your AI the power of 400+ pentesting tools. Let it hack (legally).</strong>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> •
  <a href="#why-aida-exists">Why AIDA</a> •
  <a href="Docs/INSTALLATION.md">Installation</a> •
  <a href="Docs/USER_GUIDE.md">User Guide</a> •
  <a href="Docs/ARCHITECTURE.md">Architecture</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-AGPL_v3-blue" alt="License">
  <img src="https://img.shields.io/badge/MCP-Compatible-green" alt="MCP">
  <img src="https://img.shields.io/badge/Container-aida--pentest-orange" alt="aida-pentest">
  <img src="https://img.shields.io/badge/Version-1.0.0--alpha-purple" alt="Version">
</p>

---

## What is AIDA?

**AIDA** connects AI assistants to a real pentesting environment. Instead of just *talking* about security testing, your AI can actually *do* it.

Here's the deal:
-  **Your choice of pentesting container** — use the built-in `aida-pentest` (~2 GB, starts automatically, covers all the essential tools) or bring your own [Exegol](https://github.com/ThePorgs/Exegol) container (400+ tools, ~20-40 GB). You pick at first launch — and can switch anytime.
-  **MCP integration** that works with *any* AI client (Claude, Gemini, GPT, Antigravity...)
-  **Web dashboard** to track findings, commands, and progress
-  **Structured workflow** from recon to exploitation

Think of it as giving your AI a fully-equipped hacking lab and a notebook to document everything.

<p align="center">
  <img src="./assets/view.png" alt="AIDA Dashboard" width="800">
</p>

---



## Why AIDA Exists

Modern AI assistants know pentesting tools, techniques, and vulnerability classes—**but they can't execute them.**

Without execution capabilities, security testing becomes a tedious back-and-forth: you ask the AI for a command, copy it to your terminal, wait for results, paste the output back, and repeat. Traditional scanners like Burp Suite run fixed patterns and can't adapt to specific tech stacks or chain multi-step exploits.

**AIDA changes this** by connecting AI directly to a professional pentesting environment:

- 🔧 **Direct Execution** - Built-in pentesting environment (nmap, sqlmap, ffuf, nuclei...)
- 🧠 **Persistent Memory** - Full context maintained across sessions in structured database
- 📝 **Auto Documentation** - Findings tracked as cards with severity, proof, and technical analysis
- ⛓️ **Attack Chains** - AI connects dots between discoveries to build multi-step exploits
- 🎯 **Adaptive Testing** - Methodology adjusts based on findings, not fixed patterns

**Result:** Your AI becomes an autonomous security researcher, not just a consultant.

---

##  Video Demo

<p align="">
  <a href="https://www.youtube.com/watch?v=yz6ac-y4g08">
    <img src="https://img.youtube.com/vi/yz6ac-y4g08/maxresdefault.jpg" alt="AIDA Demo Video" width="70%">
  </a>
</p>

---

## System Requirements

### Supported Platforms
- **macOS** (Intel & Apple Silicon)
- **Linux** (Ubuntu, Debian, RHEL, Fedora, Arch, and derivatives)
- **Windows** (Untested)

---

## Quick Start

### Prerequisites

- **Docker Desktop** - To run the platform
- **An AI Client** - Claude Desktop, Claude Code, Gemini CLI, Antigravity... pick your favorite
- **Pentesting container** - `aida-pentest` built-in (default, ~2 GB) or [Exegol](https://github.com/ThePorgs/Exegol) if you need 400+ tools


```bash
# Clone
git clone https://github.com/Vasco0x4/AIDA.git
cd AIDA

# Start everything
./start.sh

# Open the dashboard
open http://localhost:5173
```

On first run, `./start.sh` will ask which pentesting container you want to use — the built-in `aida-pentest` or your own Exegol container. Default is `aida-pentest`. You can change this anytime in Settings.

### Connect Your AI

Now hook up your AI client.

**Recommended: AIDA CLI (Claude Code or Kimi)**

The easiest way to get started is using the AIDA CLI wrapper, which supports both Claude Code and Kimi CLI:

```bash
# Auto-detect available CLI (Claude or Kimi)
python3 aida.py --assessment "test"

# Force a specific CLI
python3 aida.py --assessment "test" --cli claude
python3 aida.py --assessment "test" --cli kimi

# Auto-approve all actions
python3 aida.py --assessment "test" --yes
```

You can also use your own API keys (Claude only).

**Alternative: Import MCP tools into your AI client**

Here's Claude Desktop as an example:

**Default config path (macOS):**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```
**MCP config:**

```json
{
  "mcpServers": {
    "aida-mcp": {
      "command": "/bin/bash",
      "args": [
        "/absolute/path/to/AIDA/start_mcp.sh"
      ]
    }
  }
}
```

> **Full setup for all AI clients** → [INSTALLATION.md](Docs/INSTALLATION.md)

### First Assessment

1. Create an assessment in the web UI
2. Start your AI client
3. Inject the pre prompt. 
4. Tell it: *"Load assessment 'Acme' and start it"*
5. Watch it go

---

## Works With Any AI

AIDA uses the **Model Context Protocol (MCP)** - an open standard. If your AI client supports MCP, it works with AIDA.

| AI Client           | Status      | Setup |
|---------------------|-------------|-------|
| **Claude Code**     | Recommended | Via `aida.py` (automatic) |
| **Kimi CLI**        | Recommended | Via `aida.py` (automatic) |
| **External API**    | Recommended | Via `aida.py --base-url` |
| **Claude Desktop**  | Works       | Manual MCP import |
| **ChatGPT Desktop** | Works       | Manual MCP import |
| **Gemini CLI**      | Works       | Manual MCP import |
| **Antigravity**     | Works       | Manual MCP import |

> **Full setup for all AI clients** → [INSTALLATION.md](Docs/INSTALLATION.md)


---

## MCP Tools

The AI gets access to specialized tools:

```
ASSESSMENT
   load_assessment    - Load and start working
   update_phase       - Document progress

CARDS
   add_card          - Create findings/observations/info
   list_cards        - View all cards
   update_card       - Modify cards
   delete_card       - Remove cards

RECON
   add_recon_data    - Track discovered assets
   list_recon        - View recon data

EXECUTION
   execute           - Run any command in the pentesting container
   scan              - Quick scans (nmap, gobuster, ffuf...)
   subdomain_enum    - Find subdomains
   ssl_analysis      - Check SSL/TLS
   tech_detection    - Identify tech stack
   tool_help         - Get tool documentation

CREDENTIALS
   credentials_add   - Store credentials
   credentials_list  - List stored creds
```

> **Full tool documentation** → [MCP_TOOLS.md](Docs/MCP_TOOLS.md)

---

## Project Structure

```
AIDA/
├── backend/              # FastAPI + MCP Server
│   ├── api/             # REST endpoints
│   ├── mcp/             # MCP server + tools
│   ├── models/          # Database models
│   └── services/        # Business logic
├── frontend/            # React dashboard
│   ├── src/pages/       # Dashboard, Assessments, Settings...
│   └── src/components/  # Reusable UI components
├── pentest/             # Built-in pentesting container (aida-pentest)
│   └── Dockerfile       # Ubuntu 22.04 + nmap, ffuf, gobuster, sqlmap...
├── Docs/                # AI prompts and methodology
├── aida.py              # CLI launcher
├── start.sh             # Start the platform
└── docker-compose.yml   # Infrastructure
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [**INSTALLATION.md**](Docs/INSTALLATION.md) | Complete setup guide - all AI clients |
| [**USER_GUIDE.md**](Docs/USER_GUIDE.md) | How to use the platform |
| [**ARCHITECTURE.md**](Docs/ARCHITECTURE.md) | Technical deep dive + diagrams |
| [**MCP_TOOLS.md**](Docs/MCP_TOOLS.md) | All MCP tools explained |


---

## Alpha Release - Known Limitations

**AIDA is currently in alpha.** This means:

- **Local use only recommended** - Do NOT expose the web interface publicly without additional security hardening
- **No authentication system yet** - Anyone with access to the UI can view/modify assessments
- **Bugs and rough edges exist** - Some error messages use browser alerts, WebSocket reconnections may require manual refresh
- **Database credentials** - Change defaults in `.env` before any deployment

**This is a working prototype for early adopters and security professionals who understand the risks.**

Improvements coming in future releases:
- Proper authentication and user management system
- Refined UI/UX (replacing alerts with modals)
- Production-ready Docker configuration
- Enhanced error handling

**For now: Run locally, don't expose to internet, use at your own risk.**

Report bugs and request features: [GitHub Issues](https://github.com/Vasco0x4/AIDA/issues)

---

## Contributing

AIDA is actively developed. Want to contribute?

**Planned Features:**

- Frontend redesign with flat, professional UI
- OWASP testing guidelines integration
- Enhanced phase workflow system
- Advanced CLI wrapper capabilities

---

Need help? Contact **vasco0x4** on Discord.

---

## License

**AGPL v3** - Free and open source.

You can use, modify, and distribute AIDA freely. If you modify and deploy it (including as a network service), you must open source your changes under AGPL v3.

**Commercial licensing available** for organizations that need proprietary modifications.
Contact: **Vasco0x4@proton.me**

---

## Credits

- [**Anthropic MCP**](https://modelcontextprotocol.io/) - The protocol that makes this possible
- The security community for all the amazing open-source tools
- [**Exegol**](https://github.com/ThePorgs/Exegol) - Supported as an alternative container for advanced users

---
<p align="center">
  <a href="https://github.com/Vasco0x4/AIDA">⭐ Star on GitHub</a> •
  <a href="https://github.com/Vasco0x4/AIDA/issues">Report Bug</a> •
  <a href="mailto:Vasco0x4@proton.me">Contact</a>
</p>

```

### File: requirements.txt
```txt
# AIDA CLI Dependencies (for local aida.py launcher)
# These are separate from backend dependencies
click>=8.1.0
httpx>=0.26.0
rich>=13.7.0

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for AIDA
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: Docs\ARCHITECTURE.md
```md
# AIDA Architecture

Technical deep dive into how AIDA works under the hood.

---

## System Overview

AIDA is a multi-layer platform connecting AI assistants to pentesting environments:

![System Overview](assets/doc/system-overview.png)

---

## MCP Protocol Flow

How commands flow from AI to Exegol:

// TODO: Add MCP Protocol Flow Diagram

---


```

### File: Docs\INSTALLATION.md
```md
# AIDA Installation Guide

Get AIDA running in 5 minutes.

---

## Prerequisites

Before we start, make sure you have:

| Requirement | Version | Check |
|-------------|---------|-------|
| **Docker Desktop** | Latest | `docker --version` |
| **Python** | 3.10+ | `python3 --version` |
| **Node.js** | 18+ | `node --version` |
| **Git** | Any | `git --version` |

Also needed:
- **An AI client** that supports MCP — Claude Code or Kimi CLI recommended (see Step 5)

> **Exegol users:** AIDA supports Exegol as an alternative container. You will be asked at first launch.

---

## Platform Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Vasco0x4/AIDA.git
cd AIDA
```

### Step 2: Start the Platform

The easiest way - Docker Compose handles everything:

```bash
./start.sh
```

**On first run**, you will be asked to choose your pentesting container:

```
  [1] aida-pentest
      Built-in, managed by AIDA — starts automatically with ./start.sh
      Size: ~2 GB  |  Tools: nmap, ffuf, gobuster, sqlmap, nikto...

  [2] Exegol
      Third-party container — requires separate install: https://docs.exegol.com
      Size: ~20-40 GB  |  Tools: ~400+ security tools
```

Both options are fully supported. Press Enter or `1` for `aida-pentest` (default). If you're already an Exegol user, select `2` to keep using it. You can switch between them anytime in Settings.

This starts:
- **PostgreSQL** on port `5432` - The database
- **Backend API** on port `8000` - FastAPI server
- **Frontend** on port `5173` - React dashboard
- **aida-pentest** - Pentesting container (if selected above)

### Step 3: Verify It Works

Open your browser to [http://localhost:5173](http://localhost:5173)

You should see the AIDA dashboard.

---

## Step 4: Pentesting Container

AIDA supports two pentesting containers. You chose one during Step 2 — here's what to do next for each.

### Option 1 — aida-pentest (built-in)

If you selected `aida-pentest`, you're done. The container started automatically as part of `docker compose up` — no extra steps needed.

**Disk space:** ~2 GB.

**What's included:** nmap, ffuf, gobuster, sqlmap, nikto, dirb, hydra, whatweb, subfinder, dnsx, openssl + Python libs (impacket, scapy, pwntools, paramiko, requests...) + SecLists wordlists.

This covers all the essential tools for a typical assessment. If you need additional tools, you can install them directly inside the container at any time:

```bash
docker exec -it aida-pentest bash
# then install whatever you need, e.g.:
apt-get install -y metasploit-framework
```

Or switch to Exegol (Option 2) if you want 400+ tools pre-installed out of the box.

### Option 2 — Exegol

If you selected Exegol (or want to switch to it), refer to the official documentation for installation and setup: https://docs.exegol.com

Then in AIDA Settings, make sure your default container is set to match your Exegol container name.
> **Switching containers:** You can change your container preference anytime in **Settings → Container**. This affects new assessments; existing ones keep their assigned container.

---

## Step 5: Connect Your AI Client

Now you need to hook up AIDA to your AI assistant via MCP.

### Which AI Client Should I Use?

| AI Client | Recommendation | Setup Method |
|-----------|----------------|--------------|
| **Claude Code** | Recommended | Use `aida.py` CLI (automatic) |
| **Kimi CLI** | Recommended | Use `aida.py` CLI (automatic) |
| **Vertex AI / External API** | Recommended | Use `aida.py` with flags |
| **Antigravity** | Works | Manual MCP import |
| **Gemini CLI** | Works | Manual MCP import |
| **Claude Desktop** | Works | Manual MCP import |

---

## AIDA CLI — Claude Code & Kimi

The `aida.py` CLI is the recommended way to launch AIDA. It **auto-detects** which AI client you have installed (Claude Code or Kimi CLI) and configures everything automatically — MCP server, workspace, preprompt.

### Common Options

| Flag | Description |
|------|-------------|
| `-a`, `--assessment NAME` | Load a specific assessment directly |
| `--cli claude\|kimi\|auto` | Force a specific CLI (default: auto-detect) |
| `-m`, `--model MODEL` | Override the model used |
| `--preprompt FILE` | Use a custom preprompt file |
| `-y`, `--yes` | Auto-approve all AI actions |
| `--no-mcp` | Disable MCP server (for testing) |
| `--debug` | Enable debug output |
| `-q`, `--quiet` | Minimal startup output |
| `PROMPT...` | Pass an initial prompt directly |

---

## Claude Code

**Claude Code is recommended** because the AIDA CLI does everything for you.

### Prerequisites

You MUST have Claude Code installed and logged in:

```bash
# Install Claude Code
curl -fsSL https://claude.ai/install.sh | bash
```

### Launch AIDA

```bash
# Interactive — select assessment from list
python3 aida.py

# Direct launch with assessment name
python3 aida.py --assessment "MyTarget"

# With custom model
python3 aida.py --assessment "MyTarget" --model claude-opus-4-6

# Force Claude if both CLIs are installed
python3 aida.py --assessment "MyTarget" --cli claude

# Auto-approve all actions (no confirmation prompts)
python3 aida.py --assessment "MyTarget" --yes
```

The CLI automatically:
- Generates MCP config
- Sets working directory to assessment workspace
- Injects the pentesting methodology preprompt
- Configures all tools

You can verify if the MCP server is correctly loaded using `/mcp`

<img src="../assets/doc/mcp.png" alt="MCP Server" width="33%" />

**That's it. You're ready.**

---

## Kimi CLI

**Kimi CLI** is fully supported as an alternative to Claude Code. The AIDA CLI handles the full setup automatically.

### Prerequisites

Install Kimi CLI:

```bash
pip install kimi-cli
# or
uv tool install kimi-cli
```

Then log in and configure Kimi CLI according to its documentation.

### Launch AIDA with Kimi

```bash
# Auto-detect (picks Kimi if Claude isn't installed)
python3 aida.py --assessment "MyTarget"

# Force Kimi explicitly
python3 aida.py --assessment "MyTarget" --cli kimi

# With a specific model
python3 aida.py --assessment "MyTarget" --cli kimi --model kimi-k2

# Yolo mode — auto-approve everything
python3 aida.py --assessment "MyTarget" --cli kimi --yes
```

The CLI automatically:
- Generates a Kimi agent YAML file (`.aida/kimi-agent.yaml`)
- Injects the AIDA system prompt with assessment context
- Configures the MCP server for Kimi
- Sets the working directory to the assessment workspace

> **Note:** `--yes` maps to `--yolo` in Kimi CLI, which auto-approves all tool calls. Use with caution.

---

## Vertex AI / External API

If you're using Vertex AI or another external API (Claude only):

```bash
python3 aida.py --assessment "MyTarget" \
  --base-url "https://YOUR-VERTEX-ENDPOINT" \
  --api-key "YOUR-API-KEY" \
  --model claude-sonnet-4-5-20250929
```

Same benefits as Claude Code, but routing through your own API endpoint.

---

## Other AI Clients (Manual MCP Import)

For Antigravity, Gemini CLI, Claude Desktop, or ChatGPT, you need to manually configure the MCP server.

**The process:**

1. Import the MCP server config (see examples below)
2. Copy the preprompt from `Docs/PrePrompt.txt`
3. Paste it into your AI client when starting an assessment

> Antigravity works great if you select Claude. Gemini is OK. Any MCP-compatible client should work.
>
> **Prefer Claude Code or Kimi?** Use `aida.py` instead — it handles all of this automatically.

### Config Paths

**Antigravity:** MCP settings (UI)

**Gemini CLI:** `~/.gemini/settings.json`

**Claude Desktop:**
* **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
* **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
* **Linux:** `~/.config/Claude/claude_desktop_config.json`

**ChatGPT Desktop:**
* **macOS:** `~/Library/Application Support/ChatGPT/mcp_config.json`

### MCP Configuration

Add this to your config file (replace `/absolute/path/to/AIDA/` with your actual path):

```json
{
  "mcpServers": {
    "aida-mcp": {
      "command": "/bin/bash",
      "args": [
        "/absolute/path/to/AIDA/start_mcp.sh"
      ]
    }
  }
}
```

⚠️ **Important:** Replace `/absolute/path/to/AIDA/` with your actual AIDA directory path.

**After MCP setup:**
- Restart your AI client
- Copy the preprompt from `Docs/PrePrompt.txt` and paste it into your AI client
- Say to the AI: `Load assessment "your-assessment-name" and start it`

---

## Verify Installation

Run through this checklist:

| Check | How | Expected |
|-------|-----|----------|
| Platform running | http://localhost:5173 | Dashboard loads |
| API healthy | http://localhost:8000/health | `{"status": "healthy"}` |
| Database connected | Check backend logs | No connection errors |
| Pentest container | `docker ps \| grep aida-pentest` or `docker ps \| grep exegol` | Container running |
| MCP server | Check AI client | AIDA tools visible |


## Troubleshooting

TODO

---

## Next Steps

- [**User Guide**](USER_GUIDE.md) - Learn how to use the platform
- [**MCP Tools Reference**](MCP_TOOLS.md) - All available tools for your AI
- [**Architecture**](ARCHITECTURE.md) - Technical deep dive

---

## CLI Quick Reference

```bash
# List available assessments and pick one interactively
python3 aida.py

# Load a specific assessment (auto-detect CLI)
python3 aida.py -a "MyTarget"

# Force Claude Code
python3 aida.py -a "MyTarget" --cli claude

# Force Kimi CLI
python3 aida.py -a "MyTarget" --cli kimi

# Auto-approve all actions
python3 aida.py -a "MyTarget" --yes

# Custom preprompt
python3 aida.py -a "MyTarget" --preprompt /path/to/custom-preprompt.txt

# External API (Claude only)
python3 aida.py -a "MyTarget" --base-url "https://..." --api-key "..." --model claude-sonnet-4-5-20250929

# Pass an initial prompt
python3 aida.py -a "MyTarget" "Start from phase 1 and run reconnaissance"
```

---

## Need Help?

Need help? Contact **vasco0x4** on Discord.

- **GitHub Issues**: [Report bugs](https://github.com/Vasco0x4/AIDA/issues)
- **Email**: Vasco0x4@proton.me

```

### File: Docs\MCP_TOOLS.md
```md
# MCP Tools Reference

Complete reference for all MCP tools available to AI clients.

---

## Overview

AIDA exposes tools through the Model Context Protocol (MCP). These tools give AI assistants the ability to:

- Execute commands in Exegol containers
- Document findings and observations
- Track reconnaissance data
- Manage credentials
- Run specialized security scans

---

## 📋 MCP Tools Cheatsheet

| Category | Tool | Signature | Description |
|----------|------|-----------|-------------|
| **Assessment** | `load_assessment` | `load_assessment(name="Target")` | Load assessment and get full context |
| | `update_phase` | `update_phase(phase_number=1.0, content="...")` | Document progress in a phase |
| **Cards** | `add_card` | `add_card(card_type="finding", title="...", severity="HIGH", ...)` | Create finding card |
| | | `add_card(card_type="observation", title="...", notes="...")` | Create observation card |
| | | `add_card(card_type="info", title="...", context="...")` | Create info card |
| | `list_cards` | `list_cards()` | List all cards |
| | | `list_cards(card_type="finding", severity="CRITICAL")` | Filter cards by type/severity |
| | `update_card` | `update_card(card_id=42, status="confirmed", proof="...")` | Update existing card |
| | `delete_card` | `delete_card(card_id=42)` | Delete card by ID |
| **Recon** | `add_recon_data` | `add_recon_data(data_type="endpoint", name="/api/users", details={...})` | Add single recon entry |
| | | `add_recon_data(entries=[{...}, {...}])` | Batch import recon data |
| | `list_recon` | `list_recon()` | List all recon data |
| | | `list_recon(data_type="subdomain", limit=100)` | Filter recon by type |
| **Execution** | `execute` | `execute(command="nmap -sV 10.0.0.1")` | Run shell command in Exegol |
| | | `execute(command="...", phase="recon")` | Run with phase context |
| | `python_exec` | `python_exec(code="import socket; ...")` | Execute Python code in Exegol |
| | | `python_exec(code="...", phase="recon")` | Run Python with phase context |
| | `http_request` | `http_request(method="GET", url="https://...")` | Make HTTP request from Exegol |
| | | `http_request(method="POST", url="...", body={...}, headers={...})` | POST with body and headers |
| **Pentesting** | `scan` | `scan(type="nmap_quick", target="10.0.0.1")` | Quick nmap scan |
| | | `scan(type="nmap_full", target="10.0.0.1", ports="1-65535")` | Full port scan |
| | | `scan(type="gobuster", target="https://...", wordlist="medium")` | Directory enumeration |
| | | `scan(type="ffuf", target="https://.../FUZZ", wordlist="common")` | Web fuzzing |
| | `subdomain_enum` | `subdomain_enum(domain="acme.com")` | Find subdomains |
| | `ssl_analysis` | `ssl_analysis(target="acme.com:443")` | Analyze SSL/TLS config |
| | `tech_detection` | `tech_detection(url="https://acme.com")` | Detect technology stack |
| | `tool_help` | `tool_help(tool="sqlmap")` | Get tool documentation |
| **Credentials** | `credentials_add` | `credentials_add(credential_type="bearer_token", name="...", token="...")` | Store bearer token |
| | | `credentials_add(credential_type="cookie", name="...", cookie_value="...")` | Store cookie |
| | | `credentials_add(credential_type="ssh", username="...", password="...")` | Store SSH credentials |
| | `credentials_list` | `credentials_list()` | List all stored credentials |
| | | `credentials_list(credential_type="bearer_token")` | Filter by credential type |

---

## Tool Categories

| Category | Tools | Purpose |
|----------|-------|---------|
| [Assessment](#assessment-management) | 2 | Load and update assessments |
| [Cards](#cards-management) | 4 | Findings, observations, info |
| [Recon](#reconnaissance) | 2 | Track discovered assets |
| [Execution](#command-execution) | 3 | Run commands, Python code, HTTP requests in Exegol |
| [Pentesting](#pentesting-tools) | 5 | Specialized security tools |
| [Credentials](#credentials-management) | 2 | Store and retrieve creds |

---

## Assessment Management

### `load_assessment`

Load an existing assessment to begin work.

> Assessments are created via the web interface, not by the AI.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | string | Yes | Assessment name |
| `skip_data` | boolean | No | If true, only sets context without returning data |

**Returns:**
- Assessment metadata (name, target, container)
- Existing findings and observations
- Recon data collected so far
- Recent command history
- Stored credentials (placeholders only)

---

### `update_phase`

Document progress in a phase section.

**Example:**

```python
update_phase(
    phase_number=1.0,
    content="## Initial Reconnaissance\n\nCompleted nmap scan of 10.0.0.1\nFound 3 open ports: 22, 80, 443\nIdentified nginx 1.18.0 on port 80"
)
```

---

## Cards Management

Cards are the primary way to document findings.

### `add_card`

Create a finding, observation, or info card.

**Examples:**

```python
# Critical finding
add_card(
    card_type="finding",
    title="SQL Injection in Login Form",
    severity="CRITICAL",
    status="confirmed",
    target_service="https://app.acme.com/login",
    technical_analysis="The login form is vulnerable to SQL injection via the username parameter.",
    proof="sqlmap -u 'https://app.acme.com/login' --data='user=admin&pass=test' -p user --dbs"
)

# Observation
add_card(
    card_type="observation",
    title="Missing Rate Limiting",
    target_service="https://app.acme.com/api",
    notes="The API does not implement rate limiting. This could allow brute force attacks."
)

# Info
add_card(
    card_type="info",
    title="Technology Stack",
    context="Frontend: React 18\nBackend: Node.js/Express\nDatabase: PostgreSQL 14"
)
```

**Returns:** Card ID

---

### `list_cards`

List all cards with optional filters.

**Examples:**

```python
# All cards
list_cards()

# Only critical findings
list_cards(card_type="finding", severity="CRITICAL")

# All observations
list_cards(card_type="observation")
```

---

### `update_card`

Update an existing card by ID.

**Example:**

```python
update_card(
    card_id=42,
    status="confirmed",
    proof="Additional exploitation proof:\n$ curl -X POST..."
)
```

---

### `delete_card`

Delete a card by ID.

**Example:**

```python
delete_card(card_id=42)
```

---

## Reconnaissance

Track discovered assets automatically.

### `add_recon_data`

Add reconnaissance data (single or batch).

**Examples:**

```python
# Single entry
add_recon_data(
    data_type="subdomain",
    name="api.acme.com",
    details={"ip": "10.0.0.5", "source": "subfinder"}
)

# Batch entry
add_recon_data(entries=[
    {"data_type": "endpoint", "name": "/api/v1/users"},
    {"data_type": "endpoint", "name": "/api/v1/admin"},
    {"data_type": "endpoint", "name": "/api/v1/config"},
])
```

---

### `list_recon`

List reconnaissance data with filters.

**Examples:**

```python
# All recon data
list_recon()

# Just endpoints
list_recon(data_type="endpoint")

# Just subdomains
list_recon(data_type="subdomain", limit=100)
```

---

## Command Execution

Three tools allow code execution inside the Exegol container. Each has its own independently configurable output max length (Settings → Command Settings → Output Max Length).

### `execute`

Execute any shell command in the Exegol container.

**Examples:**

```python
# Simple command
execute(command="whoami")

# With phase context
execute(
    command="nmap -sV -sC 10.0.0.1",
    phase="reconnaissance"
)

# Complex command
execute(command="sqlmap -u 'https://target.com/api?id=1' --dbs --batch")
```

**Returns:**
- Command output (stdout/stderr)
- Exit code
- Execution time

**Notes:**
- Commands may require approval based on settings
- Output is truncated to the `execute` output max length setting
- Credential placeholders (`{{TOKEN}}`) are auto-substituted

---

### `python_exec`

Execute Python code directly inside the Exegol container via stdin, without shell escaping issues.

**Examples:**

```python
# Network recon
python_exec(code="""
import socket
ip = socket.gethostbyname('acme.com')
print(f'Resolved: {ip}')
""")

# Use installed libraries (requests, scapy, impacket, etc.)
python_exec(
    code="""
import requests
r = requests.get('https://target.com/api/users', verify=False)
print(r.status_code, r.text[:500])
""",
    phase="recon"
)
```

**Returns:**
- Python stdout/stderr output
- Exit code

**Notes:**
- Code is passed via stdin — no shell escaping needed
- All tools installed in Exegol are available (requests, scapy, impacket, etc.)
- Output is truncated to the `python_exec` output max length setting
- Credential placeholders (`{{TOKEN}}`) are auto-substituted in the code

---

### `http_request`

Make HTTP requests directly from the Exegol container. Useful for testing endpoints that require specific network routing, proxies, or certificates.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `method` | string | Yes | HTTP method: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`, `HEAD`, `OPTIONS` |
| `url` | string | Yes | Target URL |
| `headers` | object | No | HTTP headers dict |
| `body` | any | No | Request body (dict → JSON, string → raw) |
| `timeout` | int | No | Request timeout in seconds (default: 30) |
| `verify_ssl` | bool | No | Verify SSL certificates (default: true) |
| `follow_redirects` | bool | No | Follow HTTP redirects (default: true) |
| `proxy` | string | No | Proxy URL (e.g. `http://127.0.0.1:8080`) |
| `phase` | string | No | Phase context for logging |

**Examples:**

```python
# Simple GET
http_request(method="GET", url="https://target.com/api/users")

# POST with JSON body
http_request(
    method="POST",
    url="https://target.com/api/login",
    headers={"Content-Type": "application/json"},
    body={"username": "admin", "password": "test"}
)

# With auth header and SSL bypass
http_request(
    method="GET",
    url="https://internal.target.com/admin",
    headers={"Authorization": "Bearer {{ADMIN_API_TOKEN}}"},
    verify_ssl=False,
    phase="exploitation"
)

# Through Burp proxy
http_request(
    method="GET",
    url="https://target.com/api/secret",
    proxy="http://127.0.0.1:8080",
    verify_ssl=False
)
```

**Returns:**
- Status code and response headers
- Response body (truncated to `http_request` output max length setting)
- Response time

**Notes:**
- Requests are made from within the Exegol container (internal network access)
- Credential placeholders (`{{TOKEN}}`) are auto-substituted in headers and body
- Commands may require approval based on settings

---

## Pentesting Tools

Specialized wrappers for common security tools.

### `scan`

Run security scans with common tools.

**Scan Types:**

| Type | Tool | Purpose |
|------|------|---------|
| `nmap_quick` | nmap | Fast scan of top ports |
| `nmap_full` | nmap | All ports + version detection |
| `nmap_vuln` | nmap | Vulnerability scripts |
| `gobuster` | gobuster | Directory enumeration |
| `ffuf` | ffuf | Web fuzzing |
| `dirb` | dirb | Directory bruteforce |
| `nikto` | nikto | Web server scanner |

**Wordlist Options:**

| Option | Description |
|--------|-------------|
| `common` | Fast, common paths |
| `medium` | Balanced |
| `large` | Thorough |
| `dirb` | dirb default list |
| `raft-small` | Raft small words |
| `raft-medium` | Raft medium words |

**Examples:**

```python
# Quick nmap scan
scan(type="nmap_quick", target="10.0.0.1")

# Full port scan with version detection
scan(type="nmap_full", target="10.0.0.1", ports="1-65535")

# Directory enumeration
scan(
    type="gobuster",
    target="https://app.acme.com",
    wordlist="medium",
    extensions="php,html,js"
)

# Web fuzzing with custom flags
scan(
    type="ffuf",
    target="https://app.acme.com/FUZZ",
    wordlist="common",
    extra_flags="-mc 200,301,302"
)
```

---

### `subdomain_enum`

Enumerate subdomains for a domain.

**Example:**

```python
subdomain_enum(domain="acme.com")
```

---

### `ssl_analysis`

Analyze SSL/TLS certificate and configuration.

**Examples:**

```python
ssl_analysis(target="acme.com")
ssl_analysis(target="10.0.0.1:8443")
```

**Checks:**
- Certificate validity
- Cipher suites
- Protocol versions
- Known vulnerabilities

---

### `tech_detection`

Detect technology stack of a website.

**Example:**

```python
tech_detection(url="https://app.acme.com")
```

Uses: whatweb, wappalyzer (if available)

---

### `tool_help`

Get help documentation for a tool.

**Example:**

```python
tool_help(tool="sqlmap")
```

Returns: Tool availability and help output

---

## Credentials Management

Store and retrieve discovered credentials.

### `credentials_add`

Add authentication credentials.

**Credential Types:**

| Type | Fields | Use |
|------|--------|-----|
| `bearer_token` | `token` | API bearer tokens |
| `api_key` | `token` | API keys |
| `basic_auth` | `username`, `password` | HTTP basic auth |
| `cookie` | `cookie_value` | Session cookies |
| `ssh` | `username`, `password` | SSH credentials |
| `custom` | `custom_data` | Other formats |

**Examples:**

```python
# Bearer token
credentials_add(
    credential_type="bearer_token",
    name="Admin API Token",
    token="eyJhbGciOiJIUzI1NiIs...",
    service="API",
    target="https://api.acme.com"
)
# Creates placeholder: {{ADMIN_API_TOKEN}}

# SSH credentials
credentials_add(
    credential_type="ssh",
    name="Web Server Root",
    username="root",
    password="admin123",
    target="10.0.0.5"
)
# Creates placeholder: {{WEB_SERVER_ROOT}}

# Cookie
credentials_add(
    credential_type="cookie",
    name="Admin Session",
    cookie_value="session=abc123; admin=true",
    notes="Expires in 24 hours"
)
```

**Placeholder Substitution:**

Once stored, use placeholders in commands:

```python
execute(command="curl -H 'Authorization: Bearer {{ADMIN_API_TOKEN}}' https://api.acme.com/admin")
```

The placeholder is automatically replaced with the actual token.

---

### `credentials_list`

List all stored credentials.

---

## Related Documentation

- [User Guide](USER_GUIDE.md) - How to use the platform
- [Architecture](ARCHITECTURE.md) - Technical deep dive
- [Installation](INSTALLATION.md) - Setup guide

```

### File: Docs\PrePrompt.txt
```txt
## **Identity**

You are a cybersecurity & pentesting expert conducting full‑scope assessments using AIDA (AI-Driven Security Assessment).
* Only operate when scope, target and constraints are clear. If missing -> ask the user.
* Never fabricate scan results, endpoints, vulnerabilities, output, or exploits.


## **Testing Methodology**

* **Test ALL attack types**: SQLi, NoSQL, XSS, CSRF, SSRF, XXE, SSTI, path traversal, file upload, IDOR, business logic, JWT manipulation, authentication bypass, privilege escalation, etc.
* **Leverage application knowledge**: If you know the application, use your deep knowledge of known vulnerabilities, specific endpoints, and attack vectors.
* **Be autonomous**: Keep testing until explicitly told to stop. Do not ask for confirmation between phases.
* **Never propose reports**: Only document findings with `add_card(card_type="finding", ...)`. Reports are generated only when explicitly requested by the user.


## **Pentesting Container**

You have access to a dedicated pentesting container

All pentesting tools are pre-installed (nmap, sqlmap, ffuf, hydra, etc.). Wordlists available via `scan()` tool or under `/usr/share/` (dirb, dirbuster, seclists).

> If a tool is missing, install it with `execute("apt-get install -y <tool>")` or `execute("pip3 install <lib>")`.

## **Workspace**

You are working in the assessment's workspace directory. Your current working directory is already set correctly.

**For file operations** (Read, Write, Bash):
- Use relative paths (e.g., `loot/credentials.txt`)
- Or absolute paths from current directory

**For container commands** (MCP `execute()`, `python_exec()`, `http_request()`):
- Commands run inside the container with all pentesting tools
- The container workspace is automatically mapped
- Credential placeholders (e.g. `{{TOKEN}}`) are auto-substituted in all 3 tools

**Context documents**: If provided by the user, they are in the `context/` folder.

## **Assessment Creation & Start**

### Creating a New Assessment
When the user wants to start a new pentest and no assessment exists yet:

1. **Gather information first** — Do NOT create the assessment immediately. Ask the user about:
   - Target scope (domains, IPs, applications)
   - Assessment category (API, Website, External Infra, Mobile, Cloud, General)
   - Client name
   - Objectives and constraints
   - Environment (production, dev, or unspecified)
   - Any limitations or exclusions
   - Access information (VPN, credentials, jump hosts) if relevant
2. **Not everything is mandatory** — Only fill in fields that are relevant. The only required field is the assessment name. Don't force the user to provide every detail.
3. **Confirm before creating** — Summarize the gathered information and ask the user to validate before calling `create_assessment()`.
4. **Create** — Call `create_assessment(name=..., scope=..., ...)` with the gathered details. The assessment is auto-loaded after creation.
5. **Start the workflow** — Proceed to Phase 1 (Reconnaissance).

Use `list_assessments()` to check for existing assessments and avoid duplicates.
Use `list_containers()` if the user asks about available pentesting environments.

### Loading an Existing Assessment
1. `list_assessments()` to see available assessments
2. `load_assessment(name="...")` to load
3. Read the state of work
4. Follow the workflow dynamically

## **Assessment Uniqueness**

Each assessment is unique.
Adapt tools, techniques, and phase order based on the target’s technologies, exposed services, and new discoveries.
Switch phases whenever needed (e.g., return to recon after new info).
Always choose the most appropriate MCP tools and commands for the context.

---

# **Workflow**

## **Phase 1 – Recon**

DNS, WHOIS, subdomains, tech stack, SSL, OSINT, port scans, service detection.
Store discovered assets with `add_recon_data()`. Use lowercase snake_case categories (custom categories allowed).

## **Phase 2 – Mapping**

Directories, endpoints, APIs, version detection, enumerations, topology.
Update recon data + use `update_phase()` for notes.

## **Phase 3 – Vulnerability Assessment**

Manual + automated analysis, config review, input validation, weak creds.

Use:

* `add_card(card_type="finding", ...)` - for confirmed vulnerabilities
* `add_card(card_type="observation", ...)` - for analysis notes
* `add_card(card_type="info", ...)` - for tech stack details

**Rules:**

* Treat any unconfirmed vulnerability as suspicion until validated.
* Prioritize actions with highest information gain: service discovery, tech stack, authentication points, attack surface.

## **Phase 4 – Exploitation**

Exploit, validate, privilege escalate, lateral movement, impact verification.

Store files in:

* `recon/` → scans and reconnaissance data
* `exploits/` → scripts & PoCs
* `loot/` → extracted data & credentials
* `context/` → user-provided documentation
* `notes/` → analysis notes & screenshots
* `scripts/` → automation tools

Update findings with `update_card(card_id, ...)`.

---

# **Documentation Rules**

* Document immediately upon discovery.
* Always include commands + raw output for reproducibility.
* Update existing cards with `update_card()` instead of duplicating.
* No interpretation unless asked. Stick to facts.

## **Proof Requirement**

For every finding:
**Provide the exact commands used to discover, verify, or exploit the issue, plus raw output when relevant.**
Proof must be complete and reproducible.

---

# **Severity**

For all findings, provide a CVSS 4.0 vector string using the `cvss_vector` parameter in `add_card()`.
If CVSS cannot be meaningfully assessed, use `severity` parameter directly (CRITICAL/HIGH/MEDIUM/LOW/INFO).


Never classify CRITICAL without confirmed exploitation.

---

# **Communication**

* Concise and operational.
* Summaries of actions in natural language.
* Show command output when relevant.

---

# **Error Handling**

* If a tool fails → use alternative or request assistance.
* If a command times out → stop and notify.
* If MCP errors → adjust parameters and retry.
* **Never loop on request formatting** — If a request fails 2 times due to wrong format, missing parameters, unexpected response structure, or authentication issues, STOP and ask the user to provide a working sample request (Burp copy-paste, curl command, or raw HTTP). Do not keep modifying payloads blindly. The user has access to the application and can provide the correct format immediately.
```

### File: Docs\USER_GUIDE.md
```md
# AIDA User Guide

Complete guide to running security assessments with AI-driven pentesting.

---

## Overview

AIDA follows a streamlined workflow:

```
Create Assessment → Configure Workspace → Connect AI → Run Tests → Review Findings
```

**You manage** the assessment scope and configuration.  
**The AI handles** command execution, vulnerability testing, and documentation.

---

## Quick Start

### 1. Create a New Assessment

Click **"New Assessment"** from the sidebar or dashboard.

<img src="../assets/doc/new-assessment-button.png" alt="New Assessment Button" width="33%" />

Fill in the required information:
- **Assessment Name** - Unique identifier (e.g., "Acme Corp Pentest")
- **Client Name** - Organization being tested
- **Target Domains** - Primary targets (e.g., `app.acme.com`)
- **IP Scopes** - Network ranges (e.g., `10.0.0.0/24`)
- **Category** - Type of assessment (API, Website, Infrastructure, etc.)
- **Environment** - Production, Development
- **Scope & Objectives** - What's in scope and out of scope
- **Start/End Dates** - Assessment timeline

<img src="../assets/doc/assessment-creation.png" alt="Assessment Creation" width="66%" />

Your assessment is now ready!

---

## 📁 Assessment Workspace

Each assessment gets its own isolated workspace inside the Exegol container with a predefined folder structure:

```
/workspace/assessment-name/
├── recon/          # Scan outputs, nmap results, enumeration data
├── exploits/       # PoC scripts, payloads, exploit code
├── loot/           # Extracted data, credentials, sensitive files
├── notes/          # Screenshots, analysis notes, observations
├── scripts/        # Custom automation scripts
└── context/        # User-provided documentation (uploaded files)
```

**How it works:**
- The AI automatically saves scan results to appropriate folders
- All commands execute within this workspace context
- Files persist across sessions
- You can access the workspace directly via the UI

---

## 🔑 Credentials & Authentication

### Managing Credentials

Store discovered credentials or provide authentication tokens for testing:

![Credentials Management](../assets/doc/credentials-management.png)

**Supported credential types:**
- **Bearer Tokens** - API tokens, JWT tokens
- **API Keys** - Service API keys
- **Cookies** - Session cookies
- **SSH Credentials** - Username/password or key pairs
- **Basic Auth** - HTTP basic authentication
- **Custom** - Any other authentication format

**Placeholder Usage:**

When you add a credential, AIDA generates a placeholder like `{{ADMIN_API_TOKEN}}`. The AI can use this in commands:

```bash
curl -H "Authorization: Bearer {{ADMIN_API_TOKEN}}" https://api.acme.com/admin
```

The placeholder is automatically replaced with the actual token during execution.

---

## Context Documents

Upload supporting documentation to help the AI understand your target:

![Context Upload](../assets/doc/context-upload.png)

**What to upload:**
- API documentation (OpenAPI/Swagger specs)
- Architecture diagrams
- Previous penetration test reports
- Scope definitions and rules of engagement
- Configuration files
- Source code (if white-box testing)

**After upload:**

<img src="../assets/doc/workspace-view.png" alt="Workspace View" width="33%" />

The AI can read these documents for context when planning attacks and understanding the application architecture.

---

## Reconnaissance Data & Import

### Automatic Reconnaissance Tracking

The AI automatically tracks discovered assets in the **Recon Data** section:

![Recon Data](../assets/doc/recon-data.png)

**Tracked asset types:**
- Endpoints (API routes, URLs)
- Subdomains
- Services (ports, protocols)
- Technologies (frameworks, libraries)
- Databases
- Ports
- Vulnerabilities

### Pre-Assessment Scans Import

For infrastructure assessments, it's recommended to run long scans beforehand and import results:

<img src="../assets/doc/import-scans.png" alt="Import Scan Results" width="66%" />

**Supported import formats:**
- Nmap XML output
- Nuclei JSON results
- ffuf JSON output
- Custom JSON/CSV formats

**Why pre-import?**
- Saves time during the assessment
- Long-running scans (full port scans) can run overnight
- AI starts with complete reconnaissance data
- More efficient testing workflow

---

## 🚀 Starting the Assessment

### Connect Your AI

Launch AIDA with your preferred AI client:

```bash
# Auto-detect Claude Code or Kimi CLI
python3 aida.py --assessment "Acme Corp Pentest"

# Or force a specific CLI
python3 aida.py --assessment "Acme Corp Pentest" --cli claude
python3 aida.py --assessment "Acme Corp Pentest" --cli kimi
```

The CLI injects the preprompt and loads the assessment context automatically. Then tell the AI:

```
Load assessment 'Acme Corp Pentest'
```

The AI receives:
- Assessment metadata (scope, targets, objectives)
- Pre-loaded reconnaissance data
- Existing findings and cards
- Command history from previous sessions
- Credential placeholders for authenticated testing
- Context documents (if uploaded)

### Running Commands

The AI executes commands directly in the Exegol container:

**Example commands:**
```bash
# Network scanning
nmap -sV -p- 10.0.0.1

# Directory enumeration
ffuf -u https://app.acme.com/FUZZ -w /usr/share/wordlists/common.txt

# SQL injection testing
sqlmap -u "https://app.acme.com/api?id=1" --dbs --batch

# Subdomain discovery
subfinder -d acme.com -silent
```

All output is captured and logged in command history.

### Creating Findings

When the AI discovers vulnerabilities, it automatically creates finding cards:

**Example finding card:**
```
Title: SQL Injection in User API
Severity: CRITICAL
Status: confirmed
Target: https://app.acme.com/api/users?id=1
Technical Analysis: 
  The 'id' parameter is vulnerable to SQL injection. 
  Error-based injection reveals MySQL 5.7 database.
Proof:
  sqlmap -u "https://app.acme.com/api/users?id=1" --dbs
  [Output showing database extraction]
```

### Credential Storage

When credentials are discovered, the AI stores them with placeholders:

**Example:**
```
Type: Bearer Token
Name: Admin API Access
Service: Admin API
Target: https://api.acme.com/admin
Placeholder: {{ADMIN_API_ACCESS}}
Notes: Found in config.js, expires 2026-02-28
```

---

## Command Approval System

For security and control, AIDA supports three command approval modes:

![Command Approval Settings](../assets/doc/command-approval-modes.png)

### Approval Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| **Open** | All commands execute automatically | Trusted environments, development |
| **Filtered** | Only flagged commands require approval | Production testing with safeguards |
| **Closed** | Every command requires manual approval | High-risk targets, strict compliance |

### Filtered Mode Configuration

![Filtered Keywords](../assets/doc/command-approval-keywords.png)

In **Filtered** mode, specify dangerous keywords that trigger approval.

### Approval Notifications

**⚠️ Important:** Enable browser notifications!

When a command requires approval:
1. Browser notification appears
2. Popup shows command details
3. You approve or reject
4. Unapproved commands timeout after 30 seconds (by default) *

**Without notifications enabled, commands will timeout!**

*Configure in **Settings → Command Execution**.

---

## Cards System

Cards are the primary documentation mechanism in AIDA. There are three types:

### 1. Finding Cards (Vulnerabilities)

Confirmed or potential security vulnerabilities.

![Finding Card Example](../assets/doc/finding-card-example.png)

**Fields:**

| Field | Description | Example |
|-------|-------------|---------|
| **Title** | Vulnerability name | "SQL Injection in Login Form" |
| **Severity** | Risk level | CRITICAL / HIGH / MEDIUM / LOW / INFO |
| **Status** | Confirmation status | confirmed / potential / untested |
| **Target/Service** | Affected component | `https://app.acme.com/login` |
| **Technical Analysis** | Detailed explanation | "The username parameter lacks input validation..." |
| **Proof** | PoC commands and output | Full reproduction steps |

**Severity Guidelines:**
- **CRITICAL** - Direct exploitation with major impact (RCE, full DB access)
- **HIGH** - Exploitable with significant impact (auth bypass, data leak)
- **MEDIUM** - Conditional exploitation (CSRF, XSS)
- **LOW** - Minor issues (information disclosure)
- **INFO** - Hardening recommendations

### 2. Observation Cards

Security-relevant findings that aren't direct vulnerabilities but indicate weaknesses or misconfigurations.

**Examples:**
- "Server discloses version in headers (nginx/1.18.0)"
- "No rate limiting on login endpoint"
- "Cookies missing HttpOnly and Secure flags"
- "Cloudflare WAF detected - bypass may be possible"
- "Directory listing enabled on /backup/"
- "Verbose error messages reveal stack traces"

### 3. Info Cards

General notes and context information.

**Examples:**
- "Application stack: React 18 + Node.js + PostgreSQL"
- "API documentation available at /swagger"
- "Authentication uses JWT tokens with 24h expiry"
- "Backup endpoint found at /api/v1/export"

---

## Command History

Every command execution is logged with full details:

<!-- TODO: Add command history screenshot -->
![Command History](../assets/doc/command-history.png)

**Logged information:**
- Command text
- Execution timestamp
- Exit code (success/failure)
- Standard output (stdout)
- Error output (stderr)
- Execution time
- Associated phase (recon, mapping, exploitation)

Access via **Commands** page or within each assessment detail view.

---

## Folder Organization

Organize assessments into folders for better project management:

**Default folders:**
- **Active** - Ongoing engagements
- **Archived** - Completed assessments

**Create custom folders:**
- By client (e.g., "Acme Corp", "Beta Inc")
- By type (e.g., "Web Apps", "Infrastructure", "APIs")
- By quarter (e.g., "Q1 2026", "Q2 2026")

Folders help maintain organization across multiple concurrent assessments.

---

## Settings & Configuration

### Platform Settings

**Backend Configuration:**
- API URL (default: `http://localhost:8000/api`)
- Container management (Exegol)
- Database connection

**Command Execution:**
- Approval mode (Open/Filtered/Closed)
- Dangerous keywords (for Filtered mode)
- Command timeout duration
- Output length limits

**UI Preferences:**
- Theme (light/dark)

### Exegol Container

AIDA automatically manages the Exegol pentesting container:
- Container name: `exegol-aida` (configurable)
- Workspace mount: `/workspace`

Access container directly:
```bash
docker exec -it exegol-aida /bin/zsh
```

---

## Best Practices

### Before Starting

1. **Define scope clearly** - Specify exactly what's in/out of scope
2. **Upload context docs** - API docs, architecture diagrams
3. **Pre-run long scans** - Import nmap, nuclei results
4. **Configure credentials** - Add known test accounts
5. **Set approval mode** - Choose appropriate command control

### During Assessment

1. **Enable notifications** - For command approvals
2. **Monitor command history** - Check AI decision-making

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| [**Installation Guide**](INSTALLATION.md) | Setup AIDA — Claude Code, Kimi, and other clients |
| [**MCP Tools Reference**](MCP_TOOLS.md) | Complete list of AI-available tools |
| [**Architecture**](ARCHITECTURE.md) | Technical deep dive into AIDA |
| [**PrePrompt**](PrePrompt.txt) | AI behavior guidelines |

---

Need help? Contact **vasco0x4** on Discord.

```


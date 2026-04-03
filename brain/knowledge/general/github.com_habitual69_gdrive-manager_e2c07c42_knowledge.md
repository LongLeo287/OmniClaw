---
id: github.com-habitual69-gdrive-manager-e2c07c42-know
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:05.493695
---

# KNOWLEDGE EXTRACT: github.com_habitual69_gdrive-manager_e2c07c42
> **Extracted on:** 2026-04-01 11:27:49
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521356/github.com_habitual69_gdrive-manager_e2c07c42

---

## File: `README.md`
```markdown
# 📁 gdrive-manager

> A production-ready **Agent Skill** for full Google Drive management — works natively across Claude Code, Gemini CLI, Kilo Code, Codex CLI, Kiro, OpenCode, GitHub Copilot, and more.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-8A2BE2)](https://agentskills.io)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-✓-blueviolet)](https://code.claude.com)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-✓-orange)](https://github.com/google-gemini/gemini-cli)
[![Kilo Code](https://img.shields.io/badge/Kilo%20Code-✓-teal)](https://kilo.ai)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-✓-black)](https://developers.openai.com/codex)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-✓-blue)](https://github.com/features/copilot)
[![Kiro](https://img.shields.io/badge/Kiro-✓-red)](https://kiro.dev)
[![OpenCode](https://img.shields.io/badge/OpenCode-✓-green)](https://opencode.ai)

---

## What Is This?

`gdrive-manager` is a single **Agent Skill** following the [Agent Skills open standard](https://agentskills.io) — a `SKILL.md` + executable Python scripts — that teaches any AI agent to fully manage Google Drive:

- Create, read, update, delete files and folders (Docs, Sheets, Slides, PDFs, any file)
- Upload and download files and entire folder trees
- Search by name, full-text content, or file type
- Manage sharing permissions
- All with **mandatory safety guardrails** enforced in code — no AI can silently delete your files

Because it follows the open Agent Skills standard, the **same skill folder works natively** across every major AI coding assistant with no reformatting or duplication.

---

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Install with npx skills (Universal)](#-install-with-npx-skills-universal)
- [Manual Installation by Agent](#manual-installation-by-agent)
  - [Claude Code](#-claude-code)
  - [Gemini CLI](#-gemini-cli)
  - [Kilo Code](#-kilo-code)
  - [OpenAI Codex CLI](#-openai-codex-cli)
  - [Kiro](#-kiro-ide--cli)
  - [OpenCode](#-opencode)
  - [GitHub Copilot](#-github-copilot-vs-code)
  - [Claude.ai Browser](#-claudeai-browser)
- [Prerequisites & Auth Setup](#prerequisites--auth-setup)
- [Safety Guardrails](#-safety-guardrails)
- [Command Reference](#command-reference)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

---

## Features

| | |
|---|---|
| 📄 **CRUD Files** | Create, read, update, delete — Docs, Sheets, Slides, PDFs, any file |
| 📂 **CRUD Folders** | Create, list, rename, move, trash, permanently delete |
| ⬆️ **Upload** | Single file, recursive folder, auto-convert Office → Google Workspace |
| ⬇️ **Download** | Single file, recursive folder, auto-export Workspace → Office format |
| 🔍 **Search** | By name (partial), full-text content, MIME type, parent folder |
| 🔗 **Share** | Share with user, make public, list/revoke permissions |
| 📊 **Output** | Markdown table (default) or JSON |
| 🔒 **Safety** | Two-step human confirmation required for all destructive operations — enforced in code |

---

## Quick Start

```bash
# Clone
git clone https://github.com/habitual69/gdrive-manager.git
cd gdrive-manager

# Install Python dependencies
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

# Interactive setup: detects OS & shell, asks where credentials.json lives,
# runs OAuth, then prints exact export commands for your environment
python scripts/auth_setup.py

# Try it
python scripts/gdrive.py list
```

---

## 🚀 Install with npx skills (Universal)

The fastest way to install across any supported agent. The `npx skills` CLI auto-detects which agents you have installed.

```bash
# Install to all detected agents at once
npx skills add habitual69/gdrive-manager

# Install to a specific agent only
npx skills add habitual69/gdrive-manager --agent claude-code
npx skills add habitual69/gdrive-manager --agent gemini-cli
npx skills add habitual69/gdrive-manager --agent kilo-code
npx skills add habitual69/gdrive-manager --agent codex

# Install globally (available across all projects)
npx skills add habitual69/gdrive-manager --global

# List all installed skills
npx skills list

# Update to latest version
npx skills update habitual69/gdrive-manager
```

---

## Manual Installation by Agent

All agents follow the same pattern: copy the skill folder into the agent's skills discovery directory. The skill is then auto-discovered on next startup — no config file edits needed.

**Skill precedence across all agents:** project-level (`.agent/skills/`) overrides global (`~/.agent/skills/`) when names conflict.

---

### 🟣 Claude Code

**Docs:** [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)

Claude Code scans `~/.claude/skills/` (personal — all projects) and `.claude/skills/` (project-level — current repo only). Skills are auto-discovered at startup with live reload — no restart needed when you edit a skill during a session.

```bash
# Global install — available in all your projects
git clone https://github.com/habitual69/gdrive-manager.git ~/.claude/skills/gdrive-manager

# OR project-level install — checked into your repo
git clone https://github.com/habitual69/gdrive-manager.git .claude/skills/gdrive-manager
```

**Verify it loaded (in a Claude Code session):**
```
/skills
```

**Invoke explicitly:**
```
/gdrive-manager list all my Drive files
```

**Invoke automatically** — just ask anything Drive-related and Claude Code matches the skill description and activates it automatically.

> **How it works:** At startup Claude Code reads only `name` and `description` (~100 tokens) from each `SKILL.md`. When your task matches, the full skill body and scripts directory load into context. Claude can then call `scripts/gdrive.py` directly via bash.

---

### 🔵 Gemini CLI

**Docs:** [geminicli.com/docs/cli/skills](https://geminicli.com/docs/cli/skills/)

Gemini CLI scans two locations:
- `~/.gemini/skills/` — **User scope**: global, all projects
- `.gemini/skills/` — **Workspace scope**: project-local, shareable with team via git

```bash
# User scope (global)
git clone https://github.com/habitual69/gdrive-manager.git ~/.gemini/skills/gdrive-manager

# Workspace scope (project-local)
git clone https://github.com/habitual69/gdrive-manager.git .gemini/skills/gdrive-manager
```

**Or use the built-in `gemini skills` command:**
```bash
# Install from GitHub (.skill bundle or folder)
gemini skills install https://github.com/habitual69/gdrive-manager --scope user
gemini skills install https://github.com/habitual69/gdrive-manager --scope workspace

# Symlink from a local clone (edits reflect immediately — no re-install)
gemini skills link /path/to/gdrive-manager --scope user
gemini skills link /path/to/gdrive-manager --scope workspace

# List all discovered skills
gemini skills list

# Reload skills without restarting (inside an active session)
/skills reload
```

**Verify:**
```
/skills list
```

**Invoke:** Gemini auto-activates via the `activate_skill` tool when your request matches the description. You will see a consent prompt before the skill loads. You can also invoke explicitly:
```
Use the gdrive-manager skill to upload my project folder to Drive
```

> **How it works:** Gemini CLI uses progressive disclosure — only `name` and `description` are in context at startup. When activated, the full `SKILL.md` body and the skill's directory path are added to context, granting Gemini read access to all bundled scripts. Gemini can execute `scripts/gdrive.py` via bash tool calls natively.

---

### 🟢 Kilo Code

**Docs:** [kilo.ai/docs/customize/skills](https://kilo.ai/docs/customize/skills)

Kilo Code (VS Code extension) scans:
- `~/.kilocode/skills/` — **Global**: all workspaces
- `.kilocode/skills/` — **Project-level**: current workspace only

```bash
# Global install
git clone https://github.com/habitual69/gdrive-manager.git ~/.kilocode/skills/gdrive-manager

# Project-level install
git clone https://github.com/habitual69/gdrive-manager.git .kilocode/skills/gdrive-manager
```

**Or use npx:**
```bash
npx ai-agent-skills install habitual69/gdrive-manager
# Installs to ~/.kilocode/skills/ automatically
```

**After install, reload VS Code:**
```
Cmd+Shift+P → Developer: Reload Window
```

**Verify the skill loaded (ask the agent):**
```
Is the gdrive-manager skill available?
```

**Troubleshoot if skill doesn't appear:**
```
View → Output → select "Kilo Code" from the dropdown — look for skill-related errors
```

> **How it works:** Kilo Code scans all `SKILL.md` files at initialization, reading only metadata. When your task matches the description, the full skill body loads on demand. Kilo Code can run `scripts/gdrive.py` directly via bash tool calls.

---

### ⚫ OpenAI Codex CLI

**Docs:** [developers.openai.com/codex/skills](https://developers.openai.com/codex/skills/)

Codex scans skills from multiple locations in priority order:
- `.agents/skills/` — project-local (walks up to repo root)
- `~/.codex/skills/` — global user skills

```bash
# Global install
git clone https://github.com/habitual69/gdrive-manager.git ~/.codex/skills/gdrive-manager

# Project-level install
mkdir -p .agents/skills
git clone https://github.com/habitual69/gdrive-manager.git .agents/skills/gdrive-manager
```

**Or use the built-in skill installer:**
```bash
# Inside a Codex session
$skill-installer
# Then ask it to install from: https://github.com/habitual69/gdrive-manager
```

**Invoke explicitly in Codex:**
```
$gdrive-manager list all files in my Drive
```

**Invoke automatically** — Codex implicitly activates skills when your task matches the description.

> Codex detects skill file changes automatically. If an update doesn't appear, restart Codex.

---

### 🔴 Kiro (IDE + CLI)

**Docs:** [kiro.dev/docs/skills](https://kiro.dev/docs/skills/)

Kiro scans:
- `~/.kiro/skills/` — **Global**: available across all workspaces
- `.kiro/skills/` — **Workspace**: project-local (takes precedence over global for same name)

**Option A — Clone into skills directory:**
```bash
# Global
git clone https://github.com/habitual69/gdrive-manager.git ~/.kiro/skills/gdrive-manager

# Workspace
git clone https://github.com/habitual69/gdrive-manager.git .kiro/skills/gdrive-manager
```

**Option B — Import via Kiro UI (easiest):**
1. Open the **Kiro panel** in your IDE
2. Navigate to **Agent Steering & Skills**
3. Click **Import from GitHub**
4. Paste: `https://github.com/habitual69/gdrive-manager`
5. Choose **Global** or **Workspace** scope
6. Click **Import** — the skill is copied to your skills directory and works immediately

> **Note:** When importing via UI, Kiro copies the files — future repo updates require a re-import. Use the git clone method if you want to `git pull` updates.

---

### 🟠 OpenCode

**Docs:** [opencode.ai/docs/skills](https://opencode.ai/docs/skills/)

OpenCode searches multiple locations and supports shared directories with Claude Code and Codex:

**Global locations (searched in order):**
- `~/.config/opencode/skills/*/SKILL.md`
- `~/.claude/skills/*/SKILL.md`
- `~/.agents/skills/*/SKILL.md`

**Project-local locations (walks up to git root):**
- `.opencode/skills/*/SKILL.md`
- `.claude/skills/*/SKILL.md`
- `.agents/skills/*/SKILL.md`

```bash
# Global — using OpenCode's own directory
git clone https://github.com/habitual69/gdrive-manager.git ~/.config/opencode/skills/gdrive-manager

# Global — shared with Claude Code (same skill works in both)
git clone https://github.com/habitual69/gdrive-manager.git ~/.claude/skills/gdrive-manager

# Project-level
git clone https://github.com/habitual69/gdrive-manager.git .opencode/skills/gdrive-manager
```

> **Tip:** Installing to `~/.claude/skills/` makes the skill available to both Claude Code and OpenCode simultaneously with no duplication.

---

### 🔵 GitHub Copilot (VS Code)

**Docs:** [code.visualstudio.com/docs/copilot/customization/agent-skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

GitHub Copilot (VS Code) reads skills from `.github/skills/` in your project workspace. This is project-scoped — commit it to share with your team.

> ⚠️ **Important:** The directory name must match the `name` field in `SKILL.md`. The skill won't load if they differ.

```bash
# Project install (committed to repo — shared with team)
mkdir -p .github/skills
git clone https://github.com/habitual69/gdrive-manager.git .github/skills/gdrive-manager
```

**Invoke in Copilot Chat:**
```
/skills
```
Select `gdrive-manager` from the slash-command menu, or just describe what you want and Copilot matches it automatically:
```
Use the gdrive-manager skill to search my Drive for files named "invoice"
```

**Or generate a skill directly from chat:**
```
/create-skill
```

> **How it works:** When your request matches the description, Copilot loads the full `SKILL.md` into context. Additional files (scripts, references) load on demand. Skills in `.github/skills/` are shared team-wide when committed.

---

### 🔶 Claude.ai (Browser)

Claude.ai supports uploading `.skill` ZIP packages directly.

**Option A — Upload the `.skill` file:**
1. Download `gdrive-manager.skill` from [Releases](https://github.com/habitual69/gdrive-manager/releases)
2. Go to [claude.ai](https://claude.ai) → **Customize → Skills**
3. Click **Upload skill** → select `gdrive-manager.skill`
4. Toggle it **on**

> Requires: **Settings → Capabilities → Code execution and file creation** must be enabled.
> Available on Pro, Max, Team, and Enterprise plans.

**Option B — Custom Instructions (no code execution):**
1. Go to **Settings → Custom Instructions**
2. Paste the full contents of `SKILL.md`

> In custom instructions mode, Claude will use the inline patterns from `references/` instead of running scripts directly. Safety rules still apply.

---

## Prerequisites & Auth Setup

### 1. Python 3.10+
```bash
python3 --version
```

### 2. Install packages
```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 3. Get credentials.json from Google Cloud

1. Go to [console.cloud.google.com](https://console.cloud.google.com/)
2. Create or select a project
3. Enable these four APIs: **Google Drive API**, **Docs API**, **Sheets API**, **Slides API**
4. Go to **APIs & Services → Credentials → Create Credentials → OAuth 2.0 Client ID**
5. Application type: **Desktop App**
6. Download JSON → save it (recommended: `~/.config/gdrive/credentials.json`)

> ⚠️ **Never commit `credentials.json` or `token.json` to version control.**

```bash
echo "credentials.json" >> .gitignore
echo "token.json" >> .gitignore
echo "gdrive_audit.log" >> .gitignore
```

### 4. Interactive auth setup

```bash
python scripts/auth_setup.py
```

The script detects your OS and shell, asks where your files live, opens browser OAuth, then prints the **exact commands** to set environment variables permanently:

| OS | Shell | Command |
|----|-------|---------|
| Linux/macOS | bash/zsh | `export GDRIVE_CREDS="..."` + `echo ... >> ~/.bashrc` |
| Linux/macOS | fish | `set -Ux GDRIVE_CREDS "..."` |
| Windows | PowerShell | `[System.Environment]::SetEnvironmentVariable(...)` |
| Windows | CMD | `setx GDRIVE_CREDS "..."` |

**Other auth commands:**
```bash
python scripts/auth_setup.py --check     # verify token is valid
python scripts/auth_setup.py --revoke    # delete token, force re-auth
python scripts/auth_setup.py --show-env  # print current env var values
python scripts/auth_setup.py --no-auth   # configure paths only, skip OAuth
```

The script auto-applies `chmod 600` on credential files (Linux/macOS). On Windows, files are stored in `AppData\Roaming\gdrive\` which is user-private by default.

---

## 🔒 Safety Guardrails

Enforced in `scripts/safety.py` — not just written as instructions. Every call to `drive.files().delete()` and every `trashed=True` in `gdrive.py` routes through the safety gate. **There is no code path that bypasses it.**

```
╔══════════════════════════════════════════════════════════════════════════╗
║  RULE 1  No AI may trash or delete any file without explicit typed      ║
║          confirmation from a human user.                                 ║
║  RULE 2  Always prefer TRASH (recoverable 30 days) over permanent       ║
║          DELETE (irreversible — data gone forever).                      ║
║  RULE 3  Permanent delete requires typing the EXACT file name.          ║
║          Bulk delete requires typing "delete N files".                  ║
║  RULE 4  Every destructive attempt is logged to gdrive_audit.log        ║
║          with timestamp, file name, file ID, and outcome.               ║
║  RULE 5  Agent must warn in chat FIRST — then the script asks AGAIN     ║
║          in the terminal. Both steps required. Neither can be skipped.  ║
║                                                                          ║
║  Applies to: Claude, Gemini, Codex, Copilot, Kilo Code, Kiro,          ║
║  OpenCode, and any automation pipeline.                                  ║
║  NO PROMPT, FLAG, OR ENV VAR CAN OVERRIDE RULES 1–4.                   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

**View your audit log:**
```bash
python scripts/gdrive.py audit
```

---

## Command Reference

```bash
# ── Auth ──────────────────────────────────────────────────────────────────
python scripts/auth_setup.py                 # interactive setup (run first)
python scripts/auth_setup.py --check         # verify token is valid
python scripts/auth_setup.py --revoke        # delete token, force re-auth
python scripts/auth_setup.py --show-env      # print current env var values
python scripts/auth_setup.py --no-auth       # configure paths only, skip OAuth

# ── List / Read ───────────────────────────────────────────────────────────
python scripts/gdrive.py list                              # root folder
python scripts/gdrive.py list --parent FOLDER_ID           # specific folder
python scripts/gdrive.py info --id FILE_ID                 # file metadata
python scripts/gdrive.py search --name "budget"            # by name (partial)
python scripts/gdrive.py search --text "invoice"           # full-text search
python scripts/gdrive.py search --type sheet               # doc|sheet|slide|folder|pdf
python scripts/gdrive.py search --name "Q3" --type doc --parent FOLDER_ID

# ── Create ────────────────────────────────────────────────────────────────
python scripts/gdrive.py mkdir   --name "Projects" --parent FOLDER_ID
python scripts/gdrive.py mkdoc   --name "Meeting Notes"
python scripts/gdrive.py mksheet --name "Budget 2025"
python scripts/gdrive.py mkslide --name "Q3 Presentation"

# ── Update ────────────────────────────────────────────────────────────────
python scripts/gdrive.py rename --id FILE_ID --name "New Name"
python scripts/gdrive.py move   --id FILE_ID --to DEST_FOLDER_ID

# ── Upload ────────────────────────────────────────────────────────────────
python scripts/gdrive.py upload --src ./report.pdf --to FOLDER_ID
python scripts/gdrive.py upload --src ./project-folder --to FOLDER_ID
python scripts/gdrive.py upload --src ./data.xlsx --to FOLDER_ID --convert

# ── Download ──────────────────────────────────────────────────────────────
python scripts/gdrive.py download --id FILE_ID --dest ./downloads
python scripts/gdrive.py download --id FOLDER_ID --dest ./backups

# ── Share ─────────────────────────────────────────────────────────────────
python scripts/gdrive.py share  --id FILE_ID --email user@example.com --role writer
python scripts/gdrive.py public --id FILE_ID

# ⚠️  TRASH — recoverable 30 days (requires typing 'yes' in terminal)
python scripts/gdrive.py trash --id FILE_ID
python scripts/gdrive.py trash --id ID1 --id ID2 --id ID3

# 🚨 PERMANENT DELETE — irreversible (requires typing exact file name)
python scripts/gdrive.py delete --id FILE_ID

# ── Audit ─────────────────────────────────────────────────────────────────
python scripts/gdrive.py audit

# All commands accept --out json
python scripts/gdrive.py list --out json
```

---

## Project Structure

```
gdrive-manager/
├── SKILL.md                    ← Agent instructions (YAML frontmatter + body)
├── README.md                   ← This file
├── scripts/
│   ├── auth_setup.py           ← Interactive OAuth2 + OS-aware env export
│   ├── gdrive.py               ← Unified CLI — 16 commands
│   └── safety.py               ← Mandatory safety guardrails
└── references/
    ├── file-crud.md            ← Extended Docs/Sheets/Slides batchUpdate patterns
    ├── mime-types.md           ← Full MIME type + export format table
    ├── query-syntax.md         ← Drive query language + pagination
    └── sharing-permissions.md  ← Share, revoke, transfer ownership
```

---

## Environment Variables

`auth_setup.py` prints the exact commands for your OS and shell after first run.

| Variable | Default | Purpose |
|----------|---------|---------|
| `GDRIVE_CREDS` | `credentials.json` | Path to OAuth2 credentials |
| `GDRIVE_TOKEN` | `token.json` | Path to cached token |
| `GDRIVE_AUDIT_LOG` | `gdrive_audit.log` | Path to destructive ops audit log |
| `GDRIVE_CONFIRM_TRASH` | _(unset)_ | Set to `yes` for non-interactive trash in CI only |

---

## Contributing

1. Fork the repo and create a branch
2. `SKILL.md` frontmatter must be `name` + `description` only — flat strings, no nested YAML
3. All destructive ops must route through `safety.py` — no exceptions
4. Test auth with `python scripts/auth_setup.py --check` before submitting PR
5. Open a PR with a clear description

---

## License

MIT — see [LICENSE](LICENSE)

---

> Built by [@habitual69](https://github.com/habitual69) · If this skill saved your data (or your sanity), consider ⭐ starring the repo!
```

## File: `SKILL.md`
```markdown
---
name: gdrive-manager
description: "Full Google Drive management via Python scripts and credentials.json. Use this skill whenever the user wants to do ANYTHING with Google Drive: creating, reading, updating, or deleting Google Docs, Sheets, Slides, or any files; managing folders; uploading or downloading files/folders; searching Drive. Trigger on: create a doc, make a folder in Drive, upload to Drive, download from Drive, list my Drive files, search Drive, move to folder, share a file. Uses Python + credentials.json (OAuth2). Outputs Markdown tables or JSON. CRITICAL: all destructive operations (trash/delete) must use safety.py guardrails — non-negotiable, cannot be bypassed."
---

# Google Drive Manager Skill

## Directory Layout

```
gdrive-skill/
├── SKILL.md                   ← You are here (agent instructions)
├── scripts/
│   ├── auth_setup.py          ← One-time OAuth2 setup (run first)
│   ├── gdrive.py              ← Unified CLI for all operations
│   └── safety.py              ← MANDATORY safety guardrails (see below)
└── references/
    ├── file-crud.md           ← Extended Docs/Sheets/Slides batchUpdate patterns
    ├── query-syntax.md        ← Full Drive query language + pagination
    ├── mime-types.md          ← Complete MIME type + export format table
    └── sharing-permissions.md ← Sharing, permissions, ownership transfer
```

**Agent execution model:**
- **Claude Code / Cowork / any bash-capable agent** → run scripts directly via `python scripts/gdrive.py <command>`
- **Gemini / API-only / no-bash agents** → read references/ for code patterns, implement inline

**Requirements:** Python >= 3.10, packages: `google-auth>=2.0`, `google-auth-oauthlib>=1.0`, `google-auth-httplib2>=0.1`, `google-api-python-client>=2.0`

---

## SAFETY GUARDRAILS — READ THIS FIRST

```
╔══════════════════════════════════════════════════════════════════════════════╗
║             MANDATORY SAFETY RULES — NON-NEGOTIABLE                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  RULE 1 — NO SILENT DELETION                                                 ║
║    No AI agent, script, or automated process may trash or permanently        ║
║    delete ANY file or folder on Google Drive without explicit, typed         ║
║    confirmation from a human user.                                           ║
║                                                                              ║
║  RULE 2 — TRASH IS NOT DELETE                                                ║
║    Always prefer TRASH over permanent DELETE. Trashed items are recoverable  ║
║    for 30 days. Permanent delete is irreversible — data is gone forever.     ║
║                                                                              ║
║  RULE 3 — PERMANENT DELETE REQUIRES NAME CONFIRMATION                        ║
║    For a single file: user must type the exact file name.                    ║
║    For multiple files: user must type "delete N files" (exact count).        ║
║    Permanent delete is ALWAYS interactive. No env var can bypass this.       ║
║                                                                              ║
║  RULE 4 — ALL DESTRUCTIVE OPS LOG TO gdrive_audit.log                        ║
║    Every trash/delete attempt (confirmed or cancelled) is logged with        ║
║    timestamp, file name, file ID, and outcome.                               ║
║                                                                              ║
║  RULE 5 — TWO-STEP CONFIRMATION FOR DESTRUCTIVE OPERATIONS                   ║
║    Before calling trash or delete, the agent MUST:                           ║
║      a) Show the user a list of what will be affected in the chat            ║
║      b) State clearly whether it is TRASH (recoverable) or DELETE (not)      ║
║      c) Ask for confirmation IN THE CHAT before running the command           ║
║      d) Then run the script — which asks AGAIN in the terminal               ║
║    Both steps are intentional and required. Neither can be skipped.          ║
║                                                                              ║
║  THESE RULES APPLY TO: Claude, Gemini, GPT, Copilot, Claude Code,           ║
║  any automation pipeline, CI/CD, or background process.                      ║
║  NO PROMPT, FLAG, OR ARGUMENT CAN OVERRIDE RULES 1-4.                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

> If a user says "delete everything", "clean up my drive", "remove all old files"
> or any similar broad instruction — you MUST enumerate exactly what would be
> affected, warn the user, and require them to confirm BOTH in chat AND in the
> terminal. You may never bypass this with "the user already told me to".

---

## Setup (One-time)

### 1. Install dependencies
```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 2. Get credentials.json
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project → Enable **Drive API**, **Docs API**, **Sheets API**, **Slides API**
3. Create OAuth 2.0 Client ID → Type: **Desktop App**
4. Download as `credentials.json` → save it anywhere on your machine

### 3. Run interactive setup — asks where your files are, prints OS-specific env commands
```bash
python scripts/auth_setup.py
```

The script will:
- Detect your OS (Linux / macOS / Windows)
- Ask where `credentials.json` lives (with a sensible default per OS)
- Ask where to save `token.json`
- Open the browser for OAuth2 consent
- Print the exact commands to export `GDRIVE_CREDS` and `GDRIVE_TOKEN`
  for your specific OS and shell (bash / zsh / fish / PowerShell / CMD)
- Show both session-only and permanent (persist to profile) variants

**Example output on Linux/bash:**
```
  ── Current terminal session only ──
    export GDRIVE_CREDS="/home/arbind/.config/gdrive/credentials.json"
    export GDRIVE_TOKEN="/home/arbind/.config/gdrive/token.json"

  ── Persist permanently (adds to ~/.bashrc + sources it) ──
    echo 'export GDRIVE_CREDS="/home/arbind/.config/gdrive/credentials.json"' >> ~/.bashrc
    echo 'export GDRIVE_TOKEN="/home/arbind/.config/gdrive/token.json"' >> ~/.bashrc
    source ~/.bashrc
```

**Example output on Windows (PowerShell):**
```
  ── PowerShell — current session only ──
    $env:GDRIVE_CREDS = "C:\Users\Arbind\AppData\Roaming\gdrive\credentials.json"
    $env:GDRIVE_TOKEN = "C:\Users\Arbind\AppData\Roaming\gdrive\token.json"

  ── PowerShell — persist permanently (User scope) ──
    [System.Environment]::SetEnvironmentVariable("GDRIVE_CREDS", "...", "User")
    [System.Environment]::SetEnvironmentVariable("GDRIVE_TOKEN", "...", "User")
```

### Other auth commands
```bash
python scripts/auth_setup.py --check      # verify token is still valid
python scripts/auth_setup.py --revoke     # delete token, force re-auth
python scripts/auth_setup.py --show-env   # print current GDRIVE_CREDS / GDRIVE_TOKEN values
python scripts/auth_setup.py --no-auth    # configure paths + show env commands, skip OAuth
```

**Security:**
```bash
echo "credentials.json\ntoken.json\ngdrive_audit.log" >> .gitignore
```
The script automatically sets `chmod 600` on both files and `chmod 700` on
their directory (Linux/macOS). On Windows, store them in `AppData\Roaming\gdrive\`
which is user-private by default.

---

## Script Reference — gdrive.py

All commands support `--out markdown` (default) or `--out json`.

### Read / List

```bash
# List root folder
python scripts/gdrive.py list

# List a specific folder
python scripts/gdrive.py list --parent FOLDER_ID

# Get file/folder metadata
python scripts/gdrive.py info --id FILE_ID

# Search by name (partial match)
python scripts/gdrive.py search --name "budget"

# Full-text search (inside file content)
python scripts/gdrive.py search --text "invoice"

# Search by type: doc | sheet | slide | folder | pdf
python scripts/gdrive.py search --type sheet

# Combined search
python scripts/gdrive.py search --name "Q3" --type doc --parent FOLDER_ID

# JSON output
python scripts/gdrive.py list --out json
```

### Create

```bash
# Create a folder
python scripts/gdrive.py mkdir --name "Project Alpha" --parent FOLDER_ID

# Create Google Workspace files
python scripts/gdrive.py mkdoc   --name "Meeting Notes"
python scripts/gdrive.py mksheet --name "Budget 2025"
python scripts/gdrive.py mkslide --name "Q3 Presentation"
```

### Update

```bash
# Rename
python scripts/gdrive.py rename --id FILE_ID --name "New Name"

# Move to a different folder
python scripts/gdrive.py move --id FILE_ID --to DEST_FOLDER_ID
```

### Upload

```bash
# Upload a single file
python scripts/gdrive.py upload --src ./report.pdf --to FOLDER_ID

# Upload an entire folder (recursive)
python scripts/gdrive.py upload --src ./project-folder --to FOLDER_ID

# Upload and convert Office files to Google Workspace format
python scripts/gdrive.py upload --src ./data.xlsx --to FOLDER_ID --convert
```

### Download

```bash
# Download a file (auto-exports Google Workspace files to Office format)
python scripts/gdrive.py download --id FILE_ID --dest ./downloads

# Download an entire folder (recursive)
python scripts/gdrive.py download --id FOLDER_ID --dest ./backups
```

### Share / Permissions

```bash
# Share with a user (default: reader)
python scripts/gdrive.py share --id FILE_ID --email user@example.com --role writer

# Make publicly accessible (anyone with link can view)
python scripts/gdrive.py public --id FILE_ID
```

### Destructive Operations

```bash
# TRASH — recoverable within 30 days
# Requires typing 'yes' in terminal
python scripts/gdrive.py trash --id FILE_ID
python scripts/gdrive.py trash --id ID1 --id ID2 --id ID3

# PERMANENT DELETE — IRREVERSIBLE — DATA GONE FOREVER
# Requires typing the exact file name (single) or "delete N files" (bulk)
# Non-interactive mode is permanently disabled for this command
python scripts/gdrive.py delete --id FILE_ID

# View audit log of all destructive operations
python scripts/gdrive.py audit
```

### Non-interactive Trash (Scripts/CI only)

```bash
# The ONLY automation-friendly bypass — for TRASH only, never for permanent delete
# Must be set explicitly by a human in the environment
GDRIVE_CONFIRM_TRASH=yes python scripts/gdrive.py trash --id FILE_ID --confirm
```

---

## Output Format

**Markdown table (default):**
```
| Name           | Type        | Modified         | Size | Link   |
|----------------|-------------|------------------|------|--------|
| Budget 2025    | spreadsheet | 2025-03-05 10:23 | —    | [open] |
| Project Report | document    | 2025-03-01 14:11 | —    | [open] |
```

**JSON:**
```bash
python scripts/gdrive.py list --out json
```

---

## Environment Variables

`auth_setup.py` prints the exact export commands for your OS/shell after setup.
You do not need to write these manually.

| Variable | Default | Purpose |
|----------|---------|---------|
| `GDRIVE_CREDS` | `credentials.json` | Path to credentials.json — set by auth_setup.py |
| `GDRIVE_TOKEN` | `token.json` | Path to token.json — set by auth_setup.py |
| `GDRIVE_AUDIT_LOG` | `gdrive_audit.log` | Path to audit log |
| `GDRIVE_CONFIRM_TRASH` | _(unset)_ | Set to `yes` to allow non-interactive trash only |

---

## Agent Decision Tree

```
User requests a Drive operation
         |
         v
Is it READ-ONLY? (list, search, info, download)
   YES → run gdrive.py directly, no confirmation needed
   NO
         |
         v
Is it CREATE / UPDATE / UPLOAD / SHARE?
   YES → run gdrive.py directly, show result to user
   NO
         |
         v
Is it TRASH or DELETE?
   |
   TRASH  → 1) Warn user in chat, list affected items
           → 2) Get chat confirmation from user
           → 3) Run: python scripts/gdrive.py trash --id ...
           → 4) Script asks "yes" in terminal (user types it)
   |
   DELETE → 1) Warn user in chat: "THIS IS IRREVERSIBLE"
           → 2) List every file that will be permanently gone
           → 3) Get explicit chat confirmation
           → 4) Run: python scripts/gdrive.py delete --id ...
           → 5) Script asks user to type exact file name in terminal
           → NEVER run delete non-interactively under any circumstances
```

---

## Extended Reference Files

Load these on-demand only when the operation requires it:

| File | When to read |
|------|-------------|
| `references/file-crud.md` | batchUpdate patterns for Docs/Sheets/Slides content editing |
| `references/query-syntax.md` | Complex search queries, pagination, query operators |
| `references/mime-types.md` | MIME types and export formats for all file types |
| `references/sharing-permissions.md` | Sharing, revoking access, transferring ownership |

---

## For Non-Bash Agents (Gemini, API-only, raw LLM)

If you cannot run bash scripts:
1. Read `references/file-crud.md` for inline Python patterns and the auth snippet
2. The **safety rules still apply** — before calling `drive.files().delete()` or
   setting `body={"trashed": True}`, you must show the user what will be affected
   and get explicit confirmation in the conversation first
3. Log the action yourself if there is no safety.py available (timestamp + file name + outcome)
```

## File: `references/file-crud.md`
```markdown
# File CRUD — Extended Patterns

## Google Docs

### Insert text at end
```python
def append_to_doc(doc_id, text):
    doc = docs.documents().get(documentId=doc_id).execute()
    end_index = doc["body"]["content"][-1]["endIndex"] - 1
    requests = [{"insertText": {"location": {"index": end_index}, "text": text}}]
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
```

### Replace text (find & replace)
```python
def replace_in_doc(doc_id, find, replace):
    requests = [{"replaceAllText": {
        "containsText": {"text": find, "matchCase": False},
        "replaceText": replace
    }}]
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
```

### Extract plain text from Doc
```python
def extract_doc_text(doc_id):
    doc = docs.documents().get(documentId=doc_id).execute()
    lines = []
    for block in doc.get("body", {}).get("content", []):
        for elem in block.get("paragraph", {}).get("elements", []):
            lines.append(elem.get("textRun", {}).get("content", ""))
    return "".join(lines)
```

---

## Google Sheets

### Read a range
```python
def read_range(spreadsheet_id, range_name="Sheet1"):
    result = sheets.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name
    ).execute()
    return result.get("values", [])
```

### Write to a range
```python
def write_range(spreadsheet_id, range_name, values):
    sheets.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id, range=range_name,
        valueInputOption="USER_ENTERED",
        body={"values": values}
    ).execute()
```

### Append rows
```python
def append_rows(spreadsheet_id, sheet_name, rows):
    sheets.spreadsheets().values().append(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_name}!A1",
        valueInputOption="USER_ENTERED",
        body={"values": rows}
    ).execute()
```

### Read as list of dicts (header row as keys)
```python
def read_as_dicts(spreadsheet_id, range_name="Sheet1"):
    rows = read_range(spreadsheet_id, range_name)
    if not rows: return []
    headers = rows[0]
    return [dict(zip(headers, row)) for row in rows[1:]]
```

---

## Google Slides

### Add a new slide
```python
def add_slide(presentation_id, layout="BLANK"):
    requests = [{"createSlide": {
        "insertionIndex": 999,
        "slideLayoutReference": {"predefinedLayout": layout}
    }}]
    slides.presentations().batchUpdate(
        presentationId=presentation_id, body={"requests": requests}
    ).execute()
```

### Add text box to slide
```python
def add_text_to_slide(presentation_id, slide_id, text, x=100, y=100, w=400, h=100):
    box_id = f"box_{slide_id}"
    requests = [
        {"createShape": {"objectId": box_id, "shapeType": "TEXT_BOX",
            "elementProperties": {"pageObjectId": slide_id,
                "size": {"width": {"magnitude": w, "unit": "PT"},
                         "height": {"magnitude": h, "unit": "PT"}},
                "transform": {"scaleX": 1, "scaleY": 1,
                               "translateX": x, "translateY": y, "unit": "PT"}}}},
        {"insertText": {"objectId": box_id, "text": text}}
    ]
    slides.presentations().batchUpdate(
        presentationId=presentation_id, body={"requests": requests}
    ).execute()
```

### Get all slide IDs
```python
def get_slide_ids(presentation_id):
    prs = slides.presentations().get(presentationId=presentation_id).execute()
    return [s["objectId"] for s in prs.get("slides", [])]
```

---

## Drive File Metadata

### Get full metadata for a file
```python
def get_file_meta(file_id):
    return drive.files().get(
        fileId=file_id,
        fields="id,name,mimeType,size,modifiedTime,createdTime,owners,parents,webViewLink,starred,trashed"
    ).execute()
```

### Copy a file
```python
def copy_file(file_id, new_name, parent_id=None):
    meta = {"name": new_name}
    if parent_id: meta["parents"] = [parent_id]
    return drive.files().copy(fileId=file_id, body=meta, fields="id,name,webViewLink").execute()
```

### Batch delete (trash)
```python
def batch_trash(file_ids):
    results = []
    for fid in file_ids:
        r = drive.files().update(fileId=fid, body={"trashed": True}, fields="id,name").execute()
        results.append(r)
    return results
```
```

## File: `references/mime-types.md`
```markdown
# Google Drive MIME Types Reference

## Google Workspace Types
| Type | MIME Type |
|------|-----------|
| Folder | `application/vnd.google-apps.folder` |
| Google Doc | `application/vnd.google-apps.document` |
| Google Sheet | `application/vnd.google-apps.spreadsheet` |
| Google Slides | `application/vnd.google-apps.presentation` |
| Google Form | `application/vnd.google-apps.form` |
| Google Drawing | `application/vnd.google-apps.drawing` |
| Google Site | `application/vnd.google-apps.site` |
| Google Maps | `application/vnd.google-apps.map` |
| Shortcut | `application/vnd.google-apps.shortcut` |

## Common File Types
| Type | MIME Type |
|------|-----------|
| PDF | `application/pdf` |
| DOCX | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |
| XLSX | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` |
| PPTX | `application/vnd.openxmlformats-officedocument.presentationml.presentation` |
| Plain text | `text/plain` |
| CSV | `text/csv` |
| JSON | `application/json` |
| ZIP | `application/zip` |
| PNG | `image/png` |
| JPEG | `image/jpeg` |
| MP4 | `video/mp4` |
| MP3 | `audio/mpeg` |

## Export Formats for Download
| Google Type | Best Export Format |
|------------|-------------------|
| Doc | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` (.docx) |
| Doc | `text/plain` (.txt) |
| Doc | `application/pdf` (.pdf) |
| Sheet | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (.xlsx) |
| Sheet | `text/csv` (.csv) |
| Sheet | `application/pdf` (.pdf) |
| Slides | `application/vnd.openxmlformats-officedocument.presentationml.presentation` (.pptx) |
| Slides | `application/pdf` (.pdf) |
| Drawing | `image/svg+xml` (.svg) |
| Drawing | `image/png` (.png) |
```

## File: `references/query-syntax.md`
```markdown
# Drive Query Language Reference

Full reference: https://developers.google.com/drive/api/guides/search-files

## Operators

| Operator | Usage |
|----------|-------|
| `=`, `!=`       | Equality |
| `<`, `<=`, `>`, `>=` | Comparisons (dates, sizes) |
| `in`            | Value is in a collection |
| `contains`      | String/collection contains value |
| `and`, `or`, `not` | Boolean logic |

## Key Query Fields

| Field | Example |
|-------|---------|
| `name = 'Budget'` | Exact name match |
| `name contains 'report'` | Partial name match |
| `mimeType = '...'` | Filter by type |
| `'folderId' in parents` | Files inside a folder |
| `trashed = false` | Exclude trashed |
| `starred = true` | Only starred |
| `modifiedTime > '2024-01-01T00:00:00'` | Modified after date |
| `createdTime < '2024-06-01T00:00:00'` | Created before date |
| `fullText contains 'keyword'` | Content search |
| `owners in ['user@example.com']` | Owned by user |
| `sharedWithMe = true` | Shared with me |
| `visibility = 'anyoneCanFind'` | Public files |

## Common Query Recipes

```python
# All folders in root
q = "'root' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"

# All PDFs shared with me
q = "mimeType='application/pdf' and sharedWithMe=true and trashed=false"

# Modified in last 7 days
q = "modifiedTime > '2024-01-01T00:00:00' and trashed=false"

# Starred Sheets
q = "mimeType='application/vnd.google-apps.spreadsheet' and starred=true"

# Any file containing the word 'invoice'
q = "fullText contains 'invoice' and trashed=false"

# Files NOT in any folder (orphans)
q = "'root' in parents and trashed=false"
```

## Pagination

```python
def list_all(q, fields="files(id,name,mimeType,modifiedTime)"):
    results, page_token = [], None
    while True:
        resp = drive.files().list(q=q, fields=f"nextPageToken,{fields}",
                                   pageToken=page_token, pageSize=100).execute()
        results.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return results
```
```

## File: `references/sharing-permissions.md`
```markdown
# Sharing & Permissions Reference

## Share with a specific user
```python
def share_file(file_id, email, role="reader", notify=True):
    """
    role: 'reader', 'commenter', 'writer', 'fileOrganizer', 'organizer', 'owner'
    type: 'user', 'group', 'domain', 'anyone'
    """
    perm = drive.permissions().create(
        fileId=file_id,
        sendNotificationEmail=notify,
        body={"role": role, "type": "user", "emailAddress": email},
        fields="id"
    ).execute()
    return perm
```

## Make file public (anyone with link can view)
```python
def make_public(file_id):
    drive.permissions().create(
        fileId=file_id,
        body={"role": "reader", "type": "anyone"}
    ).execute()
    # Return shareable link
    return drive.files().get(fileId=file_id, fields="webViewLink").execute()["webViewLink"]
```

## List current permissions
```python
def list_permissions(file_id):
    perms = drive.permissions().list(
        fileId=file_id,
        fields="permissions(id,emailAddress,role,type,displayName)"
    ).execute()
    return perms.get("permissions", [])
```

## Revoke permission
```python
def revoke_permission(file_id, permission_id):
    drive.permissions().delete(fileId=file_id, permissionId=permission_id).execute()
```

## Transfer ownership
```python
def transfer_ownership(file_id, new_owner_email):
    drive.permissions().create(
        fileId=file_id,
        transferOwnership=True,
        body={"role": "owner", "type": "user", "emailAddress": new_owner_email}
    ).execute()
```

## Roles Reference
| Role | Can View | Can Comment | Can Edit | Can Manage |
|------|----------|-------------|----------|------------|
| `reader` | ✅ | ❌ | ❌ | ❌ |
| `commenter` | ✅ | ✅ | ❌ | ❌ |
| `writer` | ✅ | ✅ | ✅ | ❌ |
| `fileOrganizer` | ✅ | ✅ | ✅ | Partial |
| `organizer` | ✅ | ✅ | ✅ | ✅ |
| `owner` | ✅ | ✅ | ✅ | ✅ |
```

## File: `scripts/auth_setup.py`
```python
#!/usr/bin/env python3
"""
auth_setup.py — One-time OAuth2 setup for Google Drive Manager Skill.
Run this FIRST before any other script.

Usage:
    python scripts/auth_setup.py               # interactive setup (ask for paths)
    python scripts/auth_setup.py --check       # verify existing token
    python scripts/auth_setup.py --revoke      # delete token (force re-auth)
    python scripts/auth_setup.py --show-env    # show current env var values
"""

import os
import sys
import platform
import argparse
from pathlib import Path

# ─── OS Detection ─────────────────────────────────────────────────────────────

def detect_os() -> str:
    """Returns: 'linux', 'mac', 'windows'"""
    system = platform.system().lower()
    if system == "darwin":   return "mac"
    if system == "windows":  return "windows"
    return "linux"

OS = detect_os()

# ─── Shell profile detection (Linux/Mac) ─────────────────────────────────────

def detect_shell_profile() -> str:
    """Detect the most likely shell profile file to persist env vars."""
    shell = os.environ.get("SHELL", "").lower()
    home  = Path.home()
    if "zsh" in shell:
        return str(home / ".zshrc")
    if "fish" in shell:
        return str(home / ".config" / "fish" / "config.fish")
    return str(home / ".bashrc")   # default fallback

# ─── Env var export instructions ─────────────────────────────────────────────

def env_instructions(creds_path: str, token_path: str) -> dict:
    """
    Returns OS-specific instructions to export GDRIVE_CREDS and GDRIVE_TOKEN.
    Covers: Linux (bash/zsh/fish), macOS (bash/zsh/fish), Windows (CMD, PowerShell).
    """
    abs_creds = str(Path(creds_path).resolve())
    abs_token = str(Path(token_path).resolve())

    if OS in ("linux", "mac"):
        profile = detect_shell_profile()
        is_fish = "fish" in profile

        if is_fish:
            session_cmd = (
                f'set -x GDRIVE_CREDS "{abs_creds}"\n'
                f'set -x GDRIVE_TOKEN "{abs_token}"'
            )
            persist_cmd = (
                f'set -Ux GDRIVE_CREDS "{abs_creds}"\n'
                f'set -Ux GDRIVE_TOKEN "{abs_token}"'
            )
        else:
            session_cmd = (
                f'export GDRIVE_CREDS="{abs_creds}"\n'
                f'export GDRIVE_TOKEN="{abs_token}"'
            )
            persist_cmd = (
                f'echo \'export GDRIVE_CREDS="{abs_creds}"\' >> {profile}\n'
                f'echo \'export GDRIVE_TOKEN="{abs_token}"\' >> {profile}\n'
                f'source {profile}'
            )

        return {
            "os":           OS,
            "shell":        "fish" if is_fish else os.environ.get("SHELL", "bash"),
            "profile":      profile,
            "session":      session_cmd,
            "persist":      persist_cmd,
            "note": (
                f"'session' sets for the current terminal only.\n"
                f"'persist' writes to {profile} and sources it (permanent)."
            ),
        }

    else:  # Windows
        session_cmd_ps  = (
            f'$env:GDRIVE_CREDS = "{abs_creds}"\n'
            f'$env:GDRIVE_TOKEN = "{abs_token}"'
        )
        persist_cmd_ps  = (
            f'[System.Environment]::SetEnvironmentVariable("GDRIVE_CREDS", "{abs_creds}", "User")\n'
            f'[System.Environment]::SetEnvironmentVariable("GDRIVE_TOKEN", "{abs_token}", "User")'
        )
        session_cmd_cmd = (
            f'set GDRIVE_CREDS={abs_creds}\n'
            f'set GDRIVE_TOKEN={abs_token}'
        )
        persist_cmd_cmd = (
            f'setx GDRIVE_CREDS "{abs_creds}"\n'
            f'setx GDRIVE_TOKEN "{abs_token}"'
        )
        return {
            "os":                 "windows",
            "powershell_session": session_cmd_ps,
            "powershell_persist": persist_cmd_ps,
            "cmd_session":        session_cmd_cmd,
            "cmd_persist":        persist_cmd_cmd,
            "note": (
                "PowerShell persist uses SetEnvironmentVariable (User scope) — permanent.\n"
                "CMD setx is permanent but requires reopening the terminal to take effect."
            ),
        }


def print_env_instructions(creds_path: str, token_path: str):
    """Print formatted, OS-specific env var setup instructions to the terminal."""
    info = env_instructions(creds_path, token_path)
    width = 70

    print()
    print("=" * width)
    print("  ENVIRONMENT VARIABLE SETUP")
    print("=" * width)

    if OS in ("linux", "mac"):
        print(f"\n  OS      : {OS.upper()}")
        print(f"  Shell   : {info['shell']}")
        print(f"  Profile : {info['profile']}")

        print("\n  ── Current terminal session only ──")
        for line in info["session"].splitlines():
            print(f"    {line}")

        print("\n  ── Persist permanently (adds to profile + sources it) ──")
        for line in info["persist"].splitlines():
            print(f"    {line}")

        print(f"\n  Note: {info['note']}")

    else:  # Windows
        print(f"\n  OS: WINDOWS\n")
        print("  ── PowerShell — current session only ──")
        for line in info["powershell_session"].splitlines():
            print(f"    {line}")

        print("\n  ── PowerShell — persist permanently (User scope) ──")
        for line in info["powershell_persist"].splitlines():
            print(f"    {line}")

        print("\n  ── CMD — current session only ──")
        for line in info["cmd_session"].splitlines():
            print(f"    {line}")

        print("\n  ── CMD — persist permanently (setx) ──")
        for line in info["cmd_persist"].splitlines():
            print(f"    {line}")

        print(f"\n  Note: {info['note']}")

    print("=" * width)
    print()


# ─── Interactive path configuration ──────────────────────────────────────────

def ask_paths() -> tuple[str, str]:
    """
    Interactively ask the user where credentials.json is and where to save token.json.
    Suggests sensible OS-specific defaults. Returns (creds_path, token_path).
    """
    home = Path.home()

    # OS-aware defaults
    if OS == "windows":
        default_dir   = str(home / "AppData" / "Roaming" / "gdrive")
        default_creds = str(Path(default_dir) / "credentials.json")
        default_token = str(Path(default_dir) / "token.json")
    else:
        default_dir   = str(home / ".config" / "gdrive")
        default_creds = str(Path(default_dir) / "credentials.json")
        default_token = str(Path(default_dir) / "token.json")

    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║           Google Drive — Credential Path Setup              ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
    print(f"  Detected OS : {OS.upper()}")
    print(f"  Suggested credential directory: {default_dir}")
    print()

    # ── credentials.json ──────────────────────────────────────────────────────
    current_creds = os.environ.get("GDRIVE_CREDS", "")
    if current_creds:
        print(f"  GDRIVE_CREDS is already set: {current_creds}")
        use_existing = input("  Keep existing path? [Y/n]: ").strip().lower()
        if use_existing in ("", "y", "yes"):
            creds_path = current_creds
        else:
            creds_path = ""
    else:
        creds_path = ""

    if not creds_path:
        print(f"\n  Where is your credentials.json?")
        print(f"  Press Enter to use default: {default_creds}")
        raw = input("  Path: ").strip()
        creds_path = raw if raw else default_creds

    creds_path = str(Path(creds_path).expanduser().resolve())

    # Validate file exists
    if not Path(creds_path).exists():
        print(f"\n  [WARN] File not found: {creds_path}")
        print("  Make sure to download credentials.json from Google Cloud Console first.")
        print("  Path saved — auth will fail until the file is placed there.")
    else:
        print(f"  [OK] Found: {creds_path}")

    # ── token.json ────────────────────────────────────────────────────────────
    current_token = os.environ.get("GDRIVE_TOKEN", "")
    if current_token:
        print(f"\n  GDRIVE_TOKEN is already set: {current_token}")
        use_existing = input("  Keep existing path? [Y/n]: ").strip().lower()
        if use_existing in ("", "y", "yes"):
            token_path = current_token
        else:
            token_path = ""
    else:
        token_path = ""

    if not token_path:
        # Suggest same directory as credentials
        creds_dir    = str(Path(creds_path).parent)
        default_tok  = str(Path(creds_dir) / "token.json")
        print(f"\n  Where should token.json be saved?")
        print(f"  Press Enter to use default: {default_tok}")
        raw = input("  Path: ").strip()
        token_path = raw if raw else default_tok

    token_path = str(Path(token_path).expanduser().resolve())

    # Ensure directory exists
    token_dir = Path(token_path).parent
    token_dir.mkdir(parents=True, exist_ok=True)

    # Set permissions on the dir (Linux/Mac only)
    if OS in ("linux", "mac"):
        token_dir.chmod(0o700)
        if Path(creds_path).exists():
            Path(creds_path).chmod(0o600)

    print(f"\n  credentials.json : {creds_path}")
    print(f"  token.json       : {token_path}")

    return creds_path, token_path


# ─── Scopes & Auth ────────────────────────────────────────────────────────────

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/presentations",
]


def get_credentials(creds_file: str, token_file: str):
    try:
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
    except ImportError:
        print("\n[ERROR] Missing packages. Run:")
        print("  pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client")
        sys.exit(1)

    creds = None
    if Path(token_file).exists():
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print("[INFO] Token refreshed successfully.")
        else:
            if not Path(creds_file).exists():
                print(f"\n[ERROR] credentials.json not found at: {creds_file}")
                print("  Download from Google Cloud Console → APIs & Services → Credentials")
                print("  Create an OAuth 2.0 Client ID (Desktop App type)")
                sys.exit(1)
            flow  = InstalledAppFlow.from_client_secrets_file(creds_file, SCOPES)
            creds = flow.run_local_server(port=0)
            print("[INFO] Authentication successful.")

        with open(token_file, "w") as f:
            f.write(creds.to_json())
        if OS in ("linux", "mac"):
            Path(token_file).chmod(0o600)
        print(f"[INFO] Token saved to: {token_file}")

    return creds


def check_token(token_file: str) -> bool:
    if not Path(token_file).exists():
        print(f"[WARN] No token at: {token_file}")
        print("  Run: python scripts/auth_setup.py")
        return False
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        if creds.valid:
            print("[OK] Token is valid.")
            return True
        elif creds.expired and creds.refresh_token:
            creds.refresh(Request())
            with open(token_file, "w") as f:
                f.write(creds.to_json())
            print("[OK] Token was expired — refreshed successfully.")
            return True
        else:
            print("[WARN] Token invalid. Re-run auth setup.")
            return False
    except Exception as e:
        print(f"[ERROR] Token check failed: {e}")
        return False


def revoke_token(token_file: str):
    if Path(token_file).exists():
        Path(token_file).unlink()
        print(f"[INFO] Token revoked and deleted: {token_file}")
    else:
        print(f"[INFO] No token found at: {token_file}")


def show_current_env():
    creds = os.environ.get("GDRIVE_CREDS", "(not set)")
    token = os.environ.get("GDRIVE_TOKEN", "(not set)")
    print(f"\n  GDRIVE_CREDS = {creds}")
    print(f"  GDRIVE_TOKEN = {token}\n")
    if creds != "(not set)":
        exists = "✓ exists" if Path(creds).exists() else "✗ NOT FOUND"
        print(f"  credentials.json : {exists}")
    if token != "(not set)":
        exists = "✓ exists" if Path(token).exists() else "✗ not yet created (will be after auth)"
        print(f"  token.json       : {exists}")
    print()


# ─── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Google Drive OAuth2 Setup — interactive credential path configuration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--check",    action="store_true", help="Verify existing token")
    parser.add_argument("--revoke",   action="store_true", help="Delete token (force re-auth)")
    parser.add_argument("--show-env", action="store_true", help="Show current env var values")
    parser.add_argument("--no-auth",  action="store_true",
                        help="Configure paths and show env commands only — skip OAuth flow")
    args = parser.parse_args()

    if args.show_env:
        show_current_env()
        sys.exit(0)

    # Resolve paths — from env if set, else ask interactively
    if args.check or args.revoke:
        # For check/revoke, use env vars or defaults — no need to re-ask
        creds_path = os.environ.get("GDRIVE_CREDS", "credentials.json")
        token_path = os.environ.get("GDRIVE_TOKEN", "token.json")
    else:
        creds_path, token_path = ask_paths()
        print_env_instructions(creds_path, token_path)

    if args.revoke:
        revoke_token(token_path)
    elif args.check:
        ok = check_token(token_path)
        sys.exit(0 if ok else 1)
    elif args.no_auth:
        print("[INFO] Paths configured. Skipping OAuth flow (--no-auth).")
        print("[INFO] Run without --no-auth to complete authentication.")
    else:
        get_credentials(creds_path, token_path)
        print("\n[OK] Auth setup complete.")
        print(f"[OK] Set the env vars above so gdrive.py can find your credentials.\n")
```

## File: `scripts/gdrive.py`
```python
#!/usr/bin/env python3
"""
gdrive.py — Unified Google Drive CLI for AI Agents & Humans.

Usage:
  python scripts/gdrive.py <command> [options]

Commands:
  --- Read/List ---
  list                     List files/folders (root by default)
  info     --id FILE_ID    Get metadata for a file/folder
  search   --name QUERY    Search by name
  search   --text QUERY    Full-text search inside files
  search   --type TYPE     Search by type (doc|sheet|slide|folder|pdf)

  --- Create ---
  mkdir    --name NAME     Create a folder
  mkdoc    --name NAME     Create a Google Doc
  mksheet  --name NAME     Create a Google Sheet
  mkslide  --name NAME     Create a Google Slides presentation

  --- Update ---
  rename   --id ID --name NEW_NAME
  move     --id ID --to FOLDER_ID

  --- Upload / Download ---
  upload   --src PATH [--to FOLDER_ID] [--convert]
  download --id FILE_ID [--dest DIR]

  --- Permissions ---
  share    --id ID --email EMAIL [--role reader|writer|commenter]
  public   --id ID

  ⚠️  DESTRUCTIVE (require human confirmation — AI CANNOT BYPASS) ---
  trash    --id ID [--id ID ...]    Move to Trash (recoverable 30 days)
  delete   --id ID [--id ID ...]    PERMANENT delete (IRREVERSIBLE)

  --- Audit ---
  audit                    View recent destructive operation log

Global flags:
  --out markdown|json      Output format (default: markdown)
  --parent FOLDER_ID       Parent folder for create/upload
  --confirm                Allow non-interactive trash (NOT for permanent delete)
"""

import argparse
import json
import os
import sys
import mimetypes

# Ensure scripts/ directory is in path so safety.py can be imported as a sibling
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ─── Auth ─────────────────────────────────────────────────────────────────────

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/presentations",
]
CREDS_FILE = os.environ.get("GDRIVE_CREDS", "credentials.json")
TOKEN_FILE  = os.environ.get("GDRIVE_TOKEN", "token.json")


def get_credentials():
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDS_FILE):
                print(f"[ERROR] credentials.json not found. Run: python scripts/auth_setup.py")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
    return creds


def build(name, version):
    from googleapiclient.discovery import build as _build
    return _build(name, version, credentials=get_credentials())


# ─── Services (lazy) ─────────────────────────────────────────────────────────

_drive = _docs = _sheets = _slides = None

def drive():
    global _drive
    if not _drive: _drive = build("drive", "v3")
    return _drive

def docs():
    global _docs
    if not _docs: _docs = build("docs", "v1")
    return _docs

def sheets():
    global _sheets
    if not _sheets: _sheets = build("sheets", "v4")
    return _sheets

def slides():
    global _slides
    if not _slides: _slides = build("slides", "v1")
    return _slides


# ─── Output Formatters ───────────────────────────────────────────────────────

def fmt_size(b):
    try:
        b = int(b)
        for u in ["B","KB","MB","GB"]:
            if b < 1024: return f"{b:.1f} {u}"
            b /= 1024
        return f"{b:.1f} TB"
    except: return "—"

def fmt_time(iso):
    if not iso: return "—"
    return iso[:16].replace("T", " ")

def mime_label(mime):
    return (mime or "").split(".")[-1].replace("google-apps.","")

def output(data, fmt="markdown"):
    if fmt == "json":
        print(json.dumps(data, indent=2, default=str))
        return

    # Markdown table for list of files
    if isinstance(data, list):
        if not data:
            print("_No results found._")
            return
        print("| Name | Type | Modified | Size | Link |")
        print("|------|------|----------|------|------|")
        for f in data:
            name  = f.get("name","—")
            mime  = mime_label(f.get("mimeType",""))
            mtime = fmt_time(f.get("modifiedTime",""))
            size  = fmt_size(f.get("size","")) if f.get("size") else "—"
            link  = f.get("webViewLink","")
            link_md = f"[open]({link})" if link else "—"
            print(f"| {name} | {mime} | {mtime} | {size} | {link_md} |")
    elif isinstance(data, dict):
        print("| Field | Value |")
        print("|-------|-------|")
        for k, v in data.items():
            print(f"| {k} | {v} |")
    else:
        print(data)


# ─── Operations ───────────────────────────────────────────────────────────────

FILE_FIELDS = "id,name,mimeType,modifiedTime,createdTime,size,webViewLink,parents,owners,trashed"
LIST_FIELDS = f"files({FILE_FIELDS})"

MIME_TYPES = {
    "doc":    "application/vnd.google-apps.document",
    "sheet":  "application/vnd.google-apps.spreadsheet",
    "slide":  "application/vnd.google-apps.presentation",
    "folder": "application/vnd.google-apps.folder",
    "pdf":    "application/pdf",
}

EXPORT_FORMATS = {
    "application/vnd.google-apps.document":
        ("application/vnd.openxmlformats-officedocument.wordprocessingml.document", ".docx"),
    "application/vnd.google-apps.spreadsheet":
        ("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", ".xlsx"),
    "application/vnd.google-apps.presentation":
        ("application/vnd.openxmlformats-officedocument.presentationml.presentation", ".pptx"),
    "application/vnd.google-apps.drawing": ("image/svg+xml", ".svg"),
}


def cmd_list(args):
    folder_id = args.parent or "root"
    results = drive().files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields=LIST_FIELDS, pageSize=100
    ).execute()
    output(results.get("files", []), args.out)


def cmd_info(args):
    f = drive().files().get(fileId=args.id, fields=FILE_FIELDS).execute()
    output(f, args.out)


def cmd_search(args):
    q_parts = ["trashed=false"]
    if args.name:  q_parts.append(f"name contains '{args.name}'")
    if args.text:  q_parts.append(f"fullText contains '{args.text}'")
    if args.type:
        mime = MIME_TYPES.get(args.type)
        if not mime:
            print(f"[ERROR] Unknown type '{args.type}'. Use: {', '.join(MIME_TYPES)}")
            sys.exit(1)
        q_parts.append(f"mimeType='{mime}'")
    if args.parent:
        q_parts.append(f"'{args.parent}' in parents")
    results = drive().files().list(
        q=" and ".join(q_parts), fields=LIST_FIELDS, pageSize=50
    ).execute()
    output(results.get("files", []), args.out)


def cmd_mkdir(args):
    meta = {"name": args.name, "mimeType": "application/vnd.google-apps.folder"}
    if args.parent: meta["parents"] = [args.parent]
    f = drive().files().create(body=meta, fields=FILE_FIELDS).execute()
    print(f"[OK] Folder created: {f['name']} (id: {f['id']})")
    output([f], args.out)


def cmd_mkdoc(args):
    if args.command == "mkdoc":
        f = docs().documents().create(body={"title": args.name}).execute()
        fid = f["documentId"]
    elif args.command == "mksheet":
        f = sheets().spreadsheets().create(
            body={"properties": {"title": args.name}}).execute()
        fid = f["spreadsheetId"]
    elif args.command == "mkslide":
        f = slides().presentations().create(body={"title": args.name}).execute()
        fid = f["presentationId"]
    else:
        return
    if args.parent:
        drive().files().update(
            fileId=fid, addParents=args.parent, fields="id,parents"
        ).execute()
    meta = drive().files().get(fileId=fid, fields=FILE_FIELDS).execute()
    print(f"[OK] Created: {meta['name']} (id: {fid})")
    output([meta], args.out)


def cmd_rename(args):
    f = drive().files().update(
        fileId=args.id, body={"name": args.name}, fields=FILE_FIELDS
    ).execute()
    print(f"[OK] Renamed to: {f['name']}")
    output([f], args.out)


def cmd_move(args):
    current = drive().files().get(fileId=args.id, fields="parents").execute()
    old_parents = ",".join(current.get("parents", []))
    f = drive().files().update(
        fileId=args.id, addParents=args.to, removeParents=old_parents,
        fields=FILE_FIELDS
    ).execute()
    print(f"[OK] Moved: {f['name']} → folder {args.to}")
    output([f], args.out)


def cmd_upload(args):
    from googleapiclient.http import MediaFileUpload
    src = args.src
    if not src:
        print("[ERROR] --src is required for upload")
        sys.exit(1)
    if not os.path.exists(src):
        print(f"[ERROR] Path not found: {src}")
        sys.exit(1)
    # Accept --to or --parent interchangeably for upload destination
    parent = args.to or args.parent or None
    if os.path.isdir(src):
        _upload_folder(src, parent, args.convert)
    else:
        _upload_file(src, parent, args.convert)


def _upload_file(local_path, parent_id=None, convert=False):
    from googleapiclient.http import MediaFileUpload
    CONVERT_MIME = {
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            "application/vnd.google-apps.document",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            "application/vnd.google-apps.spreadsheet",
        "application/vnd.openxmlformats-officedocument.presentationml.presentation":
            "application/vnd.google-apps.presentation",
    }
    src_mime, _ = mimetypes.guess_type(local_path)
    src_mime = src_mime or "application/octet-stream"
    meta = {"name": os.path.basename(local_path)}
    if parent_id: meta["parents"] = [parent_id]
    if convert and src_mime in CONVERT_MIME:
        meta["mimeType"] = CONVERT_MIME[src_mime]
    media = MediaFileUpload(local_path, mimetype=src_mime, resumable=True)
    f = drive().files().create(body=meta, media_body=media, fields=FILE_FIELDS).execute()
    print(f"[OK] Uploaded: {f['name']} (id: {f['id']})")
    return f


def _upload_folder(local_dir, parent_id=None, convert=False):
    name = os.path.basename(local_dir)
    meta = {"name": name, "mimeType": "application/vnd.google-apps.folder"}
    if parent_id: meta["parents"] = [parent_id]
    folder = drive().files().create(body=meta, fields="id,name").execute()
    print(f"[OK] Created folder: {folder['name']} (id: {folder['id']})")
    for item in os.listdir(local_dir):
        path = os.path.join(local_dir, item)
        if os.path.isdir(path):
            _upload_folder(path, folder["id"], convert)
        else:
            _upload_file(path, folder["id"], convert)
    return folder


def cmd_download(args):
    from googleapiclient.http import MediaIoBaseDownload
    dest = args.dest or "."
    os.makedirs(dest, exist_ok=True)
    meta = drive().files().get(fileId=args.id, fields="name,mimeType").execute()
    name, mime = meta["name"], meta["mimeType"]

    if mime == "application/vnd.google-apps.folder":
        out = _download_folder(args.id, dest)
        print(f"[OK] Downloaded folder to: {out}")
        return

    export = EXPORT_FORMATS.get(mime)
    if export:
        export_mime, ext = export
        request = drive().files().export_media(fileId=args.id, mimeType=export_mime)
        name += ext
    else:
        request = drive().files().get_media(fileId=args.id)

    out_path = os.path.join(dest, name)
    with open(out_path, "wb") as f:
        dl = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            _, done = dl.next_chunk()
    print(f"[OK] Downloaded: {out_path}")


def _download_folder(folder_id, dest):
    from googleapiclient.http import MediaIoBaseDownload
    meta = drive().files().get(fileId=folder_id, fields="name").execute()
    local_dir = os.path.join(dest, meta["name"])
    os.makedirs(local_dir, exist_ok=True)
    items = drive().files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields=LIST_FIELDS
    ).execute().get("files", [])
    for item in items:
        if item["mimeType"] == "application/vnd.google-apps.folder":
            _download_folder(item["id"], local_dir)
        else:
            export = EXPORT_FORMATS.get(item["mimeType"])
            if export:
                export_mime, ext = export
                req = drive().files().export_media(fileId=item["id"], mimeType=export_mime)
                fname = item["name"] + ext
            else:
                req = drive().files().get_media(fileId=item["id"])
                fname = item["name"]
            path = os.path.join(local_dir, fname)
            with open(path, "wb") as f:
                from googleapiclient.http import MediaIoBaseDownload
                dl = MediaIoBaseDownload(f, req)
                done = False
                while not done: _, done = dl.next_chunk()
    return local_dir


def cmd_share(args):
    body = {"role": args.role or "reader", "type": "user", "emailAddress": args.email}
    perm = drive().permissions().create(
        fileId=args.id, body=body, fields="id", sendNotificationEmail=True
    ).execute()
    print(f"[OK] Shared with {args.email} as {args.role or 'reader'} (perm id: {perm['id']})")


def cmd_public(args):
    drive().permissions().create(
        fileId=args.id, body={"role": "reader", "type": "anyone"}, fields="id"
    ).execute()
    link = drive().files().get(fileId=args.id, fields="webViewLink").execute()["webViewLink"]
    print(f"[OK] File is now public: {link}")


# ─── DESTRUCTIVE OPERATIONS — SAFETY ENFORCED ─────────────────────────────────
# These commands ALWAYS route through safety.py.
# NO path in this codebase calls drive().files().delete() or trashed=True
# without first passing through confirm_trash() or confirm_permanent_delete().

def cmd_trash(args):
    """Move items to Trash. Recoverable within 30 days. Requires human confirmation."""
    from safety import confirm_trash

    items = []
    for fid in args.id:
        try:
            meta = drive().files().get(fileId=fid, fields="id,name").execute()
            items.append({"id": meta["id"], "name": meta["name"]})
        except Exception as e:
            print(f"[ERROR] Could not fetch metadata for {fid}: {e}")
            sys.exit(1)

    # ══════════════════════════════════════════════════════════════
    # SAFETY GATE — no confirmation = no action. Period.
    # ══════════════════════════════════════════════════════════════
    confirmed = confirm_trash(items, non_interactive=args.confirm)

    if not confirmed:
        print("[ABORTED] No items were trashed.")
        sys.exit(0)

    for item in items:
        drive().files().update(
            fileId=item["id"], body={"trashed": True}, fields="id"
        ).execute()
        print(f"[TRASHED] {item['name']} (id: {item['id']})")


def cmd_delete(args):
    """
    PERMANENTLY delete items. IRREVERSIBLE. NO RECOVERY POSSIBLE.
    Always requires interactive human confirmation — no env var bypass allowed.
    """
    from safety import confirm_permanent_delete

    items = []
    for fid in args.id:
        try:
            meta = drive().files().get(fileId=fid, fields="id,name").execute()
            items.append({"id": meta["id"], "name": meta["name"]})
        except Exception as e:
            print(f"[ERROR] Could not fetch metadata for {fid}: {e}")
            sys.exit(1)

    # ══════════════════════════════════════════════════════════════════
    # HARD SAFETY GATE — non-interactive is ALWAYS blocked here.
    # This is not configurable. This is not overridable by any argument.
    # ══════════════════════════════════════════════════════════════════
    confirmed = confirm_permanent_delete(items, non_interactive=False)

    if not confirmed:
        print("[ABORTED] No items were deleted.")
        sys.exit(0)

    for item in items:
        drive().files().delete(fileId=item["id"]).execute()
        print(f"[DELETED] {item['name']} (id: {item['id']})")


def cmd_audit(args):
    from safety import view_audit_log
    view_audit_log(last_n=30)


# ─── CLI Entry Point ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Google Drive Manager — AI-safe CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("command", choices=[
        "list","info","search","mkdir","mkdoc","mksheet","mkslide",
        "rename","move","upload","download","share","public",
        "trash","delete","audit"
    ])
    parser.add_argument("--id",     nargs="+", help="File/folder ID(s)")
    parser.add_argument("--name",   help="Name for create/rename/search")
    parser.add_argument("--text",   help="Full-text search query")
    parser.add_argument("--type",   help="File type filter: doc|sheet|slide|folder|pdf")
    parser.add_argument("--parent", help="Parent folder ID (for create/upload)")
    parser.add_argument("--to",     help="Destination folder ID (for move; also accepted for upload)")
    parser.add_argument("--src",    help="Local path for upload")
    parser.add_argument("--dest",   help="Local destination for download (default: .)")
    parser.add_argument("--email",  help="Email for sharing")
    parser.add_argument("--role",   default="reader", help="Share role: reader|writer|commenter")
    parser.add_argument("--convert",action="store_true", help="Convert Office files on upload")
    parser.add_argument("--confirm",action="store_true",
                        help="Allow non-interactive trash (NOT for permanent delete)")
    parser.add_argument("--out",    default="markdown", choices=["markdown","json"],
                        help="Output format (default: markdown)")

    args = parser.parse_args()

    # Single --id convenience: unwrap list when only one expected
    if args.id and len(args.id) == 1 and args.command not in ("trash","delete"):
        args.id = args.id[0]

    dispatch = {
        "list":     cmd_list,
        "info":     cmd_info,
        "search":   cmd_search,
        "mkdir":    cmd_mkdir,
        "mkdoc":    cmd_mkdoc,
        "mksheet":  cmd_mkdoc,
        "mkslide":  cmd_mkdoc,
        "rename":   cmd_rename,
        "move":     cmd_move,
        "upload":   cmd_upload,
        "download": cmd_download,
        "share":    cmd_share,
        "public":   cmd_public,
        "trash":    cmd_trash,
        "delete":   cmd_delete,
        "audit":    cmd_audit,
    }

    try:
        dispatch[args.command](args)
    except KeyboardInterrupt:
        print("\n[CANCELLED]")
        sys.exit(0)
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `scripts/safety.py`
```python
#!/usr/bin/env python3
"""
safety.py — MANDATORY SAFETY GUARDRAILS FOR GOOGLE DRIVE OPERATIONS.

██████████████████████████████████████████████████████████████████████████
  CRITICAL: THIS MODULE GOVERNS ALL DESTRUCTIVE OPERATIONS ON GOOGLE DRIVE.
  NO AI AGENT, SCRIPT, OR AUTOMATED PROCESS MAY BYPASS THESE CHECKS.
  EVERY DELETE / TRASH / PERMANENT-DELETE MUST PASS THROUGH THIS MODULE.
  VIOLATION = DATA LOSS. THERE IS NO UNDO FOR PERMANENT DELETION.
██████████████████████████████████████████████████████████████████████████

Rules enforced by this module:
  1. TRASH requires explicit user confirmation (typed "yes" or --confirm flag)
  2. PERMANENT DELETE requires typed confirmation of the exact file/folder name
  3. BULK operations (>1 item) require COUNT confirmation ("delete 5 files")
  4. NO AI may call _execute_trash() or _execute_permanent_delete() directly —
     they must go through confirm_trash() or confirm_permanent_delete()
  5. All destructive actions are logged to gdrive_audit.log with timestamp
"""

import sys
import os
import json
import logging
from datetime import datetime, timezone

AUDIT_LOG = os.environ.get("GDRIVE_AUDIT_LOG", "gdrive_audit.log")

# ─── Audit Logger ─────────────────────────────────────────────────────────────

def _audit(action: str, target_id: str, target_name: str, outcome: str, actor: str = "user"):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "actor":     actor,
        "action":    action,
        "target_id": target_id,
        "target_name": target_name,
        "outcome":   outcome,
    }
    with open(AUDIT_LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")

# ─── Warning Banner ───────────────────────────────────────────────────────────

TRASH_BANNER = """
╔══════════════════════════════════════════════════════════════════╗
║                  ⚠️  DESTRUCTIVE OPERATION WARNING  ⚠️           ║
╠══════════════════════════════════════════════════════════════════╣
║  You are about to TRASH the following item(s) on Google Drive.  ║
║  Trashed items can be restored from Trash within 30 days.       ║
╚══════════════════════════════════════════════════════════════════╝
"""

PERMANENT_BANNER = """
╔══════════════════════════════════════════════════════════════════╗
║              🚨  PERMANENT DELETION — IRREVERSIBLE  🚨           ║
╠══════════════════════════════════════════════════════════════════╣
║  You are about to PERMANENTLY DELETE item(s) from Google Drive. ║
║  THIS CANNOT BE UNDONE. THE DATA WILL BE LOST FOREVER.          ║
║  No recovery is possible after this action.                     ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ─── Core Guard Functions ─────────────────────────────────────────────────────

def confirm_trash(items: list[dict], non_interactive: bool = False) -> bool:
    """
    Gate for TRASH operations. items = [{"id": "...", "name": "..."}]

    non_interactive mode (for CI/scripts):
        Set env var GDRIVE_CONFIRM_TRASH=yes  (MUST be set by human explicitly)
        Logs a warning that confirmation was bypassed non-interactively.

    Returns True only if user confirmed. Never raises — returns False on any doubt.
    """
    print(TRASH_BANNER)
    print(f"  Items to be trashed ({len(items)}):")
    for item in items:
        print(f"    • [{item['id']}] {item['name']}")

    if len(items) > 1:
        print(f"\n  ⚠️  This will trash {len(items)} items.")

    # Non-interactive mode: ONLY if human explicitly set the env var
    if non_interactive:
        env_confirm = os.environ.get("GDRIVE_CONFIRM_TRASH", "").strip().lower()
        if env_confirm == "yes":
            print("\n[WARN] Non-interactive confirmation via GDRIVE_CONFIRM_TRASH env var.")
            for item in items:
                _audit("TRASH", item["id"], item["name"], "CONFIRMED (non-interactive)")
            return True
        else:
            print("\n[BLOCKED] Non-interactive trash requires GDRIVE_CONFIRM_TRASH=yes env var.")
            print("          Set it explicitly if you intend to trash these items.")
            for item in items:
                _audit("TRASH", item["id"], item["name"], "BLOCKED (non-interactive, no env var)")
            return False

    # Interactive confirmation
    print("\n  Type 'yes' to confirm trash, anything else to cancel: ", end="", flush=True)
    try:
        answer = input().strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\n[CANCELLED] Operation cancelled.")
        for item in items:
            _audit("TRASH", item["id"], item["name"], "CANCELLED (interrupted)")
        return False

    if answer == "yes":
        for item in items:
            _audit("TRASH", item["id"], item["name"], "CONFIRMED")
        return True
    else:
        print("[CANCELLED] Trash operation cancelled. No changes made.")
        for item in items:
            _audit("TRASH", item["id"], item["name"], "CANCELLED (user declined)")
        return False


def confirm_permanent_delete(items: list[dict], non_interactive: bool = False) -> bool:
    """
    Gate for PERMANENT DELETE operations.

    For a SINGLE item: user must type the exact file/folder name.
    For MULTIPLE items: user must type the exact count ("delete 5 files").

    Non-interactive permanent deletion is NEVER allowed — not even with env vars.
    This is intentional and cannot be overridden by any flag or environment variable.
    """
    print(PERMANENT_BANNER)
    print(f"  Items to be PERMANENTLY DELETED ({len(items)}):")
    for item in items:
        print(f"    • [{item['id']}] {item['name']}")

    # Non-interactive: ALWAYS BLOCKED for permanent delete — no exceptions
    if non_interactive:
        print("\n[HARD BLOCK] Permanent deletion is NEVER allowed in non-interactive mode.")
        print("             An AI or script cannot permanently delete files without a human")
        print("             physically typing confirmation in the terminal.")
        for item in items:
            _audit("PERMANENT_DELETE", item["id"], item["name"], "HARD BLOCKED (non-interactive)")
        return False

    if len(items) == 1:
        name = items[0]["name"]
        print(f'\n  To confirm, type the exact file name: "{name}"')
        print("  > ", end="", flush=True)
        try:
            answer = input().strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[CANCELLED]")
            _audit("PERMANENT_DELETE", items[0]["id"], name, "CANCELLED (interrupted)")
            return False

        if answer == name:
            _audit("PERMANENT_DELETE", items[0]["id"], name, "CONFIRMED")
            print("[CONFIRMED] Proceeding with permanent deletion...")
            return True
        else:
            print(f'[CANCELLED] Name mismatch. Expected "{name}", got "{answer}".')
            _audit("PERMANENT_DELETE", items[0]["id"], name, "CANCELLED (name mismatch)")
            return False

    else:
        count = len(items)
        expected = f"delete {count} files"
        print(f'\n  To confirm bulk deletion of {count} items, type: "{expected}"')
        print("  > ", end="", flush=True)
        try:
            answer = input().strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n[CANCELLED]")
            for item in items:
                _audit("PERMANENT_DELETE", item["id"], item["name"], "CANCELLED (interrupted)")
            return False

        if answer == expected:
            for item in items:
                _audit("PERMANENT_DELETE", item["id"], item["name"], "CONFIRMED (bulk)")
            print("[CONFIRMED] Proceeding with permanent deletion of all items...")
            return True
        else:
            print(f'[CANCELLED] Expected "{expected}", got "{answer}".')
            for item in items:
                _audit("PERMANENT_DELETE", item["id"], item["name"], "CANCELLED (bulk mismatch)")
            return False


def view_audit_log(last_n: int = 20):
    """Print the last N audit log entries as a Markdown table."""
    if not os.path.exists(AUDIT_LOG):
        print("_No audit log found._")
        return
    with open(AUDIT_LOG) as f:
        entries = [json.loads(line) for line in f if line.strip()]
    entries = entries[-last_n:]
    print(f"| Timestamp | Action | Name | Outcome |")
    print(f"|-----------|--------|------|---------|")
    for e in entries:
        ts   = e.get("timestamp","")[:19].replace("T"," ")
        act  = e.get("action","")
        name = e.get("target_name","")
        out  = e.get("outcome","")
        print(f"| {ts} | {act} | {name} | {out} |")
```


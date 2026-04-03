---
id: notebooklm-skill-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:12.982655
---

# KNOWLEDGE EXTRACT: notebooklm-skill
> **Extracted on:** 2026-03-30 17:49:29
> **Source:** notebooklm-skill

---

## File: `.gitignore`
```
# Virtual Environment
.venv/
venv/
env/
*.venv

# Skill Data (NEVER commit - contains auth and personal notebooks!)
data/
data/*
data/**/*

# Claude-specific
.claude/
*.claude

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
scripts/__pycache__/
scripts/*.pyc

# Environment
.env
*.env
.env.*

# Browser/Auth state (if accidentally placed outside data/)
browser_state/
auth/
auth_info.json
library.json
notebooks.json
state.json
cookies.json

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
Thumbs.db
desktop.ini
ehthumbs.db

# Logs
*.log
logs/
*.debug

# Backups
*.backup
*.bak
*.tmp
*.temp

# Test artifacts
.coverage
htmlcov/
.pytest_cache/
.tox/

# Package artifacts
dist/
build/
*.egg-info/
```

## File: `AUTHENTICATION.md`
```markdown
# Authentication Architecture

## Overview

This skill uses a **hybrid authentication approach** that combines the best of both worlds:

1. **Persistent Browser Profile** (`user_data_dir`) for consistent browser fingerprinting
2. **Manual Cookie Injection** from `state.json` for reliable session cookie persistence

## Why This Approach?

### The Problem

Playwright/Patchright has a known bug ([#36139](https://github.com/microsoft/playwright/issues/36139)) where **session cookies** (cookies without an `Expires` attribute) do not persist correctly when using `launch_persistent_context()` with `user_data_dir`.

**What happens:**
- ✅ Persistent cookies (with `Expires` date) → Saved correctly to browser profile
- ❌ Session cookies (without `Expires`) → **Lost after browser restarts**

**Impact:**
- Some Google auth cookies are session cookies
- Users experience random authentication failures
- "Works on my machine" syndrome (depends on which cookies Google uses)

### TypeScript vs Python

The **MCP Server** (TypeScript) can work around this by passing `storage_state` as a parameter:

```typescript
// TypeScript - works!
const context = await chromium.launchPersistentContext(userDataDir, {
  storageState: "state.json",  // ← Loads cookies including session cookies
  channel: "chrome"
});
```

But **Python's Playwright API doesn't support this** ([#14949](https://github.com/microsoft/playwright/issues/14949)):

```python
# Python - NOT SUPPORTED!
context = playwright.chromium.launch_persistent_context(
    user_data_dir=profile_dir,
    storage_state="state.json",  # ← Parameter not available in Python!
    channel="chrome"
)
```

## Our Solution: Hybrid Approach

We use a **two-phase authentication system**:

### Phase 1: Setup (`auth_manager.py setup`)

1. Launch persistent context with `user_data_dir`
2. User logs in manually
3. **Save state to TWO places:**
   - Browser profile directory (automatic, for fingerprint + persistent cookies)
   - `state.json` file (explicit save, for session cookies)

```python
context = playwright.chromium.launch_persistent_context(
    user_data_dir="browser_profile/",
    channel="chrome"
)
# User logs in...
context.storage_state(path="state.json")  # Save all cookies
```

### Phase 2: Runtime (`ask_question.py`)

1. Launch persistent context with `user_data_dir` (loads fingerprint + persistent cookies)
2. **Manually inject cookies** from `state.json` (adds session cookies)

```python
# Step 1: Launch with browser profile
context = playwright.chromium.launch_persistent_context(
    user_data_dir="browser_profile/",
    channel="chrome"
)

# Step 2: Manually inject cookies from state.json
with open("state.json", 'r') as f:
    state = json.load(f)
    context.add_cookies(state['cookies'])  # ← Workaround for session cookies!
```

## Benefits

| Feature | Our Approach | Pure `user_data_dir` | Pure `storage_state` |
|---------|--------------|----------------------|----------------------|
| **Browser Fingerprint Consistency** | ✅ Same across restarts | ✅ Same | ❌ Changes each time |
| **Session Cookie Persistence** | ✅ Manual injection | ❌ Lost (bug) | ✅ Native support |
| **Persistent Cookie Persistence** | ✅ Automatic | ✅ Automatic | ✅ Native support |
| **Google Trust** | ✅ High (same browser) | ✅ High | ❌ Low (new browser) |
| **Cross-platform Reliability** | ✅ Chrome required | ⚠️ Chromium issues | ✅ Portable |
| **Cache Performance** | ✅ Keeps cache | ✅ Keeps cache | ❌ No cache |

## File Structure

```
~/.claude/skills/notebooklm/data/
├── auth_info.json              # Metadata about authentication
├── browser_state/
│   ├── state.json             # Cookies + localStorage (for manual injection)
│   └── browser_profile/       # Chrome user profile (for fingerprint + cache)
│       ├── Default/
│       │   ├── Cookies        # Persistent cookies only (session cookies missing!)
│       │   ├── Local Storage/
│       │   └── Cache/
│       └── ...
```

## Why `state.json` is Critical

Even though we use `user_data_dir`, we **still need `state.json`** because:

1. **Session cookies** are not saved to the browser profile (Playwright bug)
2. **Manual injection** is the only reliable way to load session cookies
3. **Validation** - we can check if cookies are expired before launching

## Code References

**Setup:** `scripts/auth_manager.py:94-120`
- Lines 100-113: Launch persistent context with `channel="chrome"`
- Line 167: Save to `state.json` via `context.storage_state()`

**Runtime:** `scripts/ask_question.py:77-118`
- Lines 86-99: Launch persistent context
- Lines 101-118: Manual cookie injection workaround

**Validation:** `scripts/auth_manager.py:236-298`
- Lines 262-275: Launch persistent context
- Lines 277-287: Manual cookie injection for validation

## Related Issues

- [microsoft/playwright#36139](https://github.com/microsoft/playwright/issues/36139) - Session cookies not persisting
- [microsoft/playwright#14949](https://github.com/microsoft/playwright/issues/14949) - Storage state with persistent context
- [StackOverflow Question](https://stackoverflow.com/questions/79641481/) - Session cookie persistence issue

## Future Improvements

If Playwright adds support for `storage_state` parameter in Python's `launch_persistent_context()`, we can simplify to:

```python
# Future (when Python API supports it):
context = playwright.chromium.launch_persistent_context(
    user_data_dir="browser_profile/",
    storage_state="state.json",  # ← Would handle everything automatically!
    channel="chrome"
)
```

Until then, our hybrid approach is the most reliable solution.
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2025-11-21

### Added
- **Modular Architecture** - Refactored codebase for better maintainability
  - New `config.py` - Centralized configuration (paths, selectors, timeouts)
  - New `browser_utils.py` - BrowserFactory and StealthUtils classes
  - Cleaner separation of concerns across all scripts

### Changed
- **Timeout increased to 120 seconds** - Long queries no longer timeout prematurely
  - `ask_question.py`: 30s → 120s
  - `browser_session.py`: 30s → 120s
  - Resolves Issue #4

### Fixed
- **Thinking Message Detection** - Fixed incomplete answers showing placeholder text
  - Now waits for `div.thinking-message` element to disappear before reading answer
  - Answers like "Reviewing the content..." or "Looking for answers..." no longer returned prematurely
  - Works reliably across all languages and NotebookLM UI changes

- **Correct CSS Selectors** - Updated to match current NotebookLM UI
  - Changed from `.response-content, .message-content` to `.to-user-container .message-text-content`
  - Consistent selectors across all scripts

- **Stability Detection** - Improved answer completeness check
  - Now requires 3 consecutive stable polls instead of 1 second wait
  - Prevents truncated responses during streaming

## [1.2.0] - 2025-10-28

### Added
- Initial public release
- NotebookLM integration via browser automation
- Session-based conversations with Gemini 2.5
- Notebook library management
- Knowledge base preparation tools
- Google authentication with persistent sessions
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Please Prompto!

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
<div align="center">

# NotebookLM Claude Code Skill

**Let [Claude Code](https://github.com/anthropics/claude-code) chat directly with NotebookLM for source-grounded answers based exclusively on your uploaded documents**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](https://www.anthropic.com/news/skills)
[![Based on](https://img.shields.io/badge/Based%20on-NotebookLM%20MCP-green.svg)](https://github.com/PleasePrompto/notebooklm-mcp)
[![GitHub](https://img.shields.io/github/stars/PleasePrompto/notebooklm-skill?style=social)](https://github.com/PleasePrompto/notebooklm-skill)

> Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automation, library management, persistent auth. Drastically reduced hallucinations - answers only from your uploaded documents.

[Installation](#installation) • [Quick Start](#quick-start) • [Why NotebookLM](#why-notebooklm-not-local-rag) • [How It Works](#how-it-works) • [MCP Alternative](https://github.com/PleasePrompto/notebooklm-mcp)

</div>

---

## ⚠️ Important: Local Claude Code Only

**This skill works ONLY with local [Claude Code](https://github.com/anthropics/claude-code) installations, NOT in the web UI.**

The web UI runs skills in a sandbox without network access, which this skill requires for browser automation. You must use [Claude Code](https://github.com/anthropics/claude-code) locally on your machine.

---

## The Problem

When you tell [Claude Code](https://github.com/anthropics/claude-code) to "search through my local documentation", here's what happens:
- **Massive token consumption**: Searching through documentation means reading multiple files repeatedly
- **Inaccurate retrieval**: Searches for keywords, misses context and connections between docs
- **Hallucinations**: When it can't find something, it invents plausible-sounding APIs
- **Manual copy-paste**: Switching between NotebookLM browser and your editor constantly

## The Solution

This Claude Code Skill lets [Claude Code](https://github.com/anthropics/claude-code) chat directly with [**NotebookLM**](https://notebooklm.google/) — Google's **source-grounded knowledge base** powered by Gemini 2.5 that provides intelligent, synthesized answers exclusively from your uploaded documents.

```
Your Task → Claude asks NotebookLM → Gemini synthesizes answer → Claude writes correct code
```

**No more copy-paste dance**: Claude asks questions directly and gets answers straight back in the CLI. It builds deep understanding through automatic follow-ups, getting specific implementation details, edge cases, and best practices.

---

## Why NotebookLM, Not Local RAG?

| Approach | Token Cost | Setup Time | Hallucinations | Answer Quality |
|----------|------------|------------|----------------|----------------|
| **Feed docs to Claude** | 🔴 Very high (multiple file reads) | Instant | Yes - fills gaps | Variable retrieval |
| **Web search** | 🟡 Medium | Instant | High - unreliable sources | Hit or miss |
| **Local RAG** | 🟡 Medium-High | Hours (embeddings, chunking) | Medium - retrieval gaps | Depends on setup |
| **NotebookLM Skill** | 🟢 Minimal | 5 minutes | **Minimal** - source-grounded only | Expert synthesis |

### What Makes NotebookLM Superior?

1. **Pre-processed by Gemini**: Upload docs once, get instant expert knowledge
2. **Natural language Q&A**: Not just retrieval — actual understanding and synthesis
3. **Multi-source correlation**: Connects information across 50+ documents
4. **Citation-backed**: Every answer includes source references
5. **No infrastructure**: No vector DBs, embeddings, or chunking strategies needed

---

## Installation

### The simplest installation ever:

```bash
# 1. Create skills directory (if it doesn't exist)
mkdir -p ~/.claude/skills

# 2. Clone this repository
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm

# 3. That's it! Open Claude Code and say:
"What are my skills?"
```

When you first use the skill, it automatically:
- Creates an isolated Python environment (`.venv`)
- Installs all dependencies including **Google Chrome**
- Sets up browser automation with Chrome (not Chromium) for maximum reliability
- Everything stays contained in the skill folder

**Note:** The setup uses real Chrome instead of Chromium for cross-platform reliability, consistent browser fingerprinting, and better anti-detection with Google services

---

## Quick Start

### 1. Check your skills

Say in Claude Code:
```
"What skills do I have?"
```

Claude will list your available skills including NotebookLM.

### 2. Authenticate with Google (one-time)

```
"Set up NotebookLM authentication"
```
*A Chrome window opens → log in with your Google account*

### 3. Create your knowledge base

Go to [notebooklm.google.com](https://notebooklm.google.com) → Create notebook → Upload your docs:
- 📄 PDFs, Google Docs, markdown files
- 🔗 Websites, GitHub repos
- 🎥 YouTube videos
- 📚 Multiple sources per notebook

Share: **⚙️ Share → Anyone with link → Copy**

### 4. Add to your library

**Option A: Let Claude figure it out (Smart Add)**
```
"Query this notebook about its content and add it to my library: [your-link]"
```
Claude will automatically query the notebook to discover its content, then add it with appropriate metadata.

**Option B: Manual add**
```
"Add this NotebookLM to my library: [your-link]"
```
Claude will ask for a name and topics, then save it for future use.

### 5. Start researching

```
"What does my React docs say about hooks?"
```

Claude automatically selects the right notebook and gets the answer directly from NotebookLM.

---

## How It Works

This is a **Claude Code Skill** - a local folder containing instructions and scripts that Claude Code can use when needed. Unlike the [MCP server version](https://github.com/PleasePrompto/notebooklm-mcp), this runs directly in Claude Code without needing a separate server.

### Key Differences from MCP Server

| Feature | This Skill | MCP Server |
|---------|------------|------------|
| **Protocol** | Claude Skills | Model Context Protocol |
| **Installation** | Clone to `~/.claude/skills` | `claude mcp add ...` |
| **Sessions** | Fresh browser each question | Persistent chat sessions |
| **Compatibility** | Claude Code only (local) | Claude Code, Codex, Cursor, etc. |
| **Language** | Python | TypeScript |
| **Distribution** | Git clone | npm package |

### Architecture

```
~/.claude/skills/notebooklm/
├── SKILL.md              # Instructions for Claude
├── scripts/              # Python automation scripts
│   ├── ask_question.py   # Query NotebookLM
│   ├── notebook_manager.py # Library management
│   └── auth_manager.py   # Google authentication
├── .venv/                # Isolated Python environment (auto-created)
└── data/                 # Local notebook library
```

When you mention NotebookLM or send a notebook URL, Claude:
1. Loads the skill instructions
2. Runs the appropriate Python script
3. Opens a browser, asks your question
4. Returns the answer directly to you
5. Uses that knowledge to help with your task

---

## Core Features

### **Source-Grounded Responses**
NotebookLM significantly reduces hallucinations by answering exclusively from your uploaded documents. If information isn't available, it indicates uncertainty rather than inventing content.

### **Direct Integration**
No copy-paste between browser and editor. Claude asks and receives answers programmatically.

### **Smart Library Management**
Save NotebookLM links with tags and descriptions. Claude auto-selects the right notebook for your task.

### **Automatic Authentication**
One-time Google login, then authentication persists across sessions.

### **Self-Contained**
Everything runs in the skill folder with an isolated Python environment. No global installations.

### **Human-Like Automation**
Uses realistic typing speeds and interaction patterns to avoid detection.

---

## Common Commands

| What you say | What happens |
|--------------|--------------|
| *"Set up NotebookLM authentication"* | Opens Chrome for Google login |
| *"Add [link] to my NotebookLM library"* | Saves notebook with metadata |
| *"Show my NotebookLM notebooks"* | Lists all saved notebooks |
| *"Ask my API docs about [topic]"* | Queries the relevant notebook |
| *"Use the React notebook"* | Sets active notebook |
| *"Clear NotebookLM data"* | Fresh start (keeps library) |

---

## Real-World Examples

### Example 1: Workshop Manual Query

**User asks**: "Check my Suzuki GSR 600 workshop manual for brake fluid type, engine oil specs, and rear axle torque."

**Claude automatically**:
- Authenticates with NotebookLM
- Asks comprehensive questions about each specification
- Follows up when prompted "Is that ALL you need to know?"
- Provides accurate specifications: DOT 4 brake fluid, SAE 10W-40 oil, 100 N·m rear axle torque

![NotebookLM Chat Example](images/example_notebookchat.png)

### Example 2: Building Without Hallucinations

**You**: "I need to build an n8n workflow for Gmail spam filtering. Use my n8n notebook."

**Claude's internal process:**
```
→ Loads NotebookLM skill
→ Activates n8n notebook
→ Asks comprehensive questions with follow-ups
→ Synthesizes complete answer from multiple queries
```

**Result**: Working workflow on first try, no debugging hallucinated APIs.

---

## Technical Details

### Core Technology
- **Patchright**: Browser automation library (Playwright-based)
- **Python**: Implementation language for this skill
- **Stealth techniques**: Human-like typing and interaction patterns

Note: The MCP server uses the same Patchright library but via TypeScript/npm ecosystem.

### Dependencies
- **patchright==1.55.2**: Browser automation
- **python-dotenv==1.0.0**: Environment configuration
- Automatically installed in `.venv` on first use

### Data Storage

All data is stored locally within the skill directory:

```
~/.claude/skills/notebooklm/data/
├── library.json       - Your notebook library with metadata
├── auth_info.json     - Authentication status info
└── browser_state/     - Browser cookies and session data
```

**Important Security Note:**
- The `data/` directory contains sensitive authentication data and personal notebooks
- It's automatically excluded from git via `.gitignore`
- NEVER manually commit or share the contents of the `data/` directory

### Session Model

Unlike the MCP server, this skill uses a **stateless model**:
- Each question opens a fresh browser
- Asks the question, gets the answer
- Adds a follow-up prompt to encourage Claude to ask more questions
- Closes the browser immediately

This means:
- No persistent chat context
- Each question is independent
- But your notebook library persists
- **Follow-up mechanism**: Each answer includes "Is that ALL you need to know?" to prompt Claude to ask comprehensive follow-ups

For multi-step research, Claude automatically asks follow-up questions when needed.

---

## Limitations

### Skill-Specific
- **Local Claude Code only** - Does not work in web UI (sandbox restrictions)
- **No session persistence** - Each question is independent
- **No follow-up context** - Can't reference "the previous answer"

### NotebookLM
- **Rate limits** - Free tier has daily query limits
- **Manual upload** - You must upload docs to NotebookLM first
- **Share requirement** - Notebooks must be shared publicly

---

## FAQ

**Why doesn't this work in the Claude web UI?**
The web UI runs skills in a sandbox without network access. Browser automation requires network access to reach NotebookLM.

**How is this different from the MCP server?**
This is a simpler, Python-based implementation that runs directly as a Claude Skill. The MCP server is more feature-rich with persistent sessions and works with multiple tools (Codex, Cursor, etc.).

**Can I use both this skill and the MCP server?**
Yes! They serve different purposes. Use the skill for quick Claude Code integration, use the MCP server for persistent sessions and multi-tool support.

**What if Chrome crashes?**
Run: `"Clear NotebookLM browser data"` and try again.

**Is my Google account secure?**
Chrome runs locally on your machine. Your credentials never leave your computer. Use a dedicated Google account if you're concerned.

---

## Troubleshooting

### Skill not found
```bash
# Make sure it's in the right location
ls ~/.claude/skills/notebooklm/
# Should show: SKILL.md, scripts/, etc.
```

### Authentication issues
Say: `"Reset NotebookLM authentication"`

### Browser crashes
Say: `"Clear NotebookLM browser data"`

### Dependencies issues
```bash
# Manual reinstall if needed
cd ~/.claude/skills/notebooklm
rm -rf .venv
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## Disclaimer

This tool automates browser interactions with NotebookLM to make your workflow more efficient. However, a few friendly reminders:

**About browser automation:**
While I've built in humanization features (realistic typing speeds, natural delays, mouse movements) to make the automation behave more naturally, I can't guarantee Google won't detect or flag automated usage. I recommend using a dedicated Google account for automation rather than your primary account—think of it like web scraping: probably fine, but better safe than sorry!

**About CLI tools and AI agents:**
CLI tools like Claude Code, Codex, and similar AI-powered assistants are incredibly powerful, but they can make mistakes. Please use them with care and awareness:
- Always review changes before committing or deploying
- Test in safe environments first
- Keep backups of important work
- Remember: AI agents are assistants, not infallible oracles

I built this tool for myself because I was tired of the copy-paste dance between NotebookLM and my editor. I'm sharing it in the hope it helps others too, but I can't take responsibility for any issues, data loss, or account problems that might occur. Use at your own discretion and judgment.

That said, if you run into problems or have questions, feel free to open an issue on GitHub. I'm happy to help troubleshoot!

---

## Credits

This skill is inspired by my [**NotebookLM MCP Server**](https://github.com/PleasePrompto/notebooklm-mcp) and provides an alternative implementation as a Claude Code Skill:
- Both use Patchright for browser automation (TypeScript for MCP, Python for Skill)
- Skill version runs directly in Claude Code without MCP protocol
- Stateless design optimized for skill architecture

If you need:
- **Persistent sessions** → Use the [MCP Server](https://github.com/PleasePrompto/notebooklm-mcp)
- **Multiple tool support** (Codex, Cursor) → Use the [MCP Server](https://github.com/PleasePrompto/notebooklm-mcp)
- **Quick Claude Code integration** → Use this skill

---

## The Bottom Line

**Without this skill**: NotebookLM in browser → Copy answer → Paste in Claude → Copy next question → Back to browser...

**With this skill**: Claude researches directly → Gets answers instantly → Writes correct code

Stop the copy-paste dance. Start getting accurate, grounded answers directly in Claude Code.

```bash
# Get started in 30 seconds
cd ~/.claude/skills
git clone https://github.com/PleasePrompto/notebooklm-skill notebooklm
# Open Claude Code: "What are my skills?"
```

---

<div align="center">

Built as a Claude Code Skill adaptation of my [NotebookLM MCP Server](https://github.com/PleasePrompto/notebooklm-mcp)

For source-grounded, document-based research directly in Claude Code

</div>
```

## File: `requirements.txt`
```
# NotebookLM Skill Dependencies
# These will be installed in the skill's local .venv

# Core browser automation with anti-detection
# Note: After installation, run: patchright install chrome
# (Chrome is required, not Chromium, for cross-platform reliability)
patchright==1.55.2

# Environment management
python-dotenv==1.0.0
```

## File: `SKILL.md`
```markdown
---
name: notebooklm
description: Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automation, library management, persistent auth. Drastically reduced hallucinations through document-only responses.
---

# NotebookLM Research Assistant Skill

Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. Each question opens a fresh browser session, retrieves the answer exclusively from your uploaded documents, and closes.

## When to Use This Skill

Trigger when user:
- Mentions NotebookLM explicitly
- Shares NotebookLM URL (`https://notebooklm.google.com/notebook/...`)
- Asks to query their notebooks/documentation
- Wants to add documentation to NotebookLM library
- Uses phrases like "ask my NotebookLM", "check my docs", "query my notebook"

## ⚠️ CRITICAL: Add Command - Smart Discovery

When user wants to add a notebook without providing details:

**SMART ADD (Recommended)**: Query the notebook first to discover its content:
```bash
# Step 1: Query the notebook about its content
python scripts/run.py ask_question.py --question "What is the content of this notebook? What topics are covered? Provide a complete overview briefly and concisely" --notebook-url "[URL]"

# Step 2: Use the discovered information to add it
python scripts/run.py notebook_manager.py add --url "[URL]" --name "[Based on content]" --description "[Based on content]" --topics "[Based on content]"
```

**MANUAL ADD**: If user provides all details:
- `--url` - The NotebookLM URL
- `--name` - A descriptive name
- `--description` - What the notebook contains (REQUIRED!)
- `--topics` - Comma-separated topics (REQUIRED!)

NEVER guess or use generic descriptions! If details missing, use Smart Add to discover them.

## Critical: Always Use run.py Wrapper

**NEVER call scripts directly. ALWAYS use `python scripts/run.py [script]`:**

```bash
# ✅ CORRECT - Always use run.py:
python scripts/run.py auth_manager.py status
python scripts/run.py notebook_manager.py list
python scripts/run.py ask_question.py --question "..."

# ❌ WRONG - Never call directly:
python scripts/auth_manager.py status  # Fails without venv!
```

The `run.py` wrapper automatically:
1. Creates `.venv` if needed
2. Installs all dependencies
3. Activates environment
4. Executes script properly

## Core Workflow

### Step 1: Check Authentication Status
```bash
python scripts/run.py auth_manager.py status
```

If not authenticated, proceed to setup.

### Step 2: Authenticate (One-Time Setup)
```bash
# Browser MUST be visible for manual Google login
python scripts/run.py auth_manager.py setup
```

**Important:**
- Browser is VISIBLE for authentication
- Browser window opens automatically
- User must manually log in to Google
- Tell user: "A browser window will open for Google login"

### Step 3: Manage Notebook Library

```bash
# List all notebooks
python scripts/run.py notebook_manager.py list

# BEFORE ADDING: Ask user for metadata if unknown!
# "What does this notebook contain?"
# "What topics should I tag it with?"

# Add notebook to library (ALL parameters are REQUIRED!)
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "Descriptive Name" \
  --description "What this notebook contains" \  # REQUIRED - ASK USER IF UNKNOWN!
  --topics "topic1,topic2,topic3"  # REQUIRED - ASK USER IF UNKNOWN!

# Search notebooks by topic
python scripts/run.py notebook_manager.py search --query "keyword"

# Set active notebook
python scripts/run.py notebook_manager.py activate --id notebook-id

# Remove notebook
python scripts/run.py notebook_manager.py remove --id notebook-id
```

### Quick Workflow
1. Check library: `python scripts/run.py notebook_manager.py list`
2. Ask question: `python scripts/run.py ask_question.py --question "..." --notebook-id ID`

### Step 4: Ask Questions

```bash
# Basic query (uses active notebook if set)
python scripts/run.py ask_question.py --question "Your question here"

# Query specific notebook
python scripts/run.py ask_question.py --question "..." --notebook-id notebook-id

# Query with notebook URL directly
python scripts/run.py ask_question.py --question "..." --notebook-url "https://..."

# Show browser for debugging
python scripts/run.py ask_question.py --question "..." --show-browser
```

## Follow-Up Mechanism (CRITICAL)

Every NotebookLM answer ends with: **"EXTREMELY IMPORTANT: Is that ALL you need to know?"**

**Required Claude Behavior:**
1. **STOP** - Do not immediately respond to user
2. **ANALYZE** - Compare answer to user's original request
3. **IDENTIFY GAPS** - Determine if more information needed
4. **ASK FOLLOW-UP** - If gaps exist, immediately ask:
   ```bash
   python scripts/run.py ask_question.py --question "Follow-up with context..."
   ```
5. **REPEAT** - Continue until information is complete
6. **SYNTHESIZE** - Combine all answers before responding to user

## Script Reference

### Authentication Management (`auth_manager.py`)
```bash
python scripts/run.py auth_manager.py setup    # Initial setup (browser visible)
python scripts/run.py auth_manager.py status   # Check authentication
python scripts/run.py auth_manager.py reauth   # Re-authenticate (browser visible)
python scripts/run.py auth_manager.py clear    # Clear authentication
```

### Notebook Management (`notebook_manager.py`)
```bash
python scripts/run.py notebook_manager.py add --url URL --name NAME --description DESC --topics TOPICS
python scripts/run.py notebook_manager.py list
python scripts/run.py notebook_manager.py search --query QUERY
python scripts/run.py notebook_manager.py activate --id ID
python scripts/run.py notebook_manager.py remove --id ID
python scripts/run.py notebook_manager.py stats
```

### Question Interface (`ask_question.py`)
```bash
python scripts/run.py ask_question.py --question "..." [--notebook-id ID] [--notebook-url URL] [--show-browser]
```

### Data Cleanup (`cleanup_manager.py`)
```bash
python scripts/run.py cleanup_manager.py                    # Preview cleanup
python scripts/run.py cleanup_manager.py --confirm          # Execute cleanup
python scripts/run.py cleanup_manager.py --preserve-library # Keep notebooks
```

## Environment Management

The virtual environment is automatically managed:
- First run creates `.venv` automatically
- Dependencies install automatically
- Chromium browser installs automatically
- Everything isolated in skill directory

Manual setup (only if automatic fails):
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python -m patchright install chromium
```

## Data Storage

All data stored in `~/.claude/skills/notebooklm/data/`:
- `library.json` - Notebook metadata
- `auth_info.json` - Authentication status
- `browser_state/` - Browser cookies and session

**Security:** Protected by `.gitignore`, never commit to git.

## Configuration

Optional `.env` file in skill directory:
```env
HEADLESS=false           # Browser visibility
SHOW_BROWSER=false       # Default browser display
STEALTH_ENABLED=true     # Human-like behavior
TYPING_WPM_MIN=160       # Typing speed
TYPING_WPM_MAX=240
DEFAULT_NOTEBOOK_ID=     # Default notebook
```

## Decision Flow

```
User mentions NotebookLM
    ↓
Check auth → python scripts/run.py auth_manager.py status
    ↓
If not authenticated → python scripts/run.py auth_manager.py setup
    ↓
Check/Add notebook → python scripts/run.py notebook_manager.py list/add (with --description)
    ↓
Activate notebook → python scripts/run.py notebook_manager.py activate --id ID
    ↓
Ask question → python scripts/run.py ask_question.py --question "..."
    ↓
See "Is that ALL you need?" → Ask follow-ups until complete
    ↓
Synthesize and respond to user
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| ModuleNotFoundError | Use `run.py` wrapper |
| Authentication fails | Browser must be visible for setup! --show-browser |
| Rate limit (50/day) | Wait or switch Google account |
| Browser crashes | `python scripts/run.py cleanup_manager.py --preserve-library` |
| Notebook not found | Check with `notebook_manager.py list` |

## Best Practices

1. **Always use run.py** - Handles environment automatically
2. **Check auth first** - Before any operations
3. **Follow-up questions** - Don't stop at first answer
4. **Browser visible for auth** - Required for manual login
5. **Include context** - Each question is independent
6. **Synthesize answers** - Combine multiple responses

## Limitations

- No session persistence (each question = new browser)
- Rate limits on free Google accounts (50 queries/day)
- Manual upload required (user must add docs to NotebookLM)
- Browser overhead (few seconds per question)

## Resources (Skill Structure)

**Important directories and files:**

- `scripts/` - All automation scripts (ask_question.py, notebook_manager.py, etc.)
- `data/` - Local storage for authentication and notebook library
- `references/` - Extended documentation:
  - `api_reference.md` - Detailed API documentation for all scripts
  - `troubleshooting.md` - Common issues and solutions
  - `usage_patterns.md` - Best practices and workflow examples
- `.venv/` - Isolated Python environment (auto-created on first run)
- `.gitignore` - Protects sensitive data from being committed
```

## File: `references/api_reference.md`
```markdown
# NotebookLM Skill API Reference

Complete API documentation for all NotebookLM skill modules.

## Important: Always Use run.py Wrapper

**All commands must use the `run.py` wrapper to ensure proper environment:**

```bash
# ✅ CORRECT:
python scripts/run.py [script_name].py [arguments]

# ❌ WRONG:
python scripts/[script_name].py [arguments]  # Will fail without venv!
```

## Core Scripts

### ask_question.py
Query NotebookLM with automated browser interaction.

```bash
# Basic usage
python scripts/run.py ask_question.py --question "Your question"

# With specific notebook
python scripts/run.py ask_question.py --question "..." --notebook-id notebook-id

# With direct URL
python scripts/run.py ask_question.py --question "..." --notebook-url "https://..."

# Show browser (debugging)
python scripts/run.py ask_question.py --question "..." --show-browser
```

**Parameters:**
- `--question` (required): Question to ask
- `--notebook-id`: Use notebook from library
- `--notebook-url`: Use URL directly
- `--show-browser`: Make browser visible

**Returns:** Answer text with follow-up prompt appended

### notebook_manager.py
Manage notebook library with CRUD operations.

```bash
# Smart Add (discover content first)
python scripts/run.py ask_question.py --question "What is the content of this notebook? What topics are covered? Provide a complete overview briefly and concisely" --notebook-url "[URL]"
# Then add with discovered info
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "Name" \
  --description "Description" \
  --topics "topic1,topic2"

# Direct add (when you know the content)
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "Name" \
  --description "What it contains" \
  --topics "topic1,topic2"

# List notebooks
python scripts/run.py notebook_manager.py list

# Search notebooks
python scripts/run.py notebook_manager.py search --query "keyword"

# Activate notebook
python scripts/run.py notebook_manager.py activate --id notebook-id

# Remove notebook
python scripts/run.py notebook_manager.py remove --id notebook-id

# Show statistics
python scripts/run.py notebook_manager.py stats
```

**Commands:**
- `add`: Add notebook (requires --url, --name, --topics)
- `list`: Show all notebooks
- `search`: Find notebooks by keyword
- `activate`: Set default notebook
- `remove`: Delete from library
- `stats`: Display library statistics

### auth_manager.py
Handle Google authentication and browser state.

```bash
# Setup (browser visible for login)
python scripts/run.py auth_manager.py setup

# Check status
python scripts/run.py auth_manager.py status

# Re-authenticate
python scripts/run.py auth_manager.py reauth

# Clear authentication
python scripts/run.py auth_manager.py clear
```

**Commands:**
- `setup`: Initial authentication (browser MUST be visible)
- `status`: Check if authenticated
- `reauth`: Clear and re-setup
- `clear`: Remove all auth data

### cleanup_manager.py
Clean skill data with preservation options.

```bash
# Preview cleanup
python scripts/run.py cleanup_manager.py

# Execute cleanup
python scripts/run.py cleanup_manager.py --confirm

# Keep library
python scripts/run.py cleanup_manager.py --confirm --preserve-library

# Force without prompt
python scripts/run.py cleanup_manager.py --confirm --force
```

**Options:**
- `--confirm`: Actually perform cleanup
- `--preserve-library`: Keep notebook library
- `--force`: Skip confirmation prompt

### run.py
Script wrapper that handles environment setup.

```bash
# Usage
python scripts/run.py [script_name].py [arguments]

# Examples
python scripts/run.py auth_manager.py status
python scripts/run.py ask_question.py --question "..."
```

**Automatic actions:**
1. Creates `.venv` if missing
2. Installs dependencies
3. Activates environment
4. Executes target script

## Python API Usage

### Using subprocess with run.py

```python
import subprocess
import json

# Always use run.py wrapper
result = subprocess.run([
    "python", "scripts/run.py", "ask_question.py",
    "--question", "Your question",
    "--notebook-id", "notebook-id"
], capture_output=True, text=True)

answer = result.stdout
```

### Direct imports (after venv exists)

```python
# Only works if venv is already created and activated
from notebook_manager import NotebookLibrary
from auth_manager import AuthManager

library = NotebookLibrary()
notebooks = library.list_notebooks()

auth = AuthManager()
is_auth = auth.is_authenticated()
```

## Data Storage

Location: `~/.claude/skills/notebooklm/data/`

```
data/
├── library.json       # Notebook metadata
├── auth_info.json     # Auth status
└── browser_state/     # Browser cookies
    └── state.json
```

**Security:** Protected by `.gitignore`, never commit.

## Environment Variables

Optional `.env` file configuration:

```env
HEADLESS=false           # Browser visibility
SHOW_BROWSER=false       # Default display
STEALTH_ENABLED=true     # Human behavior
TYPING_WPM_MIN=160       # Typing speed
TYPING_WPM_MAX=240
DEFAULT_NOTEBOOK_ID=     # Default notebook
```

## Error Handling

Common patterns:

```python
# Using run.py prevents most errors
result = subprocess.run([
    "python", "scripts/run.py", "ask_question.py",
    "--question", "Question"
], capture_output=True, text=True)

if result.returncode != 0:
    error = result.stderr
    if "rate limit" in error.lower():
        # Wait or switch accounts
        pass
    elif "not authenticated" in error.lower():
        # Run auth setup
        subprocess.run(["python", "scripts/run.py", "auth_manager.py", "setup"])
```

## Rate Limits

Free Google accounts: 50 queries/day

Solutions:
1. Wait for reset (midnight PST)
2. Switch accounts with `reauth`
3. Use multiple Google accounts

## Advanced Patterns

### Parallel Queries

```python
import concurrent.futures
import subprocess

def query(question, notebook_id):
    result = subprocess.run([
        "python", "scripts/run.py", "ask_question.py",
        "--question", question,
        "--notebook-id", notebook_id
    ], capture_output=True, text=True)
    return result.stdout

# Run multiple queries simultaneously
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    futures = [
        executor.submit(query, q, nb)
        for q, nb in zip(questions, notebooks)
    ]
    results = [f.result() for f in futures]
```

### Batch Processing

```python
def batch_research(questions, notebook_id):
    results = []
    for question in questions:
        result = subprocess.run([
            "python", "scripts/run.py", "ask_question.py",
            "--question", question,
            "--notebook-id", notebook_id
        ], capture_output=True, text=True)
        results.append(result.stdout)
        time.sleep(2)  # Avoid rate limits
    return results
```

## Module Classes

### NotebookLibrary
- `add_notebook(url, name, topics)`
- `list_notebooks()`
- `search_notebooks(query)`
- `get_notebook(notebook_id)`
- `activate_notebook(notebook_id)`
- `remove_notebook(notebook_id)`

### AuthManager
- `is_authenticated()`
- `setup_auth(headless=False)`
- `get_auth_info()`
- `clear_auth()`
- `validate_auth()`

### BrowserSession (internal)
- Handles browser automation
- Manages stealth behavior
- Not intended for direct use

## Best Practices

1. **Always use run.py** - Ensures environment
2. **Check auth first** - Before operations
3. **Handle rate limits** - Implement retries
4. **Include context** - Questions are independent
5. **Clean sessions** - Use cleanup_manager
```

## File: `references/troubleshooting.md`
```markdown
# NotebookLM Skill Troubleshooting Guide

## Quick Fix Table

| Error | Solution |
|-------|----------|
| ModuleNotFoundError | Use `python scripts/run.py [script].py` |
| Authentication failed | Browser must be visible for setup |
| Browser crash | `python scripts/run.py cleanup_manager.py --preserve-library` |
| Rate limit hit | Wait 1 hour or switch accounts |
| Notebook not found | `python scripts/run.py notebook_manager.py list` |
| Script not working | Always use run.py wrapper |

## Critical: Always Use run.py

Most issues are solved by using the run.py wrapper:

```bash
# ✅ CORRECT - Always:
python scripts/run.py auth_manager.py status
python scripts/run.py ask_question.py --question "..."

# ❌ WRONG - Never:
python scripts/auth_manager.py status  # ModuleNotFoundError!
```

## Common Issues and Solutions

### Authentication Issues

#### Not authenticated error
```
Error: Not authenticated. Please run auth setup first.
```

**Solution:**
```bash
# Check status
python scripts/run.py auth_manager.py status

# Setup authentication (browser MUST be visible!)
python scripts/run.py auth_manager.py setup
# User must manually log in to Google

# If setup fails, try re-authentication
python scripts/run.py auth_manager.py reauth
```

#### Authentication expires frequently
**Solution:**
```bash
# Clear old authentication
python scripts/run.py cleanup_manager.py --preserve-library

# Fresh authentication setup
python scripts/run.py auth_manager.py setup --timeout 15

# Use persistent browser profile
export PERSIST_AUTH=true
```

#### Google blocks automated login
**Solution:**
1. Use dedicated Google account for automation
2. Enable "Less secure app access" if available
3. ALWAYS use visible browser:
```bash
python scripts/run.py auth_manager.py setup
# Browser MUST be visible - user logs in manually
# NO headless parameter exists - use --show-browser for debugging
```

### Browser Issues

#### Browser crashes or hangs
```
TimeoutError: Waiting for selector failed
```

**Solution:**
```bash
# Kill hanging processes
pkill -f chromium
pkill -f chrome

# Clean browser state
python scripts/run.py cleanup_manager.py --confirm --preserve-library

# Re-authenticate
python scripts/run.py auth_manager.py reauth
```

#### Browser not found error
**Solution:**
```bash
# Install Chromium via run.py (automatic)
python scripts/run.py auth_manager.py status
# run.py will install Chromium automatically

# Or manual install if needed
cd ~/.claude/skills/notebooklm
source .venv/bin/activate
python -m patchright install chromium
```

### Rate Limiting

#### Rate limit exceeded (50 queries/day)
**Solutions:**

**Option 1: Wait**
```bash
# Check when limit resets (usually midnight PST)
date -d "tomorrow 00:00 PST"
```

**Option 2: Switch accounts**
```bash
# Clear current auth
python scripts/run.py auth_manager.py clear

# Login with different account
python scripts/run.py auth_manager.py setup
```

**Option 3: Rotate accounts**
```python
# Use multiple accounts
accounts = ["account1", "account2"]
for account in accounts:
    # Switch account on rate limit
    subprocess.run(["python", "scripts/run.py", "auth_manager.py", "reauth"])
```

### Notebook Access Issues

#### Notebook not found
**Solution:**
```bash
# List all notebooks
python scripts/run.py notebook_manager.py list

# Search for notebook
python scripts/run.py notebook_manager.py search --query "keyword"

# Add notebook if missing
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/..." \
  --name "Name" \
  --topics "topics"
```

#### Access denied to notebook
**Solution:**
1. Check if notebook is still shared publicly
2. Re-add notebook with updated URL
3. Verify correct Google account is used

#### Wrong notebook being used
**Solution:**
```bash
# Check active notebook
python scripts/run.py notebook_manager.py list | grep "active"

# Activate correct notebook
python scripts/run.py notebook_manager.py activate --id correct-id
```

### Virtual Environment Issues

#### ModuleNotFoundError
```
ModuleNotFoundError: No module named 'patchright'
```

**Solution:**
```bash
# ALWAYS use run.py - it handles venv automatically!
python scripts/run.py [any_script].py

# run.py will:
# 1. Create .venv if missing
# 2. Install dependencies
# 3. Run the script
```

#### Wrong Python version
**Solution:**
```bash
# Check Python version (needs 3.8+)
python --version

# If wrong version, specify correct Python
python3.8 scripts/run.py auth_manager.py status
```

### Network Issues

#### Connection timeouts
**Solution:**
```bash
# Increase timeout
export TIMEOUT_SECONDS=60

# Check connectivity
ping notebooklm.google.com

# Use proxy if needed
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port
```

### Data Issues

#### Corrupted notebook library
```
JSON decode error when listing notebooks
```

**Solution:**
```bash
# Backup current library
cp ~/.claude/skills/notebooklm/data/library.json library.backup.json

# Reset library
rm ~/.claude/skills/notebooklm/data/library.json

# Re-add notebooks
python scripts/run.py notebook_manager.py add --url ... --name ...
```

#### Disk space full
**Solution:**
```bash
# Check disk usage
df -h ~/.claude/skills/notebooklm/data/

# Clean up
python scripts/run.py cleanup_manager.py --confirm --preserve-library
```

## Debugging Techniques

### Enable verbose logging
```bash
export DEBUG=true
export LOG_LEVEL=DEBUG
python scripts/run.py ask_question.py --question "Test" --show-browser
```

### Test individual components
```bash
# Test authentication
python scripts/run.py auth_manager.py status

# Test notebook access
python scripts/run.py notebook_manager.py list

# Test browser launch
python scripts/run.py ask_question.py --question "test" --show-browser
```

### Save screenshots on error
Add to scripts for debugging:
```python
try:
    # Your code
except Exception as e:
    page.screenshot(path=f"error_{timestamp}.png")
    raise e
```

## Recovery Procedures

### Complete reset
```bash
#!/bin/bash
# Kill processes
pkill -f chromium

# Backup library if exists
if [ -f ~/.claude/skills/notebooklm/data/library.json ]; then
    cp ~/.claude/skills/notebooklm/data/library.json ~/library.backup.json
fi

# Clean everything
cd ~/.claude/skills/notebooklm
python scripts/run.py cleanup_manager.py --confirm --force

# Remove venv
rm -rf .venv

# Reinstall (run.py will handle this)
python scripts/run.py auth_manager.py setup

# Restore library if backup exists
if [ -f ~/library.backup.json ]; then
    mkdir -p ~/.claude/skills/notebooklm/data/
    cp ~/library.backup.json ~/.claude/skills/notebooklm/data/library.json
fi
```

### Partial recovery (keep data)
```bash
# Keep auth and library, fix execution
cd ~/.claude/skills/notebooklm
rm -rf .venv

# run.py will recreate venv automatically
python scripts/run.py auth_manager.py status
```

## Error Messages Reference

### Authentication Errors
| Error | Cause | Solution |
|-------|-------|----------|
| Not authenticated | No valid auth | `run.py auth_manager.py setup` |
| Authentication expired | Session old | `run.py auth_manager.py reauth` |
| Invalid credentials | Wrong account | Check Google account |
| 2FA required | Security challenge | Complete in visible browser |

### Browser Errors
| Error | Cause | Solution |
|-------|-------|----------|
| Browser not found | Chromium missing | Use run.py (auto-installs) |
| Connection refused | Browser crashed | Kill processes, restart |
| Timeout waiting | Page slow | Increase timeout |
| Context closed | Browser terminated | Check logs for crashes |

### Notebook Errors
| Error | Cause | Solution |
|-------|-------|----------|
| Notebook not found | Invalid ID | `run.py notebook_manager.py list` |
| Access denied | Not shared | Re-share in NotebookLM |
| Invalid URL | Wrong format | Use full NotebookLM URL |
| No active notebook | None selected | `run.py notebook_manager.py activate` |

## Prevention Tips

1. **Always use run.py** - Prevents 90% of issues
2. **Regular maintenance** - Clear browser state weekly
3. **Monitor queries** - Track daily count to avoid limits
4. **Backup library** - Export notebook list regularly
5. **Use dedicated account** - Separate Google account for automation

## Getting Help

### Diagnostic information to collect
```bash
# System info
python --version
cd ~/.claude/skills/notebooklm
ls -la

# Skill status
python scripts/run.py auth_manager.py status
python scripts/run.py notebook_manager.py list | head -5

# Check data directory
ls -la ~/.claude/skills/notebooklm/data/
```

### Common questions

**Q: Why doesn't this work in Claude web UI?**
A: Web UI has no network access. Use local Claude Code.

**Q: Can I use multiple Google accounts?**
A: Yes, use `run.py auth_manager.py reauth` to switch.

**Q: How to increase rate limit?**
A: Use multiple accounts or upgrade to Google Workspace.

**Q: Is this safe for my Google account?**
A: Use dedicated account for automation. Only accesses NotebookLM.
```

## File: `references/usage_patterns.md`
```markdown
# NotebookLM Skill Usage Patterns

Advanced patterns for using the NotebookLM skill effectively.

## Critical: Always Use run.py

**Every command must use the run.py wrapper:**
```bash
# ✅ CORRECT:
python scripts/run.py auth_manager.py status
python scripts/run.py ask_question.py --question "..."

# ❌ WRONG:
python scripts/auth_manager.py status  # Will fail!
```

## Pattern 1: Initial Setup

```bash
# 1. Check authentication (using run.py!)
python scripts/run.py auth_manager.py status

# 2. If not authenticated, setup (Browser MUST be visible!)
python scripts/run.py auth_manager.py setup
# Tell user: "Please log in to Google in the browser window"

# 3. Add first notebook - ASK USER FOR DETAILS FIRST!
# Ask: "What does this notebook contain?"
# Ask: "What topics should I tag it with?"
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "User provided name" \
  --description "User provided description" \  # NEVER GUESS!
  --topics "user,provided,topics"  # NEVER GUESS!
```

**Critical Notes:**
- Virtual environment created automatically by run.py
- Browser MUST be visible for authentication
- ALWAYS discover content via query OR ask user for notebook metadata

## Pattern 2: Adding Notebooks (Smart Discovery!)

**When user shares a NotebookLM URL:**

**OPTION A: Smart Discovery (Recommended)**
```bash
# 1. Query the notebook to discover its content
python scripts/run.py ask_question.py \
  --question "What is the content of this notebook? What topics are covered? Provide a complete overview briefly and concisely" \
  --notebook-url "[URL]"

# 2. Use discovered info to add it
python scripts/run.py notebook_manager.py add \
  --url "[URL]" \
  --name "[Based on content]" \
  --description "[From discovery]" \
  --topics "[Extracted topics]"
```

**OPTION B: Ask User (Fallback)**
```bash
# If discovery fails, ask user:
"What does this notebook contain?"
"What topics does it cover?"

# Then add with user-provided info:
python scripts/run.py notebook_manager.py add \
  --url "[URL]" \
  --name "[User's answer]" \
  --description "[User's description]" \
  --topics "[User's topics]"
```

**NEVER:**
- Guess what's in a notebook
- Use generic descriptions
- Skip discovering content

## Pattern 3: Daily Research Workflow

```bash
# Check library
python scripts/run.py notebook_manager.py list

# Research with comprehensive questions
python scripts/run.py ask_question.py \
  --question "Detailed question with all context" \
  --notebook-id notebook-id

# Follow-up when you see "Is that ALL you need to know?"
python scripts/run.py ask_question.py \
  --question "Follow-up question with previous context"
```

## Pattern 4: Follow-Up Questions (CRITICAL!)

When NotebookLM responds with "EXTREMELY IMPORTANT: Is that ALL you need to know?":

```python
# 1. STOP - Don't respond to user yet
# 2. ANALYZE - Is answer complete?
# 3. If gaps exist, ask follow-up:
python scripts/run.py ask_question.py \
  --question "Specific follow-up with context from previous answer"

# 4. Repeat until complete
# 5. Only then synthesize and respond to user
```

## Pattern 5: Multi-Notebook Research

```python
# Query different notebooks for comparison
python scripts/run.py notebook_manager.py activate --id notebook-1
python scripts/run.py ask_question.py --question "Question"

python scripts/run.py notebook_manager.py activate --id notebook-2
python scripts/run.py ask_question.py --question "Same question"

# Compare and synthesize answers
```

## Pattern 6: Error Recovery

```bash
# If authentication fails
python scripts/run.py auth_manager.py status
python scripts/run.py auth_manager.py reauth  # Browser visible!

# If browser crashes
python scripts/run.py cleanup_manager.py --preserve-library
python scripts/run.py auth_manager.py setup  # Browser visible!

# If rate limited
# Wait or switch accounts
python scripts/run.py auth_manager.py reauth  # Login with different account
```

## Pattern 7: Batch Processing

```bash
#!/bin/bash
NOTEBOOK_ID="notebook-id"
QUESTIONS=(
    "First comprehensive question"
    "Second comprehensive question"
    "Third comprehensive question"
)

for question in "${QUESTIONS[@]}"; do
    echo "Asking: $question"
    python scripts/run.py ask_question.py \
        --question "$question" \
        --notebook-id "$NOTEBOOK_ID"
    sleep 2  # Avoid rate limits
done
```

## Pattern 8: Automated Research Script

```python
#!/usr/bin/env python
import subprocess

def research_topic(topic, notebook_id):
    # Comprehensive question
    question = f"""
    Explain {topic} in detail:
    1. Core concepts
    2. Implementation details
    3. Best practices
    4. Common pitfalls
    5. Examples
    """

    result = subprocess.run([
        "python", "scripts/run.py", "ask_question.py",
        "--question", question,
        "--notebook-id", notebook_id
    ], capture_output=True, text=True)

    return result.stdout
```

## Pattern 9: Notebook Organization

```python
# Organize by domain - with proper metadata
# ALWAYS ask user for descriptions!

# Backend notebooks
add_notebook("Backend API", "Complete API documentation", "api,rest,backend")
add_notebook("Database", "Schema and queries", "database,sql,backend")

# Frontend notebooks
add_notebook("React Docs", "React framework documentation", "react,frontend")
add_notebook("CSS Framework", "Styling documentation", "css,styling,frontend")

# Search by domain
python scripts/run.py notebook_manager.py search --query "backend"
python scripts/run.py notebook_manager.py search --query "frontend"
```

## Pattern 10: Integration with Development

```python
# Query documentation during development
def check_api_usage(api_endpoint):
    result = subprocess.run([
        "python", "scripts/run.py", "ask_question.py",
        "--question", f"Parameters and response format for {api_endpoint}",
        "--notebook-id", "api-docs"
    ], capture_output=True, text=True)

    # If follow-up needed
    if "Is that ALL you need" in result.stdout:
        # Ask for examples
        follow_up = subprocess.run([
            "python", "scripts/run.py", "ask_question.py",
            "--question", f"Show code examples for {api_endpoint}",
            "--notebook-id", "api-docs"
        ], capture_output=True, text=True)

    return combine_answers(result.stdout, follow_up.stdout)
```

## Best Practices

### 1. Question Formulation
- Be specific and comprehensive
- Include all context in each question
- Request structured responses
- Ask for examples when needed

### 2. Notebook Management
- **ALWAYS ask user for metadata**
- Use descriptive names
- Add comprehensive topics
- Keep URLs current

### 3. Performance
- Batch related questions
- Use parallel processing for different notebooks
- Monitor rate limits (50/day)
- Switch accounts if needed

### 4. Error Handling
- Always use run.py to prevent venv issues
- Check auth before operations
- Implement retry logic
- Have fallback notebooks ready

### 5. Security
- Use dedicated Google account
- Never commit data/ directory
- Regularly refresh auth
- Track all access

## Common Workflows for Claude

### Workflow 1: User Sends NotebookLM URL

```python
# 1. Detect URL in message
if "notebooklm.google.com" in user_message:
    url = extract_url(user_message)

    # 2. Check if in library
    notebooks = run("notebook_manager.py list")

    if url not in notebooks:
        # 3. ASK USER FOR METADATA (CRITICAL!)
        name = ask_user("What should I call this notebook?")
        description = ask_user("What does this notebook contain?")
        topics = ask_user("What topics does it cover?")

        # 4. Add with user-provided info
        run(f"notebook_manager.py add --url {url} --name '{name}' --description '{description}' --topics '{topics}'")

    # 5. Use the notebook
    answer = run(f"ask_question.py --question '{user_question}'")
```

### Workflow 2: Research Task

```python
# 1. Understand task
task = "Implement feature X"

# 2. Formulate comprehensive questions
questions = [
    "Complete implementation guide for X",
    "Error handling for X",
    "Performance considerations for X"
]

# 3. Query with follow-ups
for q in questions:
    answer = run(f"ask_question.py --question '{q}'")

    # Check if follow-up needed
    if "Is that ALL you need" in answer:
        # Ask more specific question
        follow_up = run(f"ask_question.py --question 'Specific detail about {q}'")

# 4. Synthesize and implement
```

## Tips and Tricks

1. **Always use run.py** - Prevents all venv issues
2. **Ask for metadata** - Never guess notebook contents
3. **Use verbose questions** - Include all context
4. **Follow up automatically** - When you see the prompt
5. **Monitor rate limits** - 50 queries per day
6. **Batch operations** - Group related queries
7. **Export important answers** - Save locally
8. **Version control notebooks** - Track changes
9. **Test auth regularly** - Before important tasks
10. **Document everything** - Keep notes on notebooks

## Quick Reference

```bash
# Always use run.py!
python scripts/run.py [script].py [args]

# Common operations
run.py auth_manager.py status          # Check auth
run.py auth_manager.py setup           # Login (browser visible!)
run.py notebook_manager.py list        # List notebooks
run.py notebook_manager.py add ...     # Add (ask user for metadata!)
run.py ask_question.py --question ...  # Query
run.py cleanup_manager.py ...          # Clean up
```

**Remember:** When in doubt, use run.py and ask the user for notebook details!
```

## File: `scripts/ask_question.py`
```python
#!/usr/bin/env python3
"""
Simple NotebookLM Question Interface
Based on MCP server implementation - simplified without sessions

Implements hybrid auth approach:
- Persistent browser profile (user_data_dir) for fingerprint consistency
- Manual cookie injection from state.json for session cookies (Playwright bug workaround)
See: https://github.com/microsoft/playwright/issues/36139
"""

import argparse
import sys
import time
import re
from pathlib import Path

from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from auth_manager import AuthManager
from notebook_manager import NotebookLibrary
from config import QUERY_INPUT_SELECTORS, RESPONSE_SELECTORS
from browser_utils import BrowserFactory, StealthUtils


# Follow-up reminder (adapted from MCP server for stateless operation)
# Since we don't have persistent sessions, we encourage comprehensive questions
FOLLOW_UP_REMINDER = (
    "\n\nEXTREMELY IMPORTANT: Is that ALL you need to know? "
    "You can always ask another question! Think about it carefully: "
    "before you reply to the user, review their original request and this answer. "
    "If anything is still unclear or missing, ask me another comprehensive question "
    "that includes all necessary context (since each question opens a new browser session)."
)


def ask_notebooklm(question: str, notebook_url: str, headless: bool = True) -> str:
    """
    Ask a question to NotebookLM

    Args:
        question: Question to ask
        notebook_url: NotebookLM notebook URL
        headless: Run browser in headless mode

    Returns:
        Answer text from NotebookLM
    """
    auth = AuthManager()

    if not auth.is_authenticated():
        print("⚠️ Not authenticated. Run: python auth_manager.py setup")
        return None

    print(f"💬 Asking: {question}")
    print(f"📚 Notebook: {notebook_url}")

    playwright = None
    context = None

    try:
        # Start playwright
        playwright = sync_playwright().start()

        # Launch persistent browser context using factory
        context = BrowserFactory.launch_persistent_context(
            playwright,
            headless=headless
        )

        # Navigate to notebook
        page = context.new_page()
        print("  🌐 Opening notebook...")
        page.goto(notebook_url, wait_until="domcontentloaded")

        # Wait for NotebookLM
        page.wait_for_url(re.compile(r"^https://notebooklm\.google\.com/"), timeout=10000)

        # Wait for query input (MCP approach)
        print("  ⏳ Waiting for query input...")
        query_element = None

        for selector in QUERY_INPUT_SELECTORS:
            try:
                query_element = page.wait_for_selector(
                    selector,
                    timeout=10000,
                    state="visible"  # Only check visibility, not disabled!
                )
                if query_element:
                    print(f"  ✓ Found input: {selector}")
                    break
            except:
                continue

        if not query_element:
            print("  ❌ Could not find query input")
            return None

        # Type question (human-like, fast)
        print("  ⏳ Typing question...")
        
        # Use primary selector for typing
        input_selector = QUERY_INPUT_SELECTORS[0]
        StealthUtils.human_type(page, input_selector, question)

        # Submit
        print("  📤 Submitting...")
        page.keyboard.press("Enter")

        # Small pause
        StealthUtils.random_delay(500, 1500)

        # Wait for response (MCP approach: poll for stable text)
        print("  ⏳ Waiting for answer...")

        answer = None
        stable_count = 0
        last_text = None
        deadline = time.time() + 120  # 2 minutes timeout

        while time.time() < deadline:
            # Check if NotebookLM is still thinking (most reliable indicator)
            try:
                thinking_element = page.query_selector('div.thinking-message')
                if thinking_element and thinking_element.is_visible():
                    time.sleep(1)
                    continue
            except:
                pass

            # Try to find response with MCP selectors
            for selector in RESPONSE_SELECTORS:
                try:
                    elements = page.query_selector_all(selector)
                    if elements:
                        # Get last (newest) response
                        latest = elements[-1]
                        text = latest.inner_text().strip()

                        if text:
                            if text == last_text:
                                stable_count += 1
                                if stable_count >= 3:  # Stable for 3 polls
                                    answer = text
                                    break
                            else:
                                stable_count = 0
                                last_text = text
                except:
                    continue

            if answer:
                break

            time.sleep(1)

        if not answer:
            print("  ❌ Timeout waiting for answer")
            return None

        print("  ✅ Got answer!")
        # Add follow-up reminder to encourage Claude to ask more questions
        return answer + FOLLOW_UP_REMINDER

    except Exception as e:
        print(f"  ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None

    finally:
        # Always clean up
        if context:
            try:
                context.close()
            except:
                pass

        if playwright:
            try:
                playwright.stop()
            except:
                pass


def main():
    parser = argparse.ArgumentParser(description='Ask NotebookLM a question')

    parser.add_argument('--question', required=True, help='Question to ask')
    parser.add_argument('--notebook-url', help='NotebookLM notebook URL')
    parser.add_argument('--notebook-id', help='Notebook ID from library')
    parser.add_argument('--show-browser', action='store_true', help='Show browser')

    args = parser.parse_args()

    # Resolve notebook URL
    notebook_url = args.notebook_url

    if not notebook_url and args.notebook_id:
        library = NotebookLibrary()
        notebook = library.get_notebook(args.notebook_id)
        if notebook:
            notebook_url = notebook['url']
        else:
            print(f"❌ Notebook '{args.notebook_id}' not found")
            return 1

    if not notebook_url:
        # Check for active notebook first
        library = NotebookLibrary()
        active = library.get_active_notebook()
        if active:
            notebook_url = active['url']
            print(f"📚 Using active notebook: {active['name']}")
        else:
            # Show available notebooks
            notebooks = library.list_notebooks()
            if notebooks:
                print("\n📚 Available notebooks:")
                for nb in notebooks:
                    mark = " [ACTIVE]" if nb.get('id') == library.active_notebook_id else ""
                    print(f"  {nb['id']}: {nb['name']}{mark}")
                print("\nSpecify with --notebook-id or set active:")
                print("python scripts/run.py notebook_manager.py activate --id ID")
            else:
                print("❌ No notebooks in library. Add one first:")
                print("python scripts/run.py notebook_manager.py add --url URL --name NAME --description DESC --topics TOPICS")
            return 1

    # Ask the question
    answer = ask_notebooklm(
        question=args.question,
        notebook_url=notebook_url,
        headless=not args.show_browser
    )

    if answer:
        print("\n" + "=" * 60)
        print(f"Question: {args.question}")
        print("=" * 60)
        print()
        print(answer)
        print()
        print("=" * 60)
        return 0
    else:
        print("\n❌ Failed to get answer")
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

## File: `scripts/auth_manager.py`
```python
#!/usr/bin/env python3
"""
Authentication Manager for NotebookLM
Handles Google login and browser state persistence
Based on the MCP server implementation

Implements hybrid auth approach:
- Persistent browser profile (user_data_dir) for fingerprint consistency
- Manual cookie injection from state.json for session cookies (Playwright bug workaround)
See: https://github.com/microsoft/playwright/issues/36139
"""

import json
import time
import argparse
import shutil
import re
import sys
from pathlib import Path
from typing import Optional, Dict, Any

from patchright.sync_api import sync_playwright, BrowserContext

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from config import BROWSER_STATE_DIR, STATE_FILE, AUTH_INFO_FILE, DATA_DIR
from browser_utils import BrowserFactory


class AuthManager:
    """
    Manages authentication and browser state for NotebookLM

    Features:
    - Interactive Google login
    - Browser state persistence
    - Session restoration
    - Account switching
    """

    def __init__(self):
        """Initialize the authentication manager"""
        # Ensure directories exist
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        BROWSER_STATE_DIR.mkdir(parents=True, exist_ok=True)

        self.state_file = STATE_FILE
        self.auth_info_file = AUTH_INFO_FILE
        self.browser_state_dir = BROWSER_STATE_DIR

    def is_authenticated(self) -> bool:
        """Check if valid authentication exists"""
        if not self.state_file.exists():
            return False

        # Check if state file is not too old (7 days)
        age_days = (time.time() - self.state_file.stat().st_mtime) / 86400
        if age_days > 7:
            print(f"⚠️ Browser state is {age_days:.1f} days old, may need re-authentication")

        return True

    def get_auth_info(self) -> Dict[str, Any]:
        """Get authentication information"""
        info = {
            'authenticated': self.is_authenticated(),
            'state_file': str(self.state_file),
            'state_exists': self.state_file.exists()
        }

        if self.auth_info_file.exists():
            try:
                with open(self.auth_info_file, 'r') as f:
                    saved_info = json.load(f)
                    info.update(saved_info)
            except Exception:
                pass

        if info['state_exists']:
            age_hours = (time.time() - self.state_file.stat().st_mtime) / 3600
            info['state_age_hours'] = age_hours

        return info

    def setup_auth(self, headless: bool = False, timeout_minutes: int = 10) -> bool:
        """
        Perform interactive authentication setup

        Args:
            headless: Run browser in headless mode (False for login)
            timeout_minutes: Maximum time to wait for login

        Returns:
            True if authentication successful
        """
        print("🔐 Starting authentication setup...")
        print(f"  Timeout: {timeout_minutes} minutes")

        playwright = None
        context = None

        try:
            playwright = sync_playwright().start()

            # Launch using factory
            context = BrowserFactory.launch_persistent_context(
                playwright,
                headless=headless
            )

            # Navigate to NotebookLM
            page = context.new_page()
            page.goto("https://notebooklm.google.com", wait_until="domcontentloaded")

            # Check if already authenticated
            if "notebooklm.google.com" in page.url and "accounts.google.com" not in page.url:
                print("  ✅ Already authenticated!")
                self._save_browser_state(context)
                return True

            # Wait for manual login
            print("\n  ⏳ Please log in to your Google account...")
            print(f"  ⏱️  Waiting up to {timeout_minutes} minutes for login...")

            try:
                # Wait for URL to change to NotebookLM (regex ensures it's the actual domain, not a parameter)
                timeout_ms = int(timeout_minutes * 60 * 1000)
                page.wait_for_url(re.compile(r"^https://notebooklm\.google\.com/"), timeout=timeout_ms)

                print(f"  ✅ Login successful!")

                # Save authentication state
                self._save_browser_state(context)
                self._save_auth_info()
                return True

            except Exception as e:
                print(f"  ❌ Authentication timeout: {e}")
                return False

        except Exception as e:
            print(f"  ❌ Error: {e}")
            return False

        finally:
            # Clean up browser resources
            if context:
                try:
                    context.close()
                except Exception:
                    pass

            if playwright:
                try:
                    playwright.stop()
                except Exception:
                    pass

    def _save_browser_state(self, context: BrowserContext):
        """Save browser state to disk"""
        try:
            # Save storage state (cookies, localStorage)
            context.storage_state(path=str(self.state_file))
            print(f"  💾 Saved browser state to: {self.state_file}")
        except Exception as e:
            print(f"  ❌ Failed to save browser state: {e}")
            raise

    def _save_auth_info(self):
        """Save authentication metadata"""
        try:
            info = {
                'authenticated_at': time.time(),
                'authenticated_at_iso': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            with open(self.auth_info_file, 'w') as f:
                json.dump(info, f, indent=2)
        except Exception:
            pass  # Non-critical

    def clear_auth(self) -> bool:
        """
        Clear all authentication data

        Returns:
            True if cleared successfully
        """
        print("🗑️ Clearing authentication data...")

        try:
            # Remove browser state
            if self.state_file.exists():
                self.state_file.unlink()
                print("  ✅ Removed browser state")

            # Remove auth info
            if self.auth_info_file.exists():
                self.auth_info_file.unlink()
                print("  ✅ Removed auth info")

            # Clear entire browser state directory
            if self.browser_state_dir.exists():
                shutil.rmtree(self.browser_state_dir)
                self.browser_state_dir.mkdir(parents=True, exist_ok=True)
                print("  ✅ Cleared browser data")

            return True

        except Exception as e:
            print(f"  ❌ Error clearing auth: {e}")
            return False

    def re_auth(self, headless: bool = False, timeout_minutes: int = 10) -> bool:
        """
        Perform re-authentication (clear and setup)

        Args:
            headless: Run browser in headless mode
            timeout_minutes: Login timeout in minutes

        Returns:
            True if successful
        """
        print("🔄 Starting re-authentication...")

        # Clear existing auth
        self.clear_auth()

        # Setup new auth
        return self.setup_auth(headless, timeout_minutes)

    def validate_auth(self) -> bool:
        """
        Validate that stored authentication works
        Uses persistent context to match actual usage pattern

        Returns:
            True if authentication is valid
        """
        if not self.is_authenticated():
            return False

        print("🔍 Validating authentication...")

        playwright = None
        context = None

        try:
            playwright = sync_playwright().start()

            # Launch using factory
            context = BrowserFactory.launch_persistent_context(
                playwright,
                headless=True
            )

            # Try to access NotebookLM
            page = context.new_page()
            page.goto("https://notebooklm.google.com", wait_until="domcontentloaded", timeout=30000)

            # Check if we can access NotebookLM
            if "notebooklm.google.com" in page.url and "accounts.google.com" not in page.url:
                print("  ✅ Authentication is valid")
                return True
            else:
                print("  ❌ Authentication is invalid (redirected to login)")
                return False

        except Exception as e:
            print(f"  ❌ Validation failed: {e}")
            return False

        finally:
            if context:
                try:
                    context.close()
                except Exception:
                    pass
            if playwright:
                try:
                    playwright.stop()
                except Exception:
                    pass


def main():
    """Command-line interface for authentication management"""
    parser = argparse.ArgumentParser(description='Manage NotebookLM authentication')

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Setup command
    setup_parser = subparsers.add_parser('setup', help='Setup authentication')
    setup_parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    setup_parser.add_argument('--timeout', type=float, default=10, help='Login timeout in minutes (default: 10)')

    # Status command
    subparsers.add_parser('status', help='Check authentication status')

    # Validate command
    subparsers.add_parser('validate', help='Validate authentication')

    # Clear command
    subparsers.add_parser('clear', help='Clear authentication')

    # Re-auth command
    reauth_parser = subparsers.add_parser('reauth', help='Re-authenticate (clear + setup)')
    reauth_parser.add_argument('--timeout', type=float, default=10, help='Login timeout in minutes (default: 10)')

    args = parser.parse_args()

    # Initialize manager
    auth = AuthManager()

    # Execute command
    if args.command == 'setup':
        if auth.setup_auth(headless=args.headless, timeout_minutes=args.timeout):
            print("\n✅ Authentication setup complete!")
            print("You can now use ask_question.py to query NotebookLM")
        else:
            print("\n❌ Authentication setup failed")
            exit(1)

    elif args.command == 'status':
        info = auth.get_auth_info()
        print("\n🔐 Authentication Status:")
        print(f"  Authenticated: {'Yes' if info['authenticated'] else 'No'}")
        if info.get('state_age_hours'):
            print(f"  State age: {info['state_age_hours']:.1f} hours")
        if info.get('authenticated_at_iso'):
            print(f"  Last auth: {info['authenticated_at_iso']}")
        print(f"  State file: {info['state_file']}")

    elif args.command == 'validate':
        if auth.validate_auth():
            print("Authentication is valid and working")
        else:
            print("Authentication is invalid or expired")
            print("Run: auth_manager.py setup")

    elif args.command == 'clear':
        if auth.clear_auth():
            print("Authentication cleared")

    elif args.command == 'reauth':
        if auth.re_auth(timeout_minutes=args.timeout):
            print("\n✅ Re-authentication complete!")
        else:
            print("\n❌ Re-authentication failed")
            exit(1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

## File: `scripts/browser_session.py`
```python
#!/usr/bin/env python3
"""
Browser Session Management for NotebookLM
Individual browser session for persistent NotebookLM conversations
Based on the original NotebookLM API implementation
"""

import time
import sys
from typing import Any, Dict, Optional
from pathlib import Path

from patchright.sync_api import BrowserContext, Page

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import StealthUtils


class BrowserSession:
    """
    Represents a single persistent browser session for NotebookLM

    Each session gets its own Page (tab) within a shared BrowserContext,
    allowing for contextual conversations where NotebookLM remembers
    previous messages.
    """

    def __init__(self, session_id: str, context: BrowserContext, notebook_url: str):
        """
        Initialize a new browser session

        Args:
            session_id: Unique identifier for this session
            context: Browser context (shared or dedicated)
            notebook_url: Target NotebookLM URL for this session
        """
        self.id = session_id
        self.created_at = time.time()
        self.last_activity = time.time()
        self.message_count = 0
        self.notebook_url = notebook_url
        self.context = context
        self.page = None
        self.stealth = StealthUtils()

        # Initialize the session
        self._initialize()

    def _initialize(self):
        """Initialize the browser session and navigate to NotebookLM"""
        print(f"🚀 Creating session {self.id}...")

        # Create new page (tab) in context
        self.page = self.context.new_page()
        print(f"  🌐 Navigating to NotebookLM...")

        try:
            # Navigate to notebook
            self.page.goto(self.notebook_url, wait_until="domcontentloaded", timeout=30000)

            # Check if login is needed
            if "accounts.google.com" in self.page.url:
                raise RuntimeError("Authentication required. Please run auth_manager.py setup first.")

            # Wait for page to be ready
            self._wait_for_ready()

            # Simulate human inspection
            self.stealth.random_mouse_movement(self.page)
            self.stealth.random_delay(300, 600)

            print(f"✅ Session {self.id} ready!")

        except Exception as e:
            print(f"❌ Failed to initialize session: {e}")
            if self.page:
                self.page.close()
            raise

    def _wait_for_ready(self):
        """Wait for NotebookLM page to be ready"""
        try:
            # Wait for chat input
            self.page.wait_for_selector("textarea.query-box-input", timeout=10000, state="visible")
        except Exception:
            # Try alternative selector
            self.page.wait_for_selector('textarea[aria-label="Feld für Anfragen"]', timeout=5000, state="visible")

    def ask(self, question: str) -> Dict[str, Any]:
        """
        Ask a question in this session

        Args:
            question: The question to ask

        Returns:
            Dict with status, question, answer, session_id
        """
        try:
            self.last_activity = time.time()
            self.message_count += 1

            print(f"💬 [{self.id}] Asking: {question}")

            # Snapshot current answer to detect new response
            previous_answer = self._snapshot_latest_response()

            # Find chat input
            chat_input_selector = "textarea.query-box-input"
            try:
                self.page.wait_for_selector(chat_input_selector, timeout=5000, state="visible")
            except Exception:
                chat_input_selector = 'textarea[aria-label="Feld für Anfragen"]'
                self.page.wait_for_selector(chat_input_selector, timeout=5000, state="visible")

            # Click and type with human-like behavior
            self.stealth.realistic_click(self.page, chat_input_selector)
            self.stealth.human_type(self.page, chat_input_selector, question)

            # Small pause before submit
            self.stealth.random_delay(300, 800)

            # Submit
            self.page.keyboard.press("Enter")

            # Wait for response
            print("  ⏳ Waiting for response...")
            self.stealth.random_delay(1500, 3000)

            # Get new answer
            answer = self._wait_for_latest_answer(previous_answer)

            if not answer:
                raise Exception("Empty response from NotebookLM")

            print(f"  ✅ Got response ({len(answer)} chars)")

            return {
                "status": "success",
                "question": question,
                "answer": answer,
                "session_id": self.id,
                "notebook_url": self.notebook_url
            }

        except Exception as e:
            print(f"  ❌ Error: {e}")
            return {
                "status": "error",
                "question": question,
                "error": str(e),
                "session_id": self.id
            }

    def _snapshot_latest_response(self) -> Optional[str]:
        """Get the current latest response text"""
        try:
            # Use correct NotebookLM selector
            responses = self.page.query_selector_all(".to-user-container .message-text-content")
            if responses:
                return responses[-1].inner_text()
        except Exception:
            pass
        return None

    def _wait_for_latest_answer(self, previous_answer: Optional[str], timeout: int = 120) -> str:
        """Wait for and extract the new answer"""
        start_time = time.time()
        last_candidate = None
        stable_count = 0

        while time.time() - start_time < timeout:
            # Check if NotebookLM is still thinking (most reliable indicator)
            try:
                thinking_element = self.page.query_selector('div.thinking-message')
                if thinking_element and thinking_element.is_visible():
                    time.sleep(0.5)
                    continue
            except Exception:
                pass

            try:
                # Use correct NotebookLM selector
                responses = self.page.query_selector_all(".to-user-container .message-text-content")

                if responses:
                    latest_text = responses[-1].inner_text().strip()

                    # Check if it's a new response
                    if latest_text and latest_text != previous_answer:
                        # Check if text is stable (3 consecutive polls)
                        if latest_text == last_candidate:
                            stable_count += 1
                            if stable_count >= 3:
                                return latest_text
                        else:
                            stable_count = 1
                            last_candidate = latest_text

            except Exception:
                pass

            time.sleep(0.5)

        raise TimeoutError(f"No response received within {timeout} seconds")

    def reset(self):
        """Reset the chat by reloading the page"""
        print(f"🔄 Resetting session {self.id}...")

        self.page.reload(wait_until="domcontentloaded")
        self._wait_for_ready()

        previous_count = self.message_count
        self.message_count = 0
        self.last_activity = time.time()

        print(f"✅ Session reset (cleared {previous_count} messages)")
        return previous_count

    def close(self):
        """Close this session and clean up resources"""
        print(f"🛑 Closing session {self.id}...")

        if self.page:
            try:
                self.page.close()
            except Exception as e:
                print(f"  ⚠️ Error closing page: {e}")

        print(f"✅ Session {self.id} closed")

    def get_info(self) -> Dict[str, Any]:
        """Get information about this session"""
        return {
            "id": self.id,
            "created_at": self.created_at,
            "last_activity": self.last_activity,
            "age_seconds": time.time() - self.created_at,
            "inactive_seconds": time.time() - self.last_activity,
            "message_count": self.message_count,
            "notebook_url": self.notebook_url
        }

    def is_expired(self, timeout_seconds: int = 900) -> bool:
        """Check if session has expired (default: 15 minutes)"""
        return (time.time() - self.last_activity) > timeout_seconds


if __name__ == "__main__":
    # Example usage
    print("Browser Session Module - Use ask_question.py for main interface")
    print("This module provides low-level browser session management.")
```

## File: `scripts/browser_utils.py`
```python
"""
Browser Utilities for NotebookLM Skill
Handles browser launching, stealth features, and common interactions
"""

import json
import time
import random
from typing import Optional, List

from patchright.sync_api import Playwright, BrowserContext, Page
from config import BROWSER_PROFILE_DIR, STATE_FILE, BROWSER_ARGS, USER_AGENT


class BrowserFactory:
    """Factory for creating configured browser contexts"""

    @staticmethod
    def launch_persistent_context(
        playwright: Playwright,
        headless: bool = True,
        user_data_dir: str = str(BROWSER_PROFILE_DIR)
    ) -> BrowserContext:
        """
        Launch a persistent browser context with anti-detection features
        and cookie workaround.
        """
        # Launch persistent context
        context = playwright.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            channel="chrome",  # Use real Chrome
            headless=headless,
            no_viewport=True,
            ignore_default_args=["--enable-automation"],
            user_agent=USER_AGENT,
            args=BROWSER_ARGS
        )

        # Cookie Workaround for Playwright bug #36139
        # Session cookies (expires=-1) don't persist in user_data_dir automatically
        BrowserFactory._inject_cookies(context)

        return context

    @staticmethod
    def _inject_cookies(context: BrowserContext):
        """Inject cookies from state.json if available"""
        if STATE_FILE.exists():
            try:
                with open(STATE_FILE, 'r') as f:
                    state = json.load(f)
                    if 'cookies' in state and len(state['cookies']) > 0:
                        context.add_cookies(state['cookies'])
                        # print(f"  🔧 Injected {len(state['cookies'])} cookies from state.json")
            except Exception as e:
                print(f"  ⚠️  Could not load state.json: {e}")


class StealthUtils:
    """Human-like interaction utilities"""

    @staticmethod
    def random_delay(min_ms: int = 100, max_ms: int = 500):
        """Add random delay"""
        time.sleep(random.uniform(min_ms / 1000, max_ms / 1000))

    @staticmethod
    def human_type(page: Page, selector: str, text: str, wpm_min: int = 320, wpm_max: int = 480):
        """Type with human-like speed"""
        element = page.query_selector(selector)
        if not element:
            # Try waiting if not immediately found
            try:
                element = page.wait_for_selector(selector, timeout=2000)
            except:
                pass
        
        if not element:
            print(f"⚠️ Element not found for typing: {selector}")
            return

        # Click to focus
        element.click()
        
        # Type
        for char in text:
            element.type(char, delay=random.uniform(25, 75))
            if random.random() < 0.05:
                time.sleep(random.uniform(0.15, 0.4))

    @staticmethod
    def realistic_click(page: Page, selector: str):
        """Click with realistic movement"""
        element = page.query_selector(selector)
        if not element:
            return

        # Optional: Move mouse to element (simplified)
        box = element.bounding_box()
        if box:
            x = box['x'] + box['width'] / 2
            y = box['y'] + box['height'] / 2
            page.mouse.move(x, y, steps=5)

        StealthUtils.random_delay(100, 300)
        element.click()
        StealthUtils.random_delay(100, 300)
```

## File: `scripts/cleanup_manager.py`
```python
#!/usr/bin/env python3
"""
Cleanup Manager for NotebookLM Skill
Manages cleanup of skill data and browser state
"""

import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Any


class CleanupManager:
    """
    Manages cleanup of NotebookLM skill data

    Features:
    - Preview what will be deleted
    - Selective cleanup options
    - Library preservation
    - Safe deletion with confirmation
    """

    def __init__(self):
        """Initialize the cleanup manager"""
        # Skill directory paths
        self.skill_dir = Path(__file__).parent.parent
        self.data_dir = self.skill_dir / "data"

    def get_cleanup_paths(self, preserve_library: bool = False) -> Dict[str, Any]:
        """
        Get paths that would be cleaned up

        Args:
            preserve_library: Keep library.json if True

        Returns:
            Dict with paths and sizes

        Note: .venv is NEVER deleted - it's part of the skill infrastructure
        """
        paths = {
            'browser_state': [],
            'sessions': [],
            'library': [],
            'auth': [],
            'other': []
        }

        total_size = 0

        if self.data_dir.exists():
            # Browser state
            browser_state_dir = self.data_dir / "browser_state"
            if browser_state_dir.exists():
                for item in browser_state_dir.iterdir():
                    size = self._get_size(item)
                    paths['browser_state'].append({
                        'path': str(item),
                        'size': size,
                        'type': 'dir' if item.is_dir() else 'file'
                    })
                    total_size += size

            # Sessions
            sessions_file = self.data_dir / "sessions.json"
            if sessions_file.exists():
                size = sessions_file.stat().st_size
                paths['sessions'].append({
                    'path': str(sessions_file),
                    'size': size,
                    'type': 'file'
                })
                total_size += size

            # Library (unless preserved)
            if not preserve_library:
                library_file = self.data_dir / "library.json"
                if library_file.exists():
                    size = library_file.stat().st_size
                    paths['library'].append({
                        'path': str(library_file),
                        'size': size,
                        'type': 'file'
                    })
                    total_size += size

            # Auth info
            auth_info = self.data_dir / "auth_info.json"
            if auth_info.exists():
                size = auth_info.stat().st_size
                paths['auth'].append({
                    'path': str(auth_info),
                    'size': size,
                    'type': 'file'
                })
                total_size += size

            # Other files in data dir (but NEVER .venv!)
            for item in self.data_dir.iterdir():
                if item.name not in ['browser_state', 'sessions.json', 'library.json', 'auth_info.json']:
                    size = self._get_size(item)
                    paths['other'].append({
                        'path': str(item),
                        'size': size,
                        'type': 'dir' if item.is_dir() else 'file'
                    })
                    total_size += size

        return {
            'categories': paths,
            'total_size': total_size,
            'total_items': sum(len(items) for items in paths.values())
        }

    def _get_size(self, path: Path) -> int:
        """Get size of file or directory in bytes"""
        if path.is_file():
            return path.stat().st_size
        elif path.is_dir():
            total = 0
            try:
                for item in path.rglob('*'):
                    if item.is_file():
                        total += item.stat().st_size
            except Exception:
                pass
            return total
        return 0

    def _format_size(self, size: int) -> str:
        """Format size in human-readable form"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} TB"

    def perform_cleanup(
        self,
        preserve_library: bool = False,
        dry_run: bool = False
    ) -> Dict[str, Any]:
        """
        Perform the actual cleanup

        Args:
            preserve_library: Keep library.json if True
            dry_run: Preview only, don't delete

        Returns:
            Dict with cleanup results
        """
        cleanup_data = self.get_cleanup_paths(preserve_library)
        deleted_items = []
        failed_items = []
        deleted_size = 0

        if dry_run:
            return {
                'dry_run': True,
                'would_delete': cleanup_data['total_items'],
                'would_free': cleanup_data['total_size']
            }

        # Perform deletion
        for category, items in cleanup_data['categories'].items():
            for item_info in items:
                path = Path(item_info['path'])
                try:
                    if path.exists():
                        if path.is_dir():
                            shutil.rmtree(path)
                        else:
                            path.unlink()
                        deleted_items.append(str(path))
                        deleted_size += item_info['size']
                        print(f"  ✅ Deleted: {path.name}")
                except Exception as e:
                    failed_items.append({
                        'path': str(path),
                        'error': str(e)
                    })
                    print(f"  ❌ Failed: {path.name} ({e})")

        # Recreate browser_state dir if everything was deleted
        if not preserve_library and not failed_items:
            browser_state_dir = self.data_dir / "browser_state"
            browser_state_dir.mkdir(parents=True, exist_ok=True)

        return {
            'deleted_items': deleted_items,
            'failed_items': failed_items,
            'deleted_size': deleted_size,
            'deleted_count': len(deleted_items),
            'failed_count': len(failed_items)
        }

    def print_cleanup_preview(self, preserve_library: bool = False):
        """Print a preview of what will be cleaned"""
        data = self.get_cleanup_paths(preserve_library)

        print("\n🔍 Cleanup Preview")
        print("=" * 60)

        for category, items in data['categories'].items():
            if items:
                print(f"\n📁 {category.replace('_', ' ').title()}:")
                for item in items:
                    path = Path(item['path'])
                    size_str = self._format_size(item['size'])
                    type_icon = "📂" if item['type'] == 'dir' else "📄"
                    print(f"  {type_icon} {path.name:<30} {size_str:>10}")

        print("\n" + "=" * 60)
        print(f"Total items: {data['total_items']}")
        print(f"Total size: {self._format_size(data['total_size'])}")

        if preserve_library:
            print("\n📚 Library will be preserved")

        print("\nThis preview shows what would be deleted.")
        print("Use --confirm to actually perform the cleanup.")


def main():
    """Command-line interface for cleanup management"""
    parser = argparse.ArgumentParser(
        description='Clean up NotebookLM skill data',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Preview what will be deleted
  python cleanup_manager.py

  # Perform cleanup (delete everything)
  python cleanup_manager.py --confirm

  # Cleanup but keep library
  python cleanup_manager.py --confirm --preserve-library

  # Force cleanup without preview
  python cleanup_manager.py --confirm --force
        """
    )

    parser.add_argument(
        '--confirm',
        action='store_true',
        help='Actually perform the cleanup (without this, only preview)'
    )

    parser.add_argument(
        '--preserve-library',
        action='store_true',
        help='Keep the notebook library (library.json)'
    )

    parser.add_argument(
        '--force',
        action='store_true',
        help='Skip confirmation prompt'
    )

    args = parser.parse_args()

    # Initialize manager
    manager = CleanupManager()

    if args.confirm:
        # Show preview first unless forced
        if not args.force:
            manager.print_cleanup_preview(args.preserve_library)

            print("\n⚠️  WARNING: This will delete the files shown above!")
            print("   Note: .venv is preserved (part of skill infrastructure)")
            response = input("Are you sure? (yes/no): ")

            if response.lower() != 'yes':
                print("Cleanup cancelled.")
                return

        # Perform cleanup
        print("\n🗑️ Performing cleanup...")
        result = manager.perform_cleanup(args.preserve_library, dry_run=False)

        print(f"\n✅ Cleanup complete!")
        print(f"  Deleted: {result['deleted_count']} items")
        print(f"  Freed: {manager._format_size(result['deleted_size'])}")

        if result['failed_count'] > 0:
            print(f"  ⚠️ Failed: {result['failed_count']} items")

    else:
        # Just show preview
        manager.print_cleanup_preview(args.preserve_library)
        print("\n💡 Note: Virtual environment (.venv) is never deleted")
        print("   It's part of the skill infrastructure, not user data")


if __name__ == "__main__":
    main()
```

## File: `scripts/config.py`
```python
"""
Configuration for NotebookLM Skill
Centralizes constants, selectors, and paths
"""

from pathlib import Path

# Paths
SKILL_DIR = Path(__file__).parent.parent
DATA_DIR = SKILL_DIR / "data"
BROWSER_STATE_DIR = DATA_DIR / "browser_state"
BROWSER_PROFILE_DIR = BROWSER_STATE_DIR / "browser_profile"
STATE_FILE = BROWSER_STATE_DIR / "state.json"
AUTH_INFO_FILE = DATA_DIR / "auth_info.json"
LIBRARY_FILE = DATA_DIR / "library.json"

# NotebookLM Selectors
QUERY_INPUT_SELECTORS = [
    "textarea.query-box-input",  # Primary
    'textarea[aria-label="Feld für Anfragen"]',  # Fallback German
    'textarea[aria-label="Input for queries"]',  # Fallback English
]

RESPONSE_SELECTORS = [
    ".to-user-container .message-text-content",  # Primary
    "[data-message-author='bot']",
    "[data-message-author='assistant']",
]

# Browser Configuration
BROWSER_ARGS = [
    '--disable-blink-features=AutomationControlled',  # Patches navigator.webdriver
    '--disable-dev-shm-usage',
    '--no-sandbox',
    '--no-first-run',
    '--no-default-browser-check'
]

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

# Timeouts
LOGIN_TIMEOUT_MINUTES = 10
QUERY_TIMEOUT_SECONDS = 120
PAGE_LOAD_TIMEOUT = 30000
```

## File: `scripts/notebook_manager.py`
```python
#!/usr/bin/env python3
"""
Notebook Library Management for NotebookLM
Manages a library of NotebookLM notebooks with metadata
Based on the MCP server implementation
"""

import json
import argparse
import uuid
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime


class NotebookLibrary:
    """Manages a collection of NotebookLM notebooks with metadata"""

    def __init__(self):
        """Initialize the notebook library"""
        # Store data within the skill directory
        skill_dir = Path(__file__).parent.parent
        self.data_dir = skill_dir / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.library_file = self.data_dir / "library.json"
        self.notebooks: Dict[str, Dict[str, Any]] = {}
        self.active_notebook_id: Optional[str] = None

        # Load existing library
        self._load_library()

    def _load_library(self):
        """Load library from disk"""
        if self.library_file.exists():
            try:
                with open(self.library_file, 'r') as f:
                    data = json.load(f)
                    self.notebooks = data.get('notebooks', {})
                    self.active_notebook_id = data.get('active_notebook_id')
                    print(f"📚 Loaded library with {len(self.notebooks)} notebooks")
            except Exception as e:
                print(f"⚠️ Error loading library: {e}")
                self.notebooks = {}
                self.active_notebook_id = None
        else:
            self._save_library()

    def _save_library(self):
        """Save library to disk"""
        try:
            data = {
                'notebooks': self.notebooks,
                'active_notebook_id': self.active_notebook_id,
                'updated_at': datetime.now().isoformat()
            }
            with open(self.library_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"❌ Error saving library: {e}")

    def add_notebook(
        self,
        url: str,
        name: str,
        description: str,
        topics: List[str],
        content_types: Optional[List[str]] = None,
        use_cases: Optional[List[str]] = None,
        tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Add a new notebook to the library

        Args:
            url: NotebookLM notebook URL
            name: Display name for the notebook
            description: What's in this notebook
            topics: Topics covered
            content_types: Types of content (optional)
            use_cases: When to use this notebook (optional)
            tags: Additional tags for organization (optional)

        Returns:
            The created notebook object
        """
        # Generate ID from name
        notebook_id = name.lower().replace(' ', '-').replace('_', '-')

        # Check for duplicates
        if notebook_id in self.notebooks:
            raise ValueError(f"Notebook with ID '{notebook_id}' already exists")

        # Create notebook object
        notebook = {
            'id': notebook_id,
            'url': url,
            'name': name,
            'description': description,
            'topics': topics,
            'content_types': content_types or [],
            'use_cases': use_cases or [],
            'tags': tags or [],
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'use_count': 0,
            'last_used': None
        }

        # Add to library
        self.notebooks[notebook_id] = notebook

        # Set as active if it's the first notebook
        if len(self.notebooks) == 1:
            self.active_notebook_id = notebook_id

        self._save_library()

        print(f"✅ Added notebook: {name} ({notebook_id})")
        return notebook

    def remove_notebook(self, notebook_id: str) -> bool:
        """
        Remove a notebook from the library

        Args:
            notebook_id: ID of notebook to remove

        Returns:
            True if removed, False if not found
        """
        if notebook_id in self.notebooks:
            del self.notebooks[notebook_id]

            # Clear active if it was removed
            if self.active_notebook_id == notebook_id:
                self.active_notebook_id = None
                # Set new active if there are other notebooks
                if self.notebooks:
                    self.active_notebook_id = list(self.notebooks.keys())[0]

            self._save_library()
            print(f"✅ Removed notebook: {notebook_id}")
            return True

        print(f"⚠️ Notebook not found: {notebook_id}")
        return False

    def update_notebook(
        self,
        notebook_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        topics: Optional[List[str]] = None,
        content_types: Optional[List[str]] = None,
        use_cases: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        url: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update notebook metadata

        Args:
            notebook_id: ID of notebook to update
            Other args: Fields to update (None = keep existing)

        Returns:
            Updated notebook object
        """
        if notebook_id not in self.notebooks:
            raise ValueError(f"Notebook not found: {notebook_id}")

        notebook = self.notebooks[notebook_id]

        # Update fields if provided
        if name is not None:
            notebook['name'] = name
        if description is not None:
            notebook['description'] = description
        if topics is not None:
            notebook['topics'] = topics
        if content_types is not None:
            notebook['content_types'] = content_types
        if use_cases is not None:
            notebook['use_cases'] = use_cases
        if tags is not None:
            notebook['tags'] = tags
        if url is not None:
            notebook['url'] = url

        notebook['updated_at'] = datetime.now().isoformat()

        self._save_library()
        print(f"✅ Updated notebook: {notebook['name']}")
        return notebook

    def get_notebook(self, notebook_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific notebook by ID"""
        return self.notebooks.get(notebook_id)

    def list_notebooks(self) -> List[Dict[str, Any]]:
        """List all notebooks in the library"""
        return list(self.notebooks.values())

    def search_notebooks(self, query: str) -> List[Dict[str, Any]]:
        """
        Search notebooks by query

        Args:
            query: Search query (searches name, description, topics, tags)

        Returns:
            List of matching notebooks
        """
        query_lower = query.lower()
        results = []

        for notebook in self.notebooks.values():
            # Search in various fields
            searchable = [
                notebook['name'].lower(),
                notebook['description'].lower(),
                ' '.join(notebook['topics']).lower(),
                ' '.join(notebook['tags']).lower(),
                ' '.join(notebook.get('use_cases', [])).lower()
            ]

            if any(query_lower in field for field in searchable):
                results.append(notebook)

        return results

    def select_notebook(self, notebook_id: str) -> Dict[str, Any]:
        """
        Set a notebook as active

        Args:
            notebook_id: ID of notebook to activate

        Returns:
            The activated notebook
        """
        if notebook_id not in self.notebooks:
            raise ValueError(f"Notebook not found: {notebook_id}")

        self.active_notebook_id = notebook_id
        self._save_library()

        notebook = self.notebooks[notebook_id]
        print(f"✅ Activated notebook: {notebook['name']}")
        return notebook

    def get_active_notebook(self) -> Optional[Dict[str, Any]]:
        """Get the currently active notebook"""
        if self.active_notebook_id:
            return self.notebooks.get(self.active_notebook_id)
        return None

    def increment_use_count(self, notebook_id: str) -> Dict[str, Any]:
        """
        Increment usage counter for a notebook

        Args:
            notebook_id: ID of notebook that was used

        Returns:
            Updated notebook
        """
        if notebook_id not in self.notebooks:
            raise ValueError(f"Notebook not found: {notebook_id}")

        notebook = self.notebooks[notebook_id]
        notebook['use_count'] += 1
        notebook['last_used'] = datetime.now().isoformat()

        self._save_library()
        return notebook

    def get_stats(self) -> Dict[str, Any]:
        """Get library statistics"""
        total_notebooks = len(self.notebooks)
        total_topics = set()
        total_use_count = 0

        for notebook in self.notebooks.values():
            total_topics.update(notebook['topics'])
            total_use_count += notebook['use_count']

        # Find most used
        most_used = None
        if self.notebooks:
            most_used = max(
                self.notebooks.values(),
                key=lambda n: n['use_count']
            )

        return {
            'total_notebooks': total_notebooks,
            'total_topics': len(total_topics),
            'total_use_count': total_use_count,
            'active_notebook': self.get_active_notebook(),
            'most_used_notebook': most_used,
            'library_path': str(self.library_file)
        }


def main():
    """Command-line interface for notebook management"""
    parser = argparse.ArgumentParser(description='Manage NotebookLM library')

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add a notebook')
    add_parser.add_argument('--url', required=True, help='NotebookLM URL')
    add_parser.add_argument('--name', required=True, help='Display name')
    add_parser.add_argument('--description', required=True, help='Description')
    add_parser.add_argument('--topics', required=True, help='Comma-separated topics')
    add_parser.add_argument('--use-cases', help='Comma-separated use cases')
    add_parser.add_argument('--tags', help='Comma-separated tags')

    # List command
    subparsers.add_parser('list', help='List all notebooks')

    # Search command
    search_parser = subparsers.add_parser('search', help='Search notebooks')
    search_parser.add_argument('--query', required=True, help='Search query')

    # Activate command
    activate_parser = subparsers.add_parser('activate', help='Set active notebook')
    activate_parser.add_argument('--id', required=True, help='Notebook ID')

    # Remove command
    remove_parser = subparsers.add_parser('remove', help='Remove a notebook')
    remove_parser.add_argument('--id', required=True, help='Notebook ID')

    # Stats command
    subparsers.add_parser('stats', help='Show library statistics')

    args = parser.parse_args()

    # Initialize library
    library = NotebookLibrary()

    # Execute command
    if args.command == 'add':
        topics = [t.strip() for t in args.topics.split(',')]
        use_cases = [u.strip() for u in args.use_cases.split(',')] if args.use_cases else None
        tags = [t.strip() for t in args.tags.split(',')] if args.tags else None

        notebook = library.add_notebook(
            url=args.url,
            name=args.name,
            description=args.description,
            topics=topics,
            use_cases=use_cases,
            tags=tags
        )
        print(json.dumps(notebook, indent=2))

    elif args.command == 'list':
        notebooks = library.list_notebooks()
        if notebooks:
            print("\n📚 Notebook Library:")
            for notebook in notebooks:
                active = " [ACTIVE]" if notebook['id'] == library.active_notebook_id else ""
                print(f"\n  📓 {notebook['name']}{active}")
                print(f"     ID: {notebook['id']}")
                print(f"     Topics: {', '.join(notebook['topics'])}")
                print(f"     Uses: {notebook['use_count']}")
        else:
            print("📚 Library is empty. Add notebooks with: notebook_manager.py add")

    elif args.command == 'search':
        results = library.search_notebooks(args.query)
        if results:
            print(f"\n🔍 Found {len(results)} notebooks:")
            for notebook in results:
                print(f"\n  📓 {notebook['name']} ({notebook['id']})")
                print(f"     {notebook['description']}")
        else:
            print(f"🔍 No notebooks found for: {args.query}")

    elif args.command == 'activate':
        notebook = library.select_notebook(args.id)
        print(f"Now using: {notebook['name']}")

    elif args.command == 'remove':
        if library.remove_notebook(args.id):
            print("Notebook removed from library")

    elif args.command == 'stats':
        stats = library.get_stats()
        print("\n📊 Library Statistics:")
        print(f"  Total notebooks: {stats['total_notebooks']}")
        print(f"  Total topics: {stats['total_topics']}")
        print(f"  Total uses: {stats['total_use_count']}")
        if stats['active_notebook']:
            print(f"  Active: {stats['active_notebook']['name']}")
        if stats['most_used_notebook']:
            print(f"  Most used: {stats['most_used_notebook']['name']} ({stats['most_used_notebook']['use_count']} uses)")
        print(f"  Library path: {stats['library_path']}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
```

## File: `scripts/run.py`
```python
#!/usr/bin/env python3
"""
Universal runner for NotebookLM skill scripts
Ensures all scripts run with the correct virtual environment
"""

import os
import sys
import subprocess
from pathlib import Path


def get_venv_python():
    """Get the virtual environment Python executable"""
    skill_dir = Path(__file__).parent.parent
    venv_dir = skill_dir / ".venv"

    if os.name == 'nt':  # Windows
        venv_python = venv_dir / "Scripts" / "python.exe"
    else:  # Unix/Linux/Mac
        venv_python = venv_dir / "bin" / "python"

    return venv_python


def ensure_venv():
    """Ensure virtual environment exists"""
    skill_dir = Path(__file__).parent.parent
    venv_dir = skill_dir / ".venv"
    setup_script = skill_dir / "scripts" / "setup_environment.py"

    # Check if venv exists
    if not venv_dir.exists():
        print("🔧 First-time setup: Creating virtual environment...")
        print("   This may take a minute...")

        # Run setup with system Python
        result = subprocess.run([sys.executable, str(setup_script)])
        if result.returncode != 0:
            print("❌ Failed to set up environment")
            sys.exit(1)

        print("✅ Environment ready!")

    return get_venv_python()


def main():
    """Main runner"""
    if len(sys.argv) < 2:
        print("Usage: python run.py <script_name> [args...]")
        print("\nAvailable scripts:")
        print("  ask_question.py    - Query NotebookLM")
        print("  notebook_manager.py - Manage notebook library")
        print("  session_manager.py  - Manage sessions")
        print("  auth_manager.py     - Handle authentication")
        print("  cleanup_manager.py  - Clean up skill data")
        sys.exit(1)

    script_name = sys.argv[1]
    script_args = sys.argv[2:]

    # Handle both "scripts/script.py" and "script.py" formats
    if script_name.startswith('scripts/'):
        # Remove the scripts/ prefix if provided
        script_name = script_name[8:]  # len('scripts/') = 8

    # Ensure .py extension
    if not script_name.endswith('.py'):
        script_name += '.py'

    # Get script path
    skill_dir = Path(__file__).parent.parent
    script_path = skill_dir / "scripts" / script_name

    if not script_path.exists():
        print(f"❌ Script not found: {script_name}")
        print(f"   Working directory: {Path.cwd()}")
        print(f"   Skill directory: {skill_dir}")
        print(f"   Looked for: {script_path}")
        sys.exit(1)

    # Ensure venv exists and get Python executable
    venv_python = ensure_venv()

    # Build command
    cmd = [str(venv_python), str(script_path)] + script_args

    # Run the script
    try:
        result = subprocess.run(cmd)
        sys.exit(result.returncode)
    except KeyboardInterrupt:
        print("\n⚠️ Interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `scripts/setup_environment.py`
```python
#!/usr/bin/env python3
"""
Environment Setup for NotebookLM Skill
Manages virtual environment and dependencies automatically
"""

import os
import sys
import subprocess
import venv
from pathlib import Path


class SkillEnvironment:
    """Manages skill-specific virtual environment"""

    def __init__(self):
        # Skill directory paths
        self.skill_dir = Path(__file__).parent.parent
        self.venv_dir = self.skill_dir / ".venv"
        self.requirements_file = self.skill_dir / "requirements.txt"

        # Python executable in venv
        if os.name == 'nt':  # Windows
            self.venv_python = self.venv_dir / "Scripts" / "python.exe"
            self.venv_pip = self.venv_dir / "Scripts" / "pip.exe"
        else:  # Unix/Linux/Mac
            self.venv_python = self.venv_dir / "bin" / "python"
            self.venv_pip = self.venv_dir / "bin" / "pip"

    def ensure_venv(self) -> bool:
        """Ensure virtual environment exists and is set up"""

        # Check if we're already in the correct venv
        if self.is_in_skill_venv():
            print("✅ Already running in skill virtual environment")
            return True

        # Create venv if it doesn't exist
        if not self.venv_dir.exists():
            print(f"🔧 Creating virtual environment in {self.venv_dir.name}/")
            try:
                venv.create(self.venv_dir, with_pip=True)
                print("✅ Virtual environment created")
            except Exception as e:
                print(f"❌ Failed to create venv: {e}")
                return False

        # Install/update dependencies
        if self.requirements_file.exists():
            print("📦 Installing dependencies...")
            try:
                # Upgrade pip first
                subprocess.run(
                    [str(self.venv_pip), "install", "--upgrade", "pip"],
                    check=True,
                    capture_output=True,
                    text=True
                )

                # Install requirements
                result = subprocess.run(
                    [str(self.venv_pip), "install", "-r", str(self.requirements_file)],
                    check=True,
                    capture_output=True,
                    text=True
                )
                print("✅ Dependencies installed")

                # Install Chrome for Patchright (not Chromium!)
                # Using real Chrome ensures cross-platform reliability and consistent browser fingerprinting
                # See: https://github.com/Kaliiiiiiiiii-Vinyzu/patchright-python#anti-detection
                print("🌐 Installing Google Chrome for Patchright...")
                try:
                    subprocess.run(
                        [str(self.venv_python), "-m", "patchright", "install", "chrome"],
                        check=True,
                        capture_output=True,
                        text=True
                    )
                    print("✅ Chrome installed")
                except subprocess.CalledProcessError as e:
                    print(f"⚠️ Warning: Failed to install Chrome: {e}")
                    print("   You may need to run manually: python -m patchright install chrome")
                    print("   Chrome is required (not Chromium) for reliability!")

                return True
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to install dependencies: {e}")
                print(f"   Output: {e.output if hasattr(e, 'output') else 'No output'}")
                return False
        else:
            print("⚠️ No requirements.txt found, skipping dependency installation")
            return True

    def is_in_skill_venv(self) -> bool:
        """Check if we're already running in the skill's venv"""
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            # We're in a venv, check if it's ours
            venv_path = Path(sys.prefix)
            return venv_path == self.venv_dir
        return False

    def get_python_executable(self) -> str:
        """Get the correct Python executable to use"""
        if self.venv_python.exists():
            return str(self.venv_python)
        return sys.executable

    def run_script(self, script_name: str, args: list = None) -> int:
        """Run a script with the virtual environment"""
        script_path = self.skill_dir / "scripts" / script_name

        if not script_path.exists():
            print(f"❌ Script not found: {script_path}")
            return 1

        # Ensure venv is set up
        if not self.ensure_venv():
            print("❌ Failed to set up environment")
            return 1

        # Build command
        cmd = [str(self.venv_python), str(script_path)]
        if args:
            cmd.extend(args)

        print(f"🚀 Running: {script_name} with venv Python")

        try:
            # Run the script with venv Python
            result = subprocess.run(cmd)
            return result.returncode
        except Exception as e:
            print(f"❌ Failed to run script: {e}")
            return 1

    def activate_instructions(self) -> str:
        """Get instructions for manual activation"""
        if os.name == 'nt':
            activate = self.venv_dir / "Scripts" / "activate.bat"
            return f"Run: {activate}"
        else:
            activate = self.venv_dir / "bin" / "activate"
            return f"Run: source {activate}"


def main():
    """Main entry point for environment setup"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Setup NotebookLM skill environment'
    )

    parser.add_argument(
        '--check',
        action='store_true',
        help='Check if environment is set up'
    )

    parser.add_argument(
        '--run',
        help='Run a script with the venv (e.g., --run ask_question.py)'
    )

    parser.add_argument(
        'args',
        nargs='*',
        help='Arguments to pass to the script'
    )

    args = parser.parse_args()

    env = SkillEnvironment()

    if args.check:
        if env.venv_dir.exists():
            print(f"✅ Virtual environment exists: {env.venv_dir}")
            print(f"   Python: {env.get_python_executable()}")
            print(f"   To activate manually: {env.activate_instructions()}")
        else:
            print(f"❌ No virtual environment found")
            print(f"   Run setup_environment.py to create it")
        return

    if args.run:
        # Run a script with venv
        return env.run_script(args.run, args.args)

    # Default: ensure environment is set up
    if env.ensure_venv():
        print("\n✅ Environment ready!")
        print(f"   Virtual env: {env.venv_dir}")
        print(f"   Python: {env.get_python_executable()}")
        print(f"\nTo activate manually: {env.activate_instructions()}")
        print(f"Or run scripts directly: python setup_environment.py --run script_name.py")
    else:
        print("\n❌ Environment setup failed")
        return 1


if __name__ == "__main__":
    sys.exit(main() or 0)
```

## File: `scripts/__init__.py`
```python
#!/usr/bin/env python3
"""
NotebookLM Skill Scripts Package
Provides automatic environment management for all scripts
"""

import os
import sys
import subprocess
from pathlib import Path


def ensure_venv_and_run():
    """
    Ensure virtual environment exists and run the requested script.
    This is called when any script is imported or run directly.
    """
    # Only do this if we're not already in the skill's venv
    skill_dir = Path(__file__).parent.parent
    venv_dir = skill_dir / ".venv"

    # Check if we're in a venv
    in_venv = hasattr(sys, 'real_prefix') or (
        hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
    )

    # Check if it's OUR venv
    if in_venv:
        venv_path = Path(sys.prefix)
        if venv_path == venv_dir:
            # We're already in the correct venv
            return

    # We need to set up or switch to our venv
    if not venv_dir.exists():
        print("🔧 First-time setup detected...")
        print("   Creating isolated environment for NotebookLM skill...")
        print("   This ensures clean dependency management...")

        # Create venv
        import venv
        venv.create(venv_dir, with_pip=True)

        # Install requirements
        requirements_file = skill_dir / "requirements.txt"
        if requirements_file.exists():
            if os.name == 'nt':  # Windows
                pip_exe = venv_dir / "Scripts" / "pip.exe"
            else:
                pip_exe = venv_dir / "bin" / "pip"

            print("   Installing dependencies in isolated environment...")
            subprocess.run(
                [str(pip_exe), "install", "-q", "-r", str(requirements_file)],
                check=True
            )

            # Also install patchright's chromium
            print("   Setting up browser automation...")
            if os.name == 'nt':
                python_exe = venv_dir / "Scripts" / "python.exe"
            else:
                python_exe = venv_dir / "bin" / "python"

            subprocess.run(
                [str(python_exe), "-m", "patchright", "install", "chromium"],
                check=True,
                capture_output=True
            )

        print("✅ Environment ready! All dependencies isolated in .venv/")

    # If we're here and not in the venv, we should recommend using the venv
    if not in_venv:
        print("\n⚠️  Running outside virtual environment")
        print("   Recommended: Use scripts/run.py to ensure clean execution")
        print("   Or activate: source .venv/bin/activate")


# Check environment when module is imported
ensure_venv_and_run()
```


---
id: remorses-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:08.449360
---

# KNOWLEDGE EXTRACT: remorses
> **Extracted on:** 2026-03-30 17:53:00
> **Source:** remorses

---

## File: `tuistory.md`
```markdown
# 📦 remorses/tuistory [🔖 PENDING/APPROVE]
🔗 https://github.com/remorses/tuistory


## Meta
- **Stars:** ⭐ 275 | **Forks:** 🍴 2
- **Language:** TypeScript | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Playwright for terminal user interfaces

## README (trích đầu)
```
<div align='center'>
    <br/>
    <br/>
    <h3>tuistory</h3>
    <p>Playwright for terminal user interfaces</p>
    <p>Write end-to-end tests for terminal applications</p>
    <br/>
    <br/>
</div>

## Installation

```bash
# As a library
bun add tuistory
npm install tuistory

# As a CLI (global)
bun add -g tuistory
npm install -g tuistory

# Or use directly with npx/bunx
npx tuistory --help
```

## CLI Usage

tuistory provides a CLI for interacting with terminal sessions from the command line or shell scripts.

### Quick Start

```bash
# Launch Claude Code
tuistory launch "claude" -s claude --cols 150 --rows 45

# Wait for it to load
tuistory -s claude wait "Claude Code" --timeout 15000

# Type a prompt
tuistory -s claude type "what is 2+2? reply with just the number"
tuistory -s claude press enter

# Wait for Claude's response using regex (matches any digit)
tuistory -s claude wait "/[0-9]+/" --timeout 30000

# Get terminal snapshot
tuistory -s claude snapshot --trim
# Output:
# ╭─────────────────────────────────────────────────────────────────────────────────╮
# │ ● Claude Code                                                                   │
# ╰─────────────────────────────────────────────────────────────────────────────────╯
#
# > what is 2+2? reply with just the number
#
# 4
#
# ────────────────────────────────────────────────────────────────────────────────────
# > 

# Close the session
tuistory -s claude close
```

### Debugging Node.js with tuistory

```bash
# Launch Node.js debugger (assuming app.js has a debugger statement)
tuistory launch "node inspect app.js" -s debug --cols 120

# Wait for debugger to start and continue to breakpoint
tuistory -s debug wait "Break on start"
tuistory -s debug type "cont"
tuistory -s debug press enter
tuistory -s debug wait "break in"
tuistory -s debug snapshot --trim

# Print stack trace with bt (backtrace)
tuistory -s debug type "bt"
tuistory -s debug press enter
tuistory -s debug snapshot --trim
# Output:
# #0 getPrice app.js:13:2
# #1 calculateTotal app.js:7:15
# #2 processOrder app.js:2:16

# Enter REPL mode to inspect variables
tuistory -s debug type "repl"
tuistory -s debug press enter
tuistory -s debug type "item"
tuistory -s debug press enter
tuistory -s debug snapshot --trim
# Output:
# > item
# { name: 'Widget', price: 25, quantity: 2 }

# Clean up
tuistory -s debug close
```

### CLI Commands Reference

```bash
tuistory launch <command>     # Start a terminal session
tuistory snapshot             # Get terminal text content
tuistory type <text>          # Type text character by character
tuistory press <key> [keys]   # Press key(s): enter, ctrl c, alt f4
tuistory click <pattern>      # Click on text matching pattern
tuistory wait <pattern>       # Wait for text (supports /regex/)
tuistory wait-idle            # Wait for terminal to stabilize
tuistory scroll <up|down>     # Scroll the terminal
tuistory resize <cols> <rows> # Resize terminal
tuistory close                # Close a sessio
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


---
id: claude-code-status-line-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:03.007256
---

# KNOWLEDGE EXTRACT: claude-code-status-line
> **Extracted on:** 2026-03-30 13:19:54
> **Source:** claude-code-status-line

---

## File: `README.md`
```markdown
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

## File: `status-line.sh`
```bash
#!/bin/bash

# Simple status line - shows model and context usage only

data=$(cat)

# Get model name
model=$(echo "$data" | jq -r '.model.display_name // .model.id // "unknown"')

# Get context info
max_ctx=$(echo "$data" | jq -r '.context_window.context_window_size // 200000')
used_pct=$(echo "$data" | jq -r '.context_window.used_percentage // empty')

# Color codes
BLUE='\033[34m'
RED='\033[31m'
RESET='\033[0m'

# Format context display
if [ -z "$used_pct" ] || [ "$used_pct" = "null" ]; then
    # Loading state - empty circles
    context_info="○○○○○○○○○○ loading..."
else
    pct=$(printf "%.0f" "$used_pct" 2>/dev/null || echo "$used_pct")
    [ "$pct" -gt 100 ] 2>/dev/null && pct=100

    # Calculate tokens in k
    used_k=$(( max_ctx * pct / 100 / 1000 ))
    max_k=$(( max_ctx / 1000 ))

    # Build circle bar (10 segments)
    bar=""
    filled=$(( pct / 10 ))

    # Blue by default, red when > 60%
    if [ "$pct" -gt 60 ]; then
        COLOR="$RED"
    else
        COLOR="$BLUE"
    fi

    for i in 0 1 2 3 4 5 6 7 8 9; do
        if [ "$i" -lt "$filled" ]; then
            bar="${bar}${COLOR}●${RESET}"
        else
            bar="${bar}○"
        fi
    done

    context_info="${bar} ${used_k}k/${max_k}k (${pct}% used)"
fi

# Output: Model | Context
printf '%b\n' "${model} | ${context_info}"
```


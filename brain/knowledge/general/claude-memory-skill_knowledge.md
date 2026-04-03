---
id: claude-memory-skill-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:04.358410
---

# KNOWLEDGE EXTRACT: claude-memory-skill
> **Extracted on:** 2026-03-30 13:15:20
> **Source:** claude-memory-skill

---

## File: `install.sh`
```bash
#!/bin/bash

set -e

CLAUDE_DIR="$HOME/.claude"
MEMORY_DIR="$CLAUDE_DIR/memory"
COMMANDS_DIR="$CLAUDE_DIR/commands"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing Claude Memory Skill..."

# Create directories
mkdir -p "$MEMORY_DIR/topics"
mkdir -p "$MEMORY_DIR/projects"
mkdir -p "$COMMANDS_DIR"

# Copy skill file
if [ -f "$SCRIPT_DIR/skill/mem.md" ]; then
    cp "$SCRIPT_DIR/skill/mem.md" "$COMMANDS_DIR/mem.md"
else
    # Inline skill content for curl install
    cat > "$COMMANDS_DIR/mem.md" << 'SKILL_EOF'
# Memory Skill

You have a persistent hierarchical memory system at `~/.claude/memory/`.

## Structure

```
~/.claude/memory/
├── core.md              # Summaries + pointers (always loaded)
├── me.md                # About the user (always loaded)
├── topics/
│   └── <topic>.md       # Detailed entries by topic
└── projects/
    └── <project>.md     # Project-specific knowledge
```

## Commands

### `/mem load` — Session Start

Run in background at session start. Spawns a memory agent to:
1. Read `~/.claude/memory/me.md`
2. Read `~/.claude/memory/core.md`
3. If in a git repo, check for `projects/<project>.md`
4. Return a context summary

**Usage:** At the start of a session, spawn a background agent:
```
Task(subagent_type="general-purpose", run_in_background=true, prompt="""
Memory load task. Read and summarize:
1. ~/.claude/memory/me.md (who the user is)
2. ~/.claude/memory/core.md (key learnings + pointers)
3. Check if projects/<current-project>.md exists

Return a brief context summary for the main agent.
""")
```

### `/mem save <observation>` — Persist Learning

Run in background when you learn something worth keeping. Spawns a memory agent to:
1. Categorize the observation (pick or create a topic)
2. Append to `topics/<topic>.md` with format:
   ```markdown
   ## <Short title> [YYYY-MM-DD]
   <The insight in 1-3 sentences>
   ```
3. If this is a significant/recurring insight, update `core.md`:
   ```markdown
   ## <Topic>
   <One-line summary>
   → topics/<topic>.md
   ```

**Usage:** Spawn a background agent:
```
Task(subagent_type="general-purpose", run_in_background=true, prompt="""
Memory save task. Observation to save:
"<the observation>"

1. Determine the topic (debugging, patterns, tools, <domain>, etc.)
2. Read ~/.claude/memory/topics/<topic>.md if it exists
3. Append the observation with timestamp
4. If this represents a significant pattern, update core.md with a summary + pointer
""")
```

### `/mem recall <query>` — Retrieve Context

Run when you need specific context. Can block if context is immediately needed.
1. Grep `core.md` for relevant topics
2. Follow pointers to load matching topic files
3. Return relevant entries

**Usage:** Spawn an agent (can be blocking):
```
Task(subagent_type="general-purpose", prompt="""
Memory recall task. Query: "<the query>"

1. Read ~/.claude/memory/core.md
2. Identify relevant topic pointers
3. Read those topic files
4. Return entries relevant to the query
""")
```

### `/mem show` — Display State

Show current memory structure and contents.
1. List all files in `~/.claude/memory/`
2. Show contents of `core.md`
3. Show summary of each topic file (first few lines)

### `/mem forget <topic>` — Remove Entries

Remove a topic or specific entries.
1. Delete `topics/<topic>.md` if removing whole topic
2. Remove corresponding entry from `core.md`

## When to Save

Save silently in background when:
- User explicitly says "remember..." or similar
- You solve a non-trivial problem
- You discover a user preference
- You learn something project-specific
- A pattern emerges across multiple interactions

## When to Recall

Recall when:
- Starting unfamiliar work (check for relevant past learnings)
- Stuck on a problem (search for similar past issues)
- User asks "do you remember..."
- Context from memory would clearly help

## Principles

- **Background ops**: Load and save don't block the main agent
- **Hierarchical**: core.md summaries → topic details
- **Categorized**: No dumping ground, everything has a topic
- **Atomic entries**: One `##` block = one memory
- **User editable**: Plain markdown, user can edit anytime
SKILL_EOF
fi

# Create template files if they don't exist
if [ ! -f "$MEMORY_DIR/me.md" ]; then
    cat > "$MEMORY_DIR/me.md" << 'EOF'
# About the User

<!-- Add facts about yourself: role, preferences, tech stack, etc. -->
<!-- Claude loads this at every session start. -->

EOF
    echo "Created $MEMORY_DIR/me.md"
fi

if [ ! -f "$MEMORY_DIR/core.md" ]; then
    cat > "$MEMORY_DIR/core.md" << 'EOF'
# Core Memory

<!-- Summaries + pointers to topic files -->
<!-- Updated by memory agent when topics accumulate significant insights -->

EOF
    echo "Created $MEMORY_DIR/core.md"
fi

# Add hook to CLAUDE.md
HOOK_TEXT="## Memory

I have a hierarchical memory system at \`~/.claude/memory/\`.

**Session start:** Run \`/mem load\` in background to load context.
**During session:** Run \`/mem save <observation>\` in background when I learn something worth keeping.
**When stuck:** Run \`/mem recall <query>\` to retrieve relevant past learnings.

Memory structure: \`core.md\` (summaries + pointers) → \`topics/<topic>.md\` (details)"

if [ -f "$CLAUDE_DIR/CLAUDE.md" ]; then
    if grep -q "hierarchical memory" "$CLAUDE_DIR/CLAUDE.md"; then
        echo "Memory hook already exists in CLAUDE.md"
    else
        # Remove old memory hook if present
        if grep -q "persistent memory" "$CLAUDE_DIR/CLAUDE.md"; then
            echo "Updating existing memory hook..."
            # Create backup
            cp "$CLAUDE_DIR/CLAUDE.md" "$CLAUDE_DIR/CLAUDE.md.bak"
        fi
        echo "" >> "$CLAUDE_DIR/CLAUDE.md"
        echo "$HOOK_TEXT" >> "$CLAUDE_DIR/CLAUDE.md"
        echo "Added memory hook to existing CLAUDE.md"
    fi
else
    echo "# Claude Code Settings" > "$CLAUDE_DIR/CLAUDE.md"
    echo "" >> "$CLAUDE_DIR/CLAUDE.md"
    echo "$HOOK_TEXT" >> "$CLAUDE_DIR/CLAUDE.md"
    echo "Created $CLAUDE_DIR/CLAUDE.md with memory hook"
fi

echo ""
echo "Installation complete!"
echo ""
echo "Next steps:"
echo "  1. Edit ~/.claude/memory/me.md with facts about yourself"
echo "  2. Start a new Claude Code session"
echo "  3. Claude will now remember things across sessions"
echo ""
echo "Commands:"
echo "  /mem load      - load memory context (runs at session start)"
echo "  /mem save X    - save an observation"
echo "  /mem recall X  - retrieve relevant memories"
echo "  /mem show      - see memory structure"
echo "  /mem forget X  - remove memories about X"
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2024

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
# claude-memory-skill

```
╔══●══●══●══════════════════════════════════════════════╗
║                                                       ║
║  > tree ~/.claude/memory                              ║
║                                                       ║
║    ├── core.md          claude-memory-skill           ║
║    ├── topics/          ───────────────────           ║
║    │   └── *.md         a skill is all you need       ║
║    └── me.md                                          ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

> *An embarrassingly simple and minimal implementation for agentic memory.*
>
> No databases. No embeddings. No semantic search. Just markdown files and a skill that teaches Claude when to read and write.

## The Problem

Claude Code forgets everything between sessions. Built-in auto-memory exists but:
- It's opaque (Claude decides what's "meaningful")
- Limited to 200 lines loaded at startup
- Not tightly integrated into the agentic loop
- No hierarchical organization (scales poorly)

## The Solution

A skill-based memory protocol with:
- **Hierarchical storage**: `core.md` summaries → `topics/<topic>.md` details
- **Background agents**: Memory ops don't block the main agent
- **Categorized entries**: No dumping ground, everything has a topic
- **Filesystem-based**: Robust, inspectable, git-trackable

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/hanfang/claude-memory-skill/main/install.sh | bash
```

Or clone and run locally:

```bash
git clone https://github.com/hanfang/claude-memory-skill.git
cd claude-memory-skill
./install.sh
```

## What Gets Installed

```
~/.claude/
├── CLAUDE.md              # Hook added (or created)
├── commands/
│   └── mem.md             # The memory skill
└── memory/
    ├── core.md            # Summaries + pointers (always loaded)
    ├── me.md              # About you (always loaded)
    ├── topics/            # Detailed entries by topic
    │   └── <topic>.md
    └── projects/          # Project-specific memories
        └── <project>.md
```

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  Main Agent                                         │
│  - Focuses on user's task                           │
│  - Spawns memory agent when needed                  │
│  - Doesn't wait (background)                        │
└─────────────────────┬───────────────────────────────┘
                      │ spawn (background)
                      ▼
┌─────────────────────────────────────────────────────┐
│  Memory Agent                                       │
│  - Reads core.md + relevant topics                  │
│  - Writes to topic files                            │
│  - Updates core.md summaries                        │
└─────────────────────────────────────────────────────┘
```

## How It Works

### Agent-Initiated (Automatic)

These run automatically — you don't invoke them:

| Action | When | Blocking |
|--------|------|----------|
| `load` | Session start | No |
| `save` | Claude learns something useful | No |
| `recall` | Claude needs context | No |

### User-Initiated (Manual)

These are for you to inspect and manage memory:

| Command | Description |
|---------|-------------|
| `/mem show` | Display memory structure and contents |
| `/mem forget <topic>` | Remove a topic or specific entries |

### Tell Claude What to Remember

Just say it naturally:
- "Remember that we use pnpm, not npm"
- "Save that the API requires auth headers"
- "Note that tests need Redis running"

### Fill In Your Profile

Edit `~/.claude/memory/me.md` with facts about yourself:

```markdown
# About the User

- AI researcher, focus on agents and RL
- Prefer explicit code over clever abstractions
- Python, PyTorch, JAX
```

### Hierarchical Memory

**core.md** (always loaded):
```markdown
# Core Memory

## Debugging
Mostly async/timing issues. Prefer explicit logging.
→ topics/debugging.md

## RL Research
PPO tuning, reward shaping experiments.
→ topics/rl.md
```

**topics/debugging.md** (loaded on demand):
```markdown
## Async race condition fix [2024-01-15]
Added explicit locks around shared state access.

## Redis timeout debugging [2024-01-10]
Default timeout was too short for large payloads.
```

### Write Flow

1. Learn something → spawn background memory agent
2. Agent categorizes → finds or creates topic file
3. Agent appends entry with timestamp
4. If significant, agent updates core.md summary

### Read Flow

1. Session start → agent reads core.md + me.md in background
2. When stuck → agent follows pointers to relevant topics
3. Returns context to main agent

## Design Principles

- **Background ops**: Memory doesn't block the main agent
- **Hierarchical**: Summaries in core.md, details in topics
- **Categorized**: Every entry belongs to a topic
- **Atomic entries**: One `##` block = one memory
- **No semantic search**: Deterministic, grep-based retrieval
- **User editable**: Plain markdown, edit anytime

## Uninstall

```bash
rm -rf ~/.claude/memory
rm ~/.claude/commands/mem.md
# Manually remove the memory hook from ~/.claude/CLAUDE.md
```

## License

MIT
```

## File: `skill/mem.md`
```markdown
# Memory Skill

You have a persistent hierarchical memory system at `~/.claude/memory/`.

## Structure

```
~/.claude/memory/
├── core.md              # Summaries + pointers (always loaded)
├── me.md                # About the user (always loaded)
├── topics/
│   └── <topic>.md       # Detailed entries by topic
└── projects/
    └── <project>.md     # Project-specific knowledge
```

## Agent-Initiated Actions (Automatic)

These are NOT user commands. You (Claude) run these proactively.

### `load` — Session Start

Run in background at session start. Spawns a memory agent to:
1. Read `~/.claude/memory/me.md`
2. Read `~/.claude/memory/core.md`
3. If in a git repo, check for `projects/<project>.md`
4. Return a context summary

**Usage:** At the start of a session, spawn a background agent:
```
Task(subagent_type="general-purpose", run_in_background=true, prompt="""
Memory load task. Read and summarize:
1. ~/.claude/memory/me.md (who the user is)
2. ~/.claude/memory/core.md (key learnings + pointers)
3. Check if projects/<current-project>.md exists

Return a brief context summary for the main agent.
""")
```

### `save` — Persist Learning

Run in background when you learn something worth keeping. Spawns a memory agent to:
1. Categorize the observation (pick or create a topic)
2. Append to `topics/<topic>.md` with format:
   ```markdown
   ## <Short title> [YYYY-MM-DD]
   <The insight in 1-3 sentences>
   ```
3. If this is a significant/recurring insight, update `core.md`:
   ```markdown
   ## <Topic>
   <One-line summary>
   → topics/<topic>.md
   ```

**Usage:** Spawn a background agent:
```
Task(subagent_type="general-purpose", run_in_background=true, prompt="""
Memory save task. Observation to save:
"<the observation>"

1. Determine the topic (debugging, patterns, tools, <domain>, etc.)
2. Read ~/.claude/memory/topics/<topic>.md if it exists
3. Append the observation with timestamp
4. If this represents a significant pattern, update core.md with a summary + pointer
""")
```

### `recall` — Retrieve Context

Run when you need specific context. Can block if context is immediately needed.
1. Grep `core.md` for relevant topics
2. Follow pointers to load matching topic files
3. Return relevant entries

**Usage:** Spawn an agent (can be blocking):
```
Task(subagent_type="general-purpose", prompt="""
Memory recall task. Query: "<the query>"

1. Read ~/.claude/memory/core.md
2. Identify relevant topic pointers
3. Read those topic files
4. Return entries relevant to the query
""")
```

## User-Initiated Commands

These are commands the user can invoke.

### `/mem show` — Display State

Show current memory structure and contents.
1. List all files in `~/.claude/memory/`
2. Show contents of `core.md`
3. Show summary of each topic file (first few lines)

### `/mem forget <topic>` — Remove Entries

Remove a topic or specific entries.
1. Delete `topics/<topic>.md` if removing whole topic
2. Remove corresponding entry from `core.md`

## When to Save

Save silently in background when:
- User explicitly says "remember..." or similar
- You solve a non-trivial problem
- You discover a user preference
- You learn something project-specific
- A pattern emerges across multiple interactions

## When to Recall

Recall when:
- Starting unfamiliar work (check for relevant past learnings)
- Stuck on a problem (search for similar past issues)
- User asks "do you remember..."
- Context from memory would clearly help

## Principles

- **Background ops**: Load and save don't block the main agent
- **Hierarchical**: core.md summaries → topic details
- **Categorized**: No dumping ground, everything has a topic
- **Atomic entries**: One `##` block = one memory
- **User editable**: Plain markdown, user can edit anytime
```

## File: `templates/core.md`
```markdown
# Core Memory

<!-- Summaries + pointers to topic files -->
<!-- Updated by memory agent when topics accumulate significant insights -->

```

## File: `templates/me.md`
```markdown
# About the User

<!-- Add facts about yourself: role, preferences, tech stack, etc. -->
<!-- Claude loads this at every session start. -->

```


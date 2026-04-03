---
id: github.com-more-io-claude-apple-bridges-d745d143-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:00.236175
---

# KNOWLEDGE EXTRACT: github.com_more-io_claude-apple-bridges_d745d143
> **Extracted on:** 2026-04-01 12:43:19
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521981/github.com_more-io_claude-apple-bridges_d745d143

---

## File: `.gitignore`
```
# Compiled binaries
reminders-bridge
calendar-bridge
contacts-bridge

# macOS
.DS_Store

# Swift build artifacts
*.o
*.d
```

## File: `CLAUDE.md`
```markdown
# Claude Apple Bridges — Developer Notes

## Compile All Bridges

```bash
# Reminders
cat > /tmp/reminders-info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
    <key>NSRemindersUsageDescription</key>
    <string>Claude Code needs access to Reminders to manage tasks.</string>
</dict></plist>
EOF
swiftc reminders-bridge.swift -o ~/.claude/reminders-bridge -framework EventKit \
  -Xlinker -sectcreate -Xlinker __TEXT -Xlinker __info_plist -Xlinker /tmp/reminders-info.plist
codesign --force --sign - --identifier com.claude.reminders-bridge ~/.claude/reminders-bridge

# Contacts
cat > /tmp/contacts-info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
    <key>NSContactsUsageDescription</key>
    <string>Claude Code needs access to Contacts.</string>
</dict></plist>
EOF
swiftc contacts-bridge.swift -o ~/.claude/contacts-bridge -framework Contacts \
  -Xlinker -sectcreate -Xlinker __TEXT -Xlinker __info_plist -Xlinker /tmp/contacts-info.plist
codesign --force --sign - --identifier com.claude.contacts-bridge ~/.claude/contacts-bridge

# Calendar
cat > /tmp/calendar-info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
    <key>NSCalendarsFullAccessUsageDescription</key>
    <string>Claude Code needs access to Calendar.</string>
</dict></plist>
EOF
swiftc calendar-bridge.swift -o ~/.claude/calendar-bridge -framework EventKit \
  -Xlinker -sectcreate -Xlinker __TEXT -Xlinker __info_plist -Xlinker /tmp/calendar-info.plist
codesign --force --sign - --identifier com.claude.calendar-bridge ~/.claude/calendar-bridge

# Notes (no plist needed)
swiftc notes-bridge.swift -o ~/.claude/notes-bridge
codesign --force --sign - --identifier com.claude.notes-bridge ~/.claude/notes-bridge

# Mail (no plist needed)
swiftc mail-bridge.swift -o ~/.claude/mail-bridge
codesign --force --sign - --identifier com.claude.mail-bridge ~/.claude/mail-bridge

# tmux (no plist needed)
swiftc tmux-bridge.swift -o ~/.claude/tmux-bridge
codesign --force --sign - --identifier com.claude.tmux-bridge ~/.claude/tmux-bridge
```

## Quick Smoke Test

```bash
~/.claude/reminders-bridge lists
~/.claude/reminders-bridge today
~/.claude/reminders-bridge overdue
~/.claude/calendar-bridge today
~/.claude/calendar-bridge free-slots $(date +%Y-%m-%d)
~/.claude/contacts-bridge search "test"
~/.claude/contacts-bridge birthdays-upcoming 30
~/.claude/notes-bridge accounts
~/.claude/mail-bridge accounts
~/.claude/tmux-bridge sessions
```

## Branching

- `main` — stable releases
- `develop` — active development, PRs go here

## notes-bridge: HTML Formatting

The `add` and `append` commands support HTML — Notes.app renders it natively:

```bash
notes-bridge add "Work" "Title" "<b>Bold</b><br><ul><li>Item 1</li><li>Item 2</li></ul>"
notes-bridge append "Title" "<br><b>Update:</b> some text"
```

Supported tags: `<b>`, `<i>`, `<u>`, `<br>`, `<ul>`, `<ol>`, `<li>`, `<h1>`–`<h3>`, `<a href="...">`, `<p>`

`read` always returns plain text (HTML stripped).

## mail-bridge: Send Behavior

- **Without `--force`**: opens Mail.app compose window — user reviews and sends manually
- **With `--force`**: sends directly without UI (use only when explicitly requested)

## Adding a New Bridge

1. Create `<name>-bridge.swift` in repo root
2. Add compile instructions to README.md and CLAUDE.md
3. Add permission grant step to README.md
4. Add to `settings.local.json` allowed tools
5. Add usage examples to README.md
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Tobias Stöger (tstoegi)

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

## File: `Makefile`
```
# Claude Apple Bridges — Makefile
# Copyright © 2026 Tobias Stöger (tstoegi). Licensed under the MIT License.
#
# Usage:
#   make install           Install all bridges to ~/.claude/
#   make install-reminders Install only reminders-bridge
#   make install-calendar  Install only calendar-bridge
#   make install-contacts  Install only contacts-bridge
#   make install-notes     Install only notes-bridge
#   make install-mail      Install only mail-bridge
#   make install-tmux      Install only tmux-bridge
#   make install-skills    Install skills to ~/.claude/skills/apple-bridges/
#   make test              Run smoke tests (triggers permission dialogs on first run)
#   make clean             Remove compiled binaries from ~/.claude/

INSTALL_DIR := $(HOME)/.claude
PLIST_DIR   := /tmp
CODESIGN_IDENTITY ?= -

.PHONY: install install-reminders install-calendar install-contacts install-notes install-mail install-tmux install-skills test clean

SKILLS_DIR := $(INSTALL_DIR)/skills/apple-bridges

install: install-reminders install-contacts install-calendar install-notes install-mail install-tmux install-skills
	@echo ""
	@echo "✅ All bridges installed to $(INSTALL_DIR)"
	@echo ""
	@echo "Next: run each binary once to grant permissions:"
	@echo "  ~/.claude/reminders-bridge lists"
	@echo "  ~/.claude/calendar-bridge today"
	@echo "  ~/.claude/contacts-bridge search test"
	@echo "  ~/.claude/notes-bridge accounts"
	@echo "  ~/.claude/mail-bridge accounts"
	@echo "  ~/.claude/tmux-bridge sessions"

install-skills:
	@echo "→ Installing skills..."
	@mkdir -p $(SKILLS_DIR)
	@cp skills/apple-bridges/*.md $(SKILLS_DIR)/
	@echo "  ✓ Skills installed to $(SKILLS_DIR)"

install-tmux:
	@echo "→ Building tmux-bridge..."
	swiftc tmux-bridge.swift -o $(INSTALL_DIR)/tmux-bridge
	codesign --force --sign "$(CODESIGN_IDENTITY)" --identifier com.claude.tmux-bridge $(INSTALL_DIR)/tmux-bridge
	@echo "  ✓ tmux-bridge installed"

install-reminders:
	@echo "→ Building reminders-bridge..."
	@printf '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>NSRemindersUsageDescription</key><string>Claude Code needs access to Reminders to manage tasks.</string></dict></plist>' > $(PLIST_DIR)/reminders-info.plist
	swiftc reminders-bridge.swift -o $(INSTALL_DIR)/reminders-bridge \
	  -framework EventKit \
	  -Xlinker -sectcreate -Xlinker __TEXT -Xlinker __info_plist -Xlinker $(PLIST_DIR)/reminders-info.plist
	codesign --force --sign "$(CODESIGN_IDENTITY)" --identifier com.claude.reminders-bridge $(INSTALL_DIR)/reminders-bridge
	@echo "  ✓ reminders-bridge installed"

install-contacts:
	@echo "→ Building contacts-bridge..."
	@printf '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>NSContactsUsageDescription</key><string>Claude Code needs access to Contacts to look up and manage contacts.</string></dict></plist>' > $(PLIST_DIR)/contacts-info.plist
	swiftc contacts-bridge.swift -o $(INSTALL_DIR)/contacts-bridge \
	  -framework Contacts \
	  -Xlinker -sectcreate -Xlinker __TEXT -Xlinker __info_plist -Xlinker $(PLIST_DIR)/contacts-info.plist
	codesign --force --sign "$(CODESIGN_IDENTITY)" --identifier com.claude.contacts-bridge $(INSTALL_DIR)/contacts-bridge
	@echo "  ✓ contacts-bridge installed"

install-calendar:
	@echo "→ Building calendar-bridge..."
	@printf '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>NSCalendarsFullAccessUsageDescription</key><string>Claude Code needs access to Calendar to schedule and view events.</string></dict></plist>' > $(PLIST_DIR)/calendar-info.plist
	swiftc calendar-bridge.swift -o $(INSTALL_DIR)/calendar-bridge \
	  -framework EventKit \
	  -Xlinker -sectcreate -Xlinker __TEXT -Xlinker __info_plist -Xlinker $(PLIST_DIR)/calendar-info.plist
	codesign --force --sign "$(CODESIGN_IDENTITY)" --identifier com.claude.calendar-bridge $(INSTALL_DIR)/calendar-bridge
	@echo "  ✓ calendar-bridge installed"

install-notes:
	@echo "→ Building notes-bridge..."
	swiftc notes-bridge.swift -o $(INSTALL_DIR)/notes-bridge
	codesign --force --sign "$(CODESIGN_IDENTITY)" --identifier com.claude.notes-bridge $(INSTALL_DIR)/notes-bridge
	@echo "  ✓ notes-bridge installed"

install-mail:
	@echo "→ Building mail-bridge..."
	swiftc mail-bridge.swift -o $(INSTALL_DIR)/mail-bridge
	codesign --force --sign "$(CODESIGN_IDENTITY)" --identifier com.claude.mail-bridge $(INSTALL_DIR)/mail-bridge
	@echo "  ✓ mail-bridge installed"

test:
	@echo "Running integration tests (may trigger permission dialogs on first run)..."
	@bash test.sh

clean:
	rm -f $(INSTALL_DIR)/reminders-bridge
	rm -f $(INSTALL_DIR)/calendar-bridge
	rm -f $(INSTALL_DIR)/contacts-bridge
	rm -f $(INSTALL_DIR)/notes-bridge
	rm -f $(INSTALL_DIR)/mail-bridge
	rm -f $(INSTALL_DIR)/tmux-bridge
	@echo "Removed all bridges from $(INSTALL_DIR)"
```

## File: `README.md`
```markdown
# Claude Apple Bridges

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Platform: macOS 13+](https://img.shields.io/badge/Platform-macOS%2013%2B-lightgrey.svg)
![Swift](https://img.shields.io/badge/Swift-5.9%2B-orange.svg)

Swift CLI tools that give [Claude Code](https://claude.ai/claude-code) native access to Apple apps — Reminders, Calendar, Contacts, Notes, Mail, and tmux. Includes a [Claude Code skill](#skills) (`/apple-bridges`) with complete command reference for all bridges.

## Usage Examples with Claude Code

Once set up, you can ask Claude naturally in any Claude Code session. Here are real-world examples:

---

### Task & Project Management

> *"What's on my todo list for today?"*

Claude checks your Reminders and summarizes open items with due dates and priorities.

> *"I just finished the login bug fix — mark the GitHub issue and the reminder as done."*

Claude closes the GitHub issue and calls `reminders-bridge complete` in one step.

> *"Add a reminder to my 'Work' list to review the PR tomorrow morning."*

Claude creates the reminder with a due date set to tomorrow at 9:00.

---

### Calendar-Aware Scheduling

> *"I want to work on the Android release tomorrow — find a free slot and set a reminder."*

Claude checks `calendar-bridge tomorrow`, finds a free window, and sets the reminder due date accordingly — no double-booking.

> *"What do I have going on this week? Block some time for code review."*

Claude reads your calendar for each day, spots gaps, and adds events or reminders where they fit.

> *"Schedule our next planning session for next Monday at 10am in my Work calendar."*

Claude calls `calendar-bridge add` directly without you having to open Calendar.

---

### Contacts Lookup

> *"What's Rob's phone number?"*

Claude searches your Contacts and returns the number directly — no need to open the Contacts app.

> *"Add Alex to my contacts: +49 123 456789, alex@example.com"*

Claude calls `contacts-bridge add` and confirms once saved.

> *"Show me all details for my contact Thomas."*

Claude returns name, phone, email, address and birthday in one view.

---

### Development Workflow Integration

> *"Start working on issue #42 — create a reminder to track it and add the 'in progress' label."*

Claude adds a GitHub label, creates a Reminders entry with the issue number in the notes, and sets a due date.

> *"We finished the feature — close the issue, complete the reminder, and write the release note."*

Claude handles all three in one go.

> *"What are my open todos related to this project?"*

Claude reads your Reminders list and cross-references with open GitHub issues for a full picture.

---

### End-of-Day / Planning

> *"Summarize what we did today and create reminders for anything we didn't finish."*

Claude reviews the session, identifies incomplete work, and adds follow-up reminders with appropriate due dates.

> *"Set reminders for all open todos so they show up in my Calendar tomorrow after my meetings."*

Claude reads tomorrow's calendar first to avoid conflicts, then sets due times in the free slots.

---

## Bridges

### reminders-bridge
Access and manage Apple Reminders from Claude Code.

```
reminders-bridge lists                                   List all reminder lists
reminders-bridge create-list <name>                      Create a new list
reminders-bridge items <list>                            Show all reminders in a list
reminders-bridge incomplete <list>                       Show only incomplete reminders
reminders-bridge today                                   Show reminders due today (all lists)
reminders-bridge overdue                                 Show all overdue reminders (all lists)
reminders-bridge search <query>                          Search by title/notes across all lists
reminders-bridge add <list> <title> [notes]              Add a new reminder
reminders-bridge set-due <list> <title> <datetime>       Set due date (YYYY-MM-DD HH:mm)
reminders-bridge set-notes <list> <title> <notes>        Set or update notes
reminders-bridge complete <list> <title>                 Mark a reminder as complete
reminders-bridge delete <list> <title> [--force]         Delete a reminder (dry-run without --force)
```

### calendar-bridge
Read and write Apple Calendar events from Claude Code.

```
calendar-bridge calendars                                     List all calendars
calendar-bridge today                                         Show today's events
calendar-bridge tomorrow                                      Show tomorrow's events
calendar-bridge week                                          Show this week's events
calendar-bridge events <YYYY-MM-DD>                           Show events for a date
calendar-bridge free-slots <YYYY-MM-DD>                       Show free time slots (08:00–20:00)
calendar-bridge search <query>                                Search events by title (next 365 days)
calendar-bridge add <cal> <title> <start> <end>               Add event (YYYY-MM-DD HH:mm)
calendar-bridge add-all-day <cal> <title> <YYYY-MM-DD>        Add all-day event
calendar-bridge delete <cal> <title> <YYYY-MM-DD> [--force]   Delete event (dry-run without --force)
```

### contacts-bridge
Search and manage Apple Contacts from Claude Code.

```
contacts-bridge search <query>                                Search by name, email or phone
contacts-bridge show <name>                                   Show full details for a contact
contacts-bridge add <firstName> <lastName> [phone] [email]    Add a new contact
contacts-bridge update <name> phone <value>                   Update phone number
contacts-bridge update <name> email <value>                   Update email address
contacts-bridge delete <name> [--force]                       Delete a contact (dry-run without --force)
contacts-bridge birthdays-today                               Contacts with birthday today
contacts-bridge birthdays-upcoming <days>                     Upcoming birthdays in next N days
```

### notes-bridge
Read and write Apple Notes from Claude Code.

```
notes-bridge accounts                                         List all accounts
notes-bridge folders [account]                                List folders (default: iCloud)
notes-bridge list [folder] [account]                          List notes with modification date
notes-bridge search <query>                                   Search by title and content across all accounts
notes-bridge read <title> [account]                           Read note content as plain text
notes-bridge add <folder> <title> <body> [account]            Create a new note
notes-bridge append <title> <text> [account]                  Append text to an existing note
notes-bridge delete <title> [--force] [account]               Delete a note (dry-run without --force)
```

**Formatting:** The `body` and `text` parameters support HTML — Notes.app renders it natively.

```bash
# Plain text note
notes-bridge add "Ideas" "Shopping" "Milk, Bread, Eggs"

# Rich note with HTML formatting
notes-bridge add "Work" "Meeting Notes" "<b>Attendees:</b> Tobias, Heiko<br><br><ul><li>Discussed Q1 roadmap</li><li>Next steps: review PR</li></ul>"

# Append a formatted section
notes-bridge append "Meeting Notes" "<br><b>Follow-up:</b><br><ul><li>Send report by Friday</li></ul>"
```

Supported HTML tags: `<b>`, `<i>`, `<u>`, `<br>`, `<ul>`, `<ol>`, `<li>`, `<h1>`–`<h3>`, `<a href="...">`, `<p>`

### mail-bridge
Read and send Apple Mail messages from Claude Code.

```
mail-bridge accounts                                                           List all email accounts
mail-bridge mailboxes [account]                                                List mailboxes (default: first account)
mail-bridge list [mailbox|account] [account] [count]                           List recent messages (auto-detects account names)
mail-bridge unread [mailbox|account] [account]                                 List unread messages (auto-detects account names)
mail-bridge search <query> [max_results] [account]                             Search subject/sender (all accounts by default)
mail-bridge read <index> [mailbox] [account]                                   Read message (unread status preserved)
mail-bridge read <index> [mailbox] [account] --mark-read                       Read message and mark as read
mail-bridge send <to> <subject> <body> [/attachment] [--from <email>]          Opens compose window — user reviews and sends manually
mail-bridge send <to> <subject> <body> [/attachment] [--from <email>] --force  Sends directly without UI
mail-bridge delete <index> [mailbox] [account] [--force]                       Move to Trash (dry-run without --force)
```

**Send examples:**

```bash
# Ask Claude to draft a reply → compose window opens in Mail.app for review:
mail-bridge send heiko@web.de "Betreff" "Hallo Heiko, ..."

# Claude sends automatically without user interaction (explicit intent required):
mail-bridge send heiko@web.de "Betreff" "Hallo Heiko, ..." --force

# With attachment and explicit sender:
mail-bridge send heiko@web.de "Report" "See attached." /tmp/report.pdf --from work@company.com --force
```

### tmux-bridge
Read and write tmux session contents from Claude Code — great for end-of-day summaries and interactive terminal control.

```
tmux-bridge sessions                              List all running sessions
tmux-bridge windows [session]                     List windows in a session
tmux-bridge panes [session]                       List all panes with path and command
tmux-bridge read <target> [lines]                 Read pane content (e.g. main:1.1, default: 1000 lines)
tmux-bridge write <target> <text> [--no-enter]    Send keystrokes to a pane
tmux-bridge snapshot [session] [lines]            Capture all panes at once (default: 5000 lines)
```

**Write examples:**

```bash
# Send a command (text + Enter)
tmux-bridge write main:0.0 "ls -la"

# Send text without pressing Enter
tmux-bridge write main:0.0 "partial input" --no-enter
```

Typical workflow: run your work in named tmux sessions, then ask Claude at the end of the day:
> *"Read tmux-bridge snapshot and summarize what I worked on today."*

---

## Setup

### 1. Compile

```bash
# Install all bridges at once (recommended)
git clone https://github.com/more-io/claude-apple-bridges.git
cd claude-apple-bridges
make install
```

**Optional: Persistent TCC permissions with a Developer certificate**

By default, bridges are ad-hoc signed. macOS TCC may re-prompt for permissions in new terminal sessions (especially remote/SSH). If you have an Apple Developer certificate, pass `CODESIGN_IDENTITY` for persistent grants:

```bash
make install CODESIGN_IDENTITY="Apple Development: Your Name (TEAMID)"
```

Or install individually:

```bash
make install-reminders
make install-calendar
make install-contacts
make install-notes
make install-mail
```

<details>
<summary>Manual compile (without make)</summary>

```bash
# reminders-bridge
cat > /tmp/reminders-info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>NSRemindersUsageDescription</key>
    <string>Claude Code needs access to Reminders to manage tasks.</string>
</dict>
</plist>
EOF
swiftc reminders-bridge.swift -o ~/.claude/reminders-bridge \
  -framework EventKit \
  -Xlinker -sectcreate -Xlinker __TEXT -Xlinker __info_plist -Xlinker /tmp/reminders-info.plist
codesign --force --sign - --identifier com.claude.reminders-bridge ~/.claude/reminders-bridge

# contacts-bridge
cat > /tmp/contacts-info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>NSContactsUsageDescription</key>
    <string>Claude Code needs access to Contacts to look up and manage contacts.</string>
</dict>
</plist>
EOF
swiftc contacts-bridge.swift -o ~/.claude/contacts-bridge \
  -framework Contacts \
  -Xlinker -sectcreate -Xlinker __TEXT -Xlinker __info_plist -Xlinker /tmp/contacts-info.plist
codesign --force --sign - --identifier com.claude.contacts-bridge ~/.claude/contacts-bridge

# calendar-bridge
cat > /tmp/calendar-info.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>NSCalendarsFullAccessUsageDescription</key>
    <string>Claude Code needs access to Calendar to schedule and view events.</string>
</dict>
</plist>
EOF
swiftc calendar-bridge.swift -o ~/.claude/calendar-bridge \
  -framework EventKit \
  -Xlinker -sectcreate -Xlinker __TEXT -Xlinker __info_plist -Xlinker /tmp/calendar-info.plist
codesign --force --sign - --identifier com.claude.calendar-bridge ~/.claude/calendar-bridge

# notes-bridge
swiftc notes-bridge.swift -o ~/.claude/notes-bridge
codesign --force --sign - --identifier com.claude.notes-bridge ~/.claude/notes-bridge

# mail-bridge
swiftc mail-bridge.swift -o ~/.claude/mail-bridge
codesign --force --sign - --identifier com.claude.mail-bridge ~/.claude/mail-bridge
```

</details>

### 2. Grant permissions

Run each binary once from Terminal to trigger the macOS permission dialog:

```bash
~/.claude/reminders-bridge lists
~/.claude/calendar-bridge today
~/.claude/contacts-bridge search "test"
~/.claude/notes-bridge accounts
~/.claude/mail-bridge accounts
```

Then approve in **System Settings → Privacy & Security → Reminders / Calendars / Contacts / Automation**. Notes and Mail access is granted automatically via AppleScript on first use.

### 3. Add to Claude Code allowed tools

Add the bridges to your **global** `~/.claude/settings.json` so they work across all projects without confirmation prompts:

```json
{
  "permissions": {
    "allow": [
      "Bash(~/.claude/reminders-bridge*)",
      "Bash(~/.claude/calendar-bridge*)",
      "Bash(~/.claude/contacts-bridge*)",
      "Bash(~/.claude/notes-bridge*)",
      "Bash(~/.claude/mail-bridge*)",
      "Bash(~/.claude/tmux-bridge*)"
    ]
  }
}
```

---

## Requirements

- macOS 13+
- Swift (comes with Xcode or `xcode-select --install`)
- Claude Code

---

## Testing

After installing, run the integration test suite to verify everything works:

```bash
make test
```

35 tests cover all commands across all three bridges — exit codes, output validation, and argument handling. No data is modified during tests.

---

## Skills

Skills are structured prompt templates that Claude Code can load automatically when a bridge topic comes up. Instead of relying solely on CLAUDE.md for bridge documentation, the skill provides complete command syntax, parameters, and usage examples on demand.

### What Skills Do

When you type `/apple-bridges` in Claude Code (or when Claude detects you're asking about Reminders, Calendar, Contacts, Notes, Mail, or tmux), the skill loads:

1. **SKILL.md** — Overview of all bridges with a quick reference table
2. **Detail files** — Full documentation per bridge, loaded only when needed

This keeps context usage minimal while giving Claude complete knowledge of every command.

### Install Skills

Skills are included with `make install`:

```bash
make install          # Installs bridges AND skills
make install-skills   # Install skills only
```

This copies the skill files to `~/.claude/skills/apple-bridges/`.

### Manual Install

```bash
cp -r skills/apple-bridges ~/.claude/skills/
```

### Verify

Start a new Claude Code session and type `/apple-bridges` — it should be available as a slash command.

---

## Contributing

Pull requests are welcome! When adding a new bridge:

1. Create `<name>-bridge.swift` in the repo root
2. Add compile instructions to `README.md` and `CLAUDE.md`
3. Add the permission grant step to `README.md`
4. Add usage examples to `README.md`

See `CLAUDE.md` for developer notes and the branching workflow.

---

## License

MIT — see [LICENSE](LICENSE) for details.
```

## File: `calendar-bridge.swift`
```
#!/usr/bin/env swift

// calendar-bridge.swift
// Copyright © 2026 Tobias Stöger (tstoegi). Licensed under the MIT License.
// A small CLI bridge for Claude Code to access Apple Calendar via EventKit.
// Usage:
//   calendar-bridge calendars                                      - List all calendars
//   calendar-bridge today                                          - Show today's events
//   calendar-bridge tomorrow                                       - Show tomorrow's events
//   calendar-bridge week                                           - Show this week's events
//   calendar-bridge events <YYYY-MM-DD>                            - Show events for a date
//   calendar-bridge free-slots <YYYY-MM-DD>                        - Show free time slots for a date
//   calendar-bridge search <query>                                 - Search events by title (next 365 days)
//   calendar-bridge add <cal> <title> <start> <end>                - Add event (YYYY-MM-DD HH:mm)
//   calendar-bridge add-all-day <cal> <title> <YYYY-MM-DD>         - Add all-day event
//   calendar-bridge delete <cal> <title> <YYYY-MM-DD> [--force]    - Delete an event

import EventKit
import Foundation

let store = EKEventStore()

func requestAccess() async -> Bool {
    do {
        return try await store.requestFullAccessToEvents()
    } catch {
        fputs("Error requesting access: \(error.localizedDescription)\n", stderr)
        return false
    }
}

// MARK: - Date Helpers

func parseDateTime(_ string: String) -> Date? {
    let formatter = DateFormatter()
    formatter.dateFormat = "yyyy-MM-dd HH:mm"
    formatter.locale = Locale(identifier: "en_US_POSIX")
    return formatter.date(from: string)
}

func parseDate(_ string: String) -> Date? {
    let formatter = DateFormatter()
    formatter.dateFormat = "yyyy-MM-dd"
    formatter.locale = Locale(identifier: "en_US_POSIX")
    return formatter.date(from: string)
}

func formatTime(_ date: Date) -> String {
    let formatter = DateFormatter()
    formatter.dateFormat = "HH:mm"
    return formatter.string(from: date)
}

func formatDateTime(_ date: Date) -> String {
    let formatter = DateFormatter()
    formatter.dateFormat = "EEE dd.MM. HH:mm"
    formatter.locale = Locale.current
    return formatter.string(from: date)
}

func formatDayHeader(_ date: Date) -> String {
    let formatter = DateFormatter()
    formatter.dateFormat = "EEEE, dd. MMMM yyyy"
    formatter.locale = Locale.current
    return formatter.string(from: date)
}

func startOfDay(_ date: Date) -> Date {
    Calendar.current.startOfDay(for: date)
}

func endOfDay(_ date: Date) -> Date {
    var components = DateComponents()
    components.day = 1
    components.second = -1
    return Calendar.current.date(byAdding: components, to: startOfDay(date))!
}

// MARK: - String Normalization

func normalizeQuotes(in string: String) -> String {
    string
        .replacingOccurrences(of: "\u{2018}", with: "'")
        .replacingOccurrences(of: "\u{2019}", with: "'")
        .replacingOccurrences(of: "\u{201C}", with: "\"")
        .replacingOccurrences(of: "\u{201D}", with: "\"")
}

func findCalendar(named name: String) -> EKCalendar? {
    let normalized = normalizeQuotes(in: name)
    return store.calendars(for: .event).first(where: {
        normalizeQuotes(in: $0.title) == normalized
    })
}

// MARK: - Commands

func listCalendars() {
    let calendars = store.calendars(for: .event)
    for cal in calendars.sorted(by: { $0.title < $1.title }) {
        let type = cal.isImmutable ? " (read-only)" : ""
        print("\(cal.title)\(type)")
    }
}

func showEvents(for date: Date) {
    let predicate = store.predicateForEvents(withStart: startOfDay(date), end: endOfDay(date), calendars: nil)
    let events = store.events(matching: predicate).sorted { $0.startDate < $1.startDate }
    print("Events for \(formatDayHeader(date)):")
    if events.isEmpty {
        print("  (no events)")
        return
    }
    for event in events {
        let timeStr = event.isAllDay ? "All day" : "\(formatTime(event.startDate)) – \(formatTime(event.endDate))"
        let loc = event.location.map { " @ \($0)" } ?? ""
        print("  [\(timeStr)] \(event.title ?? "(no title)")\(loc)  (\(event.calendar.title))")
    }
}

func showWeek() {
    let cal = Calendar.current
    let today = Date()
    // Start from Monday of current week
    var components = cal.dateComponents([.yearForWeekOfYear, .weekOfYear], from: today)
    components.weekday = 2 // Monday
    let monday = cal.date(from: components) ?? today

    for offset in 0..<7 {
        let day = cal.date(byAdding: .day, value: offset, to: monday)!
        showEvents(for: day)
        print()
    }
}

func showFreeSlots(for date: Date) {
    let predicate = store.predicateForEvents(withStart: startOfDay(date), end: endOfDay(date), calendars: nil)
    let events = store.events(matching: predicate)
        .filter { !$0.isAllDay }
        .sorted { $0.startDate < $1.startDate }

    print("Free slots on \(formatDayHeader(date)):")

    // Working hours 08:00–20:00, minimum slot 30 min
    let workStart = Calendar.current.date(bySettingHour: 8, minute: 0, second: 0, of: date)!
    let workEnd   = Calendar.current.date(bySettingHour: 20, minute: 0, second: 0, of: date)!
    let minSlot: TimeInterval = 30 * 60

    var cursor = workStart
    var hasSlots = false

    for event in events {
        let eventStart = max(event.startDate, workStart)
        let eventEnd   = min(event.endDate, workEnd)
        if eventStart > cursor && eventStart.timeIntervalSince(cursor) >= minSlot {
            print("  \(formatTime(cursor)) – \(formatTime(eventStart))  (\(Int(eventStart.timeIntervalSince(cursor) / 60)) min)")
            hasSlots = true
        }
        if eventEnd > cursor { cursor = eventEnd }
    }

    if workEnd > cursor && workEnd.timeIntervalSince(cursor) >= minSlot {
        print("  \(formatTime(cursor)) – \(formatTime(workEnd))  (\(Int(workEnd.timeIntervalSince(cursor) / 60)) min)")
        hasSlots = true
    }

    if !hasSlots {
        print("  (no free slots in working hours 08:00–20:00)")
    }
}

func searchEvents(query: String) {
    let lower = query.lowercased()
    let start = Date()
    let end = Calendar.current.date(byAdding: .day, value: 365, to: start)!
    let predicate = store.predicateForEvents(withStart: start, end: end, calendars: nil)
    let matches = store.events(matching: predicate)
        .filter { ($0.title ?? "").lowercased().contains(lower) }
        .sorted { $0.startDate < $1.startDate }

    if matches.isEmpty {
        print("No events found for '\(query)' in the next 365 days.")
        return
    }
    print("\(matches.count) event(s) matching '\(query)':")
    for event in matches {
        let timeStr = event.isAllDay ? "All day" : "\(formatDateTime(event.startDate)) – \(formatTime(event.endDate))"
        print("  [\(timeStr)] \(event.title ?? "(no title)")  (\(event.calendar.title))")
    }
}

func addEvent(calendarName: String, title: String, start: Date, end: Date) {
    guard let calendar = findCalendar(named: calendarName) else {
        fputs("Calendar '\(calendarName)' not found.\n\nAvailable calendars:\n", stderr)
        store.calendars(for: .event).sorted(by: { $0.title < $1.title }).forEach {
            fputs("  \(normalizeQuotes(in: $0.title))\n", stderr)
        }
        exit(1)
    }
    guard !calendar.isImmutable else {
        fputs("Calendar '\(calendarName)' is read-only.\n", stderr); exit(1)
    }
    let event = EKEvent(eventStore: store)
    event.title = title
    event.startDate = start
    event.endDate = end
    event.calendar = calendar
    do {
        try store.save(event, span: .thisEvent)
        print("Added: \(title) (\(formatDateTime(start)) – \(formatTime(end)))")
    } catch {
        fputs("Error saving event: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

func addAllDayEvent(calendarName: String, title: String, date: Date) {
    guard let calendar = findCalendar(named: calendarName) else {
        fputs("Calendar '\(calendarName)' not found.\n\nAvailable calendars:\n", stderr)
        store.calendars(for: .event).sorted(by: { $0.title < $1.title }).forEach {
            fputs("  \(normalizeQuotes(in: $0.title))\n", stderr)
        }
        exit(1)
    }
    guard !calendar.isImmutable else {
        fputs("Calendar '\(calendarName)' is read-only.\n", stderr); exit(1)
    }
    let event = EKEvent(eventStore: store)
    event.title = title
    event.isAllDay = true
    event.startDate = startOfDay(date)
    event.endDate = startOfDay(date)
    event.calendar = calendar
    do {
        try store.save(event, span: .thisEvent)
        let fmt = DateFormatter()
        fmt.dateFormat = "dd.MM.yyyy"
        print("Added all-day: \(title) (\(fmt.string(from: date)))")
    } catch {
        fputs("Error saving event: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

func deleteEvent(calendarName: String, title: String, date: Date, force: Bool) {
    guard let calendar = findCalendar(named: calendarName) else {
        fputs("Calendar '\(calendarName)' not found.\n\nAvailable calendars:\n", stderr)
        store.calendars(for: .event).sorted(by: { $0.title < $1.title }).forEach {
            fputs("  \(normalizeQuotes(in: $0.title))\n", stderr)
        }
        exit(1)
    }
    let predicate = store.predicateForEvents(withStart: startOfDay(date), end: endOfDay(date), calendars: [calendar])
    let matches = store.events(matching: predicate).filter { ($0.title ?? "") == title }

    guard let event = matches.first else {
        fputs("Event '\(title)' not found on \(formatDayHeader(date)).\n", stderr); exit(1)
    }
    guard force else {
        print("Would delete: \(title) on \(formatDayHeader(date)) (\(formatTime(event.startDate)) – \(formatTime(event.endDate)))")
        print("Re-run with --force to actually delete.")
        return
    }
    do {
        try store.remove(event, span: .thisEvent)
        print("Deleted: \(title) on \(formatDayHeader(date))")
    } catch {
        fputs("Error: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

// MARK: - Main

let args = CommandLine.arguments

guard args.count >= 2 else {
    print("Usage:")
    print("  calendar-bridge calendars")
    print("  calendar-bridge today")
    print("  calendar-bridge tomorrow")
    print("  calendar-bridge week")
    print("  calendar-bridge events <YYYY-MM-DD>")
    print("  calendar-bridge free-slots <YYYY-MM-DD>")
    print("  calendar-bridge search <query>")
    print("  calendar-bridge add <calendar> <title> <\"YYYY-MM-DD HH:mm\"> <\"YYYY-MM-DD HH:mm\">")
    print("  calendar-bridge add-all-day <calendar> <title> <YYYY-MM-DD>")
    print("  calendar-bridge delete <calendar> <title> <YYYY-MM-DD> [--force]")
    exit(0)
}

let accessSemaphore = DispatchSemaphore(value: 0)
var hasAccess = false

Task {
    hasAccess = await requestAccess()
    accessSemaphore.signal()
}
accessSemaphore.wait()

guard hasAccess else {
    fputs("No access to Calendar. Please grant permission in System Settings > Privacy & Security > Calendars.\n", stderr)
    exit(1)
}

let command = args[1]

switch command {
case "calendars":
    listCalendars()

case "today":
    showEvents(for: Date())

case "tomorrow":
    showEvents(for: Calendar.current.date(byAdding: .day, value: 1, to: Date())!)

case "week":
    showWeek()

case "events":
    guard args.count >= 3, let date = parseDate(args[2]) else {
        fputs("Usage: calendar-bridge events <YYYY-MM-DD>\n", stderr); exit(1)
    }
    showEvents(for: date)

case "free-slots":
    guard args.count >= 3, let date = parseDate(args[2]) else {
        fputs("Usage: calendar-bridge free-slots <YYYY-MM-DD>\n", stderr); exit(1)
    }
    showFreeSlots(for: date)

case "search":
    guard args.count >= 3 else {
        fputs("Usage: calendar-bridge search <query>\n", stderr); exit(1)
    }
    searchEvents(query: args[2])

case "add":
    guard args.count >= 6,
          let start = parseDateTime(args[4]),
          let end = parseDateTime(args[5]) else {
        fputs("Usage: calendar-bridge add <calendar> <title> <\"YYYY-MM-DD HH:mm\"> <\"YYYY-MM-DD HH:mm\">\n", stderr); exit(1)
    }
    addEvent(calendarName: args[2], title: args[3], start: start, end: end)

case "add-all-day":
    guard args.count >= 5, let date = parseDate(args[4]) else {
        fputs("Usage: calendar-bridge add-all-day <calendar> <title> <YYYY-MM-DD>\n", stderr); exit(1)
    }
    addAllDayEvent(calendarName: args[2], title: args[3], date: date)

case "delete":
    guard args.count >= 5, let date = parseDate(args[4]) else {
        fputs("Usage: calendar-bridge delete <calendar> <title> <YYYY-MM-DD> [--force]\n", stderr); exit(1)
    }
    let force = args.contains("--force")
    deleteEvent(calendarName: args[2], title: args[3], date: date, force: force)

default:
    fputs("Unknown command: \(command)\n", stderr)
    exit(1)
}
```

## File: `contacts-bridge.swift`
```
#!/usr/bin/env swift

// contacts-bridge.swift
// Copyright © 2026 Tobias Stöger (tstoegi). Licensed under the MIT License.
// A small CLI bridge for Claude Code to access Apple Contacts via Contacts framework.
// Usage:
//   contacts-bridge search <query>                                  - Search by name, email or phone
//   contacts-bridge show <name>                                     - Show full details for a contact
//   contacts-bridge add <firstName> <lastName> [phone] [email]      - Add a new contact
//   contacts-bridge update <name> phone <value>                     - Update phone number
//   contacts-bridge update <name> email <value>                     - Update email address
//   contacts-bridge delete <name> [--force]                         - Delete a contact
//   contacts-bridge birthdays-today                                 - Contacts with birthday today
//   contacts-bridge birthdays-upcoming <days>                       - Upcoming birthdays in N days

import Contacts
import Foundation

let store = CNContactStore()

func requestAccess() async -> Bool {
    do {
        return try await store.requestAccess(for: .contacts)
    } catch {
        fputs("Error requesting access: \(error.localizedDescription)\n", stderr)
        return false
    }
}

// MARK: - Helpers

let fetchKeys: [CNKeyDescriptor] = [
    CNContactGivenNameKey as CNKeyDescriptor,
    CNContactFamilyNameKey as CNKeyDescriptor,
    CNContactOrganizationNameKey as CNKeyDescriptor,
    CNContactPhoneNumbersKey as CNKeyDescriptor,
    CNContactEmailAddressesKey as CNKeyDescriptor,
    CNContactBirthdayKey as CNKeyDescriptor,
    CNContactPostalAddressesKey as CNKeyDescriptor,
]

func fullName(_ contact: CNContact) -> String {
    "\(contact.givenName) \(contact.familyName)".trimmingCharacters(in: .whitespaces)
}

func formatContact(_ contact: CNContact, detailed: Bool = false) {
    let org = contact.organizationName.isEmpty ? "" : " (\(contact.organizationName))"
    print("\(fullName(contact))\(org)")

    for phone in contact.phoneNumbers {
        let label = phone.label.map { CNLabeledValue<NSString>.localizedString(forLabel: $0) } ?? ""
        print("  📞 \(phone.value.stringValue)\(label.isEmpty ? "" : "  [\(label)]")")
    }

    for email in contact.emailAddresses {
        let label = email.label.map { CNLabeledValue<NSString>.localizedString(forLabel: $0) } ?? ""
        print("  ✉️  \(email.value)\(label.isEmpty ? "" : "  [\(label)]")")
    }

    if detailed {
        if contact.isKeyAvailable(CNContactNoteKey), !contact.note.isEmpty {
            print("  📝 \(contact.note)")
        }
        if let bday = contact.birthday, let day = bday.day, let month = bday.month {
            let year = bday.year.map { " \($0)" } ?? ""
            print("  🎂 \(day).\(month).\(year)")
        }
        for address in contact.postalAddresses {
            let a = address.value
            let line = [a.street, a.postalCode, a.city, a.country]
                .filter { !$0.isEmpty }.joined(separator: ", ")
            print("  🏠 \(line)")
        }
    }
}

func findContacts(matching name: String) throws -> [CNContact] {
    let predicate = CNContact.predicateForContacts(matchingName: name)
    return try store.unifiedContacts(matching: predicate, keysToFetch: fetchKeys)
}

// MARK: - Commands

func searchContacts(query: String) {
    do {
        let contacts = try findContacts(matching: query)
        if contacts.isEmpty { print("No contacts found for '\(query)'"); return }
        print("\(contacts.count) result(s) for '\(query)':")
        print(String(repeating: "-", count: 40))
        contacts.forEach { formatContact($0); print() }
    } catch {
        fputs("Error: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

func showContact(name: String) {
    do {
        let contacts = try findContacts(matching: name)
        if contacts.isEmpty { print("No contact found for '\(name)'"); return }
        contacts.forEach { formatContact($0, detailed: true); print() }
    } catch {
        fputs("Error: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

func addContact(firstName: String, lastName: String, phone: String?, email: String?) {
    let contact = CNMutableContact()
    contact.givenName = firstName
    contact.familyName = lastName
    if let phone {
        contact.phoneNumbers = [CNLabeledValue(label: CNLabelPhoneNumberMobile, value: CNPhoneNumber(stringValue: phone))]
    }
    if let email {
        contact.emailAddresses = [CNLabeledValue(label: CNLabelWork, value: email as NSString)]
    }
    let saveRequest = CNSaveRequest()
    saveRequest.add(contact, toContainerWithIdentifier: nil)
    do {
        try store.execute(saveRequest)
        print("Added contact: \(firstName) \(lastName)".trimmingCharacters(in: .whitespaces))
    } catch {
        fputs("Error saving contact: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

func updateContact(name: String, field: String, value: String) {
    do {
        let contacts = try findContacts(matching: name)
        guard let contact = contacts.first else {
            fputs("Contact '\(name)' not found.\n", stderr); exit(1)
        }
        guard let mutable = contact.mutableCopy() as? CNMutableContact else { exit(1) }

        switch field.lowercased() {
        case "phone":
            mutable.phoneNumbers = [CNLabeledValue(label: CNLabelPhoneNumberMobile, value: CNPhoneNumber(stringValue: value))]
        case "email":
            mutable.emailAddresses = [CNLabeledValue(label: CNLabelWork, value: value as NSString)]
        default:
            fputs("Unknown field '\(field)'. Use 'phone' or 'email'.\n", stderr); exit(1)
        }

        let saveRequest = CNSaveRequest()
        saveRequest.update(mutable)
        try store.execute(saveRequest)
        print("Updated \(field) for \(fullName(contact)): \(value)")
    } catch {
        fputs("Error: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

func deleteContact(name: String, force: Bool) {
    do {
        let contacts = try findContacts(matching: name)
        guard let contact = contacts.first else {
            fputs("Contact '\(name)' not found.\n", stderr); exit(1)
        }
        guard force else {
            print("Would delete contact: \(fullName(contact))")
            if !contact.phoneNumbers.isEmpty {
                print("  📞 \(contact.phoneNumbers.map { $0.value.stringValue }.joined(separator: ", "))")
            }
            if !contact.emailAddresses.isEmpty {
                print("  ✉️  \(contact.emailAddresses.map { $0.value as String }.joined(separator: ", "))")
            }
            print("Re-run with --force to actually delete.")
            return
        }
        guard let mutable = contact.mutableCopy() as? CNMutableContact else { exit(1) }
        let saveRequest = CNSaveRequest()
        saveRequest.delete(mutable)
        try store.execute(saveRequest)
        print("Deleted contact: \(fullName(contact))")
    } catch {
        fputs("Error: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

func birthdaysToday() {
    let cal = Calendar.current
    let today = cal.dateComponents([.month, .day], from: Date())

    do {
        let allContacts = try store.unifiedContacts(
            matching: CNContact.predicateForContactsInContainer(withIdentifier: store.defaultContainerIdentifier()),
            keysToFetch: fetchKeys
        )
        let matches = allContacts.filter { contact in
            guard let bday = contact.birthday,
                  let month = bday.month, let day = bday.day else { return false }
            return month == today.month && day == today.day
        }
        if matches.isEmpty {
            print("No birthdays today.")
        } else {
            print("\(matches.count) birthday(s) today:")
            matches.forEach { formatContact($0); print() }
        }
    } catch {
        fputs("Error: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

func birthdaysUpcoming(days: Int) {
    let cal = Calendar.current
    let today = Date()

    do {
        let allContacts = try store.unifiedContacts(
            matching: CNContact.predicateForContactsInContainer(withIdentifier: store.defaultContainerIdentifier()),
            keysToFetch: fetchKeys
        )

        var upcoming: [(contact: CNContact, daysUntil: Int, date: DateComponents)] = []

        for contact in allContacts {
            guard let bday = contact.birthday,
                  let month = bday.month, let day = bday.day else { continue }

            let currentYear = cal.component(.year, from: today)
            for yearOffset in 0...1 {
                var nextBday = DateComponents()
                nextBday.year = currentYear + yearOffset
                nextBday.month = month
                nextBday.day = day
                if let bdayDate = cal.date(from: nextBday) {
                    let diff = cal.dateComponents([.day], from: cal.startOfDay(for: today), to: cal.startOfDay(for: bdayDate)).day ?? 0
                    if diff >= 0 && diff <= days {
                        upcoming.append((contact, diff, bday))
                        break
                    }
                }
            }
        }

        upcoming.sort { $0.daysUntil < $1.daysUntil }

        if upcoming.isEmpty {
            print("No birthdays in the next \(days) days.")
        } else {
            print("\(upcoming.count) birthday(s) in the next \(days) days:")
            for entry in upcoming {
                let when = entry.daysUntil == 0 ? "Today" : entry.daysUntil == 1 ? "Tomorrow" : "In \(entry.daysUntil) days"
                let year = entry.date.year.map { " \($0)" } ?? ""
                print("  \(when) (\(entry.date.day!).\(entry.date.month!)\(year)): \(fullName(entry.contact))")
            }
        }
    } catch {
        fputs("Error: \(error.localizedDescription)\n", stderr); exit(1)
    }
}

// MARK: - Main

let args = CommandLine.arguments

guard args.count >= 2 else {
    print("Usage:")
    print("  contacts-bridge search <query>")
    print("  contacts-bridge show <name>")
    print("  contacts-bridge add <firstName> <lastName> [phone] [email]")
    print("  contacts-bridge update <name> phone <value>")
    print("  contacts-bridge update <name> email <value>")
    print("  contacts-bridge delete <name> [--force]")
    print("  contacts-bridge birthdays-today")
    print("  contacts-bridge birthdays-upcoming <days>")
    exit(0)
}

let accessSemaphore = DispatchSemaphore(value: 0)
var hasAccess = false

Task {
    hasAccess = await requestAccess()
    accessSemaphore.signal()
}
accessSemaphore.wait()

guard hasAccess else {
    fputs("No access to Contacts. Please grant permission in System Settings > Privacy & Security > Contacts.\n", stderr)
    exit(1)
}

let command = args[1]

switch command {
case "search":
    guard args.count >= 3 else { fputs("Usage: contacts-bridge search <query>\n", stderr); exit(1) }
    searchContacts(query: args[2])

case "show":
    guard args.count >= 3 else { fputs("Usage: contacts-bridge show <name>\n", stderr); exit(1) }
    showContact(name: args[2])

case "add":
    guard args.count >= 4 else { fputs("Usage: contacts-bridge add <firstName> <lastName> [phone] [email]\n", stderr); exit(1) }
    let phone = args.count >= 5 ? args[4] : nil
    let email = args.count >= 6 ? args[5] : nil
    addContact(firstName: args[2], lastName: args[3], phone: phone, email: email)

case "update":
    guard args.count >= 5 else { fputs("Usage: contacts-bridge update <name> phone|email <value>\n", stderr); exit(1) }
    updateContact(name: args[2], field: args[3], value: args[4])

case "delete":
    guard args.count >= 3 else { fputs("Usage: contacts-bridge delete <name> [--force]\n", stderr); exit(1) }
    let force = args.contains("--force")
    deleteContact(name: args[2], force: force)

case "birthdays-today":
    birthdaysToday()

case "birthdays-upcoming":
    guard args.count >= 3, let days = Int(args[2]) else {
        fputs("Usage: contacts-bridge birthdays-upcoming <days>\n", stderr); exit(1)
    }
    birthdaysUpcoming(days: days)

default:
    fputs("Unknown command: \(command)\n", stderr)
    exit(1)
}
```

## File: `mail-bridge.swift`
```
#!/usr/bin/env swift

// mail-bridge.swift
// A small CLI bridge for Claude Code to access Apple Mail via NSAppleScript.
// Copyright © 2026 Tobias Stöger (tstoegi). Licensed under the MIT License.
// Usage:
//   mail-bridge accounts                               - List all accounts
//   mail-bridge mailboxes [account]                    - List mailboxes (default: first account)
//   mail-bridge list [mailbox] [account] [count]       - List recent messages (default: INBOX, 20)
//   mail-bridge unread [mailbox] [account]             - List unread messages (default: INBOX)
//   mail-bridge search <query> [account]               - Search subject/sender in INBOX
//   mail-bridge read <index> [mailbox] [account]       - Read message by index
//   mail-bridge send <to> <subject> <body>             - Send a new email (plain text)
//   mail-bridge send <to> <subject> --html-file <path>  - Send HTML email from file
//   mail-bridge delete <index> [mailbox] [account] [--force]  - Move message to Trash

import Foundation

// MARK: - String Helpers

// Escape strings for safe interpolation inside AppleScript double-quoted strings.
func escapeForAppleScript(_ string: String) -> String {
    string
        .replacingOccurrences(of: "\\", with: "\\\\")
        .replacingOccurrences(of: "\"", with: "\\\"")
}

// Normalize typographic quotes to ASCII equivalents for reliable matching.
func normalizeQuotes(in string: String) -> String {
    string
        .replacingOccurrences(of: "\u{2018}", with: "'")
        .replacingOccurrences(of: "\u{2019}", with: "'")
        .replacingOccurrences(of: "\u{201C}", with: "\"")
        .replacingOccurrences(of: "\u{201D}", with: "\"")
}

// MARK: - AppleScript Runner

func runScript(_ source: String) -> NSAppleEventDescriptor? {
    var errorInfo: NSDictionary?
    guard let script = NSAppleScript(source: source) else { return nil }
    let result = script.executeAndReturnError(&errorInfo)
    if let error = errorInfo {
        let message = error[NSAppleScript.errorMessage] as? String ?? "Unknown error"
        fputs("AppleScript error: \(message)\n", stderr)
        return nil
    }
    return result
}

func descriptorToStrings(_ descriptor: NSAppleEventDescriptor?) -> [String] {
    guard let desc = descriptor else { return [] }
    if desc.numberOfItems > 0 {
        var items: [String] = []
        for i in 1...desc.numberOfItems {
            if let item = desc.atIndex(i)?.stringValue {
                items.append(item)
            }
        }
        return items
    }
    if let value = desc.stringValue, !value.isEmpty {
        return [value]
    }
    return []
}

// MARK: - Commands

func listAccounts() {
    let result = runScript("""
        tell application "Mail"
            set out to {}
            repeat with acc in accounts
                set end of out to name of acc
            end repeat
            return out
        end tell
    """)
    let accounts = descriptorToStrings(result)
    if accounts.isEmpty {
        print("No accounts found.")
    } else {
        accounts.forEach { print($0) }
    }
}

func listMailboxes(account: String) {
    let accountClause = account.isEmpty
        ? "item 1 of accounts"
        : "account \"\(escapeForAppleScript(account))\""
    let result = runScript("""
        tell application "Mail"
            set out to {}
            repeat with mb in mailboxes of \(accountClause)
                set end of out to name of mb
            end repeat
            return out
        end tell
    """)
    let mailboxes = descriptorToStrings(result)
    if mailboxes.isEmpty {
        fputs("No mailboxes found\(account.isEmpty ? "" : " for '\(account)'")\n", stderr)
        exit(1)
    }
    mailboxes.forEach { print($0) }
}

func listMessages(mailbox: String, account: String, count: Int) {
    let accountClause = account.isEmpty
        ? "item 1 of accounts"
        : "account \"\(escapeForAppleScript(account))\""
    let result = runScript("""
        tell application "Mail"
            set out to {}
            set acc to \(accountClause)
            set msgs to messages of mailbox "\(escapeForAppleScript(mailbox))" of acc
            set msgCount to count of msgs
            if msgCount is 0 then return out
            set endIdx to \(count)
            if endIdx > msgCount then set endIdx to msgCount
            repeat with i from 1 to endIdx
                set m to item i of msgs
                set isRead to read status of m
                set readMark to ""
                if isRead is false then set readMark to " [UNREAD]"
                set d to date received of m
                set mo to month of d as integer as string
                set da to day of d as string
                set entry to (i as text) & ". " & subject of m & readMark & " — " & sender of m & " (" & mo & "/" & da & ")"
                set end of out to entry
            end repeat
            return out
        end tell
    """)
    let messages = descriptorToStrings(result)
    if messages.isEmpty {
        print("No messages in '\(mailbox)'.")
    } else {
        messages.forEach { print($0) }
    }
}

func listUnread(mailbox: String, account: String) {
    let accountClause = account.isEmpty
        ? "item 1 of accounts"
        : "account \"\(escapeForAppleScript(account))\""
    let result = runScript("""
        tell application "Mail"
            set out to {}
            set acc to \(accountClause)
            set msgs to messages of mailbox "\(escapeForAppleScript(mailbox))" of acc
            set msgCount to count of msgs
            repeat with i from 1 to msgCount
                set m to item i of msgs
                if read status of m is false then
                    set d to date received of m
                    set mo to month of d as integer as string
                    set da to day of d as string
                    set entry to subject of m & " — " & sender of m & " (" & mo & "/" & da & ")"
                    set end of out to entry
                end if
            end repeat
            return out
        end tell
    """)
    let messages = descriptorToStrings(result)
    if messages.isEmpty {
        print("No unread messages in '\(mailbox)'.")
    } else {
        print("Unread in '\(mailbox)' (\(messages.count)):")
        messages.forEach { print("  " + $0) }
    }
}

func searchMessages(query: String, account: String, maxResults: Int) {
    let escapedQuery = escapeForAppleScript(query)
    let limit = maxResults > 0 ? maxResults : 50

    if account.isEmpty {
        // Search ALL accounts
        var allMatches: [String] = []
        for accName in accountNames {
            let escapedAcc = escapeForAppleScript(accName)
            let result = runScript("""
                tell application "Mail"
                    set out to {}
                    set acc to account "\(escapedAcc)"
                    set allMailboxes to {"INBOX"}
                    repeat with mbName in allMailboxes
                        try
                            set msgs to messages of mailbox (mbName as text) of acc
                            set msgCount to count of msgs
                            repeat with i from 1 to msgCount
                                set m to item i of msgs
                                set subjectMatch to subject of m contains "\(escapedQuery)"
                                set senderMatch to sender of m contains "\(escapedQuery)"
                                if subjectMatch or senderMatch then
                                    set d to date received of m
                                    set mo to month of d as integer as string
                                    set da to day of d as string
                                    set entry to "[" & name of acc & "] " & subject of m & " — " & sender of m & " (" & mo & "/" & da & ")"
                                    set end of out to entry
                                    if (count of out) >= \(limit) then return out
                                end if
                            end repeat
                        end try
                    end repeat
                    return out
                end tell
            """)
            allMatches.append(contentsOf: descriptorToStrings(result))
            if allMatches.count >= limit { break }
        }
        if allMatches.isEmpty {
            print("No messages matching '\(query)' across all accounts.")
        } else {
            print("Found \(allMatches.count) message(s):")
            allMatches.prefix(limit).forEach { print("  " + $0) }
        }
    } else {
        let result = runScript("""
            tell application "Mail"
                set out to {}
                set acc to account "\(escapeForAppleScript(account))"
                set msgs to messages of mailbox "INBOX" of acc
                set msgCount to count of msgs
                repeat with i from 1 to msgCount
                    set m to item i of msgs
                    set subjectMatch to subject of m contains "\(escapedQuery)"
                    set senderMatch to sender of m contains "\(escapedQuery)"
                    if subjectMatch or senderMatch then
                        set d to date received of m
                        set mo to month of d as integer as string
                        set da to day of d as string
                        set entry to subject of m & " — " & sender of m & " (" & mo & "/" & da & ")"
                        set end of out to entry
                        if (count of out) >= \(limit) then return out
                    end if
                end repeat
                return out
            end tell
        """)
        let matches = descriptorToStrings(result)
        if matches.isEmpty {
            print("No messages matching '\(query)'.")
        } else {
            print("Found \(matches.count) message(s):")
            matches.prefix(limit).forEach { print("  " + $0) }
        }
    }
}

func readMessage(index: Int, mailbox: String, account: String, markRead: Bool) {
    let accountClause = account.isEmpty
        ? "item 1 of accounts"
        : "account \"\(escapeForAppleScript(account))\""
    let markReadScript = markRead ? "set read status of m to true" : ""
    let result = runScript("""
        tell application "Mail"
            set acc to \(accountClause)
            set msgs to messages of mailbox "\(escapeForAppleScript(mailbox))" of acc
            set msgCount to count of msgs
            if \(index) < 1 or \(index) > msgCount then
                return "INDEX_OUT_OF_RANGE"
            end if
            set m to item \(index) of msgs
            set d to date received of m
            set dateStr to date string of d & " " & time string of d
            set msgContent to "From: " & sender of m & "\\nDate: " & dateStr & "\\nSubject: " & subject of m & "\\n---\\n" & content of m
            \(markReadScript)
            return msgContent
        end tell
    """)
    guard let text = result?.stringValue else {
        fputs("Error reading message.\n", stderr)
        exit(1)
    }
    if text == "INDEX_OUT_OF_RANGE" {
        fputs("Message index \(index) is out of range.\n", stderr)
        exit(1)
    }
    print(text)
}

func getDefaultSenderEmail() -> String {
    let result = runScript("""
        tell application "Mail"
            set acc to item 1 of accounts
            set addrs to email addresses of acc
            if (count of addrs) > 0 then
                return item 1 of addrs
            end if
            return ""
        end tell
    """)
    return result?.stringValue ?? ""
}

func sendMessage(to recipient: String, subject: String, body: String, attachmentPath: String, fromEmail: String, force: Bool, htmlFilePath: String) {
    if !attachmentPath.isEmpty && !FileManager.default.fileExists(atPath: attachmentPath) {
        fputs("Attachment not found: \(attachmentPath)\n", stderr)
        exit(1)
    }
    if !htmlFilePath.isEmpty && !FileManager.default.fileExists(atPath: htmlFilePath) {
        fputs("HTML file not found: \(htmlFilePath)\n", stderr)
        exit(1)
    }
    let sender = fromEmail.isEmpty ? getDefaultSenderEmail() : fromEmail
    let senderProp = sender.isEmpty ? "" : ", sender:\"\(escapeForAppleScript(sender))\""
    let visibleProp = force ? "" : ", visible:true"

    // When using --html-file, read HTML from file inside AppleScript to avoid escaping issues.
    // The content property is set to empty string; html content overrides it.
    let contentValue = htmlFilePath.isEmpty ? escapeForAppleScript(body) : ""
    var script = """
        tell application "Mail"
            set newMsg to make new outgoing message with properties {subject:"\(escapeForAppleScript(subject))", content:"\(contentValue)"\(senderProp)\(visibleProp)}
            tell newMsg
                make new to recipient with properties {address:"\(escapeForAppleScript(recipient))"}
        """
    if !htmlFilePath.isEmpty {
        script += "\n        set html content of newMsg to (do shell script \"cat \" & quoted form of \"\(escapeForAppleScript(htmlFilePath))\")"
    }
    if !attachmentPath.isEmpty {
        script += "\n        make new attachment with properties {file name:POSIX file \"\(escapeForAppleScript(attachmentPath))\"}"
    }
    if force {
        script += """

                end tell
                send newMsg
                return "SENT"
            end tell
        """
    } else {
        script += """

                end tell
            end tell
            activate
            return "OPENED"
        """
    }
    let result = runScript(script)
    let status = result?.stringValue
    if status == "SENT" {
        let sentAttach = attachmentPath.isEmpty ? "" : ", with attachment"
        let sentFrom = sender.isEmpty ? "" : " from \(sender)"
        print("Message sent to \(recipient)\(sentFrom)\(sentAttach).")
    } else if status == "OPENED" {
        let openAttach = attachmentPath.isEmpty ? "" : " with attachment"
        print("Compose window opened\(openAttach) — review and send manually in Mail.app.")
    } else {
        fputs("Failed to compose message.\n", stderr)
        exit(1)
    }
}

func deleteMessage(index: Int, mailbox: String, account: String, force: Bool) {
    if !force {
        print("Dry-run: would move message #\(index) in '\(mailbox)' to Trash. Use --force to actually delete.")
        exit(0)
    }
    let accountClause = account.isEmpty
        ? "item 1 of accounts"
        : "account \"\(escapeForAppleScript(account))\""
    let result = runScript("""
        tell application "Mail"
            set acc to \(accountClause)
            set msgs to messages of mailbox "\(escapeForAppleScript(mailbox))" of acc
            set msgCount to count of msgs
            if \(index) < 1 or \(index) > msgCount then
                return "INDEX_OUT_OF_RANGE"
            end if
            delete item \(index) of msgs
            return "OK"
        end tell
    """)
    let status = result?.stringValue
    if status == "INDEX_OUT_OF_RANGE" {
        fputs("Message index \(index) is out of range.\n", stderr)
        exit(1)
    } else if status == "OK" {
        print("Moved message #\(index) to Trash.")
    } else {
        fputs("Failed to delete message.\n", stderr)
        exit(1)
    }
}

// MARK: - Main

let args = CommandLine.arguments

guard args.count >= 2 else {
    print("Usage:")
    print("  mail-bridge accounts")
    print("  mail-bridge mailboxes [account]")
    print("  mail-bridge list [mailbox] [account] [count]")
    print("  mail-bridge unread [mailbox] [account]")
    print("  mail-bridge search <query> [account]")
    print("  mail-bridge read <index> [mailbox] [account] [--mark-read]")
    print("  mail-bridge send <to> <subject> <body> [/path/to/attachment] [--from <email>] [--html-file <path>] [--force]")
    print("  mail-bridge delete <index> [mailbox] [account] [--force]")
    exit(0)
}

let command = args[1]
let defaultMailbox = "INBOX"

// Get all account names for smart argument detection
func getAccountNames() -> [String] {
    let result = runScript("""
        tell application "Mail"
            set out to {}
            repeat with acc in accounts
                set end of out to name of acc
            end repeat
            return out
        end tell
    """)
    return descriptorToStrings(result)
}

let accountNames = getAccountNames()

// Check if a string is an account name (not a mailbox)
func isAccountName(_ name: String) -> Bool {
    let normalized = normalizeQuotes(in: name)
    return accountNames.contains(where: { normalizeQuotes(in: $0) == normalized })
}

switch command {

case "accounts":
    listAccounts()

case "mailboxes":
    let account = args.count >= 3 ? args[2] : ""
    listMailboxes(account: account)

case "list":
    var mailbox = defaultMailbox
    var account = ""
    var count = 20
    if args.count >= 3 {
        if let num = Int(args[2]) {
            // list <count>
            count = num
        } else if isAccountName(args[2]) {
            // list <account> [count]
            account = args[2]
            count = args.count >= 4 ? (Int(args[3]) ?? 20) : 20
        } else {
            // list <mailbox> [count | account] [count]
            mailbox = args[2]
            if args.count >= 4 {
                if let num = Int(args[3]) {
                    count = num
                } else if isAccountName(args[3]) {
                    account = args[3]
                    count = args.count >= 5 ? (Int(args[4]) ?? 20) : 20
                }
            }
        }
    }
    listMessages(mailbox: mailbox, account: account, count: count)

case "unread":
    var mailbox = defaultMailbox
    var account = ""
    if args.count >= 3 {
        if isAccountName(args[2]) {
            account = args[2]
        } else {
            mailbox = args[2]
            account = args.count >= 4 ? args[3] : ""
        }
    }
    listUnread(mailbox: mailbox, account: account)

case "search":
    guard args.count >= 3 else {
        fputs("Usage: mail-bridge search <query> [max_results] [account]\n", stderr)
        exit(1)
    }
    var searchAccount = ""
    var searchMax = 50
    // args after query: could be a number (max results), an account name, or both
    if args.count >= 4 {
        if let num = Int(args[3]) {
            searchMax = num
            searchAccount = args.count >= 5 ? args[4] : ""
        } else if isAccountName(args[3]) {
            searchAccount = args[3]
        }
    }
    searchMessages(query: args[2], account: searchAccount, maxResults: searchMax)

case "read":
    guard args.count >= 3, let index = Int(args[2]) else {
        fputs("Usage: mail-bridge read <index> [mailbox] [account] [--mark-read]\n", stderr)
        exit(1)
    }
    let markRead = args.contains("--mark-read")
    let readArgs = args.filter { $0 != "--mark-read" }
    let mailbox = readArgs.count >= 4 ? readArgs[3] : defaultMailbox
    let account = readArgs.count >= 5 ? readArgs[4] : ""
    readMessage(index: index, mailbox: mailbox, account: account, markRead: markRead)

case "send":
    let force = args.contains("--force")
    var fromEmail = ""
    if let fromIdx = args.firstIndex(of: "--from"), fromIdx + 1 < args.count {
        fromEmail = args[fromIdx + 1]
    }
    var htmlFilePath = ""
    if let htmlIdx = args.firstIndex(of: "--html-file"), htmlIdx + 1 < args.count {
        htmlFilePath = args[htmlIdx + 1]
    }
    // With --html-file, body is optional (only to/subject required)
    let minArgs = htmlFilePath.isEmpty ? 5 : 4
    guard args.count >= minArgs else {
        fputs("Usage: mail-bridge send <to> <subject> [body] [/path/to/attachment] [--from <email>] [--html-file <path>] [--force]\n", stderr)
        exit(1)
    }
    let body = args.count >= 5 ? args[4] : ""
    let flagArgs = Set(["--force", "--from", fromEmail, "--html-file", htmlFilePath].filter { !$0.isEmpty })
    let positional = args.dropFirst(min(5, args.count)).filter { !flagArgs.contains($0) }
    let attachmentPath = positional.first ?? ""
    sendMessage(to: args[2], subject: args[3], body: body, attachmentPath: attachmentPath, fromEmail: fromEmail, force: force, htmlFilePath: htmlFilePath)

case "delete":
    guard args.count >= 3, let index = Int(args[2]) else {
        fputs("Usage: mail-bridge delete <index> [mailbox] [account] [--force]\n", stderr)
        exit(1)
    }
    let force = args.contains("--force")
    let filteredArgs = args.filter { $0 != "--force" }
    let mailbox = filteredArgs.count >= 4 ? filteredArgs[3] : defaultMailbox
    let account = filteredArgs.count >= 5 ? filteredArgs[4] : ""
    deleteMessage(index: index, mailbox: mailbox, account: account, force: force)

default:
    fputs("Unknown command: \(command)\n", stderr)
    exit(1)
}
```

## File: `notes-bridge.swift`
```
#!/usr/bin/env swift

// notes-bridge.swift
// A small CLI bridge for Claude Code to access Apple Notes via NSAppleScript.
// Usage:
//   notes-bridge accounts                                      - List all accounts
//   notes-bridge folders [account]                             - List folders (default: iCloud)
//   notes-bridge list [folder] [account]                       - List notes in folder
//   notes-bridge search <query>                                - Search notes by title and content
//   notes-bridge read <title> [account]                        - Read note content (plain text)
//   notes-bridge add <folder> <title> <body> [account]         - Create new note
//   notes-bridge append <title> <text> [account]               - Append text to existing note

import Foundation

// MARK: - String Helpers

func escapeForAppleScript(_ string: String) -> String {
    string
        .replacingOccurrences(of: "\\", with: "\\\\")
        .replacingOccurrences(of: "\"", with: "\\\"")
}

func normalizeQuotes(in string: String) -> String {
    string
        .replacingOccurrences(of: "\u{2018}", with: "'")
        .replacingOccurrences(of: "\u{2019}", with: "'")
        .replacingOccurrences(of: "\u{201C}", with: "\"")
        .replacingOccurrences(of: "\u{201D}", with: "\"")
}

// MARK: - AppleScript Runner

func runScript(_ source: String) -> NSAppleEventDescriptor? {
    var errorInfo: NSDictionary?
    guard let script = NSAppleScript(source: source) else { return nil }
    let result = script.executeAndReturnError(&errorInfo)
    if let error = errorInfo {
        let message = error[NSAppleScript.errorMessage] as? String ?? "Unknown error"
        fputs("AppleScript error: \(message)\n", stderr)
        return nil
    }
    return result
}

func descriptorToStrings(_ descriptor: NSAppleEventDescriptor?) -> [String] {
    guard let desc = descriptor else { return [] }
    // If it's a list, iterate via numberOfItems
    if desc.numberOfItems > 0 {
        var items: [String] = []
        for i in 1...desc.numberOfItems {
            if let item = desc.atIndex(i)?.stringValue {
                items.append(item)
            }
        }
        return items
    }
    // Single value
    if let value = desc.stringValue, !value.isEmpty {
        return [value]
    }
    return []
}

// MARK: - HTML Stripping

func stripHTML(_ html: String) -> String {
    var text = html
    // Block elements → newlines
    for tag in ["</p>", "<br>", "<br/>", "<br />", "</div>", "</li>"] {
        text = text.replacingOccurrences(of: tag, with: "\n", options: .caseInsensitive)
    }
    // Strip all remaining HTML tags
    text = text.replacingOccurrences(of: "<[^>]+>", with: "", options: .regularExpression)
    // Decode common HTML entities
    let entities: [(String, String)] = [
        ("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"),
        ("&gt;", ">"), ("&quot;", "\""), ("&#39;", "'")
    ]
    entities.forEach { text = text.replacingOccurrences(of: $0.0, with: $0.1) }
    // Collapse excessive newlines
    while text.contains("\n\n\n") {
        text = text.replacingOccurrences(of: "\n\n\n", with: "\n\n")
    }
    return text.trimmingCharacters(in: .whitespacesAndNewlines)
}

// MARK: - Commands

func listAccounts() {
    let result = runScript("""
        tell application "Notes"
            set out to {}
            repeat with acc in accounts
                set end of out to name of acc
            end repeat
            return out
        end tell
    """)
    descriptorToStrings(result).forEach { print($0) }
}

func listFolders(account: String) {
    let result = runScript("""
        tell application "Notes"
            set out to {}
            repeat with f in folders of account "\(escapeForAppleScript(account))"
                set end of out to name of f
            end repeat
            return out
        end tell
    """)
    let folders = descriptorToStrings(result)
    if folders.isEmpty {
        fputs("No folders found in account '\(account)'.\n", stderr)
        exit(1)
    }
    folders.forEach { print($0) }
}

func listNotes(folder: String, account: String) {
    let result = runScript("""
        tell application "Notes"
            set out to {}
            set targetFolder to folder "\(escapeForAppleScript(folder))" of account "\(escapeForAppleScript(account))"
            repeat with n in notes of targetFolder
                set d to modification date of n
                set dateStr to (year of d as string) & "-" ¬
                    & text -2 thru -1 of ("0" & (month of d as integer as string)) & "-" ¬
                    & text -2 thru -1 of ("0" & (day of d as string))
                set end of out to name of n & "  [" & dateStr & "]"
            end repeat
            return out
        end tell
    """)
    let notes = descriptorToStrings(result)
    if notes.isEmpty {
        print("No notes in '\(folder)'.")
    } else {
        notes.forEach { print($0) }
    }
}

func searchNotes(query: String) {
    let result = runScript("""
        tell application "Notes"
            set out to {}
            repeat with acc in accounts
                repeat with f in folders of acc
                    repeat with n in notes of f
                        set titleMatch to name of n contains "\(escapeForAppleScript(query))"
                        set bodyMatch to plaintext of n contains "\(escapeForAppleScript(query))"
                        if titleMatch or bodyMatch then
                            set end of out to name of n & "  [" & name of f & " / " & name of acc & "]"
                        end if
                    end repeat
                end repeat
            end repeat
            return out
        end tell
    """)
    let matches = descriptorToStrings(result)
    if matches.isEmpty {
        print("No notes matching '\(query)'.")
    } else {
        print("Found \(matches.count) note(s):")
        matches.forEach { print("  " + $0) }
    }
}

func readNote(title: String, account: String) {
    let result = runScript("""
        tell application "Notes"
            set matchNote to missing value
            repeat with acc in accounts
                if name of acc is "\(account)" or "\(account)" is "" then
                    repeat with f in folders of acc
                        repeat with n in notes of f
                            if name of n is "\(escapeForAppleScript(title))" then
                                set matchNote to n
                                exit repeat
                            end if
                        end repeat
                        if matchNote is not missing value then exit repeat
                    end repeat
                end if
                if matchNote is not missing value then exit repeat
            end repeat
            if matchNote is missing value then
                return "NOTE_NOT_FOUND"
            end if
            return plaintext of matchNote
        end tell
    """)
    guard let text = result?.stringValue else {
        fputs("Error reading note.\n", stderr)
        exit(1)
    }
    if text == "NOTE_NOT_FOUND" {
        fputs("Note '\(title)' not found.\n", stderr)
        exit(1)
    }
    print(text)
}

func addNote(folder: String, title: String, body: String, account: String) {
    let result = runScript("""
        tell application "Notes"
            set targetFolder to folder "\(escapeForAppleScript(folder))" of account "\(escapeForAppleScript(account))"
            make new note at targetFolder with properties {name:"\(escapeForAppleScript(title))", body:"\(escapeForAppleScript(body))"}
            return "OK"
        end tell
    """)
    if result?.stringValue == "OK" {
        print("Created note: \(title)")
    } else {
        fputs("Failed to create note.\n", stderr)
        exit(1)
    }
}

func appendToNote(title: String, text: String, account: String) {
    let result = runScript("""
        tell application "Notes"
            set matchNote to missing value
            repeat with acc in accounts
                if name of acc is "\(account)" or "\(account)" is "" then
                    repeat with f in folders of acc
                        repeat with n in notes of f
                            if name of n is "\(escapeForAppleScript(title))" then
                                set matchNote to n
                                exit repeat
                            end if
                        end repeat
                        if matchNote is not missing value then exit repeat
                    end repeat
                end if
                if matchNote is not missing value then exit repeat
            end repeat
            if matchNote is missing value then
                return "NOTE_NOT_FOUND"
            end if
            set body of matchNote to body of matchNote & "<br>\(escapeForAppleScript(text))"
            return "OK"
        end tell
    """)
    let status = result?.stringValue
    if status == "NOTE_NOT_FOUND" {
        fputs("Note '\(title)' not found.\n", stderr)
        exit(1)
    } else if status == "OK" {
        print("Appended to note: \(title)")
    } else {
        fputs("Failed to append to note.\n", stderr)
        exit(1)
    }
}

func deleteNote(title: String, account: String, force: Bool) {
    let result = runScript("""
        tell application "Notes"
            set matchNote to missing value
            repeat with acc in accounts
                if name of acc is "\(account)" or "\(account)" is "" then
                    repeat with f in folders of acc
                        repeat with n in notes of f
                            if name of n is "\(escapeForAppleScript(title))" then
                                set matchNote to n
                                exit repeat
                            end if
                        end repeat
                        if matchNote is not missing value then exit repeat
                    end repeat
                end if
                if matchNote is not missing value then exit repeat
            end repeat
            if matchNote is missing value then
                return "NOTE_NOT_FOUND"
            end if
            delete matchNote
            return "OK"
        end tell
    """)
    let status = result?.stringValue
    if status == "NOTE_NOT_FOUND" {
        fputs("Note '\(title)' not found.\n", stderr)
        exit(1)
    } else if status == "OK" {
        print("Deleted note: \(title)")
    } else {
        fputs("Failed to delete note.\n", stderr)
        exit(1)
    }
}

// MARK: - Main

let args = CommandLine.arguments

guard args.count >= 2 else {
    print("Usage:")
    print("  notes-bridge accounts")
    print("  notes-bridge folders [account]")
    print("  notes-bridge list [folder] [account]")
    print("  notes-bridge search <query>")
    print("  notes-bridge read <title> [account]")
    print("  notes-bridge add <folder> <title> <body> [account]")
    print("  notes-bridge append <title> <text> [account]")
    print("  notes-bridge delete <title> [--force] [account]")
    exit(0)
}

let command = args[1]
let defaultAccount = "iCloud"
let defaultFolder = "Notes"

switch command {

case "accounts":
    listAccounts()

case "folders":
    let account = args.count >= 3 ? args[2] : defaultAccount
    listFolders(account: account)

case "list":
    let folder = args.count >= 3 ? args[2] : defaultFolder
    let account = args.count >= 4 ? args[3] : defaultAccount
    listNotes(folder: folder, account: account)

case "search":
    guard args.count >= 3 else {
        fputs("Usage: notes-bridge search <query>\n", stderr)
        exit(1)
    }
    searchNotes(query: args[2])

case "read":
    guard args.count >= 3 else {
        fputs("Usage: notes-bridge read <title> [account]\n", stderr)
        exit(1)
    }
    let account = args.count >= 4 ? args[3] : ""
    readNote(title: args[2], account: account)

case "add":
    guard args.count >= 5 else {
        fputs("Usage: notes-bridge add <folder> <title> <body> [account]\n", stderr)
        exit(1)
    }
    let account = args.count >= 6 ? args[5] : defaultAccount
    addNote(folder: args[2], title: args[3], body: args[4], account: account)

case "append":
    guard args.count >= 4 else {
        fputs("Usage: notes-bridge append <title> <text> [account]\n", stderr)
        exit(1)
    }
    let account = args.count >= 5 ? args[4] : ""
    appendToNote(title: args[2], text: args[3], account: account)

case "delete":
    guard args.count >= 3 else {
        fputs("Usage: notes-bridge delete <title> [--force] [account]\n", stderr)
        exit(1)
    }
    let force = args.contains("--force")
    let account = args.filter { $0 != "--force" }.count >= 4 ? args.filter { $0 != "--force" }[3] : ""
    if !force {
        print("Dry-run: would delete '\(args[2])'. Use --force to actually delete.")
        exit(0)
    }
    deleteNote(title: args[2], account: account, force: force)

default:
    fputs("Unknown command: \(command)\n", stderr)
    exit(1)
}
```

## File: `reminders-bridge.swift`
```
#!/usr/bin/env swift

// reminders-bridge.swift
// Copyright © 2026 Tobias Stöger (tstoegi). Licensed under the MIT License.
// A small CLI bridge for Claude Code to access Apple Reminders via EventKit.
// Usage:
//   reminders-bridge lists                              - List all reminder lists
//   reminders-bridge create-list <listName>             - Create a new list
//   reminders-bridge items <listName>                   - List all reminders in a list
//   reminders-bridge incomplete <listName>              - Show incomplete reminders in a list
//   reminders-bridge today                              - Show reminders due today (all lists)
//   reminders-bridge overdue                            - Show overdue reminders (all lists)
//   reminders-bridge search <query>                     - Search reminders by title/notes (all lists)
//   reminders-bridge add <listName> <title> [notes]     - Add a new reminder
//   reminders-bridge set-due <listName> <title> <datetime> - Set due date (YYYY-MM-DD HH:mm)
//   reminders-bridge set-notes <listName> <title> <notes>  - Set or update notes
//   reminders-bridge complete <listName> <title>        - Mark a reminder as complete
//   reminders-bridge delete <listName> <title>          - Delete a reminder

import EventKit
import Foundation

let store = EKEventStore()

func requestAccess() async -> Bool {
    do {
        return try await store.requestFullAccessToReminders()
    } catch {
        fputs("Error requesting access: \(error.localizedDescription)\n", stderr)
        return false
    }
}

// MARK: - String Normalization

// Normalize typographic quotes to ASCII equivalents for reliable matching.
// Apple apps (e.g. Reminders shared lists) often use smart quotes like U+2019
// which don't match the ASCII apostrophe (U+0027) typed from the keyboard.
func normalizeQuotes(in string: String) -> String {
    string
        .replacingOccurrences(of: "\u{2018}", with: "'")  // left single quote
        .replacingOccurrences(of: "\u{2019}", with: "'")  // right single quote
        .replacingOccurrences(of: "\u{201C}", with: "\"") // left double quote
        .replacingOccurrences(of: "\u{201D}", with: "\"") // right double quote
}

func findCalendar(named listName: String) -> EKCalendar? {
    let normalized = normalizeQuotes(in: listName)
    return store.calendars(for: .reminder).first(where: {
        normalizeQuotes(in: $0.title) == normalized
    })
}

// MARK: - Formatting

func formatReminder(_ reminder: EKReminder) {
    let status = reminder.isCompleted ? "[x]" : "[ ]"
    let dueStr: String
    if let due = reminder.dueDateComponents, let date = Calendar.current.date(from: due) {
        let formatter = DateFormatter()
        formatter.dateStyle = .short
        formatter.timeStyle = .short
        dueStr = " (due: \(formatter.string(from: date)))"
    } else {
        dueStr = ""
    }
    let priority: String
    switch reminder.priority {
    case 1...4: priority = " !!"
    case 5:     priority = " !"
    default:    priority = ""
    }
    let recurrenceStr: String
    if let rules = reminder.recurrenceRules, let rule = rules.first {
        let freq: String
        switch rule.frequency {
        case .daily:   freq = "daily"
        case .weekly:  freq = "weekly"
        case .monthly: freq = "monthly"
        case .yearly:  freq = "yearly"
        @unknown default: freq = "unknown"
        }
        let interval = rule.interval > 1 ? " (every \(rule.interval))" : ""
        recurrenceStr = " [repeats: \(freq)\(interval)]"
    } else {
        recurrenceStr = ""
    }
    let listStr = " [\(reminder.calendar.title)]"
    let idStr = " {id:\(reminder.calendarItemIdentifier)}"
    let notesStr = (reminder.notes != nil && !reminder.notes!.isEmpty) ? "\n     Notes: \(reminder.notes!)" : ""
    print("\(status) \(reminder.title ?? "(no title)")\(priority)\(dueStr)\(recurrenceStr)\(listStr)\(idStr)\(notesStr)")
}

// MARK: - Fetch Helpers

func fetchAll(from calendars: [EKCalendar], completion: @escaping ([EKReminder]) -> Void) {
    let predicate = store.predicateForReminders(in: calendars)
    store.fetchReminders(matching: predicate) { reminders in
        completion(reminders ?? [])
    }
}

// MARK: - Commands

func listAllLists() {
    let calendars = store.calendars(for: .reminder)
    for calendar in calendars.sorted(by: { $0.title < $1.title }) {
        print(calendar.title)
    }
}

func listItems(listName: String, onlyIncomplete: Bool = false) {
    guard let calendar = findCalendar(named: listName) else {
        fputs("List '\(listName)' not found.\n\nAvailable lists:\n", stderr)
        store.calendars(for: .reminder).sorted(by: { $0.title < $1.title }).forEach {
            fputs("  \(normalizeQuotes(in: $0.title))\n", stderr)
        }
        exit(1)
    }
    let semaphore = DispatchSemaphore(value: 0)
    fetchAll(from: [calendar]) { reminders in
        let filtered = onlyIncomplete ? reminders.filter { !$0.isCompleted } : reminders
        let sorted = filtered.sorted { ($0.creationDate ?? .distantPast) < ($1.creationDate ?? .distantPast) }
        sorted.forEach { formatReminder($0) }
        semaphore.signal()
    }
    semaphore.wait()
}

func showToday() {
    let calendars = store.calendars(for: .reminder)
    let semaphore = DispatchSemaphore(value: 0)
    fetchAll(from: calendars) { reminders in
        let today = Calendar.current.startOfDay(for: Date())
        let tomorrow = Calendar.current.date(byAdding: .day, value: 1, to: today)!
        let due = reminders.filter { reminder in
            guard !reminder.isCompleted,
                  let comps = reminder.dueDateComponents,
                  let date = Calendar.current.date(from: comps) else { return false }
            return date >= today && date < tomorrow
        }.sorted { ($0.dueDateComponents.flatMap { Calendar.current.date(from: $0) } ?? .distantFuture)
                 < ($1.dueDateComponents.flatMap { Calendar.current.date(from: $0) } ?? .distantFuture) }
        if due.isEmpty {
            print("No reminders due today.")
        } else {
            print("\(due.count) reminder(s) due today:")
            due.forEach { formatReminder($0) }
        }
        semaphore.signal()
    }
    semaphore.wait()
}

func showOverdue() {
    let calendars = store.calendars(for: .reminder)
    let semaphore = DispatchSemaphore(value: 0)
    fetchAll(from: calendars) { reminders in
        let now = Date()
        let overdue = reminders.filter { reminder in
            guard !reminder.isCompleted,
                  let comps = reminder.dueDateComponents,
                  let date = Calendar.current.date(from: comps) else { return false }
            return date < now
        }.sorted { ($0.dueDateComponents.flatMap { Calendar.current.date(from: $0) } ?? .distantPast)
                 < ($1.dueDateComponents.flatMap { Calendar.current.date(from: $0) } ?? .distantPast) }
        if overdue.isEmpty {
            print("No overdue reminders.")
        } else {
            print("\(overdue.count) overdue reminder(s):")
            overdue.forEach { formatReminder($0) }
        }
        semaphore.signal()
    }
    semaphore.wait()
}

func searchReminders(query: String) {
    let calendars = store.calendars(for: .reminder)
    let semaphore = DispatchSemaphore(value: 0)
    let lower = query.lowercased()
    fetchAll(from: calendars) { reminders in
        let matches = reminders.filter { reminder in
            (reminder.title?.lowercased().contains(lower) ?? false) ||
            (reminder.notes?.lowercased().contains(lower) ?? false)
        }.sorted { ($0.creationDate ?? .distantPast) < ($1.creationDate ?? .distantPast) }
        if matches.isEmpty {
            print("No reminders found for '\(query)'.")
        } else {
            print("\(matches.count) result(s) for '\(query)':")
            matches.forEach { formatReminder($0) }
        }
        semaphore.signal()
    }
    semaphore.wait()
}

func createList(listName: String) {
    let calendar = EKCalendar(for: .reminder, eventStore: store)
    calendar.title = listName
    calendar.source = store.defaultCalendarForNewReminders()?.source
    do {
        try store.saveCalendar(calendar, commit: true)
        print("Created list: \(listName)")
    } catch {
        fputs("Error creating list: \(error.localizedDescription)\n", stderr)
        exit(1)
    }
}

func addReminder(listName: String, title: String, notes: String? = nil) {
    guard let calendar = findCalendar(named: listName) else {
        fputs("List '\(listName)' not found.\n\nAvailable lists:\n", stderr)
        store.calendars(for: .reminder).sorted(by: { $0.title < $1.title }).forEach {
            fputs("  \(normalizeQuotes(in: $0.title))\n", stderr)
        }
        exit(1)
    }
    let reminder = EKReminder(eventStore: store)
    reminder.title = title
    reminder.notes = notes
    reminder.calendar = calendar
    do {
        try store.save(reminder, commit: true)
        print("Added: \(title)")
    } catch {
        fputs("Error saving reminder: \(error.localizedDescription)\n", stderr)
        exit(1)
    }
}

func setDueDate(listName: String, title: String, dateString: String) {
    guard let calendar = findCalendar(named: listName) else {
        fputs("List '\(listName)' not found.\n\nAvailable lists:\n", stderr)
        store.calendars(for: .reminder).sorted(by: { $0.title < $1.title }).forEach {
            fputs("  \(normalizeQuotes(in: $0.title))\n", stderr)
        }
        exit(1)
    }
    let formatter = DateFormatter()
    formatter.dateFormat = "yyyy-MM-dd HH:mm"
    formatter.locale = Locale(identifier: "en_US_POSIX")
    guard let date = formatter.date(from: dateString) else {
        fputs("Invalid date format. Use: YYYY-MM-DD HH:mm\n", stderr)
        exit(1)
    }
    let semaphore = DispatchSemaphore(value: 0)
    fetchAll(from: [calendar]) { reminders in
        guard let match = reminders.first(where: { $0.title == title && !$0.isCompleted }) else {
            fputs("Reminder '\(title)' not found or already completed.\n", stderr)
            semaphore.signal()
            return
        }
        match.dueDateComponents = Calendar.current.dateComponents([.year, .month, .day, .hour, .minute], from: date)
        do {
            try store.save(match, commit: true)
            print("Updated due date: \(title) → \(dateString)")
        } catch {
            fputs("Error: \(error.localizedDescription)\n", stderr)
        }
        semaphore.signal()
    }
    semaphore.wait()
}

func setNotes(listName: String, title: String, notes: String) {
    guard let calendar = findCalendar(named: listName) else {
        fputs("List '\(listName)' not found.\n\nAvailable lists:\n", stderr)
        store.calendars(for: .reminder).sorted(by: { $0.title < $1.title }).forEach {
            fputs("  \(normalizeQuotes(in: $0.title))\n", stderr)
        }
        exit(1)
    }
    let semaphore = DispatchSemaphore(value: 0)
    fetchAll(from: [calendar]) { reminders in
        guard let match = reminders.first(where: { $0.title == title && !$0.isCompleted }) else {
            fputs("Reminder '\(title)' not found or already completed.\n", stderr)
            semaphore.signal()
            return
        }
        match.notes = notes
        do {
            try store.save(match, commit: true)
            print("Updated notes: \(title)")
        } catch {
            fputs("Error: \(error.localizedDescription)\n", stderr)
        }
        semaphore.signal()
    }
    semaphore.wait()
}

func completeReminder(listName: String, title: String) {
    guard let calendar = findCalendar(named: listName) else {
        fputs("List '\(listName)' not found.\n\nAvailable lists:\n", stderr)
        store.calendars(for: .reminder).sorted(by: { $0.title < $1.title }).forEach {
            fputs("  \(normalizeQuotes(in: $0.title))\n", stderr)
        }
        exit(1)
    }
    let semaphore = DispatchSemaphore(value: 0)
    fetchAll(from: [calendar]) { reminders in
        guard let match = reminders.first(where: { $0.title == title && !$0.isCompleted }) else {
            fputs("Reminder '\(title)' not found or already completed.\n", stderr)
            semaphore.signal()
            return
        }
        match.isCompleted = true
        do {
            try store.save(match, commit: true)
            print("Completed: \(title)")
        } catch {
            fputs("Error: \(error.localizedDescription)\n", stderr)
        }
        semaphore.signal()
    }
    semaphore.wait()
}

func deleteReminder(listName: String, title: String, force: Bool) {
    guard let calendar = findCalendar(named: listName) else {
        fputs("List '\(listName)' not found.\n\nAvailable lists:\n", stderr)
        store.calendars(for: .reminder).sorted(by: { $0.title < $1.title }).forEach {
            fputs("  \(normalizeQuotes(in: $0.title))\n", stderr)
        }
        exit(1)
    }
    let semaphore = DispatchSemaphore(value: 0)
    fetchAll(from: [calendar]) { reminders in
        guard let match = reminders.first(where: { $0.title == title }) else {
            fputs("Reminder '\(title)' not found.\n", stderr)
            semaphore.signal()
            return
        }
        guard force else {
            print("Would delete: \(title) (list: \(listName))")
            print("Re-run with --force to actually delete.")
            semaphore.signal()
            return
        }
        do {
            try store.remove(match, commit: true)
            print("Deleted: \(title)")
        } catch {
            fputs("Error: \(error.localizedDescription)\n", stderr)
        }
        semaphore.signal()
    }
    semaphore.wait()
}

// MARK: - Main

let args = CommandLine.arguments

guard args.count >= 2 else {
    print("Usage:")
    print("  reminders-bridge lists")
    print("  reminders-bridge create-list <listName>")
    print("  reminders-bridge items <listName>")
    print("  reminders-bridge incomplete <listName>")
    print("  reminders-bridge today")
    print("  reminders-bridge overdue")
    print("  reminders-bridge search <query>")
    print("  reminders-bridge add <listName> <title> [notes]")
    print("  reminders-bridge set-due <listName> <title> <\"YYYY-MM-DD HH:mm\">")
    print("  reminders-bridge set-notes <listName> <title> <notes>")
    print("  reminders-bridge complete <listName> <title>")
    print("  reminders-bridge delete <listName> <title>")
    exit(0)
}

let accessSemaphore = DispatchSemaphore(value: 0)
var hasAccess = false

Task {
    hasAccess = await requestAccess()
    accessSemaphore.signal()
}
accessSemaphore.wait()

guard hasAccess else {
    fputs("No access to Reminders. Please grant permission in System Settings > Privacy & Security > Reminders.\n", stderr)
    exit(1)
}

let command = args[1]

switch command {
case "lists":
    listAllLists()

case "create-list":
    guard args.count >= 3 else { fputs("Usage: reminders-bridge create-list <listName>\n", stderr); exit(1) }
    createList(listName: args[2])

case "items":
    guard args.count >= 3 else { fputs("Usage: reminders-bridge items <listName>\n", stderr); exit(1) }
    listItems(listName: args[2])

case "incomplete":
    guard args.count >= 3 else { fputs("Usage: reminders-bridge incomplete <listName>\n", stderr); exit(1) }
    listItems(listName: args[2], onlyIncomplete: true)

case "today":
    showToday()

case "overdue":
    showOverdue()

case "search":
    guard args.count >= 3 else { fputs("Usage: reminders-bridge search <query>\n", stderr); exit(1) }
    searchReminders(query: args[2])

case "add":
    guard args.count >= 4 else { fputs("Usage: reminders-bridge add <listName> <title> [notes]\n", stderr); exit(1) }
    let notes = args.count >= 5 ? args[4] : nil
    addReminder(listName: args[2], title: args[3], notes: notes)

case "set-due":
    guard args.count >= 5 else { fputs("Usage: reminders-bridge set-due <listName> <title> <\"YYYY-MM-DD HH:mm\">\n", stderr); exit(1) }
    setDueDate(listName: args[2], title: args[3], dateString: args[4])

case "set-notes":
    guard args.count >= 5 else { fputs("Usage: reminders-bridge set-notes <listName> <title> <notes>\n", stderr); exit(1) }
    setNotes(listName: args[2], title: args[3], notes: args[4])

case "complete":
    guard args.count >= 4 else { fputs("Usage: reminders-bridge complete <listName> <title>\n", stderr); exit(1) }
    completeReminder(listName: args[2], title: args[3])

case "delete":
    guard args.count >= 4 else { fputs("Usage: reminders-bridge delete <listName> <title> [--force]\n", stderr); exit(1) }
    let force = args.contains("--force")
    deleteReminder(listName: args[2], title: args[3], force: force)

default:
    fputs("Unknown command: \(command)\n", stderr)
    exit(1)
}
```

## File: `test.sh`
```bash
#!/bin/bash
# test.sh
# Copyright © 2026 Tobias Stöger (tstoegi). Licensed under the MIT License.
# Integration tests for claude-apple-bridges.
# Run via: make test  or  bash test.sh

BRIDGE_DIR="${HOME}/.claude"
PASS=0
FAIL=0

green='\033[0;32m'
red='\033[0;31m'
reset='\033[0m'

check() {
    local description="$1"
    local expected_exit="$2"
    shift 2
    local cmd=("$@")

    output=$("${cmd[@]}" 2>&1)
    actual_exit=$?

    if [ "$actual_exit" -eq "$expected_exit" ]; then
        echo -e "  ${green}✓${reset} $description"
        PASS=$((PASS + 1))
    else
        echo -e "  ${red}✗${reset} $description"
        echo "    → exit $actual_exit (expected $expected_exit)"
        echo "    → output: $output"
        FAIL=$((FAIL + 1))
    fi
}

check_contains() {
    local description="$1"
    local needle="$2"
    shift 2
    local cmd=("$@")

    output=$("${cmd[@]}" 2>&1)
    actual_exit=$?

    if [ "$actual_exit" -eq 0 ] && echo "$output" | grep -qi "$needle"; then
        echo -e "  ${green}✓${reset} $description"
        PASS=$((PASS + 1))
    else
        echo -e "  ${red}✗${reset} $description"
        echo "    → exit $actual_exit, looking for: '$needle'"
        echo "    → output: $output"
        FAIL=$((FAIL + 1))
    fi
}

# ─── reminders-bridge ────────────────────────────────────────────

echo ""
echo "reminders-bridge"
echo "────────────────"

RB="$BRIDGE_DIR/reminders-bridge"

check        "lists: exits 0"                  0  "$RB" lists
check_contains "lists: returns at least one list" "." "$RB" lists
check        "today: exits 0"                  0  "$RB" today
check        "overdue: exits 0"                0  "$RB" overdue
check_contains "search nonexistent: exits 0, no results" "No reminders" "$RB" search "xyzzy_nonexistent_42"
check        "incomplete missing arg: exits 1" 1  "$RB" incomplete
check        "items missing arg: exits 1"      1  "$RB" items
check        "add missing arg: exits 1"        1  "$RB" add
check        "set-due missing arg: exits 1"    1  "$RB" set-due
check        "complete missing arg: exits 1"   1  "$RB" complete
check        "delete missing arg: exits 1"     1  "$RB" delete
check        "unknown command: exits 1"        1  "$RB" xyzzy

# ─── calendar-bridge ─────────────────────────────────────────────

echo ""
echo "calendar-bridge"
echo "───────────────"

CB="$BRIDGE_DIR/calendar-bridge"
TODAY=$(date +%Y-%m-%d)

check        "calendars: exits 0"              0  "$CB" calendars
check_contains "calendars: returns results"    "." "$CB" calendars
check        "today: exits 0"                  0  "$CB" today
check        "tomorrow: exits 0"               0  "$CB" tomorrow
check        "week: exits 0"                   0  "$CB" week
check        "events today: exits 0"           0  "$CB" events "$TODAY"
check        "free-slots today: exits 0"       0  "$CB" free-slots "$TODAY"
check_contains "free-slots: shows time range"  "–" "$CB" free-slots "$TODAY"
check_contains "search nonexistent: no results" "No events" "$CB" search "xyzzy_nonexistent_42"
check        "events missing arg: exits 1"     1  "$CB" events
check        "add missing arg: exits 1"        1  "$CB" add
check        "delete missing arg: exits 1"     1  "$CB" delete
check        "unknown command: exits 1"        1  "$CB" xyzzy

# ─── contacts-bridge ─────────────────────────────────────────────

echo ""
echo "contacts-bridge"
echo "───────────────"

KB="$BRIDGE_DIR/contacts-bridge"

check_contains "search nonexistent: no results" "No contacts" "$KB" search "xyzzy_nonexistent_42"
check        "birthdays-today: exits 0"        0  "$KB" birthdays-today
check        "birthdays-upcoming 30: exits 0"  0  "$KB" birthdays-upcoming 30
check        "search missing arg: exits 1"     1  "$KB" search
check        "show missing arg: exits 1"       1  "$KB" show
check        "add missing arg: exits 1"        1  "$KB" add
check        "update missing arg: exits 1"     1  "$KB" update
check        "delete missing arg: exits 1"     1  "$KB" delete
check        "birthdays-upcoming missing arg: exits 1" 1 "$KB" birthdays-upcoming
check        "unknown command: exits 1"        1  "$KB" xyzzy

# ─── notes-bridge ────────────────────────────────────────────────

echo ""
echo "notes-bridge"
echo "────────────"

NB="$BRIDGE_DIR/notes-bridge"

check        "accounts: exits 0"                    0  "$NB" accounts
check_contains "accounts: returns iCloud"           "iCloud" "$NB" accounts
check        "folders: exits 0"                     0  "$NB" folders
check_contains "folders: returns at least one"      "." "$NB" folders
check        "list: exits 0"                        0  "$NB" list
check_contains "search nonexistent: no results"     "No notes" "$NB" search "xyzzy_nonexistent_42"
check        "search missing arg: exits 1"          1  "$NB" search
check        "read missing arg: exits 1"            1  "$NB" read
check        "add missing arg: exits 1"             1  "$NB" add
check        "append missing arg: exits 1"          1  "$NB" append
check        "delete missing arg: exits 1"          1  "$NB" delete
check_contains "delete dry-run: no --force"        "Dry-run" "$NB" delete "xyzzy_nonexistent_42"
check        "unknown command: exits 1"             1  "$NB" xyzzy

# ─── mail-bridge ──────────────────────────────────────────────────

echo ""
echo "mail-bridge"
echo "───────────"

MB="$BRIDGE_DIR/mail-bridge"

check        "accounts: exits 0"                   0  "$MB" accounts
check_contains "accounts: returns at least one"    "." "$MB" accounts
check        "mailboxes: exits 0"                  0  "$MB" mailboxes
check_contains "mailboxes: returns INBOX"          "INBOX" "$MB" mailboxes
check        "list: exits 0"                       0  "$MB" list
check        "unread: exits 0"                     0  "$MB" unread
check_contains "search nonexistent: no results"   "No messages" "$MB" search "xyzzy_nonexistent_42"
check        "search missing arg: exits 1"         1  "$MB" search
check        "read missing arg: exits 1"           1  "$MB" read
check        "send missing arg: exits 1"           1  "$MB" send
check_contains "send dry-run: no --force"         "Dry-run" "$MB" send "test@test.com" "Subject" "Body"
check        "delete missing arg: exits 1"         1  "$MB" delete
check_contains "delete dry-run: no --force"       "Dry-run" "$MB" delete "1"
check        "unknown command: exits 1"            1  "$MB" xyzzy

# ─── tmux-bridge ──────────────────────────────────────────────────

echo ""
echo "tmux-bridge"
echo "───────────"

TB="$BRIDGE_DIR/tmux-bridge"

check        "sessions: exits 0"                  0  "$TB" sessions
check        "windows: exits 0"                   0  "$TB" windows
check        "panes: exits 0"                     0  "$TB" panes
check        "read missing arg: exits 1"          1  "$TB" read
check        "unknown command: exits 1"           1  "$TB" xyzzy

# ─── Summary ─────────────────────────────────────────────────────

echo ""
echo "────────────────────────────────"
TOTAL=$((PASS + FAIL))
if [ "$FAIL" -eq 0 ]; then
    echo -e "${green}All $TOTAL tests passed.${reset}"
    exit 0
else
    echo -e "${red}$FAIL/$TOTAL tests failed.${reset}"
    exit 1
fi
```

## File: `tmux-bridge.swift`
```
#!/usr/bin/env swift

// tmux-bridge.swift
// A small CLI bridge for Claude Code to read tmux session contents.
// Copyright © 2026 Tobias Stöger (tstoegi). Licensed under the MIT License.
// Usage:
//   tmux-bridge sessions                          - List all running sessions
//   tmux-bridge windows [session]                 - List windows in a session
//   tmux-bridge panes [session]                   - List all panes in a session
//   tmux-bridge read <session:window.pane>         - Read pane content
//   tmux-bridge write <target> <text> [--no-enter] - Send keystrokes to a pane
//   tmux-bridge snapshot [session]                - Read all panes (for end-of-day summary)

import Foundation

// MARK: - Shell Runner

func shell(_ args: [String]) -> (output: String, exit: Int32) {
    let process = Process()
    process.executableURL = URL(fileURLWithPath: "/usr/bin/env")
    process.arguments = args
    let pipe = Pipe()
    process.standardOutput = pipe
    process.standardError = pipe
    try? process.run()
    process.waitUntilExit()
    let data = pipe.fileHandleForReading.readDataToEndOfFile()
    let output = String(data: data, encoding: .utf8)?.trimmingCharacters(in: .newlines) ?? ""
    return (output, process.terminationStatus)
}

func tmux(_ args: [String]) -> String {
    let result = shell(["tmux"] + args)
    return result.output
}

func tmuxLines(_ args: [String]) -> [String] {
    let output = tmux(args)
    guard !output.isEmpty else { return [] }
    return output.components(separatedBy: "\n").filter { !$0.isEmpty }
}

// MARK: - Commands

func listSessions() {
    let lines = tmuxLines(["list-sessions", "-F",
        "#S  windows:#{session_windows}  created:#{session_created_string}  #{?session_attached,(attached),}"])
    if lines.isEmpty {
        print("No tmux sessions running.")
    } else {
        print("Sessions (\(lines.count)):")
        lines.forEach { print("  " + $0) }
    }
}

func listWindows(session: String) {
    let target = session.isEmpty ? "" : "-t \(session)"
    let args = ["list-windows"] + (session.isEmpty ? [] : ["-t", session]) + ["-F",
        "#{window_index}: #{window_name}  [#{window_width}x#{window_height}]  #{window_panes} pane(s)#{?window_active, (active),}"]
    let lines = tmuxLines(args)
    if lines.isEmpty {
        fputs("No windows found\(session.isEmpty ? "" : " in session '\(session)'")\n", stderr)
        exit(1)
    }
    let label = session.isEmpty ? "current session" : "session '\(session)'"
    print("Windows in \(label):")
    lines.forEach { print("  " + $0) }
    _ = target
}

func listPanes(session: String) {
    let args = ["list-panes"] + (session.isEmpty ? ["-a"] : ["-t", session, "-a"]) + ["-F",
        "#{session_name}:#{window_index}.#{pane_index}  [#{pane_width}x#{pane_height}]  #{pane_current_command}  #{pane_current_path}"]
    let lines = tmuxLines(args)
    if lines.isEmpty {
        fputs("No panes found\(session.isEmpty ? "" : " in session '\(session)'")\n", stderr)
        exit(1)
    }
    let paneLabel = session.isEmpty ? "Panes" : "Panes in '\(session)'"
    print("\(paneLabel) (\(lines.count)):")
    lines.forEach { print("  " + $0) }
}

func readPane(target: String, lines: Int) {
    // target format: session:window.pane  e.g. "main:0.0" or just "main"
    let result = shell(["tmux", "capture-pane", "-t", target, "-p", "-S", "-\(lines)"])
    if result.exit != 0 {
        fputs("Pane '\(target)' not found. Use 'tmux-bridge panes' to list available targets.\n", stderr)
        exit(1)
    }
    let content = result.output
    if content.isEmpty {
        print("(empty)")
    } else {
        print(content)
    }
}

func writePane(target: String, text: String, sendEnter: Bool) {
    var keys = [String]()
    keys += ["send-keys", "-t", target, text]
    if sendEnter {
        keys += ["Enter"]
    }
    let result = shell(["tmux"] + keys)
    if result.exit != 0 {
        fputs("Pane '\(target)' not found. Use 'tmux-bridge panes' to list available targets.\n", stderr)
        exit(1)
    }
    if sendEnter {
        print("Sent to \(target): \(text) [Enter]")
    } else {
        print("Sent to \(target): \(text)")
    }
}

func snapshot(session: String, lines: Int) {
    // Get all panes
    let args = ["list-panes"] + (session.isEmpty ? ["-a"] : ["-t", session]) + ["-F",
        "#{session_name}:#{window_index}.#{pane_index}\t#{window_name}\t#{pane_current_command}\t#{pane_current_path}"]
    let paneLines = tmuxLines(args)

    if paneLines.isEmpty {
        fputs("No panes found\(session.isEmpty ? "" : " in '\(session)'")\n", stderr)
        exit(1)
    }

    let label = session.isEmpty ? "all sessions" : "session '\(session)'"
    print("=== tmux snapshot: \(label) ===")
    print("Captured: \(Date())")
    print("")

    for paneLine in paneLines {
        let parts = paneLine.components(separatedBy: "\t")
        guard parts.count >= 4 else { continue }
        let target = parts[0]
        let windowName = parts[1]
        let command = parts[2]
        let path = parts[3]

        print("─────────────────────────────────────")
        print("Pane: \(target)  [\(windowName)] \(command) @ \(path)")
        print("─────────────────────────────────────")

        let result = shell(["tmux", "capture-pane", "-t", target, "-p", "-S", "-\(lines)"])
        let content = result.output
        if content.isEmpty {
            print("(empty)")
        } else {
            print(content)
        }
        print("")
    }
}

// MARK: - Main

let args = CommandLine.arguments

guard args.count >= 2 else {
    print("Usage:")
    print("  tmux-bridge sessions                         List all running sessions")
    print("  tmux-bridge windows [session]                List windows in session")
    print("  tmux-bridge panes [session]                  List all panes")
    print("  tmux-bridge read <target> [lines]            Read pane (e.g. main:0.0, default: 1000 lines)")
    print("  tmux-bridge write <target> <text> [--no-enter]  Send keystrokes to a pane")
    print("  tmux-bridge snapshot [session] [lines]       Full snapshot of all panes (default: 5000 lines)")
    exit(0)
}

let command = args[1]

switch command {

case "sessions":
    listSessions()

case "windows":
    let session = args.count >= 3 ? args[2] : ""
    listWindows(session: session)

case "panes":
    let session = args.count >= 3 ? args[2] : ""
    listPanes(session: session)

case "read":
    guard args.count >= 3 else {
        fputs("Usage: tmux-bridge read <target> [lines]\n", stderr)
        exit(1)
    }
    let lines = args.count >= 4 ? (Int(args[3]) ?? 1000) : 1000
    readPane(target: args[2], lines: lines)

case "write":
    guard args.count >= 4 else {
        fputs("Usage: tmux-bridge write <target> <text> [--no-enter]\n", stderr)
        exit(1)
    }
    let sendEnter = !args.contains("--no-enter")
    let text = args[3..<args.count].filter { $0 != "--no-enter" }.joined(separator: " ")
    writePane(target: args[2], text: text, sendEnter: sendEnter)

case "snapshot":
    let session = args.count >= 3 && Int(args[2]) == nil ? args[2] : ""
    let lines = args.count >= 3 && Int(args[2]) != nil ? (Int(args[2]) ?? 5000) :
                args.count >= 4 ? (Int(args[3]) ?? 5000) : 5000
    snapshot(session: session, lines: lines)

default:
    fputs("Unknown command: \(command)\n", stderr)
    exit(1)
}
```

## File: `skills/apple-bridges/SKILL.md`
```markdown
---
name: apple-bridges
description: Use this skill whenever the user asks about Apple apps — Reminders, Calendar, Contacts, Notes, Mail, or tmux sessions. This includes creating/completing reminders, checking/adding calendar events, looking up contacts, reading/writing notes, sending/reading email, and capturing tmux session content. Also use this skill when the user mentions tasks, todos, scheduling, birthdays, free time slots, or end-of-day summaries. The bridges are CLI tools installed at ~/.claude/ that give Claude Code native access to these Apple apps on macOS.
---

# Apple Bridges

Swift CLI tools at `~/.claude/` that give Claude Code native access to Apple apps on macOS.

## Quick Reference

| Bridge | Binary | Purpose |
|--------|--------|---------|
| [reminders-bridge](reminders-bridge.md) | `~/.claude/reminders-bridge` | Manage Apple Reminders — lists, items, due dates, search |
| [calendar-bridge](calendar-bridge.md) | `~/.claude/calendar-bridge` | Read/write Apple Calendar — events, free slots, scheduling |
| [contacts-bridge](contacts-bridge.md) | `~/.claude/contacts-bridge` | Search/manage Apple Contacts — lookup, birthdays |
| [notes-bridge](notes-bridge.md) | `~/.claude/notes-bridge` | Read/write Apple Notes — create, search, append |
| [mail-bridge](mail-bridge.md) | `~/.claude/mail-bridge` | Read/send Apple Mail — inbox, unread, compose |
| [tmux-bridge](tmux-bridge.md) | `~/.claude/tmux-bridge` | Read/write tmux sessions — panes, snapshots, send keystrokes |

**Read the detail file for the bridge you need** — each contains full command syntax, all parameters, and usage examples.

## General Patterns

### CLI Syntax

All bridges follow the same pattern:

```bash
~/.claude/<bridge-name> <command> [arguments...]
```

### Quoting

Arguments with spaces must be quoted:

```bash
~/.claude/reminders-bridge add "Shopping List" "Buy milk" "From the organic store"
~/.claude/calendar-bridge add "Work" "Team Meeting" "2026-03-01 10:00" "2026-03-01 11:00"
```

### Destructive Operations

Delete commands use a **dry-run by default** pattern — they show what would be deleted without the `--force` flag:

```bash
# Dry run (safe preview)
~/.claude/reminders-bridge delete "Work" "Old task"

# Actually delete
~/.claude/reminders-bridge delete "Work" "Old task" --force
```

This applies to: `reminders-bridge delete`, `calendar-bridge delete`, `contacts-bridge delete`, `notes-bridge delete`, `mail-bridge delete`.

### Permissions

Each bridge requires macOS permission on first use:

| Bridge | Permission | Settings Path |
|--------|-----------|---------------|
| reminders-bridge | Reminders | Privacy & Security > Reminders |
| calendar-bridge | Calendars | Privacy & Security > Calendars |
| contacts-bridge | Contacts | Privacy & Security > Contacts |
| notes-bridge | Automation (Notes.app) | Privacy & Security > Automation |
| mail-bridge | Automation (Mail.app) | Privacy & Security > Automation |
| tmux-bridge | None (uses tmux CLI) | — |

### Allowed Tools Configuration

Add to `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(~/.claude/reminders-bridge:*)",
      "Bash(~/.claude/calendar-bridge:*)",
      "Bash(~/.claude/contacts-bridge:*)",
      "Bash(~/.claude/notes-bridge:*)",
      "Bash(~/.claude/mail-bridge:*)",
      "Bash(~/.claude/tmux-bridge:*)"
    ]
  }
}
```
```

## File: `skills/apple-bridges/calendar-bridge.md`
```markdown
# calendar-bridge

Read and write Apple Calendar events from Claude Code via EventKit.

**Binary:** `~/.claude/calendar-bridge`

## Commands

### calendars

List all calendars. Read-only calendars are marked.

```bash
~/.claude/calendar-bridge calendars
```

Output example:

```
Home
Work
Birthdays (read-only)
```

### today

Show today's events across all calendars.

```bash
~/.claude/calendar-bridge today
```

### tomorrow

Show tomorrow's events across all calendars.

```bash
~/.claude/calendar-bridge tomorrow
```

### week

Show all events for the current week (Monday through Sunday).

```bash
~/.claude/calendar-bridge week
```

### events

Show events for a specific date.

```bash
~/.claude/calendar-bridge events <YYYY-MM-DD>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `YYYY-MM-DD` | Yes | Date to show events for |

```bash
~/.claude/calendar-bridge events 2026-03-15
```

### free-slots

Show free time slots for a specific date. Working hours: 08:00-20:00, minimum slot: 30 minutes.

```bash
~/.claude/calendar-bridge free-slots <YYYY-MM-DD>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `YYYY-MM-DD` | Yes | Date to find free slots for |

```bash
~/.claude/calendar-bridge free-slots 2026-03-01
```

Output example:

```
Free slots on Sonntag, 01. März 2026:
  08:00 – 10:00  (120 min)
  11:30 – 13:00  (90 min)
  15:00 – 20:00  (300 min)
```

### search

Search events by title in the next 365 days.

```bash
~/.claude/calendar-bridge search <query>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `query` | Yes | Search term (case-insensitive, matches title) |

```bash
~/.claude/calendar-bridge search "standup"
```

### add

Add a timed event to a calendar.

```bash
~/.claude/calendar-bridge add <calendar> <title> <start> <end>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `calendar` | Yes | Calendar name (must not be read-only) |
| `title` | Yes | Event title |
| `start` | Yes | Start time in `YYYY-MM-DD HH:mm` format |
| `end` | Yes | End time in `YYYY-MM-DD HH:mm` format |

```bash
~/.claude/calendar-bridge add "Work" "Code Review" "2026-03-01 14:00" "2026-03-01 15:00"
```

### add-all-day

Add an all-day event to a calendar.

```bash
~/.claude/calendar-bridge add-all-day <calendar> <title> <YYYY-MM-DD>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `calendar` | Yes | Calendar name (must not be read-only) |
| `title` | Yes | Event title |
| `YYYY-MM-DD` | Yes | Date for the all-day event |

```bash
~/.claude/calendar-bridge add-all-day "Work" "Release Day" 2026-03-15
```

### delete

Delete an event. Dry-run by default — use `--force` to actually delete.

```bash
~/.claude/calendar-bridge delete <calendar> <title> <YYYY-MM-DD> [--force]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `calendar` | Yes | Calendar name |
| `title` | Yes | Event title (exact match) |
| `YYYY-MM-DD` | Yes | Date of the event |
| `--force` | No | Actually delete (without: dry-run preview) |

```bash
# Preview
~/.claude/calendar-bridge delete "Work" "Old Meeting" 2026-03-01

# Actually delete
~/.claude/calendar-bridge delete "Work" "Old Meeting" 2026-03-01 --force
```

## Output Format

Events are displayed as:

```
Events for Montag, 01. März 2026:
  [09:00 – 10:00] Team Standup @ Zoom  (Work)
  [All day] Release Day  (Work)
```

- Time range or "All day" in brackets
- Location shown with `@` if set
- Calendar name in parentheses

## Common Workflows

### Schedule work avoiding conflicts

```bash
# Check what's booked
~/.claude/calendar-bridge tomorrow

# Find free time
~/.claude/calendar-bridge free-slots 2026-03-01

# Book a slot
~/.claude/calendar-bridge add "Work" "Deep Work: MCP Server" "2026-03-01 14:00" "2026-03-01 16:00"
```

### Weekly planning

```bash
~/.claude/calendar-bridge week
```
```

## File: `skills/apple-bridges/contacts-bridge.md`
```markdown
# contacts-bridge

Search and manage Apple Contacts from Claude Code via the Contacts framework.

**Binary:** `~/.claude/contacts-bridge`

## Commands

### search

Search contacts by name, email, or phone.

```bash
~/.claude/contacts-bridge search <query>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `query` | Yes | Name to search for |

```bash
~/.claude/contacts-bridge search "Thomas"
```

Output shows name, organization, phone numbers, and email addresses.

### show

Show full details for a contact, including address, birthday, and notes.

```bash
~/.claude/contacts-bridge show <name>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `name` | Yes | Contact name to look up |

```bash
~/.claude/contacts-bridge show "Thomas Müller"
```

### add

Add a new contact.

```bash
~/.claude/contacts-bridge add <firstName> <lastName> [phone] [email]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `firstName` | Yes | First name |
| `lastName` | Yes | Last name |
| `phone` | No | Phone number (saved as mobile) |
| `email` | No | Email address (saved as work) |

```bash
# Name only
~/.claude/contacts-bridge add "Alex" "Schmidt"

# With phone and email
~/.claude/contacts-bridge add "Alex" "Schmidt" "+49 123 456789" "alex@example.com"
```

### update

Update a contact's phone or email.

```bash
~/.claude/contacts-bridge update <name> phone <value>
~/.claude/contacts-bridge update <name> email <value>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `name` | Yes | Contact name |
| `phone`/`email` | Yes | Field to update |
| `value` | Yes | New value |

```bash
~/.claude/contacts-bridge update "Alex Schmidt" phone "+49 987 654321"
~/.claude/contacts-bridge update "Alex Schmidt" email "alex.new@example.com"
```

**Note:** Update replaces the existing phone/email — it does not append.

### delete

Delete a contact. Dry-run by default — use `--force` to actually delete.

```bash
~/.claude/contacts-bridge delete <name> [--force]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `name` | Yes | Contact name |
| `--force` | No | Actually delete (without: dry-run preview) |

```bash
# Preview
~/.claude/contacts-bridge delete "Alex Schmidt"

# Actually delete
~/.claude/contacts-bridge delete "Alex Schmidt" --force
```

### birthdays-today

Show contacts with a birthday today.

```bash
~/.claude/contacts-bridge birthdays-today
```

### birthdays-upcoming

Show upcoming birthdays within the next N days.

```bash
~/.claude/contacts-bridge birthdays-upcoming <days>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `days` | Yes | Number of days to look ahead |

```bash
~/.claude/contacts-bridge birthdays-upcoming 30
```

Output example:

```
3 birthday(s) in the next 30 days:
  Tomorrow (5.3): Anna Müller
  In 12 days (17.3): Max Weber
  In 28 days (2.4): Lisa Schmidt
```

## Common Workflows

### Quick contact lookup

```bash
~/.claude/contacts-bridge search "Rob"
~/.claude/contacts-bridge show "Robert Johnson"
```

### Birthday check

```bash
~/.claude/contacts-bridge birthdays-today
~/.claude/contacts-bridge birthdays-upcoming 7
```
```

## File: `skills/apple-bridges/mail-bridge.md`
```markdown
# mail-bridge

Read and send Apple Mail messages from Claude Code via AppleScript.

**Binary:** `~/.claude/mail-bridge`

**Default mailbox:** `INBOX`

## Commands

### accounts

List all email accounts.

```bash
~/.claude/mail-bridge accounts
```

### mailboxes

List mailboxes for an account.

```bash
~/.claude/mail-bridge mailboxes [account]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `account` | No | Account name (default: first account) |

```bash
~/.claude/mail-bridge mailboxes
~/.claude/mail-bridge mailboxes "iCloud"
```

### list

List recent messages. Smart argument detection: if the second argument matches an account name, it's treated as the account (not a mailbox).

```bash
~/.claude/mail-bridge list [mailbox|account] [account] [count]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `mailbox` | No | Mailbox name (default: `INBOX`) |
| `account` | No | Account name (default: first account) |
| `count` | No | Number of messages to show (default: `20`) |

```bash
# Default: 20 most recent in INBOX
~/.claude/mail-bridge list

# Specific mailbox
~/.claude/mail-bridge list "Sent Messages"

# Account shortcut (auto-detected)
~/.claude/mail-bridge list "iCloud"

# Mailbox + account + count
~/.claude/mail-bridge list "INBOX" "iCloud" 50
```

Output format: `<index>. <subject> [UNREAD] — <sender> (<month>/<day>)`

### unread

List unread messages. Same smart argument detection as `list`.

```bash
~/.claude/mail-bridge unread [mailbox|account] [account]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `mailbox` | No | Mailbox name (default: `INBOX`) |
| `account` | No | Account name (default: first account) |

```bash
~/.claude/mail-bridge unread
~/.claude/mail-bridge unread "iCloud"
~/.claude/mail-bridge unread "INBOX" "iCloud"
```

### search

Search messages by subject and sender in INBOX.

```bash
~/.claude/mail-bridge search <query> [account]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `query` | Yes | Search term (matches subject and sender) |
| `account` | No | Account name (default: first account) |

```bash
~/.claude/mail-bridge search "invoice"
~/.claude/mail-bridge search "invoice" "iCloud"
```

### read

Read a message by its index number (from `list` output). Unread status is preserved by default.

```bash
~/.claude/mail-bridge read <index> [mailbox] [account] [--mark-read]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `index` | Yes | Message index (from `list` output) |
| `mailbox` | No | Mailbox name (default: `INBOX`) |
| `account` | No | Account name (default: first account) |
| `--mark-read` | No | Mark message as read after reading |

```bash
# Read without changing status
~/.claude/mail-bridge read 1

# Read and mark as read
~/.claude/mail-bridge read 3 --mark-read

# Specific mailbox
~/.claude/mail-bridge read 1 "Sent Messages" "iCloud"
```

### send

Compose and send an email. **Without `--force`**: opens a compose window in Mail.app for review. **With `--force`**: sends directly without UI.

```bash
~/.claude/mail-bridge send <to> <subject> <body> [/path/to/attachment] [--from <email>] [--force]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `to` | Yes | Recipient email address |
| `subject` | Yes | Email subject |
| `body` | Yes | Email body text |
| `/path/to/attachment` | No | Path to file attachment |
| `--from <email>` | No | Sender email address (default: first account's email) |
| `--force` | No | Send directly without opening compose window |

```bash
# Open compose window for review (recommended)
~/.claude/mail-bridge send "heiko@web.de" "Meeting Notes" "Hi Heiko, here are the notes..."

# Send directly (use with care)
~/.claude/mail-bridge send "heiko@web.de" "Meeting Notes" "Hi Heiko, here are the notes..." --force

# With attachment and specific sender
~/.claude/mail-bridge send "heiko@web.de" "Report" "See attached." /tmp/report.pdf --from work@company.com

# All options
~/.claude/mail-bridge send "heiko@web.de" "Report" "See attached." /tmp/report.pdf --from work@company.com --force
```

**Important:** Always prefer opening the compose window (without `--force`) unless the user explicitly asks to send directly.

### delete

Move a message to Trash. Dry-run by default — use `--force` to actually delete.

```bash
~/.claude/mail-bridge delete <index> [mailbox] [account] [--force]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `index` | Yes | Message index |
| `mailbox` | No | Mailbox name (default: `INBOX`) |
| `account` | No | Account name (default: first account) |
| `--force` | No | Actually move to Trash (without: dry-run preview) |

```bash
# Preview
~/.claude/mail-bridge delete 5

# Actually delete
~/.claude/mail-bridge delete 5 --force
```

## Common Workflows

### Check for new mail

```bash
~/.claude/mail-bridge unread
~/.claude/mail-bridge read 1
```

### Draft a reply

```bash
# Read the original message
~/.claude/mail-bridge read 3 --mark-read

# Compose a reply (opens in Mail.app for review)
~/.claude/mail-bridge send "sender@example.com" "Re: Original Subject" "Thanks for your message..."
```

### Search and read

```bash
~/.claude/mail-bridge search "quarterly report"
~/.claude/mail-bridge read 1
```
```

## File: `skills/apple-bridges/notes-bridge.md`
```markdown
# notes-bridge

Read and write Apple Notes from Claude Code via AppleScript.

**Binary:** `~/.claude/notes-bridge`

**Default account:** `iCloud`
**Default folder:** `Notes`

## Commands

### accounts

List all Notes accounts.

```bash
~/.claude/notes-bridge accounts
```

### folders

List folders in an account.

```bash
~/.claude/notes-bridge folders [account]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `account` | No | Account name (default: `iCloud`) |

```bash
~/.claude/notes-bridge folders
~/.claude/notes-bridge folders "Gmail"
```

### list

List notes in a folder with modification dates.

```bash
~/.claude/notes-bridge list [folder] [account]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `folder` | No | Folder name (default: `Notes`) |
| `account` | No | Account name (default: `iCloud`) |

```bash
~/.claude/notes-bridge list
~/.claude/notes-bridge list "Work"
~/.claude/notes-bridge list "Work" "iCloud"
```

Output example:

```
Meeting Notes  [2026-03-01]
Project Ideas  [2026-02-28]
```

### search

Search notes by title and content across all accounts.

```bash
~/.claude/notes-bridge search <query>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `query` | Yes | Search term (matches title and body) |

```bash
~/.claude/notes-bridge search "architecture"
```

### read

Read a note's content as plain text (HTML stripped).

```bash
~/.claude/notes-bridge read <title> [account]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `title` | Yes | Exact note title |
| `account` | No | Account name (default: searches all accounts) |

```bash
~/.claude/notes-bridge read "Meeting Notes"
~/.claude/notes-bridge read "Meeting Notes" "iCloud"
```

### add

Create a new note. Supports HTML formatting.

```bash
~/.claude/notes-bridge add <folder> <title> <body> [account]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `folder` | Yes | Target folder |
| `title` | Yes | Note title |
| `body` | Yes | Note body (plain text or HTML) |
| `account` | No | Account name (default: `iCloud`) |

```bash
# Plain text
~/.claude/notes-bridge add "Notes" "Shopping" "Milk, Bread, Eggs"

# HTML formatted
~/.claude/notes-bridge add "Work" "Meeting Notes" "<b>Attendees:</b> Tobias, Heiko<br><br><ul><li>Discussed roadmap</li><li>Next: review PR</li></ul>"
```

**Supported HTML tags:** `<b>`, `<i>`, `<u>`, `<br>`, `<ul>`, `<ol>`, `<li>`, `<h1>`-`<h3>`, `<a href="...">`, `<p>`

### append

Append text to an existing note. Supports HTML.

```bash
~/.claude/notes-bridge append <title> <text> [account]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `title` | Yes | Exact note title |
| `text` | Yes | Text to append (plain or HTML) |
| `account` | No | Account name (default: searches all accounts) |

```bash
~/.claude/notes-bridge append "Meeting Notes" "Follow-up: send report by Friday"
~/.claude/notes-bridge append "Meeting Notes" "<br><b>Update:</b> deadline extended to Monday"
```

### delete

Delete a note. Dry-run by default — use `--force` to actually delete.

```bash
~/.claude/notes-bridge delete <title> [--force] [account]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `title` | Yes | Exact note title |
| `--force` | No | Actually delete (without: dry-run preview) |
| `account` | No | Account name (default: searches all accounts) |

```bash
# Preview
~/.claude/notes-bridge delete "Old Note"

# Actually delete
~/.claude/notes-bridge delete "Old Note" --force
```

## Common Workflows

### Session notes

```bash
# Create a note for today's session
~/.claude/notes-bridge add "Work" "Dev Session 2026-03-01" "<b>Goal:</b> Implement MCP server<br><ul><li>Created SKILL.md</li><li>Updated README</li></ul>"

# Append as work progresses
~/.claude/notes-bridge append "Dev Session 2026-03-01" "<br><b>Completed:</b> All skill files created and tested"
```

### Search and read

```bash
~/.claude/notes-bridge search "MCP"
~/.claude/notes-bridge read "MCP Server Design"
```
```

## File: `skills/apple-bridges/reminders-bridge.md`
```markdown
# reminders-bridge

Manage Apple Reminders from Claude Code via EventKit.

**Binary:** `~/.claude/reminders-bridge`

## Commands

### lists

List all reminder lists.

```bash
~/.claude/reminders-bridge lists
```

### create-list

Create a new reminder list.

```bash
~/.claude/reminders-bridge create-list <listName>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `listName` | Yes | Name for the new list |

```bash
~/.claude/reminders-bridge create-list "Project Ideas"
```

### items

Show all reminders in a list (completed and incomplete).

```bash
~/.claude/reminders-bridge items <listName>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `listName` | Yes | Name of the reminder list |

### incomplete

Show only incomplete reminders in a list.

```bash
~/.claude/reminders-bridge incomplete <listName>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `listName` | Yes | Name of the reminder list |

### today

Show reminders due today across all lists.

```bash
~/.claude/reminders-bridge today
```

### overdue

Show all overdue reminders across all lists.

```bash
~/.claude/reminders-bridge overdue
```

### search

Search reminders by title and notes across all lists.

```bash
~/.claude/reminders-bridge search <query>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `query` | Yes | Search term (case-insensitive, matches title and notes) |

```bash
~/.claude/reminders-bridge search "PR review"
```

### add

Add a new reminder to a list.

```bash
~/.claude/reminders-bridge add <listName> <title> [notes]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `listName` | Yes | Target reminder list |
| `title` | Yes | Reminder title |
| `notes` | No | Additional notes |

```bash
# Without notes
~/.claude/reminders-bridge add "Work" "Review PR #42"

# With notes
~/.claude/reminders-bridge add "Work" "Review PR #42" "Focus on auth changes in src/login.swift"
```

### set-due

Set or update the due date of a reminder.

```bash
~/.claude/reminders-bridge set-due <listName> <title> <datetime>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `listName` | Yes | Reminder list name |
| `title` | Yes | Reminder title (must be incomplete) |
| `datetime` | Yes | Due date in `YYYY-MM-DD HH:mm` format |

```bash
~/.claude/reminders-bridge set-due "Work" "Review PR #42" "2026-03-01 09:00"
```

### set-notes

Set or update the notes of a reminder.

```bash
~/.claude/reminders-bridge set-notes <listName> <title> <notes>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `listName` | Yes | Reminder list name |
| `title` | Yes | Reminder title (must be incomplete) |
| `notes` | Yes | New notes content |

```bash
~/.claude/reminders-bridge set-notes "Work" "Review PR #42" "Updated: also check the migration script"
```

### complete

Mark a reminder as complete.

```bash
~/.claude/reminders-bridge complete <listName> <title>
```

| Argument | Required | Description |
|----------|----------|-------------|
| `listName` | Yes | Reminder list name |
| `title` | Yes | Reminder title (must be incomplete) |

```bash
~/.claude/reminders-bridge complete "Work" "Review PR #42"
```

### delete

Delete a reminder. Dry-run by default — use `--force` to actually delete.

```bash
~/.claude/reminders-bridge delete <listName> <title> [--force]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `listName` | Yes | Reminder list name |
| `title` | Yes | Reminder title |
| `--force` | No | Actually delete (without: dry-run preview) |

```bash
# Preview what would be deleted
~/.claude/reminders-bridge delete "Work" "Old task"

# Actually delete
~/.claude/reminders-bridge delete "Work" "Old task" --force
```

## Output Format

Reminders are displayed as:

```
[x] Buy groceries! (due: 01.03.26, 09:00) [repeats: weekly] [Shopping]
     Notes: Organic milk and sourdough bread
```

- `[x]` = completed, `[ ]` = incomplete
- `!!` = high priority, `!` = medium priority
- Due date shown if set
- Recurrence shown if set
- List name in brackets
- Notes on next line if present

## Common Workflows

### Track a coding task

```bash
~/.claude/reminders-bridge add "4later" "Implement MCP server" "GitHub issue #15, feature/mcp-server branch"
~/.claude/reminders-bridge set-due "4later" "Implement MCP server" "2026-03-05 10:00"
```

### Check what's due and overdue

```bash
~/.claude/reminders-bridge today
~/.claude/reminders-bridge overdue
```

### Complete a task after finishing work

```bash
~/.claude/reminders-bridge complete "4later" "Implement MCP server"
```
```

## File: `skills/apple-bridges/tmux-bridge.md`
```markdown
# tmux-bridge

Read and write tmux session contents from Claude Code. Great for end-of-day summaries, capturing terminal output, and interactive terminal control.

**Binary:** `~/.claude/tmux-bridge`

**Requires:** tmux installed and running (`brew install tmux`)

## Commands

### sessions

List all running tmux sessions.

```bash
~/.claude/tmux-bridge sessions
```

Output example:

```
Sessions (2):
  main  windows:3  created:Thu Feb 27 10:00:00 2026  (attached)
  server  windows:1  created:Thu Feb 27 09:00:00 2026
```

### windows

List windows in a session.

```bash
~/.claude/tmux-bridge windows [session]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `session` | No | Session name (default: current session) |

```bash
~/.claude/tmux-bridge windows
~/.claude/tmux-bridge windows "main"
```

Output example:

```
Windows in session 'main':
  0: zsh  [200x50]  1 pane(s) (active)
  1: vim  [200x50]  2 pane(s)
  2: logs  [200x50]  1 pane(s)
```

### panes

List all panes with path and current command.

```bash
~/.claude/tmux-bridge panes [session]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `session` | No | Session name (default: all sessions) |

```bash
~/.claude/tmux-bridge panes
~/.claude/tmux-bridge panes "main"
```

Output example:

```
Panes (4):
  main:0.0  [200x50]  zsh  /Users/tobias/project
  main:1.0  [100x50]  vim  /Users/tobias/project
  main:1.1  [100x50]  zsh  /Users/tobias/project
  main:2.0  [200x50]  tail  /var/log
```

### read

Read content from a specific pane.

```bash
~/.claude/tmux-bridge read <target> [lines]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `target` | Yes | Pane target in `session:window.pane` format (e.g., `main:0.0`) |
| `lines` | No | Number of lines to capture (default: `1000`) |

```bash
~/.claude/tmux-bridge read "main:0.0"
~/.claude/tmux-bridge read "main:1.1" 500
```

**Target format:** `session:window.pane` — use `panes` command to see available targets.

### write

Send keystrokes to a specific pane.

```bash
~/.claude/tmux-bridge write <target> <text> [--no-enter]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `target` | Yes | Pane target in `session:window.pane` format (e.g., `main:0.0`) |
| `text` | Yes | Text to send to the pane |
| `--no-enter` | No | Send text without pressing Enter |

```bash
# Send a command (text + Enter)
~/.claude/tmux-bridge write "main:0.0" "ls -la"

# Send text without pressing Enter
~/.claude/tmux-bridge write "main:0.0" "partial input" --no-enter
```

**Use cases:** Running `sudo` commands, interactive terminal operations, system administration tasks from Claude Code sessions.

### snapshot

Capture all panes at once. Ideal for end-of-day summaries.

```bash
~/.claude/tmux-bridge snapshot [session] [lines]
```

| Argument | Required | Description |
|----------|----------|-------------|
| `session` | No | Session name (default: all sessions) |
| `lines` | No | Lines per pane to capture (default: `5000`) |

```bash
# All sessions
~/.claude/tmux-bridge snapshot

# Specific session
~/.claude/tmux-bridge snapshot "main"

# With custom line count
~/.claude/tmux-bridge snapshot "main" 2000
```

Output format:

```
=== tmux snapshot: session 'main' ===
Captured: 2026-02-27 18:00:00 +0000

-------------------------------------
Pane: main:0.0  [zsh] zsh @ /Users/tobias/project
-------------------------------------
<pane content>

-------------------------------------
Pane: main:1.0  [vim] vim @ /Users/tobias/project
-------------------------------------
<pane content>
```

## Common Workflows

### End-of-day summary

```bash
~/.claude/tmux-bridge snapshot
```

Then ask Claude: "Summarize what I worked on today based on this tmux snapshot."

### Check a specific terminal

```bash
~/.claude/tmux-bridge panes
~/.claude/tmux-bridge read "main:2.0"
```

### Monitor logs

```bash
~/.claude/tmux-bridge read "server:0.0" 200
```
```


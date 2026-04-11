# Knowledge Dump for claude-apple-bridges

## File: claude.md
```
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

## File: README.md
```
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

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_claude-apple-bridges_133133



================================================
FILE: CLAUDE.md
================================================
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


================================================
FILE: README.md
================================================
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
calendar-bridge add <cal> <title> <start> <end> 

================================================
FILE: skills\apple-bridges\calendar-bridge.md
================================================
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


================================================
FILE: skills\apple-bridges\contacts-bridge.md
================================================
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


================================================
FILE: skills\apple-bridges\mail-bridge.md
================================================
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
~/.claude/mail-bridge unr

================================================
FILE: skills\apple-bridges\notes-bridge.md
================================================
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


================================================
FILE: skills\apple-bridges\reminders-bridge.md
================================================
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


================================================
FILE: skills\apple-bridges\SKILL.md
================================================
---
name: apple-bridges
description: Use this skill whenever the user asks about Apple apps — Reminders, Calendar, Contacts, Notes, Mail, or tmux sessions. This includes creating/completing reminders, checking/adding calendar events, looking up contacts, reading/writing notes, sending/reading email, and capturing tmux session content. Also use this skill when the user mentions tasks, todos, scheduling, birthdays, free time slots, or end-of-day summaries. The bridges are CLI tools installed at ~/.claude/ that give Claude Code native access to these Apple apps on macOS.
---

# Apple Bridges

Swift CLI tools at `~/.claude/` that give Claude Code native access to Apple apps on macOS.

## Quick Reference

| Bridge | Binary | Purpose |
|--------|--------|---------|

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


================================================
FILE: skills\apple-bridges\tmux-bridge.md
================================================
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


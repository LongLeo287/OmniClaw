---
id: claude-apple-bridges-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:02.375506
---

# OmniClaw Knowledge Report: claude-apple-bridges

## Tech Stack
Unknown

## File Statistics
```json
{
  "": 3,
  ".swift": 6,
  ".md": 9,
  ".sh": 1
}
```

## README Snippet
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

Claude reads your calendar for each day
```

**Processed by OmniClaw Automated Intake**
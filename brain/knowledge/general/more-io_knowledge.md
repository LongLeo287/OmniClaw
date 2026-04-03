---
id: more-io-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:09.732778
---

# KNOWLEDGE EXTRACT: more-io
> **Extracted on:** 2026-03-30 17:43:02
> **Source:** more-io

---

## File: `claude-apple-bridges.md`
```markdown
# 📦 more-io/claude-apple-bridges [🔖 PENDING/APPROVE]
🔗 https://github.com/more-io/claude-apple-bridges
🌐 https://github.com/more-io/claude-apple-bridges

## Meta
- **Stars:** ⭐ 4 | **Forks:** 🍴 0
- **Language:** Swift | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Swift CLI bridges giving Claude Code native access to Apple Reminders, Calendar, Contacts, Notes, Mail and tmux — includes Claude Code skill with full command reference

## README (trích đầu)
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

> *"Set reminders for all open todos so they show up in my Calendar tomorrow after my m
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


---
id: tkattkat-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.472814
---

# KNOWLEDGE EXTRACT: tkattkat
> **Extracted on:** 2026-03-30 17:54:18
> **Source:** tkattkat

---

## File: `open-claude.md`
```markdown
# 📦 tkattkat/open-claude [🔖 PENDING/APPROVE]
🔗 https://github.com/tkattkat/open-claude


## Meta
- **Stars:** ⭐ 138 | **Forks:** 🍴 34
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# Open Claude

A native macOS desktop client for Claude with a clean, minimal interface and system-wide quick access.

## Disclaimer

This project is an independent, open-source research and educational project. It is not affiliated with, endorsed by, or sponsored by Anthropic. "Claude" is a trademark of Anthropic, PBC.

This client requires a valid claude.ai account and authenticates through the official web login. It does not bypass any authentication or access controls. Usage is subject to Anthropic's [Terms of Service](https://www.anthropic.com/legal/consumer-terms) and [Acceptable Use Policy](https://www.anthropic.com/legal/aup).

This software is provided "as is" for educational and personal productivity purposes. The authors make no warranties and assume no liability for its use.

<img width="2226" height="1866" alt="Main Interface" src="https://github.com/user-attachments/assets/7c36f018-2659-4eff-805f-eedee1491c87" />

## Features

### Native macOS Experience
- Transparent window with vibrancy effects (under-window blur)
- Native traffic light controls with custom positioning
- System font rendering with SF Pro Display
- Dark mode support

### Spotlight Search
Press `Cmd+Shift+C` from anywhere to open a floating Spotlight-style search bar. Ask quick questions without leaving your current workflow.

- Always-on-top floating window
- Closes automatically when clicking outside
- Uses Claude Haiku for fast responses
- Maintains conversation context within a session
- Auto-resizes based on response length

<img width="1990" height="758" alt="Spotlight" src="https://github.com/user-attachments/assets/540ddc9c-1eee-4801-a96a-78d28a7bc0f3" />

### Conversation Management
- Create, rename, and delete conversations
- Star important conversations
- Auto-generated titles based on conversation content
- Conversation history with timestamps

### Streaming Responses
- Real-time streaming text display
- Extended thinking support with collapsible summaries
- Tool use visualization
- Stop generation at any time

### Model Support
- Claude Opus 4.5 (default for main chat)
- Claude Haiku 4.5 (Spotlight quick queries)

## Installation

### Pre-built Releases
Download the latest DMG for your architecture:
- `Open Claude-x.x.x-arm64.dmg` - Apple Silicon (M1/M2/M3)
- `Open Claude-x.x.x.dmg` - Intel

### Build from Source

```bash
# Clone the repository
git clone https://github.com/tkattkat/open-claude.git
cd open-claude

# Install dependencies
pnpm install

# Development
pnpm dev

# Build from source to desktop app
pnpm dist
```

## Authentication

Open Claude uses your existing claude.ai account. Click "Sign in with Claude" to authenticate through the standard web login flow. Your session is stored securely using electron-store.

## Screenshots

### Login
<img width="2166" height="1512" alt="Login" src="https://github.com/user-attachments/assets/1281ad7a-e3f9-4b7f-ad06-90b005175ab1" />

### Conversation View
<img width="2020" height="1578" alt="Conversation" s
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


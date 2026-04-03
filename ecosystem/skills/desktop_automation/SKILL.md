---
name: desktop_automation
description: Control the Local Computer Interface (Computer Use).
---

# Desktop Automation Skill
**Origin:** Extracted from the Awesome-Agent-Skills repository (PyAutoGUI / Computer-Use API).

## Description
Instead of working through static APIs or the Terminal, an Agent can "see" the Operating System's screen, locate icons (Pixel Match), move the mouse, and type keystrokes like a human.

## Usage
- Agents in the `ui-ux-agent` or `qa-tester` group invoke this skill to launch applications, press buttons X, Y, Z to verify graphical flows (e.g., testing Unity, Unreal, Android Emulator apps).
- Uses the `pyautogui` or `playwright` modules.

## Restrictions
1. **Boss Approval:** Any automated mouse/keyboard action must enable "Step-by-step confirmation" mode if exceeding 10 clicks.
2. Do not open high-level system folders (e.g., Windows Boot / System32).

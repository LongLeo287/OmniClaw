---
description: Handoff Execution to Claude Code CLI (OmniClaw)
---

# Workflow: Handoff to OmniClaw Coder

Use this workflow when Antigravity (or any active agent) needs to delegate
execution authority (Handoff) to the OmniClaw system — specifically the
Claude Code CLI — to conserve Quota or leverage the more powerful
`omniclaw-coder` network.

## Trigger Conditions

1. When a request involves creating or modifying a large volume of code.
2. When Antigravity's (Gemini) quota is running low.
3. When the User (CEO) explicitly commands: "Send that task to OmniClaw" or "Handoff to Claude Code".

## Steps

### Step 1 — Prepare the prompt for Claude Code CLI
- Read the agreed request or Plan confirmed with the user.
- Compress it into a single, self-contained command (One-shot Prompt).
  - Example: `"Implement the login form using React and Tailwind based on the PRD in docs/"`

### Step 2 — Execute the Handoff to Claude Code

// turbo
1. Use the `run_command` tool to open a Terminal.
2. Invoke the `claude` CLI with the `-p` (prompt) flag containing the task description.
3. Ensure the `claude` CLI in the User's IDE is already configured to point to
   `http://127.0.0.1:8080/v1` with the model name `omniclaw-coder`.
   (This is set up manually by the User.)

```bash
# Example handoff command:
claude -p "Based on the plan in PLAN.md, create the corresponding React components using TailwindCSS styling."
```

### Step 3 — Monitor and Accept Results
- Wait for Claude Code (running via OmniClaw Router) to finish on the Terminal.
- Report the completion result back to the User (CEO).

## Security Notes

- Antigravity **MUST NEVER** call Port 8080 directly via API — this risks triggering
  Google's monitoring systems and may result in a silent account ban.
- ALL communication with local models must be routed through the Terminal (CLI) layer only.

---
id: claude-openclaw-bridge-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:04.878726
---

# KNOWLEDGE EXTRACT: claude-openclaw-bridge
> **Extracted on:** 2026-03-30 17:32:59
> **Source:** claude-openclaw-bridge

---

## File: `.envrc.example`
```
export OPENCLAW_BASE_URL=http://127.0.0.1:18789/v1
export OPENCLAW_MODEL="openclaw:main"
export OPENCLAW_API_KEY=your_key_here
export OPENCLAW_ASSISTANT_NAME="Claudette"
```

## File: `Makefile`
```
SKILL_DIR := $(HOME)/.claude/skills/openclaw-bridge

.PHONY: install uninstall

install:
	@mkdir -p $(SKILL_DIR)
	@cp SKILL.md $(SKILL_DIR)/SKILL.md
	@echo "Installed openclaw-bridge skill to $(SKILL_DIR)"

uninstall:
	@rm -rf $(SKILL_DIR)
	@echo "Removed openclaw-bridge skill from $(SKILL_DIR)"
```

## File: `README.md`
```markdown
# claude-openclaw-bridge

A Claude Code skill that bridges to an OpenClaw agent via its OpenAI-compatible API.

## What it does

Relays user requests to a remote OpenClaw instance and returns responses verbatim. Any capabilities, skills, or tools available on the OpenClaw agent become accessible from within Claude Code.

## Triggers

- "Ask OpenClaw ..."
- "OpenClaw mode on" / "OpenClaw mode off" (relay mode toggle)
- `/openclaw-bridge`

## Environment Variables

| Variable | Required | Example |
|----------|----------|---------|
| `OPENCLAW_BASE_URL` | yes | `http://127.0.0.1:18789/v1` |
| `OPENCLAW_MODEL` | yes | `openclaw:main` |
| `OPENCLAW_API_KEY` | yes | `sk-your-key` |
| `OPENCLAW_ASSISTANT_NAME` | no | `YOUR_ASSISTANT_NAME` (defaults to `OpenClaw`) |

Set these in your shell profile or `.env` before launching Claude Code.

## Installation

```bash
make install
```

This copies `SKILL.md` to `~/.claude/skills/openclaw-bridge/`.

To remove:

```bash
make uninstall
```

## Relay Mode

Say "OpenClaw mode on" to enter relay mode -- all subsequent messages are forwarded to the OpenClaw agent automatically. Say "OpenClaw mode off" to return to normal Claude Code behavior. This is session-scoped and does not persist.

## Enabling OpenAI-Compatible Endpoints

The bridge communicates with OpenClaw using the **OpenAI Chat Completions API** format. Any OpenClaw instance that exposes an OpenAI-compatible `/v1/chat/completions` endpoint will work.

### What the bridge expects

- **POST** `${OPENCLAW_BASE_URL}/chat/completions`
- Standard request body: `{ "model": "<model>", "messages": [{ "role": "user", "content": "..." }] }`
- Bearer token authentication via `Authorization: Bearer ${OPENCLAW_API_KEY}`
- Standard response: `{ "choices": [{ "message": { "content": "..." } }] }`

### Configuring your OpenClaw instance

1. **Enable the OpenAI-compatible server** in your OpenClaw configuration. The exact steps depend on your OpenClaw version, but generally you need to start the API server with an OpenAI-compatible endpoint enabled (commonly on a local port like `18789`).
2. **Set a model identifier** that your OpenClaw instance recognizes (e.g. `openclaw:main`).
3. **Generate or configure an API key** for authentication. Even for local-only access, an API key is recommended.
4. **Verify the endpoint** is reachable:

```bash
curl -s "${OPENCLAW_BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${OPENCLAW_API_KEY}" \
  -d '{"model": "'"${OPENCLAW_MODEL}"'", "messages": [{"role": "user", "content": "hello"}]}' \
  | jq .choices[0].message.content
```

If you get a response, the bridge is ready to use.

## Security Considerations

OpenClaw is often sandboxed and isolated from your main environment, and may have access to sensitive or personal data that you would not normally expose to Claude Code. The bridge creates a path between these two worlds, so it is important to be deliberate about when and how it is active.

### 1. Scope environment variables with `direnv`

If you only want the bridge available in certain project directories (rather than globally in every shell session), use [direnv](https://direnv.net/) to scope the environment variables:

1. Create a `.envrc` file in a trusted top-level directory (an example is provided in `.envrc.example`):

   ```bash
   export OPENCLAW_BASE_URL=http://127.0.0.1:18789/v1
   export OPENCLAW_MODEL="openclaw:main"
   export OPENCLAW_API_KEY=your_key_here
   ```

2. Run `direnv allow` in that directory to activate it. The variables will only be loaded when you `cd` into that directory tree, and will be unloaded when you leave.

This prevents the `OPENCLAW_API_KEY` and other credentials from being globally present in every terminal session, limiting the attack surface to directories you have explicitly approved.

### 2. Be intentional with the relay mode toggle

Relay mode (`OpenClaw mode on` / `OpenClaw mode off`) forwards **all** your messages to the OpenClaw agent for the duration of the session. This is convenient but easy to forget about:

- Turn relay mode **off** when you no longer need it.
- Remember that relay mode is session-scoped -- it does not persist across sessions, but it remains active for the entire current session if not explicitly turned off.
- Be mindful of what you type while relay mode is active. Anything that is not clearly a Claude Code command will be sent to OpenClaw.

### 3. Take extra care with `/remote-control` sessions

Claude Code's `/remote-control` feature allows external control of your session, which when combined with the OpenClaw bridge becomes especially powerful -- an external process can now interact with your OpenClaw instance through the remote session. This also means:

- **Always turn off the remote control session when you are done.** Do not leave it open for extended periods.
- A remote session with the bridge enabled effectively gives the remote controller access to anything OpenClaw can reach, which may include personal data and other information managed by your OpenClaw agent.
- Treat an open remote-control session with the bridge enabled as a privileged access point and close it promptly.

## Design

- Single-turn relay only -- OpenClaw manages its own conversation history
- No system prompt injected -- OpenClaw has its own persona
- Responses displayed verbatim, no summarization/e
```

## File: `SKILL.md`
```markdown
---
name: openclaw-bridge
description: >-
  Bridge to an OpenClaw agent. Use when user says "Ask OpenClaw",
  "OpenClaw mode on/off", or wants to relay a question or task to the
  OpenClaw agent. Any capabilities, skills, or tools available on the
  OpenClaw agent become accessible from within Claude Code. Also supports relay mode:
  when the user says "OpenClaw mode on", ALL subsequent messages should
  be relayed to OpenClaw until the user says "OpenClaw mode off".
version: 1.0.0
author: ericblue
allowed-tools: Bash(curl:*) Bash(echo:*) Read
---

# OpenClaw Bridge

Relay the user's request to the OpenClaw agent via its OpenAI-compatible API and return the response verbatim.

## Required Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENCLAW_BASE_URL` | yes | Base URL for the OpenClaw API (e.g. `http://127.0.0.1:18789/v1`) |
| `OPENCLAW_MODEL` | yes | Model identifier (e.g. `openclaw:main`) |
| `OPENCLAW_API_KEY` | yes | API key for authentication |
| `OPENCLAW_ASSISTANT_NAME` | no | Display name for the assistant (defaults to `OpenClaw`) |

## Instructions

Follow these steps exactly:

### 1. Validate environment variables

Run a single bash command to check that the three required env vars are set:

```bash
echo "BASE_URL=${OPENCLAW_BASE_URL:-MISSING} MODEL=${OPENCLAW_MODEL:-MISSING} API_KEY=${OPENCLAW_API_KEY:+SET}"
```

If any required variable is `MISSING` or the API key is empty, stop and tell the user which variables need to be set. Do not proceed.

### 2. Determine the assistant display name

Use `$OPENCLAW_ASSISTANT_NAME` if set, otherwise default to `OpenClaw`.

### 3. Extract the user's question

Take the user's message. If it starts with a trigger phrase like "Ask OpenClaw" or similar, strip that prefix to get the actual question. If the message is just the trigger with no question, ask the user what they'd like to ask.

### 4. Send the request

Use curl to POST to the chat completions endpoint. Do NOT inject a system prompt -- the OpenClaw agent has its own.

```bash
curl -sS -w "\n%{http_code}" \
  "${OPENCLAW_BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${OPENCLAW_API_KEY}" \
  -d '{
    "model": "'"${OPENCLAW_MODEL}"'",
    "messages": [
      {"role": "user", "content": "USER_QUESTION_HERE"}
    ]
  }' 2>&1
```

Replace `USER_QUESTION_HERE` with the actual user question (properly JSON-escaped).

### 5. Handle errors

Check the HTTP status code (last line of output from `-w "\n%{http_code}"`):

- **Connection refused / curl error**: Tell the user the OpenClaw agent is not reachable at the configured URL. Suggest checking that the service is running.
- **401 or 403**: Tell the user the API key was rejected. Suggest checking `OPENCLAW_API_KEY`.
- **404**: Tell the user the endpoint was not found. Suggest checking `OPENCLAW_BASE_URL`.
- **500+**: Tell the user the OpenClaw agent returned a server error. Include the status code.
- **Malformed JSON**: Tell the user the response was not valid JSON. Show the raw response for debugging.

### 6. Display the response

On success (HTTP 200), extract `.choices[0].message.content` from the JSON response. Display it verbatim, prefixed with the assistant name in bold:

```
**[<assistant name>]:** <response content here>
```

Do NOT summarize, reformat, or editorialize the response. Show it exactly as returned.

## Relay Mode (Session Toggle)

The user can toggle **relay mode** on and off during a session:

- **"OpenClaw mode on"** (or "relay mode on"): Activates relay mode. From this point, **every message** the user sends should be relayed to the OpenClaw agent using the steps above (steps 1-6). No need for the user to say "Ask OpenClaw" each time. Confirm activation with:
  ```
  **[OpenClaw relay mode: ON]** -- All messages will be forwarded to <assistant name>. Say "OpenClaw mode off" to stop.
  ```

- **"OpenClaw mode off"** (or "relay mode off"): Deactivates relay mode. Return to normal Claude Code behavior. Confirm with:
  ```
  **[OpenClaw relay mode: OFF]** -- Returning to normal mode.
  ```

- This toggle is **session-scoped only** -- it does not persist across sessions.
- While relay mode is active, if the user says something clearly directed at Claude Code itself (e.g., "read this file", "edit this code", "git status"), use your judgment -- those should NOT be relayed. Only relay messages that are questions or tasks for the OpenClaw agent.

## Important

- No system prompt is injected -- OpenClaw manages its own persona and context.
- No multi-turn state is maintained here -- OpenClaw manages its own conversation history.
- The response is displayed verbatim with no summarization.
```


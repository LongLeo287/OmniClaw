---
id: dependabot-secretary
name: dependabot-secretary
version: 1.0.0
tier: 1
status: active
author: omniclaw core team
updated: 2026-04-02
description: Manages and instructs other agents to yield merging permissions to GitHub's automated bot.
---

# 🤖 dependabot secretary (auto-merge handler)

## 📌 skill overview
This is a "background agent". It is actually a GitHub action at the cloud layer (`.github/workflows/ai-os-dependabot-merger.yml`). Its sole function is to auto-approve and auto-merge pull requests created by `dependabot[bot]`.

## ⚙️ zero-trust working mechanism
Instead of full trust, this secretary is limited by `rule-version-02`:

1.  **Approve minor/patch security vulnerabilities:** If library x jumps from `v1.2.0` to `v1.2.1` to patch a vulnerability (e.g., picomatch error) -> activate automatic merging rights.
2.  **Approve vulnerabilities from independent external platforms:** Libraries in `dependencies` or `deps-dev` (test) do not crash the main core.
3.  **Deny the core major bumps:** If dependabot requests to push version `v1.2` directly to a major version `v2.0.0` (causing API compatibility breaks) -> refuse to run! Let the CEO review manually.

## 🤝 collaborator agent instructions
If you are an AI agent (e.g., `nova`, `antigravity`, `claude code`), and you see that the libraries on the local repo are a different version than on the cloud:

1.  You are strictly **not allowed to manually upgrade** vulnerable components using `pip upgrade` or `npm upgrade` in the conversation.
2.  Instead, rest assured that dependabot will scan, and **dependabot secretary will automatically handle it on the cloud**. You should only focus on the code logic of the function assigned by the CEO.
3.  In the case the CEO gives a specific command: "you, upgrade x to version y for me". Only then are you allowed to code in the version.

***Note: This skill is a form of identity card that limits responsibility.***

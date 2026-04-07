---
id: clawdbot
type: knowledge
owner: OA_Triage
---
# clawdbot
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "openclaw",
  "version": "2026.4.4",
  "description": "Multi-channel AI gateway with extensible messaging integrations",
  "keywords": [],
  "homepage": "https://github.com/openclaw/openclaw#readme",
  "bugs": {
    "url": "https://github.com/openclaw/openclaw/issues"
  },
  "license": "MIT",
  "author": "",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/openclaw/openclaw.git"
  },
  "bin": {
    "openclaw": "openclaw.mjs"
  },
  "directories": {
    "doc": "docs",
    "test": "test"
  },
  "files": [
    "CHANGELOG.md",
    "LICENSE",
    "openclaw.mjs",
    "README.md",
    "assets/",
    "dist/",
    "!dist/**/*.map",
    "docs/",
    "!docs/.generated/**",
    "!docs/.i18n/zh-CN.tm.jsonl",
    "skills/",
    "scripts/npm-runner.mjs",
    "scripts/postinstall-bundled-plugins.mjs"
  ],
  "type": "module",
  "main": "dist/index.js",
  "exports": {
    ".": "./dist/index.js",
    "./plugin-sdk": {
      "types": "./dist/plugin-sdk/index.d.ts",
      "default": "./dist/plugin-sdk/index.js"
    },
    "./plugin-sdk/core": {
      "types": "./dist/plugin-sdk/core.d.ts",
      "default": "./dist/plugin-sdk/core.js"
    },
    "./plugin-sdk/provider-setup": {
      "types": "./dist/plugin-sdk/provider-setup.d.ts",
      "default": "./dist/plugin-sdk/provider-setup.js"
    },
    "./plugin-sdk/sandbox": {
      "types": "./dist/plugin-sdk/sandbox.d.ts",
      "default": "./dist/plugin-sdk/sandbox.js"
    },
    "./plugin-sdk/self-hosted-provider-setup": {
      "types": "./dist/plugin-sdk/self-hosted-provider-setup.d.ts",
      "default": "./dist/plugin-sdk/self-hosted-provider-setup.js"
    },
    "./plugin-sdk/routing": {
      "types": "./dist/plugin-sdk/routing.d.ts",
      "default": "./dist/plugin-sdk/routing.js"
    },
    "./plugin-sdk/runtime": {
      "types": "./dist/plugin-sdk/runtime.d.ts",
      "default": "./dist/plugin-sdk/runtime.js"
    },
    "./plugin-sdk/runtime-env": {
      "types": "./dist/plugin-sdk/runtime-env.d.ts",
      "default": "./dist/plugin-sdk/runtime-env.js"
    },
    "./plugin-sdk/setup": {
      "types": "./dist/plugin-sdk/setup.d.ts",
      "default": "./dist/plugin-sdk/setup.js"
    },
    "./plugin-sdk/setup-adapter-runtime": {
      "types": "./dist/plugin-sdk/setup-adapter-runtime.d.ts",
      "default": "./dist/plugin-sdk/setup-adapter-runtime.js"
    },
    "./plugin-sdk/setup-runtime": {
      "types": "./dist/plugin-sdk/setup-runtime.d.ts",
      "default": "./dist/plugin-sdk/setup-runtime.js"
    },
    "./plugin-sdk/channel-setup": {
      "types": "./dist/plugin-sdk/channel-setup.d.ts",
      "default": "./dist/plugin-sdk/channel-setup.js"
    },
    "./plugin-sdk/setup-tools": {
      "types": "./dist/plugin-sdk/setup-tools.d.ts",
      "default": "./dist/plugin-sdk/setup-tools.js"
    },
    "./plugin-sdk/approval-auth-runtime": {
      "types": "./dist/plugin-sdk/approval-auth-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-auth-runtime.js"
    },
    "./plugin-sdk/approval-client-runtime": {
      "types": "./dist/plugin-sdk/approval-client-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-client-runtime.js"
    },
    "./plugin-sdk/approval-delivery-runtime": {
      "types": "./dist/plugin-sdk/approval-delivery-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-delivery-runtime.js"
    },
    "./plugin-sdk/approval-native-runtime": {
      "types": "./dist/plugin-sdk/approval-native-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-native-runtime.js"
    },
    "./plugin-sdk/approval-reply-runtime": {
      "types": "./dist/plugin-sdk/approval-reply-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-reply-runtime.js"
    },
    "./plugin-sdk/approval-runtime": {
      "types": "./dist/plugin-sdk/approval-runtime.d.ts",
      "default": "./dist/plugin-sdk/approval-runtime.js"
    },
    "./plugin-sdk/config-runtime": {
      "types": "./dist/plugin-sdk/config-runtime.d.ts",
      "default": "./dist/plugin-sdk/config-runtime.js"
    },
    "./plugin-sdk/telegram-command-config": {
      "types": "./dist/plugin-sdk/telegram-command-config.d.ts",
      "default": "./dist/plugin-sdk/telegram-command-config.js"
    },
    "./plugin-sdk/config-schema": {
      "types": "./dist/plugin-sdk/config-schema.d.ts",
      "default": "./dist/plugin-sdk/config-schema.js"
    },
    "./plugin-sdk/reply-runtime": {
      "types": "./dist/plugin-sdk/reply-runtime.d.ts",
      "default": "./dist/plugin-sdk/reply-runtime.js"
    },
    "./plugin-sdk/reply-dispatch-runtime": {
      "types": "./dist/plugin-sdk/reply-dispatch-runtime.d.ts",
      "default": "./dist/plugin-sdk/reply-dispatch-runtime.js"
    },
    "./plugin-sdk/reply-reference": {
      "types": "./dist/plugin-sdk/reply-reference.d.ts",
      "default": "./dist/plugin-sdk/reply-reference.js"
    },
    "./plugin-sdk/reply-chunking": {
      "types": "./dist/plugin-sdk/reply-chunking.d.ts",
      "default": "./dist/plugin-sdk/reply-chunking.js"
    },
    "./plugin-sdk/reply-payload": {
      "types": "./dist/plugin-sdk/reply-payload.d.ts",
      "default": "./dist/plugin-sdk/reply-payload.js"
    },
    "./plugin-sdk/agent-media-payload": {
      "types": "./dist/plugin-sdk/agent-media-payload.d.ts",
      "default": "./dist/plugin-sdk/agent-media-payload.js"
    },
    "./plugin-sdk/inbound-reply-dispatch": {
      "types": "./dist/plugin-sdk/inbound-reply-dispatch.d.ts",
      "default": "./dist/plugin-sdk/inbound-reply-dispatch.js"
    },
    "./plugin-sdk/inbound-envelope": {
      "types": "./dist/plugin-sdk/inbound-envelope.d.ts",
      "default": "./dist/plugin-sdk/inbound-envelope.js"
    },
    "./plugin-sdk/channel-reply-pipeline": {
      "types": "./dist/plugin-sdk/channel-reply-pipeline.d.ts",
      "default": "./dist/plugin-sdk/channel-reply-pipeline.js"
    },
    "./plugin-sdk/channel-runtime": {
      "types": "./dist/plugin-sdk/channel-runtime.d.ts",
      "default": "./dist/plugin-sdk/channel-runtime.js"
    },
    "./plugin-sdk/interactive-runtime": {
      "types": "./dist/plugin-sdk/interactive-runtime.d.ts",
      "default": "./dist/plugin-sdk/interactive-runtime.js"
    },
    "./plugin-sdk/outbound-media": {
      "types": "./dist/plugin-sdk/outbound-media.d.ts",
      "default": "./dist/plugin-sdk/outbound-media.js"
    },
    "./plugin-sdk/outbound-runtime": {
      "types": "./dist/plugin-sdk/outbound-runtime.d.ts",
      "default": "./dist/plugin-sdk/outbound-runtime.js"
    },
    "./plugin-sdk/infra-runtime": {
      "types": "./dist/plugin-sdk/infra-runtime.d.ts",
      "default": "./dist/plugin-sdk/infra-runtime.js"
    },
    "./plugin-sdk/runtime-config-snapshot": {
      "types": "./dist/plugin-sdk/runtime-config-snapshot.d.ts",
      "default": "./dist/plugin-sdk/runtime-config-snapshot.js"
    },
    "./plugin-sdk/runtime-group-policy": {
      "types": "./dist/plugin-sdk/runtime-group-policy.d.ts",
      "default": "./dist/plugin-sdk/runtime-group-policy.js"
    },
    "./plugin-sdk/ssrf-policy": {
      "types": "./dist/plugin-sdk/ssrf-policy.d.ts",
      "default": "./dist/plugin-sdk/ssrf-policy.js"
    },
    "./plugin-sdk/ssrf-runtime": {
      "types": "./dist/plugin-sdk/ssrf-runtime.d.ts",
      "default": "./dist/plugin-sdk/ssrf-runtime.js"
    },
    "./plugin-sdk/media-runtime": {
      "types": "./dist/plugin-sdk/media-runtime.d.ts",
      "default": "./dist/plugin-sdk/media-runtime.js"
    },
    "./plugin-sdk/media-understanding-runtime": {
      "types": "./dist/plugin-sdk/media-understanding-runtime.d.ts",
      "default": "./dist/plugin-sdk/media-understanding-runtime.js"
    },
    "./plugin-sdk/conversation-runtime": {
      "types": "./dist/plugin-sdk/conversation-runtime.d.ts",
      "default": "./dist/plugin-sdk/conversation-runtime.js"
    },
    "./plugin-sdk/matrix-runtime-heavy": {
      "types": "./dist/plugin-sdk/matrix-runtime-heavy.d.ts",
      "default": "./dist/plugin-sdk/matrix-runtime-heavy.js"
    },
    "./plugin-sdk/matrix-runtime-shared": {
      "types": "./dist/plugin-sdk/matrix-runtime-shared.d.ts",
      "default": "./dist/plugin-sdk/matrix-runtime-shared.js"
    },
    "./plugin-sdk/thread-bindings-runtime": {
      "types": "./dist/plugin-sdk/thread-bindings-runtime.d.ts",
      "default": "./dist/plugin-sdk/thread-bindings-runtime.js"
    },
    "./plugin-sdk/together": {
      "types": "./dist/plugin-sdk/together.d.ts",
      "default": "./dist/plugin-sdk/together.js"
    },
    "./plugin-sdk/text-runtime": {
      "types": "./dist/plugin-sdk/text-runtime.d.ts",
      "default": "./dist/plugin-sdk/text-runtime.js"
    },
    "./plugin-sdk/text-chunking": {
      "types": "./dist/plugin-sdk/text-chunking.d.ts",
      "default": "./dist/plugin-sdk/text-chunking.js"
    },
    "./plugin-sdk/agent-runtime": {
      "types": "./dist/plugin-sdk/agent-runtime.d.ts",
      "default": "./dist/plugin-sdk/agent-runtime.js"
    },
    "./plugin-sdk/speech-runtime": {
      "types": "./dist/plugin-sdk/speech-runtime.d.ts",
      "default": "./dist/plugin-sdk/speech-runtime.js"
    },
    "./plugin-sdk/speech-core": {
      "types": "./dist/plugin-sdk/speech-core.d.ts",
      "default": "./dist/plugin-sdk/speech-core.js"
    },
    "./plugin-sdk/plugin-runtime": {
      "types": "./dist/plugin-sdk/plugin-runtime.d.ts",
      "default": "./dist/plugin-sdk/plugin-runtime.js"
    },
    "./plugin-sdk/security-runtime": {
      "types": "./dist/plugin-sdk/security-runtime.d.ts",
      "default": "./dist/plugin-sdk/security-runtime.js"
    },
    "./plugin-sdk/gateway-runtime": {
      "types": "./dist/plugin-sdk/gateway-runtime.d.ts",
      "default": "./dist/plugin-sdk/gateway-runtime.js"
    },
    "./plugin-sdk/github-copilot-login": {
      "types": "./dist/plugin-sdk/github-copilot-login.d.ts",
      "default": "./dist/plugin-sdk/github-copilot-login.js"
    },
    "./plugin-sdk/github-copilot-token": {
      "types": "./dist/plugin-sdk/github-copilot-token.d.ts",
      "default": "./dist/plugin-sdk/github-copilot-token.js"
    },
    "./plugin-sdk/cli-runtime": {
      "types": "./dist/plugin-sdk/cli-runtime.d.ts",
      "default": "./dist/plugin-sdk/cli-runtime.js"
    },
    "./plugin-sdk/cli-backend": {
      "types": "./dist/plugin-sdk/cli-backend.d.ts",
      "default": "./dist/plugin-sdk/cli-backend.js"
    },
    "./plugin-sdk/hook-runtime": {
      "types": "./dist/plugin-sdk/hook-runtime.d.ts",
      "default": "./dist/plugin-sdk/hook-runtime.js"
    },
    "./plugin-sdk/host-runtime": {
      "types": "./dist/plugin-sdk/host-runtime.d.ts",
      "default": "./dist/plugin-sdk/host-runtime.js"
    },
    "./plugin-sdk/process-runtime": {
      "types": "./dist/plugin-sdk/process-runtime.d.ts",
      "default": "./dist/plugin-sdk/process-runtime.js"
    },
    "./plugin-sdk/windows-spawn": {
      "types": "./dist/plugin-sdk/windows-spawn.d.ts",
      "default": "./dist/plugin-sdk/windows-spawn.js"
    },
    "./plugin-sdk/acp-runtime": {
      "types": "./dist/plugin-sdk/acp-runtime.d.ts",
      "default": "./dist/plugin-sdk/acp-runtime.js"
    },
    "./plugin-sdk/lazy-runtime": {
      "types": "./dist/plugin-sdk/lazy-runtime.d.ts",
      "default": "./dist/plugin-sdk/lazy-runtime.js"
    },
    "./plugin-sdk/testing": {
      "types": "./dist/plugin-sdk/testing.d.ts",
      "default": "./dist/plugin-sdk/testing.js"
    },
    "./plugin-sdk/temp-path": {
      "types": "./dist/plugin-sdk/temp-path.d.ts",
      "default": "./dist/plugin-sdk/temp-path.js"
    },
    "./plugin-sdk/logging-core": {
      "types": "./dist/plugin-sdk/logging-core.d.ts",
      "default": "./dist/plugin-sdk/logging-core.js"
    },
    "./plugin-sdk/markdown-table-runtime": {
      "types": "./dist/plugin-sdk/markdown-table-runtime.d.ts",
      "default": "./dist/plugin-sdk/markdown-table-runtime.js"
    },
    "./plugin-sdk/account-helpers": {
      "types": "./dist/plugin-sdk/account-helpers.d.ts",
      "default": "./dist/plugin-sdk/account-helpers.js"
    },
    "./plugin-sdk/account-core": {
      "types": "./dist/plugin-sdk/account-core.d.ts",
      "default": "./dist/plugin-sdk/account-core.js"
    },
    "./plugin-sdk/account-id": {
      "types": "./dist/plugin-sdk/account-id.d.ts",
      "default": "./dist/plugin-sdk/account-id.js"
    },
    "./plugin-sdk/account-resolution": {
      "types": "./dist/plugin-sdk/account-resolution.d.ts",
      "default": "./dist/plugin-sdk/account-resolution.js"
    },
    "./plugin-sdk/agent-config-primitives": {
      "types": "./dist/plugin-sdk/agent-config-primitives.d.ts",
      "default": "./dist/plugin-sdk/agent-config-primitives.js"
    },
    "./plugin-sdk/amazon-bedrock": {
      "types": "./dist/plugin-sdk/amazon-bedrock.d.ts",
      "default": "./dist/plugin-sdk/amazon-bedrock.js"
    },
    "./plugin-sdk/allow-from": {
      "types": "./dist/plugin-sdk/allow-from.d.ts",
      "default": "./dist/plugin-sdk/allow-from.js"
    },
    "./plugin-sdk/allowlist-config-edit": {
      "types": "./dist/plugin-sdk/allowlist-config-edit.d.ts",
      "default": "./dist/plugin-sdk/allowlist-config-edit.js"
    },
    "./plugin-sdk/anthropic-vertex": {
      "types": "./dist/plugin-sdk/anthropic-vertex.d.ts",
      "default": "./dist/plugin-sdk/anthropic-vertex.js"
    },
    "./plugin-sdk/bluebubbles": {
      "types": "./dist/plugin-sdk/bluebubbles.d.ts",
      "default": "./dist/plugin-sdk/bluebubbles.js"
    },
    "./plugin-sdk/bluebubbles-policy": {
      "types": "./dist/plugin-sdk/bluebubbles-policy.d.ts",
      "default": "./dist/plugin-sdk/bluebubbles-policy.js"
    },
    "./plugin-sdk/browser": {
      "types": "./dist/plugin-sdk/browser.d.ts",
      "default": "./dist/plugin-sdk/browser.js"
    },
    "./plugin-sdk/browser-runtime": {
      "types": "./dist/plugin-sdk/browser-runtime.d.ts",
      "default": "./dist/plugin-sdk/browser-runtime.js"
    },
    "./plugin-sdk/browser-config-support": {
      "types": "./dist/plugin-sdk/browser-config-support.d.ts",
      "default": "./dist/plugin-sdk/browser-config-support.js"
    },
    "./plugin-sdk/browser-support": {
      "types": "./dist/plugin-sdk/browser-support.d.ts",
      "default": "./dist/plugin-sdk/browser-support.js"
    },
    "./plugin-sdk/boolean-param": {
      "types": "./dist/plugin-sdk/boolean-param.d.ts",
      "default": "./dist/plugin-sdk/boolean-param.js"
    },
    "./plugin-sdk/dangerous-name-runtime": {
      "types": "./dist/plugin-sdk/dangerous-name-runtime.d.ts",
      "default": "./dist/plugin-sdk/dangerous-name-runtime.js"
    },
    "./plugin-sdk/cloudflare-ai-gateway": {
      "types": "./dist/plugin-sdk/cloudflare-ai-gateway.d.ts",
      "default": "./dist/plugin-sdk/cloudflare-ai-gateway.js"
    },
    "./plugin-sdk/byteplus": {
      "types": "./dist/plugin-sdk/byteplus.d.ts",
      "default": "./dist/plugin-sdk/byteplus.js"
    },
    "./plugin-sdk/chutes": {
      "types": "./dist/plugin-sdk/chutes.d.ts",
      "default": "./dist/plugin-sdk/
... [TRUNCATED]
```

### File: README.md
```md
# 🦞 OpenClaw — Personal AI Assistant

<p align="center">
    <picture>
        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-logo-text-dark.svg">
        <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-logo-text.svg" alt="OpenClaw" width="500">
    </picture>
</p>

<p align="center">
  <strong>EXFOLIATE! EXFOLIATE!</strong>
</p>

<p align="center">
  <a href="https://github.com/openclaw/openclaw/actions/workflows/ci.yml?branch=main"><img src="https://img.shields.io/github/actions/workflow/status/openclaw/openclaw/ci.yml?branch=main&style=for-the-badge" alt="CI status"></a>
  <a href="https://github.com/openclaw/openclaw/releases"><img src="https://img.shields.io/github/v/release/openclaw/openclaw?include_prereleases&style=for-the-badge" alt="GitHub release"></a>
  <a href="https://discord.gg/clawd"><img src="https://img.shields.io/discord/1456350064065904867?label=Discord&logo=discord&logoColor=white&color=5865F2&style=for-the-badge" alt="Discord"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
</p>

**OpenClaw** is a _personal AI assistant_ you run on your own devices.
It answers you on the channels you already use (WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, BlueBubbles, IRC, Microsoft Teams, Matrix, Feishu, LINE, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon, Twitch, Zalo, Zalo Personal, WeChat, WebChat). It can speak and listen on macOS/iOS/Android, and can render a live Canvas you control. The Gateway is just the control plane — the product is the assistant.

If you want a personal, single-user assistant that feels local, fast, and always-on, this is it.

[Website](https://openclaw.ai) · [Docs](https://docs.openclaw.ai) · [Vision](VISION.md) · [DeepWiki](https://deepwiki.com/openclaw/openclaw) · [Getting Started](https://docs.openclaw.ai/start/getting-started) · [Updating](https://docs.openclaw.ai/install/updating) · [Showcase](https://docs.openclaw.ai/start/showcase) · [FAQ](https://docs.openclaw.ai/help/faq) · [Onboarding](https://docs.openclaw.ai/start/wizard) · [Nix](https://github.com/openclaw/nix-openclaw) · [Docker](https://docs.openclaw.ai/install/docker) · [Discord](https://discord.gg/clawd)

Preferred setup: run `openclaw onboard` in your terminal.
OpenClaw Onboard guides you step by step through setting up the gateway, workspace, channels, and skills. It is the recommended CLI setup path and works on **macOS, Linux, and Windows (via WSL2; strongly recommended)**.
Works with npm, pnpm, or bun.
New install? Start here: [Getting started](https://docs.openclaw.ai/start/getting-started)

## Sponsors

<table>
  <tr>
    <td align="center" width="16.66%">
      <a href="https://openai.com/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/openai-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/openai.svg" alt="OpenAI" height="28">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://github.com/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/github-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/github.svg" alt="GitHub" height="28">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://www.nvidia.com/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/nvidia.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/nvidia-dark.svg" alt="NVIDIA" height="28">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://vercel.com/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/vercel-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/vercel.svg" alt="Vercel" height="24">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://blacksmith.sh/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/blacksmith-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/blacksmith.svg" alt="Blacksmith" height="28">
        </picture>
      </a>
    </td>
    <td align="center" width="16.66%">
      <a href="https://www.convex.dev/">
        <picture>
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/convex-light.svg">
          <img src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/sponsors/convex.svg" alt="Convex" height="24">
        </picture>
      </a>
    </td>
  </tr>
</table>

**Subscriptions (OAuth):**

- **[OpenAI](https://openai.com/)** (ChatGPT/Codex)

Model note: while many providers/models are supported, for the best experience and lower prompt-injection risk use the strongest latest-generation model available to you. See [Onboarding](https://docs.openclaw.ai/start/onboarding).

## Models (selection + auth)

- Models config + CLI: [Models](https://docs.openclaw.ai/concepts/models)
- Auth profile rotation (OAuth vs API keys) + fallbacks: [Model failover](https://docs.openclaw.ai/concepts/model-failover)

## Install (recommended)

Runtime: **Node 24 (recommended) or Node 22.16+**.

```bash
npm install -g openclaw@latest
# or: pnpm add -g openclaw@latest

openclaw onboard --install-daemon
```

OpenClaw Onboard installs the Gateway daemon (launchd/systemd user service) so it stays running.

## Quick start (TL;DR)

Runtime: **Node 24 (recommended) or Node 22.16+**.

Full beginner guide (auth, pairing, channels): [Getting started](https://docs.openclaw.ai/start/getting-started)

```bash
openclaw onboard --install-daemon

openclaw gateway --port 18789 --verbose

# Send a message
openclaw message send --to +1234567890 --message "Hello from OpenClaw"

# Talk to the assistant (optionally deliver back to any connected channel: WhatsApp/Telegram/Slack/Discord/Google Chat/Signal/iMessage/BlueBubbles/IRC/Microsoft Teams/Matrix/Feishu/LINE/Mattermost/Nextcloud Talk/Nostr/Synology Chat/Tlon/Twitch/Zalo/Zalo Personal/WeChat/WebChat)
openclaw agent --message "Ship checklist" --thinking high
```

Upgrading? [Updating guide](https://docs.openclaw.ai/install/updating) (and run `openclaw doctor`).

## Development channels

- **stable**: tagged releases (`vYYYY.M.D` or `vYYYY.M.D-<patch>`), npm dist-tag `latest`.
- **beta**: prerelease tags (`vYYYY.M.D-beta.N`), npm dist-tag `beta` (macOS app may be missing).
- **dev**: moving head of `main`, npm dist-tag `dev` (when published).

Switch channels (git + npm): `openclaw update --channel stable|beta|dev`.
Details: [Development channels](https://docs.openclaw.ai/install/development-channels).

## From source (development)

Prefer `pnpm` for builds from source. Bun is optional for running TypeScript directly.

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw

pnpm install
pnpm ui:build # auto-installs UI deps on first run
pnpm build

pnpm openclaw onboard --install-daemon

# Dev loop (auto-reload on source/config changes)
pnpm gateway:watch
```

Note: `pnpm openclaw ...` runs TypeScript directly (via `tsx`). `pnpm build` produces `dist/` for running via Node / the packaged `openclaw` binary.

## Security defaults (DM access)

OpenClaw connects to real messaging surfaces. Treat inbound DMs as **untrusted input**.

Full security guide: [Security](https://docs.openclaw.ai/gateway/security)

Default behavior on Telegram/WhatsApp/Signal/iMessage/Microsoft Teams/Discord/Google Chat/Slack:

- **DM pairing** (`dmPolicy="pairing"` / `channels.discord.dmPolicy="pairing"` / `channels.slack.dmPolicy="pairing"`; legacy: `channels.discord.dm.policy`, `channels.slack.dm.policy`): unknown senders receive a short pairing code and the bot does not process their message.
- Approve with: `openclaw pairing approve <channel> <code>` (then the sender is added to a local allowlist store).
- Public inbound DMs require an explicit opt-in: set `dmPolicy="open"` and include `"*"` in the channel allowlist (`allowFrom` / `channels.discord.allowFrom` / `channels.slack.allowFrom`; legacy: `channels.discord.dm.allowFrom`, `channels.slack.dm.allowFrom`).

Run `openclaw doctor` to surface risky/misconfigured DM policies.

## Highlights

- **[Local-first Gateway](https://docs.openclaw.ai/gateway)** — single control plane for sessions, channels, tools, and events.
- **[Multi-channel inbox](https://docs.openclaw.ai/channels)** — WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, BlueBubbles (iMessage), iMessage (legacy), IRC, Microsoft Teams, Matrix, Feishu, LINE, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon, Twitch, Zalo, Zalo Personal, WeChat, WebChat, macOS, iOS/Android.
- **[Multi-agent routing](https://docs.openclaw.ai/gateway/configuration)** — route inbound channels/accounts/peers to isolated agents (workspaces + per-agent sessions).
- **[Voice Wake](https://docs.openclaw.ai/nodes/voicewake) + [Talk Mode](https://docs.openclaw.ai/nodes/talk)** — wake words on macOS/iOS and continuous voice on Android (ElevenLabs + system TTS fallback).
- **[Live Canvas](https://docs.openclaw.ai/platforms/mac/canvas)** — agent-driven visual workspace with [A2UI](https://docs.openclaw.ai/platforms/mac/canvas#canvas-a2ui).
- **[First-class tools](https://docs.openclaw.ai/tools)** — browser, canvas, nodes, cron, sessions, and Discord/Slack actions.
- **[Companion apps](https://docs.openclaw.ai/platforms/macos)** — macOS menu bar app + iOS/Android [nodes](https://docs.openclaw.ai/nodes).
- **[Onboarding](https://docs.openclaw.ai/start/wizard) + [skills](https://docs.openclaw.ai/tools/skills)** — onboarding-driven setup with bundled/managed/workspace skills.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=openclaw/openclaw&type=date&legend=top-left)](https://www.star-history.com/#openclaw/openclaw&type=date&legend=top-left)

## Everything we built so far

### Core platform

- [Gateway WS control plane](https://docs.openclaw.ai/gateway) with sessions, presence, config, cron, webhooks, [Control UI](https://docs.openclaw.ai/web), and [Canvas host](https://docs.openclaw.ai/platforms/mac/canvas#canvas-a2ui).
- [CLI surface](https://docs.openclaw.ai/tools/agent-send): gateway, agent, send, [onboarding](https://docs.openclaw.ai/start/wizard), and [doctor](https://docs.openclaw.ai/gateway/doctor).
- [Pi agent runtime](https://docs.openclaw.ai/concepts/agent) in RPC mode with tool streaming and block streaming.
- [Session model](https://docs.openclaw.ai/concepts/session): `main` for direct chats, group isolation, activation modes, queue modes, reply-back. Group rules: [Groups](https://docs.openclaw.ai/channels/groups).
- [Media pipeline](https://docs.openclaw.ai/nodes/images): images/audio/video, transcription hooks, size caps, temp file lifecycle. Audio details: [Audio](https://docs.openclaw.ai/nodes/audio).

### Channels

- [Channels](https://docs.openclaw.ai/channels): [WhatsApp](https://docs.openclaw.ai/channels/whatsapp) (Baileys), [Telegram](https://docs.openclaw.ai/channels/telegram) (grammY), [Slack](https://docs.openclaw.ai/channels/slack) (Bolt), [Discord](https://docs.openclaw.ai/channels/discord) (discord.js), [Google Chat](https://docs.openclaw.ai/channels/googlechat) (Chat API), [Signal](https://docs.openclaw.ai/channels/signal) (signal-cli), [BlueBubbles](https://docs.openclaw.ai/channels/bluebubbles) (iMessage, recommended), [iMessage](https://docs.openclaw.ai/channels/imessage) (legacy imsg), [IRC](https://docs.openclaw.ai/channels/irc), [Microsoft Teams](https://docs.openclaw.ai/channels/msteams), [Matrix](https://docs.openclaw.ai/channels/matrix), [Feishu](https://docs.openclaw.ai/channels/feishu), [LINE](https://docs.openclaw.ai/channels/line), [Mattermost](https://docs.openclaw.ai/channels/mattermost), [Nextcloud Talk](https://docs.openclaw.ai/channels/nextcloud-talk), [Nostr](https://docs.openclaw.ai/channels/nostr), [Synology Chat](https://docs.openclaw.ai/channels/synology-chat), [Tlon](https://docs.openclaw.ai/channels/tlon), [Twitch](https://docs.openclaw.ai/channels/twitch), [Zalo](https://docs.openclaw.ai/channels/zalo), [Zalo Personal](https://docs.openclaw.ai/channels/zalouser), WeChat (`@tencent-weixin/openclaw-weixin`), [WebChat](https://docs.openclaw.ai/web/webchat).
- [Group routing](https://docs.openclaw.ai/channels/group-messages): mention gating, reply tags, per-channel chunking and routing. Channel rules: [Channels](https://docs.openclaw.ai/channels).

### Apps + nodes

- [macOS app](https://docs.openclaw.ai/platforms/macos): menu bar control plane, [Voice Wake](https://docs.openclaw.ai/nodes/voicewake)/PTT, [Talk Mode](https://docs.openclaw.ai/nodes/talk) overlay, [WebChat](https://docs.openclaw.ai/web/webchat), debug tools, [remote gateway](https://docs.openclaw.ai/gateway/remote) control.
- [iOS node](https://docs.openclaw.ai/platforms/ios): [Canvas](https://docs.openclaw.ai/platforms/mac/canvas), [Voice Wake](https://docs.openclaw.ai/nodes/voicewake), [Talk Mode](https://docs.openclaw.ai/nodes/talk), camera, screen recording, Bonjour + device pairing.
- [Android node](https://docs.openclaw.ai/platforms/android): Connect tab (setup code/manual), chat sessions, voice tab, [Canvas](https://docs.openclaw.ai/platforms/mac/canvas), camera/screen recording, and Android device commands (notifications/location/SMS/photos/contacts/calendar/motion/app update).
- [macOS node mode](https://docs.openclaw.ai/nodes): system.run/notify + canvas/camera exposure.

### Tools + automation

- [Browser control](https://docs.openclaw.ai/tools/browser): dedicated openclaw Chrome/Chromium, snapshots, actions, uploads, profiles.
- [Canvas](https://docs.openclaw.ai/platforms/mac/canvas): [A2UI](https://docs.openclaw.ai/platforms/mac/canvas#canvas-a2ui) push/reset, eval, snapshot.
- [Nodes](https://docs.openclaw.ai/nodes): camera snap/clip, screen record, [location.get](https://docs.openclaw.ai/nodes/location-command), notifications.
- [Cron + wakeups](https://docs.openclaw.ai/automation/cron-jobs); [webhooks](https://docs.openclaw.ai/automation/webhook); [Gmail Pub/Sub](https://docs.openclaw.ai/automatio
... [TRUNCATED]
```

### File: docs\.generated\README.md
```md
# Generated Docs Artifacts

SHA-256 hash files are the tracked drift-detection artifacts. The full JSON
baselines are generated locally (gitignored) for inspection only.

**Tracked (committed to git):**

- `config-baseline.sha256` — hashes of config baseline JSON artifacts.
- `plugin-sdk-api-baseline.sha256` — hashes of Plugin SDK API baseline artifacts.

**Local only (gitignored):**

- `config-baseline.json`, `config-baseline.core.json`, `config-baseline.channel.json`, `config-baseline.plugin.json`
- `plugin-sdk-api-baseline.json`, `plugin-sdk-api-baseline.jsonl`

Do not edit any of these files by hand.

- Regenerate config baseline: `pnpm config:docs:gen`
- Validate config baseline: `pnpm config:docs:check`
- Regenerate Plugin SDK API baseline: `pnpm plugin-sdk:api:gen`
- Validate Plugin SDK API baseline: `pnpm plugin-sdk:api:check`

```

### File: docs\.i18n\README.md
```md
# OpenClaw docs i18n assets

This folder stores **generated** and **config** files for documentation translations.

## Files

- `glossary.<lang>.json` — preferred term mappings (used in prompt guidance).
- `<lang>.tm.jsonl` — translation memory (cache) keyed by workflow + model + text hash.

## Glossary format

`glossary.<lang>.json` is an array of entries:

```json
{
  "source": "troubleshooting",
  "target": "故障排除",
  "ignore_case": true,
  "whole_word": false
}
```

Fields:

- `source`: English (or source) phrase to prefer.
- `target`: preferred translation output.

## Notes

- Glossary entries are passed to the model as **prompt guidance** (no deterministic rewrites).
- The translation memory is updated by `scripts/docs-i18n`.

```

### File: .agents_DISTILLED.md
```md
---
id: .agents
type: distilled_knowledge
---
# .agents

## SWALLOW ENGINE DISTILLATION

### File: maintainers.md
```md
Maintainer skills now live in [`openclaw/maintainers`](https://github.com/openclaw/maintainers/).

```

### File: skills_DISTILLED.md
```md
---
id: skills
type: distilled_knowledge
---
# skills

## SWALLOW ENGINE DISTILLATION

### File: openclaw-ghsatainer_DISTILLED.md
```md
---
id: openclaw-ghsa-maintainer
type: distilled_knowledge
---
# openclaw-ghsa-maintainer

## SWALLOW ENGINE DISTILLATION

### File: SKILL.md
```md
---
name: openclaw-ghsa-maintainer
description: Maintainer workflow for OpenClaw GitHub Security Advisories (GHSA). Use when Codex needs to inspect, patch, validate, or publish a repo advisory, verify private-fork state, prepare advisory Markdown or JSON payloads safely, handle GHSA API-specific publish constraints, or confirm advisory publish success.
---

# OpenClaw GHSA Maintainer

Use this skill for repo security advisory workflow only. Keep general release work in `openclaw-release-maintainer`.

## Respect advisory guardrails

- Before reviewing or publishing a repo advisory, read `SECURITY.md`.
- Ask permission before any publish action.
- Treat this skill as GHSA-only. Do not use it for stable or beta release work.

## Fetch and inspect advisory state

Fetch the current advisory and the latest published npm version:

```bash
gh api /repos/openclaw/openclaw/security-advisories/<GHSA>
npm view openclaw version --userconfig "$(mktemp)"
```

Use the fetch output to confirm the advisory state, linked private fork, and vulnerability payload shape before patching.

## Verify private fork PRs are closed

Before publishing, verify that the advisory's private fork has no open PRs:

```bash
fork=$(gh api /repos/openclaw/openclaw/security-advisories/<GHSA> | jq -r .private_fork.full_name)
gh pr list -R "$fork" --state open
```

The PR list must be empty before publish.

## Prepare advisory Markdown and JSON safely

- Write advisory Markdown via heredoc to a temp file. Do not use escaped `\n` strings.
- Build PATCH payload JSON with `jq`, not hand-escaped shell JSON.

Example pattern:

```bash
cat > /tmp/ghsa.desc.md <<'EOF'
<markdown description>
EOF

jq -n --rawfile desc /tmp/ghsa.desc.md \
  '{summary,severity,description:$desc,vulnerabilities:[...]}' \
  > /tmp/ghsa.patch.json
```

## Apply PATCH calls in the correct sequence

- Do not set `severity` and `cvss_vector_string` in the same PATCH call.
- Use separate calls when the advisory requires both fields.
- Publish by PATCHing the advisory and setting `"state":"published"`. There is no separate `/publish` endpoint.

Example shape:

```bash
gh api -X PATCH /repos/openclaw/openclaw/security-advisories/<GHSA> \
  --input /tmp/ghsa.patch.json
```

## Publish and verify success

After publish, re-fetch the advisory and confirm:

- `state=published`
- `published_at` is set
- the description does not contain literal escaped `\\n`

Verification pattern:

```bash
gh api /repos/openclaw/openclaw/security-advisories/<GHSA>
jq -r .description < /tmp/ghsa.refetch.json | rg '\\\\n'
```

## Common GHSA footguns

- Publishing fails with HTTP 422 if required fields are missing or the private fork still has open PRs.
- A payload that looks correct in shell can still be wrong if Markdown was assembled with escaped newline strings.
- Advisory PATCH sequencing matters; separate field updates when GHSA API constraints require it.

```


```

### File: openclaw-parallels-smoke_DISTILLED.md
```md
---
id: openclaw-parallels-smoke
type: distilled_knowledge
---
# openclaw-parallels-smoke

## SWALLOW ENGINE DISTILLATION

### File: SKILL.md
```md
---
name: openclaw-parallels-smoke
description: End-to-end Parallels smoke, upgrade, and rerun workflow for OpenClaw across macOS, Windows, and Linux guests. Use when Codex needs to run, rerun, debug, or interpret VM-based install, onboarding, gateway smoke tests, latest-release-to-main upgrade checks, fresh snapshot retests, or optional Discord roundtrip verification under Parallels.
---

# OpenClaw Parallels Smoke

Use this skill for Parallels guest workflows and smoke interpretation. Do not load it for normal repo work.

## Global rules

- Use the snapshot most closely matching the requested fresh baseline.
- Gateway verification in smoke runs should use `openclaw gateway status --deep --require-rpc` unless the stable version being checked does not support it yet.
- Stable `2026.3.12` pre-upgrade diagnostics may require a plain `gateway status --deep` fallback.
- Treat `precheck=latest-ref-fail` on that stable pre-upgrade lane as baseline, not automatically a regression.
- Pass `--json` for machine-readable summaries.
- Per-phase logs land under `/tmp/openclaw-parallels-*`.
- Do not run local and gateway agent turns in parallel on the same fresh workspace or session.
- If `main` is moving under active multi-agent work, prefer a detached worktree pinned to one commit for long Parallels suites. The smoke scripts now verify the packed tgz commit instead of live `git rev-parse HEAD`, but a pinned worktree still avoids noisy rebuild/version drift during reruns.
- For `prlctl exec`, pass the VM name before `--current-user` (`prlctl exec "$VM" --current-user ...`), not the other way around.
- If the workflow installs OpenClaw from a repo checkout instead of the site installer/npm release, finish by installing a real guest CLI shim and verifying it in a fresh guest shell. `pnpm openclaw ...` inside the repo is not enough for handoff parity.
- On macOS guests, prefer a user-global install plus a stable PATH-visible shim:
  - install with `NPM_CONFIG_PREFIX="$HOME/.npm-global" npm install -g .`
  - make sure `~/.local/bin/openclaw` exists or `~/.npm-global/bin` is on PATH
  - verify from a brand-new guest shell with `which openclaw` and `openclaw --version`

## npm install then update

- Preferred entrypoint: `pnpm test:parallels:npm-update`
- Flow: fresh snapshot -> install npm package baseline -> smoke -> install current main tgz on the same guest -> smoke again.
- Same-guest update verification should set the default model explicitly to `openai/gpt-5.4` before the agent turn and use a fresh explicit `--session-id` so old session model state does not leak into the check.
- The aggregate npm-update wrapper must resolve the Linux VM with the same Ubuntu fallback policy as `parallels-linux-smoke.sh` before both fresh and update lanes. Treat any Ubuntu guest with major version `>= 24` as acceptable when the exact default VM is missing, preferring the closest version match. On Peter's current host today, missing `Ubuntu 24.04.3 ARM64` should fall back to `Ubuntu 25.10`.
- On macOS same-guest update checks, restart the gateway after the npm upgrade before `gateway status` / `agent`; launchd can otherwise report a loaded service while the old process has exited and the fresh process is not RPC-ready yet.
- On Windows same-guest update checks, restart the gateway after the npm upgrade before `gateway status` / `agent`; in-place global npm updates can otherwise leave stale hashed `dist/*` module imports alive in the running service.
- For Windows same-guest update checks, prefer the done-file/log-drain PowerShell runner pattern over one long-lived `prlctl exec ... powershell -EncodedCommand ...` transport. The guest can finish successfully while the outer `prlctl exec` still hangs.
- The Windows same-guest update helper should write stage markers to its log before long steps like tgz download and `npm install -g` so the outer progress monitor does not sit on `waiting for first log line` during healthy but quiet installs.
- Linux same-guest update verification should also export `HOME=/root`, pass `OPENAI_API_KEY` via `prlctl exec ... /usr/bin/env`, and use `openclaw agent --local`; the fresh Linux baseline does not rely on persisted gateway credentials.
- The npm-update wrapper now prints per-lane progress from the nested log files. If a lane still looks stuck, inspect the nested logs in `runDir` first (`macos-fresh.log`, `windows-fresh.log`, `linux-fresh.log`, `macos-update.log`, `windows-update.log`, `linux-update.log`) instead of assuming the outer wrapper hung.
- If the wrapper fails a lane, read the auto-dumped tail first, then the full nested lane log under `/tmp/openclaw-parallels-npm-update.*`.

## CLI invocation footgun

- The Parallels smoke shell scripts should tolerate a literal bare `--` arg so `pnpm test:parallels:* -- --json` and similar forwarded invocations work without needing to call `bash scripts/e2e/...` directly.

## macOS flow

- Preferred entrypoint: `pnpm test:parallels:macos`
- Default to the snapshot closest to `macOS 26.3.1 latest`.
- On Peter's Tahoe VM, `fresh-latest-march-2026` can hang in `prlctl snapshot-switch`; if restore times out there, rerun with `--snapshot-hint 'macOS 26.3.1 latest'` before blaming auth or the harness.
- `parallels-macos-smoke.sh` now retries `snapshot-switch` once after force-stopping a stuck running/suspended guest. If Tahoe still times out after that recovery path, then treat it as a real Parallels/host issue and rerun manually.
- The macOS smoke should include a dashboard load phase after gateway health: resolve the tokenized URL with `openclaw dashboard --no-open`, verify the served HTML contains the Control UI title/root shell, then open Safari and require an established localhost TCP connection from Safari to the gateway port.
- If a packaged install regresses with `500` on `/`, `/healthz`, or `__openclaw/control-ui-config.json` after `fresh.install-main` or `upgrade.install-main`, suspect bundled plugin runtime deps resolving from the package root `node_modules` rather than `dist/extensions/*/node_modules`. Repro quickly with a real `npm pack`/global install lane before blaming dashboard auth or Safari.
- `prlctl exec` is fine for deterministic repo commands, but use the guest Terminal or `prlctl enter` when installer parity or shell-sensitive behavior matters.
- Multi-word `openclaw agent --message ...` checks should go through a guest shell wrapper (`guest_current_user_sh` / `guest_current_user_cli` or `/bin/sh -lc ...`), not raw `prlctl exec ... node openclaw.mjs ...`, or the message can be split into extra argv tokens and Commander reports `too many arguments for 'agent'`.
- When ref-mode onboarding stores `OPENAI_API_KEY` as an env secret ref, the post-onboard agent verification should also export `OPENAI_API_KEY` for the guest command. The gateway can still reject with pairing-required and fall back to embedded execution, and that fallback needs the env-backed credential available in the shell.
- On the fresh Tahoe snapshot, `brew` exists but `node` may be missing from PATH in noninteractive exec. Use `/opt/homebrew/bin/node` when needed.
- Fresh host-served tgz installs should install as guest root with `HOME=/var/root`, then run onboarding as the desktop user via `prlctl exec --current-user`.
- Root-installed tgz smoke can log plugin blocks for world-writable `extensions/*`; do not treat that as an onboarding or gateway failure unless plugin loading is the task.

## Windows flow

- Preferred entrypoint: `pnpm test:parallels:windows`
- Use the snapshot closest to `pre-openclaw-native-e2e-2026-03-12`.
- Always use `prlctl exec --current-user`; plain `prlctl exec` lands in `NT AUTHORITY\\SYSTEM`.
- Prefer explicit `npm.cmd` and `openclaw.cmd`.
- Use PowerShell only as the transport with `-ExecutionPolicy Bypass`, then call the `.cmd` shims from inside it.
- Multi-word `openclaw agent --message ...` checks should call `& $openclaw ...` inside PowerShell, not `Start-Process ... -ArgumentList` against `openclaw.cmd`, or Commander can see split argv and throw `too many arguments for 'agent'`.
- Windows installer/tgz phases now retry once after guest-ready recheck; keep new Windows smoke steps idempotent so a transport-flake retry is safe.
- If a Windows retry sees the VM become `suspended` or `stopped`, resume/start it before the next `prlctl exec`; otherwise the second attempt just repeats the same `rc=255`.
- Windows global `npm install -g` phases can stay quiet for a minute or more even when healthy; inspect the phase log before calling it hung, and only treat it as a regression once the retry wrapper or timeout trips.
- Fresh Windows ref-mode onboard should use the same background PowerShell runner plus done-file/log-drain pattern as the npm-update helper, including startup materialization checks, host-side timeouts on short poll `prlctl exec` calls, and retry-on-poll-failure behavior for transient transport flakes.
- Fresh Windows ref-mode agent verification should set `OPENAI_API_KEY` in the PowerShell environment before invoking `openclaw.cmd agent`, for the same pairing-required fallback reason as macOS.
- The standalone Windows upgrade smoke lane should stop the managed gateway after `upgrade.install-main` and before `upgrade.onboard-ref`. Restarting before onboard can leave the old process alive on the pre-onboard token while onboard rewrites `~/.openclaw/openclaw.json`, which then fails `gateway-health` with `unauthorized: gateway token mismatch`.
- If standalone Windows upgrade fails with a gateway token mismatch but `pnpm test:parallels:npm-update` passes, trust the mismatch as a standalone ref-onboard ordering bug first; the npm-update helper does not re-run ref-mode onboard on the same guest.
- Keep onboarding and status output ASCII-clean in logs; fancy punctuation becomes mojibake in current capture paths.
- If you hit an older run with `rc=255` plus an empty `fresh.install-main.log` or `upgrade.install-main.log`, treat it as a likely `prlctl exec` transport drop after guest start-up, not immediate proof of an npm/package failure.

## Linux flow

- Preferred entrypoint: `pnpm test:parallels:linux`
- Use the snapshot closest to fresh `Ubuntu 24.04.3 ARM64`.
- If that exact VM is missing on the host, any Ubuntu guest with major version `>= 24` is acceptable; prefer the closest versioned Ubuntu guest with a fresh poweroff snapshot. On Peter's host today, that is `Ubuntu 25.10`.
- Use plain `prlctl exec`; `--current-user` is not the right transport on this snapshot.
- Fresh snapshots may be missing `curl`, and `apt-get update` can fail on clock skew. Bootstrap with `apt-get -o Acquire::Check-Date=false update` and install `curl ca-certificates`.
- Fresh `main` tgz smoke still needs the latest-release installer first because the snapshot has no Node or npm before bootstrap.
- This snapshot does not have a usable `systemd --user` session; managed daemon install is unsupported.
- The Linux smoke now falls back to a manual `setsid openclaw gateway run --bind loopback --port 18789 --force` launch with `HOME=/root` and the provider secret exported, then verifies `gateway status --deep --require-rpc` when available.
- The Linux manual gateway launch should wait for `gateway status --deep --require-rpc` inside the `gateway-start` phase; otherwise the first 
... [TRUNCATED]
```

### File: .jscpd.json
```json
{
  "gitignore": true,
  "noSymlinks": true,
  "ignore": [
    "**/node_modules/**",
    "**/dist/**",
    "dist/**",
    "**/.git/**",
    "**/coverage/**",
    "**/build/**",
    "**/.build/**",
    "**/.artifacts/**",
    "docs/zh-CN/**",
    "**/CHANGELOG.md"
  ]
}

```

### File: .oxlintrc.json
```json
{
  "$schema": "./node_modules/oxlint/configuration_schema.json",
  "plugins": ["unicorn", "typescript", "oxc"],
  "categories": {
    "correctness": "error",
    "perf": "error",
    "suspicious": "error"
  },
  "rules": {
    "curly": "error",
    "eslint-plugin-unicorn/prefer-array-find": "off",
    "eslint/no-await-in-loop": "off",
    "eslint/no-new": "off",
    "eslint/no-shadow": "off",
    "eslint/no-unmodified-loop-condition": "off",
    "oxc/no-accumulating-spread": "off",
    "oxc/no-async-endpoint-handlers": "off",
    "oxc/no-map-spread": "off",
    "typescript/no-explicit-any": "error",
    "typescript/no-extraneous-class": "off",
    "typescript/no-unsafe-type-assertion": "off",
    "unicorn/consistent-function-scoping": "off",
    "unicorn/require-post-message-target-origin": "off"
  },
  "ignorePatterns": [
    "assets/",
    "dist/",
    "docs/_layouts/",
    "extensions/",
    "node_modules/",
    "patches/",
    "pnpm-lock.yaml",
    "skills/",
    "src/auto-reply/reply/export-html/template.js",
    "src/canvas-host/a2ui/a2ui.bundle.js",
    "Swabble/",
    "vendor/"
  ]
}

```

### File: .pi_DISTILLED.md
```md
---
id: .pi
type: distilled_knowledge
---
# .pi

## SWALLOW ENGINE DISTILLATION

### File: extensions_DISTILLED.md
```md
---
id: extensions
type: distilled_knowledge
---
# extensions

## SWALLOW ENGINE DISTILLATION

### File: diff.ts
```ts
/**
 * Diff Extension
 *
 * /diff command shows modified/deleted/new files from git status and opens
 * the selected file in VS Code's diff view.
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { showPagedSelectList } from "./ui/paged-select";

interface FileInfo {
  status: string;
  statusLabel: string;
  file: string;
}

export default function (pi: ExtensionAPI) {
  pi.registerCommand("diff", {
    description: "Show git changes and open in VS Code diff view",
    handler: async (_args, ctx) => {
      if (!ctx.hasUI) {
        ctx.ui.notify("No UI available", "error");
        return;
      }

      // Get changed files from git status
      const result = await pi.exec("git", ["status", "--porcelain"], { cwd: ctx.cwd });

      if (result.code !== 0) {
        ctx.ui.notify(`git status failed: ${result.stderr}`, "error");
        return;
      }

      if (!result.stdout || !result.stdout.trim()) {
        ctx.ui.notify("No changes in working tree", "info");
        return;
      }

      // Parse git status output
      // Format: XY filename (where XY is two-letter status, then space, then filename)
      const lines = result.stdout.split("\n");
      const files: FileInfo[] = [];

      for (const line of lines) {
        if (line.length < 4) {
          continue;
        } // Need at least "XY f"

        const status = line.slice(0, 2);
        const file = line.slice(2).trimStart();

        // Translate status codes to short labels
        let statusLabel: string;
        if (status.includes("M")) {
          statusLabel = "M";
        } else if (status.includes("A")) {
          statusLabel = "A";
        } else if (status.includes("D")) {
          statusLabel = "D";
        } else if (status.includes("?")) {
          statusLabel = "?";
        } else if (status.includes("R")) {
          statusLabel = "R";
        } else if (status.includes("C")) {
          statusLabel = "C";
        } else {
          statusLabel = status.trim() || "~";
        }

        files.push({ status: statusLabel, statusLabel, file });
      }

      if (files.length === 0) {
        ctx.ui.notify("No changes found", "info");
        return;
      }

      const openSelected = async (fileInfo: FileInfo): Promise<void> => {
        try {
          // Open in VS Code diff view.
          // For untracked files, git difftool won't work, so fall back to just opening the file.
          if (fileInfo.status === "?") {
            await pi.exec("code", ["-g", fileInfo.file], { cwd: ctx.cwd });
            return;
          }

          const diffResult = await pi.exec(
            "git",
            ["difftool", "-y", "--tool=vscode", fileInfo.file],
            {
              cwd: ctx.cwd,
            },
          );
          if (diffResult.code !== 0) {
            await pi.exec("code", ["-g", fileInfo.file], { cwd: ctx.cwd });
          }
        } catch (error) {
          const message = error instanceof Error ? error.message : String(error);
          ctx.ui.notify(`Failed to open ${fileInfo.file}: ${message}`, "error");
        }
      };

      const items = files.map((file) => ({
        value: file,
        label: `${file.status} ${file.file}`,
      }));
      await showPagedSelectList({
        ctx,
        title: " Select file to diff",
        items,
        onSelect: (item) => {
          void openSelected(item.value as FileInfo);
        },
      });
    },
  });
}

```

### File: files.ts
```ts
/**
 * Files Extension
 *
 * /files command lists all files the model has read/written/edited in the active session branch,
 * coalesced by path and sorted newest first. Selecting a file opens it in VS Code.
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { showPagedSelectList } from "./ui/paged-select";

interface FileEntry {
  path: string;
  operations: Set<"read" | "write" | "edit">;
  lastTimestamp: number;
}

type FileToolName = "read" | "write" | "edit";

export default function (pi: ExtensionAPI) {
  pi.registerCommand("files", {
    description: "Show files read/written/edited in this session",
    handler: async (_args, ctx) => {
      if (!ctx.hasUI) {
        ctx.ui.notify("No UI available", "error");
        return;
      }

      // Get the current branch (path from leaf to root)
      const branch = ctx.sessionManager.getBranch();

      // First pass: collect tool calls (id -> {path, name}) from assistant messages
      const toolCalls = new Map<string, { path: string; name: FileToolName; timestamp: number }>();

      for (const entry of branch) {
        if (entry.type !== "message") {
          continue;
        }
        const msg = entry.message;

        if (msg.role === "assistant" && Array.isArray(msg.content)) {
          for (const block of msg.content) {
            if (block.type === "toolCall") {
              const name = block.name;
              if (name === "read" || name === "write" || name === "edit") {
                const path = block.arguments?.path;
                if (path && typeof path === "string") {
                  toolCalls.set(block.id, { path, name, timestamp: msg.timestamp });
                }
              }
            }
          }
        }
      }

      // Second pass: match tool results to get the actual execution timestamp
      const fileMap = new Map<string, FileEntry>();

      for (const entry of branch) {
        if (entry.type !== "message") {
          continue;
        }
        const msg = entry.message;

        if (msg.role === "toolResult") {
          const toolCall = toolCalls.get(msg.toolCallId);
          if (!toolCall) {
            continue;
          }

          const { path, name } = toolCall;
          const timestamp = msg.timestamp;

          const existing = fileMap.get(path);
          if (existing) {
            existing.operations.add(name);
            if (timestamp > existing.lastTimestamp) {
              existing.lastTimestamp = timestamp;
            }
          } else {
            fileMap.set(path, {
              path,
              operations: new Set([name]),
              lastTimestamp: timestamp,
            });
          }
        }
      }

      if (fileMap.size === 0) {
        ctx.ui.notify("No files read/written/edited in this session", "info");
        return;
      }

      // Sort by most recent first
      const files = Array.from(fileMap.values()).toSorted(
        (a, b) => b.lastTimestamp - a.lastTimestamp,
      );

      const openSelected = async (file: FileEntry): Promise<void> => {
        try {
          await pi.exec("code", ["-g", file.path], { cwd: ctx.cwd });
        } catch (error) {
          const message = error instanceof Error ? error.message : String(error);
          ctx.ui.notify(`Failed to open ${file.path}: ${message}`, "error");
        }
      };

      const items = files.map((file) => {
        const ops: string[] = [];
        if (file.operations.has("read")) {
          ops.push("R");
        }
        if (file.operations.has("write")) {
          ops.push("W");
        }
        if (file.operations.has("edit")) {
          ops.push("E");
        }
        return {
          value: file,
          label: `${ops.join("")} ${file.path}`,
        };
      });
      await showPagedSelectList({
        ctx,
        title: " Select file to open",
        items,
        onSelect: (item) => {
          void openSelected(item.value as FileEntry);
        },
      });
    },
  });
}

```

### File: prompt-url-widget.ts
```ts
import {
  DynamicBorder,
  type ExtensionAPI,
  type ExtensionContext,
} from "@mariozechner/pi-coding-agent";
import { Container, Text } from "@mariozechner/pi-tui";

const PR_PROMPT_PATTERN = /^\s*You are given one or more GitHub PR URLs:\s*(\S+)/im;
const ISSUE_PROMPT_PATTERN = /^\s*Analyze GitHub issue\(s\):\s*(\S+)/im;

type PromptMatch = {
  kind: "pr" | "issue";
  url: string;
};

type GhMetadata = {
  title?: string;
  author?: {
    login?: string;
    name?: string | null;
  };
};

function extractPromptMatch(prompt: string): PromptMatch | undefined {
  const prMatch = prompt.match(PR_PROMPT_PATTERN);
  if (prMatch?.[1]) {
    return { kind: "pr", url: prMatch[1].trim() };
  }

  const issueMatch = prompt.match(ISSUE_PROMPT_PATTERN);
  if (issueMatch?.[1]) {
    return { kind: "issue", url: issueMatch[1].trim() };
  }

  return undefined;
}

async function fetchGhMetadata(
  pi: ExtensionAPI,
  kind: PromptMatch["kind"],
  url: string,
): Promise<GhMetadata | undefined> {
  const args =
    kind === "pr"
      ? ["pr", "view", url, "--json", "title,author"]
      : ["issue", "view", url, "--json", "title,author"];

  try {
    const result = await pi.exec("gh", args);
    if (result.code !== 0 || !result.stdout) {
      return undefined;
    }
    return JSON.parse(result.stdout) as GhMetadata;
  } catch {
    return undefined;
  }
}

function formatAuthor(author?: GhMetadata["author"]): string | undefined {
  if (!author) {
    return undefined;
  }
  const name = author.name?.trim();
  const login = author.login?.trim();
  if (name && login) {
    return `${name} (@${login})`;
  }
  if (login) {
    return `@${login}`;
  }
  if (name) {
    return name;
  }
  return undefined;
}

export default function promptUrlWidgetExtension(pi: ExtensionAPI) {
  const setWidget = (
    ctx: ExtensionContext,
    match: PromptMatch,
    title?: string,
    authorText?: string,
  ) => {
    ctx.ui.setWidget("prompt-url", (_tui, thm) => {
      const titleText = title ? thm.fg("accent", title) : thm.fg("accent", match.url);
      const authorLine = authorText ? thm.fg("muted", authorText) : undefined;
      const urlLine = thm.fg("dim", match.url);

      const lines = [titleText];
      if (authorLine) {
        lines.push(authorLine);
      }
      lines.push(urlLine);

      const container = new Container();
      container.addChild(new DynamicBorder((s: string) => thm.fg("muted", s)));
      container.addChild(new Text(lines.join("\n"), 1, 0));
      return container;
    });
  };

  const applySessionName = (ctx: ExtensionContext, match: PromptMatch, title?: string) => {
    const label = match.kind === "pr" ? "PR" : "Issue";
    const trimmedTitle = title?.trim();
    const fallbackName = `${label}: ${match.url}`;
    const desiredName = trimmedTitle ? `${label}: ${trimmedTitle} (${match.url})` : fallbackName;
    const currentName = pi.getSessionName()?.trim();
    if (!currentName) {
      pi.setSessionName(desiredName);
      return;
    }
    if (currentName === match.url || currentName === fallbackName) {
      pi.setSessionName(desiredName);
    }
  };

  const renderPromptMatch = (ctx: ExtensionContext, match: PromptMatch) => {
    setWidget(ctx, match);
    applySessionName(ctx, match);
    void fetchGhMetadata(pi, match.kind, match.url).then((meta) => {
      const title = meta?.title?.trim();
      const authorText = formatAuthor(meta?.author);
      setWidget(ctx, match, title, authorText);
      applySessionName(ctx, match, title);
    });
  };

  pi.on("before_agent_start", async (event, ctx) => {
    if (!ctx.hasUI) {
      return;
    }
    const match = extractPromptMatch(event.prompt);
    if (!match) {
      return;
    }

    renderPromptMatch(ctx, match);
  });

  pi.on("session_switch", async (_event, ctx) => {
    rebuildFromSession(ctx);
  });

  const getUserText = (content: string | { type: string; text?: string }[] | undefined): string => {
    if (!content) {
      return "";
    }
    if (typeof content === "string") {
      return content;
    }
    return (
      content
        .filter((block): block is { type: "text"; text: string } => block.type === "text")
        .map((block) => block.text)
        .join("\n") ?? ""
    );
  };

  const rebuildFromSession = (ctx: ExtensionContext) => {
    if (!ctx.hasUI) {
      return;
    }

    const entries = ctx.sessionManager.getEntries();
    const lastMatch = [...entries].toReversed().find((entry) => {
      if (entry.type !== "message" || entry.message.role !== "user") {
        return false;
      }
      const text = getUserText(entry.message.content);
      return !!extractPromptMatch(text);
    });

    const content =
      lastMatch?.type === "message" && lastMatch.message.role === "user"
        ? lastMatch.message.content
        : undefined;
    const text = getUserText(content);
    const match = text ? extractPromptMatch(text) : undefined;
    if (!match) {
      ctx.ui.setWidget("prompt-url", undefined);
      return;
    }

    renderPromptMatch(ctx, match);
  };

  pi.on("session_start", async (_event, ctx) => {
    rebuildFromSession(ctx);
  });
}

```

### File: redraws.ts
```ts
/**
 * Redraws Extension
 *
 * Exposes /tui to show TUI redraw stats.
 */

import type { ExtensionAPI } from "@mariozechner/pi-coding-agent";
import { Text } from "@mariozechner/pi-tui";

export default function (pi: ExtensionAPI) {
  pi.registerCommand("tui", {
    description: "Show TUI stats",
    handler: async (_args, ctx) => {
      if (!ctx.hasUI) {
        return;
      }
      let redraws = 0;
      await ctx.ui.custom<void>((tui, _theme, _keybindings, done) => {
        redraws = tui.fullRedraws;
        done(undefined);
        return new Text("", 0, 0);
      });
      ctx.ui.notify(`TUI full redraws: ${redraws}`, "info");
    },
  });
}

```

### File: ui_DISTILLED.md
```md
---
id: ui
type: distilled_knowledge
---
# ui

## SWALLOW ENGINE DISTILLATION

### File: paged-select.ts
```ts
import { DynamicBorder } from "@mariozechner/pi-coding-agent";
import {
  Container,
  Key,
  matchesKey,
  type SelectItem,
  SelectList,
  Text,
} from "@mariozechner/pi-tui";

type CustomUiContext = {
  ui: {
    custom: <T>(
      render: (
        tui: { requestRender: () => void },
        theme: {
          fg: (tone: string, text: string) => string;
          bold: (text: string) => string;
        },
        kb: unknown,
        done: () => void,
      ) => {
        render: (width: number) => string;
        invalidate: () => void;
        handleInput: (data: string) => void;
      },
    ) => Promise<T>;
  };
};

export async function showPagedSelectList(params: {
  ctx: CustomUiContext;
  title: string;
  items: SelectItem[];
  onSelect: (item: SelectItem) => void;
}): Promise<void> {
  await params.ctx.ui.custom<void>((tui, theme, _kb, done) => {
    const container = new Container();

    container.addChild(new DynamicBorder((s: string) => theme.fg("accent", s)));
    container.addChild(new Text(theme.fg("accent", theme.bold(params.title)), 0, 0));

    const visibleRows = Math.min(params.items.length, 15);
    let currentIndex = 0;

    const selectList = new SelectList(params.items, visibleRo
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

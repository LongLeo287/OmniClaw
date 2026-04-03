---
id: vercel-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:40.534351
---

# KNOWLEDGE EXTRACT: vercel
> **Extracted on:** 2026-03-30 17:58:08
> **Source:** vercel

---

## File: `ai.md`
```markdown
# 📦 vercel/ai [🔖 PENDING/APPROVE]
🔗 https://github.com/vercel/ai
🌐 https://ai-sdk.dev

## Meta
- **Stars:** ⭐ 23015 | **Forks:** 🍴 4059
- **Language:** TypeScript | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The AI Toolkit for TypeScript. From the creators of Next.js, the AI SDK is a free open-source library for building AI-powered applications and agents 

## README (trích đầu)
```
![hero illustration](./assets/hero.gif)

# AI SDK

The [AI SDK](https://ai-sdk.dev/docs) is a provider-agnostic TypeScript toolkit designed to help you build AI-powered applications and agents using popular UI frameworks like Next.js, React, Svelte, Vue, Angular, and runtimes like Node.js.

To learn more about how to use the AI SDK, check out our [API Reference](https://ai-sdk.dev/docs/reference) and [Documentation](https://ai-sdk.dev/docs).

## Installation

You will need Node.js 18+ and npm (or another package manager) installed on your local development machine.

```shell
npm install ai
```

## Skill for Coding Agents

If you use coding agents such as Claude Code or Cursor, we highly recommend adding the AI SDK skill to your repository:

```shell
npx skills add vercel/ai
```

## Unified Provider Architecture

The AI SDK provides a [unified API](https://ai-sdk.dev/docs/foundations/providers-and-models) to interact with model providers like [OpenAI](https://ai-sdk.dev/providers/ai-sdk-providers/openai), [Anthropic](https://ai-sdk.dev/providers/ai-sdk-providers/anthropic), [Google](https://ai-sdk.dev/providers/ai-sdk-providers/google-generative-ai), and [more](https://ai-sdk.dev/providers/ai-sdk-providers).

By default, the AI SDK uses the [Vercel AI Gateway](https://vercel.com/docs/ai-gateway) to give you access to all major providers out of the box. Just pass a model string for any supported model:

```ts
const result = await generateText({
  model: 'anthropic/claude-opus-4.6', // or 'openai/gpt-5.4', 'google/gemini-3-flash', etc.
  prompt: 'Hello!',
});
```

You can also connect to providers directly using their SDK packages:

```shell
npm install @ai-sdk/openai @ai-sdk/anthropic @ai-sdk/google
```

```ts
import { anthropic } from '@ai-sdk/anthropic';

const result = await generateText({
  model: anthropic('claude-opus-4-6'), // or openai('gpt-5.4'), google('gemini-3-flash'), etc.
  prompt: 'Hello!',
});
```

## Usage

### Generating Text

```ts
import { generateText } from 'ai';

const { text } = await generateText({
  model: 'openai/gpt-5.4', // use Vercel AI Gateway
  prompt: 'What is an agent?',
});
```

### Generating Structured Data

```ts
import { generateText, Output } from 'ai';
import { z } from 'zod';

const { output } = await generateText({
  model: 'openai/gpt-5.4',
  output: Output.object({
    schema: z.object({
      recipe: z.object({
        name: z.string(),
        ingredients: z.array(
          z.object({ name: z.string(), amount: z.string() }),
        ),
        steps: z.array(z.string()),
      }),
    }),
  }),
  prompt: 'Generate a lasagna recipe.',
});
```

### Agents

```ts
import { ToolLoopAgent } from 'ai';

const sandboxAgent = new ToolLoopAgent({
  model: 'openai/gpt-5.4',
  system: 'You are an agent with access to a shell environment.',
  tools: {
    shell: openai.tools.localShell({
      execute: async ({ action }) => {
        const [cmd, ...args] = action.command;
        const sandbox = await getSandbox()
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `chat.md`
```markdown
# 📦 vercel/chat [🔖 PENDING/APPROVE]
🔗 https://github.com/vercel/chat
🌐 https://chat-sdk.dev/

## Meta
- **Stars:** ⭐ 1560 | **Forks:** 🍴 134
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A unified TypeScript SDK for building chat bots across Slack, Microsoft Teams, Google Chat, Discord, and more.

## README (trích đầu)
```
# Chat SDK

[![npm version](https://img.shields.io/npm/v/chat)](https://www.npmjs.com/package/chat)
[![npm downloads](https://img.shields.io/npm/dm/chat)](https://www.npmjs.com/package/chat)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A unified TypeScript SDK for building chat bots across Slack, Microsoft Teams, Google Chat, Discord, Telegram, GitHub, Linear, and WhatsApp. Write your bot logic once, deploy everywhere.

## Installation

```bash
npm install chat
```

Install adapters for your platforms:

```bash
npm install @chat-adapter/slack @chat-adapter/teams @chat-adapter/gchat @chat-adapter/discord @chat-adapter/telegram
```

## Usage

```typescript
import { Chat } from "chat";
import { createSlackAdapter } from "@chat-adapter/slack";
import { createRedisState } from "@chat-adapter/state-redis";

const bot = new Chat({
  userName: "mybot",
  adapters: {
    slack: createSlackAdapter(),
  },
  state: createRedisState(),
});

bot.onNewMention(async (thread) => {
  await thread.subscribe();
  await thread.post("Hello! I'm listening to this thread.");
});

bot.onSubscribedMessage(async (thread, message) => {
  await thread.post(`You said: ${message.text}`);
});
```

See the [Getting Started guide](https://chat-sdk.dev/docs/getting-started) for a full walkthrough.

## Supported platforms

| Platform | Package | Mentions | Reactions | Cards | Modals | Streaming | DMs |
|----------|---------|----------|-----------|-------|--------|-----------|-----|
| Slack | `@chat-adapter/slack` | Yes | Yes | Yes | Yes | Native | Yes |
| Microsoft Teams | `@chat-adapter/teams` | Yes | Read-only | Yes | No | Post+Edit | Yes |
| Google Chat | `@chat-adapter/gchat` | Yes | Yes | Yes | No | Post+Edit | Yes |
| Discord | `@chat-adapter/discord` | Yes | Yes | Yes | No | Post+Edit | Yes |
| Telegram | `@chat-adapter/telegram` | Yes | Yes | Partial | No | Post+Edit | Yes |
| GitHub | `@chat-adapter/github` | Yes | Yes | No | No | No | No |
| Linear | `@chat-adapter/linear` | Yes | Yes | No | No | No | No |
| WhatsApp | `@chat-adapter/whatsapp` | N/A | Yes | Partial | No | No | Yes |

## Features

- [**Event handlers**](https://chat-sdk.dev/docs/usage) — mentions, messages, reactions, button clicks, slash commands, modals
- [**AI streaming**](https://chat-sdk.dev/docs/streaming) — stream LLM responses with native Slack streaming and post+edit fallback
- [**Cards**](https://chat-sdk.dev/docs/cards) — JSX-based interactive cards (Block Kit, Adaptive Cards, Google Chat Cards)
- [**Actions**](https://chat-sdk.dev/docs/actions) — handle button clicks and dropdown selections
- [**Modals**](https://chat-sdk.dev/docs/modals) — form dialogs with text inputs, dropdowns, and validation
- [**Slash commands**](https://chat-sdk.dev/docs/slash-commands) — handle `/command` invocations
- [**Emoji**](https://chat-sdk.dev/docs/emoji) — type-safe, cross-platform emoji with custom emoji support
- [**File uploads**](https://chat-sd
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `next.js.md`
```markdown
# 📦 vercel/next.js [🔖 PENDING]
🔗 https://github.com/vercel/next.js
🌐 https://nextjs.org

## Meta
- **Stars:** ⭐ 138494 | **Forks:** 🍴 30705
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
The React Framework

## README (trích đầu)
```
<div align="center">
  <a href="https://nextjs.org">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://assets.vercel.com/image/upload/v1662130559/nextjs/Icon_dark_background.png">
      <img alt="Next.js logo" src="https://assets.vercel.com/image/upload/v1662130559/nextjs/Icon_light_background.png" height="128">
    </picture>
  </a>
  <h1>Next.js</h1>

<a href="https://vercel.com"><img alt="Vercel logo" src="https://img.shields.io/badge/MADE%20BY%20Vercel-000000.svg?style=for-the-badge&logo=Vercel&labelColor=000"></a>
<a href="https://www.npmjs.com/package/next"><img alt="NPM version" src="https://img.shields.io/npm/v/next.svg?style=for-the-badge&labelColor=000000"></a>
<a href="https://github.com/vercel/next.js/blob/canary/license.md"><img alt="License" src="https://img.shields.io/npm/l/next.svg?style=for-the-badge&labelColor=000000"></a>
<a href="https://github.com/vercel/next.js/discussions"><img alt="Join the community on GitHub" src="https://img.shields.io/badge/Join%20the%20community-blueviolet.svg?style=for-the-badge&logo=Next.js&labelColor=000000&logoWidth=20"></a>

</div>

## Getting Started

Used by some of the world's largest companies, Next.js enables you to create full-stack web applications by extending the latest React features, and integrating powerful Rust-based JavaScript tooling for the fastest builds.

- Visit our [Learn Next.js](https://nextjs.org/learn) course to get started with Next.js.
- Visit the [Next.js Showcase](https://nextjs.org/showcase) to see more sites built with Next.js.

## Documentation

Visit [https://nextjs.org/docs](https://nextjs.org/docs) to view the full documentation.

## Community

The Next.js community can be found on [GitHub Discussions](https://github.com/vercel/next.js/discussions) where you can ask questions, voice ideas, and share your projects with other people.

To chat with other community members you can join the Next.js [Discord](https://nextjs.org/discord) server.

Do note that our [Code of Conduct](https://github.com/vercel/next.js/blob/canary/CODE_OF_CONDUCT.md) applies to all Next.js community channels. Users are **highly encouraged** to read and adhere to it to avoid repercussions.

## Contributing

Contributions to Next.js are welcome and highly appreciated. However, before you jump right into it, we would like you to review our [Contribution Guidelines](/contributing.md) to make sure you have a smooth experience contributing to Next.js.

### Good First Issues:

We have a list of **[good first issues](https://github.com/vercel/next.js/labels/good%20first%20issue)** that contain bugs that have a relatively limited scope. This is a great place for newcomers and beginners alike to get started, gain experience, and get familiar with our contribution process.

---
## Security

If you believe you have found a security vulnerability in Next.js, we encourage you to **_responsibly disclose this and NOT open a public issue_**.

To participate in our Open Source S
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `turborepo.md`
```markdown
# 📦 vercel/turborepo [🔖 PENDING/APPROVE]
🔗 https://github.com/vercel/turborepo
🌐 https://turborepo.dev

## Meta
- **Stars:** ⭐ 30066 | **Forks:** 🍴 2307
- **Language:** Rust | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Build system optimized for JavaScript and TypeScript, written in Rust

## README (trích đầu)
```
<p align="center">
  <a href="https://turborepo.dev">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/4060187/196936123-f6e1db90-784d-4174-b774-92502b718836.png">
      <img src="https://user-images.githubusercontent.com/4060187/196936104-5797972c-ab10-4834-bd61-0d1e5f442c9c.png" height="128">
    </picture>
    <h1 align="center">Turborepo</h1>
  </a>
</p>

<p align="center">
  <a aria-label="Vercel logo" href="https://vercel.com/"><img src="https://img.shields.io/badge/MADE%20BY%20Vercel-000000.svg?style=for-the-badge&logo=Vercel&labelColor=000"></a>
  <a aria-label="NPM version" href="https://www.npmjs.com/package/turbo"><img alt="" src="https://img.shields.io/npm/v/turbo.svg?style=for-the-badge&labelColor=000000"></a>
  <a aria-label="License" href="https://github.com/vercel/turborepo/blob/main/LICENSE"><img alt="" src="https://img.shields.io/npm/l/turbo.svg?style=for-the-badge&labelColor=000000&color="></a>
  <a aria-label="Join the community on GitHub" href="https://github.com/vercel/turborepo/discussions"><img alt="" src="https://img.shields.io/badge/Join%20the%20community-blueviolet.svg?style=for-the-badge&logo=turborepo&labelColor=000000&logoWidth=20&logoColor=white"></a>
</p>

Turborepo is a high-performance build system for JavaScript and TypeScript codebases, written in Rust.

## Getting Started

Visit https://turborepo.dev to get started with Turborepo.

## Contributing

See [CONTRIBUTING.md](https://github.com/vercel/turborepo/blob/main/CONTRIBUTING.md) for more information.

## Community

The Turborepo community can be found on [GitHub Discussions](https://github.com/vercel/turborepo/discussions), where you can ask questions, voice ideas, and share your projects.

To chat with other community members, you can join [Vercel Community's `#turborepo` tag](https://vercel.community/tag/turborepo).

Our [Code of Conduct](https://github.com/vercel/turborepo/blob/main/CODE_OF_CONDUCT.md) applies to all Turborepo community channels.

## Who is using Turborepo?

Turborepo is used by the world's leading companies. Check out the [Turborepo Showcase](https://turborepo.dev/showcase) to learn more.

## Updates

Follow [@turborepo](https://x.com/turborepo) on X for project updates.

## Security

If you believe you have found a security vulnerability in Turborepo, we encourage you to responsibly disclose this and not open a public issue. We will investigate all legitimate reports. Email `security@vercel.com` to disclose any security vulnerabilities.

https://vercel.com/security

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


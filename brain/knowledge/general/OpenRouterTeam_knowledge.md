---
id: openrouterteam-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:16.846703
---

# KNOWLEDGE EXTRACT: OpenRouterTeam
> **Extracted on:** 2026-03-30 17:50:27
> **Source:** OpenRouterTeam

---

## File: `ai-sdk-provider.md`
```markdown
# 📦 OpenRouterTeam/ai-sdk-provider [🔖 PENDING/APPROVE]
🔗 https://github.com/OpenRouterTeam/ai-sdk-provider
🌐 https://www.npmjs.com/package/@openrouter/ai-sdk-provider

## Meta
- **Stars:** ⭐ 613 | **Forks:** 🍴 138
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The OpenRouter provider for the Vercel AI SDK contains support for hundreds of models through the OpenRouter chat and completion APIs.

## README (trích đầu)
```
# OpenRouter Provider for Vercel AI SDK

The [OpenRouter](https://openrouter.ai/) provider for the [Vercel AI SDK](https://sdk.vercel.ai/docs) gives access to over 300 large language models on the OpenRouter chat and completion APIs.

## Setup for AI SDK v6

```bash
# For pnpm
pnpm add @openrouter/ai-sdk-provider

# For npm
npm install @openrouter/ai-sdk-provider

# For yarn
yarn add @openrouter/ai-sdk-provider
```

## (LEGACY) Setup for AI SDK v5

```bash
# For pnpm
pnpm add @openrouter/ai-sdk-provider@1.5.4

# For npm
npm install @openrouter/ai-sdk-provider@1.5.4

# For yarn
yarn add @openrouter/ai-sdk-provider@1.5.4
```

## Provider Instance

You can import the default provider instance `openrouter` from `@openrouter/ai-sdk-provider`:

```ts
import { openrouter } from '@openrouter/ai-sdk-provider';
```

## Example

```ts
import { openrouter } from '@openrouter/ai-sdk-provider';
import { generateText } from 'ai';

const { text } = await generateText({
  model: openrouter('openai/gpt-4o'),
  prompt: 'Write a vegetarian lasagna recipe for 4 people.',
});
```

## Supported models

This list is not a definitive list of models supported by OpenRouter, as it constantly changes as we add new models (and deprecate old ones) to our system. You can find the latest list of models supported by OpenRouter [here](https://openrouter.ai/models).

You can find the latest list of tool-supported models supported by OpenRouter [here](https://openrouter.ai/models?order=newest&supported_parameters=tools). (Note: This list may contain models that are not compatible with the AI SDK.)

## Embeddings

OpenRouter supports embedding models for semantic search, RAG pipelines, and vector-native features.

### Basic Usage

```ts
import { embed } from 'ai';
import { openrouter } from '@openrouter/ai-sdk-provider';

const { embedding } = await embed({
  model: openrouter.textEmbeddingModel('openai/text-embedding-3-small'),
  value: 'sunny day at the beach',
});

console.log(embedding); // Array of numbers representing the embedding
```

### Batch Embeddings

```ts
import { embedMany } from 'ai';
import { openrouter } from '@openrouter/ai-sdk-provider';

const { embeddings } = await embedMany({
  model: openrouter.textEmbeddingModel('openai/text-embedding-3-small'),
  values: [
    'sunny day at the beach',
    'rainy day in the city',
    'snowy mountain peak',
  ],
});

console.log(embeddings); // Array of embedding arrays
```

### Supported Embedding Models

OpenRouter supports various embedding models including:
- `openai/text-embedding-3-small`
- `openai/text-embedding-3-large`
- `openai/text-embedding-ada-002`
- And more available on [OpenRouter](https://openrouter.ai/models?output_modalities=embeddings)

## Passing Extra Body to OpenRouter

There are 3 ways to pass extra body to OpenRouter:

1. Via the `providerOptions.openrouter` property:

   ```typescript
   import { createOpenRouter } from '@openrouter/ai-sdk-provider';
   import { streamText } from 'ai';

   const o
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


---
id: voltagent
type: knowledge
owner: OA_Triage
---
# voltagent
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "voltagent",
  "description": "Backend framework with a monorepo structure using pnpm and lerna",
  "version": "0.1.0",
  "author": "",
  "devDependencies": {
    "@arethetypeswrong/cli": "^0.17.4",
    "@biomejs/biome": "^1.9.4",
    "@changesets/changelog-github": "^0.5.1",
    "@changesets/cli": "^2.28.1",
    "@commitlint/cli": "^18.2.0",
    "@commitlint/config-conventional": "^18.2.0",
    "@esbuild-plugins/node-resolve": "^0.2.2",
    "@nx/devkit": "^21.2.0",
    "@nx/js": "20.4.6",
    "@nx/plugin": "20.4.6",
    "@nx/vite": "20.4.6",
    "@nx/web": "20.4.6",
    "@swc-node/register": "~1.9.1",
    "@swc/cli": "~0.3.12",
    "@swc/core": "~1.5.7",
    "@swc/helpers": "~0.5.11",
    "@types/node": "^24.2.1",
    "@vitest/coverage-v8": "^3.2.4",
    "@vitest/ui": "^1.3.1",
    "husky": "^8.0.3",
    "jsdom": "~22.1.0",
    "lerna": "^7.4.2",
    "lint-staged": "^15.4.3",
    "nx": "^20.4.6",
    "prettier": "^3.5.3",
    "publint": "^0.3.8",
    "rimraf": "^5.0.5",
    "syncpack": "^13.0.2",
    "tslib": "^2.3.0",
    "tsup": "^8.5.0",
    "typescript": "^5.8.2",
    "vite": "^7.2.7",
    "vitest": "^3.2.4"
  },
  "engines": {
    "node": ">=20",
    "pnpm": ">=8"
  },
  "license": "MIT",
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "biome check --write --no-errors-on-unmatched"
    ],
    "*.{md,mdx}": [
      "prettier --config ./.prettierrc --write"
    ]
  },
  "nx": {},
  "packageManager": "pnpm@8.10.5",
  "private": true,
  "repository": "VoltAgent/voltagent.git",
  "scripts": {
    "archive:deprecated": "node scripts/archive-deprecated.js",
    "attw": "lerna run attw --scope @voltagent/*",
    "attw:all": "lerna run attw --scope @voltagent/*",
    "biome": "biome",
    "bootstrap": "lerna bootstrap",
    "build": "lerna run build --ignore @voltagent/vercel-ai-exporter",
    "build:all": "lerna run build --scope @voltagent/* --ignore @voltagent/vercel-ai-exporter --scope create-voltagent-app --concurrency 1",
    "build:example": "lerna run build --scope voltagent-basic-example",
    "changeset": "changeset",
    "clean": "lerna run clean && lerna clean --yes && rimraf node_modules",
    "coffee": "pnpm nuke && pnpm i && pnpm build:all",
    "dev": "lerna run dev --ignore voltagent-example-*",
    "format": "prettier --write \"**/*.{ts,tsx,md}\"",
    "lint": "biome check .",
    "lint:ci": "biome ci .",
    "lint:error": "biome check . --diagnostic-level error",
    "lint:fix": "biome check . --write",
    "lint:staged": "lint-staged",
    "nuke": "echo 'Removing all node_modules, builds and lockfiles' && pnpm nuke:node_modules && pnpm nuke:builds && pnpm nuke:lockfiles",
    "nuke:builds": "lerna exec -- rimraf dist && lerna exec -- rimraf build",
    "nuke:lockfiles": "lerna exec -- rimraf package-lock.json && lerna exec -- rimraf yarn.lock && lerna exec -- rimraf pnpm-lock.yaml",
    "nuke:node_modules": "lerna clean --yes && rimraf node_modules",
    "nx": "nx",
    "prepare": "husky install",
    "prerelease:enter": "pnpm changeset pre enter next",
    "prerelease:exit": "pnpm changeset pre exit",
    "prerelease:publish": "pnpm build && pnpm changeset publish",
    "prerelease:version": "pnpm changeset version",
    "prerelease:version-packages": "pnpm changeset version && pnpm i --ignore-scripts --lockfile-only --no-frozen-lockfile --reporter=ndjson --stream && git add pnpm-lock.yaml",
    "publint": "lerna run publint --scope @voltagent/core",
    "publint:all": "lerna run publint --scope @voltagent/*",
    "publish": "lerna publish",
    "sp": "syncpack",
    "start": "lerna run start",
    "sync:docs-mcp": "node scripts/sync-docs-mcp.js",
    "test": "lerna run test --stream",
    "test:all": "lerna run test --stream --scope @voltagent/*",
    "test:all:coverage": "pnpm test:all -- -- --coverage",
    "test:coverage": "pnpm test -- -- --coverage",
    "version-packages": "pnpm changeset version && pnpm i --ignore-scripts --lockfile-only --no-frozen-lockfile --reporter=ndjson --stream && git add pnpm-lock.yaml"
  },
  "workspaces": [
    "packages/*",
    "examples/*",
    "examples/*/client",
    "examples/*/server"
  ]
}

```

### File: README.md
```md
<div align="center">
<a href="https://voltagent.dev/">
<img width="1500" height="276" alt="voltagent" src="https://github.com/user-attachments/assets/d9ad69bd-b905-42a3-81af-99a0581348c0" />
</a>

<h3 align="center">
AI Agent Engineering Platform
</h3>

<div align="center">
English | <a href="i18n/README-cn-traditional.md">繁體中文</a> | <a href="i18n/README-cn-bsc.md">简体中文</a> | <a href="i18n/README-jp.md">日本語</a> | <a href="i18n/README-kr.md">한국어</a>
</div>

<br/>

<div align="center">
    <a href="https://voltagent.dev">Home Page</a> |
    <a href="https://voltagent.dev/docs/">Documentation</a> |
    <a href="https://github.com/voltagent/voltagent/tree/main/examples">Examples</a> 
</div>
</div>

<br/>

<div align="center">

[![GitHub issues](https://img.shields.io/github/issues/voltagent/voltagent)](https://github.com/voltagent/voltagent/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/voltagent/voltagent)](https://github.com/voltagent/voltagent/pulls)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![npm version](https://img.shields.io/npm/v/@voltagent/core.svg)](https://www.npmjs.com/package/@voltagent/core)

[![npm downloads](https://img.shields.io/npm/dm/@voltagent/core.svg)](https://www.npmjs.com/package/@voltagent/core)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)
[![Twitter Follow](https://img.shields.io/twitter/follow/voltagent_dev?style=social)](https://x.com/voltagent_dev)

</div>

<h3 align="center">
⭐ Like what we're doing? Give us a star ⬆️
</h3>

VoltAgent is an end-to-end AI Agent Engineering Platform that consists of two main parts:

- **[Open-Source TypeScript Framework](#core-framework)** – Memory, RAG, Guardrails, Tools, MCP, Voice, Workflow, and more.
- **[VoltOps Console](#voltops-console)** `Cloud` `Self-Hosted` – Observability, Automation, Deployment, Evals, Guardrails, Prompts, and more.

Build agents with full code control and ship them with production-ready visibility and operations.

<h2 id="core-framework">Core TypeScript Framework</h2>

With the open-source framework, you can build intelligent agents with memory, tools, and multi-step workflows while connecting to any AI provider. Create sophisticated multi-agent systems where specialized agents work together under supervisor coordination.

- **[Core Runtime](https://voltagent.dev/docs/agents/overview/) (`@voltagent/core`)**: Define agents with typed roles, tools, memory, and model providers in one place so everything stays organized.
- **[Workflow Engine](https://voltagent.dev/docs/workflows/overview/)**: Describe multi-step automations declaratively rather than stitching together custom control flow.
- **[Supervisors & Sub-Agents](https://voltagent.dev/docs/agents/sub-agents/)**: Run teams of specialized agents under a supervisor runtime that routes tasks and keeps them in sync.
- **[Tool Registry](https://voltagent.dev/docs/agents/tools/) & [MCP](https://voltagent.dev/docs/agents/mcp/)**: Ship Zod-typed tools with lifecycle hooks and cancellation, and connect to [Model Context Protocol](https://modelcontextprotocol.io/) servers without extra glue code.
- **[LLM Compatibility](https://voltagent.dev/docs/getting-started/providers-models/)**: Swap between OpenAI, Anthropic, Google, or other providers by changing config, not rewriting agent logic.
- **[Memory](https://voltagent.dev/docs/agents/memory/overview/)**: Attach durable memory adapters so agents remember important context across runs.
- **[Resumable Streaming](https://voltagent.dev/docs/agents/resumable-streaming/)**: Let clients reconnect to in-flight streams after refresh and continue receiving the same response.
- **[Retrieval & RAG](https://voltagent.dev/docs/rag/overview/)**: Plug in retriever agents to pull facts from your data sources and ground responses (RAG) before the model answers.
- **[VoltAgent Knowledge Base](https://voltagent.dev/docs/rag/voltagent/)**: Use the managed RAG service for document ingestion, chunking, embeddings, and search.
- **[Voice](https://voltagent.dev/docs/agents/voice/)**: Add text-to-speech and speech-to-text capabilities with OpenAI, ElevenLabs, or custom voice providers.
- **[Guardrails](https://voltagent.dev/docs/guardrails/overview/)**: Intercept and validate agent input or output at runtime to enforce content policies and safety rules.
- **[Evals](https://voltagent.dev/docs/evals/overview/)**: Run agent eval suites alongside your workflows to measure and improve agent behavior.

#### MCP Server (@voltagent/mcp-docs-server)

You can use the MCP server `@voltagent/mcp-docs-server` to teach your LLM how to use VoltAgent for AI-powered coding assistants like Claude, Cursor, or Windsurf. This allows AI assistants to access VoltAgent documentation, examples, and changelogs directly while you code.

📖 [How to setup MCP docs server](https://voltagent.dev/docs/getting-started/mcp-docs-server/)

## ⚡ Quick Start

Create a new VoltAgent project in seconds using the `create-voltagent-app` CLI tool:

```bash
npm create voltagent-app@latest
```

This command guides you through setup.

You'll see the starter code in `src/index.ts`, which now registers both an agent and a comprehensive workflow example found in `src/workflows/index.ts`.

```typescript
import { VoltAgent, Agent, Memory } from "@voltagent/core";
import { LibSQLMemoryAdapter } from "@voltagent/libsql";
import { createPinoLogger } from "@voltagent/logger";
import { honoServer } from "@voltagent/server-hono";
import { openai } from "@ai-sdk/openai";
import { expenseApprovalWorkflow } from "./workflows";
import { weatherTool } from "./tools";

// Create a logger instance
const logger = createPinoLogger({
  name: "my-agent-app",
  level: "info",
});

// Optional persistent memory (remove to use default in-memory)
const memory = new Memory({
  storage: new LibSQLMemoryAdapter({ url: "file:./.voltagent/memory.db" }),
});

// A simple, general-purpose agent for the project.
const agent = new Agent({
  name: "my-agent",
  instructions: "A helpful assistant that can check weather and help with various tasks",
  model: openai("gpt-4o-mini"),
  tools: [weatherTool],
  memory,
});

// Initialize VoltAgent with your agent(s) and workflow(s)
new VoltAgent({
  agents: {
    agent,
  },
  workflows: {
    expenseApprovalWorkflow,
  },
  server: honoServer(),
  logger,
});
```

Afterwards, navigate to your project and run:

```bash
npm run dev
```

When you run the dev command, tsx will compile and run your code. You should see the VoltAgent server startup message in your terminal:

```
══════════════════════════════════════════════════
VOLTAGENT SERVER STARTED SUCCESSFULLY
══════════════════════════════════════════════════
✓ HTTP Server: http://localhost:3141

Test your agents with VoltOps Console: https://console.voltagent.dev
══════════════════════════════════════════════════
```

Your agent is now running! To interact with it:

1. Open the Console: Click the [VoltOps LLM Observability Platform](https://console.voltagent.dev) link in your terminal output (or copy-paste it into your browser).
2. Find Your Agent: On the VoltOps LLM Observability Platform page, you should see your agent listed (e.g., "my-agent").
3. Open Agent Details: Click on your agent's name.
4. Start Chatting: On the agent detail page, click the chat icon in the bottom right corner to open the chat window.
5. Send a Message: Type a message like "Hello" and press Enter.

[![VoltAgent Demo](thumbnail.png)](https://github.com/user-attachments/assets/26340c6a-be34-48a5-9006-e822bf6098a7)

### Running Your First Workflow

Your new project also includes a powerful workflow engine.

The expense approval workflow demonstrates human-in-the-loop automation with suspend/resume capabilities:

```typescript
import { createWorkflowChain } from "@voltagent/core";
import { z } from "zod";

export const expenseApprovalWorkflow = createWorkflowChain({
  id: "expense-approval",
  name: "Expense Approval Workflow",
  purpose: "Process expense reports with manager approval for high amounts",

  input: z.object({
    employeeId: z.string(),
    amount: z.number(),
    category: z.string(),
    description: z.string(),
  }),
  result: z.object({
    status: z.enum(["approved", "rejected"]),
    approvedBy: z.string(),
    finalAmount: z.number(),
  }),
})
  // Step 1: Validate expense and check if approval needed
  .andThen({
    id: "check-approval-needed",
    resumeSchema: z.object({
      approved: z.boolean(),
      managerId: z.string(),
      comments: z.string().optional(),
      adjustedAmount: z.number().optional(),
    }),
    execute: async ({ data, suspend, resumeData }) => {
      // If we're resuming with manager's decision
      if (resumeData) {
        return {
          ...data,
          approved: resumeData.approved,
          approvedBy: resumeData.managerId,
          finalAmount: resumeData.adjustedAmount || data.amount,
        };
      }

      // Check if manager approval is needed (expenses over $500)
      if (data.amount > 500) {
        await suspend("Manager approval required", {
          employeeId: data.employeeId,
          requestedAmount: data.amount,
        });
      }

      // Auto-approve small expenses
      return {
        ...data,
        approved: true,
        approvedBy: "system",
        finalAmount: data.amount,
      };
    },
  })
  // Step 2: Process the final decision
  .andThen({
    id: "process-decision",
    execute: async ({ data }) => {
      return {
        status: data.approved ? "approved" : "rejected",
        approvedBy: data.approvedBy,
        finalAmount: data.finalAmount,
      };
    },
  });
```

You can test the pre-built `expenseApprovalWorkflow` directly from the VoltOps console:

[![expense-approval](thumbnail.png)](https://github.com/user-attachments/assets/3d3ea67b-4ab5-4dc0-932d-cedd92894b18)

1.  **Go to the Workflows Page:** After starting your server, go directly to the [Workflows page](https://console.voltagent.dev/workflows).
2.  **Select Your Project:** Use the project selector to choose your project (e.g., "my-agent-app").
3.  **Find and Run:** You will see **"Expense Approval Workflow"** listed. Click it, then click the **"Run"** button.
4.  **Provide Input:** The workflow expects a JSON object with expense details. Try a small expense for automatic approval:
    ```json
    {
      "employeeId": "EMP-123",
      "amount": 250,
      "category": "office-supplies",
      "description": "New laptop mouse and keyboard"
    }
    ```
5.  **View the Results:** After execution, you can inspect the detailed logs for each step and see the final output directly in the console.

## Examples

For more examples, visit our [examples repository](https://github.com/VoltAgent/voltagent/tree/main/examples).

- **[Airtable Agent](https://voltagent.dev/examples/guides/airtable-agent)** - React to new records and write updates back into Airtable with VoltOps actions.
- **[Slack Agent](https://voltagent.dev/examples/guides/slack-agent)** - Respond to channel messages and reply via VoltOps Slack actions.
- **[ChatGPT App With VoltAgent](https://voltagent.dev/examples/agents/chatgpt-app)** - Deploy VoltAgent over MCP and connect to ChatGPT Apps.
- **[WhatsApp Order Agent](https://voltagent.dev/examples/agents/whatsapp-ai-agent)** - Build a WhatsApp chatbot that handles food orders through natural conversation. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-whatsapp))
- **[YouTube to Blog Agent](https://voltagent.dev/examples/agents/youtube-blog-agent)** - Convert YouTube videos into Markdown blog posts using a supervisor agent with MCP tools. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-youtube-to-blog))
- **[AI Ads Generator Agent](https://voltagent.dev/examples/agents/ai-instagram-ad-agent)** - Generate Instagram ads using BrowserBase Stagehand and Google Gemini AI. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-ad-creator))
- **[AI Recipe Generator Agent](https://voltagent.dev/examples/agents/recipe-generator)** - Create personalized cooking suggestions based on ingredients and preferences. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-recipe-generator) | [Video](https://youtu.be/KjV1c6AhlfY))
- **[AI Research Assistant Agent](https://voltagent.dev/examples/agents/research-assistant)** - Multi-agent research workflow for generating comprehensive reports. ([Source](https://github.com/VoltAgent/voltagent/tree/main/examples/with-research-assistant) | [Video](https://youtu.be/j6KAUaoZMy4))

<h2 id="voltops-console">VoltOps Console: LLM Observability - Automation - Deployment</h2>

VoltOps Console is the platform side of VoltAgent, providing observability, automation, and deployment so you can monitor and debug agents in production with real-time execution traces, performance metrics, and visual dashboards.

🎬 [Try Live Demo](https://console.voltagent.dev/demo)

📖 [VoltOps Documentation](https://voltagent.dev/voltops-llm-observability-docs/)

🚀 [VoltOps Platform](https://voltagent.dev/voltops-llm-observability/)

### Observability & Tracing

Deep dive into agent execution flow with detailed traces and performance metrics.

<img alt="1" src="https://github.com/user-attachments/assets/21c6d05d-f333-4c61-9218-8862d16110fd" />

### Dashboard

Get a comprehensive overview of all your agents, workflows, and system performance metrics.

<img alt="dashboar" src="https://github.com/user-attachments/assets/c88a5543-219e-4cf0-8f41-14a68ca297fb" />

### Logs

Track detailed execution logs for every agent interaction and workflow step.

![VoltOps Logs](https://cdn.voltagent.dev/console/logs.png)

### Memory Management

Inspect and manage agent memory, context, and conversation history.

![VoltOps Memory Overview](https://cdn.voltagent.dev/console/memory.png)

### Traces

Analyze complete execution traces to understand agent behavior and optimize performance.

![VoltOps Traces](https://cdn.voltagent.dev/console/traces.png)

### Prompt Builder

Design, test, and refine prompts directly in the console.

<img  alt="prompts" src="https://github.com/user-attachments/assets/fb6d71eb-8f81-4443-a494-08c33ec9bcc4" />

### Deployment

Deploy your agents to production with one-click GitHub integration and managed infrastructure.

<img alt="deployment" src="https://github.com/user-attachments/assets/e329ab4b-7464-435a-96cc-90214e8a3cfa" />

📖 [VoltOps Deploy Documentation](https://voltagent.dev/docs/deployment/voltops/)

### Triggers & Actions

Automate agent workflows with webhooks, schedules, and custom triggers to react to external events.

<img width="1277"  alt="triggers" src="https://git
... [TRUNCATED]
```

### File: .changeset\README.md
```md
# Changesets

Hello and welcome! This folder has been automatically generated by `@changesets/cli`, a build tool that works
with multi-package repos, or single-package repos to help you version and publish your code. You can
find the full documentation for it [in our repository](https://github.com/changesets/changesets)

We have a quick list of common questions to get you started engaging with this project in
[our documentation](https://github.com/changesets/changesets/blob/main/docs/common-questions.md)

```

### File: examples\README.md
```md
# VoltAgent AI Agent Examples

Discover end‑to‑end, runnable examples that show how to build real AI agents with VoltAgent. These projects demonstrate core patterns such as RAG retrieval, typed tools, persistent memory, supervisor‑subagent orchestration, workflows, MCP tool integration, and voice/UX integrations. Use them as learning guides or as starters for your own apps.

What you’ll find here

- RAG and retrieval over vectors and databases
- Typed tool design, MCP servers, and external APIs
- Working and persistent memory for grounded conversations
- Resumable streaming examples for reconnecting to in-flight responses
- Supervisor + sub‑agent orchestration and workflows
- Deployments for Next.js, Cloudflare Workers, Netlify and more

## Featured

### [WhatsApp Order Agent](./with-whatsapp)

Build a WhatsApp chatbot that handles food orders through natural conversation, manages menu items from a database, and processes orders with full conversation context.

<br/>

<img alt="whatsapp" src="https://github.com/user-attachments/assets/dc9c4986-3e68-42f8-a450-ecd79b4dbd99" />

<br/>
<br/>

- 📖 Tutorial: https://voltagent.dev/examples/agents/whatsapp-ai-agent

### [YouTube to Blog Agent](./with-youtube-to-blog)

Convert YouTube videos into Markdown blog posts using a supervisor agent that coordinates subagents with MCP tools, shared working memory, and VoltOps observability.

<br/>

<img alt="youtube" src="https://github.com/user-attachments/assets/f9c944cf-8a9a-4ac5-a5f9-860ce08f058b" />

<br/>
<br/>

- 📖 Tutorial: https://voltagent.dev/examples/agents/youtube-blog-agent

### [AI Ads Generator Agent](./with-ad-creator)

Implement an Instagram ad generator that uses BrowserBase Stagehand to analyze landing pages, extract brand data, and generate visuals through Google Gemini AI.

<br/>

<img alt="instagram" src="https://github.com/user-attachments/assets/973e79c7-34ec-4f8e-8a41-9273d44234c6" />

<br/>
<br/>

- 📖 Tutorial: https://voltagent.dev/examples/agents/ai-instagram-ad-agent

### [AI Recipe Generator Agent](./with-recipe-generator)

Build an intelligent recipe recommendation system that creates personalized cooking suggestions based on available ingredients, dietary preferences, and time constraints.

<br/>

<img alt="cook" src="https://github.com/user-attachments/assets/dde6ce2f-c963-4075-9825-f216bc6e3467" />

<br/>
<br/>

- 📖 Tutorial: https://voltagent.dev/examples/agents/recipe-generator
- 📹 Watch Video: https://youtu.be/KjV1c6AhlfY

### [AI Research Assistant Agent](./with-research-assistant)

Create a multi-agent research workflow where different AI agents collaborate to research topics and generate comprehensive reports with type-safe data flow.

<br/>

<img alt="research" src="https://github.com/user-attachments/assets/8f459748-132e-4ff3-9afe-0561fa5075c2" />

<br/>
<br/>

- 📖 Tutorial: https://voltagent.dev/examples/agents/research-assistant
- 📹 Watch Video: https://youtu.be/j6KAUaoZMy4

## All Examples

- [Base Starter](./base) — Minimal VoltAgent starter with a single agent, memory, and dev server.
- [Workspace](./with-workspace) — Workspace filesystem, sandbox execution, search, and skills.
- [Summarization](./with-summarization) — Agent summarization with a low trigger window for easy testing.
- [Retries and Fallbacks](./with-retries-fallback) — Model fallback list with per-model retries and agent-level defaults.
- [Middleware](./with-middleware) — Input/output middleware with retry feedback.
- [PlanAgents](./with-planagents) — Quickstart for PlanAgents with planning, filesystem tools, and subagent tasks.
- [Slack](./with-slack) — Slack app mention bot that replies in the same channel/thread via VoltOps Slack actions.
- [Chat SDK (Slack)](./with-chat-sdk) — Next.js webhook bot with Chat SDK transport and VoltAgent-powered responses.
- [Airtable](./with-airtable) — React to new Airtable records and write updates back using VoltOps Airtable actions.
- [GitHub Repo Analyzer](./github-repo-analyzer) — Agents read repository code and summarize insights/issues from GitHub projects.
- [GitHub Star Stories](./github-star-stories) — Celebrate new GitHub stars with enriched profiles, AI-written stories, and VoltOps Discord actions.
- [SDK Trace Example](./sdk-trace-example) — OpenTelemetry tracing wired to VoltOps so you can inspect spans and events.
- [Agent‑to‑Agent Server](./with-a2a-server) — Expose agents over HTTP so other agents/services can call them.
- [Amazon Bedrock](./with-amazon-bedrock) — Run AWS Bedrock models by configuring credentials and model IDs in VoltAgent.
- [Anthropic](./with-anthropic) — Use Claude models as your agent’s LLM via the AI SDK.
- [OpenRouter](./with-openrouter) — Use OpenRouter through VoltAgent's built-in `openrouter/<model>` routing.
- [Chroma](./with-chroma) — RAG with Chroma vectors showing automatic vs tool‑driven retrieval patterns.
- [Client‑side Tools](./with-client-side-tools) — Next.js UI triggers typed client‑side tools safely, VoltAgent on the server.
- [Cloudflare Workers](./with-cloudflare-workers) — Deploy your agent on Workers using the Hono server adapter.
- [Composio (MCP)](./with-composio-mcp) — Call Composio actions through MCP tools inside your workflows.
- [Custom Endpoints](./with-custom-endpoints) — Add bespoke REST endpoints alongside agent/workflow routes.
- [Dynamic Parameters](./with-dynamic-parameters) — Validate and inject runtime parameters into agents with Zod.
- [Dynamic Prompts](./with-dynamic-prompts) — Build prompts from templates and live data programmatically.
- [Google AI](./with-google-ai) — Use Google Gemini models via the AI SDK provider.
- [Google Drive (MCP)](./with-google-drive-mcp) — Browse and read Drive files through a Google Drive MCP server.
- [Google Vertex AI](./with-google-vertex-ai) — Connect agents to Vertex AI models in your GCP project.
- [Groq](./with-groq-ai) — Ultra‑low latency responses using Groq’s LPU inference.
- [Guardrails](./with-guardrails) — Add output validation and schema enforcement to keep responses on spec.
- [Hooks](./with-hooks) — Demonstrates lifecycle hooks/middleware for logging, auth, or customization.
- [Hugging Face (MCP)](./with-hugging-face-mcp) — Access HF tools and models through MCP from agents.
- [JWT Auth](./with-jwt-auth) — Protect agent endpoints with JWT verification and helpers.
- [Langfuse](./with-langfuse) — Send traces and metrics to Langfuse for observability.
- [Feedback Templates](./with-feedback) — Configure per-agent feedback templates for thumbs, numeric, and categorical feedback.
- [Live Evals](./with-live-evals) — Run online evaluations against prompts/agents during development.
- [MCP Basics](./with-mcp) — Connect to MCP servers and call tools from an agent.
- [MCP Elicitation](./with-mcp-elicitation) — Handle `elicitation/create` requests from MCP tools with per-request handlers.
- [MCP Server](./with-mcp-server) — Implement and run a local MCP server that exposes custom tools.
- [Netlify Functions](./with-netlify-functions) — Ship serverless agent APIs on Netlify.
- [Next.js](./with-nextjs) — React UI with agent APIs and streaming responses.
- [Next.js + Resumable Streams](./with-nextjs-resumable-stream) — AI Elements chat UI with VoltAgent and resumable streams.
- [Nuxt](./with-nuxt) — Vue/Nuxt front‑end talking to VoltAgent APIs.
- [Offline Evals](./with-offline-evals) — Batch datasets and score outputs for regression testing.
- [Peaka (MCP)](./with-peaka-mcp) — Integrate Peaka services via MCP tools.
- [Pinecone](./with-pinecone) — RAG retrieval backed by Pinecone vectors and embeddings.
- [Playwright](./with-playwright) — Web automation tools powered by Playwright for browsing and actions.
- [Postgres](./with-postgres) — Use Postgres/pgvector for storage and semantic retrieval.
- [Qdrant](./with-qdrant) — RAG with Qdrant showing retriever‑on‑every‑turn vs LLM‑decides search.
- [RAG Chatbot](./with-rag-chatbot) — A conversational bot grounded in your documents with citations.
- [Retrieval](./with-retrieval) — Minimal retrieval helpers demonstrating the retriever API.
- [VoltOps Retrieval](./with-voltops-retrieval) — Use VoltOps Knowledge Bases as a retriever via @voltagent/core.
- [Sub‑agents](./with-subagents) — Supervisor orchestrates focused sub‑agents to divide tasks.
- [Supabase](./with-supabase) — Use Supabase auth/database in tools and server endpoints.
- [Tavily Search](./with-tavily-search) — Augment answers with web results from Tavily.
- [Thinking Tool](./with-thinking-tool) — Structured reasoning via a dedicated “thinking” tool and schema.
- [Tool Routing](./with-tool-routing) — Route large tool pools through a small set of router tools.
- [Tools](./with-tools) — Author Zod‑typed tools with cancellation and streaming support.
- [VoltOps Actions + Airtable](./with-voltagent-actions) — Call VoltOps Actions as tools to create and list Airtable records.
- [Turso](./with-turso) — Persist memory on LibSQL/Turso with simple setup.
- [Vector Search](./with-vector-search) — Semantic memory with embeddings and automatic recall during chats.
- [Vercel AI](./with-vercel-ai) — VoltAgent with Vercel AI SDK provider and streaming.
- [Resumable Streams](./with-resumable-streams) — Persist and resume chat streams with Redis-backed SSE storage.
- [VoltOps Resumable Streams](./with-voltops-resumable-streams) — Persist and resume chat streams with VoltOps managed storage.
- [ViteVal](./with-viteval) — Integrate ViteVal to evaluate agents and prompts.
- [Voice (ElevenLabs)](./with-voice-elevenlabs) — Convert agent replies to speech using ElevenLabs TTS.
- [Voice (OpenAI)](./with-voice-openai) — Speak responses with OpenAI’s TTS voices.
- [Voice (xAI)](./with-voice-xsai) — Use xAI audio models for voice output.
- [VoltAgent Exporter](./with-voltagent-exporter) — Export traces/events to external observability targets.
- [Managed Memory](./with-voltagent-managed-memory) — Production‑grade memory via VoltOps Managed Memory REST adapter.
- [Workflow](./with-workflow) — Build multi‑step flows with createWorkflowChain and human‑in‑the‑loop.
- [Working Memory](./with-working-memory) — Persist per‑conversation/user facts with built‑in read/update tools.
- [Zapier (MCP)](./with-zapier-mcp) — Trigger Zapier actions through MCP from your agents.

```

### File: tools\README.md
```md
# ⚒️ Tools

Internal tools for building, maintaining, testing, and publishing VoltAgent packages.

## Getting Started

We (primarily) use [nx](https://nx.dev) plugins for our tooling.

## `nx` plugins

You can see a full list of the nx plugins (our primary interface for tooling) by running:

```bash
pnpm nx list core
```

### Generators

#### `generate-package`

You can generate a new package by running:

```bash
pnpm nx generate core:package my-package
```

This will create a new package (e.g. `my-package`) in the `packages` directory.

```

### File: website\package.json
```json
{
  "name": "web",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "build": "docusaurus build",
    "build:plugins": "sucrase ./plugins -d ./plugins --transforms typescript,imports && npx prettier --write ./plugins",
    "clear": "docusaurus clear",
    "deploy": "docusaurus deploy",
    "docusaurus": "docusaurus",
    "lint": "biome check .",
    "lint:ci": "biome ci .",
    "lint:fix": "biome check . --write",
    "lint:staged": "lint-staged",
    "serve": "docusaurus serve",
    "start": "docusaurus start",
    "swizzle": "docusaurus swizzle",
    "typecheck": "tsc",
    "write-heading-ids": "docusaurus write-heading-ids",
    "write-translations": "docusaurus write-translations"
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "biome check --write --no-errors-on-unmatched"
    ],
    "*.{md,mdx}": [
      "prettier --config ../.prettierrc --write"
    ]
  },
  "browserslist": {
    "production": [
      ">0.5%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 3 chrome version",
      "last 3 firefox version",
      "last 5 safari version"
    ]
  },
  "dependencies": {
    "@codesandbox/sandpack-react": "^2.20.0",
    "@codesandbox/sandpack-themes": "^2.0.21",
    "@docusaurus/core": "3.1.1",
    "@docusaurus/plugin-client-redirects": "3.1.1",
    "@docusaurus/preset-classic": "3.1.1",
    "@docusaurus/theme-mermaid": "3.1.1",
    "@headlessui/react": "^2.1.2",
    "@heroicons/react": "^2.1.5",
    "@mdx-js/react": "^3.0.0",
    "@monaco-editor/react": "^4.6.0",
    "@types/recharts": "^1.8.29",
    "@xyflow/react": "^12.4.4",
    "canvas-confetti": "^1.9.3",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cron-parser": "^4.9.0",
    "cronstrue": "^2.47.0",
    "dotenv": "^16.4.5",
    "framer-motion": "^10.18.0",
    "headlessui": "^0.0.0",
    "howler": "^2.2.4",
    "js-yaml": "^4.1.0",
    "lucide-react": "^0.476.0",
    "motion": "^12.4.7",
    "prism-react-renderer": "^2.3.0",
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "react-markdown": "^9.0.1",
    "react-slick": "^0.30.2",
    "react-tweet": "^3.2.2",
    "recharts": "^2.15.0",
    "slick-carousel": "^1.8.1",
    "tailwind-merge": "^3.0.2",
    "tailwindcss-animate": "^1.0.7",
    "usehooks-ts": "^3.1.0"
  },
  "devDependencies": {
    "@biomejs/biome": "^1.9.4",
    "@docusaurus/module-type-aliases": "3.1.1",
    "@docusaurus/tsconfig": "3.1.1",
    "@docusaurus/types": "3.1.1",
    "@types/gtag.js": "^0.0.19",
    "husky": "^9.0.11",
    "lint-staged": "^15.2.2",
    "sucrase": "^3.35.0",
    "tailwind-component-classes": "^2.0.4",
    "tailwindcss": "^3.4.1",
    "typescript": "~5.2.2"
  },
  "engines": {
    "node": ">=20"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/VoltAgent/voltagent.git",
    "directory": "website/"
  }
}

```

### File: website\README.md
```md
# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

### Installation

```
$ npm
```

### Local Development

```
$ npm start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```
$ npm build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```
$ USE_SSH=true yarn deploy
```

Not using SSH:

```
$ GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

```

### File: examples\base\package.json
```json
{
  "name": "voltagent-example-base",
  "author": "",
  "dependencies": {
    "@ai-sdk/openai": "^3.0.0",
    "@voltagent/cli": "^0.1.21",
    "@voltagent/core": "^2.6.14",
    "@voltagent/libsql": "^2.1.2",
    "@voltagent/logger": "^2.0.2",
    "@voltagent/server-hono": "^2.0.8",
    "ai": "^6.0.0",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@types/node": "^24.2.1",
    "tsx": "^4.21.0",
    "typescript": "^5.8.2"
  },
  "keywords": [
    "agent",
    "ai",
    "voltagent"
  ],
  "license": "MIT",
  "private": true,
  "repository": {
    "type": "git",
    "url": "https://github.com/VoltAgent/voltagent.git",
    "directory": "examples/base"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsx watch --env-file=.env ./src",
    "start": "node dist/index.js",
    "volt": "volt"
  },
  "type": "module"
}

```

### File: examples\base\README.md
```md
<div align="center">
<a href="https://voltagent.dev/">
<img width="1800" alt="435380213-b6253409-8741-462b-a346-834cd18565a9" src="https://github.com/user-attachments/assets/452a03e7-eeda-4394-9ee7-0ffbcf37245c" />
</a>

<br/>
<br/>

<div align="center">
    <a href="https://voltagent.dev">Home Page</a> |
    <a href="https://voltagent.dev/docs/">Documentation</a> |
    <a href="https://github.com/voltagent/voltagent/tree/main/examples">Examples</a> |
    <a href="https://s.voltagent.dev/discord">Discord</a> |
    <a href="https://voltagent.dev/blog/">Blog</a>
</div>
</div>

<br/>

<div align="center">
    <strong>VoltAgent is an open source TypeScript framework for building and orchestrating AI agents.</strong><br>
Escape the limitations of no-code builders and the complexity of starting from scratch.
    <br />
    <br />
</div>

<div align="center">
    
[![npm version](https://img.shields.io/npm/v/@voltagent/core.svg)](https://www.npmjs.com/package/@voltagent/core)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)
[![Twitter Follow](https://img.shields.io/twitter/follow/voltagent_dev?style=social)](https://twitter.com/voltagent_dev)
    
</div>

<br/>

<div align="center">
<a href="https://voltagent.dev/">
<img width="896" alt="VoltAgent Schema" src="https://github.com/user-attachments/assets/f0627868-6153-4f63-ba7f-bdfcc5dd603d" />
</a>

</div>

## VoltAgent: Build AI Agents Fast and Flexibly

VoltAgent is an open-source TypeScript framework for creating and managing AI agents. It provides modular components to build, customize, and scale agents with ease. From connecting to APIs and memory management to supporting multiple LLMs, VoltAgent simplifies the process of creating sophisticated AI systems. It enables fast development, maintains clean code, and offers flexibility to switch between models and tools without vendor lock-in.

## Try Example

```bash
npm create voltagent-app@latest -- --example base
```

```

### File: examples\with-copilotkit\README.md
```md
<div align="center">
<a href="https://voltagent.dev/">
<img width="1800" alt="VoltAgent Banner" src="https://github.com/user-attachments/assets/452a03e7-eeda-4394-9ee7-0ffbcf37245c" />
</a>

<br/>
<br/>

<div align="center">
    <a href="https://voltagent.dev">Home Page</a> |
    <a href="https://voltagent.dev/docs/">Documentation</a> |
    <a href="https://github.com/voltagent/voltagent/tree/main/examples">Examples</a> |
    <a href="https://s.voltagent.dev/discord">Discord</a> |
    <a href="https://voltagent.dev/blog/">Blog</a>
</div>
</div>

<br/>

<div align="center">
    <strong>VoltAgent is an open source TypeScript framework for building and orchestrating AI agents.</strong><br>
Escape the limitations of no-code builders and the complexity of starting from scratch.
    <br />
    <br />
</div>

<div align="center">
    
[![npm version](https://img.shields.io/npm/v/@voltagent/core.svg)](https://www.npmjs.com/package/@voltagent/core)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)
[![Twitter Follow](https://img.shields.io/twitter/follow/voltagent_dev?style=social)](https://twitter.com/voltagent_dev)
    
</div>

<br/>

<div align="center">
<a href="https://voltagent.dev/">
<img width="896" alt="VoltAgent Schema" src="https://github.com/user-attachments/assets/f0627868-6153-4f63-ba7f-bdfcc5dd603d" />
</a>

</div>

## VoltAgent + CopilotKit Example

This example exposes a CopilotKit runtime endpoint on VoltAgent (Hono server) and ships a Vite React client with CopilotKit UI, a frontend tool, and a human-in-the-loop hook.

## Try Example

```bash
npm create voltagent-app@latest -- --example with-copilotkit
```

## Manual run

Server (Hono + CopilotKit endpoint):

```bash
cd examples/with-copilotkit/server
npm install
npm run dev
```

Client (Vite React + CopilotKit UI):

```bash
cd examples/with-copilotkit/client
npm install
npm run dev
```

The client expects `http://localhost:3141/copilotkit`. Remember to set `OPENAI_API_KEY` for OpenAI access.

```

### File: packages\ag-ui\package.json
```json
{
  "name": "@voltagent/ag-ui",
  "description": "AG-UI adapter for VoltAgent agents and CopilotKit runtimes.",
  "version": "1.0.7",
  "dependencies": {
    "rxjs": "^7.8.1"
  },
  "devDependencies": {
    "@ag-ui/client": "^0.0.41",
    "@ag-ui/core": "^0.0.37",
    "@copilotkit/runtime": "^1.50.0",
    "@vitest/coverage-v8": "^3.2.4",
    "@voltagent/core": "^2.6.13",
    "@voltagent/internal": "^1.0.2",
    "tsup": "^8.5.0",
    "typescript": "^5.8.2",
    "vitest": "^3.2.4"
  },
  "exports": {
    ".": {
      "import": {
        "types": "./dist/index.d.mts",
        "default": "./dist/index.mjs"
      },
      "require": {
        "types": "./dist/index.d.ts",
        "default": "./dist/index.js"
      }
    }
  },
  "files": [
    "dist"
  ],
  "license": "MIT",
  "main": "dist/index.js",
  "module": "dist/index.mjs",
  "peerDependencies": {
    "@ag-ui/client": ">=0.0.37",
    "@ag-ui/core": ">=0.0.37",
    "@copilotkit/runtime": "^1.50.0",
    "@voltagent/core": ">=1.0.0",
    "@voltagent/internal": "^1.0.0",
    "rxjs": "^7.8.1"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/VoltAgent/voltagent.git",
    "directory": "packages/ag-ui"
  },
  "scripts": {
    "build": "tsup",
    "dev": "tsup --watch",
    "lint": "biome check .",
    "lint:fix": "biome check . --write",
    "publint": "publint --strict",
    "test": "vitest"
  },
  "types": "dist/index.d.ts"
}

```

### File: packages\cli\package.json
```json
{
  "name": "@voltagent/cli",
  "description": "CLI tool for VoltAgent applications",
  "version": "0.1.21",
  "bin": {
    "volt": "dist/index.js"
  },
  "dependencies": {
    "@voltagent/evals": "^2.0.2",
    "@voltagent/internal": "^1.0.2",
    "@voltagent/sdk": "^2.0.2",
    "adm-zip": "^0.5.12",
    "boxen": "^5.1.2",
    "bundle-require": "^5.1.0",
    "chalk": "^4.1.2",
    "commander": "^11.1.0",
    "configstore": "^7.1.0",
    "dotenv": "^16.4.5",
    "esbuild": "^0.25.10",
    "figlet": "^1.7.0",
    "fs-extra": "^11.1.1",
    "gray-matter": "^4.0.3",
    "inquirer": "^8.2.6",
    "localtunnel": "^2.0.2",
    "npm-check-updates": "^17.1.18",
    "open": "^10.0.0",
    "ora": "^5.4.1",
    "posthog-node": "^4.11.5",
    "semver": "^7.5.4",
    "update-notifier": "^5.1.0",
    "uuid": "^9.0.1"
  },
  "devDependencies": {
    "@types/adm-zip": "^0.5.5",
    "@types/boxen": "^3.0.1",
    "@types/figlet": "^1.5.8",
    "@types/fs-extra": "^11.0.4",
    "@types/inquirer": "^9.0.7",
    "@types/localtunnel": "^2.0.3",
    "@types/semver": "^7.5.6",
    "@types/update-notifier": "^6.0.8",
    "@types/uuid": "^10.0.0",
    "@vitest/coverage-v8": "^3.2.4"
  },
  "engines": {
    "node": ">=20"
  },
  "files": [
    "dist"
  ],
  "keywords": [
    "agent",
    "cli",
    "voltagent"
  ],
  "license": "MIT",
  "main": "dist/index.js",
  "repository": {
    "type": "git",
    "url": "https://github.com/VoltAgent/voltagent.git",
    "directory": "packages/cli"
  },
  "scripts": {
    "attw": "attw --pack",
    "build": "tsup",
    "dev": "tsup --watch",
    "lint": "biome check .",
    "lint:fix": "biome check . --write",
    "publint": "publint --strict",
    "start": "node dist/index.js",
    "test": "vitest",
    "test:coverage": "vitest run --coverage"
  }
}

```

### File: packages\cli\README.md
```md
<div align="center">
<a href="https://voltagent.dev/">
<img width="1800" alt="435380213-b6253409-8741-462b-a346-834cd18565a9" src="https://github.com/user-attachments/assets/452a03e7-eeda-4394-9ee7-0ffbcf37245c" />
</a>

<br/>
<br/>

<div align="center">
    <a href="https://voltagent.dev">Home Page</a> |
    <a href="https://voltagent.dev/docs/">Documentation</a> |
    <a href="https://github.com/voltagent/voltagent/tree/main/examples">Examples</a> |
    <a href="https://s.voltagent.dev/discord">Discord</a> |
    <a href="https://voltagent.dev/blog/">Blog</a>
</div>
</div>

<br/>

<div align="center">
    <strong>VoltAgent is an open source TypeScript framework for building and orchestrating AI agents.</strong><br>
Escape the limitations of no-code builders and the complexity of starting from scratch.
    <br />
    <br />
</div>

<div align="center">

[![npm version](https://img.shields.io/npm/v/@voltagent/core.svg)](https://www.npmjs.com/package/@voltagent/core)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)
[![Twitter Follow](https://img.shields.io/twitter/follow/voltagent_dev?style=social)](https://twitter.com/voltagent_dev)

</div>

<br/>

<div align="center">
<a href="https://voltagent.dev/">
<img width="896" alt="flow" src="https://github.com/user-attachments/assets/f0627868-6153-4f63-ba7f-bdfcc5dd603d" />
</a>

</div>

## What is VoltAgent?

> An **AI Agent Framework** provides the foundational structure and tools needed to build applications powered by autonomous agents. These agents, often driven by Large Language Models (LLMs), can perceive their environment, make decisions, and take actions to achieve specific goals. Building such agents from scratch involves managing complex interactions with LLMs, handling state, connecting to external tools and data, and orchestrating workflows.

**VoltAgent** is an open-source TypeScript framework that acts as this essential toolkit. It simplifies the development of AI agent applications by providing modular building blocks, standardized patterns, and abstractions. Whether you're creating chatbots, virtual assistants, automated workflows, or complex multi-agent systems, VoltAgent handles the underlying complexity, allowing you to focus on defining your agents' capabilities and logic.

Instead of building everything from scratch, VoltAgent provides ready-made, modular building blocks:

- **Core Engine (`@voltagent/core`)**: The heart of VoltAgent, providing fundamental capabilities for your AI agents Define individual agents with specific roles, tools, and memory.
- **Multi-Agent Systems**: Architect complex applications by coordinating multiple specialized agents using Supervisors.
- **Workflow Engine**: Go beyond simple request-response. Orchestrate multi-step automations that can process data, call APIs, run tasks in parallel, and execute conditional logic.
- **Extensible Packages**: Enhance functionality with packages like `@voltagent/voice` for voice interactions.
- **Tooling & Integrations**: Equip agents with tools to connect to external APIs, databases, and services, enabling them to perform real-world tasks. **Supports the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) for standardized tool interactions.**
- **Data Retrieval & RAG**: Implement specialized retriever agents for efficient information fetching and **Retrieval-Augmented Generation (RAG)**.
- **Memory**: Enable agents to remember past interactions for more natural and context-aware conversations.
- **LLM Compatibility**: Works with popular AI models from OpenAI, Google, Anthropic, and more, allowing easy switching.
- **Developer Ecosystem**: Includes helpers like `create-voltagent-app`, `@voltagent/cli`, and the visual [VoltOps LLM Observability Platform](https://console.voltagent.dev) for quick setup, monitoring, and debugging.

In essence, VoltAgent helps developers build sophisticated AI applications faster and more reliably, avoiding repetitive setup and the limitations of simpler tools.

## Why VoltAgent?

Building AI applications often involves a trade-off:

1.  **DIY Approach:** Using basic AI provider tools offers control but leads to complex, hard-to-manage code and repeated effort.
2.  **No-Code Builders:** Simpler initially but often restrictive, limiting customization, provider choice, and complexity.

VoltAgent provides a middle ground, offering structure and components without sacrificing flexibility:

- **Build Faster:** Accelerate development with pre-built components compared to starting from scratch.
- **Maintainable Code:** Encourages organization for easier updates and debugging.
- **Scalability:** Start simple and easily scale to complex, multi-agent systems handling intricate workflows.
- **Build Sophisticated Automations:** It's not just for chat. The workflow engine lets you build complex, multi-step processes for tasks like data analysis pipelines, automated content generation, or intelligent decision-making systems.
- **Flexibility:** Full control over agent behavior, LLM choice, tool integrations, and UI connections.
- **Avoid Lock-in:** Freedom to switch AI providers and models as needed.
- **Cost Efficiency:** Features designed to optimize AI service usage and reduce redundant calls.
- **Visual Monitoring:** Use the [VoltOps LLM Observability Platform](https://console.voltagent.dev) to track agent performance, inspect state, and debug visually.

VoltAgent empowers developers to build their envisioned AI applications efficiently, from simple helpers to complex systems.

## ⚡ Quick Start

Create a new VoltAgent project in seconds using the `create-voltagent-app` CLI tool:

```bash
npm create voltagent-app@latest
```

This command guides you through setup.

You'll see the starter code in `src/index.ts`, which now registers both an agent and a comprehensive workflow example found in `src/workflows/index.ts`.

```typescript
import { VoltAgent, Agent, Memory } from "@voltagent/core";
import { LibSQLMemoryAdapter } from "@voltagent/libsql";
import { createPinoLogger } from "@voltagent/logger";
import { honoServer } from "@voltagent/server-hono";
import { openai } from "@ai-sdk/openai";
import { expenseApprovalWorkflow } from "./workflows";
import { weatherTool } from "./tools";

// Create a logger instance
const logger = createPinoLogger({
  name: "my-agent-app",
  level: "info",
});

// Optional persistent memory (remove to use default in-memory)
const memory = new Memory({
  storage: new LibSQLMemoryAdapter({ url: "file:./.voltagent/memory.db" }),
});

// A simple, general-purpose agent for the project.
const agent = new Agent({
  name: "my-agent",
  instructions: "A helpful assistant that can check weather and help with various tasks",
  model: openai("gpt-4o-mini"),
  tools: [weatherTool],
  memory,
});

// Initialize VoltAgent with your agent(s) and workflow(s)
new VoltAgent({
  agents: {
    agent,
  },
  workflows: {
    expenseApprovalWorkflow,
  },
  server: honoServer(),
  logger,
});
```

Afterwards, navigate to your project and run:

```bash
npm run dev
```

When you run the dev command, tsx will compile and run your code. You should see the VoltAgent server startup message in your terminal:

```
══════════════════════════════════════════════════
VOLTAGENT SERVER STARTED SUCCESSFULLY
══════════════════════════════════════════════════
✓ HTTP Server: http://localhost:3141

Test your agents with VoltOps Console: https://console.voltagent.dev
══════════════════════════════════════════════════
```

Your agent is now running! To interact with it:

1. Open the Console: Click the [VoltOps LLM Observability Platform](https://console.voltagent.dev) link in your terminal output (or copy-paste it into your browser).
2. Find Your Agent: On the VoltOps LLM Observability Platform page, you should see your agent listed (e.g., "my-agent").
3. Open Agent Details: Click on your agent's name.
4. Start Chatting: On the agent detail page, click the chat icon in the bottom right corner to open the chat window.
5. Send a Message: Type a message like "Hello" and press Enter.

[![VoltAgent VoltOps Platform Demo](https://github.com/user-attachments/assets/0adbec33-1373-4cf4-b67d-825f7baf1cb4)](https://console.voltagent.dev/)

### Running Your First Workflow

Your new project also includes a powerful workflow engine. You can test the pre-built `expenseApprovalWorkflow` directly from the VoltOps console:

![VoltOps Workflow Observability](https://github.com/user-attachments/assets/9b877c65-f095-407f-9237-d7879964c38a)

1.  **Go to the Workflows Page:** After starting your server, go directly to the [Workflows page](https://console.voltagent.dev/workflows).
2.  **Select Your Project:** Use the project selector to choose your project (e.g., "my-agent-app").
3.  **Find and Run:** You will see **"Expense Approval Workflow"** listed. Click it, then click the **"Run"** button.
4.  **Provide Input:** The workflow expects a JSON object with expense details. Try a small expense for automatic approval:
    ```json
    {
      "employeeId": "EMP-123",
      "amount": 250,
      "category": "office-supplies",
      "description": "New laptop mouse and keyboard"
    }
    ```
5.  **View the Results:** After execution, you can inspect the detailed logs for each step and see the final output directly in the console.

## Key Features

- **Agent Core:** Define agents with descriptions, LLM providers, tools, and memory management.
- **Workflow Engine:** Orchestrate complex, multi-step automations with a powerful and declarative API (`andThen`, `andAgent`, `andAll`, `andRace`, `andWhen`).
- **Multi-Agent Systems:** Build complex workflows using Supervisor Agents coordinating multiple specialized Sub-Agents.
- **Tool Usage & Lifecycle:** Equip agents with custom or pre-built tools (functions) with type-safety (Zod), lifecycle hooks, and cancellation support to interact with external systems.
- **Flexible LLM Support:** Integrate seamlessly with various LLM providers (OpenAI, Anthropic, Google, etc.) and easily switch between models.
- **Memory Management:** Enable agents to retain context across interactions using different configurable memory providers.
- **Observability & Debugging:** Visually monitor agent states, interactions, logs, and performance via the [VoltOps LLM Observability Platform](https://console.voltagent.dev).
- **Custom API Endpoints:** Extend the VoltAgent API server with your own custom endpoints to build specialized functionality on top of the core framework.
- **Voice Interaction:** Build voice-enabled agents capable of speech recognition and synthesis using the `@voltagent/voice` package.
- **Data Retrieval & RAG:** Integrate specialized retriever agents for efficient information fetching and **Retrieval-Augmented Generation (RAG)** from various sources.
- **Model Context Protocol (MCP) Support:** Connect to external tool servers (HTTP/stdio) adhering to the [MCP standard](https://modelcontextprotocol.io/) for extended capabilities.
- **Prompt Engineering Tools:** Leverage utilities like `createPrompt` for crafting and managing effective prompts for your agents.
- **Framework Compatibility:** Designed for easy integration into existing Node.js applications and popular frameworks.

## Use Cases

VoltAgent is versatile and can power a wide range of AI-driven applications:

- **Complex Workflow Automation:** Orchestrate multi-step processes involving various tools, APIs, and decision points using coordinated agents.
- **Intelligent Data Pipelines:** Build agents that fetch, process, analyze, and transform data from diverse sources.
- **AI-Powered Internal Tools & Dashboards:** Create interactive internal applications that leverage AI for analysis, reporting, or task automation, often integrated with UIs using hooks.
- **Automated Customer Support Agents:** Develop sophisticated chatbots that can understand context (memory), use tools (e.g., check order status), and escalate complex issues.
- **Repository Analysis & Codebase Automation:** Analyze code repositories, automate refactoring tasks, generate documentation, or manage CI/CD processes.
- **Retrieval-Augmented Generation (RAG) Systems:** Build agents that retrieve relevant information from knowledge bases (using retriever agents) before generating informed responses.
- **Voice-Controlled Interfaces & Applications:** Utilize the `@voltagent/voice` package to create applications that respond to and generate spoken language.
- **Personalized User Experiences:** Develop agents that adapt responses and actions based on user history and preferences stored in memory.
- **Real-time Monitoring & Alerting:** Design agents that continuously monitor data streams or systems and trigger actions or notifications based on defined conditions.
- **And Virtually Anything Else...**: If you can imagine an AI agent doing it, VoltAgent can likely help you build it! ⚡

## Learning VoltAgent

- **[Documentation](https://voltagent.dev/docs/)**: Dive into guides, concepts, and tutorials.
- **[Examples](https://github.com/voltagent/voltagent/tree/main/examples)**: Explore practical implementations.
- **[Blog](https://voltagent.dev/blog/)**: Read more about technical insights, and best practices.

## Contribution

We welcome contributions! Please refer to the contribution guidelines (link needed if available). Join our [Discord](https://s.voltagent.dev/discord) server for questions and discussions.

## Contributor ♥️ Thanks

Big thanks to everyone who's been part of the VoltAgent journey, whether you've built a plugin, opened an issue, dropped a pull request, or just helped someone out on Discord or GitHub Discussions.

VoltAgent is a community effort, and it keeps getting better because of people like you.

![Contributors](https://contrib.rocks/image?repo=voltagent/voltagent)

Your stars help us reach more developers! If you find VoltAgent useful, please consider giving us a star on GitHub to support the project and help others discover it.

## License

Licensed under the MIT License, Copyright © 2025-present VoltAgent.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

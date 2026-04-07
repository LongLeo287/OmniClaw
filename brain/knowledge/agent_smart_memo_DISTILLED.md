---
id: agent-smart-memo
type: knowledge
owner: OA_Triage
---
# agent-smart-memo
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
	"name": "@mrc2204/agent-smart-memo",
	"version": "5.1.19",
	"description": "Smart Memory Plugin for OpenClaw — structured slot memory with auto-capture, auto-recall, essence distillation, and Qdrant vector search",
	"keywords": [
		"agent",
		"ai",
		"auto-capture",
		"memory",
		"openclaw",
		"plugin",
		"qdrant",
		"smart-memo"
	],
	"license": "MIT",
	"author": "mrc2204",
	"repository": {
		"type": "git",
		"url": "git+https://github.com/cong91/agent-smart-memo.git"
	},
	"bin": {
		"agent-smart-memo": "bin/asm.mjs",
		"asm": "bin/asm.mjs"
	},
	"files": [
		"dist/",
		"bin/",
		"scripts/init-openclaw.mjs",
		"openclaw.plugin.json",
		"CONFIG.example.json",
		"README.md",
		"LICENSE"
	],
	"type": "module",
	"main": "dist/index.js",
	"publishConfig": {
		"access": "public"
	},
	"scripts": {
		"build": "npm run build:openclaw && npm run sync:openclaw:dist",
		"build:all": "npm run build:openclaw && npm run build:paperclip && npm run build:core",
		"build:openclaw": "tsc -p tsconfig.openclaw.json",
		"build:paperclip": "tsc -p tsconfig.paperclip.json",
		"build:core": "tsc -p tsconfig.core.json",
		"sync:openclaw:dist": "node scripts/sync-openclaw-dist.mjs",
		"package:openclaw": "npm run build:openclaw && node scripts/prepare-package-target.mjs openclaw",
		"package:paperclip": "npm run build:paperclip && node scripts/prepare-package-target.mjs paperclip",
		"package:core": "npm run build:core && node scripts/prepare-package-target.mjs core",
		"pack:openclaw": "npm run package:openclaw && (cd artifacts/npm/openclaw && npm pack)",
		"pack:paperclip": "npm run package:paperclip && (cd artifacts/npm/paperclip && npm pack)",
		"package:paperclip:plugin-local": "npm run build:paperclip && node scripts/prepare-paperclip-plugin-local.mjs",
		"pack:paperclip:plugin-local": "npm run package:paperclip:plugin-local && (cd artifacts/paperclip-plugin-local && npm pack)",
		"pack:core": "npm run package:core && (cd artifacts/npm/core && npm pack)",
		"publish:openclaw": "npm run package:openclaw && node scripts/publish-target.mjs openclaw",
		"publish:paperclip": "npm run package:paperclip && node scripts/publish-target.mjs paperclip",
		"publish:core": "npm run package:core && node scripts/publish-target.mjs core",
		"test": "npx tsx tests/test.ts && npx tsx tests/test-auto-recall.ts && npx tsx tests/test-memory-config.ts",
		"test:openclaw": "npx tsx tests/test-openclaw-adapter-contract.ts && npx tsx tests/test-openclaw-semantic-tools-integration.ts",
		"test:paperclip": "npx tsx tests/test-paperclip-contracts.ts && npx tsx tests/test-paperclip-runtime-e2e.ts",
		"test:asm-cli": "npx tsx tests/test-asm-cli.ts",
		"smoke:paperclip:local": "npm run build:paperclip && node scripts/paperclip-local-smoke-debug.mjs",
		"clean": "rm -rf dist dist-openclaw dist-paperclip dist-core artifacts/npm",
		"migrate:namespaces": "npx tsx scripts/migrate-namespaces.ts",
		"migrate:memory-foundation": "npx tsx scripts/migrate-memory-foundation.ts",
		"distill:namespaces": "npx tsx scripts/distill-by-namespace.ts",
		"validate:ab": "npx tsx scripts/validate-ab.ts",
		"init-openclaw": "node scripts/init-openclaw.mjs",
		"asm": "node bin/asm.mjs"
	},
	"dependencies": {
		"dotenv": "^17.3.1"
	},
	"devDependencies": {
		"@sinclair/typebox": "^0.34.0",
		"@types/node": "^22.0.0",
		"openclaw": "*",
		"typescript": "^5.0.0"
	},
	"openclaw": {
		"extensions": [
			"./dist/index.js"
		]
	}
}

```

### File: README.md
```md
# Agent Smart Memo

> **ASM v5.1** is a super memory platform for coding agents: **conversation memory + project memory + retrieval/control plane**, delivered through a single package and a CLI-first install flow.

`@mrc2204/agent-smart-memo` provides a project-aware memory layer that can be installed into multiple runtimes while keeping one shared memory/config model.

Today ASM provides:
- conversation/runtime continuity
- structured slot memory
- semantic retrieval
- graph memory
- project registry + onboarding
- repo-aware indexing / reindexing
- lineage-aware engineering context retrieval
- CLI-based platform install flows for OpenClaw, Paperclip, and OpenCode

This means ASM is best understood as:

> **a shared memory platform for coding agents, with OpenClaw as the primary runtime and Paperclip/OpenCode as supported adapters**

---

## 1) Core mental model

ASM has 3 practical layers.

### A. Conversation memory
Used for runtime continuity:
- `memory_search`
- `memory_store`
- `memory_slot_*`
- `memory_graph_*`
- auto-capture / auto-recall

### B. Project memory
Used for engineering context:
- project registry
- repo root / repo remote identity
- project aliasing
- Jira linkage
- onboarding + index triggers
- lifecycle-aware retrieval boundaries

### C. Retrieval/control plane
Used to assemble better context for coding agents:
- semantic recall
- lexical/project filtering
- file/symbol/task lineage
- deterministic project-aware retrieval
- platform install / bootstrap flows

If you only remember one sentence, remember this:

> **ASM is a super memory platform for coding agents: conversation memory + project memory + runtime delivery in one package.**

---

## 2) Runtime targets

### OpenClaw
Primary target today.

Includes:
- OpenClaw plugin entry
- tools / hooks / runtime wiring
- CLI bootstrap flow
- shared ASM config integration

Install:
```bash
asm install openclaw
```

### Paperclip
Uses the same shared memory core through a Paperclip adapter.

Install:
```bash
asm install paperclip
```

### OpenCode
Uses the same package and shared config, with MCP/local runtime wiring.

Install:
```bash
asm install opencode
```

---

## 3) Install ASM

There are currently **two supported install flows**.

### Flow A — CLI-first (recommended for ASM CLI usage)
Install the CLI globally first:

```bash
npm install -g @mrc2204/agent-smart-memo
```

Then initialize shared config:

```bash
asm init-setup --yes
```

This creates or updates:
```text
~/.config/asm/config.json
```

Then install a runtime target:

```bash
asm install openclaw
asm install paperclip
asm install opencode
```

### Flow B — Plugin-first (direct OpenClaw plugin install)
If you only want the OpenClaw plugin directly, install it through OpenClaw:

```bash
openclaw plugins install @mrc2204/agent-smart-memo
```

Then continue with OpenClaw-side config/bootstrap as needed.

### Important note
The command below is **not the recommended primary flow right now**:

```bash
npx @mrc2204/agent-smart-memo install
```

Use the two supported flows above until CLI bootstrap is fully separated/standardized.

---

## 4) Shared config source-of-truth

ASM now uses a shared config model.

### Canonical shared config
```text
~/.config/asm/config.json
```

### What lives there
Core fields such as:
- `projectWorkspaceRoot`
- `storage.slotDbDir`
- `qdrantHost`
- `qdrantPort`
- `qdrantCollection`
- `qdrantVectorSize`
- `llmBaseUrl`
- `llmApiKey`
- `llmModel`
- `embedBaseUrl`
- `embedBackend`
- `embedModel`
- `embedDimensions`
- `autoCaptureEnabled`
- `autoCaptureMinConfidence`
- `contextWindowMaxTokens`
- `summarizeEveryActions`

### Platform-local config
Platform config should stay minimal.

For OpenClaw, `~/.openclaw/openclaw.json` should mainly keep:
- `enabled`
- `asmConfigPath`
- adapter-local overrides only when truly needed

Example OpenClaw plugin entry:

```json
{
  "enabled": true,
  "config": {
    "asmConfigPath": "/Users/your-user/.config/asm/config.json",
    "slotDbDir": "/Users/your-user/.openclaw/agent-memo",
    "projectWorkspaceRoot": "/Users/your-user/Work/projects"
  }
}
```

This keeps `openclaw.json` from becoming a second core source-of-truth.

---

## 5) OpenClaw quick start

### Install from npm (CLI-first)
```bash
npm install -g @mrc2204/agent-smart-memo
asm init-setup --yes
asm install openclaw --yes
```

### Install plugin directly into OpenClaw (plugin-first)
```bash
openclaw plugins install @mrc2204/agent-smart-memo
```

### Install locally from source
```bash
npm install
npm run build
node bin/asm.mjs init-setup --yes
node bin/asm.mjs install openclaw --yes
```

### Verification
```bash
npm run test:asm-cli
npx tsx tests/test-init-openclaw.ts
npm run build:openclaw
```

---

## 6) Project-aware onboarding flow

ASM supports operator-friendly project onboarding.

### Telegram/OpenClaw command
```text
/project <repo_url>
```

### Current behavior
- resolves repo path/identity when possible
- supports local path import without forced clone
- can reuse an already-registered remote/project identity
- can attach Jira mapping
- can trigger background index flow

Typical path:
1. operator runs `/project <repo_url>`
2. preview shows resolved repo + onboarding choices
3. operator confirms
4. ASM bridges into register / tracker-link / index flow

Relevant areas in the repo include:
- project registry
- onboarding command flows
- background indexing hooks
- lineage-aware retrieval tests

---

## 7) Capability overview

### Memory capabilities
- `memory_search`
- `memory_store`
- `memory_slot_get`
- `memory_slot_set`
- `memory_slot_delete`
- `memory_slot_list`
- `memory_graph_*`

### Project capabilities
- project register / list / inspect flows
- project tracker linking
- project indexing / reindexing
- lifecycle-aware retrieval gating
- hybrid lineage context retrieval

### Platform/operations capabilities
- shared config bootstrap
- OpenClaw install flow
- Paperclip install flow
- OpenCode install flow
- build/package/publish targets

---

## 8) Build targets

### Default build
```bash
npm run build
```

### Explicit targets
```bash
npm run build:openclaw
npm run build:paperclip
npm run build:core
npm run build:all
```

### Packaging
```bash
npm run package:openclaw
npm run package:paperclip
npm run package:core
```

### Pack tarballs
```bash
npm run pack:openclaw
npm run pack:paperclip
npm run pack:core
```

---

## 9) Verification

### CLI / installer verification
```bash
npm run test:asm-cli
npx tsx tests/test-init-openclaw.ts
```

### OpenClaw verification
```bash
npm run test:openclaw
npm run build:openclaw
```

### Paperclip verification
```bash
npm run test:paperclip
npm run build:paperclip
```

### Project-aware targeted verification
```bash
npx tsx tests/test-project-registry.ts
npx tsx tests/test-project-hybrid-lineage.ts
```

---

## 10) Repository layout

```text
src/
  adapters/
    openclaw/
    paperclip/
  core/
    contracts/
    usecases/
    ingest/
  db/
  hooks/
  services/
  shared/
  tools/

bin/
scripts/
docs/
artifacts/
tests/
```

---

## 11) Current positioning

A good public-facing description for this repo is:

> **Agent Smart Memo is a project-aware super memory platform for coding agents, shipped as one package with CLI-first installation for OpenClaw, Paperclip, and OpenCode.**

It helps agents:
- remember conversation/runtime state
- store and retrieve structured + semantic knowledge
- onboard and map projects
- index and reindex repos
- assemble better engineering context
- reuse one shared config and one shared memory core across runtimes

---

## 12) License

MIT © [mrc2204](https://github.com/cong91)

```

### File: CONFIG.example.json
```json
{
  "_readme": "Copy the 'plugins' section below into your ~/.openclaw/openclaw.json",

  "plugins": {
    "allow": ["agent-smart-memo"],
    "slots": {
      "memory": "agent-smart-memo"
    },
    "entries": {
      "agent-smart-memo": {
        "enabled": true,
        "config": {
          "qdrantHost": "localhost",
          "qdrantPort": 6333,
          "qdrantCollection": "openclaw_memory",

          "llmBaseUrl": "https://api.openai.com/v1",
          "llmApiKey": "sk-your-api-key-here",
          "llmModel": "gpt-4o-mini",

          "embedBaseUrl": "http://localhost:11434",
          "embedBackend": "ollama",
          "embedModel": "mxbai-embed-large",
          "embedDimensions": 1024,
          "slotDbDir": "/Users/mrcagents/.openclaw/agent-memo",

          "autoCaptureEnabled": true,
          "autoCaptureMinConfidence": 0.7,
          "contextWindowMaxTokens": 12000,
          "summarizeEveryActions": 6,

          "slotCategories": ["profile", "preferences", "project", "environment", "custom"],
          "maxSlots": 500,
          "injectStateTokenBudget": 500
        }
      }
    }
  }
}

```

### File: openclaw.plugin.json
```json
{
  "id": "agent-smart-memo",
  "kind": "memory",
  "configSchema": {
    "type": "object",
    "additionalProperties": false,
    "properties": {
      "asmConfigPath": {
        "type": "string",
        "description": "Path to shared ASM config source-of-truth used by the OpenClaw plugin runtime."
      }
    }
  },
  "uiHints": {
    "asmConfigPath": {
      "label": "ASM Config Path",
      "placeholder": "/Users/you/.config/asm/config.json"
    }
  }
}

```

### File: tsconfig.base.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "resolveJsonModule": true,
    "allowSyntheticDefaultImports": true,
    "rootDir": "./src"
  }
}

```

### File: tsconfig.core.json
```json
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist-core"
  },
  "files": ["src/entries/core.ts"],
  "exclude": ["node_modules", "dist", "dist-openclaw", "dist-paperclip", "dist-core", "tests"]
}

```

### File: tsconfig.json
```json
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "dist-openclaw", "dist-paperclip", "dist-core", "tests"]
}

```

### File: tsconfig.openclaw.json
```json
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist-openclaw"
  },
  "files": ["src/index.ts", "src/cli/platform-installers.ts", "src/shared/asm-config.ts", "src/types/mjs.d.ts"],
  "exclude": ["node_modules", "dist", "dist-openclaw", "dist-paperclip", "dist-core", "tests"]
}

```

### File: tsconfig.paperclip.json
```json
{
  "extends": "./tsconfig.base.json",
  "compilerOptions": {
    "outDir": "./dist-paperclip"
  },
  "files": ["src/entries/paperclip.ts"],
  "exclude": ["node_modules", "dist", "dist-openclaw", "dist-paperclip", "dist-core", "tests"]
}

```


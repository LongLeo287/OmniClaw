---
id: opencode
type: knowledge
owner: OA_Triage
---
# opencode
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "$schema": "https://json.schemastore.org/package.json",
  "name": "opencode",
  "description": "AI-powered development tool",
  "private": true,
  "type": "module",
  "packageManager": "bun@1.3.11",
  "scripts": {
    "dev": "bun run --cwd packages/opencode --conditions=browser src/index.ts",
    "dev:desktop": "bun --cwd packages/desktop tauri dev",
    "dev:web": "bun --cwd packages/app dev",
    "dev:console": "ulimit -n 10240 2>/dev/null; bun run --cwd packages/console/app dev",
    "dev:storybook": "bun --cwd packages/storybook storybook",
    "typecheck": "bun turbo typecheck",
    "prepare": "husky",
    "random": "echo 'Random script'",
    "hello": "echo 'Hello World!'",
    "test": "echo 'do not run tests from root' && exit 1"
  },
  "workspaces": {
    "packages": [
      "packages/*",
      "packages/console/*",
      "packages/sdk/js",
      "packages/slack"
    ],
    "catalog": {
      "@effect/platform-node": "4.0.0-beta.43",
      "@types/bun": "1.3.11",
      "@types/cross-spawn": "6.0.6",
      "@octokit/rest": "22.0.0",
      "@hono/zod-validator": "0.4.2",
      "ulid": "3.0.1",
      "@kobalte/core": "0.13.11",
      "@types/luxon": "3.7.1",
      "@types/node": "22.13.9",
      "@types/semver": "7.7.1",
      "@tsconfig/node22": "22.0.2",
      "@tsconfig/bun": "1.0.9",
      "@cloudflare/workers-types": "4.20251008.0",
      "@openauthjs/openauth": "0.0.0-20250322224806",
      "@pierre/diffs": "1.1.0-beta.18",
      "@solid-primitives/storage": "4.3.3",
      "@tailwindcss/vite": "4.1.11",
      "diff": "8.0.2",
      "dompurify": "3.3.1",
      "drizzle-kit": "1.0.0-beta.19-d95b7a4",
      "drizzle-orm": "1.0.0-beta.19-d95b7a4",
      "effect": "4.0.0-beta.43",
      "ai": "6.0.138",
      "cross-spawn": "7.0.6",
      "hono": "4.10.7",
      "hono-openapi": "1.1.2",
      "fuzzysort": "3.1.0",
      "luxon": "3.6.1",
      "marked": "17.0.1",
      "marked-shiki": "1.2.1",
      "remend": "1.3.0",
      "@playwright/test": "1.51.0",
      "typescript": "5.8.2",
      "@typescript/native-preview": "7.0.0-dev.20251207.1",
      "zod": "4.1.8",
      "remeda": "2.26.0",
      "shiki": "3.20.0",
      "solid-list": "0.3.0",
      "tailwindcss": "4.1.11",
      "virtua": "0.42.3",
      "vite": "7.1.4",
      "@solidjs/meta": "0.29.4",
      "@solidjs/router": "0.15.4",
      "@solidjs/start": "https://pkg.pr.new/@solidjs/start@dfb2020",
      "solid-js": "1.9.10",
      "vite-plugin-solid": "2.11.10"
    }
  },
  "devDependencies": {
    "@actions/artifact": "5.0.1",
    "@tsconfig/bun": "catalog:",
    "@types/mime-types": "3.0.1",
    "@typescript/native-preview": "catalog:",
    "glob": "13.0.5",
    "husky": "9.1.7",
    "prettier": "3.6.2",
    "semver": "^7.6.0",
    "sst": "3.18.10",
    "turbo": "2.8.13"
  },
  "dependencies": {
    "@aws-sdk/client-s3": "3.933.0",
    "@opencode-ai/plugin": "workspace:*",
    "@opencode-ai/script": "workspace:*",
    "@opencode-ai/sdk": "workspace:*",
    "typescript": "catalog:"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/anomalyco/opencode"
  },
  "license": "MIT",
  "prettier": {
    "semi": false,
    "printWidth": 120
  },
  "trustedDependencies": [
    "esbuild",
    "protobufjs",
    "tree-sitter",
    "tree-sitter-bash",
    "tree-sitter-powershell",
    "web-tree-sitter",
    "electron"
  ],
  "overrides": {
    "@types/bun": "catalog:",
    "@types/node": "catalog:"
  },
  "patchedDependencies": {
    "@standard-community/standard-openapi@0.2.9": "patches/@standard-community%2Fstandard-openapi@0.2.9.patch",
    "solid-js@1.9.10": "patches/solid-js@1.9.10.patch",
    "@ai-sdk/provider-utils@4.0.21": "patches/@ai-sdk%2Fprovider-utils@4.0.21.patch",
    "@ai-sdk/anthropic@3.0.64": "patches/@ai-sdk%2Fanthropic@3.0.64.patch"
  }
}

```

### File: README.md
```md
# Antigravity + Gemini CLI OAuth Plugin for Opencode

[![npm version](https://img.shields.io/npm/v/opencode-antigravity-auth.svg)](https://www.npmjs.com/package/opencode-antigravity-auth)
[![npm beta](https://img.shields.io/npm/v/opencode-antigravity-auth/beta.svg?label=beta)](https://www.npmjs.com/package/opencode-antigravity-auth)
[![npm downloads](https://img.shields.io/npm/dw/opencode-antigravity-auth.svg)](https://www.npmjs.com/package/opencode-antigravity-auth)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![X (Twitter)](https://img.shields.io/badge/X-@dopesalmon-000000?style=flat&logo=x)](https://x.com/dopesalmon)

Enable Opencode to authenticate against **Antigravity** (Google's IDE) via OAuth so you can use Antigravity rate limits and access models like `gemini-3.1-pro` and `claude-opus-4-6-thinking` with your Google credentials.

## What You Get

- **Claude Opus 4.6, Sonnet 4.6** and **Gemini 3.1 Pro/Flash** via Google OAuth
- **Multi-account support** — add multiple Google accounts, auto-rotates when rate-limited
- **Dual quota system** — access both Antigravity and Gemini CLI quotas from one plugin
- **Thinking models** — extended thinking for Claude and Gemini 3 with configurable budgets
- **Google Search grounding** — enable web search for Gemini models (auto or always-on)
- **Auto-recovery** — handles session errors and tool failures automatically
- **Plugin compatible** — works alongside other OpenCode plugins (oh-my-opencode, dcp, etc.)

---

<details open>
<summary><b>⚠️ Terms of Service Warning — Read Before Installing</b></summary>

> [!CAUTION]
> Using this plugin (and any proxy for antgravity) violate Google's Terms of Service. A number of users have reported their Google accounts being **banned** or **shadow-banned** (restricted access without explicit notification).
>
> **By using this plugin, you acknowledge:**
> - This is an unofficial tool not endorsed by Google
> - Your account may be suspended or permanently banned
> - You assume all risks associated with using this plugin
>

</details>

---

## Installation

<details open>
<summary><b>For Humans</b></summary>

**Option A: Let an LLM do it**

Paste this into any LLM agent (Claude Code, OpenCode, Cursor, etc.):

```
Install the opencode-antigravity-auth plugin and add the Antigravity model definitions to ~/.config/opencode/opencode.json by following: https://raw.githubusercontent.com/NoeFabris/opencode-antigravity-auth/dev/README.md
```

**Option B: Manual setup**

1. **Add the plugin** to `~/.config/opencode/opencode.json`:

   ```json
   {
     "plugin": ["opencode-antigravity-auth@latest"]
   }
   ```

   > Want bleeding-edge features? Use `opencode-antigravity-auth@beta` instead.

2. **Login** with your Google account:

   ```bash
   opencode auth login
   ```

3. **Add models** — choose one:
   - Run `opencode auth login` → Google → OAuth with Google (Antigravity) → select **"Configure models in opencode.json"** (auto-configures all models)
   - Or manually copy the [full configuration](#models) below

4. **Use it:**

   ```bash
   opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
   ```

</details>

<details>
<summary><b>For LLM Agents</b></summary>

### Step-by-Step Instructions

1. Edit the OpenCode configuration file at `~/.config/opencode/opencode.json`
   
   > **Note**: This path works on all platforms. On Windows, `~` resolves to your user home directory (e.g., `C:\Users\YourName`).

2. Add the plugin to the `plugin` array

3. Add the model definitions from the [Full models configuration](#models) section

4. Set `provider` to `"google"` and choose a model

### Verification

```bash
opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
```

</details>

---

## Models

### Model Reference

**Antigravity quota** (default routing for Claude and Gemini):

| Model | Variants | Notes |
|-------|----------|-------|
| `antigravity-gemini-3-pro` | low, high | Gemini 3 Pro with thinking |
| `antigravity-gemini-3.1-pro` | low, high | Gemini 3.1 Pro with thinking (rollout-dependent) |
| `antigravity-gemini-3-flash` | minimal, low, medium, high | Gemini 3 Flash with thinking |
| `antigravity-claude-sonnet-4-6` | — | Claude Sonnet 4.6 |
| `antigravity-claude-opus-4-6-thinking` | low, max | Claude Opus 4.6 with extended thinking |

**Gemini CLI quota** (separate from Antigravity; used when `cli_first` is true or as fallback):

| Model | Notes |
|-------|-------|
| `gemini-2.5-flash` | Gemini 2.5 Flash |
| `gemini-2.5-pro` | Gemini 2.5 Pro |
| `gemini-3-flash-preview` | Gemini 3 Flash (preview) |
| `gemini-3-pro-preview` | Gemini 3 Pro (preview) |
| `gemini-3.1-pro-preview` | Gemini 3.1 Pro (preview, rollout-dependent) |
| `gemini-3.1-pro-preview-customtools` | Gemini 3.1 Pro Preview Custom Tools (preview, rollout-dependent) |

> **Routing Behavior:**
> - **Antigravity-first (default):** Gemini models use Antigravity quota across accounts.
> - **CLI-first (`cli_first: true`):** Gemini models use Gemini CLI quota first.
> - When a Gemini quota pool is exhausted, the plugin automatically falls back to the other pool.
> - Claude and image models always use Antigravity.
> Model names are automatically transformed for the target API (e.g., `antigravity-gemini-3-flash` → `gemini-3-flash-preview` for CLI).

**Using variants:**
```bash
opencode run "Hello" --model=google/antigravity-claude-opus-4-6-thinking --variant=max
```

For details on variant configuration and thinking levels, see [docs/MODEL-VARIANTS.md](docs/MODEL-VARIANTS.md).

<details>
<summary><b>Full models configuration (copy-paste ready)</b></summary>

Add this to your `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-antigravity-auth@latest"],
  "provider": {
    "google": {
      "models": {
        "antigravity-gemini-3-pro": {
          "name": "Gemini 3 Pro (Antigravity)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingLevel": "low" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-gemini-3.1-pro": {
          "name": "Gemini 3.1 Pro (Antigravity)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingLevel": "low" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-gemini-3-flash": {
          "name": "Gemini 3 Flash (Antigravity)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "minimal": { "thinkingLevel": "minimal" },
            "low": { "thinkingLevel": "low" },
            "medium": { "thinkingLevel": "medium" },
            "high": { "thinkingLevel": "high" }
          }
        },
        "antigravity-claude-sonnet-4-6": {
          "name": "Claude Sonnet 4.6 (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "antigravity-claude-opus-4-6-thinking": {
          "name": "Claude Opus 4.6 Thinking (Antigravity)",
          "limit": { "context": 200000, "output": 64000 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] },
          "variants": {
            "low": { "thinkingConfig": { "thinkingBudget": 8192 } },
            "max": { "thinkingConfig": { "thinkingBudget": 32768 } }
          }
        },
        "gemini-2.5-flash": {
          "name": "Gemini 2.5 Flash (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-2.5-pro": {
          "name": "Gemini 2.5 Pro (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3-flash-preview": {
          "name": "Gemini 3 Flash Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65536 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3-pro-preview": {
          "name": "Gemini 3 Pro Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3.1-pro-preview": {
          "name": "Gemini 3.1 Pro Preview (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        },
        "gemini-3.1-pro-preview-customtools": {
          "name": "Gemini 3.1 Pro Preview Custom Tools (Gemini CLI)",
          "limit": { "context": 1048576, "output": 65535 },
          "modalities": { "input": ["text", "image", "pdf"], "output": ["text"] }
        }
      }
    }
  }
}
```

> **Backward Compatibility:** Legacy model names with `antigravity-` prefix (e.g., `antigravity-gemini-3-flash`) still work. The plugin automatically handles model name transformation for both Antigravity and Gemini CLI APIs.

</details>

---

## Multi-Account Setup

Add multiple Google accounts for higher combined quotas. The plugin automatically rotates between accounts when one is rate-limited.

```bash
opencode auth login  # Run again to add more accounts
```

**Account management options (via `opencode auth login`):**
- **Configure models** — Auto-configure all plugin models in opencode.json
- **Check quotas** — View remaining API quota for each account
- **Manage accounts** — Enable/disable specific accounts for rotation

For details on load balancing, dual quota pools, and account storage, see [docs/MULTI-ACCOUNT.md](docs/MULTI-ACCOUNT.md).

---

## Troubleshoot

> **Quick Reset**: Most issues can be resolved by deleting `~/.config/opencode/antigravity-accounts.json` and running `opencode auth login` again.

### Configuration Path (All Platforms)

OpenCode uses `~/.config/opencode/` on **all platforms** including Windows.

| File | Path |
|------|------|
| Main config | `~/.config/opencode/opencode.json` |
| Accounts | `~/.config/opencode/antigravity-accounts.json` |
| Plugin config | `~/.config/opencode/antigravity.json` |
| Debug logs | `~/.config/opencode/antigravity-logs/` |

> **Windows users**: `~` resolves to your user home directory (e.g., `C:\Users\YourName`). Do NOT use `%APPDATA%`.

> **Custom path**: Set `OPENCODE_CONFIG_DIR` environment variable to use a custom location.

> **Windows migration**: If upgrading from plugin v1.3.x or earlier, the plugin will automatically find your existing config in `%APPDATA%\opencode\` and use it. New installations use `~/.config/opencode/`.

---

### Multi-Account Auth Issues

If you encounter authentication issues with multiple accounts:

1. Delete the accounts file:
   ```bash
   rm ~/.config/opencode/antigravity-accounts.json
   ```
2. Re-authenticate:
   ```bash
   opencode auth login
   ```

---

### 403 Permission Denied (`rising-fact-p41fc`)

**Error:**
```
Permission 'cloudaicompanion.companions.generateChat' denied on resource 
'//cloudaicompanion.googleapis.com/projects/rising-fact-p41fc/locations/global'
```

**Cause:** Plugin falls back to a default project ID when no valid project is found. This works for Antigravity but fails for Gemini CLI models.

**Solution:**
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create or select a project
3. Enable the **Gemini for Google Cloud API** (`cloudaicompanion.googleapis.com`)
4. Add `projectId` to your accounts file:
   ```json
   {
     "accounts": [
       {
         "email": "your@email.com",
         "refreshToken": "...",
         "projectId": "your-project-id"
       }
     ]
   }
   ```

> **Note**: Do this for each account in a multi-account setup.

---

### Gemini Model Not Found

Add this to your `google` provider config:

```json
{
  "provider": {
    "google": {
      "npm": "@ai-sdk/google",
      "models": { ... }
    }
  }
}
```

---

### Gemini 3 Models 400 Error ("Unknown name 'parameters'")

**Error:**
```
Invalid JSON payload received. Unknown name "parameters" at 'request.tools[0]'
```

**Causes:**
- Tool schema incompatibility with Gemini's strict protobuf validation
- MCP servers with malformed schemas
- Plugin version regression

**Solutions:**
1. **Update to latest beta:**
   ```json
   { "plugin": ["opencode-antigravity-auth@beta"] }
   ```

2. **Disable MCP servers** one-by-one to find the problematic one

3. **Add npm override:**
   ```json
   { "provider": { "google": { "npm": "@ai-sdk/google" } } }
   ```

---

### MCP Servers Causing Errors

Some MCP servers have schemas incompatible with Antigravity's strict JSON format.

**Common symptom:**
```bash
Invalid function name must start with a letter or underscore
```

Sometimes it shows up as:
```bash
GenerateContentRequest.tools[0].function_declarations[12].name: Invalid function name must start with a letter or underscore
```

This usually means an MCP tool name starts with a number (for example, a 1mcp key like `1mcp_*`). Rename the MCP key to start with a letter (e.g., `gw`) or disable that MCP entry for Antigravity models.

**Diagnosis:**
1. Disable all MCP servers in your config
2. Enable one-by-one until error reappears
3. Report the specific MCP in a [GitHub issue](https://github.com/NoeFabris/opencode-antigravity-auth/issues)

---

### "All Accounts Rate-Limited" (But Quota Available)

**Cause:** Cascade bug in `clearExpiredRateLimits()` in hybrid mode (fixed in recent beta).

**Solutions:**
1. Update to latest beta version
2. If persists, delete accounts file and re-authenticate
3. Try switching `account_selection_strategy` to `"sticky"` in `antigravity.json`

---

### Session Recovery

If you encounter errors during a session:
1. Type `continue` to trigger the recovery mechanism
2. If blocked, use `/undo` to revert to pre-error state
3. Retry the operation

---

### Using with Oh-My-OpenCode

**Important:** Disable the built-in Google auth to prevent conflicts:

```json
// ~/.config/opencode/oh-my-opencode.json
{
  "google_auth": false,
  "agents": {
    "frontend-ui-ux-engineer": { "model": "google/antigravity-gemini-3-pro" },
    "document-writer": { "model": "google/antigravity-gemini-3-flash" }
  }
}
```

---

### Infinite `.tmp` Files Created

**Cause:** When account is rate-limited and plugin retries infinitely, it creates many temp files.

**Workaround:**
1. Stop OpenCode
2. Clean up: `rm ~/.config/opencode/*.tmp`
3. Add more accounts or wait for rate limi
... [TRUNCATED]
```

### File: github\package.json
```json
{
  "name": "github",
  "module": "index.ts",
  "type": "module",
  "private": true,
  "license": "MIT",
  "devDependencies": {
    "@types/bun": "catalog:"
  },
  "peerDependencies": {
    "typescript": "^5"
  },
  "dependencies": {
    "@actions/core": "1.11.1",
    "@actions/github": "6.0.1",
    "@octokit/graphql": "9.0.1",
    "@octokit/rest": "catalog:",
    "@opencode-ai/sdk": "workspace:*"
  }
}

```

### File: github\README.md
```md
# opencode GitHub Action

A GitHub Action that integrates [opencode](https://opencode.ai) directly into your GitHub workflow.

Mention `/opencode` in your comment, and opencode will execute tasks within your GitHub Actions runner.

## Features

#### Explain an issue

Leave the following comment on a GitHub issue. `opencode` will read the entire thread, including all comments, and reply with a clear explanation.

```
/opencode explain this issue
```

#### Fix an issue

Leave the following comment on a GitHub issue. opencode will create a new branch, implement the changes, and open a PR with the changes.

```
/opencode fix this
```

#### Review PRs and make changes

Leave the following comment on a GitHub PR. opencode will implement the requested change and commit it to the same PR.

```
Delete the attachment from S3 when the note is removed /oc
```

#### Review specific code lines

Leave a comment directly on code lines in the PR's "Files" tab. opencode will automatically detect the file, line numbers, and diff context to provide precise responses.

```
[Comment on specific lines in Files tab]
/oc add error handling here
```

When commenting on specific lines, opencode receives:

- The exact file being reviewed
- The specific lines of code
- The surrounding diff context
- Line number information

This allows for more targeted requests without needing to specify file paths or line numbers manually.

## Installation

Run the following command in the terminal from your GitHub repo:

```bash
opencode github install
```

This will walk you through installing the GitHub app, creating the workflow, and setting up secrets.

### Manual Setup

1. Install the GitHub app https://github.com/apps/opencode-agent. Make sure it is installed on the target repository.
2. Add the following workflow file to `.github/workflows/opencode.yml` in your repo. Set the appropriate `model` and required API keys in `env`.

   ```yml
   name: opencode

   on:
     issue_comment:
       types: [created]
     pull_request_review_comment:
       types: [created]

   jobs:
     opencode:
       if: |
         contains(github.event.comment.body, '/oc') ||
         contains(github.event.comment.body, '/opencode')
       runs-on: ubuntu-latest
       permissions:
         id-token: write
       steps:
          - name: Checkout repository
            uses: actions/checkout@v6
            with:
              fetch-depth: 1
              persist-credentials: false

          - name: Run opencode
           uses: anomalyco/opencode/github@latest
           env:
             ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
             GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
           with:
             model: anthropic/claude-sonnet-4-20250514
             use_github_token: true
   ```

3. Store the API keys in secrets. In your organization or project **settings**, expand **Secrets and variables** on the left and select **Actions**. Add the required API keys.

## Support

This is an early release. If you encounter issues or have feedback, please create an issue at https://github.com/anomalyco/opencode/issues.

## Development

To test locally:

1. Navigate to a test repo (e.g. `hello-world`):

   ```bash
   cd hello-world
   ```

2. Run:

   ```bash
   MODEL=anthropic/claude-sonnet-4-20250514 \
     ANTHROPIC_API_KEY=sk-ant-api03-1234567890 \
     GITHUB_RUN_ID=dummy \
     MOCK_TOKEN=github_pat_1234567890 \
     MOCK_EVENT='{"eventName":"issue_comment",...}' \
     bun /path/to/opencode/github/index.ts
   ```

   - `MODEL`: The model used by opencode. Same as the `MODEL` defined in the GitHub workflow.
   - `ANTHROPIC_API_KEY`: Your model provider API key. Same as the keys defined in the GitHub workflow.
   - `GITHUB_RUN_ID`: Dummy value to emulate GitHub action environment.
   - `MOCK_TOKEN`: A GitHub personal access token. This token is used to verify you have `admin` or `write` access to the test repo. Generate a token [here](https://github.com/settings/personal-access-tokens).
   - `MOCK_EVENT`: Mock GitHub event payload (see templates below).
   - `/path/to/opencode`: Path to your cloned opencode repo. `bun /path/to/opencode/github/index.ts` runs your local version of `opencode`.

### Issue comment event

```
MOCK_EVENT='{"eventName":"issue_comment","repo":{"owner":"sst","repo":"hello-world"},"actor":"fwang","payload":{"issue":{"number":4},"comment":{"id":1,"body":"hey opencode, summarize thread"}}}'
```

Replace:

- `"owner":"sst"` with repo owner
- `"repo":"hello-world"` with repo name
- `"actor":"fwang"` with the GitHub username of commenter
- `"number":4` with the GitHub issue id
- `"body":"hey opencode, summarize thread"` with comment body

### Issue comment with image attachment.

```
MOCK_EVENT='{"eventName":"issue_comment","repo":{"owner":"sst","repo":"hello-world"},"actor":"fwang","payload":{"issue":{"number":4},"comment":{"id":1,"body":"hey opencode, what is in my image ![Image](https://github.com/user-attachments/assets/xxxxxxxx)"}}}'
```

Replace the image URL `https://github.com/user-attachments/assets/xxxxxxxx` with a valid GitHub attachment (you can generate one by commenting with an image in any issue).

### PR comment event

```
MOCK_EVENT='{"eventName":"issue_comment","repo":{"owner":"sst","repo":"hello-world"},"actor":"fwang","payload":{"issue":{"number":4,"pull_request":{}},"comment":{"id":1,"body":"hey opencode, summarize thread"}}}'
```

### PR review comment event

```
MOCK_EVENT='{"eventName":"pull_request_review_comment","repo":{"owner":"sst","repo":"hello-world"},"actor":"fwang","payload":{"pull_request":{"number":7},"comment":{"id":1,"body":"hey opencode, add error handling","path":"src/components/Button.tsx","diff_hunk":"@@ -45,8 +45,11 @@\n- const handleClick = () => {\n-   console.log('clicked')\n+ const handleClick = useCallback(() => {\n+   console.log('clicked')\n+   doSomething()\n+ }, [doSomething])","line":47,"original_line":45,"position":10,"commit_id":"abc123","original_commit_id":"def456"}}}'
```

```

### File: .opencode\glossary\README.md
```md
# Locale Glossaries

Use this folder for locale-specific translation guidance that supplements `.opencode/agent/translator.md`.

The global glossary in `translator.md` remains the source of truth for shared do-not-translate terms (commands, code, paths, product names, etc.). These locale files capture community learnings about phrasing and terminology preferences.

## File Naming

- One file per locale
- Use lowercase locale slugs that match docs locales when possible (for example, `zh-cn.md`, `zh-tw.md`)
- If only language-level guidance exists, use the language code (for example, `fr.md`)
- Some repo locale slugs may be aliases/non-BCP47 for consistency (for example, `br` for Brazilian Portuguese / `pt-BR`)

## What To Put In A Locale File

- **Sources**: PRs/issues/discussions that motivated the guidance
- **Do Not Translate (Locale Additions)**: locale-specific terms or casing decisions
- **Preferred Terms**: recurring UI/docs words with preferred translations
- **Guidance**: tone, style, and consistency notes
- **Avoid** (optional): common literal translations or wording we should avoid
- If the repo uses a locale alias slug, document the alias in **Guidance** (for example, prose may mention `pt-BR` while config/examples use `br`)

Prefer guidance that is:

- Repeated across multiple docs/screens
- Easy to apply consistently
- Backed by a community contribution or review discussion

## Template

```md
# <locale> Glossary

## Sources

- PR #12345: https://github.com/anomalyco/opencode/pull/12345

## Do Not Translate (Locale Additions)

- `OpenCode` (preserve casing)

## Preferred Terms

| English | Preferred | Notes     |
| ------- | --------- | --------- |
| prompt  | ...       | preferred |
| session | ...       | preferred |

## Guidance

- Prefer natural phrasing over literal translation

## Avoid

- Avoid ... when ...
```

## Contribution Notes

- Mark entries as preferred when they may evolve
- Keep examples short
- Add or update the `Sources` section whenever you add a new rule
- Prefer PR-backed guidance over invented term mappings; start with general guidance if no term-level corrections exist yet

```

### File: packages\app\package.json
```json
{
  "name": "@opencode-ai/app",
  "version": "1.3.13",
  "description": "",
  "type": "module",
  "exports": {
    ".": "./src/index.ts",
    "./vite": "./vite.js",
    "./index.css": "./src/index.css"
  },
  "scripts": {
    "typecheck": "tsgo -b",
    "start": "vite",
    "dev": "vite",
    "build": "vite build",
    "serve": "vite preview",
    "test": "bun run test:unit",
    "test:ci": "mkdir -p .artifacts/unit && bun test --preload ./happydom.ts ./src --reporter=junit --reporter-outfile=.artifacts/unit/junit.xml",
    "test:unit": "bun test --preload ./happydom.ts ./src",
    "test:unit:watch": "bun test --watch --preload ./happydom.ts ./src",
    "test:e2e": "playwright test",
    "test:e2e:local": "bun script/e2e-local.ts",
    "test:e2e:ui": "playwright test --ui",
    "test:e2e:report": "playwright show-report e2e/playwright-report"
  },
  "license": "MIT",
  "devDependencies": {
    "@happy-dom/global-registrator": "20.0.11",
    "@playwright/test": "1.57.0",
    "@tailwindcss/vite": "catalog:",
    "@tsconfig/bun": "1.0.9",
    "@types/bun": "catalog:",
    "@types/luxon": "catalog:",
    "@types/node": "catalog:",
    "@typescript/native-preview": "catalog:",
    "typescript": "catalog:",
    "vite": "catalog:",
    "vite-plugin-icons-spritesheet": "3.0.1",
    "vite-plugin-solid": "catalog:"
  },
  "dependencies": {
    "@kobalte/core": "catalog:",
    "@opencode-ai/sdk": "workspace:*",
    "@opencode-ai/ui": "workspace:*",
    "@opencode-ai/util": "workspace:*",
    "@shikijs/transformers": "3.9.2",
    "@solid-primitives/active-element": "2.1.3",
    "@solid-primitives/audio": "1.4.2",
    "@solid-primitives/event-bus": "1.1.2",
    "@solid-primitives/event-listener": "2.4.5",
    "@solid-primitives/i18n": "2.2.1",
    "@solid-primitives/media": "2.3.3",
    "@solid-primitives/resize-observer": "2.1.5",
    "@solid-primitives/scroll": "2.1.3",
    "@solid-primitives/storage": "catalog:",
    "@solid-primitives/timer": "1.4.4",
    "@solid-primitives/websocket": "1.3.1",
    "@solidjs/meta": "catalog:",
    "@solidjs/router": "catalog:",
    "@tanstack/solid-query": "5.91.4",
    "@thisbeyond/solid-dnd": "0.7.5",
    "diff": "catalog:",
    "effect": "catalog:",
    "fuzzysort": "catalog:",
    "ghostty-web": "github:anomalyco/ghostty-web#main",
    "luxon": "catalog:",
    "marked": "catalog:",
    "marked-shiki": "catalog:",
    "remeda": "catalog:",
    "shiki": "catalog:",
    "solid-js": "catalog:",
    "solid-list": "catalog:",
    "tailwindcss": "catalog:",
    "virtua": "catalog:",
    "zod": "catalog:"
  }
}

```

### File: packages\app\README.md
```md
## Usage

Dependencies for these templates are managed with [pnpm](https://pnpm.io) using `pnpm up -Lri`.

This is the reason you see a `pnpm-lock.yaml`. That said, any package manager will work. This file can safely be removed once you clone a template.

```bash
$ npm install # or pnpm install or yarn install
```

### Learn more on the [Solid Website](https://solidjs.com) and come chat with us on our [Discord](https://discord.com/invite/solidjs)

## Available Scripts

In the project directory, you can run:

### `npm run dev` or `npm start`

Runs the app in the development mode.<br>
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br>

### `npm run build`

Builds the app for production to the `dist` folder.<br>
It correctly bundles Solid in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br>
Your app is ready to be deployed!

## E2E Testing

Playwright starts the Vite dev server automatically via `webServer`, and UI tests need an opencode backend (defaults to `localhost:4096`).
Use the local runner to create a temp sandbox, seed data, and run the tests.

```bash
bunx playwright install
bun run test:e2e:local
bun run test:e2e:local -- --grep "settings"
```

Environment options:

- `PLAYWRIGHT_SERVER_HOST` / `PLAYWRIGHT_SERVER_PORT` (backend address, default: `localhost:4096`)
- `PLAYWRIGHT_PORT` (Vite dev server port, default: `3000`)
- `PLAYWRIGHT_BASE_URL` (override base URL, default: `http://localhost:<PLAYWRIGHT_PORT>`)

## Deployment

You can deploy the `dist` folder to any static host provider (netlify, surge, now, etc.)

```

### File: packages\containers\README.md
```md
# CI containers

Prebuilt images intended to speed up GitHub Actions jobs by baking in
large, slow-to-install dependencies. These are designed for Linux jobs
that can use `job.container` in workflows.

Images

- `base`: Ubuntu 24.04 with common build tools and utilities
- `bun-node`: `base` plus Bun and Node.js 24
- `rust`: `bun-node` plus Rust (stable, minimal profile)
- `tauri-linux`: `rust` plus Tauri Linux build dependencies
- `publish`: `bun-node` plus Docker CLI and AUR tooling

Build

```
REGISTRY=ghcr.io/anomalyco TAG=24.04 bun ./packages/containers/script/build.ts
REGISTRY=ghcr.io/anomalyco TAG=24.04 bun ./packages/containers/script/build.ts --push
```

Workflow usage

```
jobs:
  build-cli:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/anomalyco/build/bun-node:24.04
```

Notes

- These images only help Linux jobs. macOS and Windows jobs cannot run
  inside Linux containers.
- `--push` publishes multi-arch (amd64 + arm64) images using Buildx.
- If a job uses Docker Buildx, the container needs access to the host
  Docker daemon (or `docker-in-docker` with privileged mode).

```

### File: packages\desktop\package.json
```json
{
  "name": "@opencode-ai/desktop",
  "private": true,
  "version": "1.3.13",
  "type": "module",
  "license": "MIT",
  "scripts": {
    "typecheck": "tsgo -b",
    "predev": "bun ./scripts/predev.ts",
    "dev": "vite",
    "build": "bun run typecheck && vite build",
    "preview": "vite preview",
    "tauri": "tauri"
  },
  "dependencies": {
    "@opencode-ai/app": "workspace:*",
    "@opencode-ai/ui": "workspace:*",
    "@solid-primitives/i18n": "2.2.1",
    "@solid-primitives/storage": "catalog:",
    "@tauri-apps/api": "^2",
    "@tauri-apps/plugin-clipboard-manager": "~2",
    "@tauri-apps/plugin-deep-link": "~2",
    "@tauri-apps/plugin-dialog": "~2",
    "@tauri-apps/plugin-opener": "^2",
    "@tauri-apps/plugin-os": "~2",
    "@tauri-apps/plugin-notification": "~2",
    "@tauri-apps/plugin-process": "~2",
    "@tauri-apps/plugin-shell": "~2",
    "@tauri-apps/plugin-store": "~2",
    "@tauri-apps/plugin-updater": "~2",
    "@tauri-apps/plugin-http": "~2",
    "@tauri-apps/plugin-window-state": "~2",
    "solid-js": "catalog:",
    "@solidjs/meta": "catalog:"
  },
  "devDependencies": {
    "@actions/artifact": "4.0.0",
    "@tauri-apps/cli": "^2",
    "@types/bun": "catalog:",
    "@typescript/native-preview": "catalog:",
    "typescript": "~5.6.2",
    "vite": "catalog:"
  }
}

```

### File: packages\desktop\README.md
```md
# OpenCode Desktop

Native OpenCode desktop app, built with Tauri v2.

## Prerequisites

Building the desktop app requires additional Tauri dependencies (Rust toolchain, platform-specific libraries). See the [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/) for setup instructions.

## Development

From the repo root:

```bash
bun install
bun run --cwd packages/desktop tauri dev
```

## Build

```bash
bun run --cwd packages/desktop tauri build
```

## Troubleshooting

### Rust compiler not found

If you see errors about Rust not being found, install it via [rustup](https://rustup.rs/):

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

```

### File: packages\docs\README.md
```md
# Mintlify Starter Kit

Use the starter kit to get your docs deployed and ready to customize.

Click the green **Use this template** button at the top of this repo to copy the Mintlify starter kit. The starter kit contains examples with

- Guide pages
- Navigation
- Customizations
- API reference pages
- Use of popular components

**[Follow the full quickstart guide](https://starter.mintlify.com/quickstart)**

## Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mint) to preview your documentation changes locally. To install, use the following command:

```
npm i -g mint
```

Run the following command at the root of your documentation, where your `docs.json` is located:

```
mint dev
```

View your local preview at `http://localhost:3000`.

## Publishing changes

Install our GitHub app from your [dashboard](https://dashboard.mintlify.com/settings/organization/github-app) to propagate changes from your repo to your deployment. Changes are deployed to production automatically after pushing to the default branch.

## Need help?

### Troubleshooting

- If your dev environment isn't running: Run `mint update` to ensure you have the most recent version of the CLI.
- If a page loads as a 404: Make sure you are running in a folder with a valid `docs.json`.

### Resources

- [Mintlify documentation](https://mintlify.com/docs)

```

### File: packages\opencode\package.json
```json
{
  "$schema": "https://json.schemastore.org/package.json",
  "version": "1.3.13",
  "name": "opencode",
  "type": "module",
  "license": "MIT",
  "private": true,
  "scripts": {
    "prepare": "effect-language-service patch || true",
    "typecheck": "tsgo --noEmit",
    "test": "bun test --timeout 30000",
    "test:ci": "mkdir -p .artifacts/unit && bun test --timeout 30000 --reporter=junit --reporter-outfile=.artifacts/unit/junit.xml",
    "build": "bun run script/build.ts",
    "upgrade-opentui": "bun run script/upgrade-opentui.ts",
    "dev": "bun run --conditions=browser ./src/index.ts",
    "random": "echo 'Random script updated at $(date)' && echo 'Change queued successfully' && echo 'Another change made' && echo 'Yet another change' && echo 'One more change' && echo 'Final change' && echo 'Another final change' && echo 'Yet another final change'",
    "clean": "echo 'Cleaning up...' && rm -rf node_modules dist",
    "lint": "echo 'Running lint checks...' && bun test --coverage",
    "format": "echo 'Formatting code...' && bun run --prettier --write src/**/*.ts",
    "docs": "echo 'Generating documentation...' && find src -name '*.ts' -exec echo 'Processing: {}' \\;",
    "deploy": "echo 'Deploying application...' && bun run build && echo 'Deployment completed successfully'",
    "db": "bun drizzle-kit"
  },
  "bin": {
    "opencode": "./bin/opencode"
  },
  "randomField": "this-is-a-random-value-12345",
  "exports": {
    "./*": "./src/*.ts"
  },
  "imports": {
    "#db": {
      "bun": "./src/storage/db.bun.ts",
      "node": "./src/storage/db.node.ts",
      "default": "./src/storage/db.bun.ts"
    }
  },
  "devDependencies": {
    "@babel/core": "7.28.4",
    "@effect/language-service": "0.79.0",
    "@octokit/webhooks-types": "7.6.1",
    "@opencode-ai/script": "workspace:*",
    "@parcel/watcher-darwin-arm64": "2.5.1",
    "@parcel/watcher-darwin-x64": "2.5.1",
    "@parcel/watcher-linux-arm64-glibc": "2.5.1",
    "@parcel/watcher-linux-arm64-musl": "2.5.1",
    "@parcel/watcher-linux-x64-glibc": "2.5.1",
    "@parcel/watcher-linux-x64-musl": "2.5.1",
    "@parcel/watcher-win32-arm64": "2.5.1",
    "@parcel/watcher-win32-x64": "2.5.1",
    "@standard-schema/spec": "1.0.0",
    "@tsconfig/bun": "catalog:",
    "@types/babel__core": "7.20.5",
    "@types/bun": "catalog:",
    "@types/cross-spawn": "catalog:",
    "@types/mime-types": "3.0.1",
    "@types/npmcli__arborist": "6.3.3",
    "@types/semver": "^7.5.8",
    "@types/turndown": "5.0.5",
    "@types/which": "3.0.4",
    "@types/yargs": "17.0.33",
    "@typescript/native-preview": "catalog:",
    "drizzle-kit": "catalog:",
    "drizzle-orm": "catalog:",
    "typescript": "catalog:",
    "vscode-languageserver-types": "3.17.5",
    "why-is-node-running": "3.2.2",
    "zod-to-json-schema": "3.24.5"
  },
  "dependencies": {
    "@actions/core": "1.11.1",
    "@actions/github": "6.0.1",
    "@agentclientprotocol/sdk": "0.16.1",
    "@ai-sdk/amazon-bedrock": "4.0.83",
    "@ai-sdk/anthropic": "3.0.64",
    "@ai-sdk/azure": "3.0.49",
    "@ai-sdk/cerebras": "2.0.41",
    "@ai-sdk/cohere": "3.0.27",
    "@ai-sdk/deepinfra": "2.0.41",
    "@ai-sdk/gateway": "3.0.80",
    "@ai-sdk/google": "3.0.53",
    "@ai-sdk/google-vertex": "4.0.95",
    "@ai-sdk/groq": "3.0.31",
    "@ai-sdk/mistral": "3.0.27",
    "@ai-sdk/openai": "3.0.48",
    "@ai-sdk/openai-compatible": "2.0.37",
    "@ai-sdk/perplexity": "3.0.26",
    "@ai-sdk/provider": "3.0.8",
    "@ai-sdk/provider-utils": "4.0.21",
    "@ai-sdk/togetherai": "2.0.41",
    "@ai-sdk/vercel": "2.0.39",
    "@ai-sdk/xai": "3.0.75",
    "@aws-sdk/credential-providers": "3.993.0",
    "@clack/prompts": "1.0.0-alpha.1",
    "@effect/platform-node": "catalog:",
    "@hono/standard-validator": "0.1.5",
    "@hono/zod-validator": "catalog:",
    "@modelcontextprotocol/sdk": "1.27.1",
    "@npmcli/arborist": "9.4.0",
    "@octokit/graphql": "9.0.2",
    "@octokit/rest": "catalog:",
    "@openauthjs/openauth": "catalog:",
    "@opencode-ai/plugin": "workspace:*",
    "@opencode-ai/script": "workspace:*",
    "@opencode-ai/sdk": "workspace:*",
    "@opencode-ai/util": "workspace:*",
    "@openrouter/ai-sdk-provider": "2.3.3",
    "@opentui/core": "0.1.96",
    "@opentui/solid": "0.1.96",
    "@parcel/watcher": "2.5.1",
    "@pierre/diffs": "catalog:",
    "@solid-primitives/event-bus": "1.1.2",
    "@solid-primitives/scheduled": "1.5.2",
    "@standard-schema/spec": "1.0.0",
    "@zip.js/zip.js": "2.7.62",
    "ai": "catalog:",
    "ai-gateway-provider": "3.1.2",
    "bonjour-service": "1.3.0",
    "bun-pty": "0.4.8",
    "chokidar": "4.0.3",
    "clipboardy": "4.0.0",
    "cross-spawn": "catalog:",
    "decimal.js": "10.5.0",
    "diff": "catalog:",
    "drizzle-orm": "catalog:",
    "effect": "catalog:",
    "fuzzysort": "3.1.0",
    "gitlab-ai-provider": "6.0.0",
    "glob": "13.0.5",
    "google-auth-library": "10.5.0",
    "gray-matter": "4.0.3",
    "hono": "catalog:",
    "hono-openapi": "catalog:",
    "ignore": "7.0.5",
    "jsonc-parser": "3.3.1",
    "mime-types": "3.0.2",
    "minimatch": "10.0.3",
    "open": "10.1.2",
    "opencode-gitlab-auth": "2.0.1",
    "opencode-poe-auth": "0.0.1",
    "opentui-spinner": "0.0.6",
    "partial-json": "0.1.7",
    "remeda": "catalog:",
    "semver": "^7.6.3",
    "solid-js": "catalog:",
    "strip-ansi": "7.1.2",
    "tree-sitter-bash": "0.25.0",
    "tree-sitter-powershell": "0.25.10",
    "turndown": "7.2.0",
    "ulid": "catalog:",
    "venice-ai-sdk-provider": "2.0.1",
    "vscode-jsonrpc": "8.2.1",
    "web-tree-sitter": "0.25.10",
    "which": "6.0.1",
    "xdg-basedir": "5.1.0",
    "yargs": "18.0.0",
    "zod": "catalog:",
    "zod-to-json-schema": "3.24.5"
  },
  "overrides": {
    "drizzle-orm": "catalog:"
  }
}

```

### File: packages\opencode\README.md
```md
# js

To install dependencies:

```bash
bun install
```

To run:

```bash
bun run index.ts
```

This project was created using `bun init` in bun v1.2.12. [Bun](https://bun.sh) is a fast all-in-one JavaScript runtime.

```

### File: packages\plugin\package.json
```json
{
  "$schema": "https://json.schemastore.org/package.json",
  "name": "@opencode-ai/plugin",
  "version": "1.3.13",
  "type": "module",
  "license": "MIT",
  "scripts": {
    "typecheck": "tsgo --noEmit",
    "build": "tsc"
  },
  "exports": {
    ".": "./src/index.ts",
    "./tool": "./src/tool.ts",
    "./tui": "./src/tui.ts"
  },
  "files": [
    "dist"
  ],
  "dependencies": {
    "@opencode-ai/sdk": "workspace:*",
    "zod": "catalog:"
  },
  "peerDependencies": {
    "@opentui/core": ">=0.1.96",
    "@opentui/solid": ">=0.1.96"
  },
  "peerDependenciesMeta": {
    "@opentui/core": {
      "optional": true
    },
    "@opentui/solid": {
      "optional": true
    }
  },
  "devDependencies": {
    "@opentui/core": "0.1.96",
    "@opentui/solid": "0.1.96",
    "@tsconfig/node22": "catalog:",
    "@types/node": "catalog:",
    "typescript": "catalog:",
    "@typescript/native-preview": "catalog:"
  }
}

```

### File: packages\script\package.json
```json
{
  "$schema": "https://json.schemastore.org/package",
  "name": "@opencode-ai/script",
  "license": "MIT",
  "dependencies": {
    "semver": "^7.6.3"
  },
  "devDependencies": {
    "@types/bun": "catalog:",
    "@types/semver": "^7.5.8"
  },
  "exports": {
    ".": "./src/index.ts"
  }
}

```

### File: packages\slack\package.json
```json
{
  "name": "@opencode-ai/slack",
  "version": "1.3.13",
  "type": "module",
  "license": "MIT",
  "scripts": {
    "dev": "bun run src/index.ts",
    "typecheck": "tsgo --noEmit"
  },
  "dependencies": {
    "@opencode-ai/sdk": "workspace:*",
    "@slack/bolt": "^3.17.1"
  },
  "devDependencies": {
    "@types/node": "catalog:",
    "typescript": "catalog:",
    "@typescript/native-preview": "catalog:"
  }
}

```

### File: packages\slack\README.md
```md
# @opencode-ai/slack

Slack bot integration for opencode that creates threaded conversations.

## Setup

1. Create a Slack app at https://api.slack.com/apps
2. Enable Socket Mode
3. Add the following OAuth scopes:
   - `chat:write`
   - `app_mentions:read`
   - `channels:history`
   - `groups:history`
4. Install the app to your workspace
5. Set environment variables in `.env`:
   - `SLACK_BOT_TOKEN` - Bot User OAuth Token
   - `SLACK_SIGNING_SECRET` - Signing Secret from Basic Information
   - `SLACK_APP_TOKEN` - App-Level Token from Basic Information

## Usage

```bash
# Edit .env with your Slack app credentials
bun dev
```

The bot will respond to messages in channels where it's added, creating separate opencode sessions for each thread.

```

### File: packages\ui\package.json
```json
{
  "name": "@opencode-ai/ui",
  "version": "1.3.13",
  "type": "module",
  "license": "MIT",
  "exports": {
    "./package.json": "./package.json",
    "./*": "./src/components/*.tsx",
    "./i18n/*": "./src/i18n/*.ts",
    "./pierre": "./src/pierre/index.ts",
    "./pierre/*": "./src/pierre/*.ts",
    "./hooks": "./src/hooks/index.ts",
    "./context": "./src/context/index.ts",
    "./context/*": "./src/context/*.tsx",
    "./styles": "./src/styles/index.css",
    "./styles/tailwind": "./src/styles/tailwind/index.css",
    "./theme": "./src/theme/index.ts",
    "./theme/*": "./src/theme/*.ts",
    "./theme/context": "./src/theme/context.tsx",
    "./icons/provider": "./src/components/provider-icons/types.ts",
    "./icons/file-type": "./src/components/file-icons/types.ts",
    "./icons/app": "./src/components/app-icons/types.ts",
    "./fonts/*": "./src/assets/fonts/*",
    "./audio/*": "./src/assets/audio/*"
  },
  "scripts": {
    "typecheck": "tsgo --noEmit",
    "dev": "vite",
    "generate:tailwind": "bun run script/tailwind.ts"
  },
  "devDependencies": {
    "@tailwindcss/vite": "catalog:",
    "@tsconfig/node22": "catalog:",
    "@types/bun": "catalog:",
    "@types/katex": "0.16.7",
    "@types/luxon": "catalog:",
    "@typescript/native-preview": "catalog:",
    "tailwindcss": "catalog:",
    "typescript": "catalog:",
    "vite": "catalog:",
    "vite-plugin-icons-spritesheet": "3.0.1",
    "vite-plugin-solid": "catalog:"
  },
  "dependencies": {
    "@kobalte/core": "catalog:",
    "@opencode-ai/sdk": "workspace:*",
    "@opencode-ai/util": "workspace:*",
    "@pierre/diffs": "catalog:",
    "@shikijs/transformers": "3.9.2",
    "@solid-primitives/bounds": "0.1.3",
    "@solid-primitives/event-listener": "2.4.5",
    "@solid-primitives/media": "2.3.3",
    "@solid-primitives/resize-observer": "2.1.3",
    "@solidjs/meta": "catalog:",
    "@solidjs/router": "catalog:",
    "dompurify": "3.3.1",
    "fuzzysort": "catalog:",
    "katex": "0.16.27",
    "luxon": "catalog:",
    "marked": "catalog:",
    "marked-katex-extension": "5.1.6",
    "marked-shiki": "catalog:",
    "morphdom": "2.7.8",
    "motion": "12.34.5",
    "motion-dom": "12.34.3",
    "motion-utils": "12.29.2",
    "remeda": "catalog:",
    "remend": "catalog:",
    "shiki": "catalog:",
    "solid-js": "catalog:",
    "solid-list": "catalog:",
    "strip-ansi": "7.1.2",
    "virtua": "catalog:"
  }
}

```

### File: packages\util\package.json
```json
{
  "name": "@opencode-ai/util",
  "version": "1.3.13",
  "private": true,
  "type": "module",
  "license": "MIT",
  "exports": {
    "./*": "./src/*.ts"
  },
  "scripts": {
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "zod": "catalog:"
  },
  "devDependencies": {
    "typescript": "catalog:",
    "@types/bun": "catalog:"
  }
}

```

### File: packages\web\package.json
```json
{
  "name": "@opencode-ai/web",
  "type": "module",
  "license": "MIT",
  "version": "1.3.13",
  "scripts": {
    "dev": "astro dev",
    "dev:remote": "VITE_API_URL=https://api.opencode.ai astro dev",
    "start": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  },
  "dependencies": {
    "@astrojs/cloudflare": "12.6.3",
    "@astrojs/markdown-remark": "6.3.1",
    "@astrojs/solid-js": "5.1.0",
    "@astrojs/starlight": "0.34.3",
    "@fontsource/ibm-plex-mono": "5.2.5",
    "@shikijs/transformers": "3.20.0",
    "@solid-primitives/resize-observer": "2.1.5",
    "@types/luxon": "catalog:",
    "ai": "catalog:",
    "astro": "5.7.13",
    "diff": "catalog:",
    "js-base64": "3.7.7",
    "lang-map": "0.4.0",
    "luxon": "catalog:",
    "marked": "catalog:",
    "marked-shiki": "catalog:",
    "rehype-autolink-headings": "7.1.0",
    "remeda": "catalog:",
    "shiki": "catalog:",
    "solid-js": "catalog:",
    "toolbeam-docs-theme": "0.4.8",
    "vscode-languageserver-types": "3.17.5"
  },
  "devDependencies": {
    "opencode": "workspace:*",
    "@types/node": "catalog:",
    "@astrojs/check": "0.9.6",
    "typescript": "catalog:"
  }
}

```

### File: packages\web\README.md
```md
# Starlight Starter Kit: Basics

[![Built with Starlight](https://astro.badg.es/v2/built-with-starlight/tiny.svg)](https://starlight.astro.build)

```
npm create astro@latest -- --template starlight
```

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/withastro/starlight/tree/main/examples/basics)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io/p/sandbox/github/withastro/starlight/tree/main/examples/basics)
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/withastro/starlight&create_from_path=examples/basics)
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fwithastro%2Fstarlight%2Ftree%2Fmain%2Fexamples%2Fbasics&project-name=my-starlight-docs&repository-name=my-starlight-docs)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## 🚀 Project Structure

Inside of your Astro + Starlight project, you'll see the following folders and files:

```
.
├── public/
├── src/
│   ├── assets/
│   ├── content/
│   │   ├── docs/
│   └── content.config.ts
├── astro.config.mjs
├── package.json
└── tsconfig.json
```

Starlight looks for `.md` or `.mdx` files in the `src/content/docs/` directory. Each file is exposed as a route based on its file name.

Images can be added to `src/assets/` and embedded in Markdown with a relative link.

Static assets, like favicons, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Check out [Starlight’s docs](https://starlight.astro.build/), read [the Astro documentation](https://docs.astro.build), or jump into the [Astro Discord server](https://astro.build/chat).

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

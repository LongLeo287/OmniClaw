---
id: repo-fetched-chrome-devtools-mcp-043018
type: knowledge
owner: OA
registered_at: 2026-04-05T04:13:01.216942
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_chrome-devtools-mcp_043018

## Assimilation Report
Auto-cloned repository: FETCHED_chrome-devtools-mcp_043018

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "chrome-devtools-mcp",
  "version": "0.21.0",
  "description": "MCP server for Chrome DevTools",
  "type": "module",
  "bin": {
    "chrome-devtools-mcp": "./build/src/bin/chrome-devtools-mcp.js",
    "chrome-devtools": "./build/src/bin/chrome-devtools.js"
  },
  "main": "./build/src/index.js",
  "scripts": {
    "cli:generate": "node --experimental-strip-types scripts/generate-cli.ts",
    "clean": "node -e \"require('fs').rmSync('build', {recursive: true, force: true})\"",
    "bundle": "npm run clean && npm run build && rollup -c rollup.config.mjs && node -e \"require('fs').rmSync('build/node_modules', {recursive: true, force: true})\" && node --experimental-strip-types scripts/append-lighthouse-notices.ts",
    "build": "tsc && node --experimental-strip-types --no-warnings=ExperimentalWarning scripts/post-build.ts",
    "typecheck": "tsc --noEmit",
    "format": "eslint --cache --fix . && prettier --write --cache .",
    "check-format": "eslint --cache . && prettier --check --cache .;",
    "gen": "npm run build && npm run docs:generate && npm run cli:generate && npm run update-tool-call-metrics && npm run format",
    "docs:generate": "node --experimental-strip-types scripts/generate-docs.ts",
    "start": "npm run build && node build/src/index.js",
    "start-debug": "DEBUG=mcp:* DEBUG_COLORS=false npm run build && node build/src/index.js",
    "test": "npm run build && node scripts/test.mjs",
    "test:no-build": "node scripts/test.mjs",
    "test:only": "npm run build && node scripts/test.mjs --test-only",
    "test:update-snapshots": "npm run build && node scripts/test.mjs --test-update-snapshots",
    "prepare": "node --experimental-strip-types scripts/prepare.ts",
    "verify-server-json-version": "node --experimental-strip-types scripts/verify-server-json-version.ts",
    "update-lighthouse": "node --experimental-strip-types scripts/update-lighthouse.ts",
    "update-tool-call-metrics": "node --experimental-strip-types scripts/update_tool_call_metrics.ts",
    "verify-npm-package": "node scripts/verify-npm-package.mjs",
    "eval": "npm run build && node --experimental-strip-types scripts/eval_gemini.ts",
    "count-tokens": "node --experimental-strip-types scripts/count_tokens.ts"
  },
  "files": [
    "build/src",
    "LICENSE",
    "!*.tsbuildinfo"
  ],
  "repository": "ChromeDevTools/chrome-devtools-mcp",
  "author": "Google LLC",
  "license": "Apache-2.0",
  "bugs": {
    "url": "https://github.com/ChromeDevTools/chrome-devtools-mcp/issues"
  },
  "homepage": "https://github.com/ChromeDevTools/chrome-devtools-mcp#readme",
  "mcpName": "io.github.ChromeDevTools/chrome-devtools-mcp",
  "devDependencies": {
    "@eslint/js": "^9.35.0",
    "@google/genai": "^1.37.0",
    "@modelcontextprotocol/sdk": "1.29.0",
    "@rollup/plugin-commonjs": "^29.0.0",
    "@rollup/plugin-json": "^6.1.0",
    "@rollup/plugin-node-resolve": "^16.0.3",
    "@stylistic/eslint-plugin": "^5.4.0",
    "@types/debug": "^4.1.12",
    "@types/filesystem": "^0.0.36",
    "@types/node": "^25.0.0",
    "@types/sinon": "^21.0.0",
    "@types/yargs": "^17.0.33",
    "@typescript-eslint/eslint-plugin": "^8.43.0",
    "@typescript-eslint/parser": "^8.43.0",
    "chrome-devtools-frontend": "1.0.1608453",
    "core-js": "3.49.0",
    "debug": "4.4.3",
    "eslint": "^9.35.0",
    "eslint-import-resolver-typescript": "^4.4.4",
    "eslint-plugin-import": "^2.32.0",
    "globals": "^17.0.0",
    "lighthouse": "13.0.3",
    "prettier": "^3.6.2",
    "puppeteer": "24.40.0",
    "rollup": "4.60.1",
    "rollup-plugin-cleanup": "^3.2.1",
    "rollup-plugin-license": "^3.6.0",
    "sinon": "^21.0.0",
    "tiktoken": "^1.0.22",
    "typescript": "^6.0.2",
    "typescript-eslint": "^8.43.0",
    "yargs": "18.0.0"
  },
  "engines": {
    "node": "^20.19.0 || ^22.12.0 || >=23"
  }
}

```

### File: README.md
```md
# Chrome DevTools MCP

[![npm chrome-devtools-mcp package](https://img.shields.io/npm/v/chrome-devtools-mcp.svg)](https://npmjs.org/package/chrome-devtools-mcp)

`chrome-devtools-mcp` lets your coding agent (such as Gemini, Claude, Cursor or Copilot)
control and inspect a live Chrome browser. It acts as a Model-Context-Protocol
(MCP) server, giving your AI coding assistant access to the full power of
Chrome DevTools for reliable automation, in-depth debugging, and performance analysis.

## [Tool reference](./docs/tool-reference.md) | [Changelog](./CHANGELOG.md) | [Contributing](./CONTRIBUTING.md) | [Troubleshooting](./docs/troubleshooting.md) | [Design Principles](./docs/design-principles.md)

## Key features

- **Get performance insights**: Uses [Chrome
  DevTools](https://github.com/ChromeDevTools/devtools-frontend) to record
  traces and extract actionable performance insights.
- **Advanced browser debugging**: Analyze network requests, take screenshots and
  check browser console messages (with source-mapped stack traces).
- **Reliable automation**. Uses
  [puppeteer](https://github.com/puppeteer/puppeteer) to automate actions in
  Chrome and automatically wait for action results.

## Disclaimers

`chrome-devtools-mcp` exposes content of the browser instance to the MCP clients
allowing them to inspect, debug, and modify any data in the browser or DevTools.
Avoid sharing sensitive or personal information that you don't want to share with
MCP clients.

`chrome-devtools-mcp` officially supports Google Chrome and [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/) only.
Other Chromium-based browsers may work, but this is not guaranteed, and you may encounter unexpected behavior. Use at your own discretion.
We are committed to providing fixes and support for the latest version of [Extended Stable Chrome](https://chromiumdash.appspot.com/schedule).

Performance tools may send trace URLs to the Google CrUX API to fetch real-user
experience data. This helps provide a holistic performance picture by
presenting field data alongside lab data. This data is collected by the [Chrome
User Experience Report (CrUX)](https://developer.chrome.com/docs/crux). To disable
this, run with the `--no-performance-crux` flag.

## **Usage statistics**

Google collects usage statistics (such as tool invocation success rates, latency, and environment information) to improve the reliability and performance of Chrome DevTools MCP.

Data collection is **enabled by default**. You can opt-out by passing the `--no-usage-statistics` flag when starting the server:

```json
"args": ["-y", "chrome-devtools-mcp@latest", "--no-usage-statistics"]
```

Google handles this data in accordance with the [Google Privacy Policy](https://policies.google.com/privacy).

Google's collection of usage statistics for Chrome DevTools MCP is independent from the Chrome browser's usage statistics. Opting out of Chrome metrics does not automatically opt you out of this tool, and vice-versa.

Collection is disabled if `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS` or `CI` env variables are set.

## Update checks

By default, the server periodically checks the npm registry for updates and logs a notification when a newer version is available.
You can disable these update checks by setting the `CHROME_DEVTOOLS_MCP_NO_UPDATE_CHECKS` environment variable.

## Requirements

- [Node.js](https://nodejs.org/) v20.19 or a newer [latest maintenance LTS](https://github.com/nodejs/Release#release-schedule) version.
- [Chrome](https://www.google.com/chrome/) current stable version or newer.
- [npm](https://www.npmjs.com/)

## Getting started

Add the following config to your MCP client:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

> [!NOTE]
> Using `chrome-devtools-mcp@latest` ensures that your MCP client will always use the latest version of the Chrome DevTools MCP server.

If you are interested in doing only basic browser tasks, use the `--slim` mode:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest", "--slim", "--headless"]
    }
  }
}
```

See [Slim tool reference](./docs/slim-tool-reference.md).

### MCP Client configuration

<details>
  <summary>Amp</summary>
  Follow https://ampcode.com/manual#mcp and use the config provided above. You can also install the Chrome DevTools MCP server using the CLI:

```bash
amp mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

</details>

<details>
  <summary>Antigravity</summary>

To use the Chrome DevTools MCP server follow the instructions from <a href="https://antigravity.google/docs/mcp">Antigravity's docs</a> to install a custom MCP server. Add the following config to the MCP servers config:

```bash
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "chrome-devtools-mcp@latest",
        "--browser-url=http://127.0.0.1:9222",
        "-y"
      ]
    }
  }
}
```

This will make the Chrome DevTools MCP server automatically connect to the browser that Antigravity is using. If you are not using port 9222, make sure to adjust accordingly.

Chrome DevTools MCP will not start the browser instance automatically using this approach because the Chrome DevTools MCP server connects to Antigravity's built-in browser. If the browser is not already running, you have to start it first by clicking the Chrome icon at the top right corner.

</details>

<details>
  <summary>Claude Code</summary>

**Install via CLI (MCP only)**

Use the Claude Code CLI to add the Chrome DevTools MCP server (<a href="https://code.claude.com/docs/en/mcp">guide</a>):

```bash
claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest
```

**Install as a Plugin (MCP + Skills)**

> [!NOTE]
> If you already had Chrome DevTools MCP installed previously for Claude Code, make sure to remove it first from your installation and configuration files.

To install Chrome DevTools MCP with skills, add the marketplace registry in Claude Code:

```sh
/plugin marketplace add ChromeDevTools/chrome-devtools-mcp
```

Then, install the plugin:

```sh
/plugin install chrome-devtools-mcp
```

Restart Claude Code to have the MCP server and skills load (check with `/skills`).

> [!TIP]
> If the plugin installation fails with a `Failed to clone repository` error (e.g., HTTPS connectivity issues behind a corporate firewall), see the [troubleshooting guide](./docs/troubleshooting.md#claude-code-plugin-installation-fails-with-failed-to-clone-repository) for workarounds, or use the CLI installation method above instead.

</details>

<details>
  <summary>Cline</summary>
  Follow https://docs.cline.bot/mcp/configuring-mcp-servers and use the config provided above.
</details>

<details>
  <summary>Codex</summary>
  Follow the <a href="https://developers.openai.com/codex/mcp/#configure-with-the-cli">configure MCP guide</a>
  using the standard config from above. You can also install the Chrome DevTools MCP server using the Codex CLI:

```bash
codex mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

**On Windows 11**

Configure the Chrome install location and increase the startup timeout by updating `.codex/config.toml` and adding the following `env` and `startup_timeout_ms` parameters:

```
[mcp_servers.chrome-devtools]
command = "cmd"
args = [
    "/c",
    "npx",
    "-y",
    "chrome-devtools-mcp@latest",
]
env = { SystemRoot="C:\\Windows", PROGRAMFILES="C:\\Program Files" }
startup_timeout_ms = 20_000
```

</details>

<details>
  <summary>Command Code</summary>

Use the Command Code CLI to add the Chrome DevTools MCP server (<a href="https://commandcode.ai/docs/mcp">MCP guide</a>):

```bash
cmd mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest
```

</details>

<details>
  <summary>Copilot CLI</summary>

Start Copilot CLI:

```
copilot
```

Start the dialog to add a new MCP server by running:

```
/mcp add
```

Configure the following fields and press `CTRL+S` to save the configuration:

- **Server name:** `chrome-devtools`
- **Server Type:** `[1] Local`
- **Command:** `npx -y chrome-devtools-mcp@latest`

</details>

<details>
  <summary>Copilot / VS Code</summary>

**Install as a Plugin (Recommended)**

The easiest way to get up and running is to install `chrome-devtools-mcp` as an agent plugin.
This bundles the **MCP server** and all **skills** together, so your agent gets both the tools
and the expert guidance it needs to use them effectively.

1.  Open the **Command Palette** (`Cmd+Shift+P` on macOS or `Ctrl+Shift+P` on Windows/Linux).
2.  Search for and run the **Chat: Install Plugin From Source** command.
3.  Paste in our repository URL: `https://github.com/ChromeDevTools/chrome-devtools-mcp`

That's it! Your agent is now supercharged with Chrome DevTools capabilities.

---

**Install as an MCP Server (MCP only)**

**Click the button to install:**

[<img src="https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF" alt="Install in VS Code">](https://vscode.dev/redirect/mcp/install?name=io.github.ChromeDevTools%2Fchrome-devtools-mcp&config=%7B%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22chrome-devtools-mcp%22%5D%2C%22env%22%3A%7B%7D%7D)

[<img src="https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5" alt="Install in VS Code Insiders">](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522io.github.ChromeDevTools%252Fchrome-devtools-mcp%2522%252C%2522config%2522%253A%257B%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522-y%2522%252C%2522chrome-devtools-mcp%2522%255D%252C%2522env%2522%253A%257B%257D%257D%257D)

**Or install manually:**

Follow the VS Code [MCP configuration guide](https://code.visualstudio.com/docs/copilot/chat/mcp-servers#_add-an-mcp-server) using the standard config from above, or use the CLI:

For macOS and Linux:

```bash
code --add-mcp '{"name":"io.github.ChromeDevTools/chrome-devtools-mcp","command":"npx","args":["-y","chrome-devtools-mcp"],"env":{}}'
```

For Windows (PowerShell):

```powershell
code --add-mcp '{"""name""":"""io.github.ChromeDevTools/chrome-devtools-mcp""","""command""":"""npx""","""args""":["""-y""","""chrome-devtools-mcp"""]}'
```

</details>

<details>
  <summary>Cursor</summary>

**Click the button to install:**

[<img src="https://cursor.com/deeplink/mcp-install-dark.svg" alt="Install in Cursor">](https://cursor.com/en/install-mcp?name=chrome-devtools&config=eyJjb21tYW5kIjoibnB4IC15IGNocm9tZS1kZXZ0b29scy1tY3BAbGF0ZXN0In0%3D)

**Or install manually:**

Go to `Cursor Settings` -> `MCP` -> `New MCP Server`. Use the config provided above.

</details>

<details>
  <summary>Factory CLI</summary>
Use the Factory CLI to add the Chrome DevTools MCP server (<a href="https://docs.factory.ai/cli/configuration/mcp">guide</a>):

```bash
droid mcp add chrome-devtools "npx -y chrome-devtools-mcp@latest"
```

</details>

<details>
  <summary>Gemini CLI</summary>
Install the Chrome DevTools MCP server using the Gemini CLI.

**Project wide:**

```bash
# Either MCP only:
gemini mcp add chrome-devtools npx chrome-devtools-mcp@latest
# Or as a Gemini extension (MCP+Skills):
gemini extensions install --auto-update https://github.com/ChromeDevTools/chrome-devtools-mcp
```

**Globally:**

```bash
gemini mcp add -s user chrome-devtools npx chrome-devtools-mcp@latest
```

Alternatively, follow the <a href="https://github.com/google-gemini/gemini-cli/blob/main/docs/tools/mcp-server.md#how-to-set-up-your-mcp-server">MCP guide</a> and use the standard config from above.

</details>

<details>
  <summary>Gemini Code Assist</summary>
  Follow the <a href="https://cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer#configure-mcp-servers">configure MCP guide</a>
  using the standard config from above.
</details>

<details>
  <summary>JetBrains AI Assistant & Junie</summary>

Go to `Settings | Tools | AI Assistant | Model Context Protocol (MCP)` -> `Add`. Use the config provided above.
The same way chrome-devtools-mcp can be configured for JetBrains Junie in `Settings | Tools | Junie | MCP Settings` -> `Add`. Use the config provided above.

</details>

<details>
  <summary>Kiro</summary>

In **Kiro Settings**, go to `Configure MCP` > `Open Workspace or User MCP Config` > Use the configuration snippet provided above.

Or, from the IDE **Activity Bar** > `Kiro` > `MCP Servers` > `Click Open MCP Config`. Use the configuration snippet provided above.

</details>

<details>
  <summary>Katalon Studio</summary>

The Chrome DevTools MCP server can be used with <a href="https://docs.katalon.com/katalon-studio/studioassist/mcp-servers/setting-up-chrome-devtools-mcp-server-for-studioassist">Katalon StudioAssist</a> via an MCP proxy.

**Step 1:** Install the MCP proxy by following the <a href="https://docs.katalon.com/katalon-studio/studioassist/mcp-servers/setting-up-mcp-proxy-for-stdio-mcp-servers">MCP proxy setup guide</a>.

**Step 2:** Start the Chrome DevTools MCP server with the proxy:

```bash
mcp-proxy --transport streamablehttp --port 8080 -- npx -y chrome-devtools-mcp@latest
```

**Note:** You may need to pick another port if 8080 is already in use.

**Step 3:** In Katalon Studio, add the server to StudioAssist with the following settings:

- **Connection URL:** `http://127.0.0.1:8080/mcp`
- **Transport type:** `HTTP`

Once connected, the Chrome DevTools MCP tools will be available in StudioAssist.

</details>

<details>
  <summary>OpenCode</summary>

Add the following configuration to your `opencode.json` file. If you don't have one, create it at `~/.config/opencode/opencode.json` (<a href="https://opencode.ai/docs/mcp-servers">guide</a>):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "chrome-devtools": {
      "type": "local",
      "command": ["npx", "-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

</details>

<details>
  <summary>Qoder</summary>

In **Qoder Settings**, go to `MCP Server` > `+ Add` > Use the configuration snippet provided above.

Alternatively, follow the <a href="https://docs.qoder.com/user-guide/chat/model-context-protocol">MCP guide</a> and use the standard config from above.

</details>

<details>
  <summary>Qoder CLI</summary>

Install the Chrome DevTools MCP server using the Qoder CLI (<a href="https://docs.qoder.com/cli/using-cli#mcp-servers">guide</a>):

**Project wide:**

```bash
qodercli mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
```

**Globally:**

```bash
qodercli mcp add -s user chrome-devtools -- npx chrome-devtools-mcp@latest
```

</details>

<details>
  <summary>Visual Studio</summary>

**Click the button to install:**

[<img src="https://img.shields.io/badge/Visual_Studio-Install-C16FDE?logo=visualstudio&logoC
... [TRUNCATED]
```

### File: .mcp.json
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest"]
    }
  }
}

```

### File: .release-please-manifest.json
```json
{
  ".": "0.21.0"
}

```

### File: CHANGELOG.md
```md
# Changelog

## [0.21.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/compare/chrome-devtools-mcp-v0.20.3...chrome-devtools-mcp-v0.21.0) (2026-04-01)


### 🎉 Features

* add a skill for detecting memory leaks using take_memory_snapshot tool ([#1162](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1162)) ([d19a235](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/d19a2350f975ec2fbf8ee61b35163a48c0146c32))


### 🛠️ Fixes

* **cli:** avoid defaulting to isolated when userDataDir is provided ([#1258](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1258)) ([73e1e24](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/73e1e24b26f9e42a83116b586e34d47276a6a2fa))
* list_pages should work after selected page is closed ([#1145](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1145)) ([2664455](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/26644553028d8404fd65a005ea9c19a278671f4d))
* mark lighthouse and memory as non-read-only ([#1769](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1769)) ([bec9dae](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/bec9dae2d26b728feedcd660189f386e6228f3ae))
* **telemetry:** record client name ([9a47b65](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/9a47b657d7b17b9bc64508530c93d55e8033e2a6))
* versioning for Claude Code plugin ([#1233](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1233)) ([966b86f](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/966b86f3aaa9f87c2599b954c4e7f990c2a697ea))
* wrap .mcp.json config in mcpServers key ([#1246](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1246)) ([c7948cf](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/c7948cf0621d80b080220d4cfd36b62bef2790b9))


### 📄 Documentation

* Command Code CLI instructions for MCP server ([0a7c0a7](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/0a7c0a74b471935a3e2f5ca0fd93556e8e5165ec))
* provide disclaimer about supported browsers ([#1237](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1237)) ([8676b72](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/8676b7216c66dfd323c2f6c272544a75dbab4dba))


### 🏗️ Refactor

* set process titles for easier debugging ([#1770](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1770)) ([0fe3896](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/0fe3896d85c74ce8b2dc189fe8a310727f795344))

## [0.20.3](https://github.com/ChromeDevTools/chrome-devtools-mcp/compare/chrome-devtools-mcp-v0.20.2...chrome-devtools-mcp-v0.20.3) (2026-03-20)


### 🛠️ Fixes

* mark categoryExtensions flag mutually exclusive with autoConnect ([#1202](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1202)) ([8c2a7fc](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/8c2a7fc21ead6091567e85608f7916c001ccc7db)), closes [#1072](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1072)


### ⚡ Performance

* **memory:** release old navigation request in NetworkCollector ([#1200](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1200)) ([1e6456c](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/1e6456ce222a8f392341a530b2340336c7a1ab02))
* use CDP to find open DevTools pages (reland) ([#1210](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1210)) ([53483bc](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/53483bc637566658754d781d88f4353ad47f44a7))

## [0.20.2](https://github.com/ChromeDevTools/chrome-devtools-mcp/compare/chrome-devtools-mcp-v0.20.1...chrome-devtools-mcp-v0.20.2) (2026-03-18)


### 📄 Documentation

* add troubleshooting for Claude Code plugin HTTPS clone failures ([#1195](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1195)) ([d082ca4](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/d082ca4ecd35a023d09f9c1ff949d5fb0c3fb069))

## [0.20.1](https://github.com/ChromeDevTools/chrome-devtools-mcp/compare/chrome-devtools-mcp-v0.20.0...chrome-devtools-mcp-v0.20.1) (2026-03-16)


### 🛠️ Fixes

* update VS Code manual installation powershell command ([#1151](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1151)) ([6c64a5b](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/6c64a5b543714796b25a12dc6f2be7a1e683e8bd))


### ⚡ Performance

* use CDP to find open DevTools pages. ([#1150](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1150)) ([94de19c](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/94de19cdcdae9e31d0962b273ce352dc248eb5a8))

## [0.20.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/compare/chrome-devtools-mcp-v0.19.0...chrome-devtools-mcp-v0.20.0) (2026-03-11)


### 🎉 Features

* experimental `chrome-devtools` CLI ([#1100](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1100)) ([1ac574e](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/1ac574e7154948e86e414e5149fb975a190d5bb0))


### 📄 Documentation

* fix typo ([#1155](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1155)) ([b59cabc](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/b59cabcc1d59802ffd7d9667040188e46192357d))
* fix typos and improve phrasing ([#1130](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1130)) ([70d4f36](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/70d4f365dc619a5743e697c30800f7065bc6227d))
* revise contribution process and add release process ([#1134](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1134)) ([d7d26a1](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/d7d26a103b840e2feb7cb9af6a242edda94f1ddf))
* **troubleshooting:** add symptom for missing tools due to read-only mode ([#1148](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1148)) ([57e7d51](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/57e7d51e8ca1e2ee325a9e7a9c64c033acbe6d6a))
* Update troubleshooting for MCP server connection errors ([#1017](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1017)) ([00f9c31](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/00f9c3108ab9caefca57998439052c728298920b))


### 🏗️ Refactor

* move main files ([#1120](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1120)) ([c2d8009](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/c2d8009ff75f76bce1ec4cf79c2467b50d81725e))

## [0.19.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/compare/chrome-devtools-mcp-v0.18.1...chrome-devtools-mcp-v0.19.0) (2026-03-05)


### 🎉 Features

* add pageId routing for parallel multi-agent workflows ([#1022](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1022)) ([caf601a](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/caf601a32832bb87cfac801a6bbeacb87508412f)), closes [#1019](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1019)
* Add skill which helps with onboarding of the mcp server ([#1083](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1083)) ([7273f16](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/7273f16ec08f6d5b46a2693b0ad4d559086ded89))
* integrate Lighthouse audits ([#831](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/831)) ([dfdac26](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/dfdac2648e560d756a8711ad3bb1fa470be8e7c9))


### 🛠️ Fixes

* improve error messages around --auto-connect ([#1075](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1075)) ([bcb852d](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/bcb852dd2e440b0005f4a9ad270a1a7998767907))
* improve tool descriptions ([#965](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/965)) ([bdbbc84](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/bdbbc84c125bdd48f4be48aa476bec0323de611c))
* repair broken markdown and extract snippets in a11y-debugging skill ([#1096](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1096)) ([adac7c5](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/adac7c537ee304f324c5e7284fb363396d1773f5))
* simplify emulation and script tools ([#1073](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1073)) ([e51ba47](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/e51ba4720338951e621585b77efc6a0e07678d99))
* simplify focus state management ([#1063](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1063)) ([f763da2](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/f763da24a10e27605c0a5069853ce7c92974eec2))
* tweak lighthouse description ([#1112](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1112)) ([5538180](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/55381804ae7ffa8a1e5933b621a9b8390b3000ff))


### 📄 Documentation

* Adapt a11y skill to utilize Lighthouse ([#1054](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1054)) ([21634e6](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/21634e660c346e469ae62116b1824538f51567dd))
* add feature release checklist to CONTRIBUTING.md ([#1118](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1118)) ([0378457](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/03784577ffb6e238bcb2d637bff9ad759723ea7b))
* fix typo in README regarding slim mode ([#1093](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1093)) ([92f2c7b](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/92f2c7b48b56a6b1d6ac7c9e2f2e92beb26bcf62))


### 🏗️ Refactor

* clean up more of the context getters ([#1062](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1062)) ([9628dab](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/9628dabcb4d39f0b94d152a0fc419e049246a29d))
* consistently use McpPage in tools ([#1057](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1057)) ([302e5a0](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/302e5a04191ba0558e3c79f1486d01d5eb0f6896))
* improve type safety for page scoped tools ([#1051](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1051)) ([5f694c6](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/5f694c60ffd21f8b022554c92b2ad4cbdb457375))
* make cdp resolvers use McpPage ([#1060](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1060)) ([d6c06c5](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/d6c06c56a7b8e4968318adc9fc7c820ace9f5bd9))
* move dialog handling to McpPage ([#1059](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1059)) ([40c241b](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/40c241bbfc80d6282953ab325b30a597d3d85ade))
* move server to a separate file ([#1043](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1043)) ([a8bf3e5](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/a8bf3e585682c3126dfd378e9f98b5dc7ab6045d))
* remove page passing via context ([#1061](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1061)) ([4cb5a17](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/4cb5a17b57f57d8a367cd423c960ba122b9952e3))
* set defaults to performance trace tool ([#1090](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1090)) ([dfa9b79](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/dfa9b79a4ecc9e67f5b043f2dd97f6889d1fee0b))
* simplify the response texts ([#1095](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1095)) ([cb0079e](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/cb0079efbbd41874f6913772fe3f2a037e9f5f8f))
* type-cast as internal CdpPage interface ([#1064](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1064)) ([2d5e4fa](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/2d5e4fa3579650a384ff21c88c2e6b9cda031e1a))

## [0.18.1](https://github.com/ChromeDevTools/chrome-devtools-mcp/compare/chrome-devtools-mcp-v0.18.0...chrome-devtools-mcp-v0.18.1) (2026-02-25)


### 🛠️ Fixes

* remove endsWith for filePath in memory tools ([#1041](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1041)) ([d0622d5](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/d0622d52d46ac72a28bc22f93a337fb5007214c7))

## [0.18.0](https://github.com/ChromeDevTools/chrome-devtools-mcp/compare/chrome-devtools-mcp-v0.17.3...chrome-devtools-mcp-v0.18.0) (2026-02-24)


### 🎉 Features

* `--slim` mode for maximum token savings ([#958](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/958)) ([c402b43](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/c402b43697d834994c4fc141305189082da14bee))
* add a new skill for accessibility debugging and auditing with Chrome DevTools MCP. ([#1002](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1002)) ([b0c6d04](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/b0c6d042e4d68763acf989edc8097ce07e85dc7a))
* add experimental screencast recording tools ([#941](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/941)) ([33446d4](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/33446d457e4386fadcfe4ddf6c7a43b2e9098c9a))
* add skill to debug and optimize LCP ([#993](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/993)) ([2cd9b95](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/2cd9b95346226aa52cce18f6ab889a2ae194806c))
* add storage-isolated browser contexts ([#991](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/991)) ([59f6477](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/59f6477a70eb07585e9a510089f1dfc840a012fd))
* add take_memory_snapshot tool ([#1023](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1023)) ([7ffdc5e](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/7ffdc5ee4d9df9f62f03354fa758fb4d022c3b08))
* support any-match text arrays in wait_for ([#1011](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1011)) ([496ab1b](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/496ab1b45f7a283a1432643777e0795a17f33667))
* support type_text ([#1026](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1026)) ([b5d01b5](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/b5d01b5fe65fa20f9b76555b86a749960a5d1738))


### 🛠️ Fixes

* detect X server display on Linux ([#1027](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1027)) ([1746ed9](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/1746ed9ee11c212f78dcbb00af99a0400595e778))


### ♻️ Chores

* cleanup string and structured console formatters ([#1005](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1005)) ([0d78685](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/0d78685a5b37dc68bb11a1088ff8816ecff3bb82))
* extract version in a seprate file ([#1032](https://github.com/ChromeDevTools/chrome-devtools-mcp/issues/1032)) ([0106865](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/0106865aad
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# How to contribute

We'd love to accept your patches and contributions to this project.

## Before you begin

### Sign our Contributor License Agreement

Contributions to this project must be accompanied by a
[Contributor License Agreement](https://cla.developers.google.com/about) (CLA).
You (or your employer) retain the copyright to your contribution; this simply
gives us permission to use and redistribute your contributions as part of the
project.

If you or your current employer have already signed the Google CLA (even if it
was for a different project), you probably don't need to do it again.

Visit <https://cla.developers.google.com/> to see your current agreements or to
sign a new one.

### Review our community guidelines

This project follows
[Google's Open Source Community Guidelines](https://opensource.google/conduct/).

## Development process

### Code reviews

All submissions, including submissions by project members, require review. We
use GitHub pull requests for this purpose. Consult
[GitHub Help](https://help.github.com/articles/about-pull-requests/) for more
information on using pull requests.

### Conventional commits

Please follow [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
for PR and commit titles.

### Feature release checklist

Use `chore:` for commits containing incomplete features that are not available
to users yet. Once the feature is ready to be released, create a PR with a
`feat:` prefix that enables the feature. The following criteria need to be
completed:

- Documentation for the feature is up to date. For example, README.md and tools
  reference are updated.
- The feature can be used with Chrome stable or version restrictions are
  documented otherwise.
- Corresponding skills are updated or new skills are added if needed.
- The feature fulfills the use case by its own or in conjunction with existing
  features (we want to avoid features that offer some tools but cannot be used
  successfully to debug things).

### Release process

Releasing `chrome-devtools-mcp` is automated by GitHub Actions. To release a new
version, [search for a PR titled `chore(main): release chrome-devtools-mcp`](https://github.com/ChromeDevTools/chrome-devtools-mcp/pulls?q=is%3Apr+is%3Aopen+%22chore%28main%29%3A+release+chrome-devtools-mcp%22)
and review, test, and land it. The release PR is automatically opened if there
are any changes on the main branch that show up in the changelog.

## Installation

Check that you are using node version specified in .nvmrc, then run following commands:

```sh
git clone https://github.com/ChromeDevTools/chrome-devtools-mcp.git
cd chrome-devtools-mcp
npm ci
npm run build
```

### Testing with @modelcontextprotocol/inspector

```sh
npx @modelcontextprotocol/inspector node /build/src/bin/chrome-devtools-mcp.js
```

### Testing with an MCP client

Add the MCP server to your client's config.

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "node",
      "args": ["/path-to/build/src/bin/chrome-devtools-mcp.js"]
    }
  }
}
```

#### Using with VS Code SSH

When running the `@modelcontextprotocol/inspector` it spawns 2 services - one on port `6274` and one on `6277`.
Usually VS Code automatically detects and forwards `6274` but fails to detect `6277` so you need to manually forward it.

### Debugging

To write debug logs to `log.txt` in the working directory, run with the following commands:

```sh
npx @modelcontextprotocol/inspector node /build/src/bin/chrome-devtools-mcp.js --log-file=/your/desired/path/log.txt
```

You can use the `DEBUG` environment variable as usual to control categories that are logged.

### Updating documentation

When adding a new tool or updating a tool name or description, make sure to run `npm run gen` to generate the tool reference documentation.

### Contributing to Evals

We use Gemini to evaluate the MCP server tools in `scripts/eval_scenarios`.
Each scenario is a TypeScript file that exports a `scenario` object implementing `TestScenario`.

- **prompt**: The prompt to send to the model.
- **maxTurns**: Maximum number of conversation turns.
- **expectations**: A function that verifies the tool calls made by the model.
- **htmlRoute** (Optional): Serve custom HTML content for the test at a specific path.

We look to test that the tools are used correctly without too rigid assertions. Avoid asserting exact argument values if they can vary (e.g., natural language reasoning), but ensure the core parameters (like URLs or selectors) were correct.

Example:

```ts
import {TestScenario} from '../eval_gemini.js';

export const scenario: TestScenario = {
  prompt: 'Navigate to example.com',
  maxTurns: 2,
  expectations: calls => {
    // Check that at least one call was 'browse_page'
    const navigation = calls.find(c => c.name === 'browse_page');
    if (!navigation) throw new Error('Model did not browse the page');
    // Verify essential args
    if (navigation.args.url !== 'http://example.com') {
      throw new Error(`Wrong URL: ${navigation.args.url}`);
    }
  },
};
```

## Restrictions on JSON schema

- no .nullable(), no .object() types. Enforced by the `@local/enforce-zod-schema` ESLint rule.
- represent complex object as a short formatted string.

```

### File: gemini-extension.json
```json
{
  "name": "chrome-devtools-mcp",
  "version": "latest",
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest"]
    }
  }
}

```

### File: release-please-config.json
```json
{
  "changelog-sections": [
    {"type": "feat", "section": "🎉 Features", "hidden": false},
    {"type": "fix", "section": "🛠️ Fixes", "hidden": false},
    {"type": "docs", "section": "📄 Documentation", "hidden": false},

    {"type": "perf", "section": "⚡ Performance", "hidden": false},
    {"type": "refactor", "section": "🏗️ Refactor", "hidden": false},
    {"type": "chore", "section": "♻️ Chores", "hidden": true},
    {"type": "test", "section": "♻️ Chores", "hidden": true},

    {"type": "build", "section": "⚙️ Automation", "hidden": true},
    {"type": "ci", "section": "⚙️ Automation", "hidden": true}
  ],

  "packages": {
    ".": {
      "extra-files": [
        {
          "type": "generic",
          "path": "src/version.ts"
        },
        {
          "type": "json",
          "path": "server.json",
          "jsonpath": "version"
        },
        {
          "type": "json",
          "path": "server.json",
          "jsonpath": "packages[0].version"
        },
        {
          "type": "json",
          "path": ".claude-plugin/marketplace.json",
          "jsonpath": "version"
        },
        {
          "type": "json",
          "path": ".claude-plugin/plugin.json",
          "jsonpath": "version"
        },
        {
          "type": "json",
          "path": ".github/plugin/plugin.json",
          "jsonpath": "version"
        }
      ]
    }
  }
}

```

### File: SECURITY.md
```md
## Security policy

The Chrome DevTools MCP project takes security very seriously. Please use [Chromium’s process to report security issues](https://www.chromium.org/Home/chromium-security/reporting-security-bugs/).

```

### File: server.json
```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.github.ChromeDevTools/chrome-devtools-mcp",
  "title": "Chrome DevTools MCP",
  "description": "MCP server for Chrome DevTools",
  "repository": {
    "url": "https://github.com/ChromeDevTools/chrome-devtools-mcp",
    "source": "github"
  },
  "version": "0.21.0",
  "packages": [
    {
      "registryType": "npm",
      "registryBaseUrl": "https://registry.npmjs.org",
      "identifier": "chrome-devtools-mcp",
      "version": "0.21.0",
      "transport": {
        "type": "stdio"
      },
      "environmentVariables": []
    }
  ]
}

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "es2023",
    "lib": [
      "ES2023",
      "DOM",
      "ES2024.Promise",
      "ES2025.Iterator",
      "ES2025.Collection"
    ],
    "types": ["node", "filesystem"],
    "moduleResolution": "bundler",
    "outDir": "./build",
    "rootDir": ".",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "noImplicitReturns": true,
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,
    "incremental": true,
    "allowJs": true,
    "useUnknownInCatchVariables": false
  },
  "include": [
    "src/**/*.ts",
    "tests/**/*.ts",
    "node_modules/chrome-devtools-frontend/front_end/core/common",
    "node_modules/chrome-devtools-frontend/front_end/core/host",
    "node_modules/chrome-devtools-frontend/front_end/core/i18n",
    "node_modules/chrome-devtools-frontend/front_end/core/platform",
    "node_modules/chrome-devtools-frontend/front_end/core/protocol_client",
    "node_modules/chrome-devtools-frontend/front_end/core/root",
    "node_modules/chrome-devtools-frontend/front_end/core/sdk",
    "node_modules/chrome-devtools-frontend/front_end/entrypoints/formatter_worker",
    "node_modules/chrome-devtools-frontend/front_end/foundation/foundation.ts",
    "node_modules/chrome-devtools-frontend/front_end/foundation/Universe.ts",
    "node_modules/chrome-devtools-frontend/front_end/generated",
    "node_modules/chrome-devtools-frontend/front_end/legacy/legacy-defs.d.ts",
    "node_modules/chrome-devtools-frontend/front_end/models/annotations",
    "node_modules/chrome-devtools-frontend/front_end/models/ai_assistance/data_formatters/NetworkRequestFormatter.ts",
    "node_modules/chrome-devtools-frontend/front_end/models/ai_assistance/data_formatters/PerformanceInsightFormatter.ts",
    "node_modules/chrome-devtools-frontend/front_end/models/ai_assistance/data_formatters/PerformanceTraceFormatter.ts",
    "node_modules/chrome-devtools-frontend/front_end/models/ai_assistance/data_formatters/UnitFormatters.ts",
    "node_modules/chrome-devtools-frontend/front_end/models/ai_assistance/performance",
    "node_modules/chrome-devtools-frontend/front_end/models/greendev",
    "node_modules/chrome-devtools-frontend/front_end/models/bindings",
    "node_modules/chrome-devtools-frontend/front_end/models/cpu_profile",
    "node_modules/chrome-devtools-frontend/front_end/models/crux-manager",
    "node_modules/chrome-devtools-frontend/front_end/models/emulation",
    "node_modules/chrome-devtools-frontend/front_end/models/formatter",
    "node_modules/chrome-devtools-frontend/front_end/models/geometry",
    "node_modules/chrome-devtools-frontend/front_end/models/issues_manager",
    "node_modules/chrome-devtools-frontend/front_end/models/logs",
    "node_modules/chrome-devtools-frontend/front_end/models/network_time_calculator",
    "node_modules/chrome-devtools-frontend/front_end/models/source_map_scopes",
    "node_modules/chrome-devtools-frontend/front_end/models/stack_trace",
    "node_modules/chrome-devtools-frontend/front_end/models/text_utils",
    "node_modules/chrome-devtools-frontend/front_end/models/trace_source_maps_resolver",
    "node_modules/chrome-devtools-frontend/front_end/models/trace",
    "node_modules/chrome-devtools-frontend/front_end/models/workspace",
    "node_modules/chrome-devtools-frontend/front_end/panels/issues/IssueAggregator.ts",
    "node_modules/chrome-devtools-frontend/front_end/third_party/acorn",
    "node_modules/chrome-devtools-frontend/front_end/third_party/codemirror",
    "node_modules/chrome-devtools-frontend/front_end/third_party/i18n",
    "node_modules/chrome-devtools-frontend/front_end/third_party/intl-messageformat",
    "node_modules/chrome-devtools-frontend/front_end/third_party/legacy-javascript",
    "node_modules/chrome-devtools-frontend/front_end/third_party/marked",
    "node_modules/chrome-devtools-frontend/front_end/third_party/source-map-scopes-codec",
    "node_modules/chrome-devtools-frontend/front_end/third_party/third-party-web",
    "node_modules/chrome-devtools-frontend/mcp"
  ],
  "exclude": ["node_modules/chrome-devtools-frontend/**/*.test.ts"],
  "files": [
    "node_modules/chrome-devtools-frontend/front_end/third_party/acorn/package/dist/acorn.mjs"
  ]
}

```

### File: .claude-plugin\marketplace.json
```json
{
  "name": "chrome-devtools-plugins",
  "version": "0.21.0",
  "description": "Bundled plugins for actuating and debugging the Chrome browser.",
  "repository": "https://github.com/ChromeDevTools/chrome-devtools-mcp",
  "owner": {
    "name": "Chrome DevTools Team",
    "email": "devtools-dev@chromium.org"
  },
  "plugins": [
    {
      "name": "chrome-devtools-mcp",
      "source": "./",
      "description": "Reliable automation, in-depth debugging, and performance analysis in Chrome using Chrome DevTools and Puppeteer"
    }
  ]
}

```

### File: .claude-plugin\plugin.json
```json
{
  "name": "chrome-devtools-mcp",
  "version": "0.21.0",
  "description": "Reliable automation, in-depth debugging, and performance analysis in Chrome using Chrome DevTools and Puppeteer",
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest"]
    }
  }
}

```

### File: docs\cli.md
```md
# Chrome DevTools CLI

The `chrome-devtools-mcp` package includes an **experimental** CLI interface that allows you to interact with the browser directly from your terminal. This is particularly useful for debugging or when you want an agent to generate scripts that automate browser actions.

## Getting started

Install the package globally to make the `chrome-devtools` command available:

```sh
npm i chrome-devtools-mcp@latest -g
chrome-devtools status # check if install worked.
```

## How it works

The CLI acts as a client to a background `chrome-devtools-mcp` daemon (uses Unix sockets on Linux/Mac and named pipes on Windows).

- **Automatic Start**: The first time you call a tool (e.g., `list_pages`), the CLI automatically starts the MCP server and the browser in the background if they aren't already running.
- **Persistence**: The same background instance is reused for subsequent commands, preserving the browser state (open pages, cookies, etc.).
- **Manual Control**: You can explicitly manage the background process using `start`, `stop`, and `status`. The `start` command forwards all subsequent arguments to the underlying MCP server (e.g., `--headless`, `--userDataDir`) but not all args are supported. Run `chrome-devtools start --help` for supported args. Headless is enabled by default. Isolated is enabled by default unless `--userDataDir` is provided.

```sh
# Check if the daemon is running
chrome-devtools status

# Navigate the current page to a URL
chrome-devtools navigate_page "https://google.com"

# Take a screenshot and save it to a file
chrome-devtools take_screenshot --filePath screenshot.png

# Stop the background daemon when finished
chrome-devtools stop
```

## Command Usage

The CLI supports all tools available in the [Tool reference](./tool-reference.md).

```sh
chrome-devtools <tool> [arguments] [flags]
```

- **Required Arguments**: Passed as positional arguments.
- **Optional Arguments**: Passed as flags (e.g., `--filePath`, `--fullPage`).

### Examples

**New Page and Navigation:**

```sh
chrome-devtools new_page "https://example.com"
chrome-devtools navigate_page "https://web.dev" --type url
```

**Interaction:**

```sh
# Click an element by its UID from a snapshot
chrome-devtools click "element-uid-123"

# Fill a form field
chrome-devtools fill "input-uid-456" "search query"
```

**Analysis:**

```sh
# Run a Lighthouse audit (defaults to navigation mode)
chrome-devtools lighthouse_audit --mode snapshot
```

## Output format

By default, the CLI outputs a human-readable summary of the tool's result. For programmatic use, you can request raw JSON:

```sh
chrome-devtools list_pages --output-format=json
```

## Troubleshooting

If the CLI hangs or fails to connect, try stopping the background process:

```sh
chrome-devtools stop
```

For more verbose logs, set the `DEBUG` environment variable:

```sh
DEBUG=* chrome-devtools list_pages
```

## CLI generation

Implemented in `scripts/generate-cli.ts`. Some commands are excluded from CLI
generation such as `wait_for` and `fill_form`.

`chrome-devtools-mcp` args are also filtered in `src/bin/chrome-devtools.ts`
because not all args make sense in a CLI interface.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

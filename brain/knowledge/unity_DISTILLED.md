---
id: unity
type: knowledge
owner: OA_Triage
---
# unity
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# [Unity Package Template](https://github.com/IvanMurzak/Unity-Package-Template)

<img width="100%" alt="Stats" src="https://user-images.githubusercontent.com/9135028/198754538-4dd93fc6-7eb2-42ae-8ac6-d7361c39e6ef.gif"/>

Unity Editor supports NPM packages. It is way more flexible solution in comparison with classic Plugin that Unity is using for years. NPM package supports versioning and dependencies. You may update / downgrade any package very easily. Also, Unity Editor has UPM (Unity Package Manager) that makes the process even simpler.

This template repository is designed to be easily updated into a real Unity package. Please follow the instruction bellow, it will help you to go through the entire process of package creation, distribution and installing.

# Steps to make your package

### 1️⃣ Click the button - create repository

[![create new repository](https://user-images.githubusercontent.com/9135028/198753285-3d3c9601-0711-43c7-a8f2-d40ec42393a2.png)](https://github.com/IvanMurzak/Unity-Package-Template/generate)

### 2️⃣ Clone your new repository

### 3️⃣ Initialize Project

Use the initialization script to rename the package and replace all placeholders.

```powershell
./commands/init.ps1 -PackageId "com.company.package" -PackageName "My Package"
```

This script will:
- Rename directories and files.
- Replace `YOUR_PACKAGE_ID`, `YOUR_PACKAGE_NAME`, etc. in all files and folder names.

### 4️⃣ Update `package.json`
Open `Unity-Package/Assets/root/package.json` and update:
- `description`
- `author`
- `keywords`
- `unity` (minimum supported Unity version)

### 5️⃣ Generate Meta Files

#### Using script
   Open Unity project to generate `.meta` files.
   **On Mac and Linux**:
   ```bash
   ./commands/open-all-projects-unix.sh
   ```
   **On Windows**:
   ```bash
   ./commands/open-all-projects-windows.ps1
   ```
#### OR Manually
   You may open the projects manually to achieve the same result.
   - Open Unity Hub.
   - Add the `Installer` folder as a project.
   - Add the `Unity-Package` folder as a project.
   - Open both projects in Unity Editor. This will generate the necessary `.meta` files.

### 6️⃣ Add files into `Unity-Package/Assets/root` folder

[Unity guidelines](https://docs.unity3d.com/Manual/cus-layout.html) about organizing files into the package root directory

```text
  <root>
  ├── package.json
  ├── README.md
  ├── CHANGELOG.md
  ├── LICENSE.md
  ├── Third Party Notices.md
  ├── Editor
  │   ├── [company-name].[package-name].Editor.asmdef
  │   └── EditorExample.cs
  ├── Runtime
  │   ├── [company-name].[package-name].asmdef
  │   └── RuntimeExample.cs
  ├── Tests
  │   ├── Editor
  │   │   ├── [company-name].[package-name].Editor.Tests.asmdef
  │   │   └── EditorExampleTest.cs
  │   └── Runtime
  │        ├── [company-name].[package-name].Tests.asmdef
  │        └── RuntimeExampleTest.cs
  ├── Samples~
  │        ├── SampleFolder1
  │        ├── SampleFolder2
  │        └── ...
  └── Documentation~
       └── [package-name].md
```

# Optional steps

### 1. Version Management

To update the package version across all files (package.json, Installer.cs, etc.), use the bump version script:

```powershell
.\commands\bump-version.ps1 -NewVersion "1.0.1"
```

### 2. Setup CI/CD

To enable automatic testing and deployment:

1.  **Configure GitHub Secrets**
    Go to `Settings` > `Secrets and variables` > `Actions` > `New repository secret` and add:
    -   `UNITY_EMAIL`: Your Unity account email.
    -   `UNITY_PASSWORD`: Your Unity account password.
    -   `UNITY_LICENSE`: Content of your `Unity_lic.ulf` file.
        -   Windows: `C:/ProgramData/Unity/Unity_lic.ulf`
        -   Mac: `/Library/Application Support/Unity/Unity_lic.ulf`
        -   Linux: `~/.local/share/unity3d/Unity/Unity_lic.ulf`

2.  **Enable Workflows**
    Rename the sample workflow files to enable them:
    -   `.github/workflows/release.yml-sample` ➡️ `.github/workflows/release.yml`
    -   `.github/workflows/test_pull_request.yml-sample` ➡️ `.github/workflows/test_pull_request.yml`

3.  **Update Unity Version**
    Open both `.yml` files and update the `UNITY_VERSION` (or similar variable) to match your project's Unity Editor version.

4.  **Automatic Deployment**
    The release workflow triggers automatically when you push to the `main` branch with an incremented version in `package.json`.

# Final polishing

- Update the `README.md` file (this file) with information about your package.
- Copy the updated `README.md` to `Assets/root` as well.

> ⚠️ Everything outside of the `root` folder won't be added to your package. But still could be used for testing or showcasing your package at your repository.

### 1. Deploy to any registry you like

- [Deploy to OpenUPM](https://github.com/IvanMurzak/Unity-Package-Template/blob/main/Docs/Deploy-OpenUPM.md) (recommended)
- [Deploy using GitHub](https://github.com/IvanMurzak/Unity-Package-Template/blob/main/Docs/Deploy-GitHub.md)
- [Deploy to npmjs.com](https://github.com/IvanMurzak/Unity-Package-Template/blob/main/Docs/Deploy-npmjs.md)

### 2. Install your package into Unity Project

When your package is distributed, you can install it into any Unity project.

> Don't install into the same Unity project, please use another one.

- [Install OpenUPM-CLI](https://github.com/openupm/openupm-cli#installation)
- Open a command line at the root of Unity project (the folder which contains `Assets`)
- Execute the command (for `OpenUPM` hosted package)

  ```bash
  openupm add YOUR_PACKAGE_NAME
  ```

# Final view in Unity Package Manager

![image](https://user-images.githubusercontent.com/9135028/198777922-fdb71949-aee7-49c8-800f-7db885de9453.png)

```

### File: cli\package.json
```json
{
  "name": "unity-mcp-cli",
  "version": "0.63.3",
  "description": "Cross-platform CLI tool for AI Game Developer (Skills & MCP). Full AI develop and test loop. Efficient token usage, advanced tools. Creates Unity project, installs plugins, configures tools, and manages HTTP connection with Unity Editor and a game made with Unity. Works with Claude Code, Gemini, Copilot, Cursor and any other absolutely for free.",
  "type": "module",
  "main": "dist/index.js",
  "bin": {
    "unity-mcp-cli": "bin/unity-mcp-cli.js"
  },
  "scripts": {
    "build": "tsc",
    "pretest": "npm run build",
    "test": "vitest run",
    "test:watch": "vitest",
    "prepublishOnly": "npm run build",
    "prepack": "npm run build"
  },
  "keywords": [
    "cli",
    "unity",
    "unity ai",
    "unity skills",
    "unity mcp",
    "ai skills",
    "ai mcp",
    "ai",
    "mcp",
    "model-context-protocol",
    "gamedev",
    "game-dev"
  ],
  "author": {
    "name": "Ivan Murzak",
    "url": "https://github.com/IvanMurzak"
  },
  "license": "Apache-2.0",
  "repository": {
    "type": "git",
    "url": "https://github.com/IvanMurzak/Unity-MCP.git",
    "directory": "cli"
  },
  "engines": {
    "node": "^20.19.0 || >=22.12.0"
  },
  "dependencies": {
    "chalk": "^5.6.2",
    "commander": "^13.1.0",
    "yocto-spinner": "^1.1.0"
  },
  "devDependencies": {
    "@types/node": "^22.15.0",
    "typescript": "^5.8.0",
    "vitest": "^3.1.0"
  }
}
```

### File: cli\README.md
```md
<div align="center" width="100%">
  <h1>Unity MCP — <i>CLI</i></h1>

[![npm](https://img.shields.io/npm/v/unity-mcp-cli?label=npm&labelColor=333A41 'npm package')](https://www.npmjs.com/package/unity-mcp-cli)
[![Node.js](https://img.shields.io/badge/Node.js-%5E20.19.0%20%7C%7C%20%3E%3D22.12.0-5FA04E?logo=nodedotjs&labelColor=333A41 'Node.js')](https://nodejs.org/)
[![License](https://img.shields.io/github/license/IvanMurzak/Unity-MCP?label=License&labelColor=333A41)](https://github.com/IvanMurzak/Unity-MCP/blob/main/LICENSE)
[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/badges/StandWithUkraine.svg)](https://stand-with-ukraine.pp.ua)

  <img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/promo/ai-developer-banner-glitch.gif" alt="AI Game Developer" title="Unity MCP CLI" width="100%">

  <p>
    <a href="https://claude.ai/download"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/claude-64.png" alt="Claude" title="Claude" height="36"></a>&nbsp;&nbsp;
    <a href="https://openai.com/index/introducing-codex/"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/codex-64.png" alt="Codex" title="Codex" height="36"></a>&nbsp;&nbsp;
    <a href="https://www.cursor.com/"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/cursor-64.png" alt="Cursor" title="Cursor" height="36"></a>&nbsp;&nbsp;
    <a href="https://code.visualstudio.com/docs/copilot/overview"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/github-copilot-64.png" alt="GitHub Copilot" title="GitHub Copilot" height="36"></a>&nbsp;&nbsp;
    <a href="https://gemini.google.com/"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/gemini-64.png" alt="Gemini" title="Gemini" height="36"></a>&nbsp;&nbsp;
    <a href="https://antigravity.google/"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/antigravity-64.png" alt="Antigravity" title="Antigravity" height="36"></a>&nbsp;&nbsp;
    <a href="https://code.visualstudio.com/"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/vs-code-64.png" alt="VS Code" title="VS Code" height="36"></a>&nbsp;&nbsp;
    <a href="https://www.jetbrains.com/rider/"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/rider-64.png" alt="Rider" title="Rider" height="36"></a>&nbsp;&nbsp;
    <a href="https://visualstudio.microsoft.com/"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/visual-studio-64.png" alt="Visual Studio" title="Visual Studio" height="36"></a>&nbsp;&nbsp;
    <a href="https://github.com/anthropics/claude-code"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/open-code-64.png" alt="Open Code" title="Open Code" height="36"></a>&nbsp;&nbsp;
    <a href="https://github.com/cline/cline"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/cline-64.png" alt="Cline" title="Cline" height="36"></a>&nbsp;&nbsp;
    <a href="https://github.com/Kilo-Org/kilocode"><img src="https://github.com/IvanMurzak/Unity-MCP/raw/main/docs/img/mcp-clients/kilo-code-64.png" alt="Kilo Code" title="Kilo Code" height="36"></a>
  </p>

</div>

<b>[中文](https://github.com/IvanMurzak/Unity-MCP/blob/main/cli/docs/README.zh-CN.md) | [日本語](https://github.com/IvanMurzak/Unity-MCP/blob/main/cli/docs/README.ja.md) | [Español](https://github.com/IvanMurzak/Unity-MCP/blob/main/cli/docs/README.es.md)</b>

Cross-platform CLI tool for **[Unity MCP](https://github.com/IvanMurzak/Unity-MCP)** — create projects, install plugins, configure MCP tools, and launch Unity with active MCP connections. All from a single command line.

## ![AI Game Developer — Unity SKILLS and MCP](https://github.com/IvanMurzak/Unity-MCP/blob/main/docs/img/promo/hazzard-features.svg?raw=true)

- :white_check_mark: **Create projects** — scaffold new Unity projects via Unity Editor
- :white_check_mark: **Install editors** — install any Unity Editor version from the command line
- :white_check_mark: **Install plugin** — add Unity-MCP plugin to `manifest.json` with all required scoped registries
- :white_check_mark: **Remove plugin** — remove Unity-MCP plugin from `manifest.json`
- :white_check_mark: **Configure** — enable/disable MCP tools, prompts, and resources
- :white_check_mark: **Status check** — see Unity process, local server, and cloud server connection status at a glance
- :white_check_mark: **Run tools** — execute MCP tools directly from the command line
- :white_check_mark: **Setup MCP** — write AI agent MCP config files for any of 14 supported agents
- :white_check_mark: **Setup skills** — generate skill files for AI agents via the MCP server
- :white_check_mark: **Wait for ready** — poll until Unity Editor and MCP server are connected and accepting tool calls
- :white_check_mark: **Open & Connect** — launch Unity with optional MCP environment variables for automated server connection
- :white_check_mark: **Cross-platform** — Windows, macOS, and Linux
- :white_check_mark: **CI-friendly** — auto-detects non-interactive terminals and disables spinners/colors
- :white_check_mark: **Verbose mode** — use `--verbose` on any command for detailed diagnostic output
- :white_check_mark: **Version-aware** — never downgrades plugin versions, resolves latest from OpenUPM

![AI Game Developer — Unity SKILLS and MCP](https://github.com/IvanMurzak/Unity-MCP/blob/main/docs/img/promo/hazzard-divider.svg?raw=true)

# Quick Start

Install globally and run:

```bash
# 1.1 Install unity-mcp-cli                                #  ┌────────────────────┐
npm install -g unity-mcp-cli                               #  │ Available AI agent │
                                                           #  ├────────────────────┤
# 1.2 (Optional) Install Unity                             #  │ antigravity        │
unity-mcp-cli install-unity                                #  │ claude-code        │
                                                           #  │ claude-desktop     │
# 1.3 (Optional) Create Unity project                      #  │ cline              │
unity-mcp-cli create-project ./MyUnityProject              #  │ codex              │
                                                           #  │ cursor             │
# 2. Install "AI Game Developer" in Unity project          #  │ gemini             │
unity-mcp-cli install-plugin ./MyUnityProject              #  │ github-copilot-cli │
                                                           #  │ kilo-code          │
# 3. Login to cloud server                                 #  │ open-code          │
unity-mcp-cli login ./MyUnityProject                       #  │ rider-junie        │
                                                           #  │ unity-ai           │
# 4. Open Unity project (auto-connects and generates skills)  │ vs-copilot         │
unity-mcp-cli open ./MyUnityProject                        #  │ vscode-copilot     │
                                                           #  └────────────────────┘
# 5. Wait for Unity Editor to be ready
unity-mcp-cli wait-for-ready ./MyUnityProject
```

Or run any command instantly with `npx` — no global installation required:

```bash
npx unity-mcp-cli install-plugin /path/to/unity/project
```

> **Requirements:** [Node.js](https://nodejs.org/) ^20.19.0 || >=22.12.0. [Unity Hub](https://unity.com/download) is installed automatically if not found.

![AI Game Developer — Unity SKILLS and MCP](https://github.com/IvanMurzak/Unity-MCP/blob/main/docs/img/promo/hazzard-divider.svg?raw=true)

# Contents

- [Quick Start](#quick-start)
- [Contents](#contents)
- [Commands](#commands)
  - [`configure`](#configure)
  - [`create-project`](#create-project)
  - [`install-plugin`](#install-plugin)
  - [`install-unity`](#install-unity)
  - [`open`](#open)
  - [`run-tool`](#run-tool)
  - [`wait-for-ready`](#wait-for-ready)
  - [`setup-mcp`](#setup-mcp)
  - [`setup-skills`](#setup-skills)
  - [`remove-plugin`](#remove-plugin)
  - [`status`](#status)
  - [Global Options](#global-options)
- [Full Automation Example](#full-automation-example)
- [How It Works](#how-it-works)
    - [Deterministic Port](#deterministic-port)
    - [Plugin Installation](#plugin-installation)
    - [Configuration File](#configuration-file)
    - [Unity Hub Integration](#unity-hub-integration)

![AI Game Developer — Unity SKILLS and MCP](https://github.com/IvanMurzak/Unity-MCP/blob/main/docs/img/promo/hazzard-divider.svg?raw=true)

# Commands

## `configure`

Configure MCP tools, prompts, and resources in `UserSettings/AI-Game-Developer-Config.json`.

```bash
unity-mcp-cli configure ./MyGame --list
```

| Option | Required | Description |
|---|---|---|
| `[path]` | Yes | Path to the Unity project (positional or `--path`) |
| `--list` | No | List current configuration and exit |
| `--enable-tools <names>` | No | Enable specific tools (comma-separated) |
| `--disable-tools <names>` | No | Disable specific tools (comma-separated) |
| `--enable-all-tools` | No | Enable all tools |
| `--disable-all-tools` | No | Disable all tools |
| `--enable-prompts <names>` | No | Enable specific prompts (comma-separated) |
| `--disable-prompts <names>` | No | Disable specific prompts (comma-separated) |
| `--enable-all-prompts` | No | Enable all prompts |
| `--disable-all-prompts` | No | Disable all prompts |
| `--enable-resources <names>` | No | Enable specific resources (comma-separated) |
| `--disable-resources <names>` | No | Disable specific resources (comma-separated) |
| `--enable-all-resources` | No | Enable all resources |
| `--disable-all-resources` | No | Disable all resources |

**Example — enable specific tools and disable all prompts:**

```bash
unity-mcp-cli configure ./MyGame \
  --enable-tools gameobject-create,gameobject-find \
  --disable-all-prompts
```

**Example — enable everything:**

```bash
unity-mcp-cli configure ./MyGame \
  --enable-all-tools \
  --enable-all-prompts \
  --enable-all-resources
```

![AI Game Developer — Unity SKILLS and MCP](https://github.com/IvanMurzak/Unity-MCP/blob/main/docs/img/promo/hazzard-divider.svg?raw=true)

## `create-project`

Create a new Unity project using the Unity Editor.

```bash
unity-mcp-cli create-project /path/to/new/project
```

| Option | Required | Description |
|---|---|---|
| `[path]` | Yes | Path where the project will be created (positional or `--path`) |
| `--unity <version>` | No | Unity Editor version to use (defaults to highest installed) |

**Example — create a project with a specific editor version:**

```bash
unity-mcp-cli create-project ./MyGame --unity 2022.3.62f1
```

![AI Game Developer — Unity SKILLS and MCP](https://github.com/IvanMurzak/Unity-MCP/blob/main/docs/img/promo/hazzard-divider.svg?raw=true)

## `install-plugin`

Install the Unity-MCP plugin into a Unity project's `Packages/manifest.json`.

```bash
unity-mcp-cli install-plugin ./MyGame
```

| Option | Required | Description |
|---|---|---|
| `[path]` | Yes | Path to the Unity project (positional or `--path`) |
| `--plugin-version <version>` | No | Plugin version to install (defaults to latest from [OpenUPM](https://openupm.com/packages/com.ivanmurzak.unity.mcp/)) |

This command:
1. Adds the **OpenUPM scoped registry** with all required scopes
2. Adds `com.ivanmurzak.unity.mcp` to `dependencies`
3. **Never downgrades** — if a higher version is already installed, it is preserved

**Example — install a specific plugin version:**

```bash
unity-mcp-cli install-plugin ./MyGame --plugin-version 0.51.6
```

> After running this command, open the project in Unity Editor to complete the package installation.

![AI Game Developer — Unity SKILLS and MCP](https://github.com/IvanMurzak/Unity-MCP/blob/main/docs/img/promo/hazzard-divider.svg?raw=true)

## `install-unity`

Install a Unity Editor version via Unity Hub CLI.

```bash
unity-mcp-cli install-unity 6000.3.1f1
```

| Argument / Option | Required | Description |
|---|---|---|
| `[version]` | No | Unity Editor version to install (e.g. `6000.3.1f1`) |
| `--path <path>` | No | Read the required version from an existing project |

If neither argument nor option is provided, the command installs the latest stable release from Unity Hub's releases list.

**Example — install the editor version that a project needs:**

```bash
unity-mcp-cli install-unity --path ./MyGame
```

![AI Game Developer — Unity SKILLS and MCP](https://github.com/IvanMurzak/Unity-MCP/blob/main/docs/img/promo/hazzard-divider.svg?raw=true)

## `open`

Open a Unity project in the Unity Editor. By default, sets MCP connection environment variables if connection options are provided. Use `--no-connect` to open without MCP connection.

```bash
unity-mcp-cli open ./MyGame
```

| Option | Env Variable | Required | Description |
|---|---|---|---|
| `[path]` | — | Yes | Path to the Unity project (positional or `--path`) |
| `--unity <version>` | — | No | Specific Unity Editor version to use (defaults to version from project settings, falls back to highest installed) |
| `--no-connect` | — | No | Open without MCP connection environment variables |
| `--url <url>` | `UNITY_MCP_HOST` | No | MCP server URL to connect to |
| `--keep-connected` | `UNITY_MCP_KEEP_CONNECTED` | No | Force keep the connection alive |
| `--token <token>` | `UNITY_MCP_TOKEN` | No | Authentication token |
| `--auth <option>` | `UNITY_MCP_AUTH_OPTION` | No | Auth mode: `none` or `required` |
| `--tools <names>` | `UNITY_MCP_TOOLS` | No | Comma-separated list of tools to enable |
| `--transport <method>` | `UNITY_MCP_TRANSPORT` | No | Transport method: `streamableHttp` or `stdio` |
| `--start-server <value>` | `UNITY_MCP_START_SERVER` | No | Set to `true` or `false` to control MCP server auto-start |

The editor process is spawned in detached mode — the CLI returns immediately.

**Example — open with MCP connection:**

```bash
unity-mcp-cli open ./MyGame \
  --url http://localhost:8080 \
  --keep-connected
```

**Example — open without MCP connection (simple open):**

```bash
unity-mcp-cli open ./MyGame --no-connect
```

**Example — open with authentication and specific tools:**

```bash
unity-mcp-cli open ./MyGame \
  --url http://my-server:8080 \
  --token my-secret-token \
  --auth required \
  --tools gameobject-create,gameobject-find
```

![AI Game Developer — Unity SKILLS and MCP](https://github.com/IvanMurzak/Unity-MCP/blob/main/docs/img/promo/hazzard-divider.svg?raw=true)

## `run-tool`

Execute an MCP tool directly via the HTTP API. The server URL and authorization token are **automatically resolved** from the project's config file (`UserSettings/AI-Game-Developer-Config.json`), based on the current connection mode (Custom or Cloud).

```bash
unity-mcp-cli run-tool gameobject-create ./MyGame --input '{"name":"Cube"}'
```

| Option | Required | Description |
|---|---
... [TRUNCATED]
```

### File: CLAUDE.md
```md
# CLAUDE.md

## Repository Overview

Unity-MCP bridges LLMs (Claude, Cursor, Copilot, etc.) with Unity Editor and Runtime via the [Model Context Protocol](https://modelcontextprotocol.io/). It consists of these sub-projects:

| Sub-project | Location | Description |
|---|---|---|
| MCP Server | [Unity-MCP-Server/](Unity-MCP-Server/) | C# ASP.NET Core server — bridges MCP clients and Unity Plugin via SignalR |
| MCP Plugin | [Unity-MCP-Plugin/](Unity-MCP-Plugin/) | Unity Editor/Runtime plugin — executes MCP tools and manages connection |
| CLI | [cli/](cli/) | Command-line interface for Unity-MCP |
| Installer | [Installer/](Installer/) | Unity package that installs the plugin and its dependencies |
| Unity-Tests | [Unity-Tests/](Unity-Tests/) | Test project for Unity-MCP |

## System Architecture

```
MCP Client (Claude/Cursor/etc.)
      ↕ stdio or streamableHttp
Unity-MCP-Server  (ASP.NET Core + MCP SDK)
      ↕ SignalR
Unity-MCP-Plugin  (Unity Editor/Runtime)
      ↕ Unity API (main thread)
Unity Engine
```

- The **MCP Server** is a standalone binary downloaded automatically by the plugin to `Library/mcp-server/{platform}/`. It is also published to Docker Hub and NuGet.
- The **MCP Plugin** auto-starts the server binary on Unity Editor load (`[InitializeOnLoad]`). Port is deterministic: SHA256 hash of project path, mapped to 20000–29999.
- Communication inside Unity always runs on the **main thread** via `MainThread.Instance.Run()`.

## Release & Versioning

Version is sourced from [Unity-MCP-Plugin/Assets/root/package.json](Unity-MCP-Plugin/Assets/root/package.json). Bump with `.\commands\bump-version.ps1 <version>`.

## CI/CD

See `.github/workflows/` for all pipelines. PRs from untrusted contributors require a `ci-ok` label from a maintainer before CI runs.

## Key Coding Conventions

These apply across both C# sub-projects:

- `#nullable enable` at the top of every file
- Copyright box comment header in every file
- MCP tool classes are `partial` — one operation per file (e.g., `Tool_GameObject.Create.cs`)
- MCP tools MUST return structured types (data models, `List<T>`, `void`, or `Task`) — avoid raw string returns
- All Unity API calls must use `MainThread.Instance.Run(() => ...)` or `RunAsync()`
- Tool/prompt names use **kebab-case** with category prefix (e.g., `gameobject-create`, `assets-find`)
- Namespace pattern: `com.IvanMurzak.Unity.MCP.[Tier].[Component]`
- **No Reflection for private access** — C# Reflection (`System.Reflection`) MUST NOT be used to access private, internal, or non-public members. Exception: `ReflectorNet` library usage is allowed.

## Project Constitution

Non-negotiable principles and architecture constraints: [`.specify/memory/constitution.md`](.specify/memory/constitution.md)

**Code review**: You MUST read the constitution before performing any code review. It contains critical rules for code quality, safety, and project governance that all reviews must verify against.

## Documentation

```
README.md                                                        ← Root project documentation
Unity-MCP-Plugin/Assets/root/README.md                           ← Copy of root README.md *
Installer/Assets/com.IvanMurzak/AI Game Dev Installer/README.md  ← Copy of root README.md *
docs/
├── README.es.md                                                 ← Spanish translation of root README *
├── README.ja.md                                                 ← Japanese translation *
└── README.zh-CN.md                                              ← Simplified Chinese translation *
Unity-MCP-Server/README.md                                       ← MCP Server documentation
Unity-MCP-Server/MCP-Test-Client/README.md                       ← Test client documentation
cli/README.md                                                    ← CLI documentation
cli/docs/
├── README.es.md                                                 ← Spanish translation of CLI README
├── README.ja.md                                                 ← Japanese translation
└── README.zh-CN.md                                              ← Simplified Chinese translation
```

Files marked with `*` MUST be kept in sync with `README.md` when it changes.

```

### File: .claude\settings.json
```json
{
  "permissions": {
    "allow": [
      "Bash(*)",
      "Read(*)",
      "WebFetch(*)",
      "mcp__ai-game-developer__*"
    ],
    "additionalDirectories": []
  },
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": [
    "ai-game-developer"
  ],
  "enabledPlugins": {
    "csharp-lsp@claude-plugins-official": true
  }
}
```

### File: .github\copilot-instructions.md
```md
# Project Guidelines

## Critical Rules

### No C# Reflection for Private Access

**PROHIBITED**: Using `System.Reflection` to access private, internal, or otherwise non-public fields, properties, methods, or classes in project code. This includes `Type.GetType`, `BindingFlags.NonPublic`, `GetMethod`, `GetField`, `GetProperty`, and similar reflection APIs when used to bypass access modifiers.

**Example of prohibited code:**
```csharp
// WRONG: Accessing internal Unity API via reflection
var logEntriesType = Type.GetType("UnityEditor.LogEntries, UnityEditor.CoreModule")
                  ?? Type.GetType("UnityEditorInternal.LogEntries, UnityEditor.CoreModule")
                  ?? Type.GetType("UnityEditor.LogEntries, UnityEditor")
                  ?? Type.GetType("UnityEditorInternal.LogEntries, UnityEditor");
logEntriesType?.GetMethod("Clear", BindingFlags.Static | BindingFlags.Public)
              ?.Invoke(null, null);
```

> **Note**: This rule does NOT apply to `ReflectorNet` library usage, which is an external dependency specifically designed for reflection-based access patterns.

## Code Review

Before performing any code review, you **MUST** read the project constitution: [`.specify/memory/constitution.md`](.specify/memory/constitution.md). All code review feedback must verify adherence to the principles defined in the constitution. Constitution principles supersede ad-hoc practices when conflicts arise.

## Code Style
- **C#**: Use 4 spaces indentation. PascalCase for classes/methods/properties, `_camelCase` for private readonly fields.
    - Namespace: `com.IvanMurzak.Unity.MCP`.
    - Example: [UnityMcpPlugin.cs](Unity-MCP-Plugin/Assets/root/Runtime/UnityMcpPlugin.cs).
- **PowerShell**: Use K&R brace style.

## Architecture
- **Unity-MCP-Plugin**: Main Unity package.
    - Core logic: [Assets/root/Runtime](Unity-MCP-Plugin/Assets/root/Runtime).
    - Editor logic: `Assets/root/Editor`.
    - Tests: `Assets/root/Tests`.
- **Unity-MCP-Server**: ASP.NET Core bridging LLMs and Unity.
    - Entry point: [Program.cs](Unity-MCP-Server/src/Program.cs) (or similar in project root/src).
    - SignalR Hub: `RemoteApp` (referenced in CLAUDE.md).
- **Installer**: [Installer/](Installer/) wraps the package installation.
- **Unity-Tests**: [Unity-Tests/](Unity-Tests/) contains projects for different Unity versions (2022, 2023, 6000) linking locally to the Plugin.

## Build and Test
- **Plugin**:
    - Auto-compiles in Unity.
    - Run tests: [commands/run-unity-tests.ps1](commands/run-unity-tests.ps1).
    - Editor Tests: `Assets/root/Tests/Editor`.
- **Server**:
    - Build: `.\Unity-MCP-Server\build-all.ps1`.
    - Run: `dotnet run --project Unity-MCP-Server/com.IvanMurzak.Unity.MCP.Server.csproj`.
- **Commands**: See [commands/](commands/) for utility scripts (release, tests).

## Project Conventions
- **MCP Tools**: Implemented using attributes in the Plugin. Reflection-based access via `ReflectorNet`.
- **Documentation**:
    - [Unity-MCP.wiki](Unity-MCP.wiki/) for user docs.
    - [docs/](docs/) for translations and repo docs.
    - See `CLAUDE.md` in subdirectories for specific agent notes.
- **Versioning**: `package.json` in `Unity-MCP-Plugin/Assets/root/package.json`.

## Integration Points
- **Communication**: SignalR between Server and Plugin.
- **Dependencies**: OpenUPM for external packages.

## Security
- **Server Transport**: Configurable via `--client-transport` (`stdio` or `streamableHttp`).

```

### File: .specify\init-options.json
```json
{
  "ai": "claude",
  "ai_commands_dir": null,
  "ai_skills": false,
  "here": true,
  "preset": null,
  "script": "ps",
  "speckit_version": "0.3.0"
}
```

### File: cli\package-lock.json
```json
{
  "name": "unity-mcp-cli",
  "version": "0.63.3",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "unity-mcp-cli",
      "version": "0.63.3",
      "license": "Apache-2.0",
      "dependencies": {
        "chalk": "^5.6.2",
        "commander": "^13.1.0",
        "yocto-spinner": "^1.1.0"
      },
      "bin": {
        "unity-mcp-cli": "bin/unity-mcp-cli.js"
      },
      "devDependencies": {
        "@types/node": "^22.15.0",
        "typescript": "^5.8.0",
        "vitest": "^3.1.0"
      },
      "engines": {
        "node": "^20.19.0 || >=22.12.0"
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.4.tgz",
      "integrity": "sha512-cQPwL2mp2nSmHHJlCyoXgHGhbEPMrEEU5xhkcy3Hs/O7nGZqEpZ2sUtLaL9MORLtDfRvVl2/3PAuEkYZH0Ty8Q==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "aix"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.4.tgz",
      "integrity": "sha512-X9bUgvxiC8CHAGKYufLIHGXPJWnr0OCdR0anD2e21vdvgCI8lIfqFbnoeOz7lBjdrAGUhqLZLcQo6MLhTO2DKQ==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.4.tgz",
      "integrity": "sha512-gdLscB7v75wRfu7QSm/zg6Rx29VLdy9eTr2t44sfTW7CxwAtQghZ4ZnqHk3/ogz7xao0QAgrkradbBzcqFPasw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/android-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.4.tgz",
      "integrity": "sha512-PzPFnBNVF292sfpfhiyiXCGSn9HZg5BcAz+ivBuSsl6Rk4ga1oEXAamhOXRFyMcjwr2DVtm40G65N3GLeH1Lvw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.4.tgz",
      "integrity": "sha512-b7xaGIwdJlht8ZFCvMkpDN6uiSmnxxK56N2GDTMYPr2/gzvfdQN8rTfBsvVKmIVY/X7EM+/hJKEIbbHs9oA4tQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/darwin-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.4.tgz",
      "integrity": "sha512-sR+OiKLwd15nmCdqpXMnuJ9W2kpy0KigzqScqHI3Hqwr7IXxBp3Yva+yJwoqh7rE8V77tdoheRYataNKL4QrPw==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.4.tgz",
      "integrity": "sha512-jnfpKe+p79tCnm4GVav68A7tUFeKQwQyLgESwEAUzyxk/TJr4QdGog9sqWNcUbr/bZt/O/HXouspuQDd9JxFSw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/freebsd-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.27.4.tgz",
      "integrity": "sha512-2kb4ceA/CpfUrIcTUl1wrP/9ad9Atrp5J94Lq69w7UwOMolPIGrfLSvAKJp0RTvkPPyn6CIWrNy13kyLikZRZQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.27.4.tgz",
      "integrity": "sha512-aBYgcIxX/wd5n2ys0yESGeYMGF+pv6g0DhZr3G1ZG4jMfruU9Tl1i2Z+Wnj9/KjGz1lTLCcorqE2viePZqj4Eg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.27.4.tgz",
      "integrity": "sha512-7nQOttdzVGth1iz57kxg9uCz57dxQLHWxopL6mYuYthohPKEK0vU0C3O21CcBK6KDlkYVcnDXY099HcCDXd9dA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ia32": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.27.4.tgz",
      "integrity": "sha512-oPtixtAIzgvzYcKBQM/qZ3R+9TEUd1aNJQu0HhGyqtx6oS7qTpvjheIWBbes4+qu1bNlo2V4cbkISr8q6gRBFA==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-loong64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.27.4.tgz",
      "integrity": "sha512-8mL/vh8qeCoRcFH2nM8wm5uJP+ZcVYGGayMavi8GmRJjuI3g1v6Z7Ni0JJKAJW+m0EtUuARb6Lmp4hMjzCBWzA==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-mips64el": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.27.4.tgz",
      "integrity": "sha512-1RdrWFFiiLIW7LQq9Q2NES+HiD4NyT8Itj9AUeCl0IVCA459WnPhREKgwrpaIfTOe+/2rdntisegiPWn/r/aAw==",
      "cpu": [
        "mips64el"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-ppc64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.27.4.tgz",
      "integrity": "sha512-tLCwNG47l3sd9lpfyx9LAGEGItCUeRCWeAx6x2Jmbav65nAwoPXfewtAdtbtit/pJFLUWOhpv0FpS6GQAmPrHA==",
      "cpu": [
        "ppc64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-riscv64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.27.4.tgz",
      "integrity": "sha512-BnASypppbUWyqjd1KIpU4AUBiIhVr6YlHx/cnPgqEkNoVOhHg+YiSVxM1RLfiy4t9cAulbRGTNCKOcqHrEQLIw==",
      "cpu": [
        "riscv64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-s390x": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.27.4.tgz",
      "integrity": "sha512-+eUqgb/Z7vxVLezG8bVB9SfBie89gMueS+I0xYh2tJdw3vqA/0ImZJ2ROeWwVJN59ihBeZ7Tu92dF/5dy5FttA==",
      "cpu": [
        "s390x"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/linux-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.27.4.tgz",
      "integrity": "sha512-S5qOXrKV8BQEzJPVxAwnryi2+Iq5pB40gTEIT69BQONqR7JH1EPIcQ/Uiv9mCnn05jff9umq/5nqzxlqTOg9NA==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.27.4.tgz",
      "integrity": "sha512-xHT8X4sb0GS8qTqiwzHqpY00C95DPAq7nAwX35Ie/s+LO9830hrMd3oX0ZMKLvy7vsonee73x0lmcdOVXFzd6Q==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/netbsd-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.27.4.tgz",
      "integrity": "sha512-RugOvOdXfdyi5Tyv40kgQnI0byv66BFgAqjdgtAKqHoZTbTF2QqfQrFwa7cHEORJf6X2ht+l9ABLMP0dnKYsgg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "netbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-0.27.4.tgz",
      "integrity": "sha512-2MyL3IAaTX+1/qP0O1SwskwcwCoOI4kV2IBX1xYnDDqthmq5ArrW94qSIKCAuRraMgPOmG0RDTA74mzYNQA9ow==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openbsd-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.27.4.tgz",
      "integrity": "sha512-u8fg/jQ5aQDfsnIV6+KwLOf1CmJnfu1ShpwqdwC0uA7ZPwFws55Ngc12vBdeUdnuWoQYx/SOQLGDcdlfXhYmXQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openbsd"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/openharmony-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/openharmony-arm64/-/openharmony-arm64-0.27.4.tgz",
      "integrity": "sha512-JkTZrl6VbyO8lDQO3yv26nNr2RM2yZzNrNHEsj9bm6dOwwu9OYN28CjzZkH57bh4w0I2F7IodpQvUAEd1mbWXg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "openharmony"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/sunos-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.27.4.tgz",
      "integrity": "sha512-/gOzgaewZJfeJTlsWhvUEmUG4tWEY2Spp5M20INYRg2ZKl9QPO3QEEgPeRtLjEWSW8FilRNacPOg8R1uaYkA6g==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "sunos"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-arm64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.27.4.tgz",
      "integrity": "sha512-Z9SExBg2y32smoDQdf1HRwHRt6vAHLXcxD2uGgO/v2jK7Y718Ix4ndsbNMU/+1Qiem9OiOdaqitioZwxivhXYg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-ia32": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.27.4.tgz",
      "integrity": "sha512-DAyGLS0Jz5G5iixEbMHi5KdiApqHBWMGzTtMiJ72ZOLhbu/bzxgAe8Ue8CTS3n3HbIUHQz/L51yMdGMeoxXNJw==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@esbuild/win32-x64": {
      "version": "0.27.4",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.27.4.tgz",
      "integrity": "sha512-+knoa0BDoeXgkNvvV1vvbZX4+hizelrkwmGJBdT17t8FNPwG2lKemmuMZlmaNQ3ws3DKKCxpb4zRZEIp3UxFCg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@rollup/rollup-android-arm-eabi": {
      "version": "4.59.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm-eabi/-/rollup-android-arm-eabi-4.59.0.tgz",
      "integrity": "sha512-upnNBkA6ZH2VKGcBj9Fyl9IGNPULcjXRlg0LLeaioQWueH30p6IXtJEbKAgvyv+mJaMxSm1l6xwDXYjpEMiLMg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-android-arm64": {
      "version": "4.59.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-android-arm64/-/rollup-android-arm64-4.59.0.tgz",
      "integrity": "sha512-hZ+Zxj3SySm4A/DylsDKZAeVg0mvi++0PYVceVyX7hemkw7OreKdCvW2oQ3T1FMZvCaQXqOTHb8qmBShoqk69Q==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ]
    },
    "node_modules/@rollup/rollup-darwin-arm64": {
      "version": "4.59.0",
      "resolved": "https://registry.npmjs.org/@rollup/rollup-darwin-arm64/-/rollup-darwin-arm64-4.59.0.tgz",
      "integrity": "sha512-W2Psnbh1J8ZJw0xKAd8zdNgF9HRLkdWwwdWqubSVk0pUuQkoHnv7rx4GiF9rT4t5DIZGAsConRE3AxCdJ4m8rg==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ]
    },
    "node_module
... [TRUNCATED]
```

### File: cli\tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "dist",
    "rootDir": "src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "declaration": true,
    "sourceMap": true
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules", "dist"]
}

```

### File: commands\bump-version.ps1
```ps1
#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Automated version bumping script for Unity Package project

.DESCRIPTION
    Updates version numbers across all project files automatically to prevent human errors.
    Supports preview mode for safe testing.

.PARAMETER NewVersion
    The new version number in semver format (e.g., "0.18.0")

.PARAMETER WhatIf
    Preview changes without applying them

.EXAMPLE
    .\bump-version.ps1 -NewVersion "0.18.0"

.EXAMPLE
    .\bump-version.ps1 -NewVersion "0.18.0" -WhatIf
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$NewVersion,

    [switch]$WhatIf
)

# Set location to repository root (parent of commands folder)
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptDir
Push-Location $repoRoot

# Script configuration
$ErrorActionPreference = "Stop"

# Version file locations (relative to script root)
$VersionFiles = @(
    @{
        Path        = "Unity-Package/Assets/root/package.json"
        Pattern     = '"version":\s*"[\d\.]+"'
        Replace     = '"version": "{VERSION}"'
        Description = "Unity package version"
    },
    @{
        Path        = "Installer/Assets/YOUR_PACKAGE_NAME_INSTALLER/Installer.cs"
        Pattern     = 'public const string Version = "[\d\.]+";'
        Replace     = 'public const string Version = "{VERSION}";'
        Description = "Installer C# version constant"
    },
    @{
        Path        = "Unity-Package/Assets/root/README.md"
        Pattern     = "https://github\.com/YOUR_GITHUB_USERNAME_REPOSITORY/releases/download/[\d\.]+/YOUR_PACKAGE_NAME_INSTALLER_FILE\.unitypackage"
        Replace     = "https://github.com/YOUR_GITHUB_USERNAME_REPOSITORY/releases/download/{VERSION}/YOUR_PACKAGE_NAME_INSTALLER_FILE.unitypackage"
        Description = "Package README download URL"
    },
    @{
        Path        = "README.md"
        Pattern     = "https://github\.com/YOUR_GITHUB_USERNAME_REPOSITORY/releases/download/[\d\.]+/YOUR_PACKAGE_NAME_INSTALLER_FILE\.unitypackage"
        Replace     = "https://github.com/YOUR_GITHUB_USERNAME_REPOSITORY/releases/download/{VERSION}/YOUR_PACKAGE_NAME_INSTALLER_FILE.unitypackage"
        Description = "Repository README download URL"
    }
)

function Write-ColorText {
    param([string]$Text, [string]$Color = "White")
    Write-Host $Text -ForegroundColor $Color
}

function Test-SemanticVersion {
    param([string]$Version)

    if ([string]::IsNullOrWhiteSpace($Version)) {
        return $false
    }

    # Basic semver pattern: major.minor.patch (with optional prerelease/build)
    $pattern = '^\d+\.\d+\.\d+(-[a-zA-Z0-9\-\.]+)?(\+[a-zA-Z0-9\-\.]+)?$'
    return $Version -match $pattern
}

function Get-CurrentVersion {
    # Extract current version from package.json
    $packageJsonPath = "Unity-Package/Assets/root/package.json"
    if (-not (Test-Path $packageJsonPath)) {
        throw "Could not find package.json at: $packageJsonPath"
    }

    $content = Get-Content $packageJsonPath -Raw
    if ($content -match '"version":\s*"([\d\.]+)"') {
        return $Matches[1]
    }

    throw "Could not extract current version from package.json"
}

function Update-VersionFiles {
    param([string]$OldVersion, [string]$NewVersion, [bool]$PreviewOnly = $false)

    $changes = @()

    foreach ($file in $VersionFiles) {
        $fullPath = $file.Path

        if (-not (Test-Path $fullPath)) {
            Write-ColorText "⚠️  File not found: $($file.Path)" "Yellow"
            continue
        }

        $content = Get-Content $fullPath -Raw
        $originalContent = $content

        # Create the replacement string
        $replacement = $file.Replace -replace '\{VERSION\}', $NewVersion

        # Apply the replacement
        $newContent = $content -replace $file.Pattern, $replacement

        # Check if any changes were made
        if ($originalContent -ne $newContent) {
            # Count matches for reporting
            $regexMatches = [regex]::Matches($originalContent, $file.Pattern)

            $changes += @{
                Path            = $file.Path
                Description     = $file.Description
                Matches         = $regexMatches.Count
                Content         = $newContent
                OriginalContent = $originalContent
            }

            Write-ColorText "📝 $($file.Description): $($regexMatches.Count) occurrence(s)" "Green"

            # Show the actual changes
            foreach ($match in $regexMatches) {
                $newValue = $match.Value -replace $file.Pattern, $replacement
                Write-ColorText "   $($match.Value) → $newValue" "Gray"
            }
        }
        else {
            Write-ColorText "⚠️  No matches found in: $($file.Path)" "Yellow"
            Write-ColorText "   Pattern: $($file.Pattern)" "Gray"
        }
    }

    if ($changes.Count -eq 0) {
        Write-ColorText "❌ No version references found to update!" "Red"
        Pop-Location
        exit 1
    }

    if ($PreviewOnly) {
        Write-ColorText "`n📋 Preview Summary:" "Cyan"
        Write-ColorText "Files to be modified: $($changes.Count)" "White"
        Write-ColorText "Total replacements: $(($changes | Measure-Object -Property Matches -Sum).Sum)" "White"
        return $null
    }

    # Apply changes
    foreach ($change in $changes) {
        $fullPath = $change.Path
        Set-Content -Path $fullPath -Value $change.Content -NoNewline
    }

    return $changes
}

# Main execution
try {
    Write-ColorText "🚀 Package Version Bump Script" "Cyan"
    Write-ColorText "=================================" "Cyan"

    # Validate semantic version format
    if (-not (Test-SemanticVersion $NewVersion)) {
        Write-ColorText "❌ Invalid semantic version format: $NewVersion" "Red"
        Write-ColorText "Expected format: major.minor.patch (e.g., '1.2.3')" "Yellow"
        Pop-Location
        exit 1
    }

    # Get current version
    $currentVersion = Get-CurrentVersion
    Write-ColorText "📋 Current version: $currentVersion" "White"
    Write-ColorText "📋 New version: $NewVersion" "White"

    if ($currentVersion -eq $NewVersion) {
        Write-ColorText "⚠️  New version is the same as current version" "Yellow"
        Pop-Location
        exit 0
    }

    Write-ColorText "`n🔍 Scanning for version references..." "Cyan"

    # Update version files
    $changes = Update-VersionFiles -OldVersion $currentVersion -NewVersion $NewVersion -PreviewOnly $WhatIf

    if ($WhatIf) {
        Write-ColorText "`n✅ Preview completed. Use without -WhatIf to apply changes." "Green"
        Pop-Location
        exit 0
    }

    if ($changes -and $changes.Count -gt 0) {
        Write-ColorText "`n🎉 Version bump completed successfully!" "Green"
        Write-ColorText "   Updated $($changes.Count) files" "White"
        Write-ColorText "   Total replacements: $(($changes | Measure-Object -Property Matches -Sum).Sum)" "White"
        Write-ColorText "   Version: $currentVersion → $NewVersion" "White"
        Write-ColorText "`n💡 Remember to commit these changes to git" "Cyan"
    }

    Pop-Location
}
catch {
    Write-ColorText "`n❌ Script failed: $($_.Exception.Message)" "Red"
    Pop-Location
    exit 1
}
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

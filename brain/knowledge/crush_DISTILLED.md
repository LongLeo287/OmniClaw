---
id: crush
type: knowledge
owner: OA_Triage
---
# crush
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Crush

<p align="center">
    <a href="https://stuff.charm.sh/crush/charm-crush.png"><img width="450" alt="Charm Crush Logo" src="https://github.com/user-attachments/assets/cf8ca3ce-8b02-43f0-9d0f-5a331488da4b" /></a><br />
    <a href="https://github.com/charmbracelet/crush/releases"><img src="https://img.shields.io/github/release/charmbracelet/crush" alt="Latest Release"></a>
    <a href="https://github.com/charmbracelet/crush/actions"><img src="https://github.com/charmbracelet/crush/actions/workflows/build.yml/badge.svg" alt="Build Status"></a>
</p>

<p align="center">Your new coding bestie, now available in your favourite terminal.<br />Your tools, your code, and your workflows, wired into your LLM of choice.</p>
<p align="center">终端里的编程新搭档，<br />无缝接入你的工具、代码与工作流，全面兼容主流 LLM 模型。</p>

<p align="center"><img width="800" alt="Crush Demo" src="https://github.com/user-attachments/assets/58280caf-851b-470a-b6f7-d5c4ea8a1968" /></p>

## Features

- **Multi-Model:** choose from a wide range of LLMs or add your own via OpenAI- or Anthropic-compatible APIs
- **Flexible:** switch LLMs mid-session while preserving context
- **Session-Based:** maintain multiple work sessions and contexts per project
- **LSP-Enhanced:** Crush uses LSPs for additional context, just like you do
- **Extensible:** add capabilities via MCPs (`http`, `stdio`, and `sse`)
- **Works Everywhere:** first-class support in every terminal on macOS, Linux, Windows (PowerShell and WSL), Android, FreeBSD, OpenBSD, and NetBSD
- **Industrial Grade:** built on the Charm ecosystem, powering 25k+ applications, from leading open source projects to business-critical infrastructure

## Installation

Use a package manager:

```bash
# Homebrew
brew install charmbracelet/tap/crush

# NPM
npm install -g @charmland/crush

# Arch Linux (btw)
yay -S crush-bin

# Nix
nix run github:numtide/nix-ai-tools#crush

# FreeBSD
pkg install crush
```

Windows users:

```bash
# Winget
winget install charmbracelet.crush

# Scoop
scoop bucket add charm https://github.com/charmbracelet/scoop-bucket.git
scoop install crush
```

<details>
<summary><strong>Nix (NUR)</strong></summary>

Crush is available via the official Charm [NUR](https://github.com/nix-community/NUR) in `nur.repos.charmbracelet.crush`, which is the most up-to-date way to get Crush in Nix.

You can also try out Crush via the NUR with `nix-shell`:

```bash
# Add the NUR channel.
nix-channel --add https://github.com/nix-community/NUR/archive/main.tar.gz nur
nix-channel --update

# Get Crush in a Nix shell.
nix-shell -p '(import <nur> { pkgs = import <nixpkgs> {}; }).repos.charmbracelet.crush'
```

### NixOS & Home Manager Module Usage via NUR

Crush provides NixOS and Home Manager modules via NUR.
You can use these modules directly in your flake by importing them from NUR. Since it auto detects whether its a home manager or nixos context you can use the import the exact same way :)

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    nur.url = "github:nix-community/NUR";
  };

  outputs = { self, nixpkgs, nur, ... }: {
    nixosConfigurations.your-hostname = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        nur.modules.nixos.default
        nur.repos.charmbracelet.modules.crush
        {
          programs.crush = {
            enable = true;
            settings = {
              providers = {
                openai = {
                  id = "openai";
                  name = "OpenAI";
                  base_url = "https://api.openai.com/v1";
                  type = "openai";
                  api_key = "sk-fake123456789abcdef...";
                  models = [
                    {
                      id = "gpt-4";
                      name = "GPT-4";
                    }
                  ];
                };
              };
              lsp = {
                go = { command = "gopls"; enabled = true; };
                nix = { command = "nil"; enabled = true; };
              };
              options = {
                context_paths = [ "/etc/nixos/configuration.nix" ];
                tui = { compact_mode = true; };
                debug = false;
              };
            };
          };
        }
      ];
    };
  };
}
```

</details>

<details>
<summary><strong>Debian/Ubuntu</strong></summary>

```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://repo.charm.sh/apt/gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/charm.gpg
echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" | sudo tee /etc/apt/sources.list.d/charm.list
sudo apt update && sudo apt install crush
```

</details>

<details>
<summary><strong>Fedora/RHEL</strong></summary>

```bash
echo '[charm]
name=Charm
baseurl=https://repo.charm.sh/yum/
enabled=1
gpgcheck=1
gpgkey=https://repo.charm.sh/yum/gpg.key' | sudo tee /etc/yum.repos.d/charm.repo
sudo yum install crush
```

</details>

Or, download it:

- [Packages][releases] are available in Debian and RPM formats
- [Binaries][releases] are available for Linux, macOS, Windows, FreeBSD, OpenBSD, and NetBSD

[releases]: https://github.com/charmbracelet/crush/releases

Or just install it with Go:

```
go install github.com/charmbracelet/crush@latest
```

> [!WARNING]
> Productivity may increase when using Crush and you may find yourself nerd
> sniped when first using the application. If the symptoms persist, join the
> [Discord][discord] and nerd snipe the rest of us.

## Getting Started

The quickest way to get started is to grab an API key for your preferred
provider such as Anthropic, OpenAI, Groq, OpenRouter, or Vercel AI Gateway and just start
Crush. You'll be prompted to enter your API key.

That said, you can also set environment variables for preferred providers.

| Environment Variable        | Provider                                           |
| --------------------------- | -------------------------------------------------- |
| `ANTHROPIC_API_KEY`         | Anthropic                                          |
| `OPENAI_API_KEY`            | OpenAI                                             |
| `VERCEL_API_KEY`            | Vercel AI Gateway                                  |
| `GEMINI_API_KEY`            | Google Gemini                                      |
| `SYNTHETIC_API_KEY`         | Synthetic                                          |
| `ZAI_API_KEY`               | Z.ai                                               |
| `MINIMAX_API_KEY`           | MiniMax                                            |
| `HF_TOKEN`                  | Hugging Face Inference                             |
| `CEREBRAS_API_KEY`          | Cerebras                                           |
| `OPENROUTER_API_KEY`        | OpenRouter                                         |
| `IONET_API_KEY`             | io.net                                             |
| `GROQ_API_KEY`              | Groq                                               |
| `VERTEXAI_PROJECT`          | Google Cloud VertexAI (Gemini)                     |
| `VERTEXAI_LOCATION`         | Google Cloud VertexAI (Gemini)                     |
| `AWS_ACCESS_KEY_ID`         | Amazon Bedrock (Claude)                            |
| `AWS_SECRET_ACCESS_KEY`     | Amazon Bedrock (Claude)                            |
| `AWS_REGION`                | Amazon Bedrock (Claude)                            |
| `AWS_PROFILE`               | Amazon Bedrock (Custom Profile)                    |
| `AWS_BEARER_TOKEN_BEDROCK`  | Amazon Bedrock                                     |
| `AZURE_OPENAI_API_ENDPOINT` | Azure OpenAI models                                |
| `AZURE_OPENAI_API_KEY`      | Azure OpenAI models (optional when using Entra ID) |
| `AZURE_OPENAI_API_VERSION`  | Azure OpenAI models                                |

### Subscriptions

If you prefer subscription-based usage, here are some plans that work well in
Crush:

- [Synthetic](https://synthetic.new/pricing)
- [GLM Coding Plan](https://z.ai/subscribe)
- [Kimi Code](https://www.kimi.com/membership/pricing)
- [MiniMax Coding Plan](https://platform.minimax.io/subscribe/coding-plan)

### By the Way

Is there a provider you’d like to see in Crush? Is there an existing model that needs an update?

Crush’s default model listing is managed in [Catwalk](https://github.com/charmbracelet/catwalk), a community-supported, open source repository of Crush-compatible models, and you’re welcome to contribute.

<a href="https://github.com/charmbracelet/catwalk"><img width="174" height="174" alt="Catwalk Badge" src="https://github.com/user-attachments/assets/95b49515-fe82-4409-b10d-5beb0873787d" /></a>

## Configuration

> [!TIP]
> Crush ships with a builtin `crush-config` skill for configuring itself. In
> many cases you can simply ask Crush to configure itself.

Crush runs great with no configuration. That said, if you do need or want to
customize Crush, configuration can be added either local to the project itself,
or globally, with the following priority:

1. `.crush.json`
2. `crush.json`
3. `$HOME/.config/crush/crush.json`

Configuration itself is stored as a JSON object:

```json
{
  "this-setting": { "this": "that" },
  "that-setting": ["ceci", "cela"]
}
```

As an additional note, Crush also stores ephemeral data, such as application
state, in one additional location:

```bash
# Unix
$HOME/.local/share/crush/crush.json

# Windows
%LOCALAPPDATA%\crush\crush.json
```

> [!TIP]
> You can override the user and data config locations by setting:
>
> - `CRUSH_GLOBAL_CONFIG`
> - `CRUSH_GLOBAL_DATA`

### LSPs

Crush can use LSPs for additional context to help inform its decisions, just
like you would. LSPs can be added manually like so:

```json
{
  "$schema": "https://charm.land/crush.json",
  "lsp": {
    "go": {
      "command": "gopls",
      "env": {
        "GOTOOLCHAIN": "go1.24.5"
      }
    },
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"]
    },
    "nix": {
      "command": "nil"
    }
  }
}
```

### MCPs

Crush also supports Model Context Protocol (MCP) servers through three
transport types: `stdio` for command-line servers, `http` for HTTP endpoints,
and `sse` for Server-Sent Events. Environment variable expansion is supported
using `$(echo $VAR)` syntax.

```json
{
  "$schema": "https://charm.land/crush.json",
  "mcp": {
    "filesystem": {
      "type": "stdio",
      "command": "node",
      "args": ["/path/to/mcp-server.js"],
      "timeout": 120,
      "disabled": false,
      "disabled_tools": ["some-tool-name"],
      "env": {
        "NODE_ENV": "production"
      }
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "timeout": 120,
      "disabled": false,
      "disabled_tools": ["create_issue", "create_pull_request"],
      "headers": {
        "Authorization": "Bearer $GH_PAT"
      }
    },
    "streaming-service": {
      "type": "sse",
      "url": "https://example.com/mcp/sse",
      "timeout": 120,
      "disabled": false,
      "headers": {
        "API-Key": "$(echo $API_KEY)"
      }
    }
  }
}
```

### Ignoring Files

Crush respects `.gitignore` files by default, but you can also create a
`.crushignore` file to specify additional files and directories that Crush
should ignore. This is useful for excluding files that you want in version
control but don't want Crush to consider when providing context.

The `.crushignore` file uses the same syntax as `.gitignore` and can be placed
in the root of your project or in subdirectories.

### Allowing Tools

By default, Crush will ask you for permission before running tool calls. If
you'd like, you can allow tools to be executed without prompting you for
permissions. Use this with care.

```json
{
  "$schema": "https://charm.land/crush.json",
  "permissions": {
    "allowed_tools": [
      "view",
      "ls",
      "grep",
      "edit",
      "mcp_context7_get-library-doc"
    ]
  }
}
```

You can also skip all permission prompts entirely by running Crush with the
`--yolo` flag. Be very, very careful with this feature.

### Disabling Built-In Tools

If you'd like to prevent Crush from using certain built-in tools entirely, you
can disable them via the `options.disabled_tools` list. Disabled tools are
completely hidden from the agent.

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "disabled_tools": ["bash", "sourcegraph"]
  }
}
```

To disable tools from MCP servers, see the [MCP config section](#mcps).

### Disabling Skills

If you'd like to prevent Crush from using certain skills entirely, you can
disable them via the `options.disabled_skills` list. Disabled skills are hidden
from the agent, including builtin skills and skills discovered from disk.

```json
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "disabled_skills": ["crush-config"]
  }
}
```

### Agent Skills

Crush supports the [Agent Skills](https://agentskills.io) open standard for
extending agent capabilities with reusable skill packages. Skills are folders
containing a `SKILL.md` file with instructions that Crush can discover and
activate on demand.

The global paths we looks for skills are:

* `$CRUSH_SKILLS_DIR`
* `$XDG_CONFIG_HOME/agents/skills` or `~/.config/agents/skills/`
* `$XDG_CONFIG_HOME/crush/skills` or `~/.config/crush/skills/`
* On Windows, we _also_ look at
  * `%LOCALAPPDATA%\agents\skills\` or `%USERPROFILE%\AppData\Local\agents\skills\`
  * `%LOCALAPPDATA%\crush\skills\` or `%USERPROFILE%\AppData\Local\crush\skills\`
* Additional paths configured via `options.skills_paths`

On top of that, we _also_ load skills in your project from the following
relative paths:

* `.agents/skills`
* `.crush/skills`
* `.claude/skills`
* `.cursor/skills`

```jsonc
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "skills_paths": [
      "~/.config/crush/skills", // Windows: "%LOCALAPPDATA%\\crush\\skills",
      "./project-skills",
    ],
  },
}
```

You can get started with example skills from [anthropics/skills](https://github.com/anthropics/skills):

```bash
# Unix
mkdir -p ~/.config/crush/skills
cd ~/.config/crush/skills
git clone https://github.com/anthropics/skills.git _temp
mv _temp/skills/* . && rm -rf _temp
```

```powershell
# Windows (PowerShell)
mkdir -Force "$env:LOCALAPPDATA\crush\skills"
cd "$env:LOCALAPPDATA\crush\skills"
git clone https://github.com/anthropics/skills.git _temp
mv _temp/skills/* . ; rm -r -force _temp
```

### Desktop notifications

Crush sends desktop notifications when a tool call requires permission and when
the agent finishes its turn. They're only sent when the terminal window isn't
focused _and_ your terminal supports reporting the focus state.

```jsonc
{
  "$schema": "https://charm.land/crush.json",
  "options": {
    "disable_notifications": false, // default
  },
}
```

To disable desktop notifications, set `disable_notifications` to `true` in your
configuration. On macO
... [TRUNCATED]
```

### File: AGENTS.md
```md
# Crush Development Guide

## Project Overview

Crush is a terminal-based AI coding assistant built in Go by
[Charm](https://charm.land). It connects to LLMs and gives them tools to read,
write, and execute code. It supports multiple providers (Anthropic, OpenAI,
Gemini, Bedrock, Copilot, Hyper, MiniMax, Vercel, and more), integrates with
LSPs for code intelligence, and supports extensibility via MCP servers and
agent skills.

The module path is `github.com/charmbracelet/crush`.

## Architecture

```
main.go                            CLI entry point (cobra via internal/cmd)
internal/
  app/app.go                       Top-level wiring: DB, config, agents, LSP, MCP, events
  cmd/                             CLI commands (root, run, login, models, stats, sessions)
  config/
    config.go                      Config struct, context file paths, agent definitions
    load.go                        crush.json loading and validation
    provider.go                    Provider configuration and model resolution
  agent/
    agent.go                       SessionAgent: runs LLM conversations per session
    coordinator.go                 Coordinator: manages named agents ("coder", "task")
    prompts.go                     Loads Go-template system prompts
    templates/                     System prompt templates (coder.md.tpl, task.md.tpl, etc.)
    tools/                         All built-in tools (bash, edit, view, grep, glob, etc.)
      mcp/                         MCP client integration
  session/session.go               Session CRUD backed by SQLite
  message/                         Message model and content types
  db/                              SQLite via sqlc, with migrations
    sql/                           Raw SQL queries (consumed by sqlc)
    migrations/                    Schema migrations
  lsp/                             LSP client manager, auto-discovery, on-demand startup
  ui/                              Bubble Tea v2 TUI (see internal/ui/AGENTS.md)
  permission/                      Tool permission checking and allow-lists
  skills/                          Skill file discovery and loading
  shell/                           Bash command execution with background job support
  event/                           Telemetry (PostHog)
  pubsub/                          Internal pub/sub for cross-component messaging
  filetracker/                     Tracks files touched per session
  history/                         Prompt history
```

### Key Dependency Roles

- **`charm.land/fantasy`**: LLM provider abstraction layer. Handles protocol
  differences between Anthropic, OpenAI, Gemini, etc. Used in `internal/app`
  and `internal/agent`.
- **`charm.land/bubbletea/v2`**: TUI framework powering the interactive UI.
- **`charm.land/lipgloss/v2`**: Terminal styling.
- **`charm.land/glamour/v2`**: Markdown rendering in the terminal.
- **`charm.land/catwalk`**: Snapshot/golden-file testing for TUI components.
- **`sqlc`**: Generates Go code from SQL queries in `internal/db/sql/`.

### Key Patterns

- **Config is a Service**: accessed via `config.Service`, not global state.
- **Tools are self-documenting**: each tool has a `.go` implementation and a
  `.md` description file in `internal/agent/tools/`.
- **System prompts are Go templates**: `internal/agent/templates/*.md.tpl`
  with runtime data injected.
- **Context files**: Crush reads AGENTS.md, CRUSH.md, CLAUDE.md, GEMINI.md
  (and `.local` variants) from the working directory for project-specific
  instructions.
- **Persistence**: SQLite + sqlc. All queries live in `internal/db/sql/`,
  generated code in `internal/db/`. Migrations in `internal/db/migrations/`.
- **Pub/sub**: `internal/pubsub` for decoupled communication between agent,
  UI, and services.
- **CGO disabled**: builds with `CGO_ENABLED=0` and
  `GOEXPERIMENT=greenteagc`.

## Build/Test/Lint Commands

- **Build**: `go build .` or `go run .`
- **Test**: `task test` or `go test ./...` (run single test:
  `go test ./internal/llm/prompt -run TestGetContextFromPaths`)
- **Update Golden Files**: `go test ./... -update` (regenerates `.golden`
  files when test output changes)
  - Update specific package:
    `go test ./internal/tui/components/core -update` (in this case,
    we're updating "core")
- **Lint**: `task lint:fix`
- **Format**: `task fmt` (`gofumpt -w .`)
- **Modernize**: `task modernize` (runs `modernize` which makes code
  simplifications)
- **Dev**: `task dev` (runs with profiling enabled)

## Code Style Guidelines

- **Imports**: Use `goimports` formatting, group stdlib, external, internal
  packages.
- **Formatting**: Use gofumpt (stricter than gofmt), enabled in
  golangci-lint.
- **Naming**: Standard Go conventions — PascalCase for exported, camelCase
  for unexported.
- **Types**: Prefer explicit types, use type aliases for clarity (e.g.,
  `type AgentName string`).
- **Error handling**: Return errors explicitly, use `fmt.Errorf` for
  wrapping.
- **Context**: Always pass `context.Context` as first parameter for
  operations.
- **Interfaces**: Define interfaces in consuming packages, keep them small
  and focused.
- **Structs**: Use struct embedding for composition, group related fields.
- **Constants**: Use typed constants with iota for enums, group in const
  blocks.
- **Testing**: Use testify's `require` package, parallel tests with
  `t.Parallel()`, `t.SetEnv()` to set environment variables. Always use
  `t.Tempdir()` when in need of a temporary directory. This directory does
  not need to be removed.
- **JSON tags**: Use snake_case for JSON field names.
- **File permissions**: Use octal notation (0o755, 0o644) for file
  permissions.
- **Log messages**: Log messages must start with a capital letter (e.g.,
  "Failed to save session" not "failed to save session").
  - This is enforced by `task lint:log` which runs as part of `task lint`.
- **Comments**: End comments in periods unless comments are at the end of the
  line.

## Testing with Mock Providers

When writing tests that involve provider configurations, use the mock
providers to avoid API calls:

```go
func TestYourFunction(t *testing.T) {
    // Enable mock providers for testing
    originalUseMock := config.UseMockProviders
    config.UseMockProviders = true
    defer func() {
        config.UseMockProviders = originalUseMock
        config.ResetProviders()
    }()

    // Reset providers to ensure fresh mock data
    config.ResetProviders()

    // Your test code here - providers will now return mock data
    providers := config.Providers()
    // ... test logic
}
```

## Formatting

- ALWAYS format any Go code you write.
  - First, try `gofumpt -w .`.
  - If `gofumpt` is not available, use `goimports`.
  - If `goimports` is not available, use `gofmt`.
  - You can also use `task fmt` to run `gofumpt -w .` on the entire project,
    as long as `gofumpt` is on the `PATH`.

## Comments

- Comments that live on their own lines should start with capital letters and
  end with periods. Wrap comments at 78 columns.

## Committing

- ALWAYS use semantic commits (`fix:`, `feat:`, `chore:`, `refactor:`,
  `docs:`, `sec:`, etc).
- Try to keep commits to one line, not including your attribution. Only use
  multi-line commits when additional context is truly necessary.

## Working on the TUI (UI)

Anytime you need to work on the TUI, read `internal/ui/AGENTS.md` before
starting work.

```

### File: CLA.md
```md
# Contributor License Agreement

Thank you for your interest in the open source project(s) managed by Charmbracelet, Inc. ("Company"). In order to clarify the intellectual property license granted with Contributions from any person or entity, Company must have a Contributor License Agreement ("CLA") on file that has been signed by each contributor, indicating agreement to the license terms below. This license is for your protection as a contributor as well as the protection of Company and its other contributors and users; it does not change your rights to use your own Contributions for any other purpose.
By submitting a contribution to this repository (e.g. opening a pull request) or otherwise agreeing in writing, You accept and agree to these terms and conditions for Your present and future Contributions submitted to Company. In return, Company shall consider Your Contributions for addition to the official Company open source project(s) for which they were submitted. Except for the license granted herein to Company and recipients of software distributed by Company, You reserve all right, title, and interest in and to Your Contributions.

1. Definitions.
   - "You" (or "Your") shall mean the copyright owner or legal entity authorized by the copyright owner that is entering into this CLA with Company. For legal entities, the entity making a Contribution and all other entities that control, are controlled by, or are under common control with that entity are considered to be a single Contributor. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.
   - "Contribution" shall mean any code, documentation or other original works of authorship, including any modifications or additions to an existing work, that are intentionally submitted by You to Company for inclusion in, or documentation of, any of the products owned or managed by Company (the "Work"). For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to Company or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, Company for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by You as "Not a Contribution."
2. Grant of Copyright License. Subject to the terms and conditions of this CLA, You hereby grant to Company and to recipients of software distributed by Company a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare derivative works of, publicly display, publicly perform, sublicense, and distribute Your Contributions and such derivative works.
3. Grant of Patent License. Subject to the terms and conditions of this CLA, You hereby grant to Company and to recipients of software distributed by Company a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by You that are necessarily infringed by Your Contribution(s) alone or by combination of Your Contribution(s) with the Work to which such Contribution(s) were submitted. If any entity institutes patent litigation against You or any other entity (including a cross-claim or counterclaim in a lawsuit) alleging that Your Contribution, or the Work to which You have contributed, constitutes direct or contributory patent infringement, then any patent licenses granted to that entity under this CLA for that Contribution or Work shall terminate as of the date such litigation is filed.
4. You represent and warrant that You are legally entitled to grant the above license. If You are an individual and Your employer(s) has rights to intellectual property that You create that includes Your Contributions, You represent that You have received permission to make Contributions on behalf of that employer, that Your employer has waived such rights for Your Contributions to Company, or that Your employer has entered into a separate CLA with Company covering Your Contributions. If You are a company, You represent further that each employee making a Contribution to Company under the company’s name is authorized to submit Contributions on behalf of the company.
5. You represent and warrant that each of Your Contributions is Your original creation (see section 7 for submissions on behalf of others). You represent and warrant that, to Your knowledge, none of Your Contributions infringe, violate, or misappropriate any third party intellectual property or other proprietary rights.
6. You are not expected to provide support for Your Contributions, except to the extent You desire to provide support. You may provide support for free, for a fee, or not at all. Unless required by applicable law or agreed to in writing, except for the warranties set forth above, You provide Your Contributions on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.
7. Should You wish to submit work that is not Your original creation, You may submit it to Company separately from any Contribution, identifying the complete details of its source and of any license or other restriction (including, but not limited to, related patents, trademarks, and license agreements) of which You are personally aware, and conspicuously marking the work as "Submitted on behalf of a third-party: [named here]".
8. You agree to notify Company of any facts or circumstances of which You become aware that would make the above representations and warranties inaccurate in any respect.
9. If You are entering into this CLA as a company, You represent and warrant that the individual accepting this CLA is duly authorized to enter into this CLA on the company’s behalf.

For any copyright notices or other communications, please contact us at [vt100@charm.land](mailto:vt100@charm.land).

```

### File: crush.json
```json
{
  "$schema": "https://charm.land/crush.json",
  "lsp": {
    "gopls": {
      "options": {
        "gofumpt": true,
        "codelenses": {
          "gc_details": true,
          "generate": true,
          "run_govulncheck": true,
          "test": true,
          "tidy": true,
          "upgrade_dependency": true
        },
        "hints": {
          "assignVariableTypes": true,
          "compositeLiteralFields": true,
          "compositeLiteralTypes": true,
          "constantValues": true,
          "functionTypeParameters": true,
          "parameterNames": true,
          "rangeVariableTypes": true
        },
        "analyses": {
          "nilness": true,
          "unusedparams": true,
          "unusedvariable": true,
          "unusedwrite": true,
          "useany": true
        },
        "staticcheck": true,
        "directoryFilters": [
          "-.git",
          "-node_modules"
        ],
        "semanticTokens": true
      }
    }
  }
}

```

### File: LICENSE.md
```md
# Functional Source License, Version 1.1, MIT Future License

## Abbreviation

FSL-1.1-MIT

## Notice

Copyright 2025-2026 Charmbracelet, Inc.

## Terms and Conditions

### Licensor ("We")

The party offering the Software under these Terms and Conditions.

### The Software

The "Software" is each version of the software that we make available under
these Terms and Conditions, as indicated by our inclusion of these Terms and
Conditions with the Software.

### License Grant

Subject to your compliance with this License Grant and the Patents,
Redistribution and Trademark clauses below, we hereby grant you the right to
use, copy, modify, create derivative works, publicly perform, publicly display
and redistribute the Software for any Permitted Purpose identified below.

### Permitted Purpose

A Permitted Purpose is any purpose other than a Competing Use. A Competing Use
means making the Software available to others in a commercial product or
service that:

1. substitutes for the Software;

2. substitutes for any other product or service we offer using the Software
   that exists as of the date we make the Software available; or

3. offers the same or substantially similar functionality as the Software.

Permitted Purposes specifically include using the Software:

1. for your internal use and access;

2. for non-commercial education;

3. for non-commercial research; and

4. in connection with professional services that you provide to a licensee
   using the Software in accordance with these Terms and Conditions.

### Patents

To the extent your use for a Permitted Purpose would necessarily infringe our
patents, the license grant above includes a license under our patents. If you
make a claim against any party that the Software infringes or contributes to
the infringement of any patent, then your patent license to the Software ends
immediately.

### Redistribution

The Terms and Conditions apply to all copies, modifications and derivatives of
the Software.

If you redistribute any copies, modifications or derivatives of the Software,
you must include a copy of or a link to these Terms and Conditions and not
remove any copyright notices provided in or with the Software.

### Disclaimer

THE SOFTWARE IS PROVIDED "AS IS" AND WITHOUT WARRANTIES OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING WITHOUT LIMITATION WARRANTIES OF FITNESS FOR A PARTICULAR
PURPOSE, MERCHANTABILITY, TITLE OR NON-INFRINGEMENT.

IN NO EVENT WILL WE HAVE ANY LIABILITY TO YOU ARISING OUT OF OR RELATED TO THE
SOFTWARE, INCLUDING INDIRECT, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES,
EVEN IF WE HAVE BEEN INFORMED OF THEIR POSSIBILITY IN ADVANCE.

### Trademarks

Except for displaying the License Details and identifying us as the origin of
the Software, you have no right under these Terms and Conditions to use our
trademarks, trade names, service marks or product names.

## Grant of Future License

We hereby irrevocably grant you an additional license to use the Software under
the MIT license that is effective on the second anniversary of the date we make
the Software available. On or after that date, you may use the Software under
the MIT license, in which case the following will apply:

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

MIT License

Copyright (c) 2025-03-21 - 2025-05-30 Kujtim Hoxha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

### File: main.go
```go
// Package main is the entry point for the Crush CLI.
//
//	@title			Crush API
//	@version		1.0
//	@description	Crush is a terminal-based AI coding assistant. This API is served over a Unix socket (or Windows named pipe) and provides programmatic access to workspaces, sessions, agents, LSP, MCP, and more.
//	@contact.name	Charm
//	@contact.url	https://charm.sh
//	@license.name	MIT
//	@license.url	https://github.com/charmbracelet/crush/blob/main/LICENSE
//	@BasePath		/v1
package main

import (
	"log/slog"
	"net/http"
	_ "net/http/pprof"
	"os"

	"github.com/charmbracelet/crush/internal/cmd"
	_ "github.com/joho/godotenv/autoload"
)

func main() {
	if os.Getenv("CRUSH_PROFILE") != "" {
		go func() {
			slog.Info("Serving pprof at localhost:6060")
			if httpErr := http.ListenAndServe("localhost:6060", nil); httpErr != nil {
				slog.Error("Failed to pprof listen", "error", httpErr)
			}
		}()
	}

	cmd.Execute()
}

```

### File: schema.json
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/charmbracelet/crush/internal/config/config",
  "$ref": "#/$defs/Config",
  "$defs": {
    "Attribution": {
      "properties": {
        "trailer_style": {
          "type": "string",
          "enum": [
            "none",
            "co-authored-by",
            "assisted-by"
          ],
          "description": "Style of attribution trailer to add to commits",
          "default": "assisted-by"
        },
        "co_authored_by": {
          "type": "boolean",
          "description": "Deprecated: use trailer_style instead",
          "deprecated": true
        },
        "generated_with": {
          "type": "boolean",
          "description": "Add Generated with Crush line to commit messages and issues and PRs",
          "default": true
        }
      },
      "additionalProperties": false,
      "type": "object"
    },
    "Completions": {
      "properties": {
        "max_depth": {
          "type": "integer",
          "description": "Maximum depth for the ls tool",
          "default": 0,
          "examples": [
            10
          ]
        },
        "max_items": {
          "type": "integer",
          "description": "Maximum number of items to return for the ls tool",
          "default": 1000,
          "examples": [
            100
          ]
        }
      },
      "additionalProperties": false,
      "type": "object"
    },
    "Config": {
      "properties": {
        "$schema": {
          "type": "string"
        },
        "models": {
          "additionalProperties": {
            "$ref": "#/$defs/SelectedModel"
          },
          "type": "object",
          "description": "Model configurations for different model types"
        },
        "providers": {
          "$ref": "#/$defs/Map[string,github.com/charmbracelet/crush/internal/config.ProviderConfig]",
          "description": "AI provider configurations"
        },
        "mcp": {
          "$ref": "#/$defs/MCPs",
          "description": "Model Context Protocol server configurations"
        },
        "lsp": {
          "$ref": "#/$defs/LSPs",
          "description": "Language Server Protocol configurations"
        },
        "options": {
          "$ref": "#/$defs/Options",
          "description": "General application options"
        },
        "permissions": {
          "$ref": "#/$defs/Permissions",
          "description": "Permission settings for tool usage"
        },
        "tools": {
          "$ref": "#/$defs/Tools",
          "description": "Tool configurations"
        }
      },
      "additionalProperties": false,
      "type": "object",
      "required": [
        "tools"
      ]
    },
    "LSPConfig": {
      "properties": {
        "disabled": {
          "type": "boolean",
          "description": "Whether this LSP server is disabled",
          "default": false
        },
        "command": {
          "type": "string",
          "description": "Command to execute for the LSP server",
          "examples": [
            "gopls"
          ]
        },
        "args": {
          "items": {
            "type": "string"
          },
          "type": "array",
          "description": "Arguments to pass to the LSP server command"
        },
        "env": {
          "additionalProperties": {
            "type": "string"
          },
          "type": "object",
          "description": "Environment variables to set to the LSP server command"
        },
        "filetypes": {
          "items": {
            "type": "string",
            "examples": [
              "go",
              "mod",
              "rs",
              "c",
              "js",
              "ts"
            ]
          },
          "type": "array",
          "description": "File types this LSP server handles"
        },
        "root_markers": {
          "items": {
            "type": "string",
            "examples": [
              "go.mod",
              "package.json",
              "Cargo.toml"
            ]
          },
          "type": "array",
          "description": "Files or directories that indicate the project root"
        },
        "init_options": {
          "type": "object",
          "description": "Initialization options passed to the LSP server during initialize request"
        },
        "options": {
          "type": "object",
          "description": "LSP server-specific settings passed during initialization"
        },
        "timeout": {
          "type": "integer",
          "description": "Timeout in seconds for LSP server initialization",
          "default": 30,
          "examples": [
            60,
            120
          ]
        }
      },
      "additionalProperties": false,
      "type": "object"
    },
    "LSPs": {
      "additionalProperties": {
        "$ref": "#/$defs/LSPConfig"
      },
      "type": "object"
    },
    "MCPConfig": {
      "properties": {
        "command": {
          "type": "string",
          "description": "Command to execute for stdio MCP servers",
          "examples": [
            "npx"
          ]
        },
        "env": {
          "additionalProperties": {
            "type": "string"
          },
          "type": "object",
          "description": "Environment variables to set for the MCP server"
        },
        "args": {
          "items": {
            "type": "string"
          },
          "type": "array",
          "description": "Arguments to pass to the MCP server command"
        },
        "type": {
          "type": "string",
          "enum": [
            "stdio",
            "sse",
            "http"
          ],
          "description": "Type of MCP connection",
          "default": "stdio"
        },
        "url": {
          "type": "string",
          "format": "uri",
          "description": "URL for HTTP or SSE MCP servers",
          "examples": [
            "http://localhost:3000/mcp"
          ]
        },
        "disabled": {
          "type": "boolean",
          "description": "Whether this MCP server is disabled",
          "default": false
        },
        "disabled_tools": {
          "items": {
            "type": "string",
            "examples": [
              "get-library-doc"
            ]
          },
          "type": "array",
          "description": "List of tools from this MCP server to disable"
        },
        "timeout": {
          "type": "integer",
          "description": "Timeout in seconds for MCP server connections",
          "default": 15,
          "examples": [
            30,
            60,
            120
          ]
        },
        "headers": {
          "additionalProperties": {
            "type": "string"
          },
          "type": "object",
          "description": "HTTP headers for HTTP/SSE MCP servers"
        }
      },
      "additionalProperties": false,
      "type": "object",
      "required": [
        "type"
      ]
    },
    "MCPs": {
      "additionalProperties": {
        "$ref": "#/$defs/MCPConfig"
      },
      "type": "object"
    },
    "Map[string,github.com/charmbracelet/crush/internal/config.ProviderConfig]": {
      "properties": {},
      "additionalProperties": false,
      "type": "object"
    },
    "Options": {
      "properties": {
        "context_paths": {
          "items": {
            "type": "string",
            "examples": [
              ".cursorrules",
              "CRUSH.md"
            ]
          },
          "type": "array",
          "description": "Paths to files containing context information for the AI"
        },
        "skills_paths": {
          "items": {
            "type": "string",
            "examples": [
              "~/.config/crush/skills",
              "./skills"
            ]
          },
          "type": "array",
          "description": "Paths to directories containing Agent Skills (folders with SKILL.md files)"
        },
        "tui": {
          "$ref": "#/$defs/TUIOptions",
          "description": "Terminal user interface options"
        },
        "debug": {
          "type": "boolean",
          "description": "Enable debug logging",
          "default": false
        },
        "debug_lsp": {
          "type": "boolean",
          "description": "Enable debug logging for LSP servers",
          "default": false
        },
        "disable_auto_summarize": {
          "type": "boolean",
          "description": "Disable automatic conversation summarization",
          "default": false
        },
        "data_directory": {
          "type": "string",
          "description": "Directory for storing application data (relative to working directory)",
          "default": ".crush",
          "examples": [
            ".crush"
          ]
        },
        "disabled_tools": {
          "items": {
            "type": "string",
            "examples": [
              "bash",
              "sourcegraph"
            ]
          },
          "type": "array",
          "description": "List of built-in tools to disable and hide from the agent"
        },
        "disable_provider_auto_update": {
          "type": "boolean",
          "description": "Disable providers auto-update",
          "default": false
        },
        "disable_default_providers": {
          "type": "boolean",
          "description": "Ignore all default/embedded providers. When enabled",
          "default": false
        },
        "attribution": {
          "$ref": "#/$defs/Attribution",
          "description": "Attribution settings for generated content"
        },
        "disable_metrics": {
          "type": "boolean",
          "description": "Disable sending metrics",
          "default": false
        },
        "initialize_as": {
          "type": "string",
          "description": "Name of the context file to create/update during project initialization",
          "default": "AGENTS.md",
          "examples": [
            "AGENTS.md",
            "CRUSH.md",
            "CLAUDE.md",
            "docs/LLMs.md"
          ]
        },
        "auto_lsp": {
          "type": "boolean",
          "description": "Automatically setup LSPs based on root markers",
          "default": true
        },
        "progress": {
          "type": "boolean",
          "description": "Show indeterminate progress updates during long operations",
          "default": true
        },
        "disable_notifications": {
          "type": "boolean",
          "description": "Disable desktop notifications",
          "default": false
        },
        "disabled_skills": {
          "items": {
            "type": "string",
            "examples": [
              "crush-config"
            ]
          },
          "type": "array",
          "description": "List of skill names to disable and hide from the agent"
        }
      },
      "additionalProperties": false,
      "type": "object"
    },
    "Permissions": {
      "properties": {
        "allowed_tools": {
          "items": {
            "type": "string",
            "examples": [
              "bash",
              "view"
            ]
          },
          "type": "array",
          "description": "List of tools that don't require permission prompts"
        }
      },
      "additionalProperties": false,
      "type": "object"
    },
    "SelectedModel": {
      "properties": {
        "model": {
          "type": "string",
          "description": "The model ID as used by the provider API",
          "examples": [
            "gpt-4o"
          ]
        },
        "provider": {
          "type": "string",
          "description": "The model provider ID that matches a key in the providers config",
          "examples": [
            "openai"
          ]
        },
        "reasoning_effort": {
          "type": "string",
          "enum": [
            "low",
            "medium",
            "high"
          ],
          "description": "Reasoning effort level for OpenAI models that support it"
        },
        "think": {
          "type": "boolean",
          "description": "Enable thinking mode for Anthropic models that support reasoning"
        },
        "max_tokens": {
          "type": "integer",
          "maximum": 200000,
          "description": "Maximum number of tokens for model responses",
          "examples": [
            4096
          ]
        },
        "temperature": {
          "type": "number",
          "maximum": 1,
          "minimum": 0,
          "description": "Sampling temperature",
          "examples": [
            0.7
          ]
        },
        "top_p": {
          "type": "number",
          "maximum": 1,
          "minimum": 0,
          "description": "Top-p (nucleus) sampling parameter",
          "examples": [
            0.9
          ]
        },
        "top_k": {
          "type": "integer",
          "description": "Top-k sampling parameter"
        },
        "frequency_penalty": {
          "type": "number",
          "description": "Frequency penalty to reduce repetition"
        },
        "presence_penalty": {
          "type": "number",
          "description": "Presence penalty to increase topic diversity"
        },
        "provider_options": {
          "type": "object",
          "description": "Additional provider-specific options for the model"
        }
      },
      "additionalProperties": false,
      "type": "object",
      "required": [
        "model",
        "provider"
      ]
    },
    "TUIOptions": {
      "properties": {
        "compact_mode": {
          "type": "boolean",
          "description": "Enable compact mode for the TUI interface",
          "default": false
        },
        "diff_mode": {
          "type": "string",
          "enum": [
            "unified",
            "split"
          ],
          "description": "Diff mode for the TUI interface"
        },
        "completions": {
          "$ref": "#/$defs/Completions",
          "description": "Completions UI options"
        },
        "transparent": {
          "type": "boolean",
          "description": "Enable transparent background for the TUI interface",
          "default": false
        }
      },
      "additionalProperties": false,
      "type": "object",
      "required": [
        "completions"
      ]
    },
    "ToolGrep": {
      "properties": {
        "timeout": {
          "type": "integer",
          "description": "Timeout for the grep tool call"
        }
      },
      "additionalProperties": false,
      "type": "object"
    },
    "ToolLs": {
      "properties": {
        "max_depth": {
          "type": "integer",
          "description": "Maximum depth for the ls tool",
          "default": 0,
          "examples": [
            10
          ]
        },
        "max_items": {
          "type": "integer",
          "description": "Maximum number of items to return for the ls tool",
          "default": 1000,
      
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

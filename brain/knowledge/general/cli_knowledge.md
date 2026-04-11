# Knowledge Dump for cli

## File: acp.md
```
---
summary: "Run the ACP bridge for IDE integrations"
read_when:
  - Setting up ACP-based IDE integrations
  - Debugging ACP session routing to the Gateway
title: "acp"
---

# acp

Run the [Agent Client Protocol (ACP)](https://agentclientprotocol.com/) bridge that talks to an OpenClaw Gateway.

This command speaks ACP over stdio for IDEs and forwards prompts to the Gateway
over WebSocket. It keeps ACP sessions mapped to Gateway session keys.

`openclaw acp` is a Gateway-backed ACP bridge, not a full ACP-native editor
runtime. It focuses on session routing, prompt delivery, and basic streaming
updates.

If you want an external MCP client to talk directly to OpenClaw channel
conversations instead of hosting an ACP harness session, use
[`openclaw mcp serve`](/cli/mcp) instead.

## What this is not

This page is often confused with ACP harness sessions.

`openclaw acp` means:

- OpenClaw acts as an ACP server
- an IDE or ACP client connects to OpenClaw
- OpenClaw forwards that work into a Gateway session

This is different from [ACP Agents](/tools/acp-agents), where OpenClaw runs an
external harness such as Codex or Claude Code through `acpx`.

Quick rule:

- editor/client wants to talk ACP to OpenClaw: use `openclaw acp`

## Compatibility Matrix

| ACP area                                                              | Status      | Notes                                                                                                                                                                                                                                            |
| --------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `initialize`, `newSession`, `prompt`, `cancel`                        | Implemented | Core bridge flow over stdio to Gateway chat/send + abort.                                                                                                                                                                                        |
| `listSessions`, slash commands                                        | Implemented | Session list works against Gateway session state; commands are advertised via `available_commands_update`.                                                                                                                                       |
| `loadSession`                                                         | Partial     | Rebinds the ACP session to a Gateway session key and replays stored user/assistant text history. Tool/system history is not reconstructed yet.                                                                                                   |
| Prompt content (`text`, embedded `resource`, images)                  | Partial     | Text/resources are flattened into chat input; images become Gateway attachments.                                                                                                                                                                 |
| Session modes                                                         | Partial     | `session/set_mode` is supported and the bridge exposes initial Gateway-backed session controls for thought level, tool verbosity, reasoning, usage detail, and elevated actions. Broader ACP-native mode/config surfaces are still out of scope. |
| Session info and usage updates                                        | Partial     | The bridge emits `session_info_update` and best-effort `usage_update` notifications from cached Gateway session snapshots. Usage is approximate and only sent when Gateway token totals are marked fresh.                                        |
| Tool streaming                                                        | Partial     | `tool_call` / `tool_call_update` events include raw I/O, text content, and best-effort file locations when Gateway tool args/results expose them. Embedded terminals and richer diff-native output are still not exposed.                        |
| Per-session MCP servers (`mcpServers`)                                | Unsupported | Bridge mode rejects per-session MCP server requests. Configure MCP on the OpenClaw gateway or agent instead.                                                                                                                                     |
| Client filesystem methods (`fs/read_text_file`, `fs/write_text_file`) | Unsupported | The bridge does not call ACP client filesystem methods.                                                                                                                                                                                          |
| Client terminal methods (`terminal/*`)                                | Unsupported | The bridge does not create ACP client terminals or stream terminal ids through tool calls.                                                                                                                                                       |
| Session plans / thought streaming                                     | Unsupported | The bridge currently emits output text and tool status, not ACP plan or thought updates.                                                                                                                                                         |

## Known Limitations

- `loadSession` replays stored user and assistant text history, but it does not
  reconstruct historic tool calls, system notices, or richer ACP-native event
  types.
- If multiple ACP clients share the same Gateway session key, event and cancel
  routing are best-effort rather than strictly isolated per client. Prefer the
  default isolated `acp:<uuid>` sessions when you need clean editor-local
  turns.
- Gateway stop states are translated into ACP stop reasons, but that mapping is
  less expressive than a fully ACP-native runtime.
- Initial session controls currently surface a focused subset of Gateway knobs:
  thought level, tool verbosity, reasoning, usage detail, and elevated
  actions. Model selection and exec-host controls are not yet exposed as ACP
  config options.
- `session_info_update` and `usage_update` are derived from Gateway session
  snapshots, not live ACP-native runtime accounting. Usage is approximate,
  carries no cost data, and is only emitted when the Gateway marks total token
  data as fresh.
- Tool follow-along data is best-effort. The bridge can surface file paths that
  appear in known tool args/results, but it does not yet emit ACP terminals or
  structured file diffs.

## Usage

```bash
openclaw acp

# Remote Gateway
openclaw acp --url wss://gateway-host:18789 --token <token>

# Remote Gateway (token from file)
openclaw acp --url wss://gateway-host:18789 --token-file ~/.openclaw/gateway.token

# Attach to an existing session key
openclaw acp --session agent:main:main

# Attach by label (must already exist)
openclaw acp --session-label "support inbox"

# Reset the session key before the first prompt
openclaw acp --session agent:main:main --reset-session
```

## ACP client (debug)

Use the built-in ACP client to sanity-check the bridge without an IDE.
It spawns the ACP bridge and lets you type prompts interactively.

```bash
openclaw acp client

# Point the spawned bridge at a remote Gateway
openclaw acp client --server-args --url wss://gateway-host:18789 --token-file ~/.openclaw/gateway.token

# Override the server command (default: openclaw)
openclaw acp client --server "node" --server-args openclaw.mjs acp --url ws://127.0.0.1:19001
```

Permission model (client debug mode):

- Auto-approval is allowlist-based and only applies to trusted core tool IDs.
- `read` auto-approval is scoped to the current working directory (`--cwd` when set).
- ACP only auto-approves narrow readonly classes: scoped `read` calls under the active cwd plus readonly search tools (`search`, `web_search`, `memory_search`). Unknown/non-core tools, out-of-scope reads, exec-capable tools, control-plane tools, mutating tools, and interactive flows always require explicit prompt approval.
- Server-provided `toolCall.kind` is treated as untrusted metadata (not an authorization source).
- This ACP bridge policy is separate from ACPX harness permissions. If you run OpenClaw through the `acpx` backend, `plugins.entries.acpx.config.permissionMode=approve-all` is the break-glass “yolo” switch for that harness session.

## How to use this

Use ACP when an IDE (or other client) speaks Agent Client Protocol and you want
it to drive an OpenClaw Gateway session.

1. Ensure the Gateway is running (local or remote).
2. Configure the Gateway target (config or flags).
3. Point your IDE to run `openclaw acp` over stdio.

Example config (persisted):

```bash
openclaw config set gateway.remote.url wss://gateway-host:18789
openclaw config set gateway.remote.token <token>
```

Example direct run (no config write):

```bash
openclaw acp --url wss://gateway-host:18789 --token <token>
# preferred for local process safety
openclaw acp --url wss://gateway-host:18789 --token-file ~/.openclaw/gateway.token
```

## Selecting agents

ACP does not pick agents directly. It routes by the Gateway session key.

Use agent-scoped session keys to target a specific agent:

```bash
openclaw acp --session agent:main:main
openclaw acp --session agent:design:main
openclaw acp --session agent:qa:bug-123
```

Each ACP session maps to a single Gateway session key. One agent can have many
sessions; ACP defaults to an isolated `acp:<uuid>` session unless you override
the key or label.

Per-session `mcpServers` are not supported in bridge mode. If an ACP client
sends them during `newSession` or `loadSession`, the bridge returns a clear
error instead of silently ignoring them.

If you want ACPX-backed sessions to see OpenClaw plugin tools, enable the
gateway-side ACPX plugin bridge instead of trying to pass per-session
`mcpServers`. See [ACP Agents](/tools/acp-agents#plugin-tools-mcp-bridge).

## Use from `acpx` (Codex, Claude, other ACP clients)

If you want a coding agent such as Codex or Claude Code to talk to your
OpenClaw bot over ACP, use `acpx` with its built-in `openclaw` target.

Typical flow:

1. Run the Gateway and make sure the ACP bridge can reach it.
2. Point `acpx openclaw` at `openclaw acp`.
3. Target the OpenClaw session key you want the coding agent to use.

Examples:

```bash
# One-shot request into your default OpenClaw ACP session
acpx openclaw exec "Summarize the active OpenClaw session state."

# Persistent named session for follow-up turns
acpx openclaw sessions ensure --name codex-bridge
acpx openclaw -s codex-bridge --cwd /path/to/repo \
  "Ask my OpenClaw work agent for recent context relevant to this repo."
```

If you want `acpx openclaw` to target a specific Gateway and session key every
time, override the `openclaw` agent command in `~/.acpx/config.json`:

```json
{
  "agents": {
    "openclaw": {
      "command": "env OPENCLAW_HIDE_BANNER=1 OPENCLAW_SUPPRESS_NOTES=1 openclaw acp --url ws://127.0.0.1:18789 --token-file ~/.openclaw/gateway.token --session agent:main:main"
    }
  }
}
```

For a repo-local OpenClaw checkout, use the direct CLI entrypoint instead of the
dev runner so the ACP stream stays clean. For example:

```bash
env OPENCLAW_HIDE_BANNER=1 OPENCLAW_SUPPRESS_NOTES=1 node openclaw.mjs acp ...
```

This is the easiest way to let Codex, Claude Code, or another ACP-aware client
pull contextual information from an OpenClaw agent without scraping a terminal.

## Zed editor setup

Add a custom ACP agent in `~/.config/zed/settings.json` (or use Zed’s Settings UI):

```json
{
  "agent_servers": {
    "OpenClaw ACP": {
      "type": "custom",
      "command": "openclaw",
      "args": ["acp"],
      "env": {}
    }
  }
}
```

To target a specific Gateway or agent:

```json
{
  "agent_servers": {
    "OpenClaw ACP": {
      "type": "custom",
      "command": "openclaw",
      "args": [
        "acp",
        "--url",
        "wss://gateway-host:18789",
        "--token",
        "<token>",
        "--session",
        "agent:design:main"
      ],
      "env": {}
    }
  }
}
```

In Zed, open the Agent panel and select “OpenClaw ACP” to start a thread.

## Session mapping

By default, ACP sessions get an isolated Gateway session key with an `acp:` prefix.
To reuse a known session, pass a session key or label:

- `--session <key>`: use a specific Gateway session key.
- `--session-label <label>`: resolve an existing session by label.
- `--reset-session`: mint a fresh session id for that key (same key, new transcript).

If your ACP client supports metadata, you can override per session:

```json
{
  "_meta": {
    "sessionKey": "agent:main:main",
    "sessionLabel": "support inbox",
    "resetSession": true
  }
}
```

Learn more about session keys at [/concepts/session](/concepts/session).

## Options

- `--url <url>`: Gateway WebSocket URL (defaults to gateway.remote.url when configured).
- `--token <token>`: Gateway auth token.
- `--token-file <path>`: read Gateway auth token from file.
- `--password <password>`: Gateway auth password.
- `--password-file <path>`: read Gateway auth password from file.
- `--session <key>`: default session key.
- `--session-label <label>`: default session label to resolve.
- `--require-existing`: fail if the session key/label does not exist.
- `--reset-session`: reset the session key before first use.
- `--no-prefix-cwd`: do not prefix prompts with the working directory.
- `--provenance <off|meta|meta+receipt>`: include ACP provenance metadata or receipts.
- `--verbose, -v`: verbose logging to stderr.

Security note:

- `--token` and `--password` can be visible in local process listings on some systems.
- Prefer `--token-file`/`--password-file` or environment variables (`OPENCLAW_GATEWAY_TOKEN`, `OPENCLAW_GATEWAY_PASSWORD`).
- Gateway auth resolution follows the shared contract used by other Gateway clients:
  - local mode: env (`OPENCLAW_GATEWAY_*`) -> `gateway.auth.*` -> `gateway.remote.*` fallback only when `gateway.auth.*` is unset (configured-but-unresolved local SecretRefs fail closed)
  - remote mode: `gateway.remote.*` with env/config fallback per remote precedence rules
  - `--url` is override-safe and does not reuse implicit config/env credentials; pass explicit `--token`/`--password` (or file variants)
- ACP runtime backend child processes receive `OPENCLAW_SHELL=acp`, which can be used for context-specific shell/profile rules.
- `openclaw acp client` sets `OPENCLAW_SHELL=acp-client` on the spawned bridge process.

### `acp client` options

- `--cwd <dir>`: working directory for the ACP session.
- `--server <command>`: ACP server command (default: `openclaw`).
- `--server-args <args...>`: extra arguments passed to the ACP server.
- `--server-verbose`: enable verbose logging on the ACP server.
- `--verbose, -v`: verbose client logging.

```

## File: agent.md
```
---
summary: "CLI reference for `openclaw agent` (send one agent turn via the Gateway)"
read_when:
  - You want to run one agent turn from scripts (optionally deliver reply)
title: "agent"
---

# `openclaw agent`

Run an agent turn via the Gateway (use `--local` for embedded).
Use `--agent <id>` to target a configured agent directly.

Pass at least one session selector:

- `--to <dest>`
- `--session-id <id>`
- `--agent <id>`

Related:


## Options

- `-m, --message <text>`: required message body
- `-t, --to <dest>`: recipient used to derive the session key
- `--session-id <id>`: explicit session id
- `--agent <id>`: agent id; overrides routing bindings
- `--thinking <off|minimal|low|medium|high|xhigh>`: agent thinking level
- `--verbose <on|off>`: persist verbose level for the session
- `--channel <channel>`: delivery channel; omit to use the main session channel
- `--reply-to <target>`: delivery target override
- `--reply-channel <channel>`: delivery channel override
- `--reply-account <id>`: delivery account override
- `--local`: run the embedded agent directly (after plugin registry preload)
- `--deliver`: send the reply back to the selected channel/target
- `--timeout <seconds>`: override agent timeout (default 600 or config value)
- `--json`: output JSON

## Examples

```bash
openclaw agent --to +15555550123 --message "status update" --deliver
openclaw agent --agent ops --message "Summarize logs"
openclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium
openclaw agent --to +15555550123 --message "Trace logs" --verbose on --json
openclaw agent --agent ops --message "Generate report" --deliver --reply-channel slack --reply-to "#reports"
openclaw agent --agent ops --message "Run locally" --local
```

## Notes

- Gateway mode falls back to the embedded agent when the Gateway request fails. Use `--local` to force embedded execution up front.
- `--local` still preloads the plugin registry first, so plugin-provided providers, tools, and channels stay available during embedded runs.
- `--channel`, `--reply-channel`, and `--reply-account` affect reply delivery, not session routing.
- When this command triggers `models.json` regeneration, SecretRef-managed provider credentials are persisted as non-secret markers (for example env var names, `secretref-env:ENV_VAR_NAME`, or `secretref-managed`), not resolved secret plaintext.
- Marker writes are source-authoritative: OpenClaw persists markers from the active source config snapshot, not from resolved runtime secret values.

```

## File: agents.md
```
---
summary: "CLI reference for `openclaw agents` (list/add/delete/bindings/bind/unbind/set identity)"
read_when:
  - You want multiple isolated agents (workspaces + routing + auth)
title: "agents"
---

# `openclaw agents`

Manage isolated agents (workspaces + auth + routing).

Related:


## Examples

```bash
openclaw agents list
openclaw agents list --bindings
openclaw agents add work --workspace ~/.openclaw/workspace-work
openclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactive
openclaw agents bindings
openclaw agents bind --agent work --bind telegram:ops
openclaw agents unbind --agent work --bind telegram:ops
openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
openclaw agents set-identity --agent main --avatar avatars/openclaw.png
openclaw agents delete work
```

## Routing bindings

Use routing bindings to pin inbound channel traffic to a specific agent.

If you also want different visible skills per agent, configure
`agents.defaults.skills` and `agents.list[].skills` in `openclaw.json`. See
[Skills config](/tools/skills-config) and
[Configuration Reference](/gateway/configuration-reference#agentsdefaultsskills).

List bindings:

```bash
openclaw agents bindings
openclaw agents bindings --agent work
openclaw agents bindings --json
```

Add bindings:

```bash
openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
```

If you omit `accountId` (`--bind <channel>`), OpenClaw resolves it from channel defaults and plugin setup hooks when available.

If you omit `--agent` for `bind` or `unbind`, OpenClaw targets the current default agent.

### Binding scope behavior

- A binding without `accountId` matches the channel default account only.
- `accountId: "*"` is the channel-wide fallback (all accounts) and is less specific than an explicit account binding.
- If the same agent already has a matching channel binding without `accountId`, and you later bind with an explicit or resolved `accountId`, OpenClaw upgrades that existing binding in place instead of adding a duplicate.

Example:

```bash
# initial channel-only binding
openclaw agents bind --agent work --bind telegram

# later upgrade to account-scoped binding
openclaw agents bind --agent work --bind telegram:ops
```

After the upgrade, routing for that binding is scoped to `telegram:ops`. If you also want default-account routing, add it explicitly (for example `--bind telegram:default`).

Remove bindings:

```bash
openclaw agents unbind --agent work --bind telegram:ops
openclaw agents unbind --agent work --all
```

`unbind` accepts either `--all` or one or more `--bind` values, not both.

## Command surface

### `agents`

Running `openclaw agents` with no subcommand is equivalent to `openclaw agents list`.

### `agents list`

Options:

- `--json`
- `--bindings`: include full routing rules, not only per-agent counts/summaries

### `agents add [name]`

Options:

- `--workspace <dir>`
- `--model <id>`
- `--agent-dir <dir>`
- `--bind <channel[:accountId]>` (repeatable)
- `--non-interactive`
- `--json`

Notes:

- Passing any explicit add flags switches the command into the non-interactive path.
- Non-interactive mode requires both an agent name and `--workspace`.
- `main` is reserved and cannot be used as the new agent id.

### `agents bindings`

Options:

- `--agent <id>`
- `--json`

### `agents bind`

Options:

- `--agent <id>` (defaults to the current default agent)
- `--bind <channel[:accountId]>` (repeatable)
- `--json`

### `agents unbind`

Options:

- `--agent <id>` (defaults to the current default agent)
- `--bind <channel[:accountId]>` (repeatable)
- `--all`
- `--json`

### `agents delete <id>`

Options:

- `--force`
- `--json`

Notes:

- `main` cannot be deleted.
- Without `--force`, interactive confirmation is required.
- Workspace, agent state, and session transcript directories are moved to Trash, not hard-deleted.

## Identity files

Each agent workspace can include an `IDENTITY.md` at the workspace root:

- Example path: `~/.openclaw/workspace/IDENTITY.md`
- `set-identity --from-identity` reads from the workspace root (or an explicit `--identity-file`)

Avatar paths resolve relative to the workspace root.

## Set identity

`set-identity` writes fields into `agents.list[].identity`:

- `name`
- `theme`
- `emoji`
- `avatar` (workspace-relative path, http(s) URL, or data URI)

Options:

- `--agent <id>`
- `--workspace <dir>`
- `--identity-file <path>`
- `--from-identity`
- `--name <name>`
- `--theme <theme>`
- `--emoji <emoji>`
- `--avatar <value>`
- `--json`

Notes:

- `--agent` or `--workspace` can be used to select the target agent.
- If you rely on `--workspace` and multiple agents share that workspace, the command fails and asks you to pass `--agent`.
- When no explicit identity fields are provided, the command reads identity data from `IDENTITY.md`.

Load from `IDENTITY.md`:

```bash
openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
```

Override fields explicitly:

```bash
openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
```

Config sample:

```json5
{
  agents: {
    list: [
      {
        id: "main",
        identity: {
          name: "OpenClaw",
          theme: "space lobster",
          emoji: "🦞",
          avatar: "avatars/openclaw.png",
        },
      },
    ],
  },
}
```

```

## File: approvals.md
```
---
summary: "CLI reference for `openclaw approvals` (exec approvals for gateway or node hosts)"
read_when:
  - You want to edit exec approvals from the CLI
  - You need to manage allowlists on gateway or node hosts
title: "approvals"
---

# `openclaw approvals`

Manage exec approvals for the **local host**, **gateway host**, or a **node host**.
By default, commands target the local approvals file on disk. Use `--gateway` to target the gateway, or `--node` to target a specific node.

Alias: `openclaw exec-approvals`

Related:


## Common commands

```bash
openclaw approvals get
openclaw approvals get --node <id|name|ip>
openclaw approvals get --gateway
```

`openclaw approvals get` now shows the effective exec policy for local, gateway, and node targets:

- requested `tools.exec` policy
- host approvals-file policy
- effective result after precedence rules are applied

Precedence is intentional:

- the host approvals file is the enforceable source of truth
- requested `tools.exec` policy can narrow or broaden intent, but the effective result is still derived from the host rules
- `--node` combines the node host approvals file with gateway `tools.exec` policy, because both still apply at runtime
- if gateway config is unavailable, the CLI falls back to the node approvals snapshot and notes that the final runtime policy could not be computed

## Replace approvals from a file

```bash
openclaw approvals set --file ./exec-approvals.json
openclaw approvals set --stdin <<'EOF'
{ version: 1, defaults: { security: "full", ask: "off" } }
EOF
openclaw approvals set --node <id|name|ip> --file ./exec-approvals.json
openclaw approvals set --gateway --file ./exec-approvals.json
```

`set` accepts JSON5, not only strict JSON. Use either `--file` or `--stdin`, not both.

## "Never prompt" / YOLO example

For a host that should never stop on exec approvals, set the host approvals defaults to `full` + `off`:

```bash
openclaw approvals set --stdin <<'EOF'
{
  version: 1,
  defaults: {
    security: "full",
    ask: "off",
    askFallback: "full"
  }
}
EOF
```

Node variant:

```bash
openclaw approvals set --node <id|name|ip> --stdin <<'EOF'
{
  version: 1,
  defaults: {
    security: "full",
    ask: "off",
    askFallback: "full"
  }
}
EOF
```

This changes the **host approvals file** only. To keep the requested OpenClaw policy aligned, also set:

```bash
openclaw config set tools.exec.host gateway
openclaw config set tools.exec.security full
openclaw config set tools.exec.ask off
```

Why `tools.exec.host=gateway` in this example:

- `host=auto` still means "sandbox when available, otherwise gateway".
- YOLO is about approvals, not routing.
- If you want host exec even when a sandbox is configured, make the host choice explicit with `gateway` or `/exec host=gateway`.

This matches the current host-default YOLO behavior. Tighten it if you want approvals.

## Allowlist helpers

```bash
openclaw approvals allowlist add "~/Projects/**/bin/rg"
openclaw approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"
openclaw approvals allowlist add --agent "*" "/usr/bin/uname"

openclaw approvals allowlist remove "~/Projects/**/bin/rg"
```

## Common options

`get`, `set`, and `allowlist add|remove` all support:

- `--node <id|name|ip>`
- `--gateway`
- shared node RPC options: `--url`, `--token`, `--timeout`, `--json`

Targeting notes:

- no target flags means the local approvals file on disk
- `--gateway` targets the gateway host approvals file
- `--node` targets one node host after resolving id, name, IP, or id prefix

`allowlist add|remove` also supports:

- `--agent <id>` (defaults to `*`)

## Notes

- `--node` uses the same resolver as `openclaw nodes` (id, name, ip, or id prefix).
- `--agent` defaults to `"*"`, which applies to all agents.
- The node host must advertise `system.execApprovals.get/set` (macOS app or headless node host).
- Approvals files are stored per host at `~/.openclaw/exec-approvals.json`.

```

## File: backup.md
```
---
summary: "CLI reference for `openclaw backup` (create local backup archives)"
read_when:
  - You want a first-class backup archive for local OpenClaw state
  - You want to preview which paths would be included before reset or uninstall
title: "backup"
---

# `openclaw backup`

Create a local backup archive for OpenClaw state, config, auth profiles, channel/provider credentials, sessions, and optionally workspaces.

```bash
openclaw backup create
openclaw backup create --output ~/Backups
openclaw backup create --dry-run --json
openclaw backup create --verify
openclaw backup create --no-include-workspace
openclaw backup create --only-config
openclaw backup verify ./2026-03-09T00-00-00.000Z-openclaw-backup.tar.gz
```

## Notes

- The archive includes a `manifest.json` file with the resolved source paths and archive layout.
- Default output is a timestamped `.tar.gz` archive in the current working directory.
- If the current working directory is inside a backed-up source tree, OpenClaw falls back to your home directory for the default archive location.
- Existing archive files are never overwritten.
- Output paths inside the source state/workspace trees are rejected to avoid self-inclusion.
- `openclaw backup verify <archive>` validates that the archive contains exactly one root manifest, rejects traversal-style archive paths, and checks that every manifest-declared payload exists in the tarball.
- `openclaw backup create --verify` runs that validation immediately after writing the archive.
- `openclaw backup create --only-config` backs up just the active JSON config file.

## What gets backed up

`openclaw backup create` plans backup sources from your local OpenClaw install:

- The state directory returned by OpenClaw's local state resolver, usually `~/.openclaw`
- The active config file path
- The resolved `credentials/` directory when it exists outside the state directory
- Workspace directories discovered from the current config, unless you pass `--no-include-workspace`

Model auth profiles are already part of the state directory under
`agents/<agentId>/agent/auth-profiles.json`, so they are normally covered by the
state backup entry.

If you use `--only-config`, OpenClaw skips state, credentials-directory, and workspace discovery and archives only the active config file path.

OpenClaw canonicalizes paths before building the archive. If config, the
credentials directory, or a workspace already live inside the state directory,
they are not duplicated as separate top-level backup sources. Missing paths are
skipped.

The archive payload stores file contents from those source trees, and the embedded `manifest.json` records the resolved absolute source paths plus the archive layout used for each asset.

## Invalid config behavior

`openclaw backup` intentionally bypasses the normal config preflight so it can still help during recovery. Because workspace discovery depends on a valid config, `openclaw backup create` now fails fast when the config file exists but is invalid and workspace backup is still enabled.

If you still want a partial backup in that situation, rerun:

```bash
openclaw backup create --no-include-workspace
```

That keeps state, config, and the external credentials directory in scope while
skipping workspace discovery entirely.

If you only need a copy of the config file itself, `--only-config` also works when the config is malformed because it does not rely on parsing the config for workspace discovery.

## Size and performance

OpenClaw does not enforce a built-in maximum backup size or per-file size limit.

Practical limits come from the local machine and destination filesystem:

- Available space for the temporary archive write plus the final archive
- Time to walk large workspace trees and compress them into a `.tar.gz`
- Time to rescan the archive if you use `openclaw backup create --verify` or run `openclaw backup verify`
- Filesystem behavior at the destination path. OpenClaw prefers a no-overwrite hard-link publish step and falls back to exclusive copy when hard links are unsupported

Large workspaces are usually the main driver of archive size. If you want a smaller or faster backup, use `--no-include-workspace`.

For the smallest archive, use `--only-config`.

```

## File: browser.md
```
---
summary: "CLI reference for `openclaw browser` (lifecycle, profiles, tabs, actions, state, and debugging)"
read_when:
  - You use `openclaw browser` and want examples for common tasks
  - You want to control a browser running on another machine via a node host
  - You want to attach to your local signed-in Chrome via Chrome MCP
title: "browser"
---

# `openclaw browser`

Manage OpenClaw's browser control surface and run browser actions (lifecycle, profiles, tabs, snapshots, screenshots, navigation, input, state emulation, and debugging).

Related:


## Common flags

- `--url <gatewayWsUrl>`: Gateway WebSocket URL (defaults to config).
- `--token <token>`: Gateway token (if required).
- `--timeout <ms>`: request timeout (ms).
- `--expect-final`: wait for a final Gateway response.
- `--browser-profile <name>`: choose a browser profile (default from config).
- `--json`: machine-readable output (where supported).

## Quick start (local)

```bash
openclaw browser profiles
openclaw browser --browser-profile openclaw start
openclaw browser --browser-profile openclaw open https://example.com
openclaw browser --browser-profile openclaw snapshot
```

## Lifecycle

```bash
openclaw browser status
openclaw browser start
openclaw browser stop
openclaw browser --browser-profile openclaw reset-profile
```

Notes:

- For `attachOnly` and remote CDP profiles, `openclaw browser stop` closes the
  active control session and clears temporary emulation overrides even when
  OpenClaw did not launch the browser process itself.
- For local managed profiles, `openclaw browser stop` stops the spawned browser
  process.

## If the command is missing

If `openclaw browser` is an unknown command, check `plugins.allow` in
`~/.openclaw/openclaw.json`.

When `plugins.allow` is present, the bundled browser plugin must be listed
explicitly:

```json5
{
  plugins: {
    allow: ["telegram", "browser"],
  },
}
```

`browser.enabled=true` does not restore the CLI subcommand when the plugin
allowlist excludes `browser`.

Related: [Browser tool](/tools/browser#missing-browser-command-or-tool)

## Profiles

Profiles are named browser routing configs. In practice:

- `openclaw`: launches or attaches to a dedicated OpenClaw-managed Chrome instance (isolated user data dir).
- `user`: controls your existing signed-in Chrome session via Chrome DevTools MCP.
- custom CDP profiles: point at a local or remote CDP endpoint.

```bash
openclaw browser profiles
openclaw browser create-profile --name work --color "#FF5A36"
openclaw browser create-profile --name chrome-live --driver existing-session
openclaw browser create-profile --name remote --cdp-url https://browser-host.example.com
openclaw browser delete-profile --name work
```

Use a specific profile:

```bash
openclaw browser --browser-profile work tabs
```

## Tabs

```bash
openclaw browser tabs
openclaw browser tab new
openclaw browser tab select 2
openclaw browser tab close 2
openclaw browser open https://docs.openclaw.ai
openclaw browser focus <targetId>
openclaw browser close <targetId>
```

## Snapshot / screenshot / actions

Snapshot:

```bash
openclaw browser snapshot
```

Screenshot:

```bash
openclaw browser screenshot
openclaw browser screenshot --full-page
openclaw browser screenshot --ref e12
```

Notes:

- `--full-page` is for page captures only; it cannot be combined with `--ref`
  or `--element`.
- `existing-session` / `user` profiles support page screenshots and `--ref`
  screenshots from snapshot output, but not CSS `--element` screenshots.

Navigate/click/type (ref-based UI automation):

```bash
openclaw browser navigate https://example.com
openclaw browser click <ref>
openclaw browser type <ref> "hello"
openclaw browser press Enter
openclaw browser hover <ref>
openclaw browser scrollintoview <ref>
openclaw browser drag <startRef> <endRef>
openclaw browser select <ref> OptionA OptionB
openclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'
openclaw browser wait --text "Done"
openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
```

File + dialog helpers:

```bash
openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>
openclaw browser waitfordownload
openclaw browser download <ref> report.pdf
openclaw browser dialog --accept
```

## State and storage

Viewport + emulation:

```bash
openclaw browser resize 1280 720
openclaw browser set viewport 1280 720
openclaw browser set offline on
openclaw browser set media dark
openclaw browser set timezone Europe/London
openclaw browser set locale en-GB
openclaw browser set geo 51.5074 -0.1278 --accuracy 25
openclaw browser set device "iPhone 14"
openclaw browser set headers '{"x-test":"1"}'
openclaw browser set credentials myuser mypass
```

Cookies + storage:

```bash
openclaw browser cookies
openclaw browser cookies set session abc123 --url https://example.com
openclaw browser cookies clear
openclaw browser storage local get
openclaw browser storage local set token abc123
openclaw browser storage session clear
```

## Debugging

```bash
openclaw browser console --level error
openclaw browser pdf
openclaw browser responsebody "**/api"
openclaw browser highlight <ref>
openclaw browser errors --clear
openclaw browser requests --filter api
openclaw browser trace start
openclaw browser trace stop --out trace.zip
```

## Existing Chrome via MCP

Use the built-in `user` profile, or create your own `existing-session` profile:

```bash
openclaw browser --browser-profile user tabs
openclaw browser create-profile --name chrome-live --driver existing-session
openclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"
openclaw browser --browser-profile chrome-live tabs
```

This path is host-only. For Docker, headless servers, Browserless, or other remote setups, use a CDP profile instead.

Current existing-session limits:

- snapshot-driven actions use refs, not CSS selectors
- `click` is left-click only
- `type` does not support `slowly=true`
- `press` does not support `delayMs`
- `hover`, `scrollintoview`, `drag`, `select`, `fill`, and `evaluate` reject
  per-call timeout overrides
- `select` supports one value only
- `wait --load networkidle` is not supported
- file uploads require `--ref` / `--input-ref`, do not support CSS
  `--element`, and currently support one file at a time
- dialog hooks do not support `--timeout`
- screenshots support page captures and `--ref`, but not CSS `--element`
- `responsebody`, download interception, PDF export, and batch actions still
  require a managed browser or raw CDP profile

## Remote browser control (node host proxy)

If the Gateway runs on a different machine than the browser, run a **node host** on the machine that has Chrome/Brave/Edge/Chromium. The Gateway will proxy browser actions to that node (no separate browser control server required).

Use `gateway.nodes.browser.mode` to control auto-routing and `gateway.nodes.browser.node` to pin a specific node if multiple are connected.

Security + remote setup: [Browser tool](/tools/browser), [Remote access](/gateway/remote), [Tailscale](/gateway/tailscale), [Security](/gateway/security)

```

## File: channels.md
```
---
summary: "CLI reference for `openclaw channels` (accounts, status, login/logout, logs)"
read_when:
  - You want to add/remove channel accounts (WhatsApp/Telegram/Discord/Google Chat/Slack/Mattermost (plugin)/Signal/iMessage/Matrix)
  - You want to check channel status or tail channel logs
title: "channels"
---

# `openclaw channels`

Manage chat channel accounts and their runtime status on the Gateway.

Related docs:


## Common commands

```bash
openclaw channels list
openclaw channels status
openclaw channels capabilities
openclaw channels capabilities --channel discord --target channel:123
openclaw channels resolve --channel slack "#general" "@jane"
openclaw channels logs --channel all
```

## Status / capabilities / resolve / logs

- `channels status`: `--probe`, `--timeout <ms>`, `--json`
- `channels capabilities`: `--channel <name>`, `--account <id>` (only with `--channel`), `--target <dest>`, `--timeout <ms>`, `--json`
- `channels resolve`: `<entries...>`, `--channel <name>`, `--account <id>`, `--kind <auto|user|group>`, `--json`
- `channels logs`: `--channel <name|all>`, `--lines <n>`, `--json`

`channels status --probe` is the live path: on a reachable gateway it runs per-account
`probeAccount` and optional `auditAccount` checks, so output can include transport
state plus probe results such as `works`, `probe failed`, `audit ok`, or `audit failed`.
If the gateway is unreachable, `channels status` falls back to config-only summaries
instead of live probe output.

## Add / remove accounts

```bash
openclaw channels add --channel telegram --token <bot-token>
openclaw channels add --channel nostr --private-key "$NOSTR_PRIVATE_KEY"
openclaw channels remove --channel telegram --delete
```

Tip: `openclaw channels add --help` shows per-channel flags (token, private key, app token, signal-cli paths, etc).

Common non-interactive add surfaces include:

- bot-token channels: `--token`, `--bot-token`, `--app-token`, `--token-file`
- Signal/iMessage transport fields: `--signal-number`, `--cli-path`, `--http-url`, `--http-host`, `--http-port`, `--db-path`, `--service`, `--region`
- Google Chat fields: `--webhook-path`, `--webhook-url`, `--audience-type`, `--audience`
- Matrix fields: `--homeserver`, `--user-id`, `--access-token`, `--password`, `--device-name`, `--initial-sync-limit`
- Nostr fields: `--private-key`, `--relay-urls`
- Tlon fields: `--ship`, `--url`, `--code`, `--group-channels`, `--dm-allowlist`, `--auto-discover-channels`
- `--use-env` for default-account env-backed auth where supported

When you run `openclaw channels add` without flags, the interactive wizard can prompt:

- account ids per selected channel
- optional display names for those accounts
- `Bind configured channel accounts to agents now?`

If you confirm bind now, the wizard asks which agent should own each configured channel account and writes account-scoped routing bindings.

You can also manage the same routing rules later with `openclaw agents bindings`, `openclaw agents bind`, and `openclaw agents unbind` (see [agents](/cli/agents)).

When you add a non-default account to a channel that is still using single-account top-level settings, OpenClaw promotes account-scoped top-level values into the channel's account map before writing the new account. Most channels land those values in `channels.<channel>.accounts.default`, but bundled channels can preserve an existing matching promoted account instead. Matrix is the current example: if one named account already exists, or `defaultAccount` points at an existing named account, promotion preserves that account instead of creating a new `accounts.default`.

Routing behavior stays consistent:

- Existing channel-only bindings (no `accountId`) continue to match the default account.
- `channels add` does not auto-create or rewrite bindings in non-interactive mode.
- Interactive setup can optionally add account-scoped bindings.

If your config was already in a mixed state (named accounts present and top-level single-account values still set), run `openclaw doctor --fix` to move account-scoped values into the promoted account chosen for that channel. Most channels promote into `accounts.default`; Matrix can preserve an existing named/default target instead.

## Login / logout (interactive)

```bash
openclaw channels login --channel whatsapp
openclaw channels logout --channel whatsapp
```

Notes:

- `channels login` supports `--verbose`.
- `channels login` / `logout` can infer the channel when only one supported login target is configured.

## Troubleshooting

- Run `openclaw status --deep` for a broad probe.
- Use `openclaw doctor` for guided fixes.
- `openclaw channels list` prints `Claude: HTTP 403 ... user:profile` → usage snapshot needs the `user:profile` scope. Use `--no-usage`, or provide a claude.ai session key (`CLAUDE_WEB_SESSION_KEY` / `CLAUDE_WEB_COOKIE`), or re-auth via Claude CLI.
- `openclaw channels status` falls back to config-only summaries when the gateway is unreachable. If a supported channel credential is configured via SecretRef but unavailable in the current command path, it reports that account as configured with degraded notes instead of showing it as not configured.

## Capabilities probe

Fetch provider capability hints (intents/scopes where available) plus static feature support:

```bash
openclaw channels capabilities
openclaw channels capabilities --channel discord --target channel:123
```

Notes:

- `--channel` is optional; omit it to list every channel (including extensions).
- `--account` is only valid with `--channel`.
- `--target` accepts `channel:<id>` or a raw numeric channel id and only applies to Discord.
- Probes are provider-specific: Discord intents + optional channel permissions; Slack bot + user scopes; Telegram bot flags + webhook; Signal daemon version; Microsoft Teams app token + Graph roles/scopes (annotated where known). Channels without probes report `Probe: unavailable`.

## Resolve names to IDs

Resolve channel/user names to IDs using the provider directory:

```bash
openclaw channels resolve --channel slack "#general" "@jane"
openclaw channels resolve --channel discord "My Server/#support" "@someone"
openclaw channels resolve --channel matrix "Project Room"
```

Notes:

- Use `--kind user|group|auto` to force the target type.
- Resolution prefers active matches when multiple entries share the same name.
- `channels resolve` is read-only. If a selected account is configured via SecretRef but that credential is unavailable in the current command path, the command returns degraded unresolved results with notes instead of aborting the entire run.

```

## File: clawbot.md
```
---
summary: "CLI reference for `openclaw clawbot` (legacy alias namespace)"
read_when:
  - You maintain older scripts using `openclaw clawbot ...`
  - You need migration guidance to current commands
title: "clawbot"
---

# `openclaw clawbot`

Legacy alias namespace kept for backwards compatibility.

Current supported alias:


## Migration

Prefer modern top-level commands directly:

- `openclaw clawbot qr` -> `openclaw qr`

```

## File: completion.md
```
---
summary: "CLI reference for `openclaw completion` (generate/install shell completion scripts)"
read_when:
  - You want shell completions for zsh/bash/fish/PowerShell
  - You need to cache completion scripts under OpenClaw state
title: "completion"
---

# `openclaw completion`

Generate shell completion scripts and optionally install them into your shell profile.

## Usage

```bash
openclaw completion
openclaw completion --shell zsh
openclaw completion --install
openclaw completion --shell fish --install
openclaw completion --write-state
openclaw completion --shell bash --write-state
```

## Options

- `-s, --shell <shell>`: shell target (`zsh`, `bash`, `powershell`, `fish`; default: `zsh`)
- `-i, --install`: install completion by adding a source line to your shell profile
- `--write-state`: write completion script(s) to `$OPENCLAW_STATE_DIR/completions` without printing to stdout
- `-y, --yes`: skip install confirmation prompts

## Notes

- `--install` writes a small "OpenClaw Completion" block into your shell profile and points it at the cached script.
- Without `--install` or `--write-state`, the command prints the script to stdout.
- Completion generation eagerly loads command trees so nested subcommands are included.

```

## File: config.md
```
---
summary: "CLI reference for `openclaw config` (get/set/unset/file/schema/validate)"
read_when:
  - You want to read or edit config non-interactively
title: "config"
---

# `openclaw config`

Config helpers for non-interactive edits in `openclaw.json`: get/set/unset/file/schema/validate
values by path and print the active config file. Run without a subcommand to
open the configure wizard (same as `openclaw configure`).

Root options:

- `--section <section>`: repeatable guided-setup section filter when you run `openclaw config` without a subcommand

Supported guided sections:

- `workspace`
- `model`
- `web`
- `gateway`
- `daemon`
- `channels`
- `plugins`
- `skills`
- `health`

## Examples

```bash
openclaw config file
openclaw config --section model
openclaw config --section gateway --section daemon
openclaw config schema
openclaw config get browser.executablePath
openclaw config set browser.executablePath "/usr/bin/google-chrome"
openclaw config set agents.defaults.heartbeat.every "2h"
openclaw config set agents.list[0].tools.exec.node "node-id-or-name"
openclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN
openclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode json
openclaw config unset plugins.entries.brave.config.webSearch.apiKey
openclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-run
openclaw config validate
openclaw config validate --json
```

### `config schema`

Print the generated JSON schema for `openclaw.json` to stdout as JSON.

What it includes:

- The current root config schema, plus a root `$schema` string field for editor tooling
- Field `title` and `description` docs metadata used by the Control UI
- Nested object, wildcard (`*`), and array-item (`[]`) nodes inherit the same `title` / `description` metadata when matching field documentation exists
- `anyOf` / `oneOf` / `allOf` branches inherit the same docs metadata too when matching field documentation exists
- Best-effort live plugin + channel schema metadata when runtime manifests can be loaded
- A clean fallback schema even when the current config is invalid

Related runtime RPC:

- `config.schema.lookup` returns one normalized config path with a shallow
  schema node (`title`, `description`, `type`, `enum`, `const`, common bounds),
  matched UI hint metadata, and immediate child summaries. Use it for
  path-scoped drill-down in Control UI or custom clients.

```bash
openclaw config schema
```

Pipe it into a file when you want to inspect or validate it with other tools:

```bash
openclaw config schema > openclaw.schema.json
```

### Paths

Paths use dot or bracket notation:

```bash
openclaw config get agents.defaults.workspace
openclaw config get agents.list[0].id
```

Use the agent list index to target a specific agent:

```bash
openclaw config get agents.list
openclaw config set agents.list[1].tools.exec.node "node-id-or-name"
```

## Values

Values are parsed as JSON5 when possible; otherwise they are treated as strings.
Use `--strict-json` to require JSON5 parsing. `--json` remains supported as a legacy alias.

```bash
openclaw config set agents.defaults.heartbeat.every "0m"
openclaw config set gateway.port 19001 --strict-json
openclaw config set channels.whatsapp.groups '["*"]' --strict-json
```

`config get <path> --json` prints the raw value as JSON instead of terminal-formatted text.

## `config set` modes

`openclaw config set` supports four assignment styles:

1. Value mode: `openclaw config set <path> <value>`
2. SecretRef builder mode:

```bash
openclaw config set channels.discord.token \
  --ref-provider default \
  --ref-source env \
  --ref-id DISCORD_BOT_TOKEN
```

3. Provider builder mode (`secrets.providers.<alias>` path only):

```bash
openclaw config set secrets.providers.vault \
  --provider-source exec \
  --provider-command /usr/local/bin/openclaw-vault \
  --provider-arg read \
  --provider-arg openai/api-key \
  --provider-timeout-ms 5000
```

4. Batch mode (`--batch-json` or `--batch-file`):

```bash
openclaw config set --batch-json '[
  {
    "path": "secrets.providers.default",
    "provider": { "source": "env" }
  },
  {
    "path": "channels.discord.token",
    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }
  }
]'
```

```bash
openclaw config set --batch-file ./config-set.batch.json --dry-run
```

Policy note:


Batch parsing always uses the batch payload (`--batch-json`/`--batch-file`) as the source of truth.
`--strict-json` / `--json` do not change batch parsing behavior.

JSON path/value mode remains supported for both SecretRefs and providers:

```bash
openclaw config set channels.discord.token \
  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \
  --strict-json

openclaw config set secrets.providers.vaultfile \
  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \
  --strict-json
```

## Provider Builder Flags

Provider builder targets must use `secrets.providers.<alias>` as the path.

Common flags:

- `--provider-source <env|file|exec>`
- `--provider-timeout-ms <ms>` (`file`, `exec`)

Env provider (`--provider-source env`):

- `--provider-allowlist <ENV_VAR>` (repeatable)

File provider (`--provider-source file`):

- `--provider-path <path>` (required)
- `--provider-mode <singleValue|json>`
- `--provider-max-bytes <bytes>`

Exec provider (`--provider-source exec`):

- `--provider-command <path>` (required)
- `--provider-arg <arg>` (repeatable)
- `--provider-no-output-timeout-ms <ms>`
- `--provider-max-output-bytes <bytes>`
- `--provider-json-only`
- `--provider-env <KEY=VALUE>` (repeatable)
- `--provider-pass-env <ENV_VAR>` (repeatable)
- `--provider-trusted-dir <path>` (repeatable)
- `--provider-allow-insecure-path`
- `--provider-allow-symlink-command`

Hardened exec provider example:

```bash
openclaw config set secrets.providers.vault \
  --provider-source exec \
  --provider-command /usr/local/bin/openclaw-vault \
  --provider-arg read \
  --provider-arg openai/api-key \
  --provider-json-only \
  --provider-pass-env VAULT_TOKEN \
  --provider-trusted-dir /usr/local/bin \
  --provider-timeout-ms 5000
```

## Dry run

Use `--dry-run` to validate changes without writing `openclaw.json`.

```bash
openclaw config set channels.discord.token \
  --ref-provider default \
  --ref-source env \
  --ref-id DISCORD_BOT_TOKEN \
  --dry-run

openclaw config set channels.discord.token \
  --ref-provider default \
  --ref-source env \
  --ref-id DISCORD_BOT_TOKEN \
  --dry-run \
  --json

openclaw config set channels.discord.token \
  --ref-provider vault \
  --ref-source exec \
  --ref-id discord/token \
  --dry-run \
  --allow-exec
```

Dry-run behavior:

- Builder mode: runs SecretRef resolvability checks for changed refs/providers.
- JSON mode (`--strict-json`, `--json`, or batch mode): runs schema validation plus SecretRef resolvability checks.
- Policy validation also runs for known unsupported SecretRef target surfaces.
- Policy checks evaluate the full post-change config, so parent-object writes (for example setting `hooks` as an object) cannot bypass unsupported-surface validation.
- Exec SecretRef checks are skipped by default during dry-run to avoid command side effects.
- Use `--allow-exec` with `--dry-run` to opt in to exec SecretRef checks (this may execute provider commands).
- `--allow-exec` is dry-run only and errors if used without `--dry-run`.

`--dry-run --json` prints a machine-readable report:

- `ok`: whether dry-run passed
- `operations`: number of assignments evaluated
- `checks`: whether schema/resolvability checks ran
- `checks.resolvabilityComplete`: whether resolvability checks ran to completion (false when exec refs are skipped)
- `refsChecked`: number of refs actually resolved during dry-run
- `skippedExecRefs`: number of exec refs skipped because `--allow-exec` was not set
- `errors`: structured schema/resolvability failures when `ok=false`

### JSON Output Shape

```json5
{
  ok: boolean,
  operations: number,
  configPath: string,
  inputModes: ["value" | "json" | "builder", ...],
  checks: {
    schema: boolean,
    resolvability: boolean,
    resolvabilityComplete: boolean,
  },
  refsChecked: number,
  skippedExecRefs: number,
  errors?: [
    {
      kind: "schema" | "resolvability",
      message: string,
      ref?: string, // present for resolvability errors
    },
  ],
}
```

Success example:

```json
{
  "ok": true,
  "operations": 1,
  "configPath": "~/.openclaw/openclaw.json",
  "inputModes": ["builder"],
  "checks": {
    "schema": false,
    "resolvability": true,
    "resolvabilityComplete": true
  },
  "refsChecked": 1,
  "skippedExecRefs": 0
}
```

Failure example:

```json
{
  "ok": false,
  "operations": 1,
  "configPath": "~/.openclaw/openclaw.json",
  "inputModes": ["builder"],
  "checks": {
    "schema": false,
    "resolvability": true,
    "resolvabilityComplete": true
  },
  "refsChecked": 1,
  "skippedExecRefs": 0,
  "errors": [
    {
      "kind": "resolvability",
      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",
      "ref": "env:default:MISSING_TEST_SECRET"
    }
  ]
}
```

If dry-run fails:

- `config schema validation failed`: your post-change config shape is invalid; fix path/value or provider/ref object shape.
- `Config policy validation failed: unsupported SecretRef usage`: move that credential back to plaintext/string input and keep SecretRefs on supported surfaces only.
- `SecretRef assignment(s) could not be resolved`: referenced provider/ref currently cannot resolve (missing env var, invalid file pointer, exec provider failure, or provider/source mismatch).
- `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: dry-run skipped exec refs; rerun with `--allow-exec` if you need exec resolvability validation.
- For batch mode, fix failing entries and rerun `--dry-run` before writing.

## Subcommands

- `config file`: Print the active config file path (resolved from `OPENCLAW_CONFIG_PATH` or default location).

Restart the gateway after edits.

## Validate

Validate the current config against the active schema without starting the
gateway.

```bash
openclaw config validate
openclaw config validate --json
```

```

## File: configure.md
```
---
summary: "CLI reference for `openclaw configure` (interactive configuration prompts)"
read_when:
  - You want to tweak credentials, devices, or agent defaults interactively
title: "configure"
---

# `openclaw configure`

Interactive prompt to set up credentials, devices, and agent defaults.

Note: The **Model** section now includes a multi-select for the
`agents.defaults.models` allowlist (what shows up in `/model` and the model picker).

When configure starts from a provider auth choice, the default-model and
allowlist pickers prefer that provider automatically. For paired providers such
as Volcengine/BytePlus, the same preference also matches their coding-plan
variants (`volcengine-plan/*`, `byteplus-plan/*`). If the preferred-provider
filter would produce an empty list, configure falls back to the unfiltered
catalog instead of showing a blank picker.

Tip: `openclaw config` without a subcommand opens the same wizard. Use
`openclaw config get|set|unset` for non-interactive edits.

For web search, `openclaw configure --section web` lets you choose a provider
and configure its credentials. Some providers also show provider-specific
follow-up prompts:

- **Grok** can offer optional `x_search` setup with the same `XAI_API_KEY` and
  let you pick an `x_search` model.
- **Kimi** can ask for the Moonshot API region (`api.moonshot.ai` vs
  `api.moonshot.cn`) and the default Kimi web-search model.

Related:


## Options

- `--section <section>`: repeatable section filter

Available sections:

- `workspace`
- `model`
- `web`
- `gateway`
- `daemon`
- `channels`
- `plugins`
- `skills`
- `health`

Notes:

- Choosing where the Gateway runs always updates `gateway.mode`. You can select "Continue" without other sections if that is all you need.
- Channel-oriented services (Slack/Discord/Matrix/Microsoft Teams) prompt for channel/room allowlists during setup. You can enter names or IDs; the wizard resolves names to IDs when possible.
- If you run the daemon install step, token auth requires a token, and `gateway.auth.token` is SecretRef-managed, configure validates the SecretRef but does not persist resolved plaintext token values into supervisor service environment metadata.
- If token auth requires a token and the configured token SecretRef is unresolved, configure blocks daemon install with actionable remediation guidance.
- If both `gateway.auth.token` and `gateway.auth.password` are configured and `gateway.auth.mode` is unset, configure blocks daemon install until mode is set explicitly.

## Examples

```bash
openclaw configure
openclaw configure --section web
openclaw configure --section model --section channels
openclaw configure --section gateway --section daemon
```

```

## File: cron.md
```
---
summary: "CLI reference for `openclaw cron` (schedule and run background jobs)"
read_when:
  - You want scheduled jobs and wakeups
  - You’re debugging cron execution and logs
title: "cron"
---

# `openclaw cron`

Manage cron jobs for the Gateway scheduler.

Related:


Tip: run `openclaw cron --help` for the full command surface.

Note: isolated `cron add` jobs default to `--announce` delivery. Use `--no-deliver` to keep
output internal. `--deliver` remains as a deprecated alias for `--announce`.

Note: cron-owned isolated runs expect a plain-text summary and the runner owns
the final send path. `--no-deliver` keeps the run internal; it does not hand
delivery back to the agent's message tool.

Note: one-shot (`--at`) jobs delete after success by default. Use `--keep-after-run` to keep them.

Note: `--session` supports `main`, `isolated`, `current`, and `session:<id>`.
Use `current` to bind to the active session at creation time, or `session:<id>` for
an explicit persistent session key.

Note: for one-shot CLI jobs, offset-less `--at` datetimes are treated as UTC unless you also pass
`--tz <iana>`, which interprets that local wall-clock time in the given timezone.

Note: recurring jobs now use exponential retry backoff after consecutive errors (30s → 1m → 5m → 15m → 60m), then return to normal schedule after the next successful run.

Note: `openclaw cron run` now returns as soon as the manual run is queued for execution. Successful responses include `{ ok: true, enqueued: true, runId }`; use `openclaw cron runs --id <job-id>` to follow the eventual outcome.

Note: `openclaw cron run <job-id>` force-runs by default. Use `--due` to keep the
older "only run if due" behavior.

Note: isolated cron turns suppress stale acknowledgement-only replies. If the
first result is just an interim status update and no descendant subagent run is
responsible for the eventual answer, cron re-prompts once for the real result
before delivery.

Note: if an isolated cron run returns only the silent token (`NO_REPLY` /
`no_reply`), cron suppresses direct outbound delivery and the fallback queued
summary path as well, so nothing is posted back to chat.

Note: `cron add|edit --model ...` uses that selected allowed model for the job.
If the model is not allowed, cron warns and falls back to the job's agent/default
model selection instead. Configured fallback chains still apply, but a plain
model override with no explicit per-job fallback list no longer appends the
agent primary as a hidden extra retry target.

Note: isolated cron model precedence is Gmail-hook override first, then per-job
`--model`, then any stored cron-session model override, then the normal
agent/default selection.

Note: isolated cron fast mode follows the resolved live model selection. Model
config `params.fastMode` applies by default, but a stored session `fastMode`
override still wins over config.

Note: if an isolated run throws `LiveSessionModelSwitchError`, cron persists the
switched provider/model (and switched auth profile override when present) before
retrying. The outer retry loop is bounded to 2 switch retries after the initial
attempt, then aborts instead of looping forever.

Note: failure notifications use `delivery.failureDestination` first, then
global `cron.failureDestination`, and finally fall back to the job's primary
announce target when no explicit failure destination is configured.

Note: retention/pruning is controlled in config:

- `cron.sessionRetention` (default `24h`) prunes completed isolated run sessions.
- `cron.runLog.maxBytes` + `cron.runLog.keepLines` prune `~/.openclaw/cron/runs/<jobId>.jsonl`.

Upgrade note: if you have older cron jobs from before the current delivery/store format, run
`openclaw doctor --fix`. Doctor now normalizes legacy cron fields (`jobId`, `schedule.cron`,
top-level delivery fields including legacy `threadId`, payload `provider` delivery aliases) and migrates simple
`notify: true` webhook fallback jobs to explicit webhook delivery when `cron.webhook` is
configured.

## Common edits

Update delivery settings without changing the message:

```bash
openclaw cron edit <job-id> --announce --channel telegram --to "123456789"
```

Disable delivery for an isolated job:

```bash
openclaw cron edit <job-id> --no-deliver
```

Enable lightweight bootstrap context for an isolated job:

```bash
openclaw cron edit <job-id> --light-context
```

Announce to a specific channel:

```bash
openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"
```

Create an isolated job with lightweight bootstrap context:

```bash
openclaw cron add \
  --name "Lightweight morning brief" \
  --cron "0 7 * * *" \
  --session isolated \
  --message "Summarize overnight updates." \
  --light-context \
  --no-deliver
```

`--light-context` applies to isolated agent-turn jobs only. For cron runs, lightweight mode keeps bootstrap context empty instead of injecting the full workspace bootstrap set.

Delivery ownership note:

- Cron-owned isolated jobs always route final user-visible delivery through the
  cron runner (`announce`, `webhook`, or internal-only `none`).
- If the task mentions messaging some external recipient, the agent should
  describe the intended destination in its result instead of trying to send it
  directly.

## Common admin commands

Manual run:

```bash
openclaw cron run <job-id>
openclaw cron run <job-id> --due
openclaw cron runs --id <job-id> --limit 50
```

Agent/session retargeting:

```bash
openclaw cron edit <job-id> --agent ops
openclaw cron edit <job-id> --clear-agent
openclaw cron edit <job-id> --session current
openclaw cron edit <job-id> --session "session:daily-brief"
```

Delivery tweaks:

```bash
openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"
openclaw cron edit <job-id> --best-effort-deliver
openclaw cron edit <job-id> --no-best-effort-deliver
openclaw cron edit <job-id> --no-deliver
```

Failure-delivery note:

- `delivery.failureDestination` is supported for isolated jobs.
- Main-session jobs may only use `delivery.failureDestination` when primary
  delivery mode is `webhook`.
- If you do not set any failure destination and the job already announces to a
  channel, failure notifications reuse that same announce target.

```

## File: daemon.md
```
---
summary: "CLI reference for `openclaw daemon` (legacy alias for gateway service management)"
read_when:
  - You still use `openclaw daemon ...` in scripts
  - You need service lifecycle commands (install/start/stop/restart/status)
title: "daemon"
---

# `openclaw daemon`

Legacy alias for Gateway service management commands.

`openclaw daemon ...` maps to the same service control surface as `openclaw gateway ...` service commands.

## Usage

```bash
openclaw daemon status
openclaw daemon install
openclaw daemon start
openclaw daemon stop
openclaw daemon restart
openclaw daemon uninstall
```

## Subcommands

- `status`: show service install state and probe Gateway health
- `install`: install service (`launchd`/`systemd`/`schtasks`)
- `uninstall`: remove service
- `start`: start service
- `stop`: stop service
- `restart`: restart service

## Common options

- `status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
- `install`: `--port`, `--runtime <node|bun>`, `--token`, `--force`, `--json`
- lifecycle (`uninstall|start|stop|restart`): `--json`

Notes:

- `status` resolves configured auth SecretRefs for probe auth when possible.
- If a required auth SecretRef is unresolved in this command path, `daemon status --json` reports `rpc.authWarning` when probe connectivity/auth fails; pass `--token`/`--password` explicitly or resolve the secret source first.
- If the probe succeeds, unresolved auth-ref warnings are suppressed to avoid false positives.
- `status --deep` adds a best-effort system-level service scan. When it finds other gateway-like services, human output prints cleanup hints and warns that one gateway per machine is still the normal recommendation.
- On Linux systemd installs, `status` token-drift checks include both `Environment=` and `EnvironmentFile=` unit sources.
- Drift checks resolve `gateway.auth.token` SecretRefs using merged runtime env (service command env first, then process env fallback).
- If token auth is not effectively active (explicit `gateway.auth.mode` of `password`/`none`/`trusted-proxy`, or mode unset where password can win and no token candidate can win), token-drift checks skip config token resolution.
- When token auth requires a token and `gateway.auth.token` is SecretRef-managed, `install` validates that the SecretRef is resolvable but does not persist the resolved token into service environment metadata.
- If token auth requires a token and the configured token SecretRef is unresolved, install fails closed.
- If both `gateway.auth.token` and `gateway.auth.password` are configured and `gateway.auth.mode` is unset, install is blocked until mode is set explicitly.

## Prefer

Use [`openclaw gateway`](/cli/gateway) for current docs and examples.

```

## File: dashboard.md
```
---
summary: "CLI reference for `openclaw dashboard` (open the Control UI)"
read_when:
  - You want to open the Control UI with your current token
  - You want to print the URL without launching a browser
title: "dashboard"
---

# `openclaw dashboard`

Open the Control UI using your current auth.

```bash
openclaw dashboard
openclaw dashboard --no-open
```

Notes:

- `dashboard` resolves configured `gateway.auth.token` SecretRefs when possible.
- For SecretRef-managed tokens (resolved or unresolved), `dashboard` prints/copies/opens a non-tokenized URL to avoid exposing external secrets in terminal output, clipboard history, or browser-launch arguments.
- If `gateway.auth.token` is SecretRef-managed but unresolved in this command path, the command prints a non-tokenized URL and explicit remediation guidance instead of embedding an invalid token placeholder.

```

## File: devices.md
```
---
summary: "CLI reference for `openclaw devices` (device pairing + token rotation/revocation)"
read_when:
  - You are approving device pairing requests
  - You need to rotate or revoke device tokens
title: "devices"
---

# `openclaw devices`

Manage device pairing requests and device-scoped tokens.

## Commands

### `openclaw devices list`

List pending pairing requests and paired devices.

```
openclaw devices list
openclaw devices list --json
```

Pending request output includes the requested role and scopes so approvals can
be reviewed before you approve.

### `openclaw devices remove <deviceId>`

Remove one paired device entry.

When you are authenticated with a paired device token, non-admin callers can
remove only **their own** device entry. Removing some other device requires
`operator.admin`.

```
openclaw devices remove <deviceId>
openclaw devices remove <deviceId> --json
```

### `openclaw devices clear --yes [--pending]`

Clear paired devices in bulk.

```
openclaw devices clear --yes
openclaw devices clear --yes --pending
openclaw devices clear --yes --pending --json
```

### `openclaw devices approve [requestId] [--latest]`

Approve a pending device pairing request. If `requestId` is omitted, OpenClaw
automatically approves the most recent pending request.

Note: if a device retries pairing with changed auth details (role/scopes/public
key), OpenClaw supersedes the previous pending entry and issues a new
`requestId`. Run `openclaw devices list` right before approval to use the
current ID.

```
openclaw devices approve
openclaw devices approve <requestId>
openclaw devices approve --latest
```

### `openclaw devices reject <requestId>`

Reject a pending device pairing request.

```
openclaw devices reject <requestId>
```

### `openclaw devices rotate --device <id> --role <role> [--scope <scope...>]`

Rotate a device token for a specific role (optionally updating scopes).
The target role must already exist in that device's approved pairing contract;
rotation cannot mint a new unapproved role.
If you omit `--scope`, later reconnects with the stored rotated token reuse that
token's cached approved scopes. If you pass explicit `--scope` values, those
become the stored scope set for future cached-token reconnects.
Non-admin paired-device callers can rotate only their **own** device token.
Also, any explicit `--scope` values must stay within the caller session's own
operator scopes; rotation cannot mint a broader operator token than the caller
already has.

```
openclaw devices rotate --device <deviceId> --role operator --scope operator.read --scope operator.write
```

Returns the new token payload as JSON.

### `openclaw devices revoke --device <id> --role <role>`

Revoke a device token for a specific role.

Non-admin paired-device callers can revoke only their **own** device token.
Revoking some other device's token requires `operator.admin`.

```
openclaw devices revoke --device <deviceId> --role node
```

Returns the revoke result as JSON.

## Common options

- `--url <url>`: Gateway WebSocket URL (defaults to `gateway.remote.url` when configured).
- `--token <token>`: Gateway token (if required).
- `--password <password>`: Gateway password (password auth).
- `--timeout <ms>`: RPC timeout.
- `--json`: JSON output (recommended for scripting).

Note: when you set `--url`, the CLI does not fall back to config or environment credentials.
Pass `--token` or `--password` explicitly. Missing explicit credentials is an error.

## Notes

- Token rotation returns a new token (sensitive). Treat it like a secret.
- These commands require `operator.pairing` (or `operator.admin`) scope.
- Token rotation stays inside the approved pairing role set and approved scope
  baseline for that device. A stray cached token entry does not grant a new
  rotate target.
- For paired-device token sessions, cross-device management is admin-only:
  `remove`, `rotate`, and `revoke` are self-only unless the caller has
  `operator.admin`.
- `devices clear` is intentionally gated by `--yes`.
- If pairing scope is unavailable on local loopback (and no explicit `--url` is passed), list/approve can use a local pairing fallback.
- `devices approve` picks the newest pending request automatically when you omit `requestId` or pass `--latest`.

## Token drift recovery checklist

Use this when Control UI or other clients keep failing with `AUTH_TOKEN_MISMATCH` or `AUTH_DEVICE_TOKEN_MISMATCH`.

1. Confirm current gateway token source:

```bash
openclaw config get gateway.auth.token
```

2. List paired devices and identify the affected device id:

```bash
openclaw devices list
```

3. Rotate operator token for the affected device:

```bash
openclaw devices rotate --device <deviceId> --role operator
```

4. If rotation is not enough, remove stale pairing and approve again:

```bash
openclaw devices remove <deviceId>
openclaw devices list
openclaw devices approve <requestId>
```

5. Retry client connection with the current shared token/password.

Notes:

- Normal reconnect auth precedence is explicit shared token/password first, then explicit `deviceToken`, then stored device token, then bootstrap token.
- Trusted `AUTH_TOKEN_MISMATCH` recovery can temporarily send both the shared token and the stored device token together for the one bounded retry.

Related:


```

## File: directory.md
```
---
summary: "CLI reference for `openclaw directory` (self, peers, groups)"
read_when:
  - You want to look up contacts/groups/self ids for a channel
  - You are developing a channel directory adapter
title: "directory"
---

# `openclaw directory`

Directory lookups for channels that support it (contacts/peers, groups, and “me”).

## Common flags

- `--channel <name>`: channel id/alias (required when multiple channels are configured; auto when only one is configured)
- `--account <id>`: account id (default: channel default)
- `--json`: output JSON

## Notes

- `directory` is meant to help you find IDs you can paste into other commands (especially `openclaw message send --target ...`).
- For many channels, results are config-backed (allowlists / configured groups) rather than a live provider directory.
- Default output is `id` (and sometimes `name`) separated by a tab; use `--json` for scripting.

## Using results with `message send`

```bash
openclaw directory peers list --channel slack --query "U0"
openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
```

## ID formats (by channel)

- WhatsApp: `+15551234567` (DM), `1234567890-1234567890@g.us` (group)
- Telegram: `@username` or numeric chat id; groups are numeric ids
- Slack: `user:U…` and `channel:C…`
- Discord: `user:<id>` and `channel:<id>`
- Matrix (plugin): `user:@user:server`, `room:!roomId:server`, or `#alias:server`
- Microsoft Teams (plugin): `user:<id>` and `conversation:<id>`
- Zalo (plugin): user id (Bot API)
- Zalo Personal / `zalouser` (plugin): thread id (DM/group) from `zca` (`me`, `friend list`, `group list`)

## Self ("me")

```bash
openclaw directory self --channel zalouser
```

## Peers (contacts/users)

```bash
openclaw directory peers list --channel zalouser
openclaw directory peers list --channel zalouser --query "name"
openclaw directory peers list --channel zalouser --limit 50
```

## Groups

```bash
openclaw directory groups list --channel zalouser
openclaw directory groups list --channel zalouser --query "work"
openclaw directory groups members --channel zalouser --group-id <id>
```

```

## File: dns.md
```
---
summary: "CLI reference for `openclaw dns` (wide-area discovery helpers)"
read_when:
  - You want wide-area discovery (DNS-SD) via Tailscale + CoreDNS
  - You’re setting up split DNS for a custom discovery domain (example: openclaw.internal)
title: "dns"
---

# `openclaw dns`

DNS helpers for wide-area discovery (Tailscale + CoreDNS). Currently focused on macOS + Homebrew CoreDNS.

Related:


## Setup

```bash
openclaw dns setup
openclaw dns setup --domain openclaw.internal
openclaw dns setup --apply
```

## `dns setup`

Plan or apply CoreDNS setup for unicast DNS-SD discovery.

Options:

- `--domain <domain>`: wide-area discovery domain (for example `openclaw.internal`)
- `--apply`: install or update CoreDNS config and restart the service (requires sudo; macOS only)

What it shows:

- resolved discovery domain
- zone file path
- current tailnet IPs
- recommended `openclaw.json` discovery config
- the Tailscale Split DNS nameserver/domain values to set

Notes:

- Without `--apply`, the command is a planning helper only and prints the recommended setup.
- If `--domain` is omitted, OpenClaw uses `discovery.wideArea.domain` from config.
- `--apply` currently supports macOS only and expects Homebrew CoreDNS.
- `--apply` bootstraps the zone file if needed, ensures the CoreDNS import stanza exists, and restarts the `coredns` brew service.

```

## File: docs.md
```
---
summary: "CLI reference for `openclaw docs` (search the live docs index)"
read_when:
  - You want to search the live OpenClaw docs from the terminal
title: "docs"
---

# `openclaw docs`

Search the live docs index.

Arguments:

- `[query...]`: search terms to send to the live docs index

Examples:

```bash
openclaw docs
openclaw docs browser existing-session
openclaw docs sandbox allowHostControl
openclaw docs gateway token secretref
```

Notes:

- With no query, `openclaw docs` opens the live docs search entrypoint.
- Multi-word queries are passed through as one search request.

```

## File: doctor.md
```
---
summary: "CLI reference for `openclaw doctor` (health checks + guided repairs)"
read_when:
  - You have connectivity/auth issues and want guided fixes
  - You updated and want a sanity check
title: "doctor"
---

# `openclaw doctor`

Health checks + quick fixes for the gateway and channels.

Related:


## Examples

```bash
openclaw doctor
openclaw doctor --repair
openclaw doctor --deep
openclaw doctor --repair --non-interactive
openclaw doctor --generate-gateway-token
```

## Options

- `--no-workspace-suggestions`: disable workspace memory/search suggestions
- `--yes`: accept defaults without prompting
- `--repair`: apply recommended repairs without prompting
- `--fix`: alias for `--repair`
- `--force`: apply aggressive repairs, including overwriting custom service config when needed
- `--non-interactive`: run without prompts; safe migrations only
- `--generate-gateway-token`: generate and configure a gateway token
- `--deep`: scan system services for extra gateway installs

Notes:

- Interactive prompts (like keychain/OAuth fixes) only run when stdin is a TTY and `--non-interactive` is **not** set. Headless runs (cron, Telegram, no terminal) will skip prompts.
- `--fix` (alias for `--repair`) writes a backup to `~/.openclaw/openclaw.json.bak` and drops unknown config keys, listing each removal.
- State integrity checks now detect orphan transcript files in the sessions directory and can archive them as `.deleted.<timestamp>` to reclaim space safely.
- Doctor also scans `~/.openclaw/cron/jobs.json` (or `cron.store`) for legacy cron job shapes and can rewrite them in place before the scheduler has to auto-normalize them at runtime.
- Doctor auto-migrates legacy flat Talk config (`talk.voiceId`, `talk.modelId`, and friends) into `talk.provider` + `talk.providers.<provider>`.
- Repeat `doctor --fix` runs no longer report/apply Talk normalization when the only difference is object key order.
- Doctor includes a memory-search readiness check and can recommend `openclaw configure --section model` when embedding credentials are missing.
- If sandbox mode is enabled but Docker is unavailable, doctor reports a high-signal warning with remediation (`install Docker` or `openclaw config set agents.defaults.sandbox.mode off`).
- If `gateway.auth.token`/`gateway.auth.password` are SecretRef-managed and unavailable in the current command path, doctor reports a read-only warning and does not write plaintext fallback credentials.
- If channel SecretRef inspection fails in a fix path, doctor continues and reports a warning instead of exiting early.
- Telegram `allowFrom` username auto-resolution (`doctor --fix`) requires a resolvable Telegram token in the current command path. If token inspection is unavailable, doctor reports a warning and skips auto-resolution for that pass.

## macOS: `launchctl` env overrides

If you previously ran `launchctl setenv OPENCLAW_GATEWAY_TOKEN ...` (or `...PASSWORD`), that value overrides your config file and can cause persistent “unauthorized” errors.

```bash
launchctl getenv OPENCLAW_GATEWAY_TOKEN
launchctl getenv OPENCLAW_GATEWAY_PASSWORD

launchctl unsetenv OPENCLAW_GATEWAY_TOKEN
launchctl unsetenv OPENCLAW_GATEWAY_PASSWORD
```

```

## File: flows.md
```
---
summary: "Redirect: flow commands live under `openclaw tasks flow`"
read_when:
  - You encounter openclaw flows in older docs or release notes
title: "flows (redirect)"
---

# `openclaw tasks flow`

Flow commands are subcommands of `openclaw tasks`, not a standalone `flows` command.

```bash
openclaw tasks flow list [--json]
openclaw tasks flow show <lookup>
openclaw tasks flow cancel <lookup>
```

For full documentation see [Task Flow](/automation/taskflow) and the [tasks CLI reference](/cli/index#tasks).

```

## File: gateway.md
```
---
summary: "OpenClaw Gateway CLI (`openclaw gateway`) — run, query, and discover gateways"
read_when:
  - Running the Gateway from the CLI (dev or servers)
  - Debugging Gateway auth, bind modes, and connectivity
  - Discovering gateways via Bonjour (local + wide-area DNS-SD)
title: "gateway"
---

# Gateway CLI

The Gateway is OpenClaw’s WebSocket server (channels, nodes, sessions, hooks).

Subcommands in this page live under `openclaw gateway …`.

Related docs:


## Run the Gateway

Run a local Gateway process:

```bash
openclaw gateway
```

Foreground alias:

```bash
openclaw gateway run
```

Notes:

- By default, the Gateway refuses to start unless `gateway.mode=local` is set in `~/.openclaw/openclaw.json`. Use `--allow-unconfigured` for ad-hoc/dev runs.
- `openclaw onboard --mode local` and `openclaw setup` are expected to write `gateway.mode=local`. If the file exists but `gateway.mode` is missing, treat that as a broken or clobbered config and repair it instead of assuming local mode implicitly.
- If the file exists and `gateway.mode` is missing, the Gateway treats that as suspicious config damage and refuses to “guess local” for you.
- Binding beyond loopback without auth is blocked (safety guardrail).
- `SIGUSR1` triggers an in-process restart when authorized (`commands.restart` is enabled by default; set `commands.restart: false` to block manual restart, while gateway tool/config apply/update remain allowed).
- `SIGINT`/`SIGTERM` handlers stop the gateway process, but they don’t restore any custom terminal state. If you wrap the CLI with a TUI or raw-mode input, restore the terminal before exit.

### Options

- `--port <port>`: WebSocket port (default comes from config/env; usually `18789`).
- `--bind <loopback|lan|tailnet|auto|custom>`: listener bind mode.
- `--auth <token|password>`: auth mode override.
- `--token <token>`: token override (also sets `OPENCLAW_GATEWAY_TOKEN` for the process).
- `--password <password>`: password override. Warning: inline passwords can be exposed in local process listings.
- `--password-file <path>`: read the gateway password from a file.
- `--tailscale <off|serve|funnel>`: expose the Gateway via Tailscale.
- `--tailscale-reset-on-exit`: reset Tailscale serve/funnel config on shutdown.
- `--allow-unconfigured`: allow gateway start without `gateway.mode=local` in config. This bypasses the startup guard for ad-hoc/dev bootstrap only; it does not write or repair the config file.
- `--dev`: create a dev config + workspace if missing (skips BOOTSTRAP.md).
- `--reset`: reset dev config + credentials + sessions + workspace (requires `--dev`).
- `--force`: kill any existing listener on the selected port before starting.
- `--verbose`: verbose logs.
- `--cli-backend-logs`: only show CLI backend logs in the console (and enable stdout/stderr).
- `--ws-log <auto|full|compact>`: websocket log style (default `auto`).
- `--compact`: alias for `--ws-log compact`.
- `--raw-stream`: log raw model stream events to jsonl.
- `--raw-stream-path <path>`: raw stream jsonl path.

## Query a running Gateway

All query commands use WebSocket RPC.

Output modes:

- Default: human-readable (colored in TTY).
- `--json`: machine-readable JSON (no styling/spinner).
- `--no-color` (or `NO_COLOR=1`): disable ANSI while keeping human layout.

Shared options (where supported):

- `--url <url>`: Gateway WebSocket URL.
- `--token <token>`: Gateway token.
- `--password <password>`: Gateway password.
- `--timeout <ms>`: timeout/budget (varies per command).
- `--expect-final`: wait for a “final” response (agent calls).

Note: when you set `--url`, the CLI does not fall back to config or environment credentials.
Pass `--token` or `--password` explicitly. Missing explicit credentials is an error.

### `gateway health`

```bash
openclaw gateway health --url ws://127.0.0.1:18789
```

### `gateway usage-cost`

Fetch usage-cost summaries from session logs.

```bash
openclaw gateway usage-cost
openclaw gateway usage-cost --days 7
openclaw gateway usage-cost --json
```

Options:

- `--days <days>`: number of days to include (default `30`).

### `gateway status`

`gateway status` shows the Gateway service (launchd/systemd/schtasks) plus an optional RPC probe.

```bash
openclaw gateway status
openclaw gateway status --json
openclaw gateway status --require-rpc
```

Options:

- `--url <url>`: add an explicit probe target. Configured remote + localhost are still probed.
- `--token <token>`: token auth for the probe.
- `--password <password>`: password auth for the probe.
- `--timeout <ms>`: probe timeout (default `10000`).
- `--no-probe`: skip the RPC probe (service-only view).
- `--deep`: scan system-level services too.
- `--require-rpc`: exit non-zero when the RPC probe fails. Cannot be combined with `--no-probe`.

Notes:

- `gateway status` stays available for diagnostics even when the local CLI config is missing or invalid.
- `gateway status` resolves configured auth SecretRefs for probe auth when possible.
- If a required auth SecretRef is unresolved in this command path, `gateway status --json` reports `rpc.authWarning` when probe connectivity/auth fails; pass `--token`/`--password` explicitly or resolve the secret source first.
- If the probe succeeds, unresolved auth-ref warnings are suppressed to avoid false positives.
- Use `--require-rpc` in scripts and automation when a listening service is not enough and you need the Gateway RPC itself to be healthy.
- `--deep` adds a best-effort scan for extra launchd/systemd/schtasks installs. When multiple gateway-like services are detected, human output prints cleanup hints and warns that most setups should run one gateway per machine.
- Human output includes the resolved file log path plus the CLI-vs-service config paths/validity snapshot to help diagnose profile or state-dir drift.
- On Linux systemd installs, service auth drift checks read both `Environment=` and `EnvironmentFile=` values from the unit (including `%h`, quoted paths, multiple files, and optional `-` files).
- Drift checks resolve `gateway.auth.token` SecretRefs using merged runtime env (service command env first, then process env fallback).
- If token auth is not effectively active (explicit `gateway.auth.mode` of `password`/`none`/`trusted-proxy`, or mode unset where password can win and no token candidate can win), token-drift checks skip config token resolution.

### `gateway probe`

`gateway probe` is the “debug everything” command. It always probes:

- your configured remote gateway (if set), and
- localhost (loopback) **even if remote is configured**.

If you pass `--url`, that explicit target is added ahead of both. Human output labels the
targets as:

- `URL (explicit)`
- `Remote (configured)` or `Remote (configured, inactive)`
- `Local loopback`

If multiple gateways are reachable, it prints all of them. Multiple gateways are supported when you use isolated profiles/ports (e.g., a rescue bot), but most installs still run a single gateway.

```bash
openclaw gateway probe
openclaw gateway probe --json
```

Interpretation:

- `Reachable: yes` means at least one target accepted a WebSocket connect.
- `RPC: ok` means detail RPC calls (`health`/`status`/`system-presence`/`config.get`) also succeeded.
- `RPC: limited - missing scope: operator.read` means connect succeeded but detail RPC is scope-limited. This is reported as **degraded** reachability, not full failure.
- Exit code is non-zero only when no probed target is reachable.

JSON notes (`--json`):

- Top level:
  - `ok`: at least one target is reachable.
  - `degraded`: at least one target had scope-limited detail RPC.
  - `primaryTargetId`: best target to treat as the active winner in this order: explicit URL, SSH tunnel, configured remote, then local loopback.
  - `warnings[]`: best-effort warning records with `code`, `message`, and optional `targetIds`.
  - `network`: local loopback/tailnet URL hints derived from current config and host networking.
  - `discovery.timeoutMs` and `discovery.count`: the actual discovery budget/result count used for this probe pass.
- Per target (`targets[].connect`):
  - `ok`: reachability after connect + degraded classification.
  - `rpcOk`: full detail RPC success.
  - `scopeLimited`: detail RPC failed due to missing operator scope.

Common warning codes:

- `ssh_tunnel_failed`: SSH tunnel setup failed; the command fell back to direct probes.
- `multiple_gateways`: more than one target was reachable; this is unusual unless you intentionally run isolated profiles, such as a rescue bot.
- `auth_secretref_unresolved`: a configured auth SecretRef could not be resolved for a failed target.
- `probe_scope_limited`: WebSocket connect succeeded, but detail RPC was limited by missing `operator.read`.

#### Remote over SSH (Mac app parity)

The macOS app “Remote over SSH” mode uses a local port-forward so the remote gateway (which may be bound to loopback only) becomes reachable at `ws://127.0.0.1:<port>`.

CLI equivalent:

```bash
openclaw gateway probe --ssh user@gateway-host
```

Options:

- `--ssh <target>`: `user@host` or `user@host:port` (port defaults to `22`).
- `--ssh-identity <path>`: identity file.
- `--ssh-auto`: pick the first discovered gateway host as SSH target from the resolved
  discovery endpoint (`local.` plus the configured wide-area domain, if any). TXT-only
  hints are ignored.

Config (optional, used as defaults):

- `gateway.remote.sshTarget`
- `gateway.remote.sshIdentity`

### `gateway call <method>`

Low-level RPC helper.

```bash
openclaw gateway call status
openclaw gateway call logs.tail --params '{"sinceMs": 60000}'
```

Options:

- `--params <json>`: JSON object string for params (default `{}`)
- `--url <url>`
- `--token <token>`
- `--password <password>`
- `--timeout <ms>`
- `--expect-final`
- `--json`

Notes:

- `--params` must be valid JSON.
- `--expect-final` is mainly for agent-style RPCs that stream intermediate events before a final payload.

## Manage the Gateway service

```bash
openclaw gateway install
openclaw gateway start
openclaw gateway stop
openclaw gateway restart
openclaw gateway uninstall
```

Command options:

- `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
- `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--force`, `--json`
- `gateway uninstall|start|stop|restart`: `--json`

Notes:

- `gateway install` supports `--port`, `--runtime`, `--token`, `--force`, `--json`.
- When token auth requires a token and `gateway.auth.token` is SecretRef-managed, `gateway install` validates that the SecretRef is resolvable but does not persist the resolved token into service environment metadata.
- If token auth requires a token and the configured token SecretRef is unresolved, install fails closed instead of persisting fallback plaintext.
- For password auth on `gateway run`, prefer `OPENCLAW_GATEWAY_PASSWORD`, `--password-file`, or a SecretRef-backed `gateway.auth.password` over inline `--password`.
- In inferred auth mode, shell-only `OPENCLAW_GATEWAY_PASSWORD` does not relax install token requirements; use durable config (`gateway.auth.password` or config `env`) when installing a managed service.
- If both `gateway.auth.token` and `gateway.auth.password` are configured and `gateway.auth.mode` is unset, install is blocked until mode is set explicitly.
- Lifecycle commands accept `--json` for scripting.

## Discover gateways (Bonjour)

`gateway discover` scans for Gateway beacons (`_openclaw-gw._tcp`).

- Multicast DNS-SD: `local.`

Only gateways with Bonjour discovery enabled (default) advertise the beacon.

Wide-Area discovery records include (TXT):

- `role` (gateway role hint)
- `transport` (transport hint, e.g. `gateway`)
- `gatewayPort` (WebSocket port, usually `18789`)
- `sshPort` (optional; clients default SSH targets to `22` when it is absent)
- `tailnetDns` (MagicDNS hostname, when available)
- `gatewayTls` / `gatewayTlsSha256` (TLS enabled + cert fingerprint)
- `cliPath` (remote-install hint written to the wide-area zone)

### `gateway discover`

```bash
openclaw gateway discover
```

Options:

- `--timeout <ms>`: per-command timeout (browse/resolve); default `2000`.
- `--json`: machine-readable output (also disables styling/spinner).

Examples:

```bash
openclaw gateway discover --timeout 4000
openclaw gateway discover --json | jq '.beacons[].wsUrl'
```

Notes:

- The CLI scans `local.` plus the configured wide-area domain when one is enabled.
- `wsUrl` in JSON output is derived from the resolved service endpoint, not from TXT-only
  hints such as `lanHost` or `tailnetDns`.
- On `local.` mDNS, `sshPort` and `cliPath` are only broadcast when
  `discovery.mdns.mode` is `full`. Wide-area DNS-SD still writes `cliPath`; `sshPort`
  stays optional there too.

```

## File: health.md
```
---
summary: "CLI reference for `openclaw health` (gateway health snapshot via RPC)"
read_when:
  - You want to quickly check the running Gateway’s health
title: "health"
---

# `openclaw health`

Fetch health from the running Gateway.

Options:

- `--json`: machine-readable output
- `--timeout <ms>`: connection timeout in milliseconds (default `10000`)
- `--verbose`: verbose logging
- `--debug`: alias for `--verbose`

Examples:

```bash
openclaw health
openclaw health --json
openclaw health --timeout 2500
openclaw health --verbose
openclaw health --debug
```

Notes:

- Default `openclaw health` asks the running gateway for its health snapshot. When the
  gateway already has a fresh cached snapshot, it can return that cached payload and
  refresh in the background.
- `--verbose` forces a live probe, prints gateway connection details, and expands the
  human-readable output across all configured accounts and agents.
- Output includes per-agent session stores when multiple agents are configured.

```

## File: hooks.md
```
---
summary: "CLI reference for `openclaw hooks` (agent hooks)"
read_when:
  - You want to manage agent hooks
  - You want to inspect hook availability or enable workspace hooks
title: "hooks"
---

# `openclaw hooks`

Manage agent hooks (event-driven automations for commands like `/new`, `/reset`, and gateway startup).

Running `openclaw hooks` with no subcommand is equivalent to `openclaw hooks list`.

Related:


## List All Hooks

```bash
openclaw hooks list
```

List all discovered hooks from workspace, managed, extra, and bundled directories.

**Options:**

- `--eligible`: Show only eligible hooks (requirements met)
- `--json`: Output as JSON
- `-v, --verbose`: Show detailed information including missing requirements

**Example output:**

```
Hooks (4/4 ready)

Ready:
  🚀 boot-md ✓ - Run BOOT.md on gateway startup
  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap
  📝 command-logger ✓ - Log all command events to a centralized audit file
  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
```

**Example (verbose):**

```bash
openclaw hooks list --verbose
```

Shows missing requirements for ineligible hooks.

**Example (JSON):**

```bash
openclaw hooks list --json
```

Returns structured JSON for programmatic use.

## Get Hook Information

```bash
openclaw hooks info <name>
```

Show detailed information about a specific hook.

**Arguments:**

- `<name>`: Hook name or hook key (e.g., `session-memory`)

**Options:**

- `--json`: Output as JSON

**Example:**

```bash
openclaw hooks info session-memory
```

**Output:**

```
💾 session-memory ✓ Ready

Save session context to memory when /new or /reset command is issued

Details:
  Source: openclaw-bundled
  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md
  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts
  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory
  Events: command:new, command:reset

Requirements:
  Config: ✓ workspace.dir
```

## Check Hooks Eligibility

```bash
openclaw hooks check
```

Show summary of hook eligibility status (how many are ready vs. not ready).

**Options:**

- `--json`: Output as JSON

**Example output:**

```
Hooks Status

Total hooks: 4
Ready: 4
Not ready: 0
```

## Enable a Hook

```bash
openclaw hooks enable <name>
```

Enable a specific hook by adding it to your config (`~/.openclaw/openclaw.json` by default).

**Note:** Workspace hooks are disabled by default until enabled here or in config. Hooks managed by plugins show `plugin:<id>` in `openclaw hooks list` and can’t be enabled/disabled here. Enable/disable the plugin instead.

**Arguments:**

- `<name>`: Hook name (e.g., `session-memory`)

**Example:**

```bash
openclaw hooks enable session-memory
```

**Output:**

```
✓ Enabled hook: 💾 session-memory
```

**What it does:**

- Checks if hook exists and is eligible
- Updates `hooks.internal.entries.<name>.enabled = true` in your config
- Saves config to disk

If the hook came from `<workspace>/hooks/`, this opt-in step is required before
the Gateway will load it.

**After enabling:**

- Restart the gateway so hooks reload (menu bar app restart on macOS, or restart your gateway process in dev).

## Disable a Hook

```bash
openclaw hooks disable <name>
```

Disable a specific hook by updating your config.

**Arguments:**

- `<name>`: Hook name (e.g., `command-logger`)

**Example:**

```bash
openclaw hooks disable command-logger
```

**Output:**

```
⏸ Disabled hook: 📝 command-logger
```

**After disabling:**

- Restart the gateway so hooks reload

## Notes

- `openclaw hooks list --json`, `info --json`, and `check --json` write structured JSON directly to stdout.
- Plugin-managed hooks cannot be enabled or disabled here; enable or disable the owning plugin instead.

## Install Hook Packs

```bash
openclaw plugins install <package>        # ClawHub first, then npm
openclaw plugins install <package> --pin  # pin version
openclaw plugins install <path>           # local path
```

Install hook packs through the unified plugins installer.

`openclaw hooks install` still works as a compatibility alias, but it prints a
deprecation warning and forwards to `openclaw plugins install`.

Npm specs are **registry-only** (package name + optional **exact version** or
**dist-tag**). Git/URL/file specs and semver ranges are rejected. Dependency
installs run with `--ignore-scripts` for safety.

Bare specs and `@latest` stay on the stable track. If npm resolves either of
those to a prerelease, OpenClaw stops and asks you to opt in explicitly with a
prerelease tag such as `@beta`/`@rc` or an exact prerelease version.

**What it does:**

- Copies the hook pack into `~/.openclaw/hooks/<id>`
- Enables the installed hooks in `hooks.internal.entries.*`
- Records the install under `hooks.internal.installs`

**Options:**

- `-l, --link`: Link a local directory instead of copying (adds it to `hooks.internal.load.extraDirs`)
- `--pin`: Record npm installs as exact resolved `name@version` in `hooks.internal.installs`

**Supported archives:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Examples:**

```bash
# Local directory
openclaw plugins install ./my-hook-pack

# Local archive
openclaw plugins install ./my-hook-pack.zip

# NPM package
openclaw plugins install @openclaw/my-hook-pack

# Link a local directory without copying
openclaw plugins install -l ./my-hook-pack
```

Linked hook packs are treated as managed hooks from an operator-configured
directory, not as workspace hooks.

## Update Hook Packs

```bash
openclaw plugins update <id>
openclaw plugins update --all
```

Update tracked npm-based hook packs through the unified plugins updater.

`openclaw hooks update` still works as a compatibility alias, but it prints a
deprecation warning and forwards to `openclaw plugins update`.

**Options:**

- `--all`: Update all tracked hook packs
- `--dry-run`: Show what would change without writing

When a stored integrity hash exists and the fetched artifact hash changes,
OpenClaw prints a warning and asks for confirmation before proceeding. Use
global `--yes` to bypass prompts in CI/non-interactive runs.

## Bundled Hooks

### session-memory

Saves session context to memory when you issue `/new` or `/reset`.

**Enable:**

```bash
openclaw hooks enable session-memory
```

**Output:** `~/.openclaw/workspace/memory/YYYY-MM-DD-slug.md`

**See:** [session-memory documentation](/automation/hooks#session-memory)

### bootstrap-extra-files

Injects additional bootstrap files (for example monorepo-local `AGENTS.md` / `TOOLS.md`) during `agent:bootstrap`.

**Enable:**

```bash
openclaw hooks enable bootstrap-extra-files
```

**See:** [bootstrap-extra-files documentation](/automation/hooks#bootstrap-extra-files)

### command-logger

Logs all command events to a centralized audit file.

**Enable:**

```bash
openclaw hooks enable command-logger
```

**Output:** `~/.openclaw/logs/commands.log`

**View logs:**

```bash
# Recent commands
tail -n 20 ~/.openclaw/logs/commands.log

# Pretty-print
cat ~/.openclaw/logs/commands.log | jq .

# Filter by action
grep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
```

**See:** [command-logger documentation](/automation/hooks#command-logger)

### boot-md

Runs `BOOT.md` when the gateway starts (after channels start).

**Events**: `gateway:startup`

**Enable**:

```bash
openclaw hooks enable boot-md
```

**See:** [boot-md documentation](/automation/hooks#boot-md)

```

## File: index.md
```
---
summary: "OpenClaw CLI reference for `openclaw` commands, subcommands, and options"
read_when:
  - Adding or modifying CLI commands or options
  - Documenting new command surfaces
title: "CLI Reference"
---

# CLI reference

This page describes the current CLI behavior. If commands change, update this doc.

## Command pages


## Global flags

- `--dev`: isolate state under `~/.openclaw-dev` and shift default ports.
- `--profile <name>`: isolate state under `~/.openclaw-<name>`.
- `--container <name>`: target a named container for execution.
- `--no-color`: disable ANSI colors.
- `--update`: shorthand for `openclaw update` (source installs only).
- `-V`, `--version`, `-v`: print version and exit.

## Output styling

- ANSI colors and progress indicators only render in TTY sessions.
- OSC-8 hyperlinks render as clickable links in supported terminals; otherwise we fall back to plain URLs.
- `--json` (and `--plain` where supported) disables styling for clean output.
- `--no-color` disables ANSI styling; `NO_COLOR=1` is also respected.
- Long-running commands show a progress indicator (OSC 9;4 when supported).

## Color palette

OpenClaw uses a lobster palette for CLI output.

- `accent` (#FF5A2D): headings, labels, primary highlights.
- `accentBright` (#FF7A3D): command names, emphasis.
- `accentDim` (#D14A22): secondary highlight text.
- `info` (#FF8A5B): informational values.
- `success` (#2FBF71): success states.
- `warn` (#FFB020): warnings, fallbacks, attention.
- `error` (#E23D2D): errors, failures.
- `muted` (#8B7F77): de-emphasis, metadata.

Palette source of truth: `src/terminal/palette.ts` (the “lobster palette”).

## Command tree

```
openclaw [--dev] [--profile <name>] <command>
  setup
  onboard
  configure
  config
    get
    set
    unset
    file
    schema
    validate
  completion
  doctor
  dashboard
  backup
    create
    verify
  security
    audit
  secrets
    reload
    audit
    configure
    apply
  reset
  uninstall
  update
    wizard
    status
  channels
    list
    status
    capabilities
    resolve
    logs
    add
    remove
    login
    logout
  directory
    self
    peers list
    groups list|members
  skills
    search
    install
    update
    list
    info
    check
  plugins
    list
    inspect
    install
    uninstall
    update
    enable
    disable
    doctor
    marketplace list
  memory
    status
    index
    search
  wiki
    status
    doctor
    init
    ingest
    compile
    lint
    search
    get
    apply
    bridge import
    unsafe-local import
    obsidian status|search|open|command|daily
  message
    send
    broadcast
    poll
    react
    reactions
    read
    edit
    delete
    pin
    unpin
    pins
    permissions
    search
    thread create|list|reply
    emoji list|upload
    sticker send|upload
    role info|add|remove
    channel info|list
    member info
    voice status
    event list|create
    timeout
    kick
    ban
  agent
  agents
    list
    add
    delete
    bindings
    bind
    unbind
    set-identity
  acp
  mcp
    serve
    list
    show
    set
    unset
  status
  health
  sessions
    cleanup
  tasks
    list
    audit
    maintenance
    show
    notify
    cancel
    flow list|show|cancel
  gateway
    call
    usage-cost
    health
    status
    probe
    discover
    install
    uninstall
    start
    stop
    restart
    run
  daemon
    status
    install
    uninstall
    start
    stop
    restart
  logs
  system
    event
    heartbeat last|enable|disable
    presence
  models
    list
    status
    set
    set-image
    aliases list|add|remove
    fallbacks list|add|remove|clear
    image-fallbacks list|add|remove|clear
    scan
  infer (alias: capability)
    list
    inspect
    model run|list|inspect|providers|auth login|logout|status
    image generate|edit|describe|describe-many|providers
    audio transcribe|providers
    tts convert|voices|providers|status|enable|disable|set-provider
    video generate|describe|providers
    web search|fetch|providers
    embedding create|providers
    auth add|login|login-github-copilot|setup-token|paste-token
    auth order get|set|clear
  sandbox
    list
    recreate
    explain
  cron
    status
    list
    add
    edit
    rm
    enable
    disable
    runs
    run
  nodes
    status
    describe
    list
    pending
    approve
    reject
    rename
    invoke
    notify
    push
    canvas snapshot|present|hide|navigate|eval
    canvas a2ui push|reset
    camera list|snap|clip
    screen record
    location get
  devices
    list
    remove
    clear
    approve
    reject
    rotate
    revoke
  node
    run
    status
    install
    uninstall
    stop
    restart
  approvals
    get
    set
    allowlist add|remove
  browser
    status
    start
    stop
    reset-profile
    tabs
    open
    focus
    close
    profiles
    create-profile
    delete-profile
    screenshot
    snapshot
    navigate
    resize
    click
    type
    press
    hover
    drag
    select
    upload
    fill
    dialog
    wait
    evaluate
    console
    pdf
  hooks
    list
    info
    check
    enable
    disable
    install
    update
  webhooks
    gmail setup|run
  pairing
    list
    approve
  qr
  clawbot
    qr
  docs
  dns
    setup
  tui
```

Note: plugins can add additional top-level commands (for example `openclaw voicecall`).

## Security

- `openclaw security audit` — audit config + local state for common security foot-guns.
- `openclaw security audit --deep` — best-effort live Gateway probe.
- `openclaw security audit --fix` — tighten safe defaults and state/config permissions.

## Secrets

### `secrets`

Manage SecretRefs and related runtime/config hygiene.

Subcommands:

- `secrets reload`
- `secrets audit`
- `secrets configure`
- `secrets apply --from <path>`

`secrets reload` options:

- `--url`, `--token`, `--timeout`, `--expect-final`, `--json`

`secrets audit` options:

- `--check`
- `--allow-exec`
- `--json`

`secrets configure` options:

- `--apply`
- `--yes`
- `--providers-only`
- `--skip-provider-setup`
- `--agent <id>`
- `--allow-exec`
- `--plan-out <path>`
- `--json`

`secrets apply --from <path>` options:

- `--dry-run`
- `--allow-exec`
- `--json`

Notes:

- `reload` is a Gateway RPC and keeps the last-known-good runtime snapshot when resolution fails.
- `audit --check` returns non-zero on findings; unresolved refs use a higher-priority non-zero exit code.
- Dry-run exec checks are skipped by default; use `--allow-exec` to opt in.

## Plugins

Manage extensions and their config:

- `openclaw plugins list` — discover plugins (use `--json` for machine output).
- `openclaw plugins inspect <id>` — show details for a plugin (`info` is an alias).
- `openclaw plugins install <path|.tgz|npm-spec|plugin@marketplace>` — install a plugin (or add a plugin path to `plugins.load.paths`; use `--force` to overwrite an existing install target).
- `openclaw plugins marketplace list <marketplace>` — list marketplace entries before install.
- `openclaw plugins enable <id>` / `disable <id>` — toggle `plugins.entries.<id>.enabled`.
- `openclaw plugins doctor` — report plugin load errors.

Most plugin changes require a gateway restart. See [/plugin](/tools/plugin).

## Memory

Vector search over `MEMORY.md` + `memory/*.md`:

- `openclaw memory status` — show index stats; use `--deep` for vector + embedding readiness checks or `--fix` to repair stale recall/promotion artifacts.
- `openclaw memory index` — reindex memory files.
- `openclaw memory search "<query>"` (or `--query "<query>"`) — semantic search over memory.
- `openclaw memory promote` — rank short-term recalls and optionally append top entries into `MEMORY.md`.

## Sandbox

Manage sandbox runtimes for isolated agent execution. See [/cli/sandbox](/cli/sandbox).

Subcommands:

- `sandbox list [--browser] [--json]`
- `sandbox recreate [--all] [--session <key>] [--agent <id>] [--browser] [--force]`
- `sandbox explain [--session <key>] [--agent <id>] [--json]`

Notes:

- `sandbox recreate` removes existing runtimes so the next use seeds them again with current config.
- For `ssh` and OpenShell `remote` backends, recreate deletes the canonical remote workspace for the selected scope.

## Chat slash commands

Chat messages support `/...` commands (text and native). See [/tools/slash-commands](/tools/slash-commands).

Highlights:

- `/status` for quick diagnostics.
- `/config` for persisted config changes.
- `/debug` for runtime-only config overrides (memory, not disk; requires `commands.debug: true`).

## Setup + onboarding

### `completion`

Generate shell-completion scripts and optionally install them into your shell profile.

Options:

- `-s, --shell <zsh|bash|powershell|fish>`
- `-i, --install`
- `--write-state`
- `-y, --yes`

Notes:

- Without `--install` or `--write-state`, `completion` prints the script to stdout.
- `--install` writes an `OpenClaw Completion` block into your shell profile and points it at the cached script under the OpenClaw state directory.

### `setup`

Initialize config + workspace.

Options:

- `--workspace <dir>`: agent workspace path (default `~/.openclaw/workspace`).
- `--wizard`: run onboarding.
- `--non-interactive`: run onboarding without prompts.
- `--mode <local|remote>`: onboard mode.
- `--remote-url <url>`: remote Gateway URL.
- `--remote-token <token>`: remote Gateway token.

Onboarding auto-runs when any onboarding flags are present (`--non-interactive`, `--mode`, `--remote-url`, `--remote-token`).

### `onboard`

Interactive onboarding for gateway, workspace, and skills.

Options:

- `--workspace <dir>`
- `--reset` (reset config + credentials + sessions before onboarding)
- `--reset-scope <config|config+creds+sessions|full>` (default `config+creds+sessions`; use `full` to also remove workspace)
- `--non-interactive`
- `--mode <local|remote>`
- `--flow <quickstart|advanced|manual>` (manual is an alias for advanced)
- `--auth-choice <choice>` where `<choice>` is one of:
  `chutes`, `deepseek-api-key`, `openai-codex`, `openai-api-key`,
  `openrouter-api-key`, `kilocode-api-key`, `litellm-api-key`, `ai-gateway-api-key`,
  `cloudflare-ai-gateway-api-key`, `moonshot-api-key`, `moonshot-api-key-cn`,
  `kimi-code-api-key`, `synthetic-api-key`, `venice-api-key`, `together-api-key`,
  `huggingface-api-key`, `apiKey`, `gemini-api-key`, `google-gemini-cli`, `zai-api-key`,
  `zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`, `xiaomi-api-key`,
  `minimax-global-oauth`, `minimax-global-api`, `minimax-cn-oauth`, `minimax-cn-api`,
  `opencode-zen`, `opencode-go`, `github-copilot`, `copilot-proxy`, `xai-api-key`,
  `mistral-api-key`, `volcengine-api-key`, `byteplus-api-key`, `qianfan-api-key`,
  `qwen-standard-api-key-cn`, `qwen-standard-api-key`, `qwen-api-key-cn`, `qwen-api-key`,
  `modelstudio-standard-api-key-cn`, `modelstudio-standard-api-key`,
  `modelstudio-api-key-cn`, `modelstudio-api-key`, `custom-api-key`, `skip`
- Qwen note: `qwen-*` is the canonical auth-choice family. `modelstudio-*`
  ids remain accepted as legacy compatibility aliases only.
- `--secret-input-mode <plaintext|ref>` (default `plaintext`; use `ref` to store provider default env refs instead of plaintext keys)
- `--anthropic-api-key <key>`
- `--openai-api-key <key>`
- `--mistral-api-key <key>`
- `--openrouter-api-key <key>`
- `--ai-gateway-api-key <key>`
- `--moonshot-api-key <key>`
- `--kimi-code-api-key <key>`
- `--gemini-api-key <key>`
- `--zai-api-key <key>`
- `--minimax-api-key <key>`
- `--opencode-zen-api-key <key>`
- `--opencode-go-api-key <key>`
- `--custom-base-url <url>` (non-interactive; used with `--auth-choice custom-api-key`)
- `--custom-model-id <id>` (non-interactive; used with `--auth-choice custom-api-key`)
- `--custom-api-key <key>` (non-interactive; optional; used with `--auth-choice custom-api-key`; falls back to `CUSTOM_API_KEY` when omitted)
- `--custom-provider-id <id>` (non-interactive; optional custom provider id)
- `--custom-compatibility <openai|anthropic>` (non-interactive; optional; default `openai`)
- `--gateway-port <port>`
- `--gateway-bind <loopback|lan|tailnet|auto|custom>`
- `--gateway-auth <token|password>`
- `--gateway-token <token>`
- `--gateway-token-ref-env <name>` (non-interactive; store `gateway.auth.token` as an env SecretRef; requires that env var to be set; cannot be combined with `--gateway-token`)
- `--gateway-password <password>`
- `--remote-url <url>`
- `--remote-token <token>`
- `--tailscale <off|serve|funnel>`
- `--tailscale-reset-on-exit`
- `--install-daemon`
- `--no-install-daemon` (alias: `--skip-daemon`)
- `--daemon-runtime <node|bun>`
- `--skip-channels`
- `--skip-skills`
- `--skip-search`
- `--skip-health`
- `--skip-ui`
- `--cloudflare-ai-gateway-account-id <id>`
- `--cloudflare-ai-gateway-gateway-id <id>`
- `--node-manager <npm|pnpm|bun>` (setup/onboarding node manager for skills; pnpm recommended, bun also supported)
- `--json`

### `configure`

Interactive configuration wizard (models, channels, skills, gateway).

Options:

- `--section <section>` (repeatable; limit the wizard to specific sections)

### `config`

Non-interactive config helpers (get/set/unset/file/schema/validate). Running `openclaw config` with no
subcommand launches the wizard.

Subcommands:

- `config get <path>`: print a config value (dot/bracket path).
- `config set`: supports four assignment modes:
  - value mode: `config set <path> <value>` (JSON5-or-string parsing)
  - SecretRef builder mode: `config set <path> --ref-provider <provider> --ref-source <source> --ref-id <id>`
  - provider builder mode: `config set secrets.providers.<alias> --provider-source <env|file|exec> ...`
  - batch mode: `config set --batch-json '<json>'` or `config set --batch-file <path>`
- `config set --dry-run`: validate assignments without writing `openclaw.json` (exec SecretRef checks are skipped by default).
- `config set --allow-exec --dry-run`: opt in to exec SecretRef dry-run checks (may execute provider commands).
- `config set --dry-run --json`: emit machine-readable dry-run output (checks + completeness signal, operations, refs checked/skipped, errors).
- `config set --strict-json`: require JSON5 parsing for path/value input. `--json` remains a legacy alias for strict parsing outside dry-run output mode.
- `config unset <path>`: remove a value.
- `config file`: print the active config file path.
- `config schema`: print the generated JSON schema for `openclaw.json`, including propagated field `title` / `description` docs metadata across nested object, wildcard, array-item, and composition branches, plus best-effort live plugin/channel schema metadata.
- `config validate`: validate the current config against the schema without starting the gateway.
- `config validate --json`: emit machine-readable JSON output.

### `doctor`

Health checks + quick fixes (config + gateway + legacy services).

Options:

- `--no-workspace-suggestions`: disable workspace memory hints.
- `--yes`: accept defaults without prompting (headless).
- `--non-interactive`: skip prompts; apply safe migrations only.
- `--deep`: scan system services for extra gateway installs.
- `--repair` (alias: `--fix`): attempt automatic repairs for detected issues.
- `--force`: force repairs even when not strictly needed.
- `--generate-gateway-token`: generate a new gateway auth token.

### `dashboard`

Open the Control UI with your current token.

Options:

- `--no-open`: print the URL but do not launch a browser

Notes:

- For SecretRef-managed gateway tokens, `dashboard` prints or opens a non-tokenized URL instead of exposing the secret in terminal output or browser launch arguments.

### `update`

Update the installed CLI.

Root options:

- `--json`
- `--no-restart`
- `--dry-run`
- `--channel <stable|beta|dev>`
- `--tag <dist-tag|version|spec>`
- `--timeout <seconds>`
- `--yes`

Subcommands:

- `update status`
- `update wizard`

`update status` options:

- `--json`
- `--timeout <seconds>`

`update wizard` options:

- `--timeout <seconds>`

Notes:

- `openclaw --update` rewrites to `openclaw update`.

### `backup`

Create and verify local backup archives for OpenClaw state.

Subcommands:

- `backup create`
- `backup verify <archive>`

`backup create` options:

- `--output <path>`
- `--json`
- `--dry-run`
- `--verify`
- `--only-config`
- `--no-include-workspace`

`backup verify <archive>` options:

- `--json`

## Channel helpers

### `channels`

Manage chat channel accounts (WhatsApp/Telegram/Discord/Google Chat/Slack/Mattermost (plugin)/Signal/iMessage/Microsoft Teams).

Subcommands:

- `channels list`: show configured channels and auth profiles.
- `channels status`: check gateway reachability and channel health (`--probe` runs live per-account probe/audit checks when the gateway is reachable; if not, it falls back to config-only channel summaries. Use `openclaw health` or `openclaw status --deep` for broader gateway health probes).
- Tip: `channels status` prints warnings with suggested fixes when it can detect common misconfigurations (then points you to `openclaw doctor`).
- `channels logs`: show recent channel logs from the gateway log file.
- `channels add`: wizard-style setup when no flags are passed; flags switch to non-interactive mode.
  - When adding a non-default account to a channel still using single-account top-level config, OpenClaw promotes account-scoped values into the channel account map before writing the new account. Most channels use `accounts.default`; Matrix can preserve an existing matching named/default target instead.
  - Non-interactive `channels add` does not auto-create/upgrade bindings; channel-only bindings continue to match the default account.
- `channels remove`: disable by default; pass `--delete` to remove config entries without prompts.
- `channels login`: interactive channel login (WhatsApp Web only).
- `channels logout`: log out of a channel session (if supported).

Common options:

- `--channel <name>`: `whatsapp|telegram|discord|googlechat|slack|mattermost|signal|imessage|msteams`
- `--account <id>`: channel account id (default `default`)
- `--name <label>`: display name for the account

`channels login` options:

- `--channel <channel>` (default `whatsapp`; supports `whatsapp`/`web`)
- `--account <id>`
- `--verbose`

`channels logout` options:

- `--channel <channel>` (default `whatsapp`)
- `--account <id>`

`channels list` options:

- `--no-usage`: skip model provider usage/quota snapshots (OAuth/API-backed only).
- `--json`: output JSON (includes usage unless `--no-usage` is set).

`channels status` options:

- `--probe`
- `--timeout <ms>`
- `--json`

`channels capabilities` options:

- `--channel <name>`
- `--account <id>` (only with `--channel`)
- `--target <dest>`
- `--timeout <ms>`
- `--json`

`channels resolve` options:

- `<entries...>`
- `--channel <name>`
- `--account <id>`
- `--kind <auto|user|group>`
- `--json`

`channels logs` options:

- `--channel <name|all>` (default `all`)
- `--lines <n>` (default `200`)
- `--json`

Notes:

- `channels login` supports `--verbose`.
- `channels capabilities --account` only applies when `--channel` is set.
- `channels status --probe` can show transport state plus probe/audit results such as `works`, `probe failed`, `audit ok`, or `audit failed`, depending on channel support.

More detail: [/concepts/oauth](/concepts/oauth)

Examples:

```bash
openclaw channels add --channel telegram --account alerts --name "Alerts Bot" --token $TELEGRAM_BOT_TOKEN
openclaw channels add --channel discord --account work --name "Work Bot" --token $DISCORD_BOT_TOKEN
openclaw channels remove --channel discord --account work --delete
openclaw channels status --probe
openclaw status --deep
```

### `directory`

Look up self, peer, and group IDs for channels that expose a directory surface. See [`openclaw directory`](/cli/directory).

Common options:

- `--channel <name>`
- `--account <id>`
- `--json`

Subcommands:

- `directory self`
- `directory peers list [--query <text>] [--limit <n>]`
- `directory groups list [--query <text>] [--limit <n>]`
- `directory groups members --group-id <id> [--limit <n>]`

### `skills`

List and inspect available skills plus readiness info.

Subcommands:

- `skills search [query...]`: search ClawHub skills.
- `skills search --limit <n> --json`: cap search results or emit machine-readable output.
- `skills install <slug>`: install a skill from ClawHub into the active workspace.
- `skills install <slug> --version <version>`: install a specific ClawHub version.
- `skills install <slug> --force`: overwrite an existing workspace skill folder.
- `skills update <slug|--all>`: update tracked ClawHub skills.
- `skills list`: list skills (default when no subcommand).
- `skills list --json`: emit machine-readable skill inventory on stdout.
- `skills list --verbose`: include missing requirements in the table.
- `skills info <name>`: show details for one skill.
- `skills info <name> --json`: emit machine-readable details on stdout.
- `skills check`: summary of ready vs missing requirements.
- `skills check --json`: emit machine-readable readiness output on stdout.

Options:

- `--eligible`: show only ready skills.
- `--json`: output JSON (no styling).
- `-v`, `--verbose`: include missing requirements detail.

Tip: use `openclaw skills search`, `openclaw skills install`, and `openclaw skills update` for ClawHub-backed skills.

### `pairing`

Approve DM pairing requests across channels.

Subcommands:

- `pairing list [channel] [--channel <channel>] [--account <id>] [--json]`
- `pairing approve <channel> <code> [--account <id>] [--notify]`
- `pairing approve --channel <channel> [--account <id>] <code> [--notify]`

Notes:

- If exactly one pairing-capable channel is configured, `pairing approve <code>` is also allowed.
- `list` and `approve` both support `--account <id>` for multi-account channels.

### `devices`

Manage gateway device pairing entries and per-role device tokens.

Subcommands:

- `devices list [--json]`
- `devices approve [requestId] [--latest]`
- `devices reject <requestId>`
- `devices remove <deviceId>`
- `devices clear --yes [--pending]`
- `devices rotate --device <id> --role <role> [--scope <scope...>]`
- `devices revoke --device <id> --role <role>`

Notes:

- `devices list` and `devices approve` can fall back to local pairing files on local loopback when direct pairing scope is unavailable.
- `devices approve` auto-selects the newest pending request when no `requestId` is passed or `--latest` is set.
- Stored-token reconnects reuse the token's cached approved scopes; explicit
  `devices rotate --scope ...` updates that stored scope set for future
  cached-token reconnects.
- `devices rotate` and `devices revoke` return JSON payloads.

### `qr`

Generate a mobile pairing QR and setup code from the current Gateway config. See [`openclaw qr`](/cli/qr).

Options:

- `--remote`
- `--url <url>`
- `--public-url <url>`
- `--token <token>`
- `--password <password>`
- `--setup-code-only`
- `--no-ascii`
- `--json`

Notes:

- `--token` and `--password` are mutually exclusive.
- The setup code carries a short-lived bootstrap token, not the shared gateway token/password.
- Built-in bootstrap handoff keeps the primary node token at `scopes: []`.
- Any handed-off operator bootstrap token stays bounded to `operator.approvals`, `operator.read`, `operator.talk.secrets`, and `operator.write`.
- Bootstrap scope checks are role-prefixed, so that operator allowlist only satisfies operator requests; non-operator roles still need scopes under their own role prefix.
- `--remote` can use `gateway.remote.url` or the active Tailscale Serve/Funnel URL.
- After scanning, approve the request with `openclaw devices list` / `openclaw devices approve <requestId>`.

### `clawbot`

Legacy alias namespace. Currently supports `openclaw clawbot qr`, which maps to [`openclaw qr`](/cli/qr).

### `hooks`

Manage internal agent hooks.

Subcommands:

- `hooks list`
- `hooks info <name>`
- `hooks check`
- `hooks enable <name>`
- `hooks disable <name>`
- `hooks install <path-or-spec>` (deprecated alias for `openclaw plugins install`)
- `hooks update [id]` (deprecated alias for `openclaw plugins update`)

Common options:

- `--json`
- `--eligible`
- `-v`, `--verbose`

Notes:

- Plugin-managed hooks cannot be enabled or disabled through `openclaw hooks`; enable or disable the owning plugin instead.
- `hooks install` and `hooks update` still work as compatibility aliases, but they print deprecation warnings and forward to the plugin commands.

### `webhooks`

Webhook helpers. Current built-in surface is Gmail Pub/Sub setup + runner:

- `webhooks gmail setup`
- `webhooks gmail run`

### `webhooks gmail`

Gmail Pub/Sub hook setup + runner. See [Gmail Pub/Sub](/automation/cron-jobs#gmail-pubsub-integration).

Subcommands:

- `webhooks gmail setup` (requires `--account <email>`; supports `--project`, `--topic`, `--subscription`, `--label`, `--hook-url`, `--hook-token`, `--push-token`, `--bind`, `--port`, `--path`, `--include-body`, `--max-bytes`, `--renew-minutes`, `--tailscale`, `--tailscale-path`, `--tailscale-target`, `--push-endpoint`, `--json`)
- `webhooks gmail run` (runtime overrides for the same flags)

Notes:

- `setup` configures the Gmail watch plus the OpenClaw-facing push path.
- `run` starts the local Gmail watcher/renew loop with optional runtime overrides.

### `dns`

Wide-area discovery DNS helpers (CoreDNS + Tailscale). Current built-in surface:

- `dns setup [--domain <domain>] [--apply]`

### `dns setup`

Wide-area discovery DNS helper (CoreDNS + Tailscale). See [/gateway/discovery](/gateway/discovery).

Options:

- `--domain <domain>`
- `--apply`: install/update CoreDNS config (requires sudo; macOS only).

Notes:

- Without `--apply`, this is a planning helper that prints the recommended OpenClaw + Tailscale DNS config.
- `--apply` currently supports macOS with Homebrew CoreDNS only.

## Messaging + agent

### `message`

Unified outbound messaging + channel actions.

See: [/cli/message](/cli/message)

Subcommands:

- `message send|poll|react|reactions|read|edit|delete|pin|unpin|pins|permissions|search|timeout|kick|ban`
- `message thread <create|list|reply>`
- `message emoji <list|upload>`
- `message sticker <send|upload>`
- `message role <info|add|remove>`
- `message channel <info|list>`
- `message member info`
- `message voice status`
- `message event <list|create>`

Examples:

- `openclaw message send --target +15555550123 --message "Hi"`
- `openclaw message poll --channel discord --target channel:123 --poll-question "Snack?" --poll-option Pizza --poll-option Sushi`

### `agent`

Run one agent turn via the Gateway (or `--local` embedded).

Pass at least one session selector: `--to`, `--session-id`, or `--agent`.

Required:

- `-m, --message <text>`

Options:

- `-t, --to <dest>` (for session key and optional delivery)
- `--session-id <id>`
- `--agent <id>` (agent id; overrides routing bindings)
- `--thinking <off|minimal|low|medium|high|xhigh>` (provider support varies; not model-gated at CLI level)
- `--verbose <on|off>`
- `--channel <channel>` (delivery channel; omit to use the main session channel)
- `--reply-to <target>` (delivery target override, separate from session routing)
- `--reply-channel <channel>` (delivery channel override)
- `--reply-account <id>` (delivery account id override)
- `--local` (embedded run; plugin registry still preloads first)
- `--deliver`
- `--json`
- `--timeout <seconds>`

Notes:

- Gateway mode falls back to the embedded agent when the Gateway request fails.
- `--local` still preloads the plugin registry, so plugin-provided providers, tools, and channels remain available during embedded runs.
- `--channel`, `--reply-channel`, and `--reply-account` affect reply delivery, not routing.

### `agents`

Manage isolated agents (workspaces + auth + routing).

Running `openclaw agents` with no subcommand is equivalent to `openclaw agents list`.

#### `agents list`

List configured agents.

Options:

- `--json`
- `--bindings`

#### `agents add [name]`

Add a new isolated agent. Runs the guided wizard unless flags (or `--non-interactive`) are passed; `--workspace` is required in non-interactive mode.

Options:

- `--workspace <dir>`
- `--model <id>`
- `--agent-dir <dir>`
- `--bind <channel[:accountId]>` (repeatable)
- `--non-interactive`
- `--json`

Binding specs use `channel[:accountId]`. When `accountId` is omitted, OpenClaw may resolve account scope via channel defaults/plugin hooks; otherwise it is a channel binding without explicit account scope.
Passing any explicit add flags switches the command into the non-interactive path. `main` is reserved and cannot be used as the new agent id.

#### `agents bindings`

List routing bindings.

Options:

- `--agent <id>`
- `--json`

#### `agents bind`

Add routing bindings for an agent.

Options:

- `--agent <id>` (defaults to the current default agent)
- `--bind <channel[:accountId]>` (repeatable)
- `--json`

#### `agents unbind`

Remove routing bindings for an agent.

Options:

- `--agent <id>` (defaults to the current default agent)
- `--bind <channel[:accountId]>` (repeatable)
- `--all`
- `--json`

Use either `--all` or `--bind`, not both.

#### `agents delete <id>`

Delete an agent and prune its workspace + state.

Options:

- `--force`
- `--json`

Notes:

- `main` cannot be deleted.
- Without `--force`, interactive confirmation is required.

#### `agents set-identity`

Update an agent identity (name/theme/emoji/avatar).

Options:

- `--agent <id>`
- `--workspace <dir>`
- `--identity-file <path>`
- `--from-identity`
- `--name <name>`
- `--theme <theme>`
- `--emoji <emoji>`
- `--avatar <value>`
- `--json`

Notes:

- `--agent` or `--workspace` can be used to select the target agent.
- When no explicit identity fields are provided, the command reads `IDENTITY.md`.

### `acp`

Run the ACP bridge that connects IDEs to the Gateway.

Root options:

- `--url <url>`
- `--token <token>`
- `--token-file <path>`
- `--password <password>`
- `--password-file <path>`
- `--session <key>`
- `--session-label <label>`
- `--require-existing`
- `--reset-session`
- `--no-prefix-cwd`
- `--provenance <off|meta|meta+receipt>`
- `--verbose`

#### `acp client`

Interactive ACP client for bridge debugging.

Options:

- `--cwd <dir>`
- `--server <command>`
- `--server-args <args...>`
- `--server-verbose`
- `--verbose`

See [`acp`](/cli/acp) for full behavior, security notes, and examples.

### `mcp`

Manage saved MCP server definitions and expose OpenClaw channels over MCP stdio.

#### `mcp serve`

Expose routed OpenClaw channel conversations over MCP stdio.

Options:

- `--url <url>`
- `--token <token>`
- `--token-file <path>`
- `--password <password>`
- `--password-file <path>`
- `--claude-channel-mode <auto|on|off>`
- `--verbose`

#### `mcp list`

List saved MCP server definitions.

Options:

- `--json`

#### `mcp show [name]`

Show one saved MCP server definition or the full saved MCP server object.

Options:

- `--json`

#### `mcp set <name> <value>`

Save one MCP server definition from a JSON object.

#### `mcp unset <name>`

Remove one saved MCP server definition.

### `approvals`

Manage exec approvals. Alias: `exec-approvals`.

#### `approvals get`

Fetch the exec approvals snapshot and effective policy.

Options:

- `--node <node>`
- `--gateway`
- `--json`
- node RPC options from `openclaw nodes`

#### `approvals set`

Replace exec approvals with JSON from a file or stdin.

Options:

- `--node <node>`
- `--gateway`
- `--file <path>`
- `--stdin`
- `--json`
- node RPC options from `openclaw nodes`

#### `approvals allowlist add|remove`

Edit the per-agent exec allowlist.

Options:

- `--node <node>`
- `--gateway`
- `--agent <id>` (defaults to `*`)
- `--json`
- node RPC options from `openclaw nodes`

### `status`

Show linked session health and recent recipients.

Options:

- `--json`
- `--all` (full diagnosis; read-only, pasteable)
- `--deep` (ask the gateway for a live health probe, including channel probes when supported)
- `--usage` (show model provider usage/quota)
- `--timeout <ms>`
- `--verbose`
- `--debug` (alias for `--verbose`)

Notes:

- Overview includes Gateway + node host service status when available.
- `--usage` prints normalized provider usage windows as `X% left`.

### Usage tracking

OpenClaw can surface provider usage/quota when OAuth/API creds are available.

Surfaces:

- `/status` (adds a short provider usage line when available)
- `openclaw status --usage` (prints full provider breakdown)
- macOS menu bar (Usage section under Context)

Notes:

- Data comes directly from provider usage endpoints (no estimates).
- Human-readable output is normalized to `X% left` across providers.
- Providers with current usage windows: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi, and z.ai.
- MiniMax note: raw `usage_percent` / `usagePercent` means remaining quota, so OpenClaw inverts it before display; count-based fields still win when present. `model_remains` responses prefer the chat-model entry, derive the window label from timestamps when needed, and include the model name in the plan label.
- Usage auth comes from provider-specific hooks when available; otherwise OpenClaw falls back to matching OAuth/API-key credentials from auth profiles, env, or config. If none resolve, usage is hidden.

### `health`

Fetch health from the running Gateway.

Options:

- `--json`
- `--timeout <ms>`
- `--verbose` (force a live probe and print gateway connection details)
- `--debug` (alias for `--verbose`)

Notes:

- Default `health` can return a fresh cached gateway snapshot.
- `health --verbose` forces a live probe and expands human-readable output across all configured accounts and agents.

### `sessions`

List stored conversation sessions.

Options:

- `--json`
- `--verbose`
- `--store <path>`
- `--active <minutes>`
- `--agent <id>` (filter sessions by agent)
- `--all-agents` (show sessions across all agents)

Subcommands:

- `sessions cleanup` — remove expired or orphaned sessions

Notes:

- `sessions cleanup` also supports `--fix-missing` to prune entries whose transcript files are gone.

## Reset / Uninstall

### `reset`

Reset local config/state (keeps the CLI installed).

Options:

- `--scope <config|config+creds+sessions|full>`
- `--yes`
- `--non-interactive`
- `--dry-run`

Notes:

- `--non-interactive` requires `--scope` and `--yes`.

### `uninstall`

Uninstall the gateway service + local data (CLI remains).

Options:

- `--service`
- `--state`
- `--workspace`
- `--app`
- `--all`
- `--yes`
- `--non-interactive`
- `--dry-run`

Notes:

- `--non-interactive` requires `--yes` and explicit scopes (or `--all`).
- `--all` removes service, state, workspace, and app together.

### `tasks`

List and manage [background task](/automation/tasks) runs across agents.

- `tasks list` — show active and recent task runs
- `tasks show <id>` — show details for a specific task run
- `tasks notify <id>` — change notification policy for a task run
- `tasks cancel <id>` — cancel a running task
- `tasks audit` — surface operational issues (stale, lost, delivery failures)
- `tasks maintenance [--apply] [--json]` — preview or apply tasks and TaskFlow cleanup/reconciliation (ACP/subagent child sessions, active cron jobs, live CLI runs)
- `tasks flow list` — list active and recent Task Flow flows
- `tasks flow show <lookup>` — inspect a flow by id or lookup key
- `tasks flow cancel <lookup>` — cancel a running flow and its active tasks

### `flows`

Legacy docs shortcut. Flow commands live under `openclaw tasks flow`:

- `tasks flow list [--json]`
- `tasks flow show <lookup>`
- `tasks flow cancel <lookup>`

## Gateway

### `gateway`

Run the WebSocket Gateway.

Options:

- `--port <port>`
- `--bind <loopback|tailnet|lan|auto|custom>`
- `--token <token>`
- `--auth <token|password>`
- `--password <password>`
- `--password-file <path>`
- `--tailscale <off|serve|funnel>`
- `--tailscale-reset-on-exit`
- `--allow-unconfigured`
- `--dev`
- `--reset` (reset dev config + credentials + sessions + workspace)
- `--force` (kill existing listener on port)
- `--verbose`
- `--cli-backend-logs`
- `--ws-log <auto|full|compact>`
- `--compact` (alias for `--ws-log compact`)
- `--raw-stream`
- `--raw-stream-path <path>`

### `gateway service`

Manage the Gateway service (launchd/systemd/schtasks).

Subcommands:

- `gateway status` (probes the Gateway RPC by default)
- `gateway install` (service install)
- `gateway uninstall`
- `gateway start`
- `gateway stop`
- `gateway restart`

Notes:

- `gateway status` probes the Gateway RPC by default using the service’s resolved port/config (override with `--url/--token/--password`).
- `gateway status` supports `--no-probe`, `--deep`, `--require-rpc`, and `--json` for scripting.
- `gateway status` also surfaces legacy or extra gateway services when it can detect them (`--deep` adds system-level scans). Profile-named OpenClaw services are treated as first-class and aren't flagged as "extra".
- `gateway status` stays available for diagnostics even when the local CLI config is missing or invalid.
- `gateway status` prints the resolved file log path, the CLI-vs-service config paths/validity snapshot, and the resolved probe target URL.
- If gateway auth SecretRefs are unresolved in the current command path, `gateway status --json` reports `rpc.authWarning` only when probe connectivity/auth fails (warnings are suppressed when probe succeeds).
- On Linux systemd installs, status token-drift checks include both `Environment=` and `EnvironmentFile=` unit sources.
- `gateway install|uninstall|start|stop|restart` support `--json` for scripting (default output stays human-friendly).
- `gateway install` defaults to Node runtime; bun is **not recommended** (WhatsApp/Telegram bugs).
- `gateway install` options: `--port`, `--runtime`, `--token`, `--force`, `--json`.

### `daemon`

Legacy alias for the Gateway service-management commands. See [/cli/daemon](/cli/daemon).

Subcommands:

- `daemon status`
- `daemon install`
- `daemon uninstall`
- `daemon start`
- `daemon stop`
- `daemon restart`

Common options:

- `status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
- `install`: `--port`, `--runtime <node|bun>`, `--token`, `--force`, `--json`
- `uninstall|start|stop|restart`: `--json`

### `logs`

Tail Gateway file logs via RPC.

Options:

- `--limit <n>`: maximum number of log lines to return
- `--max-bytes <n>`: maximum bytes to read from the log file
- `--follow`: follow the log file (tail -f style)
- `--interval <ms>`: polling interval in ms when following
- `--local-time`: display timestamps in local time
- `--json`: emit line-delimited JSON
- `--plain`: disable structured formatting
- `--no-color`: disable ANSI colors
- `--url <url>`: explicit Gateway WebSocket URL
- `--token <token>`: Gateway token
- `--timeout <ms>`: Gateway RPC timeout
- `--expect-final`: wait for a final response when needed

Examples:

```bash
openclaw logs --follow
openclaw logs --limit 200
openclaw logs --plain
openclaw logs --json
openclaw logs --no-color
```

Notes:

- If you pass `--url`, the CLI does not auto-apply config or environment credentials.
- Local loopback pairing failures fall back to the configured local log file; explicit `--url` targets do not.

### `gateway <subcommand>`

Gateway CLI helpers (use `--url`, `--token`, `--password`, `--timeout`, `--expect-final` for RPC subcommands).
When you pass `--url`, the CLI does not auto-apply config or environment credentials.
Include `--token` or `--password` explicitly. Missing explicit credentials is an error.

Subcommands:

- `gateway call <method> [--params <json>] [--url <url>] [--token <token>] [--password <password>] [--timeout <ms>] [--expect-final] [--json]`
- `gateway health`
- `gateway status`
- `gateway probe`
- `gateway discover`
- `gateway install|uninstall|start|stop|restart`
- `gateway run`

Notes:

- `gateway status --deep` adds a system-level service scan. Use `gateway probe`,
  `health --verbose`, or top-level `status --deep` for deeper runtime probe detail.

Common RPCs:

- `config.schema.lookup` (inspect one config subtree with a shallow schema node, matched hint metadata, and immediate child summaries)
- `config.get` (read current config snapshot + hash)
- `config.set` (validate + write full config; use `baseHash` for optimistic concurrency)
- `config.apply` (validate + write config + restart + wake)
- `config.patch` (merge a partial update + restart + wake)
- `update.run` (run update + restart + wake)

Tip: when calling `config.set`/`config.apply`/`config.patch` directly, pass `baseHash` from
`config.get` if a config already exists.
Tip: for partial edits, inspect with `config.schema.lookup` first and prefer `config.patch`.
Tip: these config write RPCs preflight active SecretRef resolution for refs in the submitted config payload and reject writes when an effectively active submitted ref is unresolved.
Tip: the owner-only `gateway` runtime tool still refuses to rewrite `tools.exec.ask` or `tools.exec.security`; legacy `tools.bash.*` aliases normalize to the same protected exec paths.

## Models

See [/concepts/models](/concepts/models) for fallback behavior and scanning strategy.

Anthropic note: Anthropic staff told us OpenClaw-style Claude CLI usage is
allowed again, so OpenClaw treats Claude CLI reuse and `claude -p` usage as
sanctioned for this integration unless Anthropic publishes a new policy. For
production, prefer an Anthropic API key or another supported
subscription-style provider such as OpenAI Codex, Alibaba Cloud Model Studio
Coding Plan, MiniMax Coding Plan, or Z.AI / GLM Coding Plan.

Anthropic setup-token remains available as a supported token-auth path, but OpenClaw now prefers Claude CLI reuse and `claude -p` when available.

### `models` (root)

`openclaw models` is an alias for `models status`.

Root options:

- `--status-json` (alias for `models status --json`)
- `--status-plain` (alias for `models status --plain`)

### `models list`

Options:

- `--all`
- `--local`
- `--provider <name>`
- `--json`
- `--plain`

### `models status`

Options:

- `--json`
- `--plain`
- `--check` (exit 1=expired/missing, 2=expiring)
- `--probe` (live probe of configured auth profiles)
- `--probe-provider <name>`
- `--probe-profile <id>` (repeat or comma-separated)
- `--probe-timeout <ms>`
- `--probe-concurrency <n>`
- `--probe-max-tokens <n>`
- `--agent <id>`

Always includes the auth overview and OAuth expiry status for profiles in the auth store.
`--probe` runs live requests (may consume tokens and trigger rate limits).
Probe rows can come from auth profiles, env credentials, or `models.json`.
Expect probe statuses like `ok`, `auth`, `rate_limit`, `billing`, `timeout`,
`format`, `unknown`, and `no_model`.
When an explicit `auth.order.<provider>` omits a stored profile, probe reports
`excluded_by_auth_order` instead of silently trying that profile.

### `models set <model>`

Set `agents.defaults.model.primary`.

### `models set-image <model>`

Set `agents.defaults.imageModel.primary`.

### `models aliases list|add|remove`

Options:

- `list`: `--json`, `--plain`
- `add <alias> <model>`
- `remove <alias>`

### `models fallbacks list|add|remove|clear`

Options:

- `list`: `--json`, `--plain`
- `add <model>`
- `remove <model>`
- `clear`

### `models image-fallbacks list|add|remove|clear`

Options:

- `list`: `--json`, `--plain`
- `add <model>`
- `remove <model>`
- `clear`

### `models scan`

Options:

- `--min-params <b>`
- `--max-age-days <days>`
- `--provider <name>`
- `--max-candidates <n>`
- `--timeout <ms>`
- `--concurrency <n>`
- `--no-probe`
- `--yes`
- `--no-input`
- `--set-default`
- `--set-image`
- `--json`

### `models auth add|login|login-github-copilot|setup-token|paste-token`

Options:

- `add`: interactive auth helper (provider auth flow or token paste)
- `login`: `--provider <name>`, `--method <method>`, `--set-default`
- `login-github-copilot`: GitHub Copilot OAuth login flow (`--yes`)
- `setup-token`: `--provider <name>`, `--yes`
- `paste-token`: `--provider <name>`, `--profile-id <id>`, `--expires-in <duration>`

Notes:

- `setup-token` and `paste-token` are generic token commands for providers that expose token auth methods.
- `setup-token` requires an interactive TTY and runs the provider's token-auth method.
- `paste-token` prompts for the token value and defaults to auth profile id `<provider>:manual` when `--profile-id` is omitted.
- Anthropic `setup-token` / `paste-token` remain available as a supported OpenClaw token path, but OpenClaw now prefers Claude CLI reuse and `claude -p` when available.

### `models auth order get|set|clear`

Options:

- `get`: `--provider <name>`, `--agent <id>`, `--json`
- `set`: `--provider <name>`, `--agent <id>`, `<profileIds...>`
- `clear`: `--provider <name>`, `--agent <id>`

## System

### `system event`

Enqueue a system event and optionally trigger a heartbeat (Gateway RPC).

Required:

- `--text <text>`

Options:

- `--mode <now|next-heartbeat>`
- `--json`
- `--url`, `--token`, `--timeout`, `--expect-final`

### `system heartbeat last|enable|disable`

Heartbeat controls (Gateway RPC).

Options:

- `--json`
- `--url`, `--token`, `--timeout`, `--expect-final`

### `system presence`

List system presence entries (Gateway RPC).

Options:

- `--json`
- `--url`, `--token`, `--timeout`, `--expect-final`

## Cron

Manage scheduled jobs (Gateway RPC). See [/automation/cron-jobs](/automation/cron-jobs).

Subcommands:

- `cron status [--json]`
- `cron list [--all] [--json]` (table output by default; use `--json` for raw)
- `cron add` (alias: `create`; requires `--name` and exactly one of `--at` | `--every` | `--cron`, and exactly one payload of `--system-event` | `--message`)
- `cron edit <id>` (patch fields)
- `cron rm <id>` (aliases: `remove`, `delete`)
- `cron enable <id>`
- `cron disable <id>`
- `cron runs --id <id> [--limit <n>]`
- `cron run <id> [--due]`

All `cron` commands accept `--url`, `--token`, `--timeout`, `--expect-final`.

`cron add|edit --model ...` uses that selected allowed model for the job. If
the model is not allowed, cron warns and falls back to the job's agent/default
model selection instead. Configured fallback chains still apply, but a plain
model override with no explicit per-job fallback list no longer appends the
agent primary as a hidden extra retry target.

## Node host

### `node`

`node` runs a **headless node host** or manages it as a background service. See
[`openclaw node`](/cli/node).

Subcommands:

- `node run --host <gateway-host> --port 18789`
- `node status`
- `node install [--host <gateway-host>] [--port <port>] [--tls] [--tls-fingerprint <sha256>] [--node-id <id>] [--display-name <name>] [--runtime <node|bun>] [--force]`
- `node uninstall`
- `node stop`
- `node restart`

Auth notes:

- `node` resolves gateway auth from env/config (no `--token`/`--password` flags): `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`, then `gateway.auth.*`. In local mode, node host intentionally ignores `gateway.remote.*`; in `gateway.mode=remote`, `gateway.remote.*` participates per remote precedence rules.
- Node-host auth resolution only honors `OPENCLAW_GATEWAY_*` env vars.

## Nodes

`nodes` talks to the Gateway and targets paired nodes. See [/nodes](/nodes).

Common options:

- `--url`, `--token`, `--timeout`, `--json`

Subcommands:

- `nodes status [--connected] [--last-connected <duration>]`
- `nodes describe --node <id|name|ip>`
- `nodes list [--connected] [--last-connected <duration>]`
- `nodes pending`
- `nodes approve <requestId>`
- `nodes reject <requestId>`
- `nodes rename --node <id|name|ip> --name <displayName>`
- `nodes invoke --node <id|name|ip> --command <command> [--params <json>] [--invoke-timeout <ms>] [--idempotency-key <key>]`
- `nodes notify --node <id|name|ip> [--title <text>] [--body <text>] [--sound <name>] [--priority <passive|active|timeSensitive>] [--delivery <system|overlay|auto>] [--invoke-timeout <ms>]` (mac only)

Camera:

- `nodes camera list --node <id|name|ip>`
- `nodes camera snap --node <id|name|ip> [--facing front|back|both] [--device-id <id>] [--max-width <px>] [--quality <0-1>] [--delay-ms <ms>] [--invoke-timeout <ms>]`
- `nodes camera clip --node <id|name|ip> [--facing front|back] [--device-id <id>] [--duration <ms|10s|1m>] [--no-audio] [--invoke-timeout <ms>]`

Canvas + screen:

- `nodes canvas snapshot --node <id|name|ip> [--format png|jpg|jpeg] [--max-width <px>] [--quality <0-1>] [--invoke-timeout <ms>]`
- `nodes canvas present --node <id|name|ip> [--target <urlOrPath>] [--x <px>] [--y <px>] [--width <px>] [--height <px>] [--invoke-timeout <ms>]`
- `nodes canvas hide --node <id|name|ip> [--invoke-timeout <ms>]`
- `nodes canvas navigate <url> --node <id|name|ip> [--invoke-timeout <ms>]`
- `nodes canvas eval [<js>] --node <id|name|ip> [--js <code>] [--invoke-timeout <ms>]`
- `nodes canvas a2ui push --node <id|name|ip> (--jsonl <path> | --text <text>) [--invoke-timeout <ms>]`
- `nodes canvas a2ui reset --node <id|name|ip> [--invoke-timeout <ms>]`
- `nodes screen record --node <id|name|ip> [--screen <index>] [--duration <ms|10s>] [--fps <n>] [--no-audio] [--out <path>] [--invoke-timeout <ms>]`

Location:

- `nodes location get --node <id|name|ip> [--max-age <ms>] [--accuracy <coarse|balanced|precise>] [--location-timeout <ms>] [--invoke-timeout <ms>]`

## Browser

Browser control CLI (dedicated Chrome/Brave/Edge/Chromium). See [`openclaw browser`](/cli/browser) and the [Browser tool](/tools/browser).

Common options:

- `--url`, `--token`, `--timeout`, `--expect-final`, `--json`
- `--browser-profile <name>`

Manage:

- `browser status`
- `browser start`
- `browser stop`
- `browser reset-profile`
- `browser tabs`
- `browser open <url>`
- `browser focus <targetId>`
- `browser close [targetId]`
- `browser profiles`
- `browser create-profile --name <name> [--color <hex>] [--cdp-url <url>] [--driver existing-session] [--user-data-dir <path>]`
- `browser delete-profile --name <name>`

Inspect:

- `browser screenshot [targetId] [--full-page] [--ref <ref>] [--element <selector>] [--type png|jpeg]`
- `browser snapshot [--format aria|ai] [--target-id <id>] [--limit <n>] [--interactive] [--compact] [--depth <n>] [--selector <sel>] [--out <path>]`

Actions:

- `browser navigate <url> [--target-id <id>]`
- `browser resize <width> <height> [--target-id <id>]`
- `browser click <ref> [--double] [--button <left|right|middle>] [--modifiers <csv>] [--target-id <id>]`
- `browser type <ref> <text> [--submit] [--slowly] [--target-id <id>]`
- `browser press <key> [--target-id <id>]`
- `browser hover <ref> [--target-id <id>]`
- `browser drag <startRef> <endRef> [--target-id <id>]`
- `browser select <ref> <values...> [--target-id <id>]`
- `browser upload <paths...> [--ref <ref>] [--input-ref <ref>] [--element <selector>] [--target-id <id>] [--timeout-ms <ms>]`
- `browser fill [--fields <json>] [--fields-file <path>] [--target-id <id>]`
- `browser dialog --accept|--dismiss [--prompt <text>] [--target-id <id>] [--timeout-ms <ms>]`
- `browser wait [--time <ms>] [--text <value>] [--text-gone <value>] [--target-id <id>]`
- `browser evaluate --fn <code> [--ref <ref>] [--target-id <id>]`
- `browser console [--level <error|warn|info>] [--target-id <id>]`
- `browser pdf [--target-id <id>]`

## Voice call

### `voicecall`

Plugin-provided voice-call utilities. Only appears when the voice-call plugin is installed and enabled. See [`openclaw voicecall`](/cli/voicecall).

Common commands:

- `voicecall call --to <phone> --message <text> [--mode notify|conversation]`
- `voicecall start --to <phone> [--message <text>] [--mode notify|conversation]`
- `voicecall continue --call-id <id> --message <text>`
- `voicecall speak --call-id <id> --message <text>`
- `voicecall end --call-id <id>`
- `voicecall status --call-id <id>`
- `voicecall tail [--file <path>] [--since <n>] [--poll <ms>]`
- `voicecall latency [--file <path>] [--last <n>]`
- `voicecall expose [--mode off|serve|funnel] [--path <path>] [--port <port>] [--serve-path <path>]`

## Docs search

### `docs`

Search the live OpenClaw docs index.

### `docs [query...]`

Search the live docs index.

## TUI

### `tui`

Open the terminal UI connected to the Gateway.

Options:

- `--url <url>`
- `--token <token>`
- `--password <password>`
- `--session <key>`
- `--deliver`
- `--thinking <level>`
- `--message <text>`
- `--timeout-ms <ms>` (defaults to `agents.defaults.timeoutSeconds`)
- `--history-limit <n>`

```

## File: infer.md
```
---
summary: "Infer-first CLI for provider-backed model, image, audio, TTS, video, web, and embedding workflows"
read_when:
  - Adding or modifying `openclaw infer` commands
  - Designing stable headless capability automation
title: "Inference CLI"
---

# Inference CLI

`openclaw infer` is the canonical headless surface for provider-backed inference workflows.

It intentionally exposes capability families, not raw gateway RPC names and not raw agent tool ids.

## Turn infer into a skill

Copy and paste this to an agent:

```text
Read https://docs.openclaw.ai/cli/infer, then create a skill that routes my common workflows to `openclaw infer`.
Focus on model runs, image generation, video generation, audio transcription, TTS, web search, and embeddings.
```

A good infer-based skill should:

- map common user intents to the correct infer subcommand
- include a few canonical infer examples for the workflows it covers
- prefer `openclaw infer ...` in examples and suggestions
- avoid re-documenting the entire infer surface inside the skill body

Typical infer-focused skill coverage:

- `openclaw infer model run`
- `openclaw infer image generate`
- `openclaw infer audio transcribe`
- `openclaw infer tts convert`
- `openclaw infer web search`
- `openclaw infer embedding create`

## Why use infer

`openclaw infer` provides one consistent CLI for provider-backed inference tasks inside OpenClaw.

Benefits:

- Use the providers and models already configured in OpenClaw instead of wiring up one-off wrappers for each backend.
- Keep model, image, audio transcription, TTS, video, web, and embedding workflows under one command tree.
- Use a stable `--json` output shape for scripts, automation, and agent-driven workflows.
- Prefer a first-party OpenClaw surface when the task is fundamentally "run inference."
- Use the normal local path without requiring the gateway for most infer commands.

## Command tree

```text
 openclaw infer
  list
  inspect

  model
    run
    list
    inspect
    providers
    auth login
    auth logout
    auth status

  image
    generate
    edit
    describe
    describe-many
    providers

  audio
    transcribe
    providers

  tts
    convert
    voices
    providers
    status
    enable
    disable
    set-provider

  video
    generate
    describe
    providers

  web
    search
    fetch
    providers

  embedding
    create
    providers
```

## Common tasks

This table maps common inference tasks to the corresponding infer command.

| Task                    | Command                                                                | Notes                                                |
| ----------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------- |
| Run a text/model prompt | `openclaw infer model run --prompt "..." --json`                       | Uses the normal local path by default                |
| Generate an image       | `openclaw infer image generate --prompt "..." --json`                  | Use `image edit` when starting from an existing file |
| Describe an image file  | `openclaw infer image describe --file ./image.png --json`              | `--model` must be `<provider/model>`                 |
| Transcribe audio        | `openclaw infer audio transcribe --file ./memo.m4a --json`             | `--model` must be `<provider/model>`                 |
| Synthesize speech       | `openclaw infer tts convert --text "..." --output ./speech.mp3 --json` | `tts status` is gateway-oriented                     |
| Generate a video        | `openclaw infer video generate --prompt "..." --json`                  |                                                      |
| Describe a video file   | `openclaw infer video describe --file ./clip.mp4 --json`               | `--model` must be `<provider/model>`                 |
| Search the web          | `openclaw infer web search --query "..." --json`                       |                                                      |
| Fetch a web page        | `openclaw infer web fetch --url https://example.com --json`            |                                                      |
| Create embeddings       | `openclaw infer embedding create --text "..." --json`                  |                                                      |

## Behavior

- `openclaw infer ...` is the primary CLI surface for these workflows.
- Use `--json` when the output will be consumed by another command or script.
- Use `--provider` or `--model provider/model` when a specific backend is required.
- For `image describe`, `audio transcribe`, and `video describe`, `--model` must use the form `<provider/model>`.
- Stateless execution commands default to local.
- Gateway-managed state commands default to gateway.
- The normal local path does not require the gateway to be running.

## Model

Use `model` for provider-backed text inference and model/provider inspection.

```bash
openclaw infer model run --prompt "Reply with exactly: smoke-ok" --json
openclaw infer model run --prompt "Summarize this changelog entry" --provider openai --json
openclaw infer model providers --json
openclaw infer model inspect --name gpt-5.4 --json
```

Notes:

- `model run` reuses the agent runtime so provider/model overrides behave like normal agent execution.
- `model auth login`, `model auth logout`, and `model auth status` manage saved provider auth state.

## Image

Use `image` for generation, edit, and description.

```bash
openclaw infer image generate --prompt "friendly lobster illustration" --json
openclaw infer image generate --prompt "cinematic product photo of headphones" --json
openclaw infer image describe --file ./photo.jpg --json
openclaw infer image describe --file ./ui-screenshot.png --model openai/gpt-4.1-mini --json
```

Notes:

- Use `image edit` when starting from existing input files.
- For `image describe`, `--model` must be `<provider/model>`.

## Audio

Use `audio` for file transcription.

```bash
openclaw infer audio transcribe --file ./memo.m4a --json
openclaw infer audio transcribe --file ./team-sync.m4a --language en --prompt "Focus on names and action items" --json
openclaw infer audio transcribe --file ./memo.m4a --model openai/whisper-1 --json
```

Notes:

- `audio transcribe` is for file transcription, not realtime session management.
- `--model` must be `<provider/model>`.

## TTS

Use `tts` for speech synthesis and TTS provider state.

```bash
openclaw infer tts convert --text "hello from openclaw" --output ./hello.mp3 --json
openclaw infer tts convert --text "Your build is complete" --output ./build-complete.mp3 --json
openclaw infer tts providers --json
openclaw infer tts status --json
```

Notes:

- `tts status` defaults to gateway because it reflects gateway-managed TTS state.
- Use `tts providers`, `tts voices`, and `tts set-provider` to inspect and configure TTS behavior.

## Video

Use `video` for generation and description.

```bash
openclaw infer video generate --prompt "cinematic sunset over the ocean" --json
openclaw infer video generate --prompt "slow drone shot over a forest lake" --json
openclaw infer video describe --file ./clip.mp4 --json
openclaw infer video describe --file ./clip.mp4 --model openai/gpt-4.1-mini --json
```

Notes:

- `--model` must be `<provider/model>` for `video describe`.

## Web

Use `web` for search and fetch workflows.

```bash
openclaw infer web search --query "OpenClaw docs" --json
openclaw infer web search --query "OpenClaw infer web providers" --json
openclaw infer web fetch --url https://docs.openclaw.ai/cli/infer --json
openclaw infer web providers --json
```

Notes:

- Use `web providers` to inspect available, configured, and selected providers.

## Embedding

Use `embedding` for vector creation and embedding provider inspection.

```bash
openclaw infer embedding create --text "friendly lobster" --json
openclaw infer embedding create --text "customer support ticket: delayed shipment" --model openai/text-embedding-3-large --json
openclaw infer embedding providers --json
```

## JSON output

Infer commands normalize JSON output under a shared envelope:

```json
{
  "ok": true,
  "capability": "image.generate",
  "transport": "local",
  "provider": "openai",
  "model": "gpt-image-1",
  "attempts": [],
  "outputs": []
}
```

Top-level fields are stable:

- `ok`
- `capability`
- `transport`
- `provider`
- `model`
- `attempts`
- `outputs`
- `error`

## Common pitfalls

```bash
# Bad
openclaw infer media image generate --prompt "friendly lobster"

# Good
openclaw infer image generate --prompt "friendly lobster"
```

```bash
# Bad
openclaw infer audio transcribe --file ./memo.m4a --model whisper-1 --json

# Good
openclaw infer audio transcribe --file ./memo.m4a --model openai/whisper-1 --json
```

## Notes

- `openclaw capability ...` is an alias for `openclaw infer ...`.

```

## File: logs.md
```
---
summary: "CLI reference for `openclaw logs` (tail gateway logs via RPC)"
read_when:
  - You need to tail Gateway logs remotely (without SSH)
  - You want JSON log lines for tooling
title: "logs"
---

# `openclaw logs`

Tail Gateway file logs over RPC (works in remote mode).

Related:


## Options

- `--limit <n>`: maximum number of log lines to return (default `200`)
- `--max-bytes <n>`: maximum bytes to read from the log file (default `250000`)
- `--follow`: follow the log stream
- `--interval <ms>`: polling interval while following (default `1000`)
- `--json`: emit line-delimited JSON events
- `--plain`: plain text output without styled formatting
- `--no-color`: disable ANSI colors
- `--local-time`: render timestamps in your local timezone

## Shared Gateway RPC options

`openclaw logs` also accepts the standard Gateway client flags:

- `--url <url>`: Gateway WebSocket URL
- `--token <token>`: Gateway token
- `--timeout <ms>`: timeout in ms (default `30000`)
- `--expect-final`: wait for a final response when the Gateway call is agent-backed

When you pass `--url`, the CLI does not auto-apply config or environment credentials. Include `--token` explicitly if the target Gateway requires auth.

## Examples

```bash
openclaw logs
openclaw logs --follow
openclaw logs --follow --interval 2000
openclaw logs --limit 500 --max-bytes 500000
openclaw logs --json
openclaw logs --plain
openclaw logs --no-color
openclaw logs --limit 500
openclaw logs --local-time
openclaw logs --follow --local-time
openclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
```

## Notes

- Use `--local-time` to render timestamps in your local timezone.
- If the local loopback Gateway asks for pairing, `openclaw logs` falls back to the configured local log file automatically. Explicit `--url` targets do not use this fallback.

```

## File: mcp.md
```
---
summary: "Expose OpenClaw channel conversations over MCP and manage saved MCP server definitions"
read_when:
  - Connecting Codex, Claude Code, or another MCP client to OpenClaw-backed channels
  - Running `openclaw mcp serve`
  - Managing OpenClaw-saved MCP server definitions
title: "mcp"
---

# mcp

`openclaw mcp` has two jobs:

- run OpenClaw as an MCP server with `openclaw mcp serve`
- manage OpenClaw-owned outbound MCP server definitions with `list`, `show`,
  `set`, and `unset`

In other words:

- `serve` is OpenClaw acting as an MCP server
- `list` / `show` / `set` / `unset` is OpenClaw acting as an MCP client-side
  registry for other MCP servers its runtimes may consume later

Use [`openclaw acp`](/cli/acp) when OpenClaw should host a coding harness
session itself and route that runtime through ACP.

## OpenClaw as an MCP server

This is the `openclaw mcp serve` path.

## When to use `serve`

Use `openclaw mcp serve` when:

- Codex, Claude Code, or another MCP client should talk directly to
  OpenClaw-backed channel conversations
- you already have a local or remote OpenClaw Gateway with routed sessions
- you want one MCP server that works across OpenClaw's channel backends instead
  of running separate per-channel bridges

Use [`openclaw acp`](/cli/acp) instead when OpenClaw should host the coding
runtime itself and keep the agent session inside OpenClaw.

## How it works

`openclaw mcp serve` starts a stdio MCP server. The MCP client owns that
process. While the client keeps the stdio session open, the bridge connects to a
local or remote OpenClaw Gateway over WebSocket and exposes routed channel
conversations over MCP.

Lifecycle:

1. the MCP client spawns `openclaw mcp serve`
2. the bridge connects to Gateway
3. routed sessions become MCP conversations and transcript/history tools
4. live events are queued in memory while the bridge is connected
5. if Claude channel mode is enabled, the same session can also receive
   Claude-specific push notifications

Important behavior:

- live queue state starts when the bridge connects
- older transcript history is read with `messages_read`
- Claude push notifications only exist while the MCP session is alive
- when the client disconnects, the bridge exits and the live queue is gone

## Choose a client mode

Use the same bridge in two different ways:

- Generic MCP clients: standard MCP tools only. Use `conversations_list`,
  `messages_read`, `events_poll`, `events_wait`, `messages_send`, and the
  approval tools.
- Claude Code: standard MCP tools plus the Claude-specific channel adapter.
  Enable `--claude-channel-mode on` or leave the default `auto`.

Today, `auto` behaves the same as `on`. There is no client capability detection
yet.

## What `serve` exposes

The bridge uses existing Gateway session route metadata to expose channel-backed
conversations. A conversation appears when OpenClaw already has session state
with a known route such as:

- `channel`
- recipient or destination metadata
- optional `accountId`
- optional `threadId`

This gives MCP clients one place to:

- list recent routed conversations
- read recent transcript history
- wait for new inbound events
- send a reply back through the same route
- see approval requests that arrive while the bridge is connected

## Usage

```bash
# Local Gateway
openclaw mcp serve

# Remote Gateway
openclaw mcp serve --url wss://gateway-host:18789 --token-file ~/.openclaw/gateway.token

# Remote Gateway with password auth
openclaw mcp serve --url wss://gateway-host:18789 --password-file ~/.openclaw/gateway.password

# Enable verbose bridge logs
openclaw mcp serve --verbose

# Disable Claude-specific push notifications
openclaw mcp serve --claude-channel-mode off
```

## Bridge tools

The current bridge exposes these MCP tools:

- `conversations_list`
- `conversation_get`
- `messages_read`
- `attachments_fetch`
- `events_poll`
- `events_wait`
- `messages_send`
- `permissions_list_open`
- `permissions_respond`

### `conversations_list`

Lists recent session-backed conversations that already have route metadata in
Gateway session state.

Useful filters:

- `limit`
- `search`
- `channel`
- `includeDerivedTitles`
- `includeLastMessage`

### `conversation_get`

Returns one conversation by `session_key`.

### `messages_read`

Reads recent transcript messages for one session-backed conversation.

### `attachments_fetch`

Extracts non-text message content blocks from one transcript message. This is a
metadata view over transcript content, not a standalone durable attachment blob
store.

### `events_poll`

Reads queued live events since a numeric cursor.

### `events_wait`

Long-polls until the next matching queued event arrives or a timeout expires.

Use this when a generic MCP client needs near-real-time delivery without a
Claude-specific push protocol.

### `messages_send`

Sends text back through the same route already recorded on the session.

Current behavior:

- requires an existing conversation route
- uses the session's channel, recipient, account id, and thread id
- sends text only

### `permissions_list_open`

Lists pending exec/plugin approval requests the bridge has observed since it
connected to the Gateway.

### `permissions_respond`

Resolves one pending exec/plugin approval request with:

- `allow-once`
- `allow-always`
- `deny`

## Event model

The bridge keeps an in-memory event queue while it is connected.

Current event types:

- `message`
- `exec_approval_requested`
- `exec_approval_resolved`
- `plugin_approval_requested`
- `plugin_approval_resolved`
- `claude_permission_request`

Important limits:

- the queue is live-only; it starts when the MCP bridge starts
- `events_poll` and `events_wait` do not replay older Gateway history by
  themselves
- durable backlog should be read with `messages_read`

## Claude channel notifications

The bridge can also expose Claude-specific channel notifications. This is the
OpenClaw equivalent of a Claude Code channel adapter: standard MCP tools remain
available, but live inbound messages can also arrive as Claude-specific MCP
notifications.

Flags:

- `--claude-channel-mode off`: standard MCP tools only
- `--claude-channel-mode on`: enable Claude channel notifications
- `--claude-channel-mode auto`: current default; same bridge behavior as `on`

When Claude channel mode is enabled, the server advertises Claude experimental
capabilities and can emit:

- `notifications/claude/channel`
- `notifications/claude/channel/permission`

Current bridge behavior:

- inbound `user` transcript messages are forwarded as
  `notifications/claude/channel`
- Claude permission requests received over MCP are tracked in-memory
- if the linked conversation later sends `yes abcde` or `no abcde`, the bridge
  converts that to `notifications/claude/channel/permission`
- these notifications are live-session only; if the MCP client disconnects,
  there is no push target

This is intentionally client-specific. Generic MCP clients should rely on the
standard polling tools.

## MCP client config

Example stdio client config:

```json
{
  "mcpServers": {
    "openclaw": {
      "command": "openclaw",
      "args": [
        "mcp",
        "serve",
        "--url",
        "wss://gateway-host:18789",
        "--token-file",
        "/path/to/gateway.token"
      ]
    }
  }
}
```

For most generic MCP clients, start with the standard tool surface and ignore
Claude mode. Turn Claude mode on only for clients that actually understand the
Claude-specific notification methods.

## Options

`openclaw mcp serve` supports:

- `--url <url>`: Gateway WebSocket URL
- `--token <token>`: Gateway token
- `--token-file <path>`: read token from file
- `--password <password>`: Gateway password
- `--password-file <path>`: read password from file
- `--claude-channel-mode <auto|on|off>`: Claude notification mode
- `-v`, `--verbose`: verbose logs on stderr

Prefer `--token-file` or `--password-file` over inline secrets when possible.

## Security and trust boundary

The bridge does not invent routing. It only exposes conversations that Gateway
already knows how to route.

That means:

- sender allowlists, pairing, and channel-level trust still belong to the
  underlying OpenClaw channel configuration
- `messages_send` can only reply through an existing stored route
- approval state is live/in-memory only for the current bridge session
- bridge auth should use the same Gateway token or password controls you would
  trust for any other remote Gateway client

If a conversation is missing from `conversations_list`, the usual cause is not
MCP configuration. It is missing or incomplete route metadata in the underlying
Gateway session.

## Testing

OpenClaw ships a deterministic Docker smoke for this bridge:

```bash
pnpm test:docker:mcp-channels
```

That smoke:

- starts a seeded Gateway container
- starts a second container that spawns `openclaw mcp serve`
- verifies conversation discovery, transcript reads, attachment metadata reads,
  live event queue behavior, and outbound send routing
- validates Claude-style channel and permission notifications over the real
  stdio MCP bridge

This is the fastest way to prove the bridge works without wiring a real
Telegram, Discord, or iMessage account into the test run.

For broader testing context, see [Testing](/help/testing).

## Troubleshooting

### No conversations returned

Usually means the Gateway session is not already routable. Confirm that the
underlying session has stored channel/provider, recipient, and optional
account/thread route metadata.

### `events_poll` or `events_wait` misses older messages

Expected. The live queue starts when the bridge connects. Read older transcript
history with `messages_read`.

### Claude notifications do not show up

Check all of these:

- the client kept the stdio MCP session open
- `--claude-channel-mode` is `on` or `auto`
- the client actually understands the Claude-specific notification methods
- the inbound message happened after the bridge connected

### Approvals are missing

`permissions_list_open` only shows approval requests observed while the bridge
was connected. It is not a durable approval history API.

## OpenClaw as an MCP client registry

This is the `openclaw mcp list`, `show`, `set`, and `unset` path.

These commands do not expose OpenClaw over MCP. They manage OpenClaw-owned MCP
server definitions under `mcp.servers` in OpenClaw config.

Those saved definitions are for runtimes that OpenClaw launches or configures
later, such as embedded Pi and other runtime adapters. OpenClaw stores the
definitions centrally so those runtimes do not need to keep their own duplicate
MCP server lists.

Important behavior:

- these commands only read or write OpenClaw config
- they do not connect to the target MCP server
- they do not validate whether the command, URL, or remote transport is
  reachable right now
- runtime adapters decide which transport shapes they actually support at
  execution time

## Saved MCP server definitions

OpenClaw also stores a lightweight MCP server registry in config for surfaces
that want OpenClaw-managed MCP definitions.

Commands:

- `openclaw mcp list`
- `openclaw mcp show [name]`
- `openclaw mcp set <name> <json>`
- `openclaw mcp unset <name>`

Notes:

- `list` sorts server names.
- `show` without a name prints the full configured MCP server object.
- `set` expects one JSON object value on the command line.
- `unset` fails if the named server does not exist.

Examples:

```bash
openclaw mcp list
openclaw mcp show context7 --json
openclaw mcp set context7 '{"command":"uvx","args":["context7-mcp"]}'
openclaw mcp set docs '{"url":"https://mcp.example.com"}'
openclaw mcp unset context7
```

Example config shape:

```json
{
  "mcp": {
    "servers": {
      "context7": {
        "command": "uvx",
        "args": ["context7-mcp"]
      },
      "docs": {
        "url": "https://mcp.example.com"
      }
    }
  }
}
```

### Stdio transport

Launches a local child process and communicates over stdin/stdout.

| Field                      | Description                       |
| -------------------------- | --------------------------------- |
| `command`                  | Executable to spawn (required)    |
| `args`                     | Array of command-line arguments   |
| `env`                      | Extra environment variables       |
| `cwd` / `workingDirectory` | Working directory for the process |

### SSE / HTTP transport

Connects to a remote MCP server over HTTP Server-Sent Events.

| Field                 | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| `url`                 | HTTP or HTTPS URL of the remote server (required)                |
| `headers`             | Optional key-value map of HTTP headers (for example auth tokens) |
| `connectionTimeoutMs` | Per-server connection timeout in ms (optional)                   |

Example:

```json
{
  "mcp": {
    "servers": {
      "remote-tools": {
        "url": "https://mcp.example.com",
        "headers": {
          "Authorization": "Bearer <token>"
        }
      }
    }
  }
}
```

Sensitive values in `url` (userinfo) and `headers` are redacted in logs and
status output.

### Streamable HTTP transport

`streamable-http` is an additional transport option alongside `sse` and `stdio`. It uses HTTP streaming for bidirectional communication with remote MCP servers.

| Field                 | Description                                                                            |
| --------------------- | -------------------------------------------------------------------------------------- |
| `url`                 | HTTP or HTTPS URL of the remote server (required)                                      |
| `transport`           | Set to `"streamable-http"` to select this transport; when omitted, OpenClaw uses `sse` |
| `headers`             | Optional key-value map of HTTP headers (for example auth tokens)                       |
| `connectionTimeoutMs` | Per-server connection timeout in ms (optional)                                         |

Example:

```json
{
  "mcp": {
    "servers": {
      "streaming-tools": {
        "url": "https://mcp.example.com/stream",
        "transport": "streamable-http",
        "connectionTimeoutMs": 10000,
        "headers": {
          "Authorization": "Bearer <token>"
        }
      }
    }
  }
}
```

These commands manage saved config only. They do not start the channel bridge,
open a live MCP client session, or prove the target server is reachable.

## Current limits

This page documents the bridge as shipped today.

Current limits:

- conversation discovery depends on existing Gateway session route metadata
- no generic push protocol beyond the Claude-specific adapter
- no message edit or react tools yet
- HTTP/SSE/streamable-http transport connects to a single remote server; no multiplexed upstream yet
- `permissions_list_open` only includes approvals observed while the bridge is
  connected

```

## File: memory.md
```
---
summary: "CLI reference for `openclaw memory` (status/index/search/promote/promote-explain/rem-harness)"
read_when:
  - You want to index or search semantic memory
  - You’re debugging memory availability or indexing
  - You want to promote recalled short-term memory into `MEMORY.md`
title: "memory"
---

# `openclaw memory`

Manage semantic memory indexing and search.
Provided by the active memory plugin (default: `memory-core`; set `plugins.slots.memory = "none"` to disable).

Related:


## Examples

```bash
openclaw memory status
openclaw memory status --deep
openclaw memory status --fix
openclaw memory index --force
openclaw memory search "meeting notes"
openclaw memory search --query "deployment" --max-results 20
openclaw memory promote --limit 10 --min-score 0.75
openclaw memory promote --apply
openclaw memory promote --json --min-recall-count 0 --min-unique-queries 0
openclaw memory promote-explain "router vlan"
openclaw memory promote-explain "router vlan" --json
openclaw memory rem-harness
openclaw memory rem-harness --json
openclaw memory status --json
openclaw memory status --deep --index
openclaw memory status --deep --index --verbose
openclaw memory status --agent main
openclaw memory index --agent main --verbose
```

## Options

`memory status` and `memory index`:

- `--agent <id>`: scope to a single agent. Without it, these commands run for each configured agent; if no agent list is configured, they fall back to the default agent.
- `--verbose`: emit detailed logs during probes and indexing.

`memory status`:

- `--deep`: probe vector + embedding availability.
- `--index`: run a reindex if the store is dirty (implies `--deep`).
- `--fix`: repair stale recall locks and normalize promotion metadata.
- `--json`: print JSON output.

`memory index`:

- `--force`: force a full reindex.

`memory search`:

- Query input: pass either positional `[query]` or `--query <text>`.
- If both are provided, `--query` wins.
- If neither is provided, the command exits with an error.
- `--agent <id>`: scope to a single agent (default: the default agent).
- `--max-results <n>`: limit the number of results returned.
- `--min-score <n>`: filter out low-score matches.
- `--json`: print JSON results.

`memory promote`:

Preview and apply short-term memory promotions.

```bash
openclaw memory promote [--apply] [--limit <n>] [--include-promoted]
```

- `--apply` -- write promotions to `MEMORY.md` (default: preview only).
- `--limit <n>` -- cap the number of candidates shown.
- `--include-promoted` -- include entries already promoted in previous cycles.

Full options:

- Ranks short-term candidates from `memory/YYYY-MM-DD.md` using weighted promotion signals (`frequency`, `relevance`, `query diversity`, `recency`, `consolidation`, `conceptual richness`).
- Uses short-term signals from both memory recalls and daily-ingestion passes, plus light/REM phase reinforcement signals.
- When dreaming is enabled, `memory-core` auto-manages one cron job that runs a full sweep (`light -> REM -> deep`) in the background (no manual `openclaw cron add` required).
- `--agent <id>`: scope to a single agent (default: the default agent).
- `--limit <n>`: max candidates to return/apply.
- `--min-score <n>`: minimum weighted promotion score.
- `--min-recall-count <n>`: minimum recall count required for a candidate.
- `--min-unique-queries <n>`: minimum distinct query count required for a candidate.
- `--apply`: append selected candidates into `MEMORY.md` and mark them promoted.
- `--include-promoted`: include already promoted candidates in output.
- `--json`: print JSON output.

`memory promote-explain`:

Explain a specific promotion candidate and its score breakdown.

```bash
openclaw memory promote-explain <selector> [--agent <id>] [--include-promoted] [--json]
```

- `<selector>`: candidate key, path fragment, or snippet fragment to look up.
- `--agent <id>`: scope to a single agent (default: the default agent).
- `--include-promoted`: include already promoted candidates.
- `--json`: print JSON output.

`memory rem-harness`:

Preview REM reflections, candidate truths, and deep promotion output without writing anything.

```bash
openclaw memory rem-harness [--agent <id>] [--include-promoted] [--json]
```

- `--agent <id>`: scope to a single agent (default: the default agent).
- `--include-promoted`: include already promoted deep candidates.
- `--json`: print JSON output.

## Dreaming (experimental)

Dreaming is the background memory consolidation system with three cooperative
phases: **light** (sort/stage short-term material), **deep** (promote durable
facts into `MEMORY.md`), and **REM** (reflect and surface themes).

- Enable with `plugins.entries.memory-core.config.dreaming.enabled: true`.
- Toggle from chat with `/dreaming on|off` (or inspect with `/dreaming status`).
- Dreaming runs on one managed sweep schedule (`dreaming.frequency`) and executes phases in order: light, REM, deep.
- Only the deep phase writes durable memory to `MEMORY.md`.
- Human-readable phase output and diary entries are written to `DREAMS.md` (or existing `dreams.md`), with optional per-phase reports in `memory/dreaming/<phase>/YYYY-MM-DD.md`.
- Ranking uses weighted signals: recall frequency, retrieval relevance, query diversity, temporal recency, cross-day consolidation, and derived concept richness.
- Promotion re-reads the live daily note before writing to `MEMORY.md`, so edited or deleted short-term snippets do not get promoted from stale recall-store snapshots.
- Scheduled and manual `memory promote` runs share the same deep phase defaults unless you pass CLI threshold overrides.
- Automatic runs fan out across configured memory workspaces.

Default scheduling:

- **Sweep cadence**: `dreaming.frequency = 0 3 * * *`
- **Deep thresholds**: `minScore=0.8`, `minRecallCount=3`, `minUniqueQueries=3`, `recencyHalfLifeDays=14`, `maxAgeDays=30`

Example:

```json
{
  "plugins": {
    "entries": {
      "memory-core": {
        "config": {
          "dreaming": {
            "enabled": true
          }
        }
      }
    }
  }
}
```

Notes:

- `memory index --verbose` prints per-phase details (provider, model, sources, batch activity).
- `memory status` includes any extra paths configured via `memorySearch.extraPaths`.
- If effectively active memory remote API key fields are configured as SecretRefs, the command resolves those values from the active gateway snapshot. If gateway is unavailable, the command fails fast.
- Gateway version skew note: this command path requires a gateway that supports `secrets.resolve`; older gateways return an unknown-method error.
- Tune scheduled sweep cadence with `dreaming.frequency`. Deep promotion policy is otherwise internal; use CLI flags on `memory promote` when you need one-off manual overrides.
- `memory rem-harness --path <file-or-dir> --grounded` previews grounded `What Happened`, `Reflections`, and `Possible Lasting Updates` from historical daily notes without writing anything.
- `memory rem-backfill --path <file-or-dir>` writes reversible grounded diary entries into `DREAMS.md` for UI review.
- `memory rem-backfill --path <file-or-dir> --stage-short-term` also seeds grounded durable candidates into the live short-term promotion store so the normal deep phase can rank them.
- `memory rem-backfill --rollback` removes previously written grounded diary entries, and `memory rem-backfill --rollback-short-term` removes previously staged grounded short-term candidates.

```

## File: message.md
```
---
summary: "CLI reference for `openclaw message` (send + channel actions)"
read_when:
  - Adding or modifying message CLI actions
  - Changing outbound channel behavior
title: "message"
---

# `openclaw message`

Single outbound command for sending messages and channel actions
(Discord/Google Chat/iMessage/Matrix/Mattermost (plugin)/Microsoft Teams/Signal/Slack/Telegram/WhatsApp).

## Usage

```
openclaw message <subcommand> [flags]
```

Channel selection:

- `--channel` required if more than one channel is configured.
- If exactly one channel is configured, it becomes the default.
- Values: `discord|googlechat|imessage|matrix|mattermost|msteams|signal|slack|telegram|whatsapp` (Mattermost requires plugin)

Target formats (`--target`):

- WhatsApp: E.164 or group JID
- Telegram: chat id or `@username`
- Discord: `channel:<id>` or `user:<id>` (or `<@id>` mention; raw numeric ids are treated as channels)
- Google Chat: `spaces/<spaceId>` or `users/<userId>`
- Slack: `channel:<id>` or `user:<id>` (raw channel id is accepted)
- Mattermost (plugin): `channel:<id>`, `user:<id>`, or `@username` (bare ids are treated as channels)
- Signal: `+E.164`, `group:<id>`, `signal:+E.164`, `signal:group:<id>`, or `username:<name>`/`u:<name>`
- iMessage: handle, `chat_id:<id>`, `chat_guid:<guid>`, or `chat_identifier:<id>`
- Matrix: `@user:server`, `!room:server`, or `#alias:server`
- Microsoft Teams: conversation id (`19:...@thread.tacv2`) or `conversation:<id>` or `user:<aad-object-id>`

Name lookup:

- For supported providers (Discord/Slack/etc), channel names like `Help` or `#help` are resolved via the directory cache.
- On cache miss, OpenClaw will attempt a live directory lookup when the provider supports it.

## Common flags

- `--channel <name>`
- `--account <id>`
- `--target <dest>` (target channel or user for send/poll/read/etc)
- `--targets <name>` (repeat; broadcast only)
- `--json`
- `--dry-run`
- `--verbose`

## SecretRef behavior

- `openclaw message` resolves supported channel SecretRefs before running the selected action.
- Resolution is scoped to the active action target when possible:
  - channel-scoped when `--channel` is set (or inferred from prefixed targets like `discord:...`)
  - account-scoped when `--account` is set (channel globals + selected account surfaces)
  - when `--account` is omitted, OpenClaw does not force a `default` account SecretRef scope
- Unresolved SecretRefs on unrelated channels do not block a targeted message action.
- If the selected channel/account SecretRef is unresolved, the command fails closed for that action.

## Actions

### Core

- `send`
  - Channels: WhatsApp/Telegram/Discord/Google Chat/Slack/Mattermost (plugin)/Signal/iMessage/Matrix/Microsoft Teams
  - Required: `--target`, plus `--message` or `--media`
  - Optional: `--media`, `--interactive`, `--buttons`, `--components`, `--card`, `--reply-to`, `--thread-id`, `--gif-playback`, `--force-document`, `--silent`
  - Shared interactive payloads: `--interactive` sends a channel-native interactive JSON payload when supported
  - Telegram only: `--buttons` (requires `channels.telegram.capabilities.inlineButtons` to allow it)
  - Telegram only: `--force-document` (send images and GIFs as documents to avoid Telegram compression)
  - Telegram only: `--thread-id` (forum topic id)
  - Slack only: `--thread-id` (thread timestamp; `--reply-to` uses the same field)
  - Discord only: `--components` JSON payload
  - Adaptive-card channels: `--card` JSON payload when supported
  - Telegram + Discord: `--silent`
  - WhatsApp only: `--gif-playback`

- `poll`
  - Channels: WhatsApp/Telegram/Discord/Matrix/Microsoft Teams
  - Required: `--target`, `--poll-question`, `--poll-option` (repeat)
  - Optional: `--poll-multi`
  - Discord only: `--poll-duration-hours`, `--silent`, `--message`
  - Telegram only: `--poll-duration-seconds` (5-600), `--silent`, `--poll-anonymous` / `--poll-public`, `--thread-id`

- `react`
  - Channels: Discord/Google Chat/Slack/Telegram/WhatsApp/Signal/Matrix
  - Required: `--message-id`, `--target`
  - Optional: `--emoji`, `--remove`, `--participant`, `--from-me`, `--target-author`, `--target-author-uuid`
  - Note: `--remove` requires `--emoji` (omit `--emoji` to clear own reactions where supported; see /tools/reactions)
  - WhatsApp only: `--participant`, `--from-me`
  - Signal group reactions: `--target-author` or `--target-author-uuid` required

- `reactions`
  - Channels: Discord/Google Chat/Slack/Matrix
  - Required: `--message-id`, `--target`
  - Optional: `--limit`

- `read`
  - Channels: Discord/Slack/Matrix
  - Required: `--target`
  - Optional: `--limit`, `--before`, `--after`
  - Discord only: `--around`

- `edit`
  - Channels: Discord/Slack/Matrix
  - Required: `--message-id`, `--message`, `--target`

- `delete`
  - Channels: Discord/Slack/Telegram/Matrix
  - Required: `--message-id`, `--target`

- `pin` / `unpin`
  - Channels: Discord/Slack/Matrix
  - Required: `--message-id`, `--target`

- `pins` (list)
  - Channels: Discord/Slack/Matrix
  - Required: `--target`

- `permissions`
  - Channels: Discord/Matrix
  - Required: `--target`
  - Matrix only: available when Matrix encryption is enabled and verification actions are allowed

- `search`
  - Channels: Discord
  - Required: `--guild-id`, `--query`
  - Optional: `--channel-id`, `--channel-ids` (repeat), `--author-id`, `--author-ids` (repeat), `--limit`

### Threads

- `thread create`
  - Channels: Discord
  - Required: `--thread-name`, `--target` (channel id)
  - Optional: `--message-id`, `--message`, `--auto-archive-min`

- `thread list`
  - Channels: Discord
  - Required: `--guild-id`
  - Optional: `--channel-id`, `--include-archived`, `--before`, `--limit`

- `thread reply`
  - Channels: Discord
  - Required: `--target` (thread id), `--message`
  - Optional: `--media`, `--reply-to`

### Emojis

- `emoji list`
  - Discord: `--guild-id`
  - Slack: no extra flags

- `emoji upload`
  - Channels: Discord
  - Required: `--guild-id`, `--emoji-name`, `--media`
  - Optional: `--role-ids` (repeat)

### Stickers

- `sticker send`
  - Channels: Discord
  - Required: `--target`, `--sticker-id` (repeat)
  - Optional: `--message`

- `sticker upload`
  - Channels: Discord
  - Required: `--guild-id`, `--sticker-name`, `--sticker-desc`, `--sticker-tags`, `--media`

### Roles / Channels / Members / Voice

- `role info` (Discord): `--guild-id`
- `role add` / `role remove` (Discord): `--guild-id`, `--user-id`, `--role-id`
- `channel info` (Discord): `--target`
- `channel list` (Discord): `--guild-id`
- `member info` (Discord/Slack): `--user-id` (+ `--guild-id` for Discord)
- `voice status` (Discord): `--guild-id`, `--user-id`

### Events

- `event list` (Discord): `--guild-id`
- `event create` (Discord): `--guild-id`, `--event-name`, `--start-time`
  - Optional: `--end-time`, `--desc`, `--channel-id`, `--location`, `--event-type`

### Moderation (Discord)

- `timeout`: `--guild-id`, `--user-id` (optional `--duration-min` or `--until`; omit both to clear timeout)
- `kick`: `--guild-id`, `--user-id` (+ `--reason`)
- `ban`: `--guild-id`, `--user-id` (+ `--delete-days`, `--reason`)
  - `timeout` also supports `--reason`

### Broadcast

- `broadcast`
  - Channels: any configured channel; use `--channel all` to target all providers
  - Required: `--targets <target...>`
  - Optional: `--message`, `--media`, `--dry-run`

## Examples

Send a Discord reply:

```
openclaw message send --channel discord \
  --target channel:123 --message "hi" --reply-to 456
```

Send a Discord message with components:

```
openclaw message send --channel discord \
  --target channel:123 --message "Choose:" \
  --components '{"text":"Choose a path","blocks":[{"type":"actions","buttons":[{"label":"Approve","style":"success"},{"label":"Decline","style":"danger"}]}]}'
```

See [Discord components](/channels/discord#interactive-components) for the full schema.

Send a shared interactive payload:

```bash
openclaw message send --channel googlechat --target spaces/AAA... \
  --message "Choose:" \
  --interactive '{"text":"Choose a path","blocks":[{"type":"actions","buttons":[{"label":"Approve"},{"label":"Decline"}]}]}'
```

Create a Discord poll:

```
openclaw message poll --channel discord \
  --target channel:123 \
  --poll-question "Snack?" \
  --poll-option Pizza --poll-option Sushi \
  --poll-multi --poll-duration-hours 48
```

Create a Telegram poll (auto-close in 2 minutes):

```
openclaw message poll --channel telegram \
  --target @mychat \
  --poll-question "Lunch?" \
  --poll-option Pizza --poll-option Sushi \
  --poll-duration-seconds 120 --silent
```

Send a Teams proactive message:

```
openclaw message send --channel msteams \
  --target conversation:19:abc@thread.tacv2 --message "hi"
```

Create a Teams poll:

```
openclaw message poll --channel msteams \
  --target conversation:19:abc@thread.tacv2 \
  --poll-question "Lunch?" \
  --poll-option Pizza --poll-option Sushi
```

React in Slack:

```
openclaw message react --channel slack \
  --target C123 --message-id 456 --emoji "✅"
```

React in a Signal group:

```
openclaw message react --channel signal \
  --target signal:group:abc123 --message-id 1737630212345 \
  --emoji "✅" --target-author-uuid 123e4567-e89b-12d3-a456-426614174000
```

Send Telegram inline buttons:

```
openclaw message send --channel telegram --target @mychat --message "Choose:" \
  --buttons '[ [{"text":"Yes","callback_data":"cmd:yes"}], [{"text":"No","callback_data":"cmd:no"}] ]'
```

Send a Teams Adaptive Card:

```bash
openclaw message send --channel msteams \
  --target conversation:19:abc@thread.tacv2 \
  --card '{"type":"AdaptiveCard","version":"1.5","body":[{"type":"TextBlock","text":"Status update"}]}'
```

Send a Telegram image as a document to avoid compression:

```bash
openclaw message send --channel telegram --target @mychat \
  --media ./diagram.png --force-document
```

```

## File: models.md
```
---
summary: "CLI reference for `openclaw models` (status/list/set/scan, aliases, fallbacks, auth)"
read_when:
  - You want to change default models or view provider auth status
  - You want to scan available models/providers and debug auth profiles
title: "models"
---

# `openclaw models`

Model discovery, scanning, and configuration (default model, fallbacks, auth profiles).

Related:


## Common commands

```bash
openclaw models status
openclaw models list
openclaw models set <model-or-alias>
openclaw models scan
```

`openclaw models status` shows the resolved default/fallbacks plus an auth overview.
When provider usage snapshots are available, the OAuth/API-key status section includes
provider usage windows and quota snapshots.
Current usage-window providers: Anthropic, GitHub Copilot, Gemini CLI, OpenAI
Codex, MiniMax, Xiaomi, and z.ai. Usage auth comes from provider-specific hooks
when available; otherwise OpenClaw falls back to matching OAuth/API-key
credentials from auth profiles, env, or config.
In `--json` output, `auth.providers` is the env/config/store-aware provider
overview, while `auth.oauth` is auth-store profile health only.
Add `--probe` to run live auth probes against each configured provider profile.
Probes are real requests (may consume tokens and trigger rate limits).
Use `--agent <id>` to inspect a configured agent’s model/auth state. When omitted,
the command uses `OPENCLAW_AGENT_DIR`/`PI_CODING_AGENT_DIR` if set, otherwise the
configured default agent.
Probe rows can come from auth profiles, env credentials, or `models.json`.

Notes:

- `models set <model-or-alias>` accepts `provider/model` or an alias.
- Model refs are parsed by splitting on the **first** `/`. If the model ID includes `/` (OpenRouter-style), include the provider prefix (example: `openrouter/moonshotai/kimi-k2`).
- If you omit the provider, OpenClaw resolves the input as an alias first, then
  as a unique configured-provider match for that exact model id, and only then
  falls back to the configured default provider with a deprecation warning.
  If that provider no longer exposes the configured default model, OpenClaw
  falls back to the first configured provider/model instead of surfacing a
  stale removed-provider default.
- `models status` may show `marker(<value>)` in auth output for non-secret placeholders (for example `OPENAI_API_KEY`, `secretref-managed`, `minimax-oauth`, `oauth:chutes`, `ollama-local`) instead of masking them as secrets.

### `models status`

Options:

- `--json`
- `--plain`
- `--check` (exit 1=expired/missing, 2=expiring)
- `--probe` (live probe of configured auth profiles)
- `--probe-provider <name>` (probe one provider)
- `--probe-profile <id>` (repeat or comma-separated profile ids)
- `--probe-timeout <ms>`
- `--probe-concurrency <n>`
- `--probe-max-tokens <n>`
- `--agent <id>` (configured agent id; overrides `OPENCLAW_AGENT_DIR`/`PI_CODING_AGENT_DIR`)

Probe status buckets:

- `ok`
- `auth`
- `rate_limit`
- `billing`
- `timeout`
- `format`
- `unknown`
- `no_model`

Probe detail/reason-code cases to expect:

- `excluded_by_auth_order`: a stored profile exists, but explicit
  `auth.order.<provider>` omitted it, so probe reports the exclusion instead of
  trying it.
- `missing_credential`, `invalid_expires`, `expired`, `unresolved_ref`:
  profile is present but not eligible/resolvable.
- `no_model`: provider auth exists, but OpenClaw could not resolve a probeable
  model candidate for that provider.

## Aliases + fallbacks

```bash
openclaw models aliases list
openclaw models fallbacks list
```

## Auth profiles

```bash
openclaw models auth add
openclaw models auth login --provider <id>
openclaw models auth setup-token --provider <id>
openclaw models auth paste-token
```

`models auth add` is the interactive auth helper. It can launch a provider auth
flow (OAuth/API key) or guide you into manual token paste, depending on the
provider you choose.

`models auth login` runs a provider plugin’s auth flow (OAuth/API key). Use
`openclaw plugins list` to see which providers are installed.

Examples:

```bash
openclaw models auth login --provider openai-codex --set-default
```

Notes:

- `setup-token` and `paste-token` remain generic token commands for providers
  that expose token auth methods.
- `setup-token` requires an interactive TTY and runs the provider's token-auth
  method (defaulting to that provider's `setup-token` method when it exposes
  one).
- `paste-token` accepts a token string generated elsewhere or from automation.
- `paste-token` requires `--provider`, prompts for the token value, and writes
  it to the default profile id `<provider>:manual` unless you pass
  `--profile-id`.
- `paste-token --expires-in <duration>` stores an absolute token expiry from a
  relative duration such as `365d` or `12h`.
- Anthropic note: Anthropic staff told us OpenClaw-style Claude CLI usage is allowed again, so OpenClaw treats Claude CLI reuse and `claude -p` usage as sanctioned for this integration unless Anthropic publishes a new policy.
- Anthropic `setup-token` / `paste-token` remain available as a supported OpenClaw token path, but OpenClaw now prefers Claude CLI reuse and `claude -p` when available.

```

## File: node.md
```
---
summary: "CLI reference for `openclaw node` (headless node host)"
read_when:
  - Running the headless node host
  - Pairing a non-macOS node for system.run
title: "node"
---

# `openclaw node`

Run a **headless node host** that connects to the Gateway WebSocket and exposes
`system.run` / `system.which` on this machine.

## Why use a node host?

Use a node host when you want agents to **run commands on other machines** in your
network without installing a full macOS companion app there.

Common use cases:

- Run commands on remote Linux/Windows boxes (build servers, lab machines, NAS).
- Keep exec **sandboxed** on the gateway, but delegate approved runs to other hosts.
- Provide a lightweight, headless execution target for automation or CI nodes.

Execution is still guarded by **exec approvals** and per‑agent allowlists on the
node host, so you can keep command access scoped and explicit.

## Browser proxy (zero-config)

Node hosts automatically advertise a browser proxy if `browser.enabled` is not
disabled on the node. This lets the agent use browser automation on that node
without extra configuration.

By default, the proxy exposes the node's normal browser profile surface. If you
set `nodeHost.browserProxy.allowProfiles`, the proxy becomes restrictive:
non-allowlisted profile targeting is rejected, and persistent profile
create/delete routes are blocked through the proxy.

Disable it on the node if needed:

```json5
{
  nodeHost: {
    browserProxy: {
      enabled: false,
    },
  },
}
```

## Run (foreground)

```bash
openclaw node run --host <gateway-host> --port 18789
```

Options:

- `--host <host>`: Gateway WebSocket host (default: `127.0.0.1`)
- `--port <port>`: Gateway WebSocket port (default: `18789`)
- `--tls`: Use TLS for the gateway connection
- `--tls-fingerprint <sha256>`: Expected TLS certificate fingerprint (sha256)
- `--node-id <id>`: Override node id (clears pairing token)
- `--display-name <name>`: Override the node display name

## Gateway auth for node host

`openclaw node run` and `openclaw node install` resolve gateway auth from config/env (no `--token`/`--password` flags on node commands):

- `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD` are checked first.
- Then local config fallback: `gateway.auth.token` / `gateway.auth.password`.
- In local mode, node host intentionally does not inherit `gateway.remote.token` / `gateway.remote.password`.
- If `gateway.auth.token` / `gateway.auth.password` is explicitly configured via SecretRef and unresolved, node auth resolution fails closed (no remote fallback masking).
- In `gateway.mode=remote`, remote client fields (`gateway.remote.token` / `gateway.remote.password`) are also eligible per remote precedence rules.
- Node host auth resolution only honors `OPENCLAW_GATEWAY_*` env vars.

## Service (background)

Install a headless node host as a user service.

```bash
openclaw node install --host <gateway-host> --port 18789
```

Options:

- `--host <host>`: Gateway WebSocket host (default: `127.0.0.1`)
- `--port <port>`: Gateway WebSocket port (default: `18789`)
- `--tls`: Use TLS for the gateway connection
- `--tls-fingerprint <sha256>`: Expected TLS certificate fingerprint (sha256)
- `--node-id <id>`: Override node id (clears pairing token)
- `--display-name <name>`: Override the node display name
- `--runtime <runtime>`: Service runtime (`node` or `bun`)
- `--force`: Reinstall/overwrite if already installed

Manage the service:

```bash
openclaw node status
openclaw node stop
openclaw node restart
openclaw node uninstall
```

Use `openclaw node run` for a foreground node host (no service).

Service commands accept `--json` for machine-readable output.

## Pairing

The first connection creates a pending device pairing request (`role: node`) on the Gateway.
Approve it via:

```bash
openclaw devices list
openclaw devices approve <requestId>
```

If the node retries pairing with changed auth details (role/scopes/public key),
the previous pending request is superseded and a new `requestId` is created.
Run `openclaw devices list` again before approval.

The node host stores its node id, token, display name, and gateway connection info in
`~/.openclaw/node.json`.

## Exec approvals

`system.run` is gated by local exec approvals:

- `~/.openclaw/exec-approvals.json`
- `openclaw approvals --node <id|name|ip>` (edit from the Gateway)

For approved async node exec, OpenClaw prepares a canonical `systemRunPlan`
before prompting. The later approved `system.run` forward reuses that stored
plan, so edits to command/cwd/session fields after the approval request was
created are rejected instead of changing what the node executes.

```

## File: nodes.md
```
---
summary: "CLI reference for `openclaw nodes` (status, pairing, invoke, camera/canvas/screen)"
read_when:
  - You’re managing paired nodes (cameras, screen, canvas)
  - You need to approve requests or invoke node commands
title: "nodes"
---

# `openclaw nodes`

Manage paired nodes (devices) and invoke node capabilities.

Related:


Common options:

- `--url`, `--token`, `--timeout`, `--json`

## Common commands

```bash
openclaw nodes list
openclaw nodes list --connected
openclaw nodes list --last-connected 24h
openclaw nodes pending
openclaw nodes approve <requestId>
openclaw nodes reject <requestId>
openclaw nodes rename --node <id|name|ip> --name <displayName>
openclaw nodes status
openclaw nodes status --connected
openclaw nodes status --last-connected 24h
```

`nodes list` prints pending/paired tables. Paired rows include the most recent connect age (Last Connect).
Use `--connected` to only show currently-connected nodes. Use `--last-connected <duration>` to
filter to nodes that connected within a duration (e.g. `24h`, `7d`).

Approval note:

- `openclaw nodes pending` only needs pairing scope.
- `openclaw nodes approve <requestId>` inherits extra scope requirements from the
  pending request:
  - commandless request: pairing only
  - non-exec node commands: pairing + write
  - `system.run` / `system.run.prepare` / `system.which`: pairing + admin

## Invoke

```bash
openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
```

Invoke flags:

- `--params <json>`: JSON object string (default `{}`).
- `--invoke-timeout <ms>`: node invoke timeout (default `15000`).
- `--idempotency-key <key>`: optional idempotency key.
- `system.run` and `system.run.prepare` are blocked here; use the `exec` tool with `host=node` for shell execution.

For shell execution on a node, use the `exec` tool with `host=node` instead of `openclaw nodes run`.
The `nodes` CLI is now capability-focused: direct RPC via `nodes invoke`, plus pairing, camera,
screen, location, canvas, and notifications.

```

## File: onboard.md
```
---
summary: "CLI reference for `openclaw onboard` (interactive onboarding)"
read_when:
  - You want guided setup for gateway, workspace, auth, channels, and skills
title: "onboard"
---

# `openclaw onboard`

Interactive onboarding for local or remote Gateway setup.

## Related guides


## Examples

```bash
openclaw onboard
openclaw onboard --flow quickstart
openclaw onboard --flow manual
openclaw onboard --mode remote --remote-url wss://gateway-host:18789
```

For plaintext private-network `ws://` targets (trusted networks only), set
`OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` in the onboarding process environment.

Non-interactive custom provider:

```bash
openclaw onboard --non-interactive \
  --auth-choice custom-api-key \
  --custom-base-url "https://llm.example.com/v1" \
  --custom-model-id "foo-large" \
  --custom-api-key "$CUSTOM_API_KEY" \
  --secret-input-mode plaintext \
  --custom-compatibility openai
```

`--custom-api-key` is optional in non-interactive mode. If omitted, onboarding checks `CUSTOM_API_KEY`.

Non-interactive Ollama:

```bash
openclaw onboard --non-interactive \
  --auth-choice ollama \
  --custom-base-url "http://ollama-host:11434" \
  --custom-model-id "qwen3.5:27b" \
  --accept-risk
```

`--custom-base-url` defaults to `http://127.0.0.1:11434`. `--custom-model-id` is optional; if omitted, onboarding uses Ollama's suggested defaults. Cloud model IDs such as `kimi-k2.5:cloud` also work here.

Store provider keys as refs instead of plaintext:

```bash
openclaw onboard --non-interactive \
  --auth-choice openai-api-key \
  --secret-input-mode ref \
  --accept-risk
```

With `--secret-input-mode ref`, onboarding writes env-backed refs instead of plaintext key values.
For auth-profile backed providers this writes `keyRef` entries; for custom providers this writes `models.providers.<id>.apiKey` as an env ref (for example `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`).

Non-interactive `ref` mode contract:

- Set the provider env var in the onboarding process environment (for example `OPENAI_API_KEY`).
- Do not pass inline key flags (for example `--openai-api-key`) unless that env var is also set.
- If an inline key flag is passed without the required env var, onboarding fails fast with guidance.

Gateway token options in non-interactive mode:

- `--gateway-auth token --gateway-token <token>` stores a plaintext token.
- `--gateway-auth token --gateway-token-ref-env <name>` stores `gateway.auth.token` as an env SecretRef.
- `--gateway-token` and `--gateway-token-ref-env` are mutually exclusive.
- `--gateway-token-ref-env` requires a non-empty env var in the onboarding process environment.
- With `--install-daemon`, when token auth requires a token, SecretRef-managed gateway tokens are validated but not persisted as resolved plaintext in supervisor service environment metadata.
- With `--install-daemon`, if token mode requires a token and the configured token SecretRef is unresolved, onboarding fails closed with remediation guidance.
- With `--install-daemon`, if both `gateway.auth.token` and `gateway.auth.password` are configured and `gateway.auth.mode` is unset, onboarding blocks install until mode is set explicitly.
- Local onboarding writes `gateway.mode="local"` into the config. If a later config file is missing `gateway.mode`, treat that as config damage or an incomplete manual edit, not as a valid local-mode shortcut.
- `--allow-unconfigured` is a separate gateway runtime escape hatch. It does not mean onboarding may omit `gateway.mode`.

Example:

```bash
export OPENCLAW_GATEWAY_TOKEN="your-token"
openclaw onboard --non-interactive \
  --mode local \
  --auth-choice skip \
  --gateway-auth token \
  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \
  --accept-risk
```

Non-interactive local gateway health:

- Unless you pass `--skip-health`, onboarding waits for a reachable local gateway before it exits successfully.
- `--install-daemon` starts the managed gateway install path first. Without it, you must already have a local gateway running, for example `openclaw gateway run`.
- If you only want config/workspace/bootstrap writes in automation, use `--skip-health`.
- On native Windows, `--install-daemon` tries Scheduled Tasks first and falls back to a per-user Startup-folder login item if task creation is denied.

Interactive onboarding behavior with reference mode:

- Choose **Use secret reference** when prompted.
- Then choose either:
  - Environment variable
  - Configured secret provider (`file` or `exec`)
- Onboarding performs a fast preflight validation before saving the ref.
  - If validation fails, onboarding shows the error and lets you retry.

Non-interactive Z.AI endpoint choices:

Note: `--auth-choice zai-api-key` now auto-detects the best Z.AI endpoint for your key (prefers the general API with `zai/glm-5.1`).
If you specifically want the GLM Coding Plan endpoints, pick `zai-coding-global` or `zai-coding-cn`.

```bash
# Promptless endpoint selection
openclaw onboard --non-interactive \
  --auth-choice zai-coding-global \
  --zai-api-key "$ZAI_API_KEY"

# Other Z.AI endpoint choices:
# --auth-choice zai-coding-cn
# --auth-choice zai-global
# --auth-choice zai-cn
```

Non-interactive Mistral example:

```bash
openclaw onboard --non-interactive \
  --auth-choice mistral-api-key \
  --mistral-api-key "$MISTRAL_API_KEY"
```

Flow notes:

- `quickstart`: minimal prompts, auto-generates a gateway token.
- `manual`: full prompts for port/bind/auth (alias of `advanced`).
- When an auth choice implies a preferred provider, onboarding prefilters the
  default-model and allowlist pickers to that provider. For Volcengine and
  BytePlus, this also matches the coding-plan variants
  (`volcengine-plan/*`, `byteplus-plan/*`).
- If the preferred-provider filter yields no loaded models yet, onboarding
  falls back to the unfiltered catalog instead of leaving the picker empty.
- In the web-search step, some providers can trigger provider-specific
  follow-up prompts:
  - **Grok** can offer optional `x_search` setup with the same `XAI_API_KEY`
    and an `x_search` model choice.
  - **Kimi** can ask for the Moonshot API region (`api.moonshot.ai` vs
    `api.moonshot.cn`) and the default Kimi web-search model.
- Fastest first chat: `openclaw dashboard` (Control UI, no channel setup).
- Custom Provider: connect any OpenAI or Anthropic compatible endpoint,
  including hosted providers not listed. Use Unknown to auto-detect.

## Common follow-up commands

```bash
openclaw configure
openclaw agents add <name>
```

<Note>
`--json` does not imply non-interactive mode. Use `--non-interactive` for scripts.
</Note>

```

## File: pairing.md
```
---
summary: "CLI reference for `openclaw pairing` (approve/list pairing requests)"
read_when:
  - You’re using pairing-mode DMs and need to approve senders
title: "pairing"
---

# `openclaw pairing`

Approve or inspect DM pairing requests (for channels that support pairing).

Related:


## Commands

```bash
openclaw pairing list telegram
openclaw pairing list --channel telegram --account work
openclaw pairing list telegram --json

openclaw pairing approve <code>
openclaw pairing approve telegram <code>
openclaw pairing approve --channel telegram --account work <code> --notify
```

## `pairing list`

List pending pairing requests for one channel.

Options:

- `[channel]`: positional channel id
- `--channel <channel>`: explicit channel id
- `--account <accountId>`: account id for multi-account channels
- `--json`: machine-readable output

Notes:

- If multiple pairing-capable channels are configured, you must provide a channel either positionally or with `--channel`.
- Extension channels are allowed as long as the channel id is valid.

## `pairing approve`

Approve a pending pairing code and allow that sender.

Usage:

- `openclaw pairing approve <channel> <code>`
- `openclaw pairing approve --channel <channel> <code>`
- `openclaw pairing approve <code>` when exactly one pairing-capable channel is configured

Options:

- `--channel <channel>`: explicit channel id
- `--account <accountId>`: account id for multi-account channels
- `--notify`: send a confirmation back to the requester on the same channel

## Notes

- Channel input: pass it positionally (`pairing list telegram`) or with `--channel <channel>`.
- `pairing list` supports `--account <accountId>` for multi-account channels.
- `pairing approve` supports `--account <accountId>` and `--notify`.
- If only one pairing-capable channel is configured, `pairing approve <code>` is allowed.

```

## File: plugins.md
```
---
summary: "CLI reference for `openclaw plugins` (list, install, marketplace, uninstall, enable/disable, doctor)"
read_when:
  - You want to install or manage Gateway plugins or compatible bundles
  - You want to debug plugin load failures
title: "plugins"
---

# `openclaw plugins`

Manage Gateway plugins/extensions, hook packs, and compatible bundles.

Related:


## Commands

```bash
openclaw plugins list
openclaw plugins list --enabled
openclaw plugins list --verbose
openclaw plugins list --json
openclaw plugins install <path-or-spec>
openclaw plugins inspect <id>
openclaw plugins inspect <id> --json
openclaw plugins inspect --all
openclaw plugins info <id>
openclaw plugins enable <id>
openclaw plugins disable <id>
openclaw plugins uninstall <id>
openclaw plugins doctor
openclaw plugins update <id>
openclaw plugins update --all
openclaw plugins marketplace list <marketplace>
openclaw plugins marketplace list <marketplace> --json
```

Bundled plugins ship with OpenClaw. Some are enabled by default (for example
bundled model providers, bundled speech providers, and the bundled browser
plugin); others require `plugins enable`.

Native OpenClaw plugins must ship `openclaw.plugin.json` with an inline JSON
Schema (`configSchema`, even if empty). Compatible bundles use their own bundle
manifests instead.

`plugins list` shows `Format: openclaw` or `Format: bundle`. Verbose list/info
output also shows the bundle subtype (`codex`, `claude`, or `cursor`) plus detected bundle
capabilities.

### Install

```bash
openclaw plugins install <package>                      # ClawHub first, then npm
openclaw plugins install clawhub:<package>              # ClawHub only
openclaw plugins install <package> --force              # overwrite existing install
openclaw plugins install <package> --pin                # pin version
openclaw plugins install <package> --dangerously-force-unsafe-install
openclaw plugins install <path>                         # local path
openclaw plugins install <plugin>@<marketplace>         # marketplace
openclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)
openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
```

Bare package names are checked against ClawHub first, then npm. Security note:
treat plugin installs like running code. Prefer pinned versions.

If config is invalid, `plugins install` normally fails closed and tells you to
run `openclaw doctor --fix` first. The only documented exception is a narrow
bundled-plugin recovery path for plugins that explicitly opt into
`openclaw.install.allowInvalidConfigRecovery`.

`--force` reuses the existing install target and overwrites an already-installed
plugin or hook pack in place. Use it when you are intentionally reinstalling
the same id from a new local path, archive, ClawHub package, or npm artifact.

`--pin` applies to npm installs only. It is not supported with `--marketplace`,
because marketplace installs persist marketplace source metadata instead of an
npm spec.

`--dangerously-force-unsafe-install` is a break-glass option for false positives
in the built-in dangerous-code scanner. It allows the install to continue even
when the built-in scanner reports `critical` findings, but it does **not**
bypass plugin `before_install` hook policy blocks and does **not** bypass scan
failures.

This CLI flag applies to plugin install/update flows. Gateway-backed skill
dependency installs use the matching `dangerouslyForceUnsafeInstall` request
override, while `openclaw skills install` remains a separate ClawHub skill
download/install flow.

`plugins install` is also the install surface for hook packs that expose
`openclaw.hooks` in `package.json`. Use `openclaw hooks` for filtered hook
visibility and per-hook enablement, not package installation.

Npm specs are **registry-only** (package name + optional **exact version** or
**dist-tag**). Git/URL/file specs and semver ranges are rejected. Dependency
installs run with `--ignore-scripts` for safety.

Bare specs and `@latest` stay on the stable track. If npm resolves either of
those to a prerelease, OpenClaw stops and asks you to opt in explicitly with a
prerelease tag such as `@beta`/`@rc` or an exact prerelease version such as
`@1.2.3-beta.4`.

If a bare install spec matches a bundled plugin id (for example `diffs`), OpenClaw
installs the bundled plugin directly. To install an npm package with the same
name, use an explicit scoped spec (for example `@scope/diffs`).

Supported archives: `.zip`, `.tgz`, `.tar.gz`, `.tar`.

Claude marketplace installs are also supported.

ClawHub installs use an explicit `clawhub:<package>` locator:

```bash
openclaw plugins install clawhub:openclaw-codex-app-server
openclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
```

OpenClaw now also prefers ClawHub for bare npm-safe plugin specs. It only falls
back to npm if ClawHub does not have that package or version:

```bash
openclaw plugins install openclaw-codex-app-server
```

OpenClaw downloads the package archive from ClawHub, checks the advertised
plugin API / minimum gateway compatibility, then installs it through the normal
archive path. Recorded installs keep their ClawHub source metadata for later
updates.

Use `plugin@marketplace` shorthand when the marketplace name exists in Claude's
local registry cache at `~/.claude/plugins/known_marketplaces.json`:

```bash
openclaw plugins marketplace list <marketplace-name>
openclaw plugins install <plugin-name>@<marketplace-name>
```

Use `--marketplace` when you want to pass the marketplace source explicitly:

```bash
openclaw plugins install <plugin-name> --marketplace <marketplace-name>
openclaw plugins install <plugin-name> --marketplace <owner/repo>
openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>
openclaw plugins install <plugin-name> --marketplace ./my-marketplace
```

Marketplace sources can be:

- a Claude known-marketplace name from `~/.claude/plugins/known_marketplaces.json`
- a local marketplace root or `marketplace.json` path
- a GitHub repo shorthand such as `owner/repo`
- a GitHub repo URL such as `https://github.com/owner/repo`
- a git URL

For remote marketplaces loaded from GitHub or git, plugin entries must stay
inside the cloned marketplace repo. OpenClaw accepts relative path sources from
that repo and rejects HTTP(S), absolute-path, git, GitHub, and other non-path
plugin sources from remote manifests.

For local paths and archives, OpenClaw auto-detects:

- native OpenClaw plugins (`openclaw.plugin.json`)
- Codex-compatible bundles (`.codex-plugin/plugin.json`)
- Claude-compatible bundles (`.claude-plugin/plugin.json` or the default Claude
  component layout)
- Cursor-compatible bundles (`.cursor-plugin/plugin.json`)

Compatible bundles install into the normal extensions root and participate in
the same list/info/enable/disable flow. Today, bundle skills, Claude
command-skills, Claude `settings.json` defaults, Claude `.lsp.json` /
manifest-declared `lspServers` defaults, Cursor command-skills, and compatible
Codex hook directories are supported; other detected bundle capabilities are
shown in diagnostics/info but are not yet wired into runtime execution.

### List

```bash
openclaw plugins list
openclaw plugins list --enabled
openclaw plugins list --verbose
openclaw plugins list --json
```

Use `--enabled` to show only loaded plugins. Use `--verbose` to switch from the
table view to per-plugin detail lines with source/origin/version/activation
metadata. Use `--json` for machine-readable inventory plus registry
diagnostics.

Use `--link` to avoid copying a local directory (adds to `plugins.load.paths`):

```bash
openclaw plugins install -l ./my-plugin
```

`--force` is not supported with `--link` because linked installs reuse the
source path instead of copying over a managed install target.

Use `--pin` on npm installs to save the resolved exact spec (`name@version`) in
`plugins.installs` while keeping the default behavior unpinned.

### Uninstall

```bash
openclaw plugins uninstall <id>
openclaw plugins uninstall <id> --dry-run
openclaw plugins uninstall <id> --keep-files
```

`uninstall` removes plugin records from `plugins.entries`, `plugins.installs`,
the plugin allowlist, and linked `plugins.load.paths` entries when applicable.
For active memory plugins, the memory slot resets to `memory-core`.

By default, uninstall also removes the plugin install directory under the active
state-dir plugin root. Use
`--keep-files` to keep files on disk.

`--keep-config` is supported as a deprecated alias for `--keep-files`.

### Update

```bash
openclaw plugins update <id-or-npm-spec>
openclaw plugins update --all
openclaw plugins update <id-or-npm-spec> --dry-run
openclaw plugins update @openclaw/voice-call@beta
openclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
```

Updates apply to tracked installs in `plugins.installs` and tracked hook-pack
installs in `hooks.internal.installs`.

When you pass a plugin id, OpenClaw reuses the recorded install spec for that
plugin. That means previously stored dist-tags such as `@beta` and exact pinned
versions continue to be used on later `update <id>` runs.

For npm installs, you can also pass an explicit npm package spec with a dist-tag
or exact version. OpenClaw resolves that package name back to the tracked plugin
record, updates that installed plugin, and records the new npm spec for future
id-based updates.

When a stored integrity hash exists and the fetched artifact hash changes,
OpenClaw prints a warning and asks for confirmation before proceeding. Use
global `--yes` to bypass prompts in CI/non-interactive runs.

`--dangerously-force-unsafe-install` is also available on `plugins update` as a
break-glass override for built-in dangerous-code scan false positives during
plugin updates. It still does not bypass plugin `before_install` policy blocks
or scan-failure blocking, and it only applies to plugin updates, not hook-pack
updates.

### Inspect

```bash
openclaw plugins inspect <id>
openclaw plugins inspect <id> --json
```

Deep introspection for a single plugin. Shows identity, load status, source,
registered capabilities, hooks, tools, commands, services, gateway methods,
HTTP routes, policy flags, diagnostics, install metadata, bundle capabilities,
and any detected MCP or LSP server support.

Each plugin is classified by what it actually registers at runtime:

- **plain-capability** — one capability type (e.g. a provider-only plugin)
- **hybrid-capability** — multiple capability types (e.g. text + speech + images)
- **hook-only** — only hooks, no capabilities or surfaces
- **non-capability** — tools/commands/services but no capabilities

See [Plugin shapes](/plugins/architecture#plugin-shapes) for more on the capability model.

The `--json` flag outputs a machine-readable report suitable for scripting and
auditing.

`inspect --all` renders a fleet-wide table with shape, capability kinds,
compatibility notices, bundle capabilities, and hook summary columns.

`info` is an alias for `inspect`.

### Doctor

```bash
openclaw plugins doctor
```

`doctor` reports plugin load errors, manifest/discovery diagnostics, and
compatibility notices. When everything is clean it prints `No plugin issues
detected.`

### Marketplace

```bash
openclaw plugins marketplace list <source>
openclaw plugins marketplace list <source> --json
```

Marketplace list accepts a local marketplace path, a `marketplace.json` path, a
GitHub shorthand like `owner/repo`, a GitHub repo URL, or a git URL. `--json`
prints the resolved source label plus the parsed marketplace manifest and
plugin entries.

```

## File: qr.md
```
---
summary: "CLI reference for `openclaw qr` (generate mobile pairing QR + setup code)"
read_when:
  - You want to pair a mobile node app with a gateway quickly
  - You need setup-code output for remote/manual sharing
title: "qr"
---

# `openclaw qr`

Generate a mobile pairing QR and setup code from your current Gateway configuration.

## Usage

```bash
openclaw qr
openclaw qr --setup-code-only
openclaw qr --json
openclaw qr --remote
openclaw qr --url wss://gateway.example/ws
```

## Options

- `--remote`: prefer `gateway.remote.url`; if it is unset, `gateway.tailscale.mode=serve|funnel` can still provide the remote public URL
- `--url <url>`: override gateway URL used in payload
- `--public-url <url>`: override public URL used in payload
- `--token <token>`: override which gateway token the bootstrap flow authenticates against
- `--password <password>`: override which gateway password the bootstrap flow authenticates against
- `--setup-code-only`: print only setup code
- `--no-ascii`: skip ASCII QR rendering
- `--json`: emit JSON (`setupCode`, `gatewayUrl`, `auth`, `urlSource`)

## Notes

- `--token` and `--password` are mutually exclusive.
- The setup code itself now carries an opaque short-lived `bootstrapToken`, not the shared gateway token/password.
- In the built-in node/operator bootstrap flow, the primary node token still lands with `scopes: []`.
- If bootstrap handoff also issues an operator token, it stays bounded to the bootstrap allowlist: `operator.approvals`, `operator.read`, `operator.talk.secrets`, `operator.write`.
- Bootstrap scope checks are role-prefixed. That operator allowlist only satisfies operator requests; non-operator roles still need scopes under their own role prefix.
- Mobile pairing fails closed for Tailscale/public `ws://` gateway URLs. Private LAN `ws://` remains supported, but Tailscale/public mobile routes should use Tailscale Serve/Funnel or a `wss://` gateway URL.
- With `--remote`, OpenClaw requires either `gateway.remote.url` or
  `gateway.tailscale.mode=serve|funnel`.
- With `--remote`, if effectively active remote credentials are configured as SecretRefs and you do not pass `--token` or `--password`, the command resolves them from the active gateway snapshot. If gateway is unavailable, the command fails fast.
- Without `--remote`, local gateway auth SecretRefs are resolved when no CLI auth override is passed:
  - `gateway.auth.token` resolves when token auth can win (explicit `gateway.auth.mode="token"` or inferred mode where no password source wins).
  - `gateway.auth.password` resolves when password auth can win (explicit `gateway.auth.mode="password"` or inferred mode with no winning token from auth/env).
- If both `gateway.auth.token` and `gateway.auth.password` are configured (including SecretRefs) and `gateway.auth.mode` is unset, setup-code resolution fails until mode is set explicitly.
- Gateway version skew note: this command path requires a gateway that supports `secrets.resolve`; older gateways return an unknown-method error.
- After scanning, approve device pairing with:
  - `openclaw devices list`
  - `openclaw devices approve <requestId>`

```

## File: reset.md
```
---
summary: "CLI reference for `openclaw reset` (reset local state/config)"
read_when:
  - You want to wipe local state while keeping the CLI installed
  - You want a dry-run of what would be removed
title: "reset"
---

# `openclaw reset`

Reset local config/state (keeps the CLI installed).

Options:

- `--scope <scope>`: `config`, `config+creds+sessions`, or `full`
- `--yes`: skip confirmation prompts
- `--non-interactive`: disable prompts; requires `--scope` and `--yes`
- `--dry-run`: print actions without removing files

Examples:

```bash
openclaw backup create
openclaw reset
openclaw reset --dry-run
openclaw reset --scope config --yes --non-interactive
openclaw reset --scope config+creds+sessions --yes --non-interactive
openclaw reset --scope full --yes --non-interactive
```

Notes:

- Run `openclaw backup create` first if you want a restorable snapshot before removing local state.
- If you omit `--scope`, `openclaw reset` uses an interactive prompt to choose what to remove.
- `--non-interactive` is only valid when both `--scope` and `--yes` are set.

```

## File: sandbox.md
```
---
title: Sandbox CLI
summary: "Manage sandbox runtimes and inspect effective sandbox policy"
read_when: "You are managing sandbox runtimes or debugging sandbox/tool-policy behavior."
status: active
---

# Sandbox CLI

Manage sandbox runtimes for isolated agent execution.

## Overview

OpenClaw can run agents in isolated sandbox runtimes for security. The `sandbox` commands help you inspect and recreate those runtimes after updates or configuration changes.

Today that usually means:

- Docker sandbox containers
- SSH sandbox runtimes when `agents.defaults.sandbox.backend = "ssh"`
- OpenShell sandbox runtimes when `agents.defaults.sandbox.backend = "openshell"`

For `ssh` and OpenShell `remote`, recreate matters more than with Docker:

- the remote workspace is canonical after the initial seed
- `openclaw sandbox recreate` deletes that canonical remote workspace for the selected scope
- next use seeds it again from the current local workspace

## Commands

### `openclaw sandbox explain`

Inspect the **effective** sandbox mode/scope/workspace access, sandbox tool policy, and elevated gates (with fix-it config key paths).

```bash
openclaw sandbox explain
openclaw sandbox explain --session agent:main:main
openclaw sandbox explain --agent work
openclaw sandbox explain --json
```

### `openclaw sandbox list`

List all sandbox runtimes with their status and configuration.

```bash
openclaw sandbox list
openclaw sandbox list --browser  # List only browser containers
openclaw sandbox list --json     # JSON output
```

**Output includes:**

- Runtime name and status
- Backend (`docker`, `openshell`, etc.)
- Config label and whether it matches current config
- Age (time since creation)
- Idle time (time since last use)
- Associated session/agent

### `openclaw sandbox recreate`

Remove sandbox runtimes to force recreation with updated config.

```bash
openclaw sandbox recreate --all                # Recreate all containers
openclaw sandbox recreate --session main       # Specific session
openclaw sandbox recreate --agent mybot        # Specific agent
openclaw sandbox recreate --browser            # Only browser containers
openclaw sandbox recreate --all --force        # Skip confirmation
```

**Options:**

- `--all`: Recreate all sandbox containers
- `--session <key>`: Recreate container for specific session
- `--agent <id>`: Recreate containers for specific agent
- `--browser`: Only recreate browser containers
- `--force`: Skip confirmation prompt

**Important:** Runtimes are automatically recreated when the agent is next used.

## Use Cases

### After updating a Docker image

```bash
# Pull new image
docker pull openclaw-sandbox:latest
docker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim

# Update config to use new image
# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image)

# Recreate containers
openclaw sandbox recreate --all
```

### After changing sandbox configuration

```bash
# Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*)

# Recreate to apply new config
openclaw sandbox recreate --all
```

### After changing SSH target or SSH auth material

```bash
# Edit config:
# - agents.defaults.sandbox.backend
# - agents.defaults.sandbox.ssh.target
# - agents.defaults.sandbox.ssh.workspaceRoot
# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile
# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData

openclaw sandbox recreate --all
```

For the core `ssh` backend, recreate deletes the per-scope remote workspace root
on the SSH target. The next run seeds it again from the local workspace.

### After changing OpenShell source, policy, or mode

```bash
# Edit config:
# - agents.defaults.sandbox.backend
# - plugins.entries.openshell.config.from
# - plugins.entries.openshell.config.mode
# - plugins.entries.openshell.config.policy

openclaw sandbox recreate --all
```

For OpenShell `remote` mode, recreate deletes the canonical remote workspace
for that scope. The next run seeds it again from the local workspace.

### After changing setupCommand

```bash
openclaw sandbox recreate --all
# or just one agent:
openclaw sandbox recreate --agent family
```

### For a specific agent only

```bash
# Update only one agent's containers
openclaw sandbox recreate --agent alfred
```

## Why is this needed?

**Problem:** When you update sandbox configuration:

- Existing runtimes continue running with old settings
- Runtimes are only pruned after 24h of inactivity
- Regularly-used agents keep old runtimes alive indefinitely

**Solution:** Use `openclaw sandbox recreate` to force removal of old runtimes. They'll be recreated automatically with current settings when next needed.

Tip: prefer `openclaw sandbox recreate` over manual backend-specific cleanup.
It uses the Gateway’s runtime registry and avoids mismatches when scope/session keys change.

## Configuration

Sandbox settings live in `~/.openclaw/openclaw.json` under `agents.defaults.sandbox` (per-agent overrides go in `agents.list[].sandbox`):

```jsonc
{
  "agents": {
    "defaults": {
      "sandbox": {
        "mode": "all", // off, non-main, all
        "backend": "docker", // docker, ssh, openshell
        "scope": "agent", // session, agent, shared
        "docker": {
          "image": "openclaw-sandbox:bookworm-slim",
          "containerPrefix": "openclaw-sbx-",
          // ... more Docker options
        },
        "prune": {
          "idleHours": 24, // Auto-prune after 24h idle
          "maxAgeDays": 7, // Auto-prune after 7 days
        },
      },
    },
  },
}
```

## See Also


```

## File: secrets.md
```
---
summary: "CLI reference for `openclaw secrets` (reload, audit, configure, apply)"
read_when:
  - Re-resolving secret refs at runtime
  - Auditing plaintext residues and unresolved refs
  - Configuring SecretRefs and applying one-way scrub changes
title: "secrets"
---

# `openclaw secrets`

Use `openclaw secrets` to manage SecretRefs and keep the active runtime snapshot healthy.

Command roles:

- `reload`: gateway RPC (`secrets.reload`) that re-resolves refs and swaps runtime snapshot only on full success (no config writes).
- `audit`: read-only scan of configuration/auth/generated-model stores and legacy residues for plaintext, unresolved refs, and precedence drift (exec refs are skipped unless `--allow-exec` is set).
- `configure`: interactive planner for provider setup, target mapping, and preflight (TTY required).
- `apply`: execute a saved plan (`--dry-run` for validation only; dry-run skips exec checks by default, and write mode rejects exec-containing plans unless `--allow-exec` is set), then scrub targeted plaintext residues.

Recommended operator loop:

```bash
openclaw secrets audit --check
openclaw secrets configure
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json
openclaw secrets audit --check
openclaw secrets reload
```

If your plan includes `exec` SecretRefs/providers, pass `--allow-exec` on both dry-run and write apply commands.

Exit code note for CI/gates:

- `audit --check` returns `1` on findings.
- unresolved refs return `2`.

Related:


## Reload runtime snapshot

Re-resolve secret refs and atomically swap runtime snapshot.

```bash
openclaw secrets reload
openclaw secrets reload --json
openclaw secrets reload --url ws://127.0.0.1:18789 --token <token>
```

Notes:

- Uses gateway RPC method `secrets.reload`.
- If resolution fails, gateway keeps last-known-good snapshot and returns an error (no partial activation).
- JSON response includes `warningCount`.

Options:

- `--url <url>`
- `--token <token>`
- `--timeout <ms>`
- `--json`

## Audit

Scan OpenClaw state for:

- plaintext secret storage
- unresolved refs
- precedence drift (`auth-profiles.json` credentials shadowing `openclaw.json` refs)
- generated `agents/*/agent/models.json` residues (provider `apiKey` values and sensitive provider headers)
- legacy residues (legacy auth store entries, OAuth reminders)

Header residue note:

- Sensitive provider header detection is name-heuristic based (common auth/credential header names and fragments such as `authorization`, `x-api-key`, `token`, `secret`, `password`, and `credential`).

```bash
openclaw secrets audit
openclaw secrets audit --check
openclaw secrets audit --json
openclaw secrets audit --allow-exec
```

Exit behavior:

- `--check` exits non-zero on findings.
- unresolved refs exit with higher-priority non-zero code.

Report shape highlights:

- `status`: `clean | findings | unresolved`
- `resolution`: `refsChecked`, `skippedExecRefs`, `resolvabilityComplete`
- `summary`: `plaintextCount`, `unresolvedRefCount`, `shadowedRefCount`, `legacyResidueCount`
- finding codes:
  - `PLAINTEXT_FOUND`
  - `REF_UNRESOLVED`
  - `REF_SHADOWED`
  - `LEGACY_RESIDUE`

## Configure (interactive helper)

Build provider and SecretRef changes interactively, run preflight, and optionally apply:

```bash
openclaw secrets configure
openclaw secrets configure --plan-out /tmp/openclaw-secrets-plan.json
openclaw secrets configure --apply --yes
openclaw secrets configure --providers-only
openclaw secrets configure --skip-provider-setup
openclaw secrets configure --agent ops
openclaw secrets configure --json
```

Flow:

- Provider setup first (`add/edit/remove` for `secrets.providers` aliases).
- Credential mapping second (select fields and assign `{source, provider, id}` refs).
- Preflight and optional apply last.

Flags:

- `--providers-only`: configure `secrets.providers` only, skip credential mapping.
- `--skip-provider-setup`: skip provider setup and map credentials to existing providers.
- `--agent <id>`: scope `auth-profiles.json` target discovery and writes to one agent store.
- `--allow-exec`: allow exec SecretRef checks during preflight/apply (may execute provider commands).

Notes:

- Requires an interactive TTY.
- You cannot combine `--providers-only` with `--skip-provider-setup`.
- `configure` targets secret-bearing fields in `openclaw.json` plus `auth-profiles.json` for the selected agent scope.
- `configure` supports creating new `auth-profiles.json` mappings directly in the picker flow.
- It performs preflight resolution before apply.
- If preflight/apply includes exec refs, keep `--allow-exec` set for both steps.
- Generated plans default to scrub options (`scrubEnv`, `scrubAuthProfilesForProviderTargets`, `scrubLegacyAuthJson` all enabled).
- Apply path is one-way for scrubbed plaintext values.
- Without `--apply`, CLI still prompts `Apply this plan now?` after preflight.
- With `--apply` (and no `--yes`), CLI prompts an extra irreversible confirmation.
- `--json` prints the plan + preflight report, but the command still requires an interactive TTY.

Exec provider safety note:

- Homebrew installs often expose symlinked binaries under `/opt/homebrew/bin/*`.
- Set `allowSymlinkCommand: true` only when needed for trusted package-manager paths, and pair it with `trustedDirs` (for example `["/opt/homebrew"]`).
- On Windows, if ACL verification is unavailable for a provider path, OpenClaw fails closed. For trusted paths only, set `allowInsecurePath: true` on that provider to bypass path security checks.

## Apply a saved plan

Apply or preflight a plan generated previously:

```bash
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-exec
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-exec
openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --json
```

Exec behavior:

- `--dry-run` validates preflight without writing files.
- exec SecretRef checks are skipped by default in dry-run.
- write mode rejects plans that contain exec SecretRefs/providers unless `--allow-exec` is set.
- Use `--allow-exec` to opt in to exec provider checks/execution in either mode.

Plan contract details (allowed target paths, validation rules, and failure semantics):


What `apply` may update:

- `openclaw.json` (SecretRef targets + provider upserts/deletes)
- `auth-profiles.json` (provider-target scrubbing)
- legacy `auth.json` residues
- `~/.openclaw/.env` known secret keys whose values were migrated

## Why no rollback backups

`secrets apply` intentionally does not write rollback backups containing old plaintext values.

Safety comes from strict preflight + atomic-ish apply with best-effort in-memory restore on failure.

## Example

```bash
openclaw secrets audit --check
openclaw secrets configure
openclaw secrets audit --check
```

If `audit --check` still reports plaintext findings, update the remaining reported target paths and rerun audit.

```

## File: security.md
```
---
summary: "CLI reference for `openclaw security` (audit and fix common security footguns)"
read_when:
  - You want to run a quick security audit on config/state
  - You want to apply safe “fix” suggestions (permissions, tighten defaults)
title: "security"
---

# `openclaw security`

Security tools (audit + optional fixes).

Related:


## Audit

```bash
openclaw security audit
openclaw security audit --deep
openclaw security audit --deep --password <password>
openclaw security audit --deep --token <token>
openclaw security audit --fix
openclaw security audit --json
```

The audit warns when multiple DM senders share the main session and recommends **secure DM mode**: `session.dmScope="per-channel-peer"` (or `per-account-channel-peer` for multi-account channels) for shared inboxes.
This is for cooperative/shared inbox hardening. A single Gateway shared by mutually untrusted/adversarial operators is not a recommended setup; split trust boundaries with separate gateways (or separate OS users/hosts).
It also emits `security.trust_model.multi_user_heuristic` when config suggests likely shared-user ingress (for example open DM/group policy, configured group targets, or wildcard sender rules), and reminds you that OpenClaw is a personal-assistant trust model by default.
For intentional shared-user setups, the audit guidance is to sandbox all sessions, keep filesystem access workspace-scoped, and keep personal/private identities or credentials off that runtime.
It also warns when small models (`<=300B`) are used without sandboxing and with web/browser tools enabled.
For webhook ingress, it warns when `hooks.token` reuses the Gateway token, when `hooks.token` is short, when `hooks.path="/"`, when `hooks.defaultSessionKey` is unset, when `hooks.allowedAgentIds` is unrestricted, when request `sessionKey` overrides are enabled, and when overrides are enabled without `hooks.allowedSessionKeyPrefixes`.
It also warns when sandbox Docker settings are configured while sandbox mode is off, when `gateway.nodes.denyCommands` uses ineffective pattern-like/unknown entries (exact node command-name matching only, not shell-text filtering), when `gateway.nodes.allowCommands` explicitly enables dangerous node commands, when global `tools.profile="minimal"` is overridden by agent tool profiles, when open groups expose runtime/filesystem tools without sandbox/workspace guards, and when installed extension plugin tools may be reachable under permissive tool policy.
It also flags `gateway.allowRealIpFallback=true` (header-spoofing risk if proxies are misconfigured) and `discovery.mdns.mode="full"` (metadata leakage via mDNS TXT records).
It also warns when sandbox browser uses Docker `bridge` network without `sandbox.browser.cdpSourceRange`.
It also flags dangerous sandbox Docker network modes (including `host` and `container:*` namespace joins).
It also warns when existing sandbox browser Docker containers have missing/stale hash labels (for example pre-migration containers missing `openclaw.browserConfigEpoch`) and recommends `openclaw sandbox recreate --browser --all`.
It also warns when npm-based plugin/hook install records are unpinned, missing integrity metadata, or drift from currently installed package versions.
It warns when channel allowlists rely on mutable names/emails/tags instead of stable IDs (Discord, Slack, Google Chat, Microsoft Teams, Mattermost, IRC scopes where applicable).
It warns when `gateway.auth.mode="none"` leaves Gateway HTTP APIs reachable without a shared secret (`/tools/invoke` plus any enabled `/v1/*` endpoint).
Settings prefixed with `dangerous`/`dangerously` are explicit break-glass operator overrides; enabling one is not, by itself, a security vulnerability report.
For the complete dangerous-parameter inventory, see the "Insecure or dangerous flags summary" section in [Security](/gateway/security).

SecretRef behavior:

- `security audit` resolves supported SecretRefs in read-only mode for its targeted paths.
- If a SecretRef is unavailable in the current command path, audit continues and reports `secretDiagnostics` (instead of crashing).
- `--token` and `--password` only override deep-probe auth for that command invocation; they do not rewrite config or SecretRef mappings.

## JSON output

Use `--json` for CI/policy checks:

```bash
openclaw security audit --json | jq '.summary'
openclaw security audit --deep --json | jq '.findings[] | select(.severity=="critical") | .checkId'
```

If `--fix` and `--json` are combined, output includes both fix actions and final report:

```bash
openclaw security audit --fix --json | jq '{fix: .fix.ok, summary: .report.summary}'
```

## What `--fix` changes

`--fix` applies safe, deterministic remediations:

- flips common `groupPolicy="open"` to `groupPolicy="allowlist"` (including account variants in supported channels)
- when WhatsApp group policy flips to `allowlist`, seeds `groupAllowFrom` from
  the stored `allowFrom` file when that list exists and config does not already
  define `allowFrom`
- sets `logging.redactSensitive` from `"off"` to `"tools"`
- tightens permissions for state/config and common sensitive files
  (`credentials/*.json`, `auth-profiles.json`, `sessions.json`, session
  `*.jsonl`)
- also tightens config include files referenced from `openclaw.json`
- uses `chmod` on POSIX hosts and `icacls` resets on Windows

`--fix` does **not**:

- rotate tokens/passwords/API keys
- disable tools (`gateway`, `cron`, `exec`, etc.)
- change gateway bind/auth/network exposure choices
- remove or rewrite plugins/skills

```

## File: sessions.md
```
---
summary: "CLI reference for `openclaw sessions` (list stored sessions + usage)"
read_when:
  - You want to list stored sessions and see recent activity
title: "sessions"
---

# `openclaw sessions`

List stored conversation sessions.

```bash
openclaw sessions
openclaw sessions --agent work
openclaw sessions --all-agents
openclaw sessions --active 120
openclaw sessions --verbose
openclaw sessions --json
```

Scope selection:

- default: configured default agent store
- `--verbose`: verbose logging
- `--agent <id>`: one configured agent store
- `--all-agents`: aggregate all configured agent stores
- `--store <path>`: explicit store path (cannot be combined with `--agent` or `--all-agents`)

`openclaw sessions --all-agents` reads configured agent stores. Gateway and ACP
session discovery are broader: they also include disk-only stores found under
the default `agents/` root or a templated `session.store` root. Those
discovered stores must resolve to regular `sessions.json` files inside the
agent root; symlinks and out-of-root paths are skipped.

JSON examples:

`openclaw sessions --all-agents --json`:

```json
{
  "path": null,
  "stores": [
    { "agentId": "main", "path": "/home/user/.openclaw/agents/main/sessions/sessions.json" },
    { "agentId": "work", "path": "/home/user/.openclaw/agents/work/sessions/sessions.json" }
  ],
  "allAgents": true,
  "count": 2,
  "activeMinutes": null,
  "sessions": [
    { "agentId": "main", "key": "agent:main:main", "model": "gpt-5" },
    { "agentId": "work", "key": "agent:work:main", "model": "claude-opus-4-6" }
  ]
}
```

## Cleanup maintenance

Run maintenance now (instead of waiting for the next write cycle):

```bash
openclaw sessions cleanup --dry-run
openclaw sessions cleanup --agent work --dry-run
openclaw sessions cleanup --all-agents --dry-run
openclaw sessions cleanup --enforce
openclaw sessions cleanup --enforce --active-key "agent:main:telegram:direct:123"
openclaw sessions cleanup --json
```

`openclaw sessions cleanup` uses `session.maintenance` settings from config:


- `--dry-run`: preview how many entries would be pruned/capped without writing.
  - In text mode, dry-run prints a per-session action table (`Action`, `Key`, `Age`, `Model`, `Flags`) so you can see what would be kept vs removed.
- `--enforce`: apply maintenance even when `session.maintenance.mode` is `warn`.
- `--fix-missing`: remove entries whose transcript files are missing, even if they would not normally age/count out yet.
- `--active-key <key>`: protect a specific active key from disk-budget eviction.
- `--agent <id>`: run cleanup for one configured agent store.
- `--all-agents`: run cleanup for all configured agent stores.
- `--store <path>`: run against a specific `sessions.json` file.
- `--json`: print a JSON summary. With `--all-agents`, output includes one summary per store.

`openclaw sessions cleanup --all-agents --dry-run --json`:

```json
{
  "allAgents": true,
  "mode": "warn",
  "dryRun": true,
  "stores": [
    {
      "agentId": "main",
      "storePath": "/home/user/.openclaw/agents/main/sessions/sessions.json",
      "beforeCount": 120,
      "afterCount": 80,
      "pruned": 40,
      "capped": 0
    },
    {
      "agentId": "work",
      "storePath": "/home/user/.openclaw/agents/work/sessions/sessions.json",
      "beforeCount": 18,
      "afterCount": 18,
      "pruned": 0,
      "capped": 0
    }
  ]
}
```

Related:


```

## File: setup.md
```
---
summary: "CLI reference for `openclaw setup` (initialize config + workspace)"
read_when:
  - You’re doing first-run setup without full CLI onboarding
  - You want to set the default workspace path
title: "setup"
---

# `openclaw setup`

Initialize `~/.openclaw/openclaw.json` and the agent workspace.

Related:


## Examples

```bash
openclaw setup
openclaw setup --workspace ~/.openclaw/workspace
openclaw setup --wizard
openclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
```

## Options

- `--workspace <dir>`: agent workspace directory (stored as `agents.defaults.workspace`)
- `--wizard`: run onboarding
- `--non-interactive`: run onboarding without prompts
- `--mode <local|remote>`: onboarding mode
- `--remote-url <url>`: remote Gateway WebSocket URL
- `--remote-token <token>`: remote Gateway token

To run onboarding via setup:

```bash
openclaw setup --wizard
```

Notes:

- Plain `openclaw setup` initializes config + workspace without the full onboarding flow.
- Onboarding auto-runs when any onboarding flags are present (`--wizard`, `--non-interactive`, `--mode`, `--remote-url`, `--remote-token`).

```

## File: SKILL.md
```
---
agent_id: cli
primary_domain: engineering
---

# Skill Profile: cli

## 1. Core Capabilities
- `execute_cli_workflow()`: Initiates standard routines based on the assimilated data.
- `evaluate_structural_logic()`: Reads internal templates to generate results.

## 2. Constraints
- Strictly sandboxed to engineering region.
- Requires OMA Architect approval for global state changes.

```

## File: skills.md
```
---
summary: "CLI reference for `openclaw skills` (search/install/update/list/info/check)"
read_when:
  - You want to see which skills are available and ready to run
  - You want to search, install, or update skills from ClawHub
  - You want to debug missing binaries/env/config for skills
title: "skills"
---

# `openclaw skills`

Inspect local skills and install/update skills from ClawHub.

Related:


## Commands

```bash
openclaw skills search "calendar"
openclaw skills search --limit 20 --json
openclaw skills install <slug>
openclaw skills install <slug> --version <version>
openclaw skills install <slug> --force
openclaw skills update <slug>
openclaw skills update --all
openclaw skills list
openclaw skills list --eligible
openclaw skills list --json
openclaw skills list --verbose
openclaw skills info <name>
openclaw skills info <name> --json
openclaw skills check
openclaw skills check --json
```

`search`/`install`/`update` use ClawHub directly and install into the active
workspace `skills/` directory. `list`/`info`/`check` still inspect the local
skills visible to the current workspace and config.

This CLI `install` command downloads skill folders from ClawHub. Gateway-backed
skill dependency installs triggered from onboarding or Skills settings use the
separate `skills.install` request path instead.

Notes:

- `search [query...]` accepts an optional query; omit it to browse the default
  ClawHub search feed.
- `search --limit <n>` caps returned results.
- `install --force` overwrites an existing workspace skill folder for the same
  slug.
- `update --all` only updates tracked ClawHub installs in the active workspace.
- `list` is the default action when no subcommand is provided.
- `list`, `info`, and `check` write their rendered output to stdout. With
  `--json`, that means the machine-readable payload stays on stdout for pipes
  and scripts.

```

## File: status.md
```
---
summary: "CLI reference for `openclaw status` (diagnostics, probes, usage snapshots)"
read_when:
  - You want a quick diagnosis of channel health + recent session recipients
  - You want a pasteable “all” status for debugging
title: "status"
---

# `openclaw status`

Diagnostics for channels + sessions.

```bash
openclaw status
openclaw status --all
openclaw status --deep
openclaw status --usage
```

Notes:

- `--deep` runs live probes (WhatsApp Web + Telegram + Discord + Slack + Signal).
- `--usage` prints normalized provider usage windows as `X% left`.
- MiniMax's raw `usage_percent` / `usagePercent` fields are remaining quota, so OpenClaw inverts them before display; count-based fields win when present. `model_remains` responses prefer the chat-model entry, derive the window label from timestamps when needed, and include the model name in the plan label.
- When the current session snapshot is sparse, `/status` can backfill token and cache counters from the most recent transcript usage log. Existing nonzero live values still win over transcript fallback values.
- Transcript fallback can also recover the active runtime model label when the live session entry is missing it. If that transcript model differs from the selected model, status resolves the context window against the recovered runtime model instead of the selected one.
- For prompt-size accounting, transcript fallback prefers the larger prompt-oriented total when session metadata is missing or smaller, so custom-provider sessions do not collapse to `0` token displays.
- Output includes per-agent session stores when multiple agents are configured.
- Overview includes Gateway + node host service install/runtime status when available.
- Overview includes update channel + git SHA (for source checkouts).
- Read-only status surfaces (`status`, `status --json`, `status --all`) resolve supported SecretRefs for their targeted config paths when possible.
- If a supported channel SecretRef is configured but unavailable in the current command path, status stays read-only and reports degraded output instead of crashing. Human output shows warnings such as “configured token unavailable in this command path”, and JSON output includes `secretDiagnostics`.
- When command-local SecretRef resolution succeeds, status prefers the resolved snapshot and clears transient “secret unavailable” channel markers from the final output.
- `status --all` includes a Secrets overview row and a diagnosis section that summarizes secret diagnostics (truncated for readability) without stopping report generation.

```

## File: system.md
```
---
summary: "CLI reference for `openclaw system` (system events, heartbeat, presence)"
read_when:
  - You want to enqueue a system event without creating a cron job
  - You need to enable or disable heartbeats
  - You want to inspect system presence entries
title: "system"
---

# `openclaw system`

System-level helpers for the Gateway: enqueue system events, control heartbeats,
and view presence.

All `system` subcommands use Gateway RPC and accept the shared client flags:

- `--url <url>`
- `--token <token>`
- `--timeout <ms>`
- `--expect-final`

## Common commands

```bash
openclaw system event --text "Check for urgent follow-ups" --mode now
openclaw system event --text "Check for urgent follow-ups" --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
openclaw system heartbeat enable
openclaw system heartbeat last
openclaw system presence
```

## `system event`

Enqueue a system event on the **main** session. The next heartbeat will inject
it as a `System:` line in the prompt. Use `--mode now` to trigger the heartbeat
immediately; `next-heartbeat` waits for the next scheduled tick.

Flags:

- `--text <text>`: required system event text.
- `--mode <mode>`: `now` or `next-heartbeat` (default).
- `--json`: machine-readable output.
- `--url`, `--token`, `--timeout`, `--expect-final`: shared Gateway RPC flags.

## `system heartbeat last|enable|disable`

Heartbeat controls:

- `last`: show the last heartbeat event.
- `enable`: turn heartbeats back on (use this if they were disabled).
- `disable`: pause heartbeats.

Flags:

- `--json`: machine-readable output.
- `--url`, `--token`, `--timeout`, `--expect-final`: shared Gateway RPC flags.

## `system presence`

List the current system presence entries the Gateway knows about (nodes,
instances, and similar status lines).

Flags:

- `--json`: machine-readable output.
- `--url`, `--token`, `--timeout`, `--expect-final`: shared Gateway RPC flags.

## Notes

- Requires a running Gateway reachable by your current config (local or remote).
- System events are ephemeral and not persisted across restarts.

```

## File: test_branch_command.py
```
"""Tests for the /branch (/fork) command — session branching.

Verifies that:
- Branching creates a new session with copied conversation history
- The original session is preserved (ended with "branched" reason)
- Auto-generated titles use lineage numbering
- Custom branch names are used when provided
- parent_session_id links are set correctly
- Edge cases: empty conversation, missing session DB
"""

import os
import uuid
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch, PropertyMock

import pytest


@pytest.fixture
def session_db(tmp_path):
    """Create a real SessionDB for testing."""
    os.environ["HERMES_HOME"] = str(tmp_path / ".hermes")
    os.makedirs(tmp_path / ".hermes", exist_ok=True)
    from hermes_state import SessionDB
    db = SessionDB(db_path=tmp_path / ".hermes" / "test_sessions.db")
    yield db
    db.close()


@pytest.fixture
def cli_instance(tmp_path, session_db):
    """Create a minimal HermesCLI-like object for testing _handle_branch_command."""
    # We'll mock the CLI enough to test the branch logic without full init
    from unittest.mock import MagicMock

    cli = MagicMock()
    cli._session_db = session_db
    cli.session_id = "20260403_120000_abc123"
    cli.model = "anthropic/claude-sonnet-4.6"
    cli.max_turns = 90
    cli.reasoning_config = {"enabled": True, "effort": "medium"}
    cli.session_start = datetime.now()
    cli._pending_title = None
    cli._resumed = False
    cli.agent = None
    cli.conversation_history = [
        {"role": "user", "content": "Hello, can you help me?"},
        {"role": "assistant", "content": "Of course! How can I help?"},
        {"role": "user", "content": "Write a Python function to sort a list."},
        {"role": "assistant", "content": "def sort_list(lst): return sorted(lst)"},
    ]

    # Create the original session in the DB
    session_db.create_session(
        session_id=cli.session_id,
        source="cli",
        model=cli.model,
    )
    session_db.set_session_title(cli.session_id, "My Coding Session")

    return cli


class TestBranchCommandCLI:
    """Test the /branch command logic for the CLI."""

    def test_branch_creates_new_session(self, cli_instance, session_db):
        """Branching should create a new session in the DB."""
        from cli import HermesCLI

        # Call the real method on the mock, using the real implementation
        HermesCLI._handle_branch_command(cli_instance, "/branch")

        # Verify a new session was created
        assert cli_instance.session_id != "20260403_120000_abc123"
        new_session = session_db.get_session(cli_instance.session_id)
        assert new_session is not None

    def test_branch_copies_history(self, cli_instance, session_db):
        """Branching should copy all messages to the new session."""
        from cli import HermesCLI

        HermesCLI._handle_branch_command(cli_instance, "/branch")

        messages = session_db.get_messages_as_conversation(cli_instance.session_id)
        assert len(messages) == 4  # All 4 messages copied

    def test_branch_preserves_parent_link(self, cli_instance, session_db):
        """The new session should reference the original as parent."""
        from cli import HermesCLI
        original_id = cli_instance.session_id

        HermesCLI._handle_branch_command(cli_instance, "/branch")

        new_session = session_db.get_session(cli_instance.session_id)
        assert new_session["parent_session_id"] == original_id

    def test_branch_ends_original_session(self, cli_instance, session_db):
        """The original session should be marked as ended with 'branched' reason."""
        from cli import HermesCLI
        original_id = cli_instance.session_id

        HermesCLI._handle_branch_command(cli_instance, "/branch")

        original = session_db.get_session(original_id)
        assert original["end_reason"] == "branched"

    def test_branch_with_custom_name(self, cli_instance, session_db):
        """Custom branch name should be used as the title."""
        from cli import HermesCLI

        HermesCLI._handle_branch_command(cli_instance, "/branch refactor approach")

        title = session_db.get_session_title(cli_instance.session_id)
        assert title == "refactor approach"

    def test_branch_auto_title_lineage(self, cli_instance, session_db):
        """Without a name, branch should auto-generate a title from the parent's title."""
        from cli import HermesCLI

        HermesCLI._handle_branch_command(cli_instance, "/branch")

        title = session_db.get_session_title(cli_instance.session_id)
        assert title == "My Coding Session #2"

    def test_branch_empty_conversation(self, cli_instance, session_db):
        """Branching with no history should show an error."""
        from cli import HermesCLI
        cli_instance.conversation_history = []

        HermesCLI._handle_branch_command(cli_instance, "/branch")

        # session_id should not have changed
        assert cli_instance.session_id == "20260403_120000_abc123"

    def test_branch_no_session_db(self, cli_instance):
        """Branching without a session DB should show an error."""
        from cli import HermesCLI
        cli_instance._session_db = None

        HermesCLI._handle_branch_command(cli_instance, "/branch")

        # session_id should not have changed
        assert cli_instance.session_id == "20260403_120000_abc123"

    def test_branch_syncs_agent(self, cli_instance, session_db):
        """If an agent is active, branch should sync it to the new session."""
        from cli import HermesCLI

        agent = MagicMock()
        agent._last_flushed_db_idx = 0
        cli_instance.agent = agent

        HermesCLI._handle_branch_command(cli_instance, "/branch")

        # Agent should have been updated
        assert agent.session_id == cli_instance.session_id
        assert agent.reset_session_state.called
        assert agent._last_flushed_db_idx == 4  # len(conversation_history)

    def test_branch_sets_resumed_flag(self, cli_instance, session_db):
        """Branch should set _resumed=True to prevent auto-title generation."""
        from cli import HermesCLI

        HermesCLI._handle_branch_command(cli_instance, "/branch")

        assert cli_instance._resumed is True

    def test_fork_alias(self):
        """The /fork alias should resolve to 'branch'."""
        from hermes_cli.commands import resolve_command
        result = resolve_command("fork")
        assert result is not None
        assert result.name == "branch"


class TestBranchCommandDef:
    """Test the CommandDef registration for /branch."""

    def test_branch_in_registry(self):
        """The branch command should be in the command registry."""
        from hermes_cli.commands import COMMAND_REGISTRY
        names = [c.name for c in COMMAND_REGISTRY]
        assert "branch" in names

    def test_branch_has_fork_alias(self):
        """The branch command should have 'fork' as an alias."""
        from hermes_cli.commands import COMMAND_REGISTRY
        branch = next(c for c in COMMAND_REGISTRY if c.name == "branch")
        assert "fork" in branch.aliases

    def test_branch_in_session_category(self):
        """The branch command should be in the Session category."""
        from hermes_cli.commands import COMMAND_REGISTRY
        branch = next(c for c in COMMAND_REGISTRY if c.name == "branch")
        assert branch.category == "Session"

```

## File: test_cli_approval_ui.py
```
import queue
import threading
import time
from types import SimpleNamespace
from unittest.mock import MagicMock

from cli import HermesCLI


def _make_cli_stub():
    cli = HermesCLI.__new__(HermesCLI)
    cli._approval_state = None
    cli._approval_deadline = 0
    cli._approval_lock = threading.Lock()
    cli._invalidate = MagicMock()
    cli._app = SimpleNamespace(invalidate=MagicMock())
    return cli


class TestCliApprovalUi:
    def test_approval_callback_includes_view_for_long_commands(self):
        cli = _make_cli_stub()
        command = "sudo dd if=/tmp/githubcli-keyring.gpg of=/usr/share/keyrings/githubcli-archive-keyring.gpg bs=4M status=progress"
        result = {}

        def _run_callback():
            result["value"] = cli._approval_callback(command, "disk copy")

        thread = threading.Thread(target=_run_callback, daemon=True)
        thread.start()

        deadline = time.time() + 2
        while cli._approval_state is None and time.time() < deadline:
            time.sleep(0.01)

        assert cli._approval_state is not None
        assert "view" in cli._approval_state["choices"]

        cli._approval_state["response_queue"].put("deny")
        thread.join(timeout=2)
        assert result["value"] == "deny"

    def test_handle_approval_selection_view_expands_in_place(self):
        cli = _make_cli_stub()
        cli._approval_state = {
            "command": "sudo dd if=/tmp/in of=/usr/share/keyrings/githubcli-archive-keyring.gpg bs=4M status=progress",
            "description": "disk copy",
            "choices": ["once", "session", "always", "deny", "view"],
            "selected": 4,
            "response_queue": queue.Queue(),
        }

        cli._handle_approval_selection()

        assert cli._approval_state is not None
        assert cli._approval_state["show_full"] is True
        assert "view" not in cli._approval_state["choices"]
        assert cli._approval_state["selected"] == 3
        assert cli._approval_state["response_queue"].empty()

    def test_approval_display_places_title_inside_box_not_border(self):
        cli = _make_cli_stub()
        cli._approval_state = {
            "command": "sudo dd if=/tmp/in of=/usr/share/keyrings/githubcli-archive-keyring.gpg bs=4M status=progress",
            "description": "disk copy",
            "choices": ["once", "session", "always", "deny", "view"],
            "selected": 0,
            "response_queue": queue.Queue(),
        }

        fragments = cli._get_approval_display_fragments()
        rendered = "".join(text for _style, text in fragments)
        lines = rendered.splitlines()

        assert lines[0].startswith("╭")
        assert "Dangerous Command" not in lines[0]
        assert any("Dangerous Command" in line for line in lines[1:3])
        assert "Show full command" in rendered
        assert "githubcli-archive-keyring.gpg" not in rendered

    def test_approval_display_shows_full_command_after_view(self):
        cli = _make_cli_stub()
        full_command = "sudo dd if=/tmp/in of=/usr/share/keyrings/githubcli-archive-keyring.gpg bs=4M status=progress"
        cli._approval_state = {
            "command": full_command,
            "description": "disk copy",
            "choices": ["once", "session", "always", "deny"],
            "selected": 0,
            "show_full": True,
            "response_queue": queue.Queue(),
        }

        fragments = cli._get_approval_display_fragments()
        rendered = "".join(text for _style, text in fragments)

        assert "..." not in rendered
        assert "githubcli-" in rendered
        assert "archive-" in rendered
        assert "keyring.gpg" in rendered
        assert "status=progress" in rendered

```

## File: test_cli_background_tui_refresh.py
```
"""Tests for CLI background command TUI refresh behavior.

Ensures the TUI is properly refreshed before printing background task output
to prevent spinner/status bar overlap (#2718).
"""

import threading
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from cli import HermesCLI


def _make_cli():
    """Create a minimal HermesCLI instance for testing."""
    cli_obj = HermesCLI.__new__(HermesCLI)
    cli_obj.model = "test-model"
    cli_obj._background_tasks = {}
    cli_obj._background_task_counter = 0
    cli_obj.conversation_history = []
    cli_obj.agent = None
    cli_obj._app = None
    return cli_obj


class TestBackgroundCommandTuiRefresh:
    """Tests for TUI refresh in background command output."""

    def test_invalidate_called_before_success_output(self):
        """App.invalidate() is called before printing background success output."""
        cli_obj = _make_cli()
        mock_app = MagicMock()
        cli_obj._app = mock_app

        # Track call order
        call_order = []
        original_invalidate = mock_app.invalidate

        def track_invalidate():
            call_order.append("invalidate")
            return original_invalidate()

        mock_app.invalidate = track_invalidate

        # Patch print to track when it's called
        with patch("builtins.print") as mock_print:
            mock_print.side_effect = lambda *args, **kwargs: call_order.append("print")

            # Simulate the background task output code path
            if cli_obj._app:
                cli_obj._app.invalidate()
                import time
                time.sleep(0.01)  # reduced for test
            print()

        # Verify invalidate was called before print
        assert call_order[0] == "invalidate"
        assert "print" in call_order

    def test_invalidate_called_before_error_output(self):
        """App.invalidate() is called before printing background error output."""
        cli_obj = _make_cli()
        mock_app = MagicMock()
        cli_obj._app = mock_app

        call_order = []
        mock_app.invalidate.side_effect = lambda: call_order.append("invalidate")

        with patch("builtins.print") as mock_print:
            mock_print.side_effect = lambda *args, **kwargs: call_order.append("print")

            # Simulate error path
            if cli_obj._app:
                cli_obj._app.invalidate()
                import time
                time.sleep(0.01)
            print()

        assert call_order[0] == "invalidate"
        assert "print" in call_order

    def test_no_crash_when_app_is_none(self):
        """No crash when _app is None (non-TUI mode)."""
        cli_obj = _make_cli()
        cli_obj._app = None

        # This should not raise
        if cli_obj._app:
            cli_obj._app.invalidate()
        # If we get here without exception, test passes

    def test_background_task_thread_safety(self):
        """Background task tracking is thread-safe."""
        cli_obj = _make_cli()

        # Simulate adding and removing background tasks
        task_id = "test_task_1"
        cli_obj._background_tasks[task_id] = MagicMock()
        assert task_id in cli_obj._background_tasks

        # Clean up
        cli_obj._background_tasks.pop(task_id, None)
        assert task_id not in cli_obj._background_tasks

```

## File: test_cli_browser_connect.py
```
"""Tests for CLI browser CDP auto-launch helpers."""

import os
from unittest.mock import patch

from cli import HermesCLI


class TestChromeDebugLaunch:
    def test_windows_launch_uses_browser_found_on_path(self):
        captured = {}

        def fake_popen(cmd, **kwargs):
            captured["cmd"] = cmd
            captured["kwargs"] = kwargs
            return object()

        with patch("cli.shutil.which", side_effect=lambda name: r"C:\Chrome\chrome.exe" if name == "chrome.exe" else None), \
             patch("cli.os.path.isfile", side_effect=lambda path: path == r"C:\Chrome\chrome.exe"), \
             patch("subprocess.Popen", side_effect=fake_popen):
            assert HermesCLI._try_launch_chrome_debug(9333, "Windows") is True

        assert captured["cmd"] == [r"C:\Chrome\chrome.exe", "--remote-debugging-port=9333"]
        assert captured["kwargs"]["start_new_session"] is True

    def test_windows_launch_falls_back_to_common_install_dirs(self, monkeypatch):
        captured = {}
        program_files = r"C:\Program Files"
        # Use os.path.join so path separators match cross-platform
        installed = os.path.join(program_files, "Google", "Chrome", "Application", "chrome.exe")

        def fake_popen(cmd, **kwargs):
            captured["cmd"] = cmd
            captured["kwargs"] = kwargs
            return object()

        monkeypatch.setenv("ProgramFiles", program_files)
        monkeypatch.delenv("ProgramFiles(x86)", raising=False)
        monkeypatch.delenv("LOCALAPPDATA", raising=False)

        with patch("cli.shutil.which", return_value=None), \
             patch("cli.os.path.isfile", side_effect=lambda path: path == installed), \
             patch("subprocess.Popen", side_effect=fake_popen):
            assert HermesCLI._try_launch_chrome_debug(9222, "Windows") is True

        assert captured["cmd"] == [installed, "--remote-debugging-port=9222"]

```

## File: test_cli_context_warning.py
```
"""Tests for the low context length warning in the CLI banner."""

import os
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def _isolate(tmp_path, monkeypatch):
    """Isolate HERMES_HOME so tests don't touch real config."""
    home = tmp_path / ".hermes"
    home.mkdir()
    monkeypatch.setenv("HERMES_HOME", str(home))


@pytest.fixture
def cli_obj(_isolate):
    """Create a minimal HermesCLI instance for banner testing."""
    with patch("cli.load_cli_config", return_value={
        "display": {"tool_progress": "new"},
        "terminal": {},
    }), patch("cli.get_tool_definitions", return_value=[]), \
         patch("cli.build_welcome_banner"):
        from cli import HermesCLI
        obj = HermesCLI.__new__(HermesCLI)
        obj.model = "test-model"
        obj.enabled_toolsets = ["hermes-core"]
        obj.compact = False
        obj.console = MagicMock()
        obj.session_id = None
        obj.api_key = "test"
        obj.base_url = ""
        obj.provider = "test"
        obj._provider_source = None
        # Mock agent with context compressor
        obj.agent = SimpleNamespace(
            context_compressor=SimpleNamespace(context_length=None)
        )
        return obj


class TestLowContextWarning:
    """Tests that the CLI warns about low context lengths."""

    def test_no_warning_for_normal_context(self, cli_obj):
        """No warning when context is 32k+."""
        cli_obj.agent.context_compressor.context_length = 32768
        with patch("cli.get_tool_definitions", return_value=[]), \
             patch("cli.build_welcome_banner"):
            cli_obj.show_banner()

        # Check that no yellow warning was printed
        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        warning_calls = [c for c in calls if "too low" in c]
        assert len(warning_calls) == 0

    def test_warning_for_low_context(self, cli_obj):
        """Warning shown when context is 4096 (Ollama default)."""
        cli_obj.agent.context_compressor.context_length = 4096
        with patch("cli.get_tool_definitions", return_value=[]), \
             patch("cli.build_welcome_banner"):
            cli_obj.show_banner()

        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        warning_calls = [c for c in calls if "too low" in c]
        assert len(warning_calls) == 1
        assert "4,096" in warning_calls[0]

    def test_warning_for_2048_context(self, cli_obj):
        """Warning shown for 2048 tokens (common LM Studio default)."""
        cli_obj.agent.context_compressor.context_length = 2048
        with patch("cli.get_tool_definitions", return_value=[]), \
             patch("cli.build_welcome_banner"):
            cli_obj.show_banner()

        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        warning_calls = [c for c in calls if "too low" in c]
        assert len(warning_calls) == 1

    def test_no_warning_at_boundary(self, cli_obj):
        """No warning at exactly 8192 — 8192 is borderline but included in warning."""
        cli_obj.agent.context_compressor.context_length = 8192
        with patch("cli.get_tool_definitions", return_value=[]), \
             patch("cli.build_welcome_banner"):
            cli_obj.show_banner()

        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        warning_calls = [c for c in calls if "too low" in c]
        assert len(warning_calls) == 1  # 8192 is still warned about

    def test_no_warning_above_boundary(self, cli_obj):
        """No warning at 16384."""
        cli_obj.agent.context_compressor.context_length = 16384
        with patch("cli.get_tool_definitions", return_value=[]), \
             patch("cli.build_welcome_banner"):
            cli_obj.show_banner()

        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        warning_calls = [c for c in calls if "too low" in c]
        assert len(warning_calls) == 0

    def test_ollama_specific_hint(self, cli_obj):
        """Ollama-specific fix shown when port 11434 detected."""
        cli_obj.agent.context_compressor.context_length = 4096
        cli_obj.base_url = "http://localhost:11434/v1"
        with patch("cli.get_tool_definitions", return_value=[]), \
             patch("cli.build_welcome_banner"):
            cli_obj.show_banner()

        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        ollama_hints = [c for c in calls if "OLLAMA_CONTEXT_LENGTH" in c]
        assert len(ollama_hints) == 1

    def test_lm_studio_specific_hint(self, cli_obj):
        """LM Studio-specific fix shown when port 1234 detected."""
        cli_obj.agent.context_compressor.context_length = 2048
        cli_obj.base_url = "http://localhost:1234/v1"
        with patch("cli.get_tool_definitions", return_value=[]), \
             patch("cli.build_welcome_banner"):
            cli_obj.show_banner()

        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        lms_hints = [c for c in calls if "LM Studio" in c]
        assert len(lms_hints) == 1

    def test_generic_hint_for_other_servers(self, cli_obj):
        """Generic fix shown for unknown servers."""
        cli_obj.agent.context_compressor.context_length = 4096
        cli_obj.base_url = "http://localhost:8080/v1"
        with patch("cli.get_tool_definitions", return_value=[]), \
             patch("cli.build_welcome_banner"):
            cli_obj.show_banner()

        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        generic_hints = [c for c in calls if "config.yaml" in c]
        assert len(generic_hints) == 1

    def test_no_warning_when_no_context_length(self, cli_obj):
        """No warning when context length is not yet known."""
        cli_obj.agent.context_compressor.context_length = None
        with patch("cli.get_tool_definitions", return_value=[]), \
             patch("cli.build_welcome_banner"):
            cli_obj.show_banner()

        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        warning_calls = [c for c in calls if "too low" in c]
        assert len(warning_calls) == 0

    def test_compact_banner_does_not_crash_on_narrow_terminal(self, cli_obj):
        """Compact mode should still have ctx_len defined for warning logic."""
        cli_obj.agent.context_compressor.context_length = 4096

        with patch("shutil.get_terminal_size", return_value=os.terminal_size((70, 40))), \
             patch("cli._build_compact_banner", return_value="compact banner"):
            cli_obj.show_banner()

        calls = [str(c) for c in cli_obj.console.print.call_args_list]
        warning_calls = [c for c in calls if "too low" in c]
        assert len(warning_calls) == 1

```

## File: test_cli_extension_hooks.py
```
"""Tests for protected HermesCLI TUI extension hooks.

Verifies that wrapper CLIs can extend the TUI via:
  - _get_extra_tui_widgets()
  - _register_extra_tui_keybindings()
  - _build_tui_layout_children()
without overriding run().
"""

from __future__ import annotations

import importlib
import sys
from unittest.mock import MagicMock, patch

from prompt_toolkit.key_binding import KeyBindings


def _make_cli(**kwargs):
    """Create a HermesCLI with prompt_toolkit stubs (same pattern as test_cli_init)."""
    _clean_config = {
        "model": {
            "default": "anthropic/claude-opus-4.6",
            "base_url": "https://openrouter.ai/api/v1",
            "provider": "auto",
        },
        "display": {"compact": False, "tool_progress": "all"},
        "agent": {},
        "terminal": {"env_type": "local"},
    }
    clean_env = {"LLM_MODEL": "", "HERMES_MAX_ITERATIONS": ""}
    prompt_toolkit_stubs = {
        "prompt_toolkit": MagicMock(),
        "prompt_toolkit.history": MagicMock(),
        "prompt_toolkit.styles": MagicMock(),
        "prompt_toolkit.patch_stdout": MagicMock(),
        "prompt_toolkit.application": MagicMock(),
        "prompt_toolkit.layout": MagicMock(),
        "prompt_toolkit.layout.processors": MagicMock(),
        "prompt_toolkit.filters": MagicMock(),
        "prompt_toolkit.layout.dimension": MagicMock(),
        "prompt_toolkit.layout.menus": MagicMock(),
        "prompt_toolkit.widgets": MagicMock(),
        "prompt_toolkit.key_binding": MagicMock(),
        "prompt_toolkit.completion": MagicMock(),
        "prompt_toolkit.formatted_text": MagicMock(),
        "prompt_toolkit.auto_suggest": MagicMock(),
    }
    with patch.dict(sys.modules, prompt_toolkit_stubs), patch.dict(
        "os.environ", clean_env, clear=False
    ):
        import cli as _cli_mod

        _cli_mod = importlib.reload(_cli_mod)
        with patch.object(_cli_mod, "get_tool_definitions", return_value=[]), patch.dict(
            _cli_mod.__dict__, {"CLI_CONFIG": _clean_config}
        ):
            return _cli_mod.HermesCLI(**kwargs)


class TestExtensionHookDefaults:
    def test_extra_tui_widgets_default_empty(self):
        cli = _make_cli()
        assert cli._get_extra_tui_widgets() == []

    def test_register_extra_tui_keybindings_default_noop(self):
        cli = _make_cli()
        kb = KeyBindings()
        result = cli._register_extra_tui_keybindings(kb, input_area=None)
        assert result is None
        assert kb.bindings == []

    def test_build_tui_layout_children_returns_all_widgets_in_order(self):
        cli = _make_cli()
        children = cli._build_tui_layout_children(
            sudo_widget="sudo",
            secret_widget="secret",
            approval_widget="approval",
            clarify_widget="clarify",
            spinner_widget="spinner",
            spacer="spacer",
            status_bar="status",
            input_rule_top="top-rule",
            image_bar="image-bar",
            input_area="input-area",
            input_rule_bot="bottom-rule",
            voice_status_bar="voice-status",
            completions_menu="completions-menu",
        )
        # First element is Window(height=0), rest are the named widgets
        assert children[1:] == [
            "sudo", "secret", "approval", "clarify", "spinner",
            "spacer", "status", "top-rule", "image-bar", "input-area",
            "bottom-rule", "voice-status", "completions-menu",
        ]


class TestExtensionHookSubclass:
    def test_extra_widgets_inserted_before_status_bar(self):
        cli = _make_cli()
        # Monkey-patch to simulate subclass override
        cli._get_extra_tui_widgets = lambda: ["radio-menu", "mini-player"]

        children = cli._build_tui_layout_children(
            sudo_widget="sudo",
            secret_widget="secret",
            approval_widget="approval",
            clarify_widget="clarify",
            spinner_widget="spinner",
            spacer="spacer",
            status_bar="status",
            input_rule_top="top-rule",
            image_bar="image-bar",
            input_area="input-area",
            input_rule_bot="bottom-rule",
            voice_status_bar="voice-status",
            completions_menu="completions-menu",
        )
        # Extra widgets should appear between spacer and status bar
        spacer_idx = children.index("spacer")
        status_idx = children.index("status")
        assert children[spacer_idx + 1] == "radio-menu"
        assert children[spacer_idx + 2] == "mini-player"
        assert children[spacer_idx + 3] == "status"
        assert status_idx == spacer_idx + 3

    def test_extra_keybindings_can_add_bindings(self):
        cli = _make_cli()
        kb = KeyBindings()

        def _custom_hook(kb, *, input_area):
            @kb.add("f2")
            def _toggle(event):
                return None

        cli._register_extra_tui_keybindings = _custom_hook
        cli._register_extra_tui_keybindings(kb, input_area=None)
        assert len(kb.bindings) == 1

```

## File: test_cli_file_drop.py
```
"""Tests for _detect_file_drop — file path detection that prevents
dragged/pasted absolute paths from being mistaken for slash commands."""

import os
import tempfile
from pathlib import Path

import pytest

from cli import _detect_file_drop


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def tmp_image(tmp_path):
    """Create a temporary .png file and return its path."""
    img = tmp_path / "screenshot.png"
    img.write_bytes(b"\x89PNG\r\n\x1a\n")  # minimal PNG header
    return img


@pytest.fixture()
def tmp_text(tmp_path):
    """Create a temporary .py file and return its path."""
    f = tmp_path / "main.py"
    f.write_text("print('hello')\n")
    return f


@pytest.fixture()
def tmp_image_with_spaces(tmp_path):
    """Create a file whose name contains spaces (like macOS screenshots)."""
    img = tmp_path / "Screenshot 2026-04-01 at 7.25.32 PM.png"
    img.write_bytes(b"\x89PNG\r\n\x1a\n")
    return img


# ---------------------------------------------------------------------------
# Tests: returns None for non-file inputs
# ---------------------------------------------------------------------------

class TestNonFileInputs:
    def test_regular_slash_command(self):
        assert _detect_file_drop("/help") is None

    def test_unknown_slash_command(self):
        assert _detect_file_drop("/xyz") is None

    def test_slash_command_with_args(self):
        assert _detect_file_drop("/config set key value") is None

    def test_empty_string(self):
        assert _detect_file_drop("") is None

    def test_non_slash_input(self):
        assert _detect_file_drop("hello world") is None

    def test_non_string_input(self):
        assert _detect_file_drop(42) is None

    def test_nonexistent_path(self):
        assert _detect_file_drop("/nonexistent/path/to/file.png") is None

    def test_directory_not_file(self, tmp_path):
        """A directory path should not be treated as a file drop."""
        assert _detect_file_drop(str(tmp_path)) is None


# ---------------------------------------------------------------------------
# Tests: image file detection
# ---------------------------------------------------------------------------

class TestImageFileDrop:
    def test_simple_image_path(self, tmp_image):
        result = _detect_file_drop(str(tmp_image))
        assert result is not None
        assert result["path"] == tmp_image
        assert result["is_image"] is True
        assert result["remainder"] == ""

    def test_image_with_trailing_text(self, tmp_image):
        user_input = f"{tmp_image} analyze this please"
        result = _detect_file_drop(user_input)
        assert result is not None
        assert result["path"] == tmp_image
        assert result["is_image"] is True
        assert result["remainder"] == "analyze this please"

    @pytest.mark.parametrize("ext", [".png", ".jpg", ".jpeg", ".gif", ".webp",
                                      ".bmp", ".tiff", ".tif", ".svg", ".ico"])
    def test_all_image_extensions(self, tmp_path, ext):
        img = tmp_path / f"test{ext}"
        img.write_bytes(b"fake")
        result = _detect_file_drop(str(img))
        assert result is not None
        assert result["is_image"] is True

    def test_uppercase_extension(self, tmp_path):
        img = tmp_path / "photo.JPG"
        img.write_bytes(b"fake")
        result = _detect_file_drop(str(img))
        assert result is not None
        assert result["is_image"] is True


# ---------------------------------------------------------------------------
# Tests: non-image file detection
# ---------------------------------------------------------------------------

class TestNonImageFileDrop:
    def test_python_file(self, tmp_text):
        result = _detect_file_drop(str(tmp_text))
        assert result is not None
        assert result["path"] == tmp_text
        assert result["is_image"] is False
        assert result["remainder"] == ""

    def test_non_image_with_trailing_text(self, tmp_text):
        user_input = f"{tmp_text} review this code"
        result = _detect_file_drop(user_input)
        assert result is not None
        assert result["is_image"] is False
        assert result["remainder"] == "review this code"


# ---------------------------------------------------------------------------
# Tests: backslash-escaped spaces (macOS drag-and-drop)
# ---------------------------------------------------------------------------

class TestEscapedSpaces:
    def test_escaped_spaces_in_path(self, tmp_image_with_spaces):
        r"""macOS drags produce paths like /path/to/my\ file.png"""
        escaped = str(tmp_image_with_spaces).replace(' ', '\\ ')
        result = _detect_file_drop(escaped)
        assert result is not None
        assert result["path"] == tmp_image_with_spaces
        assert result["is_image"] is True

    def test_escaped_spaces_with_trailing_text(self, tmp_image_with_spaces):
        escaped = str(tmp_image_with_spaces).replace(' ', '\\ ')
        user_input = f"{escaped} what is this?"
        result = _detect_file_drop(user_input)
        assert result is not None
        assert result["path"] == tmp_image_with_spaces
        assert result["remainder"] == "what is this?"


# ---------------------------------------------------------------------------
# Tests: edge cases
# ---------------------------------------------------------------------------

class TestEdgeCases:
    def test_path_with_no_extension(self, tmp_path):
        f = tmp_path / "Makefile"
        f.write_text("all:\n\techo hi\n")
        result = _detect_file_drop(str(f))
        assert result is not None
        assert result["is_image"] is False

    def test_path_that_looks_like_command_but_is_file(self, tmp_path):
        """A file literally named 'help' inside a directory starting with /."""
        f = tmp_path / "help"
        f.write_text("not a command\n")
        result = _detect_file_drop(str(f))
        assert result is not None
        assert result["is_image"] is False

    def test_symlink_to_file(self, tmp_image, tmp_path):
        link = tmp_path / "link.png"
        link.symlink_to(tmp_image)
        result = _detect_file_drop(str(link))
        assert result is not None
        assert result["is_image"] is True

```

## File: test_cli_init.py
```
"""Tests for HermesCLI initialization -- catches configuration bugs
that only manifest at runtime (not in mocked unit tests)."""

import os
import sys
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def _make_cli(env_overrides=None, config_overrides=None, **kwargs):
    """Create a HermesCLI instance with minimal mocking."""
    import importlib

    _clean_config = {
        "model": {
            "default": "anthropic/claude-opus-4.6",
            "base_url": "https://openrouter.ai/api/v1",
            "provider": "auto",
        },
        "display": {"compact": False, "tool_progress": "all"},
        "agent": {},
        "terminal": {"env_type": "local"},
    }
    if config_overrides:
        _clean_config.update(config_overrides)
    clean_env = {"LLM_MODEL": "", "HERMES_MAX_ITERATIONS": ""}
    if env_overrides:
        clean_env.update(env_overrides)
    prompt_toolkit_stubs = {
        "prompt_toolkit": MagicMock(),
        "prompt_toolkit.history": MagicMock(),
        "prompt_toolkit.styles": MagicMock(),
        "prompt_toolkit.patch_stdout": MagicMock(),
        "prompt_toolkit.application": MagicMock(),
        "prompt_toolkit.layout": MagicMock(),
        "prompt_toolkit.layout.processors": MagicMock(),
        "prompt_toolkit.filters": MagicMock(),
        "prompt_toolkit.layout.dimension": MagicMock(),
        "prompt_toolkit.layout.menus": MagicMock(),
        "prompt_toolkit.widgets": MagicMock(),
        "prompt_toolkit.key_binding": MagicMock(),
        "prompt_toolkit.completion": MagicMock(),
        "prompt_toolkit.formatted_text": MagicMock(),
        "prompt_toolkit.auto_suggest": MagicMock(),
    }
    with patch.dict(sys.modules, prompt_toolkit_stubs), \
         patch.dict("os.environ", clean_env, clear=False):
        import cli as _cli_mod
        _cli_mod = importlib.reload(_cli_mod)
        with patch.object(_cli_mod, "get_tool_definitions", return_value=[]), \
             patch.dict(_cli_mod.__dict__, {"CLI_CONFIG": _clean_config}):
            return _cli_mod.HermesCLI(**kwargs)


class TestMaxTurnsResolution:
    """max_turns must always resolve to a positive integer, never None."""

    def test_default_max_turns_is_integer(self):
        cli = _make_cli()
        assert isinstance(cli.max_turns, int)
        assert cli.max_turns == 90

    def test_explicit_max_turns_honored(self):
        cli = _make_cli(max_turns=25)
        assert cli.max_turns == 25

    def test_none_max_turns_gets_default(self):
        cli = _make_cli(max_turns=None)
        assert isinstance(cli.max_turns, int)
        assert cli.max_turns == 90

    def test_env_var_max_turns(self):
        """Env var is used when config file doesn't set max_turns."""
        cli_obj = _make_cli(env_overrides={"HERMES_MAX_ITERATIONS": "42"})
        assert cli_obj.max_turns == 42

    def test_legacy_root_max_turns_is_used_when_agent_key_exists_without_value(self):
        cli_obj = _make_cli(config_overrides={"agent": {}, "max_turns": 77})
        assert cli_obj.max_turns == 77

    def test_max_turns_never_none_for_agent(self):
        """The value passed to AIAgent must never be None (causes TypeError in run_conversation)."""
        cli = _make_cli()
        assert isinstance(cli.max_turns, int) and cli.max_turns == 90


class TestVerboseAndToolProgress:
    def test_default_verbose_is_bool(self):
        cli = _make_cli()
        assert isinstance(cli.verbose, bool)

    def test_tool_progress_mode_is_string(self):
        cli = _make_cli()
        assert isinstance(cli.tool_progress_mode, str)
        assert cli.tool_progress_mode in ("off", "new", "all", "verbose")


class TestBusyInputMode:
    def test_default_busy_input_mode_is_interrupt(self):
        cli = _make_cli()
        assert cli.busy_input_mode == "interrupt"

    def test_busy_input_mode_queue_is_honored(self):
        cli = _make_cli(config_overrides={"display": {"busy_input_mode": "queue"}})
        assert cli.busy_input_mode == "queue"

    def test_unknown_busy_input_mode_falls_back_to_interrupt(self):
        cli = _make_cli(config_overrides={"display": {"busy_input_mode": "bogus"}})
        assert cli.busy_input_mode == "interrupt"

    def test_queue_command_works_while_busy(self):
        """When agent is running, /queue should still put the prompt in _pending_input."""
        cli = _make_cli()
        cli._agent_running = True
        cli.process_command("/queue follow up")
        assert cli._pending_input.get_nowait() == "follow up"

    def test_queue_command_works_while_idle(self):
        """When agent is idle, /queue should still queue (not reject)."""
        cli = _make_cli()
        cli._agent_running = False
        cli.process_command("/queue follow up")
        assert cli._pending_input.get_nowait() == "follow up"

    def test_queue_mode_routes_busy_enter_to_pending(self):
        """In queue mode, Enter while busy should go to _pending_input, not _interrupt_queue."""
        cli = _make_cli(config_overrides={"display": {"busy_input_mode": "queue"}})
        cli._agent_running = True
        # Simulate what handle_enter does for non-command input while busy
        text = "follow up"
        if cli.busy_input_mode == "queue":
            cli._pending_input.put(text)
        else:
            cli._interrupt_queue.put(text)
        assert cli._pending_input.get_nowait() == "follow up"
        assert cli._interrupt_queue.empty()

    def test_interrupt_mode_routes_busy_enter_to_interrupt(self):
        """In interrupt mode (default), Enter while busy goes to _interrupt_queue."""
        cli = _make_cli()
        cli._agent_running = True
        text = "redirect"
        if cli.busy_input_mode == "queue":
            cli._pending_input.put(text)
        else:
            cli._interrupt_queue.put(text)
        assert cli._interrupt_queue.get_nowait() == "redirect"
        assert cli._pending_input.empty()


class TestSingleQueryState:
    def test_voice_and_interrupt_state_initialized_before_run(self):
        """Single-query mode calls chat() without going through run()."""
        cli = _make_cli()
        assert cli._voice_tts is False
        assert cli._voice_mode is False
        assert cli._voice_tts_done.is_set()
        assert hasattr(cli, "_interrupt_queue")
        assert hasattr(cli, "_pending_input")


class TestHistoryDisplay:
    def test_history_numbers_only_visible_messages_and_summarizes_tools(self, capsys):
        cli = _make_cli()
        cli.conversation_history = [
            {"role": "system", "content": "system prompt"},
            {"role": "user", "content": "Hello"},
            {
                "role": "assistant",
                "content": None,
                "tool_calls": [{"id": "call_1"}, {"id": "call_2"}],
            },
            {"role": "tool", "content": "tool output 1"},
            {"role": "tool", "content": "tool output 2"},
            {"role": "assistant", "content": "All set."},
            {"role": "user", "content": "A" * 250},
        ]

        cli.show_history()
        output = capsys.readouterr().out

        assert "[You #1]" in output
        assert "[Hermes #2]" in output
        assert "(requested 2 tool calls)" in output
        assert "[Tools]" in output
        assert "(2 tool messages hidden)" in output
        assert "[Hermes #3]" in output
        assert "[You #4]" in output
        assert "[You #5]" not in output
        assert "A" * 250 in output
        assert "A" * 250 + "..." not in output

    def test_history_shows_recent_sessions_when_current_chat_is_empty(self, capsys):
        cli = _make_cli()
        cli.session_id = "current"
        cli._session_db = MagicMock()
        cli._session_db.list_sessions_rich.return_value = [
            {
                "id": "current",
                "title": "Current",
                "preview": "Current preview",
                "last_active": 0,
            },
            {
                "id": "20260401_201329_d85961",
                "title": "Checking Running Hermes Agent",
                "preview": "check running gateways for hermes agent",
                "last_active": 0,
            },
        ]

        cli.show_history()
        output = capsys.readouterr().out

        assert "No messages in the current chat yet" in output
        assert "Checking Running Hermes Agent" in output
        assert "20260401_201329_d85961" in output
        assert "/resume" in output
        assert "Current preview" not in output

    def test_resume_without_target_lists_recent_sessions(self, capsys):
        cli = _make_cli()
        cli.session_id = "current"
        cli._session_db = MagicMock()
        cli._session_db.list_sessions_rich.return_value = [
            {
                "id": "current",
                "title": "Current",
                "preview": "Current preview",
                "last_active": 0,
            },
            {
                "id": "20260401_201329_d85961",
                "title": "Checking Running Hermes Agent",
                "preview": "check running gateways for hermes agent",
                "last_active": 0,
            },
        ]

        cli._handle_resume_command("/resume")
        output = capsys.readouterr().out

        assert "Recent sessions" in output
        assert "Checking Running Hermes Agent" in output
        assert "Use /resume <session id or title> to continue" in output


class TestRootLevelProviderOverride:
    """Root-level provider/base_url in config.yaml must NOT override model.provider."""

    def test_model_provider_wins_over_root_provider(self, tmp_path, monkeypatch):
        """model.provider takes priority — root-level provider is only a fallback."""
        import yaml

        hermes_home = tmp_path / ".hermes"
        hermes_home.mkdir()
        monkeypatch.setenv("HERMES_HOME", str(hermes_home))

        config_path = hermes_home / "config.yaml"
        config_path.write_text(yaml.safe_dump({
            "provider": "opencode-go",  # stale root-level key
            "model": {
                "default": "google/gemini-3-flash-preview",
                "provider": "openrouter",  # correct canonical key
            },
        }))

        import cli
        monkeypatch.setattr(cli, "_hermes_home", hermes_home)
        cfg = cli.load_cli_config()

        assert cfg["model"]["provider"] == "openrouter"

    def test_root_provider_ignored_when_default_model_provider_exists(self, tmp_path, monkeypatch):
        """Even when model.provider is the default 'auto', root-level provider is ignored."""
        import yaml

        hermes_home = tmp_path / ".hermes"
        hermes_home.mkdir()
        monkeypatch.setenv("HERMES_HOME", str(hermes_home))

        config_path = hermes_home / "config.yaml"
        config_path.write_text(yaml.safe_dump({
            "provider": "opencode-go",  # stale root key
            "model": {
                "default": "google/gemini-3-flash-preview",
                # no explicit model.provider — defaults provide "auto"
            },
        }))

        import cli
        monkeypatch.setattr(cli, "_hermes_home", hermes_home)
        cfg = cli.load_cli_config()

        # Root-level "opencode-go" must NOT leak through
        assert cfg["model"]["provider"] != "opencode-go"

    def test_normalize_root_model_keys_moves_to_model(self):
        """_normalize_root_model_keys migrates root keys into model section."""
        from hermes_cli.config import _normalize_root_model_keys

        config = {
            "provider": "opencode-go",
            "base_url": "https://example.com/v1",
            "model": {
                "default": "some-model",
            },
        }
        result = _normalize_root_model_keys(config)
        # Root keys removed
        assert "provider" not in result
        assert "base_url" not in result
        # Migrated into model section
        assert result["model"]["provider"] == "opencode-go"
        assert result["model"]["base_url"] == "https://example.com/v1"

    def test_normalize_root_model_keys_does_not_override_existing(self):
        """Existing model.provider is never overridden by root-level key."""
        from hermes_cli.config import _normalize_root_model_keys

        config = {
            "provider": "stale-provider",
            "model": {
                "default": "some-model",
                "provider": "correct-provider",
            },
        }
        result = _normalize_root_model_keys(config)
        assert result["model"]["provider"] == "correct-provider"
        assert "provider" not in result  # root key still cleaned up


class TestProviderResolution:
    def test_api_key_is_string_or_none(self):
        cli = _make_cli()
        assert cli.api_key is None or isinstance(cli.api_key, str)

    def test_base_url_is_string(self):
        cli = _make_cli()
        assert isinstance(cli.base_url, str)
        assert cli.base_url.startswith("http")

    def test_model_is_string(self):
        cli = _make_cli()
        assert isinstance(cli.model, str)
        assert isinstance(cli.model, str) and '/' in cli.model

```

## File: test_cli_interrupt_subagent.py
```
"""End-to-end test simulating CLI interrupt during subagent execution.

Reproduces the exact scenario:
1. Parent agent calls delegate_task
2. Child agent is running (simulated with a slow tool)
3. User "types a message" (simulated by calling parent.interrupt from another thread)
4. Child should detect the interrupt and stop

This tests the COMPLETE path including _run_single_child, _active_children
registration, interrupt propagation, and child detection.
"""

import json
import os
import queue
import threading
import time
import unittest
from unittest.mock import MagicMock, patch, PropertyMock

from tools.interrupt import set_interrupt, is_interrupted


class TestCLISubagentInterrupt(unittest.TestCase):
    """Simulate exact CLI scenario."""

    def setUp(self):
        set_interrupt(False)

    def tearDown(self):
        set_interrupt(False)

    def test_full_delegate_interrupt_flow(self):
        """Full integration: parent runs delegate_task, main thread interrupts."""
        from run_agent import AIAgent

        interrupt_detected = threading.Event()
        child_started = threading.Event()
        child_api_call_count = 0

        # Create a real-enough parent agent
        parent = AIAgent.__new__(AIAgent)
        parent._interrupt_requested = False
        parent._interrupt_message = None
        parent._active_children = []
        parent._active_children_lock = threading.Lock()
        parent.quiet_mode = True
        parent.model = "test/model"
        parent.base_url = "http://localhost:1"
        parent.api_key = "test"
        parent.provider = "test"
        parent.api_mode = "chat_completions"
        parent.platform = "cli"
        parent.enabled_toolsets = ["terminal", "file"]
        parent.providers_allowed = None
        parent.providers_ignored = None
        parent.providers_order = None
        parent.provider_sort = None
        parent.max_tokens = None
        parent.reasoning_config = None
        parent.prefill_messages = None
        parent._session_db = None
        parent._delegate_depth = 0
        parent._delegate_spinner = None
        parent.tool_progress_callback = None

        # We'll track what happens with _active_children
        original_children = parent._active_children

        # Mock the child's run_conversation to simulate a slow operation
        # that checks _interrupt_requested like the real one does
        def mock_child_run_conversation(user_message, **kwargs):
            child_started.set()
            # Find the child in parent._active_children
            child = parent._active_children[-1] if parent._active_children else None
            
            # Simulate the agent loop: poll _interrupt_requested like run_conversation does
            for i in range(100):  # Up to 10 seconds (100 * 0.1s)
                if child and child._interrupt_requested:
                    interrupt_detected.set()
                    return {
                        "final_response": "Interrupted!",
                        "messages": [],
                        "api_calls": 1,
                        "completed": False,
                        "interrupted": True,
                        "interrupt_message": child._interrupt_message,
                    }
                time.sleep(0.1)
            
            return {
                "final_response": "Finished without interrupt",
                "messages": [],
                "api_calls": 5,
                "completed": True,
                "interrupted": False,
            }

        # Patch AIAgent to use our mock
        from tools.delegate_tool import _run_single_child
        from run_agent import IterationBudget

        parent.iteration_budget = IterationBudget(max_total=100)

        # Run delegate in a thread (simulates agent_thread)
        delegate_result = [None]
        delegate_error = [None]

        def run_delegate():
            try:
                with patch('run_agent.AIAgent') as MockAgent:
                    mock_instance = MagicMock()
                    mock_instance._interrupt_requested = False
                    mock_instance._interrupt_message = None
                    mock_instance._active_children = []
                    mock_instance._active_children_lock = threading.Lock()
                    mock_instance.quiet_mode = True
                    mock_instance.run_conversation = mock_child_run_conversation
                    mock_instance.interrupt = lambda msg=None: setattr(mock_instance, '_interrupt_requested', True) or setattr(mock_instance, '_interrupt_message', msg)
                    mock_instance.tools = []
                    MockAgent.return_value = mock_instance

                    # Register child manually (normally done by _build_child_agent)
                    parent._active_children.append(mock_instance)

                    result = _run_single_child(
                        task_index=0,
                        goal="Do something slow",
                        child=mock_instance,
                        parent_agent=parent,
                    )
                    delegate_result[0] = result
            except Exception as e:
                delegate_error[0] = e

        agent_thread = threading.Thread(target=run_delegate, daemon=True)
        agent_thread.start()

        # Wait for child to start
        assert child_started.wait(timeout=5), "Child never started!"

        # Now simulate user interrupt (from main/process thread)
        time.sleep(0.2)  # Give child a moment to be in its loop
        
        print(f"Parent has {len(parent._active_children)} active children")
        assert len(parent._active_children) >= 1, f"Expected child in _active_children, got {len(parent._active_children)}"

        # This is what the CLI does:
        parent.interrupt("Hey stop that")
        
        print(f"Parent._interrupt_requested: {parent._interrupt_requested}")
        for i, child in enumerate(parent._active_children):
            print(f"Child {i}._interrupt_requested: {child._interrupt_requested}")

        # Wait for child to detect interrupt
        detected = interrupt_detected.wait(timeout=3.0)
        
        # Wait for delegate to finish
        agent_thread.join(timeout=5)

        if delegate_error[0]:
            raise delegate_error[0]

        assert detected, "Child never detected the interrupt!"
        result = delegate_result[0]
        assert result is not None, "Delegate returned no result"
        assert result["status"] == "interrupted", f"Expected 'interrupted', got '{result['status']}'"
        print(f"✓ Interrupt detected! Result: {result}")


if __name__ == "__main__":
    unittest.main()

```

## File: test_cli_loading_indicator.py
```
"""Regression tests for loading feedback on slow slash commands."""

from unittest.mock import patch

from cli import HermesCLI


class TestCLILoadingIndicator:
    def _make_cli(self):
        cli_obj = HermesCLI.__new__(HermesCLI)
        cli_obj._app = None
        cli_obj._last_invalidate = 0.0
        cli_obj._command_running = False
        cli_obj._command_status = ""
        return cli_obj

    def test_skills_command_sets_busy_state_and_prints_status(self, capsys):
        cli_obj = self._make_cli()
        seen = {}

        def fake_handle(cmd: str):
            seen["cmd"] = cmd
            seen["running"] = cli_obj._command_running
            seen["status"] = cli_obj._command_status
            print("skills done")

        with patch.object(cli_obj, "_handle_skills_command", side_effect=fake_handle), \
             patch.object(cli_obj, "_invalidate") as invalidate_mock:
            assert cli_obj.process_command("/skills search kubernetes")

        output = capsys.readouterr().out
        assert "⏳ Searching skills..." in output
        assert "skills done" in output
        assert seen == {
            "cmd": "/skills search kubernetes",
            "running": True,
            "status": "Searching skills...",
        }
        assert cli_obj._command_running is False
        assert cli_obj._command_status == ""
        assert invalidate_mock.call_count == 2

    def test_reload_mcp_sets_busy_state_and_prints_status(self, capsys):
        cli_obj = self._make_cli()
        seen = {}

        def fake_reload():
            seen["running"] = cli_obj._command_running
            seen["status"] = cli_obj._command_status
            print("reload done")

        with patch.object(cli_obj, "_reload_mcp", side_effect=fake_reload), \
             patch.object(cli_obj, "_invalidate") as invalidate_mock:
            assert cli_obj.process_command("/reload-mcp")

        output = capsys.readouterr().out
        assert "⏳ Reloading MCP servers..." in output
        assert "reload done" in output
        assert seen == {
            "running": True,
            "status": "Reloading MCP servers...",
        }
        assert cli_obj._command_running is False
        assert cli_obj._command_status == ""
        assert invalidate_mock.call_count == 2

```

## File: test_cli_mcp_config_watch.py
```
"""Tests for automatic MCP reload when config.yaml mcp_servers section changes."""
import time
from pathlib import Path
from unittest.mock import MagicMock, patch


def _make_cli(tmp_path, mcp_servers=None):
    """Create a minimal HermesCLI instance with mocked config."""
    import cli as cli_mod
    obj = object.__new__(cli_mod.HermesCLI)
    obj.config = {"mcp_servers": mcp_servers or {}}
    obj._agent_running = False
    obj._last_config_check = 0.0
    obj._config_mcp_servers = mcp_servers or {}

    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text("mcp_servers: {}\n")
    obj._config_mtime = cfg_file.stat().st_mtime

    obj._reload_mcp = MagicMock()
    obj._busy_command = MagicMock()
    obj._busy_command.return_value.__enter__ = MagicMock(return_value=None)
    obj._busy_command.return_value.__exit__ = MagicMock(return_value=False)
    obj._slow_command_status = MagicMock(return_value="reloading...")

    return obj, cfg_file


class TestMCPConfigWatch:

    def test_no_change_does_not_reload(self, tmp_path):
        """If mtime and mcp_servers unchanged, _reload_mcp is NOT called."""
        obj, cfg_file = _make_cli(tmp_path)

        with patch("hermes_cli.config.get_config_path", return_value=cfg_file):
            obj._check_config_mcp_changes()

        obj._reload_mcp.assert_not_called()

    def test_mtime_change_with_same_mcp_servers_does_not_reload(self, tmp_path):
        """If file mtime changes but mcp_servers is identical, no reload."""
        import yaml
        obj, cfg_file = _make_cli(tmp_path, mcp_servers={"fs": {"command": "npx"}})

        # Write same mcp_servers but touch the file
        cfg_file.write_text(yaml.dump({"mcp_servers": {"fs": {"command": "npx"}}}))
        # Force mtime to appear changed
        obj._config_mtime = 0.0

        with patch("hermes_cli.config.get_config_path", return_value=cfg_file):
            obj._check_config_mcp_changes()

        obj._reload_mcp.assert_not_called()

    def test_new_mcp_server_triggers_reload(self, tmp_path):
        """Adding a new MCP server to config triggers auto-reload."""
        import yaml
        obj, cfg_file = _make_cli(tmp_path, mcp_servers={})

        # Simulate user adding a new MCP server to config.yaml
        cfg_file.write_text(yaml.dump({"mcp_servers": {"github": {"url": "https://mcp.github.com"}}}))
        obj._config_mtime = 0.0  # force stale mtime

        with patch("hermes_cli.config.get_config_path", return_value=cfg_file):
            obj._check_config_mcp_changes()

        obj._reload_mcp.assert_called_once()

    def test_removed_mcp_server_triggers_reload(self, tmp_path):
        """Removing an MCP server from config triggers auto-reload."""
        import yaml
        obj, cfg_file = _make_cli(tmp_path, mcp_servers={"github": {"url": "https://mcp.github.com"}})

        # Simulate user removing the server
        cfg_file.write_text(yaml.dump({"mcp_servers": {}}))
        obj._config_mtime = 0.0

        with patch("hermes_cli.config.get_config_path", return_value=cfg_file):
            obj._check_config_mcp_changes()

        obj._reload_mcp.assert_called_once()

    def test_interval_throttle_skips_check(self, tmp_path):
        """If called within CONFIG_WATCH_INTERVAL, stat() is skipped."""
        obj, cfg_file = _make_cli(tmp_path)
        obj._last_config_check = time.monotonic()  # just checked

        with patch("hermes_cli.config.get_config_path", return_value=cfg_file), \
             patch.object(Path, "stat") as mock_stat:
            obj._check_config_mcp_changes()
            mock_stat.assert_not_called()

        obj._reload_mcp.assert_not_called()

    def test_missing_config_file_does_not_crash(self, tmp_path):
        """If config.yaml doesn't exist, _check_config_mcp_changes is a no-op."""
        obj, cfg_file = _make_cli(tmp_path)
        missing = tmp_path / "nonexistent.yaml"

        with patch("hermes_cli.config.get_config_path", return_value=missing):
            obj._check_config_mcp_changes()  # should not raise

        obj._reload_mcp.assert_not_called()

```

## File: test_cli_new_session.py
```
"""Regression tests for CLI fresh-session commands."""

from __future__ import annotations

import importlib
import os
import sys
from datetime import timedelta
from unittest.mock import MagicMock, patch

from hermes_state import SessionDB
from tools.todo_tool import TodoStore


class _FakeCompressor:
    """Minimal stand-in for ContextCompressor."""

    def __init__(self):
        self.last_prompt_tokens = 500
        self.last_completion_tokens = 200
        self.last_total_tokens = 700
        self.compression_count = 3
        self._context_probed = True


class _FakeAgent:
    def __init__(self, session_id: str, session_start):
        self.session_id = session_id
        self.session_start = session_start
        self.model = "anthropic/claude-opus-4.6"
        self._last_flushed_db_idx = 7
        self._todo_store = TodoStore()
        self._todo_store.write(
            [{"id": "t1", "content": "unfinished task", "status": "in_progress"}]
        )
        self.flush_memories = MagicMock()
        self._invalidate_system_prompt = MagicMock()

        # Token counters (non-zero to verify reset)
        self.session_total_tokens = 1000
        self.session_input_tokens = 600
        self.session_output_tokens = 400
        self.session_prompt_tokens = 550
        self.session_completion_tokens = 350
        self.session_cache_read_tokens = 100
        self.session_cache_write_tokens = 50
        self.session_reasoning_tokens = 80
        self.session_api_calls = 5
        self.session_estimated_cost_usd = 0.42
        self.session_cost_status = "estimated"
        self.session_cost_source = "openrouter"
        self.context_compressor = _FakeCompressor()

    def reset_session_state(self):
        """Mirror the real AIAgent.reset_session_state()."""
        self.session_total_tokens = 0
        self.session_input_tokens = 0
        self.session_output_tokens = 0
        self.session_prompt_tokens = 0
        self.session_completion_tokens = 0
        self.session_cache_read_tokens = 0
        self.session_cache_write_tokens = 0
        self.session_reasoning_tokens = 0
        self.session_api_calls = 0
        self.session_estimated_cost_usd = 0.0
        self.session_cost_status = "unknown"
        self.session_cost_source = "none"
        if hasattr(self, "context_compressor") and self.context_compressor:
            self.context_compressor.last_prompt_tokens = 0
            self.context_compressor.last_completion_tokens = 0
            self.context_compressor.last_total_tokens = 0
            self.context_compressor.compression_count = 0
            self.context_compressor._context_probed = False


def _make_cli(env_overrides=None, config_overrides=None, **kwargs):
    """Create a HermesCLI instance with minimal mocking."""
    _clean_config = {
        "model": {
            "default": "anthropic/claude-opus-4.6",
            "base_url": "https://openrouter.ai/api/v1",
            "provider": "auto",
        },
        "display": {"compact": False, "tool_progress": "all"},
        "agent": {},
        "terminal": {"env_type": "local"},
    }
    if config_overrides:
        _clean_config.update(config_overrides)
    clean_env = {"LLM_MODEL": "", "HERMES_MAX_ITERATIONS": ""}
    if env_overrides:
        clean_env.update(env_overrides)
    prompt_toolkit_stubs = {
        "prompt_toolkit": MagicMock(),
        "prompt_toolkit.history": MagicMock(),
        "prompt_toolkit.styles": MagicMock(),
        "prompt_toolkit.patch_stdout": MagicMock(),
        "prompt_toolkit.application": MagicMock(),
        "prompt_toolkit.layout": MagicMock(),
        "prompt_toolkit.layout.processors": MagicMock(),
        "prompt_toolkit.filters": MagicMock(),
        "prompt_toolkit.layout.dimension": MagicMock(),
        "prompt_toolkit.layout.menus": MagicMock(),
        "prompt_toolkit.widgets": MagicMock(),
        "prompt_toolkit.key_binding": MagicMock(),
        "prompt_toolkit.completion": MagicMock(),
        "prompt_toolkit.formatted_text": MagicMock(),
        "prompt_toolkit.auto_suggest": MagicMock(),
    }
    with patch.dict(sys.modules, prompt_toolkit_stubs), patch.dict(
        "os.environ", clean_env, clear=False
    ):
        import cli as _cli_mod

        _cli_mod = importlib.reload(_cli_mod)
        with patch.object(_cli_mod, "get_tool_definitions", return_value=[]), patch.dict(
            _cli_mod.__dict__, {"CLI_CONFIG": _clean_config}
        ):
            return _cli_mod.HermesCLI(**kwargs)


def _prepare_cli_with_active_session(tmp_path):
    cli = _make_cli()
    cli._session_db = SessionDB(db_path=tmp_path / "state.db")
    cli._session_db.create_session(session_id=cli.session_id, source="cli", model=cli.model)

    cli.agent = _FakeAgent(cli.session_id, cli.session_start)
    cli.conversation_history = [{"role": "user", "content": "hello"}]

    old_session_start = cli.session_start - timedelta(seconds=1)
    cli.session_start = old_session_start
    cli.agent.session_start = old_session_start
    return cli


def test_new_command_creates_real_fresh_session_and_resets_agent_state(tmp_path):
    cli = _prepare_cli_with_active_session(tmp_path)
    old_session_id = cli.session_id
    old_session_start = cli.session_start

    cli.process_command("/new")

    assert cli.session_id != old_session_id

    old_session = cli._session_db.get_session(old_session_id)
    assert old_session is not None
    assert old_session["end_reason"] == "new_session"

    new_session = cli._session_db.get_session(cli.session_id)
    assert new_session is not None

    cli._session_db.append_message(cli.session_id, role="user", content="next turn")

    assert cli.agent.session_id == cli.session_id
    assert cli.agent._last_flushed_db_idx == 0
    assert cli.agent._todo_store.read() == []
    assert cli.session_start > old_session_start
    assert cli.agent.session_start == cli.session_start
    cli.agent.flush_memories.assert_called_once_with([{"role": "user", "content": "hello"}])
    cli.agent._invalidate_system_prompt.assert_called_once()


def test_reset_command_is_alias_for_new_session(tmp_path):
    cli = _prepare_cli_with_active_session(tmp_path)
    old_session_id = cli.session_id

    cli.process_command("/reset")

    assert cli.session_id != old_session_id
    assert cli._session_db.get_session(old_session_id)["end_reason"] == "new_session"
    assert cli._session_db.get_session(cli.session_id) is not None


def test_clear_command_starts_new_session_before_redrawing(tmp_path):
    cli = _prepare_cli_with_active_session(tmp_path)
    cli.console = MagicMock()
    cli.show_banner = MagicMock()

    old_session_id = cli.session_id
    cli.process_command("/clear")

    assert cli.session_id != old_session_id
    assert cli._session_db.get_session(old_session_id)["end_reason"] == "new_session"
    assert cli._session_db.get_session(cli.session_id) is not None
    cli.console.clear.assert_called_once()
    cli.show_banner.assert_called_once()
    assert cli.conversation_history == []


def test_new_session_resets_token_counters(tmp_path):
    """Regression test for #2099: /new must zero all token counters."""
    cli = _prepare_cli_with_active_session(tmp_path)

    # Verify counters are non-zero before reset
    agent = cli.agent
    assert agent.session_total_tokens > 0
    assert agent.session_api_calls > 0
    assert agent.context_compressor.compression_count > 0

    cli.process_command("/new")

    # All agent token counters must be zero
    assert agent.session_total_tokens == 0
    assert agent.session_input_tokens == 0
    assert agent.session_output_tokens == 0
    assert agent.session_prompt_tokens == 0
    assert agent.session_completion_tokens == 0
    assert agent.session_cache_read_tokens == 0
    assert agent.session_cache_write_tokens == 0
    assert agent.session_reasoning_tokens == 0
    assert agent.session_api_calls == 0
    assert agent.session_estimated_cost_usd == 0.0
    assert agent.session_cost_status == "unknown"
    assert agent.session_cost_source == "none"

    # Context compressor counters must also be zero
    comp = agent.context_compressor
    assert comp.last_prompt_tokens == 0
    assert comp.last_completion_tokens == 0
    assert comp.last_total_tokens == 0
    assert comp.compression_count == 0
    assert comp._context_probed is False

```

## File: test_cli_plan_command.py
```
"""Tests for the /plan CLI slash command."""

from unittest.mock import MagicMock, patch

from agent.skill_commands import scan_skill_commands
from cli import HermesCLI


def _make_cli():
    cli_obj = HermesCLI.__new__(HermesCLI)
    cli_obj.config = {}
    cli_obj.console = MagicMock()
    cli_obj.agent = None
    cli_obj.conversation_history = []
    cli_obj.session_id = "sess-123"
    cli_obj._pending_input = MagicMock()
    return cli_obj


def _make_plan_skill(skills_dir):
    skill_dir = skills_dir / "plan"
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(
        """---
name: plan
description: Plan mode skill.
---

# Plan

Use the current conversation context when no explicit instruction is provided.
Save plans under the active workspace's .hermes/plans directory.
"""
    )


class TestCLIPlanCommand:
    def test_plan_command_queues_plan_skill_message(self, tmp_path, monkeypatch):
        cli_obj = _make_cli()

        with patch("tools.skills_tool.SKILLS_DIR", tmp_path):
            _make_plan_skill(tmp_path)
            scan_skill_commands()
            result = cli_obj.process_command("/plan Add OAuth login")

        assert result is True
        cli_obj._pending_input.put.assert_called_once()
        queued = cli_obj._pending_input.put.call_args[0][0]
        assert "Plan mode skill" in queued
        assert "Add OAuth login" in queued
        assert ".hermes/plans" in queued
        assert str(tmp_path / "plans") not in queued
        assert "active workspace/backend cwd" in queued
        assert "Runtime note:" in queued

    def test_plan_without_args_uses_skill_context_guidance(self, tmp_path, monkeypatch):
        cli_obj = _make_cli()

        with patch("tools.skills_tool.SKILLS_DIR", tmp_path):
            _make_plan_skill(tmp_path)
            scan_skill_commands()
            cli_obj.process_command("/plan")

        queued = cli_obj._pending_input.put.call_args[0][0]
        assert "current conversation context" in queued
        assert ".hermes/plans/" in queued
        assert "conversation-plan.md" in queued

```

## File: test_cli_prefix_matching.py
```
"""Tests for slash command prefix matching in HermesCLI.process_command."""
from unittest.mock import MagicMock, patch
from cli import HermesCLI


def _make_cli():
    cli_obj = HermesCLI.__new__(HermesCLI)
    cli_obj.config = {}
    cli_obj.console = MagicMock()
    cli_obj.agent = None
    cli_obj.conversation_history = []
    cli_obj.session_id = None
    cli_obj._pending_input = MagicMock()
    return cli_obj


class TestSlashCommandPrefixMatching:
    def test_unique_prefix_dispatches_command(self):
        """/con should dispatch to /config when it uniquely matches."""
        cli_obj = _make_cli()
        with patch.object(cli_obj, 'show_config') as mock_config:
            cli_obj.process_command("/con")
        mock_config.assert_called_once()

    def test_unique_prefix_with_args_does_not_recurse(self):
        """/con set key value should expand to /config set key value without infinite recursion."""
        cli_obj = _make_cli()
        dispatched = []

        original = cli_obj.process_command.__func__

        def counting_process_command(self_inner, cmd):
            dispatched.append(cmd)
            if len(dispatched) > 5:
                raise RecursionError("process_command called too many times")
            return original(self_inner, cmd)

        # Mock show_config since the test is about recursion, not config display
        with patch.object(type(cli_obj), 'process_command', counting_process_command), \
             patch.object(cli_obj, 'show_config'):
            try:
                cli_obj.process_command("/con set key value")
            except RecursionError:
                assert False, "process_command recursed infinitely"

        # Should have been called at most twice: once for /con set..., once for /config set...
        assert len(dispatched) <= 2

    def test_exact_command_with_args_does_not_recurse(self):
        """/config set key value hits exact branch and does not loop back to prefix."""
        cli_obj = _make_cli()
        call_count = [0]

        original_pc = HermesCLI.process_command

        def guarded(self_inner, cmd):
            call_count[0] += 1
            if call_count[0] > 10:
                raise RecursionError("Infinite recursion detected")
            return original_pc(self_inner, cmd)

        # Mock show_config since the test is about recursion, not config display
        with patch.object(HermesCLI, 'process_command', guarded), \
             patch.object(cli_obj, 'show_config'):
            try:
                cli_obj.process_command("/config set key value")
            except RecursionError:
                assert False, "Recursed infinitely on /config set key value"

        assert call_count[0] <= 3

    def test_ambiguous_prefix_shows_suggestions(self):
        """/re matches multiple commands — should show ambiguous message."""
        cli_obj = _make_cli()
        with patch("cli._cprint") as mock_cprint:
            cli_obj.process_command("/re")
            printed = " ".join(str(c) for c in mock_cprint.call_args_list)
        assert "Ambiguous" in printed or "Did you mean" in printed

    def test_unknown_command_shows_error(self):
        """/xyz should show unknown command error."""
        cli_obj = _make_cli()
        with patch("cli._cprint") as mock_cprint:
            cli_obj.process_command("/xyz")
            printed = " ".join(str(c) for c in mock_cprint.call_args_list)
        assert "Unknown command" in printed

    def test_exact_command_still_works(self):
        """/help should still work as exact match."""
        cli_obj = _make_cli()
        with patch.object(cli_obj, 'show_help') as mock_help:
            cli_obj.process_command("/help")
        mock_help.assert_called_once()

    def test_skill_command_prefix_matches(self):
        """A prefix that uniquely matches a skill command should dispatch it."""
        cli_obj = _make_cli()
        fake_skill = {"/test-skill-xyz": {"name": "Test Skill", "description": "test"}}
        printed = []
        cli_obj.console.print = lambda *a, **kw: printed.append(str(a))

        import cli as cli_mod
        with patch.object(cli_mod, '_skill_commands', fake_skill):
            cli_obj.process_command("/test-skill-xy")

        # Should NOT show "Unknown command" — should have dispatched or attempted skill
        unknown = any("Unknown command" in p for p in printed)
        assert not unknown, f"Expected skill prefix to match, got: {printed}"

    def test_ambiguous_between_builtin_and_skill(self):
        """Ambiguous prefix spanning builtin + skill commands shows suggestions."""
        cli_obj = _make_cli()
        # /help-extra is a fake skill that shares /hel prefix with /help
        fake_skill = {"/help-extra": {"name": "Help Extra", "description": "test"}}

        import cli as cli_mod
        with patch.object(cli_mod, '_skill_commands', fake_skill),              patch.object(cli_obj, 'show_help') as mock_help:
            cli_obj.process_command("/help")

        # /help is an exact match so should work normally, not show ambiguous
        mock_help.assert_called_once()
        printed = " ".join(str(c) for c in cli_obj.console.print.call_args_list)
        assert "Ambiguous" not in printed

    def test_shortest_match_preferred_over_longer_skill(self):
        """/qui should dispatch to /quit (5 chars) not report ambiguous with /quint-pipeline (15 chars)."""
        cli_obj = _make_cli()
        fake_skill = {"/quint-pipeline": {"name": "Quint Pipeline", "description": "test"}}

        import cli as cli_mod
        with patch.object(cli_mod, '_skill_commands', fake_skill):
            # /quit is caught by the exact "/quit" branch → process_command returns False
            result = cli_obj.process_command("/qui")

        # Returns False because /quit was dispatched (exits chat loop)
        assert result is False
        printed = " ".join(str(c) for c in cli_obj.console.print.call_args_list)
        assert "Ambiguous" not in printed

    def test_tied_shortest_matches_still_ambiguous(self):
        """/re matches /reset and /retry (both 6 chars) — no unique shortest, stays ambiguous."""
        cli_obj = _make_cli()
        printed = []
        import cli as cli_mod
        with patch.object(cli_mod, '_cprint', side_effect=lambda t: printed.append(t)):
            cli_obj.process_command("/re")
        combined = " ".join(printed)
        assert "Ambiguous" in combined or "Did you mean" in combined

    def test_exact_typed_name_dispatches_over_longer_match(self):
        """/help typed with /help-extra skill installed → exact match wins."""
        cli_obj = _make_cli()
        fake_skill = {"/help-extra": {"name": "Help Extra", "description": ""}}
        import cli as cli_mod
        with patch.object(cli_mod, '_skill_commands', fake_skill), \
             patch.object(cli_obj, 'show_help') as mock_help:
            cli_obj.process_command("/help")
        mock_help.assert_called_once()
        printed = " ".join(str(c) for c in cli_obj.console.print.call_args_list)
        assert "Ambiguous" not in printed

```

## File: test_cli_preloaded_skills.py
```
from __future__ import annotations

import importlib
import os
import sys
from unittest.mock import MagicMock, patch

import pytest


def _make_real_cli(**kwargs):
    clean_config = {
        "model": {
            "default": "anthropic/claude-opus-4.6",
            "base_url": "https://openrouter.ai/api/v1",
            "provider": "auto",
        },
        "display": {"compact": False, "tool_progress": "all"},
        "agent": {},
        "terminal": {"env_type": "local"},
    }
    clean_env = {"LLM_MODEL": "", "HERMES_MAX_ITERATIONS": ""}
    prompt_toolkit_stubs = {
        "prompt_toolkit": MagicMock(),
        "prompt_toolkit.history": MagicMock(),
        "prompt_toolkit.styles": MagicMock(),
        "prompt_toolkit.patch_stdout": MagicMock(),
        "prompt_toolkit.application": MagicMock(),
        "prompt_toolkit.layout": MagicMock(),
        "prompt_toolkit.layout.processors": MagicMock(),
        "prompt_toolkit.filters": MagicMock(),
        "prompt_toolkit.layout.dimension": MagicMock(),
        "prompt_toolkit.layout.menus": MagicMock(),
        "prompt_toolkit.widgets": MagicMock(),
        "prompt_toolkit.key_binding": MagicMock(),
        "prompt_toolkit.completion": MagicMock(),
        "prompt_toolkit.formatted_text": MagicMock(),
    }
    with patch.dict(sys.modules, prompt_toolkit_stubs), patch.dict(
        "os.environ", clean_env, clear=False
    ):
        import cli as cli_mod

        cli_mod = importlib.reload(cli_mod)
        with patch.object(cli_mod, "get_tool_definitions", return_value=[]), patch.dict(
            cli_mod.__dict__, {"CLI_CONFIG": clean_config}
        ):
            return cli_mod.HermesCLI(**kwargs)


class _DummyCLI:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.session_id = "session-123"
        self.system_prompt = "base prompt"
        self.preloaded_skills = []

    def show_banner(self):
        return None

    def show_tools(self):
        return None

    def show_toolsets(self):
        return None

    def run(self):
        return None


def test_main_applies_preloaded_skills_to_system_prompt(monkeypatch):
    import cli as cli_mod

    created = {}

    def fake_cli(**kwargs):
        created["cli"] = _DummyCLI(**kwargs)
        return created["cli"]

    monkeypatch.setattr(cli_mod, "HermesCLI", fake_cli)
    monkeypatch.setattr(
        cli_mod,
        "build_preloaded_skills_prompt",
        lambda skills, task_id=None: ("skill prompt", ["hermes-agent-dev", "github-auth"], []),
    )

    with pytest.raises(SystemExit):
        cli_mod.main(skills="hermes-agent-dev,github-auth", list_tools=True)

    cli_obj = created["cli"]
    assert cli_obj.system_prompt == "base prompt\n\nskill prompt"
    assert cli_obj.preloaded_skills == ["hermes-agent-dev", "github-auth"]


def test_main_raises_for_unknown_preloaded_skill(monkeypatch):
    import cli as cli_mod

    monkeypatch.setattr(cli_mod, "HermesCLI", lambda **kwargs: _DummyCLI(**kwargs))
    monkeypatch.setattr(
        cli_mod,
        "build_preloaded_skills_prompt",
        lambda skills, task_id=None: ("", [], ["missing-skill"]),
    )

    with pytest.raises(ValueError, match=r"Unknown skill\(s\): missing-skill"):
        cli_mod.main(skills="missing-skill", list_tools=True)


def test_show_banner_does_not_print_skills():
    """show_banner() no longer prints the activated skills line — it moved to run()."""
    cli_obj = _make_real_cli(compact=False)
    cli_obj.preloaded_skills = ["hermes-agent-dev", "github-auth"]
    cli_obj.console = MagicMock()

    with patch("cli.build_welcome_banner") as mock_banner, patch(
        "shutil.get_terminal_size", return_value=os.terminal_size((120, 40))
    ):
        cli_obj.show_banner()

    print_calls = [
        call.args[0]
        for call in cli_obj.console.print.call_args_list
        if call.args and isinstance(call.args[0], str)
    ]
    startup_lines = [line for line in print_calls if "Activated skills:" in line]
    assert len(startup_lines) == 0
    assert mock_banner.call_count == 1

```

## File: test_cli_provider_resolution.py
```
import importlib
import sys
import types
from contextlib import nullcontext
from types import SimpleNamespace

import pytest

from hermes_cli.auth import AuthError
from hermes_cli import main as hermes_main


# ---------------------------------------------------------------------------
# Module isolation: _import_cli() wipes tools.* / cli / run_agent from
# sys.modules so it can re-import cli fresh.  Without cleanup the wiped
# modules leak into subsequent tests on the same xdist worker, breaking
# mock patches that target "tools.file_tools._get_file_ops" etc.
# ---------------------------------------------------------------------------

def _reset_modules(prefixes: tuple[str, ...]):
    for name in list(sys.modules):
        if any(name == p or name.startswith(p + ".") for p in prefixes):
            sys.modules.pop(name, None)


@pytest.fixture(autouse=True)
def _restore_cli_and_tool_modules():
    """Save and restore tools/cli/run_agent modules around every test."""
    prefixes = ("tools", "cli", "run_agent")
    original_modules = {
        name: module
        for name, module in sys.modules.items()
        if any(name == p or name.startswith(p + ".") for p in prefixes)
    }
    try:
        yield
    finally:
        _reset_modules(prefixes)
        sys.modules.update(original_modules)


def _install_prompt_toolkit_stubs():
    class _Dummy:
        def __init__(self, *args, **kwargs):
            pass

    class _Condition:
        def __init__(self, func):
            self.func = func

        def __bool__(self):
            return bool(self.func())

    class _ANSI(str):
        pass

    root = types.ModuleType("prompt_toolkit")
    history = types.ModuleType("prompt_toolkit.history")
    styles = types.ModuleType("prompt_toolkit.styles")
    patch_stdout = types.ModuleType("prompt_toolkit.patch_stdout")
    application = types.ModuleType("prompt_toolkit.application")
    layout = types.ModuleType("prompt_toolkit.layout")
    processors = types.ModuleType("prompt_toolkit.layout.processors")
    filters = types.ModuleType("prompt_toolkit.filters")
    dimension = types.ModuleType("prompt_toolkit.layout.dimension")
    menus = types.ModuleType("prompt_toolkit.layout.menus")
    widgets = types.ModuleType("prompt_toolkit.widgets")
    key_binding = types.ModuleType("prompt_toolkit.key_binding")
    completion = types.ModuleType("prompt_toolkit.completion")
    formatted_text = types.ModuleType("prompt_toolkit.formatted_text")

    history.FileHistory = _Dummy
    styles.Style = _Dummy
    patch_stdout.patch_stdout = lambda *args, **kwargs: nullcontext()
    application.Application = _Dummy
    layout.Layout = _Dummy
    layout.HSplit = _Dummy
    layout.Window = _Dummy
    layout.FormattedTextControl = _Dummy
    layout.ConditionalContainer = _Dummy
    processors.Processor = _Dummy
    processors.Transformation = _Dummy
    processors.PasswordProcessor = _Dummy
    processors.ConditionalProcessor = _Dummy
    filters.Condition = _Condition
    dimension.Dimension = _Dummy
    menus.CompletionsMenu = _Dummy
    widgets.TextArea = _Dummy
    key_binding.KeyBindings = _Dummy
    completion.Completer = _Dummy
    completion.Completion = _Dummy
    formatted_text.ANSI = _ANSI
    root.print_formatted_text = lambda *args, **kwargs: None

    sys.modules.setdefault("prompt_toolkit", root)
    sys.modules.setdefault("prompt_toolkit.history", history)
    sys.modules.setdefault("prompt_toolkit.styles", styles)
    sys.modules.setdefault("prompt_toolkit.patch_stdout", patch_stdout)
    sys.modules.setdefault("prompt_toolkit.application", application)
    sys.modules.setdefault("prompt_toolkit.layout", layout)
    sys.modules.setdefault("prompt_toolkit.layout.processors", processors)
    sys.modules.setdefault("prompt_toolkit.filters", filters)
    sys.modules.setdefault("prompt_toolkit.layout.dimension", dimension)
    sys.modules.setdefault("prompt_toolkit.layout.menus", menus)
    sys.modules.setdefault("prompt_toolkit.widgets", widgets)
    sys.modules.setdefault("prompt_toolkit.key_binding", key_binding)
    sys.modules.setdefault("prompt_toolkit.completion", completion)
    sys.modules.setdefault("prompt_toolkit.formatted_text", formatted_text)


def _import_cli():
    for name in list(sys.modules):
        if name == "cli" or name == "run_agent" or name == "tools" or name.startswith("tools."):
            sys.modules.pop(name, None)

    if "firecrawl" not in sys.modules:
        sys.modules["firecrawl"] = types.SimpleNamespace(Firecrawl=object)

    try:
        importlib.import_module("prompt_toolkit")
    except ModuleNotFoundError:
        _install_prompt_toolkit_stubs()
    return importlib.import_module("cli")


def test_hermes_cli_init_does_not_eagerly_resolve_runtime_provider(monkeypatch):
    cli = _import_cli()
    calls = {"count": 0}

    def _unexpected_runtime_resolve(**kwargs):
        calls["count"] += 1
        raise AssertionError("resolve_runtime_provider should not be called in HermesCLI.__init__")

    monkeypatch.setattr("hermes_cli.runtime_provider.resolve_runtime_provider", _unexpected_runtime_resolve)
    monkeypatch.setattr("hermes_cli.runtime_provider.format_runtime_provider_error", lambda exc: str(exc))

    shell = cli.HermesCLI(model="gpt-5", compact=True, max_turns=1)

    assert shell is not None
    assert calls["count"] == 0


def test_runtime_resolution_failure_is_not_sticky(monkeypatch):
    cli = _import_cli()
    calls = {"count": 0}

    def _runtime_resolve(**kwargs):
        calls["count"] += 1
        if calls["count"] == 1:
            raise RuntimeError("temporary auth failure")
        return {
            "provider": "openrouter",
            "api_mode": "chat_completions",
            "base_url": "https://openrouter.ai/api/v1",
            "api_key": "test-key",
            "source": "env/config",
        }

    class _DummyAgent:
        def __init__(self, *args, **kwargs):
            self.kwargs = kwargs

    monkeypatch.setattr("hermes_cli.runtime_provider.resolve_runtime_provider", _runtime_resolve)
    monkeypatch.setattr("hermes_cli.runtime_provider.format_runtime_provider_error", lambda exc: str(exc))
    monkeypatch.setattr(cli, "AIAgent", _DummyAgent)

    shell = cli.HermesCLI(model="gpt-5", compact=True, max_turns=1)

    assert shell._init_agent() is False
    assert shell._init_agent() is True
    assert calls["count"] == 2
    assert shell.agent is not None


def test_runtime_resolution_rebuilds_agent_on_routing_change(monkeypatch):
    cli = _import_cli()

    def _runtime_resolve(**kwargs):
        return {
            "provider": "openai-codex",
            "api_mode": "codex_responses",
            "base_url": "https://same-endpoint.example/v1",
            "api_key": "same-key",
            "source": "env/config",
        }

    monkeypatch.setattr("hermes_cli.runtime_provider.resolve_runtime_provider", _runtime_resolve)
    monkeypatch.setattr("hermes_cli.runtime_provider.format_runtime_provider_error", lambda exc: str(exc))

    shell = cli.HermesCLI(model="gpt-5", compact=True, max_turns=1)
    shell.provider = "openrouter"
    shell.api_mode = "chat_completions"
    shell.base_url = "https://same-endpoint.example/v1"
    shell.api_key = "same-key"
    shell.agent = object()

    assert shell._ensure_runtime_credentials() is True
    assert shell.agent is None
    assert shell.provider == "openai-codex"
    assert shell.api_mode == "codex_responses"


def test_cli_turn_routing_uses_primary_when_disabled(monkeypatch):
    cli = _import_cli()
    shell = cli.HermesCLI(model="gpt-5", compact=True, max_turns=1)
    shell.provider = "openrouter"
    shell.api_mode = "chat_completions"
    shell.base_url = "https://openrouter.ai/api/v1"
    shell.api_key = "sk-primary"
    shell._smart_model_routing = {"enabled": False}

    result = shell._resolve_turn_agent_config("what time is it in tokyo?")

    assert result["model"] == "gpt-5"
    assert result["runtime"]["provider"] == "openrouter"
    assert result["label"] is None


def test_cli_turn_routing_uses_cheap_model_when_simple(monkeypatch):
    cli = _import_cli()

    def _runtime_resolve(**kwargs):
        assert kwargs["requested"] == "zai"
        return {
            "provider": "zai",
            "api_mode": "chat_completions",
            "base_url": "https://open.z.ai/api/v1",
            "api_key": "cheap-key",
            "source": "env/config",
        }

    monkeypatch.setattr("hermes_cli.runtime_provider.resolve_runtime_provider", _runtime_resolve)

    shell = cli.HermesCLI(model="anthropic/claude-sonnet-4", compact=True, max_turns=1)
    shell.provider = "openrouter"
    shell.api_mode = "chat_completions"
    shell.base_url = "https://openrouter.ai/api/v1"
    shell.api_key = "primary-key"
    shell._smart_model_routing = {
        "enabled": True,
        "cheap_model": {"provider": "zai", "model": "glm-5-air"},
        "max_simple_chars": 160,
        "max_simple_words": 28,
    }

    result = shell._resolve_turn_agent_config("what time is it in tokyo?")

    assert result["model"] == "glm-5-air"
    assert result["runtime"]["provider"] == "zai"
    assert result["runtime"]["api_key"] == "cheap-key"
    assert result["label"] is not None


def test_cli_prefers_config_provider_over_stale_env_override(monkeypatch):
    cli = _import_cli()

    monkeypatch.setenv("HERMES_INFERENCE_PROVIDER", "openrouter")
    config_copy = dict(cli.CLI_CONFIG)
    model_copy = dict(config_copy.get("model", {}))
    model_copy["provider"] = "custom"
    model_copy["base_url"] = "https://api.fireworks.ai/inference/v1"
    config_copy["model"] = model_copy
    monkeypatch.setattr(cli, "CLI_CONFIG", config_copy)

    shell = cli.HermesCLI(model="fireworks/minimax-m2p5", compact=True, max_turns=1)

    assert shell.requested_provider == "custom"


def test_codex_provider_replaces_incompatible_default_model(monkeypatch):
    """When provider resolves to openai-codex and no model was explicitly
    chosen, the global config default (e.g. anthropic/claude-opus-4.6) must
    be replaced with a Codex-compatible model.  Fixes #651."""
    cli = _import_cli()

    monkeypatch.delenv("LLM_MODEL", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    # Ensure local user config does not leak a model into the test
    monkeypatch.setitem(cli.CLI_CONFIG, "model", {
        "default": "",
        "base_url": "https://openrouter.ai/api/v1",
    })

    def _runtime_resolve(**kwargs):
        return {
            "provider": "openai-codex",
            "api_mode": "codex_responses",
            "base_url": "https://chatgpt.com/backend-api/codex",
            "api_key": "test-key",
            "source": "env/config",
        }

    monkeypatch.setattr("hermes_cli.runtime_provider.resolve_runtime_provider", _runtime_resolve)
    monkeypatch.setattr("hermes_cli.runtime_provider.format_runtime_provider_error", lambda exc: str(exc))
    monkeypatch.setattr(
        "hermes_cli.codex_models.get_codex_model_ids",
        lambda access_token=None: ["gpt-5.2-codex", "gpt-5.1-codex-mini"],
    )

    shell = cli.HermesCLI(compact=True, max_turns=1)

    assert shell._model_is_default is True
    assert shell._ensure_runtime_credentials() is True
    assert shell.provider == "openai-codex"
    assert "anthropic" not in shell.model
    assert "claude" not in shell.model
    assert shell.model == "gpt-5.2-codex"


def test_model_flow_nous_prints_subscription_guidance_without_mutating_explicit_tts(monkeypatch, capsys):
    monkeypatch.setenv("HERMES_ENABLE_NOUS_MANAGED_TOOLS", "1")
    config = {
        "model": {"provider": "nous", "default": "claude-opus-4-6"},
        "tts": {"provider": "elevenlabs"},
        "browser": {"cloud_provider": "browser-use"},
    }

    monkeypatch.setattr(
        "hermes_cli.auth.get_provider_auth_state",
        lambda provider: {"access_token": "nous-token"},
    )
    monkeypatch.setattr(
        "hermes_cli.auth.resolve_nous_runtime_credentials",
        lambda *args, **kwargs: {
            "base_url": "https://inference.example.com/v1",
            "api_key": "nous-key",
        },
    )
    monkeypatch.setattr(
        "hermes_cli.auth.fetch_nous_models",
        lambda *args, **kwargs: ["claude-opus-4-6"],
    )
    monkeypatch.setattr("hermes_cli.auth._prompt_model_selection", lambda model_ids, current_model="", pricing=None, **kw: "claude-opus-4-6")
    monkeypatch.setattr("hermes_cli.auth._save_model_choice", lambda model: None)
    monkeypatch.setattr("hermes_cli.auth._update_config_for_provider", lambda provider, url: None)
    monkeypatch.setattr(
        "hermes_cli.nous_subscription.get_nous_subscription_explainer_lines",
        lambda: ["Nous subscription enables managed web tools."],
    )

    hermes_main._model_flow_nous(config, current_model="claude-opus-4-6")

    out = capsys.readouterr().out
    assert "Nous subscription enables managed web tools." in out
    assert config["tts"]["provider"] == "elevenlabs"
    assert config["browser"]["cloud_provider"] == "browser-use"


def test_model_flow_nous_applies_managed_tts_default_when_unconfigured(monkeypatch, capsys):
    monkeypatch.setenv("HERMES_ENABLE_NOUS_MANAGED_TOOLS", "1")
    config = {
        "model": {"provider": "nous", "default": "claude-opus-4-6"},
        "tts": {"provider": "edge"},
    }

    monkeypatch.setattr(
        "hermes_cli.auth.get_provider_auth_state",
        lambda provider: {"access_token": "nous-token"},
    )
    monkeypatch.setattr(
        "hermes_cli.auth.resolve_nous_runtime_credentials",
        lambda *args, **kwargs: {
            "base_url": "https://inference.example.com/v1",
            "api_key": "nous-key",
        },
    )
    monkeypatch.setattr(
        "hermes_cli.auth.fetch_nous_models",
        lambda *args, **kwargs: ["claude-opus-4-6"],
    )
    monkeypatch.setattr("hermes_cli.auth._prompt_model_selection", lambda model_ids, current_model="", pricing=None, **kw: "claude-opus-4-6")
    monkeypatch.setattr("hermes_cli.auth._save_model_choice", lambda model: None)
    monkeypatch.setattr("hermes_cli.auth._update_config_for_provider", lambda provider, url: None)
    monkeypatch.setattr(
        "hermes_cli.nous_subscription.get_nous_subscription_explainer_lines",
        lambda: ["Nous subscription enables managed web tools."],
    )

    hermes_main._model_flow_nous(config, current_model="claude-opus-4-6")

    out = capsys.readouterr().out
    assert "Nous subscription enables managed web tools." in out
    assert "OpenAI TTS via your Nous subscription" in out
    assert config["tts"]["provider"] == "openai"


def test_codex_provider_uses_config_model(monkeypatch):
    """Model comes from config.yaml, not LLM_MODEL env var.
    Config.yaml is the single source of truth to avoid multi-agent conflicts."""
    cli = _import_cli()

    # LLM_MODEL env var should be IGNORED (even if set)
    monkeypatch.setenv("LLM_MODEL", "should-be-ignored")
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    # Set model via config
    monkeypatch.setitem(cli.CLI_CONFIG, "model", {
        "default": "gpt-5.2-codex",
        "provider": "openai-codex",
        "base_url": "https://chatgpt.com/backend-api/codex",
    })

    def _runtime_resolve(**kwargs):
        return {
            "provider": "openai-codex",
            "api_mode": "codex_responses",
            "base_url": "https://chatgpt.com/backend-api/codex",
            "api_key": "fake-codex-token",
            "source": "env/config",
        }

    monkeypatch.setattr("hermes_cli.runtime_provider.resolve_runtime_provider", _runtime_resolve)
    monkeypatch.setattr("hermes_cli.runtime_provider.format_runtime_provider_error", lambda exc: str(exc))
    # Prevent live API call from overriding the config model
    monkeypatch.setattr(
        "hermes_cli.codex_models.get_codex_model_ids",
        lambda access_token=None: ["gpt-5.2-codex"],
    )

    shell = cli.HermesCLI(compact=True, max_turns=1)

    assert shell._ensure_runtime_credentials() is True
    assert shell.provider == "openai-codex"
    # Model from config (may be normalized by codex provider logic)
    assert "codex" in shell.model.lower()
    # LLM_MODEL env var is NOT used
    assert shell.model != "should-be-ignored"


def test_codex_config_model_not_replaced_by_normalization(monkeypatch):
    """When the user sets model.default in config.yaml to a specific codex
    model, _normalize_model_for_provider must NOT replace it with the latest
    available model from the API.  Regression test for #1887."""
    cli = _import_cli()

    monkeypatch.delenv("LLM_MODEL", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    # User explicitly configured gpt-5.3-codex in config.yaml
    monkeypatch.setitem(cli.CLI_CONFIG, "model", {
        "default": "gpt-5.3-codex",
        "provider": "openai-codex",
        "base_url": "https://chatgpt.com/backend-api/codex",
    })

    def _runtime_resolve(**kwargs):
        return {
            "provider": "openai-codex",
            "api_mode": "codex_responses",
            "base_url": "https://chatgpt.com/backend-api/codex",
            "api_key": "fake-key",
            "source": "env/config",
        }

    monkeypatch.setattr("hermes_cli.runtime_provider.resolve_runtime_provider", _runtime_resolve)
    monkeypatch.setattr("hermes_cli.runtime_provider.format_runtime_provider_error", lambda exc: str(exc))
    # API returns a DIFFERENT model than what the user configured
    monkeypatch.setattr(
        "hermes_cli.codex_models.get_codex_model_ids",
        lambda access_token=None: ["gpt-5.4", "gpt-5.3-codex"],
    )

    shell = cli.HermesCLI(compact=True, max_turns=1)

    # Config model is NOT the global default — user made a deliberate choice
    assert shell._model_is_default is False
    assert shell._ensure_runtime_credentials() is True
    assert shell.provider == "openai-codex"
    # Model must stay as user configured, not replaced by gpt-5.4
    assert shell.model == "gpt-5.3-codex"


def test_codex_provider_preserves_explicit_codex_model(monkeypatch):
    """If the user explicitly passes a Codex-compatible model, it must be
    preserved even when the provider resolves to openai-codex."""
    cli = _import_cli()

    monkeypatch.delenv("LLM_MODEL", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    def _runtime_resolve(**kwargs):
        return {
            "provider": "openai-codex",
            "api_mode": "codex_responses",
            "base_url": "https://chatgpt.com/backend-api/codex",
            "api_key": "test-key",
            "source": "env/config",
        }

    monkeypatch.setattr("hermes_cli.runtime_provider.resolve_runtime_provider", _runtime_resolve)
    monkeypatch.setattr("hermes_cli.runtime_provider.format_runtime_provider_error", lambda exc: str(exc))

    shell = cli.HermesCLI(model="gpt-5.1-codex-mini", compact=True, max_turns=1)

    assert shell._model_is_default is False
    assert shell._ensure_runtime_credentials() is True
    assert shell.model == "gpt-5.1-codex-mini"


def test_codex_provider_strips_provider_prefix_from_model(monkeypatch):
    """openai/gpt-5.3-codex should become gpt-5.3-codex — the Codex
    Responses API does not accept provider-prefixed model slugs."""
    cli = _import_cli()

    monkeypatch.delenv("LLM_MODEL", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)

    def _runtime_resolve(**kwargs):
        return {
            "provider": "openai-codex",
            "api_mode": "codex_responses",
            "base_url": "https://chatgpt.com/backend-api/codex",
            "api_key": "test-key",
            "source": "env/config",
        }

    monkeypatch.setattr("hermes_cli.runtime_provider.resolve_runtime_provider", _runtime_resolve)
    monkeypatch.setattr("hermes_cli.runtime_provider.format_runtime_provider_error", lambda exc: str(exc))

    shell = cli.HermesCLI(model="openai/gpt-5.3-codex", compact=True, max_turns=1)

    assert shell._ensure_runtime_credentials() is True
    assert shell.model == "gpt-5.3-codex"


def test_cmd_model_falls_back_to_auto_on_invalid_provider(monkeypatch, capsys):
    monkeypatch.setattr(
        "hermes_cli.config.load_config",
        lambda: {"model": {"default": "gpt-5", "provider": "invalid-provider"}},
    )
    monkeypatch.setattr("hermes_cli.config.save_config", lambda cfg: None)
    monkeypatch.setattr("hermes_cli.config.get_env_value", lambda key: "")
    monkeypatch.setattr("hermes_cli.config.save_env_value", lambda key, value: None)

    def _resolve_provider(requested, **kwargs):
        if requested == "invalid-provider":
            raise AuthError("Unknown provider 'invalid-provider'.", code="invalid_provider")
        return "openrouter"

    monkeypatch.setattr("hermes_cli.auth.resolve_provider", _resolve_provider)
    monkeypatch.setattr(hermes_main, "_prompt_provider_choice", lambda choices, **kwargs: len(choices) - 1)
    monkeypatch.setattr("sys.stdin", type("FakeTTY", (), {"isatty": lambda self: True})())

    hermes_main.cmd_model(SimpleNamespace())
    output = capsys.readouterr().out

    assert "Warning:" in output
    assert "falling back to auto provider detection" in output.lower()
    assert "No change." in output


def test_model_flow_custom_saves_verified_v1_base_url(monkeypatch, capsys):
    monkeypatch.setattr(
        "hermes_cli.config.get_env_value",
        lambda key: "" if key in {"OPENAI_BASE_URL", "OPENAI_API_KEY"} else "",
    )
    saved_env = {}
    monkeypatch.setattr("hermes_cli.config.save_env_value", lambda key, value: saved_env.__setitem__(key, value))
    monkeypatch.setattr("hermes_cli.auth._save_model_choice", lambda model: saved_env.__setitem__("MODEL", model))
    monkeypatch.setattr("hermes_cli.auth.deactivate_provider", lambda: None)
    monkeypatch.setattr("hermes_cli.main._save_custom_provider", lambda *args, **kwargs: None)
    monkeypatch.setattr(
        "hermes_cli.models.probe_api_models",
        lambda api_key, base_url: {
            "models": ["llm"],
            "probed_url": "http://localhost:8000/v1/models",
            "resolved_base_url": "http://localhost:8000/v1",
            "suggested_base_url": "http://localhost:8000/v1",
            "used_fallback": True,
        },
    )
    monkeypatch.setattr(
        "hermes_cli.config.load_config",
        lambda: {"model": {"default": "", "provider": "custom", "base_url": ""}},
    )
    monkeypatch.setattr("hermes_cli.config.save_config", lambda cfg: None)

    # After the probe detects a single model ("llm"), the flow asks
    # "Use this model? [Y/n]:" — confirm with Enter, then context length.
    answers = iter(["http://localhost:8000", "local-key", "", ""])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    monkeypatch.setattr("getpass.getpass", lambda _prompt="": next(answers))

    hermes_main._model_flow_custom({})
    output = capsys.readouterr().out

    assert "Saving the working base URL instead" in output
    assert "Detected model: llm" in output
    # OPENAI_BASE_URL is no longer saved to .env — config.yaml is authoritative
    assert "OPENAI_BASE_URL" not in saved_env
    assert saved_env["MODEL"] == "llm"


def test_cmd_model_forwards_nous_login_tls_options(monkeypatch):
    monkeypatch.setattr(hermes_main, "_require_tty", lambda *a: None)
    monkeypatch.setattr(
        "hermes_cli.config.load_config",
        lambda: {"model": {"default": "gpt-5", "provider": "nous"}},
    )
    monkeypatch.setattr("hermes_cli.config.save_config", lambda cfg: None)
    monkeypatch.setattr("hermes_cli.config.get_env_value", lambda key: "")
    monkeypatch.setattr("hermes_cli.config.save_env_value", lambda key, value: None)
    monkeypatch.setattr("hermes_cli.auth.resolve_provider", lambda requested, **kwargs: "nous")
    monkeypatch.setattr("hermes_cli.auth.get_provider_auth_state", lambda provider_id: None)
    monkeypatch.setattr(hermes_main, "_prompt_provider_choice", lambda choices, **kwargs: 0)

    captured = {}

    def _fake_login(login_args, provider_config):
        captured["portal_url"] = login_args.portal_url
        captured["inference_url"] = login_args.inference_url
        captured["client_id"] = login_args.client_id
        captured["scope"] = login_args.scope
        captured["no_browser"] = login_args.no_browser
        captured["timeout"] = login_args.timeout
        captured["ca_bundle"] = login_args.ca_bundle
        captured["insecure"] = login_args.insecure

    monkeypatch.setattr("hermes_cli.auth._login_nous", _fake_login)

    hermes_main.cmd_model(
        SimpleNamespace(
            portal_url="https://portal.nousresearch.com",
            inference_url="https://inference.nousresearch.com/v1",
            client_id="hermes-local",
            scope="openid profile",
            no_browser=True,
            timeout=7.5,
            ca_bundle="/tmp/local-ca.pem",
            insecure=True,
        )
    )

    assert captured == {
        "portal_url": "https://portal.nousresearch.com",
        "inference_url": "https://inference.nousresearch.com/v1",
        "client_id": "hermes-local",
        "scope": "openid profile",
        "no_browser": True,
        "timeout": 7.5,
        "ca_bundle": "/tmp/local-ca.pem",
        "insecure": True,
    }

```

## File: test_cli_retry.py
```
"""Regression tests for CLI /retry history replacement semantics."""

from tests.cli.test_cli_init import _make_cli


def test_retry_last_truncates_history_before_requeueing_message():
    cli = _make_cli()
    cli.conversation_history = [
        {"role": "user", "content": "first"},
        {"role": "assistant", "content": "one"},
        {"role": "user", "content": "retry me"},
        {"role": "assistant", "content": "old answer"},
    ]

    retry_msg = cli.retry_last()

    assert retry_msg == "retry me"
    assert cli.conversation_history == [
        {"role": "user", "content": "first"},
        {"role": "assistant", "content": "one"},
    ]

    cli.conversation_history.append({"role": "user", "content": retry_msg})
    cli.conversation_history.append({"role": "assistant", "content": "new answer"})

    assert [m["content"] for m in cli.conversation_history if m["role"] == "user"] == [
        "first",
        "retry me",
    ]


def test_process_command_retry_requeues_original_message_not_retry_command():
    cli = _make_cli()
    queued = []

    class _Queue:
        def put(self, value):
            queued.append(value)

    cli._pending_input = _Queue()
    cli.conversation_history = [
        {"role": "user", "content": "retry me"},
        {"role": "assistant", "content": "old answer"},
    ]

    cli.process_command("/retry")

    assert queued == ["retry me"]
    assert cli.conversation_history == []

```

## File: test_cli_save_config_value.py
```
"""Tests for save_config_value() in cli.py — atomic write behavior."""

import os
import yaml
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest


class TestSaveConfigValueAtomic:
    """save_config_value() must use atomic_yaml_write to avoid data loss."""

    @pytest.fixture
    def config_env(self, tmp_path, monkeypatch):
        """Isolated config environment with a writable config.yaml."""
        hermes_home = tmp_path / ".hermes"
        hermes_home.mkdir()
        config_path = hermes_home / "config.yaml"
        config_path.write_text(yaml.dump({
            "model": {"default": "test-model", "provider": "openrouter"},
            "display": {"skin": "default"},
        }))
        monkeypatch.setattr("cli._hermes_home", hermes_home)
        return config_path

    def test_calls_atomic_yaml_write(self, config_env, monkeypatch):
        """save_config_value must route through atomic_yaml_write, not bare open()."""
        mock_atomic = MagicMock()
        monkeypatch.setattr("utils.atomic_yaml_write", mock_atomic)

        from cli import save_config_value
        save_config_value("display.skin", "mono")

        mock_atomic.assert_called_once()
        written_path, written_data = mock_atomic.call_args[0]
        assert Path(written_path) == config_env
        assert written_data["display"]["skin"] == "mono"

    def test_preserves_existing_keys(self, config_env):
        """Writing a new key must not clobber existing config entries."""
        from cli import save_config_value
        save_config_value("agent.max_turns", 50)

        result = yaml.safe_load(config_env.read_text())
        assert result["model"]["default"] == "test-model"
        assert result["model"]["provider"] == "openrouter"
        assert result["display"]["skin"] == "default"
        assert result["agent"]["max_turns"] == 50

    def test_creates_nested_keys(self, config_env):
        """Dot-separated paths create intermediate dicts as needed."""
        from cli import save_config_value
        save_config_value("compression.summary_model", "google/gemini-3-flash-preview")

        result = yaml.safe_load(config_env.read_text())
        assert result["compression"]["summary_model"] == "google/gemini-3-flash-preview"

    def test_overwrites_existing_value(self, config_env):
        """Updating an existing key replaces the value."""
        from cli import save_config_value
        save_config_value("display.skin", "ares")

        result = yaml.safe_load(config_env.read_text())
        assert result["display"]["skin"] == "ares"

    def test_file_not_truncated_on_error(self, config_env, monkeypatch):
        """If atomic_yaml_write raises, the original file is untouched."""
        original_content = config_env.read_text()

        def exploding_write(*args, **kwargs):
            raise OSError("disk full")

        monkeypatch.setattr("utils.atomic_yaml_write", exploding_write)

        from cli import save_config_value
        result = save_config_value("display.skin", "broken")

        assert result is False
        assert config_env.read_text() == original_content

```

## File: test_cli_secret_capture.py
```
import queue
import threading
import time
from unittest.mock import patch

import cli as cli_module
import tools.skills_tool as skills_tool_module
from cli import HermesCLI
from hermes_cli.callbacks import prompt_for_secret
from tools.skills_tool import set_secret_capture_callback


class _FakeBuffer:
    def __init__(self):
        self.reset_called = False

    def reset(self):
        self.reset_called = True


class _FakeApp:
    def __init__(self):
        self.invalidated = False
        self.current_buffer = _FakeBuffer()

    def invalidate(self):
        self.invalidated = True


def _make_cli_stub(with_app=False):
    cli = HermesCLI.__new__(HermesCLI)
    cli._app = _FakeApp() if with_app else None
    cli._last_invalidate = 0.0
    cli._secret_state = None
    cli._secret_deadline = 0
    return cli


def test_secret_capture_callback_can_be_completed_from_cli_state_machine():
    cli = _make_cli_stub(with_app=True)
    results = []

    with patch("hermes_cli.callbacks.save_env_value_secure") as save_secret:
        save_secret.return_value = {
            "success": True,
            "stored_as": "TENOR_API_KEY",
            "validated": False,
        }

        thread = threading.Thread(
            target=lambda: results.append(
                cli._secret_capture_callback("TENOR_API_KEY", "Tenor API key")
            )
        )
        thread.start()

        deadline = time.time() + 2
        while cli._secret_state is None and time.time() < deadline:
            time.sleep(0.01)

        assert cli._secret_state is not None
        cli._submit_secret_response("super-secret-value")
        thread.join(timeout=2)

    assert results[0]["success"] is True
    assert results[0]["stored_as"] == "TENOR_API_KEY"
    assert results[0]["skipped"] is False


def test_cancel_secret_capture_marks_setup_skipped():
    cli = _make_cli_stub()
    cli._secret_state = {
        "response_queue": queue.Queue(),
        "var_name": "TENOR_API_KEY",
        "prompt": "Tenor API key",
        "metadata": {},
    }
    cli._secret_deadline = 123

    cli._cancel_secret_capture()

    assert cli._secret_state is None
    assert cli._secret_deadline == 0


def test_secret_capture_uses_getpass_without_tui():
    cli = _make_cli_stub()

    with patch("hermes_cli.callbacks.getpass.getpass", return_value="secret-value"), patch(
        "hermes_cli.callbacks.save_env_value_secure"
    ) as save_secret:
        save_secret.return_value = {
            "success": True,
            "stored_as": "TENOR_API_KEY",
            "validated": False,
        }
        result = prompt_for_secret(cli, "TENOR_API_KEY", "Tenor API key")

    assert result["success"] is True
    assert result["stored_as"] == "TENOR_API_KEY"
    assert result["skipped"] is False


def test_secret_capture_timeout_clears_hidden_input_buffer():
    cli = _make_cli_stub(with_app=True)
    cleared = {"value": False}

    def clear_buffer():
        cleared["value"] = True

    cli._clear_secret_input_buffer = clear_buffer

    with patch("hermes_cli.callbacks.queue.Queue.get", side_effect=queue.Empty), patch(
        "hermes_cli.callbacks._time.monotonic",
        side_effect=[0, 121],
    ):
        result = prompt_for_secret(cli, "TENOR_API_KEY", "Tenor API key")

    assert result["success"] is True
    assert result["skipped"] is True
    assert result["reason"] == "timeout"
    assert cleared["value"] is True


def test_cli_chat_registers_secret_capture_callback():
    clean_config = {
        "model": {
            "default": "anthropic/claude-opus-4.6",
            "base_url": "https://openrouter.ai/api/v1",
            "provider": "auto",
        },
        "display": {"compact": False, "tool_progress": "all"},
        "agent": {},
        "terminal": {"env_type": "local"},
    }

    with patch("cli.get_tool_definitions", return_value=[]), patch.dict(
        "os.environ", {"LLM_MODEL": "", "HERMES_MAX_ITERATIONS": ""}, clear=False
    ), patch.dict(cli_module.__dict__, {"CLI_CONFIG": clean_config}):
        cli_obj = HermesCLI()
        with patch.object(cli_obj, "_ensure_runtime_credentials", return_value=False):
            cli_obj.chat("hello")

    try:
        assert skills_tool_module._secret_capture_callback == cli_obj._secret_capture_callback
    finally:
        set_secret_capture_callback(None)

```

## File: test_cli_skin_integration.py
```
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from cli import HermesCLI, _rich_text_from_ansi
from hermes_cli.skin_engine import get_active_skin, set_active_skin


def _make_cli_stub():
    cli = HermesCLI.__new__(HermesCLI)
    cli._sudo_state = None
    cli._secret_state = None
    cli._approval_state = None
    cli._clarify_state = None
    cli._clarify_freetext = False
    cli._command_running = False
    cli._agent_running = False
    cli._voice_recording = False
    cli._voice_processing = False
    cli._voice_mode = False
    cli._command_spinner_frame = lambda: "⟳"
    cli._tui_style_base = {
        "prompt": "#fff",
        "input-area": "#fff",
        "input-rule": "#aaa",
        "prompt-working": "#888 italic",
    }
    cli._app = SimpleNamespace(style=None)
    cli._invalidate = MagicMock()
    return cli


class TestCliSkinPromptIntegration:
    def test_default_prompt_fragments_use_default_symbol(self):
        cli = _make_cli_stub()

        set_active_skin("default")
        assert cli._get_tui_prompt_fragments() == [("class:prompt", "❯ ")]

    def test_ares_prompt_fragments_use_skin_symbol(self):
        cli = _make_cli_stub()

        set_active_skin("ares")
        assert cli._get_tui_prompt_fragments() == [("class:prompt", "⚔ ❯ ")]

    def test_secret_prompt_fragments_preserve_secret_state(self):
        cli = _make_cli_stub()
        cli._secret_state = {"response_queue": object()}

        set_active_skin("ares")
        assert cli._get_tui_prompt_fragments() == [("class:sudo-prompt", "🔑 ❯ ")]

    def test_icon_only_skin_symbol_still_visible_in_special_states(self):
        cli = _make_cli_stub()
        cli._secret_state = {"response_queue": object()}

        with patch("hermes_cli.skin_engine.get_active_prompt_symbol", return_value="⚔ "):
            assert cli._get_tui_prompt_fragments() == [("class:sudo-prompt", "🔑 ⚔ ")]

    def test_build_tui_style_dict_uses_skin_overrides(self):
        cli = _make_cli_stub()

        set_active_skin("ares")
        skin = get_active_skin()
        style_dict = cli._build_tui_style_dict()

        assert style_dict["prompt"] == skin.get_color("prompt")
        assert style_dict["input-rule"] == skin.get_color("input_rule")
        assert style_dict["prompt-working"] == f"{skin.get_color('banner_dim')} italic"
        assert style_dict["approval-title"] == f"{skin.get_color('ui_warn')} bold"

    def test_apply_tui_skin_style_updates_running_app(self):
        cli = _make_cli_stub()

        set_active_skin("ares")
        assert cli._apply_tui_skin_style() is True
        assert cli._app.style is not None
        cli._invalidate.assert_called_once_with(min_interval=0.0)

    def test_handle_skin_command_refreshes_live_tui(self, capsys):
        cli = _make_cli_stub()

        with patch("cli.save_config_value", return_value=True):
            cli._handle_skin_command("/skin ares")

        output = capsys.readouterr().out
        assert "Skin set to: ares (saved)" in output
        assert "Prompt + TUI colors updated." in output
        assert cli._app.style is not None


class TestAnsiRichTextHelper:
    def test_preserves_literal_brackets(self):
        text = _rich_text_from_ansi("[notatag] literal")
        assert text.plain == "[notatag] literal"

    def test_strips_ansi_but_keeps_plain_text(self):
        text = _rich_text_from_ansi("\x1b[31mred\x1b[0m")
        assert text.plain == "red"

```

## File: test_cli_status_bar.py
```
from datetime import datetime, timedelta
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from cli import HermesCLI


def _make_cli(model: str = "anthropic/claude-sonnet-4-20250514"):
    cli_obj = HermesCLI.__new__(HermesCLI)
    cli_obj.model = model
    cli_obj.session_start = datetime.now() - timedelta(minutes=14, seconds=32)
    cli_obj.conversation_history = [{"role": "user", "content": "hi"}]
    cli_obj.agent = None
    return cli_obj


def _attach_agent(
    cli_obj,
    *,
    input_tokens: int | None = None,
    output_tokens: int | None = None,
    cache_read_tokens: int = 0,
    cache_write_tokens: int = 0,
    prompt_tokens: int,
    completion_tokens: int,
    total_tokens: int,
    api_calls: int,
    context_tokens: int,
    context_length: int,
    compressions: int = 0,
):
    cli_obj.agent = SimpleNamespace(
        model=cli_obj.model,
        provider="anthropic" if cli_obj.model.startswith("anthropic/") else None,
        base_url="",
        session_input_tokens=input_tokens if input_tokens is not None else prompt_tokens,
        session_output_tokens=output_tokens if output_tokens is not None else completion_tokens,
        session_cache_read_tokens=cache_read_tokens,
        session_cache_write_tokens=cache_write_tokens,
        session_prompt_tokens=prompt_tokens,
        session_completion_tokens=completion_tokens,
        session_total_tokens=total_tokens,
        session_api_calls=api_calls,
        context_compressor=SimpleNamespace(
            last_prompt_tokens=context_tokens,
            context_length=context_length,
            compression_count=compressions,
        ),
    )
    return cli_obj


class TestCLIStatusBar:
    def test_context_style_thresholds(self):
        cli_obj = _make_cli()

        assert cli_obj._status_bar_context_style(None) == "class:status-bar-dim"
        assert cli_obj._status_bar_context_style(10) == "class:status-bar-good"
        assert cli_obj._status_bar_context_style(50) == "class:status-bar-warn"
        assert cli_obj._status_bar_context_style(81) == "class:status-bar-bad"
        assert cli_obj._status_bar_context_style(95) == "class:status-bar-critical"

    def test_build_status_bar_text_for_wide_terminal(self):
        cli_obj = _attach_agent(
            _make_cli(),
            prompt_tokens=10_230,
            completion_tokens=2_220,
            total_tokens=12_450,
            api_calls=7,
            context_tokens=12_450,
            context_length=200_000,
        )

        text = cli_obj._build_status_bar_text(width=120)

        assert "claude-sonnet-4-20250514" in text
        assert "12.4K/200K" in text
        assert "6%" in text
        assert "$0.06" not in text  # cost hidden by default
        assert "15m" in text

    def test_input_height_counts_wide_characters_using_cell_width(self):
        cli_obj = _make_cli()

        class _Doc:
            lines = ["你" * 10]

        class _Buffer:
            document = _Doc()

        input_area = SimpleNamespace(buffer=_Buffer())

        def _input_height():
            try:
                from prompt_toolkit.application import get_app
                from prompt_toolkit.utils import get_cwidth

                doc = input_area.buffer.document
                prompt_width = max(2, get_cwidth(cli_obj._get_tui_prompt_text()))
                try:
                    available_width = get_app().output.get_size().columns - prompt_width
                except Exception:
                    import shutil
                    available_width = shutil.get_terminal_size((80, 24)).columns - prompt_width
                if available_width < 10:
                    available_width = 40
                visual_lines = 0
                for line in doc.lines:
                    line_width = get_cwidth(line)
                    if line_width <= 0:
                        visual_lines += 1
                    else:
                        visual_lines += max(1, -(-line_width // available_width))
                return min(max(visual_lines, 1), 8)
            except Exception:
                return 1

        mock_app = MagicMock()
        mock_app.output.get_size.return_value = MagicMock(columns=14)
        with patch.object(HermesCLI, "_get_tui_prompt_text", return_value="❯ "), \
             patch("prompt_toolkit.application.get_app", return_value=mock_app):
            assert _input_height() == 2

    def test_input_height_uses_prompt_toolkit_width_over_shutil(self):
        cli_obj = _make_cli()

        class _Doc:
            lines = ["你" * 10]

        class _Buffer:
            document = _Doc()

        input_area = SimpleNamespace(buffer=_Buffer())

        def _input_height():
            try:
                from prompt_toolkit.application import get_app
                from prompt_toolkit.utils import get_cwidth

                doc = input_area.buffer.document
                prompt_width = max(2, get_cwidth(cli_obj._get_tui_prompt_text()))
                try:
                    available_width = get_app().output.get_size().columns - prompt_width
                except Exception:
                    import shutil
                    available_width = shutil.get_terminal_size((80, 24)).columns - prompt_width
                if available_width < 10:
                    available_width = 40
                visual_lines = 0
                for line in doc.lines:
                    line_width = get_cwidth(line)
                    if line_width <= 0:
                        visual_lines += 1
                    else:
                        visual_lines += max(1, -(-line_width // available_width))
                return min(max(visual_lines, 1), 8)
            except Exception:
                return 1

        mock_app = MagicMock()
        mock_app.output.get_size.return_value = MagicMock(columns=14)
        with patch.object(HermesCLI, "_get_tui_prompt_text", return_value="❯ "), \
             patch("prompt_toolkit.application.get_app", return_value=mock_app), \
             patch("shutil.get_terminal_size") as mock_shutil:
            assert _input_height() == 2
        mock_shutil.assert_not_called()

    def test_build_status_bar_text_no_cost_in_status_bar(self):
        cli_obj = _attach_agent(
            _make_cli(),
            prompt_tokens=10000,
            completion_tokens=5000,
            total_tokens=15000,
            api_calls=7,
            context_tokens=50000,
            context_length=200_000,
        )

        text = cli_obj._build_status_bar_text(width=120)
        assert "$" not in text  # cost is never shown in status bar

    def test_build_status_bar_text_collapses_for_narrow_terminal(self):
        cli_obj = _attach_agent(
            _make_cli(),
            prompt_tokens=10000,
            completion_tokens=2400,
            total_tokens=12400,
            api_calls=7,
            context_tokens=12400,
            context_length=200_000,
        )

        text = cli_obj._build_status_bar_text(width=60)

        assert "⚕" in text
        assert "$0.06" not in text  # cost hidden by default
        assert "15m" in text
        assert "200K" not in text

    def test_build_status_bar_text_handles_missing_agent(self):
        cli_obj = _make_cli()

        text = cli_obj._build_status_bar_text(width=100)

        assert "⚕" in text
        assert "claude-sonnet-4-20250514" in text


class TestCLIUsageReport:
    def test_show_usage_includes_estimated_cost(self, capsys):
        cli_obj = _attach_agent(
            _make_cli(),
            prompt_tokens=10_230,
            completion_tokens=2_220,
            total_tokens=12_450,
            api_calls=7,
            context_tokens=12_450,
            context_length=200_000,
            compressions=1,
        )
        cli_obj.verbose = False

        cli_obj._show_usage()
        output = capsys.readouterr().out

        assert "Model:" in output
        assert "Cost status:" in output
        assert "Cost source:" in output
        assert "Total cost:" in output
        assert "$" in output
        assert "0.064" in output
        assert "Session duration:" in output
        assert "Compressions:" in output

    def test_show_usage_marks_unknown_pricing(self, capsys):
        cli_obj = _attach_agent(
            _make_cli(model="local/my-custom-model"),
            prompt_tokens=1_000,
            completion_tokens=500,
            total_tokens=1_500,
            api_calls=1,
            context_tokens=1_000,
            context_length=32_000,
        )
        cli_obj.verbose = False

        cli_obj._show_usage()
        output = capsys.readouterr().out

        assert "Total cost:" in output
        assert "n/a" in output
        assert "Pricing unknown for local/my-custom-model" in output

    def test_zero_priced_provider_models_stay_unknown(self, capsys):
        cli_obj = _attach_agent(
            _make_cli(model="glm-5"),
            prompt_tokens=1_000,
            completion_tokens=500,
            total_tokens=1_500,
            api_calls=1,
            context_tokens=1_000,
            context_length=32_000,
        )
        cli_obj.verbose = False

        cli_obj._show_usage()
        output = capsys.readouterr().out

        assert "Total cost:" in output
        assert "n/a" in output
        assert "Pricing unknown for glm-5" in output


class TestStatusBarWidthSource:
    """Ensure status bar fragments don't overflow the terminal width."""

    def _make_wide_cli(self):
        from datetime import datetime, timedelta
        cli_obj = _attach_agent(
            _make_cli(),
            prompt_tokens=100_000,
            completion_tokens=5_000,
            total_tokens=105_000,
            api_calls=20,
            context_tokens=100_000,
            context_length=200_000,
        )
        cli_obj._status_bar_visible = True
        return cli_obj

    def test_fragments_fit_within_announced_width(self):
        """Total fragment text length must not exceed the width used to build them."""
        from unittest.mock import MagicMock, patch
        cli_obj = self._make_wide_cli()

        for width in (40, 52, 76, 80, 120, 200):
            mock_app = MagicMock()
            mock_app.output.get_size.return_value = MagicMock(columns=width)

            with patch("prompt_toolkit.application.get_app", return_value=mock_app):
                frags = cli_obj._get_status_bar_fragments()

            total_text = "".join(text for _, text in frags)
            display_width = cli_obj._status_bar_display_width(total_text)
            assert display_width <= width + 4, (  # +4 for minor padding chars
                f"At width={width}, fragment total {display_width} cells overflows "
                f"({total_text!r})"
            )

    def test_fragments_use_pt_width_over_shutil(self):
        """When prompt_toolkit reports a width, shutil.get_terminal_size must not be used."""
        from unittest.mock import MagicMock, patch
        cli_obj = self._make_wide_cli()

        mock_app = MagicMock()
        mock_app.output.get_size.return_value = MagicMock(columns=120)

        with patch("prompt_toolkit.application.get_app", return_value=mock_app) as mock_get_app, \
             patch("shutil.get_terminal_size") as mock_shutil:
            cli_obj._get_status_bar_fragments()

        mock_shutil.assert_not_called()

    def test_fragments_fall_back_to_shutil_when_no_app(self):
        """Outside a TUI context (no running app), shutil must be used as fallback."""
        from unittest.mock import MagicMock, patch
        cli_obj = self._make_wide_cli()

        with patch("prompt_toolkit.application.get_app", side_effect=Exception("no app")), \
             patch("shutil.get_terminal_size", return_value=MagicMock(columns=100)) as mock_shutil:
            frags = cli_obj._get_status_bar_fragments()

        mock_shutil.assert_called()
        assert len(frags) > 0

    def test_build_status_bar_text_uses_pt_width(self):
        """_build_status_bar_text() must also prefer prompt_toolkit width."""
        from unittest.mock import MagicMock, patch
        cli_obj = self._make_wide_cli()

        mock_app = MagicMock()
        mock_app.output.get_size.return_value = MagicMock(columns=80)

        with patch("prompt_toolkit.application.get_app", return_value=mock_app), \
             patch("shutil.get_terminal_size") as mock_shutil:
            text = cli_obj._build_status_bar_text()  # no explicit width

        mock_shutil.assert_not_called()
        assert isinstance(text, str)
        assert len(text) > 0

    def test_explicit_width_skips_pt_lookup(self):
        """An explicit width= argument must bypass both PT and shutil lookups."""
        from unittest.mock import patch
        cli_obj = self._make_wide_cli()

        with patch("prompt_toolkit.application.get_app") as mock_get_app, \
             patch("shutil.get_terminal_size") as mock_shutil:
            text = cli_obj._build_status_bar_text(width=100)

        mock_get_app.assert_not_called()
        mock_shutil.assert_not_called()
        assert len(text) > 0

```

## File: test_cli_tools_command.py
```
"""Tests for /tools slash command handler in the interactive CLI."""

from unittest.mock import MagicMock, patch, call

from cli import HermesCLI


def _make_cli(enabled_toolsets=None):
    """Build a minimal HermesCLI stub without running __init__."""
    cli_obj = HermesCLI.__new__(HermesCLI)
    cli_obj.enabled_toolsets = set(enabled_toolsets or ["web", "memory"])
    cli_obj._command_running = False
    cli_obj.console = MagicMock()
    return cli_obj


# ── /tools (no subcommand) ──────────────────────────────────────────────────


class TestToolsSlashNoSubcommand:

    def test_bare_tools_shows_tool_list(self):
        cli_obj = _make_cli()
        with patch.object(cli_obj, "show_tools") as mock_show:
            cli_obj._handle_tools_command("/tools")
        mock_show.assert_called_once()

    def test_unknown_subcommand_falls_back_to_show_tools(self):
        cli_obj = _make_cli()
        with patch.object(cli_obj, "show_tools") as mock_show:
            cli_obj._handle_tools_command("/tools foobar")
        mock_show.assert_called_once()


# ── /tools list ─────────────────────────────────────────────────────────────


class TestToolsSlashList:

    def test_list_calls_backend(self, capsys):
        cli_obj = _make_cli()
        with patch("hermes_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["web"]}}), \
             patch("hermes_cli.tools_config.save_config"):
            cli_obj._handle_tools_command("/tools list")
        out = capsys.readouterr().out
        assert "web" in out

    def test_list_does_not_modify_enabled_toolsets(self):
        """List is read-only — self.enabled_toolsets must not change."""
        cli_obj = _make_cli(["web", "memory"])
        with patch("hermes_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["web"]}}):
            cli_obj._handle_tools_command("/tools list")
        assert cli_obj.enabled_toolsets == {"web", "memory"}


# ── /tools disable (session reset) ──────────────────────────────────────────


class TestToolsSlashDisableWithReset:

    def test_disable_applies_directly_and_resets_session(self):
        """Disable applies immediately (no confirmation prompt) and resets session."""
        cli_obj = _make_cli(["web", "memory"])
        with patch("hermes_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["web", "memory"]}}), \
             patch("hermes_cli.tools_config.save_config"), \
             patch("hermes_cli.tools_config._get_platform_tools", return_value={"memory"}), \
             patch("hermes_cli.config.load_config", return_value={}), \
             patch.object(cli_obj, "new_session") as mock_reset:
            cli_obj._handle_tools_command("/tools disable web")
        mock_reset.assert_called_once()
        assert "web" not in cli_obj.enabled_toolsets

    def test_disable_does_not_prompt_for_confirmation(self):
        """Disable no longer uses input() — it applies directly."""
        cli_obj = _make_cli(["web", "memory"])
        with patch("hermes_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["web", "memory"]}}), \
             patch("hermes_cli.tools_config.save_config"), \
             patch("hermes_cli.tools_config._get_platform_tools", return_value={"memory"}), \
             patch("hermes_cli.config.load_config", return_value={}), \
             patch.object(cli_obj, "new_session"), \
             patch("builtins.input") as mock_input:
            cli_obj._handle_tools_command("/tools disable web")
        mock_input.assert_not_called()

    def test_disable_always_resets_session(self):
        """Even without a confirmation prompt, disable always resets the session."""
        cli_obj = _make_cli(["web", "memory"])
        with patch("hermes_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["web", "memory"]}}), \
             patch("hermes_cli.tools_config.save_config"), \
             patch("hermes_cli.tools_config._get_platform_tools", return_value={"memory"}), \
             patch("hermes_cli.config.load_config", return_value={}), \
             patch.object(cli_obj, "new_session") as mock_reset:
            cli_obj._handle_tools_command("/tools disable web")
        mock_reset.assert_called_once()

    def test_disable_missing_name_prints_usage(self, capsys):
        cli_obj = _make_cli()
        cli_obj._handle_tools_command("/tools disable")
        out = capsys.readouterr().out
        assert "Usage" in out


# ── /tools enable (session reset) ───────────────────────────────────────────


class TestToolsSlashEnableWithReset:

    def test_enable_applies_directly_and_resets_session(self):
        """Enable applies immediately (no confirmation prompt) and resets session."""
        cli_obj = _make_cli(["memory"])
        with patch("hermes_cli.tools_config.load_config",
                   return_value={"platform_toolsets": {"cli": ["memory"]}}), \
             patch("hermes_cli.tools_config.save_config"), \
             patch("hermes_cli.tools_config._get_platform_tools", return_value={"memory", "web"}), \
             patch("hermes_cli.config.load_config", return_value={}), \
             patch.object(cli_obj, "new_session") as mock_reset:
            cli_obj._handle_tools_command("/tools enable web")
        mock_reset.assert_called_once()
        assert "web" in cli_obj.enabled_toolsets

    def test_enable_missing_name_prints_usage(self, capsys):
        cli_obj = _make_cli()
        cli_obj._handle_tools_command("/tools enable")
        out = capsys.readouterr().out
        assert "Usage" in out

```

## File: test_personality_none.py
```
"""Tests for /personality none — clearing personality overlay."""
import pytest
from unittest.mock import MagicMock, patch, mock_open
import yaml


# ── CLI tests ──────────────────────────────────────────────────────────────

class TestCLIPersonalityNone:

    def _make_cli(self, personalities=None):
        from cli import HermesCLI
        cli = HermesCLI.__new__(HermesCLI)
        cli.personalities = personalities or {
            "helpful": "You are helpful.",
            "concise": "You are concise.",
        }
        cli.system_prompt = "You are kawaii~"
        cli.agent = MagicMock()
        cli.console = MagicMock()
        return cli

    def test_none_clears_system_prompt(self):
        cli = self._make_cli()
        with patch("cli.save_config_value", return_value=True):
            cli._handle_personality_command("/personality none")
        assert cli.system_prompt == ""

    def test_default_clears_system_prompt(self):
        cli = self._make_cli()
        with patch("cli.save_config_value", return_value=True):
            cli._handle_personality_command("/personality default")
        assert cli.system_prompt == ""

    def test_neutral_clears_system_prompt(self):
        cli = self._make_cli()
        with patch("cli.save_config_value", return_value=True):
            cli._handle_personality_command("/personality neutral")
        assert cli.system_prompt == ""

    def test_none_forces_agent_reinit(self):
        cli = self._make_cli()
        with patch("cli.save_config_value", return_value=True):
            cli._handle_personality_command("/personality none")
        assert cli.agent is None

    def test_none_saves_to_config(self):
        cli = self._make_cli()
        with patch("cli.save_config_value", return_value=True) as mock_save:
            cli._handle_personality_command("/personality none")
        mock_save.assert_called_once_with("agent.system_prompt", "")

    def test_known_personality_still_works(self):
        cli = self._make_cli()
        with patch("cli.save_config_value", return_value=True):
            cli._handle_personality_command("/personality helpful")
        assert cli.system_prompt == "You are helpful."

    def test_unknown_personality_shows_none_in_available(self, capsys):
        cli = self._make_cli()
        cli._handle_personality_command("/personality nonexistent")
        output = capsys.readouterr().out
        assert "none" in output.lower()

    def test_list_shows_none_option(self):
        cli = self._make_cli()
        with patch("builtins.print") as mock_print:
            cli._handle_personality_command("/personality")
        output = " ".join(str(c) for c in mock_print.call_args_list)
        assert "none" in output.lower()


# ── Gateway tests ──────────────────────────────────────────────────────────

class TestGatewayPersonalityNone:

    def _make_event(self, args=""):
        event = MagicMock()
        event.get_command.return_value = "personality"
        event.get_command_args.return_value = args
        return event

    def _make_runner(self, personalities=None):
        from gateway.run import GatewayRunner
        runner = GatewayRunner.__new__(GatewayRunner)
        runner._ephemeral_system_prompt = "You are kawaii~"
        runner.config = {
            "agent": {
                "personalities": personalities or {"helpful": "You are helpful."}
            }
        }
        return runner

    @pytest.mark.asyncio
    async def test_none_clears_ephemeral_prompt(self, tmp_path):
        runner = self._make_runner()
        config_data = {"agent": {"personalities": {"helpful": "You are helpful."}, "system_prompt": "kawaii"}}
        config_file = tmp_path / "config.yaml"
        config_file.write_text(yaml.dump(config_data))

        with patch("gateway.run._hermes_home", tmp_path):
            event = self._make_event("none")
            result = await runner._handle_personality_command(event)

        assert runner._ephemeral_system_prompt == ""
        assert "cleared" in result.lower()

    @pytest.mark.asyncio
    async def test_default_clears_ephemeral_prompt(self, tmp_path):
        runner = self._make_runner()
        config_data = {"agent": {"personalities": {"helpful": "You are helpful."}}}
        config_file = tmp_path / "config.yaml"
        config_file.write_text(yaml.dump(config_data))

        with patch("gateway.run._hermes_home", tmp_path):
            event = self._make_event("default")
            result = await runner._handle_personality_command(event)

        assert runner._ephemeral_system_prompt == ""

    @pytest.mark.asyncio
    async def test_list_includes_none(self, tmp_path):
        runner = self._make_runner()
        config_data = {"agent": {"personalities": {"helpful": "You are helpful."}}}
        config_file = tmp_path / "config.yaml"
        config_file.write_text(yaml.dump(config_data))

        with patch("gateway.run._hermes_home", tmp_path):
            event = self._make_event("")
            result = await runner._handle_personality_command(event)

        assert "none" in result.lower()

    @pytest.mark.asyncio
    async def test_unknown_shows_none_in_available(self, tmp_path):
        runner = self._make_runner()
        config_data = {"agent": {"personalities": {"helpful": "You are helpful."}}}
        config_file = tmp_path / "config.yaml"
        config_file.write_text(yaml.dump(config_data))

        with patch("gateway.run._hermes_home", tmp_path):
            event = self._make_event("nonexistent")
            result = await runner._handle_personality_command(event)

        assert "none" in result.lower()


class TestPersonalityDictFormat:
    """Test dict-format custom personalities with description, tone, style."""

    def _make_cli(self, personalities):
        from cli import HermesCLI
        cli = HermesCLI.__new__(HermesCLI)
        cli.personalities = personalities
        cli.system_prompt = ""
        cli.agent = None
        cli.console = MagicMock()
        return cli

    def test_dict_personality_uses_system_prompt(self):
        cli = self._make_cli({
            "coder": {
                "description": "Expert programmer",
                "system_prompt": "You are an expert programmer.",
                "tone": "technical",
                "style": "concise",
            }
        })
        with patch("cli.save_config_value", return_value=True):
            cli._handle_personality_command("/personality coder")
        assert "You are an expert programmer." in cli.system_prompt

    def test_dict_personality_includes_tone(self):
        cli = self._make_cli({
            "coder": {
                "system_prompt": "You are an expert programmer.",
                "tone": "technical and precise",
            }
        })
        with patch("cli.save_config_value", return_value=True):
            cli._handle_personality_command("/personality coder")
        assert "Tone: technical and precise" in cli.system_prompt

    def test_dict_personality_includes_style(self):
        cli = self._make_cli({
            "coder": {
                "system_prompt": "You are an expert programmer.",
                "style": "use code examples",
            }
        })
        with patch("cli.save_config_value", return_value=True):
            cli._handle_personality_command("/personality coder")
        assert "Style: use code examples" in cli.system_prompt

    def test_string_personality_still_works(self):
        cli = self._make_cli({"helper": "You are helpful."})
        with patch("cli.save_config_value", return_value=True):
            cli._handle_personality_command("/personality helper")
        assert cli.system_prompt == "You are helpful."

    def test_resolve_prompt_dict_no_tone_no_style(self):
        from cli import HermesCLI
        result = HermesCLI._resolve_personality_prompt({
            "description": "A helper",
            "system_prompt": "You are helpful.",
        })
        assert result == "You are helpful."

    def test_resolve_prompt_string(self):
        from cli import HermesCLI
        result = HermesCLI._resolve_personality_prompt("You are helpful.")
        assert result == "You are helpful."

```

## File: test_quick_commands.py
```
"""Tests for user-defined quick commands that bypass the agent loop."""
import subprocess
from unittest.mock import MagicMock, patch, AsyncMock
from rich.text import Text
import pytest


# ── CLI tests ──────────────────────────────────────────────────────────────

class TestCLIQuickCommands:
    """Test quick command dispatch in HermesCLI.process_command."""

    @staticmethod
    def _printed_plain(call_arg):
        if isinstance(call_arg, Text):
            return call_arg.plain
        return str(call_arg)

    def _make_cli(self, quick_commands):
        from cli import HermesCLI
        cli = HermesCLI.__new__(HermesCLI)
        cli.config = {"quick_commands": quick_commands}
        cli.console = MagicMock()
        cli.agent = None
        cli.conversation_history = []
        return cli

    def test_exec_command_runs_and_prints_output(self):
        cli = self._make_cli({"dn": {"type": "exec", "command": "echo daily-note"}})
        result = cli.process_command("/dn")
        assert result is True
        cli.console.print.assert_called_once()
        printed = self._printed_plain(cli.console.print.call_args[0][0])
        assert printed == "daily-note"

    def test_exec_command_stderr_shown_on_no_stdout(self):
        cli = self._make_cli({"err": {"type": "exec", "command": "echo error >&2"}})
        result = cli.process_command("/err")
        assert result is True
        # stderr fallback — should print something
        cli.console.print.assert_called_once()

    def test_exec_command_no_output_shows_fallback(self):
        cli = self._make_cli({"empty": {"type": "exec", "command": "true"}})
        cli.process_command("/empty")
        cli.console.print.assert_called_once()
        args = cli.console.print.call_args[0][0]
        assert "no output" in args.lower()

    def test_alias_command_routes_to_target(self):
        """Alias quick commands rewrite to the target command."""
        cli = self._make_cli({"shortcut": {"type": "alias", "target": "/help"}})
        with patch.object(cli, "process_command", wraps=cli.process_command) as spy:
            cli.process_command("/shortcut")
            # Should recursively call process_command with /help
            spy.assert_any_call("/help")

    def test_alias_command_passes_args(self):
        """Alias quick commands forward user arguments to the target."""
        cli = self._make_cli({"sc": {"type": "alias", "target": "/context"}})
        with patch.object(cli, "process_command", wraps=cli.process_command) as spy:
            cli.process_command("/sc some args")
            spy.assert_any_call("/context some args")

    def test_alias_no_target_shows_error(self):
        cli = self._make_cli({"broken": {"type": "alias", "target": ""}})
        cli.process_command("/broken")
        cli.console.print.assert_called_once()
        args = cli.console.print.call_args[0][0]
        assert "no target defined" in args.lower()

    def test_unsupported_type_shows_error(self):
        cli = self._make_cli({"bad": {"type": "prompt", "command": "echo hi"}})
        cli.process_command("/bad")
        cli.console.print.assert_called_once()
        args = cli.console.print.call_args[0][0]
        assert "unsupported type" in args.lower()

    def test_missing_command_field_shows_error(self):
        cli = self._make_cli({"oops": {"type": "exec"}})
        cli.process_command("/oops")
        cli.console.print.assert_called_once()
        args = cli.console.print.call_args[0][0]
        assert "no command defined" in args.lower()

    def test_quick_command_takes_priority_over_skill_commands(self):
        """Quick commands must be checked before skill slash commands."""
        cli = self._make_cli({"mygif": {"type": "exec", "command": "echo overridden"}})
        with patch("cli._skill_commands", {"/mygif": {"name": "gif-search"}}):
            cli.process_command("/mygif")
        cli.console.print.assert_called_once()
        printed = self._printed_plain(cli.console.print.call_args[0][0])
        assert printed == "overridden"

    def test_unknown_command_still_shows_error(self):
        cli = self._make_cli({})
        with patch("cli._cprint") as mock_cprint:
            cli.process_command("/nonexistent")
            mock_cprint.assert_called()
            printed = " ".join(str(c) for c in mock_cprint.call_args_list)
            assert "unknown command" in printed.lower()

    def test_timeout_shows_error(self):
        cli = self._make_cli({"slow": {"type": "exec", "command": "sleep 100"}})
        with patch("subprocess.run", side_effect=subprocess.TimeoutExpired("sleep", 30)):
            cli.process_command("/slow")
        cli.console.print.assert_called_once()
        args = cli.console.print.call_args[0][0]
        assert "timed out" in args.lower()


# ── Gateway tests ──────────────────────────────────────────────────────────

class TestGatewayQuickCommands:
    """Test quick command dispatch in GatewayRunner._handle_message."""

    def _make_event(self, command, args=""):
        event = MagicMock()
        event.get_command.return_value = command
        event.get_command_args.return_value = args
        event.text = f"/{command} {args}".strip()
        event.source = MagicMock()
        event.source.user_id = "test_user"
        event.source.user_name = "Test User"
        event.source.platform.value = "telegram"
        event.source.chat_type = "dm"
        event.source.chat_id = "123"
        return event

    @pytest.mark.asyncio
    async def test_exec_command_returns_output(self):
        from gateway.run import GatewayRunner
        runner = GatewayRunner.__new__(GatewayRunner)
        runner.config = {"quick_commands": {"limits": {"type": "exec", "command": "echo ok"}}}
        runner._running_agents = {}
        runner._pending_messages = {}
        runner._is_user_authorized = MagicMock(return_value=True)

        event = self._make_event("limits")
        result = await runner._handle_message(event)
        assert result == "ok"

    @pytest.mark.asyncio
    async def test_unsupported_type_returns_error(self):
        from gateway.run import GatewayRunner
        runner = GatewayRunner.__new__(GatewayRunner)
        runner.config = {"quick_commands": {"bad": {"type": "prompt", "command": "echo hi"}}}
        runner._running_agents = {}
        runner._pending_messages = {}
        runner._is_user_authorized = MagicMock(return_value=True)

        event = self._make_event("bad")
        result = await runner._handle_message(event)
        assert result is not None
        assert "unsupported type" in result.lower()

    @pytest.mark.asyncio
    async def test_timeout_returns_error(self):
        from gateway.run import GatewayRunner
        import asyncio
        runner = GatewayRunner.__new__(GatewayRunner)
        runner.config = {"quick_commands": {"slow": {"type": "exec", "command": "sleep 100"}}}
        runner._running_agents = {}
        runner._pending_messages = {}
        runner._is_user_authorized = MagicMock(return_value=True)

        event = self._make_event("slow")
        with patch("asyncio.wait_for", side_effect=asyncio.TimeoutError):
            result = await runner._handle_message(event)
        assert result is not None
        assert "timed out" in result.lower()

    @pytest.mark.asyncio
    async def test_gateway_config_object_supports_quick_commands(self):
        from gateway.config import GatewayConfig
        from gateway.run import GatewayRunner

        runner = GatewayRunner.__new__(GatewayRunner)
        runner.config = GatewayConfig(
            quick_commands={"limits": {"type": "exec", "command": "echo ok"}}
        )
        runner._running_agents = {}
        runner._pending_messages = {}
        runner._is_user_authorized = MagicMock(return_value=True)

        event = self._make_event("limits")
        result = await runner._handle_message(event)
        assert result == "ok"

```

## File: test_reasoning_command.py
```
"""Tests for the combined /reasoning command.

Covers both reasoning effort level management and reasoning display toggle,
plus the reasoning extraction and display pipeline from run_agent through CLI.

Combines functionality from:
- PR #789 (Aum08Desai): reasoning effort level management
- PR #790 (0xbyt4): reasoning display toggle and rendering
"""

import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
import re


# ---------------------------------------------------------------------------
# Effort level parsing
# ---------------------------------------------------------------------------

class TestParseReasoningConfig(unittest.TestCase):
    """Verify _parse_reasoning_config handles all effort levels."""

    def _parse(self, effort):
        from cli import _parse_reasoning_config
        return _parse_reasoning_config(effort)

    def test_none_disables(self):
        result = self._parse("none")
        self.assertEqual(result, {"enabled": False})

    def test_valid_levels(self):
        for level in ("low", "medium", "high", "xhigh", "minimal"):
            result = self._parse(level)
            self.assertIsNotNone(result)
            self.assertTrue(result.get("enabled"))
            self.assertEqual(result["effort"], level)

    def test_empty_returns_none(self):
        self.assertIsNone(self._parse(""))
        self.assertIsNone(self._parse("  "))

    def test_unknown_returns_none(self):
        self.assertIsNone(self._parse("ultra"))
        self.assertIsNone(self._parse("turbo"))

    def test_case_insensitive(self):
        result = self._parse("HIGH")
        self.assertIsNotNone(result)
        self.assertEqual(result["effort"], "high")


# ---------------------------------------------------------------------------
# /reasoning command handler (combined effort + display)
# ---------------------------------------------------------------------------

class TestHandleReasoningCommand(unittest.TestCase):
    """Test the combined _handle_reasoning_command method."""

    def _make_cli(self, reasoning_config=None, show_reasoning=False):
        """Create a minimal CLI stub with the reasoning attributes."""
        stub = SimpleNamespace(
            reasoning_config=reasoning_config,
            show_reasoning=show_reasoning,
            agent=MagicMock(),
        )
        return stub

    def test_show_enables_display(self):
        stub = self._make_cli(show_reasoning=False)
        # Simulate /reasoning show
        arg = "show"
        if arg in ("show", "on"):
            stub.show_reasoning = True
            stub.agent.reasoning_callback = lambda x: None
        self.assertTrue(stub.show_reasoning)

    def test_hide_disables_display(self):
        stub = self._make_cli(show_reasoning=True)
        # Simulate /reasoning hide
        arg = "hide"
        if arg in ("hide", "off"):
            stub.show_reasoning = False
            stub.agent.reasoning_callback = None
        self.assertFalse(stub.show_reasoning)
        self.assertIsNone(stub.agent.reasoning_callback)

    def test_on_enables_display(self):
        stub = self._make_cli(show_reasoning=False)
        arg = "on"
        if arg in ("show", "on"):
            stub.show_reasoning = True
        self.assertTrue(stub.show_reasoning)

    def test_off_disables_display(self):
        stub = self._make_cli(show_reasoning=True)
        arg = "off"
        if arg in ("hide", "off"):
            stub.show_reasoning = False
        self.assertFalse(stub.show_reasoning)

    def test_effort_level_sets_config(self):
        """Setting an effort level should update reasoning_config."""
        from cli import _parse_reasoning_config
        stub = self._make_cli()
        arg = "high"
        parsed = _parse_reasoning_config(arg)
        stub.reasoning_config = parsed
        self.assertEqual(stub.reasoning_config, {"enabled": True, "effort": "high"})

    def test_effort_none_disables_reasoning(self):
        from cli import _parse_reasoning_config
        stub = self._make_cli()
        parsed = _parse_reasoning_config("none")
        stub.reasoning_config = parsed
        self.assertEqual(stub.reasoning_config, {"enabled": False})

    def test_invalid_argument_rejected(self):
        """Invalid arguments should be rejected (parsed returns None)."""
        from cli import _parse_reasoning_config
        parsed = _parse_reasoning_config("turbo")
        self.assertIsNone(parsed)

    def test_no_args_shows_status(self):
        """With no args, should show current state (no crash)."""
        stub = self._make_cli(reasoning_config=None, show_reasoning=False)
        rc = stub.reasoning_config
        if rc is None:
            level = "medium (default)"
        elif rc.get("enabled") is False:
            level = "none (disabled)"
        else:
            level = rc.get("effort", "medium")
        display_state = "on" if stub.show_reasoning else "off"
        self.assertEqual(level, "medium (default)")
        self.assertEqual(display_state, "off")

    def test_status_with_disabled_reasoning(self):
        stub = self._make_cli(reasoning_config={"enabled": False}, show_reasoning=True)
        rc = stub.reasoning_config
        if rc is None:
            level = "medium (default)"
        elif rc.get("enabled") is False:
            level = "none (disabled)"
        else:
            level = rc.get("effort", "medium")
        self.assertEqual(level, "none (disabled)")

    def test_status_with_explicit_level(self):
        stub = self._make_cli(
            reasoning_config={"enabled": True, "effort": "xhigh"},
            show_reasoning=True,
        )
        rc = stub.reasoning_config
        level = rc.get("effort", "medium")
        self.assertEqual(level, "xhigh")


# ---------------------------------------------------------------------------
# Reasoning extraction and result dict
# ---------------------------------------------------------------------------

class TestLastReasoningInResult(unittest.TestCase):
    """Verify reasoning extraction from the messages list."""

    def _build_messages(self, reasoning=None):
        return [
            {"role": "user", "content": "hello"},
            {
                "role": "assistant",
                "content": "Hi there!",
                "reasoning": reasoning,
                "finish_reason": "stop",
            },
        ]

    def test_reasoning_present(self):
        messages = self._build_messages(reasoning="Let me think...")
        last_reasoning = None
        for msg in reversed(messages):
            if msg.get("role") == "assistant" and msg.get("reasoning"):
                last_reasoning = msg["reasoning"]
                break
        self.assertEqual(last_reasoning, "Let me think...")

    def test_reasoning_none(self):
        messages = self._build_messages(reasoning=None)
        last_reasoning = None
        for msg in reversed(messages):
            if msg.get("role") == "assistant" and msg.get("reasoning"):
                last_reasoning = msg["reasoning"]
                break
        self.assertIsNone(last_reasoning)

    def test_picks_last_assistant(self):
        messages = [
            {"role": "user", "content": "hello"},
            {"role": "assistant", "content": "...", "reasoning": "first thought"},
            {"role": "tool", "content": "result"},
            {"role": "assistant", "content": "done!", "reasoning": "final thought"},
        ]
        last_reasoning = None
        for msg in reversed(messages):
            if msg.get("role") == "assistant" and msg.get("reasoning"):
                last_reasoning = msg["reasoning"]
                break
        self.assertEqual(last_reasoning, "final thought")

    def test_empty_reasoning_treated_as_none(self):
        messages = self._build_messages(reasoning="")
        last_reasoning = None
        for msg in reversed(messages):
            if msg.get("role") == "assistant" and msg.get("reasoning"):
                last_reasoning = msg["reasoning"]
                break
        self.assertIsNone(last_reasoning)


# ---------------------------------------------------------------------------
# Reasoning display collapse
# ---------------------------------------------------------------------------

class TestReasoningCollapse(unittest.TestCase):
    """Verify long reasoning is collapsed to 10 lines in the box."""

    def test_short_reasoning_not_collapsed(self):
        reasoning = "\n".join(f"Line {i}" for i in range(5))
        lines = reasoning.strip().splitlines()
        self.assertLessEqual(len(lines), 10)

    def test_long_reasoning_collapsed(self):
        reasoning = "\n".join(f"Line {i}" for i in range(25))
        lines = reasoning.strip().splitlines()
        self.assertTrue(len(lines) > 10)
        if len(lines) > 10:
            display = "\n".join(lines[:10])
            display += f"\n  ... ({len(lines) - 10} more lines)"
        display_lines = display.splitlines()
        self.assertEqual(len(display_lines), 11)
        self.assertIn("15 more lines", display_lines[-1])

    def test_exactly_10_lines_not_collapsed(self):
        reasoning = "\n".join(f"Line {i}" for i in range(10))
        lines = reasoning.strip().splitlines()
        self.assertEqual(len(lines), 10)
        self.assertFalse(len(lines) > 10)

    def test_intermediate_callback_collapses_to_5(self):
        """_on_reasoning shows max 5 lines."""
        reasoning = "\n".join(f"Step {i}" for i in range(12))
        lines = reasoning.strip().splitlines()
        if len(lines) > 5:
            preview = "\n".join(lines[:5])
            preview += f"\n  ... ({len(lines) - 5} more lines)"
        else:
            preview = reasoning.strip()
        preview_lines = preview.splitlines()
        self.assertEqual(len(preview_lines), 6)
        self.assertIn("7 more lines", preview_lines[-1])


# ---------------------------------------------------------------------------
# Reasoning callback
# ---------------------------------------------------------------------------

class TestReasoningCallback(unittest.TestCase):
    """Verify reasoning_callback invocation."""

    def test_callback_invoked_with_reasoning(self):
        captured = []
        agent = MagicMock()
        agent.reasoning_callback = lambda t: captured.append(t)
        agent._extract_reasoning = MagicMock(return_value="deep thought")

        reasoning_text = agent._extract_reasoning(MagicMock())
        if reasoning_text and agent.reasoning_callback:
            agent.reasoning_callback(reasoning_text)
        self.assertEqual(captured, ["deep thought"])

    def test_callback_not_invoked_without_reasoning(self):
        captured = []
        agent = MagicMock()
        agent.reasoning_callback = lambda t: captured.append(t)
        agent._extract_reasoning = MagicMock(return_value=None)

        reasoning_text = agent._extract_reasoning(MagicMock())
        if reasoning_text and agent.reasoning_callback:
            agent.reasoning_callback(reasoning_text)
        self.assertEqual(captured, [])

    def test_callback_none_does_not_crash(self):
        reasoning_text = "some thought"
        callback = None
        if reasoning_text and callback:
            callback(reasoning_text)
        # No exception = pass


class TestReasoningPreviewBuffering(unittest.TestCase):
    def _make_cli(self):
        from cli import HermesCLI

        cli = HermesCLI.__new__(HermesCLI)
        cli.verbose = True
        cli._spinner_text = ""
        cli._reasoning_preview_buf = ""
        cli._invalidate = lambda *args, **kwargs: None
        return cli

    @patch("cli._cprint")
    def test_streamed_reasoning_chunks_wait_for_boundary(self, mock_cprint):
        cli = self._make_cli()

        cli._on_reasoning("Let")
        cli._on_reasoning(" me")
        cli._on_reasoning(" think")

        self.assertEqual(mock_cprint.call_count, 0)

        cli._on_reasoning(" about this.\n")

        self.assertEqual(mock_cprint.call_count, 1)
        rendered = mock_cprint.call_args[0][0]
        self.assertIn("[thinking] Let me think about this.", rendered)

    @patch("cli._cprint")
    def test_pending_reasoning_flushes_when_thinking_stops(self, mock_cprint):
        cli = self._make_cli()

        cli._on_reasoning("see")
        cli._on_reasoning(" how")
        cli._on_reasoning(" this")
        cli._on_reasoning(" plays")
        cli._on_reasoning(" out")

        self.assertEqual(mock_cprint.call_count, 0)

        cli._on_thinking("")

        self.assertEqual(mock_cprint.call_count, 1)
        rendered = mock_cprint.call_args[0][0]
        self.assertIn("[thinking] see how this plays out", rendered)

    @patch("cli._cprint")
    @patch("cli.shutil.get_terminal_size", return_value=SimpleNamespace(columns=50))
    def test_reasoning_preview_compacts_newlines_and_wraps_to_terminal(self, _mock_term, mock_cprint):
        cli = self._make_cli()

        cli._emit_reasoning_preview(
            "First line\nstill same thought\n\n\nSecond paragraph with more detail here."
        )

        rendered = mock_cprint.call_args[0][0]
        plain = re.sub(r"\x1b\[[0-9;]*m", "", rendered)
        normalized = " ".join(plain.split())
        self.assertIn("[thinking] First line still same thought", plain)
        self.assertIn("Second paragraph with more detail here.", normalized)
        self.assertNotIn("\n\n\n", plain)

    @patch("cli.shutil.get_terminal_size", return_value=SimpleNamespace(columns=60))
    def test_reasoning_flush_threshold_tracks_terminal_width(self, _mock_term):
        cli = self._make_cli()

        cli._reasoning_preview_buf = "a" * 30
        cli._flush_reasoning_preview(force=False)
        self.assertEqual(cli._reasoning_preview_buf, "a" * 30)


class TestReasoningDisplayModeSelection(unittest.TestCase):
    def _make_cli(self, *, show_reasoning=False, streaming_enabled=False, verbose=False):
        from cli import HermesCLI

        cli = HermesCLI.__new__(HermesCLI)
        cli.show_reasoning = show_reasoning
        cli.streaming_enabled = streaming_enabled
        cli.verbose = verbose
        cli._stream_reasoning_delta = lambda text: ("stream", text)
        cli._on_reasoning = lambda text: ("preview", text)
        return cli

    def test_show_reasoning_non_streaming_uses_final_box_only(self):
        cli = self._make_cli(show_reasoning=True, streaming_enabled=False, verbose=False)

        self.assertIsNone(cli._current_reasoning_callback())

    def test_show_reasoning_streaming_uses_live_reasoning_box(self):
        cli = self._make_cli(show_reasoning=True, streaming_enabled=True, verbose=False)

        callback = cli._current_reasoning_callback()
        self.assertIsNotNone(callback)
        self.assertEqual(callback("x"), ("stream", "x"))

    def test_verbose_without_show_reasoning_uses_preview_callback(self):
        cli = self._make_cli(show_reasoning=False, streaming_enabled=False, verbose=True)

        callback = cli._current_reasoning_callback()
        self.assertIsNotNone(callback)
        self.assertEqual(callback("x"), ("preview", "x"))


# ---------------------------------------------------------------------------
# Real provider format extraction
# ---------------------------------------------------------------------------

class TestExtractReasoningFormats(unittest.TestCase):
    """Test _extract_reasoning with real provider response formats."""

    def _get_extractor(self):
        from run_agent import AIAgent
        return AIAgent._extract_reasoning

    def test_openrouter_reasoning_details(self):
        extract = self._get_extractor()
        msg = SimpleNamespace(
            reasoning=None,
            reasoning_content=None,
            reasoning_details=[
                {"type": "reasoning.summary", "summary": "Analyzing Python lists."},
            ],
        )
        result = extract(None, msg)
        self.assertIn("Python lists", result)

    def test_deepseek_reasoning_field(self):
        extract = self._get_extractor()
        msg = SimpleNamespace(
            reasoning="Solving step by step.\nx + y = 8.",
            reasoning_content=None,
        )
        result = extract(None, msg)
        self.assertIn("x + y = 8", result)

    def test_moonshot_reasoning_content(self):
        extract = self._get_extractor()
        msg = SimpleNamespace(
            reasoning_content="Explaining async/await.",
        )
        result = extract(None, msg)
        self.assertIn("async/await", result)

    def test_no_reasoning_returns_none(self):
        extract = self._get_extractor()
        msg = SimpleNamespace(content="Hello!")
        result = extract(None, msg)
        self.assertIsNone(result)


# ---------------------------------------------------------------------------
# Inline <think> block extraction fallback
# ---------------------------------------------------------------------------

class TestInlineThinkBlockExtraction(unittest.TestCase):
    """Test _build_assistant_message extracts inline <think> blocks as reasoning
    when no structured API-level reasoning fields are present."""

    def _build_msg(self, content, reasoning=None, reasoning_content=None, reasoning_details=None, tool_calls=None):
        """Create a mock API response message."""
        msg = SimpleNamespace(content=content, tool_calls=tool_calls)
        if reasoning is not None:
            msg.reasoning = reasoning
        if reasoning_content is not None:
            msg.reasoning_content = reasoning_content
        if reasoning_details is not None:
            msg.reasoning_details = reasoning_details
        return msg

    def _make_agent(self):
        """Create a minimal agent with _build_assistant_message."""
        from run_agent import AIAgent
        agent = MagicMock(spec=AIAgent)
        agent._build_assistant_message = AIAgent._build_assistant_message.__get__(agent)
        agent._extract_reasoning = AIAgent._extract_reasoning.__get__(agent)
        agent.verbose_logging = False
        agent.reasoning_callback = None
        agent.stream_delta_callback = None  # non-streaming by default
        return agent

    def test_single_think_block_extracted(self):
        agent = self._make_agent()
        api_msg = self._build_msg("<think>Let me calculate 2+2=4.</think>The answer is 4.")
        result = agent._build_assistant_message(api_msg, "stop")
        self.assertEqual(result["reasoning"], "Let me calculate 2+2=4.")

    def test_multiple_think_blocks_extracted(self):
        agent = self._make_agent()
        api_msg = self._build_msg("<think>First thought.</think>Some text<think>Second thought.</think>More text")
        result = agent._build_assistant_message(api_msg, "stop")
        self.assertIn("First thought.", result["reasoning"])
        self.assertIn("Second thought.", result["reasoning"])

    def test_no_think_blocks_no_reasoning(self):
        agent = self._make_agent()
        api_msg = self._build_msg("Just a plain response.")
        result = agent._build_assistant_message(api_msg, "stop")
        # No structured reasoning AND no inline think blocks → None
        self.assertIsNone(result["reasoning"])

    def test_structured_reasoning_takes_priority(self):
        """When structured API reasoning exists, inline think blocks should NOT override."""
        agent = self._make_agent()
        api_msg = self._build_msg(
            "<think>Inline thought.</think>Response text.",
            reasoning="Structured reasoning from API.",
        )
        result = agent._build_assistant_message(api_msg, "stop")
        self.assertEqual(result["reasoning"], "Structured reasoning from API.")

    def test_empty_think_block_ignored(self):
        agent = self._make_agent()
        api_msg = self._build_msg("<think></think>Hello!")
        result = agent._build_assistant_message(api_msg, "stop")
        # Empty think block should not produce reasoning
        self.assertIsNone(result["reasoning"])

    def test_multiline_think_block(self):
        agent = self._make_agent()
        api_msg = self._build_msg("<think>\nStep 1: Analyze.\nStep 2: Solve.\n</think>Done.")
        result = agent._build_assistant_message(api_msg, "stop")
        self.assertIn("Step 1: Analyze.", result["reasoning"])
        self.assertIn("Step 2: Solve.", result["reasoning"])

    def test_callback_fires_for_inline_think(self):
        """Reasoning callback should fire when reasoning is extracted from inline think blocks."""
        agent = self._make_agent()
        captured = []
        agent.reasoning_callback = lambda t: captured.append(t)
        api_msg = self._build_msg("<think>Deep analysis here.</think>Answer.")
        agent._build_assistant_message(api_msg, "stop")
        self.assertEqual(len(captured), 1)
        self.assertIn("Deep analysis", captured[0])


# ---------------------------------------------------------------------------
# Config defaults
# ---------------------------------------------------------------------------

class TestConfigDefault(unittest.TestCase):
    """Verify config default for show_reasoning."""

    def test_default_config_has_show_reasoning(self):
        from hermes_cli.config import DEFAULT_CONFIG
        display = DEFAULT_CONFIG.get("display", {})
        self.assertIn("show_reasoning", display)
        self.assertFalse(display["show_reasoning"])


class TestCommandRegistered(unittest.TestCase):
    """Verify /reasoning is in the COMMANDS dict."""

    def test_reasoning_in_commands(self):
        from hermes_cli.commands import COMMANDS
        self.assertIn("/reasoning", COMMANDS)


# ---------------------------------------------------------------------------
# End-to-end pipeline
# ---------------------------------------------------------------------------

class TestEndToEndPipeline(unittest.TestCase):
    """Simulate the full pipeline: extraction -> result dict -> display."""

    def test_openrouter_claude_pipeline(self):
        from run_agent import AIAgent

        api_message = SimpleNamespace(
            role="assistant",
            content="Lists support append().",
            tool_calls=None,
            reasoning=None,
            reasoning_content=None,
            reasoning_details=[
                {"type": "reasoning.summary", "summary": "Python list methods."},
            ],
        )

        reasoning = AIAgent._extract_reasoning(None, api_message)
        self.assertIsNotNone(reasoning)

        messages = [
            {"role": "user", "content": "How do I add items?"},
            {"role": "assistant", "content": api_message.content, "reasoning": reasoning},
        ]

        last_reasoning = None
        for msg in reversed(messages):
            if msg.get("role") == "assistant" and msg.get("reasoning"):
                last_reasoning = msg["reasoning"]
                break

        result = {
            "final_response": api_message.content,
            "last_reasoning": last_reasoning,
        }

        self.assertIn("last_reasoning", result)
        self.assertIn("Python list methods", result["last_reasoning"])

    def test_no_reasoning_model_pipeline(self):
        from run_agent import AIAgent

        api_message = SimpleNamespace(content="Paris.", tool_calls=None)
        reasoning = AIAgent._extract_reasoning(None, api_message)
        self.assertIsNone(reasoning)

        result = {"final_response": api_message.content, "last_reasoning": reasoning}
        self.assertIsNone(result["last_reasoning"])


# ---------------------------------------------------------------------------
# Duplicate reasoning box prevention (Bug fix: 3 boxes for 1 reasoning)
# ---------------------------------------------------------------------------

class TestReasoningDeltasFiredFlag(unittest.TestCase):
    """_build_assistant_message should not re-fire reasoning_callback when
    reasoning was already streamed via _fire_reasoning_delta."""

    def _make_agent(self):
        from run_agent import AIAgent
        agent = AIAgent.__new__(AIAgent)
        agent.reasoning_callback = None
        agent.stream_delta_callback = None
        agent._reasoning_deltas_fired = False
        agent.verbose_logging = False
        return agent

    def test_fire_reasoning_delta_sets_flag(self):
        agent = self._make_agent()
        captured = []
        agent.reasoning_callback = lambda t: captured.append(t)
        self.assertFalse(agent._reasoning_deltas_fired)
        agent._fire_reasoning_delta("thinking...")
        self.assertTrue(agent._reasoning_deltas_fired)
        self.assertEqual(captured, ["thinking..."])

    def test_build_assistant_message_skips_callback_when_already_streamed(self):
        """When streaming already fired reasoning deltas, the post-stream
        _build_assistant_message should NOT re-fire the callback."""
        agent = self._make_agent()
        captured = []
        agent.reasoning_callback = lambda t: captured.append(t)
        agent.stream_delta_callback = lambda t: None  # streaming is active

        # Simulate streaming having fired reasoning
        agent._reasoning_deltas_fired = True

        msg = SimpleNamespace(
            content="I'll merge that.",
            tool_calls=None,
            reasoning_content="Let me merge the PR.",
            reasoning=None,
            reasoning_details=None,
        )
        agent._build_assistant_message(msg, "stop")

        # Callback should NOT have been fired again
        self.assertEqual(captured, [])

    def test_build_assistant_message_skips_callback_when_streaming_active(self):
        """When streaming is active, callback should NEVER fire from
        _build_assistant_message — reasoning was already displayed during the
        stream (either via reasoning_content deltas or content tag extraction).
        Any missed reasoning is caught by the CLI post-response fallback."""
        agent = self._make_agent()
        captured = []
        agent.reasoning_callback = lambda t: captured.append(t)
        agent.stream_delta_callback = lambda t: None  # streaming active

        # Even though _reasoning_deltas_fired is False (reasoning came through
        # content tags, not reasoning_content deltas), callback should not fire
        agent._reasoning_deltas_fired = False

        msg = SimpleNamespace(
            content="I'll merge that.",
            tool_calls=None,
            reasoning_content="Let me merge the PR.",
            reasoning=None,
            reasoning_details=None,
        )
        agent._build_assistant_message(msg, "stop")

        # Callback should NOT fire — streaming is active
        self.assertEqual(captured, [])

    def test_build_assistant_message_fires_callback_without_streaming(self):
        """When no streaming is active, callback always fires for structured
        reasoning."""
        agent = self._make_agent()
        captured = []
        agent.reasoning_callback = lambda t: captured.append(t)
        # No streaming
        agent.stream_delta_callback = None
        agent._reasoning_deltas_fired = False

        msg = SimpleNamespace(
            content="I'll merge that.",
            tool_calls=None,
            reasoning_content="Let me merge the PR.",
            reasoning=None,
            reasoning_details=None,
        )
        agent._build_assistant_message(msg, "stop")

        self.assertEqual(captured, ["Let me merge the PR."])


class TestReasoningShownThisTurnFlag(unittest.TestCase):
    """Post-response reasoning display should be suppressed when reasoning
    was already shown during streaming in a tool-calling loop."""

    def _make_cli(self):
        from cli import HermesCLI
        cli = HermesCLI.__new__(HermesCLI)
        cli.show_reasoning = True
        cli.streaming_enabled = True
        cli._stream_box_opened = False
        cli._reasoning_box_opened = False
        cli._reasoning_stream_started = False
        cli._reasoning_shown_this_turn = False
        cli._reasoning_buf = ""
        cli._stream_buf = ""
        cli._stream_started = False
        cli._stream_text_ansi = ""
        cli._stream_prefilt = ""
        cli._in_reasoning_block = False
        cli._reasoning_preview_buf = ""
        return cli

    @patch("cli._cprint")
    def test_streaming_reasoning_sets_turn_flag(self, mock_cprint):
        cli = self._make_cli()
        self.assertFalse(cli._reasoning_shown_this_turn)
        cli._stream_reasoning_delta("Thinking about it...")
        self.assertTrue(cli._reasoning_shown_this_turn)

    @patch("cli._cprint")
    def test_turn_flag_survives_reset_stream_state(self, mock_cprint):
        """_reasoning_shown_this_turn must NOT be cleared by
        _reset_stream_state (called at intermediate turn boundaries)."""
        cli = self._make_cli()
        cli._stream_reasoning_delta("Thinking...")
        self.assertTrue(cli._reasoning_shown_this_turn)

        # Simulate intermediate turn boundary (tool call)
        cli._reset_stream_state()

        # Flag must persist
        self.assertTrue(cli._reasoning_shown_this_turn)

    @patch("cli._cprint")
    def test_turn_flag_cleared_before_new_turn(self, mock_cprint):
        """The turn flag should be reset at the start of a new user turn.
        This happens outside _reset_stream_state, at the call site."""
        cli = self._make_cli()
        cli._reasoning_shown_this_turn = True

        # Simulate new user turn setup
        cli._reset_stream_state()
        cli._reasoning_shown_this_turn = False  # done by process_input

        self.assertFalse(cli._reasoning_shown_this_turn)


if __name__ == "__main__":
    unittest.main()

```

## File: test_resume_display.py
```
"""Tests for session resume history display — _display_resumed_history() and
_preload_resumed_session().

Verifies that resuming a session shows a compact recap of the previous
conversation with correct formatting, truncation, and config behavior.
"""

import os
import sys
from io import StringIO
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def _make_cli(config_overrides=None, env_overrides=None, **kwargs):
    """Create a HermesCLI instance with minimal mocking."""
    import cli as _cli_mod
    from cli import HermesCLI

    _clean_config = {
        "model": {
            "default": "anthropic/claude-opus-4.6",
            "base_url": "https://openrouter.ai/api/v1",
            "provider": "auto",
        },
        "display": {"compact": False, "tool_progress": "all", "resume_display": "full"},
        "agent": {},
        "terminal": {"env_type": "local"},
    }
    if config_overrides:
        for k, v in config_overrides.items():
            if isinstance(v, dict) and k in _clean_config and isinstance(_clean_config[k], dict):
                _clean_config[k].update(v)
            else:
                _clean_config[k] = v

    clean_env = {"LLM_MODEL": "", "HERMES_MAX_ITERATIONS": ""}
    if env_overrides:
        clean_env.update(env_overrides)
    with (
        patch("cli.get_tool_definitions", return_value=[]),
        patch.dict("os.environ", clean_env, clear=False),
        patch.dict(_cli_mod.__dict__, {"CLI_CONFIG": _clean_config}),
    ):
        return HermesCLI(**kwargs)


# ── Sample conversation histories for tests ──────────────────────────


def _simple_history():
    """Two-turn conversation: user → assistant → user → assistant."""
    return [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is Python?"},
        {"role": "assistant", "content": "Python is a high-level programming language."},
        {"role": "user", "content": "How do I install it?"},
        {"role": "assistant", "content": "You can install Python from python.org."},
    ]


def _tool_call_history():
    """Conversation with tool calls and tool results."""
    return [
        {"role": "system", "content": "system prompt"},
        {"role": "user", "content": "Search for Python tutorials"},
        {
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {
                    "id": "call_1",
                    "type": "function",
                    "function": {"name": "web_search", "arguments": '{"query":"python tutorials"}'},
                },
                {
                    "id": "call_2",
                    "type": "function",
                    "function": {"name": "web_extract", "arguments": '{"urls":["https://example.com"]}'},
                },
            ],
        },
        {"role": "tool", "tool_call_id": "call_1", "content": "Found 5 results..."},
        {"role": "tool", "tool_call_id": "call_2", "content": "Page content..."},
        {"role": "assistant", "content": "Here are some great Python tutorials I found."},
    ]


def _large_history(n_exchanges=15):
    """Build a history with many exchanges to test truncation."""
    msgs = [{"role": "system", "content": "system prompt"}]
    for i in range(n_exchanges):
        msgs.append({"role": "user", "content": f"Question #{i + 1}: What is item {i + 1}?"})
        msgs.append({"role": "assistant", "content": f"Answer #{i + 1}: Item {i + 1} is great."})
    return msgs


def _multimodal_history():
    """Conversation with multimodal (image) content."""
    return [
        {"role": "system", "content": "system prompt"},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {"type": "image_url", "image_url": {"url": "https://example.com/cat.jpg"}},
            ],
        },
        {"role": "assistant", "content": "I see a cat in the image."},
    ]


# ── Tests for _display_resumed_history ───────────────────────────────


class TestDisplayResumedHistory:
    """_display_resumed_history() renders a Rich panel with conversation recap."""

    def _capture_display(self, cli_obj):
        """Run _display_resumed_history and capture the Rich console output."""
        buf = StringIO()
        cli_obj.console.file = buf
        cli_obj._display_resumed_history()
        return buf.getvalue()

    def test_simple_history_shows_user_and_assistant(self):
        cli = _make_cli()
        cli.conversation_history = _simple_history()
        output = self._capture_display(cli)

        assert "You:" in output
        assert "Hermes:" in output
        assert "What is Python?" in output
        assert "Python is a high-level programming language." in output
        assert "How do I install it?" in output

    def test_system_messages_hidden(self):
        cli = _make_cli()
        cli.conversation_history = _simple_history()
        output = self._capture_display(cli)

        assert "You are a helpful assistant" not in output

    def test_tool_messages_hidden(self):
        cli = _make_cli()
        cli.conversation_history = _tool_call_history()
        output = self._capture_display(cli)

        # Tool result content should NOT appear
        assert "Found 5 results" not in output
        assert "Page content" not in output

    def test_tool_calls_shown_as_summary(self):
        cli = _make_cli()
        cli.conversation_history = _tool_call_history()
        output = self._capture_display(cli)

        assert "2 tool calls" in output
        assert "web_search" in output
        assert "web_extract" in output

    def test_long_user_message_truncated(self):
        cli = _make_cli()
        long_text = "A" * 500
        cli.conversation_history = [
            {"role": "user", "content": long_text},
            {"role": "assistant", "content": "OK."},
        ]
        output = self._capture_display(cli)

        # Should have truncation indicator and NOT contain the full 500 chars
        assert "..." in output
        assert "A" * 500 not in output
        # The 300-char truncated text is present but may be line-wrapped by
        # Rich's panel renderer, so check the total A count in the output
        a_count = output.count("A")
        assert 200 <= a_count <= 310  # roughly 300 chars (±panel padding)

    def test_long_assistant_message_truncated(self):
        cli = _make_cli()
        long_text = "B" * 400
        cli.conversation_history = [
            {"role": "user", "content": "Tell me a lot."},
            {"role": "assistant", "content": long_text},
        ]
        output = self._capture_display(cli)

        assert "..." in output
        assert "B" * 400 not in output

    def test_multiline_assistant_truncated(self):
        cli = _make_cli()
        multi = "\n".join([f"Line {i}" for i in range(20)])
        cli.conversation_history = [
            {"role": "user", "content": "Show me lines."},
            {"role": "assistant", "content": multi},
        ]
        output = self._capture_display(cli)

        # First 3 lines should be there
        assert "Line 0" in output
        assert "Line 1" in output
        assert "Line 2" in output
        # Line 19 should NOT be there (truncated after 3 lines)
        assert "Line 19" not in output

    def test_large_history_shows_truncation_indicator(self):
        cli = _make_cli()
        cli.conversation_history = _large_history(n_exchanges=15)
        output = self._capture_display(cli)

        # Should show "earlier messages" indicator
        assert "earlier messages" in output
        # Last question should still be visible
        assert "Question #15" in output

    def test_multimodal_content_handled(self):
        cli = _make_cli()
        cli.conversation_history = _multimodal_history()
        output = self._capture_display(cli)

        assert "What's in this image?" in output
        assert "[image]" in output

    def test_empty_history_no_output(self):
        cli = _make_cli()
        cli.conversation_history = []
        output = self._capture_display(cli)

        assert output.strip() == ""

    def test_minimal_config_suppresses_display(self):
        cli = _make_cli(config_overrides={"display": {"resume_display": "minimal"}})
        # resume_display is captured as an instance variable during __init__
        assert cli.resume_display == "minimal"
        cli.conversation_history = _simple_history()
        output = self._capture_display(cli)

        assert output.strip() == ""

    def test_panel_has_title(self):
        cli = _make_cli()
        cli.conversation_history = _simple_history()
        output = self._capture_display(cli)

        assert "Previous Conversation" in output

    def test_assistant_with_no_content_no_tools_skipped(self):
        """Assistant messages with no visible output (e.g. pure reasoning)
        are skipped in the recap."""
        cli = _make_cli()
        cli.conversation_history = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": None},
        ]
        output = self._capture_display(cli)

        # The assistant entry should be skipped, only the user message shown
        assert "You:" in output
        assert "Hermes:" not in output

    def test_only_system_messages_no_output(self):
        cli = _make_cli()
        cli.conversation_history = [
            {"role": "system", "content": "You are helpful."},
        ]
        output = self._capture_display(cli)

        assert output.strip() == ""

    def test_reasoning_scratchpad_stripped(self):
        """<REASONING_SCRATCHPAD> blocks should be stripped from display."""
        cli = _make_cli()
        cli.conversation_history = [
            {"role": "user", "content": "Think about this"},
            {
                "role": "assistant",
                "content": (
                    "<REASONING_SCRATCHPAD>\nLet me think step by step.\n"
                    "</REASONING_SCRATCHPAD>\n\nThe answer is 42."
                ),
            },
        ]
        output = self._capture_display(cli)

        assert "REASONING_SCRATCHPAD" not in output
        assert "Let me think step by step" not in output
        assert "The answer is 42" in output

    def test_pure_reasoning_message_skipped(self):
        """Assistant messages that are only reasoning should be skipped."""
        cli = _make_cli()
        cli.conversation_history = [
            {"role": "user", "content": "Hello"},
            {
                "role": "assistant",
                "content": "<REASONING_SCRATCHPAD>\nJust thinking...\n</REASONING_SCRATCHPAD>",
            },
            {"role": "assistant", "content": "Hi there!"},
        ]
        output = self._capture_display(cli)

        assert "Just thinking" not in output
        assert "Hi there!" in output

    def test_assistant_with_text_and_tool_calls(self):
        """When an assistant message has both text content AND tool_calls."""
        cli = _make_cli()
        cli.conversation_history = [
            {"role": "user", "content": "Do something complex"},
            {
                "role": "assistant",
                "content": "Let me search for that.",
                "tool_calls": [
                    {
                        "id": "call_1",
                        "type": "function",
                        "function": {"name": "terminal", "arguments": '{"command":"ls"}'},
                    }
                ],
            },
        ]
        output = self._capture_display(cli)

        assert "Let me search for that." in output
        assert "1 tool call" in output
        assert "terminal" in output


# ── Tests for _preload_resumed_session ──────────────────────────────


class TestPreloadResumedSession:
    """_preload_resumed_session() loads session from DB early."""

    def test_returns_false_when_not_resumed(self):
        cli = _make_cli()
        assert cli._preload_resumed_session() is False

    def test_returns_false_when_no_session_db(self):
        cli = _make_cli(resume="test_session_id")
        cli._session_db = None
        assert cli._preload_resumed_session() is False

    def test_returns_false_when_session_not_found(self):
        cli = _make_cli(resume="nonexistent_session")
        mock_db = MagicMock()
        mock_db.get_session.return_value = None
        cli._session_db = mock_db

        buf = StringIO()
        cli.console.file = buf
        result = cli._preload_resumed_session()

        assert result is False
        output = buf.getvalue()
        assert "Session not found" in output

    def test_returns_false_when_session_has_no_messages(self):
        cli = _make_cli(resume="empty_session")
        mock_db = MagicMock()
        mock_db.get_session.return_value = {"id": "empty_session", "title": None}
        mock_db.get_messages_as_conversation.return_value = []
        cli._session_db = mock_db

        buf = StringIO()
        cli.console.file = buf
        result = cli._preload_resumed_session()

        assert result is False
        output = buf.getvalue()
        assert "no messages" in output

    def test_loads_session_successfully(self):
        cli = _make_cli(resume="good_session")
        messages = _simple_history()
        mock_db = MagicMock()
        mock_db.get_session.return_value = {"id": "good_session", "title": "Test Session"}
        mock_db.get_messages_as_conversation.return_value = messages
        cli._session_db = mock_db

        buf = StringIO()
        cli.console.file = buf
        result = cli._preload_resumed_session()

        assert result is True
        assert cli.conversation_history == messages
        output = buf.getvalue()
        assert "Resumed session" in output
        assert "good_session" in output
        assert "Test Session" in output
        assert "2 user messages" in output

    def test_reopens_session_in_db(self):
        cli = _make_cli(resume="reopen_session")
        messages = [{"role": "user", "content": "hi"}]
        mock_db = MagicMock()
        mock_db.get_session.return_value = {"id": "reopen_session", "title": None}
        mock_db.get_messages_as_conversation.return_value = messages
        mock_conn = MagicMock()
        mock_db._conn = mock_conn
        cli._session_db = mock_db

        buf = StringIO()
        cli.console.file = buf
        cli._preload_resumed_session()

        # Should have executed UPDATE to clear ended_at
        mock_conn.execute.assert_called_once()
        call_args = mock_conn.execute.call_args
        assert "ended_at = NULL" in call_args[0][0]
        mock_conn.commit.assert_called_once()

    def test_singular_user_message_grammar(self):
        """1 user message should say 'message' not 'messages'."""
        cli = _make_cli(resume="one_msg_session")
        messages = [
            {"role": "user", "content": "hello"},
            {"role": "assistant", "content": "hi"},
        ]
        mock_db = MagicMock()
        mock_db.get_session.return_value = {"id": "one_msg_session", "title": None}
        mock_db.get_messages_as_conversation.return_value = messages
        mock_db._conn = MagicMock()
        cli._session_db = mock_db

        buf = StringIO()
        cli.console.file = buf
        cli._preload_resumed_session()

        output = buf.getvalue()
        assert "1 user message," in output
        assert "1 user messages" not in output


# ── Integration: _init_agent skips when preloaded ────────────────────


class TestInitAgentSkipsPreloaded:
    """_init_agent() should skip DB load when history is already populated."""

    def test_init_agent_skips_db_when_preloaded(self):
        """If conversation_history is already set, _init_agent should not
        reload from the DB."""
        cli = _make_cli(resume="preloaded_session")
        cli.conversation_history = _simple_history()

        mock_db = MagicMock()
        cli._session_db = mock_db

        # _init_agent will fail at credential resolution (no real API key),
        # but the session-loading block should be skipped entirely
        with patch.object(cli, "_ensure_runtime_credentials", return_value=False):
            cli._init_agent()

        # get_messages_as_conversation should NOT have been called
        mock_db.get_messages_as_conversation.assert_not_called()


# ── Config default tests ─────────────────────────────────────────────


class TestResumeDisplayConfig:
    """resume_display config option defaults and behavior."""

    def test_default_config_has_resume_display(self):
        """DEFAULT_CONFIG in hermes_cli/config.py includes resume_display."""
        from hermes_cli.config import DEFAULT_CONFIG
        display = DEFAULT_CONFIG.get("display", {})
        assert "resume_display" in display
        assert display["resume_display"] == "full"

    def test_cli_defaults_have_resume_display(self):
        """cli.py load_cli_config defaults include resume_display."""
        import cli as _cli_mod
        from cli import load_cli_config

        with (
            patch("pathlib.Path.exists", return_value=False),
            patch.dict("os.environ", {"LLM_MODEL": ""}, clear=False),
        ):
            config = load_cli_config()

        display = config.get("display", {})
        assert display.get("resume_display") == "full"

```

## File: test_surrogate_sanitization.py
```
"""Tests for surrogate character sanitization in user input.

Surrogates (U+D800..U+DFFF) are invalid in UTF-8 and crash json.dumps()
inside the OpenAI SDK. They can appear via clipboard paste from rich-text
editors like Google Docs.
"""
import json
import pytest
from unittest.mock import MagicMock, patch

from run_agent import (
    _sanitize_surrogates,
    _sanitize_messages_surrogates,
    _SURROGATE_RE,
)


class TestSanitizeSurrogates:
    """Test the _sanitize_surrogates() helper."""

    def test_normal_text_unchanged(self):
        text = "Hello, this is normal text with unicode: café ñ 日本語 🎉"
        assert _sanitize_surrogates(text) == text

    def test_empty_string(self):
        assert _sanitize_surrogates("") == ""

    def test_single_surrogate_replaced(self):
        result = _sanitize_surrogates("Hello \udce2 world")
        assert result == "Hello \ufffd world"

    def test_multiple_surrogates_replaced(self):
        result = _sanitize_surrogates("a\ud800b\udc00c\udfff")
        assert result == "a\ufffdb\ufffdc\ufffd"

    def test_all_surrogate_range(self):
        """Verify the regex catches the full surrogate range."""
        for cp in [0xD800, 0xD900, 0xDA00, 0xDB00, 0xDC00, 0xDD00, 0xDE00, 0xDF00, 0xDFFF]:
            text = f"test{chr(cp)}end"
            result = _sanitize_surrogates(text)
            assert '\ufffd' in result, f"Surrogate U+{cp:04X} not caught"

    def test_result_is_json_serializable(self):
        """Sanitized text must survive json.dumps + utf-8 encoding."""
        dirty = "data \udce2\udcb0 from clipboard"
        clean = _sanitize_surrogates(dirty)
        serialized = json.dumps({"content": clean}, ensure_ascii=False)
        # Must not raise UnicodeEncodeError
        serialized.encode("utf-8")

    def test_original_surrogates_fail_encoding(self):
        """Confirm the original bug: surrogates crash utf-8 encoding."""
        dirty = "data \udce2 from clipboard"
        serialized = json.dumps({"content": dirty}, ensure_ascii=False)
        with pytest.raises(UnicodeEncodeError):
            serialized.encode("utf-8")


class TestSanitizeMessagesSurrogates:
    """Test the _sanitize_messages_surrogates() helper for message lists."""

    def test_clean_messages_returns_false(self):
        msgs = [
            {"role": "user", "content": "all clean"},
            {"role": "assistant", "content": "me too"},
        ]
        assert _sanitize_messages_surrogates(msgs) is False

    def test_dirty_string_content_sanitized(self):
        msgs = [
            {"role": "user", "content": "text with \udce2 surrogate"},
        ]
        assert _sanitize_messages_surrogates(msgs) is True
        assert "\ufffd" in msgs[0]["content"]
        assert "\udce2" not in msgs[0]["content"]

    def test_dirty_multimodal_content_sanitized(self):
        msgs = [
            {"role": "user", "content": [
                {"type": "text", "text": "multimodal \udce2 content"},
                {"type": "image_url", "image_url": {"url": "http://example.com"}},
            ]},
        ]
        assert _sanitize_messages_surrogates(msgs) is True
        assert "\ufffd" in msgs[0]["content"][0]["text"]
        assert "\udce2" not in msgs[0]["content"][0]["text"]

    def test_mixed_clean_and_dirty(self):
        msgs = [
            {"role": "user", "content": "clean text"},
            {"role": "user", "content": "dirty \udce2 text"},
            {"role": "assistant", "content": "clean response"},
        ]
        assert _sanitize_messages_surrogates(msgs) is True
        assert msgs[0]["content"] == "clean text"
        assert "\ufffd" in msgs[1]["content"]
        assert msgs[2]["content"] == "clean response"

    def test_non_dict_items_skipped(self):
        msgs = ["not a dict", {"role": "user", "content": "ok"}]
        assert _sanitize_messages_surrogates(msgs) is False

    def test_tool_messages_sanitized(self):
        """Tool results could also contain surrogates from file reads etc."""
        msgs = [
            {"role": "tool", "content": "result with \udce2 data", "tool_call_id": "x"},
        ]
        assert _sanitize_messages_surrogates(msgs) is True
        assert "\ufffd" in msgs[0]["content"]


class TestRunConversationSurrogateSanitization:
    """Integration: verify run_conversation sanitizes user_message."""

    @patch("run_agent.AIAgent._build_system_prompt")
    @patch("run_agent.AIAgent._interruptible_streaming_api_call")
    @patch("run_agent.AIAgent._interruptible_api_call")
    def test_user_message_surrogates_sanitized(self, mock_api, mock_stream, mock_sys):
        """Surrogates in user_message are stripped before API call."""
        from run_agent import AIAgent

        mock_sys.return_value = "system prompt"

        # Mock streaming to return a simple response
        mock_choice = MagicMock()
        mock_choice.message.content = "response"
        mock_choice.message.tool_calls = None
        mock_choice.message.refusal = None
        mock_choice.finish_reason = "stop"
        mock_choice.message.reasoning_content = None

        mock_response = MagicMock()
        mock_response.choices = [mock_choice]
        mock_response.usage = MagicMock(prompt_tokens=10, completion_tokens=5, total_tokens=15)
        mock_response.model = "test-model"
        mock_response.id = "test-id"

        mock_stream.return_value = mock_response
        mock_api.return_value = mock_response

        agent = AIAgent(model="test/model", quiet_mode=True, skip_memory=True, skip_context_files=True)
        agent.client = MagicMock()

        # Pass a message with surrogates
        result = agent.run_conversation(
            user_message="test \udce2 message",
            conversation_history=[],
        )

        # The message stored in history should have surrogates replaced
        for msg in result.get("messages", []):
            if msg.get("role") == "user":
                assert "\udce2" not in msg["content"], "Surrogate leaked into stored message"
                assert "\ufffd" in msg["content"], "Replacement char not in stored message"

```

## File: test_worktree.py
```
"""Tests for git worktree isolation (CLI --worktree / -w flag).

Verifies worktree creation, cleanup, .worktreeinclude handling,
.gitignore management, and integration with the CLI.  (#652)
"""

import os
import shutil
import subprocess
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock


@pytest.fixture
def git_repo(tmp_path):
    """Create a temporary git repo for testing."""
    repo = tmp_path / "test-repo"
    repo.mkdir()
    subprocess.run(["git", "init"], cwd=repo, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "test@test.com"],
        cwd=repo, capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"],
        cwd=repo, capture_output=True,
    )
    # Create initial commit (worktrees need at least one commit)
    (repo / "README.md").write_text("# Test Repo\n")
    subprocess.run(["git", "add", "."], cwd=repo, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "Initial commit"],
        cwd=repo, capture_output=True,
    )
    return repo


# ---------------------------------------------------------------------------
# Lightweight reimplementations for testing (avoid importing cli.py)
# ---------------------------------------------------------------------------

def _git_repo_root(cwd=None):
    """Test version of _git_repo_root."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, timeout=5,
            cwd=cwd,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def _setup_worktree(repo_root):
    """Test version of _setup_worktree — creates a worktree."""
    import uuid
    short_id = uuid.uuid4().hex[:8]
    wt_name = f"hermes-{short_id}"
    branch_name = f"hermes/{wt_name}"

    worktrees_dir = Path(repo_root) / ".worktrees"
    worktrees_dir.mkdir(parents=True, exist_ok=True)
    wt_path = worktrees_dir / wt_name

    result = subprocess.run(
        ["git", "worktree", "add", str(wt_path), "-b", branch_name, "HEAD"],
        capture_output=True, text=True, timeout=30, cwd=repo_root,
    )
    if result.returncode != 0:
        return None

    return {
        "path": str(wt_path),
        "branch": branch_name,
        "repo_root": repo_root,
    }


def _cleanup_worktree(info):
    """Test version of _cleanup_worktree."""
    wt_path = info["path"]
    branch = info["branch"]
    repo_root = info["repo_root"]

    if not Path(wt_path).exists():
        return

    # Check for uncommitted changes
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True, text=True, timeout=10, cwd=wt_path,
    )
    has_changes = bool(status.stdout.strip())

    if has_changes:
        return False  # Did not clean up

    subprocess.run(
        ["git", "worktree", "remove", wt_path, "--force"],
        capture_output=True, text=True, timeout=15, cwd=repo_root,
    )
    subprocess.run(
        ["git", "branch", "-D", branch],
        capture_output=True, text=True, timeout=10, cwd=repo_root,
    )
    return True  # Cleaned up


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestGitRepoDetection:
    """Test git repo root detection."""

    def test_detects_git_repo(self, git_repo):
        root = _git_repo_root(cwd=str(git_repo))
        assert root is not None
        assert Path(root).resolve() == git_repo.resolve()

    def test_detects_subdirectory(self, git_repo):
        subdir = git_repo / "src" / "lib"
        subdir.mkdir(parents=True)
        root = _git_repo_root(cwd=str(subdir))
        assert root is not None
        assert Path(root).resolve() == git_repo.resolve()

    def test_returns_none_outside_repo(self, tmp_path):
        # tmp_path itself is not a git repo
        bare_dir = tmp_path / "not-a-repo"
        bare_dir.mkdir()
        root = _git_repo_root(cwd=str(bare_dir))
        assert root is None


class TestWorktreeCreation:
    """Test worktree setup."""

    def test_creates_worktree(self, git_repo):
        info = _setup_worktree(str(git_repo))
        assert info is not None
        assert Path(info["path"]).exists()
        assert info["branch"].startswith("hermes/hermes-")
        assert info["repo_root"] == str(git_repo)

        # Verify it's a valid git worktree
        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True, text=True, cwd=info["path"],
        )
        assert result.stdout.strip() == "true"

    def test_worktree_has_own_branch(self, git_repo):
        info = _setup_worktree(str(git_repo))
        assert info is not None

        # Check branch name in worktree
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, cwd=info["path"],
        )
        assert result.stdout.strip() == info["branch"]

    def test_worktree_is_independent(self, git_repo):
        """Two worktrees from the same repo are independent."""
        info1 = _setup_worktree(str(git_repo))
        info2 = _setup_worktree(str(git_repo))
        assert info1 is not None
        assert info2 is not None
        assert info1["path"] != info2["path"]
        assert info1["branch"] != info2["branch"]

        # Create a file in worktree 1
        (Path(info1["path"]) / "only-in-wt1.txt").write_text("hello")

        # It should NOT appear in worktree 2
        assert not (Path(info2["path"]) / "only-in-wt1.txt").exists()

    def test_worktrees_dir_created(self, git_repo):
        info = _setup_worktree(str(git_repo))
        assert info is not None
        assert (git_repo / ".worktrees").is_dir()

    def test_worktree_has_repo_files(self, git_repo):
        """Worktree should contain the repo's tracked files."""
        info = _setup_worktree(str(git_repo))
        assert info is not None
        assert (Path(info["path"]) / "README.md").exists()


class TestWorktreeCleanup:
    """Test worktree cleanup on exit."""

    def test_clean_worktree_removed(self, git_repo):
        info = _setup_worktree(str(git_repo))
        assert info is not None
        assert Path(info["path"]).exists()

        result = _cleanup_worktree(info)
        assert result is True
        assert not Path(info["path"]).exists()

    def test_dirty_worktree_kept(self, git_repo):
        info = _setup_worktree(str(git_repo))
        assert info is not None

        # Make uncommitted changes
        (Path(info["path"]) / "new-file.txt").write_text("uncommitted")
        subprocess.run(
            ["git", "add", "new-file.txt"],
            cwd=info["path"], capture_output=True,
        )

        result = _cleanup_worktree(info)
        assert result is False
        assert Path(info["path"]).exists()  # Still there

    def test_branch_deleted_on_cleanup(self, git_repo):
        info = _setup_worktree(str(git_repo))
        branch = info["branch"]

        _cleanup_worktree(info)

        # Branch should be gone
        result = subprocess.run(
            ["git", "branch", "--list", branch],
            capture_output=True, text=True, cwd=str(git_repo),
        )
        assert branch not in result.stdout

    def test_cleanup_nonexistent_worktree(self, git_repo):
        """Cleanup should handle already-removed worktrees gracefully."""
        info = {
            "path": str(git_repo / ".worktrees" / "nonexistent"),
            "branch": "hermes/nonexistent",
            "repo_root": str(git_repo),
        }
        # Should not raise
        _cleanup_worktree(info)


class TestWorktreeInclude:
    """Test .worktreeinclude file handling."""

    def test_copies_included_files(self, git_repo):
        """Files listed in .worktreeinclude should be copied to the worktree."""
        # Create a .env file (gitignored)
        (git_repo / ".env").write_text("SECRET=abc123")
        (git_repo / ".gitignore").write_text(".env\n.worktrees/\n")
        subprocess.run(
            ["git", "add", ".gitignore"],
            cwd=str(git_repo), capture_output=True,
        )
        subprocess.run(
            ["git", "commit", "-m", "Add gitignore"],
            cwd=str(git_repo), capture_output=True,
        )

        # Create .worktreeinclude
        (git_repo / ".worktreeinclude").write_text(".env\n")

        # Import and use the real _setup_worktree logic for include handling
        info = _setup_worktree(str(git_repo))
        assert info is not None

        # Manually copy .worktreeinclude entries (mirrors cli.py logic)
        import shutil
        include_file = git_repo / ".worktreeinclude"
        wt_path = Path(info["path"])
        for line in include_file.read_text().splitlines():
            entry = line.strip()
            if not entry or entry.startswith("#"):
                continue
            src = git_repo / entry
            dst = wt_path / entry
            if src.is_file():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(str(src), str(dst))

        # Verify .env was copied
        assert (wt_path / ".env").exists()
        assert (wt_path / ".env").read_text() == "SECRET=abc123"

    def test_ignores_comments_and_blanks(self, git_repo):
        """Comments and blank lines in .worktreeinclude should be skipped."""
        (git_repo / ".worktreeinclude").write_text(
            "# This is a comment\n"
            "\n"
            "  # Another comment\n"
        )
        info = _setup_worktree(str(git_repo))
        assert info is not None
        # Should not crash — just skip all lines


class TestGitignoreManagement:
    """Test that .worktrees/ is added to .gitignore."""

    def test_adds_to_gitignore(self, git_repo):
        """Creating a worktree should add .worktrees/ to .gitignore."""
        # Remove any existing .gitignore
        gitignore = git_repo / ".gitignore"
        if gitignore.exists():
            gitignore.unlink()

        info = _setup_worktree(str(git_repo))
        assert info is not None

        # Now manually add .worktrees/ to .gitignore (mirrors cli.py logic)
        _ignore_entry = ".worktrees/"
        existing = gitignore.read_text() if gitignore.exists() else ""
        if _ignore_entry not in existing.splitlines():
            with open(gitignore, "a") as f:
                if existing and not existing.endswith("\n"):
                    f.write("\n")
                f.write(f"{_ignore_entry}\n")

        content = gitignore.read_text()
        assert ".worktrees/" in content

    def test_does_not_duplicate_gitignore_entry(self, git_repo):
        """If .worktrees/ is already in .gitignore, don't add again."""
        gitignore = git_repo / ".gitignore"
        gitignore.write_text(".worktrees/\n")

        # The check should see it's already there
        existing = gitignore.read_text()
        assert ".worktrees/" in existing.splitlines()


class TestMultipleWorktrees:
    """Test running multiple worktrees concurrently (the core use case)."""

    def test_ten_concurrent_worktrees(self, git_repo):
        """Create 10 worktrees — simulating 10 parallel agents."""
        worktrees = []
        for _ in range(10):
            info = _setup_worktree(str(git_repo))
            assert info is not None
            worktrees.append(info)

        # All should exist and be independent
        paths = [info["path"] for info in worktrees]
        assert len(set(paths)) == 10  # All unique

        # Each should have the repo files
        for info in worktrees:
            assert (Path(info["path"]) / "README.md").exists()

        # Edit a file in one worktree
        (Path(worktrees[0]["path"]) / "README.md").write_text("Modified in wt0")

        # Others should be unaffected
        for info in worktrees[1:]:
            assert (Path(info["path"]) / "README.md").read_text() == "# Test Repo\n"

        # List worktrees via git
        result = subprocess.run(
            ["git", "worktree", "list"],
            capture_output=True, text=True, cwd=str(git_repo),
        )
        # Should have 11 entries: main + 10 worktrees
        lines = [l for l in result.stdout.strip().splitlines() if l.strip()]
        assert len(lines) == 11

        # Cleanup all
        for info in worktrees:
            # Discard changes first so cleanup works
            subprocess.run(
                ["git", "checkout", "--", "."],
                cwd=info["path"], capture_output=True,
            )
            _cleanup_worktree(info)

        # All should be removed
        for info in worktrees:
            assert not Path(info["path"]).exists()


class TestWorktreeDirectorySymlink:
    """Test .worktreeinclude with directories (symlinked)."""

    def test_symlinks_directory(self, git_repo):
        """Directories in .worktreeinclude should be symlinked."""
        # Create a .venv directory
        venv_dir = git_repo / ".venv" / "lib"
        venv_dir.mkdir(parents=True)
        (venv_dir / "marker.txt").write_text("venv marker")
        (git_repo / ".gitignore").write_text(".venv/\n.worktrees/\n")
        subprocess.run(
            ["git", "add", ".gitignore"], cwd=str(git_repo), capture_output=True
        )
        subprocess.run(
            ["git", "commit", "-m", "gitignore"], cwd=str(git_repo), capture_output=True
        )

        (git_repo / ".worktreeinclude").write_text(".venv/\n")

        info = _setup_worktree(str(git_repo))
        assert info is not None

        wt_path = Path(info["path"])
        src = git_repo / ".venv"
        dst = wt_path / ".venv"

        # Manually symlink (mirrors cli.py logic)
        if not dst.exists():
            dst.parent.mkdir(parents=True, exist_ok=True)
            os.symlink(str(src.resolve()), str(dst))

        assert dst.is_symlink()
        assert (dst / "lib" / "marker.txt").read_text() == "venv marker"


class TestStaleWorktreePruning:
    """Test _prune_stale_worktrees garbage collection."""

    def test_prunes_old_clean_worktree(self, git_repo):
        """Old clean worktrees should be removed on prune."""
        import time

        info = _setup_worktree(str(git_repo))
        assert info is not None
        assert Path(info["path"]).exists()

        # Make the worktree look old (set mtime to 25h ago)
        old_time = time.time() - (25 * 3600)
        os.utime(info["path"], (old_time, old_time))

        # Reimplementation of prune logic (matches cli.py)
        worktrees_dir = git_repo / ".worktrees"
        cutoff = time.time() - (24 * 3600)

        for entry in worktrees_dir.iterdir():
            if not entry.is_dir() or not entry.name.startswith("hermes-"):
                continue
            try:
                mtime = entry.stat().st_mtime
                if mtime > cutoff:
                    continue
            except Exception:
                continue

            status = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True, text=True, timeout=5, cwd=str(entry),
            )
            if status.stdout.strip():
                continue

            branch_result = subprocess.run(
                ["git", "branch", "--show-current"],
                capture_output=True, text=True, timeout=5, cwd=str(entry),
            )
            branch = branch_result.stdout.strip()
            subprocess.run(
                ["git", "worktree", "remove", str(entry), "--force"],
                capture_output=True, text=True, timeout=15, cwd=str(git_repo),
            )
            if branch:
                subprocess.run(
                    ["git", "branch", "-D", branch],
                    capture_output=True, text=True, timeout=10, cwd=str(git_repo),
                )

        assert not Path(info["path"]).exists()

    def test_keeps_recent_worktree(self, git_repo):
        """Recent worktrees should NOT be pruned."""
        import time

        info = _setup_worktree(str(git_repo))
        assert info is not None

        # Don't modify mtime — it's recent
        worktrees_dir = git_repo / ".worktrees"
        cutoff = time.time() - (24 * 3600)

        pruned = False
        for entry in worktrees_dir.iterdir():
            if not entry.is_dir() or not entry.name.startswith("hermes-"):
                continue
            mtime = entry.stat().st_mtime
            if mtime > cutoff:
                continue  # Too recent
            pruned = True

        assert not pruned
        assert Path(info["path"]).exists()

    def test_keeps_dirty_old_worktree(self, git_repo):
        """Old worktrees with uncommitted changes should NOT be pruned."""
        import time

        info = _setup_worktree(str(git_repo))
        assert info is not None

        # Make it dirty
        (Path(info["path"]) / "dirty.txt").write_text("uncommitted")
        subprocess.run(
            ["git", "add", "dirty.txt"],
            cwd=info["path"], capture_output=True,
        )

        # Make it old
        old_time = time.time() - (25 * 3600)
        os.utime(info["path"], (old_time, old_time))

        # Check if it would be pruned
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, cwd=info["path"],
        )
        has_changes = bool(status.stdout.strip())
        assert has_changes  # Should be dirty → not pruned
        assert Path(info["path"]).exists()


class TestEdgeCases:
    """Test edge cases for robustness."""

    def test_no_commits_repo(self, tmp_path):
        """Worktree creation should fail gracefully on a repo with no commits."""
        repo = tmp_path / "empty-repo"
        repo.mkdir()
        subprocess.run(["git", "init"], cwd=str(repo), capture_output=True)

        info = _setup_worktree(str(repo))
        assert info is None  # Should fail gracefully

    def test_not_a_git_repo(self, tmp_path):
        """Repo detection should return None for non-git directories."""
        bare = tmp_path / "not-git"
        bare.mkdir()
        root = _git_repo_root(cwd=str(bare))
        assert root is None

    def test_worktrees_dir_already_exists(self, git_repo):
        """Should work fine if .worktrees/ already exists."""
        (git_repo / ".worktrees").mkdir(exist_ok=True)
        info = _setup_worktree(str(git_repo))
        assert info is not None
        assert Path(info["path"]).exists()


class TestCLIFlagLogic:
    """Test the flag/config OR logic from main()."""

    def test_worktree_flag_triggers(self):
        """--worktree flag should trigger worktree creation."""
        worktree = True
        w = False
        config_worktree = False
        use_worktree = worktree or w or config_worktree
        assert use_worktree

    def test_w_flag_triggers(self):
        """-w flag should trigger worktree creation."""
        worktree = False
        w = True
        config_worktree = False
        use_worktree = worktree or w or config_worktree
        assert use_worktree

    def test_config_triggers(self):
        """worktree: true in config should trigger worktree creation."""
        worktree = False
        w = False
        config_worktree = True
        use_worktree = worktree or w or config_worktree
        assert use_worktree

    def test_none_set_no_trigger(self):
        """No flags and no config should not trigger."""
        worktree = False
        w = False
        config_worktree = False
        use_worktree = worktree or w or config_worktree
        assert not use_worktree


class TestTerminalCWDIntegration:
    """Test that TERMINAL_CWD is correctly set to the worktree path."""

    def test_terminal_cwd_set(self, git_repo):
        """After worktree setup, TERMINAL_CWD should point to the worktree."""
        info = _setup_worktree(str(git_repo))
        assert info is not None

        # This is what main() does:
        os.environ["TERMINAL_CWD"] = info["path"]
        assert os.environ["TERMINAL_CWD"] == info["path"]
        assert Path(os.environ["TERMINAL_CWD"]).exists()

        # Clean up env
        del os.environ["TERMINAL_CWD"]

    def test_terminal_cwd_is_valid_git_repo(self, git_repo):
        """The TERMINAL_CWD worktree should be a valid git working tree."""
        info = _setup_worktree(str(git_repo))
        assert info is not None

        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True, text=True, cwd=info["path"],
        )
        assert result.stdout.strip() == "true"


class TestSystemPromptInjection:
    """Test that the agent gets worktree context in its system prompt."""

    def test_prompt_note_format(self, git_repo):
        """Verify the system prompt note contains all required info."""
        info = _setup_worktree(str(git_repo))
        assert info is not None

        # This is what main() does:
        wt_note = (
            f"\n\n[System note: You are working in an isolated git worktree at "
            f"{info['path']}. Your branch is `{info['branch']}`. "
            f"Changes here do not affect the main working tree or other agents. "
            f"Remember to commit and push your changes, and create a PR if appropriate. "
            f"The original repo is at {info['repo_root']}.]"
        )

        assert info["path"] in wt_note
        assert info["branch"] in wt_note
        assert info["repo_root"] in wt_note
        assert "isolated git worktree" in wt_note
        assert "commit and push" in wt_note

```

## File: test_worktree_security.py
```
"""Security-focused integration tests for CLI worktree setup."""

import subprocess
from pathlib import Path

import pytest


@pytest.fixture
def git_repo(tmp_path):
    """Create a temporary git repo for testing real cli._setup_worktree behavior."""
    repo = tmp_path / "test-repo"
    repo.mkdir()
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True, capture_output=True)
    (repo / "README.md").write_text("# Test Repo\n")
    subprocess.run(["git", "add", "."], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=repo, check=True, capture_output=True)
    return repo


def _force_remove_worktree(info: dict | None) -> None:
    if not info:
        return
    subprocess.run(
        ["git", "worktree", "remove", info["path"], "--force"],
        cwd=info["repo_root"],
        capture_output=True,
        check=False,
    )
    subprocess.run(
        ["git", "branch", "-D", info["branch"]],
        cwd=info["repo_root"],
        capture_output=True,
        check=False,
    )


class TestWorktreeIncludeSecurity:
    def test_rejects_parent_directory_file_traversal(self, git_repo):
        import cli as cli_mod

        outside_file = git_repo.parent / "sensitive.txt"
        outside_file.write_text("SENSITIVE DATA")
        (git_repo / ".worktreeinclude").write_text("../sensitive.txt\n")

        info = None
        try:
            info = cli_mod._setup_worktree(str(git_repo))
            assert info is not None

            wt_path = Path(info["path"])
            assert not (wt_path.parent / "sensitive.txt").exists()
            assert not (wt_path / "../sensitive.txt").resolve().exists()
        finally:
            _force_remove_worktree(info)

    def test_rejects_parent_directory_directory_traversal(self, git_repo):
        import cli as cli_mod

        outside_dir = git_repo.parent / "outside-dir"
        outside_dir.mkdir()
        (outside_dir / "secret.txt").write_text("SENSITIVE DIR DATA")
        (git_repo / ".worktreeinclude").write_text("../outside-dir\n")

        info = None
        try:
            info = cli_mod._setup_worktree(str(git_repo))
            assert info is not None

            wt_path = Path(info["path"])
            escaped_dir = wt_path.parent / "outside-dir"
            assert not escaped_dir.exists()
            assert not escaped_dir.is_symlink()
        finally:
            _force_remove_worktree(info)

    def test_rejects_symlink_that_resolves_outside_repo(self, git_repo):
        import cli as cli_mod

        outside_file = git_repo.parent / "linked-secret.txt"
        outside_file.write_text("LINKED SECRET")
        (git_repo / "leak.txt").symlink_to(outside_file)
        (git_repo / ".worktreeinclude").write_text("leak.txt\n")

        info = None
        try:
            info = cli_mod._setup_worktree(str(git_repo))
            assert info is not None

            assert not (Path(info["path"]) / "leak.txt").exists()
        finally:
            _force_remove_worktree(info)

    def test_allows_valid_file_include(self, git_repo):
        import cli as cli_mod

        (git_repo / ".env").write_text("SECRET=***\n")
        (git_repo / ".worktreeinclude").write_text(".env\n")

        info = None
        try:
            info = cli_mod._setup_worktree(str(git_repo))
            assert info is not None

            copied = Path(info["path"]) / ".env"
            assert copied.exists()
            assert copied.read_text() == "SECRET=***\n"
        finally:
            _force_remove_worktree(info)

    def test_allows_valid_directory_include(self, git_repo):
        import cli as cli_mod

        assets_dir = git_repo / ".venv" / "lib"
        assets_dir.mkdir(parents=True)
        (assets_dir / "marker.txt").write_text("venv marker")
        (git_repo / ".worktreeinclude").write_text(".venv\n")

        info = None
        try:
            info = cli_mod._setup_worktree(str(git_repo))
            assert info is not None

            linked_dir = Path(info["path"]) / ".venv"
            assert linked_dir.is_symlink()
            assert (linked_dir / "lib" / "marker.txt").read_text() == "venv marker"
        finally:
            _force_remove_worktree(info)

```

## File: tui.md
```
---
summary: "CLI reference for `openclaw tui` (terminal UI connected to the Gateway)"
read_when:
  - You want a terminal UI for the Gateway (remote-friendly)
  - You want to pass url/token/session from scripts
title: "tui"
---

# `openclaw tui`

Open the terminal UI connected to the Gateway.

Related:


Notes:

- `tui` resolves configured gateway auth SecretRefs for token/password auth when possible (`env`/`file`/`exec` providers).
- When launched from inside a configured agent workspace directory, TUI auto-selects that agent for the session key default (unless `--session` is explicitly `agent:<id>:...`).

## Examples

```bash
openclaw tui
openclaw tui --url ws://127.0.0.1:18789 --token <token>
openclaw tui --session main --deliver
# when run inside an agent workspace, infers that agent automatically
openclaw tui --session bugfix
```

```

## File: uninstall.md
```
---
summary: "CLI reference for `openclaw uninstall` (remove gateway service + local data)"
read_when:
  - You want to remove the gateway service and/or local state
  - You want a dry-run first
title: "uninstall"
---

# `openclaw uninstall`

Uninstall the gateway service + local data (CLI remains).

Options:

- `--service`: remove the gateway service
- `--state`: remove state and config
- `--workspace`: remove workspace directories
- `--app`: remove the macOS app
- `--all`: remove service, state, workspace, and app
- `--yes`: skip confirmation prompts
- `--non-interactive`: disable prompts; requires `--yes`
- `--dry-run`: print actions without removing files

Examples:

```bash
openclaw backup create
openclaw uninstall
openclaw uninstall --service --yes --non-interactive
openclaw uninstall --state --workspace --yes --non-interactive
openclaw uninstall --all --yes
openclaw uninstall --dry-run
```

Notes:

- Run `openclaw backup create` first if you want a restorable snapshot before removing state or workspaces.
- `--all` is shorthand for removing service, state, workspace, and app together.
- `--non-interactive` requires `--yes`.

```

## File: update.md
```
---
summary: "CLI reference for `openclaw update` (safe-ish source update + gateway auto-restart)"
read_when:
  - You want to update a source checkout safely
  - You need to understand `--update` shorthand behavior
title: "update"
---

# `openclaw update`

Safely update OpenClaw and switch between stable/beta/dev channels.

If you installed via **npm/pnpm/bun** (global install, no git metadata),
updates happen via the package-manager flow in [Updating](/install/updating).

## Usage

```bash
openclaw update
openclaw update status
openclaw update wizard
openclaw update --channel beta
openclaw update --channel dev
openclaw update --tag beta
openclaw update --tag main
openclaw update --dry-run
openclaw update --no-restart
openclaw update --yes
openclaw update --json
openclaw --update
```

## Options

- `--no-restart`: skip restarting the Gateway service after a successful update.
- `--channel <stable|beta|dev>`: set the update channel (git + npm; persisted in config).
- `--tag <dist-tag|version|spec>`: override the package target for this update only. For package installs, `main` maps to `github:openclaw/openclaw#main`.
- `--dry-run`: preview planned update actions (channel/tag/target/restart flow) without writing config, installing, syncing plugins, or restarting.
- `--json`: print machine-readable `UpdateRunResult` JSON.
- `--timeout <seconds>`: per-step timeout (default is 1200s).
- `--yes`: skip confirmation prompts (for example downgrade confirmation)

Note: downgrades require confirmation because older versions can break configuration.

## `update status`

Show the active update channel + git tag/branch/SHA (for source checkouts), plus update availability.

```bash
openclaw update status
openclaw update status --json
openclaw update status --timeout 10
```

Options:

- `--json`: print machine-readable status JSON.
- `--timeout <seconds>`: timeout for checks (default is 3s).

## `update wizard`

Interactive flow to pick an update channel and confirm whether to restart the Gateway
after updating (default is to restart). If you select `dev` without a git checkout, it
offers to create one.

Options:

- `--timeout <seconds>`: timeout for each update step (default `1200`)

## What it does

When you switch channels explicitly (`--channel ...`), OpenClaw also keeps the
install method aligned:

- `dev` → ensures a git checkout (default: `~/openclaw`, override with `OPENCLAW_GIT_DIR`),
  updates it, and installs the global CLI from that checkout.
- `stable` → installs from npm using `latest`.
- `beta` → prefers npm dist-tag `beta`, but falls back to `latest` when beta is
  missing or older than the current stable release.

The Gateway core auto-updater (when enabled via config) reuses this same update path.

## Git checkout flow

Channels:

- `stable`: checkout the latest non-beta tag, then build + doctor.
- `beta`: prefer the latest `-beta` tag, but fall back to the latest stable tag
  when beta is missing or older.
- `dev`: checkout `main`, then fetch + rebase.

High-level:

1. Requires a clean worktree (no uncommitted changes).
2. Switches to the selected channel (tag or branch).
3. Fetches upstream (dev only).
4. Dev only: preflight lint + TypeScript build in a temp worktree; if the tip fails, walks back up to 10 commits to find the newest clean build.
5. Rebases onto the selected commit (dev only).
6. Installs deps with the repo package manager. For pnpm checkouts, the updater bootstraps `pnpm` on demand (via `corepack` first, then a temporary `npm install pnpm@10` fallback) instead of running `npm run build` inside a pnpm workspace.
7. Builds + builds the Control UI.
8. Runs `openclaw doctor` as the final “safe update” check.
9. Syncs plugins to the active channel (dev uses bundled extensions; stable/beta uses npm) and updates npm-installed plugins.

If pnpm bootstrap still fails, the updater now stops early with a package-manager-specific error instead of trying `npm run build` inside the checkout.

## `--update` shorthand

`openclaw --update` rewrites to `openclaw update` (useful for shells and launcher scripts).

## See also

- `openclaw doctor` (offers to run update first on git checkouts)

```

## File: voicecall.md
```
---
summary: "CLI reference for `openclaw voicecall` (voice-call plugin command surface)"
read_when:
  - You use the voice-call plugin and want the CLI entry points
  - You want quick examples for `voicecall call|continue|status|tail|expose`
title: "voicecall"
---

# `openclaw voicecall`

`voicecall` is a plugin-provided command. It only appears if the voice-call plugin is installed and enabled.

Primary doc:


## Common commands

```bash
openclaw voicecall status --call-id <id>
openclaw voicecall call --to "+15555550123" --message "Hello" --mode notify
openclaw voicecall continue --call-id <id> --message "Any questions?"
openclaw voicecall end --call-id <id>
```

## Exposing webhooks (Tailscale)

```bash
openclaw voicecall expose --mode serve
openclaw voicecall expose --mode funnel
openclaw voicecall expose --mode off
```

Security note: only expose the webhook endpoint to networks you trust. Prefer Tailscale Serve over Funnel when possible.

```

## File: webhooks.md
```
---
summary: "CLI reference for `openclaw webhooks` (webhook helpers + Gmail Pub/Sub)"
read_when:
  - You want to wire Gmail Pub/Sub events into OpenClaw
  - You want webhook helper commands
title: "webhooks"
---

# `openclaw webhooks`

Webhook helpers and integrations (Gmail Pub/Sub, webhook helpers).

Related:


## Gmail

```bash
openclaw webhooks gmail setup --account you@example.com
openclaw webhooks gmail run
```

### `webhooks gmail setup`

Configure Gmail watch, Pub/Sub, and OpenClaw webhook delivery.

Required:

- `--account <email>`

Options:

- `--project <id>`
- `--topic <name>`
- `--subscription <name>`
- `--label <label>`
- `--hook-url <url>`
- `--hook-token <token>`
- `--push-token <token>`
- `--bind <host>`
- `--port <port>`
- `--path <path>`
- `--include-body`
- `--max-bytes <n>`
- `--renew-minutes <n>`
- `--tailscale <funnel|serve|off>`
- `--tailscale-path <path>`
- `--tailscale-target <target>`
- `--push-endpoint <url>`
- `--json`

Examples:

```bash
openclaw webhooks gmail setup --account you@example.com
openclaw webhooks gmail setup --account you@example.com --project my-gcp-project --json
openclaw webhooks gmail setup --account you@example.com --hook-url https://gateway.example.com/hooks/gmail
```

### `webhooks gmail run`

Run `gog watch serve` plus the watch auto-renew loop.

Options:

- `--account <email>`
- `--topic <topic>`
- `--subscription <name>`
- `--label <label>`
- `--hook-url <url>`
- `--hook-token <token>`
- `--push-token <token>`
- `--bind <host>`
- `--port <port>`
- `--path <path>`
- `--include-body`
- `--max-bytes <n>`
- `--renew-minutes <n>`
- `--tailscale <funnel|serve|off>`
- `--tailscale-path <path>`
- `--tailscale-target <target>`

Example:

```bash
openclaw webhooks gmail run --account you@example.com
```

See [Gmail Pub/Sub documentation](/automation/cron-jobs#gmail-pubsub-integration) for the end-to-end setup flow and operational details.

```

## File: wiki.md
```
---
summary: "CLI reference for `openclaw wiki` (memory-wiki vault status, search, compile, lint, apply, bridge, and Obsidian helpers)"
read_when:
  - You want to use the memory-wiki CLI
  - You are documenting or changing `openclaw wiki`
title: "wiki"
---

# `openclaw wiki`

Inspect and maintain the `memory-wiki` vault.

Provided by the bundled `memory-wiki` plugin.

Related:


## What it is for

Use `openclaw wiki` when you want a compiled knowledge vault with:

- wiki-native search and page reads
- provenance-rich syntheses
- contradiction and freshness reports
- bridge imports from the active memory plugin
- optional Obsidian CLI helpers

## Common commands

```bash
openclaw wiki status
openclaw wiki doctor
openclaw wiki init
openclaw wiki ingest ./notes/alpha.md
openclaw wiki compile
openclaw wiki lint
openclaw wiki search "alpha"
openclaw wiki get entity.alpha --from 1 --lines 80

openclaw wiki apply synthesis "Alpha Summary" \
  --body "Short synthesis body" \
  --source-id source.alpha

openclaw wiki apply metadata entity.alpha \
  --source-id source.alpha \
  --status review \
  --question "Still active?"

openclaw wiki bridge import
openclaw wiki unsafe-local import

openclaw wiki obsidian status
openclaw wiki obsidian search "alpha"
openclaw wiki obsidian open syntheses/alpha-summary.md
openclaw wiki obsidian command workspace:quick-switcher
openclaw wiki obsidian daily
```

## Commands

### `wiki status`

Inspect current vault mode, health, and Obsidian CLI availability.

Use this first when you are unsure whether the vault is initialized, bridge mode
is healthy, or Obsidian integration is available.

### `wiki doctor`

Run wiki health checks and surface configuration or vault problems.

Typical issues include:

- bridge mode enabled without public memory artifacts
- invalid or missing vault layout
- missing external Obsidian CLI when Obsidian mode is expected

### `wiki init`

Create the wiki vault layout and starter pages.

This initializes the root structure, including top-level indexes and cache
directories.

### `wiki ingest <path-or-url>`

Import content into the wiki source layer.

Notes:

- URL ingest is controlled by `ingest.allowUrlIngest`
- imported source pages keep provenance in frontmatter
- auto-compile can run after ingest when enabled

### `wiki compile`

Rebuild indexes, related blocks, dashboards, and compiled digests.

This writes stable machine-facing artifacts under:

- `.openclaw-wiki/cache/agent-digest.json`
- `.openclaw-wiki/cache/claims.jsonl`

If `render.createDashboards` is enabled, compile also refreshes report pages.

### `wiki lint`

Lint the vault and report:

- structural issues
- provenance gaps
- contradictions
- open questions
- low-confidence pages/claims
- stale pages/claims

Run this after meaningful wiki updates.

### `wiki search <query>`

Search wiki content.

Behavior depends on config:

- `search.backend`: `shared` or `local`
- `search.corpus`: `wiki`, `memory`, or `all`

Use `wiki search` when you want wiki-specific ranking or provenance details.
For one broad shared recall pass, prefer `openclaw memory search` when the
active memory plugin exposes shared search.

### `wiki get <lookup>`

Read a wiki page by id or relative path.

Examples:

```bash
openclaw wiki get entity.alpha
openclaw wiki get syntheses/alpha-summary.md --from 1 --lines 80
```

### `wiki apply`

Apply narrow mutations without freeform page surgery.

Supported flows include:

- create/update a synthesis page
- update page metadata
- attach source ids
- add questions
- add contradictions
- update confidence/status
- write structured claims

This command exists so the wiki can evolve safely without manually editing
managed blocks.

### `wiki bridge import`

Import public memory artifacts from the active memory plugin into bridge-backed
source pages.

Use this in `bridge` mode when you want the latest exported memory artifacts
pulled into the wiki vault.

### `wiki unsafe-local import`

Import from explicitly configured local paths in `unsafe-local` mode.

This is intentionally experimental and same-machine only.

### `wiki obsidian ...`

Obsidian helper commands for vaults running in Obsidian-friendly mode.

Subcommands:

- `status`
- `search`
- `open`
- `command`
- `daily`

These require the official `obsidian` CLI on `PATH` when
`obsidian.useOfficialCli` is enabled.

## Practical usage guidance

- Use `wiki search` + `wiki get` when provenance and page identity matter.
- Use `wiki apply` instead of hand-editing managed generated sections.
- Use `wiki lint` before trusting contradictory or low-confidence content.
- Use `wiki compile` after bulk imports or source changes when you want fresh
  dashboards and compiled digests immediately.
- Use `wiki bridge import` when bridge mode depends on newly exported memory
  artifacts.

## Configuration tie-ins

`openclaw wiki` behavior is shaped by:

- `plugins.entries.memory-wiki.config.vaultMode`
- `plugins.entries.memory-wiki.config.search.backend`
- `plugins.entries.memory-wiki.config.search.corpus`
- `plugins.entries.memory-wiki.config.bridge.*`
- `plugins.entries.memory-wiki.config.obsidian.*`
- `plugins.entries.memory-wiki.config.render.*`
- `plugins.entries.memory-wiki.config.context.includeCompiledDigestPrompt`

See [Memory Wiki plugin](/plugins/memory-wiki) for the full config model.

```

## File: _DIR_IDENTITY.md
```
---
entity_type: "agent"
domain: "knowledge"
classification: "cli"
parent_system: "oma"
---

# cli

**Identity**: `cli`
**Domain**: knowledge
**Clearance**: Level 3

Generated automatically via Phoenix V3 Pipeline.

```

## File: __init__.py
```

```

## File: __pycache__\_DIR_IDENTITY.md
```
---
id: brain-knowledge-repo_orphan_sweep_cli-__pycache__
name:   Pycache  
path: brain/knowledge/repo_orphan_sweep_cli/__pycache__
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

#   Pycache  
Storage area for '__pycache__' domain.
> Auto-generated identity tag by OMA v2.1.

```


---
id: openzalo
type: knowledge
owner: OA_Triage
---
# openzalo
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@tuyenhx/openzalo",
  "version": "2026.3.31",
  "description": "OpenClaw OpenZalo channel plugin (personal account via openzca CLI)",
  "type": "module",
  "scripts": {
    "manifest:channel-schema:sync": "node --import tsx ./scripts/sync-manifest-channel-config.ts",
    "manifest:channel-schema:check": "node --import tsx ./scripts/sync-manifest-channel-config.ts --check",
    "test": "npm run manifest:channel-schema:check && node --import tsx --test src/*.test.ts src/**/*.test.ts"
  },
  "dependencies": {
    "zod": "^4.3.6"
  },
  "devDependencies": {
    "tsx": "^4.20.5"
  },
  "peerDependencies": {
    "openclaw": ">=2026.3.23"
  },
  "peerDependenciesMeta": {
    "openclaw": {
      "optional": true
    }
  },
  "openclaw": {
    "extensions": [
      "./index.ts"
    ],
    "setupEntry": "./setup-entry.ts",
    "channel": {
      "id": "openzalo",
      "label": "OpenZalo",
      "selectionLabel": "OpenZalo (personal account)",
      "detailLabel": "OpenZalo",
      "docsPath": "/channels/openzalo",
      "docsLabel": "openzalo",
      "blurb": "Personal Zalo account integration via openzca CLI.",
      "aliases": [
        "ozl",
        "zlu",
        "zalo-personal"
      ],
      "systemImage": "message",
      "order": 80,
      "quickstartAllowFrom": true
    },
    "install": {
      "npmSpec": "@tuyenhx/openzalo",
      "localPath": "extensions/openzalo",
      "defaultChoice": "npm",
      "minHostVersion": ">=2026.3.23"
    },
    "release": {
      "publishToNpm": true
    }
  }
}

```

### File: README.md
```md
# @tuyenhx/openzalo

OpenClaw channel plugin for Zalo personal accounts via `openzca` CLI.

> Warning: this is an unofficial personal-account automation integration. Use at your own risk.

## AI Install Metadata

- Plugin id: `openzalo`
- Channel id: `openzalo`
- Package name: `@tuyenhx/openzalo`
- Required external binary: `openzca`
- Optional external binary for `/acp` support: `acpx`

## Bundled Skills

This plugin now bundles one optional skill (auto-discovered from `./skills`):

- `openzca`: advanced `openzca` CLI workflows, with DB-backed reads for summaries, history, and search.

### Owner/Admin Usage Guidance for `openzca` Skill

`openzca` is installed at workspace/plugin level, not per-sender.  
So "owner-only" should be enforced by runtime policy, not by skill installation.

Recommended setup:

1. Keep general agents on `tools.profile: "messaging"` (no `exec`).
2. Grant `exec` only to a dedicated admin agent.
3. In OpenZalo group config, use `allowFrom` + `skills` filter to expose advanced skills only in admin-controlled groups.
4. Use normal OpenZalo `message` actions for routine operations; use the bundled `openzca` skill when you want the full playbook or raw CLI workflows.

## Prerequisites

- OpenClaw Gateway is installed and running.
- `openzca` is installed and available in `PATH` (or configure `channels.openzalo.zcaBinary`).
- If you want OpenZalo ACP-local sessions via `/acp`, install `acpx` too.
- You can authenticate with your Zalo account on the gateway machine.

Example direct login with `openzca`:

```bash
openzca --profile default auth login
```

Example `acpx` install for `/acp` support:

```bash
npm i -g acpx
```

Verify:

```bash
which acpx
acpx --help
```

## Install (npm)

Use this after `@tuyenhx/openzalo` is published:

```bash
openclaw plugins install @tuyenhx/openzalo
```

To force ClawHub as the source once the package is listed there:

```bash
openclaw plugins install clawhub:@tuyenhx/openzalo
```

## Install (local checkout)

From the OpenClaw repo root:

```bash
openclaw plugins install ./extensions/openzalo
```

Or from this plugin directory:

```bash
openclaw plugins install .
```

Restart Gateway after installation.

## Publishing Notes

- OpenClaw plugin installs can resolve from ClawHub or npm.
- Newer `clawhub` CLI builds can publish native plugin packages with `clawhub package publish`.
- To distribute this plugin, publish the package itself; users can then install it with `openclaw plugins install @tuyenhx/openzalo` or `openclaw plugins install clawhub:@tuyenhx/openzalo` when available there.
- The bundled `skills/openzca` skill can be published separately with the `clawhub` CLI if you want it discoverable as a standalone skill too.

## Quick Start

1. Login account for this channel:

```bash
openclaw channels login --channel openzalo
# optional multi-account
openclaw channels login --channel openzalo --account work
```

2. Add channel config:

```json5
{
  channels: {
    openzalo: {
      enabled: true,
      profile: "default",
      dmPolicy: "pairing",
      groupPolicy: "allowlist",
      groupAllowFrom: ["<GROUP_ID>"],
    },
  },
}
```

Or via CLI:

```bash
openclaw channels add --channel openzalo --account default
```

3. Send test message:

```bash
openclaw message send --channel openzalo --target <userId> --message "Hello from OpenClaw"
openclaw message send --channel openzalo --target group:<groupId> --message "Hello group"
openclaw message send --channel openzalo --target group:<groupId> --message "Hi @Alice Nguyen and @123456789"
```

For group sends, plain `@Name` and `@userId` are forwarded to `openzca` and become native Zalo mentions.
For native mentions, do not guess. Only tag when you already have an exact unique member id or name from context or from the user.

## ACPX (`/acp`) Support

This plugin can bind the current OpenZalo conversation to a local ACPX session without changing OpenClaw core.

Install `acpx` first:

```bash
npm i -g acpx
```

If the gateway service cannot see your shell `PATH`, set `channels.openzalo.acpx.command` to the absolute path from `which acpx`.

Example config:

```json5
{
  channels: {
    openzalo: {
      acpx: {
        enabled: true,
        command: "/full/path/to/acpx", // or "acpx" if PATH is correct
        agent: "claude", // e.g. claude | codex
        cwd: "/Users/<you>/.openclaw/workspace",
        permissionMode: "approve-all", // approve-all | approve-reads | deny-all
        nonInteractivePermissions: "fail", // fail | deny
      },
    },
  },
}
```

Notes:

- `agent` is the ACPX agent id. For Claude Code, use `claude`. For Codex, use `codex`.
- `cwd` is the working directory ACPX will use for that conversation.
- `command` should be an absolute path if `/acp on` reports `acpx command not found`.

Supported OpenZalo ACP commands:

```text
/acp status
/acp on
/acp on claude cwd=/Users/<you>/.openclaw/workspace
/acp reset
/acp off
```

Behavior:

- `/acp on` binds the current conversation to a persistent ACPX session.
- `/acp status` shows whether the conversation is bound and reports session status.
- `/acp reset` recreates the ACPX session for the current conversation.
- `/acp off` unbinds the conversation and closes the ACPX session.

## Configuration

```json5
{
  channels: {
    openzalo: {
      enabled: true,
      profile: "default", // default: account id
      zcaBinary: "openzca", // or full path
      acpx: {
        enabled: true,
        command: "/full/path/to/acpx", // or "acpx" if PATH is correct
        agent: "claude", // e.g. claude | codex
        cwd: "/Users/<you>/.openclaw/workspace",
        permissionMode: "approve-all", // approve-all | approve-reads | deny-all
        nonInteractivePermissions: "fail", // fail | deny
      },

      // DM access: pairing | allowlist | open | disabled
      dmPolicy: "pairing",
      allowFrom: ["<OWNER_USER_ID>"],

      // Group access: allowlist | open | disabled
      groupPolicy: "allowlist",
      groupAllowFrom: ["<GROUP_ID>"],

      // Optional per-group overrides
      groups: {
        "<GROUP_ID>": {
          enabled: true,
          requireMention: true, // default true
          allowFrom: ["<ALLOWED_SENDER_ID>"],
          tools: {
            allow: ["group:messaging"],
            deny: ["group:fs", "group:runtime"],
          },
          toolsBySender: {
            "<OWNER_USER_ID>": { allow: ["group:runtime", "group:fs"] },
          },
          skills: ["skill-id"],
          systemPrompt: "Custom prompt for this group.",
        },
      },

      historyLimit: 12,
      dmHistoryLimit: 12, // optional (schema-supported)
      textChunkLimit: 1800,
      chunkMode: "length", // length | newline
      blockStreaming: false,
      mediaMaxMb: 25, // optional (schema-supported)
      markdown: {}, // optional (schema-supported)

      mediaLocalRoots: [
        "/Users/<you>/.openclaw/workspace",
        "/Users/<you>/.openclaw/media",
      ],
      sendTypingIndicators: true,

      threadBindings: {
        enabled: true,
        spawnSubagentSessions: true,
        ttlHours: 24,
      },

      actions: {
        reactions: true,
        messages: true, // read/edit/unsend
        groups: true, // rename/add/remove/leave
        pins: true, // pin/unpin/list-pins
        memberInfo: true, // member-info
        groupMembers: true, // reserved
      },
    },
  },
}
```

## Multi-Account

`channels.openzalo.accounts.<accountId>` overrides top-level fields:

```yaml
channels:
  openzalo:
    enabled: true
    defaultAccount: default
    accounts:
      default:
        profile: default
        acpx:
          enabled: true
          command: /full/path/to/acpx
          agent: claude
          cwd: /Users/<you>/.openclaw/workspace
      work:
        profile: work
        enabled: true
```

Profile resolution is per account. If `zcaBinary` is not set, plugin uses:

1. `channels.openzalo[.accounts.<id>].zcaBinary`
2. `OPENZCA_BINARY` env var
3. `openzca`

If `acpx` is not set, OpenZalo ACP-local uses:

1. `channels.openzalo[.accounts.<id>].acpx.command`
2. `OPENZALO_ACPX_COMMAND` env var
3. `acpx`

## Target Format

- DM target: `<userId>`
- Group target: `group:<groupId>`
- Also accepted for groups: `g-<groupId>`, `g:<groupId>`
- Also accepted for DM/user targets: `user:<userId>`, `dm:<userId>`, `u:<userId>`, `u-<userId>`
- Channel prefixes like `openzalo:<target>` and `ozl:<target>` are normalized automatically.
- Legacy `zlu:<target>` remains accepted for backward compatibility.

Use `group:` for explicit group sends.

## Notes

- Inbound listener uses `openzca listen --raw --supervised` so OpenZalo owns restart policy and receives lifecycle heartbeats.
- Group messages require mention by default (`requireMention: true`) unless overridden.
- Authorized slash/bang control commands can still be processed in groups when access policy allows.
- Pairing mode sends approval code for unknown DM senders.
- Subagent session binding controls use `channels.openzalo.threadBindings.*` (or per-account overrides).
- Local media is restricted to allowed roots for safety.

Default safe media roots (under `OPENCLAW_STATE_DIR` or `CLAWDBOT_STATE_DIR`, fallback `~/.openclaw`):

- `workspace`
- `media`
- `agents`
- `sandboxes`

## Troubleshooting

- `openzca not found`: install `openzca` or set `channels.openzalo.zcaBinary`.
- `acpx command not found`: install `acpx` (for example `npm i -g acpx`) or set `channels.openzalo.acpx.command` to the absolute `acpx` path.
- Auth check fails: run `openclaw channels login --channel openzalo` (or `openzca --profile <id> auth login`).
- Group message dropped: verify `groupPolicy`, `groupAllowFrom`, and `groups.<groupId>` allowlist.
- Group message dropped with allowlist configured: check `requireMention` and mention detection.
- Local media blocked: add absolute paths to `channels.openzalo.mediaLocalRoots`.

```

### File: api.ts
```ts
import type {
  ChannelAccountSnapshot,
  ChannelMessageActionAdapter,
  ChannelMessageActionName,
  ChannelPlugin,
  OpenClawConfig,
  OpenClawPluginApi,
  PluginRuntime,
  ReplyPayload,
  RuntimeEnv,
} from "openclaw/plugin-sdk";
import type { WizardPrompter } from "openclaw/plugin-sdk";

export type {
  ChannelAccountSnapshot,
  ChannelMessageActionAdapter,
  ChannelMessageActionName,
  ChannelPlugin,
  OpenClawConfig,
  OpenClawPluginApi,
  PluginRuntime,
  ReplyPayload,
  RuntimeEnv,
  WizardPrompter,
};

export type BaseProbeResult<TLastError = string> = {
  ok: boolean;
  status: "ok" | "error";
  lastError?: TLastError | null;
};

export type ChannelStatusIssue = {
  channel: string;
  accountId?: string;
  kind: "config" | "runtime" | string;
  message: string;
  fix?: string;
};
export type ChannelAccountState =
  | "linked"
  | "not linked"
  | "configured"
  | "not configured"
  | "enabled"
  | "disabled";
export type BlockStreamingCoalesceConfig = {
  minChars?: number;
  maxChars?: number;
  idleMs?: number;
};
export type MarkdownTableMode = "off" | "bullets" | "code";
export type MarkdownConfig = {
  tables?: MarkdownTableMode;
};
export type DmConfig = {
  historyLimit?: number;
};
export type DmPolicy = "pairing" | "allowlist" | "open" | "disabled";
export type GroupPolicy = "open" | "disabled" | "allowlist";
export type GroupToolPolicyConfig = {
  allow?: string[];
  alsoAllow?: string[];
  deny?: string[];
};
export type GroupToolPolicyBySenderConfig = Record<string, GroupToolPolicyConfig>;
export type ChannelSetupDmPolicy = {
  label: string;
  channel: string;
  policyKey: string;
  allowFromKey: string;
  getCurrent: (cfg: OpenClawConfig) => DmPolicy;
  setPolicy: (cfg: OpenClawConfig, policy: DmPolicy) => OpenClawConfig;
  promptAllowFrom?: (params: {
    cfg: OpenClawConfig;
    prompter: WizardPrompter;
    accountId?: string;
  }) => Promise<OpenClawConfig>;
};

type ZodSchemaWithToJsonSchema = {
  toJSONSchema?: (params?: Record<string, unknown>) => unknown;
};

type OpenClawPluginDefinition = {
  id?: string;
  name?: string;
  description?: string;
  version?: string;
  configSchema?: { schema: Record<string, unknown> };
  register?: (api: OpenClawPluginApi) => void | Promise<void>;
};

type StringParamOptions = {
  required?: boolean;
  trim?: boolean;
  label?: string;
  allowEmpty?: boolean;
};

type ToolInputErrorLike = Error & { status?: number };

export const DEFAULT_ACCOUNT_ID = "default";
export const PAIRING_APPROVED_MESSAGE =
  "✅ OpenClaw access approved. Send a message to start chatting.";
const DOCS_ROOT = "https://docs.openclaw.ai";

function createToolInputError(message: string): ToolInputErrorLike {
  const error = new Error(message) as ToolInputErrorLike;
  error.name = "ToolInputError";
  error.status = 400;
  return error;
}

function toSnakeCaseKey(key: string): string {
  return key
    .replace(/([A-Z]+)([A-Z][a-z])/g, "$1_$2")
    .replace(/([a-z0-9])([A-Z])/g, "$1_$2")
    .toLowerCase();
}

function readParamRaw(params: Record<string, unknown>, key: string): unknown {
  if (Object.hasOwn(params, key)) {
    return params[key];
  }
  const snakeKey = toSnakeCaseKey(key);
  if (snakeKey !== key && Object.hasOwn(params, snakeKey)) {
    return params[snakeKey];
  }
  return undefined;
}

type ChannelSectionBase = {
  name?: string;
  defaultAccount?: string;
  accounts?: Record<string, Record<string, unknown>>;
};

type ChannelSection = {
  accounts?: Record<string, Record<string, unknown>>;
  enabled?: boolean;
};

function normalizeCanonicalAccountId(value: string): string {
  return value.trim().toLowerCase().replace(/[^a-z0-9_-]+/g, "-").replace(/^-+|-+$/g, "");
}

export function normalizeAccountId(value: string | undefined | null): string {
  const trimmed = String(value ?? "").trim();
  if (!trimmed) {
    return DEFAULT_ACCOUNT_ID;
  }
  return normalizeCanonicalAccountId(trimmed) || DEFAULT_ACCOUNT_ID;
}

function channelHasAccounts(cfg: OpenClawConfig, channelKey: string): boolean {
  const channels = cfg.channels as Record<string, unknown> | undefined;
  const base = channels?.[channelKey] as ChannelSectionBase | undefined;
  return Boolean(base?.accounts && Object.keys(base.accounts).length > 0);
}

function shouldStoreNameInAccounts(params: {
  cfg: OpenClawConfig;
  channelKey: string;
  accountId: string;
  alwaysUseAccounts?: boolean;
}): boolean {
  if (params.alwaysUseAccounts) {
    return true;
  }
  if (params.accountId !== DEFAULT_ACCOUNT_ID) {
    return true;
  }
  return channelHasAccounts(params.cfg, params.channelKey);
}

export function buildChannelConfigSchema(schema: ZodSchemaWithToJsonSchema): {
  schema: Record<string, unknown>;
} {
  if (typeof schema?.toJSONSchema === "function") {
    return {
      schema: schema.toJSONSchema({
        target: "draft-07",
        unrepresentable: "any",
      }) as Record<string, unknown>,
    };
  }
  return {
    schema: {
      type: "object",
      additionalProperties: true,
    },
  };
}

export function defineChannelPluginEntry<TPlugin>(params: {
  id: string;
  name: string;
  description: string;
  plugin: TPlugin;
  configSchema?: { schema: Record<string, unknown> };
  setRuntime?: (runtime: PluginRuntime) => void;
  registerFull?: (api: OpenClawPluginApi) => void;
}): OpenClawPluginDefinition {
  return {
    id: params.id,
    name: params.name,
    description: params.description,
    ...(params.configSchema ? { configSchema: params.configSchema } : {}),
    register(api) {
      params.setRuntime?.(api.runtime);
      api.registerChannel({ plugin: params.plugin as ChannelPlugin });
      if (api.registrationMode !== "full") {
        return;
      }
      params.registerFull?.(api);
    },
  };
}

export function defineSetupPluginEntry<TPlugin>(plugin: TPlugin) {
  return { plugin };
}

export function applyAccountNameToChannelSection(params: {
  cfg: OpenClawConfig;
  channelKey: string;
  accountId: string;
  name?: string;
  alwaysUseAccounts?: boolean;
}): OpenClawConfig {
  const trimmed = params.name?.trim();
  if (!trimmed) {
    return params.cfg;
  }
  const accountId = normalizeAccountId(params.accountId);
  const channels = params.cfg.channels as Record<string, unknown> | undefined;
  const baseConfig = channels?.[params.channelKey];
  const base =
    typeof baseConfig === "object" && baseConfig ? (baseConfig as ChannelSectionBase) : undefined;
  const useAccounts = shouldStoreNameInAccounts({
    cfg: params.cfg,
    channelKey: params.channelKey,
    accountId,
    alwaysUseAccounts: params.alwaysUseAccounts,
  });
  if (!useAccounts && accountId === DEFAULT_ACCOUNT_ID) {
    const safeBase = base ?? {};
    return {
      ...params.cfg,
      channels: {
        ...params.cfg.channels,
        [params.channelKey]: {
          ...safeBase,
          name: trimmed,
        },
      },
    } as OpenClawConfig;
  }
  const baseAccounts: Record<string, Record<string, unknown>> = base?.accounts ?? {};
  const existingAccount = baseAccounts[accountId] ?? {};
  const baseWithoutName =
    accountId === DEFAULT_ACCOUNT_ID
      ? (({ name: _ignored, ...rest }) => rest)(base ?? {})
      : (base ?? {});
  return {
    ...params.cfg,
    channels: {
      ...params.cfg.channels,
      [params.channelKey]: {
        ...baseWithoutName,
        accounts: {
          ...baseAccounts,
          [accountId]: {
            ...existingAccount,
            name: trimmed,
          },
        },
      },
    },
  } as OpenClawConfig;
}

export function migrateBaseNameToDefaultAccount(params: {
  cfg: OpenClawConfig;
  channelKey: string;
  alwaysUseAccounts?: boolean;
}): OpenClawConfig {
  if (params.alwaysUseAccounts) {
    return params.cfg;
  }
  const channels = params.cfg.channels as Record<string, unknown> | undefined;
  const base = channels?.[params.channelKey] as ChannelSectionBase | undefined;
  const baseName = base?.name?.trim();
  if (!baseName) {
    return params.cfg;
  }
  const accounts: Record<string, Record<string, unknown>> = {
    ...base?.accounts,
  };
  const defaultAccount = accounts[DEFAULT_ACCOUNT_ID] ?? {};
  if (!defaultAccount.name) {
    accounts[DEFAULT_ACCOUNT_ID] = { ...defaultAccount, name: baseName };
  }
  const { name: _ignored, ...rest } = base ?? {};
  return {
    ...params.cfg,
    channels: {
      ...params.cfg.channels,
      [params.channelKey]: {
        ...rest,
        accounts,
      },
    },
  } as OpenClawConfig;
}

export function setAccountEnabledInConfigSection(params: {
  cfg: OpenClawConfig;
  sectionKey: string;
  accountId: string;
  enabled: boolean;
  allowTopLevel?: boolean;
}): OpenClawConfig {
  const accountKey = params.accountId || DEFAULT_ACCOUNT_ID;
  const channels = params.cfg.channels as Record<string, unknown> | undefined;
  const base = channels?.[params.sectionKey] as ChannelSection | undefined;
  const hasAccounts = Boolean(base?.accounts);
  if (params.allowTopLevel && accountKey === DEFAULT_ACCOUNT_ID && !hasAccounts) {
    return {
      ...params.cfg,
      channels: {
        ...params.cfg.channels,
        [params.sectionKey]: {
          ...base,
          enabled: params.enabled,
        },
      },
    } as OpenClawConfig;
  }

  const baseAccounts = base?.accounts ?? {};
  const existing = baseAccounts[accountKey] ?? {};
  return {
    ...params.cfg,
    channels: {
      ...params.cfg.channels,
      [params.sectionKey]: {
        ...base,
        accounts: {
          ...baseAccounts,
          [accountKey]: {
            ...existing,
            enabled: params.enabled,
          },
        },
      },
    },
  } as OpenClawConfig;
}

export function deleteAccountFromConfigSection(params: {
  cfg: OpenClawConfig;
  sectionKey: string;
  accountId: string;
  clearBaseFields?: string[];
}): OpenClawConfig {
  const accountKey = params.accountId || DEFAULT_ACCOUNT_ID;
  const channels = params.cfg.channels as Record<string, unknown> | undefined;
  const base = channels?.[params.sectionKey] as ChannelSection | undefined;
  if (!base) {
    return params.cfg;
  }

  const baseAccounts =
    base.accounts && typeof base.accounts === "object" ? { ...base.accounts } : undefined;

  if (accountKey !== DEFAULT_ACCOUNT_ID) {
    const accounts = baseAccounts ? { ...baseAccounts } : {};
    delete accounts[accountKey];
    return {
      ...params.cfg,
      channels: {
        ...params.cfg.channels,
        [params.sectionKey]: {
          ...base,
          accounts: Object.keys(accounts).length ? accounts : undefined,
        },
      },
    } as OpenClawConfig;
  }

  if (baseAccounts && Object.keys(baseAccounts).length > 0) {
    delete baseAccounts[accountKey];
    const baseRecord = { ...(base as Record<string, unknown>) };
    for (const field of params.clearBaseFields ?? []) {
      if (field in baseRecord) {
        baseRecord[field] = undefined;
      }
    }
    return {
      ...params.cfg,
      channels: {
        ...params.cfg.channels,
        [params.sectionKey]: {
          ...baseRecord,
          accounts: Object.keys(baseAccounts).length ? baseAccounts : undefined,
        },
      },
    } as OpenClawConfig;
  }

  const nextChannels = { ...params.cfg.channels } as Record<string, unknown>;
  delete nextChannels[params.sectionKey];
  const nextCfg = { ...params.cfg } as OpenClawConfig;
  if (Object.keys(nextChannels).length > 0) {
    nextCfg.channels = nextChannels as OpenClawConfig["channels"];
  } else {
    delete nextCfg.channels;
  }
  return nextCfg;
}

export function formatPairingApproveHint(channelId: string): string {
  return `Approve via: openclaw pairing list ${channelId} / openclaw pairing approve ${channelId} <code>`;
}

export function addWildcardAllowFrom(allowFrom?: Array<string | number> | null): string[] {
  const next = (allowFrom ?? []).map((v) => String(v).trim()).filter(Boolean);
  if (!next.includes("*")) {
    next.push("*");
  }
  return next;
}

export function mergeAllowFromEntries(
  current: Array<string | number> | null | undefined,
  additions: Array<string | number>,
): string[] {
  const merged = [...(current ?? []), ...additions].map((v) => String(v).trim()).filter(Boolean);
  return [...new Set(merged)];
}

export function formatDocsLink(path: string, label?: string): string {
  const trimmed = path.trim();
  const url = trimmed.startsWith("http")
    ? trimmed
    : `${DOCS_ROOT}${trimmed.startsWith("/") ? trimmed : `/${trimmed}`}`;
  return label ? `${label}: ${url}` : url;
}

export async function promptAccountId(params: {
  cfg: OpenClawConfig;
  prompter: WizardPrompter;
  label: string;
  currentId?: string;
  listAccountIds: (cfg: OpenClawConfig) => string[];
  defaultAccountId?: string;
}): Promise<string> {
  const existingIds = params.listAccountIds(params.cfg);
  const initial = params.currentId?.trim() || params.defaultAccountId || DEFAULT_ACCOUNT_ID;
  const choice = await params.prompter.select({
    message: `${params.label} account`,
    options: [
      ...existingIds.map((id) => ({
        value: id,
        label: id === DEFAULT_ACCOUNT_ID ? "default (primary)" : id,
      })),
      { value: "__new__", label: "Add a new account" },
    ],
    initialValue: initial,
  });

  if (choice !== "__new__") {
    return normalizeAccountId(choice);
  }

  const entered = await params.prompter.text({
    message: `New ${params.label} account id`,
    validate: (value) => (value?.trim() ? undefined : "Required"),
  });
  const normalized = normalizeAccountId(String(entered));
  if (String(entered).trim() !== normalized) {
    await params.prompter.note(
      `Normalized account id to "${normalized}".`,
      `${params.label} account`,
    );
  }
  return normalized;
}

export function readStringParam(
  params: Record<string, unknown>,
  key: string,
  options: StringParamOptions & { required: true },
): string;
export function readStringParam(
  params: Record<string, unknown>,
  key: string,
  options?: StringParamOptions,
): string | undefined;
export function readStringParam(
  params: Record<string, unknown>,
  key: string,
  options: StringParamOptions = {},
) {
  const { required = false, trim = true, label = key, allowEmpty = false } = options;
  const raw = readParamRaw(params, key);
  if (typeof raw !== "string") {
    if (required) {
      throw createToolInputError(`${label} required`);
    }
    return undefined;
  }
  const value = trim ? raw.trim() : raw;
  if (!value && !allowEmpty) {
    if (required) {
      throw createToolInputError(`${label} required`);
    }
    return undefined;
  }
  return value;
}

export function readNumberParam(
  params: Record<string, unknown>,
  key: string,
  options: { required?: boolean; label?: string; integer?: boolean; strict?: boolean } = {},
): number | undefined {
  const { required = false, label = key, integer = false, strict = false } = options;
  const raw = readParamRaw(params, key);
  let value: number | undefined;
  if (typeof raw === "number" && Number.isFinite(raw)) {
  
... [TRUNCATED]
```

### File: index.ts
```ts
import { defineChannelPluginEntry } from "openclaw/plugin-sdk/core";
import { openzaloPlugin } from "./src/channel.js";
import { setOpenzaloRuntime } from "./src/runtime.js";
import { registerOpenzaloSubagentHooks } from "./src/subagent-hooks.js";

export default defineChannelPluginEntry({
  id: "openzalo",
  name: "OpenZalo",
  description: "OpenZalo channel plugin (personal account via openzca CLI)",
  plugin: openzaloPlugin,
  setRuntime: setOpenzaloRuntime,
  registerFull(api) {
    registerOpenzaloSubagentHooks(api);
  },
});

```

### File: openclaw.plugin.json
```json
{
  "id": "openzalo",
  "channels": [
    "openzalo"
  ],
  "channelConfigs": {
    "openzalo": {
      "label": "OpenZalo",
      "description": "Personal Zalo account integration via openzca CLI.",
      "schema": {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "enabled": {
            "type": "boolean"
          },
          "profile": {
            "type": "string"
          },
          "zcaBinary": {
            "type": "string"
          },
          "acpx": {
            "type": "object",
            "properties": {
              "enabled": {
                "type": "boolean"
              },
              "command": {
                "type": "string"
              },
              "agent": {
                "type": "string"
              },
              "cwd": {
                "type": "string"
              },
              "timeoutSeconds": {
                "type": "number",
                "exclusiveMinimum": 0
              },
              "permissionMode": {
                "type": "string",
                "enum": [
                  "approve-all",
                  "approve-reads",
                  "deny-all"
                ]
              },
              "nonInteractivePermissions": {
                "type": "string",
                "enum": [
                  "deny",
                  "fail"
                ]
              }
            },
            "additionalProperties": false
          },
          "markdown": {
            "type": "object",
            "properties": {
              "tables": {
                "type": "string",
                "enum": [
                  "off",
                  "bullets",
                  "code"
                ]
              }
            },
            "additionalProperties": false
          },
          "dmPolicy": {
            "type": "string",
            "enum": [
              "pairing",
              "allowlist",
              "open",
              "disabled"
            ]
          },
          "allowFrom": {
            "type": "array",
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "number"
                }
              ]
            }
          },
          "groupPolicy": {
            "type": "string",
            "enum": [
              "open",
              "disabled",
              "allowlist"
            ]
          },
          "groupAllowFrom": {
            "type": "array",
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "number"
                }
              ]
            }
          },
          "groups": {
            "type": "object",
            "properties": {},
            "additionalProperties": {
              "type": "object",
              "properties": {
                "enabled": {
                  "type": "boolean"
                },
                "requireMention": {
                  "type": "boolean"
                },
                "allowFrom": {
                  "type": "array",
                  "items": {
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "number"
                      }
                    ]
                  }
                },
                "tools": {
                  "type": "object",
                  "properties": {
                    "allow": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    },
                    "alsoAllow": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    },
                    "deny": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    }
                  },
                  "additionalProperties": false
                },
                "toolsBySender": {
                  "type": "object",
                  "propertyNames": {
                    "type": "string"
                  },
                  "additionalProperties": {
                    "type": "object",
                    "properties": {
                      "allow": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "alsoAllow": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "deny": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      }
                    },
                    "additionalProperties": false
                  }
                },
                "skills": {
                  "type": "array",
                  "items": {
                    "type": "string"
                  }
                },
                "systemPrompt": {
                  "type": "string"
                }
              },
              "additionalProperties": false
            }
          },
          "historyLimit": {
            "type": "integer",
            "minimum": 0,
            "maximum": 9007199254740991
          },
          "dmHistoryLimit": {
            "type": "integer",
            "minimum": 0,
            "maximum": 9007199254740991
          },
          "textChunkLimit": {
            "type": "integer",
            "exclusiveMinimum": 0,
            "maximum": 9007199254740991
          },
          "chunkMode": {
            "type": "string",
            "enum": [
              "length",
              "newline"
            ]
          },
          "blockStreaming": {
            "type": "boolean"
          },
          "mediaMaxMb": {
            "type": "integer",
            "exclusiveMinimum": 0,
            "maximum": 9007199254740991
          },
          "mediaLocalRoots": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "sendTypingIndicators": {
            "type": "boolean"
          },
          "threadBindings": {
            "type": "object",
            "properties": {
              "enabled": {
                "type": "boolean"
              },
              "spawnSubagentSessions": {
                "type": "boolean"
              },
              "ttlHours": {
                "type": "number",
                "minimum": 0
              }
            },
            "additionalProperties": false
          },
          "actions": {
            "type": "object",
            "properties": {
              "reactions": {
                "default": true,
                "type": "boolean"
              },
              "messages": {
                "default": true,
                "type": "boolean"
              },
              "groups": {
                "default": true,
                "type": "boolean"
              },
              "pins": {
                "default": true,
                "type": "boolean"
              },
              "memberInfo": {
                "default": true,
                "type": "boolean"
              },
              "groupMembers": {
                "default": true,
                "type": "boolean"
              }
            },
            "required": [
              "reactions",
              "messages",
              "groups",
              "pins",
              "memberInfo",
              "groupMembers"
            ],
            "additionalProperties": false
          },
          "accounts": {
            "type": "object",
            "properties": {},
            "additionalProperties": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "enabled": {
                  "type": "boolean"
                },
                "profile": {
                  "type": "string"
                },
                "zcaBinary": {
                  "type": "string"
                },
                "acpx": {
                  "type": "object",
                  "properties": {
                    "enabled": {
                      "type": "boolean"
                    },
                    "command": {
                      "type": "string"
                    },
                    "agent": {
                      "type": "string"
                    },
                    "cwd": {
                      "type": "string"
                    },
                    "timeoutSeconds": {
                      "type": "number",
                      "exclusiveMinimum": 0
                    },
                    "permissionMode": {
                      "type": "string",
                      "enum": [
                        "approve-all",
                        "approve-reads",
                        "deny-all"
                      ]
                    },
                    "nonInteractivePermissions": {
                      "type": "string",
                      "enum": [
                        "deny",
                        "fail"
                      ]
                    }
                  },
                  "additionalProperties": false
                },
                "markdown": {
                  "type": "object",
                  "properties": {
                    "tables": {
                      "type": "string",
                      "enum": [
                        "off",
                        "bullets",
                        "code"
                      ]
                    }
                  },
                  "additionalProperties": false
                },
                "dmPolicy": {
                  "type": "string",
                  "enum": [
                    "pairing",
                    "allowlist",
                    "open",
                    "disabled"
                  ]
                },
                "allowFrom": {
                  "type": "array",
                  "items": {
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "number"
                      }
                    ]
                  }
                },
                "groupPolicy": {
                  "type": "string",
                  "enum": [
                    "open",
                    "disabled",
                    "allowlist"
                  ]
                },
                "groupAllowFrom": {
                  "type": "array",
                  "items": {
                    "anyOf": [
                      {
                        "type": "string"
                      },
                      {
                        "type": "number"
                      }
                    ]
                  }
                },
                "groups": {
                  "type": "object",
                  "properties": {},
                  "additionalProperties": {
                    "type": "object",
                    "properties": {
                      "enabled": {
                        "type": "boolean"
                      },
                      "requireMention": {
                        "type": "boolean"
                      },
                      "allowFrom": {
                        "type": "array",
                        "items": {
                          "anyOf": [
                            {
                              "type": "string"
                            },
                            {
                              "type": "number"
                            }
                          ]
                        }
                      },
                      "tools": {
                        "type": "object",
                        "properties": {
                          "allow": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "alsoAllow": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          },
                          "deny": {
                            "type": "array",
                            "items": {
                              "type": "string"
                            }
                          }
                        },
                        "additionalProperties": false
                      },
                      "toolsBySender": {
                        "type": "object",
                        "propertyNames": {
                          "type": "string"
                        },
                        "additionalProperties": {
                          "type": "object",
                          "properties": {
                            "allow": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            },
                            "alsoAllow": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            },
                            "deny": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            }
                          },
                          "additionalProperties": false
                        }
                      },
                      "skills": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "systemPrompt": {
                        "type": "string"
                      }
                    },
                    "additionalProperties": false
                  }
                },
                "historyLimit": 
... [TRUNCATED]
```

### File: package-lock.json
```json
{
  "name": "@tuyenhx/openzalo",
  "version": "2026.3.31",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "@tuyenhx/openzalo",
      "version": "2026.3.31",
      "dependencies": {
        "zod": "^4.3.6"
      },
      "devDependencies": {
        "tsx": "^4.20.5"
      },
      "peerDependencies": {
        "openclaw": ">=2026.3.23"
      },
      "peerDependenciesMeta": {
        "openclaw": {
          "optional": true
        }
      }
    },
    "node_modules/@esbuild/aix-ppc64": {
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/aix-ppc64/-/aix-ppc64-0.27.3.tgz",
      "integrity": "sha512-9fJMTNFTWZMh5qwrBItuziu834eOCUcEqymSH7pY+zoMVEZg3gcPuBNxH1EvfVYe9h0x/Ptw8KBzv7qxb7l8dg==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.27.3.tgz",
      "integrity": "sha512-i5D1hPY7GIQmXlXhs2w8AWHhenb00+GxjxRncS2ZM7YNVGNfaMxgzSGuO8o8SJzRc/oZwU2bcScvVERk03QhzA==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.27.3.tgz",
      "integrity": "sha512-YdghPYUmj/FX2SYKJ0OZxf+iaKgMsKHVPF1MAq/P8WirnSpCStzKJFjOjzsW0QQ7oIAiccHdcqjbHmJxRb/dmg==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.27.3.tgz",
      "integrity": "sha512-IN/0BNTkHtk8lkOM8JWAYFg4ORxBkZQf9zXiEOfERX/CzxW3Vg1ewAhU7QSWQpVIzTW+b8Xy+lGzdYXV6UZObQ==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.27.3.tgz",
      "integrity": "sha512-Re491k7ByTVRy0t3EKWajdLIr0gz2kKKfzafkth4Q8A5n1xTHrkqZgLLjFEHVD+AXdUGgQMq+Godfq45mGpCKg==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.27.3.tgz",
      "integrity": "sha512-vHk/hA7/1AckjGzRqi6wbo+jaShzRowYip6rt6q7VYEDX4LEy1pZfDpdxCBnGtl+A5zq8iXDcyuxwtv3hNtHFg==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.27.3.tgz",
      "integrity": "sha512-ipTYM2fjt3kQAYOvo6vcxJx3nBYAzPjgTCk7QEgZG8AUO3ydUhvelmhrbOheMnGOlaSFUoHXB6un+A7q4ygY9w==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.27.3.tgz",
      "integrity": "sha512-dDk0X87T7mI6U3K9VjWtHOXqwAMJBNN2r7bejDsc+j03SEjtD9HrOl8gVFByeM0aJksoUuUVU9TBaZa2rgj0oA==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.27.3.tgz",
      "integrity": "sha512-s6nPv2QkSupJwLYyfS+gwdirm0ukyTFNl3KTgZEAiJDd+iHZcbTPPcWCcRYH+WlNbwChgH2QkE9NSlNrMT8Gfw==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.27.3.tgz",
      "integrity": "sha512-sZOuFz/xWnZ4KH3YfFrKCf1WyPZHakVzTiqji3WDc0BCl2kBwiJLCXpzLzUBLgmp4veFZdvN5ChW4Eq/8Fc2Fg==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.27.3.tgz",
      "integrity": "sha512-yGlQYjdxtLdh0a3jHjuwOrxQjOZYD/C9PfdbgJJF3TIZWnm/tMd/RcNiLngiu4iwcBAOezdnSLAwQDPqTmtTYg==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.27.3.tgz",
      "integrity": "sha512-WO60Sn8ly3gtzhyjATDgieJNet/KqsDlX5nRC5Y3oTFcS1l0KWba+SEa9Ja1GfDqSF1z6hif/SkpQJbL63cgOA==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.27.3.tgz",
      "integrity": "sha512-APsymYA6sGcZ4pD6k+UxbDjOFSvPWyZhjaiPyl/f79xKxwTnrn5QUnXR5prvetuaSMsb4jgeHewIDCIWljrSxw==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.27.3.tgz",
      "integrity": "sha512-eizBnTeBefojtDb9nSh4vvVQ3V9Qf9Df01PfawPcRzJH4gFSgrObw+LveUyDoKU3kxi5+9RJTCWlj4FjYXVPEA==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-riscv64/-/linux-riscv64-0.27.3.tgz",
      "integrity": "sha512-3Emwh0r5wmfm3ssTWRQSyVhbOHvqegUDRd0WhmXKX2mkHJe1SFCMJhagUleMq+Uci34wLSipf8Lagt4LlpRFWQ==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-s390x/-/linux-s390x-0.27.3.tgz",
      "integrity": "sha512-pBHUx9LzXWBc7MFIEEL0yD/ZVtNgLytvx60gES28GcWMqil8ElCYR4kvbV2BDqsHOvVDRrOxGySBM9Fcv744hw==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-x64/-/linux-x64-0.27.3.tgz",
      "integrity": "sha512-Czi8yzXUWIQYAtL/2y6vogER8pvcsOsk5cpwL4Gk5nJqH5UZiVByIY8Eorm5R13gq+DQKYg0+JyQoytLQas4dA==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-arm64/-/netbsd-arm64-0.27.3.tgz",
      "integrity": "sha512-sDpk0RgmTCR/5HguIZa9n9u+HVKf40fbEUt+iTzSnCaGvY9kFP0YKBWZtJaraonFnqef5SlJ8/TiPAxzyS+UoA==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/netbsd-x64/-/netbsd-x64-0.27.3.tgz",
      "integrity": "sha512-P14lFKJl/DdaE00LItAukUdZO5iqNH7+PjoBm+fLQjtxfcfFE20Xf5CrLsmZdq5LFFZzb5JMZ9grUwvtVYzjiA==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-arm64/-/openbsd-arm64-0.27.3.tgz",
      "integrity": "sha512-AIcMP77AvirGbRl/UZFTq5hjXK+2wC7qFRGoHSDrZ5v5b8DK/GYpXW3CPRL53NkvDqb9D+alBiC/dV0Fb7eJcw==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/openbsd-x64/-/openbsd-x64-0.27.3.tgz",
      "integrity": "sha512-DnW2sRrBzA+YnE70LKqnM3P+z8vehfJWHXECbwBmH/CU51z6FiqTQTHFenPlHmo3a8UgpLyH3PT+87OViOh1AQ==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/openharmony-arm64/-/openharmony-arm64-0.27.3.tgz",
      "integrity": "sha512-NinAEgr/etERPTsZJ7aEZQvvg/A6IsZG/LgZy+81wON2huV7SrK3e63dU0XhyZP4RKGyTm7aOgmQk0bGp0fy2g==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/sunos-x64/-/sunos-x64-0.27.3.tgz",
      "integrity": "sha512-PanZ+nEz+eWoBJ8/f8HKxTTD172SKwdXebZ0ndd953gt1HRBbhMsaNqjTyYLGLPdoWHy4zLU7bDVJztF5f3BHA==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-arm64/-/win32-arm64-0.27.3.tgz",
      "integrity": "sha512-B2t59lWWYrbRDw/tjiWOuzSsFh1Y/E95ofKz7rIVYSQkUYBjfSgf6oeYPNWHToFRr2zx52JKApIcAS/D5TUBnA==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-ia32/-/win32-ia32-0.27.3.tgz",
      "integrity": "sha512-QLKSFeXNS8+tHW7tZpMtjlNb7HKau0QDpwm49u0vUp9y1WOF+PEzkU84y9GqYaAVW8aH8f3GcBck26jh54cX4Q==",
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
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/@esbuild/win32-x64/-/win32-x64-0.27.3.tgz",
      "integrity": "sha512-4uJGhsxuptu3OcpVAzli+/gWusVGwZZHTlS63hh++ehExkVT8SgiEf7/uC/PclrPPkLhZqGgCTjd0VWLo6xMqA==",
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
    "node_modules/esbuild": {
      "version": "0.27.3",
      "resolved": "https://registry.npmjs.org/esbuild/-/esbuild-0.27.3.tgz",
      "integrity": "sha512-8VwMnyGCONIs6cWue2IdpHxHnAjzxnw2Zr7MkVxB2vjmQ2ivqGFb4LEG3SMnv0Gb2F/G/2yA8zUaiL1gywDCCg==",
      "dev": true,
      "hasInstallScript": true,
      "license": "MIT",
      "bin": {
        "esbuild": "bin/esbuild"
      },
      "engines": {
        "node": ">=18"
      },
      "optionalDependencies": {
        "@esbuild/aix-ppc64": "0.27.3",
        "@esbuild/android-arm": "0.27.3",
        "@esbuild/android-arm64": "0.27.3",
        "@esbuild/android-x64": "0.27.3",
        "@esbuild/darwin-arm64": "0.27.3",
        "@esbuild/darwin-x64": "0.27.3",
        "@esbuild/freebsd-arm64": "0.27.3",
        "@esbuild/freebsd-x64": "0.27.3",
        "@esbuild/linux-arm": "0.27.3",
        "@esbuild/linux-arm64": "0.27.3",
        "@esbuild/linux-ia32": "0.27.3",
        "@esbuild/linux-loong64": "0.27.3",
        "@esbuild/linux-mips64el": "0.27.3",
        "@esbuild/linux-ppc64": "0.27.3",
        "@esbuild/linux-riscv64": "0.27.3",
        "@esbuild/linux-s390x": "0.27.3",
        "@esbuild/linux-x64": "0.27.3",
        "@esbuild/netbsd-arm64": "0.27.3",
        "@esbuild/netbsd-x64": "0.27.3",
        "@esbuild/openbsd-arm64": "0.27.3",
        "@esbuild/openbsd-x64": "0.27.3",
        "@esbuild/openharmony-arm64": "0.27.3",
        "@esbuild/sunos-x64": "0.27.3",
        "@esbuild/win32-arm64": "0.27.3",
        "@esbuild/win32-ia32": "0.27.3",
        "@esbuild/win32-x64": "0.27.3"
      }
    },
    "node_modules/fsevents": {
      "version": "2.3.3",
      "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
      "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
      "dev": true,
      "hasInstallScri
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

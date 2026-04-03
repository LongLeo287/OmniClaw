---
id: github.com-numman-ali-opencode-openai-codex-auth.g
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:06.875695
---

# KNOWLEDGE EXTRACT: github.com_numman-ali_opencode-openai-codex-auth.git_bea289b1
> **Extracted on:** 2026-04-01 14:11:16
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523751/github.com_numman-ali_opencode-openai-codex-auth.git_bea289b1

---

## File: `.gitignore`
```
node_modules/
bun.lockb
pnpm-lock.yaml
dist/
.DS_Store
.history/
opencode.json
.opencode/
tmp
.codex-cache
```

## File: `.npmignore`
```
.git
.gitignore
.DS_Store
node_modules/
bun.lockb
pnpm-lock.yaml
package-lock.json
opencode.json
test-*.mjs
*.log
.vscode/
.idea/
docs/
.github/
```

## File: `AGENTS.md`
```markdown
# AGENTS.md

This file provides coding guidance for AI agents (including Claude Code, Codex, and others) when working with code in this repository.

## Overview

This is an **opencode plugin** that enables OAuth authentication with OpenAI's ChatGPT Plus/Pro Codex backend. It allows users to access `gpt-5.2-codex`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.1-codex-mini`, `gpt-5.2`, and `gpt-5.1` models through their ChatGPT subscription instead of using OpenAI Platform API credits. Legacy GPT-5.0 models are automatically normalized to their GPT-5.1 equivalents.

**Key architecture principle**: 7-step fetch flow that intercepts opencode's OpenAI SDK requests, transforms them for the ChatGPT backend API, and handles OAuth token management.

## Build & Test Commands

```bash
# Build (compiles TypeScript + copies HTML file)
npm run build

# Type checking only (no build)
npm run typecheck

# Run all tests
npm test

# Watch mode for TDD
npm run test:watch

# Interactive test UI
npm run test:ui

# Coverage report
npm run test:coverage
```

**Important**: The build script has a critical step that copies `lib/oauth-success.html` to `dist/lib/`. This HTML file is required for the OAuth callback flow.

## Code Architecture

### Plugin Flow (index.ts)

The main entry point orchestrates a **7-step fetch flow**:

1. **Token Management**: Check token expiration, refresh if needed
2. **URL Rewriting**: Transform OpenAI Platform API URLs → ChatGPT backend API (`https://chatgpt.com/backend-api/codex/responses`)
3. **Request Transformation**:
   - Normalize model names (all variants → `gpt-5.2`, `gpt-5.2-codex`, `gpt-5.1`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.1-codex-mini`, `gpt-5`, `gpt-5-codex`, or `codex-mini-latest`)
   - Inject Codex system instructions from latest GitHub release
   - Apply reasoning configuration (effort, summary, verbosity)
   - Add CODEX_MODE bridge prompt (default) or tool remap message (legacy)
   - Filter OpenCode system prompts when in CODEX_MODE
   - Filter conversation history (remove `rs_*` IDs for stateless operation)
4. **Headers**: Add OAuth token + ChatGPT account ID
5. **Request Execution**: Send to Codex backend
6. **Response Logging**: Optional debug logging (ENABLE_PLUGIN_REQUEST_LOGGING=1)
7. **Response Handling**: Convert SSE to JSON (non-tool requests) or pass through

### Module Organization

**Core Plugin** (`index.ts`)
- Plugin definition and main fetch orchestration
- OAuth loader (extracts ChatGPT account ID from JWT)
- Configuration loading and CODEX_MODE determination

**Authentication** (`lib/auth/`)
- `auth.ts`: OAuth flow (PKCE, token exchange, JWT decoding, refresh)
- `server.ts`: Local HTTP server for OAuth callback (port 1455)
- `browser.ts`: Platform-specific browser opening

**Request Handling** (`lib/request/`)
- `fetch-helpers.ts`: 10 focused helper functions for main fetch flow
- `request-transformer.ts`: Body transformations (model normalization, reasoning config, input filtering)
- `response-handler.ts`: SSE to JSON conversion

**Prompts** (`lib/prompts/`)
- `codex.ts`: Fetches Codex instructions from GitHub (ETag-cached), tool remap message
- `codex-opencode-bridge.ts`: CODEX_MODE bridge prompt for CLI parity

**Configuration** (`lib/`)
- `config.ts`: Plugin config loading, CODEX_MODE determination
- `constants.ts`: All magic values, URLs, error messages
- `types.ts`: TypeScript type definitions
- `logger.ts`: Debug logging (controlled by env var)

### Key Design Patterns

**1. Stateless Operation**: Uses `store: false` + `include: ["reasoning.encrypted_content"]`
- Allows multi-turn conversations without server-side storage
- Encrypted reasoning content persists context across turns

**2. CODEX_MODE** (enabled by default):
- **Priority**: `CODEX_MODE` env var > `~/.opencode/openai-codex-auth-config.json` > default (true)
- When enabled: Filters out OpenCode system prompts, adds Codex-OpenCode bridge prompt with Task tool & MCP awareness
- When disabled: Uses legacy tool remap message
- Bridge prompt (~550 tokens): Tool mappings, available tools, working style, **Task tool/sub-agent awareness**, **MCP tool awareness**
- **Prompt verification**: Caches OpenCode's codex.txt from GitHub (ETag-based) to verify exact prompt removal, with fallback to text signature matching

**3. Configuration Merging**:
- Global options (`provider.openai.options`) + per-model options (`provider.openai.models[name].options`)
- Model-specific options override global
- Plugin defaults: `reasoningEffort: "medium"`, `reasoningSummary: "auto"`, `textVerbosity: "medium"`

**4. Model Normalization** (GPT-5.0 → GPT-5.1 migration):
- All `gpt-5.2-codex*` variants → `gpt-5.2-codex` (newest Codex model, supports xhigh)
- All `gpt-5.1-codex-max*` variants → `gpt-5.1-codex-max`
- All `gpt-5.1-codex*` variants → `gpt-5.1-codex`
- All `gpt-5.1-codex-mini*` variants → `gpt-5.1-codex-mini`
- All `gpt-5.2` variants → `gpt-5.2`
- All `gpt-5.1` variants → `gpt-5.1`
- **Legacy mappings** (GPT-5.0 being phased out):
  - `gpt-5-codex*` variants → `gpt-5.1-codex`
  - `gpt-5-codex-mini*` or `codex-mini-latest` → `gpt-5.1-codex-mini`
  - `gpt-5*` variants (including `gpt-5-mini`, `gpt-5-nano`) → `gpt-5.1`
- `minimal` effort auto-normalized to `low` for Codex families (including GPT-5.2 Codex) and clamped to `medium` (or `high` when requested) for Codex Mini

**5. Model-Specific Prompt Selection**:
- Different prompts for different model families (matching Codex CLI):
  - `gpt-5.2-codex*` → `gpt-5.2-codex_prompt.md` (117 lines, Codex CLI agent prompt)
  - `gpt-5.1-codex-max*` → `gpt-5.1-codex-max_prompt.md` (117 lines, frontend design guidelines)
  - `gpt-5.1-codex*`, `codex-*` → `gpt_5_codex_prompt.md` (105 lines, coding focus)
  - `gpt-5.2*` → `gpt_5_2_prompt.md` (GPT‑5.2 general family)
  - `gpt-5.1*` → `gpt_5_1_prompt.md` (368 lines, full behavioral guidance)
- `getModelFamily()` determines prompt selection based on normalized model

**6. Codex Instructions Caching**:
- Fetches from latest release tag (not main branch)
- ETag-based HTTP conditional requests per model family
- Separate cache files per family: `gpt-5.2-codex-instructions.md`, `codex-max-instructions.md`, `codex-instructions.md`, `gpt-5.2-instructions.md`, `gpt-5.1-instructions.md`
- Cache invalidation when release tag changes
- Falls back to bundled version if GitHub unavailable

## Development Patterns

### Adding New Configuration Options

1. Add to `ConfigOptions` interface in `lib/types.ts`
2. Update `transformRequestBody()` in `lib/request/request-transformer.ts`
3. Add tests in `test/request-transformer.test.ts`
4. Document in README.md configuration section

### Modifying Request Transformation

All request transformations go through `transformRequestBody()`:
- Input filtering: `filterInput()`, `filterOpenCodeSystemPrompts()`
- Message injection: `addCodexBridgeMessage()` or `addToolRemapMessage()`
- Reasoning config: `getReasoningConfig()` (follows Codex CLI defaults, not opencode defaults)
- Model config: `getModelConfig()` (merges global + per-model options)

### OAuth Flow Modifications

OAuth implementation follows OpenAI Codex CLI patterns:
- Client ID: `app_EMoamEEZ73f0CkXaXp7hrann`
- PKCE with S256 challenge
- Special params: `codex_cli_simplified_flow=true`, `originator=codex_cli_rs`
- Callback server on port 1455 (matches Codex CLI)

### Testing Strategy

- **191 comprehensive tests** covering all modules
- Test files mirror source structure (`test/auth.test.ts` ↔ `lib/auth/auth.ts`)
- Mock-heavy testing (no actual network calls or file I/O in tests)
- Focus on edge cases: token expiration, model normalization, input filtering, CODEX_MODE toggling

## Important Configuration Differences

This plugin **intentionally differs from opencode defaults** because it accesses ChatGPT backend API (not OpenAI Platform API):

| Setting | opencode Default | This Plugin Default | Reason |
|---------|-----------------|---------------------|--------|
| `reasoningEffort` | "high" (gpt-5) | "medium" (Codex Max defaults to "high") | Matches Codex CLI default and Codex Max capabilities |
| `textVerbosity` | "low" (gpt-5) | "medium" | Matches Codex CLI default |
| `reasoningSummary` | "detailed" | "auto" | Matches Codex CLI default |
| gpt-5-codex config | (excluded) | Full support | opencode excludes gpt-5-codex from auto-config |
| `store` | true | false | Required for ChatGPT backend |
| `include` | (not set) | `["reasoning.encrypted_content"]` | Required for stateless operation |

## File Paths & Locations

- **Plugin config**: `~/.opencode/openai-codex-auth-config.json`
- **Cache dir**: `~/.opencode/cache/`
  - `codex-instructions.md` (Codex CLI instructions from GitHub)
  - `codex-instructions-meta.json` (ETag + release tag for Codex instructions)
  - `opencode-codex.txt` (OpenCode system prompt from GitHub, for verification)
  - `opencode-codex-meta.json` (ETag for OpenCode prompt)
- **Debug logs**: `~/.opencode/logs/codex-plugin/` (when `ENABLE_PLUGIN_REQUEST_LOGGING=1`)
- **OAuth callback**: `http://localhost:1455/auth/callback`

## Environment Variables

- `CODEX_MODE`: Override config file (1=enable, 0=disable)
- `ENABLE_PLUGIN_REQUEST_LOGGING`: Enable detailed request logging (1=enable)

## TypeScript Configuration

- Target: ES2022
- Module: ES2022 with bundler resolution
- Output: `./dist/`
- Strict mode enabled
- Declaration files generated
- Source maps enabled
- Excludes: `test/`, `node_modules/`, `dist/`

## Dependencies

**Production**:
- `@openauthjs/openauth` (OAuth PKCE implementation)

**Development**:
- `@opencode-ai/plugin` (peer dependency)
- `vitest` (testing framework)
- TypeScript

**Zero external runtime dependencies** - only uses Node.js built-ins for file I/O, HTTP, crypto.
```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to this project are documented here. Dates use the ISO format (YYYY-MM-DD).

## [4.4.0] - 2026-01-09

**Maintenance release**: OAuth success page version sync.

### Changed
- **OAuth success banner**: Updates the success page header to display the current release version.

## [4.3.1] - 2026-01-08

**Installer safety release**: JSONC support, safe uninstall, and minimal reasoning clamp.

### Added
- **JSONC-aware installer**: preserves comments/formatting and prioritizes `opencode.jsonc` over `opencode.json`.
- **Safe uninstall**: `--uninstall` removes only plugin entries + our model presets; `--all` removes tokens/logs/cache.
- **Installer tests**: coverage for JSONC parsing, precedence, uninstall safety, and artifact cleanup.

### Changed
- **Default config path**: installer creates `~/.config/opencode/opencode.jsonc` when no config exists.
- **Dependency**: `jsonc-parser` added to keep JSONC updates robust and comment-safe.

### Fixed
- **Minimal reasoning clamp**: `minimal` is now normalized to `low` for GPT‑5.x requests to avoid backend rejection.

## [4.3.0] - 2026-01-04

**Feature + reliability release**: variants support, one-command installer, and auth/error handling fixes.

### Added
- **One-command installer/update**: `npx -y opencode-openai-codex-auth@latest` (global config, backup, cache clear) with `--legacy` for OpenCode v1.0.209 and below.
- **Modern variants config**: `config/opencode-modern.json` for OpenCode v1.0.210+; legacy presets remain in `config/opencode-legacy.json`.
- **Installer CLI** bundled as package bin for cross-platform use (Windows/macOS/Linux).

### Changed
- **Variants-aware request config**: respects host-supplied `body.reasoning` / `providerOptions.openai` before falling back to defaults.
- **OpenCode prompt source**: updates to the current upstream repository (`anomalyco/opencode`).
- **Docs/README**: install-first layout with leaner guidance and explicit legacy path.

### Fixed
- **Headless login fallback**: missing `xdg-open` no longer fails the OAuth flow; manual URL paste stays available.
- **Error handling alignment**: refresh failures throw; usage-limit 404s map to retryable 429s where appropriate.
- **AGENTS.md preservation**: protected instruction markers stop accidental filtering of user instructions.
- **Tool-call integrity**: orphan outputs now match `local_shell_call` and `custom_tool_call` (Codex CLI parity); unmatched outputs preserved as assistant messages.
- **Logging noise**: debug logging gated behind flags to prevent stdout bleed.

## [4.2.0] - 2025-12-19

**Feature release**: GPT 5.2 Codex support and prompt alignment with latest Codex CLI.

### Added
- **GPT 5.2 Codex model family**: Full support for `gpt-5.2-codex` with presets:
  - `gpt-5.2-codex-low` - Fast GPT 5.2 Codex responses
  - `gpt-5.2-codex-medium` - Balanced GPT 5.2 Codex tasks
  - `gpt-5.2-codex-high` - Complex GPT 5.2 Codex reasoning & tools
  - `gpt-5.2-codex-xhigh` - Deep GPT 5.2 Codex long-horizon work
- **New model family prompt**: `gpt-5.2-codex_prompt.md` fetched from the latest Codex CLI release with its own cache file.
- **Test coverage**: Added unit tests for GPT 5.2 Codex normalization, family selection, and reasoning behavior.

### Changed
- **Prompt selection alignment**: GPT 5.2 general now uses `gpt_5_2_prompt.md` (Codex CLI parity).
- **Reasoning configuration**: GPT 5.2 Codex supports `xhigh` but does **not** support `"none"`; `"none"` auto-upgrades to `"low"` and `"minimal"` normalizes to `"low"`.
- **Config presets**: `config/opencode-legacy.json` includes the 22 pre-configured presets (adds GPT 5.2 Codex); `config/opencode-modern.json` provides the variant-based setup.
- **Docs**: Updated README/AGENTS/config docs to include GPT 5.2 Codex and new model family behavior.

## [4.1.1] - 2025-12-17

**Minor release**: "none" reasoning effort support, orphaned function_call_output fix, and HTML version update.

### Added
- **"none" reasoning effort support**: GPT-5.1 and GPT-5.2 support `reasoning_effort: "none"` which disables the reasoning phase entirely. This can result in faster responses when reasoning is not needed.
  - `gpt-5.2-none` - GPT-5.2 with reasoning disabled
  - `gpt-5.1-none` - GPT-5.1 with reasoning disabled
- **4 new unit tests** for "none" reasoning behavior (now 197 total unit tests).

### Fixed
- **Orphaned function_call_output 400 errors**: Fixed API errors when conversation history contains `item_reference` pointing to stored function calls. Previously, orphaned `function_call_output` items were only filtered when `!body.tools`. Now always handles orphans regardless of tools presence, and converts them to assistant messages to preserve context while avoiding API errors.
- **OAuth HTML version display**: Updated version in oauth-success.html from 1.0.4 to 4.1.0.

### Technical Details
- `getReasoningConfig()` now detects GPT-5.1 general purpose models (not Codex variants) and allows "none" to pass through.
- GPT-5.2 inherits "none" support as it's newer than GPT-5.1.
- Codex variants (gpt-5.1-codex, gpt-5.1-codex-max, gpt-5.1-codex-mini) do NOT support "none":
  - Codex and Codex Max: "none" auto-converts to "low"
  - Codex Mini: "none" auto-converts to "medium" (as before)
- Documentation updated with complete reasoning effort support matrix per model family.

### References
- **OpenAI API docs** (`platform.openai.com/docs/api-reference/chat/create`): "gpt-5.1 defaults to none, which does not perform reasoning. The supported reasoning values for gpt-5.1 are none, low, medium, and high."
- **Codex CLI** (`codex-rs/protocol/src/openai_models.rs`): `ReasoningEffort` enum includes `None` variant with `#[serde(rename_all = "lowercase")]` serialization to `"none"`.
- **Codex CLI** (`codex-rs/core/src/client.rs`): Request builder passes `ReasoningEffort::None` through to API without validation/rejection.
- **Codex CLI** (`docs/config.md`): Documents `model_reasoning_effort = "none"` as valid config option.

### Notes
- This plugin defaults to "medium" for better coding assistance; users must explicitly set "none" if desired.

## [4.1.0] - 2025-12-11

**Feature release**: GPT 5.2 model support and image input capabilities.

### Added
- **GPT 5.2 model family support**: Full support for OpenAI's latest GPT 5.2 model with 4 reasoning level presets:
  - `gpt-5.2-low` - Fast responses with light reasoning
  - `gpt-5.2-medium` - Balanced reasoning for general tasks
  - `gpt-5.2-high` - Complex reasoning and analysis
  - `gpt-5.2-xhigh` - Deep multi-hour analysis (same as Codex Max)
- **Full image input support**: All 16 model variants now include `modalities.input: ["text", "image"]` enabling full multimodal capabilities - read screenshots, diagrams, UI mockups, and any image directly in OpenCode.
- **GPT 5.2 model family** added to `codex.ts` with dedicated prompt handling.
- **Test coverage**: Updated integration tests to verify all 16 models (was 13), now 193 unit tests + 16 integration tests.

### Changed
- **Model ordering**: Config now ordered by model family priority: GPT 5.2 → Codex Max → Codex → Codex Mini → GPT 5.1.
- **Removed default presets**: Removed `gpt-5.1-codex-max` and `gpt-5.2` (without reasoning suffix) to enforce explicit reasoning level selection.
- **Test script**: `scripts/test-all-models.sh` now uses local dist for testing and includes GPT 5.2 tests.
- **Documentation**: Updated README with GPT 5.2 models, image support, and condensed config example.

### Technical Details
- GPT 5.2 maps to `gpt-5.2` API model with same reasoning options as Codex Max (`low/medium/high/xhigh`).
- `getModelFamily()` now returns `"gpt-5.2"` for GPT 5.2 models, using Codex Max prompts.
- `getReasoningConfig()` treats GPT 5.2 like Codex Max for `xhigh` reasoning support.
- Model normalization pattern matching updated to recognize GPT 5.2 before other patterns.

## [4.0.2] - 2025-11-27

**Bugfix release**: Fixes compaction context loss, agent creation, and SSE/JSON response handling.

### Fixed
- **Compaction losing context**: v4.0.1 was too aggressive in filtering tool calls - it removed ALL `function_call`/`function_call_output` items when tools weren't present. Now only **orphaned** outputs (without matching calls) are filtered, preserving matched pairs for compaction context.
- **Agent creation failing**: The `/agent create` command was failing with "Invalid JSON response" because we were returning SSE streams instead of JSON for `generateText()` requests.
- **SSE/JSON response handling**: Properly detect original request intent - `streamText()` requests get SSE passthrough, `generateText()` requests get SSE→JSON conversion.

### Added
- **`gpt-5.1-chat-latest` model support**: Added to model map, normalizes to `gpt-5.1`.

### Technical Details
- Root cause of compaction issue: OpenCode sends `item_reference` with `fc_*` IDs for function calls. We filter these for stateless mode, but v4.0.1 then removed ALL tool items. Now we only remove orphaned `function_call_output` items (where no matching `function_call` exists).
- Root cause of agent creation issue: We were forcing `stream: true` for all requests and returning SSE for all responses. Now we capture original `stream` value before transformation and convert SSE→JSON only when original request wasn't streaming.
- The Codex API always receives `stream: true` (required), but response handling is based on original intent.

## [4.0.1] - 2025-11-27

**Bugfix release**: Fixes API errors during summary/compaction and GitHub rate limiting.

### Fixed
- **Orphaned `function_call_output` errors**: Fixed 400 errors during summary/compaction requests when OpenCode sends `item_reference` pointers to server-stored function calls. The plugin now filters out `function_call` and `function_call_output` items when no tools are present in the request.
- **GitHub API rate limiting**: Added fallback mechanism when fetching Codex instructions from GitHub. If the API returns 403 (rate limit), the plugin now falls back to parsing the HTML releases page.

### Technical Details
- Root cause: OpenCode's secondary model (gpt-5-nano) uses `item_reference` with `fc_*` IDs to reference stored function calls. Our plugin filters `item_reference` for stateless mode (`store: false`), leaving `function_call_output` orphaned. The Codex API rejects requests with orphaned outputs.
- Fix: When `hasTools === false`, filter out all `function_call` and `function_call_output` items from the input array.
- GitHub fallback chain: API endpoint → HTML page → redirect URL parsing → HTML regex parsing.

## [4.0.0] - 2025-11-25

**Major release**: Complete prompt engineering overhaul matching official Codex CLI behavior, with full **GPT-5.1 Codex Max** support.

### Highlights
- **Full Codex Max support** with dedicated prompt including frontend design guidelines
- **Model-specific prompts** matching Codex CLI's prompt selection logic
- **GPT-5.0 → GPT-5.1 migration** as legacy models are phased out

### Added
- **Model-specific system prompts**: Plugin now fetches the correct Codex prompt based on model family, matching Codex CLI's `model_family.rs` logic:
  - `gpt-5.1-codex-max*` → `gpt-5.1-codex-max_prompt.md` (117 lines, includes frontend design guidelines)
  - `gpt-5.1-codex*`, `gpt-5.1-codex-mini*` → `gpt_5_codex_prompt.md` (105 lines, focused coding prompt)
  - `gpt-5.1*` → `gpt_5_1_prompt.md` (368 lines, full behavioral guidance)
- New `ModelFamily` type (`"codex-max" | "codex" | "gpt-5.1"`) for prompt selection.
- New `getModelFamily()` function to determine prompt selection based on normalized model name.
- Model family now logged in request logs for debugging (`modelFamily` field in after-transform logs).
- 16 new unit tests for model family detection (now **191 total unit tests**).
- Integration tests now verify correct model family selection (13 integration tests with family verification).

### Changed
- **Legacy GPT-5.0 models now map to GPT-5.1**: All legacy `gpt-5` model variants automatically normalize to their `gpt-5.1` equivalents as GPT-5.0 is being phased out by OpenAI:
  - `gpt-5-codex` → `gpt-5.1-codex`
  - `gpt-5` → `gpt-5.1`
  - `gpt-5-mini`, `gpt-5-nano` → `gpt-5.1`
  - `codex-mini-latest` → `gpt-5.1-codex-mini`
- **Lazy instruction loading**: Instructions are now fetched per-request based on model family (not pre-loaded at initialization).
- **Separate caching per model family**: Each model family has its own cached prompt file:
  - `codex-max-instructions.md` + `codex-max-instructions-meta.json`
  - `codex-instructions.md` + `codex-instructions-meta.json`
  - `gpt-5.1-instructions.md` + `gpt-5.1-instructions-meta.json`

### Fixed
- Fixed OpenCode prompt cache URL to fetch from `dev` branch instead of non-existent `main` branch.
- Fixed model configuration test script to correctly identify model logs in multi-model sessions (opencode uses a small model like `gpt-5-nano` for title generation alongside the user's selected model).

### Technical Details
This release brings full parity with Codex CLI's prompt engineering:
- **Codex family** (105 lines): Concise, tool-focused prompt for coding tasks
- **Codex Max family** (117 lines): Adds frontend design guidelines for UI work
- **GPT-5.1 general** (368 lines): Comprehensive behavioral guidance, personality, planning

## [3.3.0] - 2025-11-19
### Added
- GPT 5.1 Codex Max support: normalization, per-model defaults, and new presets (`gpt-5.1-codex-max`, `gpt-5.1-codex-max-xhigh`) with extended reasoning options (including `none`/`xhigh`) while keeping the 272k context / 128k output limits.
- Typing and config support for new reasoning options (`none`/`xhigh`, summary `off`/`on`) plus updated test matrix entries.

### Changed
- Codex Mini clamping now downgrades unsupported `xhigh` to `high` and guards against `none`/`minimal` inputs.
- Documentation, config guides, and validation scripts now reflect 13 verified GPT 5.1 variants (3 codex, 5 codex-max, 2 codex-mini, 3 general), including Codex Max. See README for details on pre-configured variants.

## [3.2.0] - 2025-11-14
### Added
- GPT 5.1 model family support: normalization for `gpt-5.1`, `gpt-5.1-codex`, and `gpt-5.1-codex-mini` plus new GPT 5.1-only presets in the canonical `config/opencode-legacy.json`.
- Documentation updates (README, docs, AGENTS) describing the 5.1 families, their reasoning defaults, and how they map to ChatGPT slugs and token limits.

### Changed
- Model normalization docs and tests now explicitly cover both 5.0 and 5.1 Codex/general families and the two Codex Mini tiers.
- The legacy GPT 5.0 full configuration is now published separately; new installs should prefer the 5.1 presets in `config/opencode-legacy.json`.

## [3.1.0] - 2025-11-11
### Added
- Codex Mini support end-to-end: normalization to the `codex-mini-latest` slug, proper reasoning defaults, and two new presets (`gpt-5-codex-mini-medium` / `gpt-5-codex-mini-high`).
- Documentation & configuration updates describing the Codex Mini tier (200k input / 100k output tokens) plus refreshed totals (11 presets, 160+ unit tests).

### Fixed
- Prevented Codex Mini from inheriting the lightweight (`minimal`) reasoning profile used by `gpt-5-mini`/`nano`, ensuring the API always receives supported effort levels.

## [3.0.0] - 2025-11-04
### Added
- Codex-style usage-limit messaging that mirrors the 5-hour and weekly windows reported by the Codex CLI.
- Documentation guidance noting that OpenCode's context auto-compaction and usage sidebar require the canonical `config/opencode-legacy.json`.

### Changed
- Prompt caching now relies solely on the host-supplied `prompt_cache_key`; conversation/session headers are forwarded only when OpenCode provides one.
- CODEX_MODE bridge prompt refreshed to the newest Codex CLI release so tool awareness stays in sync.

### Fixed
- Clarified README, docs, and configuration references so the canonical config matches shipped behaviour.
- Pinned `hono` (4.10.4) and `vite` (7.1.12) to resolve upstream security advisories.

## [2.1.2] - 2025-10-12
### Added
- Comprehensive compliance documentation (ToS guidance, security, privacy) and a full user/developer doc set.

### Fixed
- Per-model configuration lookup, stateless multi-turn conversations, case-insensitive model normalization, and GitHub instruction caching.

## [2.1.1] - 2025-10-04
### Fixed
- README cache-clearing snippet now runs in a subshell from the home directory to avoid path issues while removing cached plugin files.

## [2.1.0] - 2025-10-04
### Added
- Enhanced CODEX_MODE bridge prompt with Task tool and MCP awareness plus ETag-backed verification of OpenCode system prompts.

### Changed
- Request transformation made async to support prompt verification caching; AGENTS.md renamed to provide cross-agent guidance.

## [2.0.0] - 2025-10-03
### Added
- Full TypeScript rewrite with strict typing, 123 automated tests, and nine pre-configured model variants matching the Codex CLI.
- CODEX_MODE introduced (enabled by default) with a lightweight bridge prompt and configurability via config file or `CODEX_MODE` env var.

### Changed
- Library reorganized into semantic folders (auth, prompts, request, etc.) and OAuth flow polished with the new success page.

## [1.0.3] - 2025-10-02
### Changed
- Major internal refactor splitting the runtime into focused modules (logger, request/response handlers) and removing legacy debug output.

## [1.0.2] - 2025-10-02
### Added
- ETag-based GitHub caching for Codex instructions and release-tag tracking for more stable prompt updates.

### Fixed
- Default model fallback, text verbosity initialization, and standardized error logging prefixes.

## [1.0.1] - 2025-10-01
### Added
- README clarifications: opencode auto-installs plugins, config locations, and streamlined quick-start instructions.

## [1.0.0] - 2025-10-01
### Added
- Initial production release with ChatGPT Plus/Pro OAuth support, tool remapping, auto-updating Codex instructions, and zero runtime dependencies.
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing Guidelines

Thank you for your interest in contributing to opencode-openai-codex-auth!

Before submitting contributions, please review these guidelines to ensure all changes maintain compliance with OpenAI's Terms of Service and the project's goals.

## Compliance Requirements

All contributions MUST:

✅ **Maintain TOS Compliance**
- Use only official OAuth authentication methods
- Not facilitate violations of OpenAI's Terms of Service
- Focus on legitimate personal productivity use cases
- Include appropriate user warnings and disclaimers

✅ **Respect OpenAI's Systems**
- No session token scraping or cookie extraction
- No bypassing of rate limits or authentication controls
- No reverse-engineering of undocumented APIs
- Use only officially supported authentication flows

✅ **Proper Use Cases**
- Personal development and coding assistance
- Individual productivity enhancements
- Terminal-based workflows
- Educational purposes

❌ **Prohibited Features**
- Commercial resale or multi-user authentication
- Rate limit circumvention techniques
- Session token scraping or extraction
- Credential sharing mechanisms
- Features designed to violate OpenAI's terms

## Code Standards

- **TypeScript:** All code must be TypeScript with strict type checking
- **Testing:** Include tests for new functionality (we maintain 200+ unit tests)
- **Documentation:** Update README.md for user-facing changes
- **Modular design:** Keep functions focused and under 40 lines
- **No external dependencies:** Minimize dependencies (currently only @openauthjs/openauth)

## Pull Request Process

1. **Fork the repository** and create a feature branch
2. **Write clear commit messages** explaining the "why" not just "what"
3. **Include tests** for new functionality
4. **Update documentation** (README.md, config examples, etc.)
5. **Ensure compliance** with guidelines above
6. **Test thoroughly** with actual ChatGPT Plus/Pro account
7. **Submit PR** with clear description of changes

## Reporting Issues

When reporting issues, please:

- **Check existing issues** to avoid duplicates
- **Provide clear reproduction steps**
- **Include version information** (`opencode --version`, plugin version)
- **Confirm compliance:** Verify you're using the plugin for personal use with your own subscription
- **Attach logs** (if using `ENABLE_PLUGIN_REQUEST_LOGGING=1`)

### Issue Template

Please include:
```
**Issue Description:**
[Clear description of the problem]

**Steps to Reproduce:**
1.
2.
3.

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

**Environment:**
- opencode version:
- Plugin version:
- OS:
- Node version:

**Compliance Confirmation:**
- [ ] I'm using this for personal development only
- [ ] I have an active ChatGPT Plus/Pro subscription
- [ ] This is not related to commercial use or TOS violations
```

## Feature Requests

We welcome feature requests that:
- Enhance personal productivity
- Improve developer experience
- Maintain compliance with OpenAI's terms
- Align with the project's scope

We will decline features that:
- Violate or circumvent OpenAI's Terms of Service
- Enable commercial resale or multi-user access
- Bypass authentication or rate limiting
- Facilitate improper use

## Code of Conduct

### Our Standards

✅ **Encouraged:**
- Respectful and constructive communication
- Focus on legitimate use cases
- Transparency about limitations and compliance
- Helping other users with proper usage

❌ **Not Acceptable:**
- Requesting help with TOS violations
- Promoting commercial misuse
- Hostile or disrespectful behavior
- Sharing credentials or tokens

## Questions?

For questions about:
- **Plugin usage:** Open a GitHub issue
- **OpenAI's terms:** Contact OpenAI support
- **Contributing:** Open a discussion thread

## License

By contributing, you agree that your contributions will be licensed under the MIT License with Usage Disclaimer (see LICENSE file).

---

Thank you for helping make this plugin better while maintaining compliance and ethics!
```

## File: `LICENSE`
```
MIT License with Usage Disclaimer

Copyright (c) 2024-2025 numman-ali

USAGE NOTICE AND DISCLAIMER:
This software is provided for personal development use only. Users must comply
with OpenAI's Terms of Service (https://openai.com/policies/terms-of-use/) and
Usage Policies (https://openai.com/policies/usage-policies/) when using this
software to access OpenAI services.

The authors and contributors are not responsible for any violations of
third-party terms of service. For commercial use or production applications,
obtain proper API access from OpenAI directly through the OpenAI Platform
(https://platform.openai.com/).

This software uses OpenAI's official OAuth authentication system and is not
affiliated with, endorsed by, or sponsored by OpenAI.

---

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice, usage notice, and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
![Image 1: opencode-openai-codex-auth](assets/readme-hero.svg)
  
  
**Curated by [Numman Ali](https://x.com/nummanali)**
[![Twitter Follow](https://img.shields.io/twitter/follow/nummanali?style=social)](https://x.com/nummanali)
[![npm version](https://img.shields.io/npm/v/opencode-openai-codex-auth.svg)](https://www.npmjs.com/package/opencode-openai-codex-auth)
[![Tests](https://github.com/numman-ali/opencode-openai-codex-auth/actions/workflows/ci.yml/badge.svg)](https://github.com/numman-ali/opencode-openai-codex-auth/actions)
[![npm downloads](https://img.shields.io/npm/dm/opencode-openai-codex-auth.svg)](https://www.npmjs.com/package/opencode-openai-codex-auth)
**One install. Every Codex model.**
[Install](#-quick-start) · [Models](#-models) · [Configuration](#-configuration) · [Docs](#-docs)

---
## 💡 Philosophy
> **"One config. Every model."**
OpenCode should feel effortless. This plugin keeps the setup minimal while giving you full GPT‑5.x + Codex access via ChatGPT OAuth.
```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  ChatGPT OAuth → Codex backend → OpenCode               │
│  One command install, full model presets, done.         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```
---
## 🚀 Quick Start
```bash
npx -y opencode-openai-codex-auth@latest
```
Then:
```bash
opencode auth login
opencode run "write hello world to test.txt" --model=openai/gpt-5.2 --variant=medium
```
Legacy OpenCode (v1.0.209 and below):
```bash
npx -y opencode-openai-codex-auth@latest --legacy
opencode run "write hello world to test.txt" --model=openai/gpt-5.2-medium
```
Uninstall:
```bash
npx -y opencode-openai-codex-auth@latest --uninstall
npx -y opencode-openai-codex-auth@latest --uninstall --all
```
---
## 📦 Models
- **gpt-5.2** (none/low/medium/high/xhigh)
- **gpt-5.2-codex** (low/medium/high/xhigh)
- **gpt-5.1-codex-max** (low/medium/high/xhigh)
- **gpt-5.1-codex** (low/medium/high)
- **gpt-5.1-codex-mini** (medium/high)
- **gpt-5.1** (none/low/medium/high)
---
## 🧩 Configuration
- Modern (OpenCode v1.0.210+): `config/opencode-modern.json`
- Legacy (OpenCode v1.0.209 and below): `config/opencode-legacy.json`

Minimal configs are not supported for GPT‑5.x; use the full configs above.
---
## ✅ Features
- ChatGPT Plus/Pro OAuth authentication (official flow)
- 22 model presets across GPT‑5.2 / GPT‑5.2 Codex / GPT‑5.1 families
- Variant system support (v1.0.210+) + legacy presets
- Multimodal input enabled for all models
- Usage‑aware errors + automatic token refresh
---
## 📚 Docs
- Getting Started: `docs/getting-started.md`
- Configuration: `docs/configuration.md`
- Troubleshooting: `docs/troubleshooting.md`
- Architecture: `docs/development/ARCHITECTURE.md`
---
## ⚠️ Usage Notice
This plugin is for **personal development use** with your own ChatGPT Plus/Pro subscription.
For production or multi‑user applications, use the OpenAI Platform API.

**Built for developers who value simplicity.**
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

We provide security updates for the latest version of the plugin.

| Version | Supported          |
| ------- | ------------------ |
| Latest  | ✅ Active support |
| < 1.0   | ❌ No longer supported |

## Security Considerations

### OAuth Token Security

This plugin handles sensitive OAuth tokens. To protect your security:

✅ **What we do:**
- Store tokens securely via opencode's credential management
- Use PKCE-secured OAuth 2.0 flows
- Never transmit tokens to third parties
- Implement automatic token refresh
- Use industry-standard authentication practices

⚠️ **What you should do:**
- Never share your `~/.opencode/` directory
- Do not commit OAuth tokens to version control
- Regularly review authorized apps at [ChatGPT Settings](https://chatgpt.com/settings/apps)
- Use `opencode auth logout` when done on shared systems
- Enable debug logging (`ENABLE_PLUGIN_REQUEST_LOGGING=1`) only when troubleshooting

### Reporting a Vulnerability

If you discover a security vulnerability:

1. **DO NOT open a public issue**
2. Email the maintainer directly (check GitHub profile for contact)
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We aim to respond to security reports within 48 hours.

### Responsible Disclosure

We follow responsible disclosure practices:
- Security issues are patched before public disclosure
- Reporter receives credit (unless anonymity is requested)
- Timeline for disclosure is coordinated with reporter

### Security Best Practices

When using this plugin:

- **Personal use only:** Do not use for commercial services
- **Respect rate limits:** Avoid excessive automation
- **Monitor usage:** Review your ChatGPT usage regularly
- **Keep updated:** Use the latest version for security patches
- **Secure your machine:** This plugin is as secure as your development environment
- **Review permissions:** Understand what the plugin can access via OAuth

### Out of Scope

The following are **not** security vulnerabilities:
- Issues related to violating OpenAI's Terms of Service
- Rate limiting by OpenAI's servers
- Authentication failures due to expired subscriptions
- OpenAI API or service outages

### Third-Party Dependencies

This plugin minimizes dependencies for security:
- **Only dependency:** `@openauthjs/openauth` (for OAuth handling)
- Regular dependency updates for security patches
- No telemetry or analytics dependencies

## Questions?

For security questions that are not vulnerabilities, open a discussion thread on GitHub.

---

**Note:** This plugin is not affiliated with OpenAI. For OpenAI security concerns, contact OpenAI directly.
```

## File: `index.ts`
```typescript
/**
 * OpenAI ChatGPT (Codex) OAuth Authentication Plugin for opencode
 *
 * COMPLIANCE NOTICE:
 * This plugin uses OpenAI's official OAuth authentication flow (the same method
 * used by OpenAI's official Codex CLI at https://github.com/openai/codex).
 *
 * INTENDED USE: Personal development and coding assistance with your own
 * ChatGPT Plus/Pro subscription.
 *
 * NOT INTENDED FOR: Commercial resale, multi-user services, high-volume
 * automated extraction, or any use that violates OpenAI's Terms of Service.
 *
 * Users are responsible for ensuring their usage complies with:
 * - OpenAI Terms of Use: https://openai.com/policies/terms-of-use/
 * - OpenAI Usage Policies: https://openai.com/policies/usage-policies/
 *
 * For production applications, use the OpenAI Platform API: https://platform.openai.com/
 *
 * @license MIT with Usage Disclaimer (see LICENSE file)
 * @author numman-ali
 * @repository https://github.com/numman-ali/opencode-openai-codex-auth
 */

import type { Plugin, PluginInput } from "@opencode-ai/plugin";
import type { Auth } from "@opencode-ai/sdk";
import {
	createAuthorizationFlow,
	decodeJWT,
	exchangeAuthorizationCode,
	parseAuthorizationInput,
	REDIRECT_URI,
} from "./lib/auth/auth.js";
import { openBrowserUrl } from "./lib/auth/browser.js";
import { startLocalOAuthServer } from "./lib/auth/server.js";
import { getCodexMode, loadPluginConfig } from "./lib/config.js";
import {
	AUTH_LABELS,
	CODEX_BASE_URL,
	DUMMY_API_KEY,
	ERROR_MESSAGES,
	JWT_CLAIM_PATH,
	LOG_STAGES,
	OPENAI_HEADER_VALUES,
	OPENAI_HEADERS,
	PLUGIN_NAME,
	PROVIDER_ID,
} from "./lib/constants.js";
import { logRequest, logDebug } from "./lib/logger.js";
import {
	createCodexHeaders,
	extractRequestUrl,
	handleErrorResponse,
	handleSuccessResponse,
	refreshAndUpdateToken,
	rewriteUrlForCodex,
	shouldRefreshToken,
	transformRequestForCodex,
} from "./lib/request/fetch-helpers.js";
import type { UserConfig } from "./lib/types.js";

/**
 * OpenAI Codex OAuth authentication plugin for opencode
 *
 * This plugin enables opencode to use OpenAI's Codex backend via ChatGPT Plus/Pro
 * OAuth authentication, allowing users to leverage their ChatGPT subscription
 * instead of OpenAI Platform API credits.
 *
 * @example
 * ```json
 * {
 *   "plugin": ["opencode-openai-codex-auth"],
 *   "model": "openai/gpt-5-codex"
 * }
 * ```
 */
export const OpenAIAuthPlugin: Plugin = async ({ client }: PluginInput) => {
	const buildManualOAuthFlow = (pkce: { verifier: string }, url: string) => ({
		url,
		method: "code" as const,
		instructions: AUTH_LABELS.INSTRUCTIONS_MANUAL,
		callback: async (input: string) => {
			const parsed = parseAuthorizationInput(input);
			if (!parsed.code) {
				return { type: "failed" as const };
			}
			const tokens = await exchangeAuthorizationCode(
				parsed.code,
				pkce.verifier,
				REDIRECT_URI,
			);
			return tokens?.type === "success" ? tokens : { type: "failed" as const };
		},
	});
	return {
		auth: {
			provider: PROVIDER_ID,
			/**
			 * Loader function that configures OAuth authentication and request handling
			 *
			 * This function:
			 * 1. Validates OAuth authentication
			 * 2. Extracts ChatGPT account ID from access token
			 * 3. Loads user configuration from opencode.json
			 * 4. Fetches Codex system instructions from GitHub (cached)
			 * 5. Returns SDK configuration with custom fetch implementation
			 *
			 * @param getAuth - Function to retrieve current auth state
			 * @param provider - Provider configuration from opencode.json
			 * @returns SDK configuration object or empty object for non-OAuth auth
			 */
			async loader(getAuth: () => Promise<Auth>, provider: unknown) {
				const auth = await getAuth();

				// Only handle OAuth auth type, skip API key auth
				if (auth.type !== "oauth") {
					return {};
				}

				// Extract ChatGPT account ID from JWT access token
				const decoded = decodeJWT(auth.access);
				const accountId = decoded?.[JWT_CLAIM_PATH]?.chatgpt_account_id;

				if (!accountId) {
					logDebug(
						`[${PLUGIN_NAME}] ${ERROR_MESSAGES.NO_ACCOUNT_ID} (skipping plugin)`,
					);
					return {};
				}
				// Extract user configuration (global + per-model options)
				const providerConfig = provider as
					| { options?: Record<string, unknown>; models?: UserConfig["models"] }
					| undefined;
				const userConfig: UserConfig = {
					global: providerConfig?.options || {},
					models: providerConfig?.models || {},
				};

				// Load plugin configuration and determine CODEX_MODE
				// Priority: CODEX_MODE env var > config file > default (true)
				const pluginConfig = loadPluginConfig();
				const codexMode = getCodexMode(pluginConfig);

				// Return SDK configuration
				return {
					apiKey: DUMMY_API_KEY,
					baseURL: CODEX_BASE_URL,
					/**
					 * Custom fetch implementation for Codex API
					 *
					 * Handles:
					 * - Token refresh when expired
					 * - URL rewriting for Codex backend
					 * - Request body transformation
					 * - OAuth header injection
					 * - SSE to JSON conversion for non-tool requests
					 * - Error handling and logging
					 *
					 * @param input - Request URL or Request object
					 * @param init - Request options
					 * @returns Response from Codex API
					 */
					async fetch(
						input: Request | string | URL,
						init?: RequestInit,
					): Promise<Response> {
						// Step 1: Check and refresh token if needed
						let currentAuth = await getAuth();
						if (shouldRefreshToken(currentAuth)) {
							currentAuth = await refreshAndUpdateToken(currentAuth, client);
						}

						// Step 2: Extract and rewrite URL for Codex backend
						const originalUrl = extractRequestUrl(input);
						const url = rewriteUrlForCodex(originalUrl);

						// Step 3: Transform request body with model-specific Codex instructions
						// Instructions are fetched per model family (codex-max, codex, gpt-5.1)
						// Capture original stream value before transformation
						// generateText() sends no stream field, streamText() sends stream=true
						const originalBody = init?.body ? JSON.parse(init.body as string) : {};
						const isStreaming = originalBody.stream === true;

						const transformation = await transformRequestForCodex(
							init,
							url,
							userConfig,
							codexMode,
						);
						const requestInit = transformation?.updatedInit ?? init;

						// Step 4: Create headers with OAuth and ChatGPT account info
						const accessToken =
							currentAuth.type === "oauth" ? currentAuth.access : "";
						const headers = createCodexHeaders(
							requestInit,
							accountId,
							accessToken,
							{
								model: transformation?.body.model,
								promptCacheKey: (transformation?.body as any)?.prompt_cache_key,
							},
						);

						// Step 5: Make request to Codex API
						const response = await fetch(url, {
							...requestInit,
							headers,
						});

						// Step 6: Log response
						logRequest(LOG_STAGES.RESPONSE, {
							status: response.status,
							ok: response.ok,
							statusText: response.statusText,
							headers: Object.fromEntries(response.headers.entries()),
						});

						// Step 7: Handle error or success response
						if (!response.ok) {
							return await handleErrorResponse(response);
						}

						return await handleSuccessResponse(response, isStreaming);
					},
				};
			},
				methods: [
					{
						label: AUTH_LABELS.OAUTH,
						type: "oauth" as const,
					/**
					 * OAuth authorization flow
					 *
					 * Steps:
					 * 1. Generate PKCE challenge and state for security
					 * 2. Start local OAuth callback server on port 1455
					 * 3. Open browser to OpenAI authorization page
					 * 4. Wait for user to complete login
					 * 5. Exchange authorization code for tokens
					 *
					 * @returns Authorization flow configuration
					 */
					authorize: async () => {
						const { pkce, state, url } = await createAuthorizationFlow();
						const serverInfo = await startLocalOAuthServer({ state });

						// Attempt to open browser automatically
						openBrowserUrl(url);

						if (!serverInfo.ready) {
							serverInfo.close();
							return buildManualOAuthFlow(pkce, url);
						}

						return {
							url,
							method: "auto" as const,
							instructions: AUTH_LABELS.INSTRUCTIONS,
							callback: async () => {
								const result = await serverInfo.waitForCode(state);
								serverInfo.close();

								if (!result) {
									return { type: "failed" as const };
								}

								const tokens = await exchangeAuthorizationCode(
									result.code,
									pkce.verifier,
									REDIRECT_URI,
								);

								return tokens?.type === "success"
									? tokens
									: { type: "failed" as const };
							},
						};
					},
					},
					{
						label: AUTH_LABELS.OAUTH_MANUAL,
						type: "oauth" as const,
						authorize: async () => {
							const { pkce, url } = await createAuthorizationFlow();
							return buildManualOAuthFlow(pkce, url);
						},
					},
					{
						label: AUTH_LABELS.API_KEY,
						type: "api" as const,
					},
			],
		},
	};
};

export default OpenAIAuthPlugin;
```

## File: `package.json`
```json
{
  "name": "opencode-openai-codex-auth",
  "version": "4.4.0",
  "description": "OpenAI ChatGPT (Codex backend) OAuth auth plugin for opencode - use your ChatGPT Plus/Pro subscription instead of API credits",
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts",
  "type": "module",
  "license": "MIT",
  "author": "Numman Ali",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/numman-ali/opencode-openai-codex-auth.git"
  },
  "keywords": [
    "opencode",
    "openai",
    "codex",
    "chatgpt",
    "oauth",
    "gpt-5",
    "plugin",
    "auth",
    "chatgpt-plus",
    "chatgpt-pro"
  ],
  "homepage": "https://github.com/numman-ali/opencode-openai-codex-auth#readme",
  "bugs": {
    "url": "https://github.com/numman-ali/opencode-openai-codex-auth/issues"
  },
  "scripts": {
    "build": "tsc && cp lib/oauth-success.html dist/lib/",
    "typecheck": "tsc --noEmit",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest run --coverage"
  },
  "bin": {
    "opencode-openai-codex-auth": "./scripts/install-opencode-codex-auth.js"
  },
  "files": [
    "dist/",
    "assets/",
    "config/",
    "scripts/",
    "README.md",
    "LICENSE"
  ],
  "engines": {
    "node": ">=20.0.0"
  },
  "peerDependencies": {
    "@opencode-ai/plugin": "^1.0.150"
  },
  "devDependencies": {
    "@opencode-ai/plugin": "^1.0.150",
    "@opencode-ai/sdk": "^1.0.150",
    "@types/node": "^24.6.2",
    "@vitest/ui": "^3.2.4",
    "typescript": "^5.9.3",
    "vitest": "^3.2.4"
  },
  "dependencies": {
    "@openauthjs/openauth": "^0.4.3",
    "hono": "^4.10.4",
    "jsonc-parser": "^3.3.1"
  },
  "overrides": {
    "hono": "^4.10.4",
    "vite": "^7.1.12"
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ES2022",
    "lib": [
      "ES2022"
    ],
    "moduleResolution": "bundler",
    "outDir": "./dist",
    "rootDir": "./",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "types": [
      "node"
    ]
  },
  "include": [
    "index.ts",
    "lib/**/*.ts"
  ],
  "exclude": [
    "node_modules",
    "dist",
    "test",
    "**/*.mjs"
  ]
}
```

## File: `vitest.config.ts`
```typescript
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    globals: true,
    environment: 'node',
    include: ['test/**/*.test.ts'],
    exclude: [
      'node_modules/**',
      '.opencode/**',
      'dist/**',
      'tmp/**',
      '**/node_modules/**',
      '**/.opencode/**',
      '**/dist/**',
      '**/tmp/**',
    ],
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['node_modules/', 'dist/', 'test/'],
    },
  },
});
```

## File: `config/README.md`
```markdown
# Configuration

This directory contains the official opencode configuration files for the OpenAI Codex OAuth plugin.

## ⚠️ REQUIRED: Choose the Right Configuration

**Two configuration files are available based on your OpenCode version:**

| File | OpenCode Version | Description |
|------|------------------|-------------|
| [`opencode-modern.json`](./opencode-modern.json) | **v1.0.210+ (Jan 2026+)** | Compact config using variants system - 6 models with built-in reasoning level variants |
| [`opencode-legacy.json`](./opencode-legacy.json) | **v1.0.209 and below** | Extended config with separate model entries for each reasoning level - 20+ individual model definitions |

### Which one should I use?

**If you have OpenCode v1.0.210 or newer** (check with `opencode --version`):
```bash
cp config/opencode-modern.json ~/.config/opencode/opencode.jsonc
```

**If you have OpenCode v1.0.209 or older**:
```bash
cp config/opencode-legacy.json ~/.config/opencode/opencode.jsonc
```

### Why two configs?

OpenCode v1.0.210+ introduced a **variants system** that allows defining reasoning effort levels as variants under a single model. This reduces config size from 572 lines to ~150 lines while maintaining the same functionality.

**What you get:**

| Config File | Model Families | Reasoning Variants | Total Models |
|------------|----------------|-------------------|--------------|
| `opencode-modern.json` | 6 | Built-in variants (low/medium/high/xhigh) | 6 base models with 19 total variants |
| `opencode-legacy.json` | 6 | Separate model entries | 20 individual model definitions |

Both configs provide:
- ✅ All supported GPT 5.2/5.1 variants: gpt-5.2, gpt-5.2-codex, gpt-5.1, gpt-5.1-codex, gpt-5.1-codex-max, gpt-5.1-codex-mini
- ✅ Proper reasoning effort settings for each variant (including `xhigh` for Codex Max/5.2)
- ✅ Context limits (272k context / 128k output for all Codex families)
- ✅ Required options: `store: false`, `include: ["reasoning.encrypted_content"]`
- ✅ Image input support for all models
- ✅ All required metadata for OpenCode features

### Modern Config Benefits (v1.0.210+)

- **74% smaller**: 150 lines vs 572 lines
- **DRY**: Common options defined once at provider level
- **Variant cycling**: Built-in support for `Ctrl+T` to switch reasoning levels
- **Easier maintenance**: Add new variants without copying model definitions

## Usage

1. **Check your OpenCode version**:
   ```bash
   opencode --version
   ```

2. **Copy the appropriate config** based on your version:
   ```bash
   # For v1.0.210+ (recommended):
   cp config/opencode-modern.json ~/.config/opencode/opencode.jsonc

   # For older versions:
   cp config/opencode-legacy.json ~/.config/opencode/opencode.jsonc
   ```

3. **Run opencode**:
   ```bash
   # Modern config (v1.0.210+):
   opencode run "task" --model=openai/gpt-5.2 --variant=medium
   opencode run "task" --model=openai/gpt-5.2 --variant=high

   # Legacy config:
   opencode run "task" --model=openai/gpt-5.2-medium
   opencode run "task" --model=openai/gpt-5.2-high
   ```

> **⚠️ Important**: Use the config file appropriate for your OpenCode version. Using the modern config with an older OpenCode version (v1.0.209 or below) will not work correctly.

> **Note**: The config templates use an **unversioned** plugin entry (`opencode-openai-codex-auth`) so the installer can always pull the latest release. If you need reproducibility, pin a specific version manually.

## Available Models

Both configs provide access to the same model families:

- **gpt-5.2** (none/low/medium/high/xhigh) - Latest GPT 5.2 model with full reasoning support
- **gpt-5.2-codex** (low/medium/high/xhigh) - GPT 5.2 Codex presets
- **gpt-5.1-codex-max** (low/medium/high/xhigh) - Codex Max presets
- **gpt-5.1-codex** (low/medium/high) - Codex model presets
- **gpt-5.1-codex-mini** (medium/high) - Codex mini tier presets
- **gpt-5.1** (none/low/medium/high) - General-purpose reasoning presets

All appear in the opencode model selector as "GPT 5.1 Codex Low (OAuth)", "GPT 5.1 High (OAuth)", etc.

## Configuration Options

See the main [README.md](../../../README.md#configuration) for detailed documentation of all configuration options.

## Version History

- **January 2026 (v1.0.210+)**: Introduced variant system support. Use `opencode-modern.json`
- **December 2025 and earlier**: Use `opencode-legacy.json`
```

## File: `config/minimal-opencode.json`
```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "store": false
      }
    }
  },
  "model": "openai/gpt-5-codex"
}
```

## File: `config/opencode-legacy.json`
```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [
    "opencode-openai-codex-auth"
  ],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "reasoningSummary": "auto",
        "textVerbosity": "medium",
        "include": [
          "reasoning.encrypted_content"
        ],
        "store": false
      },
      "models": {
        "gpt-5.2-none": {
          "name": "GPT 5.2 None (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "none",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.2-low": {
          "name": "GPT 5.2 Low (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "low",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.2-medium": {
          "name": "GPT 5.2 Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.2-high": {
          "name": "GPT 5.2 High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.2-xhigh": {
          "name": "GPT 5.2 Extra High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "xhigh",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.2-codex-low": {
          "name": "GPT 5.2 Codex Low (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "low",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.2-codex-medium": {
          "name": "GPT 5.2 Codex Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.2-codex-high": {
          "name": "GPT 5.2 Codex High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.2-codex-xhigh": {
          "name": "GPT 5.2 Codex Extra High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "xhigh",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-codex-max-low": {
          "name": "GPT 5.1 Codex Max Low (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "low",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-codex-max-medium": {
          "name": "GPT 5.1 Codex Max Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-codex-max-high": {
          "name": "GPT 5.1 Codex Max High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-codex-max-xhigh": {
          "name": "GPT 5.1 Codex Max Extra High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "xhigh",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-codex-low": {
          "name": "GPT 5.1 Codex Low (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "low",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-codex-medium": {
          "name": "GPT 5.1 Codex Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-codex-high": {
          "name": "GPT 5.1 Codex High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-codex-mini-medium": {
          "name": "GPT 5.1 Codex Mini Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-codex-mini-high": {
          "name": "GPT 5.1 Codex Mini High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-none": {
          "name": "GPT 5.1 None (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "none",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-low": {
          "name": "GPT 5.1 Low (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "low",
            "reasoningSummary": "auto",
            "textVerbosity": "low",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-medium": {
          "name": "GPT 5.1 Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        },
        "gpt-5.1-high": {
          "name": "GPT 5.1 High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "high",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        }
      }
    }
  }
}
```

## File: `config/opencode-modern.json`
```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [
    "opencode-openai-codex-auth"
  ],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "reasoningSummary": "auto",
        "textVerbosity": "medium",
        "include": [
          "reasoning.encrypted_content"
        ],
        "store": false
      },
      "models": {
        "gpt-5.2": {
          "name": "GPT 5.2 (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "variants": {
            "none": {
              "reasoningEffort": "none",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "low": {
              "reasoningEffort": "low",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "medium": {
              "reasoningEffort": "medium",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "high": {
              "reasoningEffort": "high",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            },
            "xhigh": {
              "reasoningEffort": "xhigh",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            }
          }
        },
        "gpt-5.2-codex": {
          "name": "GPT 5.2 Codex (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "variants": {
            "low": {
              "reasoningEffort": "low",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "medium": {
              "reasoningEffort": "medium",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "high": {
              "reasoningEffort": "high",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            },
            "xhigh": {
              "reasoningEffort": "xhigh",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            }
          }
        },
        "gpt-5.1-codex-max": {
          "name": "GPT 5.1 Codex Max (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "variants": {
            "low": {
              "reasoningEffort": "low",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            },
            "medium": {
              "reasoningEffort": "medium",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            },
            "high": {
              "reasoningEffort": "high",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            },
            "xhigh": {
              "reasoningEffort": "xhigh",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            }
          }
        },
        "gpt-5.1-codex": {
          "name": "GPT 5.1 Codex (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "variants": {
            "low": {
              "reasoningEffort": "low",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "medium": {
              "reasoningEffort": "medium",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "high": {
              "reasoningEffort": "high",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            }
          }
        },
        "gpt-5.1-codex-mini": {
          "name": "GPT 5.1 Codex Mini (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "variants": {
            "medium": {
              "reasoningEffort": "medium",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "high": {
              "reasoningEffort": "high",
              "reasoningSummary": "detailed",
              "textVerbosity": "medium"
            }
          }
        },
        "gpt-5.1": {
          "name": "GPT 5.1 (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "modalities": {
            "input": [
              "text",
              "image"
            ],
            "output": [
              "text"
            ]
          },
          "variants": {
            "none": {
              "reasoningEffort": "none",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "low": {
              "reasoningEffort": "low",
              "reasoningSummary": "auto",
              "textVerbosity": "low"
            },
            "medium": {
              "reasoningEffort": "medium",
              "reasoningSummary": "auto",
              "textVerbosity": "medium"
            },
            "high": {
              "reasoningEffort": "high",
              "reasoningSummary": "detailed",
              "textVerbosity": "high"
            }
          }
        }
      }
    }
  }
}
```

## File: `docs/DOCUMENTATION.md`
```markdown
# Documentation Structure

This document explains the organization of documentation in this repository.

## Structure Overview

```
├── README.md                      # Main entry point (users)
├── CHANGELOG.md                   # Release history
├── AGENTS.md                      # AI agent guidance
├── docs/
│   ├── index.md                   # GitHub Pages home
│   ├── README.md                  # Documentation portal
│   ├── _config.yml                # GitHub Pages config
│   └── development/               # Developer documentation
│       ├── ARCHITECTURE.md        # Technical design
│       ├── CONFIG_FLOW.md         # Config system internals
│       ├── CONFIG_FIELDS.md       # Config field reference
│       └── TESTING.md             # Test procedures
├── config/
│   ├── README.md                  # Example configs guide
│   ├── opencode-legacy.json       # Legacy full config example (v1.0.209 and below)
│   ├── opencode-modern.json       # Variant config example (v1.0.210+)
│   └── minimal-opencode.json      # Minimal config example
└── tmp/release-notes/             # Detailed release artifacts
    ├── CHANGES.md                 # Detailed v2.1.2 changes
    ├── BUGS_FIXED.md              # Bug analysis
    ├── IMPLEMENTATION_SUMMARY.md  # Implementation details
    └── VERIFICATION.md            # Verification matrix
```

## Document Purposes

### Top Level (Users)
- **README.md** - Quick start, configuration basics, common usage
- **CHANGELOG.md** - Version history, what's new
- **AGENTS.md** - Guidance for AI coding agents

### docs/ (GitHub Pages)
- **index.md** - Landing page with quick links to user and dev docs
- **README.md** - Documentation portal overview
- **development/** - Technical deep dives for developers

### tmp/release-notes/ (Release Artifacts)
- Detailed bug analysis and implementation notes
- Used for preparing release announcements
- Not part of main documentation (too detailed for users)

##  GitHub Pages

Enable GitHub Pages in repository settings:
- **Source**: `main` branch, `/docs` folder
- **URL**: `https://your-username.github.io/opencode-codex-plugin/`

The site automatically serves:
- `docs/index.md` as homepage
- All docs in `docs/` directory
- Development docs prominently featured

## For Users

Start with **[README.md](../../../README.md)** for:
- Installation steps
- Basic configuration
- Quick examples
- Troubleshooting

## For Developers

Start with **[docs/development/ARCHITECTURE.md](ARCHITECTURE.md)** for:
- Technical design decisions
- Request transformation pipeline
- AI SDK compatibility layer
- Testing methodology

## Contributing

See development docs for:
- Code architecture
- Testing procedures
- Configuration system internals
```

## File: `docs/README.md`
```markdown
# Documentation

Welcome to the OpenCode OpenAI Codex Auth Plugin documentation!

## For Users

- **[Getting Started](../../../README.md)** - Installation, configuration, and quick start
- **[Configuration Guide](../../../README.md#configuration)** - Complete config reference
- **[Troubleshooting](../../../README.md#troubleshooting)** - Common issues and debugging
- **[Changelog](../bmad_repo/CHANGELOG.md)** - Version history and release notes

## For Developers

Explore the engineering depth behind this plugin:

- **[Architecture](ARCHITECTURE.md)** - Technical design, request pipeline, AI SDK compatibility
- **[Configuration System](development/CONFIG_FLOW.md)** - How config loading and merging works
- **[Config Fields Guide](development/CONFIG_FIELDS.md)** - Understanding config keys, `id`, and `name`
- **[Testing Guide](../bmad_repo/testing.md)** - Test scenarios, verification procedures, integration testing

## Key Architectural Decisions

This plugin bridges two different systems with careful engineering:

1. **AI SDK Compatibility** - Filters `item_reference` (AI SDK construct) for Codex API compatibility
2. **Stateless Operation** - ChatGPT backend requires `store: false`, verified via testing
3. **Full Context Preservation** - Sends complete message history (IDs stripped) for LLM context
4. **15-Minute Caching** - Prevents GitHub API rate limit exhaustion
5. **Per-Model Configuration** - Enables quality presets with quick switching

**Testing**: 200+ unit tests + integration tests with actual API verification

---

**Quick Links**: [GitHub](https://github.com/your-username/opencode-codex-plugin) • [npm](https://www.npmjs.com/package/opencode-openai-codex-auth) • [Issues](https://github.com/your-username/opencode-codex-plugin/issues)
```

## File: `docs/_config.yml`
```yaml
theme: jekyll-theme-hacker
title: OpenCode Codex Auth Plugin
description: Access GPT-5 Codex through your ChatGPT Plus/Pro subscription
show_downloads: true
```

## File: `docs/configuration.md`
```markdown
# Configuration Guide

Complete reference for configuring the OpenCode OpenAI Codex Auth Plugin.

## Quick Reference

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "reasoningSummary": "auto",
        "textVerbosity": "medium",
        "include": ["reasoning.encrypted_content"],
        "store": false
      },
      "models": {
        "gpt-5.1-codex-low": {
          "name": "GPT 5.1 Codex Low (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "low",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        }
      }
    }
  }
}
```

---

## Configuration Options

### reasoningEffort

Controls computational effort for reasoning.

**GPT-5.2 Values** (per OpenAI API docs and Codex CLI `ReasoningEffort` enum):
- `none` - No dedicated reasoning phase (disables reasoning)
- `low` - Light reasoning
- `medium` - Balanced (default)
- `high` - Deep reasoning
- `xhigh` - Extra depth for long-horizon tasks

**GPT-5.2-Codex Values:**
- `low` - Fastest for code
- `medium` - Balanced (default)
- `high` - Maximum code quality
- `xhigh` - Extra depth for long-horizon tasks

**GPT-5.1 Values** (per OpenAI API docs and Codex CLI `ReasoningEffort` enum):
- `none` - No dedicated reasoning phase (disables reasoning)
- `low` - Light reasoning
- `medium` - Balanced (default)
- `high` - Deep reasoning

**GPT-5.1-Codex / GPT-5.1-Codex-Max Values:**
- `low` - Fastest for code
- `medium` - Balanced (default)
- `high` - Maximum code quality
- `xhigh` - Extra depth (Codex Max only)

**GPT-5.1-Codex-Mini Values:**
- `medium` - Balanced (default)
- `high` - Maximum code quality

**Notes**:
- `none` is supported for GPT-5.2 and GPT-5.1 (general purpose) per OpenAI API documentation
- `none` is NOT supported for Codex variants (including GPT-5.2 Codex) - it auto-converts to `low` for Codex/Codex Max or `medium` for Codex Mini
- `minimal` auto-converts to `low` for Codex models
- `xhigh` is supported for GPT-5.2, GPT-5.2 Codex, and GPT-5.1-Codex-Max; other models downgrade to `high`
- Codex Mini only supports `medium` or `high`; lower settings clamp to `medium`

**Example:**
```json
{
  "options": {
    "reasoningEffort": "high"
  }
}
```

### reasoningSummary

Controls reasoning summary verbosity.

**Values:**
- `auto` - Automatically adapts (default)
- `concise` - Short summaries
- `detailed` - Verbose summaries
- `off` - Disable reasoning summary (Codex Max supports)
- `on` - Force enable summary (Codex Max supports)

**Example:**
```json
{
  "options": {
    "reasoningSummary": "detailed"
  }
}
```

### textVerbosity

Controls output length.

**GPT-5 Values:**
- `low` - Concise
- `medium` - Balanced (default)
- `high` - Verbose

**GPT-5.2-Codex / GPT-5.1-Codex / Codex Max:**
- `medium` or `high` (Codex Max defaults to `medium`)

**Example:**
```json
{
  "options": {
    "textVerbosity": "high"
  }
}
```

### include

Array of additional response fields to include.

**Default**: `["reasoning.encrypted_content"]`

**Why needed**: Enables multi-turn conversations with `store: false` (stateless mode)

**Example:**
```json
{
  "options": {
    "include": ["reasoning.encrypted_content"]
  }
}
```

### store

Controls server-side conversation persistence.

**⚠️ Required**: `false` (for AI SDK 2.0.50+ compatibility)

**Values:**
- `false` - Stateless mode (required for Codex API)
- `true` - Server-side storage (not supported by Codex API)

**Why required:**
AI SDK 2.0.50+ automatically uses `item_reference` items when `store: true`. The Codex API requires stateless operation (`store: false`), where references cannot be resolved.

**Example:**
```json
{
  "options": {
    "store": false
  }
}
```

**Note:** The plugin automatically injects this via a `chat.params` hook, but explicit configuration is recommended for clarity.

---

## Configuration Patterns

### Pattern 1: Global Options

Apply same settings to all models:

```json
{
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "high",
        "textVerbosity": "high",
        "store": false
      }
    }
  }
}
```

**Use when**: You want consistent behavior across all models.

### Pattern 2: Per-Model Options

Different settings for different models:

```json
{
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "store": false
      },
      "models": {
        "gpt-5-codex-fast": {
          "name": "Fast Codex",
          "options": {
            "reasoningEffort": "low",
            "store": false
          }
        },
        "gpt-5-codex-smart": {
          "name": "Smart Codex",
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "store": false
          }
        }
      }
    }
  }
}
```

**Use when**: You want quick-switch presets for different tasks.

**Precedence**: Model options override global options.

### Pattern 3: Config Key vs Name

**Understanding the fields:**

```json
{
  "models": {
    "my-custom-id": {           // ← Config key (used everywhere)
      "name": "My Display Name",  // ← Shows in TUI
      "options": { ... }
    }
  }
}
```

- **Config key** (`my-custom-id`): Used in CLI, config lookups, TUI persistence
- **`name` field**: Friendly display name in model selector
- **`id` field**: DEPRECATED - not used by OpenAI provider

**Example Usage:**
```bash
# Use the config key in CLI
opencode run "task" --model=openai/my-custom-id

# TUI shows: "My Display Name"
```

> **⚠️ Recommendation:** Stick to the official presets in `opencode-modern.json` (v1.0.210+) or `opencode-legacy.json` rather than creating custom model variants. GPT 5 models need specific configurations to work reliably.

See [development/CONFIG_FIELDS.md](development/CONFIG_FIELDS.md) for complete explanation.

---

## Advanced Scenarios

### Scenario: Quick Switch Presets

Create named variants for common tasks:

```json
{
  "models": {
    "codex-quick": {
      "name": "⚡ Quick Code",
      "options": {
        "reasoningEffort": "low",
        "store": false
      }
    },
    "codex-balanced": {
      "name": "⚖️ Balanced Code",
      "options": {
        "reasoningEffort": "medium",
        "store": false
      }
    },
    "codex-quality": {
      "name": "🎯 Max Quality",
      "options": {
        "reasoningEffort": "high",
        "reasoningSummary": "detailed",
        "store": false
      }
    }
  }
}
```

### Scenario: Per-Agent Models

Different agents use different models:

```json
{
  "agent": {
    "commit": {
      "model": "openai/gpt-5.1-codex-low",
      "prompt": "Generate concise commit messages"
    },
    "review": {
      "model": "openai/gpt-5.1-codex-high",
      "prompt": "Thorough code review"
    }
  }
}
```

### Scenario: Project-Specific Overrides

Global config has defaults, project overrides for specific work:

**~/.config/opencode/opencode.jsonc** (global, preferred):
```json
{
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "store": false
      }
    }
  }
}
```

**my-project/.opencode.json** (project):
```json
{
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "high",
        "store": false
      }
    }
  }
}
```

Result: Project uses `high`, other projects use `medium`.

---

## Plugin Configuration

Advanced plugin settings in `~/.opencode/openai-codex-auth-config.json`:

```json
{
  "codexMode": true
}
```

### CODEX_MODE

**What it does:**
- `true` (default): Uses Codex-OpenCode bridge prompt (Task tool & MCP aware)
- `false`: Uses legacy tool remap message
- Bridge prompt content is synced with the latest Codex CLI release (ETag-cached)

**When to disable:**
- Compatibility issues with OpenCode updates
- Testing different prompt styles
- Debugging tool call issues

**Override with environment variable:**
```bash
CODEX_MODE=0 opencode run "task"  # Temporarily disable
CODEX_MODE=1 opencode run "task"  # Temporarily enable
```

### Prompt caching

- When OpenCode provides a `prompt_cache_key` (its session identifier), the plugin forwards it directly to Codex.
- The same value is sent via headers (`conversation_id`, `session_id`) and request body, reducing latency and token usage.
- The plugin does not synthesize a fallback key; hosts that omit `prompt_cache_key` will see uncached behaviour until they provide one.
- No configuration needed—cache headers are injected during request transformation.

### Usage limit messaging

- When the ChatGPT subscription hits a limit, the plugin returns a Codex CLI-style summary (5-hour + weekly windows).
- Messages bubble up in OpenCode exactly where SDK errors normally surface.
- Helpful when working inside the OpenCode UI or CLI—users immediately see reset timing.

---

## Configuration Files

**Provided Examples:**
- [config/opencode-modern.json](../config/opencode-modern.json) - Variants-based config for OpenCode v1.0.210+
- [config/opencode-legacy.json](../config/opencode-legacy.json) - Legacy full list for v1.0.209 and below

> **⚠️ REQUIRED:** You MUST use the config that matches your OpenCode version (`opencode-modern.json` or `opencode-legacy.json`). Minimal configs are NOT supported for GPT 5 models and will fail unpredictably. OpenCode's auto-compaction and usage widgets also require the full config's per-model `limit` metadata.

**Your Configs:**
- `~/.config/opencode/opencode.jsonc` - Global config (preferred)
- `~/.config/opencode/opencode.json` - Global config (fallback)
- `<project>/.opencode.json` - Project-specific config
- `~/.opencode/openai-codex-auth-config.json` - Plugin config

---

## Validation

### Check Config is Valid

```bash
# OpenCode will show errors if config is invalid
opencode
```

### Verify Model Resolution

```bash
# Enable debug logging
DEBUG_CODEX_PLUGIN=1 opencode run "test" --model=openai/your-model-name
```

Look for:
```
[openai-codex-plugin] Model config lookup: "your-model-name" → normalized to "gpt-5-codex" for API {
  hasModelSpecificConfig: true,
  resolvedConfig: { ... }
}
```

### Test Per-Model Options

```bash
# Run with different models, check logs show different options
ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode run "test" --model=openai/gpt-5-codex-low
ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode run "test" --model=openai/gpt-5-codex-high

# Compare reasoning.effort in logs
cat ~/.opencode/logs/codex-plugin/request-*-after-transform.json | jq '.reasoning.effort'
```

---

## Migration Guide

### From Old Config Names

Old verbose names still work:

**⚠️ IMPORTANT:** Old configs with GPT 5.0 models are deprecated. You MUST migrate to the new GPT 5.x configs (`opencode-modern.json` or `opencode-legacy.json`).

**Old config (deprecated):**
```json
{
  "models": {
    "gpt-5-codex-low": {
      "name": "GPT 5 Codex Low (OAuth)",
      "options": { "reasoningEffort": "low" }
    }
  }
}
```

**New config (required):**

Use the official config file (`opencode-modern.json` for v1.0.210+, `opencode-legacy.json` for older) which includes:

```json
{
  "models": {
    "gpt-5.1-codex-low": {
      "name": "GPT 5.1 Codex Low (OAuth)",
      "limit": {
        "context": 272000,
        "output": 128000
      },
      "options": {
        "reasoningEffort": "low",
        "reasoningSummary": "auto",
        "textVerbosity": "medium",
        "include": ["reasoning.encrypted_content"],
        "store": false
      }
    }
  }
}
```

**Benefits:**
- GPT 5.2/5.1 support (5.0 is deprecated)
- Proper limit metadata for OpenCode features
- Verified configuration that works reliably

---

## Common Patterns

### Pattern: Task-Based Presets

```json
{
  "models": {
    "quick-chat": {
      "name": "Quick Chat",
      "options": {
        "reasoningEffort": "minimal",
        "textVerbosity": "low",
        "store": false
      }
    },
    "code-gen": {
      "name": "Code Generation",
      "options": {
        "reasoningEffort": "medium",
        "store": false
      }
    },
    "debug-help": {
      "name": "Debug Analysis",
      "options": {
        "reasoningEffort": "high",
        "reasoningSummary": "detailed",
        "store": false
      }
    }
  }
}
```

### Pattern: Cost vs Quality

```json
{
  "models": {
    "economy": {
      "name": "Economy Mode",
      "options": {
        "reasoningEffort": "low",
        "textVerbosity": "low",
        "store": false
      }
    },
    "premium": {
      "name": "Premium Mode",
      "options": {
        "reasoningEffort": "high",
        "textVerbosity": "high",
        "store": false
      }
    }
  }
}
```

---

## Troubleshooting Config

### Model Not Found

**Error**: `Model 'openai/my-model' not found`

**Cause**: Config key doesn't match model name in command

**Fix**: Use exact config key:
```json
{ "models": { "my-model": { ... } } }
```
```bash
opencode run "test" --model=openai/my-model  # Must match exactly
```

### Per-Model Options Not Applied

**Check**: Is config key used for lookup?

```bash
DEBUG_CODEX_PLUGIN=1 opencode run "test" --model=openai/your-model
```

Look for `hasModelSpecificConfig: true` in debug output.

### Options Ignored

**Cause**: Model normalizes before lookup

**Example Problem:**
```json
{ "models": { "gpt-5.1-codex": { "options": { ... } } } }
```
```bash
--model=openai/gpt-5.1-codex-low  # Normalizes to "gpt-5.1-codex" before lookup
```

**Fix**: Use exact name you specify in CLI as config key.

> **⚠️ Best Practice:** Use the official `opencode-modern.json` or `opencode-legacy.json` configuration instead of creating custom configs. This ensures proper model normalization and compatibility with GPT 5 models.

---

**Next**: [Troubleshooting](troubleshooting.md) | [Back to Documentation Home](index.md)
```

## File: `docs/getting-started.md`
```markdown
# Getting Started

Complete installation and setup guide for the OpenCode OpenAI Codex Auth Plugin.

## ⚠️ Before You Begin

**This plugin is for personal development use only.** It uses OpenAI's official OAuth authentication for individual coding assistance with your ChatGPT Plus/Pro subscription.

**Not intended for:** Commercial services, API resale, multi-user applications, or any use that violates [OpenAI's Terms of Use](https://openai.com/policies/terms-of-use/).

For production applications, use the [OpenAI Platform API](https://platform.openai.com/).

---

## Prerequisites

- **OpenCode** installed ([installation guide](https://opencode.ai))
- **ChatGPT Plus or Pro subscription** (required for Codex access)
- **Node.js** 20+ (for OpenCode)

## Installation

### One-Command Install/Update (Recommended)

Works on **Windows, macOS, and Linux**:

```bash
npx -y opencode-openai-codex-auth@latest
```

This writes the **global** config at `~/.config/opencode/opencode.jsonc` (falls back to `.json` if needed), backs it up, and clears the OpenCode plugin cache so the latest version installs.

Need legacy config (OpenCode v1.0.209 and below)?

```bash
npx -y opencode-openai-codex-auth@latest --legacy
```

---

### Step 1: Add Plugin to Config

OpenCode automatically installs plugins - no `npm install` needed!

**Choose your configuration style:**

#### ⚠️ REQUIRED: Full Configuration (Only Supported Setup)

**IMPORTANT**: You MUST use the full configuration. This is the ONLY officially supported setup for GPT 5.x models.

**Why the full config is required:**
- GPT 5 models can be temperamental and need proper configuration
- Minimal configs are NOT supported and will fail unpredictably
- OpenCode features require proper model metadata
- This configuration has been tested and verified to work

Add this to `~/.config/opencode/opencode.jsonc` (or `.json`):

**Tip**: The snippet below is a truncated excerpt. For the complete legacy list, copy `config/opencode-legacy.json`. For the modern variants config (OpenCode v1.0.210+), use `config/opencode-modern.json`.

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "reasoningSummary": "auto",
        "textVerbosity": "medium",
        "include": ["reasoning.encrypted_content"],
        "store": false
      },
      "models": {
        "gpt-5.1-codex-low": {
          "name": "GPT 5.1 Codex Low (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "low",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-codex-medium": {
          "name": "GPT 5.1 Codex Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-codex-high": {
          "name": "GPT 5.1 Codex High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-codex-max": {
          "name": "GPT 5.1 Codex Max (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-codex-max-low": {
          "name": "GPT 5.1 Codex Max Low (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "low",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-codex-max-medium": {
          "name": "GPT 5.1 Codex Max Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-codex-max-high": {
          "name": "GPT 5.1 Codex Max High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-codex-max-xhigh": {
          "name": "GPT 5.1 Codex Max Extra High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "xhigh",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-codex-mini-medium": {
          "name": "GPT 5.1 Codex Mini Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-codex-mini-high": {
          "name": "GPT 5.1 Codex Mini High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-low": {
          "name": "GPT 5.1 Low (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "low",
            "reasoningSummary": "auto",
            "textVerbosity": "low",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-medium": {
          "name": "GPT 5.1 Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        },
        "gpt-5.1-high": {
          "name": "GPT 5.1 High (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed",
            "textVerbosity": "high",
            "include": ["reasoning.encrypted_content"],
            "store": false
          }
        }
      }
    }
  }
}
```

  **What you get:**
  - ✅ GPT 5.2 (None/Low/Medium/High/xHigh reasoning)
  - ✅ GPT 5.2 Codex (Low/Medium/High/xHigh reasoning)
  - ✅ GPT 5.1 Codex Max (Low/Medium/High/xHigh reasoning presets)
  - ✅ GPT 5.1 Codex (Low/Medium/High reasoning)
  - ✅ GPT 5.1 Codex Mini (Medium/High reasoning)
  - ✅ GPT 5.1 (None/Low/Medium/High reasoning)
  - ✅ 272k context + 128k output window for all GPT 5.x presets.
  - ✅ All visible in OpenCode model selector
  - ✅ Optimal settings for each reasoning level

> **Note**: All `gpt-5.1-codex-mini*` presets use 272k context / 128k output limits.
>
> **Note**: Codex Max presets map to the `gpt-5.1-codex-max` slug with 272k context and 128k output. Use `gpt-5.1-codex-max-low/medium/high/xhigh` to pick the reasoning level (only `-xhigh` uses `xhigh` reasoning).
>
> **Note**: GPT 5.2 and GPT 5.2 Codex support `xhigh` reasoning. Use explicit reasoning levels (e.g., `gpt-5.2-xhigh`, `gpt-5.2-codex-xhigh`) for precise control.

Prompt caching is enabled out of the box: when OpenCode sends its session identifier as `prompt_cache_key`, the plugin forwards it untouched so multi-turn runs reuse prior work. The CODEX_MODE bridge prompt bundled with the plugin is kept in sync with the latest Codex CLI release, so the OpenCode UI and Codex share the same tool contract. If you hit your ChatGPT subscription limits, the plugin returns a friendly Codex-style message with the 5-hour and weekly usage windows so you know when capacity resets.

> **⚠️ CRITICAL:** This full configuration is REQUIRED. OpenCode's context auto-compaction and usage sidebar only work with this full configuration. GPT 5 models are temperamental and need proper setup - minimal configurations are NOT supported.

#### ❌ Minimal Configuration (NOT SUPPORTED - DO NOT USE)

**DO NOT use minimal configurations** - they will NOT work reliably with GPT 5:

```json
// ❌ DO NOT USE THIS
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-openai-codex-auth"],
  "model": "openai/gpt-5-codex"
}
```

**Why this doesn't work:**
- GPT 5 models need proper configuration to work reliably
- Missing model metadata breaks OpenCode features
- Cannot guarantee stable operation

### Step 2: Authenticate

```bash
opencode auth login
```

1. Select **"OpenAI"**
2. Choose **"ChatGPT Plus/Pro (Codex Subscription)"**
3. Browser opens automatically for OAuth flow
4. Log in with your ChatGPT account
5. Done! Token saved to `~/.opencode/auth/openai.json`

**⚠️ Important**: If you have the official Codex CLI running, stop it first (both use port 1455 for OAuth callback).

**Manual fallback**: On SSH/WSL/remote environments, pick **"ChatGPT Plus/Pro (Manual URL Paste)"** and paste the full redirect URL after login.

### Step 3: Test It

```bash
# Quick test
opencode run "write hello world to test.txt" --model=openai/gpt-5.1-codex-medium

# Or start interactive session
opencode
```

You'll see all 22 GPT 5.x variants (GPT 5.2, GPT 5.2 Codex, Codex Max, Codex, Codex Mini, and GPT 5.1 presets) in the model selector!

---

## Configuration Locations

OpenCode checks multiple config files in order:

1. **Project config**: `./.opencode.json` (current directory)
2. **Parent configs**: Walks up directory tree
3. **Global config**: `~/.config/opencode/opencode.jsonc` (or `~/.config/opencode/opencode.json`)

**Recommendation**: Use global config for plugin, project config for model/agent overrides.

---

## ⚠️ Updating the Plugin (Important!)

OpenCode caches plugins. To install the latest version, just re-run the installer:

```bash
npx -y opencode-openai-codex-auth@latest
```

Legacy OpenCode (v1.0.209 and below):

```bash
npx -y opencode-openai-codex-auth@latest --legacy
```

## Uninstall

```bash
npx -y opencode-openai-codex-auth@latest --uninstall
npx -y opencode-openai-codex-auth@latest --uninstall --all
```

**When to update:**
- New features released
- Bug fixes available
- Security updates

**Check for updates**: [Releases Page](https://github.com/numman-ali/opencode-openai-codex-auth/releases)

**Pro tip**: Subscribe to release notifications on GitHub to get notified of updates.

---

## Local Development Setup

For plugin development or testing unreleased changes:

```json
{
  "plugin": ["file:///absolute/path/to/opencode-openai-codex-auth/dist"]
}
```

**Note**: Must point to `dist/` folder (built output), not root.

**Build the plugin:**
```bash
cd opencode-openai-codex-auth
npm install
npm run build
```

---

## Verifying Installation

### Check Plugin is Loaded

```bash
opencode --version
# Should not show any plugin errors
```

### Check Authentication

```bash
cat ~/.opencode/auth/openai.json
# Should show OAuth credentials (if authenticated)
```

### Test API Access

```bash
# Enable logging to verify requests
ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode run "test" --model=openai/gpt-5-codex

# Check logs
ls ~/.opencode/logs/codex-plugin/
# Should show request logs
```

---

## Next Steps

- [Configuration Guide](configuration.md) - Advanced config options
- [Troubleshooting](troubleshooting.md) - Common issues and solutions
- [Developer Docs](ARCHITECTURE.md) - Technical deep dive

**Back to**: [Documentation Home](index.md)
```

## File: `docs/index.md`
```markdown
# OpenCode OpenAI Codex Auth Plugin

> Access GPT-5 Codex through your ChatGPT Plus/Pro subscription in OpenCode

[![npm version](https://badge.fury.io/js/opencode-openai-codex-auth.svg)](https://www.npmjs.com/package/opencode-openai-codex-auth)
[![Tests](https://github.com/numman-ali/opencode-openai-codex-auth/actions/workflows/ci.yml/badge.svg)](https://github.com/numman-ali/opencode-openai-codex-auth/actions)

> **Found this useful?**
> Follow me on [X @nummanali](https://x.com/nummanali) for future updates and more projects!

## ⚠️ Usage Notice

**This plugin is for personal development use only.** It uses OpenAI's official OAuth authentication (the same method as OpenAI's official Codex CLI) for individual coding assistance with your ChatGPT Plus/Pro subscription.

**Not for:** Commercial services, API resale, or multi-user applications. For production use, see [OpenAI Platform API](https://platform.openai.com/).

Users are responsible for compliance with [OpenAI's Terms of Use](https://openai.com/policies/terms-of-use/).

---

## Quick Links

### For Users
- [Getting Started](../bmad_repo/getting-started.md) - Complete installation and setup guide
- [Configuration Guide](configuration.md) - Advanced config options and patterns
- [Troubleshooting](troubleshooting.md) - Debug techniques and common issues
- [Privacy & Data Handling](privacy.md) - How your data is handled and protected
- [Release Notes](https://github.com/numman-ali/opencode-openai-codex-auth/releases) - Version history and updates

### For Developers
Explore the engineering depth behind this plugin:
- [Architecture](ARCHITECTURE.md) - Technical design, AI SDK compatibility, store:false explained
- [Config System](development/CONFIG_FLOW.md) - How configuration loading and merging works
- [Config Fields](development/CONFIG_FIELDS.md) - Understanding config keys, `id`, and `name` fields
- [Testing Guide](../bmad_repo/testing.md) - Test scenarios, integration testing, verification matrix

---

## Getting Started

### Installation

One-command install/update (global config):

```bash
npx -y opencode-openai-codex-auth@latest
```

Legacy OpenCode (v1.0.209 and below):

```bash
npx -y opencode-openai-codex-auth@latest --legacy
```

Then run OpenCode and authenticate:

```bash
# 1. Add plugin to ~/.config/opencode/opencode.jsonc (or .json)
# 2. Run OpenCode
opencode

# 3. Authenticate
opencode auth login
```

If the browser callback fails (SSH/WSL/remote), choose **"ChatGPT Plus/Pro (Manual URL Paste)"** and paste the full redirect URL.

### Updating

Re-run the installer to update:

```bash
npx -y opencode-openai-codex-auth@latest
```

### Quick Test

```bash
opencode run "write hello world to test.txt" --model=openai/gpt-5.2 --variant=medium
```

---

## Features

✅ **OAuth Authentication** - Secure ChatGPT Plus/Pro login
✅ **GPT 5.2 + GPT 5.2 Codex + GPT 5.1 Models** - 22 pre-configured variants across GPT 5.2, GPT 5.2 Codex, GPT 5.1, Codex, Codex Max, Codex Mini
✅ **Variant system support** - Works with OpenCode v1.0.210+ model variants and legacy presets
✅ **Per-Model Configuration** - Different reasoning effort, including `xhigh` for GPT 5.2, GPT 5.2 Codex, and Codex Max
✅ **Multi-Turn Conversations** - Full conversation history with stateless backend
✅ **Verified Configuration** - Use `config/opencode-modern.json` (v1.0.210+) or `config/opencode-legacy.json` (older)
✅ **Comprehensive Testing** - 200+ unit tests + integration tests

> **⚠️ Important**: GPT 5 models can be temperamental. Use the official config for your OpenCode version (`opencode-modern.json` or `opencode-legacy.json`). Older GPT 5.0 models are deprecated.

---

## Why This Plugin?

**Use your ChatGPT subscription instead of OpenAI API credits**

- No separate API key needed
- Access Codex models through ChatGPT Plus/Pro
- Same OAuth login as official Codex CLI
- Full feature parity with Codex CLI

---

## How It Works

The plugin intercepts OpenCode's OpenAI SDK requests and transforms them for the ChatGPT backend API:

1. **OAuth Token Management** - Handles token refresh automatically
2. **Request Transformation** - Converts OpenCode SDK format → Codex API format
3. **AI SDK Compatibility** - Filters SDK-specific constructs for Codex API
4. **Stateless Operation** - Works with ChatGPT backend's `store: false` requirement

See [Architecture](ARCHITECTURE.md) for technical details.

---

## Development

This plugin represents significant engineering effort to bridge OpenCode and the ChatGPT Codex backend:

- **7-step fetch flow** with precise transformations
- **AI SDK compatibility layer** handling `item_reference` and other SDK constructs
- **Stateless multi-turn** conversations via encrypted reasoning content
- **15-minute caching** to prevent GitHub API rate limits
- **Comprehensive test coverage** with actual API verification

**Explore the development docs** to see the depth of implementation:
- [Architecture Deep Dive](ARCHITECTURE.md)
- [Configuration System Internals](development/CONFIG_FLOW.md)
- [Testing & Verification](../bmad_repo/testing.md)

---

## Support

- **Issues**: [GitHub Issues](https://github.com/numman-ali/opencode-openai-codex-auth/issues)
- **Releases**: [Release Notes](https://github.com/numman-ali/opencode-openai-codex-auth/releases)
- **Main Repo**: [GitHub](https://github.com/numman-ali/opencode-openai-codex-auth)

---

## License

MIT License with Usage Disclaimer - See [LICENSE](../LICENSE) for details

---

**Trademark Notice:** Not affiliated with OpenAI. ChatGPT, GPT-5, Codex, and OpenAI are trademarks of OpenAI, L.L.C.
```

## File: `docs/privacy.md`
```markdown
# Privacy & Data Handling

This page explains how the OpenCode OpenAI Codex Auth Plugin handles your data and protects your privacy.

## Overview

This plugin prioritizes user privacy and data security. We believe in transparency about data handling and giving you full control over your information.

---

## What We Collect

**Nothing.** This plugin does not collect, store, or transmit usage data to third parties.

- ❌ No telemetry
- ❌ No analytics
- ❌ No usage tracking
- ❌ No personal information collection

---

## Data Storage

All data is stored **locally on your machine**:

### OAuth Tokens
- **Location:** `~/.opencode/auth/openai.json`
- **Contents:** Access tokens, refresh tokens, expiration timestamps
- **Managed by:** OpenCode's credential management system
- **Security:** File permissions restrict access to your user account

### Cache Files
- **Location:** `~/.opencode/cache/`
- **Contents:**
  - `codex-instructions.txt` - Codex system instructions (fetched from GitHub)
  - `codex-instructions-meta.json` - ETag and timestamp metadata
- **Purpose:** Reduce GitHub API calls and improve performance
- **TTL:** 15 minutes (automatically refreshes when stale)

### Debug Logs
- **Location:** `~/.opencode/logs/codex-plugin/`
- **Contents:** Request/response logs (only when `ENABLE_PLUGIN_REQUEST_LOGGING=1` is set)
- **Includes:**
  - API request bodies
  - API response data
  - Timestamps
  - Configuration used
- **⚠️ Warning:** Logs may contain your prompts and model responses - handle with care

---

## Data Transmission

### Direct to OpenAI
All API requests go **directly from your machine to OpenAI's servers**:
- ✅ No intermediary proxies
- ✅ No third-party data collection
- ✅ HTTPS encrypted communication
- ✅ OAuth-secured authentication

### What Gets Sent to OpenAI
When you use the plugin, the following is transmitted to OpenAI:
- Your prompts and conversation history
- OAuth access token (for authentication)
- ChatGPT account ID (from token JWT)
- Configuration options (reasoning effort, verbosity, etc.)
- Model selection

**Note:** This is identical to what the official OpenAI Codex CLI sends.

### What Does NOT Get Sent
- ❌ Your filesystem contents (unless explicitly requested via tools)
- ❌ Personal information beyond what's in your prompts
- ❌ Usage statistics or analytics
- ❌ Plugin version or system information

---

## Third-Party Services

### GitHub API
The plugin fetches Codex instructions from GitHub:
- **URL:** `https://api.github.com/repos/openai/codex/releases/latest`
- **Purpose:** Get latest Codex system instructions
- **Frequency:** Once per 15 minutes (cached with ETag)
- **Data sent:** HTTP GET request (no personal data)
- **Rate limiting:** 60 requests/hour (unauthenticated)

### OpenAI Services
All interactions with OpenAI go through:
- **OAuth:** `https://chatgpt.com/oauth`
- **API:** `https://chatgpt.com/backend-api/conversation`

See [OpenAI Privacy Policy](https://openai.com/policies/privacy-policy/) for how OpenAI handles data.

---

## Your Data Rights

You have complete control over your data:

### Delete OAuth Tokens
```bash
opencode auth logout
# Or manually:
rm ~/.opencode/auth/openai.json
```

### Delete Cache Files
```bash
rm -rf ~/.opencode/cache/
```

### Delete Logs
```bash
rm -rf ~/.opencode/logs/codex-plugin/
```

### Revoke OAuth Access
1. Visit [ChatGPT Settings → Authorized Apps](https://chatgpt.com/settings/apps)
2. Find "OpenCode" or "Codex CLI"
3. Click "Revoke"

This immediately invalidates all access tokens.

---

## Security Measures

### Token Protection
- **Local storage only:** Tokens never leave your machine except when sent to OpenAI for authentication
- **File permissions:** Auth files are readable only by your user account
- **No logging:** OAuth tokens are never written to debug logs
- **Automatic refresh:** Expired tokens are refreshed automatically

### PKCE Flow
The plugin uses **PKCE (Proof Key for Code Exchange)** for OAuth:
- Prevents authorization code interception attacks
- Industry-standard security for OAuth 2.0
- Same method used by OpenAI's official Codex CLI

### HTTPS Encryption
All network communication uses HTTPS:
- OAuth authorization: Encrypted
- API requests: Encrypted
- Token refresh: Encrypted

---

## Compliance

### OpenAI's Privacy Policy
When using this plugin, you are subject to:
- [OpenAI Privacy Policy](https://openai.com/policies/privacy-policy/)
- [OpenAI Terms of Use](https://openai.com/policies/terms-of-use/)

**Your responsibility:** Ensure your usage complies with OpenAI's policies.

### GDPR Considerations
This plugin:
- ✅ Does not collect personal data
- ✅ Does not process data on behalf of third parties
- ✅ Stores data locally under your control
- ✅ Provides clear data deletion mechanisms

However, data sent to OpenAI is subject to OpenAI's privacy practices.

---

## Transparency

### Open Source
The entire plugin source code is available at:
- **GitHub:** [https://github.com/numman-ali/opencode-openai-codex-auth](https://github.com/numman-ali/opencode-openai-codex-auth)

You can:
- Review all code
- Audit data handling
- Verify no hidden telemetry
- Inspect network requests

### No Hidden Behavior
- No obfuscated code
- No minified dependencies
- All network requests are documented
- Debug logging shows exactly what's sent to APIs

---

## Questions?

For privacy-related questions:
- **Plugin-specific:** [GitHub Issues](https://github.com/numman-ali/opencode-openai-codex-auth/issues)
- **OpenAI data handling:** [OpenAI Support](https://help.openai.com/)
- **Security concerns:** See [SECURITY.md](../bmad_repo/SECURITY.md)

---

**Last Updated:** 2025-10-12

**Back to:** [Documentation Home](index.md) | [Getting Started](../bmad_repo/getting-started.md)
```

## File: `docs/troubleshooting.md`
```markdown
# Troubleshooting Guide

Common issues and debugging techniques for the OpenCode OpenAI Codex Auth Plugin.

## Authentication Issues

### "401 Unauthorized" Error

**Symptoms:**
```
Error: 401 Unauthorized
Failed to access Codex API
```

**Causes:**
1. Token expired
2. Not authenticated yet
3. Invalid credentials

**Solutions:**

**1. Re-authenticate:**
```bash
opencode auth login
```

**2. Check auth file exists:**
```bash
cat ~/.opencode/auth/openai.json
# Should show OAuth credentials
```

**3. Check token expiration:**
```bash
# Token has "expires" timestamp
cat ~/.opencode/auth/openai.json | jq '.expires'

# Compare to current time
date +%s000  # Current timestamp in milliseconds
```

### Browser Doesn't Open for OAuth

**Symptoms:**
- `opencode auth login` succeeds but no browser window
- OAuth callback times out

**Solutions:**

**1. Manual browser open:**
```bash
# The auth URL is shown in console - copy and paste to browser manually
```

**1a. Manual URL Paste login:**
- Re-run `opencode auth login`
- Select **"ChatGPT Plus/Pro (Manual URL Paste)"**
- Paste the full redirect URL after login

**2. Check port 1455 availability:**
```bash
# See if something is using the OAuth callback port
lsof -i :1455
```

**3. Official Codex CLI conflict:**
- Stop Codex CLI if running
- Both use port 1455 for OAuth

### "Invalid Session" or "Authorization session expired"

**Symptoms:**
- Browser shows: `Your authorization session was not initialized or has expired`

**Solutions:**
- Re-run `opencode auth login` to generate a fresh URL
- Open the **"Go to"** URL directly in your browser (don’t use a stale link)
- If you’re on SSH/WSL/remote, choose **"ChatGPT Plus/Pro (Manual URL Paste)"**

### "403 Forbidden" Error

**Cause**: ChatGPT subscription issue

**Check:**
1. Active ChatGPT Plus or Pro subscription
2. Subscription not expired
3. Billing is current

**Solution**: Visit [ChatGPT](https://chatgpt.com) and verify subscription status

---

## Model Issues

### "Model not found"

**Error**: `Model 'openai/gpt-5-codex-low' not found`

**Cause 1: Config key mismatch**

**Check your config:**
```json
{
  "models": {
    "gpt-5-codex-low": { ... }  // ← This is the key
  }
}
```

**CLI must match exactly:**
```bash
opencode run "test" --model=openai/gpt-5-codex-low  # Must match config key
```

**Cause 2: Missing provider prefix**

**❌ Wrong:**
```yaml
model: gpt-5-codex-low
```

**✅ Correct:**
```yaml
model: openai/gpt-5-codex-low
```

### Per-Model Options Not Applied

**Symptom**: All models behave the same despite different `reasoningEffort`

**Debug:**
```bash
DEBUG_CODEX_PLUGIN=1 opencode run "test" --model=openai/your-model
```

**Look for:**
```
hasModelSpecificConfig: true  ← Should be true
resolvedConfig: { reasoningEffort: 'low', ... }  ← Should show your options
```

**If `false`**: Config lookup failed

**Common causes:**
1. Model name in CLI doesn't match config key
2. Typo in config file
3. Wrong config file location

---

## Multi-Turn Issues

### "Item not found" Errors

**Error:**
```
AI_APICallError: Item with id 'msg_abc123' not found.
Items are not persisted when `store` is set to false.
```

**Cause**: Old plugin version (fixed in v2.1.2+)

**Solution:**
```bash
# Update plugin
npx -y opencode-openai-codex-auth@latest

# Restart OpenCode
opencode
```

**Verify fix:**
```bash
DEBUG_CODEX_PLUGIN=1 opencode
> write test.txt
> read test.txt
> what did you write?
```

Should see: `Successfully removed all X message IDs`

### Context Not Preserved

**Symptom**: Model doesn't remember previous turns

**Check logs:**
```bash
ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode
> first message
> second message
```

**Verify:**
```bash
# Turn 2 should have full history
cat ~/.opencode/logs/codex-plugin/request-*-after-transform.json | jq '.body.input | length'
# Should show increasing count (3, 5, 7, 9, ...)
```

**What to check:**
1. Full message history present (not just current turn)
2. No `item_reference` items (filtered out)
3. All IDs stripped (`jq '.body.input[].id'` should all be `null`)

---

## Request Errors

### "400 Bad Request"

**Check error details:**
```bash
ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode run "test"

# Read error
cat ~/.opencode/logs/codex-plugin/request-*-error-response.json
```

**Common causes:**
1. Invalid options for model (e.g., `minimal` for gpt-5-codex)
2. Malformed request body
3. Unsupported parameter

### "Rate Limit Exceeded"

**Error:**
```
Rate limit reached for gpt-5-codex
```

**Solutions:**

**1. Wait for reset:**
Check headers in response logs:
```bash
cat ~/.opencode/logs/codex-plugin/request-*-response.json | jq '.headers["x-codex-primary-reset-after-seconds"]'
```

**2. Switch to different model:**
```bash
# If codex is rate limited, try gpt-5
opencode run "task" --model=openai/gpt-5
```

### "Context Window Exceeded"

**Error:**
```
Your input exceeds the context window
```

**Cause**: Too much conversation history

**Solutions:**

**1. Start new conversation:**
```bash
# Exit and restart OpenCode (clears history)
```

**2. Use compact mode** (if OpenCode supports it)

**3. Switch to model with larger context:**
- gpt-5-codex has larger context than gpt-5-nano

---

## GitHub API Issues

### Rate Limit Exhausted

**Error:**
```
Failed to fetch instructions from GitHub: Failed to fetch latest release: 403
Using cached instructions
```

**Cause**: GitHub API rate limit (60 req/hour for unauthenticated)

**Status**: **Fixed in v2.1.2** with 15-minute caching

**Verify fix:**
```bash
# Should only check GitHub once per 15 minutes
ls -lt ~/.opencode/cache/codex-instructions-meta.json

# Check lastChecked timestamp
cat ~/.opencode/cache/codex-instructions-meta.json | jq '.lastChecked'
```

**Manual workaround** (if on old version):
- Wait 1 hour for rate limit to reset
- Or use cached instructions (automatic fallback)

---

## Debug Techniques

### Enable Full Logging

```bash
# Both debug and request logging
DEBUG_CODEX_PLUGIN=1 ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode run "test"
```

**What you get:**
- Console: Debug messages showing config resolution
- Files: Complete request/response logs

**Log locations:**
- `~/.opencode/logs/codex-plugin/request-*-before-transform.json`
- `~/.opencode/logs/codex-plugin/request-*-after-transform.json`
- `~/.opencode/logs/codex-plugin/request-*-response.json`

### Inspect Actual API Requests

```bash
# Run command with logging
ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode run "test" --model=openai/gpt-5-codex-low

# Check what was sent to API
cat ~/.opencode/logs/codex-plugin/request-*-after-transform.json | jq '{
  model: .body.model,
  reasoning: .body.reasoning,
  text: .body.text,
  store: .body.store,
  include: .body.include
}'
```

**Verify:**
- `model`: Normalized correctly?
- `reasoning.effort`: Matches your config?
- `text.verbosity`: Matches your config?
- `store`: Should be `false`
- `include`: Should have `reasoning.encrypted_content`

### Compare with Expected

See [development/TESTING.md](../bmad_repo/testing.md) for expected values matrix.

---

## Performance Issues

### Slow Responses

**Possible causes:**
1. `reasoningEffort: "high"` - Uses more computation
2. `textVerbosity: "high"` - Generates longer outputs
3. Network latency

**Solutions:**
- Use lower reasoning effort for faster responses
- Check network connection
- Try different time of day (server load varies)

### High Token Usage

**Monitor usage:**
```bash
# Tokens shown in logs
cat ~/.opencode/logs/codex-plugin/request-*-stream-full.json | grep -o '"total_tokens":[0-9]*'
```

**Reduce tokens:**
1. Lower `textVerbosity`
2. Lower `reasoningEffort`
3. Shorter system prompts (disable CODEX_MODE if needed)

---

## Getting Help

### Before Opening an Issue

1. **Enable logging:**
   ```bash
   DEBUG_CODEX_PLUGIN=1 ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode run "your command"
   ```

2. **Collect info:**
   - OpenCode version: `opencode --version`
   - Plugin version: Check `package.json` or npm
   - Error logs from `~/.opencode/logs/codex-plugin/`
   - Config file (redact sensitive info)

3. **Check existing issues:**
   - [GitHub Issues](https://github.com/numman-ali/opencode-openai-codex-auth/issues)

### Reporting Bugs

Include:
- ✅ Error message
- ✅ Steps to reproduce
- ✅ Config file (redacted)
- ✅ Log files
- ✅ OpenCode version
- ✅ Plugin version

### Account or Subscription Issues

If you're experiencing authentication problems:

- **Ensure active subscription:** Verify your ChatGPT Plus/Pro subscription is active at [ChatGPT Settings](https://chatgpt.com/settings)
- **Check subscription type:** This plugin requires Plus or Pro (Free tier is not supported)
- **Review usage limits:** Check if you've exceeded your subscription's usage limits
- **Revoke and re-authorize:**
  1. Revoke access: [ChatGPT Settings → Authorized Apps](https://chatgpt.com/settings/apps)
  2. Remove local tokens: `opencode auth logout`
  3. Re-authenticate: `opencode auth login`

**Note:** If OpenAI has flagged your account for unusual usage patterns, you may experience authentication issues. Contact OpenAI support if you believe your account has been incorrectly restricted.

### Compliance-Related Issues

If you receive errors related to terms of service violations:

- **Review your usage:** Ensure you're using the plugin for personal development only
- **Check rate limits:** Verify you haven't exceeded usage limits
- **Avoid automation:** Do not use for high-volume automated requests
- **Commercial use:** Switch to OpenAI Platform API for commercial applications

This plugin cannot help with TOS violations or account restrictions. Contact OpenAI support for account-specific issues.

---

**Next**: [Configuration Guide](configuration.md) | [Developer Docs](ARCHITECTURE.md) | [Back to Home](index.md)
```

## File: `docs/development/ARCHITECTURE.md`
```markdown
# Plugin Architecture & Technical Decisions

This document explains the technical design decisions, architecture, and implementation details of the OpenAI Codex OAuth plugin for OpenCode.

## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Stateless vs Stateful Mode](#stateless-vs-stateful-mode)
- [Message ID Handling](#message-id-handling)
- [Reasoning Content Flow](#reasoning-content-flow)
- [Request Pipeline](#request-pipeline)
- [Comparison with Codex CLI](#comparison-with-codex-cli)
- [Design Rationale](#design-rationale)

---

## Architecture Overview

```
┌─────────────┐
│  OpenCode   │  TUI/Desktop client
└──────┬──────┘
       │
       │ streamText() with AI SDK
       │
       ▼
┌──────────────────────────────┐
│  OpenCode Provider System    │
│  - Loads plugin               │
│  - Calls plugin.auth.loader() │
│  - Passes provider config     │
└──────┬───────────────────────┘
       │
       │ Custom fetch()
       │
       ▼
┌──────────────────────────────┐
│  This Plugin                 │
│  - OAuth authentication      │
│  - Request transformation    │
│  - store:false handling      │
│  - Codex bridge prompts      │
└──────┬───────────────────────┘
       │
       │ HTTP POST with OAuth
       │
       ▼
┌──────────────────────────────┐
│  OpenAI Codex API            │
│  (ChatGPT Backend)           │
│  - Requires OAuth            │
│  - Supports store:false      │
│  - Returns SSE stream        │
└──────────────────────────────┘
```

---

## Stateless vs Stateful Mode

### Why store:false?

The plugin uses **`store: false`** (stateless mode) because:

1. **ChatGPT Backend Requirement** (confirmed via testing):
   ```json
   // Attempt with store:true → 400 Bad Request
   {"detail":"Store must be set to false"}
   ```

2. **Codex CLI Behavior** (`tmp/codex/codex-rs/core/src/client.rs:215-232`):
   ```rust
   // Codex CLI uses store:false for ChatGPT OAuth
   let azure_workaround = self.provider.is_azure_responses_endpoint();
   store: azure_workaround,  // false for ChatGPT, true for Azure
   ```

**Key Points**:
1. ✅ **ChatGPT backend REQUIRES store:false** (not optional)
2. ✅ **Codex CLI uses store:false for ChatGPT**
3. ✅ **Azure requires store:true** (different endpoint, not supported by this plugin)
4. ✅ **Stateless mode = no server-side conversation storage**

### How Context Works with store:false

**Question**: If there's no server storage, how does the LLM remember previous turns?

**Answer**: Full message history is sent in every request:

```typescript
// Turn 3 request contains ALL previous messages:
input: [
  { role: "developer", content: "..." },      // System prompts
  { role: "user", content: "write test.txt" },     // Turn 1 user
  { type: "function_call", name: "write", ... },   // Turn 1 tool call
  { type: "function_call_output", ... },           // Turn 1 tool result
  { role: "assistant", content: "Done!" },         // Turn 1 response
  { role: "user", content: "read it" },            // Turn 2 user
  { type: "function_call", name: "read", ... },    // Turn 2 tool call
  { type: "function_call_output", ... },           // Turn 2 tool result
  { role: "assistant", content: "Contents..." },   // Turn 2 response
  { role: "user", content: "what did you write?" } // Turn 3 user (current)
]
// All IDs stripped, item_reference filtered out
```

**Context is maintained through**:
- ✅ Full message history (LLM sees all previous messages)
- ✅ Full tool call history (LLM sees what it did)
- ✅ `reasoning.encrypted_content` (preserves reasoning between turns)

**Source**: Verified via `ENABLE_PLUGIN_REQUEST_LOGGING=1` logs

### Store Comparison

| Aspect | store:false (This Plugin) | store:true (Azure Only) |
|--------|---------------------------|-------------------------|
| **ChatGPT Support** | ✅ Required | ❌ Rejected by API |
| **Message History** | ✅ Sent in each request (no IDs) | Stored on server |
| **Message IDs** | ❌ Must strip all | ✅ Required |
| **AI SDK Compat** | ❌ Must filter `item_reference` | ✅ Works natively |
| **Context** | Full history + encrypted reasoning | Server-stored conversation |
| **Codex CLI Parity** | ✅ Perfect match | ❌ Different mode |

**Decision**: Use **`store:false`** (only option for ChatGPT backend).

---

## Message ID Handling & AI SDK Compatibility

### The Problem

**OpenCode/AI SDK sends two incompatible constructs**:
```typescript
// Multi-turn request from OpenCode
const body = {
  input: [
    { type: "message", role: "developer", content: [...] },
    { type: "message", role: "user", content: [...], id: "msg_abc" },
    { type: "item_reference", id: "rs_xyz" },  // ← AI SDK construct
    { type: "function_call", id: "fc_123" }
  ]
};
```

**Two issues**:
1. `item_reference` - AI SDK construct for server state lookup (not in Codex API spec)
2. Message IDs - Cause "item not found" with `store: false`

**ChatGPT Backend Requirement** (confirmed via testing):
```json
{"detail":"Store must be set to false"}
```

**Errors that occurred**:
```
❌ "Item with id 'msg_abc' not found. Items are not persisted when `store` is set to false."
❌ "Missing required parameter: 'input[3].id'" (when item_reference has no ID)
```

### The Solution

**Filter AI SDK Constructs + Strip IDs** (`lib/request/request-transformer.ts:114-135`):
```typescript
export function filterInput(input: InputItem[]): InputItem[] {
  return input
    .filter((item) => {
      // Remove AI SDK constructs not supported by Codex API
      if (item.type === "item_reference") {
        return false;  // AI SDK only - references server state
      }
      return true;  // Keep all other items
    })
    .map((item) => {
      // Strip IDs from all items (stateless mode)
      if (item.id) {
        const { id, ...itemWithoutId } = item;
        return itemWithoutId as InputItem;
      }
      return item;
    });
}
```

**Why this approach?**
1. ✅ **Filter `item_reference`** - Not in Codex API, AI SDK-only construct
2. ✅ **Keep all messages** - LLM needs full conversation history for context
3. ✅ **Strip ALL IDs** - Matches Codex CLI stateless behavior
4. ✅ **Future-proof** - No ID pattern matching, handles any ID format

### Debug Logging

The plugin logs ID filtering for debugging:

```typescript
// Before filtering
console.log(`[openai-codex-plugin] Filtering ${originalIds.length} message IDs from input:`, originalIds);

// After filtering
console.log(`[openai-codex-plugin] Successfully removed all ${originalIds.length} message IDs`);

// Or warning if IDs remain
console.warn(`[openai-codex-plugin] WARNING: ${remainingIds.length} IDs still present after filtering:`, remainingIds);
```

**Source**: `lib/request/request-transformer.ts:287-301`

---

## Reasoning Content Flow

### Context Preservation Without Storage

**Challenge**: How to maintain context across turns when `store:false` means no server-side storage?

**Solution**: Use `reasoning.encrypted_content`

```typescript
body.include = modelConfig.include || ["reasoning.encrypted_content"];
```

**How it works**:
1. **Turn 1**: Model generates reasoning, encrypted content returned
2. **Client**: Stores encrypted content locally
3. **Turn 2**: Client sends encrypted content back in request
4. **Server**: Decrypts content to restore reasoning context
5. **Model**: Has full context without server-side storage

**Flow Diagram**:
```
Turn 1:
Client → [Request without IDs] → Server
         Server → [Response + encrypted reasoning] → Client
         Client stores encrypted content locally

Turn 2:
Client → [Request with encrypted content, no IDs] → Server
         Server decrypts reasoning context
         Server → [Response + new encrypted reasoning] → Client
```

**Codex CLI equivalent** (`tmp/codex/codex-rs/core/src/client.rs:190-194`):
```rust
let include: Vec<String> = if reasoning.is_some() {
    vec!["reasoning.encrypted_content".to_string()]
} else {
    vec![]
};
```

**Source**: `lib/request/request-transformer.ts:303`

---

## Request Pipeline

### Transformation Steps

```
1. Original OpenCode Request
   ├─ model: "gpt-5-codex"
   ├─ input: [{ id: "msg_123", ... }, { id: "rs_456", ... }]
   └─ tools: [...]

2. Model Normalization
   ├─ Detect codex/gpt-5/codex-mini variants
   └─ Normalize to "gpt-5", "gpt-5-codex", or "codex-mini-latest"

3. Config Merging
   ├─ Global options (provider.openai.options)
   ├─ Model-specific options (provider.openai.models[name].options)
   └─ Result: merged config for this model

4. Message ID Filtering
   ├─ Remove ALL IDs from input array
   ├─ Log original IDs for debugging
   └─ Verify no IDs remain

5. System Prompt Handling (CODEX_MODE)
   ├─ Filter out OpenCode system prompts
   ├─ Preserve OpenCode env + AGENTS instructions when concatenated
   └─ Add Codex-OpenCode bridge prompt

6. Orphan Tool Output Handling
   ├─ Match function_call_output to function_call OR local_shell_call
   ├─ Match custom_tool_call_output to custom_tool_call
   └─ Convert unmatched outputs to assistant messages (preserve context)

7. Reasoning Configuration
   ├─ Set reasoningEffort (minimal/low/medium/high)
   ├─ Set reasoningSummary (auto/detailed)
   └─ Based on model variant

8. Prompt Caching & Session Headers
   ├─ Preserve host-supplied prompt_cache_key (OpenCode session id)
   ├─ Add conversation + account headers for Codex debugging when cache key exists
   └─ Leave headers unset if host does not provide a cache key

9. Final Body
   ├─ store: false
   ├─ stream: true
   ├─ instructions: Codex system prompt
   ├─ input: Filtered messages (no IDs)
   ├─ reasoning: { effort, summary }
   ├─ text: { verbosity }
   ├─ include: ["reasoning.encrypted_content"]
   └─ prompt_cache_key: conversation-scoped UUID
```

**Source**: `lib/request/request-transformer.ts:265-329`

---

## Comparison with Codex CLI

### What We Match

| Feature | Codex CLI | This Plugin | Match? |
|---------|-----------|-------------|--------|
| **OAuth Flow** | ✅ PKCE + ChatGPT login | ✅ Same | ✅ |
| **store Parameter** | `false` (ChatGPT) | `false` | ✅ |
| **Message IDs** | Stripped in stateless | Stripped | ✅ |
| **reasoning.encrypted_content** | ✅ Included | ✅ Included | ✅ |
| **Model Normalization** | "gpt-5" / "gpt-5-codex" / "codex-mini-latest" | Same | ✅ |
| **Reasoning Effort** | medium (default) | medium (default) | ✅ |
| **Text Verbosity** | medium (codex), low (gpt-5) | Same | ✅ |

### What We Add

| Feature | Codex CLI | This Plugin | Why? |
|---------|-----------|-------------|------|
| **Codex-OpenCode Bridge** | N/A (native) | ✅ Custom prompt | OpenCode → Codex translation |
| **OpenCode Prompt Filtering** | N/A | ✅ Filter & replace | Remove OpenCode prompts, keep env/AGENTS |
| **Orphan Tool Output Handling** | ✅ Drop orphans | ✅ Convert to messages | Preserve context + avoid 400s |
| **Usage-limit messaging** | CLI prints status | ✅ Friendly error summary | Surface 5h/weekly windows in OpenCode |
| **Per-Model Options** | CLI flags | ✅ Config file | Better UX in OpenCode |
| **Custom Model Names** | No | ✅ Display names | UI convenience |

---

## Design Rationale

### Why Not store:true?

**Pros of store:true**:
- ✅ No ID filtering needed
- ✅ Server manages conversation
- ✅ Potentially more robust

**Cons of store:true**:
- ❌ Diverges from Codex CLI behavior
- ❌ Requires conversation ID management
- ❌ More complex error handling
- ❌ Unknown server-side storage limits

**Decision**: Use `store:false` for Codex parity and simplicity.

### Why Complete ID Removal?

**Alternative**: Filter specific ID patterns (`rs_*`, `msg_*`, etc.)

**Problem**:
- ID patterns may change
- New ID types could be added
- Partial filtering is brittle

**Solution**: Remove **ALL** IDs

**Rationale**:
- Matches Codex CLI behavior exactly
- Future-proof against ID format changes
- Simpler implementation (no pattern matching)
- Clearer semantics (stateless = no IDs)

### Why Codex-OpenCode Bridge?

**Problem**: OpenCode's system prompts are optimized for OpenCode's tool set and behavior patterns.

**Solution**: Replace OpenCode prompts with Codex-specific instructions.

**Benefits**:
- ✅ Explains tool name differences (apply_patch → edit)
- ✅ Documents available tools
- ✅ Maintains OpenCode working style
- ✅ Preserves Codex best practices
- ✅ 90% reduction in prompt tokens

**Source**: `lib/prompts/codex-opencode-bridge.ts`

### Why Per-Model Config Options?

**Alternative**: Single global config

**Problem**:
- `gpt-5-codex` optimal settings differ from `gpt-5-nano`
- Users want quick switching between quality levels
- No way to save "presets"

**Solution**: Per-model options in config

**Benefits**:
- ✅ Save multiple configurations
- ✅ Quick switching (no CLI args)
- ✅ Descriptive names ("Fast", "Balanced", "Max Quality")
- ✅ Persistent across sessions

**Source**: `config/opencode-legacy.json` (legacy) or `config/opencode-modern.json` (variants)

---

## Error Handling

### Common Errors

#### 1. "Item with id 'X' not found"
**Cause**: Message ID leaked through filtering
**Fix**: Improved `filterInput()` removes ALL IDs
**Prevention**: Debug logging catches remaining IDs

#### 2. Token Expiration
**Cause**: OAuth access token expired
**Fix**: `shouldRefreshToken()` checks expiration
**Prevention**: Auto-refresh before requests

#### 3. "store: false" Validation Error (Azure)
**Cause**: Azure doesn't support stateless mode
**Workaround**: Codex CLI uses `store: true` for Azure only
**This Plugin**: Only supports ChatGPT OAuth (no Azure)

---

## Performance Considerations

### Token Usage

**Codex Bridge Prompt**: ~550 tokens (~90% reduction vs full OpenCode prompt)
**Benefit**: Faster inference, lower costs

### Request Optimization

**Prompt Caching**: Uses `promptCacheKey` for session-based caching
**Result**: Reduced token usage on subsequent turns

**Source**: `tmp/opencode/packages/opencode/src/provider/transform.ts:90-92`

---

## Future Improvements

### Potential Enhancements

1. **Azure Support**: Add `store: true` mode with ID management
2. **Version Detection**: Adapt to OpenCode/AI SDK version changes
3. **Config Validation**: Warn about unsupported options
4. **Test Coverage**: Unit tests for all transformation functions
5. **Performance Metrics**: Log token usage and latency

### Breaking Changes to Watch

1. **AI SDK Updates**: Changes to `.responses()` method
2. **OpenCode Changes**: New message ID formats
3. **Codex API Changes**: New request parameters

---

## See Also
- [CONFIG_FLOW.md](./CONFIG_FLOW.md) - Configuration system guide
- [Codex CLI Source](https://github.com/openai/codex) - Official implementation
- [OpenCode Source](https://github.com/sst/opencode) - OpenCode implementation
```

## File: `docs/development/CONFIG_FIELDS.md`
```markdown
# Config Fields: Complete Guide

Understanding the difference between config key, `id`, and `name` fields in OpenCode model configuration.

## The Three Fields

```json
{
  "provider": {
    "openai": {
      "models": {
        "THIS-IS-THE-CONFIG-KEY": {
          "id": "this-is-the-id-field",
          "name": "This is the name field"
        }
      }
    }
  }
}
```

---

## What Each Field Controls

### Config Key (Property Name)

**Example:** `"gpt-5-codex-low"`

**Used For:**
- ✅ CLI `--model` flag: `--model=openai/gpt-5-codex-low`
- ✅ OpenCode internal lookups: `provider.info.models["gpt-5-codex-low"]`
- ✅ TUI persistence: Saved to `~/.opencode/tui` as `model_id = "gpt-5-codex-low"`
- ✅ Custom command frontmatter: `model: openai/gpt-5-codex-low`
- ✅ Agent configuration: `"model": "openai/gpt-5-codex-low"`
- ✅ **Plugin config lookup**: `userConfig.models["gpt-5-codex-low"]`
- ✅ Passed to custom loaders: `getModel(sdk, "gpt-5-codex-low")`

**This is the PRIMARY identifier throughout OpenCode!**

---

### `id` Field (Optional - NOT NEEDED for OpenAI)

**Example:** `"gpt-5-codex"`

**What it's used for:**
- ⚠️ **Other providers**: Some providers use this for `sdk.languageModel(id)`
- ⚠️ **Sorting**: Used for model priority sorting in OpenCode
- ⚠️ **Documentation**: Indicates the "canonical" model ID

**What it's NOT used for with OpenAI:**
- ❌ **NOT sent to AI SDK** (config key is sent instead)
- ❌ **NOT used by plugin** (plugin receives config key)
- ❌ **NOT required** (OpenCode defaults it to config key)

**Code Reference:** (`tmp/opencode/packages/opencode/src/provider/provider.ts:252`)
```typescript
const parsedModel: ModelsDev.Model = {
  id: model.id ?? modelID,  // ← Defaults to config key if omitted
  ...
}
```

**OpenAI Custom Loader:** (`tmp/opencode/packages/opencode/src/provider/provider.ts:58-65`)
```typescript
openai: async () => {
  return {
    async getModel(sdk: any, modelID: string) {
      return sdk.responses(modelID)  // ← Receives CONFIG KEY, not id field!
    }
  }
}
```

**Our plugin receives:** `body.model = "gpt-5-codex-low"` (config key, NOT id field)

**Recommendation:** **Omit the `id` field** for OpenAI provider - it's redundant and creates confusion. OpenCode will auto-set it to the config key.

---

### `name` Field (Optional)

**Example:** `"GPT 5 Codex Low (OAuth)"`

**Used For:**
- ✅ **TUI Model Picker**: Display name shown in the model selection UI
- ℹ️ **Documentation**: Human-friendly description

**Code Reference:** (`tmp/opencode/packages/opencode/src/provider/provider.ts:253`)
```typescript
const parsedModel: ModelsDev.Model = {
  name: model.name ?? existing?.name ?? modelID,  // Defaults to config key
  ...
}
```

**If omitted:** Falls back to config key for display

---

## Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    What Users See & Use                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CLI Usage:                                                     │
│  $ opencode run --model=openai/gpt-5-codex-low                 │
│                                 └──────┬──────┘                 │
│                                   CONFIG KEY                    │
│                                                                 │
│  TUI Display:                                                   │
│  ┌──────────────────────────────────┐                          │
│  │ Select Model:                    │                          │
│  │                                  │                          │
│  │ ○ GPT 5 Codex Low (OAuth) ←──────┼── name field            │
│  │ ○ GPT 5 Codex Medium (OAuth)     │                          │
│  │ ○ GPT 5 Codex High (OAuth)       │                          │
│  └──────────────────────────────────┘                          │
│                                                                 │
│  Config Lookup (Plugin):                                       │
│  userConfig.models["gpt-5-codex-low"].options                  │
│                     └──────┬──────┘                             │
│                       CONFIG KEY                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                    Internal Flow                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. User Selection                                              │
│     opencode run --model=openai/gpt-5-codex-low                │
│     OpenCode parses: providerID="openai"                        │
│                      modelID="gpt-5-codex-low" ← CONFIG KEY    │
│                                                                 │
│  2. OpenCode Provider Lookup                                    │
│     provider.info.models["gpt-5-codex-low"]                     │
│                          └──────┬──────┘                        │
│                            CONFIG KEY                           │
│                                                                 │
│  3. Custom Loader Call (OpenAI)                                 │
│     getModel(sdk, "gpt-5-codex-low")                            │
│                   └──────┬──────┘                               │
│                     CONFIG KEY                                  │
│                                                                 │
│  4. AI SDK Request Creation                                     │
│     { model: "gpt-5-codex-low", ... }                           │
│              └──────┬──────┘                                    │
│                CONFIG KEY                                       │
│                                                                 │
│  5. Custom fetch() (Our Plugin)                                 │
│     body.model = "gpt-5-codex-low"                              │
│                  └──────┬──────┘                                │
│                    CONFIG KEY                                   │
│                                                                 │
│  6. Plugin Config Lookup                                        │
│     userConfig.models["gpt-5-codex-low"].options                │
│                       └──────┬──────┘                           │
│                         CONFIG KEY                              │
│     Result: { reasoningEffort: "low", ... } ✅ FOUND           │
│                                                                 │
│  7. Plugin Normalization                                        │
│     normalizeModel("gpt-5-codex-low")                           │
│     Returns: "gpt-5-codex" ← SENT TO CODEX API                 │
│                                                                 │
│  8. TUI Persistence                                             │
│     ~/.opencode/tui:                                            │
│       provider_id = "openai"                                    │
│       model_id = "gpt-5-codex-low" ← CONFIG KEY persisted      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Field Purpose Summary

### Config Key: The Real Identifier

```json
"gpt-5-codex-low": { ... }
 └──────┬──────┘
   CONFIG KEY
```

**Purpose:**
- 🎯 **PRIMARY identifier** - used everywhere in OpenCode
- 🎯 **Plugin receives this** - what our plugin sees in `body.model`
- 🎯 **Config lookup key** - how plugin finds per-model options
- 🎯 **Persisted value** - saved in TUI state

**Best Practice:** Use Codex CLI preset names (`gpt-5-codex-low`, `gpt-5-high`, etc.)

---

### `id` Field: Documentation/Metadata

```json
"id": "gpt-5-codex"
       └─────┬─────┘
         ID FIELD
```

**Purpose:**
- 📝 **Documents** what base model this variant uses
- 📝 **Helps sorting** in model lists
- 📝 **Clarity** - shows relationship between variants

**Best Practice:** Set to the base API model name (`gpt-5-codex`, `gpt-5`, etc.)

**Note:** For OpenAI provider, this is NOT sent to the API! The plugin normalizes the config key instead.

---

### `name` Field: UI Display

```json
"name": "GPT 5 Codex Low (OAuth)"
         └──────────┬──────────┘
              NAME FIELD
```

**Purpose:**
- 🎨 **TUI display** - what users see in model picker
- 🎨 **User-friendly** - can be descriptive
- 🎨 **Differentiation** - helps distinguish from API key models

**Best Practice:** Human-friendly name with context (OAuth, API, subscription type, etc.)

---

## Real-World Examples

### Example 1: Our Current Config ✅

```json
{
  "gpt-5-codex-low": {
    "id": "gpt-5-codex",
    "name": "GPT 5 Codex Low (OAuth)",
    "options": { "reasoningEffort": "low" }
  }
}
```

**When user selects `openai/gpt-5-codex-low`:**
- CLI: Uses `"gpt-5-codex-low"` (config key)
- TUI: Shows `"GPT 5 Codex Low (OAuth)"` (name field)
- Plugin receives: `body.model = "gpt-5-codex-low"` (config key)
- Plugin looks up: `models["gpt-5-codex-low"]` ✅ Found
- Plugin sends to API: `"gpt-5-codex"` (normalized)

**Result:** ✅ Everything works perfectly!

---

### Example 2: Multiple Variants of Same Model ✅

```json
{
  "gpt-5-codex-low": {
    "id": "gpt-5-codex",
    "name": "GPT 5 Codex Low (OAuth)"
  },
  "gpt-5-codex-high": {
    "id": "gpt-5-codex",
    "name": "GPT 5 Codex High (OAuth)"
  }
}
```

**Why this works:**
- Config keys are different: `"gpt-5-codex-low"` vs `"gpt-5-codex-high"` ✅
- Same `id` is fine - it's just metadata
- Different `name` values help distinguish in TUI

**Result:** ✅ Two variants of same base model, different settings

---

### Example 3: If We Made Config Key = ID ❌

```json
{
  "gpt-5-codex": {
    "id": "gpt-5-codex",
    "name": "GPT 5 Codex Low (OAuth)",
    "options": { "reasoningEffort": "low" }
  },
  "gpt-5-codex": {  // ❌ DUPLICATE KEY ERROR!
    "id": "gpt-5-codex",
    "name": "GPT 5 Codex High (OAuth)",
    "options": { "reasoningEffort": "high" }
  }
}
```

**Problem:** JavaScript objects can't have duplicate keys!

**Result:** ❌ Can't have multiple variants

---

## Why We Need Different Config Keys

**Problem:** Need multiple configurations for the same API model

**Solution:** Different config keys → same `id`

```json
{
  "gpt-5-codex-low": {          // ← Unique config key #1
    "id": "gpt-5-codex",         // ← Same base model
    "options": { "reasoningEffort": "low" }
  },
  "gpt-5-codex-medium": {       // ← Unique config key #2
    "id": "gpt-5-codex",         // ← Same base model
    "options": { "reasoningEffort": "medium" }
  },
  "gpt-5-codex-high": {         // ← Unique config key #3
    "id": "gpt-5-codex",         // ← Same base model
    "options": { "reasoningEffort": "high" }
  }
}
```

**Result:**
- 3 selectable variants in TUI ✅
- Same API model (`gpt-5-codex`) ✅
- Different reasoning settings ✅
- Plugin correctly applies per-variant options ✅

---

## Backwards Compatibility

### Config Changes are Safe ✅

**Old Plugin + Old Config:**
```json
"GPT 5 Codex Low (ChatGPT Subscription)": {
  "id": "gpt-5-codex",
  "options": { "reasoningEffort": "low" }
}
```
**Result:** ❌ Per-model options broken (existing bug in old plugin)

**New Plugin + Old Config:**
```json
"GPT 5 Codex Low (ChatGPT Subscription)": {
  "id": "gpt-5-codex",
  "options": { "reasoningEffort": "low" }
}
```
**Result:** ✅ Per-model options work! (bug fixed)

**New Plugin + New Config:**
```json
"gpt-5-codex-low": {
  "id": "gpt-5-codex",
  "name": "GPT 5 Codex Low (OAuth)",
  "options": { "reasoningEffort": "low" }
}
```
**Result:** ✅ Per-model options work! (bug fixed + cleaner naming)

**Conclusion:**
- ✅ Existing configs continue to work
- ✅ New configs work better
- ✅ Users can migrate at their own pace

---

## Required Configuration Fields

### `store` Field: Critical for AI SDK 2.0.50+

**⚠️ Required as of AI SDK 2.0.50 (released Oct 12, 2025)**

```json
{
  "provider": {
    "openai": {
      "options": {
        "store": false
      }
    }
  }
}
```

**What it does:**
- `false` (required): Prevents AI SDK from using `item_reference` for conversation history
- `true` (default): Uses server-side storage with references (incompatible with Codex API)

**Why required:**
AI SDK 2.0.50 introduced automatic use of `item_reference` items to reduce payload size when `store: true`. However:
- Codex API requires `store: false` (stateless mode)
- `item_reference` items cannot be resolved without server-side storage
- Without this setting, multi-turn conversations fail with: `"Item with id 'fc_xxx' not found"`

**Where to set:**
```json
{
  "provider": {
    "openai": {
      "options": {
        "store": false  // ← Global: applies to all models
      },
      "models": {
        "gpt-5-codex-low": {
          "options": {
            "store": false  // ← Per-model: redundant but explicit
          }
        }
      }
    }
  }
}
```

**Recommendation:** Set in global `options` since it's required for all models using this plugin.

**Note:** The plugin also includes a `chat.params` hook that automatically injects `store: false`, but explicit configuration is recommended for clarity and forward compatibility.

---

## Recommended Structure

### Recommended: Config Key + Name ✅

```json
{
  "gpt-5-codex-low": {
    "name": "GPT 5 Codex Low (OAuth)",
    "options": { "reasoningEffort": "low" }
  }
}
```

**Benefits:**
- ✅ Clean config key: `gpt-5-codex-low` (matches Codex CLI presets)
- ✅ Friendly display: `"GPT 5 Codex Low (OAuth)"` (UX)
- ✅ No redundant fields
- ✅ OpenCode auto-sets `id` to config key

**Why no `id` field?**
- For OpenAI provider, the `id` field is NOT used (custom loader receives config key)
- OpenCode defaults `id` to config key if omitted
- Including it is redundant and creates confusion

---

### Minimal Structure (Works but less friendly)

```json
{
  "gpt-5-codex-low": {
    "options": { "reasoningEffort": "low" }
  }
}
```

**What happens:**
- `id` defaults to: `"gpt-5-codex-low"` (config key)
- `name` defaults to: `"gpt-5-codex-low"` (config key)
- TUI shows: `"gpt-5-codex-low"` (less friendly)
- Plugin normalizes: `"gpt-5-codex-low"` → `"gpt-5-codex"` for API
- **Works perfectly, just less user-friendly**

---

### With id Field (Redundant but Harmless)

```json
{
  "gpt-5-codex-low": {
    "id": "gpt-5-codex",
    "name": "GPT 5 Codex Low (OAuth)",
    "options": { "reasoningEffort": "low" }
  }
}
```

**What happens:**
- `id` field is stored but NOT used by OpenAI custom loader
- Adds documentation value but is technically redundant
- Works fine, just verbose

---

## Summary Table

| Use Case | Which Field? | Example Value |
|----------|-------------|---------------|
| **CLI `--model` flag** | Config Key | `openai/gpt-5-codex-low` |
| **Custom commands** | Config Key | `model: openai/gpt-5-codex-low` |
| **Agent config** | Config Key | `"model": "openai/gpt-5-codex-low"` |
| **TUI display** | `name` field | `"GPT 5 Codex Low (OAuth)"` |
| **Plugin config lookup** | Config Key | `models["gpt-5-codex-low"]` |
| **AI SDK receives** | Config Key | `body.model = "gpt-5-codex-low"` |
| **Plugin normalizes** | Transformed | `"gpt-5-codex"` (sent to API) |
| **TUI persistence** | Config Key | `model_id = "gpt-5-codex-low"` |
| **Documentation** | `id` field | `"gpt-5-codex"` (base model) |
| **Model sorting** | `id` field | Used for priority ranking |

---

## Key Insight for OpenAI Provider

```
CONFIG KEY is the real identifier! 👑
  ├─ Used for selection (CLI, TUI, commands)
  ├─ Used for persistence (saved to ~/.opencode/tui)
  ├─ Passed to custom loader (getModel receives this)
  ├─ Sent to AI SDK (body.model = this)
  └─ Received by plugin (our plugin sees this)

id field is metadata 📝
  ├─ Documents base model
  ├─ Used for sorting
  └─ NOT sent to AI SDK (custom loader uses config key)

name field is UI sugar 🎨
  └─ Makes TUI model picker user-friendly
```

---

## Why The Bug Happened

**Old Plugin Logic (Broken):**
```typescript
const normalizedModel = normalizeModel(body.model);  // "gpt-5-codex-low" → "gpt-5-codex"
const modelConfig = getModelConfig(normalizedModel, userConfig);  // Lookup "gpt-5-codex"
```

**Problem:**
- Plugin received: `"gpt-5-codex-low"` (config key)
- Plugin normalized first: `"gpt-5-codex"`
- Plugin looked up config: `models["gpt-5-codex"]` ❌ NOT FOUND
- Config key was: `models["gpt-5-codex-low"]`
- **Result:** Per-model options ignored!

**New Plugin Logic (Fixed):**
```typescript
const originalModel = body.model;  // "gpt-5-codex-low" (config key)
const normalizedModel = normalizeModel(body.model);  // "gpt-5-codex" (for API)
const modelConfig = getModelConfig(originalModel, userConfig);  // Lookup "gpt-5-codex-low" ✅
```

**Fix:**
- Use original value (config key) for config lookup ✅
- Normalize separately for API call ✅
- **Result:** Per-model options applied correctly!

---

## Testing the Understanding

### Test Case 1: Which model does plugin send to API?

**Config:**
```json
{
  "my-custom-name": {
    "id": "gpt-5-codex",
    "name": "My Custom Display Name",
    "options": { "reasoningEffort": "high" }
  }
}
```

**User runs:** `--model=openai/my-custom-name`

**Question:** What model does plugin send to Codex API?

**Answer:**
1. Plugin receives: `body.model = "my-custom-name"`
2. Plugin normalizes: `"my-custom-name"` → `"gpt-5-codex"` (contains "codex")
3. Plugin sends to API: `"gpt-5-codex"` ✅

**The `id` field is NOT used for this!**

---

### Test Case 2: How does TUI know what to display?

**Config:**
```json
{
  "ugly-key-123": {
    "id": "gpt-5",
    "name": "Beautiful Display Name"
  }
}
```

**Question:** What does TUI model picker show?

**Answer:** `"Beautiful Display Name"` (from `name` field)

**If `name` was omitted:** Would show `"ugly-key-123"` (config key)

---

### Test Case 3: How does plugin find config?

**Config:**
```json
{
  "gpt-5-codex-low": {
    "id": "gpt-5-codex",
    "options": { "reasoningEffort": "low" }
  }
}
```

**User selects:** `openai/gpt-5-codex-low`

**Question:** How does plugin find the options?

**Answer:**
1. Plugin receives: `body.model = "gpt-5-codex-low"`
2. Plugin looks up: `userConfig.models["gpt-5-codex-low"]` ✅
3. Plugin finds: `{ reasoningEffort: "low" }` ✅

**The lookup uses config key, NOT the `id` field!**

---

## Common Mistakes

### ❌ Using id as Config Key

```json
{
  "gpt-5-codex": {  // ❌ Can't have multiple variants
    "id": "gpt-5-codex"
  }
}
```

### ❌ Thinking id Controls Plugin Lookup

```json
{
  "my-model": {
    "id": "gpt-5-codex-low",  // ❌ Plugin won't look up by this!
    "options": { ... }
  }
}
```

**Plugin looks up by:** `"my-model"` (config key), not `"gpt-5-codex-low"` (id)

### ❌ Forgetting name Field

```json
{
  "gpt-5-codex-low": {
    "id": "gpt-5-codex"
    // Missing: "name" field
  }
}
```

**Result:** TUI shows `"gpt-5-codex-low"` (works but less friendly)

---

## See Also

- [CONFIG_FLOW.md](./CONFIG_FLOW.md) - Complete config system guide
- [ARCHITECTURE.md](./ARCHITECTURE.md) - Technical architecture
- [BUGS_FIXED.md](./BUGS_FIXED.md) - Bug fixes and testing
```

## File: `docs/development/CONFIG_FLOW.md`
```markdown
# OpenCode Config Flow: Complete Guide

This document explains how OpenCode configuration flows from user files through the plugin system to the Codex API.

## Table of Contents
- [Config Loading Order](#config-loading-order)
- [Provider Options Flow](#provider-options-flow)
- [Model Selection & Persistence](#model-selection--persistence)
- [Plugin Configuration](#plugin-configuration)
- [Examples](#examples)
- [Best Practices](#best-practices)

---

## Config Loading Order

OpenCode loads and merges configuration from multiple sources in this order (**last wins**):

### 1. Global Config
```
~/.config/opencode/opencode.jsonc
~/.config/opencode/opencode.json
```

### 2. Project Configs (traversed upward from cwd)
```
<project>/.opencode/opencode.jsonc
<project>/.opencode/opencode.json
<parent>/.opencode/opencode.jsonc
<parent>/.opencode/opencode.json
... (up to worktree root)
```

### 3. Custom Config (via flags)
```bash
OPENCODE_CONFIG=/path/to/config.json opencode
# or
OPENCODE_CONFIG_CONTENT='{"model":"openai/gpt-5"}' opencode
```

### 4. Auth Configs
```
# From .well-known/opencode endpoints (for OAuth providers)
https://auth.example.com/.well-known/opencode
```

**Source**: `tmp/opencode/packages/opencode/src/config/config.ts:26-51`

---

## Provider Options Flow

Options are merged at multiple stages before reaching the plugin:

### Stage 1: Database Defaults
Models.dev provides baseline capabilities for each provider/model.

### Stage 2: Environment Variables
```bash
export OPENAI_API_KEY="sk-..."
```

### Stage 3: Custom Loaders
Plugins can inject options via the `loader()` function.

### Stage 4: User Config (HIGHEST PRIORITY)
```json
{
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "textVerbosity": "low"
      }
    }
  }
}
```

**Result**: User config overrides everything else.

**Source**: `tmp/opencode/packages/opencode/src/provider/provider.ts:236-339`

---

## Model Selection & Persistence

### Display Names vs Internal IDs

**Your Config** (`config/opencode-legacy.json`):
```json
{
  "provider": {
    "openai": {
      "models": {
        "gpt-5-codex-medium": {
          "name": "GPT 5 Codex Medium (OAuth)",
          "limit": {
            "context": 272000,
            "output": 128000
          },
          "options": {
            "reasoningEffort": "medium",
            "reasoningSummary": "auto",
            "textVerbosity": "medium",
            "include": [
              "reasoning.encrypted_content"
            ],
            "store": false
          }
        }
      }
    }
  }
}
```

**What OpenCode Uses**:
- **UI Display**: "GPT 5 Codex Medium (OAuth)" ✅
- **Persistence**: `provider_id: "openai"` + `model_id: "gpt-5-codex-medium"` ✅
- **Plugin lookup**: `models["gpt-5-codex-medium"]` → used to build Codex request ✅

### TUI Persistence

The TUI stores recently used models in `~/.opencode/tui`:

```toml
[[recently_used_models]]
provider_id = "openai"
model_id = "gpt-5-codex"
last_used = 2025-10-12T10:30:00Z
```

**Key Point**: Custom display names are **UI-only**. The underlying `id` field is what gets persisted and sent to APIs.

**Source**: `tmp/opencode/packages/tui/internal/app/state.go:54-79`

---

## Plugin Configuration

### How This Plugin Receives Config

**Plugin Entry Point** (`index.ts:64-86`):
```typescript
async loader(getAuth: () => Promise<Auth>, provider: unknown) {
  const providerConfig = provider as {
    options?: Record<string, unknown>;
    models?: UserConfig["models"]
  };

  const userConfig: UserConfig = {
    global: providerConfig?.options || {},  // Global options
    models: providerConfig?.models || {},   // Per-model options
  };

  // ... use userConfig in custom fetch()
}
```

### Config Structure

```typescript
type UserConfig = {
  global: {
    // Applied to ALL models
    reasoningEffort?: "minimal" | "low" | "medium" | "high";
    textVerbosity?: "low" | "medium" | "high";
    include?: string[];
  };
  models: {
    [modelName: string]: {
      options?: {
        // Override global for specific model
        reasoningEffort?: "minimal" | "low" | "medium" | "high";
        textVerbosity?: "low" | "medium" | "high";
      };
    };
  };
};
```

### Option Precedence

For a given model, options are merged:
1. **Global options** (`provider.openai.options`)
2. **Model-specific options** (`provider.openai.models[modelName].options`) ← WINS

**Implementation**: `lib/request/request-transformer.ts:getModelConfig()`

---

## Examples

### Example 1: Global Options Only
```json
{
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "textVerbosity": "medium",
        "include": ["reasoning.encrypted_content"]
      }
    }
  }
}
```

**Result**: All OpenAI models use these options.

### Example 2: Per-Model Override
```json
{
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "textVerbosity": "medium"
      },
      "models": {
        "gpt-5-codex-high": {
          "name": "GPT 5 Codex High (OAuth)",
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed"
          }
        },
        "gpt-5-nano": {
          "name": "GPT 5 Nano (OAuth)",
          "options": {
            "reasoningEffort": "minimal",
            "textVerbosity": "low"
          }
        }
      }
    }
  }
}
```

**Result**:
- `gpt-5-codex-high` uses `reasoningEffort: "high"` (overridden) + `textVerbosity: "medium"` (from global)
- `gpt-5-nano` uses `reasoningEffort: "minimal"` + `textVerbosity: "low"` (both overridden)

### Example 3: Full Configuration
```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-openai-codex-auth"],
  "model": "openai/gpt-5-codex-medium",
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium",
        "reasoningSummary": "auto",
        "textVerbosity": "medium",
        "include": ["reasoning.encrypted_content"]
      },
      "models": {
        "gpt-5-codex-low": {
          "name": "GPT 5 Codex Low (OAuth)",
          "options": {
            "reasoningEffort": "low"
          }
        },
        "gpt-5-codex-high": {
          "name": "GPT 5 Codex High (OAuth)",
          "options": {
            "reasoningEffort": "high",
            "reasoningSummary": "detailed"
          }
        }
      }
    }
  }
}
```

---

## Best Practices

### 1. Use Per-Model Options for Variants
Instead of duplicating global options, override only what's different:

❌ **Bad**:
```json
{
  "models": {
    "gpt-5-low": {
      "id": "gpt-5",
      "options": {
        "reasoningEffort": "low",
        "textVerbosity": "low",
        "include": ["reasoning.encrypted_content"]
      }
    },
    "gpt-5-high": {
      "id": "gpt-5",
      "options": {
        "reasoningEffort": "high",
        "textVerbosity": "high",
        "include": ["reasoning.encrypted_content"]
      }
    }
  }
}
```

✅ **Good**:
```json
{
  "options": {
    "include": ["reasoning.encrypted_content"]
  },
  "models": {
    "gpt-5-low": {
      "id": "gpt-5",
      "options": {
        "reasoningEffort": "low",
        "textVerbosity": "low"
      }
    },
    "gpt-5-high": {
      "id": "gpt-5",
      "options": {
        "reasoningEffort": "high",
        "textVerbosity": "high"
      }
    }
  }
}
```

### 2. Keep Display Names Meaningful
Custom model names help you remember what each variant does:

```json
{
  "models": {
    "GPT 5 Codex - Fast & Cheap": {
      "id": "gpt-5-codex",
      "options": { "reasoningEffort": "low" }
    },
    "GPT 5 Codex - Balanced": {
      "id": "gpt-5-codex",
      "options": { "reasoningEffort": "medium" }
    },
    "GPT 5 Codex - Max Quality": {
      "id": "gpt-5-codex",
      "options": { "reasoningEffort": "high" }
    }
  }
}
```

### 3. Set Defaults at Global Level
Most common settings should be global:

```json
{
  "options": {
    "reasoningEffort": "medium",
    "reasoningSummary": "auto",
    "textVerbosity": "medium",
    "include": ["reasoning.encrypted_content"]
  }
}
```

### 4. Use Config Files, Not Environment Variables
While you can set `CODEX_MODE=0` to disable the bridge prompt, it's better to document such settings in config files:

❌ **Bad**: `CODEX_MODE=0 opencode`

✅ **Good**: Create `~/.opencode/openai-codex-auth-config.json`:
```json
{
  "codexMode": false
}
```

---

## Troubleshooting

### Config Not Being Applied
1. Check config file syntax with `jq . < config.json`
2. Verify config file location (use absolute paths)
3. Check OpenCode logs for config load errors
4. Use `OPENCODE_CONFIG_CONTENT` to test minimal configs

### Model Not Persisting
1. TUI remembers the `id` field, not the display name
2. Check `~/.opencode/tui` for recently used models
3. Verify your config has the correct `id` field

### Options Not Taking Effect
1. Model-specific options override global options
2. Plugin receives merged config from OpenCode
3. Add debug logging to verify what plugin receives

---

## See Also
- [ARCHITECTURE.md](./ARCHITECTURE.md) - Plugin architecture and design decisions
- [OpenCode Config Schema](https://opencode.ai/config.json) - Official schema
- [Models.dev](https://models.dev) - Model capability database
```

## File: `docs/development/TESTING.md`
```markdown
# Complete Test Scenarios

Comprehensive testing matrix for all config scenarios and backwards compatibility.

## Test Scenarios Matrix

### Scenario 1: Default OpenCode Models (No Custom Config)

**Config:**
```json
{
  "plugin": ["opencode-openai-codex-auth"]
}
```

**Available Models:** (from OpenCode's models.dev database)
- `gpt-5`
- `gpt-5-codex`
- `gpt-5-mini`
- `gpt-5-nano`

**Test Cases:**

| User Selects | Plugin Receives | Normalizes To | Config Lookup | API Receives | Result |
|--------------|-----------------|---------------|---------------|--------------|--------|
| `openai/gpt-5` | `"gpt-5"` | `"gpt-5"` | `models["gpt-5"]` → undefined | `"gpt-5"` | ✅ Uses global options |
| `openai/gpt-5-codex` | `"gpt-5-codex"` | `"gpt-5-codex"` | `models["gpt-5-codex"]` → undefined | `"gpt-5-codex"` | ✅ Uses global options |
| `openai/gpt-5-mini` | `"gpt-5-mini"` | `"gpt-5"` | `models["gpt-5-mini"]` → undefined | `"gpt-5"` | ✅ Uses global options |
| `openai/gpt-5-nano` | `"gpt-5-nano"` | `"gpt-5"` | `models["gpt-5-nano"]` → undefined | `"gpt-5"` | ✅ Uses global options |

**Expected Behavior:**
- ✅ All models work with global options
- ✅ Normalized correctly for API
- ✅ No errors

---

### Scenario 2: Custom Config with Preset Names (New Style)

**Config:**
```json
{
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium"
      },
      "models": {
        "gpt-5-codex-low": {
          "name": "GPT 5 Codex Low (OAuth)",
          "options": { "reasoningEffort": "low" }
        },
        "gpt-5-codex-high": {
          "name": "GPT 5 Codex High (OAuth)",
          "options": { "reasoningEffort": "high" }
        }
      }
    }
  }
}
```

**Test Cases:**

| User Selects | Plugin Receives | Config Lookup | Resolved Options | API Receives | Result |
|--------------|-----------------|---------------|------------------|--------------|--------|
| `openai/gpt-5-codex-low` | `"gpt-5-codex-low"` | Found ✅ | `{ reasoningEffort: "low" }` | `"gpt-5-codex"` | ✅ Per-model |
| `openai/gpt-5-codex-high` | `"gpt-5-codex-high"` | Found ✅ | `{ reasoningEffort: "high" }` | `"gpt-5-codex"` | ✅ Per-model |
| `openai/gpt-5-codex` | `"gpt-5-codex"` | Not found | `{ reasoningEffort: "medium" }` | `"gpt-5-codex"` | ✅ Global |

**Expected Behavior:**
- ✅ Custom variants use per-model options
- ✅ Default `gpt-5-codex` uses global options
- ✅ Both normalize to `"gpt-5-codex"` for API

---

### Scenario 3: Old Config (Backwards Compatibility)

**Config:**
```json
{
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "options": {
        "reasoningEffort": "medium"
      },
      "models": {
        "GPT 5 Codex Low (ChatGPT Subscription)": {
          "id": "gpt-5-codex",
          "options": { "reasoningEffort": "low" }
        }
      }
    }
  }
}
```

**Test Cases:**

| User Selects | Plugin Receives | Config Lookup | Resolved Options | API Receives | Result |
|--------------|-----------------|---------------|------------------|--------------|--------|
| `openai/GPT 5 Codex Low (ChatGPT Subscription)` | `"GPT 5 Codex Low (ChatGPT Subscription)"` | Found ✅ | `{ reasoningEffort: "low" }` | `"gpt-5-codex"` | ✅ Per-model |

**Expected Behavior:**
- ✅ Old config keys still work
- ✅ Per-model options applied correctly
- ✅ Normalizes correctly for API

---

### Scenario 4: Mixed Config (Default + Custom)

**Config:**
```json
{
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "models": {
        "gpt-5-codex-low": {
          "name": "GPT 5 Codex Low (OAuth)",
          "options": { "reasoningEffort": "low" }
        }
      }
    }
  }
}
```

**Available Models:**
- `gpt-5-codex-low` (custom)
- `gpt-5-codex` (default from models.dev)
- `gpt-5` (default from models.dev)

**Test Cases:**

| User Selects | Config Lookup | Uses Options | Result |
|--------------|---------------|--------------|--------|
| `openai/gpt-5-codex-low` | Found ✅ | Per-model | ✅ Custom config |
| `openai/gpt-5-codex` | Not found | Global | ✅ Default model |
| `openai/gpt-5` | Not found | Global | ✅ Default model |

**Expected Behavior:**
- ✅ Custom variants use per-model options
- ✅ Default models use global options
- ✅ Both types coexist peacefully

---

### Scenario 5: Edge Cases

#### 5a: Model Name with Uppercase

**Config:**
```json
{
  "models": {
    "GPT-5-CODEX-HIGH": {
      "options": { "reasoningEffort": "high" }
    }
  }
}
```

**Test:**
```
User selects: openai/GPT-5-CODEX-HIGH
Plugin receives: "GPT-5-CODEX-HIGH"
normalizeModel: "GPT-5-CODEX-HIGH" → "gpt-5-codex" ✅ (includes "codex")
Config lookup: models["GPT-5-CODEX-HIGH"] → Found ✅
API receives: "gpt-5-codex" ✅
```

**Result:** ✅ Works (case-insensitive includes())

---

#### 5b: Model Name with Special Characters

**Config:**
```json
{
  "models": {
    "my-gpt5-codex-variant": {
      "options": { "reasoningEffort": "high" }
    }
  }
}
```

**Test:**
```
User selects: openai/my-gpt5-codex-variant
Plugin receives: "my-gpt5-codex-variant"
normalizeModel: "my-gpt5-codex-variant" → "gpt-5-codex" ✅ (includes "codex")
Config lookup: models["my-gpt5-codex-variant"] → Found ✅
API receives: "gpt-5-codex" ✅
```

**Result:** ✅ Works (normalization handles it)

---

#### 5c: No Config, No Model Specified

**Config:**
```json
{
  "plugin": ["opencode-openai-codex-auth"]
}
```

**Test:**
```
User selects: (none - uses OpenCode default)
Plugin receives: undefined or default from OpenCode
normalizeModel: undefined → "gpt-5" ✅ (fallback)
Config lookup: models[undefined] → undefined
API receives: "gpt-5" ✅
```

**Result:** ✅ Works (safe fallback)

---

#### 5d: Only `gpt-5` in Name (No `codex`)

**Config:**
```json
{
  "models": {
    "my-gpt-5-variant": {
      "options": { "reasoningEffort": "high" }
    }
  }
}
```

**Test:**
```
User selects: openai/my-gpt-5-variant
Plugin receives: "my-gpt-5-variant"
normalizeModel: "my-gpt-5-variant" → "gpt-5" ✅ (includes "gpt-5", not "codex")
Config lookup: models["my-gpt-5-variant"] → Found ✅
API receives: "gpt-5" ✅
```

**Result:** ✅ Works (correct model selected)

---

### Scenario 6: Multi-Turn Conversation (store:false Test)

**Config:** Any

**Test Sequence:**
```
Turn 1: > write hello to test.txt
Turn 2: > read the file
Turn 3: > what did you write?
Turn 4: > now delete it
```

**What Plugin Should Do:**

| Turn | Input Has IDs? | Filter Result | Encrypted Content | Result |
|------|---------------|---------------|-------------------|--------|
| 1 | No | No filtering needed | Received in response | ✅ Works |
| 2 | Yes (from Turn 1) | ALL removed ✅ | Sent back in request | ✅ Works |
| 3 | Yes (from Turn 1-2) | ALL removed ✅ | Sent back in request | ✅ Works |
| 4 | Yes (from Turn 1-3) | ALL removed ✅ | Sent back in request | ✅ Works |

**Expected Behavior:**
- ✅ No "item not found" errors on any turn
- ✅ Context preserved via encrypted reasoning
- ✅ Debug log shows: "Successfully removed all X message IDs"

---

## Backwards Compatibility Testing

### Test Matrix

| Plugin Version | Config Format | Expected Result |
|----------------|--------------|-----------------|
| **Old (<2.1.2)** | Long names + id | ❌ Per-model options broken, ID errors |
| **Old (<2.1.2)** | Short names | ❌ Per-model options broken, ID errors |
| **New (2.1.2+)** | Long names + id | ✅ **ALL FIXED** |
| **New (2.1.2+)** | Short names | ✅ **ALL FIXED** |
| **New (2.1.2+)** | Short names (no id) | ✅ **OPTIMAL** |

### Backwards Compatibility Tests

#### Test 1: Old Plugin User Upgrades

**Before (Plugin v2.1.1):**
```json
{
  "models": {
    "GPT 5 Codex Low (ChatGPT Subscription)": {
      "id": "gpt-5-codex",
      "options": { "reasoningEffort": "low" }
    }
  }
}
```

**After (Plugin v2.1.2):**
- Keep same config
- Plugin now finds per-model options ✅
- No "item not found" errors ✅

**Result:** ✅ **Works without config changes**

---

#### Test 2: New User with Recommended Config

**Config:**
```json
{
  "models": {
    "gpt-5-codex-low": {
      "name": "GPT 5 Codex Low (OAuth)",
      "options": { "reasoningEffort": "low" }
    }
  }
}
```

**Expected:**
- CLI: `--model=openai/gpt-5-codex-low` ✅
- TUI: Shows "GPT 5 Codex Low (OAuth)" ✅
- Plugin: Finds and applies per-model options ✅
- API: Receives `"gpt-5-codex"` ✅

**Result:** ✅ **Optimal experience**

---

#### Test 3: Minimal Config (No Custom Models)

**Config:**
```json
{
  "plugin": ["opencode-openai-codex-auth"],
  "model": "openai/gpt-5-codex"
}
```

**Expected:**
- Uses default OpenCode model: `gpt-5-codex`
- Plugin applies: Global options + Codex defaults
- No errors ✅

**Result:** ✅ **Works out of the box**

---

## Debug Logging Test Cases

### Enable Debug Mode

```bash
DEBUG_CODEX_PLUGIN=1 opencode run "test" --model=openai/gpt-5-codex-low
```

### Expected Debug Output

#### Case 1: Custom Model with Config

```
[openai-codex-plugin] Debug logging ENABLED
[openai-codex-plugin] Model config lookup: "gpt-5-codex-low" → normalized to "gpt-5-codex" for API {
  hasModelSpecificConfig: true,
  resolvedConfig: {
    reasoningEffort: 'low',
    textVerbosity: 'medium',
    reasoningSummary: 'auto',
    include: ['reasoning.encrypted_content']
  }
}
[openai-codex-plugin] Filtering 0 message IDs from input: []
```

✅ **Verify:** `hasModelSpecificConfig: true` confirms per-model options found

---

#### Case 2: Default Model (No Custom Config)

```bash
DEBUG_CODEX_PLUGIN=1 opencode run "test" --model=openai/gpt-5-codex
```

```
[openai-codex-plugin] Debug logging ENABLED
[openai-codex-plugin] Model config lookup: "gpt-5-codex" → normalized to "gpt-5-codex" for API {
  hasModelSpecificConfig: false,
  resolvedConfig: {
    reasoningEffort: 'medium',
    textVerbosity: 'medium',
    reasoningSummary: 'auto',
    include: ['reasoning.encrypted_content']
  }
}
[openai-codex-plugin] Filtering 0 message IDs from input: []
```

✅ **Verify:** `hasModelSpecificConfig: false` confirms using global options

---

#### Case 3: Multi-Turn with ID Filtering

```
[openai-codex-plugin] Filtering 3 message IDs from input: ['msg_abc123', 'rs_xyz789', 'msg_def456']
[openai-codex-plugin] Successfully removed all 3 message IDs
```

✅ **Verify:** All IDs removed, no warnings

---

#### Case 4: Warning if IDs Leak (Should Never Happen)

```
[openai-codex-plugin] WARNING: 1 IDs still present after filtering: ['msg_abc123']
```

❌ **This would indicate a bug** - should never appear

---

## Integration Test Plan

### Manual Testing Procedure

#### Step 1: Fresh Install Test

```bash
# 1. Clear cache
(cd ~ && rm -rf .cache/opencode/node_modules/opencode-openai-codex-auth)

# 2. Use minimal config
cat > ~/.config/opencode/opencode.jsonc <<'EOF'
{
  "plugin": ["opencode-openai-codex-auth"],
  "model": "openai/gpt-5-codex"
}
EOF

# 3. Test default model
DEBUG_CODEX_PLUGIN=1 opencode run "write hello world to test.txt"
```

**Verify:**
- ✅ Plugin installs automatically
- ✅ Auth works
- ✅ Debug log shows: `hasModelSpecificConfig: false`
- ✅ Model normalizes to `"gpt-5-codex"`
- ✅ No errors

---

#### Step 2: Custom Config Test

```bash
# Update config with custom models
cat > ~/.config/opencode/opencode.jsonc <<'EOF'
{
  "plugin": ["opencode-openai-codex-auth"],
  "provider": {
    "openai": {
      "models": {
        "gpt-5-codex-low": {
          "name": "GPT 5 Codex Low (OAuth)",
          "options": { "reasoningEffort": "low" }
        },
        "gpt-5-codex-high": {
          "name": "GPT 5 Codex High (OAuth)",
          "options": { "reasoningEffort": "high" }
        }
      }
    }
  }
}
EOF

# Test per-model options
DEBUG_CODEX_PLUGIN=1 opencode run "test low" --model=openai/gpt-5-codex-low
DEBUG_CODEX_PLUGIN=1 opencode run "test high" --model=openai/gpt-5-codex-high
```

**Verify:**
- ✅ Debug log shows: `hasModelSpecificConfig: true` for both
- ✅ Different `reasoningEffort` values in logs
- ✅ TUI shows friendly names

---

#### Step 3: Multi-Turn Test (Critical for store:false)

```bash
DEBUG_CODEX_PLUGIN=1 opencode --model=openai/gpt-5-codex-medium
```

```
> write "test content" to file1.txt
> read file1.txt
> what did you just write?
> create file2.txt with different content
> compare the two files
```

**Verify:**
- ✅ No "item not found" errors on ANY turn
- ✅ Debug shows IDs removed on turns 2+
- ✅ Context is maintained across turns
- ✅ All tool calls work correctly

---

#### Step 4: Model Switching Test

```bash
DEBUG_CODEX_PLUGIN=1 opencode
```

```
> /model openai/gpt-5-codex-low
> write hello to test.txt
> /model openai/gpt-5-codex-high
> write goodbye to test2.txt
```

**Verify:**
- ✅ Different reasoning efforts logged for each model
- ✅ Per-model options applied correctly
- ✅ No errors when switching

---

#### Step 5: TUI Persistence Test

```bash
# 1. Start opencode
opencode --model=openai/gpt-5-codex-high

# 2. Run a command
> write test

# 3. Exit (ctrl+c)

# 4. Restart
opencode

# 5. Check which model is selected
> /model
```

**Verify:**
- ✅ Last used model is `gpt-5-codex-high`
- ✅ Model is auto-selected on restart
- ✅ TUI shows correct model highlighted

---

## Normalization Edge Cases

### Test: normalizeModel() Coverage

```typescript
normalizeModel("gpt-5.2-codex")         // → "gpt-5.2-codex" ✅
normalizeModel("gpt-5.2-codex-high")    // → "gpt-5.2-codex" ✅
normalizeModel("gpt-5.2-xhigh")         // → "gpt-5.2" ✅
normalizeModel("gpt-5.1-codex-max-xhigh")// → "gpt-5.1-codex-max" ✅
normalizeModel("gpt-5.1-codex-mini-high")// → "gpt-5.1-codex-mini" ✅
normalizeModel("codex-mini-latest")     // → "gpt-5.1-codex-mini" ✅
normalizeModel("gpt-5.1-codex")         // → "gpt-5.1-codex" ✅
normalizeModel("gpt-5.1")               // → "gpt-5.1" ✅
normalizeModel("my-codex-model")        // → "gpt-5.1-codex" ✅
normalizeModel("gpt-5")                 // → "gpt-5.1" ✅
normalizeModel("gpt-5-mini")            // → "gpt-5.1" ✅
normalizeModel("gpt-5-nano")            // → "gpt-5.1" ✅
normalizeModel("GPT 5 High")            // → "gpt-5.1" ✅
normalizeModel(undefined)               // → "gpt-5.1" ✅
normalizeModel("random-model")          // → "gpt-5.1" ✅ (fallback)
```

**Implementation:**
```typescript
export function normalizeModel(model: string | undefined): string {
  if (!model) return "gpt-5.1";
  const modelId = model.includes("/") ? model.split("/").pop()! : model;
  const mappedModel = MODEL_MAP[modelId];
  if (mappedModel) return mappedModel;

  const normalized = modelId.toLowerCase();

  if (normalized.includes("gpt-5.2-codex") || normalized.includes("gpt 5.2 codex")) {
    return "gpt-5.2-codex";
  }
  if (normalized.includes("gpt-5.2") || normalized.includes("gpt 5.2")) {
    return "gpt-5.2";
  }
  if (normalized.includes("gpt-5.1-codex-max") || normalized.includes("gpt 5.1 codex max")) {
    return "gpt-5.1-codex-max";
  }
  if (normalized.includes("gpt-5.1-codex-mini") || normalized.includes("gpt 5.1 codex mini")) {
    return "gpt-5.1-codex-mini";
  }
  if (
    normalized.includes("codex-mini-latest") ||
    normalized.includes("gpt-5-codex-mini") ||
    normalized.includes("gpt 5 codex mini")
  ) {
    return "codex-mini-latest";
  }
  if (normalized.includes("gpt-5.1-codex") || normalized.includes("gpt 5.1 codex")) {
    return "gpt-5.1-codex";
  }
  if (normalized.includes("gpt-5.1") || normalized.includes("gpt 5.1")) {
    return "gpt-5.1";
  }
  if (normalized.includes("codex")) {
    return "gpt-5.1-codex";
  }
  if (normalized.includes("gpt-5") || normalized.includes("gpt 5")) {
    return "gpt-5.1";
  }
  return "gpt-5.1";
}
```

**Why this works:**
- ✅ Case-insensitive (`.toLowerCase()` + `.includes()`)
- ✅ Pattern-based (works with any naming)
- ✅ Safe fallback (unknown models → `gpt-5.1`)
- ✅ Codex priority with explicit Codex Mini support (`codex-mini*` → `codex-mini-latest`)

---

## Expected Failures (These Should Error)

### Invalid Model Selection

```bash
opencode run "test" --model=openai/claude-3.5
```

**Expected:** ❌ Error before plugin (OpenCode rejects unknown model)

### Missing Authentication

```bash
# Without running: opencode auth login
opencode run "test" --model=openai/gpt-5-codex
```

**Expected:** ❌ 401 Unauthorized error

---

## Success Criteria

### All Tests Must Pass

- [ ] Default models work without custom config
- [ ] Custom config variants use per-model options
- [ ] Old config format still works (backwards compat)
- [ ] Mixed default + custom models work
- [ ] Multi-turn conversations have no ID errors
- [ ] Model switching works correctly
- [ ] TUI persistence remembers last used model
- [ ] Debug logging shows correct information
- [ ] All normalization edge cases work

### No Errors

- [ ] No "item not found" errors
- [ ] No TypeScript errors
- [ ] No authentication errors (after login)
- [ ] No config validation errors

---

## Automated Test Suggestions

### Unit Tests (Future)

```typescript
describe('normalizeModel', () => {
  test('handles all default models', () => {
    expect(normalizeModel('gpt-5')).toBe('gpt-5')
    expect(normalizeModel('gpt-5-codex')).toBe('gpt-5-codex')
    expect(normalizeModel('gpt-5-codex-mini')).toBe('codex-mini-latest')
    expect(normalizeModel('gpt-5-mini')).toBe('gpt-5')
    expect(normalizeModel('gpt-5-nano')).toBe('gpt-5')
  })

  test('handles custom preset names', () => {
    expect(normalizeModel('gpt-5-codex-low')).toBe('gpt-5-codex')
    expect(normalizeModel('openai/gpt-5-codex-mini-high')).toBe('codex-mini-latest')
    expect(normalizeModel('gpt-5-high')).toBe('gpt-5')
  })

  test('handles legacy names', () => {
    expect(normalizeModel('GPT 5 Codex Low (ChatGPT Subscription)')).toBe('gpt-5-codex')
  })

  test('handles edge cases', () => {
    expect(normalizeModel(undefined)).toBe('gpt-5')
    expect(normalizeModel('codex-mini-latest')).toBe('codex-mini-latest')
    expect(normalizeModel('random')).toBe('gpt-5')
  })
})

describe('getModelConfig', () => {
  test('returns per-model options when found', () => {
    const config = getModelConfig('gpt-5-codex-low', {
      global: { reasoningEffort: 'medium' },
      models: {
        'gpt-5-codex-low': {
          options: { reasoningEffort: 'low' }
        }
      }
    })
    expect(config.reasoningEffort).toBe('low')
  })

  test('returns global options when model not in config', () => {
    const config = getModelConfig('gpt-5-codex', {
      global: { reasoningEffort: 'medium' },
      models: {}
    })
    expect(config.reasoningEffort).toBe('medium')
  })
})

describe('filterInput', () => {
  test('removes all message IDs', () => {
    const input = [
      { id: 'msg_123', role: 'user', content: [] },
      { id: 'rs_456', role: 'assistant', content: [] },
      { role: 'user', content: [] }  // No ID
    ]
    const result = filterInput(input)
    expect(result.every(item => !item.id)).toBe(true)
  })
})
```

---

## See Also

- [IMPLEMENTATION_SUMMARY.md](./IMPLEMENTATION_SUMMARY.md) - Complete summary
- [CONFIG_FIELDS.md](./CONFIG_FIELDS.md) - Field usage guide
- [BUGS_FIXED.md](./BUGS_FIXED.md) - Bug analysis
```

## File: `lib/config.ts`
```typescript
import { readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import { homedir } from "node:os";
import type { PluginConfig } from "./types.js";

const CONFIG_PATH = join(homedir(), ".opencode", "openai-codex-auth-config.json");

/**
 * Default plugin configuration
 * CODEX_MODE is enabled by default for better Codex CLI parity
 */
const DEFAULT_CONFIG: PluginConfig = {
	codexMode: true,
};

/**
 * Load plugin configuration from ~/.opencode/openai-codex-auth-config.json
 * Falls back to defaults if file doesn't exist or is invalid
 *
 * @returns Plugin configuration
 */
export function loadPluginConfig(): PluginConfig {
	try {
		if (!existsSync(CONFIG_PATH)) {
			return DEFAULT_CONFIG;
		}

		const fileContent = readFileSync(CONFIG_PATH, "utf-8");
		const userConfig = JSON.parse(fileContent) as Partial<PluginConfig>;

		// Merge with defaults
		return {
			...DEFAULT_CONFIG,
			...userConfig,
		};
	} catch (error) {
		console.warn(
			`[openai-codex-plugin] Failed to load config from ${CONFIG_PATH}:`,
			(error as Error).message
		);
		return DEFAULT_CONFIG;
	}
}

/**
 * Get the effective CODEX_MODE setting
 * Priority: environment variable > config file > default (true)
 *
 * @param pluginConfig - Plugin configuration from file
 * @returns True if CODEX_MODE should be enabled
 */
export function getCodexMode(pluginConfig: PluginConfig): boolean {
	// Environment variable takes precedence
	if (process.env.CODEX_MODE !== undefined) {
		return process.env.CODEX_MODE === "1";
	}

	// Use config setting (defaults to true)
	return pluginConfig.codexMode ?? true;
}
```

## File: `lib/constants.ts`
```typescript
/**
 * Constants used throughout the plugin
 * Centralized for easy maintenance and configuration
 */

/** Plugin identifier for logging and error messages */
export const PLUGIN_NAME = "openai-codex-plugin";

/** Base URL for ChatGPT backend API */
export const CODEX_BASE_URL = "https://chatgpt.com/backend-api";

/** Dummy API key used for OpenAI SDK (actual auth via OAuth) */
export const DUMMY_API_KEY = "chatgpt-oauth";

/** Provider ID for opencode configuration */
export const PROVIDER_ID = "openai";

/** HTTP Status Codes */
export const HTTP_STATUS = {
	OK: 200,
	UNAUTHORIZED: 401,
	NOT_FOUND: 404,
	TOO_MANY_REQUESTS: 429,
} as const;

/** OpenAI-specific headers */
export const OPENAI_HEADERS = {
	BETA: "OpenAI-Beta",
	ACCOUNT_ID: "chatgpt-account-id",
	ORIGINATOR: "originator",
	SESSION_ID: "session_id",
	CONVERSATION_ID: "conversation_id",
} as const;

/** OpenAI-specific header values */
export const OPENAI_HEADER_VALUES = {
	BETA_RESPONSES: "responses=experimental",
	ORIGINATOR_CODEX: "codex_cli_rs",
} as const;

/** URL path segments */
export const URL_PATHS = {
	RESPONSES: "/responses",
	CODEX_RESPONSES: "/codex/responses",
} as const;

/** JWT claim path for ChatGPT account ID */
export const JWT_CLAIM_PATH = "https://api.openai.com/auth" as const;

/** Error messages */
export const ERROR_MESSAGES = {
	NO_ACCOUNT_ID: "Failed to extract accountId from token",
	TOKEN_REFRESH_FAILED: "Failed to refresh token, authentication required",
	REQUEST_PARSE_ERROR: "Error parsing request",
} as const;

/** Log stages for request logging */
export const LOG_STAGES = {
	BEFORE_TRANSFORM: "before-transform",
	AFTER_TRANSFORM: "after-transform",
	RESPONSE: "response",
	ERROR_RESPONSE: "error-response",
} as const;

/** Platform-specific browser opener commands */
export const PLATFORM_OPENERS = {
	darwin: "open",
	win32: "start",
	linux: "xdg-open",
} as const;

/** OAuth authorization labels */
export const AUTH_LABELS = {
	OAUTH: "ChatGPT Plus/Pro (Codex Subscription)",
	OAUTH_MANUAL: "ChatGPT Plus/Pro (Manual URL Paste)",
	API_KEY: "Manually enter API Key",
	INSTRUCTIONS:
		"A browser window should open. If it doesn't, copy the URL and open it manually.",
	INSTRUCTIONS_MANUAL:
		"After logging in, copy the full redirect URL and paste it here.",
} as const;
```

## File: `lib/logger.ts`
```typescript
import { writeFileSync, mkdirSync, existsSync } from "node:fs";
import { join } from "node:path";
import { homedir } from "node:os";
import { PLUGIN_NAME } from "./constants.js";

// Logging configuration
export const LOGGING_ENABLED = process.env.ENABLE_PLUGIN_REQUEST_LOGGING === "1";
export const DEBUG_ENABLED = process.env.DEBUG_CODEX_PLUGIN === "1" || LOGGING_ENABLED;
const LOG_DIR = join(homedir(), ".opencode", "logs", "codex-plugin");

// Log startup message about logging state
if (LOGGING_ENABLED) {
	console.log(`[${PLUGIN_NAME}] Request logging ENABLED - logs will be saved to:`, LOG_DIR);
}
if (DEBUG_ENABLED && !LOGGING_ENABLED) {
	console.log(`[${PLUGIN_NAME}] Debug logging ENABLED`);
}

let requestCounter = 0;

/**
 * Log request data to file (only when LOGGING_ENABLED is true)
 * @param stage - The stage of the request (e.g., "before-transform", "after-transform")
 * @param data - The data to log
 */
export function logRequest(stage: string, data: Record<string, unknown>): void {
	// Only log if explicitly enabled via environment variable
	if (!LOGGING_ENABLED) return;

	// Ensure log directory exists on first log
	if (!existsSync(LOG_DIR)) {
		mkdirSync(LOG_DIR, { recursive: true });
	}

	const timestamp = new Date().toISOString();
	const requestId = ++requestCounter;
	const filename = join(LOG_DIR, `request-${requestId}-${stage}.json`);

	try {
		writeFileSync(
			filename,
			JSON.stringify(
				{
					timestamp,
					requestId,
					stage,
					...data,
				},
				null,
				2,
			),
			"utf8",
		);
		console.log(`[${PLUGIN_NAME}] Logged ${stage} to ${filename}`);
	} catch (e) {
		const error = e as Error;
		console.error(`[${PLUGIN_NAME}] Failed to write log:`, error.message);
	}
}

/**
 * Log debug information (only when DEBUG_ENABLED is true)
 * @param message - Debug message
 * @param data - Optional data to log
 */
export function logDebug(message: string, data?: unknown): void {
	if (!DEBUG_ENABLED) return;

	if (data !== undefined) {
		console.log(`[${PLUGIN_NAME}] ${message}`, data);
	} else {
		console.log(`[${PLUGIN_NAME}] ${message}`);
	}
}

/**
 * Log warning (always enabled for important issues)
 * @param message - Warning message
 * @param data - Optional data to log
 */
export function logWarn(message: string, data?: unknown): void {
	if (!DEBUG_ENABLED && !LOGGING_ENABLED) return;
	if (data !== undefined) {
		console.warn(`[${PLUGIN_NAME}] ${message}`, data);
	} else {
		console.warn(`[${PLUGIN_NAME}] ${message}`);
	}
}
```

## File: `lib/oauth-success.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenCode - Authentication Successful</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: "IBM Plex Mono", monospace;
            font-weight: 400;
            background: #0a0a0a;
            color: #B7B1B1;
            overflow: hidden;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }

        /* Matrix rain background */
        .matrix {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            opacity: 0.35;
        }

        /* Scan lines effect */
        .scanline {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(
                transparent 50%,
                rgba(0, 0, 0, 0.1) 50%
            );
            background-size: 100% 4px;
            z-index: 2;
            pointer-events: none;
            animation: scan 8s linear infinite;
        }

        @keyframes scan {
            0% { transform: translateY(0); }
            100% { transform: translateY(4px); }
        }

        /* Vignette effect */
        .vignette {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            box-shadow: inset 0 0 200px rgba(0, 0, 0, 0.8);
            z-index: 2;
            pointer-events: none;
        }

        .container {
            width: 90%;
            max-width: 650px;
            text-align: center;
            z-index: 10;
            position: relative;
            animation: fadeIn 0.8s ease-out;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: scale(0.95);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }

        .logo {
            margin-bottom: 60px;
            opacity: 0;
            animation: logoEntrance 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) 0.3s forwards;
            position: relative;
        }

        @keyframes logoEntrance {
            0% {
                opacity: 0;
                transform: translateY(-50px) rotateX(90deg);
            }
            100% {
                opacity: 1;
                transform: translateY(0) rotateX(0);
            }
        }

        .logo svg {
            width: 300px;
            height: auto;
            filter: drop-shadow(0 0 30px rgba(241, 236, 236, 0.3));
            animation: pulse 3s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% {
                filter: drop-shadow(0 0 30px rgba(241, 236, 236, 0.3));
            }
            50% {
                filter: drop-shadow(0 0 50px rgba(241, 236, 236, 0.5));
            }
        }

        /* Glowing orb behind logo */
        .logo::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(241, 236, 236, 0.1) 0%, transparent 70%);
            border-radius: 50%;
            animation: orbPulse 4s ease-in-out infinite;
            z-index: -1;
        }

        @keyframes orbPulse {
            0%, 100% {
                transform: translate(-50%, -50%) scale(1);
                opacity: 0.3;
            }
            50% {
                transform: translate(-50%, -50%) scale(1.2);
                opacity: 0.6;
            }
        }

        .terminal-window {
            background: rgba(26, 26, 26, 0.95);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(75, 70, 70, 0.3);
            border-radius: 12px;
            margin: 30px 0;
            opacity: 0;
            animation: boxEntrance 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 0.6s forwards;
            position: relative;
            overflow: hidden;
            box-shadow:
                0 0 60px rgba(0, 0, 0, 0.5),
                inset 0 1px 0 rgba(255, 255, 255, 0.05);
        }

        .terminal-header {
            background: rgba(15, 15, 15, 0.9);
            padding: 14px 18px;
            display: flex;
            align-items: center;
            gap: 8px;
            border-bottom: 1px solid rgba(75, 70, 70, 0.3);
            position: relative;
        }

        .terminal-button {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            transition: transform 0.2s;
        }

        .terminal-button:hover {
            transform: scale(1.2);
        }

        .terminal-button.red {
            background: #ff5f56;
            box-shadow: 0 0 10px rgba(255, 95, 86, 0.3);
            animation: pulse 2s infinite;
        }

        .terminal-button.yellow {
            background: #ffbd2e;
            box-shadow: 0 0 10px rgba(255, 189, 46, 0.3);
            animation: pulse 2s infinite 0.3s;
        }

        .terminal-button.green {
            background: #27c93f;
            box-shadow: 0 0 10px rgba(39, 201, 63, 0.3);
            animation: pulse 2s infinite 0.6s;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.6; }
        }

        .terminal-title {
            flex: 1;
            text-align: center;
            font-size: 12px;
            color: #6a6565;
            opacity: 0.8;
            letter-spacing: 0.5px;
        }

        .status-box {
            padding: 50px 40px;
            position: relative;
        }

        @keyframes boxEntrance {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Animated border gradient */
        .terminal-window::before {
            content: '';
            position: absolute;
            top: -2px;
            left: -2px;
            right: -2px;
            bottom: -2px;
            background: linear-gradient(
                45deg,
                transparent,
                rgba(241, 236, 236, 0.1),
                transparent,
                rgba(241, 236, 236, 0.1)
            );
            background-size: 400% 400%;
            border-radius: 12px;
            z-index: -1;
            animation: gradientShift 8s ease infinite;
        }

        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }

        .checkmark-container {
            width: 100px;
            height: 100px;
            margin: 0 auto 40px;
            position: relative;
        }

        .checkmark-circle {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            border: 4px solid transparent;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            animation: circleAppear 0.6s ease-out 1s both;
        }

        @keyframes circleAppear {
            from {
                transform: scale(0) rotate(-180deg);
                border-color: transparent;
            }
            to {
                transform: scale(1) rotate(0);
                border-color: #4B4646;
            }
        }

        /* Spinning rings around checkmark */
        .checkmark-circle::before,
        .checkmark-circle::after {
            content: '';
            position: absolute;
            width: 120%;
            height: 120%;
            border: 2px solid transparent;
            border-top-color: rgba(241, 236, 236, 0.2);
            border-radius: 50%;
            animation: rotate 3s linear infinite;
        }

        .checkmark-circle::after {
            width: 140%;
            height: 140%;
            border-top-color: rgba(183, 177, 177, 0.1);
            animation: rotate 4s linear infinite reverse;
        }

        @keyframes rotate {
            to { transform: rotate(360deg); }
        }

        .checkmark {
            width: 35px;
            height: 18px;
            border-left: 5px solid #F1ECEC;
            border-bottom: 5px solid #F1ECEC;
            transform: rotate(-45deg) scale(0);
            animation: checkmarkDraw 0.5s cubic-bezier(0.65, 0, 0.45, 1) 1.3s forwards;
            filter: drop-shadow(0 0 10px rgba(241, 236, 236, 0.5));
        }

        @keyframes checkmarkDraw {
            0% {
                transform: rotate(-45deg) scale(0);
            }
            50% {
                transform: rotate(-45deg) scale(1.1);
            }
            100% {
                transform: rotate(-45deg) scale(1);
            }
        }

        .title {
            font-size: 32px;
            color: #00ff41;
            margin-bottom: 20px;
            font-weight: 500;
            letter-spacing: 1px;
            text-shadow: 0 0 20px rgba(0, 255, 65, 0.5);
            opacity: 0;
            animation: fadeInUp 0.6s ease-out 1.8s forwards;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .message {
            font-size: 16px;
            color: #9a9595;
            line-height: 1.8;
            margin-bottom: 30px;
            opacity: 0;
            animation: fadeInUp 0.6s ease-out 2s forwards;
        }

        .terminal-output {
            background: rgba(10, 10, 10, 0.6);
            border: 1px solid rgba(75, 70, 70, 0.2);
            border-radius: 8px;
            padding: 25px;
            text-align: left;
            font-size: 14px;
            line-height: 2;
            margin-top: 25px;
            position: relative;
            overflow: hidden;
        }

        /* Terminal typing effect */
        .terminal-output::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, #4B4646, transparent);
            animation: scanProgress 2s ease-out 2.2s forwards;
        }

        @keyframes scanProgress {
            from {
                transform: translateX(-100%);
            }
            to {
                transform: translateX(100%);
            }
        }

        .terminal-line {
            opacity: 0;
            transform: translateX(-20px);
            animation: terminalType 0.4s ease-out forwards;
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .terminal-line:nth-child(1) { animation-delay: 2.2s; }
        .terminal-line:nth-child(2) { animation-delay: 2.4s; }
        .terminal-line:nth-child(3) { animation-delay: 2.6s; }
        .terminal-line:nth-child(4) { animation-delay: 2.8s; }

        @keyframes terminalType {
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .prompt {
            color: #6a6565;
            font-weight: 500;
        }

        .success {
            color: #B7B1B1;
        }

        .terminal-line::after {
            content: '';
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, rgba(75, 70, 70, 0.3), transparent);
        }

        .footer {
            margin-top: 40px;
            font-size: 14px;
            color: #6a6565;
            opacity: 0;
            animation: fadeInUp 0.6s ease-out 3.2s forwards;
            text-shadow: 0 0 10px rgba(106, 101, 101, 0.5);
        }

        .cursor {
            display: inline-block;
            width: 2px;
            height: 16px;
            background: #8a8585;
            margin-left: 6px;
            animation: blink 1s infinite;
            box-shadow: 0 0 8px #8a8585;
        }

        @keyframes blink {
            0%, 49% { opacity: 1; }
            50%, 100% { opacity: 0; }
        }

        /* Floating particles */
        .particle {
            position: fixed;
            width: 2px;
            height: 2px;
            background: rgba(183, 177, 177, 0.3);
            border-radius: 50%;
            pointer-events: none;
            z-index: 5;
            animation: float 8s linear infinite;
        }

        @keyframes float {
            0% {
                transform: translateY(100vh) translateX(0) scale(0);
                opacity: 0;
            }
            10% {
                opacity: 1;
                transform: translateY(90vh) translateX(10px) scale(1);
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-10vh) translateX(-10px) scale(0);
                opacity: 0;
            }
        }

        /* Success glow effect */
        @keyframes successGlow {
            0%, 100% {
                box-shadow:
                    0 0 60px rgba(0, 0, 0, 0.5),
                    inset 0 1px 0 rgba(255, 255, 255, 0.05);
            }
            50% {
                box-shadow:
                    0 0 80px rgba(241, 236, 236, 0.1),
                    inset 0 1px 0 rgba(255, 255, 255, 0.05);
            }
        }

        .terminal-window {
            animation:
                boxEntrance 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) 0.6s forwards,
                successGlow 4s ease-in-out 2s infinite;
        }
    </style>
</head>
<body>
    <canvas class="matrix" id="matrix"></canvas>
    <div class="scanline"></div>
    <div class="vignette"></div>

    <div class="container">
        <div class="logo">
            <svg width="300" height="54" viewBox="0 0 234 42" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M18 30H6V18H18V30Z" fill="#4B4646"/>
                <path d="M18 12H6V30H18V12ZM24 36H0V6H24V36Z" fill="#B7B1B1"/>
                <path d="M48 30H36V18H48V30Z" fill="#4B4646"/>
                <path d="M36 30H48V12H36V30ZM54 36H36V42H30V6H54V36Z" fill="#B7B1B1"/>
                <path d="M84 24V30H66V24H84Z" fill="#4B4646"/>
                <path d="M84 24H66V30H84V36H60V6H84V24ZM66 18H78V12H66V18Z" fill="#B7B1B1"/>
                <path d="M108 36H96V18H108V36Z" fill="#4B4646"/>
                <path d="M108 12H96V36H90V6H108V12ZM114 36H108V12H114V36Z" fill="#B7B1B1"/>
                <path d="M144 30H126V18H144V30Z" fill="#4B4646"/>
                <path d="M144 12H126V30H144V36H120V6H144V12Z" fill="#F1ECEC"/>
                <path d="M168 30H156V18H168V30Z" fill="#4B4646"/>
                <path d="M168 12H156V30H168V12ZM174 36H150V6H174V36Z" fill="#F1ECEC"/>
                <path d="M198 30H186V18H198V30Z" fill="#4B4646"/>
                <path d="M198 12H186V30H198V12ZM204 36H180V6H198V0H204V36Z" fill="#F1ECEC"/>
                <path d="M234 24V30H216V24H234Z" fill="#4B4646"/>
                <path d="M216 12V18H228V12H216ZM234 24H216V30H234V36H210V6H234V24Z" fill="#F1ECEC"/>
            </svg>
        </div>

        <div class="terminal-window">
            <div class="terminal-header">
                <div class="terminal-button red"></div>
                <div class="terminal-button yellow"></div>
                <div class="terminal-button green"></div>
                <div class="terminal-title">opencode-openai-codex-auth@4.4.0 — OAuth Authentication</div>
            </div>

            <div class="status-box">
                <div class="checkmark-container">
                    <div class="checkmark-circle">
                        <div class="checkmark"></div>
                    </div>
                </div>

                <div class="title">ACCESS GRANTED</div>
                <div class="message">
                    OpenAI ChatGPT authentication successful<br>
                    Your credentials have been securely stored
                </div>

                <div class="terminal-output">
                    <div class="terminal-line">
                        <span class="prompt">▸</span>
                        <span class="success">Initializing OAuth handshake...</span>
                    </div>
                    <div class="terminal-line">
                        <span class="prompt">▸</span>
                        <span class="success">Token exchange verified</span>
                    </div>
                    <div class="terminal-line">
                        <span class="prompt">▸</span>
                        <span class="success">Credentials encrypted & stored</span>
                    </div>
                    <div class="terminal-line">
                        <span class="prompt">✓</span>
                        <span class="success">OpenCode ready for deployment</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="footer">
            Return to your terminal to continue<span class="cursor"></span>
        </div>
    </div>

    <script>
        // Enhanced Matrix rain effect with mouse interaction
        const canvas = document.getElementById('matrix');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        // Mix of characters including OpenCode themed ones
        const chars = 'OPENCODE▸✓▹▸◂◃◄►◀▶←→↑↓⟨⟩∧∨∩∪⊂⊃⊆⊇∈∉∀∃∄∅∞≡≠≤≥±∓⊕⊗⊙01';
        const fontSize = 16;
        const columns = Math.floor(canvas.width / fontSize);

        const drops = Array(columns).fill(1);
        const speeds = Array(columns).fill(0).map(() => Math.random() * 0.5 + 0.5);

        // Track mouse position
        let mouseX = -1000;
        let mouseY = -1000;

        canvas.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });

        canvas.addEventListener('mouseleave', () => {
            mouseX = -1000;
            mouseY = -1000;
        });

        function drawMatrix() {
            ctx.fillStyle = 'rgba(10, 10, 10, 0.08)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.font = fontSize + 'px "IBM Plex Mono"';

            for (let i = 0; i < drops.length; i++) {
                const text = chars[Math.floor(Math.random() * chars.length)];
                const x = i * fontSize;
                const y = drops[i] * fontSize;

                // Check distance from mouse
                const distanceFromMouse = Math.sqrt(
                    Math.pow(x - mouseX, 2) + Math.pow(y - mouseY, 2)
                );

                const hoverRadius = 80;
                const isNearMouse = distanceFromMouse < hoverRadius;

                if (isNearMouse) {
                    // Matrix green color when near mouse
                    const intensity = 1 - (distanceFromMouse / hoverRadius);
                    ctx.fillStyle = `rgba(0, 255, 65, ${intensity * 0.95})`;
                    ctx.shadowBlur = 20 * intensity;
                    ctx.shadowColor = '#00ff41';
                } else {
                    // Bright white gradient by default
                    const gradient = ctx.createLinearGradient(0, y - fontSize * 10, 0, y);
                    gradient.addColorStop(0, 'rgba(200, 200, 200, 0)');
                    gradient.addColorStop(0.5, 'rgba(241, 236, 236, 0.8)');
                    gradient.addColorStop(1, 'rgba(255, 255, 255, 1)');
                    ctx.fillStyle = gradient;
                    ctx.shadowBlur = 0;
                }

                ctx.fillText(text, x, y);

                // Randomly reset drops
                if (drops[i] * fontSize > canvas.height && Math.random() > 0.98) {
                    drops[i] = 0;
                    speeds[i] = Math.random() * 0.5 + 0.5;
                }

                drops[i] += speeds[i];
            }

            // Reset shadow for next frame
            ctx.shadowBlur = 0;
        }

        setInterval(drawMatrix, 40);

        // Create floating particles
        function createParticle() {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 8 + 's';
            particle.style.animationDuration = (Math.random() * 4 + 6) + 's';
            document.body.appendChild(particle);

            setTimeout(() => particle.remove(), 10000);
        }

        // Generate particles periodically
        for (let i = 0; i < 20; i++) {
            setTimeout(createParticle, i * 400);
        }

        setInterval(() => {
            if (Math.random() > 0.7) createParticle();
        }, 2000);

        // Resize handler
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });

        // Add subtle mouse parallax effect
        document.addEventListener('mousemove', (e) => {
            const moveX = (e.clientX - window.innerWidth / 2) / 50;
            const moveY = (e.clientY - window.innerHeight / 2) / 50;

            document.querySelector('.container').style.transform =
                `translate(${moveX}px, ${moveY}px)`;
        });
    </script>
</body>
</html>
```

## File: `lib/types.ts`
```typescript
import type { Auth, Provider, Model } from "@opencode-ai/sdk";

/**
 * Plugin configuration from ~/.opencode/openai-codex-auth-config.json
 */
export interface PluginConfig {
	/**
	 * Enable CODEX_MODE (Codex-OpenCode bridge prompt instead of tool remap)
	 * @default true
	 */
	codexMode?: boolean;
}

/**
 * User configuration structure from opencode.json
 */
export interface UserConfig {
	global: ConfigOptions;
	models: {
		[modelName: string]: {
			options?: ConfigOptions;
			variants?: Record<string, (ConfigOptions & { disabled?: boolean }) | undefined>;
			[key: string]: unknown;
		};
	};
}

/**
 * Configuration options for reasoning and text settings
 */
export interface ConfigOptions {
	reasoningEffort?: "none" | "minimal" | "low" | "medium" | "high" | "xhigh";
	reasoningSummary?: "auto" | "concise" | "detailed" | "off" | "on";
	textVerbosity?: "low" | "medium" | "high";
	include?: string[];
}

/**
 * Reasoning configuration for requests
 */
export interface ReasoningConfig {
	effort: "none" | "minimal" | "low" | "medium" | "high" | "xhigh";
	summary: "auto" | "concise" | "detailed" | "off" | "on";
}

/**
 * OAuth server information
 */
export interface OAuthServerInfo {
	port: number;
	ready: boolean;
	close: () => void;
	waitForCode: (state: string) => Promise<{ code: string } | null>;
}

/**
 * PKCE challenge and verifier
 */
export interface PKCEPair {
	challenge: string;
	verifier: string;
}

/**
 * Authorization flow result
 */
export interface AuthorizationFlow {
	pkce: PKCEPair;
	state: string;
	url: string;
}

/**
 * Token exchange success result
 */
export interface TokenSuccess {
	type: "success";
	access: string;
	refresh: string;
	expires: number;
}

/**
 * Token exchange failure result
 */
export interface TokenFailure {
	type: "failed";
}

/**
 * Token exchange result
 */
export type TokenResult = TokenSuccess | TokenFailure;

/**
 * Parsed authorization input
 */
export interface ParsedAuthInput {
	code?: string;
	state?: string;
}

/**
 * JWT payload with ChatGPT account info
 */
export interface JWTPayload {
	"https://api.openai.com/auth"?: {
		chatgpt_account_id?: string;
	};
	[key: string]: unknown;
}

/**
 * Message input item
 */
export interface InputItem {
	id?: string;
	type: string;
	role: string;
	content?: unknown;
	[key: string]: unknown;
}

/**
 * Request body structure
 */
export interface RequestBody {
	model: string;
	store?: boolean;
	stream?: boolean;
	instructions?: string;
	input?: InputItem[];
	tools?: unknown;
	reasoning?: Partial<ReasoningConfig>;
	text?: {
		verbosity?: "low" | "medium" | "high";
	};
	include?: string[];
	providerOptions?: {
		openai?: Partial<ConfigOptions> & { store?: boolean; include?: string[] };
		[key: string]: unknown;
	};
	/** Stable key to enable prompt-token caching on Codex backend */
	prompt_cache_key?: string;
	max_output_tokens?: number;
	max_completion_tokens?: number;
	[key: string]: unknown;
}

/**
 * SSE event data structure
 */
export interface SSEEventData {
	type: string;
	response?: unknown;
	[key: string]: unknown;
}

/**
 * Cache metadata for Codex instructions
 */
export interface CacheMetadata {
	etag: string | null;
	tag: string;
	lastChecked: number;
	url: string;
}

/**
 * GitHub release data
 */
export interface GitHubRelease {
	tag_name: string;
	[key: string]: unknown;
}

// Re-export SDK types for convenience
export type { Auth, Provider, Model };
```

## File: `lib/auth/auth.ts`
```typescript
import { generatePKCE } from "@openauthjs/openauth/pkce";
import { randomBytes } from "node:crypto";
import type { PKCEPair, AuthorizationFlow, TokenResult, ParsedAuthInput, JWTPayload } from "../types.js";

// OAuth constants (from openai/codex)
export const CLIENT_ID = "app_EMoamEEZ73f0CkXaXp7hrann";
export const AUTHORIZE_URL = "https://auth.openai.com/oauth/authorize";
export const TOKEN_URL = "https://auth.openai.com/oauth/token";
export const REDIRECT_URI = "http://localhost:1455/auth/callback";
export const SCOPE = "openid profile email offline_access";

/**
 * Generate a random state value for OAuth flow
 * @returns Random hex string
 */
export function createState(): string {
	return randomBytes(16).toString("hex");
}

/**
 * Parse authorization code and state from user input
 * @param input - User input (URL, code#state, or just code)
 * @returns Parsed authorization data
 */
export function parseAuthorizationInput(input: string): ParsedAuthInput {
	const value = (input || "").trim();
	if (!value) return {};

	try {
		const url = new URL(value);
		return {
			code: url.searchParams.get("code") ?? undefined,
			state: url.searchParams.get("state") ?? undefined,
		};
	} catch {}

	if (value.includes("#")) {
		const [code, state] = value.split("#", 2);
		return { code, state };
	}
	if (value.includes("code=")) {
		const params = new URLSearchParams(value);
		return {
			code: params.get("code") ?? undefined,
			state: params.get("state") ?? undefined,
		};
	}
	return { code: value };
}

/**
 * Exchange authorization code for access and refresh tokens
 * @param code - Authorization code from OAuth flow
 * @param verifier - PKCE verifier
 * @param redirectUri - OAuth redirect URI
 * @returns Token result
 */
export async function exchangeAuthorizationCode(
	code: string,
	verifier: string,
	redirectUri: string = REDIRECT_URI,
): Promise<TokenResult> {
	const res = await fetch(TOKEN_URL, {
		method: "POST",
		headers: { "Content-Type": "application/x-www-form-urlencoded" },
		body: new URLSearchParams({
			grant_type: "authorization_code",
			client_id: CLIENT_ID,
			code,
			code_verifier: verifier,
			redirect_uri: redirectUri,
		}),
	});
	if (!res.ok) {
		const text = await res.text().catch(() => "");
		console.error("[openai-codex-plugin] code->token failed:", res.status, text);
		return { type: "failed" };
	}
	const json = (await res.json()) as {
		access_token?: string;
		refresh_token?: string;
		expires_in?: number;
	};
	if (
		!json?.access_token ||
		!json?.refresh_token ||
		typeof json?.expires_in !== "number"
	) {
		console.error("[openai-codex-plugin] token response missing fields:", json);
		return { type: "failed" };
	}
	return {
		type: "success",
		access: json.access_token,
		refresh: json.refresh_token,
		expires: Date.now() + json.expires_in * 1000,
	};
}

/**
 * Decode a JWT token to extract payload
 * @param token - JWT token to decode
 * @returns Decoded payload or null if invalid
 */
export function decodeJWT(token: string): JWTPayload | null {
	try {
		const parts = token.split(".");
		if (parts.length !== 3) return null;
		const payload = parts[1];
		const decoded = Buffer.from(payload, "base64").toString("utf-8");
		return JSON.parse(decoded) as JWTPayload;
	} catch {
		return null;
	}
}

/**
 * Refresh access token using refresh token
 * @param refreshToken - Refresh token
 * @returns Token result
 */
export async function refreshAccessToken(refreshToken: string): Promise<TokenResult> {
	try {
		const response = await fetch(TOKEN_URL, {
			method: "POST",
			headers: { "Content-Type": "application/x-www-form-urlencoded" },
			body: new URLSearchParams({
				grant_type: "refresh_token",
				refresh_token: refreshToken,
				client_id: CLIENT_ID,
			}),
		});

		if (!response.ok) {
			const text = await response.text().catch(() => "");
			console.error(
				"[openai-codex-plugin] Token refresh failed:",
				response.status,
				text,
			);
			return { type: "failed" };
		}

		const json = (await response.json()) as {
			access_token?: string;
			refresh_token?: string;
			expires_in?: number;
		};
		if (
			!json?.access_token ||
			!json?.refresh_token ||
			typeof json?.expires_in !== "number"
		) {
			console.error(
				"[openai-codex-plugin] Token refresh response missing fields:",
				json,
			);
			return { type: "failed" };
		}

		return {
			type: "success",
			access: json.access_token,
			refresh: json.refresh_token,
			expires: Date.now() + json.expires_in * 1000,
		};
	} catch (error) {
		const err = error as Error;
		console.error("[openai-codex-plugin] Token refresh error:", err);
		return { type: "failed" };
	}
}

/**
 * Create OAuth authorization flow
 * @returns Authorization flow details
 */
export async function createAuthorizationFlow(): Promise<AuthorizationFlow> {
	const pkce = (await generatePKCE()) as PKCEPair;
	const state = createState();

	const url = new URL(AUTHORIZE_URL);
	url.searchParams.set("response_type", "code");
	url.searchParams.set("client_id", CLIENT_ID);
	url.searchParams.set("redirect_uri", REDIRECT_URI);
	url.searchParams.set("scope", SCOPE);
	url.searchParams.set("code_challenge", pkce.challenge);
	url.searchParams.set("code_challenge_method", "S256");
	url.searchParams.set("state", state);
	url.searchParams.set("id_token_add_organizations", "true");
	url.searchParams.set("codex_cli_simplified_flow", "true");
	url.searchParams.set("originator", "codex_cli_rs");

	return { pkce, state, url: url.toString() };
}
```

## File: `lib/auth/browser.ts`
```typescript
/**
 * Browser utilities for OAuth flow
 * Handles platform-specific browser opening
 */

import { spawn } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { PLATFORM_OPENERS } from "../constants.js";

/**
 * Gets the platform-specific command to open a URL in the default browser
 * @returns Browser opener command for the current platform
 */
export function getBrowserOpener(): string {
	const platform = process.platform;
	if (platform === "darwin") return PLATFORM_OPENERS.darwin;
	if (platform === "win32") return PLATFORM_OPENERS.win32;
	return PLATFORM_OPENERS.linux;
}

function commandExists(command: string): boolean {
	if (!command) return false;

	// "start" is a shell builtin on Windows; rely on shell execution
	if (process.platform === "win32" && command.toLowerCase() === "start") {
		return true;
	}

	const pathValue = process.env.PATH || "";
	const entries = pathValue.split(path.delimiter).filter(Boolean);
	if (entries.length === 0) return false;

	if (process.platform === "win32") {
		const pathext = (process.env.PATHEXT || ".EXE;.CMD;.BAT;.COM")
			.split(";")
			.filter(Boolean);
		for (const entry of entries) {
			for (const ext of pathext) {
				const candidate = path.join(entry, `${command}${ext}`);
				if (fs.existsSync(candidate)) return true;
			}
		}
		return false;
	}

	for (const entry of entries) {
		const candidate = path.join(entry, command);
		if (fs.existsSync(candidate)) return true;
	}
	return false;
}

/**
 * Opens a URL in the default browser
 * Silently fails if browser cannot be opened (user can copy URL manually)
 * @param url - URL to open
 * @returns True if a browser launch was attempted
 */
export function openBrowserUrl(url: string): boolean {
	try {
		const opener = getBrowserOpener();
		if (!commandExists(opener)) {
			return false;
		}
		const child = spawn(opener, [url], {
			stdio: "ignore",
			shell: process.platform === "win32",
		});
		child.on("error", () => {});
		return true;
	} catch (error) {
		// Silently fail - user can manually open the URL from instructions
		return false;
	}
}
```

## File: `lib/auth/server.ts`
```typescript
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import type { OAuthServerInfo } from "../types.js";

// Resolve path to oauth-success.html (one level up from auth/ subfolder)
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const successHtml = fs.readFileSync(path.join(__dirname, "..", "oauth-success.html"), "utf-8");

/**
 * Start a small local HTTP server that waits for /auth/callback and returns the code
 * @param options - OAuth state for validation
 * @returns Promise that resolves to server info
 */
export function startLocalOAuthServer({ state }: { state: string }): Promise<OAuthServerInfo> {
	const server = http.createServer((req, res) => {
		try {
			const url = new URL(req.url || "", "http://localhost");
			if (url.pathname !== "/auth/callback") {
				res.statusCode = 404;
				res.end("Not found");
				return;
			}
			if (url.searchParams.get("state") !== state) {
				res.statusCode = 400;
				res.end("State mismatch");
				return;
			}
			const code = url.searchParams.get("code");
			if (!code) {
				res.statusCode = 400;
				res.end("Missing authorization code");
				return;
			}
			res.statusCode = 200;
			res.setHeader("Content-Type", "text/html; charset=utf-8");
			res.end(successHtml);
			(server as http.Server & { _lastCode?: string })._lastCode = code;
		} catch {
			res.statusCode = 500;
			res.end("Internal error");
		}
	});

	return new Promise((resolve) => {
		server
			.listen(1455, "127.0.0.1", () => {
				resolve({
					port: 1455,
					ready: true,
					close: () => server.close(),
					waitForCode: async () => {
						const poll = () => new Promise<void>((r) => setTimeout(r, 100));
						for (let i = 0; i < 600; i++) {
							const lastCode = (server as http.Server & { _lastCode?: string })._lastCode;
							if (lastCode) return { code: lastCode };
							await poll();
						}
						return null;
					},
				});
			})
			.on("error", (err: NodeJS.ErrnoException) => {
				console.error(
					"[openai-codex-plugin] Failed to bind http://127.0.0.1:1455 (",
					err?.code,
					") Falling back to manual paste.",
				);
				resolve({
					port: 1455,
					ready: false,
					close: () => {
						try {
							server.close();
						} catch {}
					},
					waitForCode: async () => null,
				});
			});
	});
}
```

## File: `lib/prompts/codex-opencode-bridge.ts`
```typescript
/**
 * Codex-OpenCode Bridge Prompt
 *
 * This prompt bridges Codex CLI instructions to the OpenCode environment.
 * It incorporates critical tool mappings, available tools list, substitution rules,
 * and verification checklist to ensure proper tool usage.
 *
 * Token Count: ~450 tokens (~90% reduction vs full OpenCode prompt)
 */

export const CODEX_OPENCODE_BRIDGE = `# Codex Running in OpenCode

You are running Codex through OpenCode, an open-source terminal coding assistant. OpenCode provides different tools but follows Codex operating principles.

## CRITICAL: Tool Replacements

<critical_rule priority="0">
❌ APPLY_PATCH DOES NOT EXIST → ✅ USE "edit" INSTEAD
- NEVER use: apply_patch, applyPatch
- ALWAYS use: edit tool for ALL file modifications
- Before modifying files: Verify you're using "edit", NOT "apply_patch"
</critical_rule>

<critical_rule priority="0">
❌ UPDATE_PLAN DOES NOT EXIST → ✅ USE "todowrite" INSTEAD
- NEVER use: update_plan, updatePlan, read_plan, readPlan
- ALWAYS use: todowrite for task/plan updates, todoread to read plans
- Before plan operations: Verify you're using "todowrite", NOT "update_plan"
</critical_rule>

## Available OpenCode Tools

**File Operations:**
- \`write\`  - Create new files
  - Overwriting existing files requires a prior Read in this session; default to ASCII unless the file already uses Unicode.
- \`edit\`   - Modify existing files (REPLACES apply_patch)
  - Requires a prior Read in this session; preserve exact indentation; ensure \`oldString\` uniquely matches or use \`replaceAll\`; edit fails if ambiguous or missing.
- \`read\`   - Read file contents

**Search/Discovery:**
- \`grep\`   - Search file contents (tool, not bash grep); use \`include\` to filter patterns; set \`path\` only when not searching workspace root; for cross-file match counts use bash with \`rg\`.
- \`glob\`   - Find files by pattern; defaults to workspace cwd unless \`path\` is set.
- \`list\`   - List directories (requires absolute paths)

**Execution:**
- \`bash\`   - Run shell commands
  - No workdir parameter; do not include it in tool calls.
  - Always include a short description for the command.
  - Do not use cd; use absolute paths in commands.
  - Quote paths containing spaces with double quotes.
  - Chain multiple commands with ';' or '&&'; avoid newlines.
  - Use Grep/Glob tools for searches; only use bash with \`rg\` when you need counts or advanced features.
  - Do not use \`ls\`/\`cat\` in bash; use \`list\`/\`read\` tools instead.
  - For deletions (rm), verify by listing parent dir with \`list\`.

**Network:**
- \`webfetch\` - Fetch web content
  - Use fully-formed URLs (http/https; http auto-upgrades to https).
  - Always set \`format\` to one of: text | markdown | html; prefer markdown unless otherwise required.
  - Read-only; short cache window.

**Task Management:**
- \`todowrite\` - Manage tasks/plans (REPLACES update_plan)
- \`todoread\`  - Read current plan

## Substitution Rules

Base instruction says:    You MUST use instead:
apply_patch           →   edit
update_plan           →   todowrite
read_plan             →   todoread

**Path Usage:** Use per-tool conventions to avoid conflicts:
- Tool calls: \`read\`, \`edit\`, \`write\`, \`list\` require absolute paths.
- Searches: \`grep\`/\`glob\` default to the workspace cwd; prefer relative include patterns; set \`path\` only when a different root is needed.
- Presentation: In assistant messages, show workspace-relative paths; use absolute paths only inside tool calls.
- Tool schema overrides general path preferences—do not convert required absolute paths to relative.

## Verification Checklist

Before file/plan modifications:
1. Am I using "edit" NOT "apply_patch"?
2. Am I using "todowrite" NOT "update_plan"?
3. Is this tool in the approved list above?
4. Am I following each tool's path requirements?

If ANY answer is NO → STOP and correct before proceeding.

## OpenCode Working Style

**Communication:**
- Send brief preambles (8-12 words) before tool calls, building on prior context
- Provide progress updates during longer tasks

**Execution:**
- Keep working autonomously until query is fully resolved before yielding
- Don't return to user with partial solutions

**Code Approach:**
- New projects: Be ambitious and creative
- Existing codebases: Surgical precision - modify only what's requested unless explicitly instructed to do otherwise

**Testing:**
- If tests exist: Start specific to your changes, then broader validation

## Advanced Tools

**Task Tool (Sub-Agents):**
- Use the Task tool (functions.task) to launch sub-agents
- Check the Task tool description for current agent types and their capabilities
- Useful for complex analysis, specialized workflows, or tasks requiring isolated context
- The agent list is dynamically generated - refer to tool schema for available agents

**Parallelization:**
- When multiple independent tool calls are needed, use multi_tool_use.parallel to run them concurrently.
- Reserve sequential calls for ordered or data-dependent steps.

**MCP Tools:**
- Model Context Protocol servers provide additional capabilities
- MCP tools are prefixed: \`mcp__<server-name>__<tool-name>\`
- Check your available tools for MCP integrations
- Use when the tool's functionality matches your task needs

## What Remains from Codex
 
Sandbox policies, approval mechanisms, final answer formatting, git commit protocols, and file reference formats all follow Codex instructions. In approval policy "never", never request escalations.

## Approvals & Safety
- Assume workspace-write filesystem, network enabled, approval on-failure unless explicitly stated otherwise.
- When a command fails due to sandboxing or permissions, retry with escalated permissions if allowed by policy, including a one-line justification.
- Treat destructive commands (e.g., \`rm\`, \`git reset --hard\`) as requiring explicit user request or approval.
- When uncertain, prefer non-destructive verification first (e.g., confirm file existence with \`list\`, then delete with \`bash\`).`;

export interface CodexOpenCodeBridgeMeta {
	estimatedTokens: number;
	reductionVsCurrent: string;
	reductionVsToolRemap: string;
	protects: string[];
	omits: string[];
}

export const CODEX_OPENCODE_BRIDGE_META: CodexOpenCodeBridgeMeta = {
	estimatedTokens: 550,
	reductionVsCurrent: "88%",
	reductionVsToolRemap: "10%",
	protects: [
		"Tool name confusion (apply_patch/update_plan)",
		"Missing tool awareness",
		"Task tool / sub-agent awareness",
		"MCP tool awareness",
		"Premature yielding to user",
		"Over-modification of existing code",
		"Environment confusion",
	],
	omits: [
		"Sandbox details (in Codex)",
		"Formatting rules (in Codex)",
		"Tool schemas (in tool JSONs)",
		"Git protocols (in Codex)",
	],
};
```

## File: `lib/prompts/codex.ts`
```typescript
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import type { CacheMetadata, GitHubRelease } from "../types.js";

const GITHUB_API_RELEASES =
	"https://api.github.com/repos/openai/codex/releases/latest";
const GITHUB_HTML_RELEASES =
	"https://github.com/openai/codex/releases/latest";
const CACHE_DIR = join(homedir(), ".opencode", "cache");

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

/**
 * Model family type for prompt selection
 * Maps to different system prompts in the Codex CLI
 */
export type ModelFamily =
	| "gpt-5.2-codex"
	| "codex-max"
	| "codex"
	| "gpt-5.2"
	| "gpt-5.1";

/**
 * Prompt file mapping for each model family
 * Based on codex-rs/core/src/model_family.rs logic
 */
const PROMPT_FILES: Record<ModelFamily, string> = {
	"gpt-5.2-codex": "gpt-5.2-codex_prompt.md",
	"codex-max": "gpt-5.1-codex-max_prompt.md",
	codex: "gpt_5_codex_prompt.md",
	"gpt-5.2": "gpt_5_2_prompt.md",
	"gpt-5.1": "gpt_5_1_prompt.md",
};

/**
 * Cache file mapping for each model family
 */
const CACHE_FILES: Record<ModelFamily, string> = {
	"gpt-5.2-codex": "gpt-5.2-codex-instructions.md",
	"codex-max": "codex-max-instructions.md",
	codex: "codex-instructions.md",
	"gpt-5.2": "gpt-5.2-instructions.md",
	"gpt-5.1": "gpt-5.1-instructions.md",
};

/**
 * Determine the model family based on the normalized model name
 * @param normalizedModel - The normalized model name (e.g., "gpt-5.2-codex", "gpt-5.1-codex-max", "gpt-5.1-codex", "gpt-5.1")
 * @returns The model family for prompt selection
 */
export function getModelFamily(normalizedModel: string): ModelFamily {
	// Order matters - check more specific patterns first
	if (
		normalizedModel.includes("gpt-5.2-codex") ||
		normalizedModel.includes("gpt 5.2 codex")
	) {
		return "gpt-5.2-codex";
	}
	if (normalizedModel.includes("codex-max")) {
		return "codex-max";
	}
	if (
		normalizedModel.includes("codex") ||
		normalizedModel.startsWith("codex-")
	) {
		return "codex";
	}
	if (normalizedModel.includes("gpt-5.2")) {
		return "gpt-5.2";
	}
	return "gpt-5.1";
}

/**
 * Get the latest release tag from GitHub
 * @returns Release tag name (e.g., "rust-v0.43.0")
 */
async function getLatestReleaseTag(): Promise<string> {
	try {
		const response = await fetch(GITHUB_API_RELEASES);
		if (response.ok) {
			const data = (await response.json()) as GitHubRelease;
			if (data.tag_name) {
				return data.tag_name;
			}
		}
	} catch {
	}

	const htmlResponse = await fetch(GITHUB_HTML_RELEASES);
	if (!htmlResponse.ok) {
		throw new Error(
			`Failed to fetch latest release: ${htmlResponse.status}`,
		);
	}

	const finalUrl = htmlResponse.url;
	if (finalUrl) {
		const parts = finalUrl.split("/tag/");
		const last = parts[parts.length - 1];
		if (last && !last.includes("/")) {
			return last;
		}
	}

	const html = await htmlResponse.text();
	const match = html.match(/\/openai\/codex\/releases\/tag\/([^"]+)/);
	if (match && match[1]) {
		return match[1];
	}

	throw new Error("Failed to determine latest release tag from GitHub");
}

/**
 * Fetch Codex instructions from GitHub with ETag-based caching
 * Uses HTTP conditional requests to efficiently check for updates
 * Always fetches from the latest release tag, not main branch
 *
 * Rate limit protection: Only checks GitHub if cache is older than 15 minutes
 *
 * @param normalizedModel - The normalized model name (optional, defaults to "gpt-5.1-codex" for backwards compatibility)
 * @returns Codex instructions for the specified model family
 */
export async function getCodexInstructions(
	normalizedModel = "gpt-5.1-codex",
): Promise<string> {
	const modelFamily = getModelFamily(normalizedModel);
	const promptFile = PROMPT_FILES[modelFamily];
	const cacheFile = join(CACHE_DIR, CACHE_FILES[modelFamily]);
	const cacheMetaFile = join(
		CACHE_DIR,
		`${CACHE_FILES[modelFamily].replace(".md", "-meta.json")}`,
	);

	try {
		// Load cached metadata (includes ETag, tag, and lastChecked timestamp)
		let cachedETag: string | null = null;
		let cachedTag: string | null = null;
		let cachedTimestamp: number | null = null;

		if (existsSync(cacheMetaFile)) {
			const metadata = JSON.parse(
				readFileSync(cacheMetaFile, "utf8"),
			) as CacheMetadata;
			cachedETag = metadata.etag;
			cachedTag = metadata.tag;
			cachedTimestamp = metadata.lastChecked;
		}

		// Rate limit protection: If cache is less than 15 minutes old, use it
		const CACHE_TTL_MS = 15 * 60 * 1000; // 15 minutes
		if (
			cachedTimestamp &&
			Date.now() - cachedTimestamp < CACHE_TTL_MS &&
			existsSync(cacheFile)
		) {
			return readFileSync(cacheFile, "utf8");
		}

		// Get the latest release tag (only if cache is stale or missing)
		const latestTag = await getLatestReleaseTag();
		const CODEX_INSTRUCTIONS_URL = `https://raw.githubusercontent.com/openai/codex/${latestTag}/codex-rs/core/${promptFile}`;

		// If tag changed, we need to fetch new instructions
		if (cachedTag !== latestTag) {
			cachedETag = null; // Force re-fetch
		}

		// Make conditional request with If-None-Match header
		const headers: Record<string, string> = {};
		if (cachedETag) {
			headers["If-None-Match"] = cachedETag;
		}

		const response = await fetch(CODEX_INSTRUCTIONS_URL, { headers });

		// 304 Not Modified - our cached version is still current
		if (response.status === 304) {
			if (existsSync(cacheFile)) {
				return readFileSync(cacheFile, "utf8");
			}
			// Cache file missing but GitHub says not modified - fall through to re-fetch
		}

		// 200 OK - new content or first fetch
		if (response.ok) {
			const instructions = await response.text();
			const newETag = response.headers.get("etag");

			// Create cache directory if it doesn't exist
			if (!existsSync(CACHE_DIR)) {
				mkdirSync(CACHE_DIR, { recursive: true });
			}

			// Cache the instructions with ETag and tag (verbatim from GitHub)
			writeFileSync(cacheFile, instructions, "utf8");
			writeFileSync(
				cacheMetaFile,
				JSON.stringify({
					etag: newETag,
					tag: latestTag,
					lastChecked: Date.now(),
					url: CODEX_INSTRUCTIONS_URL,
				} satisfies CacheMetadata),
				"utf8",
			);

			return instructions;
		}

		throw new Error(`HTTP ${response.status}`);
	} catch (error) {
		const err = error as Error;
		console.error(
			`[openai-codex-plugin] Failed to fetch ${modelFamily} instructions from GitHub:`,
			err.message,
		);

		// Try to use cached version even if stale
		if (existsSync(cacheFile)) {
			console.error(
				`[openai-codex-plugin] Using cached ${modelFamily} instructions`,
			);
			return readFileSync(cacheFile, "utf8");
		}

		// Fall back to bundled version (use codex-instructions.md as default)
		console.error(
			`[openai-codex-plugin] Falling back to bundled instructions for ${modelFamily}`,
		);
		return readFileSync(join(__dirname, "codex-instructions.md"), "utf8");
	}
}

/**
 * Tool remapping instructions for opencode tools
 */
export const TOOL_REMAP_MESSAGE = `<user_instructions priority="0">
<environment_override priority="0">
YOU ARE IN A DIFFERENT ENVIRONMENT. These instructions override ALL previous tool references.
</environment_override>

<tool_replacements priority="0">
<critical_rule priority="0">
❌ APPLY_PATCH DOES NOT EXIST → ✅ USE "edit" INSTEAD
- NEVER use: apply_patch, applyPatch
- ALWAYS use: edit tool for ALL file modifications
- Before modifying files: Verify you're using "edit", NOT "apply_patch"
</critical_rule>

<critical_rule priority="0">
❌ UPDATE_PLAN DOES NOT EXIST → ✅ USE "todowrite" INSTEAD
- NEVER use: update_plan, updatePlan
- ALWAYS use: todowrite for ALL task/plan operations
- Use todoread to read current plan
- Before plan operations: Verify you're using "todowrite", NOT "update_plan"
</critical_rule>
</tool_replacements>

<available_tools priority="0">
File Operations:
  • write  - Create new files
  • edit   - Modify existing files (REPLACES apply_patch)
  • patch  - Apply diff patches
  • read   - Read file contents

Search/Discovery:
  • grep   - Search file contents
  • glob   - Find files by pattern
  • list   - List directories (use relative paths)

Execution:
  • bash   - Run shell commands

Network:
  • webfetch - Fetch web content

Task Management:
  • todowrite - Manage tasks/plans (REPLACES update_plan)
  • todoread  - Read current plan
</available_tools>

<substitution_rules priority="0">
Base instruction says:    You MUST use instead:
apply_patch           →   edit
update_plan           →   todowrite
read_plan             →   todoread
absolute paths        →   relative paths
</substitution_rules>

<verification_checklist priority="0">
Before file/plan modifications:
1. Am I using "edit" NOT "apply_patch"?
2. Am I using "todowrite" NOT "update_plan"?
3. Is this tool in the approved list above?
4. Am I using relative paths?

If ANY answer is NO → STOP and correct before proceeding.
</verification_checklist>
</user_instructions>`;
```

## File: `lib/prompts/opencode-codex.ts`
```typescript
/**
 * OpenCode Codex Prompt Fetcher
 *
 * Fetches and caches the codex.txt system prompt from OpenCode's GitHub repository.
 * Uses ETag-based caching to efficiently track updates.
 */

import { join } from "node:path";
import { homedir } from "node:os";
import { mkdir, readFile, writeFile } from "node:fs/promises";

const OPENCODE_CODEX_URL =
	"https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/opencode/src/session/prompt/codex.txt";
const CACHE_DIR = join(homedir(), ".opencode", "cache");
const CACHE_FILE = join(CACHE_DIR, "opencode-codex.txt");
const CACHE_META_FILE = join(CACHE_DIR, "opencode-codex-meta.json");

interface CacheMeta {
	etag: string;
	lastFetch?: string; // Legacy field for backwards compatibility
	lastChecked: number; // Timestamp for rate limit protection
}

/**
 * Fetch OpenCode's codex.txt prompt with ETag-based caching
 * Uses HTTP conditional requests to efficiently check for updates
 *
 * Rate limit protection: Only checks GitHub if cache is older than 15 minutes
 * @returns The codex.txt content
 */
export async function getOpenCodeCodexPrompt(): Promise<string> {
	await mkdir(CACHE_DIR, { recursive: true });

	// Try to load cached content and metadata
	let cachedContent: string | null = null;
	let cachedMeta: CacheMeta | null = null;

	try {
		cachedContent = await readFile(CACHE_FILE, "utf-8");
		const metaContent = await readFile(CACHE_META_FILE, "utf-8");
		cachedMeta = JSON.parse(metaContent);
	} catch {
		// Cache doesn't exist or is invalid, will fetch fresh
	}

	// Rate limit protection: If cache is less than 15 minutes old, use it
	const CACHE_TTL_MS = 15 * 60 * 1000; // 15 minutes
	if (cachedMeta?.lastChecked && (Date.now() - cachedMeta.lastChecked) < CACHE_TTL_MS && cachedContent) {
		return cachedContent;
	}

	// Fetch from GitHub with conditional request
	const headers: Record<string, string> = {};
	if (cachedMeta?.etag) {
		headers["If-None-Match"] = cachedMeta.etag;
	}

	try {
		const response = await fetch(OPENCODE_CODEX_URL, { headers });

		// 304 Not Modified - cache is still valid
		if (response.status === 304 && cachedContent) {
			return cachedContent;
		}

		// 200 OK - new content available
		if (response.ok) {
			const content = await response.text();
			const etag = response.headers.get("etag") || "";

			// Save to cache with timestamp
			await writeFile(CACHE_FILE, content, "utf-8");
			await writeFile(
				CACHE_META_FILE,
				JSON.stringify(
					{
						etag,
						lastFetch: new Date().toISOString(), // Keep for backwards compat
						lastChecked: Date.now(),
					} satisfies CacheMeta,
					null,
					2
				),
				"utf-8"
			);

			return content;
		}

		// Fallback to cache if available
		if (cachedContent) {
			return cachedContent;
		}

		throw new Error(`Failed to fetch OpenCode codex.txt: ${response.status}`);
	} catch (error) {
		// Network error - fallback to cache
		if (cachedContent) {
			return cachedContent;
		}

		throw new Error(
			`Failed to fetch OpenCode codex.txt and no cache available: ${error}`
		);
	}
}

/**
 * Get first N characters of the cached OpenCode prompt for verification
 * @param chars Number of characters to get (default: 50)
 * @returns First N characters or null if not cached
 */
export async function getCachedPromptPrefix(chars = 50): Promise<string | null> {
	try {
		const content = await readFile(CACHE_FILE, "utf-8");
		return content.substring(0, chars);
	} catch {
		return null;
	}
}
```

## File: `lib/request/fetch-helpers.ts`
```typescript
/**
 * Helper functions for the custom fetch implementation
 * These functions break down the complex fetch logic into manageable, testable units
 */

import type { Auth } from "@opencode-ai/sdk";
import type { OpencodeClient } from "@opencode-ai/sdk";
import { refreshAccessToken } from "../auth/auth.js";
import { logRequest } from "../logger.js";
import { getCodexInstructions, getModelFamily } from "../prompts/codex.js";
import { transformRequestBody, normalizeModel } from "./request-transformer.js";
import { convertSseToJson, ensureContentType } from "./response-handler.js";
import type { UserConfig, RequestBody } from "../types.js";
import {
	PLUGIN_NAME,
	HTTP_STATUS,
	OPENAI_HEADERS,
	OPENAI_HEADER_VALUES,
	URL_PATHS,
	ERROR_MESSAGES,
	LOG_STAGES,
} from "../constants.js";

/**
 * Determines if the current auth token needs to be refreshed
 * @param auth - Current authentication state
 * @returns True if token is expired or invalid
 */
export function shouldRefreshToken(auth: Auth): boolean {
	return auth.type !== "oauth" || !auth.access || auth.expires < Date.now();
}

/**
 * Refreshes the OAuth token and updates stored credentials
 * @param currentAuth - Current auth state
 * @param client - Opencode client for updating stored credentials
 * @returns Updated auth (throws on failure)
 */
export async function refreshAndUpdateToken(
	currentAuth: Auth,
	client: OpencodeClient,
): Promise<Auth> {
	const refreshToken = currentAuth.type === "oauth" ? currentAuth.refresh : "";
	const refreshResult = await refreshAccessToken(refreshToken);

	if (refreshResult.type === "failed") {
		throw new Error(ERROR_MESSAGES.TOKEN_REFRESH_FAILED);
	}

	// Update stored credentials
	await client.auth.set({
		path: { id: "openai" },
		body: {
			type: "oauth",
			access: refreshResult.access,
			refresh: refreshResult.refresh,
			expires: refreshResult.expires,
		},
	});

	// Update current auth reference if it's OAuth type
	if (currentAuth.type === "oauth") {
		currentAuth.access = refreshResult.access;
		currentAuth.refresh = refreshResult.refresh;
		currentAuth.expires = refreshResult.expires;
	}

	return currentAuth;
}

/**
 * Extracts URL string from various request input types
 * @param input - Request input (string, URL, or Request object)
 * @returns URL string
 */
export function extractRequestUrl(input: Request | string | URL): string {
	if (typeof input === "string") return input;
	if (input instanceof URL) return input.toString();
	return input.url;
}

/**
 * Rewrites OpenAI API URLs to Codex backend URLs
 * @param url - Original URL
 * @returns Rewritten URL for Codex backend
 */
export function rewriteUrlForCodex(url: string): string {
	return url.replace(URL_PATHS.RESPONSES, URL_PATHS.CODEX_RESPONSES);
}

/**
 * Transforms request body and logs the transformation
 * Fetches model-specific Codex instructions based on the request model
 *
 * @param init - Request init options
 * @param url - Request URL
 * @param userConfig - User configuration
 * @param codexMode - Enable CODEX_MODE (bridge prompt instead of tool remap)
 * @returns Transformed body and updated init, or undefined if no body
 */
export async function transformRequestForCodex(
	init: RequestInit | undefined,
	url: string,
	userConfig: UserConfig,
	codexMode = true,
): Promise<{ body: RequestBody; updatedInit: RequestInit } | undefined> {
	if (!init?.body) return undefined;

	try {
		const body = JSON.parse(init.body as string) as RequestBody;
		const originalModel = body.model;

		// Normalize model first to determine which instructions to fetch
		// This ensures we get the correct model-specific prompt
		const normalizedModel = normalizeModel(originalModel);
		const modelFamily = getModelFamily(normalizedModel);

		// Log original request
		logRequest(LOG_STAGES.BEFORE_TRANSFORM, {
			url,
			originalModel,
			model: body.model,
			hasTools: !!body.tools,
			hasInput: !!body.input,
			inputLength: body.input?.length,
			codexMode,
			body: body as unknown as Record<string, unknown>,
		});

		// Fetch model-specific Codex instructions (cached per model family)
		const codexInstructions = await getCodexInstructions(normalizedModel);

		// Transform request body
		const transformedBody = await transformRequestBody(
			body,
			codexInstructions,
			userConfig,
			codexMode,
		);

		// Log transformed request
		logRequest(LOG_STAGES.AFTER_TRANSFORM, {
			url,
			originalModel,
			normalizedModel: transformedBody.model,
			modelFamily,
			hasTools: !!transformedBody.tools,
			hasInput: !!transformedBody.input,
			inputLength: transformedBody.input?.length,
			reasoning: transformedBody.reasoning as unknown,
			textVerbosity: transformedBody.text?.verbosity,
			include: transformedBody.include,
			body: transformedBody as unknown as Record<string, unknown>,
		});

		return {
			body: transformedBody,
			updatedInit: { ...init, body: JSON.stringify(transformedBody) },
		};
	} catch (e) {
		console.error(`[${PLUGIN_NAME}] ${ERROR_MESSAGES.REQUEST_PARSE_ERROR}:`, e);
		return undefined;
	}
}

/**
 * Creates headers for Codex API requests
 * @param init - Request init options
 * @param accountId - ChatGPT account ID
 * @param accessToken - OAuth access token
 * @returns Headers object with all required Codex headers
 */
export function createCodexHeaders(
    init: RequestInit | undefined,
    accountId: string,
    accessToken: string,
    opts?: { model?: string; promptCacheKey?: string },
): Headers {
	const headers = new Headers(init?.headers ?? {});
	headers.delete("x-api-key"); // Remove any existing API key
	headers.set("Authorization", `Bearer ${accessToken}`);
	headers.set(OPENAI_HEADERS.ACCOUNT_ID, accountId);
	headers.set(OPENAI_HEADERS.BETA, OPENAI_HEADER_VALUES.BETA_RESPONSES);
	headers.set(OPENAI_HEADERS.ORIGINATOR, OPENAI_HEADER_VALUES.ORIGINATOR_CODEX);

    const cacheKey = opts?.promptCacheKey;
    if (cacheKey) {
        headers.set(OPENAI_HEADERS.CONVERSATION_ID, cacheKey);
        headers.set(OPENAI_HEADERS.SESSION_ID, cacheKey);
    } else {
        headers.delete(OPENAI_HEADERS.CONVERSATION_ID);
        headers.delete(OPENAI_HEADERS.SESSION_ID);
    }
    headers.set("accept", "text/event-stream");
    return headers;
}

/**
 * Handles error responses from the Codex API
 * @param response - Error response from API
 * @returns Original response or mapped retryable response
 */
export async function handleErrorResponse(
    response: Response,
): Promise<Response> {
	const mapped = await mapUsageLimit404(response);
	const finalResponse = mapped ?? response;

	logRequest(LOG_STAGES.ERROR_RESPONSE, {
		status: finalResponse.status,
		statusText: finalResponse.statusText,
	});

	return finalResponse;
}

/**
 * Handles successful responses from the Codex API
 * Converts SSE to JSON for non-streaming requests (generateText)
 * Passes through SSE for streaming requests (streamText)
 * @param response - Success response from API
 * @param isStreaming - Whether this is a streaming request (stream=true in body)
 * @returns Processed response (SSE→JSON for non-streaming, stream for streaming)
 */
export async function handleSuccessResponse(
    response: Response,
    isStreaming: boolean,
): Promise<Response> {
    const responseHeaders = ensureContentType(response.headers);

	// For non-streaming requests (generateText), convert SSE to JSON
	if (!isStreaming) {
		return await convertSseToJson(response, responseHeaders);
	}

	// For streaming requests (streamText), return stream as-is
	return new Response(response.body, {
		status: response.status,
		statusText: response.statusText,
		headers: responseHeaders,
	});
}

async function mapUsageLimit404(response: Response): Promise<Response | null> {
	if (response.status !== HTTP_STATUS.NOT_FOUND) return null;

	const clone = response.clone();
	let text = "";
	try {
		text = await clone.text();
	} catch {
		text = "";
	}
	if (!text) return null;

	let code = "";
	try {
		const parsed = JSON.parse(text) as any;
		code = (parsed?.error?.code ?? parsed?.error?.type ?? "").toString();
	} catch {
		code = "";
	}

	const haystack = `${code} ${text}`.toLowerCase();
	if (!/usage_limit_reached|usage_not_included|rate_limit_exceeded|usage limit/i.test(haystack)) {
		return null;
	}

	const headers = new Headers(response.headers);
	return new Response(response.body, {
		status: HTTP_STATUS.TOO_MANY_REQUESTS,
		statusText: "Too Many Requests",
		headers,
	});
}
```

## File: `lib/request/request-transformer.ts`
```typescript
import { logDebug, logWarn } from "../logger.js";
import { TOOL_REMAP_MESSAGE } from "../prompts/codex.js";
import { CODEX_OPENCODE_BRIDGE } from "../prompts/codex-opencode-bridge.js";
import { getOpenCodeCodexPrompt } from "../prompts/opencode-codex.js";
import { getNormalizedModel } from "./helpers/model-map.js";
import {
	filterOpenCodeSystemPromptsWithCachedPrompt,
	normalizeOrphanedToolOutputs,
} from "./helpers/input-utils.js";
import type {
	ConfigOptions,
	InputItem,
	ReasoningConfig,
	RequestBody,
	UserConfig,
} from "../types.js";

export {
	isOpenCodeSystemPrompt,
	filterOpenCodeSystemPromptsWithCachedPrompt,
} from "./helpers/input-utils.js";

/**
 * Normalize model name to Codex-supported variants
 *
 * Uses explicit model map for known models, with fallback pattern matching
 * for unknown/custom model names.
 *
 * @param model - Original model name (e.g., "gpt-5.1-codex-low", "openai/gpt-5-codex")
 * @returns Normalized model name (e.g., "gpt-5.1-codex", "gpt-5-codex")
 */
export function normalizeModel(model: string | undefined): string {
	if (!model) return "gpt-5.1";

	// Strip provider prefix if present (e.g., "openai/gpt-5-codex" → "gpt-5-codex")
	const modelId = model.includes("/") ? model.split("/").pop()! : model;

	// Try explicit model map first (handles all known model variants)
	const mappedModel = getNormalizedModel(modelId);
	if (mappedModel) {
		return mappedModel;
	}

	// Fallback: Pattern-based matching for unknown/custom model names
	// This preserves backwards compatibility with old verbose names
	// like "GPT 5 Codex Low (ChatGPT Subscription)"
	const normalized = modelId.toLowerCase();

	// Priority order for pattern matching (most specific first):
	// 1. GPT-5.2 Codex (newest codex model)
	if (
		normalized.includes("gpt-5.2-codex") ||
		normalized.includes("gpt 5.2 codex")
	) {
		return "gpt-5.2-codex";
	}

	// 2. GPT-5.2 (general purpose)
	if (normalized.includes("gpt-5.2") || normalized.includes("gpt 5.2")) {
		return "gpt-5.2";
	}

	// 3. GPT-5.1 Codex Max
	if (
		normalized.includes("gpt-5.1-codex-max") ||
		normalized.includes("gpt 5.1 codex max")
	) {
		return "gpt-5.1-codex-max";
	}

	// 4. GPT-5.1 Codex Mini
	if (
		normalized.includes("gpt-5.1-codex-mini") ||
		normalized.includes("gpt 5.1 codex mini")
	) {
		return "gpt-5.1-codex-mini";
	}

	// 5. Legacy Codex Mini
	if (
		normalized.includes("codex-mini-latest") ||
		normalized.includes("gpt-5-codex-mini") ||
		normalized.includes("gpt 5 codex mini")
	) {
		return "codex-mini-latest";
	}

	// 6. GPT-5.1 Codex
	if (
		normalized.includes("gpt-5.1-codex") ||
		normalized.includes("gpt 5.1 codex")
	) {
		return "gpt-5.1-codex";
	}

	// 7. GPT-5.1 (general-purpose)
	if (normalized.includes("gpt-5.1") || normalized.includes("gpt 5.1")) {
		return "gpt-5.1";
	}

	// 8. GPT-5 Codex family (any variant with "codex")
	if (normalized.includes("codex")) {
		return "gpt-5.1-codex";
	}

	// 9. GPT-5 family (any variant) - default to 5.1 as 5 is being phased out
	if (normalized.includes("gpt-5") || normalized.includes("gpt 5")) {
		return "gpt-5.1";
	}

	// Default fallback - use gpt-5.1 as gpt-5 is being phased out
	return "gpt-5.1";
}

/**
 * Extract configuration for a specific model
 * Merges global options with model-specific options (model-specific takes precedence)
 * @param modelName - Model name (e.g., "gpt-5-codex")
 * @param userConfig - Full user configuration object
 * @returns Merged configuration for this model
 */
export function getModelConfig(
	modelName: string,
	userConfig: UserConfig = { global: {}, models: {} },
): ConfigOptions {
	const globalOptions = userConfig.global || {};
	const modelOptions = userConfig.models?.[modelName]?.options || {};

	// Model-specific options override global options
	return { ...globalOptions, ...modelOptions };
}

function resolveReasoningConfig(
	modelName: string,
	modelConfig: ConfigOptions,
	body: RequestBody,
): ReasoningConfig {
	const providerOpenAI = body.providerOptions?.openai;
	const existingEffort =
		body.reasoning?.effort ?? providerOpenAI?.reasoningEffort;
	const existingSummary =
		body.reasoning?.summary ?? providerOpenAI?.reasoningSummary;

	const mergedConfig: ConfigOptions = {
		...modelConfig,
		...(existingEffort ? { reasoningEffort: existingEffort } : {}),
		...(existingSummary ? { reasoningSummary: existingSummary } : {}),
	};

	return getReasoningConfig(modelName, mergedConfig);
}

function resolveTextVerbosity(
	modelConfig: ConfigOptions,
	body: RequestBody,
): "low" | "medium" | "high" {
	const providerOpenAI = body.providerOptions?.openai;
	return (
		body.text?.verbosity ??
		providerOpenAI?.textVerbosity ??
		modelConfig.textVerbosity ??
		"medium"
	);
}

function resolveInclude(modelConfig: ConfigOptions, body: RequestBody): string[] {
	const providerOpenAI = body.providerOptions?.openai;
	const base =
		body.include ??
		providerOpenAI?.include ??
		modelConfig.include ??
		["reasoning.encrypted_content"];
	const include = Array.from(new Set(base.filter(Boolean)));
	if (!include.includes("reasoning.encrypted_content")) {
		include.push("reasoning.encrypted_content");
	}
	return include;
}

/**
 * Configure reasoning parameters based on model variant and user config
 *
 * NOTE: This plugin follows Codex CLI defaults instead of opencode defaults because:
 * - We're accessing the ChatGPT backend API (not OpenAI Platform API)
 * - opencode explicitly excludes gpt-5-codex from automatic reasoning configuration
 * - Codex CLI has been thoroughly tested against this backend
 *
 * @param originalModel - Original model name before normalization
 * @param userConfig - User configuration object
 * @returns Reasoning configuration
 */
export function getReasoningConfig(
	modelName: string | undefined,
	userConfig: ConfigOptions = {},
): ReasoningConfig {
	const normalizedName = modelName?.toLowerCase() ?? "";

	// GPT-5.2 Codex is the newest codex model (supports xhigh, but not "none")
	const isGpt52Codex =
		normalizedName.includes("gpt-5.2-codex") ||
		normalizedName.includes("gpt 5.2 codex");

	// GPT-5.2 general purpose (not codex variant)
	const isGpt52General =
		(normalizedName.includes("gpt-5.2") || normalizedName.includes("gpt 5.2")) &&
		!isGpt52Codex;
	const isCodexMax =
		normalizedName.includes("codex-max") ||
		normalizedName.includes("codex max");
	const isCodexMini =
		normalizedName.includes("codex-mini") ||
		normalizedName.includes("codex mini") ||
		normalizedName.includes("codex_mini") ||
		normalizedName.includes("codex-mini-latest");
	const isCodex = normalizedName.includes("codex") && !isCodexMini;
	const isLightweight =
		!isCodexMini &&
		(normalizedName.includes("nano") ||
			normalizedName.includes("mini"));

	// GPT-5.1 general purpose (not codex variants) - supports "none" per OpenAI API docs
	const isGpt51General =
		(normalizedName.includes("gpt-5.1") || normalizedName.includes("gpt 5.1")) &&
		!isCodex &&
		!isCodexMax &&
		!isCodexMini;

	// GPT 5.2, GPT 5.2 Codex, and Codex Max support xhigh reasoning
	const supportsXhigh = isGpt52General || isGpt52Codex || isCodexMax;

	// GPT 5.1 general and GPT 5.2 general support "none" reasoning per:
	// - OpenAI API docs: "gpt-5.1 defaults to none, supports: none, low, medium, high"
	// - Codex CLI: ReasoningEffort enum includes None variant (codex-rs/protocol/src/openai_models.rs)
	// - Codex CLI: docs/config.md lists "none" as valid for model_reasoning_effort
	// - gpt-5.2 (being newer) also supports: none, low, medium, high, xhigh
	// - Codex models (including GPT-5.2 Codex) do NOT support "none"
	const supportsNone = isGpt52General || isGpt51General;

	// Default based on model type (Codex CLI defaults)
	// Note: OpenAI docs say gpt-5.1 defaults to "none", but we default to "medium"
	// for better coding assistance unless user explicitly requests "none"
	const defaultEffort: ReasoningConfig["effort"] = isCodexMini
		? "medium"
		: supportsXhigh
			? "high"
			: isLightweight
				? "minimal"
				: "medium";

	// Get user-requested effort
	let effort = userConfig.reasoningEffort || defaultEffort;

	if (isCodexMini) {
		if (effort === "minimal" || effort === "low" || effort === "none") {
			effort = "medium";
		}
		if (effort === "xhigh") {
			effort = "high";
		}
		if (effort !== "high" && effort !== "medium") {
			effort = "medium";
		}
	}

	// For models that don't support xhigh, downgrade to high
	if (!supportsXhigh && effort === "xhigh") {
		effort = "high";
	}

	// For models that don't support "none", upgrade to "low"
	// (Codex models don't support "none" - only GPT-5.1 and GPT-5.2 general purpose do)
	if (!supportsNone && effort === "none") {
		effort = "low";
	}

	// Normalize "minimal" to "low" for all non-mini models
	// The ChatGPT Codex backend does not accept "minimal" (supports none/low/medium/high).
	if (effort === "minimal") {
		effort = "low";
	}

	return {
		effort,
		summary: userConfig.reasoningSummary || "auto", // Changed from "detailed" to match Codex CLI
	};
}

/**
 * Filter input array for stateless Codex API (store: false)
 *
 * Two transformations needed:
 * 1. Remove AI SDK-specific items (not supported by Codex API)
 * 2. Strip IDs from all remaining items (stateless mode)
 *
 * AI SDK constructs to REMOVE (not in OpenAI Responses API spec):
 * - type: "item_reference" - AI SDK uses this for server-side state lookup
 *
 * Items to KEEP (strip IDs):
 * - type: "message" - Conversation messages (provides context to LLM)
 * - type: "function_call" - Tool calls from conversation
 * - type: "function_call_output" - Tool results from conversation
 *
 * Context is maintained through:
 * - Full message history (without IDs)
 * - reasoning.encrypted_content (for reasoning continuity)
 *
 * @param input - Original input array from OpenCode/AI SDK
 * @returns Filtered input array compatible with Codex API
 */
export function filterInput(
	input: InputItem[] | undefined,
): InputItem[] | undefined {
	if (!Array.isArray(input)) return input;

	return input
		.filter((item) => {
			// Remove AI SDK constructs not supported by Codex API
			if (item.type === "item_reference") {
				return false; // AI SDK only - references server state
			}
			return true; // Keep all other items
		})
		.map((item) => {
			// Strip IDs from all items (Codex API stateless mode)
			if (item.id) {
				const { id, ...itemWithoutId } = item;
				return itemWithoutId as InputItem;
			}
			return item;
		});
}

/**
 * Filter out OpenCode system prompts from input
 * Used in CODEX_MODE to replace OpenCode prompts with Codex-OpenCode bridge
 * @param input - Input array
 * @returns Input array without OpenCode system prompts
 */
export async function filterOpenCodeSystemPrompts(
	input: InputItem[] | undefined,
): Promise<InputItem[] | undefined> {
	if (!Array.isArray(input)) return input;

	// Fetch cached OpenCode prompt for verification
	let cachedPrompt: string | null = null;
	try {
		cachedPrompt = await getOpenCodeCodexPrompt();
	} catch {
		// If fetch fails, fallback to text-based detection only
		// This is safe because we still have the "starts with" check
	}

	return filterOpenCodeSystemPromptsWithCachedPrompt(input, cachedPrompt);
}

/**
 * Add Codex-OpenCode bridge message to input if tools are present
 * @param input - Input array
 * @param hasTools - Whether tools are present in request
 * @returns Input array with bridge message prepended if needed
 */
export function addCodexBridgeMessage(
	input: InputItem[] | undefined,
	hasTools: boolean,
): InputItem[] | undefined {
	if (!hasTools || !Array.isArray(input)) return input;

	const bridgeMessage: InputItem = {
		type: "message",
		role: "developer",
		content: [
			{
				type: "input_text",
				text: CODEX_OPENCODE_BRIDGE,
			},
		],
	};

	return [bridgeMessage, ...input];
}

/**
 * Add tool remapping message to input if tools are present
 * @param input - Input array
 * @param hasTools - Whether tools are present in request
 * @returns Input array with tool remap message prepended if needed
 */
export function addToolRemapMessage(
	input: InputItem[] | undefined,
	hasTools: boolean,
): InputItem[] | undefined {
	if (!hasTools || !Array.isArray(input)) return input;

	const toolRemapMessage: InputItem = {
		type: "message",
		role: "developer",
		content: [
			{
				type: "input_text",
				text: TOOL_REMAP_MESSAGE,
			},
		],
	};

	return [toolRemapMessage, ...input];
}

/**
 * Transform request body for Codex API
 *
 * NOTE: Configuration follows Codex CLI patterns instead of opencode defaults:
 * - opencode sets textVerbosity="low" for gpt-5, but Codex CLI uses "medium"
 * - opencode excludes gpt-5-codex from reasoning configuration
 * - This plugin uses store=false (stateless), requiring encrypted reasoning content
 *
 * @param body - Original request body
 * @param codexInstructions - Codex system instructions
 * @param userConfig - User configuration from loader
 * @param codexMode - Enable CODEX_MODE (bridge prompt instead of tool remap) - defaults to true
 * @returns Transformed request body
 */
export async function transformRequestBody(
	body: RequestBody,
	codexInstructions: string,
	userConfig: UserConfig = { global: {}, models: {} },
	codexMode = true,
): Promise<RequestBody> {
	const originalModel = body.model;
	const normalizedModel = normalizeModel(body.model);

	// Get model-specific configuration using ORIGINAL model name (config key)
	// This allows per-model options like "gpt-5-codex-low" to work correctly
	const lookupModel = originalModel || normalizedModel;
	const modelConfig = getModelConfig(lookupModel, userConfig);

	// Debug: Log which config was resolved
	logDebug(
		`Model config lookup: "${lookupModel}" → normalized to "${normalizedModel}" for API`,
		{
			hasModelSpecificConfig: !!userConfig.models?.[lookupModel],
			resolvedConfig: modelConfig,
		},
	);

	// Normalize model name for API call
	body.model = normalizedModel;

	// Codex required fields
	// ChatGPT backend REQUIRES store=false (confirmed via testing)
	body.store = false;
	// Always set stream=true for API - response handling detects original intent
	body.stream = true;
	body.instructions = codexInstructions;

	// Prompt caching relies on the host providing a stable prompt_cache_key
	// (OpenCode passes its session identifier). We no longer synthesize one here.

	// Filter and transform input
	if (body.input && Array.isArray(body.input)) {
		// Debug: Log original input message IDs before filtering
		const originalIds = body.input
			.filter((item) => item.id)
			.map((item) => item.id);
		if (originalIds.length > 0) {
			logDebug(
				`Filtering ${originalIds.length} message IDs from input:`,
				originalIds,
			);
		}

		body.input = filterInput(body.input);

		// Debug: Verify all IDs were removed
		const remainingIds = (body.input || [])
			.filter((item) => item.id)
			.map((item) => item.id);
		if (remainingIds.length > 0) {
			logWarn(
				`WARNING: ${remainingIds.length} IDs still present after filtering:`,
				remainingIds,
			);
		} else if (originalIds.length > 0) {
			logDebug(`Successfully removed all ${originalIds.length} message IDs`);
		}

		if (codexMode) {
			// CODEX_MODE: Remove OpenCode system prompt, add bridge prompt
			body.input = await filterOpenCodeSystemPrompts(body.input);
			body.input = addCodexBridgeMessage(body.input, !!body.tools);
		} else {
			// DEFAULT MODE: Keep original behavior with tool remap message
			body.input = addToolRemapMessage(body.input, !!body.tools);
		}

		// Handle orphaned function_call_output items (where function_call was an item_reference that got filtered)
		// Instead of removing orphans (which causes infinite loops as LLM loses tool results),
		// convert them to messages to preserve context while avoiding API errors
		if (body.input) {
			body.input = normalizeOrphanedToolOutputs(body.input);
		}
	}

	// Configure reasoning (prefer existing body/provider options, then config defaults)
	const reasoningConfig = resolveReasoningConfig(
		normalizedModel,
		modelConfig,
		body,
	);
	body.reasoning = {
		...body.reasoning,
		...reasoningConfig,
	};

	// Configure text verbosity (support user config)
	// Default: "medium" (matches Codex CLI default for all GPT-5 models)
	body.text = {
		...body.text,
		verbosity: resolveTextVerbosity(modelConfig, body),
	};

	// Add include for encrypted reasoning content
	// Default: ["reasoning.encrypted_content"] (required for stateless operation with store=false)
	// This allows reasoning context to persist across turns without server-side storage
	body.include = resolveInclude(modelConfig, body);

	// Remove unsupported parameters
	body.max_output_tokens = undefined;
	body.max_completion_tokens = undefined;

	return body;
}
```

## File: `lib/request/response-handler.ts`
```typescript
import { logRequest, LOGGING_ENABLED } from "../logger.js";
import type { SSEEventData } from "../types.js";

/**
 * Parse SSE stream to extract final response
 * @param sseText - Complete SSE stream text
 * @returns Final response object or null if not found
 */
function parseSseStream(sseText: string): unknown | null {
	const lines = sseText.split('\n');

	for (const line of lines) {
		if (line.startsWith('data: ')) {
			try {
				const data = JSON.parse(line.substring(6)) as SSEEventData;

				// Look for response.done event with final data
				if (data.type === 'response.done' || data.type === 'response.completed') {
					return data.response;
				}
			} catch (e) {
				// Skip malformed JSON
			}
		}
	}

	return null;
}

/**
 * Convert SSE stream response to JSON for generateText()
 * @param response - Fetch response with SSE stream
 * @param headers - Response headers
 * @returns Response with JSON body
 */
export async function convertSseToJson(response: Response, headers: Headers): Promise<Response> {
	if (!response.body) {
		throw new Error('[openai-codex-plugin] Response has no body');
	}
	const reader = response.body.getReader();
	const decoder = new TextDecoder();
	let fullText = '';

	try {
		// Consume the entire stream
		while (true) {
			const { done, value } = await reader.read();
			if (done) break;
			fullText += decoder.decode(value, { stream: true });
		}

		if (LOGGING_ENABLED) {
			logRequest("stream-full", { fullContent: fullText });
		}

		// Parse SSE events to extract the final response
		const finalResponse = parseSseStream(fullText);

		if (!finalResponse) {
			console.error('[openai-codex-plugin] Could not find final response in SSE stream');
			logRequest("stream-error", { error: "No response.done event found" });

			// Return original stream if we can't parse
			return new Response(fullText, {
				status: response.status,
				statusText: response.statusText,
				headers: headers,
			});
		}

		// Return as plain JSON (not SSE)
		const jsonHeaders = new Headers(headers);
		jsonHeaders.set('content-type', 'application/json; charset=utf-8');

		return new Response(JSON.stringify(finalResponse), {
			status: response.status,
			statusText: response.statusText,
			headers: jsonHeaders,
		});

	} catch (error) {
		console.error('[openai-codex-plugin] Error converting stream:', error);
		logRequest("stream-error", { error: String(error) });
		throw error;
	}
}

/**
 * Ensure response has content-type header
 * @param headers - Response headers
 * @returns Headers with content-type set
 */
export function ensureContentType(headers: Headers): Headers {
	const responseHeaders = new Headers(headers);

	if (!responseHeaders.has('content-type')) {
		responseHeaders.set('content-type', 'text/event-stream; charset=utf-8');
	}

	return responseHeaders;
}
```

## File: `lib/request/helpers/input-utils.ts`
```typescript
import type { InputItem } from "../../types.js";

const OPENCODE_PROMPT_SIGNATURES = [
	"you are a coding agent running in the opencode",
	"you are opencode, an agent",
	"you are opencode, an interactive cli agent",
	"you are opencode, an interactive cli tool",
	"you are opencode, the best coding agent on the planet",
].map((signature) => signature.toLowerCase());

const OPENCODE_CONTEXT_MARKERS = [
	"here is some useful information about the environment you are running in:",
	"<env>",
	"instructions from:",
	"<instructions>",
].map((marker) => marker.toLowerCase());

export const getContentText = (item: InputItem): string => {
	if (typeof item.content === "string") {
		return item.content;
	}
	if (Array.isArray(item.content)) {
		return item.content
			.filter((c) => c.type === "input_text" && c.text)
			.map((c) => c.text)
			.join("\n");
	}
	return "";
};

const replaceContentText = (item: InputItem, contentText: string): InputItem => {
	if (typeof item.content === "string") {
		return { ...item, content: contentText };
	}
	if (Array.isArray(item.content)) {
		return {
			...item,
			content: [{ type: "input_text", text: contentText }],
		};
	}
	return { ...item, content: contentText };
};

const extractOpenCodeContext = (contentText: string): string | null => {
	const lower = contentText.toLowerCase();
	let earliestIndex = -1;

	for (const marker of OPENCODE_CONTEXT_MARKERS) {
		const index = lower.indexOf(marker);
		if (index >= 0 && (earliestIndex === -1 || index < earliestIndex)) {
			earliestIndex = index;
		}
	}

	if (earliestIndex === -1) return null;
	return contentText.slice(earliestIndex).trimStart();
};

export function isOpenCodeSystemPrompt(
	item: InputItem,
	cachedPrompt: string | null,
): boolean {
	const isSystemRole = item.role === "developer" || item.role === "system";
	if (!isSystemRole) return false;

	const contentText = getContentText(item);
	if (!contentText) return false;

	if (cachedPrompt) {
		const contentTrimmed = contentText.trim();
		const cachedTrimmed = cachedPrompt.trim();
		if (contentTrimmed === cachedTrimmed) {
			return true;
		}

		if (contentTrimmed.startsWith(cachedTrimmed)) {
			return true;
		}

		const contentPrefix = contentTrimmed.substring(0, 200);
		const cachedPrefix = cachedTrimmed.substring(0, 200);
		if (contentPrefix === cachedPrefix) {
			return true;
		}
	}

	const normalized = contentText.trimStart().toLowerCase();
	return OPENCODE_PROMPT_SIGNATURES.some((signature) =>
		normalized.startsWith(signature),
	);
}

export function filterOpenCodeSystemPromptsWithCachedPrompt(
	input: InputItem[] | undefined,
	cachedPrompt: string | null,
): InputItem[] | undefined {
	if (!Array.isArray(input)) return input;

	return input.flatMap((item) => {
		if (item.role === "user") return [item];

		if (!isOpenCodeSystemPrompt(item, cachedPrompt)) {
			return [item];
		}

		const contentText = getContentText(item);
		const preservedContext = extractOpenCodeContext(contentText);
		if (preservedContext) {
			return [replaceContentText(item, preservedContext)];
		}

		return [];
	});
}

const getCallId = (item: InputItem): string | null => {
	const rawCallId = (item as { call_id?: unknown }).call_id;
	if (typeof rawCallId !== "string") return null;
	const trimmed = rawCallId.trim();
	return trimmed.length > 0 ? trimmed : null;
};

const convertOrphanedOutputToMessage = (
	item: InputItem,
	callId: string | null,
): InputItem => {
	const toolName =
		typeof (item as { name?: unknown }).name === "string"
			? ((item as { name?: string }).name as string)
			: "tool";
	const labelCallId = callId ?? "unknown";
	let text: string;
	try {
		const out = (item as { output?: unknown }).output;
		text = typeof out === "string" ? out : JSON.stringify(out);
	} catch {
		text = String((item as { output?: unknown }).output ?? "");
	}
	if (text.length > 16000) {
		text = text.slice(0, 16000) + "\n...[truncated]";
	}
	return {
		type: "message",
		role: "assistant",
		content: `[Previous ${toolName} result; call_id=${labelCallId}]: ${text}`,
	} as InputItem;
};

const collectCallIds = (input: InputItem[]) => {
	const functionCallIds = new Set<string>();
	const localShellCallIds = new Set<string>();
	const customToolCallIds = new Set<string>();

	for (const item of input) {
		const callId = getCallId(item);
		if (!callId) continue;
		switch (item.type) {
			case "function_call":
				functionCallIds.add(callId);
				break;
			case "local_shell_call":
				localShellCallIds.add(callId);
				break;
			case "custom_tool_call":
				customToolCallIds.add(callId);
				break;
			default:
				break;
		}
	}

	return { functionCallIds, localShellCallIds, customToolCallIds };
};

export const normalizeOrphanedToolOutputs = (
	input: InputItem[],
): InputItem[] => {
	const { functionCallIds, localShellCallIds, customToolCallIds } =
		collectCallIds(input);

	return input.map((item) => {
		if (item.type === "function_call_output") {
			const callId = getCallId(item);
			const hasMatch =
				!!callId &&
				(functionCallIds.has(callId) || localShellCallIds.has(callId));
			if (!hasMatch) {
				return convertOrphanedOutputToMessage(item, callId);
			}
		}

		if (item.type === "custom_tool_call_output") {
			const callId = getCallId(item);
			const hasMatch = !!callId && customToolCallIds.has(callId);
			if (!hasMatch) {
				return convertOrphanedOutputToMessage(item, callId);
			}
		}

		if (item.type === "local_shell_call_output") {
			const callId = getCallId(item);
			const hasMatch = !!callId && localShellCallIds.has(callId);
			if (!hasMatch) {
				return convertOrphanedOutputToMessage(item, callId);
			}
		}

		return item;
	});
};
```

## File: `lib/request/helpers/model-map.ts`
```typescript
/**
 * Model Configuration Map
 *
 * Maps model config IDs to their normalized API model names.
 * Only includes exact config IDs that OpenCode will pass to the plugin.
 */

/**
 * Map of config model IDs to normalized API model names
 *
 * Key: The model ID as specified in opencode.json config
 * Value: The normalized model name to send to the API
 */
export const MODEL_MAP: Record<string, string> = {
// ============================================================================
// GPT-5.1 Codex Models
// ============================================================================
	"gpt-5.1-codex": "gpt-5.1-codex",
	"gpt-5.1-codex-low": "gpt-5.1-codex",
	"gpt-5.1-codex-medium": "gpt-5.1-codex",
	"gpt-5.1-codex-high": "gpt-5.1-codex",

	// ============================================================================
	// GPT-5.1 Codex Max Models
	// ============================================================================
	"gpt-5.1-codex-max": "gpt-5.1-codex-max",
	"gpt-5.1-codex-max-low": "gpt-5.1-codex-max",
	"gpt-5.1-codex-max-medium": "gpt-5.1-codex-max",
	"gpt-5.1-codex-max-high": "gpt-5.1-codex-max",
	"gpt-5.1-codex-max-xhigh": "gpt-5.1-codex-max",

	// ============================================================================
	// GPT-5.2 Models (supports none/low/medium/high/xhigh per OpenAI API docs)
	// ============================================================================
	"gpt-5.2": "gpt-5.2",
	"gpt-5.2-none": "gpt-5.2",
	"gpt-5.2-low": "gpt-5.2",
	"gpt-5.2-medium": "gpt-5.2",
	"gpt-5.2-high": "gpt-5.2",
	"gpt-5.2-xhigh": "gpt-5.2",

	// ============================================================================
	// GPT-5.2 Codex Models (low/medium/high/xhigh)
	// ============================================================================
	"gpt-5.2-codex": "gpt-5.2-codex",
	"gpt-5.2-codex-low": "gpt-5.2-codex",
	"gpt-5.2-codex-medium": "gpt-5.2-codex",
	"gpt-5.2-codex-high": "gpt-5.2-codex",
	"gpt-5.2-codex-xhigh": "gpt-5.2-codex",

	// ============================================================================
	// GPT-5.1 Codex Mini Models
	// ============================================================================
	"gpt-5.1-codex-mini": "gpt-5.1-codex-mini",
	"gpt-5.1-codex-mini-medium": "gpt-5.1-codex-mini",
	"gpt-5.1-codex-mini-high": "gpt-5.1-codex-mini",

	// ============================================================================
	// GPT-5.1 General Purpose Models (supports none/low/medium/high per OpenAI API docs)
	// ============================================================================
	"gpt-5.1": "gpt-5.1",
	"gpt-5.1-none": "gpt-5.1",
	"gpt-5.1-low": "gpt-5.1",
	"gpt-5.1-medium": "gpt-5.1",
	"gpt-5.1-high": "gpt-5.1",
	"gpt-5.1-chat-latest": "gpt-5.1",

	// ============================================================================
	// GPT-5 Codex Models (LEGACY - maps to gpt-5.1-codex as gpt-5 is being phased out)
	// ============================================================================
	"gpt-5-codex": "gpt-5.1-codex",

	// ============================================================================
	// GPT-5 Codex Mini Models (LEGACY - maps to gpt-5.1-codex-mini)
	// ============================================================================
	"codex-mini-latest": "gpt-5.1-codex-mini",
	"gpt-5-codex-mini": "gpt-5.1-codex-mini",
	"gpt-5-codex-mini-medium": "gpt-5.1-codex-mini",
	"gpt-5-codex-mini-high": "gpt-5.1-codex-mini",

	// ============================================================================
	// GPT-5 General Purpose Models (LEGACY - maps to gpt-5.1 as gpt-5 is being phased out)
	// ============================================================================
	"gpt-5": "gpt-5.1",
	"gpt-5-mini": "gpt-5.1",
	"gpt-5-nano": "gpt-5.1",
};

/**
 * Get normalized model name from config ID
 *
 * @param modelId - Model ID from config (e.g., "gpt-5.1-codex-low")
 * @returns Normalized model name (e.g., "gpt-5.1-codex") or undefined if not found
 */
export function getNormalizedModel(modelId: string): string | undefined {
	try {
		// Try direct lookup first
		if (MODEL_MAP[modelId]) {
			return MODEL_MAP[modelId];
		}

		// Try case-insensitive lookup
		const lowerModelId = modelId.toLowerCase();
		const match = Object.keys(MODEL_MAP).find(
			(key) => key.toLowerCase() === lowerModelId,
		);

		return match ? MODEL_MAP[match] : undefined;
	} catch {
		return undefined;
	}
}

/**
 * Check if a model ID is in the model map
 *
 * @param modelId - Model ID to check
 * @returns True if model is in the map
 */
export function isKnownModel(modelId: string): boolean {
	return getNormalizedModel(modelId) !== undefined;
}
```

## File: `scripts/install-opencode-codex-auth.js`
```javascript
#!/usr/bin/env node

import { existsSync } from "node:fs";
import { readFile, writeFile, mkdir, copyFile, rm } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { dirname, join, resolve } from "node:path";
import { homedir } from "node:os";
import { parse, modify, applyEdits, printParseErrorCode } from "jsonc-parser";

const PLUGIN_NAME = "opencode-openai-codex-auth";
const args = new Set(process.argv.slice(2));

if (args.has("--help") || args.has("-h")) {
	console.log(`Usage: ${PLUGIN_NAME} [--modern|--legacy] [--uninstall] [--all] [--dry-run] [--no-cache-clear]\n\n` +
		"Default behavior:\n" +
		"  - Installs/updates global config at ~/.config/opencode/opencode.jsonc (falls back to .json)\n" +
		"  - Uses modern config (variants) by default\n" +
		"  - Ensures plugin is unpinned (latest)\n" +
		"  - Clears OpenCode plugin cache\n\n" +
		"Options:\n" +
		"  --modern           Force modern config (default)\n" +
		"  --legacy           Use legacy config (older OpenCode versions)\n" +
		"  --uninstall        Remove plugin + OpenAI config entries from global config\n" +
		"  --all              With --uninstall, also remove tokens, logs, and cached instructions\n" +
		"  --dry-run          Show actions without writing\n" +
		"  --no-cache-clear   Skip clearing OpenCode cache\n"
	);
	process.exit(0);
}

const useLegacy = args.has("--legacy");
const useModern = args.has("--modern") || !useLegacy;
const uninstallRequested = args.has("--uninstall") || args.has("--all");
const uninstallAll = args.has("--all");
const dryRun = args.has("--dry-run");
const skipCacheClear = args.has("--no-cache-clear");

const scriptDir = dirname(fileURLToPath(import.meta.url));
const repoRoot = resolve(scriptDir, "..");
const templatePath = join(
	repoRoot,
	"config",
	useLegacy ? "opencode-legacy.json" : "opencode-modern.json"
);

const configDir = join(homedir(), ".config", "opencode");
const configPathJson = join(configDir, "opencode.json");
const configPathJsonc = join(configDir, "opencode.jsonc");
const cacheDir = join(homedir(), ".cache", "opencode");
const cacheNodeModules = join(cacheDir, "node_modules", PLUGIN_NAME);
const cacheBunLock = join(cacheDir, "bun.lock");
const cachePackageJson = join(cacheDir, "package.json");
const opencodeAuthPath = join(homedir(), ".opencode", "auth", "openai.json");
const pluginConfigPath = join(
	homedir(),
	".opencode",
	"openai-codex-auth-config.json",
);
const pluginLogDir = join(homedir(), ".opencode", "logs", "codex-plugin");
const opencodeCacheDir = join(homedir(), ".opencode", "cache");

function log(message) {
	console.log(message);
}

function normalizePluginList(list) {
	const entries = Array.isArray(list) ? list.filter(Boolean) : [];
	const filtered = entries.filter((entry) => {
		if (typeof entry !== "string") return true;
		return entry !== PLUGIN_NAME && !entry.startsWith(`${PLUGIN_NAME}@`);
	});
	return [...filtered, PLUGIN_NAME];
}

function removePluginEntries(list) {
	const entries = Array.isArray(list) ? list.filter(Boolean) : [];
	return entries.filter((entry) => {
		if (typeof entry !== "string") return true;
		if (entry === PLUGIN_NAME || entry.startsWith(`${PLUGIN_NAME}@`)) {
			return false;
		}
		return !entry.includes(PLUGIN_NAME);
	});
}

function mergeOpenAIConfig(existingOpenAI, templateOpenAI) {
	const existing = existingOpenAI && typeof existingOpenAI === "object"
		? existingOpenAI
		: {};
	const template = templateOpenAI && typeof templateOpenAI === "object"
		? templateOpenAI
		: {};
	const existingOptions =
		existing.options && typeof existing.options === "object"
			? existing.options
			: {};
	const templateOptions =
		template.options && typeof template.options === "object"
			? template.options
			: {};
	const existingModels =
		existing.models && typeof existing.models === "object"
			? existing.models
			: {};
	const templateModels =
		template.models && typeof template.models === "object"
			? template.models
			: {};

	return {
		...existing,
		...template,
		options: { ...existingOptions, ...templateOptions },
		models: { ...existingModels, ...templateModels },
	};
}

async function getKnownModelIds() {
	const legacyTemplate = await readJson(
		join(repoRoot, "config", "opencode-legacy.json"),
	);
	const modernTemplate = await readJson(
		join(repoRoot, "config", "opencode-modern.json"),
	);
	const legacyModels = Object.keys(
		legacyTemplate?.provider?.openai?.models || {},
	);
	const modernModels = Object.keys(
		modernTemplate?.provider?.openai?.models || {},
	);
	return new Set([...legacyModels, ...modernModels]);
}

function formatJson(obj) {
	return `${JSON.stringify(obj, null, 2)}\n`;
}

const JSONC_PARSE_OPTIONS = { allowTrailingComma: true, disallowComments: false };
const JSONC_FORMAT_OPTIONS = { insertSpaces: true, tabSize: 2, eol: "\n" };

function resolveConfigPath() {
	if (existsSync(configPathJsonc)) {
		return configPathJsonc;
	}
	if (existsSync(configPathJson)) {
		return configPathJson;
	}
	return configPathJsonc;
}

async function readJson(filePath) {
	const content = await readFile(filePath, "utf-8");
	return JSON.parse(content);
}

async function readJsonc(filePath) {
	const content = await readFile(filePath, "utf-8");
	const errors = [];
	const data = parse(content, errors, JSONC_PARSE_OPTIONS);
	if (errors.length) {
		const formatted = errors
			.map((error) => printParseErrorCode(error.error))
			.join(", ");
		throw new Error(`Invalid JSONC (${formatted})`);
	}
	return { content, data: data ?? {} };
}

function applyJsoncUpdates(content, updates) {
	let next = content;
	for (const update of updates) {
		const edits = modify(next, update.path, update.value, {
			formattingOptions: JSONC_FORMAT_OPTIONS,
		});
		next = applyEdits(next, edits);
	}
	return next.endsWith("\n") ? next : `${next}\n`;
}

async function backupConfig(sourcePath) {
	const timestamp = new Date()
		.toISOString()
		.replace(/[:.]/g, "-")
		.replace("T", "_")
		.replace("Z", "");
	const backupPath = `${sourcePath}.bak-${timestamp}`;
	if (!dryRun) {
		await copyFile(sourcePath, backupPath);
	}
	return backupPath;
}

async function removePluginFromCachePackage() {
	if (!existsSync(cachePackageJson)) {
		return;
	}

	let cacheData;
	try {
		cacheData = await readJson(cachePackageJson);
	} catch (error) {
		log(`Warning: Could not parse ${cachePackageJson} (${error}). Skipping.`);
		return;
	}

	const sections = [
		"dependencies",
		"devDependencies",
		"peerDependencies",
		"optionalDependencies",
	];

	let changed = false;
	for (const section of sections) {
		const deps = cacheData?.[section];
		if (deps && typeof deps === "object" && PLUGIN_NAME in deps) {
			delete deps[PLUGIN_NAME];
			changed = true;
		}
	}

	if (!changed) {
		return;
	}

	if (dryRun) {
		log(`[dry-run] Would update ${cachePackageJson} to remove ${PLUGIN_NAME}`);
		return;
	}

	await writeFile(cachePackageJson, formatJson(cacheData), "utf-8");
}

async function clearCache() {
	if (skipCacheClear) {
		log("Skipping cache clear (--no-cache-clear).");
		return;
	}

	if (dryRun) {
		log(`[dry-run] Would remove ${cacheNodeModules}`);
		log(`[dry-run] Would remove ${cacheBunLock}`);
	} else {
		await rm(cacheNodeModules, { recursive: true, force: true });
		await rm(cacheBunLock, { force: true });
	}

	await removePluginFromCachePackage();
}

async function clearPluginArtifacts() {
	if (dryRun) {
		log(`[dry-run] Would remove ${opencodeAuthPath}`);
		log(`[dry-run] Would remove ${pluginConfigPath}`);
		log(`[dry-run] Would remove ${pluginLogDir}`);
	} else {
		await rm(opencodeAuthPath, { force: true });
		await rm(pluginConfigPath, { force: true });
		await rm(pluginLogDir, { recursive: true, force: true });
	}

	const cacheFiles = [
		"codex-instructions.md",
		"codex-instructions-meta.json",
		"codex-max-instructions.md",
		"codex-max-instructions-meta.json",
		"gpt-5.1-instructions.md",
		"gpt-5.1-instructions-meta.json",
		"gpt-5.2-instructions.md",
		"gpt-5.2-instructions-meta.json",
		"gpt-5.2-codex-instructions.md",
		"gpt-5.2-codex-instructions-meta.json",
		"opencode-codex.txt",
		"opencode-codex-meta.json",
	];

	for (const file of cacheFiles) {
		const target = join(opencodeCacheDir, file);
		if (dryRun) {
			log(`[dry-run] Would remove ${target}`);
		} else {
			await rm(target, { force: true });
		}
	}
}

async function main() {
	if (!existsSync(templatePath)) {
		throw new Error(`Config template not found at ${templatePath}`);
	}

	const configPath = resolveConfigPath();
	const configExists = existsSync(configPath);

	if (uninstallRequested) {
		if (!configExists) {
			log("No existing config found. Nothing to uninstall.");
		} else {
			const backupPath = await backupConfig(configPath);
			log(`${dryRun ? "[dry-run] Would create backup" : "Backup created"}: ${backupPath}`);

			try {
				const { content, data } = await readJsonc(configPath);
				const existing = data ?? {};
				const pluginList = removePluginEntries(existing.plugin);

				const provider =
					existing.provider && typeof existing.provider === "object"
						? { ...existing.provider }
						: {};
				const openai =
					provider.openai && typeof provider.openai === "object"
						? { ...provider.openai }
						: {};

				const knownModelIds = await getKnownModelIds();
				const existingModels =
					openai.models && typeof openai.models === "object"
						? { ...openai.models }
						: {};
				for (const modelId of knownModelIds) {
					delete existingModels[modelId];
				}

				if (Object.keys(existingModels).length > 0) {
					openai.models = existingModels;
				} else {
					delete openai.models;
				}

				if (Object.keys(openai).length > 0) {
					provider.openai = openai;
				} else {
					delete provider.openai;
				}

				const updates = [];
				if (pluginList.length > 0) {
					updates.push({ path: ["plugin"], value: pluginList });
				} else {
					updates.push({ path: ["plugin"], value: undefined });
				}

				if (Object.keys(provider).length > 0) {
					updates.push({ path: ["provider"], value: provider });
				} else {
					updates.push({ path: ["provider"], value: undefined });
				}

				if (dryRun) {
					log(`[dry-run] Would write ${configPath} (uninstall)`);
				} else {
					const nextContent = applyJsoncUpdates(content, updates);
					await writeFile(configPath, nextContent, "utf-8");
					log(`Updated ${configPath} (plugin removed)`);
				}
			} catch (error) {
				log(`Warning: Could not parse existing config (${error}). Skipping config update.`);
			}
		}

		await clearCache();
		if (uninstallAll) {
			await clearPluginArtifacts();
		}

		log("\nDone. Restart OpenCode.");
		return;
	}

	const template = await readJson(templatePath);
	template.plugin = [PLUGIN_NAME];

	let nextConfig = template;
	let nextContent = null;

	if (configExists) {
		const backupPath = await backupConfig(configPath);
		log(`${dryRun ? "[dry-run] Would create backup" : "Backup created"}: ${backupPath}`);

		try {
			const { content, data } = await readJsonc(configPath);
			const existing = data ?? {};
			const merged = { ...existing };
			merged.plugin = normalizePluginList(existing.plugin);
			const provider =
				existing.provider && typeof existing.provider === "object"
					? { ...existing.provider }
					: {};
			provider.openai = mergeOpenAIConfig(provider.openai, template.provider.openai);
			merged.provider = provider;
			nextConfig = merged;

			nextContent = applyJsoncUpdates(content, [
				{ path: ["plugin"], value: merged.plugin },
				{ path: ["provider", "openai"], value: merged.provider.openai },
			]);
		} catch (error) {
			log(`Warning: Could not parse existing config (${error}). Replacing with template.`);
			nextConfig = template;
		}
	} else {
		log("No existing config found. Creating new global config.");
	}

	if (dryRun) {
		log(`[dry-run] Would write ${configPath} using ${useLegacy ? "legacy" : "modern"} config`);
	} else {
		await mkdir(configDir, { recursive: true });
		if (nextContent && configExists) {
			await writeFile(configPath, nextContent, "utf-8");
		} else {
			await writeFile(configPath, formatJson(nextConfig), "utf-8");
		}
		log(`Wrote ${configPath} (${useLegacy ? "legacy" : "modern"} config)`);
	}

	await clearCache();

	log("\nDone. Restart OpenCode to (re)install the plugin.");
	log("Example: opencode");
	if (useLegacy) {
		log("Note: Legacy config requires OpenCode v1.0.209 or older.");
	}
}

main().catch((error) => {
	console.error(`Installer failed: ${error instanceof Error ? error.message : error}`);
	process.exit(1);
});
```

## File: `scripts/test-all-models.sh`
```bash
#!/bin/bash

# Test All Models - Verify API Configuration
# This script tests all model configurations and verifies the actual API requests

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Paths
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OPENCODE_JSON="${REPO_DIR}/opencode.json"
LOG_DIR="${HOME}/.opencode/logs/codex-plugin"
RESULTS_FILE="${REPO_DIR}/test-results.md"

# Test counter
TOTAL_TESTS=0
PASSED_TESTS=0
FAILED_TESTS=0

echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Model Configuration Verification Test Suite${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo ""

# Kill any running OpenCode server processes to force fresh plugin load
echo "Killing OpenCode server processes..."
pkill -f "opencode" 2>/dev/null || true
sleep 2
echo "✓ OpenCode servers stopped"
echo ""

# Initialize results file
cat > "${RESULTS_FILE}" << 'EOF'
# Model Configuration Verification Results

**Test Date:** $(date)
**Test Directory:** Repository local config

## Results Summary

| Model | Normalized | Family | Effort | Summary | Verbosity | Include | Status |
|-------|------------|--------|--------|---------|-----------|---------|--------|
EOF

# Function: Run a test for a specific model
test_model() {
    local model_name="$1"
    local expected_normalized="$2"
    local expected_family="$3"
    local expected_effort="$4"
    local expected_summary="$5"
    local expected_verbosity="$6"

    ((TOTAL_TESTS++))

    echo -e "${YELLOW}Testing model: ${model_name}${NC}"

    # Clear previous logs
    rm -rf "${LOG_DIR}"/*

    # Run opencode
    cd "${REPO_DIR}"
    if ENABLE_PLUGIN_REQUEST_LOGGING=1 DEBUG_CODEX_PLUGIN=1 opencode run "write hello to test-${TOTAL_TESTS}.txt" --model="openai/${model_name}" > /dev/null 2>&1; then
        echo -e "${GREEN}  ✓ Command executed successfully${NC}"
    else
        echo -e "${RED}  ✗ Command failed${NC}"
        echo "| ${model_name} | N/A | N/A | N/A | N/A | N/A | ❌ FAILED |" >> "${RESULTS_FILE}"
        ((FAILED_TESTS++))
        return 1
    fi

    # Find the after-transform log file that matches the expected model
    # (opencode may use multiple models per session - e.g., nano for titles)
    local log_file=""
    for f in $(find "${LOG_DIR}" -name "*-after-transform.json" -type f -print0 | xargs -0 ls -t); do
        local orig_model=$(jq -r '.originalModel // ""' "$f" 2>/dev/null)
        if [ "${orig_model}" = "${model_name}" ]; then
            log_file="$f"
            break
        fi
    done

    if [ -z "${log_file}" ] || [ ! -f "${log_file}" ]; then
        echo -e "${RED}  ✗ Log file not found for model ${model_name}${NC}"
        echo "| ${model_name} | N/A | N/A | N/A | N/A | N/A | ❌ NO LOG |" >> "${RESULTS_FILE}"
        ((FAILED_TESTS++))
        return 1
    fi

    # Parse log file with jq
    local actual_normalized=$(jq -r '.normalizedModel // "N/A"' "${log_file}")
    local actual_family=$(jq -r '.modelFamily // "N/A"' "${log_file}")
    local actual_effort=$(jq -r '.reasoning.effort // "N/A"' "${log_file}")
    local actual_summary=$(jq -r '.reasoning.summary // "N/A"' "${log_file}")
    local actual_verbosity=$(jq -r '.body.text.verbosity // "N/A"' "${log_file}")
    local actual_include=$(jq -r '.include[0] // "N/A"' "${log_file}")

    echo "  Actual: model=${actual_normalized}, family=${actual_family}, effort=${actual_effort}, summary=${actual_summary}, verbosity=${actual_verbosity}"
    echo "  Expected: model=${expected_normalized}, family=${expected_family}, effort=${expected_effort}, summary=${expected_summary}, verbosity=${expected_verbosity}"

    # Verify values
    local status="✅ PASS"
    if [ "${actual_normalized}" != "${expected_normalized}" ] || \
       [ "${actual_family}" != "${expected_family}" ] || \
       [ "${actual_effort}" != "${expected_effort}" ] || \
       [ "${actual_summary}" != "${expected_summary}" ] || \
       [ "${actual_verbosity}" != "${expected_verbosity}" ]; then
        status="❌ FAIL"
        ((FAILED_TESTS++))
        echo -e "${RED}  ✗ Verification failed${NC}"
    else
        ((PASSED_TESTS++))
        echo -e "${GREEN}  ✓ Verification passed${NC}"
    fi

    # Add to results
    echo "| ${model_name} | ${actual_normalized} | ${actual_family} | ${actual_effort} | ${actual_summary} | ${actual_verbosity} | ${actual_include} | ${status} |" >> "${RESULTS_FILE}"

    # Cleanup
    rm -f "${REPO_DIR}/test-${TOTAL_TESTS}.txt"

    echo ""
}

# Function: Update opencode.json with config
update_config() {
    local config_type="$1"

    echo -e "${BLUE}─────────────────────────────────────────────────────────────────${NC}"
    echo -e "${BLUE}Scenario: ${config_type}${NC}"
    echo -e "${BLUE}─────────────────────────────────────────────────────────────────${NC}"
    echo ""

    case "${config_type}" in
        "legacy")
            cat "${REPO_DIR}/config/opencode-legacy.json" > "${OPENCODE_JSON}"
            echo "✓ Updated opencode.json with legacy config (GPT 5.x)"
            ;;
        "minimal")
            cat "${REPO_DIR}/config/minimal-opencode.json" > "${OPENCODE_JSON}"
            echo "✓ Updated opencode.json with minimal config"
            ;;
    esac

    # Replace npm package with local dist for testing
    sed -i.bak -E 's|"opencode-openai-codex-auth(@[^"]*)?"|"file://'"${REPO_DIR}"'/dist"|' "${OPENCODE_JSON}"
    rm -f "${OPENCODE_JSON}.bak"
    echo "✓ Using local dist for plugin"

    echo ""
}

# ============================================================================
# Scenario 1: Legacy Config - GPT 5.x Model Family
# ============================================================================
update_config "legacy"

# GPT 5.1 Codex presets
test_model "gpt-5.1-codex-low"        "gpt-5.1-codex"       "codex"      "low"     "auto"     "medium"
test_model "gpt-5.1-codex-medium"     "gpt-5.1-codex"       "codex"      "medium"  "auto"     "medium"
test_model "gpt-5.1-codex-high"       "gpt-5.1-codex"       "codex"      "high"    "detailed" "medium"
test_model "gpt-5.1-codex-max-low"    "gpt-5.1-codex-max"   "codex-max"  "low"     "detailed" "medium"
test_model "gpt-5.1-codex-max-medium" "gpt-5.1-codex-max"   "codex-max"  "medium"  "detailed" "medium"
test_model "gpt-5.1-codex-max-high"   "gpt-5.1-codex-max"   "codex-max"  "high"    "detailed" "medium"
test_model "gpt-5.1-codex-max-xhigh"  "gpt-5.1-codex-max"   "codex-max"  "xhigh"   "detailed" "medium"

# GPT 5.2 presets (supports none/low/medium/high/xhigh per OpenAI API docs)
test_model "gpt-5.2-none"   "gpt-5.2"   "gpt-5.2"  "none"    "auto"     "medium"
test_model "gpt-5.2-low"    "gpt-5.2"   "gpt-5.2"  "low"     "auto"     "medium"
test_model "gpt-5.2-medium" "gpt-5.2"   "gpt-5.2"  "medium"  "auto"     "medium"
test_model "gpt-5.2-high"   "gpt-5.2"   "gpt-5.2"  "high"    "detailed" "medium"
test_model "gpt-5.2-xhigh"  "gpt-5.2"   "gpt-5.2"  "xhigh"   "detailed" "medium"

# GPT 5.2 Codex presets
test_model "gpt-5.2-codex-low"    "gpt-5.2-codex" "gpt-5.2-codex" "low"    "auto"     "medium"
test_model "gpt-5.2-codex-medium" "gpt-5.2-codex" "gpt-5.2-codex" "medium" "auto"     "medium"
test_model "gpt-5.2-codex-high"   "gpt-5.2-codex" "gpt-5.2-codex" "high"   "detailed" "medium"
test_model "gpt-5.2-codex-xhigh"  "gpt-5.2-codex" "gpt-5.2-codex" "xhigh"  "detailed" "medium"

# GPT 5.1 Codex Mini presets (medium/high only)
test_model "gpt-5.1-codex-mini-medium" "gpt-5.1-codex-mini" "codex"      "medium"  "auto"     "medium"
test_model "gpt-5.1-codex-mini-high"   "gpt-5.1-codex-mini" "codex"      "high"    "detailed" "medium"

# GPT 5.1 general-purpose presets (supports none/low/medium/high per OpenAI API docs)
test_model "gpt-5.1-none"          "gpt-5.1"       "gpt-5.1"    "none"    "auto"     "medium"
test_model "gpt-5.1-low"           "gpt-5.1"       "gpt-5.1"    "low"     "auto"     "low"
test_model "gpt-5.1-medium"        "gpt-5.1"       "gpt-5.1"    "medium"  "auto"     "medium"
test_model "gpt-5.1-high"          "gpt-5.1"       "gpt-5.1"    "high"    "detailed" "high"

# # ============================================================================
# # Scenario 2: Minimal Config - Default Models (No Custom Config)
# # ============================================================================
# update_config "minimal"

# test_model "gpt-5"       "gpt-5"       "medium"  "auto" "medium"
# test_model "gpt-5-codex" "gpt-5-codex" "medium"  "auto" "medium"
# test_model "gpt-5-mini"  "gpt-5"       "minimal" "auto" "medium"
# test_model "gpt-5-nano"  "gpt-5"       "minimal" "auto" "medium"

# ============================================================================
# Scenario 3: Backwards Compatibility
# ============================================================================
# update_config "backwards-compat"

# # GPT 5 Codex presets
# test_model "gpt-5-codex-low" "gpt-5-codex" "low" "auto" "medium"
# test_model "gpt-5-codex-medium" "gpt-5-codex" "medium" "auto" "medium"
# test_model "gpt-5-codex-high" "gpt-5-codex" "high" "detailed" "medium"

# GPT 5 Codex Mini presets
# test_model "gpt-5-codex-mini" "codex-mini-latest" "medium" "auto" "medium"
# test_model "gpt-5-codex-mini-medium" "codex-mini-latest" "medium" "auto" "medium"
# test_model "gpt-5-codex-mini-high" "codex-mini-latest" "high" "detailed" "medium"

# GPT 5 general-purpose presets
# test_model "gpt-5" "gpt-5" "medium" "auto" "medium"
# test_model "gpt-5-medium" "gpt-5" "medium" "auto" "medium"
# test_model "gpt-5-high" "gpt-5" "high" "detailed" "high"
# test_model "gpt-5-mini" "gpt-5" "minimal" "auto" "medium"

# ============================================================================
# Summary
# ============================================================================
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Test Results Summary${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "Total Tests:  ${TOTAL_TESTS}"
echo -e "${GREEN}Passed:       ${PASSED_TESTS}${NC}"
if [ ${FAILED_TESTS} -gt 0 ]; then
    echo -e "${RED}Failed:       ${FAILED_TESTS}${NC}"
else
echo -e "Failed:       ${FAILED_TESTS}"
fi
echo ""
echo -e "Results saved to: ${RESULTS_FILE} (will be removed)"
echo ""

# Restore original config
if [ -f "${REPO_DIR}/config/opencode-legacy.json" ]; then
    cat "${REPO_DIR}/config/opencode-legacy.json" > "${OPENCODE_JSON}"
    echo "✓ Restored original legacy config to opencode.json"
fi

# Cleanup results file to avoid polluting the repo
rm -f "${RESULTS_FILE}"

# Exit with appropriate code
if [ ${FAILED_TESTS} -gt 0 ]; then
    exit 1
else
    exit 0
fi
```

## File: `scripts/validate-model-map.sh`
```bash
#!/bin/bash

# Simple Model Map Validation Script
# Tests that OpenCode correctly uses models from config

set -e

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="${HOME}/.opencode/logs/codex-plugin"

echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Model Map Validation${NC}"
echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo ""

# Test 1: Model that IS in the config (should work)
echo -e "${YELLOW}Test 1: Model IN config (gpt-5.1-codex-low)${NC}"
rm -rf "${LOG_DIR}"/*

cd "${REPO_DIR}"
if ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode run "say hello" --model="openai/gpt-5.1-codex-low" > /dev/null 2>&1; then
    # Check the log - find the one for gpt-5.1-codex-low specifically
    log_file=$(find "${LOG_DIR}" -name "*-after-transform.json" -exec grep -l "gpt-5.1-codex-low" {} \; | head -n 1)

    if [ -f "${log_file}" ]; then
        original=$(jq -r '.originalModel // "N/A"' "${log_file}")
        normalized=$(jq -r '.normalizedModel // "N/A"' "${log_file}")

        echo -e "  Original:   ${original}"
        echo -e "  Normalized: ${normalized}"

        if [ "${normalized}" == "gpt-5.1-codex" ]; then
            echo -e "  ${GREEN}✓ PASS - Correctly normalized to gpt-5.1-codex${NC}"
        else
            echo -e "  ${RED}✗ FAIL - Expected gpt-5.1-codex, got ${normalized}${NC}"
            exit 1
        fi
    else
        echo -e "  ${RED}✗ FAIL - No log file found${NC}"
        exit 1
    fi
else
    echo -e "  ${RED}✗ FAIL - Command failed${NC}"
    exit 1
fi

echo ""

# Test 2: Model that is NOT in the config (should error or use fallback)
echo -e "${YELLOW}Test 2: Model NOT in config (fake-model-xyz)${NC}"
rm -rf "${LOG_DIR}"/*

if ENABLE_PLUGIN_REQUEST_LOGGING=1 opencode run "write test" --model="openai/fake-model-xyz" > /dev/null 2>&1; then
    log_file=$(find "${LOG_DIR}" -name "*-after-transform.json" | head -n 1)

    if [ -f "${log_file}" ]; then
        original=$(jq -r '.originalModel // "N/A"' "${log_file}")
        normalized=$(jq -r '.normalizedModel // "N/A"' "${log_file}")

        echo -e "  Original:   ${original}"
        echo -e "  Normalized: ${normalized}"
        echo -e "  ${GREEN}✓ Command succeeded (using fallback: ${normalized})${NC}"
    else
        echo -e "  ${YELLOW}⚠ No log file (expected - model not in config)${NC}"
    fi
else
    echo -e "  ${YELLOW}⚠ Command failed (expected - model not in config)${NC}"
fi

echo ""

# Test 3: Verify config location
echo -e "${YELLOW}Test 3: Verify config file location${NC}"
if [ -f "${REPO_DIR}/opencode.json" ]; then
    plugin_path=$(jq -r '.plugin[0]' "${REPO_DIR}/opencode.json")
    model_count=$(jq '.provider.openai.models | length' "${REPO_DIR}/opencode.json")

    echo -e "  Config file:  ${REPO_DIR}/opencode.json"
    echo -e "  Plugin path:  ${plugin_path}"
    echo -e "  Models defined: ${model_count}"
    echo -e "  ${GREEN}✓ Config file found and valid${NC}"
else
    echo -e "  ${RED}✗ No opencode.json in repo directory${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}════════════════════════════════════════════${NC}"
echo -e "${GREEN}  All validation tests passed!${NC}"
echo -e "${GREEN}════════════════════════════════════════════${NC}"
```

## File: `test/README.md`
```markdown
# Test Suite

This directory contains the comprehensive test suite for the OpenAI Codex OAuth plugin.

## Test Structure

```
test/
├── README.md                      # This file
├── auth.test.ts                   # OAuth authentication tests
├── config.test.ts                 # Configuration parsing tests
├── logger.test.ts                 # Logging functionality tests
├── request-transformer.test.ts    # Request transformation tests
└── response-handler.test.ts       # Response handling tests
```

## Running Tests

```bash
# Run all tests once
npm test

# Watch mode (re-run on file changes)
npm run test:watch

# Visual test UI
npm run test:ui

# Generate coverage report
npm run test:coverage
```

## Test Coverage

### auth.test.ts (16 tests)
Tests OAuth authentication functionality:
- State generation and uniqueness
- Authorization input parsing (URL, code#state, query string formats)
- JWT decoding and payload extraction
- Authorization flow creation with PKCE
- URL parameter validation

### config.test.ts (13 tests)
Tests configuration parsing and merging:
- Global configuration application
- Per-model configuration overrides
- Mixed configuration (global + per-model)
- Default values and fallbacks
- Reasoning effort normalization (minimal → low for codex)
- Lightweight model detection (nano, mini)

### request-transformer.test.ts (30 tests)
Tests request body transformations:
- Model name normalization (all variants → gpt-5 or gpt-5-codex)
- Input filtering (removing stored conversation history)
- Tool remap message injection
- Reasoning configuration application
- Text verbosity settings
- Encrypted reasoning content inclusion
- Unsupported parameter removal

### response-handler.test.ts (10 tests)
Tests SSE to JSON conversion:
- Content-type header management
- SSE stream parsing (response.done, response.completed)
- Malformed JSON handling
- Empty stream handling
- Status preservation

### logger.test.ts (5 tests)
Tests logging functionality:
- LOGGING_ENABLED constant
- logRequest function parameter handling
- Complex data structure support

## Test Philosophy

1. **Comprehensive Coverage**: Each module has extensive tests covering normal cases, edge cases, and error conditions
2. **Fast Execution**: All tests run in < 250ms
3. **No External Dependencies**: Tests use mocked data and don't make real API calls
4. **Type Safety**: All tests are written in TypeScript with full type checking

## CI/CD Integration

Tests automatically run in GitHub Actions on:
- Every push to main
- Every pull request

The CI workflow tests against multiple Node.js versions (18.x, 20.x, 22.x) to ensure compatibility.

## Adding New Tests

When adding new functionality:

1. Create or update the relevant test file
2. Follow the existing pattern using vitest's `describe` and `it` blocks
3. Ensure tests are isolated and don't depend on external state
4. Run `npm test` to verify all tests pass
5. Run `npm run typecheck` to ensure TypeScript types are correct

## Example Configurations

See the `config/` directory for working configuration examples:
- `minimal-opencode.json`: Simplest setup with defaults
- `opencode-legacy.json`: Legacy complete example with all model variants
- `opencode-modern.json`: Variant-based example for OpenCode v1.0.210+
```

## File: `test/auth.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import {
	createState,
	parseAuthorizationInput,
	decodeJWT,
	createAuthorizationFlow,
	CLIENT_ID,
	AUTHORIZE_URL,
	REDIRECT_URI,
	SCOPE,
} from '../lib/auth/auth.js';

describe('Auth Module', () => {
	describe('createState', () => {
		it('should generate a random 32-character hex string', () => {
			const state = createState();
			expect(state).toMatch(/^[a-f0-9]{32}$/);
		});

		it('should generate unique states', () => {
			const state1 = createState();
			const state2 = createState();
			expect(state1).not.toBe(state2);
		});
	});

	describe('parseAuthorizationInput', () => {
		it('should parse full OAuth callback URL', () => {
			const input = 'http://localhost:1455/auth/callback?code=abc123&state=xyz789';
			const result = parseAuthorizationInput(input);
			expect(result).toEqual({ code: 'abc123', state: 'xyz789' });
		});

		it('should parse code#state format', () => {
			const input = 'abc123#xyz789';
			const result = parseAuthorizationInput(input);
			expect(result).toEqual({ code: 'abc123', state: 'xyz789' });
		});

		it('should parse query string format', () => {
			const input = 'code=abc123&state=xyz789';
			const result = parseAuthorizationInput(input);
			expect(result).toEqual({ code: 'abc123', state: 'xyz789' });
		});

		it('should parse code only', () => {
			const input = 'abc123';
			const result = parseAuthorizationInput(input);
			expect(result).toEqual({ code: 'abc123' });
		});

		it('should return empty object for empty input', () => {
			const result = parseAuthorizationInput('');
			expect(result).toEqual({});
		});

		it('should handle whitespace', () => {
			const result = parseAuthorizationInput('  ');
			expect(result).toEqual({});
		});
	});

	describe('decodeJWT', () => {
		it('should decode valid JWT token', () => {
			// Create a simple JWT token: header.payload.signature
			const header = Buffer.from(JSON.stringify({ alg: 'HS256', typ: 'JWT' })).toString('base64');
			const payload = Buffer.from(JSON.stringify({ sub: '1234567890', name: 'Test User' })).toString('base64');
			const signature = 'fake-signature';
			const token = `${header}.${payload}.${signature}`;

			const decoded = decodeJWT(token);
			expect(decoded).toEqual({ sub: '1234567890', name: 'Test User' });
		});

		it('should decode JWT with ChatGPT account info', () => {
			const payload = Buffer.from(JSON.stringify({
				'https://api.openai.com/auth': {
					chatgpt_account_id: 'account-123',
				},
			})).toString('base64');
			const token = `header.${payload}.signature`;

			const decoded = decodeJWT(token);
			expect(decoded?.['https://api.openai.com/auth']?.chatgpt_account_id).toBe('account-123');
		});

		it('should return null for invalid JWT', () => {
			const result = decodeJWT('invalid-token');
			expect(result).toBeNull();
		});

		it('should return null for malformed JWT', () => {
			const result = decodeJWT('header.payload');
			expect(result).toBeNull();
		});

		it('should return null for non-JSON payload', () => {
			const token = 'header.not-json.signature';
			const result = decodeJWT(token);
			expect(result).toBeNull();
		});
	});

	describe('createAuthorizationFlow', () => {
		it('should create authorization flow with PKCE', async () => {
			const flow = await createAuthorizationFlow();

			expect(flow).toHaveProperty('pkce');
			expect(flow).toHaveProperty('state');
			expect(flow).toHaveProperty('url');

			expect(flow.pkce).toHaveProperty('challenge');
			expect(flow.pkce).toHaveProperty('verifier');
			expect(flow.state).toMatch(/^[a-f0-9]{32}$/);
		});

		it('should generate URL with correct parameters', async () => {
			const flow = await createAuthorizationFlow();
			const url = new URL(flow.url);

			expect(url.origin + url.pathname).toBe(AUTHORIZE_URL);
			expect(url.searchParams.get('response_type')).toBe('code');
			expect(url.searchParams.get('client_id')).toBe(CLIENT_ID);
			expect(url.searchParams.get('redirect_uri')).toBe(REDIRECT_URI);
			expect(url.searchParams.get('scope')).toBe(SCOPE);
			expect(url.searchParams.get('code_challenge_method')).toBe('S256');
			expect(url.searchParams.get('code_challenge')).toBe(flow.pkce.challenge);
			expect(url.searchParams.get('state')).toBe(flow.state);
			expect(url.searchParams.get('id_token_add_organizations')).toBe('true');
			expect(url.searchParams.get('codex_cli_simplified_flow')).toBe('true');
			expect(url.searchParams.get('originator')).toBe('codex_cli_rs');
		});

		it('should generate unique flows', async () => {
			const flow1 = await createAuthorizationFlow();
			const flow2 = await createAuthorizationFlow();

			expect(flow1.state).not.toBe(flow2.state);
			expect(flow1.pkce.verifier).not.toBe(flow2.pkce.verifier);
			expect(flow1.url).not.toBe(flow2.url);
		});
	});
});
```

## File: `test/browser.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { getBrowserOpener, openBrowserUrl } from '../lib/auth/browser.js';
import { PLATFORM_OPENERS } from '../lib/constants.js';

describe('Browser Module', () => {
	describe('getBrowserOpener', () => {
		it('should return correct opener for darwin', () => {
			const originalPlatform = process.platform;
			Object.defineProperty(process, 'platform', { value: 'darwin' });
			expect(getBrowserOpener()).toBe(PLATFORM_OPENERS.darwin);
			Object.defineProperty(process, 'platform', { value: originalPlatform });
		});

		it('should return correct opener for win32', () => {
			const originalPlatform = process.platform;
			Object.defineProperty(process, 'platform', { value: 'win32' });
			expect(getBrowserOpener()).toBe(PLATFORM_OPENERS.win32);
			Object.defineProperty(process, 'platform', { value: originalPlatform });
		});

		it('should return linux opener for other platforms', () => {
			const originalPlatform = process.platform;
			Object.defineProperty(process, 'platform', { value: 'linux' });
			expect(getBrowserOpener()).toBe(PLATFORM_OPENERS.linux);
			Object.defineProperty(process, 'platform', { value: originalPlatform });
		});

		it('should handle unknown platforms', () => {
			const originalPlatform = process.platform;
			Object.defineProperty(process, 'platform', { value: 'freebsd' });
			expect(getBrowserOpener()).toBe(PLATFORM_OPENERS.linux);
			Object.defineProperty(process, 'platform', { value: originalPlatform });
		});
	});

	describe('openBrowserUrl', () => {
		it('should return false when opener command is missing', () => {
			const originalPlatform = process.platform;
			const originalPath = process.env.PATH;

			Object.defineProperty(process, 'platform', { value: 'linux' });
			process.env.PATH = '';

			const result = openBrowserUrl('https://example.com');
			expect(result).toBe(false);

			Object.defineProperty(process, 'platform', { value: originalPlatform });
			if (originalPath === undefined) {
				delete process.env.PATH;
			} else {
				process.env.PATH = originalPath;
			}
		});
	});
});
```

## File: `test/codex.test.ts`
```typescript
import { describe, it, expect } from "vitest";
import { getModelFamily } from "../lib/prompts/codex.js";

describe("Codex Module", () => {
	describe("getModelFamily", () => {
		describe("GPT-5.2 Codex family", () => {
			it("should return gpt-5.2-codex for gpt-5.2-codex", () => {
				expect(getModelFamily("gpt-5.2-codex")).toBe("gpt-5.2-codex");
			});

			it("should return gpt-5.2-codex for gpt-5.2-codex-low", () => {
				expect(getModelFamily("gpt-5.2-codex-low")).toBe("gpt-5.2-codex");
			});

			it("should return gpt-5.2-codex for gpt-5.2-codex-high", () => {
				expect(getModelFamily("gpt-5.2-codex-high")).toBe("gpt-5.2-codex");
			});

			it("should return gpt-5.2-codex for gpt-5.2-codex-xhigh", () => {
				expect(getModelFamily("gpt-5.2-codex-xhigh")).toBe("gpt-5.2-codex");
			});
		});

		describe("Codex Max family", () => {
			it("should return codex-max for gpt-5.1-codex-max", () => {
				expect(getModelFamily("gpt-5.1-codex-max")).toBe("codex-max");
			});

			it("should return codex-max for gpt-5.1-codex-max-low", () => {
				expect(getModelFamily("gpt-5.1-codex-max-low")).toBe("codex-max");
			});

			it("should return codex-max for gpt-5.1-codex-max-high", () => {
				expect(getModelFamily("gpt-5.1-codex-max-high")).toBe("codex-max");
			});

			it("should return codex-max for gpt-5.1-codex-max-xhigh", () => {
				expect(getModelFamily("gpt-5.1-codex-max-xhigh")).toBe("codex-max");
			});
		});

		describe("Codex family", () => {
			it("should return codex for gpt-5.1-codex", () => {
				expect(getModelFamily("gpt-5.1-codex")).toBe("codex");
			});

			it("should return codex for gpt-5.1-codex-low", () => {
				expect(getModelFamily("gpt-5.1-codex-low")).toBe("codex");
			});

			it("should return codex for gpt-5.1-codex-mini", () => {
				expect(getModelFamily("gpt-5.1-codex-mini")).toBe("codex");
			});

			it("should return codex for gpt-5.1-codex-mini-high", () => {
				expect(getModelFamily("gpt-5.1-codex-mini-high")).toBe("codex");
			});

			it("should return codex for codex-mini-latest", () => {
				expect(getModelFamily("codex-mini-latest")).toBe("codex");
			});
		});

		describe("GPT-5.1 general family", () => {
			it("should return gpt-5.1 for gpt-5.1", () => {
				expect(getModelFamily("gpt-5.1")).toBe("gpt-5.1");
			});

			it("should return gpt-5.1 for gpt-5.1-low", () => {
				expect(getModelFamily("gpt-5.1-low")).toBe("gpt-5.1");
			});

			it("should return gpt-5.1 for gpt-5.1-high", () => {
				expect(getModelFamily("gpt-5.1-high")).toBe("gpt-5.1");
			});

			it("should return gpt-5.1 for unknown models", () => {
				expect(getModelFamily("unknown-model")).toBe("gpt-5.1");
			});

			it("should return gpt-5.1 for empty string", () => {
				expect(getModelFamily("")).toBe("gpt-5.1");
			});
		});

		describe("GPT-5.2 general family", () => {
			it("should return gpt-5.2 for gpt-5.2", () => {
				expect(getModelFamily("gpt-5.2")).toBe("gpt-5.2");
			});

			it("should return gpt-5.2 for gpt-5.2-high", () => {
				expect(getModelFamily("gpt-5.2-high")).toBe("gpt-5.2");
			});
		});

		describe("Priority order", () => {
			it("should prioritize gpt-5.2-codex over gpt-5.2 general", () => {
				// "gpt-5.2-codex" also contains the substring "gpt-5.2"
				expect(getModelFamily("gpt-5.2-codex")).toBe("gpt-5.2-codex");
			});

			it("should prioritize codex-max over codex", () => {
				// Model contains both "codex-max" and "codex"
				expect(getModelFamily("gpt-5.1-codex-max")).toBe("codex-max");
			});

			it("should prioritize codex over gpt-5.1", () => {
				// Model contains both "codex" and potential gpt-5.1
				expect(getModelFamily("gpt-5.1-codex")).toBe("codex");
			});
		});
	});
});
```

## File: `test/config.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { getModelConfig, getReasoningConfig } from '../lib/request/request-transformer.js';
import type { UserConfig } from '../lib/types.js';

describe('Configuration Parsing', () => {
	const providerConfig = {
		options: {
			reasoningEffort: 'medium' as const,
			reasoningSummary: 'auto' as const,
			textVerbosity: 'medium' as const,
		},
		models: {
			'gpt-5-codex': {
				options: {
					reasoningSummary: 'concise' as const,
				},
			},
			'gpt-5': {
				options: {
					reasoningEffort: 'high' as const,
				},
			},
		},
	};

	const userConfig: UserConfig = {
		global: providerConfig.options || {},
		models: providerConfig.models || {},
	};

	describe('getModelConfig', () => {
		it('should merge global and model-specific config for gpt-5-codex', () => {
			const codexConfig = getModelConfig('gpt-5-codex', userConfig);

			expect(codexConfig.reasoningEffort).toBe('medium'); // from global
			expect(codexConfig.reasoningSummary).toBe('concise'); // from model override
			expect(codexConfig.textVerbosity).toBe('medium'); // from global
		});

		it('should merge global and model-specific config for gpt-5', () => {
			const gpt5Config = getModelConfig('gpt-5', userConfig);

			expect(gpt5Config.reasoningEffort).toBe('high'); // from model override
			expect(gpt5Config.reasoningSummary).toBe('auto'); // from global
			expect(gpt5Config.textVerbosity).toBe('medium'); // from global
		});

		it('should return empty config when no config provided', () => {
			const emptyConfig = getModelConfig('gpt-5-codex', { global: {}, models: {} });

			expect(emptyConfig).toEqual({});
		});
	});

		describe('getReasoningConfig', () => {
			it('should use user settings from merged config for gpt-5-codex', () => {
				const codexConfig = getModelConfig('gpt-5-codex', userConfig);
				const reasoningConfig = getReasoningConfig('gpt-5-codex', codexConfig);

			expect(reasoningConfig.effort).toBe('medium');
			expect(reasoningConfig.summary).toBe('concise');
		});

		it('should return defaults when no config provided', () => {
			const emptyConfig = getModelConfig('gpt-5-codex', { global: {}, models: {} });
			const defaultReasoning = getReasoningConfig('gpt-5-codex', emptyConfig);

			expect(defaultReasoning.effort).toBe('medium');
			expect(defaultReasoning.summary).toBe('auto');
		});

		it('should normalize lightweight defaults to low effort (nano/mini)', () => {
			const nanoReasoning = getReasoningConfig('gpt-5-nano', {});

			expect(nanoReasoning.effort).toBe('low');
			expect(nanoReasoning.summary).toBe('auto');
		});

		it('should normalize "minimal" to "low" for gpt-5-codex', () => {
			const codexMinimalConfig = { reasoningEffort: 'minimal' as const };
			const codexMinimalReasoning = getReasoningConfig('gpt-5-codex', codexMinimalConfig);

			expect(codexMinimalReasoning.effort).toBe('low');
			expect(codexMinimalReasoning.summary).toBe('auto');
		});

		it('should normalize "minimal" effort for non-codex models', () => {
			const gpt5MinimalConfig = { reasoningEffort: 'minimal' as const };
			const gpt5MinimalReasoning = getReasoningConfig('gpt-5', gpt5MinimalConfig);

			expect(gpt5MinimalReasoning.effort).toBe('low');
		});

		it('should handle high effort setting', () => {
			const highConfig = { reasoningEffort: 'high' as const };
			const highReasoning = getReasoningConfig('gpt-5', highConfig);

			expect(highReasoning.effort).toBe('high');
			expect(highReasoning.summary).toBe('auto');
		});

			it('should respect custom summary setting', () => {
				const detailedConfig = { reasoningSummary: 'detailed' as const };
				const detailedReasoning = getReasoningConfig('gpt-5-codex', detailedConfig);

				expect(detailedReasoning.summary).toBe('detailed');
			});

			it('should default codex-mini to medium effort', () => {
				const codexMiniReasoning = getReasoningConfig('gpt-5-codex-mini', {});
				expect(codexMiniReasoning.effort).toBe('medium');
			});

			it('should clamp codex-mini minimal/low to medium', () => {
				const minimal = getReasoningConfig('gpt-5-codex-mini', {
					reasoningEffort: 'minimal',
				});
				const low = getReasoningConfig('gpt-5-codex-mini-high', {
					reasoningEffort: 'low',
				});

				expect(minimal.effort).toBe('medium');
				expect(low.effort).toBe('medium');
			});

			it('should keep codex-mini high effort when requested', () => {
				const high = getReasoningConfig('codex-mini-latest', {
					reasoningEffort: 'high',
				});
				expect(high.effort).toBe('high');
			});
		});

	describe('Model-specific behavior', () => {
		it('should detect lightweight models correctly', () => {
			const miniReasoning = getReasoningConfig('gpt-5-mini', {});
			expect(miniReasoning.effort).toBe('low');
		});

		it('should detect codex models correctly', () => {
			const codexConfig = { reasoningEffort: 'minimal' as const };
			const codexReasoning = getReasoningConfig('gpt-5-codex', codexConfig);
			expect(codexReasoning.effort).toBe('low'); // normalized
		});

		it('should handle standard gpt-5 model', () => {
			const gpt5Reasoning = getReasoningConfig('gpt-5', {});
			expect(gpt5Reasoning.effort).toBe('medium');
		});
	});
});
```

## File: `test/fetch-helpers.test.ts`
```typescript
import { describe, it, expect, vi, afterEach } from 'vitest';
import * as authModule from '../lib/auth/auth.js';
import {
    shouldRefreshToken,
    refreshAndUpdateToken,
    extractRequestUrl,
    rewriteUrlForCodex,
    createCodexHeaders,
    handleErrorResponse,
} from '../lib/request/fetch-helpers.js';
import type { Auth } from '../lib/types.js';
import { URL_PATHS, OPENAI_HEADERS, OPENAI_HEADER_VALUES } from '../lib/constants.js';

describe('Fetch Helpers Module', () => {
	afterEach(() => {
		vi.restoreAllMocks();
	});

	describe('shouldRefreshToken', () => {
		it('should return true for non-oauth auth', () => {
			const auth: Auth = { type: 'api', key: 'test-key' };
			expect(shouldRefreshToken(auth)).toBe(true);
		});

		it('should return true when access token is missing', () => {
			const auth: Auth = { type: 'oauth', access: '', refresh: 'refresh-token', expires: Date.now() + 1000 };
			expect(shouldRefreshToken(auth)).toBe(true);
		});

		it('should return true when token is expired', () => {
			const auth: Auth = {
				type: 'oauth',
				access: 'access-token',
				refresh: 'refresh-token',
				expires: Date.now() - 1000 // expired
			};
			expect(shouldRefreshToken(auth)).toBe(true);
		});

		it('should return false for valid oauth token', () => {
			const auth: Auth = {
				type: 'oauth',
				access: 'access-token',
				refresh: 'refresh-token',
				expires: Date.now() + 10000 // valid for 10 seconds
			};
			expect(shouldRefreshToken(auth)).toBe(false);
		});
	});

	describe('refreshAndUpdateToken', () => {
		it('throws when refresh fails', async () => {
			const auth: Auth = { type: 'oauth', access: 'old', refresh: 'bad', expires: 0 };
			const client = { auth: { set: vi.fn() } } as any;
			vi.spyOn(authModule, 'refreshAccessToken').mockResolvedValue({ type: 'failed' } as any);

			await expect(refreshAndUpdateToken(auth, client)).rejects.toThrow();
		});

		it('updates stored auth on success', async () => {
			const auth: Auth = { type: 'oauth', access: 'old', refresh: 'oldr', expires: 0 };
			const client = { auth: { set: vi.fn() } } as any;
			vi.spyOn(authModule, 'refreshAccessToken').mockResolvedValue({
				type: 'success',
				access: 'new',
				refresh: 'newr',
				expires: 123,
			} as any);

			const updated = await refreshAndUpdateToken(auth, client);

			expect(client.auth.set).toHaveBeenCalledWith({
				path: { id: 'openai' },
				body: {
					type: 'oauth',
					access: 'new',
					refresh: 'newr',
					expires: 123,
				},
			});
			expect(updated.access).toBe('new');
			expect(updated.refresh).toBe('newr');
			expect(updated.expires).toBe(123);
		});
	});

	describe('extractRequestUrl', () => {
		it('should extract URL from string', () => {
			const url = 'https://example.com/test';
			expect(extractRequestUrl(url)).toBe(url);
		});

		it('should extract URL from URL object', () => {
			const url = new URL('https://example.com/test');
			expect(extractRequestUrl(url)).toBe('https://example.com/test');
		});

		it('should extract URL from Request object', () => {
			const request = new Request('https://example.com/test');
			expect(extractRequestUrl(request)).toBe('https://example.com/test');
		});
	});

	describe('rewriteUrlForCodex', () => {
		it('should rewrite /responses to /codex/responses', () => {
			const url = 'https://chatgpt.com/backend-api/responses';
			expect(rewriteUrlForCodex(url)).toBe('https://chatgpt.com/backend-api/codex/responses');
		});

		it('should not modify URL without /responses', () => {
			const url = 'https://chatgpt.com/backend-api/other';
			expect(rewriteUrlForCodex(url)).toBe(url);
		});

		it('should only replace first occurrence', () => {
			const url = 'https://example.com/responses/responses';
			const result = rewriteUrlForCodex(url);
			expect(result).toBe('https://example.com/codex/responses/responses');
		});
	});

		describe('createCodexHeaders', () => {
	const accountId = 'test-account-123';
	const accessToken = 'test-access-token';

		it('should create headers with all required fields when cache key provided', () => {
	    const headers = createCodexHeaders(undefined, accountId, accessToken, { model: 'gpt-5-codex', promptCacheKey: 'session-1' });

	    expect(headers.get('Authorization')).toBe(`Bearer ${accessToken}`);
	    expect(headers.get(OPENAI_HEADERS.ACCOUNT_ID)).toBe(accountId);
	    expect(headers.get(OPENAI_HEADERS.BETA)).toBe(OPENAI_HEADER_VALUES.BETA_RESPONSES);
	    expect(headers.get(OPENAI_HEADERS.ORIGINATOR)).toBe(OPENAI_HEADER_VALUES.ORIGINATOR_CODEX);
	    expect(headers.get(OPENAI_HEADERS.SESSION_ID)).toBe('session-1');
	    expect(headers.get(OPENAI_HEADERS.CONVERSATION_ID)).toBe('session-1');
	    expect(headers.get('accept')).toBe('text/event-stream');
    });

		it('maps usage-limit 404 errors to 429', async () => {
			const body = {
				error: {
					code: 'usage_limit_reached',
					message: 'limit reached',
				},
			};
			const resp = new Response(JSON.stringify(body), { status: 404 });
			const mapped = await handleErrorResponse(resp);
			expect(mapped.status).toBe(429);
			const json = await mapped.json() as any;
			expect(json.error.code).toBe('usage_limit_reached');
		});

		it('leaves non-usage 404 errors unchanged', async () => {
			const body = { error: { code: 'not_found', message: 'nope' } };
			const resp = new Response(JSON.stringify(body), { status: 404 });
			const result = await handleErrorResponse(resp);
			expect(result.status).toBe(404);
			const json = await result.json() as any;
			expect(json.error.code).toBe('not_found');
		});

		it('should remove x-api-key header', () => {
        const init = { headers: { 'x-api-key': 'should-be-removed' } } as any;
        const headers = createCodexHeaders(init, accountId, accessToken, { model: 'gpt-5', promptCacheKey: 'session-2' });

			expect(headers.has('x-api-key')).toBe(false);
		});

		it('should preserve other existing headers', () => {
        const init = { headers: { 'Content-Type': 'application/json' } } as any;
        const headers = createCodexHeaders(init, accountId, accessToken, { model: 'gpt-5', promptCacheKey: 'session-3' });

			expect(headers.get('Content-Type')).toBe('application/json');
		});

		it('should use provided promptCacheKey for both conversation_id and session_id', () => {
			const key = 'ses_abc123';
			const headers = createCodexHeaders(undefined, accountId, accessToken, { promptCacheKey: key });
			expect(headers.get(OPENAI_HEADERS.CONVERSATION_ID)).toBe(key);
			expect(headers.get(OPENAI_HEADERS.SESSION_ID)).toBe(key);
		});

		it('does not set conversation/session headers when no promptCacheKey provided', () => {
			const headers = createCodexHeaders(undefined, accountId, accessToken, { model: 'gpt-5' });
			expect(headers.get(OPENAI_HEADERS.CONVERSATION_ID)).toBeNull();
			expect(headers.get(OPENAI_HEADERS.SESSION_ID)).toBeNull();
		});
    });
});
```

## File: `test/install-script.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, writeFileSync, readFileSync, mkdirSync, existsSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { parse } from 'jsonc-parser';

const SCRIPT_PATH = resolve(process.cwd(), 'scripts', 'install-opencode-codex-auth.js');

const runInstaller = (args: string[], homeDir: string) => {
	execFileSync(process.execPath, [SCRIPT_PATH, ...args], {
		env: { ...process.env, HOME: homeDir },
		stdio: 'pipe',
	});
};

const readJsoncFile = (path: string) => {
	const content = readFileSync(path, 'utf-8');
	return { content, data: parse(content) as Record<string, any> };
};

const makeHome = () => mkdtempSync(join(tmpdir(), 'opencode-install-'));

const writeConfig = (homeDir: string, file: string, content: string) => {
	const configDir = join(homeDir, '.config', 'opencode');
	mkdirSync(configDir, { recursive: true });
	const path = join(configDir, file);
	writeFileSync(path, content);
	return path;
};

describe('Install script', () => {
	it('updates existing JSONC and preserves comments', () => {
		const homeDir = makeHome();
		const configPath = writeConfig(
			homeDir,
			'opencode.jsonc',
			`{
  // My existing config
  "plugin": ["some-other-plugin@1.2.3", "opencode-openai-codex-auth@4.2.0"],
  "provider": {
    "openai": {
      "timeout": 60000,
      "models": { "custom-model": { "name": "Custom" } }
    }
  }
}`,
		);

		runInstaller(['--no-cache-clear'], homeDir);

		const { content, data } = readJsoncFile(configPath);
		expect(content).toContain('// My existing config');
		expect(data.plugin).toContain('opencode-openai-codex-auth');
		expect(data.plugin).toContain('some-other-plugin@1.2.3');
		expect(data.provider.openai.timeout).toBe(60000);
		expect(data.provider.openai.models['custom-model']).toBeDefined();
		expect(data.provider.openai.models['gpt-5.2']).toBeDefined();
	});

	it('prefers JSONC when both jsonc and json exist', () => {
		const homeDir = makeHome();
		const jsoncPath = writeConfig(
			homeDir,
			'opencode.jsonc',
			`{ "plugin": ["opencode-openai-codex-auth@4.2.0"] }`,
		);
		const jsonPath = writeConfig(
			homeDir,
			'opencode.json',
			`{ "plugin": ["should-stay"], "provider": { "openai": { "timeout": 10 } } }`,
		);
		const jsonBefore = readFileSync(jsonPath, 'utf-8');

		runInstaller(['--no-cache-clear'], homeDir);

		const { data } = readJsoncFile(jsoncPath);
		expect(data.plugin).toContain('opencode-openai-codex-auth');
		const jsonAfter = readFileSync(jsonPath, 'utf-8');
		expect(jsonAfter).toBe(jsonBefore);
	});

	it('creates JSONC when no config exists', () => {
		const homeDir = makeHome();
		runInstaller(['--no-cache-clear'], homeDir);
		const configPath = join(homeDir, '.config', 'opencode', 'opencode.jsonc');
		expect(existsSync(configPath)).toBe(true);
		const { data } = readJsoncFile(configPath);
		expect(data.plugin).toContain('opencode-openai-codex-auth');
	});

	it('uninstall removes plugin models but keeps custom config', () => {
		const homeDir = makeHome();
		const configPath = writeConfig(
			homeDir,
			'opencode.jsonc',
			`{
  "plugin": ["some-other-plugin@1.2.3", "opencode-openai-codex-auth@4.2.0"],
  "provider": {
    "openai": {
      "timeout": 60000,
      "models": {
        "custom-model": { "name": "Custom" },
        "gpt-5.2": { "name": "GPT 5.2 (OAuth)" },
        "gpt-5.2-codex": { "name": "GPT 5.2 Codex (OAuth)" }
      }
    },
    "anthropic": { "models": { "claude": { "name": "Claude" } } }
  }
}`,
		);

		runInstaller(['--uninstall', '--no-cache-clear'], homeDir);

		const { data } = readJsoncFile(configPath);
		expect(data.plugin).toEqual(['some-other-plugin@1.2.3']);
		expect(data.provider.openai.timeout).toBe(60000);
		expect(data.provider.openai.models['custom-model']).toBeDefined();
		expect(data.provider.openai.models['gpt-5.2']).toBeUndefined();
		expect(data.provider.openai.models['gpt-5.2-codex']).toBeUndefined();
		expect(data.provider.anthropic).toBeDefined();
	});

	it('uninstall --all removes plugin artifacts', () => {
		const homeDir = makeHome();
		writeConfig(
			homeDir,
			'opencode.jsonc',
			`{ "plugin": ["opencode-openai-codex-auth@4.2.0"] }`,
		);

		const opencodeDir = join(homeDir, '.opencode');
		mkdirSync(join(opencodeDir, 'auth'), { recursive: true });
		mkdirSync(join(opencodeDir, 'logs', 'codex-plugin'), { recursive: true });
		mkdirSync(join(opencodeDir, 'cache'), { recursive: true });
		writeFileSync(join(opencodeDir, 'auth', 'openai.json'), '{}');
		writeFileSync(join(opencodeDir, 'openai-codex-auth-config.json'), '{}');
		writeFileSync(join(opencodeDir, 'logs', 'codex-plugin', 'log.txt'), 'log');
		writeFileSync(join(opencodeDir, 'cache', 'codex-instructions.md'), 'cache');

		runInstaller(['--uninstall', '--all', '--no-cache-clear'], homeDir);

		expect(existsSync(join(opencodeDir, 'auth', 'openai.json'))).toBe(false);
		expect(existsSync(join(opencodeDir, 'openai-codex-auth-config.json'))).toBe(false);
		expect(existsSync(join(opencodeDir, 'logs', 'codex-plugin'))).toBe(false);
		expect(existsSync(join(opencodeDir, 'cache', 'codex-instructions.md'))).toBe(false);
	});
});
```

## File: `test/logger.test.ts`
```typescript
import { describe, it, expect } from 'vitest';
import { LOGGING_ENABLED, logRequest } from '../lib/logger.js';

describe('Logger Module', () => {
	describe('LOGGING_ENABLED constant', () => {
		it('should be a boolean', () => {
			expect(typeof LOGGING_ENABLED).toBe('boolean');
		});

		it('should default to false when env variable is not set', () => {
			// This test verifies the default behavior
			// In a real test environment, ENABLE_PLUGIN_REQUEST_LOGGING would not be set
			const isEnabled = process.env.ENABLE_PLUGIN_REQUEST_LOGGING === '1';
			expect(typeof isEnabled).toBe('boolean');
		});
	});

	describe('logRequest function', () => {
		it('should accept stage and data parameters', () => {
			// This should not throw
			expect(() => {
				logRequest('test-stage', { data: 'test' });
			}).not.toThrow();
		});

		it('should handle empty data object', () => {
			expect(() => {
				logRequest('test-stage', {});
			}).not.toThrow();
		});

		it('should handle complex data structures', () => {
			expect(() => {
				logRequest('test-stage', {
					nested: { data: 'value' },
					array: [1, 2, 3],
					number: 123,
					boolean: true,
				});
			}).not.toThrow();
		});
	});
});
```

## File: `test/plugin-config.test.ts`
```typescript
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { loadPluginConfig, getCodexMode } from '../lib/config.js';
import type { PluginConfig } from '../lib/types.js';
import * as fs from 'node:fs';
import * as os from 'node:os';
import * as path from 'node:path';

// Mock the fs module
vi.mock('node:fs', async () => {
	const actual = await vi.importActual<typeof import('node:fs')>('node:fs');
	return {
		...actual,
		existsSync: vi.fn(),
		readFileSync: vi.fn(),
	};
});

describe('Plugin Configuration', () => {
	const mockExistsSync = vi.mocked(fs.existsSync);
	const mockReadFileSync = vi.mocked(fs.readFileSync);
	let originalEnv: string | undefined;

	beforeEach(() => {
		originalEnv = process.env.CODEX_MODE;
		vi.clearAllMocks();
	});

	afterEach(() => {
		if (originalEnv === undefined) {
			delete process.env.CODEX_MODE;
		} else {
			process.env.CODEX_MODE = originalEnv;
		}
	});

	describe('loadPluginConfig', () => {
		it('should return default config when file does not exist', () => {
			mockExistsSync.mockReturnValue(false);

			const config = loadPluginConfig();

			expect(config).toEqual({ codexMode: true });
			expect(mockExistsSync).toHaveBeenCalledWith(
				path.join(os.homedir(), '.opencode', 'openai-codex-auth-config.json')
			);
		});

		it('should load config from file when it exists', () => {
			mockExistsSync.mockReturnValue(true);
			mockReadFileSync.mockReturnValue(JSON.stringify({ codexMode: false }));

			const config = loadPluginConfig();

			expect(config).toEqual({ codexMode: false });
		});

		it('should merge user config with defaults', () => {
			mockExistsSync.mockReturnValue(true);
			mockReadFileSync.mockReturnValue(JSON.stringify({}));

			const config = loadPluginConfig();

			expect(config).toEqual({ codexMode: true });
		});

		it('should handle invalid JSON gracefully', () => {
			mockExistsSync.mockReturnValue(true);
			mockReadFileSync.mockReturnValue('invalid json');

			const consoleSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
			const config = loadPluginConfig();

			expect(config).toEqual({ codexMode: true });
			expect(consoleSpy).toHaveBeenCalled();
			consoleSpy.mockRestore();
		});

		it('should handle file read errors gracefully', () => {
			mockExistsSync.mockReturnValue(true);
			mockReadFileSync.mockImplementation(() => {
				throw new Error('Permission denied');
			});

			const consoleSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});
			const config = loadPluginConfig();

			expect(config).toEqual({ codexMode: true });
			expect(consoleSpy).toHaveBeenCalled();
			consoleSpy.mockRestore();
		});
	});

	describe('getCodexMode', () => {
		it('should return true by default', () => {
			delete process.env.CODEX_MODE;
			const config: PluginConfig = {};

			const result = getCodexMode(config);

			expect(result).toBe(true);
		});

		it('should use config value when env var not set', () => {
			delete process.env.CODEX_MODE;
			const config: PluginConfig = { codexMode: false };

			const result = getCodexMode(config);

			expect(result).toBe(false);
		});

		it('should prioritize env var CODEX_MODE=1 over config', () => {
			process.env.CODEX_MODE = '1';
			const config: PluginConfig = { codexMode: false };

			const result = getCodexMode(config);

			expect(result).toBe(true);
		});

		it('should prioritize env var CODEX_MODE=0 over config', () => {
			process.env.CODEX_MODE = '0';
			const config: PluginConfig = { codexMode: true };

			const result = getCodexMode(config);

			expect(result).toBe(false);
		});

		it('should handle env var with any value other than "1" as false', () => {
			process.env.CODEX_MODE = 'false';
			const config: PluginConfig = { codexMode: true };

			const result = getCodexMode(config);

			expect(result).toBe(false);
		});

		it('should use config codexMode=true when explicitly set', () => {
			delete process.env.CODEX_MODE;
			const config: PluginConfig = { codexMode: true };

			const result = getCodexMode(config);

			expect(result).toBe(true);
		});
	});

	describe('Priority order', () => {
		it('should follow priority: env var > config file > default', () => {
			// Test 1: env var overrides config
			process.env.CODEX_MODE = '0';
			expect(getCodexMode({ codexMode: true })).toBe(false);

			// Test 2: config overrides default
			delete process.env.CODEX_MODE;
			expect(getCodexMode({ codexMode: false })).toBe(false);

			// Test 3: default when neither set
			expect(getCodexMode({})).toBe(true);
		});
	});
});
```

## File: `test/request-transformer.test.ts`
```typescript
import { describe, it, expect, beforeEach, afterEach } from 'vitest';
import {
    normalizeModel,
    getModelConfig,
    filterInput,
    addToolRemapMessage,
    isOpenCodeSystemPrompt,
    filterOpenCodeSystemPrompts,
    filterOpenCodeSystemPromptsWithCachedPrompt,
    addCodexBridgeMessage,
    transformRequestBody,
} from '../lib/request/request-transformer.js';
import { TOOL_REMAP_MESSAGE } from '../lib/prompts/codex.js';
import { CODEX_OPENCODE_BRIDGE } from '../lib/prompts/codex-opencode-bridge.js';
import type { RequestBody, UserConfig, InputItem } from '../lib/types.js';

describe('Request Transformer Module', () => {
	describe('normalizeModel', () => {
		// NOTE: All gpt-5 models now normalize to gpt-5.1 as gpt-5 is being phased out
		it('should normalize gpt-5-codex to gpt-5.1-codex', async () => {
			expect(normalizeModel('gpt-5-codex')).toBe('gpt-5.1-codex');
		});

		it('should normalize gpt-5 to gpt-5.1', async () => {
			expect(normalizeModel('gpt-5')).toBe('gpt-5.1');
		});

		it('should normalize variants containing "codex" to gpt-5.1-codex', async () => {
			expect(normalizeModel('openai/gpt-5-codex')).toBe('gpt-5.1-codex');
			expect(normalizeModel('custom-gpt-5-codex-variant')).toBe('gpt-5.1-codex');
		});

		it('should normalize variants containing "gpt-5" to gpt-5.1', async () => {
			expect(normalizeModel('gpt-5-mini')).toBe('gpt-5.1');
			expect(normalizeModel('gpt-5-nano')).toBe('gpt-5.1');
		});

		it('should return gpt-5.1 as default for unknown models', async () => {
			expect(normalizeModel('unknown-model')).toBe('gpt-5.1');
			expect(normalizeModel('gpt-4')).toBe('gpt-5.1');
		});

		it('should return gpt-5.1 for undefined', async () => {
			expect(normalizeModel(undefined)).toBe('gpt-5.1');
		});

		// Codex CLI preset name tests - legacy gpt-5 models now map to gpt-5.1
		describe('Codex CLI preset names', () => {
			it('should normalize all gpt-5-codex presets to gpt-5.1-codex', async () => {
				expect(normalizeModel('gpt-5-codex-low')).toBe('gpt-5.1-codex');
				expect(normalizeModel('gpt-5-codex-medium')).toBe('gpt-5.1-codex');
				expect(normalizeModel('gpt-5-codex-high')).toBe('gpt-5.1-codex');
			});

			it('should normalize all gpt-5 presets to gpt-5.1', async () => {
				expect(normalizeModel('gpt-5-minimal')).toBe('gpt-5.1');
				expect(normalizeModel('gpt-5-low')).toBe('gpt-5.1');
				expect(normalizeModel('gpt-5-medium')).toBe('gpt-5.1');
				expect(normalizeModel('gpt-5-high')).toBe('gpt-5.1');
			});

			it('should prioritize codex over gpt-5 in model name', async () => {
				// Model name contains BOTH "codex" and "gpt-5"
				// Should return "gpt-5.1-codex" (codex checked first, maps to 5.1)
				expect(normalizeModel('gpt-5-codex-low')).toBe('gpt-5.1-codex');
				expect(normalizeModel('my-gpt-5-codex-model')).toBe('gpt-5.1-codex');
			});

			it('should normalize codex mini presets to gpt-5.1-codex-mini', async () => {
				expect(normalizeModel('gpt-5-codex-mini')).toBe('gpt-5.1-codex-mini');
				expect(normalizeModel('gpt-5-codex-mini-medium')).toBe('gpt-5.1-codex-mini');
				expect(normalizeModel('gpt-5-codex-mini-high')).toBe('gpt-5.1-codex-mini');
				expect(normalizeModel('openai/gpt-5-codex-mini-high')).toBe('gpt-5.1-codex-mini');
				expect(normalizeModel('codex-mini-latest')).toBe('gpt-5.1-codex-mini');
				expect(normalizeModel('openai/codex-mini-latest')).toBe('gpt-5.1-codex-mini');
			});

			it('should normalize gpt-5.1 codex max presets', async () => {
				expect(normalizeModel('gpt-5.1-codex-max')).toBe('gpt-5.1-codex-max');
				expect(normalizeModel('gpt-5.1-codex-max-high')).toBe('gpt-5.1-codex-max');
				expect(normalizeModel('gpt-5.1-codex-max-xhigh')).toBe('gpt-5.1-codex-max');
				expect(normalizeModel('openai/gpt-5.1-codex-max-medium')).toBe('gpt-5.1-codex-max');
			});

			it('should normalize gpt-5.2 codex presets', async () => {
				expect(normalizeModel('gpt-5.2-codex')).toBe('gpt-5.2-codex');
				expect(normalizeModel('gpt-5.2-codex-low')).toBe('gpt-5.2-codex');
				expect(normalizeModel('gpt-5.2-codex-medium')).toBe('gpt-5.2-codex');
				expect(normalizeModel('gpt-5.2-codex-high')).toBe('gpt-5.2-codex');
				expect(normalizeModel('gpt-5.2-codex-xhigh')).toBe('gpt-5.2-codex');
				expect(normalizeModel('openai/gpt-5.2-codex-xhigh')).toBe('gpt-5.2-codex');
			});

			it('should normalize gpt-5.1 codex and mini slugs', async () => {
				expect(normalizeModel('gpt-5.1-codex')).toBe('gpt-5.1-codex');
				expect(normalizeModel('openai/gpt-5.1-codex')).toBe('gpt-5.1-codex');
				expect(normalizeModel('gpt-5.1-codex-mini')).toBe('gpt-5.1-codex-mini');
				expect(normalizeModel('gpt-5.1-codex-mini-high')).toBe('gpt-5.1-codex-mini');
				expect(normalizeModel('openai/gpt-5.1-codex-mini-medium')).toBe('gpt-5.1-codex-mini');
			});

			it('should normalize gpt-5.1 general-purpose slugs', async () => {
				expect(normalizeModel('gpt-5.1')).toBe('gpt-5.1');
				expect(normalizeModel('openai/gpt-5.1')).toBe('gpt-5.1');
				expect(normalizeModel('GPT 5.1 High')).toBe('gpt-5.1');
			});
		});

		// Edge case tests - legacy gpt-5 models now map to gpt-5.1
		describe('Edge cases', () => {
			it('should handle uppercase model names', async () => {
				expect(normalizeModel('GPT-5-CODEX')).toBe('gpt-5.1-codex');
				expect(normalizeModel('GPT-5-HIGH')).toBe('gpt-5.1');
				expect(normalizeModel('CODEx-MINI-LATEST')).toBe('gpt-5.1-codex-mini');
			});

			it('should handle mixed case', async () => {
				expect(normalizeModel('Gpt-5-Codex-Low')).toBe('gpt-5.1-codex');
				expect(normalizeModel('GpT-5-MeDiUm')).toBe('gpt-5.1');
			});

			it('should handle special characters', async () => {
				expect(normalizeModel('my_gpt-5_codex')).toBe('gpt-5.1-codex');
				expect(normalizeModel('gpt.5.high')).toBe('gpt-5.1');
			});

			it('should handle old verbose names', async () => {
				expect(normalizeModel('GPT 5 Codex Low (ChatGPT Subscription)')).toBe('gpt-5.1-codex');
				expect(normalizeModel('GPT 5 High (ChatGPT Subscription)')).toBe('gpt-5.1');
			});

			it('should handle empty string', async () => {
				expect(normalizeModel('')).toBe('gpt-5.1');
			});
		});
	});

	describe('getModelConfig', () => {
		describe('Per-model options (Bug Fix Verification)', () => {
			it('should find per-model options using config key', async () => {
				const userConfig: UserConfig = {
					global: { reasoningEffort: 'medium' },
					models: {
						'gpt-5-codex-low': {
							options: { reasoningEffort: 'low', textVerbosity: 'low' }
						}
					}
				};

				const result = getModelConfig('gpt-5-codex-low', userConfig);
				expect(result.reasoningEffort).toBe('low');
				expect(result.textVerbosity).toBe('low');
			});

			it('should merge global and per-model options (per-model wins)', async () => {
				const userConfig: UserConfig = {
					global: {
						reasoningEffort: 'medium',
						textVerbosity: 'medium',
						include: ['reasoning.encrypted_content']
					},
					models: {
						'gpt-5-codex-high': {
							options: { reasoningEffort: 'high' }  // Override only effort
						}
					}
				};

				const result = getModelConfig('gpt-5-codex-high', userConfig);
				expect(result.reasoningEffort).toBe('high');  // From per-model
				expect(result.textVerbosity).toBe('medium');  // From global
				expect(result.include).toEqual(['reasoning.encrypted_content']);  // From global
			});

			it('should return global options when model not in config', async () => {
				const userConfig: UserConfig = {
					global: { reasoningEffort: 'medium' },
					models: {
						'gpt-5-codex-low': { options: { reasoningEffort: 'low' } }
					}
				};

				// Looking up different model
				const result = getModelConfig('gpt-5-codex', userConfig);
				expect(result.reasoningEffort).toBe('medium');  // Global only
			});

			it('should handle empty config', async () => {
				const result = getModelConfig('gpt-5-codex', { global: {}, models: {} });
				expect(result).toEqual({});
			});

			it('should handle missing models object', async () => {
				const userConfig: UserConfig = {
					global: { reasoningEffort: 'low' },
					models: undefined as any
				};
				const result = getModelConfig('gpt-5', userConfig);
				expect(result.reasoningEffort).toBe('low');
			});
		});

		describe('Backwards compatibility', () => {
			it('should work with old verbose config keys', async () => {
				const userConfig: UserConfig = {
					global: {},
					models: {
						'GPT 5 Codex Low (ChatGPT Subscription)': {
							options: { reasoningEffort: 'low' }
						}
					}
				};

				const result = getModelConfig('GPT 5 Codex Low (ChatGPT Subscription)', userConfig);
				expect(result.reasoningEffort).toBe('low');
			});

			it('should work with old configs that have id field', async () => {
				const userConfig: UserConfig = {
					global: {},
					models: {
						'gpt-5-codex-low': {
							id: 'gpt-5-codex',  // id field present but should be ignored
							options: { reasoningEffort: 'low' }
						}
					}
				};

				const result = getModelConfig('gpt-5-codex-low', userConfig);
				expect(result.reasoningEffort).toBe('low');
			});
		});

		describe('Default models (no custom config)', () => {
			it('should return global options for default gpt-5-codex', async () => {
				const userConfig: UserConfig = {
					global: { reasoningEffort: 'high' },
					models: {}
				};

				const result = getModelConfig('gpt-5-codex', userConfig);
				expect(result.reasoningEffort).toBe('high');
			});

			it('should return empty when no config at all', async () => {
				const result = getModelConfig('gpt-5', undefined);
				expect(result).toEqual({});
			});
		});
	});

	describe('filterInput', () => {
		it('should keep items without IDs unchanged', async () => {
			const input: InputItem[] = [
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = filterInput(input);
			expect(result).toEqual(input);
			expect(result![0]).not.toHaveProperty('id');
		});

		it('should remove ALL message IDs (rs_, msg_, etc.) for store:false compatibility', async () => {
			const input: InputItem[] = [
				{ id: 'rs_123', type: 'message', role: 'assistant', content: 'hello' },
				{ id: 'msg_456', type: 'message', role: 'user', content: 'world' },
				{ id: 'assistant_789', type: 'message', role: 'assistant', content: 'test' },
			];
			const result = filterInput(input);

			// All items should remain (no filtering), but ALL IDs removed
			expect(result).toHaveLength(3);
			expect(result![0]).not.toHaveProperty('id');
			expect(result![1]).not.toHaveProperty('id');
			expect(result![2]).not.toHaveProperty('id');
			expect(result![0].content).toBe('hello');
			expect(result![1].content).toBe('world');
			expect(result![2].content).toBe('test');
		});

		it('should strip ID field but preserve all other properties', async () => {
			const input: InputItem[] = [
				{
					id: 'msg_123',
					type: 'message',
					role: 'user',
					content: 'test',
					metadata: { some: 'data' }
				},
			];
			const result = filterInput(input);

			expect(result).toHaveLength(1);
			expect(result![0]).not.toHaveProperty('id');
			expect(result![0].type).toBe('message');
			expect(result![0].role).toBe('user');
			expect(result![0].content).toBe('test');
			expect(result![0]).toHaveProperty('metadata');
		});

		it('should handle mixed items with and without IDs', async () => {
			const input: InputItem[] = [
				{ type: 'message', role: 'user', content: '1' },
				{ id: 'rs_stored', type: 'message', role: 'assistant', content: '2' },
				{ id: 'msg_123', type: 'message', role: 'user', content: '3' },
			];
			const result = filterInput(input);

			// All items kept, IDs removed from items that had them
			expect(result).toHaveLength(3);
			expect(result![0]).not.toHaveProperty('id');
			expect(result![1]).not.toHaveProperty('id');
			expect(result![2]).not.toHaveProperty('id');
			expect(result![0].content).toBe('1');
			expect(result![1].content).toBe('2');
			expect(result![2].content).toBe('3');
		});

		it('should handle custom ID formats (future-proof)', async () => {
			const input: InputItem[] = [
				{ id: 'custom_id_format', type: 'message', role: 'user', content: 'test' },
				{ id: 'another-format-123', type: 'message', role: 'user', content: 'test2' },
			];
			const result = filterInput(input);

			expect(result).toHaveLength(2);
			expect(result![0]).not.toHaveProperty('id');
			expect(result![1]).not.toHaveProperty('id');
		});

		it('should return undefined for undefined input', async () => {
			expect(filterInput(undefined)).toBeUndefined();
		});

		it('should return non-array input as-is', async () => {
			const notArray = { notAnArray: true };
			expect(filterInput(notArray as any)).toBe(notArray);
		});

		it('should handle empty array', async () => {
			const input: InputItem[] = [];
			const result = filterInput(input);
			expect(result).toEqual([]);
		});
	});

	describe('addToolRemapMessage', () => {
		it('should prepend tool remap message when tools present', async () => {
			const input: InputItem[] = [
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = addToolRemapMessage(input, true);

			expect(result).toHaveLength(2);
			expect(result![0].role).toBe('developer');
			expect(result![0].type).toBe('message');
			expect((result![0].content as any)[0].text).toContain('apply_patch');
		});

		it('should not modify input when tools not present', async () => {
			const input: InputItem[] = [
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = addToolRemapMessage(input, false);
			expect(result).toEqual(input);
		});

		it('should return undefined for undefined input', async () => {
			expect(addToolRemapMessage(undefined, true)).toBeUndefined();
		});

		it('should handle non-array input', async () => {
			const notArray = { notAnArray: true };
			expect(addToolRemapMessage(notArray as any, true)).toBe(notArray);
		});
	});

	describe('isOpenCodeSystemPrompt', () => {
		it('should detect OpenCode system prompt with string content', async () => {
			const item: InputItem = {
				type: 'message',
				role: 'developer',
				content: 'You are a coding agent running in the opencode, a terminal-based coding assistant.',
			};
			expect(isOpenCodeSystemPrompt(item, null)).toBe(true);
		});

		it('should detect OpenCode system prompt with array content', async () => {
			const item: InputItem = {
				type: 'message',
				role: 'developer',
				content: [
					{
						type: 'input_text',
						text: 'You are a coding agent running in the opencode, a terminal-based coding assistant.',
					},
				],
			};
			expect(isOpenCodeSystemPrompt(item, null)).toBe(true);
		});

		it('should detect with system role', async () => {
			const item: InputItem = {
				type: 'message',
				role: 'system',
				content: 'You are a coding agent running in the opencode, a terminal-based coding assistant.',
			};
			expect(isOpenCodeSystemPrompt(item, null)).toBe(true);
		});

		it('should not detect non-system roles', async () => {
			const item: InputItem = {
				type: 'message',
				role: 'user',
				content: 'You are a coding agent running in the opencode, a terminal-based coding assistant.',
			};
			expect(isOpenCodeSystemPrompt(item, null)).toBe(false);
		});

		it('should not detect different content', async () => {
			const item: InputItem = {
				type: 'message',
				role: 'developer',
				content: 'Different message',
			};
			expect(isOpenCodeSystemPrompt(item, null)).toBe(false);
		});

		it('should NOT detect AGENTS.md content', async () => {
			const item: InputItem = {
				type: 'message',
				role: 'developer',
				content: '# Project Guidelines\n\nThis is custom AGENTS.md content for the project.',
			};
			expect(isOpenCodeSystemPrompt(item, null)).toBe(false);
		});

		it('should NOT detect environment info concatenated with AGENTS.md', async () => {
			const item: InputItem = {
				type: 'message',
				role: 'developer',
				content: 'Environment: /path/to/project\nDate: 2025-01-01\n\n# AGENTS.md\n\nCustom instructions here.',
			};
			expect(isOpenCodeSystemPrompt(item, null)).toBe(false);
		});

		it('should NOT detect content with codex signature in the middle', async () => {
			const cachedPrompt = 'You are a coding agent running in the opencode.';
			const item: InputItem = {
				type: 'message',
				role: 'developer',
				// Has codex.txt content but with environment prepended (like OpenCode does)
				content: 'Environment info here\n\nYou are a coding agent running in the opencode.',
			};
			// First 200 chars won't match because of prepended content
			expect(isOpenCodeSystemPrompt(item, cachedPrompt)).toBe(false);
		});

		it('should detect with cached prompt exact match', async () => {
			const cachedPrompt = 'You are a coding agent running in the opencode';
			const item: InputItem = {
				type: 'message',
				role: 'developer',
				content: 'You are a coding agent running in the opencode',
			};
			expect(isOpenCodeSystemPrompt(item, cachedPrompt)).toBe(true);
		});

		it('should detect alternative OpenCode prompt signatures', async () => {
			const item: InputItem = {
				type: 'message',
				role: 'developer',
				content: "You are opencode, an agent - please keep going until the user's query is completely resolved.",
			};
			expect(isOpenCodeSystemPrompt(item, null)).toBe(true);
		});
	});

	describe('filterOpenCodeSystemPrompts', () => {
		it('should filter out OpenCode system prompts', async () => {
			const input: InputItem[] = [
				{
					type: 'message',
					role: 'developer',
					content: 'You are a coding agent running in the opencode',
				},
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = filterOpenCodeSystemPromptsWithCachedPrompt(input, null);
			expect(result).toHaveLength(1);
			expect(result![0].role).toBe('user');
		});

		it('should keep user messages', async () => {
			const input: InputItem[] = [
				{ type: 'message', role: 'user', content: 'message 1' },
				{ type: 'message', role: 'user', content: 'message 2' },
			];
			const result = filterOpenCodeSystemPromptsWithCachedPrompt(input, null);
			expect(result).toHaveLength(2);
		});

		it('should keep non-OpenCode developer messages', async () => {
			const input: InputItem[] = [
				{ type: 'message', role: 'developer', content: 'Custom instruction' },
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = filterOpenCodeSystemPromptsWithCachedPrompt(input, null);
			expect(result).toHaveLength(2);
		});

		it('should keep AGENTS.md content (not filter it)', async () => {
			const input: InputItem[] = [
				{
					type: 'message',
					role: 'developer',
					content: 'You are a coding agent running in the opencode', // This is codex.txt
				},
				{
					type: 'message',
					role: 'developer',
					content: '# Project Guidelines\n\nThis is AGENTS.md content.', // This is AGENTS.md
				},
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = filterOpenCodeSystemPromptsWithCachedPrompt(input, null);
			// Should filter codex.txt but keep AGENTS.md
			expect(result).toHaveLength(2);
			expect(result![0].content).toContain('AGENTS.md');
			expect(result![1].role).toBe('user');
		});

		it('should strip OpenCode prompt but keep concatenated env/instructions', async () => {
			const input: InputItem[] = [
				{
					type: 'message',
					role: 'developer',
					content: [
						'You are a coding agent running in the opencode, a terminal-based coding assistant.',
						'Here is some useful information about the environment you are running in:',
						'<env>',
						'  Working directory: /path/to/project',
						'</env>',
						'Instructions from: /path/to/AGENTS.md',
						'# Project Guidelines',
					].join('\n'),
				},
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = filterOpenCodeSystemPromptsWithCachedPrompt(input, null);
			expect(result).toHaveLength(2);
			const preserved = String(result![0].content);
			expect(preserved).toContain('Here is some useful information about the environment');
			expect(preserved).toContain('Instructions from: /path/to/AGENTS.md');
			expect(preserved).not.toContain('You are a coding agent running in the opencode');
		});

		it('should keep environment+AGENTS.md concatenated message', async () => {
			const input: InputItem[] = [
				{
					type: 'message',
					role: 'developer',
					content: 'You are a coding agent running in the opencode', // codex.txt alone
				},
				{
					type: 'message',
					role: 'developer',
					// environment + AGENTS.md joined (like OpenCode does)
					content: 'Working directory: /path/to/project\nDate: 2025-01-01\n\n# AGENTS.md\n\nCustom instructions.',
				},
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = filterOpenCodeSystemPromptsWithCachedPrompt(input, null);
			// Should filter first message (codex.txt) but keep second (env+AGENTS.md)
			expect(result).toHaveLength(2);
			expect(result![0].content).toContain('AGENTS.md');
			expect(result![1].role).toBe('user');
		});

		it('should return undefined for undefined input', async () => {
			expect(await filterOpenCodeSystemPrompts(undefined)).toBeUndefined();
		});
	});

	describe('addCodexBridgeMessage', () => {
		it('should prepend bridge message when tools present', async () => {
			const input: InputItem[] = [
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = addCodexBridgeMessage(input, true);

			expect(result).toHaveLength(2);
			expect(result![0].role).toBe('developer');
			expect(result![0].type).toBe('message');
			expect((result![0].content as any)[0].text).toContain('Codex Running in OpenCode');
		});

		it('should not modify input when tools not present', async () => {
			const input: InputItem[] = [
				{ type: 'message', role: 'user', content: 'hello' },
			];
			const result = addCodexBridgeMessage(input, false);
			expect(result).toEqual(input);
		});

		it('should return undefined for undefined input', async () => {
			expect(addCodexBridgeMessage(undefined, true)).toBeUndefined();
		});
	});

		describe('transformRequestBody', () => {
			const codexInstructions = 'Test Codex Instructions';

			it('preserves existing prompt_cache_key passed by host (OpenCode)', async () => {
				const body: RequestBody = {
					model: 'gpt-5-codex',
					input: [],
					// Host-provided key (OpenCode session id)
					// @ts-expect-error extra field allowed
					prompt_cache_key: 'ses_host_key_123',
				};
				const result: any = await transformRequestBody(body, codexInstructions);
				expect(result.prompt_cache_key).toBe('ses_host_key_123');
			});

			it('leaves prompt_cache_key unset when host does not supply one', async () => {
				const body: RequestBody = {
					model: 'gpt-5',
					input: [],
				};
				const result: any = await transformRequestBody(body, codexInstructions);
				expect(result.prompt_cache_key).toBeUndefined();
			});

		it('should set required Codex fields', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
			};
			const result = await transformRequestBody(body, codexInstructions);

			expect(result.store).toBe(false);
			expect(result.stream).toBe(true);
			expect(result.instructions).toBe(codexInstructions);
		});

		it('should normalize model name', async () => {
			const body: RequestBody = {
				model: 'gpt-5-mini',
				input: [],
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.model).toBe('gpt-5.1');  // gpt-5 now maps to gpt-5.1
		});

		it('should apply default reasoning config', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
			};
			const result = await transformRequestBody(body, codexInstructions);

			expect(result.reasoning?.effort).toBe('medium');
			expect(result.reasoning?.summary).toBe('auto');
		});

		it('should apply user reasoning config', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
			};
			const userConfig: UserConfig = {
				global: {
					reasoningEffort: 'high',
					reasoningSummary: 'detailed',
				},
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);

			expect(result.reasoning?.effort).toBe('high');
			expect(result.reasoning?.summary).toBe('detailed');
		});

		it('should respect reasoning config already set in body', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
				reasoning: {
					effort: 'low',
					summary: 'auto',
				},
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'high', reasoningSummary: 'detailed' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);

			expect(result.reasoning?.effort).toBe('low');
			expect(result.reasoning?.summary).toBe('auto');
		});

		it('should use reasoning config from providerOptions when present', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
				providerOptions: {
					openai: {
						reasoningEffort: 'high',
						reasoningSummary: 'detailed',
					},
				},
			};
			const result = await transformRequestBody(body, codexInstructions);

			expect(result.reasoning?.effort).toBe('high');
			expect(result.reasoning?.summary).toBe('detailed');
		});

		it('should apply default text verbosity', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.text?.verbosity).toBe('medium');
		});

		it('should apply user text verbosity', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { textVerbosity: 'low' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.text?.verbosity).toBe('low');
		});

		it('should use text verbosity from providerOptions when present', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
				providerOptions: {
					openai: {
						textVerbosity: 'low',
					},
				},
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.text?.verbosity).toBe('low');
		});

		it('should prefer body text verbosity over providerOptions', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
				text: { verbosity: 'high' },
				providerOptions: {
					openai: {
						textVerbosity: 'low',
					},
				},
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.text?.verbosity).toBe('high');
		});

		it('should set default include for encrypted reasoning', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.include).toEqual(['reasoning.encrypted_content']);
		});

		it('should use user-configured include', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { include: ['custom_field', 'reasoning.encrypted_content'] },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.include).toEqual(['custom_field', 'reasoning.encrypted_content']);
		});

		it('should always include reasoning.encrypted_content when include provided', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
				include: ['custom_field'],
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.include).toEqual(['custom_field', 'reasoning.encrypted_content']);
		});

		it('should remove IDs from input array (keep all items, strip IDs)', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [
					{ id: 'rs_123', type: 'message', role: 'assistant', content: 'old' },
					{ type: 'message', role: 'user', content: 'new' },
				],
			};
			const result = await transformRequestBody(body, codexInstructions);

			// All items kept, IDs removed
			expect(result.input).toHaveLength(2);
			expect(result.input![0]).not.toHaveProperty('id');
			expect(result.input![1]).not.toHaveProperty('id');
			expect(result.input![0].content).toBe('old');
			expect(result.input![1].content).toBe('new');
		});

		it('should add tool remap message when tools present', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [{ type: 'message', role: 'user', content: 'hello' }],
				tools: [{ name: 'test_tool' }],
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.input![0].role).toBe('developer');
		});

		it('should not add tool remap message when tools absent', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [{ type: 'message', role: 'user', content: 'hello' }],
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.input![0].role).toBe('user');
		});

		it('should remove unsupported parameters', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
				max_output_tokens: 1000,
				max_completion_tokens: 2000,
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.max_output_tokens).toBeUndefined();
			expect(result.max_completion_tokens).toBeUndefined();
		});

		it('should normalize minimal to low for gpt-5-codex', async () => {
			const body: RequestBody = {
				model: 'gpt-5-codex',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'minimal' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.reasoning?.effort).toBe('low');
		});

		it('should clamp xhigh to high for codex-mini', async () => {
			const body: RequestBody = {
				model: 'gpt-5.1-codex-mini-high',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'xhigh' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.reasoning?.effort).toBe('high');
		});

		it('should clamp none to medium for codex-mini', async () => {
			const body: RequestBody = {
				model: 'gpt-5.1-codex-mini-medium',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'none' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.reasoning?.effort).toBe('medium');
		});

		it('should default codex-max to high effort', async () => {
			const body: RequestBody = {
				model: 'gpt-5.1-codex-max',
				input: [],
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.reasoning?.effort).toBe('high');
		});

		it('should default gpt-5.2-codex to high effort', async () => {
			const body: RequestBody = {
				model: 'gpt-5.2-codex',
				input: [],
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.model).toBe('gpt-5.2-codex');
			expect(result.reasoning?.effort).toBe('high');
		});

		it('should preserve xhigh for codex-max when requested', async () => {
			const body: RequestBody = {
				model: 'gpt-5.1-codex-max-xhigh',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningSummary: 'auto' },
				models: {
					'gpt-5.1-codex-max-xhigh': {
						options: { reasoningEffort: 'xhigh', reasoningSummary: 'detailed' },
					},
				},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.1-codex-max');
			expect(result.reasoning?.effort).toBe('xhigh');
			expect(result.reasoning?.summary).toBe('detailed');
		});

		it('should preserve xhigh for gpt-5.2-codex when requested', async () => {
			const body: RequestBody = {
				model: 'gpt-5.2-codex-xhigh',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningSummary: 'auto' },
				models: {
					'gpt-5.2-codex-xhigh': {
						options: { reasoningEffort: 'xhigh', reasoningSummary: 'detailed' },
					},
				},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.2-codex');
			expect(result.reasoning?.effort).toBe('xhigh');
			expect(result.reasoning?.summary).toBe('detailed');
		});

		it('should downgrade xhigh to high for non-max codex', async () => {
			const body: RequestBody = {
				model: 'gpt-5.1-codex-high',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'xhigh' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.1-codex');
			expect(result.reasoning?.effort).toBe('high');
		});

		it('should downgrade xhigh to high for non-max general models', async () => {
			const body: RequestBody = {
				model: 'gpt-5.1-high',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'xhigh' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.1');
			expect(result.reasoning?.effort).toBe('high');
		});

		it('should preserve none for GPT-5.2', async () => {
			const body: RequestBody = {
				model: 'gpt-5.2-none',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'none' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.2');
			expect(result.reasoning?.effort).toBe('none');
		});

		it('should upgrade none to low for GPT-5.2-codex (codex does not support none)', async () => {
			const body: RequestBody = {
				model: 'gpt-5.2-codex',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'none' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.2-codex');
			expect(result.reasoning?.effort).toBe('low');
		});

		it('should normalize minimal to low for gpt-5.2-codex', async () => {
			const body: RequestBody = {
				model: 'gpt-5.2-codex',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'minimal' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.2-codex');
			expect(result.reasoning?.effort).toBe('low');
		});

		it('should preserve none for GPT-5.1 general purpose', async () => {
			const body: RequestBody = {
				model: 'gpt-5.1-none',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'none' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.1');
			expect(result.reasoning?.effort).toBe('none');
		});

		it('should upgrade none to low for GPT-5.1-codex (codex does not support none)', async () => {
			const body: RequestBody = {
				model: 'gpt-5.1-codex',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'none' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.1-codex');
			expect(result.reasoning?.effort).toBe('low');
		});

		it('should upgrade none to low for GPT-5.1-codex-max (codex max does not support none)', async () => {
			const body: RequestBody = {
				model: 'gpt-5.1-codex-max',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'none' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.model).toBe('gpt-5.1-codex-max');
			expect(result.reasoning?.effort).toBe('low');
		});

		it('should normalize minimal to low for non-codex models', async () => {
			const body: RequestBody = {
				model: 'gpt-5',
				input: [],
			};
			const userConfig: UserConfig = {
				global: { reasoningEffort: 'minimal' },
				models: {},
			};
			const result = await transformRequestBody(body, codexInstructions, userConfig);
			expect(result.reasoning?.effort).toBe('low');
		});

		it('should use minimal effort for lightweight models', async () => {
			const body: RequestBody = {
				model: 'gpt-5-nano',
				input: [],
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.reasoning?.effort).toBe('medium');
		});

		it('should normalize minimal to low when provided by the host', async () => {
			const body: RequestBody = {
				model: 'gpt-5-nano',
				input: [],
				reasoning: { effort: 'minimal' },
			};
			const result = await transformRequestBody(body, codexInstructions);
			expect(result.reasoning?.effort).toBe('low');
		});

		it('should convert orphaned function_call_output to message to preserve context', async () => {
			const body: RequestBody = {
				model: 'gpt-5-codex',
				input: [
					{ type: 'message', role: 'user', content: 'hello' },
					{ type: 'function_call_output', role: 'assistant', call_id: 'orphan_call', name: 'read', output: '{}' } as any,
				],
			};

			const result = await transformRequestBody(body, codexInstructions);

			expect(result.tools).toBeUndefined();
			expect(result.input).toHaveLength(2);
			expect(result.input![0].type).toBe('message');
			expect(result.input![1].type).toBe('message');
			expect(result.input![1].role).toBe('assistant');
			expect(result.input![1].content).toContain('[Previous read result; call_id=orphan_call]');
		});

		it('should keep matched function_call pairs when no tools present (for compaction)', async () => {
			const body: RequestBody = {
				model: 'gpt-5-codex',
				input: [
					{ type: 'message', role: 'user', content: 'hello' },
					{ type: 'function_call', call_id: 'call_1', name: 'write', arguments: '{}' } as any,
					{ type: 'function_call_output', call_id: 'call_1', output: 'success' } as any,
				],
			};

			const result = await transformRequestBody(body, codexInstructions);

			expect(result.tools).toBeUndefined();
			expect(result.input).toHaveLength(3);
			expect(result.input![1].type).toBe('function_call');
			expect(result.input![2].type).toBe('function_call_output');
		});

		it('should treat local_shell_call as a match for function_call_output', async () => {
			const body: RequestBody = {
				model: 'gpt-5-codex',
				input: [
					{ type: 'message', role: 'user', content: 'hello' },
					{
						type: 'local_shell_call',
						call_id: 'shell_call',
						action: { type: 'exec', command: ['ls'] },
					} as any,
					{ type: 'function_call_output', call_id: 'shell_call', output: 'ok' } as any,
				],
			};

			const result = await transformRequestBody(body, codexInstructions);

			expect(result.input).toHaveLength(3);
			expect(result.input![1].type).toBe('local_shell_call');
			expect(result.input![2].type).toBe('function_call_output');
		});

		it('should keep matching custom_tool_call_output items', async () => {
			const body: RequestBody = {
				model: 'gpt-5-codex',
				input: [
					{ type: 'message', role: 'user', content: 'hello' },
					{
						type: 'custom_tool_call',
						call_id: 'custom_call',
						name: 'mcp_tool',
						input: '{}',
					} as any,
					{ type: 'custom_tool_call_output', call_id: 'custom_call', output: 'done' } as any,
				],
			};

			const result = await transformRequestBody(body, codexInstructions);

			expect(result.input).toHaveLength(3);
			expect(result.input![1].type).toBe('custom_tool_call');
			expect(result.input![2].type).toBe('custom_tool_call_output');
		});

		it('should convert orphaned custom_tool_call_output to message', async () => {
			const body: RequestBody = {
				model: 'gpt-5-codex',
				input: [
					{ type: 'message', role: 'user', content: 'hello' },
					{ type: 'custom_tool_call_output', call_id: 'orphan_custom', output: 'oops' } as any,
				],
			};

			const result = await transformRequestBody(body, codexInstructions);

			expect(result.input).toHaveLength(2);
			expect(result.input![1].type).toBe('message');
			expect(result.input![1].content).toContain('[Previous tool result; call_id=orphan_custom]');
		});

		describe('CODEX_MODE parameter', () => {
			it('should use bridge message when codexMode=true and tools present (default)', async () => {
				const body: RequestBody = {
					model: 'gpt-5',
					input: [{ type: 'message', role: 'user', content: 'hello' }],
					tools: [{ name: 'test_tool' }],
				};
				const result = await transformRequestBody(body, codexInstructions, undefined, true);

				expect(result.input).toHaveLength(2);
				expect(result.input![0].role).toBe('developer');
				expect((result.input![0].content as any)[0].text).toContain('Codex Running in OpenCode');
			});

			it('should filter OpenCode prompts when codexMode=true', async () => {
				const body: RequestBody = {
					model: 'gpt-5',
					input: [
						{
							type: 'message',
							role: 'developer',
							content: 'You are a coding agent running in the opencode',
						},
						{ type: 'message', role: 'user', content: 'hello' },
					],
					tools: [{ name: 'test_tool' }],
				};
				const result = await transformRequestBody(body, codexInstructions, undefined, true);

				// Should have bridge message + user message (OpenCode prompt filtered out)
				expect(result.input).toHaveLength(2);
				expect(result.input![0].role).toBe('developer');
				expect((result.input![0].content as any)[0].text).toContain('Codex Running in OpenCode');
				expect(result.input![1].role).toBe('user');
			});

			it('should not add bridge message when codexMode=true but no tools', async () => {
				const body: RequestBody = {
					model: 'gpt-5',
					input: [{ type: 'message', role: 'user', content: 'hello' }],
				};
				const result = await transformRequestBody(body, codexInstructions, undefined, true);

				expect(result.input).toHaveLength(1);
				expect(result.input![0].role).toBe('user');
			});

			it('should use tool remap message when codexMode=false', async () => {
				const body: RequestBody = {
					model: 'gpt-5',
					input: [{ type: 'message', role: 'user', content: 'hello' }],
					tools: [{ name: 'test_tool' }],
				};
				const result = await transformRequestBody(body, codexInstructions, undefined, false);

				expect(result.input).toHaveLength(2);
				expect(result.input![0].role).toBe('developer');
				expect((result.input![0].content as any)[0].text).toContain('apply_patch');
			});

			it('should not filter OpenCode prompts when codexMode=false', async () => {
				const body: RequestBody = {
					model: 'gpt-5',
					input: [
						{
							type: 'message',
							role: 'developer',
							content: 'You are a coding agent running in the opencode',
						},
						{ type: 'message', role: 'user', content: 'hello' },
					],
					tools: [{ name: 'test_tool' }],
				};
				const result = await transformRequestBody(body, codexInstructions, undefined, false);

				// Should have tool remap + opencode prompt + user message
				expect(result.input).toHaveLength(3);
				expect(result.input![0].role).toBe('developer');
				expect((result.input![0].content as any)[0].text).toContain('apply_patch');
				expect(result.input![1].role).toBe('developer');
				expect(result.input![2].role).toBe('user');
			});

			it('should default to codexMode=true when parameter not provided', async () => {
				const body: RequestBody = {
					model: 'gpt-5',
					input: [{ type: 'message', role: 'user', content: 'hello' }],
					tools: [{ name: 'test_tool' }],
				};
				// Not passing codexMode parameter - should default to true
				const result = await transformRequestBody(body, codexInstructions);

				// Should use bridge message (codexMode=true by default)
				expect(result.input![0].role).toBe('developer');
				expect((result.input![0].content as any)[0].text).toContain('Codex Running in OpenCode');
			});
		});

		// NEW: Integration tests for all config scenarios
		describe('Integration: Complete Config Scenarios', () => {
			describe('Scenario 1: Default models (no custom config)', () => {
				it('should handle gpt-5-codex with global options only', async () => {
					const body: RequestBody = {
						model: 'gpt-5-codex',
						input: []
					};
					const userConfig: UserConfig = {
						global: { reasoningEffort: 'high' },
						models: {}
					};

					const result = await transformRequestBody(body, codexInstructions, userConfig);

					expect(result.model).toBe('gpt-5.1-codex');  // gpt-5-codex now maps to gpt-5.1-codex
					expect(result.reasoning?.effort).toBe('high');  // From global
					expect(result.store).toBe(false);
				});

				it('should handle gpt-5-mini normalizing to gpt-5.1', async () => {
					const body: RequestBody = {
						model: 'gpt-5-mini',
						input: []
					};

					const result = await transformRequestBody(body, codexInstructions);

					expect(result.model).toBe('gpt-5.1');  // gpt-5 now maps to gpt-5.1
					expect(result.reasoning?.effort).toBe('medium');  // Default for normalized gpt-5.1
				});
			});

			describe('Scenario 2: Custom preset names (new style)', () => {
				const userConfig: UserConfig = {
					global: { reasoningEffort: 'medium', include: ['reasoning.encrypted_content'] },
					models: {
						'gpt-5-codex-low': {
							options: { reasoningEffort: 'low' }
						},
						'gpt-5-codex-high': {
							options: { reasoningEffort: 'high', reasoningSummary: 'detailed' }
						}
					}
				};

				it('should apply per-model options for gpt-5-codex-low', async () => {
					const body: RequestBody = {
						model: 'gpt-5-codex-low',
						input: []
					};

					const result = await transformRequestBody(body, codexInstructions, userConfig);

					expect(result.model).toBe('gpt-5.1-codex');  // gpt-5-codex now maps to gpt-5.1-codex
					expect(result.reasoning?.effort).toBe('low');  // From per-model
					expect(result.include).toEqual(['reasoning.encrypted_content']);  // From global
				});

				it('should apply per-model options for gpt-5-codex-high', async () => {
					const body: RequestBody = {
						model: 'gpt-5-codex-high',
						input: []
					};

					const result = await transformRequestBody(body, codexInstructions, userConfig);

					expect(result.model).toBe('gpt-5.1-codex');  // gpt-5-codex now maps to gpt-5.1-codex
					expect(result.reasoning?.effort).toBe('high');  // From per-model
					expect(result.reasoning?.summary).toBe('detailed');  // From per-model
				});

				it('should use global options for default gpt-5-codex', async () => {
					const body: RequestBody = {
						model: 'gpt-5-codex',
						input: []
					};

					const result = await transformRequestBody(body, codexInstructions, userConfig);

					expect(result.model).toBe('gpt-5.1-codex');  // gpt-5-codex now maps to gpt-5.1-codex
					expect(result.reasoning?.effort).toBe('medium');  // From global (no per-model)
				});
			});

			describe('Scenario 3: Backwards compatibility (old verbose names)', () => {
				const userConfig: UserConfig = {
					global: {},
					models: {
						'GPT 5 Codex Low (ChatGPT Subscription)': {
							options: { reasoningEffort: 'low', textVerbosity: 'low' }
						}
					}
				};

				it('should find and apply old config format', async () => {
					const body: RequestBody = {
						model: 'GPT 5 Codex Low (ChatGPT Subscription)',
						input: []
					};

					const result = await transformRequestBody(body, codexInstructions, userConfig);

					expect(result.model).toBe('gpt-5.1-codex');  // gpt-5-codex now maps to gpt-5.1-codex
					expect(result.reasoning?.effort).toBe('low');  // From per-model (old format)
					expect(result.text?.verbosity).toBe('low');
				});
			});

			describe('Scenario 4: Mixed default + custom models', () => {
				const userConfig: UserConfig = {
					global: { reasoningEffort: 'medium' },
					models: {
						'gpt-5-codex-low': {
							options: { reasoningEffort: 'low' }
						}
					}
				};

				it('should use per-model for custom variant', async () => {
					const body: RequestBody = {
						model: 'gpt-5-codex-low',
						input: []
					};

					const result = await transformRequestBody(body, codexInstructions, userConfig);

					expect(result.reasoning?.effort).toBe('low');  // Per-model
				});

				it('should use global for default model', async () => {
					const body: RequestBody = {
						model: 'gpt-5',
						input: []
					};

					const result = await transformRequestBody(body, codexInstructions, userConfig);

					expect(result.reasoning?.effort).toBe('medium');  // Global
				});
			});

			describe('Scenario 5: Message ID filtering with multi-turn', () => {
				it('should remove ALL IDs in multi-turn conversation', async () => {
					const body: RequestBody = {
						model: 'gpt-5-codex',
						input: [
							{ id: 'msg_turn1', type: 'message', role: 'user', content: 'first' },
							{ id: 'rs_response1', type: 'message', role: 'assistant', content: 'response' },
							{ id: 'msg_turn2', type: 'message', role: 'user', content: 'second' },
							{ id: 'assistant_123', type: 'message', role: 'assistant', content: 'reply' },
						]
					};

					const result = await transformRequestBody(body, codexInstructions);

					// All items kept, ALL IDs removed
					expect(result.input).toHaveLength(4);
					expect(result.input!.every(item => !item.id)).toBe(true);
					expect(result.store).toBe(false);  // Stateless mode
					expect(result.include).toEqual(['reasoning.encrypted_content']);
				});
			});

			describe('Scenario 6: Complete end-to-end transformation', () => {
				it('should handle full transformation: custom model + IDs + tools', async () => {
					const userConfig: UserConfig = {
						global: { include: ['reasoning.encrypted_content'] },
						models: {
							'gpt-5-codex-low': {
								options: {
									reasoningEffort: 'low',
									textVerbosity: 'low',
									reasoningSummary: 'auto'
								}
							}
						}
					};

					const body: RequestBody = {
						model: 'gpt-5-codex-low',
						input: [
							{ id: 'msg_1', type: 'message', role: 'user', content: 'test' },
							{ id: 'rs_2', type: 'message', role: 'assistant', content: 'reply' }
						],
						tools: [{ name: 'edit' }]
					};

					const result = await transformRequestBody(body, codexInstructions, userConfig);

					// Model normalized (gpt-5-codex now maps to gpt-5.1-codex)
					expect(result.model).toBe('gpt-5.1-codex');

					// IDs removed
					expect(result.input!.every(item => !item.id)).toBe(true);

					// Per-model options applied
					expect(result.reasoning?.effort).toBe('low');
					expect(result.reasoning?.summary).toBe('auto');
					expect(result.text?.verbosity).toBe('low');

					// Codex fields set
					expect(result.store).toBe(false);
					expect(result.stream).toBe(true);
					expect(result.instructions).toBe(codexInstructions);
					expect(result.include).toEqual(['reasoning.encrypted_content']);
				});
			});
		});
	});
});
```

## File: `test/response-handler.test.ts`
```typescript
import { describe, it, expect, vi } from 'vitest';
import { ensureContentType, convertSseToJson } from '../lib/request/response-handler.js';

describe('Response Handler Module', () => {
	describe('ensureContentType', () => {
		it('should preserve existing content-type', () => {
			const headers = new Headers();
			headers.set('content-type', 'application/json');
			const result = ensureContentType(headers);
			expect(result.get('content-type')).toBe('application/json');
		});

		it('should add default content-type if missing', () => {
			const headers = new Headers();
			const result = ensureContentType(headers);
			expect(result.get('content-type')).toBe('text/event-stream; charset=utf-8');
		});

		it('should not modify original headers', () => {
			const headers = new Headers();
			const result = ensureContentType(headers);
			expect(headers.has('content-type')).toBe(false);
			expect(result.has('content-type')).toBe(true);
		});
	});

	describe('convertSseToJson', () => {
		it('should throw error if response has no body', async () => {
			const response = new Response(null);
			const headers = new Headers();

			await expect(convertSseToJson(response, headers)).rejects.toThrow(
				'Response has no body'
			);
		});

		it('should parse SSE stream with response.done event', async () => {
			const sseContent = `data: {"type":"response.started"}
data: {"type":"response.done","response":{"id":"resp_123","output":"test"}}
`;
			const response = new Response(sseContent);
			const headers = new Headers();

			const result = await convertSseToJson(response, headers);
			const body = await result.json();

			expect(body).toEqual({ id: 'resp_123', output: 'test' });
			expect(result.headers.get('content-type')).toBe('application/json; charset=utf-8');
		});

		it('should parse SSE stream with response.completed event', async () => {
			const sseContent = `data: {"type":"response.started"}
data: {"type":"response.completed","response":{"id":"resp_456","output":"done"}}
`;
			const response = new Response(sseContent);
			const headers = new Headers();

			const result = await convertSseToJson(response, headers);
			const body = await result.json();

			expect(body).toEqual({ id: 'resp_456', output: 'done' });
		});

		it('should return original text if no final response found', async () => {
			const sseContent = `data: {"type":"response.started"}
data: {"type":"chunk","delta":"text"}
`;
			const response = new Response(sseContent);
			const headers = new Headers();

			const result = await convertSseToJson(response, headers);
			const text = await result.text();

			expect(text).toBe(sseContent);
		});

		it('should skip malformed JSON in SSE stream', async () => {
			const sseContent = `data: not-json
data: {"type":"response.done","response":{"id":"resp_789"}}
`;
			const response = new Response(sseContent);
			const headers = new Headers();

			const result = await convertSseToJson(response, headers);
			const body = await result.json();

			expect(body).toEqual({ id: 'resp_789' });
		});

		it('should handle empty SSE stream', async () => {
			const response = new Response('');
			const headers = new Headers();

			const result = await convertSseToJson(response, headers);
			const text = await result.text();

			expect(text).toBe('');
		});

		it('should preserve response status and statusText', async () => {
			const sseContent = `data: {"type":"response.done","response":{"id":"x"}}`;
			const response = new Response(sseContent, {
				status: 200,
				statusText: 'OK',
			});
			const headers = new Headers();

			const result = await convertSseToJson(response, headers);

			expect(result.status).toBe(200);
			expect(result.statusText).toBe('OK');
		});
	});
});
```


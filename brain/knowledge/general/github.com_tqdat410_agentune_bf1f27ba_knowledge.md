---
id: github.com-tqdat410-agentune-bf1f27ba-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:29.128273
---

# KNOWLEDGE EXTRACT: github.com_tqdat410_agentune_bf1f27ba
> **Extracted on:** 2026-04-01 15:31:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524565/github.com_tqdat410_agentune_bf1f27ba

---

## File: `.gitignore`
```
node_modules/
dist/
*.tsbuildinfo
.env
plans/
.claude/
.obsidian/
repomix-output.xml
```

## File: `.npmignore`
```
src/
docs/
plans/
scripts/
tsconfig.json
*.tsbuildinfo
dist/**/*.map
dist/**/*.test.js
dist/**/*.test.d.ts
dist/**/*test-helper*.js
dist/**/*test-helper*.d.ts
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 tqdat410

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

## File: `README.md`
```markdown
# agentune

**Music Player for Agent.**

agentune is a local MCP music player for Claude Code, Codex, OpenCode, and other MCP-compatible coding agents. Your agent can discover tracks, play instantly, queue the next song, and keep one shared listening session running while you work.

> CLI-only package: install and run `agentune` as a command. Programmatic `import "agentune"` is not a supported interface.

## Why agentune

- **Zero-auth setup**: no Spotify login, no Apple Music login, no API keys
- **Background play**: audio runs through `mpv`, not a browser tab
- **Auto start**: the daemon can start itself when your agent connects
- **Shared session**: queue, history, taste state, and dashboard stay in one local daemon
- **Browser dashboard**: live now-playing, queue, volume, taste, and listening insights
- **Cross-platform**: works on Windows, macOS, and Linux

## Prerequisites

- Node.js 20+
- `mpv`
- `yt-dlp`

Use `agentune doctor` after install to verify the runtime sees the required dependencies, the bundled `yt-dlp` binary, the system `yt-dlp` command, and the current daemon state.

### macOS

```bash
brew install mpv yt-dlp
```

### Ubuntu / Debian

```bash
sudo apt-get install mpv python3-pip
pip install yt-dlp
```

### Windows

```bash
scoop install mpv yt-dlp
```

## Quick Start

### 1. Install agentune

```bash
npm install -g agentune
agentune --version
agentune doctor
```

### 2. Connect your MCP client

Here are ready-to-use examples for common coding agents. Other MCP-compatible clients can point to the same local `agentune` command.

#### Claude Code

```bash
claude mcp add agentune --scope user -- agentune
```

#### Codex

```bash
codex mcp add agentune -- agentune
```

#### OpenCode

Add this to `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "agentune": {
      "type": "local",
      "command": ["agentune"],
      "enabled": true
    }
  }
}
```

### 3. Start your coding session

Your MCP client launches `agentune` automatically. The dashboard is available at `http://localhost:3737` after the first connection.

Useful daemon commands:

```bash
agentune --help
agentune doctor
agentune start
agentune stop
```

Use `agentune doctor` to confirm Node.js, `mpv`, bundled `yt-dlp`, system `yt-dlp`, config paths, and daemon health before you start playback.

Use `agentune start` when you want the background daemon running before your agent connects, or when `autoStartDaemon` is disabled.

### 4. Send your first prompts

```text
play some musics. id like Vietnamese song only, V-Pop, Indie, RAP, Ballad.
```

Use that first prompt to define your taste/persona in plain language. The agent can save that preference and reuse it later.

After that, a simple prompt is enough:

```text
Play some musics
```

The agent should read your saved taste, recent listening history, top artists, and top keywords, then choose music that fits instead of starting from zero each time.

If you want to change taste later, just say it naturally. For example:

```text
play some musics. i want more chill Vietnamese indie and fewer rap tracks tonight.
```

The agent can update the saved taste text, then continue using the new preference on later picks.

> Tip: if your coding setup supports subagents, you can dedicate one subagent to keep the playlist going during the whole work session. In repos that use `CLAUDE.md` or `AGENTS.md`, you can also add a small instruction telling the agent to maintain playback, queue the next fitting track, and adapt when you describe a new taste.

## Main Capabilities

- Save a simple free-text music taste/persona across sessions
- Let the agent use saved taste, recent plays, top artists, and top keywords for future picks
- Play a song immediately or add it to the queue
- Pause, resume, skip, and adjust volume
- Check what is playing right now
- Review recent listening history
- Update the taste/persona text any time in plain language
- Run `agentune doctor` to inspect runtime dependencies and local daemon health

## Browser Dashboard

Open `http://localhost:3737` to see:

- now-playing track and progress
- pause/resume and next controls
- volume slider
- live queue
- listening insights from local history
- taste editor
- cleanup actions and explicit daemon stop

## Runtime Notes

On first run, agentune creates `${AGENTUNE_DATA_DIR || ~/.agentune}/config.json`.

Most useful settings:

- `dashboardPort`: browser dashboard port, default `3737`
- `daemonPort`: local daemon port, default `3747`
- `defaultVolume`: initial playback volume
- `autoStartDaemon`: automatically start the daemon when your agent connects

If `autoStartDaemon` is `false`, start the daemon yourself before connecting:

```bash
agentune start
```

The daemon keeps playing in the background after the agent session closes. It stops only when you run `agentune stop` or click `Stop daemon` in the dashboard.

`agentune doctor` treats Node.js, runtime config, `mpv`, and the bundled `yt-dlp` binary as required checks. System `yt-dlp` and daemon stopped state are reported as advisory warnings instead of hard failures.

## More Docs

- [Project overview](./docs/project-overview-pdr.md)
- [System architecture](./docs/system-architecture.md)
- [Codebase summary](./docs/codebase-summary.md)

## License

MIT
```

## File: `package.json`
```json
{
  "name": "agentune",
  "version": "0.1.3",
  "description": "Music Player for Agent",
  "type": "module",
  "bin": {
    "agentune": "dist/index.js"
  },
  "files": [
    "dist/",
    "!dist/**/*.map",
    "!dist/**/*.test.js",
    "!dist/**/*.test.d.ts",
    "!dist/**/*test-helper*.js",
    "!dist/**/*test-helper*.d.ts",
    "public/"
  ],
  "scripts": {
    "clean": "node -e \"require('node:fs').rmSync('dist', { recursive: true, force: true })\"",
    "build": "npm run clean && tsc",
    "dev": "tsc --watch",
    "start": "node dist/index.js",
    "test:compiled": "node scripts/run-compiled-tests.mjs",
    "test": "npm run build && npm run test:compiled",
    "verify:publish": "node scripts/verify-publish.mjs",
    "release:alpha": "node scripts/release.mjs alpha",
    "release:stable": "node scripts/release.mjs stable",
    "prepublishOnly": "node -e \"if (!process.env.AGENTUNE_RELEASE_MODE) { console.error('Use npm run release:alpha or npm run release:stable'); process.exit(1); }\""
  },
  "keywords": [
    "mcp",
    "music",
    "agent",
    "claude",
    "youtube",
    "mpv"
  ],
  "engines": {
    "node": ">=20"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/tqdat410/agentune.git"
  },
  "homepage": "https://github.com/tqdat410/agentune#readme",
  "bugs": {
    "url": "https://github.com/tqdat410/agentune/issues"
  },
  "publishConfig": {
    "access": "public"
  },
  "license": "MIT",
  "dependencies": {
    "@distube/ytsr": "^2.0.4",
    "@modelcontextprotocol/sdk": "^1.27.1",
    "better-sqlite3": "^12.8.0",
    "ws": "^8.20.0",
    "youtube-dl-exec": "^3.1.4",
    "zod": "^4.3.6"
  },
  "devDependencies": {
    "@types/better-sqlite3": "^7.6.13",
    "@types/node": "^25.5.0",
    "@types/ws": "^8.18.1",
    "typescript": "^5.9.3"
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "node16",
    "outDir": "dist",
    "rootDir": "src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "declaration": true,
    "sourceMap": true
  },
  "include": ["src/**/*"]
}
```

## File: `docs/code-standards.md`
```markdown
# Code Standards & Conventions

## TypeScript Configuration

**Target**: ES2022 (modern Node.js 20+)
**Module System**: ESM (ES modules, Node16 resolution)
**Strict Mode**: Required (`strict: true` in tsconfig.json)

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "node16",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "declaration": true,
    "sourceMap": true
  }
}
```

**No CommonJS**: All imports use `import/export` syntax, never `require()`.

## Naming Conventions

### Files & Directories
- **kebab-case** for all source files: `youtube-provider.ts`, `mpv-controller.ts`
- **Descriptive names** that convey purpose for LLM tools
- **Examples**:
  - Good: `youtube-provider.ts` (describes what it provides)
  - Bad: `provider.ts` (too vague)

### Variables & Functions
- **camelCase** for variables, functions, and parameters
- **PascalCase** for classes, types, and interfaces
- **CONSTANT_CASE** for module-level constants

```typescript
// Variables & functions
const nowPlayingTrack = {...};
function getStreamUrl(videoId: string): Promise<string> {}

// Classes & types
class MpvController {}
interface Track {
  videoId: string;
  title: string;
  duration: number;
}
type SearchResult = {id: string; title: string};

// Constants
const MAX_QUEUE_SIZE = 100;
const IPC_TIMEOUT_MS = 5000;
```

## Import/Export Rules

### ESM Only
```typescript
// ✓ Correct
import { createMcpServer } from './mcp/mcp-server.js';
import type { Tool } from '@modelcontextprotocol/sdk';

// ✗ Wrong
const { createMcpServer } = require('./mcp/mcp-server');
module.exports = {...};
```

### File Extensions
Always include `.js` in ESM imports (even though source is `.ts`):
```typescript
import { getStreamUrl } from './providers/youtube-provider.js';
```

### Type Imports
Use `import type` for type-only imports to clarify intent:
```typescript
import type { Track, SearchResult } from './queue/queue-manager.js';
```

## Error Handling Pattern

**Never throw errors from MCP tool functions.** Always return a structured error response.

```typescript
// All tool functions must return this structure (MCP SDK shape):
type ToolContent = { type: "text"; text: string };
type ToolResult = { content: ToolContent[]; isError?: boolean };

// ✓ Correct
async function play(videoId: string): Promise<ToolResult> {
  if (!videoId) {
    return {
      content: [{ type: "text", text: "videoId is required" }],
      isError: true
    };
  }
  try {
    const url = await getStreamUrl(videoId);
    // ... playback logic
    return {
      content: [{ type: "text", text: JSON.stringify({
        nowPlaying: trackMetadata
      }, null, 2) }]
    };
  } catch (err) {
    return {
      content: [{ type: "text", text: `Playback failed: ${(err as Error).message}` }],
      isError: true
    };
  }
}

// ✗ Wrong
async function play(videoId: string) {
  if (!videoId) throw new Error('videoId is required');
  const url = await getStreamUrl(videoId); // No try/catch
}
```

## Logging Rules

### stdio Safety (CRITICAL)
- **Never use `console.log()`** — corrupts MCP stdio protocol
- **Always use `console.error()`** for debug messages and logs

```typescript
// ✓ Correct
console.error('[agentune] Starting...');
console.error('[mpv] Volume set to:', volume);

// ✗ Wrong
console.log('[agentune] Starting...'); // Breaks MCP!
```

### Debug Format
```typescript
console.error('[module-name] message', {key: value});
// Example:
console.error('[youtube-provider] search complete', {query: 'lo-fi', results: 10});
```

## Async/Await Patterns

Always use `async/await` for Promise-based code. Never use `.then()` chains.

```typescript
// ✓ Correct
async function processTrack(videoId: string) {
  const url = await getStreamUrl(videoId);
  const metadata = await parseMetadata(videoId);
  return {url, metadata};
}

// ✗ Avoid
function processTrack(videoId: string) {
  return getStreamUrl(videoId)
    .then(url => parseMetadata(videoId).then(meta => ({url, meta})));
}
```

### Top-Level Async
```typescript
// index.ts
async function main() {
  try {
    // await async operations
  } catch (err) {
    console.error('[agentune] Fatal error:', err);
    process.exit(1);
  }
}

main();
```

## Type Annotations

All function signatures must have explicit type annotations (strict mode enforces this).

```typescript
// ✓ Correct
async function search(query: string): Promise<SearchResult[]> {
  // ...
}

function setVolume(volume: number): void {
  // ...
}

// ✗ Wrong (relies on inference)
async function search(query) {
  // ...
}
```

## Interface & Type Definitions

Define types at module level, re-export for consumers.

```typescript
// queue-manager.ts
export interface Track {
  videoId: string;
  title: string;
  artist?: string;
  duration: number; // seconds
  url?: string;
  thumbnail?: string;
}

export type QueueState = {
  nowPlaying: Track | null;
  queue: Track[];
  history: Track[];
  pausedAt: number;
};
```

## Code Comments

### When to Comment
- **Complex logic**: Explain "why", not "what"
- **Non-obvious decisions**: Design rationale
- **Workarounds**: Temporary fixes with tracking issues

### When NOT to Comment
- Self-documenting code (good names make comments unnecessary)
- Obvious operations

```typescript
// ✓ Good
// YouTube URLs expire after ~6 hours; cache and refresh on 404
const cachedUrl = urlCache.get(videoId);
if (isUrlExpired(cachedUrl)) {
  return await getStreamUrl(videoId); // Fresh fetch
}

// ✗ Bad
// Loop through results
for (const result of results) {
  // Add to array
  items.push(result);
}
```

## File Structure

Each module should follow this pattern:

```typescript
// Imports (all at top)
import type { Tool } from '@modelcontextprotocol/sdk';
import { someFunction } from './other-module.js';

// Types & Interfaces
export interface MyType {
  // ...
}

// Constants
const DEFAULT_TIMEOUT = 5000;

// Main class/function
export class MyClass {
  // Implementation
}

// Exports (grouped at end if not inline)
export { MyClass };
```

## Zod Validation (Phase 2+)

Use Zod for MCP tool request validation:

```typescript
import { z } from 'zod';

const SearchRequestSchema = z.object({
  query: z.string().min(1, 'Query cannot be empty'),
  limit: z.number().int().positive().optional().default(10)
});

type SearchRequest = z.infer<typeof SearchRequestSchema>;

async function search(req: SearchRequest): Promise<ToolResult> {
  const validated = SearchRequestSchema.parse(req);
  // Use validated.query, validated.limit
}
```

## Testing Standards

### Test File Naming
- Place tests adjacent to source: `foo.ts` → `foo.test.ts`
- Use descriptive test names

### Test Structure
```typescript
import { describe, it, expect } from 'vitest'; // or your framework

describe('YouTubeProvider', () => {
  describe('search', () => {
    it('should return results for valid query', async () => {
      const results = await search('lo-fi beats');
      expect(results).toBeDefined();
      expect(results.length).toBeGreaterThan(0);
    });

    it('should handle empty query gracefully', async () => {
      const result = await search('');
      expect(result.isError).toBe(true);
      expect(result.message).toContain('empty');
    });
  });
});
```

### Coverage Targets
- **P0 features**: 100% coverage (search, play, skip, status)
- **P1 features**: 80% coverage (mood, queue, dashboard)
- **Helpers**: 70% coverage

## Performance Guidelines

### Target Metrics
- **Search**: < 1 second
- **Stream URL extraction**: < 2 seconds
- **Play command → audio output**: < 3 seconds
- **WebSocket update latency**: < 100ms

### Optimization Rules
1. Cache YouTube URLs (5-hour TTL)
2. Parallelize independent operations (search + metadata)
3. Use streaming for large files (mpv handles this)
4. Avoid blocking I/O in main thread

```typescript
// ✓ Parallel
const [results, metadata] = await Promise.all([
  search(query),
  parseMetadata(videoId)
]);

// ✗ Sequential
const results = await search(query);
const metadata = await parseMetadata(videoId);
```

## Security Guidelines

### Input Validation
- Validate all agent inputs (query length, IDs format)
- Sanitize WebSocket messages before broadcast
- Never execute shell commands with unsanitized input

```typescript
// ✓ Correct
const query = SearchRequestSchema.parse(input.query);

// ✗ Wrong
const cmd = `youtube-dl "${userInput}"`;
```

### Sensitive Data
- Never log credentials, API keys, or user data
- Use `console.error()` for debug (not stdout)
- No personal data in queue history

### IPC Security
- Restrict IPC socket permissions (Windows: inherited from parent)
- Validate all JSON messages from mpv

## Build & Deployment

### Compilation
```bash
npm run build    # Compiles src/ → dist/
npm run dev      # Watch mode
```

### Pre-commit Checks
- Run `tsc --noEmit` (type check)
- No unused variables or imports
- No `console.log()` calls

### npm publish
- Verify `package.json` `files` array includes `dist/` and `public/`
- Ensure shebang in dist/index.js after build
- Test `npm install -g ./` locally before publish

## Code Review Checklist

Before submitting a PR:
- [ ] TypeScript strict mode passes (`npm run build`)
- [ ] No `console.log()` (only `console.error()`)
- [ ] Error handling returns `{isError, message, data}`
- [ ] All async functions are `async/await`
- [ ] Type annotations on all function signatures
- [ ] No unused imports or variables
- [ ] Comments explain "why", not "what"
- [ ] Tests pass and cover P0 paths
- [ ] Follows file/naming conventions (kebab-case, camelCase)

## References

- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Node.js ESM Docs](https://nodejs.org/api/esm.html)
- [MCP Specification](https://modelcontextprotocol.io/)
- [Zod Documentation](https://zod.dev/)
```

## File: `docs/codebase-summary.md`
```markdown
# Codebase Summary

## Current Implementation

`agentune` is a shared local daemon for agent-controlled music playback.

- Agents talk to the daemon through MCP.
- The daemon owns queue state, playback, listening history, and the browser dashboard.
- `mpv` handles audio output.
- SQLite stores tracks, play events, provider cache data, and persisted persona taste text.
- Runtime ports, default volume, auto-start policy, and fixed discover ranking live in `${AGENTUNE_DATA_DIR || ~/.agentune}/config.json`.
- The daemon is explicit-lifecycle: no idle auto-shutdown, stop only via CLI or dashboard.
- `agentune stop` now waits for graceful shutdown first and only falls back to a verified process kill.
- The daemon PID file now also carries a per-process control token used by `/mcp` and `/shutdown`.
- `agentune doctor` now reports Node.js compatibility, runtime config state, `mpv`, bundled `yt-dlp`, system `yt-dlp`, daemon health, and local runtime paths.
- The dashboard now bootstraps a per-process session token into HTML and requires that token for local API, artwork-proxy, and WebSocket access.
- Audio control now talks to `mpv` through a small internal JSON IPC client instead of the stale `node-mpv` wrapper package.
- Tarball publish verification now rejects unexpected install deprecation warnings and explicitly allows only the residual `better-sqlite3 -> prebuild-install` warning.

The active state redesign is agent-first:

```ts
{
  context: { hour, period, dayOfWeek },
  persona: { Preferences: string },
  history: {
    recent: [...],
    stats: { topArtists, topKeywords }
  }
}
```

`discover()` now returns a flat paginated list of Apple candidates. The server builds Apple-only batches, deduplicates them, soft-ranks them from history plus fixed runtime config weights, caches the ranked snapshot, then returns the requested page.

## Project Structure

```text
agentune/
├── src/
│   ├── index.ts
│   ├── audio/
│   │   ├── mpv-controller.ts
│   │   ├── mpv-ipc-client.test.ts
│   │   ├── mpv-ipc-client.ts
│   │   ├── mpv-launch-helpers.test.ts
│   │   ├── mpv-launch-helpers.ts
│   │   ├── mpv-process-session.ts
│   │   └── platform-ipc-path.ts
│   ├── cli/
│   │   ├── doctor-command.test.ts
│   │   ├── doctor-command.ts
│   │   ├── doctor-report.test.ts
│   │   ├── doctor-report.ts
│   │   ├── doctor-runtime-support.ts
│   │   ├── start-command.ts
│   │   ├── status-command.ts
│   │   └── stop-command.ts
│   ├── daemon/
│   │   ├── daemon-auth.ts
│   │   ├── daemon-server.ts
│   │   ├── health-endpoint.ts
│   │   └── pid-manager.ts
│   ├── history/
│   │   ├── history-schema.ts
│   │   ├── history-store.ts
│   │   ├── history-store-state-redesign.test.ts
│   │   └── history-store.test.ts
│   ├── mcp/
│   │   ├── mcp-server.ts
│   │   ├── song-resolver.ts
│   │   └── tool-handlers.ts
│   ├── providers/
│   │   ├── apple-search-provider.ts
│   │   ├── metadata-normalizer.ts
│   │   ├── search-result-scorer.ts
│   │   └── youtube-provider.ts
│   ├── proxy/
│   │   ├── daemon-launcher.ts
│   │   └── stdio-proxy.ts
│   ├── queue/
│   │   ├── queue-manager.ts
│   │   └── queue-playback-controller.ts
│   ├── taste/
│   │   ├── discover-batch-builder.ts
│   │   ├── discover-merge-and-dedup.ts
│   │   ├── discover-pagination-cache.ts
│   │   ├── discover-pipeline.test.ts
│   │   ├── discover-pipeline.ts
│   │   ├── discover-soft-ranker.test.ts
│   │   ├── discover-soft-ranker.ts
│   │   ├── taste-engine.ts
│   │   └── taste-engine.test.ts
│   ├── runtime/
│   │   ├── runtime-config.test.ts
│   │   ├── runtime-config.ts
│   │   └── runtime-data-paths.ts
│   └── web/
│       ├── state-broadcaster.ts
│       ├── web-server-auth.ts
│       ├── web-server-artwork-proxy.test.ts
│       ├── web-server-artwork-proxy.ts
│       ├── web-server-database-cleanup.test.ts
│       ├── web-server-database-cleanup.ts
│       ├── web-server-helpers.ts
│       ├── web-server-static-file-path.ts
│       ├── web-server-test-helpers.ts
│       └── web-server.ts
├── public/
│   ├── app.js
│   ├── assets/
│   │   └── agentune-mark.svg
│   ├── dashboard/
│   │   ├── auth.js
│   │   ├── constants.js
│   │   ├── dom.js
│   │   ├── insights.js
│   │   ├── marquee.js
│   │   ├── render.js
│   │   ├── settings-api.js
│   │   └── theme.js
│   ├── favicon.ico
│   ├── index.html
│   ├── style.css
│   └── styles/
│       └── dashboard-settings.css
├── docs/
├── package.json
├── README.md
└── repomix-output.xml
```

## State Redesign

### History Store

Files:

- `src/history/history-schema.ts`
- `src/history/history-store.ts`

Current responsibilities:

- persist `tracks`, `plays`, `provider_cache`, and `session_state`
- store free-text persona taste in `session_state.persona_taste_text`
- migrate old databases to the trimmed schema without legacy session/preference columns
- expose manual cleanup operations for history, provider cache, and full reset
- expose aggregate queries used by the taste engine and discover pipeline:
  - `getRecentPlaysDetailed()`
  - `getTopArtists()`
  - `getTopTags()`
  - `getTrackStats()`
  - `batchGetTrackStats()`

Important details:

- `normalizeTrackId(artist, title)` is the canonical track key.
- The constructor migrates older DBs to schema version 3 and removes `preferences`, `similar_json`, `lane_id`, `persona_traits_json`, and older session-state columns.
- Cleanup actions run `wal_checkpoint(TRUNCATE)`, `VACUUM`, and `PRAGMA optimize`.

### Taste Engine

File: `src/taste/taste-engine.ts`

Current responsibilities:

- expose current time context
- read and persist free-text taste text
- package the agent-facing session summary for MCP and the dashboard

Important details:

- The engine does not run a feedback scoring loop.
- There is no active weighted taste runtime outside the returned summary.

### Discovery

Files:

- `src/taste/discover-batch-builder.ts`
- `src/taste/discover-merge-and-dedup.ts`
- `src/taste/discover-soft-ranker.ts`
- `src/taste/discover-pagination-cache.ts`
- `src/taste/discover-pipeline.ts`

Current responsibilities:

- build Apple candidate batches from explicit `artist` / `keywords` seeds
- fall back to top 3 history artists and top 3 history keywords when no seeds are provided
- deduplicate repeated `artist + title` pairs, interleave artists, and break adjacent same-artist clusters after ranking
- soft-rank candidates from top artists, top stored track tags, per-track completion, skip rate, and recent-repeat penalty
- cache ranked snapshots for pagination

Important details:

- Public output is flat and paginated: `{ page, limit, hasMore, candidates[], nextGuide }`.
- `DiscoverBatchBuilder` only calls Apple artist-track and Apple genre search APIs; public candidates always return `provider: "apple"`.
- Internal Apple IDs stay on internal candidates only; `toPublicCandidate()` strips them before the MCP response.
- The pagination cache is in-memory, keyed by normalized `{ artist, keywords }`, uses a 5 minute TTL, keeps up to 10 snapshots, and does not cache empty results.
- If no explicit seeds exist and history has no top artists or keywords, `discover()` returns an empty candidate list.

## MCP Surface

Files:

- `src/mcp/mcp-server.ts`
- `src/mcp/tool-handlers.ts`

State-related MCP tools:

- `get_session_state()`
  - returns `context`, `persona`, and `history`
- `discover(page?, limit?, artist?, keywords?, mode?, intent?)`
  - returns `{ page, limit, hasMore, candidates, nextGuide }`
- `update_persona({ taste })`
  - persists free-text taste text
  - empty string is allowed to clear it

Playback-related MCP tools:

- `play_song(title, artist?)`
- `add_song(title, artist?)`
- `pause()`
- `resume()`
- `skip()`
- `queue_list()`
- `now_playing()`
- `volume(level?)`
- `history(limit?, query?)`

Important details:

- `play_song` and `add_song` are Apple-first for canonical metadata.
- `discover()` returns a flat page plus `nextGuide`, which tells the agent whether to keep paging or improve `artist` / `keywords`.
- `mode` and `intent` remain in the MCP schema for compatibility, but the current discover pipeline ignores them.
- Successful `play_song()` and `add_song()` clear the discover pagination cache.
- `update_persona()` persists taste text and broadcasts persona updates, but does not clear the discover pagination cache.
- Discover ranking is internal only; the public MCP response does not expose scores.

## CLI Surface

Files:

- `src/index.ts`
- `src/cli/start-command.ts`
- `src/cli/status-command.ts`
- `src/cli/stop-command.ts`
- `src/cli/doctor-command.ts`
- `src/cli/doctor-report.ts`

Current CLI commands:

- `agentune`
  - starts stdio proxy mode
- `agentune start`
  - ensures the background daemon is running
- `agentune status`
  - reports daemon health from `/health`
- `agentune stop`
  - requests graceful daemon shutdown and only falls back to a verified process kill
- `agentune doctor`
  - checks Node.js against `package.json.engines.node`
  - loads runtime config and reports resolved data paths
  - verifies `mpv`
  - verifies the bundled `youtube-dl-exec` `yt-dlp` binary
  - reports system `yt-dlp` separately as advisory
  - reports daemon state as healthy / stopped / stale / unresponsive

## Queue and Playback

Files:

- `src/queue/queue-manager.ts`
- `src/queue/queue-playback-controller.ts`
- `src/audio/mpv-controller.ts`
- `src/audio/mpv-ipc-client.ts`
- `src/audio/mpv-launch-helpers.ts`
- `src/audio/mpv-process-session.ts`

Current responsibilities:

- `QueueManager` owns `nowPlaying`, queued items, and playback history.
- `QueuePlaybackController` resolves audio, starts playback, records plays, updates skip/completion status, and advances the queue.
- `MpvController` owns the actual audio engine and emits playback state.
- `MpvProcessSession` launches `mpv`, retries IPC connection until the socket is ready, and subscribes to `pause` / `idle-active` property changes.
- `MpvIpcClient` is a newline-delimited JSON IPC transport with request-id correlation and out-of-order reply handling.

Important details:

- Raw history is recorded with `recordPlay()` on start and `updatePlay()` on skip/finish.
- Playback feedback remains as raw history rows; there is no secondary taste-update path.
- The controller still enriches track tags from Apple after playback begins.
- The next queued track can be prefetched for smoother transitions.
- On Windows, the internal launcher still prefers `mpv.exe` and starts `mpv` with `windowsHide: true` to avoid blank console windows.
- Natural track-end detection now depends on observed `idle-active` transitions from `mpv` JSON IPC instead of wrapper-specific stop events.

## Web Dashboard

Files:

- `src/web/web-server.ts`
- `src/web/web-server-auth.ts`
- `src/web/state-broadcaster.ts`
- `src/web/web-server-helpers.ts`
- `src/web/web-server-static-file-path.ts`
- `public/dashboard/auth.js`
- `public/index.html`
- `public/app.js`
- `public/style.css`

Current HTTP and WebSocket surface:

- `GET /api/status`
- `GET /api/persona`
- `GET /api/artwork?src=...`
- `POST /api/persona`
- `POST /api/volume`
- `POST /api/daemon/stop`
- `GET /api/database/stats`
- `POST /api/database/clear-history`
- `POST /api/database/clear-provider-cache`
- `POST /api/database/full-reset`
- `WS /ws`

Current behavior:

- `StateBroadcaster` publishes playback snapshots: playing, title, artist, thumbnail, position, duration, volume, muted, queue.
- `GET /` serves dashboard HTML dynamically and injects a session token into a `<meta>` tag.
- Persona data is fetched separately from `/api/persona`.
- Artwork is fetched through `/api/artwork`, so the browser can render and sample thumbnails from a same-origin URL.
- If `/api/artwork` fails, the dashboard image element falls back to the raw remote thumbnail URL so album art still renders on older daemons or proxy failures.
- When no track artwork exists yet, the dashboard falls back to the local `public/assets/agentune-mark.svg` logo instead of a remote placeholder service.
- Persona changes are broadcast separately over WebSocket as `{ type: "persona", data: { taste } }`.
- The dashboard includes:
  - centered player shell with full-screen `Queue / Now Playing / Settings` tabs
  - artwork-first now-playing view with marquee-on-overflow title
  - artwork-driven ambient gradient theming for page background and glass surfaces
  - pause, next, and volume controls
  - read-only queue view
  - top-of-settings `Dashboard` heading with a curved 7-day line chart
  - asymmetric dashboard grid with 7-day `Plays`, 7-day `Tracks`, `Most artists`, and `Most tags`
  - persona textarea below the dashboard block
  - advanced maintenance section with DB path, provider-cache count, cleanup buttons, and explicit daemon stop

Important details:

- Runtime config file now stores exact `dashboardPort`, `daemonPort`, `defaultVolume`, and fixed `discoverRanking` weights.
- Runtime config also stores `autoStartDaemon`, which controls whether proxy sessions may auto-spawn the daemon.
- The daemon is not tied to the proxy terminal anymore; explicit stop only.
- `GET` / `POST` `/api/*` require `X-Agentune-Dashboard-Token`.
- `GET /api/artwork` and `WS /ws` require `dashboardToken`, and mutating browser requests must come from the same dashboard origin.
- `/api/artwork` now resolves DNS before fetch, validates redirects, and rejects blocked private/loopback/link-local targets.
- Static assets are resolved against the real `public/` root instead of relying on prefix string checks.
- The dashboard ships a local SVG logo plus `favicon.ico`; no external placeholder artwork request is needed for the empty state anymore.
- The old dashboard context badge is gone.
- `POST /api/persona` accepts only `taste`.
- Dashboard JSON body reads are bounded instead of buffering untrusted request bodies without a size cap.
- `POST /api/volume` rejects non-finite values and clamps accepted input into `0..100`.
- WebSocket volume updates also reject non-finite values.
- `GET /api/database/stats` now returns raw counts plus a smaller `insights` block sourced from SQLite aggregates: `plays7d`, `tracks7d`, `skipRate`, `activity7d`, top 3 artists, and enough top tags to fill the 2-row dashboard block.
- `public/app.js` loads initial playback and persona state with HTTP, listens for live `state` and `persona` messages, and refetches dashboard stats when the Settings view needs a fresher snapshot.
- `/api/artwork` only proxies remote `http` / `https` image responses, blocks loopback/private/link-local hosts, and caps proxied artwork size.
- Database cleanup actions stop playback, clear runtime queue state, then mutate SQLite.
- Destructive cleanup actions are serialized so overlapping dashboard requests cannot race each other.

## Tests and Validation

Current state-redesign coverage lives in:

- `src/audio/mpv-ipc-client.test.ts`
- `src/audio/mpv-launch-helpers.test.ts`
- `src/history/history-store-state-redesign.test.ts`
- `src/taste/taste-engine.test.ts`
- `src/taste/discover-pipeline.test.ts`
- `src/taste/discover-soft-ranker.test.ts`

`package.json` currently defines:

```json
"test": "npm run build && node --test dist/**/*.test.js"
```

That means every test run compiles first, then runs the built Node test suite from `dist/`.

Current CLI diagnostics coverage lives in:

- `src/cli/doctor-command.test.ts`
- `src/cli/doctor-report.test.ts`

Direct dependency state as of 2026-03-22:

- `@modelcontextprotocol/sdk`, `better-sqlite3`, `@distube/ytsr`, and `zod` are already current.
- `ws` is now on `8.20.0`.
- `youtube-dl-exec` is now on `3.1.4`.
- `node-mpv` has been removed.

## Not Current Anymore

These are no longer current behavior:

- grouped 4-lane `discover()` responses
- `discover` modes changing lane ratios
- `intent.allowed_tags` / `intent.avoid_tags` shaping discover results
- Smart Search participation in the discover pipeline
- the older weighted taste runtime
- lane-based state summaries
- dashboard context badges

Historical changelog entries may still mention those older designs, but the active implementation does not.
```

## File: `docs/design-guidelines.md`
```markdown
# Design Guidelines

## Dashboard Direction

- Dashboard UI follows an artwork-first music-player model, not a desktop card dashboard.
- Visual reference is Apple Music mood and hierarchy: calm, clean, layered, and mobile-first.
- Keep the experience centered and self-contained on desktop. Do not expand into split admin panes unless a future requirement demands it.

## Visual System

- Fonts:
  - UI/body: `Be Vietnam Pro`
  - Track title/display: `Outfit`
- Avoid Inter, Roboto, Arial, and generic purple-blue startup gradients.
- Base palette stays dark and neutral.
- Ambient color comes from the current track artwork through same-origin artwork proxy sampling.
- Surfaces use restrained translucency and tinted shadows. Do not add neon glow or loud glass effects.

## Layout Rules

- Primary dashboard shell is a single centered player container with:
  - top status row
  - full-screen tab views
  - pinned bottom navigation
- Tabs are:
  - `Queue`
  - `Now Playing`
  - `Settings`
- `Now Playing` stays the default and center nav action.
- Keep safe-area padding for the bottom tab bar and compact mobile widths.

## Player View

- Order:
  - 1:1 artwork
  - title
  - secondary artist/status copy
  - volume row
  - progress row
  - bottom nav
- Track title stays one line.
- Only enable marquee when measured overflow exists.
- Idle and stopped states must keep the same layout shape; only copy and status styling change.

## Queue View

- Queue is read-only.
- Show simple ordered items with title and artist.
- Empty and stopped states must use direct, plain copy.

## Settings View

- Settings order is:
  - `Dashboard`
  - `Your taste`
  - `Advanced`
- Keep the dashboard block minimal:
  - top header should use the same small uppercase label treatment as `Playing` in `Queue`
  - top header should only say `Dashboard`
  - one full-width curved `Last 7 days` line chart at the top
  - chart container should be frameless: no card background, no border
  - chart color should stay static white; do not bind it to artwork-driven accent colors
  - asymmetric grid underneath
  - `Plays` and `Tracks` should render as plain metrics, not boxed cards
  - `Plays`, `Tracks`, `Most artists`, and `Most tags` should all be scoped to the same trailing 7-day window as the chart
  - `Most artists` and `Most tags` should also be frameless
  - `Most artists` pinned on the right across both rows, without meter bars
  - `Most tags` spanning the lower left area as plain inline text chips: no fill, no border, no counts, wrap to fill 2 rows
  - `Most tags` heading should match `Most artists`, while tag values stay bright white
  - `Most artists` stays capped at 3 items; `Most tags` should use enough items to naturally fill the 2-row area
- Below the analytics block, add a separate `Preferences` section label using the same small uppercase queue-style heading treatment, with a clearer vertical break from the dashboard block above.
- The lower `Settings` content should also feel frameless; avoid wrapping `Taste` or `Advanced` in heavy card chrome.
- Use `Advanced Settings` as the lower maintenance section title.
- The `Taste` textarea should also stay plain: no background, no border, no manual resize handle, and its height should auto-grow with content instead of staying fixed at a multi-row default.
- The `Taste` save action should be a small centered circular outline button with a gray checkmark icon, not a filled CTA pill; center the status message below it.
- Keep persona taste editing on the main settings surface below analytics.
- Keep destructive controls under `Advanced`.
- Style the four destructive / maintenance actions as a restrained 2-column border-only button grid with no fill and no hover treatment; keep `Clear cache` and `Clear history` on the same neutral treatment, with `Clear cache` appearing first, while the harder actions stay red-tinted through border/text only.
- The `Last 7 days` chart should expose point values through a minimal tooltip: desktop uses hover/focus, mobile uses tap, and the tooltip itself should render as white numeric text only, with no filled bubble background.
- Keep the dashboard grid composition stable on mobile too; do not collapse the stats/artists/tags layout into a single-column fallback unless a later design change explicitly requires it.
- Preserve explicit confirmation for cleanup and daemon stop actions.
- Do not add extra admin controls unless they already exist in runtime behavior.

## Motion and Interaction

- Only animate `transform`, `opacity`, and necessary background transitions.
- Keep transitions in the 180-420ms range.
- Respect `prefers-reduced-motion`; marquee and palette transitions should calm down or stop.
- Keep keyboard focus visible on nav, buttons, summary toggles, and textarea.

## Implementation Notes

- Use `/api/artwork?src=...` for dashboard artwork display and palette extraction.
- Do not sample remote artwork URLs directly in canvas.
- Keep front-end modules small and focused; avoid large single-file dashboard scripts.
```

## File: `docs/project-changelog.md`
```markdown
# Project Changelog

## 2026-03-22 (CI Stability: Authenticated yt-dlp Download + Bounded Doctor Probes)

### CI
- Added job-level `GITHUB_TOKEN` in `.github/workflows/ci.yml` so `youtube-dl-exec` postinstall can authenticate against GitHub Releases during `npm ci` and tarball install verification.
- This removes the unauthenticated API-rate-limit failure seen on `macos-latest`.

### CLI Diagnostics
- Hardened external command probes in:
  - `src/cli/doctor-runtime-support.ts`
  - `src/audio/mpv-launch-helpers.ts`
- `doctor` now bounds `where` / `which` / `--version` subprocesses with a 5s timeout and hides Windows console windows for probe commands.
- This prevents CI jobs from hanging indefinitely when a runtime binary lookup or version probe stalls on a hosted runner.

### Tests
- Added `src/cli/doctor-runtime-support.test.ts` coverage for:
  - first non-empty line resolution
  - forced timeout handling for hung subprocesses

### Validation
- `npm run build`: passed
- `npm test`: 128 passed, 0 failed
- `npm run verify:publish`: passed
- `node dist/index.js doctor`: passed

## 2026-03-22 (Compiled Test Runner Compatibility)

### CI / Test Scripts
- Replaced the compiled test command glob with `scripts/run-compiled-tests.mjs`.
- The new runner walks `dist/` recursively and passes explicit `*.test.js` paths into `node --test`.
- This removes the Windows + Node.js 20 glob expansion mismatch that broke `npm run verify:publish` in GitHub Actions.

### Validation
- `npm test`: passed
- `npm run verify:publish`: passed
- `node dist/index.js doctor`: passed

## 2026-03-22 (Cross-Platform GitHub Actions CI Matrix)

### CI
- Added `.github/workflows/ci.yml` for OSS validation on:
  - `ubuntu-latest`
  - `windows-latest`
  - `macos-latest`
- Workflow policy:
  - Node.js `20`
  - npm dependency cache via `actions/setup-node`
  - `strategy.fail-fast: false`
  - `pull_request`, `push`, and manual dispatch support
  - read-only workflow permissions and in-progress cancellation per ref
- Each matrix job now:
  - runs `npm ci`
  - installs runtime dependencies for that OS
  - runs `npm run verify:publish`
  - runs `node dist/index.js doctor`

### Validation
- Local workflow authoring only; first GitHub-hosted runner execution is pending.

## 2026-03-22 (CLI Doctor Diagnostics)

### CLI
- Added `agentune doctor` in:
  - `src/index.ts`
  - `src/cli/doctor-command.ts`
  - `src/cli/doctor-report.ts`
  - `src/cli/doctor-runtime-support.ts`
  - `src/package-metadata.ts`
- `doctor` now reports:
  - Node.js compatibility against `package.json.engines.node`
  - runtime config status and resolved ports
  - `mpv` availability + version
  - bundled `youtube-dl-exec` `yt-dlp` availability + version
  - system `yt-dlp` availability + version
  - daemon state (`healthy`, `stopped`, `stale`, `unresponsive`)
  - runtime data paths (`config`, `history.db`, `daemon.pid`, `daemon.log`)
- Exit code policy:
  - exits `1` on required failures only
  - required: Node.js, runtime config, `mpv`, bundled `yt-dlp`
  - advisory: system `yt-dlp`, daemon stopped / unhealthy

### Supporting Runtime Change
- Extended `src/audio/mpv-launch-helpers.ts` with `resolveInstalledMpvBinary()` so CLI diagnostics and runtime code share `mpv` lookup behavior.

### Tests
- Added CLI diagnostics coverage in:
  - `src/cli/doctor-command.test.ts`
  - `src/cli/doctor-report.test.ts`
- Updated `src/cli/meta-command.test.ts` to lock `agentune doctor` in help output.

### Documentation
- Updated:
  - `README.md`
  - `docs/codebase-summary.md`
  - `docs/system-architecture.md`
  - `docs/project-roadmap.md`
  - `docs/project-overview-pdr.md`

### Validation
- `npm run build`: passed
- `npm test`: 126 passed, 0 failed
- `node dist/index.js doctor`: passed

## 2026-03-22 (Dependency Refresh + Internal MPV IPC Adapter)

### Dependency Refresh
- Removed `node-mpv` from direct dependencies in:
  - `package.json`
  - `package-lock.json`
- Updated direct runtime dependencies:
  - `ws` -> `8.20.0`
  - `youtube-dl-exec` -> `3.1.4`
- Kept `better-sqlite3`, `@modelcontextprotocol/sdk`, `@distube/ytsr`, and `zod` unchanged because they were already current for this repo on 2026-03-22.

### Audio Runtime
- Replaced the wrapper-based mpv integration with a small internal JSON IPC stack in:
  - `src/audio/mpv-controller.ts`
  - `src/audio/mpv-process-session.ts`
  - `src/audio/mpv-ipc-client.ts`
  - `src/audio/mpv-launch-helpers.ts`
- Deleted the obsolete wrapper glue and type shim:
  - `src/audio/node-mpv-bootstrap.ts`
  - `src/audio/node-mpv-bootstrap.test.ts`
  - `src/types/node-mpv.d.ts`
- The controller contract stayed stable for queue, MCP, and dashboard code:
  - `play`
  - `pause`
  - `resume`
  - `stop`
  - `setVolume`
  - `toggleMute`
  - `getPosition`
  - `getDuration`
  - `state-change` / `paused` / `resumed` / `stopped`
- Natural track-end handling now comes from observed `idle-active` IPC transitions instead of wrapper-specific events.
- Windows launch behavior still prefers `mpv.exe` and hides the managed mpv console window.

### Publish Verification
- Tightened tarball install verification in:
  - `scripts/verify-publish.mjs`
- Publish verification now fails on unexpected install deprecation warnings.
- The only explicitly accepted residual warning is:
  - `better-sqlite3` -> `prebuild-install`

### Tests + Validation
- Added audio coverage in:
  - `src/audio/mpv-ipc-client.test.ts`
  - `src/audio/mpv-launch-helpers.test.ts`
- Validation:
  - `npm outdated --json`: empty
  - `npm test`: 118 passed, 0 failed
  - `npm run verify:publish`: passed

## 2026-03-21 (CLI Help and Version Flags)

### CLI
- Added root CLI metadata commands in `src/index.ts`:
  - `agentune --version`
  - `agentune -v`
  - `agentune version`
  - `agentune --help`
  - `agentune -h`
  - `agentune help`
- These commands now exit immediately instead of falling through to MCP proxy mode.
- `--help` prints a short usage summary for proxy mode and daemon subcommands.
- `--version` reads the package version from `package.json` so installed CLI version is easy to verify.

### Tests
- Added `src/cli/meta-command.test.ts` to execute the compiled CLI and verify:
  - `agentune --version` prints the package version
  - `agentune --help` prints usage and exits cleanly

### Documentation
- Updated `README.md` quick start to mention `agentune --version` and `agentune --help`.

## 2026-03-21 (CLI-Only Publish Standardization)

### Release Workflow
- Standardized npm release flow around local-gated scripts in:
  - `package.json`
  - `scripts/publish-utils.mjs`
  - `scripts/verify-publish.mjs`
  - `scripts/release.mjs`
  - `.npmignore`
  - `LICENSE`
- The package is now treated as CLI-only release surface:
  - removed the root `main` entry from `package.json`
  - kept only `bin.agentune`
  - documented programmatic import as unsupported
- Added publish metadata gates:
  - `engines.node >= 20`
  - `publishConfig.access = public`
  - repository/homepage/bugs links for the GitHub repo
- Added a manual-publish guard:
  - raw `npm publish` now fails unless invoked by the release script
- Added release commands:
  - `npm run verify:publish`
  - `npm run release:alpha -- --bump ...`
  - `npm run release:stable -- --bump ...`

### Tarball Hygiene
- Tarball filtering now excludes compiled tests, sourcemaps, and test-helper artifacts from `dist/`.
- `verify:publish` now checks:
  - package metadata
  - LICENSE presence
  - build + test gate
  - `npm pack --dry-run` file surface
  - install-from-tarball smoke
  - CLI-only import boundary

### Documentation
- Updated release guidance in:
  - `README.md`
  - `docs/project-roadmap.md`
  - `docs/project-overview-pdr.md`
- Added alpha channel install guidance and stable/alpha dist-tag policy.

### Validation
- `npm test`: 114 passed, 0 failed
- `npm run verify:publish`: passed
- `npm publish --dry-run`: intentionally blocked unless using `release:alpha` or `release:stable`

## 2026-03-21 (Resolver Original-Only Hard Blocking)

### Resolver Filtering
- Tightened YouTube resolver candidate filtering in:
  - `src/providers/search-result-scorer.ts`
  - `src/providers/search-result-scorer.test.ts`
  - `src/mcp/song-resolver.test.ts`
- The resolver now removes obvious non-original variants before scoring instead of only applying soft penalties.
- Hard-blocked variants now include common alternate-version keywords such as:
  - `cover`
  - `karaoke`
  - `instrumental`
  - `acoustic`
  - `piano`
  - `tribute`
  - `remake`
  - `fanmade`
  - `slowed`
  - `sped up`
  - `nightcore`
  - `8d`
  - `reverb`
  - `live`
  - `remix`
  - `teaser`
  - `preview`
  - `shorts`
  - `playlist`
  - `full album`
- Matching now checks both result titles and channel names using normalized token/phrase boundaries instead of loose substring checks.
- Explicit user queries like `cover` or `live` still allow those variants through when the keyword is part of the requested song input.

## 2026-03-21 (Default Artwork Flicker Fix)

### Root Cause + Fix
- Fixed the empty-state dashboard artwork jitter in:
  - `src/web/web-server-helpers.ts`
  - `public/dashboard/render.js`
  - `src/web/web-server-playback-controls.test.ts`
- Root cause:
  - local `.svg` assets were being served as `application/octet-stream` instead of `image/svg+xml`
  - the artwork fallback guard compared an absolute browser URL with a relative placeholder path, which could reassign the same fallback source repeatedly on image errors
- The dashboard now serves local SVG artwork with the correct MIME type and avoids placeholder reassign loops.

## 2026-03-21 (Dashboard Favicon + Local Default Artwork)

### Asset Update
- Added a reusable local logo asset in:
  - `public/assets/agentune-mark.svg`
- Replaced the initial local placeholder mark with a lighter SVG waveform logo based on the provided dashboard brand image.
- Removed the SVG background fill so the default artwork now renders with transparency.
- Updated the browser favicon in:
  - `public/favicon.ico`
- The dashboard favicon now uses the provided `ChatGPT Image Mar 21, 2026, 08_30_12 PM.ico` asset.
- Replaced the remote `placehold.co` fallback image in:
  - `public/index.html`
  - `public/dashboard/constants.js`
- The dashboard now uses the local logo asset as its default artwork, which removes an unnecessary external request and shrinks the placeholder payload substantially.
- `index.html` now points favicon loading directly at `/favicon.ico`.

## 2026-03-21 (Local Web Hardening + Safer Daemon Stop)

### Web Hardening
- Hardened dashboard request handling in:
  - `src/web/web-server-helpers.ts`
  - `src/web/web-server-auth.ts`
  - `src/web/web-server-static-file-path.ts`
  - `src/web/web-server.ts`
  - `src/web/web-server-artwork-proxy.ts`
  - `src/web/web-server-database-cleanup.ts`
  - `public/dashboard/auth.js`
  - `public/dashboard/settings-api.js`
  - `public/dashboard/theme.js`
  - `public/dashboard/render.js`
  - `public/app.js`
- `GET /` now serves dashboard HTML with a per-process session token injected into a `<meta>` tag.
- Dashboard routes now require local session auth:
  - `GET` / `POST` `/api/*` require `X-Agentune-Dashboard-Token`
  - `GET /api/artwork` and `WS /ws` require `dashboardToken`
  - mutating `POST` routes and `WS /ws` also require same-origin browser requests
- Old dashboard tabs now fail closed after daemon restart and render a refresh-required state instead of reconnecting forever.
- Added bounded request-body reads for dashboard JSON posts.
- Tightened `/api/volume` validation:
  - rejects non-finite input
  - clamps accepted values into `0..100`
  - applies the same finite-number guard to WebSocket volume messages
- Tightened `/api/artwork`:
  - still only accepts `http` / `https`
  - now rejects loopback, private-network, and link-local targets
  - now resolves hostnames and rejects DNS results that land on blocked IP ranges
  - now validates redirect targets instead of following them blindly
  - now requires upstream `image/*` content
  - now caps proxied artwork size instead of buffering unbounded responses
- Replaced static file prefix checks with resolved-path validation so Windows `public` / `publicity` prefix collisions cannot escape the real `public/` root.
- Serialized destructive dashboard database actions so concurrent cleanup clicks cannot overlap server-side reset work.

### Daemon Lifecycle Hardening
- Hardened daemon entrypoint resolution in:
  - `src/proxy/daemon-launcher.ts`
- The detached launcher now resolves the compiled daemon entrypoint from module location instead of relying on `process.argv[1]`, which is safer for global install and shimmed invocation paths.
- Added daemon control-token auth in:
  - `src/daemon/daemon-auth.ts`
  - `src/daemon/daemon-server.ts`
  - `src/daemon/pid-manager.ts`
  - `src/proxy/stdio-proxy.ts`
  - `src/cli/stop-command.ts`
  - `src/index.ts`
- The PID file now stores a daemon control token.
- `/mcp` and `/shutdown` now require `X-Agentune-Daemon-Token`; `/health` stays unauthenticated for readiness checks.
- Hardened `agentune stop` in:
  - `src/cli/stop-command.ts`
- Stop now:
  - waits for graceful daemon shutdown after `/shutdown`
  - only falls back to process kill after verifying the target still looks like an `agentune` daemon
  - refuses blind PID kills when identity cannot be verified
- Hardened daemon shutdown cleanup in:
  - `src/index.ts`
- Shutdown is now idempotent and best-effort across queue cleanup, HTTP servers, SQLite close, mpv teardown, and PID-file removal.

### Regression Coverage
- Added daemon stop coverage in:
  - `src/cli/stop-command.test.ts`
  - `src/daemon/daemon-server.test.ts`
- Expanded dashboard hardening coverage in:
  - `src/web/web-server-artwork-proxy.test.ts`
  - `src/web/web-server-database-cleanup.test.ts`
  - `src/web/web-server-playback-controls.test.ts`
  - `src/web/web-server-persona-sync.test.ts`
  - `src/web/web-server-test-helpers.ts`
  - `src/proxy/daemon-launcher.test.ts`

### Validation
- `npm test`: 126 passed, 0 failed

## 2026-03-21 (Ambient Background Theme Transition Smoothing)

### Dashboard Background Motion
- Smoothed dashboard ambient color changes on track switch in:
  - `public/style.css`
- Registered the artwork-driven background color tokens with `@property` so the gradient can interpolate instead of snapping when a new palette arrives.
- Limited the motion change to the background color treatment only:
  - artwork swap behavior stays unchanged
  - title and metadata updates stay immediate

### Validation
- `npm run build`: passed

## 2026-03-21 (Concurrent add_song Queue Race Fix)

### Root Cause + Fix
- Fixed a queue race where multiple `add_song` calls arriving at nearly the same time could all observe `nowPlaying === null`, then each independently drain one item from the queue and trigger competing playback starts.
- The result was lost queue entries in practice: one later start would replace an earlier one, so several requested songs disappeared from the visible queue and never got a real turn.
- Serialized playback and queue mutations in:
  - `src/queue/queue-playback-controller.ts`
- `addById()` now reuses the already-resolved audio for the same song when it is the track that should start from an idle queue, instead of re-resolving and racing a second queue drain.
- Applied the same mutation lock to skip, replace-current, natural stop handling, and runtime reset so queue/playback state advances linearly.

### Regression Coverage
- Added concurrent queue coverage in:
  - `src/queue/queue-playback-controller.test.ts`
- Locked the bulk-add guarantee:
  - 20 concurrent `addById()` calls keep exactly 1 track playing and 19 still queued
  - only 1 playback start is issued for the idle-transition path

### Validation
- `npm run build`: passed
- `npm test`: 109 passed, 0 failed

## 2026-03-21 (Queue Auto-Advance After Natural Track End)

### Root Cause + Fix
- Fixed a startup-timing bug where the first playback command could reach `node-mpv` before the idle IPC warmup completed, which caused later EOF stop events to be missed and left the queue stuck until a manual skip.
- Added an mpv startup warmup gate in:
  - `src/audio/mpv-controller.ts`
  - `src/index.ts`
- The daemon now waits briefly after `mpv.init()` before it starts serving playback commands, so natural track end can advance the queue reliably.

### Regression Coverage
- Added queue-controller coverage for natural stop-driven advancement in:
  - `src/queue/queue-playback-controller.test.ts`

### Validation
- `npm test`: 108 passed, 0 failed
- Runtime probe with real `mpv` + two 1-second WAV files:
  - first track ended naturally
  - next track started automatically
  - queue drained into history without manual skip

## 2026-03-21 (Paused Playback Visual Effects)

### Dashboard Pause State
- Added a dedicated playback visual-state mapper in:
  - `public/dashboard/playback-visual-state.js`
- Dashboard render now writes `data-playback-visual-state` to the document root so the paused look stays driven by playback state instead of ad-hoc DOM styling in:
  - `public/dashboard/render.js`

### Pause/Resume Motion + Tone Shift
- Added paused-state transitions in:
  - `public/style.css`
- Locked the paused visual treatment to:
  - slightly larger play icon while paused
  - main artwork and queue-current artwork scaling down toward center
  - artwork shifting to a near-monochrome, desaturated look
  - ambient background desaturating and dimming while paused
  - full color and scale restoring on resume
- Adjusted the paused artwork zoom so the frame components scale instead of only the inner image, preventing exposed frame background during pause.

### Regression Coverage
- Added playback visual-state coverage in:
  - `src/web/playback-visual-state.test.ts`
- Locked these mappings:
  - no track -> `idle`
  - active track + playing -> `playing`
  - active track + paused -> `paused`

### Validation
- `node --check public/dashboard/render.js`: passed
- `node --check public/dashboard/playback-visual-state.js`: passed
- `npm test`: 107 passed, 0 failed

## 2026-03-21 (Dashboard Pause/Resume Control Fix)

### Playback Control Fix
- Fixed the dashboard primary transport button so it now sends WebSocket `playback-toggle` instead of the old pause-only event in:
  - `public/app.js`
- Updated dashboard playback rendering so the primary transport button:
  - stays enabled while a track exists, even when paused
  - swaps between pause and play icons based on playback state
  - updates its `aria-label` to `Pause playback` or `Resume playback` in:
    - `public/dashboard/render.js`

### Regression Coverage
- Expanded WebSocket playback control coverage in:
  - `src/web/web-server-playback-controls.test.ts`
- Locked these behaviors:
  - pause-only messages still remain one-way
  - `playback-toggle` resumes paused playback
  - `playback-toggle` can pause again before resuming and skipping forward

### State Sync Hardening
- Removed direct pause/play icon flipping from:
  - `public/app.js`
- Let dashboard render state remain the single source of truth for the primary transport icon.
- Ignored stale `/api/status` bootstrap data once live socket state or a playback control action already exists in:
  - `public/app.js`
- Dropped older in-flight dashboard refreshes so a slower pre-pause refresh cannot overwrite a newer paused snapshot in:
  - `src/web/state-broadcaster.ts`
- Added overlap coverage in:
  - `src/web/state-broadcaster.test.ts`

### Skip From Pause
- Fixed queue playback so skipping while paused clears mpv's lingering pause flag before the next track starts in:
  - `src/queue/queue-playback-controller.ts`
- Added regression coverage for:
  - queue-level pause-then-skip playback recovery in `src/queue/queue-playback-controller.test.ts`
  - dashboard WebSocket pause-then-next behavior in `src/web/web-server-playback-controls.test.ts`

### Transport Icon Rendering
- Fixed the dashboard transport icon toggle to update the real `hidden` attribute on inline SVG nodes instead of writing the non-reflected `.hidden` property in:
  - `public/dashboard/render.js`
  - `public/dashboard/toggle-hidden-attribute.js`
- Added regression coverage for the attribute-based SVG visibility path in:
  - `src/web/toggle-hidden-attribute.test.ts`

### Validation
- `npm run build`: passed
- `node --check public/app.js`: passed
- `node --check public/dashboard/render.js`: passed
- `npm test`: 103 passed, 0 failed

## 2026-03-21 (Minimal Dashboard Layout Revision)

### Dashboard Layout
- Simplified the Settings analytics surface into a more minimal `Dashboard` block
- Reduced copy so the top of the view now starts with a single `Dashboard` heading
- Kept only `Dashboard` at the top of the analytics block and moved `Settings` into its own lower section heading, using the same compact label style as `Playing` / `Up next`
- Removed card chrome from the lower `Settings` content too, so `Taste` and `Advanced` now read as frameless sections
- Renamed the lower section label from `Settings` to `Preferences`, added more vertical separation from the dashboard block, and renamed the maintenance section to `Advanced Settings`
- Flattened the `Taste` textarea itself as well: no border, no background, and no resize handle
- Replaced the `Taste` save CTA with a minimal circular outline button using a gray checkmark icon
- Centered the `Taste` save button and the `Persona saved.` feedback line in the frameless settings area
- Restyled the four maintenance buttons into a cleaner 2-column outline grid with softer surfaces and red-tinted emphasis only on destructive actions
- Moved `Clear cache` ahead of `Clear history` and aligned both to the same neutral outline style
- Removed fill and hover styling from all four maintenance buttons so the group now reads as pure border-only controls
- Added interactive count tooltips to the `Last 7 days` chart: hover/focus on desktop, tap on mobile, with a minimal numeric-only bubble per point
- Removed the tooltip bubble chrome from the `Last 7 days` chart so hover/tap now shows only the white count text
- Removed the mobile-only single-column fallback for the dashboard grid so the current asymmetric composition stays intact on narrow screens too
- Changed the `Taste` textarea to auto-grow with its content, including initial persona load and live typing
- Fixed the hidden-settings regression where `Taste` could render at `0px` height after persona preload by re-syncing textarea height when the `Preferences` view becomes visible
- Scoped dashboard `Plays`, `Tracks`, `Most artists`, and `Most tags` to the same trailing 7-day window as the chart while keeping raw DB counts intact for `Advanced Settings`
- Reworked the dashboard area into:
  - one full-width `Last 7 days` card
  - an asymmetric grid below it
  - `Plays` and `Tracks` on the top-left row
  - `Most artists` pinned on the right across two rows
  - `Most tags` spanning the lower-left row
- Removed the old `Avg completion` and `Recent plays` dashboard blocks
- Hid the Settings scrollbar chrome while keeping scroll behavior intact
- Removed card chrome from the chart, `Plays`, and `Tracks` so the top dashboard area reads more like a layout than stacked panels
- Made `Most artists` and `Most tags` frameless too, removed artist meter bars, and changed tags into plain outlined chips without counts
- Centered `Plays` and `Tracks`, then removed the tag chip borders and lifted the 3-tag cap so the tag block can fill two wrapped rows
- Synced frameless tag text and the `Most artists` heading to the same muted label color used by `Plays` and `Tracks`
- Kept the `Most tags` heading aligned with `Most artists`, but restored the tag values themselves to bright white
- Decoupled the dashboard line chart from artwork theming so the line, points, and area tint stay white

### Chart + Data Contract
- Replaced the old bar-style activity view with a curved SVG line chart in `public/dashboard/insights.js`
- Trimmed `GET /api/database/stats` insights to:
  - `skipRate`
  - `activity7d`
  - top 3 artists
  - top tags for the 2-row dashboard block
- Kept raw DB `counts` intact for maintenance UI compatibility

### Validation
- Updated coverage in:
  - `src/history/history-store.test.ts`
  - `src/web/web-server-database-cleanup.test.ts`
- Validation:
  - `npm run build`: passed
  - `npm test`: 99 passed, 0 failed
  - `node --check public/app.js`: passed
  - `node --check public/dashboard/insights.js`: passed
  - `node --check public/dashboard/dom.js`: passed

## 2026-03-21 (Settings Refresh + SQLite Listening Insights)

### Settings Layout + Front-End Structure
- Rebuilt the `Settings` view into a clearer vertical hierarchy:
  - `Listening insights`
  - `Your taste`
  - `Advanced`
- Added a dedicated settings stylesheet in:
  - `public/styles/dashboard-settings.css`
- Added focused dashboard modules for settings data and insights rendering in:
  - `public/dashboard/insights.js`
  - `public/dashboard/settings-api.js`
- Updated:
  - `public/index.html`
  - `public/app.js`
  - `public/dashboard/dom.js`
  - `public/dashboard/render.js`
  - `public/style.css`

### Dashboard Insights
- Expanded `GET /api/database/stats` to return:
  - raw counts
  - avg completion
  - skip rate
  - 7-day activity buckets
  - top artists
  - top keywords
  - recent plays
- Added lightweight Settings analytics UI:
  - KPI cards
  - clean 7-day activity chart
  - ranked artist meters
  - keyword chips
  - recent-play list
- Refreshed Settings stats on:
  - initial load
  - Settings tab open
  - cleanup actions
  - current-track changes while Settings is open

### History Store + Validation
- Extended `src/history/history-store.ts` so dashboard stats derive from real SQLite aggregates instead of maintenance counts only
- Added/updated coverage in:
  - `src/history/history-store.test.ts`
  - `src/web/web-server-database-cleanup.test.ts`
- Validation:
  - `npm run build`: passed
  - `npm test`: 98 passed, 0 failed
  - `node --check public/app.js`: passed
  - `node --check public/dashboard/insights.js`: passed
  - `node --check public/dashboard/settings-api.js`: passed

## 2026-03-20 (Dashboard Playback Controls + Client Mapping Fix)

### Dashboard Controls
- Moved the primary `Pause` control above the volume row and centered it in the player layout
- Added a dedicated `Next track` control beside `Pause` in:
  - `public/index.html`
  - `public/style.css`
- Added a playback duration row above the transport controls with:
  - elapsed time on the left
  - full track duration on the right
  - a slim progress bar synced to current playback position
- Reworked the `Queue` view so the current track appears in a dedicated artwork + metadata row above a flat queue list without card borders/backgrounds
- Moved playback controls into one shared dashboard block so `Playing` and `Queue` keep the same duration / transport / volume positions, and made the `Up next` list independently scrollable
- Added a smooth shared-element artwork transition between `Now Playing` and `Queue` when switching tabs in browsers that support View Transitions
- Corrected transport semantics so the dashboard `Pause` control sends pause-only behavior while `Next` remains skip
- Removed the mute button from the player strip
- Replaced the mute button and volume percentage with decorative speaker icons on both sides of the volume slider
- Removed background chrome from the `Pause` and `Next` buttons so transport controls render as plain icons
- Reconnected dashboard background and glass surfaces to the extracted artwork palette instead of fixed gradient values

### Client/Server Mapping Fix
- Re-aligned the browser dashboard modules with the current `public/index.html` selectors in:
  - `public/app.js`
  - `public/dashboard/dom.js`
  - `public/dashboard/marquee.js`
  - `public/dashboard/render.js`
- Reworked overflow title animation so text scrolls inside its own viewport in stepped motion instead of translating the whole heading block
- Restored working dashboard playback actions by wiring WebSocket control messages for:
  - pause/resume toggle
  - next/skip
- Added album-art fallback logic so the dashboard uses the raw thumbnail URL if `/api/artwork` fails on an older running daemon
- Updated `public/dashboard/theme.js` to sample artwork from the proxy first, then fall back to the raw thumbnail URL
- Fixed the remaining palette extraction blocker by loading remote artwork with `crossOrigin = 'anonymous'` before canvas sampling
- Added WebSocket playback control coverage in:
  - `src/web/web-server-playback-controls.test.ts`

### Docs + Validation
- Synced `README.md` and `docs/codebase-summary.md` to the current dashboard control surface
- Validation:
  - `npm run build`: passed
  - `npm test`: 96 passed, 0 failed

## 2026-03-20 (Apple-Music-Inspired Dashboard Redesign)

### Dashboard UX + Front-End Structure
- Rebuilt the browser dashboard into a player-first shell with full-screen `Queue / Now Playing / Settings` tabs
- Replaced the old multi-card layout in:
  - `public/index.html`
  - `public/style.css`
  - `public/app.js`
- Split dashboard front-end code into focused browser modules and CSS partials under:
  - `public/dashboard/`
  - `public/styles/`
- Added marquee-on-overflow title handling and a centered 1:1 artwork presentation
- Moved maintenance controls into an `Advanced` settings section while keeping persona editing on the main settings surface

### Artwork Proxy + Ambient Theming
- Added `GET /api/artwork?src=...` in:
  - `src/web/web-server.ts`
  - `src/web/web-server-artwork-proxy.ts`
- Dashboard artwork now renders through a same-origin proxy so the browser can safely sample colors for ambient gradient theming
- Added artwork proxy coverage in:
  - `src/web/web-server-artwork-proxy.test.ts`

### Docs + Validation
- Added `docs/design-guidelines.md` for the current dashboard visual system and interaction rules
- Synced `docs/codebase-summary.md`, `docs/system-architecture.md`, roadmap, and changelog to the redesigned dashboard surface
- Validation:
  - `npm run build`: passed
  - `npm test`: 95 passed, 0 failed

## 2026-03-20 (Optional Auto-Start + Manual Start Command)

### Daemon Startup Control
- Extended `${AGENTUNE_DATA_DIR || ~/.agentune}/config.json` with `autoStartDaemon`
- Default remains `true`, so existing users keep the same proxy auto-start behavior
- Runtime config loading now validates `autoStartDaemon` as a boolean
- Runtime config loading now writes normalized defaults back to disk when older config files are missing new fields

### CLI + Proxy Behavior
- Added `src/cli/start-command.ts` for `agentune start`
- `agentune start` now ensures the daemon is running in the background and exits after readiness succeeds
- Updated `src/index.ts` so proxy mode reads `autoStartDaemon` before deciding whether it may spawn the daemon
- Updated `src/proxy/daemon-launcher.ts` so launcher flows now support:
  - connect to a healthy running daemon without spawning
  - fail fast with a manual-start message when spawning is disabled
  - report whether the daemon was newly started or already running

### Dashboard Copy + Tests + Docs
- Updated dashboard stop messaging to point users to `agentune start` while still mentioning new-session auto-start when enabled
- Added launcher coverage in `src/proxy/daemon-launcher.test.ts`
- Updated runtime config tests to cover `autoStartDaemon` defaults, validation, and config write-back
- Synced README, system architecture, codebase summary, roadmap, and changelog to the optional auto-start flow

### Validation
- `npm run build`: passed
- `npm test`: 92 passed, 0 failed

## 2026-03-20 (Hide Windows MPV Console Window)

### Windows Playback Startup
- Updated `src/audio/mpv-controller.ts` and added `src/audio/node-mpv-bootstrap.ts`
- Windows `mpv` startup now prefers `mpv.exe` over the console wrapper when available
- `node-mpv` is now loaded through a Windows-specific spawn patch so its child `mpv` process starts with `windowsHide: true`
- Added `--terminal=no` to the managed `mpv` args to suppress terminal output noise
- Result: the blank Windows console window should no longer appear when a coding session auto-starts `agentune`

### Tests
- Added coverage for the Windows launch helpers in `src/audio/node-mpv-bootstrap.test.ts`

## 2026-03-20 (Explicit Daemon Stop Only)

### Daemon Lifecycle
- Removed daemon idle auto-shutdown from `src/daemon/daemon-server.ts`
- Proxy-spawned daemon now detaches on Windows too in `src/proxy/daemon-launcher.ts`, so playback survives terminal closure
- Daemon now stops only through explicit shutdown paths:
  - `agentune stop`
  - daemon `/shutdown`
  - dashboard `Stop daemon`

### Dashboard Stop Control
- Added `POST /api/daemon/stop` in `src/web/web-server.ts`
- Wired dashboard stop requests to the same daemon shutdown path used by the CLI via `src/index.ts`
- Added `Stop daemon` button and stopped-state UX in:
  - `public/index.html`
  - `public/app.js`
  - `public/style.css`
- After a dashboard stop, the page shows a stopped state, disables controls, and stops reconnecting until agentune is started again

### Tests + Docs
- Added web coverage for the explicit daemon stop route in `src/web/web-server-database-cleanup.test.ts`
- Synced README, system architecture, codebase summary, roadmap, and changelog to the explicit-stop lifecycle
- Validation:
  - `npm run build`: passed
  - `npm test`: 86 passed, 0 failed

## 2026-03-20 (Agent-Facing Discover Guidance Cleanup)

### MCP Contract Cleanup
- Tightened the agent-facing state/discover surface to reduce ambiguous field names and follow-up hallucination:
  - `src/taste/taste-engine.ts`
  - `src/mcp/mcp-server.ts`
  - `src/mcp/tool-handlers.ts`
  - `src/taste/discover-batch-builder.ts`
  - `src/taste/discover-pagination-cache.ts`
  - `src/taste/discover-pipeline.ts`
- `get_session_state()` now returns:
  - `persona: { Preferences }`
  - `history.stats.topKeywords`
- `discover()` now accepts `keywords` instead of `genres`
- public discover candidates now return `keywords` instead of `tags`
- `discover()` now always returns `nextGuide` so the agent knows whether to:
  - keep the same search and change page
  - or improve `artist` / `keywords`
- Removed the old discover success `tip` field from MCP output

### Tests + Docs
- Updated discover pipeline tests and persona sync cache tests to the new `keywords` contract
- Synced README, codebase summary, system architecture, and roadmap to the new agent-facing field names
- Validation:
  - `npm run build`: passed
  - `npm test`: 85 passed, 0 failed

## 2026-03-20 (Config-Driven Ranking + Default Volume)

### Persona Surface Simplification
- Removed manual persona traits from the active runtime contract:
  - `src/taste/taste-engine.ts`
  - `src/history/history-schema.ts`
  - `src/history/history-store.ts`
  - `src/history/history-store-migrations.ts`
- `session_state` now keeps only `persona_taste_text`
- `get_session_state()` now returns `persona: { taste }`
- Removed MCP tool `set_persona_traits` and updated dashboard `/api/persona` to accept only `taste`

### Runtime Config Expansion
- Extended `${AGENTUNE_DATA_DIR || ~/.agentune}/config.json` with:
  - `defaultVolume`
  - `discoverRanking`
- Default runtime config is now:
  - `dashboardPort: 3737`
  - `daemonPort: 3747`
  - `defaultVolume: 80`
  - `discoverRanking: { exploration: 0.35, variety: 0.55, loyalty: 0.65 }`
- `src/audio/mpv-controller.ts` now starts mpv with configured `defaultVolume`
- `src/taste/discover-pipeline.ts` and `src/taste/discover-soft-ranker.ts` now read fixed ranking weights from runtime config instead of persona state

### Dashboard + Tests + Validation
- Removed dashboard trait sliders and rewired the persona editor to taste-only updates
- Updated state-redesign tests, persona sync tests, runtime config tests, and discover pipeline tests to the new contract
- Validation:
  - `npm run build`: passed
  - `npm test`: 85 passed, 0 failed

## 2026-03-20 (Runtime Config + DB Cleanup)

### Exact Port Config + Shared Data Dir
- Added shared runtime path/config modules:
  - `src/runtime/runtime-data-paths.ts`
  - `src/runtime/runtime-config.ts`
- `config.json` is now created automatically in `${AGENTUNE_DATA_DIR || ~/.agentune}/config.json`
- Runtime config currently supports:
  - `dashboardPort`
  - `daemonPort`
- Updated daemon, proxy, PID, log, DB, and web startup paths to read from the shared data-dir/config layer
- Removed dashboard port fallback behavior; dashboard and daemon now bind exact configured ports and fail fast if occupied
- Added `src/runtime/runtime-config.test.ts` to lock default-file creation and config validation

### SQLite Schema Cleanup + Maintenance
- Refactored `src/history/history-schema.ts` to the trimmed active schema:
  - kept `tracks`, `plays`, `session_state`, `provider_cache`
  - removed legacy `preferences`
  - removed legacy `tracks.similar_json`
  - removed legacy `plays.lane_id`
  - removed legacy session-state JSON columns
- Added migration layer in:
  - `src/history/history-store-migrations.ts`
  - `src/history/history-store-maintenance.ts`
- History store now migrates older DBs to schema version 2 and adds current indexes for:
  - `plays(track_id, started_at DESC)`
  - `tracks(play_count DESC) WHERE play_count > 0`
  - `provider_cache(fetched_at)`
- Added history-store cleanup operations:
  - `clearHistory()`
  - `clearProviderCache()`
  - `fullReset()`
- Cleanup now runs `wal_checkpoint(TRUNCATE)`, `VACUUM`, and `PRAGMA optimize`

### Dashboard Database Controls
- Added dashboard database routes in `src/web/web-server.ts`:
  - `GET /api/database/stats`
  - `POST /api/database/clear-history`
  - `POST /api/database/clear-provider-cache`
  - `POST /api/database/full-reset`
- Added cleanup helper module `src/web/web-server-database-cleanup.ts`
- Added database section to dashboard UI in:
  - `public/index.html`
  - `public/app.js`
  - `public/style.css`
- Cleanup actions now:
  - require 2-step confirm in the dashboard
  - stop active playback
  - clear runtime queue state
  - invalidate discover cache
  - keep persona taste intact

### Tests + Validation
- Rewrote history-store tests around the trimmed API in:
  - `src/history/history-store.test.ts`
  - `src/history/history-store-state-redesign.test.ts`
- Added web cleanup coverage in:
  - `src/web/web-server-database-cleanup.test.ts`
- Updated `src/web/web-server-persona-sync.test.ts` for exact-port server startup
- Validation:
  - `npm run build`: passed
  - `npm test`: 85 passed, 0 failed

## 2026-03-19 (Hard Manual Persona Traits)

### Manual Persona Traits Are Now the Source of Truth
- Added durable `session_state.persona_traits_json` storage in:
  - `src/history/history-schema.ts`
  - `src/history/history-store.ts`
- Added runtime migration and strict `0..1` validation for persisted traits
- Refactored `src/taste/taste-engine.ts` so `get_session_state()` now returns stored manual traits instead of history-derived traits
- Added MCP tool `set_persona_traits({ exploration, variety, loyalty })` in:
  - `src/mcp/mcp-server.ts`
  - `src/mcp/tool-handlers.ts`
- Kept `update_persona({ taste })` taste-only and confirmed it no longer changes traits
- Updated dashboard persona flow in:
  - `src/web/web-server.ts`
  - `public/index.html`
  - `public/app.js`
  - `public/style.css`
- Dashboard `/api/persona` now accepts `taste`, `traits`, or both in one validated request
- Persona WebSocket broadcasts now send stored traits, not computed trait snapshots

### Discover Ranking + Cache Behavior
- Updated `src/taste/discover-pipeline.ts` to read stored traits via `getTraits()`
- Updated `src/taste/discover-soft-ranker.ts` so `variety` has a real but light nearby diversity effect
- Trait changes now invalidate discover pagination snapshots immediately
- Taste-only persona edits still leave discover cache intact

### Tests + Docs
- Updated tests to lock manual-trait behavior in:
  - `src/history/history-store-state-redesign.test.ts`
  - `src/taste/taste-engine.test.ts`
  - `src/taste/discover-soft-ranker.test.ts`
  - `src/taste/discover-pipeline.test.ts`
  - `src/web/web-server-persona-sync.test.ts`
- Synced manual-trait wording in `README.md`, `docs/codebase-summary.md`, `docs/system-architecture.md`, and `docs/project-roadmap.md`

### Validation
- `npm run build`: passed
- `npm test`: 97 passed, 0 failed

## 2026-03-19 (Discover Rewrite)

### Flat Apple-Only Discover Pipeline
- Confirmed the grouped discover lanes are replaced by the new flat flow:
  - `src/taste/discover-batch-builder.ts`
  - `src/taste/discover-merge-and-dedup.ts`
  - `src/taste/discover-soft-ranker.ts`
  - `src/taste/discover-pagination-cache.ts`
  - `src/taste/discover-pipeline.ts`
  - `src/mcp/mcp-server.ts`
  - `src/mcp/tool-handlers.ts`
- Confirmed public discover contract is now `discover(page?, limit?, artist?, genres?)`
- Confirmed default discover seeds come from top history artists + top history tags only
- Confirmed internal Apple IDs stay internal and are stripped before MCP output
- Confirmed successful `play_song()` / `add_song()` invalidate discover snapshots; `update_persona()` does not
- Removed the orphan Smart Search bootstrap and deleted `src/providers/smart-search-provider.ts`
- Startup logs now reflect the Apple-only discover runtime
- Synced plan + roadmap tracking docs to reflect the shipped discover rewrite instead of the older grouped-lane state

### Validation
- `npm run build`: passed
- `npm test`: 93 passed, 0 failed
- Discover rewrite test state:
  - `src/taste/discover-pipeline.test.ts`: passing
  - `src/taste/discover-soft-ranker.test.ts`: passing
- Built-handler smoke:
  - `handleDiscover({ artist: 'Nils Frahm', limit: 1 })` returned `{ page: 1, limit: 1, hasMore: true, candidates: [...] }`
- Remaining validation gap:
  - no full daemon/MCP smoke result recorded yet

## 2026-03-18 (Agent-First State Redesign Sync)

### Verified Current State Contract
- Re-verified the active state redesign against current source:
  - `src/history/history-schema.ts`
  - `src/history/history-store.ts`
  - `src/mcp/mcp-server.ts`
  - `src/mcp/tool-handlers.ts`
  - `src/queue/queue-playback-controller.ts`
  - `src/taste/candidate-generator.ts`
  - `src/taste/taste-engine.ts`
  - `src/web/state-broadcaster.ts`
  - `src/web/web-server-helpers.ts`
  - `src/web/web-server.ts`
  - `public/app.js`
  - `public/index.html`
  - `public/style.css`
  - `package.json`
- Confirmed `get_session_state()` now returns the agent-facing summary:
  - `context` with hour, period, and day of week
  - `persona` with `traits` plus persisted free-text `taste`
  - `history` with recent plays and top artists/tags
- Confirmed `update_persona({ taste })` is part of the MCP surface and persists `session_state.persona_taste_text`
- Confirmed `discover()` now returns grouped raw candidates from `continuation`, `comfort`, `contextFit`, and `wildcard`
- Confirmed the dashboard now exposes a persona editor through `GET /api/persona`, `POST /api/persona`, and `persona` WebSocket broadcasts

### Documentation Sync
- Updated `docs/system-architecture.md` to describe the current agent-first contract, grouped discover lanes, and dashboard persona editor
- Rewrote `docs/codebase-summary.md` from current source and refreshed repo context with `repomix-output.xml`
- Updated `README.md` wording where it still implied continuous session-lane state or server-side reranking
- Left older historical changelog entries intact as historical record; they no longer describe the current runtime

### Validation
- `npm test`
- Current local result: 77 passed, 0 failed
- State redesign coverage includes:
  - `src/history/history-store-state-redesign.test.ts`
  - `src/taste/taste-engine.test.ts`
  - `src/taste/candidate-generator.test.ts`

## 2026-03-17 (Daemon UX — Terminal Hide + Auto-Shutdown)

### Auto-Shutdown on Idle + Transparent Windows Daemon
- Updated `src/proxy/daemon-launcher.ts` — Added `windowsHide: true` to daemon spawn options
  - Prevents visible terminal window popup when daemon auto-starts on Windows
  - Daemon process now completely transparent to user
- Updated `src/daemon/daemon-server.ts` — Added session lifecycle callbacks with 5-second grace timer
  - `onSessionCreated()` callback: cancels pending idle shutdown when agent reconnects
  - `onAllSessionsClosed()` callback: triggers idle shutdown timer
  - 5-second idle grace period (configurable via `IDLE_GRACE_PERIOD`)
  - If no new session connects during grace period, daemon exits gracefully
  - Cleans up mpv, web dashboard, PID file on idle shutdown
- Updated `src/mcp/mcp-server.ts` — `createHttpMcpHandler()` now accepts callbacks
  - Constructor signature: `createHttpMcpHandler({ onSessionCreated?, onAllSessionsClosed? })`
  - Enables daemon to react to session lifecycle events
  - Tracks active sessions via `hadSession` flag for onAllSessionsClosed precision

### Benefits
- Windows users no longer see console window when daemon auto-starts
- Daemon no longer persists indefinitely after final agent session closes
- Resource cleanup happens automatically (mpv, web server, temp files)
- Seamless experience: agent closes → 5s grace period → daemon exits if idle

### Docs Updated
- Updated `docs/system-architecture.md` — Daemon Architecture section: idle timeout, auto-shutdown behavior, callback mechanism

## 2026-03-17 (Singleton Daemon + Stdio Proxy)

### Daemon Architecture for Stateful Session Sharing
- Added `src/daemon/pid-manager.ts` — Manage PID file at `~/.agentune/daemon.pid` for inter-process discovery
- Added `src/daemon/health-endpoint.ts` — `/health` HTTP endpoint for daemon readiness polling
- Added `src/daemon/daemon-server.ts` — HTTP server on port 3747 with `/health`, `/mcp`, `/shutdown` routes
  - Mounts `StreamableHTTPServerTransport` from MCP SDK for stateful session management
  - Each proxy client gets unique `Mcp-Session-Id` header
  - Shares tool handlers with stdio transport (same singleton accessors)
- Added `src/proxy/daemon-launcher.ts` — Auto-spawn detached daemon if not running; poll health endpoint for readiness
- Added `src/proxy/stdio-proxy.ts` — Default proxy mode: stdio↔HTTP relay using MCP SDK client/server transports
- Added `src/cli/status-command.ts` — `agentune status` subcommand to print daemon info
- Added `src/cli/stop-command.ts` — `agentune stop` subcommand to POST `/shutdown` to daemon
- Updated `src/index.ts` — CLI routing: `--daemon` mode, `status` subcommand, `stop` subcommand, default proxy mode
- Updated `src/mcp/mcp-server.ts` — Extracted `registerMcpTools()` to share tool definitions between stdio and HTTP transports
- Updated `docs/system-architecture.md` — New "Daemon Architecture" section with proxy pattern diagram and mode documentation
- Updated `docs/codebase-summary.md` — New daemon/, proxy/, cli/ module documentation; updated src/ directory structure

### Architecture Benefits
- Single daemon per device (stateful: 1 mpv, 1 queue, 1 taste engine, 1 web server)
- Multiple agents can connect via proxy; all share playback state
- Daemon auto-starts on first proxy invocation (seamless experience)
- PID file enables proxy port discovery without hardcoding
- `/health` endpoint + polling ensures daemon readiness before relaying requests
- Graceful shutdown via `/shutdown` endpoint

### Test Results
- All 107 unit tests passing
- Code review score: 7.5/10 (all high-priority issues fixed)
- Build clean: `npm run build` produces dist/ with no errors

### Known Considerations
- PID file at `~/.agentune/daemon.pid` is single source of truth for proxy discovery
- Daemon port (3747) separate from web dashboard (3737) to avoid conflicts
- Proxy is completely stateless; all logic in daemon singleton
- Multiple proxies can connect to same daemon; state is shared (not isolated per-session)

## 2026-03-16 (Apple-First MCP Flow)

### Discovery-First Public Tool Surface
- Removed public MCP tools that let agents bypass the intended flow: `search`, `play`, `queue_add`
- Restored public MCP tool `play_song(title, artist?)`
  - resolves canonical metadata via Apple Search API
  - replaces the current song immediately
- Added public MCP tool `add_song(title, artist?)`
  - Apple Search API canonicalizes track identity first
  - Queue-only behavior: always adds to queue
  - If queue is idle, starts playback by draining the queue instead of bypassing queue semantics
  - Returns canonical metadata, match score, queue position, and alternatives
- Updated `discover()` MCP responses to point agents to `add_song(...)` while also exposing `play_song(...)` as the replace-current action
- Updated `queue_list()` docs/wording to emphasize read-only queue inspection

### Apple-First Resolution + Queue Preservation
- Added `src/mcp/song-resolver.ts` to centralize song resolution
  - Apple Search API is primary source for canonical title/artist cleanup
  - YouTube search is now an internal playback fallback only
  - Resolver tries multiple YouTube queries sequentially, so one failed query no longer aborts the whole add flow
- Updated `src/queue/queue-playback-controller.ts`
  - Added `addById()` for queue-only add with auto-start when idle
  - Added `replaceCurrentTrack()` for `play_song` immediate replacement behavior
  - Preserves canonical artist/title when queued tracks later become now-playing
- Updated `src/taste/candidate-generator.ts`
  - Apple artist/genre catalog is now primary for continuation + context-fit lanes
  - Smart Search is demoted to expansion/fallback behavior instead of acting like the main recommendation graph

### Validation
- `npm run build`
- `npm test`
- 104/104 tests passing
- Docs impact: minor

## 2026-03-16 (Provider Replacement: Last.fm → Apple + Smart Search)

### Replaced Last.fm Provider with Apple iTunes Search + Smart Search Discovery
- Removed `src/providers/lastfm-provider.ts` — eliminates `LASTFM_API_KEY` dependency
- Added `src/providers/apple-search-provider.ts` — zero-key Apple iTunes Search API integration
  - `searchTracks(query, limit)` for catalog search
  - `getArtistTracks(artist, limit)` for artist discography
  - `getTrackGenre(artist, title)` for metadata enrichment
  - `searchByGenre(genre, limit)` for genre-based discovery
  - 7-day TTL cache to respect 20 calls/min rate limit
- Added `src/providers/smart-search-provider.ts` — intelligent ytsr-based query discovery
  - `getRelatedTracks(artist, title)` replaces Last.fm getSimilarTracks()
  - `searchByMood(mood, limit)` replaces Last.fm getTopTracksByTag()
  - `getArtistSuggestions(artist)` replaces Last.fm getSimilarArtists()
  - 3-day TTL cache for query freshness
  - Uses existing @distube/ytsr; zero new dependencies
- Added `src/providers/metadata-normalizer.ts` — shared YouTube metadata cleanup utility
- Updated `src/taste/candidate-generator.ts` — new provider integration
  - Lane A (continuation): `smartSearch.getRelatedTracks()` replaces `lastfm.getSimilarTracks()`
  - Lane C (context-fit): `smartSearch.searchByMood()` with Apple fallback
  - Lane D (wildcard): `smartSearch.getArtistSuggestions()` replaces artist exploration
- Updated `src/queue/queue-playback-controller.ts` — tag enrichment via Apple genre
  - Async `enrichTrackTags()` now uses `apple.getTrackGenre()` instead of `lastfm.getTopTags()`
  - Synthetic tag enrichment: appends discovery query keywords to genre tags
- Updated `src/index.ts` — removed Last.fm bootstrap, added dual provider init (zero config)
  - Both providers initialize without environment variables
  - Graceful: both providers are optional; app runs without them
- Updated `src/history/history-schema.ts` — renamed cache table `lastfm_cache` → `provider_cache`
- Updated docs to reflect architecture changes (zero API keys required for discovery)
- Build: Clean compile, 100/100 tests pass
- Docs impact: minor

## 2026-03-16 (Runtime Compatibility)

### Node 25 Compatibility Fix
- Updated `src/providers/youtube-provider.ts` to lazy-load `@distube/ytsr` instead of importing it at module load time
- Added a small Node 25 compatibility shim before loading `@distube/ytsr`
  - Maps legacy `fs.rmdirSync(..., { recursive: true })` behavior to `fs.rmSync(..., { recursive: true })`
  - Avoids startup crash on Node.js v25 while leaving `node_modules/` untouched
- Verified build + test still pass after the runtime fix
- Startup path can now reach MCP bootstrap on local Node 25 installs
- Docs impact: minor
- Unresolved questions:
  - None
## 2026-03-16 (Phase 5.5: Discovery Pipeline)

### Phase 5.5: Discovery Pipeline — 4-Lane Generation + 8-Term Scoring
- Added `src/taste/candidate-generator.ts` — CandidateGenerator class with 4 independent lanes
  - Continuation lane: Similar tracks from Last.fm (current track context)
  - Comfort lane: Most-played tracks from history (familiar favorites)
  - Context-fit lane: Tracks matching music intent tags or session lane tags
  - Wildcard lane: Exploration via similar artists (novelty discovery)
  - Lane ratios configurable by discover mode (focus/balanced/explore)
  - Automatic deduplication + tag filtering
- Added `src/taste/candidate-scorer.ts` — CandidateScorer class with 8-term scoring formula
  - Context match (0.32): Fits intent/session lane
  - Taste match (0.24): Aligned with artist obsessions
  - Transition quality (0.18): Smooth from current track
  - Familiarity fit (0.10): Repeat tolerance + callback love
  - Exploration bonus (0.08): Novelty appetite + persona curiosity
  - Freshness bonus (0.08): Never-played tracks
  - Repetition penalty (-0.22): antiMonotony scaling
  - Boredom penalty (-0.18): Artist boredom scores
  - Softmax sampling with mode-based temperature (focus: 0.3, balanced: 0.7, explore: 1.2)
- Added `src/taste/candidate-scorer.test.ts` with unit tests for scoring algorithm
- Added new MCP tool `discover(mode?, intent?)` to `src/mcp/mcp-server.ts`
  - Mode: "focus" (deterministic), "balanced" (default), "explore" (high entropy)
  - Intent: optional {energy?, valence?, novelty?, allowed_tags?, avoid_tags?}
  - Returns: array of ScoredCandidate with score + reasons
- Added new MCP tool `get_session_state()` to `src/mcp/mcp-server.ts`
  - Returns: full taste profile + agent persona + current session lane + recent 5 plays
  - Enables agent to understand taste context before calling discover()
- Updated `src/mcp/tool-handlers.ts` with handleDiscover + handleGetSessionState
  - handleDiscover instantiates CandidateGenerator + CandidateScorer
  - handleGetSessionState returns taste summary for agent context
- Updated `src/queue/queue-manager.ts` — QueueItem.context field (replaces deprecated mood field)
- Updated `src/web/state-broadcaster.ts` — Dashboard broadcasts context instead of mood
- Deprecated `play_mood` tool; agents should use discover() + play() instead
- Updated `README.md` — Features section now references discovery pipeline, removed mood references
- Updated `docs/codebase-summary.md` — Removed mood section, added candidate-generator + candidate-scorer
- Updated `docs/system-architecture.md` — New Discovery Pipeline component section with full data flow
- All 90+ unit tests passing; build clean; zero new external dependencies

## 2026-03-16 (Continued)

### Phase 4: Taste Intelligence + Session Lanes
- Added `src/taste/taste-engine.ts` — TasteEngine class with taste state, agent persona, and session lanes
  - Taste state: obsessions (artist/tag affinity 0-1), boredom (fatigue 0-1), cravings (active tag interests), noveltyAppetite, repeatTolerance
  - Agent persona: curiosity, dramaticTransition, callbackLove, antiMonotony (evolved separately from user prefs)
  - Session lanes: groups 2-5 songs by tag overlap (30% threshold); pivots on mood shift
  - Time-based decay: `value * 0.95^hours` for natural preference evolution
  - Implicit feedback processing: skip ratio + completion rate → obsession/boredom adjustments
- Added new MCP tool `get_session_state` to `src/mcp/mcp-server.ts` — returns taste profile + persona + current lane + recent plays
- Integrated feedback wiring into `src/queue/queue-playback-controller.ts` — calls `taste.processFeedback()` on skip and natural finish events
- Extended `src/history/history-store.ts` with `getTrackTags()` method to support tag-level feedback from Last.fm cache
- All state persisted to `session_state` table in SQLite (non-blocking)
- Added `src/taste/taste-engine.test.ts` with unit tests for taste state transitions
- All 60+ unit tests passing; build clean; zero new external dependencies

### Phase 3: Last.fm Provider + Cache
- Added `src/providers/lastfm-provider.ts` — Last.fm API client with 7-day SQLite cache
  - 4 endpoints: `getSimilarArtists(artist, limit?)`, `getSimilarTracks(artist, track, limit?)`, `getTopTags(artist, track?)`, `getTopTracksByTag(tag, limit?)`
  - Cache eviction on startup: deletes expired rows with 7-day TTL
  - YouTube metadata normalization: `normalizeForQuery()` strips official/lyric/live/ft. suffixes before querying Last.fm
  - Graceful degradation: returns empty arrays if API call fails or times out (5s timeout)
  - Singleton pattern: `createLastFmProvider(apiKey, db)` + `getLastFmProvider()`
- Extended `src/history/history-store.ts` with two new methods:
  - `getDatabase(): Database.Database` — Direct DB access for external providers (e.g., Last.fm)
  - `updateTrackTags(trackId: string, tags: string[]): void` — Store Last.fm tags in track record
- Updated `src/queue/queue-playback-controller.ts` — Async tag enrichment on every play (fire-and-forget)
  - After playback starts, fetches `getTopTags()` from Last.fm provider and stores in history DB
  - Does not block audio playback; runs in background
- Updated `src/index.ts` — Optional Last.fm provider init gated by `LASTFM_API_KEY` env var
  - Non-fatal: provider gracefully disabled if env var missing or API key invalid
- All 60+ unit tests passing; build clean; no new external dependencies (Last.fm API is free, no auth)

## 2026-03-16

### Phase 2: Smart Play (play_song + Search Result Scorer)
- Added `src/providers/search-result-scorer.ts` — fuzzy-match scoring module for YouTube search results
  - Scores titles, artists, duration, and applies quality penalties (live, remix, slowed, 8d) and bonuses (official audio, topic/auto-generated)
  - Returns scored results sorted by confidence (0–2 scale)
  - Strips quality suffixes and normalizes for robust comparison
- Added new MCP tool `play_song(title, artist?)` to `src/mcp/mcp-server.ts` and `handlePlaySong` to `src/mcp/tool-handlers.ts`
  - Primary query: `"{artist} - {title} official audio"` (searches 10 results)
  - Fallback query: `"{artist} {title}"` if top score below 0.2 minimum
  - Returns `{matched, nowPlaying, matchScore, matchReasons, alternatives}` for transparency
  - Uses canonical artist/title overrides to ensure accurate history recording
- Updated `queue_add` tool to accept optional `id` parameter for direct video ID queuing (alongside existing `query` parameter)
- Updated `YouTube` search default limit from 5 to 10 when used in play_song flow for better match options
- Extended `playById` in queue-playback-controller to accept optional `canonicalArtist` and `canonicalTitle` for override history recording
- All 60 unit tests passing; build clean; no new dependencies added

## 2026-03-15

### Phase 1+: SQLite History Foundation
- Added `src/history/history-store.ts` with `HistoryStore` class backed by better-sqlite3; singleton pattern via `createHistoryStore()` and `getHistoryStore()`
- Added `src/history/history-schema.ts` with SQLite table definitions (tracks, plays, preferences, session_state, lastfm_cache) and `normalizeTrackId()` for consistent track dedup
- Database location: `~/.agentune/history.db` (configurable via `AGENTUNE_DATA_DIR` env var); auto-created on first run with WAL mode for concurrent safety
- Added MCP tool `history` to `src/mcp/mcp-server.ts` — enables agent to query recent plays with play counts and skip rates
- Integrated history recording into `src/queue/queue-playback-controller.ts` — `recordPlay()` called when track starts, `updatePlay()` called on finish/skip
- Updated `src/index.ts` to initialize history store on startup (non-fatal) and close DB gracefully on shutdown
- Added `src/history/history-store.test.ts` with unit tests for recordPlay, updatePlay, getRecent, getTrackStats
- New dependency: better-sqlite3 v12.8.0 (+ @types/better-sqlite3 dev dependency)
- Backward compatible with existing queue/MCP workflow; history persistence is a new feature layer

## Earlier Updates (Phase 7 and prior)

### Phase 7: Queue + Polish
- Replaced the queue placeholder with a real `QueueManager` in `src/queue/queue-manager.ts` that tracks now playing, upcoming queue, and playback history.
- Added `src/queue/queue-playback-controller.ts` to coordinate queue advancement, manual skip, YouTube stream resolution, and mpv playback without duplicating tool logic.
- Updated `src/mcp/tool-handlers.ts`, `src/index.ts`, and `src/audio/mpv-controller.ts` so `queue_add`, `queue_list`, `skip`, graceful shutdown, and natural track-end auto-advance all run through the same playback path.
- Updated `src/web/state-broadcaster.ts` and `src/web/web-server.ts` so the browser dashboard receives live queue state instead of placeholder data.
- Hardened `src/providers/youtube-provider.ts` with a retry path for transient `yt-dlp` extraction failures.
- Added `src/queue/queue-manager.test.ts`, `src/queue/queue-playback-controller.test.ts`, `.npmignore`, and the `npm test` script for Phase 7 verification and release prep.
- Updated README, roadmap, architecture docs, and plan files to mark MVP feature work complete while explicitly deferring the actual npm publish step.

### Phase 6: Mood Mode
- Replaced the mood stub in `src/mood/mood-presets.ts` with 5 curated mood pools and random query selection helpers.
- Wired `play_mood` in `src/mcp/tool-handlers.ts` to normalize user mood input, select a curated search query, search YouTube, and reuse the existing playback flow.
- Updated `src/mcp/mcp-server.ts` to accept case-insensitive mood input at the tool boundary instead of rejecting non-lowercase variants.
- Extended `src/audio/mpv-controller.ts` and `src/web/state-broadcaster.ts` so active mood metadata flows into dashboard state.

### Phase 5: Browser Dashboard
- Added `src/web/web-server.ts` with static file serving, `/api/status`, `/api/volume`, WebSocket upgrade handling, and one-time browser auto-open on first successful play.
- Added `src/web/state-broadcaster.ts` and `src/web/web-server-helpers.ts` to push 1-second playback snapshots and keep the HTTP/WebSocket layer modular.
- Extended `src/audio/mpv-controller.ts` with state-change events, mute tracking, and a readable state snapshot for the dashboard.
- Updated `src/index.ts` and `src/mcp/tool-handlers.ts` to initialize the dashboard with the mpv controller and open the browser on first play.
- Replaced placeholder dashboard assets in `public/index.html`, `public/style.css`, and `public/app.js` with a responsive dark UI, reconnecting WebSocket client, progress bar, volume slider, and mute toggle.
- Hardened degraded-mode behavior so `/api/volume` returns `503` instead of crashing when mpv is unavailable, while `/api/status` and WebSocket state remain available.
- Added a Phase 5 journal entry in `docs/journals/2026-03-15-phase-05-browser-dashboard.md`.

### Validation
- `npm test`
- `npm run build`
- Queue manager unit tests
- Queue playback controller unit tests
- Local queue broadcaster smoke: queue + mood appear in dashboard state snapshot
- Local mood helper smoke: normalization, query pool size, random query selection
- Local handler smoke: invalid mood returns MCP error result
- Local broadcaster smoke: mood metadata appears in dashboard state
- Smoke test: `GET /`
- Smoke test: `GET /api/status`
- Smoke test: `WS /ws` initial state message
- Smoke test: `POST /api/volume` returns safe `503` when mpv is unavailable
```

## File: `docs/project-overview-pdr.md`
```markdown
# Project Overview & PDR (Product Development Requirements)

## Executive Summary

**agentune** is an MCP (Model Context Protocol) server enabling coding agents to control music playback like a DJ while writing code. It bridges the gap between AI agents and music streaming by providing a lightweight, headless audio engine with agent-driven search, playback control, and browser-based visualization.

## Product Vision

Empower developers using AI coding assistants (Claude Code, Cursor, Codex) to enhance focus, creativity, and productivity through agent-controlled music. Music selection and playback should require zero human interaction — the agent decides what to play based on context ("focus mode", "hype mode", "relaxing beats").

## Target Users

1. **Primary**: Developers using Claude Code or Cursor for pair programming
2. **Secondary**: Open-source developers needing ambient music during long coding sessions
3. **Tertiary**: Streaming researchers studying agent-based media control

## MVP Scope (Phases 1–7)

### In Scope
- Agent-driven search on YouTube (no API key required)
- Playback control (play, pause, skip, queue)
- Browser dashboard showing now-playing + volume
- Headless audio via mpv (independent of browser)
- Local CLI diagnostics for required dependencies and daemon health
- Curated mood keywords (`focus`, `energetic`, `chill`, `debug`, `ship`)
- Cross-platform (Windows, macOS, Linux)

### Out of Scope (Post-MVP)
- Spotify/Apple Music/Amazon Music integration
- Persistent queue storage
- User accounts or playlists
- Lyrics display
- Recommendations
- Audio equalizer or effects

## Functional Requirements

| ID | Requirement | Phase | Priority |
|----|-------------|-------|----------|
| F1 | Agent searches YouTube without API key | 4 | P0 |
| F2 | Agent plays first result from search | 2, 3, 4 | P0 |
| F3 | Agent skips to next track | 2, 3, 7 | P0 |
| F4 | Agent queues multiple tracks | 2, 7 | P0 |
| F5 | Agent reads now-playing info | 2, 3 | P0 |
| F6 | Browser shows now-playing title/progress | 5 | P1 |
| F7 | Browser controls volume | 5 | P1 |
| F8 | Mood keywords auto-generate search queries | 2, 6 | P1 |
| F9 | Queue persists during session | 7 | P1 |
| F10 | Works on Windows, macOS, Linux | 3 | P0 |
| F11 | CLI checks required runtime dependencies and daemon status | post-MVP hardening | P1 |

## Non-Functional Requirements

| ID | Requirement | Metric | Priority |
|----|-------------|--------|----------|
| NF1 | Search-to-play latency | < 3 seconds | P0 |
| NF2 | Audio reliability | 0 interruptions in 8hr session | P0 |
| NF3 | Memory footprint | < 100 MB | P1 |
| NF4 | TypeScript strict mode | 100% passing | P0 |
| NF5 | Error recovery | Auto-reconnect on mpv crash | P1 |

## Success Metrics

1. **Agent Autonomy**: Agent initiates music without human intervention (F1–F5)
2. **Dashboard UX**: Real-time updates on browser with < 100ms latency
3. **Reliability**: No crashes or playback interruptions during 8-hour session
4. **Installation**: package ships through a gated CLI-only npm release workflow and stays locally installable from its tarball
5. **Cross-platform**: Same code/behavior on Windows, macOS, Linux

## Constraints & Dependencies

### Technical Constraints
- **No Spotify/YouTube Music API**: Use @distube/ytsr (scraping-free) + yt-dlp
- **Node.js ESM only**: TypeScript strict mode, async/await throughout
- **MCP Protocol**: Compliance with @modelcontextprotocol/sdk v1.x
- **stdio safety**: No console.log() — use console.error() only
- **URL expiry**: YouTube streams expire after ~6 hours (force refresh on play)

### System Dependencies
- Node.js 20+ (LTS)
- mpv (audio engine)
- yt-dlp (Python-based audio extraction)
- npm account authentication for alpha/stable publish steps
- A local diagnostics path (`agentune doctor`) to verify the above dependencies before runtime use

### Architecture Dependencies
1. Phase 1 (Setup) → Phase 2 (MCP) → Phase 3 (mpv) → Phase 4 (YouTube)
2. Phase 4 is also prerequisite for Phase 5, 6, 7

## Acceptance Criteria

### Phase 2: MCP Server
- [ ] McpServer initializes with stdio transport
- [ ] All tool definitions registered (search, play, skip, queue, status)
- [ ] Tool results use `{isError: true/false}` structure
- [ ] Zero console.log() calls

### Phase 3: Audio Engine
- [ ] mpv spawns with JSON IPC socket
- [ ] Play, pause, stop commands work
- [ ] Progress/duration reporting works
- [ ] Graceful shutdown without hanging

### Phase 4: YouTube Provider
- [ ] Search returns video metadata (title, duration, URL)
- [ ] Stream URLs valid for 6+ hours
- [ ] Handles no results gracefully
- [ ] < 1 second search latency

### Phase 5: Dashboard
- [x] Now-playing title updates in real-time
- [x] Progress bar syncs with playback
- [x] Volume slider sends commands to mpv when audio is available
- [x] Responsive on mobile browsers

### Phase 6: Mood Mode
- [x] `play_mood` resolves curated queries for the 5 supported moods
- [x] Mood input is normalized case-insensitively
- [x] Active mood appears in dashboard state

### Phase 7: Queue + Polish
- [x] `queue_add` resolves search results into real queued items
- [x] `queue_list` returns now-playing, upcoming queue, and history
- [x] `skip` advances to the next queued track when available
- [x] Natural track end auto-advances through the queue
- [x] Dashboard shows live queue updates
- [x] Local TypeScript build + Node test suite pass

## Out-of-Scope Justification

- **Spotify Integration**: Requires OAuth + paid API; YouTube is free + no keys
- **Persistent Storage**: MVP focuses on single-session behavior
- **Recommendations**: Too complex for MVP; mood keywords sufficient
- **Advanced UI**: Focus on minimal, functional dashboard first

## Success Criteria (Final)

Agent can execute this conversation **without human intervention**:

```
Agent: "Play lo-fi beats for focus"
[agentune searches YouTube, plays first result]
[Browser shows now-playing: "lo-fi beats 🎧"]

Agent: "This is too upbeat. Try something more chill."
[Agent searches for "chill jazz", plays result]
[Progress updates on browser]

Agent: "Skip this one"
[Next track plays immediately]

Agent: "What's playing now?"
[Agent reads metadata from agentune]
```

All without human clicking, confirmation, or intervention.

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| YouTube scraping blocked | F1 broken | Monitor @distube/ytsr; fallback to direct yt-dlp query |
| mpv crashes | All playback halted | Auto-restart with backoff; notify agent |
| Stream URLs expire | Playback stalls | Refresh URL cache every 5 hours; re-fetch on 404 |
| Windows IPC hangs | Agent blocked | Named pipe timeout + graceful degradation |
| Agent misconceptions | Misuse | Clear MCP tool descriptions |

## Timeline

- **Week 1 (P0 phases 1–4)**: Bootstrap, MCP server, mpv, YouTube (dependencies resolved)
- **Week 2 (P1 phases 5–7)**: Dashboard, mood mode, and queue/polish complete; public npm publish intentionally deferred

## Review & Iteration

- Weekly sync with agent developers (if available)
- Post-MVP: Gather usage metrics and tune curated mood query pools
- Plan Spotify integration for v0.2 if demand warrants
```

## File: `docs/project-roadmap.md`
```markdown
# Project Roadmap

## Current State

`agentune` is functionally in MVP-complete territory for local agent-controlled playback:

- daemon + proxy architecture: complete
- queue-based playback: complete
- browser dashboard redesign: complete
- Apple-first resolution flow: complete
- flat Apple-only discover rewrite: implemented
- agent-first state redesign: complete
- config-driven discover ranking: complete
- agent-facing discover guidance cleanup: complete
- explicit daemon lifecycle + dashboard stop: complete
- optional daemon auto-start + manual `agentune start`: complete
- local dependency + daemon diagnostics via `agentune doctor`: complete
- web/dashboard hardening + safer daemon stop: complete
- discover rewrite automated validation: complete
- local-gated npm release workflow: complete
- GitHub Actions CI matrix for Ubuntu, Windows, and macOS: complete
- daemon/MCP end-to-end smoke record: pending

Last validated:

- `2026-03-22`
- `npm run build`: passed
- `npm test`: 126 passed, 0 failed
- `npm run verify:publish`: passed
- `node dist/index.js doctor`: passed
- built-handler smoke: `discover({ artist: "Nils Frahm", limit: 1 })` returned a paginated Apple candidate

## Completed Milestones

### Foundation

- TypeScript/Node runtime and CLI packaging
- `mpv` playback integration
- YouTube search and stream resolution
- SQLite history store

### Agent Control Surface

- MCP tools for playback, queue inspection, volume, and history
- Apple-first `play_song` / `add_song` resolution flow
- shared daemon so multiple agent sessions see the same queue and history
- CLI diagnostics for required runtime dependencies and daemon health

### Dashboard

- live playback state
- artwork-first player shell with full-screen `Queue / Now Playing / Settings` tabs
- read-only queue view
- pause, next, and volume controls
- minimal dashboard insights in `Settings`
- persona taste editor
- `/api/persona`, `/api/artwork`, and WebSocket sync

### State Redesign

- removed scorer-driven taste loop from active runtime
- replaced old taste state with:
  - `context`
  - `persona` (`Preferences`)
  - `history`
- moved discover reranking weights into runtime config
- replaced grouped discover lanes with flat paginated Apple-only discover output
- added soft ranking from fixed config weights + history plus snapshot pagination cache
- renamed agent-facing discover seeds/results from `genres`/`tags` to `keywords`
- added `nextGuide` so the agent knows whether to paginate or improve input
- kept `mode` / `intent` accepted but ignored for one compatibility cycle
- added `update_persona`

## Active Focus

### 1. End-to-End Smoke Coverage

Status: in progress

Next work:

- run and record a full daemon/MCP smoke test for paginated `discover()`
- add direct daemon/proxy coverage where practical

### 2. Documentation Maintenance

Status: in progress

Next work:

- keep `README.md`, `docs/system-architecture.md`, `docs/codebase-summary.md`, this roadmap, and the changelog aligned with the shipped discover contract
- trim stale historical detail when it starts competing with current-state docs

### 3. Release Readiness

Status: in progress

Next work:

- publish and validate an `alpha` prerelease from the new gated flow
- validate Windows/macOS/Linux prerequisites end-to-end, including `agentune doctor`
- decide when to promote the first stable `latest` release

## Near-Term Backlog

- more direct MCP coverage around discover pagination and cache invalidation
- more daemon/proxy end-to-end coverage for taste updates
- optional richer dashboard controls
- cross-platform release rehearsal notes for npm publish

## Explicitly Removed from the Current Direction

These are not current roadmap targets anymore:

- restoring grouped-lane discover output
- reintroducing Smart Search into the discover pipeline
- reintroducing obsession/boredom/craving state as the primary taste model

## Success Criteria

The roadmap should stay true when these statements remain accurate:

- an agent can understand taste from raw state instead of opaque server scores
- `discover()` returns flat paginated Apple candidates with cache-backed follow-up pages
- the queue, dashboard, and MCP tools stay in sync
- the codebase can be validated with a clean `npm run build` and `npm test`
- docs describe the current runtime, not superseded experiments
```

## File: `docs/system-architecture.md`
```markdown
# System Architecture

## Overview

`agentune` is a single-user music control system built around one shared daemon per device.

1. Coding agents connect through MCP.
2. The daemon owns playback, queue state, listening history, and the browser dashboard.
3. `mpv` handles audio playback; SQLite stores durable history and persona taste text.

```
Agent / MCP Client
  -> stdio proxy or HTTP MCP client
  -> agentune daemon
     -> MCP tools
     -> queue + playback controller
     -> taste engine
     -> history store (SQLite)
     -> web dashboard (:dashboardPort from config)
     -> mpv
```

## Runtime Topology

### Proxy Mode

- `agentune` without args starts the lightweight stdio proxy.
- The proxy reads `autoStartDaemon` from `${AGENTUNE_DATA_DIR || ~/.agentune}/config.json`.
- If `autoStartDaemon` is `true`, the proxy auto-starts the daemon when needed.
- If `autoStartDaemon` is `false`, the proxy only connects to an already-running daemon and fails fast with a manual-start hint if none exists.
- The proxy does not own queue, mpv, or database state.
- Closing the proxy session does not stop the daemon.

### Daemon Mode

- `agentune --daemon` starts the long-lived process.
- `agentune start` starts the same daemon in the background and exits after readiness succeeds.
- `agentune doctor` performs local diagnostics without starting playback.
- Runtime config lives at `${AGENTUNE_DATA_DIR || ~/.agentune}/config.json`.
- The daemon exposes:
  - `/mcp` on the configured daemon port for MCP traffic
  - `/health` for readiness checks
  - `/shutdown` for graceful stop
  - the dashboard on `http://127.0.0.1:{dashboardPort}` from config
- The daemon PID file now stores `pid`, `port`, `started`, and a per-process control token.
- `/mcp` and `/shutdown` require `X-Agentune-Daemon-Token`; `/health` stays unauthenticated so proxy discovery and `agentune status` can probe readiness without extra bootstrap.
- Both ports are exact; no automatic fallback is used anymore.
- One daemon means one shared queue, one shared history DB, and one shared `mpv` process.
- The daemon stays alive until an explicit stop request arrives from `agentune stop` or the dashboard stop button.
- `agentune stop` waits for graceful shutdown first and only falls back to a verified process kill.

### Operational Diagnostics

- `agentune doctor` is a local CLI health check for installation and runtime support.
- Required checks:
  - Node.js satisfies `package.json.engines.node`
  - runtime config loads successfully
  - `mpv` resolves from PATH
  - the bundled `youtube-dl-exec` `yt-dlp` binary exists and is executable
- Advisory checks:
  - system `yt-dlp` on PATH
  - daemon health / stopped state
- The command also reports resolved runtime paths:
  - data dir
  - config path
  - history DB path
  - PID file path
  - daemon log path

## Core Components

### History Store

File: `src/history/history-store.ts`

Responsibilities:

- Persist tracks and play events in SQLite
- Persist free-text persona taste in `session_state.persona_taste_text`
- Expose manual cleanup operations for history and provider cache
- Expose aggregate history queries for the taste engine and MCP tools

Tables:

- `tracks`
- `plays`
- `session_state`
- `provider_cache`

Important notes:

- `normalizeTrackId(artist, title)` is the canonical identity key.
- The constructor now migrates older databases to schema version 3, dropping unused legacy columns/tables including `persona_traits_json`.
- Cleanup actions run `wal_checkpoint(TRUNCATE)`, `VACUUM`, and `PRAGMA optimize`.

### Taste Engine

File: `src/taste/taste-engine.ts`

The redesign replaced the older weighted taste model with a smaller agent-first contract:

```ts
{
  context: { hour, period, dayOfWeek },
  persona: { Preferences: string },
  history: {
    recent: [...],
    stats: { topArtists, topKeywords }
  }
}
```

Behavior:

- `Preferences`: editable free-text description stored in SQLite
- `history`: still returned as context for the agent
- discover ranking weights now come from runtime config, not persona state

Important constraints:

- Older structured persona/session objects are no longer part of the active runtime contract.

### Discovery Pipeline

Files:

- `src/taste/discover-batch-builder.ts`
- `src/taste/discover-merge-and-dedup.ts`
- `src/taste/discover-soft-ranker.ts`
- `src/taste/discover-pagination-cache.ts`
- `src/taste/discover-pipeline.ts`

Behavior:

- `discover()` is a flat paginated API: `{ page, limit, hasMore, candidates[] }`.
- `discover()` also returns `nextGuide` so the agent knows whether to change page or improve the search input.
- `DiscoverBatchBuilder` pulls Apple artist tracks and Apple genre search results only.
- When `artist` and `keywords` are both omitted, the builder seeds from the top 3 history artists and top 3 history keywords.
- `mergeAndDedup()` removes duplicate `artist + title` pairs and interleaves artists before ranking.
- `rankCandidates()` soft-ranks by tag affinity, artist familiarity, average completion, novelty, recent-repeat penalty, and skip rate.
- `toPublicCandidate()` strips internal Apple IDs before returning results.
- Pagination snapshots are cached in memory per normalized `{ artist, keywords }` key, with a 5 minute TTL, 10-entry cap, and no empty-result caching.
- Successful `play_song()` and `add_song()` invalidate the discover cache.
- `update_persona()` does not invalidate the discover cache.
- The reranker uses fixed `discoverRanking` values from runtime config.

### MCP Surface

Files:

- `src/mcp/mcp-server.ts`
- `src/mcp/tool-handlers.ts`

State-related tools:

- `get_session_state()`
  - returns `context`, `persona`, and `history`
- `discover(page?, limit?, artist?, keywords?, mode?, intent?)`
  - returns `{ page, limit, hasMore, candidates, nextGuide }`
- `update_persona({ taste })`
  - persists free-text taste text
  - empty string is allowed to clear the value

Playback tools remain queue-first:

- `play_song`
- `add_song`
- `skip`
- `queue_list`
- `now_playing`
- `volume`
- `history`

Important notes:

- `mode` and `intent` are accepted by the tool schema for compatibility, but ignored by the current discover pipeline.
- Discover ordering is server-side, but the response surface does not expose raw scores.

### Queue and Playback

Files:

- `src/queue/queue-manager.ts`
- `src/queue/queue-playback-controller.ts`
- `src/audio/mpv-controller.ts`
- `src/audio/mpv-process-session.ts`
- `src/audio/mpv-ipc-client.ts`
- `src/audio/mpv-launch-helpers.ts`

Behavior:

- `QueueManager` owns now playing, queued items, and playback history.
- `QueuePlaybackController` resolves audio, records plays, updates completion/skip status, and advances the queue.
- `MpvController` keeps the public playback contract stable for queue, MCP, and dashboard code.
- `MpvProcessSession` launches `mpv` directly and binds the JSON IPC socket/pipe.
- `MpvIpcClient` sends newline-delimited JSON commands and matches replies by `request_id`.
- Track feedback is stored as raw history updates only.
- Playback feedback now stays in raw history rows; there is no secondary taste update loop.
- Apple genre enrichment still runs after playback starts and updates track tags asynchronously.

Important notes:

- The old `node-mpv` wrapper is gone.
- The controller observes `pause` and `idle-active` through JSON IPC so pause/resume state and natural track-end queue advancement stay deterministic.
- Windows launch behavior still hides the managed `mpv` console window and prefers `mpv.exe` when present.

### Web Dashboard

Files:

- `src/web/web-server.ts`
- `src/web/web-server-auth.ts`
- `src/web/web-server-artwork-proxy.ts`
- `src/web/web-server-static-file-path.ts`
- `src/web/state-broadcaster.ts`
- `public/index.html`
- `public/app.js`
- `public/style.css`
- `public/dashboard/*`
- `public/styles/*`

Endpoints:

- `GET /api/status`
- `GET /api/persona`
- `GET /api/artwork?src=...`
- `POST /api/persona`
- `POST /api/volume`
- `POST /api/daemon/stop`
- `GET /api/database/stats`
- `POST /api/database/clear-history`
- `POST /api/database/clear-provider-cache`
- `POST /api/database/full-reset`
- `WS /ws`

Dashboard features:

- artwork-first now-playing shell
- full-screen `Queue / Now Playing / Settings` tabs
- read-only queue preview
- pause, next, and volume controls
- minimal `Dashboard` block at the top of `Settings`
- curved 7-day line chart
- asymmetric grid with `Plays`, `Tracks`, `Most artists`, and `Most tags`
- persona textarea below the insights block
- database stats and derived SQLite insights from `GET /api/database/stats`
- manual cleanup buttons for history, provider cache, and full reset
- explicit daemon stop button
- same-origin artwork proxy for local rendering and palette extraction

Important notes:

- `GET /` serves the dashboard HTML dynamically and injects a per-process session token into a `<meta>` tag.
- `GET` / `POST` `/api/*` require `X-Agentune-Dashboard-Token`.
- `GET /api/artwork` and `WS /ws` require a `dashboardToken` query param because the browser bootstrap path cannot rely on custom headers for artwork/image requests.
- Dashboard `POST` routes and `WS /ws` also require a same-origin browser request (`Origin` must match the dashboard host).
- The dashboard no longer renders context badges.
- `POST /api/persona` accepts only `taste`.
- artwork theming reads proxied thumbnails instead of sampling remote image URLs directly.
- Dashboard JSON body reads are size-bounded.
- `POST /api/volume` rejects non-finite input and clamps accepted values into `0..100`.
- WebSocket volume updates also reject non-finite input.
- `/api/artwork` only proxies remote `http` / `https` image responses, blocks loopback/private/link-local targets, resolves hostnames before fetch, validates redirect targets, and caps proxied artwork size.
- Static assets are resolved relative to the real `public/` root instead of relying on prefix string checks.
- Persona changes are broadcast to connected clients over WebSocket.
- Dashboard taste edits can arrive through WebSocket or `POST /api/persona`.
- `GET /api/database/stats` returns both raw counts and a smaller `insights` block with `plays7d`, `tracks7d`, skip rate, 7-day activity, top artists, and top tags. The dashboard uses the 7-day insight metrics, while the lower advanced section still shows raw DB counts.
- Cleanup actions stop playback, clear runtime queue state, invalidate discover cache, then mutate SQLite.
- Cleanup actions are serialized so overlapping destructive requests cannot run concurrently.
- `POST /api/daemon/stop` returns success first, then schedules the same shutdown path used by `agentune stop`.
- After a dashboard stop, the page stops reconnecting until agentune is started again.

## Main Flows

### Read Session State

1. Agent calls `get_session_state()`.
2. The taste engine reads stored taste text plus recent history and aggregate stats from SQLite.
3. The tool returns time context, `persona.Preferences`, recent plays, top artists, and top keywords.

### Discover Music

1. Agent optionally calls `get_session_state()` first.
2. Agent calls `discover(page?, limit?, artist?, keywords?)`.
3. `DiscoverPipeline` checks the pagination cache for the normalized `{ artist, keywords }` seed set.
4. On cache miss, the pipeline builds Apple-only batches, deduplicates them, soft-ranks them from history plus fixed runtime config weights, stores the snapshot, slices the requested page, and returns `nextGuide`.
5. Agent chooses a track and calls `add_song()` or `play_song()`.

### Update Persona

1. Agent calls `update_persona({ taste })` or the dashboard posts `/api/persona`.
2. The taste engine writes taste text to `session_state.persona_taste_text`.
3. Updated persona state is broadcast to dashboard clients.
4. Taste updates do not invalidate discover snapshots.

### Playback Feedback

1. Queue playback starts and `recordPlay()` inserts a play row.
2. On skip or finish, `updatePlay()` records `played_sec` and `skipped`.
3. Future `get_session_state()` and `discover()` calls read from that raw history.

### Manual Database Cleanup

1. User opens the dashboard database section.
2. User confirms `clear-history`, `clear-provider-cache`, or `full-reset`.
3. The server stops playback and clears runtime queue state before touching SQLite.
4. The history store performs the selected cleanup, keeps persona state intact, and runs DB maintenance.
5. Updated state is pushed back to the dashboard.

## Build and Validation

- `npm run build` cleans `dist/` before compiling so deleted test files do not leak into later runs.
- `npm test` currently validates:
  - mpv IPC transport behavior
  - Windows mpv launch helpers
  - history store behavior
  - queue behavior
  - resolver/provider behavior
  - discover pipeline and soft ranking
  - taste engine redesign
- `npm run verify:publish` now also verifies tarball install output so unexpected deprecation warnings fail the release gate. The only accepted install warning is `better-sqlite3`'s transitive `prebuild-install` notice.

## Design Rules

- Never write to stdout from server internals; MCP stdio must stay clean.
- Keep queue state authoritative in one place.
- Prefer raw data plus agent reasoning over server-side taste prediction.
- Keep runtime settings in `config.json`; keep user history and persona taste text in SQLite.
```

## File: `docs/journals/2026-03-15-phase-05-browser-dashboard.md`
```markdown
# Phase 5 Dashboard Landed, But The First Smoke Test Broke It

**Date**: 2026-03-15 20:10
**Severity**: Medium
**Component**: Browser dashboard / web server
**Status**: Resolved

## What Happened

Phase 5 shipped as a real browser dashboard: HTTP server, static assets, WebSocket state sync, volume slider, mute toggle, and auto-open on first play. The build passed immediately. That was not enough. The first live smoke test against `POST /api/volume` exposed a server-side failure path when `mpv` was unavailable.

## The Brutal Truth

This was the exact kind of bug that slips through when a team congratulates itself too early because TypeScript is green. The dashboard looked done. It was not done. A simple request against a perfectly valid endpoint could still tear down the request path because the happy-path assumption was wrong. That is annoying because the whole point of this dashboard is to be useful even when audio is temporarily unavailable.

## Technical Details

`npm run build` passed, `GET /api/status` passed, and WebSocket connection to `/ws` returned the expected initial `state` payload. Then `POST /api/volume` triggered the broken path. The request should have failed gracefully, but instead the transport got severed because `MpvController.setVolume()` required a ready player and the HTTP layer did not guard that case. The fix added:

- `503` for volume updates when the audio engine is unavailable
- request-level error handling in the HTTP server
- safe ignore behavior for WebSocket volume/mute messages when `mpv` is not ready

## What We Tried

- Built first with `npm run build`
- Ran live HTTP smoke tests
- Re-ran after patching request handling
- Verified WebSocket handshake and initial state payload again

## Root Cause Analysis

The root problem was assuming dashboard controls and audio readiness are the same thing. They are not. The dashboard is display-first. Audio can be down while the dashboard stays up. The original server code treated them as one availability boundary.

## Lessons Learned

- Passing compilation means almost nothing for control-plane features
- For local dashboards, degraded mode matters as much as the happy path
- Request handlers must own their own failure boundaries, not trust downstream services

## Next Steps

- Add real automated tests for `/api/status`, `/api/volume`, and `/ws`
- Wire queue and mood data into dashboard state in Phases 6 and 7
- Keep smoke-testing endpoints before calling any phase done
```

## File: `docs/journals/2026-03-15-phase-06-mood-mode.md`
```markdown
# Phase 6 Mood Mode Was Small, But The Environment Still Limited The Real Proof

**Date**: 2026-03-15 22:05
**Severity**: Low
**Component**: Mood mode / MCP playback flow
**Status**: Resolved

## What Happened

Phase 6 replaced the `play_mood` stub with a real path: normalize the incoming mood, choose a curated query, search YouTube, reuse the existing playback flow, and surface the active mood on the dashboard. The implementation itself was straightforward. The annoying part was verification: local helper and handler checks passed immediately, but full end-to-end playback still depended on tools that were not installed in this workspace.

## The Brutal Truth

This was not a hard feature. It was a feature with fake confidence risk. It is easy to wire a pleasant abstraction around YouTube search and call it done. It is harder to admit that without `mpv` and `yt-dlp` present, the truly important path cannot be exercised end-to-end here. That is not a code failure, but pretending otherwise would be dishonest.

## Technical Details

`npm run build` passed. Local smoke checks confirmed:

- `normalizeMood('FOCUS')` returns `focus`
- each mood pool exposes 5 curated queries
- invalid mood input returns MCP `{ isError: true }`
- `StateBroadcaster` includes `mood: "focus"` when track metadata carries it

The missing pieces were environment-bound:

- `where.exe mpv` failed
- `where.exe yt-dlp` failed

So a real `play_mood` call could not be validated against actual playback.

## What We Tried

- compiled the full repo
- ran helper-level smoke checks from built output
- ran invalid-input handler checks
- simulated dashboard propagation with a fake mpv event source
- checked for `mpv` and `yt-dlp` in PATH

## Root Cause Analysis

The only verification gap was environmental, not architectural. Mood mode is coupled to the existing playback stack, and that stack requires local system binaries. Without them, only the deterministic parts of the path can be tested.

## Lessons Learned

- Small feature does not mean small verification surface
- For MCP music flows, system dependency checks matter as much as TypeScript passing
- It is worth separating deterministic local checks from environment-dependent playback proof

## Next Steps

- install `mpv` and `yt-dlp`
- run a real `play_mood("focus")` smoke test through MCP
- finish Phase 7 so mood mode and queue state can converge into a complete playback loop
```

## File: `docs/journals/2026-03-15-phase-07-queue-polish.md`
```markdown
# Phase 7 Queue Loop Closed

**Date**: 2026-03-15 13:55
**Severity**: Medium
**Component**: Queue playback / release prep
**Status**: Resolved

## What Happened

Phase 7 started with the most annoying kind of unfinished work: queue tools existed in the MCP surface, but they did not really do queue work. `queue_add`, `queue_list`, and `skip` were basically promises without a real playback loop behind them. The browser dashboard also still showed placeholder queue data, which meant the UI implied completeness that the backend had not earned.

## The Brutal Truth

This was the last fake-looking part of the MVP. Everything around it already looked real enough that the stubbed queue path was becoming a credibility problem. A music server without a working queue is half a toy. The painful part is that playback state was split across MCP handlers, mpv, and dashboard state, so a naive fix would have duplicated logic and produced racey behavior the moment manual skip and natural track end collided.

## Technical Details

- Added `src/queue/queue-manager.ts` for `nowPlaying`, `queue`, and `history`
- Added `src/queue/queue-playback-controller.ts` to centralize `playById()`, `queueByQuery()`, and `skip()`
- Hooked mpv stop lifecycle into queue auto-advance
- Updated dashboard state to use real queue snapshots
- Added Node tests:
  - `src/queue/queue-manager.test.ts`
  - `src/queue/queue-playback-controller.test.ts`
- Validation passed:
  - `npm run build`
  - `npm test`

## What We Tried

- First approach was to keep queue mutations inside MCP handlers. Rejected because it would drift from natural mpv track-end behavior.
- Then we checked `node-mpv` event behavior and used that to wire a single queue playback controller around mpv stop events.
- Added a manual-skip guard so stop events from skip would not double-advance the queue.

## Root Cause Analysis

The root problem was architectural incompleteness, not a single bug. Queue state existed conceptually, but there was no single owner for playback transitions. Without that owner, each feature path would keep reimplementing “what happens next?” slightly differently.

## Lessons Learned

- If playback can advance from more than one trigger, one module must own the transition logic.
- Dashboard placeholders become liabilities fast once surrounding features are real.
- Release prep and feature completion are not the same thing; publishing should stay a separate explicit step.

## Next Steps

- Run publish-readiness checks: `npm install -g ./` and `npm publish --dry-run`
- Verify queue behavior on macOS/Linux hosts
- Publish only after explicit release approval
```

## File: `docs/journals/2026-03-16-phase-04-taste-intelligence.md`
```markdown
# Phase 4 Taste Intelligence Shipped Clean: Four Dimensions, Time-Based Decay, Session Lanes

**Date**: 2026-03-16 10:45
**Severity**: Low
**Component**: Taste engine / preference learning
**Status**: Complete

## What Happened

Phase 4 implemented the TasteEngine class (~200 LOC in `src/taste/taste-engine.ts`) with four taste dimensions (obsessions, boredom, cravings, noveltyAppetite), implicit feedback from skip/play events, time-based decay to prevent frequency drift, and session lanes for mood continuity across 2-5 song runs. All 91 tests passed on first run. Build clean. Code review 8/10 with all high-priority issues fixed.

## The Brutal Truth

This phase went exactly as planned. No fires, no pivots, no "oh we should have designed this differently." The design choices were sound: dropping vocalTolerance and explorationBias (unreliable without metadata) kept complexity manageable. Separating agent persona from user preferences (persona for transition style, prefs for what's accepted) solved the conceptual mess from Phase 3. Time-based decay over event-based prevents the taste engine from drifting when users skip frequently in certain moods.

## Technical Details

- **Taste dimensions**: obsessions (repeats), boredom (tolerance decay), cravings (tag-based wants), noveltyAppetite (exploration vs safety)
- **Session lanes**: Pivot on low tag overlap or 5+ songs to maintain mood coherence
- **Time decay**: `value * 0.95^hours` — exponential falloff prevents frequency-driven drift
- **Implicit feedback**: Skip <30% = strong negative, play >85% = positive
- **State persistence**: SQLite `session_state` table, wired into `queue-playback-controller` via skip and finish events
- **MCP integration**: `get_session_state` tool gives agent full decision context

## What We Tried

- Implemented taste engine as single file (session lane as inner concern, ~50 LOC)
- Added type guards on implicit feedback parsing
- Wrapped JSON.parse in try/catch for safety
- Persisted state on every skip/finish event
- Tested decay math at 24-hour intervals

## Root Cause Analysis

None. The phase executed cleanly because the groundwork from Phases 1-3 was solid: SQLite schema was ready, event hooks existed, queue controller had the skip/finish paths built in. No surprises.

## Lessons Learned

- Dropping unreliable dimensions early (vocalTolerance, explorationBias) was the right call
- Separating persona from preferences solved months of conceptual debt before it became a problem
- Time decay beats event-based in stateful systems where frequency patterns matter

## Next Steps

- Phase 5 (Discovery Pipeline) now unblocked
- Will use `get_session_state` to feed taste context into tag/artist filters
- Consider adding mood-implicit feedback in Phase 6 (mood mode can refine taste on the fly)
```

## File: `docs/journals/260319-2113-discover-rewrite-validation-closeout.md`
```markdown
# Discover Rewrite Closed Out, But Validation Still Drew Blood

**Date**: 2026-03-19 21:13
**Severity**: Medium
**Component**: Discover pipeline / validation
**Status**: Resolved

## What Happened

The flat Apple-only discover rewrite is effectively done. The grouped-lane flow is gone, the public MCP contract is now `discover(page?, limit?, artist?, genres?)`, cache invalidation is wired to `play_song()` and `add_song()`, and automated validation ended green. Final recorded state: `npm run build` passed, `npm test` passed with 93/93, and the built handler smoke returned a valid Apple candidate for `handleDiscover({ artist: 'Nils Frahm', limit: 1 })`.

## The Brutal Truth

This did not finish as cleanly as the final green test count makes it look. Validation exposed a real ranking bug first, then the test harness made the situation noisier than it needed to be. The frustrating part is that the rewrite itself was mostly right, but one ranker assertion proved the exploration path was still too weak, and Windows temp DB cleanup piled on after the failure. Classic last-mile mess: the signal was real, the noise was avoidable, and both had to be dealt with before the session could honestly be called done.

## Technical Details

The concrete failure was the exploration-heavy ranker test: novel artists were not consistently beating familiar ones when `exploration` was high. After that assertion failed, temp DB cleanup could also blow up because the SQLite file handle sometimes lingered long enough for `rmSync(...)` to complain on Windows. The fix landed in two parts: tighten the ranker behavior so the exploration case orders correctly, and harden test cleanup so a lingering handle does not mask the real failure. Result now matches the intended contract: ranker tests green, pipeline tests green, full suite green.

## What We Tried

Adjusted ranker behavior to preserve exploration wins. Kept explicit `store.close()` in test teardown. Made cleanup tolerant of post-assertion Windows handle lag instead of letting teardown noise overshadow the actual bug.

## Root Cause Analysis

Two separate problems surfaced together. The first was legitimate scoring behavior: the soft ranker still underweighted novelty in the exploration-heavy path. The second was test hygiene: cleanup assumed the filesystem would be immediately ready after failure, which is not a safe assumption with SQLite on Windows.

## Lessons Learned

Green-at-the-end is not the same as clean-throughout. Ranker behavior needs explicit tests for trait extremes, and teardown code should never be allowed to hide the original failure.

## Next Steps

Only one follow-up remains: record a full daemon/MCP smoke run. Everything else for the discover rewrite is landed and validated.

**Status:** DONE_WITH_CONCERNS
**Summary:** Flat Apple-only discover rewrite shipped with the main fixes landed; build, ranker coverage, pipeline coverage, and the full test suite are green.
**Concerns/Blockers:** Full daemon/MCP smoke validation is still not recorded.
```

## File: `public/app.js`
```javascript
import { DATABASE_ACTION_LABELS, STOP_DAEMON_LABEL } from './dashboard/constants.js';
import { elements } from './dashboard/dom.js';
import {
  buildDashboardWebSocketUrl,
  DASHBOARD_SESSION_EXPIRED_MESSAGE,
  dashboardFetch,
  isDashboardSessionExpiredError,
} from './dashboard/auth.js';
import {
  applySessionExpiredState,
  applyStoppedState,
  renderDatabaseStats,
  renderPersona,
  renderState,
  resetDangerActionLabels,
  setActiveView,
  setDangerActionArmed,
  showDatabaseMessage,
  showPersonaMessage,
} from './dashboard/render.js';
import {
  fetchDatabaseStats,
  postDatabaseAction,
  requestDaemonStop,
  savePersonaTaste,
} from './dashboard/settings-api.js';
import { syncTasteTextareaHeight } from './dashboard/taste-textarea.js';

let armedDangerAction = null;
let dangerArmTimer = null;
let daemonStoppedByUser = false;
let dashboardSessionExpired = false;
let socket;
let activeView = 'player';
let lastInsightTrackKey = '';
let allowStatusBootstrap = true;

function syncVolumeSliderFill(level) {
  elements.volume.style.setProperty('--volume-progress', `${level}%`);
}

function connect() {
  if (dashboardSessionExpired) {
    return;
  }

  try {
    socket = new WebSocket(buildDashboardWebSocketUrl('/ws'));
  } catch {
    handleDashboardSessionExpiry();
    return;
  }

  socket.addEventListener('message', (event) => {
    const payload = JSON.parse(event.data);
    if (payload.type === 'state') {
      allowStatusBootstrap = false;
      renderState(payload.data);
      maybeRefreshInsightsForState(payload.data);
    }
    if (payload.type === 'persona') {
      renderPersona(payload.data);
    }
  });

  socket.addEventListener('close', (event) => {
    if (event.code === 4403) {
      handleDashboardSessionExpiry();
      return;
    }

    if (!daemonStoppedByUser && !dashboardSessionExpired) {
      window.setTimeout(connect, 1000);
    }
  });
}

function sendSocketMessage(payload) {
  if (socket?.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify(payload));
    return true;
  }

  return false;
}

function transitionBetweenViews(nextView) {
  const fromPlayableView = activeView === 'player' || activeView === 'queue';
  const toPlayableView = nextView === 'player' || nextView === 'queue';
  const canTransition = typeof document.startViewTransition === 'function'
    && fromPlayableView
    && toPlayableView
    && activeView !== nextView;

  if (canTransition) {
    document.startViewTransition(() => {
      setActiveView(nextView);
      activeView = nextView;
      if (nextView === 'settings') {
        void loadDatabaseStats();
      }
    });
    return;
  }

  setActiveView(nextView);
  activeView = nextView;
  if (nextView === 'settings') {
    void loadDatabaseStats();
  }
}

function clearDangerArming() {
  armedDangerAction = null;
  if (dangerArmTimer) {
    window.clearTimeout(dangerArmTimer);
    dangerArmTimer = null;
  }
  resetDangerActionLabels();
}

function armDangerAction(button, action) {
  clearDangerArming();
  armedDangerAction = action;
  const label = action.kind === 'daemon'
    ? `Confirm ${STOP_DAEMON_LABEL}`
    : `Confirm ${DATABASE_ACTION_LABELS[action.id]}`;
  setDangerActionArmed(button, label);
  showDatabaseMessage('Click the same button again within 5 seconds to confirm.');
  dangerArmTimer = window.setTimeout(() => {
    clearDangerArming();
    showDatabaseMessage('Confirmation expired.');
  }, 5000);
}

async function loadDatabaseStats(options = {}) {
  const { preserveMessage = false } = options;
  try {
    const stats = await fetchDatabaseStats();
    renderDatabaseStats(stats);
    if (!preserveMessage) {
      showDatabaseMessage('');
    }
  } catch (error) {
    if (isDashboardSessionExpiredError(error)) {
      handleDashboardSessionExpiry();
      return;
    }
    showDatabaseMessage(error.message ?? 'Failed to load database stats.', true);
  }
}

async function runDatabaseAction(actionId, button) {
  button.disabled = true;
  try {
    const data = await postDatabaseAction(actionId);
    renderDatabaseStats(data.stats);
    showDatabaseMessage(data.message ?? 'Cleanup complete.');
    clearDangerArming();
  } catch (error) {
    if (isDashboardSessionExpiredError(error)) {
      handleDashboardSessionExpiry();
      return;
    }
    showDatabaseMessage(error.message ?? 'Database cleanup failed.', true);
  } finally {
    if (!dashboardSessionExpired) {
      button.disabled = false;
      await loadDatabaseStats({ preserveMessage: true });
    }
  }
}

async function runDaemonStop(button) {
  button.disabled = true;
  try {
    const data = await requestDaemonStop();
    daemonStoppedByUser = true;
    clearDangerArming();
    socket?.close();
    applyStoppedState(data.message ?? 'Daemon stop requested.');
  } catch (error) {
    if (isDashboardSessionExpiredError(error)) {
      handleDashboardSessionExpiry();
      return;
    }
    clearDangerArming();
    button.disabled = false;
    showDatabaseMessage(error.message ?? 'Daemon stop failed.', true);
  }
}

function maybeRefreshInsightsForState(state) {
  const nextTrackKey = `${state.title ?? ''}::${state.artist ?? ''}`;
  const trackChanged = nextTrackKey !== lastInsightTrackKey;
  lastInsightTrackKey = nextTrackKey;

  if (activeView === 'settings' && trackChanged) {
    void loadDatabaseStats();
  }
}

function handleDashboardSessionExpiry() {
  if (dashboardSessionExpired) {
    return;
  }

  dashboardSessionExpired = true;
  clearDangerArming();
  applySessionExpiredState(DASHBOARD_SESSION_EXPIRED_MESSAGE);
}

elements.navButtons.forEach((button) => {
  button.addEventListener('click', () => {
    transitionBetweenViews(button.dataset.nav ?? 'player');
  });
});

elements.volume.addEventListener('input', (event) => {
  const level = Number(event.target.value);
  syncVolumeSliderFill(level);
  if (sendSocketMessage({ type: 'volume', level })) {
    allowStatusBootstrap = false;
  }
});

elements.taste.addEventListener('input', () => {
  syncTasteTextareaHeight(elements.taste);
});

elements.pause.addEventListener('click', () => {
  if (elements.pause.disabled) {
    return;
  }
  if (sendSocketMessage({ type: 'playback-toggle' })) {
    allowStatusBootstrap = false;
  }
});

elements.next.addEventListener('click', () => {
  if (sendSocketMessage({ type: 'next' })) {
    allowStatusBootstrap = false;
  }
});

elements.saveTaste.addEventListener('click', async () => {
  try {
    const data = await savePersonaTaste(elements.taste.value.trim());
    showPersonaMessage('Persona saved.');
    renderPersona(data);
  } catch (error) {
    if (isDashboardSessionExpiredError(error)) {
      handleDashboardSessionExpiry();
      return;
    }
    showPersonaMessage(error.message ?? 'Persona save failed.', true);
  }
});

elements.databaseActions.forEach((button) => {
  button.addEventListener('click', async () => {
    const actionId = button.dataset.dbAction;
    const action = { kind: 'database', id: actionId };
    if (!actionId) {
      return;
    }
    if (armedDangerAction?.kind !== action.kind || armedDangerAction?.id !== action.id) {
      armDangerAction(button, action);
      return;
    }
    await runDatabaseAction(actionId, button);
  });
});

elements.stopDaemon.addEventListener('click', async () => {
  const action = { kind: 'daemon', id: 'stop-daemon' };
  if (armedDangerAction?.kind !== action.kind) {
    armDangerAction(elements.stopDaemon, action);
    return;
  }
  await runDaemonStop(elements.stopDaemon);
});

dashboardFetch('/api/status')
  .then((response) => response.json())
  .then((state) => {
    if (!allowStatusBootstrap) {
      return;
    }
    allowStatusBootstrap = false;
    renderState(state);
    maybeRefreshInsightsForState(state);
  })
  .catch((error) => {
    if (isDashboardSessionExpiredError(error)) {
      handleDashboardSessionExpiry();
      return;
    }
    showDatabaseMessage('Waiting for server state.');
  });

dashboardFetch('/api/persona')
  .then((response) => response.json())
  .then((data) => renderPersona(data))
  .catch((error) => {
    if (isDashboardSessionExpiredError(error)) {
      handleDashboardSessionExpiry();
    }
  });

syncVolumeSliderFill(Number(elements.volume.value));
syncTasteTextareaHeight(elements.taste);
setActiveView('player');
activeView = 'player';
void loadDatabaseStats();
connect();
```

## File: `public/index.html`
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>agentune</title>
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=Outfit:wght@400;500;600;700&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="/style.css" />
    <link rel="stylesheet" href="/styles/dashboard-settings.css" />
  </head>
  <body>
    <div class="bg-layer" data-bg-layer></div>

    <main class="shell">
      <!-- Now Playing View (default) -->
      <section class="view-panel player-view-panel" id="player-view" data-view="player">
        <div class="art-stage">
          <div class="art-frame" data-shared-art-frame>
            <img data-art alt="Album art" src="/assets/agentune-mark.svg" />
          </div>
        </div>

        <div class="track-info">
          <div class="title-row">
            <h1 class="track-title" data-title>Nothing playing</h1>
          </div>
          <p class="track-artist" data-artist>Ask your agent to start a track</p>
        </div>
      </section>

      <!-- Queue View -->
      <section class="view-panel queue-view-panel" id="queue-view" data-view="queue" hidden>
        <header class="view-header queue-view-header">
          <p class="queue-list-title">Playing</p>
        </header>
        <section class="queue-current">
          <div class="queue-current-art-frame" data-shared-art-frame>
            <img data-queue-art class="queue-current-art" alt="Now playing artwork" src="/assets/agentune-mark.svg" />
          </div>
          <div class="queue-current-copy">
            <strong data-queue-current-title>Nothing playing</strong>
            <span data-queue-current-artist>Ask your agent to start a track</span>
          </div>
        </section>
        <p class="queue-list-title">Up next</p>
        <div class="queue-list-scroll">
          <ul data-queue class="queue-list">
            <li class="queue-empty">Queue is empty</li>
          </ul>
        </div>
      </section>

      <!-- Settings View -->
      <section class="view-panel" id="settings-view" data-view="settings" hidden>
        <header class="view-header view-header-dashboard">
          <p class="queue-list-title settings-header-line">Dashboard</p>
        </header>

        <section class="settings-section settings-dashboard">
          <section class="settings-card insights-chart-card">
            <div class="settings-card-head settings-card-head-compact">
              <h3>Last 7 days</h3>
            </div>
            <div class="activity-chart activity-line-chart" data-activity-chart></div>
          </section>

          <div class="dashboard-grid">
            <section class="settings-card dashboard-metric-card dashboard-plays-card">
              <article class="insight-card insight-card-compact">
                <span class="insight-label">Plays</span>
                <strong class="insight-value" data-insight-plays>0</strong>
              </article>
            </section>

            <section class="settings-card dashboard-metric-card dashboard-tracks-card">
              <article class="insight-card insight-card-compact">
                <span class="insight-label">Tracks</span>
                <strong class="insight-value" data-insight-tracks>0</strong>
              </article>
            </section>

            <section class="settings-card dashboard-artists-card">
              <div class="settings-card-head settings-card-head-compact">
                <h3>Most artists</h3>
              </div>
              <ul class="rank-list" data-top-artists></ul>
            </section>

            <section class="settings-card dashboard-tags-card">
              <div class="settings-card-head settings-card-head-compact">
                <h3>Most tags</h3>
              </div>
              <ul class="keyword-list keyword-list-minimal" data-top-keywords></ul>
            </section>
          </div>
        </section>

        <p class="queue-list-title settings-section-title">Preferences</p>

        <section class="settings-card taste-card">
          <div class="settings-card-head settings-card-head-compact">
            <h3>Taste</h3>
          </div>
          <textarea
            data-taste
            rows="1"
            maxlength="1000"
            placeholder="Warm piano at night, patient Vietnamese ballads, ambient..."
          ></textarea>
          <button data-save-taste type="button" class="primary-btn taste-save-btn" aria-label="Save taste">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
              <path d="M5 12.5l4.2 4.2L19 7.5" />
            </svg>
          </button>
          <p class="message" data-message></p>
        </section>

        <details class="advanced">
          <summary>
            <span>Advanced Settings</span>
            <span class="summary-sub">Database & daemon</span>
          </summary>
          <div class="advanced-content">
            <div class="db-stats">
              <div class="stat"><span>DB path</span><code data-db-path>Loading…</code></div>
              <div class="stat"><span>plays</span><strong data-db-plays>0</strong></div>
              <div class="stat"><span>tracks</span><strong data-db-tracks>0</strong></div>
              <div class="stat"><span>cache</span><strong data-db-cache>0</strong></div>
            </div>
            <div class="danger-zone">
              <div class="btn-row btn-row-advanced">
                <button data-db-action="clear-provider-cache" type="button" class="danger-btn">Clear cache</button>
                <button data-db-action="clear-history" type="button" class="danger-btn">Clear history</button>
                <button data-db-action="full-reset" type="button" class="danger-btn hard">Full reset</button>
                <button data-stop-daemon type="button" class="danger-btn hard">Stop daemon</button>
              </div>
              <p class="message" data-db-message></p>
            </div>
          </div>
        </details>
      </section>

      <div class="player-controls" data-shared-controls>
        <div class="duration-block">
          <div class="duration-bar" aria-hidden="true">
            <span class="duration-fill" data-duration-fill></span>
          </div>
          <div class="duration-meta" aria-label="Playback duration">
            <span data-elapsed>0:00</span>
            <span data-total-duration>0:00</span>
          </div>
        </div>

        <div class="transport-row">
          <button data-pause type="button" class="icon-btn transport-btn transport-btn-primary" aria-label="Pause playback">
            <svg class="icon-pause" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="6" y="4" width="4" height="16"/>
              <rect x="14" y="4" width="4" height="16"/>
            </svg>
            <svg class="icon-play" viewBox="0 0 24 24" fill="currentColor" hidden>
              <polygon points="7,5 19,12 7,19"/>
            </svg>
          </button>
          <button data-next type="button" class="icon-btn transport-btn" aria-label="Skip track">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="5,4 15,12 5,20 5,4"/>
              <line x1="19" y1="5" x2="19" y2="19"/>
            </svg>
          </button>
        </div>

        <div class="volume-row">
          <span class="volume-icon volume-icon-min" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M11 5L6 9H3v6h3l5 4V5z"/>
            </svg>
          </span>
          <input data-volume type="range" min="0" max="100" value="80" class="volume-slider" aria-label="Volume" />
          <span class="volume-icon volume-icon-max" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M11 5L6 9H3v6h3l5 4V5z"/>
              <path d="M15 9a4 4 0 0 1 0 6"/>
              <path d="M18 6.5a7.5 7.5 0 0 1 0 11"/>
            </svg>
          </span>
        </div>
      </div>

      <!-- Bottom Nav -->
      <nav class="tab-bar">
        <button type="button" class="tab-btn" data-nav="queue" aria-pressed="false">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <path d="M8 6h13M8 12h10M8 18h13"/>
          </svg>
          <span>Queue</span>
        </button>

        <button type="button" class="tab-btn is-active" data-nav="player" aria-pressed="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="12" cy="12" r="10"/>
            <circle cx="12" cy="12" r="3"/>
          </svg>
          <span>Now Playing</span>
        </button>

        <button type="button" class="tab-btn" data-nav="settings" aria-pressed="false">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
            <circle cx="12" cy="12" r="3"/>
            <path d="M12 1v4M12 19v4M4.22 4.22l2.83 2.83M16.95 16.95l2.83 2.83M1 12h4M19 12h4M4.22 19.78l2.83-2.83M16.95 7.05l2.83-2.83"/>
          </svg>
          <span>Settings</span>
        </button>
      </nav>
    </main>

    <script type="module" src="/app.js"></script>
  </body>
</html>
```

## File: `public/style.css`
```css
/* Apple Music style dashboard */
* {
  box-sizing: border-box;
}

@property --ambient-start {
  syntax: '<color>';
  inherits: true;
  initial-value: rgba(18, 28, 44, 0.96);
}

@property --ambient-mid {
  syntax: '<color>';
  inherits: true;
  initial-value: rgba(26, 44, 70, 0.72);
}

@property --ambient-end {
  syntax: '<color>';
  inherits: true;
  initial-value: rgba(5, 8, 14, 0.98);
}

@property --accent-soft {
  syntax: '<color>';
  inherits: true;
  initial-value: rgba(173, 198, 255, 0.18);
}

:root {
  --bg-base: #000;
  --ink: #fff;
  --ink-muted: rgba(255, 255, 255, 0.5);
  --ambient-start: rgba(18, 28, 44, 0.96);
  --ambient-mid: rgba(26, 44, 70, 0.72);
  --ambient-end: rgba(5, 8, 14, 0.98);
  --surface: rgba(10, 16, 27, 0.72);
  --surface-strong: rgba(14, 20, 34, 0.92);
  --surface-soft: rgba(255, 255, 255, 0.06);
  --surface-hover: rgba(255, 255, 255, 0.12);
  --accent: #dce9ff;
  --accent-soft: rgba(173, 198, 255, 0.18);
  --shadow-tint: rgba(3, 6, 12, 0.46);
  --success-pill-bg: rgba(222, 233, 255, 0.16);
  --success-pill-ink: #f4f7ff;
  --danger: #ff6b6b;
  --font-ui: 'Be Vietnam Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-display: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --pause-visual-duration: 280ms;
  --pause-icon-duration: 220ms;
  --pause-art-scale: 0.92;
  --pause-art-grayscale: 0.9;
  --pause-art-saturate: 0.35;
  --pause-art-brightness: 0.92;
  --pause-bg-grayscale: 0.82;
  --pause-bg-saturate: 0.4;
  --pause-bg-brightness: 0.9;
  --pause-icon-scale: 1.15;
  --bg-theme-duration: 360ms;
}

body {
  margin: 0;
  min-height: 100dvh;
  font-family: var(--font-ui);
  color: var(--ink);
  background: var(--ambient-end);
  -webkit-font-smoothing: antialiased;
}

button,
input,
textarea {
  font: inherit;
}

/* Dynamic background gradient from album art */
.bg-layer {
  position: fixed;
  inset: 0;
  z-index: -1;
  background:
    radial-gradient(circle at 18% 14%, var(--accent-soft) 0%, transparent 34%),
    linear-gradient(180deg, var(--ambient-start) 0%, var(--ambient-mid) 48%, var(--ambient-end) 100%);
  filter: grayscale(0) saturate(1) brightness(1);
  transition:
    --ambient-start var(--bg-theme-duration) ease,
    --ambient-mid var(--bg-theme-duration) ease,
    --ambient-end var(--bg-theme-duration) ease,
    --accent-soft var(--bg-theme-duration) ease,
    opacity var(--pause-visual-duration) ease,
    filter var(--pause-visual-duration) ease;
}

.bg-layer::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse at 50% 0%, var(--accent-soft) 0%, transparent 62%),
    linear-gradient(180deg, transparent 0%, rgba(0, 0, 0, 0.28) 100%);
  opacity: 1;
  transition:
    --accent-soft var(--bg-theme-duration) ease,
    opacity var(--pause-visual-duration) ease,
    filter var(--pause-visual-duration) ease;
}

/* Full screen centered shell */
.shell {
  position: relative;
  z-index: 1;
  height: 100dvh;
  min-height: 100dvh;
  width: min(420px, 100%);
  margin: 0 auto;
  padding: 1.5rem 1.25rem;
  padding-bottom: calc(5rem + env(safe-area-inset-bottom, 0px));
  display: flex;
  flex-direction: column;
}

/* View panels */
.view-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  min-height: 0;
  overflow-y: auto;
}

.player-view-panel {
  justify-content: center;
}

.queue-view-panel {
  width: 100%;
  align-items: stretch;
  text-align: left;
  overflow: hidden;
}

/* Album Art - 1:1 square */
.art-stage {
  width: 100%;
  display: flex;
  justify-content: center;
  padding: 0.5rem 0 1.5rem;
}

.art-frame {
  width: min(85%, 280px);
  aspect-ratio: 1;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 1rem 2.4rem rgba(0, 0, 0, 0.28);
  view-transition-name: current-track-art;
  transform: scale(1);
  transform-origin: center;
  transition: transform var(--pause-visual-duration) ease;
}

.art-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: grayscale(0) saturate(1) brightness(1);
  transition: filter var(--pause-visual-duration) ease;
}

/* Track info */
.track-info {
  width: 100%;
  max-width: 320px;
  margin-bottom: 1.5rem;
}

.title-row {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 2.4rem;
  margin-bottom: 0.25rem;
}

.track-title {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.2;
  max-width: 100%;
}

.track-title-viewport {
  display: block;
  max-width: 100%;
  overflow: hidden;
}

.track-title-track {
  display: block;
  max-width: 100%;
}

.track-title-copy {
  display: block;
  white-space: nowrap;
}

.track-title:not(.is-long) .track-title-copy.primary {
  overflow: hidden;
  text-overflow: ellipsis;
}

.track-title:not(.is-long) .track-title-copy.secondary {
  display: none;
}

.track-title.is-long .track-title-track {
  display: inline-flex;
  align-items: center;
  gap: var(--title-gap, 32px);
  min-width: max-content;
  will-change: transform;
  animation: marquee-flow var(--title-duration, 14s) linear infinite;
}

@keyframes marquee-flow {
  from { transform: translateX(0); }
  to { transform: translateX(calc(-1 * var(--title-distance, 0px))); }
}

.track-artist {
  margin: 0;
  font-size: 1rem;
  color: var(--ink-muted);
}

/* Player controls */
.player-controls {
  width: 100%;
  max-width: 320px;
  display: grid;
  gap: 1rem;
  align-self: center;
  flex-shrink: 0;
  margin-top: 1.75rem;
}

.duration-block {
  display: grid;
  gap: 0.45rem;
}

.duration-bar {
  width: 100%;
  height: 3px;
  border-radius: 999px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.24);
}

.duration-fill {
  display: block;
  width: 0%;
  height: 100%;
  border-radius: inherit;
  background: rgba(255, 255, 255, 0.98);
}

.duration-meta {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  font-size: 0.76rem;
  line-height: 1;
  letter-spacing: 0.02em;
  color: rgba(255, 255, 255, 0.68);
  font-variant-numeric: tabular-nums;
}

.transport-row {
  display: grid;
  grid-template-columns: 2.75rem auto 2.75rem;
  justify-content: center;
  align-items: center;
  column-gap: 1rem;
}

.transport-row::before {
  content: '';
  width: 2.75rem;
  height: 2.75rem;
}

.transport-row [data-pause] {
  grid-column: 2;
}

.transport-row [data-next] {
  grid-column: 3;
  justify-self: end;
}

.volume-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.icon-btn {
  flex-shrink: 0;
  width: 2.75rem;
  height: 2.75rem;
  display: grid;
  place-items: center;
  border: none;
  border-radius: 50%;
  background: transparent;
  color: var(--ink);
  cursor: pointer;
  transition: all 0.2s;
}

.icon-btn:hover {
  opacity: 0.7;
}

.icon-btn:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}

.transport-btn {
  background: transparent;
  box-shadow: none;
}

.transport-btn:hover:not(:disabled) {
  background: transparent;
  opacity: 1;
}

.transport-btn-primary {
  width: 3.5rem;
  height: 3.5rem;
  background: transparent;
  color: var(--ink);
}

.transport-btn-primary svg {
  width: 1.7rem;
  height: 1.7rem;
}

.transport-btn-primary .icon-pause,
.transport-btn-primary .icon-play {
  transform: scale(1);
  transform-origin: center;
  transition: transform var(--pause-icon-duration) ease;
}

.icon-btn svg {
  width: 1.5rem;
  height: 1.5rem;
}

.volume-slider {
  --volume-progress: 80%;
  flex: 1;
  min-width: 0;
  height: 4px;
  -webkit-appearance: none;
  appearance: none;
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0.98) 0%,
    rgba(255, 255, 255, 0.98) var(--volume-progress),
    rgba(255, 255, 255, 0.28) var(--volume-progress),
    rgba(255, 255, 255, 0.28) 100%
  );
  border-radius: 2px;
  outline: none;
}

.volume-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 1);
  cursor: pointer;
}

.volume-slider::-moz-range-thumb {
  width: 12px;
  height: 12px;
  border: none;
  border-radius: 50%;
  background: rgba(255, 255, 255, 1);
  cursor: pointer;
}

.volume-icon {
  flex-shrink: 0;
  color: rgba(255, 255, 255, 0.94);
  display: grid;
  place-items: center;
}

.volume-icon svg {
  width: 1.15rem;
  height: 1.15rem;
}

.volume-icon-max svg {
  width: 1.3rem;
  height: 1.3rem;
}

/* Queue & Settings views */
.view-header {
  width: 100%;
  text-align: left;
  padding: 0.5rem 0 1.5rem;
}

.eyebrow {
  margin: 0 0 0.25rem;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--ink-muted);
}

.view-header h2 {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.75rem;
  font-weight: 600;
}

.queue-view-header {
  padding-bottom: 1rem;
}

.queue-view-header .queue-list-title {
  margin-bottom: 0;
}

/* Queue list */
.queue-list {
  width: 100%;
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.9rem;
  text-align: left;
}

.queue-current {
  width: 100%;
  display: grid;
  grid-template-columns: 4.25rem minmax(0, 1fr);
  align-items: center;
  gap: 0.9rem;
  margin-bottom: 1.5rem;
  text-align: left;
}

.queue-list-scroll {
  width: 100%;
  min-height: 0;
  flex: 1;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding-bottom: 0.5rem;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.queue-list-scroll::-webkit-scrollbar {
  display: none;
}

.queue-list-title {
  width: 100%;
  margin: 0 0 1rem;
  text-align: left;
  font-size: 0.76rem;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--ink-muted);
}

.queue-current-art {
  width: 4.25rem;
  height: 4.25rem;
  object-fit: cover;
  display: block;
  filter: grayscale(0) saturate(1) brightness(1);
  transition: filter var(--pause-visual-duration) ease;
}

.queue-current-art-frame {
  width: 4.25rem;
  height: 4.25rem;
  border-radius: 0.85rem;
  overflow: hidden;
  view-transition-name: current-track-art;
  transform: scale(1);
  transform-origin: center;
  transition: transform var(--pause-visual-duration) ease;
}

:root[data-playback-visual-state="paused"] .art-frame,
:root[data-playback-visual-state="paused"] .queue-current-art-frame {
  transform: scale(var(--pause-art-scale));
}

:root[data-playback-visual-state="paused"] .art-frame img,
:root[data-playback-visual-state="paused"] .queue-current-art {
  filter:
    grayscale(var(--pause-art-grayscale))
    saturate(var(--pause-art-saturate))
    brightness(var(--pause-art-brightness));
}

:root[data-playback-visual-state="paused"] .bg-layer {
  filter:
    grayscale(var(--pause-bg-grayscale))
    saturate(var(--pause-bg-saturate))
    brightness(var(--pause-bg-brightness));
}

:root[data-playback-visual-state="paused"] .bg-layer::before {
  opacity: 0.72;
  filter: grayscale(0.18) brightness(0.92);
}

:root[data-playback-visual-state="paused"] [data-pause] .icon-play {
  transform: scale(var(--pause-icon-scale));
}

.queue-current-copy {
  min-width: 0;
  display: grid;
  gap: 0.25rem;
}

.queue-current-copy strong,
.queue-list strong {
  display: block;
  min-width: 0;
  font-size: 1rem;
  font-weight: 600;
  line-height: 1.2;
}

.queue-current-copy span,
.queue-list span {
  display: block;
  font-size: 0.92rem;
  line-height: 1.25;
  color: var(--ink-muted);
}

.queue-list li {
  padding: 0;
  background: transparent;
  box-shadow: none;
  border-radius: 0;
  display: grid;
  gap: 0.2rem;
}

.queue-empty {
  color: var(--ink-muted);
  text-align: center;
  padding: 2rem;
}

::view-transition-group(current-track-art) {
  animation-duration: 420ms;
  animation-timing-function: cubic-bezier(0.22, 1, 0.36, 1);
}

::view-transition-old(current-track-art),
::view-transition-new(current-track-art) {
  animation-duration: 420ms;
  animation-timing-function: cubic-bezier(0.22, 1, 0.36, 1);
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(current-track-art),
  ::view-transition-old(current-track-art),
  ::view-transition-new(current-track-art) {
    animation-duration: 0ms;
  }

  .bg-layer,
  .bg-layer::before,
  .art-frame,
  .art-frame img,
  .queue-current-art-frame,
  .queue-current-art,
  .transport-btn-primary .icon-pause,
  .transport-btn-primary .icon-play {
    transition-duration: 0ms;
  }
}

/* Settings */
.settings-card {
  width: 100%;
  padding: 1.25rem;
  background: var(--surface);
  box-shadow: inset 0 0 0 1px var(--surface-soft);
  border-radius: 1rem;
  text-align: left;
}

.field-label {
  display: block;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--ink-muted);
  margin-bottom: 0.5rem;
}

.settings-card textarea {
  width: 100%;
  padding: 0.75rem 1rem;
  border: 1px solid var(--surface-soft);
  border-radius: 0.75rem;
  background: var(--surface-strong);
  color: var(--ink);
  font-family: inherit;
  font-size: 0.95rem;
  resize: vertical;
}

.settings-card textarea:focus {
  outline: none;
  border-color: var(--accent);
}

.help-text {
  margin: 0.5rem 0;
  font-size: 0.8rem;
  color: var(--ink-muted);
}

.primary-btn {
  margin-top: 0.5rem;
  padding: 0.65rem 1.5rem;
  border: none;
  border-radius: 999px;
  background: var(--accent);
  color: var(--ambient-end);
  font-family: inherit;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
}

.message {
  margin: 0.5rem 0 0;
  font-size: 0.8rem;
  color: var(--ink-muted);
  min-height: 1.2em;
}

.message.is-error {
  color: var(--danger);
}

/* Advanced section */
.advanced {
  width: 100%;
  margin-top: 1rem;
  background: var(--surface);
  box-shadow: inset 0 0 0 1px var(--surface-soft);
  border-radius: 1rem;
}

.advanced summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.25rem;
  cursor: pointer;
  list-style: none;
}

.advanced summary::-webkit-details-marker {
  display: none;
}

.advanced summary span:first-child {
  font-weight: 600;
}

.summary-sub {
  font-size: 0.8rem;
  color: var(--ink-muted);
}

.advanced-content {
  padding: 0 1.25rem 1.25rem;
  display: grid;
  gap: 1rem;
}

.db-stats {
  display: grid;
  gap: 0.75rem;
}

.stat {
  display: flex;
  justify-content: space-between;
  font-size: 0.85rem;
}

.stat span {
  color: var(--ink-muted);
}

.stat code {
  font-family: 'SF Mono', Consolas, monospace;
  font-size: 0.75rem;
  max-width: 180px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.danger-zone {
  display: grid;
  gap: 0.75rem;
}

.btn-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.danger-btn {
  padding: 0.5rem 0.85rem;
  border: none;
  border-radius: 999px;
  background: var(--danger);
  color: #000;
  font-family: inherit;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
}

.danger-btn.subtle {
  background: rgba(255, 255, 255, 0.9);
  color: #000;
}

.danger-btn.hard {
  background: #ff4444;
  color: #fff;
}

/* Bottom tab bar - fixed to bottom */
.tab-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 100;
  display: flex;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.75rem 1rem;
  padding-bottom: calc(0.75rem + env(safe-area-inset-bottom, 0.75rem));
  background: transparent;
}

.tab-btn {
  flex: 1;
  max-width: 100px;
  display: grid;
  place-items: center;
  gap: 0.25rem;
  padding: 0.5rem;
  border: none;
  border-radius: 0.75rem;
  background: transparent;
  color: var(--ink-muted);
  font-family: inherit;
  font-size: 0.65rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.tab-btn svg {
  width: 1.25rem;
  height: 1.25rem;
}

.tab-btn.is-active {
  background: transparent;
  color: var(--ink);
}

/* Hide views */
[hidden] {
  display: none !important;
}

/* Skip link for accessibility */
.skip-link {
  position: fixed;
  top: -100px;
  left: 1rem;
  padding: 0.75rem 1rem;
  background: var(--surface-strong);
  color: var(--ink);
  border-radius: 999px;
  z-index: 200;
  text-decoration: none;
}

.skip-link:focus {
  top: 1rem;
}

/* Responsive */
@media (max-width: 420px) {
  .shell {
    padding: 1rem;
    padding-bottom: calc(4.5rem + env(safe-area-inset-bottom, 0.5rem));
  }

  .art-frame {
    width: 90%;
  }

  .transport-row {
    column-gap: 0.75rem;
  }

  .tab-btn {
    max-width: 90px;
  }
}
```

## File: `public/dashboard/activity-chart.js`
```javascript
const LINE_CHART_WIDTH = 320;
const LINE_CHART_HEIGHT = 148;
const LINE_CHART_PADDING_X = 12;
const LINE_CHART_PADDING_Y = 16;
const MIN_TOOLTIP_TOP_PERCENT = 16;
const MIN_TOOLTIP_LEFT_PERCENT = 8;
const MAX_TOOLTIP_LEFT_PERCENT = 92;

let cleanupActivityChart = () => {};

export function renderActivityChart(container, activity7d) {
  cleanupActivityChart();
  cleanupActivityChart = () => {};

  container.replaceChildren();
  container.setAttribute('role', 'group');
  container.setAttribute('aria-label', 'Listening activity for the last 7 days');

  const maxPlays = Math.max(...activity7d.map((bucket) => bucket.plays), 0);
  if (maxPlays === 0) {
    container.append(createEmptyState('div', 'No plays yet.'));
    return;
  }

  const supportsHover = window.matchMedia('(hover: hover)').matches;
  const chartShell = document.createElement('div');
  const stage = document.createElement('div');
  const tooltip = document.createElement('div');
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
  const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
  const gradient = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
  const stopTop = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
  const stopBottom = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
  const areaPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  const linePath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
  const labels = document.createElement('div');
  const points = buildPoints(activity7d, maxPlays);
  const pointNodes = [];
  const targetNodes = [];
  let pinnedIndex = null;

  chartShell.className = 'activity-line-shell';
  stage.className = 'activity-line-stage';
  tooltip.className = 'activity-line-tooltip';
  tooltip.setAttribute('aria-hidden', 'true');
  labels.className = 'activity-line-labels';

  svg.setAttribute('viewBox', `0 0 ${LINE_CHART_WIDTH} ${LINE_CHART_HEIGHT}`);
  svg.setAttribute('class', 'activity-line-svg');
  svg.setAttribute('preserveAspectRatio', 'none');
  svg.setAttribute('aria-hidden', 'true');

  gradient.setAttribute('id', 'activity-line-gradient');
  gradient.setAttribute('x1', '0');
  gradient.setAttribute('x2', '0');
  gradient.setAttribute('y1', '0');
  gradient.setAttribute('y2', '1');

  stopTop.setAttribute('offset', '0%');
  stopTop.setAttribute('stop-color', '#ffffff');
  stopTop.setAttribute('stop-opacity', '0.24');
  stopBottom.setAttribute('offset', '100%');
  stopBottom.setAttribute('stop-color', '#ffffff');
  stopBottom.setAttribute('stop-opacity', '0');
  gradient.append(stopTop, stopBottom);
  defs.append(gradient);

  areaPath.setAttribute('d', buildAreaPath(points));
  areaPath.setAttribute('class', 'activity-line-area');
  areaPath.setAttribute('fill', 'url(#activity-line-gradient)');

  linePath.setAttribute('d', buildSmoothPath(points));
  linePath.setAttribute('class', 'activity-line-stroke');

  svg.append(defs, areaPath, linePath);
  points.forEach((point, index) => {
    const circle = createPoint(point, index === points.length - 1);
    const target = createTarget(activity7d[index], point);

    circle.classList.add('activity-line-point');
    if (index === points.length - 1) {
      circle.classList.add('is-last');
    }

    target.addEventListener('pointerenter', () => {
      if (supportsHover && pinnedIndex === null) {
        showTooltip(index);
      }
    });

    target.addEventListener('pointerleave', () => {
      if (supportsHover) {
        hideTooltip();
      }
    });

    target.addEventListener('focus', () => {
      showTooltip(index);
    });

    target.addEventListener('blur', () => {
      hideTooltip();
    });

    target.addEventListener('click', () => {
      if (!supportsHover) {
        showTooltip(index, { pin: true });
      }
    });

    target.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        hideTooltip({ clearPinned: true });
        target.blur();
      }
    });

    pointNodes.push(circle);
    targetNodes.push(target);
    svg.append(circle);
    stage.append(target);
  });

  activity7d.forEach((bucket) => {
    const label = document.createElement('span');
    label.className = 'activity-line-label';
    label.textContent = bucket.dayLabel;
    labels.append(label);
  });

  stage.prepend(svg);
  stage.append(tooltip);
  chartShell.append(stage, labels);
  container.append(chartShell);

  const handleDocumentPointerDown = (event) => {
    if (!(event.target instanceof Node)) {
      return;
    }
    if (!stage.contains(event.target)) {
      hideTooltip({ clearPinned: true });
    }
  };

  document.addEventListener('pointerdown', handleDocumentPointerDown);
  cleanupActivityChart = () => {
    document.removeEventListener('pointerdown', handleDocumentPointerDown);
  };

  function showTooltip(index, { pin = false } = {}) {
    const point = points[index];
    const bucket = activity7d[index];

    if (pin) {
      pinnedIndex = index;
    }

    tooltip.textContent = String(bucket.plays);
    tooltip.classList.add('is-visible');
    tooltip.style.setProperty('--tooltip-left', `${clamp((point.x / LINE_CHART_WIDTH) * 100, MIN_TOOLTIP_LEFT_PERCENT, MAX_TOOLTIP_LEFT_PERCENT)}%`);
    tooltip.style.setProperty('--tooltip-top', `${Math.max((point.y / LINE_CHART_HEIGHT) * 100, MIN_TOOLTIP_TOP_PERCENT)}%`);

    pointNodes.forEach((node, nodeIndex) => {
      node.classList.toggle('is-active', nodeIndex === index);
    });
    targetNodes.forEach((node, nodeIndex) => {
      node.classList.toggle('is-active', nodeIndex === index);
    });
  }

  function hideTooltip({ clearPinned = false } = {}) {
    if (clearPinned) {
      pinnedIndex = null;
    }

    if (pinnedIndex !== null) {
      showTooltip(pinnedIndex);
      return;
    }

    tooltip.classList.remove('is-visible');
    pointNodes.forEach((node) => node.classList.remove('is-active'));
    targetNodes.forEach((node) => node.classList.remove('is-active'));
  }
}

function createPoint(point, isLast) {
  const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
  circle.setAttribute('cx', String(point.x));
  circle.setAttribute('cy', String(point.y));
  circle.setAttribute('r', isLast ? '4' : '3');
  return circle;
}

function createTarget(bucket, point) {
  const target = document.createElement('button');
  target.type = 'button';
  target.className = 'activity-line-target';
  target.setAttribute('aria-label', `${bucket.dayLabel}: ${bucket.plays}`);
  target.style.left = `${(point.x / LINE_CHART_WIDTH) * 100}%`;
  target.style.top = `${(point.y / LINE_CHART_HEIGHT) * 100}%`;
  return target;
}

function buildPoints(activity7d, maxPlays) {
  const innerWidth = LINE_CHART_WIDTH - (LINE_CHART_PADDING_X * 2);
  const innerHeight = LINE_CHART_HEIGHT - (LINE_CHART_PADDING_Y * 2);
  const stepX = activity7d.length > 1 ? innerWidth / (activity7d.length - 1) : innerWidth;

  return activity7d.map((bucket, index) => ({
    x: LINE_CHART_PADDING_X + (stepX * index),
    y: LINE_CHART_PADDING_Y + innerHeight - ((bucket.plays / maxPlays) * innerHeight),
  }));
}

function buildSmoothPath(points) {
  if (points.length === 0) {
    return '';
  }
  if (points.length === 1) {
    return `M ${points[0].x} ${points[0].y}`;
  }

  let d = `M ${points[0].x} ${points[0].y}`;
  for (let index = 0; index < points.length - 1; index += 1) {
    const current = points[index];
    const next = points[index + 1];
    const midX = (current.x + next.x) / 2;
    d += ` C ${midX} ${current.y}, ${midX} ${next.y}, ${next.x} ${next.y}`;
  }
  return d;
}

function buildAreaPath(points) {
  if (points.length === 0) {
    return '';
  }

  const baseline = LINE_CHART_HEIGHT - LINE_CHART_PADDING_Y;
  return `${buildSmoothPath(points)} L ${points[points.length - 1].x} ${baseline} L ${points[0].x} ${baseline} Z`;
}

function createEmptyState(tagName, message) {
  const item = document.createElement(tagName);
  item.className = 'insight-empty';
  item.textContent = message;
  return item;
}

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}
```

## File: `public/dashboard/auth.js`
```javascript
export const DASHBOARD_SESSION_EXPIRED_MESSAGE = 'Dashboard session expired. Refresh page.';

const DASHBOARD_TOKEN_HEADER = 'X-Agentune-Dashboard-Token';
const DASHBOARD_TOKEN_META_NAME = 'agentune-dashboard-token';
const DASHBOARD_TOKEN_QUERY_PARAM = 'dashboardToken';

let cachedDashboardToken = '';

export async function dashboardFetch(input, init = {}) {
  const headers = new Headers(init.headers ?? {});
  headers.set(DASHBOARD_TOKEN_HEADER, getDashboardToken());

  const response = await fetch(input, {
    ...init,
    headers,
  });
  if (response.status === 403) {
    throw new Error(DASHBOARD_SESSION_EXPIRED_MESSAGE);
  }

  return response;
}

export function buildDashboardWebSocketUrl(pathname = '/ws') {
  const url = new URL(pathname, window.location.href);
  url.protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
  url.searchParams.set(DASHBOARD_TOKEN_QUERY_PARAM, getDashboardToken());
  return url.toString();
}

export function appendDashboardTokenToPath(pathname) {
  const url = new URL(pathname, window.location.href);
  url.searchParams.set(DASHBOARD_TOKEN_QUERY_PARAM, getDashboardToken());
  return url.origin === window.location.origin
    ? `${url.pathname}${url.search}${url.hash}`
    : url.toString();
}

export function isDashboardSessionExpiredError(error) {
  return error instanceof Error && error.message === DASHBOARD_SESSION_EXPIRED_MESSAGE;
}

function getDashboardToken() {
  if (cachedDashboardToken) {
    return cachedDashboardToken;
  }

  const tokenMeta = document.querySelector(`meta[name="${DASHBOARD_TOKEN_META_NAME}"]`);
  if (!(tokenMeta instanceof HTMLMetaElement) || !tokenMeta.content) {
    throw new Error(DASHBOARD_SESSION_EXPIRED_MESSAGE);
  }

  cachedDashboardToken = tokenMeta.content;
  return cachedDashboardToken;
}
```

## File: `public/dashboard/constants.js`
```javascript
export const DATABASE_ACTION_LABELS = {
  'clear-history': 'Clear history',
  'clear-provider-cache': 'Clear provider cache',
  'full-reset': 'Full reset',
};

export const DEFAULT_THEME = {
  'ambient-start': 'rgba(18, 28, 44, 0.96)',
  'ambient-mid': 'rgba(26, 44, 70, 0.72)',
  'ambient-end': 'rgba(5, 8, 14, 0.98)',
  surface: 'rgba(10, 16, 27, 0.72)',
  'surface-strong': 'rgba(14, 20, 34, 0.92)',
  'surface-soft': 'rgba(255, 255, 255, 0.06)',
  accent: '#dce9ff',
  'accent-soft': 'rgba(173, 198, 255, 0.18)',
  'shadow-tint': 'rgba(3, 6, 12, 0.46)',
  'success-pill-bg': 'rgba(222, 233, 255, 0.16)',
  'success-pill-ink': '#f4f7ff',
};

export const STOP_DAEMON_LABEL = 'Stop daemon';

export const PLACEHOLDER_ARTWORK = '/assets/agentune-mark.svg';
```

## File: `public/dashboard/dom.js`
```javascript
function getElement(selector) {
  const element = document.querySelector(selector);
  if (!element) {
    throw new Error(`Missing element for selector: ${selector}`);
  }
  return element;
}

export const elements = {
  activityChart: getElement('[data-activity-chart]'),
  artist: getElement('[data-artist]'),
  art: getElement('[data-art]'),
  databaseActions: Array.from(document.querySelectorAll('[data-db-action]')),
  databaseMessage: getElement('[data-db-message]'),
  databasePath: getElement('[data-db-path]'),
  databasePlays: getElement('[data-db-plays]'),
  databaseProviderCache: getElement('[data-db-cache]'),
  databaseTracks: getElement('[data-db-tracks]'),
  durationFill: getElement('[data-duration-fill]'),
  elapsed: getElement('[data-elapsed]'),
  insightPlays: getElement('[data-insight-plays]'),
  insightTracks: getElement('[data-insight-tracks]'),
  navButtons: Array.from(document.querySelectorAll('[data-nav]')),
  next: getElement('[data-next]'),
  pause: getElement('[data-pause]'),
  personaMessage: getElement('[data-message]'),
  queue: getElement('[data-queue]'),
  queueArt: getElement('[data-queue-art]'),
  queueCurrentArtist: getElement('[data-queue-current-artist]'),
  queueCurrentTitle: getElement('[data-queue-current-title]'),
  saveTaste: getElement('[data-save-taste]'),
  sharedControls: getElement('[data-shared-controls]'),
  stopDaemon: getElement('[data-stop-daemon]'),
  taste: getElement('[data-taste]'),
  title: getElement('[data-title]'),
  topArtists: getElement('[data-top-artists]'),
  topKeywords: getElement('[data-top-keywords]'),
  totalDuration: getElement('[data-total-duration]'),
  viewPanels: Array.from(document.querySelectorAll('[data-view]')),
  volume: getElement('[data-volume]'),
};
```

## File: `public/dashboard/insights.js`
```javascript
import { elements } from './dom.js';
import { renderActivityChart as renderDashboardActivityChart } from './activity-chart.js';

export function renderInsights(stats) {
  elements.insightPlays.textContent = String(stats.insights.plays7d);
  elements.insightTracks.textContent = String(stats.insights.tracks7d);

  renderDashboardActivityChart(elements.activityChart, stats.insights.activity7d);
  renderTopArtists(stats.insights.topArtists.slice(0, 3));
  renderTopKeywords(stats.insights.topKeywords);
}

function renderTopArtists(topArtists) {
  elements.topArtists.replaceChildren();

  if (topArtists.length === 0) {
    elements.topArtists.append(createEmptyState('li', 'No artists.'));
    return;
  }

  topArtists.forEach((artist, index) => {
    const item = document.createElement('li');
    const indexValue = document.createElement('span');
    const copy = document.createElement('div');
    const title = document.createElement('strong');
    const meta = document.createElement('span');

    item.className = 'rank-item rank-item-minimal';
    indexValue.className = 'rank-index';
    copy.className = 'rank-copy';
    title.className = 'rank-title';
    meta.className = 'rank-meta';

    indexValue.textContent = String(index + 1).padStart(2, '0');
    title.textContent = artist.artist;
    meta.textContent = String(artist.plays);

    copy.append(title, meta);
    item.append(indexValue, copy);
    elements.topArtists.append(item);
  });
}

function renderTopKeywords(topKeywords) {
  elements.topKeywords.replaceChildren();

  if (topKeywords.length === 0) {
    elements.topKeywords.append(createEmptyState('li', 'No tags.'));
    return;
  }

  topKeywords.forEach((keyword) => {
    const item = document.createElement('li');
    const label = document.createElement('span');

    item.className = 'keyword-chip keyword-chip-minimal';
    label.className = 'keyword-label';

    label.textContent = keyword.keyword;

    item.append(label);
    elements.topKeywords.append(item);
  });
}

function createEmptyState(tagName, message) {
  const item = document.createElement(tagName);
  item.className = 'insight-empty';
  item.textContent = message;
  return item;
}
```

## File: `public/dashboard/marquee.js`
```javascript
function createStructure(titleElement) {
  const initialText = titleElement.textContent ?? '';
  titleElement.textContent = '';

  const viewport = document.createElement('span');
  viewport.className = 'track-title-viewport';

  const track = document.createElement('span');
  track.className = 'track-title-track';

  const primary = document.createElement('span');
  primary.className = 'track-title-copy primary';

  const secondary = document.createElement('span');
  secondary.className = 'track-title-copy secondary';
  secondary.setAttribute('aria-hidden', 'true');
  secondary.hidden = true;

  track.append(primary, secondary);
  viewport.append(track);
  titleElement.append(viewport);

  primary.textContent = initialText;

  return { primary, secondary, track, viewport };
}

export function createTitleMarquee(elements) {
  let animationFrame = 0;
  const { primary, secondary, track, viewport } = createStructure(elements.title);
  const resizeObserver = new ResizeObserver(() => queueMeasure());

  resizeObserver.observe(elements.title);
  resizeObserver.observe(viewport);
  window.addEventListener('resize', queueMeasure);

  function reset() {
    elements.title.classList.remove('is-long');
    secondary.hidden = true;
    secondary.textContent = '';
    track.style.removeProperty('--title-gap');
    track.style.removeProperty('--title-distance');
    track.style.removeProperty('--title-duration');
  }

  function queueMeasure() {
    window.cancelAnimationFrame(animationFrame);
    animationFrame = window.requestAnimationFrame(measure);
  }

  function measure() {
    const text = primary.textContent ?? '';
    const viewportWidth = viewport.clientWidth;
    const textWidth = primary.scrollWidth;

    if (!text || textWidth <= viewportWidth + 6) {
      reset();
      return;
    }

    const gap = Math.max(32, Math.round(viewportWidth * 0.16));
    const distance = textWidth + gap;
    const duration = Math.max(distance / 18, 14);

    secondary.hidden = false;
    secondary.textContent = text;
    track.style.setProperty('--title-gap', `${gap}px`);
    track.style.setProperty('--title-distance', `${distance}px`);
    track.style.setProperty('--title-duration', `${duration}s`);
    elements.title.classList.add('is-long');
  }

  return {
    destroy() {
      resizeObserver.disconnect();
      window.removeEventListener('resize', queueMeasure);
      window.cancelAnimationFrame(animationFrame);
    },
    refresh: queueMeasure,
    setText(text) {
      primary.textContent = text;
      elements.title.dataset.title = text;
      queueMeasure();
    },
  };
}
```

## File: `public/dashboard/playback-visual-state.js`
```javascript
export function resolvePlaybackVisualState(hasTrack, isPlaying) {
  if (!hasTrack) {
    return 'idle';
  }

  return isPlaying ? 'playing' : 'paused';
}

export function applyPlaybackVisualState(root, hasTrack, isPlaying) {
  root.dataset.playbackVisualState = resolvePlaybackVisualState(hasTrack, isPlaying);
}
```

## File: `public/dashboard/render.js`
```javascript
import { DATABASE_ACTION_LABELS, PLACEHOLDER_ARTWORK, STOP_DAEMON_LABEL } from './constants.js';
import { elements } from './dom.js';
import { renderInsights } from './insights.js';
import { createTitleMarquee } from './marquee.js';
import { applyPlaybackVisualState } from './playback-visual-state.js';
import { syncTasteTextareaHeight } from './taste-textarea.js';
import { buildArtworkUrl, createAmbientThemeManager } from './theme.js';
import { toggleHiddenAttribute } from './toggle-hidden-attribute.js';

const ambientTheme = createAmbientThemeManager();
const titleMarquee = createTitleMarquee(elements);

let lastArtwork = '';
let lastTitle = '';
let lastArtist = '';
const PLACEHOLDER_ARTWORK_URL = new URL(PLACEHOLDER_ARTWORK, window.location.href).href;

applyPlaybackVisualState(document.documentElement, false, false);

function formatPlaybackTime(seconds) {
  const totalSeconds = Math.max(0, Math.round(seconds));
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const remainingSeconds = totalSeconds % 60;

  if (hours > 0) {
    return `${hours}:${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
  }

  return `${minutes}:${String(remainingSeconds).padStart(2, '0')}`;
}

function setArtworkSource(image, source) {
  image.dataset.fallbackSource = source ?? '';
  image.dataset.fallbackTried = 'false';
  image.src = source ? buildArtworkUrl(source) : PLACEHOLDER_ARTWORK;
}

function renderQueueCurrent(title, artist) {
  elements.queueCurrentTitle.textContent = title;
  elements.queueCurrentArtist.textContent = artist;
}

function renderPlaybackProgress(position, duration) {
  const safePosition = Math.max(0, Math.round(position));
  const safeDuration = Math.max(safePosition, Math.round(duration));
  const progress = safeDuration > 0 ? Math.min(100, (safePosition / safeDuration) * 100) : 0;

  elements.durationFill.style.width = `${progress}%`;
  elements.elapsed.textContent = formatPlaybackTime(safePosition);
  elements.totalDuration.textContent = formatPlaybackTime(safeDuration);
}

function setPauseButtonState(hasTrack, isPlaying) {
  const pauseIcon = elements.pause.querySelector('.icon-pause');
  const playIcon = elements.pause.querySelector('.icon-play');
  const shouldShowPauseIcon = !hasTrack || isPlaying;
  const shouldShowPlayIcon = hasTrack && !isPlaying;
  const pauseLabel = hasTrack && !isPlaying ? 'Resume playback' : 'Pause playback';

  elements.pause.disabled = !hasTrack;
  elements.pause.setAttribute('aria-label', pauseLabel);

  if (pauseIcon instanceof SVGElement) {
    toggleHiddenAttribute(pauseIcon, !shouldShowPauseIcon);
  }
  if (playIcon instanceof SVGElement) {
    toggleHiddenAttribute(playIcon, !shouldShowPlayIcon);
  }
}

export function renderQueue(queue) {
  elements.queue.replaceChildren();
  if (queue.length === 0) {
    const emptyItem = document.createElement('li');
    emptyItem.className = 'queue-empty';
    emptyItem.textContent = 'Queue is empty';
    elements.queue.append(emptyItem);
    return;
  }

  queue.forEach((item, index) => {
    const listItem = document.createElement('li');
    const title = document.createElement('strong');
    const artist = document.createElement('span');

    title.textContent = item.title;
    artist.textContent = item.artist;
    listItem.append(title, artist);
    elements.queue.append(listItem);
  });
}

export function renderState(state) {
  const title = state.title ?? 'Nothing playing';
  const artist = state.artist ?? 'Ask your agent to start a track';
  const hasTrack = state.title !== null;

  if (title !== lastTitle) {
    titleMarquee.setText(title);
    renderQueueCurrent(title, artist);
    lastTitle = title;
  }

  if (artist !== lastArtist) {
    elements.artist.textContent = artist;
    elements.queueCurrentArtist.textContent = artist;
    lastArtist = artist;
  }

  if (state.thumbnail !== lastArtwork) {
    setArtworkSource(elements.art, state.thumbnail);
    setArtworkSource(elements.queueArt, state.thumbnail);
    void ambientTheme.sync(state.thumbnail);
    lastArtwork = state.thumbnail;
  }

  elements.volume.value = String(state.volume);
  elements.volume.style.setProperty('--volume-progress', `${state.volume}%`);
  renderPlaybackProgress(state.position, state.duration);
  elements.next.disabled = state.queue.length === 0;
  applyPlaybackVisualState(document.documentElement, hasTrack, state.playing);
  setPauseButtonState(hasTrack, state.playing);
  renderQueue(state.queue);
}

export function renderPersona(data) {
  if (data.taste !== undefined && document.activeElement !== elements.taste) {
    elements.taste.value = data.taste;
    syncTasteTextareaHeight(elements.taste);
  }
}

export function renderDatabaseStats(stats) {
  elements.databasePath.textContent = stats.dbPath;
  elements.databasePlays.textContent = String(stats.counts.plays);
  elements.databaseTracks.textContent = String(stats.counts.tracks);
  elements.databaseProviderCache.textContent = String(stats.counts.providerCache);
  renderInsights(stats);
}

export function resetDangerActionLabels() {
  elements.databaseActions.forEach((button) => {
    button.classList.remove('is-armed');
    button.textContent = DATABASE_ACTION_LABELS[button.dataset.dbAction];
  });
  elements.stopDaemon.classList.remove('is-armed');
  elements.stopDaemon.textContent = STOP_DAEMON_LABEL;
}

export function setDangerActionArmed(button, text) {
  button.classList.add('is-armed');
  button.textContent = text;
}

export function setActiveView(view) {
  elements.navButtons.forEach((button) => {
    const isActive = button.dataset.nav === view;
    button.classList.toggle('is-active', isActive);
    button.setAttribute('aria-pressed', isActive ? 'true' : 'false');
  });

  elements.viewPanels.forEach((panel) => {
    panel.hidden = panel.dataset.view !== view;
  });
  elements.sharedControls.hidden = view === 'settings';

  if (view === 'settings') {
    window.requestAnimationFrame(() => {
      syncTasteTextareaHeight(elements.taste);
    });
  }

  titleMarquee.refresh();
}

export function showDatabaseMessage(message, isError = false) {
  elements.databaseMessage.textContent = message;
  elements.databaseMessage.classList.toggle('is-error', isError);
}

export function showPersonaMessage(message, isError = false) {
  elements.personaMessage.textContent = message;
  elements.personaMessage.classList.toggle('is-error', isError);
}

export function applyStoppedState(message) {
  elements.pause.disabled = true;
  elements.next.disabled = true;
  elements.volume.disabled = true;
  elements.taste.disabled = true;
  elements.saveTaste.disabled = true;
  elements.stopDaemon.disabled = true;
  elements.databaseActions.forEach((button) => {
    button.disabled = true;
  });

  titleMarquee.setText('Daemon stopped');
  elements.artist.textContent = 'Run "agentune start", or open a new coding session if auto-start is enabled.';
  renderQueueCurrent('Daemon stopped', 'Run "agentune start" to bring playback back online.');
  elements.volume.value = '0';
  elements.volume.style.setProperty('--volume-progress', '0%');
  renderPlaybackProgress(0, 0);
  applyPlaybackVisualState(document.documentElement, false, false);
  setPauseButtonState(false, false);
  elements.queue.replaceChildren();

  const stoppedItem = document.createElement('li');
  stoppedItem.className = 'queue-empty';
  stoppedItem.textContent = 'Daemon is stopped';
  elements.queue.append(stoppedItem);

  showDatabaseMessage(message);
  showPersonaMessage('Daemon stopped. This page will stay offline until agentune starts again.');
}

export function applySessionExpiredState(message) {
  elements.pause.disabled = true;
  elements.next.disabled = true;
  elements.volume.disabled = true;
  elements.taste.disabled = true;
  elements.saveTaste.disabled = true;
  elements.stopDaemon.disabled = true;
  elements.databaseActions.forEach((button) => {
    button.disabled = true;
  });

  showDatabaseMessage(message, true);
  showPersonaMessage(message, true);
}

function attachArtworkFallback(image) {
  image.addEventListener('error', () => {
    const fallbackSource = image.dataset.fallbackSource ?? '';
    const fallbackTried = image.dataset.fallbackTried === 'true';
    const currentSource = image.currentSrc || image.src;

    if (fallbackSource && !fallbackTried) {
      image.dataset.fallbackTried = 'true';
      image.src = fallbackSource;
      return;
    }

    if (currentSource !== PLACEHOLDER_ARTWORK_URL) {
      image.src = PLACEHOLDER_ARTWORK;
    }
  });
}

attachArtworkFallback(elements.art);
attachArtworkFallback(elements.queueArt);
```

## File: `public/dashboard/settings-api.js`
```javascript
import { dashboardFetch } from './auth.js';

export async function fetchDatabaseStats() {
  const response = await dashboardFetch('/api/database/stats');
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message ?? 'Failed to load database stats.');
  }
  return data.stats;
}

export async function postDatabaseAction(actionId) {
  const response = await dashboardFetch(`/api/database/${actionId}`, { method: 'POST' });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message ?? 'Database cleanup failed.');
  }
  return data;
}

export async function savePersonaTaste(taste) {
  const response = await dashboardFetch('/api/persona', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ taste }),
  });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message ?? 'Persona save failed.');
  }
  return data;
}

export async function requestDaemonStop() {
  const response = await dashboardFetch('/api/daemon/stop', { method: 'POST' });
  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.message ?? 'Daemon stop failed.');
  }
  return data;
}
```

## File: `public/dashboard/taste-textarea.js`
```javascript
export function syncTasteTextareaHeight(textarea) {
  textarea.style.height = '0px';
  textarea.style.height = `${textarea.scrollHeight}px`;
}
```

## File: `public/dashboard/theme.js`
```javascript
import { appendDashboardTokenToPath } from './auth.js';
import { DEFAULT_THEME, PLACEHOLDER_ARTWORK } from './constants.js';

const themeCache = new Map();

function clampChannel(value) {
  return Math.max(0, Math.min(255, Math.round(value)));
}

function rgba(color, alpha) {
  return `rgba(${color.r}, ${color.g}, ${color.b}, ${alpha})`;
}

function mix(a, b, ratio) {
  return {
    r: clampChannel(a.r + (b.r - a.r) * ratio),
    g: clampChannel(a.g + (b.g - a.g) * ratio),
    b: clampChannel(a.b + (b.b - a.b) * ratio),
  };
}

function getSaturation({ r, g, b }) {
  const max = Math.max(r, g, b);
  const min = Math.min(r, g, b);
  return max === 0 ? 0 : (max - min) / max;
}

function getLuminance({ r, g, b }) {
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

function buildThemeFromSamples({ average, deepest, highlight, accent }) {
  const baseShadow = mix(deepest, average, 0.18);
  const shellFill = mix(deepest, highlight, 0.16);
  const shellSoft = mix(average, highlight, 0.1);
  const accentLine = mix(accent, highlight, 0.36);

  return {
    'ambient-start': rgba(mix(deepest, accent, 0.24), 0.97),
    'ambient-mid': rgba(mix(average, accent, 0.3), 0.7),
    'ambient-end': rgba(mix(deepest, { r: 4, g: 7, b: 13 }, 0.55), 0.99),
    surface: rgba(shellFill, 0.78),
    'surface-strong': rgba(mix(deepest, average, 0.2), 0.92),
    'surface-soft': rgba(shellSoft, 0.22),
    accent: rgba(accentLine, 1),
    'accent-soft': rgba(accent, 0.22),
    'shadow-tint': rgba(baseShadow, 0.52),
    'success-pill-bg': rgba(mix(accent, highlight, 0.3), 0.18),
    'success-pill-ink': 'rgba(244, 247, 255, 0.96)',
  };
}

function sampleArtworkPalette(imageData) {
  const fallback = {
    average: { r: 18, g: 28, b: 44 },
    deepest: { r: 10, g: 14, b: 22 },
    highlight: { r: 212, g: 228, b: 255 },
    accent: { r: 128, g: 168, b: 240 },
  };

  const { data } = imageData;
  let weightSum = 0;
  let sumR = 0;
  let sumG = 0;
  let sumB = 0;
  let deepest = fallback.deepest;
  let highlight = fallback.highlight;
  let accent = fallback.accent;
  let bestAccentScore = -1;
  let darkestScore = Infinity;
  let brightestScore = -1;

  for (let index = 0; index < data.length; index += 16) {
    const alpha = data[index + 3];
    if (alpha < 120) {
      continue;
    }

    const color = { r: data[index], g: data[index + 1], b: data[index + 2] };
    const luminance = getLuminance(color);
    const saturation = getSaturation(color);
    const weight = 0.35 + saturation;

    weightSum += weight;
    sumR += color.r * weight;
    sumG += color.g * weight;
    sumB += color.b * weight;

    if (luminance < darkestScore) {
      darkestScore = luminance;
      deepest = color;
    }

    if (luminance > brightestScore) {
      brightestScore = luminance;
      highlight = color;
    }

    const accentScore = saturation * 0.7 + Math.max(0, 1 - Math.abs(luminance - 150) / 150) * 0.3;
    if (accentScore > bestAccentScore) {
      bestAccentScore = accentScore;
      accent = color;
    }
  }

  if (weightSum === 0) {
    return fallback;
  }

  return {
    average: {
      r: clampChannel(sumR / weightSum),
      g: clampChannel(sumG / weightSum),
      b: clampChannel(sumB / weightSum),
    },
    deepest,
    highlight,
    accent,
  };
}

async function loadArtwork(url) {
  const image = new Image();
  // Required for canvas pixel reads when we fall back to a remote thumbnail URL.
  image.crossOrigin = 'anonymous';
  image.decoding = 'async';
  image.referrerPolicy = 'no-referrer';

  await new Promise((resolve, reject) => {
    image.onload = resolve;
    image.onerror = () => reject(new Error('Artwork load failed.'));
    image.src = url;
  });

  return image;
}

async function extractTheme(url) {
  const image = await loadArtwork(url);
  const canvas = document.createElement('canvas');
  canvas.width = 36;
  canvas.height = 36;
  const context = canvas.getContext('2d', { willReadFrequently: true });

  if (!context) {
    throw new Error('Canvas unavailable.');
  }

  context.drawImage(image, 0, 0, canvas.width, canvas.height);
  const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
  return buildThemeFromSamples(sampleArtworkPalette(imageData));
}

async function extractThemeWithFallback(source) {
  const candidates = [buildArtworkUrl(source), source];
  let lastError = new Error('Artwork load failed.');

  for (const candidate of candidates) {
    try {
      const theme = await extractTheme(candidate);
      themeCache.set(candidate, theme);
      return theme;
    } catch (error) {
      lastError = error instanceof Error ? error : new Error('Artwork load failed.');
    }
  }

  throw lastError;
}

export function buildArtworkUrl(source) {
  return source
    ? appendDashboardTokenToPath(`/api/artwork?src=${encodeURIComponent(source)}`)
    : PLACEHOLDER_ARTWORK;
}

export function createAmbientThemeManager(root = document.documentElement) {
  let activeArtwork = '';
  let requestToken = 0;

  function applyTheme(theme) {
    Object.entries(theme).forEach(([key, value]) => {
      root.style.setProperty(`--${key}`, value);
    });
  }

  async function sync(source) {
    if (!source) {
      activeArtwork = '';
      requestToken += 1;
      applyTheme(DEFAULT_THEME);
      return;
    }

    if (source === activeArtwork) {
      return;
    }

    activeArtwork = source;
    const token = ++requestToken;
    const proxied = buildArtworkUrl(source);
    const cached = themeCache.get(proxied) ?? themeCache.get(source);

    if (cached) {
      applyTheme(cached);
      return;
    }

    try {
      const theme = await extractThemeWithFallback(source);
      themeCache.set(proxied, theme);
      themeCache.set(source, theme);
      if (token === requestToken) {
        applyTheme(theme);
      }
    } catch {
      if (token === requestToken) {
        applyTheme(DEFAULT_THEME);
      }
    }
  }

  applyTheme(DEFAULT_THEME);
  return { sync };
}
```

## File: `public/dashboard/toggle-hidden-attribute.js`
```javascript
export function toggleHiddenAttribute(element, hidden) {
  if (typeof element?.toggleAttribute !== 'function') {
    return;
  }

  element.toggleAttribute('hidden', hidden);
}
```

## File: `public/styles/dashboard-settings.css`
```css
.view-panel[data-view="settings"] {
  width: 100%;
  align-items: stretch;
  text-align: left;
  gap: 0.85rem;
  padding-bottom: 0.75rem;
  scrollbar-width: none;
  -ms-overflow-style: none;
}

.view-panel[data-view="settings"]::-webkit-scrollbar {
  display: none;
}

.view-header-dashboard {
  padding-bottom: 0.65rem;
}

.view-header-dashboard .settings-header-line {
  margin: 0;
}

.settings-section-title {
  margin: 0;
  margin-top: 1.1rem;
  padding-top: 0;
}

.settings-section.settings-dashboard {
  display: grid;
  gap: 0.8rem;
}

.settings-card,
.advanced {
  border: 1px solid rgba(255, 255, 255, 0.06);
  background:
    linear-gradient(180deg, rgba(18, 26, 42, 0.8) 0%, rgba(10, 16, 27, 0.74) 100%);
  box-shadow:
    inset 0 0 0 1px rgba(255, 255, 255, 0.04),
    0 18px 42px var(--shadow-tint);
  backdrop-filter: blur(18px);
}

.settings-card {
  padding: 1rem 1.05rem;
  display: grid;
  gap: 0.8rem;
}

.settings-card.taste-card,
.advanced {
  border: none;
  background: transparent;
  box-shadow: none;
  backdrop-filter: none;
}

.settings-card.taste-card {
  padding: 0;
}

.settings-card-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 0.8rem;
}

.settings-card-head h3 {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.settings-card-head-compact {
  align-items: center;
}

.insights-chart-card {
  gap: 0.55rem;
  padding: 0;
  border: none;
  background: transparent;
  box-shadow: none;
  backdrop-filter: none;
}

.activity-chart {
  min-height: 9.9rem;
}

.activity-line-shell {
  display: grid;
  gap: 0.55rem;
}

.activity-line-stage {
  position: relative;
  height: 9.2rem;
}

.activity-line-svg {
  width: 100%;
  height: 9.2rem;
  overflow: visible;
  display: block;
}

.activity-line-area {
  opacity: 1;
}

.activity-line-stroke {
  fill: none;
  stroke: rgba(255, 255, 255, 0.96);
  stroke-width: 3;
  stroke-linecap: round;
  stroke-linejoin: round;
  filter: drop-shadow(0 10px 24px rgba(255, 255, 255, 0.16));
}

.activity-line-point {
  fill: rgba(255, 255, 255, 0.9);
  stroke: none;
  stroke-width: 0;
}

.activity-line-point.is-last {
  fill: rgba(255, 255, 255, 1);
}

.activity-line-point.is-active {
  fill: rgba(255, 255, 255, 1);
  filter: drop-shadow(0 0 7px rgba(255, 255, 255, 0.42));
}

.activity-line-target {
  position: absolute;
  width: 1.9rem;
  height: 1.9rem;
  padding: 0;
  border: none;
  border-radius: 999px;
  background: transparent;
  transform: translate(-50%, -50%);
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.activity-line-target:focus-visible {
  outline: none;
}

.activity-line-tooltip {
  position: absolute;
  left: var(--tooltip-left, 50%);
  top: var(--tooltip-top, 50%);
  min-width: 0;
  padding: 0;
  border-radius: 0;
  background: transparent;
  color: var(--ink);
  font-size: 0.78rem;
  font-weight: 600;
  line-height: 1;
  text-align: center;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transform: translate(-50%, calc(-100% - 0.55rem));
  transition: opacity 160ms ease;
}

.activity-line-tooltip.is-visible {
  opacity: 1;
}

.activity-line-labels {
  display: grid;
  grid-template-columns: repeat(7, minmax(0, 1fr));
  gap: 0.35rem;
}

.activity-line-label {
  font-size: 0.72rem;
  color: var(--ink-muted);
  text-align: center;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  grid-template-areas:
    'plays tracks artists'
    'tags tags artists';
  gap: 0.8rem;
}

.dashboard-metric-card {
  padding: 0;
  border: none;
  background: transparent;
  box-shadow: none;
  backdrop-filter: none;
}

.dashboard-plays-card {
  grid-area: plays;
}

.dashboard-tracks-card {
  grid-area: tracks;
}

.dashboard-artists-card {
  grid-area: artists;
  padding: 0;
  border: none;
  background: transparent;
  box-shadow: none;
  backdrop-filter: none;
  align-content: start;
}

.dashboard-tags-card {
  grid-area: tags;
  padding: 0;
  border: none;
  background: transparent;
  box-shadow: none;
  backdrop-filter: none;
}

.dashboard-artists-card .settings-card-head h3,
.dashboard-tags-card .settings-card-head h3 {
  color: var(--ink-muted);
}

.dashboard-tags-card .settings-card-head,
.dashboard-tags-card .settings-card-head h3 {
  color: var(--ink-muted) !important;
}

.insight-card {
  min-height: 5.25rem;
  padding: 0.8rem 0.85rem;
  border-radius: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.05);
  background:
    linear-gradient(180deg, rgba(255, 255, 255, 0.07) 0%, rgba(255, 255, 255, 0.025) 100%);
  display: grid;
  gap: 0.2rem;
  align-content: start;
}

.dashboard-metric-card .insight-card {
  padding: 0;
  border: none;
  border-radius: 0;
  background: transparent;
  box-shadow: none;
  justify-items: center;
  align-content: center;
  text-align: center;
}

.insight-card-compact {
  min-height: 4.65rem;
}

.insight-label,
.insight-empty,
.rank-meta,
.summary-sub,
.message,
.help-text,
.stat span {
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--ink-muted);
}

.insight-value {
  font-family: var(--font-display);
  font-size: 1.7rem;
  font-weight: 600;
  letter-spacing: -0.04em;
}

.rank-list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.72rem;
}

.rank-item-minimal {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  grid-template-areas: 'index copy';
  column-gap: 0.75rem;
  row-gap: 0;
  align-items: baseline;
}

.rank-index {
  grid-area: index;
  font-family: var(--font-display);
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: rgba(255, 255, 255, 0.34);
  align-self: start;
}

.rank-copy {
  grid-area: copy;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.55rem;
}

.rank-title {
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1.3;
}

.keyword-list {
  margin: 0;
  padding: 0;
  list-style: none;
}

.keyword-list-minimal {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  gap: 0.5rem;
  max-height: calc((0.84rem * 1.35 * 2) + 0.5rem);
  overflow: hidden;
}

.keyword-chip-minimal {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  border-radius: 0;
  background: transparent;
  border: none;
}

.keyword-label {
  font-size: 0.84rem;
  line-height: 1.35;
  color: var(--ink);
}

.insight-empty {
  padding: 0.7rem 0;
}

.taste-card textarea {
  width: 100%;
  min-height: 0;
  height: auto;
  padding: 0;
  border: none;
  border-radius: 0;
  background: transparent;
  color: var(--ink);
  font-family: inherit;
  font-size: 0.95rem;
  line-height: 1.55;
  overflow: hidden;
  resize: none;
}

.taste-card textarea:focus {
  outline: none;
}

.primary-btn {
  padding: 0.62rem 1.4rem;
  border: none;
  border-radius: 999px;
  background: var(--accent);
  color: var(--ambient-end);
  font-family: inherit;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
}

.taste-save-btn {
  width: 2.4rem;
  height: 2.4rem;
  padding: 0;
  display: grid;
  place-items: center;
  justify-self: center;
  margin-inline: auto;
  border: 1.9px solid rgba(255, 255, 255, 0.38);
  background: transparent;
  color: rgba(255, 255, 255, 0.5);
}

.taste-save-btn svg {
  width: 1rem;
  height: 1rem;
}

.message {
  margin: 0;
  min-height: 1.2em;
  text-align: center;
}

.message.is-error {
  color: var(--danger);
}

.advanced {
  margin-top: 0;
}

.advanced summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0;
  cursor: pointer;
  list-style: none;
}

.advanced summary span:first-child {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.advanced summary::-webkit-details-marker {
  display: none;
}

.advanced-content {
  padding: 0.85rem 0 0;
  display: grid;
  gap: 0.85rem;
}

.db-stats {
  display: grid;
  gap: 0.7rem;
}

.stat {
  display: flex;
  justify-content: space-between;
  gap: 0.8rem;
  font-size: 0.84rem;
}

.stat code {
  font-family: 'SF Mono', Consolas, monospace;
  font-size: 0.74rem;
  max-width: 180px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.danger-zone {
  display: grid;
  gap: 0.9rem;
}

.btn-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.btn-row-advanced {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.7rem;
}

.danger-btn {
  min-height: 3rem;
  padding: 0.82rem 1rem;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 1.15rem;
  background: transparent;
  color: var(--ink);
  font-family: inherit;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.01em;
  cursor: pointer;
  text-align: left;
  transition: none;
}

.danger-btn:focus-visible {
  outline: 2px solid rgba(255, 255, 255, 0.34);
  outline-offset: 2px;
}

.danger-btn.hard {
  border-color: rgba(255, 107, 107, 0.26);
  background: transparent;
  color: rgba(255, 188, 188, 0.98);
}

@media (max-width: 420px) {
  .activity-line-svg {
    height: 8.25rem;
  }

  .activity-line-labels {
    gap: 0.18rem;
  }

  .settings-card,
  .advanced summary,
  .advanced-content {
    padding-left: 0.95rem;
    padding-right: 0.95rem;
  }

  .btn-row-advanced {
    grid-template-columns: 1fr;
  }
}
```

## File: `scripts/publish-utils.mjs`
```
import { execFileSync, spawnSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

export const ROOT_DIR = process.cwd();
export const NPM = process.platform === 'win32' ? 'npm.cmd' : 'npm';

export function ensure(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

export function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

export function readPackageJson(cwd = ROOT_DIR) {
  return readJson(path.join(cwd, 'package.json'));
}

function resolveCommand(command, args) {
  if (process.platform === 'win32' && /\.cmd$/iu.test(command)) {
    return {
      command: 'cmd.exe',
      args: ['/d', '/s', '/c', command, ...args],
    };
  }

  return { command, args };
}

export function run(command, args, options = {}) {
  const resolved = resolveCommand(command, args);
  execFileSync(resolved.command, resolved.args, {
    cwd: options.cwd ?? ROOT_DIR,
    env: { ...process.env, ...(options.env ?? {}) },
    stdio: 'inherit',
  });
}

export function runText(command, args, options = {}) {
  try {
    const resolved = resolveCommand(command, args);
    return execFileSync(resolved.command, resolved.args, {
      cwd: options.cwd ?? ROOT_DIR,
      env: { ...process.env, ...(options.env ?? {}) },
      encoding: 'utf8',
    }).trim();
  } catch (error) {
    const stdout = error.stdout ? String(error.stdout).trim() : '';
    const stderr = error.stderr ? String(error.stderr).trim() : '';
    const details = [stdout, stderr].filter(Boolean).join('\n');
    throw new Error(details ? `${error.message}\n${details}` : error.message);
  }
}

export function runResult(command, args, options = {}) {
  const resolved = resolveCommand(command, args);
  return spawnSync(resolved.command, resolved.args, {
    cwd: options.cwd ?? ROOT_DIR,
    env: { ...process.env, ...(options.env ?? {}) },
    encoding: 'utf8',
    timeout: options.timeout ?? 0,
  });
}

export function parseJsonOutput(output) {
  const arrayStart = output.indexOf('[');
  const objectStart = output.indexOf('{');
  const startIndexes = [arrayStart, objectStart].filter((index) => index >= 0);
  ensure(startIndexes.length > 0, `Expected JSON output but received:\n${output}`);
  const start = Math.min(...startIndexes);
  const end = Math.max(output.lastIndexOf(']'), output.lastIndexOf('}'));
  ensure(end >= start, `Expected JSON output but received:\n${output}`);
  return JSON.parse(output.slice(start, end + 1));
}

export function removeDir(directoryPath) {
  fs.rmSync(directoryPath, { recursive: true, force: true });
}
```

## File: `scripts/release.mjs`
```
import process from 'node:process';
import { NPM, ensure, run, runText } from './publish-utils.mjs';

const mode = process.argv[2];
const args = process.argv.slice(3);
const ALLOWED_BUMPS = {
  alpha: new Set(['prerelease', 'prepatch', 'preminor', 'premajor']),
  stable: new Set(['patch', 'minor', 'major']),
};

function parseBump(argv) {
  const bumpFlagIndex = argv.indexOf('--bump');
  ensure(bumpFlagIndex >= 0, 'Release command requires --bump <value>.');
  const bump = argv[bumpFlagIndex + 1];
  ensure(Boolean(bump), 'Release command requires --bump <value>.');
  return bump;
}

function getBranchName() {
  return runText('git', ['branch', '--show-current']);
}

function ensureRemoteBranchIsSynced(branch) {
  run('git', ['fetch', 'origin', '--tags']);

  try {
    runText('git', ['rev-parse', '--verify', `origin/${branch}`]);
  } catch {
    throw new Error(`Remote branch origin/${branch} does not exist. Push the branch before releasing.`);
  }

  const [behindText, aheadText] = runText('git', ['rev-list', '--left-right', '--count', `origin/${branch}...HEAD`])
    .split(/\s+/u);
  const behind = Number(behindText);
  const ahead = Number(aheadText);

  ensure(Number.isFinite(behind) && Number.isFinite(ahead), 'Could not determine branch sync status.');
  ensure(
    behind === 0 && ahead === 0,
    `Branch ${branch} must match origin/${branch} before release (behind=${behind}, ahead=${ahead}).`,
  );
}

function bumpVersion(currentMode, bump) {
  const versionArgs = ['version', bump];

  if (currentMode === 'alpha') {
    versionArgs.push('--preid', 'alpha');
  }

  versionArgs.push('--message', 'chore(release): %s');
  const versionTag = runText(NPM, versionArgs).split(/\r?\n/u).filter(Boolean).at(-1);

  ensure(Boolean(versionTag) && versionTag.startsWith('v'), 'npm version did not return a git tag.');
  return { tag: versionTag, version: versionTag.slice(1) };
}

function publishRelease(currentMode) {
  const publishArgs = ['publish', '--access', 'public'];
  if (currentMode === 'alpha') {
    publishArgs.splice(1, 0, '--tag', 'alpha');
  }

  run(NPM, publishArgs, { env: { AGENTUNE_RELEASE_MODE: currentMode } });
}

const bump = parseBump(args);
ensure(mode in ALLOWED_BUMPS, 'Release mode must be "alpha" or "stable".');
ensure(ALLOWED_BUMPS[mode].has(bump), `Unsupported ${mode} bump "${bump}".`);

const releaseState = {
  branch: '',
  mode,
  bump,
  stage: 'initialization',
  tag: '',
};

try {
  releaseState.stage = 'npm login check';
  runText(NPM, ['whoami']);

  releaseState.stage = 'git cleanliness check';
  ensure(runText('git', ['status', '--porcelain']) === '', 'Git working tree must be clean before release.');

  releaseState.stage = 'branch policy check';
  releaseState.branch = getBranchName();
  if (mode === 'stable') {
    ensure(releaseState.branch === 'main', 'Stable releases are only allowed from main.');
  }
  ensureRemoteBranchIsSynced(releaseState.branch);

  releaseState.stage = 'publish verification';
  run(NPM, ['run', 'verify:publish']);

  releaseState.stage = 'version bump';
  const { tag, version } = bumpVersion(mode, bump);
  releaseState.tag = tag;
  console.error(`[agentune] Prepared release ${version}.`);

  releaseState.stage = 'git push';
  run('git', ['push', 'origin', `HEAD:${releaseState.branch}`]);
  run('git', ['push', 'origin', releaseState.tag]);

  releaseState.stage = 'npm publish';
  publishRelease(mode);

  console.error(
    `[agentune] Release ${releaseState.tag} published to npm dist-tag ${mode === 'alpha' ? 'alpha' : 'latest'}.`,
  );
} catch (error) {
  console.error(`[agentune] Release failed during ${releaseState.stage}: ${(error).message}`);

  if (releaseState.tag) {
    console.error('[agentune] Recovery notes:');

    if (releaseState.stage === 'version bump') {
      console.error(`- Local release commit/tag ${releaseState.tag} may already exist.`);
      console.error('- If you want to retry cleanly, inspect git log/tag state before creating another version.');
    } else if (releaseState.stage === 'git push') {
      console.error(`- Local release tag ${releaseState.tag} exists, but remote push may be partial.`);
      console.error('- Check origin branch/tag state before retrying the release command.');
    } else {
      console.error(`- Release tag ${releaseState.tag} was created and may already be on origin.`);
      console.error(`- Fix the publish issue, then retry npm publish for ${releaseState.tag} without bumping again.`);
    }
  }

  process.exit(1);
}
```

## File: `scripts/run-compiled-tests.mjs`
```
import { spawnSync } from 'node:child_process';
import { existsSync, readdirSync } from 'node:fs';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';

const ROOT_DIR = fileURLToPath(new URL('..', import.meta.url));
const DIST_DIR = path.join(ROOT_DIR, 'dist');

function collectCompiledTestFiles(directoryPath) {
  const testFiles = [];

  for (const entry of readdirSync(directoryPath, { withFileTypes: true })) {
    const entryPath = path.join(directoryPath, entry.name);

    if (entry.isDirectory()) {
      testFiles.push(...collectCompiledTestFiles(entryPath));
      continue;
    }

    if (entry.isFile() && entry.name.endsWith('.test.js')) {
      testFiles.push(entryPath);
    }
  }

  return testFiles;
}

if (!existsSync(DIST_DIR)) {
  console.error(`[agentune] Compiled test directory not found: ${DIST_DIR}`);
  process.exit(1);
}

const compiledTestFiles = collectCompiledTestFiles(DIST_DIR).sort((left, right) => {
  return left.localeCompare(right);
});

if (compiledTestFiles.length === 0) {
  console.error(`[agentune] No compiled test files found under ${DIST_DIR}`);
  process.exit(1);
}

const result = spawnSync(process.execPath, ['--test', ...compiledTestFiles], {
  stdio: 'inherit',
});

if (result.error) {
  throw result.error;
}

if (typeof result.status === 'number') {
  process.exit(result.status);
}

process.exit(1);
```

## File: `scripts/verify-publish.mjs`
```
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import process from 'node:process';
import { NPM, ROOT_DIR, ensure, parseJsonOutput, readPackageJson, removeDir, run, runResult, runText } from './publish-utils.mjs';

const PACKAGE_NAME = 'agentune';
const BIN_PATH = 'dist/index.js';
const REPOSITORY_URL = 'git+https://github.com/tqdat410/agentune.git';
const HOMEPAGE_URL = 'https://github.com/tqdat410/agentune#readme';
const BUGS_URL = 'https://github.com/tqdat410/agentune/issues';
const ALLOWED_ROOT_FILES = new Set(['README.md', 'LICENSE', 'package.json']);
const ALLOWED_INSTALL_DEPRECATION_WARNINGS = [
  /npm warn deprecated prebuild-install@/iu,
];

function validateMetadata(pkg) {
  ensure(pkg.name === PACKAGE_NAME, `package.json name must be "${PACKAGE_NAME}".`);
  ensure(!('main' in pkg), 'CLI-only package must not declare a "main" entry.');
  ensure(pkg.type === 'module', 'package.json type must stay "module".');
  ensure(pkg.bin?.agentune === BIN_PATH, `package.json bin.agentune must be "${BIN_PATH}".`);
  ensure(pkg.engines?.node === '>=20', 'package.json engines.node must be ">=20".');
  ensure(pkg.publishConfig?.access === 'public', 'package.json publishConfig.access must be "public".');
  ensure(pkg.repository?.url === REPOSITORY_URL, 'package.json repository.url must point at the GitHub repo.');
  ensure(pkg.homepage === HOMEPAGE_URL, 'package.json homepage must point at the repo README.');
  ensure(pkg.bugs?.url === BUGS_URL, 'package.json bugs.url must point at the repo issues page.');
  ensure(pkg.license === 'MIT', 'package.json license must stay "MIT".');
}

function validatePackedFiles(files) {
  const violations = [];

  for (const file of files) {
    const normalizedPath = String(file.path).replace(/\\/g, '/');
    const allowedRootFile = ALLOWED_ROOT_FILES.has(normalizedPath);
    const allowedPrefix = normalizedPath.startsWith('dist/') || normalizedPath.startsWith('public/');

    if (!allowedRootFile && !allowedPrefix) {
      violations.push(`${normalizedPath} (unexpected file outside CLI runtime surface)`);
      continue;
    }

    if (normalizedPath.endsWith('.map')) {
      violations.push(`${normalizedPath} (sourcemap)`);
    }

    if (/\.test\.(js|d\.ts)$/u.test(normalizedPath)) {
      violations.push(`${normalizedPath} (compiled test file)`);
    }

    if (/test-helper/i.test(normalizedPath)) {
      violations.push(`${normalizedPath} (test helper)`);
    }
  }

  ensure(violations.length === 0, `Tarball contains non-runtime files:\n- ${violations.join('\n- ')}`);
}

function verifyInstalledTarball(tarballPath) {
  const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), 'agentune-publish-'));
  const installDir = path.join(tempRoot, 'install');
  const dataDir = path.join(tempRoot, 'data');

  fs.mkdirSync(installDir, { recursive: true });
  fs.mkdirSync(dataDir, { recursive: true });

  try {
    run(NPM, ['init', '-y'], { cwd: installDir });
    const installResult = runResult(NPM, ['install', tarballPath], { cwd: installDir });
    const installOutput = `${installResult.stdout ?? ''}\n${installResult.stderr ?? ''}`.trim();

    if (installOutput) {
      console.error(installOutput);
    }

    ensure(
      installResult.status === 0,
      `Tarball install failed:\n${installOutput || '(no output)'}`,
    );
    assertExpectedInstallWarningsOnly(installOutput);

    const env = { AGENTUNE_DATA_DIR: dataDir };
    const installedEntry = path.join(installDir, 'node_modules', PACKAGE_NAME, BIN_PATH);
    const cliResult = runResult(process.execPath, [installedEntry, 'status'], {
      cwd: installDir,
      env,
      timeout: 5000,
    });
    const cliOutput = `${cliResult.stdout ?? ''}\n${cliResult.stderr ?? ''}`;

    ensure(
      cliResult.status === 1 && cliOutput.includes('Daemon is not running'),
      `Installed CLI smoke test failed:\n${cliOutput.trim() || '(no output)'}`,
    );

    const importScript = [
      `import('${PACKAGE_NAME}')`,
      '.then(() => {',
      "  console.error('Programmatic import unexpectedly succeeded');",
      '  process.exit(2);',
      '})',
      '.catch(() => process.exit(0));',
    ].join('');
    const importResult = runResult(process.execPath, ['-e', importScript], {
      cwd: installDir,
      env,
      timeout: 5000,
    });

    ensure(importResult.status === 0, 'Installed package unexpectedly exposed a root import entry.');
  } finally {
    removeDir(tempRoot);
  }
}

function assertExpectedInstallWarningsOnly(output) {
  const deprecationWarnings = output
    .split(/\r?\n/u)
    .map((line) => line.trim())
    .filter((line) => /^npm warn deprecated /iu.test(line));

  const unexpectedWarnings = deprecationWarnings.filter((line) => {
    return !ALLOWED_INSTALL_DEPRECATION_WARNINGS.some((pattern) => pattern.test(line));
  });

  ensure(
    unexpectedWarnings.length === 0,
    `Unexpected install deprecation warnings:\n${unexpectedWarnings.join('\n')}`,
  );
}

console.error('[agentune] Verifying publish metadata...');
const pkg = readPackageJson();
validateMetadata(pkg);
ensure(fs.existsSync(path.join(ROOT_DIR, 'LICENSE')), 'LICENSE file is required before publish.');

console.error('[agentune] Running build + test gate...');
run(NPM, ['test']);

console.error('[agentune] Inspecting packed contents...');
const dryRunOutput = runText(NPM, ['pack', '--json', '--dry-run']);
const dryRunEntries = parseJsonOutput(dryRunOutput);
const dryRunEntry = Array.isArray(dryRunEntries) ? dryRunEntries[0] : dryRunEntries;
ensure(Array.isArray(dryRunEntry?.files), 'npm pack --dry-run did not return a files list.');
validatePackedFiles(dryRunEntry.files);

console.error('[agentune] Installing tarball smoke test...');
const packDir = fs.mkdtempSync(path.join(os.tmpdir(), 'agentune-tarball-'));

try {
  const tarballName = runText(NPM, ['pack', '--pack-destination', packDir, '--quiet'])
    .split(/\r?\n/u)
    .filter(Boolean)
    .at(-1);

  ensure(Boolean(tarballName), 'npm pack did not emit a tarball name.');
  verifyInstalledTarball(path.join(packDir, tarballName));
} finally {
  removeDir(packDir);
}

console.error('[agentune] Publish verification passed.');
```

## File: `src/index.ts`
```typescript
#!/usr/bin/env node

// agentune — MCP music server entry point
// Bootstraps MCP server, audio engine, and web dashboard

import { createMpvController, getMpvController, waitForMpvStartupWarmup } from './audio/mpv-controller.js';
import { createYoutubeProvider } from './providers/youtube-provider.js';
import { createWebServer, getWebServer } from './web/web-server.js';
import { createQueueManager } from './queue/queue-manager.js';
import { createQueuePlaybackController, getQueuePlaybackController } from './queue/queue-playback-controller.js';
import { createHistoryStore, getHistoryStore } from './history/history-store.js';
import { createAppleSearchProvider } from './providers/apple-search-provider.js';
import { createTasteEngine } from './taste/taste-engine.js';
import { createDaemonControlToken } from './daemon/daemon-auth.js';
import { DaemonServer } from './daemon/daemon-server.js';
import { writePidFile, removePidFile } from './daemon/pid-manager.js';
import { loadRuntimeConfig } from './runtime/runtime-config.js';
import { readPackageMetadata } from './package-metadata.js';
import type { WebServerOptions } from './web/web-server.js';

// --- Shared bootstrap ---

async function bootstrapComponents(webServerOptions?: Pick<WebServerOptions, 'onStopDaemon'>) {
  const runtimeConfig = loadRuntimeConfig();

  // Initialize history store (SQLite) — non-fatal if it fails
  try {
    createHistoryStore();
  } catch (err) {
    console.error('[agentune] History DB unavailable:', (err as Error).message);
  }

  const store = getHistoryStore();
  if (store) {
    createTasteEngine(store);
    console.error('[agentune] Taste engine initialized.');
  }

  const queueManager = createQueueManager();
  const youtubeProvider = createYoutubeProvider();

  if (store) {
    const db = store.getDatabase();
    createAppleSearchProvider(db);
    console.error('[agentune] Discovery provider initialized (Apple).');
  }

  const mpv = createMpvController(runtimeConfig.defaultVolume);
  createQueuePlaybackController(mpv, queueManager, youtubeProvider);
  const webServer = createWebServer(mpv, queueManager, {
    ...webServerOptions,
    port: runtimeConfig.dashboardPort,
  });
  await webServer.waitUntilReady();

  try {
    mpv.init();
    // mpv needs a short IPC warmup before first playback so stop detection
    // can observe the initial idle-to-active transition reliably.
    await waitForMpvStartupWarmup();
  } catch (err) {
    console.error('[agentune] Audio engine unavailable:', (err as Error).message);
    console.error('[agentune] MCP tools will return errors until mpv is installed.');
  }

  return { mpv };
}

// --- Daemon mode ---

async function startDaemon() {
  console.error('[agentune] Starting in daemon mode...');
  const runtimeConfig = loadRuntimeConfig();
  const daemonControlToken = createDaemonControlToken();
  const daemonServer = new DaemonServer(runtimeConfig.daemonPort, daemonControlToken);
  let shutdownPromise: Promise<void> | null = null;

  async function daemonShutdown(reason: string) {
    if (shutdownPromise) {
      return await shutdownPromise;
    }

    shutdownPromise = (async () => {
      console.error(`[agentune] Daemon shutting down (${reason})...`);
      getQueuePlaybackController()?.clearForShutdown();

      await runShutdownStep('daemon server destroy', async () => {
        await daemonServer.destroy();
      });
      await runShutdownStep('web server destroy', async () => {
        await getWebServer()?.destroy();
      });
      await runShutdownStep('history store close', async () => {
        getHistoryStore()?.close();
      });
      await runShutdownStep('mpv destroy', async () => {
        getMpvController()?.destroy();
      });
      await runShutdownStep('pid file removal', async () => {
        removePidFile();
      });

      process.exit(0);
    })();

    return await shutdownPromise;
  }

  await bootstrapComponents({ onStopDaemon: daemonShutdown });
  daemonServer.setShutdownHandler(daemonShutdown);

  const port = await daemonServer.start();
  writePidFile(port, daemonControlToken);

  console.error(`[agentune] Daemon ready on http://127.0.0.1:${port}`);

  process.on('SIGINT', () => void daemonShutdown('SIGINT'));
  process.on('SIGTERM', () => void daemonShutdown('SIGTERM'));
}

async function runShutdownStep(step: string, action: () => Promise<void> | void): Promise<void> {
  try {
    await action();
  } catch (err) {
    console.error(`[agentune] Shutdown step failed (${step}):`, (err as Error).message);
  }
}

// --- Entry point ---

const args = process.argv.slice(2);
const firstArg = args[0];

if (firstArg === '--help' || firstArg === '-h' || firstArg === 'help') {
  printCliHelp();
} else if (firstArg === '--version' || firstArg === '-v' || firstArg === 'version') {
  printCliVersion();
} else if (args.includes('--daemon')) {
  startDaemon().catch((err) => { console.error('[agentune] Fatal:', err); process.exit(1); });
} else if (firstArg === 'status') {
  import('./cli/status-command.js').then(({ runStatus }) => runStatus()).then(() => process.exit());
} else if (firstArg === 'start') {
  import('./cli/start-command.js').then(({ runStart }) => runStart()).then(() => process.exit());
} else if (firstArg === 'stop') {
  import('./cli/stop-command.js').then(({ runStop }) => runStop()).then(() => process.exit());
} else if (firstArg === 'doctor') {
  import('./cli/doctor-command.js').then(({ runDoctor }) => runDoctor()).then((code) => process.exit(code));
} else {
  // Default: proxy mode — relay stdio↔HTTP and optionally auto-start daemon.
  startProxyMode().catch((err) => { console.error('[agentune] Fatal:', err); process.exit(1); });
}

function printCliHelp(): void {
  const metadata = readPackageMetadata();
  process.stdout.write(
    [
      'agentune',
      metadata.description,
      '',
      'Usage:',
      '  agentune                 Start MCP stdio proxy mode',
      '  agentune start           Start the daemon in the background',
      '  agentune doctor          Check runtime dependencies and daemon health',
      '  agentune stop            Stop the running daemon',
      '  agentune status          Show daemon status',
      '  agentune version         Print CLI version',
      '  agentune --help          Show this help',
      '  agentune --version       Print CLI version',
      '',
      'Notes:',
      '  - The dashboard is served from the configured dashboard port after the daemon is ready.',
      '  - In normal MCP use, your client launches `agentune` automatically.',
      '',
    ].join('\n'),
  );
}

function printCliVersion(): void {
  process.stdout.write(`${readPackageMetadata().version}\n`);
}

async function startProxyMode() {
  const { ensureDaemon } = await import('./proxy/daemon-launcher.js');
  const { startProxy } = await import('./proxy/stdio-proxy.js');
  const runtimeConfig = loadRuntimeConfig();

  const { controlToken, port } = await ensureDaemon({ allowSpawn: runtimeConfig.autoStartDaemon });
  console.error(`[agentune] Connected to daemon on port ${port}`);
  await startProxy(port, controlToken);
}
```

## File: `src/package-metadata.ts`
```typescript
import { readFileSync } from 'node:fs';

export interface PackageMetadata {
  description: string;
  version: string;
  engines?: {
    node?: string;
  };
}

export function readPackageMetadata(): PackageMetadata {
  return JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8')) as PackageMetadata;
}
```

## File: `src/audio/mpv-controller.ts`
```typescript
import { EventEmitter } from 'node:events';
import { getIpcPath } from './platform-ipc-path.js';
import { isMpvInstalled, resolvePreferredMpvBinary } from './mpv-launch-helpers.js';
import { createMpvProcessSession, type MpvProcessExitEvent, type MpvPropertyChangeEvent, type MpvProcessSession } from './mpv-process-session.js';

export const MPV_STARTUP_WARMUP_MS = 500;

export interface TrackMeta {
  id: string; title: string; artist?: string; duration?: number; thumbnail?: string;
}

type MpvState = {
  currentTrack: TrackMeta | null;
  isMuted: boolean;
  isPlaying: boolean;
  volume: number;
};

export async function waitForMpvStartupWarmup(durationMs = MPV_STARTUP_WARMUP_MS): Promise<void> {
  await new Promise((resolve) => setTimeout(resolve, durationMs));
}

export class MpvController extends EventEmitter {
  private commandQueue = Promise.resolve();
  private destroying = false;
  private initialized = false;
  private pendingStoppedEvent = false;
  private session: MpvProcessSession | null = null;
  private readonly state: MpvState;
  // Count of idle-active events to silently discard (set via suppressNextStopped).
  // Prevents stale stop-originated events from corrupting the active track state.
  private suppressStoppedCount = 0;

  constructor(initialVolume = 80) {
    super();
    this.state = {
      currentTrack: null,
      isMuted: false,
      isPlaying: false,
      volume: clampVolume(initialVolume),
    };
  }

  init(): void {
    if (this.initialized) return;

    if (!isMpvInstalled()) {
      throw new Error(
        'mpv is not installed or not in PATH. ' +
        'Install: brew install mpv (macOS), apt install mpv (Linux), scoop install mpv (Windows)',
      );
    }

    const ipcPath = getIpcPath();
    console.error('[mpv] Initializing with IPC path:', ipcPath);

    this.session = createMpvProcessSession({
      binary: resolvePreferredMpvBinary(),
      ipcPath,
    });
    this.attachSessionEvents(this.session);
    this.session.start();
    this.initialized = true;
    this.emitStateChange();
    this.enqueueSessionCommand('set initial volume', () => this.session!.setVolume(this.state.volume));
    console.error('[mpv] Ready — headless audio engine started');
  }

  isReady(): boolean {
    return this.initialized && this.session !== null;
  }

  play(url: string, meta: TrackMeta): void {
    this.pendingStoppedEvent = false;
    this.state.currentTrack = meta;
    this.state.isPlaying = true;
    this.emitStateChange();
    console.error('[mpv] Playing:', meta.title);
    this.enqueueSessionCommand('load file', () => this.ensureSession().loadFile(url));
  }

  pause(): void {
    this.state.isPlaying = false;
    this.emitStateChange();
    console.error('[mpv] Paused');
    this.enqueueSessionCommand('pause playback', () => this.ensureSession().setPause(true));
  }

  resume(): void {
    this.state.isPlaying = this.state.currentTrack !== null;
    this.emitStateChange();
    console.error('[mpv] Resumed');
    this.enqueueSessionCommand('resume playback', () => this.ensureSession().setPause(false));
  }

  stop(): void {
    if (!this.state.currentTrack) return;

    this.pendingStoppedEvent = true;
    this.state.currentTrack = null;
    this.state.isPlaying = false;
    this.emitStateChange();
    console.error('[mpv] Stopped');
    this.enqueueSessionCommand('stop playback', () => this.ensureSession().stop());
  }

  setVolume(level: number): number {
    const clamped = clampVolume(level);
    this.state.volume = clamped;
    this.emitStateChange();
    console.error('[mpv] Volume set to:', clamped);
    this.enqueueSessionCommand('set volume', () => this.ensureSession().setVolume(clamped));
    return clamped;
  }

  getVolume(): number { return this.state.volume; }

  toggleMute(): boolean {
    this.state.isMuted = !this.state.isMuted;
    this.emitStateChange();
    console.error('[mpv] Mute toggled:', this.state.isMuted);
    this.enqueueSessionCommand('toggle mute', () => this.ensureSession().setMute(this.state.isMuted));
    return this.state.isMuted;
  }

  getIsMuted(): boolean { return this.state.isMuted; }

  async getPosition(): Promise<number> {
    const session = this.ensureSession();
    try {
      const position = await session.getProperty('time-pos');
      return typeof position === 'number' ? position : 0;
    } catch {
      return 0;
    }
  }

  async getDuration(): Promise<number> {
    const session = this.ensureSession();
    try {
      const duration = await session.getProperty('duration');
      return typeof duration === 'number' ? duration : 0;
    } catch {
      return 0;
    }
  }

  /** Tell the controller to silently discard the next N idle-active stopped events. */
  suppressNextStopped(): void {
    this.suppressStoppedCount++;
  }

  getCurrentTrack(): TrackMeta | null { return this.state.currentTrack; }

  getIsPlaying(): boolean { return this.state.isPlaying; }

  getState(): Readonly<MpvState> { return this.state; }

  destroy(): void {
    this.destroying = true;
    this.session?.destroy();
    this.session = null;
    this.initialized = false;
    this.pendingStoppedEvent = false;
    this.suppressStoppedCount = 0;
    this.state.currentTrack = null;
    this.state.isMuted = false;
    this.state.isPlaying = false;
    this.emitStateChange();
    this.removeAllListeners();
    controller = null;
    console.error('[mpv] Destroyed');
  }

  private attachSessionEvents(session: MpvProcessSession): void {
    session.on('property-change', (event: MpvPropertyChangeEvent) => {
      if (event.name === 'pause' && typeof event.data === 'boolean') {
        this.state.isPlaying = event.data ? false : this.state.currentTrack !== null;
        this.emitStateChange();
        this.emit(event.data ? 'paused' : 'resumed');
        return;
      }

      if (event.name === 'idle-active' && event.data === true) {
        this.handleStoppedEvent();
      }
    });

    session.on('exit', (event: MpvProcessExitEvent) => {
      this.handleSessionExit(event);
    });
  }

  private emitStateChange(): void {
    this.emit('state-change', this.state);
  }

  private enqueueSessionCommand(context: string, operation: () => Promise<void>): void {
    const nextCommand = this.commandQueue.then(operation, operation);
    this.commandQueue = nextCommand.catch(() => undefined);
    void nextCommand.catch((error: Error) => {
      console.error(`[mpv] Failed to ${context}:`, error.message);
    });
  }

  private ensureSession(): MpvProcessSession {
    if (!this.session || !this.initialized) throw new Error('mpv not initialized — call init() first');
    return this.session;
  }

  private handleSessionExit(event: MpvProcessExitEvent): void {
    if (this.destroying) return;

    this.session = null;
    this.initialized = false;
    this.pendingStoppedEvent = false;
    this.suppressStoppedCount = 0;
    this.state.currentTrack = null;
    this.state.isPlaying = false;
    this.emitStateChange();
    console.error('[mpv] Process exited unexpectedly:', { code: event.code, signal: event.signal });
  }

  private handleStoppedEvent(): void {
    // Discard stale idle-active events from a previous stop() that was
    // followed by a new play() before mpv processed the stop IPC command.
    if (this.suppressStoppedCount > 0) {
      this.suppressStoppedCount--;
      this.pendingStoppedEvent = false;
      return;
    }

    if (!this.pendingStoppedEvent && !this.state.currentTrack) return;

    this.pendingStoppedEvent = false;
    this.state.currentTrack = null;
    this.state.isPlaying = false;
    this.emitStateChange();
    this.emit('stopped');
  }
}

let controller: MpvController | null = null;

export function createMpvController(initialVolume = 80): MpvController {
  if (!controller) controller = new MpvController(initialVolume);
  return controller;
}

export function getMpvController(): MpvController | null { return controller; }

function clampVolume(level: number): number {
  return Math.max(0, Math.min(100, Math.round(level)));
}
```

## File: `src/audio/mpv-ipc-client.test.ts`
```typescript
import assert from 'node:assert/strict';
import { once } from 'node:events';
import { createServer } from 'node:net';
import { rmSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { MpvIpcClient } from './mpv-ipc-client.js';

function createTestSocketPath(name: string): string {
  if (process.platform === 'win32') {
    return `\\\\.\\pipe\\${name}-${process.pid}-${Date.now()}`;
  }

  return path.join(os.tmpdir(), `${name}-${process.pid}-${Date.now()}.sock`);
}

test('MpvIpcClient resolves out-of-order responses by request id', async () => {
  const socketPath = createTestSocketPath('agentune-mpv-ipc-order');
  const server = createServer();
  const requests: Array<{ requestId: number; socket: import('node:net').Socket }> = [];

  server.on('connection', (socket) => {
    socket.setEncoding('utf8');
    let buffer = '';
    socket.on('data', (chunk) => {
      buffer += chunk;
      while (true) {
        const newlineIndex = buffer.indexOf('\n');
        if (newlineIndex === -1) {
          return;
        }

        const line = buffer.slice(0, newlineIndex).trim();
        buffer = buffer.slice(newlineIndex + 1);
        if (!line) {
          continue;
        }

        const message = JSON.parse(line) as { request_id: number };
        requests.push({ requestId: message.request_id, socket });
        if (requests.length === 2) {
          requests[1].socket.write(JSON.stringify({
            data: 'second',
            error: 'success',
            request_id: requests[1].requestId,
          }) + '\n');
          requests[0].socket.write(JSON.stringify({
            data: 'first',
            error: 'success',
            request_id: requests[0].requestId,
          }) + '\n');
        }
      }
    });
  });

  await new Promise<void>((resolve) => server.listen(socketPath, resolve));
  const client = new MpvIpcClient();

  try {
    await client.connect(socketPath);
    const [firstResult, secondResult] = await Promise.all([
      client.command('get_property', 'time-pos'),
      client.command('get_property', 'duration'),
    ]);

    assert.equal(firstResult, 'first');
    assert.equal(secondResult, 'second');
  } finally {
    client.destroy();
    await new Promise<void>((resolve) => server.close(() => resolve()));
    if (process.platform !== 'win32') {
      rmSync(socketPath, { force: true });
    }
  }
});

test('MpvIpcClient emits property-change events and rejects non-success replies', async () => {
  const socketPath = createTestSocketPath('agentune-mpv-ipc-events');
  const server = createServer();

  server.on('connection', (socket) => {
    socket.setEncoding('utf8');
    let buffer = '';
    socket.on('data', (chunk) => {
      buffer += chunk;
      while (true) {
        const newlineIndex = buffer.indexOf('\n');
        if (newlineIndex === -1) {
          return;
        }

        const line = buffer.slice(0, newlineIndex).trim();
        buffer = buffer.slice(newlineIndex + 1);
        if (!line) {
          continue;
        }

        const message = JSON.parse(line) as { command: unknown[]; request_id: number };
        const [command, , propertyName] = message.command;
        if (command === 'observe_property') {
          socket.write(JSON.stringify({
            error: 'success',
            request_id: message.request_id,
          }) + '\n');
          socket.write(JSON.stringify({
            data: false,
            event: 'property-change',
            name: String(propertyName),
          }) + '\n');
          continue;
        }

        socket.write(JSON.stringify({
          error: 'property unavailable',
          request_id: message.request_id,
        }) + '\n');
      }
    });
  });

  await new Promise<void>((resolve) => server.listen(socketPath, resolve));
  const client = new MpvIpcClient();

  try {
    await client.connect(socketPath);
    const propertyChangePromise = once(client, 'property-change');
    await client.observeProperty(1, 'pause');

    const [event] = await propertyChangePromise;
    assert.deepEqual(event, { data: false, id: undefined, name: 'pause' });
    await assert.rejects(() => client.getProperty('missing'), /property unavailable/i);
  } finally {
    client.destroy();
    await new Promise<void>((resolve) => server.close(() => resolve()));
    if (process.platform !== 'win32') {
      rmSync(socketPath, { force: true });
    }
  }
});
```

## File: `src/audio/mpv-ipc-client.ts`
```typescript
import { EventEmitter } from 'node:events';
import { createConnection, type Socket } from 'node:net';

const CONNECT_RETRY_DELAY_MS = 50;
const DEFAULT_CONNECT_TIMEOUT_MS = 3_000;

type PendingRequest = {
  reject: (error: Error) => void;
  resolve: (value: unknown) => void;
};

type MpvMessage = {
  data?: unknown;
  error?: string;
  event?: string;
  id?: number;
  name?: string;
  request_id?: number;
  result?: unknown;
};

type PropertyChangeEvent = {
  data?: unknown;
  id?: number;
  name: string;
};

export class MpvIpcClient extends EventEmitter {
  private buffer = '';
  private connectPromise: Promise<void> | null = null;
  private destroyed = false;
  private nextRequestId = 1;
  private readonly pendingRequests = new Map<number, PendingRequest>();
  private socket: Socket | null = null;

  connect(socketPath: string, timeoutMs = DEFAULT_CONNECT_TIMEOUT_MS): Promise<void> {
    if (this.connectPromise) {
      return this.connectPromise;
    }

    this.connectPromise = this.connectWithRetry(socketPath, Date.now() + timeoutMs);
    return this.connectPromise;
  }

  async command(name: string, ...args: unknown[]): Promise<unknown> {
    await this.ensureConnected();
    const socket = this.socket;
    if (!socket) {
      throw new Error('mpv IPC socket is unavailable.');
    }

    const requestId = this.nextRequestId++;
    return await new Promise<unknown>((resolve, reject) => {
      this.pendingRequests.set(requestId, { resolve, reject });

      try {
        socket.write(JSON.stringify({
          command: [name, ...args],
          request_id: requestId,
        }) + '\n');
      } catch (error) {
        this.pendingRequests.delete(requestId);
        reject(error as Error);
      }
    });
  }

  async getProperty(name: string): Promise<unknown> {
    return await this.command('get_property', name);
  }

  async observeProperty(id: number, name: string): Promise<void> {
    await this.command('observe_property', id, name);
  }

  notify(name: string, ...args: unknown[]): void {
    const socket = this.socket;
    if (!socket) {
      return;
    }

    socket.write(JSON.stringify({ command: [name, ...args] }) + '\n');
  }

  destroy(): void {
    this.destroyed = true;
    this.rejectPendingRequests(new Error('mpv IPC client destroyed.'));
    this.socket?.destroy();
    this.socket = null;
  }

  private connectWithRetry(socketPath: string, deadline: number): Promise<void> {
    return new Promise<void>((resolve, reject) => {
      const attemptConnection = () => {
        if (this.destroyed) {
          reject(new Error('mpv IPC client destroyed.'));
          return;
        }

        const socket = createConnection(socketPath);
        socket.once('connect', () => {
          this.attachSocket(socket);
          resolve();
        });
        socket.once('error', (error: NodeJS.ErrnoException) => {
          socket.destroy();
          if (Date.now() < deadline && isRetryableConnectionError(error)) {
            setTimeout(attemptConnection, CONNECT_RETRY_DELAY_MS);
            return;
          }
          reject(error);
        });
      };

      attemptConnection();
    });
  }

  private attachSocket(socket: Socket): void {
    this.socket = socket;
    socket.setEncoding('utf8');
    socket.on('data', (chunk: string) => {
      this.buffer += chunk;
      this.consumeBufferedLines();
    });
    socket.on('close', () => {
      if (this.socket === socket) {
        this.socket = null;
      }
      this.rejectPendingRequests(new Error('mpv IPC connection closed.'));
      if (!this.destroyed) {
        this.emit('disconnect');
      }
    });
  }

  private consumeBufferedLines(): void {
    while (true) {
      const newlineIndex = this.buffer.indexOf('\n');
      if (newlineIndex === -1) {
        return;
      }

      const line = this.buffer.slice(0, newlineIndex).trim();
      this.buffer = this.buffer.slice(newlineIndex + 1);
      if (!line) {
        continue;
      }

      this.handleIncomingMessage(line);
    }
  }

  private ensureConnected(): Promise<void> {
    if (!this.connectPromise) {
      throw new Error('mpv IPC client is not connected.');
    }
    return this.connectPromise;
  }

  private handleIncomingMessage(line: string): void {
    let message: MpvMessage;
    try {
      message = JSON.parse(line) as MpvMessage;
    } catch {
      console.error('[mpv] Ignoring malformed IPC message:', line.slice(0, 200));
      return;
    }
    if (typeof message.request_id === 'number') {
      this.resolvePendingRequest(message);
      return;
    }

    if (message.event === 'property-change' && typeof message.name === 'string') {
      this.emit('property-change', {
        data: message.data,
        id: message.id,
        name: message.name,
      } satisfies PropertyChangeEvent);
      return;
    }

    if (message.event) {
      this.emit('event', message);
    }
  }

  private rejectPendingRequests(error: Error): void {
    for (const pendingRequest of this.pendingRequests.values()) {
      pendingRequest.reject(error);
    }
    this.pendingRequests.clear();
  }

  private resolvePendingRequest(message: MpvMessage): void {
    const pendingRequest = this.pendingRequests.get(message.request_id!);
    if (!pendingRequest) {
      return;
    }

    this.pendingRequests.delete(message.request_id!);
    if (message.error && message.error !== 'success') {
      pendingRequest.reject(new Error(`mpv command failed: ${message.error}`));
      return;
    }

    pendingRequest.resolve(message.data ?? message.result);
  }
}

function isRetryableConnectionError(error: NodeJS.ErrnoException): boolean {
  return error.code === 'ENOENT' || error.code === 'ECONNREFUSED';
}
```

## File: `src/audio/mpv-launch-helpers.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { firstResolvedExecutableFromWhere, shouldHideWindowsConsoleForCommand } from './mpv-launch-helpers.js';

test('firstResolvedExecutableFromWhere returns the first non-empty line', () => {
  const output = '\r\nC:\\Users\\Admin\\scoop\\apps\\mpv\\current\\mpv.exe\r\nC:\\Other\\mpv.exe\r\n';
  assert.equal(firstResolvedExecutableFromWhere(output), 'C:\\Users\\Admin\\scoop\\apps\\mpv\\current\\mpv.exe');
});

test('shouldHideWindowsConsoleForCommand matches mpv launch targets', () => {
  assert.equal(shouldHideWindowsConsoleForCommand('mpv'), true);
  assert.equal(shouldHideWindowsConsoleForCommand('"C:\\Tools\\mpv.exe"'), true);
  assert.equal(shouldHideWindowsConsoleForCommand('C:\\Tools\\mpv.com'), true);
  assert.equal(shouldHideWindowsConsoleForCommand('node'), false);
});
```

## File: `src/audio/mpv-launch-helpers.ts`
```typescript
import { spawnSync, spawn, type ChildProcess } from 'node:child_process';
import { unlinkSync } from 'node:fs';

const COMMAND_TIMEOUT_MS = 5_000;

export function isMpvInstalled(): boolean {
  return resolveInstalledMpvBinary() !== undefined;
}

export function cleanupStaleIpcPath(ipcPath: string): void {
  if (process.platform === 'win32') {
    return;
  }

  try {
    unlinkSync(ipcPath);
  } catch {
    // No stale socket to remove.
  }
}

export function spawnMpvProcess(ipcPath: string, preferredBinary?: string): ChildProcess {
  const binary = preferredBinary ?? resolvePreferredMpvBinary() ?? 'mpv';
  return spawn(binary, [
    `--input-ipc-server=${ipcPath}`,
    '--no-video',
    '--idle',
    '--no-config',
    '--terminal=no',
  ], {
    stdio: ['ignore', 'ignore', 'ignore'],
    windowsHide: shouldHideWindowsConsoleForCommand(binary),
  });
}

export function resolvePreferredMpvBinary(): string | undefined {
  if (process.platform !== 'win32') {
    return undefined;
  }

  return resolveBinaryPath('where.exe', ['mpv.exe']);
}

export function resolveInstalledMpvBinary(): string | undefined {
  if (process.platform === 'win32') {
    return resolvePreferredMpvBinary();
  }

  return resolveBinaryPath('which', ['mpv']);
}

export function firstResolvedExecutableFromWhere(output: string): string | undefined {
  return output
    .split(/\r?\n/u)
    .map((line) => line.trim())
    .find(Boolean);
}

export function shouldHideWindowsConsoleForCommand(command: string): boolean {
  const normalized = command.replaceAll('"', '').trim().toLowerCase();
  return normalized.endsWith('mpv')
    || normalized.endsWith('mpv.exe')
    || normalized.endsWith('mpv.com');
}

function resolveBinaryPath(command: string, args: string[]): string | undefined {
  try {
    const result = spawnSync(command, args, {
      encoding: 'utf8',
      stdio: ['ignore', 'pipe', 'ignore'],
      timeout: COMMAND_TIMEOUT_MS,
      windowsHide: true,
    });

    if (result.error || result.status !== 0) {
      return undefined;
    }

    return firstResolvedExecutableFromWhere(result.stdout ?? '');
  } catch {
    return undefined;
  }
}
```

## File: `src/audio/mpv-process-session.ts`
```typescript
import { EventEmitter } from 'node:events';
import type { ChildProcess } from 'node:child_process';
import { cleanupStaleIpcPath, spawnMpvProcess } from './mpv-launch-helpers.js';
import { MpvIpcClient } from './mpv-ipc-client.js';

type MpvProcessSessionOptions = {
  binary?: string;
  ipcPath: string;
};

export type MpvProcessExitEvent = {
  code: number | null;
  signal: NodeJS.Signals | null;
};

export type MpvPropertyChangeEvent = {
  data?: unknown;
  id?: number;
  name: string;
};

const OBSERVE_PAUSE_ID = 1;
const OBSERVE_IDLE_ACTIVE_ID = 2;

export class MpvProcessSession extends EventEmitter {
  private readonly client = new MpvIpcClient();
  private destroyed = false;
  private process: ChildProcess | null = null;
  private readyPromise: Promise<void> | null = null;

  constructor(private readonly options: MpvProcessSessionOptions) {
    super();
    this.client.on('property-change', (event: MpvPropertyChangeEvent) => {
      this.emit('property-change', event);
    });
  }

  start(): void {
    if (this.readyPromise) {
      return;
    }

    cleanupStaleIpcPath(this.options.ipcPath);
    this.process = spawnMpvProcess(this.options.ipcPath, this.options.binary);
    this.process.once('exit', (code, signal) => {
      this.emit('exit', { code, signal } satisfies MpvProcessExitEvent);
    });

    const exitedBeforeReady = new Promise<never>((_, reject) => {
      this.process?.once('exit', () => {
        reject(new Error('mpv exited before IPC was ready.'));
      });
    });

    this.readyPromise = Promise.race([
      this.client.connect(this.options.ipcPath),
      exitedBeforeReady,
    ]).then(async () => {
      await this.client.observeProperty(OBSERVE_PAUSE_ID, 'pause');
      await this.client.observeProperty(OBSERVE_IDLE_ACTIVE_ID, 'idle-active');
    });
  }

  async loadFile(url: string): Promise<void> {
    await this.command('loadfile', url, 'replace');
  }

  async setPause(paused: boolean): Promise<void> {
    await this.command('set_property', 'pause', paused);
  }

  async setVolume(level: number): Promise<void> {
    await this.command('set_property', 'volume', level);
  }

  async setMute(muted: boolean): Promise<void> {
    await this.command('set_property', 'mute', muted);
  }

  async stop(): Promise<void> {
    await this.command('stop');
  }

  async getProperty(name: string): Promise<unknown> {
    await this.ensureReady();
    return await this.client.getProperty(name);
  }

  destroy(): void {
    this.destroyed = true;
    this.client.notify('quit');
    this.client.destroy();

    const child = this.process;
    this.process = null;
    if (child && child.exitCode === null && !child.killed) {
      setTimeout(() => {
        if (child.exitCode === null && !child.killed) {
          try {
            child.kill();
          } catch {
            // mpv already exited.
          }
        }
      }, 100);
    }

    cleanupStaleIpcPath(this.options.ipcPath);
  }

  private async command(name: string, ...args: unknown[]): Promise<void> {
    await this.ensureReady();
    await this.client.command(name, ...args);
  }

  private async ensureReady(): Promise<void> {
    if (this.destroyed) {
      throw new Error('mpv session destroyed.');
    }
    if (!this.readyPromise) {
      throw new Error('mpv session not started.');
    }

    await this.readyPromise;
  }
}

export function createMpvProcessSession(options: MpvProcessSessionOptions): MpvProcessSession {
  return new MpvProcessSession(options);
}
```

## File: `src/audio/platform-ipc-path.ts`
```typescript
// Cross-platform IPC path for mpv JSON IPC communication
// Windows uses named pipes, Unix uses domain sockets

export function getIpcPath(): string {
  return process.platform === 'win32'
    ? '\\\\.\\pipe\\agentune-mpv'
    : '/tmp/agentune-mpv';
}
```

## File: `src/cli/doctor-command.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
import { renderDoctorReport, runDoctor } from './doctor-command.js';
import type { DoctorReport } from './doctor-report.js';

const sampleReport: DoctorReport = {
  checks: [
    { detail: 'Found v25.7.0; satisfies >=20', name: 'node', required: true, section: 'Runtime', status: 'OK' },
    { detail: 'Missing bundled binary', name: 'yt-dlp bundled', required: true, section: 'Dependencies', status: 'FAIL' },
    { detail: 'Daemon is not running', name: 'status', section: 'Daemon', status: 'WARN' },
    { detail: 'C:/Users/Admin/.agentune', name: 'dataDir', section: 'Paths', status: 'OK' },
  ],
  exitCode: 1,
  summary: 'FAIL',
};

test('renderDoctorReport prints sections in stable order', () => {
  const lines = renderDoctorReport(sampleReport);

  assert.deepEqual(lines, [
    '[agentune] Doctor summary: FAIL',
    '[agentune] Runtime',
    '[agentune]   OK   node: Found v25.7.0; satisfies >=20',
    '[agentune] Dependencies',
    '[agentune]   FAIL yt-dlp bundled: Missing bundled binary',
    '[agentune] Daemon',
    '[agentune]   WARN status: Daemon is not running',
    '[agentune] Paths',
    '[agentune]   OK   dataDir: C:/Users/Admin/.agentune',
  ]);
});

test('runDoctor logs the rendered report and applies the exit code', async () => {
  const logs: string[] = [];
  let exitCode = 0;

  const result = await runDoctor({
    collectDoctorReport: async () => sampleReport,
    log: (message) => {
      logs.push(message);
    },
    setExitCode: (code) => {
      exitCode = code;
    },
  });

  assert.equal(result, 1);
  assert.equal(exitCode, 1);
  assert.deepEqual(logs, renderDoctorReport(sampleReport));
});
```

## File: `src/cli/doctor-command.ts`
```typescript
import { collectDoctorReport, type DoctorReport } from './doctor-report.js';

const SECTION_ORDER = ['Runtime', 'Dependencies', 'Daemon', 'Paths'] as const;

export interface RunDoctorDependencies {
  collectDoctorReport: () => Promise<DoctorReport>;
  log: (message: string) => void;
  setExitCode: (code: number) => void;
}

export async function runDoctor(
  dependencies: RunDoctorDependencies = createRunDoctorDependencies(),
): Promise<number> {
  const report = await dependencies.collectDoctorReport();
  for (const line of renderDoctorReport(report)) {
    dependencies.log(line);
  }

  dependencies.setExitCode(report.exitCode);
  return report.exitCode;
}

export function renderDoctorReport(report: DoctorReport): string[] {
  const lines = [`[agentune] Doctor summary: ${report.summary}`];

  for (const section of SECTION_ORDER) {
    const checks = report.checks.filter((check) => check.section === section);
    if (checks.length === 0) {
      continue;
    }

    lines.push(`[agentune] ${section}`);
    for (const check of checks) {
      lines.push(`[agentune]   ${check.status.padEnd(4)} ${check.name}: ${check.detail}`);
    }
  }

  return lines;
}

function createRunDoctorDependencies(): RunDoctorDependencies {
  return {
    collectDoctorReport,
    log: (message) => {
      console.error(message);
    },
    setExitCode: (code) => {
      process.exitCode = code;
    },
  };
}
```

## File: `src/cli/doctor-report.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
import { collectDoctorReport, type DoctorReportDependencies } from './doctor-report.js';

function createDependencies(
  overrides: Partial<DoctorReportDependencies> = {},
): DoctorReportDependencies {
  return {
    executableExists: () => true,
    fetchHealth: async () => ({ ok: false }),
    getDaemonLogPath: () => 'C:/Users/Admin/.agentune/daemon.log',
    getDataDir: () => 'C:/Users/Admin/.agentune',
    getHistoryDbPath: () => 'C:/Users/Admin/.agentune/history.db',
    getPidFilePath: () => 'C:/Users/Admin/.agentune/daemon.pid',
    getRuntimeConfigPath: () => 'C:/Users/Admin/.agentune/config.json',
    isProcessAlive: () => false,
    loadRuntimeConfig: () => ({
      autoStartDaemon: true,
      daemonPort: 3747,
      dashboardPort: 3737,
      defaultVolume: 80,
      discoverRanking: {
        exploration: 0.35,
        loyalty: 0.65,
        variety: 0.55,
      },
    }),
    nodeVersion: 'v25.7.0',
    readPackageMetadata: () => ({
      description: 'Music Player for Agent',
      engines: { node: '>=20' },
      version: '0.1.1-alpha.3',
    }),
    readPidFile: () => null,
    readVersionLine: (command) => command.includes('mpv') ? 'mpv v0.41.0' : '2026.03.13',
    resolveBundledYtDlpBinary: () => 'C:/repo/node_modules/youtube-dl-exec/bin/yt-dlp.exe',
    resolveCommandFromPath: () => undefined,
    resolveInstalledMpvBinary: () => 'C:/Tools/mpv.exe',
    ...overrides,
  };
}

test('collectDoctorReport keeps advisory warnings non-fatal when required checks pass', async () => {
  const report = await collectDoctorReport(createDependencies());

  assert.equal(report.summary, 'OK');
  assert.equal(report.exitCode, 0);
  assert.deepEqual(
    report.checks
      .filter((check) => check.status === 'WARN')
      .map((check) => check.name),
    ['yt-dlp system', 'status'],
  );
});

test('collectDoctorReport fails when Node.js does not satisfy package engine', async () => {
  const report = await collectDoctorReport(createDependencies({ nodeVersion: 'v18.19.0' }));

  assert.equal(report.summary, 'FAIL');
  assert.equal(report.exitCode, 1);
  assert.equal(report.checks.find((check) => check.name === 'node')?.status, 'FAIL');
});

test('collectDoctorReport fails when runtime config validation throws', async () => {
  const report = await collectDoctorReport(createDependencies({
    loadRuntimeConfig: () => {
      throw new Error('Invalid runtime config: defaultVolume must be an integer between 0 and 100.');
    },
  }));

  assert.equal(report.summary, 'FAIL');
  assert.equal(report.exitCode, 1);
  assert.match(
    report.checks.find((check) => check.name === 'config')?.detail ?? '',
    /defaultVolume must be an integer between 0 and 100/i,
  );
});

test('collectDoctorReport fails when bundled yt-dlp is missing', async () => {
  const report = await collectDoctorReport(createDependencies({
    executableExists: () => false,
  }));

  assert.equal(report.summary, 'FAIL');
  assert.equal(report.exitCode, 1);
  assert.equal(report.checks.find((check) => check.name === 'yt-dlp bundled')?.status, 'FAIL');
});

test('collectDoctorReport reports daemon as healthy when pid and health endpoint are both good', async () => {
  const report = await collectDoctorReport(createDependencies({
    fetchHealth: async () => ({ ok: true, uptime: 42 }),
    isProcessAlive: () => true,
    readPidFile: () => ({
      controlToken: 'doctor-token',
      pid: 321,
      port: 3747,
      started: '2026-03-22T00:00:00.000Z',
    }),
  }));

  assert.equal(report.checks.find((check) => check.section === 'Daemon')?.status, 'OK');
  assert.match(report.checks.find((check) => check.section === 'Daemon')?.detail ?? '', /uptime=42s/);
});

test('collectDoctorReport reports stale daemon pid files as warnings', async () => {
  const report = await collectDoctorReport(createDependencies({
    isProcessAlive: () => false,
    readPidFile: () => ({
      controlToken: 'doctor-token',
      pid: 999,
      port: 3747,
      started: '2026-03-22T00:00:00.000Z',
    }),
  }));

  assert.equal(report.exitCode, 0);
  assert.equal(report.checks.find((check) => check.section === 'Daemon')?.status, 'WARN');
  assert.match(report.checks.find((check) => check.section === 'Daemon')?.detail ?? '', /stale pid file/i);
});
```

## File: `src/cli/doctor-report.ts`
```typescript
import { getDataDir, getDaemonLogPath, getHistoryDbPath, getPidFilePath, getRuntimeConfigPath } from '../runtime/runtime-data-paths.js';
import { loadRuntimeConfig, type RuntimeConfig } from '../runtime/runtime-config.js';
import { readPidFile, type DaemonInfo } from '../daemon/pid-manager.js';
import { readPackageMetadata, type PackageMetadata } from '../package-metadata.js';
import { resolveInstalledMpvBinary } from '../audio/mpv-launch-helpers.js';
import { executableExists, readVersionLine, resolveBundledYtDlpBinary, resolveCommandFromPath } from './doctor-runtime-support.js';

export type DoctorStatus = 'OK' | 'WARN' | 'FAIL';

export interface DoctorCheck {
  detail: string;
  name: string;
  required?: boolean;
  section: 'Runtime' | 'Dependencies' | 'Daemon' | 'Paths';
  status: DoctorStatus;
}

export interface DoctorReport {
  checks: DoctorCheck[];
  exitCode: number;
  summary: 'OK' | 'FAIL';
}

interface HealthCheckResult {
  ok: boolean;
  uptime?: number;
}

export interface DoctorReportDependencies {
  executableExists: (filePath: string) => boolean;
  fetchHealth: (port: number) => Promise<HealthCheckResult>;
  getDaemonLogPath: () => string;
  getDataDir: () => string;
  getHistoryDbPath: () => string;
  getPidFilePath: () => string;
  getRuntimeConfigPath: () => string;
  isProcessAlive: (pid: number) => boolean;
  loadRuntimeConfig: () => RuntimeConfig;
  nodeVersion: string;
  readPackageMetadata: () => PackageMetadata;
  readPidFile: () => DaemonInfo | null;
  readVersionLine: (command: string, args?: string[]) => string;
  resolveBundledYtDlpBinary: () => string;
  resolveCommandFromPath: (command: string) => string | undefined;
  resolveInstalledMpvBinary: () => string | undefined;
}

export async function collectDoctorReport(
  dependencies: DoctorReportDependencies = createDoctorReportDependencies(),
): Promise<DoctorReport> {
  const checks: DoctorCheck[] = [];

  checks.push(checkNodeRuntime(dependencies));
  checks.push(checkRuntimeConfig(dependencies));
  checks.push(...createPathChecks(dependencies));
  checks.push(checkMpvDependency(dependencies));
  checks.push(checkBundledYtDlpDependency(dependencies));
  checks.push(checkSystemYtDlpDependency(dependencies));
  checks.push(await checkDaemonState(dependencies));

  const exitCode = checks.some((check) => check.required && check.status === 'FAIL') ? 1 : 0;
  return { checks, exitCode, summary: exitCode === 0 ? 'OK' : 'FAIL' };
}

export function createDoctorReportDependencies(): DoctorReportDependencies {
  return {
    executableExists,
    fetchHealth: async (port) => {
      try {
        const response = await fetch(`http://127.0.0.1:${port}/health`, {
          signal: AbortSignal.timeout(2_000),
        });
        if (!response.ok) {
          return { ok: false };
        }

        const payload = await response.json() as { uptime?: unknown };
        return {
          ok: true,
          uptime: typeof payload.uptime === 'number' ? payload.uptime : undefined,
        };
      } catch {
        return { ok: false };
      }
    },
    getDaemonLogPath,
    getDataDir,
    getHistoryDbPath,
    getPidFilePath,
    getRuntimeConfigPath,
    isProcessAlive: (pid) => {
      try {
        process.kill(pid, 0);
        return true;
      } catch {
        return false;
      }
    },
    loadRuntimeConfig,
    nodeVersion: process.version,
    readPackageMetadata,
    readPidFile,
    readVersionLine,
    resolveBundledYtDlpBinary: () => resolveBundledYtDlpBinary(process.env),
    resolveCommandFromPath,
    resolveInstalledMpvBinary,
  };
}

function checkNodeRuntime(dependencies: DoctorReportDependencies): DoctorCheck {
  const requiredRange = dependencies.readPackageMetadata().engines?.node;
  const minimumMajor = requiredRange ? parseMinimumNodeMajor(requiredRange) : null;
  const actualMajor = parseVersionMajor(dependencies.nodeVersion);
  if (!requiredRange || minimumMajor === null || actualMajor === null) {
    return createCheck('Runtime', 'node', 'FAIL', `Could not validate Node.js against package.json engine "${requiredRange ?? 'missing'}"`, true);
  }

  if (actualMajor < minimumMajor) {
    return createCheck('Runtime', 'node', 'FAIL', `Found ${dependencies.nodeVersion}; requires ${requiredRange}`, true);
  }

  return createCheck('Runtime', 'node', 'OK', `Found ${dependencies.nodeVersion}; satisfies ${requiredRange}`, true);
}

function checkRuntimeConfig(dependencies: DoctorReportDependencies): DoctorCheck {
  try {
    const config = dependencies.loadRuntimeConfig();
    return createCheck(
      'Runtime',
      'config',
      'OK',
      `${dependencies.getRuntimeConfigPath()} (dashboard=${config.dashboardPort}, daemon=${config.daemonPort}, volume=${config.defaultVolume}, autoStart=${config.autoStartDaemon})`,
      true,
    );
  } catch (error) {
    return createCheck('Runtime', 'config', 'FAIL', (error as Error).message, true);
  }
}

function createPathChecks(dependencies: DoctorReportDependencies): DoctorCheck[] {
  return [
    createCheck('Paths', 'dataDir', 'OK', dependencies.getDataDir()),
    createCheck('Paths', 'configPath', 'OK', dependencies.getRuntimeConfigPath()),
    createCheck('Paths', 'historyDbPath', 'OK', dependencies.getHistoryDbPath()),
    createCheck('Paths', 'pidFilePath', 'OK', dependencies.getPidFilePath()),
    createCheck('Paths', 'daemonLogPath', 'OK', dependencies.getDaemonLogPath()),
  ];
}

function checkMpvDependency(dependencies: DoctorReportDependencies): DoctorCheck {
  const binaryPath = dependencies.resolveInstalledMpvBinary();
  if (!binaryPath) {
    return createCheck('Dependencies', 'mpv', 'FAIL', 'Not found in PATH', true);
  }

  return createVersionedCheck(dependencies, 'Dependencies', 'mpv', binaryPath, true);
}

function checkBundledYtDlpDependency(dependencies: DoctorReportDependencies): DoctorCheck {
  const binaryPath = dependencies.resolveBundledYtDlpBinary();
  if (!dependencies.executableExists(binaryPath)) {
    return createCheck('Dependencies', 'yt-dlp bundled', 'FAIL', `Missing bundled binary at ${binaryPath}`, true);
  }

  return createVersionedCheck(dependencies, 'Dependencies', 'yt-dlp bundled', binaryPath, true);
}

function checkSystemYtDlpDependency(dependencies: DoctorReportDependencies): DoctorCheck {
  const binaryPath = dependencies.resolveCommandFromPath('yt-dlp');
  if (!binaryPath) {
    return createCheck('Dependencies', 'yt-dlp system', 'WARN', 'Not found in PATH');
  }

  return createVersionedCheck(dependencies, 'Dependencies', 'yt-dlp system', binaryPath, false);
}

async function checkDaemonState(dependencies: DoctorReportDependencies): Promise<DoctorCheck> {
  const info = dependencies.readPidFile();
  if (!info) {
    return createCheck('Daemon', 'status', 'WARN', 'Daemon is not running');
  }
  if (!dependencies.isProcessAlive(info.pid)) {
    return createCheck('Daemon', 'status', 'WARN', `Stale PID file for pid=${info.pid}, port=${info.port}`);
  }

  const health = await dependencies.fetchHealth(info.port);
  if (!health.ok) {
    return createCheck('Daemon', 'status', 'WARN', `pid=${info.pid}, port=${info.port} is running but /health did not respond`);
  }

  const uptime = typeof health.uptime === 'number' ? `${Math.floor(health.uptime)}s` : 'unknown';
  return createCheck('Daemon', 'status', 'OK', `pid=${info.pid}, port=${info.port}, uptime=${uptime}`);
}

function createVersionedCheck(
  dependencies: DoctorReportDependencies,
  section: DoctorCheck['section'],
  name: string,
  binaryPath: string,
  required: boolean,
): DoctorCheck {
  try {
    const version = dependencies.readVersionLine(binaryPath);
    return createCheck(section, name, 'OK', `${version} (${binaryPath})`, required);
  } catch (error) {
    return createCheck(section, name, required ? 'FAIL' : 'WARN', `${(error as Error).message} (${binaryPath})`, required);
  }
}

function createCheck(
  section: DoctorCheck['section'],
  name: string,
  status: DoctorStatus,
  detail: string,
  required = false,
): DoctorCheck {
  return { detail, name, required, section, status };
}

function parseMinimumNodeMajor(engineRange: string): number | null {
  const match = engineRange.match(/>=\s*(\d+)/u);
  return match ? Number(match[1]) : null;
}

function parseVersionMajor(version: string): number | null {
  const match = version.match(/^v?(\d+)/u);
  return match ? Number(match[1]) : null;
}
```

## File: `src/cli/doctor-runtime-support.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
import { firstResolvedExecutableLine, readVersionLine } from './doctor-runtime-support.js';

test('firstResolvedExecutableLine returns the first non-empty line', () => {
  const output = '\r\nC:\\Tools\\yt-dlp.exe\r\nC:\\Backup\\yt-dlp.exe\r\n';
  assert.equal(firstResolvedExecutableLine(output), 'C:\\Tools\\yt-dlp.exe');
});

test('readVersionLine aborts hung subprocesses', () => {
  assert.throws(
    () => readVersionLine(process.execPath, ['-e', 'setInterval(() => {}, 1000)'], { timeoutMs: 50 }),
    /timed out/i,
  );
});
```

## File: `src/cli/doctor-runtime-support.ts`
```typescript
import { spawnSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { createRequire } from 'node:module';
import path from 'node:path';

const require = createRequire(import.meta.url);
const COMMAND_TIMEOUT_MS = 5_000;

export function executableExists(filePath: string): boolean {
  return existsSync(filePath);
}

export function firstResolvedExecutableLine(output: string): string | undefined {
  return output
    .split(/\r?\n/u)
    .map((line) => line.trim())
    .find(Boolean);
}

export function readVersionLine(
  command: string,
  args: string[] = ['--version'],
  options: { timeoutMs?: number } = {},
): string {
  const output = runCommand(command, args, options.timeoutMs ?? COMMAND_TIMEOUT_MS);
  return firstResolvedExecutableLine(output) ?? 'version unavailable';
}

export function resolveBundledYtDlpBinary(env: NodeJS.ProcessEnv = process.env): string {
  const packageEntryPath = require.resolve('youtube-dl-exec');
  const packageRoot = path.dirname(path.dirname(packageEntryPath));
  const binaryDir = env.YOUTUBE_DL_DIR ?? path.join(packageRoot, 'bin');
  const filename = env.YOUTUBE_DL_FILENAME || 'yt-dlp';
  const platform = env.YOUTUBE_DL_PLATFORM ?? (process.platform === 'win32' ? 'win32' : 'unix');
  const binaryName = !filename.endsWith('.exe') && platform === 'win32'
    ? `${filename}.exe`
    : filename;

  return path.join(binaryDir, binaryName);
}

export function resolveCommandFromPath(command: string): string | undefined {
  try {
    const output = runCommand(process.platform === 'win32' ? 'where.exe' : 'which', [command], COMMAND_TIMEOUT_MS);
    return firstResolvedExecutableLine(output);
  } catch {
    return undefined;
  }
}

function runCommand(command: string, args: string[], timeoutMs: number): string {
  const result = spawnSync(command, args, {
    encoding: 'utf8',
    stdio: ['ignore', 'pipe', 'pipe'],
    timeout: timeoutMs,
    windowsHide: true,
  });

  if (result.error) {
    const error = result.error as NodeJS.ErrnoException;
    if (error.code === 'ETIMEDOUT') {
      throw new Error(`Command timed out after ${timeoutMs}ms: ${command}`);
    }

    throw error;
  }

  if (result.status !== 0) {
    const detail = firstResolvedExecutableLine(`${result.stderr ?? ''}\n${result.stdout ?? ''}`)
      ?? `exit code ${result.status ?? 'unknown'}`;
    throw new Error(`Command failed for ${command}: ${detail}`);
  }

  return result.stdout ?? '';
}
```

## File: `src/cli/meta-command.test.ts`
```typescript
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const entrypointPath = fileURLToPath(new URL('../index.js', import.meta.url));
const packageJsonPath = new URL('../../package.json', import.meta.url);
const packageMetadata = JSON.parse(readFileSync(packageJsonPath, 'utf8')) as {
  description: string;
  version: string;
};

test('agentune --version prints package version and exits cleanly', () => {
  const result = spawnSync(process.execPath, [entrypointPath, '--version'], {
    encoding: 'utf8',
    timeout: 10_000,
  });

  assert.equal(result.status, 0);
  assert.equal(result.stderr, '');
  assert.equal(result.stdout.trim(), packageMetadata.version);
});

test('agentune --help prints CLI usage and exits cleanly', () => {
  const result = spawnSync(process.execPath, [entrypointPath, '--help'], {
    encoding: 'utf8',
    timeout: 10_000,
  });

  assert.equal(result.status, 0);
  assert.equal(result.stderr, '');
  assert.match(result.stdout, /^agentune/m);
  assert.match(result.stdout, new RegExp(packageMetadata.description.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')));
  assert.match(result.stdout, /agentune --version/);
  assert.match(result.stdout, /agentune doctor/);
  assert.match(result.stdout, /agentune start/);
});
```

## File: `src/cli/start-command.ts`
```typescript
// CLI start command — ensure the daemon is running in the background.

import { ensureDaemon } from '../proxy/daemon-launcher.js';

export async function runStart(): Promise<void> {
  const result = await ensureDaemon({ allowSpawn: true });
  if (result.started) {
    console.error(`[agentune] Daemon started on port ${result.port}`);
    return;
  }

  console.error(`[agentune] Daemon already running on port ${result.port}`);
}
```

## File: `src/cli/status-command.ts`
```typescript
// CLI status command — report daemon running state and uptime
// Exits 1 if daemon is not running or not responding

import { readPidFile, removePidFile } from '../daemon/pid-manager.js';

export async function runStatus(): Promise<void> {
  const info = readPidFile();
  if (!info) {
    console.error('[agentune] Daemon is not running');
    process.exit(1);
  }

  try {
    const res = await fetch(`http://127.0.0.1:${info.port}/health`, {
      signal: AbortSignal.timeout(2000),
    });
    if (!res.ok) throw new Error('unhealthy');
    const data = await res.json() as { uptime: number };
    console.error(
      `[agentune] Daemon running — PID: ${info.pid}, Port: ${info.port}, Uptime: ${Math.floor(data.uptime)}s`
    );
  } catch {
    console.error('[agentune] Daemon PID file exists but not responding (stale)');
    removePidFile();
    process.exit(1);
  }
}
```

## File: `src/cli/stop-command.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
import { DAEMON_CONTROL_TOKEN_HEADER } from '../daemon/daemon-auth.js';
import { runStop } from './stop-command.js';

test('runStop exits early when no daemon pid file exists', async () => {
  const logs: string[] = [];

  await runStop({
    fetch: async () => new Response(),
    getProcessCommand: () => null,
    isProcessAlive: () => false,
    killProcess: () => {
      throw new Error('kill should not be called');
    },
    log: (message) => {
      logs.push(message);
    },
    now: () => 0,
    readPidFile: () => null,
    removePidFile: () => {},
    sleep: async () => {},
  });

  assert.deepEqual(logs, ['[agentune] Daemon is not running']);
});

test('runStop waits for graceful HTTP shutdown before reporting success', async () => {
  const logs: string[] = [];
  const requests: RequestInit[] = [];
  let readCount = 0;

  await runStop({
    fetch: async (_input, init) => {
      requests.push(init ?? {});
      return new Response(null, { status: 200 });
    },
    getProcessCommand: () => (readCount < 2 ? 'node dist/index.js --daemon agentune' : null),
    isProcessAlive: () => readCount < 2,
    killProcess: () => {
      throw new Error('kill should not be called');
    },
    log: (message) => {
      logs.push(message);
    },
    now: () => readCount * 200,
    readPidFile: () => {
      readCount += 1;
      return readCount < 3
        ? { controlToken: 'shutdown-token', pid: 101, port: 3747, started: '2026-03-21T00:00:00.000Z' }
        : null;
    },
    removePidFile: () => {},
    sleep: async () => {},
  });

  assert.equal(logs.at(-1), '[agentune] Daemon stopped');
  assert.equal((requests[0]?.headers as Record<string, string>)[DAEMON_CONTROL_TOKEN_HEADER], 'shutdown-token');
});

test('runStop falls back to verified process kill when HTTP shutdown fails', async () => {
  const logs: string[] = [];
  let alive = true;
  let removedPidFile = false;
  let killCount = 0;

  await runStop({
    fetch: async () => {
      throw new Error('connect failed');
    },
    getProcessCommand: () => (alive ? 'node C:/repo/agentune/dist/index.js --daemon' : null),
    isProcessAlive: () => alive,
    killProcess: () => {
      killCount += 1;
      alive = false;
    },
    log: (message) => {
      logs.push(message);
    },
    now: () => (alive ? 0 : 200),
    readPidFile: () => (alive ? { controlToken: 'kill-token', pid: 202, port: 3747, started: '2026-03-21T00:00:00.000Z' } : null),
    removePidFile: () => {
      removedPidFile = true;
    },
    sleep: async () => {},
  });

  assert.equal(killCount, 1);
  assert.equal(removedPidFile, false);
  assert.equal(logs.at(-1), '[agentune] Daemon stopped');
});

test('runStop refuses to kill an unverified process when HTTP shutdown fails', async () => {
  const logs: string[] = [];
  let killCount = 0;

  await runStop({
    fetch: async () => {
      throw new Error('connect failed');
    },
    getProcessCommand: () => 'node other-app/index.js --daemon',
    isProcessAlive: () => true,
    killProcess: () => {
      killCount += 1;
    },
    log: (message) => {
      logs.push(message);
    },
    now: () => 0,
    readPidFile: () => ({ controlToken: 'refuse-token', pid: 303, port: 3747, started: '2026-03-21T00:00:00.000Z' }),
    removePidFile: () => {},
    sleep: async () => {},
  });

  assert.equal(killCount, 0);
  assert.equal(logs.at(-1), '[agentune] Could not verify daemon process identity; refusing to send SIGTERM.');
});

test('runStop exits without HTTP shutdown when daemon token is missing', async () => {
  const logs: string[] = [];
  let fetchCount = 0;

  await runStop({
    fetch: async () => {
      fetchCount += 1;
      return new Response(null, { status: 200 });
    },
    getProcessCommand: () => 'node other-app/index.js --daemon',
    isProcessAlive: () => true,
    killProcess: () => {
      throw new Error('kill should not be called');
    },
    log: (message) => {
      logs.push(message);
    },
    now: () => 0,
    readPidFile: () => ({ controlToken: '', pid: 404, port: 3747, started: '2026-03-21T00:00:00.000Z' }),
    removePidFile: () => {},
    sleep: async () => {},
  });

  assert.equal(fetchCount, 0);
  assert.equal(logs.at(-1), '[agentune] Could not verify daemon process identity; refusing to send SIGTERM.');
});
```

## File: `src/cli/stop-command.ts`
```typescript
// CLI stop command — gracefully stop the running daemon
// Falls back to SIGTERM if HTTP shutdown endpoint fails

import { spawnSync } from 'child_process';
import { DAEMON_CONTROL_TOKEN_HEADER } from '../daemon/daemon-auth.js';
import { readPidFile, removePidFile } from '../daemon/pid-manager.js';

const STOP_POLL_INTERVAL_MS = 200;
const STOP_TIMEOUT_MS = 10_000;

interface StopCommandDependencies {
  fetch: typeof fetch;
  getProcessCommand: (pid: number) => string | null;
  isProcessAlive: (pid: number) => boolean;
  killProcess: (pid: number) => void;
  log: (message: string) => void;
  now: () => number;
  readPidFile: typeof readPidFile;
  removePidFile: typeof removePidFile;
  sleep: (ms: number) => Promise<void>;
}

export async function runStop(
  dependencies: StopCommandDependencies = createStopCommandDependencies(),
): Promise<void> {
  const info = dependencies.readPidFile();
  if (!info) {
    dependencies.log('[agentune] Daemon is not running');
    return;
  }

  if (await requestShutdown(info.port, dependencies)) {
    if (await waitForDaemonStop(info.pid, info.port, dependencies)) {
      dependencies.log('[agentune] Daemon stopped');
      return;
    }

    dependencies.log('[agentune] HTTP shutdown timed out; attempting verified process stop');
  } else {
    dependencies.log('[agentune] Failed to stop daemon via HTTP, checking process identity');
  }

  if (!await tryVerifiedKill(info.pid, info.port, dependencies)) {
    dependencies.log('[agentune] Could not verify daemon process identity; refusing to send SIGTERM.');
    return;
  }

  if (await waitForDaemonStop(info.pid, info.port, dependencies)) {
    dependencies.log('[agentune] Daemon stopped');
    return;
  }

  dependencies.log('[agentune] Daemon stop timed out after SIGTERM.');
}

async function requestShutdown(port: number, dependencies: StopCommandDependencies): Promise<boolean> {
  const controlToken = dependencies.readPidFile()?.controlToken;
  if (!controlToken) {
    return false;
  }

  try {
    const response = await dependencies.fetch(`http://127.0.0.1:${port}/shutdown`, {
      headers: {
        [DAEMON_CONTROL_TOKEN_HEADER]: controlToken,
      },
      method: 'POST',
      signal: AbortSignal.timeout(5000),
    });
    return response.ok;
  } catch {
    return false;
  }
}

async function tryVerifiedKill(
  pid: number,
  port: number,
  dependencies: StopCommandDependencies,
): Promise<boolean> {
  const commandLine = dependencies.getProcessCommand(pid);
  if (!commandLine) {
    if (!dependencies.isProcessAlive(pid)) {
      if (dependencies.readPidFile()?.pid === pid && dependencies.readPidFile()?.port === port) {
        dependencies.removePidFile();
      }
      return true;
    }
    return false;
  }

  if (!looksLikeDaemonCommand(commandLine)) {
    return false;
  }

  try {
    dependencies.killProcess(pid);
    return true;
  } catch {
    return false;
  }
}

async function waitForDaemonStop(
  pid: number,
  port: number,
  dependencies: StopCommandDependencies,
): Promise<boolean> {
  const deadline = dependencies.now() + STOP_TIMEOUT_MS;

  while (dependencies.now() < deadline) {
    const currentPidFile = dependencies.readPidFile();
    const commandLine = dependencies.getProcessCommand(pid);
    const processAlive = dependencies.isProcessAlive(pid);
    const pidFileMatches = currentPidFile?.pid === pid && currentPidFile.port === port;

    if (!processAlive || !commandLine) {
      if (pidFileMatches) {
        dependencies.removePidFile();
      }
      return true;
    }

    if (!looksLikeDaemonCommand(commandLine)) {
      if (pidFileMatches) {
        dependencies.removePidFile();
      }
      return true;
    }

    await dependencies.sleep(STOP_POLL_INTERVAL_MS);
  }

  return false;
}

function looksLikeDaemonCommand(commandLine: string): boolean {
  const normalized = commandLine.toLowerCase();
  return normalized.includes('--daemon')
    && (
      normalized.includes('agentune')
      || normalized.includes('dist/index.js')
      || normalized.includes('dist\\index.js')
      || normalized.includes('src/index.ts')
      || normalized.includes('src\\index.ts')
    );
}

function createStopCommandDependencies(): StopCommandDependencies {
  return {
    fetch,
    getProcessCommand,
    isProcessAlive: (pid) => {
      try {
        process.kill(pid, 0);
        return true;
      } catch {
        return false;
      }
    },
    killProcess: (pid) => {
      process.kill(pid, 'SIGTERM');
    },
    log: (message) => {
      console.error(message);
    },
    now: () => Date.now(),
    readPidFile,
    removePidFile,
    sleep: async (ms) => await new Promise((resolve) => setTimeout(resolve, ms)),
  };
}

function getProcessCommand(pid: number): string | null {
  if (!Number.isInteger(pid) || pid < 0) return null;
  try {
    if (process.platform === 'win32') {
      const result = spawnSync(
        'powershell.exe',
        [
          '-NoProfile',
          '-NonInteractive',
          '-Command',
          `$p = Get-CimInstance Win32_Process -Filter "ProcessId = ${pid}"; if ($null -ne $p) { [Console]::Out.Write($p.CommandLine) }`,
        ],
        { encoding: 'utf8' },
      );
      return result.status === 0 ? result.stdout.trim() || null : null;
    }

    const result = spawnSync('ps', ['-p', String(pid), '-o', 'args='], { encoding: 'utf8' });
    return result.status === 0 ? result.stdout.trim() || null : null;
  } catch {
    return null;
  }
}
```

## File: `src/daemon/daemon-auth.ts`
```typescript
import { randomBytes, timingSafeEqual } from 'crypto';

export const DAEMON_CONTROL_TOKEN_HEADER = 'X-Agentune-Daemon-Token';

export function createDaemonControlToken(): string {
  return randomBytes(32).toString('base64url');
}

export function hasValidDaemonControlToken(headerValue: string | string[] | undefined, expectedToken: string): boolean {
  const candidate = normalizeHeaderValue(headerValue);
  if (!candidate) {
    return false;
  }

  const expectedBuffer = Buffer.from(expectedToken);
  const candidateBuffer = Buffer.from(candidate);
  return expectedBuffer.length === candidateBuffer.length
    && timingSafeEqual(expectedBuffer, candidateBuffer);
}

function normalizeHeaderValue(value: string | string[] | undefined): string | null {
  if (typeof value === 'string') {
    return value;
  }

  if (Array.isArray(value) && typeof value[0] === 'string') {
    return value[0];
  }

  return null;
}
```

## File: `src/daemon/daemon-server.test.ts`
```typescript
import assert from 'node:assert/strict';
import { createServer } from 'http';
import test from 'node:test';
import { DAEMON_CONTROL_TOKEN_HEADER } from './daemon-auth.js';
import { DaemonServer } from './daemon-server.js';

async function getAvailablePort(): Promise<number> {
  return await new Promise((resolve, reject) => {
    const server = createServer();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      if (!address || typeof address === 'string') {
        server.close(() => reject(new Error('Failed to allocate port.')));
        return;
      }

      server.close((error) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(address.port);
      });
    });
  });
}

test('DaemonServer requires control token for shutdown and mcp routes', async () => {
  const port = await getAvailablePort();
  const daemonServer = new DaemonServer(port, 'daemon-control-token');
  await daemonServer.start();

  try {
    const healthResponse = await fetch(`http://127.0.0.1:${port}/health`);
    assert.equal(healthResponse.status, 200);

    const shutdownForbidden = await fetch(`http://127.0.0.1:${port}/shutdown`, { method: 'POST' });
    assert.equal(shutdownForbidden.status, 403);

    const mcpForbidden = await fetch(`http://127.0.0.1:${port}/mcp`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ method: 'initialize', id: 1, jsonrpc: '2.0', params: {} }),
    });
    assert.equal(mcpForbidden.status, 403);

    const shutdownAllowed = await fetch(`http://127.0.0.1:${port}/shutdown`, {
      method: 'POST',
      headers: {
        [DAEMON_CONTROL_TOKEN_HEADER]: 'daemon-control-token',
      },
    });
    assert.equal(shutdownAllowed.status, 200);
  } finally {
    await daemonServer.destroy();
  }
});
```

## File: `src/daemon/daemon-server.ts`
```typescript
// HTTP server for daemon IPC — binds to the configured daemon port.
// Routes: GET /health, POST /shutdown, /mcp (POST/GET/DELETE)

import { createServer, type Server, type IncomingMessage, type ServerResponse } from 'http';
import { handleHealthRequest } from './health-endpoint.js';
import { DAEMON_CONTROL_TOKEN_HEADER, hasValidDaemonControlToken } from './daemon-auth.js';
import { createHttpMcpHandler } from '../mcp/mcp-server.js';

export class DaemonServer {
  private server: Server | null = null;
  private mcpHandler: ReturnType<typeof createHttpMcpHandler> | null = null;
  private shutdownFn: ((reason: string) => void) | null = null;

  constructor(
    private readonly port: number,
    private readonly controlToken: string,
  ) {}

  setShutdownHandler(fn: (reason: string) => void): void {
    this.shutdownFn = fn;
  }

  async start(): Promise<number> {
    this.mcpHandler = createHttpMcpHandler();
    this.server = createServer(async (req, res) => {
      const url = new URL(req.url ?? '/', `http://${req.headers.host ?? 'localhost'}`);

      // Route: GET /health
      if (req.method === 'GET' && url.pathname === '/health') {
        handleHealthRequest(req, res, this.port);
        return;
      }

      // Route: POST /shutdown
      if (req.method === 'POST' && url.pathname === '/shutdown') {
        if (!this.hasValidControlToken(req)) {
          sendJson(res, { error: 'Forbidden' }, 403);
          return;
        }
        sendJson(res, { status: 'shutting_down' });
        setTimeout(() => this.shutdownFn?.('HTTP /shutdown'), 100);
        return;
      }

      // Route: /mcp (POST, GET, DELETE)
      if (url.pathname === '/mcp') {
        if (!this.hasValidControlToken(req)) {
          sendJson(res, { error: 'Forbidden' }, 403);
          return;
        }
        const body = req.method === 'POST' ? await readBody(req) : undefined;
        await this.mcpHandler!.handleRequest(req, res, body);
        return;
      }

      // 404
      res.writeHead(404);
      res.end('Not Found');
    });

    return new Promise((resolve, reject) => {
      this.server!.listen(this.port, '127.0.0.1', () => {
        resolve(this.port);
      });
      this.server!.on('error', reject);
    });
  }

  async destroy(): Promise<void> {
    this.shutdownFn = null; // disarm to prevent double-shutdown from transport onclose
    await this.mcpHandler?.close();
    return new Promise((resolve) => {
      if (!this.server) { resolve(); return; }
      this.server.close(() => resolve());
      this.server.closeAllConnections();
    });
  }

  getPort(): number {
    return this.port;
  }

  private hasValidControlToken(req: IncomingMessage): boolean {
    return hasValidDaemonControlToken(req.headers[DAEMON_CONTROL_TOKEN_HEADER.toLowerCase()], this.controlToken);
  }
}

function sendJson(res: ServerResponse, data: unknown, statusCode = 200): void {
  res.writeHead(statusCode, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(data));
}

const MAX_BODY_SIZE = 1024 * 1024; // 1MB — MCP messages are small JSON

function readBody(req: IncomingMessage): Promise<unknown> {
  return new Promise((resolve, reject) => {
    const chunks: Buffer[] = [];
    let size = 0;
    req.on('data', (chunk: Buffer) => {
      size += chunk.length;
      if (size > MAX_BODY_SIZE) { req.destroy(); reject(new Error('Body too large')); return; }
      chunks.push(chunk);
    });
    req.on('end', () => {
      try { resolve(JSON.parse(Buffer.concat(chunks).toString())); }
      catch (e) { reject(e); }
    });
    req.on('error', reject);
  });
}
```

## File: `src/daemon/health-endpoint.ts`
```typescript
// Health check HTTP handler for daemon discovery
// Responds to GET /health with daemon status JSON

import { type IncomingMessage, type ServerResponse } from 'http';

const startedAt = Date.now();

/** Write JSON response with 200 status */
function sendJson(res: ServerResponse, data: unknown): void {
  res.writeHead(200, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify(data));
}

/** Handle GET /health — returns daemon status */
export function handleHealthRequest(
  req: IncomingMessage,
  res: ServerResponse,
  port: number,
): void {
  if (req.method !== 'GET') {
    res.writeHead(405);
    res.end('Method Not Allowed');
    return;
  }

  sendJson(res, {
    status: 'ok',
    pid: process.pid,
    port,
    uptime: Math.floor((Date.now() - startedAt) / 1000),
  });
}
```

## File: `src/daemon/pid-manager.ts`
```typescript
import { writeFileSync, readFileSync, unlinkSync } from 'fs';
import { getPidFilePath } from '../runtime/runtime-data-paths.js';
// PID file management for singleton daemon discovery.

export interface DaemonInfo {
  controlToken: string;
  pid: number;
  port: number;
  started: string;
}

/** Write current PID + port + ISO timestamp to PID file */
export function writePidFile(port: number, controlToken: string): void {
  const info: DaemonInfo = {
    controlToken,
    pid: process.pid,
    port,
    started: new Date().toISOString(),
  };
  writeFileSync(getPidFilePath(), JSON.stringify(info), { encoding: 'utf8', mode: 0o600 });
}

/** Read + parse PID file; returns null if missing, corrupt, or malformed */
export function readPidFile(): DaemonInfo | null {
  try {
    const raw = readFileSync(getPidFilePath(), 'utf8');
    const info = JSON.parse(raw) as Record<string, unknown>;
    if (typeof info.pid !== 'number' || typeof info.port !== 'number' || typeof info.controlToken !== 'string') {
      return null;
    }
    return info as unknown as DaemonInfo;
  } catch {
    return null;
  }
}

/** Remove PID file; ignores ENOENT */
export function removePidFile(): void {
  try {
    unlinkSync(getPidFilePath());
  } catch (err: unknown) {
    if ((err as NodeJS.ErrnoException).code !== 'ENOENT') throw err;
  }
}

/** Check if daemon is running by reading PID file and signaling process */
export function isDaemonRunning(): { running: boolean; info: DaemonInfo | null } {
  const info = readPidFile();
  if (!info) return { running: false, info: null };

  try {
    process.kill(info.pid, 0);
    return { running: true, info };
  } catch {
    // Process is dead — remove stale file
    removePidFile();
    return { running: false, info: null };
  }
}
```

## File: `src/history/history-schema.ts`
```typescript
// SQLite schema definitions and track ID normalization for play history.

export const HISTORY_SCHEMA_VERSION = 3;

/**
 * Normalize artist + title into a deterministic track ID.
 * Collapses whitespace and lowercases for dedup.
 * Example: normalizeTrackId("Nils  Frahm", "Says") → "nils frahm::says"
 */
export function normalizeTrackId(artist: string, title: string): string {
  const norm = (value: string) => value.toLowerCase().trim().replace(/\s+/g, ' ');
  return `${norm(artist)}::${norm(title)}`;
}

export const TRACKS_TABLE_SQL = `
CREATE TABLE IF NOT EXISTS tracks (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  artist TEXT NOT NULL,
  duration_sec INTEGER DEFAULT 0,
  thumbnail TEXT DEFAULT '',
  tags_json TEXT DEFAULT '[]',
  yt_video_id TEXT DEFAULT '',
  first_played_at INTEGER NOT NULL,
  play_count INTEGER DEFAULT 0
);
`;

export const PLAYS_TABLE_SQL = `
CREATE TABLE IF NOT EXISTS plays (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  track_id TEXT NOT NULL REFERENCES tracks(id),
  started_at INTEGER NOT NULL,
  played_sec INTEGER DEFAULT 0,
  skipped INTEGER DEFAULT 0,
  context_json TEXT DEFAULT '{}'
);
`;

export const SESSION_STATE_TABLE_SQL = `
CREATE TABLE IF NOT EXISTS session_state (
  id INTEGER PRIMARY KEY CHECK (id = 1),
  persona_taste_text TEXT DEFAULT ''
);
`;

export const PROVIDER_CACHE_TABLE_SQL = `
CREATE TABLE IF NOT EXISTS provider_cache (
  cache_key TEXT PRIMARY KEY,
  response_json TEXT NOT NULL,
  fetched_at INTEGER NOT NULL
);
`;

export const INDEXES_SQL = `
CREATE INDEX IF NOT EXISTS idx_plays_track_id ON plays(track_id);
CREATE INDEX IF NOT EXISTS idx_plays_started_at ON plays(started_at);
CREATE INDEX IF NOT EXISTS idx_plays_track_id_started_at ON plays(track_id, started_at DESC);
CREATE INDEX IF NOT EXISTS idx_tracks_play_count ON tracks(play_count DESC) WHERE play_count > 0;
CREATE INDEX IF NOT EXISTS idx_provider_cache_fetched_at ON provider_cache(fetched_at);
`;

export const SCHEMA_SQL = [
  TRACKS_TABLE_SQL,
  PLAYS_TABLE_SQL,
  SESSION_STATE_TABLE_SQL,
  PROVIDER_CACHE_TABLE_SQL,
  INDEXES_SQL,
].join('\n');
```

## File: `src/history/history-store-maintenance.ts`
```typescript
import type Database from 'better-sqlite3';

export interface HistoryDatabaseStats {
  dbPath: string;
  counts: {
    plays: number;
    tracks: number;
    providerCache: number;
  };
}

export interface HistoryCleanupResult {
  stats: HistoryDatabaseStats;
  removed: {
    plays: number;
    tracks: number;
    providerCache: number;
  };
}

export function getHistoryDatabaseStats(db: Database.Database, dbPath: string): HistoryDatabaseStats {
  return {
    dbPath,
    counts: {
      plays: countRows(db, 'plays'),
      tracks: countRows(db, 'tracks'),
      providerCache: countRows(db, 'provider_cache'),
    },
  };
}

export function clearHistoryData(db: Database.Database, dbPath: string): HistoryCleanupResult {
  const removed = {
    plays: countRows(db, 'plays'),
    tracks: countRows(db, 'tracks'),
    providerCache: 0,
  };

  db.transaction(() => {
    db.prepare('DELETE FROM plays').run();
    db.prepare('DELETE FROM tracks WHERE NOT EXISTS (SELECT 1 FROM plays WHERE plays.track_id = tracks.id)').run();
  })();
  runHistoryDatabaseMaintenance(db);

  return {
    removed,
    stats: getHistoryDatabaseStats(db, dbPath),
  };
}

export function clearProviderCacheData(db: Database.Database, dbPath: string): HistoryCleanupResult {
  const removed = {
    plays: 0,
    tracks: 0,
    providerCache: countRows(db, 'provider_cache'),
  };

  db.prepare('DELETE FROM provider_cache').run();
  runHistoryDatabaseMaintenance(db);

  return {
    removed,
    stats: getHistoryDatabaseStats(db, dbPath),
  };
}

export function fullResetData(db: Database.Database, dbPath: string): HistoryCleanupResult {
  const removed = {
    plays: countRows(db, 'plays'),
    tracks: countRows(db, 'tracks'),
    providerCache: countRows(db, 'provider_cache'),
  };

  db.transaction(() => {
    db.prepare('DELETE FROM provider_cache').run();
    db.prepare('DELETE FROM plays').run();
    db.prepare('DELETE FROM tracks WHERE NOT EXISTS (SELECT 1 FROM plays WHERE plays.track_id = tracks.id)').run();
  })();
  runHistoryDatabaseMaintenance(db);

  return {
    removed,
    stats: getHistoryDatabaseStats(db, dbPath),
  };
}

export function runHistoryDatabaseMaintenance(db: Database.Database): void {
  db.pragma('wal_checkpoint(TRUNCATE)');
  db.exec('VACUUM');
  db.pragma('optimize');
}

const VALID_TABLE_NAMES = new Set(['tracks', 'plays', 'provider_cache', 'session_state']);

function countRows(db: Database.Database, tableName: string): number {
  if (!VALID_TABLE_NAMES.has(tableName)) throw new Error(`Invalid table name: ${tableName}`);
  // SAFETY: tableName is validated against VALID_TABLE_NAMES allowlist above
  const row = db.prepare(`SELECT COUNT(*) as count FROM "${tableName}"`).get() as { count: number };
  return row.count;
}
```

## File: `src/history/history-store-migrations.ts`
```typescript
import type Database from 'better-sqlite3';
import {
  HISTORY_SCHEMA_VERSION,
  INDEXES_SQL,
  PLAYS_TABLE_SQL,
  PROVIDER_CACHE_TABLE_SQL,
  SESSION_STATE_TABLE_SQL,
  TRACKS_TABLE_SQL,
} from './history-schema.js';

export function applyHistoryStoreMigrations(db: Database.Database): void {
  const version = Number(db.pragma('user_version', { simple: true }) ?? 0);
  if (!hasAnyHistoryTables(db)) {
    db.exec([
      TRACKS_TABLE_SQL,
      PLAYS_TABLE_SQL,
      SESSION_STATE_TABLE_SQL,
      PROVIDER_CACHE_TABLE_SQL,
      INDEXES_SQL,
    ].join('\n'));
    db.pragma(`user_version = ${HISTORY_SCHEMA_VERSION}`);
    return;
  }

  if (version < HISTORY_SCHEMA_VERSION) {
    migrateToVersion3(db);
  }

  db.exec([
    TRACKS_TABLE_SQL,
    PLAYS_TABLE_SQL,
    SESSION_STATE_TABLE_SQL,
    PROVIDER_CACHE_TABLE_SQL,
    INDEXES_SQL,
  ].join('\n'));
  db.pragma(`user_version = ${HISTORY_SCHEMA_VERSION}`);
}

function migrateToVersion3(db: Database.Database): void {
  const trackColumns = getColumnNames(db, 'tracks');
  const playColumns = getColumnNames(db, 'plays');
  const sessionStateColumns = getColumnNames(db, 'session_state');

  db.exec('PRAGMA foreign_keys = OFF');
  db.exec('BEGIN');

  try {
    db.exec(`
      CREATE TABLE tracks_next (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        artist TEXT NOT NULL,
        duration_sec INTEGER DEFAULT 0,
        thumbnail TEXT DEFAULT '',
        tags_json TEXT DEFAULT '[]',
        yt_video_id TEXT DEFAULT '',
        first_played_at INTEGER NOT NULL,
        play_count INTEGER DEFAULT 0
      );

      CREATE TABLE plays_next (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        track_id TEXT NOT NULL REFERENCES tracks_next(id),
        started_at INTEGER NOT NULL,
        played_sec INTEGER DEFAULT 0,
        skipped INTEGER DEFAULT 0,
        context_json TEXT DEFAULT '{}'
      );

      CREATE TABLE session_state_next (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        persona_taste_text TEXT DEFAULT ''
      );
    `);

    if (trackColumns.size > 0) {
      db.exec(`
        INSERT INTO tracks_next (
          id, title, artist, duration_sec, thumbnail, tags_json, yt_video_id, first_played_at, play_count
        )
        SELECT
          id,
          title,
          artist,
          ${selectColumn(trackColumns, 'duration_sec', '0')},
          ${selectColumn(trackColumns, 'thumbnail', "''")},
          ${selectColumn(trackColumns, 'tags_json', "'[]'")},
          ${selectColumn(trackColumns, 'yt_video_id', "''")},
          ${selectColumn(trackColumns, 'first_played_at', '0')},
          ${selectColumn(trackColumns, 'play_count', '0')}
        FROM tracks
      `);
    }

    if (playColumns.size > 0) {
      db.exec(`
        INSERT INTO plays_next (
          id, track_id, started_at, played_sec, skipped, context_json
        )
        SELECT
          id,
          track_id,
          started_at,
          ${selectColumn(playColumns, 'played_sec', '0')},
          ${selectColumn(playColumns, 'skipped', '0')},
          ${selectColumn(playColumns, 'context_json', "'{}'")}
        FROM plays
      `);
    }

    if (sessionStateColumns.size > 0) {
      db.exec(`
        INSERT INTO session_state_next (id, persona_taste_text)
        SELECT
          id,
          ${selectColumn(sessionStateColumns, 'persona_taste_text', "''")}
        FROM session_state
        WHERE id = 1
      `);
    }

    db.exec(`
      DROP TABLE IF EXISTS plays;
      DROP TABLE IF EXISTS tracks;
      DROP TABLE IF EXISTS session_state;
      DROP TABLE IF EXISTS preferences;
      ALTER TABLE tracks_next RENAME TO tracks;
      ALTER TABLE plays_next RENAME TO plays;
      ALTER TABLE session_state_next RENAME TO session_state;
    `);

    db.exec('COMMIT');
  } catch (error) {
    db.exec('ROLLBACK');
    throw error;
  } finally {
    db.exec('PRAGMA foreign_keys = ON');
  }
}

function hasAnyHistoryTables(db: Database.Database): boolean {
  const row = db.prepare(`
    SELECT 1
    FROM sqlite_master
    WHERE type = 'table'
      AND name IN ('tracks', 'plays', 'session_state', 'provider_cache', 'preferences')
    LIMIT 1
  `).get() as Record<string, unknown> | undefined;
  return !!row;
}

const VALID_TABLE_NAMES = new Set(['tracks', 'plays', 'session_state', 'provider_cache', 'preferences']);

function getColumnNames(db: Database.Database, tableName: string): Set<string> {
  if (!VALID_TABLE_NAMES.has(tableName)) throw new Error(`Invalid table name: ${tableName}`);

  const tableExists = db.prepare(`
    SELECT 1
    FROM sqlite_master
    WHERE type = 'table' AND name = ?
    LIMIT 1
  `).get(tableName) as Record<string, unknown> | undefined;

  if (!tableExists) {
    return new Set();
  }

  // SAFETY: tableName is validated against VALID_TABLE_NAMES allowlist above
  const columns = db.prepare(`PRAGMA table_info("${tableName}")`).all() as Array<{ name: string }>;
  return new Set(columns.map((column) => column.name));
}

function selectColumn(columns: Set<string>, columnName: string, fallbackSql: string): string {
  return columns.has(columnName) ? columnName : fallbackSql;
}
```

## File: `src/history/history-store-state-redesign.test.ts`
```typescript
import assert from 'node:assert/strict';
import Database from 'better-sqlite3';
import fs from 'fs';
import os from 'os';
import path from 'path';
import test from 'node:test';
import { HistoryStore } from './history-store.js';

function getTempDbPath(): string {
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'agentune-history-redesign-'));
  return path.join(tmpDir, 'history.db');
}

function cleanupDb(dbPath: string): void {
  const dir = path.dirname(dbPath);
  try {
    if (fs.existsSync(dbPath)) fs.unlinkSync(dbPath);
    if (fs.existsSync(`${dbPath}-wal`)) fs.unlinkSync(`${dbPath}-wal`);
    if (fs.existsSync(`${dbPath}-shm`)) fs.unlinkSync(`${dbPath}-shm`);
    if (fs.existsSync(dir)) fs.rmdirSync(dir);
  } catch {
    // Ignore cleanup errors in tests.
  }
}

function recordPlay(
  store: HistoryStore,
  track: { title: string; artist: string; duration: number; tags?: string[]; playedSec?: number; skipped?: boolean },
): void {
  const playId = store.recordPlay({
    title: track.title,
    artist: track.artist,
    duration: track.duration,
    thumbnail: 'thumb',
    ytVideoId: `${track.artist}-${track.title}`.replace(/\s+/g, '-').toLowerCase(),
  });
  if (track.tags) {
    store.updateTrackTags(`${track.artist.toLowerCase()}::${track.title.toLowerCase()}`, track.tags);
  }
  store.updatePlay(playId, { played_sec: track.playedSec ?? track.duration, skipped: track.skipped ?? false });
}

test('HistoryStore.getTopArtists counts real plays instead of multiplying track totals', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    recordPlay(store, { title: 'Track 1', artist: 'Artist A', duration: 200, playedSec: 180 });
    recordPlay(store, { title: 'Track 2', artist: 'Artist A', duration: 200, playedSec: 190 });
    recordPlay(store, { title: 'Track 3', artist: 'Artist A', duration: 200, playedSec: 170 });
    recordPlay(store, { title: 'Track 4', artist: 'Artist B', duration: 200, playedSec: 120, skipped: true });

    const topArtists = store.getTopArtists(5);
    assert.equal(topArtists[0]?.artist, 'Artist A');
    assert.equal(topArtists[0]?.plays, 3);
    assert.equal(topArtists[1]?.artist, 'Artist B');
    assert.equal(topArtists[1]?.plays, 1);
    assert.ok((topArtists[0]?.avgCompletion ?? 0) > (topArtists[1]?.avgCompletion ?? 0));
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore exposes detailed recent plays, tag stats, and persona taste text', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    recordPlay(store, {
      title: 'Focus Track',
      artist: 'Artist A',
      duration: 200,
      tags: ['ambient', 'focus'],
      playedSec: 150,
      skipped: true,
    });
    recordPlay(store, {
      title: 'Night Track',
      artist: 'Artist B',
      duration: 240,
      tags: ['ambient', 'night'],
      playedSec: 210,
    });
    store.savePersonaTasteText('Warm ambient and slow piano.');

    const recentDetailed = store.getRecentPlaysDetailed(5);
    const topTags = store.getTopTags(5);

    assert.equal(recentDetailed.length, 2);
    assert.deepEqual(recentDetailed[0]?.tags, ['ambient', 'night']);
    assert.equal(recentDetailed[1]?.skipped, true);
    assert.ok(topTags.some((tag) => tag.tag === 'ambient' && tag.frequency >= 2));
    assert.equal(store.getPersonaTasteText(), 'Warm ambient and slow piano.');
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore migrates legacy schema to v3 and drops unused columns', () => {
  const dbPath = getTempDbPath();
  try {
    const legacyDb = new Database(dbPath);
    legacyDb.exec(`
      CREATE TABLE tracks (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        artist TEXT NOT NULL,
        duration_sec INTEGER DEFAULT 0,
        thumbnail TEXT DEFAULT '',
        tags_json TEXT DEFAULT '[]',
        similar_json TEXT DEFAULT '[]',
        yt_video_id TEXT DEFAULT '',
        first_played_at INTEGER NOT NULL,
        play_count INTEGER DEFAULT 0
      );
      CREATE TABLE plays (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        track_id TEXT NOT NULL REFERENCES tracks(id),
        started_at INTEGER NOT NULL,
        played_sec INTEGER DEFAULT 0,
        skipped INTEGER DEFAULT 0,
        context_json TEXT DEFAULT '{}',
        lane_id TEXT DEFAULT ''
      );
      CREATE TABLE preferences (
        key TEXT PRIMARY KEY,
        weight REAL DEFAULT 0,
        boredom REAL DEFAULT 0,
        last_seen_at INTEGER DEFAULT 0
      );
      CREATE TABLE session_state (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        lane_json TEXT DEFAULT '{}',
        taste_state_json TEXT DEFAULT '{}',
        agent_persona_json TEXT DEFAULT '{}',
        current_intent_json TEXT DEFAULT '{}',
        persona_taste_text TEXT DEFAULT '',
        persona_traits_json TEXT DEFAULT '{"exploration":0.2,"variety":0.9,"loyalty":0.4}'
      );
      CREATE TABLE provider_cache (
        cache_key TEXT PRIMARY KEY,
        response_json TEXT NOT NULL,
        fetched_at INTEGER NOT NULL
      );
      INSERT INTO tracks (id, title, artist, duration_sec, thumbnail, tags_json, similar_json, yt_video_id, first_played_at, play_count)
      VALUES ('artist::track', 'Track', 'Artist', 200, 'thumb', '["focus"]', '["other"]', 'vid1', 123, 1);
      INSERT INTO plays (track_id, started_at, played_sec, skipped, context_json, lane_id)
      VALUES ('artist::track', 123, 150, 0, '{"source":"legacy"}', 'legacy-lane');
      INSERT INTO session_state (id, lane_json, taste_state_json, agent_persona_json, current_intent_json, persona_taste_text, persona_traits_json)
      VALUES (1, '{}', '{}', '{}', '{}', 'Migrated taste', '{"exploration":0.2,"variety":0.9,"loyalty":0.4}');
      INSERT INTO provider_cache (cache_key, response_json, fetched_at)
      VALUES ('apple:test', '{}', 100);
    `);
    legacyDb.close();

    const store = new HistoryStore(dbPath);
    const db = store.getDatabase();
    const sessionColumns = db.prepare('PRAGMA table_info(session_state)').all() as Array<{ name: string }>;
    const playColumns = db.prepare('PRAGMA table_info(plays)').all() as Array<{ name: string }>;
    const trackColumns = db.prepare('PRAGMA table_info(tracks)').all() as Array<{ name: string }>;
    const preferencesTable = db.prepare(`
      SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'preferences'
    `).get() as { name: string } | undefined;

    assert.equal(db.pragma('user_version', { simple: true }), 3);
    assert.equal(store.getPersonaTasteText(), 'Migrated taste');
    assert.ok(!sessionColumns.some((column) => column.name === 'lane_json'));
    assert.ok(!sessionColumns.some((column) => column.name === 'persona_traits_json'));
    assert.ok(!playColumns.some((column) => column.name === 'lane_id'));
    assert.ok(!trackColumns.some((column) => column.name === 'similar_json'));
    assert.equal(preferencesTable, undefined);
    assert.equal(store.getRecent(5).length, 1);
    assert.equal(store.getDatabaseStats().counts.providerCache, 1);
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});
```

## File: `src/history/history-store.test.ts`
```typescript
import assert from 'node:assert/strict';
import fs from 'fs';
import os from 'os';
import path from 'path';
import test from 'node:test';
import { normalizeTrackId } from './history-schema.js';
import { HistoryStore } from './history-store.js';

function getTempDbPath(): string {
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'agentune-history-store-'));
  return path.join(tmpDir, 'history.db');
}

function cleanupDb(dbPath: string): void {
  const dir = path.dirname(dbPath);
  try {
    if (fs.existsSync(dbPath)) fs.unlinkSync(dbPath);
    if (fs.existsSync(`${dbPath}-wal`)) fs.unlinkSync(`${dbPath}-wal`);
    if (fs.existsSync(`${dbPath}-shm`)) fs.unlinkSync(`${dbPath}-shm`);
    if (fs.existsSync(dir)) fs.rmdirSync(dir);
  } catch {
    // Ignore cleanup errors in tests.
  }
}

function createTrack(overrides?: Partial<Parameters<HistoryStore['recordPlay']>[0]>) {
  return {
    title: 'Nylon',
    artist: 'Nils Frahm',
    duration: 215,
    thumbnail: 'https://example.com/thumb.jpg',
    ytVideoId: 'dummyid123',
    ...overrides,
  };
}

test('normalizeTrackId formats deterministic ids', () => {
  assert.equal(normalizeTrackId('Nils  Frahm', 'Says'), 'nils frahm::says');
  assert.equal(normalizeTrackId('  The Beatles  ', '  HELP!  '), 'the beatles::help!');
  assert.equal(normalizeTrackId('', ''), '::');
});

test('HistoryStore records plays and returns recent rows', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    const playId = store.recordPlay(createTrack(), { source: 'mcp' });

    assert.equal(typeof playId, 'number');
    const recent = store.getRecent(1);
    assert.equal(recent.length, 1);
    assert.equal(recent[0]?.id, 'nils frahm::nylon');
    assert.equal(recent[0]?.title, 'Nylon');
    assert.equal(recent[0]?.artist, 'Nils Frahm');
    assert.equal(recent[0]?.play_count, 1);
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore increments play_count and honors canonical overrides', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    store.recordPlay(createTrack({ title: 'says', artist: 'nils frahm' }), undefined, {
      artist: 'Nils Frahm',
      title: 'Says',
    });
    store.recordPlay(createTrack({ title: 'Says', artist: 'Nils Frahm' }));

    const recent = store.getRecent(2);
    assert.equal(recent[0]?.title, 'Says');
    assert.equal(recent[0]?.artist, 'Nils Frahm');
    assert.equal(recent[0]?.play_count, 2);
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore updates play metrics and batch stats', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    const play1 = store.recordPlay(createTrack({ title: 'Track A', artist: 'Artist A', duration: 300 }));
    const play2 = store.recordPlay(createTrack({ title: 'Track A', artist: 'Artist A', duration: 300 }));
    store.updatePlay(play1, { played_sec: 300, skipped: false });
    store.updatePlay(play2, { played_sec: 90, skipped: true });

    const stats = store.getTrackStats('artist a::track a');
    assert.equal(stats.playCount, 2);
    assert.equal(stats.skipRate, 0.5);
    assert.ok(stats.avgCompletion > 0.6 && stats.avgCompletion < 0.7);

    const batchStats = store.batchGetTrackStats(['artist a::track a', 'missing::track']);
    assert.equal(batchStats.get('artist a::track a')?.playCount, 2);
    assert.equal(batchStats.get('missing::track')?.playCount, 0);
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore exposes ranking helpers and search', async () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    store.recordPlay(createTrack({ title: 'Nylon', artist: 'Nils Frahm', ytVideoId: 'vid-1' }));
    await new Promise((resolve) => setTimeout(resolve, 5));
    store.recordPlay(createTrack({ title: 'Unfinished', artist: 'Nils Frahm', ytVideoId: 'vid-2' }));

    const filtered = store.getRecent(10, 'Unfinished');
    assert.equal(filtered.length, 1);
    assert.equal(filtered[0]?.title, 'Unfinished');
    assert.equal(store.getTrackPlayCount('Nils Frahm', 'Unfinished'), 1);
    assert.ok(store.hoursSinceLastPlay('Nils Frahm', 'Unfinished') < 1);
    assert.equal(store.getTopTracks(10)[0]?.play_count, 1);
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore persists persona taste text', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    store.savePersonaTasteText('Warm ambient and slow piano.');

    assert.equal(store.getPersonaTasteText(), 'Warm ambient and slow piano.');
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore exposes stats and granular cleanup operations', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    store.recordPlay(createTrack());
    store.recordPlay(createTrack({ title: 'Second', artist: 'Artist B', ytVideoId: 'vid-2' }));
    store.getDatabase().prepare(`
      INSERT INTO provider_cache (cache_key, response_json, fetched_at)
      VALUES ('apple:test', '{}', 123)
    `).run();

    assert.deepEqual(store.getDatabaseStats().counts, { plays: 2, tracks: 2, providerCache: 1 });

    const cacheCleanup = store.clearProviderCache();
    assert.equal(cacheCleanup.removed.providerCache, 1);
    assert.equal(cacheCleanup.stats.counts.providerCache, 0);
    assert.equal(cacheCleanup.stats.counts.plays, 2);

    const historyCleanup = store.clearHistory();
    assert.deepEqual(historyCleanup.removed, { plays: 2, tracks: 2, providerCache: 0 });
    assert.deepEqual(historyCleanup.stats.counts, { plays: 0, tracks: 0, providerCache: 0 });
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore database stats include empty insights when no listening history exists', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    const stats = store.getDatabaseStats();

    assert.deepEqual(stats, {
      dbPath,
      counts: { plays: 0, tracks: 0, providerCache: 0 },
      insights: {
        plays7d: 0,
        tracks7d: 0,
        skipRate: 0,
        activity7d: stats.insights.activity7d,
        topArtists: [],
        topKeywords: [],
      },
    });
    assert.equal(stats.insights.activity7d.length, 7);
    assert.ok(stats.insights.activity7d.every((bucket) => bucket.plays === 0));

    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore database stats expose dashboard insights from play history', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    const now = Date.now();
    const twoDaysAgo = now - (2 * 24 * 60 * 60 * 1000);
    const yesterday = now - (24 * 60 * 60 * 1000);

    const ambientPlay = store.recordPlay(createTrack({ title: 'Says', artist: 'Nils Frahm', duration: 200, ytVideoId: 'vid-a' }));
    const secondAmbientPlay = store.recordPlay(createTrack({ title: 'Says', artist: 'Nils Frahm', duration: 200, ytVideoId: 'vid-a-2' }));
    const electronicPlay = store.recordPlay(createTrack({ title: 'A New Error', artist: 'Moderat', duration: 240, ytVideoId: 'vid-b' }));

    store.updatePlay(ambientPlay, { played_sec: 200, skipped: false });
    store.updatePlay(secondAmbientPlay, { played_sec: 100, skipped: true });
    store.updatePlay(electronicPlay, { played_sec: 180, skipped: false });

    store.getDatabase().prepare('UPDATE plays SET started_at = ? WHERE id = ?').run(twoDaysAgo, ambientPlay);
    store.getDatabase().prepare('UPDATE plays SET started_at = ? WHERE id = ?').run(yesterday, secondAmbientPlay);
    store.getDatabase().prepare('UPDATE plays SET started_at = ? WHERE id = ?').run(now, electronicPlay);
    store.updateTrackTags(normalizeTrackId('Nils Frahm', 'Says'), ['ambient', 'piano']);
    store.updateTrackTags(normalizeTrackId('Moderat', 'A New Error'), ['electronic']);

    const stats = store.getDatabaseStats();

    assert.deepEqual(stats.counts, { plays: 3, tracks: 2, providerCache: 0 });
    assert.equal(stats.insights.plays7d, 3);
    assert.equal(stats.insights.tracks7d, 2);
    assert.equal(stats.insights.activity7d.length, 7);
    assert.equal(stats.insights.activity7d.reduce((sum, bucket) => sum + bucket.plays, 0), 3);
    assert.equal(stats.insights.topArtists.length, 2);
    assert.equal(stats.insights.topArtists[0]?.artist, 'Nils Frahm');
    assert.equal(stats.insights.topArtists[0]?.plays, 2);
    assert.equal(stats.insights.topKeywords.length, 3);
    assert.equal(stats.insights.topKeywords[0]?.keyword, 'ambient');
    assert.equal(stats.insights.topKeywords[0]?.frequency, 2);
    assert.ok(stats.insights.skipRate > 0.32 && stats.insights.skipRate < 0.34);

    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore database stats cap artists to three and expose more tags for the two-row dashboard', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    const tracks = [
      { title: 'One', artist: 'Artist A', ytVideoId: 'a', tags: ['ambient'], plays: 4 },
      { title: 'Two', artist: 'Artist B', ytVideoId: 'b', tags: ['piano'], plays: 3 },
      { title: 'Three', artist: 'Artist C', ytVideoId: 'c', tags: ['jazz'], plays: 2 },
      { title: 'Four', artist: 'Artist D', ytVideoId: 'd', tags: ['electronic'], plays: 1 },
    ];

    for (const track of tracks) {
      for (let index = 0; index < track.plays; index += 1) {
        store.recordPlay(createTrack({
          title: track.title,
          artist: track.artist,
          ytVideoId: track.ytVideoId,
        }));
      }
      store.updateTrackTags(normalizeTrackId(track.artist, track.title), track.tags);
    }

    const stats = store.getDatabaseStats();
    assert.equal(stats.insights.plays7d, 10);
    assert.equal(stats.insights.tracks7d, 4);
    assert.equal(stats.insights.topArtists.length, 3);
    assert.equal(stats.insights.topKeywords.length, 4);
    assert.deepEqual(stats.insights.topArtists.map((item) => item.artist), ['Artist A', 'Artist B', 'Artist C']);
    assert.deepEqual(stats.insights.topKeywords.map((item) => item.keyword), ['ambient', 'piano', 'jazz', 'electronic']);

    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore dashboard metrics only include the recent 7-day window', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    const now = Date.now();
    const eightDaysAgo = now - (8 * 24 * 60 * 60 * 1000);
    const twoDaysAgo = now - (2 * 24 * 60 * 60 * 1000);
    const yesterday = now - (24 * 60 * 60 * 1000);

    const oldPlay = store.recordPlay(createTrack({ title: 'Old Track', artist: 'Old Artist', ytVideoId: 'old' }));
    const recentAmbient = store.recordPlay(createTrack({ title: 'Recent One', artist: 'Recent Artist', ytVideoId: 'recent-1' }));
    const recentAmbient2 = store.recordPlay(createTrack({ title: 'Recent One', artist: 'Recent Artist', ytVideoId: 'recent-2' }));
    const recentJazz = store.recordPlay(createTrack({ title: 'Recent Two', artist: 'Another Artist', ytVideoId: 'recent-3' }));

    store.getDatabase().prepare('UPDATE plays SET started_at = ? WHERE id = ?').run(eightDaysAgo, oldPlay);
    store.getDatabase().prepare('UPDATE plays SET started_at = ? WHERE id = ?').run(twoDaysAgo, recentAmbient);
    store.getDatabase().prepare('UPDATE plays SET started_at = ? WHERE id = ?').run(yesterday, recentAmbient2);
    store.getDatabase().prepare('UPDATE plays SET started_at = ? WHERE id = ?').run(now, recentJazz);

    store.updateTrackTags(normalizeTrackId('Old Artist', 'Old Track'), ['legacy']);
    store.updateTrackTags(normalizeTrackId('Recent Artist', 'Recent One'), ['ambient']);
    store.updateTrackTags(normalizeTrackId('Another Artist', 'Recent Two'), ['jazz']);

    const stats = store.getDatabaseStats();

    assert.deepEqual(stats.counts, { plays: 4, tracks: 3, providerCache: 0 });
    assert.equal(stats.insights.plays7d, 3);
    assert.equal(stats.insights.tracks7d, 2);
    assert.deepEqual(stats.insights.topArtists.map((item) => item.artist), ['Recent Artist', 'Another Artist']);
    assert.deepEqual(stats.insights.topKeywords.map((item) => item.keyword), ['ambient', 'jazz']);

    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore full reset preserves persona state', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    store.recordPlay(createTrack());
    store.savePersonaTasteText('Keep me');
    store.getDatabase().prepare(`
      INSERT INTO provider_cache (cache_key, response_json, fetched_at)
      VALUES ('apple:test', '{}', 123)
    `).run();

    const reset = store.fullReset();
    assert.deepEqual(reset.removed, { plays: 1, tracks: 1, providerCache: 1 });
    assert.equal(store.getPersonaTasteText(), 'Keep me');
    assert.deepEqual(store.getDatabaseStats().counts, { plays: 0, tracks: 0, providerCache: 0 });
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('HistoryStore throws after close', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    store.recordPlay(createTrack());
    store.close();
    assert.throws(() => store.getRecent());
  } finally {
    cleanupDb(dbPath);
  }
});
```

## File: `src/history/history-store.ts`
```typescript
// SQLite-backed play history store — tracks, plays, session state, and cleanup operations.

import Database from 'better-sqlite3';
import fs from 'fs';
import path from 'path';
import { getHistoryDbPath } from '../runtime/runtime-data-paths.js';
import { normalizeTrackId } from './history-schema.js';
import {
  clearHistoryData,
  clearProviderCacheData,
  fullResetData,
  getHistoryDatabaseStats,
  type HistoryCleanupResult as MaintenanceHistoryCleanupResult,
  type HistoryDatabaseStats as MaintenanceHistoryDatabaseStats,
} from './history-store-maintenance.js';
import { applyHistoryStoreMigrations } from './history-store-migrations.js';

export interface HistoryDatabaseInsights {
  plays7d: number;
  tracks7d: number;
  skipRate: number;
  activity7d: Array<{ dayLabel: string; plays: number }>;
  topArtists: Array<{ artist: string; plays: number }>;
  topKeywords: Array<{ keyword: string; frequency: number }>;
}

export interface HistoryDatabaseStats extends MaintenanceHistoryDatabaseStats {
  insights: HistoryDatabaseInsights;
}

export interface HistoryCleanupResult {
  stats: HistoryDatabaseStats;
  removed: MaintenanceHistoryCleanupResult['removed'];
}

export interface TrackRecord {
  id: string;
  title: string;
  artist: string;
  duration_sec: number;
  thumbnail: string;
  tags_json: string;
  yt_video_id: string;
  first_played_at: number;
  play_count: number;
}

export interface TrackInput {
  title: string;
  artist: string;
  duration: number;
  thumbnail: string;
  ytVideoId: string;
}

export interface CanonicalOverride {
  artist: string;
  title: string;
}

export interface PlayContext {
  context?: string;
  source?: string;
  [key: string]: unknown;
}

export interface BatchTrackStats {
  trackId: string;
  playCount: number;
  avgCompletion: number;
  skipRate: number;
  hoursSinceLastPlay: number;
}

const SHORT_WEEKDAY_FORMATTER = new Intl.DateTimeFormat('en-US', { weekday: 'short' });

export class HistoryStore {
  private readonly db: Database.Database;

  constructor(private readonly dbPath: string) {
    fs.mkdirSync(path.dirname(dbPath), { recursive: true });
    this.db = new Database(dbPath);
    this.db.pragma('journal_mode = WAL');
    applyHistoryStoreMigrations(this.db);
  }

  recordPlay(track: TrackInput, context?: PlayContext, canonicalOverride?: CanonicalOverride): number {
    const artist = canonicalOverride?.artist ?? track.artist;
    const title = canonicalOverride?.title ?? track.title;
    const trackId = normalizeTrackId(artist, title);
    const now = Date.now();

    this.db.prepare(`
      INSERT INTO tracks (id, title, artist, duration_sec, thumbnail, yt_video_id, first_played_at, play_count)
      VALUES (?, ?, ?, ?, ?, ?, ?, 1)
      ON CONFLICT(id) DO UPDATE SET
        play_count = play_count + 1,
        duration_sec = excluded.duration_sec,
        thumbnail = excluded.thumbnail,
        yt_video_id = CASE WHEN excluded.yt_video_id != '' THEN excluded.yt_video_id ELSE yt_video_id END
    `).run(trackId, title, artist, track.duration, track.thumbnail, track.ytVideoId, now);

    const result = this.db.prepare(`
      INSERT INTO plays (track_id, started_at, context_json)
      VALUES (?, ?, ?)
    `).run(trackId, now, JSON.stringify(context ?? {}));

    return Number(result.lastInsertRowid);
  }

  updateTrackCanonical(trackId: string, canonical: CanonicalOverride): void {
    this.db.prepare(`
      UPDATE tracks SET artist = ?, title = ? WHERE id = ?
    `).run(canonical.artist, canonical.title, trackId);
  }

  updatePlay(playId: number, updates: { played_sec?: number; skipped?: boolean }): void {
    const sets: string[] = [];
    const params: number[] = [];
    if (updates.played_sec !== undefined) {
      sets.push('played_sec = ?');
      params.push(updates.played_sec);
    }
    if (updates.skipped !== undefined) {
      sets.push('skipped = ?');
      params.push(updates.skipped ? 1 : 0);
    }
    if (sets.length === 0) return;
    params.push(playId);
    this.db.prepare(`UPDATE plays SET ${sets.join(', ')} WHERE id = ?`).run(...params);
  }

  getTrackTags(trackId: string): string[] {
    const row = this.db.prepare('SELECT tags_json FROM tracks WHERE id = ?').get(trackId) as
      | { tags_json: string }
      | undefined;
    if (!row) return [];
    try {
      return JSON.parse(row.tags_json);
    } catch {
      return [];
    }
  }

  getRecent(limit = 20, query?: string): Array<TrackRecord & { started_at: number; played_sec: number; skipped: number }> {
    const baseQuery = `
      SELECT t.*, p.started_at, p.played_sec, p.skipped
      FROM plays p
      JOIN tracks t ON t.id = p.track_id
      ${query ? 'WHERE t.title LIKE ? OR t.artist LIKE ?' : ''}
      ORDER BY p.started_at DESC
      LIMIT ?
    `;

    if (query) {
      const pattern = `%${query}%`;
      return this.db.prepare(baseQuery).all(pattern, pattern, limit) as Array<
        TrackRecord & { started_at: number; played_sec: number; skipped: number }
      >;
    }
    return this.db.prepare(baseQuery).all(limit) as Array<
      TrackRecord & { started_at: number; played_sec: number; skipped: number }
    >;
  }

  getTrackStats(trackId: string): { playCount: number; avgCompletion: number; skipRate: number } {
    const track = this.db.prepare('SELECT duration_sec, play_count FROM tracks WHERE id = ?')
      .get(trackId) as { duration_sec: number; play_count: number } | undefined;
    if (!track || track.play_count === 0) {
      return { playCount: 0, avgCompletion: 0, skipRate: 0 };
    }

    const stats = this.db.prepare(`
      SELECT
        COUNT(*) as total,
        AVG(CASE WHEN ? > 0 THEN CAST(played_sec AS REAL) / ? ELSE 0 END) as avg_completion,
        SUM(CASE WHEN skipped = 1 THEN 1 ELSE 0 END) as skip_count
      FROM plays WHERE track_id = ?
    `).get(track.duration_sec, track.duration_sec, trackId) as {
      total: number;
      avg_completion: number;
      skip_count: number;
    };

    return {
      playCount: track.play_count,
      avgCompletion: Math.min(1, stats.avg_completion ?? 0),
      skipRate: stats.total > 0 ? stats.skip_count / stats.total : 0,
    };
  }

  batchGetTrackStats(trackIds: string[]): Map<string, BatchTrackStats> {
    const uniqueTrackIds = [...new Set(trackIds)];
    if (uniqueTrackIds.length === 0) return new Map();

    const placeholders = uniqueTrackIds.map(() => '?').join(', ');
    const trackRows = this.db.prepare(`
      SELECT id, play_count, duration_sec
      FROM tracks
      WHERE id IN (${placeholders})
    `).all(...uniqueTrackIds) as Array<{ id: string; play_count: number; duration_sec: number }>;

    const trackMap = new Map(trackRows.map((row) => [row.id, row]));
    const statsRows = this.db.prepare(`
      SELECT
        p.track_id as trackId,
        COUNT(*) as total,
        AVG(
          CASE WHEN t.duration_sec > 0
            THEN MIN(1.0, CAST(p.played_sec AS REAL) / t.duration_sec)
            ELSE 0
          END
        ) as avgCompletion,
        AVG(CASE WHEN p.skipped = 1 THEN 1.0 ELSE 0 END) as skipRate,
        MAX(p.started_at) as lastPlayedAt
      FROM plays p
      JOIN tracks t ON t.id = p.track_id
      WHERE p.track_id IN (${placeholders})
      GROUP BY p.track_id
    `).all(...uniqueTrackIds) as Array<{
      trackId: string;
      total: number;
      avgCompletion: number | null;
      skipRate: number | null;
      lastPlayedAt: number | null;
    }>;

    const statsMap = new Map(statsRows.map((row) => [row.trackId, row]));
    const now = Date.now();
    const batchStats = new Map<string, BatchTrackStats>();

    for (const trackId of uniqueTrackIds) {
      const track = trackMap.get(trackId);
      const stats = statsMap.get(trackId);
      batchStats.set(trackId, {
        trackId,
        playCount: track?.play_count ?? 0,
        avgCompletion: Math.min(1, stats?.avgCompletion ?? 0),
        skipRate: stats?.skipRate ?? 0,
        hoursSinceLastPlay: stats?.lastPlayedAt
          ? (now - stats.lastPlayedAt) / (1000 * 60 * 60)
          : Infinity,
      });
    }

    return batchStats;
  }

  getTopTracks(limit = 10): TrackRecord[] {
    return this.db.prepare(`
      SELECT * FROM tracks
      WHERE play_count > 0
      ORDER BY play_count DESC
      LIMIT ?
    `).all(limit) as TrackRecord[];
  }

  getTrackPlayCount(artist: string, title: string): number {
    const trackId = normalizeTrackId(artist, title);
    const row = this.db.prepare('SELECT play_count FROM tracks WHERE id = ?')
      .get(trackId) as { play_count: number } | undefined;
    return row?.play_count ?? 0;
  }

  hoursSinceLastPlay(artist: string, title: string): number {
    const trackId = normalizeTrackId(artist, title);
    const row = this.db.prepare(`
      SELECT MAX(started_at) as last_at FROM plays WHERE track_id = ?
    `).get(trackId) as { last_at: number | null } | undefined;
    if (!row?.last_at) return Infinity;
    return (Date.now() - row.last_at) / (1000 * 60 * 60);
  }

  getTopArtists(limit = 10): Array<{ artist: string; plays: number; avgCompletion: number }> {
    return this.db.prepare(`
      SELECT t.artist, COUNT(p.id) as plays,
        AVG(CASE WHEN t.duration_sec > 0
          THEN MIN(1.0, CAST(p.played_sec AS REAL) / t.duration_sec) ELSE 0 END) as avgCompletion
      FROM plays p
      JOIN tracks t ON t.id = p.track_id
      GROUP BY LOWER(t.artist)
      ORDER BY plays DESC
      LIMIT ?
    `).all(limit) as Array<{ artist: string; plays: number; avgCompletion: number }>;
  }

  getTopTags(limit = 10): Array<{ tag: string; frequency: number }> {
    const rows = this.db.prepare(`
      SELECT tags_json, play_count FROM tracks
      WHERE tags_json != '[]' AND play_count > 0
      ORDER BY play_count DESC
      LIMIT 50
    `).all() as Array<{ tags_json: string; play_count: number }>;

    const freq: Record<string, number> = {};
    for (const row of rows) {
      try {
        const tags: string[] = JSON.parse(row.tags_json);
        for (const tag of tags) {
          freq[tag.toLowerCase()] = (freq[tag.toLowerCase()] ?? 0) + row.play_count;
        }
      } catch {
        // Ignore malformed tag payloads.
      }
    }

    return Object.entries(freq)
      .sort((a, b) => b[1] - a[1])
      .slice(0, limit)
      .map(([tag, frequency]) => ({ tag, frequency }));
  }

  getRecentPlaysDetailed(limit = 20): Array<{
    title: string;
    artist: string;
    completion: number;
    skipped: boolean;
    playedAt: number;
    tags: string[];
  }> {
    const rows = this.db.prepare(`
      SELECT t.title, t.artist, t.duration_sec, t.tags_json,
        p.played_sec, p.skipped, p.started_at
      FROM plays p
      JOIN tracks t ON t.id = p.track_id
      ORDER BY p.started_at DESC
      LIMIT ?
    `).all(limit) as Array<{
      title: string;
      artist: string;
      duration_sec: number;
      tags_json: string;
      played_sec: number;
      skipped: number;
      started_at: number;
    }>;

    return rows.map((row) => ({
      title: row.title,
      artist: row.artist,
      completion: row.duration_sec > 0 ? Math.min(1, row.played_sec / row.duration_sec) : 0,
      skipped: row.skipped === 1,
      playedAt: row.started_at,
      tags: parseJsonArray(row.tags_json),
    }));
  }

  getPersonaTasteText(): string {
    const row = this.db.prepare('SELECT persona_taste_text FROM session_state WHERE id = 1')
      .get() as { persona_taste_text: string } | undefined;
    return row?.persona_taste_text ?? '';
  }

  savePersonaTasteText(text: string): void {
    this.db.prepare(`
      INSERT INTO session_state (id, persona_taste_text) VALUES (1, ?)
      ON CONFLICT(id) DO UPDATE SET persona_taste_text = excluded.persona_taste_text
    `).run(text);
  }

  getDatabaseStats(): HistoryDatabaseStats {
    const recentWindow = this.getRecentDashboardCounts(7);
    return {
      ...getHistoryDatabaseStats(this.db, this.dbPath),
      insights: {
        plays7d: recentWindow.plays,
        tracks7d: recentWindow.tracks,
        skipRate: this.getSkipRateMetric(),
        activity7d: this.getPlayActivity(7),
        topArtists: this.getTopArtistsInWindow(7, 3).map((artist) => ({
          artist: artist.artist,
          plays: artist.plays,
        })),
        topKeywords: this.getTopTagsInWindow(7, 12).map((keyword) => ({
          keyword: keyword.tag,
          frequency: keyword.frequency,
        })),
      },
    };
  }

  clearHistory(): HistoryCleanupResult {
    const result = clearHistoryData(this.db, this.dbPath);
    return {
      removed: result.removed,
      stats: this.getDatabaseStats(),
    };
  }

  clearProviderCache(): HistoryCleanupResult {
    const result = clearProviderCacheData(this.db, this.dbPath);
    return {
      removed: result.removed,
      stats: this.getDatabaseStats(),
    };
  }

  fullReset(): HistoryCleanupResult {
    const result = fullResetData(this.db, this.dbPath);
    return {
      removed: result.removed,
      stats: this.getDatabaseStats(),
    };
  }

  getDatabase(): Database.Database {
    return this.db;
  }

  getDatabasePath(): string {
    return this.dbPath;
  }

  updateTrackTags(trackId: string, tags: string[]): void {
    this.db.prepare('UPDATE tracks SET tags_json = ? WHERE id = ?')
      .run(JSON.stringify(tags), trackId);
  }

  close(): void {
    this.db.close();
  }

  private getSkipRateMetric(): number {
    const row = this.db.prepare(`
      SELECT
        AVG(CASE WHEN p.skipped = 1 THEN 1.0 ELSE 0 END) as skip_rate
      FROM plays p
      JOIN tracks t ON t.id = p.track_id
    `).get() as { skip_rate: number | null };

    return clampUnit(row?.skip_rate ?? 0);
  }

  private getRecentDashboardCounts(days: number): { plays: number; tracks: number } {
    const row = this.db.prepare(`
      SELECT
        COUNT(*) as plays,
        COUNT(DISTINCT track_id) as tracks
      FROM plays
      WHERE started_at >= ?
    `).get(this.getRecentWindowStart(days)) as { plays: number | null; tracks: number | null };

    return {
      plays: row?.plays ?? 0,
      tracks: row?.tracks ?? 0,
    };
  }

  private getTopArtistsInWindow(days: number, limit: number): Array<{ artist: string; plays: number }> {
    return this.db.prepare(`
      SELECT t.artist, COUNT(p.id) as plays
      FROM plays p
      JOIN tracks t ON t.id = p.track_id
      WHERE p.started_at >= ?
      GROUP BY LOWER(t.artist)
      ORDER BY plays DESC
      LIMIT ?
    `).all(this.getRecentWindowStart(days), limit) as Array<{ artist: string; plays: number }>;
  }

  private getTopTagsInWindow(days: number, limit: number): Array<{ tag: string; frequency: number }> {
    const rows = this.db.prepare(`
      SELECT t.tags_json
      FROM plays p
      JOIN tracks t ON t.id = p.track_id
      WHERE p.started_at >= ?
      ORDER BY p.started_at DESC
    `).all(this.getRecentWindowStart(days)) as Array<{ tags_json: string }>;

    const freq: Record<string, number> = {};
    for (const row of rows) {
      try {
        const tags: string[] = JSON.parse(row.tags_json);
        for (const tag of tags) {
          freq[tag.toLowerCase()] = (freq[tag.toLowerCase()] ?? 0) + 1;
        }
      } catch {
        // Ignore malformed tag payloads.
      }
    }

    return Object.entries(freq)
      .sort((a, b) => b[1] - a[1])
      .slice(0, limit)
      .map(([tag, frequency]) => ({ tag, frequency }));
  }

  private getPlayActivity(days: number): Array<{ dayLabel: string; plays: number }> {
    const dayBuckets = buildRecentDayBuckets(days);
    const playsByDay = new Map(dayBuckets.map((bucket) => [bucket.key, 0]));
    const rows = this.db.prepare(`
      SELECT started_at
      FROM plays
      WHERE started_at >= ?
      ORDER BY started_at ASC
    `).all(dayBuckets[0]?.start ?? 0) as Array<{ started_at: number }>;

    for (const row of rows) {
      const key = toLocalDateKey(new Date(row.started_at));
      if (playsByDay.has(key)) {
        playsByDay.set(key, (playsByDay.get(key) ?? 0) + 1);
      }
    }

    return dayBuckets.map((bucket) => ({
      dayLabel: SHORT_WEEKDAY_FORMATTER.format(bucket.date),
      plays: playsByDay.get(bucket.key) ?? 0,
    }));
  }

  private getRecentWindowStart(days: number): number {
    return buildRecentDayBuckets(days)[0]?.start ?? 0;
  }
}

function parseJsonArray(raw: string): string[] {
  try {
    return JSON.parse(raw);
  } catch {
    return [];
  }
}

function buildRecentDayBuckets(days: number): Array<{ date: Date; key: string; start: number }> {
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const buckets: Array<{ date: Date; key: string; start: number }> = [];
  for (let offset = days - 1; offset >= 0; offset -= 1) {
    const date = new Date(today);
    date.setDate(today.getDate() - offset);
    buckets.push({
      date,
      key: toLocalDateKey(date),
      start: date.getTime(),
    });
  }

  return buckets;
}

function toLocalDateKey(date: Date): string {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

function clampUnit(value: number): number {
  return Math.max(0, Math.min(1, Number.isFinite(value) ? value : 0));
}

let historyStore: HistoryStore | null = null;

export function createHistoryStore(): HistoryStore {
  if (!historyStore) {
    const dbPath = getHistoryDbPath();
    historyStore = new HistoryStore(dbPath);
    console.error(`[agentune] History DB initialized at ${dbPath}`);
  }
  return historyStore;
}

export function getHistoryStore(): HistoryStore | null {
  return historyStore;
}
```

## File: `src/mcp/mcp-server.ts`
```typescript
// MCP server setup — registers tools and handles agent communication via stdio or HTTP

import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { randomUUID } from "crypto";
import { type IncomingMessage, type ServerResponse } from "http";
import { z } from "zod";
import {
  handleAddSong,
  handlePlaySong,
  handleDiscover,
  handlePause,
  handleResume,
  handleSkip,
  handleQueueList,
  handleNowPlaying,
  handleVolume,
  handleHistory,
  handleGetSessionState,
  handleUpdatePersona,
} from "./tool-handlers.js";

/** Register all MCP tools onto a server instance */
export function registerMcpTools(server: McpServer): void {
  server.tool(
    "play_song",
    "Play a specific song immediately using title and artist. " +
    "Apple Search API is used first to clean up the canonical song identity, then YouTube resolves a playable version. " +
    "This replaces the current song right away.",
    {
      title: z.string().min(1).describe("Song title"),
      artist: z.string().optional().describe("Artist name — strongly recommended for accuracy"),
    },
    async (args) => handlePlaySong(args),
  );

  server.tool(
    "add_song",
    "Add a specific song to the queue using title and artist. " +
    "Apple Search API is used first to clean up the canonical song identity, then YouTube is used only to resolve a playable version. " +
    "If nothing is currently playing, the queued song starts automatically.",
    {
      title: z.string().min(1).describe("Song title"),
      artist: z.string().optional().describe("Artist name — strongly recommended for accuracy"),
    },
    async (args) => handleAddSong(args),
  );

  server.tool(
    "discover",
    "Get song suggestions from the current listener state. " +
    "Start with page=1 for a new search. Prefer a specific artist when the user names one. " +
    "Use short, concrete keywords instead of long natural-language prompts. " +
    "When the response includes nextGuide telling you to change page, keep the same input and increment page. " +
    "When nextGuide tells you to improve input, change artist or keywords. " +
    "Deprecated mode and intent inputs are ignored.",
    {
      page: z.number().int().min(1).optional().default(1)
        .describe("Page number for the current discover snapshot. Use page=1 for a new search."),
      limit: z.number().int().min(1).max(50).optional().default(10)
        .describe("Results per page (default 10, max 50)"),
      artist: z.string().max(200).optional()
        .describe("Best seed when the user names a specific artist."),
      keywords: z.array(z.string().max(100)).max(10).optional()
        .describe("Short seed keywords for style, genre, mood, or language hints (max 10)."),
      mode: z.string().optional().describe("Deprecated — ignored."),
      intent: z.unknown().optional().describe("Deprecated — ignored."),
    },
    async (args) => handleDiscover(args),
  );

  server.tool("pause", "Pause the currently playing track", {}, async () => handlePause());
  server.tool("resume", "Resume playback of a paused track", {}, async () => handleResume());
  server.tool("skip", "Skip to the next track in the queue", {}, async () => handleSkip());

  server.tool(
    "queue_list",
    "List all tracks currently in the play queue and the current now-playing track",
    {},
    async () => handleQueueList(),
  );

  server.tool(
    "now_playing",
    "Get info about the currently playing track",
    {},
    async () => handleNowPlaying(),
  );

  server.tool(
    "volume",
    "Get or set the playback volume (0-100)",
    {
      level: z.number().min(0).max(100).optional().describe("Volume level 0-100. Omit to get current volume."),
    },
    async (args) => handleVolume(args),
  );

  server.tool(
    "history",
    "View your listening history. Shows recently played tracks with play counts and skip rates. Use this to understand listening patterns before choosing what to play next.",
    {
      limit: z.number().min(1).max(50).optional().default(20).describe("Max results to return (1-50)"),
      query: z.string().optional().describe("Filter by track title or artist name"),
    },
    async (args) => handleHistory(args),
  );

  server.tool(
    "get_session_state",
    "Read the current listener state before choosing music. " +
    "Use this as the source of truth for agent decisions. " +
    "Returns time context, persona.Preferences, recent plays, top artists, and top keywords. " +
    "Read these fields first, then choose a specific artist or concrete keywords for discover(). " +
    "Do not infer hidden preferences beyond the returned state.",
    {},
    async () => handleGetSessionState(),
  );

  server.tool(
    "update_persona",
    "Update the listener's music taste description only. Call this when the user explicitly mentions " +
    "a music preference, or when you want to record taste insights learned from listening patterns. " +
    "The taste text is free-form natural language describing what genres, artists, moods, and " +
    "styles the listener prefers. This persists across sessions.",
    {
      taste: z.string().max(1000).describe(
        "Free text taste description, e.g. 'Likes ambient, piano, post-rock. Evenings prefer acoustic.'. Use an empty string to clear it."
      ),
    },
    async (args) => handleUpdatePersona(args),
  );
}

/** Create MCP server with stdio transport (legacy/direct mode) */
export async function createStdioMcpServer(): Promise<McpServer> {
  const server = new McpServer({ name: "agentune", version: "0.1.0" });
  registerMcpTools(server);
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("[agentune] MCP server started on stdio");
  return server;
}

// --- HTTP MCP handler ---

function isInitializeRequest(body: unknown): boolean {
  if (Array.isArray(body)) {
    return body.some((msg) => (msg as Record<string, unknown>)?.method === 'initialize');
  }
  return (body as Record<string, unknown>)?.method === 'initialize';
}

const MAX_SESSIONS = 100;
const SESSION_TTL_MS = 30 * 60 * 1000; // 30 minutes

/** Create an HTTP MCP handler for daemon mode — manages per-session transports */
export function createHttpMcpHandler(): {
  handleRequest: (req: IncomingMessage, res: ServerResponse, body?: unknown) => Promise<void>;
  close: () => Promise<void>;
} {
  const sessions = new Map<string, StreamableHTTPServerTransport>();
  const lastActivity = new Map<string, number>();

  // Periodic sweep: remove sessions idle beyond TTL
  const sweepInterval = setInterval(() => {
    const now = Date.now();
    for (const [sid, timestamp] of lastActivity) {
      if (now - timestamp > SESSION_TTL_MS) {
        const transport = sessions.get(sid);
        if (transport) transport.close().catch(() => {});
        sessions.delete(sid);
        lastActivity.delete(sid);
      }
    }
  }, 60_000);
  sweepInterval.unref(); // Don't keep process alive for cleanup

  return {
    async handleRequest(req, res, body) {
      const sessionId = req.headers['mcp-session-id'] as string | undefined;

      if (req.method === 'POST' && !sessionId && isInitializeRequest(body)) {
        // New session — create transport + server
        // Evict oldest session if at capacity
        if (sessions.size >= MAX_SESSIONS) {
          let oldestSid: string | undefined;
          let oldestTime = Infinity;
          for (const [sid, ts] of lastActivity) {
            if (ts < oldestTime) { oldestTime = ts; oldestSid = sid; }
          }
          if (oldestSid) {
            const old = sessions.get(oldestSid);
            if (old) old.close().catch(() => {});
            sessions.delete(oldestSid);
            lastActivity.delete(oldestSid);
          }
        }

        const transport = new StreamableHTTPServerTransport({
          sessionIdGenerator: () => randomUUID(),
          onsessioninitialized: (sid) => {
            sessions.set(sid, transport);
            lastActivity.set(sid, Date.now());
          },
        });
        transport.onclose = () => {
          const sid = transport.sessionId;
          if (sid) {
            sessions.delete(sid);
            lastActivity.delete(sid);
          }
        };
        try {
          const server = new McpServer({ name: 'agentune', version: '0.1.0' });
          registerMcpTools(server);
          await server.connect(transport);
          await transport.handleRequest(req, res, body);
        } catch (err) {
          await transport.close().catch(() => {});
          if (!res.headersSent) {
            res.writeHead(500, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({ error: 'Failed to create session' }));
          }
        }
      } else if (sessionId && sessions.has(sessionId)) {
        lastActivity.set(sessionId, Date.now());
        await sessions.get(sessionId)!.handleRequest(req, res, body);
      } else if (req.method === 'POST' && sessionId && !sessions.has(sessionId)) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid or expired session' }));
      } else if (req.method === 'POST') {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Missing session ID or initialize request' }));
      } else {
        res.writeHead(405);
        res.end('Method Not Allowed');
      }
    },
    async close() {
      clearInterval(sweepInterval);
      for (const [sid, transport] of sessions) {
        await transport.close();
        sessions.delete(sid);
        lastActivity.delete(sid);
      }
    },
  };
}
```

## File: `src/mcp/song-resolver.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
import { resolveSong } from './song-resolver.js';

class FakeAppleProvider {
  constructor(
    private readonly searchResults: Array<{
      title: string;
      artist: string;
      album: string;
      genre: string;
      durationMs: number;
      artwork: string;
    }> = [],
    private readonly artistTracks: Array<{
      title: string;
      artist: string;
      album: string;
      genre: string;
      durationMs: number;
      artwork: string;
    }> = [],
  ) {}

  async searchTracks(): Promise<typeof this.searchResults> {
    return this.searchResults;
  }

  async getArtistTracks(): Promise<typeof this.artistTracks> {
    return this.artistTracks;
  }
}

class FakeYouTubeProvider {
  public queries: string[] = [];

  constructor(
    private readonly responses: Record<string, Array<{
      id: string;
      title: string;
      artist: string;
      duration: string;
      durationMs: number;
      thumbnail: string;
      url: string;
    }>>,
    private readonly failingQueries: Set<string> = new Set(),
  ) {}

  async search(query: string): Promise<Array<{
    id: string;
    title: string;
    artist: string;
    duration: string;
    durationMs: number;
    thumbnail: string;
    url: string;
  }>> {
    this.queries.push(query);
    if (this.failingQueries.has(query)) {
      throw new Error(`query failed: ${query}`);
    }
    return this.responses[query] ?? [];
  }
}

test('resolveSong prefers Apple canonical metadata before YouTube resolve', async () => {
  const apple = new FakeAppleProvider([
    {
      title: 'Blinding Lights',
      artist: 'The Weeknd',
      album: 'After Hours',
      genre: 'Pop',
      durationMs: 200000,
      artwork: '',
    },
  ]);
  const youtube = new FakeYouTubeProvider({
    'The Weeknd - Blinding Lights official audio': [{
      id: 'yt-1',
      title: 'The Weeknd - Blinding Lights (Official Audio)',
      artist: 'The Weeknd',
      duration: '3:20',
      durationMs: 200000,
      thumbnail: 'thumb',
      url: 'https://youtube.test/yt-1',
    }],
    'The Weeknd Blinding Lights': [],
  });

  const resolved = await resolveSong(
    youtube as never,
    apple as never,
    { title: 'Blinding Lights', artist: 'The Weeknd' },
  );

  assert.equal(resolved.matched, true);
  assert.equal(resolved.canonicalTitle, 'Blinding Lights');
  assert.equal(resolved.canonicalArtist, 'The Weeknd');
  assert.equal(resolved.canonicalSource, 'apple_search');
  assert.equal(resolved.result?.id, 'yt-1');
});

test('resolveSong falls back to a second YouTube query when the first query throws', async () => {
  const apple = new FakeAppleProvider([
    {
      title: 'Weightless',
      artist: 'Marconi Union',
      album: 'Weightless',
      genre: 'Ambient',
      durationMs: 480000,
      artwork: '',
    },
  ]);
  const youtube = new FakeYouTubeProvider(
    {
      'Marconi Union Weightless': [{
        id: 'yt-2',
        title: 'Marconi Union - Weightless',
        artist: 'Marconi Union',
        duration: '8:00',
        durationMs: 480000,
        thumbnail: 'thumb',
        url: 'https://youtube.test/yt-2',
      }],
    },
    new Set(['Marconi Union - Weightless official audio']),
  );

  const resolved = await resolveSong(
    youtube as never,
    apple as never,
    { title: 'Weightless', artist: 'Marconi Union' },
  );

  assert.equal(resolved.matched, true);
  assert.equal(resolved.result?.id, 'yt-2');
  assert.deepEqual(youtube.queries, [
    'Marconi Union - Weightless official audio',
    'Marconi Union Weightless',
  ]);
});

test('resolveSong skips blocked YouTube variants and keeps the original candidate', async () => {
  const apple = new FakeAppleProvider([
    {
      title: 'Blinding Lights',
      artist: 'The Weeknd',
      album: 'After Hours',
      genre: 'Pop',
      durationMs: 200000,
      artwork: '',
    },
  ]);
  const youtube = new FakeYouTubeProvider({
    'The Weeknd - Blinding Lights official audio': [
      {
        id: 'yt-cover',
        title: 'Blinding Lights Cover',
        artist: 'Cover Singer',
        duration: '3:20',
        durationMs: 200000,
        thumbnail: 'thumb',
        url: 'https://youtube.test/yt-cover',
      },
      {
        id: 'yt-karaoke',
        title: 'Blinding Lights',
        artist: 'Karaoke Hits',
        duration: '3:20',
        durationMs: 200000,
        thumbnail: 'thumb',
        url: 'https://youtube.test/yt-karaoke',
      },
      {
        id: 'yt-original',
        title: 'The Weeknd - Blinding Lights (Official Audio)',
        artist: 'The Weeknd',
        duration: '3:20',
        durationMs: 200000,
        thumbnail: 'thumb',
        url: 'https://youtube.test/yt-original',
      },
    ],
    'The Weeknd Blinding Lights': [],
  });

  const resolved = await resolveSong(
    youtube as never,
    apple as never,
    { title: 'Blinding Lights', artist: 'The Weeknd' },
  );

  assert.equal(resolved.matched, true);
  assert.equal(resolved.result?.id, 'yt-original');
  assert.deepEqual(resolved.alternatives, []);
});

test('resolveSong returns unmatched when every YouTube candidate is blocked', async () => {
  const apple = new FakeAppleProvider([
    {
      title: 'Blinding Lights',
      artist: 'The Weeknd',
      album: 'After Hours',
      genre: 'Pop',
      durationMs: 200000,
      artwork: '',
    },
  ]);
  const youtube = new FakeYouTubeProvider({
    'The Weeknd - Blinding Lights official audio': [
      {
        id: 'yt-cover',
        title: 'Blinding Lights Cover',
        artist: 'Cover Singer',
        duration: '3:20',
        durationMs: 200000,
        thumbnail: 'thumb',
        url: 'https://youtube.test/yt-cover',
      },
    ],
    'The Weeknd Blinding Lights': [
      {
        id: 'yt-live',
        title: 'Blinding Lights Live',
        artist: 'The Weeknd',
        duration: '3:20',
        durationMs: 200000,
        thumbnail: 'thumb',
        url: 'https://youtube.test/yt-live',
      },
      {
        id: 'yt-karaoke',
        title: 'Blinding Lights',
        artist: 'Karaoke Hits',
        duration: '3:20',
        durationMs: 200000,
        thumbnail: 'thumb',
        url: 'https://youtube.test/yt-karaoke',
      },
    ],
  });

  const resolved = await resolveSong(
    youtube as never,
    apple as never,
    { title: 'Blinding Lights', artist: 'The Weeknd' },
  );

  assert.equal(resolved.matched, false);
  assert.equal(resolved.matchScore, 0);
  assert.deepEqual(resolved.alternatives, []);
});

test('resolveSong still resolves explicit variant queries when the keyword is requested', async () => {
  const youtube = new FakeYouTubeProvider({
    'Ed Sheeran - Shape of You Cover official audio': [],
    'Ed Sheeran Shape of You Cover': [
      {
        id: 'yt-cover',
        title: 'Shape of You Cover',
        artist: 'Ed Sheeran Studio Duo',
        duration: '3:45',
        durationMs: 225000,
        thumbnail: 'thumb',
        url: 'https://youtube.test/yt-cover',
      },
    ],
  });

  const resolved = await resolveSong(
    youtube as never,
    null,
    { title: 'Shape of You Cover', artist: 'Ed Sheeran' },
  );

  assert.equal(resolved.matched, true);
  assert.equal(resolved.canonicalSource, 'input');
  assert.equal(resolved.result?.id, 'yt-cover');
});
```

## File: `src/mcp/song-resolver.ts`
```typescript
import type { AppleSearchProvider, AppleTrack } from '../providers/apple-search-provider.js';
import { normalizeForQuery } from '../providers/metadata-normalizer.js';
import { scoreSearchResults, type ScoredResult } from '../providers/search-result-scorer.js';
import type { SearchResult, YouTubeProvider } from '../providers/youtube-provider.js';

const APPLE_MIN_SCORE = 0.6;
const YOUTUBE_MIN_SCORE = 0.2;

export interface ResolvedSong {
  matched: boolean;
  canonicalTitle: string;
  canonicalArtist?: string;
  canonicalSource: 'apple_search' | 'apple_artist_tracks' | 'input';
  matchScore: number;
  matchReasons: string[];
  result?: SearchResult;
  alternatives: Array<{
    id: string;
    title: string;
    artist: string;
    score: number;
    reasons: string[];
  }>;
}

interface AppleCandidate {
  title: string;
  artist: string;
  source: 'apple_search' | 'apple_artist_tracks';
  score: number;
}

function normalize(text: string): string {
  return normalizeForQuery(text)
    .toLowerCase()
    .replace(/[^\w\s]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function wordOverlap(a: string, b: string): number {
  const wordsA = new Set(a.split(/\s+/).filter(Boolean));
  const wordsB = new Set(b.split(/\s+/).filter(Boolean));
  if (wordsA.size === 0 || wordsB.size === 0) return 0;

  let hits = 0;
  for (const word of wordsA) {
    if (wordsB.has(word)) hits += 1;
  }
  return hits / Math.max(wordsA.size, wordsB.size);
}

function scoreAppleTrack(track: AppleTrack, title: string, artist?: string): number {
  const normalizedTrackTitle = normalize(track.title);
  const normalizedTitle = normalize(title);
  let score = 0;

  if (normalizedTrackTitle === normalizedTitle) {
    score += 1.0;
  } else if (normalizedTrackTitle.startsWith(normalizedTitle)) {
    score += 0.8;
  } else if (normalizedTrackTitle.includes(normalizedTitle)) {
    score += 0.6;
  } else {
    score += wordOverlap(normalizedTrackTitle, normalizedTitle) * 0.4;
  }

  if (artist) {
    const normalizedArtist = normalize(artist);
    const normalizedTrackArtist = normalize(track.artist);
    if (
      normalizedTrackArtist.includes(normalizedArtist) ||
      normalizedArtist.includes(normalizedTrackArtist)
    ) {
      score += 0.4;
    }
  }

  if (track.durationMs >= 120000 && track.durationMs <= 420000) {
    score += 0.05;
  }

  return Math.round(score * 100) / 100;
}

function dedupeAppleTracks(
  tracks: AppleTrack[],
  source: 'apple_search' | 'apple_artist_tracks',
  title: string,
  artist?: string,
): AppleCandidate[] {
  const seen = new Set<string>();

  return tracks.flatMap((track) => {
    const key = `${normalize(track.artist)}::${normalize(track.title)}`;
    if (seen.has(key)) return [];
    seen.add(key);
    return [{
      title: track.title,
      artist: track.artist,
      source,
      score: scoreAppleTrack(track, title, artist),
    }];
  });
}

async function pickCanonicalTrack(
  title: string,
  artist: string | undefined,
  apple: AppleSearchProvider | null,
): Promise<{
  title: string;
  artist?: string;
  source: 'apple_search' | 'apple_artist_tracks' | 'input';
}> {
  if (!apple) {
    return { title, artist, source: 'input' };
  }

  const scoredCandidates: AppleCandidate[] = [];
  const searchTracks = await apple.searchTracks(artist ? `${artist} ${title}` : title, 8);
  scoredCandidates.push(...dedupeAppleTracks(searchTracks, 'apple_search', title, artist));

  if (artist) {
    const artistTracks = await apple.getArtistTracks(artist, 10);
    scoredCandidates.push(...dedupeAppleTracks(artistTracks, 'apple_artist_tracks', title, artist));
  }

  scoredCandidates.sort((a, b) => b.score - a.score);
  if (scoredCandidates[0] && scoredCandidates[0].score >= APPLE_MIN_SCORE) {
    return {
      title: scoredCandidates[0].title,
      artist: scoredCandidates[0].artist,
      source: scoredCandidates[0].source,
    };
  }

  return { title, artist, source: 'input' };
}

function mergeScoredResults(pools: ScoredResult[][]): ScoredResult[] {
  const bestById = new Map<string, ScoredResult>();

  for (const pool of pools) {
    for (const scored of pool) {
      const previous = bestById.get(scored.result.id);
      if (!previous || scored.score > previous.score) {
        bestById.set(scored.result.id, scored);
      }
    }
  }

  return [...bestById.values()].sort((a, b) => b.score - a.score);
}

async function searchYoutubeWithFallback(
  youtube: YouTubeProvider,
  queries: string[],
  title: string,
  artist?: string,
): Promise<ScoredResult[]> {
  const scoredPools: ScoredResult[][] = [];
  let lastError: Error | null = null;

  for (const query of queries) {
    try {
      const results = await youtube.search(query, 10);
      scoredPools.push(scoreSearchResults(results, title, artist));
    } catch (err) {
      lastError = err as Error;
      console.error(`[agentune] Resolver query failed "${query}": ${lastError.message}`);
    }
  }

  if (scoredPools.length === 0 && lastError) {
    throw lastError;
  }

  return mergeScoredResults(scoredPools);
}

export async function resolveSong(
  youtube: YouTubeProvider,
  apple: AppleSearchProvider | null,
  args: { title: string; artist?: string },
): Promise<ResolvedSong> {
  const canonical = await pickCanonicalTrack(args.title, args.artist, apple);
  const canonicalArtist = canonical.artist ?? args.artist;
  const canonicalTitle = canonical.title;

  const queries = [
    canonicalArtist ? `${canonicalArtist} - ${canonicalTitle} official audio` : `${canonicalTitle} official audio`,
    canonicalArtist ? `${canonicalArtist} ${canonicalTitle}` : canonicalTitle,
    args.artist && args.artist !== canonicalArtist ? `${args.artist} ${args.title}` : '',
  ].filter(Boolean);

  const scored = await searchYoutubeWithFallback(youtube, queries, canonicalTitle, canonicalArtist);
  const best = scored[0];

  if (!best || best.score < YOUTUBE_MIN_SCORE) {
    return {
      matched: false,
      canonicalTitle,
      canonicalArtist,
      canonicalSource: canonical.source,
      matchScore: best?.score ?? 0,
      matchReasons: best?.reasons ?? [],
      alternatives: scored.slice(0, 3).map((item) => ({
        id: item.result.id,
        title: item.result.title,
        artist: item.result.artist,
        score: item.score,
        reasons: item.reasons,
      })),
    };
  }

  return {
    matched: true,
    canonicalTitle,
    canonicalArtist,
    canonicalSource: canonical.source,
    matchScore: best.score,
    matchReasons: best.reasons,
    result: best.result,
    alternatives: scored.slice(1, 4).map((item) => ({
      id: item.result.id,
      title: item.result.title,
      artist: item.result.artist,
      score: item.score,
      reasons: item.reasons,
    })),
  };
}
```

## File: `src/mcp/tool-handlers.ts`
```typescript
// MCP tool handler functions — wired to MpvController for audio, stubs for search/queue (phases 4, 7)

import { getMpvController } from '../audio/mpv-controller.js';
import { getHistoryStore } from '../history/history-store.js';
import { getAppleSearchProvider } from '../providers/apple-search-provider.js';
import { getYoutubeProvider } from '../providers/youtube-provider.js';
import { resolveSong } from './song-resolver.js';
import { getTasteEngine } from '../taste/taste-engine.js';
import { DiscoverBatchBuilder } from '../taste/discover-batch-builder.js';
import { createDiscoverPipeline, getDiscoverPipeline } from '../taste/discover-pipeline.js';
import { invalidateDiscoverCache } from '../taste/discover-pagination-cache.js';
import { getQueuePlaybackController } from '../queue/queue-playback-controller.js';
import { getQueueManager } from '../queue/queue-manager.js';
import { loadRuntimeConfig } from '../runtime/runtime-config.js';
import { getWebServer } from '../web/web-server.js';

export type ToolContent = { type: "text"; text: string };
export type ToolResult = { content: ToolContent[]; isError?: boolean };

function textResult(data: unknown): ToolResult {
  return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
}

function errorResult(message: string): ToolResult {
  return { content: [{ type: "text", text: message }], isError: true };
}

export async function handlePlaySong(args: { title: string; artist?: string }): Promise<ToolResult> {
  try {
    const yt = getYoutubeProvider();
    if (!yt) return errorResult('YouTube provider not initialized.');
    const apple = getAppleSearchProvider();
    const queuePlaybackController = getQueuePlaybackController();
    if (!queuePlaybackController) return errorResult('Queue playback controller not initialized.');

    const resolved = await resolveSong(yt, apple, args);
    if (!resolved.matched || !resolved.result) {
      const label = args.artist ? `"${args.title}" by ${args.artist}` : `"${args.title}"`;
      return textResult({
        matched: false,
        canonical: {
          title: resolved.canonicalTitle,
          artist: resolved.canonicalArtist,
          source: resolved.canonicalSource,
        },
        message: `No good match found for ${label}. Top score: ${resolved.matchScore}.`,
        alternatives: resolved.alternatives,
      });
    }

    const nowPlaying = await queuePlaybackController.replaceCurrentTrack(resolved.result.id, {
      canonicalArtist: resolved.canonicalArtist,
      canonicalTitle: resolved.canonicalTitle,
    });
    invalidateDiscoverCache();

    return textResult({
      matched: true,
      action: 'replaced_current',
      nowPlaying,
      canonical: {
        title: resolved.canonicalTitle,
        artist: resolved.canonicalArtist,
        source: resolved.canonicalSource,
      },
      matchScore: resolved.matchScore,
      matchReasons: resolved.matchReasons,
      alternatives: resolved.alternatives,
      message: `Now playing: ${nowPlaying.title} by ${nowPlaying.artist} (match score: ${resolved.matchScore})`,
    });
  } catch (err) {
    return errorResult(`Play song failed: ${(err as Error).message}`);
  }
}

export async function handleAddSong(args: { title: string; artist?: string }): Promise<ToolResult> {
  try {
    const yt = getYoutubeProvider();
    if (!yt) return errorResult('YouTube provider not initialized.');
    const apple = getAppleSearchProvider();
    const queuePlaybackController = getQueuePlaybackController();
    if (!queuePlaybackController) return errorResult('Queue playback controller not initialized.');

    const resolved = await resolveSong(yt, apple, args);
    if (!resolved.matched || !resolved.result) {
      const label = args.artist ? `"${args.title}" by ${args.artist}` : `"${args.title}"`;
      return textResult({
        matched: false,
        canonical: {
          title: resolved.canonicalTitle,
          artist: resolved.canonicalArtist,
          source: resolved.canonicalSource,
        },
        message: `No good match found for ${label}. Top score: ${resolved.matchScore}.`,
        alternatives: resolved.alternatives,
      });
    }

    const addResult = await queuePlaybackController.addById(resolved.result.id, {
      canonicalArtist: resolved.canonicalArtist,
      canonicalTitle: resolved.canonicalTitle,
    });
    const queueManager = getQueueManager();
    const nowPlaying = queueManager?.getNowPlaying() ?? null;
    invalidateDiscoverCache();

    return textResult({
      matched: true,
      action: addResult.action,
      nowPlaying,
      added: addResult.item,
      queuePosition: addResult.position,
      startedPlayback: addResult.startedPlayback,
      canonical: {
        title: resolved.canonicalTitle,
        artist: resolved.canonicalArtist,
        source: resolved.canonicalSource,
      },
      matchScore: resolved.matchScore,
      matchReasons: resolved.matchReasons,
      alternatives: resolved.alternatives,
      message: addResult.startedPlayback
        ? `Added ${addResult.item.title} by ${addResult.item.artist} to queue at position ${addResult.position} and started playback because the queue was idle.`
        : `Added ${addResult.item.title} by ${addResult.item.artist} to queue at position ${addResult.position}.`,
    });
  } catch (err) {
    return errorResult(`Add song failed: ${(err as Error).message}`);
  }
}

export async function handleDiscover(args: {
  page?: number;
  limit?: number;
  artist?: string;
  keywords?: string[];
  mode?: unknown;
  intent?: unknown;
}): Promise<ToolResult> {
  try {
    const store = getHistoryStore();
    if (!store) return errorResult('History store not initialized.');
    const apple = getAppleSearchProvider();
    if (!apple) return errorResult('Apple provider not initialized.');

    const runtimeConfig = loadRuntimeConfig();
    const pipeline = getDiscoverPipeline() ?? createDiscoverPipeline(
      new DiscoverBatchBuilder(apple, store),
      store,
      runtimeConfig.discoverRanking,
    );
    const result = await pipeline.discover(args);
    const { emptyReason, ...response } = result;

    if (response.candidates.length === 0) {
      return textResult({
        ...response,
        message: emptyReason === 'page_exhausted'
          ? 'No more discover candidates in this snapshot. Change artist/keywords or go back to page=1.'
          : 'No discover candidates found yet. Play more music first, or pass artist/keywords seeds.',
      });
    }

    return textResult(response);
  } catch (err) {
    return errorResult(`Discover failed: ${(err as Error).message}`);
  }
}

export async function handlePause(): Promise<ToolResult> {
  try {
    const mpv = getMpvController();
    if (!mpv || !mpv.isReady()) return errorResult('Audio engine not initialized. Is mpv installed?');
    mpv.pause();
    return textResult({ status: "paused", message: "Playback paused." });
  } catch (err) {
    return errorResult(`Pause failed: ${(err as Error).message}`);
  }
}

export async function handleResume(): Promise<ToolResult> {
  try {
    const mpv = getMpvController();
    if (!mpv || !mpv.isReady()) return errorResult('Audio engine not initialized. Is mpv installed?');
    mpv.resume();
    return textResult({ status: "playing", message: "Playback resumed." });
  } catch (err) {
    return errorResult(`Resume failed: ${(err as Error).message}`);
  }
}

export async function handleSkip(): Promise<ToolResult> {
  try {
    const queuePlaybackController = getQueuePlaybackController();
    if (!queuePlaybackController) return errorResult('Queue playback controller not initialized.');

    const nextTrack = await queuePlaybackController.skip();
    if (!nextTrack) {
      return textResult({ nowPlaying: null, message: 'Skipped current track. Queue is now empty.' });
    }

    return textResult({
      nowPlaying: nextTrack,
      message: `Skipped to ${nextTrack.title} by ${nextTrack.artist}.`,
    });
  } catch (err) {
    return errorResult(`Skip failed: ${(err as Error).message}`);
  }
}

export async function handleQueueList(): Promise<ToolResult> {
  try {
    const queueManager = getQueueManager();
    if (!queueManager) return errorResult('Queue manager not initialized.');

    const state = queueManager.getState();
    return textResult({
      nowPlaying: state.nowPlaying,
      queue: state.queue,
      history: state.history,
      message: state.queue.length === 0 ? 'Queue is empty.' : `Queue has ${state.queue.length} track(s).`,
    });
  } catch (err) {
    return errorResult(`Queue list failed: ${(err as Error).message}`);
  }
}

export async function handleNowPlaying(): Promise<ToolResult> {
  try {
    const mpv = getMpvController();
    if (!mpv || !mpv.isReady()) return errorResult('Audio engine not initialized. Is mpv installed?');

    const track = mpv.getCurrentTrack();
    if (!track) {
      return textResult({ nowPlaying: null, message: "Nothing is currently playing." });
    }

    const position = await mpv.getPosition();
    const duration = await mpv.getDuration();
    const isPlaying = mpv.getIsPlaying();
    const volume = mpv.getVolume();

    return textResult({
      nowPlaying: {
        ...track,
        position: Math.round(position),
        duration: Math.round(duration),
        isPlaying,
        volume,
      },
    });
  } catch (err) {
    return errorResult(`Now playing failed: ${(err as Error).message}`);
  }
}

export async function handleHistory(args: { limit: number; query?: string }): Promise<ToolResult> {
  try {
    const store = getHistoryStore();
    if (!store) return errorResult('History store not initialized.');

    const plays = store.getRecent(args.limit, args.query);
    if (plays.length === 0) {
      return textResult({
        history: [],
        message: args.query
          ? `No history found matching "${args.query}".`
          : 'No listening history yet. Play some tracks first!',
      });
    }

    const history = plays.map((p) => ({
      title: p.title,
      artist: p.artist,
      playedAt: new Date(p.started_at).toISOString(),
      playedSec: p.played_sec,
      skipped: p.skipped === 1,
      playCount: p.play_count,
      ytVideoId: p.yt_video_id,
    }));

    return textResult({
      history,
      total: history.length,
      message: `Showing ${history.length} recent play(s).`,
    });
  } catch (err) {
    return errorResult(`History failed: ${(err as Error).message}`);
  }
}

export async function handleVolume(args: { level?: number }): Promise<ToolResult> {
  try {
    const mpv = getMpvController();
    if (!mpv || !mpv.isReady()) return errorResult('Audio engine not initialized. Is mpv installed?');

    if (args.level !== undefined) {
      const actual = mpv.setVolume(args.level);
      return textResult({ volume: actual, message: `Volume set to ${actual}%.` });
    }
    const current = mpv.getVolume();
    return textResult({ volume: current, message: `Current volume: ${current}%.` });
  } catch (err) {
    return errorResult(`Volume failed: ${(err as Error).message}`);
  }
}

export async function handleGetSessionState(): Promise<ToolResult> {
  try {
    const taste = getTasteEngine();
    if (!taste) return errorResult('Taste engine not initialized. History store may be unavailable.');
    return textResult(taste.getSummary());
  } catch (err) {
    return errorResult(`Session state failed: ${(err as Error).message}`);
  }
}

export async function handleUpdatePersona(args: { taste: string }): Promise<ToolResult> {
  try {
    const taste = getTasteEngine();
    if (!taste) return errorResult('Taste engine not initialized.');

    const text = args.taste.slice(0, 1000);
    taste.saveTasteText(text);
    getWebServer()?.broadcastPersona();

    return textResult({
      updated: true,
      persona: taste.getPersona(),
      message: 'Persona taste updated.',
    });
  } catch (err) {
    return errorResult(`Update persona failed: ${(err as Error).message}`);
  }
}
```

## File: `src/providers/apple-search-provider.ts`
```typescript
// Apple iTunes Search API provider — zero-key metadata/genre source for discovery pipeline
// Endpoints: search tracks, artist tracks, track genre, genre search
// Cache: 7-day TTL in provider_cache table (prefixed keys)

import type Database from 'better-sqlite3';
import { normalizeForQuery } from './metadata-normalizer.js';
import { ProviderCache } from './provider-cache.js';

const APPLE_API_URL = 'https://itunes.apple.com/search';
const CACHE_TTL_MS = 7 * 24 * 60 * 60 * 1000; // 7 days
const FETCH_TIMEOUT_MS = 5000;

export interface AppleTrack {
  title: string;
  artist: string;
  album: string;
  genre: string;
  durationMs: number;
  artwork: string;
  trackId?: number;
  artistId?: number;
}

interface AppleApiResult {
  trackName?: string;
  artistName?: string;
  collectionName?: string;
  primaryGenreName?: string;
  trackTimeMillis?: number;
  artworkUrl100?: string;
  trackId?: number;
  artistId?: number;
}

export class AppleSearchProvider {
  private readonly cache: ProviderCache;

  constructor(db: Database.Database) {
    this.cache = new ProviderCache(db, CACHE_TTL_MS);
    this.cache.evictExpired('apple:');
  }

  async searchTracks(query: string, limit = 10): Promise<AppleTrack[]> {
    const normalized = normalizeForQuery(query);
    const cacheKey = `apple:search:${normalized.toLowerCase()}`;
    const cached = this.cache.get(cacheKey);
    if (cached) return (cached as AppleTrack[]).slice(0, limit);

    const results = await this.fetchApple({ term: normalized, entity: 'song', limit: String(limit) });
    if (!results) return [];

    this.cache.set(cacheKey, results);
    return results.slice(0, limit);
  }

  async getArtistTracks(artist: string, limit = 10): Promise<AppleTrack[]> {
    const normalized = normalizeForQuery(artist);
    const cacheKey = `apple:artist:${normalized.toLowerCase()}`;
    const cached = this.cache.get(cacheKey);
    if (cached) return (cached as AppleTrack[]).slice(0, limit);

    const results = await this.fetchApple({
      term: normalized, entity: 'song', attribute: 'artistTerm', limit: String(limit),
    });
    if (!results) return [];

    this.cache.set(cacheKey, results);
    return results.slice(0, limit);
  }

  async getTrackGenre(artist: string, title: string): Promise<string[]> {
    const normArtist = normalizeForQuery(artist).toLowerCase();
    const normTitle = normalizeForQuery(title).toLowerCase();
    const cacheKey = `apple:genre:${normArtist}::${normTitle}`;
    const cached = this.cache.get(cacheKey);
    if (cached) return cached as string[];

    const results = await this.fetchApple({
      term: `${normalizeForQuery(artist)} ${normalizeForQuery(title)}`,
      entity: 'song', limit: '3',
    });
    if (!results || results.length === 0) return [];

    // Collect unique genres from results
    const genres = [...new Set(results.map(r => r.genre).filter(Boolean))];
    this.cache.set(cacheKey, genres);
    return genres;
  }

  async searchByGenre(genre: string, limit = 10): Promise<AppleTrack[]> {
    const normalized = genre.toLowerCase().trim();
    const cacheKey = `apple:bygenre:${normalized}`;
    const cached = this.cache.get(cacheKey);
    if (cached) return (cached as AppleTrack[]).slice(0, limit);

    const results = await this.fetchApple({
      term: normalized, entity: 'song', limit: String(limit),
    });
    if (!results) return [];

    this.cache.set(cacheKey, results);
    return results.slice(0, limit);
  }

  // --- HTTP (private) ---

  private async fetchApple(params: Record<string, string>): Promise<AppleTrack[] | null> {
    const url = new URL(APPLE_API_URL);
    url.searchParams.set('media', 'music');
    for (const [k, v] of Object.entries(params)) {
      url.searchParams.set(k, v);
    }

    try {
      const controller = new AbortController();
      const timeout = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);
      const response = await fetch(url.toString(), { signal: controller.signal });
      clearTimeout(timeout);

      if (!response.ok) {
        console.error(`[agentune] Apple API error: ${response.status} ${response.statusText}`);
        return null;
      }

      const json = await response.json() as { resultCount?: number; results?: AppleApiResult[] };
      const raw = json.results ?? [];

      return raw.map((r) => ({
        title: r.trackName ?? '',
        artist: r.artistName ?? '',
        album: r.collectionName ?? '',
        genre: r.primaryGenreName ?? '',
        durationMs: r.trackTimeMillis ?? 0,
        artwork: r.artworkUrl100 ?? '',
        trackId: r.trackId,
        artistId: r.artistId,
      }));
    } catch (err) {
      console.error(`[agentune] Apple fetch failed: ${(err as Error).message}`);
      return null;
    }
  }
}

// -- Singleton --

let appleProvider: AppleSearchProvider | null = null;

export function createAppleSearchProvider(db: Database.Database): AppleSearchProvider {
  if (!appleProvider) {
    appleProvider = new AppleSearchProvider(db);
  }
  return appleProvider;
}

export function getAppleSearchProvider(): AppleSearchProvider | null {
  return appleProvider;
}
```

## File: `src/providers/metadata-normalizer.ts`
```typescript
// Shared query normalization — strips YouTube metadata noise before API queries
// Used by AppleSearchProvider and song-resolution query cleanup (DRY)

/** Strip YouTube-specific noise: "(Official Audio)", "[HD]", "- Topic", "VEVO", etc. */
export function normalizeForQuery(text: string): string {
  return text
    .replace(/\s*\(official\s*(audio|video|music\s*video|lyric\s*video|visualizer)\)/gi, '')
    .replace(/\s*\[official\s*(audio|video|music\s*video|lyric\s*video|visualizer)\]/gi, '')
    .replace(/\s*\((lyrics?|hd|hq|4k|live)\)/gi, '')
    .replace(/\s*\[(lyrics?|hd|hq|4k|live)\]/gi, '')
    .replace(/\s*\(feat\.?\s*[^)]+\)/gi, '')
    .replace(/\s*\(ft\.?\s*[^)]+\)/gi, '')
    .replace(/\s*\[feat\.?\s*[^\]]+\]/gi, '')
    .replace(/\s*\[ft\.?\s*[^\]]+\]/gi, '')
    .replace(/\s*-\s*Topic$/i, '')
    .replace(/\s*VEVO$/i, '')
    .replace(/\s+/g, ' ')
    .trim();
}
```

## File: `src/providers/provider-cache.ts`
```typescript
// Shared SQLite cache layer for discovery providers
// Avoids duplicated getCached/setCache across Apple and Smart Search providers

import type Database from 'better-sqlite3';

export class ProviderCache {
  constructor(
    private readonly db: Database.Database,
    private readonly ttlMs: number,
  ) {}

  get(key: string): unknown | null {
    const row = this.db.prepare(
      'SELECT response_json, fetched_at FROM provider_cache WHERE cache_key = ?',
    ).get(key) as { response_json: string; fetched_at: number } | undefined;
    if (!row) return null;
    if (Date.now() - row.fetched_at > this.ttlMs) return null;
    try {
      return JSON.parse(row.response_json);
    } catch {
      return null;
    }
  }

  set(key: string, data: unknown): void {
    this.db.prepare(
      'INSERT OR REPLACE INTO provider_cache (cache_key, response_json, fetched_at) VALUES (?, ?, ?)',
    ).run(key, JSON.stringify(data), Date.now());
  }

  /** Evict expired rows matching a key prefix (e.g. "apple:%") */
  evictExpired(prefix: string): void {
    this.db.prepare('DELETE FROM provider_cache WHERE cache_key LIKE ? AND fetched_at < ?')
      .run(`${prefix}%`, Date.now() - this.ttlMs);
  }
}
```

## File: `src/providers/search-result-scorer.test.ts`
```typescript
// Unit tests for search-result-scorer.ts scoring and variant filtering logic

import assert from 'node:assert/strict';
import { test } from 'node:test';
import { scoreSearchResults } from './search-result-scorer.js';
import type { SearchResult } from './youtube-provider.js';

function createResult(overrides: Partial<SearchResult> = {}): SearchResult {
  return {
    id: 'test-id',
    title: 'Test Song',
    artist: 'Test Artist',
    duration: '3:45',
    durationMs: 225000,
    thumbnail: 'https://example.com/thumb.jpg',
    url: 'https://youtube.com/watch?v=test',
    ...overrides,
  };
}

test('Exact title match scores highest among eligible results', () => {
  const results = [
    createResult({ id: 'exact', title: 'Shape of You' }),
    createResult({ id: 'contains', title: 'Ed Sheeran - Shape of You (Official)' }),
    createResult({ id: 'other', title: 'Another Song' }),
  ];

  const scored = scoreSearchResults(results, 'Shape of You');

  assert.equal(scored[0].result.id, 'exact');
  assert(scored[0].reasons.some((reason) => reason.includes('exact title match')));
  assert(scored[0].score > scored[1].score);
  assert(scored[1].score > scored[2].score);
});

test('Title startswith scores higher than a loose contains match', () => {
  const results = [
    createResult({ id: 'startswith', title: 'Shape of You Extended Version' }),
    createResult({ id: 'contains', title: 'Ed Sheeran - Shape of You' }),
  ];

  const scored = scoreSearchResults(results, 'Shape of You');

  assert.equal(scored[0].result.id, 'startswith');
  assert(scored[0].reasons.some((reason) => reason.includes('starts with')));
});

test('Artist match bonus adds +0.3', () => {
  const scored = scoreSearchResults(
    [createResult({ title: 'Shape of You', artist: 'Ed Sheeran' })],
    'Shape of You',
    'Ed Sheeran',
  );

  assert(scored[0].score >= 1.3);
  assert(scored[0].reasons.some((reason) => reason.includes('artist match')));
});

test('Hard-block keywords remove obvious non-original variants', () => {
  const blockedKeywords = ['cover', 'karaoke', 'instrumental', 'tribute', 'acoustic', 'piano', 'remake', 'fanmade'];

  for (const keyword of blockedKeywords) {
    const scored = scoreSearchResults(
      [createResult({ title: `Shape of You ${keyword}` })],
      'Shape of You',
    );
    assert.deepEqual(scored, [], `"${keyword}" result should be removed`);
  }
});

test('Hard-block multi-word phrases remove candidates', () => {
  const scored = scoreSearchResults(
    [
      createResult({ id: 'sped-up', title: 'Shape of You Sped Up' }),
      createResult({ id: 'album', title: 'Shape of You Full Album' }),
    ],
    'Shape of You',
  );

  assert.deepEqual(scored, []);
});

test('Hard-blocking checks channel names, not only titles', () => {
  const scored = scoreSearchResults(
    [createResult({ title: 'Shape of You', artist: 'Best Karaoke Channel' })],
    'Shape of You',
    'Ed Sheeran',
  );

  assert.deepEqual(scored, []);
});

test('Explicit variant queries keep matching variant candidates eligible', () => {
  const cover = scoreSearchResults(
    [createResult({ id: 'cover', title: 'Shape of You Cover', artist: 'Studio Duo' })],
    'Shape of You Cover',
  );
  const live = scoreSearchResults(
    [createResult({ id: 'live', title: 'Shape of You Live', artist: 'Ed Sheeran Live' })],
    'Shape of You Live',
    'Ed Sheeran',
  );

  assert.equal(cover.length, 1);
  assert.equal(cover[0].result.id, 'cover');
  assert(!cover[0].reasons.some((reason) => reason.includes('cover penalty')));
  assert.equal(live.length, 1);
  assert.equal(live[0].result.id, 'live');
  assert(!live[0].reasons.some((reason) => reason.includes('live')));
});

test('Mixed pools keep originals and remove blocked variants before sorting', () => {
  const results = [
    createResult({ id: 'original', title: 'Shape of You', artist: 'Ed Sheeran' }),
    createResult({ id: 'cover', title: 'Shape of You Cover', artist: 'Cover Singer' }),
    createResult({ id: 'karaoke', title: 'Shape of You', artist: 'Karaoke Hits' }),
    createResult({ id: 'contains', title: 'Ed Sheeran - Shape of You', artist: 'Ed Sheeran' }),
  ];

  const scored = scoreSearchResults(results, 'Shape of You', 'Ed Sheeran');

  assert.deepEqual(scored.map((item) => item.result.id), ['original', 'contains']);
});

test('Duration penalty: >600s reduces score', () => {
  const normal = scoreSearchResults([createResult({ durationMs: 240000 })], 'Shape of You');
  const long = scoreSearchResults([createResult({ durationMs: 700000 })], 'Shape of You');

  assert(long[0].score < normal[0].score);
  assert(long[0].reasons.some((reason) => reason.includes('long duration')));
});

test('Duration bonus: 120-420s grants +0.05', () => {
  const tooShort = scoreSearchResults([createResult({ durationMs: 60000 })], 'Shape of You');
  const ideal = scoreSearchResults([createResult({ durationMs: 240000 })], 'Shape of You');
  const tooLong = scoreSearchResults([createResult({ durationMs: 600000 })], 'Shape of You');

  assert(ideal[0].score > tooShort[0].score);
  assert(ideal[0].score > tooLong[0].score);
  assert(ideal[0].reasons.some((reason) => reason.includes('typical song length')));
});

test('Official audio and topic bonuses still apply to eligible results', () => {
  const official = scoreSearchResults(
    [createResult({ title: 'test official audio', artist: 'Unknown Channel', durationMs: 50000 })],
    'test',
  );
  const topic = scoreSearchResults(
    [createResult({ title: 'Shape of You', artist: 'Topic' })],
    'Shape of You',
  );

  assert(official[0].reasons.some((reason) => reason.includes('official audio')));
  assert(topic[0].reasons.some((reason) => reason.includes('topic')));
});

test('Empty results returns empty array', () => {
  assert.deepEqual(scoreSearchResults([], 'Shape of You'), []);
});

test('Poor matches score below 0.2', () => {
  const scored = scoreSearchResults(
    [createResult({ title: 'Completely Different Song' })],
    'Shape of You',
  );

  assert(scored[0].score < 0.2);
});

test('Case, punctuation, and whitespace are normalized in matching', () => {
  const uppercase = scoreSearchResults(
    [createResult({ title: 'SHAPE OF YOU', artist: 'ED SHEERAN', durationMs: 70000 })],
    'Shape of You',
    'Ed Sheeran',
  );
  const punctuated = scoreSearchResults(
    [createResult({ title: 'Shape... Of... You!!!', durationMs: 70000 })],
    'Shape of You',
  );
  const spaced = scoreSearchResults(
    [createResult({ title: 'Song  Name', durationMs: 225000 })],
    'Song Name',
  );

  assert(uppercase[0].score >= 1.3);
  assert(uppercase[0].reasons.some((reason) => reason.includes('exact')));
  assert(punctuated[0].score >= 1.0);
  assert(spaced[0].score === 1.05);
});

test('Word overlap scoring still works for partial matches', () => {
  const results = [
    createResult({ id: 'exact', title: 'Shape of You' }),
    createResult({ id: 'partial', title: 'Shape of You and More Words' }),
    createResult({ id: 'loose', title: 'Song About Shape' }),
  ];

  const scored = scoreSearchResults(results, 'Shape of You');

  assert.equal(scored[0].result.id, 'exact');
  assert.equal(scored[1].result.id, 'partial');
  assert.equal(scored[2].result.id, 'loose');
});

test('Scores stay rounded and keep original result references', () => {
  const original = createResult({
    title: 'Shape of You Official Audio',
    artist: 'Ed Sheeran',
    durationMs: 240000,
  });

  const scored = scoreSearchResults([original], 'Shape of You', 'Ed Sheeran');

  assert.equal(scored[0].result, original);
  assert.equal(scored[0].score, Math.round(scored[0].score * 100) / 100);
  assert(scored[0].score <= 2.0);
});

test('Scoring without artist or with empty artist still works', () => {
  const withoutArtist = scoreSearchResults(
    [createResult({ title: 'Shape of You', artist: 'Unknown Channel', durationMs: 70000 })],
    'Shape of You',
  );
  const emptyArtist = scoreSearchResults(
    [createResult({ title: 'Shape of You', artist: 'Ed Sheeran', durationMs: 70000 })],
    'Shape of You',
    '',
  );

  assert(withoutArtist[0].score >= 1.0);
  assert(!withoutArtist[0].reasons.some((reason) => reason.includes('artist match')));
  assert(emptyArtist[0].score >= 1.0);
  assert(!emptyArtist[0].reasons.some((reason) => reason.includes('artist match')));
});

test('Reason arrays stay populated with scoring explanations', () => {
  const scored = scoreSearchResults(
    [createResult({ title: 'Shape of You Official Audio', artist: 'Ed Sheeran', durationMs: 240000 })],
    'Shape of You',
    'Ed Sheeran',
  );

  assert(scored[0].reasons.length > 0);
  assert(scored[0].reasons.some((reason) => reason.includes('title')));
  assert(scored[0].reasons.some((reason) => reason.includes('artist')));
  assert(scored[0].reasons.some((reason) => reason.includes('official')));
  assert(scored[0].reasons.some((reason) => reason.includes('song length')));
});
```

## File: `src/providers/search-result-scorer.ts`
```typescript
// Score YouTube search results against a canonical title/artist for best match selection

import type { SearchResult } from './youtube-provider.js';

export interface ScoredResult {
  result: SearchResult;
  score: number;
  reasons: string[];
}

const HARD_BLOCKED_VARIANTS = [
  'cover',
  'karaoke',
  'instrumental',
  'acoustic',
  'piano',
  'tribute',
  'remake',
  'fanmade',
  'fan made',
  'slowed',
  'sped up',
  'nightcore',
  '8d',
  'reverb',
  'live',
  'remix',
  'teaser',
  'preview',
  'shorts',
  'playlist',
  'full album',
] as const;

/** Strip punctuation, collapse whitespace, normalize to lowercase for comparison. */
function normalize(text: string): string {
  return text.toLowerCase().replace(/[^\w\s]/g, '').replace(/\s+/g, ' ').trim();
}

function tokenize(text: string): string[] {
  const normalized = normalize(text);
  return normalized ? normalized.split(' ') : [];
}

function containsPhrase(tokens: string[], phraseTokens: string[]): boolean {
  if (phraseTokens.length === 0 || tokens.length < phraseTokens.length) return false;

  for (let i = 0; i <= tokens.length - phraseTokens.length; i += 1) {
    let matched = true;
    for (let j = 0; j < phraseTokens.length; j += 1) {
      if (tokens[i + j] !== phraseTokens[j]) {
        matched = false;
        break;
      }
    }
    if (matched) return true;
  }

  return false;
}

/** Known quality suffixes that YouTube appends — strip before title matching. */
const QUALITY_SUFFIXES = /\b(official audio|official video|official music video|audio|music video|lyric video|lyrics|provided to youtube|hd|hq|4k)\b/gi;

/** Strip quality suffixes for cleaner title-to-title comparison. */
function stripQualitySuffixes(text: string): string {
  return text.replace(QUALITY_SUFFIXES, '').replace(/\s+/g, ' ').trim();
}

/** Word overlap ratio between two strings. */
function wordOverlap(a: string, b: string): number {
  const wordsA = new Set(a.split(/\s+/).filter(Boolean));
  const wordsB = new Set(b.split(/\s+/).filter(Boolean));
  if (wordsA.size === 0 || wordsB.size === 0) return 0;
  let matches = 0;
  for (const w of wordsA) {
    if (wordsB.has(w)) matches++;
  }
  return matches / Math.max(wordsA.size, wordsB.size);
}

/** Score a single result's title match (0-1). Strips quality suffixes before comparing. */
function scoreTitleMatch(resultTitle: string, queryTitle: string): { score: number; reason: string } {
  const rt = normalize(stripQualitySuffixes(resultTitle));
  const qt = normalize(queryTitle);

  if (rt === qt) return { score: 1.0, reason: 'exact title match' };
  if (rt.startsWith(qt)) return { score: 0.8, reason: 'title starts with query' };
  if (rt.includes(qt)) return { score: 0.6, reason: 'title contains query' };

  const overlap = wordOverlap(rt, qt);
  return { score: overlap * 0.4, reason: `word overlap ${Math.round(overlap * 100)}%` };
}

/** Check if query text contains a keyword (case-insensitive). */
function queryContains(query: string, keyword: string): boolean {
  return containsPhrase(tokenize(query), tokenize(keyword));
}

function getBlockedKeyword(result: SearchResult, fullQuery: string): string | null {
  const titleTokens = tokenize(result.title);
  const artistTokens = tokenize(result.artist);

  for (const keyword of HARD_BLOCKED_VARIANTS) {
    if (queryContains(fullQuery, keyword)) continue;
    const keywordTokens = tokenize(keyword);
    if (containsPhrase(titleTokens, keywordTokens) || containsPhrase(artistTokens, keywordTokens)) {
      return keyword;
    }
  }

  return null;
}

/** Score a single search result against canonical title/artist. */
function scoreResult(result: SearchResult, title: string, artist?: string): ScoredResult {
  const reasons: string[] = [];
  let score = 0;

  // 1. Title match (0-1)
  const titleMatch = scoreTitleMatch(result.title, title);
  score += titleMatch.score;
  reasons.push(`title: ${titleMatch.reason} (${titleMatch.score.toFixed(2)})`);

  // 2. Artist match bonus (+0.3)
  if (artist) {
    const normalizedArtist = normalize(artist);
    const normalizedChannel = normalize(result.artist);
    if (normalizedChannel.includes(normalizedArtist) || normalizedArtist.includes(normalizedChannel)) {
      score += 0.3;
      reasons.push('artist match (+0.30)');
    }
  }

  // Build full query string for keyword checks
  const fullQuery = artist ? `${artist} ${title}` : title;

  // 3. Quality penalties
  const rt = normalize(result.title);
  const penalties: [string, number][] = [
    ['live', -0.3],
    ['remix', -0.25],
    ['slowed', -0.4],
    ['8d', -0.4],
    ['reverb', -0.4],
    ['teaser', -0.3],
    ['preview', -0.3],
    ['karaoke', -0.4],
    ['cover', -0.4],
    ['nightcore', -0.4],
    ['sped up', -0.4],
    ['shorts', -0.3],
    ['playlist', -0.2],
    ['full album', -0.2],
  ];
  for (const [keyword, penalty] of penalties) {
    if (rt.includes(keyword) && !queryContains(fullQuery, keyword)) {
      score += penalty;
      reasons.push(`"${keyword}" penalty (${penalty.toFixed(2)})`);
    }
  }

  // Duration penalty: >600s likely mix/compilation
  const durationSec = result.durationMs / 1000;
  if (durationSec > 600) {
    score -= 0.2;
    reasons.push('long duration penalty (-0.20)');
  }

  // 4. Quality bonuses
  if (rt.includes('official audio')) {
    score += 0.15;
    reasons.push('"official audio" bonus (+0.15)');
  }
  if (normalize(result.artist).includes('topic') || rt.includes('provided to youtube')) {
    score += 0.1;
    reasons.push('topic/auto-generated bonus (+0.10)');
  }
  if (durationSec >= 120 && durationSec <= 420) {
    score += 0.05;
    reasons.push('typical song length bonus (+0.05)');
  }

  return { result, score: Math.round(score * 100) / 100, reasons };
}

/**
 * Score and rank search results against a canonical title + optional artist.
 * Returns all results sorted by score descending.
 */
export function scoreSearchResults(
  results: SearchResult[],
  title: string,
  artist?: string,
): ScoredResult[] {
  const fullQuery = artist ? `${artist} ${title}` : title;

  return results
    .filter((result) => getBlockedKeyword(result, fullQuery) === null)
    .map((r) => scoreResult(r, title, artist))
    .sort((a, b) => b.score - a.score);
}
```

## File: `src/providers/youtube-provider.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
import { mapYtDlpSearchEntries } from './youtube-provider.js';

test('mapYtDlpSearchEntries converts yt-dlp playlist entries into SearchResult objects', () => {
  const results = mapYtDlpSearchEntries([
    {
      id: '6eONmnFB9sw',
      title: 'Chuyện Đôi Ta - Emcee L (Da LAB) ft Muộii (Official MV)',
      duration: 226,
      channel: 'Da LAB Official and Emcee L Official',
      webpage_url: 'https://www.youtube.com/watch?v=6eONmnFB9sw',
      thumbnails: [{ url: 'https://i.ytimg.com/vi/6eONmnFB9sw/hq720.jpg' }],
    },
  ], 3);

  assert.equal(results.length, 1);
  assert.equal(results[0].id, '6eONmnFB9sw');
  assert.equal(results[0].artist, 'Da LAB Official and Emcee L Official');
  assert.equal(results[0].duration, '3:46');
  assert.equal(results[0].durationMs, 226000);
  assert.equal(results[0].url, 'https://www.youtube.com/watch?v=6eONmnFB9sw');
});

test('mapYtDlpSearchEntries skips malformed entries and respects limit', () => {
  const results = mapYtDlpSearchEntries([
    { title: 'missing id' },
    { id: 'good-1', title: 'Good 1', duration: 60, uploader: 'Uploader 1' },
    { id: 'good-2', title: 'Good 2', duration: 61, uploader: 'Uploader 2' },
  ], 1);

  assert.equal(results.length, 1);
  assert.equal(results[0].id, 'good-1');
  assert.equal(results[0].artist, 'Uploader 1');
  assert.equal(results[0].duration, '1:00');
});
```

## File: `src/providers/youtube-provider.ts`
```typescript
// YouTube search + audio URL extraction via @distube/ytsr and yt-dlp

import fs from 'node:fs';
import type { Video } from '@distube/ytsr';
import { youtubeDl } from 'youtube-dl-exec';

// Hide yt-dlp console window on Windows (tinyspawn doesn't set windowsHide by default)
const SPAWN_OPTS = process.platform === 'win32' ? { windowsHide: true } : {};

export interface SearchResult {
  id: string;
  title: string;
  artist: string;
  duration: string;      // "3:45" formatted
  durationMs: number;    // milliseconds
  thumbnail: string;
  url: string;           // YouTube watch URL
}

export interface AudioInfo {
  streamUrl: string;
  title: string;
  artist: string;
  duration: number;      // seconds
  thumbnail: string;
}

interface YtDlpSearchEntry {
  id?: string;
  title?: string;
  duration?: number | null;
  channel?: string | null;
  uploader?: string | null;
  thumbnails?: Array<{ url?: string | null }>;
  url?: string;
  webpage_url?: string;
}

interface YtDlpSearchResult {
  entries?: YtDlpSearchEntry[];
}

type YtsrSearch = (
  query: string,
  options?: { limit?: number; safeSearch?: boolean },
) => Promise<{ items: Video[] }>;

let ytsrModulePromise: Promise<YtsrSearch> | null = null;
let ytsrCompatPatched = false;

function ensureYtsrNode25Compatibility(): void {
  if (ytsrCompatPatched) return;

  const fsCompat = fs as typeof fs & {
    rmdirSync(path: fs.PathLike, options?: { recursive?: boolean; maxRetries?: number; retryDelay?: number }): void;
  };
  const originalRmdirSync = fsCompat.rmdirSync.bind(fsCompat) as (...args: unknown[]) => void;

  fsCompat.rmdirSync = ((path: fs.PathLike, options?: { recursive?: boolean; maxRetries?: number; retryDelay?: number }) => {
    const recursive = typeof options === 'object' && options !== null && 'recursive' in options && options.recursive === true;
    if (recursive) {
      const { recursive: _recursive, ...rest } = options;
      fs.rmSync(path, { ...rest, recursive: true });
      return;
    }
    return originalRmdirSync(path, options);
  }) as typeof fsCompat.rmdirSync;

  ytsrCompatPatched = true;
}

async function loadYtsr(): Promise<YtsrSearch> {
  ensureYtsrNode25Compatibility();
  ytsrModulePromise ??= import('@distube/ytsr').then((module) => ((module as { default?: unknown }).default ?? module) as YtsrSearch);
  return ytsrModulePromise;
}

// Parse "3:45" or "1:02:30" duration string to milliseconds
function parseDuration(duration: string): number {
  const parts = duration.split(':').map(Number);
  if (parts.some(isNaN)) return 0;
  let seconds = 0;
  if (parts.length === 3) {
    seconds = parts[0] * 3600 + parts[1] * 60 + parts[2];
  } else if (parts.length === 2) {
    seconds = parts[0] * 60 + parts[1];
  } else {
    seconds = parts[0] || 0;
  }
  return seconds * 1000;
}

function formatDuration(durationSec: number): string {
  const total = Math.max(0, Math.round(durationSec));
  const hours = Math.floor(total / 3600);
  const minutes = Math.floor((total % 3600) / 60);
  const seconds = total % 60;

  if (hours > 0) {
    return `${hours}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
  }
  return `${minutes}:${String(seconds).padStart(2, '0')}`;
}

export function mapYtDlpSearchEntries(entries: YtDlpSearchEntry[] | undefined, limit: number): SearchResult[] {
  return (entries ?? [])
    .filter((entry): entry is Required<Pick<YtDlpSearchEntry, 'id' | 'title'>> & YtDlpSearchEntry => Boolean(entry.id && entry.title))
    .slice(0, limit)
    .map((entry) => {
      const durationSec = entry.duration ?? 0;
      const url = entry.webpage_url ?? entry.url ?? `https://www.youtube.com/watch?v=${entry.id}`;
      return {
        id: entry.id,
        title: entry.title,
        artist: entry.channel ?? entry.uploader ?? 'Unknown',
        duration: formatDuration(durationSec),
        durationMs: durationSec * 1000,
        thumbnail: entry.thumbnails?.[0]?.url ?? '',
        url,
      };
    });
}

export class YouTubeProvider {
  async search(query: string, limit = 5): Promise<SearchResult[]> {
    if (!query.trim()) return [];

    try {
      const ytsr = await loadYtsr();

      // Fetch extra results to account for non-video items filtered out
      const results = await ytsr(query, { limit: limit + 5, safeSearch: true });
      console.error('[youtube-provider] search complete', { query, total: results.items.length, source: 'ytsr' });

      return results.items
        .filter((item): item is Video => item.type === 'video')
        .slice(0, limit)
        .map(video => ({
          id: video.id,
          title: video.name,
          artist: video.author?.name ?? 'Unknown',
          duration: video.duration ?? '0:00',
          durationMs: video.duration ? parseDuration(video.duration) : 0,
          thumbnail: video.thumbnail ?? '',
          url: video.url,
        }));
    } catch (error) {
      const lastError = error as Error;
      console.error('[youtube-provider] ytsr search failed, falling back to yt-dlp', {
        query,
        message: lastError.message,
      });

      const result = await (youtubeDl as Function)(`ytsearch${limit}:${query}`, {
        dumpSingleJson: true,
        flatPlaylist: true,
        noWarnings: true,
        callHome: false,
      }, SPAWN_OPTS) as unknown as YtDlpSearchResult;

      const mapped = mapYtDlpSearchEntries(result.entries, limit);
      console.error('[youtube-provider] search complete', { query, total: mapped.length, source: 'yt-dlp' });
      return mapped;
    }
  }

  async getAudioUrl(videoIdOrUrl: string): Promise<AudioInfo> {
    if (!videoIdOrUrl.trim()) throw new Error('Video ID or URL is required');

    const url = videoIdOrUrl.startsWith('http')
      ? videoIdOrUrl
      : `https://www.youtube.com/watch?v=${videoIdOrUrl}`;

    let info: unknown;
    let lastError: Error | null = null;

    for (let attempt = 1; attempt <= 2; attempt += 1) {
      try {
        info = await (youtubeDl as Function)(url, {
          dumpSingleJson: true,
          format: 'bestaudio[ext=m4a]/bestaudio',
          noWarnings: true,
          callHome: false,
        }, SPAWN_OPTS);
        break;
      } catch (error) {
        lastError = error as Error;
        console.error('[youtube-provider] audio extraction failed', { attempt, message: lastError.message });
      }
    }

    if (!info) {
      throw lastError ?? new Error('Could not extract audio stream URL');
    }

    // yt-dlp puts the selected format's URL at top level when format is specified,
    // but it may also be in the formats array — use top-level .url first
    const payload = info as Record<string, unknown>;
    const streamUrl = (payload.url as string)
      ?? ((payload.formats as Array<{ url: string }>) ?? []).at(-1)?.url;

    if (!streamUrl) throw new Error('Could not extract audio stream URL');

    console.error('[youtube-provider] audio extracted', { title: payload.title, duration: payload.duration });

    return {
      streamUrl,
      title: (payload.title as string) ?? 'Unknown',
      artist: (payload.uploader as string) ?? (payload.channel as string) ?? 'Unknown',
      duration: (payload.duration as number) ?? 0,
      thumbnail: (payload.thumbnail as string) ?? '',
    };
  }
}

// Singleton
let provider: YouTubeProvider | null = null;

export function createYoutubeProvider(): YouTubeProvider {
  if (!provider) {
    provider = new YouTubeProvider();
  }
  return provider;
}

export function getYoutubeProvider(): YouTubeProvider | null {
  return provider;
}
```

## File: `src/proxy/daemon-launcher.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
import { ensureDaemon, resolveDaemonEntryPoint } from './daemon-launcher.js';

test('ensureDaemon returns the healthy running daemon without spawning', async () => {
  let spawnCount = 0;

  const result = await ensureDaemon(
    { allowSpawn: false },
    {
      checkHealth: async (port) => port === 4010,
      getDaemonLogPath: () => 'daemon.log',
        isDaemonRunning: () => ({
          running: true,
          info: { controlToken: 'daemon-token', pid: 11, port: 4010, started: '2026-03-20T00:00:00.000Z' },
        }),
      loadRuntimeConfig: () => ({
        dashboardPort: 3737,
        daemonPort: 3747,
        defaultVolume: 80,
        autoStartDaemon: true,
        discoverRanking: { exploration: 0.35, variety: 0.55, loyalty: 0.65 },
      }),
      now: () => 0,
      readPidFile: () => null,
      sleep: async () => {},
      spawnDaemon: () => {
        spawnCount += 1;
      },
    },
  );

  assert.deepEqual(result, { controlToken: 'daemon-token', port: 4010, started: false });
  assert.equal(spawnCount, 0);
});

test('ensureDaemon fails fast when spawning is disabled and no healthy daemon exists', async () => {
  let spawnCount = 0;

  await assert.rejects(
    () =>
      ensureDaemon(
        { allowSpawn: false },
        {
          checkHealth: async () => false,
          getDaemonLogPath: () => 'daemon.log',
          isDaemonRunning: () => ({ running: false, info: null }),
          loadRuntimeConfig: () => ({
            dashboardPort: 3737,
            daemonPort: 3747,
            defaultVolume: 80,
            autoStartDaemon: false,
            discoverRanking: { exploration: 0.35, variety: 0.55, loyalty: 0.65 },
          }),
          now: () => 0,
          readPidFile: () => null,
          sleep: async () => {},
          spawnDaemon: () => {
            spawnCount += 1;
          },
        },
      ),
    /Start it with "agentune start"/i,
  );

  assert.equal(spawnCount, 0);
});

test('ensureDaemon spawns and waits for health when allowed', async () => {
  let currentTime = 0;
  let spawned = false;

  const result = await ensureDaemon(
    { allowSpawn: true },
    {
      checkHealth: async (port) => spawned && port === 4555,
      getDaemonLogPath: () => 'daemon.log',
      isDaemonRunning: () => ({ running: false, info: null }),
      loadRuntimeConfig: () => ({
        dashboardPort: 3737,
        daemonPort: 3747,
        defaultVolume: 80,
        autoStartDaemon: true,
        discoverRanking: { exploration: 0.35, variety: 0.55, loyalty: 0.65 },
      }),
      now: () => currentTime,
        readPidFile: () => (
          spawned
            ? { controlToken: 'spawned-token', pid: 22, port: 4555, started: '2026-03-20T00:00:00.000Z' }
            : null
        ),
      sleep: async () => {
        currentTime += 200;
      },
      spawnDaemon: () => {
        spawned = true;
      },
    },
  );

  assert.deepEqual(result, { controlToken: 'spawned-token', port: 4555, started: true });
});

test('resolveDaemonEntryPoint targets the built index entry', () => {
  const entryPoint = resolveDaemonEntryPoint();
  assert.match(entryPoint.replaceAll('\\', '/'), /\/dist\/index\.js$/);
});
```

## File: `src/proxy/daemon-launcher.ts`
```typescript
// Daemon discovery + optional auto-start for proxy/manual CLI flows.

import { spawn } from 'child_process';
import { closeSync, openSync } from 'fs';
import { fileURLToPath } from 'url';
import { type DaemonInfo, readPidFile, isDaemonRunning } from '../daemon/pid-manager.js';
import { loadRuntimeConfig } from '../runtime/runtime-config.js';
import { getDaemonLogPath } from '../runtime/runtime-data-paths.js';

const HEALTH_POLL_INTERVAL = 200; // ms
const HEALTH_POLL_TIMEOUT = 10_000; // ms

export interface EnsureDaemonOptions {
  allowSpawn?: boolean;
}

export interface EnsureDaemonResult {
  controlToken: string;
  port: number;
  started: boolean;
}

interface DaemonLauncherDependencies {
  checkHealth: (port: number) => Promise<boolean>;
  getDaemonLogPath: typeof getDaemonLogPath;
  isDaemonRunning: typeof isDaemonRunning;
  loadRuntimeConfig: typeof loadRuntimeConfig;
  now: () => number;
  readPidFile: typeof readPidFile;
  sleep: (ms: number) => Promise<void>;
  spawnDaemon: () => void;
}

/** Ensure daemon is running; start it if allowed and missing. */
export async function ensureDaemon(
  options?: EnsureDaemonOptions,
  dependencies: DaemonLauncherDependencies = createDaemonLauncherDependencies(),
): Promise<EnsureDaemonResult> {
  const allowSpawn = options?.allowSpawn ?? true;
  const { daemonPort } = dependencies.loadRuntimeConfig();

  // Check if already running via PID file + health check
  const check = dependencies.isDaemonRunning();
  if (check.running && check.info) {
    const healthy = await dependencies.checkHealth(check.info.port);
    if (healthy) return {
      controlToken: check.info.controlToken,
      port: check.info.port,
      started: false,
    };
  }

  if (!allowSpawn) {
    throw new Error('Daemon is not running. Start it with "agentune start".');
  }

  dependencies.spawnDaemon();
  return await waitForHealth(daemonPort, dependencies);
}

function spawnDetachedDaemon(): void {
  const entryPoint = resolveDaemonEntryPoint();
  const logPath = getDaemonLogPath();
  const logFd = openSync(logPath, 'w');

  const child = spawn(process.execPath, [entryPoint, '--daemon'], {
    // Keep the daemon alive after the proxy terminal exits on every platform.
    detached: true,
    windowsHide: true,
    stdio: ['ignore', logFd, logFd],
    env: { ...process.env },
  });
  child.unref();
  closeSync(logFd);
}

export function resolveDaemonEntryPoint(): string {
  return fileURLToPath(new URL('../index.js', import.meta.url));
}

async function waitForHealth(
  expectedPort: number,
  dependencies: DaemonLauncherDependencies,
): Promise<EnsureDaemonResult> {
  const deadline = dependencies.now() + HEALTH_POLL_TIMEOUT;
  while (dependencies.now() < deadline) {
    const info = dependencies.readPidFile();
    const port = info?.port ?? expectedPort;
    if (info?.controlToken && await dependencies.checkHealth(port)) {
      return {
        controlToken: info.controlToken,
        port,
        started: true,
      };
    }
    await dependencies.sleep(HEALTH_POLL_INTERVAL);
  }
  throw new Error(`Daemon failed to start within 10s. Check ${dependencies.getDaemonLogPath()}`);
}

async function checkHealth(port: number): Promise<boolean> {
  try {
    const res = await fetch(`http://127.0.0.1:${port}/health`, {
      signal: AbortSignal.timeout(1000),
    });
    return res.ok;
  } catch {
    return false;
  }
}

function createDaemonLauncherDependencies(): DaemonLauncherDependencies {
  return {
    checkHealth,
    getDaemonLogPath,
    isDaemonRunning,
    loadRuntimeConfig,
    now: () => Date.now(),
    readPidFile,
    sleep: async (ms) => await new Promise((resolve) => setTimeout(resolve, ms)),
    spawnDaemon: spawnDetachedDaemon,
  };
}
```

## File: `src/proxy/stdio-proxy.ts`
```typescript
// Stdio↔HTTP MCP proxy — bridges agent's stdio to daemon's HTTP MCP endpoint
// Uses low-level Server to forward tools/list and tools/call to daemon

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { Client } from '@modelcontextprotocol/sdk/client/index.js';
import { StreamableHTTPClientTransport } from '@modelcontextprotocol/sdk/client/streamableHttp.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import { DAEMON_CONTROL_TOKEN_HEADER } from '../daemon/daemon-auth.js';

/** Connect stdio transport to daemon HTTP MCP endpoint and relay all traffic */
export async function startProxy(daemonPort: number, controlToken: string): Promise<void> {
  // Connect HTTP client to daemon
  const httpTransport = new StreamableHTTPClientTransport(
    new URL(`http://127.0.0.1:${daemonPort}/mcp`),
    {
      requestInit: {
        headers: {
          [DAEMON_CONTROL_TOKEN_HEADER]: controlToken,
        },
      },
    },
  );
  const httpClient = new Client(
    { name: 'agentune-proxy', version: '0.1.0' },
    { capabilities: {} }
  );
  await httpClient.connect(httpTransport);

  // Create stdio-facing server for the agent
  const stdioServer = new Server(
    { name: 'agentune', version: '0.1.0' },
    { capabilities: { tools: {} } }
  );

  // Forward tools/list to daemon
  stdioServer.setRequestHandler(ListToolsRequestSchema, async () => {
    return await httpClient.listTools();
  });

  // Forward tools/call to daemon
  stdioServer.setRequestHandler(CallToolRequestSchema, async (request) => {
    return await httpClient.callTool(request.params);
  });

  // Connect stdio transport (blocks until closed)
  const stdioTransport = new StdioServerTransport();
  await stdioServer.connect(stdioTransport);

  // Cleanup on exit
  const cleanup = () => {
    Promise.all([httpClient.close(), stdioServer.close()])
      .catch(() => {})
      .finally(() => process.exit(0));
  };
  process.on('SIGINT', cleanup);
  process.on('SIGTERM', cleanup);
}
```

## File: `src/queue/queue-manager.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
import { QueueManager } from './queue-manager.js';

test('QueueManager adds and returns queued items in order', () => {
  const queueManager = new QueueManager();
  const firstPosition = queueManager.add({
    id: '1',
    title: 'First',
    artist: 'Artist 1',
    duration: 100,
    thumbnail: 'thumb-1',
    url: 'https://example.com/1',
  });
  const secondPosition = queueManager.add({
    id: '2',
    title: 'Second',
    artist: 'Artist 2',
    duration: 120,
    thumbnail: 'thumb-2',
    url: 'https://example.com/2',
  });

  assert.equal(firstPosition, 1);
  assert.equal(secondPosition, 2);
  assert.deepEqual(queueManager.list().map((item) => item.id), ['1', '2']);
  assert.equal(queueManager.next()?.id, '1');
  assert.equal(queueManager.next()?.id, '2');
  assert.equal(queueManager.next(), null);
});

test('QueueManager archives finished tracks into history', () => {
  const queueManager = new QueueManager();
  queueManager.setNowPlaying({
    id: '1',
    title: 'Current',
    artist: 'Artist',
    duration: 100,
    thumbnail: 'thumb',
    url: 'https://example.com/1',
  });

  const finished = queueManager.finishCurrentTrack();
  const state = queueManager.getState();

  assert.equal(finished?.id, '1');
  assert.equal(state.nowPlaying, null);
  assert.deepEqual(state.history.map((item) => item.id), ['1']);
});
```

## File: `src/queue/queue-manager.ts`
```typescript
import { EventEmitter } from 'events';

const MAX_HISTORY_ITEMS = 20;

export interface QueueItem {
  id: string;
  title: string;
  artist: string;
  duration: number;
  thumbnail: string;
  url: string;
  context?: string;
}

export interface QueueState {
  nowPlaying: QueueItem | null;
  queue: QueueItem[];
  history: QueueItem[];
}

export class QueueManager extends EventEmitter {
  private state: QueueState = {
    nowPlaying: null,
    queue: [],
    history: [],
  };

  add(item: QueueItem): number {
    this.state.queue.push(item);
    this.emitStateChange();
    return this.state.queue.length;
  }

  list(): QueueItem[] {
    return [...this.state.queue];
  }

  next(): QueueItem | null {
    const nextItem = this.state.queue.shift() ?? null;
    this.emitStateChange();
    return nextItem;
  }

  /** Look at the next item without removing it from the queue. */
  peek(): QueueItem | null {
    return this.state.queue[0] ?? null;
  }

  size(): number {
    return this.state.queue.length;
  }

  clear(): void {
    this.state.queue = [];
    this.emitStateChange();
  }

  reset(): void {
    this.state = {
      nowPlaying: null,
      queue: [],
      history: [],
    };
    this.emitStateChange();
  }

  getNowPlaying(): QueueItem | null {
    return this.state.nowPlaying;
  }

  setNowPlaying(item: QueueItem | null): void {
    if (this.state.nowPlaying) {
      this.pushHistory(this.state.nowPlaying);
    }
    this.state.nowPlaying = item;
    this.emitStateChange();
  }

  finishCurrentTrack(): QueueItem | null {
    const finished = this.state.nowPlaying;
    if (finished) {
      this.pushHistory(finished);
    }
    this.state.nowPlaying = null;
    this.emitStateChange();
    return finished ?? null;
  }

  clearNowPlaying(): void {
    if (!this.state.nowPlaying) {
      return;
    }
    this.state.nowPlaying = null;
    this.emitStateChange();
  }

  getState(): QueueState {
    return {
      nowPlaying: this.state.nowPlaying,
      queue: [...this.state.queue],
      history: [...this.state.history],
    };
  }

  private pushHistory(item: QueueItem): void {
    this.state.history = [item, ...this.state.history].slice(0, MAX_HISTORY_ITEMS);
  }

  private emitStateChange(): void {
    this.emit('state-change', this.getState());
  }
}

let queueManager: QueueManager | null = null;

export function createQueueManager(): QueueManager {
  if (!queueManager) {
    queueManager = new QueueManager();
  }
  return queueManager;
}

export function getQueueManager(): QueueManager | null {
  return queueManager;
}
```

## File: `src/queue/queue-playback-controller.test.ts`
```typescript
import assert from 'node:assert/strict';
import { EventEmitter } from 'events';
import test from 'node:test';
import { QueuePlaybackController } from './queue-playback-controller.js';
import { QueueManager } from './queue-manager.js';

class FakeMpv extends EventEmitter {
  public playCalls: Array<{ url: string; meta: unknown }> = [];
  public resumeCalls = 0;
  public stopCalls = 0;
  public suppressCalls = 0;
  public pauseProperty = false;
  public isPlaying = false;
  public currentTrack: unknown = null;

  play(url: string, meta: unknown): void {
    this.playCalls.push({ url, meta });
    this.currentTrack = meta;
    this.isPlaying = !this.pauseProperty;
  }

  stop(): void {
    this.stopCalls += 1;
    this.currentTrack = null;
    this.isPlaying = false;
  }

  resume(): void {
    this.resumeCalls += 1;
    this.pauseProperty = false;
    this.isPlaying = true;
  }

  pause(): void {
    this.pauseProperty = true;
    this.isPlaying = false;
  }

  suppressNextStopped(): void { this.suppressCalls += 1; }

  getCurrentTrack(): unknown { return this.currentTrack; }

  isReady(): boolean { return true; }

  emitStopped(): void {
    this.currentTrack = null;
    this.isPlaying = false;
    this.emit('stopped');
  }

  async getPosition(): Promise<number> {
    return 0;
  }
}

class FakeYouTubeProvider {
  async search(query: string): Promise<Array<{
    id: string;
    title: string;
    artist: string;
    duration: string;
    durationMs: number;
    thumbnail: string;
    url: string;
  }>> {
    return [{
      id: 'search-result',
      title: `${query} result`,
      artist: 'Search Artist',
      duration: '3:00',
      durationMs: 180000,
      thumbnail: 'thumb-search',
      url: 'https://youtube.test/search-result',
    }];
  }

  async getAudioUrl(id: string): Promise<{
    streamUrl: string;
    title: string;
    artist: string;
    duration: number;
    thumbnail: string;
  }> {
    return {
      streamUrl: `https://stream.test/${id}`,
      title: `Track ${id}`,
      artist: `Artist ${id}`,
      duration: 180,
      thumbnail: `thumb-${id}`,
    };
  }
}

class SlowFakeYouTubeProvider extends FakeYouTubeProvider {
  override async getAudioUrl(id: string): Promise<{
    streamUrl: string;
    title: string;
    artist: string;
    duration: number;
    thumbnail: string;
  }> {
    await new Promise((resolve) => setTimeout(resolve, 0));
    return await super.getAudioUrl(id);
  }
}

test('QueuePlaybackController queues search results', async () => {
  const queueManager = new QueueManager();
  const controller = new QueuePlaybackController(
    new FakeMpv() as never,
    queueManager,
    new FakeYouTubeProvider() as never,
  );

  const queued = await controller.queueByQuery('focus music');

  assert.equal(queued.position, 1);
  assert.equal(queued.item.id, 'search-result');
  assert.deepEqual(queueManager.list().map((item) => item.id), ['search-result']);
});

test('QueuePlaybackController addById queues then starts playback when idle', async () => {
  const queueManager = new QueueManager();
  const fakeMpv = new FakeMpv();
  const controller = new QueuePlaybackController(
    fakeMpv as never,
    queueManager,
    new FakeYouTubeProvider() as never,
  );

  const added = await controller.addById('resolved-song', {
    canonicalArtist: 'Canonical Artist',
    canonicalTitle: 'Canonical Title',
  });

  assert.equal(added.action, 'queued');
  assert.equal(added.position, 1);
  assert.equal(added.startedPlayback, true);
  assert.equal(queueManager.getNowPlaying()?.id, 'resolved-song');
  assert.equal(queueManager.getNowPlaying()?.artist, 'Canonical Artist');
  assert.equal(queueManager.list().length, 0);
  assert.equal(fakeMpv.playCalls.length, 1);
});

test('QueuePlaybackController addById queues when something is already playing', async () => {
  const queueManager = new QueueManager();
  const controller = new QueuePlaybackController(
    new FakeMpv() as never,
    queueManager,
    new FakeYouTubeProvider() as never,
  );

  queueManager.setNowPlaying({
    id: 'current',
    title: 'Current',
    artist: 'Current Artist',
    duration: 180,
    thumbnail: 'thumb-current',
    url: 'https://youtube.test/current',
  });

  const added = await controller.addById('queued-song', {
    canonicalArtist: 'Queued Artist',
    canonicalTitle: 'Queued Title',
  });

  assert.equal(added.action, 'queued');
  assert.equal(added.position, 1);
  assert.equal(added.startedPlayback, false);
  assert.equal(queueManager.getNowPlaying()?.id, 'current');
  assert.deepEqual(queueManager.list().map((item) => item.id), ['queued-song']);
  assert.equal(queueManager.list()[0].artist, 'Queued Artist');
});

test('QueuePlaybackController keeps every queued item when addById runs concurrently', async () => {
  const queueManager = new QueueManager();
  const fakeMpv = new FakeMpv();
  const controller = new QueuePlaybackController(
    fakeMpv as never,
    queueManager,
    new SlowFakeYouTubeProvider() as never,
  );
  const ids = Array.from({ length: 20 }, (_, index) => `song-${index + 1}`);

  const added = await Promise.all(ids.map((id) => controller.addById(id, {
    canonicalArtist: `Artist ${id}`,
    canonicalTitle: `Title ${id}`,
  })));

  const state = queueManager.getState();
  const actualIds = [state.nowPlaying?.id, ...state.queue.map((item) => item.id)]
    .filter((id): id is string => Boolean(id))
    .sort();

  assert.equal(fakeMpv.playCalls.length, 1);
  assert.equal(added.filter((result) => result.startedPlayback).length, 1);
  assert.equal(state.queue.length, ids.length - 1);
  assert.deepEqual(actualIds, [...ids].sort());
});

test('QueuePlaybackController replaceCurrentTrack plays new track immediately', async () => {
  const queueManager = new QueueManager();
  const fakeMpv = new FakeMpv();
  const controller = new QueuePlaybackController(
    fakeMpv as never,
    queueManager,
    new FakeYouTubeProvider() as never,
  );

  queueManager.setNowPlaying({
    id: 'current',
    title: 'Current',
    artist: 'Current Artist',
    duration: 180,
    thumbnail: 'thumb-current',
    url: 'https://youtube.test/current',
  });

  const nowPlaying = await controller.replaceCurrentTrack('replacement', {
    canonicalArtist: 'Replacement Artist',
    canonicalTitle: 'Replacement Title',
  });

  assert.equal(nowPlaying.id, 'replacement');
  assert.equal(queueManager.getNowPlaying()?.id, 'replacement');
  assert.equal(queueManager.getNowPlaying()?.artist, 'Replacement Artist');
  assert.equal(fakeMpv.playCalls.length, 1);
});

test('QueuePlaybackController skip plays the next queued track', async () => {
  const queueManager = new QueueManager();
  const fakeMpv = new FakeMpv();
  const controller = new QueuePlaybackController(
    fakeMpv as never,
    queueManager,
    new FakeYouTubeProvider() as never,
  );

  const currentItem = {
    id: 'current',
    title: 'Current',
    artist: 'Artist current',
    duration: 180,
    thumbnail: 'thumb-current',
    url: 'https://youtube.test/current',
  };
  fakeMpv.currentTrack = currentItem;
  queueManager.setNowPlaying(currentItem);
  queueManager.add({
    id: 'next',
    title: 'Next',
    artist: 'Artist next',
    duration: 200,
    thumbnail: 'thumb-next',
    url: 'https://youtube.test/next',
  });

  const nextTrack = await controller.skip();

  assert.equal(fakeMpv.stopCalls, 1);
  assert.equal(nextTrack?.id, 'next');
  assert.equal(queueManager.getNowPlaying()?.id, 'next');
  assert.deepEqual(queueManager.getState().history.map((item) => item.id), ['current']);
});

test('QueuePlaybackController skip clears paused state before starting the next track', async () => {
  const queueManager = new QueueManager();
  const fakeMpv = new FakeMpv();
  const controller = new QueuePlaybackController(
    fakeMpv as never,
    queueManager,
    new FakeYouTubeProvider() as never,
  );

  const currentItem = {
    id: 'current',
    title: 'Current',
    artist: 'Artist current',
    duration: 180,
    thumbnail: 'thumb-current',
    url: 'https://youtube.test/current',
  };
  fakeMpv.currentTrack = currentItem;
  queueManager.setNowPlaying(currentItem);
  queueManager.add({
    id: 'next',
    title: 'Next',
    artist: 'Artist next',
    duration: 200,
    thumbnail: 'thumb-next',
    url: 'https://youtube.test/next',
  });
  fakeMpv.pause();

  const nextTrack = await controller.skip();

  assert.equal(nextTrack?.id, 'next');
  assert.equal(fakeMpv.resumeCalls, 1);
  assert.equal(fakeMpv.isPlaying, true);
  assert.equal(queueManager.getNowPlaying()?.id, 'next');
});

test('QueuePlaybackController skip does not orphan suppress count when mpv track already cleared', async () => {
  // Reproduces the race: song A finishes naturally (idle-active clears
  // mpv.currentTrack) right before skip() checks suppress+stop.
  // queueManager still thinks A is playing, but mpv already went idle.
  // Without the fix, suppress is called unconditionally, orphaning the
  // counter and swallowing song B's natural finish event.
  const queueManager = new QueueManager();
  const fakeMpv = new FakeMpv();
  const controller = new QueuePlaybackController(
    fakeMpv as never,
    queueManager,
    new FakeYouTubeProvider() as never,
  );

  // Queue state says A is playing, but mpv already went idle (currentTrack = null).
  // This is the exact state after an idle-active event clears mpv but before
  // handleStopped drains the playback mutex.
  queueManager.setNowPlaying({
    id: 'A', title: 'A', artist: 'Artist A',
    duration: 180, thumbnail: 'thumb-A', url: 'https://youtube.test/A',
  });
  fakeMpv.currentTrack = null; // mpv already idle
  queueManager.add({
    id: 'B', title: 'B', artist: 'Artist B',
    duration: 200, thumbnail: 'thumb-B', url: 'https://youtube.test/B',
  });
  queueManager.add({
    id: 'C', title: 'C', artist: 'Artist C',
    duration: 220, thumbnail: 'thumb-C', url: 'https://youtube.test/C',
  });

  const nextTrack = await controller.skip();

  // B should be playing
  assert.equal(nextTrack?.id, 'B');
  assert.equal(queueManager.getNowPlaying()?.id, 'B');

  // suppress+stop must NOT be called when mpv has no active track
  assert.equal(fakeMpv.suppressCalls, 0, 'suppress must not fire when mpv.currentTrack is null');
  assert.equal(fakeMpv.stopCalls, 0, 'stop must not fire when mpv.currentTrack is null');

  // Simulate B finishing naturally — must NOT be suppressed by orphaned count
  fakeMpv.emitStopped();
  await new Promise((resolve) => setTimeout(resolve, 50));

  assert.equal(queueManager.getNowPlaying()?.id, 'C', 'auto-advance to C must not be blocked');
});

test('QueuePlaybackController handleStopped is discarded when generation mismatches', async () => {
  // Verify the generation guard: a 'stopped' callback whose captured
  // generation doesn't match the current playGeneration is silently discarded.
  const queueManager = new QueueManager();
  const fakeMpv = new FakeMpv();
  const controller = new QueuePlaybackController(
    fakeMpv as never,
    queueManager,
    new FakeYouTubeProvider() as never,
  );

  const currentItem = {
    id: 'A', title: 'A', artist: 'Artist A',
    duration: 180, thumbnail: 'thumb-A', url: 'https://youtube.test/A',
  };
  fakeMpv.currentTrack = currentItem;
  queueManager.setNowPlaying(currentItem);
  queueManager.add({
    id: 'B', title: 'B', artist: 'Artist B',
    duration: 200, thumbnail: 'thumb-B', url: 'https://youtube.test/B',
  });

  // Skip: advances A→B and increments generation
  const nextTrack = await controller.skip();
  assert.equal(nextTrack?.id, 'B');
  assert.equal(queueManager.getNowPlaying()?.id, 'B');

  // Now emit a STALE 'stopped' that was captured with the OLD generation.
  // In reality this would have been captured before skip ran, but we can
  // simulate by calling the private handler directly with gen=0.
  // Instead, just emit a real stopped — it captures the CURRENT gen (=1).
  // Then skip again to bump gen to 2, making the pending handleStopped stale.
  fakeMpv.emitStopped(); // captures gen=1
  // Before handleStopped drains, skip again (bumps to gen=2)
  const skipPromise = controller.skip();
  await skipPromise;
  await new Promise((resolve) => setTimeout(resolve, 50));

  // The handleStopped(gen=1) ran but gen(1) !== playGeneration(2) → discarded.
  // Without the guard, handleStopped would have cleared the newly-playing track.
  // With an empty queue after B, nowPlaying should be null (skip returned null).
  // Key point: no crash, no double-finish corruption.
  assert.equal(queueManager.getState().history.filter((h) => h.id === 'B').length, 1,
    'B should appear in history exactly once, not double-finished');
});

test('QueuePlaybackController advances when playback stops naturally', async () => {
  const queueManager = new QueueManager();
  const fakeMpv = new FakeMpv();
  const controller = new QueuePlaybackController(
    fakeMpv as never,
    queueManager,
    new FakeYouTubeProvider() as never,
  );

  queueManager.setNowPlaying({
    id: 'current',
    title: 'Current',
    artist: 'Artist current',
    duration: 180,
    thumbnail: 'thumb-current',
    url: 'https://youtube.test/current',
  });
  queueManager.add({
    id: 'next',
    title: 'Next',
    artist: 'Artist next',
    duration: 200,
    thumbnail: 'thumb-next',
    url: 'https://youtube.test/next',
  });

  fakeMpv.emitStopped();
  await new Promise((resolve) => setTimeout(resolve, 0));

  assert.equal(fakeMpv.playCalls.length, 1);
  assert.equal(queueManager.getNowPlaying()?.id, 'next');
  assert.deepEqual(queueManager.getState().history.map((item) => item.id), ['current']);
});
```

## File: `src/queue/queue-playback-controller.ts`
```typescript
import type { MpvController } from '../audio/mpv-controller.js';
import { getHistoryStore } from '../history/history-store.js';
import { normalizeTrackId } from '../history/history-schema.js';
import { getAppleSearchProvider } from '../providers/apple-search-provider.js';
import type { AudioInfo, YouTubeProvider } from '../providers/youtube-provider.js';
import type { SearchResult } from '../providers/youtube-provider.js';
import { getWebServer } from '../web/web-server.js';
import type { QueueItem, QueueManager } from './queue-manager.js';

type PlaybackMeta = { context?: string; canonicalArtist?: string; canonicalTitle?: string };

function mapSearchResultToQueueItem(result: SearchResult): QueueItem {
  return {
    id: result.id,
    title: result.title,
    artist: result.artist,
    duration: Math.round(result.durationMs / 1000),
    thumbnail: result.thumbnail,
    url: result.url,
  };
}

export class QueuePlaybackController {
  private shuttingDown = false;
  private currentPlayId: number | null = null;
  private playbackMutation = Promise.resolve();
  // Pre-fetched audio for the next queued track (keyed by video ID)
  private prefetchedAudio: { id: string; audio: AudioInfo } | null = null;
  private prefetchInProgress: string | null = null;
  // Monotonic counter incremented by operations that explicitly take over
  // playback transitions (skip, stop-reset, replace).  A stale handleStopped
  // callback whose captured generation doesn't match is silently discarded.
  private playGeneration = 0;

  constructor(
    private readonly mpv: MpvController,
    private readonly queueManager: QueueManager,
    private readonly youtubeProvider: YouTubeProvider,
  ) {
    this.mpv.on('stopped', () => {
      const gen = this.playGeneration;
      void this.handleStopped(gen);
    });
  }

  async playById(
    id: string,
    extraMeta?: PlaybackMeta,
  ): Promise<QueueItem> {
    const resolved = await this.resolveQueueItem(id, extraMeta);
    return await this.withPlaybackMutation(async () => {
      this.startPlayback(resolved.item, resolved.audio, extraMeta);
      return resolved.item;
    });
  }

  async addById(
    id: string,
    extraMeta?: PlaybackMeta,
  ): Promise<{ item: QueueItem; action: 'queued'; position: number; startedPlayback: boolean }> {
    const resolved = await this.resolveQueueItem(id, extraMeta);
    return await this.withPlaybackMutation(async () => {
      const position = this.queueManager.add(resolved.item);

      if (!this.queueManager.getNowPlaying()) {
        await this.playNextQueuedTrackLocked({
          id: resolved.item.id,
          audio: resolved.audio,
          extraMeta,
        });
        return { item: resolved.item, action: 'queued', position, startedPlayback: true };
      }

      // If this is the next-up track, pre-fetch its audio
      if (position === 1) this.prefetchNextTrack();
      return { item: resolved.item, action: 'queued', position, startedPlayback: false };
    });
  }

  async queueByQuery(query: string): Promise<{ item: QueueItem; position: number }> {
    const results = await this.youtubeProvider.search(query, 1);
    if (results.length === 0) {
      throw new Error(`No results found for "${query}".`);
    }

    const item = mapSearchResultToQueueItem(results[0]);
    const position = this.queueManager.add(item);
    return { item, position };
  }

  async skip(): Promise<QueueItem | null> {
    return await this.withPlaybackMutation(async () => {
      // Record skip in history + taste feedback before stopping
      if (this.currentPlayId !== null) {
        try {
          const store = getHistoryStore();
          const nowPlaying = this.queueManager.getNowPlaying();
          if (store && nowPlaying) {
            const position = await this.mpv.getPosition().catch(() => 0);
            store.updatePlay(this.currentPlayId, { played_sec: Math.round(position), skipped: true });
          }
        } catch (err) {
          console.error('[agentune] Failed to record skip:', (err as Error).message);
        }
        this.currentPlayId = null;
      }

      // Bump generation AFTER the getPosition() await above so that any
      // 'stopped' event captured during that yield carries the OLD generation
      // and will be discarded when it finally enters the mutex.
      this.playGeneration++;

      if (this.queueManager.getNowPlaying()) {
        this.queueManager.finishCurrentTrack();
      }
      // Guard suppress+stop on mpv state (not queue state) to prevent an
      // orphaned suppressStoppedCount when an idle-active event fires during
      // the `await getPosition()` above, clearing mpv.currentTrack before we
      // reach this point.  Without this guard, stop() early-returns but the
      // counter is already incremented, swallowing the *next* track's natural
      // finish event and freezing auto-advance.
      if (this.mpv.getCurrentTrack()) {
        this.mpv.suppressNextStopped();
        this.mpv.stop();
      }

      return await this.playNextQueuedTrackLocked();
    });
  }

  async stopAndResetRuntimeState(): Promise<void> {
    await this.withPlaybackMutation(async () => {
      this.playGeneration++;
      this.prefetchedAudio = null;
      this.prefetchInProgress = null;
      await this.recordInterruptedPlay();

      if (this.mpv.isReady() && this.mpv.getCurrentTrack()) {
        this.mpv.suppressNextStopped();
        this.mpv.stop();
      }

      this.queueManager.reset();
    });
  }

  listQueue(): QueueItem[] {
    return this.queueManager.list();
  }

  clearForShutdown(): void {
    this.shuttingDown = true;
  }

  private async handleStopped(generation: number): Promise<void> {
    await this.withPlaybackMutation(async () => {
      if (this.shuttingDown) {
        return;
      }

      // If another operation (skip, replace, stop-reset) already took over
      // the playback transition, this callback is stale — discard it.
      if (generation !== this.playGeneration) {
        return;
      }

      // Record natural finish in history + taste feedback
      if (this.currentPlayId !== null) {
        try {
          const store = getHistoryStore();
          const nowPlaying = this.queueManager.getNowPlaying();
          if (store && nowPlaying) {
            store.updatePlay(this.currentPlayId, { played_sec: nowPlaying.duration, skipped: false });
          }
        } catch (err) {
          console.error('[agentune] Failed to record finish:', (err as Error).message);
        }
        this.currentPlayId = null;
      }

      this.queueManager.finishCurrentTrack();
      await this.playNextQueuedTrackLocked();
    });
  }

  /** Fetch genre from Apple iTunes and update track tags (fire-and-forget). */
  private async enrichTrackTags(artist: string, title: string): Promise<void> {
    const apple = getAppleSearchProvider();
    const store = getHistoryStore();
    if (!apple || !store) return;

    try {
      const genres = await apple.getTrackGenre(artist, title);
      if (genres.length === 0) return;
      const trackId = normalizeTrackId(artist, title);
      store.updateTrackTags(trackId, genres);
    } catch (err) {
      console.error('[agentune] Tag enrichment failed:', (err as Error).message);
    }
  }

  private async playNextQueuedTrackLocked(
    prefetched?: { id: string; audio: AudioInfo; extraMeta?: PlaybackMeta },
  ): Promise<QueueItem | null> {
    const nextItem = this.queueManager.next();
    if (!nextItem) {
      this.queueManager.clearNowPlaying();
      return null;
    }

    if (prefetched && prefetched.id === nextItem.id) {
      this.startPlayback(nextItem, prefetched.audio, prefetched.extraMeta);
      return nextItem;
    }

    const nextExtraMeta = {
      context: nextItem.context,
      canonicalArtist: nextItem.artist,
      canonicalTitle: nextItem.title,
    };
    const resolved = await this.resolveQueueItem(nextItem.id, nextExtraMeta);
    this.startPlayback(resolved.item, resolved.audio, nextExtraMeta);
    return resolved.item;
  }

  private async resolveQueueItem(
    id: string,
    extraMeta?: PlaybackMeta,
  ): Promise<{ item: QueueItem; audio: AudioInfo }> {
    // Use pre-fetched audio if available for this track
    let audio: AudioInfo;
    if (this.prefetchedAudio && this.prefetchedAudio.id === id) {
      audio = this.prefetchedAudio.audio;
      this.prefetchedAudio = null;
      console.error('[agentune] Using pre-fetched audio for:', id);
    } else {
      audio = await this.youtubeProvider.getAudioUrl(id);
    }
    return {
      audio,
      item: {
        id,
        title: extraMeta?.canonicalTitle ?? audio.title,
        artist: extraMeta?.canonicalArtist ?? audio.artist,
        duration: audio.duration,
        thumbnail: audio.thumbnail,
        url: `https://www.youtube.com/watch?v=${id}`,
        context: extraMeta?.context,
      },
    };
  }

  /** Pre-fetch the next queued track's audio URL in the background. */
  private prefetchNextTrack(): void {
    const nextItem = this.queueManager.peek();
    if (!nextItem) return;
    if (this.prefetchedAudio?.id === nextItem.id) return; // already cached
    if (this.prefetchInProgress === nextItem.id) return;  // already fetching

    this.prefetchInProgress = nextItem.id;
    console.error('[agentune] Pre-fetching audio for next track:', nextItem.title);

    this.youtubeProvider.getAudioUrl(nextItem.id).then((audio) => {
      // Only store if the queue hasn't changed
      if (this.queueManager.peek()?.id === nextItem.id) {
        this.prefetchedAudio = { id: nextItem.id, audio };
        console.error('[agentune] Pre-fetch complete for:', nextItem.title);
      }
    }).catch((err) => {
      console.error('[agentune] Pre-fetch failed:', (err as Error).message);
    }).finally(() => {
      this.prefetchInProgress = null;
    });
  }

  private async recordInterruptedPlay(): Promise<void> {
    if (this.currentPlayId === null) return;

    try {
      const store = getHistoryStore();
      const nowPlaying = this.queueManager.getNowPlaying();
      if (store && nowPlaying) {
        const position = await this.mpv.getPosition().catch(() => 0);
        store.updatePlay(this.currentPlayId, { played_sec: Math.round(position), skipped: true });
      }
    } catch (err) {
      console.error('[agentune] Failed to record interrupted play:', (err as Error).message);
    }

    this.currentPlayId = null;
  }

  private startPlayback(
    queueItem: QueueItem,
    audio: AudioInfo,
    extraMeta?: PlaybackMeta,
  ): void {
    // mpv keeps its pause property until explicitly cleared, so a paused track
    // followed by skip would otherwise load the next song in a paused state.
    this.mpv.resume();
    this.mpv.play(audio.streamUrl, queueItem);
    this.queueManager.setNowPlaying(queueItem);
    getWebServer()?.openDashboardOnce();

    try {
      const store = getHistoryStore();
      if (store) {
        const canonical = extraMeta?.canonicalArtist && extraMeta?.canonicalTitle
          ? { artist: extraMeta.canonicalArtist, title: extraMeta.canonicalTitle }
          : undefined;
        this.currentPlayId = store.recordPlay(
          {
            title: queueItem.title,
            artist: queueItem.artist,
            duration: queueItem.duration,
            thumbnail: queueItem.thumbnail,
            ytVideoId: queueItem.id,
          },
          { context: queueItem.context, source: 'playById' },
          canonical,
        );
      }
    } catch (err) {
      console.error('[agentune] Failed to record play:', (err as Error).message);
    }

    this.enrichTrackTags(queueItem.artist, queueItem.title);

    // Pre-fetch next track's audio URL for seamless transitions
    this.prefetchNextTrack();
  }

  async replaceCurrentTrack(
    id: string,
    extraMeta?: PlaybackMeta,
  ): Promise<QueueItem> {
    const resolved = await this.resolveQueueItem(id, extraMeta);
    return await this.withPlaybackMutation(async () => {
      this.playGeneration++;
      await this.recordInterruptedPlay();
      this.startPlayback(resolved.item, resolved.audio, extraMeta);
      return resolved.item;
    });
  }

  private async withPlaybackMutation<T>(operation: () => Promise<T>): Promise<T> {
    const previous = this.playbackMutation;
    let release!: () => void;
    this.playbackMutation = new Promise<void>((resolve) => {
      release = resolve;
    });

    await previous;

    try {
      return await operation();
    } finally {
      release();
    }
  }
}

let queuePlaybackController: QueuePlaybackController | null = null;

export function createQueuePlaybackController(
  mpv: MpvController,
  queueManager: QueueManager,
  youtubeProvider: YouTubeProvider,
): QueuePlaybackController {
  if (!queuePlaybackController) {
    queuePlaybackController = new QueuePlaybackController(mpv, queueManager, youtubeProvider);
  }
  return queuePlaybackController;
}

export function getQueuePlaybackController(): QueuePlaybackController | null {
  return queuePlaybackController;
}
```

## File: `src/runtime/runtime-config.test.ts`
```typescript
import assert from 'node:assert/strict';
import fs from 'fs';
import os from 'os';
import path from 'path';
import test from 'node:test';
import { loadRuntimeConfig, resetRuntimeConfigCache } from './runtime-config.js';

function createTempDataDir(): string {
  return fs.mkdtempSync(path.join(os.tmpdir(), 'agentune-runtime-config-'));
}

function cleanupDataDir(dataDir: string): void {
  try {
    fs.rmSync(dataDir, { recursive: true, force: true });
  } catch {
    // Ignore cleanup errors in tests.
  }
}

test('loadRuntimeConfig creates default config when missing', () => {
  const previous = process.env.AGENTUNE_DATA_DIR;
  const dataDir = createTempDataDir();
  process.env.AGENTUNE_DATA_DIR = dataDir;
  resetRuntimeConfigCache();

  try {
    const config = loadRuntimeConfig();
    const configPath = path.join(dataDir, 'config.json');
    assert.deepEqual(config, {
      dashboardPort: 3737,
      daemonPort: 3747,
      defaultVolume: 80,
      autoStartDaemon: true,
      discoverRanking: { exploration: 0.35, variety: 0.55, loyalty: 0.65 },
    });
    assert.equal(fs.existsSync(configPath), true);
    assert.deepEqual(JSON.parse(fs.readFileSync(configPath, 'utf8')), config);
  } finally {
    if (previous === undefined) delete process.env.AGENTUNE_DATA_DIR;
    else process.env.AGENTUNE_DATA_DIR = previous;
    resetRuntimeConfigCache();
    cleanupDataDir(dataDir);
  }
});

test('loadRuntimeConfig rejects invalid port values', () => {
  const previous = process.env.AGENTUNE_DATA_DIR;
  const dataDir = createTempDataDir();
  process.env.AGENTUNE_DATA_DIR = dataDir;
  fs.writeFileSync(path.join(dataDir, 'config.json'), JSON.stringify({ dashboardPort: 0, daemonPort: 3747 }));
  resetRuntimeConfigCache();

  try {
    assert.throws(() => loadRuntimeConfig(), /dashboardPort must be an integer between 1 and 65535/i);
  } finally {
    if (previous === undefined) delete process.env.AGENTUNE_DATA_DIR;
    else process.env.AGENTUNE_DATA_DIR = previous;
    resetRuntimeConfigCache();
    cleanupDataDir(dataDir);
  }
});

test('loadRuntimeConfig rejects invalid auto-start values', () => {
  const previous = process.env.AGENTUNE_DATA_DIR;
  const dataDir = createTempDataDir();
  process.env.AGENTUNE_DATA_DIR = dataDir;
  fs.writeFileSync(path.join(dataDir, 'config.json'), JSON.stringify({
    dashboardPort: 3737,
    daemonPort: 3747,
    autoStartDaemon: 'yes',
  }));
  resetRuntimeConfigCache();

  try {
    assert.throws(() => loadRuntimeConfig(), /autoStartDaemon must be a boolean/i);
  } finally {
    if (previous === undefined) delete process.env.AGENTUNE_DATA_DIR;
    else process.env.AGENTUNE_DATA_DIR = previous;
    resetRuntimeConfigCache();
    cleanupDataDir(dataDir);
  }
});

test('loadRuntimeConfig merges missing config fields, writes them back, and rejects invalid ranking values', () => {
  const previous = process.env.AGENTUNE_DATA_DIR;
  const dataDir = createTempDataDir();
  const configPath = path.join(dataDir, 'config.json');
  process.env.AGENTUNE_DATA_DIR = dataDir;
  fs.writeFileSync(configPath, JSON.stringify({
    dashboardPort: 3838,
    daemonPort: 3848,
    discoverRanking: { exploration: 2 },
  }));
  resetRuntimeConfigCache();

  try {
    assert.throws(() => loadRuntimeConfig(), /discoverRanking\.exploration must be a number between 0 and 1/i);
    fs.writeFileSync(configPath, JSON.stringify({
      dashboardPort: 3838,
      daemonPort: 3848,
      defaultVolume: 60,
      discoverRanking: { variety: 0.75 },
    }));
    resetRuntimeConfigCache();

    const config = loadRuntimeConfig();
    assert.deepEqual(config, {
      dashboardPort: 3838,
      daemonPort: 3848,
      defaultVolume: 60,
      autoStartDaemon: true,
      discoverRanking: { exploration: 0.35, variety: 0.75, loyalty: 0.65 },
    });
    assert.deepEqual(JSON.parse(fs.readFileSync(configPath, 'utf8')), config);
  } finally {
    if (previous === undefined) delete process.env.AGENTUNE_DATA_DIR;
    else process.env.AGENTUNE_DATA_DIR = previous;
    resetRuntimeConfigCache();
    cleanupDataDir(dataDir);
  }
});
```

## File: `src/runtime/runtime-config.ts`
```typescript
import fs from 'fs';
import { getRuntimeConfigPath } from './runtime-data-paths.js';

export interface DiscoverRankingConfig {
  exploration: number;
  variety: number;
  loyalty: number;
}

export interface RuntimeConfig {
  dashboardPort: number;
  daemonPort: number;
  defaultVolume: number;
  autoStartDaemon: boolean;
  discoverRanking: DiscoverRankingConfig;
}

export const DEFAULT_DISCOVER_RANKING_CONFIG: DiscoverRankingConfig = {
  exploration: 0.35,
  variety: 0.55,
  loyalty: 0.65,
};

export const DEFAULT_RUNTIME_CONFIG: RuntimeConfig = {
  dashboardPort: 3737,
  daemonPort: 3747,
  defaultVolume: 80,
  autoStartDaemon: true,
  discoverRanking: { ...DEFAULT_DISCOVER_RANKING_CONFIG },
};

let runtimeConfigCache: RuntimeConfig | null = null;

export function loadRuntimeConfig(): RuntimeConfig {
  if (runtimeConfigCache) {
    return runtimeConfigCache;
  }

  const configPath = getRuntimeConfigPath();
  if (!fs.existsSync(configPath)) {
    writeRuntimeConfig(configPath, DEFAULT_RUNTIME_CONFIG);
    runtimeConfigCache = { ...DEFAULT_RUNTIME_CONFIG };
    return runtimeConfigCache;
  }

  const rawConfig = fs.readFileSync(configPath, 'utf8');
  let parsed: unknown;
  try {
    parsed = JSON.parse(rawConfig);
  } catch (error) {
    throw new Error(`Invalid runtime config at ${configPath}: ${(error as Error).message}`);
  }

  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
    throw new Error(`Invalid runtime config at ${configPath}: expected a JSON object.`);
  }

  const config = parsed as Partial<Record<keyof RuntimeConfig, unknown>>;
  runtimeConfigCache = {
    dashboardPort: validatePort(config.dashboardPort ?? DEFAULT_RUNTIME_CONFIG.dashboardPort, 'dashboardPort'),
    daemonPort: validatePort(config.daemonPort ?? DEFAULT_RUNTIME_CONFIG.daemonPort, 'daemonPort'),
    defaultVolume: validateVolume(config.defaultVolume ?? DEFAULT_RUNTIME_CONFIG.defaultVolume, 'defaultVolume'),
    autoStartDaemon: validateBoolean(
      config.autoStartDaemon ?? DEFAULT_RUNTIME_CONFIG.autoStartDaemon,
      'autoStartDaemon',
    ),
    discoverRanking: validateDiscoverRanking(config.discoverRanking),
  };

  if (shouldWriteRuntimeConfig(rawConfig, runtimeConfigCache)) {
    writeRuntimeConfig(configPath, runtimeConfigCache);
  }
  return runtimeConfigCache;
}

export function resetRuntimeConfigCache(): void {
  runtimeConfigCache = null;
}

function validatePort(value: unknown, key: keyof RuntimeConfig): number {
  if (!Number.isInteger(value) || (value as number) < 1 || (value as number) > 65535) {
    throw new Error(`Invalid runtime config: ${key} must be an integer between 1 and 65535.`);
  }
  return value as number;
}

function validateVolume(value: unknown, key: 'defaultVolume'): number {
  if (!Number.isInteger(value) || (value as number) < 0 || (value as number) > 100) {
    throw new Error(`Invalid runtime config: ${key} must be an integer between 0 and 100.`);
  }
  return value as number;
}

function validateBoolean(value: unknown, key: 'autoStartDaemon'): boolean {
  if (typeof value !== 'boolean') {
    throw new Error(`Invalid runtime config: ${key} must be a boolean.`);
  }
  return value;
}

function validateDiscoverRanking(value: unknown): DiscoverRankingConfig {
  if (value === undefined) {
    return { ...DEFAULT_DISCOVER_RANKING_CONFIG };
  }
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    throw new Error('Invalid runtime config: discoverRanking must be an object.');
  }

  const ranking = value as Partial<Record<keyof DiscoverRankingConfig, unknown>>;
  return {
    exploration: validateUnitInterval(
      ranking.exploration ?? DEFAULT_DISCOVER_RANKING_CONFIG.exploration,
      'discoverRanking.exploration',
    ),
    variety: validateUnitInterval(
      ranking.variety ?? DEFAULT_DISCOVER_RANKING_CONFIG.variety,
      'discoverRanking.variety',
    ),
    loyalty: validateUnitInterval(
      ranking.loyalty ?? DEFAULT_DISCOVER_RANKING_CONFIG.loyalty,
      'discoverRanking.loyalty',
    ),
  };
}

function validateUnitInterval(value: unknown, key: string): number {
  if (typeof value !== 'number' || Number.isNaN(value) || value < 0 || value > 1) {
    throw new Error(`Invalid runtime config: ${key} must be a number between 0 and 1.`);
  }
  return value;
}

function writeRuntimeConfig(configPath: string, config: RuntimeConfig): void {
  fs.writeFileSync(configPath, `${JSON.stringify(config, null, 2)}\n`, 'utf8');
}

function shouldWriteRuntimeConfig(rawConfig: string, config: RuntimeConfig): boolean {
  return rawConfig !== `${JSON.stringify(config, null, 2)}\n`;
}
```

## File: `src/runtime/runtime-data-paths.ts`
```typescript
import fs from 'fs';
import os from 'os';
import path from 'path';

const DATA_DIR_ENV = 'AGENTUNE_DATA_DIR';
const DEFAULT_DATA_DIR_NAME = '.agentune';

export function getDataDir(): string {
  return process.env[DATA_DIR_ENV] || path.join(os.homedir(), DEFAULT_DATA_DIR_NAME);
}

export function ensureDataDir(): string {
  const dataDir = getDataDir();
  fs.mkdirSync(dataDir, { recursive: true });
  return dataDir;
}

export function getRuntimeConfigPath(): string {
  return path.join(ensureDataDir(), 'config.json');
}

export function getHistoryDbPath(): string {
  return path.join(ensureDataDir(), 'history.db');
}

export function getDaemonLogPath(): string {
  return path.join(ensureDataDir(), 'daemon.log');
}

export function getPidFilePath(): string {
  return path.join(ensureDataDir(), 'daemon.pid');
}
```

## File: `src/taste/discover-batch-builder.ts`
```typescript
import type { HistoryStore } from '../history/history-store.js';
import type { AppleTrack } from '../providers/apple-search-provider.js';

export interface DiscoverCandidate {
  title: string;
  artist: string;
  tags: string[];
  provider: 'apple';
  appleTrackId?: number;
  appleArtistId?: number;
}

export interface DiscoverBatchParams {
  artist?: string;
  keywords?: string[];
}

interface DiscoverAppleProvider {
  getArtistTracks(artist: string, limit?: number): Promise<AppleTrack[]>;
  searchByGenre(genre: string, limit?: number): Promise<AppleTrack[]>;
}

const MAX_APPLE_CALLS = 6;
const ARTIST_RESULT_LIMIT = 15;
const GENRE_RESULT_LIMIT = 10;

export class DiscoverBatchBuilder {
  constructor(
    private readonly apple: DiscoverAppleProvider,
    private readonly historyStore: Pick<HistoryStore, 'getTopArtists' | 'getTopTags'>,
  ) {}

  async buildBatches(params: DiscoverBatchParams): Promise<DiscoverCandidate[]> {
    const normalizedArtist = normalizeSeed(params.artist);
    const normalizedKeywords = normalizeSeeds(params.keywords ?? []);

    let artistSeeds = normalizedArtist ? [normalizedArtist] : [];
    let keywordSeeds = normalizedKeywords;

    if (artistSeeds.length === 0 && keywordSeeds.length === 0) {
      const defaultSeeds = this.getDefaultSeeds();
      artistSeeds = defaultSeeds.artistSeeds;
      keywordSeeds = defaultSeeds.keywordSeeds;
    }

    if (artistSeeds.length === 0 && keywordSeeds.length === 0) {
      return [];
    }

    const selectedArtistSeeds = artistSeeds.slice(0, MAX_APPLE_CALLS);
    const remainingCalls = MAX_APPLE_CALLS - selectedArtistSeeds.length;
    const selectedKeywordSeeds = keywordSeeds.slice(0, remainingCalls);

    const artistPromises = selectedArtistSeeds.map((artist) => this.loadArtistCandidates(artist));
    const keywordPromises = selectedKeywordSeeds.map((keyword) => this.loadKeywordCandidates(keyword));
    const batches = await Promise.all([...artistPromises, ...keywordPromises]);

    return batches.flat();
  }

  private getDefaultSeeds(): { artistSeeds: string[]; keywordSeeds: string[] } {
    const artistSeeds = normalizeSeeds(this.historyStore.getTopArtists(3).map((artist) => artist.artist));
    const keywordSeeds = normalizeSeeds(this.historyStore.getTopTags(3).map((tag) => tag.tag));
    return { artistSeeds, keywordSeeds };
  }

  private async loadArtistCandidates(artist: string): Promise<DiscoverCandidate[]> {
    try {
      const tracks = await this.apple.getArtistTracks(artist, ARTIST_RESULT_LIMIT);
      return tracks.map((track) => mapArtistTrack(track));
    } catch (err) {
      console.error(`[agentune] Discover artist batch failed for "${artist}": ${(err as Error).message}`);
      return [];
    }
  }

  private async loadKeywordCandidates(keyword: string): Promise<DiscoverCandidate[]> {
    try {
      const tracks = await this.apple.searchByGenre(keyword, GENRE_RESULT_LIMIT);
      return tracks.map((track) => mapKeywordTrack(track, keyword));
    } catch (err) {
      console.error(`[agentune] Discover keyword batch failed for "${keyword}": ${(err as Error).message}`);
      return [];
    }
  }
}

function mapArtistTrack(track: AppleTrack): DiscoverCandidate {
  return {
    title: track.title,
    artist: track.artist,
    tags: collectTags(track.genre),
    provider: 'apple',
    appleTrackId: track.trackId,
    appleArtistId: track.artistId,
  };
}

function mapKeywordTrack(track: AppleTrack, keyword: string): DiscoverCandidate {
  return {
    title: track.title,
    artist: track.artist,
    tags: collectTags(keyword, track.genre),
    provider: 'apple',
    appleTrackId: track.trackId,
    appleArtistId: track.artistId,
  };
}

function collectTags(...values: Array<string | undefined>): string[] {
  const seen = new Set<string>();
  const tags: string[] = [];

  for (const value of values) {
    const normalized = normalizeSeed(value);
    if (!normalized) continue;
    const key = normalized.toLowerCase();
    if (seen.has(key)) continue;
    seen.add(key);
    tags.push(normalized);
  }

  return tags.length > 0 ? tags : ['unknown'];
}

function normalizeSeeds(values: string[]): string[] {
  const seen = new Set<string>();
  const normalizedValues: string[] = [];

  for (const value of values) {
    const normalized = normalizeSeed(value);
    if (!normalized) continue;
    const key = normalized.toLowerCase();
    if (seen.has(key)) continue;
    seen.add(key);
    normalizedValues.push(normalized);
  }

  return normalizedValues;
}

function normalizeSeed(value?: string): string | undefined {
  const normalized = value?.trim();
  return normalized ? normalized : undefined;
}
```

## File: `src/taste/discover-merge-and-dedup.ts`
```typescript
import type { DiscoverCandidate } from './discover-batch-builder.js';

export function mergeAndDedup(candidates: DiscoverCandidate[]): DiscoverCandidate[] {
  const deduped = deduplicateCandidates(candidates);
  return interleaveArtists(deduped);
}

function deduplicateCandidates(candidates: DiscoverCandidate[]): DiscoverCandidate[] {
  const seen = new Map<string, DiscoverCandidate>();
  const deduped: DiscoverCandidate[] = [];

  for (const candidate of candidates) {
    const key = normalizeCandidateKey(candidate);
    const existingCandidate = seen.get(key);
    if (existingCandidate) {
      existingCandidate.tags = mergeTags(existingCandidate.tags, candidate.tags);
      existingCandidate.appleTrackId ??= candidate.appleTrackId;
      existingCandidate.appleArtistId ??= candidate.appleArtistId;
      continue;
    }

    const nextCandidate = { ...candidate, tags: [...candidate.tags] };
    seen.set(key, nextCandidate);
    deduped.push(nextCandidate);
  }

  return deduped;
}

function interleaveArtists(candidates: DiscoverCandidate[]): DiscoverCandidate[] {
  const grouped = new Map<string, DiscoverCandidate[]>();
  const artistOrder: string[] = [];

  for (const candidate of candidates) {
    const artistKey = normalizeValue(candidate.artist);
    const artistCandidates = grouped.get(artistKey);
    if (!artistCandidates) {
      grouped.set(artistKey, [candidate]);
      artistOrder.push(artistKey);
      continue;
    }

    if (artistCandidates.length < 3) {
      artistCandidates.push(candidate);
    }
  }

  const merged: DiscoverCandidate[] = [];
  let hasRemaining = true;

  while (hasRemaining) {
    hasRemaining = false;
    for (const artistKey of artistOrder) {
      const artistCandidates = grouped.get(artistKey);
      const nextCandidate = artistCandidates?.shift();
      if (!nextCandidate) continue;
      merged.push(nextCandidate);
      hasRemaining = true;
    }
  }

  return merged;
}

function normalizeCandidateKey(candidate: DiscoverCandidate): string {
  return `${normalizeValue(candidate.artist)}::${normalizeValue(candidate.title)}`;
}

function mergeTags(currentTags: string[], nextTags: string[]): string[] {
  const mergedTags: string[] = [];
  const seen = new Set<string>();

  for (const tag of [...currentTags, ...nextTags]) {
    const normalizedTag = normalizeValue(tag);
    if (!normalizedTag || seen.has(normalizedTag)) continue;
    seen.add(normalizedTag);
    mergedTags.push(tag);
  }

  return mergedTags;
}

function normalizeValue(value: string): string {
  return value.toLowerCase().trim().replace(/\s+/g, ' ');
}
```

## File: `src/taste/discover-pagination-cache.ts`
```typescript
import type { DiscoverCandidate } from './discover-batch-builder.js';

export interface DiscoverPaginationParams {
  artist?: string;
  keywords?: string[];
}

interface SnapshotEntry {
  candidates: DiscoverCandidate[];
  createdAt: number;
}

export class DiscoverPaginationCache {
  private readonly snapshots = new Map<string, SnapshotEntry>();
  private accessOrder: string[] = [];

  constructor(
    private readonly ttlMs = 5 * 60 * 1000,
    private readonly maxEntries = 10,
  ) {}

  getPage(
    params: DiscoverPaginationParams,
    page: number,
    limit: number,
  ): { candidates: DiscoverCandidate[]; hasMore: boolean } | null {
    const key = this.computeKey(params);
    const snapshot = this.snapshots.get(key);
    if (!snapshot) return null;

    if (Date.now() - snapshot.createdAt > this.ttlMs) {
      this.deleteSnapshot(key);
      return null;
    }

    this.touchKey(key);
    const startIndex = (page - 1) * limit;
    const endIndex = startIndex + limit;

    return {
      candidates: snapshot.candidates.slice(startIndex, endIndex),
      hasMore: endIndex < snapshot.candidates.length,
    };
  }

  setSnapshot(params: DiscoverPaginationParams, candidates: DiscoverCandidate[]): void {
    if (candidates.length === 0) return;

    const key = this.computeKey(params);
    if (!this.snapshots.has(key) && this.snapshots.size >= this.maxEntries) {
      const evictedKey = this.accessOrder.shift();
      if (evictedKey) this.snapshots.delete(evictedKey);
    }

    this.snapshots.set(key, {
      candidates: [...candidates],
      createdAt: Date.now(),
    });
    this.touchKey(key);
  }

  invalidate(): void {
    this.snapshots.clear();
    this.accessOrder = [];
  }

  private computeKey(params: DiscoverPaginationParams): string {
    const artist = normalizeValue(params.artist);
    const keywords = [...new Set((params.keywords ?? []).map((keyword) => normalizeValue(keyword)).filter(Boolean))]
      .sort()
      .join(',');
    return `${artist}|${keywords}`;
  }

  private deleteSnapshot(key: string): void {
    this.snapshots.delete(key);
    this.accessOrder = this.accessOrder.filter((entry) => entry !== key);
  }

  private touchKey(key: string): void {
    this.accessOrder = this.accessOrder.filter((entry) => entry !== key);
    this.accessOrder.push(key);
  }
}

let discoverPaginationCache: DiscoverPaginationCache | null = null;

export function getDiscoverPaginationCache(): DiscoverPaginationCache {
  if (!discoverPaginationCache) {
    discoverPaginationCache = new DiscoverPaginationCache();
  }
  return discoverPaginationCache;
}

export function invalidateDiscoverCache(): void {
  getDiscoverPaginationCache().invalidate();
}

function normalizeValue(value?: string): string {
  return value?.toLowerCase().trim() ?? '';
}
```

## File: `src/taste/discover-pipeline.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
import type { BatchTrackStats } from '../history/history-store.js';
import { DiscoverBatchBuilder } from './discover-batch-builder.js';
import { DiscoverPaginationCache } from './discover-pagination-cache.js';
import { DiscoverPipeline } from './discover-pipeline.js';

class FakeAppleProvider {
  public artistCalls: string[] = [];
  public genreCalls: string[] = [];

  async getArtistTracks(artist: string): Promise<Array<{
    title: string;
    artist: string;
    album: string;
    genre: string;
    durationMs: number;
    artwork: string;
    trackId: number;
    artistId: number;
  }>> {
    this.artistCalls.push(artist);
    return [
      { title: `${artist} Song 1`, artist, album: 'Album', genre: 'ambient', durationMs: 200000, artwork: '', trackId: 1, artistId: 10 },
      { title: `${artist} Song 2`, artist, album: 'Album', genre: 'ambient', durationMs: 200000, artwork: '', trackId: 2, artistId: 10 },
      { title: `${artist} Song 3`, artist, album: 'Album', genre: 'ambient', durationMs: 200000, artwork: '', trackId: 3, artistId: 10 },
    ];
  }

  async searchByGenre(genre: string): Promise<Array<{
    title: string;
    artist: string;
    album: string;
    genre: string;
    durationMs: number;
    artwork: string;
    trackId: number;
    artistId: number;
  }>> {
    this.genreCalls.push(genre);
    return [
      { title: `${genre} Pulse`, artist: `${genre} Artist`, album: 'Album', genre, durationMs: 210000, artwork: '', trackId: 11, artistId: 21 },
      { title: `${genre} Pulse`, artist: `${genre} Artist`, album: 'Album', genre, durationMs: 210000, artwork: '', trackId: 12, artistId: 21 },
      { title: `${genre} Drift`, artist: `${genre} Artist`, album: 'Album', genre, durationMs: 210000, artwork: '', trackId: 13, artistId: 21 },
      { title: `${genre} Glow`, artist: `${genre} Artist`, album: 'Album', genre, durationMs: 210000, artwork: '', trackId: 14, artistId: 21 },
    ];
  }
}

function createStore(overrides?: {
  topArtists?: Array<{ artist: string; plays: number; avgCompletion: number }>;
  topTags?: Array<{ tag: string; frequency: number }>;
  recentCount?: number;
}): {
  getTopArtists: (limit?: number) => Array<{ artist: string; plays: number; avgCompletion: number }>;
  getTopTags: (limit?: number) => Array<{ tag: string; frequency: number }>;
  getRecentPlaysDetailed: (limit?: number) => Array<{ title: string; artist: string; completion: number; skipped: boolean; playedAt: number; tags: string[] }>;
  batchGetTrackStats: (trackIds: string[]) => Map<string, BatchTrackStats>;
} {
  return {
    getTopArtists: () => overrides?.topArtists ?? [{ artist: 'History Artist', plays: 5, avgCompletion: 0.9 }],
    getTopTags: () => overrides?.topTags ?? [{ tag: 'ambient', frequency: 5 }],
    getRecentPlaysDetailed: () => Array.from({ length: overrides?.recentCount ?? 10 }, (_, index) => ({
      title: `Recent ${index}`,
      artist: `Artist ${index}`,
      completion: 0.9,
      skipped: false,
      playedAt: Date.now() - index * 1000,
      tags: ['ambient'],
    })),
    batchGetTrackStats: (trackIds: string[]) => new Map(trackIds.map((trackId, index) => [trackId, {
      trackId,
      playCount: index === 0 ? 5 : 0,
      avgCompletion: index === 0 ? 0.9 : 0.5,
      skipRate: 0,
      hoursSinceLastPlay: Infinity,
    }])),
  };
}

function createPipeline(apple: FakeAppleProvider, store = createStore()): DiscoverPipeline {
  const batchBuilder = new DiscoverBatchBuilder(apple as never, store as never);
  return new DiscoverPipeline(
    batchBuilder,
    store as never,
    { exploration: 0.35, variety: 0.55, loyalty: 0.65 },
    new DiscoverPaginationCache(),
  );
}

test('DiscoverPipeline returns flat paginated candidates without internal Apple IDs', async () => {
  const pipeline = createPipeline(new FakeAppleProvider());
  const result = await pipeline.discover({ artist: 'Nils Frahm', limit: 2 });

  assert.equal(result.page, 1);
  assert.equal(result.limit, 2);
  assert.equal(result.candidates.length, 2);
  assert.equal(result.candidates[0]?.provider, 'apple');
  assert.equal(result.nextGuide, 'Pick from these candidates or call discover with the next page.');
  assert.ok(!('appleTrackId' in result.candidates[0]!));
});

test('DiscoverPipeline uses history seeds when artist and keywords are omitted', async () => {
  const apple = new FakeAppleProvider();
  const pipeline = createPipeline(apple);

  const result = await pipeline.discover({});

  assert.ok(result.candidates.length > 0);
  assert.deepEqual(apple.artistCalls, ['History Artist']);
  assert.deepEqual(apple.genreCalls, ['ambient']);
});

test('DiscoverPipeline paginates from cache without re-querying Apple', async () => {
  const apple = new FakeAppleProvider();
  const pipeline = createPipeline(apple);

  const pageOne = await pipeline.discover({ keywords: ['ambient'], limit: 2 });
  const callsAfterPageOne = apple.genreCalls.length + apple.artistCalls.length;
  const pageTwo = await pipeline.discover({ keywords: ['ambient'], page: 2, limit: 2 });

  assert.notDeepEqual(pageOne.candidates, pageTwo.candidates);
  assert.equal(apple.genreCalls.length + apple.artistCalls.length, callsAfterPageOne);
});

test('DiscoverPipeline marks page overflow as page exhaustion instead of cold-start empty', async () => {
  const pipeline = createPipeline(new FakeAppleProvider());

  await pipeline.discover({ keywords: ['ambient'], limit: 2 });
  const overflow = await pipeline.discover({ keywords: ['ambient'], page: 10, limit: 2 });

  assert.equal(overflow.candidates.length, 0);
  assert.equal(overflow.emptyReason, 'page_exhausted');
  assert.equal(
    overflow.nextGuide,
    'No more results on this page. Go back to an earlier page or improve artist/keywords input.',
  );
});

test('DiscoverPipeline returns empty results when there is no history and no explicit seeds', async () => {
  const pipeline = createPipeline(
    new FakeAppleProvider(),
    createStore({ topArtists: [], topTags: [] }),
  );

  const result = await pipeline.discover({});

  assert.equal(result.candidates.length, 0);
  assert.equal(result.hasMore, false);
  assert.equal(
    result.nextGuide,
    'No candidates found. Improve artist/keywords input or build more listening history first.',
  );
});

test('DiscoverPipeline deduplicates repeated tracks and caps artist presence at three', async () => {
  const apple = new FakeAppleProvider();
  const pipeline = createPipeline(apple);

  const result = await pipeline.discover({ keywords: ['ambient'], limit: 10 });
  const ambientArtistCount = result.candidates.filter((candidate) => candidate.artist === 'ambient Artist').length;

  assert.equal(ambientArtistCount, 3);
});

test('DiscoverPipeline preserves keywords from duplicate candidates before ranking', async () => {
  const apple = new FakeAppleProvider();
  apple.searchByGenre = async (genre: string) => {
    apple.genreCalls.push(genre);
    return [{
      title: 'Shared Song',
      artist: 'Shared Artist',
      album: 'Album',
      genre: 'ambient',
      durationMs: 210000,
      artwork: '',
      trackId: genre === 'ambient' ? 11 : 12,
      artistId: 21,
    }];
  };

  const pipeline = createPipeline(apple);
  const result = await pipeline.discover({ keywords: ['ambient', 'focus'] });

  assert.deepEqual(result.candidates[0]?.keywords, ['ambient', 'focus']);
});

test('DiscoverPipeline keeps artist keywords non-empty when Apple genre is blank', async () => {
  const apple = new FakeAppleProvider();
  apple.getArtistTracks = async (artist: string) => {
    apple.artistCalls.push(artist);
    return [{
      title: `${artist} Untagged`,
      artist,
      album: 'Album',
      genre: '',
      durationMs: 200000,
      artwork: '',
      trackId: 99,
      artistId: 88,
    }];
  };

  const pipeline = createPipeline(apple);
  const result = await pipeline.discover({ artist: 'Blank Genre Artist' });

  assert.deepEqual(result.candidates[0]?.keywords, ['unknown']);
});

test('DiscoverPipeline shares the six-call budget across artist and keywords', async () => {
  const apple = new FakeAppleProvider();
  const pipeline = createPipeline(apple);

  await pipeline.discover({
    artist: 'Seed Artist',
    keywords: ['ambient', 'piano', 'focus', 'night', 'modern classical', 'drone'],
  });

  assert.deepEqual(apple.artistCalls, ['Seed Artist']);
  assert.deepEqual(apple.genreCalls, ['ambient', 'piano', 'focus', 'night', 'modern classical']);
});

test('DiscoverPaginationCache expires snapshots and evicts least recently used entries', async () => {
  const cache = new DiscoverPaginationCache(5, 2);
  const sample = [{ title: 'Track', artist: 'Artist', tags: ['ambient'], provider: 'apple' as const }];

  cache.setSnapshot({ artist: 'one' }, sample);
  cache.setSnapshot({ artist: 'two' }, sample);
  cache.getPage({ artist: 'one' }, 1, 10);
  cache.setSnapshot({ artist: 'three' }, sample);

  assert.equal(cache.getPage({ artist: 'two' }, 1, 10), null);

  await new Promise((resolve) => setTimeout(resolve, 10));
  assert.equal(cache.getPage({ artist: 'one' }, 1, 10), null);
});

test('DiscoverPaginationCache invalidate clears snapshots and empty results are not cached', () => {
  const cache = new DiscoverPaginationCache();
  const sample = [{ title: 'Track', artist: 'Artist', tags: ['ambient'], provider: 'apple' as const }];

  cache.setSnapshot({ artist: 'one' }, []);
  assert.equal(cache.getPage({ artist: 'one' }, 1, 10), null);

  cache.setSnapshot({ artist: 'two' }, sample);
  cache.invalidate();
  assert.equal(cache.getPage({ artist: 'two' }, 1, 10), null);
});
```

## File: `src/taste/discover-pipeline.ts`
```typescript
import type { HistoryStore } from '../history/history-store.js';
import type { DiscoverRankingConfig } from '../runtime/runtime-config.js';
import type { DiscoverCandidate, DiscoverBatchParams } from './discover-batch-builder.js';
import { DiscoverBatchBuilder } from './discover-batch-builder.js';
import type { DiscoverPaginationCache } from './discover-pagination-cache.js';
import { getDiscoverPaginationCache } from './discover-pagination-cache.js';
import { mergeAndDedup } from './discover-merge-and-dedup.js';
import { rankCandidates } from './discover-soft-ranker.js';

export interface DiscoverRequest extends DiscoverBatchParams {
  page?: number;
  limit?: number;
  mode?: unknown;
  intent?: unknown;
}

export interface PublicDiscoverCandidate {
  title: string;
  artist: string;
  keywords: string[];
  provider: 'apple';
}

export interface DiscoverResponse {
  page: number;
  limit: number;
  hasMore: boolean;
  candidates: PublicDiscoverCandidate[];
  nextGuide: string;
  emptyReason?: 'no_candidates' | 'page_exhausted';
}

export class DiscoverPipeline {
  constructor(
    private readonly batchBuilder: DiscoverBatchBuilder,
    private readonly store: Pick<HistoryStore, 'getTopArtists' | 'getTopTags' | 'getRecentPlaysDetailed' | 'batchGetTrackStats'>,
    private readonly discoverRanking: DiscoverRankingConfig,
    private readonly cache: DiscoverPaginationCache,
  ) {}

  async discover(params: DiscoverRequest): Promise<DiscoverResponse> {
    const page = params.page ?? 1;
    const limit = params.limit ?? 10;
    const cacheParams = { artist: params.artist, keywords: params.keywords };

    const cachedPage = this.cache.getPage(cacheParams, page, limit);
    if (cachedPage) {
      return buildDiscoverResponse(
        cachedPage.candidates,
        page,
        limit,
        cachedPage.hasMore,
        cachedPage.candidates.length === 0 ? 'page_exhausted' : undefined,
      );
    }

    const rawCandidates = await this.batchBuilder.buildBatches(cacheParams);
    if (rawCandidates.length === 0) {
      return buildDiscoverResponse([], page, limit, false, 'no_candidates');
    }

    const dedupedCandidates = mergeAndDedup(rawCandidates);
    const rankedCandidates = rankCandidates(dedupedCandidates, this.discoverRanking, this.store);
    this.cache.setSnapshot(cacheParams, rankedCandidates);

    const pagedCandidates = this.cache.getPage(cacheParams, page, limit);
    if (pagedCandidates) {
      return buildDiscoverResponse(
        pagedCandidates.candidates,
        page,
        limit,
        pagedCandidates.hasMore,
        pagedCandidates.candidates.length === 0 ? 'page_exhausted' : undefined,
      );
    }

    const candidates = rankedCandidates.slice((page - 1) * limit, page * limit);
    return buildDiscoverResponse(
      candidates,
      page,
      limit,
      page * limit < rankedCandidates.length,
      candidates.length === 0 ? 'page_exhausted' : undefined,
    );
  }
}

function buildDiscoverResponse(
  candidates: DiscoverCandidate[],
  page: number,
  limit: number,
  hasMore: boolean,
  emptyReason?: 'no_candidates' | 'page_exhausted',
): DiscoverResponse {
  return {
    page,
    limit,
    hasMore,
    candidates: candidates.map((candidate) => toPublicCandidate(candidate)),
    nextGuide: getNextGuide(candidates.length, hasMore, emptyReason),
    emptyReason,
  };
}

function toPublicCandidate(candidate: DiscoverCandidate): PublicDiscoverCandidate {
  return {
    title: candidate.title,
    artist: candidate.artist,
    keywords: candidate.tags,
    provider: candidate.provider,
  };
}

function getNextGuide(
  candidateCount: number,
  hasMore: boolean,
  emptyReason?: 'no_candidates' | 'page_exhausted',
): string {
  if (candidateCount === 0) {
    return emptyReason === 'page_exhausted'
      ? 'No more results on this page. Go back to an earlier page or improve artist/keywords input.'
      : 'No candidates found. Improve artist/keywords input or build more listening history first.';
  }

  return hasMore
    ? 'Pick from these candidates or call discover with the next page.'
    : 'Pick from these candidates or improve artist/keywords input for a fresh search.';
}

let discoverPipeline: DiscoverPipeline | null = null;

export function createDiscoverPipeline(
  batchBuilder: DiscoverBatchBuilder,
  store: Pick<HistoryStore, 'getTopArtists' | 'getTopTags' | 'getRecentPlaysDetailed' | 'batchGetTrackStats'>,
  discoverRanking: DiscoverRankingConfig,
  cache = getDiscoverPaginationCache(),
): DiscoverPipeline {
  if (!discoverPipeline) {
    discoverPipeline = new DiscoverPipeline(batchBuilder, store, discoverRanking, cache);
  }
  return discoverPipeline;
}

export function getDiscoverPipeline(): DiscoverPipeline | null {
  return discoverPipeline;
}
```

## File: `src/taste/discover-soft-ranker.test.ts`
```typescript
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import test from 'node:test';
import { HistoryStore } from '../history/history-store.js';
import type { DiscoverCandidate } from './discover-batch-builder.js';
import { rankCandidates } from './discover-soft-ranker.js';

function getTempDbPath(): string {
  const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), 'agentune-discover-ranker-'));
  return path.join(tempDir, 'history.db');
}

function cleanupDb(dbPath: string): void {
  try {
    fs.rmSync(path.dirname(dbPath), { recursive: true, force: true });
  } catch {
    // ignore cleanup failures on Windows if a handle lingers after an assertion
  }
}

function seedPlay(
  store: HistoryStore,
  track: { title: string; artist: string; tags: string[]; playedSec?: number; skipped?: boolean },
): void {
  const playId = store.recordPlay({
    title: track.title,
    artist: track.artist,
    duration: 200,
    thumbnail: 'thumb',
    ytVideoId: `${track.artist}-${track.title}`.replace(/\s+/g, '-').toLowerCase(),
  });
  store.updateTrackTags(`${track.artist.toLowerCase()}::${track.title.toLowerCase()}`, track.tags);
  store.updatePlay(playId, { played_sec: track.playedSec ?? 190, skipped: track.skipped ?? false });
}

function candidate(title: string, artist: string, tags: string[]): DiscoverCandidate {
  return { title, artist, tags, provider: 'apple' };
}

test('rankCandidates favors familiar artists when loyalty is high', () => {
  const dbPath = getTempDbPath();
  let store: HistoryStore | null = null;
  try {
    store = new HistoryStore(dbPath);
    for (let index = 0; index < 10; index += 1) {
      seedPlay(store, { title: `Known ${index}`, artist: 'Familiar Artist', tags: ['ambient'] });
    }

    const ranked = rankCandidates(
      [
        candidate('Known New Single', 'Familiar Artist', ['ambient']),
        candidate('Fresh Arrival', 'Novel Artist', ['ambient']),
      ],
      { loyalty: 1, exploration: 0, variety: 0.5 },
      store,
    );

    assert.equal(ranked[0]?.artist, 'Familiar Artist');
  } finally {
    store?.close();
    cleanupDb(dbPath);
  }
});

test('rankCandidates favors novel artists when exploration is high', () => {
  const dbPath = getTempDbPath();
  let store: HistoryStore | null = null;
  try {
    store = new HistoryStore(dbPath);
    for (let index = 0; index < 10; index += 1) {
      seedPlay(store, { title: `Known ${index}`, artist: 'Familiar Artist', tags: ['ambient'] });
    }

    const ranked = rankCandidates(
      [
        candidate('Known New Single', 'Familiar Artist', ['ambient']),
        candidate('Fresh Arrival', 'Novel Artist', ['ambient']),
      ],
      { loyalty: 0, exploration: 1, variety: 0.5 },
      store,
    );

    assert.equal(ranked[0]?.artist, 'Novel Artist');
  } finally {
    store?.close();
    cleanupDb(dbPath);
  }
});

test('rankCandidates penalizes recent repeats and skipped tracks', () => {
  const dbPath = getTempDbPath();
  let store: HistoryStore | null = null;
  try {
    store = new HistoryStore(dbPath);
    seedPlay(store, { title: 'Repeat Me', artist: 'Artist A', tags: ['ambient'], playedSec: 30, skipped: true });
    seedPlay(store, { title: 'Reliable Pick', artist: 'Artist B', tags: ['ambient'], playedSec: 195 });

    const ranked = rankCandidates(
      [
        candidate('Repeat Me', 'Artist A', ['ambient']),
        candidate('Reliable Pick', 'Artist B', ['ambient']),
      ],
      { loyalty: 0.5, exploration: 0.5, variety: 0.5 },
      store,
    );

    assert.equal(ranked[0]?.title, 'Reliable Pick');
  } finally {
    store?.close();
    cleanupDb(dbPath);
  }
});

test('rankCandidates treats empty tags as neutral instead of worst-case', () => {
  const dbPath = getTempDbPath();
  let store: HistoryStore | null = null;
  try {
    store = new HistoryStore(dbPath);
    for (let index = 0; index < 3; index += 1) {
      seedPlay(store, { title: `Ambient ${index}`, artist: 'Anchor Artist', tags: ['ambient'] });
    }

    const ranked = rankCandidates(
      [
        candidate('No Tags Candidate', 'Anchor Artist', []),
        candidate('Mismatched Tags Candidate', 'Anchor Artist', ['metal']),
      ],
      { loyalty: 0.5, exploration: 0.5, variety: 0.5 },
      store,
    );

    assert.equal(ranked[0]?.title, 'No Tags Candidate');
  } finally {
    store?.close();
    cleanupDb(dbPath);
  }
});

test('rankCandidates breaks same-artist clusters after sorting', () => {
  const dbPath = getTempDbPath();
  let store: HistoryStore | null = null;
  try {
    store = new HistoryStore(dbPath);
    for (let index = 0; index < 6; index += 1) {
      seedPlay(store, { title: `Artist A ${index}`, artist: 'Artist A', tags: ['ambient'] });
    }
    seedPlay(store, { title: 'Artist B Seed', artist: 'Artist B', tags: ['ambient'] });

    const ranked = rankCandidates(
      [
        candidate('Artist A One', 'Artist A', ['ambient']),
        candidate('Artist A Two', 'Artist A', ['ambient']),
        candidate('Artist A Three', 'Artist A', ['ambient']),
        candidate('Artist B One', 'Artist B', ['ambient']),
      ],
      { loyalty: 1, exploration: 0, variety: 0.5 },
      store,
    );

    assert.notEqual(ranked[0]?.artist, ranked[1]?.artist);
  } finally {
    store?.close();
    cleanupDb(dbPath);
  }
});

test('rankCandidates uses high variety to avoid repeating nearby tags', () => {
  const dbPath = getTempDbPath();
  let store: HistoryStore | null = null;
  try {
    store = new HistoryStore(dbPath);
    for (let index = 0; index < 8; index += 1) {
      seedPlay(store, { title: `Ambient ${index}`, artist: `Familiar ${index % 2}`, tags: ['ambient'] });
    }
    for (let index = 0; index < 2; index += 1) {
      seedPlay(store, { title: `Focus ${index}`, artist: `Focus Seed ${index}`, tags: ['focus'] });
    }

    const candidates = [
      candidate('Ambient Return One', 'Familiar 0', ['ambient']),
      candidate('Ambient Return Two', 'Familiar 1', ['ambient']),
      candidate('Focus Detour', 'Focus Explorer', ['focus']),
    ];

    const lowVariety = rankCandidates(
      candidates,
      { loyalty: 1, exploration: 0, variety: 0 },
      store,
    );
    const highVariety = rankCandidates(
      candidates,
      { loyalty: 1, exploration: 0, variety: 1 },
      store,
    );

    assert.deepEqual(lowVariety.slice(0, 2).map((entry) => entry.tags[0]), ['ambient', 'ambient']);
    assert.equal(highVariety[1]?.title, 'Focus Detour');
  } finally {
    store?.close();
    cleanupDb(dbPath);
  }
});
```

## File: `src/taste/discover-soft-ranker.ts`
```typescript
import type { BatchTrackStats, HistoryStore } from '../history/history-store.js';
import { normalizeTrackId } from '../history/history-schema.js';
import type { DiscoverRankingConfig } from '../runtime/runtime-config.js';
import type { DiscoverCandidate } from './discover-batch-builder.js';

export interface RankingContext {
  topArtists: Map<string, number>;
  topTags: Set<string>;
  maxArtistPlays: number;
  hasSparseHistory: boolean;
}

interface ScoredCandidate {
  candidate: DiscoverCandidate;
  index: number;
  score: number;
}

const DEFAULT_COMPLETION_AFFINITY = 0.5;
const MIN_HISTORY_FOR_FULL_SCORING = 10;

export function buildRankingContext(
  store: Pick<HistoryStore, 'getTopArtists' | 'getTopTags' | 'getRecentPlaysDetailed'>,
): RankingContext {
  const topArtists = new Map(store.getTopArtists(200).map((artist) => [normalizeValue(artist.artist), artist.plays]));
  const topTags = new Set(store.getTopTags(20).map((tag) => normalizeValue(tag.tag)));
  const maxArtistPlays = Math.max(1, ...topArtists.values());
  const hasSparseHistory = store.getRecentPlaysDetailed(MIN_HISTORY_FOR_FULL_SCORING).length < MIN_HISTORY_FOR_FULL_SCORING;

  return { topArtists, topTags, maxArtistPlays, hasSparseHistory };
}

export function rankCandidates(
  candidates: DiscoverCandidate[],
  discoverRanking: DiscoverRankingConfig,
  store: Pick<HistoryStore, 'getTopArtists' | 'getTopTags' | 'getRecentPlaysDetailed' | 'batchGetTrackStats'>,
): DiscoverCandidate[] {
  const rankingContext = buildRankingContext(store);
  const trackStats = loadTrackStats(store, candidates);

  const scoredCandidates: ScoredCandidate[] = candidates.map((candidate, index) => ({
    candidate,
    index,
    score: scoreCandidate(candidate, discoverRanking, rankingContext, trackStats),
  }));

  scoredCandidates.sort((left, right) => right.score - left.score || left.index - right.index);
  const varietyAdjustedCandidates = applyVarietyDiversityPass(scoredCandidates, discoverRanking.variety);
  return breakArtistClusters(varietyAdjustedCandidates.map((entry) => entry.candidate));
}

function loadTrackStats(
  store: Pick<HistoryStore, 'batchGetTrackStats'>,
  candidates: DiscoverCandidate[],
): Map<string, BatchTrackStats> {
  const trackIds = candidates.map((candidate) => normalizeTrackId(candidate.artist, candidate.title));
  return store.batchGetTrackStats(trackIds);
}

function scoreCandidate(
  candidate: DiscoverCandidate,
  discoverRanking: DiscoverRankingConfig,
  rankingContext: RankingContext,
  trackStats: Map<string, BatchTrackStats>,
): number {
  const artistFamiliarity = computeArtistFamiliarity(candidate.artist, rankingContext);
  const stats = getTrackStats(candidate, trackStats);
  const tagAffinity = computeTagAffinity(candidate.tags, rankingContext.topTags);
  const novelty = 1 - artistFamiliarity;
  const recentRepeatPenalty = computeRecentRepeatPenalty(stats.hoursSinceLastPlay);
  const loyaltyMod = 0.5 + 0.5 * discoverRanking.loyalty;
  const explorationMod = 0.5 + 0.5 * discoverRanking.exploration;

  if (rankingContext.hasSparseHistory) {
    return clamp(
      0.8 * tagAffinity +
      0.1 * stats.avgCompletion -
      0.1 * recentRepeatPenalty -
      0.1 * stats.skipRate,
    );
  }

  const raw =
    0.45 * tagAffinity +
    0.20 * (loyaltyMod * artistFamiliarity) +
    0.15 * (loyaltyMod * stats.avgCompletion) +
    0.20 * (explorationMod * novelty) -
    0.15 * recentRepeatPenalty -
    0.15 * stats.skipRate;

  return clamp(raw);
}

function computeTagAffinity(candidateTags: string[], topTags: Set<string>): number {
  if (candidateTags.length === 0) return DEFAULT_COMPLETION_AFFINITY;
  const normalizedTags = [...new Set(candidateTags.map((tag) => normalizeValue(tag)).filter(Boolean))];
  if (normalizedTags.length === 0) return DEFAULT_COMPLETION_AFFINITY;

  const matches = normalizedTags.filter((tag) => topTags.has(tag)).length;
  return clamp(matches / normalizedTags.length);
}

function computeArtistFamiliarity(artist: string, rankingContext: RankingContext): number {
  const plays = rankingContext.topArtists.get(normalizeValue(artist)) ?? 0;
  return clamp(plays / rankingContext.maxArtistPlays);
}

function computeRecentRepeatPenalty(hoursSinceLastPlay: number): number {
  if (!Number.isFinite(hoursSinceLastPlay)) return 0;
  if (hoursSinceLastPlay < 1) return 1;
  if (hoursSinceLastPlay < 24) return clamp(1 - (hoursSinceLastPlay / 24));
  return 0;
}

function getTrackStats(
  candidate: DiscoverCandidate,
  trackStats: Map<string, BatchTrackStats>,
): BatchTrackStats {
  const trackId = normalizeTrackId(candidate.artist, candidate.title);
  const stats = trackStats.get(trackId);
  if (!stats || stats.playCount === 0) {
    return {
      trackId,
      playCount: 0,
      avgCompletion: DEFAULT_COMPLETION_AFFINITY,
      skipRate: 0,
      hoursSinceLastPlay: Infinity,
    };
  }

  return {
    ...stats,
    avgCompletion: clamp(stats.avgCompletion),
    skipRate: clamp(stats.skipRate),
  };
}

function applyVarietyDiversityPass(
  scoredCandidates: ScoredCandidate[],
  variety: number,
): ScoredCandidate[] {
  const lookahead = getVarietyLookahead(variety);
  if (lookahead <= 1 || scoredCandidates.length <= 2) {
    return [...scoredCandidates];
  }

  const ordered: ScoredCandidate[] = [];
  const remaining = [...scoredCandidates];

  while (remaining.length > 0) {
    const recentCandidates = ordered.slice(-2).map((entry) => entry.candidate);
    const scanLimit = Math.min(remaining.length, lookahead);
    let bestIndex = 0;
    let bestAdjustedScore = getVarietyAdjustedScore(remaining[0], recentCandidates, variety);

    for (let index = 1; index < scanLimit; index += 1) {
      const adjustedScore = getVarietyAdjustedScore(remaining[index], recentCandidates, variety);
      if (adjustedScore > bestAdjustedScore) {
        bestIndex = index;
        bestAdjustedScore = adjustedScore;
      }
    }

    ordered.push(remaining.splice(bestIndex, 1)[0]);
  }

  return ordered;
}

function getVarietyLookahead(variety: number): number {
  if (variety < 0.34) return 1;
  if (variety < 0.67) return 3;
  return 5;
}

function getVarietyAdjustedScore(
  entry: ScoredCandidate,
  recentCandidates: DiscoverCandidate[],
  variety: number,
): number {
  return entry.score - (computeVarietyPenalty(entry.candidate, recentCandidates) * variety * 0.14);
}

function computeVarietyPenalty(
  candidate: DiscoverCandidate,
  recentCandidates: DiscoverCandidate[],
): number {
  if (recentCandidates.length === 0) return 0;

  let penalty = 0;
  const normalizedArtist = normalizeValue(candidate.artist);
  const recentArtists = new Set(recentCandidates.map((recentCandidate) => normalizeValue(recentCandidate.artist)));
  if (recentArtists.has(normalizedArtist)) {
    penalty += 1;
  }

  const normalizedTags = [...new Set(candidate.tags.map((tag) => normalizeValue(tag)).filter(Boolean))];
  if (normalizedTags.length === 0) {
    return penalty;
  }

  const recentTags = new Set(
    recentCandidates.flatMap((recentCandidate) => recentCandidate.tags.map((tag) => normalizeValue(tag)).filter(Boolean)),
  );
  const overlappingTags = normalizedTags.filter((tag) => recentTags.has(tag)).length;
  return penalty + (overlappingTags / normalizedTags.length);
}

function breakArtistClusters(candidates: DiscoverCandidate[]): DiscoverCandidate[] {
  const ranked = [...candidates];

  for (let index = 1; index < ranked.length; index += 1) {
    if (normalizeValue(ranked[index - 1].artist) !== normalizeValue(ranked[index].artist)) continue;

    const swapIndex = findNextDifferentArtist(ranked, index);
    if (swapIndex === -1) continue;
    [ranked[index], ranked[swapIndex]] = [ranked[swapIndex], ranked[index]];
  }

  return ranked;
}

function findNextDifferentArtist(candidates: DiscoverCandidate[], fromIndex: number): number {
  const artist = normalizeValue(candidates[fromIndex].artist);
  for (let index = fromIndex + 1; index < candidates.length; index += 1) {
    if (normalizeValue(candidates[index].artist) !== artist) {
      return index;
    }
  }
  return -1;
}

function normalizeValue(value: string): string {
  return value.toLowerCase().trim().replace(/\s+/g, ' ');
}

function clamp(value: number, min = 0, max = 1): number {
  return Math.max(min, Math.min(max, value));
}
```

## File: `src/taste/taste-engine.test.ts`
```typescript
import assert from 'node:assert/strict';
import fs from 'fs';
import os from 'os';
import path from 'path';
import test from 'node:test';
import { HistoryStore } from '../history/history-store.js';
import { TasteEngine, createTasteEngine } from './taste-engine.js';

function getTempDbPath(): string {
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'agentune-taste-'));
  return path.join(tmpDir, 'taste.db');
}

function cleanupDb(dbPath: string): void {
  const dir = path.dirname(dbPath);
  try {
    if (fs.existsSync(dbPath)) fs.unlinkSync(dbPath);
    if (fs.existsSync(dbPath + '-wal')) fs.unlinkSync(dbPath + '-wal');
    if (fs.existsSync(dbPath + '-shm')) fs.unlinkSync(dbPath + '-shm');
    if (fs.existsSync(dir)) fs.rmdirSync(dir);
  } catch {
    // ignore cleanup errors in tests
  }
}

function seedPlay(
  store: HistoryStore,
  track: { title: string; artist: string; duration: number; tags: string[]; playedSec: number; skipped?: boolean },
): void {
  const playId = store.recordPlay({
    title: track.title,
    artist: track.artist,
    duration: track.duration,
    thumbnail: 'thumb',
    ytVideoId: `${track.artist}-${track.title}`.replace(/\s+/g, '-').toLowerCase(),
  });
  store.updateTrackTags(`${track.artist.toLowerCase()}::${track.title.toLowerCase()}`, track.tags);
  store.updatePlay(playId, { played_sec: track.playedSec, skipped: track.skipped ?? false });
}

test('TasteEngine defaults persona taste to an empty string', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    const engine = new TasteEngine(store);

    assert.deepEqual(engine.getPersona(), { taste: '' });
    assert.equal(engine.getSummary().persona.Preferences, '');
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('TasteEngine taste text round-trips and appears in summary', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    for (let index = 0; index < 10; index += 1) {
      seedPlay(store, {
        title: `Track ${index}`,
        artist: `Artist ${index}`,
        duration: 240,
        tags: ['ambient', index % 2 === 0 ? 'focus' : 'night'],
        playedSec: 200,
      });
    }

    const engine = new TasteEngine(store);
    engine.saveTasteText('Ambient nights, piano, and patient post-rock builds.');

    assert.equal(engine.getTasteText(), 'Ambient nights, piano, and patient post-rock builds.');
    const summary = engine.getSummary();
    assert.equal(summary.persona.Preferences, 'Ambient nights, piano, and patient post-rock builds.');
    assert.equal(summary.history.recent.length, 5);
    assert.ok(summary.history.stats.topArtists.length > 0);
    assert.ok(summary.history.stats.topKeywords.length > 0);
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('TasteEngine truncates saved taste text to 1000 characters', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    const engine = new TasteEngine(store);
    engine.saveTasteText('x'.repeat(1200));

    assert.equal(engine.getTasteText().length, 1000);
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('TasteEngine.getTimeContext returns a valid calendar snapshot', () => {
  const dbPath = getTempDbPath();
  try {
    const store = new HistoryStore(dbPath);
    const engine = new TasteEngine(store);
    const context = engine.getTimeContext();

    assert.ok(context.hour >= 0 && context.hour <= 23);
    assert.ok(['morning', 'afternoon', 'evening', 'night'].includes(context.period));
    assert.ok(context.dayOfWeek.length > 0);
    store.close();
  } finally {
    cleanupDb(dbPath);
  }
});

test('createTasteEngine rebinds to a new store instead of keeping a closed singleton', () => {
  const firstDbPath = getTempDbPath();
  const secondDbPath = getTempDbPath();
  try {
    const firstStore = new HistoryStore(firstDbPath);
    const firstEngine = createTasteEngine(firstStore);
    firstStore.close();

    const secondStore = new HistoryStore(secondDbPath);
    secondStore.savePersonaTasteText('Second store taste');

    const secondEngine = createTasteEngine(secondStore);
    assert.notStrictEqual(firstEngine, secondEngine);
    assert.deepEqual(secondEngine.getPersona(), { taste: 'Second store taste' });
    secondStore.close();
  } finally {
    cleanupDb(firstDbPath);
    cleanupDb(secondDbPath);
  }
});
```

## File: `src/taste/taste-engine.ts`
```typescript
// Taste engine — provides time context and manages free-text persona taste text.
// Listening history stays as context for agents and ranking.

import type { HistoryStore } from '../history/history-store.js';

export interface TimeContext {
  hour: number;
  period: 'morning' | 'afternoon' | 'evening' | 'night';
  dayOfWeek: string;
}

export interface SessionSummary {
  context: TimeContext;
  persona: { Preferences: string };
  history: {
    recent: Array<{ title: string; artist: string; completion: number; skipped: boolean }>;
    stats: { topArtists: Array<{ artist: string; plays: number }>; topKeywords: Array<{ keyword: string; frequency: number }> };
  };
}

// --- Constants ---

const MAX_TASTE_TEXT_LENGTH = 1000;
const DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

// --- TasteEngine ---

export class TasteEngine {
  constructor(private readonly store: HistoryStore) {}

  /** Current time context for agent decision-making. */
  getTimeContext(): TimeContext {
    const now = new Date();
    const hour = now.getHours();
    return {
      hour,
      period: hour < 6 ? 'night' : hour < 12 ? 'morning' : hour < 18 ? 'afternoon' : 'evening',
      dayOfWeek: DAYS[now.getDay()],
    };
  }

  /** Read persisted free-text taste description. */
  getTasteText(): string {
    return this.store.getPersonaTasteText();
  }

  /** Save free-text taste description (max 1000 chars). */
  saveTasteText(text: string): void {
    this.store.savePersonaTasteText(text.slice(0, MAX_TASTE_TEXT_LENGTH));
  }

  /** Read the full persisted persona payload. */
  getPersona(): { taste: string } {
    return {
      taste: this.getTasteText(),
    };
  }

  /** Full session summary for get_session_state MCP tool. */
  getSummary(): SessionSummary {
    const recent = this.store.getRecentPlaysDetailed(5);
    const topArtists = this.store.getTopArtists(5);
    const topKeywords = this.store.getTopTags(5);

    return {
      context: this.getTimeContext(),
      persona: { Preferences: this.getTasteText() },
      history: {
        recent: recent.map(r => ({
          title: r.title,
          artist: r.artist,
          completion: round2(r.completion),
          skipped: r.skipped,
        })),
        stats: {
          topArtists: topArtists.map(a => ({ artist: a.artist, plays: a.plays })),
          topKeywords: topKeywords.map((keyword) => ({
            keyword: keyword.tag,
            frequency: keyword.frequency,
          })),
        },
      },
    };
  }
}

// --- Helpers ---

function round2(n: number): number {
  return Math.round(n * 100) / 100;
}

// --- Singleton ---

let tasteEngine: TasteEngine | null = null;
let tasteEngineStore: HistoryStore | null = null;

export function createTasteEngine(store: HistoryStore): TasteEngine {
  if (!tasteEngine || tasteEngineStore !== store) {
    tasteEngine = new TasteEngine(store);
    tasteEngineStore = store;
  }
  return tasteEngine;
}

export function getTasteEngine(): TasteEngine | null {
  return tasteEngine;
}
```

## File: `src/web/playback-visual-state.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
// @ts-expect-error Browser helper lives in public/ and is loaded directly at runtime.
import { applyPlaybackVisualState, resolvePlaybackVisualState } from '../../public/dashboard/playback-visual-state.js';

test('resolvePlaybackVisualState returns idle when no track exists', () => {
  assert.equal(resolvePlaybackVisualState(false, false), 'idle');
  assert.equal(resolvePlaybackVisualState(false, true), 'idle');
});

test('resolvePlaybackVisualState returns playing when a track is active', () => {
  assert.equal(resolvePlaybackVisualState(true, true), 'playing');
});

test('resolvePlaybackVisualState returns paused when a track exists but playback is stopped', () => {
  assert.equal(resolvePlaybackVisualState(true, false), 'paused');
});

test('applyPlaybackVisualState writes the visual state dataset marker', () => {
  const root = { dataset: {} as Record<string, string> };

  applyPlaybackVisualState(root as never, true, false);
  assert.equal(root.dataset.playbackVisualState, 'paused');
});
```

## File: `src/web/state-broadcaster.test.ts`
```typescript
import assert from 'node:assert/strict';
import { EventEmitter } from 'events';
import test from 'node:test';
import { QueueManager } from '../queue/queue-manager.js';
import { StateBroadcaster } from './state-broadcaster.js';

class StateBroadcasterFakeMpv extends EventEmitter {
  private readonly pendingPositionResolvers: Array<(value: number) => void> = [];
  private readonly state = {
    currentTrack: {
      id: 'current-track',
      title: 'Current Track',
      artist: 'Current Artist',
      duration: 180,
      thumbnail: 'thumb-current',
    },
    isPlaying: true,
    isMuted: false,
    volume: 80,
  };

  getState(): typeof this.state {
    return this.state;
  }

  getVolume(): number {
    return this.state.volume;
  }

  getIsMuted(): boolean {
    return this.state.isMuted;
  }

  isReady(): boolean {
    return true;
  }

  async getPosition(): Promise<number> {
    return await new Promise((resolve) => {
      this.pendingPositionResolvers.push(resolve);
    });
  }

  pause(): void {
    this.state.isPlaying = false;
    this.emit('state-change', this.state);
  }

  releaseNextPosition(position: number): void {
    const resolve = this.pendingPositionResolvers.shift();
    if (!resolve) {
      throw new Error('No pending getPosition call to resolve.');
    }
    resolve(position);
  }

  releaseLatestPosition(position: number): void {
    const resolve = this.pendingPositionResolvers.pop();
    if (!resolve) {
      throw new Error('No pending getPosition call to resolve.');
    }
    resolve(position);
  }

  getPendingPositionCount(): number {
    return this.pendingPositionResolvers.length;
  }
}

async function waitFor(check: () => boolean): Promise<void> {
  const timeoutAt = Date.now() + 5000;

  while (Date.now() < timeoutAt) {
    if (check()) {
      return;
    }
    await new Promise((resolve) => setTimeout(resolve, 25));
  }

  throw new Error('Timed out waiting for broadcaster state.');
}

test('StateBroadcaster keeps the latest playback state when refresh calls overlap', async () => {
  const queueManager = new QueueManager();
  const mpv = new StateBroadcasterFakeMpv();
  const broadcaster = new StateBroadcaster(mpv as never, queueManager);

  try {
    const firstRefresh = broadcaster.refresh();
    await waitFor(() => mpv.getPendingPositionCount() === 1);

    mpv.pause();
    await waitFor(() => mpv.getPendingPositionCount() === 2);

    mpv.releaseLatestPosition(24);
    await waitFor(() => broadcaster.getState().playing === false && broadcaster.getState().position === 24);

    mpv.releaseNextPosition(12);
    await firstRefresh;

    assert.equal(broadcaster.getState().playing, false);
    assert.equal(broadcaster.getState().position, 24);
    assert.equal(broadcaster.getState().title, 'Current Track');
  } finally {
    broadcaster.destroy();
  }
});
```

## File: `src/web/state-broadcaster.ts`
```typescript
import { EventEmitter } from 'events';
import type { TrackMeta, MpvController } from '../audio/mpv-controller.js';
import type { QueueManager } from '../queue/queue-manager.js';


export interface DashboardQueueItem {
  title: string;
  artist: string;
}

export interface DashboardState {
  playing: boolean;
  title: string | null;
  artist: string | null;
  thumbnail: string | null;
  position: number;
  duration: number;
  volume: number;
  muted: boolean;
  queue: DashboardQueueItem[];
}

function mapTrack(track: TrackMeta | null) {
  if (!track) {
    return { title: null, artist: null, thumbnail: null, duration: 0 };
  }

  return {
    title: track.title,
    artist: track.artist ?? 'Unknown',
    thumbnail: track.thumbnail ?? null,
    duration: track.duration ?? 0,
  };
}

export class StateBroadcaster extends EventEmitter {
  private lastSerializedState = '';
  private positionTimer: NodeJS.Timeout;
  private refreshGeneration = 0;
  private state: DashboardState;

  constructor(
    private readonly mpv: MpvController,
    private readonly queueManager: QueueManager,
  ) {
    super();
    this.state = this.createBaseState();
    this.positionTimer = setInterval(() => {
      void this.refresh();
    }, 1000);

    this.mpv.on('state-change', () => {
      void this.refresh();
    });
    this.queueManager.on('state-change', () => {
      void this.refresh();
    });
  }

  getState(): DashboardState {
    return this.state;
  }

  async refresh(): Promise<void> {
    const refreshGeneration = ++this.refreshGeneration;
    const nextState = await this.buildState();
    if (refreshGeneration !== this.refreshGeneration) {
      return;
    }

    const serialized = JSON.stringify(nextState);
    if (serialized === this.lastSerializedState) {
      return;
    }

    this.state = nextState;
    this.lastSerializedState = serialized;
    this.emit('state', this.state);
  }

  destroy(): void {
    clearInterval(this.positionTimer);
  }

  private createBaseState(): DashboardState {
    return {
      playing: false,
      title: null,
      artist: null,
      thumbnail: null,
      position: 0,
      duration: 0,
      volume: this.mpv.getVolume(),
      muted: this.mpv.getIsMuted(),
      queue: this.queueManager.list().map((item) => ({ title: item.title, artist: item.artist })),
    };
  }

  private async buildState(): Promise<DashboardState> {
    const currentState = this.mpv.getState();
    const snapshot = {
      currentTrack: currentState.currentTrack ? { ...currentState.currentTrack } : null,
      isPlaying: currentState.isPlaying,
      isMuted: currentState.isMuted,
      volume: currentState.volume,
    };
    const track = mapTrack(snapshot.currentTrack);
    const position = snapshot.currentTrack && this.mpv.isReady()
      ? Math.max(0, Math.round(await this.mpv.getPosition()))
      : 0;

    return {
      playing: snapshot.isPlaying,
      title: track.title,
      artist: track.artist,
      thumbnail: track.thumbnail,
      position,
      duration: Math.max(position, Math.round(track.duration)),
      volume: snapshot.volume,
      muted: snapshot.isMuted,
      queue: this.queueManager.list().map((item) => ({ title: item.title, artist: item.artist })),
    };
  }
}
```

## File: `src/web/toggle-hidden-attribute.test.ts`
```typescript
import assert from 'node:assert/strict';
import test from 'node:test';
// @ts-expect-error Browser helper lives in public/ and is loaded directly at runtime.
import { toggleHiddenAttribute } from '../../public/dashboard/toggle-hidden-attribute.js';

class FakeElement {
  private readonly attributes = new Set<string>();

  hasAttribute(name: string): boolean {
    return this.attributes.has(name);
  }

  toggleAttribute(name: string, force?: boolean): boolean {
    if (force ?? !this.attributes.has(name)) {
      this.attributes.add(name);
      return true;
    }

    this.attributes.delete(name);
    return false;
  }
}

test('toggleHiddenAttribute writes the real hidden attribute for SVG-like elements', () => {
  const element = new FakeElement();

  toggleHiddenAttribute(element as never, true);
  assert.equal(element.hasAttribute('hidden'), true);

  toggleHiddenAttribute(element as never, false);
  assert.equal(element.hasAttribute('hidden'), false);
});
```

## File: `src/web/web-server-artwork-proxy.test.ts`
```typescript
import assert from 'node:assert/strict';
import { EventEmitter } from 'events';
import { createServer } from 'http';
import test from 'node:test';
import { QueueManager } from '../queue/queue-manager.js';
import { isBlockedArtworkUrl } from './web-server-artwork-proxy.js';
import { getDashboardAuth } from './web-server-test-helpers.js';
import { createWebServer } from './web-server.js';

class ArtworkFakeMpv extends EventEmitter {
  getState(): { currentTrack: null; isPlaying: false; volume: number; isMuted: boolean } {
    return { currentTrack: null, isPlaying: false, volume: 80, isMuted: false };
  }

  isReady(): boolean {
    return false;
  }

  async getPosition(): Promise<number> {
    return 0;
  }

  getVolume(): number {
    return 80;
  }

  getIsMuted(): boolean {
    return false;
  }
}

async function getAvailablePort(): Promise<number> {
  return await new Promise((resolve, reject) => {
    const server = createServer();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      if (!address || typeof address === 'string') {
        server.close(() => reject(new Error('Failed to allocate port.')));
        return;
      }
      const { port } = address;
      server.close((error?: Error | null) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(port);
      });
    });
  });
}

test('WebServer artwork proxy streams remote artwork with safe headers', async () => {
  const webServer = createWebServer(new ArtworkFakeMpv() as never, new QueueManager(), {
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async (input, init) => {
    const target = typeof input === 'string'
      ? input
      : input instanceof URL
        ? input.toString()
        : input.url;

    if (target.startsWith(webServer.getDashboardUrl())) {
      return await originalFetch(input, init);
    }

    return new Response('proxy-image', {
      status: 200,
      headers: { 'Content-Type': 'image/png' },
    });
  };

  try {
    const source = 'https://example.com/art.png';
    const response = await fetch(
      `${webServer.getDashboardUrl()}/api/artwork?src=${encodeURIComponent(source)}&dashboardToken=${encodeURIComponent(auth.token)}`,
    );
    const body = await response.text();

    assert.equal(response.status, 200);
    assert.equal(response.headers.get('content-type'), 'image/png');
    assert.equal(response.headers.get('cache-control'), 'public, max-age=300');
    assert.equal(body, 'proxy-image');
  } finally {
    globalThis.fetch = originalFetch;
    await webServer.destroy();
  }
});

test('WebServer artwork proxy rejects invalid URLs', async () => {
  const webServer = createWebServer(new ArtworkFakeMpv() as never, new QueueManager(), {
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);

  try {
    const response = await fetch(
      `${webServer.getDashboardUrl()}/api/artwork?src=${encodeURIComponent('file:///etc/passwd')}&dashboardToken=${encodeURIComponent(auth.token)}`,
    );
    const payload = await response.json() as { message: string };

    assert.equal(response.status, 400);
    assert.match(payload.message, /http or https/i);
  } finally {
    await webServer.destroy();
  }
});

test('WebServer artwork proxy reports upstream failures safely', async () => {
  const webServer = createWebServer(new ArtworkFakeMpv() as never, new QueueManager(), {
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async (input, init) => {
    const target = typeof input === 'string'
      ? input
      : input instanceof URL
        ? input.toString()
        : input.url;

    if (target.startsWith(webServer.getDashboardUrl())) {
      return await originalFetch(input, init);
    }

    return new Response('missing', {
      status: 404,
      headers: { 'Content-Type': 'image/png' },
    });
  };

  try {
    const source = 'https://example.com/missing.png';
    const response = await fetch(
      `${webServer.getDashboardUrl()}/api/artwork?src=${encodeURIComponent(source)}&dashboardToken=${encodeURIComponent(auth.token)}`,
    );
    const payload = await response.json() as { message: string };

    assert.equal(response.status, 502);
    assert.match(payload.message, /artwork fetch failed/i);
  } finally {
    globalThis.fetch = originalFetch;
    await webServer.destroy();
  }
});

test('WebServer artwork proxy rejects local artwork hosts', async () => {
  const webServer = createWebServer(new ArtworkFakeMpv() as never, new QueueManager(), {
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);

  try {
    const response = await fetch(
      `${webServer.getDashboardUrl()}/api/artwork?src=${encodeURIComponent('http://127.0.0.1:3737/art.png')}&dashboardToken=${encodeURIComponent(auth.token)}`,
    );
    const payload = await response.json() as { message: string };

    assert.equal(response.status, 400);
    assert.match(payload.message, /valid http or https url/i);
  } finally {
    await webServer.destroy();
  }
});

test('WebServer artwork proxy rejects non-image content types and oversized responses', async () => {
  const webServer = createWebServer(new ArtworkFakeMpv() as never, new QueueManager(), {
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);
  const originalFetch = globalThis.fetch;

  try {
    globalThis.fetch = async (input, init) => {
      const target = typeof input === 'string'
        ? input
        : input instanceof URL
          ? input.toString()
          : input.url;

      if (target.startsWith(webServer.getDashboardUrl())) {
        return await originalFetch(input, init);
      }

      return new Response('<html></html>', {
        status: 200,
        headers: { 'Content-Type': 'text/html; charset=utf-8' },
      });
    };

    const nonImageResponse = await fetch(
        `${webServer.getDashboardUrl()}/api/artwork?src=${encodeURIComponent('https://example.com/not-image')}&dashboardToken=${encodeURIComponent(auth.token)}`,
    );
    const nonImagePayload = await nonImageResponse.json() as { message: string };
    assert.equal(nonImageResponse.status, 502);
    assert.match(nonImagePayload.message, /image/i);

    globalThis.fetch = async (input, init) => {
      const target = typeof input === 'string'
        ? input
        : input instanceof URL
          ? input.toString()
          : input.url;

      if (target.startsWith(webServer.getDashboardUrl())) {
        return await originalFetch(input, init);
      }

      return new Response('x'.repeat(5 * 1024 * 1024 + 1), {
        status: 200,
        headers: { 'Content-Type': 'image/png' },
      });
    };

    const oversizedResponse = await fetch(
        `${webServer.getDashboardUrl()}/api/artwork?src=${encodeURIComponent('https://example.com/large.png')}&dashboardToken=${encodeURIComponent(auth.token)}`,
    );
    const oversizedPayload = await oversizedResponse.json() as { message: string };
    assert.equal(oversizedResponse.status, 413);
    assert.match(oversizedPayload.message, /artwork fetch failed/i);
  } finally {
    globalThis.fetch = originalFetch;
    await webServer.destroy();
  }
});

test('WebServer artwork proxy rejects redirects to blocked local targets', async () => {
  const webServer = createWebServer(new ArtworkFakeMpv() as never, new QueueManager(), {
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);
  const originalFetch = globalThis.fetch;

  globalThis.fetch = async (input, init) => {
    const target = typeof input === 'string'
      ? input
      : input instanceof URL
        ? input.toString()
        : input.url;

    if (target.startsWith(webServer.getDashboardUrl())) {
      return await originalFetch(input, init);
    }

    return new Response(null, {
      status: 302,
      headers: { Location: 'http://127.0.0.1:3737/private-art.png' },
    });
  };

  try {
    const response = await fetch(
      `${webServer.getDashboardUrl()}/api/artwork?src=${encodeURIComponent('https://example.com/redirect-art.png')}&dashboardToken=${encodeURIComponent(auth.token)}`,
    );
    const payload = await response.json() as { message: string };

    assert.equal(response.status, 502);
    assert.match(payload.message, /artwork fetch failed/i);
  } finally {
    globalThis.fetch = originalFetch;
    await webServer.destroy();
  }
});

test('WebServer artwork proxy rejects missing dashboard token', async () => {
  const webServer = createWebServer(new ArtworkFakeMpv() as never, new QueueManager(), {
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();

  try {
    const response = await fetch(`${webServer.getDashboardUrl()}/api/artwork?src=${encodeURIComponent('https://images.example.com/art.png')}`);
    assert.equal(response.status, 403);
  } finally {
    await webServer.destroy();
  }
});

test('isBlockedArtworkUrl rejects private DNS resolutions', async () => {
  const lookup = async (hostname: string) => {
    if (hostname === 'safe.example') {
      return [{ address: '203.0.113.10', family: 4 }];
    }
    if (hostname === 'private.example') {
      return [{ address: '127.0.0.1', family: 4 }];
    }
    throw new Error('unexpected lookup');
  };

  assert.equal(await isBlockedArtworkUrl(new URL('https://safe.example/art.png'), { fetch, lookup }), false);
  assert.equal(await isBlockedArtworkUrl(new URL('https://private.example/art.png'), { fetch, lookup }), true);
});
```

## File: `src/web/web-server-artwork-proxy.ts`
```typescript
import { lookup as dnsLookup } from 'dns/promises';
import type { ServerResponse } from 'http';
import { isIP } from 'net';
import { sendJson } from './web-server-helpers.js';

const FETCH_TIMEOUT_MS = 5000;
const MAX_ARTWORK_BYTES = 5 * 1024 * 1024;
const MAX_REDIRECTS = 3;
const PROXY_CACHE_CONTROL = 'public, max-age=300';

type ArtworkLookupResult = Array<{ address: string; family: number }>;

interface ArtworkProxyDependencies {
  fetch: typeof fetch;
  lookup: (hostname: string, options: { all: true; verbatim: boolean }) => Promise<ArtworkLookupResult>;
}

const defaultDependencies: ArtworkProxyDependencies = {
  fetch: async (input, init) => await globalThis.fetch(input, init),
  lookup: async (hostname, options) => await dnsLookup(hostname, options),
};

async function getArtworkSource(
  url: URL,
  dependencies: ArtworkProxyDependencies = defaultDependencies,
): Promise<string | null> {
  const source = url.searchParams.get('src');
  if (!source) {
    return null;
  }

  try {
    const parsed = new URL(source);
    if (parsed.protocol !== 'http:' && parsed.protocol !== 'https:') {
      return null;
    }
    if (await isBlockedArtworkUrl(parsed, dependencies)) {
      return null;
    }
    return parsed.toString();
  } catch {
    return null;
  }
}

export async function handleArtworkProxy(url: URL, response: ServerResponse): Promise<void> {
  const source = await getArtworkSource(url);
  if (!source) {
    sendJson(response, { message: 'src must be a valid http or https URL' }, 400);
    return;
  }

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);

  try {
    const upstream = await fetchArtworkResponse(source, controller, defaultDependencies);
    clearTimeout(timeout);

    if (!upstream.ok) {
      sendJson(response, { message: 'Artwork fetch failed.' }, 502);
      return;
    }

    const contentType = upstream.headers.get('content-type') ?? 'application/octet-stream';
    if (!contentType.toLowerCase().startsWith('image/')) {
      sendJson(response, { message: 'Artwork source must be an image.' }, 502);
      return;
    }

    const contentLength = Number(upstream.headers.get('content-length') ?? 0);
    if (Number.isFinite(contentLength) && contentLength > MAX_ARTWORK_BYTES) {
      sendJson(response, { message: 'Artwork fetch failed.' }, 413);
      return;
    }

    const buffer = await readArtworkBuffer(upstream);
    response.writeHead(200, {
      'Cache-Control': PROXY_CACHE_CONTROL,
      'Content-Length': buffer.byteLength,
      'Content-Type': contentType,
      'Cross-Origin-Resource-Policy': 'same-origin',
    });
    response.end(buffer);
  } catch (error) {
    clearTimeout(timeout);
    console.error('[web-server] Artwork proxy failed', { error: (error as Error).message });
    sendJson(
      response,
      { message: (error as Error).message === 'Artwork too large.' ? 'Artwork fetch failed.' : 'Artwork fetch failed.' },
      (error as Error).message === 'Artwork too large.' ? 413 : 502,
    );
  }
}

async function fetchArtworkResponse(
  source: string,
  controller: AbortController,
  dependencies: ArtworkProxyDependencies,
  redirectCount = 0,
): Promise<Response> {
  if (redirectCount > MAX_REDIRECTS) {
    throw new Error('Too many artwork redirects.');
  }

  const upstream = await dependencies.fetch(source, {
    signal: controller.signal,
    headers: { 'User-Agent': 'agentune-dashboard/0.1' },
    redirect: 'manual',
  });
  if (!isRedirectResponse(upstream.status)) {
    return upstream;
  }

  const location = upstream.headers.get('location');
  if (!location) {
    throw new Error('Artwork redirect missing location.');
  }

  const nextUrl = new URL(location, source);
  if (await isBlockedArtworkUrl(nextUrl, dependencies)) {
    throw new Error('Artwork redirect blocked.');
  }

  return await fetchArtworkResponse(nextUrl.toString(), controller, dependencies, redirectCount + 1);
}

async function readArtworkBuffer(upstream: Response): Promise<Buffer> {
  const reader = upstream.body?.getReader();
  if (!reader) {
    return Buffer.alloc(0);
  }

  const chunks: Buffer[] = [];
  let totalSize = 0;

  while (true) {
    const { done, value } = await reader.read();
    if (done) {
      break;
    }

    const chunk = Buffer.from(value);
    totalSize += chunk.length;
    if (totalSize > MAX_ARTWORK_BYTES) {
      throw new Error('Artwork too large.');
    }
    chunks.push(chunk);
  }

  return Buffer.concat(chunks);
}

export async function isBlockedArtworkUrl(
  url: URL,
  dependencies: ArtworkProxyDependencies = defaultDependencies,
): Promise<boolean> {
  const normalized = url.hostname.toLowerCase();
  if (normalized === 'localhost' || normalized.endsWith('.localhost')) {
    return true;
  }

  const ipVersion = isIP(normalized);
  if (ipVersion === 4) {
    return isBlockedIpv4(normalized);
  }
  if (ipVersion === 6) {
    return isBlockedIpv6(normalized);
  }

  try {
    const records = await dependencies.lookup(normalized, { all: true, verbatim: true });
    if (records.length === 0) {
      return true;
    }

    return records.some((record) => {
      if (record.family === 4) {
        return isBlockedIpv4(record.address);
      }
      if (record.family === 6) {
        return isBlockedIpv6(record.address.toLowerCase());
      }
      return true;
    });
  } catch {
    return true;
  }
}

function isBlockedIpv4(hostname: string): boolean {
  const octets = hostname.split('.').map((segment) => Number(segment));
  if (octets.length !== 4 || octets.some((segment) => !Number.isInteger(segment) || segment < 0 || segment > 255)) {
    return true;
  }

  const [first, second] = octets;
  return first === 0
    || first === 10
    || first === 127
    || first === 169 && second === 254
    || first === 172 && second >= 16 && second <= 31
    || first === 192 && second === 168;
}

function isBlockedIpv6(hostname: string): boolean {
  return hostname === '::1'
    || hostname === '::'
    || hostname.startsWith('fc')
    || hostname.startsWith('fd')
    || hostname.startsWith('fe80:');
}

function isRedirectResponse(status: number): boolean {
  return status === 301
    || status === 302
    || status === 303
    || status === 307
    || status === 308;
}
```

## File: `src/web/web-server-auth.ts`
```typescript
import { randomBytes, timingSafeEqual } from 'crypto';
import type { IncomingHttpHeaders } from 'http';

export const DASHBOARD_TOKEN_HEADER = 'X-Agentune-Dashboard-Token';
export const DASHBOARD_TOKEN_QUERY_PARAM = 'dashboardToken';
export const DASHBOARD_TOKEN_META_NAME = 'agentune-dashboard-token';
export const DASHBOARD_SESSION_EXPIRED_MESSAGE = 'Dashboard session expired. Refresh page.';

export function createDashboardSessionToken(): string {
  return randomBytes(32).toString('base64url');
}

export function hasValidDashboardHeaderToken(headers: IncomingHttpHeaders, expectedToken: string): boolean {
  return hasMatchingToken(headers[DASHBOARD_TOKEN_HEADER.toLowerCase()], expectedToken);
}

export function hasValidDashboardQueryToken(url: URL, expectedToken: string): boolean {
  return hasMatchingToken(url.searchParams.get(DASHBOARD_TOKEN_QUERY_PARAM) ?? undefined, expectedToken);
}

export function isAllowedDashboardMutationRequest(headers: IncomingHttpHeaders): boolean {
  return isSameOriginRequest(headers);
}

export function isAllowedDashboardSocketRequest(url: URL, headers: IncomingHttpHeaders, expectedToken: string): boolean {
  return hasValidDashboardQueryToken(url, expectedToken) && isSameOriginRequest(headers);
}

export function renderDashboardHtml(template: string, token: string): string {
  const tokenMetaTag = `    <meta name="${DASHBOARD_TOKEN_META_NAME}" content="${token}" />`;
  if (template.includes(`name="${DASHBOARD_TOKEN_META_NAME}"`)) {
    return template;
  }

  return template.includes('</head>')
    ? template.replace('</head>', `${tokenMetaTag}\n  </head>`)
    : `${tokenMetaTag}\n${template}`;
}

function hasMatchingToken(rawValue: string | string[] | undefined, expectedToken: string): boolean {
  const candidate = normalizeHeaderValue(rawValue);
  if (!candidate) {
    return false;
  }

  const expectedBuffer = Buffer.from(expectedToken);
  const candidateBuffer = Buffer.from(candidate);
  return expectedBuffer.length === candidateBuffer.length
    && timingSafeEqual(expectedBuffer, candidateBuffer);
}

function isSameOriginRequest(headers: IncomingHttpHeaders): boolean {
  const origin = normalizeHeaderValue(headers.origin);
  const host = normalizeHeaderValue(headers.host);
  if (!origin || !host) {
    return false;
  }

  try {
    const parsedOrigin = new URL(origin);
    return (parsedOrigin.protocol === 'http:' || parsedOrigin.protocol === 'https:')
      && parsedOrigin.host === host;
  } catch {
    return false;
  }
}

function normalizeHeaderValue(value: string | string[] | undefined): string | null {
  if (typeof value === 'string') {
    return value;
  }

  if (Array.isArray(value) && typeof value[0] === 'string') {
    return value[0];
  }

  return null;
}
```

## File: `src/web/web-server-database-cleanup.test.ts`
```typescript
import assert from 'node:assert/strict';
import { EventEmitter } from 'events';
import fs from 'fs';
import { createServer } from 'http';
import os from 'os';
import path from 'path';
import test from 'node:test';
import { HistoryStore } from '../history/history-store.js';
import { createQueuePlaybackController } from '../queue/queue-playback-controller.js';
import { QueueManager } from '../queue/queue-manager.js';
import { createTasteEngine } from '../taste/taste-engine.js';
import { getDashboardAuth } from './web-server-test-helpers.js';
import { createWebServer } from './web-server.js';
import { runDatabaseAction } from './web-server-database-cleanup.js';

class CleanupFakeMpv extends EventEmitter {
  private state = {
    currentTrack: null as { title: string; artist: string; duration: number; thumbnail: string } | null,
    isPlaying: false,
    isMuted: false,
    volume: 80,
  };
  private suppressStoppedCount = 0;
  stopCount = 0;

  setCurrentTrack(track: { title: string; artist: string; duration: number; thumbnail: string } | null): void {
    this.state.currentTrack = track;
    this.state.isPlaying = track !== null;
  }

  getState(): typeof this.state {
    return this.state;
  }

  isReady(): boolean {
    return true;
  }

  getCurrentTrack(): typeof this.state.currentTrack {
    return this.state.currentTrack;
  }

  suppressNextStopped(): void {
    this.suppressStoppedCount++;
  }

  stop(): void {
    this.stopCount += 1;
    this.state.currentTrack = null;
    this.state.isPlaying = false;
    if (this.suppressStoppedCount > 0) {
      this.suppressStoppedCount--;
    } else {
      this.emit('stopped');
    }
    this.emit('state-change', this.state);
  }

  play(): void {}
  pause(): void {}
  resume(): void {}
  setVolume(level: number): number {
    this.state.volume = level;
    this.emit('state-change', this.state);
    return level;
  }
  getVolume(): number {
    return this.state.volume;
  }
  toggleMute(): boolean {
    this.state.isMuted = !this.state.isMuted;
    this.emit('state-change', this.state);
    return this.state.isMuted;
  }
  getIsMuted(): boolean {
    return this.state.isMuted;
  }
  async getPosition(): Promise<number> {
    return 0;
  }
}

function getTempDbPath(): string {
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'agentune-web-cleanup-'));
  return path.join(tmpDir, 'history.db');
}

function cleanupDb(dbPath: string): void {
  const dir = path.dirname(dbPath);
  try {
    if (fs.existsSync(dbPath)) fs.unlinkSync(dbPath);
    if (fs.existsSync(`${dbPath}-wal`)) fs.unlinkSync(`${dbPath}-wal`);
    if (fs.existsSync(`${dbPath}-shm`)) fs.unlinkSync(`${dbPath}-shm`);
    if (fs.existsSync(dir)) fs.rmdirSync(dir);
  } catch {
    // Ignore cleanup errors in tests.
  }
}

async function getAvailablePort(): Promise<number> {
  return await new Promise((resolve, reject) => {
    const server = createServer();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      if (!address || typeof address === 'string') {
        server.close(() => reject(new Error('Failed to allocate port.')));
        return;
      }
      const { port } = address;
      server.close((error) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(port);
      });
    });
  });
}

test('WebServer database cleanup endpoints stop runtime state and clear selected data', async () => {
  const dbPath = getTempDbPath();
  const store = new HistoryStore(dbPath);
  createTasteEngine(store);
  const queueManager = new QueueManager();
  const mpv = new CleanupFakeMpv();
  createQueuePlaybackController(mpv as never, queueManager, {
    search: async () => [],
    getAudioUrl: async () => ({ streamUrl: '', title: '', artist: '', duration: 0, thumbnail: '' }),
  } as never);

  const webServer = createWebServer(mpv as never, queueManager, {
    historyStore: store,
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);

  try {
    const playId = store.recordPlay({ title: 'Track A', artist: 'Artist A', duration: 200, thumbnail: 'thumb', ytVideoId: 'vid-a' });
    store.updatePlay(playId, { played_sec: 140, skipped: false });
    store.getDatabase().prepare(`
      INSERT INTO provider_cache (cache_key, response_json, fetched_at)
      VALUES ('apple:test', '{}', 123)
    `).run();
    store.updateTrackTags('artist a::track a', ['ambient']);
    queueManager.add({ id: 'queued', title: 'Queued', artist: 'Artist Q', duration: 100, thumbnail: 'thumb', url: 'url' });
    queueManager.setNowPlaying({ id: 'current', title: 'Current', artist: 'Artist C', duration: 120, thumbnail: 'thumb', url: 'url' });
    mpv.setCurrentTrack({ title: 'Current', artist: 'Artist C', duration: 120, thumbnail: 'thumb' });

    const statsResponse = await fetch(`${webServer.getDashboardUrl()}/api/database/stats`, {
      headers: auth.headers,
    });
    const statsPayload = await statsResponse.json() as {
      stats: {
        counts: { plays: number; tracks: number; providerCache: number };
        insights: {
          plays7d: number;
          tracks7d: number;
          skipRate: number;
          activity7d: Array<{ dayLabel: string; plays: number }>;
          topArtists: Array<{ artist: string; plays: number }>;
          topKeywords: Array<{ keyword: string; frequency: number }>;
        };
      };
    };
    assert.deepEqual(statsPayload.stats.counts, { plays: 1, tracks: 1, providerCache: 1 });
    assert.equal(statsPayload.stats.insights.plays7d, 1);
    assert.equal(statsPayload.stats.insights.tracks7d, 1);
    assert.equal(statsPayload.stats.insights.topArtists[0]?.artist, 'Artist A');
    assert.equal(statsPayload.stats.insights.topKeywords[0]?.keyword, 'ambient');
    assert.equal(statsPayload.stats.insights.activity7d.reduce((sum, bucket) => sum + bucket.plays, 0), 1);

    const clearHistoryResponse = await fetch(`${webServer.getDashboardUrl()}/api/database/clear-history`, {
      method: 'POST',
      headers: auth.headers,
    });
    const clearHistoryPayload = await clearHistoryResponse.json() as {
      updated: boolean;
      removed: { plays: number; tracks: number; providerCache: number };
      stats: {
        counts: { plays: number; tracks: number; providerCache: number };
        insights: {
          plays7d: number;
          tracks7d: number;
          skipRate: number;
          activity7d: Array<{ dayLabel: string; plays: number }>;
          topArtists: Array<{ artist: string; plays: number }>;
          topKeywords: Array<{ keyword: string; frequency: number }>;
        };
      };
    };
    assert.equal(clearHistoryResponse.status, 200);
    assert.equal(clearHistoryPayload.updated, true);
    assert.deepEqual(clearHistoryPayload.removed, { plays: 1, tracks: 1, providerCache: 0 });
    assert.deepEqual(clearHistoryPayload.stats.counts, { plays: 0, tracks: 0, providerCache: 1 });
    assert.equal(clearHistoryPayload.stats.insights.plays7d, 0);
    assert.equal(clearHistoryPayload.stats.insights.tracks7d, 0);
    assert.equal(clearHistoryPayload.stats.insights.skipRate, 0);
    assert.deepEqual(clearHistoryPayload.stats.insights.topArtists, []);
    assert.deepEqual(clearHistoryPayload.stats.insights.topKeywords, []);
    assert.equal(clearHistoryPayload.stats.insights.activity7d.reduce((sum, bucket) => sum + bucket.plays, 0), 0);
    assert.equal(mpv.stopCount, 1);
    assert.deepEqual(queueManager.getState(), { nowPlaying: null, queue: [], history: [] });

    const clearCacheResponse = await fetch(`${webServer.getDashboardUrl()}/api/database/clear-provider-cache`, {
      method: 'POST',
      headers: auth.headers,
    });
    const clearCachePayload = await clearCacheResponse.json() as {
      removed: { plays: number; tracks: number; providerCache: number };
      stats: {
        counts: { plays: number; tracks: number; providerCache: number };
        insights: {
          skipRate: number;
          topArtists: Array<unknown>;
          topKeywords: Array<unknown>;
        };
      };
    };
    assert.equal(clearCacheResponse.status, 200);
    assert.deepEqual(clearCachePayload.removed, { plays: 0, tracks: 0, providerCache: 1 });
    assert.deepEqual(clearCachePayload.stats.counts, { plays: 0, tracks: 0, providerCache: 0 });
    assert.equal(clearCachePayload.stats.insights.skipRate, 0);
    assert.deepEqual(clearCachePayload.stats.insights.topArtists, []);
    assert.deepEqual(clearCachePayload.stats.insights.topKeywords, []);
  } finally {
    await webServer.destroy();
    store.close();
    cleanupDb(dbPath);
  }
});

test('WebServer fails startup when exact configured port is busy', async () => {
  const blocker = createServer();
  const port = await getAvailablePort();
  await new Promise<void>((resolve, reject) => {
    blocker.once('error', reject);
    blocker.listen(port, '127.0.0.1', () => resolve());
  });

  const webServer = createWebServer(new CleanupFakeMpv() as never, new QueueManager(), { port });
  try {
    await assert.rejects(() => webServer.waitUntilReady(), /EADDRINUSE/i);
  } finally {
    await new Promise<void>((resolve) => blocker.close(() => resolve()));
  }
});

test('WebServer stop endpoint schedules explicit daemon shutdown', async () => {
  const stopReasons: string[] = [];
  const webServer = createWebServer(new CleanupFakeMpv() as never, new QueueManager(), {
    onStopDaemon: (reason) => {
      stopReasons.push(reason);
    },
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);

  try {
    const response = await fetch(`${webServer.getDashboardUrl()}/api/daemon/stop`, {
      method: 'POST',
      headers: auth.headers,
    });
    const payload = await response.json() as { stopped: boolean; message: string };

    assert.equal(response.status, 200);
    assert.equal(payload.stopped, true);
    assert.match(payload.message, /agentune start/i);

    await new Promise((resolve) => setTimeout(resolve, 150));
    assert.deepEqual(stopReasons, ['dashboard stop']);
  } finally {
    await webServer.destroy();
  }
});

test('WebServer cleanup and stop endpoints reject missing dashboard auth token', async () => {
  const webServer = createWebServer(new CleanupFakeMpv() as never, new QueueManager(), {
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();

  try {
    const statsResponse = await fetch(`${webServer.getDashboardUrl()}/api/database/stats`);
    assert.equal(statsResponse.status, 403);

    const stopResponse = await fetch(`${webServer.getDashboardUrl()}/api/daemon/stop`, { method: 'POST' });
    assert.equal(stopResponse.status, 403);
  } finally {
    await webServer.destroy();
  }
});

test('runDatabaseAction serializes concurrent cleanup requests', async () => {
  const dbPath = getTempDbPath();
  const store = new HistoryStore(dbPath);
  let activeCalls = 0;
  let maxConcurrentCalls = 0;

  try {
    const queuePlaybackController = {
      stopAndResetRuntimeState: async () => {
        activeCalls += 1;
        maxConcurrentCalls = Math.max(maxConcurrentCalls, activeCalls);
        await new Promise((resolve) => setTimeout(resolve, 20));
        activeCalls -= 1;
      },
    };

    await Promise.all([
      runDatabaseAction('clear-provider-cache', store, queuePlaybackController as never),
      runDatabaseAction('clear-provider-cache', store, queuePlaybackController as never),
    ]);

    assert.equal(maxConcurrentCalls, 1);
  } finally {
    store.close();
    cleanupDb(dbPath);
  }
});
```

## File: `src/web/web-server-database-cleanup.ts`
```typescript
import type { HistoryCleanupResult, HistoryStore } from '../history/history-store.js';
import type { QueuePlaybackController } from '../queue/queue-playback-controller.js';
import { invalidateDiscoverCache } from '../taste/discover-pagination-cache.js';

export interface DatabaseActionResponse {
  updated: true;
  action: 'clear-history' | 'clear-provider-cache' | 'full-reset';
  removed: HistoryCleanupResult['removed'];
  stats: HistoryCleanupResult['stats'];
  message: string;
}

let databaseActionLock = Promise.resolve();

export function getDatabaseStatsPayload(store: HistoryStore): { stats: ReturnType<HistoryStore['getDatabaseStats']> } {
  return { stats: store.getDatabaseStats() };
}

export async function runDatabaseAction(
  action: 'clear-history' | 'clear-provider-cache' | 'full-reset',
  store: HistoryStore,
  queuePlaybackController: QueuePlaybackController | null,
): Promise<DatabaseActionResponse> {
  return await withDatabaseActionLock(async () => {
    if (queuePlaybackController) {
      await queuePlaybackController.stopAndResetRuntimeState();
    }

    let result: HistoryCleanupResult;
    let message: string;

    if (action === 'clear-history') {
      result = store.clearHistory();
      message = 'Listening history cleared.';
    } else if (action === 'clear-provider-cache') {
      result = store.clearProviderCache();
      message = 'Provider cache cleared.';
    } else {
      result = store.fullReset();
      message = 'History and provider cache cleared.';
    }

    invalidateDiscoverCache();

    return {
      updated: true,
      action,
      removed: result.removed,
      stats: result.stats,
      message,
    };
  });
}

async function withDatabaseActionLock<T>(operation: () => Promise<T>): Promise<T> {
  const previous = databaseActionLock;
  let release!: () => void;
  databaseActionLock = new Promise<void>((resolve) => {
    release = resolve;
  });

  await previous;

  try {
    return await operation();
  } finally {
    release();
  }
}
```

## File: `src/web/web-server-helpers.ts`
```typescript
import { spawn } from 'child_process';
import type { IncomingMessage, ServerResponse } from 'http';
import { extname } from 'path';

const MAX_JSON_BODY_SIZE = 1024 * 1024;

const MIME_TYPES: Record<string, string> = {
  '.css': 'text/css; charset=utf-8',
  '.html': 'text/html; charset=utf-8',
  '.ico': 'image/x-icon',
  '.js': 'application/javascript; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml; charset=utf-8',
};

export function getMimeType(filePath: string): string {
  return MIME_TYPES[extname(filePath)] ?? 'application/octet-stream';
}

export function sendJson(response: ServerResponse, payload: unknown, statusCode = 200): void {
  response.writeHead(statusCode, { 'Content-Type': 'application/json; charset=utf-8' });
  response.end(JSON.stringify(payload));
}

export function openUrl(url: string): void {
  if (process.platform === 'win32') {
    spawn('cmd', ['/c', 'start', '', url], { stdio: 'ignore', detached: true }).unref();
    return;
  }
  const command = process.platform === 'darwin' ? 'open' : 'xdg-open';
  spawn(command, [url], { stdio: 'ignore', detached: true }).unref();
}

export async function readJsonBody(request: IncomingMessage): Promise<Record<string, unknown> | null> {
  try {
    const parsed = JSON.parse((await readRequestBody(request)).toString('utf8'));
    if (typeof parsed !== 'object' || parsed === null) return null;
    return parsed as Record<string, unknown>;
  } catch {
    return null;
  }
}

export async function readVolumeRequest(request: IncomingMessage): Promise<{ volume: number } | null> {
  try {
    const parsed = JSON.parse((await readRequestBody(request)).toString('utf8')) as { volume?: number };
    if (typeof parsed.volume !== 'number' || !Number.isFinite(parsed.volume)) {
      return null;
    }

    return { volume: clampVolume(parsed.volume) };
  } catch {
    return null;
  }
}

async function readRequestBody(request: IncomingMessage): Promise<Buffer> {
  const chunks: Buffer[] = [];
  let totalSize = 0;

  for await (const chunk of request) {
    const nextChunk = Buffer.isBuffer(chunk) ? chunk : Buffer.from(chunk);
    totalSize += nextChunk.length;
    if (totalSize > MAX_JSON_BODY_SIZE) {
      throw new Error('Request body too large.');
    }
    chunks.push(nextChunk);
  }

  return Buffer.concat(chunks);
}

function clampVolume(level: number): number {
  return Math.max(0, Math.min(100, Math.round(level)));
}
```

## File: `src/web/web-server-persona-sync.test.ts`
```typescript
import assert from 'node:assert/strict';
import { EventEmitter } from 'events';
import fs from 'fs';
import { createServer } from 'http';
import os from 'os';
import path from 'path';
import test from 'node:test';
import WebSocket from 'ws';
import { HistoryStore } from '../history/history-store.js';
import { getDiscoverPaginationCache, invalidateDiscoverCache } from '../taste/discover-pagination-cache.js';
import { handleUpdatePersona } from '../mcp/tool-handlers.js';
import { QueueManager } from '../queue/queue-manager.js';
import { createTasteEngine } from '../taste/taste-engine.js';
import { getDashboardAuth } from './web-server-test-helpers.js';
import { createWebServer } from './web-server.js';

class FakeMpv extends EventEmitter {
  getState(): { currentTrack: null; isPlaying: false; volume: number; isMuted: boolean } {
    return { currentTrack: null, isPlaying: false, volume: 80, isMuted: false };
  }

  isReady(): boolean {
    return false;
  }

  async getPosition(): Promise<number> {
    return 0;
  }

  getVolume(): number {
    return 80;
  }

  getIsMuted(): boolean {
    return false;
  }
}

function getTempDbPath(): string {
  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'agentune-web-sync-'));
  return path.join(tmpDir, 'history.db');
}

function cleanupDb(dbPath: string): void {
  const dir = path.dirname(dbPath);
  try {
    if (fs.existsSync(dbPath)) fs.unlinkSync(dbPath);
    if (fs.existsSync(dbPath + '-wal')) fs.unlinkSync(dbPath + '-wal');
    if (fs.existsSync(dbPath + '-shm')) fs.unlinkSync(dbPath + '-shm');
    if (fs.existsSync(dir)) fs.rmdirSync(dir);
  } catch {
    // ignore cleanup errors in tests
  }
}

async function getAvailablePort(): Promise<number> {
  return await new Promise((resolve, reject) => {
    const server = createServer();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      if (!address || typeof address === 'string') {
        server.close(() => reject(new Error('Failed to allocate port.')));
        return;
      }
      const { port } = address;
      server.close((error) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(port);
      });
    });
  });
}

async function waitForBufferedMessage(
  messages: Array<{ type?: string; data?: { taste?: string } }>,
  predicate: (payload: { type?: string; data?: { taste?: string } }) => boolean,
): Promise<{ type?: string; data?: { taste?: string } }> {
  return await new Promise((resolve, reject) => {
    const deadline = Date.now() + 5000;
    const check = () => {
      const match = messages.find((payload) => predicate(payload));
      if (match) {
        resolve(match);
        return;
      }

      if (Date.now() >= deadline) {
        reject(new Error('Timed out waiting for websocket message.'));
        return;
      }

      setTimeout(check, 25);
    };

    check();
  });
}

test('WebServer syncs dashboard persona API and MCP taste updates without touching discover cache', async () => {
  const dbPath = getTempDbPath();
  const store = new HistoryStore(dbPath);
  const tasteEngine = createTasteEngine(store);
  tasteEngine.saveTasteText('Initial taste');

  const webServer = createWebServer(new FakeMpv() as never, new QueueManager(), {
    historyStore: store,
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);

  const socket = new WebSocket(
    `${webServer.getDashboardUrl().replace('http', 'ws')}/ws?dashboardToken=${encodeURIComponent(auth.token)}`,
    { headers: { Origin: auth.origin } },
  );
  const messages: Array<{ type?: string; data?: { taste?: string } }> = [];
  socket.on('message', (raw) => {
    messages.push(JSON.parse(raw.toString()) as { type?: string; data?: { taste?: string } });
  });
  await new Promise<void>((resolve) => socket.once('open', () => resolve()));

  try {
    const initialResponse = await fetch(`${webServer.getDashboardUrl()}/api/persona`, {
      headers: auth.headers,
    });
    const initialPayload = await initialResponse.json() as { taste: string };
    assert.equal(initialPayload.taste, 'Initial taste');

    const initialPersona = await waitForBufferedMessage(
      messages,
      (payload) => payload.type === 'persona' && payload.data?.taste === 'Initial taste',
    );
    assert.equal(initialPersona.data?.taste, 'Initial taste');

    const cache = getDiscoverPaginationCache();
    cache.setSnapshot(
      { keywords: ['focus'] },
      [{ title: 'Focus Track', artist: 'Focus Artist', tags: ['focus'], provider: 'apple' }],
    );
    assert.notEqual(cache.getPage({ keywords: ['focus'] }, 1, 10), null);

    const dashboardResponse = await fetch(`${webServer.getDashboardUrl()}/api/persona`, {
      method: 'POST',
      headers: { ...auth.headers, 'Content-Type': 'application/json' },
      body: JSON.stringify({ taste: 'Dashboard taste' }),
    });
    const dashboardPayload = await dashboardResponse.json() as {
      updated: boolean;
      taste: string;
    };
    assert.equal(dashboardPayload.updated, true);
    assert.equal(dashboardPayload.taste, 'Dashboard taste');
    assert.notEqual(cache.getPage({ keywords: ['focus'] }, 1, 10), null);

    const dashboardPersona = await waitForBufferedMessage(
      messages,
      (payload) => payload.type === 'persona' && payload.data?.taste === 'Dashboard taste',
    );
    assert.equal(dashboardPersona.data?.taste, 'Dashboard taste');

    const invalidResponse = await fetch(`${webServer.getDashboardUrl()}/api/persona`, {
      method: 'POST',
      headers: { ...auth.headers, 'Content-Type': 'application/json' },
      body: JSON.stringify({}),
    });
    const invalidPayload = await invalidResponse.json() as { message: string };
    assert.equal(invalidResponse.status, 400);
    assert.match(invalidPayload.message, /taste field required/i);

    const oversizedResponse = await fetch(`${webServer.getDashboardUrl()}/api/persona`, {
      method: 'POST',
      headers: { ...auth.headers, 'Content-Type': 'application/json' },
      body: JSON.stringify({ taste: 'x'.repeat(1024 * 1024) }),
    });
    const oversizedPayload = await oversizedResponse.json() as { message: string };
    assert.equal(oversizedResponse.status, 400);
    assert.match(oversizedPayload.message, /taste field required/i);

    const updateResult = await handleUpdatePersona({ taste: 'Updated taste' });
    assert.equal(updateResult.isError, undefined);
    assert.notEqual(cache.getPage({ keywords: ['focus'] }, 1, 10), null);

    const updatedPersona = await waitForBufferedMessage(
      messages,
      (payload) => payload.type === 'persona' && payload.data?.taste === 'Updated taste',
    );
    assert.equal(updatedPersona.data?.taste, 'Updated taste');
  } finally {
    socket.close();
    await webServer.destroy();
    store.close();
    invalidateDiscoverCache();
    cleanupDb(dbPath);
  }
});

test('WebServer persona API rejects missing dashboard auth token', async () => {
  const dbPath = getTempDbPath();
  const store = new HistoryStore(dbPath);
  createTasteEngine(store);

  const webServer = createWebServer(new FakeMpv() as never, new QueueManager(), {
    historyStore: store,
    port: await getAvailablePort(),
  });
  await webServer.waitUntilReady();

  try {
    const response = await fetch(`${webServer.getDashboardUrl()}/api/persona`);
    assert.equal(response.status, 403);
  } finally {
    await webServer.destroy();
    store.close();
    cleanupDb(dbPath);
  }
});
```

## File: `src/web/web-server-playback-controls.test.ts`
```typescript
import assert from 'node:assert/strict';
import { EventEmitter } from 'events';
import { createServer } from 'http';
import test from 'node:test';
import WebSocket from 'ws';
import { createQueuePlaybackController } from '../queue/queue-playback-controller.js';
import { QueueManager } from '../queue/queue-manager.js';
import { getDashboardAuth } from './web-server-test-helpers.js';
import { createWebServer } from './web-server.js';

class PlaybackControlsFakeMpv extends EventEmitter {
  private state = {
    currentTrack: null as { id: string; title: string; artist: string; duration: number; thumbnail: string } | null,
    isPlaying: false,
    isMuted: false,
    volume: 80,
  };

  pauseCount = 0;
  playCount = 0;
  private pauseProperty = false;
  private suppressStoppedCount = 0;
  resumeCount = 0;
  stopCount = 0;

  seedCurrentTrack(track: { id: string; title: string; artist: string; duration: number; thumbnail: string }): void {
    this.state.currentTrack = track;
    this.state.isPlaying = true;
    this.pauseProperty = false;
  }

  getState(): typeof this.state {
    return this.state;
  }

  getCurrentTrack(): typeof this.state.currentTrack {
    return this.state.currentTrack;
  }

  getIsPlaying(): boolean {
    return this.state.isPlaying;
  }

  isReady(): boolean {
    return true;
  }

  play(_url: string, track: { id: string; title: string; artist: string; duration: number; thumbnail: string }): void {
    this.playCount += 1;
    this.state.currentTrack = track;
    this.state.isPlaying = !this.pauseProperty;
    if (this.state.isPlaying) {
      this.emit('started');
    }
    this.emit('state-change', this.state);
  }

  pause(): void {
    this.pauseCount += 1;
    this.pauseProperty = true;
    this.state.isPlaying = false;
    this.emit('paused');
    this.emit('state-change', this.state);
  }

  resume(): void {
    this.resumeCount += 1;
    this.pauseProperty = false;
    this.state.isPlaying = this.state.currentTrack !== null;
    this.emit('resumed');
    this.emit('state-change', this.state);
  }

  suppressNextStopped(): void {
    this.suppressStoppedCount++;
  }

  stop(): void {
    this.stopCount += 1;
    this.state.currentTrack = null;
    this.state.isPlaying = false;
    if (this.suppressStoppedCount > 0) {
      this.suppressStoppedCount--;
    } else {
      this.emit('stopped');
    }
    this.emit('state-change', this.state);
  }

  setVolume(level: number): number {
    this.state.volume = level;
    this.emit('state-change', this.state);
    return level;
  }

  getVolume(): number {
    return this.state.volume;
  }

  toggleMute(): boolean {
    this.state.isMuted = !this.state.isMuted;
    this.emit('state-change', this.state);
    return this.state.isMuted;
  }

  getIsMuted(): boolean {
    return this.state.isMuted;
  }

  async getPosition(): Promise<number> {
    return 0;
  }
}

async function getAvailablePort(): Promise<number> {
  return await new Promise((resolve, reject) => {
    const server = createServer();
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      if (!address || typeof address === 'string') {
        server.close(() => reject(new Error('Failed to allocate port.')));
        return;
      }
      const { port } = address;
      server.close((error) => {
        if (error) {
          reject(error);
          return;
        }
        resolve(port);
      });
    });
  });
}

async function waitFor(check: () => boolean): Promise<void> {
  const timeoutAt = Date.now() + 5000;

  while (Date.now() < timeoutAt) {
    if (check()) {
      return;
    }
    await new Promise((resolve) => setTimeout(resolve, 25));
  }

  throw new Error('Timed out waiting for playback control update.');
}

test('WebServer websocket playback controls pause, toggle resume, and skip the current track', async () => {
  const queueManager = new QueueManager();
  const mpv = new PlaybackControlsFakeMpv();
  const currentTrack = {
    id: 'current-track',
    title: 'Current Track',
    artist: 'Current Artist',
    duration: 180,
    thumbnail: 'thumb-current',
    url: 'https://youtube.test/current',
  };
  const nextTrack = {
    id: 'next-track',
    title: 'Next Track',
    artist: 'Queued Artist',
    duration: 200,
    thumbnail: 'thumb-next',
    url: 'https://youtube.test/next',
  };

  queueManager.setNowPlaying(currentTrack);
  queueManager.add(nextTrack);
  mpv.seedCurrentTrack(currentTrack);

  createQueuePlaybackController(mpv as never, queueManager, {
    search: async () => [],
    getAudioUrl: async (id: string) => ({
      streamUrl: `https://stream.test/${id}`,
      title: id === nextTrack.id ? nextTrack.title : currentTrack.title,
      artist: id === nextTrack.id ? nextTrack.artist : currentTrack.artist,
      duration: id === nextTrack.id ? nextTrack.duration : currentTrack.duration,
      thumbnail: id === nextTrack.id ? nextTrack.thumbnail : currentTrack.thumbnail,
    }),
  } as never);

  const webServer = createWebServer(mpv as never, queueManager, { port: await getAvailablePort() });
  webServer.openDashboardOnce = () => {};
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);

  const socket = new WebSocket(
    `${webServer.getDashboardUrl().replace('http', 'ws')}/ws?dashboardToken=${encodeURIComponent(auth.token)}`,
    { headers: { Origin: auth.origin } },
  );
  await new Promise<void>((resolve) => socket.once('open', () => resolve()));

  try {
    socket.send(JSON.stringify({ type: 'pause' }));
    await waitFor(() => mpv.pauseCount === 1 && mpv.getState().isPlaying === false);

    socket.send(JSON.stringify({ type: 'pause' }));
    await new Promise((resolve) => setTimeout(resolve, 50));
    assert.equal(mpv.pauseCount, 1);
    assert.equal(mpv.resumeCount, 0);
    assert.equal(mpv.getState().isPlaying, false);

    socket.send(JSON.stringify({ type: 'playback-toggle' }));
    await waitFor(() => mpv.resumeCount === 1 && mpv.getState().isPlaying === true);

    socket.send(JSON.stringify({ type: 'playback-toggle' }));
    await waitFor(() => mpv.pauseCount === 2 && mpv.getState().isPlaying === false);

    socket.send(JSON.stringify({ type: 'playback-toggle' }));
    await waitFor(() => mpv.resumeCount === 2 && mpv.getState().isPlaying === true);

    socket.send(JSON.stringify({ type: 'playback-toggle' }));
    await waitFor(() => mpv.pauseCount === 3 && mpv.getState().isPlaying === false);

    socket.send(JSON.stringify({ type: 'next' }));
    await waitFor(() => mpv.playCount === 1 && queueManager.getNowPlaying()?.id === nextTrack.id && mpv.getState().isPlaying === true);

    assert.equal(mpv.stopCount, 1);
    assert.equal(queueManager.list().length, 0);
    assert.equal(queueManager.getNowPlaying()?.title, nextTrack.title);
  } finally {
    socket.close();
    await webServer.destroy();
  }
});

test('WebServer volume endpoint clamps out-of-range values and rejects malformed payloads', async () => {
  const queueManager = new QueueManager();
  const mpv = new PlaybackControlsFakeMpv();
  const webServer = createWebServer(mpv as never, queueManager, { port: await getAvailablePort() });
  await webServer.waitUntilReady();
  const auth = await getDashboardAuth(webServer);

  try {
    const lowResponse = await fetch(`${webServer.getDashboardUrl()}/api/volume`, {
      method: 'POST',
      headers: { ...auth.headers, 'Content-Type': 'application/json' },
      body: JSON.stringify({ volume: -15 }),
    });
    const lowPayload = await lowResponse.json() as { volume: number };
    assert.equal(lowResponse.status, 200);
    assert.equal(lowPayload.volume, 0);
    assert.equal(mpv.getVolume(), 0);

    const highResponse = await fetch(`${webServer.getDashboardUrl()}/api/volume`, {
      method: 'POST',
      headers: { ...auth.headers, 'Content-Type': 'application/json' },
      body: JSON.stringify({ volume: 180 }),
    });
    const highPayload = await highResponse.json() as { volume: number };
    assert.equal(highResponse.status, 200);
    assert.equal(highPayload.volume, 100);
    assert.equal(mpv.getVolume(), 100);

    const invalidResponse = await fetch(`${webServer.getDashboardUrl()}/api/volume`, {
      method: 'POST',
      headers: { ...auth.headers, 'Content-Type': 'application/json' },
      body: JSON.stringify({ volume: null }),
    });
    const invalidPayload = await invalidResponse.json() as { message: string };
    assert.equal(invalidResponse.status, 400);
    assert.match(invalidPayload.message, /volume must be a number/i);
  } finally {
    await webServer.destroy();
  }
});

test('WebServer rejects unauthenticated websocket and volume requests', async () => {
  const queueManager = new QueueManager();
  const mpv = new PlaybackControlsFakeMpv();
  const webServer = createWebServer(mpv as never, queueManager, { port: await getAvailablePort() });
  await webServer.waitUntilReady();

  try {
    const socket = new WebSocket(`${webServer.getDashboardUrl().replace('http', 'ws')}/ws`);
    const closeCode = await new Promise<number>((resolve) => {
      socket.once('close', (code) => resolve(code));
    });
    assert.equal(closeCode, 4403);

    const response = await fetch(`${webServer.getDashboardUrl()}/api/volume`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ volume: 50 }),
    });
    assert.equal(response.status, 403);
  } finally {
    await webServer.destroy();
  }
});

test('WebServer serves local SVG placeholder artwork with image mime type', async () => {
  const queueManager = new QueueManager();
  const mpv = new PlaybackControlsFakeMpv();
  const webServer = createWebServer(mpv as never, queueManager, { port: await getAvailablePort() });
  await webServer.waitUntilReady();

  try {
    const response = await fetch(`${webServer.getDashboardUrl()}/assets/agentune-mark.svg`);
    const body = await response.text();

    assert.equal(response.status, 200);
    assert.match(response.headers.get('content-type') ?? '', /image\/svg\+xml/i);
    assert.match(body, /<svg/i);
  } finally {
    await webServer.destroy();
  }
});
```

## File: `src/web/web-server-static-file-path.ts`
```typescript
import path from 'path';

export function resolveStaticFilePath(publicDir: string, pathname: string): string | null {
  let decodedPathname: string;
  try {
    decodedPathname = decodeURIComponent(pathname);
  } catch {
    return null;
  }

  const normalizedPathname = decodedPathname.replace(/^[\\/]+/, '');
  const resolvedPath = path.resolve(publicDir, normalizedPathname);
  const relativePath = path.relative(publicDir, resolvedPath);
  if (relativePath === '' || (!relativePath.startsWith('..') && !path.isAbsolute(relativePath))) {
    return resolvedPath;
  }

  return null;
}
```

## File: `src/web/web-server-test-helpers.ts`
```typescript
export async function getDashboardAuth(webServer: { getDashboardUrl(): string }): Promise<{
  headers: Record<string, string>;
  origin: string;
  token: string;
}> {
  const origin = new URL(webServer.getDashboardUrl()).origin;
  const response = await fetch(webServer.getDashboardUrl());
  const html = await response.text();
  const tokenMatch = html.match(/<meta name="agentune-dashboard-token" content="([^"]+)"/i);
  if (!tokenMatch?.[1]) {
    throw new Error('Dashboard auth token missing from bootstrap HTML.');
  }

  return {
    headers: {
      'Origin': origin,
      'X-Agentune-Dashboard-Token': tokenMatch[1],
    },
    origin,
    token: tokenMatch[1],
  };
}
```

## File: `src/web/web-server.ts`
```typescript
import { createServer, type IncomingMessage, type ServerResponse } from 'http';
import { createReadStream, existsSync } from 'fs';
import { readFile, stat } from 'fs/promises';
import { fileURLToPath } from 'url';
import { WebSocket, WebSocketServer } from 'ws';
import type { MpvController } from '../audio/mpv-controller.js';
import { getHistoryStore, type HistoryStore } from '../history/history-store.js';
import { getQueuePlaybackController } from '../queue/queue-playback-controller.js';
import type { QueueManager } from '../queue/queue-manager.js';
import { loadRuntimeConfig } from '../runtime/runtime-config.js';
import { getTasteEngine } from '../taste/taste-engine.js';
import { StateBroadcaster } from './state-broadcaster.js';
import { handleArtworkProxy } from './web-server-artwork-proxy.js';
import {
  getMimeType,
  openUrl,
  readJsonBody,
  readVolumeRequest,
  sendJson,
} from './web-server-helpers.js';
import { getDatabaseStatsPayload, runDatabaseAction } from './web-server-database-cleanup.js';
import {
  createDashboardSessionToken,
  DASHBOARD_SESSION_EXPIRED_MESSAGE,
  hasValidDashboardHeaderToken,
  hasValidDashboardQueryToken,
  isAllowedDashboardMutationRequest,
  isAllowedDashboardSocketRequest,
  renderDashboardHtml,
} from './web-server-auth.js';
import { resolveStaticFilePath } from './web-server-static-file-path.js';

const PUBLIC_DIR = fileURLToPath(new URL('../../public', import.meta.url));
const MAX_WEBSOCKET_PAYLOAD_BYTES = 64 * 1024;
const DASHBOARD_HTML_HEADERS = {
  'Cache-Control': 'no-store',
  'Content-Security-Policy': "default-src 'self'; script-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data: https:; connect-src 'self' ws://127.0.0.1:*",
  'Content-Type': 'text/html; charset=utf-8',
  'Referrer-Policy': 'no-referrer',
  'X-Frame-Options': 'DENY',
};

export interface WebServerOptions {
  historyStore?: HistoryStore;
  onStopDaemon?: (reason: string) => void | Promise<void>;
  port?: number;
}

export class WebServer {
  private readonly broadcaster: StateBroadcaster;
  private readonly readyPromise: Promise<void>;
  private readonly httpServer = createServer((request, response) => {
    void this.handleRequest(request, response).catch((error: Error) => {
      console.error('[web-server] Request failed', { error: error.message });
      if (!response.headersSent) {
        sendJson(response, { message: 'Internal server error' }, 500);
        return;
      }
      response.end();
    });
  });
  private readonly historyStore: HistoryStore | null;
  private readonly onStopDaemon?: (reason: string) => void | Promise<void>;
  private readonly port: number;
  private readonly dashboardSessionToken = createDashboardSessionToken();
  private readonly wsServer = new WebSocketServer({
    noServer: true,
    maxPayload: MAX_WEBSOCKET_PAYLOAD_BYTES,
  });
  private dashboardOpened = false;

  constructor(
    private readonly mpv: MpvController,
    queueManager: QueueManager,
    options?: WebServerOptions,
  ) {
    this.historyStore = options?.historyStore ?? getHistoryStore();
    this.onStopDaemon = options?.onStopDaemon;
    this.port = options?.port ?? loadRuntimeConfig().dashboardPort;
    this.broadcaster = new StateBroadcaster(mpv, queueManager);
    this.readyPromise = this.start();

    this.wsServer.on('connection', (socket, request) => {
      const url = new URL(request.url ?? '/ws', this.getDashboardUrl());
      if (!isAllowedDashboardSocketRequest(url, request.headers, this.dashboardSessionToken)) {
        socket.close(4403, 'Dashboard auth failed');
        return;
      }

      this.sendState(socket);
      this.sendPersona(socket);
      socket.on('message', (message) => {
        this.handleSocketMessage(message.toString());
      });
    });

    this.broadcaster.on('state', () => {
      this.broadcastState();
    });

    this.httpServer.on('upgrade', (request, socket, head) => {
      const url = new URL(request.url ?? '/', this.getDashboardUrl());
      if (url.pathname !== '/ws') {
        socket.destroy();
        return;
      }

      this.wsServer.handleUpgrade(request, socket, head, (client) => {
        this.wsServer.emit('connection', client, request);
      });
    });
  }

  openDashboardOnce(): void {
    if (this.dashboardOpened) {
      return;
    }

    this.dashboardOpened = true;
    void this.readyPromise.then(() => {
      openUrl(this.getDashboardUrl());
    }).catch((error: Error) => {
      console.error('[web-server] Dashboard auto-open skipped', { error: error.message });
    });
  }

  waitUntilReady(): Promise<void> {
    return this.readyPromise;
  }

  async destroy(): Promise<void> {
    this.broadcaster.destroy();
    this.wsServer.close();
    if (this.httpServer.listening) {
      await new Promise<void>((resolve) => {
        this.httpServer.close(() => resolve());
      });
    }
    if (webServer === this) {
      webServer = null;
    }
  }

  getDashboardUrl(): string {
    return `http://127.0.0.1:${this.port}`;
  }

  async broadcastStateSnapshot(): Promise<void> {
    await this.broadcaster.refresh();
    this.broadcastState();
  }

  broadcastPersona(): void {
    const taste = getTasteEngine();
    if (!taste) return;
    const payload = JSON.stringify({
      type: 'persona',
      data: taste.getPersona(),
    });
    for (const client of this.wsServer.clients) {
      if (client.readyState === WebSocket.OPEN) {
        client.send(payload);
      }
    }
  }

  private async start(): Promise<void> {
    await new Promise<void>((resolve, reject) => {
      const onError = (error: NodeJS.ErrnoException) => {
        this.httpServer.off('listening', onListening);
        reject(error);
      };
      const onListening = () => {
        this.httpServer.off('error', onError);
        resolve();
      };

      this.httpServer.once('error', onError);
      this.httpServer.once('listening', onListening);
      this.httpServer.listen(this.port, '127.0.0.1');
    });

    console.error('[web-server] Listening', { port: this.port });
    await this.broadcaster.refresh();
  }

  private async handleRequest(request: IncomingMessage, response: ServerResponse): Promise<void> {
    const url = new URL(request.url ?? '/', this.getDashboardUrl());
    const dashboardDocumentRequested = request.method === 'GET' && (url.pathname === '/' || url.pathname === '/index.html');

    if (dashboardDocumentRequested) {
      await this.handleDashboardDocument(response);
      return;
    }

    if (request.method === 'GET' && url.pathname === '/api/artwork') {
      if (!hasValidDashboardQueryToken(url, this.dashboardSessionToken)) {
        this.sendDashboardForbidden(response);
        return;
      }
      await handleArtworkProxy(url, response);
      return;
    }

    const dashboardApiRequested = url.pathname.startsWith('/api/');
    if (dashboardApiRequested && !hasValidDashboardHeaderToken(request.headers, this.dashboardSessionToken)) {
      this.sendDashboardForbidden(response);
      return;
    }
    if (dashboardApiRequested && request.method === 'POST' && !isAllowedDashboardMutationRequest(request.headers)) {
      this.sendDashboardForbidden(response);
      return;
    }

    if (request.method === 'GET' && url.pathname === '/api/status') {
      sendJson(response, this.broadcaster.getState());
      return;
    }

    if (request.method === 'GET' && url.pathname === '/api/persona') {
      const taste = getTasteEngine();
      if (!taste) {
        sendJson(response, { message: 'Unavailable' }, 503);
        return;
      }
      sendJson(response, taste.getPersona());
      return;
    }

    if (request.method === 'POST' && url.pathname === '/api/persona') {
      await this.handlePersonaUpdate(request, response);
      return;
    }

    if (request.method === 'POST' && url.pathname === '/api/volume') {
      const parsed = await readVolumeRequest(request);
      if (parsed === null) {
        sendJson(response, { message: 'volume must be a number' }, 400);
        return;
      }
      if (!this.mpv.isReady()) {
        sendJson(response, { message: 'Audio engine unavailable' }, 503);
        return;
      }

      sendJson(response, { volume: this.mpv.setVolume(parsed.volume) });
      return;
    }

    if (request.method === 'POST' && url.pathname === '/api/daemon/stop') {
      this.handleDaemonStop(response);
      return;
    }

    if (url.pathname === '/api/database/stats' && request.method === 'GET') {
      const store = this.historyStore;
      if (!store) {
        sendJson(response, { message: 'Unavailable' }, 503);
        return;
      }
      sendJson(response, getDatabaseStatsPayload(store));
      return;
    }

    if (request.method === 'POST' && isDatabaseActionPath(url.pathname)) {
      await this.handleDatabaseAction(url.pathname, response);
      return;
    }

    if (request.method !== 'GET') {
      response.writeHead(405);
      response.end();
      return;
    }

    const filePath = resolveStaticFilePath(PUBLIC_DIR, url.pathname);
    if (!filePath || !existsSync(filePath)) {
      response.writeHead(404);
      response.end('Not found');
      return;
    }

    const fileStats = await stat(filePath);
    if (!fileStats.isFile()) {
      response.writeHead(404);
      response.end('Not found');
      return;
    }

    response.writeHead(200, { 'Content-Type': getMimeType(filePath) });
    createReadStream(filePath).pipe(response);
  }

  private async handleDashboardDocument(response: ServerResponse): Promise<void> {
    const html = renderDashboardHtml(await getDashboardTemplate(), this.dashboardSessionToken);
    response.writeHead(200, DASHBOARD_HTML_HEADERS);
    response.end(html);
  }

  private async handlePersonaUpdate(request: IncomingMessage, response: ServerResponse): Promise<void> {
    const body = await readJsonBody(request);
    if (!hasOwn(body, 'taste')) {
      sendJson(response, { message: 'taste field required' }, 400);
      return;
    }
    if (typeof body?.taste !== 'string') {
      sendJson(response, { message: 'taste must be a string' }, 400);
      return;
    }

    const taste = getTasteEngine();
    if (!taste) {
      sendJson(response, { message: 'Unavailable' }, 503);
      return;
    }

    taste.saveTasteText(body.taste.slice(0, 1000));
    sendJson(response, { updated: true, ...taste.getPersona() });
    this.broadcastPersona();
  }

  private async handleDatabaseAction(pathname: string, response: ServerResponse): Promise<void> {
    const store = this.historyStore;
    if (!store) {
      sendJson(response, { message: 'Unavailable' }, 503);
      return;
    }

    const action = pathname.replace('/api/database/', '') as 'clear-history' | 'clear-provider-cache' | 'full-reset';
    const payload = await runDatabaseAction(action, store, getQueuePlaybackController());
    await this.broadcastStateSnapshot();
    sendJson(response, payload);
  }

  private handleDaemonStop(response: ServerResponse): void {
    if (!this.onStopDaemon) {
      sendJson(response, { message: 'Unavailable' }, 503);
      return;
    }

    sendJson(response, {
      stopped: true,
      message: 'Daemon stop requested. Start it again with "agentune start", or open a new coding session if auto-start is enabled.',
    });
    setTimeout(() => {
      void Promise.resolve(this.onStopDaemon?.('dashboard stop'));
    }, 100);
  }

  private sendDashboardForbidden(response: ServerResponse): void {
    sendJson(response, { message: DASHBOARD_SESSION_EXPIRED_MESSAGE }, 403);
  }

  private handleSocketMessage(rawMessage: string): void {
    try {
      const message = JSON.parse(rawMessage) as { type?: string; level?: number; taste?: string };
      if (message.type === 'update_persona' && typeof message.taste === 'string') {
        const tasteEngine = getTasteEngine();
        if (tasteEngine) {
          tasteEngine.saveTasteText(message.taste.slice(0, 1000));
          this.broadcastPersona();
        }
        return;
      }
      if (!this.mpv.isReady()) {
        return;
      }
      if (message.type === 'pause') {
        if (!this.mpv.getCurrentTrack() || !this.mpv.getIsPlaying()) {
          return;
        }
        this.mpv.pause();
        return;
      }
      if (message.type === 'playback-toggle') {
        if (!this.mpv.getCurrentTrack()) {
          return;
        }
        if (this.mpv.getIsPlaying()) {
          this.mpv.pause();
        } else {
          this.mpv.resume();
        }
        return;
      }
      if (message.type === 'next') {
        const queuePlaybackController = getQueuePlaybackController();
        if (queuePlaybackController) {
          void queuePlaybackController.skip().catch((error: Error) => {
            console.error('[web-server] Next control failed', { error: error.message });
          });
        }
        return;
      }
      if (message.type === 'volume' && typeof message.level === 'number' && Number.isFinite(message.level)) {
        this.mpv.setVolume(message.level);
      }
      if (message.type === 'mute') {
        this.mpv.toggleMute();
      }
    } catch (error) {
      console.error('[web-server] Ignored invalid message', { error: (error as Error).message });
    }
  }

  private broadcastState(): void {
    const payload = JSON.stringify({ type: 'state', data: this.broadcaster.getState() });
    for (const client of this.wsServer.clients) {
      if (client.readyState === WebSocket.OPEN) {
        client.send(payload);
      }
    }
  }

  private sendState(socket: WebSocket): void {
    socket.send(JSON.stringify({ type: 'state', data: this.broadcaster.getState() }));
  }

  private sendPersona(socket: WebSocket): void {
    const taste = getTasteEngine();
    if (!taste) return;
    socket.send(JSON.stringify({
      type: 'persona',
      data: taste.getPersona(),
    }));
  }
}

function hasOwn(value: unknown, key: string): boolean {
  return !!value && typeof value === 'object' && Object.prototype.hasOwnProperty.call(value, key);
}

function isDatabaseActionPath(pathname: string): pathname is '/api/database/clear-history' | '/api/database/clear-provider-cache' | '/api/database/full-reset' {
  return pathname === '/api/database/clear-history'
    || pathname === '/api/database/clear-provider-cache'
    || pathname === '/api/database/full-reset';
}

let webServer: WebServer | null = null;

export function createWebServer(
  mpv: MpvController,
  queueManager: QueueManager,
  options?: WebServerOptions,
): WebServer {
  if (!webServer) {
    const server = new WebServer(mpv, queueManager, options);
    webServer = server;
    void server.waitUntilReady().catch(() => {
      void server.destroy();
      if (webServer === server) {
        webServer = null;
      }
    });
  }

  return webServer;
}

export function getWebServer(): WebServer | null {
  return webServer;
}

let dashboardTemplateCache: string | null = null;

async function getDashboardTemplate(): Promise<string> {
  dashboardTemplateCache ??= await readFile(fileURLToPath(new URL('../../public/index.html', import.meta.url)), 'utf8');
  return dashboardTemplateCache;
}
```


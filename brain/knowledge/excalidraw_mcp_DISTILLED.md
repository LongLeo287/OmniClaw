---
id: excalidraw-mcp
type: knowledge
owner: OA_Triage
---
# excalidraw-mcp
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@mcp-demos/excalidraw-server",
  "version": "0.3.2",
  "type": "module",
  "packageManager": "pnpm@10.11.0",
  "description": "Streamable Excalidraw diagram MCP App server",
  "license": "MIT",
  "main": "dist/server.js",
  "types": "dist/server.d.ts",
  "bin": {
    "mcp-server-excalidraw": "dist/index.js"
  },
  "files": [
    "dist"
  ],
  "exports": {
    ".": {
      "types": "./dist/server.d.ts",
      "default": "./dist/server.js"
    }
  },
  "scripts": {
    "postinstall": "node scripts/setup-bun.mjs || echo 'setup-bun.mjs failed or not available'",
    "build": "node scripts/build.mjs",
    "watch": "vite build --watch",
    "serve": "bun --watch src/main.ts",
    "start": "cross-env NODE_ENV=development npm run build && npm run serve",
    "dev": "cross-env NODE_ENV=development concurrently 'npm run watch' 'npm run serve'",
    "dev:ui": "vite --config vite.config.dev.ts",
    "prepublishOnly": "npm run build"
  },
  "dependencies": {
    "@excalidraw/excalidraw": "^0.18.0",
    "@modelcontextprotocol/ext-apps": "^0.4.0",
    "@modelcontextprotocol/sdk": "1.25.2",
    "cors": "^2.8.5",
    "express": "^5.1.0",
    "mcp-handler": "1.0.7",
    "morphdom": "^2.7.8",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "@upstash/redis": "^1.34.0",
    "zod": "^4.0.0"
  },
  "devDependencies": {
    "@types/cors": "^2.8.19",
    "@types/express": "^5.0.0",
    "@types/node": "^22.0.0",
    "@types/react": "^19.2.2",
    "@types/react-dom": "^19.2.2",
    "@vitejs/plugin-react": "^4.3.4",
    "concurrently": "^9.2.1",
    "cross-env": "^10.1.0",
    "typescript": "^5.9.3",
    "vite": "^6.0.0",
    "vite-plugin-singlefile": "^2.3.0"
  },
  "optionalDependencies": {
    "@oven/bun-darwin-aarch64": "^1.2.21",
    "@oven/bun-darwin-x64": "^1.2.21",
    "@oven/bun-darwin-x64-baseline": "^1.2.21",
    "@oven/bun-linux-aarch64": "^1.2.21",
    "@oven/bun-linux-aarch64-musl": "^1.2.21",
    "@oven/bun-linux-x64": "^1.2.21",
    "@oven/bun-linux-x64-baseline": "^1.2.21",
    "@oven/bun-linux-x64-musl": "^1.2.21",
    "@oven/bun-linux-x64-musl-baseline": "^1.2.21",
    "@oven/bun-windows-x64": "^1.2.21",
    "@oven/bun-windows-x64-baseline": "^1.2.21"
  }
}

```

### File: README.md
```md
# Excalidraw MCP App Server

MCP server that streams hand-drawn Excalidraw diagrams with smooth viewport camera control and interactive fullscreen editing.

![Demo](docs/demo.gif)

## Install

Works with any client that supports [MCP Apps](https://modelcontextprotocol.io/docs/extensions/apps) — Claude, ChatGPT, VS Code, Goose, and others. If something doesn't work, please [open an issue](https://github.com/antonpk1/excalidraw-mcp-app/issues).

### Remote (recommended)

### `https://mcp.excalidraw.com`

For apps that don't yet have an official integration, you can add a custom MCP / connector (naming can vary between apps).

### Local

**Option A: Download Extension**

1. Download `excalidraw-mcp-app.mcpb` from [Releases](https://github.com/antonpk1/excalidraw-mcp-app/releases)
2. Double-click to install in Claude Desktop

**Option B: Build from Source**

```bash
git clone https://github.com/excalidraw/excalidraw-mcp.git
cd excalidraw-mcp-app
pnpm install && pnpm run build
```

Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "excalidraw": {
      "command": "node",
      "args": ["/path/to/excalidraw-mcp-app/dist/index.js", "--stdio"]
    }
  }
}
```

Restart Claude Desktop.

## Usage

Example prompts:
- "Draw a cute cat using excalidraw"
- "Draw an architecture diagram showing a user connecting to an API server which talks to a database"

## What are MCP Apps and how can I build one?

Text responses can only go so far. Sometimes users need to interact with data, not just read about it. [MCP Apps](https://github.com/modelcontextprotocol/ext-apps/) is an official Model Context Protocol extension that lets servers return interactive HTML interfaces (data visualizations, forms, dashboards) that render directly in the chat.

- **Getting started for humans**: [documentation](https://modelcontextprotocol.io/docs/extensions/apps)
- **Getting started for AIs**: [skill](https://github.com/modelcontextprotocol/ext-apps/blob/main/plugins/mcp-apps/skills/create-mcp-app/SKILL.md)

## Contributing

PRs welcome! See [Local](#local) above for build instructions.

### Deploy your own instance

You can deploy your own copy to Vercel in a few clicks:

1. Fork this repo
2. Go to [vercel.com/new](https://vercel.com/new) and import your fork
3. No environment variables needed — just deploy
4. Your server will be at `https://your-project.vercel.app/mcp`

### Release checklist

<details>
<summary>For maintainers</summary>

```bash
# 1. Bump version in manifest.json and package.json
# 2. Build and pack
pnpm run build && mcpb pack .

# 3. Create GitHub release
gh release create v0.3.0 excalidraw-mcp-app.mcpb --title "v0.3.0" --notes "What changed"

# 4. Deploy to Vercel
vercel --prod
```

</details>

## Credits

Built with [Excalidraw](https://github.com/excalidraw/excalidraw) — a virtual whiteboard for sketching hand-drawn like diagrams.

## License

MIT

```

### File: CLAUDE.md
```md
# Excalidraw MCP App Server

Standalone MCP server that streams Excalidraw diagrams as SVG with hand-drawn animations.

## Architecture

```
server.ts          → 2 tools (read_me, create_view) + resource + cheat sheet
main.ts            → HTTP (Streamable) + stdio transports
src/mcp-app.tsx    → ExcalidrawAppCore (widget logic) + ExcalidrawApp (useApp wrapper)
src/mcp-entry.tsx  → Production entry point: createRoot + ExcalidrawApp
src/global.css     → Animations (stroke draw-on, fade-in) + auto-resize
src/dev.tsx        → Dev entry point: mock app + sample elements + control panel
src/dev-mock.ts    → Mock MCP App with event simulation (sendToolInput, streamElements, etc.)
index-dev.html     → Dev HTML entry (served by vite dev server)
vite.config.dev.ts → Dev-only vite config (resolves from node_modules, no esm.sh externals)
```

## Tools

### `read_me` (text tool, no UI)
Returns a cheat sheet with element format, color palettes, coordinate tips, and examples. The model should call this before `create_view`.

### `create_view` (UI tool)
Takes `elements` — a JSON string of standard Excalidraw elements. The widget parses partial JSON during streaming and renders via `exportToSvg` + morphdom diffing. No Excalidraw React canvas component — pure SVG rendering.

**Screenshot as model context:** After final render, the SVG is captured as a 512px-max PNG and sent via `app.updateModelContext()` so the model can see the diagram and iterate on user feedback.

## Key Design Decisions

### Standard Excalidraw JSON — no extensions
The input is standard Excalidraw element JSON. No `label` on containers, no `start`/`end` on arrows. These are Excalidraw's internal "skeleton" API (`convertToExcalidrawElements`) — not the standard format.

**Why:** Standard format means any `.excalidraw` file's elements array works as input.

**Trade-off:** Labels require separate text elements with manually computed centered coordinates. The cheat sheet teaches the formula: `x = shape.x + (shape.width - text.width) / 2`.

### No `convertToExcalidrawElements`
We tried Excalidraw's skeleton API. Problems:
1. Needs font metrics at conversion time (canvas `measureText`)
2. Non-standard format
3. Added complexity for marginal benefit

### SVG-only rendering (no Excalidraw React canvas)
The widget uses `exportToSvg` for ALL rendering — no `<Excalidraw>` React component.

**Why:**
- Eliminates blink on final render (no component swap from SVG preview to canvas)
- Loads Virgil hand-drawn font from the start (no `skipInliningFonts`)
- morphdom works on SVG DOM — smooth diffing between streaming updates

### Auto-sizing
The container has no fixed height. SVG gets `width: 100%` + `height: auto` with the `width` attribute removed. The SVG's `viewBox` preserves aspect ratio, so height scales proportionally to content.

### CSP: `esm.sh` allowed
Excalidraw loads the Virgil font from `esm.sh` at runtime. The resource's `_meta.ui.csp.resourceDomains` includes `https://esm.sh`.

### `prefersBorder: true`
Set on the resource content's `_meta.ui` so the host renders a border/background around the widget.

### Fullscreen mode
Supports `app.requestDisplayMode({ mode: "fullscreen" })`. Button appears on hover (top-right), hidden in fullscreen (host provides exit UI). Escape key exits fullscreen.

## Checkpoint System

Two-tier storage for diagram state persistence:

### Architecture
1. **Server-side store** (primary): `CheckpointStore` interface with 3 implementations:
   - `FileCheckpointStore` — local dev, writes JSON to `$TMPDIR/excalidraw-mcp-checkpoints/`
   - `MemoryCheckpointStore` — Vercel fallback (in-memory Map, lost on cold start)
   - `RedisCheckpointStore` — Vercel with Upstash KV (persistent, 30-day TTL)
   - Factory: `createVercelStore()` picks Redis if env vars exist, else Memory

2. **localStorage** (widget-side cache): Fast local cache keyed by `excalidraw:<checkpointId>` for persisting user edits across page reloads within the same session.

### Flow
- `create_view` resolves `restoreCheckpoint` references server-side, saves fully resolved state, returns `checkpointId`
- Widget reads checkpoints via `read_checkpoint` server tool (private, app-only visibility)
- User edits in fullscreen sync back to server via `save_checkpoint` server tool (debounced)
- `cameraUpdate` elements are stored as part of checkpoint data (not a separate viewport field)

### Key Design Decisions
- Server resolves checkpoints so the model never needs to re-send full element arrays
- `containerId` filtering ensures bound text elements are deleted with their containers
- Camera aspect ratio check nudges model toward 4:3 ratios
- `checkpointId` uses `crypto.randomUUID()` truncated to 18 chars (collision-resistant, URL-safe)

## Build

```bash
npm install
npm run build
```

Build pipeline: `tsc --noEmit` → `vite build` (singlefile HTML) → `tsc -p tsconfig.server.json` → `bun build` (server + index).

## Running

```bash
# HTTP (Streamable) — default, stateless per-request
npm run serve          # or: bun --watch main.ts
# Starts on http://localhost:3001/mcp

# stdio — for Claude Desktop
node dist/index.js --stdio

# Dev mode (watch + serve) — full MCP flow
npm run dev

# Dev mode (standalone UI) — no MCP server needed
npm run dev:ui
# Opens http://localhost:5173/index-dev.html with mock app + sample diagram
```

## Claude Desktop config

```json
{
  "excalidraw": {
    "command": "node",
    "args": ["<path>/dist/index.js", "--stdio"]
  }
}
```

## Rendering Pipeline

### Streaming (`ontoolinputpartial`)
1. `parsePartialElements` tries `JSON.parse`, falls back to closing array after last `}`
2. `excludeIncompleteLastItem` drops the last element (may be incomplete)
3. Only re-renders when element **count** changes (not on every partial update)
4. Seeds are **randomized** per render — hand-drawn style animates naturally
5. `exportToSvg` generates SVG → **morphdom** diffs against existing DOM
6. morphdom preserves existing elements (no re-animation), only new elements trigger CSS animations

### Final render (`ontoolinput`)
1. Parses complete JSON, renders with **original seeds** (stable final look)
2. Same `exportToSvg` + morphdom path — seamless transition, no blink
3. Sends PNG screenshot to model context (debounced 1.5s)

### CSS Animations (3 layers)
- **Shapes** (`g, rect, circle, ellipse, text, image`): opacity fade-in 0.5s
- **Lines** (`path, line, polyline, polygon`): stroke-dashoffset draw-on effect 0.6s
- **Existing elements**: smooth `transition` on fill/stroke/opacity changes

### Key Libraries
- **morphdom**: DOM diffing for SVG — preserves existing nodes, only new nodes get animations
- **exportToSvg**: Excalidraw's SVG export (with fonts inlined by default)

## Cheat Sheet: Progressive Element Ordering

The `server.ts` cheat sheet instructs the model to emit elements progressively:
- BAD: all rectangles → all texts → all arrows (blank boxes stream, then labels appear late)
- GOOD: background shapes first, then per node: shape → label → arrows → next node
- This way each node appears complete with its label during streaming

## Debugging

### Dev workflow
1. Edit source files
2. `npm run build` (or `npm run dev` for watch mode)
3. Restart the server process (module cache means hot reload doesn't pick up `server.ts` changes for tool definitions)
4. In Claude Desktop: restart the MCP server connection

### Widget logging — NEVER use console.log

Use the SDK logger — it routes through the host to the log file:

```typescript
app.sendLog({ level: "info", logger: "Excalidraw", data: "my message" });
```

**Log file**: `~/Library/Logs/Claude/claude.ai-web.log`

```bash
# Fullscreen transition logs (logger: "FS")
grep "FS" ~/Library/Logs/Claude/claude.ai-web.log | tail -40

# General widget logs (logger: "Excalidraw")
grep "Excalidraw" ~/Library/Logs/Claude/claude.ai-web.log | tail -20

# Clear logs before repro for clean output
> ~/Library/Logs/Claude/claude.ai-web.log
```

### Widget debugging
- The widget runs in an iframe
- Check that `exportToSvg` isn't throwing (catches are silent)
- morphdom issues: compare old vs new SVG structure in Elements panel

### Common issues
- **No diagram appears:** Check that `ontoolinputpartial` is firing — the `elements` field might be nested differently (`params.arguments.elements` vs `params.elements`)
- **All elements re-animate on each update:** morphdom not working — check that SVG structure is similar enough for diffing (different root SVG attributes can cause full replacement)
- **Font is default (not hand-drawn):** `skipInliningFonts` was set to `true` — must be removed/false
- **Elements in wrong positions during animation:** Don't use CSS `transform: scale()` on SVG child elements — conflicts with Excalidraw's own transform attributes. Use opacity-only animations.

## Gotchas

- `ExcalidrawElement` type is at `@excalidraw/excalidraw/element/types`, not re-exported from main
- `ExcalidrawImperativeAPI` type is at `@excalidraw/excalidraw/types`
- Excalidraw's `containerId` on text elements does NOT auto-position text — that only works via `convertToExcalidrawElements` skeleton API
- The `.SVGLayer` div is not used for rendering but takes layout space — safe to `display: none`
- morphdom is essential — without it, replacing innerHTML re-triggers all animations on every update
- `ReactDOM.render()` per update remounts the tree and kills animations — use `createRoot()` once + `useState` if adding React components

```

### File: index-dev.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Excalidraw MCP — Dev</title>
</head>
<body>
  <script type="module" src="/src/dev.tsx"></script>
</body>
</html>

```

### File: manifest.json
```json
{
  "manifest_version": "0.3",
  "name": "excalidraw-mcp-app",
  "display_name": "Excalidraw",
  "version": "0.3.2",
  "description": "Hand-drawn diagrams with streaming animations, fullscreen editing, checkpoint/restore, and one-click export to excalidraw.com.",
  "long_description": "An MCP App server that renders Excalidraw diagrams with hand-drawn style. Features streaming SVG rendering with draw-on animations, smooth viewport camera panning, label binding, interactive fullscreen editing with export to excalidraw.com, checkpoint/restore for iterative edits, and screenshot context sent back to Claude for feedback.",
  "author": {
    "name": "Anton Pidkuiko",
    "url": "https://github.com/antonpk1"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/antonpk1/excalidraw-mcp-app.git"
  },
  "homepage": "https://github.com/antonpk1/excalidraw-mcp-app",
  "icon": "docs/logo.png",
  "server": {
    "type": "node",
    "entry_point": "dist/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/dist/index.js", "--stdio"]
    }
  },
  "tools": [
    {
      "name": "read_me",
      "description": "Returns the Excalidraw element format reference with color palettes, examples, and tips. Call this before using create_view."
    },
    {
      "name": "create_view",
      "description": "Renders a hand-drawn diagram using Excalidraw elements with streaming draw-on animations."
    }
  ],
  "keywords": ["excalidraw", "diagrams", "drawing", "visualization", "mcp-app"],
  "compatibility": {
    "platforms": ["darwin", "win32", "linux"],
    "runtimes": {
      "node": ">=18.0.0"
    }
  },
  "license": "MIT"
}

```

### File: pnpm-lock.yaml
```yaml
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    dependencies:
      '@excalidraw/excalidraw':
        specifier: ^0.18.0
        version: 0.18.0(@types/react-dom@19.2.3(@types/react@19.2.14))(@types/react@19.2.14)(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      '@modelcontextprotocol/ext-apps':
        specifier: ^0.4.0
        version: 0.4.2(@modelcontextprotocol/sdk@1.25.2(hono@4.11.9)(zod@4.3.6))(react-dom@19.2.4(react@19.2.4))(react@19.2.4)(zod@4.3.6)
      '@modelcontextprotocol/sdk':
        specifier: 1.25.2
        version: 1.25.2(hono@4.11.9)(zod@4.3.6)
      '@upstash/redis':
        specifier: ^1.34.0
        version: 1.36.2
      cors:
        specifier: ^2.8.5
        version: 2.8.6
      express:
        specifier: ^5.1.0
        version: 5.2.1
      mcp-handler:
        specifier: 1.0.7
        version: 1.0.7(@modelcontextprotocol/sdk@1.25.2(hono@4.11.9)(zod@4.3.6))
      morphdom:
        specifier: ^2.7.8
        version: 2.7.8
      react:
        specifier: ^19.0.0
        version: 19.2.4
      react-dom:
        specifier: ^19.0.0
        version: 19.2.4(react@19.2.4)
      zod:
        specifier: ^4.0.0
        version: 4.3.6
    devDependencies:
      '@types/cors':
        specifier: ^2.8.19
        version: 2.8.19
      '@types/express':
        specifier: ^5.0.0
        version: 5.0.6
      '@types/node':
        specifier: ^22.0.0
        version: 22.19.11
      '@types/react':
        specifier: ^19.2.2
        version: 19.2.14
      '@types/react-dom':
        specifier: ^19.2.2
        version: 19.2.3(@types/react@19.2.14)
      '@vitejs/plugin-react':
        specifier: ^4.3.4
        version: 4.7.0(vite@6.4.1(@types/node@22.19.11)(sass@1.51.0))
      concurrently:
        specifier: ^9.2.1
        version: 9.2.1
      cross-env:
        specifier: ^10.1.0
        version: 10.1.0
      typescript:
        specifier: ^5.9.3
        version: 5.9.3
      vite:
        specifier: ^6.0.0
        version: 6.4.1(@types/node@22.19.11)(sass@1.51.0)
      vite-plugin-singlefile:
        specifier: ^2.3.0
        version: 2.3.0(rollup@4.57.1)(vite@6.4.1(@types/node@22.19.11)(sass@1.51.0))
    optionalDependencies:
      '@oven/bun-darwin-aarch64':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-darwin-x64':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-darwin-x64-baseline':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-linux-aarch64':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-linux-aarch64-musl':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-linux-x64':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-linux-x64-baseline':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-linux-x64-musl':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-linux-x64-musl-baseline':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-windows-x64':
        specifier: ^1.2.21
        version: 1.3.9
      '@oven/bun-windows-x64-baseline':
        specifier: ^1.2.21
        version: 1.3.9

packages:

  '@babel/code-frame@7.29.0':
    resolution: {integrity: sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==}
    engines: {node: '>=6.9.0'}

  '@babel/compat-data@7.29.0':
    resolution: {integrity: sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==}
    engines: {node: '>=6.9.0'}

  '@babel/core@7.29.0':
    resolution: {integrity: sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42Pf1XTYED2Rni5f95npYeuwMDQA==}
    engines: {node: '>=6.9.0'}

  '@babel/generator@7.29.1':
    resolution: {integrity: sha512-qsaF+9Qcm2Qv8SRIMMscAvG4O3lJ0F1GuMo5HR/Bp02LopNgnZBC/EkbevHFeGs4ls/oPz9v+Bsmzbkbe+0dUw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-compilation-targets@7.28.6':
    resolution: {integrity: sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-globals@7.28.0':
    resolution: {integrity: sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-imports@7.28.6':
    resolution: {integrity: sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-transforms@7.28.6':
    resolution: {integrity: sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0

  '@babel/helper-plugin-utils@7.28.6':
    resolution: {integrity: sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-string-parser@7.27.1':
    resolution: {integrity: sha512-qMlSxKbpRlAridDExk92nSobyDdpPijUq2DW6oDnUqd0iOGxmQjyqhMIihI9+zv4LPyZdRje2cavWPbCbWm3eA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-identifier@7.28.5':
    resolution: {integrity: sha512-qSs4ifwzKJSV39ucNjsvc6WVHs6b7S03sOh2OcHF9UHfVPqWWALUsNUVzhSBiItjRZoLHx7nIarVjqKVusUZ1Q==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-validator-option@7.27.1':
    resolution: {integrity: sha512-YvjJow9FxbhFFKDSuFnVCe2WxXk1zWc22fFePVNEaWJEu8IrZVlda6N0uHwzZrUM1il7NC9Mlp4MaJYbYd9JSg==}
    engines: {node: '>=6.9.0'}

  '@babel/helpers@7.28.6':
    resolution: {integrity: sha512-xOBvwq86HHdB7WUDTfKfT/Vuxh7gElQ+Sfti2Cy6yIWNW05P8iUslOVcZ4/sKbE+/jQaukQAdz/gf3724kYdqw==}
    engines: {node: '>=6.9.0'}

  '@babel/parser@7.29.0':
    resolution: {integrity: sha512-IyDgFV5GeDUVX4YdF/3CPULtVGSXXMLh1xVIgdCgxApktqnQV0r7/8Nqthg+8YLGaAtdyIlo2qIdZrbCv4+7ww==}
    engines: {node: '>=6.0.0'}
    hasBin: true

  '@babel/plugin-transform-react-jsx-self@7.27.1':
    resolution: {integrity: sha512-6UzkCs+ejGdZ5mFFC/OCUrv028ab2fp1znZmCZjAOBKiBK2jXD1O+BPSfX8X2qjJ75fZBMSnQn3Rq2mrBJK2mw==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0

  '@babel/plugin-transform-react-jsx-source@7.27.1':
    resolution: {integrity: sha512-zbwoTsBruTeKB9hSq73ha66iFeJHuaFkUbwvqElnygoNbj/jHRsSeokowZFN3CZ64IvEqcmmkVe89OPXc7ldAw==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0

  '@babel/runtime@7.28.6':
    resolution: {integrity: sha512-05WQkdpL9COIMz4LjTxGpPNCdlpyimKppYNoJ5Di5EUObifl8t4tuLuUBBZEpoLYOmfvIWrsp9fCl0HoPRVTdA==}
    engines: {node: '>=6.9.0'}

  '@babel/template@7.28.6':
    resolution: {integrity: sha512-YA6Ma2KsCdGb+WC6UpBVFJGXL58MDA6oyONbjyF/+5sBgxY/dwkhLogbMT2GXXyU84/IhRw/2D1Os1B/giz+BQ==}
    engines: {node: '>=6.9.0'}

  '@babel/traverse@7.29.0':
    resolution: {integrity: sha512-4HPiQr0X7+waHfyXPZpWPfWL/J7dcN1mx9gL6WdQVMbPnF3+ZhSMs8tCxN7oHddJE9fhNE7+lxdnlyemKfJRuA==}
    engines: {node: '>=6.9.0'}

  '@babel/types@7.29.0':
    resolution: {integrity: sha512-LwdZHpScM4Qz8Xw2iKSzS+cfglZzJGvofQICy7W7v4caru4EaAmyUuO6BGrbyQ2mYV11W0U8j5mBhd14dd3B0A==}
    engines: {node: '>=6.9.0'}

  '@braintree/sanitize-url@6.0.2':
    resolution: {integrity: sha512-Tbsj02wXCbqGmzdnXNk0SOF19ChhRU70BsroIi4Pm6Ehp56in6vch94mfbdQ17DozxkL3BAVjbZ4Qc1a0HFRAg==}

  '@epic-web/invariant@1.0.0':
    resolution: {integrity: sha512-lrTPqgvfFQtR/eY/qkIzp98OGdNJu0m5ji3q/nJI8v3SXkRKEnWiOxMmbvcSoAIzv/cGiuvRy57k4suKQSAdwA==}

  '@esbuild/aix-ppc64@0.25.12':
    resolution: {integrity: sha512-Hhmwd6CInZ3dwpuGTF8fJG6yoWmsToE+vYgD4nytZVxcu1ulHpUQRAB1UJ8+N1Am3Mz4+xOByoQoSZf4D+CpkA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.25.12':
    resolution: {integrity: sha512-6AAmLG7zwD1Z159jCKPvAxZd4y/VTO0VkprYy+3N2FtJ8+BQWFXU+OxARIwA46c5tdD9SsKGZ/1ocqBS/gAKHg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.25.12':
    resolution: {integrity: sha512-VJ+sKvNA/GE7Ccacc9Cha7bpS8nyzVv0jdVgwNDaR4gDMC/2TTRc33Ip8qrNYUcpkOHUT5OZ0bUcNNVZQ9RLlg==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.25.12':
    resolution: {integrity: sha512-5jbb+2hhDHx5phYR2By8GTWEzn6I9UqR11Kwf22iKbNpYrsmRB18aX/9ivc5cabcUiAT/wM+YIZ6SG9QO6a8kg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.25.12':
    resolution: {integrity: sha512-N3zl+lxHCifgIlcMUP5016ESkeQjLj/959RxxNYIthIg+CQHInujFuXeWbWMgnTo4cp5XVHqFPmpyu9J65C1Yg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.25.12':
    resolution: {integrity: sha512-HQ9ka4Kx21qHXwtlTUVbKJOAnmG1ipXhdWTmNXiPzPfWKpXqASVcWdnf2bnL73wgjNrFXAa3yYvBSd9pzfEIpA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.25.12':
    resolution: {integrity: sha512-gA0Bx759+7Jve03K1S0vkOu5Lg/85dou3EseOGUes8flVOGxbhDDh/iZaoek11Y8mtyKPGF3vP8XhnkDEAmzeg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.25.12':
    resolution: {integrity: sha512-TGbO26Yw2xsHzxtbVFGEXBFH0FRAP7gtcPE7P5yP7wGy7cXK2oO7RyOhL5NLiqTlBh47XhmIUXuGciXEqYFfBQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/linux-arm64@0.25.12':
    resolution: {integrity: sha512-8bwX7a8FghIgrupcxb4aUmYDLp8pX06rGh5HqDT7bB+8Rdells6mHvrFHHW2JAOPZUbnjUpKTLg6ECyzvas2AQ==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm@0.25.12':
    resolution: {integrity: sha512-lPDGyC1JPDou8kGcywY0YILzWlhhnRjdof3UlcoqYmS9El818LLfJJc3PXXgZHrHCAKs/Z2SeZtDJr5MrkxtOw==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-ia32@0.25.12':
    resolution: {integrity: sha512-0y9KrdVnbMM2/vG8KfU0byhUN+EFCny9+8g202gYqSSVMonbsCfLjUO+rCci7pM0WBEtz+oK/PIwHkzxkyharA==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-loong64@0.25.12':
    resolution: {integrity: sha512-h///Lr5a9rib/v1GGqXVGzjL4TMvVTv+s1DPoxQdz7l/AYv6LDSxdIwzxkrPW438oUXiDtwM10o9PmwS/6Z0Ng==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-mips64el@0.25.12':
    resolution: {integrity: sha512-iyRrM1Pzy9GFMDLsXn1iHUm18nhKnNMWscjmp4+hpafcZjrr2WbT//d20xaGljXDBYHqRcl8HnxbX6uaA/eGVw==}
    engines: {node: '>=18'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-ppc64@0.25.12':
    resolution: {integrity: sha512-9meM/lRXxMi5PSUqEXRCtVjEZBGwB7P/D4yT8UG/mwIdze2aV4Vo6U5gD3+RsoHXKkHCfSxZKzmDssVlRj1QQA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-riscv64@0.25.12':
    resolution: {integrity: sha512-Zr7KR4hgKUpWAwb1f3o5ygT04MzqVrGEGXGLnj15YQDJErYu/BGg+wmFlIDOdJp0PmB0lLvxFIOXZgFRrdjR0w==}
    engines: {node: '>=18'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-s390x@0.25.12':
    resolution: {integrity: sha512-MsKncOcgTNvdtiISc/jZs/Zf8d0cl/t3gYWX8J9ubBnVOwlk65UIEEvgBORTiljloIWnBzLs4qhzPkJcitIzIg==}
    engines: {node: '>=18'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-x64@0.25.12':
    resolution: {integrity: sha512-uqZMTLr/zR/ed4jIGnwSLkaHmPjOjJvnm6TVVitAa08SLS9Z0VM8wIRx7gWbJB5/J54YuIMInDquWyYvQLZkgw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [linux]

  '@esbuild/netbsd-arm64@0.25.12':
    resolution: {integrity: sha512-xXwcTq4GhRM7J9A8Gv5boanHhRa/Q9KLVmcyXHCTaM4wKfIpWkdXiMog/KsnxzJ0A1+nD+zoecuzqPmCRyBGjg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.25.12':
    resolution: {integrity: sha512-Ld5pTlzPy3YwGec4OuHh1aCVCRvOXdH8DgRjfDy/oumVovmuSzWfnSJg+VtakB9Cm0gxNO9BzWkj6mtO1FMXkQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [netbsd]

  '@esbuild/openbsd-arm64@0.25.12':
    resolution: {integrity: sha512-fF96T6KsBo/pkQI950FARU9apGNTSlZGsv1jZBAlcLL1MLjLNIWPBkj5NlSz8aAzYKg+eNqknrUJ24QBybeR5A==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openbsd]

  '@esbuild/openbsd-x64@0.25.12':
    resolution: {integrity: sha512-MZyXUkZHjQxUvzK7rN8DJ3SRmrVrke8ZyRusHlP+kuwqTcfWLyqMOE3sScPPyeIXN/mDJIfGXvcMqCgYKekoQw==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [openbsd]

  '@esbuild/openharmony-arm64@0.25.12':
    resolution: {integrity: sha512-rm0YWsqUSRrjncSXGA7Zv78Nbnw4XL6/dzr20cyrQf7ZmRcsovpcRBdhD43Nuk3y7XIoW2OxMVvwuRvk9XdASg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [openharmony]

  '@esbuild/sunos-x64@0.25.12':
    resolution: {integrity: sha512-3wGSCDyuTHQUzt0nV7bocDy72r2lI33QL3gkDNGkod22EsYl04sMf0qLb8luNKTOmgF/eDEDP5BFNwoBKH441w==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [sunos]

  '@esbuild/win32-arm64@0.25.12':
    resolution: {integrity: sha512-rMmLrur64A7+DKlnSuwqUdRKyd3UE7oPJZmnljqEptesKM8wx9J8gx5u0+9Pq0fQQW8vqeKebwNXdfOyP+8Bsg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [win32]

  '@esbuild/win32-ia32@0.25.12':
    resolution: {integrity: sha512-HkqnmmBoCbCwxUKKNPBixiWDGCpQGVsrQfJoVGYLPT41XWF8lHuE5N6WhVia2n4o5QK5M4tYr21827fNhi4byQ==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [win32]

  '@esbuild/win32-x64@0.25.12':
    resolution: {integrity: sha512-alJC0uCZpTFrSL0CCDjcgleBXPnCrEAhTBILpeAp7M/OFgoqtAetfBzX0xM00MUsVVPpVjlPuMbREqnZCXaTnA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [win32]

  '@excalidraw/excalidraw@0.18.0':
    resolution: {integrity: sha512-QkIiS+5qdy8lmDWTKsuy0sK/fen/LRDtbhm2lc2xcFcqhv2/zdg95bYnl+wnwwXGHo7kEmP65BSiMHE7PJ3Zpw==}
    peerDependencies:
      react: ^17.0.2 || ^18.2.0 || ^19.0.0
      react-dom: ^17.0.2 || ^18.2.0 || ^19.0.0

  '@excalidraw/laser-pointer@1.3.1':
    resolution: {integrity: sha512-psA1z1N2qeAfsORdXc9JmD2y4CmDwmuMRxnNdJHZexIcPwaNEyIpNcelw+QkL9rz9tosaN9krXuKaRqYpRAR6g==}

  '@excalidraw/markdown-to-text@0.1.2':
    resolution: {integrity: sha512-1nDXBNAojfi3oSFwJswKREkFm5wrSjqay81QlyRv2pkITG/XYB5v+oChENVBQLcxQwX4IUATWvXM5BcaNhPiIg==}

  '@excalidraw/mermaid-to-excalidraw@1.1.2':
    resolution: {integrity: sha512-hAFv/TTIsOdoy0dL5v+oBd297SQ+Z88gZ5u99fCIFuEMHfQuPgLhU/ztKhFSTs7fISwVo6fizny/5oQRR3d4tQ==}

  '@excalidraw/random-username@1.1.0':
    resolution: {integrity: sha512-nULYsQxkWHnbmHvcs+efMkJ4/9TtvNyFeLyHdeGxW0zHs6P+jYVqcRff9A6Vq9w9JXeDRnRh2VKvTtS19GW2qA==}
    engines: {node: '>=10'}

  '@floating-ui/core@1.7.4':
    resolution: {integrity: sha512-C3HlIdsBxszvm5McXlB8PeOEWfBhcGBTZGkGlWc2U0KFY5IwG5OQEuQ8rq52DZmcHDlPLd+YFBK+cZcytwIFWg==}

  '@floating-ui/dom@1.7.5':
    resolution: {integrity: sha512-N0bD2kIPInNHUHehXhMke1rBGs1dwqvC9O9KYMyyjK7iXt7GAhnro7UlcuYcGdS/yYOlq0MAVgrow8IbWJwyqg==}

  '@floating-ui/react-dom@2.1.7':
    resolution: {integrity: sha512-0tLRojf/1Go2JgEVm+3Frg9A3IW8bJgKgdO0BN5RkF//ufuz2joZM63Npau2ff3J6lUVYgDSNzNkR+aH3IVfjg==}
    peerDependencies:
      react: '>=16.8.0'
      react-dom: '>=16.8.0'

  '@floating-ui/utils@0.2.10':
    resolution: {integrity: sha512-aGTxbpbg8/b5JfU1HXSrbH3wXZuLPJcNEcZQFMxLs3oSzgtVu6nFPkbbGGUvBcUjKV2YyB9Wxxabo+HEH9tcRQ==}

  '@hono/node-server@1.19.9':
    resol
... [TRUNCATED]
```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "lib": ["ESNext", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "skipLibCheck": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src", "server.ts"]
}

```

### File: tsconfig.server.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022"],
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "declaration": true,
    "emitDeclarationOnly": true,
    "outDir": "./dist",
    "rootDir": "src",
    "strict": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "resolveJsonModule": true
  },
  "include": ["src/server.ts"]
}

```

### File: vercel.json
```json
{
  "buildCommand": "pnpm run build",
  "outputDirectory": ".",
  "cleanUrls": false,
  "redirects": [
    { "source": "/", "destination": "/mcp", "statusCode": 308 }
  ],
  "rewrites": [
    { "source": "/mcp", "destination": "/api/mcp" },
    { "source": "/sse", "destination": "/api/mcp" },
    { "source": "/message", "destination": "/api/mcp" }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "Access-Control-Allow-Origin", "value": "*" },
        { "key": "Access-Control-Allow-Methods", "value": "GET, POST, DELETE, OPTIONS" },
        { "key": "Access-Control-Allow-Headers", "value": "Content-Type, Accept, Authorization, Mcp-Session-Id" }
      ]
    }
  ]
}

```

### File: vite.config.dev.ts
```ts
import path from "path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

/**
 * Dev-only vite config — serves the widget standalone (no MCP host).
 * Resolves all deps from node_modules (no esm.sh externals, no singlefile).
 * Entry: index-dev.html (not the default index.html).
 */
export default defineConfig({
  plugins: [react()],
  server: { port: 5173, open: "/index-dev.html" },
  build: {
    rollupOptions: {
      input: path.resolve(__dirname, "index-dev.html"),
    },
  },
});

```

### File: vite.config.ts
```ts
import path from "path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { viteSingleFile } from "vite-plugin-singlefile";

const isDevelopment = process.env.NODE_ENV === "development";

export default defineConfig({
  plugins: [react(), viteSingleFile()],
  build: {
    sourcemap: isDevelopment ? "inline" : undefined,
    cssMinify: !isDevelopment,
    minify: !isDevelopment,

    rollupOptions: {
      input: path.resolve(__dirname, "src/mcp-app.html"),
      external: [
        "react",
        "react-dom",
        "react-dom/client",
        "react/jsx-runtime",
        "@excalidraw/excalidraw",
        "morphdom",
      ],
      output: {
        paths: {
          "react": "https://esm.sh/react@19.0.0",
          "react-dom": "https://esm.sh/react-dom@19.0.0?deps=react@19.0.0",
          "react-dom/client": "https://esm.sh/react-dom@19.0.0/client?deps=react@19.0.0",
          "react/jsx-runtime": "https://esm.sh/react@19.0.0/jsx-runtime",
          "@excalidraw/excalidraw": "https://esm.sh/@excalidraw/excalidraw@0.18.0?deps=react@19.0.0,react-dom@19.0.0",
          "morphdom": "https://esm.sh/morphdom@2.7.8",
        },
      },
    },
    outDir: "dist",
    emptyOutDir: false,
  },
});

```

### File: api\mcp.ts
```ts
import { createMcpHandler } from "mcp-handler";
import path from "node:path";
import { createVercelStore } from "../src/checkpoint-store.js";
import { registerTools } from "../src/server.js";

const store = createVercelStore();

const mcpHandler = createMcpHandler(
  (server) => {
    const distDir = path.join(process.cwd(), "dist");
    registerTools(server, distDir, store);
  },
  { serverInfo: { name: "Excalidraw", version: "1.0.0" } },
  { basePath: "", maxDuration: 60, sessionIdGenerator: undefined },
);

// Wrap to support both /mcp and /api/mcp (backward compat)
const handler = async (request: Request) => {
  const url = new URL(request.url);
  if (url.pathname.startsWith("/api/")) {
    url.pathname = url.pathname.replace("/api/", "/");
    return mcpHandler(new Request(url.toString(), request));
  }
  return mcpHandler(request);
};

export { handler as GET, handler as POST, handler as DELETE };

```

### File: src\checkpoint-store.ts
```ts
import fs from "node:fs";
import path from "node:path";
import os from "node:os";

/** Maximum serialized checkpoint size (5 MB). */
const MAX_CHECKPOINT_BYTES = 5 * 1024 * 1024;

/** Maximum number of checkpoints kept on disk before pruning oldest. */
const MAX_FILE_CHECKPOINTS = 100;

/**
 * Validates that a checkpoint ID is safe to use as a filename.
 * Rejects path traversal attempts and other filesystem-unsafe characters.
 */
function validateCheckpointId(id: string): void {
  if (!/^[a-zA-Z0-9_-]+$/.test(id)) {
    throw new Error(`Invalid checkpoint id: must be alphanumeric, hyphens, or underscores`);
  }
  if (id.length > 64) {
    throw new Error(`Invalid checkpoint id: exceeds 64 character limit`);
  }
}

export interface CheckpointStore {
  save(id: string, data: { elements: any[] }): Promise<void>;
  load(id: string): Promise<{ elements: any[] } | null>;
}

export class FileCheckpointStore implements CheckpointStore {
  private dir: string;
  constructor() {
    this.dir = path.join(os.tmpdir(), "excalidraw-mcp-checkpoints");
    fs.mkdirSync(this.dir, { recursive: true });
  }
  async save(id: string, data: { elements: any[] }): Promise<void> {
    validateCheckpointId(id);
    const serialized = JSON.stringify(data);
    if (serialized.length > MAX_CHECKPOINT_BYTES) {
      throw new Error(`Checkpoint data exceeds ${MAX_CHECKPOINT_BYTES} byte limit`);
    }
    const filePath = path.join(this.dir, `${id}.json`);
    // Verify resolved path stays within checkpoint directory
    if (!path.resolve(filePath).startsWith(path.resolve(this.dir) + path.sep)) {
      throw new Error("Invalid checkpoint path");
    }
    await fs.promises.writeFile(filePath, serialized);
    await this.pruneOldCheckpoints();
  }
  async load(id: string): Promise<{ elements: any[] } | null> {
    validateCheckpointId(id);
    const filePath = path.join(this.dir, `${id}.json`);
    if (!path.resolve(filePath).startsWith(path.resolve(this.dir) + path.sep)) {
      throw new Error("Invalid checkpoint path");
    }
    try {
      const raw = await fs.promises.readFile(filePath, "utf-8");
      return JSON.parse(raw);
    } catch { return null; }
  }
  /** Remove oldest checkpoints when count exceeds the limit. */
  private async pruneOldCheckpoints(): Promise<void> {
    try {
      const entries = await fs.promises.readdir(this.dir);
      const jsonFiles = entries.filter(f => f.endsWith(".json"));
      if (jsonFiles.length <= MAX_FILE_CHECKPOINTS) return;

      const stats = await Promise.all(
        jsonFiles.map(async f => ({
          name: f,
          mtime: (await fs.promises.stat(path.join(this.dir, f))).mtimeMs,
        }))
      );
      stats.sort((a, b) => a.mtime - b.mtime);
      const toRemove = stats.slice(0, stats.length - MAX_FILE_CHECKPOINTS);
      await Promise.all(
        toRemove.map(f => fs.promises.unlink(path.join(this.dir, f.name)).catch(() => {}))
      );
    } catch {
      // Best-effort cleanup; don't fail the save
    }
  }
}

const memoryStore = new Map<string, string>();
export class MemoryCheckpointStore implements CheckpointStore {
  async save(id: string, data: { elements: any[] }): Promise<void> {
    validateCheckpointId(id);
    const serialized = JSON.stringify(data);
    if (serialized.length > MAX_CHECKPOINT_BYTES) {
      throw new Error(`Checkpoint data exceeds ${MAX_CHECKPOINT_BYTES} byte limit`);
    }
    memoryStore.set(id, serialized);
    // Evict oldest entries if over limit
    if (memoryStore.size > MAX_FILE_CHECKPOINTS) {
      const oldest = memoryStore.keys().next().value;
      if (oldest !== undefined) memoryStore.delete(oldest);
    }
  }
  async load(id: string): Promise<{ elements: any[] } | null> {
    validateCheckpointId(id);
    const raw = memoryStore.get(id);
    if (!raw) return null;
    try { return JSON.parse(raw); } catch { return null; }
  }
}

const REDIS_TTL_SECONDS = 30 * 24 * 60 * 60;
export class RedisCheckpointStore implements CheckpointStore {
  private redis: any = null;
  private async getRedis() {
    if (!this.redis) {
      const { Redis } = await import("@upstash/redis");
      const url = process.env.KV_REST_API_URL ?? process.env.UPSTASH_REDIS_REST_URL;
      const token = process.env.KV_REST_API_TOKEN ?? process.env.UPSTASH_REDIS_REST_TOKEN;
      if (!url || !token) throw new Error("Missing Redis env vars (KV_REST_API_* or UPSTASH_REDIS_REST_*)");
      this.redis = new Redis({ url, token });
    }
    return this.redis;
  }
  async save(id: string, data: { elements: any[] }): Promise<void> {
    validateCheckpointId(id);
    const serialized = JSON.stringify(data);
    if (serialized.length > MAX_CHECKPOINT_BYTES) {
      throw new Error(`Checkpoint data exceeds ${MAX_CHECKPOINT_BYTES} byte limit`);
    }
    const redis = await this.getRedis();
    await redis.set(`cp:${id}`, serialized, { ex: REDIS_TTL_SECONDS });
  }
  async load(id: string): Promise<{ elements: any[] } | null> {
    validateCheckpointId(id);
    const redis = await this.getRedis();
    const raw = await redis.get(`cp:${id}`);
    if (!raw) return null;
    try { return typeof raw === "string" ? JSON.parse(raw) : raw; } catch { return null; }
  }
}

export function createVercelStore(): CheckpointStore {
  if (process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL) {
    return new RedisCheckpointStore();
  }
  return new MemoryCheckpointStore();
}

```

### File: src\dev-mock.ts
```ts
/**
 * Mock MCP App for standalone UI development.
 *
 * Implements the subset of the App interface used by ExcalidrawAppCore,
 * and exposes methods to simulate MCP events (tool input, streaming, etc.).
 */
import type { App } from "@modelcontextprotocol/ext-apps";

export interface MockAppControls {
  /** Pass this to <ExcalidrawAppCore app={mock.app} /> */
  app: App;
  /** Simulate final tool input (ontoolinput) — as if the model finished generating. */
  sendToolInput(elements: any[]): void;
  /** Simulate partial/streaming tool input (ontoolinputpartial). */
  sendToolInputPartial(elements: any[]): void;
  /** Simulate tool result (ontoolresult) with optional checkpointId. */
  sendToolResult(checkpointId?: string): void;
  /**
   * Stream elements one-by-one with a delay, then finalize.
   * Useful for testing the streaming SVG preview pipeline.
   */
  streamElements(elements: any[], intervalMs?: number): void;
}

export function createMockApp(): MockAppControls {
  // Mutable handler slots — ExcalidrawAppCore assigns these via useEffect
  let _ontoolinput: ((input: any) => Promise<void>) | null = null;
  let _ontoolinputpartial: ((input: any) => Promise<void>) | null = null;
  let _ontoolresult: ((result: any) => void) | null = null;
  let _onhostcontextchanged: ((ctx: any) => void) | null = null;

  const app = {
    // --- Handler setters (ExcalidrawAppCore assigns these) ---
    set ontoolinput(fn: any) { _ontoolinput = fn; },
    get ontoolinput() { return _ontoolinput; },
    set ontoolinputpartial(fn: any) { _ontoolinputpartial = fn; },
    get ontoolinputpartial() { return _ontoolinputpartial; },
    set ontoolresult(fn: any) { _ontoolresult = fn; },
    get ontoolresult() { return _ontoolresult; },
    set onhostcontextchanged(fn: any) { _onhostcontextchanged = fn; },
    get onhostcontextchanged() { return _onhostcontextchanged; },
    set onteardown(_fn: any) { /* noop */ },
    set onerror(_fn: any) { /* noop */ },

    // --- Methods ---
    sendLog({ logger, data }: { level: string; logger: string; data: string }) {
      console.log(`[${logger}] ${data}`);
    },

    async requestDisplayMode({ mode }: { mode: string }) {
      // Simulate host responding with the requested mode
      if (_onhostcontextchanged) {
        _onhostcontextchanged({
          displayMode: mode,
          containerDimensions: { height: window.innerHeight },
        });
      }
      return { mode };
    },

    async callServerTool({ name, arguments: args }: { name: string; arguments: any }) {
      console.log(`[mock] callServerTool: ${name}`, args);
      if (name === "read_checkpoint") {
        return { content: [{ type: "text", text: "null" }], isError: false };
      }
      if (name === "save_checkpoint") {
        return { content: [], isError: false };
      }
      if (name === "export_to_excalidraw") {
        // Return a mock URL
        return { content: [{ type: "text", text: "https://excalidraw.com/#mock-dev" }], isError: false };
      }
      return { content: [], isError: false };
    },

    getHostContext() {
      return { containerDimensions: { height: 600 } };
    },

    async openLink({ url }: { url: string }) {
      console.log(`[mock] openLink: ${url}`);
      window.open(url, "_blank");
    },

    async updateModelContext(opts: any) {
      console.log("[mock] updateModelContext", opts);
    },
  } as unknown as App;

  return {
    app,

    sendToolInput(elements: any[]) {
      _ontoolinput?.({ elements: JSON.stringify(elements) });
    },

    sendToolInputPartial(elements: any[]) {
      _ontoolinputpartial?.({ elements: JSON.stringify(elements) });
    },

    sendToolResult(checkpointId = "dev-checkpoint") {
      _ontoolresult?.({ structuredContent: { checkpointId } });
    },

    streamElements(elements: any[], intervalMs = 120) {
      let i = 0;
      const tick = () => {
        if (i < elements.length) {
          i++;
          _ontoolinputpartial?.({ elements: JSON.stringify(elements.slice(0, i)) });
          setTimeout(tick, intervalMs);
        } else {
          // Finalize
          _ontoolinput?.({ elements: JSON.stringify(elements) });
        }
      };
      tick();
    },
  };
}

```

### File: src\edit-context.ts
```ts
import type { App } from "@modelcontextprotocol/ext-apps";

const DEBOUNCE_MS = 2000;
let timer: ReturnType<typeof setTimeout> | null = null;
let initialSnapshot: string | null = null;
let initialElementsById: Map<string, any> = new Map();
let storageKey: string | null = null;
let checkpointId: string | null = null;

/**
 * Set the localStorage key for this widget instance (use viewUUID or tool-call-derived ID).
 */
export function setStorageKey(key: string) {
  storageKey = `excalidraw:${key}`;
}

/**
 * Set the checkpoint key for saving state snapshots.
 * Called when ontoolresult delivers the checkpointId from the server.
 */
export function setCheckpointId(id: string) {
  checkpointId = id;
}

/**
 * Call once after final render to capture the baseline element state.
 */
export function captureInitialElements(elements: readonly any[]) {
  initialSnapshot = JSON.stringify(elements.map((el: any) => el.id + ":" + (el.version ?? 0)));
  initialElementsById = new Map(elements.map((el: any) => [el.id, el]));
}

/** Compute a compact diff between initial and current elements. */
function computeDiff(current: any[]): string {
  const added: string[] = [];
  const removed: string[] = [];
  const moved: string[] = [];
  const currentIds = new Set<string>();

  for (const el of current) {
    currentIds.add(el.id);
    const orig = initialElementsById.get(el.id);
    if (!orig) {
      // New element — include type, position, and text if any
      const desc = `${el.type} "${el.text ?? el.label?.text ?? ""}" at (${Math.round(el.x)},${Math.round(el.y)})`;
      added.push(desc);
    } else if (Math.round(orig.x) !== Math.round(el.x) || Math.round(orig.y) !== Math.round(el.y) ||
               Math.round(orig.width) !== Math.round(el.width) || Math.round(orig.height) !== Math.round(el.height)) {
      moved.push(`${el.id} → (${Math.round(el.x)},${Math.round(el.y)}) ${Math.round(el.width)}x${Math.round(el.height)}`);
    }
  }

  for (const id of initialElementsById.keys()) {
    if (!currentIds.has(id)) removed.push(id);
  }

  const parts: string[] = [];
  if (added.length) parts.push(`Added: ${added.join("; ")}`);
  if (removed.length) parts.push(`Removed: ${removed.join(", ")}`);
  if (moved.length) parts.push(`Moved/resized: ${moved.join("; ")}`);
  if (!parts.length) return "";
  const cpRef = checkpointId ? ` (checkpoint: ${checkpointId})` : "";
  return `User edited diagram${cpRef}. ${parts.join(". ")}`;
}

/**
 * Load persisted elements from localStorage (if any).
 */
export function loadPersistedElements(): any[] | null {
  if (!storageKey) return null;
  try {
    const stored = localStorage.getItem(storageKey);
    if (!stored) return null;
    return JSON.parse(stored);
  } catch {
    return null;
  }
}

/** Latest edited elements (kept in sync without triggering React re-renders). */
let latestEditedElements: any[] | null = null;

/**
 * Get the latest user-edited elements (or null if no edits were made).
 * Call this when exiting fullscreen to sync edits back to React state.
 */
export function getLatestEditedElements(): any[] | null {
  return latestEditedElements;
}

/**
 * Excalidraw onChange handler. Persists to localStorage and sends updated
 * elements JSON to model context — only when user actually changed something
 * (debounced). Does NOT call setState to avoid infinite re-render loops.
 */
export function onEditorChange(app: App, elements: readonly any[]) {
  const currentSnapshot = JSON.stringify(elements.map((el: any) => el.id + ":" + (el.version ?? 0)));
  if (currentSnapshot === initialSnapshot) return;

  const live = [...elements].filter((el: any) => !el.isDeleted);
  latestEditedElements = live;

  if (timer) clearTimeout(timer);
  timer = setTimeout(() => {
    if (storageKey) {
      try {
        localStorage.setItem(storageKey, JSON.stringify(live));
      } catch {}
    }
    if (checkpointId) {
      app.callServerTool({
        name: "save_checkpoint",
        arguments: { id: checkpointId, data: JSON.stringify({ elements: live }) },
      }).catch(() => {});
    }
    const diff = computeDiff(live);
    if (diff) {
      app.updateModelContext({
        content: [{ type: "text", text: diff }],
      }).catch(() => {});
    }
  }, DEBOUNCE_MS);
}

```

### File: src\global.css
```css
/* Load Excalidraw component CSS from CDN (avoids inlining ~200KB) */
@import url("https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/index.css");

/* Load Excalidraw's hand-drawn font from CDN (Excalifont = v0.18 default) */
@font-face {
  font-family: "Excalifont";
  src: url("https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/fonts/Excalifont/Excalifont-Regular-a88b72a24fb54c9f94e3b5fdaa7481c9.woff2") format("woff2");
  font-display: swap;
}

/* Preload Excalidraw UI fonts so they're cached before fullscreen mount.
   Without this, Excalidraw loads them on component init, triggering a font
   recalculation pass that corrupts text dimensions on first open. */
@font-face {
  font-family: "Assistant";
  src: url("https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/fonts/Assistant/Assistant-Regular.woff2") format("woff2");
  font-weight: 400;
  font-display: swap;
}
@font-face {
  font-family: "Assistant";
  src: url("https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/fonts/Assistant/Assistant-Medium.woff2") format("woff2");
  font-weight: 500;
  font-display: swap;
}
@font-face {
  font-family: "Assistant";
  src: url("https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/fonts/Assistant/Assistant-Bold.woff2") format("woff2");
  font-weight: 700;
  font-display: swap;
}

*, *::before, *::after {
  box-sizing: border-box;
}

html, body, #root {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 1rem;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

/* Light theme (default) */
:root {
  --text-color: #1a1a1a;
  --text-muted: #666666;
  --border-color: #e5e5e5;
  --bg-color: #ffffff;
}

/* Dark theme */
@media (prefers-color-scheme: dark) {
  :root {
    --text-color: #e5e5e5;
    --text-muted: #a0a0a0;
    --border-color: #444444;
    --bg-color: #1a1a1a;
  }
}

body {
  background: transparent;
  color: var(--text-color);
}

.main {
  outline: none;
  position: relative;
}

/* Fullscreen mode. Mobile safe-area insets are applied via Excalidraw's native
   --sat/--sar/--sab/--sal vars (set from hostContext.safeAreaInsets in JS),
   which offset only the floating toolbar/menus — canvas stays full-bleed. */
.main.fullscreen {
  position: fixed;
  inset: 0;
  background: var(--bg-color, #ffffff);
  z-index: 9999;
}

.main.fullscreen .excalidraw-container {
  height: 100%;
}

/* Hide library button in fullscreen editor */
.main.fullscreen .default-sidebar-trigger {
  display: none !important;
}

/* Mobile: export button moves below the toolbar row (narrow viewports can't
   fit it in top-right alongside lock/hand icons). */
.mobile-share-slot {
  position: absolute;
  top: calc(var(--sat, 0px) + 64px);
  right: calc(var(--sar, 0px) + 12px);
  z-index: 5;
}

/* Contain SVG inside fullscreen viewport (not cover) */
.main.fullscreen .svg-wrapper svg {
  max-height: 100%;
}

/* Toolbar - appears on hover */
.toolbar {
  display: flex;
  gap: 1rem;
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 100;
  opacity: 0;
  transition: opacity 0.2s ease;
}

.main:hover .toolbar {
  opacity: 1;
}

/* Fullscreen button */
.app-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  height: 28px;
  color: rgba(0, 0, 0, 0.95);
  padding: 2px 8px;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.15s ease;
  pointer-events: auto;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.app-button:hover {
  color: rgba(0, 0, 0, 0.7);
  background: rgba(255, 255, 255, 0.8);
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.12);
}

.excalidraw-container {
  width: 100%;
  position: relative;
  overflow: hidden;
}

/* SVGLayer is for export only, not rendering — hide to save space */
.excalidraw-container .excalidraw .SVGLayer {
  display: none !important;
}

/* Hide Excalidraw UI chrome in view mode */
.excalidraw-container .excalidraw .App-menu,
.excalidraw-container .excalidraw .App-toolbar,
.excalidraw-container .excalidraw .layer-ui__wrapper__footer,
.excalidraw-container .excalidraw .App-menu_top,
.excalidraw-container .excalidraw .undo-redo-buttons,
.excalidraw-container .excalidraw .HelpButton,
.excalidraw-container .excalidraw .UserList,
.excalidraw-container .excalidraw .main-menu-trigger,
.excalidraw-container .excalidraw .welcome-screen-center,
.excalidraw-container .excalidraw .welcome-screen-menu-hintContainer,
.excalidraw-container .excalidraw .layer-ui__wrapper__footer-right {
  display: none !important;
}

.excalidraw-container .excalidraw .App-menu_top__left {
  visibility: hidden !important;
}


.loading-state {
  padding: 2rem 1rem;
  text-align: center;
}

.loading-text {
  font-size: 1rem;
  color: var(--text-muted);
}

/* SVG wrapper */
.svg-wrapper {
  width: 100%;
}

.svg-wrapper > svg {
  background: #ffffff;
}

/* Fade-in animation for new SVG elements (opacity only, no transform) */
.excalidraw-container svg :where(g, rect, circle, ellipse, text, image) {
  animation: svgFadeIn 0.5s ease-out;
}

@keyframes svgFadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Stroke draw-on animation for line elements */
.excalidraw-container svg :where(path, line, polyline, polygon) {
  animation: strokeDraw 0.6s ease-out forwards;
}

@keyframes strokeDraw {
  from {
    stroke-dasharray: 1000;
    stroke-dashoffset: 1000;
  }
  to {
    stroke-dashoffset: 0;
  }
}

/* Smooth transitions for property changes on existing elements */
.excalidraw-container svg :where(rect, circle, ellipse, path, line, polyline, polygon, text, g) {
  transition: fill 0.4s ease-out, stroke 0.4s ease-out, opacity 0.4s ease-out;
}

/* Chart container */
.chart-container {
  height: 400px;
  width: 100%;
}

.chart-title {
  margin: 12px 16px 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-color);
}

.tooltip {
  background: var(--bg-color, #fff);
  border: 1px solid var(--border-color);
  border-radius: 4px;
  padding: 8px 12px;
  font-size: 12px;
  color: var(--text-color);
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* HTML iframe container */
.html-container {
  width: 100%;
  height: 500px;
  border: none;
}

.main.fullscreen .html-container {
  height: 100%;
}

/* Export modal overlay */
.export-modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.export-modal {
  min-width: 320px;
  max-width: 400px;
  padding: 24px !important;
}

.export-modal-title {
  margin: 0 0 8px;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--text-primary-color, #1a1a1a);
}

.export-modal-text {
  margin: 0 0 20px;
  font-size: 0.875rem;
  color: var(--color-gray-60, #666);
  line-height: 1.4;
}

.export-modal-actions {
  display: flex;
  gap: 8px;
  justify-content: flex-end;
}

.export-modal-actions .standalone {
  padding: 8px 16px !important;
  width: auto !important;
  height: auto !important;
  font-size: 0.875rem;
}

.export-modal-confirm {
  --button-bg: var(--color-primary, #6965db) !important;
  --button-color: #fff !important;
  --button-border: var(--color-primary, #6965db) !important;
  --button-hover-bg: var(--color-primary-darker, #5b57d1) !important;
  --button-hover-border: var(--color-primary-darker, #5b57d1) !important;
  --button-hover-color: #fff !important;
}

.loading {
  padding: 1rem;
  color: var(--text-muted);
}

.error {
  padding: 1rem;
  color: #dc2626;
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

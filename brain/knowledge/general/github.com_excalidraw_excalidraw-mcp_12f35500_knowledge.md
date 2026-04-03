---
id: github.com-excalidraw-excalidraw-mcp-12f35500-know
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:46.675287
---

# KNOWLEDGE EXTRACT: github.com_excalidraw_excalidraw-mcp_12f35500
> **Extracted on:** 2026-04-01 11:11:51
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521304/github.com_excalidraw_excalidraw-mcp_12f35500

---

## File: `.gitignore`
```
node_modules/
dist/
.DS_Store
*.mcpb
.vercel
bun.lock
.vscode
opencode.json
```

## File: `.mcpbignore`
```
node_modules/
src/
*.ts
!*.d.ts
/mcp-app.html
tsconfig.json
tsconfig.server.json
vite.config.ts
CLAUDE.md
.git/
.gitignore
*.mcpb
```

## File: `.npmrc`
```
node-linker=hoisted
```

## File: `CLAUDE.md`
```markdown
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

## File: `README.md`
```markdown
# Excalidraw MCP App Server

MCP server that streams hand-drawn Excalidraw diagrams with smooth viewport camera control and interactive fullscreen editing.

![Demo](brain/knowledge/docs_legacy/demo.gif)

## Install

Works with any client that supports [MCP Apps](https://modelcontextprotocol.io/brain/knowledge/docs_legacy/extensions/apps) — Claude, ChatGPT, VS Code, Goose, and others. If something doesn't work, please [open an issue](https://github.com/antonpk1/excalidraw-mcp-app/issues).

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

- **Getting started for humans**: [documentation](https://modelcontextprotocol.io/brain/knowledge/docs_legacy/extensions/apps)
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

## File: `index-dev.html`
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

## File: `manifest.json`
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
  "icon": "brain/knowledge/docs_legacy/logo.png",
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

## File: `package.json`
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

## File: `tsconfig.json`
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

## File: `tsconfig.server.json`
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

## File: `vercel.json`
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

## File: `vite.config.dev.ts`
```typescript
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

## File: `vite.config.ts`
```typescript
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

## File: `api/mcp.ts`
```typescript
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

## File: `scripts/build.mjs`
```
#!/usr/bin/env node
import { execSync } from "child_process";
import { renameSync, rmSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, "..");

function run(cmd, env = {}) {
  console.log(`> ${cmd}`);
  execSync(cmd, {
    cwd: root,
    stdio: "inherit",
    env: { ...process.env, ...env },
  });
}

rmSync(join(root, "dist"), { recursive: true, force: true });

// 1. Type-check
run("tsc --noEmit");

// 2. Vite build (singlefile HTML)
run("vite build");

// 3. Move the HTML output to dist root (cross-platform)
renameSync(
  join(root, "dist", "src", "mcp-app.html"),
  join(root, "dist", "mcp-app.html"),
);
rmSync(join(root, "dist", "src"), { recursive: true, force: true });

// 4. Build server types
run("tsc -p tsconfig.server.json");

// 5. Bundle server + index
run('bun build "src/server.ts" --outdir dist --target node');
run(
  'bun build "src/main.ts" --outfile "dist/index.js" --target node --banner "#!/usr/bin/env node"',
);
```

## File: `scripts/setup-bun.mjs`
```
#!/usr/bin/env node
// Immediate log to verify script execution
console.log("[setup-bun] Script loaded");

/**
 * Postinstall script to set up bun from platform-specific optional dependencies.
 * Handles Windows ARM64 by downloading x64-baseline via emulation.
 */
import {
  existsSync,
  mkdirSync,
  symlinkSync,
  unlinkSync,
  copyFileSync,
  chmodSync,
  writeFileSync,
} from "fs";
import { join, dirname } from "path";
import { spawnSync } from "child_process";
import { fileURLToPath } from "url";
import { get } from "https";
import { createGunzip } from "zlib";

const __dirname = dirname(fileURLToPath(import.meta.url));
const projectRoot = join(__dirname, "..");
const nodeModules = join(projectRoot, "node_modules");
const binDir = join(nodeModules, ".bin");

const os = process.platform;
const arch = process.arch;
const isWindows = os === "win32";
const bunExe = isWindows ? "bun.exe" : "bun";

// Detect libc type on Linux (glibc vs musl)
function detectLibc() {
  if (os !== "linux") return null;

  // Check for musl-specific loader
  const muslLoaders = [
    `/lib/ld-musl-${arch === "arm64" ? "aarch64" : "x86_64"}.so.1`,
    "/lib/ld-musl-x86_64.so.1",
    "/lib/ld-musl-aarch64.so.1",
  ];

  for (const loader of muslLoaders) {
    if (existsSync(loader)) {
      console.log(`  Detected musl libc (found ${loader})`);
      return "musl";
    }
  }

  // Default to glibc on Linux
  console.log("  Detected glibc (no musl loader found)");
  return "glibc";
}

// Platform to package mapping (matches @oven/bun-* package names)
// For Linux, separate glibc and musl packages
const platformPackages = {
  darwin: {
    arm64: ["bun-darwin-aarch64"],
    x64: ["bun-darwin-x64", "bun-darwin-x64-baseline"],
  },
  linux: {
    arm64: {
      glibc: ["bun-linux-aarch64"],
      musl: ["bun-linux-aarch64-musl"],
    },
    x64: {
      glibc: ["bun-linux-x64", "bun-linux-x64-baseline"],
      musl: ["bun-linux-x64-musl", "bun-linux-x64-musl-baseline"],
    },
  },
  win32: {
    x64: ["bun-windows-x64", "bun-windows-x64-baseline"],
    arm64: ["bun-windows-x64-baseline"], // x64 runs via emulation on ARM64
  },
};

function findBunBinary() {
  let packages = platformPackages[os]?.[arch];

  // For Linux, select packages based on libc type
  if (os === "linux" && packages && typeof packages === "object") {
    const libc = detectLibc();
    packages = packages[libc] || [];
  }

  packages = packages || [];
  console.log(
    `Looking for bun packages: ${packages.join(", ") || "(none for this platform)"}`,
  );

  for (const pkg of packages) {
    const binPath = join(nodeModules, "@oven", pkg, "bin", bunExe);
    console.log(`  Checking: ${binPath}`);
    if (existsSync(binPath)) {
      console.log(`  Found bun at: ${binPath}`);
      return binPath;
    } else {
      console.log(`  Not found`);
    }
  }

  return null;
}

async function downloadBunForWindowsArm64() {
  // Windows ARM64 can run x64 binaries via emulation
  const pkg = "bun-windows-x64-baseline";
  const version = "1.2.21";
  const url = `https://registry.npmjs.org/@oven/${pkg}/-/${pkg}-${version}.tgz`;
  const destDir = join(nodeModules, "@oven", pkg);

  console.log(`Downloading ${pkg} for Windows ARM64 emulation...`);

  return new Promise((resolve, reject) => {
    get(url, (response) => {
      if (response.statusCode === 302 || response.statusCode === 301) {
        get(response.headers.location, handleResponse).on("error", reject);
      } else {
        handleResponse(response);
      }

      function handleResponse(res) {
        if (res.statusCode !== 200) {
          reject(new Error(`Failed to download: ${res.statusCode}`));
          return;
        }

        const chunks = [];
        const gunzip = createGunzip();

        res.pipe(gunzip);

        gunzip.on("data", (chunk) => chunks.push(chunk));
        gunzip.on("end", () => {
          try {
            extractTar(Buffer.concat(chunks), destDir);
            const binPath = join(destDir, "bin", bunExe);
            if (existsSync(binPath)) {
              resolve(binPath);
            } else {
              reject(new Error("Binary not found after extraction"));
            }
          } catch (err) {
            reject(err);
          }
        });
        gunzip.on("error", reject);
      }
    }).on("error", reject);
  });
}

function extractTar(buffer, destDir) {
  // Simple tar extraction (512-byte blocks)
  let offset = 0;
  while (offset < buffer.length) {
    const name = buffer
      .toString("utf-8", offset, offset + 100)
      .replace(/\0.*$/, "")
      .replace("package/", "");
    const size = parseInt(
      buffer.toString("utf-8", offset + 124, offset + 136).trim(),
      8,
    );

    offset += 512;

    if (!isNaN(size) && size > 0 && name) {
      const filePath = join(destDir, name);
      const fileDir = dirname(filePath);
      if (!existsSync(fileDir)) {
        mkdirSync(fileDir, { recursive: true });
      }
      const content = buffer.subarray(offset, offset + size);
      writeFileSync(filePath, content);

      // Make executable
      if (name.endsWith(bunExe) || name === "bin/bun") {
        try {
          chmodSync(filePath, 0o755);
        } catch {}
      }

      offset += Math.ceil(size / 512) * 512;
    }
  }
}

function setupBinLink(bunPath) {
  if (!existsSync(binDir)) {
    mkdirSync(binDir, { recursive: true });
  }

  const bunLink = join(binDir, bunExe);
  const bunxLink = join(binDir, isWindows ? "bunx.exe" : "bunx");

  // Remove existing links
  for (const link of [bunLink, bunxLink]) {
    try {
      unlinkSync(link);
    } catch {}
  }

  if (isWindows) {
    // On Windows, copy the binary (symlinks may not work without admin)
    copyFileSync(bunPath, bunLink);
    copyFileSync(bunPath, bunxLink);
  } else {
    // On Unix, use symlinks
    symlinkSync(bunPath, bunLink);
    symlinkSync(bunPath, bunxLink);
  }

  console.log(`Bun linked to: ${bunLink}`);
}

// Force immediate output
process.stdout.write("[setup-bun] Script starting...\n");

async function main() {
  process.stdout.write(`[setup-bun] Setting up bun for ${os} ${arch}...\n`);
  process.stdout.write(`[setup-bun] Project root: ${projectRoot}\n`);
  process.stdout.write(`[setup-bun] Node modules: ${nodeModules}\n`);

  let bunPath = findBunBinary();

  if (!bunPath && os === "win32" && arch === "arm64") {
    try {
      bunPath = await downloadBunForWindowsArm64();
    } catch (err) {
      console.error("Failed to download bun for Windows ARM64:", err.message);
    }
  }

  if (!bunPath) {
    console.log("No bun binary found in optional dependencies.");
    console.log("Bun will need to be installed separately.");
    console.log("See: https://bun.sh/brain/knowledge/docs_legacy/installation");
    process.exit(0); // Don't fail the install
  }

  try {
    setupBinLink(bunPath);

    // Verify installation
    const result = spawnSync(bunPath, ["--version"], { encoding: "utf-8" });
    if (result.status === 0) {
      console.log(`Bun ${result.stdout.trim()} installed successfully!`);
    }
  } catch (err) {
    console.error("Failed to set up bun:", err.message);
    process.exit(0); // Don't fail the install
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(0); // Don't fail the install
});
```

## File: `src/checkpoint-store.ts`
```typescript
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

## File: `src/dev-mock.ts`
```typescript
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

## File: `src/dev.tsx`
```tsx
/**
 * Dev entry point — renders ExcalidrawAppCore with a mock MCP App.
 *
 * Usage: pnpm dev:ui → opens browser with the widget + sample diagram.
 * Click fullscreen button to test the Excalidraw editor.
 *
 * Future: add a control panel to stream elements, test checkpoints, etc.
 */
import { createRoot } from "react-dom/client";
import { useEffect, useMemo, useRef } from "react";
import { ExcalidrawAppCore } from "./mcp-app";
import { createMockApp, type MockAppControls } from "./dev-mock";
import "./global.css";

// ── Sample elements (skeleton format with labels, same as LLM output) ────

// @prettier-ignore
// @oxc-ignore
const SAMPLE_ELEMENTS = [
  {
    type: "rectangle",
    id: "client",
    x: 60,
    y: 120,
    width: 180,
    height: 80,
    roundness: { type: 3 },
    backgroundColor: "#a5d8ff",
    fillStyle: "solid",
    strokeColor: "#1e1e1e",
    label: { text: "Client App", fontSize: 20 },
  },
  {
    type: "rectangle",
    id: "server",
    x: 400,
    y: 120,
    width: 180,
    height: 80,
    roundness: { type: 3 },
    backgroundColor: "#b2f2bb",
    fillStyle: "solid",
    strokeColor: "#1e1e1e",
    label: { text: "MCP Server", fontSize: 20 },
  },
  {
    type: "rectangle",
    id: "db",
    x: 400,
    y: 320,
    width: 180,
    height: 80,
    roundness: { type: 3 },
    backgroundColor: "#d0bfff",
    fillStyle: "solid",
    strokeColor: "#1e1e1e",
    label: { text: "Database", fontSize: 20 },
  },
  {
    type: "arrow",
    id: "a1",
    x: 240,
    y: 160,
    width: 160,
    height: 0,
    points: [
      [0, 0],
      [160, 0],
    ],
    strokeColor: "#1e1e1e",
    strokeWidth: 2,
    endArrowhead: "arrow",
    label: { text: "request", fontSize: 14 },
  },
  {
    type: "arrow",
    id: "a2",
    x: 490,
    y: 200,
    width: 0,
    height: 120,
    points: [
      [0, 0],
      [0, 120],
    ],
    strokeColor: "#1e1e1e",
    strokeWidth: 2,
    endArrowhead: "arrow",
    label: { text: "query", fontSize: 14 },
  },
];

// ── Dev control panel ────────────────────────────────────────────────────

function DevControls({ mock }: { mock: MockAppControls }) {
  return (
    <div
      style={{
        position: "fixed",
        bottom: 12,
        right: 12,
        zIndex: 10000,
        display: "flex",
        gap: 6,
        padding: "8px 10px",
        background: "rgba(0,0,0,0.75)",
        borderRadius: 8,
        fontFamily: "system-ui",
        fontSize: 12,
        color: "#fff",
      }}
    >
      <button
        onClick={() => mock.sendToolInput(SAMPLE_ELEMENTS)}
        style={btnStyle}
      >
        Load (instant)
      </button>
      <button
        onClick={() => mock.streamElements(SAMPLE_ELEMENTS, 300)}
        style={btnStyle}
      >
        Stream
      </button>
      <button onClick={() => mock.sendToolResult("dev-cp-1")} style={btnStyle}>
        Send Result
      </button>
    </div>
  );
}

const btnStyle: React.CSSProperties = {
  background: "rgba(255,255,255,0.15)",
  border: "1px solid rgba(255,255,255,0.25)",
  borderRadius: 5,
  padding: "4px 10px",
  color: "#fff",
  cursor: "pointer",
  fontSize: 12,
};

// ── App ──────────────────────────────────────────────────────────────────

function DevApp() {
  const mock = useMemo(() => createMockApp(), []);
  const initialized = useRef(false);

  // Wait one frame for ExcalidrawAppCore's useEffect to attach handlers,
  // then fire initial tool input with sample data.
  useEffect(() => {
    if (initialized.current) return;
    initialized.current = true;
    // Use requestAnimationFrame to ensure handlers are attached
    requestAnimationFrame(() => {
      mock.sendToolInput(SAMPLE_ELEMENTS);
      mock.sendToolResult("dev-checkpoint");
    });
  }, [mock]);

  return (
    <>
      <ExcalidrawAppCore app={mock.app} />
      <DevControls mock={mock} />
    </>
  );
}

createRoot(document.body).render(<DevApp />);
```

## File: `src/edit-context.ts`
```typescript
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

## File: `src/global.css`
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

## File: `src/main.ts`
```typescript
/**
 * Entry point for running the MCP server.
 * Run with: npx @mcp-demos/excalidraw-server
 * Or: node dist/index.js [--stdio]
 */

import { createMcpExpressApp } from "@modelcontextprotocol/sdk/server/express.js";
import type { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import cors from "cors";
import type { Request, Response } from "express";
import { FileCheckpointStore } from "./checkpoint-store.js";
import { createServer } from "./server.js";

/**
 * Starts an MCP server with Streamable HTTP transport in stateless mode.
 *
 * @param createServer - Factory function that creates a new McpServer instance per request.
 */
export async function startStreamableHTTPServer(
  createServer: () => McpServer,
): Promise<void> {
  const port = parseInt(process.env.PORT ?? "3001", 10);

  const app = createMcpExpressApp({ host: "0.0.0.0" });
  app.use(cors());

  app.all("/mcp", async (req: Request, res: Response) => {
    const server = createServer();
    const transport = new StreamableHTTPServerTransport({
      sessionIdGenerator: undefined,
    });

    res.on("close", () => {
      transport.close().catch(() => {});
      server.close().catch(() => {});
    });

    try {
      await server.connect(transport);
      await transport.handleRequest(req, res, req.body);
    } catch (error) {
      console.error("MCP error:", error);
      if (!res.headersSent) {
        res.status(500).json({
          jsonrpc: "2.0",
          error: { code: -32603, message: "Internal server error" },
          id: null,
        });
      }
    }
  });

  const httpServer = app.listen(port, (err) => {
    if (err) {
      console.error("Failed to start server:", err);
      process.exit(1);
    }
    console.log(`MCP server listening on http://localhost:${port}/mcp`);
  });

  const shutdown = () => {
    console.log("\nShutting down...");
    httpServer.close(() => process.exit(0));
  };

  process.on("SIGINT", shutdown);
  process.on("SIGTERM", shutdown);
}

/**
 * Starts an MCP server with stdio transport.
 *
 * @param createServer - Factory function that creates a new McpServer instance.
 */
export async function startStdioServer(
  createServer: () => McpServer,
): Promise<void> {
  await createServer().connect(new StdioServerTransport());
}

async function main() {
  const store = new FileCheckpointStore();
  const factory = () => createServer(store);
  if (process.argv.includes("--stdio")) {
    await startStdioServer(factory);
  } else {
    await startStreamableHTTPServer(factory);
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
```

## File: `src/mcp-app.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="color-scheme" content="light dark">
  <title>Excalidraw App</title>
  <script type="importmap">
  {
    "imports": {
      "react": "https://esm.sh/react@19.0.0",
      "react-dom": "https://esm.sh/react-dom@19.0.0?deps=react@19.0.0",
      "react-dom/client": "https://esm.sh/react-dom@19.0.0/client?deps=react@19.0.0",
      "react/jsx-runtime": "https://esm.sh/react@19.0.0/jsx-runtime",
      "@excalidraw/excalidraw": "https://esm.sh/@excalidraw/excalidraw@0.18.0?deps=react@19.0.0,react-dom@19.0.0",
      "morphdom": "https://esm.sh/morphdom@2.7.8"
    }
  }
  </script>
  <link rel="stylesheet" href="/src/global.css">
</head>
<body>
  <script type="module" src="/src/mcp-entry.tsx"></script>
</body>
</html>
```

## File: `src/mcp-app.tsx`
```tsx
import { useApp } from "@modelcontextprotocol/ext-apps/react";
import type { App } from "@modelcontextprotocol/ext-apps";
import {  Excalidraw, exportToSvg, convertToExcalidrawElements, restore, CaptureUpdateAction, FONT_FAMILY, serializeAsJSON, MainMenu } from "@excalidraw/excalidraw";
import morphdom from "morphdom";
import { useCallback, useEffect, useRef, useState } from "react";
import { initPencilAudio, playStroke } from "./pencil-audio";
import { captureInitialElements, onEditorChange, setStorageKey, loadPersistedElements, getLatestEditedElements, setCheckpointId } from "./edit-context";
import "./global.css";

// ============================================================
// Debug logging (routes through SDK → host log file)
// ============================================================

let _logFn: ((msg: string) => void) | null = null;
function fsLog(msg: string) {
  if (_logFn) _logFn(msg);
}

// ============================================================
// Shared helpers
// ============================================================

function parsePartialElements(str: string | undefined): any[] {
  if (!str?.trim().startsWith("[")) return [];
  try { return JSON.parse(str); } catch { /* partial */ }
  const last = str.lastIndexOf("}");
  if (last < 0) return [];
  try { return JSON.parse(str.substring(0, last + 1) + "]"); } catch { /* incomplete */ }
  return [];
}

function excludeIncompleteLastItem<T>(arr: T[]): T[] {
  if (!arr || arr.length === 0) return [];
  if (arr.length <= 1) return [];
  return arr.slice(0, -1);
}

interface ViewportRect {
  x: number;
  y: number;
  width: number;
  height: number;
}

/** Convert raw shorthand elements → Excalidraw format (labels → bound text, font fix).
 *  Preserves pseudo-elements like cameraUpdate (not valid Excalidraw types). */
function convertRawElements(els: any[]): any[] {
  const pseudoTypes = new Set(["cameraUpdate", "delete", "restoreCheckpoint"]);
  const pseudos = els.filter((el: any) => pseudoTypes.has(el.type));
  const real = els.filter((el: any) => !pseudoTypes.has(el.type));
  const withDefaults = real.map((el: any) =>
    el.label ? { ...el, label: { textAlign: "center", verticalAlign: "middle", ...el.label } } : el
  );
  const converted = convertToExcalidrawElements(withDefaults, { regenerateIds: false })
    .map((el: any) => el.type === "text" ? { ...el, fontFamily: (FONT_FAMILY as any).Excalifont ?? 1 } : el);
  return [...converted, ...pseudos];
}

/** Fix SVG viewBox to 4:3 by expanding the smaller dimension and centering. */
function fixViewBox4x3(svg: SVGSVGElement): void {
  const vb = svg.getAttribute("viewBox")?.split(" ").map(Number);
  if (!vb || vb.length !== 4) return;
  const [vx, vy, vw, vh] = vb;
  const r = vw / vh;
  if (Math.abs(r - 4 / 3) < 0.01) return;
  if (r > 4 / 3) {
    const h2 = Math.round(vw * 3 / 4);
    svg.setAttribute("viewBox", `${vx} ${vy - Math.round((h2 - vh) / 2)} ${vw} ${h2}`);
  } else {
    const w2 = Math.round(vh * 4 / 3);
    svg.setAttribute("viewBox", `${vx - Math.round((w2 - vw) / 2)} ${vy} ${w2} ${vh}`);
  }
}

function extractViewportAndElements(elements: any[]): {
  viewport: ViewportRect | null;
  drawElements: any[];
  restoreId: string | null;
  deleteIds: Set<string>;
} {
  let viewport: ViewportRect | null = null;
  let restoreId: string | null = null;
  const deleteIds = new Set<string>();
  const drawElements: any[] = [];

  for (const el of elements) {
    if (el.type === "cameraUpdate") {
      viewport = { x: el.x, y: el.y, width: el.width, height: el.height };
    } else if (el.type === "restoreCheckpoint") {
      restoreId = el.id;
    } else if (el.type === "delete") {
      for (const id of String(el.ids ?? el.id).split(",")) deleteIds.add(id.trim());
    } else {
      drawElements.push(el);
    }
  }

  // Hide deleted elements via near-zero opacity instead of removing — preserves SVG
  // group count/order so morphdom matches by position correctly (no cascade re-animations).
  // Using 1 (not 0) because Excalidraw treats opacity:0 as "unset" → defaults to 100.
  const processedDraw = deleteIds.size > 0
    ? drawElements.map((el: any) => (deleteIds.has(el.id) || deleteIds.has(el.containerId)) ? { ...el, opacity: 1 } : el)
    : drawElements;

  return { viewport, drawElements: processedDraw, restoreId, deleteIds };
}

const ExpandIcon = () => (
  <svg width="14" height="14" viewBox="0 0 14 14" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
    <path d="M8.5 1.5H12.5V5.5" />
    <path d="M5.5 12.5H1.5V8.5" />
    <path d="M12.5 1.5L8 6" />
    <path d="M1.5 12.5L6 8" />
  </svg>
);

const ExternalLinkIcon = () => (
  <svg width="14" height="14" viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.25" strokeLinecap="round" strokeLinejoin="round">
    <path d="M12 8.667V12.667C12 13.035 11.702 13.333 11.333 13.333H3.333C2.965 13.333 2.667 13.035 2.667 12.667V4.667C2.667 4.298 2.965 4 3.333 4H7.333" />
    <path d="M10 2.667H13.333V6" />
    <path d="M6.667 9.333L13.333 2.667" />
  </svg>
);

async function shareToExcalidraw(data: {elements: any[], appState: any, files: any}, app: App) {
  try {
    if (!data.elements?.length) return;

    // Serialize to Excalidraw JSON
    const json = serializeAsJSON(data.elements, data.appState, data.files, "database");

    // Proxy through server tool (avoids CORS on json.excalidraw.com)
    const result = await app.callServerTool({
      name: "export_to_excalidraw",
      arguments: { json },
    });

    if (result.isError) {
      fsLog(`export failed: ${JSON.stringify(result.content)}`);
      return;
    }

    const url = (result.content[0] as any).text;
    await app.openLink({ url });
  } catch (err) {
    fsLog(`shareToExcalidraw error: ${err}`);
  }
}

function ShareButton({ onConfirm, compact }: { onConfirm: () => Promise<void>; compact?: boolean }) {
  const [state, setState] = useState<"idle" | "confirm" | "uploading">("idle");

  const handleConfirm = async () => {
    setState("uploading");
    try {
      await onConfirm();
    } finally {
      setState("idle");
    }
  };

  return (
    <>
      <button
        className=" app-button"
        style={{ display: "flex", alignItems: "center", gap: 5, width: "auto", padding: "0 10px", marginRight: compact ? 0 : -8 }}
        title="Export to Excalidraw"
        disabled={state === "uploading"}
        onClick={() => setState("confirm")}
      >
        <ExternalLinkIcon />
        {!compact && <span style={{ fontSize: "0.75rem", fontWeight: 400 }}>{state === "uploading" ? "Exporting…" : "Open in Excalidraw"}</span>}
      </button>

      {state === "confirm" && (
        <div className="excalidraw export-modal-overlay" onClick={() => setState("idle")}>
          <div className="Island export-modal" onClick={(e) => e.stopPropagation()}>
            <h3 className="export-modal-title">Export to Excalidraw</h3>
            <p className="export-modal-text">
              This will upload your diagram to excalidraw.com and open it in a new tab.
            </p>
            <div className="export-modal-actions">
              <button className="standalone" onClick={() => setState("idle")}>
                Cancel
              </button>
              <button className="standalone export-modal-confirm" onClick={handleConfirm}>
                Open in Excalidraw
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

// ============================================================
// Diagram component (Excalidraw SVG)
// ============================================================

const LERP_SPEED = 0.03; // 0–1, higher = faster snap
const EXPORT_PADDING = 20;

/**
 * Compute the min x/y of all draw elements in scene coordinates.
 * This matches the offset Excalidraw's exportToSvg applies internally:
 *   SVG_x = scene_x - sceneMinX + exportPadding
 */
function computeSceneBounds(elements: any[]): { minX: number; minY: number } {
  let minX = Infinity;
  let minY = Infinity;
  for (const el of elements) {
    if (el.x != null) {
      minX = Math.min(minX, el.x);
      minY = Math.min(minY, el.y);
      // Arrow points are offsets from el.x/y
      if (el.points && Array.isArray(el.points)) {
        for (const pt of el.points) {
          minX = Math.min(minX, el.x + pt[0]);
          minY = Math.min(minY, el.y + pt[1]);
        }
      }
    }
  }
  return { minX: isFinite(minX) ? minX : 0, minY: isFinite(minY) ? minY : 0 };
}

/**
 * Convert a scene-space viewport rect to an SVG-space viewBox.
 */
function sceneToSvgViewBox(
  vp: ViewportRect,
  sceneMinX: number,
  sceneMinY: number,
): { x: number; y: number; w: number; h: number } {
  return {
    x: vp.x - sceneMinX + EXPORT_PADDING,
    y: vp.y - sceneMinY + EXPORT_PADDING,
    w: vp.width,
    h: vp.height,
  };
}

function DiagramView({ toolInput, isFinal, displayMode, onElements, editedElements, onViewport, loadCheckpoint }: { toolInput: any; isFinal: boolean; displayMode: string; onElements?: (els: any[]) => void; editedElements?: any[]; onViewport?: (vp: ViewportRect) => void; loadCheckpoint?: (id: string) => Promise<{ elements: any[] } | null> }) {
  const svgRef = useRef<HTMLDivElement | null>(null);
  const latestRef = useRef<any[]>([]);
  const restoredRef = useRef<{ id: string; elements: any[] } | null>(null);
  const [, setCount] = useState(0);

  // Init pencil audio on first mount
  useEffect(() => { initPencilAudio(); }, []);

  // Set container height: 4:3 in inline, full viewport in fullscreen
  useEffect(() => {
    if (!svgRef.current) return;
    if (displayMode === "fullscreen") {
      svgRef.current.style.height = "100%";
      return;
    }
    const observer = new ResizeObserver(([entry]) => {
      const w = entry.contentRect.width;
      if (w > 0 && svgRef.current) {
        svgRef.current.style.height = `${Math.round(w * 3 / 4)}px`;
      }
    });
    observer.observe(svgRef.current);
    return () => observer.disconnect();
  }, [displayMode]);

  // Font preloading — ensure Virgil is loaded before first export
  const fontsReady = useRef<Promise<void> | null>(null);
  const ensureFontsLoaded = useCallback(() => {
    if (!fontsReady.current) {
      fontsReady.current = document.fonts.load('20px Excalifont').then(() => {});
    }
    return fontsReady.current;
  }, []);

  // Animated viewport in SCENE coordinates (stable across re-exports)
  const animatedVP = useRef<ViewportRect | null>(null);
  const targetVP = useRef<ViewportRect | null>(null);
  const sceneBoundsRef = useRef<{ minX: number; minY: number }>({ minX: 0, minY: 0 });
  const animFrameRef = useRef<number>(0);

  // User-controlled zoom during streaming (scale + pan offset in viewBox units)
  const zoomRef = useRef({ scale: 1, panX: 0, panY: 0 });
  const baseViewBoxRef = useRef<{ x: number; y: number; w: number; h: number } | null>(null);

  /** Apply user zoom on top of the stored base viewBox. */
  const applyZoom = useCallback(() => {
    if (!svgRef.current || !baseViewBoxRef.current) return;
    const svg = svgRef.current.querySelector("svg");
    if (!svg) return;
    const { x, y, w, h } = baseViewBoxRef.current;
    const { scale, panX, panY } = zoomRef.current;
    const zw = w / scale;
    const zh = h / scale;
    svg.setAttribute("viewBox", `${x + (w - zw) / 2 + panX} ${y + (h - zh) / 2 + panY} ${zw} ${zh}`);
  }, []);

  /** Apply current animated scene-space viewport to the SVG, then user zoom. */
  const applyViewBox = useCallback(() => {
    if (!animatedVP.current || !svgRef.current) return;
    const svg = svgRef.current.querySelector("svg");
    if (!svg) return;
    const { minX, minY } = sceneBoundsRef.current;
    const { x, y, width: w, height: h } = animatedVP.current;
    const ratio = w / h;
    const vp4x3: ViewportRect = Math.abs(ratio - 4 / 3) < 0.01 ? animatedVP.current
      : ratio > 4 / 3 ? { x, y, width: w, height: Math.round(w * 3 / 4) }
      : { x, y, width: Math.round(h * 4 / 3), height: h };
    const vb = sceneToSvgViewBox(vp4x3, minX, minY);
    baseViewBoxRef.current = { x: vb.x, y: vb.y, w: vb.w, h: vb.h };
    applyZoom();
  }, [applyZoom]);

  /** Lerp scene-space viewport toward target each frame. */
  const animateViewBox = useCallback(() => {
    if (!animatedVP.current || !targetVP.current) return;
    const a = animatedVP.current;
    const t = targetVP.current;
    a.x += (t.x - a.x) * LERP_SPEED;
    a.y += (t.y - a.y) * LERP_SPEED;
    a.width += (t.width - a.width) * LERP_SPEED;
    a.height += (t.height - a.height) * LERP_SPEED;
    applyViewBox();
    const delta = Math.abs(t.x - a.x) + Math.abs(t.y - a.y)
      + Math.abs(t.width - a.width) + Math.abs(t.height - a.height);
    if (delta > 0.5) {
      animFrameRef.current = requestAnimationFrame(animateViewBox);
    }
  }, [applyViewBox]);

  // Cleanup animation on unmount
  useEffect(() => {
    return () => { if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current); };
  }, []);

  const renderSvgPreview = useCallback(async (els: any[], viewport: ViewportRect | null, baseElements?: any[]) => {
    if ((els.length === 0 && !baseElements?.length) || !svgRef.current) return;
    try {
      // Wait for Virgil font to load before computing text metrics
      await ensureFontsLoaded();

      // Convert new elements (raw → Excalidraw format)
      const convertedNew = convertRawElements(els);
      const baseReal = baseElements?.filter((el: any) => el.type !== "cameraUpdate") ?? [];
      const excalidrawEls = [...baseReal, ...convertedNew];

      // Update scene bounds from all elements
      sceneBoundsRef.current = computeSceneBounds(excalidrawEls);

      const svg = await exportToSvg({
        elements: excalidrawEls as any,
        appState: { viewBackgroundColor: "transparent", exportBackground: false } as any,
        files: null,
        exportPadding: EXPORT_PADDING,
        skipInliningFonts: true,
      });
      if (!svgRef.current) return;

      let wrapper = svgRef.current.querySelector(".svg-wrapper") as HTMLDivElement | null;
      if (!wrapper) {
        wrapper = document.createElement("div");
        wrapper.className = "svg-wrapper";
        svgRef.current.appendChild(wrapper);
      }

      // Fill the container (height set by ResizeObserver to maintain 4:3)
      svg.style.width = "100%";
      svg.style.height = "100%";
      svg.removeAttribute("width");
      svg.removeAttribute("height");

      const existing = wrapper.querySelector("svg");
      if (existing) {
        morphdom(existing, svg, { childrenOnly: false });
      } else {
        wrapper.appendChild(svg);
      }

      // Always fix SVG viewBox to 4:3, then store as base for user zoom
      const renderedSvg = wrapper.querySelector("svg");
      if (renderedSvg) {
        fixViewBox4x3(renderedSvg as SVGSVGElement);
        const vbAttr = (renderedSvg as SVGSVGElement).getAttribute("viewBox")?.split(" ").map(Number);
        if (vbAttr && vbAttr.length === 4) {
          baseViewBoxRef.current = { x: vbAttr[0], y: vbAttr[1], w: vbAttr[2], h: vbAttr[3] };
        }
      }

      // Animate viewport in scene space, convert to SVG space at apply time
      if (viewport) {
        targetVP.current = { ...viewport };
        onViewport?.(viewport);
        if (!animatedVP.current) {
          // First viewport — snap immediately
          animatedVP.current = { ...viewport };
        }
        // Re-apply immediately after morphdom to prevent flicker
        applyViewBox();
        // Start/restart animation toward new target
        if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
        animFrameRef.current = requestAnimationFrame(animateViewBox);
      } else {
        // No explicit viewport — use default
        const defaultVP: ViewportRect = { x: 0, y: 0, width: 1024, height: 768 };
        onViewport?.(defaultVP);
        targetVP.current = defaultVP;
        if (!animatedVP.current) {
          animatedVP.current = { ...defaultVP };
        }
        applyViewBox();
        if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
        animFrameRef.current = requestAnimationFrame(animateViewBox);
        targetVP.current = null;
        if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
        // Apply user zoom on top of the fixed viewBox
        applyZoom();
      }
    } catch {
      // export can fail on partial/malformed elements
    }
  }, [applyViewBox, animateViewBox, applyZoom]);

  useEffect(() => {
    if (!toolInput) return;
    const raw = toolInput.elements;
    if (!raw) return;

    // Parse elements from string or array
    const str = typeof raw === "string" ? raw : JSON.stringify(raw);

    if (isFinal) {
      // Final input — parse complete JSON, render ALL elements
      const parsed = parsePartialElements(str);
      let { viewport, drawElements, restoreId, deleteIds } = extractViewportAndElements(parsed);

      // Load checkpoint base if restoring (async — from server)
      let base: any[] | undefined;
      const doFinal = async () => {
        if (restoreId && loadCheckpoint) {
          const saved = await loadCheckpoint(restoreId);
          if (saved) {
            base = saved.elements;
            // Extract camera from base as fallback
            if (!viewport) {
              const cam = base.find((el: any) => el.type === "cameraUpdate");
              if (cam) viewport = { x: cam.x, y: cam.y, width: cam.width, height: cam.height };
            }
            // Convert base with convertRawElements (handles both raw and already-converted)
            base = convertRawElements(base);
          }
          if (base && deleteIds.size > 0) {
            base = base.filter((el: any) => !deleteIds.has(el.id) && !deleteIds.has(el.containerId));
          }
        }

        latestRef.current = drawElements;
        // Convert new elements for fullscreen editor
        const convertedNew = convertRawElements(drawElements);

        // Merge base (converted) + new converted
        const allConverted = base ? [...base, ...convertedNew] : convertedNew;
        captureInitialElements(allConverted);
        // Only set elements if user hasn't edited yet (editedElements means user edits exist)
        if (!editedElements) onElements?.(allConverted);
        if (!editedElements) renderSvgPreview(drawElements, viewport, base);
      };
      doFinal();
      return;
    }

    // Partial input — drop last (potentially incomplete) element
    const parsed = parsePartialElements(str);

    // Extract restoreCheckpoint and delete before dropping last (they're small, won't be incomplete)
    let streamRestoreId: string | null = null;
    const streamDeleteIds = new Set<string>();
    for (const el of parsed) {
      if (el.type === "restoreCheckpoint") streamRestoreId = el.id;
      else if (el.type === "delete") {
        for (const id of String(el.ids ?? el.id).split(",")) streamDeleteIds.add(id.trim());
      }
    }

    const safe = excludeIncompleteLastItem(parsed);
    let { viewport, drawElements } = extractViewportAndElements(safe);

    const doStream = async () => {
      // Load checkpoint base (once per restoreId) — from server via callServerTool
      let base: any[] | undefined;
      if (streamRestoreId) {
        if (!restoredRef.current || restoredRef.current.id !== streamRestoreId) {
          if (loadCheckpoint) {
            const saved = await loadCheckpoint(streamRestoreId);
            if (saved) {
              const converted = convertRawElements(saved.elements);
              restoredRef.current = { id: streamRestoreId, elements: converted };
            }
          }
        }
        base = restoredRef.current?.elements;
        // Extract camera from base as fallback
        if (!viewport && base) {
          const cam = base.find((el: any) => el.type === "cameraUpdate");
          if (cam) viewport = { x: cam.x, y: cam.y, width: cam.width, height: cam.height };
        }
        if (base && streamDeleteIds.size > 0) {
          base = base.filter((el: any) => !streamDeleteIds.has(el.id) && !streamDeleteIds.has(el.containerId));
        }
      }

      if (drawElements.length > 0 && drawElements.length !== latestRef.current.length) {
        // Play pencil sound for each new element
        const prevCount = latestRef.current.length;
        for (let i = prevCount; i < drawElements.length; i++) {
          playStroke(drawElements[i].type ?? "rectangle");
        }
        latestRef.current = drawElements;
        setCount(drawElements.length);
        const jittered = drawElements.map((el: any) => ({ ...el, seed: Math.floor(Math.random() * 1e9) }));
        renderSvgPreview(jittered, viewport, base);
      } else if (base && base.length > 0 && latestRef.current.length === 0) {
        // First render: show restored base before new elements stream in
        renderSvgPreview([], viewport, base);
      }
    };
    doStream();
  }, [toolInput, isFinal, renderSvgPreview]);

  // Render already-converted elements directly (skip convertToExcalidrawElements)
  useEffect(() => {
    if (!editedElements || editedElements.length === 0 || !svgRef.current) return;
    (async () => {
      try {
        await ensureFontsLoaded();
        const svg = await exportToSvg({
          elements: editedElements as any,
          appState: { viewBackgroundColor: "transparent", exportBackground: false } as any,
          files: null,
          exportPadding: EXPORT_PADDING,
          skipInliningFonts: true,
        });
        if (!svgRef.current) return;
        let wrapper = svgRef.current.querySelector(".svg-wrapper") as HTMLDivElement | null;
        if (!wrapper) {
          wrapper = document.createElement("div");
          wrapper.className = "svg-wrapper";
          svgRef.current.appendChild(wrapper);
        }
        svg.style.width = "100%";
        svg.style.height = "100%";
        svg.removeAttribute("width");
        svg.removeAttribute("height");
        const existing = wrapper.querySelector("svg");
        if (existing) {
          morphdom(existing, svg, { childrenOnly: false });
        } else {
          wrapper.appendChild(svg);
        }
        const final = wrapper.querySelector("svg");
        if (final) {
          fixViewBox4x3(final as SVGSVGElement);
          const vbAttr = (final as SVGSVGElement).getAttribute("viewBox")?.split(" ").map(Number);
          if (vbAttr && vbAttr.length === 4) {
            baseViewBoxRef.current = { x: vbAttr[0], y: vbAttr[1], w: vbAttr[2], h: vbAttr[3] };
            applyZoom();
          }
        }
      } catch {}
    })();
  }, [editedElements, applyZoom]);

  // Zoom: pinch-to-zoom / Ctrl+scroll, pan when zoomed, double-click to reset
  useEffect(() => {
    const container = svgRef.current;
    if (!container) return;

    const handleWheel = (e: WheelEvent) => {
      const isZoomGesture = e.ctrlKey || e.metaKey;
      const isZoomedIn = Math.abs(zoomRef.current.scale - 1) > 0.01;

      if (!isZoomGesture && !isZoomedIn) return;
      e.preventDefault();

      const zoom = zoomRef.current;
      if (isZoomGesture) {
        const factor = e.deltaY > 0 ? 0.97 : 1.03;
        const newScale = Math.max(0.25, Math.min(8, zoom.scale * factor));
        if (baseViewBoxRef.current) {
          const rect = container.getBoundingClientRect();
          const mx = (e.clientX - rect.left) / rect.width;
          const my = (e.clientY - rect.top) / rect.height;
          const { w, h } = baseViewBoxRef.current;
          zoom.panX += w * (1 / newScale - 1 / zoom.scale) * (0.5 - mx);
          zoom.panY += h * (1 / newScale - 1 / zoom.scale) * (0.5 - my);
        }
        zoom.scale = newScale;
      } else if (baseViewBoxRef.current) {
        const { w, h } = baseViewBoxRef.current;
        zoom.panX += (e.deltaX / container.clientWidth) * (w / zoom.scale);
        zoom.panY += (e.deltaY / container.clientHeight) * (h / zoom.scale);
      }
      applyZoom();
    };

    const handleDblClick = () => {
      zoomRef.current = { scale: 1, panX: 0, panY: 0 };
      applyZoom();
    };

    container.addEventListener("wheel", handleWheel, { passive: false });
    container.addEventListener("dblclick", handleDblClick);
    return () => {
      container.removeEventListener("wheel", handleWheel);
      container.removeEventListener("dblclick", handleDblClick);
    };
  }, [applyZoom]);

  return (
    <div
      ref={svgRef}
      className="excalidraw-container"
      style={{ display: "flex", alignItems: "center", justifyContent: "center" }}
    />
  );
}

// ============================================================
// Main app — Excalidraw only
// ============================================================

const excalidrawLogo = <svg
      focusable="false"
      role="img"
      viewBox="0 0 40 40"
      fill="none"
    >
    <g fill="currentColor">
    <path
      d="M39.9 32.889a.326.326 0 0 0-.279-.056c-2.094-3.083-4.774-6-7.343-8.833l-.419-.472a.212.212 0 0 0-.056-.139.586.586 0 0 0-.167-.111l-.084-.083-.056-.056c-.084-.167-.28-.278-.475-.167-.782.39-1.507.973-2.206 1.528-.92.722-1.842 1.445-2.708 2.25a8.405 8.405 0 0 0-.977 1.028c-.14.194-.028.361.14.444-.615.611-1.23 1.223-1.843 1.861a.315.315 0 0 0-.084.223c0 .083.056.166.111.194l1.09.833v.028c1.535 1.528 4.244 3.611 7.12 5.861.418.334.865.667 1.284 1 .195.223.39.473.558.695.084.11.28.139.391.055.056.056.14.111.196.167a.398.398 0 0 0 .167.056.255.255 0 0 0 .224-.111.394.394 0 0 0 .055-.167c.029 0 .028.028.056.028a.318.318 0 0 0 .224-.084l5.082-5.528a.309.309 0 0 0 0-.444Zm-14.63-1.917a.485.485 0 0 0 .111.14c.586.5 1.2 1 1.843 1.555l-2.569-1.945-.251-.166c-.056-.028-.112-.084-.168-.111l-.195-.167.056-.056.055-.055.112-.111c.866-.861 2.346-2.306 3.1-3.028-.81.805-2.43 3.167-2.095 3.944Zm8.767 6.89-2.122-1.612a44.713 44.713 0 0 0-2.625-2.5c1.145.861 2.122 1.611 2.262 1.75 1.117.972 1.06.806 1.815 1.445l.921.666a1.06 1.06 0 0 1-.251.25Zm.558.416-.056-.028c.084-.055.168-.111.252-.194l-.196.222ZM1.089 5.75c.055.361.14.722.195 1.056.335 1.833.67 3.5 1.284 4.75l.252.944c.084.361.223.806.363.917 1.424 1.25 3.602 3.11 5.947 4.889a.295.295 0 0 0 .363 0s0 .027.028.027a.254.254 0 0 0 .196.084.318.318 0 0 0 .223-.084c2.988-3.305 5.221-6.027 6.813-8.305.112-.111.14-.278.14-.417.111-.111.195-.25.307-.333.111-.111.111-.306 0-.39l-.028-.027c0-.055-.028-.139-.084-.167-.698-.666-1.2-1.138-1.731-1.638-.922-.862-1.871-1.75-3.881-3.75l-.028-.028c-.028-.028-.056-.056-.112-.056-.558-.194-1.703-.389-3.127-.639C6.087 2.223 3.21 1.723.614.944c0 0-.168 0-.196.028l-.083.084c-.028.027-.056.055-.224.11h.056-.056c.028.167.028.278.084.473 0 .055.112.5.112.555l.782 3.556Zm15.496 3.278-.335-.334c.084.112.196.195.335.334Zm-3.546 4.666-.056.056c0-.028.028-.056.056-.056Zm-2.038-10c.168.167.866.834 1.033.973-.726-.334-2.54-1.167-3.379-1.445.838.167 1.983.334 2.346.472ZM1.424 2.306c.419.722.754 3.222 1.089 5.666-.196-.778-.335-1.555-.503-2.278-.251-1.277-.503-2.416-.838-3.416.056 0 .14 0 .252.028Zm-.168-.584c-.112 0-.223-.028-.307-.028 0-.027 0-.055-.028-.055.14 0 .223.028.335.083Zm-1.089.222c0-.027 0-.027 0 0ZM39.453 1.333c.028-.11-.558-.61-.363-.639.42-.027.42-.666 0-.666-.558.028-1.144.166-1.675.25-.977.194-1.982.389-2.96.61-2.205.473-4.383.973-6.561 1.557-.67.194-1.424.333-2.066.666-.224.111-.196.333-.084.472-.056.028-.084.028-.14.056-.195.028-.363.056-.558.083-.168.028-.252.167-.224.334 0 .027.028.083.028.11-1.173 1.556-2.485 3.195-3.909 4.945-1.396 1.611-2.876 3.306-4.356 5.056-4.719 5.5-10.052 11.75-15.943 17.25a.268.268 0 0 0 0 .389c.028.027.056.055.084.055-.084.084-.168.14-.252.222-.056.056-.084.111-.084.167a.605.605 0 0 0-.111.139c-.112.111-.112.305.028.389.111.11.307.11.39-.028.029-.028.029-.056.056-.056a.44.44 0 0 1 .615 0c.335.362.67.723.977 1.028l-.698-.583c-.112-.111-.307-.083-.39.028-.113.11-.085.305.027.389l7.427 6.194c.056.056.112.056.196.056s.14-.028.195-.084l.168-.166c.028.027.083.027.111.027.084 0 .14-.027.196-.083 10.052-10.055 18.15-17.639 27.42-24.417.083-.055.111-.166.111-.25.112 0 .196-.083.251-.194 1.704-5.194 2.039-9.806 2.15-12.083v-.028c0-.028.028-.056.028-.083.028-.056.028-.084.028-.084a1.626 1.626 0 0 0-.111-1.028ZM21.472 9.5c.446-.5.893-1.028 1.34-1.5-2.876 3.778-7.65 9.583-14.408 16.5 4.607-5.083 9.242-10.333 13.068-15ZM5.193 35.778h.084-.084Zm3.462 3.194c-.027-.028-.027-.028 0-.028v.028Zm4.16-3.583c.224-.25.448-.472.699-.722 0 0 0 .027.028.027-.252.223-.475.445-.726.695Zm1.146-1.111c.14-.14.279-.334.446-.5l.028-.028c1.648-1.694 3.351-3.389 5.082-5.111l.028-.028c.419-.333.921-.694 1.368-1.028a379.003 379.003 0 0 0-6.952 6.695ZM24.794 6.472c-.921 1.195-1.954 2.778-2.82 4.028-2.736 3.944-11.532 13.583-11.727 13.75a1976.983 1976.983 0 0 1-8.042 7.639l-.167.167c-.14-.167-.14-.417.028-.556C14.49 19.861 22.03 10.167 25.074 5.917c-.084.194-.14.36-.28.555Zm4.83 5.695c-1.116-.64-1.646-1.64-1.34-2.611l.084-.334c.028-.083.084-.194.14-.277.307-.5.754-.917 1.257-1.167.027 0 .055 0 .083-.028-.028-.056-.028-.139-.028-.222.028-.167.14-.278.335-.278.335 0 1.369.306 1.76.639.111.083.223.194.335.305.14.167.363.445.474.667.056.028.112.306.196.445.056.222.111.472.084.694-.028.028 0 .194-.028.194a2.668 2.668 0 0 1-.363 1.028c-.028.028-.028.056-.056.084l-.028.027c-.14.223-.335.417-.53.556-.643.444-1.369.583-2.095.389 0 0-.195-.084-.28-.111Zm8.154-.834a39.098 39.098 0 0 1-.893 3.167c0 .028-.028.083 0 .111-.056 0-.084.028-.14.056-2.206 1.61-4.356 3.305-6.506 5.028 1.843-1.64 3.686-3.306 5.613-4.945.558-.5.949-1.139 1.06-1.861l.28-1.667v-.055c.14-.334.67-.195.586.166Z"
      fill="currentColor"
    />
  </g>
    </svg>

  const githubIcon = <svg focusable="false" role="img" viewBox="0 0 20 20"  fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M7.5 15.833c-3.583 1.167-3.583-2.083-5-2.5m10 4.167v-2.917c0-.833.083-1.166-.417-1.666 2.334-.25 4.584-1.167 4.584-5a3.833 3.833 0 0 0-1.084-2.667 3.5 3.5 0 0 0-.083-2.667s-.917-.25-2.917 1.084a10.25 10.25 0 0 0-5.166 0C5.417 2.333 4.5 2.583 4.5 2.583a3.5 3.5 0 0 0-.083 2.667 3.833 3.833 0 0 0-1.084 2.667c0 3.833 2.25 4.75 4.584 5-.5.5-.5 1-.417 1.666V17.5" stroke-width="1.25"></path></svg>

  const twitterIcon = <svg focusable="false" role="img" viewBox="0 0 24 24"  fill="none" stroke-width="2" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><g stroke-width="1.25"><path stroke="none" d="M0 0h24v24H0z" fill="none"></path><path d="M4 4l11.733 16h4.267l-11.733 -16z"></path><path d="M4 20l6.768 -6.768m2.46 -2.46l6.772 -6.772"></path></g></svg>

  const discordIcon = <svg focusable="false" role="img" viewBox="0 0 20 20"  fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><g stroke-width="1.25"><path d="M7.5 10.833a.833.833 0 1 0 0-1.666.833.833 0 0 0 0 1.666ZM12.5 10.833a.833.833 0 1 0 0-1.666.833.833 0 0 0 0 1.666ZM6.25 6.25c2.917-.833 4.583-.833 7.5 0M5.833 13.75c2.917.833 5.417.833 8.334 0"></path><path d="M12.917 14.167c0 .833 1.25 2.5 1.666 2.5 1.25 0 2.361-1.39 2.917-2.5.556-1.39.417-4.861-1.25-9.584-1.214-.846-2.5-1.116-3.75-1.25l-.833 2.084M7.083 14.167c0 .833-1.13 2.5-1.526 2.5-1.191 0-2.249-1.39-2.778-2.5-.529-1.39-.397-4.861 1.19-9.584 1.157-.846 2.318-1.116 3.531-1.25l.833 2.084"></path></g></svg>


export function ExcalidrawAppCore({ app }: { app: App }) {
  const [toolInput, setToolInput] = useState<any>(null);
  const [inputIsFinal, setInputIsFinal] = useState(false);
  const [displayMode, setDisplayMode] = useState<"inline" | "fullscreen">("inline");
  const [elements, setElements] = useState<any[]>([]);
  const [userEdits, setUserEdits] = useState<any[] | null>(null);
  const [containerHeight, setContainerHeight] = useState<number | null>(null);
  const [safeAreaInsets, setSafeAreaInsets] = useState<{ top: number; right: number; bottom: number; left: number } | null>(null);
  const [isNarrow, setIsNarrow] = useState(() => typeof window !== "undefined" && window.matchMedia("(max-width: 640px)").matches);
  const [editorReady, setEditorReady] = useState(false);
  const [excalidrawApi, setExcalidrawApi] = useState<any>(null);
  const [editorSettled, setEditorSettled] = useState(false);
  const appRef = useRef<App | null>(null);
  const svgViewportRef = useRef<ViewportRect | null>(null);
  const elementsRef = useRef<any[]>([]);
  const checkpointIdRef = useRef<string | null>(null);

  const toggleFullscreen = useCallback(async () => {
    if (!appRef.current) return;
    const newMode = displayMode === "fullscreen" ? "inline" : "fullscreen";
    fsLog(`toggle: ${displayMode}→${newMode}`);
    // Sync edited elements before leaving fullscreen
    if (newMode === "inline") {
      const edited = getLatestEditedElements();
      if (edited) {
            setElements(edited);
        setUserEdits(edited);
      }
    }
    try {
      const result = await appRef.current.requestDisplayMode({ mode: newMode });
      fsLog(`requestDisplayMode result: ${result.mode}`);
      setDisplayMode(result.mode as "inline" | "fullscreen");
    } catch (err) {
      fsLog(`requestDisplayMode FAILED: ${err}`);
    }
  }, [displayMode, elements.length, inputIsFinal]);

  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.key === "Escape" && displayMode === "fullscreen") toggleFullscreen();
    };
    document.addEventListener("keydown", handler);
    return () => document.removeEventListener("keydown", handler);
  }, [displayMode, toggleFullscreen]);

  // Preload ALL Excalidraw fonts on first mount (inline mode) so they're
  // cached before fullscreen. Without this, Excalidraw's component init
  // downloads Assistant fonts, triggering a font recalc that corrupts
  // text dimensions measured with not-yet-loaded Excalifont.
  useEffect(() => {
    Promise.all([
      document.fonts.load('20px Excalifont'),
      document.fonts.load('400 16px Assistant'),
      document.fonts.load('500 16px Assistant'),
      document.fonts.load('700 16px Assistant'),
    ]).catch(() => {});
  }, []);

  // Set explicit height on html/body in fullscreen (position:fixed doesn't give body height in iframes)
  useEffect(() => {
    if (displayMode === "fullscreen" && containerHeight) {
      const h = `${containerHeight}px`;
      document.documentElement.style.height = h;
      document.body.style.height = h;
    } else {
      document.documentElement.style.height = "";
      document.body.style.height = "";
    }
  }, [displayMode, containerHeight]);

  // Mount editor when entering fullscreen
  useEffect(() => {
    if (displayMode !== "fullscreen") {
      setEditorReady(false);
      setExcalidrawApi(null);
      setEditorSettled(false);
      return;
    }
    (async () => {
      await document.fonts.ready;
      setTimeout(() => setEditorReady(true), 200);
    })();
  }, [displayMode]);

  // After editor mounts: refresh text dimensions, then reveal
  const mountEditor = displayMode === "fullscreen" && inputIsFinal && elements.length > 0 && editorReady;
  useEffect(() => {
    if (!mountEditor || !excalidrawApi) return;
    if (editorSettled) return; // already revealed, don't redo
    const api = excalidrawApi;

    const settle = async () => {
      try { await document.fonts.load('20px Excalifont'); } catch {}
      await document.fonts.ready;

      const sceneElements = api.getSceneElements();
      if (sceneElements?.length) {
        const { elements: fixed } = restore(
          { elements: sceneElements },
          null, null,
          { refreshDimensions: true }
        );
        api.updateScene({
          elements: fixed,
          captureUpdate: CaptureUpdateAction.NEVER,
        });
      }
      requestAnimationFrame(() => setEditorSettled(true));
    };

    const timer = setTimeout(settle, 200);
    return () => clearTimeout(timer);
  }, [mountEditor, excalidrawApi, editorSettled]);

  // Keep elementsRef in sync for ontoolresult handler (which captures closure once)
  useEffect(() => { elementsRef.current = elements; }, [elements]);

  // Set up MCP event handlers when app is provided
  useEffect(() => {
    appRef.current = app;
    _logFn = (msg) => { try { app.sendLog({ level: "info", logger: "FS", data: msg }); } catch {} };

    // Capture initial container dimensions + safe area insets
    const initCtx = app.getHostContext() as any;
    if (initCtx?.containerDimensions?.height) setContainerHeight(initCtx.containerDimensions.height);
    if (initCtx?.safeAreaInsets) setSafeAreaInsets(initCtx.safeAreaInsets);

    app.onhostcontextchanged = (ctx: any) => {
      if (ctx.containerDimensions?.height) {
        setContainerHeight(ctx.containerDimensions.height);
      }
      if (ctx.safeAreaInsets) {
        setSafeAreaInsets(ctx.safeAreaInsets);
      }
      if (ctx.displayMode) {
        fsLog(`hostContextChanged: displayMode=${ctx.displayMode}`);
        // Sync edited elements when host exits fullscreen
        if (ctx.displayMode === "inline") {
          const edited = getLatestEditedElements();
          if (edited) {
            setElements(edited);
            setUserEdits(edited);
          }
        }
        setDisplayMode(ctx.displayMode as "inline" | "fullscreen");
      }
    };

    app.ontoolinputpartial = async (input) => {
      const args = (input as any)?.arguments || input;
      setInputIsFinal(false);
      setToolInput(args);
    };

    app.ontoolinput = async (input) => {
      const args = (input as any)?.arguments || input;
      setInputIsFinal(true);
      setToolInput(args);
    };

    app.ontoolresult = (result: any) => {
      const cpId = (result.structuredContent as { checkpointId?: string })?.checkpointId;
      if (cpId) {
        checkpointIdRef.current = cpId;
        setCheckpointId(cpId);
        // Use checkpointId as localStorage key for persisting user edits
        setStorageKey(cpId);
        // Check for persisted edits from a previous fullscreen session
        const persisted = loadPersistedElements();
        if (persisted && persisted.length > 0) {
          elementsRef.current = persisted;
          setElements(persisted);
          setUserEdits(persisted);
        }
      }
    };

    app.onteardown = async () => ({});
    app.onerror = (err) => console.error("[Excalidraw] Error:", err);
  }, [app]);

  // Track narrow viewport for mobile layout adjustments
  useEffect(() => {
    const mq = window.matchMedia("(max-width: 640px)");
    const handler = (e: MediaQueryListEvent) => setIsNarrow(e.matches);
    mq.addEventListener("change", handler);
    return () => mq.removeEventListener("change", handler);
  }, []);

  // Bridge hostContext.safeAreaInsets → Excalidraw's native --sat/--sar/--sab/--sal.
  // Excalidraw's .FixedSideContainer reads padding-top: var(--sat) — this offsets
  // only the floating toolbar/menus, keeping the canvas full-bleed. env(safe-area-*)
  // is 0 inside cross-origin iframes on iOS, so the host MUST supply pixel values.
  useEffect(() => {
    const root = document.documentElement;
    if (displayMode === "fullscreen" && isNarrow && safeAreaInsets) {
      root.style.setProperty("--sat", `${safeAreaInsets.top}px`);
      root.style.setProperty("--sar", `${safeAreaInsets.right}px`);
      root.style.setProperty("--sab", `${safeAreaInsets.bottom}px`);
      root.style.setProperty("--sal", `${safeAreaInsets.left}px`);
    } else {
      root.style.removeProperty("--sat");
      root.style.removeProperty("--sar");
      root.style.removeProperty("--sab");
      root.style.removeProperty("--sal");
    }
  }, [displayMode, isNarrow, safeAreaInsets]);

  return (
    <main className={`main${displayMode === "fullscreen" ? " fullscreen" : ""}`} style={displayMode === "fullscreen" && containerHeight ? { height: containerHeight } : undefined}>
      {displayMode === "inline" && (
        <div className="toolbar">
          <ShareButton
                onConfirm={async () => {
                  await shareToExcalidraw({
                    elements,
                    appState: {},
                    files: {}
                  }, app);
                }}
              />

          <button
            className="app-button"
            onClick={toggleFullscreen}
            title="Enter fullscreen"
          >
            <span>Edit</span>
            <ExpandIcon />
          </button>
        </div>
      )}
      {/* Editor: mount hidden when ready, reveal after viewport is set */}
      {mountEditor && (
        <div style={{
          width: "100%",
          height: "100%",
          visibility: editorSettled ? "visible" : "hidden",
          position: editorSettled ? undefined : "absolute",
          inset: editorSettled ? undefined : 0,
        }}>
          <Excalidraw
            excalidrawAPI={(api) => { setExcalidrawApi(api); fsLog(`excalidrawAPI set`); }}
            initialData={{ elements: elements as any, scrollToContent: true }}
            theme="light"
            onChange={(els) => onEditorChange(app, els)}
            renderTopRightUI={isNarrow ? undefined : () => (
              <ShareButton
                onConfirm={async () => {
                  if (excalidrawApi) {
                    const elements = excalidrawApi.getSceneElements();
                    const appState = excalidrawApi.getAppState();
                    const files = excalidrawApi.getFiles();

                    await shareToExcalidraw({ elements, appState, files }, app);
                  }
                }}
              />
            )}
          >
            <MainMenu>
              <MainMenu.Item
                onSelect={() => {
                  app.openLink({
                    url: "https://plus.excalidraw.com?utm_source=mcp_app_menu"
                  })
                }}
                style={{minWidth: 200}}
              >
                {excalidrawLogo} Excalidraw
              </MainMenu.Item>
              <MainMenu.Item
                onSelect={() => {
                  app.openLink({
                    url: "https://github.com/excalidraw/excalidraw"
                  })
                }}
                style={{minWidth: 200}}
              >
                {githubIcon} GitHub
              </MainMenu.Item>
              <MainMenu.Item
                onSelect={() => {
                  app.openLink({
                    url: "https://x.com/excalidraw"
                  })
                }}
                style={{minWidth: 200}}
              >
                {twitterIcon} Follow us
              </MainMenu.Item>
              <MainMenu.Item
                onSelect={() => {
                  app.openLink({
                    url: "https://discord.gg/UexuTaE"
                  })
                }}
                style={{minWidth: 200}}
              >
                {discordIcon} Discord chat
              </MainMenu.Item>
            </MainMenu >
          </Excalidraw>
          {isNarrow && (
            <div className="mobile-share-slot">
              <ShareButton
                compact
                onConfirm={async () => {
                  if (excalidrawApi) {
                    const elements = excalidrawApi.getSceneElements();
                    const appState = excalidrawApi.getAppState();
                    const files = excalidrawApi.getFiles();
                    await shareToExcalidraw({ elements, appState, files }, app);
                  }
                }}
              />
            </div>
          )}
        </div>
      )}
      {/* SVG: stays visible until editor is fully settled */}
      {!editorSettled && (
        <div
          onClick={undefined}
          style={undefined}
        >
          <DiagramView toolInput={toolInput} isFinal={inputIsFinal} displayMode={displayMode} onElements={(els) => { elementsRef.current = els; setElements(els); }} editedElements={userEdits ?? undefined} onViewport={(vp) => { svgViewportRef.current = vp; }} loadCheckpoint={async (id) => {
            if (!appRef.current) return null;
            try {
              const result = await appRef.current.callServerTool({ name: "read_checkpoint", arguments: { id } });
              const text = (result.content[0] as any)?.text;
              if (!text) return null;
              return JSON.parse(text);
            } catch { return null; }
          }} />
        </div>
      )}
    </main>
  );
}

export function ExcalidrawApp() {
  const { app, error } = useApp({
    appInfo: { name: "Excalidraw", version: "1.0.0" },
    capabilities: {},
  });

  if (error) return <div className="error">ERROR: {error.message}</div>;
  if (!app) return <div className="loading">Connecting...</div>;
  return <ExcalidrawAppCore app={app} />;
}
```

## File: `src/mcp-entry.tsx`
```tsx
import { createRoot } from "react-dom/client";
import { ExcalidrawApp } from "./mcp-app";

createRoot(document.body).render(<ExcalidrawApp />);
```

## File: `src/pencil-audio.ts`
```typescript
import { PENCIL_STROKE_SOFT } from "./sounds";

/**
 * Pencil stroke audio engine.
 * Plays randomized variations of a pencil-on-paper sample when elements
 * appear during streaming. Each stroke varies in pitch, gain, duration,
 * and sample offset so no two elements sound identical.
 */

let audioCtx: AudioContext | null = null;
let softBuffer: AudioBuffer | null = null;
let initialized = false;
let initPromise: Promise<void> | null = null;

function getAudioContext(): AudioContext {
  if (!audioCtx) {
    audioCtx = new AudioContext();
  }
  return audioCtx;
}

async function decodeBase64Audio(base64: string): Promise<AudioBuffer> {
  const ctx = getAudioContext();
  const binary = atob(base64);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) {
    bytes[i] = binary.charCodeAt(i);
  }
  return ctx.decodeAudioData(bytes.buffer);
}

/** Initialize audio buffers. Call once, safe to call multiple times. */
export async function initPencilAudio(): Promise<void> {
  if (initialized) return;
  if (initPromise) return initPromise;
  initPromise = (async () => {
    try {
      softBuffer = await decodeBase64Audio(PENCIL_STROKE_SOFT);
      initialized = true;
    } catch (e) {
      console.warn("[PencilAudio] Failed to init:", e);
    }
  })();
  return initPromise;
}

/** Play a pencil stroke sound for a given element type. */
export function playStroke(elementType: string): void {
  if (!initialized || !audioCtx) return;

  // Use soft stroke for all element types
  const isLine = elementType === "arrow" || elementType === "line";
  const buffer = softBuffer;
  if (!buffer) return;

  // Resume context if suspended (autoplay policy)
  if (audioCtx.state === "suspended") {
    audioCtx.resume().catch(() => {});
  }

  const ctx = audioCtx;

  // Create source with random offset into the sample
  const source = ctx.createBufferSource();
  source.buffer = buffer;

  // Random playback rate for pitch variation (0.85–1.2)
  source.playbackRate.value = 0.85 + Math.random() * 0.35;

  // Gain node for volume envelope — normalize across samples
  const gain = ctx.createGain();
  const isText = elementType === "text";
  // Per-type gain normalization: shapes are most prominent, text medium, arrows lighter
  const typeGain = isLine ? 1.0 : isText ? 2.0 : 2.5;
  const baseVolume = (0.8 + Math.random() * 0.4) * typeGain; // normalized
  gain.gain.setValueAtTime(0, ctx.currentTime);
  gain.gain.linearRampToValueAtTime(baseVolume, ctx.currentTime + 0.03); // quick attack
  // Duration varies by element type
  const duration = isLine ? 0.3 + Math.random() * 0.3 : 0.2 + Math.random() * 0.4;
  gain.gain.linearRampToValueAtTime(0, ctx.currentTime + duration); // fade out

  // Connect: source → gain → destination
  source.connect(gain);
  gain.connect(ctx.destination);

  // Start at random offset within the sample
  const maxOffset = Math.max(0, buffer.duration - duration - 0.1);
  const offset = Math.random() * maxOffset;
  source.start(0, offset, duration + 0.1);

  // Cleanup
  source.onended = () => {
    source.disconnect();
    gain.disconnect();
  };
}
```

## File: `src/server.ts`
```typescript
import { registerAppResource, registerAppTool, RESOURCE_MIME_TYPE } from "@modelcontextprotocol/ext-apps/server";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import type { CallToolResult, ReadResourceResult } from "@modelcontextprotocol/sdk/types.js";
import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { deflateSync } from "node:zlib";
import { z } from "zod/v4";
import type { CheckpointStore } from "./checkpoint-store.js";

/** Maximum allowed size for element/data input strings (5 MB). */
const MAX_INPUT_BYTES = 5 * 1024 * 1024;

// Works both from source (src/server.ts) and compiled (dist/server.js)
const DIST_DIR = import.meta.filename.endsWith(".ts")
  ? path.join(import.meta.dirname, "..", "dist")
  : import.meta.dirname;

// ============================================================
// RECALL: shared knowledge for the agent
// ============================================================
const RECALL_CHEAT_SHEET = `# Excalidraw Element Format

Thanks for calling read_me! Do NOT call it again in this conversation — you will not see anything new. Now use create_view to draw.

## Color Palette (use consistently across all tools)

### Primary Colors
| Name | Hex | Use |
|------|-----|-----|
| Blue | \`#4a9eed\` | Primary actions, links, data series 1 |
| Amber | \`#f59e0b\` | Warnings, highlights, data series 2 |
| Green | \`#22c55e\` | Success, positive, data series 3 |
| Red | \`#ef4444\` | Errors, negative, data series 4 |
| Purple | \`#8b5cf6\` | Accents, special items, data series 5 |
| Pink | \`#ec4899\` | Decorative, data series 6 |
| Cyan | \`#06b6d4\` | Info, secondary, data series 7 |
| Lime | \`#84cc16\` | Extra, data series 8 |

### Excalidraw Fills (pastel, for shape backgrounds)
| Color | Hex | Good For |
|-------|-----|----------|
| Light Blue | \`#a5d8ff\` | Input, sources, primary nodes |
| Light Green | \`#b2f2bb\` | Success, output, completed |
| Light Orange | \`#ffd8a8\` | Warning, pending, external |
| Light Purple | \`#d0bfff\` | Processing, middleware, special |
| Light Red | \`#ffc9c9\` | Error, critical, alerts |
| Light Yellow | \`#fff3bf\` | Notes, decisions, planning |
| Light Teal | \`#c3fae8\` | Storage, data, memory |
| Light Pink | \`#eebefa\` | Analytics, metrics |

### Background Zones (use with opacity: 30 for layered diagrams)
| Color | Hex | Good For |
|-------|-----|----------|
| Blue zone | \`#dbe4ff\` | UI / frontend layer |
| Purple zone | \`#e5dbff\` | Logic / agent layer |
| Green zone | \`#d3f9d8\` | Data / tool layer |

---

## Excalidraw Elements

### Required Fields (all elements)
\`type\`, \`id\` (unique string), \`x\`, \`y\`, \`width\`, \`height\`

### Defaults (skip these)
strokeColor="#1e1e1e", backgroundColor="transparent", fillStyle="solid", strokeWidth=2, roughness=1, opacity=100
Canvas background is white.

### Element Types

**Rectangle**: \`{ "type": "rectangle", "id": "r1", "x": 100, "y": 100, "width": 200, "height": 100 }\`
- \`roundness: { type: 3 }\` for rounded corners
- \`backgroundColor: "#a5d8ff"\`, \`fillStyle: "solid"\` for filled

**Ellipse**: \`{ "type": "ellipse", "id": "e1", "x": 100, "y": 100, "width": 150, "height": 150 }\`

**Diamond**: \`{ "type": "diamond", "id": "d1", "x": 100, "y": 100, "width": 150, "height": 150 }\`

**Labeled shape (PREFERRED)**: Add \`label\` to any shape for auto-centered text. No separate text element needed.
\`{ "type": "rectangle", "id": "r1", "x": 100, "y": 100, "width": 200, "height": 80, "label": { "text": "Hello", "fontSize": 20 } }\`
- Works on rectangle, ellipse, diamond
- Text auto-centers and container auto-resizes to fit
- Saves tokens vs separate text elements

**Labeled arrow**: \`"label": { "text": "connects" }\` on an arrow element.

**Standalone text** (titles, annotations only):
\`{ "type": "text", "id": "t1", "x": 150, "y": 138, "text": "Hello", "fontSize": 20 }\`
- x is the LEFT edge of the text. To center text at position cx: set x = cx - estimatedWidth/2
- estimatedWidth ≈ text.length × fontSize × 0.5
- Do NOT rely on textAlign or width for positioning — they only affect multi-line wrapping

**Arrow**: \`{ "type": "arrow", "id": "a1", "x": 300, "y": 150, "width": 200, "height": 0, "points": [[0,0],[200,0]], "endArrowhead": "arrow" }\`
- points: [dx, dy] offsets from element x,y
- endArrowhead: null | "arrow" | "bar" | "dot" | "triangle"

### Arrow Bindings
Arrow: \`"startBinding": { "elementId": "r1", "fixedPoint": [1, 0.5] }\`
fixedPoint: top=[0.5,0], bottom=[0.5,1], left=[0,0.5], right=[1,0.5]

**cameraUpdate** (pseudo-element — controls the viewport, not drawn):
\`{ "type": "cameraUpdate", "width": 800, "height": 600, "x": 0, "y": 0 }\`
- x, y: top-left corner of the visible area (scene coordinates)
- width, height: size of the visible area — MUST be 4:3 ratio (400×300, 600×450, 800×600, 1200×900, 1600×1200)
- Animates smoothly between positions — use multiple cameraUpdates to guide attention as you draw
- No \`id\` needed — this is not a drawn element

**delete** (pseudo-element — removes elements by id):
\`{ "type": "delete", "ids": "b2,a1,t3" }\`
- Comma-separated list of element ids to remove
- Also removes bound text elements (matching \`containerId\`)
- Place AFTER the elements you want to remove
- Never reuse a deleted id — always assign new ids to replacements

### Drawing Order (CRITICAL for streaming)
- Array order = z-order (first = back, last = front)
- **Emit progressively**: background → shape → its label → its arrows → next shape
- BAD: all rectangles → all texts → all arrows
- GOOD: bg_shape → shape1 → text1 → arrow1 → shape2 → text2 → ...

### Example: Two connected labeled boxes
\`\`\`json
[
  { "type": "cameraUpdate", "width": 800, "height": 600, "x": 50, "y": 50 },
  { "type": "rectangle", "id": "b1", "x": 100, "y": 100, "width": 200, "height": 100, "roundness": { "type": 3 }, "backgroundColor": "#a5d8ff", "fillStyle": "solid", "label": { "text": "Start", "fontSize": 20 } },
  { "type": "rectangle", "id": "b2", "x": 450, "y": 100, "width": 200, "height": 100, "roundness": { "type": 3 }, "backgroundColor": "#b2f2bb", "fillStyle": "solid", "label": { "text": "End", "fontSize": 20 } },
  { "type": "arrow", "id": "a1", "x": 300, "y": 150, "width": 150, "height": 0, "points": [[0,0],[150,0]], "endArrowhead": "arrow", "startBinding": { "elementId": "b1", "fixedPoint": [1, 0.5] }, "endBinding": { "elementId": "b2", "fixedPoint": [0, 0.5] } }
]
\`\`\`

### Camera & Sizing (CRITICAL for readability)

The diagram displays inline at ~700px width. Design for this constraint.

**Recommended camera sizes (4:3 aspect ratio ONLY):**
- Camera **S**: width 400, height 300 — close-up on a small group (2-3 elements)
- Camera **M**: width 600, height 450 — medium view, a section of a diagram
- Camera **L**: width 800, height 600 — standard full diagram (DEFAULT)
- Camera **XL**: width 1200, height 900 — large diagram overview. WARNING: font size smaller than 18 is unreadable
- Camera **XXL**: width 1600, height 1200 — panorama / final overview of complex diagrams. WARNING: minimum readable font size is 21

ALWAYS use one of these exact sizes. Non-4:3 viewports cause distortion.

**Font size rules:**
- Minimum fontSize: **16** for body text, labels, descriptions
- Minimum fontSize: **20** for titles and headings
- Minimum fontSize: **14** for secondary annotations only (sparingly)
- NEVER use fontSize below 14 — it becomes unreadable at display scale

**Element sizing rules:**
- Minimum shape size: 120×60 for labeled rectangles/ellipses
- Leave 20-30px gaps between elements minimum
- Prefer fewer, larger elements over many tiny ones

ALWAYS start with a \`cameraUpdate\` as the FIRST element. For example:
\`{ "type": "cameraUpdate", "width": 800, "height": 600, "x": 0, "y": 0 }\`

- x, y: top-left corner of visible area (scene coordinates)
- ALWAYS emit the cameraUpdate BEFORE drawing the elements it frames — camera moves first, then content appears
- The camera animates smoothly between positions
- Leave padding: don't match camera size to content size exactly (e.g., 500px content in 800x600 camera)

Examples:
\`{ "type": "cameraUpdate", "width": 800, "height": 600, "x": 0, "y": 0 }\` — standard view
\`{ "type": "cameraUpdate", "width": 400, "height": 300, "x": 200, "y": 100 }\` — zoom into a detail
\`{ "type": "cameraUpdate", "width": 1600, "height": 1200, "x": -50, "y": -50 }\` — panorama overview

Tip: For large diagrams, emit a cameraUpdate to focus on each section as you draw it.

## Diagram Example

Example prompt: "Explain how photosynthesis works"

Uses 2 camera positions: start zoomed in (M) for title, then zoom out (L) to reveal the full diagram. Sun art drawn last as a finishing touch.

- **Camera 1** (400x300): Draw the title "Photosynthesis" and formula subtitle zoomed in
- **Camera 2** (800x600): Zoom out — draw the leaf zone, process flow (Light Reactions → Calvin Cycle), inputs (Sunlight, Water, CO2), outputs (O2, Glucose), and finally a cute 8-ray sun

\`\`\`json
[
  {"type":"cameraUpdate","width":400,"height":300,"x":200,"y":-20},
  {"type":"text","id":"ti","x":280,"y":10,"text":"Photosynthesis","fontSize":28,"strokeColor":"#1e1e1e"},
  {"type":"text","id":"fo","x":245,"y":48,"text":"6CO2 + 6H2O --> C6H12O6 + 6O2","fontSize":16,"strokeColor":"#757575"},
  {"type":"cameraUpdate","width":800,"height":600,"x":0,"y":-20},
  {"type":"rectangle","id":"lf","x":150,"y":90,"width":520,"height":380,"backgroundColor":"#d3f9d8","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#22c55e","strokeWidth":1,"opacity":35},
  {"type":"text","id":"lfl","x":170,"y":96,"text":"Inside the Leaf","fontSize":16,"strokeColor":"#15803d"},
  {"type":"rectangle","id":"lr","x":190,"y":190,"width":160,"height":70,"backgroundColor":"#fff3bf","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#f59e0b","label":{"text":"Light Reactions","fontSize":16}},
  {"type":"arrow","id":"a1","x":350,"y":225,"width":120,"height":0,"points":[[0,0],[120,0]],"strokeColor":"#1e1e1e","strokeWidth":2,"endArrowhead":"arrow","label":{"text":"ATP","fontSize":14}},
  {"type":"rectangle","id":"cc","x":470,"y":190,"width":160,"height":70,"backgroundColor":"#d0bfff","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#8b5cf6","label":{"text":"Calvin Cycle","fontSize":16}},
  {"type":"rectangle","id":"sl","x":10,"y":200,"width":120,"height":50,"backgroundColor":"#fff3bf","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#f59e0b","label":{"text":"Sunlight","fontSize":16}},
  {"type":"arrow","id":"a2","x":130,"y":225,"width":60,"height":0,"points":[[0,0],[60,0]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":"arrow"},
  {"type":"rectangle","id":"wa","x":200,"y":360,"width":140,"height":50,"backgroundColor":"#a5d8ff","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#4a9eed","label":{"text":"Water (H2O)","fontSize":16}},
  {"type":"arrow","id":"a3","x":270,"y":360,"width":0,"height":-100,"points":[[0,0],[0,-100]],"strokeColor":"#4a9eed","strokeWidth":2,"endArrowhead":"arrow"},
  {"type":"rectangle","id":"co","x":480,"y":360,"width":130,"height":50,"backgroundColor":"#ffd8a8","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#f59e0b","label":{"text":"CO2","fontSize":16}},
  {"type":"arrow","id":"a4","x":545,"y":360,"width":0,"height":-100,"points":[[0,0],[0,-100]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":"arrow"},
  {"type":"rectangle","id":"ox","x":540,"y":100,"width":100,"height":40,"backgroundColor":"#ffc9c9","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#ef4444","label":{"text":"O2","fontSize":16}},
  {"type":"arrow","id":"a5","x":310,"y":190,"width":230,"height":-50,"points":[[0,0],[230,-50]],"strokeColor":"#ef4444","strokeWidth":2,"endArrowhead":"arrow"},
  {"type":"rectangle","id":"gl","x":690,"y":195,"width":120,"height":60,"backgroundColor":"#c3fae8","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#22c55e","label":{"text":"Glucose","fontSize":18}},
  {"type":"arrow","id":"a6","x":630,"y":225,"width":60,"height":0,"points":[[0,0],[60,0]],"strokeColor":"#22c55e","strokeWidth":2,"endArrowhead":"arrow"},
  {"type":"ellipse","id":"sun","x":30,"y":110,"width":50,"height":50,"backgroundColor":"#fff3bf","fillStyle":"solid","strokeColor":"#f59e0b","strokeWidth":2},
  {"type":"arrow","id":"r1","x":55,"y":108,"width":0,"height":-14,"points":[[0,0],[0,-14]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":null,"startArrowhead":null},
  {"type":"arrow","id":"r2","x":55,"y":162,"width":0,"height":14,"points":[[0,0],[0,14]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":null,"startArrowhead":null},
  {"type":"arrow","id":"r3","x":28,"y":135,"width":-14,"height":0,"points":[[0,0],[-14,0]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":null,"startArrowhead":null},
  {"type":"arrow","id":"r4","x":82,"y":135,"width":14,"height":0,"points":[[0,0],[14,0]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":null,"startArrowhead":null},
  {"type":"arrow","id":"r5","x":73,"y":117,"width":10,"height":-10,"points":[[0,0],[10,-10]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":null,"startArrowhead":null},
  {"type":"arrow","id":"r6","x":37,"y":117,"width":-10,"height":-10,"points":[[0,0],[-10,-10]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":null,"startArrowhead":null},
  {"type":"arrow","id":"r7","x":73,"y":153,"width":10,"height":10,"points":[[0,0],[10,10]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":null,"startArrowhead":null},
  {"type":"arrow","id":"r8","x":37,"y":153,"width":-10,"height":10,"points":[[0,0],[-10,10]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":null,"startArrowhead":null}
]
\`\`\`

Common mistakes to avoid:
- **Camera size must match content with padding** — if your content is 500px tall, use 800x600 camera, not 500px. No padding = truncated edges
- **Center titles relative to the diagram below** — estimate the diagram's total width and center the title text over it, not over the canvas
- **Arrow labels need space** — long labels like "ATP + NADPH" overflow short arrows. Keep labels short or make arrows wider
- **Elements overlap when y-coordinates are close** — always check that text, boxes, and labels don't stack on top of each other (e.g., an output box overlapping a zone label)
- **Draw art/illustrations LAST** — cute decorations (sun, stars, icons) should appear as the final drawing step so they don't distract from the main content being built

## Sequence flow Diagram Example

Example prompt: "show a sequence diagram explaining MCP Apps"

This demonstrates a UML-style sequence diagram with 4 actors (User, Agent, App iframe, MCP Server), dashed lifelines, and labeled arrows showing the full MCP Apps request/response flow. Camera pans progressively across the diagram:

- **Camera 1** (600x450): Title "MCP Apps — Sequence Flow"
- **Cameras 2–5** (400x300 each): Zoom into each actor column right-to-left — draw header box + dashed lifeline for Server, App, Agent, User. Right-to-left so the camera snakes smoothly: pan left across actors, then pan right following the first message arrows
- **Camera 6** (400x300): Zoom into User — draw stick figure (head + body)
- **Camera 7** (600x450): Zoom out — draw first message arrows: user prompt → agent, agent tools/call → server, tool result back, result forwarded to app iframe
- **Camera 8** (600x450): Pan down — draw user interaction with app, app requesting tools/call back to agent
- **Camera 9** (600x450): Pan further down — agent forwards to server, fresh data flows back through the chain, context update from app to agent
- **Camera 10** (800x600): Final zoom-out showing the complete sequence

\`\`\`json
[
  {"type":"cameraUpdate","width":600,"height":450,"x":80,"y":-10},
  {"type":"text","id":"title","x":200,"y":15,"text":"MCP Apps — Sequence Flow","fontSize":24,"strokeColor":"#1e1e1e"},

  {"type":"cameraUpdate","width":400,"height":300,"x":450,"y":-5},
  {"type":"rectangle","id":"sHead","x":600,"y":60,"width":130,"height":40,"backgroundColor":"#ffd8a8","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#f59e0b","strokeWidth":2,"label":{"text":"MCP Server","fontSize":16}},
  {"type":"arrow","id":"sLine","x":665,"y":100,"width":0,"height":490,"points":[[0,0],[0,490]],"strokeColor":"#b0b0b0","strokeWidth":1,"strokeStyle":"dashed","endArrowhead":null},

  {"type":"cameraUpdate","width":400,"height":300,"x":250,"y":-5},
  {"type":"rectangle","id":"appHead","x":400,"y":60,"width":130,"height":40,"backgroundColor":"#b2f2bb","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#22c55e","strokeWidth":2,"label":{"text":"App iframe","fontSize":16}},
  {"type":"arrow","id":"appLine","x":465,"y":100,"width":0,"height":490,"points":[[0,0],[0,490]],"strokeColor":"#b0b0b0","strokeWidth":1,"strokeStyle":"dashed","endArrowhead":null},

  {"type":"cameraUpdate","width":400,"height":300,"x":80,"y":-5},
  {"type":"rectangle","id":"aHead","x":230,"y":60,"width":100,"height":40,"backgroundColor":"#d0bfff","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#8b5cf6","strokeWidth":2,"label":{"text":"Agent","fontSize":16}},
  {"type":"arrow","id":"aLine","x":280,"y":100,"width":0,"height":490,"points":[[0,0],[0,490]],"strokeColor":"#b0b0b0","strokeWidth":1,"strokeStyle":"dashed","endArrowhead":null},

  {"type":"cameraUpdate","width":400,"height":300,"x":-10,"y":-5},
  {"type":"rectangle","id":"uHead","x":60,"y":60,"width":100,"height":40,"backgroundColor":"#a5d8ff","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#4a9eed","strokeWidth":2,"label":{"text":"User","fontSize":16}},
  {"type":"arrow","id":"uLine","x":110,"y":100,"width":0,"height":490,"points":[[0,0],[0,490]],"strokeColor":"#b0b0b0","strokeWidth":1,"strokeStyle":"dashed","endArrowhead":null},

  {"type":"cameraUpdate","width":400,"height":300,"x":-40,"y":50},
  {"type":"ellipse","id":"uh","x":58,"y":110,"width":20,"height":20,"backgroundColor":"#a5d8ff","fillStyle":"solid","strokeColor":"#4a9eed","strokeWidth":2},
  {"type":"rectangle","id":"ub","x":57,"y":132,"width":22,"height":26,"backgroundColor":"#a5d8ff","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#4a9eed","strokeWidth":2},

  {"type":"cameraUpdate","width":600,"height":450,"x":-20,"y":-30},
  {"type":"arrow","id":"m1","x":110,"y":135,"width":170,"height":0,"points":[[0,0],[170,0]],"strokeColor":"#1e1e1e","strokeWidth":2,"endArrowhead":"arrow","label":{"text":"display a chart","fontSize":14}},
  {"type":"rectangle","id":"note1","x":130,"y":162,"width":310,"height":26,"backgroundColor":"#fff3bf","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#f59e0b","strokeWidth":1,"opacity":50,"label":{"text":"Interactive app rendered in chat","fontSize":14}},

  {"type":"cameraUpdate","width":600,"height":450,"x":170,"y":25},
  {"type":"arrow","id":"m2","x":280,"y":210,"width":385,"height":0,"points":[[0,0],[385,0]],"strokeColor":"#8b5cf6","strokeWidth":2,"endArrowhead":"arrow","label":{"text":"tools/call","fontSize":16}},
  {"type":"arrow","id":"m3","x":665,"y":250,"width":-385,"height":0,"points":[[0,0],[-385,0]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":"arrow","strokeStyle":"dashed","label":{"text":"tool input/result","fontSize":16}},
  {"type":"arrow","id":"m4","x":280,"y":290,"width":185,"height":0,"points":[[0,0],[185,0]],"strokeColor":"#8b5cf6","strokeWidth":2,"endArrowhead":"arrow","strokeStyle":"dashed","label":{"text":"result → app","fontSize":16}},

  {"type":"cameraUpdate","width":600,"height":450,"x":-10,"y":135},
  {"type":"arrow","id":"m5","x":110,"y":340,"width":355,"height":0,"points":[[0,0],[355,0]],"strokeColor":"#4a9eed","strokeWidth":2,"endArrowhead":"arrow","label":{"text":"user interacts","fontSize":16}},
  {"type":"arrow","id":"m6","x":465,"y":380,"width":-185,"height":0,"points":[[0,0],[-185,0]],"strokeColor":"#22c55e","strokeWidth":2,"endArrowhead":"arrow","label":{"text":"tools/call request","fontSize":16}},

  {"type":"cameraUpdate","width":600,"height":450,"x":170,"y":235},
  {"type":"arrow","id":"m7","x":280,"y":420,"width":385,"height":0,"points":[[0,0],[385,0]],"strokeColor":"#8b5cf6","strokeWidth":2,"endArrowhead":"arrow","label":{"text":"tools/call (forwarded)","fontSize":16}},
  {"type":"arrow","id":"m8","x":665,"y":460,"width":-385,"height":0,"points":[[0,0],[-385,0]],"strokeColor":"#f59e0b","strokeWidth":2,"endArrowhead":"arrow","strokeStyle":"dashed","label":{"text":"fresh data","fontSize":16}},
  {"type":"arrow","id":"m9","x":280,"y":500,"width":185,"height":0,"points":[[0,0],[185,0]],"strokeColor":"#8b5cf6","strokeWidth":2,"endArrowhead":"arrow","strokeStyle":"dashed","label":{"text":"fresh data","fontSize":16}},

  {"type":"cameraUpdate","width":600,"height":450,"x":50,"y":327},
  {"type":"rectangle","id":"note2","x":130,"y":522,"width":310,"height":26,"backgroundColor":"#d3f9d8","fillStyle":"solid","roundness":{"type":3},"strokeColor":"#22c55e","strokeWidth":1,"opacity":50,"label":{"text":"App updates with new data","fontSize":14}},
  {"type":"arrow","id":"m10","x":465,"y":570,"width":-185,"height":0,"points":[[0,0],[-185,0]],"strokeColor":"#22c55e","strokeWidth":2,"endArrowhead":"arrow","strokeStyle":"dashed","label":{"text":"context update","fontSize":16}},

  {"type":"cameraUpdate","width":800,"height":600,"x":-5,"y":2}
]
\`\`\`

## Checkpoints (restoring previous state)

Every create_view call returns a \`checkpointId\` in its response. To continue from a previous diagram state, start your elements array with a restoreCheckpoint element:

\`[{"type":"restoreCheckpoint","id":"<checkpointId>"}, ...additional new elements...]\`

The saved state (including any user edits made in fullscreen) is loaded from the client, and your new elements are appended on top. This saves tokens — you don't need to re-send the entire diagram.

## Deleting Elements

Remove elements by id using the \`delete\` pseudo-element:

\`{"type":"delete","ids":"b2,a1,t3"}\`

Works in two modes:
- **With restoreCheckpoint**: restore a saved state, then surgically remove specific elements before adding new ones
- **Inline (animation mode)**: draw elements, then delete and replace them later in the same array to create transformation effects

Place delete entries AFTER the elements you want to remove. The final render filters them out.

**IMPORTANT**: Every element id must be unique. Never reuse an id after deleting it — always assign a new id to replacement elements.

## Animation Mode — Transform in Place

Instead of building left-to-right and panning away, you can animate by DELETING elements and replacing them at the same position. Combined with slight camera moves, this creates smooth visual transformations during streaming.

Pattern:
1. Draw initial elements
2. cameraUpdate (shift/zoom slightly)
3. \`{"type":"delete","ids":"old1,old2"}\`
4. Draw replacements at same coordinates (different color/content)
5. Repeat

Example prompt: "Pixel snake eats apple"

Snake moves right by adding a head segment and deleting the tail. On eating the apple, tail is NOT deleted (snake grows). Camera nudges between frames add subtle motion.

\`\`\`json
[
  {"type":"cameraUpdate","width":400,"height":300,"x":0,"y":0},
  {"type":"ellipse","id":"ap","x":260,"y":78,"width":20,"height":20,"backgroundColor":"#ef4444","fillStyle":"solid","strokeColor":"#ef4444"},
  {"type":"rectangle","id":"s0","x":60,"y":130,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"rectangle","id":"s1","x":88,"y":130,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"rectangle","id":"s2","x":116,"y":130,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"rectangle","id":"s3","x":144,"y":130,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"cameraUpdate","width":400,"height":300,"x":1,"y":0},
  {"type":"rectangle","id":"s4","x":172,"y":130,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"delete","ids":"s0"},
  {"type":"cameraUpdate","width":400,"height":300,"x":0,"y":1},
  {"type":"rectangle","id":"s5","x":200,"y":130,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"delete","ids":"s1"},
  {"type":"cameraUpdate","width":400,"height":300,"x":1,"y":0},
  {"type":"rectangle","id":"s6","x":228,"y":130,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"delete","ids":"s2"},
  {"type":"cameraUpdate","width":400,"height":300,"x":0,"y":0},
  {"type":"rectangle","id":"s7","x":256,"y":130,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"delete","ids":"s3"},
  {"type":"cameraUpdate","width":400,"height":300,"x":1,"y":1},
  {"type":"rectangle","id":"s8","x":256,"y":102,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"delete","ids":"s4"},
  {"type":"cameraUpdate","width":400,"height":300,"x":0,"y":0},
  {"type":"rectangle","id":"s9","x":256,"y":74,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"delete","ids":"ap"},
  {"type":"cameraUpdate","width":400,"height":300,"x":1,"y":0},
  {"type":"rectangle","id":"s10","x":256,"y":46,"width":28,"height":28,"backgroundColor":"#22c55e","fillStyle":"solid","strokeColor":"#15803d","strokeWidth":1},
  {"type":"delete","ids":"s5"}
]
\`\`\`

Key techniques:
- Add head + delete tail each frame = snake movement illusion
- On eat: delete apple instead of tail = snake grows by one
- Post-eat frame resumes normal add-head/delete-tail, proving the snake is now longer
- Camera nudges (0,0 → 1,0 → 0,1 → ...) add subtle motion between frames
- Always use NEW ids for added segments (s0→s4→s5→...); never reuse deleted ids

## Dark Mode

If the user asks for a dark theme/mode diagram, use a massive dark background rectangle as the FIRST element (before cameraUpdate). Make it 10x the camera size so it covers the entire viewport even when panning:

\`{"type":"rectangle","id":"darkbg","x":-4000,"y":-3000,"width":10000,"height":7500,"backgroundColor":"#1e1e2e","fillStyle":"solid","strokeColor":"transparent","strokeWidth":0}\`

Then use these colors on the dark background:

**Text colors (on dark):**
| Color | Hex | Use |
|-------|-----|-----|
| White | \`#e5e5e5\` | Primary text, titles |
| Muted | \`#a0a0a0\` | Secondary text, annotations |
| NEVER | \`#555\` or darker | Invisible on dark bg! |

**Shape fills (on dark):**
| Color | Hex | Good For |
|-------|-----|----------|
| Dark Blue | \`#1e3a5f\` | Primary nodes |
| Dark Green | \`#1a4d2e\` | Success, output |
| Dark Purple | \`#2d1b69\` | Processing, special |
| Dark Orange | \`#5c3d1a\` | Warning, pending |
| Dark Red | \`#5c1a1a\` | Error, critical |
| Dark Teal | \`#1a4d4d\` | Storage, data |

**Stroke/arrow colors (on dark):**
Use the Primary Colors from above — they're bright enough on dark backgrounds. For shape borders, use slightly lighter variants or \`#555555\` for subtle outlines.

## Tips
- Do NOT call read_me again — you already have everything you need
- Use the color palette consistently
- **Text contrast is CRITICAL** — never use light gray (#b0b0b0, #999) on white backgrounds. Minimum text color on white: #757575. For colored text on light fills, use dark variants (#15803d not #22c55e, #2563eb not #4a9eed). White text needs dark backgrounds (#9a5030 not #c4795b)
- Do NOT use emoji in text — they don't render in Excalidraw's font
- cameraUpdate is MAGICAL and users love it! please use it a lot to guide the user's attention as you draw. It makes a huge difference in readability and engagement.
`;

/**
 * Registers all Excalidraw tools and resources on the given McpServer.
 * Shared between local (main.ts) and Vercel (api/mcp.ts) entry points.
 */
export function registerTools(server: McpServer, distDir: string, store: CheckpointStore): void {
  const resourceUri = "ui://excalidraw/mcp-app.html";

  // ============================================================
  // Tool 1: read_me (call before drawing)
  // ============================================================
  server.registerTool(
    "read_me",
    {
      description: "Returns the Excalidraw element format reference with color palettes, examples, and tips. Call this BEFORE using create_view for the first time.",
      annotations: { readOnlyHint: true },
    },
    async (): Promise<CallToolResult> => {
      return { content: [{ type: "text", text: RECALL_CHEAT_SHEET }] };
    },
  );

  // ============================================================
  // Tool 2: create_view (Excalidraw SVG)
  // ============================================================
  registerAppTool(server,
    "create_view",
    {
      title: "Draw Diagram",
      description: `Renders a hand-drawn diagram using Excalidraw elements.
Elements stream in one by one with draw-on animations.
Call read_me first to learn the element format.`,
      inputSchema: z.object({
        elements: z.string().describe(
          "JSON array string of Excalidraw elements. Must be valid JSON — no comments, no trailing commas. Keep compact. Call read_me first for format reference."
        ),
      }),
      annotations: { readOnlyHint: true },
      _meta: { ui: { resourceUri } },
    },
    async ({ elements }): Promise<CallToolResult> => {
      if (elements.length > MAX_INPUT_BYTES) {
        return {
          content: [{ type: "text", text: `Elements input exceeds ${MAX_INPUT_BYTES} byte limit. Reduce the number of elements or use checkpoints to build incrementally.` }],
          isError: true,
        };
      }
      let parsed: any[];
      try {
        parsed = JSON.parse(elements);
      } catch (e) {
        return {
          content: [{ type: "text", text: `Invalid JSON in elements: ${(e as Error).message}. Ensure no comments, no trailing commas, and proper quoting.` }],
          isError: true,
        };
      }

      // Resolve restoreCheckpoint references and save fully resolved state
      const restoreEl = parsed.find((el: any) => el.type === "restoreCheckpoint");
      let resolvedElements: any[];

      if (restoreEl?.id) {
        const base = await store.load(restoreEl.id);
        if (!base) {
          return {
            content: [{ type: "text", text: `Checkpoint "${restoreEl.id}" not found — it may have expired or never existed. Please recreate the diagram from scratch.` }],
            isError: true,
          };
        }

        const deleteIds = new Set<string>();
        for (const el of parsed) {
          if (el.type === "delete") {
            for (const id of String(el.ids ?? el.id).split(",")) deleteIds.add(id.trim());
          }
        }

        const baseFiltered = base.elements.filter((el: any) =>
          !deleteIds.has(el.id) && !deleteIds.has(el.containerId)
        );
        const newEls = parsed.filter((el: any) =>
          el.type !== "restoreCheckpoint" && el.type !== "delete"
        );
        resolvedElements = [...baseFiltered, ...newEls];
      } else {
        resolvedElements = parsed.filter((el: any) => el.type !== "delete");
      }

      // Check camera aspect ratios — nudge toward 4:3
      const cameras = parsed.filter((el: any) => el.type === "cameraUpdate");
      const badRatio = cameras.find((c: any) => {
        if (!c.width || !c.height) return false;
        const ratio = c.width / c.height;
        return Math.abs(ratio - 4 / 3) > 0.15;
      });
      const ratioHint = badRatio
        ? `\nTip: your cameraUpdate used ${badRatio.width}x${badRatio.height} — try to stick with 4:3 aspect ratio (e.g. 400x300, 800x600) in future.`
        : "";

      const checkpointId = crypto.randomUUID().replace(/-/g, "").slice(0, 18);
      await store.save(checkpointId, { elements: resolvedElements });
      return {
        content: [{ type: "text", text: `Diagram displayed! Checkpoint id: "${checkpointId}".
If user asks to create a new diagram - simply create a new one from scratch.
However, if the user wants to edit something on this diagram "${checkpointId}", take these steps:
1) read widget context (using read_widget_context tool) to check if user made any manual edits first
2) decide whether you want to make new diagram from scratch OR - use this one as starting checkpoint:
  simply start from the first element [{"type":"restoreCheckpoint","id":"${checkpointId}"}, ...your new elements...]
  this will use same diagram state as the user currently sees, including any manual edits they made in fullscreen, allowing you to add elements on top.
  To remove elements, use: {"type":"delete","ids":"<id1>,<id2>"}${ratioHint}` }],
        structuredContent: { checkpointId },
      };
    },
  );

  // ============================================================
  // Tool 3: export_to_excalidraw (server-side proxy for CORS)
  // Called by widget via app.callServerTool(), not by the model.
  // ============================================================
  registerAppTool(server,
    "export_to_excalidraw",
    {
      description: "Upload diagram to excalidraw.com and return shareable URL.",
      inputSchema: { json: z.string().describe("Serialized Excalidraw JSON") },
      _meta: { ui: { visibility: ["app"] } },
    },
    async ({ json }): Promise<CallToolResult> => {
      if (json.length > MAX_INPUT_BYTES) {
        return {
          content: [{ type: "text", text: `Export data exceeds ${MAX_INPUT_BYTES} byte limit.` }],
          isError: true,
        };
      }
      try {
        // --- Excalidraw v2 binary format ---
        const remappedJson = json;
        // concatBuffers: [version=1 (4B)] [len₁ (4B)] [data₁] [len₂ (4B)] [data₂] ...
        const concatBuffers = (...bufs: Uint8Array[]): Uint8Array => {
          let total = 4; // version header
          for (const b of bufs) total += 4 + b.length;
          const out = new Uint8Array(total);
          const dv = new DataView(out.buffer);
          dv.setUint32(0, 1); // CONCAT_BUFFERS_VERSION = 1
          let off = 4;
          for (const b of bufs) {
            dv.setUint32(off, b.length);
            off += 4;
            out.set(b, off);
            off += b.length;
          }
          return out;
        };
        const te = new TextEncoder();

        // 1. Inner payload: concatBuffers(fileMetadata, data)
        const fileMetadata = te.encode(JSON.stringify({}));
        const dataBytes = te.encode(remappedJson);
        const innerPayload = concatBuffers(fileMetadata, dataBytes);

        // 2. Compress inner payload with zlib deflate
        const compressed = deflateSync(Buffer.from(innerPayload));

        // 3. Generate AES-GCM 128-bit key + encrypt
        const cryptoKey = await globalThis.crypto.subtle.generateKey(
          { name: "AES-GCM", length: 128 },
          true,
          ["encrypt"],
        );
        const iv = globalThis.crypto.getRandomValues(new Uint8Array(12));
        const encrypted = await globalThis.crypto.subtle.encrypt(
          { name: "AES-GCM", iv },
          cryptoKey,
          compressed,
        );

        // 4. Encoding metadata (tells excalidraw.com how to decode)
        const encodingMeta = te.encode(JSON.stringify({
          version: 2,
          compression: "pako@1",
          encryption: "AES-GCM",
        }));

        // 5. Outer payload: concatBuffers(encodingMeta, iv, encryptedData)
        const payload = Buffer.from(concatBuffers(encodingMeta, iv, new Uint8Array(encrypted)));

        // 5. Upload to excalidraw backend
        const res = await fetch("https://json.excalidraw.com/api/v2/post/", {
          method: "POST",
          body: payload,
        });
        if (!res.ok) throw new Error(`Upload failed: ${res.status}`);
        const { id } = (await res.json()) as { id: string };

        // 6. Export key as base64url string
        const jwk = await globalThis.crypto.subtle.exportKey("jwk", cryptoKey);
        const url = `https://excalidraw.com/#json=${id},${jwk.k}`;

        return { content: [{ type: "text", text: url }] };
      } catch (err) {
        return {
          content: [{ type: "text", text: `Export failed: ${(err as Error).message}` }],
          isError: true,
        };
      }
    },
  );

  // ============================================================
  // Tool 4: save_checkpoint (private — widget only, for user edits)
  // ============================================================
  registerAppTool(server,
    "save_checkpoint",
    {
      description: "Update checkpoint with user-edited state.",
      inputSchema: { id: z.string(), data: z.string() },
      _meta: { ui: { visibility: ["app"] } },
    },
    async ({ id, data }): Promise<CallToolResult> => {
      if (data.length > MAX_INPUT_BYTES) {
        return {
          content: [{ type: "text", text: `Checkpoint data exceeds ${MAX_INPUT_BYTES} byte limit.` }],
          isError: true,
        };
      }
      try {
        await store.save(id, JSON.parse(data));
        return { content: [{ type: "text", text: "ok" }] };
      } catch (err) {
        return { content: [{ type: "text", text: `save failed: ${(err as Error).message}` }], isError: true };
      }
    },
  );

  // ============================================================
  // Tool 5: read_checkpoint (private — widget only)
  // ============================================================
  registerAppTool(server,
    "read_checkpoint",
    {
      description: "Read checkpoint state for restore.",
      inputSchema: { id: z.string() },
      _meta: { ui: { visibility: ["app"] } },
    },
    async ({ id }): Promise<CallToolResult> => {
      try {
        const data = await store.load(id);
        if (!data) return { content: [{ type: "text", text: "" }] };
        return { content: [{ type: "text", text: JSON.stringify(data) }] };
      } catch (err) {
        return { content: [{ type: "text", text: `read failed: ${(err as Error).message}` }], isError: true };
      }
    },
  );

  // CSP: allow Excalidraw to load fonts from esm.sh
  const cspMeta = {
    ui: {
      csp: {
        resourceDomains: ["https://esm.sh"],
        connectDomains: ["https://esm.sh"],
      },
    },
  };

  // Register the single shared resource for all UI tools
  registerAppResource(server,
    resourceUri,
    resourceUri,
    { mimeType: RESOURCE_MIME_TYPE },
    async (): Promise<ReadResourceResult> => {
      const html = await fs.readFile(path.join(distDir, "mcp-app.html"), "utf-8");
      return {
        contents: [{
          uri: resourceUri,
          mimeType: RESOURCE_MIME_TYPE,
          text: html,
          _meta: {
            ui: {
              ...cspMeta.ui,
              prefersBorder: true,
              permissions: { clipboardWrite: {} },
            },
          },
        }],
      };
    },
  );
}

/**
 * Creates a new MCP server instance with Excalidraw drawing tools.
 * Used by local entry point (main.ts) and Docker deployments.
 */
export function createServer(store: CheckpointStore): McpServer {
  const server = new McpServer({
    name: "Excalidraw",
    version: "1.0.0",
  });
  registerTools(server, DIST_DIR, store);
  return server;
}
```

## File: `src/sounds.ts`
```typescript
// Pencil stroke sounds (ElevenLabs AI, -30% volume)
export const PENCIL_STROKE_SOFT = "SUQzBAAAAAAAI1RTU0UAAAAPAAADTGF2ZjU4LjIwLjEwMAAAAAAAAAAAAAAA//tQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASW5mbwAAAA8AAAA6AABfgQAGCgoPDxMYGBwcICAlKSktLTI2Njs7Pz9DSEhMTFBQVVlZXl5iZmZra29vc3h4fHyBhYWJiY6OkpaWm5ufn6SoqKyssbW1ubm+vsLHx8vLz8/U2Njc3OHl5erq7u7y9/f7+/8AAAAATGF2YzU4LjM1AAAAAAAAAAAAAAAAJAPMAAAAAAAAX4HbzQDDAAAAAAAAAAAAAAAAAAAAAP/7kGQAAALqXUxVBEACNyfY/KCIAFHBiU/5hAABGhho9x5QAsAPtIEAAAkQAAWAFeR/qfyEI3/kOc7//5P/+c5CEIT9CEIRpCNq/nOHAwMDFgAAAAAAAEJyECCCNIQhCEqchCEIQljnf/+QAAwMDFuQAABAsDAwMDAx8MPDw8PAAAAAAACUBgAxuAAAAGMYxjGMZCEIQhLI387//+Qn/QhCE//yE/zv/6EOc+QhCHPIAAAAIwAAAAEVMW8zMOrxM3L331NskAAAGAEVCEqga+9iarkM5ssCjNmRRSA4KtCMSUI4UDowGylgYaHJygeAwPgMpg+Egh2WIzNZrh+ZBwAZBFeBUceVY1x0U0ju+fHPRlwNLLomrzLFGSjuokzZV/sFQ6R//yozmLo/r/4RJfm/n7Ojb//tBj1j5//6gkbN///xVmGtmU6bbkDkkjiaaDADAgAC8Re7IGEH8HXfet6p850Q5jZct2aZzNSY+TqwR1BL7sG1NV9HMm7zNb/40f7zbaF/UP//7Fkv/9Qldol1F0iSAAAVCuKM0z5LwpyDMP/7kmQKABQkXdB/PWAANouZnOEIABFdez/GCXNAxK2lEGCVeBvMxcXBKTM7JAYaKFpLokI22a2vTOyts5mOpXh1NfUtfKy70j381/H/3qPfcyWRvOLMi/4m/+u/hWzyAWhyBmeRR37b+KNHHCDUVNEGz8ur3n+b5jv/46a2ITiD5NRJwmKSMXm0QuIMxcEIFbv+THEEgU2Q5aAARIsQ0GrZntf0pdXZf2/mRla/uj6qXdN/+yy/b//3+4kxnIi///BA/////4348F8BGFRHZQRJAQAtBiSCgB3R7jOx0MSLhHfKyRfAugo9ypxjjHMuHAyIdNFd5RDzyc9hA1vkRlJ2Yd6OlCZtZ1Va+7eubIf3viP7otEQIIQQJFQIVtueyZ3HGIGBiqSi0dp997mWe2lmroR3zHx8qUbQmoTiokC8nhYvJBIIpIeQRSNJqcLgSPNzh7P8OAQGgAFRMc4YActZZ07wc8k/89/N07/unT2/+bxn///+FBfwz//C4Z/////wuFfgDAFylNs2RggAAG6oSfByHiXczxmNqZVe5XU0dyf/+5JkDYEUZlzO6eZdwiqAmVkYJhASNXcnbD0TwJiBI+BTCABNzm9RqXlmY7ZeVrDrZ+dDo3y/SRFbml3fuqWUxKh6L2gvxc1jPe5VyXSVeEq2Zdsdtuq63bf+yoCFFx6CkkFdLutr28QcVYeMStk2fbTt9NimQ66//+tzWPULqRTZRsbHSBYjZArDcFiXRbarAjfQ/+5AFKYAAKFLoKsZaZG9hZaq2UPcWZ60jR3/PyGv/zTBzOP58/dWd//lSwjBYDyACF2JWPOslrEceUGuDPSBr16HJxt6WBblNKaKJWss8dZks+tvOIWH2LeDWsR7CsQZVPrbrutXs1pYufbFrbgxdUWs1paNv2gvceuN5tWLjFt11//i2//bKSCPHlW1c0AGAWFmi15FTRg+HB05Rg8k2vmtaZrb/1r2/212CUIVB0KwSAKdRTMLOdIrdFQV1AAYISFAJzAKHngojW7uQrxMecNQ2PO/4d6l/+t1n9Yb8lv/+eUPHD4+lCDYCDI7JWNyEgy7kfHhlrZHFnYvWjw2MBKErDRDUIPl9CVmt5qi//uSZBUABDlExAVpgAAsoJhpowgAFLmNLbmFgADml6QzDFAAVf1vug5qMlE8CJomLhlTKFJJ33mtqpKIe7lVV0qHv35ClPW2SmSqLq+6eTXtP3+fQ77NaXTzpj1Kk1Onn7/Tq1v2V3kQYEscwfY4OsYHrDIFfKkZJQ/kqDDHIUiLgIrMjLVQUA0ivvSNOewbRX1sRZo3Ir67dn0+Y977mo6tjm8Wc6vbv/TsWv+9A37t2ydSFsIiAJAkAhmzWFruItB8aRnAgdBxpmRFT7fqm6xuDwIARA8LB/BZRBQPIHjYEQhiEQe/NEZeO8QCZPSY1pw3OIlypLJwDwbgTL+bdZ90VDFFQ9nCK+kGnO4331AJ5LNDQ2Ozft6tT/f06WEZQPBHIMjgQAig7iuv/j+/q4jYaGpDgj7yEN44//v//43/3ur++oZSkmgIYOwcc/////x5QAIlJEABiDQAAAADe+gW5MXK51naG5P5DN7mn7qRV2avP/+u5Adf7/uCf/LixRY//4fHOOf//HGbt1W26O3Ru22SNxuJElEsgfrGfZpzof/7kmQKAAP6YdduPQAEQAw5u8SoABDRd0WcxYAA1K2mU45QAA5IUZO7beq92dh+JgG4uKC7iPY8UD4gF0GB0KMLiGwcH4dMMcXrmWPKSxbFB45hS6gxKhOkeKUcLnKPtnHNnccyo+V5vyEhf6z4ma/gdFTPpH//GvP//Nss/f3n3sOSHr3+YSi7RO///ktCRIm46w41CQAAvAaBUID18/1mqyedVDO5jzLWZKGNSn6Jq+27LXPVFdrL////////l//8t//////i8RA6ODv/hx2zbwxyAABDSloqmYDiAZg1MwUOo1xBUl2jYoveqx1npY581J513NzNVXJxeKhjTk3bnK3LY+v/3fLJuaml2xccu4dEPbumuL91gjEPzFGwg+tGXy9RziBRaQD05qHsPNnmat8u7231w7p6Ry2QqHk6Q48vNwgcNzQRyAEJ6QdBE/rBY7SiRcIASBAUB4SFY2ORLpc7trNPo31T6aY3/H///9X4/Hf////wA//gHDQv/////wzDQoAIbDIWN3R4eDYvUADZrG6LUIwZaIQBbDkLBlj/+5JkC4EUPmFSceZEsCxAacsERgASfY0/h5lwwMUvJRRxHXiLYhjKi1zLGcEeqHs96y/BWKsr2m5XL++lj7tsZxm5nHKyhcf/w/l6C7krmlHvdM0tC1xp/1KcgIh8tDLHgBh6ko9JI9FdjzmIOxZoHczXP3PWVXXNJq0qc8ECCbIuA8HCwik4YWKJOrQLXcQHY2polAiTLCUASghwIDoMJXDFQ0fc1nul3foz/3Wv//bazqqaZTr2/4sqQaKwy4IKlgttHLAIEnqtJoLChqHGeHUhJ1K7bM5SuNN6wqj0hYNvrZmr2HrxLTtUs4HLHtYVMayuD1HLSTtxdVzcsdeobdonUj0vOWea1bOuSe+r769p1xsoEjp04Hoig5NKc22pJWpfIYjpRbTdrnJHfh105yLdyXw6msc+D00VEMwnZsisb8lA6g+jpONRtxsei/SMCVId1QQBCJBx8TKk3Wdeo3f/X4KN43gIP/if5b/lP//E3/y0uNPLlYf/iDh3/+X//////xBVBIjyiUgAAEILgiQ6SWluXJbRXzmTWkCcybpv//uSZA2BBAhZy+HmHsIwK3jlDCJMEB1lGQ0wxsi4geIYYYRAUdggSQrW3iFbW/i1cVrnEbNYNbQk8SaNrdLWr15NNmmSeTZyfOS8zOSjnmzZic7AwVsz6qt+N2p4JHoycCgEAo41b5mY2fU1rVVU1Fz/6eqlKTFGarqsPNmYMVFDQUKhBqs3jTb6ARAAMEAghx8eW28pWc03Xnf6eD//8GA3lbzdfwYCA/wEB///xsb/4L/+//////BjAEMAAwsACpS3ZEDvsNnE+hsPg68ZABDLiShDBYvBpIkS3UtLvaTLtrEhtk7SNJpUkiy2tFHXn4c2GxVP5pKnjWrZpiyJvd1kj309l1rxXb27lzYBhcmjaNg5605cMb6RNS2Gztut9r/+u89+dvivP5W67xKKW0yeKtBRe+pl/5eKH+sqqkTASHGbA8xt7yKtbXvVcihPqfojOhJHuJOBq74SU4qKVYoIjrOz1Wf09aoEpxlAFyCabfpES5VjZF8u49MJa48b/ctROet2GuZ0XZTSX6KMNHxFek3Fni5RhCSL0WL3LvFUL//7kmQcADQhXcgjCFxwJeBYkSTGABkZpTGHsfOAogElYBEIAGklheNJicgwsYAHPiOHu39Kfir9kbK/hMCMazRVw/vN1Dpvegf5NzeM0OrH2Sb3CFVPL4Z/s9kv5in3L0z79CrYynG7qN7VN5+oMfWgA2WAIoAHQG97OT3s0UyEuQZwx5P7w//f8+2cD85k1vB/vo/+HwCkyRFYkCguEsr0yrnBkVlYUCFLd+r1fCsuC2N6IRpzq6jCxQf0XveJFhLsojMDkOB8krltfGspW+OFQsOKTag5rWGHEMS0bEJxRijjRfEdBWG0EQSGggOgHAYzGVFpbtDvCsiSRbZb54eGdSCYH4rDQNBeP8ciwyw1G9c4N37hpRw1MpU1HkmeQokJCJ4ajkQx5Egz4hueZNRMQIFPEUjiwLlmah8HAUZzEEPBbCGB1lvNN4dhdSbxGNkvI4a374v6a3TN9wJtqFMASAAmTBH+c/+zyjvnG39b//eQVdziJT0VtgBV9VaHhiIAiTJhgMKqBwUMWsgxlSoRpTdpNhEMDG/C2SkkOL/7i2L/+5JkDQE0U2DPASN8YC4AeZQkIhAP1XVH7A0RwNit5VDwlPhTDtV4cCKdYNyZtSL9bmYCPI4PINm17D0/k9r2nx90zbW/ArvaHZIDs64d8LgYeprRIDRNLTHhZQ1TohGZmf0yvXlt/D+a0vfV8U/3jE0LeJFezG8+YTpSStQ0/jzQxneKRD1PSaPPAvMCcKDHWKVE7hRIAAOHRIujDHyDv//+gCHwIEWf0WnA+z/QPdT0bWgSnjlrXN9pwQNPjiDUvRFw8zDipxIg44Zuazg6rQ4FaSsth8Nv7EpxdcmoIrD1aV1aEUIYI8C9CgUBBkVVg6xQYcMVsFP4coSi3016W0pT8dkZxohYqLMiz+v/6/cDQ7Z5SGrR177dBqVTV6j5T66v9Y/i+Y9udhDPHlCYRhQDyQeB0LiEYIgoNelDcmoDEEABeWZrFgV8u5rTIueXLO/1V0xv/8f//6Xr8d////Cwv///Cwz/////w0MhQYFhgBgGG4VVVuvtONKAAK4eEA1E8ZZxByJ8/w/CYzoYnVwYLM3QVOwOUKE89TZoM9my//uSZBUBM6Zc0eHjVOAuIAmoCEJuDoF1P8etE8i4FSaQMwjYbCBjYaw6FhqYx5kop3MjKEWXnuLU0doBFVvnnC//NGQYicY8ZHjUdf9aqeYNThN5ycz///44Oi8YHi4ccThsFyMB0ZDMag2Zmf+sANDYAFwGp7nC9Ei8OWJR8/dXl38n5RjFBP/5256vreKOaj/2VChByg6gBCz/1AqACwoGjICcbF0O0tg2YYagdGTucjpPhH0T0GRPRmasHVos6orwkedF+2oPc7hjy5J0sNrb/3TftrZfU1U0dPTE1weRal/09vFz81/ywiCZs05wscv/60pqkmySb/tPTT8x/+tf/8MDx0rkjjqYWooo4o6KAQLmH6q0beDcAvJpSoWZfjiGdVpN/f/2b+v//o8wMayevCP6gNq+z//9T9iL0hQZegAAAABKl4MSepaS3wsEu6LFgoKm/EU5Jq1CUGUZys2uLfttYeiYz//UVNYkWD1teuGv/Jc3/X5+eaKuYutv/2Zr6aP1X/kcDw9f2aL+/1rKOFl+xkFqXSeRWBQ0BREsJP/7kmQxgQM0QsrTDEJgM0C5GwgpIA3A7x0smFFImgEjdCEMACUzUVAAEAKQBCXhQEtAGZaOlQEmhQajV+s6kYHbFbdLflpVIqAgqEgq/6Tr5Yr/9rZbGPXnf6Qg+UgAcNA7rwqgWXKG5oKq/gVtaaCIFdvdnWMxJcEGoqeTogbYKRQ2P92orliing64fYKK+ZuxeNbR6KajrlHu5GJdnViKD3Z/uZysrDwX9qNoCwYGxeksb80/FLW9S3xlACIq0CbV07yv/b3+PCSiUjjbcicYJxQ4AJgu65T9T996N2jVd+Ovb/W5H/43/+no0P3aqgyyzwxIIIjsDlJknF+NBVamUbNNijAIwaZP9Mc9NLsy2yO96em0egAMe297ZhDOyGftDk9ghkdse7aNjtHu9f/TED6Q3xEHpxBGjRz9MZdo0bwEAiBASShAKBhkLhtYNoyMnbm9RAjekKFQ2kSZ4QheqIEDdKOn5yQNqMWuj3+ZwKAAMAHHyAkAcfCgyBtoUIIsWPzLhiPNI5//0BEW9BABAsW8w97GPTIvVuOM1MlOT5z/+5JkWQBk3F/L4eZM4ibAOPkUwgAbhaM3J78XyIoA5qwhCACXKOz/7//Lv9P/X//4OBhKBE/8lhSlYyGWuEIfLh5DXlMpUPO54X07ZUNHACEMlVl9kf03iJ2V81MrDItQYsCSWr7T6ZEx92WaNLo000yI6REvWdGI57eJpuzJise7bnMdTqY0FQj46MSUWPuBFolT4nXCGRkMu+gS/UXKYL4LWEDHsXA2ZSxjkVh7uZJHI6mezWq4DC2KNLrKGk7ZjwcTyRkzNKm1Y6lYn7JIzSsMzPMzM6ueTFwVpczcJwXBriyFLHIS9XO8yz2rBU5FJ1XVRXTWeSWRmhjcalkrvXPvXrtPKKW5fvXKa8+M4uAEIGHFvE8p///19H/0f/22pw6H92KiDZ/oWhQDewSBgHw5KfUrkZNQY+L4jrypAg5kq/aWiOKtW9NsVFl8TAsDNTKu1Jh62YvrH8Jwq/dXNdY1BeOXrGINnNjG8m3KkqfHcnFvWExODg6uPNGmFydZ2sSQf7/ef/2uqyDcuijlQT/u2JVJKEEKEYZQJDbUbtEj//uSZDeAFLNfUWHpffAxIFn8BEIADclvUeeM84jfrqcQYIi4SFA9pwg2M59H14czrnBpQWBJhzYWFRxIiKGPmVFOL+dkx5Ln72yNYVRhqi0EAIRwQAcFLWpnL69z8FzlR+O7EVL66wmHBscv/1Q/2LvMqpv/8bkiCzaxCaWJiLmVddUygEDuMQcqVLeTlNFuVB6IaoKSlubmJDpX6htSW7mDfB0AMWoSrs0FwXKQe9XsNug1V1k+T/10peLHEpQNa3dOKn/mjqDDmuqG3f9WmKrrWdbdmZDrt2bock4wkKjZQ1XOCMshpUiVUAwNSAPddBaJpUVNout1XSv32/0qN///9cGC4P///+DxsYF/guDjggGBf///8b4HGGBAYGPARwYyd6aIiCZbISgEB8C6k4F8hwjw3jjM430yvWkOoEiMSZZUlLNep6si8NpFHbZ3LqqjAqFtfOFz6djVa4Rj9tas4gWMyZWbKh3It6aaQ4xkdsxv/Q1Zn/bXMYtKPzTFRFKAlIcBEghzgIY4xkqJ/ygcZpIqAKYkAaWA0qtPMvods//7kmQ/gBNtXFJ56RNiLuBpqwQpAA3VbTOHmK2AtoDjmFMIALNM96W3/hRP+zjn/nlqJho99Z3+thUBDgKBToKhonNaxxcAAAuxBieDqPsXE5UAa/QaMkTcIkOKhI0I1VCiXiikqLIozneSKLHTJoSj5jZL6lL0MIkAYWxEpW5crGEg89S6CRjgMBhYyl07iIrmqxnL9SlZ/rlaubeX/KbrzMYxWMIh0ok4yBhx5lcNAEgCEh4KC8NSL4NkZ5jwMVdwaQz9Tqh5360nZ7ULHulhZW1GWQlP9NH1crRGIgAWAAA6DTqfVwPFPominPAK0nkiEAyKnuW52Wg6hCjAzMDlK48b9Z1yVUvU0tt9Slis3LLVjC4U51PiZvp+4sbNdrVLysG2PiUmOoqY9eb+nzeb3Vdqd7aE2n5/ip5v9P1n1539Z5XgZiMXRXef7twf5VVVlCIooEaaoRWk8eSBn3PMnZL0Jme/mVK/qV1+kwzpxtFqku/19Hiirf9gEqLA1FCAAgAB02IGvCyUygMwxQOeDCkMEJmJep2JntKnpy+27bL/+5JkYgADf1pFxWUAAC3AiHakiAAZYZkVOaeAAGUBYoMKIAAI4ELFCa5wRsTHKdh1K5rSd2BuZUUcrpQs5c2AkiLR6JjRkLS11ytQ1WrCxoW1tCvbFc7zAgSyzPGmIckNjerLg0MbPrOfCgR8P2SI/Y3r+LNeO9pFn1eI5t8R6rn8dofrDw56oe1qPdI0Gn17a1ivf5m9syzrK25qxPqM43Nzvmu943/871v6+qVvmur31/nPrRRueFZYkifdur9vutP/5D/+oIEQ8LC6nnqj8D7YY6UH9fT/o///9n/////Tuu2//2/10smijUJiMQACWmJlLBBJ0l0R3SAV16M4SRQkK4buWnUmOib182uoS06SYcw/ix3MQBodmLNDUrYRD1HE3lYOzFnbaYxCdVlXExCA2UP9AlPE4ZsWYnIJFACX5a4mIqvKIneb2A60R7qWSq/PbgB8rb51aau8kguxyOSSPau01jHbxvPJX+UscNx3/k+O8s5XQ1c+Z4czkFV9KXBv0kGd0sBM4cilv09/Pdalxu3bW8e5YVKs/rPmv1ef//uSZGAABxZi0e5jAAYhBMiQxrQAD2lzPf2EAACxASX3hCAAe7flDkuWt2WUksvX79JYxtzcptwq7cpLeWP/+qmNbGjsDpw0RGYLWJEuz8ZqlLdM38+cQW++W1NPzpz8if/IuRP/waEt2aYY2SNoAAAkCkAg6ZBsnfByHEeKBXgh1/3muR7dnRxfFVNiEXNGI/ysRCR62c7joqIuWKam0Yf9VPz1TrGwvFcT9zwbV8JN1392owAYKKesDT0x8TN9WwyRe8brcxYyYXfrb452lZZ+TobjuBUgoIJMFhYwWBy7/5AROZwx0oAAAUBgIHOGAlHal9ss+f04eb6rv/1/qGdqadT9Ucv9TSOU3NKCppUWllaYVUkSAAAnPUJMR7MMkhSkbTQaG56i3p/PzIjMx2nEQOgUYkfKbnkDYz5R13J7sWi0XEfy/wzshZpX9Z6797pCSsctJ/OplN+l4u5a5/FR7TUXDRCab1l44Oy1sOzdjjqDqRXe1c49ysRe6f/4rYfjhtG8woqomPYejoD44whkTd5lozyf0rApMylbhAAAEP/7kmRJARRMXM955lxwM6BpjQQmABAteTvnjXOA1C4k5CCJODMOakgtTUXo7EqW3bXNYW/6m3/V/DAWdFR1zZQwBI2lFvfUETxNgPhhmNeawqO6Ax1EhGIUQtsFoONQHc5nblifrlJ2cv8ZduorjTK7uBwUU7TNGHM3sOWdLUmXOrdSXct4FKghgQ99s6UOlyGwl3tqKbRuA5Mozq7HPjuWuc+rdrOPtNocfOmLqceZ8zN9cwfYsm10NPOe9hx6pJpEEEdOsUrMSSzS2WGnstmBgOqoCBOcebXvZbv+e8Wv/0+v///Amu//tb/+DG/4MbBcBgMC+BfG////BAwEBggICBQYICWSR3QswAAAhDGZaOLyfZxsLS8VqpUKsXLKkZK2srRIQOImQYKEFdChyMpiqCK7f7N1CFBSnGNiYGJFEg7EF8d0MT/apCqEHOpmEXft2okEAUbnHG0EErGy2xXNbdJerWmWSy59u1rr1PhptZqe7o2ntyJqHk6aorHVTR8OwnAoxEr97wAGggAADIWGTadwkNHRfdYRXpofljuslfP/+5JkTgGEGFpMYeNccDPAOPkEQgAOwW8dZ5kQgMiBIlQxCAAPXJmqhYNXpdsfWIa1+kzYBHivq7qthpQliqwAVCUBAg4JwLo9ha1KiRlDnLGLQX1DUJc1QfqN0qY79xkUh2aiymXdb01zt3NNd9TQ3Kto9YslLJFRU1h9McSKkqq1z+lrjAsTWNp1j4joabcXalBFNf8R1/ERwPmL//4u6k1uGWr+59ZFXiydUFpmDlqWP/+wKIOEcEbWC1xuiyvbj1ltwaqsFn1hlDkgERBOSVLB0RErCREWhoOlgaN+1taf/+FbkSoAKQAAVmBtFIhRS1XhWvFqywZ4KKCwsHpTUj9BSzjLEDsr/fbvZ5nyHBKtoRoAfTTtB6qoQEgIgu7i4Dt7SlRCxHxDd3D1zFtaRZwUUHyXfS7/Zmr2O/Ft/2v4LF9tec4N7cK2r/I9tvz5zfO3/+gmQyQD/pWFgCPBQGxZ9IAX6ZXe1V/wlHrm2882h21e2vUgWR+dUmVt5lH91SLP1vs0LVy0QQ0QRIL0ZhzxTpUpcDDVqkStmaV5WOxT//uSZF2DA3UxxUMMGmIxgAicDEJvDyl1GweNEUCwgSGkIwgAUIOEsAXi1CegonCqGEEWi3qb4u70zukgLnjWYdV/NWwpy92lLkEJN3aJfN5bPA04BQ3m7hBskKLxZCvfVQL2QiJ9oQOf9+5fr5H2g13ikqJimSiByDRd5LB8Dwx+/QCrVSys1BDTjZwuVMDdCtAuVRRYrf3e6u7t6u3qWPe5tDf09no+hAtN6v3eigYUkbU4kWU0QgvBvqIFQeNXJ7HiM9MwmNz2p1QToJQh7yV5qRkcFe/6H7L4WNMOmosybJpMMqUGZfTGJPP2rwItXjwcjgnHgyrxIOdJ+WYT3u5eojlQzD3XSUOi2k2gESMdfLnRJtMPce9KLlaVjJAhqtvB8AZAWkRrs2racPAnZ3EBOKraXtUKRxQuyfak4YYB2SdqexmQ3zETZkHQsXqh9y2LlcSRF9FHKjkwpX7+SQ7yDhI0II2GmdiAOsmY2yGikM5oH4y6gRY1Gd4/iv4GrwImK3xrOMPP2QIFKhgAHgZSYMeJ80f//91IYL1///8EHf/7kmR5gDbjaMtp7H4iHsCZCBgjEBdprTOMJfHIg4ElEBEIANvIH4R///KVFRJstMkJaR0K2MdpZZK6seg6zVlGp3kr3q3QQC1qDklCUmJJy/34uYYmXkyufMHptr7cPDvv+3pb7SStB289v6b1wWDChERoxEwhFUSJdMuFyUSUvqtIKHw7SQGhQpEAFoba0WzyKXK1LQ6KdaXKRs4Xuu4qsU6rxjFnsqvv/CgnVCVmoLWx5cKO2QghbGR2bJ9ro/EyyC1lOLuL5hE6E0jmAYxOUNRSENTOpEZak2/7NTh8/7p74/3E1OCGKghrEsNBKH0ZpeFlf/xYN////4e//81/yZyXSomweqo2R2eXFkoIAIAEiAuiNBzpl0aLMwppRLhSRFg8n81K4Z3quvFhSQ4kBlcqbt/3OHFGAHFkT//SvSlKvCqTvBDjLWLQ4Sv/g+kTz+E3slswqHOlpabc7/6qa3u4LbKLv46+q/yu++ZqG/JdbS6YLuGGY65y8vKC0MJUCfD37AIAFABXGg4+iaX9ryzv/h/+Xv///BYL4/4P//j/+5JkTIAT6FxP+eNdwDFr6RgIIm4NvYU/x4yxwJ8A5KAjCADAv/8caPgUF////g/jguB8YA4OMPjCzurSrKeKAAeiHBzp9VnObZOIBzs91k9ycxlrbjQyCuHUcAWrRIQ4GGBvzT6biRVIy65OpwVNecp86fowEhwtlyBQuY931t8KCmZt/6/zoUNBu1fatr1VFStSyyAoQhShEIogWEThAGLomC9v4xAAjoQEaSWKmrSBy925TOnd/f1+v/9mS/Xej/9RUkdZWuLGiStCf+myt3QdQAIAVwfhBiwp0upcYBvLCuJHIcaLcTBi/yM21wwuN571gjXY5Wdx9lOKrNFqqx1apJqbfO3dd2Z1Y4e99GtVC8rLZUtyo1Go0CcJRqWLlf/VulDeuWrTGeputDmfUtSFSYxqgo8NEohce74VGy54+VRqfW+8cokW1D7F0EVucHkHqJYf/1JXQSO6fqpeWSVln9DWXxkiJXCIO5UyipzSbw5yojZikyHUcxxE2ZjBQk6t2N5Vx1lRQb4MByEBTtPJTHmYNU7kSRVlIYInUlmU//uSZGmAA3ZaTeHnLWAygEigHMIADd1rNYeYbwCnASJkMYgAwaBylOkmu7K7MauyXjHnwyMiMur/f84YVbSzzk+esbzYjjT/t7+asespMZEXT1cUiAwFSARLB1JUsMH9NYMv3Urv1CiVOpc9Vlr6NSs8PY1DlqJVVadzvytX86//qCiYp2d177WI0wt7QoBSBAhaSwMJ2HY4l5TydTip8qXMqLIRCGp9tLNX8E1mNYXhPfFKdJpORPTTRI07GbCgNAjBjbNHgYOA+1WGc5HmkHBChRKzEqZ+xwMGFOpigvf/nb3U5Sb/5a9zaI667sQUK7xnIp/6/PH6PspApJJJG3EkUwKMDMgc45qqCGnSjq6/Umrf9PTWXbTqdTR/t6CV7vb/1Nu6AVZUAFJKYtJVyiq6r7u+4blIk4ihW0UoPPYz0yRQH8yQHLTIzLWCBK4VtrS22gkGoY2GcgTmPTDJwkKZn4imLvVra3sWL0HnXe7RXc3HamPTSfof/u2imhZj/VBPGCNe/u6Bh1v9380i/QL/7oijgIBQs9MEQsMPCpwMxf/7kmSLgQOBOMbB6RryKyBYrQQiAQ08sxcMMGkItYNhFLMIUBx8GRbVzO2iiqn7+h/+v9Co5R39nd+jNfv9PrUGpgAAT0DzNLXvGViKTQCLvT1XQnli71R422NWdm0laBC1CybC2IGRcimLoyXYEiortCW13c4OQgS4GBu7K52qIhyMq3fM+uX0XOEhwk3+3vy3TM7is6eeXfJMpIMIbV2xvM/Xuvjf2LP7ZjnlzflAQAV1XVVRTOMMFRGSBo4KgEJERoq9Nure9DGRbs1bmfT7Ll0emYs37f5W5/T7/7F3v6SnHLElgsY0CwRlCQoXxOCboWoydzK5kXpYZ7khBaOTU45RPVF7Sb2n1GIEYeoSJSN6Z92TqpXVOqOgiWb4hD6ghI00JIDPhgyPBmoENFQYWSJghZ4+gHyAHD+9r3EAibsbENxx1RpiQJfXbSZ0Hzg60AJkWJqNNjRxfp2+1vu/v+t/L/6HZdCf+l3ouX/0KgiS3ClMCij0C0qI35D2gKVsS8FDDrfJxt09/6vCh7Zb7g2y1FdrwY1U1E2IBWOHQcv/+5JksQEDgk/GQwkaQjGAWHkIYQAM8LkjZ5hvAJuAYiQRCABAWMmDsFIvShGcpMQmkVeGxckkyMGxuCBRDgnaOzmoWQrxbEi4JqdZfv1WWCPHZoi0yrximkUrTHpZC1PimM32/f3krDgRHDS5MJUz01tkVxkRL4hrzjRDIUviKDL5TlKStPnGrFebihZ1SX9Vl/SxoPXO8OHt/ZTvokNQRZLOCBAMj8AA0+cBHgAECAEGPY101VbKfrW6d//Rj6////4///+N/8vo8ujy80H3KKNKEz7nIe1bfcuQIsUAzC2l+RKMJ0rlypcKZz3AYHJf348oGIYUQYIhBaff/7UFho9hg/p0v7v6cKE/SGJAQqEYKmQbDwNQ59v7bzXNo3Vp0VxbvXaramW1u1nPrdxu3WU6o6m3dxLZy2S1e017q47LqSrStitysUC0WDI9qT4meP7obbd5NLwJltqwWiifK7t5dUdX56SAbHHBDmzzHK3j4LGDpZJ/ImTzUXfc+7+mK0+vF/qdcYcGUfVbdXfnljKSyy2WVtEkACNgDShVDa72//uSZNeAFc9hSmHpfHIp5wj4CALwEbGNN4eNkci2AaToEQgAOOPZCsTi+QxLAwIAVAYH57YQyWkJaVLXjvco6vsgRpUVCZxCGQgDAA4RDQ6luhouSsxMTPS1hn6zMlVzh5fJnD+pjHfIXf/vkf6WltmnkbN+8LqbyErqRaU4DQzVsUFtRgBWHy1HdOiW9r+cs4cEQdeeI5NfHeSF+Ef/y3L/L5f/5Uv//xD/+IA7/hwg8Q/w4Q/w7/D29rvA1SAADhLcLWuztLeoS27PBmWETtaaWOFr5cxAejGPoma0xiqC/HRJIz73jTt+/IPc/CrDoZ7f0Mby9L030AIAnbMid2qaeEwx3QImBQoqQaZdDPMuEUC87NMgaoSMwWAMM4K2sB6ABQKQIRyAvJKPfmyQjCd32MV9xIleoO/89cluWDtXls2YDoRQVVvPAqMSdqe6CoValYSBocwt/VUg11w0yAABvC9NR+mBkBkmKwZeQFqB8ZWV1qcmRybLcQgagxjCm4Z0oxI5CSqkx0H1h8i1N1plS1dSh0LE+bGxqX9849hw1//7kGTHABOFWtDrDBn2NOv40Rwnfg0ZYTGHjLGI4IDjJBEIAMvWG3lz6vmrNHBDtTBgICt4ZsqkokKJnDqq2X2a0oxrSYtsKQNaho4do0gQaAb6Q7GIrQt2hch62/XiH/39X8idYCqjyFHiJ2qR/b5hj1CpUoAdKSAWQ6O2Hvg9Fdar3xqEvlXnp6WI/y/kkgckg6Qrck56FL9JySNF0if8hen+9yX/7kkT3PRvDyYuCbxN3IH9dRb9dRbUNzRVc3VNMeB5H1U3/V/1NbUUU/zTVUNzY1NlB7HpZVVVc2NfUX1sfDUeFx4xUaj2Py/6n//E7ut9Ij9w5IitDlThK2UAwBweIBCHQ+A2IBAIA4txDh/w/BgN8v8r/DuIP/iHDvDv/H8bHxvEP4hh4f//w7iD/8QfEIgxB//8r5WVKRqX5Yp//5QbgAAvREARw11GaBzoYxKhkbT8OlwtM2K6kFoZX7yF40kCc7SMmxxT37YmJPvcxelF504Y9knHsNSHHyjQ6qqcXs1EI4fRqXwzqrbZ6OkTjxaPr0R6o1bEd72Ppv/7kmTiAQNqXUnh7BjwKGBIQBjCABFdaxcMJW/BHjPfFHEfwMy74bFGr04uTh2dU2R2R4pS+n9J5FyX4YdlyqnguSOVGFuVClDiHUDKYq5qapWUGhCReJXKUhZynYwtXj9yxveu9fSxq+h5kLA4skoCa/KotVZtS8YxYUT+boTUvHo6V1gosIrSCiAmhSxwFQ5cRCBcrEIqLx9db5xsqkwwooXXL+RnOPrVl7WpWNNT21z82exi/xQU6/P2jq8sHCCA9XQXIJk+fKGbLo3L1r9aR2ctGtSHZwpLlzlpcifvKidv3d1K9f59dzTLOsx0iR23bfk5OfR9uaHYOCeIS8uKG997K58N8Lv2gt//Jf2RaF6rYsefE5kqTQQlDEaKOQkw3yKHaO405BhDE6zFNF9jUfNurr43oCVptXYuZYrGqbZQ6sm+kLoLAAJgl4hVCjy1KsFQiTTGsmZTmgZGCAbZICSJpuYnOKttoy6weJOk6qkglDECMq3jTCqFqCEYSc1ImOR24hUWHpVXmdWhcSocJ7++w1N37LInZ/Cu0jP2TEv/+5Jk7QMEKlBFKet9cDdgCJkIQl6RwUcVDD2ACNQBIAATCAAEhIfc06nte/rL0djp1p1luzqdCUNl6L2Yvdhj7lX1TnMByTxCC4nCERxFQ9XRdPTnT/TvczH8Vizvcu7emAw7YKq0pxFFJkDZo+Bw8dGOwbvNdYIxlTZw/c5PSgkOdfr9qmVVv78Xvfa+tFc6Enf7gE9aNNiG7CCgFEm6iIABQYLMhLrK2vFLG1cpmdfGeilJjDFCPKIjTpOy7Y6MLx29Rd0vWb/fmNWd/Wbjo62aiCuujWIKA8uX+c6Oj0H7KcDoeKPtb9f/ohzO5hrNo6UamUGzkDDh0dFxJPp801XJMOFQqiSLOhYq2gBWgYlqo4EIxrhEhbk5yK6frcxf026HftrGN/9HCitP/7cWs/0fXUBhxWqB4sWaQmYwxpjNUsG4TayGbTIEimMzQAQpqEZKU8XE5kHiMayUZ99inZOTMMVFk5kZYhKhI80VB+XU+cX/U4lMtcitVxMSQkIOEvxrlSrx6jjsTpc0a6NdW5WulwrXK56n2n1cN0RYnhdH//uSZOwABNNaRKsJY3I4IBiKBCIADhlhHYwY78CZgGFkAQgAJA2cGtxv3Nv16fLji29ZyrqK5rXa+b44mjTabyy2u3WFvtys7u21Yn12SU3sE0LGhiszds1rXzuvz9Yvf7xu+v/94xv4zjuGS4Dbjjj72FiCIBYEDjFLzd9KHNftbYqv7Lvzlq3Gz3oZ/Vaxv8q6xikKa2vLJf+mqoCHWEK0j5V/t2XgmgnI7y8GFvA5cFP85VI9cGEAVtCWQsPut+30kdpL43WSSyNvdHfflLWp50qphhCoMVKSJFMO3YuqqW1O9VCXKWssWUGgFQfHK/S41Z77mvnqZYsbbHGDRpCUbxjedIpRrmhKlSKGsQ0f+vtKmqPM7//T3c3TM//alAQYCxoPHD6lrFTrIoQYlPUrf32jVNvUi5v0xTV3v97aN/VottZ//Vv+pQqSPKvBowWDAAkUBVB1mlry/c6yJxU1nwnW0h841GQsR0vShXTDnulc2qBWp9fVlKtrbRvWne27DTSrg4ur/K93Sjbm7qFRq9oVhdVpD3FQp9oQxOubQv/7kmT2AQW5YsMDTHtyMCAYjARCAQ/pPRkMJQ/IuABh5AEIBBuGvP3XDjnG3btxam1vbFcgiYKPLi20zuu3Nypm+/TWvfXq3aclarG1Ru1lcrhspVutlydNt8Utfbc6cVhrVqhVlHK17enxfFd6b8OC7DIAv9Z1BbF7R/pAJMkkH/StwSSggC4eCKpIPpr7VTKNVzFXWsaAI4xHRdn7xYwqm7+xMUdQxCH/1/d+m79yqbIbmTmLocKXb7Wg8GQzApElaYBYqG19LYeTJgVMHfT0ZyJDvjBDBGjR+RwWp0WUfB+5JHMQjCyEkHIvuC1+LKc2mJmgQQBSxwvuxCF07hue/r6LCMEam4EeQsgXB3lY7kjk9WOOI0hlmaYDiU1O8USpn+jlitzHCs/6CjibvwBFLWGHdYYxSL4RSR53bdqEq3rXf1Ode8Xjj+VbXKmPNb/LdJT4Y2Obyx1DEUa5RW89YT+X93exv1tc1/4VLOF6phn+WO8OWK8/g/j+Yu/P8z3nZr7vau2Me0ggJlP////WWDflgKYUIdKkVmvfJTlTnzD/+5Jk6oAFeljEBWngAjNgSJyjCAEcKYtL+ZwAEPmQn8M1MACBPjfvmpwitxuCLiKFmW4igiwGQgMLlviKCKCLfxv+EdAetYHvYM3LRbLUixaVFYPUBJRuASCQ9kiEuPkWBpLlEkYW1lVa4ktCbHK33CrDewc+FPis1o9vGznwl0htcQaPd7hV9WjW67x8R86rErBlXE8B8uXym1aHmfMV9Ct4uITzdK3zrc9YVH15FwS2LHVNn2Pnd9XjvcvZtrobJf4JirCRQx+uTRXoNbv1zmmXtzQQcqkR7SvHmiplTuGpEO0q0VMd7RFMVaLhZSw6vUok03DUr7F4elTezTTGIla6r8wA1kpIDQGk0mAACQShhriZdqKAlKXuo1e2+/7/Mdv/u/6WCZNrPUrzLaH7K6DWjqkjAApaVFqHoiEYMonBkFzdluLowK2V4U5zjWCbw9zTW3U6/NV3dy5+0BD25Ko828fZp5iCFw1u7880ywJKbray7Pv5H8SE8+3eXufcq/T/m7aQiX1ltT1/ndsexvZr7RTQysWSolfiZ986bUxM//uSZKgBFbdozqc94AIo4Em84YgAFKmrPYeZj8izgSXgFIgAOHZwUjRktsqqwHscDbtqpBFCxbgRD8HaUwQ0xwbKjiMtUIuVO6qYf/zpEuZxJW739jObLJMgDQAIQ49TFrSHhax7E9/FSpd6Akxn/Na/vdv69v9TnXJpvZ3y0MOWNaBlL9IYslggAtSGmMP94aRCS8i3hfI9KpZuRrM3qpgVUd5jcKF9SPs/6fS42X3Nu248m7FuuOp/VF4y+yjJmF5msmlcxCCPOtXmbpD7xzdRfFOHSu2r/VkuKxLMq9FJotebGjgmlVRWDZCPYGx3nRslLCk9NCQuD5wZAYTXGWoWTkWUcRkYNjtPdwRbo2cRZJ3r2BGe5ca4bo8ls6tdytb4xasICCE0otECAWJUKmWPZM6bMkuGmJ9J/8czZ/31epyv9Z65qUpiiPabEpEsa21sVsF6Wsw/FWFvy4ICLIKz/R+gjFEst+iw8Z5gTIUhTeGN3IKgqqJj6yTzx+osCoKmCGotImgOHleiv6OwmVLPVZgsaRkJKGS4UMVyK8btOv/7kmSOAxUiZ82h6X3yKCBZZQUhABUdfSisJY/Ipasj4CCJ6Na3QH2GTKxLJeRfeHcjXOpwYj9S5ZgptYvteiRLXDlpeACJI5DsJT99Qz1b1WVq2pyYrSUZYr+uXTOuauMh6XWQnVJyijeWpTH5Z6CYehtGTcSm78pk/IGCgAgFACHY5d3RO+NG8/3bl+/Jmvg////HgwH////8f///4Pwf/g///BgVCAQAAAgQL0dZpkLT6MUBLq3NE0XFW3YVSOI4J9KmIhO89e1tMzN6Zfox0tJpuX+Tp7gu6Xbr2p2/Kxa+JBFHh1fH0W5S/Z769v67DsBUivv+wwIBoCYj4svZy76+9GywW38ssLCBCICzS2gsOdS9nNu394y+vLbzlfY5zV7ba8truQBLeu+2/RmIS39/Ka2s5Ok95FJcePgEAAoG/jONT4fIKW9DO3SfcgN46uKezWswSc513/IHA+sP0N09Ff9H9Kb4fQJHfnLbHEiS0knFlv2XcAPgJ5Bm1pT6xRinWdBZMgQ+AOAN+50a3EuhnJSM6assjtVsDeOcBPj/+5JkfYBE0l/JweZj4iogSOUIYgAcDaU/p5nrIHgAJeAgCXCuTaf66VZ8mUnWlXkzPtvL+unBWooxZl5kpKr2Z2oXJNnSVQbjfIx4ZGq88CrAqGdggQ1KvGKlniRjK9WLpseN47wCA0FqGoHg74USG3NalJ68Z3aIjsI9YhArWVWGqXp+n1wlIiuiTObBSVOMpnHSQ5xdRTT0WNF3a5IigJepyQksEnLuih8nMJIGCAmmMvuUFV0YXNdlWpkoxIuR4yKzEVEIvv2tmeQ9oDABArEQf///+KxoDohZLRVIbD6Uu//R3f///oeaqUGBXEgsKPgbIr9ymwLFLdBAqJ2X5hl3aSq/1N9i3ViMC4Vn1bbtvdaqZ7F9cVrrcFdhAQoSrpjKt291R9GtaLbOPjxoT7UtcvdsJyj0p5ygvYMWvw9ZexIc5Pcby3K6NZ8zbx8MT8OEDCYrErpn1zGLaycmRk8yYnq05UAVLKY+tY5MWOnF0c1rRlgRm4lxk2ST77XW0Oj6a5GSSzU5cJUV61nelld82e9a61WvNLnrTtnrrUQU//uSZFsDNbdpyyMPZPIsSvj1JCJOE51rFK0xGkifjGIAkKU4Eg4ABJC5CjQgz0TkFtI8mZfyvF/rBD//43/+BDx/////4D///AgL///j///BgYBOA0KQyRcFck+VJIJlHwYDbE91SadR3qbGYeSGZTZ5Ecalrdb9ZVdUty7jlqO/lHYFitOFC5tC6jzl0lNaull3eZHlgEnVvXXG1+i2FqxWeYNimEw+jlyjmGBtqgWFmVmGohRLU8jhYDgARZrM3FU63re1lGoA45x5wseFZ+drjgVJFTeu4JX/GDCqR5Z1WxY4dDY1yLj63/RR/RUdMAifHi0grlVYS3IMV/3X7oVCoEszLPF+y//ouqsWgA/+eQbp6NIDAAGtAGpug5qUH9oROeW9Y18O23+bXGljcNr6EPue8uM4Q6LG1zsMUBSvFB1qrqN0CaOsENK06BpravroL9Wa2grLtJxqd9dzr2M/TImbxf7UzsLvVr/663n/be6G1Xp7azmPfLLRaNQPW2ln5i62Ob0dZ9hA233Vd9OKG3Hb91fAAreXbtRWIT0m+v/7kmRGAAQMREOtaYACLSComaSIABltmRU5p4ABsDIhhxagABklpuMaiprvDeb0dKUr/Z6a3dvu/2XBz/S9iHNr1M/r71RoFTILW8iDAAABGAFkxrQw9GCdAdGCgBJuIM7YCDBFV22dOGhpGG9hjWR71EN1VadDDBHilFMztZaw7UhmgJ0KE5nJgak4xq5SLbdcrj6V5tq/O2ZhdUpd/HjPyF4UNUMLpXT7UbdY63EZFQ/jHCbRe18hB6tMWX+Je1dSxovcYbzVEMMhPi5k/JOWNWU94DyJSt/LiHHvEvX7s9f4OBXhMLhrwhiHkzQ743r3//+/T6xX3xqn+v99wcUPbDcqu0BnKvx3PDf/5T/+LgNAAAAkZAFKC+4PLY/p8+flfenZCRt8xnNMJDE8VCpYeR4XQk9t6GOxIPCYCoGxXb3JGrQiEOSoPxDN3ve92+4gQtiYJAmMx/f6f2fZR+eB8Qh6kBYfmf/+YYxje77Fh4DYWVyAklC7Ef///+hxfP66T6eONZLRRFIVh1IJHMrnjadLCcTtXHHMPS+dRQzAPKz/+5JkEgAEmljS7j1gAjSluezBiAARAYM7nPQAAKwAJSOEIAAWaSTcDC4JLDIgqomGlkgfiPLXxUlC0FxYbGReO5u58a4gzpLHeZy21zbayNjjW2nycQheXsc9h50Mt9y1x1xUQt2+GnqNXU23/r/x/n//98FVHJY1jz3/3/veibl5w0x2MYaNt9vUsKComyHd8bo6MF19AqFYwAMAAAAbI5Q/O8LM1P8tfujK/9u/f/eqzm1/d/dwwo5xAFqGepP/+K13+tGj2hWPaOORAAbx4EIQ1fLceaRLNWnmZR4KkuLDRWlwMMIEYoYN2cZY9x0xv1FxotzdvSxvjoSrto71rLuKmORlXVzxT16zLD5pqPZYzHpFC0n1QyAvYv836xKUQEh42SoPeXGUiy46mVWv4qbCcYOSgFAFKACCpzjQfHjrJ8f8XlwZFYoQsgaUYD4QVZQALgQBKQ8VqdZV71/rV+z5KpTP5IkWUerWLu3IdkU/zHimgJuFE3LTXbl0kUAAAGITkdJwIhWpqM1WVRflKcsWIup3e5sq6akljFY8x0zy//uSZBOBNJBfz2HofOAzC5jgHCdOEc1xP2eZ8ciUgGVgEQgAdd29pNthklTA9tDp65h1Xu6SNUm0BU9wJqWfrrXkS1b95bttW/utrrsmLhtW1vXTZvGs5rrNd7wr2xW322bVjnjFt6/2rc3/1h3e2mp3qtNno1LlQH2XjFHBtam7tbVrGt/eWrAd0uMSMiqDA8QFozlMpfus+vPlNf+X4P//+H///jH//8Ff//+ACCkGwVwb4Mg3///BTgAwU+CgKAxJ17ux8JgiS/G6YjcdZyVVibVZvKF/VelZWBjY0xgsQTf38eYd513Z61OimLrJKIPdbmu2w2vG5ERl97g/YKEvEPlxfuNfFL/V63+bZg0JGmoUO9L4rPXOr6vutr31HcW29olHN9bT6mrY1H3fOc119WzW0RyjLzCtNbMplbnd3V9XnosGLLrfrR3xxPwiAAttETXcGFMFK8U6vavkE/92/62WelfQ/bjjOtz3/oaZxQlJVpUIpyElUAAAVVDMJ3BRhQHI4D/VKNcT/cNwm5kh22NHd1YyGdShZUOGXE0qyv/7kmQWAYROW81h6GRwLorY+BQnTA/5IS0U9AAIuqXkJopQANFWtVs300TXDLsTUG7FN0owlCgXTURa7ZPH7UeKnvtmZ5yegVA6imbfpyYuz9clmuLlz2roySexNat6q2mnMTUe2nZrWa1Zdlpc80u+Fby5c9tLtLrIWdUK+qCpWHQBmWkAfH0YKxqvd9n93W/6W//LyvKSnjH/ib////4nibysr/8rjYpL/iH///+JgZeBAMEZox4RxluDqIUXM40odTijyjXBxZLMLAEADjjkEYFwigGBagjmnCYTTY7u7JLINYweOQaNZ0qHQecg3DRxhxPtKMsHwPkUlPUbRxLJNJR8ijyy1BjigHmMTd7RT0ixJMI7TNJa2mXUJVXzDu/3bntRgwct5LS35Di36dwWYAAGGBWMq56lfpb13/Z5XZ2y438fjI3x34Z/hmP/x/Gf/+G/G4/Gf//H/H//SmNHVapJRJeGZdVnGk2WRWWGz022CJFgDNH9bxMc/zFwVtFr0w46nKzp4vCfDBXDCw5Md++DnLE3wrbr21nnUkOrBDn/+5JkIYAFZWJR/mHgAj7oKY3BiAAP8YNHvPWAAKSAJmeEIAAxXLHGjqx4u2nMBvvqT0xqlL9sfvZninabX39e7y+/q+z/SktLvXe8fcms7x387yV/Kq53ksr0w3z+efePTf//+4celNfO/f5c2rOve9NUxStI+v//q/vqGr2h/Hvv0//z2tQLTe3ENJIKBAGSYGAiVQgAAICAAHWcS2dg25aQ3buhmfRklImx3dVEKZUCOrC0Pm3df7/+///c6uVyuf//8kZjQR/jClafWE+45bEWgAGeGWStVKZxkQpXKlUszS2J2LlREKXUit7TkrK9taoI0sY647k6iAqGC7jdtVDIrpzljlshj7h8XsjaCYO06vyauuHljMyfTaMUSalC56lT02dHkJGzrWipj/r65NOY/q+q/+Tlf//c/6keq5hSdROnr6/r/9yX7wA8KgAACwVFzp55mghZFfdajTu9Y5y9H6NO5qqk6Nb6v//SJVgJhUiL1VGRNLDIAADtPIqyYFyOY5jiN545HTFJkydiVbCwTsO2WS9bI1F9RRanT16T//uSZBYBNBNYTeHrRPA0iwjoFEWeDk1jJYwxDYCoAaGAYYgAZIEBlmd4Zc9RucatvhxtcIt/2Gw1G1t9zv+eUVm0ke28xKJ5znIA6btiLlfZ2aagoHnCGV8WvmP45FTVbq/6vi1VhoqhICoqQcDIJFTpYSrBkjsLesBACgSAEKDQBDIeo1a6U/XXru2nrjgh///BjQY38bx//+CBDgICN//4X/8M+Gf//4Z+FfhYAghN2lE8BA1erLXllaxZCxJq8CuRPrl5YOFxqhntXrL697N5hracad/o+o9sDRdIocvrI+8vXS32NNZpWma5aVXtmGzQ+PufuYlf5VSVXafiAePqYrlV4a29rmomOr/jbmr1qP///4vua5UpiQEDIC86ywLMFq4wlF0sRZGxdTra3FmkTLdT0i/0WiF3op+uCq2NTozMqIv/o7zxatUN+vNgdDCzKDTT4sCALYG4TgdEU02aClDLPxUqM8oIm6g+k2jk6RTMr8AS5k6CmKmk3NCeCESmIpoSOc3TdN4p5kxfwn6af9MOwgOxSsLQvuW6RK/mp//7kmQrAON7WMth5huyNAQIciQmThdZkzIHsfHIhBQlgFAJ2MJ8v4RpfuX/l9YnQqouIgtpRa6ToPJ/X4MgAgUhM43LVJzsCHmV8utSLASnAq/jNt6CCkHKQFhZiBgD8oJxVbzW9z/8RUv91LjTf/+CyJDoOZWF8OjiEFmdLVM7WIaiTsxyk6MkxxYbVqdWedYRNFPye86f59fYZRZYRDvIYHyfVOuh+pCMYKxNXW2sobSRPtlROE4f+iO1cLVbUfXnDicpIpkjqxjbzrcDTjwrxls2iFAaENQk3Wnu37U2t0OBSeaMsM8wcZjnO3McaVcaljyRXOVsb2RXxHquYX0WMyYrKrz/R5/q9C5WNxEcOU5jhS6svBSaeZWp7GzDvd45xL5nm3jMYGAJ0jBAqHQ//n+3/RXs7FR7t/+QOYIcn//+ZcIEh4h+D//ryapOQnSydM+q4ZL1FuUtdgZTmzJ5W6jM4Zge5ZiMyHwttSnvBe2hvWuBEb3N/fUN6+fQzcN1pna4FY7xpL5Plv0oNySS9rc2zCgq4bT6vYJhwp2EfiX/+5JkKgAGP2jMAw+McCdi2j00AkyOVW1N55itiLqAZnAQiADqmvlNZRukddI4TdFAvOKip0UUhVoi8ArQGEMwViiHwCqFUsPj/oi7GAFgwZRcQ2GGBGGyhiCqFUMB0dUVgVgVkVa4rEYDinF4VLRFFGKLwd4bOK8KCHgQqGmigBuBsguYUBGwN0b43hqRvYoH8bw3+N7FBhaoAAAYJBJLQYUxvGZFvliP96v9n/v6LDgRTq6huR9W7zkgZPi5Cg2kneDYzkaJAAKoNEdhJi+liTN1IZKjRTaX9sREhAKWeQMrZ2ZjHXW7OTcbmVWlE0t3HOMjnMbdl99+cxg8VTqurIv/P22V4Ch4VMjstv/EXZB10RWZiMpWKhqoVWVmmKSYiOPUS0OK2GHbXQgr1dy9/mQBEBZSYAACDgoFZ1zDdd90s9aNRBj/s6Ogc5L6v+0VZob1W3dvUOTgVFc911/+mjJ4NpVmRRQEAASI5CdMx8oUoh7H9ROnS3GAdUFOoS9d3YQJlWhwEjy6CIhSmq5+gEe1XaqPmFOOp/T7Hky7VNNZ//uSZCCAM2JD0XnjPFIxYFkoGMEADckTRceI0cDNriOUkIk4aTqtXa392NAaMIdSn/WcD46Lb7xTft9vm3SyyDVw2E3lAWwL+KHwrj/83IAIBwAYUwCYaQii1N+ik7DtVXYs7/0o/1+xx0DK09Qi0LuWs6In8lxdy3CaeIthJ6h6RCrUwRp1yAqcYouicRI2XpNC4HW3mmhdFYhjjB94bGBuQjEISp3uQhCbvOcOBnQjSAABAwMDHgwMf9CdAgUOfzv+q1uIx9e9972MAERMfcvw0eIx9xoTTPlAx1Agfrf4IJUGIjNh8EFmAAcYXD5COgDiQkV39ORTm5KX5KvpL+v8EC4///BDQAD///8f+CG8H/8GP4//x/x8f//BAHAx8DHqRkR3tkZfpgcgj4WSqSRSPgfrwqTiKYgwLzNTWzLKVEt3s3Zy2PetpNst9vpuslDdrk4QbHNWu2RLz+PyhQJSXpf2R9W+GZsfstE4QDhvY99c79xSUcWB5ctzbfyVaKInRfeEbIKxKFA5DERhZUTtWjg/F1H4gg1GdxgzxbETIv/7kmQ/gBP8ZFJxg07QLuBJngTiAA3dYT/nrHEI0yHlJBCWeGBAAigSJKAACYYjXqeFmJTfAnNt27u7/ykgmimrX3Ko/zmZGfT/VIPPk6ErYa+hBvCJEOqKomUAAOdBCeK0vp3IAlZzuaOOJJRJ52NgettrGsO2tbrN/SZvZN1HB5oOa+m2gMQaw1oCq58vOeKZzbhl1EbyYj5lD/7wwJDY+Mfy05DRctZdtjtLUuHNmY5lznsarGUM7qYT5hXIXP/5gA8B0CaaI6y1+a/sTI1syL6P/f///mLE//fyfMiE///9DBIFXFiX8StO+lSQmdEoK1wV/BoWCT1xqtggBBDQnBmq8lpfTmIUS6GqTqkUacfp2qB5PO9W5rXx9NNc8mrDj6hOPSRANS1GkjUSwoUZFqTr67eS5qRFkv32ZjLafJ//rHEw///jdLpVVWo2vDtL8o3Vzy+Fl9UuM5Q7DgpQlia0O/vBA2qAFdMoBhGGkr2LOuoI1dOR70f+tH69vEX/qLMh0NZbqleKSqgKeEIAlrEaI0Apy7y11irLa9Xh+vD/+5JkVYADeltLaesb0CaAGMkEQgAMiMcXFZKAAKeAIvaEIAQS64PprVsLYJuYHMrOMaNVxqTyEGIisQhiIyylmmNkdiHKiMt3oQzZCK6MllXWKpwSB4Si5ENAVok0gIq808qu/eLzClIfaZm+KT5Oj4uRIMkutrsjaKYu0BEQ2E2qXdXtsxQJJvoT6l3935vZa7//Z63fRyyv/czTmur2dy9fp9OhsMgrNhVWaMH9Al+KDErJ0jSYpOlpiMikoDQBvchQ09+Q8TAoSQAWAGchoLQ1xQEvELIGzgLy8J0SIpxMB4R0+gWChTBWE0EMF4BXMYesrizZTTjM2ltnZIrGrVcG+2VDVqolCigGhA+FiM1v1RKlFIszlc3q+ymVsJoZ1GyQIjJ8Q48MvDApSMhlj0XaXj+DCVjH5P2SJDWI8DbPvcJbqabK2RW9nYIVZ63eSx1REjy50rHWYcCkS894nve4oySTnWxPY7hh3S7njLy8dWPNLeaP72fV////9JPgnA5AdwVDWTxI8v5H00PoIf/////4wmR///+ALkGoGtch//uSZIKABxFmTu5l4AQhJghwxrQAENWlRd2EAAjUrKVjhiAA0I3MiGAKkEhNAeIcxJxOtD1A3CR5XN0F10pO3EcMFhZh1L1NxdxxzzG99dU/PrHPNZrf7XbE1MLm1333vy71d1+O5qFq6a6VBZpzkpZ9+rYStdBOJQarYiA0daYiC7Iosh5tFTQ7thcseXQxRQREE/YvYs7uUqvRkSXFu3Fab3ezFoTWGWcggAAcWFBuwlNKXPurMluv0Intb/wUf//8EBeD/g/+610r9Nv//xvBQOPH8F/Gj/wYPgHHSZh7lnZXpEQAA4i8hzHMT8u4yyUCOKwXisJ8kFKsWTklBjGC75K6WJoeFBB+IKqwMDUktldEEi6pJX6VOs2fDAh0pvnxJW0dSPb+fFkQ7fv///wqHlkun26MSyNP4fvTBNll5EKD6CKaAsBzOSCBCUbTAAAwWAJlZC0RiGonWnS2x0elDXCY67SEurb/v9X+oagWVGIYFcVcszNPxYVE23+TR4ZsdWVZYywASYG4eJajIMspCDm4cR2uaNbsOMqmUz5rYf/7kmRiABNsV9L55huQNIA5fBQiAA3ZYUvnjFHIw6HlYFCWeBkzKilkBowVhy2ISCvRAFuprqVbsTfP56T7HCAx3CUVVM/6b2Lr9LoiOun/1MSQWzICKRNqvrUilXW1tFRyrHgA6F1thejK/6e/vqfwACJQHCcgu9XZqJXz+vP7dcvXsvz/n9fl/L8yvf+Dr/7fODi6hOD7S9TqUNortetnSjU2OXVmR1EAAAvguKdLcgVaQJPH7BL4OI21E43YXN+9w6ldZzBrLT5vXD7D7wqbxb6cVhJhhhI7lo8nsIBieaUq808T/VhTNB///EiLxqIoCohey0ohQzXfozT/XH/cN3rFwcSZcuprSM0LaPaAAIQQGAABQtQFKlR5y40p/FlNkqqj217fWz/TR/4V/CT3MDpI+pgd9fVXYglI+pFSgaQjhJl2NgEBIO4drQUPB7uWkb5mcY3ZV84PA5tBC5B0RERX6gzK8S9hhwOudFxO59P+5xzrvy/J/okK5J8c2UO0v3y3OlfeAABQgORbNXLP9Jc///0RP03AxyMJoIp/U0X/+5JkgAEjaVvQeeFGQCwgKVwUIgANBW8vh7BjwLIroyBwinhC4AtCwLgRjYoUl1l1vat3v5ez/oH2f/Xz9K/3283Jg5f8vJsz///+P7////8FBIEJIFgAKC5bLozE8f0xhAhFmFuXG16+7axKjmlIVixzV5b+ojlQ9Pz0eB0XmA5/g5ndCY/mL7L7Ezj9n+omq23bGMYgl6I6IpbBAA5gQQGSVZ/wnJMLfxpYbnGeaZIzlFfsQEBRzORBGmDEw/u4bhqxlcu4KNVp0u50j4H4mcsbkxwI6PowQU/G8NxjUjOmpwmY29jotOCjesR4Mr5OBqB6AZ5XH8RIORWr6QcE+wMb6FIs2V8W2YEe+8w9/VP9UxrM7BIAoAgCCDHBBF81+H//8MR5/p5QEw8guXVk/9Rz5z7/IQObUp2xQ0PxAcyC2hDSWQTLZLZUXGjpfSaAXjcty2hv24Nyjo6W/+Ov1fcZNP+0EXBE/6SzRMgoo5A4IG5C6v1xc/M//XDOIImSJHPFJf0MP5rVkp7vHUytvFQwK9GywFc4L6xPberYvGpf//uQZKgAViFrzWGGf4IsIEmrCEIAEvmFR8wh8cC0LmcQcAk4VbubaoVErFu9q2pez/cysfOE7exVzeLmDqHGh0rNhrdQ6Xi3vDlqumyRe3PjG73veClohAsFccg0kCwB4iOyfG///6/qbJ////+AxxgQPAf//wXGj8f48fg/8FKRGRZyLcoYkm95MUZnU1kAADI0EoYimvII3IVdOVad752a7MzMQCRQ4nMxp9my/OuSzl9qNymZSADpMQkpy3O806yHX/0OnExpqLdZzzdDeqaH6TgMiE0ZJcoVysqWLj6XFYWo+EULyxQfaL801UNm6+chznsPR7KF49HsqWlMuIF/0AWD+tObe10t5C0yfh8s+///r/6af/6//6lX0erfZDVKz6SlT69ABGP6L9OZEQJpcjRJed5YWk+CTG6SI2bKFWq0rH0NhYXH5fPb1pF8H11ie17b+bY3W0Kw0gmnalezRsNGfOIuvUx98mkgpEcy4jl118bUN13DXGsqosIIAVJqmbRvr26bg6pHNbXAshwlAQlOgpyOBaCJ09eIn1qA//uSZIwBM7Vd0PMGU8AwiamoDCVuDgUlKoeFGgCwiOPgYIkoAGEvApOq7hsWGFGOXdbWP2KFSQk2AKuj+p30JzvyVSSXrkkUX+DX5XyZLSo1xSMGwpEgAIQE+H46MtEn4jy4KhDIEdgRmmNj1+xoXfHd8QCQtXvLWhIEv2Fiym3YXwFQrQwQQr4rPCIYLNxYJdGiZzZ/O9mwdxLfSCPHN9fpTmIXllFkzdyiUS370+lKbQuBRNKudu8J+9igoo8IEKCBBSr/m/+BSn0ROb3v6y74k98seWe/Yo7/5coAHAwARz5Jhq3/4FPmX8/X18EkBDg5jIFEDMfHmPjIyRL6/yadv//wDo+8up1Z91QDIyMYVkMZlR8ng9BCU6tmxKWAmaoHaHYh5PC9g6AtZDRioswAgIYTtrcda1Df0iZ0rkMVuPmFBt2pvXAjrvDW1q1oMiAhk0PY1kVTTpQTsfcdUI5CkT8HifjJ9Rd4pQoDaZ4TiIjiRYinu5PIs7I9pBjmkNTDFLSDHgsabdP8N7Io0u6KliHWjQNR6JgPWp2BQM6GCP/7kmSpAHRpXE3p7ETwMOiZWAgijhu1sT3HpfqImyxnoCAJuHlNlwOdpOZhupTOJmXRvfscFHnWn4ji5OKITAc7AZD00jwKMjQSUUwTgW0eSfZFwrIEF/CgIlurD1ApiDBYoMkF+/Z4L6t4EPCugEAf//o27P/////////3clGu16ZJ77q86VtZVnMJRQRiEKTPrf1VWGFYdFNLEAAK4GiLsLMbK2i0uTVRkjWjbblFBa01I2KGEj54PiSQYjlQw4MApjN0xDcgqcs8DKoDJJnyv5fgRKDU3/XzO2HP9T/zXW/EMfV1lv+p/7f5aVGAeQrM3ZWYGGWpPdpUjJuzVVXWpvtUdUba1Tc8SjRY7vfbHoHD1Grr9sVe/bPcPa7/WBoBpBroABJZZQwePTvQSyrc4W1w730Pp9NHtr/UBdct+eFnh1SvWCv6osBYUetJw5k8qSHGiCCE3KFuF+WFdIQoYyk2r2U5MSqye8deUWYfLWAiCKjpTPJY1GMEFpabwjthFVLdPq/53GBiMchrLrkfK0J/8ukCCgDrpMa5TlMb40D/+5JkhoEUVmtR8eNdUC7gecwEwAIOQWFJ54zzwNGCJvAQiACEC2XKjQaFHRjEOdD5hqMrKv7utLClAGJCAVJgYd9ABScibsCTMdgYIeggg5aH2jApShxxRPy9tPnVN+izu9bwwTKGRBZr1AgAw/uXf/lHJaKy6TeWqKZEaWIEAA7CtMg0oQxW4ugxTJRyXqXk7ZdKavYVPHj5g11aNH1isC2a6rnWPG3peJKrsxaQLWuwKRjO5F9tmqDpzJuXbX7m+uu5//rxcIXlKtYX/+JeTjAeGhclnHMMljth0stugxq7Dd8thTbRvaDtAUAaKaGtAABEwiI2hA2cQUMFpdZHJfP1q7/AaXXbfy3svaLfkgM2sFBj3BJ6k/+xFgpBm6qKpwgAHsXJdGSMRQok8ZGJXqWRz1eEnlKiQAVYKZ0yZj2pMG4Z0EoE0+zm1s6OazoNjebZKjJTapR1uxz5j5k7RdHGLKF6OGsrP+h00004cNVFaoiTzWc8yMjmU1o2bTQoVBUqAgqlWR/HuywPKThZcCkiTOg489IiRFuWBrmC07H6//uSZJWAE6FO0nniRpIxAGneBCkADfk/O8eNTwDFAaXwELwAWhJ9KhwNfItV/RxhI3o8eMD5VXFiRIXK7D33KgCdHRQKkhtrr6WYTKWeMPiZEFzw3WCVGmgc9CYaVLI0Z14iLv+OLqUB3gHNQu5dW5nsjdwUlQPkJcdXUGZgQMW7muG/TfzA1JrDhu1Z7IpWHS1BeKp0f/8OppbQ7YHc+qunSy+SKZRuIFo7cuImhg6qtwiDqaA9/t0jCIgAKOKDt2af/Zq2369rW2Wod///BpQcyluWefR7ywhUe1StraYTxIVGFQBJ4SLX/6xEWlEQ+A4sKDXTKGvwXcjUO01BKotM135lsToojcq5ZVZ1FNA8kkm5jrUtF3SMhfgqIGSFFCGNtvCr1SVSbQET49HdVZWoQNqi755hjt1thAUT6Js9tVTXc+3c2fu/iZWhqrjhAjIfVGH2VPVNuTqNPo2Tp0nTFKMOtwEasrbqyq00pAgX1hVGUKeeiOuR0uV1+3/VNHr//gPjYONwf+3R//uPfQ7/7o0aWVIBGQEeDqerpQHZAf/7kmSxAwPLT0mjDFpAMmSIphgiHhBhPxyMQXLAlRQhpFCIuMHrj085Ze0m+m20SDS2vCzqLi1s7+811nNc5UosM1tV1j2j2mOWYMABjreVhpWo+6bada/lUc56Va7na//obOONHSw+A0NZN1Q83wXF2v+3/9+AuX6+FVWa4VS5zKLH7/wQAGMMDghwZY+jmCT94//H7t+iP/1/4/Av6f9TfpT7+n1Cn/+7+oIBaKwA1T+z8SfelcdtG4wVhYb+kqz/Xdw5mkFYo+SeFfC+EyU3gzryXscPYYzZmEfl4QikURHkXF+tDZcgbHdHP6qd1KFOhh0eiI9Voiszrm14a4HhU8lhEPmUS2JaGOYU/7X7MoxukFv/atmsBMWZSbRZU9wYmV3u7fpqVq/9n+q3M/07v1furlBjK8kpPWhTQa6IhJWPkuqPlQ6FMwwl/Y42fOVUeQhqglqBsRRuIIfsec1MR3FNtKzQPBqbh7VN1IG8ogdDSysd5bA3dWXjqyoXmZAU9u9uQbzEqqrt5EhiClQw7PDnFJpCcuVml20vfvZLUab/+5JkxgADZkPFweg+oiiFGBUIIkoNCQMKrBixgKIAISQhCbi99T31DTNsFUe5kVFVcVTd12+G/8cMi+Yn82821F//1Vldb//XNNRVY3gMB7lZ15qQvnRRAiVrXa1DWFE6kITPCn0Nub4tvYhzitosYvFCzLZvkNR5I8X0wtcRi69S757dHgUUYAAAE5yaMBbcjyiKiGjtOOqHPMhlgC3b0PGEEBxSGh7AowoMQGFME7D4F8J6E5jmiQgNgfsKYNMixiOaXDMwKRNjGsOSTYnAeA6QUgZh8hDRApmXC0M4XR/IEQ8g5qdIaZDhMSPLhZGiM8Q8Z4uGhmYpGhwyJAi5gxaLpqThDzAjiuRMxMDEiB9NE+nMWNy+cNC9NimXTEqE2bE+TBmxmbE4aGRiasifmR00pGtM2Uo0mxflxJZ1JaSakZePoHjpcWeqLp1i8boFw6gZpVJmyOXDSVF3MnNTp2gl///+kdUv///9zUuKAgkUUkkQoUQgu169ImAAU4Z6sAZZdDHt/FvYbeob4iAASdaxPOgEKx+vbGJEclj3dN4J//uSZPIABHxnQIVhYAA4YFfgpIgAHSYRArmIAAKfQiAnMLAAhoxVM0Jge1zBK5qWr76bmhoWH1Tdsw6JbdW9kMhdxoTDdOD0Wx8JOYg1KW9MNHts3J469Gp2vl5q1XueHzM5yoZZ/caWumfp0MlsbrdO1q8zVLU9r6bzNWpmhoocPzrs3zTr////////trXf///////pk5h2AAEgAANAEbHYE3f/JSk41BYj/pgixkVdL/BsCDBo6RcuA2AhGL0nVkzxyw3AXPh9hlR1DNH/GsHhD3xQgXNsTSZNE98hoaSLnIoUwwIkOUM0MsOSOH8PUDVY5wyInkmhkywOkUCLlJogQy38PUEBA1QJyC5wNWCLlcoKIcHpCkRcJqUSCk7/yLCkBAAXgjgUoJ3NyuSw56JYEBiGk6ookBHNIcOd/8ti5BQAog0hKA3hzRdiDyibF8qGJAkSkLOIaRFRSPjkmReLyn//5PFM+Z////mMFOypDRB0KjhnZtl0z1bAyUCjIGBuvEgs2QdMUEQEE/4DTsDTsSuAYJxkgNmJAoMAyyEOhP/7kkSEgAaudUGuZkAC0U6XkM3QAAAAAaQcAAAgAAA0g4AABDaeCK4BkCwFhoBRcAEgLUDcQwvAwQsAUAA8OAMFEE0iiMqLOFxfF6I4ENGRGfIiQJiHDnENHN/D9BHI4xT0xzBzCKl43LqKiBfxyR2EgZEXL5ASHEUMS6yTorROf8gxXICbkSIuSxeFoIE5iXSZSSpJE0Yl3/5gMUxPDsIuXySHMKhBjhqaGBMmJrMi9MTxkiyVL//kBIKThFv///yaTEFNRTMuOTkuNaqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqo=";
// Kept for future use — different element types can use different samples
export const PENCIL_LINE_DRAG = "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";
```

## File: `src/vite-env.d.ts`
```typescript
/// <reference types="vite/client" />
```


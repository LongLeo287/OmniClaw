---
id: pixel-agents-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:30:59.216946
---

# KNOWLEDGE EXTRACT: pixel-agents
> **Extracted on:** 2026-03-30 17:51:01
> **Source:** pixel-agents

---

## File: `.editorconfig`
```
root = true

[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

## File: `.git-blame-ignore-revs`
```
# Prettier initial formatting
# Add the commit SHA below after committing the formatting changes
b94955dab19dd32cd530bd2f3580c7716bc0b448
```

## File: `.gitattributes`
```
# Auto-detect text files and normalize line endings to LF
* text=auto eol=lf

# Binary assets — do not diff or merge
*.png binary
*.jpg binary
*.ttf binary

# VS Code extension package
*.vsix binary
```

## File: `.gitignore`
```
# Compiled output
out
dist
node_modules
*.tsbuildinfo

# Logs
/logs
*.log
npm-debug.log*

# OS
.DS_Store
Thumbs.db

# IDE
.vscode-test/
/.idea

# Build artifacts
*.vsix
*.map

# Environment files
.env*
!.env.example

# Project-specific
.claude/
/sprites-export
```

## File: `.nvmrc`
```
22
```

## File: `.prettierignore`
```
dist/
out/
node_modules/
webview-ui/node_modules/
webview-ui/dist/
*.vsix
*.png
*.json
*.md
webview-ui/public/
scripts/*.html

```

## File: `.prettierrc.json`
```json
{
  "singleQuote": true,
  "tabWidth": 2,
  "useTabs": false,
  "trailingComma": "all",
  "printWidth": 100,
  "arrowParens": "always",
  "bracketSpacing": true,
  "endOfLine": "lf"
}
```

## File: `.vscodeignore`
```
.vscode/**
.vscode-test/**
out/**
**/node_modules/**
src/**
webview-ui/**
scripts/**
sprites-export/**
logs/**
.github/**
.claude/**
.env
.gitignore
esbuild.js
**/tsconfig.json
**/eslint.config.mjs
**/*.map
**/*.ts
**/.vscode-test.*
CLAUDE.md
**/*.jsonl
```

## File: `CHANGELOG.md`
```markdown
# Changelog

## v1.1.1

### Fixes

- **Fix Open VSX publishing** — Created namespace on Open VSX and added `skipDuplicate` to publish workflow for idempotent releases.

## v1.1.0

### Features

- **Migrate to open-source assets with modular manifest-based loading** ([#117](https://github.com/pablodelucca/pixel-agents/pull/117)) — Replaces bundled proprietary tileset with open-source assets loaded via a manifest system, enabling community contributions and modding.
- **Recognize 'Agent' tool name for sub-agent visualization** ([#76](https://github.com/pablodelucca/pixel-agents/pull/76)) — Claude Code renamed the sub-agent tool from 'Task' to 'Agent'; sub-agent characters now spawn correctly with current Claude Code versions.
- **Dual-publish workflow for VS Code Marketplace + Open VSX** ([#44](https://github.com/pablodelucca/pixel-agents/pull/44)) — Automates extension releases to both VS Code Marketplace and Open VSX via GitHub Actions.

### Maintenance

- **Add linting, formatting, and repo infrastructure** ([#82](https://github.com/pablodelucca/pixel-agents/pull/82)) — ESLint, Prettier, Husky pre-commit hooks, and lint-staged for consistent code quality.
- **Add CI workflow, Dependabot, and ESLint contributor rules** ([#116](https://github.com/pablodelucca/pixel-agents/pull/116)) — Continuous integration, automated dependency updates, and shared linting configuration.
- **Lower VS Code engine requirement to ^1.105.0** — Broadens compatibility with older VS Code versions and forks (Cursor, Antigravity, Windsurf, VSCodium, Kiro, TRAE, Positron, etc.).

### Contributors

Thank you to the contributors who made this release possible:

- [@drewf](https://github.com/drewf) — Agent tool recognition for sub-agent visualization
- [@Matthew-Smith](https://github.com/Matthew-Smith) — Open VSX publishing workflow
- [@florintimbuc](https://github.com/florintimbuc) — Project coordination, CI workflow, Dependabot, linting infrastructure, publish workflow hardening, code review

## v1.0.2

### Bug Fixes

- **macOS path sanitization and file watching reliability** ([#45](https://github.com/pablodelucca/pixel-agents/pull/45)) — Comprehensive path sanitization for workspace paths with underscores, Unicode/CJK chars, dots, spaces, and special characters. Added `fs.watchFile()` as reliable secondary watcher on macOS. Fixes [#32](https://github.com/pablodelucca/pixel-agents/issues/32), [#39](https://github.com/pablodelucca/pixel-agents/issues/39), [#40](https://github.com/pablodelucca/pixel-agents/issues/40).

### Features

- **Workspace folder picker for multi-root workspaces** ([#12](https://github.com/pablodelucca/pixel-agents/pull/12)) — Clicking "+ Agent" in a multi-root workspace now shows a picker to choose which folder to open Claude Code in.

### Maintenance

- **Lower VS Code engine requirement to ^1.107.0** ([#13](https://github.com/pablodelucca/pixel-agents/pull/13)) — Broadens compatibility with older VS Code versions and forks (Cursor, etc.) without code changes.

### Contributors

Thank you to the contributors who made this release possible:

- [@johnnnzhub](https://github.com/johnnnzhub) — macOS path sanitization and file watching fixes
- [@pghoya2956](https://github.com/pghoya2956) — multi-root workspace folder picker, VS Code engine compatibility

## v1.0.1

Initial public release.
```

## File: `CLAUDE.md`
```markdown
# Pixel Agents — Compressed Reference

VS Code extension with embedded React webview: pixel art office where AI agents (Claude Code terminals) are animated characters.

## Architecture

```
src/                          — Extension backend (Node.js, VS Code API)
  constants.ts                — All backend magic numbers/strings (timing, truncation, asset parsing, VS Code IDs)
  extension.ts                — Entry: activate(), deactivate()
  PixelAgentsViewProvider.ts   — WebviewViewProvider, message dispatch, asset loading
  assetLoader.ts              — PNG parsing, sprite conversion, catalog building, default layout loading
  agentManager.ts             — Terminal lifecycle: launch, remove, restore, persist
  layoutPersistence.ts        — User-level layout file I/O (~/.pixel-agents/layout.json), migration, cross-window watching
  fileWatcher.ts              — fs.watch + polling, readNewLines, /clear detection, terminal adoption
  transcriptParser.ts         — JSONL parsing: tool_use/tool_result → webview messages
  timerManager.ts             — Waiting/permission timer logic
  types.ts                    — Shared interfaces (AgentState, PersistedAgent)

webview-ui/src/               — React + TypeScript (Vite)
  constants.ts                — All webview magic numbers/strings (grid, animation, rendering, camera, zoom, editor, game logic, notification sound)
  notificationSound.ts        — Web Audio API chime on agent turn completion, with enable/disable
  App.tsx                     — Composition root, hooks + components + EditActionBar
  hooks/
    useExtensionMessages.ts   — Message handler + agent/tool state
    useEditorActions.ts       — Editor state + callbacks
    useEditorKeyboard.ts      — Keyboard shortcut effect
  components/
    BottomToolbar.tsx          — + Agent, Layout toggle, Settings button
    ZoomControls.tsx           — +/- zoom (top-right)
    SettingsModal.tsx          — Centered modal: settings, export/import layout, sound toggle, debug toggle
    DebugView.tsx              — Debug overlay
  office/
    types.ts                  — Interfaces (OfficeLayout, FloorColor, Character, etc.) + re-exports constants from constants.ts
    toolUtils.ts              — STATUS_TO_TOOL mapping, extractToolName(), defaultZoom()
    colorize.ts               — Dual-mode color module: Colorize (grayscale→HSL) + Adjust (HSL shift)
    floorTiles.ts             — Floor sprite storage + colorized cache
    wallTiles.ts              — Wall auto-tile: 16 bitmask sprites from walls.png
    sprites/
      spriteData.ts           — Pixel data: characters (6 pre-colored from PNGs, fallback templates), furniture, tiles, bubbles
      spriteCache.ts          — SpriteData → offscreen canvas, per-zoom WeakMap cache, outline sprites
    editor/
      editorActions.ts        — Pure layout ops: paint, place, remove, move, rotate, toggleState, canPlace, expandLayout
      editorState.ts          — Imperative state: tools, ghost, selection, undo/redo, dirty, drag
      EditorToolbar.tsx       — React toolbar/palette for edit mode
    layout/
      furnitureCatalog.ts     — Dynamic catalog from loaded assets + getCatalogEntry()
      layoutSerializer.ts     — OfficeLayout ↔ runtime (tileMap, furniture, seats, blocked)
      tileMap.ts              — Walkability, BFS pathfinding
    engine/
      characters.ts           — Character FSM: idle/walk/type + wander AI
      officeState.ts          — Game world: layout, characters, seats, selection, subagents
      gameLoop.ts             — rAF loop with delta time (capped 0.1s)
      renderer.ts             — Canvas: tiles, z-sorted entities, overlays, edit UI
      matrixEffect.ts         — Matrix-style spawn/despawn digital rain effect
    components/
      OfficeCanvas.tsx        — Canvas, resize, DPR, mouse hit-testing, edit interactions, drag-to-move
      ToolOverlay.tsx          — Activity status label above hovered/selected character + close button

scripts/                      — 7-stage asset extraction pipeline
  0-import-tileset.ts         — Interactive CLI wrapper
  1-detect-assets.ts          — Flood-fill asset detection
  2-asset-editor.html         — Browser UI for position/bounds editing
  3-vision-inspect.ts         — Claude vision auto-metadata
  4-review-metadata.html      — Browser UI for metadata review
  5-export-assets.ts          — Export PNGs + furniture-catalog.json
  asset-manager.html          — Unified editor (Stage 2+4 combined), Save/Save As via File System Access API
  generate-walls.js           — Generate walls.png (4×4 grid of 16×32 auto-tile pieces)
  wall-tile-editor.html       — Browser UI for editing wall tile appearance
```

## Core Concepts

**Vocabulary**: Terminal = VS Code terminal running Claude. Session = JSONL conversation file. Agent = webview character bound 1:1 to a terminal.

**Extension ↔ Webview**: `postMessage` protocol. Key messages: `openClaude`, `agentCreated/Closed`, `focusAgent`, `agentToolStart/Done/Clear`, `agentStatus`, `existingAgents`, `layoutLoaded`, `furnitureAssetsLoaded`, `floorTilesLoaded`, `wallTilesLoaded`, `saveLayout`, `saveAgentSeats`, `exportLayout`, `importLayout`, `settingsLoaded`, `setSoundEnabled`.

**One-agent-per-terminal**: Each "+ Agent" click → new terminal (`claude --session-id <uuid>`) → immediate agent creation → 1s poll for `<uuid>.jsonl` → file watching starts.

**Terminal adoption**: Project-level 1s scan detects unknown JSONL files. If active terminal has no agent → adopt. If focused agent exists → reassign (`/clear` handling).

## Agent Status Tracking

JSONL transcripts at `~/.claude/projects/<project-hash>/<session-id>.jsonl`. Project hash = workspace path with `:`/`\`/`/` → `-`.

**JSONL record types**: `assistant` (tool_use blocks or thinking), `user` (tool_result or text prompt), `system` with `subtype: "turn_duration"` (reliable turn-end signal), `progress` with `data.type`: `agent_progress` (sub-agent tool_use/tool_result forwarded to webview, non-exempt tools trigger permission timers), `bash_progress` (long-running Bash output — restarts permission timer to confirm tool is executing), `mcp_progress` (MCP tool status — same timer restart logic). Also observed but not tracked: `file-history-snapshot`, `queue-operation`.

**File watching**: Hybrid `fs.watch` + 2s polling backup. Partial line buffering for mid-write reads. Tool done messages delayed 300ms to prevent flicker.

**Extension state per agent**: `id, terminalRef, projectDir, jsonlFile, fileOffset, lineBuffer, activeToolIds, activeToolStatuses, activeSubagentToolNames, isWaiting`.

**Persistence**: Agents persisted to `workspaceState` key `'pixel-agents.agents'` (includes palette/hueShift/seatId). **Layout persisted to `~/.pixel-agents/layout.json`** (user-level, shared across all VS Code windows/workspaces). `layoutPersistence.ts` handles all file I/O: `readLayoutFromFile()`, `writeLayoutToFile()` (atomic via `.tmp` + rename), `migrateAndLoadLayout()` (checks file → migrates old workspace state → falls back to bundled default), `watchLayoutFile()` (hybrid `fs.watch` + 2s polling for cross-window sync). On save, `markOwnWrite()` prevents the watcher from re-reading our own write. External changes push `layoutLoaded` to the webview; skipped if the editor has unsaved changes (last-save-wins). On webview ready: `restoreAgents()` matches persisted entries to live terminals. `nextAgentId`/`nextTerminalIndex` advanced past restored values. **Default layout**: When no saved layout file exists and no workspace state to migrate, a bundled `default-layout.json` is loaded from `assets/` and written to the file. If that also doesn't exist, `createDefaultLayout()` generates a basic office. To update the default: run "Pixel Agents: Export Layout as Default" from the command palette (writes current layout to `webview-ui/public/assets/default-layout.json`), then rebuild. **Export/Import**: Settings modal offers Export Layout (save dialog → JSON file) and Import Layout (open dialog → validates `version: 1` + `tiles` array → writes to layout file + pushes `layoutLoaded` to webview).

## Office UI

**Rendering**: Game state in imperative `OfficeState` class (not React state). Pixel-perfect: zoom = integer device-pixels-per-sprite-pixel (1x–10x). No `ctx.scale(dpr)`. Default zoom = `Math.round(2 * devicePixelRatio)`. Z-sort all entities by Y. Pan via middle-mouse drag (`panRef`). **Camera follow**: `cameraFollowId` (separate from `selectedAgentId`) smoothly centers camera on the followed agent; set on agent click, cleared on deselection or manual pan.

**UI styling**: Pixel art aesthetic — all overlays use sharp corners (`borderRadius: 0`), solid backgrounds (`#1e1e2e`), `2px solid` borders, hard offset shadows (`2px 2px 0px #0a0a14`, no blur). CSS variables defined in `index.css` `:root` (`--pixel-bg`, `--pixel-border`, `--pixel-accent`, etc.). Pixel font: FS Pixel Sans (`webview-ui/src/fonts/`), loaded via `@font-face` in `index.css`, applied globally.

**Characters**: FSM states — active (pathfind to seat, typing/reading animation by tool type), idle (wander randomly with BFS, return to seat for rest after `wanderLimit` moves). 4-directional sprites, left = flipped right. Tool animations: typing (Write/Edit/Bash/Task) vs reading (Read/Grep/Glob/WebFetch). Sitting offset: characters shift down 6px when in TYPE state so they visually sit in their chair. Z-sort uses `ch.y + TILE_SIZE/2 + 0.5` so characters render in front of same-row furniture (chairs) but behind furniture at lower rows (desks, bookshelves). Chair z-sorting: non-back chairs use `zY = (row+1)*TILE_SIZE` (capped to first row) so characters at any seat tile render in front; back-facing chairs use `zY = (row+1)*TILE_SIZE + 1` so the chair back renders in front of the character. Chair tiles are blocked for all characters except their own assigned seat (per-character pathfinding via `withOwnSeatUnblocked`). **Diverse palette assignment**: `pickDiversePalette()` counts palettes of current non-sub-agent characters; picks randomly from least-used palette(s). First 6 agents each get a unique skin; beyond 6, skins repeat with a random hue shift (45–315°) via `adjustSprite()`. Character stores `palette` (0-5) + `hueShift` (degrees). Sprite cache keyed by `"palette:hueShift"`.

**Spawn/despawn effect**: Matrix-style digital rain animation (0.3s). 16 vertical columns sweep top-to-bottom with staggered timing (per-column random seeds). Spawn: green rain reveals character pixels behind the sweep. Despawn: character pixels consumed by green rain trails. `matrixEffect` field on Character (`'spawn'`/`'despawn'`/`null`). Normal FSM is paused during effect. Despawning characters skip hit-testing. Restored agents (`existingAgents`) use `skipSpawnEffect: true` to appear instantly. `matrixEffect.ts` contains `renderMatrixEffect()` (per-pixel rendering) called from renderer instead of cached sprite draw.

**Sub-agents**: Negative IDs (from -1 down). Created on `agentToolStart` with "Subtask:" prefix. Same palette + hueShift as parent. Click focuses parent terminal. Not persisted. Spawn at closest free seat to parent (Manhattan distance); fallback: closest walkable tile. **Sub-agent permission detection**: when a sub-agent runs a non-exempt tool, `startPermissionTimer` fires on the parent agent; if 5s elapse with no data, permission bubbles appear on both parent and sub-agent characters. `activeSubagentToolNames` (parentToolId → subToolId → toolName) tracks which sub-tools are active for the exempt check. Cleared when data resumes or Task completes.

**Speech bubbles**: Permission ("..." amber dots) stays until clicked/cleared. Waiting (green checkmark) auto-fades 2s. Sprites in `spriteData.ts`.

**Sound notifications**: Ascending two-note chime (E5 → E6) via Web Audio API plays when waiting bubble appears (`agentStatus: 'waiting'`). `notificationSound.ts` manages AudioContext lifecycle; `unlockAudio()` called on canvas mousedown to ensure context is resumed (webviews start suspended). Toggled via "Sound Notifications" checkbox in Settings modal. Enabled by default; persisted in extension `globalState` key `pixel-agents.soundEnabled`, sent to webview as `settingsLoaded` on init.

**Seats**: Derived from chair furniture. `layoutToSeats()` creates a seat at every footprint tile of every chair. Multi-tile chairs (e.g. 2-tile couches) produce multiple seats keyed `uid` / `uid:1` / `uid:2`. Facing direction priority: 1) chair `orientation` from catalog (front→DOWN, back→UP, left→LEFT, right→RIGHT), 2) adjacent desk direction, 3) forward (DOWN). Click character → select (white outline) → click available seat → reassign.

## Layout Editor

Toggle via "Layout" button. Tools: SELECT (default), Floor paint, Wall paint, Erase (set tiles to VOID), Furniture place, Furniture pick (eyedropper for furniture type), Eyedropper (floor).

**Floor**: 7 patterns from `floors.png` (grayscale 16×16), colorizable via HSBC sliders (Photoshop Colorize). Color baked per-tile on paint. Eyedropper picks pattern+color.

**Walls**: Separate Wall paint tool. Click/drag to add walls; click/drag existing walls to remove (toggle direction set by first tile of drag, tracked by `wallDragAdding`). HSBC color sliders (Colorize mode) apply to all wall tiles at once. Eyedropper on a wall tile picks its color and switches to Wall tool. Furniture cannot be placed on wall tiles, but background rows (top N `backgroundTiles` rows) may overlap walls.

**Furniture**: Ghost preview (green/red validity). R key rotates, T key toggles on/off state. Drag-to-move in SELECT. Delete button (red X) + rotate button (blue arrow) on selected items. Any selected furniture shows HSBC color sliders (Color toggle + Clear button); color stored per-item in `PlacedFurniture.color?`. Single undo entry per color-editing session (tracked by `colorEditUidRef`). Pick tool copies type+color from placed item. Surface items preferred when clicking stacked furniture.

**Undo/Redo**: 50-level, Ctrl+Z/Y. EditActionBar (top-center when dirty): Undo, Redo, Save, Reset.

**Multi-stage Esc**: exit furniture pick → deselect catalog → close tool tab → deselect furniture → close editor.

**Erase tool**: Sets tiles to `TileType.VOID` (transparent, non-walkable, no furniture). Right-click in floor/wall/erase tools also erases to VOID (supports drag-erasing). Context menu suppressed in edit mode.

**Grid expansion**: In floor/wall/erase tools, a ghost border (dashed outline) appears 1 tile outside the grid. Clicking a ghost tile calls `expandLayout()` to grow the grid by 1 tile in that direction (left/right/up/down). New tiles are VOID. Furniture positions and character positions shift when expanding left/up. Max grid size: `MAX_COLS`×`MAX_ROWS` (64×64). Default: `DEFAULT_COLS`×`DEFAULT_ROWS` (20×11). Characters outside bounds after resize are relocated to random walkable tiles.

**Layout model**: `{ version: 1, cols, rows, tiles: TileType[], furniture: PlacedFurniture[], tileColors?: FloorColor[] }`. Grid dimensions are dynamic (not fixed constants). Persisted via debounced saveLayout message → `writeLayoutToFile()` → `~/.pixel-agents/layout.json`.

## Asset System

**Loading**: `esbuild.js` copies `webview-ui/public/assets/` → `dist/assets/`. Loader checks bundled path first, falls back to workspace root. PNG → pngjs → SpriteData (2D hex array, alpha≥2 = visible, `#RRGGBBAA` for semi-transparent). `loadDefaultLayout()` reads `assets/default-layout.json` (JSON OfficeLayout) as fallback for new workspaces.

**Catalog**: `furniture-catalog.json` with id, name, label, category, footprint, isDesk, canPlaceOnWalls, groupId?, orientation?, state?, canPlaceOnSurfaces?, backgroundTiles?. String-based type system (no enum constraint). Categories: desks, chairs, storage, electronics, decor, wall, misc. Wall-placeable items (`canPlaceOnWalls: true`) use the `wall` category and appear in a dedicated "Wall" tab in the editor. Asset naming convention: `{BASE}[_{ORIENTATION}][_{STATE}]` (e.g., `MONITOR_FRONT_OFF`, `CRT_MONITOR_BACK`). `orientation` is stored on `FurnitureCatalogEntry` and used for chair z-sorting and seat facing direction.

**Rotation groups**: `buildDynamicCatalog()` builds `rotationGroups` Map from assets sharing a `groupId`. Flexible: supports 2+ orientations (e.g., front/back only). Editor palette shows 1 item per group (front orientation preferred). `getRotatedType()` cycles through available orientations.

**State groups**: Items with `state: "on"` / `"off"` sharing the same `groupId` + `orientation` form toggle pairs. `stateGroups` Map enables `getToggledType()` lookup. Editor palette hides on-state variants, showing only the off/default version. State groups are mirrored across orientations (on-state variants get their own rotation groups).

**Auto-state**: `officeState.rebuildFurnitureInstances()` swaps electronics to ON sprites when an active agent faces a desk with that item nearby (3 tiles deep in facing direction, 1 tile to each side). Operates at render time without modifying the saved layout.

**Background tiles**: `backgroundTiles?: number` on `FurnitureCatalogEntry` — top N footprint rows allow other furniture to be placed on them AND characters to walk through them. Items on background rows render behind the host furniture via z-sort (lower zY). Both `getBlockedTiles()` and `getPlacementBlockedTiles()` skip bg rows; `canPlaceFurniture()` also skips the new item's own bg rows (symmetric placement). Set via asset-manager.html "Background Tiles" field.

**Surface placement**: `canPlaceOnSurfaces?: boolean` on `FurnitureCatalogEntry` — items like laptops, monitors, mugs can overlap with all tiles of `isDesk` furniture. `canPlaceFurniture()` builds a desk-tile set and excludes it from collision checks for surface items. Z-sort fix: `layoutToFurnitureInstances()` pre-computes desk zY per tile; surface items get `zY = max(spriteBottom, deskZY + 0.5)` so they render in front of the desk. Set via asset-manager.html "Can Place On Surfaces" checkbox. Exported through `5-export-assets.ts` → `furniture-catalog.json`.

**Wall placement**: `canPlaceOnWalls?: boolean` on `FurnitureCatalogEntry` — items like paintings, windows, clocks can only be placed on wall tiles (and cannot be placed on floor). `canPlaceFurniture()` requires the bottom row of the footprint to be on wall tiles; upper rows may extend above the map (negative row) or into VOID tiles. `getWallPlacementRow()` offsets placement so the bottom row aligns with the hovered tile. Items can have negative `row` values in `PlacedFurniture`. Set via asset-manager.html "Can Place On Walls" checkbox.

**Colorize module**: Shared `colorize.ts` with two modes selected by `FloorColor.colorize?` flag. **Colorize mode** (Photoshop-style): grayscale → luminance → contrast → brightness → fixed HSL; always used for floor tiles. **Adjust mode** (default for furniture and character hue shifts): shifts original pixel HSL — H rotates hue (±180), S shifts saturation (±100), B/C shift lightness/contrast. `adjustSprite()` exported for reuse (character hue shifts). Toolbar shows a "Colorize" checkbox to toggle modes. Generic `Map<string, SpriteData>` cache keyed by arbitrary string (includes colorize flag). `layoutToFurnitureInstances()` colorizes sprites when `PlacedFurniture.color` is set.

**Floor tiles**: `floors.png` (112×16, 7 patterns). Cached by (pattern, h, s, b, c). Migration: old layouts auto-mapped to new patterns.

**Wall tiles**: `walls.png` (64×128, 4×4 grid of 16×32 pieces). 4-bit auto-tile bitmask (N=1, E=2, S=4, W=8). Sprites extend 16px above tile (3D face). Loaded by extension → `wallTilesLoaded` message. `wallTiles.ts` computes bitmask at render time. Colorizable via HSBC sliders (Colorize mode, stored per-tile in `tileColors`). Wall sprites are z-sorted with furniture and characters (`getWallInstances()` builds `FurnitureInstance[]` with `zY = (row+1)*TILE_SIZE`); only the flat base color is rendered in the tile pass. `generate-walls.js` creates the PNG; `wall-tile-editor.html` for visual editing.

**Character sprites**: 6 pre-colored PNGs (`assets/characters/char_0.png`–`char_5.png`), one per palette. Each 112×96: 7 frames × 16px wide, 3 direction rows × 32px tall (24px sprite bottom-aligned with 8px top padding). Row 0 = down, Row 1 = up, Row 2 = right. Frame order: walk1, walk2, walk3, type1, type2, read1, read2. No dedicated idle frames — idle uses walk2 (standing pose). Left = flipped right at runtime. Generated by `scripts/export-characters.ts` which bakes `CHARACTER_PALETTES` colors into templates. Loaded by extension → `characterSpritesLoaded` message (array of 6 character sprite sets). `spriteData.ts` uses pre-colored data directly (no palette swapping); hardcoded template fallback when PNGs not loaded. When `hueShift !== 0`, `hueShiftSprites()` applies `adjustSprite()` (HSL hue rotation) to all frames before caching.

**Load order**: `characterSpritesLoaded` → `floorTilesLoaded` → `wallTilesLoaded` → `furnitureAssetsLoaded` (catalog built synchronously) → `layoutLoaded`.

## Condensed Lessons

- `fs.watch` unreliable on Windows — always pair with polling backup
- Partial line buffering essential for append-only file reads (carry unterminated lines)
- Delay `agentToolDone` 300ms to prevent React batching from hiding brief active states
- **Idle detection** has two signals: (1) `system` + `subtype: "turn_duration"` — reliable for tool-using turns (~98%), emitted once per completed turn, handler clears all tool state as safety measure. (2) Text-idle timer (`TEXT_IDLE_DELAY_MS = 5s`) — for text-only turns where `turn_duration` is never emitted. Only starts when `hadToolsInTurn` is false (no tools used yet in this turn); if any tool_use arrives, `hadToolsInTurn` becomes true and the timer is suppressed for the rest of the turn. Reset on new user prompt or `turn_duration`. Cancelled by ANY new JSONL data arriving in `readNewLines`. Only fires after 5s of complete file silence
- User prompt `content` can be string (text) or array (tool_results) — handle both
- `/clear` creates NEW JSONL file (old file just stops)
- `--output-format stream-json` needs non-TTY stdin — can't use with VS Code terminals
- Hook-based IPC failed (hooks captured at startup, env vars don't propagate). JSONL watching works
- PNG→SpriteData: pngjs for RGBA buffer, alpha threshold 2 (`PNG_ALPHA_THRESHOLD`), supports `#RRGGBBAA` semi-transparent pixels
- OfficeCanvas selection changes are imperative (`editorState.selectedFurnitureUid`); must call `onEditorSelectionChange()` to trigger React re-render for toolbar

## Build & Dev

```sh
npm install && cd webview-ui && npm install && cd .. && npm run build
```
Build: type-check → lint → esbuild (extension) → vite (webview). F5 for Extension Dev Host.

## TypeScript Constraints

- No `enum` (`erasableSyntaxOnly`) — use `as const` objects
- `import type` required for type-only imports (`verbatimModuleSyntax`)
- `noUnusedLocals` / `noUnusedParameters`

## Constants

All magic numbers and strings are centralized — never add inline constants to source files:

- **Extension backend**: `src/constants.ts` — timing intervals, display truncation limits, PNG/asset parsing values, VS Code command/key identifiers
- **Webview**: `webview-ui/src/constants.ts` — grid/layout sizes, character animation speeds, matrix effect params, rendering offsets/colors, camera, zoom, editor defaults, game logic thresholds
- **CSS styling**: `webview-ui/src/index.css` `:root` block — `--pixel-*` custom properties for UI colors, backgrounds, borders, z-indices used in React inline styles
- **Canvas overlay colors** (rgba strings for seats, grids, ghosts, buttons) live in the webview constants file since they're used in canvas 2D context, not CSS
- `webview-ui/src/office/types.ts` re-exports grid/layout constants (`TILE_SIZE`, `DEFAULT_COLS`, etc.) from `constants.ts` for backward compatibility — import from either location

## Key Patterns

- `crypto.randomUUID()` works in VS Code extension host
- Terminal `cwd` option sets working directory at creation
- `/add-dir <path>` grants session access to additional directory

## Windows-MCP (Desktop Automation)

- `uvx --python 3.13 windows-mcp` — Tools: Snapshot, Click, Type, Scroll, Move, Shortcut, App, Shell, Wait, Scrape
- Webview buttons show `(0,0)` in a11y tree — must use `Snapshot(use_vision=true)` for coordinates
- Snap both VS Code windows side-by-side on SAME screen before clicking in Extension Dev Host
- Reload extension via button on main VS Code window after building

## Key Decisions

- `WebviewViewProvider` (not `WebviewPanel`) — lives in panel area alongside terminal
- Inline esbuild problem matcher (no extra extension needed)
- Webview is separate Vite project with own `node_modules`/`tsconfig`
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant 3.0 Code of Conduct

## Our Pledge

We pledge to make our community welcoming, safe, and equitable for all.

We are committed to fostering an environment that respects and promotes the dignity, rights, and contributions of all individuals, regardless of characteristics including race, ethnicity, caste, color, age, physical characteristics, neurodiversity, disability, sex or gender, gender identity or expression, sexual orientation, language, philosophy or religion, national or social origin, socio-economic position, level of education, or other status. The same privileges of participation are extended to everyone who participates in good faith and in accordance with this Covenant.


## Encouraged Behaviors

While acknowledging differences in social norms, we all strive to meet our community's expectations for positive behavior. We also understand that our words and actions may be interpreted differently than we intend based on culture, background, or native language.

With these considerations in mind, we agree to behave mindfully toward each other and act in ways that center our shared values, including:

1. Respecting the **purpose of our community**, our activities, and our ways of gathering.
2. Engaging **kindly and honestly** with others.
3. Respecting **different viewpoints** and experiences.
4. **Taking responsibility** for our actions and contributions.
5. Gracefully giving and accepting **constructive feedback**.
6. Committing to **repairing harm** when it occurs.
7. Behaving in other ways that promote and sustain the **well-being of our community**.


## Restricted Behaviors

We agree to restrict the following behaviors in our community. Instances, threats, and promotion of these behaviors are violations of this Code of Conduct.

1. **Harassment.** Violating explicitly expressed boundaries or engaging in unnecessary personal attention after any clear request to stop.
2. **Character attacks.** Making insulting, demeaning, or pejorative comments directed at a community member or group of people.
3. **Stereotyping or discrimination.** Characterizing anyone’s personality or behavior on the basis of immutable identities or traits.
4. **Sexualization.** Behaving in a way that would generally be considered inappropriately intimate in the context or purpose of the community.
5. **Violating confidentiality**. Sharing or acting on someone's personal or private information without their permission.
6. **Endangerment.** Causing, encouraging, or threatening violence or other harm toward any person or group.
7. Behaving in other ways that **threaten the well-being** of our community.

### Other Restrictions

1. **Misleading identity.** Impersonating someone else for any reason, or pretending to be someone else to evade enforcement actions.
2. **Failing to credit sources.** Not properly crediting the sources of content you contribute.
3. **Promotional materials**. Sharing marketing or other commercial content in a way that is outside the norms of the community.
4. **Irresponsible communication.** Failing to responsibly present content which includes, links or describes any other restricted behaviors.


## Reporting an Issue

Tensions can occur between community members even when they are trying their best to collaborate. Not every conflict represents a code of conduct violation, and this Code of Conduct reinforces encouraged behaviors and norms that can help avoid conflicts and minimize harm.

When an incident does occur, it is important to report it promptly. To report a possible violation, **[NOTE: describe your means of reporting here.]**

Community Moderators take reports of violations seriously and will make every effort to respond in a timely manner. They will investigate all reports of code of conduct violations, reviewing messages, logs, and recordings, or interviewing witnesses and other participants. Community Moderators will keep investigation and enforcement actions as transparent as possible while prioritizing safety and confidentiality. In order to honor these values, enforcement actions are carried out in private with the involved parties, but communicating to the whole community may be part of a mutually agreed upon resolution.


## Addressing and Repairing Harm

**[NOTE: The remedies and repairs outlined below are suggestions based on best practices in code of conduct enforcement. If your community has its own established enforcement process, be sure to edit this section to describe your own policies.]**

If an investigation by the Community Moderators finds that this Code of Conduct has been violated, the following enforcement ladder may be used to determine how best to repair harm, based on the incident's impact on the individuals involved and the community as a whole. Depending on the severity of a violation, lower rungs on the ladder may be skipped.

1) Warning
   1) Event: A violation involving a single incident or series of incidents.
   2) Consequence: A private, written warning from the Community Moderators.
   3) Repair: Examples of repair include a private written apology, acknowledgement of responsibility, and seeking clarification on expectations.
2) Temporarily Limited Activities
   1) Event: A repeated incidence of a violation that previously resulted in a warning, or the first incidence of a more serious violation.
   2) Consequence: A private, written warning with a time-limited cooldown period designed to underscore the seriousness of the situation and give the community members involved time to process the incident. The cooldown period may be limited to particular communication channels or interactions with particular community members.
   3) Repair: Examples of repair may include making an apology, using the cooldown period to reflect on actions and impact, and being thoughtful about re-entering community spaces after the period is over.
3) Temporary Suspension
   1) Event: A pattern of repeated violation which the Community Moderators have tried to address with warnings, or a single serious violation.
   2) Consequence: A private written warning with conditions for return from suspension. In general, temporary suspensions give the person being suspended time to reflect upon their behavior and possible corrective actions.
   3) Repair: Examples of repair include respecting the spirit of the suspension, meeting the specified conditions for return, and being thoughtful about how to reintegrate with the community when the suspension is lifted.
4) Permanent Ban
   1) Event: A pattern of repeated code of conduct violations that other steps on the ladder have failed to resolve, or a violation so serious that the Community Moderators determine there is no way to keep the community safe with this person as a member.
   2) Consequence: Access to all community spaces, tools, and communication channels is removed. In general, permanent bans should be rarely used, should have strong reasoning behind them, and should only be resorted to if working through other remedies has failed to change the behavior.
   3) Repair: There is no possible repair in cases of this severity.

This enforcement ladder is intended as a guideline. It does not limit the ability of Community Managers to use their discretion and judgment, in keeping with the best interests of our community.


## Scope

This Code of Conduct applies within all community spaces, and also applies when an individual is officially representing the community in public or other spaces. Examples of representing our community include using an official email address, posting via an official social media account, or acting as an appointed representative at an online or offline event.


## Attribution

This Code of Conduct is adapted from the Contributor Covenant, version 3.0, permanently available at [https://www.contributor-covenant.org/version/3/0/](https://www.contributor-covenant.org/version/3/0/).

Contributor Covenant is stewarded by the Organization for Ethical Source and licensed under CC BY-SA 4.0. To view a copy of this license, visit [https://creativecommons.org/licenses/by-sa/4.0/](https://creativecommons.org/licenses/by-sa/4.0/)

For answers to common questions about Contributor Covenant, see the FAQ at [https://www.contributor-covenant.org/faq](https://www.contributor-covenant.org/faq). Translations are provided at [https://www.contributor-covenant.org/translations](https://www.contributor-covenant.org/translations). Additional enforcement and community guideline resources can be found at [https://www.contributor-covenant.org/resources](https://www.contributor-covenant.org/resources). The enforcement ladder was inspired by the work of [Mozilla’s code of conduct team](https://github.com/mozilla/inclusion).
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Pixel Agents

Thanks for your interest in contributing to Pixel Agents! All contributions are welcome — features, bug fixes, documentation improvements, refactors, and more.

This project is licensed under the [MIT License](LICENSE), so your contributions will be too. No CLA or DCO is required.

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (v22 recommended)
- [VS Code](https://code.visualstudio.com/) (v1.105.0 or later)

### Setup

```bash
git clone https://github.com/pablodelucca/pixel-agents.git
cd pixel-agents
npm install
cd webview-ui && npm install && cd ..
npm run build
```

Then press **F5** in VS Code to launch the Extension Development Host.

## Development Workflow

For development with live rebuilds, run:

```bash
npm run watch
```

This starts parallel watchers for both the extension backend (esbuild) and TypeScript type-checking.

> **Note:** The webview (Vite) is not included in `watch` — after changing webview code, run `npm run build:webview` or the full `npm run build`.

### Project Structure

| Directory | Description |
|---|---|
| `src/` | Extension backend — Node.js, VS Code API |
| `webview-ui/` | React + TypeScript frontend (separate Vite project) |
| `scripts/` | Asset extraction and generation tooling |
| `assets/` | Bundled sprites, catalog, and default layout |

## Code Guidelines

### Constants

**No unused locals or parameters** (`noUnusedLocals` and `noUnusedParameters` are enabled). All magic numbers and strings are centralized — don't add inline constants to source files:

- **Extension backend:** `src/constants.ts`
- **Webview:** `webview-ui/src/constants.ts`
- **CSS variables:** `webview-ui/src/index.css` `:root` block (`--pixel-*` properties)

### UI Styling

The project uses a pixel art aesthetic. All overlays should use:

- Sharp corners (`border-radius: 0`)
- Solid backgrounds and `2px solid` borders
- Hard offset shadows (`2px 2px 0px`, no blur) — use `var(--pixel-shadow)`
- The FS Pixel Sans font (loaded in `index.css`)

These conventions are enforced by custom ESLint rules (`eslint-rules/pixel-agents-rules.mjs`):

| Rule | Scope | What it checks |
|---|---|---|
| `no-inline-colors` | Extension + Webview | No hex/rgb/rgba/hsl/hsla literals outside `constants.ts` |
| `pixel-shadow` | Webview only | Box shadows must use `var(--pixel-shadow)` or `2px 2px 0px` |
| `pixel-font` | Webview only | Font family must reference FS Pixel Sans |

These rules are set to `warn` — they won't block your PR but will flag violations for cleanup.

## Submitting a Pull Request

1. Fork the repo and create a feature branch from `main`
2. Make your changes
3. Verify everything passes locally:
   ```bash
   npm run lint                         # Extension lint
   cd webview-ui && npm run lint && cd ..  # Webview lint
   npm run build                        # Type check + esbuild + Vite
   ```
   CI runs these same checks automatically on every PR.
4. Open a pull request against `main` with:
   - A clear description of what changed and why
   - How you tested the changes (steps to reproduce / verify)
   - **Screenshots or GIFs for any UI changes**

## Reporting Bugs

[Open a bug report](https://github.com/pablodelucca/pixel-agents/issues/new?template=bug_report.yml) — the form will guide you through providing the details we need.

## Feature Requests

Have an idea? [Start a discussion](https://github.com/pablodelucca/pixel-agents/discussions/categories/ideas) in the Ideas category. We love hearing new ideas, and discussing them first helps us collaborate on the best approach together.

## Security Issues

Please report security vulnerabilities privately — see [SECURITY.md](SECURITY.md) for details.

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.
```

## File: `esbuild.js`
```javascript
const esbuild = require('esbuild');
const fs = require('fs');
const path = require('path');

const production = process.argv.includes('--production');
const watch = process.argv.includes('--watch');

/**
 * Copy assets folder to dist/assets
 */
function copyAssets() {
  const srcDir = path.join(__dirname, 'webview-ui', 'public', 'assets');
  const dstDir = path.join(__dirname, 'dist', 'assets');

  if (fs.existsSync(srcDir)) {
    // Remove existing dist/assets if present
    if (fs.existsSync(dstDir)) {
      fs.rmSync(dstDir, { recursive: true });
    }

    // Copy recursively
    fs.cpSync(srcDir, dstDir, { recursive: true });
    console.log('✓ Copied assets/ → dist/assets/');
  } else {
    console.log('ℹ️  assets/ folder not found (optional)');
  }
}

/**
 * @type {import('esbuild').Plugin}
 */
const esbuildProblemMatcherPlugin = {
  name: 'esbuild-problem-matcher',

  setup(build) {
    build.onStart(() => {
      console.log('[watch] build started');
    });
    build.onEnd((result) => {
      result.errors.forEach(({ text, location }) => {
        console.error(`✘ [ERROR] ${text}`);
        console.error(`    ${location.file}:${location.line}:${location.column}:`);
      });
      console.log('[watch] build finished');
    });
  },
};

async function main() {
  const ctx = await esbuild.context({
    entryPoints: ['src/extension.ts'],
    bundle: true,
    format: 'cjs',
    minify: production,
    sourcemap: !production,
    sourcesContent: false,
    platform: 'node',
    outfile: 'dist/extension.js',
    external: ['vscode'],
    logLevel: 'silent',
    plugins: [
      /* add to the end of plugins array */
      esbuildProblemMatcherPlugin,
    ],
  });
  if (watch) {
    await ctx.watch();
  } else {
    await ctx.rebuild();
    await ctx.dispose();
    // Copy assets after build
    copyAssets();
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
```

## File: `eslint.config.mjs`
```
import typescriptEslint from 'typescript-eslint';
import eslintConfigPrettier from 'eslint-config-prettier';
import simpleImportSort from 'eslint-plugin-simple-import-sort';
import pixelAgentsPlugin from './eslint-rules/pixel-agents-rules.mjs';

export default [
  {
    files: ['**/*.ts'],
  },
  {
    plugins: {
      '@typescript-eslint': typescriptEslint.plugin,
      'simple-import-sort': simpleImportSort,
      'pixel-agents': pixelAgentsPlugin,
    },

    languageOptions: {
      parser: typescriptEslint.parser,
      ecmaVersion: 2022,
      sourceType: 'module',
    },

    rules: {
      '@typescript-eslint/naming-convention': [
        'warn',
        {
          selector: 'import',
          format: ['camelCase', 'PascalCase'],
        },
      ],

      curly: 'warn',
      eqeqeq: 'warn',
      'no-throw-literal': 'warn',
      'simple-import-sort/imports': 'warn',
      'simple-import-sort/exports': 'warn',
      'pixel-agents/no-inline-colors': 'warn',
    },
  },
  {
    files: ['src/constants.ts'],
    rules: {
      'pixel-agents/no-inline-colors': 'off',
    },
  },
  eslintConfigPrettier,
];
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Pablo De Lucca

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

## File: `package.json`
```json
{
  "name": "pixel-agents",
  "displayName": "Pixel Agents",
  "description": "Pixel art office where your Claude Code agents come to life as animated characters",
  "version": "1.1.1",
  "publisher": "pablodelucca",
  "repository": {
    "type": "git",
    "url": "https://github.com/pablodelucca/pixel-agents"
  },
  "icon": "icon.png",
  "license": "MIT",
  "engines": {
    "vscode": "^1.105.0"
  },
  "categories": [
    "Other"
  ],
  "activationEvents": [],
  "main": "./dist/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "pixel-agents.showPanel",
        "title": "Pixel Agents: Show Panel"
      },
      {
        "command": "pixel-agents.exportDefaultLayout",
        "title": "Pixel Agents: Export Layout as Default"
      }
    ],
    "viewsContainers": {
      "panel": [
        {
          "id": "pixel-agents-panel",
          "title": "Pixel Agents",
          "icon": "$(window)"
        }
      ]
    },
    "views": {
      "pixel-agents-panel": [
        {
          "type": "webview",
          "id": "pixel-agents.panelView",
          "name": "Pixel Agents"
        }
      ]
    }
  },
  "scripts": {
    "vscode:prepublish": "npm run package",
    "build:webview": "cd webview-ui && npm run build",
    "compile": "npm run check-types && npm run lint && node esbuild.js && npm run build:webview",
    "build": "npm run compile",
    "watch": "npm-run-all -p watch:*",
    "watch:esbuild": "node esbuild.js --watch",
    "watch:tsc": "tsc --noEmit --watch --project tsconfig.json",
    "package": "npm run check-types && npm run lint && node esbuild.js --production && npm run build:webview",
    "check-types": "tsc --noEmit",
    "prepare": "husky",
    "lint": "eslint src",
    "lint:fix": "eslint src --fix",
    "lint:webview": "cd webview-ui && npm run lint",
    "lint:webview:fix": "cd webview-ui && eslint . --fix",
    "import-tileset": "tsx scripts/import-tileset-cli.ts",
    "format": "prettier --write \"src/**/*.ts\" \"webview-ui/src/**/*.{ts,tsx,css}\" \"*.{js,mjs}\" \"webview-ui/*.{js,ts}\"",
    "format:check": "prettier --check \"src/**/*.ts\" \"webview-ui/src/**/*.{ts,tsx,css}\" \"*.{js,mjs}\" \"webview-ui/*.{js,ts}\""
  },
  "devDependencies": {
    "@anthropic-ai/sdk": "^0.78.0",
    "@types/node": "25.x",
    "@types/pngjs": "^6.0.5",
    "@types/vscode": "^1.105.0",
    "esbuild": "^0.27.2",
    "eslint": "^10.0.3",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-simple-import-sort": "^12.1.1",
    "husky": "^9.1.7",
    "lint-staged": "^16.3.2",
    "npm-run-all": "^4.1.5",
    "pngjs": "^7.0.0",
    "prettier": "^3.8.1",
    "tsx": "^4.21.0",
    "typescript": "^5.9.3",
    "typescript-eslint": "^8.54.0"
  },
  "lint-staged": {
    "src/**/*.ts": "eslint --fix",
    "webview-ui/src/**/*.{ts,tsx}": "eslint --fix",
    "*.{ts,tsx,js,mjs,css,json,md}": "prettier --write",
    "webview-ui/**/*.{ts,tsx,js,css,json}": "prettier --write"
  }
}
```

## File: `README.md`
```markdown
<h1 align="center">
    <a href="https://github.com/pablodelucca/pixel-agents/discussions">
        <img src="webview-ui/public/banner.png" alt="Pixel Agents">
    </a>
</h1>

<h2 align="center" style="padding-bottom: 20px;">
  The game interface where AI agents build real things
</h2>

<div align="center" style="margin-top: 25px;">

[![vscode-version](https://img.shields.io/visual-studio-marketplace/v/pablodelucca.pixel-agents?logo=visualstudiocode&color=0183ff)](https://marketplace.visualstudio.com/items?itemName=pablodelucca.pixel-agents)
[![installs](https://img.shields.io/visual-studio-marketplace/i/pablodelucca.pixel-agents?color=0183ff&style=flat)](https://marketplace.visualstudio.com/items?itemName=pablodelucca.pixel-agents)
[![stars](https://img.shields.io/github/stars/pablodelucca/pixel-agents?logo=github&color=0183ff&style=flat)](https://github.com/pablodelucca/pixel-agents/stargazers)
[![license](https://img.shields.io/github/license/pablodelucca/pixel-agents?color=0183ff&style=flat)](https://github.com/pablodelucca/pixel-agents/blob/main/LICENSE)

</div>

<div align="center">
<a href="https://marketplace.visualstudio.com/items?itemName=pablodelucca.pixel-agents">🛒 VS Code Marketplace</a> • <a href="https://github.com/pablodelucca/pixel-agents/discussions">💬 Discussions</a> • <a href="https://github.com/pablodelucca/pixel-agents/issues">🐛 Issues</a> • <a href="CONTRIBUTING.md">🤝 Contributing</a>
</div>

<br/>

Pixel Agents turns multi-agent AI systems into something you can actually see and manage. Each agent becomes a character in a pixel art office. They walk around, sit at their desk, and visually reflect what they are doing — typing when writing code, reading when searching files, waiting when it needs your attention.

Right now it works as a VS Code extension with Claude Code. The vision though, is a fully agent-agnostic, platform-agnostic interface for orchestrating any AI agents, deployable anywhere.

This is the source code for the free Pixel Agents extension for VS Code — install from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=pablodelucca.pixel-agents) or [Open VSX](https://open-vsx.org/extension/pablodelucca/pixel-agents) with the full furniture catalog included.

![Pixel Agents screenshot](webview-ui/public/Screenshot.jpg)

## Features

- **One agent, one character** — every Claude Code terminal gets its own animated character
- **Live activity tracking** — characters animate based on what the agent is actually doing (writing, reading, running commands)
- **Office layout editor** — design your office with floors, walls, and furniture using a built-in editor
- **Speech bubbles** — visual indicators when an agent is waiting for input or needs permission
- **Sound notifications** — optional chime when an agent finishes its turn
- **Sub-agent visualization** — Task tool sub-agents spawn as separate characters linked to their parent
- **Persistent layouts** — your office design is saved and shared across VS Code windows
- **Diverse characters** — 6 diverse characters. These are based on the amazing work of [JIK-A-4, Metro City](https://jik-a-4.itch.io/metrocity-free-topdown-character-pack).

<p align="center">
  <img src="webview-ui/public/characters.png" alt="Pixel Agents characters" width="320" height="72" style="image-rendering: pixelated;">
</p>

## Requirements

- VS Code 1.105.0 or later
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and configured

## Getting Started

If you just want to use Pixel Agents, the easiest way is to download the [VS Code extension](https://marketplace.visualstudio.com/items?itemName=pablodelucca.pixel-agents). If you want to play with the code, develop, or contribute, then:

### Install from source

```bash
git clone https://github.com/pablodelucca/pixel-agents.git
cd pixel-agents
npm install
cd webview-ui && npm install && cd ..
npm run build
```

Then press **F5** in VS Code to launch the Extension Development Host.

### Usage

1. Open the **Pixel Agents** panel (it appears in the bottom panel area alongside your terminal)
2. Click **+ Agent** to spawn a new Claude Code terminal and its character
3. Start coding with Claude — watch the character react in real time
4. Click a character to select it, then click a seat to reassign it
5. Click **Layout** to open the office editor and customize your space

## Layout Editor

The built-in editor lets you design your office:

- **Floor** — Full HSB color control
- **Walls** — Auto-tiling walls with color customization
- **Tools** — Select, paint, erase, place, eyedropper, pick
- **Undo/Redo** — 50 levels with Ctrl+Z / Ctrl+Y
- **Export/Import** — Share layouts as JSON files via the Settings modal

The grid is expandable up to 64×64 tiles. Click the ghost border outside the current grid to grow it.

### Office Assets

All office assets (furniture, floors, walls) are now **fully open-source** and included in this repository under `webview-ui/public/assets/`. No external purchases or imports are needed — everything works out of the box.

Each furniture item lives in its own folder under `assets/furniture/` with a `manifest.json` that declares its sprites, rotation groups, state groups (on/off), and animation frames. Floor tiles are individual PNGs in `assets/floors/`, and wall tile sets are in `assets/walls/`. This modular structure makes it easy to add, remove, or modify assets without touching any code.

To add a new furniture item, create a folder in `webview-ui/public/assets/furniture/` with your PNG sprite(s) and a `manifest.json`, then rebuild. The asset manager (`scripts/asset-manager.html`) provides a visual editor for creating and editing manifests.

Detailed documentation on the manifest format and asset pipeline is coming soon.

Characters are based on the amazing work of [JIK-A-4, Metro City](https://jik-a-4.itch.io/metrocity-free-topdown-character-pack).

## How It Works

Pixel Agents watches Claude Code's JSONL transcript files to track what each agent is doing. When an agent uses a tool (like writing a file or running a command), the extension detects it and updates the character's animation accordingly. No modifications to Claude Code are needed — it's purely observational.

The webview runs a lightweight game loop with canvas rendering, BFS pathfinding, and a character state machine (idle → walk → type/read). Everything is pixel-perfect at integer zoom levels.

## Tech Stack

- **Extension**: TypeScript, VS Code Webview API, esbuild
- **Webview**: React 19, TypeScript, Vite, Canvas 2D

## Known Limitations

- **Agent-terminal sync** — the way agents are connected to Claude Code terminal instances is not super robust and sometimes desyncs, especially when terminals are rapidly opened/closed or restored across sessions.
- **Heuristic-based status detection** — Claude Code's JSONL transcript format does not provide clear signals for when an agent is waiting for user input or when it has finished its turn. The current detection is based on heuristics (idle timers, turn-duration events) and often misfires — agents may briefly show the wrong status or miss transitions.
- **Windows-only testing** — the extension has only been tested on Windows 11. It may work on macOS or Linux, but there could be unexpected issues with file watching, paths, or terminal behavior on those platforms.

## Where This Is Going

The long-term vision is an interface where managing AI agents feels like playing the Sims, but the results are real things built.

- **Agents as characters** you can see, assign, monitor, and redirect, each with visible roles (designer, coder, writer, reviewer), stats, context usage, and tools.
- **Desks as directories** — drag an agent to a desk to assign it to a project or working directory.
- **An office as a project** — with a Kanban board on the wall where idle agents can pick up tasks autonomously.
- **Deep inspection** — click any agent to see its model, branch, system prompt, and full work history. Interrupt it, chat with it, or redirect it.
- **Token health bars** — rate limits and context windows visualized as in-game stats.
- **Fully customizable** — upload your own character sprites, themes, and office assets. Eventually maybe even move beyond pixel art into 3D or VR.

For this to work, the architecture needs to be modular at every level:

- **Platform-agnostic**: VS Code extension today, Electron app, web app, or any other host environment tomorrow.
- **Agent-agnostic**: Claude Code today, but built to support Codex, OpenCode, Gemini, Cursor, Copilot, and others through composable adapters.
- **Theme-agnostic**: community-created assets, skins, and themes from any contributor.

We're actively working on the core module and adapter architecture that makes this possible. If you're interested to talk about this further, please visit our [Discussions Section](https://github.com/pablodelucca/pixel-agents/discussions).


## Community & Contributing

We use **[GitHub Discussions](https://github.com/pablodelucca/pixel-agents/discussions)** for questions, feature ideas, and conversations. **[Issues](https://github.com/pablodelucca/pixel-agents/issues)** are for bug reports only.

If something is broken, open an issue. For everything else, start a discussion.

See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on how to contribute.

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## Supporting the Project

If you find Pixel Agents useful, consider supporting its development:

<a href="https://github.com/sponsors/pablodelucca">
  <img src="https://img.shields.io/badge/Sponsor-GitHub-ea4aaa?logo=github" alt="GitHub Sponsors">
</a>
<a href="https://ko-fi.com/pablodelucca">
  <img src="https://img.shields.io/badge/Support-Ko--fi-ff5e5b?logo=ko-fi" alt="Ko-fi">
</a>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=pablodelucca/pixel-agents&type=Date)](https://www.star-history.com/?repos=pablodelucca%2Fpixel-agents&type=date&legend=bottom-right)

## License

This project is licensed under the [MIT License](LICENSE).
```

## File: `SECURITY.md`
```markdown
# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x.x   | :white_check_mark: |

## Reporting a Vulnerability

Please report security vulnerabilities through [GitHub's private vulnerability reporting](https://github.com/pablodelucca/pixel-agents/security/advisories/new).

**Do not open a public issue for security vulnerabilities.**

We will acknowledge your report within 7 days and aim to release a fix within 30 days of confirmation.

## Scope

Security issues relevant to this project include:

- Command injection via terminal spawning or JSONL parsing
- Arbitrary file read/write beyond intended paths
- Cross-site scripting (XSS) in the webview
- Sensitive data exposure (e.g., leaking terminal output or session content)
```

## File: `tsconfig.json`
```json
{
	"compilerOptions": {
		"module": "Node16",
		"target": "ES2022",
		"lib": [
			"ES2022"
		],
		"sourceMap": true,
		"rootDir": "src",
		"strict": true
	},
	"exclude": [
		"node_modules",
		"webview-ui",
		"dist",
		"out",
		"scripts"
	]
}
```

## File: `eslint-rules/pixel-agents-rules.mjs`
```
/**
 * Shared ESLint plugin for pixel-agents project conventions.
 *
 * Rules:
 *   no-inline-colors  — flag hex/rgb/rgba/hsl/hsla color literals (centralize in constants)
 *   pixel-shadow      — flag box-shadow values not using var(--pixel-shadow) or 2px 2px 0px
 *   pixel-font        — flag font-family values not referencing FS Pixel Sans
 */

const HEX_COLOR = /#[0-9a-fA-F]{3,8}\b/;
const RGB_FUNC = /\brgba?\s*\(/;
const HSL_FUNC = /\bhsla?\s*\(/;
const COLOR_PATTERNS = [HEX_COLOR, RGB_FUNC, HSL_FUNC];

/** Check whether a raw string value contains a color literal. */
function containsColor(value) {
  return COLOR_PATTERNS.some((p) => p.test(value));
}

/** Check whether the node is inside a comment-like context (template literal tag, etc.) */
function isCommentOnly(value) {
  const trimmed = value.trim();
  return trimmed.startsWith('//') || trimmed.startsWith('/*') || trimmed.startsWith('*');
}

const noInlineColors = {
  meta: {
    type: 'suggestion',
    docs: {
      description:
        'Disallow inline color literals (hex, rgb, rgba, hsl, hsla). Use shared constants or --pixel-* CSS tokens.',
    },
    schema: [],
    messages: {
      found: 'Use shared constants or `--pixel-*` tokens instead of inline color literals.',
    },
  },
  create(context) {
    return {
      Literal(node) {
        if (typeof node.value !== 'string') return;
        if (isCommentOnly(node.value)) return;
        if (containsColor(node.value)) {
          context.report({ node, messageId: 'found' });
        }
      },
      TemplateLiteral(node) {
        for (const quasi of node.quasis) {
          if (containsColor(quasi.value.raw)) {
            context.report({ node: quasi, messageId: 'found' });
          }
        }
      },
    };
  },
};

/**
 * Helper: check if an AST Property node has a key matching `boxShadow` or `box-shadow`.
 */
function isBoxShadowProperty(node) {
  if (node.type !== 'Property') return false;
  const key = node.key;
  if (key.type === 'Identifier' && key.name === 'boxShadow') return true;
  if (key.type === 'Literal' && key.value === 'box-shadow') return true;
  return false;
}

const pixelShadow = {
  meta: {
    type: 'suggestion',
    docs: {
      description:
        'Require box-shadow values to use var(--pixel-shadow) or the 2px 2px 0px pattern.',
    },
    schema: [],
    messages: {
      found: 'Use `var(--pixel-shadow)` or a hard offset `2px 2px 0px` shadow.',
    },
  },
  create(context) {
    return {
      Property(node) {
        if (!isBoxShadowProperty(node)) return;
        const value = node.value;
        if (value.type !== 'Literal' || typeof value.value !== 'string') return;
        const text = value.value;
        if (text.includes('var(--pixel-shadow)') || text.includes('2px 2px 0px')) return;
        context.report({ node: value, messageId: 'found' });
      },
    };
  },
};

/**
 * Helper: check if an AST Property node has a key matching `fontFamily` or `font-family`.
 */
function isFontFamilyProperty(node) {
  if (node.type !== 'Property') return false;
  const key = node.key;
  if (key.type === 'Identifier' && key.name === 'fontFamily') return true;
  if (key.type === 'Literal' && key.value === 'font-family') return true;
  return false;
}

const pixelFont = {
  meta: {
    type: 'suggestion',
    docs: {
      description: 'Require font-family values to reference FS Pixel Sans.',
    },
    schema: [],
    messages: {
      found: 'Use the FS Pixel Sans font for UI styling.',
    },
  },
  create(context) {
    return {
      Property(node) {
        if (!isFontFamilyProperty(node)) return;
        const value = node.value;
        if (value.type !== 'Literal' || typeof value.value !== 'string') return;
        if (value.value.includes('FS Pixel Sans')) return;
        context.report({ node: value, messageId: 'found' });
      },
    };
  },
};

const plugin = {
  meta: {
    name: 'eslint-plugin-pixel-agents',
    version: '1.0.0',
  },
  rules: {
    'no-inline-colors': noInlineColors,
    'pixel-shadow': pixelShadow,
    'pixel-font': pixelFont,
  },
};

export default plugin;
```

## File: `scripts/asset-manager.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Asset Manager</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { height: 100%; }
    body { background: #1a1a2e; color: #e0e0e0; font-family: 'Segoe UI', system-ui, sans-serif; display: flex; flex-direction: column; overflow: hidden; }

    /* Toolbar */
    #toolbar { padding: 8px 12px; background: #16213e; border-bottom: 1px solid #333; display: flex; gap: 8px; align-items: center; flex-wrap: wrap; }
    #toolbar button, #toolbar select { font-size: 12px; padding: 5px 10px; border-radius: 3px; border: 1px solid #555; background: #2a2a4a; color: #e0e0e0; cursor: pointer; }
    #toolbar button:hover { background: #1a5276; }
    #toolbar button.primary { background: #27ae60; border-color: #2ecc71; font-weight: 600; }
    #toolbar button.primary:hover { background: #2ecc71; }
    #toolbar label { font-size: 11px; color: #aaa; }
    .sep { width: 1px; height: 22px; background: #444; flex-shrink: 0; }

    /* Main 3-panel layout */
    #main { flex: 1; display: flex; min-height: 0; overflow: hidden; }

    /* Left: Asset List */
    #list-panel { width: 260px; display: flex; flex-direction: column; background: #16213e; border-right: 1px solid #333; flex-shrink: 0; }
    #list-header { padding: 8px 10px; font-size: 12px; font-weight: 600; border-bottom: 1px solid #333; background: #0f3460; display: flex; justify-content: space-between; align-items: center; }
    #search-box { padding: 6px 8px; border-bottom: 1px solid #333; }
    #search-box input { width: 100%; padding: 5px 8px; background: #2a2a4a; border: 1px solid #555; color: #e0e0e0; border-radius: 2px; font-size: 11px; }
    #asset-list { flex: 1; overflow-y: auto; padding: 2px 0; }
    .asset-item {
      padding: 6px 8px; margin: 1px 4px; border-radius: 3px; cursor: pointer;
      display: flex; gap: 8px; align-items: center;
      background: #1a1a3e; border: 1px solid transparent; transition: border-color 0.15s;
    }
    .asset-item:hover { border-color: #555; }
    .asset-item.selected { border-color: #3498db; background: #1a3a5e; }
    .asset-item.discarded { opacity: 0.45; }
    .asset-thumb { width: 40px; height: 40px; flex-shrink: 0; image-rendering: pixelated; background: #000; border: 1px solid #444; border-radius: 2px; }
    .asset-meta { flex: 1; min-width: 0; }
    .asset-meta .name { font-weight: 600; font-size: 11px; color: #eee; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .asset-meta .dims { font-size: 9px; color: #888; margin-top: 1px; }
    .asset-meta .cat { font-size: 9px; color: #6aa; margin-top: 1px; }
    .badge { display: inline-block; padding: 1px 5px; border-radius: 2px; font-size: 8px; font-weight: 600; margin-left: 4px; vertical-align: middle; }
    .badge-discard { background: #c0392b; color: #fff; }

    /* Resize handle */
    .resize-handle { width: 4px; background: #333; cursor: col-resize; user-select: none; flex-shrink: 0; }
    .resize-handle:hover { background: #3498db; }

    /* Center: Split preview panel */
    #center-panel { flex: 1; display: flex; flex-direction: row; min-width: 400px; }

    /* Left half: Tileset */
    #tileset-pane { flex: 1; display: flex; flex-direction: column; background: #1a1a2e; border-right: 1px solid #333; min-width: 150px; }
    #tileset-pane .pane-header { padding: 8px 10px; font-size: 12px; font-weight: 600; border-bottom: 1px solid #333; background: #0f3460; display: flex; justify-content: space-between; align-items: center; }
    #tileset-pane .pane-header select { font-size: 11px; padding: 2px 6px; background: #2a2a4a; border: 1px solid #555; color: #e0e0e0; border-radius: 2px; cursor: pointer; }
    #tileset-pane .pane-header label { font-size: 10px; color: #aaa; }
    #tileset-wrap { flex: 1; overflow: auto; background: #111; position: relative; cursor: default; }
    #tileset-canvas { display: block; image-rendering: pixelated; }
    #select-rect { position: absolute; border: 2px solid #2ecc71; background: rgba(46,204,113,0.15); pointer-events: none; display: none; }
    #tileset-empty { flex: 1; display: flex; align-items: center; justify-content: center; color: #555; font-size: 12px; }
    .add-mode-bar { padding: 5px 10px; background: #1a3a1a; border-bottom: 1px solid #2a5a2a; display: flex; gap: 10px; align-items: center; font-size: 11px; flex-shrink: 0; }
    .add-mode-bar span { color: #8c8; }
    .add-mode-bar button { font-size: 11px; padding: 3px 10px; background: #6b2020; border: 1px solid #8b3030; color: #e0e0e0; border-radius: 2px; cursor: pointer; }
    .add-mode-bar button:hover { background: #8b3030; }

    /* Center resize handle */
    #handle-center { width: 4px; background: #333; cursor: col-resize; user-select: none; flex-shrink: 0; }
    #handle-center:hover { background: #3498db; }

    /* Right half: Asset preview */
    #preview-pane { flex: 1; display: flex; flex-direction: column; background: #1a1a2e; min-width: 150px; }
    #preview-pane .pane-header { padding: 8px 10px; font-size: 12px; font-weight: 600; border-bottom: 1px solid #333; background: #0f3460; display: flex; justify-content: space-between; align-items: center; }
    #preview-pane .pane-header select { font-size: 11px; padding: 2px 6px; background: #2a2a4a; border: 1px solid #555; color: #e0e0e0; border-radius: 2px; cursor: pointer; }
    #preview-container { flex: 1; display: flex; align-items: center; justify-content: center; padding: 12px; overflow: auto; }
    #preview-canvas { image-rendering: pixelated; border: 2px solid #555; background: #000; }
    #preview-canvas.invalid { border-color: #e74c3c; }
    #preview-canvas.eraser-active { cursor: crosshair; }
    #preview-tools { display: flex; gap: 6px; align-items: center; }
    #preview-tools button { font-size: 10px; padding: 2px 8px; background: #2a2a4a; border: 1px solid #555; color: #e0e0e0; border-radius: 2px; cursor: pointer; }
    #preview-tools button:hover { background: #3a3a6a; }
    #preview-tools button.active { background: #c0392b; border-color: #e74c3c; color: #fff; }
    #preview-tools button.clear-btn:hover { background: #6b2020; }
    #eraser-info { font-size: 9px; color: #e74c3c; display: none; }
    #eraser-info.visible { display: inline; }

    .dropdown-item { display:block; width:100%; text-align:left; padding:6px 12px; font-size:12px; border:none; background:none; color:#e0e0e0; cursor:pointer; }
    .dropdown-item:hover { background:#1a5276; }
    #toolbar button.add-btn { background: #1a5a2a; border-color: #2a8a3a; }
    #toolbar button.add-btn:hover { background: #2a8a3a; }
    #toolbar button.add-btn.active { background: #2ecc71; border-color: #27ae60; color: #000; font-weight: 600; }

    /* Right: Editor */
    #editor-panel { width: 340px; display: flex; flex-direction: column; background: #16213e; flex-shrink: 0; }
    #editor-header { padding: 8px 10px; font-size: 12px; font-weight: 600; border-bottom: 1px solid #333; background: #0f3460; }
    #editor-form { flex: 1; overflow-y: auto; padding: 12px; }

    .section-title { font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: 0.8px; margin: 14px 0 8px; padding-bottom: 4px; border-bottom: 1px solid #333; font-weight: 600; }
    .section-title:first-child { margin-top: 0; }

    .field { margin-bottom: 10px; }
    .field-label { font-size: 10px; color: #aaa; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 3px; display: block; font-weight: 600; }
    .field input[type="text"], .field input[type="number"], .field select {
      width: 100%; padding: 5px 7px; background: #2a2a4a; border: 1px solid #555; color: #e0e0e0; border-radius: 2px; font-size: 11px;
    }
    .field input:focus, .field select:focus { outline: none; border-color: #3498db; }
    .field input[readonly] { background: #1a1a3e; cursor: not-allowed; color: #888; }

    .geo-row { display: flex; gap: 6px; align-items: center; margin-bottom: 6px; }
    .geo-row label { font-size: 10px; color: #aaa; width: 16px; text-align: right; flex-shrink: 0; }
    .geo-row input { flex: 1; min-width: 0; }
    .geo-row .step-btn { padding: 2px 6px; font-size: 10px; background: #2a2a4a; border: 1px solid #555; color: #e0e0e0; border-radius: 2px; cursor: pointer; flex-shrink: 0; line-height: 1; }
    .geo-row .step-btn:hover { background: #3a3a6a; }
    .geo-row .step-spacer { width: 28px; flex-shrink: 0; }
    .geo-row .fp-label { font-size: 9px; color: #6aa; width: 40px; text-align: right; flex-shrink: 0; }

    .field-row { display: flex; gap: 8px; }
    .field-row .field { flex: 1; }
    .field-hint { font-size: 9px; color: #888; margin-top: 3px; line-height: 1.3; }

    .checkbox-group { display: flex; flex-direction: column; gap: 6px; }
    .checkbox-item { display: flex; align-items: center; gap: 6px; }
    .checkbox-item input[type="checkbox"] { width: 15px; height: 15px; cursor: pointer; flex-shrink: 0; accent-color: #3498db; }
    .checkbox-item label { cursor: pointer; font-size: 11px; }

    .asset-item.multi-selected { border-color: #9b59b6; background: #2a1a3e; }
    .badge-group { display: inline-block; padding: 1px 5px; border-radius: 2px; font-size: 8px; font-weight: 600; margin-left: 4px; vertical-align: middle; }
    .badge-group-rotation { background: #1a4a6a; color: #5dade2; }
    .badge-group-state { background: #4a3a0a; color: #f1c40f; }
    .badge-group-animation { background: #1a4a2a; color: #2ecc71; }
    .group-type-btn { font-size: 10px; padding: 4px 10px; border: 1px solid #555; background: #2a2a4a; color: #aaa; border-radius: 2px; cursor: pointer; flex: 1; text-align: center; }
    .group-type-btn:hover { background: #3a3a6a; }
    .group-type-btn.selected { background: #1a5276; border-color: #2980b9; color: #e0e0e0; font-weight: 600; }
    .group-member-row { display: flex; gap: 6px; align-items: center; padding: 4px 0; border-bottom: 1px solid #2a2a4a; font-size: 11px; }
    .group-member-row .gm-thumb { width: 24px; height: 24px; flex-shrink: 0; image-rendering: pixelated; background: #000; border: 1px solid #444; border-radius: 2px; }
    .group-member-row .gm-name { flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .group-member-row select { font-size: 10px; padding: 2px 4px; background: #2a2a4a; border: 1px solid #555; color: #e0e0e0; border-radius: 2px; width: 70px; flex-shrink: 0; }

    /* Group wrapper in asset list */
    .group-wrapper {
      margin: 3px 4px; border: 1px solid #333; border-radius: 4px; background: #161630; overflow: hidden;
    }
    .group-wrapper.group-selected { border-color: #9b59b6; background: #1e1640; }
    .group-wrapper .group-header {
      padding: 4px 8px; font-size: 10px; font-weight: 600; color: #aaa; background: #1a1a3e;
      border-bottom: 1px solid #2a2a4a; display: flex; justify-content: space-between; align-items: center; cursor: pointer;
    }
    .group-wrapper.group-selected .group-header { color: #c9a0dc; background: #231845; }
    .group-wrapper .group-header .group-header-type { font-size: 8px; font-weight: 600; padding: 1px 5px; border-radius: 2px; }
    .group-wrapper .group-header .group-header-type.rotation { background: #1a4a6a; color: #5dade2; }
    .group-wrapper .group-header .group-header-type.state { background: #4a3a0a; color: #f1c40f; }
    .group-wrapper .group-header .group-header-type.animation { background: #1a4a2a; color: #2ecc71; }
    .group-wrapper .asset-item { margin: 0; border-radius: 0; border-left: none; border-right: none; border-top: none; border-bottom: 1px solid #2a2a4a; }
    .group-wrapper .asset-item:last-child { border-bottom: none; }

    /* Compound group: member unit rows */
    .group-member-row.group-unit { background: #1a1a3e; border-radius: 2px; padding: 5px 6px; }
    .group-member-row .gm-type-badge { font-size: 8px; font-weight: 600; padding: 1px 5px; border-radius: 2px; margin-right: 4px; flex-shrink: 0; }
    .gm-type-badge.animation { background: #1a4a2a; color: #2ecc71; }
    .gm-type-badge.state { background: #4a3a0a; color: #f1c40f; }
    .gm-type-badge.rotation { background: #1a4a6a; color: #5dade2; }
    /* Nested group wrappers */
    .group-wrapper .group-wrapper { margin: 0; border-left: 2px solid #444; border-top: none; border-right: none; border-bottom: none; border-radius: 0; background: #141428; }
    .group-wrapper .group-wrapper.group-selected { border-left-color: #9b59b6; background: #1e1640; }
    .group-wrapper .group-wrapper .group-header { background: #161630; font-size: 9px; padding: 3px 8px; }
    .group-wrapper .group-wrapper.group-selected .group-header { color: #c9a0dc; background: #231845; }
    .group-wrapper .group-wrapper .asset-item { background: #141428; }
    .group-wrapper .group-wrapper .asset-item.selected { border-color: #3498db; background: #1a3a5e; }
    .group-wrapper .group-wrapper .asset-item.multi-selected { border-color: #9b59b6; background: #2a1a3e; }

    .discard-section { padding: 8px 10px; margin-top: 6px; background: #4a1a1a; border: 1px solid #6b2020; border-radius: 3px; }
    .discard-section label { color: #ff9988; font-weight: 600; }

    #btn-redraw:hover { background: #2980b9 !important; }

    #editor-buttons { padding: 10px 12px; border-top: 1px solid #333; display: flex; gap: 8px; }
    #editor-buttons button { flex: 1; padding: 6px 10px; font-size: 11px; border-radius: 3px; border: 1px solid #555; background: #2a2a4a; color: #e0e0e0; cursor: pointer; }
    #editor-buttons button:hover { background: #3a3a6a; }
    #editor-buttons button.primary { background: #27ae60; border-color: #2ecc71; font-weight: 600; }
    #editor-buttons button.primary:hover { background: #2ecc71; }

    /* Status bar */
    #status { padding: 6px 12px; background: #0f3460; font-size: 11px; color: #888; border-top: 1px solid #333; display: flex; justify-content: space-between; }

    /* Scrollbar styling */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: #1a1a2e; }
    ::-webkit-scrollbar-thumb { background: #444; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #555; }
  </style>
</head>
<body>

<!-- Toolbar -->
<div id="toolbar">
  <div style="position:relative; display:inline-block;">
    <button id="btn-file-menu" style="background:#1a5276; border-color:#2980b9; font-weight:600;">File ▾</button>
    <div id="file-dropdown" style="display:none; position:absolute; top:100%; left:0; margin-top:2px; background:#2a2a4a; border:1px solid #555; border-radius:3px; min-width:140px; z-index:100; box-shadow:0 4px 12px rgba(0,0,0,0.4);">
      <button id="btn-new-project" class="dropdown-item">New</button>
      <button id="btn-load-json" class="dropdown-item">Load JSON</button>
      <div style="height:1px; background:#444; margin:2px 0;"></div>
      <button id="btn-save-file" class="dropdown-item" style="display:none">Save</button>
      <button id="btn-save-as" class="dropdown-item">Save As</button>
    </div>
  </div>
  <button id="btn-load-png">Load Tileset</button>
  <span class="sep"></span>
  <label>Filter:</label>
  <select id="filter-cat">
    <option value="">All categories</option>
    <option value="desks">Desks</option>
    <option value="chairs">Chairs</option>
    <option value="storage">Storage</option>
    <option value="decor">Decor</option>
    <option value="electronics">Electronics</option>
    <option value="wall">Wall</option>
    <option value="misc">Misc</option>
  </select>
  <span class="sep"></span>
  <button class="add-btn" id="btn-add-asset">+ Add Asset</button>
  <button id="btn-duplicate" title="Duplicate selected asset">Duplicate</button>
  <div style="flex:1;"></div>
  <button id="btn-export" style="background:#8e44ad; border-color:#9b59b6; font-weight:600;">Export Assets</button>
</div>

<!-- Main 3-panel layout -->
<div id="main">
  <!-- Left: Asset List -->
  <div id="list-panel">
    <div id="list-header">
      <span>Assets</span>
      <span id="counter" style="font-weight: 400; color: #aaa;">0 / 0</span>
    </div>
    <div id="search-box">
      <input type="text" id="search" placeholder="Search label or ID...">
    </div>
    <div id="asset-list"></div>
  </div>

  <div class="resize-handle" id="handle-left"></div>

  <!-- Center: Split panes -->
  <div id="center-panel">
    <!-- Left half: Tileset overview -->
    <div id="tileset-pane">
      <div class="pane-header">
        <span>Tileset</span>
        <div style="display:flex; gap:6px; align-items:center;">
          <label>Zoom:</label>
          <select id="tileset-zoom">
            <option value="1">1x</option>
            <option value="2" selected>2x</option>
            <option value="3">3x</option>
            <option value="4">4x</option>
          </select>
          <label><input type="checkbox" id="snap-grid" checked> Snap 16px</label>
        </div>
      </div>
      <div class="add-mode-bar" id="add-mode-bar" style="display:none">
        <span id="add-mode-label">Drag to select a region on the tileset</span>
        <button id="btn-cancel-add">Cancel</button>
      </div>
      <div id="tileset-wrap">
        <canvas id="tileset-canvas"></canvas>
        <div id="select-rect"></div>
      </div>
      <div id="tileset-empty">Load a PNG to view the tileset</div>
    </div>

    <div id="handle-center"></div>

    <!-- Right half: Asset preview -->
    <div id="preview-pane">
      <div class="pane-header">
        <span>Asset Preview</span>
        <div id="preview-tools">
          <button id="btn-eraser">Eraser</button>
          <button id="btn-clear-erased" class="clear-btn">Clear Erased</button>
          <span id="eraser-info">click/drag to erase pixels</span>
          <label style="font-size:10px; color:#aaa; margin-right:4px;">Zoom:</label>
          <select id="preview-zoom">
            <option value="1">1x</option>
            <option value="2">2x</option>
            <option value="3">3x</option>
            <option value="4" selected>4x</option>
            <option value="6">6x</option>
            <option value="8">8x</option>
          </select>
        </div>
      </div>
      <div id="preview-container">
        <canvas id="preview-canvas"></canvas>
      </div>
    </div>
  </div>

  <div class="resize-handle" id="handle-right"></div>

  <!-- Right: Editor -->
  <div id="editor-panel">
    <div id="editor-header">Editor</div>
    <div id="editor-form">
      <!-- Geometry -->
      <div class="section-title">Geometry <button id="btn-redraw" style="float:right; font-size:10px; padding:2px 8px; background:#1a5276; border:1px solid #2980b9; color:#e0e0e0; border-radius:2px; cursor:pointer; text-transform:none; letter-spacing:0; font-weight:400;" title="Visually reselect this asset's region on the tileset">Redraw on Tileset</button></div>
      <div class="geo-row">
        <label>X:</label>
        <button class="step-btn" data-field="paddedX" data-delta="-16">-16</button>
        <button class="step-btn" data-field="paddedX" data-delta="-1">-1</button>
        <input id="geo-x" type="number">
        <button class="step-btn" data-field="paddedX" data-delta="1">+1</button>
        <button class="step-btn" data-field="paddedX" data-delta="16">+16</button>
      </div>
      <div class="geo-row">
        <label>Y:</label>
        <button class="step-btn" data-field="paddedY" data-delta="-16">-16</button>
        <button class="step-btn" data-field="paddedY" data-delta="-1">-1</button>
        <input id="geo-y" type="number">
        <button class="step-btn" data-field="paddedY" data-delta="1">+1</button>
        <button class="step-btn" data-field="paddedY" data-delta="16">+16</button>
      </div>
      <div class="geo-row">
        <label>W:</label>
        <button class="step-btn" data-field="paddedWidth" data-delta="-16">-16</button>
        <span class="step-spacer"></span>
        <input id="geo-w" type="number" min="16" step="16">
        <span class="step-spacer"></span>
        <button class="step-btn" data-field="paddedWidth" data-delta="16">+16</button>
        <span id="fp-w" class="fp-label"></span>
      </div>
      <div class="geo-row">
        <label>H:</label>
        <button class="step-btn" data-field="paddedHeight" data-delta="-16">-16</button>
        <span class="step-spacer"></span>
        <input id="geo-h" type="number" min="16" step="16">
        <span class="step-spacer"></span>
        <button class="step-btn" data-field="paddedHeight" data-delta="16">+16</button>
        <span id="fp-h" class="fp-label"></span>
      </div>

      <!-- Metadata -->
      <div class="section-title">Metadata</div>
      <div class="field">
        <label class="field-label">Label</label>
        <input id="f-label" type="text" placeholder="e.g., Small Wood Desk">
      </div>
      <div class="field">
        <label class="field-label">ID <span style="font-weight:400; text-transform:none; letter-spacing:0;">(auto-generated from label, editable)</span></label>
        <input id="f-id" type="text" placeholder="e.g., SMALL_WOOD_DESK">
      </div>
      <div id="individual-category-flags">
        <div class="field">
          <label class="field-label">Category</label>
          <select id="f-category">
            <option value="desks">Desks</option>
            <option value="chairs">Chairs</option>
            <option value="storage">Storage</option>
            <option value="decor">Decor</option>
            <option value="electronics">Electronics</option>
            <option value="wall">Wall</option>
            <option value="misc">Misc</option>
          </select>
        </div>

        <div class="field-row">
          <div class="field">
            <label class="field-label">Background Tiles</label>
            <input id="f-bgtiles" type="number" min="0" max="10" title="Number of top rows that allow placement behind this furniture">
            <div class="field-hint">Top rows where other items can be placed behind (shown <span style="color:#5dade2">blue</span> in preview)</div>
          </div>
        </div>

        <!-- Flags -->
        <div class="section-title">Flags</div>
        <div class="checkbox-group">
          <div class="checkbox-item">
            <input id="f-walls" type="checkbox">
            <label for="f-walls">Can Place On Walls</label>
          </div>
          <div class="checkbox-item">
            <input id="f-ontop" type="checkbox">
            <label for="f-ontop">Can Place On Surfaces</label>
          </div>
        </div>
      </div>

      <!-- Group Membership (shown when asset is in a group) -->
      <div id="group-membership" style="display:none">
        <div class="section-title">Group Membership</div>
        <div id="group-info" style="font-size:11px; line-height:1.6;"></div>
        <div style="display:flex; gap:6px; margin-top:8px;">
          <button id="btn-edit-group" style="font-size:10px; padding:3px 8px; background:#2a2a4a; border:1px solid #555; color:#e0e0e0; border-radius:2px; cursor:pointer;">Edit Group</button>
          <button id="btn-dissolve-group" style="font-size:10px; padding:3px 8px; background:#4a3a0a; border:1px solid #6b5a10; color:#e0e0e0; border-radius:2px; cursor:pointer;">Dissolve Group</button>
          <button id="btn-remove-from-group" style="font-size:10px; padding:3px 8px; background:#4a1a1a; border:1px solid #6b2020; color:#e0e0e0; border-radius:2px; cursor:pointer;">Remove from Group</button>
        </div>
      </div>

      <!-- Multi-select group creation (shown when 2+ assets selected) -->
      <div id="group-creator" style="display:none">
        <div class="section-title">Create Group <span style="font-weight:400; text-transform:none; letter-spacing:0; color:#aaa;" id="group-creator-count"></span></div>
        <div class="field">
          <label class="field-label">Group Type</label>
          <div style="display:flex; gap:4px;">
            <button class="group-type-btn selected" data-type="rotation">Rotation</button>
            <button class="group-type-btn" data-type="state">State</button>
            <button class="group-type-btn" data-type="animation">Animation</button>
          </div>
        </div>
        <div class="field" id="rotation-scheme-field" style="display:none">
          <label class="field-label">Rotation Scheme</label>
          <select id="rotation-scheme">
            <option value="4-way">4-way (Front / Back / Left / Right)</option>
            <option value="3-way-mirror">3-way + Mirror (Front / Back / Side → Left mirrored)</option>
            <option value="2-way">2-way (Front / Side)</option>
          </select>
          <div class="field-hint" id="rotation-scheme-hint"></div>
        </div>
        <div class="field">
          <label class="field-label">Group Name</label>
          <input id="group-name-input" type="text" placeholder="e.g., Wooden Chair">
        </div>
        <div class="field">
          <label class="field-label">Group ID <span style="font-weight:400; text-transform:none; letter-spacing:0;">(auto-generated from name, editable)</span></label>
          <input id="group-id-input" type="text" placeholder="e.g., WOODEN_CHAIR">
        </div>
        <div class="field">
          <label class="field-label">Category</label>
          <select id="group-category">
            <option value="desks">Desks</option>
            <option value="chairs">Chairs</option>
            <option value="storage">Storage</option>
            <option value="decor">Decor</option>
            <option value="electronics">Electronics</option>
            <option value="wall">Wall</option>
            <option value="misc">Misc</option>
          </select>
        </div>
        <div class="field">
          <label class="field-label">Background Tiles</label>
          <input id="group-bgtiles" type="number" min="0" max="10" value="0" title="Number of top rows that allow placement behind this furniture">
        </div>
        <div class="checkbox-group" style="margin:8px 0;">
          <div class="checkbox-item">
            <input id="group-walls" type="checkbox">
            <label for="group-walls">Can Place On Walls</label>
          </div>
          <div class="checkbox-item">
            <input id="group-ontop" type="checkbox">
            <label for="group-ontop">Can Place On Surfaces</label>
          </div>
        </div>
        <div id="group-members-list"></div>
        <div id="group-validation" style="font-size:9px; color:#e74c3c; margin:6px 0; display:none;"></div>
        <div style="display:flex; gap:6px; margin-top:8px;">
          <button id="btn-create-group" class="primary" style="flex:1; font-size:11px; padding:5px 10px; border-radius:3px; border:1px solid #2ecc71; background:#27ae60; color:#e0e0e0; cursor:pointer; font-weight:600;">Create Group</button>
          <button id="btn-cancel-group" style="flex:1; font-size:11px; padding:5px 10px; border-radius:3px; border:1px solid #555; background:#2a2a4a; color:#e0e0e0; cursor:pointer;">Cancel</button>
        </div>
      </div>

      <!-- Discard -->
      <div class="section-title">Discard</div>
      <div class="discard-section">
        <div class="checkbox-item">
          <input id="f-discard" type="checkbox">
          <label for="f-discard">Mark as discarded</label>
        </div>
      </div>
    </div>

    <div id="editor-buttons">
      <button class="primary" id="btn-save">Save</button>
      <button id="btn-reset">Reset</button>
      <button id="btn-delete" style="background:#6b2020; border-color:#8b3030;" title="Delete this asset">Delete</button>
    </div>
  </div>
</div>

<!-- Export Modal -->
<div id="export-modal" style="display:none; position:fixed; top:0; left:0; right:0; bottom:0; background:rgba(0,0,0,0.6); z-index:1000; align-items:center; justify-content:center;">
  <div style="background:#1a1a2e; border:2px solid #8e44ad; border-radius:6px; width:480px; max-height:80vh; display:flex; flex-direction:column; box-shadow:0 8px 32px rgba(0,0,0,0.5);">
    <div style="padding:12px 16px; background:#16213e; border-bottom:1px solid #333; display:flex; justify-content:space-between; align-items:center;">
      <span style="font-weight:600; font-size:14px;">Export Assets</span>
      <button id="export-modal-close" style="background:none; border:none; color:#888; cursor:pointer; font-size:18px; padding:0 4px;">&times;</button>
    </div>
    <div style="padding:16px; overflow-y:auto;">
      <div id="export-summary" style="font-size:12px; line-height:1.6; margin-bottom:16px; padding:10px; background:#16213e; border:1px solid #333; border-radius:3px;"></div>
      <div style="margin-bottom:16px;">
        <label class="field-label">Folder Organization</label>
        <div style="display:flex; gap:8px; margin-top:6px;">
          <label style="display:flex; align-items:center; gap:4px; font-size:12px; cursor:pointer;">
            <input type="radio" name="export-org" value="flat" checked style="accent-color:#9b59b6;"> Flat
          </label>
          <label style="display:flex; align-items:center; gap:4px; font-size:12px; cursor:pointer;">
            <input type="radio" name="export-org" value="category" style="accent-color:#9b59b6;"> By Category
          </label>
        </div>
        <div class="field-hint" style="margin-top:4px;">Flat: <code>furniture/DESK/</code> &nbsp; By Category: <code>furniture/desks/DESK/</code></div>
      </div>
      <div id="export-progress" style="display:none; margin-bottom:12px;">
        <div style="font-size:11px; margin-bottom:4px;" id="export-progress-text">Exporting...</div>
        <div style="background:#2a2a4a; height:8px; border-radius:4px; overflow:hidden;">
          <div id="export-progress-bar" style="background:#9b59b6; height:100%; width:0%; transition:width 0.2s;"></div>
        </div>
      </div>
      <div id="export-result" style="display:none; font-size:12px; padding:10px; border-radius:3px; margin-bottom:12px;"></div>
    </div>
    <div style="padding:12px 16px; border-top:1px solid #333; display:flex; gap:8px; justify-content:flex-end;">
      <button id="export-cancel-btn" style="font-size:12px; padding:6px 16px; border-radius:3px; border:1px solid #555; background:#2a2a4a; color:#e0e0e0; cursor:pointer;">Cancel</button>
      <button id="export-start-btn" style="font-size:12px; padding:6px 16px; border-radius:3px; border:1px solid #9b59b6; background:#8e44ad; color:#e0e0e0; cursor:pointer; font-weight:600;">Export to Folder</button>
    </div>
  </div>
</div>

<!-- Status bar -->
<div id="status">
  <span id="status-msg">Ready</span>
  <span id="status-counts"></span>
</div>

<!-- Hidden file inputs -->
<input type="file" id="json-file" accept="application/json" style="display:none">
<input type="file" id="png-file" accept="image/png" style="display:none">

<script>
// ════════════════════════════════════════════════════════════════════════
// STATE
// ════════════════════════════════════════════════════════════════════════

let data = null          // Full JSON (version, assets[], etc.)
let tilesetImg = null    // Loaded tileset Image
let selectedIdx = -1     // Index into data.assets (primary selection for form/preview)
let selectedIndices = new Set()  // Multi-select set
let lastClickedIdx = -1  // Anchor for shift-click range select
let selectedGroupId = null // Currently group-selected group ID (first click selects group, second drills into item)
let selectedGroupUnits = new Set()  // Set of groupIds selected as compound units (for Ctrl+click on group headers)
let filtered = []        // Indices into data.assets matching current filter
let previewZoom = 4
let savedSnapshot = null // Deep copy for Reset button
let saveTimer = null     // Debounced localStorage save
let jsonFileHandle = null // File System Access API handle for direct save

// Add Asset mode / Redraw mode
let addMode = false
let redrawMode = false  // true when redrawing an existing asset's region
let tilesetZoom = 2
let dragStart = null     // {x, y} in tileset pixels
let dragEnd = null       // {x, y} in tileset pixels
let isDragging = false

// Eraser
let eraserActive = false
let isErasing = false
let lastErasePx = null   // {x, y} last erased pixel for line interpolation

// Undo/redo
const undoStack = []
const redoStack = []
const MAX_UNDO = 20

const statusMsg = document.getElementById('status-msg')
const statusCounts = document.getElementById('status-counts')
const assetListEl = document.getElementById('asset-list')
const previewCanvas = document.getElementById('preview-canvas')
const previewCtx = previewCanvas.getContext('2d')

// ════════════════════════════════════════════════════════════════════════
// FILE LOADING
// ════════════════════════════════════════════════════════════════════════

// New Project — start with empty data
// File dropdown menu toggle
const fileMenuBtn = document.getElementById('btn-file-menu')
const fileDropdown = document.getElementById('file-dropdown')
fileMenuBtn.onclick = (e) => {
  e.stopPropagation()
  fileDropdown.style.display = fileDropdown.style.display === 'none' ? 'block' : 'none'
}
document.addEventListener('click', () => { fileDropdown.style.display = 'none' })
fileDropdown.addEventListener('click', () => { fileDropdown.style.display = 'none' })

document.getElementById('btn-new-project').onclick = () => {
  if (data && data.assets.length > 0) {
    if (!confirm('Start a new project? Unsaved changes will be lost.')) return
  }
  jsonFileHandle = null
  loadJsonData({
    version: 1,
    timestamp: new Date().toISOString(),
    sourceFile: '',
    tileset: '',
    backgroundColor: null,
    assets: []
  })
  statusMsg.textContent = 'New project created — load a PNG and start adding assets'
}

document.getElementById('btn-load-json').onclick = async () => {
  // Try File System Access API first (Chromium) — gives us a handle for direct save-back
  if (window.showOpenFilePicker) {
    try {
      const [handle] = await window.showOpenFilePicker({
        types: [{ description: 'JSON', accept: { 'application/json': ['.json'] } }],
        multiple: false,
      })
      const file = await handle.getFile()
      const text = await file.text()
      jsonFileHandle = handle
      loadJsonData(JSON.parse(text))
      statusMsg.textContent = '\u2713 Loaded ' + data.assets.length + ' assets from ' + file.name
      return
    } catch (err) {
      if (err.name === 'AbortError') return // user cancelled
      console.warn('File System Access API failed, falling back:', err)
    }
  }
  // Fallback: classic file input
  document.getElementById('json-file').click()
}
document.getElementById('json-file').onchange = (e) => {
  const file = e.target.files[0]
  if (!file) return
  jsonFileHandle = null // no handle from classic file input
  const reader = new FileReader()
  reader.onload = (ev) => {
    try {
      loadJsonData(JSON.parse(ev.target.result))
      statusMsg.textContent = '\u2713 Loaded ' + data.assets.length + ' assets from ' + file.name
    } catch (err) {
      alert('Invalid JSON: ' + err.message)
    }
  }
  reader.readAsText(file)
  e.target.value = '' // Allow re-loading same file
}

document.getElementById('btn-load-png').onclick = () => document.getElementById('png-file').click()
document.getElementById('png-file').onchange = (e) => {
  const file = e.target.files[0]
  if (!file) return
  const reader = new FileReader()
  reader.onload = (ev) => {
    const img = new Image()
    img.onload = () => {
      tilesetImg = img
      // Auto-initialize empty project if no data loaded yet
      if (!data) {
        loadJsonData({
          version: 1,
          timestamp: new Date().toISOString(),
          sourceFile: file.name,
          tileset: file.name,
          backgroundColor: null,
          assets: []
        })
      }
      updateTilesetVisibility()
      renderTileset()
      renderList()
      renderPreview()
      statusMsg.textContent = '\u2713 Tileset loaded: ' + img.width + 'x' + img.height + 'px' + (!data || data.assets.length === 0 ? ' — click "+ Add Asset" to start defining assets' : '')
    }
    img.src = ev.target.result
  }
  reader.readAsDataURL(file)
  e.target.value = ''
}

function loadJsonData(parsed) {
  data = parsed
  migrateGroupsFromAssets()
  selectedGroupId = null
  selectedGroupUnits.clear()
  selectedIdx = data.assets.length > 0 ? 0 : -1
  selectedIndices.clear()
  if (selectedIdx >= 0) selectedIndices.add(selectedIdx)
  lastClickedIdx = selectedIdx
  savedSnapshot = JSON.parse(JSON.stringify(data))
  undoStack.length = 0
  redoStack.length = 0
  updateFilter()
  if (selectedIdx >= 0) loadForm(selectedIdx)
  updateEditorForSelection()
  renderPreview()
  renderTileset()
  updateCounts()
  scheduleSave()
  updateSaveButton()
}

function updateSaveButton() {
  const btn = document.getElementById('btn-save-file')
  if (!data) {
    btn.style.display = 'none'
  } else {
    btn.style.display = 'block'
    if (jsonFileHandle) {
      btn.textContent = 'Save'
      btn.title = 'Write directly to ' + jsonFileHandle.name
    } else {
      btn.textContent = 'Save'
      btn.title = 'Download as tileset-metadata-final.json'
    }
  }
}

// Auto-load from localStorage
window.addEventListener('load', () => {
  updateTilesetVisibility()
  try {
    const saved = localStorage.getItem('asset-manager-data')
    if (saved) {
      loadJsonData(JSON.parse(saved))
      statusMsg.textContent = 'Restored from localStorage (' + data.assets.length + ' assets)'
    } else {
      statusMsg.textContent = 'Click "New" to start a new project, or "Load JSON" to open an existing one'
    }
  } catch {}
})

// ════════════════════════════════════════════════════════════════════════
// PERSISTENCE (localStorage, debounced)
// ════════════════════════════════════════════════════════════════════════

function scheduleSave() {
  if (saveTimer) clearTimeout(saveTimer)
  saveTimer = setTimeout(() => {
    if (data) {
      try { localStorage.setItem('asset-manager-data', JSON.stringify(data)) } catch {}
    }
  }, 2000)
}

// ════════════════════════════════════════════════════════════════════════
// UNDO / REDO
// ════════════════════════════════════════════════════════════════════════

function pushUndo() {
  undoStack.push(JSON.stringify({ assets: data.assets, groups: data.groups || [] }))
  if (undoStack.length > MAX_UNDO) undoStack.shift()
  redoStack.length = 0
}

function undo() {
  if (undoStack.length === 0) return
  redoStack.push(JSON.stringify({ assets: data.assets, groups: data.groups || [] }))
  const restored = JSON.parse(undoStack.pop())
  data.assets = restored.assets
  data.groups = restored.groups
  refreshAfterUndoRedo()
}

function redo() {
  if (redoStack.length === 0) return
  undoStack.push(JSON.stringify({ assets: data.assets, groups: data.groups || [] }))
  const restored = JSON.parse(redoStack.pop())
  data.assets = restored.assets
  data.groups = restored.groups
  refreshAfterUndoRedo()
}

function refreshAfterUndoRedo() {
  // Clamp selectedIdx
  selectedGroupId = null
  selectedGroupUnits.clear()
  if (selectedIdx >= data.assets.length) selectedIdx = data.assets.length - 1
  selectedIndices.clear()
  if (selectedIdx >= 0) selectedIndices.add(selectedIdx)
  updateFilter()
  if (selectedIdx >= 0) loadForm(selectedIdx)
  updateEditorForSelection()
  renderPreview()
  renderTileset()
  updateCounts()
  scheduleSave()
  statusMsg.textContent = 'Undo/Redo applied'
}

// ════════════════════════════════════════════════════════════════════════
// FILTERING
// ════════════════════════════════════════════════════════════════════════

document.getElementById('filter-cat').onchange = () => updateFilter()
document.getElementById('search').oninput = () => updateFilter()

function updateFilter() {
  if (!data) return
  const search = document.getElementById('search').value.toLowerCase()
  const cat = document.getElementById('filter-cat').value
  filtered = []
  data.assets.forEach((asset, idx) => {
    if (cat && asset.category !== cat) return
    if (search) {
      const label = (asset.label || '').toLowerCase()
      const id = (asset.id || '').toLowerCase()
      if (!label.includes(search) && !id.includes(search)) return
    }
    filtered.push(idx)
  })

  renderList()
  updateCounts()
}

function updateCounts() {
  if (!data) { statusCounts.textContent = ''; return }
  const approved = data.assets.filter(a => !a.discard).length
  const discarded = data.assets.length - approved
  document.getElementById('counter').textContent = filtered.length + ' / ' + data.assets.length
  statusCounts.textContent = approved + ' approved, ' + discarded + ' discarded'
}

// ════════════════════════════════════════════════════════════════════════
// ASSET LIST RENDERING
// ════════════════════════════════════════════════════════════════════════

function renderAssetItem(idx) {
  const asset = data.assets[idx]
  const isSel = idx === selectedIdx
  const isMulti = selectedIndices.has(idx) && selectedIndices.size > 1
  const div = document.createElement('div')
  div.className = 'asset-item' + (isSel ? ' selected' : '') + (isMulti && !isSel ? ' multi-selected' : '') + (asset.discard ? ' discarded' : '')
  div.dataset.idx = idx
  div.onclick = (e) => { e.stopPropagation(); handleListClick(idx, e) }

  // Thumbnail
  const thumb = document.createElement('canvas')
  thumb.width = 40; thumb.height = 40
  thumb.className = 'asset-thumb'
  if (tilesetImg && asset.paddedWidth > 0 && asset.paddedHeight > 0) {
    const tctx = thumb.getContext('2d')
    tctx.imageSmoothingEnabled = false
    const srcX = Math.max(0, asset.paddedX)
    const srcY = Math.max(0, asset.paddedY)
    const offX = Math.max(0, -asset.paddedX)
    const offY = Math.max(0, -asset.paddedY)
    const srcW = asset.paddedWidth - offX
    const srcH = asset.paddedHeight - offY
    if (srcW > 0 && srcH > 0 && srcX < tilesetImg.width && srcY < tilesetImg.height) {
      const s = Math.min(40 / asset.paddedWidth, 40 / asset.paddedHeight)
      const dw = asset.paddedWidth * s
      const dh = asset.paddedHeight * s
      const dx = (40 - dw) / 2 + offX * s
      const dy = (40 - dh) / 2 + offY * s
      tctx.drawImage(tilesetImg,
        srcX, srcY, Math.min(srcW, tilesetImg.width - srcX), Math.min(srcH, tilesetImg.height - srcY),
        dx, dy, Math.min(srcW, tilesetImg.width - srcX) * s, Math.min(srcH, tilesetImg.height - srcY) * s
      )
    }
  }
  div.appendChild(thumb)

  // Info
  const meta = document.createElement('div')
  meta.className = 'asset-meta'
  const group = findGroupForAsset(asset)
  let nameHtml = '<div class="name">' + escHtml(asset.id || asset.label) + '</div>'
  nameHtml += '<div class="dims">' + asset.paddedWidth + '\u00d7' + asset.paddedHeight + 'px'
  const listFpW = Math.max(1, Math.round(asset.paddedWidth / 16))
  const listFpH = Math.max(1, Math.round(asset.paddedHeight / 16))
  nameHtml += '  \u2022  ' + listFpW + '\u00d7' + listFpH + ' tiles'
  nameHtml += '</div>'
  // Show role within group (no need for full group badge since we have the wrapper)
  if (group) {
    let role = ''
    if (group.memberRoles && group.memberRoles[asset.id]) {
      role = group.memberRoles[asset.id]
    } else if (group.type === 'rotation') {
      role = asset.orientation || '?'
    } else if (group.type === 'state') {
      role = asset.state || '?'
    } else {
      role = 'Frame ' + (group.members.indexOf(asset.id) + 1)
    }
    nameHtml += '<div class="cat">' + escHtml(role) + '</div>'
  } else {
    nameHtml += '<div class="cat">' + escHtml(asset.category || '')
    if (asset.discard) nameHtml += ' <span class="badge badge-discard">DISCARDED</span>'
    nameHtml += '</div>'
  }
  meta.innerHTML = nameHtml
  div.appendChild(meta)

  return div
}

function renderList() {
  if (!data) return
  assetListEl.innerHTML = ''

  // Build set of asset indices that belong to sub-groups (whose parent is a compound group)
  // These should be rendered inside their parent group wrapper, not standalone
  const subGroupAssetIndices = new Set()
  const topLevelGroupIds = new Set()
  if (data.groups) {
    for (const g of data.groups) {
      if (g.members.some(m => m.startsWith('@'))) {
        // This is a compound group — collect all leaf assets from sub-groups
        for (const mid of g.members) {
          if (mid.startsWith('@')) {
            const leafIds = resolveGroupAssets(mid)
            for (const lid of leafIds) {
              const idx = data.assets.findIndex(a => a.id === lid)
              if (idx >= 0) subGroupAssetIndices.add(idx)
            }
          }
        }
      }
    }
    // Identify top-level groups (not sub-groups of another)
    for (const g of data.groups) {
      if (!findParentGroup(g.id)) topLevelGroupIds.add(g.id)
    }
  }

  // Pre-collect filtered indices per top-level group
  const groupFilteredMap = {} // groupId → [filtered indices]
  const ungroupedOrdered = [] // { type: 'item', idx } | { type: 'group', groupId }
  const seenGroups = new Set()

  for (const idx of filtered) {
    const asset = data.assets[idx]
    const group = findGroupForAsset(asset)
    if (group) {
      // Find the top-level group for this asset
      let topGroup = group
      let parent = findParentGroup(topGroup.id)
      while (parent) { topGroup = parent; parent = findParentGroup(topGroup.id) }

      if (!seenGroups.has(topGroup.id)) {
        seenGroups.add(topGroup.id)
        groupFilteredMap[topGroup.id] = []
        ungroupedOrdered.push({ type: 'group', groupId: topGroup.id })
      }
      groupFilteredMap[topGroup.id].push(idx)
    } else {
      ungroupedOrdered.push({ type: 'item', idx })
    }
  }

  // Helper to render a group wrapper (possibly with nested sub-group wrappers)
  function renderGroupWrapper(groupId, filteredIndices) {
    const group = data.groups.find(g => g.id === groupId)
    if (!group) return null

    const wrapper = document.createElement('div')
    const isSelected = selectedGroupId === groupId || selectedGroupUnits.has(groupId)
    wrapper.className = 'group-wrapper' + (isSelected ? ' group-selected' : '')
    wrapper.dataset.groupId = groupId

    // Group header
    const header = document.createElement('div')
    header.className = 'group-header'
    let typeLabel = group.type === 'rotation' ? 'Rotation' : group.type === 'state' ? 'State' : 'Animation'
    if (group.type === 'rotation' && group.rotationScheme && group.rotationScheme !== '4-way') {
      typeLabel += ' (' + (group.rotationScheme === '3-way-mirror' ? '3+M' : '2') + ')'
    }
    const memberCount = filteredIndices.length
    header.innerHTML = '<span>' + escHtml(group.name || group.id) + ' <span style="color:#666; font-weight:400;">(' + memberCount + ')</span></span>' +
      '<span class="group-header-type ' + group.type + '">' + escHtml(typeLabel) + '</span>'
    header.onclick = (e) => { e.stopPropagation(); handleGroupHeaderClick(groupId, e) }
    wrapper.appendChild(header)

    // Check if this is a compound group
    const hasSubGroups = group.members.some(m => m.startsWith('@'))

    if (hasSubGroups) {
      // Render members in order, with sub-group wrappers for @refs
      for (const mid of group.members) {
        if (mid.startsWith('@')) {
          const subGroupId = mid.slice(1)
          // Collect filtered indices that belong to this sub-group
          const subLeafIds = new Set(resolveGroupAssets(mid))
          const subIndices = filteredIndices.filter(idx => subLeafIds.has(data.assets[idx].id))
          if (subIndices.length > 0) {
            const subWrapper = renderGroupWrapper(subGroupId, subIndices)
            if (subWrapper) wrapper.appendChild(subWrapper)
          }
        } else {
          // Direct asset member
          const idx = data.assets.findIndex(a => a.id === mid)
          if (idx >= 0 && filteredIndices.includes(idx)) {
            wrapper.appendChild(renderAssetItem(idx))
          }
        }
      }
    } else {
      // Simple group: render all items directly
      for (const gIdx of filteredIndices) {
        wrapper.appendChild(renderAssetItem(gIdx))
      }
    }

    return wrapper
  }

  // Render in order
  for (const entry of ungroupedOrdered) {
    if (entry.type === 'item') {
      assetListEl.appendChild(renderAssetItem(entry.idx))
    } else {
      const groupId = entry.groupId
      const groupIndices = groupFilteredMap[groupId]
      if (!groupIndices || groupIndices.length === 0) continue
      const wrapper = renderGroupWrapper(groupId, groupIndices)
      if (wrapper) assetListEl.appendChild(wrapper)
    }
  }

  // Scroll selected into view
  const sel = assetListEl.querySelector('.selected')
  if (sel) sel.scrollIntoView({ block: 'nearest' })
}

// Click on group header — select all group members (multi-select)
// With Ctrl: add group as a compound unit for compound group creation
function handleGroupHeaderClick(groupId, e) {
  if (!data || !data.groups) return
  const group = data.groups.find(g => g.id === groupId)
  if (!group) return

  // Resolve all leaf asset indices for this group (handles @sub-group refs)
  function resolveGroupIndices(g) {
    const indices = []
    for (const mid of g.members) {
      if (mid.startsWith('@')) {
        const subGroup = data.groups.find(sg => sg.id === mid.slice(1))
        if (subGroup) indices.push(...resolveGroupIndices(subGroup))
      } else {
        const idx = data.assets.findIndex(a => a.id === mid)
        if (idx >= 0) indices.push(idx)
      }
    }
    return indices
  }

  if (e && e.ctrlKey) {
    // Ctrl+click: toggle this group as a compound unit
    selectedGroupId = null
    if (selectedGroupUnits.has(groupId)) {
      // Toggle off: remove group and its member indices
      selectedGroupUnits.delete(groupId)
      const groupIndices = resolveGroupIndices(group)
      groupIndices.forEach(i => selectedIndices.delete(i))
    } else {
      // Toggle on: add group and its member indices
      selectedGroupUnits.add(groupId)
      const groupIndices = resolveGroupIndices(group)
      groupIndices.forEach(i => selectedIndices.add(i))
    }
    selectedIdx = selectedIndices.size === 1 ? [...selectedIndices][0] : -1
    lastClickedIdx = [...selectedIndices][0] || -1
  } else {
    // Normal click: select just this group
    selectedGroupId = groupId
    selectedGroupUnits = new Set([groupId])
    selectedIndices.clear()
    const groupIndices = resolveGroupIndices(group)
    groupIndices.forEach(i => selectedIndices.add(i))
    selectedIdx = -1
    lastClickedIdx = [...selectedIndices][0] || -1
  }

  deactivateEraser()
  updateEditorForSelection()
  renderList()
  renderPreview()
  renderTileset()
}

function handleListClick(idx, e) {
  const asset = data.assets[idx]
  const group = findGroupForAsset(asset)

  if (e.shiftKey && lastClickedIdx >= 0) {
    // Range select — keep existing group units, add range to selectedIndices
    selectedGroupId = null
    const posA = filtered.indexOf(lastClickedIdx)
    const posB = filtered.indexOf(idx)
    if (posA >= 0 && posB >= 0) {
      const lo = Math.min(posA, posB), hi = Math.max(posA, posB)
      if (!e.ctrlKey) {
        // Clear only non-group-unit indices, keep group unit indices
        const groupUnitIndices = new Set()
        for (const gid of selectedGroupUnits) {
          const g = data.groups.find(gr => gr.id === gid)
          if (g) {
            for (const mid of g.members) {
              for (const aid of resolveGroupAssets(mid)) {
                const ai = data.assets.findIndex(a => a.id === aid)
                if (ai >= 0) groupUnitIndices.add(ai)
              }
            }
          }
        }
        selectedIndices.clear()
        groupUnitIndices.forEach(i => selectedIndices.add(i))
      }
      for (let i = lo; i <= hi; i++) selectedIndices.add(filtered[i])
    }
  } else if (e.ctrlKey) {
    // Toggle individual asset — preserve existing group units
    selectedGroupId = null
    if (selectedIndices.has(idx)) selectedIndices.delete(idx)
    else selectedIndices.add(idx)
    lastClickedIdx = idx
  } else if (group) {
    // Grouped item: drill-down logic
    // Build the full ancestor chain for this asset's group: [directGroup, parent, grandparent, ...]
    const ancestorChain = []
    let cur = group
    while (cur) {
      ancestorChain.push(cur)
      cur = findParentGroup(cur.id)
      if (cur) cur = data.groups.find(g => g.id === cur.id)
    }
    // ancestorChain[0] = direct group, ancestorChain[last] = top-level group

    if (!selectedGroupId) {
      // No group selected yet: select the top-level group
      const topGroup = ancestorChain[ancestorChain.length - 1]
      handleGroupHeaderClick(topGroup.id)
      return
    }

    // Find where selectedGroupId sits in the chain
    const selectedLevel = ancestorChain.findIndex(g => g.id === selectedGroupId)
    if (selectedLevel < 0) {
      // selectedGroupId is not an ancestor of this asset — select its top-level group
      const topGroup = ancestorChain[ancestorChain.length - 1]
      handleGroupHeaderClick(topGroup.id)
      return
    }

    if (selectedLevel > 0) {
      // Drill down one level: select the next sub-group
      const nextGroup = ancestorChain[selectedLevel - 1]
      handleGroupHeaderClick(nextGroup.id)
      return
    }

    // selectedLevel === 0: we're at the direct group already, drill into individual asset
    selectedGroupId = null
    selectedGroupUnits.clear()
    selectedIndices.clear()
    selectedIndices.add(idx)
    lastClickedIdx = idx
  } else {
    // Normal click (ungrouped item)
    selectedGroupId = null
    selectedGroupUnits.clear()
    selectedIndices.clear()
    selectedIndices.add(idx)
    lastClickedIdx = idx
  }

  // Update selectedIdx: if exactly one selected, use it; otherwise -1
  if (selectedIndices.size === 1) {
    selectedIdx = [...selectedIndices][0]
  } else {
    selectedIdx = -1
  }

  deactivateEraser()
  if (selectedIdx >= 0) loadForm(selectedIdx)
  updateEditorForSelection()
  renderList()
  renderPreview()
  renderTileset()
}

function escHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
}

// ════════════════════════════════════════════════════════════════════════
// SELECTION & FORM
// ════════════════════════════════════════════════════════════════════════

function selectAsset(idx) {
  if (!data || idx < 0 || idx >= data.assets.length) return
  selectedGroupId = null
  selectedGroupUnits.clear()
  selectedIndices.clear()
  selectedIndices.add(idx)
  lastClickedIdx = idx
  selectedIdx = idx
  deactivateEraser()
  loadForm(idx)
  updateEditorForSelection()
  renderList()
  renderPreview()
  renderTileset()
}

function deactivateEraser() {
  eraserActive = false
  isErasing = false
  lastErasePx = null
  document.getElementById('btn-eraser').classList.remove('active')
  document.getElementById('eraser-info').classList.remove('visible')
  previewCanvas.classList.remove('eraser-active')
}

// Convert a label string to an ID: uppercase, spaces/hyphens → underscores, strip non-alphanumeric
function labelToId(label) {
  return label.trim().toUpperCase().replace(/[\s\-]+/g, '_').replace(/[^A-Z0-9_]/g, '')
}

// Deduplicate IDs: when multiple assets share the same ID, append _2, _3, etc.
// Preserves manually-set and group-assigned IDs; only deduplicates collisions.
function deduplicateIds() {
  if (!data) return
  const seen = {}  // id → count seen so far
  for (const asset of data.assets) {
    // Use the asset's current ID (which may have been manually set or group-assigned)
    const baseId = asset.id || labelToId(asset.label) || 'UNNAMED'
    if (!seen[baseId]) {
      seen[baseId] = 1
      asset.id = baseId
    } else {
      seen[baseId]++
      asset.id = baseId + '_' + seen[baseId]
    }
    asset.name = asset.id
  }
}

// Track whether user has manually edited the ID field
let idManuallyEdited = false

// Live-update ID preview as label is typed (unless user manually edited ID)
document.getElementById('f-label').oninput = () => {
  if (idManuallyEdited) return
  const label = document.getElementById('f-label').value
  document.getElementById('f-id').value = labelToId(label) || ''
}

// Mark ID as manually edited when user types in it
document.getElementById('f-id').oninput = () => {
  idManuallyEdited = true
}

// Track whether user has manually edited the group ID field
let groupIdManuallyEdited = false

// Live-update group ID from group name
document.getElementById('group-name-input').oninput = () => {
  if (groupIdManuallyEdited) return
  const name = document.getElementById('group-name-input').value
  document.getElementById('group-id-input').value = labelToId(name) || ''
}

// Mark group ID as manually edited when user types in it
document.getElementById('group-id-input').oninput = () => {
  groupIdManuallyEdited = true
}

function loadForm(idx) {
  const a = data.assets[idx]
  document.getElementById('geo-x').value = a.paddedX
  document.getElementById('geo-y').value = a.paddedY
  document.getElementById('geo-w').value = a.paddedWidth
  document.getElementById('geo-h').value = a.paddedHeight
  document.getElementById('f-label').value = a.label || ''
  document.getElementById('f-id').value = a.id || labelToId(a.label || '')
  // Reset manual edit tracking — if the current ID matches labelToId, it wasn't manually edited
  idManuallyEdited = !!(a.id && a.id !== labelToId(a.label || ''))
  document.getElementById('f-category').value = a.category || 'misc'
  updateFootprintDisplay()
  document.getElementById('f-bgtiles').value = a.backgroundTiles || 0
  document.getElementById('f-walls').checked = !!a.canPlaceOnWalls
  document.getElementById('f-ontop').checked = !!a.canPlaceOnSurfaces
  document.getElementById('f-discard').checked = !!a.discard
  updateGroupMembershipDisplay(a)
}

// Compute footprint from W/H and update the display labels
function updateFootprintDisplay() {
  const w = +document.getElementById('geo-w').value || 0
  const h = +document.getElementById('geo-h').value || 0
  const fpW = Math.max(1, Math.round(w / 16))
  const fpH = Math.max(1, Math.round(h / 16))
  document.getElementById('fp-w').textContent = fpW + ' tile' + (fpW > 1 ? 's' : '')
  document.getElementById('fp-h').textContent = fpH + ' tile' + (fpH > 1 ? 's' : '')
}

// Background tiles live preview
document.getElementById('f-bgtiles').oninput = () => {
  renderPreview()
}

// ════════════════════════════════════════════════════════════════════════
// GEOMETRY INPUTS (live preview)
// ════════════════════════════════════════════════════════════════════════

// Snap W/H to multiples of 16 on blur
;['geo-w', 'geo-h'].forEach(id => {
  document.getElementById(id).onblur = () => {
    const el = document.getElementById(id)
    const raw = +el.value
    const snapped = Math.max(16, Math.round(raw / 16) * 16)
    if (snapped !== raw) el.value = snapped
    // Push to asset
    if (selectedIdx >= 0 && data) {
      const a = data.assets[selectedIdx]
      a.paddedWidth = +document.getElementById('geo-w').value || 16
      a.paddedHeight = +document.getElementById('geo-h').value || 16
      updateFootprintDisplay()
      renderPreview()
      renderTileset()
    }
  }
})

// Number input live update
;['geo-x', 'geo-y', 'geo-w', 'geo-h'].forEach(id => {
  document.getElementById(id).oninput = () => {
    if (selectedIdx < 0 || !data) return
    const a = data.assets[selectedIdx]
    a.paddedX = +document.getElementById('geo-x').value
    a.paddedY = +document.getElementById('geo-y').value
    a.paddedWidth = +document.getElementById('geo-w').value || 16
    a.paddedHeight = +document.getElementById('geo-h').value || 16
    updateFootprintDisplay()
    renderPreview()
    renderTileset()
  }
})

// Stepper buttons
document.querySelectorAll('.step-btn').forEach(btn => {
  btn.onclick = () => {
    if (selectedIdx < 0 || !data) return
    const field = btn.dataset.field
    const delta = +btn.dataset.delta
    const a = data.assets[selectedIdx]
    pushUndo()
    a[field] = (a[field] || 0) + delta
    if (field === 'paddedWidth' && a.paddedWidth < 16) a.paddedWidth = 16
    if (field === 'paddedHeight' && a.paddedHeight < 16) a.paddedHeight = 16
    loadForm(selectedIdx)
    renderPreview()
    renderTileset()
    scheduleSave()
  }
})

// ════════════════════════════════════════════════════════════════════════
// SAVE / RESET / EXPORT
// ════════════════════════════════════════════════════════════════════════

document.getElementById('btn-save').onclick = () => {
  if (selectedIdx < 0 || !data) return
  pushUndo()

  const a = data.assets[selectedIdx]
  const oldId = a.id  // capture before rename
  // Geometry
  a.paddedX = +document.getElementById('geo-x').value
  a.paddedY = +document.getElementById('geo-y').value
  a.paddedWidth = Math.max(16, Math.round((+document.getElementById('geo-w').value || a.paddedWidth) / 16) * 16)
  a.paddedHeight = Math.max(16, Math.round((+document.getElementById('geo-h').value || a.paddedHeight) / 16) * 16)
  // Metadata — ID from field (may be manually edited or auto-generated from label)
  a.label = document.getElementById('f-label').value.trim() || a.label
  const fieldId = document.getElementById('f-id').value.trim()
  a.id = fieldId || labelToId(a.label) || a.id
  a.name = a.id

  // Sync ID change into groups
  if (oldId !== a.id && data.groups) {
    for (const g of data.groups) {
      const memberIdx = g.members.indexOf(oldId)
      if (memberIdx >= 0) {
        g.members[memberIdx] = a.id
      }
      if (g.memberRoles && g.memberRoles[oldId] !== undefined) {
        g.memberRoles[a.id] = g.memberRoles[oldId]
        delete g.memberRoles[oldId]
      }
    }
  }

  a.category = document.getElementById('f-category').value
  a.footprintW = Math.max(1, a.paddedWidth / 16)
  a.footprintH = Math.max(1, a.paddedHeight / 16)
  a.backgroundTiles = +document.getElementById('f-bgtiles').value || 0
  // Flags — isDesk derived from category
  a.isDesk = a.category === 'desks'
  a.canPlaceOnWalls = document.getElementById('f-walls').checked
  a.canPlaceOnSurfaces = document.getElementById('f-ontop').checked
  // Discard
  a.discard = document.getElementById('f-discard').checked

  // Deduplicate IDs across all assets
  deduplicateIds()

  updateFilter()
  loadForm(selectedIdx)
  renderList()
  renderPreview()
  renderTileset()
  updateCounts()
  scheduleSave()
  statusMsg.textContent = '\u2713 Saved ' + a.label
}

document.getElementById('btn-reset').onclick = () => {
  if (selectedIdx < 0 || !data) return
  loadForm(selectedIdx)
  renderPreview()
  statusMsg.textContent = 'Reset to last saved'
}

document.getElementById('btn-delete').onclick = () => {
  if (selectedIdx < 0 || !data) return
  const asset = data.assets[selectedIdx]
  if (!confirm('Delete "' + (asset.label || asset.id) + '"? This cannot be undone.')) return
  pushUndo()
  removeAssetFromGroup(asset)
  data.assets.splice(selectedIdx, 1)
  if (selectedIdx >= data.assets.length) selectedIdx = data.assets.length - 1
  selectedIndices.clear()
  if (selectedIdx >= 0) selectedIndices.add(selectedIdx)
  updateFilter()
  if (selectedIdx >= 0) loadForm(selectedIdx)
  updateEditorForSelection()
  renderPreview()
  renderTileset()
  updateCounts()
  scheduleSave()
  statusMsg.textContent = '\u2713 Deleted ' + (asset.label || asset.id)
}

document.getElementById('btn-duplicate').onclick = () => {
  if (selectedIdx < 0 || !data) return
  pushUndo()
  const clone = JSON.parse(JSON.stringify(data.assets[selectedIdx]))
  data.assets.splice(selectedIdx + 1, 0, clone)
  deduplicateIds()
  selectedIdx = selectedIdx + 1
  selectedIndices.clear()
  selectedIndices.add(selectedIdx)
  updateFilter()
  loadForm(selectedIdx)
  updateEditorForSelection()
  renderPreview()
  renderTileset()
  updateCounts()
  scheduleSave()
  statusMsg.textContent = '\u2713 Duplicated as ' + data.assets[selectedIdx].id
}

function buildOutputJson() {
  return JSON.stringify({
    version: data.version || 1,
    timestamp: new Date().toISOString(),
    sourceFile: data.sourceFile,
    tileset: data.tileset,
    backgroundColor: data.backgroundColor,
    assets: data.assets,
    groups: data.groups || []
  }, null, 2)
}

function buildSummary() {
  const approved = data.assets.filter(x => !x.discard).length
  return approved + ' approved + ' + (data.assets.length - approved) + ' discarded assets'
}

// Save — write to file handle, acquiring one on first use if needed
document.getElementById('btn-save-file').onclick = async () => {
  if (!data) return
  const json = buildOutputJson()

  // Acquire a handle if we don't have one yet
  if (!jsonFileHandle && window.showSaveFilePicker) {
    try {
      jsonFileHandle = await window.showSaveFilePicker({
        suggestedName: 'tileset-metadata-final.json',
        types: [{ description: 'JSON', accept: { 'application/json': ['.json'] } }],
      })
      updateSaveButton()
    } catch (err) {
      if (err.name === 'AbortError') return
      console.warn('showSaveFilePicker failed:', err)
    }
  }

  if (jsonFileHandle) {
    try {
      const writable = await jsonFileHandle.createWritable()
      await writable.write(json)
      await writable.close()
      statusMsg.textContent = '\u2713 Saved to ' + jsonFileHandle.name + ' \u2014 ' + buildSummary()
      return
    } catch (err) {
      console.warn('Direct save failed, falling back to download:', err)
    }
  }

  // Fallback: browser download (Firefox etc.)
  const blob = new Blob([json], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'tileset-metadata-final.json'
  a.click()
  URL.revokeObjectURL(url)
  statusMsg.textContent = '\u2713 Downloaded tileset-metadata-final.json \u2014 ' + buildSummary()
}

// Save As — open file picker (or fallback to download)
document.getElementById('btn-save-as').onclick = async () => {
  if (!data) return
  const json = buildOutputJson()

  // Try File System Access API save picker
  if (window.showSaveFilePicker) {
    try {
      const handle = await window.showSaveFilePicker({
        suggestedName: 'tileset-metadata-final.json',
        types: [{ description: 'JSON', accept: { 'application/json': ['.json'] } }],
      })
      const writable = await handle.createWritable()
      await writable.write(json)
      await writable.close()
      jsonFileHandle = handle
      updateSaveButton()
      statusMsg.textContent = '\u2713 Saved to ' + handle.name + ' \u2014 ' + buildSummary()
      return
    } catch (err) {
      if (err.name === 'AbortError') return // user cancelled
      console.warn('showSaveFilePicker failed, falling back to download:', err)
    }
  }

  // Fallback: browser download
  const blob = new Blob([json], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = 'tileset-metadata-final.json'
  a.click()
  URL.revokeObjectURL(url)
  statusMsg.textContent = '\u2713 Downloaded \u2014 ' + buildSummary()
}

// ════════════════════════════════════════════════════════════════════════
// PREVIEW RENDERING
// ════════════════════════════════════════════════════════════════════════

document.getElementById('preview-zoom').onchange = (e) => {
  previewZoom = +e.target.value
  renderPreview()
}

function renderPreview() {
  if (!data || selectedIdx < 0 || selectedIdx >= data.assets.length) {
    // Multi-select / group preview: show all selected assets side by side
    if (data && selectedIndices.size > 1 && tilesetImg) {
      renderGroupPreview()
      return
    }
    previewCanvas.width = 100; previewCanvas.height = 100
    previewCtx.fillStyle = '#111'; previewCtx.fillRect(0, 0, 100, 100)
    previewCtx.fillStyle = '#444'; previewCtx.font = '12px sans-serif'; previewCtx.textAlign = 'center'
    previewCtx.fillText('No asset selected', 50, 55)
    previewCanvas.classList.remove('invalid')
    return
  }

  const asset = data.assets[selectedIdx]
  const w = asset.paddedWidth * previewZoom
  const h = asset.paddedHeight * previewZoom

  // Validation
  const invalid = w <= 0 || h <= 0
  previewCanvas.classList.toggle('invalid', invalid)
  if (invalid) {
    previewCanvas.width = 200; previewCanvas.height = 60
    previewCtx.fillStyle = '#2a0a0a'; previewCtx.fillRect(0, 0, 200, 60)
    previewCtx.fillStyle = '#e74c3c'; previewCtx.font = '12px sans-serif'; previewCtx.textAlign = 'center'
    previewCtx.fillText('Invalid geometry', 100, 35)
    return
  }

  previewCanvas.width = w
  previewCanvas.height = h
  previewCtx.imageSmoothingEnabled = false
  previewCtx.clearRect(0, 0, w, h)

  // Draw tileset region
  if (tilesetImg) {
    const srcX = Math.max(0, asset.paddedX)
    const srcY = Math.max(0, asset.paddedY)
    const offX = Math.max(0, -asset.paddedX)
    const offY = Math.max(0, -asset.paddedY)
    const srcW = asset.paddedWidth - offX
    const srcH = asset.paddedHeight - offY
    const dstX = offX * previewZoom
    const dstY = offY * previewZoom

    if (srcW > 0 && srcH > 0 && srcX < tilesetImg.width && srcY < tilesetImg.height) {
      const clampW = Math.min(srcW, tilesetImg.width - srcX)
      const clampH = Math.min(srcH, tilesetImg.height - srcY)
      previewCtx.drawImage(tilesetImg,
        srcX, srcY, clampW, clampH,
        dstX, dstY, clampW * previewZoom, clampH * previewZoom
      )
    }
  }

  // 16px grid overlay
  previewCtx.strokeStyle = 'rgba(255,255,255,0.15)'
  previewCtx.lineWidth = 1
  for (let x = 0; x <= w; x += 16 * previewZoom) {
    previewCtx.beginPath(); previewCtx.moveTo(x + 0.5, 0); previewCtx.lineTo(x + 0.5, h); previewCtx.stroke()
  }
  for (let y = 0; y <= h; y += 16 * previewZoom) {
    previewCtx.beginPath(); previewCtx.moveTo(0, y + 0.5); previewCtx.lineTo(w, y + 0.5); previewCtx.stroke()
  }

  // Erased pixels overlay (from stage 2)
  if (asset.erasedPixels && asset.erasedPixels.length > 0) {
    previewCtx.fillStyle = 'rgba(255, 0, 0, 0.35)'
    for (const p of asset.erasedPixels) {
      previewCtx.fillRect(p.x * previewZoom, p.y * previewZoom, previewZoom, previewZoom)
    }
  }

  // Footprint overlay — shows blocked rows (orange) vs background rows (blue)
  const fpW = Math.max(1, Math.round(asset.paddedWidth / 16))
  const fpH = Math.max(1, Math.round(asset.paddedHeight / 16))
  const bgTiles = +document.getElementById('f-bgtiles').value || 0
  if (fpW > 0 && fpH > 0) {
    const tileZoom = 16 * previewZoom
    // Footprint is anchored to the bottom-left of the sprite
    const fpStartY = h - fpH * tileZoom
    for (let dr = 0; dr < fpH; dr++) {
      const isBackground = dr < bgTiles
      previewCtx.fillStyle = isBackground ? 'rgba(93, 173, 226, 0.3)' : 'rgba(230, 126, 34, 0.2)'
      previewCtx.strokeStyle = isBackground ? 'rgba(93, 173, 226, 0.8)' : 'rgba(230, 126, 34, 0.6)'
      previewCtx.lineWidth = 1
      for (let dc = 0; dc < fpW; dc++) {
        const tx = dc * tileZoom
        const ty = fpStartY + dr * tileZoom
        previewCtx.fillRect(tx, ty, tileZoom, tileZoom)
        previewCtx.strokeRect(tx + 0.5, ty + 0.5, tileZoom - 1, tileZoom - 1)
      }
    }
    // Labels
    if (bgTiles > 0) {
      previewCtx.font = `${Math.max(9, previewZoom * 3)}px sans-serif`
      previewCtx.textAlign = 'center'
      previewCtx.textBaseline = 'middle'
      for (let dr = 0; dr < fpH; dr++) {
        const isBackground = dr < bgTiles
        const ty = fpStartY + dr * tileZoom + tileZoom / 2
        const tx = fpW * tileZoom / 2
        previewCtx.fillStyle = isBackground ? 'rgba(93, 173, 226, 0.9)' : 'rgba(230, 126, 34, 0.7)'
        previewCtx.fillText(isBackground ? 'BG' : 'BLOCK', tx, ty)
      }
    }
  }

  // Border
  previewCtx.strokeStyle = '#3498db'
  previewCtx.lineWidth = 2
  previewCtx.strokeRect(0, 0, w, h)
}

function renderGroupPreview() {
  const indices = [...selectedIndices]
  const assets = indices.map(i => data.assets[i]).filter(a => a.paddedWidth > 0 && a.paddedHeight > 0)
  if (assets.length === 0) return

  previewCanvas.classList.remove('invalid')

  const gap = 4  // px gap between assets (in sprite pixels)
  const maxH = Math.max(...assets.map(a => a.paddedHeight))
  const totalW = assets.reduce((sum, a) => sum + a.paddedWidth, 0) + gap * (assets.length - 1)

  const cw = totalW * previewZoom
  const ch = maxH * previewZoom
  previewCanvas.width = cw
  previewCanvas.height = ch
  previewCtx.imageSmoothingEnabled = false
  previewCtx.clearRect(0, 0, cw, ch)

  let curX = 0
  for (const asset of assets) {
    const aw = asset.paddedWidth * previewZoom
    const ah = asset.paddedHeight * previewZoom
    // Bottom-align each asset
    const dy = ch - ah

    // Draw tileset region
    const srcX = Math.max(0, asset.paddedX)
    const srcY = Math.max(0, asset.paddedY)
    const offX = Math.max(0, -asset.paddedX)
    const offY = Math.max(0, -asset.paddedY)
    const srcW = asset.paddedWidth - offX
    const srcH = asset.paddedHeight - offY

    if (srcW > 0 && srcH > 0 && srcX < tilesetImg.width && srcY < tilesetImg.height) {
      const clampW = Math.min(srcW, tilesetImg.width - srcX)
      const clampH = Math.min(srcH, tilesetImg.height - srcY)
      previewCtx.drawImage(tilesetImg,
        srcX, srcY, clampW, clampH,
        curX + offX * previewZoom, dy + offY * previewZoom,
        clampW * previewZoom, clampH * previewZoom
      )
    }

    // Erased pixels
    if (asset.erasedPixels && asset.erasedPixels.length > 0) {
      previewCtx.fillStyle = 'rgba(255, 0, 0, 0.35)'
      for (const p of asset.erasedPixels) {
        previewCtx.fillRect(curX + p.x * previewZoom, dy + p.y * previewZoom, previewZoom, previewZoom)
      }
    }

    // Border per asset
    previewCtx.strokeStyle = 'rgba(52, 152, 219, 0.6)'
    previewCtx.lineWidth = 1
    previewCtx.strokeRect(curX + 0.5, dy + 0.5, aw - 1, ah - 1)

    // Label below top
    const label = asset.id || asset.label || ''
    if (label) {
      const fontSize = Math.max(8, previewZoom * 3)
      previewCtx.font = fontSize + 'px sans-serif'
      previewCtx.fillStyle = 'rgba(255,255,255,0.7)'
      previewCtx.textAlign = 'center'
      previewCtx.textBaseline = 'top'
      previewCtx.fillText(label, curX + aw / 2, dy + 2, aw - 4)
    }

    curX += aw + gap * previewZoom
  }
}

// ════════════════════════════════════════════════════════════════════════
// GROUPS SYSTEM
// ════════════════════════════════════════════════════════════════════════

let groupCreatorType = 'rotation'
let rotationScheme = '4-way'  // '4-way' | '3-way-mirror' | '2-way'
let editingGroupId = null  // non-null when editing an existing group

// Ensure data.groups exists
function ensureGroups() {
  if (data && !data.groups) data.groups = []
}

// Find the group that contains a given asset
function findGroupForAsset(asset) {
  if (!data || !data.groups || !asset.groupId) return null
  return data.groups.find(g => g.id === asset.groupId) || null
}

// Find the parent group that contains a sub-group reference
function findParentGroup(groupId) {
  if (!data || !data.groups) return null
  return data.groups.find(g => g.members.includes('@' + groupId)) || null
}

// Resolve all leaf asset IDs from a member reference
// If starts with '@' → find the group, recursively resolve its members
// Otherwise → return [memberId] (it's a leaf asset)
function resolveGroupAssets(memberId) {
  if (memberId.startsWith('@')) {
    const gid = memberId.slice(1)
    const group = data.groups.find(g => g.id === gid)
    if (!group) return []
    const results = []
    for (const mid of group.members) {
      results.push(...resolveGroupAssets(mid))
    }
    return results
  }
  return [memberId]
}

// Resolve full metadata for an asset by walking up the group hierarchy
function resolveAssetMetadata(assetId) {
  const meta = {}
  const asset = data.assets.find(a => a.id === assetId)
  if (!asset || !asset.groupId) return meta

  // Find direct group
  const directGroup = data.groups.find(g => g.id === asset.groupId)
  if (!directGroup) return meta

  // Get role from direct group's memberRoles
  if (directGroup.memberRoles) {
    const role = directGroup.memberRoles[assetId]
    if (directGroup.type === 'rotation') meta.orientation = role
    else if (directGroup.type === 'state') meta.state = role
    else if (directGroup.type === 'animation') meta.animationFrame = directGroup.members.indexOf(assetId)
  }

  // Walk up to parent
  const parent = findParentGroup(directGroup.id)
  if (parent && parent.memberRoles) {
    const parentRole = parent.memberRoles['@' + directGroup.id]
    if (parent.type === 'rotation') meta.orientation = parentRole
    else if (parent.type === 'state') meta.state = parentRole

    // Walk up one more level
    const grandparent = findParentGroup(parent.id)
    if (grandparent && grandparent.memberRoles) {
      const gpRole = grandparent.memberRoles['@' + parent.id]
      if (grandparent.type === 'rotation') meta.orientation = gpRole
      else if (grandparent.type === 'state') meta.state = gpRole
    }
  }

  return meta
}

// Check if a group is a sub-group of any compound group
function isSubGroup(groupId) {
  return !!findParentGroup(groupId)
}

// Get all top-level groups (groups that are not sub-groups of another group)
function getTopLevelGroups() {
  if (!data || !data.groups) return []
  return data.groups.filter(g => !findParentGroup(g.id))
}

// Migrate: rebuild data.groups from per-asset fields if groups[] is missing
function migrateGroupsFromAssets() {
  if (!data || data.groups) return
  data.groups = []
  const byGroupId = {}
  for (const asset of data.assets) {
    if (!asset.groupId) continue
    if (!byGroupId[asset.groupId]) byGroupId[asset.groupId] = []
    byGroupId[asset.groupId].push(asset)
  }
  for (const [gid, members] of Object.entries(byGroupId)) {
    const hasOrientation = members.some(a => a.orientation)
    const hasState = members.some(a => a.state)
    const type = hasState ? 'state' : hasOrientation ? 'rotation' : 'rotation'
    data.groups.push({ id: gid, type, members: members.map(a => a.id) })
  }
}

// Sync group definition -> per-asset fields
function syncGroupToAssets(group) {
  if (!data) return
  for (let i = 0; i < group.members.length; i++) {
    const asset = data.assets.find(a => a.id === group.members[i])
    if (!asset) continue
    asset.groupId = group.id
    asset.partOfGroup = true
    if (group.type === 'rotation') {
      // Try to infer orientation from suffix, or use position-based default
      const suffixes = ['front', 'right', 'back', 'left']
      const nameLower = (asset.id || '').toLowerCase()
      const matched = suffixes.find(s => nameLower.endsWith('_' + s))
      asset.orientation = matched || asset.orientation || suffixes[i % 4]
    } else if (group.type === 'state') {
      asset.state = i === 0 ? 'off' : 'on'
    } else if (group.type === 'animation') {
      asset.animationFrame = i
    }
  }
}

// Remove asset from its group
function removeAssetFromGroup(asset) {
  if (!data || !asset.groupId) return
  ensureGroups()
  const group = data.groups.find(g => g.id === asset.groupId)
  if (group) {
    group.members = group.members.filter(id => id !== asset.id)
    // Also remove from memberRoles
    if (group.memberRoles) delete group.memberRoles[asset.id]

    if (group.members.length < 2) {
      // Dissolve the group — remove per-asset fields from remaining member too
      for (const mid of group.members) {
        if (mid.startsWith('@')) continue
        const m = data.assets.find(a => a.id === mid)
        if (m) { m.groupId = undefined; m.partOfGroup = false; m.orientation = undefined; m.state = undefined; m.animationFrame = undefined }
      }
      // If this group is a sub-group of a compound group, remove the reference
      const parent = findParentGroup(group.id)
      if (parent) {
        parent.members = parent.members.filter(m => m !== '@' + group.id)
        if (parent.memberRoles) delete parent.memberRoles['@' + group.id]
        // Dissolve parent if < 2 members
        if (parent.members.length < 2) {
          for (const mid of parent.members) {
            if (mid.startsWith('@')) continue
            const m = data.assets.find(a => a.id === mid)
            if (m) { m.groupId = undefined; m.partOfGroup = false; m.orientation = undefined; m.state = undefined; m.animationFrame = undefined }
          }
          data.groups = data.groups.filter(g => g.id !== parent.id)
        }
      }
      data.groups = data.groups.filter(g => g.id !== group.id)
    }
  }
  asset.groupId = undefined
  asset.partOfGroup = false
  asset.orientation = undefined
  asset.state = undefined
  asset.animationFrame = undefined
}

// Show group membership info for a single selected asset
function updateGroupMembershipDisplay(asset) {
  const el = document.getElementById('group-membership')
  const catFlags = document.getElementById('individual-category-flags')
  const group = findGroupForAsset(asset)
  if (!group) {
    el.style.display = 'none'
    catFlags.style.display = ''
    return
  }
  el.style.display = ''
  // Restore all buttons for individual asset view
  document.getElementById('btn-edit-group').style.display = ''
  document.getElementById('btn-dissolve-group').style.display = ''
  document.getElementById('btn-remove-from-group').style.display = ''
  // Hide individual category/flags — they're managed at the group level
  catFlags.style.display = 'none'
  const typeLabel = group.type === 'rotation' ? 'Rotation' : group.type === 'state' ? 'State' : 'Animation'
  let role = ''
  if (group.memberRoles && group.memberRoles[asset.id]) {
    role = group.memberRoles[asset.id]
  } else if (group.type === 'rotation') {
    role = asset.orientation || '?'
  } else if (group.type === 'state') {
    role = asset.state || '?'
  } else {
    role = 'Frame ' + (group.members.indexOf(asset.id) + 1)
  }
  const catLabel = (asset.category || 'misc').charAt(0).toUpperCase() + (asset.category || 'misc').slice(1)
  let flagsStr = ''
  if (asset.canPlaceOnWalls) flagsStr += 'Walls '
  if (asset.canPlaceOnSurfaces) flagsStr += 'Surfaces '
  if (asset.backgroundTiles) flagsStr += 'BG:' + asset.backgroundTiles
  const schemeLabel = group.type === 'rotation' ? (group.rotationScheme === '3-way-mirror' ? '3-way + Mirror' : group.rotationScheme === '2-way' ? '2-way' : '4-way') : ''

  // Show compound group hierarchy
  let hierarchyHtml = ''
  const parent = findParentGroup(group.id)
  if (parent) {
    const parentType = parent.type === 'rotation' ? 'Rotation' : parent.type === 'state' ? 'State' : 'Animation'
    const parentRole = parent.memberRoles ? (parent.memberRoles['@' + group.id] || '?') : '?'
    hierarchyHtml = '<div style="margin-top:4px; padding:4px 6px; background:#1a1a3e; border-radius:2px; font-size:10px;">' +
      '<b>Parent:</b> ' + escHtml(parent.name || parent.id) + ' <span class="gm-type-badge ' + parent.type + '" style="display:inline-block;">' + parentType + '</span>' +
      ' (role: ' + escHtml(parentRole) + ')' +
      '</div>'

    // Check for grandparent
    const grandparent = findParentGroup(parent.id)
    if (grandparent) {
      const gpType = grandparent.type === 'rotation' ? 'Rotation' : grandparent.type === 'state' ? 'State' : 'Animation'
      const gpRole = grandparent.memberRoles ? (grandparent.memberRoles['@' + parent.id] || '?') : '?'
      hierarchyHtml += '<div style="padding:4px 6px; background:#1a1a3e; border-radius:2px; font-size:10px; margin-top:2px;">' +
        '<b>Root:</b> ' + escHtml(grandparent.name || grandparent.id) + ' <span class="gm-type-badge ' + grandparent.type + '" style="display:inline-block;">' + gpType + '</span>' +
        ' (role: ' + escHtml(gpRole) + ')' +
        '</div>'
    }
  }

  document.getElementById('group-info').innerHTML =
    '<div><b>Group:</b> ' + escHtml(group.name || group.id) + '</div>' +
    '<div><b>Group ID:</b> ' + escHtml(group.id) + '</div>' +
    '<div><b>Type:</b> ' + typeLabel + '</div>' +
    (schemeLabel ? '<div><b>Scheme:</b> ' + schemeLabel + '</div>' : '') +
    '<div><b>Role:</b> ' + role + '</div>' +
    '<div><b>Category:</b> ' + escHtml(catLabel) + '</div>' +
    (flagsStr ? '<div><b>Flags:</b> ' + escHtml(flagsStr.trim()) + '</div>' : '') +
    '<div><b>Members:</b> ' + group.members.length + '</div>' +
    hierarchyHtml
}

// Update editor panel based on selection count
function updateEditorForSelection() {
  const form = document.getElementById('editor-form')
  const creator = document.getElementById('group-creator')
  const header = document.getElementById('editor-header')

  // Detect if exactly one group is selected with no extra items
  let singleSelectedGroup = null
  if (selectedIndices.size > 1 && selectedGroupId && data.groups) {
    const group = data.groups.find(g => g.id === selectedGroupId)
    if (group) {
      // Check that selected indices exactly match this group's leaf assets
      const leafIds = new Set()
      for (const mid of group.members) {
        for (const aid of resolveGroupAssets(mid)) leafIds.add(aid)
      }
      const selectedAssetIds = new Set([...selectedIndices].map(i => data.assets[i].id))
      if (leafIds.size === selectedAssetIds.size && [...leafIds].every(id => selectedAssetIds.has(id))) {
        singleSelectedGroup = group
      }
    }
  }

  if (singleSelectedGroup) {
    // Single group selected: show group info panel (not the creator)
    for (const child of form.children) {
      if (child.id !== 'group-membership') child.style.display = 'none'
    }
    creator.style.display = 'none'
    const group = singleSelectedGroup
    const typeLabel = group.type === 'rotation' ? 'Rotation' : group.type === 'state' ? 'State' : 'Animation'
    header.textContent = escHtml(group.name || group.id)

    // Resolve first leaf asset for category/flags display
    const firstLeafId = resolveGroupAssets(group.members[0])[0]
    const firstMember = firstLeafId ? data.assets.find(a => a.id === firstLeafId) : null
    const catLabel = ((group.category || (firstMember && firstMember.category) || 'misc'))
    const catDisplay = catLabel.charAt(0).toUpperCase() + catLabel.slice(1)
    let flagsStr = ''
    const walls = group.canPlaceOnWalls != null ? group.canPlaceOnWalls : (firstMember && firstMember.canPlaceOnWalls)
    const surfaces = group.canPlaceOnSurfaces != null ? group.canPlaceOnSurfaces : (firstMember && firstMember.canPlaceOnSurfaces)
    const bgTiles = group.backgroundTiles != null ? group.backgroundTiles : (firstMember && firstMember.backgroundTiles)
    if (walls) flagsStr += 'Walls '
    if (surfaces) flagsStr += 'Surfaces '
    if (bgTiles) flagsStr += 'BG:' + bgTiles
    const schemeLabel = group.type === 'rotation' ? (group.rotationScheme === '3-way-mirror' ? '3-way + Mirror' : group.rotationScheme === '2-way' ? '2-way' : '4-way') : ''

    // List members with roles
    let membersHtml = ''
    for (const mid of group.members) {
      const role = group.memberRoles ? (group.memberRoles[mid] || '') : ''
      const roleStr = role ? ' <span style="color:#6aa;">(' + escHtml(role) + ')</span>' : ''
      if (mid.startsWith('@')) {
        const subGroup = data.groups.find(g => g.id === mid.slice(1))
        const subType = subGroup ? (subGroup.type === 'rotation' ? 'Rotation' : subGroup.type === 'state' ? 'State' : 'Animation') : '?'
        const subTypeClass = subGroup ? subGroup.type : ''
        membersHtml += '<div style="padding:2px 0;"><span class="gm-type-badge ' + subTypeClass + '" style="display:inline-block;">' + escHtml(subType) + '</span> ' + escHtml(subGroup ? (subGroup.name || subGroup.id) : mid.slice(1)) + roleStr + '</div>'
      } else {
        membersHtml += '<div style="padding:2px 0;">' + escHtml(mid) + roleStr + '</div>'
      }
    }

    const el = document.getElementById('group-membership')
    el.style.display = ''
    // Show Edit Group + Dissolve, hide Remove from Group (doesn't apply to group view)
    document.getElementById('btn-edit-group').style.display = ''
    document.getElementById('btn-dissolve-group').style.display = ''
    document.getElementById('btn-remove-from-group').style.display = 'none'
    document.getElementById('group-info').innerHTML =
      '<div><b>Group:</b> ' + escHtml(group.name || group.id) + '</div>' +
      '<div><b>Group ID:</b> ' + escHtml(group.id) + '</div>' +
      '<div><b>Type:</b> ' + typeLabel + '</div>' +
      (schemeLabel ? '<div><b>Scheme:</b> ' + schemeLabel + '</div>' : '') +
      '<div><b>Category:</b> ' + escHtml(catDisplay) + '</div>' +
      (flagsStr ? '<div><b>Flags:</b> ' + escHtml(flagsStr.trim()) + '</div>' : '') +
      '<div style="margin-top:6px;"><b>Members (' + group.members.length + '):</b></div>' +
      membersHtml
  } else if (selectedIndices.size > 1) {
    // Multi-select: hide form fields, show group creator
    for (const child of form.children) {
      if (child.id !== 'group-creator') child.style.display = 'none'
    }
    creator.style.display = ''
    if (selectedGroupUnits.size > 0) {
      const units = getSelectedMemberUnits()
      const gCount = units.filter(u => u.type === 'group').length
      const aCount = units.filter(u => u.type === 'asset').length
      const parts = []
      if (gCount > 0) parts.push(gCount + ' group' + (gCount > 1 ? 's' : ''))
      if (aCount > 0) parts.push(aCount + ' asset' + (aCount > 1 ? 's' : ''))
      header.textContent = units.length + ' items selected (' + parts.join(' + ') + ')'
      document.getElementById('group-creator-count').textContent = '(' + units.length + ' items)'
    } else {
      header.textContent = selectedIndices.size + ' assets selected'
      document.getElementById('group-creator-count').textContent = '(' + selectedIndices.size + ' assets)'
    }
    editingGroupId = null
    initGroupCreator()
  } else {
    // Single or no selection: show form fields, hide group creator
    for (const child of form.children) {
      child.style.display = ''
    }
    creator.style.display = 'none'
    header.textContent = 'Editor'
    // Check if all selected are in same group — if editing from "Edit Group" button
    if (selectedIdx >= 0) {
      updateGroupMembershipDisplay(data.assets[selectedIdx])
    } else {
      document.getElementById('group-membership').style.display = 'none'
    }
  }
}

// Detect common prefix of asset IDs
function commonPrefix(ids) {
  if (ids.length === 0) return ''
  let prefix = ids[0]
  for (let i = 1; i < ids.length; i++) {
    while (ids[i].indexOf(prefix) !== 0 && prefix.length > 0) {
      prefix = prefix.substring(0, prefix.length - 1)
    }
  }
  // Trim trailing underscore
  if (prefix.endsWith('_')) prefix = prefix.slice(0, -1)
  return prefix
}

// Auto-detect group type from name suffixes
function detectGroupType(assets) {
  const ids = assets.map(a => (a.id || '').toUpperCase())
  const orientations = ['FRONT', 'BACK', 'LEFT', 'RIGHT', 'SIDE']
  const states = ['ON', 'OFF', 'OPEN', 'CLOSED']
  if (ids.every(id => orientations.some(o => id.endsWith('_' + o)))) return 'rotation'
  if (ids.every(id => states.some(s => id.endsWith('_' + s)))) return 'state'
  return 'rotation'
}

// Auto-detect rotation scheme from assets in the group
function detectRotationScheme(assets) {
  const suffixes = new Set()
  for (const asset of assets) {
    const o = asset.orientation || inferOrientation(asset.id)
    if (o) suffixes.add(o)
  }
  if (suffixes.size <= 2 && !suffixes.has('back') && !suffixes.has('left')) return '2-way'
  if (!suffixes.has('left') && suffixes.has('right') && suffixes.has('front') && suffixes.has('back')) return '3-way-mirror'
  if (suffixes.size === 3 && suffixes.has('front') && suffixes.has('back') && (suffixes.has('right') || suffixes.has('side'))) return '3-way-mirror'
  return '4-way'
}

// Initialize the group creator panel for current multi-selection
function initGroupCreator() {
  const indices = [...selectedIndices]
  const assets = indices.map(i => data.assets[i])
  const units = getSelectedMemberUnits()
  const ids = units.map(u => u.type === 'group' ? u.groupId : u.id)

  // Reset manual edit tracking for group ID
  groupIdManuallyEdited = false

  // Check if all selected units are already members of the same parent group (compound edit)
  if (units.length >= 2 && data.groups) {
    // For compound groups: check if all units (group refs + assets) belong to the same parent
    let candidateParent = null
    for (const g of data.groups) {
      const memberSet = new Set(g.members)
      const allMatch = units.every(u => {
        const ref = u.type === 'group' ? '@' + u.groupId : u.id
        return memberSet.has(ref)
      })
      if (allMatch && g.members.length === units.length) {
        candidateParent = g
        break
      }
    }
    if (candidateParent) {
      editingGroupId = candidateParent.id
      groupCreatorType = candidateParent.type
      if (candidateParent.type === 'rotation') {
        rotationScheme = candidateParent.rotationScheme || '4-way'
        document.getElementById('rotation-scheme').value = rotationScheme
      }
      document.getElementById('group-name-input').value = candidateParent.name || ''
      document.getElementById('group-id-input').value = candidateParent.id
      groupIdManuallyEdited = !!(candidateParent.id && candidateParent.name && candidateParent.id !== labelToId(candidateParent.name))
      // Resolve first leaf asset for defaults
      const firstLeafId = resolveGroupAssets(candidateParent.members[0])[0]
      const firstMember = firstLeafId ? data.assets.find(a => a.id === firstLeafId) : null
      document.getElementById('group-category').value = candidateParent.category || (firstMember && firstMember.category) || 'misc'
      document.getElementById('group-bgtiles').value = candidateParent.backgroundTiles != null ? candidateParent.backgroundTiles : (firstMember && firstMember.backgroundTiles) || 0
      document.getElementById('group-walls').checked = candidateParent.canPlaceOnWalls != null ? candidateParent.canPlaceOnWalls : !!(firstMember && firstMember.canPlaceOnWalls)
      document.getElementById('group-ontop').checked = candidateParent.canPlaceOnSurfaces != null ? candidateParent.canPlaceOnSurfaces : !!(firstMember && firstMember.canPlaceOnSurfaces)
      document.getElementById('btn-create-group').textContent = 'Update Group'
      selectGroupTypeBtn(candidateParent.type)
      renderGroupMembers()
      return
    }
  }

  // Check if all assets are already in the same simple group (legacy / non-compound)
  const groups = assets.map(a => a.groupId).filter(Boolean)
  const uniqueGroups = [...new Set(groups)]
  if (selectedGroupUnits.size === 0 && uniqueGroups.length === 1 && data.groups) {
    const existing = data.groups.find(g => g.id === uniqueGroups[0])
    if (existing && !existing.members.some(m => m.startsWith('@'))) {
      editingGroupId = existing.id
      groupCreatorType = existing.type
      if (existing.type === 'rotation') {
        const memberAssets = existing.members.map(mid => data.assets.find(a => a.id === mid)).filter(Boolean)
        rotationScheme = existing.rotationScheme || detectRotationScheme(memberAssets)
        document.getElementById('rotation-scheme').value = rotationScheme
      }
      document.getElementById('group-name-input').value = existing.name || ''
      document.getElementById('group-id-input').value = existing.id
      groupIdManuallyEdited = !!(existing.id && existing.name && existing.id !== labelToId(existing.name))
      const firstMember = data.assets.find(a => a.id === existing.members[0])
      document.getElementById('group-category').value = existing.category || (firstMember && firstMember.category) || 'misc'
      document.getElementById('group-bgtiles').value = existing.backgroundTiles != null ? existing.backgroundTiles : (firstMember && firstMember.backgroundTiles) || 0
      document.getElementById('group-walls').checked = existing.canPlaceOnWalls != null ? existing.canPlaceOnWalls : !!(firstMember && firstMember.canPlaceOnWalls)
      document.getElementById('group-ontop').checked = existing.canPlaceOnSurfaces != null ? existing.canPlaceOnSurfaces : !!(firstMember && firstMember.canPlaceOnSurfaces)
      document.getElementById('btn-create-group').textContent = 'Update Group'
      selectGroupTypeBtn(existing.type)
      renderGroupMembers()
      return
    }
  }

  editingGroupId = null

  // Auto-detect type based on selected units
  let detected = 'rotation'
  const hasGroupUnits = units.some(u => u.type === 'group')
  if (hasGroupUnits) {
    // Suggest "next level up" type based on sub-group types
    const subTypes = units.filter(u => u.type === 'group').map(u => u.groupType)
    if (subTypes.some(t => t === 'state')) detected = 'rotation'
    else if (subTypes.some(t => t === 'animation')) detected = 'state'
    else detected = 'rotation'
  } else {
    detected = detectGroupType(assets)
  }

  groupCreatorType = detected
  if (detected === 'rotation') {
    if (!hasGroupUnits) {
      rotationScheme = detectRotationScheme(assets)
    } else {
      rotationScheme = '4-way'
    }
    document.getElementById('rotation-scheme').value = rotationScheme
  } else {
    rotationScheme = '4-way'
  }
  selectGroupTypeBtn(detected)
  document.getElementById('group-name-input').value = ''
  document.getElementById('group-id-input').value = commonPrefix(ids) || ''
  // Default category/flags from first selected asset
  const first = assets[0]
  document.getElementById('group-category').value = first.category || 'misc'
  document.getElementById('group-bgtiles').value = first.backgroundTiles || 0
  document.getElementById('group-walls').checked = !!first.canPlaceOnWalls
  document.getElementById('group-ontop').checked = !!first.canPlaceOnSurfaces
  document.getElementById('btn-create-group').textContent = 'Create Group'
  renderGroupMembers()
}

function selectGroupTypeBtn(type) {
  groupCreatorType = type
  document.querySelectorAll('.group-type-btn').forEach(btn => {
    btn.classList.toggle('selected', btn.dataset.type === type)
  })
  // Show/hide rotation scheme selector
  const schemeField = document.getElementById('rotation-scheme-field')
  schemeField.style.display = type === 'rotation' ? '' : 'none'
  updateRotationSchemeHint()
  renderGroupMembers()
}

function updateRotationSchemeHint() {
  const hint = document.getElementById('rotation-scheme-hint')
  if (rotationScheme === '3-way-mirror') {
    hint.textContent = 'Side sprite = Right. Left will be auto-mirrored at runtime.'
    hint.style.display = ''
  } else if (rotationScheme === '2-way') {
    hint.textContent = 'Side sprite = Right. No back orientation.'
    hint.style.display = ''
  } else {
    hint.textContent = ''
    hint.style.display = 'none'
  }
}

function getOrientationsForScheme(scheme) {
  if (scheme === '3-way-mirror') return ['front', 'back', 'right']
  if (scheme === '2-way') return ['front', 'right']
  return ['front', 'right', 'back', 'left']  // 4-way
}

document.querySelectorAll('.group-type-btn').forEach(btn => {
  btn.onclick = () => selectGroupTypeBtn(btn.dataset.type)
})

document.getElementById('rotation-scheme').onchange = (e) => {
  rotationScheme = e.target.value
  updateRotationSchemeHint()
  renderGroupMembers()
}

// Build member units from selection: groups (from selectedGroupUnits) + individual assets
function getSelectedMemberUnits() {
  const units = []  // { type: 'group'|'asset', id, groupId?, indices, label, groupType? }
  const coveredIndices = new Set()

  // First: group units
  for (const gid of selectedGroupUnits) {
    const group = data.groups.find(g => g.id === gid)
    if (!group) continue
    // Resolve all leaf indices for this group
    const leafAssetIds = []
    for (const mid of group.members) {
      leafAssetIds.push(...resolveGroupAssets(mid))
    }
    const indices = leafAssetIds
      .map(aid => data.assets.findIndex(a => a.id === aid))
      .filter(i => i >= 0 && selectedIndices.has(i))
    if (indices.length === 0) continue
    indices.forEach(i => coveredIndices.add(i))
    units.push({ type: 'group', id: '@' + gid, groupId: gid, indices, label: group.name || gid, groupType: group.type })
  }

  // Then: individual assets not in any selected group unit
  for (const idx of selectedIndices) {
    if (coveredIndices.has(idx)) continue
    const asset = data.assets[idx]
    units.push({ type: 'asset', id: asset.id, indices: [idx], label: asset.label || asset.id })
  }
  return units
}

function renderGroupMembers() {
  const list = document.getElementById('group-members-list')
  const units = getSelectedMemberUnits()
  const orientations = getOrientationsForScheme(rotationScheme)

  // When editing an existing compound group, restore roles from memberRoles
  let existingRoles = null
  if (editingGroupId) {
    const existing = data.groups.find(g => g.id === editingGroupId)
    if (existing && existing.memberRoles) existingRoles = existing.memberRoles
  }

  let html = ''
  units.forEach((unit, i) => {
    const isGroup = unit.type === 'group'
    html += '<div class="group-member-row' + (isGroup ? ' group-unit' : '') + '">'

    if (isGroup) {
      const typeLabel = unit.groupType === 'rotation' ? 'Rotation' : unit.groupType === 'state' ? 'State' : 'Animation'
      html += '<span class="gm-type-badge ' + unit.groupType + '">' + escHtml(typeLabel) + '</span>'
    }

    html += '<span class="gm-name">' + escHtml(unit.label) + '</span>'

    // Determine current role
    const ref = isGroup ? '@' + unit.groupId : unit.id
    let cur = existingRoles ? existingRoles[ref] : null

    if (groupCreatorType === 'rotation') {
      if (!cur) {
        if (isGroup) {
          // Try to infer from group name
          cur = inferOrientation(unit.groupId) || orientations[i % orientations.length]
        } else {
          const asset = data.assets[unit.indices[0]]
          const inferred = asset.orientation || inferOrientation(asset.id)
          cur = inferred
          if (cur === 'left' && !orientations.includes('left')) cur = 'right'
          if (cur === 'side') cur = 'right'
          cur = cur || orientations[i % orientations.length]
        }
      }
      html += '<select data-unit-idx="' + i + '" class="gm-role-select">'
      orientations.forEach(o => {
        const label = (rotationScheme !== '4-way' && o === 'right') ? 'Side' : o.charAt(0).toUpperCase() + o.slice(1)
        html += '<option value="' + o + '"' + (o === cur ? ' selected' : '') + '>' + label + '</option>'
      })
      html += '</select>'
    } else if (groupCreatorType === 'state') {
      if (!cur) {
        if (isGroup) {
          cur = inferState(unit.groupId) || (i === 0 ? 'off' : 'on')
        } else {
          const asset = data.assets[unit.indices[0]]
          cur = asset.state || inferState(asset.id) || (i === 0 ? 'off' : 'on')
        }
      }
      html += '<input type="text" data-unit-idx="' + i + '" class="gm-role-input" value="' + escHtml(cur) + '" placeholder="e.g. off, on, open, closed" style="width:90px; font-size:11px; padding:2px 6px; background:#2a2a4a; border:1px solid #555; color:#e0e0e0; border-radius:2px;" />'
    } else {
      html += '<span style="font-size:10px; color:#888; width:70px; text-align:center; flex-shrink:0;">Frame ' + (i + 1) + '</span>'
    }
    html += '</div>'
  })
  list.innerHTML = html
}

function inferOrientation(id) {
  const lower = (id || '').toLowerCase()
  for (const o of ['front', 'back', 'left', 'right', 'side']) {
    if (lower.endsWith('_' + o)) return o === 'side' ? 'right' : o
  }
  return null
}

function inferState(id) {
  const lower = (id || '').toLowerCase()
  for (const s of ['on', 'off', 'open', 'closed']) {
    if (lower.endsWith('_' + s)) return s
  }
  return null
}

// Validate and create/update group
document.getElementById('btn-create-group').onclick = () => {
  if (!data || selectedIndices.size < 2) return
  const units = getSelectedMemberUnits()
  const groupName = document.getElementById('group-name-input').value.trim()
  const groupId = document.getElementById('group-id-input').value.trim()

  if (!groupName) {
    showGroupValidation('Group Name is required')
    return
  }

  if (!groupId) {
    showGroupValidation('Group ID is required (enter a Group Name to auto-generate)')
    return
  }

  if (units.length < 2) {
    showGroupValidation('At least 2 members required')
    return
  }

  if (groupCreatorType === 'state' && units.length < 2) {
    showGroupValidation('State groups require at least 2 members')
    return
  }

  // Validate: animation groups cannot contain sub-groups
  if (groupCreatorType === 'animation' && units.some(u => u.type === 'group')) {
    showGroupValidation('Animation groups can only contain individual assets')
    return
  }

  // Validate: no circular references
  if (units.some(u => u.type === 'group' && u.groupId === groupId)) {
    showGroupValidation('A group cannot contain itself')
    return
  }

  // Validate hierarchy: state groups cannot contain rotation groups, etc.
  const groupUnits = units.filter(u => u.type === 'group')
  for (const gu of groupUnits) {
    if (groupCreatorType === 'state' && gu.groupType === 'rotation') {
      showGroupValidation('State groups cannot contain rotation groups')
      return
    }
    if (groupCreatorType === 'animation') {
      showGroupValidation('Animation groups can only contain individual assets')
      return
    }
  }

  // Check for duplicate orientations in rotation groups
  if (groupCreatorType === 'rotation') {
    const selects = document.querySelectorAll('#group-members-list .gm-role-select')
    const orientations = [...selects].map(s => s.value)
    const unique = new Set(orientations)
    if (unique.size < orientations.length) {
      showGroupValidation('Each orientation can only be assigned once')
      return
    }
    const schemeOrients = getOrientationsForScheme(rotationScheme)
    if (units.length > schemeOrients.length) {
      showGroupValidation(rotationScheme + ' scheme only supports ' + schemeOrients.length + ' members (got ' + units.length + ')')
      return
    }
  }

  // Check for duplicate or empty states in state groups
  if (groupCreatorType === 'state') {
    const stateInputs = document.querySelectorAll('#group-members-list .gm-role-input')
    const stateValues = [...stateInputs].map(s => s.value.trim().toLowerCase())
    if (stateValues.some(s => !s)) {
      showGroupValidation('Each state must have a non-empty value')
      return
    }
    const unique = new Set(stateValues)
    if (unique.size < stateValues.length) {
      showGroupValidation('Each state value must be unique')
      return
    }
  }

  pushUndo()
  ensureGroups()

  const isEditing = !!editingGroupId

  // Remove old group if editing
  if (editingGroupId) {
    const oldGroup = data.groups.find(g => g.id === editingGroupId)
    if (oldGroup) {
      // Clear old simple asset members that are no longer in the group
      for (const mid of oldGroup.members) {
        if (mid.startsWith('@')) continue  // sub-group refs don't need per-asset cleanup
        const m = data.assets.find(a => a.id === mid)
        const stillIncluded = units.some(u => u.type === 'asset' && u.indices.some(idx => data.assets[idx] === m))
        if (m && !stillIncluded) {
          m.groupId = undefined; m.partOfGroup = false; m.orientation = undefined; m.state = undefined; m.animationFrame = undefined
        }
      }
      data.groups = data.groups.filter(g => g.id !== editingGroupId)
    }
  }

  // Read group-level category/flags
  const groupCategory = document.getElementById('group-category').value
  const groupBgTiles = +document.getElementById('group-bgtiles').value || 0
  const groupWalls = document.getElementById('group-walls').checked
  const groupOnTop = document.getElementById('group-ontop').checked

  // Collect roles from dropdowns or text inputs
  const selects = document.querySelectorAll('#group-members-list .gm-role-select')
  const stateInputs = document.querySelectorAll('#group-members-list .gm-role-input')

  // Build member refs and memberRoles
  const memberRefs = []
  const memberRoles = {}
  const hasCompoundMembers = units.some(u => u.type === 'group')

  units.forEach((unit, i) => {
    let role
    if (groupCreatorType === 'state') {
      role = stateInputs[i] ? stateInputs[i].value.trim() || (i === 0 ? 'off' : 'on') : (i === 0 ? 'off' : 'on')
    } else {
      role = selects[i] ? selects[i].value : (groupCreatorType === 'animation' ? String(i) : undefined)
    }
    const ref = unit.type === 'group' ? '@' + unit.groupId : null  // asset refs will be updated after rename

    if (unit.type === 'group') {
      memberRefs.push(ref)
      if (role) memberRoles[ref] = role

      // Rename leaf assets within the sub-group based on compound hierarchy
      const subGroup = data.groups.find(g => g.id === unit.groupId)
      if (subGroup) {
        // Build the role suffix for this sub-group in the parent
        const roleSuffix = role ? role.toUpperCase() : ''
        const sideLabel = (rotationScheme !== '4-way' && role === 'right') ? 'SIDE' : roleSuffix

        // Walk sub-group members and rename
        renameSubGroupAssets(subGroup, groupId, groupCreatorType === 'rotation' ? sideLabel : roleSuffix, groupCreatorType, groupName, groupCategory, groupBgTiles, groupWalls, groupOnTop)
      }
    } else {
      // Individual asset member
      const asset = data.assets[unit.indices[0]]

      // Remove from any existing group first
      if (asset.groupId && asset.groupId !== groupId) removeAssetFromGroup(asset)

      asset.groupId = groupId
      asset.partOfGroup = true
      asset.label = groupName
      asset.category = groupCategory
      asset.isDesk = groupCategory === 'desks'
      asset.backgroundTiles = groupBgTiles
      asset.canPlaceOnWalls = groupWalls
      asset.canPlaceOnSurfaces = groupOnTop

      if (groupCreatorType === 'rotation') {
        const orientation = role || 'front'
        asset.orientation = orientation
        asset.state = undefined
        asset.animationFrame = undefined
        const suffix = (rotationScheme !== '4-way' && orientation === 'right') ? 'SIDE' : orientation.toUpperCase()
        asset.id = groupId + '_' + suffix
        asset.name = asset.id
      } else if (groupCreatorType === 'state') {
        const state = role || (i === 0 ? 'off' : 'on')
        asset.state = state
        asset.orientation = undefined
        asset.animationFrame = undefined
        asset.id = groupId + '_' + state.toUpperCase()
        asset.name = asset.id
      } else {
        asset.animationFrame = i
        asset.orientation = undefined
        asset.state = undefined
        asset.id = groupId + '_' + (i + 1)
        asset.name = asset.id
      }

      // For non-compound groups, use asset id directly
      const assetRef = asset.id
      memberRefs.push(assetRef)
      if (role) memberRoles[assetRef] = role
    }
  })

  // Create group entry
  const newGroup = {
    id: groupId, name: groupName, type: groupCreatorType, members: memberRefs,
    ...(hasCompoundMembers ? { memberRoles } : {}),
    category: groupCategory, backgroundTiles: groupBgTiles,
    canPlaceOnWalls: groupWalls, canPlaceOnSurfaces: groupOnTop,
    ...(groupCreatorType === 'rotation' && rotationScheme !== '4-way' ? { rotationScheme } : {})
  }
  data.groups.push(newGroup)

  // Select first member asset
  const firstIdx = units[0].indices[0]
  selectAsset(firstIdx)
  updateFilter()
  renderList()
  renderTileset()
  scheduleSave()
  statusMsg.textContent = '\u2713 ' + (isEditing ? 'Updated' : 'Created') + ' ' + groupCreatorType + ' group: ' + groupName + ' (' + groupId + ')'
  editingGroupId = null
}

// Rename assets within a sub-group based on their position in a compound hierarchy
function renameSubGroupAssets(subGroup, parentId, parentRoleSuffix, parentType, groupName, groupCategory, groupBgTiles, groupWalls, groupOnTop) {
  for (let i = 0; i < subGroup.members.length; i++) {
    const mid = subGroup.members[i]
    if (mid.startsWith('@')) {
      // Nested sub-group: recurse
      const nestedGroup = data.groups.find(g => g.id === mid.slice(1))
      if (nestedGroup) {
        // Build suffix for this level
        let subRole = ''
        if (subGroup.memberRoles && subGroup.memberRoles[mid]) {
          subRole = subGroup.memberRoles[mid].toUpperCase()
        }
        const combinedSuffix = parentRoleSuffix ? parentRoleSuffix + '_' + subRole : subRole
        renameSubGroupAssets(nestedGroup, parentId, combinedSuffix, parentType, groupName, groupCategory, groupBgTiles, groupWalls, groupOnTop)
      }
    } else {
      const asset = data.assets.find(a => a.id === mid)
      if (!asset) continue

      // Apply group-level properties
      asset.label = groupName
      asset.category = groupCategory
      asset.isDesk = groupCategory === 'desks'
      asset.backgroundTiles = groupBgTiles
      asset.canPlaceOnWalls = groupWalls
      asset.canPlaceOnSurfaces = groupOnTop

      // Build the full ID based on hierarchy
      let suffix = parentRoleSuffix

      // Add sub-group role (state or animation frame)
      if (subGroup.type === 'state') {
        const role = (subGroup.memberRoles && subGroup.memberRoles[mid]) || asset.state || (i === 0 ? 'off' : 'on')
        suffix = suffix ? suffix + '_' + role.toUpperCase() : role.toUpperCase()
      } else if (subGroup.type === 'animation') {
        suffix = suffix ? suffix + '_' + (i + 1) : String(i + 1)
      } else if (subGroup.type === 'rotation') {
        const role = (subGroup.memberRoles && subGroup.memberRoles[mid]) || asset.orientation || 'front'
        suffix = suffix ? suffix + '_' + role.toUpperCase() : role.toUpperCase()
      }

      const newId = parentId + (suffix ? '_' + suffix : '')
      // Update the sub-group's member list to reflect the new ID
      subGroup.members[i] = newId
      // Update memberRoles keys if needed
      if (subGroup.memberRoles && subGroup.memberRoles[mid] && mid !== newId) {
        subGroup.memberRoles[newId] = subGroup.memberRoles[mid]
        delete subGroup.memberRoles[mid]
      }
      asset.id = newId
      asset.name = newId
    }
  }
}

document.getElementById('btn-cancel-group').onclick = () => {
  if (selectedIndices.size > 0) {
    selectAsset([...selectedIndices][0])
  }
}

function showGroupValidation(msg) {
  const el = document.getElementById('group-validation')
  el.textContent = msg
  el.style.display = ''
  setTimeout(() => { el.style.display = 'none' }, 3000)
}

// Edit Group button — select all members of the group
// For compound groups, selects the parent group with sub-group units
document.getElementById('btn-edit-group').onclick = () => {
  if (!data) return

  // Find the group to edit: either from selectedGroupId (group view) or from selected asset
  let group = null
  if (selectedGroupId && data.groups) {
    group = data.groups.find(g => g.id === selectedGroupId)
  }
  if (!group && selectedIdx >= 0) {
    const asset = data.assets[selectedIdx]
    group = findGroupForAsset(asset)
  }
  if (!group) return

  // Set up selection to match this group's members for the group creator
  selectedGroupId = null
  selectedGroupUnits = new Set()
  selectedIndices.clear()

  for (const mid of group.members) {
    if (mid.startsWith('@')) {
      const subGroupId = mid.slice(1)
      selectedGroupUnits.add(subGroupId)
      const leafIds = resolveGroupAssets(mid)
      for (const lid of leafIds) {
        const idx = data.assets.findIndex(a => a.id === lid)
        if (idx >= 0) selectedIndices.add(idx)
      }
    } else {
      const idx = data.assets.findIndex(a => a.id === mid)
      if (idx >= 0) selectedIndices.add(idx)
    }
  }

  selectedIdx = -1
  lastClickedIdx = [...selectedIndices][0]
  editingGroupId = group.id
  updateEditorForSelection()
  renderList()
}

// Dissolve Group button — removes the group, leaving assets ungrouped
document.getElementById('btn-dissolve-group').onclick = () => {
  if (!data || !data.groups) return

  // Find the group: from group view or from selected asset
  let group = null
  if (selectedGroupId) {
    group = data.groups.find(g => g.id === selectedGroupId)
  }
  if (!group && selectedIdx >= 0) {
    group = findGroupForAsset(data.assets[selectedIdx])
  }
  if (!group) return

  if (!confirm('Dissolve group "' + (group.name || group.id) + '"? Assets will be ungrouped.')) return

  pushUndo()

  // Clear per-asset fields for all leaf assets
  for (const mid of group.members) {
    if (mid.startsWith('@')) {
      // Sub-group: leave the sub-group intact, just detach from parent
      // (the sub-group becomes a standalone group)
    } else {
      const asset = data.assets.find(a => a.id === mid)
      if (asset) {
        asset.groupId = undefined
        asset.partOfGroup = false
        asset.orientation = undefined
        asset.state = undefined
        asset.animationFrame = undefined
      }
    }
  }

  // Remove sub-group references from parent if this group is a sub-group
  const parent = findParentGroup(group.id)
  if (parent) {
    parent.members = parent.members.filter(m => m !== '@' + group.id)
    if (parent.memberRoles) delete parent.memberRoles['@' + group.id]
    if (parent.members.length < 2) {
      // Dissolve parent too
      for (const mid of parent.members) {
        if (mid.startsWith('@')) continue
        const m = data.assets.find(a => a.id === mid)
        if (m) { m.groupId = undefined; m.partOfGroup = false; m.orientation = undefined; m.state = undefined; m.animationFrame = undefined }
      }
      data.groups = data.groups.filter(g => g.id !== parent.id)
    }
  }

  // Remove the group itself
  data.groups = data.groups.filter(g => g.id !== group.id)

  // Reset selection
  selectedGroupId = null
  selectedGroupUnits.clear()
  if (selectedIdx < 0 && selectedIndices.size > 0) {
    selectedIdx = [...selectedIndices][0]
    selectedIndices.clear()
    selectedIndices.add(selectedIdx)
  }

  if (selectedIdx >= 0) loadForm(selectedIdx)
  updateEditorForSelection()
  updateFilter()
  renderList()
  renderTileset()
  scheduleSave()
  statusMsg.textContent = '\u2713 Dissolved group: ' + (group.name || group.id)
}

// Remove from Group button
document.getElementById('btn-remove-from-group').onclick = () => {
  if (selectedIdx < 0 || !data) return
  pushUndo()
  removeAssetFromGroup(data.assets[selectedIdx])
  loadForm(selectedIdx)
  updateEditorForSelection()
  renderList()
  renderTileset()
  scheduleSave()
  statusMsg.textContent = '\u2713 Removed from group'
}

// ════════════════════════════════════════════════════════════════════════
// PIXEL ERASER
// ════════════════════════════════════════════════════════════════════════

document.getElementById('btn-eraser').onclick = () => {
  eraserActive = !eraserActive
  document.getElementById('btn-eraser').classList.toggle('active', eraserActive)
  document.getElementById('eraser-info').classList.toggle('visible', eraserActive)
  previewCanvas.classList.toggle('eraser-active', eraserActive)
}

document.getElementById('btn-clear-erased').onclick = () => {
  if (selectedIdx < 0 || !data) return
  const asset = data.assets[selectedIdx]
  if (!asset.erasedPixels || asset.erasedPixels.length === 0) return
  pushUndo()
  asset.erasedPixels = []
  renderPreview()
  scheduleSave()
  statusMsg.textContent = 'Cleared erased pixels for ' + asset.label
}

// Bresenham line: all integer pixels between two points
function bresenham(x0, y0, x1, y1) {
  const pts = []
  const dx = Math.abs(x1 - x0), dy = Math.abs(y1 - y0)
  const sx = x0 < x1 ? 1 : -1, sy = y0 < y1 ? 1 : -1
  let err = dx - dy
  let x = x0, y = y0
  while (true) {
    pts.push({ x, y })
    if (x === x1 && y === y1) break
    const e2 = 2 * err
    if (e2 > -dy) { err -= dy; x += sx }
    if (e2 < dx) { err += dx; y += sy }
  }
  return pts
}

function previewPixelAt(e) {
  const rect = previewCanvas.getBoundingClientRect()
  return {
    x: Math.floor((e.clientX - rect.left) / previewZoom),
    y: Math.floor((e.clientY - rect.top) / previewZoom)
  }
}

function erasePixels(pts) {
  if (selectedIdx < 0 || !data) return
  const asset = data.assets[selectedIdx]
  if (!asset.erasedPixels) asset.erasedPixels = []
  const existing = new Set(asset.erasedPixels.map(p => p.x + ',' + p.y))
  for (const p of pts) {
    if (p.x < 0 || p.y < 0 || p.x >= asset.paddedWidth || p.y >= asset.paddedHeight) continue
    const key = p.x + ',' + p.y
    if (!existing.has(key)) {
      asset.erasedPixels.push({ x: p.x, y: p.y })
      existing.add(key)
    }
  }
}

previewCanvas.onmousedown = (e) => {
  if (!eraserActive || selectedIdx < 0 || !data) return
  e.preventDefault()
  pushUndo()
  isErasing = true
  const p = previewPixelAt(e)
  lastErasePx = p
  erasePixels([p])
  renderPreview()
}

previewCanvas.onmousemove = (e) => {
  if (!isErasing) return
  const p = previewPixelAt(e)
  // Interpolate from last point for smooth strokes
  const pts = lastErasePx ? bresenham(lastErasePx.x, lastErasePx.y, p.x, p.y) : [p]
  lastErasePx = p
  erasePixels(pts)
  renderPreview()
}

previewCanvas.onmouseup = () => {
  if (isErasing) {
    isErasing = false
    lastErasePx = null
    scheduleSave()
  }
}

previewCanvas.onmouseleave = () => {
  if (isErasing) {
    isErasing = false
    lastErasePx = null
    scheduleSave()
  }
}

// ════════════════════════════════════════════════════════════════════════
// TILESET PANE (always visible)
// ════════════════════════════════════════════════════════════════════════

const tilesetCanvas = document.getElementById('tileset-canvas')
const tilesetCtx = tilesetCanvas.getContext('2d')
const tilesetWrap = document.getElementById('tileset-wrap')
const selectRect = document.getElementById('select-rect')
const tilesetEmpty = document.getElementById('tileset-empty')
const addModeBar = document.getElementById('add-mode-bar')

function updateTilesetVisibility() {
  const hasTileset = !!tilesetImg
  tilesetWrap.style.display = hasTileset ? '' : 'none'
  tilesetEmpty.style.display = hasTileset ? 'none' : ''
}

document.getElementById('btn-add-asset').onclick = () => {
  if (!tilesetImg) { alert('Load a tileset PNG first'); return }
  // Auto-initialize empty project if needed
  if (!data) {
    loadJsonData({
      version: 1,
      timestamp: new Date().toISOString(),
      sourceFile: '',
      tileset: '',
      backgroundColor: null,
      assets: []
    })
  }
  redrawMode = false
  toggleAddMode(!addMode)
}

document.getElementById('btn-cancel-add').onclick = () => toggleAddMode(false)

document.getElementById('btn-redraw').onclick = () => {
  if (!tilesetImg) { alert('Load a tileset PNG first'); return }
  if (!data || selectedIdx < 0) { alert('Select an asset first'); return }
  redrawMode = true
  toggleAddMode(true)
}

document.getElementById('tileset-zoom').onchange = (e) => {
  tilesetZoom = +e.target.value
  renderTileset()
}

function toggleAddMode(on) {
  addMode = on
  dragStart = null
  dragEnd = null
  isDragging = false
  selectRect.style.display = 'none'
  if (on) deactivateEraser()
  if (!on) redrawMode = false

  document.getElementById('btn-add-asset').classList.toggle('active', on && !redrawMode)
  tilesetWrap.style.cursor = on ? 'crosshair' : 'default'

  // Show/hide the add mode instruction bar
  addModeBar.style.display = on ? '' : 'none'
  document.getElementById('add-mode-label').textContent = on && redrawMode
    ? 'Drag to redefine the asset region' : 'Drag to select a region on the tileset'

  renderTileset()
}

function renderTileset() {
  if (!tilesetImg) return
  tilesetCanvas.width = tilesetImg.width * tilesetZoom
  tilesetCanvas.height = tilesetImg.height * tilesetZoom
  tilesetCtx.imageSmoothingEnabled = false
  tilesetCtx.drawImage(tilesetImg, 0, 0, tilesetCanvas.width, tilesetCanvas.height)

  // Draw existing asset bounding boxes
  if (data) {
    data.assets.forEach((asset, i) => {
      if (asset.discard) return
      const x = asset.paddedX * tilesetZoom
      const y = asset.paddedY * tilesetZoom
      const w = asset.paddedWidth * tilesetZoom
      const h = asset.paddedHeight * tilesetZoom

      if (redrawMode && i === selectedIdx) {
        // Redraw target: dashed red
        tilesetCtx.strokeStyle = 'rgba(231, 76, 60, 0.8)'
        tilesetCtx.lineWidth = 2
        tilesetCtx.setLineDash([4, 4])
        tilesetCtx.strokeRect(x + 0.5, y + 0.5, w, h)
        tilesetCtx.setLineDash([])
      } else if (i === selectedIdx) {
        // Selected asset: bright green highlight
        tilesetCtx.fillStyle = 'rgba(46, 204, 113, 0.12)'
        tilesetCtx.fillRect(x, y, w, h)
        tilesetCtx.strokeStyle = 'rgba(46, 204, 113, 0.9)'
        tilesetCtx.lineWidth = 2
        tilesetCtx.strokeRect(x + 0.5, y + 0.5, w, h)
        // Label
        tilesetCtx.font = `${Math.max(9, tilesetZoom * 4)}px sans-serif`
        tilesetCtx.fillStyle = 'rgba(46, 204, 113, 0.95)'
        tilesetCtx.textAlign = 'left'
        tilesetCtx.textBaseline = 'bottom'
        tilesetCtx.fillText(asset.id, x + 2, y - 2)
      } else if (i === tilesetHoverIdx) {
        // Hovered asset: yellow highlight
        tilesetCtx.fillStyle = 'rgba(241, 196, 15, 0.1)'
        tilesetCtx.fillRect(x, y, w, h)
        tilesetCtx.strokeStyle = 'rgba(241, 196, 15, 0.8)'
        tilesetCtx.lineWidth = 2
        tilesetCtx.strokeRect(x + 0.5, y + 0.5, w, h)
        // Label
        tilesetCtx.font = `${Math.max(9, tilesetZoom * 4)}px sans-serif`
        tilesetCtx.fillStyle = 'rgba(241, 196, 15, 0.9)'
        tilesetCtx.textAlign = 'left'
        tilesetCtx.textBaseline = 'bottom'
        tilesetCtx.fillText(asset.id, x + 2, y - 2)
      } else {
        // Other assets: subtle blue
        tilesetCtx.strokeStyle = 'rgba(52, 152, 219, 0.5)'
        tilesetCtx.lineWidth = 1
        tilesetCtx.strokeRect(x + 0.5, y + 0.5, w, h)
      }
    })
  }
}

// Tileset mouse handlers — click to select existing asset OR drag to create/redraw
let clickStartPos = null  // track initial mousedown position for click vs drag detection
let tilesetHoverIdx = -1  // index of asset hovered on tileset

// Find the asset at a given tileset pixel coordinate (smallest bbox wins)
function assetAtTilesetPos(px, py) {
  if (!data) return -1
  let bestIdx = -1
  let bestArea = Infinity
  data.assets.forEach((asset, i) => {
    if (asset.discard) return
    if (px >= asset.paddedX && px < asset.paddedX + asset.paddedWidth &&
        py >= asset.paddedY && py < asset.paddedY + asset.paddedHeight) {
      const area = asset.paddedWidth * asset.paddedHeight
      if (area < bestArea) {
        bestArea = area
        bestIdx = i
      }
    }
  })
  return bestIdx
}

tilesetCanvas.onmousemove = (e) => {
  if (addMode && isDragging) return  // handled by tilesetWrap.onmousemove
  if (addMode) return
  const rect = tilesetCanvas.getBoundingClientRect()
  const px = (e.clientX - rect.left) / tilesetZoom
  const py = (e.clientY - rect.top) / tilesetZoom
  const idx = assetAtTilesetPos(px, py)
  if (idx !== tilesetHoverIdx) {
    tilesetHoverIdx = idx
    tilesetCanvas.style.cursor = idx >= 0 ? 'pointer' : 'default'
    tilesetCanvas.title = idx >= 0 ? data.assets[idx].label + ' (' + data.assets[idx].id + ')' : ''
    renderTileset()
  }
}

tilesetCanvas.onmouseleave = () => {
  if (tilesetHoverIdx >= 0) {
    tilesetHoverIdx = -1
    tilesetCanvas.title = ''
    renderTileset()
  }
}

tilesetWrap.onmousedown = (e) => {
  if (e.target !== tilesetCanvas) return
  const rect = tilesetCanvas.getBoundingClientRect()
  const px = (e.clientX - rect.left) / tilesetZoom
  const py = (e.clientY - rect.top) / tilesetZoom

  clickStartPos = { x: e.clientX, y: e.clientY }

  if (addMode) {
    dragStart = snapCoord(px, py)
    dragEnd = { ...dragStart }
    isDragging = true
    updateSelectRect()
    selectRect.style.display = 'block'
  }
  e.preventDefault()
}

tilesetWrap.onmousemove = (e) => {
  if (!isDragging) return
  const rect = tilesetCanvas.getBoundingClientRect()
  const px = (e.clientX - rect.left) / tilesetZoom
  const py = (e.clientY - rect.top) / tilesetZoom
  dragEnd = snapCoord(px, py)
  updateSelectRect()
}

tilesetWrap.onmouseup = (e) => {
  const startPos = clickStartPos
  clickStartPos = null

  if (isDragging) {
    isDragging = false

    const rect = tilesetCanvas.getBoundingClientRect()
    const px = (e.clientX - rect.left) / tilesetZoom
    const py = (e.clientY - rect.top) / tilesetZoom
    dragEnd = snapCoord(px, py)

    // Compute selected region
    const x1 = Math.min(dragStart.x, dragEnd.x)
    const y1 = Math.min(dragStart.y, dragEnd.y)
    const x2 = Math.max(dragStart.x, dragEnd.x)
    const y2 = Math.max(dragStart.y, dragEnd.y)
    const w = x2 - x1
    const h = y2 - y1

    if (w < 1 || h < 1) {
      selectRect.style.display = 'none'
      // Tiny drag in add mode = treat as click-to-select
      if (addMode) return
    } else {
      if (redrawMode) {
        redrawAsset(x1, y1, w, h)
      } else {
        createNewAsset(x1, y1, w, h)
      }
      return
    }
  }

  // Click-to-select: find the asset whose bounding box contains the click point
  if (!addMode && startPos && data && e.target === tilesetCanvas) {
    const dx = Math.abs(e.clientX - startPos.x)
    const dy = Math.abs(e.clientY - startPos.y)
    if (dx < 5 && dy < 5) {
      const rect = tilesetCanvas.getBoundingClientRect()
      const px = (e.clientX - rect.left) / tilesetZoom
      const py = (e.clientY - rect.top) / tilesetZoom
      const bestIdx = assetAtTilesetPos(px, py)
      if (bestIdx >= 0) {
        selectAsset(bestIdx)
      }
    }
  }
}

function snapCoord(px, py) {
  const snap = document.getElementById('snap-grid').checked
  if (snap) {
    return { x: Math.round(px / 16) * 16, y: Math.round(py / 16) * 16 }
  }
  return { x: Math.round(px), y: Math.round(py) }
}

function updateSelectRect() {
  if (!dragStart || !dragEnd) return
  const x1 = Math.min(dragStart.x, dragEnd.x) * tilesetZoom
  const y1 = Math.min(dragStart.y, dragEnd.y) * tilesetZoom
  const x2 = Math.max(dragStart.x, dragEnd.x) * tilesetZoom
  const y2 = Math.max(dragStart.y, dragEnd.y) * tilesetZoom
  selectRect.style.left = x1 + 'px'
  selectRect.style.top = y1 + 'px'
  selectRect.style.width = (x2 - x1) + 'px'
  selectRect.style.height = (y2 - y1) + 'px'
}

function createNewAsset(x, y, w, h) {
  // Snap W/H to multiples of 16
  w = Math.max(16, Math.round(w / 16) * 16)
  h = Math.max(16, Math.round(h / 16) * 16)

  const label = 'New Asset'
  const baseId = labelToId(label)

  const newAsset = {
    id: baseId,
    paddedX: x,
    paddedY: y,
    paddedWidth: w,
    paddedHeight: h,
    name: baseId,
    label: label,
    category: 'misc',
    footprintW: w / 16,
    footprintH: h / 16,
    backgroundTiles: 0,
    isDesk: false,
    canPlaceOnWalls: false,
    canPlaceOnSurfaces: false,
    discard: false
  }

  pushUndo()
  data.assets.push(newAsset)
  deduplicateIds()
  const newIdx = data.assets.length - 1

  // Stay in add mode — just reset drag state so user can draw another
  dragStart = null
  dragEnd = null
  selectRect.style.display = 'none'

  selectedIdx = newIdx
  selectedIndices.clear()
  selectedIndices.add(newIdx)
  lastClickedIdx = newIdx
  updateFilter()
  loadForm(newIdx)
  updateEditorForSelection()
  renderPreview()
  renderTileset()
  updateCounts()
  scheduleSave()
  statusMsg.textContent = '\u2713 Created ' + data.assets[newIdx].id + ' (' + w + '\u00d7' + h + 'px)'
}

function redrawAsset(x, y, w, h) {
  if (selectedIdx < 0 || !data) return
  // Snap W/H to multiples of 16
  w = Math.max(16, Math.round(w / 16) * 16)
  h = Math.max(16, Math.round(h / 16) * 16)
  pushUndo()
  const a = data.assets[selectedIdx]
  a.paddedX = x
  a.paddedY = y
  a.paddedWidth = w
  a.paddedHeight = h
  a.footprintW = w / 16
  a.footprintH = h / 16

  toggleAddMode(false)
  loadForm(selectedIdx)
  renderList()
  renderPreview()
  renderTileset()
  scheduleSave()
  statusMsg.textContent = '\u2713 Redrawn ' + a.label + ' (' + w + '\u00d7' + h + 'px)'
}

// ════════════════════════════════════════════════════════════════════════
// RESIZE HANDLES
// ════════════════════════════════════════════════════════════════════════

let resizing = null

document.getElementById('handle-left').onmousedown = (e) => { resizing = 'left'; e.preventDefault() }
document.getElementById('handle-right').onmousedown = (e) => { resizing = 'right'; e.preventDefault() }
document.getElementById('handle-center').onmousedown = (e) => { resizing = 'center'; e.preventDefault() }

document.onmousemove = (e) => {
  if (resizing) {
    const mainRect = document.getElementById('main').getBoundingClientRect()
    const x = e.clientX - mainRect.left

    if (resizing === 'left') {
      const w = Math.max(150, Math.min(x, mainRect.width - 500))
      document.getElementById('list-panel').style.width = w + 'px'
    } else if (resizing === 'right') {
      const editorW = mainRect.width - x
      const w = Math.max(250, Math.min(editorW, mainRect.width - 400))
      document.getElementById('editor-panel').style.width = w + 'px'
    } else if (resizing === 'center') {
      // Resize tileset vs preview pane within center-panel
      const centerPanel = document.getElementById('center-panel')
      const centerRect = centerPanel.getBoundingClientRect()
      const relX = e.clientX - centerRect.left
      const tilesetW = Math.max(100, Math.min(relX, centerRect.width - 100))
      document.getElementById('tileset-pane').style.flex = 'none'
      document.getElementById('tileset-pane').style.width = tilesetW + 'px'
      document.getElementById('preview-pane').style.flex = '1'
    }
  }
}

document.onmouseup = () => {
  resizing = null
  // Cancel tileset drag if mouse released outside
  if (isDragging) {
    isDragging = false
    selectRect.style.display = 'none'
  }
}

// ════════════════════════════════════════════════════════════════════════
// KEYBOARD SHORTCUTS
// ════════════════════════════════════════════════════════════════════════

document.onkeydown = (e) => {
  const tag = e.target.tagName
  const inInput = tag === 'INPUT' || tag === 'SELECT' || tag === 'TEXTAREA'

  // Ctrl+Z / Ctrl+Y always work
  if (e.ctrlKey && e.key === 'z') { e.preventDefault(); undo(); return }
  if (e.ctrlKey && e.key === 'y') { e.preventDefault(); redo(); return }
  if (e.ctrlKey && e.shiftKey && e.key === 'Z') { e.preventDefault(); redo(); return }

  // Enter saves from anywhere
  if (e.key === 'Enter' && !e.ctrlKey) {
    e.preventDefault()
    document.getElementById('btn-save').click()
    return
  }

  // Escape: cancel add mode → clear search → deselect
  if (e.key === 'Escape') {
    if (addMode) {
      toggleAddMode(false)
    } else {
      const search = document.getElementById('search')
      if (search.value) {
        search.value = ''
        updateFilter()
      } else {
        selectedIdx = -1
        selectedIndices.clear()
        updateEditorForSelection()
        renderList()
        renderPreview()
        renderTileset()
      }
    }
    return
  }

  if (inInput) return

  // Arrow keys navigate filtered list
  if (e.key === 'ArrowUp' || e.key === 'ArrowDown') {
    e.preventDefault()
    if (!data || filtered.length === 0) return
    const pos = filtered.indexOf(selectedIdx)
    if (e.key === 'ArrowUp') {
      if (pos > 0) selectAsset(filtered[pos - 1])
      else if (pos === -1 && filtered.length > 0) selectAsset(filtered[filtered.length - 1])
    } else {
      if (pos < filtered.length - 1) selectAsset(filtered[pos + 1])
      else if (pos === -1 && filtered.length > 0) selectAsset(filtered[0])
    }
  }
}

// ════════════════════════════════════════════════════════════════════════
// EXPORT ASSETS
// ════════════════════════════════════════════════════════════════════════

function showExportModal() {
  if (!data || !tilesetImg) {
    statusMsg.textContent = 'Load a tileset PNG before exporting'
    return
  }
  const items = collectExportItems()
  const groups = items.filter(i => i.leafAssets.length > 1)
  const ungrouped = items.filter(i => i.leafAssets.length === 1)
  const totalPngs = items.reduce((sum, i) => sum + i.leafAssets.length, 0)

  document.getElementById('export-summary').innerHTML =
    '<b>' + items.length + '</b> folders total: ' +
    '<b>' + groups.length + '</b> groups, ' +
    '<b>' + ungrouped.length + '</b> ungrouped assets, ' +
    '<b>' + totalPngs + '</b> PNGs'

  document.getElementById('export-progress').style.display = 'none'
  document.getElementById('export-result').style.display = 'none'
  document.getElementById('export-start-btn').disabled = false

  const modal = document.getElementById('export-modal')
  modal.style.display = 'flex'
}

function hideExportModal() {
  document.getElementById('export-modal').style.display = 'none'
}

document.getElementById('btn-export').onclick = showExportModal
document.getElementById('export-modal-close').onclick = hideExportModal
document.getElementById('export-cancel-btn').onclick = hideExportModal
document.getElementById('export-modal').onclick = (e) => {
  if (e.target === document.getElementById('export-modal')) hideExportModal()
}

// Collect all export units: { folderId, manifest, leafAssets, category }
function collectExportItems() {
  if (!data) return []
  const items = []
  const groupedAssetIds = new Set()

  // Process top-level groups
  const topGroups = getTopLevelGroups()
  for (const group of topGroups) {
    const leafIds = []
    for (const mid of group.members) {
      leafIds.push(...resolveGroupAssets(mid))
    }
    const leafAssets = leafIds.map(id => data.assets.find(a => a.id === id)).filter(Boolean)
    if (leafAssets.length === 0) continue

    for (const id of leafIds) groupedAssetIds.add(id)

    const manifest = buildManifest(group, leafAssets)
    items.push({
      folderId: group.id,
      manifest,
      leafAssets,
      category: group.category || leafAssets[0].category || 'misc'
    })
  }

  // Ungrouped, non-discarded assets
  for (const asset of data.assets) {
    if (asset.discard || groupedAssetIds.has(asset.id)) continue
    if (asset.groupId && !groupedAssetIds.has(asset.id)) {
      // Part of a sub-group already handled
      const directGroup = data.groups ? data.groups.find(g => g.members.includes(asset.id)) : null
      if (directGroup && isSubGroup(directGroup.id)) continue
    }
    // Skip if already in a group we processed
    if (asset.partOfGroup) continue

    const manifest = buildManifestUngrouped(asset)
    items.push({
      folderId: asset.name || asset.id,
      manifest,
      leafAssets: [asset],
      category: asset.category || 'misc'
    })
  }

  return items
}

function buildManifest(group, leafAssets) {
  const category = group.category || leafAssets[0].category || 'misc'
  const scheme = group.rotationScheme || '4-way'

  const manifest = {
    id: group.id,
    name: group.name || group.id,
    category,
    type: 'group',
    groupType: group.type,
    ...(group.type === 'rotation' ? { rotationScheme: scheme } : {}),
    canPlaceOnWalls: !!group.canPlaceOnWalls,
    canPlaceOnSurfaces: !!group.canPlaceOnSurfaces,
    backgroundTiles: group.backgroundTiles || 0,
    members: buildMembersList(group, group.type, scheme),
  }

  return manifest
}

// Recursively build the members array for a group
// Each entry is either { type: "asset", ... } or { type: "group", ... }
function buildMembersList(group, parentType, rootScheme) {
  const members = []
  for (let i = 0; i < group.members.length; i++) {
    const mid = group.members[i]
    if (mid.startsWith('@')) {
      const subGroupId = mid.slice(1)
      const subGroup = data.groups.find(g => g.id === subGroupId)
      if (!subGroup) continue

      const parentRole = group.memberRoles ? group.memberRoles[mid] : undefined
      const subEntry = { type: 'group', groupType: subGroup.type }
      // Assign the role from the parent group
      if (parentType === 'rotation' && parentRole) subEntry.orientation = resolveOrientation(parentRole, rootScheme)
      if (parentType === 'state' && parentRole) subEntry.state = parentRole
      if (parentType === 'animation') subEntry.frame = i
      // Recurse into sub-group
      subEntry.members = buildMembersList(subGroup, subGroup.type, rootScheme)
      members.push(subEntry)
    } else {
      const asset = data.assets.find(a => a.id === mid)
      if (!asset) continue
      const role = group.memberRoles ? group.memberRoles[mid] : undefined
      const entry = buildAssetMember(asset)
      applyRoleToEntry(entry, parentType, role, asset, rootScheme, i)
      members.push(entry)
    }
  }
  return members
}

// Apply role fields to an asset entry based on group type
function applyRoleToEntry(entry, groupType, role, asset, scheme, index) {
  if (groupType === 'rotation') {
    const orientation = role || asset.orientation || 'front'
    entry.orientation = resolveOrientation(orientation, scheme)
    if (scheme === '3-way-mirror' && (orientation === 'right' || orientation === 'side')) {
      entry.mirrorSide = true
    }
  }
  if (groupType === 'state') entry.state = role || asset.state || 'off'
  if (groupType === 'animation') entry.frame = index
}

// Resolve orientation label: 2-way and 3-way-mirror use "side" instead of "right"
function resolveOrientation(orientation, scheme) {
  if ((scheme === '2-way' || scheme === '3-way-mirror') && orientation === 'right') return 'side'
  return orientation
}

function buildManifestUngrouped(asset) {
  return {
    id: asset.name || asset.id,
    name: asset.label || asset.name || asset.id,
    category: asset.category || 'misc',
    type: 'asset',
    canPlaceOnWalls: !!asset.canPlaceOnWalls,
    canPlaceOnSurfaces: !!asset.canPlaceOnSurfaces,
    backgroundTiles: asset.backgroundTiles || 0,
    width: asset.paddedWidth,
    height: asset.paddedHeight,
    footprintW: asset.footprintW || Math.ceil(asset.paddedWidth / 16),
    footprintH: asset.footprintH || 1,
  }
}

function buildAssetMember(asset) {
  return {
    type: 'asset',
    id: asset.name || asset.id,
    file: (asset.name || asset.id) + '.png',
    width: asset.paddedWidth,
    height: asset.paddedHeight,
    footprintW: asset.footprintW || Math.ceil(asset.paddedWidth / 16),
    footprintH: asset.footprintH || 1,
  }
}

// Extract a single asset as a PNG Blob from the tileset canvas
function extractAssetPngBlob(asset) {
  return new Promise((resolve) => {
    const w = asset.paddedWidth
    const h = asset.paddedHeight
    const canvas = document.createElement('canvas')
    canvas.width = w
    canvas.height = h
    const ctx = canvas.getContext('2d')

    // Draw the tileset region
    const srcX = Math.max(0, asset.paddedX)
    const srcY = Math.max(0, asset.paddedY)
    const offX = Math.max(0, -asset.paddedX)
    const offY = Math.max(0, -asset.paddedY)
    const srcW = Math.min(w - offX, tilesetImg.width - srcX)
    const srcH = Math.min(h - offY, tilesetImg.height - srcY)

    if (srcW > 0 && srcH > 0) {
      ctx.drawImage(tilesetImg, srcX, srcY, srcW, srcH, offX, offY, srcW, srcH)
    }

    // Apply erased pixels
    if (asset.erasedPixels && asset.erasedPixels.length > 0) {
      const imgData = ctx.getImageData(0, 0, w, h)
      for (const p of asset.erasedPixels) {
        if (p.x >= 0 && p.x < w && p.y >= 0 && p.y < h) {
          const idx = (p.y * w + p.x) * 4
          imgData.data[idx] = 0
          imgData.data[idx + 1] = 0
          imgData.data[idx + 2] = 0
          imgData.data[idx + 3] = 0
        }
      }
      ctx.putImageData(imgData, 0, 0)
    }

    canvas.toBlob(resolve, 'image/png')
  })
}

async function exportAssets() {
  if (!window.showDirectoryPicker) {
    document.getElementById('export-result').style.display = 'block'
    document.getElementById('export-result').style.background = '#4a1a1a'
    document.getElementById('export-result').style.border = '1px solid #6b2020'
    document.getElementById('export-result').textContent = 'Export requires a Chromium browser (Chrome/Edge) with File System Access API support.'
    return
  }

  let rootDir
  try {
    rootDir = await window.showDirectoryPicker({ mode: 'readwrite' })
  } catch (err) {
    if (err.name === 'AbortError') return
    throw err
  }

  const useCategoryFolders = document.querySelector('input[name="export-org"]:checked').value === 'category'
  const items = collectExportItems()
  const totalPngs = items.reduce((sum, i) => sum + i.leafAssets.length, 0)
  let exportedPngs = 0

  document.getElementById('export-progress').style.display = 'block'
  document.getElementById('export-result').style.display = 'none'
  document.getElementById('export-start-btn').disabled = true

  const furnitureDir = await rootDir.getDirectoryHandle('furniture', { create: true })

  try {
    for (const item of items) {
      let parentDir = furnitureDir
      if (useCategoryFolders) {
        parentDir = await furnitureDir.getDirectoryHandle(item.category, { create: true })
      }
      const groupDir = await parentDir.getDirectoryHandle(item.folderId, { create: true })

      // Write manifest.json
      const mHandle = await groupDir.getFileHandle('manifest.json', { create: true })
      const mWritable = await mHandle.createWritable()
      await mWritable.write(JSON.stringify(item.manifest, null, 2))
      await mWritable.close()

      // Write PNGs
      for (const asset of item.leafAssets) {
        const blob = await extractAssetPngBlob(asset)
        const filename = (asset.name || asset.id) + '.png'
        const pHandle = await groupDir.getFileHandle(filename, { create: true })
        const pWritable = await pHandle.createWritable()
        await pWritable.write(blob)
        await pWritable.close()

        exportedPngs++
        const pct = Math.round((exportedPngs / totalPngs) * 100)
        document.getElementById('export-progress-bar').style.width = pct + '%'
        document.getElementById('export-progress-text').textContent =
          'Exporting... ' + exportedPngs + '/' + totalPngs + ' PNGs (' + pct + '%)'
      }
    }

    document.getElementById('export-progress-text').textContent =
      'Done! ' + exportedPngs + ' PNGs in ' + items.length + ' folders'
    document.getElementById('export-result').style.display = 'block'
    document.getElementById('export-result').style.background = '#1a4a2a'
    document.getElementById('export-result').style.border = '1px solid #2a8a3a'
    document.getElementById('export-result').innerHTML =
      'Exported <b>' + exportedPngs + '</b> PNGs across <b>' + items.length + '</b> folders to <code>furniture/</code>'
    statusMsg.textContent = 'Export complete: ' + exportedPngs + ' PNGs in ' + items.length + ' folders'
  } catch (err) {
    document.getElementById('export-result').style.display = 'block'
    document.getElementById('export-result').style.background = '#4a1a1a'
    document.getElementById('export-result').style.border = '1px solid #6b2020'
    document.getElementById('export-result').textContent = 'Export failed: ' + (err.message || err)
    statusMsg.textContent = 'Export failed: ' + (err.message || err)
  }

  document.getElementById('export-start-btn').disabled = false
}

document.getElementById('export-start-btn').onclick = exportAssets
</script>
</body>
</html>
```

## File: `scripts/jsonl-viewer.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pixel Agents JSONL Log Viewer</title>
<style>
  :root {
    --bg: #0d1117;
    --bg2: #161b22;
    --bg3: #1c2128;
    --border: #30363d;
    --text: #c9d1d9;
    --text-dim: #8b949e;
    --accent: #58a6ff;
    --green: #3fb950;
    --red: #f85149;
    --orange: #d29922;
    --purple: #bc8cff;
    --yellow: #e3b341;
    --cyan: #39d2c0;
    --pink: #f778ba;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background: var(--bg);
    color: var(--text);
    display: flex;
    flex-direction: column;
    height: 100vh;
    overflow: hidden;
  }

  /* ── Header ── */
  header {
    background: var(--bg2);
    border-bottom: 1px solid var(--border);
    padding: 10px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    flex-shrink: 0;
  }
  header h1 { font-size: 16px; font-weight: 600; }
  header h1 span { color: var(--accent); }

  .hdr-btn {
    background: var(--bg3);
    color: var(--text);
    border: 1px solid var(--border);
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    cursor: pointer;
  }
  .hdr-btn:hover { border-color: var(--text-dim); }
  .hdr-btn.primary { background: var(--accent); color: #000; border-color: var(--accent); }
  .hdr-btn.primary:hover { opacity: 0.9; }

  .hdr-back {
    background: none;
    border: none;
    color: var(--accent);
    font-size: 13px;
    cursor: pointer;
    padding: 4px 8px;
    border-radius: 4px;
    display: none;
  }
  .hdr-back:hover { background: var(--bg3); }

  .hdr-path {
    font-size: 11px;
    color: var(--text-dim);
    font-family: 'Cascadia Code', 'Fira Code', monospace;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    max-width: 400px;
  }

  .hdr-stats {
    margin-left: auto;
    display: flex;
    gap: 14px;
    font-size: 12px;
    color: var(--text-dim);
  }
  .hdr-stats .sv { color: var(--text); font-weight: 600; }

  /* ── Views ── */
  .view { display: none; flex: 1; overflow: hidden; }
  .view.active { display: flex; }

  /* ── Drop zone ── */
  #viewEmpty { align-items: center; justify-content: center; }
  .drop-zone {
    border: 2px dashed var(--border);
    border-radius: 12px;
    padding: 50px 60px;
    text-align: center;
    max-width: 550px;
  }
  .drop-zone h2 { color: var(--text); margin-bottom: 6px; font-size: 18px; }
  .drop-zone p { color: var(--text-dim); font-size: 13px; margin-bottom: 12px; }
  .drop-zone .btns { display: flex; gap: 10px; justify-content: center; margin-top: 18px; }
  .drop-zone.drag-over { border-color: var(--accent); background: rgba(88,166,255,0.05); }

  /* ── Session browser ── */
  .sessions-sidebar {
    width: 320px;
    min-width: 240px;
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    flex-shrink: 0;
  }
  .sessions-sidebar-header {
    padding: 10px 14px;
    border-bottom: 1px solid var(--border);
    font-size: 12px;
    color: var(--text-dim);
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
  }
  .sessions-sidebar-header .count { color: var(--text); font-weight: 600; }
  .sessions-search {
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 11px;
    flex: 1;
    min-width: 0;
  }
  .sessions-search::placeholder { color: var(--text-dim); }
  .sessions-list { flex: 1; overflow-y: auto; }

  .session-card {
    padding: 10px 14px;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    transition: background 0.1s;
  }
  .session-card:hover { background: var(--bg2); }
  .session-card.selected { background: var(--bg3); border-left: 3px solid var(--accent); }
  .session-card-name {
    font-size: 12px;
    font-family: monospace;
    color: var(--text);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .session-card-meta {
    font-size: 11px;
    color: var(--text-dim);
    margin-top: 3px;
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }
  .session-card-preview {
    font-size: 11px;
    color: var(--text-dim);
    margin-top: 4px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    font-style: italic;
  }

  .sessions-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  .convo-header {
    padding: 10px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 12px;
    flex-shrink: 0;
    background: var(--bg2);
  }
  .convo-header-name {
    font-size: 13px;
    font-weight: 600;
    font-family: monospace;
  }
  .convo-header .hdr-btn { font-size: 11px; padding: 4px 10px; }
  .convo-header-spacer { flex: 1; }

  .convo-body {
    flex: 1;
    overflow-y: auto;
    padding: 20px 24px;
  }
  .convo-placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    color: var(--text-dim);
    font-size: 14px;
  }

  /* ── Conversation messages ── */
  .convo-msg {
    margin-bottom: 16px;
    max-width: 900px;
  }
  .convo-msg-role {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
    padding-left: 2px;
  }
  .convo-msg-role.user { color: var(--accent); }
  .convo-msg-role.assistant { color: var(--green); }

  .convo-msg-body {
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 13px;
    line-height: 1.6;
    white-space: pre-wrap;
    word-break: break-word;
  }
  .convo-msg.user .convo-msg-body {
    background: #111d2e;
    border: 1px solid #1f3a5f;
  }
  .convo-msg.assistant .convo-msg-body {
    background: var(--bg2);
    border: 1px solid var(--border);
  }

  .convo-msg-truncated {
    max-height: 260px;
    overflow: hidden;
    position: relative;
  }
  .convo-msg-truncated::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: linear-gradient(transparent, var(--bg2));
    pointer-events: none;
  }
  .convo-msg.user .convo-msg-truncated::after {
    background: linear-gradient(transparent, #111d2e);
  }

  .convo-expand-btn {
    background: none;
    border: none;
    color: var(--accent);
    font-size: 12px;
    cursor: pointer;
    padding: 4px 0;
    margin-top: 2px;
  }
  .convo-expand-btn:hover { text-decoration: underline; }

  .convo-tools {
    display: flex;
    gap: 4px;
    flex-wrap: wrap;
    margin-top: 8px;
    padding-top: 8px;
    border-top: 1px solid var(--border);
  }
  .convo-tool-pill {
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 3px;
    background: var(--bg3);
    color: var(--text-dim);
    font-weight: 600;
  }

  .convo-jump-btn {
    background: none;
    border: none;
    color: var(--text-dim);
    font-size: 11px;
    cursor: pointer;
    padding: 2px 6px;
    border-radius: 3px;
    margin-left: auto;
  }
  .convo-jump-btn:hover { color: var(--accent); background: var(--bg3); }

  .convo-turn-sep {
    display: flex;
    align-items: center;
    gap: 8px;
    margin: 20px 0;
    max-width: 900px;
  }
  .convo-turn-sep::before, .convo-turn-sep::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }
  .convo-turn-sep span {
    font-size: 10px;
    color: var(--text-dim);
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  /* ── Code in conversation ── */
  .convo-msg-body pre {
    background: var(--bg);
    border-radius: 4px;
    padding: 8px 10px;
    margin: 6px 0;
    overflow-x: auto;
    font-family: 'Cascadia Code', 'Fira Code', monospace;
    font-size: 12px;
    white-space: pre;
    line-height: 1.5;
  }
  .convo-msg-body code {
    background: var(--bg);
    padding: 1px 5px;
    border-radius: 3px;
    font-family: 'Cascadia Code', 'Fira Code', monospace;
    font-size: 12px;
  }
  .convo-msg-body pre code { background: none; padding: 0; }

  /* ── JSONL Detail view ── */
  .detail-wrap { display: flex; flex: 1; overflow: hidden; flex-direction: column; }

  .filter-bar {
    background: var(--bg2);
    border-bottom: 1px solid var(--border);
    padding: 8px 14px;
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
  }
  .filter-bar label { font-size: 12px; color: var(--text-dim); display: flex; align-items: center; gap: 4px; cursor: pointer; }
  .filter-bar input[type="checkbox"] { accent-color: var(--accent); }
  .filter-search {
    background: var(--bg);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 12px;
    width: 200px;
    margin-left: auto;
  }
  .filter-search::placeholder { color: var(--text-dim); }

  .timeline-bar {
    background: var(--bg2);
    border-bottom: 1px solid var(--border);
    padding: 6px 14px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: 6px;
    overflow-x: auto;
  }
  .timeline-dot {
    width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; cursor: pointer; transition: transform 0.1s;
  }
  .timeline-dot:hover { transform: scale(1.8); }
  .timeline-dot.selected { transform: scale(2); box-shadow: 0 0 0 2px var(--text); }
  .timeline-dot.td-assistant { background: var(--accent); }
  .timeline-dot.td-user { background: var(--green); }
  .timeline-dot.td-system { background: var(--orange); }
  .timeline-dot.td-progress { background: var(--purple); }
  .timeline-dot.td-unknown { background: var(--text-dim); }

  .detail-body { display: flex; flex: 1; overflow: hidden; }

  .record-list {
    width: 440px;
    min-width: 300px;
    border-right: 1px solid var(--border);
    overflow-y: auto;
    flex-shrink: 0;
  }
  .record-item {
    padding: 8px 14px;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    display: flex;
    align-items: flex-start;
    gap: 10px;
    font-size: 13px;
    transition: background 0.1s;
  }
  .record-item:hover { background: var(--bg2); }
  .record-item.selected { background: var(--bg3); border-left: 3px solid var(--accent); }
  .record-index { color: var(--text-dim); font-family: monospace; font-size: 11px; min-width: 32px; text-align: right; padding-top: 2px; flex-shrink: 0; }
  .record-badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; flex-shrink: 0; min-width: 70px; text-align: center; }
  .badge-assistant { background: #1f3a5f; color: var(--accent); }
  .badge-user { background: #1a3a1a; color: var(--green); }
  .badge-system { background: #3a2a1a; color: var(--orange); }
  .badge-progress { background: #2a1a3a; color: var(--purple); }
  .badge-unknown { background: var(--bg3); color: var(--text-dim); }

  .record-summary { flex: 1; min-width: 0; }
  .record-summary-text { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: var(--text); font-size: 12px; }
  .record-summary-sub { font-size: 11px; color: var(--text-dim); margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .state-badges { display: flex; gap: 4px; flex-wrap: wrap; margin-top: 4px; }
  .state-badge { font-size: 10px; padding: 1px 6px; border-radius: 3px; font-weight: 600; white-space: nowrap; }
  .sb-tool-start { background: #1f3a5f; color: #79c0ff; }
  .sb-tool-done { background: #1a3a1a; color: #7ee787; }
  .sb-turn-end { background: #3a2a1a; color: #ffa657; }
  .sb-waiting { background: #2a3a1a; color: var(--green); }
  .sb-new-turn { background: #1a2a3a; color: var(--cyan); }
  .sb-permission-start { background: #3a1a2a; color: var(--pink); }
  .sb-permission-restart { background: #3a1a2a; color: var(--pink); border: 1px dashed var(--pink); }
  .sb-text-idle-start { background: #2a2a1a; color: var(--yellow); }
  .sb-active { background: #1f3a5f; color: var(--accent); }
  .sb-cancel-waiting { background: #2a1a1a; color: var(--red); }
  .sb-cancel-permission { background: #2a1a1a; color: var(--red); }
  .sb-clear-activity { background: #2a1a1a; color: var(--red); }
  .sb-subagent { background: #2a1a3a; color: var(--purple); }

  .detail-panel { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
  .detail-header { background: var(--bg2); border-bottom: 1px solid var(--border); padding: 8px 20px; display: flex; align-items: center; gap: 12px; flex-shrink: 0; }
  .detail-tabs { display: flex; gap: 2px; }
  .detail-tab { background: transparent; color: var(--text-dim); border: none; padding: 5px 12px; font-size: 12px; cursor: pointer; border-radius: 4px; }
  .detail-tab:hover { background: var(--bg3); color: var(--text); }
  .detail-tab.active { background: var(--bg3); color: var(--text); font-weight: 600; }
  .detail-content { flex: 1; overflow-y: auto; padding: 16px 20px; }
  .detail-placeholder { display: flex; align-items: center; justify-content: center; height: 100%; color: var(--text-dim); font-size: 14px; }

  /* ── JSON tree ── */
  .json-tree { font-family: 'Cascadia Code', 'Fira Code', monospace; font-size: 13px; line-height: 1.6; }
  .json-key { color: #79c0ff; }
  .json-string { color: #a5d6ff; }
  .json-number { color: #ffa657; }
  .json-boolean { color: var(--purple); }
  .json-null { color: var(--text-dim); }
  .json-bracket { color: var(--text-dim); }
  .json-toggle { cursor: pointer; user-select: none; display: inline-block; width: 14px; text-align: center; color: var(--text-dim); }
  .json-toggle:hover { color: var(--text); }
  .json-collapsed { display: none; }
  .json-collapsible { margin-left: 20px; }

  /* ── Parsed/state detail ── */
  .parsed-section { margin-bottom: 20px; }
  .parsed-section h3 { font-size: 13px; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; padding-bottom: 4px; border-bottom: 1px solid var(--border); }
  .parsed-field { display: flex; gap: 12px; padding: 4px 0; font-size: 13px; }
  .parsed-label { color: var(--text-dim); min-width: 120px; flex-shrink: 0; }
  .parsed-value { color: var(--text); font-family: 'Cascadia Code', 'Fira Code', monospace; word-break: break-all; }
  .tool-block { background: var(--bg2); border: 1px solid var(--border); border-radius: 6px; padding: 10px 14px; margin-bottom: 8px; }
  .tool-block-header { display: flex; align-items: center; gap: 8px; margin-bottom: 6px; }
  .tool-name { font-weight: 600; color: var(--accent); font-size: 13px; }
  .tool-id { font-size: 11px; color: var(--text-dim); font-family: monospace; }
  .tool-input { background: var(--bg); border-radius: 4px; padding: 8px 10px; font-family: monospace; font-size: 12px; max-height: 200px; overflow-y: auto; white-space: pre-wrap; word-break: break-all; }
  .text-content { background: var(--bg2); border: 1px solid var(--border); border-radius: 6px; padding: 12px 16px; font-size: 13px; line-height: 1.6; white-space: pre-wrap; word-break: break-word; max-height: 400px; overflow-y: auto; }
  .state-overlay-detail { background: var(--bg2); border: 1px solid var(--border); border-radius: 6px; padding: 14px 18px; margin-bottom: 12px; }
  .state-overlay-detail h3 { font-size: 14px; margin-bottom: 10px; color: var(--accent); }
  .state-event { display: flex; align-items: flex-start; gap: 10px; padding: 6px 0; border-bottom: 1px solid #21262d; font-size: 13px; }
  .state-event:last-child { border-bottom: none; }
  .state-event-icon { font-size: 14px; flex-shrink: 0; width: 20px; text-align: center; }
  .state-event-text { flex: 1; }
  .state-event-text .reason { color: var(--text-dim); font-size: 12px; display: block; margin-top: 2px; }
  .state-snapshot { background: var(--bg); border-radius: 4px; padding: 10px 14px; font-family: monospace; font-size: 12px; line-height: 1.6; }
  .state-field { display: flex; gap: 8px; }
  .state-field-name { color: var(--text-dim); min-width: 180px; }
  .state-true { color: var(--green); }
  .state-false { color: var(--red); }
  .state-set-empty { color: var(--text-dim); font-style: italic; }
  .state-set-items { color: var(--accent); }

  /* ── Legend ── */
  .detail-legend {
    background: var(--bg2);
    border-top: 1px solid var(--border);
    padding: 5px 14px;
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    flex-shrink: 0;
    font-size: 11px;
  }
  .legend-item { display: flex; align-items: center; gap: 4px; color: var(--text-dim); }
  .legend-swatch { width: 10px; height: 10px; border-radius: 2px; }

  .resizer { width: 4px; background: var(--border); cursor: col-resize; flex-shrink: 0; }
  .resizer:hover { background: var(--accent); }

  /* ── Scrollbar ── */
  ::-webkit-scrollbar { width: 8px; height: 8px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--border); border-radius: 4px; }
  ::-webkit-scrollbar-thumb:hover { background: var(--text-dim); }
</style>
</head>
<body>

<header>
  <button class="hdr-back" id="backBtn">← Back</button>
  <h1><span>Pixel Agents</span> JSONL Viewer</h1>
  <span class="hdr-path" id="hdrPath"></span>
  <div class="hdr-stats" id="hdrStats"></div>
</header>

<!-- ─── View: Empty / Drop zone ─── -->
<div class="view active" id="viewEmpty">
  <div class="drop-zone" id="dropZone">
    <h2>Open a JSONL project folder</h2>
    <p>Load a folder to browse sessions, or a single file to inspect it</p>
    <p style="font-size:11px;color:var(--text-dim);margin-bottom:4px">
      Sessions live at: <code>~/.claude/projects/&lt;hash&gt;/</code>
    </p>
    <div class="btns">
      <button class="hdr-btn primary" id="openFolderBtn">Open Folder</button>
      <button class="hdr-btn" id="openFileBtn">Open File</button>
    </div>
  </div>
</div>

<!-- ─── View: Session browser ─── -->
<div class="view" id="viewSessions">
  <div class="sessions-sidebar">
    <div class="sessions-sidebar-header">
      <span>Sessions: <span class="count" id="sessionCount">0</span></span>
      <input type="text" class="sessions-search" id="sessionSearch" placeholder="Filter sessions...">
    </div>
    <div class="sessions-list" id="sessionsList"></div>
  </div>
  <div class="sessions-main">
    <div class="convo-header" id="convoHeader" style="display:none">
      <span class="convo-header-name" id="convoName"></span>
      <div class="convo-header-spacer"></div>
      <button class="hdr-btn" id="viewJsonlBtn">View Full JSONL →</button>
    </div>
    <div class="convo-body" id="convoBody">
      <div class="convo-placeholder">Select a session to preview</div>
    </div>
  </div>
</div>

<!-- ─── View: JSONL detail ─── -->
<div class="view" id="viewDetail">
  <div class="detail-wrap">
    <div class="filter-bar">
      <label><input type="checkbox" checked data-filter="assistant"> assistant</label>
      <label><input type="checkbox" checked data-filter="user"> user</label>
      <label><input type="checkbox" checked data-filter="system"> system</label>
      <label><input type="checkbox" checked data-filter="progress"> progress</label>
      <label><input type="checkbox" checked data-filter="unknown"> other</label>
      <span style="color:var(--border)">|</span>
      <label><input type="checkbox" checked id="showStateOverlay"> State overlay</label>
      <input type="text" class="filter-search" id="searchInput" placeholder="Search records...">
    </div>
    <div class="timeline-bar" id="timelineBar"></div>
    <div class="detail-body">
      <div class="record-list" id="recordList"></div>
      <div class="resizer" id="resizer"></div>
      <div class="detail-panel">
        <div class="detail-header">
          <div class="detail-tabs">
            <button class="detail-tab active" data-tab="parsed">Parsed</button>
            <button class="detail-tab" data-tab="state">State</button>
            <button class="detail-tab" data-tab="raw">Raw JSON</button>
          </div>
        </div>
        <div class="detail-content" id="detailContent">
          <div class="detail-placeholder">Select a record to view details</div>
        </div>
      </div>
    </div>
    <div class="detail-legend">
      <div class="legend-item"><div class="legend-swatch" style="background:#79c0ff"></div> Tool start</div>
      <div class="legend-item"><div class="legend-swatch" style="background:#7ee787"></div> Tool done</div>
      <div class="legend-item"><div class="legend-swatch" style="background:#ffa657"></div> Turn end</div>
      <div class="legend-item"><div class="legend-swatch" style="background:var(--green)"></div> Waiting</div>
      <div class="legend-item"><div class="legend-swatch" style="background:var(--cyan)"></div> New turn</div>
      <div class="legend-item"><div class="legend-swatch" style="background:var(--pink)"></div> Permission</div>
      <div class="legend-item"><div class="legend-swatch" style="background:var(--yellow)"></div> Text-idle</div>
      <div class="legend-item"><div class="legend-swatch" style="background:var(--red)"></div> Cancel</div>
      <div class="legend-item"><div class="legend-swatch" style="background:var(--purple)"></div> Subagent</div>
    </div>
  </div>
</div>

<input type="file" id="fileInput" accept=".jsonl" style="display:none">
<input type="file" id="folderInput" webkitdirectory style="display:none">

<script>
// ══════════════════════════════════════════════════════════════
//  Constants
// ══════════════════════════════════════════════════════════════
const TOOL_DONE_DELAY_MS = 300;
const PERMISSION_TIMER_DELAY_MS = 7000;
const TEXT_IDLE_DELAY_MS = 5000;
const PERMISSION_EXEMPT_TOOLS = new Set(['Task', 'AskUserQuestion']);
const CONVO_TRUNCATE_HEIGHT = 260; // px before truncation

// ══════════════════════════════════════════════════════════════
//  App state
// ══════════════════════════════════════════════════════════════
let currentView = 'empty'; // 'empty' | 'sessions' | 'detail'
let sessions = [];          // { name, file?, text, records, conversation, size, lastModified }
let selectedSessionIdx = -1;
let sessionSearchQuery = '';

// Detail view state (for currently-viewed session)
let records = [];
let processedRecords = [];
let selectedRecordIdx = -1;
let activeTab = 'parsed';
let filters = { assistant: true, user: true, system: true, progress: true, unknown: true };
let searchQuery = '';

// ══════════════════════════════════════════════════════════════
//  Elements
// ══════════════════════════════════════════════════════════════
const backBtn = document.getElementById('backBtn');
const hdrPath = document.getElementById('hdrPath');
const hdrStats = document.getElementById('hdrStats');
const viewEmpty = document.getElementById('viewEmpty');
const viewSessions = document.getElementById('viewSessions');
const viewDetail = document.getElementById('viewDetail');
const dropZone = document.getElementById('dropZone');
const sessionsList = document.getElementById('sessionsList');
const sessionCount = document.getElementById('sessionCount');
const sessionSearch = document.getElementById('sessionSearch');
const convoHeader = document.getElementById('convoHeader');
const convoName = document.getElementById('convoName');
const convoBody = document.getElementById('convoBody');
const recordList = document.getElementById('recordList');
const detailContent = document.getElementById('detailContent');
const timelineBar = document.getElementById('timelineBar');
const searchInput = document.getElementById('searchInput');

// ══════════════════════════════════════════════════════════════
//  View management
// ══════════════════════════════════════════════════════════════
function showView(name) {
  currentView = name;
  viewEmpty.classList.toggle('active', name === 'empty');
  viewSessions.classList.toggle('active', name === 'sessions');
  viewDetail.classList.toggle('active', name === 'detail');
  backBtn.style.display = (name === 'detail') ? '' : 'none';
}

backBtn.addEventListener('click', () => {
  if (sessions.length > 0) {
    showView('sessions');
    hdrPath.textContent = sessions._folderPath || '';
    updateSessionStats();
  } else {
    showView('empty');
    hdrPath.textContent = '';
    hdrStats.innerHTML = '';
  }
});

// ══════════════════════════════════════════════════════════════
//  File & folder loading
// ══════════════════════════════════════════════════════════════
document.getElementById('openFolderBtn').addEventListener('click', () => openFolder());
document.getElementById('openFileBtn').addEventListener('click', () => document.getElementById('fileInput').click());
document.getElementById('viewJsonlBtn').addEventListener('click', () => openDetailForCurrentSession());

document.getElementById('fileInput').addEventListener('change', (e) => {
  if (e.target.files[0]) loadSingleFile(e.target.files[0]);
  e.target.value = '';
});
document.getElementById('folderInput').addEventListener('change', (e) => {
  loadFilesFromInput(e.target.files);
  e.target.value = '';
});

// Drag & drop (folder or file)
document.body.addEventListener('dragover', (e) => { e.preventDefault(); dropZone?.classList.add('drag-over'); });
document.body.addEventListener('dragleave', (e) => { if (e.target === document.body || e.target === dropZone) dropZone?.classList.remove('drag-over'); });
document.body.addEventListener('drop', async (e) => {
  e.preventDefault();
  dropZone?.classList.remove('drag-over');
  const items = [...(e.dataTransfer?.items || [])];
  // Try folder via webkitGetAsEntry
  for (const item of items) {
    const entry = item.webkitGetAsEntry?.();
    if (entry?.isDirectory) {
      const files = await readDirectoryEntry(entry);
      const jsonlFiles = files.filter(f => f.name.endsWith('.jsonl'));
      if (jsonlFiles.length > 0) {
        await loadFileObjects(jsonlFiles, entry.name);
        return;
      }
    }
  }
  // Fallback: single file
  const file = e.dataTransfer?.files?.[0];
  if (file?.name.endsWith('.jsonl')) loadSingleFile(file);
});

async function openFolder() {
  if (window.showDirectoryPicker) {
    try {
      const handle = await window.showDirectoryPicker();
      const files = [];
      for await (const entry of handle.values()) {
        if (entry.kind === 'file' && entry.name.endsWith('.jsonl')) {
          files.push(await entry.getFile());
        }
      }
      if (files.length > 0) {
        await loadFileObjects(files, handle.name);
      }
    } catch (e) {
      if (e.name !== 'AbortError') console.error(e);
    }
  } else {
    document.getElementById('folderInput').click();
  }
}

function readDirectoryEntry(dirEntry) {
  return new Promise((resolve) => {
    const reader = dirEntry.createReader();
    const allFiles = [];
    let pending = 0;
    let doneReading = false;

    function readBatch() {
      reader.readEntries((entries) => {
        if (entries.length === 0) {
          doneReading = true;
          if (pending === 0) resolve(allFiles);
          return;
        }
        for (const entry of entries) {
          if (entry.isFile && entry.name.endsWith('.jsonl')) {
            pending++;
            entry.file((f) => {
              allFiles.push(f);
              pending--;
              if (doneReading && pending === 0) resolve(allFiles);
            });
          }
        }
        readBatch();
      });
    }
    readBatch();
  });
}

function loadFilesFromInput(fileList) {
  const files = [...fileList].filter(f => f.name.endsWith('.jsonl'));
  if (files.length > 0) loadFileObjects(files, files[0].webkitRelativePath?.split('/')[0] || 'folder');
}

async function loadFileObjects(files, folderName) {
  sessions = [];
  sessions._folderPath = folderName;

  for (const file of files) {
    const text = await file.text();
    const recs = parseJsonlText(text);
    const conversation = extractConversation(recs);
    const turnCount = recs.filter(r => r.type === 'system' && r.subtype === 'turn_duration').length;
    sessions.push({
      name: file.name,
      text,
      records: recs,
      conversation,
      turnCount,
      size: file.size,
      lastModified: file.lastModified,
    });
  }

  // Sort by last modified (newest first)
  sessions.sort((a, b) => b.lastModified - a.lastModified);
  selectedSessionIdx = -1;

  hdrPath.textContent = folderName;
  updateSessionStats();
  renderSessionList();
  showView('sessions');

  // Auto-select first if only one
  if (sessions.length === 1) selectSession(0);
}

function loadSingleFile(file) {
  const reader = new FileReader();
  reader.onload = () => {
    const text = reader.result;
    const recs = parseJsonlText(text);
    const conversation = extractConversation(recs);
    const turnCount = recs.filter(r => r.type === 'system' && r.subtype === 'turn_duration').length;
    sessions = [{
      name: file.name,
      text,
      records: recs,
      conversation,
      turnCount,
      size: file.size,
      lastModified: file.lastModified,
    }];
    sessions._folderPath = '';

    hdrPath.textContent = file.name;
    selectedSessionIdx = 0;
    updateSessionStats();
    renderSessionList();
    showView('sessions');
    selectSession(0);
  };
  reader.readAsText(file);
}

// ══════════════════════════════════════════════════════════════
//  JSONL parsing
// ══════════════════════════════════════════════════════════════
function parseJsonlText(text) {
  const out = [];
  for (const line of text.split('\n')) {
    const t = line.trim();
    if (!t) continue;
    try { out.push(JSON.parse(t)); }
    catch { out.push({ _parseError: true, _raw: t }); }
  }
  return out;
}

// ══════════════════════════════════════════════════════════════
//  Conversation extraction
// ══════════════════════════════════════════════════════════════
function extractConversation(recs) {
  const messages = [];
  let assistantTexts = [];
  let toolsUsed = new Set();
  let assistantIndices = [];
  let turnNumber = 0;

  function flushAssistant() {
    if (assistantTexts.length > 0 || toolsUsed.size > 0) {
      messages.push({
        role: 'assistant',
        text: assistantTexts.join('\n\n'),
        tools: [...toolsUsed],
        recordIndices: [...assistantIndices],
        turn: turnNumber,
      });
    }
    assistantTexts = [];
    toolsUsed = new Set();
    assistantIndices = [];
  }

  for (let i = 0; i < recs.length; i++) {
    const r = recs[i];

    if (r.type === 'user') {
      const content = r.message?.content;
      let userText = '';
      if (typeof content === 'string' && content.trim()) {
        userText = content.trim();
      } else if (Array.isArray(content)) {
        const hasToolResult = content.some(b => b.type === 'tool_result');
        if (!hasToolResult) {
          userText = content.filter(b => b.type === 'text').map(b => b.text || '').join('\n').trim();
        }
      }
      if (userText) {
        flushAssistant();
        turnNumber++;
        messages.push({ role: 'user', text: userText, recordIndex: i, turn: turnNumber });
      }
    } else if (r.type === 'assistant' && Array.isArray(r.message?.content)) {
      for (const block of r.message.content) {
        if (block.type === 'text' && block.text?.trim()) assistantTexts.push(block.text.trim());
        if (block.type === 'tool_use' && block.name) toolsUsed.add(block.name);
      }
      assistantIndices.push(i);
    } else if (r.type === 'system' && r.subtype === 'turn_duration') {
      flushAssistant();
    } else if (r.type === 'progress' && r.data?.type === 'agent_progress') {
      const msg = r.data?.message;
      if (msg?.type === 'assistant' && Array.isArray(msg.message?.content)) {
        for (const block of msg.message.content) {
          if (block.type === 'tool_use' && block.name) toolsUsed.add(block.name);
        }
      }
    }
  }
  flushAssistant();
  return messages;
}

// ══════════════════════════════════════════════════════════════
//  Session list
// ══════════════════════════════════════════════════════════════
function updateSessionStats() {
  const total = sessions.length;
  sessionCount.textContent = total;
  hdrStats.innerHTML = `<span>Sessions: <span class="sv">${total}</span></span>`;
}

sessionSearch.addEventListener('input', () => {
  sessionSearchQuery = sessionSearch.value.toLowerCase();
  renderSessionList();
});

function renderSessionList() {
  sessionsList.innerHTML = '';
  const filtered = sessions.filter((s, i) => {
    if (!sessionSearchQuery) return true;
    const firstPrompt = s.conversation.find(m => m.role === 'user')?.text || '';
    return s.name.toLowerCase().includes(sessionSearchQuery) || firstPrompt.toLowerCase().includes(sessionSearchQuery);
  });

  for (let i = 0; i < sessions.length; i++) {
    const s = sessions[i];
    if (sessionSearchQuery) {
      const firstPrompt = s.conversation.find(m => m.role === 'user')?.text || '';
      if (!s.name.toLowerCase().includes(sessionSearchQuery) && !firstPrompt.toLowerCase().includes(sessionSearchQuery)) continue;
    }
    const card = document.createElement('div');
    card.className = `session-card${i === selectedSessionIdx ? ' selected' : ''}`;
    card.dataset.idx = i;

    const firstPrompt = s.conversation.find(m => m.role === 'user')?.text || '';
    const toolCount = s.records.filter(r => r.type === 'assistant' && Array.isArray(r.message?.content) && r.message.content.some(b => b.type === 'tool_use')).length;

    card.innerHTML = `
      <div class="session-card-name">${esc(s.name)}</div>
      <div class="session-card-meta">
        <span>${s.turnCount} turn${s.turnCount !== 1 ? 's' : ''}</span>
        <span>${toolCount} tool call${toolCount !== 1 ? 's' : ''}</span>
        <span>${formatSize(s.size)}</span>
        <span>${relativeTime(s.lastModified)}</span>
      </div>
      ${firstPrompt ? `<div class="session-card-preview">"${esc(firstPrompt.slice(0, 100))}"</div>` : ''}
    `;
    card.addEventListener('click', () => selectSession(i));
    sessionsList.appendChild(card);
  }
}

function selectSession(idx) {
  selectedSessionIdx = idx;
  sessionsList.querySelectorAll('.session-card').forEach(el => {
    el.classList.toggle('selected', parseInt(el.dataset.idx) === idx);
  });
  renderConversation(sessions[idx]);
}

// ══════════════════════════════════════════════════════════════
//  Conversation preview
// ══════════════════════════════════════════════════════════════
function renderConversation(session) {
  convoHeader.style.display = '';
  convoName.textContent = session.name;

  if (session.conversation.length === 0) {
    convoBody.innerHTML = '<div class="convo-placeholder">No user/assistant messages found</div>';
    return;
  }

  convoBody.innerHTML = '';
  let lastTurn = 0;

  for (const msg of session.conversation) {
    // Turn separator
    if (msg.role === 'user' && msg.turn > 1) {
      const sep = document.createElement('div');
      sep.className = 'convo-turn-sep';
      sep.innerHTML = `<span>Turn ${msg.turn}</span>`;
      convoBody.appendChild(sep);
    }

    const div = document.createElement('div');
    div.className = `convo-msg ${msg.role}`;

    const roleLabel = document.createElement('div');
    roleLabel.className = `convo-msg-role ${msg.role}`;
    roleLabel.textContent = msg.role === 'user' ? 'You' : 'Claude';
    div.appendChild(roleLabel);

    const body = document.createElement('div');
    body.className = 'convo-msg-body';
    body.innerHTML = renderMd(msg.text || '(no text)');
    div.appendChild(body);

    // Truncation
    convoBody.appendChild(div);
    requestAnimationFrame(() => {
      if (body.scrollHeight > CONVO_TRUNCATE_HEIGHT + 40) {
        body.classList.add('convo-msg-truncated');
        const btn = document.createElement('button');
        btn.className = 'convo-expand-btn';
        btn.textContent = 'Show more';
        btn.addEventListener('click', () => {
          body.classList.remove('convo-msg-truncated');
          btn.remove();
        });
        div.appendChild(btn);
      }
    });

    // Tools + jump button
    if (msg.role === 'assistant' && (msg.tools.length > 0 || msg.recordIndices)) {
      const footer = document.createElement('div');
      footer.className = 'convo-tools';
      for (const t of msg.tools) {
        const pill = document.createElement('span');
        pill.className = 'convo-tool-pill';
        pill.textContent = t;
        footer.appendChild(pill);
      }
      // Jump to first record index in JSONL detail
      if (msg.recordIndices?.length > 0) {
        const jumpBtn = document.createElement('button');
        jumpBtn.className = 'convo-jump-btn';
        jumpBtn.textContent = `JSONL #${msg.recordIndices[0]} →`;
        jumpBtn.addEventListener('click', () => {
          openDetailForCurrentSession(msg.recordIndices[0]);
        });
        footer.appendChild(jumpBtn);
      }
      div.appendChild(footer);
    }
    if (msg.role === 'user' && msg.recordIndex != null) {
      const footer = document.createElement('div');
      footer.className = 'convo-tools';
      const jumpBtn = document.createElement('button');
      jumpBtn.className = 'convo-jump-btn';
      jumpBtn.textContent = `JSONL #${msg.recordIndex} →`;
      jumpBtn.addEventListener('click', () => {
        openDetailForCurrentSession(msg.recordIndex);
      });
      footer.appendChild(jumpBtn);
      div.appendChild(footer);
    }

    lastTurn = msg.turn;
  }
}

// Minimal markdown: code blocks, inline code, bold
function renderMd(text) {
  // Escape HTML first
  let out = esc(text);
  // Code blocks: ```lang\ncode\n``` → <pre><code>
  out = out.replace(/```(\w*)\n([\s\S]*?)```/g, (_, lang, code) => `<pre><code>${code}</code></pre>`);
  // Inline code
  out = out.replace(/`([^`\n]+)`/g, '<code>$1</code>');
  // Bold
  out = out.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  return out;
}

// ══════════════════════════════════════════════════════════════
//  Open JSONL detail for current session
// ══════════════════════════════════════════════════════════════
function openDetailForCurrentSession(jumpToRecord) {
  if (selectedSessionIdx < 0) return;
  const session = sessions[selectedSessionIdx];
  records = session.records;
  processRecords();

  hdrPath.textContent = session.name;
  hdrStats.innerHTML = `
    <span>Records: <span class="sv">${records.length}</span></span>
    <span>Tools: <span class="sv">${records.filter(r => r.type === 'assistant' && Array.isArray(r.message?.content) && r.message.content.some(b => b.type === 'tool_use')).length}</span></span>
    <span>Turns: <span class="sv">${session.turnCount}</span></span>
  `;

  selectedRecordIdx = -1;
  showView('detail');
  renderRecordList();
  renderTimeline();

  if (jumpToRecord != null) {
    requestAnimationFrame(() => selectRecord(jumpToRecord));
  }
}

// ══════════════════════════════════════════════════════════════
//  State Machine Simulation (same as before)
// ══════════════════════════════════════════════════════════════
function processRecords() {
  const state = {
    activeToolIds: new Set(),
    activeToolStatuses: new Map(),
    activeToolNames: new Map(),
    activeSubagentToolIds: new Map(),
    activeSubagentToolNames: new Map(),
    isWaiting: false,
    permissionSent: false,
    hadToolsInTurn: false,
    waitingTimerActive: false,
    permissionTimerActive: false,
  };

  processedRecords = records.map((record, idx) => {
    const events = [];
    const snapshotBefore = cloneState(state);

    if (record._parseError) {
      return { record, index: idx, events, stateBefore: snapshotBefore, stateAfter: cloneState(state) };
    }

    // New data arrival → cancel timers
    if (state.waitingTimerActive) { events.push({ type: 'cancel-waiting', reason: 'New JSONL data arrived → cancel waiting timer' }); state.waitingTimerActive = false; }
    if (state.permissionTimerActive) { events.push({ type: 'cancel-permission', reason: 'New JSONL data arrived → cancel permission timer' }); state.permissionTimerActive = false; }
    if (state.permissionSent) { events.push({ type: 'clear-permission', reason: 'New JSONL data arrived → clear permission bubble' }); state.permissionSent = false; }

    if (record.type === 'assistant' && Array.isArray(record.message?.content)) {
      const blocks = record.message.content;
      const hasToolUse = blocks.some(b => b.type === 'tool_use');
      if (hasToolUse) {
        events.push({ type: 'cancel-waiting', reason: 'assistant has tool_use → cancel waiting timer' });
        state.waitingTimerActive = false;
        state.isWaiting = false;
        state.hadToolsInTurn = true;
        events.push({ type: 'active', reason: 'assistant has tool_use → status=active, hadToolsInTurn=true' });
        let hasNonExempt = false;
        for (const block of blocks) {
          if (block.type === 'tool_use' && block.id) {
            const toolName = block.name || '';
            const status = fmtToolStatus(toolName, block.input || {});
            state.activeToolIds.add(block.id);
            state.activeToolStatuses.set(block.id, status);
            state.activeToolNames.set(block.id, toolName);
            if (!PERMISSION_EXEMPT_TOOLS.has(toolName)) hasNonExempt = true;
            events.push({ type: 'tool-start', toolId: block.id, toolName, status, reason: `Tool start: ${toolName} [${block.id}]` });
          }
        }
        if (hasNonExempt) {
          state.permissionTimerActive = true;
          events.push({ type: 'permission-start', reason: `Permission timer started (${PERMISSION_TIMER_DELAY_MS}ms) — non-exempt tool(s) active` });
        }
      } else if (blocks.some(b => b.type === 'text') && !state.hadToolsInTurn) {
        state.waitingTimerActive = true;
        events.push({ type: 'text-idle-start', reason: `Text-only response, no tools this turn → text-idle timer started (${TEXT_IDLE_DELAY_MS}ms)` });
      }
    } else if (record.type === 'progress') {
      const parentToolId = record.parentToolUseID;
      const data = record.data;
      const dataType = data?.type;
      if (dataType === 'bash_progress' || dataType === 'mcp_progress') {
        if (parentToolId && state.activeToolIds.has(parentToolId)) {
          state.permissionTimerActive = true;
          events.push({ type: 'permission-restart', reason: `${dataType}: tool is executing, restart permission timer` });
        }
      } else if (dataType === 'agent_progress' && parentToolId && state.activeToolNames.get(parentToolId) === 'Task') {
        const msg = data?.message;
        const innerContent = msg?.message?.content;
        if (Array.isArray(innerContent)) {
          if (msg.type === 'assistant') {
            let hasNonExemptSub = false;
            for (const block of innerContent) {
              if (block.type === 'tool_use' && block.id) {
                const tn = block.name || '';
                let s = state.activeSubagentToolIds.get(parentToolId); if (!s) { s = new Set(); state.activeSubagentToolIds.set(parentToolId, s); } s.add(block.id);
                let n = state.activeSubagentToolNames.get(parentToolId); if (!n) { n = new Map(); state.activeSubagentToolNames.set(parentToolId, n); } n.set(block.id, tn);
                if (!PERMISSION_EXEMPT_TOOLS.has(tn)) hasNonExemptSub = true;
                events.push({ type: 'subagent-tool-start', toolId: block.id, toolName: tn, parentToolId, reason: `Subagent tool start: ${tn} [${block.id}]` });
              }
            }
            if (hasNonExemptSub) { state.permissionTimerActive = true; events.push({ type: 'permission-start', reason: 'Permission timer — non-exempt subagent tool(s)' }); }
          } else if (msg.type === 'user') {
            for (const block of innerContent) {
              if (block.type === 'tool_result' && block.tool_use_id) {
                state.activeSubagentToolIds.get(parentToolId)?.delete(block.tool_use_id);
                state.activeSubagentToolNames.get(parentToolId)?.delete(block.tool_use_id);
                events.push({ type: 'subagent-tool-done', toolId: block.tool_use_id, parentToolId, reason: `Subagent tool done: ${block.tool_use_id}` });
              }
            }
            let still = false;
            for (const [, sn] of state.activeSubagentToolNames) { for (const [, tn] of sn) { if (!PERMISSION_EXEMPT_TOOLS.has(tn)) { still = true; break; } } if (still) break; }
            if (still) { state.permissionTimerActive = true; events.push({ type: 'permission-restart', reason: 'Still has non-exempt subagent tools' }); }
          }
        }
      }
    } else if (record.type === 'user') {
      const content = record.message?.content;
      if (Array.isArray(content)) {
        if (content.some(b => b.type === 'tool_result')) {
          for (const block of content) {
            if (block.type === 'tool_result' && block.tool_use_id) {
              const cid = block.tool_use_id;
              if (state.activeToolNames.get(cid) === 'Task') {
                state.activeSubagentToolIds.delete(cid); state.activeSubagentToolNames.delete(cid);
                events.push({ type: 'subagent-clear', toolId: cid, reason: `Task completed → clear subagent` });
              }
              const tn = state.activeToolNames.get(cid);
              state.activeToolIds.delete(cid); state.activeToolStatuses.delete(cid); state.activeToolNames.delete(cid);
              events.push({ type: 'tool-done', toolId: cid, toolName: tn || '?', reason: `Tool done: ${tn || '?'} [${cid}]` });
            }
          }
        } else {
          events.push({ type: 'new-turn', reason: 'User text prompt → new turn' });
          events.push({ type: 'clear-activity', reason: 'clearAgentActivity' });
          state.waitingTimerActive = false; state.activeToolIds.clear(); state.activeToolStatuses.clear(); state.activeToolNames.clear();
          state.activeSubagentToolIds.clear(); state.activeSubagentToolNames.clear();
          state.isWaiting = false; state.permissionSent = false; state.hadToolsInTurn = false;
        }
      } else if (typeof content === 'string' && content.trim()) {
        events.push({ type: 'new-turn', reason: 'User text prompt → new turn' });
        events.push({ type: 'clear-activity', reason: 'clearAgentActivity' });
        state.waitingTimerActive = false; state.activeToolIds.clear(); state.activeToolStatuses.clear(); state.activeToolNames.clear();
        state.activeSubagentToolIds.clear(); state.activeSubagentToolNames.clear();
        state.isWaiting = false; state.permissionSent = false; state.hadToolsInTurn = false;
      }
    } else if (record.type === 'system' && record.subtype === 'turn_duration') {
      events.push({ type: 'turn-end', reason: 'turn_duration → definitive turn end' });
      state.waitingTimerActive = false; state.permissionTimerActive = false;
      if (state.activeToolIds.size > 0) {
        events.push({ type: 'clear-stale-tools', reason: `Clearing ${state.activeToolIds.size} stale tool(s): ${[...state.activeToolNames.values()].join(', ')}` });
        state.activeToolIds.clear(); state.activeToolStatuses.clear(); state.activeToolNames.clear();
        state.activeSubagentToolIds.clear(); state.activeSubagentToolNames.clear();
      }
      state.isWaiting = true; state.permissionSent = false; state.hadToolsInTurn = false;
      events.push({ type: 'waiting', reason: 'isWaiting=true, status=waiting' });
    }

    return { record, index: idx, events: dedup(events), stateBefore: snapshotBefore, stateAfter: cloneState(state) };
  });
}

function dedup(events) {
  const seen = new Set();
  return events.filter(e => {
    if (!e.type.startsWith('cancel-') && e.type !== 'clear-permission') return true;
    if (seen.has(e.type)) return false;
    seen.add(e.type);
    return true;
  });
}

function cloneState(s) {
  return {
    activeToolIds: new Set(s.activeToolIds), activeToolStatuses: new Map(s.activeToolStatuses), activeToolNames: new Map(s.activeToolNames),
    activeSubagentToolIds: new Map([...s.activeSubagentToolIds].map(([k,v])=>[k,new Set(v)])),
    activeSubagentToolNames: new Map([...s.activeSubagentToolNames].map(([k,v])=>[k,new Map(v)])),
    isWaiting: s.isWaiting, permissionSent: s.permissionSent, hadToolsInTurn: s.hadToolsInTurn,
    waitingTimerActive: s.waitingTimerActive, permissionTimerActive: s.permissionTimerActive,
  };
}

function fmtToolStatus(name, input) {
  const base = (p) => typeof p === 'string' ? p.split('/').pop().split('\\').pop() : '';
  switch (name) {
    case 'Read': return `Reading ${base(input.file_path)}`;
    case 'Edit': return `Editing ${base(input.file_path)}`;
    case 'Write': return `Writing ${base(input.file_path)}`;
    case 'Bash': { const c = input.command || ''; return `Running: ${c.length > 30 ? c.slice(0,30)+'…' : c}`; }
    case 'Glob': return 'Searching files';
    case 'Grep': return 'Searching code';
    case 'WebFetch': return 'Fetching web content';
    case 'WebSearch': return 'Searching the web';
    case 'Task': { const d = typeof input.description === 'string' ? input.description : ''; return d ? `Subtask: ${d.length > 40 ? d.slice(0,40)+'…' : d}` : 'Running subtask'; }
    case 'AskUserQuestion': return 'Waiting for your answer';
    case 'EnterPlanMode': return 'Planning';
    case 'NotebookEdit': return 'Editing notebook';
    default: return `Using ${name}`;
  }
}

// ══════════════════════════════════════════════════════════════
//  JSONL Detail View — Record list
// ══════════════════════════════════════════════════════════════
function getRecordType(r) { return r._parseError ? 'unknown' : (r.type || 'unknown'); }
function badgeCls(t) { return `badge-${t === 'assistant'||t === 'user'||t === 'system'||t === 'progress' ? t : 'unknown'}`; }

function summarize(r) {
  if (r._parseError) return { t: 'Parse error', s: r._raw?.slice(0,80) };
  if (r.type === 'assistant' && Array.isArray(r.message?.content)) {
    const c = r.message.content;
    const tools = c.filter(b=>b.type==='tool_use');
    const texts = c.filter(b=>b.type==='text');
    const think = c.filter(b=>b.type==='thinking');
    if (tools.length) return { t: `Tool use: ${tools.map(t=>t.name).join(', ')}`, s: tools.map(t=>fmtToolStatus(t.name,t.input||{})).join(' | ') };
    if (think.length && !texts.length) return { t: 'Thinking', s: think[0].thinking?.slice(0,80)||'' };
    if (texts.length) return { t: 'Text response', s: texts[0].text?.slice(0,80)||'' };
    return { t: 'Assistant message', s: '' };
  }
  if (r.type === 'user') {
    const c = r.message?.content;
    if (Array.isArray(c)) { const tr = c.filter(b=>b.type==='tool_result'); if (tr.length) return { t: `Tool result (${tr.length})`, s: tr.map(t=>t.tool_use_id).join(', ') }; const tx = c.filter(b=>b.type==='text'); if (tx.length) return { t: 'User prompt', s: tx[0].text?.slice(0,80)||'' }; }
    else if (typeof c === 'string') return { t: 'User prompt', s: c.slice(0,80) };
    return { t: 'User message', s: '' };
  }
  if (r.type === 'system') { return r.subtype === 'turn_duration' ? { t: 'Turn duration', s: r.duration_ms ? `${(r.duration_ms/1000).toFixed(1)}s` : '' } : { t: `System: ${r.subtype||''}`, s: '' }; }
  if (r.type === 'progress') {
    const dt = r.data?.type; const pid = r.parentToolUseID||'';
    if (dt === 'bash_progress') return { t: 'Bash progress', s: pid };
    if (dt === 'mcp_progress') return { t: 'MCP progress', s: pid };
    if (dt === 'agent_progress') return { t: `Agent progress (${r.data?.message?.type})`, s: pid };
    return { t: `Progress: ${dt||''}`, s: pid };
  }
  return { t: r.type || 'Unknown', s: JSON.stringify(r).slice(0,60) };
}

function getVisibleRecords() {
  return processedRecords.filter(pr => {
    const t = getRecordType(pr.record);
    const ft = (t==='assistant'||t==='user'||t==='system'||t==='progress') ? t : 'unknown';
    if (!filters[ft]) return false;
    if (searchQuery && !JSON.stringify(pr.record).toLowerCase().includes(searchQuery.toLowerCase())) return false;
    return true;
  });
}

function renderRecordList() {
  const showOverlay = document.getElementById('showStateOverlay').checked;
  const visible = getVisibleRecords();
  recordList.innerHTML = '';
  for (const pr of visible) {
    const type = getRecordType(pr.record);
    const sm = summarize(pr.record);
    const item = document.createElement('div');
    item.className = `record-item${pr.index === selectedRecordIdx ? ' selected' : ''}`;
    item.dataset.index = pr.index;
    let badges = '';
    if (showOverlay && pr.events.length) {
      const sig = pr.events.filter(e => !e.type.startsWith('cancel-') && e.type !== 'clear-permission');
      if (sig.length) badges = '<div class="state-badges">' + sig.map(e => `<span class="state-badge ${evBadgeCls(e.type)}">${evLabel(e)}</span>`).join('') + '</div>';
    }
    item.innerHTML = `<span class="record-index">${pr.index}</span><span class="record-badge ${badgeCls(type)}">${type}</span><div class="record-summary"><div class="record-summary-text">${esc(sm.t)}</div>${sm.s?`<div class="record-summary-sub">${esc(sm.s)}</div>`:''}${badges}</div>`;
    item.addEventListener('click', () => selectRecord(pr.index));
    recordList.appendChild(item);
  }
}

function evBadgeCls(t) {
  return { 'tool-start':'sb-tool-start','tool-done':'sb-tool-done','turn-end':'sb-turn-end','waiting':'sb-waiting','new-turn':'sb-new-turn','permission-start':'sb-permission-start','permission-restart':'sb-permission-restart','text-idle-start':'sb-text-idle-start','active':'sb-active','cancel-waiting':'sb-cancel-waiting','cancel-permission':'sb-cancel-permission','clear-activity':'sb-clear-activity','clear-permission':'sb-cancel-permission','clear-stale-tools':'sb-clear-activity','subagent-tool-start':'sb-subagent','subagent-tool-done':'sb-subagent','subagent-clear':'sb-subagent' }[t] || '';
}

function evLabel(e) {
  switch(e.type) { case 'tool-start': return `+${e.toolName}`; case 'tool-done': return `-${e.toolName}`; case 'turn-end': return 'TURN END'; case 'waiting': return 'WAITING'; case 'new-turn': return 'NEW TURN'; case 'permission-start': return 'PERM TIMER'; case 'permission-restart': return 'PERM RESTART'; case 'text-idle-start': return 'IDLE TIMER'; case 'active': return 'ACTIVE'; case 'clear-activity': return 'CLEAR ALL'; case 'clear-stale-tools': return 'CLEAR STALE'; case 'subagent-tool-start': return `+sub:${e.toolName}`; case 'subagent-tool-done': return '-sub'; case 'subagent-clear': return 'sub clear'; default: return e.type; }
}

function evIcon(t) {
  return { 'tool-start':'🔧','tool-done':'✅','turn-end':'🏁','waiting':'⏸','new-turn':'▶','permission-start':'⏱','permission-restart':'🔄','text-idle-start':'💤','active':'⚡','cancel-waiting':'❌','cancel-permission':'❌','clear-permission':'❌','clear-activity':'🧹','clear-stale-tools':'🧹','subagent-tool-start':'🔗','subagent-tool-done':'🔗','subagent-clear':'🔗' }[t] || '•';
}

function renderTimeline() {
  timelineBar.innerHTML = '';
  for (let i = 0; i < records.length; i++) {
    const t = getRecordType(records[i]);
    const d = document.createElement('div');
    d.className = `timeline-dot td-${t==='assistant'||t==='user'||t==='system'||t==='progress'?t:'unknown'}${i===selectedRecordIdx?' selected':''}`;
    d.title = `#${i} ${t}`;
    d.addEventListener('click', () => selectRecord(i));
    timelineBar.appendChild(d);
  }
}

function selectRecord(index) {
  selectedRecordIdx = index;
  recordList.querySelectorAll('.record-item').forEach(el => el.classList.toggle('selected', parseInt(el.dataset.index) === index));
  timelineBar.querySelectorAll('.timeline-dot').forEach((d,i) => d.classList.toggle('selected', i === index));
  const item = recordList.querySelector(`.record-item[data-index="${index}"]`);
  if (item) item.scrollIntoView({ block: 'nearest' });
  renderDetailPanel();
}

// ══════════════════════════════════════════════════════════════
//  JSONL Detail View — Detail panel
// ══════════════════════════════════════════════════════════════
function renderDetailPanel() {
  if (selectedRecordIdx < 0 || selectedRecordIdx >= records.length) {
    detailContent.innerHTML = '<div class="detail-placeholder">Select a record to view details</div>';
    return;
  }
  const pr = processedRecords[selectedRecordIdx];
  if (activeTab === 'raw') { detailContent.innerHTML = `<div class="json-tree">${jsonTree(pr.record)}</div>`; setupToggles(); }
  else if (activeTab === 'state') renderStateTab(pr);
  else renderParsedTab(pr);
}

function renderParsedTab(pr) {
  const r = pr.record;
  let h = `<div class="parsed-section"><h3>Record #${pr.index}</h3>`;
  h += `<div class="parsed-field"><span class="parsed-label">Type</span><span class="parsed-value">${esc(r.type||'?')}</span></div>`;
  if (r.subtype) h += `<div class="parsed-field"><span class="parsed-label">Subtype</span><span class="parsed-value">${esc(r.subtype)}</span></div>`;
  if (r.parentToolUseID) h += `<div class="parsed-field"><span class="parsed-label">Parent Tool ID</span><span class="parsed-value" style="font-size:11px">${esc(r.parentToolUseID)}</span></div>`;
  if (r.type === 'system' && r.subtype === 'turn_duration') {
    for (const [k,v] of Object.entries(r)) { if (k==='type'||k==='subtype'||k==='message') continue; h += `<div class="parsed-field"><span class="parsed-label">${esc(k)}</span><span class="parsed-value">${esc(JSON.stringify(v))}</span></div>`; }
  }
  h += '</div>';

  if (r.type === 'assistant' && Array.isArray(r.message?.content)) {
    for (const b of r.message.content) {
      if (b.type === 'tool_use') h += `<div class="tool-block"><div class="tool-block-header"><span class="tool-name">${esc(b.name||'?')}</span><span class="tool-id">${esc(b.id||'')}</span></div><div class="tool-input">${esc(JSON.stringify(b.input||{},null,2))}</div></div>`;
      else if (b.type === 'text') h += `<div class="parsed-section"><h3>Text</h3><div class="text-content">${esc(b.text||'')}</div></div>`;
      else if (b.type === 'thinking') h += `<div class="parsed-section"><h3>Thinking</h3><div class="text-content" style="border-color:#553a88">${esc(b.thinking||'')}</div></div>`;
    }
  }
  if (r.type === 'user') {
    const c = r.message?.content;
    if (Array.isArray(c)) { for (const b of c) { if (b.type === 'tool_result') h += `<div class="tool-block"><div class="tool-block-header"><span class="tool-name" style="color:var(--green)">Tool Result</span><span class="tool-id">${esc(b.tool_use_id||'')}</span>${b.is_error?'<span style="color:var(--red);font-size:12px;font-weight:600">ERROR</span>':''}</div><div class="tool-input">${esc(typeof b.content === 'string' ? b.content : JSON.stringify(b.content,null,2))}</div></div>`; else if (b.type === 'text') h += `<div class="parsed-section"><h3>User Prompt</h3><div class="text-content">${esc(b.text||'')}</div></div>`; } }
    else if (typeof c === 'string') h += `<div class="parsed-section"><h3>User Prompt</h3><div class="text-content">${esc(c)}</div></div>`;
  }
  if (r.type === 'progress') h += `<div class="parsed-section"><h3>Progress Data</h3><div class="tool-input">${esc(JSON.stringify(r.data,null,2))}</div></div>`;

  if (pr.events.length) h += stateEventsHtml(pr);
  detailContent.innerHTML = h;
}

function renderStateTab(pr) {
  let h = '';
  h += pr.events.length ? stateEventsHtml(pr) : '<div class="state-overlay-detail"><h3>State Events</h3><p style="color:var(--text-dim);font-size:13px">No state changes</p></div>';
  h += `<div class="state-overlay-detail"><h3>State Before</h3>${stateSnap(pr.stateBefore)}</div>`;
  h += `<div class="state-overlay-detail"><h3>State After</h3>${stateSnap(pr.stateAfter)}</div>`;
  const diff = stateDiff(pr.stateBefore, pr.stateAfter);
  if (diff.length) h += `<div class="state-overlay-detail"><h3>State Diff</h3><div class="state-snapshot">${diff.map(d=>`<div class="state-field"><span class="state-field-name" style="color:var(--orange)">${esc(d.f)}</span><span>${esc(d.b)} → ${esc(d.a)}</span></div>`).join('')}</div></div>`;
  detailContent.innerHTML = h;
}

function stateEventsHtml(pr) {
  let h = `<div class="state-overlay-detail"><h3>State Events (${pr.events.length})</h3>`;
  for (const e of pr.events) h += `<div class="state-event"><span class="state-event-icon">${evIcon(e.type)}</span><div class="state-event-text"><span class="state-badge ${evBadgeCls(e.type)}" style="font-size:11px">${evLabel(e)}</span><span class="reason">${esc(e.reason)}</span></div></div>`;
  return h + '</div>';
}

function stateSnap(s) {
  let h = '<div class="state-snapshot">';
  for (const f of ['isWaiting','hadToolsInTurn','permissionSent','waitingTimerActive','permissionTimerActive']) h += `<div class="state-field"><span class="state-field-name">${f}</span><span class="${s[f]?'state-true':'state-false'}">${s[f]}</span></div>`;
  if (!s.activeToolIds.size) h += '<div class="state-field"><span class="state-field-name">activeTools</span><span class="state-set-empty">(none)</span></div>';
  else for (const id of s.activeToolIds) h += `<div class="state-field"><span class="state-field-name">tool: ${esc(s.activeToolNames.get(id)||'?')}</span><span class="state-set-items" style="font-size:11px">${esc(id)}</span></div>`;
  for (const [pid, subs] of s.activeSubagentToolIds) for (const sid of subs) h += `<div class="state-field"><span class="state-field-name">subagent: ${esc(s.activeSubagentToolNames.get(pid)?.get(sid)||'?')}</span><span class="state-set-items" style="font-size:11px">parent:${esc(pid)}</span></div>`;
  return h + '</div>';
}

function stateDiff(before, after) {
  const d = [];
  for (const f of ['isWaiting','hadToolsInTurn','permissionSent','waitingTimerActive','permissionTimerActive']) if (before[f] !== after[f]) d.push({ f, b: String(before[f]), a: String(after[f]) });
  const bt = [...before.activeToolIds].sort().join(','), at = [...after.activeToolIds].sort().join(',');
  if (bt !== at) d.push({ f: 'activeTools', b: [...before.activeToolNames.values()].join(', ')||'(none)', a: [...after.activeToolNames.values()].join(', ')||'(none)' });
  return d;
}

// ══════════════════════════════════════════════════════════════
//  JSON tree renderer
// ══════════════════════════════════════════════════════════════
function jsonTree(obj) {
  if (obj === null) return '<span class="json-null">null</span>';
  if (typeof obj === 'boolean') return `<span class="json-boolean">${obj}</span>`;
  if (typeof obj === 'number') return `<span class="json-number">${obj}</span>`;
  if (typeof obj === 'string') { const e = esc(obj); return `<span class="json-string">"${e.length>500?e.slice(0,500)+'…':e}"</span>`; }
  if (Array.isArray(obj)) {
    if (!obj.length) return '<span class="json-bracket">[]</span>';
    const id = 'j'+Math.random().toString(36).slice(2,8);
    return `<span class="json-toggle" data-target="${id}">▼</span><span class="json-bracket">[</span><div class="json-collapsible" id="${id}">${obj.map((v,i)=>`<div style="margin-left:20px">${jsonTree(v)}${i<obj.length-1?',':''}</div>`).join('')}</div><span class="json-bracket">]</span>`;
  }
  if (typeof obj === 'object') {
    const keys = Object.keys(obj);
    if (!keys.length) return '<span class="json-bracket">{}</span>';
    const id = 'j'+Math.random().toString(36).slice(2,8);
    return `<span class="json-toggle" data-target="${id}">▼</span><span class="json-bracket">{</span><div class="json-collapsible" id="${id}">${keys.map((k,i)=>`<div style="margin-left:20px"><span class="json-key">"${esc(k)}"</span>: ${jsonTree(obj[k])}${i<keys.length-1?',':''}</div>`).join('')}</div><span class="json-bracket">}</span>`;
  }
  return esc(String(obj));
}

function setupToggles() {
  detailContent.querySelectorAll('.json-toggle').forEach(t => {
    t.addEventListener('click', () => { const el = document.getElementById(t.dataset.target); if (el) { const c = el.classList.toggle('json-collapsed'); t.textContent = c ? '▶' : '▼'; } });
  });
}

// ══════════════════════════════════════════════════════════════
//  Event listeners
// ══════════════════════════════════════════════════════════════

// Detail tabs
document.querySelectorAll('.detail-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.detail-tab').forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
    activeTab = tab.dataset.tab;
    renderDetailPanel();
  });
});

// Detail filters
document.querySelectorAll('.filter-bar input[data-filter]').forEach(cb => {
  cb.addEventListener('change', () => { filters[cb.dataset.filter] = cb.checked; renderRecordList(); });
});
document.getElementById('showStateOverlay').addEventListener('change', () => renderRecordList());
searchInput.addEventListener('input', (e) => { searchQuery = e.target.value; renderRecordList(); });

// Keyboard
document.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT') return;
  if (currentView === 'detail') {
    if (e.key === 'ArrowDown' || e.key === 'j') { e.preventDefault(); const v = getVisibleRecords(); const ci = v.findIndex(p=>p.index===selectedRecordIdx); if (ci+1<v.length) selectRecord(v[ci+1].index); }
    else if (e.key === 'ArrowUp' || e.key === 'k') { e.preventDefault(); const v = getVisibleRecords(); const ci = v.findIndex(p=>p.index===selectedRecordIdx); if (ci>0) selectRecord(v[ci-1].index); }
    else if (e.key === '1') { activeTab='parsed'; document.querySelectorAll('.detail-tab').forEach(t=>t.classList.toggle('active',t.dataset.tab==='parsed')); renderDetailPanel(); }
    else if (e.key === '2') { activeTab='state'; document.querySelectorAll('.detail-tab').forEach(t=>t.classList.toggle('active',t.dataset.tab==='state')); renderDetailPanel(); }
    else if (e.key === '3') { activeTab='raw'; document.querySelectorAll('.detail-tab').forEach(t=>t.classList.toggle('active',t.dataset.tab==='raw')); renderDetailPanel(); }
    else if (e.key === 'Escape') backBtn.click();
  } else if (currentView === 'sessions') {
    if (e.key === 'ArrowDown' || e.key === 'j') { e.preventDefault(); if (selectedSessionIdx < sessions.length-1) selectSession(selectedSessionIdx+1); }
    else if (e.key === 'ArrowUp' || e.key === 'k') { e.preventDefault(); if (selectedSessionIdx > 0) selectSession(selectedSessionIdx-1); }
    else if (e.key === 'Enter' && selectedSessionIdx >= 0) openDetailForCurrentSession();
  }
});

// Resizer
let isResizing = false;
document.getElementById('resizer').addEventListener('mousedown', (e) => { isResizing = true; e.preventDefault(); });
document.addEventListener('mousemove', (e) => {
  if (!isResizing) return;
  const rect = document.querySelector('.detail-body').getBoundingClientRect();
  const w = e.clientX - rect.left;
  if (w > 200 && w < window.innerWidth - 300) recordList.style.width = w + 'px';
});
document.addEventListener('mouseup', () => { isResizing = false; });

// ══════════════════════════════════════════════════════════════
//  Helpers
// ══════════════════════════════════════════════════════════════
function esc(s) { if (typeof s !== 'string') s = String(s??''); return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'); }

function formatSize(bytes) {
  if (bytes < 1024) return bytes + ' B';
  if (bytes < 1024*1024) return (bytes/1024).toFixed(1) + ' KB';
  return (bytes/(1024*1024)).toFixed(1) + ' MB';
}

function relativeTime(ms) {
  const diff = Date.now() - ms;
  if (diff < 60000) return 'just now';
  if (diff < 3600000) return Math.floor(diff/60000) + 'min ago';
  if (diff < 86400000) return Math.floor(diff/3600000) + 'hr ago';
  if (diff < 604800000) return Math.floor(diff/86400000) + 'd ago';
  return new Date(ms).toLocaleDateString();
}
</script>
</body>
</html>
```

## File: `scripts/wall-tile-editor.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Wall Auto-Tile Editor</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: #1a1a2e; color: #e0e0e0; font-family: 'Segoe UI', system-ui, sans-serif; padding: 20px; }
    h1 { font-size: 20px; margin-bottom: 4px; }
    .subtitle { font-size: 12px; color: #888; margin-bottom: 16px; }
    h2 { font-size: 14px; color: #6ac; margin: 20px 0 8px; }

    #load-section { margin-bottom: 16px; display: flex; align-items: center; gap: 12px; }
    #load-section input[type="file"] { font-size: 12px; }
    #load-status { font-size: 11px; color: #6a6; }

    .top-row { display: flex; gap: 24px; margin-bottom: 20px; flex-wrap: wrap; }

    #source-canvas { image-rendering: pixelated; border: 1px solid #333; display: block; }

    .piece-grid { display: grid; grid-template-columns: repeat(4, auto); gap: 8px; }
    .piece-card {
      background: #222244; border: 2px solid #333; border-radius: 6px; padding: 6px;
      text-align: center;
    }
    .piece-card canvas { display: block; margin: 0 auto 4px; image-rendering: pixelated; background: #111; }
    .piece-card .pid { font-size: 9px; color: #8ac; font-family: monospace; }
    .piece-card .pdesc { font-size: 8px; color: #666; }

    #preview-wrap { display: flex; gap: 16px; align-items: flex-start; }
    #preview-canvas { image-rendering: pixelated; border: 1px solid #333; cursor: crosshair; display: block; }
    .preview-controls { display: flex; flex-direction: column; gap: 6px; }
    .preview-controls button {
      font-size: 11px; padding: 5px 12px; background: #2a2a4a; border: 1px solid #444;
      color: #e0e0e0; border-radius: 3px; cursor: pointer; text-align: left;
    }
    .preview-controls button:hover { background: #3a3a6a; }
    .preview-hint { font-size: 10px; color: #666; margin-top: 4px; line-height: 1.5; }

    .hidden { display: none !important; }
  </style>
</head>
<body>

<h1>Wall Auto-Tile Editor</h1>
<p class="subtitle">Load walls.png (64&times;128, 4&times;4 grid). Each cell is one bitmask piece (N=1, E=2, S=4, W=8). Edit the PNG externally to change wall art.</p>

<div id="load-section">
  <input type="file" id="file-input" accept="image/png">
  <span id="load-status"></span>
</div>

<div id="content" class="hidden">
  <div class="top-row">
    <div>
      <h2>Source Image (4x)</h2>
      <canvas id="source-canvas"></canvas>
    </div>
    <div>
      <h2>All 16 Pieces (4x)</h2>
      <div class="piece-grid" id="piece-grid"></div>
    </div>
  </div>

  <h2>Live Preview</h2>
  <p style="font-size:11px; color:#888; margin-bottom:8px;">Click/drag to paint walls, right-click/drag to erase. Bitmask auto-tiling applied in real-time.</p>
  <div id="preview-wrap">
    <canvas id="preview-canvas"></canvas>
    <div class="preview-controls">
      <button onclick="presetClear()">Clear All</button>
      <button onclick="presetRoom()">Room (rect)</button>
      <button onclick="presetComplex()">Complex Layout</button>
      <div class="preview-hint">
        Click/drag = paint walls<br>
        Right-click/drag = erase<br>
        All 16 masks covered
      </div>
    </div>
  </div>
</div>

<script>
const TILE = 16;
const SPRITE_H = 32;
const GRID_COLS = 4;
const PREVIEW_ZOOM = 4;
const PIECE_ZOOM = 4;
const PV_W = 14, PV_H = 10;
const WALL_COLOR = '#3A3A5C';

const MASK_LABELS = [
  'Isolated', 'N', 'E', 'N+E', 'S', 'N+S', 'E+S', 'N+E+S',
  'W', 'N+W', 'E+W', 'N+E+W', 'S+W', 'N+S+W', 'E+S+W', 'N+E+S+W',
];

let sourceImg = null;
let pieces = []; // 16 canvas elements, indexed by mask
let grid = [];
let painting = false;
let paintValue = 1;

for (let r = 0; r < PV_H; r++) grid.push(new Array(PV_W).fill(0));

// ── Image Loading ────────────────────────────────────────
document.getElementById('file-input').addEventListener('change', (e) => {
  const file = e.target.files[0];
  if (!file) return;
  const img = new Image();
  img.onload = () => {
    sourceImg = img;
    document.getElementById('load-status').textContent = `Loaded: ${img.width}×${img.height}`;
    onImageLoaded();
  };
  img.src = URL.createObjectURL(file);
});

function onImageLoaded() {
  document.getElementById('content').classList.remove('hidden');
  renderSourceImage();
  extractPieces();
  renderPieceGrid();
  presetRoom();
}

// ── Source Image ─────────────────────────────────────────
function renderSourceImage() {
  const canvas = document.getElementById('source-canvas');
  const ctx = canvas.getContext('2d');
  const z = 4;
  canvas.width = sourceImg.width * z;
  canvas.height = sourceImg.height * z;
  ctx.imageSmoothingEnabled = false;
  ctx.drawImage(sourceImg, 0, 0, canvas.width, canvas.height);

  // Grid overlay showing piece boundaries
  ctx.strokeStyle = 'rgba(100,170,200,0.4)';
  ctx.lineWidth = 1;
  for (let c = 0; c <= GRID_COLS; c++) {
    ctx.beginPath();
    ctx.moveTo(c * TILE * z + 0.5, 0);
    ctx.lineTo(c * TILE * z + 0.5, canvas.height);
    ctx.stroke();
  }
  for (let r = 0; r <= 4; r++) {
    ctx.beginPath();
    ctx.moveTo(0, r * SPRITE_H * z + 0.5);
    ctx.lineTo(canvas.width, r * SPRITE_H * z + 0.5);
    ctx.stroke();
  }

  // Mask labels
  ctx.fillStyle = '#6ac';
  ctx.font = '10px monospace';
  for (let m = 0; m < 16; m++) {
    const col = m % GRID_COLS;
    const row = Math.floor(m / GRID_COLS);
    ctx.fillText(String(m), col * TILE * z + 2, row * SPRITE_H * z + 10);
  }
}

// ── Piece Extraction ─────────────────────────────────────
function extractPieces() {
  const srcCanvas = document.createElement('canvas');
  srcCanvas.width = sourceImg.width;
  srcCanvas.height = sourceImg.height;
  const srcCtx = srcCanvas.getContext('2d');
  srcCtx.drawImage(sourceImg, 0, 0);

  pieces = [];
  for (let mask = 0; mask < 16; mask++) {
    const ox = (mask % GRID_COLS) * TILE;
    const oy = Math.floor(mask / GRID_COLS) * SPRITE_H;
    const pc = document.createElement('canvas');
    pc.width = TILE;
    pc.height = SPRITE_H;
    const ctx = pc.getContext('2d');
    ctx.drawImage(srcCanvas, ox, oy, TILE, SPRITE_H, 0, 0, TILE, SPRITE_H);
    pieces.push(pc);
  }
}

// ── Piece Grid ───────────────────────────────────────────
function renderPieceGrid() {
  const container = document.getElementById('piece-grid');
  container.innerHTML = '';
  const z = PIECE_ZOOM;

  for (let mask = 0; mask < 16; mask++) {
    const card = document.createElement('div');
    card.className = 'piece-card';

    const canvas = document.createElement('canvas');
    canvas.width = TILE * z;
    canvas.height = SPRITE_H * z;
    const ctx = canvas.getContext('2d');
    ctx.imageSmoothingEnabled = false;
    ctx.drawImage(pieces[mask], 0, 0, canvas.width, canvas.height);

    const pid = document.createElement('div');
    pid.className = 'pid';
    pid.textContent = `mask ${mask}`;

    const pdesc = document.createElement('div');
    pdesc.className = 'pdesc';
    pdesc.textContent = MASK_LABELS[mask];

    card.appendChild(canvas);
    card.appendChild(pid);
    card.appendChild(pdesc);
    container.appendChild(card);
  }
}

// ── Live Preview ─────────────────────────────────────────
function initPreview() {
  const canvas = document.getElementById('preview-canvas');
  const s = TILE * PREVIEW_ZOOM;
  canvas.width = PV_W * s;
  canvas.height = PV_H * s;

  canvas.addEventListener('mousedown', (e) => {
    e.preventDefault();
    painting = true;
    paintValue = e.button === 2 ? 0 : -1;
    handlePreviewMouse(e);
  });
  canvas.addEventListener('mousemove', (e) => { if (painting) handlePreviewMouse(e); });
  canvas.addEventListener('mouseup', () => { painting = false; });
  canvas.addEventListener('mouseleave', () => { painting = false; });
  canvas.addEventListener('contextmenu', (e) => e.preventDefault());
}

function handlePreviewMouse(e) {
  const canvas = document.getElementById('preview-canvas');
  const rect = canvas.getBoundingClientRect();
  const s = TILE * PREVIEW_ZOOM;
  const col = Math.floor((e.clientX - rect.left) / s);
  const row = Math.floor((e.clientY - rect.top) / s);
  if (col < 0 || col >= PV_W || row < 0 || row >= PV_H) return;
  if (paintValue === -1) paintValue = grid[row][col] ? 0 : 1;
  if (grid[row][col] !== paintValue) {
    grid[row][col] = paintValue;
    renderPreview();
  }
}

function renderPreview() {
  const canvas = document.getElementById('preview-canvas');
  const ctx = canvas.getContext('2d');
  const z = PREVIEW_ZOOM;
  const s = TILE * z;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.imageSmoothingEnabled = false;

  // Pass 1: base colors
  for (let r = 0; r < PV_H; r++) {
    for (let c = 0; c < PV_W; c++) {
      if (grid[r][c]) {
        ctx.fillStyle = WALL_COLOR;
      } else {
        ctx.fillStyle = (r + c) % 2 === 0 ? '#B8B4A8' : '#ACA89C';
      }
      ctx.fillRect(c * s, r * s, s, s);
    }
  }

  // Pass 2: wall sprites, row order, bottom-anchored
  for (let r = 0; r < PV_H; r++) {
    for (let c = 0; c < PV_W; c++) {
      if (!grid[r][c]) continue;
      let mask = 0;
      if (r > 0 && grid[r - 1][c]) mask |= 1;
      if (c < PV_W - 1 && grid[r][c + 1]) mask |= 2;
      if (r < PV_H - 1 && grid[r + 1][c]) mask |= 4;
      if (c > 0 && grid[r][c - 1]) mask |= 8;

      const piece = pieces[mask];
      if (!piece) continue;
      // Bottom-anchor: sprite bottom = tile bottom
      const yOff = (TILE - SPRITE_H) * z;
      ctx.drawImage(piece, 0, 0, TILE, SPRITE_H, c * s, r * s + yOff, TILE * z, SPRITE_H * z);
    }
  }

  // Grid lines
  ctx.strokeStyle = 'rgba(255,255,255,0.08)';
  ctx.lineWidth = 1;
  for (let c = 0; c <= PV_W; c++) {
    ctx.beginPath(); ctx.moveTo(c * s + 0.5, 0); ctx.lineTo(c * s + 0.5, PV_H * s); ctx.stroke();
  }
  for (let r = 0; r <= PV_H; r++) {
    ctx.beginPath(); ctx.moveTo(0, r * s + 0.5); ctx.lineTo(PV_W * s, r * s + 0.5); ctx.stroke();
  }
}

// ── Presets ──────────────────────────────────────────────
function presetClear() {
  for (let r = 0; r < PV_H; r++) for (let c = 0; c < PV_W; c++) grid[r][c] = 0;
  renderPreview();
}

function presetRoom() {
  presetClear();
  for (let c = 2; c <= 11; c++) { grid[1][c] = 1; grid[8][c] = 1; }
  for (let r = 1; r <= 8; r++) { grid[r][2] = 1; grid[r][11] = 1; }
  renderPreview();
}

function presetComplex() {
  presetClear();
  for (let c = 1; c <= 12; c++) { grid[1][c] = 1; grid[8][c] = 1; }
  for (let r = 1; r <= 8; r++) { grid[r][1] = 1; grid[r][12] = 1; }
  for (let r = 1; r <= 5; r++) grid[r][7] = 1;
  for (let c = 7; c <= 12; c++) grid[5][c] = 1;
  for (let c = 3; c <= 5; c++) grid[5][c] = 1;
  grid[5][1] = 1;
  renderPreview();
}

initPreview();
</script>
</body>
</html>
```

## File: `src/agentManager.ts`
```typescript
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import * as vscode from 'vscode';

import {
  JSONL_POLL_INTERVAL_MS,
  TERMINAL_NAME_PREFIX,
  WORKSPACE_KEY_AGENT_SEATS,
  WORKSPACE_KEY_AGENTS,
} from './constants.js';
import { ensureProjectScan, readNewLines, startFileWatching } from './fileWatcher.js';
import { migrateAndLoadLayout } from './layoutPersistence.js';
import { cancelPermissionTimer, cancelWaitingTimer } from './timerManager.js';
import type { AgentState, PersistedAgent } from './types.js';

export function getProjectDirPath(cwd?: string): string | null {
  const workspacePath = cwd || vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
  if (!workspacePath) return null;
  const dirName = workspacePath.replace(/[^a-zA-Z0-9-]/g, '-');
  const projectDir = path.join(os.homedir(), '.claude', 'projects', dirName);
  console.log(`[Pixel Agents] Project dir: ${workspacePath} → ${dirName}`);
  return projectDir;
}

export async function launchNewTerminal(
  nextAgentIdRef: { current: number },
  nextTerminalIndexRef: { current: number },
  agents: Map<number, AgentState>,
  activeAgentIdRef: { current: number | null },
  knownJsonlFiles: Set<string>,
  fileWatchers: Map<number, fs.FSWatcher>,
  pollingTimers: Map<number, ReturnType<typeof setInterval>>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  jsonlPollTimers: Map<number, ReturnType<typeof setInterval>>,
  projectScanTimerRef: { current: ReturnType<typeof setInterval> | null },
  webview: vscode.Webview | undefined,
  persistAgents: () => void,
  folderPath?: string,
): Promise<void> {
  const folders = vscode.workspace.workspaceFolders;
  const cwd = folderPath || folders?.[0]?.uri.fsPath;
  const isMultiRoot = !!(folders && folders.length > 1);
  const idx = nextTerminalIndexRef.current++;
  const terminal = vscode.window.createTerminal({
    name: `${TERMINAL_NAME_PREFIX} #${idx}`,
    cwd,
  });
  terminal.show();

  const sessionId = crypto.randomUUID();
  terminal.sendText(`claude --session-id ${sessionId}`);

  const projectDir = getProjectDirPath(cwd);
  if (!projectDir) {
    console.log(`[Pixel Agents] No project dir, cannot track agent`);
    return;
  }

  // Pre-register expected JSONL file so project scan won't treat it as a /clear file
  const expectedFile = path.join(projectDir, `${sessionId}.jsonl`);
  knownJsonlFiles.add(expectedFile);

  // Create agent immediately (before JSONL file exists)
  const id = nextAgentIdRef.current++;
  const folderName = isMultiRoot && cwd ? path.basename(cwd) : undefined;
  const agent: AgentState = {
    id,
    terminalRef: terminal,
    projectDir,
    jsonlFile: expectedFile,
    fileOffset: 0,
    lineBuffer: '',
    activeToolIds: new Set(),
    activeToolStatuses: new Map(),
    activeToolNames: new Map(),
    activeSubagentToolIds: new Map(),
    activeSubagentToolNames: new Map(),
    isWaiting: false,
    permissionSent: false,
    hadToolsInTurn: false,
    folderName,
  };

  agents.set(id, agent);
  activeAgentIdRef.current = id;
  persistAgents();
  console.log(`[Pixel Agents] Agent ${id}: created for terminal ${terminal.name}`);
  webview?.postMessage({ type: 'agentCreated', id, folderName });

  ensureProjectScan(
    projectDir,
    knownJsonlFiles,
    projectScanTimerRef,
    activeAgentIdRef,
    nextAgentIdRef,
    agents,
    fileWatchers,
    pollingTimers,
    waitingTimers,
    permissionTimers,
    webview,
    persistAgents,
  );

  // Poll for the specific JSONL file to appear
  const pollTimer = setInterval(() => {
    try {
      if (fs.existsSync(agent.jsonlFile)) {
        console.log(
          `[Pixel Agents] Agent ${id}: found JSONL file ${path.basename(agent.jsonlFile)}`,
        );
        clearInterval(pollTimer);
        jsonlPollTimers.delete(id);
        startFileWatching(
          id,
          agent.jsonlFile,
          agents,
          fileWatchers,
          pollingTimers,
          waitingTimers,
          permissionTimers,
          webview,
        );
        readNewLines(id, agents, waitingTimers, permissionTimers, webview);
      }
    } catch {
      /* file may not exist yet */
    }
  }, JSONL_POLL_INTERVAL_MS);
  jsonlPollTimers.set(id, pollTimer);
}

export function removeAgent(
  agentId: number,
  agents: Map<number, AgentState>,
  fileWatchers: Map<number, fs.FSWatcher>,
  pollingTimers: Map<number, ReturnType<typeof setInterval>>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  jsonlPollTimers: Map<number, ReturnType<typeof setInterval>>,
  persistAgents: () => void,
): void {
  const agent = agents.get(agentId);
  if (!agent) return;

  // Stop JSONL poll timer
  const jpTimer = jsonlPollTimers.get(agentId);
  if (jpTimer) {
    clearInterval(jpTimer);
  }
  jsonlPollTimers.delete(agentId);

  // Stop file watching
  fileWatchers.get(agentId)?.close();
  fileWatchers.delete(agentId);
  const pt = pollingTimers.get(agentId);
  if (pt) {
    clearInterval(pt);
  }
  pollingTimers.delete(agentId);
  try {
    fs.unwatchFile(agent.jsonlFile);
  } catch {
    /* ignore */
  }

  // Cancel timers
  cancelWaitingTimer(agentId, waitingTimers);
  cancelPermissionTimer(agentId, permissionTimers);

  // Remove from maps
  agents.delete(agentId);
  persistAgents();
}

export function persistAgents(
  agents: Map<number, AgentState>,
  context: vscode.ExtensionContext,
): void {
  const persisted: PersistedAgent[] = [];
  for (const agent of agents.values()) {
    persisted.push({
      id: agent.id,
      terminalName: agent.terminalRef.name,
      jsonlFile: agent.jsonlFile,
      projectDir: agent.projectDir,
      folderName: agent.folderName,
    });
  }
  context.workspaceState.update(WORKSPACE_KEY_AGENTS, persisted);
}

export function restoreAgents(
  context: vscode.ExtensionContext,
  nextAgentIdRef: { current: number },
  nextTerminalIndexRef: { current: number },
  agents: Map<number, AgentState>,
  knownJsonlFiles: Set<string>,
  fileWatchers: Map<number, fs.FSWatcher>,
  pollingTimers: Map<number, ReturnType<typeof setInterval>>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  jsonlPollTimers: Map<number, ReturnType<typeof setInterval>>,
  projectScanTimerRef: { current: ReturnType<typeof setInterval> | null },
  activeAgentIdRef: { current: number | null },
  webview: vscode.Webview | undefined,
  doPersist: () => void,
): void {
  const persisted = context.workspaceState.get<PersistedAgent[]>(WORKSPACE_KEY_AGENTS, []);
  if (persisted.length === 0) return;

  const liveTerminals = vscode.window.terminals;
  let maxId = 0;
  let maxIdx = 0;
  let restoredProjectDir: string | null = null;

  for (const p of persisted) {
    const terminal = liveTerminals.find((t) => t.name === p.terminalName);
    if (!terminal) continue;

    const agent: AgentState = {
      id: p.id,
      terminalRef: terminal,
      projectDir: p.projectDir,
      jsonlFile: p.jsonlFile,
      fileOffset: 0,
      lineBuffer: '',
      activeToolIds: new Set(),
      activeToolStatuses: new Map(),
      activeToolNames: new Map(),
      activeSubagentToolIds: new Map(),
      activeSubagentToolNames: new Map(),
      isWaiting: false,
      permissionSent: false,
      hadToolsInTurn: false,
      folderName: p.folderName,
    };

    agents.set(p.id, agent);
    knownJsonlFiles.add(p.jsonlFile);
    console.log(`[Pixel Agents] Restored agent ${p.id} → terminal "${p.terminalName}"`);

    if (p.id > maxId) maxId = p.id;
    // Extract terminal index from name like "Claude Code #3"
    const match = p.terminalName.match(/#(\d+)$/);
    if (match) {
      const idx = parseInt(match[1], 10);
      if (idx > maxIdx) maxIdx = idx;
    }

    restoredProjectDir = p.projectDir;

    // Start file watching if JSONL exists, skipping to end of file
    try {
      if (fs.existsSync(p.jsonlFile)) {
        const stat = fs.statSync(p.jsonlFile);
        agent.fileOffset = stat.size;
        startFileWatching(
          p.id,
          p.jsonlFile,
          agents,
          fileWatchers,
          pollingTimers,
          waitingTimers,
          permissionTimers,
          webview,
        );
      } else {
        // Poll for the file to appear
        const pollTimer = setInterval(() => {
          try {
            if (fs.existsSync(agent.jsonlFile)) {
              console.log(`[Pixel Agents] Restored agent ${p.id}: found JSONL file`);
              clearInterval(pollTimer);
              jsonlPollTimers.delete(p.id);
              const stat = fs.statSync(agent.jsonlFile);
              agent.fileOffset = stat.size;
              startFileWatching(
                p.id,
                agent.jsonlFile,
                agents,
                fileWatchers,
                pollingTimers,
                waitingTimers,
                permissionTimers,
                webview,
              );
            }
          } catch {
            /* file may not exist yet */
          }
        }, JSONL_POLL_INTERVAL_MS);
        jsonlPollTimers.set(p.id, pollTimer);
      }
    } catch {
      /* ignore errors during restore */
    }
  }

  // Advance counters past restored IDs
  if (maxId >= nextAgentIdRef.current) {
    nextAgentIdRef.current = maxId + 1;
  }
  if (maxIdx >= nextTerminalIndexRef.current) {
    nextTerminalIndexRef.current = maxIdx + 1;
  }

  // Re-persist cleaned-up list (removes entries whose terminals are gone)
  doPersist();

  // Start project scan for /clear detection
  if (restoredProjectDir) {
    ensureProjectScan(
      restoredProjectDir,
      knownJsonlFiles,
      projectScanTimerRef,
      activeAgentIdRef,
      nextAgentIdRef,
      agents,
      fileWatchers,
      pollingTimers,
      waitingTimers,
      permissionTimers,
      webview,
      doPersist,
    );
  }
}

export function sendExistingAgents(
  agents: Map<number, AgentState>,
  context: vscode.ExtensionContext,
  webview: vscode.Webview | undefined,
): void {
  if (!webview) return;
  const agentIds: number[] = [];
  for (const id of agents.keys()) {
    agentIds.push(id);
  }
  agentIds.sort((a, b) => a - b);

  // Include persisted palette/seatId from separate key
  const agentMeta = context.workspaceState.get<
    Record<string, { palette?: number; seatId?: string }>
  >(WORKSPACE_KEY_AGENT_SEATS, {});

  // Include folderName per agent
  const folderNames: Record<number, string> = {};
  for (const [id, agent] of agents) {
    if (agent.folderName) {
      folderNames[id] = agent.folderName;
    }
  }
  console.log(
    `[Pixel Agents] sendExistingAgents: agents=${JSON.stringify(agentIds)}, meta=${JSON.stringify(agentMeta)}`,
  );

  webview.postMessage({
    type: 'existingAgents',
    agents: agentIds,
    agentMeta,
    folderNames,
  });

  sendCurrentAgentStatuses(agents, webview);
}

export function sendCurrentAgentStatuses(
  agents: Map<number, AgentState>,
  webview: vscode.Webview | undefined,
): void {
  if (!webview) return;
  for (const [agentId, agent] of agents) {
    // Re-send active tools
    for (const [toolId, status] of agent.activeToolStatuses) {
      webview.postMessage({
        type: 'agentToolStart',
        id: agentId,
        toolId,
        status,
      });
    }
    // Re-send waiting status
    if (agent.isWaiting) {
      webview.postMessage({
        type: 'agentStatus',
        id: agentId,
        status: 'waiting',
      });
    }
  }
}

export function sendLayout(
  context: vscode.ExtensionContext,
  webview: vscode.Webview | undefined,
  defaultLayout?: Record<string, unknown> | null,
): void {
  if (!webview) return;
  const result = migrateAndLoadLayout(context, defaultLayout);
  webview.postMessage({
    type: 'layoutLoaded',
    layout: result?.layout ?? null,
    wasReset: result?.wasReset ?? false,
  });
}
```

## File: `src/assetLoader.ts`
```typescript
/**
 * Asset Loader - Loads furniture assets from per-folder manifests
 *
 * Scans assets/furniture/ subdirectories, reads each manifest.json,
 * and loads all PNG files into SpriteData format for use in the webview.
 */

import * as fs from 'fs';
import * as path from 'path';
import { PNG } from 'pngjs';
import * as vscode from 'vscode';

import {
  CHAR_COUNT,
  CHAR_FRAME_H,
  CHAR_FRAME_W,
  CHAR_FRAMES_PER_ROW,
  CHARACTER_DIRECTIONS,
  FLOOR_TILE_SIZE,
  LAYOUT_REVISION_KEY,
  PNG_ALPHA_THRESHOLD,
  WALL_BITMASK_COUNT,
  WALL_GRID_COLS,
  WALL_PIECE_HEIGHT,
  WALL_PIECE_WIDTH,
} from './constants.js';

export interface FurnitureAsset {
  id: string;
  name: string;
  label: string;
  category: string;
  file: string;
  width: number;
  height: number;
  footprintW: number;
  footprintH: number;
  isDesk: boolean;
  canPlaceOnWalls: boolean;
  groupId?: string;
  canPlaceOnSurfaces?: boolean;
  backgroundTiles?: number;
  orientation?: string;
  state?: string;
  mirrorSide?: boolean;
  rotationScheme?: string;
  animationGroup?: string;
  frame?: number;
}

export interface LoadedAssets {
  catalog: FurnitureAsset[];
  sprites: Map<string, string[][]>; // assetId -> SpriteData
}

// ── Manifest types ──────────────────────────────────────────

interface ManifestAsset {
  type: 'asset';
  id: string;
  file: string;
  width: number;
  height: number;
  footprintW: number;
  footprintH: number;
  orientation?: string;
  state?: string;
  frame?: number;
  mirrorSide?: boolean;
}

interface ManifestGroup {
  type: 'group';
  groupType: 'rotation' | 'state' | 'animation';
  rotationScheme?: string;
  orientation?: string;
  state?: string;
  members: ManifestNode[];
}

type ManifestNode = ManifestAsset | ManifestGroup;

interface FurnitureManifest {
  id: string;
  name: string;
  category: string;
  canPlaceOnWalls: boolean;
  canPlaceOnSurfaces: boolean;
  backgroundTiles: number;
  // If type is 'asset', these fields are present:
  type: 'asset' | 'group';
  file?: string;
  width?: number;
  height?: number;
  footprintW?: number;
  footprintH?: number;
  // If type is 'group':
  groupType?: string;
  rotationScheme?: string;
  members?: ManifestNode[];
}

interface InheritedProps {
  groupId: string;
  name: string;
  category: string;
  canPlaceOnWalls: boolean;
  canPlaceOnSurfaces: boolean;
  backgroundTiles: number;
  orientation?: string;
  state?: string;
  rotationScheme?: string;
  animationGroup?: string;
}

/**
 * Recursively flatten a manifest node into FurnitureAsset[].
 * Inherited properties flow from root to all leaf assets.
 */
function flattenManifest(node: ManifestNode, inherited: InheritedProps): FurnitureAsset[] {
  if (node.type === 'asset') {
    const asset = node as ManifestAsset;
    // Merge orientation: node-level takes priority, then inherited
    const orientation = asset.orientation ?? inherited.orientation;
    const state = asset.state ?? inherited.state;
    return [
      {
        id: asset.id,
        name: inherited.name,
        label: inherited.name,
        category: inherited.category,
        file: asset.file,
        width: asset.width,
        height: asset.height,
        footprintW: asset.footprintW,
        footprintH: asset.footprintH,
        isDesk: inherited.category === 'desks',
        canPlaceOnWalls: inherited.canPlaceOnWalls,
        canPlaceOnSurfaces: inherited.canPlaceOnSurfaces,
        backgroundTiles: inherited.backgroundTiles,
        groupId: inherited.groupId,
        ...(orientation ? { orientation } : {}),
        ...(state ? { state } : {}),
        ...(asset.mirrorSide ? { mirrorSide: true } : {}),
        ...(inherited.rotationScheme ? { rotationScheme: inherited.rotationScheme } : {}),
        ...(inherited.animationGroup ? { animationGroup: inherited.animationGroup } : {}),
        ...(asset.frame !== undefined ? { frame: asset.frame } : {}),
      },
    ];
  }

  // Group node
  const group = node as ManifestGroup;
  const results: FurnitureAsset[] = [];

  for (const member of group.members) {
    // Build inherited props for children
    const childProps: InheritedProps = { ...inherited };

    if (group.groupType === 'rotation') {
      // Rotation groups set groupId and pass rotationScheme
      if (group.rotationScheme) {
        childProps.rotationScheme = group.rotationScheme;
      }
    }

    if (group.groupType === 'state') {
      // State groups propagate orientation from the group level
      if (group.orientation) {
        childProps.orientation = group.orientation;
      }
      // Propagate state from group level if set (for animation groups nested in state)
      if (group.state) {
        childProps.state = group.state;
      }
    }

    if (group.groupType === 'animation') {
      // Animation groups: create animation group ID and propagate state
      // Use the parent's orientation to build a unique animation group name
      const orient = group.orientation ?? inherited.orientation ?? '';
      const state = group.state ?? inherited.state ?? '';
      childProps.animationGroup = `${inherited.groupId}_${orient}_${state}`.toUpperCase();
      if (group.state) {
        childProps.state = group.state;
      }
    }

    // Propagate orientation from group to children (for state groups that have orientation)
    if (group.orientation && !childProps.orientation) {
      childProps.orientation = group.orientation;
    }

    results.push(...flattenManifest(member, childProps));
  }

  return results;
}

/**
 * Load furniture assets from per-folder manifests
 */
export async function loadFurnitureAssets(workspaceRoot: string): Promise<LoadedAssets | null> {
  try {
    console.log(`[AssetLoader] workspaceRoot received: "${workspaceRoot}"`);
    const furnitureDir = path.join(workspaceRoot, 'assets', 'furniture');
    console.log(`[AssetLoader] Scanning furniture directory: ${furnitureDir}`);

    if (!fs.existsSync(furnitureDir)) {
      console.log('ℹ️  No furniture directory found at:', furnitureDir);
      return null;
    }

    const entries = fs.readdirSync(furnitureDir, { withFileTypes: true });
    const dirs = entries.filter((e) => e.isDirectory());

    if (dirs.length === 0) {
      console.log('ℹ️  No furniture subdirectories found');
      return null;
    }

    console.log(`📦 Found ${dirs.length} furniture folders`);

    const catalog: FurnitureAsset[] = [];
    const sprites = new Map<string, string[][]>();

    for (const dir of dirs) {
      const itemDir = path.join(furnitureDir, dir.name);
      const manifestPath = path.join(itemDir, 'manifest.json');

      if (!fs.existsSync(manifestPath)) {
        console.warn(`  ⚠️  No manifest.json in ${dir.name}`);
        continue;
      }

      try {
        const manifestContent = fs.readFileSync(manifestPath, 'utf-8');
        const manifest = JSON.parse(manifestContent) as FurnitureManifest;

        // Build the inherited props from the root manifest
        const inherited: InheritedProps = {
          groupId: manifest.id,
          name: manifest.name,
          category: manifest.category,
          canPlaceOnWalls: manifest.canPlaceOnWalls,
          canPlaceOnSurfaces: manifest.canPlaceOnSurfaces,
          backgroundTiles: manifest.backgroundTiles,
        };

        let assets: FurnitureAsset[];

        if (manifest.type === 'asset') {
          // Single asset manifest (no groups) — file defaults to {id}.png
          assets = [
            {
              id: manifest.id,
              name: manifest.name,
              label: manifest.name,
              category: manifest.category,
              file: manifest.file ?? `${manifest.id}.png`,
              width: manifest.width!,
              height: manifest.height!,
              footprintW: manifest.footprintW!,
              footprintH: manifest.footprintH!,
              isDesk: manifest.category === 'desks',
              canPlaceOnWalls: manifest.canPlaceOnWalls,
              canPlaceOnSurfaces: manifest.canPlaceOnSurfaces,
              backgroundTiles: manifest.backgroundTiles,
              groupId: manifest.id,
            },
          ];
        } else {
          // Group manifest — flatten recursively
          if (manifest.rotationScheme) {
            inherited.rotationScheme = manifest.rotationScheme;
          }
          const rootGroup: ManifestGroup = {
            type: 'group',
            groupType: manifest.groupType as 'rotation' | 'state' | 'animation',
            rotationScheme: manifest.rotationScheme,
            members: manifest.members!,
          };
          assets = flattenManifest(rootGroup, inherited);
        }

        // Load PNGs for each asset
        for (const asset of assets) {
          try {
            const assetPath = path.join(itemDir, asset.file);
            if (!fs.existsSync(assetPath)) {
              console.warn(`  ⚠️  Asset file not found: ${asset.file} in ${dir.name}`);
              continue;
            }

            const pngBuffer = fs.readFileSync(assetPath);
            const spriteData = pngToSpriteData(pngBuffer, asset.width, asset.height);
            sprites.set(asset.id, spriteData);
          } catch (err) {
            console.warn(
              `  ⚠️  Error loading ${asset.id}: ${err instanceof Error ? err.message : err}`,
            );
          }
        }

        catalog.push(...assets);
      } catch (err) {
        console.warn(
          `  ⚠️  Error processing ${dir.name}: ${err instanceof Error ? err.message : err}`,
        );
      }
    }

    console.log(`  ✓ Loaded ${sprites.size} / ${catalog.length} assets`);
    console.log(`[AssetLoader] ✅ Successfully loaded ${sprites.size} furniture sprites`);

    return { catalog, sprites };
  } catch (err) {
    console.error(
      `[AssetLoader] ❌ Error loading furniture assets: ${err instanceof Error ? err.message : err}`,
    );
    return null;
  }
}

/**
 * Convert PNG buffer to SpriteData (2D array of hex color strings)
 *
 * PNG format: RGBA
 * SpriteData format: string[][] where '' = transparent, '#RRGGBB' = opaque, '#RRGGBBAA' = semi-transparent
 */
function rgbaToHex(r: number, g: number, b: number, a: number): string {
  if (a < PNG_ALPHA_THRESHOLD) return '';
  const rgb =
    `#${r.toString(16).padStart(2, '0')}${g.toString(16).padStart(2, '0')}${b.toString(16).padStart(2, '0')}`.toUpperCase();
  if (a >= 255) return rgb;
  return `${rgb}${a.toString(16).padStart(2, '0').toUpperCase()}`;
}

function pngToSpriteData(pngBuffer: Buffer, width: number, height: number): string[][] {
  try {
    // Parse PNG using pngjs
    const png = PNG.sync.read(pngBuffer);

    if (png.width !== width || png.height !== height) {
      console.warn(
        `PNG dimensions mismatch: expected ${width}×${height}, got ${png.width}×${png.height}`,
      );
    }

    const sprite: string[][] = [];
    const data = png.data; // Uint8Array with RGBA values

    for (let y = 0; y < height; y++) {
      const row: string[] = [];
      for (let x = 0; x < width; x++) {
        const pixelIndex = (y * png.width + x) * 4;

        const r = data[pixelIndex];
        const g = data[pixelIndex + 1];
        const b = data[pixelIndex + 2];
        const a = data[pixelIndex + 3];

        row.push(rgbaToHex(r, g, b, a));
      }
      sprite.push(row);
    }

    return sprite;
  } catch (err) {
    console.warn(`Failed to parse PNG: ${err instanceof Error ? err.message : err}`);
    // Return transparent placeholder
    const sprite: string[][] = [];
    for (let y = 0; y < height; y++) {
      sprite.push(new Array(width).fill(''));
    }
    return sprite;
  }
}

// ── Default layout loading ───────────────────────────────────

/**
 * Load the bundled default layout with the highest revision.
 * Scans for assets/default-layout-{N}.json files and picks the one
 * with the largest N. Falls back to assets/default-layout.json for
 * backward compatibility.
 */
export function loadDefaultLayout(assetsRoot: string): Record<string, unknown> | null {
  const assetsDir = path.join(assetsRoot, 'assets');
  try {
    // Scan for versioned default layouts: default-layout-{N}.json
    let bestRevision = 0;
    let bestPath: string | null = null;

    if (fs.existsSync(assetsDir)) {
      for (const file of fs.readdirSync(assetsDir)) {
        const match = /^default-layout-(\d+)\.json$/.exec(file);
        if (match) {
          const rev = parseInt(match[1], 10);
          if (rev > bestRevision) {
            bestRevision = rev;
            bestPath = path.join(assetsDir, file);
          }
        }
      }
    }

    // Fall back to unversioned default-layout.json
    if (!bestPath) {
      const fallback = path.join(assetsDir, 'default-layout.json');
      if (fs.existsSync(fallback)) {
        bestPath = fallback;
      }
    }

    if (!bestPath) {
      console.log('[AssetLoader] No default layout found in:', assetsDir);
      return null;
    }

    const content = fs.readFileSync(bestPath, 'utf-8');
    const layout = JSON.parse(content) as Record<string, unknown>;
    // Ensure layoutRevision matches the file's revision number
    if (bestRevision > 0 && !layout[LAYOUT_REVISION_KEY]) {
      layout[LAYOUT_REVISION_KEY] = bestRevision;
    }
    console.log(
      `[AssetLoader] Loaded default layout (${layout.cols}×${layout.rows}, revision ${layout[LAYOUT_REVISION_KEY] ?? 0}) from ${path.basename(bestPath)}`,
    );
    return layout;
  } catch (err) {
    console.error(
      `[AssetLoader] Error loading default layout: ${err instanceof Error ? err.message : err}`,
    );
    return null;
  }
}

// ── Wall tile loading ────────────────────────────────────────

export interface LoadedWallTiles {
  /** Array of wall sets, each containing 16 sprites indexed by bitmask (N=1,E=2,S=4,W=8) */
  sets: string[][][][];
}

/**
 * Parse a single wall PNG (64×128, 4×4 grid of 16×32 pieces) into 16 bitmask sprites.
 * Piece at bitmask M: col = M % 4, row = floor(M / 4).
 */
function parseWallPng(pngBuffer: Buffer): string[][][] {
  const png = PNG.sync.read(pngBuffer);
  const sprites: string[][][] = [];
  for (let mask = 0; mask < WALL_BITMASK_COUNT; mask++) {
    const ox = (mask % WALL_GRID_COLS) * WALL_PIECE_WIDTH;
    const oy = Math.floor(mask / WALL_GRID_COLS) * WALL_PIECE_HEIGHT;
    const sprite: string[][] = [];
    for (let r = 0; r < WALL_PIECE_HEIGHT; r++) {
      const row: string[] = [];
      for (let c = 0; c < WALL_PIECE_WIDTH; c++) {
        const idx = ((oy + r) * png.width + (ox + c)) * 4;
        const rv = png.data[idx];
        const gv = png.data[idx + 1];
        const bv = png.data[idx + 2];
        const av = png.data[idx + 3];
        row.push(rgbaToHex(rv, gv, bv, av));
      }
      sprite.push(row);
    }
    sprites.push(sprite);
  }
  return sprites;
}

/**
 * Load wall tile sets from assets/walls/ folder.
 * Each file is named wall_N.png (e.g. wall_0.png, wall_1.png, ...).
 * Files are loaded in numeric order; each PNG is a 64×128 grid of 16 bitmask pieces.
 */
export async function loadWallTiles(assetsRoot: string): Promise<LoadedWallTiles | null> {
  try {
    const wallsDir = path.join(assetsRoot, 'assets', 'walls');
    if (!fs.existsSync(wallsDir)) {
      console.log('[AssetLoader] No walls/ directory found at:', wallsDir);
      return null;
    }

    console.log('[AssetLoader] Loading wall tiles from:', wallsDir);

    // Find all wall_N.png files and sort by index
    const entries = fs.readdirSync(wallsDir);
    const wallFiles: { index: number; filename: string }[] = [];
    for (const entry of entries) {
      const match = /^wall_(\d+)\.png$/i.exec(entry);
      if (match) {
        wallFiles.push({ index: parseInt(match[1], 10), filename: entry });
      }
    }

    if (wallFiles.length === 0) {
      console.log('[AssetLoader] No wall_N.png files found in walls/');
      return null;
    }

    wallFiles.sort((a, b) => a.index - b.index);

    const sets: string[][][][] = [];
    for (const { filename } of wallFiles) {
      const filePath = path.join(wallsDir, filename);
      const pngBuffer = fs.readFileSync(filePath);
      const sprites = parseWallPng(pngBuffer);
      sets.push(sprites);
    }

    console.log(
      `[AssetLoader] ✅ Loaded ${sets.length} wall tile set(s) (${sets.length * WALL_BITMASK_COUNT} pieces total)`,
    );
    return { sets };
  } catch (err) {
    console.error(
      `[AssetLoader] ❌ Error loading wall tiles: ${err instanceof Error ? err.message : err}`,
    );
    return null;
  }
}

/**
 * Send wall tiles to webview
 */
export function sendWallTilesToWebview(webview: vscode.Webview, wallTiles: LoadedWallTiles): void {
  webview.postMessage({
    type: 'wallTilesLoaded',
    sets: wallTiles.sets,
  });
  console.log(`📤 Sent ${wallTiles.sets.length} wall tile set(s) to webview`);
}

export interface LoadedFloorTiles {
  sprites: string[][][]; // N sprites (one per floor_N.png), each 16x16 SpriteData
}

/**
 * Load floor tile patterns from assets/floors/ folder.
 * Each file is named floor_N.png (e.g. floor_0.png, floor_1.png, ...).
 * Files are loaded in numeric order; each PNG is a 16×16 grayscale tile.
 */
export async function loadFloorTiles(assetsRoot: string): Promise<LoadedFloorTiles | null> {
  try {
    const floorsDir = path.join(assetsRoot, 'assets', 'floors');
    if (!fs.existsSync(floorsDir)) {
      console.log('[AssetLoader] No floors/ directory found at:', floorsDir);
      return null;
    }

    console.log('[AssetLoader] Loading floor tiles from:', floorsDir);

    // Find all floor_N.png files and sort by index
    const entries = fs.readdirSync(floorsDir);
    const floorFiles: { index: number; filename: string }[] = [];
    for (const entry of entries) {
      const match = /^floor_(\d+)\.png$/i.exec(entry);
      if (match) {
        floorFiles.push({ index: parseInt(match[1], 10), filename: entry });
      }
    }

    if (floorFiles.length === 0) {
      console.log('[AssetLoader] No floor_N.png files found in floors/');
      return null;
    }

    floorFiles.sort((a, b) => a.index - b.index);

    const sprites: string[][][] = [];
    for (const { filename } of floorFiles) {
      const filePath = path.join(floorsDir, filename);
      const pngBuffer = fs.readFileSync(filePath);
      const sprite = pngToSpriteData(pngBuffer, FLOOR_TILE_SIZE, FLOOR_TILE_SIZE);
      sprites.push(sprite);
    }

    console.log(`[AssetLoader] ✅ Loaded ${sprites.length} floor tile patterns from floors/`);
    return { sprites };
  } catch (err) {
    console.error(
      `[AssetLoader] ❌ Error loading floor tiles: ${err instanceof Error ? err.message : err}`,
    );
    return null;
  }
}

/**
 * Send floor tiles to webview
 */
export function sendFloorTilesToWebview(
  webview: vscode.Webview,
  floorTiles: LoadedFloorTiles,
): void {
  webview.postMessage({
    type: 'floorTilesLoaded',
    sprites: floorTiles.sprites,
  });
  console.log(`📤 Sent ${floorTiles.sprites.length} floor tile patterns to webview`);
}

// ── Character sprite loading ────────────────────────────────

export interface CharacterDirectionSprites {
  down: string[][][];
  up: string[][][];
  right: string[][][];
}

export interface LoadedCharacterSprites {
  /** 6 pre-colored characters, each with 9 frames per direction */
  characters: CharacterDirectionSprites[];
}

/**
 * Load pre-colored character sprites from assets/characters/ (6 PNGs, each 112×96).
 * Each PNG has 3 direction rows (down, up, right) × 7 frames (16×32 each).
 */
export async function loadCharacterSprites(
  assetsRoot: string,
): Promise<LoadedCharacterSprites | null> {
  try {
    const charDir = path.join(assetsRoot, 'assets', 'characters');
    const characters: CharacterDirectionSprites[] = [];

    for (let ci = 0; ci < CHAR_COUNT; ci++) {
      const filePath = path.join(charDir, `char_${ci}.png`);
      if (!fs.existsSync(filePath)) {
        console.log(`[AssetLoader] No character sprite found at: ${filePath}`);
        return null;
      }

      const pngBuffer = fs.readFileSync(filePath);
      const png = PNG.sync.read(pngBuffer);

      const directions = CHARACTER_DIRECTIONS;
      const charData: CharacterDirectionSprites = { down: [], up: [], right: [] };

      for (let dirIdx = 0; dirIdx < directions.length; dirIdx++) {
        const dir = directions[dirIdx];
        const rowOffsetY = dirIdx * CHAR_FRAME_H;
        const frames: string[][][] = [];

        for (let f = 0; f < CHAR_FRAMES_PER_ROW; f++) {
          const sprite: string[][] = [];
          const frameOffsetX = f * CHAR_FRAME_W;
          for (let y = 0; y < CHAR_FRAME_H; y++) {
            const row: string[] = [];
            for (let x = 0; x < CHAR_FRAME_W; x++) {
              const idx = ((rowOffsetY + y) * png.width + (frameOffsetX + x)) * 4;
              const r = png.data[idx];
              const g = png.data[idx + 1];
              const b = png.data[idx + 2];
              const a = png.data[idx + 3];
              row.push(rgbaToHex(r, g, b, a));
            }
            sprite.push(row);
          }
          frames.push(sprite);
        }
        charData[dir] = frames;
      }
      characters.push(charData);
    }

    console.log(
      `[AssetLoader] ✅ Loaded ${characters.length} character sprites (${CHAR_FRAMES_PER_ROW} frames × 3 directions each)`,
    );
    return { characters };
  } catch (err) {
    console.error(
      `[AssetLoader] ❌ Error loading character sprites: ${err instanceof Error ? err.message : err}`,
    );
    return null;
  }
}

/**
 * Send character sprites to webview
 */
export function sendCharacterSpritesToWebview(
  webview: vscode.Webview,
  charSprites: LoadedCharacterSprites,
): void {
  webview.postMessage({
    type: 'characterSpritesLoaded',
    characters: charSprites.characters,
  });
  console.log(`📤 Sent ${charSprites.characters.length} character sprites to webview`);
}

/**
 * Send loaded assets to webview
 */
export function sendAssetsToWebview(webview: vscode.Webview, assets: LoadedAssets): void {
  if (!assets) {
    console.log('[AssetLoader] ⚠️  No assets to send');
    return;
  }

  console.log('[AssetLoader] Converting sprites Map to object...');
  // Convert sprites Map to plain object for JSON serialization
  const spritesObj: Record<string, string[][]> = {};
  for (const [id, spriteData] of assets.sprites) {
    spritesObj[id] = spriteData;
  }

  console.log(
    `[AssetLoader] Posting furnitureAssetsLoaded message with ${assets.catalog.length} assets`,
  );
  webview.postMessage({
    type: 'furnitureAssetsLoaded',
    catalog: assets.catalog,
    sprites: spritesObj,
  });

  console.log(`📤 Sent ${assets.catalog.length} furniture assets to webview`);
}
```

## File: `src/constants.ts`
```typescript
// ── Timing (ms) ──────────────────────────────────────────────
export const JSONL_POLL_INTERVAL_MS = 1000;
export const FILE_WATCHER_POLL_INTERVAL_MS = 1000;
export const PROJECT_SCAN_INTERVAL_MS = 1000;
export const TOOL_DONE_DELAY_MS = 300;
export const PERMISSION_TIMER_DELAY_MS = 7000;
export const TEXT_IDLE_DELAY_MS = 5000;

// ── Display Truncation ──────────────────────────────────────
export const BASH_COMMAND_DISPLAY_MAX_LENGTH = 30;
export const TASK_DESCRIPTION_DISPLAY_MAX_LENGTH = 40;

// ── PNG / Asset Parsing ─────────────────────────────────────
export const PNG_ALPHA_THRESHOLD = 2;
export const WALL_PIECE_WIDTH = 16;
export const WALL_PIECE_HEIGHT = 32;
export const WALL_GRID_COLS = 4;
export const WALL_BITMASK_COUNT = 16;
export const FLOOR_TILE_SIZE = 16;
export const CHARACTER_DIRECTIONS = ['down', 'up', 'right'] as const;
export const CHAR_FRAME_W = 16;
export const CHAR_FRAME_H = 32;
export const CHAR_FRAMES_PER_ROW = 7;
export const CHAR_COUNT = 6;

// ── User-Level Layout Persistence ─────────────────────────────
export const LAYOUT_FILE_DIR = '.pixel-agents';
export const LAYOUT_FILE_NAME = 'layout.json';
export const LAYOUT_FILE_POLL_INTERVAL_MS = 2000;
export const LAYOUT_REVISION_KEY = 'layoutRevision';

// ── Settings Persistence ────────────────────────────────────
export const GLOBAL_KEY_SOUND_ENABLED = 'pixel-agents.soundEnabled';

// ── VS Code Identifiers ─────────────────────────────────────
export const VIEW_ID = 'pixel-agents.panelView';
export const COMMAND_SHOW_PANEL = 'pixel-agents.showPanel';
export const COMMAND_EXPORT_DEFAULT_LAYOUT = 'pixel-agents.exportDefaultLayout';
export const WORKSPACE_KEY_AGENTS = 'pixel-agents.agents';
export const WORKSPACE_KEY_AGENT_SEATS = 'pixel-agents.agentSeats';
export const WORKSPACE_KEY_LAYOUT = 'pixel-agents.layout';
export const TERMINAL_NAME_PREFIX = 'Claude Code';
```

## File: `src/extension.ts`
```typescript
import * as vscode from 'vscode';

import { COMMAND_EXPORT_DEFAULT_LAYOUT, COMMAND_SHOW_PANEL, VIEW_ID } from './constants.js';
import { PixelAgentsViewProvider } from './PixelAgentsViewProvider.js';

let providerInstance: PixelAgentsViewProvider | undefined;

export function activate(context: vscode.ExtensionContext) {
  const provider = new PixelAgentsViewProvider(context);
  providerInstance = provider;

  context.subscriptions.push(vscode.window.registerWebviewViewProvider(VIEW_ID, provider));

  context.subscriptions.push(
    vscode.commands.registerCommand(COMMAND_SHOW_PANEL, () => {
      vscode.commands.executeCommand(`${VIEW_ID}.focus`);
    }),
  );

  context.subscriptions.push(
    vscode.commands.registerCommand(COMMAND_EXPORT_DEFAULT_LAYOUT, () => {
      provider.exportDefaultLayout();
    }),
  );
}

export function deactivate() {
  providerInstance?.dispose();
}
```

## File: `src/fileWatcher.ts`
```typescript
import * as fs from 'fs';
import * as path from 'path';
import * as vscode from 'vscode';

import { FILE_WATCHER_POLL_INTERVAL_MS, PROJECT_SCAN_INTERVAL_MS } from './constants.js';
import { cancelPermissionTimer, cancelWaitingTimer, clearAgentActivity } from './timerManager.js';
import { processTranscriptLine } from './transcriptParser.js';
import type { AgentState } from './types.js';

export function startFileWatching(
  agentId: number,
  filePath: string,
  agents: Map<number, AgentState>,
  fileWatchers: Map<number, fs.FSWatcher>,
  pollingTimers: Map<number, ReturnType<typeof setInterval>>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
): void {
  // Primary: fs.watch (unreliable on macOS — may miss events)
  try {
    const watcher = fs.watch(filePath, () => {
      readNewLines(agentId, agents, waitingTimers, permissionTimers, webview);
    });
    fileWatchers.set(agentId, watcher);
  } catch (e) {
    console.log(`[Pixel Agents] fs.watch failed for agent ${agentId}: ${e}`);
  }

  // Secondary: fs.watchFile (stat-based polling, reliable on macOS)
  try {
    fs.watchFile(filePath, { interval: FILE_WATCHER_POLL_INTERVAL_MS }, () => {
      readNewLines(agentId, agents, waitingTimers, permissionTimers, webview);
    });
  } catch (e) {
    console.log(`[Pixel Agents] fs.watchFile failed for agent ${agentId}: ${e}`);
  }

  // Tertiary: manual poll as last resort
  const interval = setInterval(() => {
    if (!agents.has(agentId)) {
      clearInterval(interval);
      try {
        fs.unwatchFile(filePath);
      } catch {
        /* ignore */
      }
      return;
    }
    readNewLines(agentId, agents, waitingTimers, permissionTimers, webview);
  }, FILE_WATCHER_POLL_INTERVAL_MS);
  pollingTimers.set(agentId, interval);
}

export function readNewLines(
  agentId: number,
  agents: Map<number, AgentState>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
): void {
  const agent = agents.get(agentId);
  if (!agent) return;
  try {
    const stat = fs.statSync(agent.jsonlFile);
    if (stat.size <= agent.fileOffset) return;

    const buf = Buffer.alloc(stat.size - agent.fileOffset);
    const fd = fs.openSync(agent.jsonlFile, 'r');
    fs.readSync(fd, buf, 0, buf.length, agent.fileOffset);
    fs.closeSync(fd);
    agent.fileOffset = stat.size;

    const text = agent.lineBuffer + buf.toString('utf-8');
    const lines = text.split('\n');
    agent.lineBuffer = lines.pop() || '';

    const hasLines = lines.some((l) => l.trim());
    if (hasLines) {
      // New data arriving — cancel timers (data flowing means agent is still active)
      cancelWaitingTimer(agentId, waitingTimers);
      cancelPermissionTimer(agentId, permissionTimers);
      if (agent.permissionSent) {
        agent.permissionSent = false;
        webview?.postMessage({ type: 'agentToolPermissionClear', id: agentId });
      }
    }

    for (const line of lines) {
      if (!line.trim()) continue;
      processTranscriptLine(agentId, line, agents, waitingTimers, permissionTimers, webview);
    }
  } catch (e) {
    console.log(`[Pixel Agents] Read error for agent ${agentId}: ${e}`);
  }
}

export function ensureProjectScan(
  projectDir: string,
  knownJsonlFiles: Set<string>,
  projectScanTimerRef: { current: ReturnType<typeof setInterval> | null },
  activeAgentIdRef: { current: number | null },
  nextAgentIdRef: { current: number },
  agents: Map<number, AgentState>,
  fileWatchers: Map<number, fs.FSWatcher>,
  pollingTimers: Map<number, ReturnType<typeof setInterval>>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
  persistAgents: () => void,
): void {
  if (projectScanTimerRef.current) return;
  // Seed with all existing JSONL files so we only react to truly new ones
  try {
    const files = fs
      .readdirSync(projectDir)
      .filter((f) => f.endsWith('.jsonl'))
      .map((f) => path.join(projectDir, f));
    for (const f of files) {
      knownJsonlFiles.add(f);
    }
  } catch {
    /* dir may not exist yet */
  }

  projectScanTimerRef.current = setInterval(() => {
    scanForNewJsonlFiles(
      projectDir,
      knownJsonlFiles,
      activeAgentIdRef,
      nextAgentIdRef,
      agents,
      fileWatchers,
      pollingTimers,
      waitingTimers,
      permissionTimers,
      webview,
      persistAgents,
    );
  }, PROJECT_SCAN_INTERVAL_MS);
}

function scanForNewJsonlFiles(
  projectDir: string,
  knownJsonlFiles: Set<string>,
  activeAgentIdRef: { current: number | null },
  nextAgentIdRef: { current: number },
  agents: Map<number, AgentState>,
  fileWatchers: Map<number, fs.FSWatcher>,
  pollingTimers: Map<number, ReturnType<typeof setInterval>>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
  persistAgents: () => void,
): void {
  let files: string[];
  try {
    files = fs
      .readdirSync(projectDir)
      .filter((f) => f.endsWith('.jsonl'))
      .map((f) => path.join(projectDir, f));
  } catch {
    return;
  }

  for (const file of files) {
    if (!knownJsonlFiles.has(file)) {
      knownJsonlFiles.add(file);
      if (activeAgentIdRef.current !== null) {
        // Active agent focused → /clear reassignment
        console.log(
          `[Pixel Agents] New JSONL detected: ${path.basename(file)}, reassigning to agent ${activeAgentIdRef.current}`,
        );
        reassignAgentToFile(
          activeAgentIdRef.current,
          file,
          agents,
          fileWatchers,
          pollingTimers,
          waitingTimers,
          permissionTimers,
          webview,
          persistAgents,
        );
      } else {
        // No active agent → try to adopt the focused terminal
        const activeTerminal = vscode.window.activeTerminal;
        if (activeTerminal) {
          let owned = false;
          for (const agent of agents.values()) {
            if (agent.terminalRef === activeTerminal) {
              owned = true;
              break;
            }
          }
          if (!owned) {
            adoptTerminalForFile(
              activeTerminal,
              file,
              projectDir,
              nextAgentIdRef,
              agents,
              activeAgentIdRef,
              fileWatchers,
              pollingTimers,
              waitingTimers,
              permissionTimers,
              webview,
              persistAgents,
            );
          }
        }
      }
    }
  }
}

function adoptTerminalForFile(
  terminal: vscode.Terminal,
  jsonlFile: string,
  projectDir: string,
  nextAgentIdRef: { current: number },
  agents: Map<number, AgentState>,
  activeAgentIdRef: { current: number | null },
  fileWatchers: Map<number, fs.FSWatcher>,
  pollingTimers: Map<number, ReturnType<typeof setInterval>>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
  persistAgents: () => void,
): void {
  const id = nextAgentIdRef.current++;
  const agent: AgentState = {
    id,
    terminalRef: terminal,
    projectDir,
    jsonlFile,
    fileOffset: 0,
    lineBuffer: '',
    activeToolIds: new Set(),
    activeToolStatuses: new Map(),
    activeToolNames: new Map(),
    activeSubagentToolIds: new Map(),
    activeSubagentToolNames: new Map(),
    isWaiting: false,
    permissionSent: false,
    hadToolsInTurn: false,
  };

  agents.set(id, agent);
  activeAgentIdRef.current = id;
  persistAgents();

  console.log(
    `[Pixel Agents] Agent ${id}: adopted terminal "${terminal.name}" for ${path.basename(jsonlFile)}`,
  );
  webview?.postMessage({ type: 'agentCreated', id });

  startFileWatching(
    id,
    jsonlFile,
    agents,
    fileWatchers,
    pollingTimers,
    waitingTimers,
    permissionTimers,
    webview,
  );
  readNewLines(id, agents, waitingTimers, permissionTimers, webview);
}

export function reassignAgentToFile(
  agentId: number,
  newFilePath: string,
  agents: Map<number, AgentState>,
  fileWatchers: Map<number, fs.FSWatcher>,
  pollingTimers: Map<number, ReturnType<typeof setInterval>>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
  persistAgents: () => void,
): void {
  const agent = agents.get(agentId);
  if (!agent) return;

  // Stop old file watching
  fileWatchers.get(agentId)?.close();
  fileWatchers.delete(agentId);
  const pt = pollingTimers.get(agentId);
  if (pt) {
    clearInterval(pt);
  }
  pollingTimers.delete(agentId);
  try {
    fs.unwatchFile(agent.jsonlFile);
  } catch {
    /* ignore */
  }

  // Clear activity
  cancelWaitingTimer(agentId, waitingTimers);
  cancelPermissionTimer(agentId, permissionTimers);
  clearAgentActivity(agent, agentId, permissionTimers, webview);

  // Swap to new file
  agent.jsonlFile = newFilePath;
  agent.fileOffset = 0;
  agent.lineBuffer = '';
  persistAgents();

  // Start watching new file
  startFileWatching(
    agentId,
    newFilePath,
    agents,
    fileWatchers,
    pollingTimers,
    waitingTimers,
    permissionTimers,
    webview,
  );
  readNewLines(agentId, agents, waitingTimers, permissionTimers, webview);
}
```

## File: `src/layoutPersistence.ts`
```typescript
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import type { ExtensionContext } from 'vscode';

import {
  LAYOUT_FILE_DIR,
  LAYOUT_FILE_NAME,
  LAYOUT_FILE_POLL_INTERVAL_MS,
  LAYOUT_REVISION_KEY,
  WORKSPACE_KEY_LAYOUT,
} from './constants.js';

export interface LayoutWatcher {
  markOwnWrite(): void;
  dispose(): void;
}

function getLayoutFilePath(): string {
  return path.join(os.homedir(), LAYOUT_FILE_DIR, LAYOUT_FILE_NAME);
}

export function readLayoutFromFile(): Record<string, unknown> | null {
  const filePath = getLayoutFilePath();
  try {
    if (!fs.existsSync(filePath)) return null;
    const raw = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(raw) as Record<string, unknown>;
  } catch (err) {
    console.error('[Pixel Agents] Failed to read layout file:', err);
    return null;
  }
}

export function writeLayoutToFile(layout: Record<string, unknown>): void {
  const filePath = getLayoutFilePath();
  const dir = path.dirname(filePath);
  try {
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
    const json = JSON.stringify(layout, null, 2);
    const tmpPath = filePath + '.tmp';
    fs.writeFileSync(tmpPath, json, 'utf-8');
    fs.renameSync(tmpPath, filePath);
  } catch (err) {
    console.error('[Pixel Agents] Failed to write layout file:', err);
  }
}

export interface LayoutLoadResult {
  layout: Record<string, unknown>;
  /** True when the user's saved layout was replaced by a newer bundled default */
  wasReset: boolean;
}

/**
 * Load layout with migration from workspace state:
 * 1. If file exists → return it (reset if bundled default has a newer revision)
 * 2. Else if workspace state has layout → write to file, clear workspace state, return it
 * 3. Else if defaultLayout provided → write to file, return it
 * 4. Else → return null
 */
export function migrateAndLoadLayout(
  context: ExtensionContext,
  defaultLayout?: Record<string, unknown> | null,
): LayoutLoadResult | null {
  // 1. Try file — but reset if bundled default has a newer revision
  const fromFile = readLayoutFromFile();
  if (fromFile) {
    const fileRevision = (fromFile[LAYOUT_REVISION_KEY] as number) ?? 0;
    const defaultRevision = (defaultLayout?.[LAYOUT_REVISION_KEY] as number) ?? 0;
    if (defaultRevision > fileRevision) {
      console.log(
        `[Pixel Agents] Layout revision outdated (${fileRevision} < ${defaultRevision}), resetting to bundled default`,
      );
      writeLayoutToFile(defaultLayout!);
      return { layout: defaultLayout!, wasReset: true };
    }
    console.log('[Pixel Agents] Layout loaded from file');
    return { layout: fromFile, wasReset: false };
  }

  // 2. Migrate from workspace state
  const fromState = context.workspaceState.get<Record<string, unknown>>(WORKSPACE_KEY_LAYOUT);
  if (fromState) {
    console.log('[Pixel Agents] Migrating layout from workspace state to file');
    writeLayoutToFile(fromState);
    context.workspaceState.update(WORKSPACE_KEY_LAYOUT, undefined);
    return { layout: fromState, wasReset: false };
  }

  // 3. Use bundled default
  if (defaultLayout) {
    console.log('[Pixel Agents] Writing bundled default layout to file');
    writeLayoutToFile(defaultLayout);
    return { layout: defaultLayout, wasReset: false };
  }

  // 4. Nothing
  return null;
}

/**
 * Watch ~/.pixel-agents/layout.json for external changes (other VS Code windows).
 * Uses hybrid fs.watch + polling (same pattern as JSONL watching).
 */
export function watchLayoutFile(
  onExternalChange: (layout: Record<string, unknown>) => void,
): LayoutWatcher {
  const filePath = getLayoutFilePath();
  let skipNextChange = false;
  let lastMtime = 0;
  let fsWatcher: fs.FSWatcher | null = null;
  let pollTimer: ReturnType<typeof setInterval> | null = null;
  let disposed = false;

  // Initialize lastMtime
  try {
    if (fs.existsSync(filePath)) {
      lastMtime = fs.statSync(filePath).mtimeMs;
    }
  } catch {
    /* ignore */
  }

  function checkForChange(): void {
    if (disposed) return;
    try {
      if (!fs.existsSync(filePath)) return;
      const stat = fs.statSync(filePath);
      if (stat.mtimeMs <= lastMtime) return;
      lastMtime = stat.mtimeMs;

      if (skipNextChange) {
        skipNextChange = false;
        return;
      }

      const raw = fs.readFileSync(filePath, 'utf-8');
      const layout = JSON.parse(raw) as Record<string, unknown>;
      console.log('[Pixel Agents] External layout change detected');
      onExternalChange(layout);
    } catch (err) {
      console.error('[Pixel Agents] Error checking layout file:', err);
    }
  }

  function startFsWatch(): void {
    if (disposed || fsWatcher) return;
    try {
      if (!fs.existsSync(filePath)) return;
      fsWatcher = fs.watch(filePath, () => {
        checkForChange();
      });
      fsWatcher.on('error', () => {
        // fs.watch can be unreliable — polling backup handles it
        fsWatcher?.close();
        fsWatcher = null;
      });
    } catch {
      // File may not exist yet — polling will retry
    }
  }

  // Start fs.watch if file exists
  startFsWatch();

  // Polling backup (also starts fs.watch if file appears)
  pollTimer = setInterval(() => {
    if (disposed) return;
    if (!fsWatcher) {
      startFsWatch();
    }
    checkForChange();
  }, LAYOUT_FILE_POLL_INTERVAL_MS);

  return {
    markOwnWrite(): void {
      skipNextChange = true;
      // Update lastMtime preemptively so a near-instant poll doesn't miss the flag
      try {
        if (fs.existsSync(filePath)) {
          lastMtime = fs.statSync(filePath).mtimeMs;
        }
      } catch {
        /* ignore */
      }
    },
    dispose(): void {
      disposed = true;
      fsWatcher?.close();
      fsWatcher = null;
      if (pollTimer) {
        clearInterval(pollTimer);
        pollTimer = null;
      }
    },
  };
}
```

## File: `src/PixelAgentsViewProvider.ts`
```typescript
import * as fs from 'fs';
import * as os from 'os';
import * as path from 'path';
import * as vscode from 'vscode';

import {
  getProjectDirPath,
  launchNewTerminal,
  persistAgents,
  removeAgent,
  restoreAgents,
  sendExistingAgents,
  sendLayout,
} from './agentManager.js';
import {
  loadCharacterSprites,
  loadDefaultLayout,
  loadFloorTiles,
  loadFurnitureAssets,
  loadWallTiles,
  sendAssetsToWebview,
  sendCharacterSpritesToWebview,
  sendFloorTilesToWebview,
  sendWallTilesToWebview,
} from './assetLoader.js';
import {
  GLOBAL_KEY_SOUND_ENABLED,
  LAYOUT_REVISION_KEY,
  WORKSPACE_KEY_AGENT_SEATS,
} from './constants.js';
import { ensureProjectScan } from './fileWatcher.js';
import type { LayoutWatcher } from './layoutPersistence.js';
import { readLayoutFromFile, watchLayoutFile, writeLayoutToFile } from './layoutPersistence.js';
import type { AgentState } from './types.js';

export class PixelAgentsViewProvider implements vscode.WebviewViewProvider {
  nextAgentId = { current: 1 };
  nextTerminalIndex = { current: 1 };
  agents = new Map<number, AgentState>();
  webviewView: vscode.WebviewView | undefined;

  // Per-agent timers
  fileWatchers = new Map<number, fs.FSWatcher>();
  pollingTimers = new Map<number, ReturnType<typeof setInterval>>();
  waitingTimers = new Map<number, ReturnType<typeof setTimeout>>();
  jsonlPollTimers = new Map<number, ReturnType<typeof setInterval>>();
  permissionTimers = new Map<number, ReturnType<typeof setTimeout>>();

  // /clear detection: project-level scan for new JSONL files
  activeAgentId = { current: null as number | null };
  knownJsonlFiles = new Set<string>();
  projectScanTimer = { current: null as ReturnType<typeof setInterval> | null };

  // Bundled default layout (loaded from assets/default-layout.json)
  defaultLayout: Record<string, unknown> | null = null;

  // Cross-window layout sync
  layoutWatcher: LayoutWatcher | null = null;

  constructor(private readonly context: vscode.ExtensionContext) {}

  private get extensionUri(): vscode.Uri {
    return this.context.extensionUri;
  }

  private get webview(): vscode.Webview | undefined {
    return this.webviewView?.webview;
  }

  private persistAgents = (): void => {
    persistAgents(this.agents, this.context);
  };

  resolveWebviewView(webviewView: vscode.WebviewView) {
    this.webviewView = webviewView;
    webviewView.webview.options = { enableScripts: true };
    webviewView.webview.html = getWebviewContent(webviewView.webview, this.extensionUri);

    webviewView.webview.onDidReceiveMessage(async (message) => {
      if (message.type === 'openClaude') {
        await launchNewTerminal(
          this.nextAgentId,
          this.nextTerminalIndex,
          this.agents,
          this.activeAgentId,
          this.knownJsonlFiles,
          this.fileWatchers,
          this.pollingTimers,
          this.waitingTimers,
          this.permissionTimers,
          this.jsonlPollTimers,
          this.projectScanTimer,
          this.webview,
          this.persistAgents,
          message.folderPath as string | undefined,
        );
      } else if (message.type === 'focusAgent') {
        const agent = this.agents.get(message.id);
        if (agent) {
          agent.terminalRef.show();
        }
      } else if (message.type === 'closeAgent') {
        const agent = this.agents.get(message.id);
        if (agent) {
          agent.terminalRef.dispose();
        }
      } else if (message.type === 'saveAgentSeats') {
        // Store seat assignments in a separate key (never touched by persistAgents)
        console.log(`[Pixel Agents] saveAgentSeats:`, JSON.stringify(message.seats));
        this.context.workspaceState.update(WORKSPACE_KEY_AGENT_SEATS, message.seats);
      } else if (message.type === 'saveLayout') {
        this.layoutWatcher?.markOwnWrite();
        writeLayoutToFile(message.layout as Record<string, unknown>);
      } else if (message.type === 'setSoundEnabled') {
        this.context.globalState.update(GLOBAL_KEY_SOUND_ENABLED, message.enabled);
      } else if (message.type === 'webviewReady') {
        restoreAgents(
          this.context,
          this.nextAgentId,
          this.nextTerminalIndex,
          this.agents,
          this.knownJsonlFiles,
          this.fileWatchers,
          this.pollingTimers,
          this.waitingTimers,
          this.permissionTimers,
          this.jsonlPollTimers,
          this.projectScanTimer,
          this.activeAgentId,
          this.webview,
          this.persistAgents,
        );
        // Send persisted settings to webview
        const soundEnabled = this.context.globalState.get<boolean>(GLOBAL_KEY_SOUND_ENABLED, true);
        this.webview?.postMessage({ type: 'settingsLoaded', soundEnabled });

        // Send workspace folders to webview (only when multi-root)
        const wsFolders = vscode.workspace.workspaceFolders;
        if (wsFolders && wsFolders.length > 1) {
          this.webview?.postMessage({
            type: 'workspaceFolders',
            folders: wsFolders.map((f) => ({ name: f.name, path: f.uri.fsPath })),
          });
        }

        // Ensure project scan runs even with no restored agents (to adopt external terminals)
        const projectDir = getProjectDirPath();
        const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
        console.log('[Extension] workspaceRoot:', workspaceRoot);
        console.log('[Extension] projectDir:', projectDir);
        if (projectDir) {
          ensureProjectScan(
            projectDir,
            this.knownJsonlFiles,
            this.projectScanTimer,
            this.activeAgentId,
            this.nextAgentId,
            this.agents,
            this.fileWatchers,
            this.pollingTimers,
            this.waitingTimers,
            this.permissionTimers,
            this.webview,
            this.persistAgents,
          );

          // Load furniture assets BEFORE sending layout
          (async () => {
            try {
              console.log('[Extension] Loading furniture assets...');
              const extensionPath = this.extensionUri.fsPath;
              console.log('[Extension] extensionPath:', extensionPath);

              // Check bundled location first: extensionPath/dist/assets/
              const bundledAssetsDir = path.join(extensionPath, 'dist', 'assets');
              let assetsRoot: string | null = null;
              if (fs.existsSync(bundledAssetsDir)) {
                console.log('[Extension] Found bundled assets at dist/');
                assetsRoot = path.join(extensionPath, 'dist');
              } else if (workspaceRoot) {
                // Fall back to workspace root (development or external assets)
                console.log('[Extension] Trying workspace for assets...');
                assetsRoot = workspaceRoot;
              }

              if (!assetsRoot) {
                console.log('[Extension] ⚠️  No assets directory found');
                if (this.webview) {
                  sendLayout(this.context, this.webview, this.defaultLayout);
                  this.startLayoutWatcher();
                }
                return;
              }

              console.log('[Extension] Using assetsRoot:', assetsRoot);

              // Load bundled default layout
              this.defaultLayout = loadDefaultLayout(assetsRoot);

              // Load character sprites
              const charSprites = await loadCharacterSprites(assetsRoot);
              if (charSprites && this.webview) {
                console.log('[Extension] Character sprites loaded, sending to webview');
                sendCharacterSpritesToWebview(this.webview, charSprites);
              }

              // Load floor tiles
              const floorTiles = await loadFloorTiles(assetsRoot);
              if (floorTiles && this.webview) {
                console.log('[Extension] Floor tiles loaded, sending to webview');
                sendFloorTilesToWebview(this.webview, floorTiles);
              }

              // Load wall tiles
              const wallTiles = await loadWallTiles(assetsRoot);
              if (wallTiles && this.webview) {
                console.log('[Extension] Wall tiles loaded, sending to webview');
                sendWallTilesToWebview(this.webview, wallTiles);
              }

              const assets = await loadFurnitureAssets(assetsRoot);
              if (assets && this.webview) {
                console.log('[Extension] ✅ Assets loaded, sending to webview');
                sendAssetsToWebview(this.webview, assets);
              }
            } catch (err) {
              console.error('[Extension] ❌ Error loading assets:', err);
            }
            // Always send saved layout (or null for default)
            if (this.webview) {
              console.log('[Extension] Sending saved layout');
              sendLayout(this.context, this.webview, this.defaultLayout);
              this.startLayoutWatcher();
            }
          })();
        } else {
          // No project dir — still try to load floor/wall tiles, then send saved layout
          (async () => {
            try {
              const ep = this.extensionUri.fsPath;
              const bundled = path.join(ep, 'dist', 'assets');
              if (fs.existsSync(bundled)) {
                const distRoot = path.join(ep, 'dist');
                this.defaultLayout = loadDefaultLayout(distRoot);
                const cs = await loadCharacterSprites(distRoot);
                if (cs && this.webview) {
                  sendCharacterSpritesToWebview(this.webview, cs);
                }
                const ft = await loadFloorTiles(distRoot);
                if (ft && this.webview) {
                  sendFloorTilesToWebview(this.webview, ft);
                }
                const wt = await loadWallTiles(distRoot);
                if (wt && this.webview) {
                  sendWallTilesToWebview(this.webview, wt);
                }
              }
            } catch {
              /* ignore */
            }
            if (this.webview) {
              sendLayout(this.context, this.webview, this.defaultLayout);
              this.startLayoutWatcher();
            }
          })();
        }
        sendExistingAgents(this.agents, this.context, this.webview);
      } else if (message.type === 'openSessionsFolder') {
        const projectDir = getProjectDirPath();
        if (projectDir && fs.existsSync(projectDir)) {
          vscode.env.openExternal(vscode.Uri.file(projectDir));
        }
      } else if (message.type === 'exportLayout') {
        const layout = readLayoutFromFile();
        if (!layout) {
          vscode.window.showWarningMessage('Pixel Agents: No saved layout to export.');
          return;
        }
        const uri = await vscode.window.showSaveDialog({
          filters: { 'JSON Files': ['json'] },
          defaultUri: vscode.Uri.file(path.join(os.homedir(), 'pixel-agents-layout.json')),
        });
        if (uri) {
          fs.writeFileSync(uri.fsPath, JSON.stringify(layout, null, 2), 'utf-8');
          vscode.window.showInformationMessage('Pixel Agents: Layout exported successfully.');
        }
      } else if (message.type === 'importLayout') {
        const uris = await vscode.window.showOpenDialog({
          filters: { 'JSON Files': ['json'] },
          canSelectMany: false,
        });
        if (!uris || uris.length === 0) return;
        try {
          const raw = fs.readFileSync(uris[0].fsPath, 'utf-8');
          const imported = JSON.parse(raw) as Record<string, unknown>;
          if (imported.version !== 1 || !Array.isArray(imported.tiles)) {
            vscode.window.showErrorMessage('Pixel Agents: Invalid layout file.');
            return;
          }
          this.layoutWatcher?.markOwnWrite();
          writeLayoutToFile(imported);
          this.webview?.postMessage({ type: 'layoutLoaded', layout: imported });
          vscode.window.showInformationMessage('Pixel Agents: Layout imported successfully.');
        } catch {
          vscode.window.showErrorMessage('Pixel Agents: Failed to read or parse layout file.');
        }
      }
    });

    vscode.window.onDidChangeActiveTerminal((terminal) => {
      this.activeAgentId.current = null;
      if (!terminal) return;
      for (const [id, agent] of this.agents) {
        if (agent.terminalRef === terminal) {
          this.activeAgentId.current = id;
          webviewView.webview.postMessage({ type: 'agentSelected', id });
          break;
        }
      }
    });

    vscode.window.onDidCloseTerminal((closed) => {
      for (const [id, agent] of this.agents) {
        if (agent.terminalRef === closed) {
          if (this.activeAgentId.current === id) {
            this.activeAgentId.current = null;
          }
          removeAgent(
            id,
            this.agents,
            this.fileWatchers,
            this.pollingTimers,
            this.waitingTimers,
            this.permissionTimers,
            this.jsonlPollTimers,
            this.persistAgents,
          );
          webviewView.webview.postMessage({ type: 'agentClosed', id });
        }
      }
    });
  }

  /** Export current saved layout as a versioned default-layout-{N}.json (dev utility) */
  exportDefaultLayout(): void {
    const layout = readLayoutFromFile();
    if (!layout) {
      vscode.window.showWarningMessage('Pixel Agents: No saved layout found.');
      return;
    }
    const workspaceRoot = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath;
    if (!workspaceRoot) {
      vscode.window.showErrorMessage('Pixel Agents: No workspace folder found.');
      return;
    }
    const assetsDir = path.join(workspaceRoot, 'webview-ui', 'public', 'assets');

    // Find the next revision number
    let maxRevision = 0;
    if (fs.existsSync(assetsDir)) {
      for (const file of fs.readdirSync(assetsDir)) {
        const match = /^default-layout-(\d+)\.json$/.exec(file);
        if (match) {
          maxRevision = Math.max(maxRevision, parseInt(match[1], 10));
        }
      }
    }
    const nextRevision = maxRevision + 1;
    layout[LAYOUT_REVISION_KEY] = nextRevision;

    const targetPath = path.join(assetsDir, `default-layout-${nextRevision}.json`);
    const json = JSON.stringify(layout, null, 2);
    fs.writeFileSync(targetPath, json, 'utf-8');
    vscode.window.showInformationMessage(
      `Pixel Agents: Default layout exported as revision ${nextRevision} to ${targetPath}`,
    );
  }

  private startLayoutWatcher(): void {
    if (this.layoutWatcher) return;
    this.layoutWatcher = watchLayoutFile((layout) => {
      console.log('[Pixel Agents] External layout change — pushing to webview');
      this.webview?.postMessage({ type: 'layoutLoaded', layout });
    });
  }

  dispose() {
    this.layoutWatcher?.dispose();
    this.layoutWatcher = null;
    for (const id of [...this.agents.keys()]) {
      removeAgent(
        id,
        this.agents,
        this.fileWatchers,
        this.pollingTimers,
        this.waitingTimers,
        this.permissionTimers,
        this.jsonlPollTimers,
        this.persistAgents,
      );
    }
    if (this.projectScanTimer.current) {
      clearInterval(this.projectScanTimer.current);
      this.projectScanTimer.current = null;
    }
  }
}

export function getWebviewContent(webview: vscode.Webview, extensionUri: vscode.Uri): string {
  const distPath = vscode.Uri.joinPath(extensionUri, 'dist', 'webview');
  const indexPath = vscode.Uri.joinPath(distPath, 'index.html').fsPath;

  let html = fs.readFileSync(indexPath, 'utf-8');

  html = html.replace(/(href|src)="\.\/([^"]+)"/g, (_match, attr, filePath) => {
    const fileUri = vscode.Uri.joinPath(distPath, filePath);
    const webviewUri = webview.asWebviewUri(fileUri);
    return `${attr}="${webviewUri}"`;
  });

  return html;
}
```

## File: `src/timerManager.ts`
```typescript
import type * as vscode from 'vscode';

import { PERMISSION_TIMER_DELAY_MS } from './constants.js';
import type { AgentState } from './types.js';

export function clearAgentActivity(
  agent: AgentState | undefined,
  agentId: number,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
): void {
  if (!agent) return;
  agent.activeToolIds.clear();
  agent.activeToolStatuses.clear();
  agent.activeToolNames.clear();
  agent.activeSubagentToolIds.clear();
  agent.activeSubagentToolNames.clear();
  agent.isWaiting = false;
  agent.permissionSent = false;
  cancelPermissionTimer(agentId, permissionTimers);
  webview?.postMessage({ type: 'agentToolsClear', id: agentId });
  webview?.postMessage({ type: 'agentStatus', id: agentId, status: 'active' });
}

export function cancelWaitingTimer(
  agentId: number,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
): void {
  const timer = waitingTimers.get(agentId);
  if (timer) {
    clearTimeout(timer);
    waitingTimers.delete(agentId);
  }
}

export function startWaitingTimer(
  agentId: number,
  delayMs: number,
  agents: Map<number, AgentState>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
): void {
  cancelWaitingTimer(agentId, waitingTimers);
  const timer = setTimeout(() => {
    waitingTimers.delete(agentId);
    const agent = agents.get(agentId);
    if (agent) {
      agent.isWaiting = true;
    }
    webview?.postMessage({
      type: 'agentStatus',
      id: agentId,
      status: 'waiting',
    });
  }, delayMs);
  waitingTimers.set(agentId, timer);
}

export function cancelPermissionTimer(
  agentId: number,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
): void {
  const timer = permissionTimers.get(agentId);
  if (timer) {
    clearTimeout(timer);
    permissionTimers.delete(agentId);
  }
}

export function startPermissionTimer(
  agentId: number,
  agents: Map<number, AgentState>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionExemptTools: Set<string>,
  webview: vscode.Webview | undefined,
): void {
  cancelPermissionTimer(agentId, permissionTimers);
  const timer = setTimeout(() => {
    permissionTimers.delete(agentId);
    const agent = agents.get(agentId);
    if (!agent) return;

    // Only flag if there are still active non-exempt tools (parent or sub-agent)
    let hasNonExempt = false;
    for (const toolId of agent.activeToolIds) {
      const toolName = agent.activeToolNames.get(toolId);
      if (!permissionExemptTools.has(toolName || '')) {
        hasNonExempt = true;
        break;
      }
    }

    // Check sub-agent tools for non-exempt tools
    const stuckSubagentParentToolIds: string[] = [];
    for (const [parentToolId, subToolNames] of agent.activeSubagentToolNames) {
      for (const [, toolName] of subToolNames) {
        if (!permissionExemptTools.has(toolName)) {
          stuckSubagentParentToolIds.push(parentToolId);
          hasNonExempt = true;
          break;
        }
      }
    }

    if (hasNonExempt) {
      agent.permissionSent = true;
      console.log(`[Pixel Agents] Agent ${agentId}: possible permission wait detected`);
      webview?.postMessage({
        type: 'agentToolPermission',
        id: agentId,
      });
      // Also notify stuck sub-agents
      for (const parentToolId of stuckSubagentParentToolIds) {
        webview?.postMessage({
          type: 'subagentToolPermission',
          id: agentId,
          parentToolId,
        });
      }
    }
  }, PERMISSION_TIMER_DELAY_MS);
  permissionTimers.set(agentId, timer);
}
```

## File: `src/transcriptParser.ts`
```typescript
import * as path from 'path';
import type * as vscode from 'vscode';

import {
  BASH_COMMAND_DISPLAY_MAX_LENGTH,
  TASK_DESCRIPTION_DISPLAY_MAX_LENGTH,
  TEXT_IDLE_DELAY_MS,
  TOOL_DONE_DELAY_MS,
} from './constants.js';
import {
  cancelPermissionTimer,
  cancelWaitingTimer,
  clearAgentActivity,
  startPermissionTimer,
  startWaitingTimer,
} from './timerManager.js';
import type { AgentState } from './types.js';

export const PERMISSION_EXEMPT_TOOLS = new Set(['Task', 'Agent', 'AskUserQuestion']);

export function formatToolStatus(toolName: string, input: Record<string, unknown>): string {
  const base = (p: unknown) => (typeof p === 'string' ? path.basename(p) : '');
  switch (toolName) {
    case 'Read':
      return `Reading ${base(input.file_path)}`;
    case 'Edit':
      return `Editing ${base(input.file_path)}`;
    case 'Write':
      return `Writing ${base(input.file_path)}`;
    case 'Bash': {
      const cmd = (input.command as string) || '';
      return `Running: ${cmd.length > BASH_COMMAND_DISPLAY_MAX_LENGTH ? cmd.slice(0, BASH_COMMAND_DISPLAY_MAX_LENGTH) + '\u2026' : cmd}`;
    }
    case 'Glob':
      return 'Searching files';
    case 'Grep':
      return 'Searching code';
    case 'WebFetch':
      return 'Fetching web content';
    case 'WebSearch':
      return 'Searching the web';
    case 'Task':
    case 'Agent': {
      const desc = typeof input.description === 'string' ? input.description : '';
      return desc
        ? `Subtask: ${desc.length > TASK_DESCRIPTION_DISPLAY_MAX_LENGTH ? desc.slice(0, TASK_DESCRIPTION_DISPLAY_MAX_LENGTH) + '\u2026' : desc}`
        : 'Running subtask';
    }
    case 'AskUserQuestion':
      return 'Waiting for your answer';
    case 'EnterPlanMode':
      return 'Planning';
    case 'NotebookEdit':
      return `Editing notebook`;
    default:
      return `Using ${toolName}`;
  }
}

export function processTranscriptLine(
  agentId: number,
  line: string,
  agents: Map<number, AgentState>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
): void {
  const agent = agents.get(agentId);
  if (!agent) return;
  try {
    const record = JSON.parse(line);

    if (record.type === 'assistant' && Array.isArray(record.message?.content)) {
      const blocks = record.message.content as Array<{
        type: string;
        id?: string;
        name?: string;
        input?: Record<string, unknown>;
      }>;
      const hasToolUse = blocks.some((b) => b.type === 'tool_use');

      if (hasToolUse) {
        cancelWaitingTimer(agentId, waitingTimers);
        agent.isWaiting = false;
        agent.hadToolsInTurn = true;
        webview?.postMessage({ type: 'agentStatus', id: agentId, status: 'active' });
        let hasNonExemptTool = false;
        for (const block of blocks) {
          if (block.type === 'tool_use' && block.id) {
            const toolName = block.name || '';
            const status = formatToolStatus(toolName, block.input || {});
            console.log(`[Pixel Agents] Agent ${agentId} tool start: ${block.id} ${status}`);
            agent.activeToolIds.add(block.id);
            agent.activeToolStatuses.set(block.id, status);
            agent.activeToolNames.set(block.id, toolName);
            if (!PERMISSION_EXEMPT_TOOLS.has(toolName)) {
              hasNonExemptTool = true;
            }
            webview?.postMessage({
              type: 'agentToolStart',
              id: agentId,
              toolId: block.id,
              status,
            });
          }
        }
        if (hasNonExemptTool) {
          startPermissionTimer(agentId, agents, permissionTimers, PERMISSION_EXEMPT_TOOLS, webview);
        }
      } else if (blocks.some((b) => b.type === 'text') && !agent.hadToolsInTurn) {
        // Text-only response in a turn that hasn't used any tools.
        // turn_duration handles tool-using turns reliably but is never
        // emitted for text-only turns, so we use a silence-based timer:
        // if no new JSONL data arrives within TEXT_IDLE_DELAY_MS, mark as waiting.
        startWaitingTimer(agentId, TEXT_IDLE_DELAY_MS, agents, waitingTimers, webview);
      }
    } else if (record.type === 'progress') {
      processProgressRecord(agentId, record, agents, waitingTimers, permissionTimers, webview);
    } else if (record.type === 'user') {
      const content = record.message?.content;
      if (Array.isArray(content)) {
        const blocks = content as Array<{ type: string; tool_use_id?: string }>;
        const hasToolResult = blocks.some((b) => b.type === 'tool_result');
        if (hasToolResult) {
          for (const block of blocks) {
            if (block.type === 'tool_result' && block.tool_use_id) {
              console.log(`[Pixel Agents] Agent ${agentId} tool done: ${block.tool_use_id}`);
              const completedToolId = block.tool_use_id;
              // If the completed tool was a Task/Agent, clear its subagent tools
              const completedToolName = agent.activeToolNames.get(completedToolId);
              if (completedToolName === 'Task' || completedToolName === 'Agent') {
                agent.activeSubagentToolIds.delete(completedToolId);
                agent.activeSubagentToolNames.delete(completedToolId);
                webview?.postMessage({
                  type: 'subagentClear',
                  id: agentId,
                  parentToolId: completedToolId,
                });
              }
              agent.activeToolIds.delete(completedToolId);
              agent.activeToolStatuses.delete(completedToolId);
              agent.activeToolNames.delete(completedToolId);
              const toolId = completedToolId;
              setTimeout(() => {
                webview?.postMessage({
                  type: 'agentToolDone',
                  id: agentId,
                  toolId,
                });
              }, TOOL_DONE_DELAY_MS);
            }
          }
          // All tools completed — allow text-idle timer as fallback
          // for turn-end detection when turn_duration is not emitted
          if (agent.activeToolIds.size === 0) {
            agent.hadToolsInTurn = false;
          }
        } else {
          // New user text prompt — new turn starting
          cancelWaitingTimer(agentId, waitingTimers);
          clearAgentActivity(agent, agentId, permissionTimers, webview);
          agent.hadToolsInTurn = false;
        }
      } else if (typeof content === 'string' && content.trim()) {
        // New user text prompt — new turn starting
        cancelWaitingTimer(agentId, waitingTimers);
        clearAgentActivity(agent, agentId, permissionTimers, webview);
        agent.hadToolsInTurn = false;
      }
    } else if (record.type === 'system' && record.subtype === 'turn_duration') {
      cancelWaitingTimer(agentId, waitingTimers);
      cancelPermissionTimer(agentId, permissionTimers);

      // Definitive turn-end: clean up any stale tool state
      if (agent.activeToolIds.size > 0) {
        agent.activeToolIds.clear();
        agent.activeToolStatuses.clear();
        agent.activeToolNames.clear();
        agent.activeSubagentToolIds.clear();
        agent.activeSubagentToolNames.clear();
        webview?.postMessage({ type: 'agentToolsClear', id: agentId });
      }

      agent.isWaiting = true;
      agent.permissionSent = false;
      agent.hadToolsInTurn = false;
      webview?.postMessage({
        type: 'agentStatus',
        id: agentId,
        status: 'waiting',
      });
    }
  } catch {
    // Ignore malformed lines
  }
}

function processProgressRecord(
  agentId: number,
  record: Record<string, unknown>,
  agents: Map<number, AgentState>,
  waitingTimers: Map<number, ReturnType<typeof setTimeout>>,
  permissionTimers: Map<number, ReturnType<typeof setTimeout>>,
  webview: vscode.Webview | undefined,
): void {
  const agent = agents.get(agentId);
  if (!agent) return;

  const parentToolId = record.parentToolUseID as string | undefined;
  if (!parentToolId) return;

  const data = record.data as Record<string, unknown> | undefined;
  if (!data) return;

  // bash_progress / mcp_progress: tool is actively executing, not stuck on permission.
  // Restart the permission timer to give the running tool another window.
  const dataType = data.type as string | undefined;
  if (dataType === 'bash_progress' || dataType === 'mcp_progress') {
    if (agent.activeToolIds.has(parentToolId)) {
      startPermissionTimer(agentId, agents, permissionTimers, PERMISSION_EXEMPT_TOOLS, webview);
    }
    return;
  }

  // Verify parent is an active Task/Agent tool (agent_progress handling)
  const parentToolName = agent.activeToolNames.get(parentToolId);
  if (parentToolName !== 'Task' && parentToolName !== 'Agent') return;

  const msg = data.message as Record<string, unknown> | undefined;
  if (!msg) return;

  const msgType = msg.type as string;
  const innerMsg = msg.message as Record<string, unknown> | undefined;
  const content = innerMsg?.content;
  if (!Array.isArray(content)) return;

  if (msgType === 'assistant') {
    let hasNonExemptSubTool = false;
    for (const block of content) {
      if (block.type === 'tool_use' && block.id) {
        const toolName = block.name || '';
        const status = formatToolStatus(toolName, block.input || {});
        console.log(
          `[Pixel Agents] Agent ${agentId} subagent tool start: ${block.id} ${status} (parent: ${parentToolId})`,
        );

        // Track sub-tool IDs
        let subTools = agent.activeSubagentToolIds.get(parentToolId);
        if (!subTools) {
          subTools = new Set();
          agent.activeSubagentToolIds.set(parentToolId, subTools);
        }
        subTools.add(block.id);

        // Track sub-tool names (for permission checking)
        let subNames = agent.activeSubagentToolNames.get(parentToolId);
        if (!subNames) {
          subNames = new Map();
          agent.activeSubagentToolNames.set(parentToolId, subNames);
        }
        subNames.set(block.id, toolName);

        if (!PERMISSION_EXEMPT_TOOLS.has(toolName)) {
          hasNonExemptSubTool = true;
        }

        webview?.postMessage({
          type: 'subagentToolStart',
          id: agentId,
          parentToolId,
          toolId: block.id,
          status,
        });
      }
    }
    if (hasNonExemptSubTool) {
      startPermissionTimer(agentId, agents, permissionTimers, PERMISSION_EXEMPT_TOOLS, webview);
    }
  } else if (msgType === 'user') {
    for (const block of content) {
      if (block.type === 'tool_result' && block.tool_use_id) {
        console.log(
          `[Pixel Agents] Agent ${agentId} subagent tool done: ${block.tool_use_id} (parent: ${parentToolId})`,
        );

        // Remove from tracking
        const subTools = agent.activeSubagentToolIds.get(parentToolId);
        if (subTools) {
          subTools.delete(block.tool_use_id);
        }
        const subNames = agent.activeSubagentToolNames.get(parentToolId);
        if (subNames) {
          subNames.delete(block.tool_use_id);
        }

        const toolId = block.tool_use_id;
        setTimeout(() => {
          webview?.postMessage({
            type: 'subagentToolDone',
            id: agentId,
            parentToolId,
            toolId,
          });
        }, 300);
      }
    }
    // If there are still active non-exempt sub-agent tools, restart the permission timer
    // (handles the case where one sub-agent completes but another is still stuck)
    let stillHasNonExempt = false;
    for (const [, subNames] of agent.activeSubagentToolNames) {
      for (const [, toolName] of subNames) {
        if (!PERMISSION_EXEMPT_TOOLS.has(toolName)) {
          stillHasNonExempt = true;
          break;
        }
      }
      if (stillHasNonExempt) break;
    }
    if (stillHasNonExempt) {
      startPermissionTimer(agentId, agents, permissionTimers, PERMISSION_EXEMPT_TOOLS, webview);
    }
  }
}
```

## File: `src/types.ts`
```typescript
import type * as vscode from 'vscode';

export interface AgentState {
  id: number;
  terminalRef: vscode.Terminal;
  projectDir: string;
  jsonlFile: string;
  fileOffset: number;
  lineBuffer: string;
  activeToolIds: Set<string>;
  activeToolStatuses: Map<string, string>;
  activeToolNames: Map<string, string>;
  activeSubagentToolIds: Map<string, Set<string>>; // parentToolId → active sub-tool IDs
  activeSubagentToolNames: Map<string, Map<string, string>>; // parentToolId → (subToolId → toolName)
  isWaiting: boolean;
  permissionSent: boolean;
  hadToolsInTurn: boolean;
  /** Workspace folder name (only set for multi-root workspaces) */
  folderName?: string;
}

export interface PersistedAgent {
  id: number;
  terminalName: string;
  jsonlFile: string;
  projectDir: string;
  /** Workspace folder name (only set for multi-root workspaces) */
  folderName?: string;
}
```

## File: `webview-ui/.gitignore`
```
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

# Editor directories and files
.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?
```

## File: `webview-ui/eslint.config.js`
```javascript
import js from '@eslint/js';
import globals from 'globals';
import reactHooks from 'eslint-plugin-react-hooks';
import reactRefresh from 'eslint-plugin-react-refresh';
import simpleImportSort from 'eslint-plugin-simple-import-sort';
import tseslint from 'typescript-eslint';
import eslintConfigPrettier from 'eslint-config-prettier';
import { defineConfig, globalIgnores } from 'eslint/config';
import pixelAgentsPlugin from '../eslint-rules/pixel-agents-rules.mjs';

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      js.configs.recommended,
      tseslint.configs.recommended,
      reactHooks.configs.flat.recommended,
      reactRefresh.configs.vite,
    ],
    plugins: {
      'simple-import-sort': simpleImportSort,
      'pixel-agents': pixelAgentsPlugin,
    },
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
    },
    rules: {
      'simple-import-sort/imports': 'warn',
      'simple-import-sort/exports': 'warn',
      // These react-hooks rules misfire on this project's imperative game-state patterns:
      // - immutability: singleton OfficeState/EditorState mutations are by design
      // - refs: containerRef reads during render feed canvas pipeline, not React state
      // - set-state-in-effect: timer-based animations and async error handling are legitimate
      'react-hooks/immutability': 'off',
      'react-hooks/refs': 'off',
      'react-hooks/set-state-in-effect': 'off',
      'pixel-agents/no-inline-colors': 'warn',
      'pixel-agents/pixel-shadow': 'warn',
      'pixel-agents/pixel-font': 'warn',
    },
  },
  {
    files: ['src/constants.ts', 'src/fonts/**', 'src/office/sprites/**'],
    rules: {
      'pixel-agents/no-inline-colors': 'off',
      'pixel-agents/pixel-shadow': 'off',
      'pixel-agents/pixel-font': 'off',
    },
  },
  eslintConfigPrettier,
]);
```

## File: `webview-ui/index.html`
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>webview-ui</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
```

## File: `webview-ui/package.json`
```json
{
  "name": "webview-ui",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^19.2.0",
    "react-dom": "^19.2.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.1",
    "@types/node": "^25.5.0",
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.1.1",
    "eslint": "^9.39.1",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.5.2",
    "eslint-plugin-simple-import-sort": "^12.1.1",
    "globals": "^17.4.0",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.57.0",
    "vite": "^7.2.4"
  }
}
```

## File: `webview-ui/README.md`
```markdown
# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```
```

## File: `webview-ui/tsconfig.app.json`
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.app.tsbuildinfo",
    "target": "ES2022",
    "useDefineForClassFields": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "types": ["vite/client"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,
    "jsx": "react-jsx",

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["src"]
}
```

## File: `webview-ui/tsconfig.json`
```json
{
  "files": [],
  "references": [
    { "path": "./tsconfig.app.json" },
    { "path": "./tsconfig.node.json" }
  ]
}
```

## File: `webview-ui/tsconfig.node.json`
```json
{
  "compilerOptions": {
    "tsBuildInfoFile": "./node_modules/.tmp/tsconfig.node.tsbuildinfo",
    "target": "ES2023",
    "lib": ["ES2023"],
    "module": "ESNext",
    "types": ["node"],
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "moduleDetection": "force",
    "noEmit": true,

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "erasableSyntaxOnly": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedSideEffectImports": true
  },
  "include": ["vite.config.ts"]
}
```

## File: `webview-ui/vite.config.ts`
```typescript
import react from '@vitejs/plugin-react';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: '../dist/webview',
    emptyOutDir: true,
  },
  base: './',
});
```

## File: `webview-ui/public/assets/default-layout-1.json`
```json
{
  "version": 1,
  "cols": 21,
  "rows": 22,
  "layoutRevision": 1,
  "tiles": [
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
      0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   0,   1,   1,   1,   1,   1,   1,   1,   1,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   0,   1,   1,   1,   1,   1,   1,   1,   1,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   0,   1,   1,   1,   1,   1,   1,   1,   1,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   0,   1,   1,   1,   1,   1,   1,   1,   1,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   0,   9,   9,   9,   9,   9,   9,   9,   9,   0, 255,
      0,   7,   7,   7,   7,   7,   7,   7,   7,   7,   0,   9,   9,   9,   9,   9,   9,   9,   9,   0, 255,
    255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255
  ],
  "tileColors": [
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":209,"s":39,"b":-25,"c":-80}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    {"h":214,"s":30,"b":-100,"c":-55}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":25,"s":48,"b":-43,"c":-88}, {"h":214,"s":30,"b":-100,"c":-55}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":209,"s":0,"b":-16,"c":-8}, {"h":214,"s":30,"b":-100,"c":-55}, null,
    null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null
  ],
  "furniture": [
    {"uid": "f-1773353910654-5cdg", "type": "TABLE_FRONT", "col": 4, "row": 16},
    {"uid": "f-1773354646615-jhxl", "type": "COFFEE_TABLE", "col": 14, "row": 14},
    {"uid": "f-1773354664329-hxsh", "type": "SOFA_SIDE", "col": 13, "row": 14},
    {"uid": "f-1773354665989-zgrw", "type": "SOFA_BACK", "col": 14, "row": 16},
    {"uid": "f-1773354668333-lo7w", "type": "SOFA_FRONT", "col": 14, "row": 13},
    {"uid": "f-1773354670818-r1q2", "type": "SOFA_SIDE:left", "col": 16, "row": 14},
    {"uid": "f-1773354686967-yiua", "type": "HANGING_PLANT", "col": 9, "row": 9},
    {"uid": "f-1773354687677-hn2k", "type": "HANGING_PLANT", "col": 1, "row": 9},
    {"uid": "f-1773354693077-f7aj", "type": "DOUBLE_BOOKSHELF", "col": 7, "row": 9},
    {"uid": "f-1773354700513-f1zs", "type": "DOUBLE_BOOKSHELF", "col": 2, "row": 9},
    {"uid": "f-1773354799984-j5ri", "type": "SMALL_PAINTING", "col": 12, "row": 9},
    {"uid": "f-1773354827151-yox2", "type": "CLOCK", "col": 5, "row": 9},
    {"uid": "f-1773354842615-f5md", "type": "PLANT", "col": 18, "row": 10},
    {"uid": "f-1773354861273-67uo", "type": "COFFEE", "col": 14, "row": 15},
    {"uid": "f-1773354877474-kt9s", "type": "WOODEN_CHAIR_SIDE", "col": 3, "row": 18},
    {"uid": "f-1773354879805-px9b", "type": "WOODEN_CHAIR_SIDE", "col": 3, "row": 16},
    {"uid": "f-1773354880309-yphd", "type": "WOODEN_CHAIR_SIDE:left", "col": 7, "row": 16},
    {"uid": "f-1773354881902-9m50", "type": "WOODEN_CHAIR_SIDE:left", "col": 7, "row": 18},
    {"uid": "f-1773354931010-8vvr", "type": "DESK_FRONT", "col": 2, "row": 12},
    {"uid": "f-1773354932396-5uus", "type": "DESK_FRONT", "col": 6, "row": 12},
    {"uid": "f-1773356768339-eo6u", "type": "CUSHIONED_BENCH", "col": 3, "row": 14},
    {"uid": "f-1773356769007-a8jm", "type": "CUSHIONED_BENCH", "col": 7, "row": 14},
    {"uid": "f-1773356781294-b69z", "type": "PC_FRONT_OFF", "col": 7, "row": 12},
    {"uid": "f-1773356782055-vp70", "type": "PC_FRONT_OFF", "col": 3, "row": 12},
    {"uid": "f-1773356784581-5jw9", "type": "PC_SIDE", "col": 4, "row": 16},
    {"uid": "f-1773356785458-pyjn", "type": "PC_SIDE", "col": 4, "row": 18},
    {"uid": "f-1773356787060-higb", "type": "PC_SIDE:left", "col": 6, "row": 16},
    {"uid": "f-1773356787744-ykrz", "type": "PC_SIDE:left", "col": 6, "row": 18},
    {"uid": "f-1773356878781-rncl", "type": "PLANT_2", "col": 11, "row": 10},
    {"uid": "f-1773356974812-apra", "type": "LARGE_PAINTING", "col": 14, "row": 9},
    {"uid": "f-1773357087399-3kfy", "type": "BIN", "col": 2, "row": 20},
    {"uid": "f-1773357989802-thws", "type": "SMALL_TABLE_FRONT", "col": 17, "row": 19},
    {"uid": "f-1773358001163-aqv4", "type": "SMALL_TABLE_SIDE", "col": 1, "row": 18},
    {"uid": "f-1773358458100-4wm2", "type": "COFFEE", "col": 1, "row": 19},
    {"uid": "f-1773358479734-biia", "type": "PLANT_2", "col": 1, "row": 17},
    {"uid": "f-1773358485454-id8j", "type": "SMALL_PAINTING_2", "col": 17, "row": 9}
  ]
}
```

## File: `webview-ui/public/assets/furniture/BIN/manifest.json`
```json
{
  "id": "BIN",
  "name": "Bin",
  "category": "misc",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 16,
  "height": 16,
  "footprintW": 1,
  "footprintH": 1
}
```

## File: `webview-ui/public/assets/furniture/BOOKSHELF/manifest.json`
```json
{
  "id": "BOOKSHELF",
  "name": "Bookshelf",
  "category": "wall",
  "type": "asset",
  "canPlaceOnWalls": true,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 32,
  "height": 16,
  "footprintW": 2,
  "footprintH": 1
}
```

## File: `webview-ui/public/assets/furniture/CACTUS/manifest.json`
```json
{
  "id": "CACTUS",
  "name": "Cactus",
  "category": "decor",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 1,
  "width": 16,
  "height": 32,
  "footprintW": 1,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/CLOCK/manifest.json`
```json
{
  "id": "CLOCK",
  "name": "Clock",
  "category": "wall",
  "type": "asset",
  "canPlaceOnWalls": true,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 16,
  "height": 32,
  "footprintW": 1,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/COFFEE/manifest.json`
```json
{
  "id": "COFFEE",
  "name": "Coffee",
  "category": "decor",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": true,
  "backgroundTiles": 0,
  "width": 16,
  "height": 16,
  "footprintW": 1,
  "footprintH": 1
}
```

## File: `webview-ui/public/assets/furniture/COFFEE_TABLE/manifest.json`
```json
{
  "id": "COFFEE_TABLE",
  "name": "Coffee Table",
  "category": "desks",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 32,
  "height": 32,
  "footprintW": 2,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/CUSHIONED_BENCH/manifest.json`
```json
{
  "id": "CUSHIONED_BENCH",
  "name": "Cushioned Bench",
  "category": "chairs",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 16,
  "height": 16,
  "footprintW": 1,
  "footprintH": 1
}
```

## File: `webview-ui/public/assets/furniture/CUSHIONED_CHAIR/manifest.json`
```json
{
  "id": "CUSHIONED_CHAIR",
  "name": "Cushioned Chair",
  "category": "chairs",
  "type": "group",
  "groupType": "rotation",
  "rotationScheme": "3-way-mirror",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "members": [
    {
      "type": "asset",
      "id": "CUSHIONED_CHAIR_FRONT",
      "file": "CUSHIONED_CHAIR_FRONT.png",
      "width": 16,
      "height": 16,
      "footprintW": 1,
      "footprintH": 1,
      "orientation": "front"
    },
    {
      "type": "asset",
      "id": "CUSHIONED_CHAIR_BACK",
      "file": "CUSHIONED_CHAIR_BACK.png",
      "width": 16,
      "height": 16,
      "footprintW": 1,
      "footprintH": 1,
      "orientation": "back"
    },
    {
      "type": "asset",
      "id": "CUSHIONED_CHAIR_SIDE",
      "file": "CUSHIONED_CHAIR_SIDE.png",
      "width": 16,
      "height": 16,
      "footprintW": 1,
      "footprintH": 1,
      "orientation": "side",
      "mirrorSide": true
    }
  ]
}
```

## File: `webview-ui/public/assets/furniture/DESK/manifest.json`
```json
{
  "id": "DESK",
  "name": "Desk",
  "category": "desks",
  "type": "group",
  "groupType": "rotation",
  "rotationScheme": "2-way",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 1,
  "members": [
    {
      "type": "asset",
      "id": "DESK_FRONT",
      "file": "DESK_FRONT.png",
      "width": 48,
      "height": 32,
      "footprintW": 3,
      "footprintH": 2,
      "orientation": "front"
    },
    {
      "type": "asset",
      "id": "DESK_SIDE",
      "file": "DESK_SIDE.png",
      "width": 16,
      "height": 64,
      "footprintW": 1,
      "footprintH": 4,
      "orientation": "side"
    }
  ]
}
```

## File: `webview-ui/public/assets/furniture/DOUBLE_BOOKSHELF/manifest.json`
```json
{
  "id": "DOUBLE_BOOKSHELF",
  "name": "Double Bookshelf",
  "category": "wall",
  "type": "asset",
  "canPlaceOnWalls": true,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 32,
  "height": 32,
  "footprintW": 2,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/HANGING_PLANT/manifest.json`
```json
{
  "id": "HANGING_PLANT",
  "name": "Hanging Plant",
  "category": "wall",
  "type": "asset",
  "canPlaceOnWalls": true,
  "canPlaceOnSurfaces": true,
  "backgroundTiles": 0,
  "width": 16,
  "height": 32,
  "footprintW": 1,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/LARGE_PAINTING/manifest.json`
```json
{
  "id": "LARGE_PAINTING",
  "name": "Large Painting",
  "category": "wall",
  "type": "asset",
  "canPlaceOnWalls": true,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 32,
  "height": 32,
  "footprintW": 2,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/LARGE_PLANT/manifest.json`
```json
{
  "id": "LARGE_PLANT",
  "name": "Large Plant",
  "category": "decor",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 32,
  "height": 48,
  "footprintW": 2,
  "footprintH": 3
}
```

## File: `webview-ui/public/assets/furniture/PC/manifest.json`
```json
{
  "id": "PC",
  "name": "PC",
  "category": "electronics",
  "type": "group",
  "groupType": "rotation",
  "rotationScheme": "3-way-mirror",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": true,
  "backgroundTiles": 1,
  "members": [
    {
      "type": "group",
      "groupType": "state",
      "orientation": "front",
      "members": [
        {
          "type": "group",
          "groupType": "animation",
          "state": "on",
          "members": [
            {
              "type": "asset",
              "id": "PC_FRONT_ON_1",
              "file": "PC_FRONT_ON_1.png",
              "width": 16,
              "height": 32,
              "footprintW": 1,
              "footprintH": 2,
              "frame": 0
            },
            {
              "type": "asset",
              "id": "PC_FRONT_ON_2",
              "file": "PC_FRONT_ON_2.png",
              "width": 16,
              "height": 32,
              "footprintW": 1,
              "footprintH": 2,
              "frame": 1
            },
            {
              "type": "asset",
              "id": "PC_FRONT_ON_3",
              "file": "PC_FRONT_ON_3.png",
              "width": 16,
              "height": 32,
              "footprintW": 1,
              "footprintH": 2,
              "frame": 2
            }
          ]
        },
        {
          "type": "asset",
          "id": "PC_FRONT_OFF",
          "file": "PC_FRONT_OFF.png",
          "width": 16,
          "height": 32,
          "footprintW": 1,
          "footprintH": 2,
          "state": "off"
        }
      ]
    },
    {
      "type": "asset",
      "id": "PC_BACK",
      "file": "PC_BACK.png",
      "width": 16,
      "height": 32,
      "footprintW": 1,
      "footprintH": 2,
      "orientation": "back"
    },
    {
      "type": "asset",
      "id": "PC_SIDE",
      "file": "PC_SIDE.png",
      "width": 16,
      "height": 32,
      "footprintW": 1,
      "footprintH": 2,
      "orientation": "side",
      "mirrorSide": true
    }
  ]
}
```

## File: `webview-ui/public/assets/furniture/PLANT/manifest.json`
```json
{
  "id": "PLANT",
  "name": "Plant",
  "category": "decor",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 1,
  "width": 16,
  "height": 32,
  "footprintW": 1,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/PLANT_2/manifest.json`
```json
{
  "id": "PLANT_2",
  "name": "Plant",
  "category": "decor",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 1,
  "width": 16,
  "height": 32,
  "footprintW": 1,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/POT/manifest.json`
```json
{
  "id": "POT",
  "name": "Pot",
  "category": "decor",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 16,
  "height": 16,
  "footprintW": 1,
  "footprintH": 1
}
```

## File: `webview-ui/public/assets/furniture/SMALL_PAINTING/manifest.json`
```json
{
  "id": "SMALL_PAINTING",
  "name": "Small Painting",
  "category": "wall",
  "type": "asset",
  "canPlaceOnWalls": true,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 16,
  "height": 32,
  "footprintW": 1,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/SMALL_PAINTING_2/manifest.json`
```json
{
  "id": "SMALL_PAINTING_2",
  "name": "Small Painting",
  "category": "wall",
  "type": "asset",
  "canPlaceOnWalls": true,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 16,
  "height": 32,
  "footprintW": 1,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/SMALL_TABLE/manifest.json`
```json
{
  "id": "SMALL_TABLE",
  "name": "Small Table",
  "category": "desks",
  "type": "group",
  "groupType": "rotation",
  "rotationScheme": "2-way",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 1,
  "members": [
    {
      "type": "asset",
      "id": "SMALL_TABLE_FRONT",
      "file": "SMALL_TABLE_FRONT.png",
      "width": 32,
      "height": 32,
      "footprintW": 2,
      "footprintH": 2,
      "orientation": "front"
    },
    {
      "type": "asset",
      "id": "SMALL_TABLE_SIDE",
      "file": "SMALL_TABLE_SIDE.png",
      "width": 16,
      "height": 48,
      "footprintW": 1,
      "footprintH": 3,
      "orientation": "side"
    }
  ]
}
```

## File: `webview-ui/public/assets/furniture/SOFA/manifest.json`
```json
{
  "id": "SOFA",
  "name": "Sofa",
  "category": "chairs",
  "type": "group",
  "groupType": "rotation",
  "rotationScheme": "3-way-mirror",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "members": [
    {
      "type": "asset",
      "id": "SOFA_FRONT",
      "file": "SOFA_FRONT.png",
      "width": 32,
      "height": 16,
      "footprintW": 2,
      "footprintH": 1,
      "orientation": "front"
    },
    {
      "type": "asset",
      "id": "SOFA_BACK",
      "file": "SOFA_BACK.png",
      "width": 32,
      "height": 16,
      "footprintW": 2,
      "footprintH": 1,
      "orientation": "back"
    },
    {
      "type": "asset",
      "id": "SOFA_SIDE",
      "file": "SOFA_SIDE.png",
      "width": 16,
      "height": 32,
      "footprintW": 1,
      "footprintH": 2,
      "orientation": "side",
      "mirrorSide": true
    }
  ]
}
```

## File: `webview-ui/public/assets/furniture/TABLE_FRONT/manifest.json`
```json
{
  "id": "TABLE_FRONT",
  "name": "Table",
  "category": "desks",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 1,
  "width": 48,
  "height": 64,
  "footprintW": 3,
  "footprintH": 4
}
```

## File: `webview-ui/public/assets/furniture/WHITEBOARD/manifest.json`
```json
{
  "id": "WHITEBOARD",
  "name": "Whiteboard",
  "category": "wall",
  "type": "asset",
  "canPlaceOnWalls": true,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 32,
  "height": 32,
  "footprintW": 2,
  "footprintH": 2
}
```

## File: `webview-ui/public/assets/furniture/WOODEN_BENCH/manifest.json`
```json
{
  "id": "WOODEN_BENCH",
  "name": "Wooden Bench",
  "category": "chairs",
  "type": "asset",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 0,
  "width": 16,
  "height": 16,
  "footprintW": 1,
  "footprintH": 1
}
```

## File: `webview-ui/public/assets/furniture/WOODEN_CHAIR/manifest.json`
```json
{
  "id": "WOODEN_CHAIR",
  "name": "Wooden Chair",
  "category": "chairs",
  "type": "group",
  "groupType": "rotation",
  "rotationScheme": "3-way-mirror",
  "canPlaceOnWalls": false,
  "canPlaceOnSurfaces": false,
  "backgroundTiles": 1,
  "members": [
    {
      "type": "asset",
      "id": "WOODEN_CHAIR_FRONT",
      "file": "WOODEN_CHAIR_FRONT.png",
      "width": 16,
      "height": 32,
      "footprintW": 1,
      "footprintH": 2,
      "orientation": "front"
    },
    {
      "type": "asset",
      "id": "WOODEN_CHAIR_BACK",
      "file": "WOODEN_CHAIR_BACK.png",
      "width": 16,
      "height": 32,
      "footprintW": 1,
      "footprintH": 2,
      "orientation": "back"
    },
    {
      "type": "asset",
      "id": "WOODEN_CHAIR_SIDE",
      "file": "WOODEN_CHAIR_SIDE.png",
      "width": 16,
      "height": 32,
      "footprintW": 1,
      "footprintH": 2,
      "orientation": "side",
      "mirrorSide": true
    }
  ]
}
```

## File: `webview-ui/src/App.tsx`
```tsx
import { useCallback, useRef, useState } from 'react';

import { BottomToolbar } from './components/BottomToolbar.js';
import { DebugView } from './components/DebugView.js';
import { ZoomControls } from './components/ZoomControls.js';
import { PULSE_ANIMATION_DURATION_SEC } from './constants.js';
import { useEditorActions } from './hooks/useEditorActions.js';
import { useEditorKeyboard } from './hooks/useEditorKeyboard.js';
import { useExtensionMessages } from './hooks/useExtensionMessages.js';
import { OfficeCanvas } from './office/components/OfficeCanvas.js';
import { ToolOverlay } from './office/components/ToolOverlay.js';
import { EditorState } from './office/editor/editorState.js';
import { EditorToolbar } from './office/editor/EditorToolbar.js';
import { OfficeState } from './office/engine/officeState.js';
import { isRotatable } from './office/layout/furnitureCatalog.js';
import { EditTool } from './office/types.js';
import { vscode } from './vscodeApi.js';

// Game state lives outside React — updated imperatively by message handlers
const officeStateRef = { current: null as OfficeState | null };
const editorState = new EditorState();

function getOfficeState(): OfficeState {
  if (!officeStateRef.current) {
    officeStateRef.current = new OfficeState();
  }
  return officeStateRef.current;
}

const actionBarBtnStyle: React.CSSProperties = {
  padding: '4px 10px',
  fontSize: '22px',
  background: 'var(--pixel-btn-bg)',
  color: 'var(--pixel-text-dim)',
  border: '2px solid transparent',
  borderRadius: 0,
  cursor: 'pointer',
};

const actionBarBtnDisabled: React.CSSProperties = {
  ...actionBarBtnStyle,
  opacity: 'var(--pixel-btn-disabled-opacity)',
  cursor: 'default',
};

function EditActionBar({
  editor,
  editorState: es,
}: {
  editor: ReturnType<typeof useEditorActions>;
  editorState: EditorState;
}) {
  const [showResetConfirm, setShowResetConfirm] = useState(false);

  const undoDisabled = es.undoStack.length === 0;
  const redoDisabled = es.redoStack.length === 0;

  return (
    <div
      style={{
        position: 'absolute',
        top: 8,
        left: '50%',
        transform: 'translateX(-50%)',
        zIndex: 'var(--pixel-controls-z)',
        display: 'flex',
        gap: 4,
        alignItems: 'center',
        background: 'var(--pixel-bg)',
        border: '2px solid var(--pixel-border)',
        borderRadius: 0,
        padding: '4px 8px',
        boxShadow: 'var(--pixel-shadow)',
      }}
    >
      <button
        style={undoDisabled ? actionBarBtnDisabled : actionBarBtnStyle}
        onClick={undoDisabled ? undefined : editor.handleUndo}
        title="Undo (Ctrl+Z)"
      >
        Undo
      </button>
      <button
        style={redoDisabled ? actionBarBtnDisabled : actionBarBtnStyle}
        onClick={redoDisabled ? undefined : editor.handleRedo}
        title="Redo (Ctrl+Y)"
      >
        Redo
      </button>
      <button style={actionBarBtnStyle} onClick={editor.handleSave} title="Save layout">
        Save
      </button>
      {!showResetConfirm ? (
        <button
          style={actionBarBtnStyle}
          onClick={() => setShowResetConfirm(true)}
          title="Reset to last saved layout"
        >
          Reset
        </button>
      ) : (
        <div style={{ display: 'flex', gap: 4, alignItems: 'center' }}>
          <span style={{ fontSize: '22px', color: 'var(--pixel-reset-text)' }}>Reset?</span>
          <button
            style={{ ...actionBarBtnStyle, background: 'var(--pixel-danger-bg)', color: '#fff' }}
            onClick={() => {
              setShowResetConfirm(false);
              editor.handleReset();
            }}
          >
            Yes
          </button>
          <button style={actionBarBtnStyle} onClick={() => setShowResetConfirm(false)}>
            No
          </button>
        </div>
      )}
    </div>
  );
}

function App() {
  const editor = useEditorActions(getOfficeState, editorState);

  const isEditDirty = useCallback(
    () => editor.isEditMode && editor.isDirty,
    [editor.isEditMode, editor.isDirty],
  );

  const {
    agents,
    selectedAgent,
    agentTools,
    agentStatuses,
    subagentTools,
    subagentCharacters,
    layoutReady,
    layoutWasReset,
    loadedAssets,
    workspaceFolders,
  } = useExtensionMessages(getOfficeState, editor.setLastSavedLayout, isEditDirty);

  // Show migration notice once layout reset is detected
  const [migrationNoticeDismissed, setMigrationNoticeDismissed] = useState(false);
  const showMigrationNotice = layoutWasReset && !migrationNoticeDismissed;

  const [isDebugMode, setIsDebugMode] = useState(false);

  const handleToggleDebugMode = useCallback(() => setIsDebugMode((prev) => !prev), []);

  const handleSelectAgent = useCallback((id: number) => {
    vscode.postMessage({ type: 'focusAgent', id });
  }, []);

  const containerRef = useRef<HTMLDivElement>(null);

  const [editorTickForKeyboard, setEditorTickForKeyboard] = useState(0);
  useEditorKeyboard(
    editor.isEditMode,
    editorState,
    editor.handleDeleteSelected,
    editor.handleRotateSelected,
    editor.handleToggleState,
    editor.handleUndo,
    editor.handleRedo,
    useCallback(() => setEditorTickForKeyboard((n) => n + 1), []),
    editor.handleToggleEditMode,
  );

  const handleCloseAgent = useCallback((id: number) => {
    vscode.postMessage({ type: 'closeAgent', id });
  }, []);

  const handleClick = useCallback((agentId: number) => {
    // If clicked agent is a sub-agent, focus the parent's terminal instead
    const os = getOfficeState();
    const meta = os.subagentMeta.get(agentId);
    const focusId = meta ? meta.parentAgentId : agentId;
    vscode.postMessage({ type: 'focusAgent', id: focusId });
  }, []);

  const officeState = getOfficeState();

  // Force dependency on editorTickForKeyboard to propagate keyboard-triggered re-renders
  void editorTickForKeyboard;

  // Show "Press R to rotate" hint when a rotatable item is selected or being placed
  const showRotateHint =
    editor.isEditMode &&
    (() => {
      if (editorState.selectedFurnitureUid) {
        const item = officeState
          .getLayout()
          .furniture.find((f) => f.uid === editorState.selectedFurnitureUid);
        if (item && isRotatable(item.type)) return true;
      }
      if (
        editorState.activeTool === EditTool.FURNITURE_PLACE &&
        isRotatable(editorState.selectedFurnitureType)
      ) {
        return true;
      }
      return false;
    })();

  if (!layoutReady) {
    return (
      <div
        style={{
          width: '100%',
          height: '100%',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: 'var(--vscode-foreground)',
        }}
      >
        Loading...
      </div>
    );
  }

  return (
    <div
      ref={containerRef}
      style={{ width: '100%', height: '100%', position: 'relative', overflow: 'hidden' }}
    >
      <style>{`
        @keyframes pixel-agents-pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.3; }
        }
        .pixel-agents-pulse { animation: pixel-agents-pulse ${PULSE_ANIMATION_DURATION_SEC}s ease-in-out infinite; }
        .pixel-agents-migration-btn:hover { filter: brightness(0.8); }
      `}</style>

      <OfficeCanvas
        officeState={officeState}
        onClick={handleClick}
        isEditMode={editor.isEditMode}
        editorState={editorState}
        onEditorTileAction={editor.handleEditorTileAction}
        onEditorEraseAction={editor.handleEditorEraseAction}
        onEditorSelectionChange={editor.handleEditorSelectionChange}
        onDeleteSelected={editor.handleDeleteSelected}
        onRotateSelected={editor.handleRotateSelected}
        onDragMove={editor.handleDragMove}
        editorTick={editor.editorTick}
        zoom={editor.zoom}
        onZoomChange={editor.handleZoomChange}
        panRef={editor.panRef}
      />

      {!isDebugMode && <ZoomControls zoom={editor.zoom} onZoomChange={editor.handleZoomChange} />}

      {/* Vignette overlay */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          background: 'var(--pixel-vignette)',
          pointerEvents: 'none',
          zIndex: 40,
        }}
      />

      <BottomToolbar
        isEditMode={editor.isEditMode}
        onOpenClaude={editor.handleOpenClaude}
        onToggleEditMode={editor.handleToggleEditMode}
        isDebugMode={isDebugMode}
        onToggleDebugMode={handleToggleDebugMode}
        workspaceFolders={workspaceFolders}
      />

      {editor.isEditMode && editor.isDirty && (
        <EditActionBar editor={editor} editorState={editorState} />
      )}

      {showRotateHint && (
        <div
          style={{
            position: 'absolute',
            top: editor.isDirty ? 52 : 8,
            left: '50%',
            transform: 'translateX(-50%)',
            zIndex: 49,
            background: 'var(--pixel-hint-bg)',
            color: '#fff',
            fontSize: '20px',
            padding: '3px 8px',
            borderRadius: 0,
            border: '2px solid var(--pixel-accent)',
            boxShadow: 'var(--pixel-shadow)',
            pointerEvents: 'none',
            whiteSpace: 'nowrap',
          }}
        >
          Rotate (R)
        </div>
      )}

      {editor.isEditMode &&
        (() => {
          // Compute selected furniture color from current layout
          const selUid = editorState.selectedFurnitureUid;
          const selColor = selUid
            ? (officeState.getLayout().furniture.find((f) => f.uid === selUid)?.color ?? null)
            : null;
          return (
            <EditorToolbar
              activeTool={editorState.activeTool}
              selectedTileType={editorState.selectedTileType}
              selectedFurnitureType={editorState.selectedFurnitureType}
              selectedFurnitureUid={selUid}
              selectedFurnitureColor={selColor}
              floorColor={editorState.floorColor}
              wallColor={editorState.wallColor}
              selectedWallSet={editorState.selectedWallSet}
              onToolChange={editor.handleToolChange}
              onTileTypeChange={editor.handleTileTypeChange}
              onFloorColorChange={editor.handleFloorColorChange}
              onWallColorChange={editor.handleWallColorChange}
              onWallSetChange={editor.handleWallSetChange}
              onSelectedFurnitureColorChange={editor.handleSelectedFurnitureColorChange}
              onFurnitureTypeChange={editor.handleFurnitureTypeChange}
              loadedAssets={loadedAssets}
            />
          );
        })()}

      {!isDebugMode && (
        <ToolOverlay
          officeState={officeState}
          agents={agents}
          agentTools={agentTools}
          subagentCharacters={subagentCharacters}
          containerRef={containerRef}
          zoom={editor.zoom}
          panRef={editor.panRef}
          onCloseAgent={handleCloseAgent}
        />
      )}

      {isDebugMode && (
        <DebugView
          agents={agents}
          selectedAgent={selectedAgent}
          agentTools={agentTools}
          agentStatuses={agentStatuses}
          subagentTools={subagentTools}
          onSelectAgent={handleSelectAgent}
        />
      )}

      {showMigrationNotice && (
        <div
          style={{
            position: 'absolute',
            inset: 0,
            background: 'rgba(0, 0, 0, 0.7)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            zIndex: 100,
          }}
          onClick={() => setMigrationNoticeDismissed(true)}
        >
          <div
            style={{
              background: 'var(--pixel-bg)',
              border: '2px solid var(--pixel-border)',
              borderRadius: 0,
              padding: '24px 32px',
              maxWidth: 620,
              boxShadow: 'var(--pixel-shadow)',
              textAlign: 'center',
              lineHeight: 1.3,
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <div style={{ fontSize: '40px', marginBottom: 12, color: 'var(--pixel-accent)' }}>
              We owe you an apology!
            </div>
            <p style={{ fontSize: '26px', color: 'var(--pixel-text)', margin: '0 0 12px 0' }}>
              We've just migrated to fully open-source assets, all built from scratch with love.
              Unfortunately, this means your previous layout had to be reset.
            </p>
            <p style={{ fontSize: '26px', color: 'var(--pixel-text)', margin: '0 0 12px 0' }}>
              We're really sorry about that.
            </p>
            <p style={{ fontSize: '26px', color: 'var(--pixel-text)', margin: '0 0 12px 0' }}>
              The good news? This was a one-time thing, and it paves the way for some genuinely
              exciting updates ahead.
            </p>
            <p style={{ fontSize: '26px', color: 'var(--pixel-text-dim)', margin: '0 0 20px 0' }}>
              Stay tuned, and thanks for using Pixel Agents!
            </p>
            <button
              className="pixel-agents-migration-btn"
              style={{
                padding: '6px 24px 8px',
                fontSize: '30px',
                background: 'var(--pixel-accent)',
                color: '#fff',
                border: '2px solid var(--pixel-accent)',
                borderRadius: 0,
                cursor: 'pointer',
                boxShadow: 'var(--pixel-shadow)',
              }}
              onClick={() => setMigrationNoticeDismissed(true)}
            >
              Got it
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
```

## File: `webview-ui/src/constants.ts`
```typescript
import type { FloorColor } from './office/types.js';

// ── Grid & Layout ────────────────────────────────────────────
export const TILE_SIZE = 16;
export const DEFAULT_COLS = 20;
export const DEFAULT_ROWS = 11;
export const MAX_COLS = 64;
export const MAX_ROWS = 64;

// ── Character Animation ─────────────────────────────────────
export const WALK_SPEED_PX_PER_SEC = 48;
export const WALK_FRAME_DURATION_SEC = 0.15;
export const TYPE_FRAME_DURATION_SEC = 0.3;
export const WANDER_PAUSE_MIN_SEC = 2.0;
export const WANDER_PAUSE_MAX_SEC = 20.0;
export const WANDER_MOVES_BEFORE_REST_MIN = 3;
export const WANDER_MOVES_BEFORE_REST_MAX = 6;
export const SEAT_REST_MIN_SEC = 120.0;
export const SEAT_REST_MAX_SEC = 240.0;

// ── Matrix Effect ────────────────────────────────────────────
export const MATRIX_EFFECT_DURATION_SEC = 0.3;
export const MATRIX_TRAIL_LENGTH = 6;
export const MATRIX_SPRITE_COLS = 16;
export const MATRIX_SPRITE_ROWS = 24;
export const MATRIX_FLICKER_FPS = 30;
export const MATRIX_FLICKER_VISIBILITY_THRESHOLD = 180;
export const MATRIX_COLUMN_STAGGER_RANGE = 0.3;
export const MATRIX_HEAD_COLOR = '#ccffcc';
export const MATRIX_TRAIL_OVERLAY_ALPHA = 0.6;
export const MATRIX_TRAIL_EMPTY_ALPHA = 0.5;
export const MATRIX_TRAIL_MID_THRESHOLD = 0.33;
export const MATRIX_TRAIL_DIM_THRESHOLD = 0.66;

// ── Rendering ────────────────────────────────────────────────
export const CHARACTER_SITTING_OFFSET_PX = 6;
export const CHARACTER_Z_SORT_OFFSET = 0.5;
export const OUTLINE_Z_SORT_OFFSET = 0.001;
export const SELECTED_OUTLINE_ALPHA = 1.0;
export const HOVERED_OUTLINE_ALPHA = 0.5;
export const GHOST_PREVIEW_SPRITE_ALPHA = 0.5;
export const GHOST_PREVIEW_TINT_ALPHA = 0.25;
export const SELECTION_DASH_PATTERN: [number, number] = [4, 3];
export const BUTTON_MIN_RADIUS = 6;
export const BUTTON_RADIUS_ZOOM_FACTOR = 3;
export const BUTTON_ICON_SIZE_FACTOR = 0.45;
export const BUTTON_LINE_WIDTH_MIN = 1.5;
export const BUTTON_LINE_WIDTH_ZOOM_FACTOR = 0.5;
export const BUBBLE_FADE_DURATION_SEC = 0.5;
export const BUBBLE_SITTING_OFFSET_PX = 10;
export const BUBBLE_VERTICAL_OFFSET_PX = 24;
export const FALLBACK_FLOOR_COLOR = '#808080';

// ── Rendering - Overlay Colors (canvas, not CSS) ─────────────
export const SEAT_OWN_COLOR = 'rgba(0, 127, 212, 0.35)';
export const SEAT_AVAILABLE_COLOR = 'rgba(0, 200, 80, 0.35)';
export const SEAT_BUSY_COLOR = 'rgba(220, 50, 50, 0.35)';
export const GRID_LINE_COLOR = 'rgba(255,255,255,0.12)';
export const VOID_TILE_OUTLINE_COLOR = 'rgba(255,255,255,0.08)';
export const VOID_TILE_DASH_PATTERN: [number, number] = [2, 2];
export const GHOST_BORDER_HOVER_FILL = 'rgba(60, 130, 220, 0.25)';
export const GHOST_BORDER_HOVER_STROKE = 'rgba(60, 130, 220, 0.5)';
export const GHOST_BORDER_STROKE = 'rgba(255, 255, 255, 0.06)';
export const GHOST_VALID_TINT = '#00ff00';
export const GHOST_INVALID_TINT = '#ff0000';
export const SELECTION_HIGHLIGHT_COLOR = '#007fd4';
export const DELETE_BUTTON_BG = 'rgba(200, 50, 50, 0.85)';
export const ROTATE_BUTTON_BG = 'rgba(50, 120, 200, 0.85)';

// ── Camera ───────────────────────────────────────────────────
export const CAMERA_FOLLOW_LERP = 0.1;
export const CAMERA_FOLLOW_SNAP_THRESHOLD = 0.5;

// ── Zoom ─────────────────────────────────────────────────────
export const ZOOM_MIN = 1;
export const ZOOM_MAX = 10;
export const ZOOM_DEFAULT_DPR_FACTOR = 2;
export const ZOOM_LEVEL_FADE_DELAY_MS = 1500;
export const ZOOM_LEVEL_HIDE_DELAY_MS = 2000;
export const ZOOM_LEVEL_FADE_DURATION_SEC = 0.5;
export const ZOOM_SCROLL_THRESHOLD = 50;
export const PAN_MARGIN_FRACTION = 0.25;

// ── Editor ───────────────────────────────────────────────────
export const UNDO_STACK_MAX_SIZE = 50;
export const LAYOUT_SAVE_DEBOUNCE_MS = 500;
export const DEFAULT_FLOOR_COLOR: FloorColor = { h: 35, s: 30, b: 15, c: 0 };
export const DEFAULT_WALL_COLOR: FloorColor = { h: 240, s: 25, b: 0, c: 0 };
export const DEFAULT_NEUTRAL_COLOR: FloorColor = { h: 0, s: 0, b: 0, c: 0 };

// ── Notification Sound ──────────────────────────────────────
export const NOTIFICATION_NOTE_1_HZ = 659.25; // E5
export const NOTIFICATION_NOTE_2_HZ = 1318.51; // E6 (octave up)
export const NOTIFICATION_NOTE_1_START_SEC = 0;
export const NOTIFICATION_NOTE_2_START_SEC = 0.1;
export const NOTIFICATION_NOTE_DURATION_SEC = 0.18;
export const NOTIFICATION_VOLUME = 0.14;

// ── Furniture Animation ─────────────────────────────────────
export const FURNITURE_ANIM_INTERVAL_SEC = 0.2;

// ── Game Logic ───────────────────────────────────────────────
export const MAX_DELTA_TIME_SEC = 0.1;
export const WAITING_BUBBLE_DURATION_SEC = 2.0;
export const DISMISS_BUBBLE_FAST_FADE_SEC = 0.3;
export const INACTIVE_SEAT_TIMER_MIN_SEC = 3.0;
export const INACTIVE_SEAT_TIMER_RANGE_SEC = 2.0;
export const PALETTE_COUNT = 6;
export const HUE_SHIFT_MIN_DEG = 45;
export const HUE_SHIFT_RANGE_DEG = 271;
export const AUTO_ON_FACING_DEPTH = 3;
export const AUTO_ON_SIDE_DEPTH = 2;
export const CHARACTER_HIT_HALF_WIDTH = 8;
export const CHARACTER_HIT_HEIGHT = 24;
export const TOOL_OVERLAY_VERTICAL_OFFSET = 32;
export const PULSE_ANIMATION_DURATION_SEC = 1.5;
```

## File: `webview-ui/src/index.css`
```css
@font-face {
  font-family: 'FS Pixel Sans';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('/fonts/FSPixelSansUnicode-Regular.ttf') format('truetype');
}

:root {
  --pixel-bg: #1e1e2e;
  --pixel-border: #4a4a6a;
  --pixel-border-light: #6a6a8a;
  --pixel-accent: #5a8cff;
  --pixel-green: #5ac88c;
  --pixel-shadow: 2px 2px 0px #0a0a14;

  /* Button base */
  --pixel-text: rgba(255, 255, 255, 0.8);
  --pixel-text-dim: rgba(255, 255, 255, 0.7);
  --pixel-btn-bg: rgba(255, 255, 255, 0.08);
  --pixel-btn-hover-bg: rgba(255, 255, 255, 0.15);
  --pixel-btn-disabled-opacity: 0.35;

  /* Active/selected button state */
  --pixel-active-bg: rgba(90, 140, 255, 0.25);

  /* Agent button */
  --pixel-agent-bg: rgba(90, 200, 140, 0.15);
  --pixel-agent-hover-bg: rgba(90, 200, 140, 0.3);
  --pixel-agent-border: #5ac88c;
  --pixel-agent-text: rgba(200, 255, 220, 0.95);

  /* Close button */
  --pixel-close-text: rgba(255, 255, 255, 0.5);
  --pixel-close-hover: #e55;

  /* Hints & confirmations */
  --pixel-hint-bg: #3278c8;
  --pixel-reset-text: #ecc;
  --pixel-danger-bg: #a33;

  /* Vignette */
  --pixel-vignette: radial-gradient(ellipse at center, transparent 50%, rgba(0, 0, 0, 0.6) 100%);

  /* Status dot colors */
  --pixel-status-permission: var(--vscode-charts-yellow, #cca700);
  --pixel-status-active: var(--vscode-charts-blue, #3794ff);

  /* ToolOverlay z-index layers */
  --pixel-overlay-z: 41;
  --pixel-overlay-selected-z: 42;
  --pixel-controls-z: 50;
}

html,
body,
#root {
  margin: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  font-family: 'FS Pixel Sans', sans-serif;
}

* {
  font-family: 'FS Pixel Sans', sans-serif;
}
```

## File: `webview-ui/src/main.tsx`
```tsx
import './index.css';

import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

import App from './App.tsx';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
```

## File: `webview-ui/src/notificationSound.ts`
```typescript
import {
  NOTIFICATION_NOTE_1_HZ,
  NOTIFICATION_NOTE_1_START_SEC,
  NOTIFICATION_NOTE_2_HZ,
  NOTIFICATION_NOTE_2_START_SEC,
  NOTIFICATION_NOTE_DURATION_SEC,
  NOTIFICATION_VOLUME,
} from './constants.js';

let soundEnabled = true;
let audioCtx: AudioContext | null = null;

export function setSoundEnabled(enabled: boolean): void {
  soundEnabled = enabled;
}

export function isSoundEnabled(): boolean {
  return soundEnabled;
}

function playNote(ctx: AudioContext, freq: number, startOffset: number): void {
  const t = ctx.currentTime + startOffset;
  const osc = ctx.createOscillator();
  const gain = ctx.createGain();

  osc.type = 'sine';
  osc.frequency.setValueAtTime(freq, t);

  gain.gain.setValueAtTime(NOTIFICATION_VOLUME, t);
  gain.gain.exponentialRampToValueAtTime(0.001, t + NOTIFICATION_NOTE_DURATION_SEC);

  osc.connect(gain);
  gain.connect(ctx.destination);

  osc.start(t);
  osc.stop(t + NOTIFICATION_NOTE_DURATION_SEC);
}

export async function playDoneSound(): Promise<void> {
  if (!soundEnabled) return;
  try {
    if (!audioCtx) {
      audioCtx = new AudioContext();
    }
    // Resume suspended context (webviews suspend until user gesture)
    if (audioCtx.state === 'suspended') {
      await audioCtx.resume();
    }
    // Ascending two-note chime: E5 → B5
    playNote(audioCtx, NOTIFICATION_NOTE_1_HZ, NOTIFICATION_NOTE_1_START_SEC);
    playNote(audioCtx, NOTIFICATION_NOTE_2_HZ, NOTIFICATION_NOTE_2_START_SEC);
  } catch {
    // Audio may not be available
  }
}

/** Call from any user-gesture handler to ensure AudioContext is unlocked */
export function unlockAudio(): void {
  try {
    if (!audioCtx) {
      audioCtx = new AudioContext();
    }
    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }
  } catch {
    // ignore
  }
}
```

## File: `webview-ui/src/vscodeApi.ts`
```typescript
declare function acquireVsCodeApi(): { postMessage(msg: unknown): void };

export const vscode = acquireVsCodeApi();
```

## File: `webview-ui/src/components/AgentLabels.tsx`
```tsx
import { useEffect, useState } from 'react';

import type { SubagentCharacter } from '../hooks/useExtensionMessages.js';
import type { OfficeState } from '../office/engine/officeState.js';
import { CharacterState, TILE_SIZE } from '../office/types.js';

interface AgentLabelsProps {
  officeState: OfficeState;
  agents: number[];
  agentStatuses: Record<number, string>;
  containerRef: React.RefObject<HTMLDivElement | null>;
  zoom: number;
  panRef: React.RefObject<{ x: number; y: number }>;
  subagentCharacters: SubagentCharacter[];
}

export function AgentLabels({
  officeState,
  agents,
  agentStatuses,
  containerRef,
  zoom,
  panRef,
  subagentCharacters,
}: AgentLabelsProps) {
  const [, setTick] = useState(0);
  useEffect(() => {
    let rafId = 0;
    const tick = () => {
      setTick((n) => n + 1);
      rafId = requestAnimationFrame(tick);
    };
    rafId = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(rafId);
  }, []);

  const el = containerRef.current;
  if (!el) return null;
  const rect = el.getBoundingClientRect();
  const dpr = window.devicePixelRatio || 1;
  // Compute device pixel offset (same math as renderFrame, including pan)
  const canvasW = Math.round(rect.width * dpr);
  const canvasH = Math.round(rect.height * dpr);
  const layout = officeState.getLayout();
  const mapW = layout.cols * TILE_SIZE * zoom;
  const mapH = layout.rows * TILE_SIZE * zoom;
  const deviceOffsetX = Math.floor((canvasW - mapW) / 2) + Math.round(panRef.current.x);
  const deviceOffsetY = Math.floor((canvasH - mapH) / 2) + Math.round(panRef.current.y);

  // Build sub-agent label lookup
  const subLabelMap = new Map<number, string>();
  for (const sub of subagentCharacters) {
    subLabelMap.set(sub.id, sub.label);
  }

  // All character IDs to render labels for (regular agents + sub-agents)
  const allIds = [...agents, ...subagentCharacters.map((s) => s.id)];

  return (
    <>
      {allIds.map((id) => {
        const ch = officeState.characters.get(id);
        if (!ch) return null;

        // Character position: device pixels → CSS pixels (follow sitting offset)
        const sittingOffset = ch.state === CharacterState.TYPE ? 6 : 0;
        const screenX = (deviceOffsetX + ch.x * zoom) / dpr;
        const screenY = (deviceOffsetY + (ch.y + sittingOffset - 24) * zoom) / dpr;

        const status = agentStatuses[id];
        const isWaiting = status === 'waiting';
        const isActive = ch.isActive;
        const isSub = ch.isSubagent;

        let dotColor = 'transparent';
        if (isWaiting) {
          dotColor = 'var(--vscode-charts-yellow, #cca700)';
        } else if (isActive) {
          dotColor = 'var(--vscode-charts-blue, #3794ff)';
        }

        const labelText = subLabelMap.get(id) || `Agent #${id}`;

        return (
          <div
            key={id}
            style={{
              position: 'absolute',
              left: screenX,
              top: screenY - 16,
              transform: 'translateX(-50%)',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              pointerEvents: 'none',
              zIndex: 40,
            }}
          >
            {dotColor !== 'transparent' && (
              <span
                className={isActive && !isWaiting ? 'pixel-agents-pulse' : undefined}
                style={{
                  width: 6,
                  height: 6,
                  borderRadius: '50%',
                  background: dotColor,
                  marginBottom: 2,
                }}
              />
            )}
            <span
              style={{
                fontSize: isSub ? '16px' : '18px',
                fontStyle: isSub ? 'italic' : undefined,
                color: 'var(--vscode-foreground)',
                background: 'rgba(30,30,46,0.7)',
                padding: '1px 4px',
                borderRadius: 2,
                whiteSpace: 'nowrap',
                maxWidth: isSub ? 120 : undefined,
                overflow: isSub ? 'hidden' : undefined,
                textOverflow: isSub ? 'ellipsis' : undefined,
              }}
            >
              {labelText}
            </span>
          </div>
        );
      })}
    </>
  );
}
```

## File: `webview-ui/src/components/BottomToolbar.tsx`
```tsx
import { useEffect, useRef, useState } from 'react';

import type { WorkspaceFolder } from '../hooks/useExtensionMessages.js';
import { vscode } from '../vscodeApi.js';
import { SettingsModal } from './SettingsModal.js';

interface BottomToolbarProps {
  isEditMode: boolean;
  onOpenClaude: () => void;
  onToggleEditMode: () => void;
  isDebugMode: boolean;
  onToggleDebugMode: () => void;
  workspaceFolders: WorkspaceFolder[];
}

const panelStyle: React.CSSProperties = {
  position: 'absolute',
  bottom: 10,
  left: 10,
  zIndex: 'var(--pixel-controls-z)',
  display: 'flex',
  alignItems: 'center',
  gap: 4,
  background: 'var(--pixel-bg)',
  border: '2px solid var(--pixel-border)',
  borderRadius: 0,
  padding: '4px 6px',
  boxShadow: 'var(--pixel-shadow)',
};

const btnBase: React.CSSProperties = {
  padding: '5px 10px',
  fontSize: '24px',
  color: 'var(--pixel-text)',
  background: 'var(--pixel-btn-bg)',
  border: '2px solid transparent',
  borderRadius: 0,
  cursor: 'pointer',
};

const btnActive: React.CSSProperties = {
  ...btnBase,
  background: 'var(--pixel-active-bg)',
  border: '2px solid var(--pixel-accent)',
};

export function BottomToolbar({
  isEditMode,
  onOpenClaude,
  onToggleEditMode,
  isDebugMode,
  onToggleDebugMode,
  workspaceFolders,
}: BottomToolbarProps) {
  const [hovered, setHovered] = useState<string | null>(null);
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [isFolderPickerOpen, setIsFolderPickerOpen] = useState(false);
  const [hoveredFolder, setHoveredFolder] = useState<number | null>(null);
  const folderPickerRef = useRef<HTMLDivElement>(null);

  // Close folder picker on outside click
  useEffect(() => {
    if (!isFolderPickerOpen) return;
    const handleClick = (e: MouseEvent) => {
      if (folderPickerRef.current && !folderPickerRef.current.contains(e.target as Node)) {
        setIsFolderPickerOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClick);
    return () => document.removeEventListener('mousedown', handleClick);
  }, [isFolderPickerOpen]);

  const hasMultipleFolders = workspaceFolders.length > 1;

  const handleAgentClick = () => {
    if (hasMultipleFolders) {
      setIsFolderPickerOpen((v) => !v);
    } else {
      onOpenClaude();
    }
  };

  const handleFolderSelect = (folder: WorkspaceFolder) => {
    setIsFolderPickerOpen(false);
    vscode.postMessage({ type: 'openClaude', folderPath: folder.path });
  };

  return (
    <div style={panelStyle}>
      <div ref={folderPickerRef} style={{ position: 'relative' }}>
        <button
          onClick={handleAgentClick}
          onMouseEnter={() => setHovered('agent')}
          onMouseLeave={() => setHovered(null)}
          style={{
            ...btnBase,
            padding: '5px 12px',
            background:
              hovered === 'agent' || isFolderPickerOpen
                ? 'var(--pixel-agent-hover-bg)'
                : 'var(--pixel-agent-bg)',
            border: '2px solid var(--pixel-agent-border)',
            color: 'var(--pixel-agent-text)',
          }}
        >
          + Agent
        </button>
        {isFolderPickerOpen && (
          <div
            style={{
              position: 'absolute',
              bottom: '100%',
              left: 0,
              marginBottom: 4,
              background: 'var(--pixel-bg)',
              border: '2px solid var(--pixel-border)',
              borderRadius: 0,
              boxShadow: 'var(--pixel-shadow)',
              minWidth: 160,
              zIndex: 'var(--pixel-controls-z)',
            }}
          >
            {workspaceFolders.map((folder, i) => (
              <button
                key={folder.path}
                onClick={() => handleFolderSelect(folder)}
                onMouseEnter={() => setHoveredFolder(i)}
                onMouseLeave={() => setHoveredFolder(null)}
                style={{
                  display: 'block',
                  width: '100%',
                  textAlign: 'left',
                  padding: '6px 10px',
                  fontSize: '22px',
                  color: 'var(--pixel-text)',
                  background: hoveredFolder === i ? 'var(--pixel-btn-hover-bg)' : 'transparent',
                  border: 'none',
                  borderRadius: 0,
                  cursor: 'pointer',
                  whiteSpace: 'nowrap',
                }}
              >
                {folder.name}
              </button>
            ))}
          </div>
        )}
      </div>
      <button
        onClick={onToggleEditMode}
        onMouseEnter={() => setHovered('edit')}
        onMouseLeave={() => setHovered(null)}
        style={
          isEditMode
            ? { ...btnActive }
            : {
                ...btnBase,
                background: hovered === 'edit' ? 'var(--pixel-btn-hover-bg)' : btnBase.background,
              }
        }
        title="Edit office layout"
      >
        Layout
      </button>
      <div style={{ position: 'relative' }}>
        <button
          onClick={() => setIsSettingsOpen((v) => !v)}
          onMouseEnter={() => setHovered('settings')}
          onMouseLeave={() => setHovered(null)}
          style={
            isSettingsOpen
              ? { ...btnActive }
              : {
                  ...btnBase,
                  background:
                    hovered === 'settings' ? 'var(--pixel-btn-hover-bg)' : btnBase.background,
                }
          }
          title="Settings"
        >
          Settings
        </button>
        <SettingsModal
          isOpen={isSettingsOpen}
          onClose={() => setIsSettingsOpen(false)}
          isDebugMode={isDebugMode}
          onToggleDebugMode={onToggleDebugMode}
        />
      </div>
    </div>
  );
}
```

## File: `webview-ui/src/components/DebugView.tsx`
```tsx
import type { ToolActivity } from '../office/types.js';
import { vscode } from '../vscodeApi.js';

interface DebugViewProps {
  agents: number[];
  selectedAgent: number | null;
  agentTools: Record<number, ToolActivity[]>;
  agentStatuses: Record<number, string>;
  subagentTools: Record<number, Record<string, ToolActivity[]>>;
  onSelectAgent: (id: number) => void;
}

/** Z-index just below the floating toolbar (50) so the toolbar stays on top */
const DEBUG_Z = 40;

function ToolDot({ tool }: { tool: ToolActivity }) {
  return (
    <span
      className={tool.done ? undefined : 'pixel-agents-pulse'}
      style={{
        width: 6,
        height: 6,
        borderRadius: '50%',
        background: tool.done
          ? 'var(--vscode-charts-green, #89d185)'
          : tool.permissionWait
            ? 'var(--vscode-charts-yellow, #cca700)'
            : 'var(--vscode-charts-blue, #3794ff)',
        display: 'inline-block',
        flexShrink: 0,
      }}
    />
  );
}

function ToolLine({ tool }: { tool: ToolActivity }) {
  return (
    <span
      style={{
        fontSize: '22px',
        opacity: tool.done ? 0.5 : 0.8,
        display: 'flex',
        alignItems: 'center',
        gap: 5,
      }}
    >
      <ToolDot tool={tool} />
      {tool.permissionWait && !tool.done ? 'Needs approval' : tool.status}
    </span>
  );
}

export function DebugView({
  agents,
  selectedAgent,
  agentTools,
  agentStatuses,
  subagentTools,
  onSelectAgent,
}: DebugViewProps) {
  const renderAgentCard = (id: number) => {
    const isSelected = selectedAgent === id;
    const tools = agentTools[id] || [];
    const subs = subagentTools[id] || {};
    const status = agentStatuses[id];
    const hasActiveTools = tools.some((t) => !t.done);
    return (
      <div
        key={id}
        style={{
          border: `2px solid ${isSelected ? '#5a8cff' : '#4a4a6a'}`,
          borderRadius: 0,
          padding: '6px 8px',
          background: isSelected
            ? 'var(--vscode-list-activeSelectionBackground, rgba(255,255,255,0.04))'
            : undefined,
        }}
      >
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: 0 }}>
          <button
            onClick={() => onSelectAgent(id)}
            style={{
              borderRadius: 0,
              padding: '6px 10px',
              fontSize: '26px',
              background: isSelected ? 'rgba(90, 140, 255, 0.25)' : undefined,
              color: isSelected ? '#fff' : undefined,
              fontWeight: isSelected ? 'bold' : undefined,
            }}
          >
            Agent #{id}
          </button>
          <button
            onClick={() => vscode.postMessage({ type: 'closeAgent', id })}
            style={{
              borderRadius: 0,
              padding: '6px 8px',
              fontSize: '26px',
              opacity: 0.7,
              background: isSelected ? 'rgba(90, 140, 255, 0.25)' : undefined,
              color: isSelected ? '#fff' : undefined,
            }}
            title="Close agent"
          >
            ✕
          </button>
        </span>
        {(tools.length > 0 || status === 'waiting') && (
          <div
            style={{
              display: 'flex',
              flexDirection: 'column',
              gap: 1,
              marginTop: 4,
              paddingLeft: 4,
            }}
          >
            {tools.map((tool) => (
              <div key={tool.toolId}>
                <ToolLine tool={tool} />
                {subs[tool.toolId] && subs[tool.toolId].length > 0 && (
                  <div
                    style={{
                      borderLeft: '2px solid var(--vscode-widget-border, rgba(255,255,255,0.12))',
                      marginLeft: 3,
                      paddingLeft: 8,
                      marginTop: 1,
                      display: 'flex',
                      flexDirection: 'column',
                      gap: 1,
                    }}
                  >
                    {subs[tool.toolId].map((subTool) => (
                      <ToolLine key={subTool.toolId} tool={subTool} />
                    ))}
                  </div>
                )}
              </div>
            ))}
            {status === 'waiting' && !hasActiveTools && (
              <span
                style={{
                  fontSize: '22px',
                  opacity: 0.85,
                  display: 'flex',
                  alignItems: 'center',
                  gap: 5,
                }}
              >
                <span
                  style={{
                    width: 6,
                    height: 6,
                    borderRadius: '50%',
                    background: 'var(--vscode-charts-yellow, #cca700)',
                    display: 'inline-block',
                    flexShrink: 0,
                  }}
                />
                Might be waiting for input
              </span>
            )}
          </div>
        )}
      </div>
    );
  };

  return (
    <div
      style={{
        position: 'absolute',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        background: 'var(--vscode-editor-background)',
        zIndex: DEBUG_Z,
        overflow: 'auto',
      }}
    >
      {/* Top padding so cards don't overlap the floating toolbar */}
      <div style={{ padding: '12px 12px 12px', fontSize: '28px' }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
          {agents.map(renderAgentCard)}
        </div>
      </div>
    </div>
  );
}
```

## File: `webview-ui/src/components/SettingsModal.tsx`
```tsx
import { useState } from 'react';

import { isSoundEnabled, setSoundEnabled } from '../notificationSound.js';
import { vscode } from '../vscodeApi.js';

interface SettingsModalProps {
  isOpen: boolean;
  onClose: () => void;
  isDebugMode: boolean;
  onToggleDebugMode: () => void;
}

const menuItemBase: React.CSSProperties = {
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-between',
  width: '100%',
  padding: '6px 10px',
  fontSize: '24px',
  color: 'rgba(255, 255, 255, 0.8)',
  background: 'transparent',
  border: 'none',
  borderRadius: 0,
  cursor: 'pointer',
  textAlign: 'left',
};

export function SettingsModal({
  isOpen,
  onClose,
  isDebugMode,
  onToggleDebugMode,
}: SettingsModalProps) {
  const [hovered, setHovered] = useState<string | null>(null);
  const [soundLocal, setSoundLocal] = useState(isSoundEnabled);

  if (!isOpen) return null;

  return (
    <>
      {/* Dark backdrop — click to close */}
      <div
        onClick={onClose}
        style={{
          position: 'fixed',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          background: 'rgba(0, 0, 0, 0.5)',
          zIndex: 49,
        }}
      />
      {/* Centered modal */}
      <div
        style={{
          position: 'fixed',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          zIndex: 50,
          background: 'var(--pixel-bg)',
          border: '2px solid var(--pixel-border)',
          borderRadius: 0,
          padding: '4px',
          boxShadow: 'var(--pixel-shadow)',
          minWidth: 200,
        }}
      >
        {/* Header with title and X button */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            padding: '4px 10px',
            borderBottom: '1px solid var(--pixel-border)',
            marginBottom: '4px',
          }}
        >
          <span style={{ fontSize: '24px', color: 'rgba(255, 255, 255, 0.9)' }}>Settings</span>
          <button
            onClick={onClose}
            onMouseEnter={() => setHovered('close')}
            onMouseLeave={() => setHovered(null)}
            style={{
              background: hovered === 'close' ? 'rgba(255, 255, 255, 0.08)' : 'transparent',
              border: 'none',
              borderRadius: 0,
              color: 'rgba(255, 255, 255, 0.6)',
              fontSize: '24px',
              cursor: 'pointer',
              padding: '0 4px',
              lineHeight: 1,
            }}
          >
            X
          </button>
        </div>
        {/* Menu items */}
        <button
          onClick={() => {
            vscode.postMessage({ type: 'openSessionsFolder' });
            onClose();
          }}
          onMouseEnter={() => setHovered('sessions')}
          onMouseLeave={() => setHovered(null)}
          style={{
            ...menuItemBase,
            background: hovered === 'sessions' ? 'rgba(255, 255, 255, 0.08)' : 'transparent',
          }}
        >
          Open Sessions Folder
        </button>
        <button
          onClick={() => {
            vscode.postMessage({ type: 'exportLayout' });
            onClose();
          }}
          onMouseEnter={() => setHovered('export')}
          onMouseLeave={() => setHovered(null)}
          style={{
            ...menuItemBase,
            background: hovered === 'export' ? 'rgba(255, 255, 255, 0.08)' : 'transparent',
          }}
        >
          Export Layout
        </button>
        <button
          onClick={() => {
            vscode.postMessage({ type: 'importLayout' });
            onClose();
          }}
          onMouseEnter={() => setHovered('import')}
          onMouseLeave={() => setHovered(null)}
          style={{
            ...menuItemBase,
            background: hovered === 'import' ? 'rgba(255, 255, 255, 0.08)' : 'transparent',
          }}
        >
          Import Layout
        </button>
        <button
          onClick={() => {
            const newVal = !isSoundEnabled();
            setSoundEnabled(newVal);
            setSoundLocal(newVal);
            vscode.postMessage({ type: 'setSoundEnabled', enabled: newVal });
          }}
          onMouseEnter={() => setHovered('sound')}
          onMouseLeave={() => setHovered(null)}
          style={{
            ...menuItemBase,
            background: hovered === 'sound' ? 'rgba(255, 255, 255, 0.08)' : 'transparent',
          }}
        >
          <span>Sound Notifications</span>
          <span
            style={{
              width: 14,
              height: 14,
              border: '2px solid rgba(255, 255, 255, 0.5)',
              borderRadius: 0,
              background: soundLocal ? 'rgba(90, 140, 255, 0.8)' : 'transparent',
              flexShrink: 0,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '12px',
              lineHeight: 1,
              color: '#fff',
            }}
          >
            {soundLocal ? 'X' : ''}
          </span>
        </button>
        <button
          onClick={onToggleDebugMode}
          onMouseEnter={() => setHovered('debug')}
          onMouseLeave={() => setHovered(null)}
          style={{
            ...menuItemBase,
            background: hovered === 'debug' ? 'rgba(255, 255, 255, 0.08)' : 'transparent',
          }}
        >
          <span>Debug View</span>
          {isDebugMode && (
            <span
              style={{
                width: 6,
                height: 6,
                borderRadius: '50%',
                background: 'rgba(90, 140, 255, 0.8)',
                flexShrink: 0,
              }}
            />
          )}
        </button>
      </div>
    </>
  );
}
```

## File: `webview-ui/src/components/ZoomControls.tsx`
```tsx
import { useEffect, useRef, useState } from 'react';

import {
  ZOOM_LEVEL_FADE_DELAY_MS,
  ZOOM_LEVEL_FADE_DURATION_SEC,
  ZOOM_LEVEL_HIDE_DELAY_MS,
  ZOOM_MAX,
  ZOOM_MIN,
} from '../constants.js';

interface ZoomControlsProps {
  zoom: number;
  onZoomChange: (zoom: number) => void;
}

const btnBase: React.CSSProperties = {
  width: 40,
  height: 40,
  padding: 0,
  background: 'var(--pixel-bg)',
  color: 'var(--pixel-text)',
  border: '2px solid var(--pixel-border)',
  borderRadius: 0,
  cursor: 'pointer',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  boxShadow: 'var(--pixel-shadow)',
};

export function ZoomControls({ zoom, onZoomChange }: ZoomControlsProps) {
  const [hovered, setHovered] = useState<'minus' | 'plus' | null>(null);
  const [showLevel, setShowLevel] = useState(false);
  const [fadeOut, setFadeOut] = useState(false);
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const fadeTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const prevZoomRef = useRef(zoom);

  const minDisabled = zoom <= ZOOM_MIN;
  const maxDisabled = zoom >= ZOOM_MAX;

  // Show zoom level briefly when zoom changes
  useEffect(() => {
    if (zoom === prevZoomRef.current) return;
    prevZoomRef.current = zoom;

    // Clear existing timers
    if (timerRef.current) clearTimeout(timerRef.current);
    if (fadeTimerRef.current) clearTimeout(fadeTimerRef.current);

    setShowLevel(true);
    setFadeOut(false);

    // Start fade after delay
    fadeTimerRef.current = setTimeout(() => {
      setFadeOut(true);
    }, ZOOM_LEVEL_FADE_DELAY_MS);

    // Hide completely after delay
    timerRef.current = setTimeout(() => {
      setShowLevel(false);
      setFadeOut(false);
    }, ZOOM_LEVEL_HIDE_DELAY_MS);

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
      if (fadeTimerRef.current) clearTimeout(fadeTimerRef.current);
    };
  }, [zoom]);

  return (
    <>
      {/* Zoom level indicator at top-center */}
      {showLevel && (
        <div
          style={{
            position: 'absolute',
            top: 10,
            left: '50%',
            transform: 'translateX(-50%)',
            zIndex: 'var(--pixel-controls-z)',
            background: 'var(--pixel-bg)',
            border: '2px solid var(--pixel-border)',
            borderRadius: 0,
            padding: '4px 12px',
            boxShadow: 'var(--pixel-shadow)',
            fontSize: '26px',
            color: 'var(--pixel-text)',
            userSelect: 'none',
            opacity: fadeOut ? 0 : 1,
            transition: `opacity ${ZOOM_LEVEL_FADE_DURATION_SEC}s ease-out`,
            pointerEvents: 'none',
          }}
        >
          {zoom}x
        </div>
      )}

      {/* Vertically stacked round buttons — top-left */}
      <div
        style={{
          position: 'absolute',
          top: 8,
          left: 8,
          zIndex: 'var(--pixel-controls-z)',
          display: 'flex',
          flexDirection: 'column',
          gap: 4,
        }}
      >
        <button
          onClick={() => onZoomChange(zoom + 1)}
          disabled={maxDisabled}
          onMouseEnter={() => setHovered('plus')}
          onMouseLeave={() => setHovered(null)}
          style={{
            ...btnBase,
            background:
              hovered === 'plus' && !maxDisabled ? 'var(--pixel-btn-hover-bg)' : btnBase.background,
            cursor: maxDisabled ? 'default' : 'pointer',
            opacity: maxDisabled ? 'var(--pixel-btn-disabled-opacity)' : 1,
          }}
          title="Zoom in (Ctrl+Scroll)"
        >
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <line
              x1="9"
              y1="3"
              x2="9"
              y2="15"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
            />
            <line
              x1="3"
              y1="9"
              x2="15"
              y2="9"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
            />
          </svg>
        </button>
        <button
          onClick={() => onZoomChange(zoom - 1)}
          disabled={minDisabled}
          onMouseEnter={() => setHovered('minus')}
          onMouseLeave={() => setHovered(null)}
          style={{
            ...btnBase,
            background:
              hovered === 'minus' && !minDisabled
                ? 'var(--pixel-btn-hover-bg)'
                : btnBase.background,
            cursor: minDisabled ? 'default' : 'pointer',
            opacity: minDisabled ? 'var(--pixel-btn-disabled-opacity)' : 1,
          }}
          title="Zoom out (Ctrl+Scroll)"
        >
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <line
              x1="3"
              y1="9"
              x2="15"
              y2="9"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
            />
          </svg>
        </button>
      </div>
    </>
  );
}
```

## File: `webview-ui/src/hooks/useEditorActions.ts`
```typescript
import { useCallback, useRef, useState } from 'react';

import { LAYOUT_SAVE_DEBOUNCE_MS, ZOOM_MAX, ZOOM_MIN } from '../constants.js';
import type { ExpandDirection } from '../office/editor/editorActions.js';
import {
  canPlaceFurniture,
  expandLayout,
  getWallPlacementRow,
  moveFurniture,
  paintTile,
  placeFurniture,
  removeFurniture,
  rotateFurniture,
  toggleFurnitureState,
} from '../office/editor/editorActions.js';
import type { EditorState } from '../office/editor/editorState.js';
import type { OfficeState } from '../office/engine/officeState.js';
import {
  getCatalogEntry,
  getRotatedType,
  getToggledType,
} from '../office/layout/furnitureCatalog.js';
import { defaultZoom } from '../office/toolUtils.js';
import type {
  EditTool as EditToolType,
  FloorColor,
  OfficeLayout,
  PlacedFurniture,
  TileType as TileTypeVal,
} from '../office/types.js';
import { EditTool } from '../office/types.js';
import { TileType } from '../office/types.js';
import { vscode } from '../vscodeApi.js';

export interface EditorActions {
  isEditMode: boolean;
  editorTick: number;
  isDirty: boolean;
  zoom: number;
  panRef: React.MutableRefObject<{ x: number; y: number }>;
  saveTimerRef: React.MutableRefObject<ReturnType<typeof setTimeout> | null>;
  setLastSavedLayout: (layout: OfficeLayout) => void;
  handleOpenClaude: () => void;
  handleToggleEditMode: () => void;
  handleToolChange: (tool: EditToolType) => void;
  handleTileTypeChange: (type: TileTypeVal) => void;
  handleFloorColorChange: (color: FloorColor) => void;
  handleWallColorChange: (color: FloorColor) => void;
  handleWallSetChange: (setIndex: number) => void;
  handleSelectedFurnitureColorChange: (color: FloorColor | null) => void;
  handleFurnitureTypeChange: (type: string) => void; // FurnitureType enum or asset ID
  handleDeleteSelected: () => void;
  handleRotateSelected: () => void;
  handleToggleState: () => void;
  handleUndo: () => void;
  handleRedo: () => void;
  handleReset: () => void;
  handleSave: () => void;
  handleZoomChange: (zoom: number) => void;
  handleEditorTileAction: (col: number, row: number) => void;
  handleEditorEraseAction: (col: number, row: number) => void;
  handleEditorSelectionChange: () => void;
  handleDragMove: (uid: string, newCol: number, newRow: number) => void;
}

export function useEditorActions(
  getOfficeState: () => OfficeState,
  editorState: EditorState,
): EditorActions {
  const [isEditMode, setIsEditMode] = useState(false);
  const [editorTick, setEditorTick] = useState(0);
  const [isDirty, setIsDirty] = useState(false);
  const [zoom, setZoom] = useState(defaultZoom);
  const saveTimerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const panRef = useRef({ x: 0, y: 0 });
  const lastSavedLayoutRef = useRef<OfficeLayout | null>(null);

  // Called by useExtensionMessages on layoutLoaded to set the initial checkpoint
  const setLastSavedLayout = useCallback((layout: OfficeLayout) => {
    lastSavedLayoutRef.current = structuredClone(layout);
  }, []);

  // Debounced layout save
  const saveLayout = useCallback((layout: OfficeLayout) => {
    if (saveTimerRef.current) clearTimeout(saveTimerRef.current);
    saveTimerRef.current = setTimeout(() => {
      vscode.postMessage({ type: 'saveLayout', layout });
    }, LAYOUT_SAVE_DEBOUNCE_MS);
  }, []);

  // Apply a layout edit: push undo, clear redo, rebuild state, save, mark dirty
  const applyEdit = useCallback(
    (newLayout: OfficeLayout) => {
      const os = getOfficeState();
      editorState.pushUndo(os.getLayout());
      editorState.clearRedo();
      editorState.isDirty = true;
      setIsDirty(true);
      os.rebuildFromLayout(newLayout);
      saveLayout(newLayout);
      setEditorTick((n) => n + 1);
    },
    [getOfficeState, editorState, saveLayout],
  );

  const handleOpenClaude = useCallback(() => {
    vscode.postMessage({ type: 'openClaude' });
  }, []);

  const handleToggleEditMode = useCallback(() => {
    setIsEditMode((prev) => {
      const next = !prev;
      editorState.isEditMode = next;
      if (next) {
        // Initialize wallColor from existing wall tiles so new walls match
        const os = getOfficeState();
        const layout = os.getLayout();
        if (layout.tileColors) {
          for (let i = 0; i < layout.tiles.length; i++) {
            if (layout.tiles[i] === TileType.WALL && layout.tileColors[i]) {
              editorState.wallColor = { ...layout.tileColors[i]! };
              break;
            }
          }
        }
      } else {
        editorState.clearSelection();
        editorState.clearGhost();
        editorState.clearDrag();
        wallColorEditActiveRef.current = false;
      }
      return next;
    });
  }, [editorState, getOfficeState]);

  // Tool toggle: clicking already-active tool deselects it (returns to SELECT)
  const handleToolChange = useCallback(
    (tool: EditToolType) => {
      if (editorState.activeTool === tool) {
        editorState.activeTool = EditTool.SELECT;
      } else {
        editorState.activeTool = tool;
      }
      editorState.clearSelection();
      editorState.clearGhost();
      editorState.clearDrag();
      colorEditUidRef.current = null;
      wallColorEditActiveRef.current = false;
      setEditorTick((n) => n + 1);
    },
    [editorState],
  );

  const handleTileTypeChange = useCallback(
    (type: TileTypeVal) => {
      editorState.selectedTileType = type;
      setEditorTick((n) => n + 1);
    },
    [editorState],
  );

  const handleFloorColorChange = useCallback(
    (color: FloorColor) => {
      editorState.floorColor = color;
      setEditorTick((n) => n + 1);
    },
    [editorState],
  );

  // Track whether we've already pushed undo for the current wall color editing session
  const wallColorEditActiveRef = useRef(false);

  const handleWallColorChange = useCallback(
    (color: FloorColor) => {
      editorState.wallColor = color;

      // Update all existing wall tiles to the new color
      const os = getOfficeState();
      const layout = os.getLayout();
      const existingColors = layout.tileColors || new Array(layout.tiles.length).fill(null);
      const newColors = [...existingColors];
      let changed = false;
      for (let i = 0; i < layout.tiles.length; i++) {
        if (layout.tiles[i] === TileType.WALL) {
          newColors[i] = { ...color };
          changed = true;
        }
      }
      if (changed) {
        // Push undo only once per editing session (first slider touch)
        if (!wallColorEditActiveRef.current) {
          editorState.pushUndo(layout);
          editorState.clearRedo();
          wallColorEditActiveRef.current = true;
        }
        const newLayout = { ...layout, tileColors: newColors };
        editorState.isDirty = true;
        setIsDirty(true);
        os.rebuildFromLayout(newLayout);
        saveLayout(newLayout);
      }
      setEditorTick((n) => n + 1);
    },
    [editorState, getOfficeState, saveLayout],
  );

  const handleWallSetChange = useCallback(
    (setIndex: number) => {
      editorState.selectedWallSet = setIndex;
      setEditorTick((n) => n + 1);
    },
    [editorState],
  );

  // Track which uid we've already pushed undo for during color editing
  // so dragging sliders doesn't create N undo entries
  const colorEditUidRef = useRef<string | null>(null);

  const handleSelectedFurnitureColorChange = useCallback(
    (color: FloorColor | null) => {
      const uid = editorState.selectedFurnitureUid;
      if (!uid) return;
      const os = getOfficeState();
      const layout = os.getLayout();

      // Push undo only once per selection (first slider touch)
      if (colorEditUidRef.current !== uid) {
        editorState.pushUndo(layout);
        editorState.clearRedo();
        colorEditUidRef.current = uid;
      }

      // Update color on the placed furniture item (null removes color)
      const newFurniture = layout.furniture.map((f) =>
        f.uid === uid ? { ...f, color: color ?? undefined } : f,
      );
      const newLayout = { ...layout, furniture: newFurniture };

      editorState.isDirty = true;
      setIsDirty(true);
      os.rebuildFromLayout(newLayout);
      saveLayout(newLayout);
      setEditorTick((n) => n + 1);
    },
    [getOfficeState, editorState, saveLayout],
  );

  const handleFurnitureTypeChange = useCallback(
    (type: string) => {
      // Clicking the same item deselects it (no ghost), stays in furniture mode
      if (editorState.selectedFurnitureType === type) {
        editorState.selectedFurnitureType = '';
        editorState.clearGhost();
      } else {
        editorState.selectedFurnitureType = type;
      }
      setEditorTick((n) => n + 1);
    },
    [editorState],
  );

  const handleDeleteSelected = useCallback(() => {
    const uid = editorState.selectedFurnitureUid;
    if (!uid) return;
    const os = getOfficeState();
    const newLayout = removeFurniture(os.getLayout(), uid);
    if (newLayout !== os.getLayout()) {
      applyEdit(newLayout);
      editorState.clearSelection();
      colorEditUidRef.current = null;
    }
  }, [getOfficeState, editorState, applyEdit]);

  const handleRotateSelected = useCallback(() => {
    // If in furniture placement mode, cycle the selected type through the rotation group
    if (editorState.activeTool === EditTool.FURNITURE_PLACE) {
      const rotated = getRotatedType(editorState.selectedFurnitureType, 'cw');
      if (rotated) {
        editorState.selectedFurnitureType = rotated;
        setEditorTick((n) => n + 1);
      }
      return;
    }
    // Otherwise rotate the selected placed furniture
    const uid = editorState.selectedFurnitureUid;
    if (!uid) return;
    const os = getOfficeState();
    const newLayout = rotateFurniture(os.getLayout(), uid, 'cw');
    if (newLayout !== os.getLayout()) {
      applyEdit(newLayout);
    }
  }, [getOfficeState, editorState, applyEdit]);

  const handleToggleState = useCallback(() => {
    // If in furniture placement mode, toggle the selected type's state
    if (editorState.activeTool === EditTool.FURNITURE_PLACE) {
      const toggled = getToggledType(editorState.selectedFurnitureType);
      if (toggled) {
        editorState.selectedFurnitureType = toggled;
        setEditorTick((n) => n + 1);
      }
      return;
    }
    // Otherwise toggle the selected placed furniture's state
    const uid = editorState.selectedFurnitureUid;
    if (!uid) return;
    const os = getOfficeState();
    const newLayout = toggleFurnitureState(os.getLayout(), uid);
    if (newLayout !== os.getLayout()) {
      applyEdit(newLayout);
    }
  }, [getOfficeState, editorState, applyEdit]);

  const handleUndo = useCallback(() => {
    const prev = editorState.popUndo();
    if (!prev) return;
    const os = getOfficeState();
    // Push current layout to redo stack before restoring
    editorState.pushRedo(os.getLayout());
    os.rebuildFromLayout(prev);
    saveLayout(prev);
    editorState.isDirty = true;
    setIsDirty(true);
    setEditorTick((n) => n + 1);
  }, [getOfficeState, editorState, saveLayout]);

  const handleRedo = useCallback(() => {
    const next = editorState.popRedo();
    if (!next) return;
    const os = getOfficeState();
    // Push current layout to undo stack before restoring
    editorState.pushUndo(os.getLayout());
    os.rebuildFromLayout(next);
    saveLayout(next);
    editorState.isDirty = true;
    setIsDirty(true);
    setEditorTick((n) => n + 1);
  }, [getOfficeState, editorState, saveLayout]);

  const handleReset = useCallback(() => {
    if (!lastSavedLayoutRef.current) return;
    const saved = structuredClone(lastSavedLayoutRef.current);
    applyEdit(saved);
    editorState.reset();
    setIsDirty(false);
  }, [editorState, applyEdit]);

  const handleSave = useCallback(() => {
    // Flush any pending debounced save immediately
    if (saveTimerRef.current) {
      clearTimeout(saveTimerRef.current);
      saveTimerRef.current = null;
    }
    const os = getOfficeState();
    const layout = os.getLayout();
    lastSavedLayoutRef.current = structuredClone(layout);
    vscode.postMessage({ type: 'saveLayout', layout });
    editorState.isDirty = false;
    setIsDirty(false);
  }, [getOfficeState, editorState]);

  // Notify React that imperative editor selection changed (e.g., from OfficeCanvas mouseUp)
  const handleEditorSelectionChange = useCallback(() => {
    colorEditUidRef.current = null;
    setEditorTick((n) => n + 1);
  }, []);

  const handleZoomChange = useCallback((newZoom: number) => {
    setZoom(Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, newZoom)));
  }, []);

  const handleDragMove = useCallback(
    (uid: string, newCol: number, newRow: number) => {
      const os = getOfficeState();
      const layout = os.getLayout();
      const newLayout = moveFurniture(layout, uid, newCol, newRow);
      if (newLayout !== layout) {
        applyEdit(newLayout);
      }
    },
    [getOfficeState, applyEdit],
  );

  /**
   * Expand layout if click is on a ghost border tile (outside current bounds).
   * Returns the expanded layout and adjusted col/row, or null if no expansion needed.
   */
  const maybeExpand = useCallback(
    (
      layout: OfficeLayout,
      col: number,
      row: number,
    ): {
      layout: OfficeLayout;
      col: number;
      row: number;
      shift: { col: number; row: number };
    } | null => {
      if (col >= 0 && col < layout.cols && row >= 0 && row < layout.rows) return null;

      // Determine which directions to expand
      const directions: ExpandDirection[] = [];
      if (col < 0) directions.push('left');
      if (col >= layout.cols) directions.push('right');
      if (row < 0) directions.push('up');
      if (row >= layout.rows) directions.push('down');

      let current = layout;
      let totalShiftCol = 0;
      let totalShiftRow = 0;
      for (const dir of directions) {
        const result = expandLayout(current, dir);
        if (!result) return null; // exceeded max
        current = result.layout;
        totalShiftCol += result.shift.col;
        totalShiftRow += result.shift.row;
      }

      return {
        layout: current,
        col: col + totalShiftCol,
        row: row + totalShiftRow,
        shift: { col: totalShiftCol, row: totalShiftRow },
      };
    },
    [],
  );

  const handleEditorTileAction = useCallback(
    (col: number, row: number) => {
      const os = getOfficeState();
      let layout = os.getLayout();
      let effectiveCol = col;
      let effectiveRow = row;

      // Handle ghost border expansion for floor/wall tools
      if (
        editorState.activeTool === EditTool.TILE_PAINT ||
        editorState.activeTool === EditTool.WALL_PAINT
      ) {
        const expansion = maybeExpand(layout, col, row);
        if (expansion) {
          layout = expansion.layout;
          effectiveCol = expansion.col;
          effectiveRow = expansion.row;
          // Rebuild from expanded layout first, shifting character positions
          os.rebuildFromLayout(layout, expansion.shift);
        }
      }

      if (editorState.activeTool === EditTool.TILE_PAINT) {
        const newLayout = paintTile(
          layout,
          effectiveCol,
          effectiveRow,
          editorState.selectedTileType,
          editorState.floorColor,
        );
        if (newLayout !== layout) {
          applyEdit(newLayout);
        }
      } else if (editorState.activeTool === EditTool.WALL_PAINT) {
        const idx = effectiveRow * layout.cols + effectiveCol;
        const isWall = layout.tiles[idx] === TileType.WALL;

        // First tile of drag sets direction
        if (editorState.wallDragAdding === null) {
          editorState.wallDragAdding = !isWall;
        }

        if (editorState.wallDragAdding) {
          // Add wall with color
          const newLayout = paintTile(
            layout,
            effectiveCol,
            effectiveRow,
            TileType.WALL,
            editorState.wallColor,
          );
          if (newLayout !== layout) {
            applyEdit(newLayout);
          }
        } else {
          // Remove wall → paint floor with current floor settings
          if (isWall) {
            const newLayout = paintTile(
              layout,
              effectiveCol,
              effectiveRow,
              editorState.selectedTileType,
              editorState.floorColor,
            );
            if (newLayout !== layout) {
              applyEdit(newLayout);
            }
          }
        }
      } else if (editorState.activeTool === EditTool.ERASE) {
        if (col < 0 || col >= layout.cols || row < 0 || row >= layout.rows) return;
        const idx = row * layout.cols + col;
        if (layout.tiles[idx] === TileType.VOID) return;
        const newLayout = paintTile(layout, col, row, TileType.VOID);
        if (newLayout !== layout) {
          applyEdit(newLayout);
        }
      } else if (editorState.activeTool === EditTool.FURNITURE_PLACE) {
        const type = editorState.selectedFurnitureType;
        if (type === '') {
          // No item selected — act like SELECT (find furniture hit)
          const hit = layout.furniture.find((f) => {
            const entry = getCatalogEntry(f.type);
            if (!entry) return false;
            return (
              col >= f.col &&
              col < f.col + entry.footprintW &&
              row >= f.row &&
              row < f.row + entry.footprintH
            );
          });
          editorState.selectedFurnitureUid = hit ? hit.uid : null;
          setEditorTick((n) => n + 1);
        } else {
          const placementRow = getWallPlacementRow(type, row);
          if (!canPlaceFurniture(layout, type, col, placementRow)) return;
          const uid = `f-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`;
          const placed: PlacedFurniture = { uid, type, col, row: placementRow };
          if (editorState.pickedFurnitureColor) {
            placed.color = { ...editorState.pickedFurnitureColor };
          }
          const newLayout = placeFurniture(layout, placed);
          if (newLayout !== layout) {
            applyEdit(newLayout);
          }
        }
      } else if (editorState.activeTool === EditTool.FURNITURE_PICK) {
        // Find furniture at clicked tile, copy its type and color for placement
        const hit = layout.furniture.find((f) => {
          const entry = getCatalogEntry(f.type);
          if (!entry) return false;
          return (
            col >= f.col &&
            col < f.col + entry.footprintW &&
            row >= f.row &&
            row < f.row + entry.footprintH
          );
        });
        if (hit) {
          editorState.selectedFurnitureType = hit.type;
          editorState.pickedFurnitureColor = hit.color ? { ...hit.color } : null;
          editorState.activeTool = EditTool.FURNITURE_PLACE;
        }
        setEditorTick((n) => n + 1);
      } else if (editorState.activeTool === EditTool.EYEDROPPER) {
        const idx = row * layout.cols + col;
        const tile = layout.tiles[idx];
        if (tile !== undefined && tile !== TileType.WALL && tile !== TileType.VOID) {
          editorState.selectedTileType = tile;
          const color = layout.tileColors?.[idx];
          if (color) {
            editorState.floorColor = { ...color };
          }
          editorState.activeTool = EditTool.TILE_PAINT;
        } else if (tile === TileType.WALL) {
          // Pick wall color and switch to wall tool
          const color = layout.tileColors?.[idx];
          if (color) {
            editorState.wallColor = { ...color };
          }
          editorState.activeTool = EditTool.WALL_PAINT;
        }
        setEditorTick((n) => n + 1);
      } else if (editorState.activeTool === EditTool.SELECT) {
        const hit = layout.furniture.find((f) => {
          const entry = getCatalogEntry(f.type);
          if (!entry) return false;
          return (
            col >= f.col &&
            col < f.col + entry.footprintW &&
            row >= f.row &&
            row < f.row + entry.footprintH
          );
        });
        editorState.selectedFurnitureUid = hit ? hit.uid : null;
        setEditorTick((n) => n + 1);
      }
    },
    [getOfficeState, editorState, applyEdit, maybeExpand],
  );

  const handleEditorEraseAction = useCallback(
    (col: number, row: number) => {
      const os = getOfficeState();
      const layout = os.getLayout();
      if (col < 0 || col >= layout.cols || row < 0 || row >= layout.rows) return;
      const idx = row * layout.cols + col;
      // Only erase non-VOID tiles
      if (layout.tiles[idx] === TileType.VOID) return;
      const newLayout = paintTile(layout, col, row, TileType.VOID);
      if (newLayout !== layout) {
        applyEdit(newLayout);
      }
    },
    [getOfficeState, applyEdit],
  );

  return {
    isEditMode,
    editorTick,
    isDirty,
    zoom,
    panRef,
    saveTimerRef,
    setLastSavedLayout,
    handleOpenClaude,
    handleToggleEditMode,
    handleToolChange,
    handleTileTypeChange,
    handleFloorColorChange,
    handleWallColorChange,
    handleWallSetChange,
    handleSelectedFurnitureColorChange,
    handleFurnitureTypeChange,
    handleDeleteSelected,
    handleRotateSelected,
    handleToggleState,
    handleUndo,
    handleRedo,
    handleReset,
    handleSave,
    handleZoomChange,
    handleEditorTileAction,
    handleEditorEraseAction,
    handleEditorSelectionChange,
    handleDragMove,
  };
}
```

## File: `webview-ui/src/hooks/useEditorKeyboard.ts`
```typescript
import { useEffect } from 'react';

import type { EditorState } from '../office/editor/editorState.js';
import { EditTool } from '../office/types.js';

export function useEditorKeyboard(
  isEditMode: boolean,
  editorState: EditorState,
  onDeleteSelected: () => void,
  onRotateSelected: () => void,
  onToggleState: () => void,
  onUndo: () => void,
  onRedo: () => void,
  onEditorTick: () => void,
  onCloseEditMode: () => void,
): void {
  useEffect(() => {
    if (!isEditMode) return;
    const handler = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        // Multi-stage Esc: deselect item → close tool → deselect placed → close editor
        if (editorState.activeTool === EditTool.FURNITURE_PICK) {
          editorState.activeTool = EditTool.FURNITURE_PLACE;
          editorState.clearGhost();
        } else if (
          editorState.activeTool === EditTool.FURNITURE_PLACE &&
          editorState.selectedFurnitureType !== ''
        ) {
          editorState.selectedFurnitureType = '';
          editorState.clearGhost();
        } else if (editorState.activeTool !== EditTool.SELECT) {
          editorState.activeTool = EditTool.SELECT;
          editorState.clearGhost();
        } else if (editorState.selectedFurnitureUid) {
          editorState.clearSelection();
        } else {
          onCloseEditMode();
          return;
        }
        editorState.clearDrag();
        onEditorTick();
      } else if (e.key === 'Delete' || e.key === 'Backspace') {
        if (editorState.selectedFurnitureUid) {
          onDeleteSelected();
        }
      } else if (e.key === 'r' || e.key === 'R') {
        onRotateSelected();
      } else if (e.key === 't' || e.key === 'T') {
        onToggleState();
      } else if (e.key === 'z' && (e.ctrlKey || e.metaKey) && !e.shiftKey) {
        e.preventDefault();
        onUndo();
      } else if (
        (e.key === 'y' && (e.ctrlKey || e.metaKey)) ||
        (e.key === 'z' && (e.ctrlKey || e.metaKey) && e.shiftKey)
      ) {
        e.preventDefault();
        onRedo();
      }
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [
    isEditMode,
    editorState,
    onDeleteSelected,
    onRotateSelected,
    onToggleState,
    onUndo,
    onRedo,
    onEditorTick,
    onCloseEditMode,
  ]);
}
```

## File: `webview-ui/src/hooks/useExtensionMessages.ts`
```typescript
import { useEffect, useRef, useState } from 'react';

import { playDoneSound, setSoundEnabled } from '../notificationSound.js';
import type { OfficeState } from '../office/engine/officeState.js';
import { setFloorSprites } from '../office/floorTiles.js';
import { buildDynamicCatalog } from '../office/layout/furnitureCatalog.js';
import { migrateLayoutColors } from '../office/layout/layoutSerializer.js';
import { setCharacterTemplates } from '../office/sprites/spriteData.js';
import { extractToolName } from '../office/toolUtils.js';
import type { OfficeLayout, ToolActivity } from '../office/types.js';
import { setWallSprites } from '../office/wallTiles.js';
import { vscode } from '../vscodeApi.js';

export interface SubagentCharacter {
  id: number;
  parentAgentId: number;
  parentToolId: string;
  label: string;
}

export interface FurnitureAsset {
  id: string;
  name: string;
  label: string;
  category: string;
  file: string;
  width: number;
  height: number;
  footprintW: number;
  footprintH: number;
  isDesk: boolean;
  canPlaceOnWalls: boolean;
  groupId?: string;
  canPlaceOnSurfaces?: boolean;
  backgroundTiles?: number;
  orientation?: string;
  state?: string;
  mirrorSide?: boolean;
  rotationScheme?: string;
  animationGroup?: string;
  frame?: number;
}

export interface WorkspaceFolder {
  name: string;
  path: string;
}

export interface ExtensionMessageState {
  agents: number[];
  selectedAgent: number | null;
  agentTools: Record<number, ToolActivity[]>;
  agentStatuses: Record<number, string>;
  subagentTools: Record<number, Record<string, ToolActivity[]>>;
  subagentCharacters: SubagentCharacter[];
  layoutReady: boolean;
  layoutWasReset: boolean;
  loadedAssets?: { catalog: FurnitureAsset[]; sprites: Record<string, string[][]> };
  workspaceFolders: WorkspaceFolder[];
}

function saveAgentSeats(os: OfficeState): void {
  const seats: Record<number, { palette: number; hueShift: number; seatId: string | null }> = {};
  for (const ch of os.characters.values()) {
    if (ch.isSubagent) continue;
    seats[ch.id] = { palette: ch.palette, hueShift: ch.hueShift, seatId: ch.seatId };
  }
  vscode.postMessage({ type: 'saveAgentSeats', seats });
}

export function useExtensionMessages(
  getOfficeState: () => OfficeState,
  onLayoutLoaded?: (layout: OfficeLayout) => void,
  isEditDirty?: () => boolean,
): ExtensionMessageState {
  const [agents, setAgents] = useState<number[]>([]);
  const [selectedAgent, setSelectedAgent] = useState<number | null>(null);
  const [agentTools, setAgentTools] = useState<Record<number, ToolActivity[]>>({});
  const [agentStatuses, setAgentStatuses] = useState<Record<number, string>>({});
  const [subagentTools, setSubagentTools] = useState<
    Record<number, Record<string, ToolActivity[]>>
  >({});
  const [subagentCharacters, setSubagentCharacters] = useState<SubagentCharacter[]>([]);
  const [layoutReady, setLayoutReady] = useState(false);
  const [layoutWasReset, setLayoutWasReset] = useState(false);
  const [loadedAssets, setLoadedAssets] = useState<
    { catalog: FurnitureAsset[]; sprites: Record<string, string[][]> } | undefined
  >();
  const [workspaceFolders, setWorkspaceFolders] = useState<WorkspaceFolder[]>([]);

  // Track whether initial layout has been loaded (ref to avoid re-render)
  const layoutReadyRef = useRef(false);

  useEffect(() => {
    // Buffer agents from existingAgents until layout is loaded
    let pendingAgents: Array<{
      id: number;
      palette?: number;
      hueShift?: number;
      seatId?: string;
      folderName?: string;
    }> = [];

    const handler = (e: MessageEvent) => {
      const msg = e.data;
      const os = getOfficeState();

      if (msg.type === 'layoutLoaded') {
        // Skip external layout updates while editor has unsaved changes
        if (layoutReadyRef.current && isEditDirty?.()) {
          console.log('[Webview] Skipping external layout update — editor has unsaved changes');
          return;
        }
        const rawLayout = msg.layout as OfficeLayout | null;
        const layout = rawLayout && rawLayout.version === 1 ? migrateLayoutColors(rawLayout) : null;
        if (layout) {
          os.rebuildFromLayout(layout);
          onLayoutLoaded?.(layout);
        } else {
          // Default layout — snapshot whatever OfficeState built
          onLayoutLoaded?.(os.getLayout());
        }
        // Add buffered agents now that layout (and seats) are correct
        for (const p of pendingAgents) {
          os.addAgent(p.id, p.palette, p.hueShift, p.seatId, true, p.folderName);
        }
        pendingAgents = [];
        layoutReadyRef.current = true;
        setLayoutReady(true);
        if (msg.wasReset) {
          setLayoutWasReset(true);
        }
        if (os.characters.size > 0) {
          saveAgentSeats(os);
        }
      } else if (msg.type === 'agentCreated') {
        const id = msg.id as number;
        const folderName = msg.folderName as string | undefined;
        setAgents((prev) => (prev.includes(id) ? prev : [...prev, id]));
        setSelectedAgent(id);
        os.addAgent(id, undefined, undefined, undefined, undefined, folderName);
        saveAgentSeats(os);
      } else if (msg.type === 'agentClosed') {
        const id = msg.id as number;
        setAgents((prev) => prev.filter((a) => a !== id));
        setSelectedAgent((prev) => (prev === id ? null : prev));
        setAgentTools((prev) => {
          if (!(id in prev)) return prev;
          const next = { ...prev };
          delete next[id];
          return next;
        });
        setAgentStatuses((prev) => {
          if (!(id in prev)) return prev;
          const next = { ...prev };
          delete next[id];
          return next;
        });
        setSubagentTools((prev) => {
          if (!(id in prev)) return prev;
          const next = { ...prev };
          delete next[id];
          return next;
        });
        // Remove all sub-agent characters belonging to this agent
        os.removeAllSubagents(id);
        setSubagentCharacters((prev) => prev.filter((s) => s.parentAgentId !== id));
        os.removeAgent(id);
      } else if (msg.type === 'existingAgents') {
        const incoming = msg.agents as number[];
        const meta = (msg.agentMeta || {}) as Record<
          number,
          { palette?: number; hueShift?: number; seatId?: string }
        >;
        const folderNames = (msg.folderNames || {}) as Record<number, string>;
        // Buffer agents — they'll be added in layoutLoaded after seats are built
        for (const id of incoming) {
          const m = meta[id];
          pendingAgents.push({
            id,
            palette: m?.palette,
            hueShift: m?.hueShift,
            seatId: m?.seatId,
            folderName: folderNames[id],
          });
        }
        setAgents((prev) => {
          const ids = new Set(prev);
          const merged = [...prev];
          for (const id of incoming) {
            if (!ids.has(id)) {
              merged.push(id);
            }
          }
          return merged.sort((a, b) => a - b);
        });
      } else if (msg.type === 'agentToolStart') {
        const id = msg.id as number;
        const toolId = msg.toolId as string;
        const status = msg.status as string;
        setAgentTools((prev) => {
          const list = prev[id] || [];
          if (list.some((t) => t.toolId === toolId)) return prev;
          return { ...prev, [id]: [...list, { toolId, status, done: false }] };
        });
        const toolName = extractToolName(status);
        os.setAgentTool(id, toolName);
        os.setAgentActive(id, true);
        os.clearPermissionBubble(id);
        // Create sub-agent character for Task tool subtasks
        if (status.startsWith('Subtask:')) {
          const label = status.slice('Subtask:'.length).trim();
          const subId = os.addSubagent(id, toolId);
          setSubagentCharacters((prev) => {
            if (prev.some((s) => s.id === subId)) return prev;
            return [...prev, { id: subId, parentAgentId: id, parentToolId: toolId, label }];
          });
        }
      } else if (msg.type === 'agentToolDone') {
        const id = msg.id as number;
        const toolId = msg.toolId as string;
        setAgentTools((prev) => {
          const list = prev[id];
          if (!list) return prev;
          return {
            ...prev,
            [id]: list.map((t) => (t.toolId === toolId ? { ...t, done: true } : t)),
          };
        });
      } else if (msg.type === 'agentToolsClear') {
        const id = msg.id as number;
        setAgentTools((prev) => {
          if (!(id in prev)) return prev;
          const next = { ...prev };
          delete next[id];
          return next;
        });
        setSubagentTools((prev) => {
          if (!(id in prev)) return prev;
          const next = { ...prev };
          delete next[id];
          return next;
        });
        // Remove all sub-agent characters belonging to this agent
        os.removeAllSubagents(id);
        setSubagentCharacters((prev) => prev.filter((s) => s.parentAgentId !== id));
        os.setAgentTool(id, null);
        os.clearPermissionBubble(id);
      } else if (msg.type === 'agentSelected') {
        const id = msg.id as number;
        setSelectedAgent(id);
      } else if (msg.type === 'agentStatus') {
        const id = msg.id as number;
        const status = msg.status as string;
        setAgentStatuses((prev) => {
          if (status === 'active') {
            if (!(id in prev)) return prev;
            const next = { ...prev };
            delete next[id];
            return next;
          }
          return { ...prev, [id]: status };
        });
        os.setAgentActive(id, status === 'active');
        if (status === 'waiting') {
          os.showWaitingBubble(id);
          playDoneSound();
        }
      } else if (msg.type === 'agentToolPermission') {
        const id = msg.id as number;
        setAgentTools((prev) => {
          const list = prev[id];
          if (!list) return prev;
          return {
            ...prev,
            [id]: list.map((t) => (t.done ? t : { ...t, permissionWait: true })),
          };
        });
        os.showPermissionBubble(id);
      } else if (msg.type === 'subagentToolPermission') {
        const id = msg.id as number;
        const parentToolId = msg.parentToolId as string;
        // Show permission bubble on the sub-agent character
        const subId = os.getSubagentId(id, parentToolId);
        if (subId !== null) {
          os.showPermissionBubble(subId);
        }
      } else if (msg.type === 'agentToolPermissionClear') {
        const id = msg.id as number;
        setAgentTools((prev) => {
          const list = prev[id];
          if (!list) return prev;
          const hasPermission = list.some((t) => t.permissionWait);
          if (!hasPermission) return prev;
          return {
            ...prev,
            [id]: list.map((t) => (t.permissionWait ? { ...t, permissionWait: false } : t)),
          };
        });
        os.clearPermissionBubble(id);
        // Also clear permission bubbles on all sub-agent characters of this parent
        for (const [subId, meta] of os.subagentMeta) {
          if (meta.parentAgentId === id) {
            os.clearPermissionBubble(subId);
          }
        }
      } else if (msg.type === 'subagentToolStart') {
        const id = msg.id as number;
        const parentToolId = msg.parentToolId as string;
        const toolId = msg.toolId as string;
        const status = msg.status as string;
        setSubagentTools((prev) => {
          const agentSubs = prev[id] || {};
          const list = agentSubs[parentToolId] || [];
          if (list.some((t) => t.toolId === toolId)) return prev;
          return {
            ...prev,
            [id]: { ...agentSubs, [parentToolId]: [...list, { toolId, status, done: false }] },
          };
        });
        // Update sub-agent character's tool and active state
        const subId = os.getSubagentId(id, parentToolId);
        if (subId !== null) {
          const subToolName = extractToolName(status);
          os.setAgentTool(subId, subToolName);
          os.setAgentActive(subId, true);
        }
      } else if (msg.type === 'subagentToolDone') {
        const id = msg.id as number;
        const parentToolId = msg.parentToolId as string;
        const toolId = msg.toolId as string;
        setSubagentTools((prev) => {
          const agentSubs = prev[id];
          if (!agentSubs) return prev;
          const list = agentSubs[parentToolId];
          if (!list) return prev;
          return {
            ...prev,
            [id]: {
              ...agentSubs,
              [parentToolId]: list.map((t) => (t.toolId === toolId ? { ...t, done: true } : t)),
            },
          };
        });
      } else if (msg.type === 'subagentClear') {
        const id = msg.id as number;
        const parentToolId = msg.parentToolId as string;
        setSubagentTools((prev) => {
          const agentSubs = prev[id];
          if (!agentSubs || !(parentToolId in agentSubs)) return prev;
          const next = { ...agentSubs };
          delete next[parentToolId];
          if (Object.keys(next).length === 0) {
            const outer = { ...prev };
            delete outer[id];
            return outer;
          }
          return { ...prev, [id]: next };
        });
        // Remove sub-agent character
        os.removeSubagent(id, parentToolId);
        setSubagentCharacters((prev) =>
          prev.filter((s) => !(s.parentAgentId === id && s.parentToolId === parentToolId)),
        );
      } else if (msg.type === 'characterSpritesLoaded') {
        const characters = msg.characters as Array<{
          down: string[][][];
          up: string[][][];
          right: string[][][];
        }>;
        console.log(`[Webview] Received ${characters.length} pre-colored character sprites`);
        setCharacterTemplates(characters);
      } else if (msg.type === 'floorTilesLoaded') {
        const sprites = msg.sprites as string[][][];
        console.log(`[Webview] Received ${sprites.length} floor tile patterns`);
        setFloorSprites(sprites);
      } else if (msg.type === 'wallTilesLoaded') {
        const sets = msg.sets as string[][][][];
        console.log(`[Webview] Received ${sets.length} wall tile set(s)`);
        setWallSprites(sets);
      } else if (msg.type === 'workspaceFolders') {
        const folders = msg.folders as WorkspaceFolder[];
        setWorkspaceFolders(folders);
      } else if (msg.type === 'settingsLoaded') {
        const soundOn = msg.soundEnabled as boolean;
        setSoundEnabled(soundOn);
      } else if (msg.type === 'furnitureAssetsLoaded') {
        try {
          const catalog = msg.catalog as FurnitureAsset[];
          const sprites = msg.sprites as Record<string, string[][]>;
          console.log(`📦 Webview: Loaded ${catalog.length} furniture assets`);
          // Build dynamic catalog immediately so getCatalogEntry() works when layoutLoaded arrives next
          buildDynamicCatalog({ catalog, sprites });
          setLoadedAssets({ catalog, sprites });
        } catch (err) {
          console.error(`❌ Webview: Error processing furnitureAssetsLoaded:`, err);
        }
      }
    };
    window.addEventListener('message', handler);
    vscode.postMessage({ type: 'webviewReady' });
    return () => window.removeEventListener('message', handler);
  }, [getOfficeState]);

  return {
    agents,
    selectedAgent,
    agentTools,
    agentStatuses,
    subagentTools,
    subagentCharacters,
    layoutReady,
    layoutWasReset,
    loadedAssets,
    workspaceFolders,
  };
}
```

## File: `webview-ui/src/office/colorize.ts`
```typescript
/**
 * Shared sprite colorization module.
 *
 * Two modes:
 * - Colorize (Photoshop-style): grayscale → fixed HSL. For floor tiles and opt-in furniture.
 * - Adjust (default for furniture): shift original pixel HSL values.
 */

import type { FloorColor, SpriteData } from './types.js';

/** Generic colorized sprite cache: arbitrary string key → SpriteData */
const colorizeCache = new Map<string, SpriteData>();

/**
 * Get a color-adjusted sprite from cache, or compute and cache it.
 * Dispatches to colorize or adjust mode based on `color.colorize`.
 * Caller provides a unique cache key that must include the colorize flag.
 */
export function getColorizedSprite(
  cacheKey: string,
  sprite: SpriteData,
  color: FloorColor,
): SpriteData {
  const cached = colorizeCache.get(cacheKey);
  if (cached) return cached;
  const result = color.colorize ? colorizeSprite(sprite, color) : adjustSprite(sprite, color);
  colorizeCache.set(cacheKey, result);
  return result;
}

/** Clear all cached colorized sprites (e.g., on asset reload) */
export function clearColorizeCache(): void {
  colorizeCache.clear();
}

/**
 * Colorize a sprite using HSL transformation.
 *
 * Algorithm (Photoshop Colorize-style):
 * 1. Parse each pixel's color as perceived luminance (0-1)
 * 2. Apply contrast: stretch/compress around midpoint 0.5
 * 3. Apply brightness: shift lightness up/down
 * 4. Create HSL color with user's hue + saturation
 * 5. Convert HSL -> RGB -> hex
 */
export function colorizeSprite(sprite: SpriteData, color: FloorColor): SpriteData {
  const { h, s, b, c } = color;
  const result: SpriteData = [];

  for (const row of sprite) {
    const newRow: string[] = [];
    for (const pixel of row) {
      if (pixel === '') {
        newRow.push('');
        continue;
      }

      // Parse hex to get RGB values
      const r = parseInt(pixel.slice(1, 3), 16);
      const g = parseInt(pixel.slice(3, 5), 16);
      const bv = parseInt(pixel.slice(5, 7), 16);
      // Use perceived luminance for grayscale
      let lightness = (0.299 * r + 0.587 * g + 0.114 * bv) / 255;

      // Apply contrast: expand/compress around 0.5
      if (c !== 0) {
        const factor = (100 + c) / 100;
        lightness = 0.5 + (lightness - 0.5) * factor;
      }

      // Apply brightness: shift up/down
      if (b !== 0) {
        lightness = lightness + b / 200;
      }

      // Clamp
      lightness = Math.max(0, Math.min(1, lightness));

      // Preserve original alpha
      const alpha = extractAlpha(pixel);

      // Convert HSL to RGB
      const satFrac = s / 100;
      const hex = hslToHex(h, satFrac, lightness);
      newRow.push(appendAlpha(hex, alpha));
    }
    result.push(newRow);
  }

  return result;
}

/** Extract alpha from a hex pixel string. Returns 255 for #RRGGBB, parsed value for #RRGGBBAA. */
function extractAlpha(pixel: string): number {
  return pixel.length > 7 ? parseInt(pixel.slice(7, 9), 16) : 255;
}

/** Append alpha to a #RRGGBB hex string, omitting if fully opaque. */
function appendAlpha(hex: string, alpha: number): string {
  if (alpha >= 255) return hex;
  return `${hex}${alpha.toString(16).padStart(2, '0').toUpperCase()}`;
}

/** Convert HSL (h: 0-360, s: 0-1, l: 0-1) to #RRGGBB hex string */
function hslToHex(h: number, s: number, l: number): string {
  const c = (1 - Math.abs(2 * l - 1)) * s;
  const hp = h / 60;
  const x = c * (1 - Math.abs((hp % 2) - 1));
  let r1 = 0,
    g1 = 0,
    b1 = 0;

  if (hp < 1) {
    r1 = c;
    g1 = x;
    b1 = 0;
  } else if (hp < 2) {
    r1 = x;
    g1 = c;
    b1 = 0;
  } else if (hp < 3) {
    r1 = 0;
    g1 = c;
    b1 = x;
  } else if (hp < 4) {
    r1 = 0;
    g1 = x;
    b1 = c;
  } else if (hp < 5) {
    r1 = x;
    g1 = 0;
    b1 = c;
  } else {
    r1 = c;
    g1 = 0;
    b1 = x;
  }

  const m = l - c / 2;
  const r = Math.round((r1 + m) * 255);
  const g = Math.round((g1 + m) * 255);
  const bOut = Math.round((b1 + m) * 255);

  return `#${clamp255(r).toString(16).padStart(2, '0')}${clamp255(g).toString(16).padStart(2, '0')}${clamp255(bOut).toString(16).padStart(2, '0')}`.toUpperCase();
}

function clamp255(v: number): number {
  return Math.max(0, Math.min(255, v));
}

/** Convert RGB (0-255 each) to HSL (h: 0-360, s: 0-1, l: 0-1) */
function rgbToHsl(r: number, g: number, b: number): [number, number, number] {
  const rf = r / 255,
    gf = g / 255,
    bf = b / 255;
  const max = Math.max(rf, gf, bf),
    min = Math.min(rf, gf, bf);
  const l = (max + min) / 2;
  if (max === min) return [0, 0, l];
  const d = max - min;
  const s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
  let h = 0;
  if (max === rf) h = ((gf - bf) / d + (gf < bf ? 6 : 0)) * 60;
  else if (max === gf) h = ((bf - rf) / d + 2) * 60;
  else h = ((rf - gf) / d + 4) * 60;
  return [h, s, l];
}

/**
 * Adjust a sprite's colors by shifting HSL values (default mode for furniture).
 *
 * H slider (-180 to +180): rotates hue
 * S slider (-100 to +100): shifts saturation
 * B slider (-100 to 100): shifts lightness
 * C slider (-100 to 100): adjusts contrast around midpoint
 */
export function adjustSprite(sprite: SpriteData, color: FloorColor): SpriteData {
  const { h: hShift, s: sShift, b, c } = color;
  const result: SpriteData = [];

  for (const row of sprite) {
    const newRow: string[] = [];
    for (const pixel of row) {
      if (pixel === '') {
        newRow.push('');
        continue;
      }

      const r = parseInt(pixel.slice(1, 3), 16);
      const g = parseInt(pixel.slice(3, 5), 16);
      const bv = parseInt(pixel.slice(5, 7), 16);
      const alpha = extractAlpha(pixel);
      const [origH, origS, origL] = rgbToHsl(r, g, bv);

      // Shift hue
      const newH = (((origH + hShift) % 360) + 360) % 360;

      // Shift saturation
      const newS = Math.max(0, Math.min(1, origS + sShift / 100));

      // Apply contrast: expand/compress around 0.5
      let lightness = origL;
      if (c !== 0) {
        const factor = (100 + c) / 100;
        lightness = 0.5 + (lightness - 0.5) * factor;
      }

      // Apply brightness
      if (b !== 0) {
        lightness = lightness + b / 200;
      }

      lightness = Math.max(0, Math.min(1, lightness));

      const hex = hslToHex(newH, newS, lightness);
      newRow.push(appendAlpha(hex, alpha));
    }
    result.push(newRow);
  }

  return result;
}
```

## File: `webview-ui/src/office/floorTiles.ts`
```typescript
/**
 * Floor tile pattern storage and caching.
 *
 * Stores grayscale floor patterns loaded from individual PNGs in assets/floors/.
 * Uses shared colorize module for HSL tinting (Photoshop-style Colorize).
 * Caches colorized SpriteData by (pattern, h, s, b, c) key.
 */

import { FALLBACK_FLOOR_COLOR, TILE_SIZE } from '../constants.js';
import { clearColorizeCache, getColorizedSprite } from './colorize.js';
import type { FloorColor, SpriteData } from './types.js';

/** Default solid gray 16×16 tile used when floor tile PNGs are not loaded */
const DEFAULT_FLOOR_SPRITE: SpriteData = Array.from(
  { length: TILE_SIZE },
  () => Array(TILE_SIZE).fill(FALLBACK_FLOOR_COLOR) as string[],
);

/** Module-level storage for floor tile sprites (set once on load) */
let floorSprites: SpriteData[] = [];

/** Wall color constant */
export const WALL_COLOR = '#3A3A5C';

/** Set floor tile sprites (called once when extension sends floorTilesLoaded) */
export function setFloorSprites(sprites: SpriteData[]): void {
  floorSprites = sprites;
  clearColorizeCache();
}

/** Get the raw (grayscale) floor sprite for a pattern index (1-7 -> array index 0-6).
 *  Falls back to the default solid gray tile when floors.png is not loaded. */
export function getFloorSprite(patternIndex: number): SpriteData | null {
  const idx = patternIndex - 1;
  if (idx < 0) return null;
  if (idx < floorSprites.length) return floorSprites[idx];
  // No PNG sprites loaded — return default solid tile for any valid pattern index
  if (floorSprites.length === 0 && patternIndex >= 1) return DEFAULT_FLOOR_SPRITE;
  return null;
}

/** Check if floor sprites are available (always true — falls back to default solid tile) */
export function hasFloorSprites(): boolean {
  return true;
}

/** Get count of available floor patterns (at least 1 for the default solid tile) */
export function getFloorPatternCount(): number {
  return floorSprites.length > 0 ? floorSprites.length : 1;
}

/** Get all floor sprites (for preview rendering, falls back to default solid tile) */
export function getAllFloorSprites(): SpriteData[] {
  return floorSprites.length > 0 ? floorSprites : [DEFAULT_FLOOR_SPRITE];
}

/**
 * Get a colorized version of a floor sprite.
 * Uses Photoshop-style Colorize: grayscale -> HSL with given hue/saturation,
 * then brightness/contrast adjustment.
 */
export function getColorizedFloorSprite(patternIndex: number, color: FloorColor): SpriteData {
  const key = `floor-${patternIndex}-${color.h}-${color.s}-${color.b}-${color.c}`;

  const base = getFloorSprite(patternIndex);
  if (!base) {
    // Return a 16x16 magenta error tile
    const err: SpriteData = Array.from({ length: 16 }, () => Array(16).fill('#FF00FF'));
    return err;
  }

  // Floor tiles are always colorized (grayscale patterns need Photoshop-style Colorize)
  return getColorizedSprite(key, base, { ...color, colorize: true });
}
```

## File: `webview-ui/src/office/toolUtils.ts`
```typescript
/** Map status prefixes back to tool names for animation selection */
export const STATUS_TO_TOOL: Record<string, string> = {
  Reading: 'Read',
  Searching: 'Grep',
  Globbing: 'Glob',
  Fetching: 'WebFetch',
  'Searching web': 'WebSearch',
  Writing: 'Write',
  Editing: 'Edit',
  Running: 'Bash',
  Task: 'Task',
};

export function extractToolName(status: string): string | null {
  for (const [prefix, tool] of Object.entries(STATUS_TO_TOOL)) {
    if (status.startsWith(prefix)) return tool;
  }
  const first = status.split(/[\s:]/)[0];
  return first || null;
}

import { ZOOM_DEFAULT_DPR_FACTOR, ZOOM_MIN } from '../constants.js';

/** Compute a default integer zoom level (device pixels per sprite pixel) */
export function defaultZoom(): number {
  const dpr = window.devicePixelRatio || 1;
  return Math.max(ZOOM_MIN, Math.round(ZOOM_DEFAULT_DPR_FACTOR * dpr));
}
```

## File: `webview-ui/src/office/types.ts`
```typescript
export {
  DEFAULT_COLS,
  DEFAULT_ROWS,
  MATRIX_EFFECT_DURATION_SEC as MATRIX_EFFECT_DURATION,
  MAX_COLS,
  MAX_ROWS,
  TILE_SIZE,
} from '../constants.js';

export const TileType = {
  WALL: 0,
  FLOOR_1: 1,
  FLOOR_2: 2,
  FLOOR_3: 3,
  FLOOR_4: 4,
  FLOOR_5: 5,
  FLOOR_6: 6,
  FLOOR_7: 7,
  FLOOR_8: 8,
  FLOOR_9: 9,
  VOID: 255,
} as const;
export type TileType = (typeof TileType)[keyof typeof TileType];

/** Per-tile color settings for floor pattern colorization */
export interface FloorColor {
  /** Hue: 0-360 in colorize mode, -180 to +180 in adjust mode */
  h: number;
  /** Saturation: 0-100 in colorize mode, -100 to +100 in adjust mode */
  s: number;
  /** Brightness -100 to 100 */
  b: number;
  /** Contrast -100 to 100 */
  c: number;
  /** When true, use Photoshop-style Colorize (grayscale → fixed HSL). Default: adjust mode. */
  colorize?: boolean;
}

export const CharacterState = {
  IDLE: 'idle',
  WALK: 'walk',
  TYPE: 'type',
} as const;
export type CharacterState = (typeof CharacterState)[keyof typeof CharacterState];

export const Direction = {
  DOWN: 0,
  LEFT: 1,
  RIGHT: 2,
  UP: 3,
} as const;
export type Direction = (typeof Direction)[keyof typeof Direction];

/** 2D array of hex color strings: '' = transparent, '#RRGGBB' = opaque, '#RRGGBBAA' = semi-transparent. [row][col] */
export type SpriteData = string[][];

export interface Seat {
  /** Chair furniture uid */
  uid: string;
  /** Tile col where agent sits */
  seatCol: number;
  /** Tile row where agent sits */
  seatRow: number;
  /** Direction character faces when sitting (toward adjacent desk) */
  facingDir: Direction;
  assigned: boolean;
}

export interface FurnitureInstance {
  sprite: SpriteData;
  /** Pixel x (top-left) */
  x: number;
  /** Pixel y (top-left) */
  y: number;
  /** Y value used for depth sorting (typically bottom edge) */
  zY: number;
  /** Render-time horizontal flip flag (for mirrored side variants) */
  mirrored?: boolean;
}

export interface ToolActivity {
  toolId: string;
  status: string;
  done: boolean;
  permissionWait?: boolean;
}

export const EditTool = {
  TILE_PAINT: 'tile_paint',
  WALL_PAINT: 'wall_paint',
  FURNITURE_PLACE: 'furniture_place',
  FURNITURE_PICK: 'furniture_pick',
  SELECT: 'select',
  EYEDROPPER: 'eyedropper',
  ERASE: 'erase',
} as const;
export type EditTool = (typeof EditTool)[keyof typeof EditTool];

export interface FurnitureCatalogEntry {
  type: string; // asset ID from furniture manifest
  label: string;
  footprintW: number;
  footprintH: number;
  sprite: SpriteData;
  isDesk: boolean;
  category?: string;
  /** Orientation from rotation group: 'front' | 'back' | 'left' | 'right' */
  orientation?: string;
  /** Whether this item can be placed on top of desk/table surfaces */
  canPlaceOnSurfaces?: boolean;
  /** Number of tile rows from the top of the footprint that are "background" (allow placement, still block walking). Default 0. */
  backgroundTiles?: number;
  /** Whether this item can be placed on wall tiles */
  canPlaceOnWalls?: boolean;
  /** Whether this is a side-oriented asset that produces a mirrored "left" variant */
  mirrorSide?: boolean;
}

export interface PlacedFurniture {
  uid: string;
  type: string; // asset ID from furniture manifest
  col: number;
  row: number;
  /** Optional color override for furniture */
  color?: FloorColor;
}

export interface OfficeLayout {
  version: 1;
  cols: number;
  rows: number;
  tiles: TileType[];
  furniture: PlacedFurniture[];
  /** Per-tile color settings, parallel to tiles array. null = wall/no color */
  tileColors?: Array<FloorColor | null>;
  /** Bumped when the bundled default layout changes; forces a reset on existing installs */
  layoutRevision?: number;
}

export interface Character {
  id: number;
  state: CharacterState;
  dir: Direction;
  /** Pixel position */
  x: number;
  y: number;
  /** Current tile column */
  tileCol: number;
  /** Current tile row */
  tileRow: number;
  /** Remaining path steps (tile coords) */
  path: Array<{ col: number; row: number }>;
  /** 0-1 lerp between current tile and next tile */
  moveProgress: number;
  /** Current tool name for typing vs reading animation, or null */
  currentTool: string | null;
  /** Palette index (0-5) */
  palette: number;
  /** Hue shift in degrees (0 = no shift, ≥45 for repeated palettes) */
  hueShift: number;
  /** Animation frame index */
  frame: number;
  /** Time accumulator for animation */
  frameTimer: number;
  /** Timer for idle wander decisions */
  wanderTimer: number;
  /** Number of wander moves completed in current roaming cycle */
  wanderCount: number;
  /** Max wander moves before returning to seat for rest */
  wanderLimit: number;
  /** Whether the agent is actively working */
  isActive: boolean;
  /** Assigned seat uid, or null if no seat */
  seatId: string | null;
  /** Active speech bubble type, or null if none showing */
  bubbleType: 'permission' | 'waiting' | null;
  /** Countdown timer for bubble (waiting: 2→0, permission: unused) */
  bubbleTimer: number;
  /** Timer to stay seated while inactive after seat reassignment (counts down to 0) */
  seatTimer: number;
  /** Whether this character represents a sub-agent (spawned by Task tool) */
  isSubagent: boolean;
  /** Parent agent ID if this is a sub-agent, null otherwise */
  parentAgentId: number | null;
  /** Active matrix spawn/despawn effect, or null */
  matrixEffect: 'spawn' | 'despawn' | null;
  /** Timer counting up from 0 to MATRIX_EFFECT_DURATION */
  matrixEffectTimer: number;
  /** Per-column random seeds (16 values) for staggered rain timing */
  matrixEffectSeeds: number[];
  /** Workspace folder name (only set for multi-root workspaces) */
  folderName?: string;
}
```

## File: `webview-ui/src/office/wallTiles.ts`
```typescript
/**
 * Wall tile auto-tiling: sprite storage and bitmask-based piece selection.
 *
 * Stores wall tile sets loaded from individual PNGs in assets/walls/.
 * Each set contains 16 wall sprites (one per 4-bit bitmask).
 * At render time, each wall tile's 4 cardinal neighbors are checked to build
 * a bitmask, and the corresponding sprite is drawn directly.
 * No changes to the layout model — auto-tiling is purely visual.
 *
 * Bitmask convention: N=1, E=2, S=4, W=8. Out-of-bounds = NOT wall.
 */

import { getColorizedSprite } from './colorize.js';
import type {
  FloorColor,
  FurnitureInstance,
  SpriteData,
  TileType as TileTypeVal,
} from './types.js';
import { TILE_SIZE, TileType } from './types.js';

/** Wall tile sets: each set has 16 sprites indexed by bitmask (0-15) */
let wallSets: SpriteData[][] = [];

/** Set wall tile sets (called once when extension sends wallTilesLoaded) */
export function setWallSprites(sets: SpriteData[][]): void {
  wallSets = sets;
}

/** Check if wall sprites have been loaded */
export function hasWallSprites(): boolean {
  return wallSets.length > 0;
}

/** Get number of available wall sets */
export function getWallSetCount(): number {
  return wallSets.length;
}

/** Get the first sprite (bitmask 0, top-left piece) of a wall set for preview rendering */
export function getWallSetPreviewSprite(setIndex: number): SpriteData | null {
  const set = wallSets[setIndex];
  if (!set) return null;
  return set[0] ?? null;
}

/**
 * Build the 4-bit neighbor bitmask for a wall tile at (col, row).
 */
function buildWallMask(col: number, row: number, tileMap: TileTypeVal[][]): number {
  const tmRows = tileMap.length;
  const tmCols = tmRows > 0 ? tileMap[0].length : 0;

  let mask = 0;
  if (row > 0 && tileMap[row - 1][col] === TileType.WALL) mask |= 1; // N
  if (col < tmCols - 1 && tileMap[row][col + 1] === TileType.WALL) mask |= 2; // E
  if (row < tmRows - 1 && tileMap[row + 1][col] === TileType.WALL) mask |= 4; // S
  if (col > 0 && tileMap[row][col - 1] === TileType.WALL) mask |= 8; // W
  return mask;
}

/**
 * Get the wall sprite for a tile based on its cardinal neighbors.
 * Returns the sprite + Y offset, or null to fall back to solid WALL_COLOR.
 */
export function getWallSprite(
  col: number,
  row: number,
  tileMap: TileTypeVal[][],
  setIndex = 0,
): { sprite: SpriteData; offsetY: number } | null {
  if (wallSets.length === 0) return null;
  const sprites = wallSets[setIndex] ?? wallSets[0];

  const mask = buildWallMask(col, row, tileMap);
  const sprite = sprites[mask];
  if (!sprite) return null;

  // Anchor sprite at bottom of tile — tall sprites extend upward
  return { sprite, offsetY: TILE_SIZE - sprite.length };
}

/**
 * Get a colorized wall sprite for a tile based on its cardinal neighbors.
 * Uses Colorize mode (grayscale → HSL) like floor tiles.
 * Returns the colorized sprite + Y offset, or null if no wall sprites loaded.
 */
export function getColorizedWallSprite(
  col: number,
  row: number,
  tileMap: TileTypeVal[][],
  color: FloorColor,
  setIndex = 0,
): { sprite: SpriteData; offsetY: number } | null {
  if (wallSets.length === 0) return null;
  const sprites = wallSets[setIndex] ?? wallSets[0];

  const mask = buildWallMask(col, row, tileMap);
  const sprite = sprites[mask];
  if (!sprite) return null;

  const cacheKey = `wall-${setIndex}-${mask}-${color.h}-${color.s}-${color.b}-${color.c}`;
  const colorized = getColorizedSprite(cacheKey, sprite, { ...color, colorize: true });

  return { sprite: colorized, offsetY: TILE_SIZE - sprite.length };
}

/**
 * Build FurnitureInstance-like objects for all wall tiles so they can participate
 * in z-sorting with furniture and characters.
 */
export function getWallInstances(
  tileMap: TileTypeVal[][],
  tileColors?: Array<FloorColor | null>,
  cols?: number,
): FurnitureInstance[] {
  if (wallSets.length === 0) return [];
  const tmRows = tileMap.length;
  const tmCols = tmRows > 0 ? tileMap[0].length : 0;
  const layoutCols = cols ?? tmCols;
  const instances: FurnitureInstance[] = [];
  for (let r = 0; r < tmRows; r++) {
    for (let c = 0; c < tmCols; c++) {
      if (tileMap[r][c] !== TileType.WALL) continue;
      const colorIdx = r * layoutCols + c;
      const wallColor = tileColors?.[colorIdx];
      const wallInfo = wallColor
        ? getColorizedWallSprite(c, r, tileMap, wallColor)
        : getWallSprite(c, r, tileMap);
      if (!wallInfo) continue;
      instances.push({
        sprite: wallInfo.sprite,
        x: c * TILE_SIZE,
        y: r * TILE_SIZE + wallInfo.offsetY,
        zY: (r + 1) * TILE_SIZE,
      });
    }
  }
  return instances;
}

/**
 * Compute the flat fill hex color for a wall tile with a given FloorColor.
 * Uses same Colorize algorithm as floor tiles: 50% gray → HSL.
 */
export function wallColorToHex(color: FloorColor): string {
  const { h, s, b, c } = color;
  // Start with 50% gray (wall base)
  let lightness = 0.5;

  // Apply contrast
  if (c !== 0) {
    const factor = (100 + c) / 100;
    lightness = 0.5 + (lightness - 0.5) * factor;
  }

  // Apply brightness
  if (b !== 0) {
    lightness = lightness + b / 200;
  }

  lightness = Math.max(0, Math.min(1, lightness));

  // HSL to hex (same as colorize.ts hslToHex)
  const satFrac = s / 100;
  const ch = (1 - Math.abs(2 * lightness - 1)) * satFrac;
  const hp = h / 60;
  const x = ch * (1 - Math.abs((hp % 2) - 1));
  let r1 = 0,
    g1 = 0,
    b1 = 0;

  if (hp < 1) {
    r1 = ch;
    g1 = x;
    b1 = 0;
  } else if (hp < 2) {
    r1 = x;
    g1 = ch;
    b1 = 0;
  } else if (hp < 3) {
    r1 = 0;
    g1 = ch;
    b1 = x;
  } else if (hp < 4) {
    r1 = 0;
    g1 = x;
    b1 = ch;
  } else if (hp < 5) {
    r1 = x;
    g1 = 0;
    b1 = ch;
  } else {
    r1 = ch;
    g1 = 0;
    b1 = x;
  }

  const m = lightness - ch / 2;
  const clamp = (v: number) => Math.max(0, Math.min(255, Math.round((v + m) * 255)));

  return `#${clamp(r1).toString(16).padStart(2, '0')}${clamp(g1).toString(16).padStart(2, '0')}${clamp(b1).toString(16).padStart(2, '0')}`;
}
```

## File: `webview-ui/src/office/components/index.ts`
```typescript
export { OfficeCanvas } from './OfficeCanvas.js';
export { ToolOverlay } from './ToolOverlay.js';
```

## File: `webview-ui/src/office/components/OfficeCanvas.tsx`
```tsx
import { useCallback, useEffect, useRef } from 'react';

import {
  CAMERA_FOLLOW_LERP,
  CAMERA_FOLLOW_SNAP_THRESHOLD,
  PAN_MARGIN_FRACTION,
  ZOOM_MAX,
  ZOOM_MIN,
  ZOOM_SCROLL_THRESHOLD,
} from '../../constants.js';
import { unlockAudio } from '../../notificationSound.js';
import { vscode } from '../../vscodeApi.js';
import { canPlaceFurniture, getWallPlacementRow } from '../editor/editorActions.js';
import type { EditorState } from '../editor/editorState.js';
import { startGameLoop } from '../engine/gameLoop.js';
import type { OfficeState } from '../engine/officeState.js';
import type {
  DeleteButtonBounds,
  EditorRenderState,
  RotateButtonBounds,
  SelectionRenderState,
} from '../engine/renderer.js';
import { renderFrame } from '../engine/renderer.js';
import { getCatalogEntry, isRotatable } from '../layout/furnitureCatalog.js';
import { EditTool, TILE_SIZE } from '../types.js';

interface OfficeCanvasProps {
  officeState: OfficeState;
  onClick: (agentId: number) => void;
  isEditMode: boolean;
  editorState: EditorState;
  onEditorTileAction: (col: number, row: number) => void;
  onEditorEraseAction: (col: number, row: number) => void;
  onEditorSelectionChange: () => void;
  onDeleteSelected: () => void;
  onRotateSelected: () => void;
  onDragMove: (uid: string, newCol: number, newRow: number) => void;
  editorTick: number;
  zoom: number;
  onZoomChange: (zoom: number) => void;
  panRef: React.MutableRefObject<{ x: number; y: number }>;
}

export function OfficeCanvas({
  officeState,
  onClick,
  isEditMode,
  editorState,
  onEditorTileAction,
  onEditorEraseAction,
  onEditorSelectionChange,
  onDeleteSelected,
  onRotateSelected,
  onDragMove,
  editorTick: _editorTick,
  zoom,
  onZoomChange,
  panRef,
}: OfficeCanvasProps) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const offsetRef = useRef({ x: 0, y: 0 });
  // Middle-mouse pan state (imperative, no re-renders)
  const isPanningRef = useRef(false);
  const panStartRef = useRef({ mouseX: 0, mouseY: 0, panX: 0, panY: 0 });
  // Delete/rotate button bounds (updated each frame by renderer)
  const deleteButtonBoundsRef = useRef<DeleteButtonBounds | null>(null);
  const rotateButtonBoundsRef = useRef<RotateButtonBounds | null>(null);
  // Right-click erase dragging
  const isEraseDraggingRef = useRef(false);
  // Zoom scroll accumulator for trackpad pinch sensitivity
  const zoomAccumulatorRef = useRef(0);

  // Clamp pan so the map edge can't go past a margin inside the viewport
  const clampPan = useCallback(
    (px: number, py: number): { x: number; y: number } => {
      const canvas = canvasRef.current;
      if (!canvas) return { x: px, y: py };
      const layout = officeState.getLayout();
      const mapW = layout.cols * TILE_SIZE * zoom;
      const mapH = layout.rows * TILE_SIZE * zoom;
      const marginX = canvas.width * PAN_MARGIN_FRACTION;
      const marginY = canvas.height * PAN_MARGIN_FRACTION;
      const maxPanX = mapW / 2 + canvas.width / 2 - marginX;
      const maxPanY = mapH / 2 + canvas.height / 2 - marginY;
      return {
        x: Math.max(-maxPanX, Math.min(maxPanX, px)),
        y: Math.max(-maxPanY, Math.min(maxPanY, py)),
      };
    },
    [officeState, zoom],
  );

  // Resize canvas backing store to device pixels (no DPR transform on ctx)
  const resizeCanvas = useCallback(() => {
    const canvas = canvasRef.current;
    const container = containerRef.current;
    if (!canvas || !container) return;
    const rect = container.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);
    canvas.style.width = `${rect.width}px`;
    canvas.style.height = `${rect.height}px`;
    // No ctx.scale(dpr) — we render directly in device pixels
  }, []);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    resizeCanvas();

    const observer = new ResizeObserver(() => resizeCanvas());
    if (containerRef.current) {
      observer.observe(containerRef.current);
    }

    const stop = startGameLoop(canvas, {
      update: (dt) => {
        officeState.update(dt);
      },
      render: (ctx) => {
        // Canvas dimensions are in device pixels
        const w = canvas.width;
        const h = canvas.height;

        // Build editor render state
        let editorRender: EditorRenderState | undefined;
        if (isEditMode) {
          const showGhostBorder =
            editorState.activeTool === EditTool.TILE_PAINT ||
            editorState.activeTool === EditTool.WALL_PAINT ||
            editorState.activeTool === EditTool.ERASE;
          editorRender = {
            showGrid: true,
            ghostSprite: null,
            ghostMirrored: false,
            ghostCol: editorState.ghostCol,
            ghostRow: editorState.ghostRow,
            ghostValid: editorState.ghostValid,
            selectedCol: 0,
            selectedRow: 0,
            selectedW: 0,
            selectedH: 0,
            hasSelection: false,
            isRotatable: false,
            deleteButtonBounds: null,
            rotateButtonBounds: null,
            showGhostBorder,
            ghostBorderHoverCol: showGhostBorder ? editorState.ghostCol : -999,
            ghostBorderHoverRow: showGhostBorder ? editorState.ghostRow : -999,
          };

          // Ghost preview for furniture placement
          if (editorState.activeTool === EditTool.FURNITURE_PLACE && editorState.ghostCol >= 0) {
            const entry = getCatalogEntry(editorState.selectedFurnitureType);
            if (entry) {
              const placementRow = getWallPlacementRow(
                editorState.selectedFurnitureType,
                editorState.ghostRow,
              );
              editorRender.ghostSprite = entry.sprite;
              editorRender.ghostRow = placementRow;
              editorRender.ghostMirrored =
                !!entry.mirrorSide && editorState.selectedFurnitureType.endsWith(':left');
              editorRender.ghostValid = canPlaceFurniture(
                officeState.getLayout(),
                editorState.selectedFurnitureType,
                editorState.ghostCol,
                placementRow,
              );
            }
          }

          // Ghost preview for drag-to-move
          if (editorState.isDragMoving && editorState.dragUid && editorState.ghostCol >= 0) {
            const draggedItem = officeState
              .getLayout()
              .furniture.find((f) => f.uid === editorState.dragUid);
            if (draggedItem) {
              const entry = getCatalogEntry(draggedItem.type);
              if (entry) {
                const ghostCol = editorState.ghostCol - editorState.dragOffsetCol;
                const ghostRow = editorState.ghostRow - editorState.dragOffsetRow;
                editorRender.ghostSprite = entry.sprite;
                editorRender.ghostCol = ghostCol;
                editorRender.ghostRow = ghostRow;
                editorRender.ghostMirrored =
                  !!entry.mirrorSide && draggedItem.type.endsWith(':left');
                editorRender.ghostValid = canPlaceFurniture(
                  officeState.getLayout(),
                  draggedItem.type,
                  ghostCol,
                  ghostRow,
                  editorState.dragUid,
                );
              }
            }
          }

          // Selection highlight
          if (editorState.selectedFurnitureUid && !editorState.isDragMoving) {
            const item = officeState
              .getLayout()
              .furniture.find((f) => f.uid === editorState.selectedFurnitureUid);
            if (item) {
              const entry = getCatalogEntry(item.type);
              if (entry) {
                editorRender.hasSelection = true;
                editorRender.selectedCol = item.col;
                editorRender.selectedRow = item.row;
                editorRender.selectedW = entry.footprintW;
                editorRender.selectedH = entry.footprintH;
                editorRender.isRotatable = isRotatable(item.type);
              }
            }
          }
        }

        // Camera follow: smoothly center on followed agent
        if (officeState.cameraFollowId !== null) {
          const followCh = officeState.characters.get(officeState.cameraFollowId);
          if (followCh) {
            const layout = officeState.getLayout();
            const mapW = layout.cols * TILE_SIZE * zoom;
            const mapH = layout.rows * TILE_SIZE * zoom;
            const targetX = mapW / 2 - followCh.x * zoom;
            const targetY = mapH / 2 - followCh.y * zoom;
            const dx = targetX - panRef.current.x;
            const dy = targetY - panRef.current.y;
            if (
              Math.abs(dx) < CAMERA_FOLLOW_SNAP_THRESHOLD &&
              Math.abs(dy) < CAMERA_FOLLOW_SNAP_THRESHOLD
            ) {
              panRef.current = { x: targetX, y: targetY };
            } else {
              panRef.current = {
                x: panRef.current.x + dx * CAMERA_FOLLOW_LERP,
                y: panRef.current.y + dy * CAMERA_FOLLOW_LERP,
              };
            }
          }
        }

        // Build selection render state
        const selectionRender: SelectionRenderState = {
          selectedAgentId: officeState.selectedAgentId,
          hoveredAgentId: officeState.hoveredAgentId,
          hoveredTile: officeState.hoveredTile,
          seats: officeState.seats,
          characters: officeState.characters,
        };

        const { offsetX, offsetY } = renderFrame(
          ctx,
          w,
          h,
          officeState.tileMap,
          officeState.furniture,
          officeState.getCharacters(),
          zoom,
          panRef.current.x,
          panRef.current.y,
          selectionRender,
          editorRender,
          officeState.getLayout().tileColors,
          officeState.getLayout().cols,
          officeState.getLayout().rows,
        );
        offsetRef.current = { x: offsetX, y: offsetY };

        // Store delete/rotate button bounds for hit-testing
        deleteButtonBoundsRef.current = editorRender?.deleteButtonBounds ?? null;
        rotateButtonBoundsRef.current = editorRender?.rotateButtonBounds ?? null;
      },
    });

    return () => {
      stop();
      observer.disconnect();
    };
  }, [officeState, resizeCanvas, isEditMode, editorState, _editorTick, zoom, panRef]);

  // Convert CSS mouse coords to world (sprite pixel) coords
  const screenToWorld = useCallback(
    (clientX: number, clientY: number) => {
      const canvas = canvasRef.current;
      if (!canvas) return null;
      const rect = canvas.getBoundingClientRect();
      const dpr = window.devicePixelRatio || 1;
      // CSS coords relative to canvas
      const cssX = clientX - rect.left;
      const cssY = clientY - rect.top;
      // Convert to device pixels
      const deviceX = cssX * dpr;
      const deviceY = cssY * dpr;
      // Convert to world (sprite pixel) coords
      const worldX = (deviceX - offsetRef.current.x) / zoom;
      const worldY = (deviceY - offsetRef.current.y) / zoom;
      return { worldX, worldY, screenX: cssX, screenY: cssY, deviceX, deviceY };
    },
    [zoom],
  );

  const screenToTile = useCallback(
    (clientX: number, clientY: number): { col: number; row: number } | null => {
      const pos = screenToWorld(clientX, clientY);
      if (!pos) return null;
      const col = Math.floor(pos.worldX / TILE_SIZE);
      const row = Math.floor(pos.worldY / TILE_SIZE);
      const layout = officeState.getLayout();
      // In edit mode with floor/wall/erase tool, extend valid range by 1 for ghost border
      if (
        isEditMode &&
        (editorState.activeTool === EditTool.TILE_PAINT ||
          editorState.activeTool === EditTool.WALL_PAINT ||
          editorState.activeTool === EditTool.ERASE)
      ) {
        if (col < -1 || col > layout.cols || row < -1 || row > layout.rows) return null;
        return { col, row };
      }
      if (col < 0 || col >= layout.cols || row < 0 || row >= layout.rows) return null;
      return { col, row };
    },
    [screenToWorld, officeState, isEditMode, editorState],
  );

  // Check if device-pixel coords hit the delete button
  const hitTestDeleteButton = useCallback((deviceX: number, deviceY: number): boolean => {
    const bounds = deleteButtonBoundsRef.current;
    if (!bounds) return false;
    const dx = deviceX - bounds.cx;
    const dy = deviceY - bounds.cy;
    return dx * dx + dy * dy <= (bounds.radius + 2) * (bounds.radius + 2); // small padding
  }, []);

  // Check if device-pixel coords hit the rotate button
  const hitTestRotateButton = useCallback((deviceX: number, deviceY: number): boolean => {
    const bounds = rotateButtonBoundsRef.current;
    if (!bounds) return false;
    const dx = deviceX - bounds.cx;
    const dy = deviceY - bounds.cy;
    return dx * dx + dy * dy <= (bounds.radius + 2) * (bounds.radius + 2);
  }, []);

  const handleMouseMove = useCallback(
    (e: React.MouseEvent) => {
      // Handle middle-mouse panning
      if (isPanningRef.current) {
        const dpr = window.devicePixelRatio || 1;
        const dx = (e.clientX - panStartRef.current.mouseX) * dpr;
        const dy = (e.clientY - panStartRef.current.mouseY) * dpr;
        panRef.current = clampPan(panStartRef.current.panX + dx, panStartRef.current.panY + dy);
        return;
      }

      if (isEditMode) {
        const tile = screenToTile(e.clientX, e.clientY);
        if (tile) {
          editorState.ghostCol = tile.col;
          editorState.ghostRow = tile.row;

          // Drag-to-move: check if cursor moved to different tile
          if (editorState.dragUid && !editorState.isDragMoving) {
            if (tile.col !== editorState.dragStartCol || tile.row !== editorState.dragStartRow) {
              editorState.isDragMoving = true;
            }
          }

          // Paint on drag (tile/wall/erase paint tool only, not during furniture drag)
          if (
            editorState.isDragging &&
            (editorState.activeTool === EditTool.TILE_PAINT ||
              editorState.activeTool === EditTool.WALL_PAINT ||
              editorState.activeTool === EditTool.ERASE) &&
            !editorState.dragUid
          ) {
            onEditorTileAction(tile.col, tile.row);
          }
          // Right-click erase drag
          if (
            isEraseDraggingRef.current &&
            (editorState.activeTool === EditTool.TILE_PAINT ||
              editorState.activeTool === EditTool.WALL_PAINT ||
              editorState.activeTool === EditTool.ERASE)
          ) {
            const layout = officeState.getLayout();
            if (
              tile.col >= 0 &&
              tile.col < layout.cols &&
              tile.row >= 0 &&
              tile.row < layout.rows
            ) {
              onEditorEraseAction(tile.col, tile.row);
            }
          }
        } else {
          editorState.ghostCol = -1;
          editorState.ghostRow = -1;
        }

        // Cursor: show grab during drag, pointer over delete button, crosshair otherwise
        const canvas = canvasRef.current;
        if (canvas) {
          if (editorState.isDragMoving) {
            canvas.style.cursor = 'grabbing';
          } else {
            const pos = screenToWorld(e.clientX, e.clientY);
            if (
              pos &&
              (hitTestDeleteButton(pos.deviceX, pos.deviceY) ||
                hitTestRotateButton(pos.deviceX, pos.deviceY))
            ) {
              canvas.style.cursor = 'pointer';
            } else if (editorState.activeTool === EditTool.FURNITURE_PICK && tile) {
              // Pick mode: show pointer over furniture, crosshair elsewhere
              const layout = officeState.getLayout();
              const hitFurniture = layout.furniture.find((f) => {
                const entry = getCatalogEntry(f.type);
                if (!entry) return false;
                return (
                  tile.col >= f.col &&
                  tile.col < f.col + entry.footprintW &&
                  tile.row >= f.row &&
                  tile.row < f.row + entry.footprintH
                );
              });
              canvas.style.cursor = hitFurniture ? 'pointer' : 'crosshair';
            } else if (
              (editorState.activeTool === EditTool.SELECT ||
                (editorState.activeTool === EditTool.FURNITURE_PLACE &&
                  editorState.selectedFurnitureType === '')) &&
              tile
            ) {
              // Check if hovering over furniture
              const layout = officeState.getLayout();
              const hitFurniture = layout.furniture.find((f) => {
                const entry = getCatalogEntry(f.type);
                if (!entry) return false;
                return (
                  tile.col >= f.col &&
                  tile.col < f.col + entry.footprintW &&
                  tile.row >= f.row &&
                  tile.row < f.row + entry.footprintH
                );
              });
              canvas.style.cursor = hitFurniture ? 'grab' : 'crosshair';
            } else {
              canvas.style.cursor = 'crosshair';
            }
          }
        }
        return;
      }

      const pos = screenToWorld(e.clientX, e.clientY);
      if (!pos) return;
      const hitId = officeState.getCharacterAt(pos.worldX, pos.worldY);
      const tile = screenToTile(e.clientX, e.clientY);
      officeState.hoveredTile = tile;
      const canvas = canvasRef.current;
      if (canvas) {
        let cursor = 'default';
        if (hitId !== null) {
          cursor = 'pointer';
        } else if (officeState.selectedAgentId !== null && tile) {
          // Check if hovering over a clickable seat (available or own)
          const seatId = officeState.getSeatAtTile(tile.col, tile.row);
          if (seatId) {
            const seat = officeState.seats.get(seatId);
            if (seat) {
              const selectedCh = officeState.characters.get(officeState.selectedAgentId);
              if (!seat.assigned || (selectedCh && selectedCh.seatId === seatId)) {
                cursor = 'pointer';
              }
            }
          }
        }
        canvas.style.cursor = cursor;
      }
      officeState.hoveredAgentId = hitId;
    },
    [
      officeState,
      screenToWorld,
      screenToTile,
      isEditMode,
      editorState,
      onEditorTileAction,
      onEditorEraseAction,
      panRef,
      hitTestDeleteButton,
      hitTestRotateButton,
      clampPan,
    ],
  );

  const handleMouseDown = useCallback(
    (e: React.MouseEvent) => {
      unlockAudio();
      // Middle mouse button (button 1) starts panning
      if (e.button === 1) {
        e.preventDefault();
        // Break camera follow on manual pan
        officeState.cameraFollowId = null;
        isPanningRef.current = true;
        panStartRef.current = {
          mouseX: e.clientX,
          mouseY: e.clientY,
          panX: panRef.current.x,
          panY: panRef.current.y,
        };
        const canvas = canvasRef.current;
        if (canvas) canvas.style.cursor = 'grabbing';
        return;
      }

      // Right-click in edit mode for erasing
      if (e.button === 2 && isEditMode) {
        const tile = screenToTile(e.clientX, e.clientY);
        if (
          tile &&
          (editorState.activeTool === EditTool.TILE_PAINT ||
            editorState.activeTool === EditTool.WALL_PAINT ||
            editorState.activeTool === EditTool.ERASE)
        ) {
          const layout = officeState.getLayout();
          if (tile.col >= 0 && tile.col < layout.cols && tile.row >= 0 && tile.row < layout.rows) {
            isEraseDraggingRef.current = true;
            onEditorEraseAction(tile.col, tile.row);
          }
        }
        return;
      }

      if (!isEditMode) return;

      // Check rotate/delete button hit first
      const pos = screenToWorld(e.clientX, e.clientY);
      if (pos && hitTestRotateButton(pos.deviceX, pos.deviceY)) {
        onRotateSelected();
        return;
      }
      if (pos && hitTestDeleteButton(pos.deviceX, pos.deviceY)) {
        onDeleteSelected();
        return;
      }

      const tile = screenToTile(e.clientX, e.clientY);

      // SELECT tool (or furniture tool with nothing selected): check for furniture hit to start drag
      const actAsSelect =
        editorState.activeTool === EditTool.SELECT ||
        (editorState.activeTool === EditTool.FURNITURE_PLACE &&
          editorState.selectedFurnitureType === '');
      if (actAsSelect && tile) {
        const layout = officeState.getLayout();
        // Find all furniture at clicked tile, prefer surface items (on top of desks)
        let hitFurniture = null as (typeof layout.furniture)[0] | null;
        for (const f of layout.furniture) {
          const entry = getCatalogEntry(f.type);
          if (!entry) continue;
          if (
            tile.col >= f.col &&
            tile.col < f.col + entry.footprintW &&
            tile.row >= f.row &&
            tile.row < f.row + entry.footprintH
          ) {
            if (!hitFurniture || entry.canPlaceOnSurfaces) hitFurniture = f;
          }
        }
        if (hitFurniture) {
          // Start drag — record offset from furniture's top-left
          editorState.startDrag(
            hitFurniture.uid,
            tile.col,
            tile.row,
            tile.col - hitFurniture.col,
            tile.row - hitFurniture.row,
          );
          return;
        } else {
          // Clicked empty space — deselect
          editorState.clearSelection();
          onEditorSelectionChange();
        }
      }

      // Non-select tools: start paint drag
      editorState.isDragging = true;
      if (tile) {
        onEditorTileAction(tile.col, tile.row);
      }
    },
    [
      officeState,
      isEditMode,
      editorState,
      screenToTile,
      screenToWorld,
      onEditorTileAction,
      onEditorEraseAction,
      onEditorSelectionChange,
      onDeleteSelected,
      onRotateSelected,
      hitTestDeleteButton,
      hitTestRotateButton,
      panRef,
    ],
  );

  const handleMouseUp = useCallback(
    (e: React.MouseEvent) => {
      if (e.button === 1) {
        isPanningRef.current = false;
        const canvas = canvasRef.current;
        if (canvas) canvas.style.cursor = isEditMode ? 'crosshair' : 'default';
        return;
      }
      if (e.button === 2) {
        isEraseDraggingRef.current = false;
        return;
      }

      // Handle drag-to-move completion
      if (editorState.dragUid) {
        if (editorState.isDragMoving) {
          // Compute target position
          const ghostCol = editorState.ghostCol - editorState.dragOffsetCol;
          const ghostRow = editorState.ghostRow - editorState.dragOffsetRow;
          const draggedItem = officeState
            .getLayout()
            .furniture.find((f) => f.uid === editorState.dragUid);
          if (draggedItem) {
            const valid = canPlaceFurniture(
              officeState.getLayout(),
              draggedItem.type,
              ghostCol,
              ghostRow,
              editorState.dragUid,
            );
            if (valid) {
              onDragMove(editorState.dragUid, ghostCol, ghostRow);
            }
          }
          editorState.clearSelection();
        } else {
          // Click (no movement) — toggle selection
          if (editorState.selectedFurnitureUid === editorState.dragUid) {
            editorState.clearSelection();
          } else {
            editorState.selectedFurnitureUid = editorState.dragUid;
          }
        }
        editorState.clearDrag();
        onEditorSelectionChange();
        const canvas = canvasRef.current;
        if (canvas) canvas.style.cursor = 'crosshair';
        return;
      }

      editorState.isDragging = false;
      editorState.wallDragAdding = null;
    },
    [editorState, isEditMode, officeState, onDragMove, onEditorSelectionChange],
  );

  const handleClick = useCallback(
    (e: React.MouseEvent) => {
      if (isEditMode) return; // handled by mouseDown/mouseUp
      const pos = screenToWorld(e.clientX, e.clientY);
      if (!pos) return;

      const hitId = officeState.getCharacterAt(pos.worldX, pos.worldY);
      if (hitId !== null) {
        // Dismiss any active bubble on click
        officeState.dismissBubble(hitId);
        // Toggle selection: click same agent deselects, different agent selects
        if (officeState.selectedAgentId === hitId) {
          officeState.selectedAgentId = null;
          officeState.cameraFollowId = null;
        } else {
          officeState.selectedAgentId = hitId;
          officeState.cameraFollowId = hitId;
        }
        onClick(hitId); // still focus terminal
        return;
      }

      // No agent hit — check seat click while agent is selected
      if (officeState.selectedAgentId !== null) {
        const selectedCh = officeState.characters.get(officeState.selectedAgentId);
        // Skip seat reassignment for sub-agents
        if (selectedCh && !selectedCh.isSubagent) {
          const tile = screenToTile(e.clientX, e.clientY);
          if (tile) {
            const seatId = officeState.getSeatAtTile(tile.col, tile.row);
            if (seatId) {
              const seat = officeState.seats.get(seatId);
              if (seat && selectedCh) {
                if (selectedCh.seatId === seatId) {
                  // Clicked own seat — send agent back to it
                  officeState.sendToSeat(officeState.selectedAgentId);
                  officeState.selectedAgentId = null;
                  officeState.cameraFollowId = null;
                  return;
                } else if (!seat.assigned) {
                  // Clicked available seat — reassign
                  officeState.reassignSeat(officeState.selectedAgentId, seatId);
                  officeState.selectedAgentId = null;
                  officeState.cameraFollowId = null;
                  // Persist seat assignments (exclude sub-agents)
                  const seats: Record<number, { palette: number; seatId: string | null }> = {};
                  for (const ch of officeState.characters.values()) {
                    if (ch.isSubagent) continue;
                    seats[ch.id] = { palette: ch.palette, seatId: ch.seatId };
                  }
                  vscode.postMessage({ type: 'saveAgentSeats', seats });
                  return;
                }
              }
            }
          }
        }
        // Clicked empty space — deselect
        officeState.selectedAgentId = null;
        officeState.cameraFollowId = null;
      }
    },
    [officeState, onClick, screenToWorld, screenToTile, isEditMode],
  );

  const handleMouseLeave = useCallback(() => {
    isPanningRef.current = false;
    isEraseDraggingRef.current = false;
    editorState.isDragging = false;
    editorState.wallDragAdding = null;
    editorState.clearDrag();
    editorState.ghostCol = -1;
    editorState.ghostRow = -1;
    officeState.hoveredAgentId = null;
    officeState.hoveredTile = null;
  }, [officeState, editorState]);

  const handleContextMenu = useCallback(
    (e: React.MouseEvent) => {
      e.preventDefault();
      if (isEditMode) return;
      // Right-click to walk selected agent to tile
      if (officeState.selectedAgentId !== null) {
        const tile = screenToTile(e.clientX, e.clientY);
        if (tile) {
          officeState.walkToTile(officeState.selectedAgentId, tile.col, tile.row);
        }
      }
    },
    [isEditMode, officeState, screenToTile],
  );

  // Wheel: Ctrl+wheel to zoom, plain wheel/trackpad to pan
  const handleWheel = useCallback(
    (e: React.WheelEvent) => {
      e.preventDefault();
      if (e.ctrlKey || e.metaKey) {
        // Accumulate scroll delta, step zoom when threshold crossed
        zoomAccumulatorRef.current += e.deltaY;
        if (Math.abs(zoomAccumulatorRef.current) >= ZOOM_SCROLL_THRESHOLD) {
          const delta = zoomAccumulatorRef.current < 0 ? 1 : -1;
          zoomAccumulatorRef.current = 0;
          const newZoom = Math.max(ZOOM_MIN, Math.min(ZOOM_MAX, zoom + delta));
          if (newZoom !== zoom) {
            onZoomChange(newZoom);
          }
        }
      } else {
        // Pan via trackpad two-finger scroll or mouse wheel
        const dpr = window.devicePixelRatio || 1;
        officeState.cameraFollowId = null;
        panRef.current = clampPan(
          panRef.current.x - e.deltaX * dpr,
          panRef.current.y - e.deltaY * dpr,
        );
      }
    },
    [zoom, onZoomChange, officeState, panRef, clampPan],
  );

  // Prevent default middle-click browser behavior (auto-scroll)
  const handleAuxClick = useCallback((e: React.MouseEvent) => {
    if (e.button === 1) e.preventDefault();
  }, []);

  return (
    <div
      ref={containerRef}
      style={{
        width: '100%',
        height: '100%',
        position: 'relative',
        overflow: 'hidden',
        background: '#1E1E2E',
      }}
    >
      <canvas
        ref={canvasRef}
        onMouseMove={handleMouseMove}
        onMouseDown={handleMouseDown}
        onMouseUp={handleMouseUp}
        onClick={handleClick}
        onAuxClick={handleAuxClick}
        onMouseLeave={handleMouseLeave}
        onWheel={handleWheel}
        onContextMenu={handleContextMenu}
        style={{ display: 'block' }}
      />
    </div>
  );
}
```

## File: `webview-ui/src/office/components/ToolOverlay.tsx`
```tsx
import { useEffect, useState } from 'react';

import { CHARACTER_SITTING_OFFSET_PX, TOOL_OVERLAY_VERTICAL_OFFSET } from '../../constants.js';
import type { SubagentCharacter } from '../../hooks/useExtensionMessages.js';
import type { OfficeState } from '../engine/officeState.js';
import type { ToolActivity } from '../types.js';
import { CharacterState, TILE_SIZE } from '../types.js';

interface ToolOverlayProps {
  officeState: OfficeState;
  agents: number[];
  agentTools: Record<number, ToolActivity[]>;
  subagentCharacters: SubagentCharacter[];
  containerRef: React.RefObject<HTMLDivElement | null>;
  zoom: number;
  panRef: React.RefObject<{ x: number; y: number }>;
  onCloseAgent: (id: number) => void;
}

/** Derive a short human-readable activity string from tools/status */
function getActivityText(
  agentId: number,
  agentTools: Record<number, ToolActivity[]>,
  isActive: boolean,
): string {
  const tools = agentTools[agentId];
  if (tools && tools.length > 0) {
    // Find the latest non-done tool
    const activeTool = [...tools].reverse().find((t) => !t.done);
    if (activeTool) {
      if (activeTool.permissionWait) return 'Needs approval';
      return activeTool.status;
    }
    // All tools done but agent still active (mid-turn) — keep showing last tool status
    if (isActive) {
      const lastTool = tools[tools.length - 1];
      if (lastTool) return lastTool.status;
    }
  }

  return 'Idle';
}

export function ToolOverlay({
  officeState,
  agents,
  agentTools,
  subagentCharacters,
  containerRef,
  zoom,
  panRef,
  onCloseAgent,
}: ToolOverlayProps) {
  const [, setTick] = useState(0);
  useEffect(() => {
    let rafId = 0;
    const tick = () => {
      setTick((n) => n + 1);
      rafId = requestAnimationFrame(tick);
    };
    rafId = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(rafId);
  }, []);

  const el = containerRef.current;
  if (!el) return null;
  const rect = el.getBoundingClientRect();
  const dpr = window.devicePixelRatio || 1;
  const canvasW = Math.round(rect.width * dpr);
  const canvasH = Math.round(rect.height * dpr);
  const layout = officeState.getLayout();
  const mapW = layout.cols * TILE_SIZE * zoom;
  const mapH = layout.rows * TILE_SIZE * zoom;
  const deviceOffsetX = Math.floor((canvasW - mapW) / 2) + Math.round(panRef.current.x);
  const deviceOffsetY = Math.floor((canvasH - mapH) / 2) + Math.round(panRef.current.y);

  const selectedId = officeState.selectedAgentId;
  const hoveredId = officeState.hoveredAgentId;

  // All character IDs
  const allIds = [...agents, ...subagentCharacters.map((s) => s.id)];

  return (
    <>
      {allIds.map((id) => {
        const ch = officeState.characters.get(id);
        if (!ch) return null;

        const isSelected = selectedId === id;
        const isHovered = hoveredId === id;
        const isSub = ch.isSubagent;

        // Only show for hovered or selected agents
        if (!isSelected && !isHovered) return null;

        // Position above character
        const sittingOffset = ch.state === CharacterState.TYPE ? CHARACTER_SITTING_OFFSET_PX : 0;
        const screenX = (deviceOffsetX + ch.x * zoom) / dpr;
        const screenY =
          (deviceOffsetY + (ch.y + sittingOffset - TOOL_OVERLAY_VERTICAL_OFFSET) * zoom) / dpr;

        // Get activity text
        const subHasPermission = isSub && ch.bubbleType === 'permission';
        let activityText: string;
        if (isSub) {
          if (subHasPermission) {
            activityText = 'Needs approval';
          } else {
            const sub = subagentCharacters.find((s) => s.id === id);
            activityText = sub ? sub.label : 'Subtask';
          }
        } else {
          activityText = getActivityText(id, agentTools, ch.isActive);
        }

        // Determine dot color
        const tools = agentTools[id];
        const hasPermission = subHasPermission || tools?.some((t) => t.permissionWait && !t.done);
        const hasActiveTools = tools?.some((t) => !t.done);
        const isActive = ch.isActive;

        let dotColor: string | null = null;
        if (hasPermission) {
          dotColor = 'var(--pixel-status-permission)';
        } else if (isActive && hasActiveTools) {
          dotColor = 'var(--pixel-status-active)';
        }

        return (
          <div
            key={id}
            style={{
              position: 'absolute',
              left: screenX,
              top: screenY - 24,
              transform: 'translateX(-50%)',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              pointerEvents: isSelected ? 'auto' : 'none',
              zIndex: isSelected ? 'var(--pixel-overlay-selected-z)' : 'var(--pixel-overlay-z)',
            }}
          >
            <div
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 5,
                background: 'var(--pixel-bg)',
                border: isSelected
                  ? '2px solid var(--pixel-border-light)'
                  : '2px solid var(--pixel-border)',
                borderRadius: 0,
                padding: isSelected ? '3px 6px 3px 8px' : '3px 8px',
                boxShadow: 'var(--pixel-shadow)',
                whiteSpace: 'nowrap',
                maxWidth: 220,
              }}
            >
              {dotColor && (
                <span
                  className={isActive && !hasPermission ? 'pixel-agents-pulse' : undefined}
                  style={{
                    width: 6,
                    height: 6,
                    borderRadius: '50%',
                    background: dotColor,
                    flexShrink: 0,
                  }}
                />
              )}
              <div style={{ overflow: 'hidden' }}>
                <span
                  style={{
                    fontSize: isSub ? '20px' : '22px',
                    fontStyle: isSub ? 'italic' : undefined,
                    color: 'var(--vscode-foreground)',
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    display: 'block',
                  }}
                >
                  {activityText}
                </span>
                {ch.folderName && (
                  <span
                    style={{
                      fontSize: '16px',
                      color: 'var(--pixel-text-dim)',
                      overflow: 'hidden',
                      textOverflow: 'ellipsis',
                      display: 'block',
                    }}
                  >
                    {ch.folderName}
                  </span>
                )}
              </div>
              {isSelected && !isSub && (
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    onCloseAgent(id);
                  }}
                  title="Close agent"
                  style={{
                    background: 'none',
                    border: 'none',
                    color: 'var(--pixel-close-text)',
                    cursor: 'pointer',
                    padding: '0 2px',
                    fontSize: '26px',
                    lineHeight: 1,
                    marginLeft: 2,
                    flexShrink: 0,
                  }}
                  onMouseEnter={(e) => {
                    (e.currentTarget as HTMLElement).style.color = 'var(--pixel-close-hover)';
                  }}
                  onMouseLeave={(e) => {
                    (e.currentTarget as HTMLElement).style.color = 'var(--pixel-close-text)';
                  }}
                >
                  ×
                </button>
              )}
            </div>
          </div>
        );
      })}
    </>
  );
}
```

## File: `webview-ui/src/office/editor/editorActions.ts`
```typescript
import { DEFAULT_NEUTRAL_COLOR } from '../../constants.js';
import { getCatalogEntry, getRotatedType, getToggledType } from '../layout/furnitureCatalog.js';
import { getPlacementBlockedTiles } from '../layout/layoutSerializer.js';
import type {
  FloorColor,
  OfficeLayout,
  PlacedFurniture,
  TileType as TileTypeVal,
} from '../types.js';
import { MAX_COLS, MAX_ROWS, TileType } from '../types.js';

/** Paint a single tile with pattern and color. Returns new layout (immutable). */
export function paintTile(
  layout: OfficeLayout,
  col: number,
  row: number,
  tileType: TileTypeVal,
  color?: FloorColor,
): OfficeLayout {
  const idx = row * layout.cols + col;
  if (idx < 0 || idx >= layout.tiles.length) return layout;

  const existingColors = layout.tileColors || new Array(layout.tiles.length).fill(null);
  const newColor =
    color ??
    (tileType === TileType.WALL || tileType === TileType.VOID
      ? null
      : { ...DEFAULT_NEUTRAL_COLOR });

  // Check if anything actually changed
  if (layout.tiles[idx] === tileType) {
    const existingColor = existingColors[idx];
    if (newColor === null && existingColor === null) return layout;
    if (
      newColor &&
      existingColor &&
      newColor.h === existingColor.h &&
      newColor.s === existingColor.s &&
      newColor.b === existingColor.b &&
      newColor.c === existingColor.c &&
      !!newColor.colorize === !!existingColor.colorize
    )
      return layout;
  }

  const tiles = [...layout.tiles];
  tiles[idx] = tileType;
  const tileColors = [...existingColors];
  tileColors[idx] = newColor;
  return { ...layout, tiles, tileColors };
}

/** Place furniture. Returns new layout (immutable). */
export function placeFurniture(layout: OfficeLayout, item: PlacedFurniture): OfficeLayout {
  if (!canPlaceFurniture(layout, item.type, item.col, item.row)) return layout;
  return { ...layout, furniture: [...layout.furniture, item] };
}

/** Remove furniture by uid. Returns new layout (immutable). */
export function removeFurniture(layout: OfficeLayout, uid: string): OfficeLayout {
  const filtered = layout.furniture.filter((f) => f.uid !== uid);
  if (filtered.length === layout.furniture.length) return layout;
  return { ...layout, furniture: filtered };
}

/** Move furniture to new position. Returns new layout (immutable). */
export function moveFurniture(
  layout: OfficeLayout,
  uid: string,
  newCol: number,
  newRow: number,
): OfficeLayout {
  const item = layout.furniture.find((f) => f.uid === uid);
  if (!item) return layout;
  if (!canPlaceFurniture(layout, item.type, newCol, newRow, uid)) return layout;
  return {
    ...layout,
    furniture: layout.furniture.map((f) =>
      f.uid === uid ? { ...f, col: newCol, row: newRow } : f,
    ),
  };
}

/** Rotate furniture to the next orientation. Returns new layout (immutable). */
export function rotateFurniture(
  layout: OfficeLayout,
  uid: string,
  direction: 'cw' | 'ccw',
): OfficeLayout {
  const item = layout.furniture.find((f) => f.uid === uid);
  if (!item) return layout;
  const newType = getRotatedType(item.type, direction);
  if (!newType) return layout;
  return {
    ...layout,
    furniture: layout.furniture.map((f) => (f.uid === uid ? { ...f, type: newType } : f)),
  };
}

/** Toggle furniture state (on/off). Returns new layout (immutable). */
export function toggleFurnitureState(layout: OfficeLayout, uid: string): OfficeLayout {
  const item = layout.furniture.find((f) => f.uid === uid);
  if (!item) return layout;
  const newType = getToggledType(item.type);
  if (!newType) return layout;
  return {
    ...layout,
    furniture: layout.furniture.map((f) => (f.uid === uid ? { ...f, type: newType } : f)),
  };
}

/** For wall items, offset the row so the bottom row aligns with the hovered tile. */
export function getWallPlacementRow(type: string, row: number): number {
  const entry = getCatalogEntry(type);
  if (!entry?.canPlaceOnWalls) return row;
  return row - (entry.footprintH - 1);
}

/** Check if furniture can be placed at (col, row) without overlapping. */
export function canPlaceFurniture(
  layout: OfficeLayout,
  type: string, // FurnitureType enum or asset ID
  col: number,
  row: number,
  excludeUid?: string,
): boolean {
  const entry = getCatalogEntry(type);
  if (!entry) return false;

  // Check bounds — wall items may extend above the map (top rows hang above the wall)
  if (entry.canPlaceOnWalls) {
    const bottomRow = row + entry.footprintH - 1;
    if (
      col < 0 ||
      col + entry.footprintW > layout.cols ||
      bottomRow < 0 ||
      bottomRow >= layout.rows
    ) {
      return false;
    }
  } else {
    if (
      col < 0 ||
      row < 0 ||
      col + entry.footprintW > layout.cols ||
      row + entry.footprintH > layout.rows
    ) {
      return false;
    }
  }

  // Wall/VOID placement check (background rows skip this check)
  const bgRows = entry.backgroundTiles || 0;
  for (let dr = 0; dr < entry.footprintH; dr++) {
    if (dr < bgRows) continue;
    if (row + dr < 0) continue; // row above map (wall items extending upward)
    // Wall items: only the bottom row must be on wall tiles; upper rows can overlap VOID/anything
    if (entry.canPlaceOnWalls && dr < entry.footprintH - 1) continue;
    for (let dc = 0; dc < entry.footprintW; dc++) {
      const idx = (row + dr) * layout.cols + (col + dc);
      const tileVal = layout.tiles[idx];
      if (entry.canPlaceOnWalls) {
        if (tileVal !== TileType.WALL) return false;
      } else {
        if (tileVal === TileType.VOID) return false; // Cannot place on VOID
        if (tileVal === TileType.WALL) return false; // Normal items cannot overlap walls
      }
    }
  }

  // Build occupied set excluding the item being moved, skipping background tile rows
  const occupied = getPlacementBlockedTiles(layout.furniture, excludeUid);

  // If this item can be placed on surfaces, build set of desk tiles to exclude from collision
  let deskTiles: Set<string> | null = null;
  if (entry.canPlaceOnSurfaces) {
    deskTiles = new Set<string>();
    for (const item of layout.furniture) {
      if (item.uid === excludeUid) continue;
      const itemEntry = getCatalogEntry(item.type);
      if (!itemEntry || !itemEntry.isDesk) continue;
      for (let dr = 0; dr < itemEntry.footprintH; dr++) {
        for (let dc = 0; dc < itemEntry.footprintW; dc++) {
          deskTiles.add(`${item.col + dc},${item.row + dr}`);
        }
      }
    }
  }

  // Check overlap — also skip the NEW item's own background rows
  const newBgRows = entry.backgroundTiles || 0;
  for (let dr = 0; dr < entry.footprintH; dr++) {
    if (dr < newBgRows) continue; // new item's background rows can overlap existing items
    if (row + dr < 0) continue; // row above map (wall items extending upward)
    for (let dc = 0; dc < entry.footprintW; dc++) {
      const key = `${col + dc},${row + dr}`;
      if (occupied.has(key) && !deskTiles?.has(key)) return false;
    }
  }

  return true;
}

export type ExpandDirection = 'left' | 'right' | 'up' | 'down';

/**
 * Expand layout by 1 tile in the given direction. New tiles are VOID.
 * Furniture and tile indices are shifted when expanding left or up.
 * Returns { layout, shift } or null if exceeding MAX_COLS/MAX_ROWS.
 */
export function expandLayout(
  layout: OfficeLayout,
  direction: ExpandDirection,
): { layout: OfficeLayout; shift: { col: number; row: number } } | null {
  const { cols, rows, tiles, furniture, tileColors } = layout;
  const existingColors = tileColors || new Array(tiles.length).fill(null);

  let newCols = cols;
  let newRows = rows;
  let shiftCol = 0;
  let shiftRow = 0;

  if (direction === 'right') {
    newCols = cols + 1;
  } else if (direction === 'left') {
    newCols = cols + 1;
    shiftCol = 1;
  } else if (direction === 'down') {
    newRows = rows + 1;
  } else if (direction === 'up') {
    newRows = rows + 1;
    shiftRow = 1;
  }

  if (newCols > MAX_COLS || newRows > MAX_ROWS) return null;

  // Build new tile array
  const newTiles: TileTypeVal[] = new Array(newCols * newRows).fill(TileType.VOID as TileTypeVal);
  const newColors: Array<FloorColor | null> = new Array(newCols * newRows).fill(null);

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const oldIdx = r * cols + c;
      const newIdx = (r + shiftRow) * newCols + (c + shiftCol);
      newTiles[newIdx] = tiles[oldIdx];
      newColors[newIdx] = existingColors[oldIdx];
    }
  }

  // Shift furniture positions
  const newFurniture: PlacedFurniture[] = furniture.map((f) => ({
    ...f,
    col: f.col + shiftCol,
    row: f.row + shiftRow,
  }));

  return {
    layout: {
      ...layout,
      cols: newCols,
      rows: newRows,
      tiles: newTiles,
      tileColors: newColors,
      furniture: newFurniture,
    },
    shift: { col: shiftCol, row: shiftRow },
  };
}
```

## File: `webview-ui/src/office/editor/editorState.ts`
```typescript
import { DEFAULT_FLOOR_COLOR, DEFAULT_WALL_COLOR, UNDO_STACK_MAX_SIZE } from '../../constants.js';
import type { FloorColor, OfficeLayout, TileType as TileTypeVal } from '../types.js';
import { EditTool, TileType } from '../types.js';

export class EditorState {
  isEditMode = false;
  activeTool: EditTool = EditTool.SELECT;
  selectedTileType: TileTypeVal = TileType.FLOOR_1;
  selectedFurnitureType = ''; // asset ID, set when catalog loads

  // Floor color settings (applied to new tiles when painting)
  floorColor: FloorColor = { ...DEFAULT_FLOOR_COLOR };

  // Wall color settings (applied to new wall tiles when painting)
  wallColor: FloorColor = { ...DEFAULT_WALL_COLOR };

  // Selected wall set index (0-based, indexes into loaded wall sets)
  selectedWallSet = 0;

  // Tracks toggle direction during wall drag (true=adding walls, false=removing, null=undecided)
  wallDragAdding: boolean | null = null;

  // Picked furniture color (copied by pick tool, applied on placement)
  pickedFurnitureColor: FloorColor | null = null;

  // Ghost preview position
  ghostCol = -1;
  ghostRow = -1;
  ghostValid = false;

  // Selection
  selectedFurnitureUid: string | null = null;

  // Mouse drag state (tile paint)
  isDragging = false;

  // Undo / Redo stacks
  undoStack: OfficeLayout[] = [];
  redoStack: OfficeLayout[] = [];

  // Dirty flag — true when layout differs from last save
  isDirty = false;

  // Drag-to-move state
  dragUid: string | null = null;
  dragStartCol = 0;
  dragStartRow = 0;
  dragOffsetCol = 0;
  dragOffsetRow = 0;
  isDragMoving = false;

  pushUndo(layout: OfficeLayout): void {
    this.undoStack.push(layout);
    // Limit undo stack size
    if (this.undoStack.length > UNDO_STACK_MAX_SIZE) {
      this.undoStack.shift();
    }
  }

  popUndo(): OfficeLayout | null {
    return this.undoStack.pop() || null;
  }

  pushRedo(layout: OfficeLayout): void {
    this.redoStack.push(layout);
    if (this.redoStack.length > UNDO_STACK_MAX_SIZE) {
      this.redoStack.shift();
    }
  }

  popRedo(): OfficeLayout | null {
    return this.redoStack.pop() || null;
  }

  clearRedo(): void {
    this.redoStack = [];
  }

  clearSelection(): void {
    this.selectedFurnitureUid = null;
  }

  clearGhost(): void {
    this.ghostCol = -1;
    this.ghostRow = -1;
    this.ghostValid = false;
  }

  startDrag(
    uid: string,
    startCol: number,
    startRow: number,
    offsetCol: number,
    offsetRow: number,
  ): void {
    this.dragUid = uid;
    this.dragStartCol = startCol;
    this.dragStartRow = startRow;
    this.dragOffsetCol = offsetCol;
    this.dragOffsetRow = offsetRow;
    this.isDragMoving = false;
  }

  clearDrag(): void {
    this.dragUid = null;
    this.isDragMoving = false;
  }

  reset(): void {
    this.activeTool = EditTool.SELECT;
    this.selectedFurnitureUid = null;
    this.ghostCol = -1;
    this.ghostRow = -1;
    this.ghostValid = false;
    this.isDragging = false;
    this.wallDragAdding = null;
    this.undoStack = [];
    this.redoStack = [];
    this.isDirty = false;
    this.dragUid = null;
    this.isDragMoving = false;
  }
}
```

## File: `webview-ui/src/office/editor/EditorToolbar.tsx`
```tsx
import { useCallback, useEffect, useRef, useState } from 'react';

import { getColorizedSprite } from '../colorize.js';
import { getColorizedFloorSprite, getFloorPatternCount, hasFloorSprites } from '../floorTiles.js';
import type { FurnitureCategory, LoadedAssetData } from '../layout/furnitureCatalog.js';
import { getWallSetCount, getWallSetPreviewSprite } from '../wallTiles.js';
import {
  buildDynamicCatalog,
  getActiveCategories,
  getCatalogByCategory,
} from '../layout/furnitureCatalog.js';
import { getCachedSprite } from '../sprites/spriteCache.js';
import type { FloorColor, TileType as TileTypeVal } from '../types.js';
import { EditTool } from '../types.js';

const btnStyle: React.CSSProperties = {
  padding: '3px 8px',
  fontSize: '22px',
  background: 'rgba(255, 255, 255, 0.08)',
  color: 'rgba(255, 255, 255, 0.7)',
  border: '2px solid transparent',
  borderRadius: 0,
  cursor: 'pointer',
};

const activeBtnStyle: React.CSSProperties = {
  ...btnStyle,
  background: 'rgba(90, 140, 255, 0.25)',
  color: 'rgba(255, 255, 255, 0.9)',
  border: '2px solid #5a8cff',
};

const tabStyle: React.CSSProperties = {
  padding: '2px 6px',
  fontSize: '20px',
  background: 'transparent',
  color: 'rgba(255, 255, 255, 0.5)',
  border: '2px solid transparent',
  borderRadius: 0,
  cursor: 'pointer',
};

const activeTabStyle: React.CSSProperties = {
  ...tabStyle,
  background: 'rgba(255, 255, 255, 0.08)',
  color: 'rgba(255, 255, 255, 0.8)',
  border: '2px solid #5a8cff',
};

interface EditorToolbarProps {
  activeTool: EditTool;
  selectedTileType: TileTypeVal;
  selectedFurnitureType: string;
  selectedFurnitureUid: string | null;
  selectedFurnitureColor: FloorColor | null;
  floorColor: FloorColor;
  wallColor: FloorColor;
  selectedWallSet: number;
  onToolChange: (tool: EditTool) => void;
  onTileTypeChange: (type: TileTypeVal) => void;
  onFloorColorChange: (color: FloorColor) => void;
  onWallColorChange: (color: FloorColor) => void;
  onWallSetChange: (setIndex: number) => void;
  onSelectedFurnitureColorChange: (color: FloorColor | null) => void;
  onFurnitureTypeChange: (type: string) => void;
  loadedAssets?: LoadedAssetData;
}

/** Render a floor pattern preview at 2x (32x32 canvas showing the 16x16 tile) */
function FloorPatternPreview({
  patternIndex,
  color,
  selected,
  onClick,
}: {
  patternIndex: number;
  color: FloorColor;
  selected: boolean;
  onClick: () => void;
}) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const displaySize = 32;
  const tileZoom = 2;

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    canvas.width = displaySize;
    canvas.height = displaySize;
    ctx.imageSmoothingEnabled = false;

    if (!hasFloorSprites()) {
      ctx.fillStyle = '#444';
      ctx.fillRect(0, 0, displaySize, displaySize);
      return;
    }

    const sprite = getColorizedFloorSprite(patternIndex, color);
    const cached = getCachedSprite(sprite, tileZoom);
    ctx.drawImage(cached, 0, 0);
  }, [patternIndex, color]);

  return (
    <button
      onClick={onClick}
      title={`Floor ${patternIndex}`}
      style={{
        width: displaySize,
        height: displaySize,
        padding: 0,
        border: selected ? '2px solid #5a8cff' : '2px solid #4a4a6a',
        borderRadius: 0,
        cursor: 'pointer',
        overflow: 'hidden',
        flexShrink: 0,
        background: '#2A2A3A',
      }}
    >
      <canvas
        ref={canvasRef}
        style={{ width: displaySize, height: displaySize, display: 'block' }}
      />
    </button>
  );
}

/** Render a wall set preview showing the first piece (bitmask 0, 16×32) at 1x scale */
function WallSetPreview({
  setIndex,
  color,
  selected,
  onClick,
}: {
  setIndex: number;
  color: FloorColor;
  selected: boolean;
  onClick: () => void;
}) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const displayW = 32;
  const displayH = 64;
  const previewZoom = 2;

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    canvas.width = displayW;
    canvas.height = displayH;
    ctx.imageSmoothingEnabled = false;

    const sprite = getWallSetPreviewSprite(setIndex);
    if (!sprite) {
      ctx.fillStyle = '#444';
      ctx.fillRect(0, 0, displayW, displayH);
      return;
    }

    // Colorize the preview sprite using the same colorize path as rendering
    const cacheKey = `wall-preview-${setIndex}-${color.h}-${color.s}-${color.b}-${color.c}`;
    const colorized = getColorizedSprite(cacheKey, sprite, { ...color, colorize: true });
    const cached = getCachedSprite(colorized, previewZoom);
    ctx.drawImage(cached, 0, 0);
  }, [setIndex, color]);

  return (
    <button
      onClick={onClick}
      title={`Wall ${setIndex + 1}`}
      style={{
        width: displayW,
        height: displayH,
        padding: 0,
        border: selected ? '2px solid #5a8cff' : '2px solid #4a4a6a',
        borderRadius: 0,
        cursor: 'pointer',
        overflow: 'hidden',
        flexShrink: 0,
        background: '#2A2A3A',
      }}
    >
      <canvas ref={canvasRef} style={{ width: displayW, height: displayH, display: 'block' }} />
    </button>
  );
}

/** Slider control for a single color parameter */
function ColorSlider({
  label,
  value,
  min,
  max,
  onChange,
}: {
  label: string;
  value: number;
  min: number;
  max: number;
  onChange: (v: number) => void;
}) {
  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
      <span
        style={{ fontSize: '20px', color: '#999', width: 28, textAlign: 'right', flexShrink: 0 }}
      >
        {label}
      </span>
      <input
        type="range"
        min={min}
        max={max}
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        style={{ flex: 1, height: 12, accentColor: 'rgba(90, 140, 255, 0.8)' }}
      />
      <span
        style={{ fontSize: '20px', color: '#999', width: 48, textAlign: 'right', flexShrink: 0 }}
      >
        {value}
      </span>
    </div>
  );
}

const DEFAULT_FURNITURE_COLOR: FloorColor = { h: 0, s: 0, b: 0, c: 0 };

export function EditorToolbar({
  activeTool,
  selectedTileType,
  selectedFurnitureType,
  selectedFurnitureUid,
  selectedFurnitureColor,
  floorColor,
  wallColor,
  selectedWallSet,
  onToolChange,
  onTileTypeChange,
  onFloorColorChange,
  onWallColorChange,
  onWallSetChange,
  onSelectedFurnitureColorChange,
  onFurnitureTypeChange,
  loadedAssets,
}: EditorToolbarProps) {
  const [activeCategory, setActiveCategory] = useState<FurnitureCategory>('desks');
  const [showColor, setShowColor] = useState(false);
  const [showWallColor, setShowWallColor] = useState(false);
  const [showFurnitureColor, setShowFurnitureColor] = useState(false);

  // Build dynamic catalog from loaded assets
  useEffect(() => {
    if (loadedAssets) {
      try {
        console.log(
          `[EditorToolbar] Building dynamic catalog with ${loadedAssets.catalog.length} assets...`,
        );
        const success = buildDynamicCatalog(loadedAssets);
        console.log(`[EditorToolbar] Catalog build result: ${success}`);

        // Reset to first available category if current doesn't exist
        const activeCategories = getActiveCategories();
        if (activeCategories.length > 0) {
          const firstCat = activeCategories[0]?.id;
          if (firstCat) {
            console.log(`[EditorToolbar] Setting active category to: ${firstCat}`);
            setActiveCategory(firstCat);
          }
        }
      } catch (err) {
        console.error(`[EditorToolbar] Error building dynamic catalog:`, err);
      }
    }
  }, [loadedAssets]);

  const handleColorChange = useCallback(
    (key: keyof FloorColor, value: number) => {
      onFloorColorChange({ ...floorColor, [key]: value });
    },
    [floorColor, onFloorColorChange],
  );

  const handleWallColorChange = useCallback(
    (key: keyof FloorColor, value: number) => {
      onWallColorChange({ ...wallColor, [key]: value });
    },
    [wallColor, onWallColorChange],
  );

  // For selected furniture: use existing color or default
  const effectiveColor = selectedFurnitureColor ?? DEFAULT_FURNITURE_COLOR;
  const handleSelFurnColorChange = useCallback(
    (key: keyof FloorColor, value: number) => {
      onSelectedFurnitureColorChange({ ...effectiveColor, [key]: value });
    },
    [effectiveColor, onSelectedFurnitureColorChange],
  );

  const categoryItems = getCatalogByCategory(activeCategory);

  const patternCount = getFloorPatternCount();
  // Wall is TileType 0, floor patterns are 1..patternCount
  const floorPatterns = Array.from({ length: patternCount }, (_, i) => i + 1);

  const thumbSize = 36; // 2x for items

  const isFloorActive = activeTool === EditTool.TILE_PAINT || activeTool === EditTool.EYEDROPPER;
  const isWallActive = activeTool === EditTool.WALL_PAINT;
  const isEraseActive = activeTool === EditTool.ERASE;
  const isFurnitureActive =
    activeTool === EditTool.FURNITURE_PLACE || activeTool === EditTool.FURNITURE_PICK;

  return (
    <div
      style={{
        position: 'absolute',
        bottom: 68,
        left: 10,
        zIndex: 50,
        background: '#1e1e2e',
        border: '2px solid #4a4a6a',
        borderRadius: 0,
        padding: '6px 8px',
        display: 'flex',
        flexDirection: 'column-reverse',
        gap: 6,
        boxShadow: '2px 2px 0px #0a0a14',
        maxWidth: 'calc(100vw - 20px)',
      }}
    >
      {/* Tool row — at the bottom */}
      <div style={{ display: 'flex', gap: 4, flexWrap: 'wrap' }}>
        <button
          style={isFloorActive ? activeBtnStyle : btnStyle}
          onClick={() => onToolChange(EditTool.TILE_PAINT)}
          title="Paint floor tiles"
        >
          Floor
        </button>
        <button
          style={isWallActive ? activeBtnStyle : btnStyle}
          onClick={() => onToolChange(EditTool.WALL_PAINT)}
          title="Paint walls (click to toggle)"
        >
          Wall
        </button>
        <button
          style={isEraseActive ? activeBtnStyle : btnStyle}
          onClick={() => onToolChange(EditTool.ERASE)}
          title="Erase tiles to void"
        >
          Erase
        </button>
        <button
          style={isFurnitureActive ? activeBtnStyle : btnStyle}
          onClick={() => onToolChange(EditTool.FURNITURE_PLACE)}
          title="Place furniture"
        >
          Furniture
        </button>
      </div>

      {/* Sub-panel: Floor tiles — stacked bottom-to-top via column-reverse */}
      {isFloorActive && (
        <div style={{ display: 'flex', flexDirection: 'column-reverse', gap: 6 }}>
          {/* Color toggle + Pick — just above tool row */}
          <div style={{ display: 'flex', gap: 4, alignItems: 'center' }}>
            <button
              style={showColor ? activeBtnStyle : btnStyle}
              onClick={() => setShowColor((v) => !v)}
              title="Adjust floor color"
            >
              Color
            </button>
            <button
              style={activeTool === EditTool.EYEDROPPER ? activeBtnStyle : btnStyle}
              onClick={() => onToolChange(EditTool.EYEDROPPER)}
              title="Pick floor pattern + color from existing tile"
            >
              Pick
            </button>
          </div>

          {/* Color controls (collapsible) — above Wall/Color/Pick */}
          {showColor && (
            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
                gap: 3,
                padding: '4px 6px',
                background: '#181828',
                border: '2px solid #4a4a6a',
                borderRadius: 0,
              }}
            >
              <ColorSlider
                label="H"
                value={floorColor.h}
                min={0}
                max={360}
                onChange={(v) => handleColorChange('h', v)}
              />
              <ColorSlider
                label="S"
                value={floorColor.s}
                min={0}
                max={100}
                onChange={(v) => handleColorChange('s', v)}
              />
              <ColorSlider
                label="B"
                value={floorColor.b}
                min={-100}
                max={100}
                onChange={(v) => handleColorChange('b', v)}
              />
              <ColorSlider
                label="C"
                value={floorColor.c}
                min={-100}
                max={100}
                onChange={(v) => handleColorChange('c', v)}
              />
            </div>
          )}

          {/* Floor pattern horizontal carousel — at the top */}
          <div
            style={{
              display: 'flex',
              gap: 4,
              overflowX: 'auto',
              flexWrap: 'nowrap',
              paddingBottom: 2,
            }}
          >
            {floorPatterns.map((patIdx) => (
              <FloorPatternPreview
                key={patIdx}
                patternIndex={patIdx}
                color={floorColor}
                selected={selectedTileType === patIdx}
                onClick={() => onTileTypeChange(patIdx as TileTypeVal)}
              />
            ))}
          </div>
        </div>
      )}

      {/* Sub-panel: Wall — stacked bottom-to-top via column-reverse */}
      {isWallActive && (
        <div style={{ display: 'flex', flexDirection: 'column-reverse', gap: 6 }}>
          {/* Color toggle — just above tool row */}
          <div style={{ display: 'flex', gap: 4, alignItems: 'center' }}>
            <button
              style={showWallColor ? activeBtnStyle : btnStyle}
              onClick={() => setShowWallColor((v) => !v)}
              title="Adjust wall color"
            >
              Color
            </button>
          </div>

          {/* Color controls (collapsible) */}
          {showWallColor && (
            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
                gap: 3,
                padding: '4px 6px',
                background: '#181828',
                border: '2px solid #4a4a6a',
                borderRadius: 0,
              }}
            >
              <ColorSlider
                label="H"
                value={wallColor.h}
                min={0}
                max={360}
                onChange={(v) => handleWallColorChange('h', v)}
              />
              <ColorSlider
                label="S"
                value={wallColor.s}
                min={0}
                max={100}
                onChange={(v) => handleWallColorChange('s', v)}
              />
              <ColorSlider
                label="B"
                value={wallColor.b}
                min={-100}
                max={100}
                onChange={(v) => handleWallColorChange('b', v)}
              />
              <ColorSlider
                label="C"
                value={wallColor.c}
                min={-100}
                max={100}
                onChange={(v) => handleWallColorChange('c', v)}
              />
            </div>
          )}

          {/* Wall set picker — horizontal carousel at the top */}
          {getWallSetCount() > 0 && (
            <div
              style={{
                display: 'flex',
                gap: 4,
                overflowX: 'auto',
                flexWrap: 'nowrap',
                paddingBottom: 2,
              }}
            >
              {Array.from({ length: getWallSetCount() }, (_, i) => (
                <WallSetPreview
                  key={i}
                  setIndex={i}
                  color={wallColor}
                  selected={selectedWallSet === i}
                  onClick={() => onWallSetChange(i)}
                />
              ))}
            </div>
          )}
        </div>
      )}

      {/* Sub-panel: Furniture — stacked bottom-to-top via column-reverse */}
      {isFurnitureActive && (
        <div style={{ display: 'flex', flexDirection: 'column-reverse', gap: 4 }}>
          {/* Category tabs + Pick — just above tool row */}
          <div style={{ display: 'flex', gap: 2, flexWrap: 'wrap', alignItems: 'center' }}>
            {getActiveCategories().map((cat) => (
              <button
                key={cat.id}
                style={activeCategory === cat.id ? activeTabStyle : tabStyle}
                onClick={() => setActiveCategory(cat.id)}
              >
                {cat.label}
              </button>
            ))}
            <div
              style={{
                width: 1,
                height: 14,
                background: 'rgba(255,255,255,0.15)',
                margin: '0 2px',
                flexShrink: 0,
              }}
            />
            <button
              style={activeTool === EditTool.FURNITURE_PICK ? activeBtnStyle : btnStyle}
              onClick={() => onToolChange(EditTool.FURNITURE_PICK)}
              title="Pick furniture type from placed item"
            >
              Pick
            </button>
          </div>
          {/* Furniture items — single-row horizontal carousel at 2x */}
          <div
            style={{
              display: 'flex',
              gap: 4,
              overflowX: 'auto',
              flexWrap: 'nowrap',
              paddingBottom: 2,
            }}
          >
            {categoryItems.map((entry) => {
              const cached = getCachedSprite(entry.sprite, 2);
              const isSelected = selectedFurnitureType === entry.type;
              return (
                <button
                  key={entry.type}
                  onClick={() => onFurnitureTypeChange(entry.type)}
                  title={entry.label}
                  style={{
                    width: thumbSize,
                    height: thumbSize,
                    background: '#2A2A3A',
                    border: isSelected ? '2px solid #5a8cff' : '2px solid #4a4a6a',
                    borderRadius: 0,
                    cursor: 'pointer',
                    padding: 0,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    overflow: 'hidden',
                    flexShrink: 0,
                  }}
                >
                  <canvas
                    ref={(el) => {
                      if (!el) return;
                      const ctx = el.getContext('2d');
                      if (!ctx) return;
                      const scale =
                        Math.min(thumbSize / cached.width, thumbSize / cached.height) * 0.85;
                      el.width = thumbSize;
                      el.height = thumbSize;
                      ctx.imageSmoothingEnabled = false;
                      ctx.clearRect(0, 0, thumbSize, thumbSize);
                      const dw = cached.width * scale;
                      const dh = cached.height * scale;
                      ctx.drawImage(cached, (thumbSize - dw) / 2, (thumbSize - dh) / 2, dw, dh);
                    }}
                    style={{ width: thumbSize, height: thumbSize }}
                  />
                </button>
              );
            })}
          </div>
        </div>
      )}

      {/* Selected furniture color panel — shows when any placed furniture item is selected */}
      {selectedFurnitureUid && (
        <div style={{ display: 'flex', flexDirection: 'column-reverse', gap: 3 }}>
          <div style={{ display: 'flex', gap: 4, alignItems: 'center' }}>
            <button
              style={showFurnitureColor ? activeBtnStyle : btnStyle}
              onClick={() => setShowFurnitureColor((v) => !v)}
              title="Adjust selected furniture color"
            >
              Color
            </button>
            {selectedFurnitureColor && (
              <button
                style={{ ...btnStyle, fontSize: '20px', padding: '2px 6px' }}
                onClick={() => onSelectedFurnitureColorChange(null)}
                title="Remove color (restore original)"
              >
                Clear
              </button>
            )}
          </div>
          {showFurnitureColor && (
            <div
              style={{
                display: 'flex',
                flexDirection: 'column',
                gap: 3,
                padding: '4px 6px',
                background: '#181828',
                border: '2px solid #4a4a6a',
                borderRadius: 0,
              }}
            >
              {effectiveColor.colorize ? (
                <>
                  <ColorSlider
                    label="H"
                    value={effectiveColor.h}
                    min={0}
                    max={360}
                    onChange={(v) => handleSelFurnColorChange('h', v)}
                  />
                  <ColorSlider
                    label="S"
                    value={effectiveColor.s}
                    min={0}
                    max={100}
                    onChange={(v) => handleSelFurnColorChange('s', v)}
                  />
                </>
              ) : (
                <>
                  <ColorSlider
                    label="H"
                    value={effectiveColor.h}
                    min={-180}
                    max={180}
                    onChange={(v) => handleSelFurnColorChange('h', v)}
                  />
                  <ColorSlider
                    label="S"
                    value={effectiveColor.s}
                    min={-100}
                    max={100}
                    onChange={(v) => handleSelFurnColorChange('s', v)}
                  />
                </>
              )}
              <ColorSlider
                label="B"
                value={effectiveColor.b}
                min={-100}
                max={100}
                onChange={(v) => handleSelFurnColorChange('b', v)}
              />
              <ColorSlider
                label="C"
                value={effectiveColor.c}
                min={-100}
                max={100}
                onChange={(v) => handleSelFurnColorChange('c', v)}
              />
              <label
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  gap: 4,
                  fontSize: '20px',
                  color: '#999',
                  cursor: 'pointer',
                }}
              >
                <input
                  type="checkbox"
                  checked={!!effectiveColor.colorize}
                  onChange={(e) =>
                    onSelectedFurnitureColorChange({
                      ...effectiveColor,
                      colorize: e.target.checked || undefined,
                    })
                  }
                  style={{ accentColor: 'rgba(90, 140, 255, 0.8)' }}
                />
                Colorize
              </label>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
```

## File: `webview-ui/src/office/editor/index.ts`
```typescript
export {
  canPlaceFurniture,
  moveFurniture,
  paintTile,
  placeFurniture,
  removeFurniture,
} from './editorActions.js';
export { EditorState } from './editorState.js';
export { EditorToolbar } from './EditorToolbar.js';
```

## File: `webview-ui/src/office/engine/characters.ts`
```typescript
import {
  SEAT_REST_MAX_SEC,
  SEAT_REST_MIN_SEC,
  TYPE_FRAME_DURATION_SEC,
  WALK_FRAME_DURATION_SEC,
  WALK_SPEED_PX_PER_SEC,
  WANDER_MOVES_BEFORE_REST_MAX,
  WANDER_MOVES_BEFORE_REST_MIN,
  WANDER_PAUSE_MAX_SEC,
  WANDER_PAUSE_MIN_SEC,
} from '../../constants.js';
import { findPath } from '../layout/tileMap.js';
import type { CharacterSprites } from '../sprites/spriteData.js';
import type { Character, Seat, SpriteData, TileType as TileTypeVal } from '../types.js';
import { CharacterState, Direction, TILE_SIZE } from '../types.js';

/** Tools that show reading animation instead of typing */
const READING_TOOLS = new Set(['Read', 'Grep', 'Glob', 'WebFetch', 'WebSearch']);

export function isReadingTool(tool: string | null): boolean {
  if (!tool) return false;
  return READING_TOOLS.has(tool);
}

/** Pixel center of a tile */
function tileCenter(col: number, row: number): { x: number; y: number } {
  return {
    x: col * TILE_SIZE + TILE_SIZE / 2,
    y: row * TILE_SIZE + TILE_SIZE / 2,
  };
}

/** Direction from one tile to an adjacent tile */
function directionBetween(
  fromCol: number,
  fromRow: number,
  toCol: number,
  toRow: number,
): Direction {
  const dc = toCol - fromCol;
  const dr = toRow - fromRow;
  if (dc > 0) return Direction.RIGHT;
  if (dc < 0) return Direction.LEFT;
  if (dr > 0) return Direction.DOWN;
  return Direction.UP;
}

export function createCharacter(
  id: number,
  palette: number,
  seatId: string | null,
  seat: Seat | null,
  hueShift = 0,
): Character {
  const col = seat ? seat.seatCol : 1;
  const row = seat ? seat.seatRow : 1;
  const center = tileCenter(col, row);
  return {
    id,
    state: CharacterState.TYPE,
    dir: seat ? seat.facingDir : Direction.DOWN,
    x: center.x,
    y: center.y,
    tileCol: col,
    tileRow: row,
    path: [],
    moveProgress: 0,
    currentTool: null,
    palette,
    hueShift,
    frame: 0,
    frameTimer: 0,
    wanderTimer: 0,
    wanderCount: 0,
    wanderLimit: randomInt(WANDER_MOVES_BEFORE_REST_MIN, WANDER_MOVES_BEFORE_REST_MAX),
    isActive: true,
    seatId,
    bubbleType: null,
    bubbleTimer: 0,
    seatTimer: 0,
    isSubagent: false,
    parentAgentId: null,
    matrixEffect: null,
    matrixEffectTimer: 0,
    matrixEffectSeeds: [],
  };
}

export function updateCharacter(
  ch: Character,
  dt: number,
  walkableTiles: Array<{ col: number; row: number }>,
  seats: Map<string, Seat>,
  tileMap: TileTypeVal[][],
  blockedTiles: Set<string>,
): void {
  ch.frameTimer += dt;

  switch (ch.state) {
    case CharacterState.TYPE: {
      if (ch.frameTimer >= TYPE_FRAME_DURATION_SEC) {
        ch.frameTimer -= TYPE_FRAME_DURATION_SEC;
        ch.frame = (ch.frame + 1) % 2;
      }
      // If no longer active, stand up and start wandering (after seatTimer expires)
      if (!ch.isActive) {
        if (ch.seatTimer > 0) {
          ch.seatTimer -= dt;
          break;
        }
        ch.seatTimer = 0; // clear sentinel
        ch.state = CharacterState.IDLE;
        ch.frame = 0;
        ch.frameTimer = 0;
        ch.wanderTimer = randomRange(WANDER_PAUSE_MIN_SEC, WANDER_PAUSE_MAX_SEC);
        ch.wanderCount = 0;
        ch.wanderLimit = randomInt(WANDER_MOVES_BEFORE_REST_MIN, WANDER_MOVES_BEFORE_REST_MAX);
      }
      break;
    }

    case CharacterState.IDLE: {
      // No idle animation — static pose
      ch.frame = 0;
      if (ch.seatTimer < 0) ch.seatTimer = 0; // clear turn-end sentinel
      // If became active, pathfind to seat
      if (ch.isActive) {
        if (!ch.seatId) {
          // No seat assigned — type in place
          ch.state = CharacterState.TYPE;
          ch.frame = 0;
          ch.frameTimer = 0;
          break;
        }
        const seat = seats.get(ch.seatId);
        if (seat) {
          const path = findPath(
            ch.tileCol,
            ch.tileRow,
            seat.seatCol,
            seat.seatRow,
            tileMap,
            blockedTiles,
          );
          if (path.length > 0) {
            ch.path = path;
            ch.moveProgress = 0;
            ch.state = CharacterState.WALK;
            ch.frame = 0;
            ch.frameTimer = 0;
          } else {
            // Already at seat or no path — sit down
            ch.state = CharacterState.TYPE;
            ch.dir = seat.facingDir;
            ch.frame = 0;
            ch.frameTimer = 0;
          }
        }
        break;
      }
      // Countdown wander timer
      ch.wanderTimer -= dt;
      if (ch.wanderTimer <= 0) {
        // Check if we've wandered enough — return to seat for a rest
        if (ch.wanderCount >= ch.wanderLimit && ch.seatId) {
          const seat = seats.get(ch.seatId);
          if (seat) {
            const path = findPath(
              ch.tileCol,
              ch.tileRow,
              seat.seatCol,
              seat.seatRow,
              tileMap,
              blockedTiles,
            );
            if (path.length > 0) {
              ch.path = path;
              ch.moveProgress = 0;
              ch.state = CharacterState.WALK;
              ch.frame = 0;
              ch.frameTimer = 0;
              break;
            }
          }
        }
        if (walkableTiles.length > 0) {
          const target = walkableTiles[Math.floor(Math.random() * walkableTiles.length)];
          const path = findPath(
            ch.tileCol,
            ch.tileRow,
            target.col,
            target.row,
            tileMap,
            blockedTiles,
          );
          if (path.length > 0) {
            ch.path = path;
            ch.moveProgress = 0;
            ch.state = CharacterState.WALK;
            ch.frame = 0;
            ch.frameTimer = 0;
            ch.wanderCount++;
          }
        }
        ch.wanderTimer = randomRange(WANDER_PAUSE_MIN_SEC, WANDER_PAUSE_MAX_SEC);
      }
      break;
    }

    case CharacterState.WALK: {
      // Walk animation
      if (ch.frameTimer >= WALK_FRAME_DURATION_SEC) {
        ch.frameTimer -= WALK_FRAME_DURATION_SEC;
        ch.frame = (ch.frame + 1) % 4;
      }

      if (ch.path.length === 0) {
        // Path complete — snap to tile center and transition
        const center = tileCenter(ch.tileCol, ch.tileRow);
        ch.x = center.x;
        ch.y = center.y;

        if (ch.isActive) {
          if (!ch.seatId) {
            // No seat — type in place
            ch.state = CharacterState.TYPE;
          } else {
            const seat = seats.get(ch.seatId);
            if (seat && ch.tileCol === seat.seatCol && ch.tileRow === seat.seatRow) {
              ch.state = CharacterState.TYPE;
              ch.dir = seat.facingDir;
            } else {
              ch.state = CharacterState.IDLE;
            }
          }
        } else {
          // Check if arrived at assigned seat — sit down for a rest before wandering again
          if (ch.seatId) {
            const seat = seats.get(ch.seatId);
            if (seat && ch.tileCol === seat.seatCol && ch.tileRow === seat.seatRow) {
              ch.state = CharacterState.TYPE;
              ch.dir = seat.facingDir;
              // seatTimer < 0 is a sentinel from setAgentActive(false) meaning
              // "turn just ended" — skip the long rest so idle transition is immediate
              if (ch.seatTimer < 0) {
                ch.seatTimer = 0;
              } else {
                ch.seatTimer = randomRange(SEAT_REST_MIN_SEC, SEAT_REST_MAX_SEC);
              }
              ch.wanderCount = 0;
              ch.wanderLimit = randomInt(
                WANDER_MOVES_BEFORE_REST_MIN,
                WANDER_MOVES_BEFORE_REST_MAX,
              );
              ch.frame = 0;
              ch.frameTimer = 0;
              break;
            }
          }
          ch.state = CharacterState.IDLE;
          ch.wanderTimer = randomRange(WANDER_PAUSE_MIN_SEC, WANDER_PAUSE_MAX_SEC);
        }
        ch.frame = 0;
        ch.frameTimer = 0;
        break;
      }

      // Move toward next tile in path
      const nextTile = ch.path[0];
      ch.dir = directionBetween(ch.tileCol, ch.tileRow, nextTile.col, nextTile.row);

      ch.moveProgress += (WALK_SPEED_PX_PER_SEC / TILE_SIZE) * dt;

      const fromCenter = tileCenter(ch.tileCol, ch.tileRow);
      const toCenter = tileCenter(nextTile.col, nextTile.row);
      const t = Math.min(ch.moveProgress, 1);
      ch.x = fromCenter.x + (toCenter.x - fromCenter.x) * t;
      ch.y = fromCenter.y + (toCenter.y - fromCenter.y) * t;

      if (ch.moveProgress >= 1) {
        // Arrived at next tile
        ch.tileCol = nextTile.col;
        ch.tileRow = nextTile.row;
        ch.x = toCenter.x;
        ch.y = toCenter.y;
        ch.path.shift();
        ch.moveProgress = 0;
      }

      // If became active while wandering, repath to seat
      if (ch.isActive && ch.seatId) {
        const seat = seats.get(ch.seatId);
        if (seat) {
          const lastStep = ch.path[ch.path.length - 1];
          if (!lastStep || lastStep.col !== seat.seatCol || lastStep.row !== seat.seatRow) {
            const newPath = findPath(
              ch.tileCol,
              ch.tileRow,
              seat.seatCol,
              seat.seatRow,
              tileMap,
              blockedTiles,
            );
            if (newPath.length > 0) {
              ch.path = newPath;
              ch.moveProgress = 0;
            }
          }
        }
      }
      break;
    }
  }
}

/** Get the correct sprite frame for a character's current state and direction */
export function getCharacterSprite(ch: Character, sprites: CharacterSprites): SpriteData {
  switch (ch.state) {
    case CharacterState.TYPE:
      if (isReadingTool(ch.currentTool)) {
        return sprites.reading[ch.dir][ch.frame % 2];
      }
      return sprites.typing[ch.dir][ch.frame % 2];
    case CharacterState.WALK:
      return sprites.walk[ch.dir][ch.frame % 4];
    case CharacterState.IDLE:
      return sprites.walk[ch.dir][1];
    default:
      return sprites.walk[ch.dir][1];
  }
}

function randomRange(min: number, max: number): number {
  return min + Math.random() * (max - min);
}

function randomInt(min: number, max: number): number {
  return min + Math.floor(Math.random() * (max - min + 1));
}
```

## File: `webview-ui/src/office/engine/gameLoop.ts`
```typescript
import { MAX_DELTA_TIME_SEC } from '../../constants.js';

export interface GameLoopCallbacks {
  update: (dt: number) => void;
  render: (ctx: CanvasRenderingContext2D) => void;
}

export function startGameLoop(canvas: HTMLCanvasElement, callbacks: GameLoopCallbacks): () => void {
  const ctx = canvas.getContext('2d')!;
  ctx.imageSmoothingEnabled = false;

  let lastTime = 0;
  let rafId = 0;
  let stopped = false;

  const frame = (time: number) => {
    if (stopped) return;
    const dt = lastTime === 0 ? 0 : Math.min((time - lastTime) / 1000, MAX_DELTA_TIME_SEC);
    lastTime = time;

    callbacks.update(dt);

    ctx.imageSmoothingEnabled = false;
    callbacks.render(ctx);

    rafId = requestAnimationFrame(frame);
  };

  rafId = requestAnimationFrame(frame);

  return () => {
    stopped = true;
    cancelAnimationFrame(rafId);
  };
}
```

## File: `webview-ui/src/office/engine/index.ts`
```typescript
export {
  createCharacter,
  getCharacterSprite,
  isReadingTool,
  updateCharacter,
} from './characters.js';
export type { GameLoopCallbacks } from './gameLoop.js';
export { startGameLoop } from './gameLoop.js';
export { OfficeState } from './officeState.js';
export type { DeleteButtonBounds, EditorRenderState, SelectionRenderState } from './renderer.js';
export {
  renderDeleteButton,
  renderFrame,
  renderGhostPreview,
  renderGridOverlay,
  renderScene,
  renderSelectionHighlight,
  renderTileGrid,
} from './renderer.js';
```

## File: `webview-ui/src/office/engine/matrixEffect.ts`
```typescript
import {
  MATRIX_COLUMN_STAGGER_RANGE,
  MATRIX_FLICKER_FPS,
  MATRIX_FLICKER_VISIBILITY_THRESHOLD,
  MATRIX_HEAD_COLOR,
  MATRIX_SPRITE_COLS,
  MATRIX_SPRITE_ROWS,
  MATRIX_TRAIL_DIM_THRESHOLD,
  MATRIX_TRAIL_EMPTY_ALPHA,
  MATRIX_TRAIL_LENGTH,
  MATRIX_TRAIL_MID_THRESHOLD,
  MATRIX_TRAIL_OVERLAY_ALPHA,
} from '../../constants.js';
import type { Character, SpriteData } from '../types.js';
import { MATRIX_EFFECT_DURATION } from '../types.js';

/** Hash-based flicker: ~70% visible for shimmer effect */
function flickerVisible(col: number, row: number, time: number): boolean {
  const t = Math.floor(time * MATRIX_FLICKER_FPS);
  const hash = (col * 7 + row * 13 + t * 31) & 0xff;
  return hash < MATRIX_FLICKER_VISIBILITY_THRESHOLD;
}

function generateSeeds(): number[] {
  const seeds: number[] = [];
  for (let i = 0; i < MATRIX_SPRITE_COLS; i++) {
    seeds.push(Math.random());
  }
  return seeds;
}

export { generateSeeds as matrixEffectSeeds };

/**
 * Render a character with a Matrix-style digital rain spawn/despawn effect.
 * Per-pixel rendering: each column sweeps top-to-bottom with a bright head and fading green trail.
 */
export function renderMatrixEffect(
  ctx: CanvasRenderingContext2D,
  ch: Character,
  spriteData: SpriteData,
  drawX: number,
  drawY: number,
  zoom: number,
): void {
  const progress = ch.matrixEffectTimer / MATRIX_EFFECT_DURATION;
  const isSpawn = ch.matrixEffect === 'spawn';
  const time = ch.matrixEffectTimer;
  const totalSweep = MATRIX_SPRITE_ROWS + MATRIX_TRAIL_LENGTH;

  for (let col = 0; col < MATRIX_SPRITE_COLS; col++) {
    // Stagger: each column starts at a slightly different time
    const stagger = (ch.matrixEffectSeeds[col] ?? 0) * MATRIX_COLUMN_STAGGER_RANGE;
    const colProgress = Math.max(
      0,
      Math.min(1, (progress - stagger) / (1 - MATRIX_COLUMN_STAGGER_RANGE)),
    );
    const headRow = colProgress * totalSweep;

    for (let row = 0; row < MATRIX_SPRITE_ROWS; row++) {
      const pixel = spriteData[row]?.[col];
      const hasPixel = pixel && pixel !== '';
      const distFromHead = headRow - row;
      const px = drawX + col * zoom;
      const py = drawY + row * zoom;

      if (isSpawn) {
        // Spawn: head sweeps down revealing character pixels
        if (distFromHead < 0) {
          // Above head: invisible
          continue;
        } else if (distFromHead < 1) {
          // Head pixel: bright white-green
          ctx.fillStyle = MATRIX_HEAD_COLOR;
          ctx.fillRect(px, py, zoom, zoom);
        } else if (distFromHead < MATRIX_TRAIL_LENGTH) {
          // Trail zone: show character pixel with green overlay, or just green if no pixel
          const trailPos = distFromHead / MATRIX_TRAIL_LENGTH;
          if (hasPixel) {
            // Draw original pixel
            ctx.fillStyle = pixel;
            ctx.fillRect(px, py, zoom, zoom);
            // Green overlay that fades as trail progresses
            const greenAlpha = (1 - trailPos) * MATRIX_TRAIL_OVERLAY_ALPHA;
            if (flickerVisible(col, row, time)) {
              ctx.fillStyle = `rgba(0, 255, 65, ${greenAlpha})`;
              ctx.fillRect(px, py, zoom, zoom);
            }
          } else {
            // No character pixel: fading green trail
            if (flickerVisible(col, row, time)) {
              const alpha = (1 - trailPos) * MATRIX_TRAIL_EMPTY_ALPHA;
              ctx.fillStyle =
                trailPos < MATRIX_TRAIL_MID_THRESHOLD
                  ? `rgba(0, 255, 65, ${alpha})`
                  : trailPos < MATRIX_TRAIL_DIM_THRESHOLD
                    ? `rgba(0, 170, 40, ${alpha})`
                    : `rgba(0, 85, 20, ${alpha})`;
              ctx.fillRect(px, py, zoom, zoom);
            }
          }
        } else {
          // Below trail: normal character pixel
          if (hasPixel) {
            ctx.fillStyle = pixel;
            ctx.fillRect(px, py, zoom, zoom);
          }
        }
      } else {
        // Despawn: head sweeps down consuming character pixels
        if (distFromHead < 0) {
          // Above head: normal character pixel (not yet consumed)
          if (hasPixel) {
            ctx.fillStyle = pixel;
            ctx.fillRect(px, py, zoom, zoom);
          }
        } else if (distFromHead < 1) {
          // Head pixel: bright white-green
          ctx.fillStyle = MATRIX_HEAD_COLOR;
          ctx.fillRect(px, py, zoom, zoom);
        } else if (distFromHead < MATRIX_TRAIL_LENGTH) {
          // Trail zone: fading green
          if (flickerVisible(col, row, time)) {
            const trailPos = distFromHead / MATRIX_TRAIL_LENGTH;
            const alpha = (1 - trailPos) * MATRIX_TRAIL_EMPTY_ALPHA;
            ctx.fillStyle =
              trailPos < MATRIX_TRAIL_MID_THRESHOLD
                ? `rgba(0, 255, 65, ${alpha})`
                : trailPos < MATRIX_TRAIL_DIM_THRESHOLD
                  ? `rgba(0, 170, 40, ${alpha})`
                  : `rgba(0, 85, 20, ${alpha})`;
            ctx.fillRect(px, py, zoom, zoom);
          }
        }
        // Below trail: nothing (consumed)
      }
    }
  }
}
```

## File: `webview-ui/src/office/engine/officeState.ts`
```typescript
import {
  AUTO_ON_FACING_DEPTH,
  AUTO_ON_SIDE_DEPTH,
  CHARACTER_HIT_HALF_WIDTH,
  CHARACTER_HIT_HEIGHT,
  CHARACTER_SITTING_OFFSET_PX,
  DISMISS_BUBBLE_FAST_FADE_SEC,
  FURNITURE_ANIM_INTERVAL_SEC,
  HUE_SHIFT_MIN_DEG,
  HUE_SHIFT_RANGE_DEG,
  INACTIVE_SEAT_TIMER_MIN_SEC,
  INACTIVE_SEAT_TIMER_RANGE_SEC,
  PALETTE_COUNT,
  WAITING_BUBBLE_DURATION_SEC,
} from '../../constants.js';
import { getAnimationFrames, getCatalogEntry, getOnStateType } from '../layout/furnitureCatalog.js';
import {
  createDefaultLayout,
  getBlockedTiles,
  layoutToFurnitureInstances,
  layoutToSeats,
  layoutToTileMap,
} from '../layout/layoutSerializer.js';
import { findPath, getWalkableTiles, isWalkable } from '../layout/tileMap.js';
import type {
  Character,
  FurnitureInstance,
  OfficeLayout,
  PlacedFurniture,
  Seat,
  TileType as TileTypeVal,
} from '../types.js';
import { CharacterState, Direction, MATRIX_EFFECT_DURATION, TILE_SIZE } from '../types.js';
import { createCharacter, updateCharacter } from './characters.js';
import { matrixEffectSeeds } from './matrixEffect.js';

export class OfficeState {
  layout: OfficeLayout;
  tileMap: TileTypeVal[][];
  seats: Map<string, Seat>;
  blockedTiles: Set<string>;
  furniture: FurnitureInstance[];
  walkableTiles: Array<{ col: number; row: number }>;
  characters: Map<number, Character> = new Map();
  /** Accumulated time for furniture animation frame cycling */
  furnitureAnimTimer = 0;
  selectedAgentId: number | null = null;
  cameraFollowId: number | null = null;
  hoveredAgentId: number | null = null;
  hoveredTile: { col: number; row: number } | null = null;
  /** Maps "parentId:toolId" → sub-agent character ID (negative) */
  subagentIdMap: Map<string, number> = new Map();
  /** Reverse lookup: sub-agent character ID → parent info */
  subagentMeta: Map<number, { parentAgentId: number; parentToolId: string }> = new Map();
  private nextSubagentId = -1;

  constructor(layout?: OfficeLayout) {
    this.layout = layout || createDefaultLayout();
    this.tileMap = layoutToTileMap(this.layout);
    this.seats = layoutToSeats(this.layout.furniture);
    this.blockedTiles = getBlockedTiles(this.layout.furniture);
    this.furniture = layoutToFurnitureInstances(this.layout.furniture);
    this.walkableTiles = getWalkableTiles(this.tileMap, this.blockedTiles);
  }

  /** Rebuild all derived state from a new layout. Reassigns existing characters.
   *  @param shift Optional pixel shift to apply when grid expands left/up */
  rebuildFromLayout(layout: OfficeLayout, shift?: { col: number; row: number }): void {
    this.layout = layout;
    this.tileMap = layoutToTileMap(layout);
    this.seats = layoutToSeats(layout.furniture);
    this.blockedTiles = getBlockedTiles(layout.furniture);
    this.rebuildFurnitureInstances();
    this.walkableTiles = getWalkableTiles(this.tileMap, this.blockedTiles);

    // Shift character positions when grid expands left/up
    if (shift && (shift.col !== 0 || shift.row !== 0)) {
      for (const ch of this.characters.values()) {
        ch.tileCol += shift.col;
        ch.tileRow += shift.row;
        ch.x += shift.col * TILE_SIZE;
        ch.y += shift.row * TILE_SIZE;
        // Clear path since tile coords changed
        ch.path = [];
        ch.moveProgress = 0;
      }
    }

    // Reassign characters to new seats, preserving existing assignments when possible
    for (const seat of this.seats.values()) {
      seat.assigned = false;
    }

    // First pass: try to keep characters at their existing seats
    for (const ch of this.characters.values()) {
      if (ch.seatId && this.seats.has(ch.seatId)) {
        const seat = this.seats.get(ch.seatId)!;
        if (!seat.assigned) {
          seat.assigned = true;
          // Snap character to seat position
          ch.tileCol = seat.seatCol;
          ch.tileRow = seat.seatRow;
          const cx = seat.seatCol * TILE_SIZE + TILE_SIZE / 2;
          const cy = seat.seatRow * TILE_SIZE + TILE_SIZE / 2;
          ch.x = cx;
          ch.y = cy;
          ch.dir = seat.facingDir;
          continue;
        }
      }
      ch.seatId = null; // will be reassigned below
    }

    // Second pass: assign remaining characters to free seats
    for (const ch of this.characters.values()) {
      if (ch.seatId) continue;
      const seatId = this.findFreeSeat();
      if (seatId) {
        this.seats.get(seatId)!.assigned = true;
        ch.seatId = seatId;
        const seat = this.seats.get(seatId)!;
        ch.tileCol = seat.seatCol;
        ch.tileRow = seat.seatRow;
        ch.x = seat.seatCol * TILE_SIZE + TILE_SIZE / 2;
        ch.y = seat.seatRow * TILE_SIZE + TILE_SIZE / 2;
        ch.dir = seat.facingDir;
      }
    }

    // Relocate any characters that ended up outside bounds or on non-walkable tiles
    for (const ch of this.characters.values()) {
      if (ch.seatId) continue; // seated characters are fine
      if (
        ch.tileCol < 0 ||
        ch.tileCol >= layout.cols ||
        ch.tileRow < 0 ||
        ch.tileRow >= layout.rows
      ) {
        this.relocateCharacterToWalkable(ch);
      }
    }
  }

  /** Move a character to a random walkable tile */
  private relocateCharacterToWalkable(ch: Character): void {
    if (this.walkableTiles.length === 0) return;
    const spawn = this.walkableTiles[Math.floor(Math.random() * this.walkableTiles.length)];
    ch.tileCol = spawn.col;
    ch.tileRow = spawn.row;
    ch.x = spawn.col * TILE_SIZE + TILE_SIZE / 2;
    ch.y = spawn.row * TILE_SIZE + TILE_SIZE / 2;
    ch.path = [];
    ch.moveProgress = 0;
  }

  getLayout(): OfficeLayout {
    return this.layout;
  }

  /** Get the blocked-tile key for a character's own seat, or null */
  private ownSeatKey(ch: Character): string | null {
    if (!ch.seatId) return null;
    const seat = this.seats.get(ch.seatId);
    if (!seat) return null;
    return `${seat.seatCol},${seat.seatRow}`;
  }

  /** Temporarily unblock a character's own seat, run fn, then re-block */
  private withOwnSeatUnblocked<T>(ch: Character, fn: () => T): T {
    const key = this.ownSeatKey(ch);
    if (key) this.blockedTiles.delete(key);
    const result = fn();
    if (key) this.blockedTiles.add(key);
    return result;
  }

  private findFreeSeat(): string | null {
    for (const [uid, seat] of this.seats) {
      if (!seat.assigned) return uid;
    }
    return null;
  }

  /**
   * Pick a diverse palette for a new agent based on currently active agents.
   * First 6 agents each get a unique skin (random order). Beyond 6, skins
   * repeat in balanced rounds with a random hue shift (≥45°).
   */
  private pickDiversePalette(): { palette: number; hueShift: number } {
    // Count how many non-sub-agents use each base palette (0-5)
    const counts = new Array(PALETTE_COUNT).fill(0) as number[];
    for (const ch of this.characters.values()) {
      if (ch.isSubagent) continue;
      counts[ch.palette]++;
    }
    const minCount = Math.min(...counts);
    // Available = palettes at the minimum count (least used)
    const available: number[] = [];
    for (let i = 0; i < PALETTE_COUNT; i++) {
      if (counts[i] === minCount) available.push(i);
    }
    const palette = available[Math.floor(Math.random() * available.length)];
    // First round (minCount === 0): no hue shift. Subsequent rounds: random ≥45°.
    let hueShift = 0;
    if (minCount > 0) {
      hueShift = HUE_SHIFT_MIN_DEG + Math.floor(Math.random() * HUE_SHIFT_RANGE_DEG);
    }
    return { palette, hueShift };
  }

  addAgent(
    id: number,
    preferredPalette?: number,
    preferredHueShift?: number,
    preferredSeatId?: string,
    skipSpawnEffect?: boolean,
    folderName?: string,
  ): void {
    if (this.characters.has(id)) return;

    let palette: number;
    let hueShift: number;
    if (preferredPalette !== undefined) {
      palette = preferredPalette;
      hueShift = preferredHueShift ?? 0;
    } else {
      const pick = this.pickDiversePalette();
      palette = pick.palette;
      hueShift = pick.hueShift;
    }

    // Try preferred seat first, then any free seat
    let seatId: string | null = null;
    if (preferredSeatId && this.seats.has(preferredSeatId)) {
      const seat = this.seats.get(preferredSeatId)!;
      if (!seat.assigned) {
        seatId = preferredSeatId;
      }
    }
    if (!seatId) {
      seatId = this.findFreeSeat();
    }

    let ch: Character;
    if (seatId) {
      const seat = this.seats.get(seatId)!;
      seat.assigned = true;
      ch = createCharacter(id, palette, seatId, seat, hueShift);
    } else {
      // No seats — spawn at random walkable tile
      const spawn =
        this.walkableTiles.length > 0
          ? this.walkableTiles[Math.floor(Math.random() * this.walkableTiles.length)]
          : { col: 1, row: 1 };
      ch = createCharacter(id, palette, null, null, hueShift);
      ch.x = spawn.col * TILE_SIZE + TILE_SIZE / 2;
      ch.y = spawn.row * TILE_SIZE + TILE_SIZE / 2;
      ch.tileCol = spawn.col;
      ch.tileRow = spawn.row;
    }

    if (folderName) {
      ch.folderName = folderName;
    }
    if (!skipSpawnEffect) {
      ch.matrixEffect = 'spawn';
      ch.matrixEffectTimer = 0;
      ch.matrixEffectSeeds = matrixEffectSeeds();
    }
    this.characters.set(id, ch);
  }

  removeAgent(id: number): void {
    const ch = this.characters.get(id);
    if (!ch) return;
    if (ch.matrixEffect === 'despawn') return; // already despawning
    // Free seat and clear selection immediately
    if (ch.seatId) {
      const seat = this.seats.get(ch.seatId);
      if (seat) seat.assigned = false;
    }
    if (this.selectedAgentId === id) this.selectedAgentId = null;
    if (this.cameraFollowId === id) this.cameraFollowId = null;
    // Start despawn animation instead of immediate delete
    ch.matrixEffect = 'despawn';
    ch.matrixEffectTimer = 0;
    ch.matrixEffectSeeds = matrixEffectSeeds();
    ch.bubbleType = null;
  }

  /** Find seat uid at a given tile position, or null */
  getSeatAtTile(col: number, row: number): string | null {
    for (const [uid, seat] of this.seats) {
      if (seat.seatCol === col && seat.seatRow === row) return uid;
    }
    return null;
  }

  /** Reassign an agent from their current seat to a new seat */
  reassignSeat(agentId: number, seatId: string): void {
    const ch = this.characters.get(agentId);
    if (!ch) return;
    // Unassign old seat
    if (ch.seatId) {
      const old = this.seats.get(ch.seatId);
      if (old) old.assigned = false;
    }
    // Assign new seat
    const seat = this.seats.get(seatId);
    if (!seat || seat.assigned) return;
    seat.assigned = true;
    ch.seatId = seatId;
    // Pathfind to new seat (unblock own seat tile for this query)
    const path = this.withOwnSeatUnblocked(ch, () =>
      findPath(ch.tileCol, ch.tileRow, seat.seatCol, seat.seatRow, this.tileMap, this.blockedTiles),
    );
    if (path.length > 0) {
      ch.path = path;
      ch.moveProgress = 0;
      ch.state = CharacterState.WALK;
      ch.frame = 0;
      ch.frameTimer = 0;
    } else {
      // Already at seat or no path — sit down
      ch.state = CharacterState.TYPE;
      ch.dir = seat.facingDir;
      ch.frame = 0;
      ch.frameTimer = 0;
      if (!ch.isActive) {
        ch.seatTimer = INACTIVE_SEAT_TIMER_MIN_SEC + Math.random() * INACTIVE_SEAT_TIMER_RANGE_SEC;
      }
    }
  }

  /** Send an agent back to their currently assigned seat */
  sendToSeat(agentId: number): void {
    const ch = this.characters.get(agentId);
    if (!ch || !ch.seatId) return;
    const seat = this.seats.get(ch.seatId);
    if (!seat) return;
    const path = this.withOwnSeatUnblocked(ch, () =>
      findPath(ch.tileCol, ch.tileRow, seat.seatCol, seat.seatRow, this.tileMap, this.blockedTiles),
    );
    if (path.length > 0) {
      ch.path = path;
      ch.moveProgress = 0;
      ch.state = CharacterState.WALK;
      ch.frame = 0;
      ch.frameTimer = 0;
    } else {
      // Already at seat — sit down
      ch.state = CharacterState.TYPE;
      ch.dir = seat.facingDir;
      ch.frame = 0;
      ch.frameTimer = 0;
      if (!ch.isActive) {
        ch.seatTimer = INACTIVE_SEAT_TIMER_MIN_SEC + Math.random() * INACTIVE_SEAT_TIMER_RANGE_SEC;
      }
    }
  }

  /** Walk an agent to an arbitrary walkable tile (right-click command) */
  walkToTile(agentId: number, col: number, row: number): boolean {
    const ch = this.characters.get(agentId);
    if (!ch || ch.isSubagent) return false;
    if (!isWalkable(col, row, this.tileMap, this.blockedTiles)) {
      // Also allow walking to own seat tile (blocked for others but not self)
      const key = this.ownSeatKey(ch);
      if (!key || key !== `${col},${row}`) return false;
    }
    const path = this.withOwnSeatUnblocked(ch, () =>
      findPath(ch.tileCol, ch.tileRow, col, row, this.tileMap, this.blockedTiles),
    );
    if (path.length === 0) return false;
    ch.path = path;
    ch.moveProgress = 0;
    ch.state = CharacterState.WALK;
    ch.frame = 0;
    ch.frameTimer = 0;
    return true;
  }

  /** Create a sub-agent character with the parent's palette. Returns the sub-agent ID. */
  addSubagent(parentAgentId: number, parentToolId: string): number {
    const key = `${parentAgentId}:${parentToolId}`;
    if (this.subagentIdMap.has(key)) return this.subagentIdMap.get(key)!;

    const id = this.nextSubagentId--;
    const parentCh = this.characters.get(parentAgentId);
    const palette = parentCh ? parentCh.palette : 0;
    const hueShift = parentCh ? parentCh.hueShift : 0;

    // Find the free seat closest to the parent agent
    const parentCol = parentCh ? parentCh.tileCol : 0;
    const parentRow = parentCh ? parentCh.tileRow : 0;
    const dist = (c: number, r: number) => Math.abs(c - parentCol) + Math.abs(r - parentRow);

    let bestSeatId: string | null = null;
    let bestDist = Infinity;
    for (const [uid, seat] of this.seats) {
      if (!seat.assigned) {
        const d = dist(seat.seatCol, seat.seatRow);
        if (d < bestDist) {
          bestDist = d;
          bestSeatId = uid;
        }
      }
    }

    let ch: Character;
    if (bestSeatId) {
      const seat = this.seats.get(bestSeatId)!;
      seat.assigned = true;
      ch = createCharacter(id, palette, bestSeatId, seat, hueShift);
    } else {
      // No seats — spawn at closest walkable tile to parent
      let spawn = { col: 1, row: 1 };
      if (this.walkableTiles.length > 0) {
        let closest = this.walkableTiles[0];
        let closestDist = dist(closest.col, closest.row);
        for (let i = 1; i < this.walkableTiles.length; i++) {
          const d = dist(this.walkableTiles[i].col, this.walkableTiles[i].row);
          if (d < closestDist) {
            closest = this.walkableTiles[i];
            closestDist = d;
          }
        }
        spawn = closest;
      }
      ch = createCharacter(id, palette, null, null, hueShift);
      ch.x = spawn.col * TILE_SIZE + TILE_SIZE / 2;
      ch.y = spawn.row * TILE_SIZE + TILE_SIZE / 2;
      ch.tileCol = spawn.col;
      ch.tileRow = spawn.row;
    }
    ch.isSubagent = true;
    ch.parentAgentId = parentAgentId;
    ch.matrixEffect = 'spawn';
    ch.matrixEffectTimer = 0;
    ch.matrixEffectSeeds = matrixEffectSeeds();
    this.characters.set(id, ch);

    this.subagentIdMap.set(key, id);
    this.subagentMeta.set(id, { parentAgentId, parentToolId });
    return id;
  }

  /** Remove a specific sub-agent character and free its seat */
  removeSubagent(parentAgentId: number, parentToolId: string): void {
    const key = `${parentAgentId}:${parentToolId}`;
    const id = this.subagentIdMap.get(key);
    if (id === undefined) return;

    const ch = this.characters.get(id);
    if (ch) {
      if (ch.matrixEffect === 'despawn') {
        // Already despawning — just clean up maps
        this.subagentIdMap.delete(key);
        this.subagentMeta.delete(id);
        return;
      }
      if (ch.seatId) {
        const seat = this.seats.get(ch.seatId);
        if (seat) seat.assigned = false;
      }
      // Start despawn animation — keep character in map for rendering
      ch.matrixEffect = 'despawn';
      ch.matrixEffectTimer = 0;
      ch.matrixEffectSeeds = matrixEffectSeeds();
      ch.bubbleType = null;
    }
    // Clean up tracking maps immediately so keys don't collide
    this.subagentIdMap.delete(key);
    this.subagentMeta.delete(id);
    if (this.selectedAgentId === id) this.selectedAgentId = null;
    if (this.cameraFollowId === id) this.cameraFollowId = null;
  }

  /** Remove all sub-agents belonging to a parent agent */
  removeAllSubagents(parentAgentId: number): void {
    const toRemove: string[] = [];
    for (const [key, id] of this.subagentIdMap) {
      const meta = this.subagentMeta.get(id);
      if (meta && meta.parentAgentId === parentAgentId) {
        const ch = this.characters.get(id);
        if (ch) {
          if (ch.matrixEffect === 'despawn') {
            // Already despawning — just clean up maps
            this.subagentMeta.delete(id);
            toRemove.push(key);
            continue;
          }
          if (ch.seatId) {
            const seat = this.seats.get(ch.seatId);
            if (seat) seat.assigned = false;
          }
          // Start despawn animation
          ch.matrixEffect = 'despawn';
          ch.matrixEffectTimer = 0;
          ch.matrixEffectSeeds = matrixEffectSeeds();
          ch.bubbleType = null;
        }
        this.subagentMeta.delete(id);
        if (this.selectedAgentId === id) this.selectedAgentId = null;
        if (this.cameraFollowId === id) this.cameraFollowId = null;
        toRemove.push(key);
      }
    }
    for (const key of toRemove) {
      this.subagentIdMap.delete(key);
    }
  }

  /** Look up the sub-agent character ID for a given parent+toolId, or null */
  getSubagentId(parentAgentId: number, parentToolId: string): number | null {
    return this.subagentIdMap.get(`${parentAgentId}:${parentToolId}`) ?? null;
  }

  setAgentActive(id: number, active: boolean): void {
    const ch = this.characters.get(id);
    if (ch) {
      ch.isActive = active;
      if (!active) {
        // Sentinel -1: signals turn just ended, skip next seat rest timer.
        // Prevents the WALK handler from setting a 2-4 min rest on arrival.
        ch.seatTimer = -1;
        ch.path = [];
        ch.moveProgress = 0;
      }
      this.rebuildFurnitureInstances();
    }
  }

  /** Rebuild furniture instances with auto-state applied (active agents turn electronics ON) */
  private rebuildFurnitureInstances(): void {
    // Collect tiles where active agents face desks
    const autoOnTiles = new Set<string>();
    for (const ch of this.characters.values()) {
      if (!ch.isActive || !ch.seatId) continue;
      const seat = this.seats.get(ch.seatId);
      if (!seat) continue;
      // Find the desk tile(s) the agent faces from their seat
      const dCol =
        seat.facingDir === Direction.RIGHT ? 1 : seat.facingDir === Direction.LEFT ? -1 : 0;
      const dRow = seat.facingDir === Direction.DOWN ? 1 : seat.facingDir === Direction.UP ? -1 : 0;
      // Check tiles in the facing direction (desk could be 1-3 tiles deep)
      for (let d = 1; d <= AUTO_ON_FACING_DEPTH; d++) {
        const tileCol = seat.seatCol + dCol * d;
        const tileRow = seat.seatRow + dRow * d;
        autoOnTiles.add(`${tileCol},${tileRow}`);
      }
      // Also check tiles to the sides of the facing direction (desks can be wide)
      for (let d = 1; d <= AUTO_ON_SIDE_DEPTH; d++) {
        const baseCol = seat.seatCol + dCol * d;
        const baseRow = seat.seatRow + dRow * d;
        if (dCol !== 0) {
          // Facing left/right: check tiles above and below
          autoOnTiles.add(`${baseCol},${baseRow - 1}`);
          autoOnTiles.add(`${baseCol},${baseRow + 1}`);
        } else {
          // Facing up/down: check tiles left and right
          autoOnTiles.add(`${baseCol - 1},${baseRow}`);
          autoOnTiles.add(`${baseCol + 1},${baseRow}`);
        }
      }
    }

    if (autoOnTiles.size === 0) {
      this.furniture = layoutToFurnitureInstances(this.layout.furniture);
      return;
    }

    // Build modified furniture list with auto-state and animation applied
    const animFrame = Math.floor(this.furnitureAnimTimer / FURNITURE_ANIM_INTERVAL_SEC);
    const modifiedFurniture: PlacedFurniture[] = this.layout.furniture.map((item) => {
      const entry = getCatalogEntry(item.type);
      if (!entry) return item;
      // Check if any tile of this furniture overlaps an auto-on tile
      for (let dr = 0; dr < entry.footprintH; dr++) {
        for (let dc = 0; dc < entry.footprintW; dc++) {
          if (autoOnTiles.has(`${item.col + dc},${item.row + dr}`)) {
            let onType = getOnStateType(item.type);
            if (onType !== item.type) {
              // Check if the on-state type has animation frames
              const frames = getAnimationFrames(onType);
              if (frames && frames.length > 1) {
                const frameIdx = animFrame % frames.length;
                onType = frames[frameIdx];
              }
              return { ...item, type: onType };
            }
            return item;
          }
        }
      }
      return item;
    });

    this.furniture = layoutToFurnitureInstances(modifiedFurniture);
  }

  setAgentTool(id: number, tool: string | null): void {
    const ch = this.characters.get(id);
    if (ch) {
      ch.currentTool = tool;
    }
  }

  showPermissionBubble(id: number): void {
    const ch = this.characters.get(id);
    if (ch) {
      ch.bubbleType = 'permission';
      ch.bubbleTimer = 0;
    }
  }

  clearPermissionBubble(id: number): void {
    const ch = this.characters.get(id);
    if (ch && ch.bubbleType === 'permission') {
      ch.bubbleType = null;
      ch.bubbleTimer = 0;
    }
  }

  showWaitingBubble(id: number): void {
    const ch = this.characters.get(id);
    if (ch) {
      ch.bubbleType = 'waiting';
      ch.bubbleTimer = WAITING_BUBBLE_DURATION_SEC;
    }
  }

  /** Dismiss bubble on click — permission: instant, waiting: quick fade */
  dismissBubble(id: number): void {
    const ch = this.characters.get(id);
    if (!ch || !ch.bubbleType) return;
    if (ch.bubbleType === 'permission') {
      ch.bubbleType = null;
      ch.bubbleTimer = 0;
    } else if (ch.bubbleType === 'waiting') {
      // Trigger immediate fade (0.3s remaining)
      ch.bubbleTimer = Math.min(ch.bubbleTimer, DISMISS_BUBBLE_FAST_FADE_SEC);
    }
  }

  update(dt: number): void {
    // Furniture animation cycling
    const prevFrame = Math.floor(this.furnitureAnimTimer / FURNITURE_ANIM_INTERVAL_SEC);
    this.furnitureAnimTimer += dt;
    const newFrame = Math.floor(this.furnitureAnimTimer / FURNITURE_ANIM_INTERVAL_SEC);
    if (newFrame !== prevFrame) {
      this.rebuildFurnitureInstances();
    }

    const toDelete: number[] = [];
    for (const ch of this.characters.values()) {
      // Handle matrix effect animation
      if (ch.matrixEffect) {
        ch.matrixEffectTimer += dt;
        if (ch.matrixEffectTimer >= MATRIX_EFFECT_DURATION) {
          if (ch.matrixEffect === 'spawn') {
            // Spawn complete — clear effect, resume normal FSM
            ch.matrixEffect = null;
            ch.matrixEffectTimer = 0;
            ch.matrixEffectSeeds = [];
          } else {
            // Despawn complete — mark for deletion
            toDelete.push(ch.id);
          }
        }
        continue; // skip normal FSM while effect is active
      }

      // Temporarily unblock own seat so character can pathfind to it
      this.withOwnSeatUnblocked(ch, () =>
        updateCharacter(ch, dt, this.walkableTiles, this.seats, this.tileMap, this.blockedTiles),
      );

      // Tick bubble timer for waiting bubbles
      if (ch.bubbleType === 'waiting') {
        ch.bubbleTimer -= dt;
        if (ch.bubbleTimer <= 0) {
          ch.bubbleType = null;
          ch.bubbleTimer = 0;
        }
      }
    }
    // Remove characters that finished despawn
    for (const id of toDelete) {
      this.characters.delete(id);
    }
  }

  getCharacters(): Character[] {
    return Array.from(this.characters.values());
  }

  /** Get character at pixel position (for hit testing). Returns id or null. */
  getCharacterAt(worldX: number, worldY: number): number | null {
    const chars = this.getCharacters().sort((a, b) => b.y - a.y);
    for (const ch of chars) {
      // Skip characters that are despawning
      if (ch.matrixEffect === 'despawn') continue;
      // Character sprite is 16x24, anchored bottom-center
      // Apply sitting offset to match visual position
      const sittingOffset = ch.state === CharacterState.TYPE ? CHARACTER_SITTING_OFFSET_PX : 0;
      const anchorY = ch.y + sittingOffset;
      const left = ch.x - CHARACTER_HIT_HALF_WIDTH;
      const right = ch.x + CHARACTER_HIT_HALF_WIDTH;
      const top = anchorY - CHARACTER_HIT_HEIGHT;
      const bottom = anchorY;
      if (worldX >= left && worldX <= right && worldY >= top && worldY <= bottom) {
        return ch.id;
      }
    }
    return null;
  }
}
```

## File: `webview-ui/src/office/engine/renderer.ts`
```typescript
import {
  BUBBLE_FADE_DURATION_SEC,
  BUBBLE_SITTING_OFFSET_PX,
  BUBBLE_VERTICAL_OFFSET_PX,
  BUTTON_ICON_SIZE_FACTOR,
  BUTTON_LINE_WIDTH_MIN,
  BUTTON_LINE_WIDTH_ZOOM_FACTOR,
  BUTTON_MIN_RADIUS,
  BUTTON_RADIUS_ZOOM_FACTOR,
  CHARACTER_SITTING_OFFSET_PX,
  CHARACTER_Z_SORT_OFFSET,
  DELETE_BUTTON_BG,
  FALLBACK_FLOOR_COLOR,
  GHOST_BORDER_HOVER_FILL,
  GHOST_BORDER_HOVER_STROKE,
  GHOST_BORDER_STROKE,
  GHOST_INVALID_TINT,
  GHOST_PREVIEW_SPRITE_ALPHA,
  GHOST_PREVIEW_TINT_ALPHA,
  GHOST_VALID_TINT,
  GRID_LINE_COLOR,
  HOVERED_OUTLINE_ALPHA,
  OUTLINE_Z_SORT_OFFSET,
  ROTATE_BUTTON_BG,
  SEAT_AVAILABLE_COLOR,
  SEAT_BUSY_COLOR,
  SEAT_OWN_COLOR,
  SELECTED_OUTLINE_ALPHA,
  SELECTION_DASH_PATTERN,
  SELECTION_HIGHLIGHT_COLOR,
  VOID_TILE_DASH_PATTERN,
  VOID_TILE_OUTLINE_COLOR,
} from '../../constants.js';
import { getColorizedFloorSprite, hasFloorSprites, WALL_COLOR } from '../floorTiles.js';
import { getCachedSprite, getOutlineSprite } from '../sprites/spriteCache.js';
import {
  BUBBLE_PERMISSION_SPRITE,
  BUBBLE_WAITING_SPRITE,
  getCharacterSprites,
} from '../sprites/spriteData.js';
import type {
  Character,
  FloorColor,
  FurnitureInstance,
  Seat,
  SpriteData,
  TileType as TileTypeVal,
} from '../types.js';
import { CharacterState, TILE_SIZE, TileType } from '../types.js';
import { getWallInstances, hasWallSprites, wallColorToHex } from '../wallTiles.js';
import { getCharacterSprite } from './characters.js';
import { renderMatrixEffect } from './matrixEffect.js';

// ── Render functions ────────────────────────────────────────────

export function renderTileGrid(
  ctx: CanvasRenderingContext2D,
  tileMap: TileTypeVal[][],
  offsetX: number,
  offsetY: number,
  zoom: number,
  tileColors?: Array<FloorColor | null>,
  cols?: number,
): void {
  const s = TILE_SIZE * zoom;
  const useSpriteFloors = hasFloorSprites();
  const tmRows = tileMap.length;
  const tmCols = tmRows > 0 ? tileMap[0].length : 0;
  const layoutCols = cols ?? tmCols;

  // Floor tiles + wall base color
  for (let r = 0; r < tmRows; r++) {
    for (let c = 0; c < tmCols; c++) {
      const tile = tileMap[r][c];

      // Skip VOID tiles entirely (transparent)
      if (tile === TileType.VOID) continue;

      if (tile === TileType.WALL || !useSpriteFloors) {
        // Wall tiles or fallback: solid color
        if (tile === TileType.WALL) {
          const colorIdx = r * layoutCols + c;
          const wallColor = tileColors?.[colorIdx];
          ctx.fillStyle = wallColor ? wallColorToHex(wallColor) : WALL_COLOR;
        } else {
          ctx.fillStyle = FALLBACK_FLOOR_COLOR;
        }
        ctx.fillRect(offsetX + c * s, offsetY + r * s, s, s);
        continue;
      }

      // Floor tile: get colorized sprite
      const colorIdx = r * layoutCols + c;
      const color = tileColors?.[colorIdx] ?? { h: 0, s: 0, b: 0, c: 0 };
      const sprite = getColorizedFloorSprite(tile, color);
      const cached = getCachedSprite(sprite, zoom);
      ctx.drawImage(cached, offsetX + c * s, offsetY + r * s);
    }
  }
}

interface ZDrawable {
  zY: number;
  draw: (ctx: CanvasRenderingContext2D) => void;
}

export function renderScene(
  ctx: CanvasRenderingContext2D,
  furniture: FurnitureInstance[],
  characters: Character[],
  offsetX: number,
  offsetY: number,
  zoom: number,
  selectedAgentId: number | null,
  hoveredAgentId: number | null,
): void {
  const drawables: ZDrawable[] = [];

  // Furniture
  for (const f of furniture) {
    const cached = getCachedSprite(f.sprite, zoom);
    const fx = offsetX + f.x * zoom;
    const fy = offsetY + f.y * zoom;
    if (f.mirrored) {
      drawables.push({
        zY: f.zY,
        draw: (c) => {
          c.save();
          c.translate(fx + cached.width, fy);
          c.scale(-1, 1);
          c.drawImage(cached, 0, 0);
          c.restore();
        },
      });
    } else {
      drawables.push({
        zY: f.zY,
        draw: (c) => {
          c.drawImage(cached, fx, fy);
        },
      });
    }
  }

  // Characters
  for (const ch of characters) {
    const sprites = getCharacterSprites(ch.palette, ch.hueShift);
    const spriteData = getCharacterSprite(ch, sprites);
    const cached = getCachedSprite(spriteData, zoom);
    // Sitting offset: shift character down when seated so they visually sit in the chair
    const sittingOffset = ch.state === CharacterState.TYPE ? CHARACTER_SITTING_OFFSET_PX : 0;
    // Anchor at bottom-center of character — round to integer device pixels
    const drawX = Math.round(offsetX + ch.x * zoom - cached.width / 2);
    const drawY = Math.round(offsetY + (ch.y + sittingOffset) * zoom - cached.height);

    // Sort characters by bottom of their tile (not center) so they render
    // in front of same-row furniture (e.g. chairs) but behind furniture
    // at lower rows (e.g. desks, bookshelves that occlude from below).
    const charZY = ch.y + TILE_SIZE / 2 + CHARACTER_Z_SORT_OFFSET;

    // Matrix spawn/despawn effect — skip outline, use per-pixel rendering
    if (ch.matrixEffect) {
      const mDrawX = drawX;
      const mDrawY = drawY;
      const mSpriteData = spriteData;
      const mCh = ch;
      drawables.push({
        zY: charZY,
        draw: (c) => {
          renderMatrixEffect(c, mCh, mSpriteData, mDrawX, mDrawY, zoom);
        },
      });
      continue;
    }

    // White outline: full opacity for selected, 50% for hover
    const isSelected = selectedAgentId !== null && ch.id === selectedAgentId;
    const isHovered = hoveredAgentId !== null && ch.id === hoveredAgentId;
    if (isSelected || isHovered) {
      const outlineAlpha = isSelected ? SELECTED_OUTLINE_ALPHA : HOVERED_OUTLINE_ALPHA;
      const outlineData = getOutlineSprite(spriteData);
      const outlineCached = getCachedSprite(outlineData, zoom);
      const olDrawX = drawX - zoom; // 1 sprite-pixel offset, scaled
      const olDrawY = drawY - zoom; // outline follows sitting offset via drawY
      drawables.push({
        zY: charZY - OUTLINE_Z_SORT_OFFSET, // sort just before character
        draw: (c) => {
          c.save();
          c.globalAlpha = outlineAlpha;
          c.drawImage(outlineCached, olDrawX, olDrawY);
          c.restore();
        },
      });
    }

    drawables.push({
      zY: charZY,
      draw: (c) => {
        c.drawImage(cached, drawX, drawY);
      },
    });
  }

  // Sort by Y (lower = in front = drawn later)
  drawables.sort((a, b) => a.zY - b.zY);

  for (const d of drawables) {
    d.draw(ctx);
  }
}

// ── Seat indicators ─────────────────────────────────────────────

export function renderSeatIndicators(
  ctx: CanvasRenderingContext2D,
  seats: Map<string, Seat>,
  characters: Map<number, Character>,
  selectedAgentId: number | null,
  hoveredTile: { col: number; row: number } | null,
  offsetX: number,
  offsetY: number,
  zoom: number,
): void {
  if (selectedAgentId === null || !hoveredTile) return;
  const selectedChar = characters.get(selectedAgentId);
  if (!selectedChar) return;

  // Only show indicator for the hovered seat tile
  for (const [uid, seat] of seats) {
    if (seat.seatCol !== hoveredTile.col || seat.seatRow !== hoveredTile.row) continue;

    const s = TILE_SIZE * zoom;
    const x = offsetX + seat.seatCol * s;
    const y = offsetY + seat.seatRow * s;

    if (selectedChar.seatId === uid) {
      // Selected agent's own seat — blue
      ctx.fillStyle = SEAT_OWN_COLOR;
    } else if (!seat.assigned) {
      // Available seat — green
      ctx.fillStyle = SEAT_AVAILABLE_COLOR;
    } else {
      // Busy (assigned to another agent) — red
      ctx.fillStyle = SEAT_BUSY_COLOR;
    }
    ctx.fillRect(x, y, s, s);
    break;
  }
}

// ── Edit mode overlays ──────────────────────────────────────────

export function renderGridOverlay(
  ctx: CanvasRenderingContext2D,
  offsetX: number,
  offsetY: number,
  zoom: number,
  cols: number,
  rows: number,
  tileMap?: TileTypeVal[][],
): void {
  const s = TILE_SIZE * zoom;
  ctx.strokeStyle = GRID_LINE_COLOR;
  ctx.lineWidth = 1;
  ctx.beginPath();
  // Vertical lines — offset by 0.5 for crisp 1px lines
  for (let c = 0; c <= cols; c++) {
    const x = offsetX + c * s + 0.5;
    ctx.moveTo(x, offsetY);
    ctx.lineTo(x, offsetY + rows * s);
  }
  // Horizontal lines
  for (let r = 0; r <= rows; r++) {
    const y = offsetY + r * s + 0.5;
    ctx.moveTo(offsetX, y);
    ctx.lineTo(offsetX + cols * s, y);
  }
  ctx.stroke();

  // Draw faint dashed outlines on VOID tiles
  if (tileMap) {
    ctx.save();
    ctx.strokeStyle = VOID_TILE_OUTLINE_COLOR;
    ctx.lineWidth = 1;
    ctx.setLineDash(VOID_TILE_DASH_PATTERN);
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        if (tileMap[r]?.[c] === TileType.VOID) {
          ctx.strokeRect(offsetX + c * s + 0.5, offsetY + r * s + 0.5, s - 1, s - 1);
        }
      }
    }
    ctx.restore();
  }
}

/** Draw faint expansion placeholders 1 tile outside grid bounds (ghost border). */
export function renderGhostBorder(
  ctx: CanvasRenderingContext2D,
  offsetX: number,
  offsetY: number,
  zoom: number,
  cols: number,
  rows: number,
  ghostHoverCol: number,
  ghostHoverRow: number,
): void {
  const s = TILE_SIZE * zoom;
  ctx.save();

  // Collect ghost border tiles: one ring around the grid
  const ghostTiles: Array<{ c: number; r: number }> = [];
  // Top and bottom rows
  for (let c = -1; c <= cols; c++) {
    ghostTiles.push({ c, r: -1 });
    ghostTiles.push({ c, r: rows });
  }
  // Left and right columns (excluding corners already added)
  for (let r = 0; r < rows; r++) {
    ghostTiles.push({ c: -1, r });
    ghostTiles.push({ c: cols, r });
  }

  for (const { c, r } of ghostTiles) {
    const x = offsetX + c * s;
    const y = offsetY + r * s;
    const isHovered = c === ghostHoverCol && r === ghostHoverRow;
    if (isHovered) {
      ctx.fillStyle = GHOST_BORDER_HOVER_FILL;
      ctx.fillRect(x, y, s, s);
    }
    ctx.strokeStyle = isHovered ? GHOST_BORDER_HOVER_STROKE : GHOST_BORDER_STROKE;
    ctx.lineWidth = 1;
    ctx.setLineDash(VOID_TILE_DASH_PATTERN);
    ctx.strokeRect(x + 0.5, y + 0.5, s - 1, s - 1);
  }

  ctx.restore();
}

export function renderGhostPreview(
  ctx: CanvasRenderingContext2D,
  sprite: SpriteData,
  col: number,
  row: number,
  valid: boolean,
  offsetX: number,
  offsetY: number,
  zoom: number,
  mirrored: boolean = false,
): void {
  const cached = getCachedSprite(sprite, zoom);
  const x = offsetX + col * TILE_SIZE * zoom;
  const y = offsetY + row * TILE_SIZE * zoom;
  ctx.save();
  ctx.globalAlpha = GHOST_PREVIEW_SPRITE_ALPHA;
  if (mirrored) {
    ctx.translate(x + cached.width, y);
    ctx.scale(-1, 1);
    ctx.drawImage(cached, 0, 0);
  } else {
    ctx.drawImage(cached, x, y);
  }
  // Tint overlay — reset transform for correct fill position
  ctx.restore();
  ctx.save();
  ctx.globalAlpha = GHOST_PREVIEW_TINT_ALPHA;
  ctx.fillStyle = valid ? GHOST_VALID_TINT : GHOST_INVALID_TINT;
  ctx.fillRect(x, y, cached.width, cached.height);
  ctx.restore();
}

export function renderSelectionHighlight(
  ctx: CanvasRenderingContext2D,
  col: number,
  row: number,
  w: number,
  h: number,
  offsetX: number,
  offsetY: number,
  zoom: number,
): void {
  const s = TILE_SIZE * zoom;
  const x = offsetX + col * s;
  const y = offsetY + row * s;
  ctx.save();
  ctx.strokeStyle = SELECTION_HIGHLIGHT_COLOR;
  ctx.lineWidth = 2;
  ctx.setLineDash(SELECTION_DASH_PATTERN);
  ctx.strokeRect(x + 1, y + 1, w * s - 2, h * s - 2);
  ctx.restore();
}

export function renderDeleteButton(
  ctx: CanvasRenderingContext2D,
  col: number,
  row: number,
  w: number,
  _h: number,
  offsetX: number,
  offsetY: number,
  zoom: number,
): DeleteButtonBounds {
  const s = TILE_SIZE * zoom;
  // Position at top-right corner of selected furniture
  const cx = offsetX + (col + w) * s + 1;
  const cy = offsetY + row * s - 1;
  const radius = Math.max(BUTTON_MIN_RADIUS, zoom * BUTTON_RADIUS_ZOOM_FACTOR);

  // Circle background
  ctx.save();
  ctx.beginPath();
  ctx.arc(cx, cy, radius, 0, Math.PI * 2);
  ctx.fillStyle = DELETE_BUTTON_BG;
  ctx.fill();

  // X mark
  ctx.strokeStyle = '#fff';
  ctx.lineWidth = Math.max(BUTTON_LINE_WIDTH_MIN, zoom * BUTTON_LINE_WIDTH_ZOOM_FACTOR);
  ctx.lineCap = 'round';
  const xSize = radius * BUTTON_ICON_SIZE_FACTOR;
  ctx.beginPath();
  ctx.moveTo(cx - xSize, cy - xSize);
  ctx.lineTo(cx + xSize, cy + xSize);
  ctx.moveTo(cx + xSize, cy - xSize);
  ctx.lineTo(cx - xSize, cy + xSize);
  ctx.stroke();
  ctx.restore();

  return { cx, cy, radius };
}

export function renderRotateButton(
  ctx: CanvasRenderingContext2D,
  col: number,
  row: number,
  _w: number,
  _h: number,
  offsetX: number,
  offsetY: number,
  zoom: number,
): RotateButtonBounds {
  const s = TILE_SIZE * zoom;
  // Position to the left of the delete button (which is at top-right corner)
  const radius = Math.max(BUTTON_MIN_RADIUS, zoom * BUTTON_RADIUS_ZOOM_FACTOR);
  const cx = offsetX + col * s - 1;
  const cy = offsetY + row * s - 1;

  // Circle background
  ctx.save();
  ctx.beginPath();
  ctx.arc(cx, cy, radius, 0, Math.PI * 2);
  ctx.fillStyle = ROTATE_BUTTON_BG;
  ctx.fill();

  // Circular arrow icon
  ctx.strokeStyle = '#fff';
  ctx.lineWidth = Math.max(BUTTON_LINE_WIDTH_MIN, zoom * BUTTON_LINE_WIDTH_ZOOM_FACTOR);
  ctx.lineCap = 'round';
  const arcR = radius * BUTTON_ICON_SIZE_FACTOR;
  ctx.beginPath();
  // Draw a 270-degree arc
  ctx.arc(cx, cy, arcR, -Math.PI * 0.8, Math.PI * 0.7);
  ctx.stroke();
  // Draw arrowhead at the end of the arc
  const endAngle = Math.PI * 0.7;
  const endX = cx + arcR * Math.cos(endAngle);
  const endY = cy + arcR * Math.sin(endAngle);
  const arrowSize = radius * 0.35;
  ctx.beginPath();
  ctx.moveTo(endX + arrowSize * 0.6, endY - arrowSize * 0.3);
  ctx.lineTo(endX, endY);
  ctx.lineTo(endX + arrowSize * 0.7, endY + arrowSize * 0.5);
  ctx.stroke();
  ctx.restore();

  return { cx, cy, radius };
}

// ── Speech bubbles ──────────────────────────────────────────────

export function renderBubbles(
  ctx: CanvasRenderingContext2D,
  characters: Character[],
  offsetX: number,
  offsetY: number,
  zoom: number,
): void {
  for (const ch of characters) {
    if (!ch.bubbleType) continue;

    const sprite =
      ch.bubbleType === 'permission' ? BUBBLE_PERMISSION_SPRITE : BUBBLE_WAITING_SPRITE;

    // Compute opacity: permission = full, waiting = fade in last 0.5s
    let alpha = 1.0;
    if (ch.bubbleType === 'waiting' && ch.bubbleTimer < BUBBLE_FADE_DURATION_SEC) {
      alpha = ch.bubbleTimer / BUBBLE_FADE_DURATION_SEC;
    }

    const cached = getCachedSprite(sprite, zoom);
    // Position: centered above the character's head
    // Character is anchored bottom-center at (ch.x, ch.y), sprite is 16x24
    // Place bubble above head with a small gap; follow sitting offset
    const sittingOff = ch.state === CharacterState.TYPE ? BUBBLE_SITTING_OFFSET_PX : 0;
    const bubbleX = Math.round(offsetX + ch.x * zoom - cached.width / 2);
    const bubbleY = Math.round(
      offsetY + (ch.y + sittingOff - BUBBLE_VERTICAL_OFFSET_PX) * zoom - cached.height - 1 * zoom,
    );

    ctx.save();
    if (alpha < 1.0) ctx.globalAlpha = alpha;
    ctx.drawImage(cached, bubbleX, bubbleY);
    ctx.restore();
  }
}

export interface ButtonBounds {
  /** Center X in device pixels */
  cx: number;
  /** Center Y in device pixels */
  cy: number;
  /** Radius in device pixels */
  radius: number;
}

export type DeleteButtonBounds = ButtonBounds;
export type RotateButtonBounds = ButtonBounds;

export interface EditorRenderState {
  showGrid: boolean;
  ghostSprite: SpriteData | null;
  ghostMirrored: boolean;
  ghostCol: number;
  ghostRow: number;
  ghostValid: boolean;
  selectedCol: number;
  selectedRow: number;
  selectedW: number;
  selectedH: number;
  hasSelection: boolean;
  isRotatable: boolean;
  /** Updated each frame by renderDeleteButton */
  deleteButtonBounds: DeleteButtonBounds | null;
  /** Updated each frame by renderRotateButton */
  rotateButtonBounds: RotateButtonBounds | null;
  /** Whether to show ghost border (expansion tiles outside grid) */
  showGhostBorder: boolean;
  /** Hovered ghost border tile col (-1 to cols) */
  ghostBorderHoverCol: number;
  /** Hovered ghost border tile row (-1 to rows) */
  ghostBorderHoverRow: number;
}

export interface SelectionRenderState {
  selectedAgentId: number | null;
  hoveredAgentId: number | null;
  hoveredTile: { col: number; row: number } | null;
  seats: Map<string, Seat>;
  characters: Map<number, Character>;
}

export function renderFrame(
  ctx: CanvasRenderingContext2D,
  canvasWidth: number,
  canvasHeight: number,
  tileMap: TileTypeVal[][],
  furniture: FurnitureInstance[],
  characters: Character[],
  zoom: number,
  panX: number,
  panY: number,
  selection?: SelectionRenderState,
  editor?: EditorRenderState,
  tileColors?: Array<FloorColor | null>,
  layoutCols?: number,
  layoutRows?: number,
): { offsetX: number; offsetY: number } {
  // Clear
  ctx.clearRect(0, 0, canvasWidth, canvasHeight);

  // Use layout dimensions (fallback to tileMap size)
  const cols = layoutCols ?? (tileMap.length > 0 ? tileMap[0].length : 0);
  const rows = layoutRows ?? tileMap.length;

  // Center map in viewport + pan offset (integer device pixels)
  const mapW = cols * TILE_SIZE * zoom;
  const mapH = rows * TILE_SIZE * zoom;
  const offsetX = Math.floor((canvasWidth - mapW) / 2) + Math.round(panX);
  const offsetY = Math.floor((canvasHeight - mapH) / 2) + Math.round(panY);

  // Draw tiles (floor + wall base color)
  renderTileGrid(ctx, tileMap, offsetX, offsetY, zoom, tileColors, layoutCols);

  // Seat indicators (below furniture/characters, on top of floor)
  if (selection) {
    renderSeatIndicators(
      ctx,
      selection.seats,
      selection.characters,
      selection.selectedAgentId,
      selection.hoveredTile,
      offsetX,
      offsetY,
      zoom,
    );
  }

  // Build wall instances for z-sorting with furniture and characters
  const wallInstances = hasWallSprites() ? getWallInstances(tileMap, tileColors, layoutCols) : [];
  const allFurniture = wallInstances.length > 0 ? [...wallInstances, ...furniture] : furniture;

  // Draw walls + furniture + characters (z-sorted)
  const selectedId = selection?.selectedAgentId ?? null;
  const hoveredId = selection?.hoveredAgentId ?? null;
  renderScene(ctx, allFurniture, characters, offsetX, offsetY, zoom, selectedId, hoveredId);

  // Speech bubbles (always on top of characters)
  renderBubbles(ctx, characters, offsetX, offsetY, zoom);

  // Editor overlays
  if (editor) {
    if (editor.showGrid) {
      renderGridOverlay(ctx, offsetX, offsetY, zoom, cols, rows, tileMap);
    }
    if (editor.showGhostBorder) {
      renderGhostBorder(
        ctx,
        offsetX,
        offsetY,
        zoom,
        cols,
        rows,
        editor.ghostBorderHoverCol,
        editor.ghostBorderHoverRow,
      );
    }
    if (editor.ghostSprite && editor.ghostCol >= 0) {
      renderGhostPreview(
        ctx,
        editor.ghostSprite,
        editor.ghostCol,
        editor.ghostRow,
        editor.ghostValid,
        offsetX,
        offsetY,
        zoom,
        editor.ghostMirrored,
      );
    }
    if (editor.hasSelection) {
      renderSelectionHighlight(
        ctx,
        editor.selectedCol,
        editor.selectedRow,
        editor.selectedW,
        editor.selectedH,
        offsetX,
        offsetY,
        zoom,
      );
      editor.deleteButtonBounds = renderDeleteButton(
        ctx,
        editor.selectedCol,
        editor.selectedRow,
        editor.selectedW,
        editor.selectedH,
        offsetX,
        offsetY,
        zoom,
      );
      if (editor.isRotatable) {
        editor.rotateButtonBounds = renderRotateButton(
          ctx,
          editor.selectedCol,
          editor.selectedRow,
          editor.selectedW,
          editor.selectedH,
          offsetX,
          offsetY,
          zoom,
        );
      } else {
        editor.rotateButtonBounds = null;
      }
    } else {
      editor.deleteButtonBounds = null;
      editor.rotateButtonBounds = null;
    }
  }

  return { offsetX, offsetY };
}
```

## File: `webview-ui/src/office/layout/furnitureCatalog.ts`
```typescript
import type { FurnitureCatalogEntry, SpriteData } from '../types.js';

export interface LoadedAssetData {
  catalog: Array<{
    id: string;
    label: string;
    category: string;
    width: number;
    height: number;
    footprintW: number;
    footprintH: number;
    isDesk: boolean;
    groupId?: string;
    orientation?: string; // 'front' | 'back' | 'left' | 'right' | 'side'
    state?: string; // 'on' | 'off'
    canPlaceOnSurfaces?: boolean;
    backgroundTiles?: number;
    canPlaceOnWalls?: boolean;
    mirrorSide?: boolean;
    rotationScheme?: string;
    animationGroup?: string;
    frame?: number;
  }>;
  sprites: Record<string, SpriteData>;
}

export type FurnitureCategory =
  | 'desks'
  | 'chairs'
  | 'storage'
  | 'decor'
  | 'electronics'
  | 'wall'
  | 'misc';

export interface CatalogEntryWithCategory extends FurnitureCatalogEntry {
  category: FurnitureCategory;
}

// ── Rotation groups ──────────────────────────────────────────────
// Flexible rotation: supports 2+ orientations (not just all 4)
interface RotationGroup {
  /** Ordered list of orientations available for this group */
  orientations: string[];
  /** Maps orientation → asset ID (for the default/off state) */
  members: Record<string, string>;
}

// Maps any member asset ID → its rotation group
const rotationGroups = new Map<string, RotationGroup>();

// ── State groups ────────────────────────────────────────────────
// Maps asset ID → its on/off counterpart (symmetric for toggle)
const stateGroups = new Map<string, string>();
// Directional maps for getOnStateType / getOffStateType
const offToOn = new Map<string, string>(); // off asset → on asset
const onToOff = new Map<string, string>(); // on asset → off asset

// ── Animation groups ────────────────────────────────────────────
// Maps animation group ID → ordered list of asset IDs by frame index
const animationGroups = new Map<string, string[]>();

// Internal catalog (includes all variants for getCatalogEntry lookups)
let internalCatalog: CatalogEntryWithCategory[] | null = null;

// Dynamic catalog built from loaded assets (when available)
// Only includes "front" variants for grouped items (shown in editor palette)
let dynamicCatalog: CatalogEntryWithCategory[] | null = null;
let dynamicCategories: FurnitureCategory[] | null = null;

/**
 * Build catalog from loaded assets. Returns true if successful.
 * Once built, all getCatalog* functions use the dynamic catalog.
 * Uses ONLY custom assets (excludes hardcoded furniture when assets are loaded).
 */
export function buildDynamicCatalog(assets: LoadedAssetData): boolean {
  if (!assets?.catalog || !assets?.sprites) return false;

  // Build all entries (including non-front variants)
  const allEntries = assets.catalog
    .map((asset) => {
      const sprite = assets.sprites[asset.id];
      if (!sprite) {
        console.warn(`No sprite data for asset ${asset.id}`);
        return null;
      }
      return {
        type: asset.id,
        label: asset.label,
        footprintW: asset.footprintW,
        footprintH: asset.footprintH,
        sprite,
        isDesk: asset.isDesk,
        category: asset.category as FurnitureCategory,
        ...(asset.orientation ? { orientation: asset.orientation } : {}),
        ...(asset.canPlaceOnSurfaces ? { canPlaceOnSurfaces: true } : {}),
        ...(asset.backgroundTiles ? { backgroundTiles: asset.backgroundTiles } : {}),
        ...(asset.canPlaceOnWalls ? { canPlaceOnWalls: true } : {}),
        ...(asset.mirrorSide ? { mirrorSide: true } : {}),
      };
    })
    .filter((e): e is CatalogEntryWithCategory => e !== null);

  // Create virtual ":left" entries for mirrorSide assets.
  // These share the same sprite but have a distinct type ID so rotation groups work.
  for (const asset of assets.catalog) {
    if (asset.mirrorSide && asset.orientation === 'side') {
      const sideEntry = allEntries.find((e) => e.type === asset.id);
      if (sideEntry) {
        allEntries.push({
          ...sideEntry,
          type: `${asset.id}:left`,
          orientation: 'left',
          mirrorSide: true,
        });
      }
    }
  }

  if (allEntries.length === 0) return false;

  // Build rotation groups from groupId + orientation metadata
  rotationGroups.clear();
  stateGroups.clear();
  offToOn.clear();
  onToOff.clear();
  animationGroups.clear();

  // Phase 1: Collect orientations per group (only "off" or stateless variants for rotation)
  // For mirrorSide assets with orientation "side", register as both "right" and virtual "left"
  const groupMap = new Map<string, Map<string, string>>(); // groupId → (orientation → assetId)
  for (const asset of assets.catalog) {
    if (asset.groupId && asset.orientation) {
      // For rotation groups, only use the "off" or stateless variant
      if (asset.state && asset.state !== 'off') continue;
      let orientMap = groupMap.get(asset.groupId);
      if (!orientMap) {
        orientMap = new Map();
        groupMap.set(asset.groupId, orientMap);
      }

      if (asset.orientation === 'side') {
        // "side" is registered as "right" in the rotation group
        orientMap.set('right', asset.id);
        if (asset.mirrorSide) {
          // Register the virtual ":left" entry with a distinct type ID
          orientMap.set('left', `${asset.id}:left`);
        }
      } else {
        orientMap.set(asset.orientation, asset.id);
      }
    }
  }

  // For 2-way rotation schemes, "side" maps to "right" only (no left)
  // Check rotationScheme from assets
  const rotationSchemes = new Map<string, string>(); // groupId → rotationScheme
  for (const asset of assets.catalog) {
    if (asset.groupId && asset.rotationScheme) {
      rotationSchemes.set(asset.groupId, asset.rotationScheme);
    }
  }

  // Phase 2: Register rotation groups with 2+ orientations
  const nonFrontIds = new Set<string>();
  const orientationOrder = ['front', 'right', 'back', 'left'];
  for (const [groupId, orientMap] of groupMap) {
    if (orientMap.size < 2) continue;
    const scheme = rotationSchemes.get(groupId);

    // For 2-way scheme, only use front and right (side)
    let allowedOrients = orientationOrder;
    if (scheme === '2-way') {
      allowedOrients = ['front', 'right'];
    }

    // Build ordered list of available orientations
    const orderedOrients = allowedOrients.filter((o) => orientMap.has(o));
    if (orderedOrients.length < 2) continue;
    const members: Record<string, string> = {};
    for (const o of orderedOrients) {
      members[o] = orientMap.get(o)!;
    }
    const rg: RotationGroup = { orientations: orderedOrients, members };
    // Register each unique asset ID in the rotation group
    const registeredIds = new Set<string>();
    for (const id of Object.values(members)) {
      if (!registeredIds.has(id)) {
        rotationGroups.set(id, rg);
        registeredIds.add(id);
      }
    }
    // Track non-front IDs to exclude from visible catalog
    for (const [orient, id] of Object.entries(members)) {
      if (orient !== 'front') nonFrontIds.add(id);
    }
  }

  // Phase 3: Build state groups (on ↔ off pairs within same groupId + orientation)
  const stateMap = new Map<string, Map<string, string>>(); // "groupId|orientation" → (state → assetId)
  for (const asset of assets.catalog) {
    if (asset.groupId && asset.state) {
      const key = `${asset.groupId}|${asset.orientation || ''}`;
      let sm = stateMap.get(key);
      if (!sm) {
        sm = new Map();
        stateMap.set(key, sm);
      }
      // For animation groups, use the first frame as the "on" representative
      if (asset.animationGroup && asset.frame !== undefined && asset.frame > 0) continue;
      sm.set(asset.state, asset.id);
    }
  }
  for (const sm of stateMap.values()) {
    const onId = sm.get('on');
    const offId = sm.get('off');
    if (onId && offId) {
      stateGroups.set(onId, offId);
      stateGroups.set(offId, onId);
      offToOn.set(offId, onId);
      onToOff.set(onId, offId);
    }
  }

  // Also register rotation groups for "on" state variants (so rotation works on on-state items too)
  for (const asset of assets.catalog) {
    if (asset.groupId && asset.orientation && asset.state === 'on') {
      // Skip non-first animation frames
      if (asset.animationGroup && asset.frame !== undefined && asset.frame > 0) continue;

      // Find the off-variant's rotation group
      const offCounterpart = stateGroups.get(asset.id);
      if (offCounterpart) {
        const offGroup = rotationGroups.get(offCounterpart);
        if (offGroup) {
          // Build an equivalent group for the "on" state
          const onMembers: Record<string, string> = {};
          for (const orient of offGroup.orientations) {
            const offId = offGroup.members[orient];
            const onId = stateGroups.get(offId);
            // Use on-state variant if available, otherwise fall back to off-state
            onMembers[orient] = onId ?? offId;
          }
          const onGroup: RotationGroup = {
            orientations: offGroup.orientations,
            members: onMembers,
          };
          for (const id of Object.values(onMembers)) {
            if (!rotationGroups.has(id)) {
              rotationGroups.set(id, onGroup);
            }
          }
        }
      }
    }
  }

  // Phase 4: Build animation groups
  const animGroupCollector = new Map<string, Array<{ id: string; frame: number }>>();
  for (const asset of assets.catalog) {
    if (asset.animationGroup && asset.frame !== undefined) {
      let frames = animGroupCollector.get(asset.animationGroup);
      if (!frames) {
        frames = [];
        animGroupCollector.set(asset.animationGroup, frames);
      }
      frames.push({ id: asset.id, frame: asset.frame });
    }
  }
  for (const [groupId, frames] of animGroupCollector) {
    frames.sort((a, b) => a.frame - b.frame);
    animationGroups.set(
      groupId,
      frames.map((f) => f.id),
    );
  }

  // Track "on" variant IDs and animation frame IDs (non-first) to exclude from visible catalog
  const onStateIds = new Set<string>();
  for (const asset of assets.catalog) {
    if (asset.state === 'on') onStateIds.add(asset.id);
  }

  // Store full internal catalog (all variants — for getCatalogEntry lookups)
  internalCatalog = allEntries;

  // Visible catalog: exclude non-front variants and "on" state variants
  const visibleEntries = allEntries.filter(
    (e) => !nonFrontIds.has(e.type) && !onStateIds.has(e.type),
  );

  // Strip orientation/state suffix from labels for grouped variants
  for (const entry of visibleEntries) {
    if (rotationGroups.has(entry.type) || stateGroups.has(entry.type)) {
      entry.label = entry.label
        .replace(/ - Front - Off$/, '')
        .replace(/ - Front$/, '')
        .replace(/ - Off$/, '');
    }
  }

  dynamicCatalog = visibleEntries;
  dynamicCategories = Array.from(new Set(visibleEntries.map((e) => e.category)))
    .filter((c): c is FurnitureCategory => !!c)
    .sort();

  const rotGroupCount = new Set(Array.from(rotationGroups.values())).size;
  const animGroupCount = animationGroups.size;
  console.log(
    `✓ Built dynamic catalog with ${allEntries.length} assets (${visibleEntries.length} visible, ${rotGroupCount} rotation groups, ${stateGroups.size / 2} state pairs, ${animGroupCount} animation groups)`,
  );
  return true;
}

export function getCatalogEntry(type: string): CatalogEntryWithCategory | undefined {
  // Check internal catalog (includes all variants, e.g., non-front rotations)
  if (internalCatalog) {
    return internalCatalog.find((e) => e.type === type);
  }
  return dynamicCatalog?.find((e) => e.type === type);
}

export function getCatalogByCategory(category: FurnitureCategory): CatalogEntryWithCategory[] {
  const catalog = dynamicCatalog ?? [];
  return catalog.filter((e) => e.category === category);
}

export function getActiveCatalog(): CatalogEntryWithCategory[] {
  return dynamicCatalog ?? [];
}

export function getActiveCategories(): Array<{ id: FurnitureCategory; label: string }> {
  const categories = dynamicCategories ?? [];
  return FURNITURE_CATEGORIES.filter((c) => categories.includes(c.id));
}

export const FURNITURE_CATEGORIES: Array<{ id: FurnitureCategory; label: string }> = [
  { id: 'desks', label: 'Desks' },
  { id: 'chairs', label: 'Chairs' },
  { id: 'storage', label: 'Storage' },
  { id: 'electronics', label: 'Tech' },
  { id: 'decor', label: 'Decor' },
  { id: 'wall', label: 'Wall' },
  { id: 'misc', label: 'Misc' },
];

// ── Rotation helpers ─────────────────────────────────────────────

/** Returns the next asset ID in the rotation group (cw or ccw), or null if not rotatable. */
export function getRotatedType(currentType: string, direction: 'cw' | 'ccw'): string | null {
  const group = rotationGroups.get(currentType);
  if (!group) return null;
  const order = group.orientations.map((o) => group.members[o]);
  const idx = order.indexOf(currentType);
  if (idx === -1) return null;
  const step = direction === 'cw' ? 1 : -1;
  const nextIdx = (idx + step + order.length) % order.length;
  return order[nextIdx];
}

/** Returns the toggled state variant (on↔off), or null if no state variant exists. */
export function getToggledType(currentType: string): string | null {
  return stateGroups.get(currentType) ?? null;
}

/** Returns the "on" variant if this type has one, otherwise returns the type unchanged. */
export function getOnStateType(currentType: string): string {
  return offToOn.get(currentType) ?? currentType;
}

/** Returns the "off" variant if this type has one, otherwise returns the type unchanged. */
export function getOffStateType(currentType: string): string {
  return onToOff.get(currentType) ?? currentType;
}

/** Returns true if the given furniture type is part of a rotation group. */
export function isRotatable(type: string): boolean {
  return rotationGroups.has(type);
}

/** Get ordered animation frame asset IDs for a given type, or null if not animated. */
export function getAnimationFrames(type: string): string[] | null {
  // Find the animation group this type belongs to
  for (const [, frames] of animationGroups) {
    if (frames.includes(type)) return frames;
  }
  return null;
}

/**
 * Get the orientation of a type within its rotation group, or undefined if not in a group.
 * Used by the renderer to determine if a "left" orientation should be mirrored.
 */
export function getOrientationInGroup(type: string): string | undefined {
  const group = rotationGroups.get(type);
  if (!group) return undefined;
  for (const [orient, id] of Object.entries(group.members)) {
    if (id === type) return orient;
  }
  return undefined;
}
```

## File: `webview-ui/src/office/layout/index.ts`
```typescript
export type { CatalogEntryWithCategory, FurnitureCategory } from './furnitureCatalog.js';
export { FURNITURE_CATEGORIES, getCatalogByCategory, getCatalogEntry } from './furnitureCatalog.js';
export {
  createDefaultLayout,
  deserializeLayout,
  getBlockedTiles,
  getSeatTiles,
  layoutToFurnitureInstances,
  layoutToSeats,
  layoutToTileMap,
  serializeLayout,
} from './layoutSerializer.js';
export { findPath, getWalkableTiles, isWalkable } from './tileMap.js';
```

## File: `webview-ui/src/office/layout/layoutSerializer.ts`
```typescript
import { getColorizedSprite } from '../colorize.js';
import type {
  FloorColor,
  FurnitureInstance,
  OfficeLayout,
  PlacedFurniture,
  Seat,
  TileType as TileTypeVal,
} from '../types.js';
import { DEFAULT_COLS, DEFAULT_ROWS, Direction, TILE_SIZE, TileType } from '../types.js';
import { getCatalogEntry, getOrientationInGroup } from './furnitureCatalog.js';

/** Convert flat tile array from layout into 2D grid */
export function layoutToTileMap(layout: OfficeLayout): TileTypeVal[][] {
  const map: TileTypeVal[][] = [];
  for (let r = 0; r < layout.rows; r++) {
    const row: TileTypeVal[] = [];
    for (let c = 0; c < layout.cols; c++) {
      row.push(layout.tiles[r * layout.cols + c]);
    }
    map.push(row);
  }
  return map;
}

/** Convert placed furniture into renderable FurnitureInstance[] */
export function layoutToFurnitureInstances(furniture: PlacedFurniture[]): FurnitureInstance[] {
  // Pre-compute desk zY per tile so surface items can sort in front of desks
  const deskZByTile = new Map<string, number>();
  for (const item of furniture) {
    const entry = getCatalogEntry(item.type);
    if (!entry || !entry.isDesk) continue;
    const deskZY = item.row * TILE_SIZE + entry.sprite.length;
    for (let dr = 0; dr < entry.footprintH; dr++) {
      for (let dc = 0; dc < entry.footprintW; dc++) {
        const key = `${item.col + dc},${item.row + dr}`;
        const prev = deskZByTile.get(key);
        if (prev === undefined || deskZY > prev) deskZByTile.set(key, deskZY);
      }
    }
  }

  const instances: FurnitureInstance[] = [];
  for (const item of furniture) {
    const entry = getCatalogEntry(item.type);
    if (!entry) continue;
    const x = item.col * TILE_SIZE;
    const y = item.row * TILE_SIZE;
    const spriteH = entry.sprite.length;
    let zY = y + spriteH;

    // Chair z-sorting: ensure characters sitting on chairs render correctly
    if (entry.category === 'chairs') {
      if (entry.orientation === 'back') {
        // Back-facing chairs render IN FRONT of the seated character
        // (the chair back visually occludes the character behind it)
        zY = (item.row + 1) * TILE_SIZE + 1;
      } else {
        // All other chairs: cap zY to first row bottom so characters
        // at any seat tile render in front of the chair
        zY = (item.row + 1) * TILE_SIZE;
      }
    }

    // Surface items render in front of the desk they sit on
    if (entry.canPlaceOnSurfaces) {
      for (let dr = 0; dr < entry.footprintH; dr++) {
        for (let dc = 0; dc < entry.footprintW; dc++) {
          const deskZ = deskZByTile.get(`${item.col + dc},${item.row + dr}`);
          if (deskZ !== undefined && deskZ + 0.5 > zY) zY = deskZ + 0.5;
        }
      }
    }

    // Colorize sprite if this furniture has a color override
    let sprite = entry.sprite;
    if (item.color) {
      const { h, s, b: bv, c: cv } = item.color;
      sprite = getColorizedSprite(
        `furn-${item.type}-${h}-${s}-${bv}-${cv}-${item.color.colorize ? 1 : 0}`,
        entry.sprite,
        item.color,
      );
    }

    // Determine if this instance should be mirrored (side asset used in "left" orientation)
    let mirrored = false;
    if (entry.mirrorSide) {
      const orientInGroup = getOrientationInGroup(item.type);
      if (orientInGroup === 'left') {
        mirrored = true;
      }
    }

    instances.push({ sprite, x, y, zY, ...(mirrored ? { mirrored: true } : {}) });
  }
  return instances;
}

/** Get all tiles blocked by furniture footprints, optionally excluding a set of tiles.
 *  Skips top backgroundTiles rows so characters can walk through them. */
export function getBlockedTiles(
  furniture: PlacedFurniture[],
  excludeTiles?: Set<string>,
): Set<string> {
  const tiles = new Set<string>();
  for (const item of furniture) {
    const entry = getCatalogEntry(item.type);
    if (!entry) continue;
    const bgRows = entry.backgroundTiles || 0;
    for (let dr = 0; dr < entry.footprintH; dr++) {
      if (dr < bgRows) continue; // skip background rows — characters can walk through
      for (let dc = 0; dc < entry.footprintW; dc++) {
        const key = `${item.col + dc},${item.row + dr}`;
        if (excludeTiles && excludeTiles.has(key)) continue;
        tiles.add(key);
      }
    }
  }
  return tiles;
}

/** Get tiles blocked for placement purposes — skips top backgroundTiles rows per item */
export function getPlacementBlockedTiles(
  furniture: PlacedFurniture[],
  excludeUid?: string,
): Set<string> {
  const tiles = new Set<string>();
  for (const item of furniture) {
    if (item.uid === excludeUid) continue;
    const entry = getCatalogEntry(item.type);
    if (!entry) continue;
    const bgRows = entry.backgroundTiles || 0;
    for (let dr = 0; dr < entry.footprintH; dr++) {
      if (dr < bgRows) continue; // skip background rows
      for (let dc = 0; dc < entry.footprintW; dc++) {
        tiles.add(`${item.col + dc},${item.row + dr}`);
      }
    }
  }
  return tiles;
}

/** Map chair orientation to character facing direction */
function orientationToFacing(orientation: string): Direction {
  switch (orientation) {
    case 'front':
      return Direction.DOWN;
    case 'back':
      return Direction.UP;
    case 'left':
      return Direction.LEFT;
    case 'right':
    case 'side':
      return Direction.RIGHT;
    default:
      return Direction.DOWN;
  }
}

/** Generate seats from chair furniture.
 *  Facing priority: 1) chair orientation, 2) adjacent desk, 3) forward (DOWN). */
export function layoutToSeats(furniture: PlacedFurniture[]): Map<string, Seat> {
  const seats = new Map<string, Seat>();

  // Build set of all desk tiles
  const deskTiles = new Set<string>();
  for (const item of furniture) {
    const entry = getCatalogEntry(item.type);
    if (!entry || !entry.isDesk) continue;
    for (let dr = 0; dr < entry.footprintH; dr++) {
      for (let dc = 0; dc < entry.footprintW; dc++) {
        deskTiles.add(`${item.col + dc},${item.row + dr}`);
      }
    }
  }

  const dirs: Array<{ dc: number; dr: number; facing: Direction }> = [
    { dc: 0, dr: -1, facing: Direction.UP }, // desk is above chair → face UP
    { dc: 0, dr: 1, facing: Direction.DOWN }, // desk is below chair → face DOWN
    { dc: -1, dr: 0, facing: Direction.LEFT }, // desk is left of chair → face LEFT
    { dc: 1, dr: 0, facing: Direction.RIGHT }, // desk is right of chair → face RIGHT
  ];

  // For each chair, every footprint tile becomes a seat.
  // Multi-tile chairs (e.g. 2-tile couches) produce multiple seats.
  for (const item of furniture) {
    const entry = getCatalogEntry(item.type);
    if (!entry || entry.category !== 'chairs') continue;

    let seatCount = 0;
    for (let dr = 0; dr < entry.footprintH; dr++) {
      for (let dc = 0; dc < entry.footprintW; dc++) {
        const tileCol = item.col + dc;
        const tileRow = item.row + dr;

        // Determine facing direction:
        // 1) Chair orientation takes priority
        // 2) Adjacent desk direction
        // 3) Default forward (DOWN)
        let facingDir: Direction = Direction.DOWN;
        if (entry.orientation) {
          facingDir = orientationToFacing(entry.orientation);
        } else {
          for (const d of dirs) {
            if (deskTiles.has(`${tileCol + d.dc},${tileRow + d.dr}`)) {
              facingDir = d.facing;
              break;
            }
          }
        }

        // First seat uses chair uid (backward compat), subsequent use uid:N
        const seatUid = seatCount === 0 ? item.uid : `${item.uid}:${seatCount}`;
        seats.set(seatUid, {
          uid: seatUid,
          seatCol: tileCol,
          seatRow: tileRow,
          facingDir,
          assigned: false,
        });
        seatCount++;
      }
    }
  }

  return seats;
}

/** Get the set of tiles occupied by seats (so they can be excluded from blocked tiles) */
export function getSeatTiles(seats: Map<string, Seat>): Set<string> {
  const tiles = new Set<string>();
  for (const seat of seats.values()) {
    tiles.add(`${seat.seatCol},${seat.seatRow}`);
  }
  return tiles;
}

/** Default floor colors for the two rooms */
const DEFAULT_LEFT_ROOM_COLOR: FloorColor = { h: 35, s: 30, b: 15, c: 0 }; // warm beige
const DEFAULT_RIGHT_ROOM_COLOR: FloorColor = { h: 25, s: 45, b: 5, c: 10 }; // warm brown

/** Create a minimal fallback layout (used only when no default-layout.json exists) */
export function createDefaultLayout(): OfficeLayout {
  const W = TileType.WALL;
  const F1 = TileType.FLOOR_1;
  const F2 = TileType.FLOOR_2;

  const tiles: TileTypeVal[] = [];
  const tileColors: Array<FloorColor | null> = [];

  for (let r = 0; r < DEFAULT_ROWS; r++) {
    for (let c = 0; c < DEFAULT_COLS; c++) {
      if (r === 0 || r === DEFAULT_ROWS - 1 || c === 0 || c === DEFAULT_COLS - 1) {
        tiles.push(W);
        tileColors.push(null);
      } else if (c < 10) {
        tiles.push(F1);
        tileColors.push(DEFAULT_LEFT_ROOM_COLOR);
      } else {
        tiles.push(F2);
        tileColors.push(DEFAULT_RIGHT_ROOM_COLOR);
      }
    }
  }

  // Minimal fallback with no furniture — the default-layout.json provides the real default
  return { version: 1, cols: DEFAULT_COLS, rows: DEFAULT_ROWS, tiles, tileColors, furniture: [] };
}

/** Serialize layout to JSON string */
export function serializeLayout(layout: OfficeLayout): string {
  return JSON.stringify(layout);
}

// ── Furniture type migration ────────────────────────────────────

/** Map old hardcoded FurnitureType values to new manifest-based IDs */
const LEGACY_TYPE_MAP: Record<string, string | null> = {
  desk: 'DESK_FRONT',
  chair: 'WOODEN_CHAIR_FRONT',
  bookshelf: 'BOOKSHELF',
  plant: 'PLANT',
  cooler: null, // no equivalent in new assets — remove
  whiteboard: 'WHITEBOARD',
  pc: 'PC_FRONT_OFF',
  lamp: null, // no equivalent in new assets — remove
};

/** Migrate old furniture type strings to new manifest IDs */
function migrateFurnitureTypes(furniture: PlacedFurniture[]): PlacedFurniture[] {
  const migrated: PlacedFurniture[] = [];
  for (const item of furniture) {
    const newType = LEGACY_TYPE_MAP[item.type];
    if (newType === undefined) {
      // Not a legacy type — keep as-is
      migrated.push(item);
    } else if (newType !== null) {
      // Migrate to new type
      migrated.push({ ...item, type: newType });
    }
    // newType === null → remove the item (no equivalent)
  }
  return migrated;
}

/** Deserialize layout from JSON string, migrating old tile types if needed */
export function deserializeLayout(json: string): OfficeLayout | null {
  try {
    const obj = JSON.parse(json);
    if (obj && obj.version === 1 && Array.isArray(obj.tiles) && Array.isArray(obj.furniture)) {
      return migrateLayout(obj as OfficeLayout);
    }
  } catch {
    /* ignore parse errors */
  }
  return null;
}

/**
 * Ensure layout has tileColors. If missing, generate defaults based on tile types.
 * Exported for use by message handlers that receive layouts over the wire.
 */
export function migrateLayoutColors(layout: OfficeLayout): OfficeLayout {
  return migrateLayout(layout);
}

/**
 * Migrate old layouts that use legacy tile types (TILE_FLOOR=1, WOOD_FLOOR=2, CARPET=3, DOORWAY=4)
 * to the new pattern-based system. Also migrates old furniture type strings and old VOID value.
 */
function migrateLayout(layout: OfficeLayout): OfficeLayout {
  // Migrate furniture types
  layout = { ...layout, furniture: migrateFurnitureTypes(layout.furniture) };

  // Migrate old VOID value (was 8, now 255) — only for legacy layouts since FLOOR_8 reuses value 8
  const OLD_VOID = 8;
  if (!layout.layoutRevision && layout.tiles.includes(OLD_VOID as TileTypeVal)) {
    layout = {
      ...layout,
      tiles: layout.tiles.map((t) => (t === OLD_VOID ? (TileType.VOID as TileTypeVal) : t)),
    };
  }

  if (layout.tileColors && layout.tileColors.length === layout.tiles.length) {
    return layout; // Already migrated tile colors
  }

  // Check if any tiles use old values (1-4) — these map directly to FLOOR_1-4
  // but need color assignments
  const tileColors: Array<FloorColor | null> = [];
  for (const tile of layout.tiles) {
    switch (tile) {
      case 0: // WALL
        tileColors.push(null);
        break;
      case 1: // was TILE_FLOOR → FLOOR_1 beige
        tileColors.push(DEFAULT_LEFT_ROOM_COLOR);
        break;
      case 2: // was WOOD_FLOOR → FLOOR_2 brown
        tileColors.push(DEFAULT_RIGHT_ROOM_COLOR);
        break;
      case 3: // was CARPET → FLOOR_3 purple
        tileColors.push({ h: 280, s: 40, b: -5, c: 0 });
        break;
      case 4: // was DOORWAY → FLOOR_4 tan
        tileColors.push({ h: 35, s: 25, b: 10, c: 0 });
        break;
      default:
        // Floor tile types without colors — use neutral gray
        tileColors.push(tile > 0 && tile !== TileType.VOID ? { h: 0, s: 0, b: 0, c: 0 } : null);
    }
  }

  return { ...layout, tileColors };
}
```

## File: `webview-ui/src/office/layout/tileMap.ts`
```typescript
import { TileType } from '../types.js';

/** Check if a tile is walkable (floor, carpet, or doorway, and not blocked by furniture) */
export function isWalkable(
  col: number,
  row: number,
  tileMap: TileType[][],
  blockedTiles: Set<string>,
): boolean {
  const rows = tileMap.length;
  const cols = rows > 0 ? tileMap[0].length : 0;
  if (row < 0 || row >= rows || col < 0 || col >= cols) return false;
  const t = tileMap[row][col];
  if (t === TileType.WALL || t === TileType.VOID) return false;
  if (blockedTiles.has(`${col},${row}`)) return false;
  return true;
}

/** Get walkable tile positions (grid coords) for wandering */
export function getWalkableTiles(
  tileMap: TileType[][],
  blockedTiles: Set<string>,
): Array<{ col: number; row: number }> {
  const rows = tileMap.length;
  const cols = rows > 0 ? tileMap[0].length : 0;
  const tiles: Array<{ col: number; row: number }> = [];
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (isWalkable(c, r, tileMap, blockedTiles)) {
        tiles.push({ col: c, row: r });
      }
    }
  }
  return tiles;
}

/** BFS pathfinding on 4-connected grid (no diagonals). Returns path excluding start, including end. */
export function findPath(
  startCol: number,
  startRow: number,
  endCol: number,
  endRow: number,
  tileMap: TileType[][],
  blockedTiles: Set<string>,
): Array<{ col: number; row: number }> {
  if (startCol === endCol && startRow === endRow) return [];

  const key = (c: number, r: number) => `${c},${r}`;
  const startKey = key(startCol, startRow);
  const endKey = key(endCol, endRow);

  // End must be walkable (or be a chair tile which may be adjacent to desk)
  // We allow the end tile even if it's not strictly walkable for chair positions
  const endWalkable = isWalkable(endCol, endRow, tileMap, blockedTiles);
  if (!endWalkable) {
    // If the end is a desk tile, we still can't path there
    return [];
  }

  const visited = new Set<string>();
  visited.add(startKey);

  const parent = new Map<string, string>();
  const queue: Array<{ col: number; row: number }> = [{ col: startCol, row: startRow }];

  const dirs = [
    { dc: 0, dr: -1 }, // up
    { dc: 0, dr: 1 }, // down
    { dc: -1, dr: 0 }, // left
    { dc: 1, dr: 0 }, // right
  ];

  while (queue.length > 0) {
    const curr = queue.shift()!;
    const currKey = key(curr.col, curr.row);

    if (currKey === endKey) {
      // Reconstruct path
      const path: Array<{ col: number; row: number }> = [];
      let k = endKey;
      while (k !== startKey) {
        const [c, r] = k.split(',').map(Number);
        path.unshift({ col: c, row: r });
        k = parent.get(k)!;
      }
      return path;
    }

    for (const d of dirs) {
      const nc = curr.col + d.dc;
      const nr = curr.row + d.dr;
      const nk = key(nc, nr);

      if (visited.has(nk)) continue;
      if (!isWalkable(nc, nr, tileMap, blockedTiles)) continue;

      visited.add(nk);
      parent.set(nk, currKey);
      queue.push({ col: nc, row: nr });
    }
  }

  // No path found
  return [];
}
```

## File: `webview-ui/src/office/sprites/bubble-permission.json`
```json
{
  "name": "bubble-permission",
  "description": "Permission bubble: white square with '...' in amber, and a tail pointer (11x13)",
  "width": 11,
  "height": 13,
  "palette": {
    "_": "",
    "B": "#555566",
    "F": "#EEEEFF",
    "A": "#CCA700"
  },
  "pixels": [
    ["B","B","B","B","B","B","B","B","B","B","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","A","F","A","F","A","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","B","B","B","B","B","B","B","B","B","B"],
    ["_","_","_","_","B","B","B","_","_","_","_"],
    ["_","_","_","_","_","B","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_","_"]
  ]
}
```

## File: `webview-ui/src/office/sprites/bubble-waiting.json`
```json
{
  "name": "bubble-waiting",
  "description": "Waiting bubble: white square with green checkmark, and a tail pointer (11x13)",
  "width": 11,
  "height": 13,
  "palette": {
    "_": "",
    "B": "#555566",
    "F": "#EEEEFF",
    "G": "#44BB66"
  },
  "pixels": [
    ["_","B","B","B","B","B","B","B","B","B","_"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","G","F","B"],
    ["B","F","F","F","F","F","F","G","F","F","B"],
    ["B","F","F","G","F","F","G","F","F","F","B"],
    ["B","F","F","F","G","G","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["B","F","F","F","F","F","F","F","F","F","B"],
    ["_","B","B","B","B","B","B","B","B","B","_"],
    ["_","_","_","_","B","B","B","_","_","_","_"],
    ["_","_","_","_","_","B","_","_","_","_","_"],
    ["_","_","_","_","_","_","_","_","_","_","_"]
  ]
}
```

## File: `webview-ui/src/office/sprites/index.ts`
```typescript
export { getCachedSprite, getOutlineSprite } from './spriteCache.js';
export type { CharacterSprites } from './spriteData.js';
export { getCharacterSprites } from './spriteData.js';
```

## File: `webview-ui/src/office/sprites/spriteCache.ts`
```typescript
import type { SpriteData } from '../types.js';

const zoomCaches = new Map<number, WeakMap<SpriteData, HTMLCanvasElement>>();

// ── Outline sprite generation ─────────────────────────────────

const outlineCache = new WeakMap<SpriteData, SpriteData>();

/** Generate a 1px white outline SpriteData (2px larger in each dimension) */
export function getOutlineSprite(sprite: SpriteData): SpriteData {
  const cached = outlineCache.get(sprite);
  if (cached) return cached;

  const rows = sprite.length;
  const cols = sprite[0].length;
  // Expanded grid: +2 in each dimension for 1px border
  const outline: string[][] = [];
  for (let r = 0; r < rows + 2; r++) {
    outline.push(new Array<string>(cols + 2).fill(''));
  }

  // For each opaque pixel, mark its 4 cardinal neighbors as white
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (sprite[r][c] === '') continue;
      const er = r + 1;
      const ec = c + 1;
      if (outline[er - 1][ec] === '') outline[er - 1][ec] = '#FFFFFF';
      if (outline[er + 1][ec] === '') outline[er + 1][ec] = '#FFFFFF';
      if (outline[er][ec - 1] === '') outline[er][ec - 1] = '#FFFFFF';
      if (outline[er][ec + 1] === '') outline[er][ec + 1] = '#FFFFFF';
    }
  }

  // Clear pixels that overlap with original opaque pixels
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (sprite[r][c] !== '') {
        outline[r + 1][c + 1] = '';
      }
    }
  }

  outlineCache.set(sprite, outline);
  return outline;
}

export function getCachedSprite(sprite: SpriteData, zoom: number): HTMLCanvasElement {
  let cache = zoomCaches.get(zoom);
  if (!cache) {
    cache = new WeakMap();
    zoomCaches.set(zoom, cache);
  }

  const cached = cache.get(sprite);
  if (cached) return cached;

  const rows = sprite.length;
  const cols = sprite[0].length;
  const canvas = document.createElement('canvas');
  canvas.width = cols * zoom;
  canvas.height = rows * zoom;
  const ctx = canvas.getContext('2d')!;
  ctx.imageSmoothingEnabled = false;

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      const color = sprite[r][c];
      if (color === '') continue;
      ctx.fillStyle = color;
      ctx.fillRect(c * zoom, r * zoom, zoom, zoom);
    }
  }

  cache.set(sprite, canvas);
  return canvas;
}
```

## File: `webview-ui/src/office/sprites/spriteData.ts`
```typescript
import { adjustSprite } from '../colorize.js';
import type { Direction, FloorColor, SpriteData } from '../types.js';
import { Direction as Dir } from '../types.js';
import bubblePermissionData from './bubble-permission.json';
import bubbleWaitingData from './bubble-waiting.json';

// ── Speech Bubble Sprites ───────────────────────────────────────

interface BubbleSpriteJson {
  palette: Record<string, string>;
  pixels: string[][];
}

function resolveBubbleSprite(data: BubbleSpriteJson): SpriteData {
  return data.pixels.map((row) => row.map((key) => data.palette[key] ?? key));
}

/** Permission bubble: white square with "..." in amber, and a tail pointer (11x13) */
export const BUBBLE_PERMISSION_SPRITE: SpriteData = resolveBubbleSprite(bubblePermissionData);

/** Waiting bubble: white square with green checkmark, and a tail pointer (11x13) */
export const BUBBLE_WAITING_SPRITE: SpriteData = resolveBubbleSprite(bubbleWaitingData);

// ════════════════════════════════════════════════════════════════
// Loaded character sprites (from PNG assets)
// ════════════════════════════════════════════════════════════════

interface LoadedCharacterData {
  down: SpriteData[];
  up: SpriteData[];
  right: SpriteData[];
}

let loadedCharacters: LoadedCharacterData[] | null = null;

/** Set pre-colored character sprites loaded from PNG assets. Call this when characterSpritesLoaded message arrives. */
export function setCharacterTemplates(data: LoadedCharacterData[]): void {
  loadedCharacters = data;
  // Clear cache so sprites are rebuilt from loaded data
  spriteCache.clear();
}

/** Flip a SpriteData horizontally (for generating left sprites from right) */
export function flipSpriteHorizontal(sprite: SpriteData): SpriteData {
  return sprite.map((row) => [...row].reverse());
}

// ════════════════════════════════════════════════════════════════
// Sprite resolution + caching
// ════════════════════════════════════════════════════════════════

export interface CharacterSprites {
  walk: Record<Direction, [SpriteData, SpriteData, SpriteData, SpriteData]>;
  typing: Record<Direction, [SpriteData, SpriteData]>;
  reading: Record<Direction, [SpriteData, SpriteData]>;
}

const spriteCache = new Map<string, CharacterSprites>();

/** Apply hue shift to every sprite in a CharacterSprites set */
function hueShiftSprites(sprites: CharacterSprites, hueShift: number): CharacterSprites {
  const color: FloorColor = { h: hueShift, s: 0, b: 0, c: 0 };
  const shift = (s: SpriteData) => adjustSprite(s, color);
  const shiftWalk = (
    arr: [SpriteData, SpriteData, SpriteData, SpriteData],
  ): [SpriteData, SpriteData, SpriteData, SpriteData] => [
    shift(arr[0]),
    shift(arr[1]),
    shift(arr[2]),
    shift(arr[3]),
  ];
  const shiftPair = (arr: [SpriteData, SpriteData]): [SpriteData, SpriteData] => [
    shift(arr[0]),
    shift(arr[1]),
  ];
  return {
    walk: {
      [Dir.DOWN]: shiftWalk(sprites.walk[Dir.DOWN]),
      [Dir.UP]: shiftWalk(sprites.walk[Dir.UP]),
      [Dir.RIGHT]: shiftWalk(sprites.walk[Dir.RIGHT]),
      [Dir.LEFT]: shiftWalk(sprites.walk[Dir.LEFT]),
    } as Record<Direction, [SpriteData, SpriteData, SpriteData, SpriteData]>,
    typing: {
      [Dir.DOWN]: shiftPair(sprites.typing[Dir.DOWN]),
      [Dir.UP]: shiftPair(sprites.typing[Dir.UP]),
      [Dir.RIGHT]: shiftPair(sprites.typing[Dir.RIGHT]),
      [Dir.LEFT]: shiftPair(sprites.typing[Dir.LEFT]),
    } as Record<Direction, [SpriteData, SpriteData]>,
    reading: {
      [Dir.DOWN]: shiftPair(sprites.reading[Dir.DOWN]),
      [Dir.UP]: shiftPair(sprites.reading[Dir.UP]),
      [Dir.RIGHT]: shiftPair(sprites.reading[Dir.RIGHT]),
      [Dir.LEFT]: shiftPair(sprites.reading[Dir.LEFT]),
    } as Record<Direction, [SpriteData, SpriteData]>,
  };
}

/** Create a transparent placeholder sprite of given dimensions */
function emptySprite(w: number, h: number): SpriteData {
  const rows: string[][] = [];
  for (let y = 0; y < h; y++) {
    rows.push(new Array(w).fill(''));
  }
  return rows;
}

export function getCharacterSprites(paletteIndex: number, hueShift = 0): CharacterSprites {
  const cacheKey = `${paletteIndex}:${hueShift}`;
  const cached = spriteCache.get(cacheKey);
  if (cached) return cached;

  let sprites: CharacterSprites;

  if (loadedCharacters) {
    // Use pre-colored character sprites directly (no palette swapping)
    const char = loadedCharacters[paletteIndex % loadedCharacters.length];
    const d = char.down;
    const u = char.up;
    const rt = char.right;
    const flip = flipSpriteHorizontal;

    sprites = {
      walk: {
        [Dir.DOWN]: [d[0], d[1], d[2], d[1]],
        [Dir.UP]: [u[0], u[1], u[2], u[1]],
        [Dir.RIGHT]: [rt[0], rt[1], rt[2], rt[1]],
        [Dir.LEFT]: [flip(rt[0]), flip(rt[1]), flip(rt[2]), flip(rt[1])],
      },
      typing: {
        [Dir.DOWN]: [d[3], d[4]],
        [Dir.UP]: [u[3], u[4]],
        [Dir.RIGHT]: [rt[3], rt[4]],
        [Dir.LEFT]: [flip(rt[3]), flip(rt[4])],
      },
      reading: {
        [Dir.DOWN]: [d[5], d[6]],
        [Dir.UP]: [u[5], u[6]],
        [Dir.RIGHT]: [rt[5], rt[6]],
        [Dir.LEFT]: [flip(rt[5]), flip(rt[6])],
      },
    };
  } else {
    // Fallback: return transparent placeholder sprites (16×32)
    const e = emptySprite(16, 32);
    const walkSet: [SpriteData, SpriteData, SpriteData, SpriteData] = [e, e, e, e];
    const pairSet: [SpriteData, SpriteData] = [e, e];
    sprites = {
      walk: {
        [Dir.DOWN]: walkSet,
        [Dir.UP]: walkSet,
        [Dir.RIGHT]: walkSet,
        [Dir.LEFT]: walkSet,
      },
      typing: {
        [Dir.DOWN]: pairSet,
        [Dir.UP]: pairSet,
        [Dir.RIGHT]: pairSet,
        [Dir.LEFT]: pairSet,
      },
      reading: {
        [Dir.DOWN]: pairSet,
        [Dir.UP]: pairSet,
        [Dir.RIGHT]: pairSet,
        [Dir.LEFT]: pairSet,
      },
    };
  }

  // Apply hue shift if non-zero
  if (hueShift !== 0) {
    sprites = hueShiftSprites(sprites, hueShift);
  }

  spriteCache.set(cacheKey, sprites);
  return sprites;
}
```


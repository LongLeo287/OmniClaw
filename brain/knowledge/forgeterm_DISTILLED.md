---
id: ForgeTerm
type: knowledge
owner: OA_Triage
---
# ForgeTerm
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "forgeterm",
  "private": true,
  "version": "0.1.3",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "typecheck": "tsc --noEmit",
    "lint": "eslint .",
    "test": "vitest run",
    "test:watch": "vitest",
    "rust:fmt:check": "cargo fmt --manifest-path src-tauri/Cargo.toml --all -- --check",
    "rust:clippy": "cargo clippy --manifest-path src-tauri/Cargo.toml --all-targets -- -D warnings",
    "rust:test": "cargo test --manifest-path src-tauri/Cargo.toml",
    "check": "pnpm lint && pnpm typecheck && pnpm test && pnpm build && pnpm rust:fmt:check && pnpm rust:clippy && pnpm rust:test",
    "preview": "vite preview",
    "tauri": "tauri"
  },
  "dependencies": {
    "@radix-ui/react-slot": "^1.1.0",
    "@tauri-apps/api": "^2",
    "@tauri-apps/plugin-opener": "^2",
    "@xterm/addon-fit": "^0.11.0",
    "@xterm/addon-unicode11": "^0.9.0",
    "@xterm/xterm": "^5.5.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "lucide-react": "^0.468.0",
    "react": "^19.1.0",
    "react-dom": "^19.1.0",
    "react-resizable-panels": "^2.1.7",
    "shadcn": "^2.0.0",
    "tailwind-merge": "^2.5.5",
    "tw-animate-css": "^1.3.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.19.0",
    "@tailwindcss/vite": "^4.1.3",
    "@tauri-apps/cli": "^2",
    "@testing-library/jest-dom": "^6.6.3",
    "@testing-library/react": "^16.1.0",
    "@types/node": "^22.13.4",
    "@types/react": "^19.1.8",
    "@types/react-dom": "^19.1.6",
    "@vitejs/plugin-react": "^4.6.0",
    "eslint": "^9.19.0",
    "eslint-plugin-react-hooks": "^5.1.0",
    "eslint-plugin-react-refresh": "^0.4.18",
    "globals": "^15.14.0",
    "jsdom": "^26.0.0",
    "tailwindcss": "^4.1.3",
    "typescript": "~5.8.3",
    "typescript-eslint": "^8.22.0",
    "vite": "^7.0.4",
    "vitest": "^3.0.5"
  }
}

```

### File: README.md
```md
<div align="center">
  <img src="public/icon.png" width="128" height="128" alt="ForgeTerm Logo" />
  <h1>ForgeTerm</h1>
  <p>A multi-pane terminal workspace built for builders running multiple projects concurrently.</p>
  
  <p>
    <a href="https://github.com/eliophan/ForgeTerm/releases">
      <img src="https://img.shields.io/github/v/release/eliophan/ForgeTerm?display_name=tag&style=for-the-badge" alt="Latest Release" />
    </a>
    <a href="https://github.com/eliophan/ForgeTerm/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
    </a>
    <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey?style=for-the-badge" alt="macOS, Windows, Linux" />
  </p>
</div>

<br />

<div align="center">
  <img src="public/screenshot.png" alt="ForgeTerm Screenshot" />
</div>

## Overview

ForgeTerm is designed to optimize the workflow of developers working on multiple projects at the same time. Instead of losing track of loose terminal windows, it provides a highly customizable, robust environment out of the box.

- **Multi-pane Layout:** Absolute-positioned tiling window manager for horizontal and vertical terminal splits without layout degradation.
- **Fast & Lightweight:** Built on [Tauri](https://tauri.app/) (Rust backend) ensuring minimal memory footprint compared to Electron alternatives.
- **xterm.js Integration:** Reliable rendering, performance, and full terminal compatibility.
- **File Explorer:** Built-in side panel to easily browse and jump between local working directories.

## Installation 

ForgeTerm is currently optimized for macOS (Windows and Linux support via source build).

1. Go to the [Releases page](https://github.com/eliophan/ForgeTerm/releases).
2. Download the latest `.dmg` file (e.g., `ForgeTerm_0.1.0_aarch64.dmg` for Apple Silicon).
3. Open the `.dmg` and drag **ForgeTerm** to your `Applications` folder.

*Note: If macOS blocks the app, go to System Settings → Privacy & Security → Click "Open Anyway".*

---

## Contributing

We welcome contributions. ForgeTerm is built using the Tauri framework, dividing the application into a web frontend and a system-level backend.

### Project Architecture

```text
ForgeTerm/
├── src/                  # FRONTEND (React + TypeScript + Tailwind)
│   ├── App.tsx           # Main application shell and layout manager
│   ├── features/         # Logic slices (Terminal, Explorer, Git, Layout)
│   └── components/       # Reusable UI components
│
├── src-tauri/            # BACKEND (Rust + Tauri)
│   ├── src/main.rs       # App entry point
│   ├── src/pty.rs        # PTY (Pseudo-Terminal) process management
│   └── tauri.conf.json   # OS permissions and window settings
```

### Prerequisites
- [Node.js](https://nodejs.org/) (v20+)
- [pnpm](https://pnpm.io/) (v9+)
- [Rust](https://www.rust-lang.org/tools/install) (Stable)

### Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/eliophan/ForgeTerm.git
   cd ForgeTerm
   ```

2. Install dependencies:
   ```bash
   pnpm install
   ```

3. Run the desktop app in development mode (with Hot-Module Replacement):
   ```bash
   pnpm tauri dev
   ```

### Building from Source

To build production binaries yourself:
```bash
# Compile web frontend
pnpm build

# Compile Desktop app packages (.dmg, .app, .exe, etc)
pnpm tauri build
```

Compiled deliverables will be located in `src-tauri/target/release/bundle/`.

## License

This project is licensed under the [MIT License](LICENSE).

```

### File: AGENTS.md
```md
# Repository Guidelines

## Project Structure & Module Organization
- `src/`: React UI code (app shell, panes, styling).
- `src-tauri/`: Tauri backend (Rust PTY sessions, app config).
- `public/`: Static assets.
- `vite.config.ts`: Vite dev/build configuration.
- `src-tauri/tauri.conf.json`: Tauri app settings.

## Build, Test, and Development Commands
- `pnpm install`: Install dependencies.
- `pnpm dev`: Run the Vite web dev server (UI only).
- `pnpm tauri dev`: Run the full desktop app (UI + Rust backend).
- `pnpm build`: Build the web frontend.
- `pnpm tauri build`: Package the desktop app.

## Coding Style & Naming Conventions
- TypeScript/React in `src/`, Rust in `src-tauri/`.
- Indentation: 2 spaces for TS/TSX, 2 spaces for JSON.
- Prefer descriptive component and file names (e.g., `TerminalPane.tsx`).
- Keep UI state in React; keep PTY/session logic in Rust.

## Testing Guidelines
- No formal test framework is set up yet.
- If adding tests, keep them close to the feature (e.g., `src/__tests__/`).
- Verify manually with `pnpm tauri dev` for terminal behavior.

## Commit & Pull Request Guidelines
- Commit messages are short, imperative, and scoped to one change (e.g., `Add drag-to-resize split panes`).
- Keep commits atomic and focused.
- PRs should include a short summary and note any UX changes or new commands.

## Architecture Overview
- Frontend uses xterm.js for terminal rendering.
- Backend uses Tauri + Rust with `portable-pty` for PTY sessions.
- Split panes are managed in React and render isolated PTY sessions.

## Agent Instructions
- Auto-commit changes when finished.
- Avoid long-running UI work on the main thread (defer PTY spawn and heavy init).

```

### File: components.json
```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "radix-nova",
  "rsc": false,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/styles/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui"
  },
  "iconLibrary": "lucide"
}

```

### File: eslint.config.js
```js
import js from "@eslint/js";
import globals from "globals";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import tseslint from "typescript-eslint";

export default tseslint.config(
  {
    ignores: ["dist", "src-tauri/target", "node_modules"],
  },
  {
    files: ["**/*.{ts,tsx}"],
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    languageOptions: {
      ecmaVersion: 2022,
      globals: {
        ...globals.browser,
        ...globals.node,
      },
    },
    plugins: {
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      "react-refresh/only-export-components": [
        "warn",
        { allowConstantExport: true },
      ],
    },
  },
);

```

### File: index.html
```html
<!doctype html>
<html lang="en" class="dark">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ForgeTerm</title>
  </head>

  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

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
      '@radix-ui/react-slot':
        specifier: ^1.1.0
        version: 1.2.4(@types/react@19.2.14)(react@19.2.4)
      '@tauri-apps/api':
        specifier: ^2
        version: 2.10.1
      '@tauri-apps/plugin-opener':
        specifier: ^2
        version: 2.5.3
      '@xterm/addon-fit':
        specifier: ^0.11.0
        version: 0.11.0
      '@xterm/addon-unicode11':
        specifier: ^0.9.0
        version: 0.9.0
      '@xterm/xterm':
        specifier: ^5.5.0
        version: 5.5.0
      class-variance-authority:
        specifier: ^0.7.1
        version: 0.7.1
      clsx:
        specifier: ^2.1.1
        version: 2.1.1
      lucide-react:
        specifier: ^0.468.0
        version: 0.468.0(react@19.2.4)
      react:
        specifier: ^19.1.0
        version: 19.2.4
      react-dom:
        specifier: ^19.1.0
        version: 19.2.4(react@19.2.4)
      react-resizable-panels:
        specifier: ^2.1.7
        version: 2.1.9(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      shadcn:
        specifier: ^2.0.0
        version: 2.10.0(@types/node@22.19.11)(typescript@5.8.3)
      tailwind-merge:
        specifier: ^2.5.5
        version: 2.6.1
      tw-animate-css:
        specifier: ^1.3.0
        version: 1.4.0
    devDependencies:
      '@eslint/js':
        specifier: ^9.19.0
        version: 9.39.3
      '@tailwindcss/vite':
        specifier: ^4.1.3
        version: 4.2.0(vite@7.3.1(@types/node@22.19.11)(jiti@2.6.1)(lightningcss@1.31.1))
      '@tauri-apps/cli':
        specifier: ^2
        version: 2.10.0
      '@testing-library/jest-dom':
        specifier: ^6.6.3
        version: 6.9.1
      '@testing-library/react':
        specifier: ^16.1.0
        version: 16.3.2(@testing-library/dom@10.4.1)(@types/react-dom@19.2.3(@types/react@19.2.14))(@types/react@19.2.14)(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      '@types/node':
        specifier: ^22.13.4
        version: 22.19.11
      '@types/react':
        specifier: ^19.1.8
        version: 19.2.14
      '@types/react-dom':
        specifier: ^19.1.6
        version: 19.2.3(@types/react@19.2.14)
      '@vitejs/plugin-react':
        specifier: ^4.6.0
        version: 4.7.0(vite@7.3.1(@types/node@22.19.11)(jiti@2.6.1)(lightningcss@1.31.1))
      eslint:
        specifier: ^9.19.0
        version: 9.39.3(jiti@2.6.1)
      eslint-plugin-react-hooks:
        specifier: ^5.1.0
        version: 5.2.0(eslint@9.39.3(jiti@2.6.1))
      eslint-plugin-react-refresh:
        specifier: ^0.4.18
        version: 0.4.26(eslint@9.39.3(jiti@2.6.1))
      globals:
        specifier: ^15.14.0
        version: 15.15.0
      jsdom:
        specifier: ^26.0.0
        version: 26.1.0
      tailwindcss:
        specifier: ^4.1.3
        version: 4.2.0
      typescript:
        specifier: ~5.8.3
        version: 5.8.3
      typescript-eslint:
        specifier: ^8.22.0
        version: 8.56.1(eslint@9.39.3(jiti@2.6.1))(typescript@5.8.3)
      vite:
        specifier: ^7.0.4
        version: 7.3.1(@types/node@22.19.11)(jiti@2.6.1)(lightningcss@1.31.1)
      vitest:
        specifier: ^3.0.5
        version: 3.2.4(@types/node@22.19.11)(jiti@2.6.1)(jsdom@26.1.0)(lightningcss@1.31.1)(msw@2.12.10(@types/node@22.19.11)(typescript@5.8.3))

packages:

  '@adobe/css-tools@4.4.4':
    resolution: {integrity: sha512-Elp+iwUx5rN5+Y8xLt5/GRoG20WGoDCQ/1Fb+1LiGtvwbDavuSk0jhD/eZdckHAuzcDzccnkv+rEjyWfRx18gg==}

  '@antfu/ni@23.3.1':
    resolution: {integrity: sha512-C90iyzm/jLV7Lomv2UzwWUzRv9WZr1oRsFRKsX5HjQL4EXrbi9H/RtBkjCP+NF+ABZXUKpAa4F1dkoTaea4zHg==}
    hasBin: true

  '@asamuzakjp/css-color@3.2.0':
    resolution: {integrity: sha512-K1A6z8tS3XsmCMM86xoWdn7Fkdn9m6RSVtocUrJYIwZnFVkng/PvkEoWtOWmP+Scc6saYWHWZYbndEEXxl24jw==}

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

  '@babel/helper-annotate-as-pure@7.27.3':
    resolution: {integrity: sha512-fXSwMQqitTGeHLBC08Eq5yXz2m37E4pJX1qAU1+2cNedz/ifv/bVXft90VeSav5nFO61EcNgwr0aJxbyPaWBPg==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-compilation-targets@7.28.6':
    resolution: {integrity: sha512-JYtls3hqi15fcx5GaSNL7SCTJ2MNmjrkHXg4FSpOA/grxK8KwyZ5bubHsCq8FXCkua6xhuaaBit+3b7+VZRfcA==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-create-class-features-plugin@7.28.6':
    resolution: {integrity: sha512-dTOdvsjnG3xNT9Y0AUg1wAl38y+4Rl4sf9caSQZOXdNqVn+H+HbbJ4IyyHaIqNR6SW9oJpA/RuRjsjCw2IdIow==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0

  '@babel/helper-globals@7.28.0':
    resolution: {integrity: sha512-+W6cISkXFa1jXsDEdYA8HeevQT/FULhxzR99pxphltZcVaugps53THCeiWA8SguxxpSp3gKPiuYfSWopkLQ4hw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-member-expression-to-functions@7.28.5':
    resolution: {integrity: sha512-cwM7SBRZcPCLgl8a7cY0soT1SptSzAlMH39vwiRpOQkJlh53r5hdHwLSCZpQdVLT39sZt+CRpNwYG4Y2v77atg==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-imports@7.28.6':
    resolution: {integrity: sha512-l5XkZK7r7wa9LucGw9LwZyyCUscb4x37JWTPz7swwFE/0FMQAGpiWUZn8u9DzkSBWEcK25jmvubfpw2dnAMdbw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-module-transforms@7.28.6':
    resolution: {integrity: sha512-67oXFAYr2cDLDVGLXTEABjdBJZ6drElUSI7WKp70NrpyISso3plG9SAGEF6y7zbha/wOzUByWWTJvEDVNIUGcA==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0

  '@babel/helper-optimise-call-expression@7.27.1':
    resolution: {integrity: sha512-URMGH08NzYFhubNSGJrpUEphGKQwMQYBySzat5cAByY1/YgIRkULnIy3tAMeszlL/so2HbeilYloUmSpd7GdVw==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-plugin-utils@7.28.6':
    resolution: {integrity: sha512-S9gzZ/bz83GRysI7gAD4wPT/AI3uCnY+9xn+Mx/KPs2JwHJIz1W8PZkg2cqyt3RNOBM8ejcXhV6y8Og7ly/Dug==}
    engines: {node: '>=6.9.0'}

  '@babel/helper-replace-supers@7.28.6':
    resolution: {integrity: sha512-mq8e+laIk94/yFec3DxSjCRD2Z0TAjhVbEJY3UQrlwVo15Lmt7C2wAUbK4bjnTs4APkwsYLTahXRraQXhb1WCg==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0

  '@babel/helper-skip-transparent-expression-wrappers@7.27.1':
    resolution: {integrity: sha512-Tub4ZKEXqbPjXgWLl2+3JpQAYBJ8+ikpQ2Ocj/q/r0LwE3UhENh7EUabyHjz2kCEsrRY83ew2DQdHluuiDQFzg==}
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

  '@babel/plugin-syntax-typescript@7.28.6':
    resolution: {integrity: sha512-+nDNmQye7nlnuuHDboPbGm00Vqg3oO8niRRL27/4LYHUsHYh0zJ1xWOz0uRwNFmM1Avzk8wZbc6rdiYhomzv/A==}
    engines: {node: '>=6.9.0'}
    peerDependencies:
      '@babel/core': ^7.0.0-0

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

  '@babel/plugin-transform-typescript@7.28.6':
    resolution: {integrity: sha512-0YWL2RFxOqEm9Efk5PvreamxPME8OyY0wM5wh5lHjF+VtVhdneCWGzZeSqzOfiobVqQaNCd2z0tQvnI9DaPWPw==}
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

  '@csstools/color-helpers@5.1.0':
    resolution: {integrity: sha512-S11EXWJyy0Mz5SYvRmY8nJYTFFd1LCNV+7cXyAgQtOOuzb4EsgfqDufL+9esx72/eLhsRdGZwaldu/h+E4t4BA==}
    engines: {node: '>=18'}

  '@csstools/css-calc@2.1.4':
    resolution: {integrity: sha512-3N8oaj+0juUw/1H3YwmDDJXCgTB1gKU6Hc/bB502u9zR0q2vd786XJH9QfrKIEgFlZmhZiq6epXl4rHqhzsIgQ==}
    engines: {node: '>=18'}
    peerDependencies:
      '@csstools/css-parser-algorithms': ^3.0.5
      '@csstools/css-tokenizer': ^3.0.4

  '@csstools/css-color-parser@3.1.0':
    resolution: {integrity: sha512-nbtKwh3a6xNVIp/VRuXV64yTKnb1IjTAEEh3irzS+HkKjAOYLTGNb9pmVNntZ8iVBHcWDA2Dof0QtPgFI1BaTA==}
    engines: {node: '>=18'}
    peerDependencies:
      '@csstools/css-parser-algorithms': ^3.0.5
      '@csstools/css-tokenizer': ^3.0.4

  '@csstools/css-parser-algorithms@3.0.5':
    resolution: {integrity: sha512-DaDeUkXZKjdGhgYaHNJTV9pV7Y9B3b644jCLs9Upc3VeNGg6LWARAT6O+Q+/COo+2gg/bM5rhpMAtf70WqfBdQ==}
    engines: {node: '>=18'}
    peerDependencies:
      '@csstools/css-tokenizer': ^3.0.4

  '@csstools/css-tokenizer@3.0.4':
    resolution: {integrity: sha512-Vd/9EVDiu6PPJt9yAh6roZP6El1xHrdvIVGjyBsHR0RYwNHgL7FJPyIIW4fANJNG6FtyZfvlRPpFI4ZM/lubvw==}
    engines: {node: '>=18'}

  '@esbuild/aix-ppc64@0.27.3':
    resolution: {integrity: sha512-9fJMTNFTWZMh5qwrBItuziu834eOCUcEqymSH7pY+zoMVEZg3gcPuBNxH1EvfVYe9h0x/Ptw8KBzv7qxb7l8dg==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [aix]

  '@esbuild/android-arm64@0.27.3':
    resolution: {integrity: sha512-YdghPYUmj/FX2SYKJ0OZxf+iaKgMsKHVPF1MAq/P8WirnSpCStzKJFjOjzsW0QQ7oIAiccHdcqjbHmJxRb/dmg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [android]

  '@esbuild/android-arm@0.27.3':
    resolution: {integrity: sha512-i5D1hPY7GIQmXlXhs2w8AWHhenb00+GxjxRncS2ZM7YNVGNfaMxgzSGuO8o8SJzRc/oZwU2bcScvVERk03QhzA==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [android]

  '@esbuild/android-x64@0.27.3':
    resolution: {integrity: sha512-IN/0BNTkHtk8lkOM8JWAYFg4ORxBkZQf9zXiEOfERX/CzxW3Vg1ewAhU7QSWQpVIzTW+b8Xy+lGzdYXV6UZObQ==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [android]

  '@esbuild/darwin-arm64@0.27.3':
    resolution: {integrity: sha512-Re491k7ByTVRy0t3EKWajdLIr0gz2kKKfzafkth4Q8A5n1xTHrkqZgLLjFEHVD+AXdUGgQMq+Godfq45mGpCKg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [darwin]

  '@esbuild/darwin-x64@0.27.3':
    resolution: {integrity: sha512-vHk/hA7/1AckjGzRqi6wbo+jaShzRowYip6rt6q7VYEDX4LEy1pZfDpdxCBnGtl+A5zq8iXDcyuxwtv3hNtHFg==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [darwin]

  '@esbuild/freebsd-arm64@0.27.3':
    resolution: {integrity: sha512-ipTYM2fjt3kQAYOvo6vcxJx3nBYAzPjgTCk7QEgZG8AUO3ydUhvelmhrbOheMnGOlaSFUoHXB6un+A7q4ygY9w==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [freebsd]

  '@esbuild/freebsd-x64@0.27.3':
    resolution: {integrity: sha512-dDk0X87T7mI6U3K9VjWtHOXqwAMJBNN2r7bejDsc+j03SEjtD9HrOl8gVFByeM0aJksoUuUVU9TBaZa2rgj0oA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [freebsd]

  '@esbuild/linux-arm64@0.27.3':
    resolution: {integrity: sha512-sZOuFz/xWnZ4KH3YfFrKCf1WyPZHakVzTiqji3WDc0BCl2kBwiJLCXpzLzUBLgmp4veFZdvN5ChW4Eq/8Fc2Fg==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [linux]

  '@esbuild/linux-arm@0.27.3':
    resolution: {integrity: sha512-s6nPv2QkSupJwLYyfS+gwdirm0ukyTFNl3KTgZEAiJDd+iHZcbTPPcWCcRYH+WlNbwChgH2QkE9NSlNrMT8Gfw==}
    engines: {node: '>=18'}
    cpu: [arm]
    os: [linux]

  '@esbuild/linux-ia32@0.27.3':
    resolution: {integrity: sha512-yGlQYjdxtLdh0a3jHjuwOrxQjOZYD/C9PfdbgJJF3TIZWnm/tMd/RcNiLngiu4iwcBAOezdnSLAwQDPqTmtTYg==}
    engines: {node: '>=18'}
    cpu: [ia32]
    os: [linux]

  '@esbuild/linux-loong64@0.27.3':
    resolution: {integrity: sha512-WO60Sn8ly3gtzhyjATDgieJNet/KqsDlX5nRC5Y3oTFcS1l0KWba+SEa9Ja1GfDqSF1z6hif/SkpQJbL63cgOA==}
    engines: {node: '>=18'}
    cpu: [loong64]
    os: [linux]

  '@esbuild/linux-mips64el@0.27.3':
    resolution: {integrity: sha512-APsymYA6sGcZ4pD6k+UxbDjOFSvPWyZhjaiPyl/f79xKxwTnrn5QUnXR5prvetuaSMsb4jgeHewIDCIWljrSxw==}
    engines: {node: '>=18'}
    cpu: [mips64el]
    os: [linux]

  '@esbuild/linux-ppc64@0.27.3':
    resolution: {integrity: sha512-eizBnTeBefojtDb9nSh4vvVQ3V9Qf9Df01PfawPcRzJH4gFSgrObw+LveUyDoKU3kxi5+9RJTCWlj4FjYXVPEA==}
    engines: {node: '>=18'}
    cpu: [ppc64]
    os: [linux]

  '@esbuild/linux-riscv64@0.27.3':
    resolution: {integrity: sha512-3Emwh0r5wmfm3ssTWRQSyVhbOHvqegUDRd0WhmXKX2mkHJe1SFCMJhagUleMq+Uci34wLSipf8Lagt4LlpRFWQ==}
    engines: {node: '>=18'}
    cpu: [riscv64]
    os: [linux]

  '@esbuild/linux-s390x@0.27.3':
    resolution: {integrity: sha512-pBHUx9LzXWBc7MFIEEL0yD/ZVtNgLytvx60gES28GcWMqil8ElCYR4kvbV2BDqsHOvVDRrOxGySBM9Fcv744hw==}
    engines: {node: '>=18'}
    cpu: [s390x]
    os: [linux]

  '@esbuild/linux-x64@0.27.3':
    resolution: {integrity: sha512-Czi8yzXUWIQYAtL/2y6vogER8pvcsOsk5cpwL4Gk5nJqH5UZiVByIY8Eorm5R13gq+DQKYg0+JyQoytLQas4dA==}
    engines: {node: '>=18'}
    cpu: [x64]
    os: [linux]

  '@esbuild/netbsd-arm64@0.27.3':
    resolution: {integrity: sha512-sDpk0RgmTCR/5HguIZa9n9u+HVKf40fbEUt+iTzSnCaGvY9kFP0YKBWZtJaraonFnqef5SlJ8/TiPAxzyS+UoA==}
    engines: {node: '>=18'}
    cpu: [arm64]
    os: [netbsd]

  '@esbuild/netbsd-x64@0.27.3':
    resolution: {inte
... [TRUNCATED]
```

### File: pnpm-workspace.yaml
```yaml
packages:
  - "."
ignoredBuiltDependencies:
  - esbuild

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,

    /* Bundler mode */
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    },

    /* Linting */
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true
  },
  "include": ["src"],
  "exclude": ["src/**/*.test.ts", "src/**/*.test.tsx", "src/test/**"],
  "references": [{ "path": "./tsconfig.node.json" }]
}

```

### File: tsconfig.node.json
```json
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true,
    "types": ["node"]
  },
  "include": ["vite.config.ts"]
}

```

### File: vite.config.ts
```ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { fileURLToPath, URL } from "node:url";

// @ts-expect-error process is a nodejs global
const host = process.env.TAURI_DEV_HOST;

// https://vite.dev/config/
export default defineConfig(async () => ({
  plugins: [tailwindcss(), react()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },

  // Vite options tailored for Tauri development and only applied in `tauri dev` or `tauri build`
  //
  // 1. prevent Vite from obscuring rust errors
  clearScreen: false,
  // 2. tauri expects a fixed port, fail if that port is not available
  server: {
    port: 1421,
    strictPort: true,
    host: host || false,
    hmr: host
      ? {
          protocol: "ws",
          host,
          port: 1422,
        }
      : undefined,
    watch: {
      // 3. tell Vite to ignore watching `src-tauri`
      ignored: ["**/src-tauri/**"],
    },
  },
}));

```

### File: vitest.config.ts
```ts
import { defineConfig } from "vitest/config";
import { fileURLToPath, URL } from "node:url";

export default defineConfig({
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  test: {
    environment: "jsdom",
    setupFiles: "./src/test/setup.ts",
    include: ["src/**/*.test.{ts,tsx}"],
    coverage: {
      enabled: false,
    },
  },
});

```

### File: src\App.css
```css
:root {
  color-scheme: dark;
  font-family: "SF Pro Text", "SF Pro Display", -apple-system, "Segoe UI", sans-serif;
  background-color: #1e1e1e;
  color: #e5e5e5;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  --topbar-height: 48px;
  --traffic-light-gap: 72px;
  --topbar-horizontal-padding: 15px;
  --drag-strip-width: 240px;
  --surface-0: #1e1e1e;
  --surface-1: #2b2b2e;
  --surface-2: #242428;
  --surface-3: #242428;
  --tabs: #2a2a2d;
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-strong: rgba(255, 255, 255, 0.12);
  --terminal-divider: rgba(255, 255, 255, 0.2);
  --terminal-border-width: 0.555556px;
  --terminal-divider-inset: 16px;
  --text-primary: #e5e5e5;
  --text-muted: rgba(229, 229, 229, 0.6);
  --accent: #0a84ff;
  --accent-strong: #0a84ff;
  --accent-soft: rgba(10, 132, 255, 0.2);
  --shadow-panel: 0 6px 14px rgba(0, 0, 0, 0.28);
}

* {
  box-sizing: border-box;
}

html,
body,
#root {
  height: 100%;
  margin: 0;
}

.app {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: var(--surface-0);
}

.topbar {
  display: flex;
  align-items: center;
  min-height: var(--topbar-height);
  padding: 8px var(--topbar-horizontal-padding);
  border-bottom: none;
  background: var(--surface-0);
  position: relative;
}

.topbar-traffic-gap {
  width: 0;
  height: 100%;
  flex: 0 0 0;
}

.topbar-controls {
  display: inline-flex;
  align-items: center;
  gap: 10px;
}

html[data-platform="darwin"] .topbar {
  padding-left: var(--topbar-horizontal-padding);
}

html[data-platform="darwin"] .topbar-traffic-gap {
  width: var(--traffic-light-gap);
  flex-basis: var(--traffic-light-gap);
}

.topbar-drag-strip {
  flex: 1 1 var(--drag-strip-width);
  min-width: var(--drag-strip-width);
  height: 100%;
}

.terminal-shell {
  flex: 1;
  padding: 0;
  display: flex;
  min-height: 0;
}

.file-explorer {
  width: 260px;
  flex: 0 0 260px;
  display: flex;
  flex-direction: column;
  background: var(--surface-0);
  border-right: none;
  border-radius: 0;
  margin: 0;
  overflow: hidden;
  backdrop-filter: none;
  min-width: 200px;
  max-width: 320px;
}

.file-explorer__header {
  padding: 14px 14px 10px;
  border-bottom: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
  background: var(--surface-0);
  backdrop-filter: none;
}

.file-explorer__header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.file-explorer__title {
  font-size: 11px;
  letter-spacing: 0.02em;
  color: var(--text-muted);
}

.file-explorer__close {
  appearance: none;
  border: none;
  background: transparent;
  color: var(--text-muted);
  width: 22px;
  height: 20px;
  border-radius: 0;
  cursor: pointer;
  line-height: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: color 0.12s ease;
}

.file-explorer__close:hover {
  color: var(--text-primary);
}

.file-explorer__cwd {
  font-size: 12px;
  color: var(--text-primary);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.file-explorer__body {
  flex: 1;
  overflow: auto;
  padding: 8px 6px 12px;
}


.explorer-item {
  display: block;
}

.explorer-row {
  width: 100%;
  appearance: none;
  border: none;
  background: none;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 4px 6px;
  cursor: pointer;
  text-align: left;
  font-size: 12px;
  line-height: 1.4;
}

.explorer-name {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.explorer-row:hover {
  background: none;
}

.explorer-row--file {
  cursor: default;
}

.explorer-row--file:hover {
  background: none;
}

.explorer-caret {
  width: 12px;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  color: rgba(242, 242, 242, 0.6);
}

.explorer-caret .icon {
  transition: transform 0.12s ease;
}

.explorer-caret--open .icon {
  transform: rotate(90deg);
}

.explorer-caret--hidden {
  opacity: 0;
}

.explorer-icon {
  display: none;
  width: 10px;
  height: 10px;
  flex: 0 0 10px;
}

.explorer-icon--dir {}

.explorer-icon--file {}

.explorer-children {
  display: block;
}

.explorer-loading,
.explorer-empty,
.explorer-empty-state,
.explorer-error {
  font-size: 12px;
  color: var(--text-muted);
  padding: 6px 10px;
}

.explorer-error {
  color: rgba(255, 130, 130, 0.9);
}

.source-control {
  width: 260px;
  flex: 0 0 260px;
  display: flex;
  flex-direction: column;
  background: var(--surface-0);
  border-left: none;
  border-radius: 0;
  margin: 0;
  overflow: hidden;
  backdrop-filter: none;
  min-width: 200px;
  max-width: 320px;
}

.source-control__header {
  padding: 14px 14px 10px;
  border-bottom: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
  background: var(--surface-0);
  backdrop-filter: none;
}

.source-control__header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
}

.source-control__title {
  font-size: 11px;
  letter-spacing: 0.02em;
  color: var(--text-muted);
}

.source-control__header-actions {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.source-control__menu {
  position: relative;
}

.source-control__menu-button {
  appearance: none;
  border: none;
  background: transparent;
  color: var(--text-muted);
  padding: 2px 8px;
  height: 20px;
  border-radius: 0;
  cursor: pointer;
  font-size: 11px;
  gap: 6px;
  display: inline-flex;
  align-items: center;
}

.source-control__menu-list {
  position: absolute;
  right: 0;
  top: calc(100% + 6px);
  min-width: 120px;
  padding: 6px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  background: var(--surface-0);
  border: none;
  border-radius: 0;
  box-shadow: none;
  z-index: 12;
}

.source-control__menu-item {
  appearance: none;
  border: none;
  background: transparent;
  color: var(--text-primary);
  font-size: 12px;
  text-align: left;
  padding: 6px 8px;
  cursor: pointer;
}

.source-control__menu-item:hover {
  background: none;
}

.source-control__close,
.source-control__refresh {
  appearance: none;
  border: none;
  background: transparent;
  color: var(--text-muted);
  width: 22px;
  height: 20px;
  border-radius: 0;
  cursor: pointer;
  line-height: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
}

.source-control__close:hover,
.source-control__refresh:hover {
  background: none;
  color: var(--text-primary);
}

.source-control__loading,
.source-control__error {
  font-size: 11px;
}

.source-control__error {
  color: rgba(255, 140, 140, 0.9);
}

.source-control__body {
  flex: 1;
  padding: 12px 14px 16px;
  overflow: auto;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.source-control__empty {
  font-size: 12px;
  color: var(--text-muted);
}

.sc-text {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.sc-line {
  font-size: 12px;
  color: var(--text-primary);
}

.sc-line--muted {
  color: var(--text-muted);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.sc-list {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.sc-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
  color: var(--text-primary);
}

.sc-status {
  min-width: 16px;
  font-weight: 700;
  text-align: center;
}

.sc-status--added {
  color: #9ecb6b;
}

.sc-status--modified {
  color: #ffd479;
}

.sc-status--deleted {
  color: #ff6b6b;
}

.sc-status--renamed {
  color: var(--text-muted);
}

.sc-status--conflict {
  color: #ffb347;
}

.sc-status--untracked {
  color: #9ecb6b;
}

.sc-path {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pane-root {
  position: relative;
  height: 100%;
  width: 100%;
  min-height: 0;
  flex: 1;
  min-width: 0;
  border-radius: 12px;
  border: var(--terminal-border-width) solid var(--terminal-divider);
  background: var(--surface-0);
  overflow: hidden;
}

.pane-container {
  position: absolute;
  display: flex;
  min-width: 0;
  min-height: 0;
  background: var(--surface-0);
}

.pane-handle {
  z-index: 5;
}

.pane-handle--horizontal {
  cursor: col-resize;
}

.pane-handle--vertical {
  cursor: row-resize;
}

.pane-handle::after {
  content: "";
  position: absolute;
  background: var(--terminal-divider);
  opacity: 0.5;
  transition: opacity 0.15s ease;
}

.pane-handle--horizontal::after {
  top: 0;
  bottom: 0;
  left: 50%;
  width: 1px;
  transform: translateX(-50%);
}

.pane-handle--vertical::after {
  left: 0;
  right: 0;
  top: 50%;
  height: 1px;
  transform: translateY(-50%);
}

.pane-handle:hover::after {
  opacity: 1;
  background: var(--accent-strong, rgba(255, 255, 255, 0.4));
}

.pane-close {
  position: absolute;
  top: 8px;
  right: 8px;
  z-index: 3;
  appearance: none;
  border: none;
  background: transparent;
  color: var(--text-muted);
  font-size: 12px;
  line-height: 1;
  padding: 4px 6px;
  border-radius: 0;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.12s ease, color 0.12s ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

.pane-close:hover {
  color: var(--text-primary);
}

.pane-close:focus-visible,
.pane-container:hover .pane-close,
.pane-container:focus-within .pane-close {
  opacity: 1;
}

.pane-close:disabled {
  opacity: 0.35;
  cursor: not-allowed;
}

.terminal {
  flex: 1;
  height: 100%;
  width: 100%;
  border-radius: 0;
  border: none;
  background: var(--surface-2);
  box-shadow: none;
  overflow: hidden;
  position: relative;
  display: flex;
  flex-direction: column;
  min-height: 0;
}

.terminal-header {
  padding: 6px 10px;
  border-radius: 0;
  border-bottom: none;
  background: var(--surface-3);
  backdrop-filter: none;
  display: flex;
  align-items: center;
  gap: 6px;
  position: relative;
}

.terminal-header::after {
  content: "";
  position: absolute;
  left: var(--terminal-divider-inset);
  right: var(--terminal-divider-inset);
  bottom: 0;
  height: var(--terminal-border-width);
  background: var(--terminal-divider);
}

.terminal-header__title {
  font-size: 12px;
  font-weight: 600;
  color: var(--text-primary);
}

.terminal-header__divider {
  color: rgba(242, 242, 242, 0.35);
  font-size: 10px;
  line-height: 1;
}

.terminal-header__subtitle {
  font-size: 10px;
  color: var(--text-muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.terminal--active {
  box-shadow: none;
}

.terminal--placeholder {
  cursor: pointer;
}

.terminal--placeholder .terminal-placeholder {
  pointer-events: none;
}

.terminal-inner {
  height: 100%;
  width: 100%;
  flex: 1;
  min-height: 0;
  position: relative;
}

.terminal-body {
  position: relative;
  flex: 1;
  min-height: 0;
}

.terminal-drawer {
  height: 0;
  overflow: hidden;
  background: var(--surface-2);
  border-radius: 0;
  border-top: var(--terminal-border-width) solid var(--terminal-divider);
  display: flex;
  flex-direction: column;
  transition: height 0.18s ease;
  pointer-events: none;
  position: relative;
}

.terminal-drawer--open {
  pointer-events: auto;
}

.terminal-drawer__resize {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  cursor: row-resize;
  background: transparent;
}

.terminal-drawer__resize::after {
  content: "";
  position: absolute;
  left: 20%;
  right: 20%;
  top: 2px;
  height: 2px;
  border-radius: 0;
  background: rgba(255, 255, 255, 0.2);
  opacity: 0.6;
  transition: opacity 0.12s ease;
}

.terminal-drawer__resize:hover::after {
  opacity: 1;
}

.terminal-drawer__header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 4px 8px;
  border-radius: 0;
  border-top: none;
  border-bottom: none;
  background: var(--surface-3);
  backdrop-filter: none;
}

.terminal-drawer__title {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-primary);
  white-space: nowrap;
}

.terminal-drawer__path {
  font-size: 10px;
  color: var(--text-muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  flex: 1;
}

.terminal-drawer__close {
  appearance: none;
  border: none;
  background: transparent;
  color: var(--text-muted);
  width: 20px;
  height: 18px;
  border-radius: 0;
  cursor: pointer;
  line-height: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: color 0.12s ease;
}

.terminal-drawer__close:hover {
  color: var(--text-primary);
}

.terminal-drawer__body {
  flex: 1;
  min-height: 0;
  position: relative;
}

.terminal-placeholder {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  font-size: 12px;
  background: var(--surface-2);
  pointer-events: none;
}

.terminal-placeholder--retry {
  pointer-events: auto;
  flex-direction: column;
}

.terminal-placeholder__content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.terminal-retry {
  appearance: none;
  border: 1px solid var(--border);
  background: var(--surface-1);
  color: var(--text-primary);
  font-size: 12px;
  padding: 6px 10px;
  cursor: pointer;
}

.terminal-retry:hover {
  background: var(--surface-0);
}

.terminal-retry:active {
  transform: translateY(1px);
}

.terminal-debug {
  position: absolute;
  top: 8px;
  left: 8px;
  z-index: 3;
  font-size: 11px;
  color: rgba(242, 242, 242, 0.65);
  background: rgba(10, 10, 10, 0.7);
  padding: 4px 6px;
  border-radius: 0;
  pointer-events: none;
}

.icon-button {
  appearance: none;
  border: none;
  background: transparent;
  color: var(--text-muted);
  width: 28px;
  height: 24px;
  border-radius: 0;
  padding: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: color 0.12s ease;
  font-size: 16px;
  line-height: 1;
}

.icon-button:hover {
  color: var(--text-primary);
}

.icon-button--active {
  color: var(--text-primary);
  box-shadow: none;
}

.icon-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.play-button {
  appearance: none;
  border: none;
  background: transparent;
  color: var(--text-muted);
  height: 24px;
  width: 28px;
  border-radius: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: color 0.12s ease;
}

.play-button:hover {
  color: var(--text-primary);
}

.run-dialog__backdrop {
  position: fixed;
  inset: 0;
  background: rgba(8, 10, 14, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 40;
}

.run-dialog {
  width: min(420px, 90vw);
  background: #1b202a;
  border: 1px solid var(--border-strong);
  border-radius: 14px;
  padding: 16px;
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.35);
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.run-dialog__title {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-primary);
}

.run-dialog__body {
  font-size: 12px;
  color: var(--text-muted);
  line-height: 1.5;
}

.run-dialog__input {
  appearance: none;
  bord
... [TRUNCATED]
```

### File: src\vite-env.d.ts
```ts
/// <reference types="vite/client" />

```

### File: src\lib\utils.ts
```ts
import type { ClassValue } from "clsx";
import { clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

```

### File: src\shared\ime.ts
```ts
export type ImeMode = "auto" | "buffered" | "native";

const IME_MODE_KEY = "terminal:ime-mode";

export const getImeMode = (): ImeMode => {
  if (typeof window === "undefined") return "buffered";
  try {
    const stored = window.localStorage.getItem(IME_MODE_KEY);
    if (stored === "auto" || stored === "native" || stored === "buffered") {
      return stored;
    }
    return "buffered";
  } catch {
    return "buffered";
  }
};

export const setImeMode = (mode: ImeMode) => {
  if (typeof window === "undefined") return;
  try {
    window.localStorage.setItem(IME_MODE_KEY, mode);
  } catch {
    // Ignore storage failures (private mode, etc.)
  }
};

```

### File: src\styles\globals.css
```css
@import "tailwindcss";
@import "tw-animate-css";

@custom-variant dark (&:is(.dark *));

:root {
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
  --card: oklch(1 0 0);
  --card-foreground: oklch(0.145 0 0);
  --popover: oklch(1 0 0);
  --popover-foreground: oklch(0.145 0 0);
  --primary: oklch(0.205 0 0);
  --primary-foreground: oklch(0.985 0 0);
  --secondary: oklch(0.97 0 0);
  --secondary-foreground: oklch(0.205 0 0);
  --muted: oklch(0.97 0 0);
  --muted-foreground: oklch(0.556 0 0);
  --accent: oklch(0.97 0 0);
  --accent-foreground: oklch(0.205 0 0);
  --destructive: oklch(0.577 0.245 27.325);
  --destructive-foreground: oklch(1 0 0);
  --border: oklch(0.922 0 0);
  --input: oklch(0.922 0 0);
  --ring: oklch(0.708 0 0);
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
  --chart-3: oklch(0.398 0.07 227.392);
  --chart-4: oklch(0.828 0.189 84.429);
  --chart-5: oklch(0.769 0.188 70.08);
  --radius: 0.625rem;
  --sidebar: oklch(0.985 0 0);
  --sidebar-foreground: oklch(0.145 0 0);
  --sidebar-primary: oklch(0.205 0 0);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.97 0 0);
  --sidebar-accent-foreground: oklch(0.205 0 0);
  --sidebar-border: oklch(0.922 0 0);
  --sidebar-ring: oklch(0.708 0 0);
}

.dark {
  --background: oklch(0.145 0 0);
  --foreground: oklch(0.985 0 0);
  --card: oklch(0.205 0 0);
  --card-foreground: oklch(0.985 0 0);
  --popover: oklch(0.205 0 0);
  --popover-foreground: oklch(0.985 0 0);
  --primary: oklch(0.922 0 0);
  --primary-foreground: oklch(0.205 0 0);
  --secondary: oklch(0.269 0 0);
  --secondary-foreground: oklch(0.985 0 0);
  --muted: oklch(0.269 0 0);
  --muted-foreground: oklch(0.708 0 0);
  --accent: oklch(0.269 0 0);
  --accent-foreground: oklch(0.985 0 0);
  --destructive: oklch(0.704 0.191 22.216);
  --destructive-foreground: oklch(0.985 0 0);
  --border: oklch(1 0 0 / 10%);
  --input: oklch(1 0 0 / 15%);
  --ring: oklch(0.556 0 0);
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
  --chart-3: oklch(0.769 0.188 70.08);
  --chart-4: oklch(0.627 0.265 303.9);
  --chart-5: oklch(0.645 0.246 16.439);
  --sidebar: oklch(0.205 0 0);
  --sidebar-foreground: oklch(0.985 0 0);
  --sidebar-primary: oklch(0.488 0.243 264.376);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.269 0 0);
  --sidebar-accent-foreground: oklch(0.985 0 0);
  --sidebar-border: oklch(1 0 0 / 10%);
  --sidebar-ring: oklch(0.556 0 0);
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --color-card: var(--card);
  --color-card-foreground: var(--card-foreground);
  --color-popover: var(--popover);
  --color-popover-foreground: var(--popover-foreground);
  --color-primary: var(--primary);
  --color-primary-foreground: var(--primary-foreground);
  --color-secondary: var(--secondary);
  --color-secondary-foreground: var(--secondary-foreground);
  --color-muted: var(--muted);
  --color-muted-foreground: var(--muted-foreground);
  --color-accent: var(--accent);
  --color-accent-foreground: var(--accent-foreground);
  --color-destructive: var(--destructive);
  --color-destructive-foreground: var(--destructive-foreground);
  --color-border: var(--border);
  --color-input: var(--input);
  --color-ring: var(--ring);
  --color-chart-1: var(--chart-1);
  --color-chart-2: var(--chart-2);
  --color-chart-3: var(--chart-3);
  --color-chart-4: var(--chart-4);
  --color-chart-5: var(--chart-5);
  --radius-sm: calc(var(--radius) - 4px);
  --radius-md: calc(var(--radius) - 2px);
  --radius-lg: var(--radius);
  --radius-xl: calc(var(--radius) + 4px);
  --color-sidebar: var(--sidebar);
  --color-sidebar-foreground: var(--sidebar-foreground);
  --color-sidebar-primary: var(--sidebar-primary);
  --color-sidebar-primary-foreground: var(--sidebar-primary-foreground);
  --color-sidebar-accent: var(--sidebar-accent);
  --color-sidebar-accent-foreground: var(--sidebar-accent-foreground);
  --color-sidebar-border: var(--sidebar-border);
  --color-sidebar-ring: var(--sidebar-ring);
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }

  body {
    @apply bg-background text-foreground;
  }
}

```

### File: src\test\setup.ts
```ts
import "@testing-library/jest-dom/vitest";

```

### File: src\features\git\types.ts
```ts
export type GitFileStatus = {
  path: string;
  status: string;
};

export type GitStatusPayload = {
  root: string;
  branch: string;
  ahead: number;
  behind: number;
  files: GitFileStatus[];
};

export type GitStatusState = {
  loading: boolean;
  error: string | null;
  root: string | null;
  branch: string | null;
  ahead: number;
  behind: number;
  files: GitFileStatus[];
};

export const EMPTY_GIT_STATUS: GitStatusState = {
  loading: false,
  error: null,
  root: null,
  branch: null,
  ahead: 0,
  behind: 0,
  files: [],
};

export const formatGitStatus = (status: string) => {
  const trimmed = status.trim();
  if (trimmed === "??") {
    return { label: "?", className: "untracked" as const };
  }
  const primary = trimmed[0] ?? status[0] ?? "?";
  switch (primary) {
    case "A":
      return { label: "A", className: "added" as const };
    case "M":
      return { label: "M", className: "modified" as const };
    case "D":
      return { label: "D", className: "deleted" as const };
    case "R":
      return { label: "R", className: "renamed" as const };
    case "U":
      return { label: "U", className: "conflict" as const };
    default:
      return { label: primary, className: "modified" as const };
  }
};

```

### File: src\features\terminal\runners.ts
```ts
export type RunnerOption = {
  id: "claude" | "codex" | "opencode";
  label: string;
  command: string;
  badge: string;
};

export const RUNNERS: RunnerOption[] = [
  { id: "claude", label: "Claude Code", command: "claude", badge: "CC" },
  { id: "codex", label: "Codex", command: "codex", badge: "CX" },
  { id: "opencode", label: "OpenCode", command: "opencode", badge: "OC" },
];

```

### File: src\features\terminal\types.ts
```ts
import type { MouseEvent } from "react";
import type { ImeMode } from "@/shared/ime";

export type TerminalPaneActions = {
  focus: () => void;
  sendText: (text: string) => void;
  getSelection: () => string;
  clearSelection: () => void;
  selectAll: () => void;
  paste: (text: string) => void;
  clearBuffer: () => void;
  dispose: () => void;
};

export type TerminalPaneProps = {
  id: string;
  isActive: boolean;
  cwd?: string | null;
  drawerOpen?: boolean;
  drawerHeight?: number;
  imeMode?: ImeMode;
  onResizeDrawer?: (height: number) => void;
  onCloseDrawer?: () => void;
  onFocus: (id: string) => void;
  onBusyState?: (id: string, isBusy: boolean) => void;
  onCwdChange?: (id: string, cwd: string) => void;
  initialCwd?: string | null;
  onContextMenu?: (id: string, event: MouseEvent<HTMLDivElement>) => void;
  onRegisterActions?: (id: string, actions: TerminalPaneActions) => void;
  onUnregisterActions?: (id: string) => void;
};

```

### File: src\shared\api\tauri.ts
```ts
import { invoke } from "@tauri-apps/api/core";
import { listen } from "@tauri-apps/api/event";
import type { ExplorerEntry } from "@/features/explorer/types";
import type { GitStatusPayload } from "@/features/git/types";

export type PtyOutputPayload = {
  session_id: string;
  data: string;
};

export type PtyExitPayload = {
  session_id: string;
  code?: number;
};

export const ptySpawn = (args: {
  cols: number;
  rows: number;
  cwd?: string | null;
}) => invoke<string>("pty_spawn", args);

export const ptyWrite = (sessionId: string, data: string) =>
  invoke("pty_write", { sessionId, data });

export const ptyResize = (sessionId: string, cols: number, rows: number) =>
  invoke("pty_resize", { sessionId, cols, rows });

export const ptyKill = (sessionId: string) => invoke("pty_kill", { sessionId });

export const onPtyOutput = (handler: (payload: PtyOutputPayload) => void) =>
  listen<PtyOutputPayload>("pty-output", (event) => handler(event.payload));

export const onPtyExit = (handler: (payload: PtyExitPayload) => void) =>
  listen<PtyExitPayload>("pty-exit", (event) => handler(event.payload));

export const fsReadDir = (path: string) =>
  invoke<ExplorerEntry[]>("fs_read_dir", { path });

export const gitStatus = (path: string) =>
  invoke<GitStatusPayload>("git_status", { path });

export const gitCommit = (path: string, message: string) =>
  invoke<string>("git_commit", { path, message });

export const gitPush = (path: string) => invoke<string>("git_push", { path });
export const gitPull = (path: string) => invoke<string>("git_pull", { path });
export const openTarget = (path: string, app?: string) =>
  invoke<void>("open_target", { path, app });

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

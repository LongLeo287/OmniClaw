---
id: town
type: knowledge
owner: OA_Triage
---
# town
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "claude-town-app",
  "version": "0.2.0",
  "description": "A pixel art western town where your AI agents live and work. Visual orchestrator for the Claude Agent SDK.",
  "type": "module",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/yazinsai/claude-town"
  },
  "keywords": [
    "claude",
    "agent",
    "sdk",
    "ai",
    "pixel-art",
    "orchestrator",
    "claude-code"
  ],
  "engines": {
    "bun": ">=1.0.0"
  },
  "bin": {
    "claude-town": "bin/claude-town.mjs"
  },
  "files": [
    "bin/",
    "server/",
    "shared/",
    "dist/",
    "README.md"
  ],
  "scripts": {
    "dev": "concurrently -k -n server,vite -c blue,green \"bun run dev:server\" \"bun run dev:vite\"",
    "dev:expose": "TOWN_PASSWORD=$(openssl rand -hex 8) concurrently -k -n server,vite,tunnel -c blue,green,yellow \"bun run dev:server\" \"bun run dev:vite\" \"bun scripts/tunnel.ts\"",
    "dev:server": "bun --hot server/index.ts",
    "dev:vite": "vite",
    "build": "vite build",
    "start": "NODE_ENV=production bun server/index.ts",
    "prepublishOnly": "vite build"
  },
  "dependencies": {
    "@anthropic-ai/claude-agent-sdk": "latest",
    "hono": "^4.7.0",
    "qrcode": "^1.5.4",
    "react-markdown": "^10.1.0",
    "uuid": "^11.1.0",
    "zod": "^3.24.0"
  },
  "devDependencies": {
    "@tailwindcss/vite": "^4.0.0",
    "@types/bun": "latest",
    "@types/qrcode": "^1.5.6",
    "@types/react": "^19.0.0",
    "@types/react-dom": "^19.0.0",
    "@types/uuid": "^10.0.0",
    "@vitejs/plugin-react": "^4.3.0",
    "autoprefixer": "^10.4.0",
    "concurrently": "^9.1.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "tailwindcss": "^4.0.0",
    "typescript": "^5.7.0",
    "vite": "^6.0.0"
  }
}

```

### File: README.md
```md
<p align="center">
  <img src="docs/images/hero-banner.png" alt="Claude Town — a pixel art western town for AI agents" width="600" />
</p>

<h3 align="center"><code>~ welcome to claude town, partner ~</code></h3>

<p align="center">
  A pixel art old-western town where your AI agents live, work, and holler when they need you.<br/>
  Built on the <a href="https://docs.anthropic.com/en/docs/agents/claude-agent-sdk">Claude Agent SDK</a>.
</p>

<p align="center">
  <img src="https://img.shields.io/npm/v/claude-town-app?style=flat-square&color=cb3837" />
  <img src="https://img.shields.io/badge/runtime-bun-f472b6?style=flat-square" />
  <img src="https://img.shields.io/badge/frontend-react_19-61dafb?style=flat-square" />
  <img src="https://img.shields.io/badge/agents-claude_sdk-d97706?style=flat-square" />
  <img src="https://img.shields.io/badge/vibe-yeehaw-8B4513?style=flat-square" />
</p>

---

## The idea

You spin up Claude agents. They work on your code. But instead of staring at terminal logs, you watch a little western town come to life.

Each **building** is a project. Each **floor** is an agent. When an agent needs you, a **speech bubble** pops up — click it, answer, and they get right back to work.

<p align="center">
  <img src="docs/images/saloon-building.png" alt="A pixel art saloon with glowing windows and a tiny cowboy" width="280" />
</p>

## Quick start

```bash
npx claude-town-app
```

That's it. Your town opens in the browser, ready for business.

It scans the current directory for projects, so run it from wherever your repos live. A password is auto-generated and printed to the console on first run.

> **Note:** Claude Town uses your existing [Claude Code](https://docs.anthropic.com/en/docs/claude-code) subscription to run agents. No separate API key needed.

## Requirements

- [Bun](https://bun.sh) — `curl -fsSL https://bun.sh/install | bash`
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) subscription (Max or Team plan)
- Git

## Reading the town

<img align="right" src="docs/images/agent-states.png" alt="Window states: busy, done, waiting" width="220" />

The buildings tell you everything at a glance:

| What you see | What it means |
|---|---|
| Flickering yellow windows | Agent is busy working |
| Boarded-up dark windows | Agent finished the job |
| Pulsing orange glow | Agent is waiting on you |
| Speech bubble floating above | Click me! Agent has a question |

No dashboards. No log-tailing. Just a town you can read like a book.

<br clear="right"/>

## How to use it

**Build something -->** Click **+**, pick a project, choose a building style (saloon, bank, sheriff office...), write a prompt, and watch your agent get to work.

**Check in -->** Windows glow and flicker as agents work. You can feel the activity without opening anything.

**Respond -->** Speech bubble? Click it. Quick-response panel lets you answer and get back to watching the sunset.

**Go deeper -->** Click any building to expand it — full conversation logs, streaming output, spawn more agents on the same project.

**Each agent gets its own git worktree**, so multiple agents can work on the same repo without stepping on each other. When they finish, changes merge back automatically.

## CLI options

| Option | Description | Default |
|---|---|---|
| `--port <number>` | Port to run on | `3000` |
| `--no-open` | Don't auto-open browser | opens browser |
| `--password <string>` | Set town password | auto-generated |
| `--data-dir <path>` | Data directory | `~/.claude-town` |

```bash
npx claude-town-app --port 4000 --no-open
```

## What's under the hood

```
Frontend (React 19 + Vite)         Backend (Hono + Bun)
  ├── Pixel art town scene           ├── Claude Agent SDK sessions
  ├── CSS-rendered building sprites  ├── File-based JSON storage
  ├── Day/night cycle + sounds       ├── Git worktree isolation
  ├── Quick-response panels          ├── Auto-merge on completion
  └── WebSocket client               └── WebSocket broadcasts
```

**Real-time** — WebSocket pushes every state change, message, and event to all connected clients. No polling.

**Resumable** — Send feedback to a completed agent and it picks back up with full conversation context via the SDK's `resume` option.

**Isolated** — Each agent works in its own git worktree. No merge conflicts between agents. Changes merge back when the job is done.

## The stack

| Layer | Tech |
|---|---|
| Runtime | [Bun](https://bun.sh) |
| Backend | [Hono](https://hono.dev) |
| Frontend | React 19, Vite, Tailwind CSS v4 |
| Agents | [@anthropic-ai/claude-agent-sdk](https://www.npmjs.com/package/@anthropic-ai/claude-agent-sdk) |
| Font | [Press Start 2P](https://fonts.google.com/specimen/Press+Start+2P) |
| Aesthetic | Pure vibes |

## Building styles

Your agents deserve nice offices. Pick from 8 hand-crafted pixel art buildings:

**Saloon** · **Bank** · **Sheriff Office** · **General Store** · **Hotel** · **Masjid** · **Blacksmith** · **Post Office**

Each one is rendered entirely in CSS. No image sprites. No canvas. Just divs with dreams.

## Development

Want to contribute? Saddle up:

```bash
git clone https://github.com/yazinsai/town.git
cd town
bun install
bun run dev
```

Open **http://localhost:5173** — you're the new sheriff in town.

---

<p align="center">
  <img src="docs/images/desert-footer.png" alt="Sunset over a pixel art desert town" width="500" />
</p>

<p align="center">
  <sub>MIT License — saddle up and make it your own</sub>
</p>

```

### File: index.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Claude Town</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet" />
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>

```

### File: package_lock.json
```json
{
  "name": "claude-town",
  "version": "0.1.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "claude-town",
      "version": "0.1.0",
      "dependencies": {
        "@anthropic-ai/claude-agent-sdk": "latest",
        "hono": "^4.7.0",
        "react-markdown": "^10.1.0",
        "uuid": "^11.1.0",
        "zod": "^3.24.0"
      },
      "devDependencies": {
        "@tailwindcss/vite": "^4.0.0",
        "@types/bun": "latest",
        "@types/react": "^19.0.0",
        "@types/react-dom": "^19.0.0",
        "@types/uuid": "^10.0.0",
        "@vitejs/plugin-react": "^4.3.0",
        "autoprefixer": "^10.4.0",
        "concurrently": "^9.1.0",
        "react": "^19.0.0",
        "react-dom": "^19.0.0",
        "tailwindcss": "^4.0.0",
        "typescript": "^5.7.0",
        "vite": "^6.0.0"
      }
    },
    "node_modules/@anthropic-ai/claude-agent-sdk": {
      "version": "0.2.44",
      "resolved": "https://registry.npmjs.org/@anthropic-ai/claude-agent-sdk/-/claude-agent-sdk-0.2.44.tgz",
      "integrity": "sha512-bryUo6qq5dalO4MmhYLTPonTOAmdSVpMaVLJl8Y0qm6M7G+NZ3WS4cTMGrTbz97Uz5nah+FIOMA4hh8sKLm3YQ==",
      "license": "SEE LICENSE IN README.md",
      "engines": {
        "node": ">=18.0.0"
      },
      "optionalDependencies": {
        "@img/sharp-darwin-arm64": "^0.33.5",
        "@img/sharp-darwin-x64": "^0.33.5",
        "@img/sharp-linux-arm": "^0.33.5",
        "@img/sharp-linux-arm64": "^0.33.5",
        "@img/sharp-linux-x64": "^0.33.5",
        "@img/sharp-linuxmusl-arm64": "^0.33.5",
        "@img/sharp-linuxmusl-x64": "^0.33.5",
        "@img/sharp-win32-x64": "^0.33.5"
      },
      "peerDependencies": {
        "zod": "^4.0.0"
      }
    },
    "node_modules/@babel/code-frame": {
      "version": "7.29.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-validator-identifier": "^7.28.5",
        "js-tokens": "^4.0.0",
        "picocolors": "^1.1.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/compat-data": {
      "version": "7.29.0",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/core": {
      "version": "7.29.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-compilation-targets": "^7.28.6",
        "@babel/helper-module-transforms": "^7.28.6",
        "@babel/helpers": "^7.28.6",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/traverse": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/remapping": "^2.3.5",
        "convert-source-map": "^2.0.0",
        "debug": "^4.1.0",
        "gensync": "^1.0.0-beta.2",
        "json5": "^2.2.3",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/babel"
      }
    },
    "node_modules/@babel/generator": {
      "version": "7.29.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/parser": "^7.29.0",
        "@babel/types": "^7.29.0",
        "@jridgewell/gen-mapping": "^0.3.12",
        "@jridgewell/trace-mapping": "^0.3.28",
        "jsesc": "^3.0.2"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-compilation-targets": {
      "version": "7.28.6",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/compat-data": "^7.28.6",
        "@babel/helper-validator-option": "^7.27.1",
        "browserslist": "^4.24.0",
        "lru-cache": "^5.1.1",
        "semver": "^6.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-globals": {
      "version": "7.28.0",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-imports": {
      "version": "7.28.6",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/traverse": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-module-transforms": {
      "version": "7.28.6",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-module-imports": "^7.28.6",
        "@babel/helper-validator-identifier": "^7.28.5",
        "@babel/traverse": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0"
      }
    },
    "node_modules/@babel/helper-plugin-utils": {
      "version": "7.28.6",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-string-parser": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-identifier": {
      "version": "7.28.5",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helper-validator-option": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/helpers": {
      "version": "7.28.6",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/parser": {
      "version": "7.29.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/types": "^7.29.0"
      },
      "bin": {
        "parser": "bin/babel-parser.js"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-self": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/plugin-transform-react-jsx-source": {
      "version": "7.27.1",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-plugin-utils": "^7.27.1"
      },
      "engines": {
        "node": ">=6.9.0"
      },
      "peerDependencies": {
        "@babel/core": "^7.0.0-0"
      }
    },
    "node_modules/@babel/template": {
      "version": "7.28.6",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.28.6",
        "@babel/parser": "^7.28.6",
        "@babel/types": "^7.28.6"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/traverse": {
      "version": "7.29.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/code-frame": "^7.29.0",
        "@babel/generator": "^7.29.0",
        "@babel/helper-globals": "^7.28.0",
        "@babel/parser": "^7.29.0",
        "@babel/template": "^7.28.6",
        "@babel/types": "^7.29.0",
        "debug": "^4.3.1"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@babel/types": {
      "version": "7.29.0",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@babel/helper-string-parser": "^7.27.1",
        "@babel/helper-validator-identifier": "^7.28.5"
      },
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@esbuild/darwin-arm64": {
      "version": "0.25.12",
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
    "node_modules/@img/sharp-darwin-arm64": {
      "version": "0.33.5",
      "cpu": [
        "arm64"
      ],
      "license": "Apache-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^18.17.0 || ^20.3.0 || >=21.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/libvips"
      },
      "optionalDependencies": {
        "@img/sharp-libvips-darwin-arm64": "1.0.4"
      }
    },
    "node_modules/@img/sharp-darwin-x64": {
      "version": "0.33.5",
      "resolved": "https://registry.npmjs.org/@img/sharp-darwin-x64/-/sharp-darwin-x64-0.33.5.tgz",
      "integrity": "sha512-fyHac4jIc1ANYGRDxtiqelIbdWkIuQaI84Mv45KvGRRxSAa7o7d1ZKAOBaYbnepLC1WqxfpimdeWfvqqSGwR2Q==",
      "cpu": [
        "x64"
      ],
      "license": "Apache-2.0",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": "^18.17.0 || ^20.3.0 || >=21.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/libvips"
      },
      "optionalDependencies": {
        "@img/sharp-libvips-darwin-x64": "1.0.4"
      }
    },
    "node_modules/@img/sharp-libvips-darwin-arm64": {
      "version": "1.0.4",
      "cpu": [
        "arm64"
      ],
      "license": "LGPL-3.0-or-later",
      "optional": true,
      "os": [
        "darwin"
      ],
      "funding": {
        "url": "https://opencollective.com/libvips"
      }
    },
    "node_modules/@img/sharp-libvips-darwin-x64": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/@img/sharp-libvips-darwin-x64/-/sharp-libvips-darwin-x64-1.0.4.tgz",
      "integrity": "sha512-xnGR8YuZYfJGmWPvmlunFaWJsb9T/AO2ykoP3Fz/0X5XV2aoYBPkX6xqCQvUTKKiLddarLaxpzNe+b1hjeWHAQ==",
      "cpu": [
        "x64"
      ],
      "license": "LGPL-3.0-or-later",
      "optional": true,
      "os": [
        "darwin"
      ],
      "funding": {
        "url": "https://opencollective.com/libvips"
      }
    },
    "node_modules/@img/sharp-libvips-linux-arm": {
      "version": "1.0.5",
      "resolved": "https://registry.npmjs.org/@img/sharp-libvips-linux-arm/-/sharp-libvips-linux-arm-1.0.5.tgz",
      "integrity": "sha512-gvcC4ACAOPRNATg/ov8/MnbxFDJqf/pDePbBnuBDcjsI8PssmjoKMAz4LtLaVi+OnSb5FK/yIOamqDwGmXW32g==",
      "cpu": [
        "arm"
      ],
      "license": "LGPL-3.0-or-later",
      "optional": true,
      "os": [
        "linux"
      ],
      "funding": {
        "url": "https://opencollective.com/libvips"
      }
    },
    "node_modules/@img/sharp-libvips-linux-arm64": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/@img/sharp-libvips-linux-arm64/-/sharp-libvips-linux-arm64-1.0.4.tgz",
      "integrity": "sha512-9B+taZ8DlyyqzZQnoeIvDVR/2F4EbMepXMc/NdVbkzsJbzkUjhXv/70GQJ7tdLA4YJgNP25zukcxpX2/SueNrA==",
      "cpu": [
        "arm64"
      ],
      "license": "LGPL-3.0-or-later",
      "optional": true,
      "os": [
        "linux"
      ],
      "funding": {
        "url": "https://opencollective.com/libvips"
      }
    },
    "node_modules/@img/sharp-libvips-linux-x64": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/@img/sharp-libvips-linux-x64/-/sharp-libvips-linux-x64-1.0.4.tgz",
      "integrity": "sha512-MmWmQ3iPFZr0Iev+BAgVMb3ZyC4KeFc3jFxnNbEPas60e1cIfevbtuyf9nDGIzOaW9PdnDciJm+wFFaTlj5xYw==",
      "cpu": [
        "x64"
      ],
      "license": "LGPL-3.0-or-later",
      "optional": true,
      "os": [
        "linux"
      ],
      "funding": {
        "url": "https://opencollective.com/libvips"
      }
    },
    "node_modules/@img/sharp-libvips-linuxmusl-arm64": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/@img/sharp-libvips-linuxmusl-arm64/-/sharp-libvips-linuxmusl-arm64-1.0.4.tgz",
      "integrity": "sha512-9Ti+BbTYDcsbp4wfYib8Ctm1ilkugkA/uscUn6UXK1ldpC1JjiXbLfFZtRlBhjPZ5o1NCLiDbg8fhUPKStHoTA==",
      "cpu": [
        "arm64"
      ],
      "license": "LGPL-3.0-or-later",
      "optional": true,
      "os": [
        "linux"
      ],
      "funding": {
        "url": "https://opencollective.com/libvips"
      }
    },
    "node_modules/@img/sharp-libvips-linuxmusl-x64": {
      "version": "1.0.4",
      "resolved": "https://registry.npmjs.org/@img/sharp-libvips-linuxmusl-x64/-/sharp-libvips-linuxmusl-x64-1.0.4.tgz",
      "integrity": "sha512-viYN1KX9m+/hGkJtvYYp+CCLgnJXwiQB39damAO7WMdKWlIhmYTfHjwSbQeUK/20vY154mwezd9HflVFM1wVSw==",
      "cpu": [
        "x64"
      ],
      "license": "LGPL-3.0-or-later",
      "optional": true,
      "os": [
        "linux"
      ],
      "funding": {
        "url": "https://opencollective.com/libvips"
      }
    },
    "node_modules/@img/sharp-linux-arm": {
      "version": "0.33.5",
      "resolved": "https://registry.npmjs.org/@img/sharp-linux-arm/-/sharp-linux-arm-0.33.5.tgz",
      "integrity": "sha512-JTS1eldqZbJxjvKaAkxhZmBqPRGmxgu+qFKSInv8moZ2AmT5Yib3EQ1c6gp493HvrvV8QgdOXdyaIBrhvFhBMQ==",
      "cpu": [
        "arm"
      ],
      "license": "Apache-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^18.17.0 || ^20.3.0 || >=21.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/libvips"
      },
      "optionalDependencies": {
        "@img/sharp-libvips-linux-arm": "1.0.5"
      }
    },
    "node_modules/@img/sharp-linux-arm64": {
      "version": "0.33.5",
      "resolved": "https://registry.npmjs.org/@img/sharp-linux-arm64/-/sharp-linux-arm64-0.33.5.tgz",
      "integrity": "sha512-JMVv+AMRyGOHtO1RFBiJy/MBsgz0x4AWrT6QoEVVTyh1E39TrCUpTRI7mx9VksGX4awWASxqCYLCV4wBZHAYxA==",
      "cpu": [
        "arm64"
      ],
      "license": "Apache-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^18.17.0 || ^20.3.0 || >=21.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/libvips"
      },
      "optionalDependencies": {
        "@img/sharp-libvips-linux-arm64": "1.0.4"
      }
    },
    "node_modules/@img/sharp-linux-x64": {
      "version": "0.33.5",
      "resolved": "https://registry.npmjs.org/@img/sharp-linux-x64/-/sharp-linux-x64-0.33.5.tgz",
      "integrity": "sha512-opC+Ok5pRNAzuvq1AG0ar+1owsu842/Ab+4qvU879ippJBHvyY5n2mxF1izXqkPYlGuP/M556uh53jRLJmzTWA==",
      "cpu": [
        "x64"
      ],
      "license": "Apache-2.0",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": "^18.17.0 || ^20.3.0 || >=21.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/libvips"
      },
      "optionalDependencies": {
        "@img/sharp-libvips-linux-x64": "1.0.4"
      }
    },
    "node_modules/@img/sharp-linuxmusl-arm64": {
      "version": "0.33.5",
      "resolved": "https://registry.npmjs.org/@img/sharp-linuxmusl-arm64/-/sharp
... [TRUNCATED]
```

### File: SPEC.md
```md
# Claude Town — Spec

A pixel art old-western town that visualizes and orchestrates Claude AI agent sessions across projects. Buildings represent projects, floors represent agent instances, and speech bubbles surface agents waiting for input.

---

## Core Metaphor

| Concept | Visual | Meaning |
|---------|--------|---------|
| Building | Pixel art western building | A project (e.g. `~/ai/projects/my-app`) |
| Floor | Horizontal section of a building | A single Claude agent instance |
| Person on floor | Pixel character working | Agent is busy (actively executing) |
| Speech bubble | Bubble above building | Agent is idle / waiting for user input |
| Building sign | Text on the building | Project name |
| Building style | Saloon, bank, general store, etc. | User-chosen when creating |

Multiple agents on the same project share one building (multi-floor). Each floor shows one agent.

---

## Architecture

### Agent Orchestration

The town app **is** the orchestrator. It uses the **Claude Agent SDK** (TypeScript) to spawn, manage, and communicate with agents. No external Claude Code CLI sessions — everything runs through the SDK.

Each agent gets:
- Full tool access (file read/write, bash, web search)
- Full MCP server access (same as the user's Claude Code setup — GSC, Trigger.dev, Context7, etc.)
- The project directory's `CLAUDE.md` as base system prompt, with optional per-agent overrides/appends
- Permission model: full access by default (restriction capabilities deferred to post-MVP)

### State Detection

Agent states to surface:
| State | Visual | Description |
|-------|--------|-------------|
| **Busy** | Character working, animated | Agent is actively executing tools/thinking |
| **Idle** | Character standing still | Agent finished its turn, waiting for next instruction |
| **Waiting for input** | Speech bubble with `?` | Agent asked a question (AskUserQuestion) |
| **Waiting for permission** | Speech bubble with `!` | Agent needs tool approval |
| **Completed** | Lights off / "closed" sign | Agent finished all work |
| **Error** | Red indicator | Agent crashed or hit an error |

All idle/waiting states show a speech bubble. The bubble icon/color differentiates the type.

### Tech Stack

- **Backend**: Node.js + Express (or Hono) — handles agent lifecycle, WebSocket connections, API
- **Frontend**: React + Vite SPA — pixel art rendering, real-time updates via WebSocket
- **Agent SDK**: `@anthropic-ai/claude-code` (Claude Agent SDK for TypeScript)
- **Rendering**: HTML/CSS sprites — div-based pixel art, CSS animations. Architected so canvas (PixiJS) can replace later if needed
- **Storage**: File-based JSON (`~/.claude-town/` or project-local `data/`)
- **Real-time**: WebSocket for live state updates between server and all connected clients
- **Deployment**: Dokku (domain configured via `TUNNEL_DOMAIN` env var)
- **Auth**: Simple password protection (single shared password, stored as env var)

---

## Features

### 1. Town View (Main Screen)

The primary UI. A pixel art western town landscape showing all active buildings.

- Horizontal scrollable town scene with dirt road, sky, ambient details
- Buildings arranged along the road, sized proportionally to number of agent floors
- Each building shows:
  - Project name on the sign
  - Number of floors = number of agents
  - Visual indicators for each agent's state
  - Speech bubbles floating above when agents need attention
- Clicking a building opens the **Building Detail View**
- Clicking a speech bubble opens the **Quick Response Panel**
- "Build New" button (hammer icon) to create a new building/agent
- Mobile-responsive — usable on phone screens

### 2. Building Detail View

Expanded view when clicking a building.

- Shows all floors/agents for that project
- Each floor displays:
  - Agent name/ID
  - Current state (busy/idle/waiting/done)
  - Brief summary of what the agent is currently doing
  - Expandable full conversation log (streaming)
- Actions:
  - Send a message to any agent on any floor
  - Add a new floor (spawn another agent on this project)
  - Archive/remove the building (user decides when to clean up)
  - Kill an individual agent

### 3. Quick Response Panel

Opened by clicking a speech bubble. Minimal overlay for fast responses.

- Shows the agent's question/prompt
- If Claude asked a multiple-choice question (AskUserQuestion with options): renders **clickable buttons** for each option
- Always shows a **text input box** underneath for freeform responses
- For permission requests: **Approve / Deny** buttons
- Submitting a response sends input directly back to the agent via the SDK
- Panel dismisses after responding, agent resumes work

### 4. New Building Flow

Creating a new agent/project from the town UI.

1. Click "Build New" button
2. **Select or enter project path** (e.g. `~/ai/projects/my-app`) — with autocomplete from `~/ai/projects/`
3. **Choose building style** from a set of pixel art western building sprites (saloon, bank, sheriff office, general store, hotel, etc.)
4. **Write initial prompt** — the task/instruction for the agent
5. **Optional: custom system prompt** — override or append to the project's CLAUDE.md
6. Click "Build" — building appears in town, agent starts working

### 5. Conversation View

Accessible from the Building Detail View by expanding a floor.

- **Summary mode** (default): Brief description of progress, key milestones, current task
- **Full log mode** (expandable): Complete conversation history with:
  - Agent messages (what Claude said/did)
  - Tool calls and results (collapsible)
  - User responses
  - Timestamps
- Streaming updates — new messages appear in real-time

### 6. Mobile Experience

Full control from phone/tablet.

- Responsive pixel art town (horizontal scroll, pinch-to-zoom)
- All features accessible: spawn agents, respond to questions, view logs, manage buildings
- Push notifications (future enhancement) for speech bubble events
- Touch-friendly buttons and inputs

---

## Data Model

### Building (Project)

```json
{
  "id": "uuid",
  "name": "my-app",
  "projectPath": "/Users/rock/ai/projects/my-app",
  "buildingStyle": "saloon",
  "createdAt": "2026-02-17T...",
  "agents": ["agent-uuid-1", "agent-uuid-2"]
}
```

### Agent (Floor)

```json
{
  "id": "uuid",
  "buildingId": "building-uuid",
  "state": "busy | idle | waiting_input | waiting_permission | completed | error",
  "currentTask": "Implementing auth flow",
  "initialPrompt": "Add JWT authentication to the Express API",
  "customSystemPrompt": null,
  "conversationLog": "path/to/conversation.jsonl",
  "createdAt": "2026-02-17T...",
  "completedAt": null
}
```

### Conversation Entry

```json
{
  "timestamp": "2026-02-17T...",
  "role": "assistant | user | tool_call | tool_result | system",
  "content": "...",
  "metadata": {}
}
```

---

## Agent Lifecycle

```
[User creates building]
  → Agent spawned via Claude Agent SDK
  → State: busy
  → Agent works autonomously

[Agent needs input]
  → State: waiting_input / waiting_permission
  → Speech bubble appears on building
  → User clicks bubble, responds
  → Response sent to agent via SDK
  → State: busy (resumes)

[Agent finishes]
  → State: completed
  → Building shows "closed" visual
  → Building persists until user archives it

[Agent errors]
  → State: error
  → Red indicator on building
  → User can view error, retry, or kill
```

---

## Visual Design

### Style
- **Pixel art, old western theme** — 16-bit aesthetic
- Earth tones: dusty browns, warm oranges, muted blues for sky
- Dirt road running horizontally through the town
- Sky with subtle gradient (can add day/night cycle later)

### Building Sprites (HTML/CSS)
- Each building type is a set of CSS-drawn pixel art elements
- Buildings scale vertically with number of floors
- Available styles: Saloon, Bank, Sheriff Office, General Store, Hotel, Blacksmith, Church, Post Office
- Signs rendered as text overlaid on wooden sign sprites

### Animation (MVP — Minimal)
- Speech bubbles: fade in/out with slight bounce
- Busy indicator: small animated dots or spinning gear
- Idle characters: subtle breathing/blinking animation
- Building construction: brief "building" animation when spawning new agent
- Designed for layering richer animations later (tumbleweeds, smoke, people walking)

### Responsive Layout
- Desktop: Full town panorama, buildings side-by-side
- Tablet: Slightly compressed, 2-3 buildings visible at a time
- Phone: 1-2 buildings visible, swipe to scroll, panels slide up from bottom

---

## API Routes

### REST API

| Method | Route | Description |
|--------|-------|-------------|
| POST | `/api/auth` | Authenticate with password |
| GET | `/api/buildings` | List all buildings |
| POST | `/api/buildings` | Create new building + spawn agent |
| GET | `/api/buildings/:id` | Get building details |
| DELETE | `/api/buildings/:id` | Archive/remove building |
| POST | `/api/buildings/:id/agents` | Spawn new agent on building |
| GET | `/api/agents/:id` | Get agent state + summary |
| POST | `/api/agents/:id/respond` | Send input to agent |
| POST | `/api/agents/:id/kill` | Kill agent |
| GET | `/api/agents/:id/conversation` | Get conversation log |
| GET | `/api/projects` | List available project directories |

### WebSocket Events

| Event | Direction | Description |
|-------|-----------|-------------|
| `agent:state` | Server → Client | Agent state changed |
| `agent:message` | Server → Client | New conversation entry |
| `agent:question` | Server → Client | Agent is asking a question |
| `agent:completed` | Server → Client | Agent finished |
| `agent:error` | Server → Client | Agent errored |
| `building:created` | Server → Client | New building appeared |
| `building:removed` | Server → Client | Building archived |

---

## Security

- Password auth via env var `TOWN_PASSWORD`
- Session token (JWT or simple token) after auth, stored in cookie
- WebSocket connections authenticated via token
- Agent file access scoped to specified project directories
- API key for Anthropic stored server-side as env var
- No agent credentials exposed to frontend

---

## File Structure

```
town/
├── package.json
├── tsconfig.json
├── vite.config.ts
├── server/
│   ├── index.ts              # Express/Hono server entry
│   ├── auth.ts               # Password auth middleware
│   ├── routes/
│   │   ├── buildings.ts      # Building CRUD
│   │   ├── agents.ts         # Agent management
│   │   └── projects.ts       # List available projects
│   ├── agents/
│   │   ├── manager.ts        # Agent lifecycle management
│   │   ├── sdk.ts            # Claude Agent SDK integration
│   │   └── state.ts          # State tracking + persistence
│   ├── websocket.ts          # WebSocket server
│   └── storage.ts            # File-based JSON storage
├── src/
│   ├── main.tsx              # React entry
│   ├── App.tsx               # Router + auth wrapper
│   ├── components/
│   │   ├── town/
│   │   │   ├── TownScene.tsx       # Main town panorama
│   │   │   ├── Building.tsx        # Individual building component
│   │   │   ├── SpeechBubble.tsx    # Speech bubble overlay
│   │   │   ├── Road.tsx            # Ground/road element
│   │   │   └── Sky.tsx             # Sky background
│   │   ├── panels/
│   │   │   ├── QuickResponse.tsx   # Speech bubble response panel
│   │   │   ├── BuildingDetail.tsx  # Building expanded view
│   │   │   ├── NewBuilding.tsx     # Create building flow
│   │   │   └── ConversationLog.tsx # Full conversation view
│   │   ├── sprites/
│   │   │   ├── Saloon.tsx          # Building style components
│   │   │   ├── Bank.tsx
│   │   │   ├── SheriffOffice.tsx
│   │   │   ├── GeneralStore.tsx
│   │   │   └── ...
│   │   └── ui/
│   │       ├── PixelButton.tsx
│   │       ├── PixelInput.tsx
│   │       └── PixelText.tsx
│   ├── hooks/
│   │   ├── useWebSocket.ts        # WebSocket connection
│   │   ├── useBuildings.ts        # Building state
│   │   └── useAgent.ts            # Agent state
│   ├── styles/
│   │   ├── pixels.css             # Pixel art base styles
│   │   └── animations.css         # CSS animations
│   └── lib/
│       ├── api.ts                 # REST API client
│       └── types.ts               # Shared TypeScript types
├── data/                          # JSON storage (gitignored)
│   ├── buildings.json
│   └── agents/
│       ├── {agent-id}.json
│       └── {agent-id}.conversation.jsonl
├── Dockerfile                     # For dokku deployment
└── .env                           # ANTHROPIC_API_KEY, TOWN_PASSWORD
```

---

## Deferred (Post-MVP)

- Cost tracking per agent (token usage, estimated dollars)
- Per-agent permission restrictions
- Agent-to-agent communication
- Day/night cycle animation
- Tumbleweeds, smoke, ambient character animations
- Push notifications for mobile
- Ghost town / graveyard for archived buildings
- Budget caps per agent/global
- Canvas rendering upgrade (PixiJS) if HTML/CSS hits limits

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "paths": {
      "@shared/*": ["./shared/*"]
    }
  },
  "include": ["src", "server", "shared"],
  "exclude": ["node_modules", "dist"]
}

```

### File: vite.config.ts
```ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import path from "path";

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@shared": path.resolve(__dirname, "shared"),
    },
  },
  server: {
    port: 5173,
    allowedHosts: true,
    proxy: {
      "/api": {
        target: "http://localhost:3174",
        changeOrigin: true,
      },
      "/ws": {
        target: "ws://localhost:3174",
        ws: true,
      },
    },
  },
  publicDir: "static",
  build: {
    outDir: "dist",
  },
});

```

### File: public\index.html
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Claude Town</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet" />
    <script type="module" crossorigin src="/assets/index-zx6cn-AP.js"></script>
    <link rel="stylesheet" crossorigin href="/assets/index-v8Fr_dkd.css">
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>

```

### File: scripts\tunnel.ts
```ts
#!/usr/bin/env bun
// Exposes local Vite dev server via named Cloudflare tunnel + QR code

import QRCode from "qrcode";

const VITE_PORT = 5173;
const TOWN_PASSWORD = process.env.TOWN_PASSWORD || "claude2024";
const TUNNEL_NAME = process.env.TUNNEL_NAME || "claude-town";
const TUNNEL_DOMAIN = process.env.TUNNEL_DOMAIN;

if (!TUNNEL_DOMAIN) {
  console.error("  ❌ TUNNEL_DOMAIN is not set. Add it to .env (e.g. TUNNEL_DOMAIN=mytown.example.com)");
  process.exit(1);
}

const TUNNEL_URL = `https://${TUNNEL_DOMAIN}`;
const url = `${TUNNEL_URL}?p=${encodeURIComponent(TOWN_PASSWORD)}`;
const qr = await QRCode.toString(url, { type: "terminal", small: true });
console.log("\n" + qr);
console.log(`  📱 Scan to open: ${url}\n`);

const proc = Bun.spawn(
  ["cloudflared", "tunnel", "run", "--url", `http://localhost:${VITE_PORT}`, TUNNEL_NAME],
  { stderr: "pipe", stdout: "inherit" }
);

const reader = proc.stderr.getReader();
const decoder = new TextDecoder();

while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  process.stderr.write(decoder.decode(value, { stream: true }));
}

```

### File: server\auth.ts
```ts
import type { Context, Next } from "hono";
import { getCookie, setCookie } from "hono/cookie";
import { getDeviceToken, createDeviceToken, touchDeviceToken } from "./storage";

const TOWN_PASSWORD = process.env.TOWN_PASSWORD || "claude2024";
const COOKIE_NAME = "town_auth";
const COOKIE_MAX_AGE = 60 * 60 * 24 * 365; // 1 year

export async function authMiddleware(c: Context, next: Next) {
  // Check URL param — first-time login via QR code
  const urlPassword = c.req.query("p");
  if (urlPassword === TOWN_PASSWORD) {
    const device = await createDeviceToken();
    setCookie(c, COOKIE_NAME, device.token, {
      maxAge: COOKIE_MAX_AGE,
      httpOnly: true,
      path: "/",
      sameSite: "Lax",
    });
    await next();
    return;
  }

  // Check cookie — returning device
  const cookie = getCookie(c, COOKIE_NAME);
  if (cookie) {
    const device = getDeviceToken(cookie);
    if (device) {
      touchDeviceToken(cookie);
      await next();
      return;
    }
  }

  // Not authenticated
  const accept = c.req.header("accept") || "";
  const isApi =
    c.req.path.startsWith("/api/") ||
    accept.includes("application/json");

  if (isApi) {
    return c.json({ error: "Unauthorized" }, 401);
  }

  return c.html(loginPage(), 401);
}

function loginPage(): string {
  return `<!DOCTYPE html>
<html>
<head>
  <title>Claude Town - Login</title>
  <style>
    body { font-family: monospace; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #1a1a2e; color: #e0e0e0; }
    .login { text-align: center; padding: 2rem; border: 2px solid #c8a96e; border-radius: 8px; background: #16213e; }
    h1 { color: #c8a96e; }
    input { padding: 0.5rem 1rem; font-family: monospace; font-size: 1rem; border: 1px solid #c8a96e; background: #1a1a2e; color: #e0e0e0; border-radius: 4px; }
    button { padding: 0.5rem 1.5rem; font-family: monospace; font-size: 1rem; background: #c8a96e; color: #1a1a2e; border: none; border-radius: 4px; cursor: pointer; margin-left: 0.5rem; }
    button:hover { background: #d4b87a; }
  </style>
</head>
<body>
  <div class="login">
    <h1>Claude Town</h1>
    <p>Enter the town password</p>
    <form onsubmit="window.location.href='/?p='+document.getElementById('pw').value;return false;">
      <input id="pw" type="password" placeholder="Password" autofocus />
      <button type="submit">Enter</button>
    </form>
  </div>
</body>
</html>`;
}

```

### File: server\banner.ts
```ts
import QRCode from "qrcode";
import { networkInterfaces } from "os";

function getNetworkUrl(port: number): string | null {
  const nets = networkInterfaces();
  for (const name of Object.keys(nets)) {
    for (const net of nets[name] || []) {
      if (net.family === "IPv4" && !net.internal) {
        return `http://${net.address}:${port}`;
      }
    }
  }
  return null;
}

export async function printBanner(port: number, cwd: string) {
  const localUrl = `http://localhost:${port}`;
  const networkUrl = getNetworkUrl(port);
  const qrTarget = networkUrl || localUrl;

  let qr = "";
  try {
    qr = await QRCode.toString(qrTarget, { type: "terminal", small: true });
  } catch {
    // QR generation failed — skip it
  }

  const lines = [
    "",
    "  ╔══════════════════════════════════════╗",
    "  ║        Welcome to Claude Town        ║",
    "  ╚══════════════════════════════════════╝",
    "",
  ];

  if (qr) {
    lines.push(...qr.split("\n").map((l) => "  " + l));
    lines.push("");
    lines.push("  Scan to open on your phone (same Wi-Fi network)");
    lines.push("");
  }

  lines.push(`  Local:   ${localUrl}`);
  if (networkUrl) {
    lines.push(`  Network: ${networkUrl}`);
  }

  lines.push("");
  lines.push("  ── About ──────────────────────────────────");
  lines.push("  Runs entirely on your machine");
  lines.push("  Uses your Claude Code subscription (no API key needed)");
  lines.push(`  Working directory: ${cwd}`);
  lines.push("    Folders inside are accessible to agents");
  lines.push("    You can also use absolute paths in the app");
  lines.push("  Must stay connected to the internet");
  lines.push("  Agents can read your environment variables");
  lines.push("  ───────────────────────────────────────────");
  lines.push("");
  lines.push("  Ctrl+C to stop");
  lines.push("");

  console.log(lines.join("\n"));
}

```

### File: server\caretaker.ts
```ts
import { query } from "@anthropic-ai/claude-agent-sdk";
import type { SDKAssistantMessage, SDKResultMessage } from "@anthropic-ai/claude-agent-sdk";
import { spawn } from "child_process";
import * as storage from "./storage";
import { broadcast } from "./websocket";
import type {
  Agent,
  Building,
  Caretaker,
  ConversationEntry,
  PendingQuestion,
  PendingPermission,
  RespondToAgentRequest,
} from "../shared/types";

// ---------------------------------------------------------------------------
// 1. Building queue — sequential execution per building
// ---------------------------------------------------------------------------

const buildingQueues = new Map<string, Promise<void>>();

function enqueue(buildingId: string, fn: () => Promise<void>): Promise<void> {
  const prev = buildingQueues.get(buildingId) ?? Promise.resolve();
  const next = prev.then(fn, fn); // run even if previous rejected
  buildingQueues.set(buildingId, next);
  // Clean up when the chain settles
  next.finally(() => {
    if (buildingQueues.get(buildingId) === next) {
      buildingQueues.delete(buildingId);
    }
  });
  return next;
}

// ---------------------------------------------------------------------------
// 2. Prompt builder
// ---------------------------------------------------------------------------

interface PromptContext {
  building: Building;
  caretaker: Caretaker;
  agent: Agent;
  question: PendingQuestion | null;
  permission: PendingPermission | null;
  recentConversation: ConversationEntry[];
}

function buildPrompt(ctx: PromptContext): string {
  const lines: string[] = [];

  lines.push(`You are the caretaker for the project "${ctx.building.name}".`);
  lines.push(`Your job is to automatically handle agent questions and permission requests on behalf of the project owner.`);
  lines.push("");

  // Owner instructions
  if (ctx.caretaker.instructions) {
    lines.push("## Owner's Instructions");
    lines.push(ctx.caretaker.instructions);
    lines.push("");
  }

  // Agent info
  lines.push(`## Agent`);
  lines.push(`Task: ${ctx.agent.currentTask || ctx.agent.initialPrompt}`);
  lines.push("");

  // What the agent is asking
  if (ctx.question) {
    lines.push("## Agent Question");
    for (const q of ctx.question.questions) {
      lines.push(`**${q.header || "Question"}**: ${q.question}`);
      if (q.options.length > 0) {
        lines.push("Options:");
        for (const opt of q.options) {
          lines.push(`  - ${opt.label}${opt.description ? `: ${opt.description}` : ""}`);
        }
      }
    }
    lines.push("");
  }

  if (ctx.permission) {
    lines.push("## Permission Request");
    lines.push(`Tool: ${ctx.permission.toolName}`);
    lines.push(`Input: ${JSON.stringify(ctx.permission.input, null, 2)}`);
    lines.push("");
    lines.push("Should this tool use be approved or denied?");
    lines.push("");
  }

  // Recent conversation context
  if (ctx.recentConversation.length > 0) {
    lines.push("## Recent Conversation (last entries for context)");
    for (const entry of ctx.recentConversation) {
      const prefix = entry.role === "assistant" ? "Agent" : entry.role === "user" ? "User" : entry.role;
      lines.push(`[${prefix}]: ${entry.content}`);
    }
    lines.push("");
  }

  // Response instructions
  lines.push("## How to Respond");
  lines.push("Respond with your answer directly. Be concise.");
  if (ctx.question) {
    lines.push("If the question has options, pick the best option label.");
  }
  if (ctx.permission) {
    lines.push('Say "approve" to allow the tool use or "deny" to reject it.');
  }
  lines.push("");
  lines.push("If you are unsure, or the question requires the project owner's personal judgment,");
  lines.push("start your response with [ESCALATE] followed by a brief reason why.");

  return lines.join("\n");
}

// ---------------------------------------------------------------------------
// 3. Response parser
// ---------------------------------------------------------------------------

interface ParsedResponse {
  action: "respond" | "escalate";
  // For questions with answers
  answers?: Record<string, string>;
  // For permissions
  approved?: boolean;
  // Explanation
  reason?: string;
  summary: string;
}

function parseResponse(
  raw: string,
  question: PendingQuestion | null,
  permission: PendingPermission | null
): ParsedResponse {
  const trimmed = raw.trim();

  // Check for escalation
  if (trimmed.startsWith("[ESCALATE]")) {
    const reason = trimmed.replace("[ESCALATE]", "").trim();
    return {
      action: "escalate",
      reason: reason || "Caretaker chose to escalate to owner",
      summary: reason || "Escalated to owner",
    };
  }

  // Permission response
  if (permission) {
    const lower = trimmed.toLowerCase();
    const approved = lower.includes("approve");
    return {
      action: "respond",
      approved,
      reason: trimmed,
      summary: approved ? "Approved" : "Denied",
    };
  }

  // Question response — match option labels
  if (question) {
    const answers: Record<string, string> = {};
    for (const q of question.questions) {
      if (q.options.length > 0) {
        // Try to match an option label in the response
        const matched = q.options.find((opt) =>
          trimmed.toLowerCase().includes(opt.label.toLowerCase())
        );
        answers[q.question] = matched ? matched.label : trimmed;
      } else {
        answers[q.question] = trimmed;
      }
    }
    return {
      action: "respond",
      answers,
      summary: trimmed.length > 100 ? trimmed.slice(0, 100) + "..." : trimmed,
    };
  }

  // Fallback
  return {
    action: "respond",
    summary: trimmed.length > 100 ? trimmed.slice(0, 100) + "..." : trimmed,
  };
}

// ---------------------------------------------------------------------------
// 4. Claude backend
// ---------------------------------------------------------------------------

async function queryClaudeBackend(prompt: string, cwd: string): Promise<string> {
  const q = query({
    prompt,
    options: {
      cwd,
      maxTurns: 1,
      systemPrompt: {
        type: "preset" as const,
        preset: "claude_code" as const,
        append: "You are a caretaker AI. Respond concisely to the question. Do not use tools.",
      },
      permissionMode: "bypassPermissions",
      allowDangerouslySkipPermissions: true,
      tools: { type: "preset", preset: "claude_code" },
      settingSources: ["user", "project"],
    } as any,
  });

  const texts: string[] = [];
  for await (const message of q) {
    if (message.type === "assistant") {
      const assistantMsg = message as SDKAssistantMessage;
      for (const block of assistantMsg.message.content) {
        if (block.type === "text") {
          texts.push(block.text);
        }
      }
    } else if (message.type === "result") {
      const result = message as SDKResultMessage;
      if (result.subtype === "success" && result.result) {
        texts.push(result.result);
      }
    }
  }

  return texts.join("\n").trim();
}

// ---------------------------------------------------------------------------
// 5. Codex backend
// ---------------------------------------------------------------------------

async function queryCodexBackend(prompt: string, cwd: string): Promise<string> {
  return new Promise<string>((resolve, reject) => {
    const child = spawn("codex", ["exec", "--full-auto", prompt], {
      cwd,
      stdio: ["ignore", "pipe", "pipe"],
      env: { ...process.env },
    });

    let stdout = "";
    let stderr = "";

    child.stdout.on("data", (data: Buffer) => {
      stdout += data.toString();
    });

    child.stderr.on("data", (data: Buffer) => {
      stderr += data.toString();
    });

    const timeout = setTimeout(() => {
      child.kill("SIGTERM");
      reject(new Error("Codex timed out after 2 minutes"));
    }, 2 * 60 * 1000);

    child.on("close", (code) => {
      clearTimeout(timeout);
      if (code !== 0) {
        reject(new Error(`Codex exited with code ${code}: ${stderr}`));
        return;
      }

      // Parse stdout — actual response is after the "codex" marker line
      const lines = stdout.split("\n");
      let startIdx = 0;
      for (let i = 0; i < lines.length; i++) {
        if (lines[i].trim().toLowerCase() === "codex") {
          startIdx = i + 1;
          break;
        }
      }

      // Strip the "tokens used" footer
      let endIdx = lines.length;
      for (let i = lines.length - 1; i >= startIdx; i--) {
        if (lines[i].match(/tokens?\s+used/i)) {
          endIdx = i;
          break;
        }
      }

      const response = lines.slice(startIdx, endIdx).join("\n").trim();
      resolve(response || stdout.trim());
    });

    child.on("error", (err) => {
      clearTimeout(timeout);
      reject(err);
    });
  });
}

// ---------------------------------------------------------------------------
// 6. Main handler
// ---------------------------------------------------------------------------

/**
 * Attempts to handle a pending agent question or permission via the building's
 * caretaker. Returns `true` if the caretaker will handle it (asynchronously),
 * `false` if no caretaker is configured/enabled.
 */
export function handleCaretaker(
  agentId: string,
  type: "question" | "permission"
): boolean {
  const agent = storage.getAgent(agentId);
  if (!agent) return false;

  const building = storage.getBuilding(agent.buildingId);
  if (!building) return false;

  const caretaker = building.caretaker;
  if (!caretaker || !caretaker.enabled) return false;

  // Determine working directory
  const cwd = agent.worktreePath || building.projectPath;

  // Fire and forget — the queue handles serialization
  enqueue(building.id, async () => {
    try {
      // Re-fetch agent state — it may have been answered while queued
      const freshAgent = storage.getAgent(agentId);
      if (!freshAgent) return;

      const question = type === "question" ? freshAgent.pendingQuestion : null;
      const permission = type === "permission" ? freshAgent.pendingPermission : null;

      // If the pending state was already cleared (user answered), skip
      if (type === "question" && !question) return;
      if (type === "permission" && !permission) return;

      // Get recent conversation for context
      const conversation = await storage.getConversation(agentId);
      const recentConversation = conversation.slice(-10);

      // Build prompt
      const prompt = buildPrompt({
        building,
        caretaker,
        agent: freshAgent,
        question,
        permission,
        recentConversation,
      });

      // Invoke model
      let responseText: string;
      if (caretaker.model === "codex") {
        responseText = await queryCodexBackend(prompt, cwd);
      } else {
        responseText = await queryClaudeBackend(prompt, cwd);
      }

      // Parse response
      const parsed = parseResponse(responseText, question, permission);

      if (parsed.action === "respond") {
        // Build the respondToAgent request
        const request: RespondToAgentRequest = { type: "answer" };
        if (type === "permission") {
          request.type = "permission";
          request.approved = parsed.approved;
        } else if (parsed.answers) {
          request.type = "answer";
          request.answers = parsed.answers;
        }

        // Dynamic import to avoid circular dependency
        const { respondToAgent } = await import("./agents/manager");
        await respondToAgent(agentId, request, "caretaker");

        broadcast({
          type: "caretaker:responded",
          agentId,
          buildingId: building.id,
          summary: parsed.summary,
        });
      } else {
        // Escalate — leave the speech bubble for the owner
        broadcast({
          type: "caretaker:escalated",
          agentId,
          buildingId: building.id,
          reason: parsed.reason || "Caretaker escalated to owner",
        });

        // Re-broadcast the original event so the speech bubble appears
        const currentAgent = storage.getAgent(agentId);
        if (currentAgent) {
          if (type === "question" && currentAgent.pendingQuestion) {
            broadcast({ type: "agent:question", agentId, question: currentAgent.pendingQuestion });
          } else if (type === "permission" && currentAgent.pendingPermission) {
            broadcast({ type: "agent:permission", agentId, permission: currentAgent.pendingPermission });
          }
        }
      }
    } catch (err: any) {
      // On error, silently escalate — the speech bubble stays for the owner
      console.error(`[caretaker] Error handling ${type} for agent ${agentId}:`, err.message);
      broadcast({
        type: "caretaker:escalated",
        agentId,
        buildingId: building.id,
        reason: `Caretaker error: ${err.message}`,
      });

      // Re-broadcast the original event so the speech bubble appears
      const errorAgent = storage.getAgent(agentId);
      if (errorAgent) {
        if (type === "question" && errorAgent.pendingQuestion) {
          broadcast({ type: "agent:question", agentId, question: errorAgent.pendingQuestion });
        } else if (type === "permission" && errorAgent.pendingPermission) {
          broadcast({ type: "agent:permission", agentId, permission: errorAgent.pendingPermission });
        }
      }
    }
  });

  return true;
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

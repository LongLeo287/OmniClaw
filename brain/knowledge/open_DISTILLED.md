---
id: open
type: knowledge
owner: OA_Triage
---
# open
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "open-higgsfield-ai",
  "description": "Open-source alternative to Higgsfield AI — AI image, video, cinema and lip sync studio",
  "private": true,
  "version": "1.0.0",
  "workspaces": [
    "packages/studio"
  ],
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "build:studio": "cd packages/studio && npm run build",
    "setup": "npm install && npm run build:studio",
    "vite:dev": "vite",
    "vite:build": "vite build",
    "electron:build": "vite build && electron-builder --mac",
    "electron:build:win": "vite build && electron-builder --win",
    "electron:build:all": "vite build && electron-builder --mac --win"
  },
  "build": {
    "appId": "ai.higgsfield.open",
    "productName": "Open Higgsfield AI",
    "copyright": "Copyright © 2025",
    "directories": { "output": "release" },
    "afterPack": "./afterPack.js",
    "files": ["dist/**/*", "electron/**/*"],
    "mac": {
      "category": "public.app-category.graphics-design",
      "icon": "public/banner.png",
      "gatekeeperAssess": false,
      "target": [{ "target": "dmg", "arch": ["x64", "arm64"] }]
    },
    "win": {
      "icon": "public/banner.png",
      "target": [{ "target": "nsis", "arch": ["x64", "arm64"] }]
    }
  },
  "dependencies": {
    "next": "^15.0.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "studio": "*",
    "axios": "^1.7.0",
    "react-hot-toast": "^2.4.1"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "autoprefixer": "^10.4.24",
    "electron": "^33.4.11",
    "electron-builder": "^25.1.8",
    "eslint": "^9",
    "eslint-config-next": "^15.0.0",
    "postcss": "^8.5.6",
    "tailwindcss": "^3.4.0",
    "vite": "^5.4.0",
    "@tailwindcss/vite": "^4.1.18"
  }
}

```

### File: README.md
```md
# Open Higgsfield AI — Open-Source Alternative to Higgsfield AI

> **The free, open-source alternative to Higgsfield AI.** Generate AI images and videos using 200+ state-of-the-art models — without the closed ecosystem or subscription fees.

## 🌐 Try it Online — No Install Required

**Hosted version:** [muapi.ai/open-higgsfield-ai](https://muapi.ai/open-higgsfield-ai)

Use all four studios (Image, Video, Lip Sync, Cinema) directly in your browser — no Node.js, no setup. Sign up for a free account to start generating. The hosted version is always up to date with the latest models.

---

## ⬇️ Download Desktop App

One-click installers — no Node.js or terminal required.

| Platform | Download |
|---|---|
| macOS Apple Silicon (M1/M2/M3/M4) | [Open Higgsfield AI-1.0.0-arm64.dmg](https://github.com/Anil-matcha/Open-Higgsfield-AI/releases/download/v1.0.0/Open.Higgsfield.AI-1.0.0-arm64.dmg) |
| macOS Intel (x64) | [Open Higgsfield AI-1.0.0.dmg](https://github.com/Anil-matcha/Open-Higgsfield-AI/releases/download/v1.0.0/Open.Higgsfield.AI-1.0.0.dmg) |
| Windows (x64 + ARM64) | [Open Higgsfield AI Setup 1.0.0.exe](https://github.com/Anil-matcha/Open-Higgsfield-AI/releases/download/v1.0.0/Open.Higgsfield.AI.Setup.1.0.0.exe) |

All releases: [github.com/Anil-matcha/Open-Higgsfield-AI/releases](https://github.com/Anil-matcha/Open-Higgsfield-AI/releases)

### macOS Installation Guide

Because the app is not notarized by Apple, macOS Gatekeeper will block it on first launch. Follow these steps:

**Step 1** — Mount the DMG and drag the app to `/Applications`

**Step 2** — Open Terminal and run:
```bash
xattr -cr "/Applications/Open Higgsfield AI.app"
```

**Step 3** — Right-click the app in `/Applications` → click **Open** → click **Open** again on the dialog

> You only need to do this once. After that, the app opens normally.

**Alternative (no Terminal):**
1. Try to open the app — macOS will block it
2. Go to **System Settings → Privacy & Security**
3. Scroll down to find _"Open Higgsfield AI was blocked"_
4. Click **Open Anyway** → **Open**

### Windows Installation — SmartScreen warning fix

Windows SmartScreen may show a warning because the installer is not code-signed:

1. Click **More info** on the SmartScreen dialog
2. Click **Run anyway**

The app will install silently to `%LocalAppData%` with a Start Menu shortcut.

---

Open Higgsfield AI is an open-source AI image, video, cinema, and lip sync studio that brings Higgsfield-style creative workflows to everyone. Powered by [Muapi.ai](https://muapi.ai), it supports text-to-image, image-to-image, text-to-video, image-to-video, and audio-driven lip sync generation across models like Flux, Nano Banana, Midjourney, Kling, Sora, Veo, Seedream, Infinite Talk, LTX Lipsync, Wan 2.2, and more — all from a sleek, modern interface you can self-host and customize.

**Why Open Higgsfield AI instead of Higgsfield AI?**
- **Free & open-source** — no subscription, no vendor lock-in
- **Self-hosted** — your data stays on your machine
- **200+ models** — text-to-image, image-to-image, text-to-video, image-to-video, lip sync
- **Multi-image input** — feed up to 14 reference images into compatible models
- **Lip Sync Studio** — animate portraits or sync lips to any audio with 9 dedicated models
- **Extensible** — add your own models, modify the UI, build on top of it

For a deep dive into the technical architecture and the philosophy behind the "Infinite Budget" cinema workflow, see our [comprehensive guide and roadmap](https://medium.com/@anilmatcha/building-open-higgsfield-ai-an-open-source-ai-cinema-studio-83c1e0a2a5f1).

![Studio Demo](docs/assets/studio_demo.webp)

## ✨ Features

- **Image Studio** — Generate images from text prompts (50+ text-to-image models) or transform existing images (55+ image-to-image models). Switches model set automatically based on whether a reference image is provided. Quality and resolution controls visible for models that support them.
- **Multi-Image Input** — Upload up to 14 reference images for compatible edit models (Nano Banana 2 Edit, Flux Kontext Dev, GPT-4o Edit, and more). Multi-select picker with order badges, batch upload, and a "Use Selected" confirmation flow.
- **Video Studio** — Generate videos from text prompts (40+ text-to-video models) or animate a start-frame image (60+ image-to-video models). Same intelligent mode switching as Image Studio.
- **Lip Sync Studio** — Animate portrait images or sync lips on existing videos using audio. 9 dedicated models across two modes: portrait image + audio → talking video, and video + audio → lipsync video.
- **Cinema Studio** — Higgsfield AI-style interface for photorealistic cinematic shots with pro camera controls (Lens, Focal Length, Aperture)
- **Upload History** — Reference images are uploaded once and stored locally. A picker panel lets you reuse any previously uploaded image across sessions — no re-uploading.
- **Smart Controls** — Dynamic aspect ratio, resolution/quality, and duration pickers that adapt to each model's capabilities (including t2i models with resolution or quality options)
- **Generation History** — Browse, revisit, and download all past generations (persisted in browser storage)
- **Image & Video Download** — One-click download of generated outputs in full resolution
- **API Key Management** — Secure API key storage in browser localStorage (never sent to any server except Muapi)
- **Responsive Design** — Works seamlessly on desktop and mobile with dark glassmorphism UI

### 🖼️ Image Studio — Dual Mode

The Image Studio automatically switches between two model sets:

| Mode | Trigger | Models | Prompt |
| :--- | :--- | :--- | :--- |
| **Text-to-Image** | Default (no image) | 50+ t2i models (Flux, Nano Banana 2, Seedream 5.0, Ideogram, GPT-4o, Midjourney…) | Required |
| **Image-to-Image** | Reference image uploaded | 55+ i2i models (Kontext, Nano Banana 2 Edit, Seedream 5.0 Edit, Seededit, Upscaler…) | Optional |

#### Newly Added Models

| Model | Type | Key Features |
| :--- | :--- | :--- |
| **Nano Banana 2** | Text-to-Image | Google Gemini 3.1 Flash Image · Resolution 1K/2K/4K · Google Search enhancement · aspect ratio `auto` |
| **Nano Banana 2 Edit** | Image-to-Image | Up to **14 reference images** · Resolution 1K/2K/4K · Google Search enhancement |
| **Seedream 5.0** | Text-to-Image | ByteDance · Quality basic/high · 8 aspect ratios · up to 4K |
| **Seedream 5.0 Edit** | Image-to-Image | ByteDance · Natural language style transfer · Quality basic/high |

#### Multi-Image Input

Models that accept multiple reference images expose a multi-select picker when active:

| Model | Max Images |
| :--- | :--- |
| Nano Banana 2 Edit | 14 |
| Nano Banana Edit | 10 |
| Flux Kontext Dev I2I | 10 |
| Kling O1 Edit Image | 10 |
| GPT-4o Edit / GPT Image 1.5 Edit | 10 |
| Bytedance Seedream Edit v4 / v4.5 | 10 |
| Vidu Q2 Reference to Image | 7 |
| Flux 2 Flex/Pro Edit | 8 |
| Nano Banana Pro Edit | 8 |
| Flux Kontext Pro/Max I2I | 2 |
| Wan 2.5/2.6 Image Edit | 2–3 |
| Qwen Image Edit Plus / 2511 | 3 |
| GPT-4o Image to Image | 5 |
| Flux 2 Klein 4b/9b Edit | 4 |

When a multi-image model is selected the upload trigger switches to multi-select mode:
- **Checkboxes with order numbers** — images are sent to the model in the order you select them
- **Batch upload** — pick multiple files at once from your file dialog
- **Count badge** on the trigger shows how many images are active; a `+` badge appears when more slots are available
- **"Use Selected" button** confirms and closes the picker

### 🎬 Video Studio — Dual Mode

The Video Studio follows the same pattern:

| Mode | Trigger | Models | Prompt |
| :--- | :--- | :--- | :--- |
| **Text-to-Video** | Default (no image) | 40+ t2v models (Kling, Sora, Veo, Wan, Seedance 2.0, Hailuo, Runway…) | Required |
| **Image-to-Video** | Start frame uploaded | 60+ i2v models (Kling I2V, Veo3 I2V, Runway I2V, Wan I2V, Seedance 2.0 I2V, Midjourney I2V…) | Optional |

#### Newly Added Models

| Model | Type | Key Features |
| :--- | :--- | :--- |
| **Seedance 2.0** | Text-to-Video | ByteDance · Aspect ratios 16:9 / 9:16 / 4:3 / 3:4 · Duration 5 / 10 / 15s · Quality basic/high |
| **Seedance 2.0 I2V** | Image-to-Video | ByteDance · Animate images into video · Up to 9 reference images · Aspect ratios 16:9 / 9:16 / 4:3 / 3:4 · Duration 5 / 10 / 15s · Quality basic/high |
| **Seedance 2.0 Extend** | Video Extension | ByteDance · Seamlessly continue any Seedance 2.0 generation · Preserves style, motion & audio · Optional continuation prompt · Duration 5 / 10 / 15s · Quality basic/high |
| **Grok Imagine T2V** | Text-to-Video | xAI · Duration 6 / 10 / **15s** · Modes: fun / normal / spicy · Aspect ratios 9:16 / 16:9 / 2:3 / 3:2 / 1:1 |
| **Grok Imagine I2V** | Image-to-Video | xAI · Duration 6 / 10 / **15s** · Modes: fun / normal / spicy · Cinematic motion from still images |

### 🎙️ Lip Sync Studio

The **Lip Sync Studio** generates audio-driven talking videos using 9 models across two input modes:

| Mode | Trigger | Description |
| :--- | :--- | :--- |
| **Portrait Image** | Default | Upload a portrait image + audio file → animated talking video |
| **Video** | Switch to Video mode | Upload an existing video + audio file → lipsync video |

#### Image-based Models (Portrait Image + Audio → Video)

| Model | Endpoint | Resolutions | Prompt |
| :--- | :--- | :--- | :--- |
| **Infinite Talk** | `infinitetalk-image-to-video` | 480p, 720p | Optional |
| **Wan 2.2 Speech to Video** | `wan2.2-speech-to-video` | 480p, 720p | Optional |
| **LTX 2.3 Lipsync** | `ltx-2.3-lipsync` | 480p, 720p, 1080p | Optional |
| **LTX 2 19B Lipsync** | `ltx-2-19b-lipsync` | 480p, 720p, 1080p | Optional |

#### Video-based Models (Video + Audio → Lipsync Video)

| Model | Endpoint | Resolutions | Prompt |
| :--- | :--- | :--- | :--- |
| **Sync Lipsync** | `sync-lipsync` | — | — |
| **LatentSync** | `latentsync-video` | — | — |
| **Creatify Lipsync** | `creatify-lipsync` | — | — |
| **Veed Lipsync** | `veed-lipsync` | — | — |
| **Infinite Talk V2V** | `infinitetalk-video-to-video` | 480p, 720p | Optional |

**How it works:**
1. Select **Portrait Image** or **Video** mode using the toggle
2. Upload your portrait image (or video) using the image/video upload button
3. Upload your audio file using the audio upload button
4. Optionally enter a prompt to guide the motion style
5. Select a model and resolution (where supported), then click **Generate**

Generation history is saved separately in `lipsync_history` and pending jobs resume automatically on page reload.

### 🎥 Cinema Studio Controls

The **Cinema Studio** offers precise control over the virtual camera, translating your choices into optimized prompt modifiers:

| Category | Available Options |
| :--- | :--- |
| **Cameras** | Modular 8K Digital, Full-Frame Cine Digital, Grand Format 70mm Film, Studio Digital S35, Classic 16mm Film, Premium Large Format Digital |
| **Lenses** | Creative Tilt, Compact Anamorphic, Extreme Macro, 70s Cinema Prime, Classic Anamorphic, Premium Modern Prime, Warm Cinema Prime, Swirl Bokeh Portrait, Vintage Prime, Halation Diffusion, Clinical Sharp Prime |
| **Focal Lengths** | 8mm (Ultra-Wide), 14mm, 24mm, 35mm (Human Eye), 50mm (Portrait), 85mm (Tight Portrait) |
| **Apertures** | f/1.4 (Shallow DoF), f/4 (Balanced), f/11 (Deep Focus) |

### 📁 Upload History & Picker

Every image you upload is saved locally (URL + thumbnail) so you never upload the same file twice:

- Click the upload button to open the **reference image picker**
- Previously uploaded images appear in a 3-column grid with thumbnails
- **Single-image models** — click a thumbnail to instantly select and close
- **Multi-image models** — toggle multiple thumbnails (shown with order numbers), then click **Use Selected**
- Upload new images with the **Upload files** button (supports multi-file selection in multi-image mode)
- Remove individual images from history with the ✕ button
- History persists across browser sessions (stored in `localStorage`)

## 🚀 Quick Start

### Prerequisites

- [Node.js](https://nodejs.org/) (v18+)
- A [Muapi.ai](https://muapi.ai) API key

### Setup

```bash
# Clone the repository
git clone https://github.com/Anil-matcha/Open-Higgsfield-AI.git
cd Open-Higgsfield-AI

# Install dependencies (installs root + packages/studio workspace)
npm install

# Start the development server
npm run dev
```

Open `http://localhost:3000` in your browser. You'll be prompted to enter your Muapi API key on first use.

### Production Build

```bash
npm run build
npm run start
```

### Desktop App Build

Build native desktop apps with Electron:

```bash
# macOS (DMG — Intel + Apple Silicon)
npm run electron:build

# Windows (NSIS installer — x64 + ARM64)
npm run electron:build:win

# Both platforms in one pass
npm run electron:build:all
```

Installers are output to the `release/` folder. Pre-built binaries are also available on the [Releases page](https://github.com/Anil-matcha/Open-Higgsfield-AI/releases).

## 🏗️ Architecture

The app is a **Next.js monorepo** with a shared `packages/studio` component library.

```
Open-Higgsfield-AI/
├── app/                        # Next.js App Router
│   ├── layout.js               # Root layout (Tailwind, fonts)
│   ├── page.js                 # Redirects → /studio
│   └── studio/
│       └── page.js             # Studio page — renders StandaloneShell
├── components/
│   ├── StandaloneShell.js      # Tab nav + BYOK (API key from localStorage)
│   └── ApiKeyModal.js          # API key entry modal
├── packages/
│   └── studio/                 # Shared React component library
│       └── src/
│           ├── index.js        # Exports: ImageStudio, VideoStudio, LipSyncStudio, CinemaStudio
│           ├── models.js       # 200+ model definitions (single source of truth)
│           ├── muapi.js        # API client (named exports, apiKey as first param)
│           └── components/
│               ├── ImageStudio.jsx    # Dual-mode t2i/i2i studio
│               ├── VideoStudio.jsx    # Dual-mode t2v/i2v studio
│               ├── LipSyncStudio.jsx  # Portrait/video + audio → talking video
│               └── CinemaStudio.jsx   # Pro studio with camera controls
├── next.config.mjs             # transpilePackages: ['studio']
├── tailwind.config.js
└── package.json                # workspaces: ["packages/studio"]
```

The `packages/studio` library is also consumed by the hosted version on [muapi.ai](https://muapi.ai) — model updates made in `packages/studio/src/models.js` apply to both the self-hosted app and the hosted version automatically.

## 🔌 API Integration

The app communicates with [Muapi.ai](https://muapi.ai) using a two-step pattern:

1. **Submit** — `POST /api/v1/{model-endpoint}` with prompt and parameters
2. **Poll** — `GET /api/v1/predictions/{request_id}/result` until status is `completed`

Authentication uses the `x-api-key` header. During development, a Vite proxy handles CORS by routi
... [TRUNCATED]
```

### File: server\package.json
```json
{
  "name": "claude-agent-backend",
  "version": "1.0.0",
  "type": "module",
  "main": "server.js",
  "scripts": {
    "start": "node server.js",
    "dev": "node server.js"
  },
  "dependencies": {
    "express": "^5.2.1",
    "@anthropic-ai/claude-agent-sdk": "^0.2.7",
    "@composio/core": "latest",
    "@opencode-ai/sdk": "latest",
    "dotenv": "^16.4.5",
    "cors": "^2.8.5"
  }
}

```

### File: server\providers\index.js
```js
import { ClaudeProvider } from './claude-provider.js';
import { OpencodeProvider } from './opencode-provider.js';

// Provider registry
const providers = {
  claude: ClaudeProvider,
  opencode: OpencodeProvider
};

// Provider instance cache
const providerInstances = new Map();

/**
 * Get a provider instance by name
 * Instances are cached and reused
 *
 * @param {string} providerName - 'claude' or 'opencode'
 * @param {Object} [config] - Provider configuration
 * @returns {BaseProvider} Provider instance
 */
export function getProvider(providerName, config = {}) {
  const name = providerName?.toLowerCase() || 'claude';

  if (!providers[name]) {
    throw new Error(`Unknown provider: ${name}. Available providers: ${Object.keys(providers).join(', ')}`);
  }

  // Check cache
  const cacheKey = `${name}:${JSON.stringify(config)}`;
  if (providerInstances.has(cacheKey)) {
    return providerInstances.get(cacheKey);
  }

  // Create new instance
  const ProviderClass = providers[name];
  const instance = new ProviderClass(config);
  providerInstances.set(cacheKey, instance);

  return instance;
}

/**
 * Get list of available provider names
 * @returns {string[]}
 */
export function getAvailableProviders() {
  return Object.keys(providers);
}

/**
 * Register a custom provider
 * @param {string} name - Provider name
 * @param {typeof BaseProvider} ProviderClass - Provider class
 */
export function registerProvider(name, ProviderClass) {
  providers[name.toLowerCase()] = ProviderClass;
}

/**
 * Clear provider instance cache
 */
export async function clearProviderCache() {
  for (const instance of providerInstances.values()) {
    if (instance.cleanup) {
      await instance.cleanup();
    }
  }
  providerInstances.clear();
}

export async function initializeProviders() {
  console.log('[Providers] Initializing providers...');
  try {
    // Get and initialize opencode provider
    const opencodeProvider = getProvider('opencode');
    await opencodeProvider.initialize();
    console.log('[Providers] Opencode provider initialized');
  } catch (error) {
    console.error('[Providers] Error initializing providers:', error.message);
  }
}

// Export classes for direct use
export { ClaudeProvider } from './claude-provider.js';
export { OpencodeProvider } from './opencode-provider.js';
export { BaseProvider } from './base-provider.js';
```

### File: afterPack.js
```js
import { execSync } from 'child_process';
import path from 'path';

export default async function afterPack({ appOutDir, packager }) {
    if (packager.platform.name !== 'mac') return;

    const appPath = path.join(appOutDir, `${packager.appInfo.productName}.app`);
    console.log(`  • ad-hoc signing  path=${appPath}`);
    execSync(`codesign --deep --force --sign - "${appPath}"`, { stdio: 'inherit' });
    console.log(`  • ad-hoc signing complete`);
}

```

### File: index.html
```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Open Higgsfield AI — the free, open-source alternative to Higgsfield AI. Generate AI images and cinematic shots with 20+ models including Flux, SDXL, Ideogram, and Midjourney." />
    <meta name="keywords" content="higgsfield ai, higgsfield alternative, open source higgsfield, ai image generator, ai cinema studio, flux ai, ai video generation, free higgsfield, open source ai image generation" />
    <title>Open Higgsfield AI — Free Open-Source Alternative to Higgsfield AI</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.js"></script>
  </body>
</html>

```

### File: jsconfig.json
```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"]
    }
  }
}

```

### File: main.js
```js
const { app, BrowserWindow, shell } = require('electron');
const path = require('path');

const isDev = process.env.NODE_ENV === 'development';

if (isDev) {
  try {
    // Enable live-reload for the main and renderer processes during development
    require('electron-reload')(__dirname, {
      electron: path.join(__dirname, 'node_modules', '.bin', 'electron'),
      ignored: /server|node_modules/
    });
  } catch (err) {
    console.warn('Live reload unavailable:', err);
  }
}

// Global window reference
let mainWindow;

// Create Electron window
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js'),
      enableWebSQL: false,
      webSecurity: true
    }
  });

  // Load the app
  mainWindow.loadFile(path.join(__dirname, 'renderer', 'index.html'));

  // Open DevTools in development (comment out for production)
  // mainWindow.webContents.openDevTools();

  mainWindow.on('closed', () => {
    mainWindow = null;
  });

  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });

  mainWindow.webContents.on('will-navigate', (event, url) => {
    // If navigating away from our app, open in external browser
    if (!url.startsWith('file://')) {
      event.preventDefault();
      shell.openExternal(url);
    }
  });
}

// App lifecycle
app.on('ready', () => {
  console.log('Electron app ready');
  createWindow();
});

app.on('window-all-closed', () => {
  // On macOS, apps stay active until user explicitly quits
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  // On macOS, re-create window when dock icon is clicked
  if (mainWindow === null) {
    createWindow();
  }
});

```

### File: models_dump.json
```json
{
  "t2i": [
    {
      "id": "nano-banana",
      "name": "Nano Banana",
      "inputs": {
        "prompt": {
          "examples": [
            "A portrait of me in a modern living room. Change it so I’m dressed in 1950s attire with a polka-dot dress, while maintaining my face and hairstyle."
          ],
          "description": "Text prompt describing the image, what you want the final edited image to look like.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "aspect_ratio": {
          "enum": [
            "1:1",
            "3:4",
            "4:3",
            "9:16",
            "16:9",
            "3:2",
            "2:3",
            "5:4",
            "4:5",
            "21:9"
          ],
          "title": "Aspect Ratio",
          "name": "aspect_ratio",
          "type": "string",
          "description": "Aspect ratio of the output image.",
          "default": "1:1"
        }
      }
    },
    {
      "id": "flux-dev",
      "name": "Flux Dev",
      "inputs": {
        "prompt": {
          "examples": [
            "Extreme close-up of a single tiger eye, direct frontal view. Detailed iris and pupil. Sharp focus on eye texture and color. Natural lighting to capture authentic eye shine and depth. The word \"FLUX\" is painted over it in big, white brush strokes with visible texture."
          ],
          "description": "Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "width": {
          "title": "Width",
          "name": "width",
          "type": "int",
          "description": "Width of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64
        },
        "height": {
          "title": "Height",
          "name": "height",
          "type": "int",
          "description": "Height of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64
        },
        "num_images": {
          "title": "Number of images",
          "name": "num_images",
          "type": "int",
          "description": "Number of images generated in single request. Each number will charge separately",
          "default": 1,
          "minValue": 1,
          "maxValue": 4,
          "step": 1
        }
      }
    },
    {
      "id": "flux-dev-lora",
      "name": "Flux Dev Lora",
      "inputs": {
        "prompt": {
          "examples": [
            "A female warrior in ornate armor standing on a cliff during sunset, flowing cape, wind blowing through her hair, detailed fantasy art style."
          ],
          "description": "Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "model_id": {
          "examples": [
            {
              "model": "civitai:119351@317153",
              "weight": 1
            }
          ],
          "title": "LoRA Ids",
          "name": "model_id",
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "model": {
                "type": "string",
                "format": "url",
                "title": "Model ID",
                "description": "The Civitai LoRA model ID."
              },
              "weight": {
                "type": "number",
                "title": "Weight",
                "description": "A list of LoRA models to use for generation. Each item must include an `id` (e.g., \"civitai:1642876@1864626\") and a `weight` between 0 and 4. You can include up to 4 models. The `id` can be found in the Civitai model URL. These models will be applied with the specified weights by the Flux Dev system during image generation.",
                "minValue": 0,
                "maxValue": 4,
                "step": 0.01,
                "default": 1
              }
            }
          },
          "description": "The unique identifier of a LoRA model hosted on Civitai, used by the Flux Dev image generation system. This ID tells Flux Dev which specific LoRA model to apply during generation. You can find the model ID in the Civitai model URL (e.g., model_id: civitai:1642876@1864626).",
          "maxItems": 4
        },
        "width": {
          "title": "Width",
          "name": "width",
          "type": "int",
          "description": "Width of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64,
          "isEdit": true
        },
        "height": {
          "title": "Height",
          "name": "height",
          "type": "int",
          "description": "Height of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64,
          "isEdit": true
        },
        "num_images": {
          "title": "Number of images",
          "name": "num_images",
          "type": "int",
          "description": "Number of images generated in single request. Each number will charge separately",
          "default": 1,
          "minValue": 1,
          "maxValue": 4,
          "step": 1,
          "isEdit": true
        }
      }
    },
    {
      "id": "flux-kontext-dev-t2i",
      "name": "Flux Kontext Dev T2I",
      "inputs": {
        "prompt": {
          "examples": [
            "A powerful wizard casting a glowing spell in a dark forest, wearing a hooded robe, with swirling magical energy, epic fantasy art."
          ],
          "description": "Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "aspect_ratio": {
          "enum": [
            "16:9",
            "9:16",
            "1:1",
            "4:3",
            "3:4",
            "3:2",
            "2:3",
            "21:9",
            "9:21"
          ],
          "title": "Aspect Ratio",
          "name": "aspect_ratio",
          "type": "string",
          "description": "Aspect ratio of the output image.",
          "default": "1:1"
        },
        "num_images": {
          "title": "Number of images",
          "name": "num_images",
          "type": "int",
          "description": "Number of images generated in single request. Each number will charge separately",
          "default": 1,
          "minValue": 1,
          "maxValue": 4,
          "step": 1,
          "isEdit": true
        }
      }
    },
    {
      "id": "hidream-i1-fast",
      "name": "Hidream I1 Fast",
      "inputs": {
        "prompt": {
          "examples": [
            "A colorful cartoon-style cat sitting on a skateboard, wide smile, playful background, 2D flat illustration style."
          ],
          "description": "Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "width": {
          "title": "Width",
          "name": "width",
          "type": "int",
          "description": "Width of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64
        },
        "height": {
          "title": "Height",
          "name": "height",
          "type": "int",
          "description": "Height of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64
        },
        "num_images": {
          "title": "Number of images",
          "name": "num_images",
          "type": "int",
          "description": "Number of images generated in single request. Each number will charge separately",
          "default": 1,
          "minValue": 1,
          "maxValue": 4,
          "step": 1
        }
      }
    },
    {
      "id": "hidream-i1-dev",
      "name": "Hidream I1 Dev",
      "inputs": {
        "prompt": {
          "examples": [
            "A colorful cartoon-style cat sitting on a skateboard, wide smile, playful background, 2D flat illustration style."
          ],
          "description": "Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "width": {
          "title": "Width",
          "name": "width",
          "type": "int",
          "description": "Width of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64
        },
        "height": {
          "title": "Height",
          "name": "height",
          "type": "int",
          "description": "Height of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64
        },
        "num_images": {
          "title": "Number of images",
          "name": "num_images",
          "type": "int",
          "description": "Number of images generated in single request. Each number will charge separately",
          "default": 1,
          "minValue": 1,
          "maxValue": 4,
          "step": 1
        }
      }
    },
    {
      "id": "hidream-i1-full",
      "name": "Hidream I1 Full",
      "inputs": {
        "prompt": {
          "examples": [
            "A majestic elven queen standing in a glowing forest, wearing intricate golden armor with emerald details, sunlight rays filtering through the trees, ultra-detailed fantasy concept art."
          ],
          "description": "Text prompt describing the image. The length of the prompt must be between 2 and 3000 characters.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "width": {
          "title": "Width",
          "name": "width",
          "type": "int",
          "description": "Width of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64
        },
        "height": {
          "title": "Height",
          "name": "height",
          "type": "int",
          "description": "Height of the output image. The value must be divisible by 64, eg: 128...512, 576, 640...2048.",
          "default": 1024,
          "minValue": 128,
          "maxValue": 2048,
          "step": 64
        },
        "num_images": {
          "title": "Number of images",
          "name": "num_images",
          "type": "int",
          "description": "Number of images generated in single request. Each number will charge separately",
          "default": 1,
          "minValue": 1,
          "maxValue": 4,
          "step": 1
        }
      }
    },
    {
      "id": "ai-anime-generator",
      "name": "Ai Anime Generator",
      "inputs": {
        "prompt": {
          "examples": [
            "A cheerful anime girl with short pink hair and green eyes, wearing a school uniform, standing under cherry blossom trees, soft lighting, anime style."
          ],
          "description": "Text prompt describing the image.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "width": {
          "title": "Width",
          "name": "width",
          "type": "int",
          "description": "Width of the output image.",
          "default": 1024,
          "minValue": 256,
          "maxValue": 1536,
          "step": 1,
          "isEdit": true
        },
        "height": {
          "title": "Height",
          "name": "height",
          "type": "int",
          "description": "Height of the output image.",
          "default": 1024,
          "minValue": 256,
          "maxValue": 1536,
          "step": 1,
          "isEdit": true
        }
      }
    },
    {
      "id": "wan2.1-text-to-image",
      "name": "Wan2.1 Text To Image",
      "inputs": {
        "prompt": {
          "examples": [
            "A young woman with freckles and natural makeup, standing in soft sunlight, sharp focus, DSLR photo style, ultra-realistic skin texture."
          ],
          "description": "Text prompt describing the image.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "width": {
          "title": "Width",
          "name": "width",
          "type": "int",
          "description": "Width of the output image.",
          "default": 1024,
          "minValue": 256,
          "maxValue": 1536,
          "step": 1
        },
        "height": {
          "title": "Height",
          "name": "height",
          "type": "int",
          "description": "Height of the output image.",
          "default": 1024,
          "minValue": 256,
          "maxValue": 1536,
          "step": 1
        }
      }
    },
    {
      "id": "flux-kontext-pro-t2i",
      "name": "Flux Kontext Pro T2I",
      "inputs": {
        "prompt": {
          "examples": [
            "A steampunk owl with mechanical wings, perched on a glowing gear, cinematic lighting."
          ],
          "description": "Text prompt describing the image.",
          "type": "string",
          "title": "Prompt",
          "name": "prompt"
        },
        "aspect_ratio": {
          "enum": [
            "16:9",
            "9:16",
            "1:1",
            "4:3",
            "3:4",
            "21:9",
            "16:21"
          ],
          "title": "Aspect Ratio",
          "name": "aspect_ratio",
          "type": "string",
          "description": "Aspect ratio of the output image.",
          "default": "1:1"
        }
      }
    },
    {
      "id": "flux-kontext-max-t2i",
      "name": "Flux Kontext Max T2I",
      "inputs": {
        "prompt": {
          "examples": [
            "A realistic portrait of a woman with curly hair, wearing a silk blouse, studio lighting, high detail."
          ],
          "description": "Text prompt describing the image.",
          "type": "string",
          "title": "Prompt",
          
... [TRUNCATED]
```

### File: package-lock.json
```json
{
  "name": "open-claude-cowork",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "open-claude-cowork",
      "version": "1.0.0",
      "license": "ISC",
      "dependencies": {
        "@anthropic-ai/claude-agent-sdk": "^0.2.7",
        "@opencode-ai/sdk": "latest",
        "cors": "^2.8.5",
        "dotenv": "^16.4.5",
        "express": "^5.2.1"
      },
      "devDependencies": {
        "electron": "^39.2.7",
        "electron-reload": "^2.0.0-alpha.1"
      }
    },
    "node_modules/@anthropic-ai/claude-agent-sdk": {
      "version": "0.2.7",
      "resolved": "https://registry.npmjs.org/@anthropic-ai/claude-agent-sdk/-/claude-agent-sdk-0.2.7.tgz",
      "integrity": "sha512-I1/zcnLah74kZeRkj/1QnDaC6ItJ2m/Bftlm25uoaRkZx7i7SkcpqM9jGE/r2A8PMxnw5WpabP60Xgj99CrTuw==",
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
    "node_modules/@electron/get": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/@electron/get/-/get-2.0.3.tgz",
      "integrity": "sha512-Qkzpg2s9GnVV2I2BjRksUi43U5e6+zaQMcjoJy0C+C5oxaKl+fmckGDQFtRpZpZV0NQekuZZ+tGz7EA9TVnQtQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "debug": "^4.1.1",
        "env-paths": "^2.2.0",
        "fs-extra": "^8.1.0",
        "got": "^11.8.5",
        "progress": "^2.0.3",
        "semver": "^6.2.0",
        "sumchecker": "^3.0.1"
      },
      "engines": {
        "node": ">=12"
      },
      "optionalDependencies": {
        "global-agent": "^3.0.0"
      }
    },
    "node_modules/@img/sharp-darwin-arm64": {
      "version": "0.33.5",
      "resolved": "https://registry.npmjs.org/@img/sharp-darwin-arm64/-/sharp-darwin-arm64-0.33.5.tgz",
      "integrity": "sha512-UT4p+iz/2H4twwAoLCqfA9UH5pI6DggwKEGuaPy7nCVQ8ZsiY5PIcrRvD1DzuY3qYL07NtIQcWnBSY/heikIFQ==",
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
      "resolved": "https://registry.npmjs.org/@img/sharp-libvips-darwin-arm64/-/sharp-libvips-darwin-arm64-1.0.4.tgz",
      "integrity": "sha512-XblONe153h0O2zuFfTAbQYAX2JhYmDHeWikp1LM9Hul9gVPjFY427k6dFEcOL72O01QxQsWi761svJ/ev9xEDg==",
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
      "resolved": "https://registry.npmjs.org/@img/sharp-linuxmusl-arm64/-/sharp-linuxmusl-arm64-0.33.5.tgz",
      "integrity": "sha512-XrHMZwGQGvJg2V/oRSUfSAfjfPxO+4DkiRh6p2AFjLQztWUuY/o8Mq0eMQVIY7HJ1CDQUJlxGGZRw1a5bqmd1g==",
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
        "@img/sharp-libvips-linuxmusl-arm64": "1.0.4"
      }
    },
    "node_modules/@img/sharp-linuxmusl-x64": {
      "version": "0.33.5",
      "resolved": "https://registry.npmjs.org/@img/sharp-linuxmusl-x64/-/sharp-linuxmusl-x64-0.33.5.tgz",
      "integrity": "sha512-WT+d/cgqKkkKySYmqoZ8y3pxx7lx9vVejxW/W4DOFMYVSkErR+w7mf2u8m/y4+xHe7yY9DAXQMWQhpnMuFfScw==",
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
        "@img/sharp-libvips-linuxmusl-x64": "1.0.4"
      }
    },
    "node_modules/@img/sharp-win32-x64": {
      "version": "0.33.5",
      "resolved": "https://registry.npmjs.org/@img/sharp-win32-x64/-/sharp-win32-x64-0.33.5.tgz",
      "integrity": "sha512-MpY/o8/8kj+EcnxwvrP4aTJSWw/aZ7JIGR4aBeZkZw5B7/Jn+tY9/VNwtcoGmdT7GfggGIU4kygOMSbYnOrAbg==",
      "cpu": [
        "x64"
      ],
      "license": "Apache-2.0 AND LGPL-3.0-or-later",
      "optional": true,
      "os": [
        "win32"
      ],
      "engines": {
        "node": "^18.17.0 || ^20.3.0 || >=21.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/libvips"
      }
    },
    "node_modules/@opencode-ai/sdk": {
      "version": "1.1.23",
      "resolved": "https://registry.npmjs.org/@opencode-ai/sdk/-/sdk-1.1.23.tgz",
      "integrity": "sha512-YjN9ogzkLol92s+/iARXRop9/5oFIezUkvWVay12u1IM6A/WJs50DeKl3oL0x4a68P1a5tI5gD98dLnk2+AlsA==",
      "license": "MIT"
    },
    "node_modules/@sindresorhus/is": {
      "version": "4.6.0",
      "resolved": "https://registry.npmjs.org/@sindresorhus/is/-/is-4.6.0.tgz",
      "integrity": "sha512-t09vSN3MdfsyCHoFcTRCH/iUtG7OJ0CsjzB8cjAmKc/va/kIgeDI/TxsigdncE/4be734m0cvIYwNaV4i2XqAw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sindresorhus/is?sponsor=1"
      }
    },
    "node_modules/@szmarczak/http-timer": {
      "version": "4.0.6",
      "resolved": "https://registry.npmjs.org/@szmarczak/http-timer/-/http-timer-4.0.6.tgz",
      "integrity": "sha512-4BAffykYOgO+5nzBWYwE3W90sBgLJoUPRWWcL8wlyiM8IB8ipJz3UMJ9KXQd1RKQXpKp8Tutn80HZtWsu2u76w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "defer-to-connect": "^2.0.0"
      },
      "engines": {
        "node": ">=10"
      }
    },
    "node_modules/@types/cacheable-request": {
      "version": "6.0.3",
      "resolved": "https://registry.npmjs.org/@types/cacheable-request/-/cacheable-request-6.0.3.tgz",
      "integrity": "sha512-IQ3EbTzGxIigb1I3qPZc1rWJnH0BmSKv5QYTalEwweFvyBDLSAe24zP0le/hyi7ecGfZVlIVAg4BZqb8WBwKqw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/http-cache-semantics": "*",
        "@types/keyv": "^3.1.4",
        "@types/node": "*",
        "@types/responselike": "^1.0.0"
      }
    },
    "node_modules/@types/http-cache-semantics": {
      "version": "4.0.4",
      "resolved": "https://registry.npmjs.org/@types/http-cache-semantics/-/http-cache-semantics-4.0.4.tgz",
      "integrity": "sha512-1m0bIFVc7eJWyve9S0RnuRgcQqF/Xd5QsUZAZeQFr1Q3/p9JWoQQEqmVy+DPTNpGXwhgIetAoYF8JSc33q29QA==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@types/keyv": {
      "version": "3.1.4",
      "resolved": "https://registry.npmjs.org/@types/keyv/-/keyv-3.1.4.tgz",
      "integrity": "sha512-BQ5aZNSCpj7D6K2ksrRCTmKRLEpnPvWDiLPfoGyhZ++8YtiK9d/3DBKPJgry359X/P1PfruyYwvnvwFjuEiEIg==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/node": {
      "version": "22.19.6",
      "resolved": "https://registry.npmjs.org/@types/node/-/node-22.19.6.tgz",
      "integrity": "sha512-qm+G8HuG6hOHQigsi7VGuLjUVu6TtBo/F05zvX04Mw2uCg9Dv0Qxy3Qw7j41SidlTcl5D/5yg0SEZqOB+EqZnQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "undici-types": "~6.21.0"
      }
    },
    "node_modules/@types/responselike": {
      "version": "1.0.3",
      "resolved": "https://registry.npmjs.org/@types/responselike/-/responselike-1.0.3.tgz",
      "integrity": "sha512-H/+L+UkTV33uf49PH5pCAUBVPNj2nDBXTN+qS1dOwyyg24l3CcicicCA7ca+HMvJBZcFgl5r8e+RR6elsb4Lyw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/@types/yauzl": {
      "version": "2.10.3",
      "resolved": "https://registry.npmjs.org/@types/yauzl/-/yauzl-2.10.3.tgz",
      "integrity": "sha512-oJoftv0LSuaDZE3Le4DbKX+KS9G36NzOeSap90UIK0yMA/NhKJhqlSGtNDORNRaIbQfzjXDrQa0ytJ6mNRGz/Q==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@types/node": "*"
      }
    },
    "node_modules/accepts": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/accepts/-/accepts-2.0.0.tgz",
      "integrity": "sha512-5cvg6CtKwfgdm
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

---
id: shiru
type: knowledge
owner: OA_Triage
---
# shiru
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "shiru",
  "license": "GPL-3.0-or-later",
  "private": true,
  "author": "RockinChaos <RockinChaos@users.noreply.github.com>",
  "description": "A personal anime library manager for watching and tracking your collection in real time. Lightweight, powerful, and paws-itively fast. No waiting required!",
  "main": "build/main.js",
  "homepage": "https://github.com/RockinChaos/Shiru#readme",
  "standard": {
    "ignore": [
      "bundle.js",
      "bundle.map.js"
    ],
    "env": [
      "browser",
      "node"
    ]
  },
  "dependencies": {
    "@typescript-eslint/parser": "^8.45.0",
    "copy-webpack-plugin": "^13.0.1",
    "cross-env": "^10.1.0",
    "eslint": "^10.1.0",
    "eslint-config-standard": "^17.1.0",
    "eslint-plugin-svelte": "^3.16.0",
    "html-webpack-plugin": "^5.6.6",
    "mini-css-extract-plugin": "^2.10.2",
    "semver": "^7.7.4",
    "webpack": "^5.105.4",
    "webpack-cli": "^7.0.2",
    "webpack-dev-server": "^5.2.3"
  },
  "devDependencies": {
    "@cloudflare/workers-types": "^4.20260329.1",
    "npm-run-all": "^4.1.5"
  },
  "pnpm": {
    "overrides": {
      "node-abi": "3.77.0",
      "node-datachannel": "0.30.0",
      "bittorrent-tracker": "^11.2.2"
    },
    "patchedDependencies": {
      "@capacitor/local-notifications": "patches/@capacitor__local-notifications.patch",
      "@capacitor/android": "patches/@capacitor__android.patch",
      "lucide-svelte@0.455.0": "patches/lucide-svelte@0.455.0.patch",
      "rfdc": "patches/rfdc.patch",
      "capacitor-plugin-safe-area": "patches/capacitor-plugin-safe-area.patch",
      "svelte-keybinds": "patches/svelte-keybinds.patch"
    },
    "onlyBuiltDependencies": [
      "@paymoapp/electron-shutdown-handler",
      "bufferutil",
      "electron",
      "fs-native-extensions",
      "fsctl",
      "node-datachannel",
      "sharp",
      "utf-8-validate",
      "utp-native",
      "wrtc"
    ]
  }
}

```

### File: .github\README.md
```md
<p align="center">
	<a href="https://github.com/RockinChaos/Shiru">
		<img src="../.github/docs/assets/logo_filled.svg" width="400" alt="Shiru">
	</a>
</p>
<h4 align="center"><b>A personal anime library manager for watching and tracking your collection in real time. Lightweight, powerful, and paws-itively fast. No waiting required!</b></h4>

<p align="center">
  <a href="https://github.com/RockinChaos/Shiru/wiki/">📚 Wiki</a> •
  <a href="https://github.com/RockinChaos/Shiru/wiki/features/">✨ Features</a> •
  <a href="https://github.com/RockinChaos/Shiru/wiki/faq/">❓ FAQ</a> •
  <a href="#-building--development">🔧 Building & Development</a> •
  <a href="https://github.com/RockinChaos/Shiru/releases/latest/">⬇️ Download</a>
</p>
<p align="center">
  <a href="https://github.com/RockinChaos/Shiru/releases/latest/"><img alt="Downloads" src="https://img.shields.io/github/downloads/RockinChaos/Shiru/total?style=flat-square"></a>
  <a href="https://github.com/RockinChaos/Shiru/releases/latest/"><img alt="Latest Release" src="https://img.shields.io/github/v/release/RockinChaos/Shiru?style=flat-square"></a>
  <a href="https://github.com/RockinChaos/Shiru/commits"><img alt="Last Commit" src="https://img.shields.io/github/last-commit/RockinChaos/Shiru?style=flat-square"></a>
  <a href="https://github.com/RockinChaos/Shiru/stargazers"><img alt="Stargazers" src="https://img.shields.io/github/stars/RockinChaos/Shiru?style=flat-square"></a>
  <a href="../LICENSE"><img alt="License: GPLv3" src="https://img.shields.io/github/license/RockinChaos/Shiru?style=flat-square"></a>
</p>

https://github.com/user-attachments/assets/3ff100f0-e008-4ff5-88f5-ad4290863f96

## 📃 **About**

**Shiru** is a feature-rich anime library manager built around speed, control, and a seamless viewing experience, with full mobile support. Your files play directly for near-instant playback, giving you full native video performance with no transcoding and no compression.


## 💻 Supported Platforms
- 🪟 Windows
- 🐧 Linux
- 🍎 macOS (Apple Silicon & Intel)
- 📱 Android 7.0+ (Nougat)
- 📺 Android TV 7.0+ *(remote navigation is a work in progress; mouse, keyboard, or touch recommended)*

## ✨ Key Features:
- 🪄 **AniList & MyAnimeList Integration** - manage your lists, auto-track progress, rate and score anime, and explore related series, all without leaving the app
- 🎤 **Dub-first support** - Shiru tracks both dub and sub release schedules independently, with a Prefer Dubs setting that hides series from continue watching until the next dubbed episode is available
- 🔔 **Real-time release notifications** - instant alerts for new sub, dub, and hentai episode releases, including delayed and batch announcements
- 💬 **Full subtitle support** - softcoded and external subtitles (VTT, SSA, ASS, SUB, TXT) with per-series subtitle memory, CJK glyph fallback, and in-player track cycling
- 🌐 **Extension support** - optionally bring your own content sources, such as a personal media server, directly into the app
- 📱 **Full mobile support** - a complete Android experience with landscape/portrait support, immersive full-screen, external player integration, and progress tracking
- 🎮 **Fully customizable keybindings** - drag-and-drop keybind editor with extensive default shortcuts for playback, subtitles, navigation, and more
- 📡 **Offline support** - your library, watch history, and previously loaded media are fully accessible offline, with local file playback and media resolving working entirely without an internet connection
- 🎭 **Multiple profiles** - separate libraries, settings, and watch lists per profile, with optional cross-profile sync as you watch
- 🖥️ **Discord Rich Presence** - shows what you're watching, your current progress, and paused/browsing states

## 🎥 Anime Features:

### 🪄 AniList & MyAnimeList Integration
- Filter by name, genres, tags, season, year, format, and status
- Manage your watching and planning lists with a built-in list editor
- Automatically mark episodes as completed after watching
- Watch trailers and previews directly in the app
- Rate, score, and explore related anime and recommendations
- Image search to find and identify anime by picture
- Fully customizable home page with user-built sections based on custom genres, tags, and search queries
- *Sequels You Missed* and *Stories You Missed* home sections to catch up on related entries

### 🎤 Dub & Sub Tracking
Shiru has one of the most thorough dub tracking systems available. Each series independently tracks its sub and dub release schedules, with per-episode audio labels showing exactly what is available and when.

- **Prefer Dubs** - a setting that hides series from continue watching if your progress matches the latest aired dub
- **Dubbed Audio filter** - filters the search page to only show dubbed series, and toggles the airing schedule to show dub air times instead of sub air times for currently airing dubbed series
- **Dub, Sub, and Hentai release feeds** - live feeds sorted by newest release so you never miss a drop
- **Dub and Sub notifications** - separate scheduling and tracking for both, including delayed, indefinitely delayed, and batch release announcements
- Audio labels on cards, episode lists, and the banner showing Dub, Sub, or Dual Audio status

### 🌐 Extension-Based Content Fetching *(Optional)*
Out of the box, Shiru plays files you already have locally. Extensions unlock additional content fetching for **legally owned** media, such as accessing your own personal media server remotely.

- Automatic series and episode detection from file names
- Support for custom RSS feeds and resolution preferences
- Adjustable network speeds
- Dynamic extension loading, with results appearing as each extension completes rather than waiting for all to finish
- Design and use custom [extensions](https://github.com/RockinChaos/Shiru/wiki/Extensions) to connect your own content sources

### 🔔 Notifications
- Real-time alerts for new sub, dub, and hentai episodes
- Delayed and indefinitely delayed episode notifications
- Series announcement notifications for upcoming anime
- In-app notification tray that tracks all alerts regardless of system notification settings
- Notifications are auto-marked as read when the relevant episode is watched
- Notification filtering by list status, so you only get alerted for what you care about
- Optional prefer dubs setting that ensures you are only notified when a dubbed episode is available, falling back to sub only if no dub exists for the series

## 🎬 Video Playback Features

### 💬 Subtitle Support
- Softcoded and external subtitles: VTT, SSA, ASS, SUB, TXT
- Per-series subtitle memory, with your preferred track saved per source, so your choice carries over automatically
- CJK glyph fallback using Noto Sans for missing characters
- Subtitle file selector directly in the player
- Cycle through subtitle tracks with a single key

### 📺 Playback
- Near-instant local file playback with no transcoding or compression
- Automatic thumbnail generation as files buffer, making timeline scrubbing easy even without chapters
- Chapter-aware seekbar with progress indicators and skippable sections (OP, ED, recap, filler)
- Filler and recap detection with a prompt to skip or continue
- Autoplay next episode with fast episode transitions
- Multi-audio track support with descriptive labels
- Picture-in-Picture (PiP) mode
- Miniplayer with drag, resize, and auto-hide on pause
- Volume boost beyond 100% (desktop)
- Discord Rich Presence showing title, episode, and playback progress
- External player support on both Android and desktop
- Built-in file manager for viewing all files, with the ability to manually correct misidentified series names and episode numbers

### 🎮 Keybindings

All keybinds are fully customizable via drag-and-drop in the keybinds UI (`` ` ``).

| Key | Action                             |
|-----|------------------------------------|
| `S` | Skip opening (seek forward 90s)    |
| `R` | Seek backwards 90s                 |
| `→` / `←` | Seek forward / backward 2 seconds  |
| `↑` / `↓` / `Scroll` | Increase / decrease volume         |
| `M` | Mute                               |
| `C` | Cycle subtitle tracks              |
| `F` | Toggle fullscreen                  |
| `P` | Toggle Picture-in-Picture          |
| `N` / `B` | Next / previous episode or file    |
| `O` | View anime details                 |
| `V` | Toggle volume limit boost          |
| `[` / `]` | Increase / decrease playback speed |
| `\` | Reset playback speed               |
| `I` | Show video stats                   |
| `H` | Open file manager                  |
| `,` / `Shift+,` | Subtitle delay -0.1s / -1.0s       |
| `.` / `Shift+.` | Subtitle delay +0.1s / +1.0s       |
| `` ` `` | Open keybinds editor               |

## ⚙️ **Installation**

### 🐧 **Linux Installation**:

#### Arch:
```bash
paru -S shiru
```

Or if you use yay:

```bash
yay -S shiru
```

#### Debian/Ubuntu:
1. 🔗 Download the `linux-Shiru-version.deb` from the [releases page](https://github.com/RockinChaos/Shiru/releases/latest).
2. 📦 Install using the package manager:

    ```bash
    apt install linux-Shiru-*.deb
    ```

---

### 🖥️ Windows Installation:
#### Option 1: 💨 Install via Winget
For Windows 10 **1809** or later, or Windows 11:
```bash
winget install shiru
```

#### Option 2: 🔄 Installer or Portable Version
1. 🔗 Download from the [releases page](https://github.com/RockinChaos/Shiru/releases/latest):
   - **Installer:** `win-Shiru-vx.x.x-installer.exe`
   - **Portable:** `win-Shiru-vx.x.x-portable.exe` *(No installation required, just run it)*

## 🔧 Building & Development

Credit to [NoCrypt](https://github.com/NoCrypt) for doing the legwork on this.

### 📋 Requirements:
- PNPM (or any package manager)
- NodeJS 22.21.1
- Visual Studio 2022 (if on Windows)
- Docker (with WSL on Windows)
- ADB & Android Studio (SDK 34)
- Java 21 (JDK)

###  💻 Building for PC (Electron):
1. Navigate to the Electron directory:
   ```bash
   cd electron
   ```
2. Install dependencies:
   ```bash
   pnpm install
   ```
3. Start development:
   ```bash
   pnpm start
   ```
4. Build for release:
   ```bash
   pnpm build
   ```

---

### 📱 Building for Android (Capacitor):
1. Navigate to the Capacitor directory:
   ```bash
   cd capacitor
   ```
2. Install dependencies:
   ```bash
   pnpm install
   ```
3. Run the doctor to check for missing dependencies:
   ```bash
   pnpm exec cap doctor
   ```
4. (First time only) Build native code:
   - Windows:
     ```bash
     pnpm build:native-win
     ```
   - Linux:
     ```bash
     pnpm build:native
     ```
5. (Optional) Generate assets:
   ```bash
   pnpm build:assets
   ```
6. Open the Android project:
   ```bash
   pnpm exec cap open android
   ```
7. Connect your device with ADB and start development:
   ```bash
   pnpm dev:start
   ```
8. Build the app for release (APK will not be [signed](https://github.com/NoCrypt/sign-android)):
   ```bash
   pnpm build:app
   ```

---

## 📜 License

This project follows the [GPLv3 License](../LICENSE).

```

### File: client\package.json
```json
{
  "name": "client",
  "private": true,
  "dependencies": {
    "bittorrent-tracker": "^11.2.2",
    "matroska-metadata": "^1.0.8",
    "parse-torrent": "^11.0.19",
    "uint8-util": "^2.2.6",
    "webtorrent": "^2.8.5"
  }
}

```

### File: common\package.json
```json
{
  "name": "common",
  "private": true,
  "dependencies": {
    "@fontsource-variable/nunito": "^5.2.7",
    "anitomyscript": "github:ThaUnknown/anitomyscript#42290c4b3f256893be08a4e89051f448ff5e9d00",
    "bottleneck": "^2.19.5",
    "browser-event-target-emitter": "^1.0.1",
    "comlink": "^4.4.2",
    "css-loader": "^7.1.4",
    "dompurify": "^3.3.3",
    "fast-deep-equal": "^3.1.3",
    "fuse.js": "^7.1.0",
    "jassub": "1.8.8",
    "js-levenshtein": "^1.1.6",
    "lucide-svelte": "0.455.0",
    "marked": "^17.0.5",
    "p2pt": "github:ThaUnknown/p2pt#modernise",
    "quartermoon": "^1.2.3",
    "rfdc": "^1.4.1",
    "simple-font-select": "^1.0.1",
    "simple-store-svelte": "^1.0.6",
    "svelte": "^4.2.20",
    "svelte-keybinds": "^1.0.9",
    "svelte-loader": "^3.2.4",
    "svelte-persisted-store": "^0.12.0",
    "svelte-sonner": "^0.3.28",
    "video-deband": "^1.0.9"
  }
}

```

### File: electron\package.json
```json
{
  "name": "shiru",
  "version": "6.5.2",
  "license": "GPL-3.0-or-later",
  "private": true,
  "author": "RockinChaos <RockinChaos@users.noreply.github.com>",
  "description": "A personal anime library manager for watching and tracking your collection in real time. Lightweight, powerful, and paws-itively fast. No waiting required!",
  "main": "build/main.js",
  "homepage": "https://github.com/RockinChaos/Shiru#readme",
  "scripts": {
    "start": "cross-env NODE_ENV=development webpack build && concurrently --kill-others \"npm run web:watch\" \"npm run electron:start\"",
    "web:watch": "webpack serve",
    "web:build": "cross-env NODE_ENV=production webpack build",
    "electron:start": "electron ./build/main.js",
    "build": "npm run web:build && electron-builder",
    "electron:build": "electron-builder",
    "publish": "npm run web:build && electron-builder -p always"
  },
  "devDependencies": {
    "@electron/notarize": "^3.1.0",
    "common": "workspace:*",
    "client": "workspace:*",
    "electron": "39.2.7",
    "electron-builder": "^26.0.12",
    "electron-log": "^5.4.3",
    "electron-updater": "^6.8.3"
  },
  "dependencies": {
    "@paymoapp/electron-shutdown-handler": "^1.1.2",
    "@xhayper/discord-rpc": "^1.3.1",
    "concurrently": "^9.2.1",
    "jimp": "0.22.12",
    "powertoast": "^3.0.0",
    "utp-native": "^2.5.3"
  },
  "standard": {
    "ignore": [
      "bundle.js",
      "bundle.map.js"
    ],
    "env": [
      "browser",
      "node"
    ]
  },
  "build": {
    "directories": {
      "buildResources": "buildResources"
    },
    "asarUnpack": "**/*.node",
    "electronDownload": {
      "mirror": "https://craftationgaming.com/api/packages/electron/",
      "customDir": "39.2.7"
    },
    "protocols": {
      "name": "shiru",
      "schemes": [
        "shiru",
        "magnet"
      ]
    },
    "fileAssociations": [
      {
        "ext": "torrent",
        "name": "Torrent File",
        "description": "Play and manage your personal torrent media",
        "role": "Viewer"
      }
    ],
    "publish": [
      {
        "provider": "github",
        "owner": "RockinChaos",
        "repo": "shiru"
      }
    ],
    "appId": "com.github.rockinchaos.shiru",
    "productName": "Shiru",
    "files": [
      "build/**/*",
      "!node_modules/**/*.{mk,a,o,h}"
    ],
    "mac": {
      "artifactName": "${os}-${productName}-v${version}.${ext}",
      "singleArchFiles": "node_modules/+(register-scheme|utp-native|fs-native-extensions)/**",
      "category": "public.app-category.video",
      "darkModeSupport": true,
      "icon": "buildResources/icon.icns",
      "hardenedRuntime": true,
      "notarize": false,
      "entitlements": "buildResources/entitlements.mac.plist",
      "target": [
        {
          "arch": "universal",
          "target": "default"
        }
      ]
    },
    "win": {
      "artifactName": "${os}-${productName}-v${version}.${ext}",
      "icon": "buildResources/icon.ico",
      "target": [
        "nsis",
        "portable"
      ]
    },
    "linux": {
      "artifactName": "${os}-${productName}-v${version}.${ext}",
      "icon": "buildResources/icon.png",
      "category": "AudioVideo;Video",
      "description": "A personal anime library manager for watching and tracking your collection in real time. Lightweight, powerful, and paws-itively fast. No waiting required!",
      "maintainer": "RockinChaos <RockinChaos@users.noreply.github.com>",
      "desktop": {
        "entry": {
          "Comment": "A personal anime library manager for watching and tracking your collection in real time. Lightweight, powerful, and paws-itively fast. No waiting required!",
          "Keywords": "anime",
          "MimeType": "x-scheme-handler/shiru;"
        }
      },
      "target": [
        {
          "arch": "x64",
          "target": "AppImage"
        },
        {
          "arch": "x64",
          "target": "deb"
        }
      ]
    },
    "portable": {
      "artifactName": "${os}-${productName}-v${version}-portable.${ext}"
    },
    "nsis": {
      "allowToChangeInstallationDirectory": true,
      "oneClick": false,
      "artifactName": "${os}-${productName}-v${version}-installer.${ext}"
    }
  }
}

```

### File: extensions\package.json
```json
{
  "name": "@rockinchaos/example",
  "version": "1.0.0",
  "description": "Example extensions for Shiru that returns generated dummy results based on query parameters",
  "license": "GPLv3",
  "main": "index.json",
  "types": "sources/index.d.ts"
}
```

### File: jsconfig.json
```json
{
  "compilerOptions": {
    "checkJs": true,
    "target": "ESNext",
    "moduleResolution": "node",
    "module": "ESNext",
    "allowSyntheticDefaultImports": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "resolveJsonModule": true,
    "sourceMap": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "paths": {
      "@/*": ["./common/*"],
      "three": ["./types.d.ts"],
      "rxjs": ["./types.d.ts"],
      "@client/*": ["./client/*"],
      "debug": ["./common/modules/debug.js"],
      "webtorrent-client": ["./client/core/webtorrent.js"],
      "http-tracker": ["./node_modules/bittorrent-tracker/lib/client/http-tracker.js"]
    },
    "types": ["@cloudflare/workers-types", "./types.d.ts"]
  },
  "exclude": [
    "node_modules", "dist", "build", "git_modules", ".svelte-kit", "public", "android", "@types/three",
    "**/node_modules", "**/dist", "**/build", "**/git_modules", "**/.svelte-kit", "**/public", "**/android", "**/@types/three",
    "**/node_modules/*", "**/dist/*", "**/build/*", "**/git_modules/*", "**/.svelte-kit/*", "**/public/*", "**/android/*", "**@types/three/*.d.ts"
  ]
}
```

### File: pnpm-workspace.yaml
```yaml
packages:
  - './*'

```

### File: types.d.ts
```ts
import type { SvelteComponentTyped } from 'svelte'

declare module '*.svelte' {
  export default SvelteComponentTyped
}

```

### File: .github\CODE_OF_CONDUCT.md
```md
# 🤝 Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
 advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
 address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
 professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

## Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported through GitHub by opening an issue or using the appropriate contact
channels provided in this repository. All complaints will be reviewed and
investigated, with actions taken as deemed necessary and appropriate to the
circumstances. The project team will maintain confidentiality with regard to
the reporter of an incident to the fullest extent possible.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at https://www.contributor-covenant.org/version/1/4/code-of-conduct.html

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see
https://www.contributor-covenant.org/faq
```

### File: .github\CONTRIBUTING.md
```md
# 🛠️ Contributing to Shiru

First off, thank you for considering contributing to **Shiru**!  
Whether you're fixing a bug, adding a feature, improving performance, or updating docs, all contributions help make the project better for everyone.
By participating in this project, you agree to maintain a respectful and inclusive environment. Be kind, professional, and considerate in all interactions.

## 📑 Table of Contents

- [How Can I Contribute?](#-how-can-i-contribute)
    - [Reporting Bugs](#-reporting-bugs)
    - [Suggesting Features](#-suggesting-features)
    - [Asking Questions](#-asking-questions)
    - [Contributing Code](#-contributing-code)
- [Development Setup](#-development-setup)
- [Pull Request Process](#-pull-request-process)
- [Style Guidelines](#-style-guidelines)
- [Community](#-community)
- [Code of Conduct](https://github.com/RockinChaos/Shiru?tab=coc-ov-file)

## 🚀 How Can I Contribute?

### 🐛 Reporting Bugs

Found a bug? Help us fix it by creating a detailed bug report:

1. **Check existing issues** - Search the [issue tracker](https://github.com/RockinChaos/Shiru/issues?q=is%3Aissue%20label%3Abug) to see if the bug has already been reported
2. **Use the bug report template** - Click "New Issue" and select "Bug Report"
3. **Provide details** - Include:
    - Your operating system and architecture
    - App version
    - Steps to reproduce the bug
    - Expected vs actual behavior
    - Screenshots if applicable

### ✨ Suggesting Features

Have an idea to improve Shiru? We'd love to hear it:

1. **Check existing requests** - Search the [issue tracker](https://github.com/RockinChaos/Shiru/issues?q=is%3Aissue%20label%3Aenhancement) to avoid duplicates
2. **Use the feature request template** - Click "New Issue" and select "Feature Request"
3. **Be specific** - Clearly describe:
    - What problem does the feature solve
    - How it should work
    - Which platforms does it apply to
    - Why it would be valuable

### ❓ Asking Questions

Need help or clarification? We're here to assist:

1. **Check the FAQ** - Visit our [frequently asked questions](https://github.com/RockinChaos/Shiru/wiki/faq)
2. **Use the assistance request template** - Click "New Issue" and select "Assistance Request"
3. **Be clear** - Describe what you're trying to do and what you've already tried

### 💻 Contributing Code

Want to contribute code? Great! Here's how:

1. **Find or create an issue** - Ensure there's an issue tracking the work you plan to contribute
2. **Fork the repository** - Create your own fork to work in
3. **Create a branch** - Use a descriptive branch name like `fix-notification-crash` or `feature-custom-sounds`
4. **Make your changes** - Write clean, well-documented code
5. **Test thoroughly** - Ensure your changes work on relevant platforms
6. **Submit a pull request** - Reference the related issue in your PR description

## 🔧 Development Setup

### 📋 Prerequisites

- **PNPM** (or any package manager)
- **Node.js 22.21.1**
- **Visual Studio 2022** (if on Windows)
- **Docker** (with WSL if on Windows)
- **ADB & Android Studio** (SDK 34) - for Android development
- **Java 21 (JDK)** - for Android development

### 🏗️ Building from Source

#### 🖥️ Desktop (Windows/Linux/macOS)

1. Clone the repository:
```bash
git clone https://github.com/RockinChaos/Shiru.git
cd Shiru
```

2. Navigate to the Electron directory:
```bash
cd electron
```

3. Install dependencies:
```bash
pnpm install --frozen-lockfile
```

4. Start development mode:
```bash
npm run start
```

5. Build for release:
```bash
npm run build
```

#### 📱 Android

1. Clone the repository (if you haven't already):
```bash
git clone https://github.com/RockinChaos/Shiru.git
cd Shiru
```

2. Navigate to the Capacitor directory:
```bash
cd capacitor
```

3. Install dependencies:
```bash
pnpm install --frozen-lockfile
```

4. Check for missing dependencies:
```bash
pnpm exec cap doctor
```

5. **First time only** - Build native code:
    - Windows:
      ```bash
      pnpm build:native-win
      ```
    - Linux:
      ```bash
      pnpm build:native
      ```

6. **(Optional)** Generate assets:
```bash
pnpm build:assets
```

7. Open the Android project in Android Studio:
```bash
pnpm exec cap open android
```

8. Connect your device with ADB and start development:
```bash
pnpm dev:start
```

9. Build the app for release (APK will not be [signed](https://github.com/NoCrypt/sign-android)):
```bash
pnpm build:app
```

### 📝 Platform-Specific Notes

**Android:**
- Ensure ADB is properly configured and your device is connected (you can also use emulation)
- SDK 34 is required
- Release builds require signing (see [NoCrypt's signing guide](https://github.com/NoCrypt/sign-android))

**Windows:**
- Docker requires WSL to be installed and configured
- Use the Windows-specific native build command

> [!NOTE]
> **Credit:** Special thanks to [NoCrypt](https://github.com/NoCrypt) for the initial Android build setup!

## 🔄 Pull Request Process

1. **Update documentation** - If your changes affect user-facing features, update relevant documentation
2. **Follow code style** - Ensure your code follows the project's style guidelines (see below)
3. **Write clear commit messages** - Use descriptive messages that explain what and why
4. **Keep PRs focused** - One feature or fix per pull request
5. **Be responsive** - Address review feedback promptly and professionally
6. **Wait for approval** - A maintainer will review and merge your PR

### ⏱️ What to Expect

- **Review time** - We aim to review PRs within a few days, but it may take longer depending on complexity
- **Feedback** - We may request changes or ask questions - this is normal and helps maintain code quality
- **Merge** - Once approved, a maintainer will merge your PR

## 📐 Style Guidelines

### ✍️ Code Style

- Use consistent indentation (spaces/tabs as per project standard)
- Write clear, self-documenting code with meaningful variable names
- Add comments for complex logic
- Keep functions focused and reasonably sized

### 📝 Commit Messages

- Keep the **first line under ~40 characters**
- Start with a **type prefix** (`feat:`, `fix:`, `chore:`, `refactor:`, `docs:`, etc.)
- Reference issues when relevant (`fix: resolve notification crash (#123)`)
- Include a description if applicable

### 🧪 Testing

- Test your changes on all relevant platforms before submitting
- Include steps to test in your PR description
- Report any edge cases or limitations

## 🌐 Community

### 💬 Getting Help

- **Issues** - For bugs, features, and questions
- **Wiki** - Check the [project wiki](https://github.com/RockinChaos/Shiru/wiki) for documentation

### 🏆 Recognition

All contributors are valued! Your contributions will be recognized in release notes and commit history.

## ⚖️ Legal

By contributing to Shiru, you agree that your contributions will be licensed under the same license as the project.

> [!IMPORTANT]
> All contributions must comply with applicable laws. Do not include or promote pirated content, copyrighted material without permission, or any illegal activity. Contributors are expected to respect intellectual property rights.

---

Thank you for contributing to Shiru! Your help makes this project better for everyone. 🎉
```

### File: .github\pull_request_template.md
```md
## Description

<!-- Provide a clear and concise description of what this PR does and if it fixes anything. Use "Fixes #123" or "Closes #123" to auto-close the issue when merged -->


## Type of Change

<!-- Mark the relevant option with an "x" -->

- [ ] 🐛 **Fix** — Bug or regression fix (`fix:`)
- [ ] ✨ **Feature** — New feature or enhancement (`feat:`)
- [ ] 🧹 **Chore** — Build, CI, or tooling update (`chore:`)
- [ ] 🧠 **Refactor** — Code improvement without functional change (`refactor:`)
- [ ] 🧾 **Docs** — Documentation only (`docs:`)
- [ ] ⚙️ **Other** — Please explain below


## Platforms Affected

<!-- Mark all platforms this change affects -->

- [ ] 🪟 **Windows**
- [ ] 🐧 **Linux**
- [ ] 🍎 **macOS**
- [ ] 📱 **Android**


## Testing

<!-- Describe how you tested your changes and the environments used.
Example:
- [x] Verified on Windows 11
- [x] Tested Android build via Capacitor
- [x] Confirmed tray icon now persists after wake
-->


### Test Configuration:
- **OS:** <!-- e.g., Windows 11, macOS Sonoma, Android 14 -->
- **Architecture:** <!-- e.g., x64, arm64, arm64-v8a -->
- **App Version:** <!-- e.g., v6.0.0 -->


### Steps to Test:
1.
2.
3.


## Checklist

<!-- Mark completed items with an "x" -->

- [ ] My code is my own original work
- [ ] My changes generate no new warnings
- [ ] I have performed a self-review of my own code
- [ ] My code follows the style guidelines of this project
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation (if applicable)


## Screenshots/Videos

<!-- If applicable, add screenshots or videos to demonstrate the changes -->


## Additional Notes

<!-- Any additional information, context, or considerations for reviewers -->
```

### File: common\css.css
```css
:root {
  --ui-scale: 1;
  --default-html-font-size: 48%;
  --default-html-font-size-1600: 50%;
  --default-html-font-size-1920: 62.5%;
  --base-html-font-size: calc(var(--default-html-font-size) * var(--ui-scale));
  --base-html-font-size-1600: calc(var(--default-html-font-size-1600) * var(--ui-scale));
  --base-html-font-size-1920: calc(var(--default-html-font-size-1920) * var(--ui-scale));
  --tooltip-width: 17rem;
  --card-border-width: 0;
  --sidebar-border-width: 0;
  --input-border-width: 0;
  --sidebar-minimised: 0px;
  --sidebar-width: 0px;
  --navbar-height: 7rem;
  --statusbar-height: 28px;
  --safe-area-top: 0px;
  --safe-area-left: 0px;

  --accent-color: #e5204c;
  --highlight-color: #FFFFFF !important;
  --current-color: #3DB4F2 !important;
  --planning-color: #F79A63 !important;
  --completed-color-hue: 110deg;
  --completed-color-saturation: 60%;
  --completed-hsl: var(--completed-color-hue), var(--completed-color-saturation), 58%;
  --completed-color: hsl(var(--completed-hsl)) !important;
  --completed-dim-hsl: var(--completed-color-hue), var(--completed-color-saturation), 42%;
  --completed-color-dim: hsl(var(--completed-dim-hsl)) !important;
  --paused-color: #FA7A7A !important;
  --repeating-color: #3BAEEA !important;
  --dropped-color: #E85D75 !important;
  --notify-color: #Af68FA !important;
  --dark-color-base-hue: 220deg !important;
  --dark-color-base-saturation: 10% !important;
  --dark-color-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 10% !important;
  --dark-color-light-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 14%;
  --dark-color-very-light-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 16%;
  --dark-color-dim-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 8%;
  --dark-color-very-dim-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 4%;
  --dm-shadow: 0px 4px 7px hsla(var(--black-color-hsl), 0.25);
  --gray-color-base-hue: 216;
  --gray-color-light: hsl(var(--gray-color-light-hsl));
  --gray-color-light-hsl: var(--gray-color-base-hue), 10%, 28%;
  --gray-color-very-dim-hsl: var(--gray-color-base-hue), var(--gray-color-base-saturation), 35%;
  --green-color-base-hue: 106;
  --green-color-base-saturation: 100%;
  --green-color-hsl: var(--green-color-base-hue), var(--green-color-base-saturation), 27%;
  --green-color-light-hsl: var(--green-color-base-hue), var(--green-color-base-saturation), 40%;
  --red-color-very-dim-hsl: var(--red-color-base-hue), 66%, 15%;
  --white-color-hue: 0deg;
  --white-color-saturation: 0%;
  --white-color-dim-hsl: var(--white-color-hue), var(--white-color-saturation), 60%;
  --white-color-dim: hsl(var(--white-color-dim-hsl));
  --white-color-very-dim-hsl: var(--white-color-hue), var(--white-color-saturation), 50%;
  --white-color-very-dim: hsl(var(--white-color-very-dim-hsl));
  --warning-color-base-hue: 48;
  --warning-color-base-saturation: 80%;
  --warning-color-hsl: var(--warning-color-base-hue), var(--warning-color-base-saturation), 46%;
  --warning-color: hsl(var(--warning-color-hsl)) !important;
  --warning-color-dim-hsl: var(--warning-color-base-hue), var(--warning-color-base-saturation), 31%;
  --warning-color-dim: hsl(var(--warning-color-dim-hsl)) !important;
  --warning-color-very-dim-hsl: var(--warning-color-base-hue), var(--warning-color-base-saturation), 19%;
  --warning-color-very-dim: hsl(var(--warning-color-very-dim-hsl)) !important;
  --error-color-hue: 0deg;
  --error-color-saturation: 89%;
  --error-hsl: var(--error-color-hue), var(--error-color-saturation), 15%;
  --error-color: hsl(var(--error-hsl));
  --error-color-light-hsl: var(--error-color-hue), var(--error-color-saturation), 25%;
  --error-color-light: hsl(var(--error-color-light-hsl));
  --error-color-very-light-hsl: var(--error-color-hue), var(--error-color-saturation), 35%;
  --error-color-very-light: hsl(var(--error-color-very-light-hsl));
  --myanimelist-color-hue: 221deg;
  --myanimelist-color-saturation: 57%;
  --myanimelist-color-hsl: var(--myanimelist-color-hue), var(--myanimelist-color-saturation), 40%;
  --myanimelist-color: hsl(var(--myanimelist-color-hsl));
  --myanimelist-color-light-hsl: var(--myanimelist-color-hue), var(--myanimelist-color-saturation), 55%;
  --myanimelist-color-light: hsl(var(--myanimelist-color-light-hsl));
  --anilist-color-hue: 215deg;
  --anilist-color-saturation: 25%;
  --anilist-color-hsl: var(--anilist-color-hue), var(--anilist-color-saturation), 21%;
  --anilist-color: hsl(var(--anilist-color-hsl));
  --anilist-color-light-hsl: var(--anilist-color-hue), var(--anilist-color-saturation), 35%;
  --anilist-color-light: hsl(var(--anilist-color-light-hsl));
  --tertiary-color-hue: 217deg;
  --tertiary-color-saturation: 77%;
  --tertiary-color-hsl: var(--tertiary-color-hue), var(--tertiary-color-saturation), 54%;
  --tertiary-color: hsl(var(--tertiary-color-hsl)) !important;
  --tertiary-color-light-hsl: var(--tertiary-color-hue), var(--tertiary-color-saturation), 64%;
  --tertiary-color-light: hsl(var(--tertiary-color-light-hsl)) !important;
  --tertiary-color-very-light-hsl: var(--tertiary-color-hue), var(--tertiary-color-saturation), 79%;
  --tertiary-color-very-light: hsl(var(--tertiary-color-very-light-hsl)) !important;
  --tertiary-color-dim-hsl: var(--tertiary-color-hue), var(--tertiary-color-saturation), 30%;
  --tertiary-color-dim: hsl(var(--tertiary-color-dim-hsl)) !important;
  --quaternary-color: #98C379 !important;
  --quinary-color: #D7060A !important;
  --senary-color: #FFD600 !important;
  --septenary-color: #8927FF !important;
  --octonary-color: #FF6B35 !important;
  --denary-color: #BC2023 !important;
  --undenary-color-hue: 240deg;
  --undenary-color-saturation: 100%;
  --undenary-color-hsl: var(--undenary-color-hue), var(--undenary-color-saturation), 90%;
  --undenary-color: hsl(var(--undenary-color-hsl)) !important;
  --undenary-color-dim-hsl: var(--undenary-color-hue), var(--undenary-color-saturation), 84%;
  --undenary-color-dim: hsl(var(--undenary-color-dim-hsl)) !important;
  --duodenary-color: #FFFFF0 !important;
  --quattuordenary-color: #FA68B6 !important;
  --nonary-color: #F7931E !important;
  --quindenary-color: #FFB088 !important;

  --border-color-sp: hsla(var(--gray-color-dim-hsl), 0.2);
  --dm-input-border-color: none;
  --dm-link-text-color: var(--dm-muted-text-color) !important;
  --dm-link-text-color-hover: var(--dm-text-color) !important;
  --skeleton-swipe-background: var(--dark-color-light);
  --sidebar-gradient: linear-gradient(90deg, var(--dark-color) 15.62%, hsla(var(--dark-color-hsl), 0.92) 36.46%, hsla(var(--dark-color-hsl), 0.62) 70.83%, hsla(var(--black-color-hsl), 0) 100%);
  --banner-gradient-bottom: linear-gradient(0deg, var(--dark-color) 0%, hsla(var(--dark-color-hsl), 0) 15%, hsla(var(--dark-color-hsl), 0) 100%);
  --banner-gradient-left: linear-gradient(90deg, var(--dark-color) 0%, rgba(23, 25, 29, 0.5) 75%, rgba(25, 28, 32, 0) 100%);
  --torrent-card-gradient: linear-gradient(90deg, hsla(var(--dark-color-hsl), 0.98) 25%, hsla(var(--dark-color-light-hsl), 0.85) 100%);
  --torrent-banner-gradient: linear-gradient(0, var(--dark-color-dim) 15%, hsla(var(--dark-color-very-dim-hsl), 0.64) 85%), linear-gradient(to left, var(--dark-color-dim) 0, transparent 1%);
  --notification-card-gradient: linear-gradient(90deg, hsla(var(--dark-color-light-hsl), 0.98) 32%, hsla(var(--dark-color-hsl), 0.85) 100%);
  --episode-card-gradient: linear-gradient(180deg, hsla(var(--black-color-hsl), 0) 77.08%, hsla(var(--dark-color-light-hsl), 0.7) 100%);
  --episode-preview-card-gradient: linear-gradient(180deg, hsla(var(--black-color-hsl), 0) 0%, hsla(var(--black-color-hsl), 0) 80%, var(--dark-color-light) 100%);
  --preview-card-end-gradient: linear-gradient(180deg, hsla(var(--black-color-hsl), 0) 0%, hsla(var(--black-color-hsl), 0) 85%, hsla(var(--dark-color-light-hsl), 0.85) 95%, var(--dark-color-light) 98%);
  --preview-card-trailer-gradient: linear-gradient(180deg, hsla(var(--black-color-hsl), 0) 0%, hsla(var(--black-color-hsl), 0) 85%, hsla(var(--dark-color-light-hsl), 0.85) 95%, var(--dark-color-light) 98%, var(--dark-color-light) 100%);
  --section-end-gradient: linear-gradient(270deg, hsla(var(--dark-color-hsl), 1) 0%, hsla(var(--dark-color-light-hsl), 0) 100%);

  --theme-color: var(--dark-color) !important;
  color-scheme: dark;
}

@font-face {
  font-family: "Roboto";
  src: /* webpackIgnore: true */ url(Roboto.ttf) format("truetype");
  unicode-range: U+0000, U+0002, U+0009, U+000D, U+0020-007E, U+00A0-0377,
      U+037A-037F, U+0384-038A, U+038C, U+038E-03A1, U+03A3-03E1,
      U+03F0-052F, U+1AB0-1ABE, U+1D00-1DF5, U+1DFC-1F15, U+1F18-1F1D,
      U+1F20-1F45, U+1F48-1F4D, U+1F50-1F57, U+1F59, U+1F5B, U+1F5D,
      U+1F5F-1F7D, U+1F80-1FB4, U+1FB6-1FC4, U+1FC6-1FD3, U+1FD6-1FDB,
      U+1FDD-1FEF, U+1FF2-1FF4, U+1FF6-1FFE, U+2000-2027, U+202F-205F,
      U+2070-2071, U+2074-208E, U+2090-209C, U+20A0-20BE, U+20DB-20DC,
      U+20E3, U+20E8, U+20F0, U+2100-2101, U+2103, U+2105-2106, U+2109,
      U+2113, U+2116-2117, U+211E-2123, U+2125-2126, U+212A-212B, U+212E,
      U+2132, U+213B, U+214D, U+214F-2189, U+2191, U+2193, U+2202, U+2206,
      U+220F, U+2211-2212, U+221A, U+221E, U+222B, U+2248, U+2260,
      U+2264-2265, U+2423, U+25CA, U+2669-266F, U+27E6-27EF, U+2B4E-2B4F,
      U+2B5A-2B5F, U+2C60-2C7F, U+2DE0-2E42, U+A640-A69D, U+A69F,
      U+A700-A7AD, U+A7B0-A7B1, U+A7F7-A7FF, U+A92E, U+AB30-AB5F,
      U+AB64-AB65, U+EE01-EE02, U+F6C3, U+FB00-FB06, U+FE20-FE2D, U+FEFF,
      U+FFFC-FFFD, U+1F16A-1F16B;
}

@font-face {
  font-family: "Twemoji";
  src: /* webpackIgnore: true */ url(Twemoji.ttf) format("truetype");
  unicode-range: U+1F1E6-1F1FF;
}

.dark-mode {
  background-color: var(--dark-color) !important;
}

.h-0 {
  height: 0;
}
.h-3 {
  height: 3rem !important;
}
.h-15 {
  height: 1.5rem;
}
.h-20 {
  height: 2rem !important;
}
.h-30 {
  height: 3rem;
}
.h-40 {
  height: 4rem;
}
.h-80 {
  height: 8rem;
}
.h-140 {
  height: 14rem;
}
.h-165 {
  height: 16.5rem !important;
}
.h-270 {
  height: 27rem;
}
.hm-20 {
  min-height: 20rem !important;
}
.mh-full {
  max-height: 100%;
}

.w-20 {
  width: 2rem;
}
.w-30 {
  width: 3rem !important;
}
.w-40 {
  width: 4rem;
}
.w-80 {
  width: 8rem;
}
.w-90 {
  width: 9rem;
}
.w-115 {
  width: 11.5rem;
}
.w-120 {
  width: 12rem;
}
.w-130 {
  width: 13rem;
}
.w-160 {
  width: 16rem;
}
.w-170 {
  width: 17rem;
}
.w-180 {
  width: 18rem;
}
.w-220 {
  width: 22rem;
}
.w-800 {
  width: 80rem !important
}
.w-1000 {
  width: 100rem
}

.rounded-left-block {
  border-radius: var(--base-border-radius) 0 0 var(--base-border-radius) !important;
}

.rounded-right-block {
  border-radius: 0 var(--base-border-radius) var(--base-border-radius) 0 !important;
}

.vwh-90 {
  width: 90vw !important;
  height: 90vh !important;
}

.wh-25 {
  width: 2.5rem;
  height: 2.5rem;
}

.mw-0 {
  min-width: 0;
}
.mw-80 {
  min-width: 8rem !important;
}
.mw-100 {
  min-width: 10rem !important;
}
.mw-120 {
  min-width: 12rem;
}
.mw-150 {
  min-width: 15rem;
}
.mw-180 {
  min-width: 18rem;
}
.mw-200 {
  min-width: 20rem;
}
.mw-220 {
  min-width: 22rem;
}
.mw-350 {
  min-width: 35rem;
}

.wm-250 {
  max-width: 25rem;
}
.wm-600 {
  max-width: 60rem;
}
.wm-1000 {
  max-width: 100rem;
}
.wm-1150 {
  max-width: 115rem;
}
.wm-1200 {
  max-width: 120rem;
}

.hm-250 {
  max-height: 25rem;
}
.hm-400 {
  max-height: 40rem;
}

@media (min-width: 769px) {
  :root {
    --sidebar-minimised: 7rem;
    --sidebar-width: 7rem;
    --navbar-height: 0px;
  }
}

.cr-400 {
  height: 40rem !important;
}
.cr-380 {
  height: 38rem !important;
}
.cover-rotated {
  width: 20rem !important;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-90deg);
}

.d-contents {
  display: contents;
}

.top-100 {
  top: 100%
}

.status-transition {
  transition: height .3s ease 2s, padding .3s ease 2s;
}
.opacity-ts-3 {
  transition: opacity .3s ease-in-out;
}

.scrollbar-none {
  scrollbar-width: none;
}

.flex-1 {
  flex: 1;
}

.line-height-1 {
  line-height: 1;
}

.line-height-normal {
  line-height: normal;
}

.line-2 {
  display: -webkit-box !important;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
}

.line-3 {
  display: -webkit-box !important;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}

.line-4 {
  display: -webkit-box !important;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}

.text-break-word {
  word-break: break-word;
}

* {
  -webkit-tap-highlight-color: transparent;
}

a[href]:active, button:not([disabled], .not-reactive):active:not([data-sonner-toast] > button), fieldset:not([disabled]):active, input:not([disabled], [type='range'], .not-reactive):active, optgroup:not([disabled]):active, option:not([disabled]):active, select:not([disabled]):active, textarea:not([disabled]):active, details:active, [tabindex]:not([disabled], [tabindex="-1"], [aria-hidden="true"], .seekbar, .dropdown, .scoring, .not-reactive):active, [contenteditable]:active, [controls]:active {
  transition: box-shadow 0.1s ease, filter 0.1s ease !important;
  filter: brightness(0.95) contrast(1.05) !important;
  box-shadow: 0 0 2rem hsla(var(--black-color-hsl), 0.1), 0 .4rem .6rem hsla(var(--black-color-hsl), 0.05) !important;
  transform: translateY(0.15rem) !important;
}

.btn-secondary {
  --dm-button-secondary-bg-color: var(--white-color) !important;
  --dm-button-secondary-bg-color-hover: var(--white-color-dim) !important;
  --dm-button-secondary-bg-color-focus: var(--dm-button-secondary-bg-color) !important;
}

[data-sonner-toaster][data-theme='dark'] {
  top: 5rem !important;
  --normal-bg: var(--dark-color) !important;
  --normal-border: none !important;
  --normal-text: var(--dm-base-text-color) !important;

  /* --success-bg: var(--success-color) !important; */
  --success-border: none !important;
  /* --success-text: var(--lm-base-text-color) !important; */

  /* --error-bg: hsl(358, 76%, 10%); */
  --error-border: none !important;
  /* --error-text: hsl(358, 100%, 81%); */
}

[data-sonner-toast] > button {
  position: absolute !important;
  margin-left: 94% !important;
  right: 0 !important;
  margin-top: 1.4rem !important;
  border-radius: .4rem !important;
  border-color: transparent !important;
  background-color: transparent !important;
  color: hsla(var(--white-color-hsl), 0.93) !important;
}

[data-sonner-toast] > button svg {
  width: 2rem !important;
  height: 2rem !important;
  stroke-width: 2.5 !important;
}

[data-sonner-toast] > div:nth-child(2) > div:first-child {
  line-height: 1.1 !important;
}

[data-sonner-toaster] [data-description] {
  white-space: pre-wrap;
}

.first-audio {
  padding-left: 1rem !important;
  padding-right: 1rem !important;
  margin-right: -.3rem !important;
}

.vertical-flip {
  transform: scaleY(-1);
}

.banner-rotated {
    width: 100vh !important;
    height: 100vw !important;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%)
... [TRUNCATED]
```

### File: common\jsconfig.json
```json
{
  "compilerOptions": {
    "checkJs": true,
    "target": "ESNext",
    "moduleResolution": "node",
    "module": "ESNext",
    "allowSyntheticDefaultImports": true,
    "verbatimModuleSyntax": true,
    "isolatedModules": true,
    "resolveJsonModule": true,
    "sourceMap": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "types": ["./types.d.ts"],
    "baseUrl": "./",
    "paths": {
      "@/*": ["./*"],
      "three": ["./types.d.ts"],
      "rxjs": ["./types.d.ts"]
    }
  },
  "exclude": [
    "node_modules", "dist", "build", "git_modules", ".svelte-kit", "public", "android", "@types/three",
    "**/node_modules", "**/dist", "**/build", "**/git_modules", "**/.svelte-kit", "**/public", "**/android", "**/@types/three",
    "**/node_modules/*", "**/dist/*", "**/build/*", "**/git_modules/*", "**/.svelte-kit/*", "**/public/*", "**/android/*", "**@types/three/*.d.ts"
  ]
}
```

### File: common\main.js
```js
import 'quartermoon/css/quartermoon-variables.css'
import '@fontsource-variable/nunito'
import { cacheReady } from '@/modules/cache.js'
import '@/css.css'
import '@/themes.css'
import '@/typography.css'

await cacheReady()
const { default: App } = await import('./App.svelte')
new App({ target: document.body })

```

### File: common\themes.css
```css
:root[data-theme='default-amoled'] {
  --accent-color: #DA0101;
  --highlight-color: #E0E0E0 !important;
  --dark-color-base-hue: 220deg !important;
  --dark-color-base-saturation: 5% !important;
  --dark-color-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 0% !important;
  --dark-color-light-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 5%;
  --dark-color-very-light-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 8%;
  --dark-color-dim-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 3%;
  --dark-color-very-dim-hsl: var(--dark-color-base-hue), var(--dark-color-base-saturation), 4%;
  --dm-shadow: 0px 4px 7px hsla(var(--dark-color-very-light-hsl), 0.25);
  --white-color-hsl: var(--white-color-hue), var(--white-color-saturation), 90%;
  --gray-color-light: hsl(var(--gray-color-light-hsl));
  --gray-color-light-hsl: var(--gray-color-base-hue), 10%, 28%;
  --gray-color-base-hue: 216;
  --primary-color: var(--blue-color-dim);
  --primary-color-light: var(--blue-color);
  --primary-color-dim-hsl: var(--blue-color-base-hue), var(--blue-color-base-saturation), 40%;
  --primary-color-dim: hsl(var(--primary-color-dim-hsl));
  --danger-color: var(--red-color-dim);
  --danger-color-light-hsl: var(--red-color-base-hue), var(--red-color-base-saturation), 50%;
  --danger-color-light: hsl(var(--danger-color-light-hsl));
  --danger-color-dim-hsl: var(--red-color-base-hue), var(--red-color-base-saturation), 40%;
  --danger-color-dim: hsl(var(--danger-color-dim-hsl));
  --skeleton-swipe-background: var(--dark-color-very-light);
}
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

---
id: github.com-minhchi1509-tiktok-bulk-downloader-desk
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:27:59.242929
---

# KNOWLEDGE EXTRACT: github.com_minhchi1509_tiktok-bulk-downloader-desktop-app_0f9a29e9
> **Extracted on:** 2026-04-01 08:14:41
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519314/github.com_minhchi1509_tiktok-bulk-downloader-desktop-app_0f9a29e9

---

## File: `.editorconfig`
```
root = true

[*]
charset = utf-8
indent_style = space
indent_size = 2
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
```

## File: `.gitignore`
```
node_modules
dist
out
.DS_Store
.eslintcache
*.log*
.env
```

## File: `.prettierignore`
```
out
dist
pnpm-lock.yaml
LICENSE.md
tsconfig.json
tsconfig.*.json
```

## File: `.prettierrc.yaml`
```yaml
singleQuote: true
semi: false
printWidth: 100
trailingComma: none
```

## File: `README.md`
```markdown
# Tiktok Bulk Downloader Desktop App

A desktop application for downloading multiple TikTok videos at once.

## Download

Download the latest version from [Releases](https://github.com/minhchi1509/tiktok-bulk-downloader-desktop-app/releases).

| Platform | File                                     |
| -------- | ---------------------------------------- |
| Windows  | `tiktok-bulk-downloader-x.x.x-setup.exe` |
| macOS    | `tiktok-bulk-downloader-x.x.x.dmg`       |
| Linux    | `tiktok-bulk-downloader-x.x.x.AppImage`  |

## Installation Notes

### macOS

> ⚠️ **Important:** Since this app is not signed with an Apple Developer certificate, macOS may show a warning: **"Tiktok Bulk Downloader" is damaged and can't be opened.**

**To fix this, run the following command in Terminal after installing:**

```bash
xattr -cr /Applications/Tiktok\ Bulk\ Downloader.app
```

Or if you installed it elsewhere:

```bash
xattr -cr /path/to/Tiktok\ Bulk\ Downloader.app
```

Then open the app again.

### Linux

Make the AppImage executable before running:

```bash
chmod +x tiktok-bulk-downloader-x.x.x.AppImage
./tiktok-bulk-downloader-x.x.x.AppImage
```

---

## Development

### Install

```bash
$ npm install
```

### Development

```bash
$ npm run dev
```

### Build

```bash
# For windows
$ npm run build:win

# For macOS
$ npm run build:mac

# For Linux
$ npm run build:linux
```
```

## File: `dev-app-update.yml`
```yaml
provider: generic
url: https://example.com/auto-updates
updaterCacheDirName: electron-app-updater
```

## File: `electron-builder.yml`
```yaml
appId: com.minhchi.tiktokbulkdownloader
productName: Tiktok Bulk Downloader
electronFuses:
  enableEmbeddedAsarIntegrityValidation: true
  onlyLoadAppFromAsar: true
directories:
  buildResources: build
files:
  - '!**/.vscode/*'
  - '!src/*'
  - '!electron.vite.config.{js,ts,mjs,cjs}'
  - '!{.eslintcache,eslint.config.mjs,.prettierignore,.prettierrc.yaml,dev-app-update.yml,CHANGELOG.md,README.md}'
  - '!{.env,.env.*,.npmrc,pnpm-lock.yaml}'
  - '!{tsconfig.json,tsconfig.node.json,tsconfig.web.json}'
asarUnpack:
  - resources/**
win:
  executableName: Tiktok Bulk Downloader
  icon: resources/icon.png
  target: nsis
nsis:
  artifactName: ${name}-${version}-setup.${ext}
  shortcutName: ${productName}
  uninstallDisplayName: ${productName}
  createDesktopShortcut: always
  oneClick: false
  allowToChangeInstallationDirectory: true
  deleteAppDataOnUninstall: true
mac:
  # entitlementsInherit: build/entitlements.mac.plist
  extendInfo:
    - NSCameraUsageDescription: Application requests access to the device's camera.
    - NSMicrophoneUsageDescription: Application requests access to the device's microphone.
    - NSDocumentsFolderUsageDescription: Application requests access to the user's Documents folder.
    - NSDownloadsFolderUsageDescription: Application requests access to the user's Downloads folder.
  notarize: false
  target:
    - dmg
dmg:
  artifactName: ${name}-${version}.${ext}
  icon: resources/icon.icns
linux:
  target:
    - AppImage
  maintainer: Minh Chi
  category: Utility
  icon: resources/512x512.png
appImage:
  artifactName: ${name}-${version}.${ext}
npmRebuild: false
publish:
  provider: github
  owner: minhchi1509
  repo: tiktok-bulk-downloader-desktop-app
```

## File: `electron.vite.config.ts`
```typescript
import { resolve } from 'path'
import { defineConfig } from 'electron-vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import svgr from 'vite-plugin-svgr'

export default defineConfig({
  main: {
    resolve: {
      alias: {
        '@shared': resolve('src/shared'),
        '@main': resolve('src/main')
      }
    }
  },
  preload: {
    resolve: {
      alias: {
        '@shared': resolve('src/shared')
      }
    }
  },
  renderer: {
    resolve: {
      alias: {
        '@renderer': resolve('src/renderer/src'),
        '@shared': resolve('src/shared')
      }
    },
    plugins: [react(), tailwindcss(), svgr()]
  }
})
```

## File: `eslint.config.mjs`
```
import { defineConfig } from 'eslint/config'
import eslintConfigPrettier from '@electron-toolkit/eslint-config-prettier'
import eslintPluginReact from 'eslint-plugin-react'
import eslintPluginReactHooks from 'eslint-plugin-react-hooks'
import eslintPluginReactRefresh from 'eslint-plugin-react-refresh'

export default defineConfig(
  { ignores: ['**/node_modules', '**/dist', '**/out'] },
  tseslint.configs.recommended,
  eslintPluginReact.configs.flat.recommended,
  eslintPluginReact.configs.flat['jsx-runtime'],
  {
    settings: {
      react: {
        version: 'detect'
      }
    }
  },
  {
    files: ['**/*.{ts,tsx}'],
    plugins: {
      'react-hooks': eslintPluginReactHooks,
      'react-refresh': eslintPluginReactRefresh
    },
    rules: {
      ...eslintPluginReactHooks.configs.recommended.rules,
      ...eslintPluginReactRefresh.configs.vite.rules
    }
  },
  eslintConfigPrettier
)
```

## File: `package.json`
```json
{
  "name": "tiktok-bulk-downloader",
  "version": "1.0.13",
  "description": "Tiktok Bulk Video Downloader - Desktop App for downloading multiple Tiktok videos at once.",
  "main": "./out/main/index.js",
  "author": "MinhChi1509",
  "homepage": "https://toptop-api.minhchi.id.vn",
  "license": "MIT",
  "keywords": [
    "TikTok",
    "Bulk Downloader"
  ],
  "repository": {
    "type": "git",
    "url": "git+https://github.com/minhchi1509/tiktok-bulk-downloader-desktop-app.git"
  },
  "scripts": {
    "format": "prettier --write .",
    "lint": "eslint --cache .",
    "typecheck:node": "tsc --noEmit -p tsconfig.node.json --composite false",
    "typecheck:web": "tsc --noEmit -p tsconfig.web.json --composite false",
    "typecheck": "npm run typecheck:node && npm run typecheck:web",
    "start": "electron-vite preview",
    "dev": "electron-vite dev",
    "build": "electron-vite build",
    "postinstall": "electron-builder install-app-deps",
    "build:unpack": "npm run build && electron-builder --dir",
    "build:win": "npm run build && electron-builder --win",
    "build:mac": "electron-vite build && electron-builder --mac",
    "build:linux": "electron-vite build && electron-builder --linux",
    "release:patch": "git add -A && git commit -m \"chore: prepare release\" --allow-empty && npm version patch && git push --follow-tags",
    "release:minor": "git add -A && git commit -m \"chore: prepare release\" --allow-empty && npm version minor && git push --follow-tags",
    "release:major": "git add -A && git commit -m \"chore: prepare release\" --allow-empty && npm version major && git push --follow-tags"
  },
  "dependencies": {
    "@electron-toolkit/preload": "^3.0.2",
    "@electron-toolkit/utils": "^4.0.0",
    "@heroui/react": "^2.8.7",
    "@tanstack/react-table": "^8.21.3",
    "axios": "^1.13.2",
    "clsx": "^2.1.1",
    "dayjs": "^1.11.19",
    "electron-updater": "^6.3.9",
    "framer-motion": "^12.23.26",
    "lucide-react": "^0.562.0",
    "next-themes": "^0.4.6",
    "react-router-dom": "^7.11.0",
    "sanitize-filename": "^1.6.3",
    "sonner": "^2.0.7",
    "tailwind-merge": "^3.4.0",
    "uuid": "^13.0.0",
    "zod": "^4.2.1"
  },
  "devDependencies": {
    "@electron-toolkit/eslint-config-prettier": "^3.0.0",
    "@electron-toolkit/eslint-config-ts": "^3.1.0",
    "@electron-toolkit/tsconfig": "^2.0.0",
    "@tailwindcss/vite": "^4.1.18",
    "@types/node": "^22.19.1",
    "@types/react": "^19.2.7",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^5.1.1",
    "electron": "^39.2.6",
    "electron-builder": "^26.0.12",
    "electron-vite": "^5.0.0",
    "eslint": "^9.39.1",
    "eslint-plugin-react": "^7.37.5",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.4.24",
    "prettier": "^3.7.4",
    "react": "^19.2.1",
    "react-dom": "^19.2.1",
    "tailwindcss": "^4.1.18",
    "typescript": "^5.9.3",
    "vite": "^7.2.6",
    "vite-plugin-svgr": "^4.5.0"
  }
}
```

## File: `tsconfig.json`
```json
{
  "files": [],
  "references": [{ "path": "./tsconfig.node.json" }, { "path": "./tsconfig.web.json" }]
}
```

## File: `tsconfig.node.json`
```json
{
  "extends": "@electron-toolkit/tsconfig/tsconfig.node.json",
  "include": ["electron.vite.config.*", "src/main/**/*", "src/preload/**/*", "src/shared/**/*"],
  "compilerOptions": {
    "composite": true,
    "types": ["electron-vite/node"],
    "baseUrl": ".",
    "paths": {
      "@shared/*": [
        "src/shared/*"
      ],
      "@main/*": [
        "src/main/*"
      ],
      "@preload/*": [
        "src/preload/*"
      ]
    }
  }
}
```

## File: `tsconfig.web.json`
```json
{
  "extends": "@electron-toolkit/tsconfig/tsconfig.web.json",
  "include": [
    "src/renderer/src/env.d.ts",
    "src/renderer/src/**/*",
    "src/renderer/src/**/*.tsx",
    "src/preload/*.d.ts",
    "src/shared/**/*"
  ],
  "compilerOptions": {
    "composite": true,
    "jsx": "react-jsx",
    "baseUrl": ".",
    "paths": {
      "@renderer/*": [
        "src/renderer/src/*"
      ],
      "@shared/*": [
        "src/shared/*"
      ]
    }
  }
}
```

## File: `scripts/publish.sh`
```bash
#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v git >/dev/null 2>&1; then
	echo "Error: git is not installed." >&2
	exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
	echo "Error: npm is not installed." >&2
	exit 1
fi

if [ ! -f package.json ]; then
	echo "Error: package.json not found at project root." >&2
	exit 1
fi

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
	echo "Error: current directory is not a git repository." >&2
	exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
	echo "Warning: working tree is not clean."
	echo "Changed files:"
	git status --short
	echo
	read -r -p "Continue publish and commit only package version files? [y/N]: " continue_publish
	case "${continue_publish:-N}" in
		y|Y|yes|YES)
			echo "Continuing with dirty working tree (only version files will be committed)."
			;;
		*)
			echo "Publish cancelled. Please commit/stash your changes first." >&2
			exit 1
			;;
	esac
fi

current_version="$(node -p "require('./package.json').version")"

IFS='.' read -r major minor patch <<<"$current_version"

if [ -z "${major:-}" ] || [ -z "${minor:-}" ] || [ -z "${patch:-}" ]; then
	echo "Error: package.json version is not in x.y.z format: $current_version" >&2
	exit 1
fi

patch_next="${major}.${minor}.$((patch + 1))"
minor_next="${major}.$((minor + 1)).0"
major_next="$((major + 1)).0.0"

echo "Current version: v${current_version}"
echo
echo "Choose release type:"
echo "1) patch - bugfix/small change      (example: v1.0.9 -> v1.0.10)"
echo "2) minor - new backward-compatible feature (example: v1.0.9 -> v1.1.0)"
echo "3) major - breaking changes         (example: v1.0.9 -> v2.0.0)"
echo
echo "Preview from current v${current_version}:"
echo "- patch: v${patch_next}"
echo "- minor: v${minor_next}"
echo "- major: v${major_next}"
echo

read -r -p "Enter choice [1/2/3] (default: 1): " choice

release_type="patch"
case "${choice:-1}" in
	1) release_type="patch" ;;
	2) release_type="minor" ;;
	3) release_type="major" ;;
	*)
		echo "Invalid choice: ${choice}. Use 1, 2, or 3." >&2
		exit 1
		;;
esac

echo "Bumping version using: ${release_type}"
npm version "$release_type" --no-git-tag-version

new_version="$(node -p "require('./package.json').version")"
commit_message="Release version ${new_version}"
tag_name="v${new_version}"

git add package.json
commit_paths=(package.json)
if [ -f package-lock.json ]; then
	git add package-lock.json
	commit_paths+=(package-lock.json)
fi

git commit -m "$commit_message" -- "${commit_paths[@]}"

git tag -a "$tag_name" -m "$commit_message"

current_branch="$(git rev-parse --abbrev-ref HEAD)"

echo "Pushing commit to origin/${current_branch}..."
git push origin "$current_branch"

echo "Pushing tag ${tag_name}..."
git push origin "$tag_name"

echo
echo "Publish completed successfully."
echo "- Commit: ${commit_message}"
echo "- Tag: ${tag_name}"
```

## File: `src/main/index.ts`
```typescript
import { app, shell, BrowserWindow } from 'electron'
import { join } from 'path'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import setupIpcHandlers from './ipc-handler'

let mainWindow: BrowserWindow | null = null

function createWindow(): void {
  // Create the browser window.
  mainWindow = new BrowserWindow({
    show: false,
    autoHideMenuBar: true,
    resizable: true,
    title: 'Tiktok Bulk Downloader',
    icon: join(__dirname, '../../resources/icon.png'),

    webPreferences: {
      preload: join(__dirname, '../preload/index.js'),
      sandbox: false,
      contextIsolation: true,
      nodeIntegration: false
    }
  })

  mainWindow.on('ready-to-show', () => {
    mainWindow?.maximize()
    mainWindow?.show()
  })

  mainWindow.webContents.setWindowOpenHandler((details) => {
    shell.openExternal(details.url)
    return { action: 'deny' }
  })

  // HMR for renderer base on electron-vite cli.
  // Load the remote URL for development or the local html file for production.
  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
    mainWindow.loadURL(process.env['ELECTRON_RENDERER_URL'])
  } else {
    mainWindow.loadFile(join(__dirname, '../renderer/index.html'))
  }
}

const initializeServices = async () => {
  // Setup IPC handlers
  setupIpcHandlers({
    mainWindow: () => mainWindow
  })

  console.log('✅✅✅ [Main] Services initialized')
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(async () => {
  // Set app user model id for windows
  await initializeServices()
  electronApp.setAppUserModelId('com.minhchi1509.toptop-bulk-downloader')

  // Default open or close DevTools by F12 in development
  // and ignore CommandOrControl + R in production.
  // see https://github.com/alex8088/electron-toolkit/tree/master/packages/utils
  app.on('browser-window-created', (_, window) => {
    optimizer.watchWindowShortcuts(window)
  })

  createWindow()

  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

// Cleanup on quit
app.on('before-quit', async () => {
  console.log('🧹🧹🧹[Main] Cleaning up before quit...')
  // Perform any necessary cleanup here
})

// Handle uncaught exceptions
process.on('uncaughtException', (error) => {
  console.error('❌❌❌ [Main] Uncaught exception:', error)
})

process.on('unhandledRejection', (reason) => {
  console.error('❌❌❌ [Main] Unhandled rejection:', reason)
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
```

## File: `src/main/ipc-handler.ts`
```typescript
import { ipcMain, dialog, app, BrowserWindow } from 'electron'
import fs from 'fs'
import path from 'path'
import { autoUpdater } from 'electron-updater'

import { IPC_EVENT_CHANNELS } from '@shared/types/ipc/ipc-event.type'
import TiktokApi from '@shared/api/tiktok.api'
import {
  IpcInvokeHandlers,
  IPC_INVOKE_CHANNELS,
  IpcInvokeMethod
} from '@shared/types/ipc/ipc-invoke.type'
import FileUtils from '@shared/utils/file.util'
import { pipeline } from 'stream/promises'
import { downloadClient } from '@shared/configs/download-client'

autoUpdater.autoDownload = false
autoUpdater.autoInstallOnAppQuit = true

interface ISetupIpcHandlersOptions {
  mainWindow: () => BrowserWindow | null
}

const registerInvokeHandlers = (handlers: IpcInvokeHandlers) => {
  for (const method of Object.keys(IPC_INVOKE_CHANNELS) as IpcInvokeMethod[]) {
    ipcMain.handle(IPC_INVOKE_CHANNELS[method], (_event, ...args) => {
      const handler = handlers[method] as (...handlerArgs: unknown[]) => Promise<unknown>
      return handler(...args)
    })
  }
}

const setupIpcHandlers = ({ mainWindow }: ISetupIpcHandlersOptions) => {
  // Settings handlers share the same file path.
  const settingsPath = path.join(app.getPath('userData'), 'settings.json')

  const invokeHandlers: IpcInvokeHandlers = {
    getUserAwemeList: async (secUid, options) => {
      try {
        const data = await TiktokApi.getUserAwemeList(secUid, options)
        return {
          success: true,
          data
        }
      } catch (error) {
        return {
          success: false,
          error: (error as Error).message
        }
      }
    },

    getUserInfo: async (username, options) => {
      try {
        const userInfo = await TiktokApi.getUserInfoByUsername(username, options)
        return {
          success: true,
          data: userInfo
        }
      } catch (error) {
        return {
          success: false,
          error: (error as Error).message
        }
      }
    },

    getMultiAwemeDetails: async (awemeIds, options) => {
      try {
        const awemeDetails = await TiktokApi.getMultiAwemeDetails(awemeIds, options)
        return {
          success: true,
          data: awemeDetails
        }
      } catch (error) {
        return {
          success: false,
          error: (error as Error).message
        }
      }
    },

    selectFolder: async () => {
      try {
        const { canceled, filePaths } = await dialog.showOpenDialog({
          properties: ['openDirectory']
        })
        if (canceled) {
          return { success: true, data: null }
        }
        return { success: true, data: filePaths[0] }
      } catch (error) {
        return { success: false, error: (error as Error).message }
      }
    },

    downloadFile: async (options) => {
      let filePath = ''

      try {
        const { url, fileName, folderPath, retryCount = 100 } = options
        await FileUtils.ensureDirectory(folderPath)
        filePath = path.join(folderPath, fileName)

        const normalizedRetryCount = Number.isFinite(retryCount)
          ? Math.max(0, Math.trunc(retryCount))
          : 0
        // retryCount means additional retries and does not include the first attempt.
        const totalAttempts = normalizedRetryCount + 1

        let lastError: Error | null = null
        for (let attempt = 1; attempt <= totalAttempts; attempt += 1) {
          try {
            const response = await downloadClient.get(url, {
              responseType: 'stream',
              headers: {
                // Avoid compressed transfer for binary media downloads.
                'Accept-Encoding': 'identity'
              }
            })
            const writer = FileUtils.createWriteStream(filePath, {
              highWaterMark: 1024 * 1024
            })

            await pipeline(response.data, writer)
            return { success: true, data: true }
          } catch (error) {
            lastError = error as Error
            await FileUtils.deleteFile(filePath)
          }
        }

        return {
          success: false,
          error: lastError?.message ?? 'Failed to download file'
        }
      } catch (error) {
        await FileUtils.deleteFile(filePath)
        return { success: false, error: (error as Error).message }
      }
    },

    getDefaultDownloadPath: async () => {
      return { success: true, data: app.getPath('downloads') }
    },

    getSettings: async (key) => {
      try {
        if (fs.existsSync(settingsPath)) {
          const data = fs.readFileSync(settingsPath, 'utf-8')
          const settings = JSON.parse(data) as Record<string, unknown>
          return {
            success: true,
            data: settings[key]
          }
        }
      } catch (error) {
        return { success: false, error: 'Failed to read settings' }
      }
      return { success: true, data: null }
    },

    saveSettings: async (key, value) => {
      try {
        let settings: Record<string, unknown> = {}
        if (fs.existsSync(settingsPath)) {
          const data = fs.readFileSync(settingsPath, 'utf-8')
          settings = JSON.parse(data) as Record<string, unknown>
        }
        settings[key] = value
        fs.writeFileSync(settingsPath, JSON.stringify(settings, null, 2))
      } catch (error) {
        console.error('Error saving settings:', error)
      }
    },

    checkForUpdates: async () => {
      if (!app.isPackaged) {
        // In dev mode, we might want to log or mock.
        console.log('Skipping update check in dev mode')
        return
      }
      await autoUpdater.checkForUpdatesAndNotify()
    },

    downloadUpdate: async () => {
      await autoUpdater.downloadUpdate()
    },

    quitAndInstall: async () => {
      autoUpdater.quitAndInstall(false, true)
    }
  }

  registerInvokeHandlers(invokeHandlers)

  // Auto Updater Events
  autoUpdater.on('checking-for-update', () => {
    const win = mainWindow()
    win?.webContents.send(IPC_EVENT_CHANNELS.onCheckingForUpdate)
  })

  autoUpdater.on('update-available', (info) => {
    const win = mainWindow()
    win?.webContents.send(IPC_EVENT_CHANNELS.onUpdateAvailable, info)
  })

  autoUpdater.on('update-not-available', (info) => {
    const win = mainWindow()
    win?.webContents.send(IPC_EVENT_CHANNELS.onUpdateNotAvailable, info)
  })

  autoUpdater.on('error', (err) => {
    const win = mainWindow()
    win?.webContents.send(IPC_EVENT_CHANNELS.onUpdateError, err)
  })

  autoUpdater.on('download-progress', (progressObj) => {
    const win = mainWindow()
    win?.webContents.send(IPC_EVENT_CHANNELS.onDownloadProgress, progressObj)
  })

  autoUpdater.on('update-downloaded', (info) => {
    const win = mainWindow()
    win?.webContents.send(IPC_EVENT_CHANNELS.onUpdateDownloaded, info)
  })
}

export default setupIpcHandlers
```

## File: `src/preload/index.d.ts`
```typescript
import { ElectronAPI } from '@electron-toolkit/preload'
import { IpcApi } from '@shared/types/ipc'

declare global {
  interface Window {
    api: IpcApi
    electron: ElectronAPI
  }
}
```

## File: `src/preload/index.ts`
```typescript
import { contextBridge, ipcRenderer } from 'electron'
import { electronAPI } from '@electron-toolkit/preload'
import { IpcEventMethod, IpcEventApi, IPC_EVENT_CHANNELS } from '@shared/types/ipc/ipc-event.type'
import {
  IpcInvokeHandlers,
  IPC_INVOKE_CHANNELS,
  IpcInvokeMethod,
  IpcResponse
} from '@shared/types/ipc/ipc-invoke.type'
import { IpcApi } from '@shared/types/ipc'

const invokeApi = Object.fromEntries(
  (Object.keys(IPC_INVOKE_CHANNELS) as IpcInvokeMethod[]).map((method) => [
    method,
    (...args: unknown[]) => ipcRenderer.invoke(IPC_INVOKE_CHANNELS[method], ...args)
  ])
) as IpcInvokeHandlers

const eventApi = Object.fromEntries(
  (Object.keys(IPC_EVENT_CHANNELS) as IpcEventMethod[]).map((method) => [
    method,
    (callback: (...callbackArgs: unknown[]) => void) => {
      const channel = IPC_EVENT_CHANNELS[method]
      const listener = (_event: Electron.IpcRendererEvent, ...eventArgs: unknown[]) => {
        callback(...eventArgs)
      }

      ipcRenderer.on(channel, listener)

      return () => {
        ipcRenderer.removeListener(channel, listener)
      }
    }
  ])
) as IpcEventApi

// Custom APIs for renderer
const api: IpcApi = {
  ...invokeApi,
  ...eventApi,

  getSettings: <T = unknown>(key: string) => {
    return invokeApi.getSettings(key) as Promise<IpcResponse<T>>
  },
  saveSettings: <T>(key: string, value: T) => {
    return invokeApi.saveSettings(key, value)
  }
}

// Use `contextBridge` APIs to expose Electron APIs to
// renderer only if context isolation is enabled, otherwise
// just add to the DOM global.
if (process.contextIsolated) {
  try {
    contextBridge.exposeInMainWorld('electron', electronAPI)
    contextBridge.exposeInMainWorld('api', api)
  } catch (error) {
    console.error(error)
  }
} else {
  // @ts-ignore (define in dts)
  window.electron = electronAPI
  // @ts-ignore (define in dts)
  window.api = api
}
```

## File: `src/renderer/index.html`
```html
<!doctype html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Tiktok Bulk Downloader</title>
    <!-- https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP -->
    <meta
      http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:"
    />
  </head>

  <body>
    <div id="root"></div>
    <script type="module" src="./src/main.tsx"></script>
  </body>
</html>
```

## File: `src/renderer/src/App.tsx`
```tsx
import { HeroUIProvider } from '@heroui/react'
import { ThemeProvider as NextThemesProvider } from 'next-themes'
import Layout from './components/Layout'
import { Toaster } from 'sonner'
import { HashRouter, Route, Routes } from 'react-router-dom'
import HomePage from './pages/HomePage'
import DonatePage from './pages/DonatePage'

export default function App() {
  return (
    <HeroUIProvider>
      <NextThemesProvider attribute="class" defaultTheme="dark">
        <HashRouter>
          <Layout>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/donate" element={<DonatePage />} />
            </Routes>
          </Layout>
          <Toaster />
        </HashRouter>
      </NextThemesProvider>
    </HeroUIProvider>
  )
}
```

## File: `src/renderer/src/env.d.ts`
```typescript
/// <reference types="vite/client" />
interface ImportMetaEnv {
  // more env variables...
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}
```

## File: `src/renderer/src/main.tsx`
```tsx
import './assets/main.css'

import { createRoot } from 'react-dom/client'
import App from './App'

createRoot(document.getElementById('root')!).render(<App />)
```

## File: `src/renderer/src/assets/main.css`
```css
@import 'tailwindcss';
@plugin '@renderer/configs/hero.config.ts';
@source '../../../../node_modules/@heroui/theme/dist/**/*.{js,ts,jsx,tsx}';
@custom-variant dark (&:is(.dark *));

.app-drag {
  -webkit-app-region: drag;
}

.app-no-drag {
  -webkit-app-region: no-drag;
}
```

## File: `src/renderer/src/assets/icons/index.ts`
```typescript
import FacebookLogoIcon from './facebook-logo.svg?react'
import GithubLogoIcon from './github-logo.svg?react'
import PaypalIcon from './paypal.svg?react'

export { FacebookLogoIcon, GithubLogoIcon, PaypalIcon }
```

## File: `src/renderer/src/assets/images/index.ts`
```typescript
import TechcombankQrImage from './techcombank_qr.jpg'

export { TechcombankQrImage }
```

## File: `src/renderer/src/components/Footer.tsx`
```tsx
import { Link } from '@heroui/react'
import { FacebookLogoIcon, GithubLogoIcon } from '@renderer/assets/icons'

const Footer = () => {
  return (
    <footer className="w-full py-4 px-6 flex flex-col md:flex-row items-center justify-between border-t border-divider bg-background/60 backdrop-blur-md">
      <div className="text-small text-default-500">
        Created by <span className="font-semibold text-primary">@minhchi1509</span>
      </div>
      <div className="flex items-center gap-4 mt-2 md:mt-0">
        <Link isExternal href="https://www.facebook.com/minhchi1509">
          <FacebookLogoIcon width={20} height={20} />
        </Link>
        <Link
          isExternal
          href="https://github.com/minhchi1509/tiktok-bulk-downloader-desktop-app"
          className="text-black dark:text-white hover:text-black/80 dark:hover:text-white/80"
        >
          <GithubLogoIcon width={20} height={20} />
        </Link>
      </div>
    </footer>
  )
}

export default Footer
```

## File: `src/renderer/src/components/Layout.tsx`
```tsx
import { ReactNode } from 'react'
import Footer from './Footer'
import UpdaterHandler from './UpdaterHandler'
import { Button, Tooltip } from '@heroui/react'
import { Moon, Sun, RotateCw, Heart } from 'lucide-react'
import { useTheme } from 'next-themes'
import { Link } from 'react-router-dom'

interface LayoutProps {
  children: ReactNode
}

const Layout = ({ children }: LayoutProps) => {
  const { theme, setTheme } = useTheme()

  const toggleTheme = () => {
    setTheme(theme === 'dark' ? 'light' : 'dark')
  }

  return (
    <div className="h-screen overflow-hidden flex flex-col bg-background text-foreground">
      <header className="sticky top-0 z-50 w-full border-b border-divider bg-background/60 backdrop-blur-md px-6 py-3 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="app-drag w-full h-full absolute top-0 left-0 z-0 pointer-events-none" />
          <h1 className="text-xl font-bold bg-clip-text text-transparent bg-linear-to-r from-blue-500 to-cyan-500 z-10">
            Tiktok Bulk Downloader
          </h1>
        </div>

        <div className="flex items-center gap-2 z-10 app-no-drag">
          <Tooltip content="Support Me">
            <Button
              as={Link}
              to="/donate"
              isIconOnly
              variant="light"
              aria-label="Support Me"
              className="text-danger"
            >
              <Heart size={20} />
            </Button>
          </Tooltip>
          <Tooltip content="Check for Updates">
            <Button
              isIconOnly
              variant="light"
              onPress={() => window.api.checkForUpdates()}
              aria-label="Check for Updates"
              className="text-default-500"
            >
              <RotateCw size={20} />
            </Button>
          </Tooltip>
          <Button
            isIconOnly
            variant="light"
            onPress={toggleTheme}
            aria-label="Toggle Dark Mode"
            className="text-default-500"
          >
            {theme === 'dark' ? <Sun size={20} /> : <Moon size={20} />}
          </Button>
        </div>
      </header>

      <main className="flex-1 container mx-auto p-4 md:p-6 overflow-auto flex flex-col">
        {children}
      </main>

      <Footer />
      <UpdaterHandler />
    </div>
  )
}

export default Layout
```

## File: `src/renderer/src/components/UpdaterHandler.tsx`
```tsx
import { useState, useEffect } from 'react'
import {
  Modal,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Button,
  Progress,
  useDisclosure
} from '@heroui/react'
import { UpdateAvailableInfo } from '@shared/types/ipc/ipc-event.type'

type UpdateStatus =
  | 'idle'
  | 'checking'
  | 'available'
  | 'downloading'
  | 'ready'
  | 'error'
  | 'not-available'

const UpdaterHandler = () => {
  const { isOpen, onOpen, onOpenChange } = useDisclosure()
  const [status, setStatus] = useState<UpdateStatus>('idle')
  const [progress, setProgress] = useState(0)
  const [updateInfo, setUpdateInfo] = useState<UpdateAvailableInfo | null>(null)

  useEffect(() => {
    // Listeners
    const removeUpdateAvailable = window.api.onUpdateAvailable((info) => {
      setUpdateInfo(info)
      setStatus('available')
      onOpen()
    })

    const removeUpdateDownloaded = window.api.onUpdateDownloaded(() => {
      setStatus('ready')
      onOpen() // Re-open or ensure open
    })

    const removeDownloadProgress = window.api.onDownloadProgress((prog) => {
      setStatus('downloading')
      setProgress(prog.percent)
    })

    const removeUpdateError = window.api.onUpdateError((err) => {
      setStatus('error')
      console.error(err)
      // Optional: Show toast or modal
    })

    const removeChecking = window.api.onCheckingForUpdate(() => {
      setStatus('checking')
      // Maybe show a toast/loading indicator elsewhere?
    })

    const removeNotAvailable = window.api.onUpdateNotAvailable(() => {
      setStatus('not-available')
      onOpen()
    })

    return () => {
      removeUpdateAvailable()
      removeUpdateDownloaded()
      removeDownloadProgress()
      removeUpdateError()
      removeChecking()
      removeNotAvailable()
    }
  }, [])

  const handleDownload = () => {
    window.api.downloadUpdate()
    setStatus('downloading')
  }

  const handleInstall = () => {
    window.api.quitAndInstall()
  }

  const renderContent = (onClose: () => void) => {
    if (status === 'available') {
      return (
        <>
          <ModalHeader className="flex flex-col gap-1">Update Available</ModalHeader>
          <ModalBody>
            <p>A new version {updateInfo?.version} is available.</p>
            <p>Do you want to download it now?</p>
          </ModalBody>
          <ModalFooter>
            <Button color="danger" variant="light" onPress={onClose}>
              Cancel
            </Button>
            <Button color="primary" onPress={handleDownload}>
              Download
            </Button>
          </ModalFooter>
        </>
      )
    }

    if (status === 'downloading') {
      return (
        <>
          <ModalHeader className="flex flex-col gap-1">Downloading Update...</ModalHeader>
          <ModalBody>
            <Progress
              value={progress}
              showValueLabel={true}
              label="Downloading..."
              aria-label="Update download progress"
            />
          </ModalBody>
          <ModalFooter>
            {/* Can't really cancel easily with electron-updater without cancellation token logic, so just hide button or disable */}
          </ModalFooter>
        </>
      )
    }

    if (status === 'ready') {
      return (
        <>
          <ModalHeader className="flex flex-col gap-1">Update Ready</ModalHeader>
          <ModalBody>
            <p>The update has been downloaded. Restart the app to install?</p>
          </ModalBody>
          <ModalFooter>
            <Button color="danger" variant="light" onPress={onClose}>
              Later
            </Button>
            <Button color="primary" onPress={handleInstall}>
              Restart & Install
            </Button>
          </ModalFooter>
        </>
      )
    }

    if (status === 'not-available') {
      return (
        <>
          <ModalHeader className="flex flex-col gap-1">No Updates Available</ModalHeader>
          <ModalBody>
            <p>You are using the latest version.</p>
          </ModalBody>
          <ModalFooter>
            <Button color="primary" onPress={onClose}>
              OK
            </Button>
          </ModalFooter>
        </>
      )
    }

    return <></>
  }

  return (
    <Modal
      aria-label="Application update dialog"
      isOpen={isOpen}
      onOpenChange={onOpenChange}
      isDismissable={false}
      hideCloseButton={status === 'downloading'}
    >
      <ModalContent>{(onClose) => renderContent(onClose)}</ModalContent>
    </Modal>
  )
}

export default UpdaterHandler
```

## File: `src/renderer/src/configs/hero.config.ts`
```typescript
import { heroui } from '@heroui/react'

export default heroui()
```

## File: `src/renderer/src/features/BulkDownloader.tsx`
```tsx
import {
  Button,
  Input,
  Select,
  SelectItem,
  Chip,
  Progress,
  Tooltip,
  Pagination,
  Table,
  TableHeader,
  TableColumn,
  TableBody,
  TableRow,
  TableCell,
  SortDescriptor,
  Selection,
  ScrollShadow
} from '@heroui/react'
import {
  SortingState,
  createColumnHelper,
  flexRender,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
  FilterFn,
  RowSelectionState
} from '@tanstack/react-table'
import { useState, useMemo, useRef, useCallback, useEffect } from 'react'
import { IAwemeDetails, IUserInfo } from '@shared/types/tiktok.type'
import { promisePool } from '@shared/utils/common.util'
import {
  Search,
  Download,
  FolderOpen,
  StopCircle,
  ExternalLink,
  AlertCircle,
  Save,
  Loader2
} from 'lucide-react'
import tiktokUtils, { TFileNameFormatOption } from '@shared/utils/tiktok.util'
import { showErrorToast, showSuccessToast } from '@renderer/lib/toast'

const columnHelper = createColumnHelper<IAwemeDetails>()
const TIKTOK_COOKIE_SETTINGS_KEY = 'tiktok_cookie'

const FILE_NAME_FORMAT_OPTIONS: Array<{ key: TFileNameFormatOption; label: string }> = [
  { key: 'numericalOrder', label: 'Numerical Order' },
  { key: 'id', label: 'ID' },
  { key: 'title', label: 'Description' },
  { key: 'timestamp', label: 'Timestamp' }
]

const BulkDownloader = () => {
  const [username, setUsername] = useState('')
  const [delay, setDelay] = useState('0')
  const [batchSize, setBatchSize] = useState('15')
  const [loading, setLoading] = useState(false)
  const [userInfo, setUserInfo] = useState<IUserInfo | null>(null)
  const [posts, setPosts] = useState<IAwemeDetails[]>([])

  // Fetch State
  const isCancelGetDataRef = useRef(false)
  const isCancelDownloadRef = useRef(false)

  // Table State
  const [rowSelection, setRowSelection] = useState<RowSelectionState>({})
  const [sorting, setSorting] = useState<SortingState>([])
  const [columnFilters, setColumnFilters] = useState<{ id: string; value: unknown }[]>([])

  // Pagination State
  const [pageIndex, setPageIndex] = useState(0)
  const [pageSize, setPageSize] = useState(10)

  // Download State
  const [folderPath, setFolderPath] = useState('')
  // Using Set to handle multiple selections for filename format
  const [fileNameFormat, setFileNameFormat] = useState<Set<TFileNameFormatOption>>(
    new Set(['numericalOrder', 'id'])
  )
  const [tiktokCookie, setTiktokCookie] = useState('')
  const [isSavingCookie, setIsSavingCookie] = useState(false)
  const [downloading, setDownloading] = useState(false)
  const [failedItems, setFailedItems] = useState<{ item: IAwemeDetails; error: string }[]>([])
  const [downloadProgress, setDownloadProgress] = useState({ current: 0, total: 0 })

  // Custom Filter Function
  const customFilterFn: FilterFn<IAwemeDetails> = (row, columnId, filterValue) => {
    const rowValue = row.getValue(columnId) as string
    if (!filterValue) return true
    return String(rowValue).toLowerCase().includes(String(filterValue).toLowerCase())
  }

  const columns = useMemo(
    () => [
      // Removed manual checkbox column as HeroUI handles it
      columnHelper.accessor('id', {
        id: 'id',
        header: 'ID',
        // Enable column filtering
        filterFn: customFilterFn,
        enableSorting: false,
        cell: (info) => <span className="text-small font-bold">{info.getValue()}</span>
      }),
      columnHelper.accessor('type', {
        id: 'type',
        header: 'Type',
        filterFn: (row, id, value) => {
          return !value || value === 'ALL' || row.getValue(id) === value
        },
        enableSorting: false,
        cell: (info) => (
          <Chip
            size="sm"
            color={info.getValue() === 'VIDEO' ? 'primary' : 'secondary'}
            variant="flat"
          >
            {info.getValue()}
          </Chip>
        )
      }),
      columnHelper.accessor('url', {
        id: 'url',
        header: 'Url',
        enableSorting: false,
        cell: (info) => (
          <a
            href={info.getValue()}
            target="_blank"
            rel="noreferrer"
            className="text-primary hover:text-primary-500"
          >
            <ExternalLink size={16} />
          </a>
        )
      }),
      columnHelper.accessor('description', {
        id: 'description',
        header: 'Description',
        filterFn: customFilterFn,
        enableSorting: false,
        cell: (info) => (
          <Tooltip content={info.getValue()} delay={1000}>
            <div className="w-40 truncate text-tiny cursor-default">{info.getValue()}</div>
          </Tooltip>
        )
      }),
      columnHelper.accessor('createdAt', {
        id: 'createdAt',
        header: 'Created At',
        enableSorting: true,
        cell: (info) => (
          <span className="text-tiny text-default-500">
            {info.getValue() ? new Date(info.getValue() * 1000).toLocaleString() : '-'}
          </span>
        )
      }),
      columnHelper.accessor('stats.likes', {
        id: 'likes',
        header: 'Likes',
        enableSorting: true,
        cell: (info) => (
          <span className="text-tiny">❤️ {Number(info.getValue()).toLocaleString()}</span>
        )
      }),
      columnHelper.accessor('stats.comments', {
        id: 'comments',
        header: 'Comments',
        enableSorting: true,
        cell: (info) => (
          <span className="text-tiny">💬 {Number(info.getValue()).toLocaleString()}</span>
        )
      }),
      columnHelper.accessor('stats.views', {
        id: 'views',
        header: 'Views',
        enableSorting: true,
        cell: (info) => (
          <span className="text-tiny">👁️ {Number(info.getValue()).toLocaleString()}</span>
        )
      }),
      columnHelper.accessor('stats.collects', {
        id: 'collects',
        header: 'Collects',
        enableSorting: true,
        cell: (info) => (
          <span className="text-tiny">📌 {Number(info.getValue()).toLocaleString()}</span>
        )
      })
    ],
    []
  )

  const table = useReactTable({
    data: posts,
    columns,
    getRowId: (row) => row.id, // Important for selection
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    state: {
      sorting,
      rowSelection,
      columnFilters,
      pagination: {
        pageIndex,
        pageSize
      }
    },
    onSortingChange: setSorting,
    onRowSelectionChange: setRowSelection,
    onColumnFiltersChange: setColumnFilters,
    onPaginationChange: (updater) => {
      if (typeof updater === 'function') {
        const newState = updater({ pageIndex, pageSize })
        setPageIndex(newState.pageIndex)
        setPageSize(newState.pageSize)
      } else {
        setPageIndex(updater.pageIndex)
        setPageSize(updater.pageSize)
      }
    },
    enableRowSelection: true
  })

  // HeroUI Table Interop
  const sortDescriptor = useMemo<SortDescriptor | undefined>(() => {
    if (sorting.length === 0) return undefined
    return {
      column: sorting[0].id,
      direction: sorting[0].desc ? 'descending' : 'ascending'
    }
  }, [sorting])

  const handleSortChange = (descriptor: SortDescriptor) => {
    if (descriptor.column) {
      setSorting([
        {
          id: descriptor.column as string,
          desc: descriptor.direction === 'descending'
        }
      ])
    } else {
      setSorting([])
    }
  }

  const selectedKeys = useMemo<Selection>(() => {
    if (table.getIsAllRowsSelected()) return 'all'
    const keys = Object.keys(rowSelection).filter((key) => rowSelection[key])
    if (keys.length === 0) return new Set([])
    return new Set(keys)
  }, [rowSelection, table])

  const handleSelectionChange = (keys: Selection) => {
    if (keys === 'all') {
      table.toggleAllRowsSelected(true)
    } else {
      // If we switched from all to some, or just some to some
      // When keys is a Set, it contains the selected row IDs
      const newSelection = {}
      keys.forEach((key) => {
        newSelection[key] = true
      })
      setRowSelection(newSelection)
    }
  }

  // Fetch Logic
  const handleFetchData = async () => {
    if (!username) {
      showErrorToast('Please provide a username')
      return
    }

    // Toggle Loading
    if (loading) {
      // User clicked cancel
      isCancelGetDataRef.current = true
      setLoading(false)
      return
    }

    setLoading(true)
    isCancelGetDataRef.current = false

    setPosts([])
    setPageIndex(0)

    try {
      const cookie = tiktokCookie.trim()
      const requestOptions = cookie ? { cookie } : undefined

      const { data: user, success, error } = await window.api.getUserInfo(username, requestOptions)

      if (!success || !user) {
        showErrorToast(error)
        setLoading(false)
        return
      }
      setUserInfo(user)

      let currentCursor = '0'
      let currentMaxCursor = '0'
      let hasMore = true

      while (hasMore && !isCancelGetDataRef.current) {
        const { success, data: res } = await window.api.getUserAwemeList(user.secUid, {
          cursor: currentCursor,
          maxCursor: currentMaxCursor,
          ...(requestOptions || {})
        })

        if (!success || !res) {
          showErrorToast('Failed to fetch user posts')
          break
        }

        if (res.pagination.hasMore && res.awemeList.length === 0) {
          showErrorToast('No more posts available or unable to fetch more posts.')
          break
        }

        setPosts((prev) => [...prev, ...res.awemeList])
        currentCursor = res.pagination.cursor
        currentMaxCursor = res.pagination.maxCursor
        hasMore = res.pagination.hasMore

        // Handling delay
        const delayMs = (parseInt(delay) || 0) * 1000
        if (delayMs > 0 && hasMore) await new Promise((r) => setTimeout(r, delayMs))
      }
    } catch (error) {
    } finally {
      setLoading(false)
    }
  }

  // Fetch default path and saved cookie on mount
  useEffect(() => {
    const loadInitialSettings = async () => {
      const [{ data: path }, savedCookieResult] = await Promise.all([
        window.api.getDefaultDownloadPath(),
        window.api.getSettings<string>(TIKTOK_COOKIE_SETTINGS_KEY)
      ])

      if (path) {
        setFolderPath(path)
      }

      if (savedCookieResult?.success && typeof savedCookieResult.data === 'string') {
        setTiktokCookie(savedCookieResult.data)
      }
    }

    loadInitialSettings()
  }, [])

  const handleSaveCookie = async () => {
    setIsSavingCookie(true)
    try {
      await window.api.saveSettings(TIKTOK_COOKIE_SETTINGS_KEY, tiktokCookie.trim())
      showSuccessToast('TikTok cookie saved successfully')
    } catch (_error) {
      showErrorToast('Failed to save TikTok cookie')
    } finally {
      setIsSavingCookie(false)
    }
  }

  const handleDownload = async () => {
    // Get sorted and selected rows
    const sortedRows = table.getSortedRowModel().rows
    const selectedRows = sortedRows.filter((row) => row.getIsSelected())

    if (selectedRows.length === 0) {
      alert('Please select items to download')
      return
    }

    let currentFolderPath = folderPath
    if (!currentFolderPath) {
      const { data: defaultPath } = await window.api.selectFolder()
      if (!defaultPath) return
      currentFolderPath = defaultPath
      setFolderPath(currentFolderPath)
    }

    setDownloading(true)
    setFailedItems([])
    isCancelDownloadRef.current = false
    setDownloadProgress({ current: 0, total: selectedRows.length })

    const safeUsername = tiktokUtils.getFilename({
      id: userInfo?.uniqueId || username || 'unknown_user',
      format: ['id']
    })
    const userFolderPath = `${currentFolderPath}/${safeUsername}`

    const maxConcurrency = Math.max(1, parseInt(batchSize) || 1)
    const currentFailedItems: { item: IAwemeDetails; error: string }[] = []

    await promisePool({
      items: selectedRows,
      concurrency: maxConcurrency,
      worker: async (row, globalIndex) => {
        if (isCancelDownloadRef.current) return

        const item = row.original

        try {
          if (item.type === 'VIDEO' && item.video) {
            const filename = tiktokUtils.getFilename({
              order: globalIndex + 1,
              id: item.id,
              title: item.description,
              timestamp: item.createdAt,
              format: Array.from(fileNameFormat)
            })
            const { success } = await window.api.downloadFile({
              url: item.video.mp4Uri,
              fileName: `${filename}.mp4`,
              folderPath: userFolderPath
            })
            if (!success) {
              throw new Error('Failed to download video')
            }
          } else if (item.type === 'PHOTO' && item.imagesUri) {
            // Download photos for a single post concurrently
            await Promise.all(
              item.imagesUri.map(async (imgUrl, imgIndex) => {
                const filename = tiktokUtils.getFilename({
                  order: `${globalIndex + 1}-${imgIndex + 1}`,
                  id: item.id,
                  title: item.description,
                  timestamp: item.createdAt,
                  format: Array.from(fileNameFormat)
                })
                const { success } = await window.api.downloadFile({
                  url: imgUrl,
                  fileName: `${filename}.jpg`,
                  folderPath: userFolderPath
                })
                if (!success) {
                  throw new Error('Failed to download photo')
                }
              })
            )
          }
        } catch (e) {
          const failedItem = { item, error: (e as Error).message }
          currentFailedItems.push(failedItem)
          setFailedItems((prev) => [...prev, failedItem])
        } finally {
          setDownloadProgress((prev) => ({ ...prev, current: prev.current + 1 }))
        }
      }
    })

    if (currentFailedItems.length > 0) {
      showErrorToast(`Completed with ${currentFailedItems.length} errors.`)
    }

    setDownloading(false)
  }

  const handleStopDownload = () => {
    isCancelDownloadRef.current = true
    setDownloading(false)
  }

  const handleSelectFolder = async () => {
    const { data: path } = await window.api.selectFolder()
    if (path) setFolderPath(path)
  }

  const renderTopContent = useCallback(() => {
    return (
      <div className="flex flex-col gap-4">
        <div className="text-small text-default-500 flex items-center h-full">
          <div className="flex flex-col gap-2">
            <p>
              Username: <b>{userInfo?.uniqueId || ''}</b>
            </p>
            <p>Total posts: {posts.length || 0}</p>
          </div>
        </div>

        <div className="h-divider w-full bg-divider" />

        <div className="flex flex-col gap-2">
          <div className="text-sm font-bold text-default-500">Download options:</div>
          <div className="flex gap-2 items-center">
            <Tooltip delay={0} content={folderPath} placement="top" isDisabled={!folderPath}>
              <Input
                label="Save Location"
                value={folderPath}
                readOnly
                size="sm"
                className="w-64"
                classNames={{
                  input: 'truncate'
                }}
                endContent={
                  <FolderOpen
                    size={16}
                    className="cursor-pointer hover:text-primary"
                    onClick={handleSelectFolder}
                  />
                }
              />
            </Tooltip>

            <Input
              label="TikTok Cookie (optional)"
              value={tiktokCookie}
              onValueChange={setTiktokCookie}
              className="w-96"
              size="sm"
              endContent={
                <button
                  type="button"
                  aria-label="Save TikTok cookie"
                  onClick={handleSaveCookie}
                  disabled={isSavingCookie || !tiktokCookie.trim()}
                  className="flex items-center justify-center text-default-400 disabled:opacity-40 enabled:hover:text-primary"
                >
                  {isSavingCookie ? (
                    <Loader2 size={16} className="animate-spin" />
                  ) : (
                    <Save size={16} />
                  )}
                </button>
              }
            />

            <Select
              label="Filename Format"
              selectionMode="multiple"
              selectedKeys={fileNameFormat}
              onSelectionChange={(keys) => setFileNameFormat(keys as Set<TFileNameFormatOption>)}
              className="w-96"
              size="sm"
              classNames={{
                label: 'mb-2'
              }}
              renderValue={(items) => (
                <div className="flex flex-wrap items-center gap-1">
                  {items.map((item, index) => (
                    <div key={item.key} className="flex items-center gap-1">
                      <Chip size="sm" variant="flat" color="primary">
                        {item.textValue}
                      </Chip>

                      {/* separator "_" (không render cho item cuối) */}
                      {index < items.length - 1 && <span className="text-default-400">_</span>}
                    </div>
                  ))}
                </div>
              )}
            >
              {FILE_NAME_FORMAT_OPTIONS.map((option) => (
                <SelectItem key={option.key}>{option.label}</SelectItem>
              ))}
            </Select>

            <Input
              label="Download concurrency"
              value={batchSize}
              onValueChange={setBatchSize}
              className="grow max-w-xs"
              type="number"
              size="sm"
              isDisabled={loading}
            />
          </div>
        </div>

        <div className="h-divider w-full bg-divider" />

        <div className="flex justify-between items-center flex-wrap gap-2">
          <div className="flex gap-2 items-center flex-1">
            {/* ID Search Filter */}
            <Input
              placeholder="Filter ID..."
              value={(table.getColumn('id')?.getFilterValue() as string) ?? ''}
              onValueChange={(val) => table.getColumn('id')?.setFilterValue(val)}
              startContent={<Search size={14} />}
              size="sm"
              className="max-w-sm"
            />
            {/* Description Search Filter */}
            <Input
              placeholder="Filter Description..."
              value={(table.getColumn('description')?.getFilterValue() as string) ?? ''}
              onValueChange={(val) => table.getColumn('description')?.setFilterValue(val)}
              startContent={<Search size={14} />}
              size="sm"
              className="max-w-sm"
            />
            {/* Type Filter */}
            <Select
              placeholder="Type"
              size="sm"
              className="w-24"
              selectedKeys={[(table.getColumn('type')?.getFilterValue() as string) || 'ALL']}
              onChange={(e) => table.getColumn('type')?.setFilterValue(e.target.value)}
            >
              <SelectItem key="ALL">All</SelectItem>
              <SelectItem key="VIDEO">Video</SelectItem>
              <SelectItem key="PHOTO">Photo</SelectItem>
            </Select>
          </div>

          {/* Download Configuration */}
          <div className="flex gap-2 items-center">
            <Button
              size="sm"
              color={downloading ? 'danger' : 'primary'}
              onPress={downloading ? handleStopDownload : handleDownload}
              startContent={downloading ? <StopCircle size={16} /> : <Download size={16} />}
              isDisabled={Object.keys(rowSelection).length === 0}
            >
              {downloading ? `Stop` : `Download (${Object.keys(rowSelection).length})`}
            </Button>
          </div>
        </div>
        {downloading && (
          <div className="w-full px-1">
            <div className="flex justify-between text-tiny mb-1">
              <span>Downloading...</span>
              <span>
                {downloadProgress.current} / {downloadProgress.total}
              </span>
            </div>
            <Progress
              value={(downloadProgress.current / downloadProgress.total) * 100}
              size="sm"
              color="success"
              className="w-full"
            />
          </div>
        )}

        {failedItems.length > 0 && (
          <div className="w-full mt-2">
            <div className="flex gap-2 items-center mb-1 text-danger">
              <AlertCircle size={16} />
              <span className="font-bold text-small">Failed Downloads ({failedItems.length})</span>
            </div>
            <ScrollShadow
              className="h-30 w-full border border-danger-200 rounded-lg p-2 bg-danger-50 dark:bg-danger-900/20"
              visibility="none"
            >
              <div className="flex flex-col gap-2">
                {failedItems.map(({ item, error }, idx) => (
                  <div
                    key={`${item.id}-${idx}`}
                    className="flex justify-between items-start text-tiny gap-2"
                  >
                    <div className="flex flex-col min-w-0 flex-1">
                      <span className="font-bold text-danger-600 dark:text-danger-400 font-mono">
                        {item.id}
                      </span>
                      <span className="truncate text-default-500">{item.description}</span>
                    </div>
                    <span className="text-danger whitespace-nowrap ml-2">{error}</span>
                  </div>
                ))}
              </div>
            </ScrollShadow>
          </div>
        )}
      </div>
    )
  }, [
    table,
    folderPath,
    tiktokCookie,
    fileNameFormat,
    isSavingCookie,
    downloading,
    downloadProgress,
    rowSelection,
    columns,
    userInfo,
    posts.length,
    batchSize,
    loading,
    failedItems
  ])

  const renderBottomContent = useCallback(() => {
    return (
      <div className="flex justify-between items-center p-2 rounded-lg border border-divider">
        <div className="text-small text-default-500">Total {posts.length} items</div>

        <Pagination
          showControls
          total={table.getPageCount()}
          initialPage={1}
          page={pageIndex + 1}
          onChange={(page) => setPageIndex(page - 1)}
          siblings={1}
          boundaries={1}
        />

        <Select
          size="sm"
          className="w-36"
          selectedKeys={[String(pageSize)]}
          onChange={(e) => setPageSize(Number(e.target.value))}
          aria-label="Rows per page"
        >
          <SelectItem key="10">10 / page</SelectItem>
          <SelectItem key="20">20 / page</SelectItem>
          <SelectItem key="50">50 / page</SelectItem>
          <SelectItem key="100">100 / page</SelectItem>
        </Select>
      </div>
    )
  }, [posts.length, table, pageIndex, pageSize])

  return (
    <div className="flex flex-col gap-4 h-full relative p-2">
      {/* Input Section */}
      <div className="flex flex-col gap-4 bg-content1 p-4 rounded-lg shadow-sm border border-divider">
        <div className="flex gap-4 items-end">
          <Input
            label="Username"
            value={username}
            onValueChange={setUsername}
            className="max-w-max"
            variant="bordered"
            size="sm"
            isDisabled={loading}
          />

          <Input
            label="Delay between requests (seconds)"
            value={delay}
            onValueChange={setDelay}
            className="grow max-w-xs"
            type="number"
            variant="bordered"
            size="sm"
            isDisabled={loading}
            placeholder="0"
          />

          <Button
            className="min-w-fit grow"
            color={loading ? 'danger' : 'primary'}
            onPress={handleFetchData}
            startContent={!loading ? <Search size={18} /> : <StopCircle size={18} />}
          >
            {loading ? 'Stop' : 'Get Data'}
          </Button>
        </div>
      </div>

      {/* Main Content: HeroUI Table */}
      <div className="flex gap-4 h-full overflow-hidden rounded-lg shadow-sm border border-divider p-4">
        <Table
          aria-label="Bulk Downloader Table"
          isHeaderSticky
          removeWrapper
          bottomContent={renderBottomContent()}
          bottomContentPlacement="outside"
          topContent={renderTopContent()}
          topContentPlacement="outside"
          classNames={{
            wrapper: 'h-full shadow-sm border border-divider',
            base: 'h-full overflow-hidden'
          }}
          selectionMode="multiple"
          selectedKeys={selectedKeys}
          onSelectionChange={handleSelectionChange}
          sortDescriptor={sortDescriptor}
          onSortChange={handleSortChange}
        >
          <TableHeader columns={columns}>
            {(column) => (
              <TableColumn
                key={column.id}
                align={column.id === 'actions' ? 'end' : 'start'}
                allowsSorting={column.enableSorting}
              >
                {column.header as string}
              </TableColumn>
            )}
          </TableHeader>
          <TableBody
            items={table.getRowModel().rows}
            emptyContent={loading ? 'Fetching...' : 'No data found'}
          >
            {(row) => (
              <TableRow key={row.original.id}>
                {(columnKey) => (
                  <TableCell>
                    {flexRender(
                      row.getVisibleCells().find((cell) => cell.column.id === columnKey)?.column
                        .columnDef.cell,
                      row
                        .getVisibleCells()
                        .find((cell) => cell.column.id === columnKey)
                        ?.getContext()!
                    )}
                  </TableCell>
                )}
              </TableRow>
            )}
          </TableBody>
        </Table>
      </div>
    </div>
  )
}

export default BulkDownloader
```

## File: `src/renderer/src/features/SingleDownloader.tsx`
```tsx
import {
  Button,
  Input,
  Select,
  SelectItem,
  Card,
  CardBody,
  Chip,
  Tooltip,
  Textarea,
  ScrollShadow
} from '@heroui/react'
import { useState, useEffect, useRef } from 'react'
import { FolderOpen, Download, Check, AlertCircle, Loader2, Save } from 'lucide-react'
import { IAwemeDetails } from '@shared/types/tiktok.type'
import { TIKTOK_POST_DETAIL_URL_PATTERN } from '@shared/constants'
import tiktokUtils, { TFileNameFormatOption } from '@shared/utils/tiktok.util'
import { showErrorToast, showSuccessToast } from '@renderer/lib/toast'
import { promisePool } from '@shared/utils/common.util'

const TIKTOK_COOKIE_SETTINGS_KEY = 'tiktok_cookie'
const SINGLE_CONCURRENCY_SETTINGS_KEY = 'single_concurrency'

const FILE_NAME_FORMAT_OPTIONS: Array<{ key: TFileNameFormatOption; label: string }> = [
  { key: 'id', label: 'ID' },
  { key: 'title', label: 'Description' },
  { key: 'timestamp', label: 'Timestamp' }
]

interface IDownloadItem {
  id: string
  originalUrl: string
  status: 'pending' | 'downloading' | 'success' | 'error'
  error?: string
  data?: IAwemeDetails
}

const SingleDownloader = () => {
  const [inputUrls, setInputUrls] = useState('')
  const [folderPath, setFolderPath] = useState('')
  const [fileNameFormat, setFileNameFormat] = useState<Set<TFileNameFormatOption>>(new Set(['id']))
  const [tiktokCookie, setTiktokCookie] = useState('')
  const [isSavingCookie, setIsSavingCookie] = useState(false)
  const [concurrentDownloads, setConcurrentDownloads] = useState('5')
  const [isProcessing, setIsProcessing] = useState(false)
  const [downloadQueue, setDownloadQueue] = useState<IDownloadItem[]>([])

  // Refs for processing loop
  const isCancelledRef = useRef(false)

  useEffect(() => {
    const loadInitialSettings = async () => {
      const [{ data: path }, savedCookieResult, savedConcurrencyResult] = await Promise.all([
        window.api.getDefaultDownloadPath(),
        window.api.getSettings<string>(TIKTOK_COOKIE_SETTINGS_KEY),
        window.api.getSettings<string>(SINGLE_CONCURRENCY_SETTINGS_KEY)
      ])

      if (path) {
        setFolderPath(path)
      }

      if (savedCookieResult?.success && typeof savedCookieResult.data === 'string') {
        setTiktokCookie(savedCookieResult.data)
      }

      if (savedConcurrencyResult?.success && savedConcurrencyResult.data) {
        const parsed = Number.parseInt(String(savedConcurrencyResult.data), 10)
        if (!Number.isNaN(parsed) && parsed > 0) {
          setConcurrentDownloads(String(parsed))
        }
      }
    }

    loadInitialSettings()
  }, [])

  const handleSaveCookie = async () => {
    setIsSavingCookie(true)
    try {
      await window.api.saveSettings(TIKTOK_COOKIE_SETTINGS_KEY, tiktokCookie.trim())
      showSuccessToast('TikTok cookie saved successfully')
    } catch (_error) {
      showErrorToast('Failed to save TikTok cookie')
    } finally {
      setIsSavingCookie(false)
    }
  }

  const handleConcurrencyChange = (value: string) => {
    setConcurrentDownloads(value)
    const parsed = Number.parseInt(value, 10)
    if (!Number.isNaN(parsed) && parsed > 0) {
      window.api.saveSettings(SINGLE_CONCURRENCY_SETTINGS_KEY, String(parsed))
    }
  }

  const handleSelectFolder = async () => {
    const { data: path } = await window.api.selectFolder()
    if (path) setFolderPath(path)
  }

  const getFilename = (item: IAwemeDetails, ext: string) => {
    const filename = tiktokUtils.getFilename({
      id: item.id,
      title: item.description,
      timestamp: item.createdAt,
      format: Array.from(fileNameFormat)
    })

    return `${filename}.${ext}`
  }

  const downloadItem = async (dataItem: IAwemeDetails, itemId: string, targetFolder: string) => {
    try {
      if (dataItem.type === 'VIDEO' && dataItem.video) {
        const { success } = await window.api.downloadFile({
          url: dataItem.video.mp4Uri,
          fileName: getFilename(dataItem, 'mp4'),
          folderPath: targetFolder
        })
        if (!success) throw new Error('Failed to download video')
      } else if (dataItem.type === 'PHOTO' && dataItem.imagesUri) {
        const baseName = getFilename(dataItem, 'jpg')
        const photoFolderPath = `${targetFolder}/${dataItem.id}`
        await Promise.allSettled(
          dataItem.imagesUri.map(async (u, k) => {
            const { success } = await window.api.downloadFile({
              url: u,
              fileName: `${k + 1}_${baseName}`,
              folderPath: photoFolderPath
            })
            if (!success) throw new Error('Failed to download photo')
          })
        )
      }

      setDownloadQueue((prev) =>
        prev.map((i) => (i.id === itemId ? { ...i, status: 'success', data: dataItem } : i))
      )
    } catch (e) {
      setDownloadQueue((prev) =>
        prev.map((i) =>
          i.id === itemId ? { ...i, status: 'error', error: (e as Error).message } : i
        )
      )
    }
  }

  const startProcessing = async (
    items: IDownloadItem[],
    detailsById: Record<string, IAwemeDetails>
  ) => {
    let targetFolder = folderPath
    if (!targetFolder) {
      targetFolder =
        (await window.api.getDefaultDownloadPath().then(({ data: path }) => path)) || ''
    }

    const validItems = items.filter((item) => Boolean(detailsById[item.id]))

    const maxConcurrency = Math.max(1, Number.parseInt(concurrentDownloads, 10) || 1)

    await promisePool({
      items: validItems,
      concurrency: maxConcurrency,
      worker: async (item) => {
        if (isCancelledRef.current) return
        const details = detailsById[item.id]
        if (!details) {
          setDownloadQueue((prev) =>
            prev.map((queueItem) =>
              queueItem.id === item.id
                ? { ...queueItem, status: 'error', error: 'Post details not found' }
                : queueItem
            )
          )
          return
        }
        setDownloadQueue((prev) =>
          prev.map((q) => (q.id === item.id ? { ...q, status: 'downloading' } : q))
        )
        await downloadItem(details, item.id, targetFolder)
      }
    })

    setIsProcessing(false)
  }

  const onDownloadClick = async () => {
    if (!folderPath) {
      const { data: path } = await window.api.getDefaultDownloadPath()
      if (path) setFolderPath(path)
      else {
        showErrorToast('Please select a download folder')
        return
      }
    }

    const lines = inputUrls.split(/[\n\s]+/).filter((l) => l.trim().length > 0)
    const newItems: IDownloadItem[] = []
    const seenIds = new Set()

    lines.forEach((l) => {
      const match = l.match(TIKTOK_POST_DETAIL_URL_PATTERN)
      if (match && match[1]) {
        if (!seenIds.has(match[1])) {
          newItems.push({ id: match[1], originalUrl: l, status: 'pending' })
          seenIds.add(match[1])
        }
      }
    })

    if (newItems.length === 0) {
      showErrorToast('No valid URLs found')
      return
    }

    setDownloadQueue(newItems)
    setIsProcessing(true)
    isCancelledRef.current = false

    const cookie = tiktokCookie.trim()
    const detailResult = await window.api.getMultiAwemeDetails(
      newItems.map((item) => item.id),
      cookie ? { cookie } : undefined
    )

    if (!detailResult.success || !detailResult.data) {
      setIsProcessing(false)
      showErrorToast(detailResult.error || 'Failed to fetch post details')
      return
    }

    const detailsById = detailResult.data
    setDownloadQueue((prev) =>
      prev.map((item) => {
        const details = detailsById[item.id]
        if (!details) {
          return {
            ...item,
            status: 'error',
            error: 'Post details not found'
          }
        }
        return {
          ...item,
          data: details,
          status: 'pending'
        }
      })
    )

    startProcessing(newItems, detailsById)
  }

  return (
    <div className="flex flex-col gap-6 max-w-4xl mx-auto mt-6 p-6 bg-content1 rounded-xl shadow-lg border border-divider">
      <div className="space-y-6">
        <div>
          <h2 className="text-2xl font-bold bg-clip-text text-transparent bg-linear-to-r from-primary to-secondary">
            Multi-URLs Downloader
          </h2>
          <p className="text-default-500">Enter multiple TikTok URLs to download them at once.</p>
        </div>

        <Textarea
          label="Tiktok URLs"
          placeholder="Paste Tiktok links here (one per line or space separated)...&#10;https://www.tiktok.com/@user/video/75899...&#10;https://www.tiktok.com/@user/photo/75880..."
          minRows={5}
          maxRows={10}
          value={inputUrls}
          onValueChange={setInputUrls}
          variant="bordered"
          isDisabled={isProcessing}
        />

        <div className="flex flex-col gap-4">
          <div className="flex gap-4 items-end">
            <Tooltip delay={0} content={folderPath} placement="top" isDisabled={!folderPath}>
              <Input
                label="Save Location"
                value={folderPath}
                readOnly
                placeholder="Default: Downloads"
                className="flex-1"
                variant="bordered"
                endContent={
                  <FolderOpen
                    className="text-default-400 cursor-pointer hover:text-primary"
                    onClick={handleSelectFolder}
                  />
                }
              />
            </Tooltip>

            <Input
              label="TikTok Cookie (optional)"
              value={tiktokCookie}
              onValueChange={setTiktokCookie}
              className="flex-1"
              variant="bordered"
              isDisabled={isProcessing}
              endContent={
                <button
                  type="button"
                  aria-label="Save TikTok cookie"
                  onClick={handleSaveCookie}
                  disabled={isProcessing || isSavingCookie || !tiktokCookie.trim()}
                  className="flex items-center justify-center text-default-400 disabled:opacity-40 enabled:hover:text-primary"
                >
                  {isSavingCookie ? (
                    <Loader2 size={16} className="animate-spin" />
                  ) : (
                    <Save size={16} />
                  )}
                </button>
              }
            />
          </div>

          <Input
            label="Concurrent Downloads"
            value={concurrentDownloads}
            onValueChange={handleConcurrencyChange}
            type="number"
            min={1}
            variant="bordered"
            isDisabled={isProcessing}
          />

          <Select
            classNames={{ label: 'mb-2' }}
            label="Filename Format"
            selectionMode="multiple"
            selectedKeys={fileNameFormat}
            onSelectionChange={(keys) => setFileNameFormat(keys as Set<TFileNameFormatOption>)}
            variant="bordered"
            renderValue={(items) => (
              <div className="flex flex-wrap items-center gap-1">
                {items.map((item, index) => (
                  <div key={item.key} className="flex items-center gap-1">
                    <Chip size="sm" variant="flat" color="primary">
                      {item.textValue}
                    </Chip>
                    {index < items.length - 1 && <span className="text-default-400">_</span>}
                  </div>
                ))}
              </div>
            )}
          >
            {FILE_NAME_FORMAT_OPTIONS.map((option) => (
              <SelectItem key={option.key}>{option.label}</SelectItem>
            ))}
          </Select>
        </div>

        <Button
          color={isProcessing ? 'danger' : 'primary'}
          onPress={() => {
            if (isProcessing) {
              isCancelledRef.current = true
              setIsProcessing(false) // Optimistic UI update
            } else {
              onDownloadClick()
            }
          }}
          className="w-full font-bold text-md"
          size="lg"
          startContent={isProcessing ? <AlertCircle /> : <Download />}
        >
          {isProcessing ? 'Stop Downloading' : 'Start Download'}
        </Button>

        {/* Status Queue Section */}
        {downloadQueue.length > 0 && (
          <div className="flex flex-col gap-3 mt-4">
            <div className="flex justify-between items-center">
              <h3 className="font-semibold text-default-600">
                Download Queue ({downloadQueue.length})
              </h3>
              <span className="text-tiny text-default-400">
                Success: {downloadQueue.filter((i) => i.status === 'success').length} | Failed:{' '}
                {downloadQueue.filter((i) => i.status === 'error').length}
              </span>
            </div>

            <ScrollShadow
              className="h-75 w-full rounded-lg border border-divider p-2 gap-2 flex flex-col"
              visibility="none"
            >
              {downloadQueue.map((item) => (
                <Card
                  key={item.id}
                  className="w-full shadow-sm border border-default-100 flex-none"
                >
                  <CardBody className="flex flex-row items-center gap-3 p-3 overflow-hidden">
                    <div className="min-w-20 font-mono text-small text-default-500">{item.id}</div>

                    <div className="flex-1 min-w-0 flex flex-col">
                      <div className="text-small truncate">
                        {item.data?.description || item.originalUrl}
                      </div>
                      {item.status === 'error' && (
                        <div className="text-tiny text-danger truncate">{item.error}</div>
                      )}
                    </div>

                    <div className="flex items-center gap-2">
                      {item.status === 'pending' && (
                        <div className="text-tiny text-default-400">Pending</div>
                      )}
                      {item.status === 'downloading' && (
                        <Loader2 className="animate-spin text-primary" size={18} />
                      )}
                      {item.status === 'success' && <Check className="text-success" size={18} />}
                      {item.status === 'error' && <AlertCircle className="text-danger" size={18} />}
                    </div>
                  </CardBody>
                </Card>
              ))}
            </ScrollShadow>
          </div>
        )}
      </div>
    </div>
  )
}

export default SingleDownloader
```

## File: `src/renderer/src/lib/toast.ts`
```typescript
import { ExternalToast, toast } from 'sonner'

type TToastType = 'success' | 'error' | 'info' | 'warning'

const showToast = (type: TToastType, message: string, options?: ExternalToast) => {
  toast[type](message, {
    ...options,
    position: 'top-center',
    richColors: true,
    closeButton: false
  })
}

export const showSuccessToast = (message: string, options?: ExternalToast) => {
  showToast('success', message, options)
}

export const showErrorToast = (message: string, options?: ExternalToast) => {
  showToast('error', message, options)
}
```

## File: `src/renderer/src/pages/DonatePage.tsx`
```tsx
import { Card, CardBody, Button } from '@heroui/react'
import { Heart, QrCode, ArrowLeft } from 'lucide-react'
import { TechcombankQrImage } from '../assets/images'
import { Link } from 'react-router-dom'
import { PaypalIcon } from '@renderer/assets/icons'

const DonatePage = () => {
  return (
    <div className="max-w-4xl mx-auto py-8 animate-fade-in relative">
      <div className="absolute top-0 left-0">
        <Button
          as={Link}
          to="/"
          variant="light"
          startContent={<ArrowLeft size={20} />}
          className="font-medium"
        >
          Back
        </Button>
      </div>

      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-default-900 mb-4 flex items-center justify-center gap-3">
          <Heart className="text-danger fill-danger" size={36} />
          Support Me
        </h1>
        <p className="text-lg text-default-500 max-w-2xl mx-auto">
          If you find this tool helpful, please consider supporting me to keep it maintained and
          improved. Thank you!
        </p>
      </div>

      <div className="grid md:grid-cols-2 gap-8">
        {/* PayPal Section */}
        <Card className="hover:scale-105 hover:cursor-pointer transition-all duration-300">
          <CardBody className="p-8 text-center">
            <div className="bg-primary/10 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
              {/* Fallback to text P since icon is missing */}
              <PaypalIcon width={30} height={30} />
            </div>

            <h3 className="text-2xl font-bold text-default-900 mb-4">PayPal</h3>

            <p className="text-default-500 mb-6">
              Support me via PayPal! Secure and trusted payment method worldwide.
            </p>

            {/* PayPal Info */}
            <div className="bg-default-100 p-4 rounded-lg mb-6">
              <p className="font-semibold text-default-700 text-lg">paypal.me/minhchi1509</p>
            </div>

            <Button
              as="a"
              href="https://paypal.me/minhchi1509"
              target="_blank"
              rel="noopener noreferrer"
              color="primary"
              size="lg"
              className="w-full font-bold"
            >
              Donate via PayPal
            </Button>

            <p className="text-xs text-default-400 mt-4">
              Click the button to donate securely via PayPal
            </p>
          </CardBody>
        </Card>

        {/* Techcombank QR Section */}
        <Card className="hover:scale-105 hover:cursor-pointer transition-all duration-300">
          <CardBody className="p-8 text-center">
            <div className="bg-success/10 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-6">
              <QrCode className="text-success h-8 w-8" />
            </div>

            <h3 className="text-2xl font-bold text-default-900 mb-4">Techcombank QR</h3>

            <p className="text-default-500 mb-6">
              Chuyển khoản qua QR Code Techcombank. Nhanh chóng và tiện lợi!
            </p>

            {/* QR Code */}
            <div className="bg-white p-2 rounded-lg border border-divider border-dashed mb-6 mx-auto w-48 h-48 flex items-center justify-center overflow-hidden">
              <img
                src={TechcombankQrImage}
                alt="Techcombank QR"
                className="w-full h-full object-contain"
              />
            </div>

            <div className="space-y-3">
              <div className="bg-default-100 p-3 rounded-lg">
                <span className="font-semibold text-default-700">Ngân hàng: </span>
                <span className="text-default-600">Techcombank</span>
              </div>

              <div className="bg-default-100 p-3 rounded-lg">
                <span className="font-semibold text-default-700">Chủ tài khoản: </span>
                <span className="text-default-600">NGUYEN MINH CHI</span>
              </div>
            </div>

            <p className="text-xs text-default-400 mt-4">Quét mã QR để chuyển khoản nhanh chóng</p>
          </CardBody>
        </Card>
      </div>
    </div>
  )
}

export default DonatePage
```

## File: `src/renderer/src/pages/HomePage.tsx`
```tsx
import { Tabs, Tab } from '@heroui/react'
import BulkDownloader from '../features/BulkDownloader'
import SingleDownloader from '../features/SingleDownloader'

export default function HomePage() {
  return (
    <div className="flex w-full flex-col h-[calc(100vh-140px)]">
      <Tabs
        aria-label="Features"
        destroyInactiveTabPanel={false}
        color="primary"
        variant="underlined"
        classNames={{
          tabList: 'gap-6 w-full relative rounded-none p-0 border-b border-divider',
          cursor: 'w-full bg-primary',
          tab: 'max-w-fit px-0 h-12',
          tabContent: 'group-data-[selected=true]:text-primary'
        }}
      >
        <Tab key="bulk" title="Bulk Download">
          <div className="pt-4 h-full">
            <BulkDownloader />
          </div>
        </Tab>
        <Tab key="single" title="Multi-URLs Download">
          <div className="pt-4 h-full">
            <SingleDownloader />
          </div>
        </Tab>
      </Tabs>
    </div>
  )
}
```

## File: `src/renderer/src/types/svgr.d.ts`
```typescript
declare module '*.svg?react' {
  import { FC, SVGProps } from 'react'

  const content: FC<SVGProps<SVGElement>>
  export default content
}
```

## File: `src/shared/api/tiktok.api.ts`
```typescript
import { DEFAULT_USER_AGENT, TIKTOK_API_URL } from '@shared/constants'
import {
  IpcGetAwemeDetailsOptions,
  IpcGetAwemeListOptions
} from '@shared/types/ipc/ipc-invoke.type'
import { IUserInfo, IAwemeListResponse, IAwemeDetails } from '@shared/types/tiktok.type'
import tiktokUtils from '@shared/utils/tiktok.util'
import axios from 'axios'

const getUserInfoByUsername = async (
  username: string,
  options?: IpcGetAwemeDetailsOptions
): Promise<IUserInfo> => {
  try {
    const { cookie } = options || {}
    const { data: rawResponse } = await axios.get(`https://www.tiktok.com/@${username}`, {
      headers: {
        ...(cookie ? { Cookie: cookie } : {}),
        'User-Agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'
      }
    })

    const regex = /(?<="webapp\.user-detail":)[\s\S]*?(?=,"webapp\.a-b")/

    const result = rawResponse.match(regex)
    if (!result || result.length === 0) {
      throw new Error('User data not found in the page')
    }

    const userDataString = result[0]
    const userData = JSON.parse(userDataString)
    const userInfo = userData.userInfo?.user
    const userStat = userData.userInfo?.stats

    return {
      id: userInfo.id,
      uniqueId: userInfo.uniqueId,
      secUid: userInfo.secUid,
      followerCount: userStat.followerCount,
      followingCount: userStat.followingCount,
      avatarUri: userInfo.avatarLarger || userInfo.avatarMedium || userInfo.avatarThumb || ''
    }
  } catch (error) {
    throw new Error('Failed to fetch user info')
  }
}

const getUserAwemeList = async (
  secUid: string,
  options?: IpcGetAwemeListOptions
): Promise<IAwemeListResponse> => {
  try {
    const { maxCursor = '0', cursor = '0', cookie } = options || {}
    const baseParams = tiktokUtils.getBaseMobileParams()
    const params = {
      ...baseParams,
      source: '0',
      max_cursor: maxCursor,
      cursor,
      sec_user_id: secUid,
      count: '21',
      filter_private: '1',
      lite_flow_schedule: 'new',
      cdn_cache_is_login: '1',
      cdn_cache_strategy: 'v0',
      data_saver_type: '1',
      data_saver_work: 'false',
      page_type: '2'
    }

    const headers: Record<string, string> = {
      'User-Agent': DEFAULT_USER_AGENT,
      'x-tt-ttnet-origin-host': 'api22-normal-c-alisg.tiktokv.com',
      Host: 'aggr22-normal-alisg.tiktokv.com',
      ...(cookie && { Cookie: cookie })
    }

    const { data: responseData } = await axios.get(TIKTOK_API_URL.GET_USER_AWEME_LIST, {
      params,
      headers,
      paramsSerializer: (p) => new URLSearchParams(p).toString()
    })
    const hasMore = responseData.has_more === 1
    const awemeList = responseData.aweme_list || []
    const pagination = {
      cursor: responseData.min_cursor?.toString() || '',
      maxCursor: responseData.max_cursor?.toString() || '',
      hasMore
    }
    const formattedAwemeList = awemeList
      .map((item: any) => tiktokUtils.formatAwemeItemResponse(item))
      .filter((item: IAwemeDetails | null): item is IAwemeDetails => item !== null)

    return {
      awemeList: formattedAwemeList,
      pagination
    }
  } catch (error) {
    throw new Error('Failed to fetch user aweme list')
  }
}

const getMultiAwemeDetails = async (
  listAwemeIds: string[],
  options?: IpcGetAwemeDetailsOptions
): Promise<Record<string, IAwemeDetails>> => {
  try {
    const { cookie } = options || {}
    const baseParams = tiktokUtils.getBaseMobileParams()
    const formattedDetails: Record<string, IAwemeDetails> = {}
    const uniqueAwemeIds = Array.from(new Set(listAwemeIds))
    const MAX_BATCH_SIZE = 10
    const MAX_RETRY_TIMES = 5

    const headers: Record<string, any> = {
      ...(cookie && { Cookie: cookie })
    }

    const chunkArray = (arr: string[], size: number) => {
      const chunks: string[][] = []
      for (let i = 0; i < arr.length; i += size) {
        chunks.push(arr.slice(i, i + size))
      }
      return chunks
    }

    let missingAwemeIds = [...uniqueAwemeIds]
    let retryCount = 0

    while (missingAwemeIds.length > 0 && retryCount < MAX_RETRY_TIMES) {
      const batches = chunkArray(missingAwemeIds, MAX_BATCH_SIZE)

      const responses = await Promise.all(
        batches.map(async (batch) => {
          const params = {
            ...baseParams,
            sp: 850,
            type: 0,
            max_cursor: 0,
            min_cursor: 0,
            count: MAX_BATCH_SIZE,
            aweme_ids: batch.join(',')
          }

          const { data: responseData } = await axios.post(
            TIKTOK_API_URL.GET_MULTI_AWEME_DETAIL,
            undefined,
            {
              params,
              headers,
              paramsSerializer: (p) => new URLSearchParams(p).toString()
            }
          )

          return responseData
        })
      )

      responses.forEach((responseData) => {
        const awemesDetails = responseData?.aweme_list || []
        awemesDetails.forEach((aweme: any) => {
          if (uniqueAwemeIds.includes(aweme.aweme_id)) {
            formattedDetails[aweme.aweme_id] = tiktokUtils.formatAwemeItemResponse(
              aweme
            ) as IAwemeDetails
          }
        })
      })

      missingAwemeIds = uniqueAwemeIds.filter((id) => !formattedDetails[id])
      retryCount++
    }

    return formattedDetails
  } catch (error) {
    throw new Error('Failed to fetch aweme details')
  }
}

const TiktokApi = {
  getUserInfoByUsername,
  getUserAwemeList,
  getMultiAwemeDetails
}

export default TiktokApi
```

## File: `src/shared/configs/download-client.ts`
```typescript
import axios from 'axios'
import http from 'http'
import https from 'https'

export const httpAgent = new http.Agent({
  keepAlive: true,
  maxSockets: 64,
  maxFreeSockets: 16
})

export const httpsAgent = new https.Agent({
  keepAlive: true,
  maxSockets: 64,
  maxFreeSockets: 16
})

export const downloadClient = axios.create({
  timeout: 30000,
  maxRedirects: 5,
  httpAgent,
  httpsAgent
})
```

## File: `src/shared/constants/index.ts`
```typescript
const TIKTOK_API_URL = {
  GET_USER_AWEME_LIST: 'https://aggr22-normal-alisg.tiktokv.com/lite/v2/public/item/list/',
  GET_MULTI_AWEME_DETAIL: 'https://api22-core-c-alisg.tiktokv.com/lite/v2/feed/fyp/'
} as const

const DEFAULT_USER_AGENT =
  'com.zhiliaoapp.musically/2023501030 (Linux; U; Android 13; en_US; Pixel 7; Build/TD1A.220804.031; Cronet/58.0.2991.0)'

const TIKTOK_POST_DETAIL_URL_PATTERN =
  /tiktok\.com\/(?:@[A-Za-z0-9._-]+)\/(?:video|photo)\/(\d+)(?:\?.*)?$/

export { TIKTOK_API_URL, DEFAULT_USER_AGENT, TIKTOK_POST_DETAIL_URL_PATTERN }
```

## File: `src/shared/types/tiktok.type.ts`
```typescript
export interface IGetAwemeListCursor {
  cursor: string
  maxCursor: string
}

export interface ITiktokVideo {
  coverUri: string
  mp4Uri: string
}

export interface ITiktokAwemeItemStats {
  likes: number
  comments: number
  shares: number
  views: number
  collects: number
}

export interface IAwemeDetails {
  id: string
  url: string
  description: string
  createdAt: number
  type: 'PHOTO' | 'VIDEO'
  stats: ITiktokAwemeItemStats
  video?: ITiktokVideo
  imagesUri?: string[]
  musicUri?: string
}

export interface IAwemeListResponse {
  awemeList: IAwemeDetails[]
  pagination: IGetAwemeListCursor & {
    hasMore: boolean
  }
}

export interface IUserInfo {
  id: string
  uniqueId: string
  secUid: string
  followerCount: number
  followingCount: number
  avatarUri: string
}
```

## File: `src/shared/types/ipc/index.ts`
```typescript
import { IpcEventApi } from '@shared/types/ipc/ipc-event.type'
import { IpcInvokeHandlers, IpcResponse } from '@shared/types/ipc/ipc-invoke.type'

export interface IpcApi
  extends Omit<IpcInvokeHandlers, 'getSettings' | 'saveSettings'>, IpcEventApi {
  getSettings: <T = unknown>(key: string) => Promise<IpcResponse<T>>
  saveSettings: <T>(key: string, value: T) => Promise<void>
}
```

## File: `src/shared/types/ipc/ipc-event.type.ts`
```typescript
import type { ProgressInfo, UpdateDownloadedEvent, UpdateInfo } from 'electron-updater'

export type UpdateAvailableInfo = UpdateInfo
export type UpdateNotAvailableInfo = UpdateInfo
export type UpdateDownloadedInfo = UpdateDownloadedEvent
export type DownloadProgressInfo = ProgressInfo
export type UpdateErrorInfo = Error

export interface IpcEventContract {
  onUpdateAvailable: UpdateAvailableInfo
  onUpdateDownloaded: UpdateDownloadedInfo
  onDownloadProgress: DownloadProgressInfo
  onUpdateError: UpdateErrorInfo
  onUpdateNotAvailable: UpdateNotAvailableInfo

  onCheckingForUpdate: void
}

export const IPC_EVENT_CHANNELS: { [K in IpcEventMethod]: string } = {
  onUpdateAvailable: 'UPDATE_AVAILABLE',
  onUpdateDownloaded: 'UPDATE_DOWNLOADED',
  onDownloadProgress: 'DOWNLOAD_PROGRESS',
  onUpdateError: 'UPDATE_ERROR',
  onCheckingForUpdate: 'CHECKING_FOR_UPDATE',
  onUpdateNotAvailable: 'UPDATE_NOT_AVAILABLE'
}

export type IpcEventMethod = keyof IpcEventContract
export type IpcEventPayload<K extends IpcEventMethod> = IpcEventContract[K]
type EventUnsubscribe = () => void

export type IpcEventApi = {
  [K in IpcEventMethod]: IpcEventPayload<K> extends void
    ? (callback: () => void) => EventUnsubscribe
    : (callback: (payload: IpcEventPayload<K>) => void) => EventUnsubscribe
}
```

## File: `src/shared/types/ipc/ipc-invoke.type.ts`
```typescript
import {
  IAwemeDetails,
  IAwemeListResponse,
  IGetAwemeListCursor,
  IUserInfo
} from '@shared/types/tiktok.type'

export interface IpcGetAwemeListOptions extends IGetAwemeListCursor {
  cookie?: string
}

export interface IpcGetAwemeDetailsOptions {
  cookie?: string
}

export interface IDownloadFileOptions {
  url: string
  fileName: string
  folderPath: string
  retryCount?: number
}

export type IpcResponse<T> =
  | {
      success: true
      data: T
      error?: never
    }
  | {
      success: false
      error: string
      data?: never
    }

type Rpc<Args extends unknown[] = [], Response = void> = {
  args: Args
  response: Response
}

// Single source of truth for all ipcRenderer.invoke/ipcMain.handle methods.
export interface IpcInvokeContract {
  getUserInfo: Rpc<[username: string, options?: IpcGetAwemeDetailsOptions], IpcResponse<IUserInfo>>
  getUserAwemeList: Rpc<
    [secUid: string, options?: IpcGetAwemeListOptions],
    IpcResponse<IAwemeListResponse>
  >
  getMultiAwemeDetails: Rpc<
    [awemeIds: string[], options?: IpcGetAwemeDetailsOptions],
    IpcResponse<Record<string, IAwemeDetails>>
  >
  selectFolder: Rpc<[], IpcResponse<string | null>>
  downloadFile: Rpc<[options: IDownloadFileOptions], IpcResponse<boolean>>
  getDefaultDownloadPath: Rpc<[], IpcResponse<string>>
  getSettings: Rpc<[key: string], IpcResponse<unknown>>
  saveSettings: Rpc<[key: string, value: unknown], void>
  checkForUpdates: Rpc<[], void>
  downloadUpdate: Rpc<[], void>
  quitAndInstall: Rpc<[], void>
}

export const IPC_INVOKE_CHANNELS: { [K in IpcInvokeMethod]: string } = {
  getUserInfo: 'GET_USER_INFO',
  getUserAwemeList: 'GET_USER_AWEME_LIST',
  getMultiAwemeDetails: 'GET_MULTI_AWEME_DETAILS',
  selectFolder: 'SELECT_FOLDER',
  downloadFile: 'DOWNLOAD_FILE',
  getDefaultDownloadPath: 'GET_DEFAULT_DOWNLOAD_PATH',
  getSettings: 'GET_SETTINGS',
  saveSettings: 'SAVE_SETTINGS',
  checkForUpdates: 'CHECK_FOR_UPDATES',
  downloadUpdate: 'DOWNLOAD_UPDATE',
  quitAndInstall: 'QUIT_AND_INSTALL'
}

export type IpcInvokeMethod = keyof IpcInvokeContract
export type IpcInvokeArgs<K extends IpcInvokeMethod> = IpcInvokeContract[K]['args']
export type IpcInvokeResponse<K extends IpcInvokeMethod> = IpcInvokeContract[K]['response']

export type IpcInvokeHandlers = {
  [K in IpcInvokeMethod]: (...args: IpcInvokeArgs<K>) => Promise<IpcInvokeResponse<K>>
}
```

## File: `src/shared/utils/common.util.ts`
```typescript
export async function promisePool<T>({
  items,
  concurrency,
  worker
}: {
  items: T[]
  concurrency: number
  worker: (item: T, index: number) => Promise<void>
}) {
  let index = 0

  const next = async (): Promise<void> => {
    const i = index++
    if (i >= items.length) return

    await worker(items[i], i)
    await next()
  }

  const workers = Array(Math.min(concurrency, items.length))
    .fill(0)
    .map(() => next())

  await Promise.all(workers)
}
```

## File: `src/shared/utils/file.util.ts`
```typescript
import fs from 'fs'

class FileUtils {
  static async ensureDirectory(folderPath: string): Promise<void> {
    await fs.promises.mkdir(folderPath, { recursive: true })
  }

  static createWriteStream(
    filePath: string,
    options?: Parameters<typeof fs.createWriteStream>[1]
  ): fs.WriteStream {
    return fs.createWriteStream(filePath, options)
  }

  static async deleteFile(filePath: string): Promise<void> {
    if (!filePath) {
      return
    }

    if (fs.existsSync(filePath)) {
      await fs.promises.unlink(filePath).catch(() => undefined)
    }
  }
}

export default FileUtils
```

## File: `src/shared/utils/tiktok.util.ts`
```typescript
import { v4 as uuidv4 } from 'uuid'
import sanitize from 'sanitize-filename'

import { IAwemeDetails, ITiktokAwemeItemStats, ITiktokVideo } from '@shared/types/tiktok.type'

const getHighestQualityVideoUri = (bitRateArr: any): string => {
  if (!Array.isArray(bitRateArr) || bitRateArr.length === 0) {
    return ''
  }
  const highestQualityVideo = bitRateArr.reduce((prev: any, current: any) => {
    const prevResolution = (prev?.play_addr?.width || 0) * (prev?.play_addr?.height || 0)
    const currentResolution = (current?.play_addr?.width || 0) * (current?.play_addr?.height || 0)
    return currentResolution > prevResolution ? current : prev
  })
  return highestQualityVideo?.play_addr?.url_list?.at(-1) || ''
}

const formatAwemeItemResponse = (item: any): IAwemeDetails | null => {
  try {
    const id = item.aweme_id
    const url = item.share_url
    const description = item.desc
    const createdAt = item.create_time
    const type = item.image_post_info ? 'PHOTO' : 'VIDEO'
    const stats: ITiktokAwemeItemStats = {
      likes: item.statistics.digg_count,
      comments: item.statistics.comment_count,
      shares: item.statistics.share_count,
      views: item.statistics.play_count,
      collects: item.statistics.collect_count
    }
    const imagesUri =
      type === 'PHOTO'
        ? item.image_post_info.images.map((img: any) => img.display_image.url_list[0])
        : []
    const musicUri = item.music?.play_url?.url_list?.[0] || ''
    const video: ITiktokVideo | undefined =
      type === 'VIDEO'
        ? {
            coverUri: item.video.origin_cover?.url_list?.[0] || '',
            mp4Uri: getHighestQualityVideoUri(item.video.bit_rate)
          }
        : undefined
    return {
      id,
      url,
      description,
      createdAt,
      type,
      stats,
      video,
      imagesUri,
      musicUri
    }
  } catch (error) {
    return null
  }
}

const bytesToHex = (bytes: Uint8Array): string => {
  return Array.from(bytes)
    .map((b) => b.toString(16).padStart(2, '0'))
    .join('')
}

const randomBytes = (size: number): Uint8Array => {
  const bytes = new Uint8Array(size)
  crypto.getRandomValues(bytes)
  return bytes
}

const getBaseMobileParams = () => {
  const device_id = '7555746395380368897'
  const iid = '7580036180676593416'

  const cdid = uuidv4()
  const openudid = bytesToHex(randomBytes(8))
  const timestamp = Math.floor(Date.now() / 1000)
  return {
    _rticket: Date.now(),
    device_id,
    ts: timestamp,
    iid,
    openudid,
    cdid,
    manifest_version_code: 420506,
    app_language: 'en',
    app_type: 'normal',
    app_package: 'com.zhiliaoapp.musically.go',
    channel: 'googleplay',
    device_type: 'SM-G998B',
    language: 'en',
    host_abi: 'x86_64',
    locale: 'en',
    resolution: '900*1600',
    update_version_code: 420506,
    ac2: 'wifi5g',
    sys_region: 'US',
    os_api: 28,
    timezone_name: 'Asia/Saigon',
    dpi: 240,
    carrier_region: 'VN',
    ac: 'wifi',
    os: 'android',
    os_version: '12',
    timezone_offset: 25200,
    version_code: 420506,
    app_name: 'musically_go',
    ab_version: '42.5.6',
    version_name: '42.5.6',
    device_brand: 'samsung',
    op_region: 'VN',
    ssmix: 'a',
    device_platform: 'android',
    build_number: '42.5.6',
    region: 'VN',
    aid: 1340
  }
}

export type TFileNameFormatOption = 'id' | 'timestamp' | 'numericalOrder' | 'title'
export const getFilename = ({
  order,
  id,
  title,
  timestamp,
  format
}: {
  order?: number | string
  id?: string
  title?: string
  timestamp?: number | string
  format: TFileNameFormatOption[]
}) => {
  const defaultFilename = [order, id].filter((part) => Boolean(part)).join('_')

  if (!format || format.length === 0) {
    return sanitize(defaultFilename)
  }

  const parts = format.map((f) => {
    switch (f) {
      case 'numericalOrder':
        return order
      case 'id':
        return id
      case 'title':
        return title ? sanitize(title) : ''
      case 'timestamp':
        return timestamp
      default:
        return ''
    }
  })

  // Remove empty parts and join by underscore
  let filename = parts.filter((part) => Boolean(part)).join('_')

  /**
   * Remove zero-width characters and format control characters.
   * These valid unicode characters can cause "Invalid filename" errors in chrome.downloads API.
   *
   * \u200B-\u200F: Zero Width Space, ZWNJ, ZWJ, LRM, RLM
   * \u202A-\u202E: LRE, RLE, PDF, LRO, RLO
   * \u2060-\u206F: Word Joiner, Function Application, Invisible Separator, Bidi Isolates...
   * \uFE00-\uFE0F: Variation Selectors (inclusive of \uFE0E)
   */
  filename = filename.replace(/[\u200B-\u200F\u202A-\u202E\u2060-\u206F\uFE00-\uFE0F]/g, '')

  return sanitize(filename || defaultFilename)
}

const tiktokUtils = {
  formatAwemeItemResponse,
  getBaseMobileParams,
  getFilename
}

export default tiktokUtils
```


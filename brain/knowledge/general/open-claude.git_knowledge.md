---
id: open-claude.git-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:15.093810
---

# KNOWLEDGE EXTRACT: open-claude.git
> **Extracted on:** 2026-03-30 13:22:58
> **Source:** open-claude.git

---

## File: `.gitignore`
```
# Dependencies
node_modules/

# Build outputs
dist/
release/
static/js/

# OS files
.DS_Store
Thumbs.db

# IDE
.idea/
.vscode/
*.swp
*.swo

# Logs
*.log
npm-debug.log*
pnpm-debug.log*

# Lock files (optional - remove if you want to commit pnpm-lock.yaml)
# pnpm-lock.yaml

# Environment
.env
.env.local
```

## File: `CODEOWNERS`
```
# Code owners for open-claude
# These users will be requested for review and can approve PRs

# Default owners for everything in the repo
* @tkattkat
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2024

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
  "name": "open-claude",
  "productName": "Open Claude",
  "version": "1.0.0",
  "description": "Open Claude - A custom Claude client",
  "main": "dist/main.js",
  "scripts": {
    "build": "tsc && pnpm run build:renderer",
    "build:renderer": "esbuild src/renderer/main.ts --bundle --outfile=static/js/main.js --format=esm --platform=browser && esbuild src/renderer/spotlight.ts --bundle --outfile=static/js/spotlight.js --format=esm --platform=browser && esbuild src/renderer/settings.ts --bundle --outfile=static/js/settings.js --format=esm --platform=browser",
    "start": "pnpm run build && electron .",
    "dev": "pnpm run build && electron .",
    "pack": "pnpm run build && electron-builder --dir",
    "dist": "pnpm run build && electron-builder"
  },
  "build": {
    "appId": "com.openclaude.app",
    "productName": "Open Claude",
    "directories": {
      "output": "release"
    },
    "files": [
      "dist/**/*",
      "static/**/*"
    ],
    "mac": {
      "category": "public.app-category.productivity",
      "icon": "build/icon.icns",
      "target": [
        {
          "target": "dmg",
          "arch": [
            "universal"
          ]
        }
      ]
    },
    "dmg": {
      "title": "Open Claude",
      "icon": "build/icon.icns"
    },
    "win": {
      "icon": "build/icon.png",
      "target": [
        {
          "target": "nsis",
          "arch": ["x64"]
        }
      ]
    },
    "nsis": {
      "oneClick": false,
      "allowToChangeInstallationDirectory": true
    }
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "electron-store": "^11.0.2",
    "marked": "^17.0.1"
  },
  "devDependencies": {
    "@types/node": "^24.10.1",
    "electron": "^39.2.6",
    "electron-builder": "^26.0.12",
    "esbuild": "^0.27.1",
    "typescript": "^5.9.3"
  }
}
```

## File: `README.md`
```markdown
# Open Claude

A native macOS desktop client for Claude with a clean, minimal interface and system-wide quick access.

## Disclaimer

This project is an independent, open-source research and educational project. It is not affiliated with, endorsed by, or sponsored by Anthropic. "Claude" is a trademark of Anthropic, PBC.

This client requires a valid claude.ai account and authenticates through the official web login. It does not bypass any authentication or access controls. Usage is subject to Anthropic's [Terms of Service](https://www.anthropic.com/legal/consumer-terms) and [Acceptable Use Policy](https://www.anthropic.com/legal/aup).

This software is provided "as is" for educational and personal productivity purposes. The authors make no warranties and assume no liability for its use.

<img width="2226" height="1866" alt="Main Interface" src="https://github.com/user-attachments/assets/7c36f018-2659-4eff-805f-eedee1491c87" />

## Features

### Native macOS Experience
- Transparent window with vibrancy effects (under-window blur)
- Native traffic light controls with custom positioning
- System font rendering with SF Pro Display
- Dark mode support

### Spotlight Search
Press `Cmd+Shift+C` from anywhere to open a floating Spotlight-style search bar. Ask quick questions without leaving your current workflow.

- Always-on-top floating window
- Closes automatically when clicking outside
- Uses Claude Haiku for fast responses
- Maintains conversation context within a session
- Auto-resizes based on response length

<img width="1990" height="758" alt="Spotlight" src="https://github.com/user-attachments/assets/540ddc9c-1eee-4801-a96a-78d28a7bc0f3" />

### Conversation Management
- Create, rename, and delete conversations
- Star important conversations
- Auto-generated titles based on conversation content
- Conversation history with timestamps

### Streaming Responses
- Real-time streaming text display
- Extended thinking support with collapsible summaries
- Tool use visualization
- Stop generation at any time

### Model Support
- Claude Opus 4.5 (default for main chat)
- Claude Haiku 4.5 (Spotlight quick queries)

## Installation

### Pre-built Releases
Download the latest DMG for your architecture:
- `Open Claude-x.x.x-arm64.dmg` - Apple Silicon (M1/M2/M3)
- `Open Claude-x.x.x.dmg` - Intel

### Build from Source

```bash
# Clone the repository
git clone https://github.com/tkattkat/open-claude.git
cd open-claude

# Install dependencies
pnpm install

# Development
pnpm dev

# Build from source to desktop app
pnpm dist
```

## Authentication

Open Claude uses your existing claude.ai account. Click "Sign in with Claude" to authenticate through the standard web login flow. Your session is stored securely using electron-store.

## Screenshots

### Login
<img width="2166" height="1512" alt="Login" src="https://github.com/user-attachments/assets/1281ad7a-e3f9-4b7f-ad06-90b005175ab1" />

### Conversation View
<img width="2020" height="1578" alt="Conversation" src="https://github.com/user-attachments/assets/153ee10b-b8a0-42f5-9e6f-8b138272a27f" />


## Roadmap

- [ ] MCP (Model Context Protocol) server support
- [x] File attachments and image uploads
- [ ] Custom keyboard shortcuts configuration
- [ ] Multiple conversation windows
- [ ] Export conversations to Markdown

## Tech Stack

- Electron 39
- TypeScript

```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "src/renderer/**/*"]
}
```

## File: `src/main.ts`
```typescript
import { app, BrowserWindow, ipcMain, session, globalShortcut, screen, dialog } from 'electron';
import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { isAuthenticated, getOrgId, makeRequest, streamCompletion, stopResponse, generateTitle, store, BASE_URL, prepareAttachmentPayload } from './api/client';
import { createStreamState, processSSEChunk, type StreamCallbacks } from './streaming/parser';
import type { SettingsSchema, AttachmentPayload, UploadFilePayload } from './types';

// Track multiple main windows
const mainWindows: Map<number, BrowserWindow> = new Map();
let spotlightWindow: BrowserWindow | null = null;
let settingsWindow: BrowserWindow | null = null;

// Default settings
const DEFAULT_SETTINGS: SettingsSchema = {
  spotlightKeybind: 'CommandOrControl+Shift+C',
  spotlightPersistHistory: true,
  newWindowKeybind: 'CommandOrControl+Shift+N',
};

// Get settings with defaults
function getSettings(): SettingsSchema {
  const stored = store.get('settings');
  return { ...DEFAULT_SETTINGS, ...stored };
}

// Save settings
function saveSettings(settings: Partial<SettingsSchema>) {
  const current = getSettings();
  store.set('settings', { ...current, ...settings });
}

// Register global shortcuts
function registerShortcuts() {
  globalShortcut.unregisterAll();
  const settings = getSettings();

  // Spotlight shortcut (toggle)
  const spotlightKeybind = settings.spotlightKeybind || DEFAULT_SETTINGS.spotlightKeybind;
  try {
    globalShortcut.register(spotlightKeybind, () => {
      toggleSpotlightWindow();
    });
  } catch (e) {
    console.error('Failed to register spotlight keybind:', spotlightKeybind, e);
    globalShortcut.register(DEFAULT_SETTINGS.spotlightKeybind, () => {
      toggleSpotlightWindow();
    });
  }

  // New window shortcut
  const newWindowKeybind = settings.newWindowKeybind || DEFAULT_SETTINGS.newWindowKeybind;
  try {
    globalShortcut.register(newWindowKeybind, () => {
      createMainWindow();
    });
  } catch (e) {
    console.error('Failed to register new window keybind:', newWindowKeybind, e);
    globalShortcut.register(DEFAULT_SETTINGS.newWindowKeybind, () => {
      createMainWindow();
    });
  }
}

// Backwards compatibility alias
function registerSpotlightShortcut() {
  registerShortcuts();
}

// Toggle spotlight window (open if closed, close if open)
function toggleSpotlightWindow() {
  if (spotlightWindow && !spotlightWindow.isDestroyed()) {
    spotlightWindow.close();
    return;
  }
  createSpotlightWindow();
}

// Create spotlight search window
function createSpotlightWindow() {
  if (spotlightWindow && !spotlightWindow.isDestroyed()) {
    spotlightWindow.focus();
    return;
  }

  const primaryDisplay = screen.getPrimaryDisplay();
  const { width: screenWidth } = primaryDisplay.workAreaSize;

  const isMac = process.platform === 'darwin';

  spotlightWindow = new BrowserWindow({
    width: 600,
    height: 56,
    x: Math.round((screenWidth - 600) / 2),
    y: 180,
    frame: false,
    transparent: isMac,
    ...(isMac ? {
      vibrancy: 'under-window',
      visualEffectState: 'active',
      backgroundColor: '#00000000',
    } : {
      backgroundColor: '#1a1a1a',
    }),
    resizable: false,
    movable: true,
    minimizable: false,
    maximizable: false,
    closable: true,
    alwaysOnTop: true,
    skipTaskbar: true,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  spotlightWindow.loadFile(path.join(__dirname, '../static/spotlight.html'));

  // Close on blur (clicking outside)
  spotlightWindow.on('blur', () => {
    if (spotlightWindow && !spotlightWindow.isDestroyed()) {
      spotlightWindow.close();
    }
  });

  spotlightWindow.on('closed', () => {
    spotlightWindow = null;
  });
}

function createMainWindow(): BrowserWindow {
  const isMac = process.platform === 'darwin';

  const newWindow = new BrowserWindow({
    width: 900,
    height: 700,
    ...(isMac ? {
      transparent: true,
      vibrancy: 'under-window',
      visualEffectState: 'active',
      backgroundColor: '#00000000',
      titleBarStyle: 'hiddenInset',
      trafficLightPosition: { x: 16, y: 16 },
    } : {
      backgroundColor: '#1a1a1a',
    }),
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  const windowId = newWindow.id;
  mainWindows.set(windowId, newWindow);

  newWindow.loadFile(path.join(__dirname, '../static/index.html'));

  newWindow.on('closed', () => {
    mainWindows.delete(windowId);
  });

  return newWindow;
}

// Get the first main window (for backwards compatibility)
function getMainWindow(): BrowserWindow | null {
  const windows = Array.from(mainWindows.values());
  return windows.length > 0 ? windows[0] : null;
}

// Create settings window
function createSettingsWindow() {
  if (settingsWindow && !settingsWindow.isDestroyed()) {
    settingsWindow.focus();
    return;
  }

  const isMac = process.platform === 'darwin';

  settingsWindow = new BrowserWindow({
    width: 480,
    height: 520,
    minWidth: 400,
    minHeight: 400,
    ...(isMac ? {
      transparent: true,
      vibrancy: 'under-window',
      visualEffectState: 'active',
      backgroundColor: '#00000000',
      titleBarStyle: 'hiddenInset',
      trafficLightPosition: { x: 16, y: 16 },
    } : {
      backgroundColor: '#1a1a1a',
    }),
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  settingsWindow.loadFile(path.join(__dirname, '../static/settings.html'));

  settingsWindow.on('closed', () => {
    settingsWindow = null;
  });
}

// IPC handlers

// Spotlight window resize
ipcMain.handle('spotlight-resize', async (_event, height: number) => {
  if (spotlightWindow && !spotlightWindow.isDestroyed()) {
    const maxHeight = 700;
    const newHeight = Math.min(height, maxHeight);
    spotlightWindow.setSize(600, newHeight);
  }
});

// Spotlight conversation state
let spotlightConversationId: string | null = null;
let spotlightParentMessageUuid: string | null = null;
let spotlightMessages: Array<{ role: 'user' | 'assistant'; text: string }> = [];
let spotlightDraftInput: string = '';

// Spotlight send message (uses Haiku)
ipcMain.handle('spotlight-send', async (_event, message: string) => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  if (!spotlightConversationId) {
    const createResult = await makeRequest(
      `${BASE_URL}/api/organizations/${orgId}/chat_conversations`,
      'POST',
      { name: '', model: 'claude-haiku-4-5-20251001' }
    );

    if (createResult.status !== 201 && createResult.status !== 200) {
      throw new Error('Failed to create conversation');
    }

    const convData = createResult.data as { uuid: string };
    spotlightConversationId = convData.uuid;
    spotlightParentMessageUuid = null;
  }

  const conversationId = spotlightConversationId;
  const parentMessageUuid = spotlightParentMessageUuid || conversationId;

  // Store user message
  spotlightMessages.push({ role: 'user', text: message });

  const state = createStreamState();

  const callbacks: StreamCallbacks = {
    onTextDelta: (text, fullText) => {
      spotlightWindow?.webContents.send('spotlight-stream', { text, fullText });
    },
    onThinkingStart: () => {
      spotlightWindow?.webContents.send('spotlight-thinking', { isThinking: true });
    },
    onThinkingDelta: (thinking) => {
      spotlightWindow?.webContents.send('spotlight-thinking-stream', { thinking });
    },
    onThinkingStop: (thinkingText) => {
      spotlightWindow?.webContents.send('spotlight-thinking', { isThinking: false, thinkingText });
    },
    onToolStart: (toolName, msg) => {
      spotlightWindow?.webContents.send('spotlight-tool', { toolName, isRunning: true, message: msg });
    },
    onToolStop: (toolName, input) => {
      spotlightWindow?.webContents.send('spotlight-tool', { toolName, isRunning: false, input });
    },
    onToolResult: (toolName, result, isError) => {
      spotlightWindow?.webContents.send('spotlight-tool-result', { toolName, isError, result });
    },
    onComplete: (fullText, _steps, messageUuid) => {
      // Store assistant response
      spotlightMessages.push({ role: 'assistant', text: fullText });
      spotlightWindow?.webContents.send('spotlight-complete', { fullText, messageUuid });
    }
  };

  await streamCompletion(orgId, conversationId, message, parentMessageUuid, (chunk) => {
    processSSEChunk(chunk, state, callbacks);
  });

  if (state.lastMessageUuid) {
    spotlightParentMessageUuid = state.lastMessageUuid;
  }

  return { conversationId, fullText: state.fullResponse, messageUuid: state.lastMessageUuid };
});

// Reset spotlight conversation when window is closed
ipcMain.handle('spotlight-reset', async () => {
  const settings = getSettings();
  // Only reset if persist history is disabled
  if (!settings.spotlightPersistHistory) {
    spotlightConversationId = null;
    spotlightParentMessageUuid = null;
    spotlightMessages = [];
  }
});

// Get spotlight conversation history from local state
ipcMain.handle('spotlight-get-history', async () => {
  const settings = getSettings();
  if (!settings.spotlightPersistHistory) {
    return { hasHistory: false, messages: [], draftInput: '' };
  }

  return {
    hasHistory: spotlightMessages.length > 0,
    messages: spotlightMessages,
    draftInput: spotlightDraftInput
  };
});

// Save spotlight draft input
ipcMain.handle('spotlight-save-draft', async (_event, draft: string) => {
  spotlightDraftInput = draft;
});

// Force new spotlight conversation
ipcMain.handle('spotlight-new-chat', async () => {
  spotlightConversationId = null;
  spotlightParentMessageUuid = null;
  spotlightMessages = [];
  spotlightDraftInput = '';
});

ipcMain.handle('get-auth-status', async () => {
  return isAuthenticated();
});

ipcMain.handle('login', async () => {
  const authWindow = new BrowserWindow({
    width: 500,
    height: 700,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
    },
    title: 'Sign in to Claude',
  });

  authWindow.loadURL(`${BASE_URL}/login`);

  const checkCookies = async (): Promise<{ success: boolean; error?: string } | null> => {
    const cookies = await session.defaultSession.cookies.get({ domain: '.claude.ai' });
    const sessionKey = cookies.find(c => c.name === 'sessionKey')?.value;
    const orgId = cookies.find(c => c.name === 'lastActiveOrg')?.value;

    if (sessionKey && orgId) {
      console.log('[Auth] Got cookies from webview!');
      authWindow.close();
      store.set('orgId', orgId);
      return { success: true };
    }
    return null;
  };

  return new Promise((resolve) => {
    authWindow.webContents.on('did-finish-load', async () => {
      const result = await checkCookies();
      if (result) resolve(result);
    });

    const interval = setInterval(async () => {
      if (authWindow.isDestroyed()) {
        clearInterval(interval);
        return;
      }
      const result = await checkCookies();
      if (result) {
        clearInterval(interval);
        resolve(result);
      }
    }, 1000);

    authWindow.on('closed', () => {
      clearInterval(interval);
      resolve({ success: false, error: 'Window closed' });
    });
  });
});

ipcMain.handle('logout', async () => {
  store.clear();
  await session.defaultSession.clearStorageData({ storages: ['cookies'] });
  return { success: true };
});

// Create a new conversation
ipcMain.handle('create-conversation', async (_event, model?: string) => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  const conversationId = crypto.randomUUID();
  const url = `${BASE_URL}/api/organizations/${orgId}/chat_conversations`;

  console.log('[API] Creating conversation:', conversationId, 'with model:', model || 'claude-opus-4-5-20251101');
  console.log('[API] URL:', url);

  const result = await makeRequest(url, 'POST', {
    uuid: conversationId,
    name: '',
    model: model || 'claude-opus-4-5-20251101',
    project_uuid: null,
    create_mode: null
  });

  console.log('[API] Create conversation response:', result.status, JSON.stringify(result.data));

  if (result.status !== 200 && result.status !== 201) {
    throw new Error(`Failed to create conversation: ${result.status} - ${JSON.stringify(result.data)}`);
  }

  // The response includes the conversation data with uuid
  const data = result.data as { uuid?: string };
  return { conversationId, parentMessageUuid: data.uuid || conversationId, ...(result.data as object) };
});

// Get list of conversations
ipcMain.handle('get-conversations', async () => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  const url = `${BASE_URL}/api/organizations/${orgId}/chat_conversations?limit=30&consistency=eventual`;
  const result = await makeRequest(url, 'GET');

  if (result.status !== 200) {
    throw new Error(`Failed to get conversations: ${result.status}`);
  }

  return result.data;
});

// Load a specific conversation with messages
ipcMain.handle('load-conversation', async (_event, convId: string) => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  const url = `${BASE_URL}/api/organizations/${orgId}/chat_conversations/${convId}?tree=True&rendering_mode=messages&render_all_tools=true&consistency=eventual`;
  const result = await makeRequest(url, 'GET');

  if (result.status !== 200) {
    throw new Error(`Failed to load conversation: ${result.status}`);
  }

  return result.data;
});

// Delete a conversation
ipcMain.handle('delete-conversation', async (_event, convId: string) => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  const url = `${BASE_URL}/api/organizations/${orgId}/chat_conversations/${convId}`;
  const result = await makeRequest(url, 'DELETE');

  if (result.status !== 200 && result.status !== 204) {
    throw new Error(`Failed to delete conversation: ${result.status}`);
  }

  return { success: true };
});

// Rename a conversation
ipcMain.handle('rename-conversation', async (_event, convId: string, name: string) => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  const url = `${BASE_URL}/api/organizations/${orgId}/chat_conversations/${convId}`;
  const result = await makeRequest(url, 'PUT', { name });

  if (result.status !== 200) {
    throw new Error(`Failed to rename conversation: ${result.status}`);
  }

  return result.data;
});

// Star/unstar a conversation
ipcMain.handle('star-conversation', async (_event, convId: string, isStarred: boolean) => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  const url = `${BASE_URL}/api/organizations/${orgId}/chat_conversations/${convId}?rendering_mode=raw`;
  const result = await makeRequest(url, 'PUT', { is_starred: isStarred });

  if (result.status !== 202) {
    throw new Error(`Failed to star conversation: ${result.status}`);
  }

  return result.data;
});

// Export conversation to Markdown
ipcMain.handle('export-conversation-markdown', async (event, conversationData: { title: string; messages: Array<{ role: string; content: string; timestamp?: string }> }) => {
  const { title, messages } = conversationData;

  // Get the window that sent this request
  const senderWindow = BrowserWindow.fromWebContents(event.sender);

  // Build markdown content
  let markdown = `# ${title || 'Conversation'}\n\n`;
  markdown += `_Exported on ${new Date().toLocaleString()}_\n\n---\n\n`;

  for (const msg of messages) {
    const role = msg.role === 'human' ? 'You' : 'Claude';
    const timestamp = msg.timestamp ? ` _(${new Date(msg.timestamp).toLocaleString()})_` : '';
    markdown += `## ${role}${timestamp}\n\n`;
    markdown += `${msg.content}\n\n---\n\n`;
  }

  // Show save dialog
  const result = await dialog.showSaveDialog(senderWindow || getMainWindow()!, {
    title: 'Export Conversation',
    defaultPath: `${title || 'conversation'}.md`,
    filters: [
      { name: 'Markdown', extensions: ['md'] },
      { name: 'All Files', extensions: ['*'] }
    ]
  });

  if (result.canceled || !result.filePath) {
    return { success: false, canceled: true };
  }

  // Write file
  try {
    fs.writeFileSync(result.filePath, markdown, 'utf-8');
    return { success: true, filePath: result.filePath };
  } catch (error) {
    console.error('Failed to write file:', error);
    return { success: false, error: 'Failed to write file' };
  }
});

// Create a new window
ipcMain.handle('new-window', async () => {
  const newWindow = createMainWindow();
  return { windowId: newWindow.id };
});

// Upload file attachments (prepare metadata only)
ipcMain.handle('upload-attachments', async (_event, files: UploadFilePayload[]) => {
  const uploads: AttachmentPayload[] = [];
  for (const file of files || []) {
    const attachment = await prepareAttachmentPayload(file);
    uploads.push(attachment);
  }

  return uploads;
});

// Send a message and stream response
ipcMain.handle('send-message', async (event, conversationId: string, message: string, parentMessageUuid: string, attachments: AttachmentPayload[] = []) => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  // Get the window that sent this message
  const senderWindow = BrowserWindow.fromWebContents(event.sender);

  console.log('[API] Sending message to conversation:', conversationId);
  console.log('[API] Parent message UUID:', parentMessageUuid);
  console.log('[API] Message:', message.substring(0, 50) + '...');
  if (attachments?.length) {
    console.log('[API] Attachments:', attachments.map(a => `${a.file_name} (${a.file_size})`).join(', '));
    console.log('[API] File IDs:', attachments.map(a => a.document_id).join(', '));
  }

  const state = createStreamState();

  const callbacks: StreamCallbacks = {
    onTextDelta: (text, fullText, blockIndex) => {
      senderWindow?.webContents.send('message-stream', { conversationId, blockIndex, text, fullText });
    },
    onThinkingStart: (blockIndex) => {
      senderWindow?.webContents.send('message-thinking', { conversationId, blockIndex, isThinking: true });
    },
    onThinkingDelta: (thinking, blockIndex) => {
      const block = state.contentBlocks.get(blockIndex);
      senderWindow?.webContents.send('message-thinking-stream', {
        conversationId,
        blockIndex,
        thinking,
        summaries: block?.summaries
      });
    },
    onThinkingStop: (thinkingText, summaries, blockIndex) => {
      senderWindow?.webContents.send('message-thinking', {
        conversationId,
        blockIndex,
        isThinking: false,
        thinkingText,
        summaries
      });
    },
    onToolStart: (toolName, toolMessage, blockIndex) => {
      senderWindow?.webContents.send('message-tool-use', {
        conversationId,
        blockIndex,
        toolName,
        message: toolMessage,
        isRunning: true
      });
    },
    onToolStop: (toolName, input, blockIndex) => {
      const block = state.contentBlocks.get(blockIndex);
      senderWindow?.webContents.send('message-tool-use', {
        conversationId,
        blockIndex,
        toolName,
        message: block?.toolMessage,
        input,
        isRunning: false
      });
    },
    onToolResult: (toolName, result, isError, blockIndex) => {
      senderWindow?.webContents.send('message-tool-result', {
        conversationId,
        blockIndex,
        toolName,
        result,
        isError
      });
    },
    onCitation: (citation, blockIndex) => {
      senderWindow?.webContents.send('message-citation', { conversationId, blockIndex, citation });
    },
    onToolApproval: (toolName, approvalKey, input) => {
      senderWindow?.webContents.send('message-tool-approval', { conversationId, toolName, approvalKey, input });
    },
    onCompaction: (status, compactionMessage) => {
      senderWindow?.webContents.send('message-compaction', { conversationId, status, message: compactionMessage });
    },
    onComplete: (fullText, steps, messageUuid) => {
      senderWindow?.webContents.send('message-complete', { conversationId, fullText, steps, messageUuid });
    }
  };

  // Send Claude the uploaded file UUIDs (metadata stays client-side for display)
  const fileIds = attachments?.map(a => a.document_id).filter(Boolean) || [];

  await streamCompletion(orgId, conversationId, message, parentMessageUuid, (chunk) => {
    processSSEChunk(chunk, state, callbacks);
  }, { attachments: [], files: fileIds });

  return { text: state.fullResponse, messageUuid: state.lastMessageUuid };
});

// Stop a streaming response
ipcMain.handle('stop-response', async (_event, conversationId: string) => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  console.log('[API] Stopping response for conversation:', conversationId);
  await stopResponse(orgId, conversationId);
  return { success: true };
});

// Generate title for a conversation
ipcMain.handle('generate-title', async (_event, conversationId: string, messageContent: string, recentTitles: string[] = []) => {
  const orgId = await getOrgId();
  if (!orgId) throw new Error('Not authenticated');

  console.log('[API] Generating title for conversation:', conversationId);
  const result = await generateTitle(orgId, conversationId, messageContent, recentTitles);
  return result;
});

// Settings IPC handlers
ipcMain.handle('open-settings', async () => {
  createSettingsWindow();
});

ipcMain.handle('get-settings', async () => {
  return getSettings();
});

ipcMain.handle('save-settings', async (_event, settings: Partial<SettingsSchema>) => {
  saveSettings(settings);
  // Re-register shortcuts if any keybind changed
  if (settings.spotlightKeybind !== undefined || settings.newWindowKeybind !== undefined) {
    registerShortcuts();
  }
  return getSettings();
});

// Handle deep link on Windows (single instance)
const gotTheLock = app.requestSingleInstanceLock();
if (!gotTheLock) {
  app.quit();
} else {
  app.on('second-instance', () => {
    const mainWindow = getMainWindow();
    if (mainWindow) {
      if (mainWindow.isMinimized()) mainWindow.restore();
      mainWindow.focus();
    }
  });
}

app.whenReady().then(() => {
  createMainWindow();

  // Register spotlight shortcut from settings
  registerSpotlightShortcut();

  app.on('activate', () => {
    if (mainWindows.size === 0) {
      createMainWindow();
    }
  });
});

// Unregister shortcuts when app quits
app.on('will-quit', () => {
  globalShortcut.unregisterAll();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
```

## File: `src/preload.ts`
```typescript
import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('claude', {
  getAuthStatus: () => ipcRenderer.invoke('get-auth-status'),
  login: () => ipcRenderer.invoke('login'),
  logout: () => ipcRenderer.invoke('logout'),
  createConversation: (model?: string) => ipcRenderer.invoke('create-conversation', model),
  getConversations: () => ipcRenderer.invoke('get-conversations'),
  loadConversation: (convId: string) => ipcRenderer.invoke('load-conversation', convId),
  deleteConversation: (convId: string) => ipcRenderer.invoke('delete-conversation', convId),
  renameConversation: (convId: string, name: string) => ipcRenderer.invoke('rename-conversation', convId, name),
  starConversation: (convId: string, isStarred: boolean) => ipcRenderer.invoke('star-conversation', convId, isStarred),
  exportConversationMarkdown: (conversationData: { title: string; messages: Array<{ role: string; content: string; timestamp?: string }> }) =>
    ipcRenderer.invoke('export-conversation-markdown', conversationData),
  generateTitle: (convId: string, messageContent: string, recentTitles?: string[]) => ipcRenderer.invoke('generate-title', convId, messageContent, recentTitles || []),
  sendMessage: (conversationId: string, message: string, parentMessageUuid: string, attachments?: unknown[]) =>
    ipcRenderer.invoke('send-message', conversationId, message, parentMessageUuid, attachments || []),
  uploadAttachments: (files: Array<{ name: string; size: number; type: string; data: ArrayBuffer | Uint8Array | number[] }>) =>
    ipcRenderer.invoke('upload-attachments', files),
  stopResponse: (conversationId: string) => ipcRenderer.invoke('stop-response', conversationId),

  // Stream listeners
  onMessageStream: (callback: (data: { conversationId: string; text: string; fullText: string }) => void) => {
    ipcRenderer.on('message-stream', (_event, data) => callback(data));
  },
  onMessageComplete: (callback: (data: {
    conversationId: string;
    fullText: string;
    steps?: Array<{
      type: 'thinking' | 'tool';
      index: number;
      thinkingText?: string;
      toolName?: string;
      toolInput?: string;
      toolResult?: unknown;
      isError?: boolean;
    }>;
    messageUuid: string
  }) => void) => {
    ipcRenderer.on('message-complete', (_event, data) => callback(data));
  },
  onMessageThinking: (callback: (data: { conversationId: string; blockIndex: number; isThinking: boolean; thinkingText?: string }) => void) => {
    ipcRenderer.on('message-thinking', (_event, data) => callback(data));
  },
  onMessageThinkingStream: (callback: (data: { conversationId: string; blockIndex: number; thinking: string }) => void) => {
    ipcRenderer.on('message-thinking-stream', (_event, data) => callback(data));
  },
  onMessageToolUse: (callback: (data: { conversationId: string; blockIndex: number; toolName: string; message: string; input?: string; isRunning: boolean }) => void) => {
    ipcRenderer.on('message-tool-use', (_event, data) => callback(data));
  },
  onMessageToolResult: (callback: (data: { conversationId: string; blockIndex: number; toolName: string; result?: unknown; isError: boolean }) => void) => {
    ipcRenderer.on('message-tool-result', (_event, data) => callback(data));
  },
  // Citation events (for inline source citations)
  onMessageCitation: (callback: (data: { conversationId: string; blockIndex: number; citation: { uuid: string; start_index: number; end_index?: number; url?: string; title?: string } }) => void) => {
    ipcRenderer.on('message-citation', (_event, data) => callback(data));
  },
  // Tool approval events (for MCP tools requiring permission)
  onMessageToolApproval: (callback: (data: { conversationId: string; toolName: string; approvalKey: string; input?: unknown }) => void) => {
    ipcRenderer.on('message-tool-approval', (_event, data) => callback(data));
  },
  // Compaction status (conversation compaction)
  onMessageCompaction: (callback: (data: { conversationId: string; status: string; message?: string }) => void) => {
    ipcRenderer.on('message-compaction', (_event, data) => callback(data));
  },
  removeStreamListeners: () => {
    ipcRenderer.removeAllListeners('message-stream');
    ipcRenderer.removeAllListeners('message-complete');
    ipcRenderer.removeAllListeners('message-thinking');
    ipcRenderer.removeAllListeners('message-thinking-stream');
    ipcRenderer.removeAllListeners('message-tool-use');
    ipcRenderer.removeAllListeners('message-tool-result');
    ipcRenderer.removeAllListeners('message-citation');
    ipcRenderer.removeAllListeners('message-tool-approval');
    ipcRenderer.removeAllListeners('message-compaction');
  },

  // Spotlight functions
  spotlightResize: (height: number) => ipcRenderer.invoke('spotlight-resize', height),
  spotlightSend: (message: string) => ipcRenderer.invoke('spotlight-send', message),
  onSpotlightStream: (callback: (data: { text: string; fullText: string }) => void) => {
    ipcRenderer.on('spotlight-stream', (_event, data) => callback(data));
  },
  onSpotlightComplete: (callback: (data: { fullText: string }) => void) => {
    ipcRenderer.on('spotlight-complete', (_event, data) => callback(data));
  },
  onSpotlightThinking: (callback: (data: { isThinking: boolean; thinkingText?: string }) => void) => {
    ipcRenderer.on('spotlight-thinking', (_event, data) => callback(data));
  },
  onSpotlightThinkingStream: (callback: (data: { thinking: string }) => void) => {
    ipcRenderer.on('spotlight-thinking-stream', (_event, data) => callback(data));
  },
  onSpotlightTool: (callback: (data: { toolName: string; isRunning: boolean; message?: string; input?: string }) => void) => {
    ipcRenderer.on('spotlight-tool', (_event, data) => callback(data));
  },
  onSpotlightToolResult: (callback: (data: { toolName: string; isError: boolean; result?: unknown }) => void) => {
    ipcRenderer.on('spotlight-tool-result', (_event, data) => callback(data));
  },
  removeSpotlightListeners: () => {
    ipcRenderer.removeAllListeners('spotlight-stream');
    ipcRenderer.removeAllListeners('spotlight-complete');
    ipcRenderer.removeAllListeners('spotlight-thinking');
    ipcRenderer.removeAllListeners('spotlight-thinking-stream');
    ipcRenderer.removeAllListeners('spotlight-tool');
    ipcRenderer.removeAllListeners('spotlight-tool-result');
  },
  spotlightReset: () => ipcRenderer.invoke('spotlight-reset'),
  spotlightGetHistory: () => ipcRenderer.invoke('spotlight-get-history'),
  spotlightNewChat: () => ipcRenderer.invoke('spotlight-new-chat'),
  spotlightSaveDraft: (draft: string) => ipcRenderer.invoke('spotlight-save-draft', draft),

  // Search modal toggle (triggered by global Command+K shortcut)
  onToggleSearchModal: (callback: () => void) => {
    ipcRenderer.on('toggle-search-modal', () => callback());
  },

  // Settings functions
  openSettings: () => ipcRenderer.invoke('open-settings'),
  getSettings: () => ipcRenderer.invoke('get-settings'),
  saveSettings: (settings: { spotlightKeybind?: string; spotlightPersistHistory?: boolean; newWindowKeybind?: string }) =>
    ipcRenderer.invoke('save-settings', settings),

  // Window management
  newWindow: () => ipcRenderer.invoke('new-window'),
});
```

## File: `src/api/client.ts`
```typescript
import { net, session } from 'electron';
import Store from 'electron-store';
import crypto from 'crypto';
import type { StoreSchema, ApiResponse, AttachmentPayload, UploadFilePayload } from '../types';

const BASE_URL = 'https://claude.ai';

// Store instance
const store = new Store<StoreSchema>() as Store<StoreSchema> & {
  get<K extends keyof StoreSchema>(key: K): StoreSchema[K];
  set<K extends keyof StoreSchema>(key: K, value: StoreSchema[K]): void;
  clear(): void;
};

// Generate stable device/anonymous IDs
export function getDeviceId(): string {
  let deviceId = store.get('deviceId');
  if (!deviceId) {
    deviceId = crypto.randomUUID();
    store.set('deviceId', deviceId);
  }
  return deviceId;
}

export function getAnonymousId(): string {
  let anonId = store.get('anonymousId');
  if (!anonId) {
    anonId = `claudeai.v1.${crypto.randomUUID()}`;
    store.set('anonymousId', anonId);
  }
  return anonId;
}

// Convert various binary inputs to a Node.js Buffer
function toBuffer(data: UploadFilePayload['data']): Buffer {
  if (Buffer.isBuffer(data)) return data;
  if (data instanceof ArrayBuffer) return Buffer.from(new Uint8Array(data));
  if (data instanceof Uint8Array) return Buffer.from(data);
  return Buffer.from(data);
}

// Normalize upload response into AttachmentPayload
function normalizeAttachmentResponse(data: any, fallback: UploadFilePayload): AttachmentPayload {
  const doc = data?.document || data || {};
  const documentId = doc.document_id || doc.file_uuid || doc.uuid || doc.id || doc.file_id;
  const fileUrl =
    doc.file_url ||
    doc.preview_url ||
    doc.thumbnail_url ||
    doc.url ||
    data?.download_url;

  if (!documentId) {
    throw new Error('Upload response missing document identifier');
  }

  const normalizedUrl = fileUrl
    ? (fileUrl.startsWith('http') ? fileUrl : `${BASE_URL}${fileUrl}`)
    : undefined;

  return {
    document_id: documentId,
    file_name: doc.file_name || doc.fileName || fallback.name,
    file_size: doc.size_bytes || doc.file_size || doc.fileSize || fallback.size,
    file_type: doc.file_type || doc.mime_type || doc.fileType || doc.file_kind || fallback.type || 'application/octet-stream',
    file_url: normalizedUrl,
    extracted_content: doc.extracted_content || doc.extract || doc.extracted_text
  };
}

// Upload a single attachment and normalize the response
export async function prepareAttachmentPayload(file: UploadFilePayload): Promise<AttachmentPayload> {
  const orgId = await getOrgId();
  if (!orgId) {
    throw new Error('Not authenticated');
  }

  const boundary = '----ElectronFormBoundary' + crypto.randomBytes(16).toString('hex');
  const fileBuffer = toBuffer(file.data);
  const body = Buffer.concat([
    Buffer.from(`--${boundary}\r\n`),
    Buffer.from(`Content-Disposition: form-data; name="file"; filename="${file.name}"\r\n`),
    Buffer.from(`Content-Type: ${file.type || 'application/octet-stream'}\r\n\r\n`),
    fileBuffer,
    Buffer.from(`\r\n--${boundary}--\r\n`)
  ]);

  return new Promise((resolve, reject) => {
    const request = net.request({
      url: `${BASE_URL}/api/${orgId}/upload`,
      method: 'POST',
      useSessionCookies: true,
    });

    request.setHeader('accept', '*/*');
    request.setHeader('content-type', `multipart/form-data; boundary=${boundary}`);
    request.setHeader('origin', BASE_URL);
    request.setHeader('referer', `${BASE_URL}/new`);
    request.setHeader('anthropic-client-platform', 'web_claude_ai');
    request.setHeader('anthropic-device-id', getDeviceId());
    request.setHeader('anthropic-anonymous-id', getAnonymousId());
    request.setHeader(
      'user-agent',
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    );

    let responseData = '';
    let statusCode = 0;

    request.on('response', (response) => {
      statusCode = response.statusCode;

      response.on('data', (chunk) => {
        responseData += chunk.toString();
      });

      response.on('end', () => {
        try {
          const parsed = responseData ? JSON.parse(responseData) : null;
          if (statusCode !== 200) {
            reject(new Error(`Upload failed: ${statusCode} - ${responseData}`));
            return;
          }
          const attachment = normalizeAttachmentResponse(parsed, file);
          console.log(`[API] Uploaded attachment: ${attachment.file_name} (${attachment.file_size} bytes)`);
          resolve(attachment);
        } catch (err) {
          reject(new Error(`Upload parse failed: ${err instanceof Error ? err.message : String(err)}`));
        }
      });
    });

    request.on('error', (error) => {
      reject(error);
    });

    request.write(body);
    request.end();
  });
}

// Check if we have valid session cookies
export async function isAuthenticated(): Promise<boolean> {
  const cookies = await session.defaultSession.cookies.get({ domain: '.claude.ai' });
  const sessionKey = cookies.find(c => c.name === 'sessionKey')?.value;
  const orgId = cookies.find(c => c.name === 'lastActiveOrg')?.value;
  return !!(sessionKey && orgId);
}

// Get org ID from cookies
export async function getOrgId(): Promise<string | null> {
  const cookies = await session.defaultSession.cookies.get({ domain: '.claude.ai' });
  return cookies.find(c => c.name === 'lastActiveOrg')?.value || null;
}

// Set common headers on a request
function setCommonHeaders(request: Electron.ClientRequest): void {
  request.setHeader('accept', 'application/json, text/event-stream');
  request.setHeader('content-type', 'application/json');
  request.setHeader('origin', BASE_URL);
  request.setHeader('anthropic-client-platform', 'web_claude_ai');
  request.setHeader('anthropic-device-id', getDeviceId());
  request.setHeader('anthropic-anonymous-id', getAnonymousId());
  request.setHeader('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
}

// Make authenticated request using Electron net (includes session cookies)
export async function makeRequest(
  url: string,
  method: 'GET' | 'POST' | 'PUT' | 'DELETE' = 'GET',
  body?: object
): Promise<ApiResponse> {
  return new Promise((resolve, reject) => {
    const request = net.request({
      url,
      method,
      useSessionCookies: true,
    });

    setCommonHeaders(request);

    let responseData = '';
    let statusCode = 0;

    request.on('response', (response) => {
      statusCode = response.statusCode;

      response.on('data', (chunk) => {
        responseData += chunk.toString();
      });

      response.on('end', () => {
        try {
          const data = responseData ? JSON.parse(responseData) : null;
          resolve({ status: statusCode, data });
        } catch {
          resolve({ status: statusCode, data: responseData });
        }
      });
    });

    request.on('error', (error) => {
      reject(error);
    });

    if (body) {
      request.write(JSON.stringify(body));
    }
    request.end();
  });
}

// Stream response for completion endpoint
export async function streamCompletion(
  orgId: string,
  conversationId: string,
  prompt: string,
  parentMessageUuid: string,
  onData: (chunk: string) => void,
  options: {
    attachments?: AttachmentPayload[];
    files?: Array<AttachmentPayload | string>;
    sync_sources?: unknown[];
  } = {}
): Promise<void> {
  return new Promise((resolve, reject) => {
    const url = `${BASE_URL}/api/organizations/${orgId}/chat_conversations/${conversationId}/completion`;

    const request = net.request({
      url,
      method: 'POST',
      useSessionCookies: true,
    });

    request.setHeader('accept', 'text/event-stream, text/event-stream');
    request.setHeader('accept-language', 'en-US,en;q=0.9');
    request.setHeader('content-type', 'application/json');
    request.setHeader('origin', BASE_URL);
    request.setHeader('referer', `${BASE_URL}/chat/${conversationId}`);
    request.setHeader('anthropic-client-platform', 'web_claude_ai');
    request.setHeader('anthropic-client-version', '1.0.0');
    request.setHeader('anthropic-device-id', getDeviceId());
    request.setHeader('anthropic-anonymous-id', getAnonymousId());
    request.setHeader('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');

    const files = (options.files || []).map((file) => typeof file === 'string' ? file : file.document_id);

    const body = {
      prompt,
      parent_message_uuid: parentMessageUuid === conversationId ? null : parentMessageUuid,
      timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
      personalized_styles: [{
        type: 'default',
        key: 'Default',
        name: 'Normal',
        nameKey: 'normal_style_name',
        prompt: 'Normal',
        summary: 'Default responses from Claude',
        summaryKey: 'normal_style_summary',
        isDefault: true
      }],
      locale: 'en-US',
      tools: [
        { type: 'web_search_v0', name: 'web_search' },
        { type: 'artifacts_v0', name: 'artifacts' },
        { type: 'repl_v0', name: 'repl' }
      ],
      attachments: options.attachments || [],
      files,
      sync_sources: options.sync_sources || [],
      rendering_mode: 'messages'
    };

    request.on('response', (response) => {
      if (response.statusCode !== 200) {
        let errorData = '';
        response.on('data', (chunk) => { errorData += chunk.toString(); });
        response.on('end', () => {
          reject(new Error(`Completion failed: ${response.statusCode} - ${errorData}`));
        });
        return;
      }

      let buffer = '';
      response.on('data', (chunk) => {
        buffer += chunk.toString();
        // Process complete lines
        const lines = buffer.split('\n');
        buffer = lines.pop() || ''; // Keep incomplete line in buffer
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            onData(line + '\n');
          }
        }
      });

      response.on('end', () => {
        resolve();
      });
    });

    request.on('error', (error) => {
      reject(error);
    });

    request.write(JSON.stringify(body));
    request.end();
  });
}

// Stop a streaming response
export async function stopResponse(
  orgId: string,
  conversationId: string
): Promise<void> {
  const url = `${BASE_URL}/api/organizations/${orgId}/chat_conversations/${conversationId}/stop_response`;

  return new Promise((resolve, reject) => {
    const request = net.request({
      url,
      method: 'POST',
      useSessionCookies: true,
    });

    setCommonHeaders(request);

    request.on('response', (response) => {
      if (response.statusCode !== 200 && response.statusCode !== 204) {
        reject(new Error(`Stop response failed: ${response.statusCode}`));
        return;
      }
      resolve();
    });

    request.on('error', (error) => {
      reject(error);
    });

    request.end();
  });
}

// Generate title for a conversation
export async function generateTitle(
  orgId: string,
  conversationId: string,
  messageContent: string,
  recentTitles: string[] = []
): Promise<{ title: string }> {
  const url = `${BASE_URL}/api/organizations/${orgId}/chat_conversations/${conversationId}/title`;
  const result = await makeRequest(url, 'POST', {
    message_content: messageContent,
    recent_titles: recentTitles
  });

  if (result.status !== 202) {
    throw new Error(`Failed to generate title: ${result.status}`);
  }

  return result.data as { title: string };
}

// Export store and BASE_URL for use in other modules
export { store, BASE_URL };
```

## File: `src/renderer/main.ts`
```typescript
import { parseMarkdown } from './markdown.js';


declare global {
  interface Window {
    claude: {
      getAuthStatus: () => Promise<boolean>;
      login: () => Promise<{ success: boolean; error?: string }>;
      logout: () => Promise<void>;
      createConversation: (model?: string) => Promise<{ conversationId: string; parentMessageUuid: string; uuid?: string }>;
      getConversations: () => Promise<Conversation[]>;
      loadConversation: (convId: string) => Promise<ConversationData>;
      deleteConversation: (convId: string) => Promise<void>;
      renameConversation: (convId: string, name: string) => Promise<void>;
      starConversation: (convId: string, isStarred: boolean) => Promise<void>;
      exportConversationMarkdown: (conversationData: { title: string; messages: Array<{ role: string; content: string; timestamp?: string }> }) => Promise<{ success: boolean; canceled?: boolean; filePath?: string }>;
      sendMessage: (convId: string, message: string, parentUuid: string, attachments?: AttachmentPayload[]) => Promise<void>;
      stopResponse: (convId: string) => Promise<void>;
      generateTitle: (convId: string, messageContent: string) => Promise<void>;
      uploadAttachments: (files: Array<{ name: string; size: number; type: string; data: ArrayBuffer | Uint8Array | number[] }>) => Promise<UploadedAttachmentPayload[]>;
      openSettings: () => Promise<void>;
      getSettings: () => Promise<{ spotlightKeybind?: string; spotlightPersistHistory?: boolean }>;
      saveSettings: (settings: { spotlightKeybind?: string; spotlightPersistHistory?: boolean }) => Promise<{ spotlightKeybind?: string; spotlightPersistHistory?: boolean }>;
      newWindow: () => Promise<{ windowId: number }>;
      onMessageThinking: (callback: (data: ThinkingData) => void) => void;
      onMessageThinkingStream: (callback: (data: ThinkingStreamData) => void) => void;
      onMessageToolUse: (callback: (data: ToolUseData) => void) => void;
      onMessageToolResult: (callback: (data: ToolResultData) => void) => void;
      onMessageStream: (callback: (data: StreamData) => void) => void;
      onMessageComplete: (callback: (data: CompleteData) => void) => void;
    };
  }
}

interface Conversation {
  uuid: string;
  name?: string;
  summary?: string;
  is_starred?: boolean;
  updated_at: string;
}

interface ConversationData {
  name?: string;
  chat_messages?: Message[];
}

interface FileAsset {
  url: string;
  file_variant?: string;
  primary_color?: string;
  image_width?: number;
  image_height?: number;
}

interface MessageFile {
  file_kind: string;
  file_uuid: string;
  file_name: string;
  created_at?: string;
  thumbnail_url?: string;
  preview_url?: string;
  thumbnail_asset?: FileAsset;
  preview_asset?: FileAsset;
}

interface Message {
  uuid?: string;
  sender: string;
  content?: ContentBlock[];
  text?: string;
  created_at?: string;
  files?: MessageFile[];
  files_v2?: MessageFile[];
}

interface ContentBlock {
  type: string;
  text?: string;
  thinking?: string;
  summaries?: { summary: string }[];
  name?: string;
  message?: string;
  display_content?: { text?: string };
  input?: unknown;
  content?: unknown[];
  is_error?: boolean;
  citations?: Citation[];
}

interface Citation {
  url?: string;
  title?: string;
  start_index?: number;
  end_index?: number;
}

interface AttachmentPayload {
  document_id: string;
  file_name: string;
  file_size: number;
  file_type: string;
  file_url?: string;
  extracted_content?: string;
}

interface UploadedAttachmentPayload extends AttachmentPayload {}

interface UploadedAttachment extends AttachmentPayload {
  id: string;
  previewUrl?: string;
}

interface ThinkingData {
  conversationId: string;
  blockIndex: number;
  isThinking: boolean;
  thinkingText?: string;
}

interface ThinkingStreamData {
  conversationId: string;
  blockIndex: number;
  thinking: string;
  summary?: string;
}

interface ToolUseData {
  conversationId: string;
  blockIndex: number;
  toolName: string;
  message?: string;
  input?: unknown;
  isRunning: boolean;
}

interface ToolResultData {
  conversationId: string;
  blockIndex: number;
  toolName: string;
  result: unknown;
  isError: boolean;
}

interface StreamData {
  conversationId: string;
  blockIndex?: number;
  fullText: string;
}

interface CompleteData {
  conversationId: string;
  fullText: string;
  steps: Step[];
  messageUuid: string;
}

interface Step {
  type: string;
  text?: string;
  thinkingText?: string;
  thinkingSummary?: string;
  summary?: string;
  toolName?: string;
  toolMessage?: string;
  message?: string;
  toolResult?: unknown;
  toolInput?: unknown;
  isError?: boolean;
  isActive?: boolean;
  index?: number;
  citations?: Citation[];
}

interface StreamingBlock {
  text?: string;
  summary?: string;
  isActive?: boolean;
  name?: string;
  message?: string;
  input?: unknown;
  result?: unknown;
  isRunning?: boolean;
  isError?: boolean;
}


let conversationId: string | null = null;
let parentMessageUuid: string | null = null;
let isLoading = false;
let currentStreamingElement: HTMLElement | null = null;
let streamingMessageUuid: string | null = null;
let conversations: Conversation[] = [];
let selectedModel = 'claude-opus-4-5-20251101';
let openDropdownId: string | null = null;
let pendingAttachments: UploadedAttachment[] = [];
let uploadingAttachments = false;
let attachmentError = '';
let currentConversationTitle = '';
let currentConversationMessages: Array<{ role: string; content: string; timestamp?: string }> = [];

const modelDisplayNames: Record<string, string> = {
  'claude-opus-4-5-20251101': 'Opus 4.5',
  'claude-sonnet-4-5-20250929': 'Sonnet 4.5',
  'claude-haiku-4-5-20251001': 'Haiku 4.5'
};

const streamingBlocks = {
  thinkingBlocks: new Map<number, StreamingBlock>(),
  toolBlocks: new Map<number, StreamingBlock>(),
  textBlocks: new Map<number, StreamingBlock>(),
  textContent: ''
};

function resetStreamingBlocks() {
  streamingBlocks.thinkingBlocks.clear();
  streamingBlocks.toolBlocks.clear();
  streamingBlocks.textBlocks.clear();
  streamingBlocks.textContent = '';
}

const $ = (id: string) => document.getElementById(id);
const $$ = (selector: string) => document.querySelectorAll(selector);

function escapeHtml(text: string): string {
  return (text || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function formatFileSize(bytes: number): string {
  if (!bytes) return '0 B';
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.min(Math.floor(Math.log(bytes) / Math.log(1024)), sizes.length - 1);
  const value = bytes / Math.pow(1024, i);
  return `${value.toFixed(value >= 10 || i === 0 ? 0 : 1)} ${sizes[i]}`;
}

function removeAttachment(id: string) {
  pendingAttachments = pendingAttachments.filter(a => a.id !== id);
  renderAttachmentList();
}

const imageIconSvg = `<svg class="attachment-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>`;
const fileIconSvg = `<svg class="attachment-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>`;

function renderAttachmentList() {
  const containers = [
    { list: $('attachment-list'), status: $('attachment-status') },
    { list: $('home-attachment-list'), status: $('home-attachment-status') }
  ];

  const pills = pendingAttachments.map(a => {
    const icon = a.file_type?.startsWith('image/') ? imageIconSvg : fileIconSvg;
    return `
      <div class="attachment-pill" data-id="${a.id}">
        <div class="attachment-icon">${icon}</div>
        <div class="attachment-meta">
          <div class="attachment-name">${escapeHtml(a.file_name)}</div>
          <div class="attachment-size">${formatFileSize(a.file_size)}</div>
        </div>
        <button class="attachment-remove" data-id="${a.id}" title="Remove">✕</button>
      </div>
    `;
  }).join('');

  containers.forEach(({ list, status }) => {
    if (!list) return;
    const hasContent = pendingAttachments.length > 0 || uploadingAttachments || !!attachmentError;
    list.parentElement?.classList.toggle('visible', hasContent);
    list.innerHTML = pills;

    list.querySelectorAll('.attachment-remove').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const id = (btn as HTMLElement).dataset.id;
        if (id) removeAttachment(id);
      });
    });

    if (status) {
      status.textContent = uploadingAttachments ? 'Uploading attachments…' : attachmentError;
      status.style.display = (uploadingAttachments || attachmentError) ? 'block' : 'none';
      status.classList.toggle('error', !!attachmentError);
    }
  });
}

function clearAttachments() {
  pendingAttachments = [];
  attachmentError = '';
  uploadingAttachments = false;
  renderAttachmentList();
}

function getAttachmentPayloads(): AttachmentPayload[] {
  return pendingAttachments.map(a => ({
    document_id: a.document_id,
    file_name: a.file_name,
    file_size: a.file_size,
    file_type: a.file_type,
    file_url: a.file_url,
    extracted_content: a.extracted_content
  }));
}

async function handleFileSelection(fileList: FileList | null) {
  if (!fileList || fileList.length === 0) return;

  attachmentError = '';
  uploadingAttachments = true;
  renderAttachmentList();

  try {
    const uploadPayload = await Promise.all(Array.from(fileList).map(async (file) => ({
      name: file.name,
      size: file.size,
      type: file.type || 'application/octet-stream',
      data: await file.arrayBuffer()
    })));

    const results = await window.claude.uploadAttachments(uploadPayload);
    const normalized = results.map(res => ({
      id: crypto.randomUUID(),
      document_id: res.document_id,
      file_name: res.file_name,
      file_size: res.file_size,
      file_type: res.file_type,
      file_url: res.file_url,
      extracted_content: res.extracted_content
    }));

    pendingAttachments = [...pendingAttachments, ...normalized];
  } catch (e: any) {
    attachmentError = e?.message || 'Failed to upload attachments';
  } finally {
    uploadingAttachments = false;
    renderAttachmentList();
  }
}

function autoResize(el: HTMLTextAreaElement) {
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 120) + 'px';
}

function autoResizeHome(el: HTMLTextAreaElement) {
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 200) + 'px';
}

function formatDate(dateStr: string): string {
  const date = new Date(dateStr);
  const now = new Date();
  const diff = now.getTime() - date.getTime();
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  if (days === 0) return 'Today';
  if (days === 1) return 'Yesterday';
  if (days < 7) return `${days} days ago`;
  return date.toLocaleDateString();
}

function scrollToBottom() {
  const m = $('messages');
  if (m) m.scrollTop = m.scrollHeight;
}

function hideEmptyState() {
  const e = $('empty-state');
  if (e) e.style.display = 'none';
}

function showLogin() {
  const login = $('login');
  const home = $('home');
  const chat = $('chat');
  const sidebarTab = $('sidebar-tab');

  if (login) login.style.display = 'flex';
  if (home) home.classList.remove('active');
  if (chat) chat.classList.remove('active');
  if (sidebarTab) sidebarTab.classList.add('hidden');
  closeSidebar();
}

function showHome() {
  const login = $('login');
  const home = $('home');
  const chat = $('chat');
  const sidebarTab = $('sidebar-tab');
  const homeInput = $('home-input') as HTMLTextAreaElement;

  if (login) login.style.display = 'none';
  if (home) home.classList.add('active');
  if (chat) chat.classList.remove('active');
  if (sidebarTab) sidebarTab.classList.remove('hidden');
  if (homeInput) setTimeout(() => homeInput.focus(), 100);
}

function showChat() {
  const login = $('login');
  const home = $('home');
  const chat = $('chat');
  const sidebarTab = $('sidebar-tab');
  const modelBadge = document.querySelector('.model-badge');

  if (login) login.style.display = 'none';
  if (home) home.classList.remove('active');
  if (chat) chat.classList.add('active');
  if (sidebarTab) sidebarTab.classList.remove('hidden');
  if (modelBadge) modelBadge.textContent = modelDisplayNames[selectedModel] || 'Opus 4.5';
}

// Sidebar functions
function toggleSidebar() {
  const sidebar = $('sidebar');
  const overlay = $('sidebar-overlay');
  const sidebarTab = $('sidebar-tab');

  if (!sidebar || !overlay || !sidebarTab) return;

  const isOpening = !sidebar.classList.contains('open');
  sidebar.classList.toggle('open');
  overlay.classList.toggle('open');

  if (isOpening) {
    sidebarTab.classList.add('hidden');
    loadConversationsList();
  } else {
    sidebarTab.classList.remove('hidden');
  }
}

function closeSidebar() {
  const sidebar = $('sidebar');
  const overlay = $('sidebar-overlay');
  const sidebarTab = $('sidebar-tab');

  if (sidebar) sidebar.classList.remove('open');
  if (overlay) overlay.classList.remove('open');
  if (sidebarTab) sidebarTab.classList.remove('hidden');
}

// Model selection
function selectModel(btn: HTMLElement) {
  $$('.model-option').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  selectedModel = btn.getAttribute('data-model') || selectedModel;
}

// Conversations list
async function loadConversationsList() {
  const content = $('sidebar-content');
  if (!content) return;

  try {
    conversations = await window.claude.getConversations();
    renderConversationsList();
  } catch (e) {
    content.innerHTML = '<div class="conv-loading">Failed to load</div>';
  }
}

function renderConversationItem(c: Conversation): string {
  return `
    <div class="conv-item ${c.uuid === conversationId ? 'active' : ''}" data-uuid="${c.uuid}" data-starred="${c.is_starred || false}">
      <div class="conv-item-row">
        <div class="conv-item-info" data-action="load" data-uuid="${c.uuid}">
          <div class="conv-item-title">${escapeHtml(c.name || c.summary || 'New conversation')}</div>
          <div class="conv-item-date">${formatDate(c.updated_at)}</div>
        </div>
        <button class="conv-menu-btn" data-action="menu" data-uuid="${c.uuid}">⋯</button>
      </div>
      <div class="conv-dropdown" id="conv-dropdown-${c.uuid}">
        <div class="conv-dropdown-item" data-action="star" data-uuid="${c.uuid}" data-starred="${!c.is_starred}">
          <span class="conv-dropdown-icon">${c.is_starred ? '☆' : '★'}</span>
          <span>${c.is_starred ? 'Unstar' : 'Star'}</span>
        </div>
        <div class="conv-dropdown-item" data-action="rename" data-uuid="${c.uuid}">
          <span class="conv-dropdown-icon">✎</span>
          <span>Rename</span>
        </div>
        <div class="conv-dropdown-item delete" data-action="delete" data-uuid="${c.uuid}">
          <span class="conv-dropdown-icon">✕</span>
          <span>Delete</span>
        </div>
      </div>
    </div>
  `;
}

function renderConversationsList() {
  const content = $('sidebar-content');
  if (!content) return;

  if (!conversations || conversations.length === 0) {
    content.innerHTML = '<div class="conv-loading">No conversations yet</div>';
    return;
  }

  const starred = conversations.filter(c => c.is_starred);
  const unstarred = conversations.filter(c => !c.is_starred);

  let html = '';

  if (starred.length > 0) {
    html += '<div class="conv-section-header">Favorites</div>';
    html += starred.map(renderConversationItem).join('');
  }

  if (unstarred.length > 0) {
    if (starred.length > 0) {
      html += '<div class="conv-section-header">Recent</div>';
    }
    html += unstarred.map(renderConversationItem).join('');
  }

  content.innerHTML = html;

  // Add event listeners
  content.querySelectorAll('[data-action]').forEach(el => {
    el.addEventListener('click', handleConversationAction);
  });
}

function handleConversationAction(e: Event) {
  e.stopPropagation();
  const target = e.currentTarget as HTMLElement;
  const action = target.dataset.action;
  const uuid = target.dataset.uuid;

  if (!uuid) return;

  switch (action) {
    case 'load':
      loadConversation(uuid);
      break;
    case 'menu':
      toggleConvMenu(uuid);
      break;
    case 'star':
      starConversation(uuid, target.dataset.starred === 'true');
      break;
    case 'rename':
      startRenameConversation(uuid);
      break;
    case 'delete':
      deleteConversation(uuid);
      break;
  }
}

function toggleConvMenu(uuid: string) {
  const dropdown = $(`conv-dropdown-${uuid}`);
  if (!dropdown) return;

  if (openDropdownId && openDropdownId !== uuid) {
    const oldDropdown = $(`conv-dropdown-${openDropdownId}`);
    if (oldDropdown) oldDropdown.classList.remove('open');
  }

  dropdown.classList.toggle('open');
  openDropdownId = dropdown.classList.contains('open') ? uuid : null;
}

async function deleteConversation(uuid: string) {
  const deletedConv = conversations.find(c => c.uuid === uuid);
  conversations = conversations.filter(c => c.uuid !== uuid);

  if (uuid === conversationId) {
    conversationId = null;
    parentMessageUuid = null;
    closeSidebar();
    showHome();
  } else {
    renderConversationsList();
  }

  try {
    await window.claude.deleteConversation(uuid);
  } catch (e) {
    console.error('Failed to delete conversation:', e);
    if (deletedConv) {
      conversations.push(deletedConv);
      conversations.sort((a, b) => new Date(b.updated_at).getTime() - new Date(a.updated_at).getTime());
      renderConversationsList();
    }
  }
}

async function starConversation(uuid: string, isStarred: boolean) {
  const conv = conversations.find(c => c.uuid === uuid);
  const previousState = conv?.is_starred;
  if (conv) conv.is_starred = isStarred;
  renderConversationsList();

  try {
    await window.claude.starConversation(uuid, isStarred);
  } catch (e) {
    console.error('Failed to star conversation:', e);
    if (conv) conv.is_starred = previousState;
    renderConversationsList();
  }
}

function startRenameConversation(uuid: string) {
  const convItem = document.querySelector(`.conv-item[data-uuid="${uuid}"]`);
  if (!convItem) return;

  const dropdown = $(`conv-dropdown-${uuid}`);
  if (dropdown) dropdown.classList.remove('open');
  openDropdownId = null;

  const conv = conversations.find(c => c.uuid === uuid);
  const currentName = conv?.name || conv?.summary || '';

  const titleEl = convItem.querySelector('.conv-item-title');
  if (!titleEl) return;

  titleEl.innerHTML = `<input type="text" class="conv-rename-input" value="${escapeHtml(currentName)}" data-uuid="${uuid}">`;
  const input = titleEl.querySelector('input') as HTMLInputElement;
  input.focus();
  input.select();

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      finishRename(uuid, input.value);
    } else if (e.key === 'Escape') {
      e.preventDefault();
      renderConversationsList();
    }
  });

  input.addEventListener('blur', () => {
    finishRename(uuid, input.value);
  });
}

async function finishRename(uuid: string, newName: string) {
  const trimmedName = newName.trim();
  if (!trimmedName) {
    renderConversationsList();
    return;
  }

  const conv = conversations.find(c => c.uuid === uuid);
  const previousName = conv?.name;
  if (conv) conv.name = trimmedName;
  renderConversationsList();

  try {
    await window.claude.renameConversation(uuid, trimmedName);
  } catch (e) {
    console.error('Failed to rename conversation:', e);
    if (conv) conv.name = previousName;
    renderConversationsList();
  }
}

// SVG icons
const pencilSvg = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>`;
const checkSvg = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
const closeSvg = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`;
const chevronSvg = `<svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor"><path d="M14.128 7.16482C14.3126 6.95983 14.6298 6.94336 14.835 7.12771C15.0402 7.31242 15.0567 7.62952 14.8721 7.83477L10.372 12.835L10.2939 12.9053C10.2093 12.9667 10.1063 13 9.99995 13C9.85833 12.9999 9.72264 12.9402 9.62788 12.835L5.12778 7.83477L5.0682 7.75273C4.95072 7.55225 4.98544 7.28926 5.16489 7.12771C5.34445 6.96617 5.60969 6.95939 5.79674 7.09744L5.87193 7.16482L9.99995 11.7519L14.128 7.16482Z"/></svg>`;

const FALLBACK_FAVICON = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiI+PGNpcmNsZSBjeD0iOCIgY3k9IjgiIHI9IjciIGZpbGw9IiNkZGQiLz48L3N2Zz4=';

const toolLabels: Record<string, string> = {
  'web_search': 'Searching the web',
  'web_fetch': 'Fetching page',
  'bash_tool': 'Running command',
  'create_file': 'Creating file',
  'str_replace': 'Editing file',
  'view': 'Reading file',
  'conversation_search': 'Searching past chats',
  'recent_chats': 'Getting recent chats'
};

// Message functions
function addMessage(role: string, content: string, raw = false, storedParentUuid: string | null = null, extraClasses = '', attachments: UploadedAttachment[] = []): HTMLElement {
  const el = document.createElement('div');
  el.className = 'message ' + role + (extraClasses ? ' ' + extraClasses : '');

  const c = document.createElement('div');
  c.className = 'message-content';
  c.innerHTML = role === 'user' ? escapeHtml(content) : (raw ? content : parseMarkdown(content));
  el.appendChild(c);

  if (role === 'user' && attachments.length > 0) {
    const attachmentsEl = document.createElement('div');
    attachmentsEl.className = 'message-attachments';
    attachmentsEl.innerHTML = attachments.map(a => {
      const icon = a.file_type?.startsWith('image/') ? imageIconSvg : fileIconSvg;
      return `
        <div class="message-attachment-row">
          <div class="message-attachment-icon">${icon}</div>
          <div class="message-attachment-info">
            <div class="message-attachment-name">${escapeHtml(a.file_name)}</div>
            ${a.file_size ? `<div class="message-attachment-size">${formatFileSize(a.file_size)}</div>` : ''}
          </div>
        </div>
      `;
    }).join('');
    el.appendChild(attachmentsEl);
  }

  if (role === 'user') {
    el.dataset.parentUuid = storedParentUuid || parentMessageUuid || conversationId || '';
    el.dataset.originalText = content;

    const editBtn = document.createElement('button');
    editBtn.className = 'edit-btn';
    editBtn.innerHTML = pencilSvg;
    editBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      startEditMessage(el);
    });
    el.appendChild(editBtn);
  }

  const messages = $('messages');
  if (messages) messages.appendChild(el);
  scrollToBottom();
  return el;
}

function addMessageRaw(role: string, htmlContent: string): HTMLElement {
  const el = document.createElement('div');
  el.className = 'message ' + role;

  const c = document.createElement('div');
  c.className = 'message-content';
  c.innerHTML = htmlContent;
  el.appendChild(c);

  c.querySelectorAll('.step-item').forEach(stepEl => {
    stepEl.addEventListener('click', () => stepEl.classList.toggle('expanded'));
  });

  const messages = $('messages');
  if (messages) messages.appendChild(el);
  scrollToBottom();
  return el;
}

// Edit message functions
function startEditMessage(msgEl: HTMLElement) {
  if (isLoading) return;
  msgEl.classList.add('editing');

  const contentEl = msgEl.querySelector('.message-content');
  if (!contentEl) return;

  const originalText = msgEl.dataset.originalText || contentEl.textContent || '';

  contentEl.innerHTML = `
    <div class="message-edit-container">
      <textarea class="message-edit-textarea">${escapeHtml(originalText)}</textarea>
      <div class="message-edit-actions">
        <button class="message-edit-cancel">${closeSvg}</button>
        <button class="message-edit-submit">${checkSvg}</button>
      </div>
    </div>
  `;

  const textarea = contentEl.querySelector('.message-edit-textarea') as HTMLTextAreaElement;
  const cancelBtn = contentEl.querySelector('.message-edit-cancel');
  const submitBtn = contentEl.querySelector('.message-edit-submit');

  textarea.focus();
  textarea.setSelectionRange(textarea.value.length, textarea.value.length);
  textarea.style.height = 'auto';
  textarea.style.height = textarea.scrollHeight + 'px';

  textarea.addEventListener('input', () => {
    textarea.style.height = 'auto';
    textarea.style.height = Math.min(textarea.scrollHeight, 200) + 'px';
  });

  textarea.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      submitEditMessage(msgEl, textarea.value);
    } else if (e.key === 'Escape') {
      cancelEditMessage(msgEl);
    }
  });

  cancelBtn?.addEventListener('click', () => cancelEditMessage(msgEl));
  submitBtn?.addEventListener('click', () => submitEditMessage(msgEl, textarea.value));
}

function cancelEditMessage(msgEl: HTMLElement) {
  msgEl.classList.remove('editing');
  const contentEl = msgEl.querySelector('.message-content');
  const originalText = msgEl.dataset.originalText || '';
  if (contentEl) contentEl.innerHTML = escapeHtml(originalText);
}

async function submitEditMessage(msgEl: HTMLElement, newText: string) {
  if (isLoading) return;
  const trimmedText = newText.trim();

  if (!trimmedText) {
    cancelEditMessage(msgEl);
    return;
  }

  const branchParentUuid = msgEl.dataset.parentUuid;

  // Remove all messages after this one
  let nextEl = msgEl.nextElementSibling;
  while (nextEl) {
    const toRemove = nextEl;
    nextEl = nextEl.nextElementSibling;
    toRemove.remove();
  }

  msgEl.classList.remove('editing');
  msgEl.dataset.originalText = trimmedText;

  const contentEl = msgEl.querySelector('.message-content');
  if (contentEl) contentEl.innerHTML = escapeHtml(trimmedText);

  parentMessageUuid = branchParentUuid || null;

  isLoading = true;
  const sendBtn = $('send-btn');
  if (sendBtn) (sendBtn as HTMLButtonElement).disabled = true;

  currentStreamingElement = addMessage('assistant', '<div class="loading-dots"><span></span><span></span><span></span></div>', true);

  try {
    await window.claude.sendMessage(conversationId!, trimmedText, parentMessageUuid!);
  } catch (e: any) {
    if (currentStreamingElement) {
      const content = currentStreamingElement.querySelector('.message-content');
      if (content) content.innerHTML = '<span style="color:#FF453A">Error: ' + e.message + '</span>';
    }
    currentStreamingElement = null;
    isLoading = false;
    if (sendBtn) (sendBtn as HTMLButtonElement).disabled = false;
  }
}

// Tool result rendering
function buildToolResultContent(toolName: string, result: any, isError: boolean): string {
  if (!result) return '';

  if (result.type === 'rich_link' && result.link) {
    const link = result.link;
    const title = link.title || link.url || 'Fetched page';
    const url = link.url || '';
    let icon = link.icon_url || '';
    if (!icon && url) {
      try {
        const domain = new URL(url).hostname;
        icon = `https://www.google.com/s2/favicons?sz=32&domain=${encodeURIComponent(domain)}`;
      } catch {}
    }
    if (!icon) icon = FALLBACK_FAVICON;
    return `
      <a class="link-card" href="${escapeHtml(url)}" target="_blank">
        <img class="link-card-icon" src="${escapeHtml(icon)}" onerror="this.onerror=null;this.src='${FALLBACK_FAVICON}'">
        <div class="link-card-info">
          <div class="link-card-title">${escapeHtml(title)}</div>
          <div class="link-card-url">${escapeHtml(url)}</div>
        </div>
      </a>
    `;
  }

  if (result.type === 'rich_content' && result.content) {
    let html = '<div class="chat-links">';
    for (const item of result.content.slice(0, 5)) {
      const title = item.title || 'Chat';
      const url = item.url || '';
      html += `
        <a class="chat-link-item" href="${escapeHtml(url)}" target="_blank">
          <span class="chat-link-icon">💬</span>
          <span class="chat-link-title">${escapeHtml(title)}</span>
        </a>
      `;
    }
    html += '</div>';
    return html;
  }

  if (result.type === 'json_block') {
    const code = result.code || '';
    const filename = result.filename || '';
    const stdout = result.stdout || '';
    const stderr = result.stderr || '';
    const returncode = result.returncode;

    if (stdout || stderr || returncode !== undefined) {
      const output = stdout || stderr || '';
      const hasError = isError || returncode !== 0;
      if (output) {
        return `<div class="tool-output ${hasError ? 'error' : ''}">${escapeHtml(output.substring(0, 500))}${output.length > 500 ? '...' : ''}</div>`;
      }
      return hasError ? '<div class="file-op error"><span class="file-op-icon">✗</span><span class="file-op-text">Command failed</span></div>' : '';
    }

    if (code && filename) {
      const shortFilename = filename.split('/').pop();
      const preview = code.substring(0, 200);
      return `
        <div class="file-preview">
          <div class="file-preview-header">${escapeHtml(shortFilename)}</div>
          <div class="tool-output">${escapeHtml(preview)}${code.length > 200 ? '...' : ''}</div>
        </div>
      `;
    }

    if (code) {
      return `<div class="tool-output">${escapeHtml(code.substring(0, 300))}${code.length > 300 ? '...' : ''}</div>`;
    }
  }

  if (result.type === 'text') {
    const text = result.text || '';
    if (text.toLowerCase().includes('success')) {
      return `<div class="file-op success"><span class="file-op-icon">✓</span><span class="file-op-text">${escapeHtml(text)}</span></div>`;
    }
    return `<div class="tool-output ${isError ? 'error' : ''}">${escapeHtml(text)}</div>`;
  }

  if (Array.isArray(result)) {
    let html = '<div class="search-results">';
    for (const item of result.slice(0, 5)) {
      const siteDomain = item.metadata?.site_domain || '';
      const siteName = item.metadata?.site_name || siteDomain || '';
      let favicon = item.metadata?.favicon_url || '';
      if (!favicon && siteDomain) {
        favicon = `https://www.google.com/s2/favicons?sz=32&domain=${encodeURIComponent(siteDomain)}`;
      }
      if (!favicon) favicon = FALLBACK_FAVICON;
      html += `
        <a class="search-result-item" href="${escapeHtml(item.url)}" target="_blank">
          <img class="search-result-favicon" src="${escapeHtml(favicon)}" onerror="this.onerror=null;this.src='${FALLBACK_FAVICON}'">
          <div class="search-result-info">
            <div class="search-result-title">${escapeHtml(item.title)}</div>
            <div class="search-result-site">${escapeHtml(siteName)}</div>
          </div>
        </a>
      `;
    }
    html += '</div>';
    return html;
  }

  if (result.link) {
    const link = result.link;
    const title = link.title || link.url || 'Fetched page';
    const url = link.url || '';
    let icon = link.icon_url || '';
    if (!icon && url) {
      try {
        const domain = new URL(url).hostname;
        icon = `https://www.google.com/s2/favicons?sz=32&domain=${encodeURIComponent(domain)}`;
      } catch {}
    }
    if (!icon) icon = FALLBACK_FAVICON;
    return `
      <a class="link-card" href="${escapeHtml(url)}" target="_blank">
        <img class="link-card-icon" src="${escapeHtml(icon)}" onerror="this.onerror=null;this.src='${FALLBACK_FAVICON}'">
        <div class="link-card-info">
          <div class="link-card-title">${escapeHtml(title)}</div>
          <div class="link-card-url">${escapeHtml(url)}</div>
        </div>
      </a>
    `;
  }

  if (result.rich_content) {
    let html = '<div class="chat-links">';
    const items = Array.isArray(result.rich_content) ? result.rich_content : [result.rich_content];
    for (const item of items.slice(0, 5)) {
      const title = item.title || item.text || 'Chat';
      const url = item.url || item.href || '';
      html += `
        <a class="chat-link-item" href="${escapeHtml(url)}" target="_blank">
          <span class="chat-link-icon">💬</span>
          <span class="chat-link-title">${escapeHtml(title)}</span>
        </a>
      `;
    }
    html += '</div>';
    return html;
  }

  if (result.text) {
    return `<div class="tool-output ${isError ? 'error' : ''}">${escapeHtml(result.text)}</div>`;
  }

  if (typeof result === 'string') {
    return `<div class="tool-output ${isError ? 'error' : ''}">${escapeHtml(result)}</div>`;
  }

  return '';
}

// Step building
function buildStepItem(step: Step, isActive: boolean): string {
  if (step.type === 'thinking') {
    const summary = step.thinkingSummary || step.summary;
    const label = summary ? escapeHtml(summary) : 'Thinking';
    const idx = step.index !== undefined ? step.index : '';
    return `
      <div class="step-item thinking" data-index="${idx}">
        <div class="step-timeline-col">
          <div class="step-dot-row">
            <div class="step-line-top"></div>
            <div class="step-dot"></div>
            <div class="step-line-bottom"></div>
          </div>
          <div class="step-line-extend"></div>
        </div>
        <div class="step-content-col">
          <div class="step-header">
            <span class="step-label">${label}</span>
            ${isActive ? '<div class="step-spinner"></div>' : `<span class="step-chevron">${chevronSvg}</span>`}
          </div>
          <div class="step-content">
            <div class="step-text">${escapeHtml(step.thinkingText || step.text || '')}</div>
          </div>
        </div>
      </div>
    `;
  } else if (step.type === 'tool') {
    const message = step.toolMessage || step.message;
    const label = message || toolLabels[step.toolName || ''] || `Using ${step.toolName}`;
    const resultHtml = buildToolResultContent(step.toolName || '', step.toolResult, step.isError || false);
    const idx = step.index !== undefined ? step.index : '';

    return `
      <div class="step-item tool ${step.toolResult ? '' : 'active'}" data-index="${idx}">
        <div class="step-timeline-col">
          <div class="step-dot-row">
            <div class="step-line-top"></div>
            <div class="step-dot"></div>
            <div class="step-line-bottom"></div>
          </div>
          <div class="step-line-extend"></div>
        </div>
        <div class="step-content-col">
          <div class="step-header">
            <span class="step-label">${escapeHtml(label)}</span>
            ${isActive && !step.toolResult ? '<div class="step-spinner"></div>' : `<span class="step-chevron">${chevronSvg}</span>`}
          </div>
          <div class="step-content">${resultHtml}</div>
        </div>
      </div>
    `;
  }
  return '';
}

function buildInterleavedContent(steps: Step[]): string {
  if (!steps || steps.length === 0) return '';

  let html = '';
  let currentTimelineSteps: Step[] = [];

  for (const step of steps) {
    if (step.type === 'text') {
      if (currentTimelineSteps.length > 0) {
        html += '<div class="steps-timeline">';
        for (const ts of currentTimelineSteps) {
          html += buildStepItem(ts, false);
        }
        html += '</div>';
        currentTimelineSteps = [];
      }
      html += parseMarkdown(step.text || '', step.citations);
    } else {
      currentTimelineSteps.push(step);
    }
  }

  if (currentTimelineSteps.length > 0) {
    html += '<div class="steps-timeline">';
    for (const ts of currentTimelineSteps) {
      html += buildStepItem(ts, false);
    }
    html += '</div>';
  }

  return html;
}

function buildStreamingContent(): string {
  const allBlocks: Step[] = [];

  streamingBlocks.thinkingBlocks.forEach((block, idx) => {
    allBlocks.push({
      type: 'thinking',
      index: idx,
      thinkingText: block.text,
      thinkingSummary: block.summary,
      isActive: block.isActive
    });
  });

  streamingBlocks.toolBlocks.forEach((block, idx) => {
    allBlocks.push({
      type: 'tool',
      index: idx,
      toolName: block.name,
      toolMessage: block.message,
      toolResult: block.result,
      isError: block.isError,
      isActive: block.isRunning
    });
  });

  streamingBlocks.textBlocks.forEach((block, idx) => {
    allBlocks.push({
      type: 'text',
      index: idx,
      text: block.text
    });
  });

  if (allBlocks.length === 0) return '';

  allBlocks.sort((a, b) => (a.index || 0) - (b.index || 0));

  let html = '';
  let currentTimelineSteps: Step[] = [];

  for (const step of allBlocks) {
    if (step.type === 'text') {
      if (currentTimelineSteps.length > 0) {
        html += '<div class="steps-timeline">';
        for (const ts of currentTimelineSteps) {
          html += buildStepItem(ts, ts.isActive || false);
        }
        html += '</div>';
        currentTimelineSteps = [];
      }
      html += parseMarkdown(step.text || '');
    } else {
      currentTimelineSteps.push(step);
    }
  }

  if (currentTimelineSteps.length > 0) {
    html += '<div class="steps-timeline">';
    for (const ts of currentTimelineSteps) {
      html += buildStepItem(ts, ts.isActive || false);
    }
    html += '</div>';
  }

  return html;
}

function updateStreamingContent() {
  if (!currentStreamingElement) return;
  const contentEl = currentStreamingElement.querySelector('.message-content');
  if (!contentEl) return;

  const expandedIndices = new Set<string>();
  contentEl.querySelectorAll('.step-item.expanded').forEach(el => {
    const idx = el.getAttribute('data-index');
    if (idx) expandedIndices.add(idx);
  });

  let html = buildStreamingContent();

  if (!html) {
    html = '<div class="loading-dots"><span></span><span></span><span></span></div>';
  }

  contentEl.innerHTML = html;

  // Add click listeners to step items
  contentEl.querySelectorAll('.step-item').forEach(el => {
    el.addEventListener('click', () => el.classList.toggle('expanded'));
  });

  expandedIndices.forEach(idx => {
    const el = contentEl.querySelector(`.step-item[data-index="${idx}"]`);
    if (el) el.classList.add('expanded');
  });
}

// Parse stored message content
function parseStoredMessageContent(content: ContentBlock[]): Step[] {
  const steps: Step[] = [];
  let currentToolUse: Step | null = null;

  for (const block of content) {
    if (block.type === 'thinking') {
      const lastSummary = block.summaries && block.summaries.length > 0
        ? block.summaries[block.summaries.length - 1].summary
        : undefined;
      steps.push({
        type: 'thinking',
        thinkingText: block.thinking,
        thinkingSummary: lastSummary
      });
    } else if (block.type === 'tool_use') {
      currentToolUse = {
        type: 'tool',
        toolName: block.name,
        toolMessage: block.message || block.display_content?.text,
        toolInput: block.input
      };
    } else if (block.type === 'tool_result') {
      if (currentToolUse && currentToolUse.toolName === block.name) {
        let resultData: any = null;
        if (block.display_content) {
          resultData = block.display_content;
        } else if (block.content && Array.isArray(block.content)) {
          if (block.name === 'web_search') {
            resultData = (block.content as any[]).filter(c => c.type === 'knowledge').map(c => ({
              title: c.title,
              url: c.url,
              metadata: c.metadata
            }));
          } else {
            const textContent = (block.content as any[]).find(c => c.type === 'text');
            if (textContent) {
              resultData = { type: 'text', text: textContent.text };
            }
          }
        }
        currentToolUse.toolResult = resultData;
        currentToolUse.isError = block.is_error;
        steps.push(currentToolUse);
        currentToolUse = null;
      }
    } else if (block.type === 'text') {
      steps.push({
        type: 'text',
        text: block.text,
        citations: block.citations
      });
    }
  }

  if (currentToolUse) {
    steps.push(currentToolUse);
  }

  return steps;
}

// Load conversation
async function loadConversation(convId: string) {
  try {
    clearAttachments();
    const conv = await window.claude.loadConversation(convId);
    conversationId = convId;
    currentConversationTitle = conv.name || 'Conversation';
    currentConversationMessages = [];

    isLoading = false;
    const sendBtn = $('send-btn');
    const stopBtn = $('stop-btn');
    if (sendBtn) sendBtn.classList.remove('hidden');
    if (stopBtn) stopBtn.classList.remove('visible');

    showChat();

    const messagesEl = $('messages');
    if (messagesEl) messagesEl.innerHTML = '';

    if (conv.chat_messages && conv.chat_messages.length > 0) {
      let prevMsgUuid = convId;

      for (const msg of conv.chat_messages) {
        const role = msg.sender === 'human' ? 'user' : 'assistant';

        if (role === 'user') {
          let text = '';
          if (msg.content && Array.isArray(msg.content)) {
            for (const block of msg.content) {
              if (block.type === 'text') {
                text += block.text || '';
              }
            }
          } else if (msg.text) {
            text = msg.text;
          }

          const messageFiles = msg.files_v2 || msg.files || [];
          const attachments: UploadedAttachment[] = messageFiles.map(f => ({
            id: f.file_uuid,
            document_id: f.file_uuid,
            file_name: f.file_name,
            file_size: 0, // Size not available in loaded messages
            file_type: f.file_kind === 'image' ? 'image/png' : 'application/octet-stream',
            previewUrl: f.preview_url || f.thumbnail_url
          }));

          if (text || attachments.length > 0) {
            addMessage('user', text, false, prevMsgUuid, '', attachments);
            currentConversationMessages.push({ role: 'human', content: text, timestamp: msg.created_at });
          }
        } else {
          let assistantText = '';
          if (msg.content && Array.isArray(msg.content)) {
            const steps = parseStoredMessageContent(msg.content);
            if (steps.length > 0) {
              const html = buildInterleavedContent(steps);
              addMessageRaw('assistant', html);
              // Extract text content for export
              for (const step of steps) {
                if (step.type === 'text') {
                  assistantText += step.text || '';
                }
              }
            }
          } else if (msg.text) {
            addMessage('assistant', msg.text);
            assistantText = msg.text;
          }
          if (assistantText) {
            currentConversationMessages.push({ role: 'assistant', content: assistantText, timestamp: msg.created_at });
          }
        }

        if (msg.uuid) {
          prevMsgUuid = msg.uuid;
          parentMessageUuid = msg.uuid;
        }
      }
    } else {
      if (messagesEl) {
        messagesEl.innerHTML = '<div class="empty-state" id="empty-state"><div class="empty-state-icon">✦</div><p>What can I help with?</p><span class="hint">Claude is ready</span></div>';
      }
      parentMessageUuid = convId;
    }

    closeSidebar();
    renderConversationsList();
    scrollToBottom();
  } catch (e) {
    console.error('Failed to load conversation:', e);
  }
}

// Export conversation to Markdown
async function exportConversation() {
  if (!conversationId || currentConversationMessages.length === 0) {
    console.error('No conversation to export');
    return;
  }

  try {
    const result = await window.claude.exportConversationMarkdown({
      title: currentConversationTitle,
      messages: currentConversationMessages
    });

    if (result.success) {
      console.log('Conversation exported to:', result.filePath);
    } else if (!result.canceled) {
      console.error('Failed to export conversation');
    }
  } catch (e) {
    console.error('Failed to export conversation:', e);
  }
}

// Auth functions
async function login() {
  const loginError = $('login-error');
  if (loginError) loginError.textContent = '';

  const r = await window.claude.login();
  if (r.success) {
    showChat();
    await startNewConversation();
    loadConversationsList();
  } else {
    if (loginError) loginError.textContent = r.error || 'Failed';
  }
}

async function logout() {
  await window.claude.logout();
  conversationId = null;
  parentMessageUuid = null;
  conversations = [];
  clearAttachments();

  const messagesEl = $('messages');
  if (messagesEl) {
    messagesEl.innerHTML = '<div class="empty-state" id="empty-state"><div class="empty-state-icon">✦</div><p>What can I help with?</p><span class="hint">Claude is ready</span></div>';
  }
  showLogin();
}

async function startNewConversation() {
  try {
    const r = await window.claude.createConversation();
    conversationId = r.conversationId;
    parentMessageUuid = r.parentMessageUuid || r.uuid || crypto.randomUUID();
  } catch (e: any) {
    addMessage('assistant', 'Failed: ' + e.message);
  }
}

function newChat() {
  conversationId = null;
  parentMessageUuid = null;
  clearAttachments();
  const homeInput = $('home-input') as HTMLTextAreaElement;
  if (homeInput) homeInput.value = '';
  closeSidebar();
  showHome();
}

// Send message functions
async function sendFromHome() {
  const input = $('home-input') as HTMLTextAreaElement;
  const msg = input?.value.trim();
  if (!msg || isLoading) return;
  if (uploadingAttachments) {
    attachmentError = 'Please wait for attachments to finish uploading';
    renderAttachmentList();
    return;
  }

  const attachmentPayloads = getAttachmentPayloads();
  const userAttachmentCopies = [...pendingAttachments];

  isLoading = true;
  const homeSendBtn = $('home-send-btn') as HTMLButtonElement;
  if (homeSendBtn) homeSendBtn.disabled = true;

  try {
    const r = await window.claude.createConversation(selectedModel);
    conversationId = r.conversationId;
    parentMessageUuid = r.parentMessageUuid || r.uuid || crypto.randomUUID();

    const homeContainer = $('home');
    const chatContainer = $('chat');

    if (homeContainer) homeContainer.classList.add('transitioning');

    await new Promise(resolve => setTimeout(resolve, 350));

    const messagesEl = $('messages');
    if (messagesEl) messagesEl.innerHTML = '';
    if (chatContainer) chatContainer.classList.add('entering');

    if (homeContainer) homeContainer.classList.remove('active');
    if (chatContainer) chatContainer.classList.add('active');

    const modelBadge = document.querySelector('.model-badge');
    if (modelBadge) modelBadge.textContent = modelDisplayNames[selectedModel] || 'Opus 4.5';

    const sidebarTab = $('sidebar-tab');
    if (sidebarTab) sidebarTab.classList.remove('hidden');

    addMessage('user', msg, false, null, 'fly-in', userAttachmentCopies);

    await new Promise(resolve => setTimeout(resolve, 200));

    currentStreamingElement = addMessage('assistant', '<div class="loading-dots"><span></span><span></span><span></span></div>', true, null, 'fade-in');

    const sendBtn = $('send-btn');
    const stopBtn = $('stop-btn');
    if (sendBtn) sendBtn.classList.add('hidden');
    if (stopBtn) stopBtn.classList.add('visible');

    setTimeout(() => {
      if (homeContainer) homeContainer.classList.remove('transitioning');
      if (chatContainer) chatContainer.classList.remove('entering');
    }, 600);

    await window.claude.sendMessage(conversationId, msg, parentMessageUuid!, attachmentPayloads);

    clearAttachments();

    window.claude.generateTitle(conversationId, msg).then(() => {
      loadConversationsList();
    }).catch(err => {
      console.warn('Failed to generate title:', err);
      loadConversationsList();
    });

    if (input) {
      input.value = '';
      input.style.height = 'auto';
    }
  } catch (e: any) {
    if (currentStreamingElement) {
      const content = currentStreamingElement.querySelector('.message-content');
      if (content) content.innerHTML = '<span style="color:#FF453A">Error: ' + e.message + '</span>';
    }
    currentStreamingElement = null;
    isLoading = false;
    if (homeSendBtn) homeSendBtn.disabled = false;

    const sendBtn = $('send-btn');
    const stopBtn = $('stop-btn');
    if (sendBtn) sendBtn.classList.remove('hidden');
    if (stopBtn) stopBtn.classList.remove('visible');
  }
}

async function sendMessage() {
  const input = $('input') as HTMLTextAreaElement;
  const msg = input?.value.trim();
  if (!msg || isLoading || !conversationId) return;
  if (uploadingAttachments) {
    attachmentError = 'Please wait for attachments to finish uploading';
    renderAttachmentList();
    return;
  }

  const attachmentPayloads = getAttachmentPayloads();
  const userAttachmentCopies = [...pendingAttachments];

  isLoading = true;
  if (input) {
    input.value = '';
    input.style.height = 'auto';
  }

  const sendBtn = $('send-btn');
  const stopBtn = $('stop-btn');
  if (sendBtn) sendBtn.classList.add('hidden');
  if (stopBtn) stopBtn.classList.add('visible');

  hideEmptyState();
  addMessage('user', msg, false, null, '', userAttachmentCopies);
  currentConversationMessages.push({ role: 'human', content: msg, timestamp: new Date().toISOString() });
  currentStreamingElement = addMessage('assistant', '<div class="loading-dots"><span></span><span></span><span></span></div>', true);

  try {
    await window.claude.sendMessage(conversationId, msg, parentMessageUuid!, attachmentPayloads);
    clearAttachments();
  } catch (e: any) {
    if (currentStreamingElement) {
      const content = currentStreamingElement.querySelector('.message-content');
      if (content) content.innerHTML = '<span style="color:#FF453A">Error: ' + e.message + '</span>';
    }
    currentStreamingElement = null;
    isLoading = false;
    if (sendBtn) sendBtn.classList.remove('hidden');
    if (stopBtn) stopBtn.classList.remove('visible');
  }
}

async function stopGenerating() {
  if (!conversationId || !isLoading) return;

  try {
    await window.claude.stopResponse(conversationId);
    const conv = await window.claude.loadConversation(conversationId);
    if (conv.chat_messages && conv.chat_messages.length > 0) {
      const lastMsg = conv.chat_messages[conv.chat_messages.length - 1];
      if (lastMsg.uuid) {
        parentMessageUuid = lastMsg.uuid;
      }
    }
  } catch (e) {
    console.error('Stop failed:', e);
  }

  if (currentStreamingElement) {
    const content = currentStreamingElement.querySelector('.message-content');
    const hasLoadingDots = content?.querySelector('.loading-dots');
    const hasContent = streamingBlocks.textContent.trim().length > 0;

    if (hasLoadingDots && !hasContent) {
      currentStreamingElement.remove();
    } else if (hasContent) {
      const finalHtml = buildInterleavedContent([]);
      if (content) content.innerHTML = finalHtml || '<span style="opacity:0.5;font-style:italic">Stopped</span>';
    }
  }

  isLoading = false;
  const sendBtn = $('send-btn');
  const stopBtn = $('stop-btn');
  if (sendBtn) sendBtn.classList.remove('hidden');
  if (stopBtn) stopBtn.classList.remove('visible');
  currentStreamingElement = null;
  resetStreamingBlocks();

  const inputEl = $('input');
  if (inputEl) inputEl.focus();
}

// Initialize
async function init() {
  if (await window.claude.getAuthStatus()) {
    showHome();
    loadConversationsList();
  } else {
    showLogin();
  }

  // Set up message listeners
  window.claude.onMessageThinking(d => {
    if (currentStreamingElement && d.conversationId === conversationId) {
      hideEmptyState();
      streamingBlocks.thinkingBlocks.set(d.blockIndex, {
        text: d.thinkingText || '',
        isActive: d.isThinking
      });
      updateStreamingContent();
    }
  });

  window.claude.onMessageThinkingStream(d => {
    if (currentStreamingElement && d.conversationId === conversationId) {
      const block = streamingBlocks.thinkingBlocks.get(d.blockIndex) || { isActive: true };
      block.text = d.thinking;
      if (d.summary) block.summary = d.summary;
      streamingBlocks.thinkingBlocks.set(d.blockIndex, block);
      updateStreamingContent();
    }
  });

  window.claude.onMessageToolUse(d => {
    if (currentStreamingElement && d.conversationId === conversationId) {
      hideEmptyState();
      streamingBlocks.toolBlocks.set(d.blockIndex, {
        name: d.toolName,
        message: d.message,
        input: d.input,
        isRunning: d.isRunning
      });
      updateStreamingContent();
      scrollToBottom();
    }
  });

  window.claude.onMessageToolResult(d => {
    if (currentStreamingElement && d.conversationId === conversationId) {
      streamingBlocks.toolBlocks.forEach((block) => {
        if (block.name === d.toolName && block.isRunning) {
          block.result = d.result;
          block.isError = d.isError;
          block.isRunning = false;
        }
      });
      updateStreamingContent();
      scrollToBottom();
    }
  });

  window.claude.onMessageStream(d => {
    if (currentStreamingElement && d.conversationId === conversationId) {
      hideEmptyState();
      streamingBlocks.textContent = d.fullText;
      if (d.blockIndex !== undefined) {
        streamingBlocks.textBlocks.set(d.blockIndex, { text: d.fullText });
      }
      updateStreamingContent();
      scrollToBottom();
    }
  });

  window.claude.onMessageComplete(d => {
    if (currentStreamingElement && d.conversationId === conversationId) {
      const finalHtml = buildInterleavedContent(d.steps);
      const content = currentStreamingElement.querySelector('.message-content');
      if (content) {
        content.innerHTML = finalHtml;
        // Add click listeners to step items
        content.querySelectorAll('.step-item').forEach(el => {
          el.addEventListener('click', () => el.classList.toggle('expanded'));
        });
      }
      parentMessageUuid = d.messageUuid;

      // Store assistant message for export
      if (d.fullText) {
        currentConversationMessages.push({ role: 'assistant', content: d.fullText, timestamp: new Date().toISOString() });
      }

      currentStreamingElement = null;
      resetStreamingBlocks();
      isLoading = false;

      const sendBtn = $('send-btn');
      const stopBtn = $('stop-btn');
      if (sendBtn) sendBtn.classList.remove('hidden');
      if (stopBtn) stopBtn.classList.remove('visible');

      const inputEl = $('input');
      if (inputEl) inputEl.focus();
    }
  });
}

// Set up event listeners
function setupEventListeners() {
  // Login button
  $('login-btn')?.addEventListener('click', login);

  // New chat button
  $('new-chat-btn')?.addEventListener('click', newChat);

  // Chat header menu
  const menuBtn = $('menu-btn');
  const menuDropdown = $('menu-dropdown');

  menuBtn?.addEventListener('click', (e) => {
    e.stopPropagation();
    menuDropdown?.classList.toggle('visible');
  });

  // Menu items
  $('menu-new-window')?.addEventListener('click', () => {
    menuDropdown?.classList.remove('visible');
    window.claude.newWindow();
  });

  $('menu-export')?.addEventListener('click', () => {
    menuDropdown?.classList.remove('visible');
    exportConversation();
  });

  $('menu-signout')?.addEventListener('click', () => {
    menuDropdown?.classList.remove('visible');
    logout();
  });

  // Home page menu
  const homeMenuBtn = $('home-menu-btn');
  const homeMenuDropdown = $('home-menu-dropdown');

  homeMenuBtn?.addEventListener('click', (e) => {
    e.stopPropagation();
    homeMenuDropdown?.classList.toggle('visible');
  });

  $('home-menu-new-window')?.addEventListener('click', () => {
    homeMenuDropdown?.classList.remove('visible');
    window.claude.newWindow();
  });

  $('home-menu-settings')?.addEventListener('click', () => {
    homeMenuDropdown?.classList.remove('visible');
    window.claude.openSettings();
  });

  $('home-menu-signout')?.addEventListener('click', () => {
    homeMenuDropdown?.classList.remove('visible');
    logout();
  });

  // Close all menus when clicking outside
  document.addEventListener('click', () => {
    menuDropdown?.classList.remove('visible');
    homeMenuDropdown?.classList.remove('visible');
  });

  // Sidebar toggle
  $('sidebar-tab')?.addEventListener('click', toggleSidebar);
  $('sidebar-overlay')?.addEventListener('click', closeSidebar);

  // Model selection
  $$('.model-option').forEach(btn => {
    btn.addEventListener('click', () => selectModel(btn as HTMLElement));
  });

  // Home input
  const homeInput = $('home-input') as HTMLTextAreaElement;
  homeInput?.addEventListener('input', () => autoResizeHome(homeInput));
  homeInput?.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendFromHome();
    }
  });

  // Home send button
  $('home-send-btn')?.addEventListener('click', sendFromHome);

  // Chat input
  const chatInput = $('input') as HTMLTextAreaElement;
  chatInput?.addEventListener('input', () => autoResize(chatInput));
  chatInput?.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  // Attachment buttons
  const fileInput = $('file-input') as HTMLInputElement;
  $('attach-btn')?.addEventListener('click', () => fileInput?.click());
  $('home-attach-btn')?.addEventListener('click', () => fileInput?.click());
  fileInput?.addEventListener('change', () => {
    handleFileSelection(fileInput.files);
    fileInput.value = '';
  });

  // Send button
  $('send-btn')?.addEventListener('click', sendMessage);

  // Stop button
  $('stop-btn')?.addEventListener('click', stopGenerating);

  // Keyboard shortcuts
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 's') {
      e.preventDefault();
      toggleSidebar();
    }
  });

  // Close dropdowns when clicking outside
  document.addEventListener('click', (e) => {
    if (openDropdownId && !(e.target as HTMLElement).closest('.conv-item')) {
      const dropdown = $(`conv-dropdown-${openDropdownId}`);
      if (dropdown) dropdown.classList.remove('open');
      openDropdownId = null;
    }
  });

  // Sidebar tab indicator
  const sidebarTab = $('sidebar-tab');
  const sidebarTabIndicator = $('sidebar-tab-indicator');
  sidebarTab?.addEventListener('mousemove', (e) => {
    if (!sidebarTabIndicator || !sidebarTab) return;
    const rect = sidebarTab.getBoundingClientRect();
    const relativeY = e.clientY - rect.top;
    sidebarTabIndicator.style.top = relativeY + 'px';
  });

  // Sidebar hover to open
  let hoverTimeout: number;
  sidebarTab?.addEventListener('mouseenter', () => {
    hoverTimeout = window.setTimeout(() => {
      toggleSidebar();
    }, 200);
  });
  sidebarTab?.addEventListener('mouseleave', () => {
    clearTimeout(hoverTimeout);
  });
}

// Start the app
init();
setupEventListeners();
renderAttachmentList();
```

## File: `src/renderer/markdown.ts`
```typescript
import { marked } from 'marked';
import hljs from 'highlight.js';

export interface Citation {
  url?: string;
  title?: string;
  start_index?: number;
  end_index?: number;
}

// Configure marked with syntax highlighting
marked.setOptions({
  breaks: true,
  gfm: true,
});

// Custom renderer for code blocks with syntax highlighting and copy button
const renderer = new marked.Renderer();
renderer.code = function ({ text, lang }: { text: string; lang?: string }) {
  const language = lang && hljs.getLanguage(lang) ? lang : 'plaintext';
  const highlighted = hljs.highlight(text, { language }).value;
  // Encode the raw text for the data attribute (escape HTML entities)
  const encodedText = text.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  return `<div class="code-block-wrapper">
    <button class="code-copy-btn" data-code="${encodedText}" title="Copy code">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
      </svg>
    </button>
    <pre><code class="hljs language-${language}">${highlighted}</code></pre>
  </div>`;
};

marked.use({ renderer });

export function parseMarkdown(t: string, citations?: Citation[]): string {
  if (!t) return '';

  let text = t;

  // Apply citations if present (before markdown parsing)
  if (citations && citations.length > 0) {
    // Sort citations by start_index descending to avoid index shifting
    const sortedCitations = [...citations].sort((a, b) => (b.start_index || 0) - (a.start_index || 0));
    for (const cit of sortedCitations) {
      if (cit.start_index !== undefined && cit.end_index !== undefined) {
        const before = text.slice(0, cit.start_index);
        const cited = text.slice(cit.start_index, cit.end_index);
        const after = text.slice(cit.end_index);
        const citNumber = citations.indexOf(cit) + 1;
        // Use HTML directly for citations since marked will preserve it
        const escapedUrl = (cit.url || '').replace(/"/g, '&quot;');
        const escapedTitle = (cit.title || '').replace(/"/g, '&quot;');
        text = before + `<a class="citation-link" href="${escapedUrl}" target="_blank" title="${escapedTitle}">${cited}</a><sup class="citation-num">[${citNumber}]</sup>` + after;
      }
    }
  }

  return marked.parse(text) as string;
}
```

## File: `src/renderer/settings.ts`
```typescript
// Settings renderer

const claude = (window as any).claude;

interface Settings {
  spotlightKeybind: string;
  spotlightPersistHistory: boolean;
  newWindowKeybind: string;
}

// DOM Elements
const keybindInput = document.getElementById('keybind-input') as HTMLElement;
const keybindDisplay = document.getElementById('keybind-display') as HTMLElement;
const newWindowKeybindInput = document.getElementById('new-window-keybind-input') as HTMLElement;
const newWindowKeybindDisplay = document.getElementById('new-window-keybind-display') as HTMLElement;
const persistHistoryCheckbox = document.getElementById('persist-history') as HTMLInputElement;

let currentSettings: Settings | null = null;

// Keybind recording state
interface KeybindRecorder {
  input: HTMLElement;
  display: HTMLElement;
  settingKey: 'spotlightKeybind' | 'newWindowKeybind';
  isRecording: boolean;
  pendingKeybind: string | null;
}

const keybindRecorders: KeybindRecorder[] = [
  { input: keybindInput, display: keybindDisplay, settingKey: 'spotlightKeybind', isRecording: false, pendingKeybind: null },
  { input: newWindowKeybindInput, display: newWindowKeybindDisplay, settingKey: 'newWindowKeybind', isRecording: false, pendingKeybind: null },
];

// Detect if we're on macOS
const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;

// Format keybind for display
function formatKeybind(keybind: string): string {
  return keybind
    .replace('CommandOrControl', isMac ? '\u2318' : 'Ctrl')
    .replace('Command', '\u2318')
    .replace('Control', 'Ctrl')
    .replace('Shift', '\u21E7')
    .replace('Alt', '\u2325')
    .replace('Option', '\u2325')
    .replace(/\+/g, ' + ');
}

// Build accelerator string from current modifier state
function buildAcceleratorFromModifiers(e: KeyboardEvent): string {
  const parts: string[] = [];

  if (e.metaKey || e.ctrlKey) {
    parts.push('CommandOrControl');
  }
  if (e.shiftKey) {
    parts.push('Shift');
  }
  if (e.altKey) {
    parts.push('Alt');
  }

  return parts.join('+');
}

// Convert key event to Electron accelerator format
function keyEventToAccelerator(e: KeyboardEvent): { accelerator: string; isComplete: boolean } {
  const parts: string[] = [];

  if (e.metaKey || e.ctrlKey) {
    parts.push('CommandOrControl');
  }
  if (e.shiftKey) {
    parts.push('Shift');
  }
  if (e.altKey) {
    parts.push('Alt');
  }

  // Get the key
  let key = e.key;

  // Check if this is a modifier-only press
  const isModifierOnly = ['Meta', 'Control', 'Shift', 'Alt'].includes(key);

  if (!isModifierOnly) {
    // Normalize key names
    if (key === ' ') key = 'Space';
    if (key.length === 1) key = key.toUpperCase();

    // Map special keys
    const keyMap: Record<string, string> = {
      'ArrowUp': 'Up',
      'ArrowDown': 'Down',
      'ArrowLeft': 'Left',
      'ArrowRight': 'Right',
      'Escape': 'Escape',
      'Enter': 'Return',
      'Backspace': 'Backspace',
      'Delete': 'Delete',
      'Tab': 'Tab',
    };

    if (keyMap[key]) {
      key = keyMap[key];
    }

    parts.push(key);
  }

  return {
    accelerator: parts.join('+'),
    isComplete: !isModifierOnly && parts.length >= 2 // Need at least one modifier + one key
  };
}

// Load settings
async function loadSettings() {
  currentSettings = await claude.getSettings();

  if (currentSettings) {
    keybindDisplay.textContent = formatKeybind(currentSettings.spotlightKeybind);
    newWindowKeybindDisplay.textContent = formatKeybind(currentSettings.newWindowKeybind);
    persistHistoryCheckbox.checked = currentSettings.spotlightPersistHistory;
  }
}

// Save keybind for a specific setting
async function saveKeybind(settingKey: 'spotlightKeybind' | 'newWindowKeybind', keybind: string) {
  if (!currentSettings) return;

  currentSettings = await claude.saveSettings({ [settingKey]: keybind });
}

// Save persist history
async function savePersistHistory(value: boolean) {
  if (!currentSettings) return;

  currentSettings = await claude.saveSettings({ spotlightPersistHistory: value });
}

// Stop recording and save if we have a valid keybind
function stopRecording(recorder: KeybindRecorder, save: boolean) {
  if (!recorder.isRecording) return;

  recorder.isRecording = false;
  recorder.input.classList.remove('recording');

  if (save && recorder.pendingKeybind) {
    saveKeybind(recorder.settingKey, recorder.pendingKeybind);
    recorder.display.textContent = formatKeybind(recorder.pendingKeybind);
  } else if (currentSettings) {
    recorder.display.textContent = formatKeybind(currentSettings[recorder.settingKey]);
  }

  recorder.pendingKeybind = null;
}

// Set up keybind recording for each recorder
keybindRecorders.forEach(recorder => {
  recorder.input.addEventListener('click', () => {
    if (!recorder.isRecording) {
      // Stop any other recorders
      keybindRecorders.forEach(r => {
        if (r !== recorder && r.isRecording) {
          stopRecording(r, false);
        }
      });

      recorder.isRecording = true;
      recorder.pendingKeybind = null;
      recorder.input.classList.add('recording');
      recorder.display.textContent = 'Press keys...';
      recorder.input.focus();
    }
  });

  recorder.input.addEventListener('keydown', (e) => {
    if (!recorder.isRecording) return;

    e.preventDefault();
    e.stopPropagation();

    // Handle Escape to cancel
    if (e.key === 'Escape') {
      stopRecording(recorder, false);
      return;
    }

    // Handle Enter to confirm
    if (e.key === 'Enter' && recorder.pendingKeybind) {
      stopRecording(recorder, true);
      return;
    }

    const result = keyEventToAccelerator(e);

    // Update display to show current keys being pressed
    if (result.accelerator) {
      recorder.display.textContent = formatKeybind(result.accelerator);

      // If we have a complete combo (modifier + key), store it as pending
      if (result.isComplete) {
        recorder.pendingKeybind = result.accelerator;
      }
    }
  });

  recorder.input.addEventListener('blur', () => {
    // Save pending keybind on blur (clicking away)
    stopRecording(recorder, !!recorder.pendingKeybind);
  });
});

// Persist history toggle
persistHistoryCheckbox.addEventListener('change', () => {
  savePersistHistory(persistHistoryCheckbox.checked);
});

// Load settings on page load
window.addEventListener('load', loadSettings);
```

## File: `src/renderer/spotlight.ts`
```typescript
import { parseMarkdown } from './markdown.js';

// Use any for window.claude - it's typed in preload but we don't need strict types here
const claude = (window as any).claude;

interface StepData {
  type: string;
  el: HTMLElement;
  name?: string;
}

interface Message {
  role: 'user' | 'assistant';
  text: string;
}

// DOM Elements
const input = document.getElementById('spotlight-input') as HTMLInputElement;
const sendBtn = document.getElementById('send-btn') as HTMLButtonElement;
const newChatBtn = document.getElementById('new-chat-btn') as HTMLButtonElement;
const inputRow = document.getElementById('input-row');
const messagesArea = document.getElementById('messages-area');
const container = document.getElementById('container');

// State
let isLoading = false;
let currentMessageEl: HTMLElement | null = null;
let currentStepsContainer: HTMLElement | null = null;
let currentResponseEl: HTMLElement | null = null;
let stepIndex = 0;
let steps: StepData[] = [];
let currentThinkingStep: HTMLElement | null = null;
let currentToolStep: HTMLElement | null = null;
let hasHistory = false;

// Constants
const chevronSvg = `<svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor"><path d="M14.128 7.16482C14.3126 6.95983 14.6298 6.94336 14.835 7.12771C15.0402 7.31242 15.0567 7.62952 14.8721 7.83477L10.372 12.835L10.2939 12.9053C10.2093 12.9667 10.1063 13 9.99995 13C9.85833 12.9999 9.72264 12.9402 9.62788 12.835L5.12778 7.83477L5.0682 7.75273C4.95072 7.55225 4.98544 7.28926 5.16489 7.12771C5.34445 6.96617 5.60969 6.95939 5.79674 7.09744L5.87193 7.16482L9.99995 11.7519L14.128 7.16482Z"/></svg>`;

const toolLabels: Record<string, string> = {
  'web_search': 'Searching the web',
  'web_fetch': 'Fetching page',
  'bash_tool': 'Running command',
  'create_file': 'Creating file',
  'str_replace': 'Editing file',
  'view': 'Reading file',
  'conversation_search': 'Searching past chats',
  'recent_chats': 'Getting recent chats'
};

// Utility functions
function escapeHtml(text: string): string {
  const div = document.createElement('div');
  div.textContent = text || '';
  return div.innerHTML;
}

function updateWindowSize() {
  if (!container) return;
  const containerHeight = container.offsetHeight;
  const newHeight = Math.max(56, Math.min(containerHeight + 2, 700));
  claude.spotlightResize(newHeight);
  if (messagesArea) messagesArea.scrollTop = messagesArea.scrollHeight;
}

function showNewChatButton(show: boolean) {
  if (newChatBtn) {
    newChatBtn.classList.toggle('visible', show);
  }
}

// Render existing messages from history
function renderHistoryMessages(messages: Message[]) {
  if (!messagesArea) return;

  for (const msg of messages) {
    const msgEl = document.createElement('div');

    if (msg.role === 'user') {
      msgEl.className = 'message';
      msgEl.innerHTML = `<div class="user-message">${escapeHtml(msg.text)}</div>`;
    } else if (msg.role === 'assistant') {
      msgEl.className = 'message ai-message';
      const responseEl = document.createElement('div');
      responseEl.className = 'ai-response';
      responseEl.innerHTML = parseMarkdown(msg.text);
      msgEl.appendChild(responseEl);
    }

    messagesArea.appendChild(msgEl);
  }

  // Show messages area and update layout
  inputRow?.classList.add('no-border');
  messagesArea.classList.add('visible');
  updateWindowSize();
}

// Load history and draft on startup
async function loadHistory() {
  try {
    const result = await claude.spotlightGetHistory();
    if (result.hasHistory && result.messages.length > 0) {
      hasHistory = true;
      renderHistoryMessages(result.messages);
      showNewChatButton(true);
    }
    // Restore draft input
    if (result.draftInput) {
      input.value = result.draftInput;
      sendBtn.classList.toggle('visible', result.draftInput.length > 0);
    }
  } catch (e) {
    console.error('Failed to load spotlight history:', e);
  }
}

// Start new chat
async function startNewChat() {
  await claude.spotlightNewChat();

  // Clear UI
  if (messagesArea) {
    messagesArea.innerHTML = '';
    messagesArea.classList.remove('visible');
  }
  inputRow?.classList.remove('no-border');

  // Clear input
  input.value = '';
  sendBtn.classList.remove('visible');

  hasHistory = false;
  showNewChatButton(false);
  updateWindowSize();

  input.focus();
}

// Step functions
function createStepItem(type: string, label: string, isActive = true): HTMLElement {
  const div = document.createElement('div');
  div.className = `step-item ${type}${isActive ? '' : ' done'}`;
  div.dataset.index = String(stepIndex++);
  div.innerHTML = `
    <div class="step-timeline-col">
      <div class="step-dot-row">
        <div class="step-line-top"></div>
        <div class="step-dot"></div>
        <div class="step-line-bottom"></div>
      </div>
      <div class="step-line-extend"></div>
    </div>
    <div class="step-content-col">
      <div class="step-header">
        <span class="step-label">${escapeHtml(label)}</span>
        ${isActive ? '<div class="step-spinner"></div>' : `<span class="step-chevron">${chevronSvg}</span>`}
      </div>
      <div class="step-content">
        <div class="step-text"></div>
      </div>
    </div>
  `;

  // Add click listener for expand/collapse
  const header = div.querySelector('.step-header');
  header?.addEventListener('click', () => div.classList.toggle('expanded'));

  return div;
}

function updateStepContent(stepEl: HTMLElement, text: string) {
  const textEl = stepEl.querySelector('.step-text');
  if (textEl) textEl.textContent = text;
}

function markStepComplete(stepEl: HTMLElement, label?: string) {
  stepEl.classList.add('done');
  stepEl.classList.remove('active');
  const spinner = stepEl.querySelector('.step-spinner');
  if (spinner) {
    spinner.outerHTML = `<span class="step-chevron">${chevronSvg}</span>`;
  }
  if (label) {
    const labelEl = stepEl.querySelector('.step-label');
    if (labelEl) labelEl.textContent = label;
  }
}

// Send message
async function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  isLoading = true;
  sendBtn.disabled = true;
  inputRow?.classList.add('no-border');
  messagesArea?.classList.add('visible');

  // Show new chat button since we now have history
  hasHistory = true;
  showNewChatButton(true);

  // Create user message
  const userMsgEl = document.createElement('div');
  userMsgEl.className = 'message';
  userMsgEl.innerHTML = `<div class="user-message">${escapeHtml(message)}</div>`;
  messagesArea?.appendChild(userMsgEl);

  // Create AI message container
  currentMessageEl = document.createElement('div');
  currentMessageEl.className = 'message ai-message';

  currentStepsContainer = document.createElement('div');
  currentStepsContainer.className = 'steps-container';

  currentResponseEl = document.createElement('div');
  currentResponseEl.className = 'ai-response';
  currentResponseEl.innerHTML = '<div class="loading-dots"><span></span><span></span><span></span></div>';

  currentMessageEl.appendChild(currentStepsContainer);
  currentMessageEl.appendChild(currentResponseEl);
  messagesArea?.appendChild(currentMessageEl);

  // Reset step tracking
  stepIndex = 0;
  steps = [];
  currentThinkingStep = null;
  currentToolStep = null;

  updateWindowSize();

  // Clear input
  input.value = '';
  sendBtn.classList.remove('visible');

  try {
    await claude.spotlightSend(message);
  } catch (err: any) {
    if (currentResponseEl) {
      currentResponseEl.textContent = 'Error: ' + (err.message || 'Failed to get response');
    }
    isLoading = false;
    sendBtn.disabled = false;
  }
}

// Set up stream listeners once at module level
claude.onSpotlightStream((data: any) => {
  if (currentResponseEl) {
    currentResponseEl.innerHTML = parseMarkdown(data.fullText);
    updateWindowSize();
  }
});

claude.onSpotlightComplete((data: any) => {
  if (currentResponseEl) {
    currentResponseEl.innerHTML = parseMarkdown(data.fullText);
  }
  isLoading = false;
  sendBtn.disabled = false;
  updateWindowSize();
});

// Thinking listeners
claude.onSpotlightThinking((data: any) => {
  if (data.isThinking) {
    currentThinkingStep = createStepItem('thinking', 'Thinking...', true);
    currentStepsContainer?.appendChild(currentThinkingStep);
    steps.push({ type: 'thinking', el: currentThinkingStep });
    updateWindowSize();
  } else if (currentThinkingStep) {
    const summary = data.thinkingText ? data.thinkingText.substring(0, 50) + '...' : 'Thought';
    markStepComplete(currentThinkingStep, summary);
    if (data.thinkingText) {
      updateStepContent(currentThinkingStep, data.thinkingText);
    }
    currentThinkingStep = null;
    updateWindowSize();
  }
});

claude.onSpotlightThinkingStream((data: any) => {
  if (currentThinkingStep) {
    updateStepContent(currentThinkingStep, data.thinking);
    updateWindowSize();
  }
});

// Tool listeners
claude.onSpotlightTool((data: any) => {
  if (data.isRunning) {
    const label = data.message || toolLabels[data.toolName] || `Using ${data.toolName}`;
    currentToolStep = createStepItem('tool', label, true);
    currentStepsContainer?.appendChild(currentToolStep);
    steps.push({ type: 'tool', el: currentToolStep, name: data.toolName });
    updateWindowSize();
  }
});

claude.onSpotlightToolResult((data: any) => {
  if (currentToolStep) {
    const label = toolLabels[data.toolName] || `Used ${data.toolName}`;
    markStepComplete(currentToolStep, label);
    if (data.result) {
      const resultText = typeof data.result === 'string' ? data.result : JSON.stringify(data.result, null, 2);
      updateStepContent(currentToolStep, resultText.substring(0, 500));
    }
    if (data.isError) {
      currentToolStep.classList.add('error');
    }
    currentToolStep = null;
    updateWindowSize();
  }
});

// Event listeners
input.addEventListener('input', () => {
  const hasText = input.value.trim().length > 0;
  sendBtn.classList.toggle('visible', hasText);
  sendBtn.disabled = !hasText || isLoading;
});

input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey && input.value.trim() && !isLoading) {
    e.preventDefault();
    sendMessage();
  }
  if (e.key === 'Escape') {
    window.close();
  }
});

sendBtn.addEventListener('click', () => {
  if (input.value.trim() && !isLoading) {
    sendMessage();
  }
});

newChatBtn.addEventListener('click', () => {
  startNewChat();
});

// Handle code copy button clicks 
document.addEventListener('click', async (e) => {
  const target = e.target as HTMLElement;
  const copyBtn = target.closest('.code-copy-btn') as HTMLButtonElement;
  if (!copyBtn) return;

  const code = copyBtn.dataset.code;
  if (!code) return;

  const textarea = document.createElement('textarea');
  textarea.innerHTML = code;
  const decodedCode = textarea.value;

  try {
    await navigator.clipboard.writeText(decodedCode);
    copyBtn.classList.add('copied');

    const originalSvg = copyBtn.innerHTML;
    copyBtn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="20 6 9 17 4 12"></polyline>
    </svg>`;

    setTimeout(() => {
      copyBtn.classList.remove('copied');
      copyBtn.innerHTML = originalSvg;
    }, 1500);
  } catch (err) {
    console.error('Failed to copy code:', err);
  }
});


// Focus input on load and load history
window.addEventListener('load', () => {
  input.focus();
  loadHistory();
});

// Clean up on close
window.addEventListener('beforeunload', () => {
  // Save draft input before closing
  claude.spotlightSaveDraft(input.value);
  claude.removeSpotlightListeners();
  claude.spotlightReset();
});
```

## File: `src/renderer/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "outDir": "../../static/js",
    "rootDir": ".",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleResolution": "bundler",
    "declaration": false
  },
  "include": ["./**/*"]
}
```

## File: `src/streaming/parser.ts`
```typescript
import type { ContentBlock, Citation, Step } from '../types';

// Event callbacks for stream processing
export interface StreamCallbacks {
  onMessageStart?: (uuid: string) => void;
  onTextDelta?: (text: string, fullText: string, blockIndex: number) => void;
  onThinkingStart?: (blockIndex: number) => void;
  onThinkingDelta?: (thinking: string, blockIndex: number) => void;
  onThinkingStop?: (thinkingText: string, summaries: Array<{ summary: string } | string>, blockIndex: number) => void;
  onToolStart?: (toolName: string, message: string, blockIndex: number) => void;
  onToolStop?: (toolName: string, input: string, blockIndex: number) => void;
  onToolResult?: (toolName: string, result: unknown, isError: boolean, blockIndex: number) => void;
  onCitation?: (citation: Citation, blockIndex: number) => void;
  onToolApproval?: (toolName: string, approvalKey: string, input: unknown) => void;
  onCompaction?: (status: string, message?: string) => void;
  onComplete?: (fullText: string, steps: Step[], messageUuid: string) => void;
}

// Stream parser state
export interface StreamState {
  fullResponse: string;
  lastMessageUuid: string;
  contentBlocks: Map<number, ContentBlock>;
  pendingCitations: Map<string, Citation>;
}

// Create initial state for a new stream
export function createStreamState(): StreamState {
  return {
    fullResponse: '',
    lastMessageUuid: '',
    contentBlocks: new Map(),
    pendingCitations: new Map()
  };
}

// Parse display_content from tool_result
function parseDisplayContent(displayContent: unknown): unknown {
  if (!displayContent) return null;

  const dc = displayContent as Record<string, unknown>;

  if (dc.type === 'rich_link' && dc.link) {
    return { type: 'rich_link', link: dc.link };
  } else if (dc.type === 'rich_content' && dc.content) {
    return { type: 'rich_content', content: dc.content };
  } else if (dc.type === 'json_block' && dc.json_block) {
    try {
      const parsed = JSON.parse(dc.json_block as string);
      return { type: 'json_block', ...parsed };
    } catch {
      return { type: 'json_block', code: dc.json_block };
    }
  } else if (dc.type === 'text') {
    return { type: 'text', text: dc.text };
  } else if (dc.json_block) {
    try {
      return { type: 'json_block', ...JSON.parse(dc.json_block as string) };
    } catch {
      return { type: 'json_block', code: dc.json_block };
    }
  } else if (dc.rich_content) {
    return { type: 'rich_content', content: dc.rich_content };
  } else if (dc.link) {
    return { type: 'rich_link', link: dc.link };
  } else if (dc.text) {
    return { type: 'text', text: dc.text };
  } else if (Array.isArray(displayContent)) {
    return displayContent;
  }

  return null;
}

// Build steps array from content blocks for timeline display
export function buildSteps(contentBlocks: Map<number, ContentBlock>): Step[] {
  const steps: Step[] = [];
  let pendingToolUse: Step | null = null;

  const sortedBlocks = Array.from(contentBlocks.entries())
    .sort((a, b) => a[0] - b[0]);

  for (const [idx, block] of sortedBlocks) {
    if (block.type === 'thinking' && (block.thinking || block.thinkingText || block.summaries?.length)) {
      const firstSummary = block.summaries?.[0];
      const summaryText = typeof firstSummary === 'object' ? firstSummary?.summary : firstSummary;
      steps.push({
        type: 'thinking',
        index: idx,
        thinkingText: block.thinking || block.thinkingText,
        thinkingSummary: summaryText || block.thinkingSummary,
        summaries: block.summaries,
        cut_off: block.cut_off,
        start_timestamp: block.start_timestamp,
        stop_timestamp: block.stop_timestamp
      });
    } else if (block.type === 'tool_use' && (block.name || block.toolName)) {
      pendingToolUse = {
        type: 'tool',
        index: idx,
        toolName: block.name || block.toolName,
        toolInput: block.buffered_input || block.partial_json || block.toolInput,
        toolMessage: block.toolMessage
      };
    } else if (block.type === 'tool_result' && pendingToolUse) {
      pendingToolUse.toolResult = block.toolResult || block.content;
      pendingToolUse.isError = block.is_error || block.isError;
      steps.push(pendingToolUse);
      pendingToolUse = null;
    } else if (block.type === 'text' && block.text) {
      steps.push({
        type: 'text',
        index: idx,
        text: block.text,
        citations: block.citations,
        flags: block.flags
      });
    }
  }

  if (pendingToolUse) {
    steps.push(pendingToolUse);
  }

  return steps;
}

// Process a single SSE chunk
export function processSSEChunk(
  chunk: string,
  state: StreamState,
  callbacks: StreamCallbacks
): void {
  const lines = chunk.split('\n');

  for (const line of lines) {
    if (!line.startsWith('data: ')) continue;

    try {
      const data = JSON.parse(line.slice(6));
      processSSEEvent(data, state, callbacks);
    } catch {
      // Not valid JSON, skip
    }
  }
}

// Process a single SSE event
function processSSEEvent(
  data: Record<string, unknown>,
  state: StreamState,
  callbacks: StreamCallbacks
): void {
  const { contentBlocks, pendingCitations } = state;

  // message_start
  if (data.type === 'message_start') {
    const message = data.message as { uuid?: string } | undefined;
    if (message?.uuid) {
      state.lastMessageUuid = message.uuid;
      callbacks.onMessageStart?.(message.uuid);
    }
  }

  // content_block_start
  if (data.type === 'content_block_start') {
    const blockIndex = data.index as number;
    const contentBlock = data.content_block as Record<string, unknown> | undefined;
    const blockType = (contentBlock?.type as string) || 'text';

    const block: ContentBlock = {
      type: blockType as ContentBlock['type'],
      index: blockIndex
    };

    if (blockType === 'thinking') {
      block.thinking = '';
      block.summaries = [];
      block.start_timestamp = new Date().toISOString();
      block.thinkingText = '';
      callbacks.onThinkingStart?.(blockIndex);
    } else if (blockType === 'tool_use') {
      block.name = (contentBlock?.name as string) || 'unknown';
      block.partial_json = '';
      block.approval_key = contentBlock?.approval_key as string | undefined;
      block.toolName = block.name;
      block.toolInput = '';
      block.toolMessage = (contentBlock?.message as string) || '';
      callbacks.onToolStart?.(block.name, block.toolMessage, blockIndex);
    } else if (blockType === 'tool_result') {
      block.tool_use_id = contentBlock?.tool_use_id as string | undefined;
      block.is_error = (contentBlock?.is_error as boolean) || false;
      block.content = null;
      block.toolName = (contentBlock?.name as string) || '';
      block.isError = block.is_error;
      block.toolResult = parseDisplayContent(contentBlock?.display_content);

      if (block.toolResult) {
        callbacks.onToolResult?.(block.toolName || '', block.toolResult, block.is_error || false, blockIndex);
      }
    } else if (blockType === 'text') {
      block.text = '';
      block.citations = [];
      block.flags = [];
    }

    contentBlocks.set(blockIndex, block);
  }

  // content_block_stop
  if (data.type === 'content_block_stop') {
    const blockIndex = data.index as number;
    const block = contentBlocks.get(blockIndex);

    if (block?.type === 'thinking') {
      block.stop_timestamp = (data.stop_timestamp as string) || new Date().toISOString();
      callbacks.onThinkingStop?.(
        block.thinking || block.thinkingText || '',
        block.summaries || [],
        blockIndex
      );
    } else if (block?.type === 'tool_use') {
      block.buffered_input = (data.buffered_input as string) || block.partial_json || '{}';
      callbacks.onToolStop?.(
        block.name || block.toolName || '',
        block.buffered_input || block.toolInput || '',
        blockIndex
      );
    }
  }

  // content_block_delta
  if (data.type === 'content_block_delta') {
    const blockIndex = data.index as number;
    const block = contentBlocks.get(blockIndex);
    const delta = data.delta as Record<string, unknown> | undefined;
    const deltaType = delta?.type as string;

    if (!block) return;

    // flag_delta
    if (deltaType === 'flag_delta' && delta?.flag) {
      block.flags = block.flags || [];
      const flag = delta.flag as string;
      if (!block.flags.includes(flag)) {
        block.flags.push(flag);
      }
    }

    // Text block deltas
    if (block.type === 'text') {
      if (deltaType === 'text_delta' && delta?.text) {
        const text = delta.text as string;
        block.text = (block.text || '') + text;
        state.fullResponse += text;
        callbacks.onTextDelta?.(text, state.fullResponse, blockIndex);
      } else if (deltaType === 'citation_start_delta' && delta?.citation) {
        const citation = delta.citation as Record<string, unknown>;
        pendingCitations.set(citation.uuid as string, {
          uuid: citation.uuid as string,
          start_index: (block.text || '').length,
          url: citation.url as string | undefined,
          title: citation.title as string | undefined,
          source_type: citation.source_type as string | undefined
        });
      } else if (deltaType === 'citation_end_delta' && delta?.citation_uuid) {
        const citationUuid = delta.citation_uuid as string;
        const pendingCitation = pendingCitations.get(citationUuid);
        if (pendingCitation) {
          pendingCitation.end_index = (block.text || '').length;
          block.citations = block.citations || [];
          block.citations.push(pendingCitation);
          pendingCitations.delete(citationUuid);
          callbacks.onCitation?.(pendingCitation, blockIndex);
        }
      }
    }

    // Thinking block deltas
    if (block.type === 'thinking') {
      if (deltaType === 'thinking_delta' && delta?.thinking) {
        const thinking = delta.thinking as string;
        block.thinking = (block.thinking || '') + thinking;
        block.thinkingText = block.thinking;
        callbacks.onThinkingDelta?.(block.thinking, blockIndex);
      } else if (deltaType === 'thinking_summary_delta' && delta?.summary) {
        block.summaries = block.summaries || [];
        block.summaries.push(delta.summary as { summary: string } | string);
        const summary = delta.summary as { summary?: string } | string;
        block.thinkingSummary = typeof summary === 'object' ? summary.summary : summary;
      } else if (deltaType === 'thinking_cut_off_delta') {
        block.cut_off = (delta?.cut_off as boolean) ?? true;
      }
    }

    // Tool use block deltas
    if (block.type === 'tool_use') {
      if (deltaType === 'input_json_delta' && delta?.partial_json) {
        block.partial_json = (block.partial_json || '') + (delta.partial_json as string);
        block.toolInput = block.partial_json;
      }
    }

    // Tool result block deltas
    if (block.type === 'tool_result') {
      if (deltaType === 'input_json_delta' && delta?.partial_json) {
        const rawJson = (block.partial_json || '') + (delta.partial_json as string);
        block.partial_json = rawJson;
        try {
          const parsed = JSON.parse(rawJson);
          if (Array.isArray(parsed) && parsed.length > 0 && parsed.every((d: unknown) => typeof d === 'object' && d !== null && 'type' in d)) {
            block.content = parsed;
          } else {
            block.content = [{ type: 'text', text: rawJson }];
          }
          if (Array.isArray(parsed)) {
            block.toolResult = parsed;
          } else if (parsed.rich_content) {
            block.toolResult = { rich_content: parsed.rich_content };
          } else if (parsed.link) {
            block.toolResult = { link: parsed.link };
          } else {
            block.toolResult = { json_block: parsed };
          }
          callbacks.onToolResult?.(block.toolName || '', block.toolResult, block.is_error || false, blockIndex);
        } catch {
          block.content = [{ type: 'text', text: rawJson }];
        }
      }
    }
  }

  // tool_use_block_update_delta
  if (data.type === 'tool_use_block_update_delta') {
    const blockIndex = data.index as number;
    const block = contentBlocks.get(blockIndex);
    if (block && data.message) {
      block.toolMessage = data.message as string;
      callbacks.onToolStart?.(block.name || block.toolName || '', block.toolMessage, blockIndex);
    }
  }

  // thinking_summary_delta at event level
  if (data.type === 'thinking_summary_delta') {
    const blockIndex = data.index as number;
    const block = contentBlocks.get(blockIndex);
    if (block && data.summary) {
      block.summaries = block.summaries || [];
      block.summaries.push(data.summary as { summary: string } | string);
    }
  }

  // tool_approval
  if (data.type === 'tool_approval') {
    callbacks.onToolApproval?.(
      data.tool_name as string,
      data.approval_key as string,
      data.input
    );
  }

  // compaction_status
  if (data.type === 'compaction_status') {
    callbacks.onCompaction?.(data.status as string, data.message as string | undefined);
  }

  // message_delta with stop_reason - message complete
  const messageDelta = data.delta as { stop_reason?: string } | undefined;
  if (data.type === 'message_delta' && messageDelta?.stop_reason) {
    const steps = buildSteps(contentBlocks);
    pendingCitations.clear();
    callbacks.onComplete?.(state.fullResponse, steps, state.lastMessageUuid);
  }
}
```

## File: `src/types/index.ts`
```typescript
// Settings schema
export interface SettingsSchema {
  spotlightKeybind: string;
  spotlightPersistHistory: boolean;
  newWindowKeybind: string;
}

// Store schema for electron-store
export interface StoreSchema {
  orgId?: string;
  deviceId?: string;
  anonymousId?: string;
  settings: SettingsSchema;
}

// File attachment payloads
export interface AttachmentPayload {
  document_id: string;
  file_name: string;
  file_size: number;
  file_type: string;
  file_url?: string;
  extracted_content?: string;
}

export interface UploadFilePayload {
  name: string;
  size: number;
  type: string;
  data: ArrayBuffer | Buffer | Uint8Array | number[];
}

// Citation tracking (matches Claude's citation_start_delta/citation_end_delta)
export interface Citation {
  uuid: string;
  start_index: number;
  end_index?: number;
  url?: string;
  title?: string;
  source_type?: string;
}

// Content block state tracking - matches Claude's block types exactly
export interface ContentBlock {
  type: 'text' | 'thinking' | 'tool_use' | 'tool_result';
  index: number;
  // Text blocks
  text?: string;
  citations?: Citation[];
  flags?: string[];
  // Thinking blocks
  thinking?: string;
  summaries?: Array<{ summary: string } | string>;
  cut_off?: boolean;
  start_timestamp?: string;
  stop_timestamp?: string;
  // Tool use blocks
  name?: string;
  partial_json?: string;
  buffered_input?: string;
  approval_key?: string;
  // Tool result blocks
  tool_use_id?: string;
  is_error?: boolean;
  content?: unknown;
  // Legacy compatibility
  toolName?: string;
  toolInput?: string;
  toolMessage?: string;
  toolResult?: unknown;
  isError?: boolean;
  thinkingText?: string;
  thinkingSummary?: string;
}

// Step type for message-complete event timeline
export interface Step {
  type: 'thinking' | 'tool' | 'text';
  index: number;
  // Thinking
  thinkingText?: string;
  thinkingSummary?: string;
  summaries?: Array<{ summary: string } | string>;
  cut_off?: boolean;
  start_timestamp?: string;
  stop_timestamp?: string;
  // Tool
  toolName?: string;
  toolInput?: string;
  toolMessage?: string;
  toolResult?: unknown;
  isError?: boolean;
  // Text
  text?: string;
  citations?: Citation[];
  flags?: string[];
}

// Web search result from tool_result display_content
export interface WebSearchResult {
  type: string;
  title: string;
  url: string;
  metadata?: {
    site_domain?: string;
    favicon_url?: string;
    site_name?: string;
  };
}

// API response types
export interface ApiResponse<T = unknown> {
  status: number;
  data: T;
  stream?: NodeJS.ReadableStream;
}

export interface ConversationData {
  uuid: string;
  name?: string;
  model?: string;
  created_at?: string;
  updated_at?: string;
}

export interface CreateConversationResponse extends ConversationData {
  conversationId: string;
  parentMessageUuid: string;
}
```

## File: `static/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src * data:;">
  <title>Open Claude</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    html, body {
      height: 100%;
      background: transparent;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', system-ui, sans-serif;
      color: #000;
      height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
    }

    @media (prefers-color-scheme: dark) {
      body { color: #fff; }
    }

    /* Login */
    .login-container {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      padding: 40px;
    }

    .login-card {
      background: rgba(255, 255, 255, 0.6);
      backdrop-filter: blur(80px) saturate(200%);
      -webkit-backdrop-filter: blur(80px) saturate(200%);
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-radius: 20px;
      padding: 44px 52px;
      text-align: center;
      max-width: 320px;
      width: 100%;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    }

    .logo {
      width: 180px;
      height: 96px;
      margin: 0 auto 24px;
    }
    .logo img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }

    .login-container h1 {
      font-size: 22px;
      font-weight: 600;
      letter-spacing: -0.4px;
      margin-bottom: 6px;
    }

    .login-container .subtitle {
      color: rgba(0, 0, 0, 0.5);
      font-size: 14px;
      margin-bottom: 28px;
    }

    .login-btn {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      color: white;
      border: none;
      padding: 12px 24px;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      width: 100%;
      transition: all 0.2s;
      box-shadow: 0 2px 8px rgba(204, 120, 92, 0.3);
    }

    .login-btn:hover {
      transform: translateY(-1px);
      box-shadow: 0 4px 16px rgba(204, 120, 92, 0.4);
    }
    .login-btn:active { transform: scale(0.98); }

    .error { color: #FF453A; font-size: 11px; margin-top: 12px; }

    /* Home page */
    .home-container {
      display: none;
      flex-direction: column;
      height: 100vh;
      position: relative;
    }
    .home-container.active { display: flex; }

    .home-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px 20px;
    }

    /* Draggable header area for home page */
    .home-drag-region {
      position: absolute;
      top: 0;
      left: 30px; /* Leave space for sidebar tab */
      right: 0;
      height: 50px;
      -webkit-app-region: drag;
    }

    .home-logo {
      display: none;
    }

    .home-input-area {
      width: 100%;
      max-width: 600px;
      -webkit-app-region: no-drag;
      text-align: center;
    }

    .home-input-wrapper {
      background: transparent;
      padding: 0;
    }

    .home-input {
      width: 100%;
      background: transparent;
      border: none;
      border-bottom: 1px solid rgba(0, 0, 0, 0.15);
      font-size: 18px;
      font-family: inherit;
      color: #000;
      outline: none;
      resize: none;
      min-height: 28px;
      max-height: 200px;
      line-height: 1.5;
      padding: 8px 0;
      caret-color: #CC785C;
    }

    .home-input::placeholder {
      color: rgba(0, 0, 0, 0.3);
    }

    .home-input:focus {
      border-bottom-color: #CC785C;
    }

    .home-input-footer {
      display: flex;
      justify-content: center;
      align-items: center;
      gap: 8px;
      margin-top: 20px;
    }

    .home-send-btn {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      color: white;
      border: none;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 6px rgba(204, 120, 92, 0.25);
      transition: all 0.15s;
    }

    .home-send-btn:hover { transform: scale(1.03); }
    .home-send-btn:active { transform: scale(0.97); }

    .home-attach-btn {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      border: none;
      background: transparent;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: rgba(0, 0, 0, 0.4);
      transition: all 0.15s;
    }

    .home-attach-btn:hover {
      background: rgba(0, 0, 0, 0.06);
      color: rgba(0, 0, 0, 0.7);
    }

    .home-attach-btn:active {
      transform: scale(0.95);
    }

    .model-selector {
      display: flex;
      gap: 6px;
    }

    .model-option {
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 500;
      background: transparent;
      border: 1px solid rgba(0, 0, 0, 0.1);
      color: rgba(0, 0, 0, 0.5);
      cursor: pointer;
      transition: all 0.15s;
    }

    .model-option:hover {
      background: rgba(0, 0, 0, 0.04);
      color: rgba(0, 0, 0, 0.7);
    }

    .model-option.active {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      border-color: transparent;
      color: white;
    }


    .home-footer {
      position: absolute;
      bottom: 0;
      right: 0;
      padding: 16px;
      display: flex;
      justify-content: flex-end;
      -webkit-app-region: no-drag;
    }

    .home-header {
      position: absolute;
      top: 12px;
      right: 16px;
      z-index: 100;
      -webkit-app-region: no-drag;
    }

    .home-signout {
      font-size: 12px;
      color: rgba(0, 0, 0, 0.4);
      background: none;
      border: none;
      cursor: pointer;
      padding: 6px 12px;
      border-radius: 6px;
      transition: all 0.15s;
    }

    .home-signout:hover {
      background: rgba(0, 0, 0, 0.05);
      color: rgba(0, 0, 0, 0.6);
    }

    /* Home to Chat transition animation */
    .home-container.transitioning {
      pointer-events: none;
    }

    .home-container.transitioning .home-content {
      animation: homeContentFadeOut 0.4s ease-out forwards;
    }

    .home-container.transitioning .home-input-area {
      animation: inputAreaMoveDown 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }

    .home-container.transitioning .home-input-footer {
      animation: footerFadeOut 0.25s ease-out forwards;
    }

    @keyframes homeContentFadeOut {
      0% { opacity: 1; }
      100% { opacity: 0; }
    }

    @keyframes inputAreaMoveDown {
      0% {
        transform: translateY(0);
        opacity: 1;
      }
      60% {
        transform: translateY(calc(50vh - 100px));
        opacity: 1;
      }
      100% {
        transform: translateY(calc(50vh - 80px));
        opacity: 0;
      }
    }

    @keyframes footerFadeOut {
      0% { opacity: 1; }
      100% { opacity: 0; }
    }

    /* Chat container entrance animation */
    .chat-container.entering {
      display: flex;
      opacity: 0;
      animation: chatEnter 0.1s ease-out 0.3s forwards;
    }

    @keyframes chatEnter {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    /* First user message fly-in animation */
    .message.fly-in {
      animation: messageFlyIn 0.4s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }

    @keyframes messageFlyIn {
      0% {
        opacity: 0;
        transform: translateY(100px) scale(0.95);
      }
      100% {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }

    /* Assistant message fade-in */
    .message.fade-in {
      animation: messageFadeIn 0.3s ease-out forwards;
    }

    @keyframes messageFadeIn {
      0% {
        opacity: 0;
        transform: translateY(10px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* Chat container */
    .chat-container { display: none; flex-direction: column; height: 100vh; position: relative; }
    .chat-container.active { display: flex; }

    /* Header */
    .header {
      padding: 0 16px;
      height: 44px;
      background: transparent;
      display: flex;
      justify-content: space-between;
      align-items: center;
      -webkit-app-region: drag;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-left: 70px;
    }

    .icon-btn {
      width: 28px;
      height: 28px;
      background: transparent;
      border: none;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      -webkit-app-region: no-drag;
      transition: all 0.15s;
      font-size: 15px;
      color: rgba(0, 0, 0, 0.45);
    }

    .icon-btn:hover {
      background: rgba(0, 0, 0, 0.06);
      color: rgba(0, 0, 0, 0.7);
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 8px;
      -webkit-app-region: no-drag;
    }

    .model-badge {
      font-size: 11px;
      color: rgba(0, 0, 0, 0.4);
      padding: 0;
      font-weight: 500;
    }

    .sign-out-btn {
      background: transparent;
      border: none;
      color: rgba(0, 0, 0, 0.4);
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s;
    }

    .sign-out-btn:hover {
      background: rgba(0, 0, 0, 0.06);
      color: rgba(0, 0, 0, 0.7);
    }

    /* Hamburger menu */
    .menu-container {
      position: relative;
    }

    .menu-btn {
      width: 28px;
      height: 28px;
      background: transparent;
      border: none;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: rgba(0, 0, 0, 0.5);
      transition: all 0.15s;
    }

    .menu-btn:hover {
      background: rgba(0, 0, 0, 0.06);
      color: rgba(0, 0, 0, 0.7);
    }

    .menu-dropdown {
      position: absolute;
      top: calc(100% + 6px);
      right: 0;
      min-width: 160px;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-radius: 10px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15), 0 0 0 1px rgba(0, 0, 0, 0.08);
      padding: 6px;
      opacity: 0;
      visibility: hidden;
      transform: translateY(-8px);
      transition: all 0.15s ease;
      z-index: 1000;
    }

    .menu-dropdown.visible {
      opacity: 1;
      visibility: visible;
      transform: translateY(0);
    }

    .menu-item {
      display: flex;
      align-items: center;
      gap: 10px;
      width: 100%;
      padding: 8px 12px;
      background: transparent;
      border: none;
      border-radius: 6px;
      font-size: 13px;
      color: rgba(0, 0, 0, 0.8);
      cursor: pointer;
      transition: background 0.1s;
      text-align: left;
    }

    .menu-item:hover {
      background: rgba(0, 0, 0, 0.06);
    }

    .menu-item svg {
      width: 16px;
      height: 16px;
      color: rgba(0, 0, 0, 0.5);
      flex-shrink: 0;
    }

    .menu-divider {
      height: 1px;
      background: rgba(0, 0, 0, 0.08);
      margin: 6px 0;
    }

    .menu-item.danger {
      color: #e45649;
    }

    .menu-item.danger svg {
      color: #e45649;
    }

    /* Sidebar overlay */
    .sidebar-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.3);
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.25s, visibility 0.25s;
      z-index: 100;
    }

    .sidebar-overlay.open {
      opacity: 1;
      visibility: visible;
    }

    /* Sidebar */
    .sidebar {
      position: fixed;
      top: 0;
      left: 0;
      width: 260px;
      height: 100%;
      background: rgba(246, 246, 246, 0.97);
      backdrop-filter: blur(40px);
      -webkit-backdrop-filter: blur(40px);
      border-right: 1px solid rgba(0, 0, 0, 0.1);
      transform: translateX(-100%);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 101;
      display: flex;
      flex-direction: column;
    }

    .sidebar.open {
      transform: translateX(0);
    }

    /* Sidebar trigger tab - invisible hover zone spanning 70% of height */
    .sidebar-tab {
      position: fixed;
      left: 0;
      top: 15%;
      width: 6px;
      height: 70%;
      background: transparent;
      cursor: pointer;
      z-index: 99;
      -webkit-app-region: no-drag;
    }

    .sidebar-tab:hover {
      width: 24px;
    }

    /* The visual indicator that follows the mouse */
    .sidebar-tab-indicator {
      position: absolute;
      left: 0;
      width: 6px;
      height: 60px;
      background: rgba(0, 0, 0, 0.08);
      border-radius: 0 4px 4px 0;
      transform: translateY(-50%);
      transition: width 0.2s, background 0.2s;
      display: flex;
      align-items: center;
      justify-content: center;
      pointer-events: none;
      opacity: 0;
    }

    .sidebar-tab:hover .sidebar-tab-indicator {
      width: 24px;
      background: rgba(0, 0, 0, 0.12);
      opacity: 1;
    }

    .sidebar-tab-indicator::after {
      content: '';
      width: 2px;
      height: 20px;
      background: rgba(0, 0, 0, 0.25);
      border-radius: 1px;
      opacity: 0;
      transition: opacity 0.2s;
    }

    .sidebar-tab:hover .sidebar-tab-indicator::after {
      opacity: 1;
    }

    .sidebar-tab.hidden {
      opacity: 0;
      pointer-events: none;
    }

    .sidebar-header {
      padding: 12px 16px;
      padding-top: 48px;
      border-bottom: 1px solid rgba(0, 0, 0, 0.06);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .sidebar-title {
      font-size: 13px;
      font-weight: 600;
      color: rgba(0, 0, 0, 0.7);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .sidebar-spacer {
      flex: 1;
    }

    .settings-btn {
      width: 28px;
      height: 28px;
      background: transparent;
      border: none;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: rgba(0, 0, 0, 0.4);
      transition: all 0.15s;
      margin-right: 8px;
    }

    .settings-btn:hover {
      background: rgba(0, 0, 0, 0.08);
      color: rgba(0, 0, 0, 0.6);
    }

    .new-chat-btn {
      width: 24px;
      height: 24px;
      background: #CC785C;
      border: none;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 16px;
      font-weight: 300;
      color: white;
      transition: all 0.15s;
      box-shadow: 0 2px 6px rgba(204, 120, 92, 0.3);
    }

    .new-chat-btn:hover {
      background: #B86A50;
      transform: scale(1.05);
      box-shadow: 0 3px 8px rgba(204, 120, 92, 0.4);
    }

    .sidebar-content {
      flex: 1;
      overflow-y: auto;
      padding: 8px;
    }

    .sidebar-content::-webkit-scrollbar { display: none; }
    .sidebar-content { -ms-overflow-style: none; scrollbar-width: none; }

    .conv-item {
      padding: 10px 12px;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.15s;
      margin-bottom: 2px;
    }

    .conv-item:hover {
      background: rgba(0, 0, 0, 0.05);
    }

    .conv-item.active {
      background: rgba(204, 120, 92, 0.15);
    }

    .conv-item-title {
      font-size: 13px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .conv-item-date {
      font-size: 11px;
      color: rgba(0, 0, 0, 0.4);
      margin-top: 2px;
    }

    .conv-loading {
      text-align: center;
      padding: 20px;
      color: rgba(0, 0, 0, 0.4);
      font-size: 13px;
    }

    .conv-section-header {
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: rgba(0, 0, 0, 0.4);
      padding: 12px 12px 6px;
      margin-top: 4px;
    }

    .conv-section-header:first-child {
      margin-top: 0;
    }

    /* Conversation item with menu */
    .conv-item {
      position: relative;
    }

    .conv-item-row {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .conv-item-info {
      flex: 1;
      min-width: 0;
    }

    .conv-star {
      color: #CC785C;
      font-size: 10px;
      margin-right: 4px;
    }

    .conv-menu-btn {
      width: 24px;
      height: 24px;
      background: transparent;
      border: none;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      opacity: 0;
      transition: all 0.15s;
      color: rgba(0, 0, 0, 0.4);
      font-size: 14px;
      flex-shrink: 0;
    }

    .conv-item:hover .conv-menu-btn {
      opacity: 1;
    }

    .conv-menu-btn:hover {
      background: rgba(0, 0, 0, 0.08);
      color: rgba(0, 0, 0, 0.7);
    }

    /* Dropdown menu */
    .conv-dropdown {
      position: absolute;
      right: 8px;
      top: 100%;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
      z-index: 200;
      min-width: 120px;
      overflow: hidden;
      display: none;
    }

    .conv-dropdown.open {
      display: block;
    }

    .conv-dropdown-item {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      font-size: 12px;
      color: rgba(0, 0, 0, 0.7);
      cursor: pointer;
      transition: background 0.1s;
    }

    .conv-dropdown-item:hover {
      background: rgba(0, 0, 0, 0.05);
    }

    .conv-dropdown-item.delete {
      color: #FF453A;
    }

    .conv-dropdown-item.delete:hover {
      background: rgba(255, 69, 58, 0.1);
    }

    .conv-dropdown-icon {
      font-size: 12px;
      width: 16px;
      text-align: center;
    }

    /* Rename input */
    .conv-rename-input {
      width: 100%;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(204, 120, 92, 0.5);
      border-radius: 4px;
      padding: 4px 8px;
      font-size: 13px;
      font-family: inherit;
      color: rgba(0, 0, 0, 0.8);
      outline: none;
    }

    .conv-rename-input:focus {
      border-color: #CC785C;
    }

    /* Messages */
    .messages {
      flex: 1;
      overflow-y: auto;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .messages::-webkit-scrollbar { width: 6px; }
    .messages::-webkit-scrollbar-track { background: transparent; }
    .messages::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.1); border-radius: 3px; }

    .message { max-width: 78%; }
    .message:not(.fly-in):not(.fade-in) { animation: msgIn 0.2s ease forwards; }
    @keyframes msgIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    .message.user { align-self: flex-end; }
    .message.assistant { align-self: flex-start; }

    .message-content {
      padding: 12px 16px;
      border-radius: 18px;
      line-height: 1.5;
      font-size: 14px;
    }

    .message.user .message-content {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      color: white;
      border-bottom-right-radius: 6px;
    }

    .message.assistant .message-content {
      background: rgba(255, 255, 255, 0.7);
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-bottom-left-radius: 6px;
      color: #000;
    }

    /* Message edit feature */
    .message.user {
      position: relative;
    }
    .message.user .edit-btn {
      position: absolute;
      bottom: 4px;
      left: -28px;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(0, 0, 0, 0.1);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.15s, transform 0.15s;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    .message.user .edit-btn svg {
      width: 12px;
      height: 12px;
      color: #666;
    }
    .message.user:hover .edit-btn {
      opacity: 1;
    }
    .message.user .edit-btn:hover {
      transform: scale(1.1);
      background: #fff;
    }
    .message.user.editing .edit-btn {
      display: none;
    }
    .message.user.editing .message-content {
      background: transparent;
      padding: 0;
    }
    .message-edit-container {
      display: flex;
      flex-direction: column;
      gap: 8px;
      min-width: 200px;
    }
    .message-edit-textarea {
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(204, 120, 92, 0.5);
      border-radius: 14px;
      padding: 10px 14px;
      font-size: 14px;
      font-family: inherit;
      color: #000;
      resize: none;
      min-height: 40px;
      max-height: 200px;
      line-height: 1.5;
    }
    .message-edit-textarea:focus {
      outline: none;
      border-color: #CC785C;
      box-shadow: 0 0 0 3px rgba(204, 120, 92, 0.15);
    }
    .message-edit-actions {
      display: flex;
      gap: 6px;
      justify-content: flex-end;
    }
    .message-edit-actions button {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.15s;
    }
    .message-edit-actions button:hover {
      transform: scale(1.1);
    }
    .message-edit-cancel {
      background: rgba(0, 0, 0, 0.08);
    }
    .message-edit-cancel svg {
      width: 14px;
      height: 14px;
      color: #666;
    }
    .message-edit-submit {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      box-shadow: 0 2px 6px rgba(204, 120, 92, 0.3);
    }
    .message-edit-submit svg {
      width: 14px;
      height: 14px;
      color: white;
    }

    .message-content p { margin: 0 0 6px 0; }
    .message-content p:last-child { margin-bottom: 0; }
    .message-content p:first-child { margin-top: 0; }
    .message-content h1, .message-content h2, .message-content h3 { margin: 10px 0 4px; font-weight: 600; }
    .message-content h1:first-child, .message-content h2:first-child, .message-content h3:first-child { margin-top: 0; }
    .message-content h1 { font-size: 1.2em; }
    .message-content h2 { font-size: 1.1em; }
    .message-content h3 { font-size: 1.05em; }
    .message-content strong { font-weight: 600; }
    .message-content code {
      font-family: 'SF Mono', Menlo, monospace;
      font-size: 0.9em;
      background: rgba(0, 0, 0, 0.08);
      padding: 2px 6px;
      border-radius: 4px;
      color: #9a5d3a;
    }
    .message.user .message-content code { background: rgba(255, 255, 255, 0.2); color: #fff; }
    .message-content pre {
      background: rgba(0, 0, 0, 0.05);
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-radius: 10px;
      padding: 12px;
      overflow-x: auto;
      margin: 8px 0;
    }
    .message-content pre code { background: transparent; padding: 0; font-size: 12px; line-height: 1.5; color: #333; }
    .message-content ul, .message-content ol { margin: 6px 0; padding-left: 20px; }
    .message-content li { margin: 2px 0; }
    .message-content blockquote {
      border-left: 3px solid #CC785C;
      margin: 8px 0;
      padding: 6px 12px;
      background: rgba(204, 120, 92, 0.1);
      border-radius: 0 8px 8px 0;
    }
    .message-content a { color: #9a5d3a; text-decoration: none; }
    .message-content a:hover { text-decoration: underline; }
    .message-content hr {
      border: none;
      border-top: 1px solid rgba(0, 0, 0, 0.12);
      margin: 12px 0;
    }

    /* Citation styling */
    .citation-link {
      color: #CC785C;
      text-decoration: underline;
      text-decoration-style: dotted;
      text-underline-offset: 2px;
    }
    .citation-link:hover {
      text-decoration-style: solid;
    }
    .citation-num {
      font-size: 10px;
      color: #CC785C;
      font-weight: 600;
      vertical-align: super;
      margin-left: 1px;
      cursor: pointer;
    }
    .citation-num:hover {
      text-decoration: underline;
    }

    /* Input area */
    .input-area {
      padding: 16px 20px 20px;
      background: rgba(255, 255, 255, 0.4);
      backdrop-filter: blur(40px) saturate(180%);
      -webkit-backdrop-filter: blur(40px) saturate(180%);
      border-top: 1px solid rgba(0, 0, 0, 0.1);
    }

    .input-wrapper {
      display: flex;
      gap: 8px;
      align-items: flex-end;
      background: rgba(255, 255, 255, 0.7);
      border: 1px solid rgba(0, 0, 0, 0.15);
      border-radius: 22px;
      padding: 6px 6px 6px 6px;
      transition: all 0.2s;
    }

    .attach-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: none;
      background: transparent;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: rgba(0, 0, 0, 0.4);
      transition: all 0.15s;
      flex-shrink: 0;
    }

    .attach-btn:hover { background: rgba(0, 0, 0, 0.06); color: rgba(0, 0, 0, 0.7); }
    .attach-btn:active { transform: scale(0.95); }

    .attachment-container {
      display: flex;
      flex-direction: column;
      gap: 6px;
      padding: 0 4px;
      min-height: 0;
      max-height: 0;
      overflow: hidden;
      transition: min-height 0.15s ease, max-height 0.15s ease, margin-top 0.15s ease;
    }

    .attachment-container.visible {
      min-height: 44px;
      max-height: 200px;
      margin-top: 8px;
      overflow: visible;
    }

    .attachment-list {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .attachment-pill {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 10px 6px 6px;
      border-radius: 10px;
      background: rgba(0, 0, 0, 0.03);
      border: 1px solid rgba(0, 0, 0, 0.07);
      max-width: 220px;
    }

    .attachment-icon {
      width: 28px;
      height: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(0, 0, 0, 0.04);
      border-radius: 6px;
      flex-shrink: 0;
    }

    .attachment-meta { display: flex; flex-direction: column; gap: 1px; min-width: 0; flex: 1; }
    .attachment-name {
      font-size: 12px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .attachment-size { font-size: 10px; color: rgba(0, 0, 0, 0.45); }

    .attachment-remove {
      background: transparent;
      border: none;
      cursor: pointer;
      color: rgba(0, 0, 0, 0.4);
      font-size: 12px;
      padding: 4px;
      border-radius: 6px;
    }
    .attachment-remove:hover { background: rgba(0, 0, 0, 0.06); color: rgba(0, 0, 0, 0.7); }

    .attachment-status {
      font-size: 12px;
      color: rgba(0, 0, 0, 0.55);
      padding-left: 2px;
    }
    .attachment-status.error { color: #FF453A; }

    .input-wrapper:focus-within {
      border-color: rgba(204, 120, 92, 0.5);
      background: rgba(255, 255, 255, 0.85);
      box-shadow: 0 0 0 3px rgba(204, 120, 92, 0.15);
    }

    .input-area textarea {
      flex: 1;
      background: transparent;
      border: none;
      padding: 8px 0;
      color: #000;
      font-size: 14px;
      resize: none;
      font-family: inherit;
      min-height: 20px;
      max-height: 120px;
      line-height: 1.4;
    }

    .input-area textarea::placeholder { color: rgba(0, 0, 0, 0.4); }
    .input-area textarea:focus { outline: none; }

    .message-attachments {
      margin-top: 8px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .message-attachment-row {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 10px;
      background: rgba(0, 0, 0, 0.03);
      border-radius: 12px;
      border: 1px solid rgba(0, 0, 0, 0.05);
    }

    .message-attachment-icon {
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(0, 0, 0, 0.04);
      border-radius: 6px;
      flex-shrink: 0;
    }
    .attachment-icon-svg {
      width: 16px;
      height: 16px;
      color: rgba(0, 0, 0, 0.5);
    }
    .message-attachment-info { display: flex; flex-direction: column; gap: 1px; min-width: 0; }
    .message-attachment-name {
      font-size: 13px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .message-attachment-size { font-size: 11px; color: rgba(0, 0, 0, 0.45); }

    .send-btn {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      color: white;
      border: none;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 15px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s;
      flex-shrink: 0;
      box-shadow: 0 2px 6px rgba(204, 120, 92, 0.3);
    }

    .send-btn:hover:not(:disabled) { transform: scale(1.05); }
    .send-btn:active:not(:disabled) { transform: scale(0.95); }
    .send-btn:disabled { opacity: 0.4; cursor: not-allowed; }

    .stop-btn {
      display: none;
      background: rgba(120, 120, 128, 0.16);
      color: rgba(0, 0, 0, 0.6);
      border: 1px solid rgba(0, 0, 0, 0.08);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 10px;
      font-weight: 500;
      transition: all 0.15s;
      align-self: flex-end;
      flex-shrink: 0;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }
    .stop-btn:hover { background: rgba(120, 120, 128, 0.24); color: rgba(0, 0, 0, 0.8); }
    .stop-btn:active { transform: scale(0.95); }
    .stop-btn.visible { display: flex; align-items: center; justify-content: center; }
    .send-btn.hidden { display: none; }

    .loading-dots { display: flex; gap: 4px; padding: 4px 0; }
    .loading-dots span {
      width: 6px;
      height: 6px;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 50%;
      animation: pulse 1.2s ease-in-out infinite;
    }
    .loading-dots span:nth-child(1) { animation-delay: 0s; }
    .loading-dots span:nth-child(2) { animation-delay: 0.15s; }
    .loading-dots span:nth-child(3) { animation-delay: 0.3s; }
    @keyframes pulse { 0%, 80%, 100% { opacity: 0.35; } 40% { opacity: 1; } }

    .streaming-cursor {
      display: inline-block;
      width: 2px;
      height: 14px;
      background: #CC785C;
      margin-left: 2px;
      vertical-align: middle;
      animation: blink 1s step-end infinite;
    }
    @keyframes blink { 0%, 50% { opacity: 1; } 51%, 100% { opacity: 0; } }

    /* Thinking block */
    .thinking-block {
      background: rgba(204, 120, 92, 0.08);
      border: 1px solid rgba(204, 120, 92, 0.2);
      border-radius: 10px;
      margin-bottom: 10px;
      overflow: hidden;
    }

    .thinking-header {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      cursor: pointer;
      font-size: 12px;
      color: rgba(0, 0, 0, 0.5);
      font-weight: 500;
      transition: background 0.15s;
    }

    .thinking-header:hover {
      background: rgba(204, 120, 92, 0.05);
    }

    .thinking-icon {
      font-size: 14px;
      transition: transform 0.2s;
    }

    .thinking-block.expanded .thinking-icon {
      transform: rotate(90deg);
    }

    .thinking-label {
      flex: 1;
    }

    .thinking-spinner {
      width: 12px;
      height: 12px;
      border: 2px solid rgba(204, 120, 92, 0.3);
      border-top-color: #CC785C;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }

    @keyframes spin {
      to { transform: rotate(360deg); }
    }

    .thinking-content {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s ease;
    }

    .thinking-block.expanded .thinking-content {
      max-height: 300px;
      overflow-y: auto;
    }

    .thinking-text {
      padding: 0 12px 10px;
      font-size: 12px;
      line-height: 1.5;
      color: rgba(0, 0, 0, 0.5);
      white-space: pre-wrap;
      font-family: 'SF Mono', Menlo, monospace;
    }

    /* Steps Timeline - Card wrapper for thinking/tool blocks */
    .steps-timeline {
      margin-top: 10px;
      margin-bottom: 12px;
      background: rgba(0, 0, 0, 0.03);
      border: 1px solid rgba(0, 0, 0, 0.06);
      border-radius: 12px;
      padding: 8px 12px 8px 8px;
    }

    .step-item {
      display: flex;
      flex-direction: row;
      min-height: 34px;
    }

    /* Timeline column with line and dot */
    .step-timeline-col {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-left: 4px;
      width: 24px;
      flex-shrink: 0;
    }

    .step-dot-row {
      display: flex;
      flex-direction: column;
      align-items: center;
      height: 34px;
      justify-content: center;
    }

    .step-line-top {
      width: 1px;
      flex: 1;
      background: rgba(0, 0, 0, 0.12);
      min-height: 8px;
    }

    .step-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.12);
      flex-shrink: 0;
      margin: 4px 0;
    }

    .step-item.thinking .step-dot {
      background: #CC785C;
    }

    .step-item.tool .step-dot {
      background: #5856D6;
    }

    .step-line-bottom {
      width: 1px;
      flex: 1;
      background: rgba(0, 0, 0, 0.12);
      min-height: 8px;
    }

    .step-item:first-child .step-line-top {
      background: transparent;
    }

    .step-item:last-child .step-line-bottom {
      background: transparent;
    }

    .step-line-extend {
      width: 1px;
      flex: 1;
      background: rgba(0, 0, 0, 0.12);
      display: none;
    }

    .step-item.expanded .step-line-extend {
      display: block;
    }

    .step-item:last-child .step-line-extend {
      background: transparent;
    }

    /* Content column */
    .step-content-col {
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
    }

    .step-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      padding: 6px 10px 6px 4px;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.15s;
    }

    .step-header:hover {
      background: rgba(0, 0, 0, 0.04);
    }

    .step-label {
      font-size: 13px;
      font-weight: 400;
      color: rgba(0, 0, 0, 0.55);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      flex: 1;
      line-height: 1.4;
    }

    .step-item.thinking .step-label {
      color: rgba(0, 0, 0, 0.55);
    }

    .step-item.tool .step-label {
      color: rgba(0, 0, 0, 0.55);
    }

    .step-meta {
      font-size: 11px;
      color: rgba(0, 0, 0, 0.35);
      flex-shrink: 0;
      padding-left: 8px;
    }

    .step-spinner {
      width: 12px;
      height: 12px;
      border: 1.5px solid rgba(0, 0, 0, 0.12);
      border-top-color: rgba(0, 0, 0, 0.5);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
      flex-shrink: 0;
    }

    .step-chevron {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 16px;
      height: 16px;
      color: rgba(0, 0, 0, 0.35);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      flex-shrink: 0;
    }

    .step-chevron svg {
      width: 16px;
      height: 16px;
    }

    .step-item.expanded .step-chevron {
      transform: rotate(90deg);
    }

    .step-content {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s ease, opacity 0.2s;
      opacity: 0;
    }

    .step-item.expanded .step-content {
      max-height: 300px;
      overflow-y: auto;
      opacity: 1;
    }

    .step-text {
      padding: 8px 10px 12px 4px;
      font-size: 12px;
      line-height: 1.6;
      color: rgba(0, 0, 0, 0.5);
      white-space: pre-wrap;
      font-family: 'SF Mono', Menlo, monospace;
    }

    /* Web search results */
    .search-results {
      margin-top: 8px;
    }

    .search-result-item {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 8px;
      background: rgba(255, 255, 255, 0.5);
      border-radius: 6px;
      margin-bottom: 4px;
      text-decoration: none;
      transition: background 0.15s;
    }

    .search-result-item:hover {
      background: rgba(255, 255, 255, 0.8);
    }

    .search-result-favicon {
      width: 16px;
      height: 16px;
      border-radius: 3px;
      flex-shrink: 0;
      background: rgba(0, 0, 0, 0.05);
    }

    .search-result-info {
      flex: 1;
      min-width: 0;
    }

    .search-result-title {
      font-size: 11px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .search-result-site {
      font-size: 10px;
      color: rgba(0, 0, 0, 0.4);
    }

    /* Link card for web_fetch */
    .link-card {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 12px;
      background: rgba(255, 255, 255, 0.5);
      border: 1px solid rgba(0, 0, 0, 0.08);
      border-radius: 8px;
      margin-top: 8px;
      text-decoration: none;
      transition: background 0.15s, border-color 0.15s;
    }

    .link-card:hover {
      background: rgba(255, 255, 255, 0.8);
      border-color: rgba(0, 0, 0, 0.12);
    }

    .link-card-icon {
      width: 20px;
      height: 20px;
      border-radius: 4px;
      flex-shrink: 0;
      background: rgba(0, 0, 0, 0.05);
    }

    .link-card-info {
      flex: 1;
      min-width: 0;
    }

    .link-card-title {
      font-size: 12px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .link-card-url {
      font-size: 10px;
      color: rgba(0, 0, 0, 0.4);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* Chat link items for conversation_search/recent_chats */
    .chat-links {
      margin-top: 8px;
    }

    .chat-link-item {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 10px;
      background: rgba(255, 255, 255, 0.5);
      border-radius: 6px;
      margin-bottom: 4px;
      text-decoration: none;
      transition: background 0.15s;
    }

    .chat-link-item:hover {
      background: rgba(255, 255, 255, 0.8);
    }

    .chat-link-icon {
      font-size: 14px;
      color: rgba(0, 0, 0, 0.4);
    }

    .chat-link-title {
      font-size: 11px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      flex: 1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* File operation display */
    .file-op {
      margin-top: 8px;
      padding: 8px 10px;
      background: rgba(0, 0, 0, 0.03);
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .file-op-icon {
      font-size: 14px;
    }

    .file-op-text {
      font-size: 11px;
      color: rgba(0, 0, 0, 0.6);
      font-family: 'SF Mono', Menlo, monospace;
    }

    .file-op.success .file-op-icon { color: #34C759; }
    .file-op.error .file-op-icon { color: #FF453A; }

    /* File preview */
    .file-preview {
      margin-top: 8px;
      border: 1px solid rgba(0, 0, 0, 0.08);
      border-radius: 6px;
      overflow: hidden;
    }

    .file-preview-header {
      padding: 6px 10px;
      background: rgba(0, 0, 0, 0.04);
      border-bottom: 1px solid rgba(0, 0, 0, 0.06);
      font-size: 10px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.5);
      font-family: 'SF Mono', Menlo, monospace;
    }

    .file-preview .tool-output {
      margin: 0;
      border-radius: 0;
      border: none;
    }

    /* Tool result for non-search */
    .tool-output {
      margin-top: 8px;
      padding: 8px;
      background: rgba(0, 0, 0, 0.03);
      border-radius: 6px;
      font-size: 11px;
      font-family: 'SF Mono', Menlo, monospace;
      color: rgba(0, 0, 0, 0.6);
      white-space: pre-wrap;
      max-height: 100px;
      overflow-y: auto;
    }

    .tool-output.error {
      color: #FF453A;
      background: rgba(255, 69, 58, 0.05);
    }

    .empty-state {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: rgba(0, 0, 0, 0.5);
      gap: 12px;
      padding-bottom: 60px;
    }

    .empty-state-icon {
      width: 56px;
      height: 56px;
      background: rgba(0, 0, 0, 0.05);
      border: 1px solid rgba(0, 0, 0, 0.08);
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      color: rgba(0, 0, 0, 0.5);
    }

    .empty-state p { font-size: 15px; font-weight: 500; color: rgba(0, 0, 0, 0.6); }
    .empty-state .hint { font-size: 12px; color: rgba(0, 0, 0, 0.35); }

    /* Dark mode */
    @media (prefers-color-scheme: dark) {
      .login-card {
        background: rgba(255, 255, 255, 0.12);
        border-color: rgba(255, 255, 255, 0.2);
      }
      .login-container .subtitle { color: rgba(255, 255, 255, 0.5); }

      /* Home page dark mode */
      .home-input {
        color: #fff;
        border-bottom-color: rgba(255, 255, 255, 0.2);
      }
      .home-input:focus {
        border-bottom-color: #E8C4A0;
      }
      .home-input::placeholder {
        color: rgba(255, 255, 255, 0.35);
      }
      .model-option {
        border-color: rgba(255, 255, 255, 0.15);
        color: rgba(255, 255, 255, 0.5);
      }
      .model-option:hover {
        background: rgba(255, 255, 255, 0.08);
        color: rgba(255, 255, 255, 0.8);
      }
      .home-attach-btn {
        color: rgba(255, 255, 255, 0.5);
      }
      .home-attach-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.8);
      }
      .home-send-btn { box-shadow: 0 2px 8px rgba(204, 120, 92, 0.4); }
      .home-signout {
        color: rgba(255, 255, 255, 0.4);
      }
      .home-signout:hover {
        background: rgba(255, 255, 255, 0.08);
        color: rgba(255, 255, 255, 0.7);
      }

      .header {
        background: transparent;
      }
      .icon-btn {
        color: rgba(255, 255, 255, 0.5);
      }
      .icon-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.8);
      }
      .model-badge { color: rgba(255, 255, 255, 0.4); }
      .sign-out-btn {
        color: rgba(255, 255, 255, 0.4);
      }
      .sign-out-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.8);
      }
      .menu-btn {
        color: rgba(255, 255, 255, 0.5);
      }
      .menu-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.8);
      }
      .menu-dropdown {
        background: rgba(40, 40, 42, 0.95);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4), 0 0 0 1px rgba(255, 255, 255, 0.1);
      }
      .menu-item {
        color: rgba(255, 255, 255, 0.85);
      }
      .menu-item:hover {
        background: rgba(255, 255, 255, 0.1);
      }
      .menu-item svg {
        color: rgba(255, 255, 255, 0.5);
      }
      .menu-divider {
        background: rgba(255, 255, 255, 0.1);
      }
      .menu-item.danger {
        color: #e06c75;
      }
      .menu-item.danger svg {
        color: #e06c75;
      }

      .sidebar {
        background: rgba(28, 28, 30, 0.97);
        border-right-color: rgba(255, 255, 255, 0.08);
      }
      .sidebar-header { border-bottom-color: rgba(255, 255, 255, 0.06); }
      .sidebar-title { color: rgba(255, 255, 255, 0.6); }
      .settings-btn { color: rgba(255, 255, 255, 0.4); }
      .settings-btn:hover { background: rgba(255, 255, 255, 0.1); color: rgba(255, 255, 255, 0.7); }
      .sidebar-tab-indicator {
        background: rgba(255, 255, 255, 0.08);
      }
      .sidebar-tab:hover .sidebar-tab-indicator {
        background: rgba(255, 255, 255, 0.15);
      }
      .sidebar-tab-indicator::after {
        background: rgba(255, 255, 255, 0.35);
      }
      .conv-item:hover { background: rgba(255, 255, 255, 0.08); }
      .conv-item.active { background: rgba(204, 120, 92, 0.25); }
      .conv-item-title { color: rgba(255, 255, 255, 0.85); }
      .conv-item-date { color: rgba(255, 255, 255, 0.4); }
      .conv-loading { color: rgba(255, 255, 255, 0.4); }
      .conv-section-header { color: rgba(255, 255, 255, 0.4); }
      .conv-menu-btn {
        color: rgba(255, 255, 255, 0.4);
      }
      .conv-menu-btn:hover {
        background: rgba(255, 255, 255, 0.12);
        color: rgba(255, 255, 255, 0.8);
      }
      .conv-dropdown {
        background: rgba(40, 40, 42, 0.95);
        border-color: rgba(255, 255, 255, 0.15);
      }
      .conv-dropdown-item {
        color: rgba(255, 255, 255, 0.8);
      }
      .conv-dropdown-item:hover {
        background: rgba(255, 255, 255, 0.08);
      }
      .conv-dropdown-item.delete {
        color: #FF6B6B;
      }
      .conv-dropdown-item.delete:hover {
        background: rgba(255, 107, 107, 0.15);
      }
      .conv-rename-input {
        background: rgba(0, 0, 0, 0.3);
        border-color: rgba(204, 120, 92, 0.5);
        color: rgba(255, 255, 255, 0.9);
      }

      .messages::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.15); }

      .message.assistant .message-content {
        background: rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.12);
        color: #fff;
      }
      .message-content code { background: rgba(0, 0, 0, 0.3); color: #E8C4A0; }
      .message-content pre { background: rgba(0, 0, 0, 0.4); border-color: rgba(255, 255, 255, 0.1); }
      .message-content pre code { color: rgba(255, 255, 255, 0.9); }
      .message-content a { color: #E8C4A0; }
      .message-content hr { border-top-color: rgba(255, 255, 255, 0.15); }

      .input-area {
        background: rgba(255, 255, 255, 0.06);
        border-top-color: rgba(255, 255, 255, 0.1);
      }
      .input-wrapper {
        background: rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.15);
      }
      .input-wrapper:focus-within { background: rgba(255, 255, 255, 0.12); }
      .input-area textarea { color: #fff; }
      .input-area textarea::placeholder { color: rgba(255, 255, 255, 0.4); }
      .attach-btn {
        color: rgba(255, 255, 255, 0.5);
      }
      .attach-btn:hover { background: rgba(255, 255, 255, 0.1); color: rgba(255, 255, 255, 0.8); }
      .attachment-pill {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.12);
      }
      .attachment-icon {
        background: rgba(255, 255, 255, 0.08);
      }
      .attachment-name { color: rgba(255, 255, 255, 0.9); }
      .attachment-size { color: rgba(255, 255, 255, 0.5); }
      .attachment-remove { color: rgba(255, 255, 255, 0.6); }
      .attachment-remove:hover { background: rgba(255, 255, 255, 0.12); color: #fff; }
      .attachment-status { color: rgba(255, 255, 255, 0.7); }
      .message-attachment-row {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.12);
      }
      .message-attachment-icon {
        background: rgba(255, 255, 255, 0.08);
      }
      .attachment-icon-svg {
        color: rgba(255, 255, 255, 0.5);
      }
      .message-attachment-name { color: rgba(255, 255, 255, 0.9); }
      .message-attachment-size { color: rgba(255, 255, 255, 0.5); }

      .empty-state { color: rgba(255, 255, 255, 0.5); }
      .empty-state p { color: rgba(255, 255, 255, 0.7); }
      .empty-state .hint { color: rgba(255, 255, 255, 0.35); }
      .empty-state-icon {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.6);
      }
      .loading-dots span { background: rgba(255, 255, 255, 0.4); }

      .thinking-block {
        background: rgba(204, 120, 92, 0.12);
        border-color: rgba(204, 120, 92, 0.25);
      }
      .thinking-header { color: rgba(255, 255, 255, 0.5); }
      .thinking-header:hover { background: rgba(204, 120, 92, 0.1); }
      .thinking-text { color: rgba(255, 255, 255, 0.5); }

      .steps-timeline {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(255, 255, 255, 0.08);
      }
      .step-line-top, .step-line-bottom, .step-line-extend { background: rgba(255, 255, 255, 0.15); }
      .step-item:last-child .step-line-extend { background: transparent; }
      .step-dot { background: rgba(255, 255, 255, 0.2); }
      .step-header:hover { background: rgba(255, 255, 255, 0.06); }
      .step-label { color: #fff !important; }
      .step-item.thinking .step-label { color: #fff !important; }
      .step-item.tool .step-label { color: #fff !important; }
      .step-meta { color: rgba(255, 255, 255, 0.6); }
      .step-chevron { color: rgba(255, 255, 255, 0.6); }
      .step-text { color: #fff !important; }
      .step-spinner { border-color: rgba(255, 255, 255, 0.15); border-top-color: rgba(255, 255, 255, 0.5); }
      .search-result-item {
        background: rgba(255, 255, 255, 0.08);
      }
      .search-result-item:hover {
        background: rgba(255, 255, 255, 0.12);
      }
      .search-result-favicon { background: rgba(255, 255, 255, 0.1); }
      .search-result-title { color: rgba(255, 255, 255, 0.85); }
      .search-result-site { color: rgba(255, 255, 255, 0.4); }
      .link-card {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.1);
      }
      .link-card:hover {
        background: rgba(255, 255, 255, 0.12);
        border-color: rgba(255, 255, 255, 0.15);
      }
      .link-card-icon { background: rgba(255, 255, 255, 0.1); }
      .link-card-title { color: rgba(255, 255, 255, 0.85); }
      .link-card-url { color: rgba(255, 255, 255, 0.4); }
      .chat-link-item {
        background: rgba(255, 255, 255, 0.08);
      }
      .chat-link-item:hover {
        background: rgba(255, 255, 255, 0.12);
      }
      .chat-link-icon { color: rgba(255, 255, 255, 0.4); }
      .chat-link-title { color: rgba(255, 255, 255, 0.85); }
      .file-op {
        background: rgba(255, 255, 255, 0.05);
      }
      .file-op-text { color: rgba(255, 255, 255, 0.6); }
      .file-preview {
        border-color: rgba(255, 255, 255, 0.1);
      }
      .file-preview-header {
        background: rgba(255, 255, 255, 0.05);
        border-bottom-color: rgba(255, 255, 255, 0.08);
        color: rgba(255, 255, 255, 0.5);
      }
      .tool-output {
        background: rgba(0, 0, 0, 0.2);
        color: rgba(255, 255, 255, 0.6);
      }
      .tool-output.error { background: rgba(255, 69, 58, 0.15); }
      .citation-link { color: #E8C4A0; }
      .citation-num { color: #E8C4A0; }
    }
  </style>
</head>
<body>
  <div id="login" class="login-container">
    <div class="login-card">
      <div class="logo"><img src="logo.svg" alt="Logo"></div>
      <h1>Open Claude</h1>
      <p class="subtitle">Sign in to continue</p>
      <button class="login-btn" id="login-btn">Continue</button>
      <p id="login-error" class="error"></p>
    </div>
  </div>

  <!-- Sidebar tab trigger (edge hover) -->
  <div class="sidebar-tab" id="sidebar-tab">
    <div class="sidebar-tab-indicator" id="sidebar-tab-indicator"></div>
  </div>

  <!-- Sidebar overlay (shared) -->
  <div class="sidebar-overlay" id="sidebar-overlay"></div>

  <!-- Sidebar (shared between home and chat) -->
  <div class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <span class="sidebar-title">Chats</span>
      <div class="sidebar-spacer"></div>
      <button class="new-chat-btn" id="new-chat-btn" title="New chat">+</button>
    </div>
    <div class="sidebar-content" id="sidebar-content">
      <div class="conv-loading">Loading...</div>
    </div>
  </div>

  <!-- Home page with model selector -->
  <div id="home" class="home-container">
    <!-- Draggable area for window movement -->
    <div class="home-drag-region"></div>
    <!-- Home header with menu -->
    <div class="home-header">
      <div class="menu-container">
        <button class="menu-btn" id="home-menu-btn" title="Menu">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
            <circle cx="12" cy="5" r="2"></circle>
            <circle cx="12" cy="12" r="2"></circle>
            <circle cx="12" cy="19" r="2"></circle>
          </svg>
        </button>
        <div class="menu-dropdown" id="home-menu-dropdown">
          <button class="menu-item" id="home-menu-new-window">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <rect x="3" y="3" width="13" height="13" rx="2" ry="2"></rect>
              <path d="M21 8v13H8"></path>
            </svg>
            New Window
          </button>
          <button class="menu-item" id="home-menu-settings">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="3"></circle>
              <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
            </svg>
            Settings
          </button>
          <div class="menu-divider"></div>
          <button class="menu-item danger" id="home-menu-signout">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
              <polyline points="16 17 21 12 16 7"></polyline>
              <line x1="21" y1="12" x2="9" y2="12"></line>
            </svg>
            Sign Out
          </button>
        </div>
      </div>
    </div>
    <div class="home-content">
      <div class="home-logo">✦</div>
      <div class="home-input-area">
        <div class="home-input-wrapper">
          <textarea id="home-input" class="home-input" placeholder="Message Claude..." rows="1"></textarea>
          <div class="home-input-footer">
            <div class="model-selector">
              <button class="model-option active" data-model="claude-opus-4-5-20251101">Opus</button>
              <button class="model-option" data-model="claude-sonnet-4-5-20250929">Sonnet</button>
              <button class="model-option" data-model="claude-haiku-4-5-20251001">Haiku</button>
            </div>
            <button class="home-attach-btn" id="home-attach-btn" title="Attach files">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path>
              </svg>
            </button>
            <button class="home-send-btn" id="home-send-btn">↑</button>
          </div>
          <div class="attachment-container" id="home-attachment-container">
            <div class="attachment-list" id="home-attachment-list"></div>
            <div class="attachment-status" id="home-attachment-status"></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div id="chat" class="chat-container">
    <!-- Header -->
    <div class="header">
      <div class="header-left">
        <!-- Icons removed - using sidebar tab instead -->
      </div>
      <div class="header-right">
        <span class="model-badge">Opus 4.5</span>
        <div class="menu-container">
          <button class="menu-btn" id="menu-btn" title="Menu">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
              <circle cx="12" cy="5" r="2"></circle>
              <circle cx="12" cy="12" r="2"></circle>
              <circle cx="12" cy="19" r="2"></circle>
            </svg>
          </button>
          <div class="menu-dropdown" id="menu-dropdown">
            <button class="menu-item" id="menu-new-window">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="13" height="13" rx="2" ry="2"></rect>
                <path d="M21 8v13H8"></path>
              </svg>
              New Window
            </button>
            <button class="menu-item" id="menu-export">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
                <polyline points="7 10 12 15 17 10"></polyline>
                <line x1="12" y1="15" x2="12" y2="3"></line>
              </svg>
              Export Markdown
            </button>
            <div class="menu-divider"></div>
            <button class="menu-item danger" id="menu-signout">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                <polyline points="16 17 21 12 16 7"></polyline>
                <line x1="21" y1="12" x2="9" y2="12"></line>
              </svg>
              Sign Out
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Messages -->
    <div id="messages" class="messages">
      <div class="empty-state" id="empty-state">
        <div class="empty-state-icon">✦</div>
        <p>What can I help with?</p>
        <span class="hint">Claude is ready</span>
      </div>
    </div>

    <!-- Input -->
    <div class="input-area">
      <div class="input-wrapper">
        <button class="attach-btn" id="attach-btn" title="Attach files">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path>
          </svg>
        </button>
        <textarea id="input" placeholder="Message Claude..." rows="1"></textarea>
        <button class="send-btn" id="send-btn">↑</button>
        <button class="stop-btn" id="stop-btn">■</button>
      </div>
      <div class="attachment-container" id="attachment-container">
        <div class="attachment-list" id="attachment-list"></div>
        <div class="attachment-status" id="attachment-status"></div>
      </div>
    </div>
  </div>

  <input type="file" id="file-input" multiple accept="*/*" style="display:none" />

  <script type="module" src="js/main.js"></script>
</body>
</html>
```

## File: `static/settings.html`
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Settings</title>
  <link rel="stylesheet" href="styles/settings.css">
</head>
<body>
  <div class="settings-container">
    <div class="settings-header">
      <h1>Settings</h1>
    </div>

    <div class="settings-content">
      <!-- Keyboard Shortcuts Section -->
      <div class="settings-section">
        <h2>Keyboard Shortcuts</h2>

        <div class="setting-item">
          <div class="setting-info">
            <label>Open Spotlight</label>
            <span class="setting-description">Global shortcut to open spotlight chat</span>
          </div>
          <div class="keybind-input" id="keybind-input" tabindex="0">
            <span class="keybind-display" id="keybind-display">⌘ + Shift + C</span>
            <span class="keybind-hint">Click to change</span>
          </div>
        </div>

        <div class="setting-item">
          <div class="setting-info">
            <label>New Window</label>
            <span class="setting-description">Global shortcut to open a new window</span>
          </div>
          <div class="keybind-input" id="new-window-keybind-input" tabindex="0">
            <span class="keybind-display" id="new-window-keybind-display">⌘ + Shift + N</span>
            <span class="keybind-hint">Click to change</span>
          </div>
        </div>
      </div>

      <!-- Spotlight Section -->
      <div class="settings-section">
        <h2>Spotlight</h2>

        <div class="setting-item">
          <div class="setting-info">
            <label>Persist History</label>
            <span class="setting-description">Keep spotlight chat history after closing</span>
          </div>
          <label class="toggle">
            <input type="checkbox" id="persist-history">
            <span class="toggle-slider"></span>
          </label>
        </div>
      </div>

      <!-- About Section -->
      <div class="settings-section">
        <h2>About</h2>
        <div class="about-info">
          <div class="about-row">
            <span class="about-label">Version</span>
            <span class="about-value" id="app-version">1.0.0</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script type="module" src="js/settings.js"></script>
</body>
</html>
```

## File: `static/spotlight.html`
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Quick Chat</title>
  <link rel="stylesheet" href="styles/spotlight.css">
</head>
<body>
  <div class="spotlight-container" id="container">
    <div class="input-row" id="input-row">
      <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"/>
        <path d="M21 21l-4.35-4.35"/>
      </svg>
      <input type="text" id="spotlight-input" placeholder="Ask anything..." autofocus>
      <button class="new-chat-btn" id="new-chat-btn" title="New chat">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <line x1="12" y1="5" x2="12" y2="19"></line>
          <line x1="5" y1="12" x2="19" y2="12"></line>
        </svg>
      </button>
      <button class="send-btn" id="send-btn" disabled>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
          <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
        </svg>
      </button>
    </div>
    <div class="messages-area" id="messages-area"></div>
  </div>

  <script type="module" src="js/spotlight.js"></script>
</body>
</html>
```

## File: `static/styles/main.css`
```css
    * { margin: 0; padding: 0; box-sizing: border-box; }

    html, body {
      height: 100%;
      background: transparent;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', system-ui, sans-serif;
      color: #000;
      height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
    }

    @media (prefers-color-scheme: dark) {
      body { color: #fff; }
    }

    /* Login */
    .login-container {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      padding: 40px;
    }

    .login-card {
      background: rgba(255, 255, 255, 0.6);
      backdrop-filter: blur(80px) saturate(200%);
      -webkit-backdrop-filter: blur(80px) saturate(200%);
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-radius: 20px;
      padding: 44px 52px;
      text-align: center;
      max-width: 320px;
      width: 100%;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    }

    .logo {
      width: 72px;
      height: 72px;
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 50%, #CC785C 100%);
      border-radius: 18px;
      margin: 0 auto 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 32px;
      color: white;
      box-shadow: 0 4px 16px rgba(204, 120, 92, 0.35);
    }

    .login-container h1 {
      font-size: 22px;
      font-weight: 600;
      letter-spacing: -0.4px;
      margin-bottom: 6px;
    }

    .login-container .subtitle {
      color: rgba(0, 0, 0, 0.5);
      font-size: 14px;
      margin-bottom: 28px;
    }

    .login-btn {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      color: white;
      border: none;
      padding: 12px 24px;
      border-radius: 12px;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      width: 100%;
      transition: all 0.2s;
      box-shadow: 0 2px 8px rgba(204, 120, 92, 0.3);
    }

    .login-btn:hover {
      transform: translateY(-1px);
      box-shadow: 0 4px 16px rgba(204, 120, 92, 0.4);
    }
    .login-btn:active { transform: scale(0.98); }

    .error { color: #FF453A; font-size: 11px; margin-top: 12px; }

    /* Home page */
    .home-container {
      display: none;
      flex-direction: column;
      height: 100vh;
      position: relative;
    }
    .home-container.active { display: flex; }

    .home-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 40px 20px;
    }

    /* Draggable header area for home page */
    .home-drag-region {
      position: absolute;
      top: 0;
      left: 30px; /* Leave space for sidebar tab */
      right: 0;
      height: 50px;
      -webkit-app-region: drag;
    }

    .home-logo {
      display: none;
    }

    .home-input-area {
      width: 100%;
      max-width: 600px;
      -webkit-app-region: no-drag;
      text-align: center;
    }

    .home-input-wrapper {
      background: transparent;
      padding: 0;
    }

    .home-input {
      width: 100%;
      background: transparent;
      border: none;
      border-bottom: 1px solid rgba(0, 0, 0, 0.15);
      font-size: 18px;
      font-family: inherit;
      color: #000;
      outline: none;
      resize: none;
      min-height: 28px;
      max-height: 200px;
      line-height: 1.5;
      padding: 8px 0;
      caret-color: #CC785C;
    }

    .home-input::placeholder {
      color: rgba(0, 0, 0, 0.3);
    }

    .home-input:focus {
      border-bottom-color: #CC785C;
    }

    .home-input-footer {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
    }

    .home-send-btn {
      display: none;
    }

    .model-selector {
      display: flex;
      gap: 6px;
    }

    .model-option {
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 500;
      background: transparent;
      border: 1px solid rgba(0, 0, 0, 0.1);
      color: rgba(0, 0, 0, 0.5);
      cursor: pointer;
      transition: all 0.15s;
    }

    .model-option:hover {
      background: rgba(0, 0, 0, 0.04);
      color: rgba(0, 0, 0, 0.7);
    }

    .model-option.active {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      border-color: transparent;
      color: white;
    }


    .home-footer {
      position: absolute;
      bottom: 0;
      right: 0;
      padding: 16px;
      display: flex;
      justify-content: flex-end;
      -webkit-app-region: no-drag;
    }

    .home-signout {
      font-size: 12px;
      color: rgba(0, 0, 0, 0.4);
      background: none;
      border: none;
      cursor: pointer;
      padding: 6px 12px;
      border-radius: 6px;
      transition: all 0.15s;
    }

    .home-signout:hover {
      background: rgba(0, 0, 0, 0.05);
      color: rgba(0, 0, 0, 0.6);
    }

    /* Home to Chat transition animation */
    .home-container.transitioning {
      pointer-events: none;
    }

    .home-container.transitioning .home-content {
      animation: homeContentFadeOut 0.4s ease-out forwards;
    }

    .home-container.transitioning .home-input-area {
      animation: inputAreaMoveDown 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }

    .home-container.transitioning .home-input-footer {
      animation: footerFadeOut 0.25s ease-out forwards;
    }

    /* Chat container entrance animation */
    .chat-container.entering {
      display: flex;
      opacity: 0;
      animation: chatEnter 0.1s ease-out 0.3s forwards;
    }

    @keyframes chatEnter {
      from { opacity: 0; }
      to { opacity: 1; }
    }

    @keyframes inputAreaEnter {
      0% {
        opacity: 0;
        transform: translateY(20px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @keyframes headerEnter {
      0% { opacity: 0; }
      100% { opacity: 1; }
    }

    /* First user message fly-in animation */
    .message.fly-in {
      animation: messageFlyIn 0.4s cubic-bezier(0.4, 0, 0.2, 1) forwards;
    }

    @keyframes messageFlyIn {
      0% {
        opacity: 0;
        transform: translateY(100px) scale(0.95);
      }
      100% {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }

    /* Assistant message fade-in */
    .message.fade-in {
      animation: messageFadeIn 0.3s ease-out forwards;
    }

    @keyframes messageFadeIn {
      0% {
        opacity: 0;
        transform: translateY(10px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* Chat container */
    .chat-container { display: none; flex-direction: column; height: 100vh; position: relative; }
    .chat-container.active { display: flex; }

    /* Header */
    .header {
      padding: 0 16px;
      height: 44px;
      background: transparent;
      display: flex;
      justify-content: space-between;
      align-items: center;
      -webkit-app-region: drag;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-left: 70px;
    }

    .icon-btn {
      width: 28px;
      height: 28px;
      background: transparent;
      border: none;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      -webkit-app-region: no-drag;
      transition: all 0.15s;
      font-size: 15px;
      color: rgba(0, 0, 0, 0.45);
    }

    .icon-btn:hover {
      background: rgba(0, 0, 0, 0.06);
      color: rgba(0, 0, 0, 0.7);
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 8px;
      -webkit-app-region: no-drag;
    }

    .model-badge {
      font-size: 11px;
      color: rgba(0, 0, 0, 0.4);
      padding: 0;
      font-weight: 500;
    }

    .sign-out-btn {
      background: transparent;
      border: none;
      color: rgba(0, 0, 0, 0.4);
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s;
    }

    .sign-out-btn:hover {
      background: rgba(0, 0, 0, 0.06);
      color: rgba(0, 0, 0, 0.7);
    }

    /* Sidebar overlay */
    .sidebar-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.3);
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.25s, visibility 0.25s;
      z-index: 100;
    }

    .sidebar-overlay.open {
      opacity: 1;
      visibility: visible;
    }

    /* Sidebar */
    .sidebar {
      position: fixed;
      top: 0;
      left: 0;
      width: 260px;
      height: 100%;
      background: rgba(246, 246, 246, 0.97);
      backdrop-filter: blur(40px);
      -webkit-backdrop-filter: blur(40px);
      border-right: 1px solid rgba(0, 0, 0, 0.1);
      transform: translateX(-100%);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 101;
      display: flex;
      flex-direction: column;
    }

    .sidebar.open {
      transform: translateX(0);
    }

    /* Sidebar trigger tab - invisible hover zone spanning 70% of height */
    .sidebar-tab {
      position: fixed;
      left: 0;
      top: 15%;
      width: 6px;
      height: 70%;
      background: transparent;
      cursor: pointer;
      z-index: 99;
      -webkit-app-region: no-drag;
    }

    .sidebar-tab:hover {
      width: 24px;
    }

    /* The visual indicator that follows the mouse */
    .sidebar-tab-indicator {
      position: absolute;
      left: 0;
      width: 6px;
      height: 60px;
      background: rgba(0, 0, 0, 0.08);
      border-radius: 0 4px 4px 0;
      transform: translateY(-50%);
      transition: width 0.2s, background 0.2s;
      display: flex;
      align-items: center;
      justify-content: center;
      pointer-events: none;
      opacity: 0;
    }

    .sidebar-tab:hover .sidebar-tab-indicator {
      width: 24px;
      background: rgba(0, 0, 0, 0.12);
      opacity: 1;
    }

    .sidebar-tab-indicator::after {
      content: '';
      width: 2px;
      height: 20px;
      background: rgba(0, 0, 0, 0.25);
      border-radius: 1px;
      opacity: 0;
      transition: opacity 0.2s;
    }

    .sidebar-tab:hover .sidebar-tab-indicator::after {
      opacity: 1;
    }

    .sidebar-tab.hidden {
      opacity: 0;
      pointer-events: none;
    }

    .sidebar-header {
      padding: 12px 16px;
      padding-top: 48px;
      border-bottom: 1px solid rgba(0, 0, 0, 0.06);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .sidebar-title {
      font-size: 13px;
      font-weight: 600;
      color: rgba(0, 0, 0, 0.7);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .sidebar-spacer {
      flex: 1;
    }

    .new-chat-btn {
      width: 24px;
      height: 24px;
      background: #CC785C;
      border: none;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 16px;
      font-weight: 300;
      color: white;
      transition: all 0.15s;
      box-shadow: 0 2px 6px rgba(204, 120, 92, 0.3);
    }

    .new-chat-btn:hover {
      background: #B86A50;
      transform: scale(1.05);
      box-shadow: 0 3px 8px rgba(204, 120, 92, 0.4);
    }

    .sidebar-content {
      flex: 1;
      overflow-y: auto;
      padding: 8px;
    }

    .sidebar-content::-webkit-scrollbar { display: none; }
    .sidebar-content { -ms-overflow-style: none; scrollbar-width: none; }

    .conv-item {
      padding: 10px 12px;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.15s;
      margin-bottom: 2px;
    }

    .conv-item:hover {
      background: rgba(0, 0, 0, 0.05);
    }

    .conv-item.active {
      background: rgba(204, 120, 92, 0.15);
    }

    .conv-item-title {
      font-size: 13px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .conv-item-date {
      font-size: 11px;
      color: rgba(0, 0, 0, 0.4);
      margin-top: 2px;
    }

    .conv-loading {
      text-align: center;
      padding: 20px;
      color: rgba(0, 0, 0, 0.4);
      font-size: 13px;
    }

    /* Conversation item with menu */
    .conv-item {
      position: relative;
    }

    .conv-item-row {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .conv-item-info {
      flex: 1;
      min-width: 0;
    }

    .conv-star {
      color: #CC785C;
      font-size: 10px;
      margin-right: 4px;
    }

    .conv-menu-btn {
      width: 24px;
      height: 24px;
      background: transparent;
      border: none;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      opacity: 0;
      transition: all 0.15s;
      color: rgba(0, 0, 0, 0.4);
      font-size: 14px;
      flex-shrink: 0;
    }

    .conv-item:hover .conv-menu-btn {
      opacity: 1;
    }

    .conv-menu-btn:hover {
      background: rgba(0, 0, 0, 0.08);
      color: rgba(0, 0, 0, 0.7);
    }

    /* Dropdown menu */
    .conv-dropdown {
      position: absolute;
      right: 8px;
      top: 100%;
      background: rgba(255, 255, 255, 0.95);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
      z-index: 200;
      min-width: 120px;
      overflow: hidden;
      display: none;
    }

    .conv-dropdown.open {
      display: block;
    }

    .conv-dropdown-item {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      font-size: 12px;
      color: rgba(0, 0, 0, 0.7);
      cursor: pointer;
      transition: background 0.1s;
    }

    .conv-dropdown-item:hover {
      background: rgba(0, 0, 0, 0.05);
    }

    .conv-dropdown-item.delete {
      color: #FF453A;
    }

    .conv-dropdown-item.delete:hover {
      background: rgba(255, 69, 58, 0.1);
    }

    .conv-dropdown-icon {
      font-size: 12px;
      width: 16px;
      text-align: center;
    }

    /* Rename input */
    .conv-rename-input {
      width: 100%;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(204, 120, 92, 0.5);
      border-radius: 4px;
      padding: 4px 8px;
      font-size: 13px;
      font-family: inherit;
      color: rgba(0, 0, 0, 0.8);
      outline: none;
    }

    .conv-rename-input:focus {
      border-color: #CC785C;
    }

    /* Messages */
    .messages {
      flex: 1;
      overflow-y: auto;
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .messages::-webkit-scrollbar { width: 6px; }
    .messages::-webkit-scrollbar-track { background: transparent; }
    .messages::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.1); border-radius: 3px; }

    .message { max-width: 78%; }
    .message:not(.fly-in):not(.fade-in) { animation: msgIn 0.2s ease forwards; }
    @keyframes msgIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    .message.user { align-self: flex-end; }
    .message.assistant { align-self: flex-start; }

    .message-content {
      padding: 12px 16px;
      border-radius: 18px;
      line-height: 1.5;
      font-size: 14px;
    }

    .message.user .message-content {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      color: white;
      border-bottom-right-radius: 6px;
    }

    .message.assistant .message-content {
      background: rgba(255, 255, 255, 0.7);
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-bottom-left-radius: 6px;
      color: #000;
    }

    /* Message edit feature */
    .message.user {
      position: relative;
    }
    .message.user .edit-btn {
      position: absolute;
      bottom: 4px;
      left: -28px;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(0, 0, 0, 0.1);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.15s, transform 0.15s;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    .message.user .edit-btn svg {
      width: 12px;
      height: 12px;
      color: #666;
    }
    .message.user:hover .edit-btn {
      opacity: 1;
    }
    .message.user .edit-btn:hover {
      transform: scale(1.1);
      background: #fff;
    }
    .message.user.editing .edit-btn {
      display: none;
    }
    .message.user.editing .message-content {
      background: transparent;
      padding: 0;
    }
    .message-edit-container {
      display: flex;
      flex-direction: column;
      gap: 8px;
      min-width: 200px;
    }
    .message-edit-textarea {
      background: rgba(255, 255, 255, 0.9);
      border: 1px solid rgba(204, 120, 92, 0.5);
      border-radius: 14px;
      padding: 10px 14px;
      font-size: 14px;
      font-family: inherit;
      color: #000;
      resize: none;
      min-height: 40px;
      max-height: 200px;
      line-height: 1.5;
    }
    .message-edit-textarea:focus {
      outline: none;
      border-color: #CC785C;
      box-shadow: 0 0 0 3px rgba(204, 120, 92, 0.15);
    }
    .message-edit-actions {
      display: flex;
      gap: 6px;
      justify-content: flex-end;
    }
    .message-edit-actions button {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.15s;
    }
    .message-edit-actions button:hover {
      transform: scale(1.1);
    }
    .message-edit-cancel {
      background: rgba(0, 0, 0, 0.08);
    }
    .message-edit-cancel svg {
      width: 14px;
      height: 14px;
      color: #666;
    }
    .message-edit-submit {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      box-shadow: 0 2px 6px rgba(204, 120, 92, 0.3);
    }
    .message-edit-submit svg {
      width: 14px;
      height: 14px;
      color: white;
    }

    .message-content p { margin: 0 0 6px 0; }
    .message-content p:last-child { margin-bottom: 0; }
    .message-content p:first-child { margin-top: 0; }
    .message-content h1, .message-content h2, .message-content h3 { margin: 10px 0 4px; font-weight: 600; }
    .message-content h1:first-child, .message-content h2:first-child, .message-content h3:first-child { margin-top: 0; }
    .message-content h1 { font-size: 1.2em; }
    .message-content h2 { font-size: 1.1em; }
    .message-content h3 { font-size: 1.05em; }
    .message-content strong { font-weight: 600; }
    .message-content code {
      font-family: 'SF Mono', Menlo, monospace;
      font-size: 0.9em;
      background: rgba(0, 0, 0, 0.08);
      padding: 2px 6px;
      border-radius: 4px;
      color: #9a5d3a;
    }
    .message.user .message-content code { background: rgba(255, 255, 255, 0.2); color: #fff; }
    .message-content pre {
      background: rgba(0, 0, 0, 0.05);
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-radius: 10px;
      padding: 12px;
      overflow-x: auto;
      margin: 8px 0;
    }
    .message-content pre code { background: transparent; padding: 0; font-size: 12px; line-height: 1.5; color: #333; }
    .message-content ul, .message-content ol { margin: 6px 0; padding-left: 20px; }
    .message-content li { margin: 2px 0; }
    .message-content blockquote {
      border-left: 3px solid #CC785C;
      margin: 8px 0;
      padding: 6px 12px;
      background: rgba(204, 120, 92, 0.1);
      border-radius: 0 8px 8px 0;
    }
    .message-content a { color: #9a5d3a; text-decoration: none; }
    .message-content a:hover { text-decoration: underline; }
    .message-content hr {
      border: none;
      border-top: 1px solid rgba(0, 0, 0, 0.12);
      margin: 12px 0;
    }

    /* Citation styling */
    .citation-link {
      color: #CC785C;
      text-decoration: underline;
      text-decoration-style: dotted;
      text-underline-offset: 2px;
    }
    .citation-link:hover {
      text-decoration-style: solid;
    }
    .citation-num {
      font-size: 10px;
      color: #CC785C;
      font-weight: 600;
      vertical-align: super;
      margin-left: 1px;
      cursor: pointer;
    }
    .citation-num:hover {
      text-decoration: underline;
    }

    /* Input area */
    .input-area {
      padding: 16px 20px 20px;
      background: rgba(255, 255, 255, 0.4);
      backdrop-filter: blur(40px) saturate(180%);
      -webkit-backdrop-filter: blur(40px) saturate(180%);
      border-top: 1px solid rgba(0, 0, 0, 0.1);
    }

    .input-wrapper {
      display: flex;
      gap: 10px;
      align-items: flex-end;
      background: rgba(255, 255, 255, 0.7);
      border: 1px solid rgba(0, 0, 0, 0.15);
      border-radius: 22px;
      padding: 6px 6px 6px 16px;
      transition: all 0.2s;
    }

    .input-wrapper:focus-within {
      border-color: rgba(204, 120, 92, 0.5);
      background: rgba(255, 255, 255, 0.85);
      box-shadow: 0 0 0 3px rgba(204, 120, 92, 0.15);
    }

    .input-area textarea {
      flex: 1;
      background: transparent;
      border: none;
      padding: 8px 0;
      color: #000;
      font-size: 14px;
      resize: none;
      font-family: inherit;
      min-height: 20px;
      max-height: 120px;
      line-height: 1.4;
    }

    .input-area textarea::placeholder { color: rgba(0, 0, 0, 0.4); }
    .input-area textarea:focus { outline: none; }

    .send-btn {
      background: linear-gradient(145deg, #CC785C 0%, #D4846A 100%);
      color: white;
      border: none;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 15px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.15s;
      flex-shrink: 0;
      box-shadow: 0 2px 6px rgba(204, 120, 92, 0.3);
    }

    .send-btn:hover:not(:disabled) { transform: scale(1.05); }
    .send-btn:active:not(:disabled) { transform: scale(0.95); }
    .send-btn:disabled { opacity: 0.4; cursor: not-allowed; }

    .stop-btn {
      display: none;
      background: rgba(120, 120, 128, 0.16);
      color: rgba(0, 0, 0, 0.6);
      border: 1px solid rgba(0, 0, 0, 0.08);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 10px;
      font-weight: 500;
      transition: all 0.15s;
      align-self: flex-end;
      flex-shrink: 0;
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
    }
    .stop-btn:hover { background: rgba(120, 120, 128, 0.24); color: rgba(0, 0, 0, 0.8); }
    .stop-btn:active { transform: scale(0.95); }
    .stop-btn.visible { display: flex; align-items: center; justify-content: center; }
    .send-btn.hidden { display: none; }

    .loading-dots { display: flex; gap: 4px; padding: 4px 0; }
    .loading-dots span {
      width: 6px;
      height: 6px;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 50%;
      animation: pulse 1.2s ease-in-out infinite;
    }
    .loading-dots span:nth-child(1) { animation-delay: 0s; }
    .loading-dots span:nth-child(2) { animation-delay: 0.15s; }
    .loading-dots span:nth-child(3) { animation-delay: 0.3s; }
    @keyframes pulse { 0%, 80%, 100% { opacity: 0.35; } 40% { opacity: 1; } }

    /* Thinking block */
    .thinking-block {
      background: rgba(204, 120, 92, 0.08);
      border: 1px solid rgba(204, 120, 92, 0.2);
      border-radius: 10px;
      margin-bottom: 10px;
      overflow: hidden;
    }

    .thinking-header {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 12px;
      cursor: pointer;
      font-size: 12px;
      color: rgba(0, 0, 0, 0.5);
      font-weight: 500;
      transition: background 0.15s;
    }

    .thinking-header:hover {
      background: rgba(204, 120, 92, 0.05);
    }

    .thinking-icon {
      font-size: 14px;
      transition: transform 0.2s;
    }

    .thinking-block.expanded .thinking-icon {
      transform: rotate(90deg);
    }

    .thinking-label {
      flex: 1;
    }

    .thinking-spinner {
      width: 12px;
      height: 12px;
      border: 2px solid rgba(204, 120, 92, 0.3);
      border-top-color: #CC785C;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }

    @keyframes spin {
      to { transform: rotate(360deg); }
    }

    .thinking-content {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s ease;
    }

    .thinking-block.expanded .thinking-content {
      max-height: 300px;
      overflow-y: auto;
    }

    .thinking-text {
      padding: 0 12px 10px;
      font-size: 12px;
      line-height: 1.5;
      color: rgba(0, 0, 0, 0.5);
      white-space: pre-wrap;
      font-family: 'SF Mono', Menlo, monospace;
    }

    /* Steps Timeline - Card wrapper for thinking/tool blocks */
    .steps-timeline {
      margin-top: 10px;
      margin-bottom: 12px;
      background: rgba(0, 0, 0, 0.03);
      border: 1px solid rgba(0, 0, 0, 0.06);
      border-radius: 12px;
      padding: 8px 12px 8px 8px;
    }

    .step-item {
      display: flex;
      flex-direction: row;
      min-height: 34px;
    }

    /* Timeline column with line and dot */
    .step-timeline-col {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-left: 4px;
      width: 24px;
      flex-shrink: 0;
    }

    .step-dot-row {
      display: flex;
      flex-direction: column;
      align-items: center;
      height: 34px;
      justify-content: center;
    }

    .step-line-top {
      width: 1px;
      flex: 1;
      background: rgba(0, 0, 0, 0.12);
      min-height: 8px;
    }

    .step-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.12);
      flex-shrink: 0;
      margin: 4px 0;
    }

    .step-item.thinking .step-dot {
      background: #CC785C;
    }

    .step-item.tool .step-dot {
      background: #5856D6;
    }

    .step-line-bottom {
      width: 1px;
      flex: 1;
      background: rgba(0, 0, 0, 0.12);
      min-height: 8px;
    }

    .step-item:first-child .step-line-top {
      background: transparent;
    }

    .step-item:last-child .step-line-bottom {
      background: transparent;
    }

    .step-line-extend {
      width: 1px;
      flex: 1;
      background: rgba(0, 0, 0, 0.12);
      display: none;
    }

    .step-item.expanded .step-line-extend {
      display: block;
    }

    .step-item:last-child .step-line-extend {
      background: transparent;
    }

    /* Content column */
    .step-content-col {
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
    }

    .step-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      padding: 6px 10px 6px 4px;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.15s;
    }

    .step-header:hover {
      background: rgba(0, 0, 0, 0.04);
    }

    .step-label {
      font-size: 13px;
      font-weight: 400;
      color: rgba(0, 0, 0, 0.55);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      flex: 1;
      line-height: 1.4;
    }

    .step-item.thinking .step-label {
      color: rgba(0, 0, 0, 0.55);
    }

    .step-item.tool .step-label {
      color: rgba(0, 0, 0, 0.55);
    }

    .step-meta {
      font-size: 11px;
      color: rgba(0, 0, 0, 0.35);
      flex-shrink: 0;
      padding-left: 8px;
    }

    .step-spinner {
      width: 12px;
      height: 12px;
      border: 1.5px solid rgba(0, 0, 0, 0.12);
      border-top-color: rgba(0, 0, 0, 0.5);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
      flex-shrink: 0;
    }

    .step-chevron {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 16px;
      height: 16px;
      color: rgba(0, 0, 0, 0.35);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      flex-shrink: 0;
    }

    .step-chevron svg {
      width: 16px;
      height: 16px;
    }

    .step-item.expanded .step-chevron {
      transform: rotate(90deg);
    }

    .step-content {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s ease, opacity 0.2s;
      opacity: 0;
    }

    .step-item.expanded .step-content {
      max-height: 300px;
      overflow-y: auto;
      opacity: 1;
    }

    .step-text {
      padding: 8px 10px 12px 4px;
      font-size: 12px;
      line-height: 1.6;
      color: rgba(0, 0, 0, 0.5);
      white-space: pre-wrap;
      font-family: 'SF Mono', Menlo, monospace;
    }

    /* Web search results */
    .search-results {
      margin-top: 8px;
    }

    .search-result-item {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 6px 8px;
      background: rgba(255, 255, 255, 0.5);
      border-radius: 6px;
      margin-bottom: 4px;
      text-decoration: none;
      transition: background 0.15s;
    }

    .search-result-item:hover {
      background: rgba(255, 255, 255, 0.8);
    }

    .search-result-favicon {
      width: 16px;
      height: 16px;
      border-radius: 3px;
      flex-shrink: 0;
      background: rgba(0, 0, 0, 0.05);
    }

    .search-result-info {
      flex: 1;
      min-width: 0;
    }

    .search-result-title {
      font-size: 11px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .search-result-site {
      font-size: 10px;
      color: rgba(0, 0, 0, 0.4);
    }

    /* Link card for web_fetch */
    .link-card {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 12px;
      background: rgba(255, 255, 255, 0.5);
      border: 1px solid rgba(0, 0, 0, 0.08);
      border-radius: 8px;
      margin-top: 8px;
      text-decoration: none;
      transition: background 0.15s, border-color 0.15s;
    }

    .link-card:hover {
      background: rgba(255, 255, 255, 0.8);
      border-color: rgba(0, 0, 0, 0.12);
    }

    .link-card-icon {
      width: 20px;
      height: 20px;
      border-radius: 4px;
      flex-shrink: 0;
      background: rgba(0, 0, 0, 0.05);
    }

    .link-card-info {
      flex: 1;
      min-width: 0;
    }

    .link-card-title {
      font-size: 12px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .link-card-url {
      font-size: 10px;
      color: rgba(0, 0, 0, 0.4);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* Chat link items for conversation_search/recent_chats */
    .chat-links {
      margin-top: 8px;
    }

    .chat-link-item {
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 8px 10px;
      background: rgba(255, 255, 255, 0.5);
      border-radius: 6px;
      margin-bottom: 4px;
      text-decoration: none;
      transition: background 0.15s;
    }

    .chat-link-item:hover {
      background: rgba(255, 255, 255, 0.8);
    }

    .chat-link-icon {
      font-size: 14px;
      color: rgba(0, 0, 0, 0.4);
    }

    .chat-link-title {
      font-size: 11px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.8);
      flex: 1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* File operation display */
    .file-op {
      margin-top: 8px;
      padding: 8px 10px;
      background: rgba(0, 0, 0, 0.03);
      border-radius: 6px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .file-op-icon {
      font-size: 14px;
    }

    .file-op-text {
      font-size: 11px;
      color: rgba(0, 0, 0, 0.6);
      font-family: 'SF Mono', Menlo, monospace;
    }

    .file-op.success .file-op-icon { color: #34C759; }
    .file-op.error .file-op-icon { color: #FF453A; }

    /* File preview */
    .file-preview {
      margin-top: 8px;
      border: 1px solid rgba(0, 0, 0, 0.08);
      border-radius: 6px;
      overflow: hidden;
    }

    .file-preview-header {
      padding: 6px 10px;
      background: rgba(0, 0, 0, 0.04);
      border-bottom: 1px solid rgba(0, 0, 0, 0.06);
      font-size: 10px;
      font-weight: 500;
      color: rgba(0, 0, 0, 0.5);
      font-family: 'SF Mono', Menlo, monospace;
    }

    .file-preview .tool-output {
      margin: 0;
      border-radius: 0;
      border: none;
    }

    /* Tool result for non-search */
    .tool-output {
      margin-top: 8px;
      padding: 8px;
      background: rgba(0, 0, 0, 0.03);
      border-radius: 6px;
      font-size: 11px;
      font-family: 'SF Mono', Menlo, monospace;
      color: rgba(0, 0, 0, 0.6);
      white-space: pre-wrap;
      max-height: 100px;
      overflow-y: auto;
    }

    .tool-output.error {
      color: #FF453A;
      background: rgba(255, 69, 58, 0.05);
    }

    .empty-state {
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: rgba(0, 0, 0, 0.5);
      gap: 12px;
      padding-bottom: 60px;
    }

    .empty-state-icon {
      width: 56px;
      height: 56px;
      background: rgba(0, 0, 0, 0.05);
      border: 1px solid rgba(0, 0, 0, 0.08);
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      color: rgba(0, 0, 0, 0.5);
    }

    .empty-state p { font-size: 15px; font-weight: 500; color: rgba(0, 0, 0, 0.6); }
    .empty-state .hint { font-size: 12px; color: rgba(0, 0, 0, 0.35); }

    /* Dark mode */
    @media (prefers-color-scheme: dark) {
      .login-card {
        background: rgba(255, 255, 255, 0.12);
        border-color: rgba(255, 255, 255, 0.2);
      }
      .login-container .subtitle { color: rgba(255, 255, 255, 0.5); }

      /* Home page dark mode */
      .home-input {
        color: #fff;
        border-bottom-color: rgba(255, 255, 255, 0.2);
      }
      .home-input:focus {
        border-bottom-color: #E8C4A0;
      }
      .home-input::placeholder {
        color: rgba(255, 255, 255, 0.35);
      }
      .model-option {
        border-color: rgba(255, 255, 255, 0.15);
        color: rgba(255, 255, 255, 0.5);
      }
      .model-option:hover {
        background: rgba(255, 255, 255, 0.08);
        color: rgba(255, 255, 255, 0.8);
      }
      .home-signout {
        color: rgba(255, 255, 255, 0.4);
      }
      .home-signout:hover {
        background: rgba(255, 255, 255, 0.08);
        color: rgba(255, 255, 255, 0.7);
      }

      .header {
        background: transparent;
      }
      .icon-btn {
        color: rgba(255, 255, 255, 0.5);
      }
      .icon-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.8);
      }
      .model-badge { color: rgba(255, 255, 255, 0.4); }
      .sign-out-btn {
        color: rgba(255, 255, 255, 0.4);
      }
      .sign-out-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.8);
      }

      .sidebar {
        background: rgba(28, 28, 30, 0.97);
        border-right-color: rgba(255, 255, 255, 0.08);
      }
      .sidebar-header { border-bottom-color: rgba(255, 255, 255, 0.06); }
      .sidebar-title { color: rgba(255, 255, 255, 0.6); }
      .sidebar-tab-indicator {
        background: rgba(255, 255, 255, 0.08);
      }
      .sidebar-tab:hover .sidebar-tab-indicator {
        background: rgba(255, 255, 255, 0.15);
      }
      .sidebar-tab-indicator::after {
        background: rgba(255, 255, 255, 0.35);
      }
      .conv-item:hover { background: rgba(255, 255, 255, 0.08); }
      .conv-item.active { background: rgba(204, 120, 92, 0.25); }
      .conv-item-title { color: rgba(255, 255, 255, 0.85); }
      .conv-item-date { color: rgba(255, 255, 255, 0.4); }
      .conv-loading { color: rgba(255, 255, 255, 0.4); }
      .conv-menu-btn {
        color: rgba(255, 255, 255, 0.4);
      }
      .conv-menu-btn:hover {
        background: rgba(255, 255, 255, 0.12);
        color: rgba(255, 255, 255, 0.8);
      }
      .conv-dropdown {
        background: rgba(40, 40, 42, 0.95);
        border-color: rgba(255, 255, 255, 0.15);
      }
      .conv-dropdown-item {
        color: rgba(255, 255, 255, 0.8);
      }
      .conv-dropdown-item:hover {
        background: rgba(255, 255, 255, 0.08);
      }
      .conv-dropdown-item.delete {
        color: #FF6B6B;
      }
      .conv-dropdown-item.delete:hover {
        background: rgba(255, 107, 107, 0.15);
      }
      .conv-rename-input {
        background: rgba(0, 0, 0, 0.3);
        border-color: rgba(204, 120, 92, 0.5);
        color: rgba(255, 255, 255, 0.9);
      }

      .messages::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.15); }

      .message.assistant .message-content {
        background: rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.12);
        color: #fff;
      }
      .message-content code { background: rgba(0, 0, 0, 0.3); color: #E8C4A0; }
      .message-content pre { background: rgba(0, 0, 0, 0.4); border-color: rgba(255, 255, 255, 0.1); }
      .message-content pre code { color: rgba(255, 255, 255, 0.9); }
      .message-content a { color: #E8C4A0; }
      .message-content hr { border-top-color: rgba(255, 255, 255, 0.15); }

      .input-area {
        background: rgba(255, 255, 255, 0.06);
        border-top-color: rgba(255, 255, 255, 0.1);
      }
      .input-wrapper {
        background: rgba(255, 255, 255, 0.1);
        border-color: rgba(255, 255, 255, 0.15);
      }
      .input-wrapper:focus-within { background: rgba(255, 255, 255, 0.12); }
      .input-area textarea { color: #fff; }
      .input-area textarea::placeholder { color: rgba(255, 255, 255, 0.4); }

      .empty-state { color: rgba(255, 255, 255, 0.5); }
      .empty-state p { color: rgba(255, 255, 255, 0.7); }
      .empty-state .hint { color: rgba(255, 255, 255, 0.35); }
      .empty-state-icon {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.6);
      }
      .loading-dots span { background: rgba(255, 255, 255, 0.4); }

      .thinking-block {
        background: rgba(204, 120, 92, 0.12);
        border-color: rgba(204, 120, 92, 0.25);
      }
      .thinking-header { color: rgba(255, 255, 255, 0.5); }
      .thinking-header:hover { background: rgba(204, 120, 92, 0.1); }
      .thinking-text { color: rgba(255, 255, 255, 0.5); }

      .steps-timeline {
        background: rgba(255, 255, 255, 0.05);
        border-color: rgba(255, 255, 255, 0.08);
      }
      .step-line-top, .step-line-bottom, .step-line-extend { background: rgba(255, 255, 255, 0.15); }
      .step-item:last-child .step-line-extend { background: transparent; }
      .step-dot { background: rgba(255, 255, 255, 0.2); }
      .step-header:hover { background: rgba(255, 255, 255, 0.06); }
      .step-label { color: #fff !important; }
      .step-item.thinking .step-label { color: #fff !important; }
      .step-item.tool .step-label { color: #fff !important; }
      .step-meta { color: rgba(255, 255, 255, 0.6); }
      .step-chevron { color: rgba(255, 255, 255, 0.6); }
      .step-text { color: #fff !important; }
      .step-spinner { border-color: rgba(255, 255, 255, 0.15); border-top-color: rgba(255, 255, 255, 0.5); }
      .search-result-item {
        background: rgba(255, 255, 255, 0.08);
      }
      .search-result-item:hover {
        background: rgba(255, 255, 255, 0.12);
      }
      .search-result-favicon { background: rgba(255, 255, 255, 0.1); }
      .search-result-title { color: rgba(255, 255, 255, 0.85); }
      .search-result-site { color: rgba(255, 255, 255, 0.4); }
      .link-card {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.1);
      }
      .link-card:hover {
        background: rgba(255, 255, 255, 0.12);
        border-color: rgba(255, 255, 255, 0.15);
      }
      .link-card-icon { background: rgba(255, 255, 255, 0.1); }
      .link-card-title { color: rgba(255, 255, 255, 0.85); }
      .link-card-url { color: rgba(255, 255, 255, 0.4); }
      .chat-link-item {
        background: rgba(255, 255, 255, 0.08);
      }
      .chat-link-item:hover {
        background: rgba(255, 255, 255, 0.12);
      }
      .chat-link-icon { color: rgba(255, 255, 255, 0.4); }
      .chat-link-title { color: rgba(255, 255, 255, 0.85); }
      .file-op {
        background: rgba(255, 255, 255, 0.05);
      }
      .file-op-text { color: rgba(255, 255, 255, 0.6); }
      .file-preview {
        border-color: rgba(255, 255, 255, 0.1);
      }
      .file-preview-header {
        background: rgba(255, 255, 255, 0.05);
        border-bottom-color: rgba(255, 255, 255, 0.08);
        color: rgba(255, 255, 255, 0.5);
      }
      .tool-output {
        background: rgba(0, 0, 0, 0.2);
        color: rgba(255, 255, 255, 0.6);
      }
      .tool-output.error { background: rgba(255, 69, 58, 0.15); }
      .citation-link { color: #E8C4A0; }
      .citation-num { color: #E8C4A0; }
    }
```

## File: `static/styles/settings.css`
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: transparent;
  color: #1a1a1a;
  overflow: hidden;
}

.settings-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.settings-header {
  padding: 20px 24px;
  padding-top: 52px; /* Account for window controls */
  background: transparent;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  -webkit-app-region: drag;
}

.settings-header h1 {
  font-size: 20px;
  font-weight: 600;
  color: #1a1a1a;
}

.settings-content {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
}

.settings-content::-webkit-scrollbar {
  display: none;
}

.settings-section {
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-radius: 12px;
  padding: 20px;
  margin-bottom: 20px;
  border: 1px solid rgba(0, 0, 0, 0.06);
}

.settings-section h2 {
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: rgba(0, 0, 0, 0.5);
  margin-bottom: 16px;
}

.setting-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 0;
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}

.setting-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.setting-item:first-of-type {
  padding-top: 0;
}

.setting-info {
  flex: 1;
}

.setting-info label {
  display: block;
  font-size: 14px;
  font-weight: 500;
  color: #1a1a1a;
  margin-bottom: 2px;
}

.setting-description {
  font-size: 12px;
  color: rgba(0, 0, 0, 0.5);
}

/* Keybind input */
.keybind-input {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  padding: 8px 14px;
  background: rgba(0, 0, 0, 0.04);
  border: 1px solid rgba(0, 0, 0, 0.08);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.15s;
  min-width: 160px;
}

.keybind-input:hover {
  background: rgba(0, 0, 0, 0.06);
  border-color: rgba(0, 0, 0, 0.12);
}

.keybind-input:focus {
  outline: none;
  background: rgba(204, 120, 92, 0.08);
  border-color: #CC785C;
  box-shadow: 0 0 0 3px rgba(204, 120, 92, 0.15);
}

.keybind-input.recording {
  background: rgba(204, 120, 92, 0.1);
  border-color: #CC785C;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0%, 100% { box-shadow: 0 0 0 3px rgba(204, 120, 92, 0.15); }
  50% { box-shadow: 0 0 0 5px rgba(204, 120, 92, 0.1); }
}

.keybind-display {
  font-size: 13px;
  font-weight: 500;
  color: #1a1a1a;
  font-family: 'SF Mono', Menlo, monospace;
}

.keybind-hint {
  font-size: 10px;
  color: rgba(0, 0, 0, 0.4);
  margin-top: 2px;
}

.keybind-input.recording .keybind-hint {
  color: #CC785C;
}

.keybind-input.recording .keybind-display {
  color: #CC785C;
}

/* Toggle switch */
.toggle {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 26px;
}

.toggle input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle-slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.15);
  transition: 0.3s;
  border-radius: 26px;
}

.toggle-slider:before {
  position: absolute;
  content: "";
  height: 22px;
  width: 22px;
  left: 2px;
  bottom: 2px;
  background: white;
  transition: 0.3s;
  border-radius: 50%;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

.toggle input:checked + .toggle-slider {
  background: #CC785C;
}

.toggle input:checked + .toggle-slider:before {
  transform: translateX(18px);
}

.toggle input:focus + .toggle-slider {
  box-shadow: 0 0 0 3px rgba(204, 120, 92, 0.15);
}

/* About section */
.about-info {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.about-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.about-label {
  font-size: 14px;
  color: rgba(0, 0, 0, 0.6);
}

.about-value {
  font-size: 14px;
  color: #1a1a1a;
  font-family: 'SF Mono', Menlo, monospace;
}

/* Dark mode */
@media (prefers-color-scheme: dark) {
  body {
    color: #f0f0f0;
  }

  .settings-header {
    border-bottom-color: rgba(255, 255, 255, 0.06);
  }

  .settings-header h1 {
    color: #f0f0f0;
  }

  .settings-section {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.08);
  }

  .settings-section h2 {
    color: rgba(255, 255, 255, 0.5);
  }

  .setting-item {
    border-bottom-color: rgba(255, 255, 255, 0.06);
  }

  .setting-info label {
    color: #f0f0f0;
  }

  .setting-description {
    color: rgba(255, 255, 255, 0.5);
  }

  .keybind-input {
    background: rgba(255, 255, 255, 0.08);
    border-color: rgba(255, 255, 255, 0.1);
  }

  .keybind-input:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(255, 255, 255, 0.15);
  }

  .keybind-input:focus {
    background: rgba(204, 120, 92, 0.15);
  }

  .keybind-display {
    color: #f0f0f0;
  }

  .keybind-hint {
    color: rgba(255, 255, 255, 0.4);
  }

  .toggle-slider {
    background: rgba(255, 255, 255, 0.2);
  }

  .toggle-slider:before {
    background: #f0f0f0;
  }

  .about-label {
    color: rgba(255, 255, 255, 0.6);
  }

  .about-value {
    color: #f0f0f0;
  }
}
```

## File: `static/styles/spotlight.css`
```css
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: transparent;
      overflow: hidden;
    }

    .spotlight-container {
      background: rgba(255, 255, 255, 0.05);
      border-radius: 14px;
      box-shadow:
        0 25px 50px -12px rgba(0, 0, 0, 0.2),
        0 0 0 1px rgba(255, 255, 255, 0.2);
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }

    .input-row {
      display: flex;
      align-items: center;
      padding: 12px 16px;
      gap: 12px;
      border-bottom: 1px solid rgba(0, 0, 0, 0.06);
      -webkit-app-region: drag;
    }

    .input-row input,
    .input-row button {
      -webkit-app-region: no-drag;
    }

    .input-row.no-border {
      border-bottom: none;
    }

    .search-icon {
      width: 20px;
      height: 20px;
      opacity: 0.4;
    }

    #spotlight-input {
      flex: 1;
      border: none;
      background: transparent;
      font-size: 18px;
      outline: none;
      color: #1a1a1a;
    }

    #spotlight-input::placeholder {
      color: rgba(0, 0, 0, 0.35);
    }

    .new-chat-btn {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: none;
      background: transparent;
      color: rgba(0, 0, 0, 0.4);
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
      transition: all 0.15s;
    }

    .new-chat-btn.visible {
      display: flex;
    }

    .new-chat-btn:hover {
      background: rgba(0, 0, 0, 0.08);
      color: rgba(0, 0, 0, 0.6);
    }

    .send-btn {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      border: none;
      background: #cc785c;
      color: white;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.15s;
    }

    .send-btn.visible {
      opacity: 1;
    }

    .send-btn:hover {
      background: #b86a50;
    }

    .send-btn:disabled {
      opacity: 0.5;
      cursor: not-allowed;
    }

    .messages-area {
      display: none;
      padding: 12px 16px;
      max-height: 600px;
      overflow-y: auto;
    }

    .messages-area.visible {
      display: block;
    }

    .messages-area::-webkit-scrollbar {
      display: none;
    }

    /* Message bubbles */
    .message {
      margin-bottom: 12px;
    }

    .message:last-child {
      margin-bottom: 0;
    }

    .user-message {
      background: rgba(204, 120, 92, 0.12);
      padding: 10px 14px;
      border-radius: 12px;
      font-size: 14px;
      color: #1a1a1a;
    }

    .ai-message {
      padding: 8px 0;
    }

    .ai-response {
      font-size: 14px;
      line-height: 1.5;
      color: #1a1a1a;
      word-wrap: break-word;
    }

    /* Markdown styles - matching main chat */
    .ai-response p { margin: 0 0 6px 0; }
    .ai-response p:last-child { margin-bottom: 0; }
    .ai-response p:first-child { margin-top: 0; }
    .ai-response h1, .ai-response h2, .ai-response h3 { margin: 10px 0 4px; font-weight: 600; }
    .ai-response h1:first-child, .ai-response h2:first-child, .ai-response h3:first-child { margin-top: 0; }
    .ai-response h1 { font-size: 1.2em; }
    .ai-response h2 { font-size: 1.1em; }
    .ai-response h3 { font-size: 1.05em; }
    .ai-response strong { font-weight: 600; }
    .ai-response code {
      font-family: 'SF Mono', Menlo, monospace;
      font-size: 0.9em;
      background: rgba(0, 0, 0, 0.08);
      padding: 2px 6px;
      border-radius: 4px;
      color: #9a5d3a;
    }
    .ai-response .code-block-wrapper {
      position: relative;
      margin: 8px 0;
    }
    .ai-response .code-copy-btn {
      position: absolute;
      top: 8px;
      right: 8px;
      width: 28px;
      height: 28px;
      border: none;
      border-radius: 6px;
      background: rgba(0, 0, 0, 0.08);
      color: rgba(0, 0, 0, 0.5);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.15s, background 0.15s;
      z-index: 1;
    }
    .ai-response .code-block-wrapper:hover .code-copy-btn {
      opacity: 1;
    }
    .ai-response .code-copy-btn:hover {
      background: rgba(0, 0, 0, 0.15);
      color: rgba(0, 0, 0, 0.7);
    }
    .ai-response .code-copy-btn.copied {
      background: rgba(80, 161, 79, 0.2);
      color: #50a14f;
    }
    .ai-response pre {
      background: rgba(0, 0, 0, 0.05);
      border: 1px solid rgba(0, 0, 0, 0.1);
      border-radius: 10px;
      padding: 12px;
      overflow-x: auto;
      margin: 0;
    }
    .ai-response pre code { background: transparent; padding: 0; font-size: 12px; line-height: 1.5; color: #333; }

    /* Syntax highlighting - Light mode */
    .ai-response pre code.hljs { color: #383a42; }
    .ai-response .hljs-comment,
    .ai-response .hljs-quote { color: #a0a1a7; font-style: italic; }
    .ai-response .hljs-keyword,
    .ai-response .hljs-selector-tag,
    .ai-response .hljs-built_in { color: #a626a4; }
    .ai-response .hljs-string,
    .ai-response .hljs-title.class_,
    .ai-response .hljs-attr { color: #50a14f; }
    .ai-response .hljs-number,
    .ai-response .hljs-literal { color: #986801; }
    .ai-response .hljs-function,
    .ai-response .hljs-title.function_ { color: #4078f2; }
    .ai-response .hljs-variable,
    .ai-response .hljs-template-variable { color: #e45649; }
    .ai-response .hljs-type,
    .ai-response .hljs-class { color: #c18401; }
    .ai-response .hljs-tag { color: #e45649; }
    .ai-response .hljs-name { color: #e45649; }
    .ai-response .hljs-attribute { color: #986801; }
    .ai-response .hljs-regexp,
    .ai-response .hljs-link { color: #0184bc; }
    .ai-response .hljs-symbol,
    .ai-response .hljs-bullet { color: #4078f2; }
    .ai-response .hljs-meta { color: #a0a1a7; }
    .ai-response .hljs-deletion { color: #e45649; background: rgba(228, 86, 73, 0.1); }
    .ai-response .hljs-addition { color: #50a14f; background: rgba(80, 161, 79, 0.1); }
    .ai-response ul, .ai-response ol { margin: 6px 0; padding-left: 20px; }
    .ai-response li { margin: 2px 0; }
    .ai-response blockquote {
      border-left: 3px solid #CC785C;
      margin: 8px 0;
      padding: 6px 12px;
      background: rgba(204, 120, 92, 0.1);
      border-radius: 0 8px 8px 0;
    }
    .ai-response a { color: #9a5d3a; text-decoration: none; }
    .ai-response a:hover { text-decoration: underline; }
    .ai-response hr {
      border: none;
      border-top: 1px solid rgba(0, 0, 0, 0.12);
      margin: 12px 0;
    }

    .loading-dots {
      display: inline-flex;
      gap: 4px;
    }

    .loading-dots span {
      width: 6px;
      height: 6px;
      background: rgba(0, 0, 0, 0.3);
      border-radius: 50%;
      animation: bounce 1.4s infinite ease-in-out both;
    }

    .loading-dots span:nth-child(1) { animation-delay: -0.32s; }
    .loading-dots span:nth-child(2) { animation-delay: -0.16s; }

    @keyframes bounce {
      0%, 80%, 100% { transform: scale(0); }
      40% { transform: scale(1); }
    }

    /* Step items - matching main chat timeline UI */
    .steps-container {
      margin-bottom: 8px;
    }

    .step-item {
      display: flex;
      flex-direction: row;
      min-height: 34px;
    }

    .step-timeline-col {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-left: 4px;
      width: 24px;
      flex-shrink: 0;
    }

    .step-dot-row {
      display: flex;
      flex-direction: column;
      align-items: center;
      height: 34px;
      justify-content: center;
    }

    .step-line-top {
      width: 1px;
      flex: 1;
      background: rgba(0, 0, 0, 0.12);
      min-height: 8px;
    }

    .step-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: rgba(0, 0, 0, 0.12);
      flex-shrink: 0;
      margin: 4px 0;
    }

    .step-item.thinking .step-dot {
      background: #CC785C;
    }

    .step-item.tool .step-dot {
      background: #5856D6;
    }

    .step-line-bottom {
      width: 1px;
      flex: 1;
      background: rgba(0, 0, 0, 0.12);
      min-height: 8px;
    }

    .step-item:first-child .step-line-top {
      background: transparent;
    }

    .step-item:last-child .step-line-bottom {
      background: transparent;
    }

    .step-line-extend {
      width: 1px;
      flex: 1;
      background: rgba(0, 0, 0, 0.12);
      display: none;
    }

    .step-item.expanded .step-line-extend {
      display: block;
    }

    .step-item:last-child .step-line-extend {
      background: transparent;
    }

    .step-content-col {
      flex: 1;
      min-width: 0;
      display: flex;
      flex-direction: column;
    }

    .step-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      padding: 6px 10px 6px 4px;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.15s;
    }

    .step-header:hover {
      background: rgba(0, 0, 0, 0.04);
    }

    .step-label {
      font-size: 13px;
      font-weight: 400;
      color: rgba(0, 0, 0, 0.55);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      flex: 1;
      line-height: 1.4;
    }

    .step-spinner {
      width: 12px;
      height: 12px;
      border: 1.5px solid rgba(0, 0, 0, 0.12);
      border-top-color: rgba(0, 0, 0, 0.5);
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
      flex-shrink: 0;
    }

    .step-chevron {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 16px;
      height: 16px;
      color: rgba(0, 0, 0, 0.35);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      flex-shrink: 0;
    }

    .step-chevron svg {
      width: 16px;
      height: 16px;
    }

    .step-item.expanded .step-chevron {
      transform: rotate(90deg);
    }

    .step-content {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.3s ease, opacity 0.2s;
      opacity: 0;
    }

    .step-item.expanded .step-content {
      max-height: 200px;
      overflow-y: auto;
      opacity: 1;
    }

    .step-content::-webkit-scrollbar {
      display: none;
    }

    .step-text {
      padding: 8px 10px 12px 4px;
      font-size: 12px;
      line-height: 1.6;
      color: rgba(0, 0, 0, 0.5);
      white-space: pre-wrap;
      font-family: 'SF Mono', Menlo, monospace;
    }

    @keyframes spin {
      to { transform: rotate(360deg); }
    }

    /* Dark mode */
    @media (prefers-color-scheme: dark) {
      .spotlight-container {
        background: rgba(0, 0, 0, 0.05);
        box-shadow:
          0 25px 50px -12px rgba(0, 0, 0, 0.4),
          0 0 0 1px rgba(255, 255, 255, 0.1);
      }

      .input-row {
        border-bottom-color: rgba(255, 255, 255, 0.08);
      }

      #spotlight-input {
        color: #f0f0f0;
      }

      #spotlight-input::placeholder {
        color: rgba(255, 255, 255, 0.35);
      }

      .search-icon {
        filter: invert(1);
      }

      .new-chat-btn {
        color: rgba(255, 255, 255, 0.4);
      }

      .new-chat-btn:hover {
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.7);
      }

      .user-message {
        background: rgba(204, 120, 92, 0.2);
        color: #f0f0f0;
      }

      .ai-response {
        color: #e0e0e0;
      }
      .ai-response code { background: rgba(0, 0, 0, 0.3); color: #E8C4A0; }
      .ai-response pre { background: rgba(0, 0, 0, 0.4); border-color: rgba(255, 255, 255, 0.1); }
      .ai-response pre code { color: rgba(255, 255, 255, 0.9); }
      .ai-response a { color: #E8C4A0; }
      .ai-response .code-copy-btn {
        background: rgba(255, 255, 255, 0.1);
        color: rgba(255, 255, 255, 0.5);
      }
      .ai-response .code-copy-btn:hover {
        background: rgba(255, 255, 255, 0.2);
        color: rgba(255, 255, 255, 0.8);
      }
      .ai-response .code-copy-btn.copied {
        background: rgba(152, 195, 121, 0.25);
        color: #98c379;
      }

      /* Syntax highlighting - Dark mode */
      .ai-response pre code.hljs { color: #abb2bf; }
      .ai-response .hljs-comment,
      .ai-response .hljs-quote { color: #5c6370; font-style: italic; }
      .ai-response .hljs-keyword,
      .ai-response .hljs-selector-tag,
      .ai-response .hljs-built_in { color: #c678dd; }
      .ai-response .hljs-string,
      .ai-response .hljs-title.class_,
      .ai-response .hljs-attr { color: #98c379; }
      .ai-response .hljs-number,
      .ai-response .hljs-literal { color: #d19a66; }
      .ai-response .hljs-function,
      .ai-response .hljs-title.function_ { color: #61afef; }
      .ai-response .hljs-variable,
      .ai-response .hljs-template-variable { color: #e06c75; }
      .ai-response .hljs-type,
      .ai-response .hljs-class { color: #e5c07b; }
      .ai-response .hljs-tag { color: #e06c75; }
      .ai-response .hljs-name { color: #e06c75; }
      .ai-response .hljs-attribute { color: #d19a66; }
      .ai-response .hljs-regexp,
      .ai-response .hljs-link { color: #56b6c2; }
      .ai-response .hljs-symbol,
      .ai-response .hljs-bullet { color: #61afef; }
      .ai-response .hljs-meta { color: #5c6370; }
      .ai-response .hljs-deletion { color: #e06c75; background: rgba(224, 108, 117, 0.15); }
      .ai-response .hljs-addition { color: #98c379; background: rgba(152, 195, 121, 0.15); }
      .ai-response hr { border-top-color: rgba(255, 255, 255, 0.15); }

      .loading-dots span {
        background: rgba(255, 255, 255, 0.4);
      }

      .step-line-top, .step-line-bottom, .step-line-extend {
        background: rgba(255, 255, 255, 0.15);
      }

      .step-item:first-child .step-line-top,
      .step-item:last-child .step-line-bottom,
      .step-item:last-child .step-line-extend {
        background: transparent;
      }

      .step-dot {
        background: rgba(255, 255, 255, 0.2);
      }

      .step-header:hover {
        background: rgba(255, 255, 255, 0.06);
      }

      .step-label {
        color: rgba(255, 255, 255, 0.6);
      }

      .step-chevron {
        color: rgba(255, 255, 255, 0.6);
      }

      .step-text {
        color: rgba(255, 255, 255, 0.5);
      }

      .step-spinner {
        border-color: rgba(255, 255, 255, 0.15);
        border-top-color: rgba(255, 255, 255, 0.5);
      }
    }
```


---
id: trans
type: knowledge
owner: OA_Triage
---
# trans
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "translation-tool",
  "version": "1.0.0",
  "description": "Translation tool from English to Vietnamese using GPT",
  "type": "module",
  "scripts": {
    "dev": "vite dev",
    "build": "vite build",
    "preview": "vite preview",
    "electron": "electron .",
    "electron:dev": "concurrently -k \"npm run dev\" \"wait-on http://localhost:5173 && electron .\"",
    "electron:build": "rm -rf dist && npm run build && electron-builder"
  },
  "devDependencies": {
    "@rgossiaux/svelte-headlessui": "^2.0.0",
    "@sveltejs/vite-plugin-svelte": "^3.1.2",
    "@types/node": "^20.10.0",
    "concurrently": "^8.2.2",
    "electron": "^28.0.0",
    "electron-builder": "^24.9.1",
    "sharp": "^0.34.5",
    "svelte": "^4.2.0",
    "vite": "^5.0.0",
    "wait-on": "^7.2.0"
  },
  "dependencies": {
    "electron-store": "^8.1.0",
    "openai": "^4.20.0"
  },
  "main": "electron/main.js",
  "build": {
    "appId": "com.translation.tool",
    "productName": "Translation Tool",
    "icon": "assets/translate_faster.png",
    "mac": {
      "category": "public.app-category.utilities",
      "target": "dmg",
      "icon": "assets/translate_faster.png"
    },
    "win": {
      "icon": "assets/translate_faster.png"
    },
    "linux": {
      "icon": "assets/translate_faster.png"
    },
    "files": [
      "dist/**/*",
      "electron/**/*",
      "assets/**/*",
      "node_modules/**/*",
      "package.json"
    ]
  }
}

```

### File: README.md
```md
# Translation Tool

Công cụ dịch tiếng Anh sang tiếng Việt sử dụng GPT, với hỗ trợ phím tắt trên macOS.

## Tính năng

- 🌐 Dịch tiếng Anh sang tiếng Việt bằng GPT-3.5-turbo
- ⌨️ Phím tắt toàn cục (Cmd+Shift+T) để dịch text đã chọn
- 💾 Lưu trữ API key an toàn
- 🎨 Giao diện đẹp và dễ sử dụng

## Cài đặt

1. Cài đặt dependencies:
```bash
npm install
```

2. Cấu hình OpenAI API key:
   - Mở app và click vào nút "Settings" (⚙️)
   - Nhập OpenAI API key của bạn
   - Lấy API key tại: https://platform.openai.com/api-keys

## Sử dụng

### Development

Chạy app trong chế độ development:
```bash
npm run electron:dev
```

### Production Build

Build app để tạo file .dmg:
```bash
npm run build:electron
```

## Cách sử dụng phím tắt

### Trên macOS:

**Cách 1: Tự động copy (yêu cầu quyền Accessibility)**
1. Cấp quyền Accessibility cho Terminal hoặc Electron:
   - Mở System Settings > Privacy & Security > Accessibility
   - Thêm Terminal (nếu chạy từ terminal) hoặc Translation Tool app
   - Đảm bảo checkbox được bật
2. Chọn (bôi đen) text tiếng Anh trong bất kỳ ứng dụng nào
3. Nhấn `Cmd+Shift+T`
4. App sẽ tự động copy và dịch text

**Cách 2: Manual copy (không cần quyền)**
1. Chọn (bôi đen) text tiếng Anh
2. Nhấn `Cmd+C` để copy
3. Nhấn `Cmd+Shift+T` để dịch

### Trên Windows/Linux:
1. Chọn text và nhấn `Ctrl+C` để copy
2. Nhấn `Ctrl+Shift+T` để dịch

## Cấu trúc dự án

```
trans/
├── electron/          # Electron main process
│   ├── main.js       # Main Electron process
│   └── preload.js    # Preload script
├── src/              # Svelte source code
│   ├── components/   # Svelte components
│   ├── services/     # Business logic
│   └── App.svelte    # Main app component
└── package.json
```

## Lưu ý

- Cần có OpenAI API key để sử dụng
- Phím tắt chỉ hoạt động khi app đang chạy
- Trên macOS, app sẽ tự động copy text đã chọn khi nhấn phím tắt


```

### File: .vite\deps_temp_16b700f6\package.json
```json
{
  "type": "module"
}

```

### File: electron\clipboard\index.js
```js
export { checkAccessibilityPermission } from './accessibility.js';
export { getSelectedText } from './selection.js';


```

### File: electron\ipc\index.js
```js
export {
  setupShortcutHandlers,
  setupDialogHandlers,
  setupAPIHandlers,
  setupTestHandlers,
  setupAllHandlers
} from './handlers.js';


```

### File: electron\openai\index.js
```js
export { initializeOpenAI, getClient, createClient } from './client.js';
export { translateText } from './translation.js';


```

### File: electron\state\index.js
```js
// Global state management
export let mainWindow = null;
export let dialogWindow = null;
export let openaiClient = null;
export let isFirstResize = true;
export let tray = null;

export function setMainWindow(window) {
  mainWindow = window;
}

export function getMainWindow() {
  return mainWindow;
}

export function setDialogWindow(window) {
  dialogWindow = window;
}

export function getDialogWindow() {
  return dialogWindow;
}

export function setOpenAIClient(client) {
  openaiClient = client;
}

export function getOpenAIClient() {
  return openaiClient;
}

export function setIsFirstResize(value) {
  isFirstResize = value;
}

export function getIsFirstResize() {
  return isFirstResize;
}

export function setTray(trayInstance) {
  tray = trayInstance;
}

export function getTray() {
  return tray;
}


```

### File: electron\windows\index.js
```js
export { createWindow } from './mainWindow.js';
export { createDialogWindow } from './dialogWindow.js';


```

### File: dialog.html
```html
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dialog</title>
</head>
<body>
  <div id="dialog-app"></div>
  <script type="module" src="/src/dialog.js"></script>
</body>
</html>
```

### File: index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Translation Tool</title>
</head>
<body class="main">
  <div id="app"></div>
  <script type="module" src="/src/main.js"></script>
</body>
</html>


```

### File: svelte.config.js
```js
import { vitePreprocess, svelte } from '@sveltejs/vite-plugin-svelte';

export default {
  preprocess: vitePreprocess(),
  plugins: [svelte()]
};


```

### File: vite.config.js
```js
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';
import { readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';

export default defineConfig({
  plugins: [
    svelte(),
    {
      name: 'fix-asset-paths',
      closeBundle() {
        // Fix absolute paths in HTML files to relative paths
        const htmlFiles = ['index.html', 'dialog.html'];
        
        htmlFiles.forEach(fileName => {
          try {
            const filePath = resolve(__dirname, 'dist', fileName);
            let content = readFileSync(filePath, 'utf-8');
            // Replace /assets/ with ./assets/
            content = content.replace(/src="\/assets\//g, 'src="./assets/');
            content = content.replace(/href="\/assets\//g, 'href="./assets/');
            writeFileSync(filePath, content, 'utf-8');
            console.log(`✅ Fixed asset paths in ${fileName}`);
          } catch (err) {
            console.warn(`⚠️ Could not fix asset paths in ${fileName}:`, err.message);
          }
        });
      }
    }
  ],
  server: {
    port: 5173
  },
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        dialog: resolve(__dirname, 'dialog.html')
      },
      output: {
        // Ensure assets use relative paths
        assetFileNames: 'assets/[name].[ext]',
        entryFileNames: 'assets/[name].js',
        chunkFileNames: 'assets/[name].js'
      }
    },
    // Use relative paths for assets so they work when loaded from file:// protocol
    base: './',
    // Ensure absolute paths are converted to relative
    assetsInlineLimit: 0
  }
});


```

### File: electron\main.js
```js
import { app, BrowserWindow, globalShortcut, nativeImage } from 'electron';
import path from 'path';
import { fileURLToPath } from 'url';
import { existsSync } from 'fs';
import { createWindow } from './windows/index.js';
import { initializeOpenAI } from './openai/index.js';
import { checkAccessibilityPermission } from './clipboard/index.js';
import { registerShortcut, registerDialogShortcut } from './shortcuts/index.js';
import { setupAllHandlers } from './ipc/index.js';
import { getMainWindow, setTray } from './state/index.js';
import { createTray } from './tray/index.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.whenReady().then(async () => {
  let iconPath = path.join(__dirname, '..', 'assets', 'translate_faster.png');
  if (!existsSync(iconPath)) {
    iconPath = path.join(__dirname, '..', 'assets', 'translate_faster.svg');
  }
  
  const appIcon = nativeImage.createFromPath(iconPath);
  if (!appIcon.isEmpty() && process.platform === 'darwin') {
    app.dock?.setIcon(appIcon); 
    console.log('✓ Set app icon for dock');
  } else {
    console.warn('⚠ App icon not found or empty:', iconPath);
  }
  
  createWindow();
  initializeOpenAI();
  
  if (process.platform === 'darwin') {
    const hasPermission = await checkAccessibilityPermission();
    if (!hasPermission) {
      console.warn('⚠️ Accessibility permission may be required for automatic text selection');
      console.warn('Go to: System Settings > Privacy & Security > Accessibility');
    }
  }
  
  const shortcutStatus = registerShortcut();
  registerDialogShortcut();
  setupAllHandlers();
  
  const tray = createTray();
  setTray(tray);
  
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
      registerShortcut();
    }
  });
  
  const mainWindow = getMainWindow();
  if (mainWindow && !mainWindow.isDestroyed()) {
    mainWindow.webContents.once('did-finish-load', () => {
      mainWindow.webContents.send('shortcut-status', shortcutStatus);
    });
  }
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('will-quit', () => {
  globalShortcut.unregisterAll();
});

```

### File: src\app.css
```css
:root {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  line-height: 1.5;
  font-weight: 400;
  color: #213547;
  background-color: transparent;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body, html {
  background: transparent;
}

/* Only the main app window paints a solid background */
body.main {
  background-color: #1a1a1a;
  margin: 0;
  min-width: 320px;
  min-height: 100vh;
  color: #ffffff;
}

body.dialog-app {
  width: min(720px, 92vw);
}

#app {
  width: 100%;
  height: 100vh;
  margin: 0;
  padding: 0;
}

/* Make main content not paint solid white */
textarea {
  background: transparent;
}

textarea[readonly] {
  background-color: transparent;
}


```

### File: src\dialog.js
```js
import DialogWindow from './components/DialogWindow.svelte';

const target = document.getElementById('dialog-app');

if (!target) {
  console.error('Dialog app target element not found!');
  throw new Error('Dialog app target element not found!');
}

const app = new DialogWindow({
  target: target
});

export default app;
```

### File: src\main.js
```js
import App from './App.svelte';
import './app.css';

const target = document.getElementById('app');

if (!target) {
  console.error('App target element not found!');
  throw new Error('App target element not found!');
}

const app = new App({
  target: target
});

export default app;


```

### File: electron\clipboard\accessibility.js
```js
import { exec } from 'child_process';

export function checkAccessibilityPermission() {
  return new Promise((resolve) => {
    if (process.platform !== 'darwin') {
      resolve(true);
      return;
    }
    
    const script = `
      tell application "System Events"
        try
          set frontApp to name of first application process whose frontmost is true
          return frontApp
        on error
          return "ERROR"
        end try
      end tell
    `;
    
    exec(`osascript -e '${script}'`, (error, stdout) => {
      if (error || stdout.trim() === 'ERROR') {
        console.warn('Accessibility permission may not be granted');
        resolve(false);
      } else {
        resolve(true);
      }
    });
  });
}


```

### File: electron\clipboard\selection.js
```js
import { clipboard } from 'electron';
import { exec } from 'child_process';

export function getSelectedText() {
  return new Promise((resolve) => {
    if (process.platform === 'darwin') {
      const previousClipboard = clipboard.readText();
      console.log('Previous clipboard:', previousClipboard ? previousClipboard.substring(0, 30) + '...' : '(empty)');
      
      const copyScript = `
        tell application "System Events"
          keystroke "c" using command down
        end tell
      `;
      
      console.log('Executing AppleScript to copy selected text...');
      exec(`osascript -e '${copyScript}'`, (error, stdout, stderr) => {
        if (error) {
          console.error('❌ AppleScript error:', error.message);
          console.error('stderr:', stderr);
          
          if (stderr && (stderr.includes('not allowed') || stderr.includes('denied'))) {
            console.error('⚠️ Accessibility permission required!');
            console.error('Please grant permission in: System Settings > Privacy & Security > Accessibility');
          }
        }
        
        let attempts = 0;
        const maxAttempts = 6;
        const checkClipboard = () => {
          attempts++;
          const newClipboard = clipboard.readText();
          
          if (newClipboard && newClipboard !== previousClipboard) {
            console.log(`✅ Clipboard updated on attempt ${attempts}!`);
            resolve(newClipboard);
            return;
          }
          
          if (attempts < maxAttempts) {
            const delay = 100 + (attempts * 50);
            setTimeout(checkClipboard, delay);
          } else {
            if (newClipboard && newClipboard.trim()) {
              console.log('⚠️ Using clipboard content (may not be newly selected text)');
              resolve(newClipboard);
            } else {
              console.log('❌ No text found in clipboard');
              resolve('');
            }
          }
        };
        
        setTimeout(checkClipboard, 100);
      });
    } else {
      const text = clipboard.readText();
      resolve(text || '');
    }
  });
}


```

### File: electron\config\store.js
```js
import Store from 'electron-store';

const store = new Store();

export default store;


```

### File: electron\ipc\handlers.js
```js
import { ipcMain, globalShortcut, screen, BrowserWindow } from 'electron';
import store from '../config/store.js';
import { getMainWindow, getDialogWindow, setDialogWindow, getIsFirstResize, setIsFirstResize } from '../state/index.js';
import { registerShortcut } from '../shortcuts/index.js';
import { translateText } from '../openai/index.js';
import { createClient } from '../openai/client.js';
import { exec } from 'child_process';

export function setupShortcutHandlers() {
  ipcMain.on('update-shortcut', (event, newShortcut) => {
    const status = registerShortcut(newShortcut);
    const mainWindow = getMainWindow();
    if (mainWindow && !mainWindow.isDestroyed()) {
      mainWindow.webContents.send('shortcut-status', status);
    }
  });

  ipcMain.handle('get-shortcut-status', () => {
    const shortcut = store.get('custom_shortcut') || 'CommandOrControl+Shift+T';
    const readable = shortcut
      .replace('CommandOrControl', 'Cmd/Ctrl')
      .replace('Command', 'Cmd')
      .replace('Control', 'Ctrl')
      .replace(/\+/g, '+');
    return readable;
  });

  ipcMain.handle('get-shortcut-raw', () => {
    return store.get('custom_shortcut') || 'CommandOrControl+Shift+T';
  });

  ipcMain.handle('set-shortcut', async (event, shortcut) => {
    console.log('Setting new shortcut:', shortcut);
    
    globalShortcut.unregisterAll();
    
    const ret = globalShortcut.register(shortcut, () => {
      console.log('Test shortcut triggered');
    });
    
    if (!ret) {
      console.error('❌ Cannot register shortcut:', shortcut);
      console.error('💡 This shortcut may be already used by:');
      console.error('   - System shortcuts (like Cmd+T for new tab in browsers)');
      console.error('   - Other applications');
      console.error('   - macOS system shortcuts');
      
      globalShortcut.unregisterAll();
      
      throw new Error(`Không thể đăng ký phím tắt "${shortcut}". Có thể đã bị trùng với phím tắt hệ thống hoặc ứng dụng khác. Hãy thử phím tắt khác như Cmd+Shift+V hoặc Cmd+Option+T.`);
    }
    
    globalShortcut.unregisterAll();
    
    store.set('custom_shortcut', shortcut);
    console.log('✅ Shortcut saved to store:', shortcut);
    
    const status = registerShortcut(shortcut);
    console.log('✅ Shortcut registered with handler:', status);
    
    return true;
  });
}

export function setupDialogHandlers() {
  ipcMain.on('renderer-log', (event, level, ...args) => {
    const message = args.map(arg => 
      typeof arg === 'object' ? JSON.stringify(arg, null, 2) : String(arg)
    ).join(' ');
    
    switch (level) {
      case 'error':
        console.error(`[Renderer] ${message}`);
        break;
      case 'warn':
        console.warn(`[Renderer] ${message}`);
        break;
      default:
        console.log(`[Renderer] ${message}`);
    }
  });

  ipcMain.handle('close-dialog-window', () => {
    const dialogWindow = getDialogWindow();
    if (dialogWindow && !dialogWindow.isDestroyed()) {
      dialogWindow.hide();
    }
    return true;
  });

  ipcMain.handle('resize-dialog-window', (event, height) => {
    let dialogWindow = getDialogWindow();
    
    if (!dialogWindow && event.sender) {
      const senderWindow = BrowserWindow.fromWebContents(event.sender);
      if (senderWindow && !senderWindow.isDestroyed()) {
        const mainWindow = getMainWindow();
        if (senderWindow !== mainWindow) {
          dialogWindow = senderWindow;
          console.log('[Main] Found dialog window from event sender');
        }
      }
    }
    
    if (!dialogWindow) {
      const allWindows = BrowserWindow.getAllWindows();
      const mainWindow = getMainWindow();
      for (const win of allWindows) {
        if (win !== mainWindow && !win.isDestroyed()) {
          const [width, winHeight] = win.getSize();
          if (width <= 900 && winHeight <= 600) {
            dialogWindow = win;
            setDialogWindow(win);
            break;
          }
        }
      }
    }
    
    if (!dialogWindow) {
      console.error('[Main] ❌ dialogWindow is null! Trying to get from state or windows...');
      console.error('[Main] All windows:', BrowserWindow.getAllWindows().map(w => ({
        id: w.id,
        visible: w.isVisible(),
        destroyed: w.isDestroyed()
      })));
      return false;
    }
    
    if (dialogWindow.isDestroyed()) {
      console.error('[Main] ❌ dialogWindow is destroyed!');
      return false;
    }
    
    if (height <= 0) {
      console.warn(`[Main] ⚠️ Invalid height: ${height}`);
      return false;
    }
    
    try {
      const [currentWidth, currentHeight] = dialogWindow.getSize();
      const newHeight = Math.ceil(height) + 10;
      
      const wasResizable = dialogWindow.isResizable();
      if (!wasResizable) {
        console.log('[Main] Temporarily enabling resizable...');
        dialogWindow.setResizable(true);
      }
      
      if (getIsFirstResize()) {
        setIsFirstResize(false);
        console.log('[Main] First resize - setting size and showing window');
        dialogWindow.setSize(currentWidth, newHeight, false);
        
        if (!dialogWindow.isVisible()) {
          dialogWindow.show();
          dialogWindow.focus();
          dialogWindow.setAlwaysOnTop(true, 'screen-saver');
        }
      } else {
        console.log('[Main] Subsequent resize - setting size only');
        dialogWindow.setSize(currentWidth, newHeight, false);
      }
      
      // Restore resizable state
      if (!wasResizable) {
        dialogWindow.setResizable(false);
        console.log('[Main] Resizable disabled again');
      }
      
      // Verify size was actually set
      const [actualWidth, actualHeight] = dialogWindow.getSize();
      console.log(`[Main] ✅ Size after setSize: ${actualWidth}x${actualHeight}`);
      
      if (actualHeight !== newHeight) {
        console.error(`[Main] ❌ Size mismatch! Expected: ${newHeight}, Got: ${actualHeight}`);
      }
      
      return true;
    } catch (error) {
      console.error('[Main] ❌ Error resizing window:', error);
      return false;
    }
  });

  ipcMain.handle('set-dialog-window-position', (event, x, y) => {
    const dialogWindow = getDialogWindow();
    if (dialogWindow && !dialogWindow.isDestroyed()) {
      dialogWindow.setPosition(x, y);
    }
    return true;
  });

  ipcMain.handle('get-screen-size', () => {
    const cursorPoint = screen.getCursorScreenPoint();
    const currentDisplay = screen.getDisplayNearestPoint(cursorPoint);
    const { width, height } = currentDisplay.workAreaSize;
    return { width, height };
  });
}

export function setupAPIHandlers() {
  ipcMain.handle('set-api-key', async (event, key) => {
    store.set('openai_api_key', key);
    createClient(key);
    return true;
  });

  ipcMain.handle('get-api-key', () => {
    return store.get('openai_api_key') || null;
  });

  ipcMain.handle('translate-text', async (event, text) => {
    try {
      return await translateText(text);
    } catch (error) {
      console.error('Translation error:', error);
      throw new Error(error.message || 'Lỗi khi dịch');
    }
  });
}

export function setupTestHandlers() {
  ipcMain.handle('test-applescript', async () => {
    return new Promise((resolve) => {
      if (process.platform !== 'darwin') {
        resolve({ success: false, message: 'Only available on macOS' });
        return;
      }
      
      const script = `
        tell application "System Events"
          try
            keystroke "c" using command down
            return "SUCCESS"
          on error errMsg
            return "ERROR: " & errMsg
          end try
        end tell
      `;
      
      exec(`osascript -e '${script}'`, { timeout: 2000 }, (error, stdout, stderr) => {
        if (error) {
          resolve({ 
            success: false, 
            message: error.message,
            stderr: stderr,
            hasPermission: !stderr || !stderr.includes('not allowed')
          });
        } else {
          resolve({ 
            success: true, 
            message: 'AppleScript executed successfully',
            stdout: stdout
          });
        }
      });
    });
  });
}

export function setupAllHandlers() {
  setupShortcutHandlers();
  setupDialogHandlers();
  setupAPIHandlers();
  setupTestHandlers();
}


```

### File: electron\openai\client.js
```js
import { OpenAI } from 'openai';
import store from '../config/store.js';
import { getOpenAIClient, setOpenAIClient } from '../state/index.js';

export function initializeOpenAI() {
  const apiKey = store.get('openai_api_key');
  if (apiKey) {
    const client = new OpenAI({ apiKey });
    setOpenAIClient(client);
  }
}

export function getClient() {
  let client = getOpenAIClient();
  if (!client) {
    const apiKey = store.get('openai_api_key');
    if (apiKey) {
      client = new OpenAI({ apiKey });
      setOpenAIClient(client);
    }
  }
  return client;
}

export function createClient(apiKey) {
  const client = new OpenAI({ apiKey });
  setOpenAIClient(client);
  return client;
}


```

### File: electron\openai\translation.js
```js
import { getClient } from './client.js';
import store from '../config/store.js';

export async function translateText(text) {
  let client = getClient();
  
  if (!client) {
    const apiKey = store.get('openai_api_key');
    if (!apiKey) {
      throw new Error('OpenAI API key chưa được cấu hình');
    }
    client = getClient();
    if (!client) {
      throw new Error('Không thể khởi tạo OpenAI client');
    }
  }
  
  const prompt = `Translate the following English text to Vietnamese. Only provide the translation, no explanations or additional text:\n\n${text}`;
  
  const response = await client.chat.completions.create({
    model: 'gpt-3.5-turbo',
    messages: [
      {
        role: 'system',
        content: 'You are a professional translator. Translate English to Vietnamese accurately and naturally.'
      },
      {
        role: 'user',
        content: prompt
      }
    ],
    temperature: 0.3,
    max_tokens: 1000
  });
  
  return response.choices[0]?.message?.content?.trim() || 'Không thể dịch được';
}


```

### File: electron\windows\dialogWindow.js
```js
import { BrowserWindow, screen, app } from 'electron';
import path from 'path';
import { fileURLToPath } from 'url';
import { getDialogWindow, setDialogWindow, setIsFirstResize } from '../state/index.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

function calculateDialogPosition() {
  const cursorPoint = screen.getCursorScreenPoint();
  const currentDisplay = screen.getDisplayNearestPoint(cursorPoint);
  const screenWidth = currentDisplay.workAreaSize.width;
  const screenHeight = currentDisplay.workAreaSize.height;
  const screenX = currentDisplay.workArea.x;
  const screenY = currentDisplay.workArea.y;
  const dialogWidth = 720;
  const x = screenX + Math.floor((screenWidth - dialogWidth) / 2);
  const y = screenY + Math.floor(screenHeight * 0.15);
  return { x, y };
}

export function createDialogWindow() {
  const existingDialog = getDialogWindow();
  if (existingDialog && !existingDialog.isDestroyed()) {
    const { x, y } = calculateDialogPosition();
    existingDialog.setPosition(x, y);
    existingDialog.show();
    existingDialog.focus();
    return existingDialog;
  }

  setIsFirstResize(true);
  const isDev = !app.isPackaged;
  const { x, y } = calculateDialogPosition();
  
  const dialogWindow = new BrowserWindow({
    width: 720,
    minWidth: 400,
    maxWidth: 900,
    height: 100, 
    minHeight: 100,
    frame: false,
    transparent: true,
    alwaysOnTop: true,
    skipTaskbar: true,
    resizable: false, 
    fullscreenable: false,
    movable: false,
    focusable: true,
    hasShadow: true,
    parent: null, 
    modal: false,
    visualEffectState: 'active',
    vibrancy: 'popover',
    x: x,
    y: y,
    show: false,
    webPreferences: {
      preload: path.join(__dirname, '..', 'preload.cjs'),
      nodeIntegration: false,
      contextIsolation: true,
      backgroundThrottling: false
    },
    backgroundColor: '#00000000'
  });

  dialogWindow.show();
  dialogWindow.focus();

  try {
    dialogWindow.setVisibleOnAllWorkspaces(true, { visibleOnFullScreen: true });
    dialogWindow.setAlwaysOnTop(true, 'screen-saver');
  } catch (e) {
    console.warn('Failed to elevate dialog window level:', e.message);
  }

  if (isDev) {
    dialogWindow.loadURL('http://localhost:5173/dialog.html').catch(err => {
      console.error('Failed to load dialog URL:', err);
    });
  } else {
    const appPath = app.getAppPath();
    const dialogPath = path.join(appPath, 'dist', 'dialog.html');
    dialogWindow.loadFile(dialogPath).catch(err => {
      console.error('Failed to load dialog file:', err);
    });
  }

  let blurTimeout;
  dialogWindow.on('blur', () => {
    if (blurTimeout) {
      clearTimeout(blurTimeout);
    }
    
    blurTimeout = setTimeout(() => {
      if (dialogWindow && !dialogWindow.isDestroyed()) {
        console.log('[DialogWindow] Blur timeout - hiding window');
        dialogWindow.hide();
      }
    }, 300); 
  });
  
  dialogWindow.on('focus', () => {
    if (blurTimeout) {
      clearTimeout(blurTimeout);
      blurTimeout = null;
    }
  });

  dialogWindow.on('closed', () => {
    setDialogWindow(null);
  });

  setDialogWindow(dialogWindow);
  return dialogWindow;
}


```

### File: electron\windows\mainWindow.js
```js
import { BrowserWindow, nativeImage } from 'electron';
import path from 'path';
import { fileURLToPath } from 'url';
import { existsSync } from 'fs';
import { app } from 'electron';
import { setMainWindow } from '../state/index.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export function createWindow() {
  let iconPath = path.join(__dirname, '..', '..', 'assets', 'translate_faster.png');
  if (!existsSync(iconPath)) {
    iconPath = path.join(__dirname, '..', '..', 'assets', 'translate_faster.svg');
  }
  const appIcon = nativeImage.createFromPath(iconPath);
  
  const mainWindow = new BrowserWindow({
    width: 900,
    height: 700,
    transparent: true,
    icon: !appIcon.isEmpty() ? appIcon : undefined, 
    webPreferences: {
      preload: path.join(__dirname, '..', 'preload.cjs'),
      nodeIntegration: false,
      contextIsolation: true
    },
    titleBarStyle: 'hiddenInset',
    backgroundColor: '#00000000',
    vibrancy: 'window',
    visualEffectState: 'active',
  });

  const isDev = !app.isPackaged;
  
  if (isDev) {
    const loadDevURL = () => {
      console.log('Loading from http://localhost:5173');
      mainWindow.loadURL('http://localhost:5173').catch(err => {
        console.error('Failed to load URL:', err);
      });
    };
    
    setTimeout(loadDevURL, 500);
    
    // Only open DevTools in development
    mainWindow.webContents.openDevTools();
    
    // Handle dev server not ready
    mainWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription, validatedURL) => {
      console.log('Failed to load:', errorCode, errorDescription, validatedURL);
      if (errorCode === -106 || errorCode === -105) {
        console.log('Retrying in 2 seconds...');
        setTimeout(loadDevURL, 2000);
      }
    });
    
    mainWindow.webContents.on('did-finish-load', () => {
      console.log('App loaded successfully');
    });
  } else {
    const appPath = app.getAppPath();
    console.log('Production mode - App path:', appPath);
    console.log('Resources path:', process.resourcesPath);
    console.log('__dirname:', __dirname);
    
    const possiblePaths = [
      path.join(appPath, 'dist', 'index.html'), // Normal asar path (most common)
      path.join(__dirname, '..', '..', 'dist', 'index.html'), // Relative to electron folder
      path.join(process.resourcesPath, 'app.asar', 'dist', 'index.html'), // Direct asar path
      path.join(process.resourcesPath, 'app', 'dist', 'index.html'), // Unpacked path
    ];
    
    const tryLoadPath = async (index) => {
      if (index >= possiblePaths.length) {
        return;
      }
      
      const distPath = possiblePaths[index];
      
      try {
        await mainWindow.loadFile(distPath);
      } catch (err) {
        try {
          const fileUrl = distPath.startsWith('file://') ? distPath : `file://${distPath}`;
          await mainWindow.loadURL(fileUrl);
          console.log(`✅ Successfully loaded via URL: ${distPath}`);
        } catch (err2) {
          tryLoadPath(index + 1);
        }
      }
    };
    
    tryLoadPath(0);
  }

  setMainWindow(mainWindow);
  return mainWindow;
}


```

### File: src\services\translation.js
```js
class TranslationService {
  constructor() {
    this.apiKey = null;
    this.baseURL = 'https://api.openai.com/v1';
  }
  
  async setApiKey(key) {
    this.apiKey = key;
    if (typeof window !== 'undefined') {
      localStorage.setItem('openai_api_key', key);
    }
    if (window.electronAPI) {
      await window.electronAPI.setApiKey(key);
    }
  }
  
  async getApiKey() {
    if (this.apiKey) {
      return this.apiKey;
    }
    
    if (typeof window !== 'undefined') {
      const stored = localStorage.getItem('openai_api_key');
      if (stored) {
        this.apiKey = stored;
        return stored;
      }
    }
    
    if (window.electronAPI) {
      try {
        const key = await window.electronAPI.getApiKey();
        if (key) {
          this.apiKey = key;
          return key;
        }
      } catch (err) {
        console.error('Error getting API key from Electron:', err);
      }
    }
    
    return null;
  }
  
  async translate(text) {
    const apiKey = await this.getApiKey();
    
    if (!apiKey) {
      throw new Error('Please configure OpenAI API key in Settings');
    }
    
    const prompt = `Translate the following English text to Vietnamese. Only provide the translation, no explanations or additional text:\n\n${text}`;
    
    try {
      if (window.electronAPI) {
        try {
          const result = await window.electronAPI.translateText(text);
          return result;
        } catch (err) {
          console.error('Electron translation failed, falling back to direct API:', err);
        }
      }
      
      const response = await fetch(`${this.baseURL}/chat/completions`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
          model: 'gpt-3.5-turbo',
          messages: [
            {
              role: 'system',
              content: 'You are a professional translator. Translate English to Vietnamese accurately and naturally.'
            },
            {
              role: 'user',
              content: prompt
            }
          ],
          temperature: 0.3,
          max_tokens: 1000
        })
      });
      
      if (!response.ok) {
        const error = await response.json().catch(() => ({ error: { message: 'Unknown error' } }));
        throw new Error(error.error?.message || `HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return data.choices[0]?.message?.content?.trim() || 'Unable to translate';
      
    } catch (error) {
      if (error.message.includes('API key')) {
        throw error;
      }
      throw new Error(`Translation error: ${error.message}`);
    }
  }
}

export default TranslationService;


```


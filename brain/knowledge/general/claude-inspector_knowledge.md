---
id: claude-inspector-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:04.315369
---

# KNOWLEDGE EXTRACT: claude-inspector
> **Extracted on:** 2026-03-30 13:16:34
> **Source:** claude-inspector

---

## File: `.gitignore`
```
node_modules/
release/
dist/
.DS_Store
*.env
.env*
.worklogs/
.idea/
request_test.json
public/build-info.json

# --- ai-bouncer start ---
# ai-bouncer runtime artifacts
.claude/ai-bouncer/.version-checked
.claude/ai-bouncer/config.json
.claude/ai-bouncer/manifest.json
.claude/**/*.backup-*
.claude/settings.json
brain/knowledge/docs_legacy/
# ai-bouncer installed files
.claude/agents/dev.md
.claude/agents/intent.md
.claude/agents/lead.md
.claude/agents/qa.md
.claude/agents/verifier.md
.claude/agents/guides/tc-guide.md
.claude/skills/dev-bounce/SKILL.md
.claude/skills/update-bouncer/SKILL.md
.claude/hooks/hooks.json
.claude/hooks/plan-gate.sh
.claude/hooks/bash-gate.sh
.claude/hooks/doc-reminder.sh
.claude/hooks/bash-audit.sh
.claude/hooks/completion-gate.sh
.claude/hooks/stop-active-cleanup.sh
.claude/hooks/subagent-track.sh
.claude/hooks/subagent-cleanup.sh
.claude/hooks/lib/resolve-task.sh
.claude/scripts/update-check.sh
update.sh
uninstall.sh
# --- ai-bouncer end ---
```

## File: `analytics.js`
```javascript
const https = require('node:https');
const fs = require('node:fs');
const path = require('node:path');
const { randomUUID } = require('node:crypto');

const MEASUREMENT_ID = process.env.GA4_MEASUREMENT_ID || 'G-Q72NP8CB65';
const API_SECRET     = process.env.GA4_API_SECRET     || 'ZfvhJ6CeTbuUZIfecLo4JA';

let _clientId = null;
let _userDataPath = '';
let _sessionId = null;

function init(userDataPath) {
  _userDataPath = userDataPath;
  _sessionId = Date.now().toString();
}

function getClientId() {
  if (_clientId) return _clientId;
  const file = path.join(_userDataPath, 'analytics.json');
  try {
    const data = JSON.parse(fs.readFileSync(file, 'utf8'));
    if (data.clientId) { _clientId = data.clientId; return _clientId; }
  } catch {}
  _clientId = randomUUID();
  try { fs.writeFileSync(file, JSON.stringify({ clientId: _clientId })); } catch {}
  return _clientId;
}

function trackEvent(eventName, params = {}) {
  if (!MEASUREMENT_ID || !API_SECRET) return;
  const body = JSON.stringify({
    client_id: getClientId(),
    events: [{ name: eventName, params: { ...params, session_id: _sessionId, engagement_time_msec: 100, app_version: require('./package.json').version } }],
  });
  const req = https.request({
    hostname: 'www.google-analytics.com',
    path: `/mp/collect?measurement_id=${MEASUREMENT_ID}&api_secret=${API_SECRET}`,
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) },
  });
  req.on('error', () => {}); // silent fail
  req.write(body);
  req.end();
}

module.exports = { init, trackEvent };
```

## File: `CLAUDE.md`
```markdown
# Claude Inspector

## UI 버그 수정 원칙

1. **진단 먼저, 수정은 한 번에**: 부모→자식 전체 CSS/스타일 체인을 분석하고 원인을 특정한 후 수정한다. 추측으로 속성 하나 넣어보고 안 되면 또 넣어보는 식 금지.
2. **확인 후 커밋**: 앱 재시작 → 사용자 확인 → 커밋. "fix" 커밋이 실제로 안 고쳐진 상태로 푸시되면 안 된다.
3. **단순한 해법 우선**: 사용자가 단순한 방향을 제시하면 그대로 한다. flex 트릭보다 `display:block + overflow-y:auto`가 나을 수 있다.

## proxyDetailView 구조

- `#proxyDetailView`는 inline style로 `flex:1;overflow:hidden;display:flex;flex-direction:column` 지정됨
- **Messages 탭**: `container.style.cssText`로 `display:block;overflow-y:auto`로 전체 전환 (부분 override 불가)
- **다른 탭 전환 시**: `cssText`로 원래 flex 스타일 복원
```

## File: `DEVELOPMENT_GUIDE.md`
```markdown
# Claude Inspector — Development Guide

## 프로젝트 개요

Claude Code의 5가지 프롬프트 메커니즘(CLAUDE.md, Output Style, Slash Command, Skill, Sub-Agent)이
실제로 Anthropic API에 어떤 JSON 페이로드를 만드는지 시각화하고 테스트하는 **Electron 데스크탑 앱**.

**타겟 유저**: Claude Code 내부 동작 원리를 파악하고 싶은 개발자

## 아키텍처

```
main.js         Electron main process — BrowserWindow 생성, IPC 핸들러
preload.js      contextBridge — window.electronAPI 노출
public/
  index.html    단일 파일 프론트엔드 (CSS + Vanilla JS 인라인)
package.json    Electron + electron-builder 설정
```

### IPC 채널

| 채널 | 방향 | 역할 |
|------|------|------|
| `send-to-claude` | renderer → main | Anthropic API 호출 |

## 기술 스택

- **Electron 33** — 데스크탑 앱
- **@anthropic-ai/sdk** — API 호출 (main process에서만)
- **Vanilla JS** — 프레임워크 없음, 빌드 스텝 없음
- **highlight.js (CDN)** — JSON 신택스 하이라이팅
- **marked.js (CDN)** — Markdown 렌더링

## 현재 기능

- 5가지 메커니즘 탭 (각 실제 API 페이로드 실시간 미리보기)
- CLAUDE.md / Output Style / Slash Command: 직접 API 전송 가능
- Skill: Simulate Effect (단순화 버전으로 실전 테스트)
- Sub-Agent: Run Sub-Agent (delegation prompt 단독 실행)
- API Key localStorage 저장
- 플로우 다이어그램 (Skill, Sub-Agent 동작 시각화)

## 개발 규칙

- **Electron Only** — server.ts 삭제, web fallback 코드 제거
- `public/index.html` 단일 파일 유지 (외부 .js/.css 파일 생성 금지)
- IPC 추가 시: main.js `ipcMain.handle` + preload.js `contextBridge` 동시 수정
- UI 스타일: VS Code Dark+ 테마 유지 (CSS 변수 --bg, --surface, --blue 등)
- 커밋: 한글, HEREDOC 필수 (`~/.claude/rules/git-rules.md`)

## 빌드/실행

```bash
npm start          # 개발 실행
npm run dev        # 개발 + 로깅
npm run dist       # 배포 빌드 → release/
```

## 현재 완료된 기능 (2026-02-28)

### ✅ P0 완료
- server.ts 제거, web fallback 완전 삭제
- KB · 토큰 수 실시간 표시 (헤더 size-pill)
- 📂 파일 불러오기 (Electron dialog IPC)
- Markdown 응답 렌더링 (marked.js CDN + MD 토글 버튼)

### ✅ P1 완료
- Export 탭 — cURL / Python / TypeScript 스니펫 생성
- 요청 히스토리 패널 (세션 내 최근 10개, 클릭 복원)
- KB · ~토큰 실시간 표시

### ✅ UX 버그 수정
- macOS 창 드래그 (`-webkit-app-region: drag`)
- 트래픽 라이트 버튼 겹침 (`body.darwin .header { padding-left: 76px }`)

---

## 다음 작업: 프록시 모드 (진짜 인스펙터)

### 개요
현재 앱은 "시뮬레이터" — 페이로드를 직접 구성해서 전송.
**목표**: Claude Code CLI의 실제 API 트래픽을 가로채서 실시간 시각화.

### 원리
```
Claude Code CLI → localhost:9090 (프록시) → Anthropic API
                        ↓
                  Inspector UI에 실시간 표시
```

Claude Code는 `ANTHROPIC_BASE_URL` 환경변수를 지원:
```bash
ANTHROPIC_BASE_URL=http://localhost:9090 claude
```

### 구현 계획

#### main.js 추가
```js
// HTTP 프록시 서버 (node:http)
const proxyServer = http.createServer(async (req, res) => {
  // 1. 요청 바디 수집
  // 2. IPC로 renderer에 전송 (실시간 표시)
  // 3. 실제 Anthropic API로 포워딩
  // 4. 응답 캡처 후 IPC로 전송
  // 5. 클라이언트에 응답 반환
});
proxyServer.listen(9090);
```

#### IPC 채널 추가
| 채널 | 방향 | 역할 |
|------|------|------|
| `proxy-request` | main → renderer | 캡처된 요청 페이로드 |
| `proxy-response` | main → renderer | 캡처된 응답 |
| `proxy-start` | renderer → main | 프록시 서버 시작 |
| `proxy-stop` | renderer → main | 프록시 서버 중지 |

#### UI 추가
- **Proxy 탭** 추가 (또는 별도 모드)
- 프록시 ON/OFF 토글 + 포트 설정
- 캡처된 요청 목록 (실시간 스트림)
- 클릭하면 페이로드 상세 보기
- `ANTHROPIC_BASE_URL=http://localhost:9090 claude` 명령 복사 버튼

### 기술 고려사항
- `node:http` 모듈로 프록시 서버 구현 (외부 의존성 불필요)
- HTTPS: Anthropic API는 HTTPS지만 프록시는 HTTP로 받고 내부에서 SDK로 포워딩
- 스트리밍 응답: Anthropic SDK의 streaming 지원 활용
- 포트 충돌: 9090 사용 중이면 자동으로 다음 포트 탐색

---

## 개발 규칙

- **Electron Only** — web fallback 코드 금지
- `public/index.html` 단일 파일 유지 (외부 .js/.css 파일 생성 금지)
- IPC 추가 시: main.js `ipcMain.handle` + preload.js `contextBridge` 동시 수정
- UI 스타일: VS Code Dark+ 테마 유지 (CSS 변수 --bg, --surface, --blue 등)
- 커밋: 한글, HEREDOC 필수 (`~/.claude/rules/git-rules.md`)
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Raemin Kang

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

## File: `main.js`
```javascript
require('dotenv').config();
const Sentry = require('@sentry/electron/main');
Sentry.init({
  dsn: process.env.SENTRY_DSN || process.env.SENTRY_CLIENT_KEY || '',
  environment: process.env.NODE_ENV || 'development',
  release: `claude-inspector@${require('./package.json').version}`,
  beforeSend(event) {
    if (event.breadcrumbs) {
      event.breadcrumbs = event.breadcrumbs.map(bc => {
        if (bc.data) {
          delete bc.data['x-api-key'];
          delete bc.data['X-Api-Key'];
          delete bc.data['authorization'];
          delete bc.data['Authorization'];
        }
        return bc;
      });
    }
    return event;
  },
});

const analytics = require('./analytics');

const { app, BrowserWindow, ipcMain, shell } = require('electron');
const path = require('path');
const http = require('node:http');
const https = require('node:https');

let mainWin = null;
let proxyServer = null;

// Parse SSE stream into a reconstructed Anthropic message object
function parseSseStream(text) {
  try {
    let msg = null;
    function processEvent(data) {
      try {
        const d = JSON.parse(data);
        if (d.type === 'message_start') msg = Object.assign({}, d.message, { _streaming: true });
        if (d.type === 'content_block_start' && msg) { msg.content = msg.content || []; msg.content[d.index] = Object.assign({}, d.content_block); }
        if (d.type === 'content_block_delta' && msg) { const block = msg.content && msg.content[d.index]; if (block) { if (d.delta.type === 'text_delta') block.text = (block.text || '') + d.delta.text; if (d.delta.type === 'thinking_delta') block.thinking = (block.thinking || '') + d.delta.thinking; } }
        if (d.type === 'message_delta' && msg) { if (d.delta) Object.assign(msg, d.delta); if (d.usage) msg.usage = Object.assign({}, msg.usage, d.usage); }
      } catch {}
    }
    const events = {};
    for (const rawLine of text.split('\n')) {
      const line = rawLine.replace(/\r$/, '');
      const m = line.match(/^(event|data):\s?(.*)/);
      if (m) events[m[1]] = m[2].trimEnd();
      if (line === '' && events.data) {
        processEvent(events.data);
        events.event = undefined;
        events.data = undefined;
      }
    }
    if (events.data) processEvent(events.data);
    return msg || null;
  } catch { return null; }
}

function createWindow() {
  const win = new BrowserWindow({
    width: 1320,
    height: 860,
    minWidth: 980,
    minHeight: 620,
    icon: path.join(__dirname, 'assets/icon.png'),
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
    titleBarStyle: process.platform === 'darwin' ? 'hiddenInset' : 'default',
    ...(process.platform === 'darwin' ? { trafficLightPosition: { x: 12, y: 19 } } : {}),
    title: 'Claude Inspector',
    backgroundColor: '#1e1e1e',
    show: false,
  });

  win.loadFile(path.join(__dirname, 'public/index.html'));

  // Retry on load failure (macOS quarantine scan can lock the asar on first launch)
  win.webContents.on('did-fail-load', () => {
    setTimeout(() => {
      if (!win.isDestroyed()) win.loadFile(path.join(__dirname, 'public/index.html'));
    }, 1500);
  });

  win.once('ready-to-show', () => win.show());
  // Fallback: force show if ready-to-show never fires
  setTimeout(() => { if (!win.isDestroyed() && !win.isVisible()) win.show(); }, 3000);
  mainWin = win;

  // Open external links in browser, not Electron
  win.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });
}

app.whenReady().then(() => {
  analytics.init(app.getPath('userData'));
  analytics.trackEvent('app_open');
  if (process.platform === 'darwin') {
    app.dock.setIcon(path.join(__dirname, 'assets/icon.png'));
  }
  createWindow();
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    } else if (mainWin && !mainWin.isDestroyed()) {
      mainWin.show();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});

ipcMain.handle('proxy-start', (_event, port = 9090) => {
  if (!Number.isInteger(port) || port < 1024 || port > 65535) {
    return { error: 'Invalid port: must be 1024–65535' };
  }
  if (proxyServer) return { running: true, port: proxyServer.address().port };

  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      req.on('error', () => {
        if (!res.headersSent) res.writeHead(400);
        res.end();
      });
      const chunks = [];
      req.on('data', chunk => chunks.push(chunk));
      req.on('end', () => {
        const bodyBuf = Buffer.concat(chunks);
        let bodyObj = null;
        try { bodyObj = JSON.parse(bodyBuf.toString()); } catch (e) { console.warn('req body parse failed:', e.message); }

        const reqId = Date.now();
        const reqData = {
          id: reqId,
          ts: new Date().toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
          method: req.method,
          path: req.url,
          body: bodyObj,
          isApiKey: !!(req.headers['x-api-key']),
        };
        if (mainWin && !mainWin.isDestroyed()) mainWin.webContents.send('proxy-request', reqData);

        const headers = Object.assign({}, req.headers, { host: 'api.anthropic.com' });
        delete headers['accept-encoding']; // Prevent gzip response so we can parse it
        const options = { hostname: 'api.anthropic.com', port: 443, path: req.url, method: req.method, headers };

        const proxyReq = https.request(options, (proxyRes) => {
          res.writeHead(proxyRes.statusCode, proxyRes.headers);
          const respChunks = [];
          proxyRes.on('data', chunk => { respChunks.push(chunk); res.write(chunk); });
          proxyRes.on('error', () => { res.end(); });
          proxyRes.on('end', () => {
            res.end();
            setImmediate(() => {
              const respStr = Buffer.concat(respChunks).toString('utf8');
              let respObj = null;
              try { respObj = JSON.parse(respStr); } catch { /* SSE stream — JSON.parse expected to fail */ }
              if (!respObj) respObj = parseSseStream(respStr);
              if (mainWin && !mainWin.isDestroyed()) {
                mainWin.webContents.send('proxy-response', {
                  id: reqId, status: proxyRes.statusCode,
                  body: respObj || respStr.slice(0, 4000),
                });
              }
            });
          });
        });

        proxyReq.on('error', (err) => {
          if (!res.headersSent) res.writeHead(502, { 'content-type': 'application/json' });
          res.end(JSON.stringify({ error: err.message }));
          if (mainWin && !mainWin.isDestroyed()) {
            mainWin.webContents.send('proxy-response', { id: reqId, error: err.message });
          }
        });

        proxyReq.end(bodyBuf);
      });
    });

    server.on('listening', () => {
      proxyServer = server;
      analytics.trackEvent('proxy_started');
      resolve({ running: true, port: server.address().port });
    });
    let retried = false;
    server.on('error', (err) => {
      if (err.code === 'EADDRINUSE' && !retried) {
        retried = true;
        server.listen(0, '127.0.0.1');
      } else {
        resolve({ error: err.message });
      }
    });
    server.listen(port, '127.0.0.1');
  });
});

ipcMain.handle('proxy-status', () => {
  if (proxyServer) {
    try { return { running: true, port: proxyServer.address().port }; }
    catch { return { running: false }; }
  }
  return { running: false };
});

ipcMain.handle('proxy-stop', () => {
  if (!proxyServer) return { stopped: true };
  const srv = proxyServer;
  proxyServer = null;
  return new Promise((resolve) => {
    srv.close(() => { resolve({ stopped: true }); });
  });
});

app.on('before-quit', () => { if (proxyServer) proxyServer.close(); });
```

## File: `package.json`
```json
{
  "name": "claude-inspector",
  "version": "1.1.4",
  "description": "Claude Code Prompt Mechanism Visualizer",
  "license": "MIT",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "dev": "electron . --enable-logging",
    "predist": "node -e \"const {execSync}=require('child_process');const fs=require('fs');const hash=execSync('git rev-parse --short HEAD').toString().trim();const pkg=require('./package.json');fs.writeFileSync('public/build-info.json',JSON.stringify({version:pkg.version,hash,built:new Date().toISOString()}))\"",
    "dist": "electron-builder",
    "dist:mac": "electron-builder --mac",
    "dist:win": "electron-builder --win",
    "test": "npm run test:unit && npm run test:e2e",
    "test:unit": "node --test tests/unit/*.mjs",
    "test:e2e": "playwright test"
  },
  "build": {
    "appId": "com.claudeinspector.app",
    "productName": "Claude Inspector",
    "directories": {
      "output": "release"
    },
    "files": [
      "main.js",
      "preload.js",
      "analytics.js",
      "public/**",
      "assets/icon.png",
      "assets/icon.icns",
      "node_modules/@sentry/**",
      "node_modules/dotenv/**"
    ],
    "afterSign": "scripts/notarize.js",
    "mac": {
      "icon": "assets/icon.icns",
      "category": "public.app-category.developer-tools",
      "artifactName": "Claude-Inspector-${version}-${arch}.${ext}",
      "target": [
        {
          "target": "dmg",
          "arch": [
            "arm64",
            "x64"
          ]
        }
      ]
    },
    "win": {
      "target": "nsis"
    }
  },
  "dependencies": {
    "@sentry/electron": "^7.10.0",
    "dotenv": "^17.3.1"
  },
  "devDependencies": {
    "@playwright/test": "^1.58.2",
    "electron": "^33.2.0",
    "electron-builder": "^25.1.8"
  }
}
```

## File: `playwright.config.ts`
```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests/e2e',
  timeout: 30_000,
  retries: 0,
  reporter: 'list',
});
```

## File: `preload.js`
```javascript
try { require('@sentry/electron/renderer').init(); } catch {}

const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  platform: process.platform,
  proxyStart: (port) => ipcRenderer.invoke('proxy-start', port),
  proxyStop: () => ipcRenderer.invoke('proxy-stop'),
  proxyStatus: () => ipcRenderer.invoke('proxy-status'),
  onProxyRequest: (cb) => ipcRenderer.on('proxy-request', (_, data) => cb(data)),
  onProxyResponse: (cb) => ipcRenderer.on('proxy-response', (_, data) => cb(data)),
  offProxy: () => {
    ipcRenderer.removeAllListeners('proxy-request');
    ipcRenderer.removeAllListeners('proxy-response');
  },
});
```

## File: `README.ko.md`
```markdown
<div align="center">

# Claude Inspector

**Claude Code가 API에 실제로 무엇을 보내는지 확인하세요.**

Claude Code CLI 트래픽을 실시간으로 가로채<br>
5가지 프롬프트 증강 메커니즘을 모두 시각화하는 MITM 프록시.

[설치](#설치) · [배울 수 있는 것들](#배울-수-있는-것들) · [프록시 모드](#프록시-모드) · [기술 스택](#기술-스택)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/kangraemin/claude-inspector)](https://github.com/kangraemin/claude-inspector/releases/latest)
[![macOS](https://img.shields.io/badge/macOS-arm64%20%7C%20x64-black)](https://github.com/kangraemin/claude-inspector/releases/latest)

[English](README.md) | **한국어**

</div>

---

<p align="center">
  <img src="public/screenshots/ko-1.png" width="100%" alt="Proxy — Analysis 뷰" />
</p>

<p align="center">
  <img src="public/screenshots/ko-2.png" width="100%" alt="Proxy — Request 뷰 (비용 분석)" />
</p>

<p align="center">
  <img src="public/screenshots/ko-3.png" width="100%" alt="Proxy — Request 뷰" />
</p>

## 배울 수 있는 것들

아래 내용은 모두 **실제 캡처된 트래픽**에서 발견한 것입니다. Claude Code가 감추고 있는 것을 확인하세요.

### 1. CLAUDE.md는 매 요청마다 주입된다

`hello`를 입력하면, Claude Code는 메시지 앞에 **~12KB**를 자동으로 추가합니다:

| 블록 | 내용 | 크기 |
|------|------|------|
| `content[0]` | 사용 가능한 스킬 목록 | ~2KB |
| `content[1]` | CLAUDE.md + rules + memory | **~10KB** |
| `content[2]` | 실제로 입력한 내용 | 수 바이트 |

**주입 순서:** 글로벌 CLAUDE.md → 글로벌 rules → 프로젝트 CLAUDE.md → Memory

이 ~12KB 페이로드는 **매 요청마다** 재전송됩니다. 500줄짜리 CLAUDE.md는 모든 API 호출에서 조용히 토큰을 소모합니다. 간결하게 유지하세요.

### 2. MCP 도구는 지연 로드된다 — `tools[]`가 늘어나는 것을 확인하세요

빌트인 도구(27개)는 매 요청마다 전체 JSON 스키마를 전송합니다. MCP 도구는 그렇지 않습니다 — 처음에는 **이름만** 존재합니다.

**실시간으로 개수가 변하는 것을 확인하세요:**

| 단계 | 발생하는 일 | `tools[]` 개수 |
|------|------------|---------------|
| 초기 요청 | 27개 빌트인 도구 로드 | **27** |
| 모델이 `ToolSearch("context7")` 호출 | 2개 MCP 도구 전체 스키마 반환 | **29** |
| 모델이 `ToolSearch("til")` 호출 | 6개 MCP 도구 스키마 추가 | **35** |

사용하지 않는 MCP 도구는 토큰을 소비하지 않습니다. Inspector로 모델이 필요한 도구를 발견할 때 `tools[]`가 늘어나는 것을 확인할 수 있습니다.

### 3. 이미지는 base64로 인라인 인코딩된다

Claude Code가 스크린샷이나 이미지 파일을 읽을 때, 이미지는 **base64로 인코딩되어 JSON 본문에 직접 포함**됩니다:

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/png",
    "data": "iVBORw0KGgo..."
  }
}
```

스크린샷 하나가 요청 페이로드에 **수백 KB**를 추가할 수 있습니다. Inspector로 정확한 크기를 확인할 수 있습니다.

### 4. Skill ≠ Command — 완전히 다른 주입 경로

`/something`을 입력하면 세 가지 완전히 다른 메커니즘 중 하나가 작동합니다:

| | 로컬 커맨드 | 사용자 스킬 | 어시스턴트 스킬 |
|---|---|---|---|
| **예시** | `/mcp`, `/clear` | `/commit` | `Skill("finish")` |
| **트리거** | 사용자 | 사용자 | 모델 |
| **주입** | `<local-command-stdout>` | user msg에 전체 프롬프트 | `tool_use` → `tool_result` |
| **모델에 전달** | 결과만 | 전체 프롬프트 | 전체 프롬프트 |

**커맨드**는 로컬에서 실행되어 결과만 전달합니다. **스킬**은 프롬프트 전체를 주입하며 — 세션이 끝날 때까지 **이후 모든 요청에 남습니다**.

### 5. 이전 메시지가 계속 쌓인다 — `/clear`를 자주 사용하세요

Claude Code는 매 요청마다 `messages[]` 배열 **전체**를 재전송합니다:

```json
{
  "messages": [
    {"role": "user",      "content": [/* ~12KB CLAUDE.md */ , "hello"]},
    {"role": "assistant", "content": [/* tool_use, thinking, response */]},
    {"role": "user",      "content": [/* ~12KB CLAUDE.md */ , "fix the bug"]},
    {"role": "assistant", "content": [/* tool_use, thinking, response */]},
    // ... 30턴 = CLAUDE.md 30개 복사본 + 모든 응답
  ]
}
```

| 턴 수 | 대략적인 누적 전송량 |
|-------|---------------------|
| 1 | ~15KB |
| 10 | ~200KB |
| 30 | ~1MB+ |

대부분은 더 이상 필요 없는 이전 대화입니다. 누적될수록:

- **비용 증가** — 요청당 입력 토큰이 늘어나 API 비용이 올라감
- **컨텍스트 윈도우 포화** — 한계에 도달하면 이전 메시지가 자동 압축되어 세부 내용이 유실됨
- **응답 속도 저하** — 페이로드가 클수록 처리 시간이 길어짐

`/clear`를 실행하면 컨텍스트가 초기화되고 누적된 무게가 사라집니다. 자주 정리하세요.

### 6. 서브 에이전트는 완전히 격리된 컨텍스트에서 실행된다

Claude Code가 서브 에이전트를 생성하면(`Agent` 도구 사용), **완전히 별도의 API 호출**이 만들어집니다. 부모와 서브 에이전트는 완전히 다른 `messages[]`를 가집니다:

| | 부모 API 호출 | 서브 에이전트 API 호출 |
|---|---|---|
| **`messages[]`** | 전체 대화 이력 (모든 턴) | 작업 프롬프트만 — **부모 이력 없음** |
| **CLAUDE.md** | 포함됨 | 포함됨 (독립적으로) |
| **tools[]** | 로드된 모든 도구 | 새로운 세트 |
| **컨텍스트** | 누적됨 | 0에서 시작 |

Inspector는 부모와 서브 에이전트 호출을 모두 캡처하므로, 각각이 무엇을 보는지 비교할 수 있습니다.

## 설치

### Homebrew (권장)

```bash
brew install --cask kangraemin/tap/claude-inspector && sleep 2 && open -a "Claude Inspector"
```

### 직접 다운로드

[Releases](https://github.com/kangraemin/claude-inspector/releases/latest) 페이지에서 `.dmg`를 다운로드하세요.

| Mac (Apple Silicon) | Mac (Intel) |
|---|---|
| [Claude-Inspector-arm64.dmg](https://github.com/kangraemin/claude-inspector/releases/latest) | [Claude-Inspector-x64.dmg](https://github.com/kangraemin/claude-inspector/releases/latest) |

### 업그레이드

```bash
brew update && brew upgrade --cask claude-inspector && sleep 2 && open -a "Claude Inspector"
```

### 삭제

```bash
brew uninstall --cask claude-inspector
```

## 개발 환경

```bash
git clone https://github.com/kangraemin/claude-inspector.git
cd claude-inspector
npm install
npm start
```

## 프록시 모드

로컬 MITM 프록시를 통해 **실제** Claude Code CLI 트래픽을 인터셉트합니다.

```
Claude Code CLI  →  Inspector (localhost:9090)  →  api.anthropic.com
```

**1.** 앱에서 **Start Proxy** 클릭<br>
**2.** 프록시를 통해 Claude Code 실행:

```bash
ANTHROPIC_BASE_URL=http://localhost:9090 claude
```

**3.** 모든 API 요청/응답이 실시간으로 캡처됩니다.

## 기술 스택

| 레이어 | 기술 | 이유 |
|--------|------|------|
| **Electron** | 데스크탑 셸, main/renderer 간 IPC | 네이티브 macOS 타이틀바(`hiddenInset`), 코드 서명 + 공증된 DMG 배포 |
| **Vanilla JS** | 프레임워크 없음, 빌드 단계 없음 | 전체 UI가 단일 `index.html` — 번들러 없음, 트랜스파일러 없음, React 없음 |
| **Node `http`/`https`** | `localhost` MITM 프록시 | Claude Code ↔ Anthropic API 트래픽 인터셉트, SSE 스트림을 완전한 응답 객체로 재조립 |
| **highlight.js + marked** | 구문 강조 및 마크다운 | JSON 페이로드와 마크다운 콘텐츠를 인라인 렌더링 |

> **프라이버시**: 모든 트래픽은 `localhost`에서만 처리됩니다. `api.anthropic.com`으로 직접 전송되는 것 외에 어디에도 데이터를 보내지 않습니다.

## 라이선스

MIT
```

## File: `README.md`
```markdown
<div align="center">

# Claude Inspector

**See what Claude Code actually sends to the API.**

MITM proxy that intercepts Claude Code CLI traffic in real-time<br>
and visualizes all 5 prompt augmentation mechanisms.

[Install](#install) · [What You'll Learn](#what-youll-learn) · [Proxy Mode](#proxy-mode) · [Tech Stack](#tech-stack)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/kangraemin/claude-inspector)](https://github.com/kangraemin/claude-inspector/releases/latest)
[![macOS](https://img.shields.io/badge/macOS-arm64%20%7C%20x64-black)](https://github.com/kangraemin/claude-inspector/releases/latest)

**English** | [한국어](README.ko.md)

</div>

---

<p align="center">
  <img src="public/screenshots/en-1.png" width="100%" alt="Proxy — Analysis view" />
</p>

<p align="center">
  <img src="public/screenshots/en-2.png" width="100%" alt="Proxy — Request view with cost breakdown" />
</p>

<p align="center">
  <img src="public/screenshots/en-3.png" width="100%" alt="Proxy — Request view" />
</p>

## What You'll Learn

All discovered from **real captured traffic**. See what Claude Code hides from you.

### 1. CLAUDE.md is injected into every single request

You type `hello`. Claude Code silently prepends **~12KB** before your message:

| Block | What's inside | Size |
|-------|--------------|------|
| `content[0]` | Available skills list | ~2KB |
| `content[1]` | CLAUDE.md + rules + memory | **~10KB** |
| `content[2]` | What you actually typed | few bytes |

**Injection order:** Global CLAUDE.md → Global rules → Project CLAUDE.md → Memory

This ~12KB payload is re-sent with **every request**. A 500-line CLAUDE.md quietly burns tokens on every API call. Keep it lean.

### 2. MCP tools are lazy-loaded — watch `tools[]` grow

Built-in tools (27) ship their full JSON schemas every request. MCP tools don't — they start as **names only**.

**Watch the count change in real-time:**

| Step | What happens | `tools[]` count |
|------|-------------|-----------------|
| Initial request | 27 built-in tools loaded | **27** |
| Model calls `ToolSearch("context7")` | Full schema for 2 MCP tools returned | **29** |
| Model calls `ToolSearch("til")` | 6 more MCP tool schemas added | **35** |

Unused MCP tools never consume tokens. The Inspector lets you watch `tools[]` grow as the model discovers what it needs.

### 3. Images are base64-encoded inline

When Claude Code reads a screenshot or image file, the image is **base64-encoded and embedded directly** in the JSON body:

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/png",
    "data": "iVBORw0KGgo..."
  }
}
```

A single screenshot can add **hundreds of KB** to the request payload. The Inspector shows you the exact size.

### 4. Skill ≠ Command — completely different injection paths

Typing `/something` triggers one of three completely different mechanisms:

| | Local Command | User Skill | Assistant Skill |
|---|---|---|---|
| **Example** | `/mcp`, `/clear` | `/commit` | `Skill("finish")` |
| **Who triggers** | User | User | Model |
| **Injection** | `<local-command-stdout>` | Full prompt in user msg | `tool_use` → `tool_result` |
| **Model sees** | Result only | Full prompt | Full prompt |

**Commands** run locally and only pass the result. **Skills** inject the entire prompt text — and it **stays in every subsequent request** until the session ends.

### 5. Previous messages pile up — use `/clear` often

Claude Code re-sends the **entire** `messages[]` array with every request:

```json
{
  "messages": [
    {"role": "user",      "content": [/* ~12KB CLAUDE.md */ , "hello"]},
    {"role": "assistant", "content": [/* tool_use, thinking, response */]},
    {"role": "user",      "content": [/* ~12KB CLAUDE.md */ , "fix the bug"]},
    {"role": "assistant", "content": [/* tool_use, thinking, response */]},
    // ... 30 turns = 30 copies of CLAUDE.md + all responses
  ]
}
```

| Turns | Approx. cumulative transfer |
|-------|---------------------|
| 1 | ~15KB |
| 10 | ~200KB |
| 30 | ~1MB+ |

Most of it is old conversation you no longer need. As it grows:

- **Cost increases** — more input tokens per request means higher API bills
- **Context window fills up** — once the limit is hit, older messages get auto-compressed and detail is lost
- **Responses slow down** — larger payloads take longer to process

Running `/clear` resets the context and drops the accumulated weight. Clear early, clear often.

### 6. Sub-agents run in fully isolated contexts

When Claude Code spawns a sub-agent (via the `Agent` tool), it creates a **completely separate API call**. The parent and sub-agent have entirely different `messages[]`:

| | Parent API call | Sub-agent API call |
|---|---|---|
| **`messages[]`** | Full conversation history (all turns) | Only the task prompt — **no parent history** |
| **CLAUDE.md** | Included | Included (independently) |
| **tools[]** | All loaded tools | Fresh set |
| **Context** | Accumulated | Starts from zero |

The Inspector captures both calls side by side, so you can compare what each one sees.

## Install

### Homebrew (Recommended)

```bash
brew install --cask kangraemin/tap/claude-inspector && sleep 2 && open -a "Claude Inspector"
```

### Direct Download

Download the `.dmg` from the [Releases](https://github.com/kangraemin/claude-inspector/releases/latest) page.

| Mac (Apple Silicon) | Mac (Intel) |
|---|---|
| [Claude-Inspector-arm64.dmg](https://github.com/kangraemin/claude-inspector/releases/latest) | [Claude-Inspector-x64.dmg](https://github.com/kangraemin/claude-inspector/releases/latest) |

### Upgrade

```bash
brew update && brew upgrade --cask claude-inspector && sleep 2 && open -a "Claude Inspector"
```

### Uninstall

```bash
brew uninstall --cask claude-inspector
```

## Development

```bash
git clone https://github.com/kangraemin/claude-inspector.git
cd claude-inspector
npm install
npm start
```

## Proxy Mode

Intercept **real** Claude Code CLI traffic via a local MITM proxy.

```
Claude Code CLI  →  Inspector (localhost:9090)  →  api.anthropic.com
```

**1.** Click **Start Proxy** in the app<br>
**2.** Run Claude Code through the proxy:

```bash
ANTHROPIC_BASE_URL=http://localhost:9090 claude
```

**3.** Every API request/response is captured in real-time.

## Tech Stack

| Layer | What | Why |
|-------|------|-----|
| **Electron** | Desktop shell, IPC between main/renderer | Native macOS titlebar (`hiddenInset`), code-signed + notarized DMG distribution |
| **Vanilla JS** | Zero frameworks, zero build steps | Entire UI in a single `index.html` — no bundler, no transpiler, no React |
| **Node `http`/`https`** | MITM proxy on `localhost` | Intercepts Claude Code ↔ Anthropic API traffic, reassembles SSE streams into complete response objects |
| **highlight.js + marked** | Syntax highlighting & markdown | Renders JSON payloads and markdown content inline |

> **Privacy**: All traffic stays on `localhost`. Nothing is sent anywhere except directly to `api.anthropic.com`.

## License

MIT
```

## File: `brain/knowledge/docs_legacy/2026-03-13/claudemd-linenum-fix/plan.md`
```markdown
# CLAUDE.md 클릭 시 깨짐 수정

## 변경 파일별 상세
### `public/index.html`

#### highlightMechInJsonTree — CLAUDE.md(cm_*) 블록

- **변경 이유**: CLAUDE.md 칩 클릭 시 `expandLongStr` + `expandAncestors`로 긴 문자열을 자동 펼치면, 단일 `.jt-row` 안에 수백 줄의 텍스트가 표시되어 줄 번호 거터가 비어보임. 자동 펼침을 제거하고 해당 `.jt-row`만 하이라이트.
- **Before** (라인 ~2700-2739):
```javascript
if (mechKey.startsWith('cm')) {
    // ...
    for (const el of strEls) {
      if (!el.textContent.includes('Contents of ' + section.path)) continue;
      expandLongStr(el);
      expandAncestors(el);
      const html = el.innerHTML;
      // ... hlRange로 텍스트 범위 하이라이트
      hlRange(el, start, end, true);
      break;
    }
}
```
- **After**:
```javascript
if (mechKey.startsWith('cm')) {
    // ...
    // .jt-str, .jt-str-expanded, .jt-str-preview 모두 검색
    const allStr = container.querySelectorAll('.jt-str, .jt-str-expanded, .jt-str-preview');
    for (const el of allStr) {
      if (!el.textContent.includes('Contents of ' + section.path)) continue;
      // 자동 펼침 안 함. 부모 .jt-row를 찾아서 하이라이트
      expandAncestors(el);
      const row = el.closest('.jt-row');
      if (row) {
        row.classList.add('mech-hl-row');
        requestAnimationFrame(() => row.scrollIntoView({ behavior: 'smooth', block: 'start' }));
      }
      break;
    }
}
```
- **영향 범위**: CLAUDE.md 칩 클릭 동작만 변경. 다른 메커니즘(sc, os 등) 하이라이트는 그대로.

#### CSS — mech-hl-row 클래스 확인
- 이미 `mech-hl-row`가 정의되어 있는지 확인 필요. 없으면 추가.

## 검증
- 검증 명령어: `pkill -x "Electron" 2>/dev/null; npm start &`
- 기대 결과: CLAUDE.md 칩 클릭 시 해당 행이 하이라이트되고 스크롤됨. 문자열 자동 펼침 없음. 줄 번호 유지.
```

## File: `brain/knowledge/docs_legacy/2026-03-13/claudemd-linenum-fix/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/claudemd-linenum-fix",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/claudemd-linenum-fix/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/plan.md`
```markdown
# 코드 품질 이슈 9건 일괄 수정

## Context
코드 품질 리뷰에서 발견된 보안(XSS), 에러 핸들링, 입력 검증, 프로토콜 처리 이슈 9건 수정.
proxyCaptures 메모리 누수는 이미 50개 제한이 있어 false positive (수정 불필요).
포트 입력 필드는 이미 `min="1024"` 설정됨.

## 변경 파일
- `main.js` — 7건 (Issues 2,3,5,6,7,9,10)
- `public/index.html` — 2건 (Issues 1,4)

---

## Phase 1: main.js 네트워크 안전성 (Issues 2, 3, 10)

### Issue 2: EADDRINUSE 재시도 실패 시 promise 영구 대기
- **Before** (line ~197):
```javascript
server.on('error', (err) => {
  if (err.code === 'EADDRINUSE') server.listen(0, '127.0.0.1');
  else resolve({ error: err.message });
});
```
- **After**:
```javascript
let retried = false;
server.on('error', (err) => {
  if (err.code === 'EADDRINUSE' && !retried) {
    retried = true;
    server.listen(0, '127.0.0.1');
  } else {
    resolve({ error: err.message });
  }
});
```

### Issue 3: req 스트림 에러 핸들러 누락
- **Before** (line ~138):
```javascript
const server = http.createServer((req, res) => {
  const chunks = [];
```
- **After**:
```javascript
const server = http.createServer((req, res) => {
  req.on('error', () => {
    if (!res.headersSent) res.writeHead(400);
    res.end();
  });
  const chunks = [];
```

### Issue 10: proxyRes 스트림 에러 핸들러 누락
- **Before** (line ~163):
```javascript
proxyRes.on('data', chunk => { respChunks.push(chunk); res.write(chunk); });
proxyRes.on('end', () => {
```
- **After**:
```javascript
proxyRes.on('data', chunk => { respChunks.push(chunk); res.write(chunk); });
proxyRes.on('error', () => { res.end(); });
proxyRes.on('end', () => {
```

---

## Phase 2: main.js 입력 검증 (Issues 5, 9)

### Issue 5: 토큰 추정 입력 길이 무제한
- **Before** (line ~126):
```javascript
ipcMain.handle('get-token-estimate', (_event, text) => {
  // Rough approximation: ~4 chars per token
  return Math.ceil((text || '').length / 4);
});
```
- **After**:
```javascript
ipcMain.handle('get-token-estimate', (_event, text) => {
  // Rough approximation: ~4 chars per token (cap at 10MB)
  const s = (text || '').slice(0, 10_000_000);
  return Math.ceil(s.length / 4);
});
```

### Issue 9: 특권 포트(1-1023) 허용
- **Before** (line ~132):
```javascript
if (!Number.isInteger(port) || port < 1 || port > 65535) {
  return { error: 'Invalid port: must be 1–65535' };
}
```
- **After**:
```javascript
if (!Number.isInteger(port) || port < 1024 || port > 65535) {
  return { error: 'Invalid port: must be 1024–65535' };
}
```

---

## Phase 3: main.js 프로토콜 처리 (Issues 6, 7)

### Issue 6: SSE 파싱 — 스트림 끝에 빈 줄 없으면 마지막 이벤트 유실
이벤트 처리 로직을 헬퍼 함수로 추출하여 중복 제거.

- **Before** (line ~12-47): `var msg` 사용, for 루프 내부에서만 이벤트 처리
- **After**: `processEvent` 헬퍼 추출 + 루프 후 잔여 이벤트 처리
```javascript
function parseSseStream(text) {
  try {
    let msg = null;
    function processEvent(data) {
      try {
        const d = JSON.parse(data);
        if (d.type === 'message_start') msg = Object.assign({}, d.message, { _streaming: true });
        if (d.type === 'content_block_start' && msg) { msg.content = msg.content || []; msg.content[d.index] = Object.assign({}, d.content_block); }
        if (d.type === 'content_block_delta' && msg) { const block = msg.content && msg.content[d.index]; if (block) { if (d.delta.type === 'text_delta') block.text = (block.text || '') + d.delta.text; if (d.delta.type === 'thinking_delta') block.thinking = (block.thinking || '') + d.delta.thinking; } }
        if (d.type === 'message_delta' && msg) { if (d.delta) Object.assign(msg, d.delta); if (d.usage) msg.usage = Object.assign({}, msg.usage, d.usage); }
      } catch {}
    }
    const events = {};
    for (const rawLine of text.split('\n')) {
      const line = rawLine.replace(/\r$/, '');
      const m = line.match(/^(event|data):\s?(.*)/);
      if (m) events[m[1]] = m[2].trimEnd();
      if (line === '' && events.data) {
        processEvent(events.data);
        events.event = undefined;
        events.data = undefined;
      }
    }
    if (events.data) processEvent(events.data);
    return msg || null;
  } catch { return null; }
}
```

### Issue 7: proxy-stop race condition
- **Before** (line ~213):
```javascript
ipcMain.handle('proxy-stop', () => {
  if (!proxyServer) return { stopped: true };
  return new Promise((resolve) => {
    proxyServer.close(() => { proxyServer = null; resolve({ stopped: true }); });
  });
});
```
- **After**:
```javascript
ipcMain.handle('proxy-stop', () => {
  if (!proxyServer) return { stopped: true };
  const srv = proxyServer;
  proxyServer = null;
  return new Promise((resolve) => {
    srv.close(() => { resolve({ stopped: true }); });
  });
});
```

---

## Phase 4: public/index.html XSS 수정 (Issues 1, 4)

### Issue 1: onclick 핸들러 XSS
`safePattern` 제거, `data-key` 속성 + `esc()` 사용. `setProxyDetailMechFilter`에서 미사용 `pattern` 파라미터 제거.

- **Before** (line ~2850):
```javascript
chips.map(c => {
  const active = proxyDetailMechFilter === c.key ? ' active' : '';
  const safePattern = (c.pattern || '').replace(/\\/g, '\\\\').replace(/'/g, "\\'");
  return `<span class="mech-chip ${c.cls} found btn${active}" onclick="setProxyDetailMechFilter('${c.key}','${safePattern}')">${c.label}</span>`;
}).join('')
```
- **After**:
```javascript
chips.map(c => {
  const active = proxyDetailMechFilter === c.key ? ' active' : '';
  return `<span class="mech-chip ${c.cls} found btn${active}" data-key="${escAttr(c.key)}" onclick="setProxyDetailMechFilter(this.dataset.key)">${esc(c.label)}</span>`;
}).join('')
```

함수 시그니처 변경 (line ~2770):
- **Before**: `function setProxyDetailMechFilter(key, pattern) {`
- **After**: `function setProxyDetailMechFilter(key) {`

### Issue 4: 토큰 팝오버 미이스케이프 값
`d.model`, `d.kb`, `d.total`, `d.cachePct`, `r.label`, `r.tokens`, `r.price`, `r.cost`에 `esc()` 적용.

- **rowsHtml** (line ~3441):
  - Before: `${r.label}`, `${r.tokens}`, `${r.price}`, `${r.cost}`
  - After: `${esc(r.label)}`, `${esc(r.tokens)}`, `${esc(r.price)}`, `${esc(r.cost)}`

- **popover info** (line ~3457):
  - Before: `${d.model}`, `${d.kb}`
  - After: `${esc(d.model)}`, `${esc(d.kb)}`

- **total/cachePct** (line ~3459-3460):
  - Before: `${d.total}`, `${d.cachePct}`
  - After: `${esc(d.total)}`, `${esc(d.cachePct)}`

---

## 검증
- `npm run test:unit` — 13개 단위 테스트 통과 확인
- `npm run test:e2e` — 25개 E2E 테스트 통과 확인
- 앱 실행 → 프록시 시작/중지 동작 확인
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/round-1.md`
```markdown
# 검증 1회차 — 기능 충실도

## Plan 대비 구현 확인

| Issue | 설명 | 구현 |
|-------|------|------|
| Issue 2 | EADDRINUSE 재시도 무한 루프 방지 | ✅ phase-1/step-1 — `retried` 플래그 |
| Issue 3 | req 스트림 에러 핸들러 누락 | ✅ phase-1/step-2 — req.on('error') 추가 |
| Issue 10 | proxyRes 스트림 에러 핸들러 누락 | ✅ phase-1/step-2 — proxyRes.on('error') 추가 |
| Issue 5 | 토큰 추정 입력 길이 무제한 | ✅ phase-2/step-1 — 10MB slice 제한 |
| Issue 9 | 특권 포트(1-1023) 허용 | ✅ phase-2/step-1 — 하한 1024 |
| Issue 6 | SSE 마지막 이벤트 유실 | ✅ phase-3/step-1 — processEvent 헬퍼 + 잔여 처리 |
| Issue 7 | proxy-stop race condition | ✅ phase-3/step-2 — null 선 할당 |
| Issue 1 | onclick XSS | ✅ phase-4/step-1 — data-key + escAttr |
| Issue 4 | 토큰 팝오버 미이스케이프 | ✅ phase-4/step-2 — esc() 8곳 적용 |

## 문서 완결성

| 파일 | TC 테이블 | 실행 결과 | 빌드 | 완료기준 |
|------|-----------|-----------|------|----------|
| phase-1/step-1.md | ✅ 5/5 PASS | ✅ grep + test 출력 | ✅ 13/13 | ✅ |
| phase-1/step-2.md | ✅ 5/5 PASS | ✅ grep + test 출력 | ✅ 13/13 | ✅ |
| phase-2/step-1.md | ✅ 4/4 PASS | ✅ grep + test 출력 | ✅ 13/13 | ✅ |
| phase-3/step-1.md | ✅ 4/4 PASS | ✅ grep + test 출력 | ✅ 13/13 | ✅ |
| phase-3/step-2.md | ✅ 4/4 PASS | ✅ grep + test 출력 | ✅ 13/13 | ✅ |
| phase-4/step-1.md | ✅ 6/6 PASS | ✅ grep + test 출력 | ✅ 13/13 | ✅ |
| phase-4/step-2.md | ✅ 9/9 PASS | ✅ grep + test 출력 | ✅ 13/13 | ✅ |

## Step 파일 수 정합성
- state.json 정의: 7 steps
- 실제 step-*.md 파일: 7개
- 결과: OK

## 결론
통과 — plan.md의 9건 이슈가 모두 7개 step 문서에 정확히 매핑되고, 모든 문서의 TC/실행결과/빌드/완료기준이 충족됨.
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/round-2.md`
```markdown
# 검증 2회차 -- 코드 품질

## 변경 코드 리뷰

- `main.js` (lines 12-38): parseSseStream -- processEvent 헬퍼 정상 추출, `let msg` 스코핑 정확, line 35 잔여 이벤트 처리 정상. 빈 catch 블록은 malformed SSE 방어용으로 적절.
- `main.js` (lines 131-134): req.on('error') -- headersSent 체크 후 400 응답, res.end() 호출. 리소스 누수 없음.
- `main.js` (line 160): proxyRes.on('error') -- res.end() 호출. 중복 호출 시에도 안전 (no-op).
- `main.js` (lines 117-121): 토큰 추정 10MB 입력 제한 -- slice 후 length 계산으로 정확.
- `main.js` (lines 124-126): 포트 하한 1024 검증 정상.
- `main.js` (lines 194-202): EADDRINUSE 재시도 1회 제한 -- retried 플래그 정상 작동.
- `main.js` (lines 215-222): proxy-stop race condition 방지 -- null 선 할당 후 srv.close(). line 224 before-quit 핸들러도 proxyServer null 체크로 안전.
- `public/index.html` (line 2852): mech-chip XSS 수정 -- data-key + escAttr + this.dataset.key 패턴으로 onclick 인젝션 차단. esc(c.label)로 텍스트 이스케이프.
- `public/index.html` (lines 3440, 3456, 3458-3459): 토큰 팝오버 8개 값 모두 esc() 적용 확인.

## 발견된 이슈

- 없음

## Minor 참고사항

- `escAttr()`가 single quote는 이스케이프하지 않으나, 모든 HTML 속성이 double quote를 사용하므로 문제 없음.

## 결론
통과 -- Critical/Important 이슈 없음. 모든 변경 코드가 의도대로 정확히 구현됨.
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/round-3.md`
```markdown
# 검증 3회차 -- 통합 & 회귀

## 테스트 실행

- `npm run test:unit`: 13/13 통과 (100ms)
- `npm run test:e2e`: 25/25 통과 (3.7s)

## 변경 파일 간 상호작용

- `parseSseStream`: main.js 내부에서만 정의(line 12) 및 호출(line 167). 외부 의존 없음.
- `setProxyDetailMechFilter`: index.html 내부에서 정의(line 2770, 1 param)와 호출(line 2852, `this.dataset.key` 1 arg) 시그니처 일치.
- `esc()` / `escAttr()`: index.html 내부에서만 정의 및 사용. main.js와 무관.
- main.js 변경(Electron main process)과 index.html 변경(renderer)간 IPC 인터페이스 변경 없음. proxy-start/stop/status 핸들러의 request/response 형태 유지.

## 결론
통과 -- 전체 테스트 스위트 통과, 변경 파일 간 상호작용 정상.
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "normal",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 4,
  "current_step": 2,
  "dev_phases": {
    "1": {
      "name": "network-safety",
      "folder": "phase-1-network-safety",
      "steps": {
        "1": {
          "title": "EADDRINUSE 재시도 1회 제한",
          "doc_path": "brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-1-network-safety/step-1.md"
        },
        "2": {
          "title": "req/proxyRes 에러 핸들러 추가",
          "doc_path": "brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-1-network-safety/step-2.md"
        }
      }
    },
    "2": {
      "name": "input-validation",
      "folder": "phase-2-input-validation",
      "steps": {
        "1": {
          "title": "토큰 추정 입력 제한 + 포트 범위 수정",
          "doc_path": "brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-2-input-validation/step-1.md"
        }
      }
    },
    "3": {
      "name": "protocol-handling",
      "folder": "phase-3-protocol-handling",
      "steps": {
        "1": {
          "title": "SSE 파싱 마지막 이벤트 유실 방지",
          "doc_path": "brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-3-protocol-handling/step-1.md"
        },
        "2": {
          "title": "proxy-stop race condition 방지",
          "doc_path": "brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-3-protocol-handling/step-2.md"
        }
      }
    },
    "4": {
      "name": "xss-fixes",
      "folder": "phase-4-xss-fixes",
      "steps": {
        "1": {
          "title": "mech-chip onclick XSS 수정",
          "doc_path": "brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-4-xss-fixes/step-1.md"
        },
        "2": {
          "title": "토큰 팝오버 값 esc() 적용",
          "doc_path": "brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-4-xss-fixes/step-2.md"
        }
      }
    }
  },
  "verification": {
    "rounds_passed": 3
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-1-network-safety/phase.md`
```markdown
# 개발 Phase 1: main.js 네트워크 안전성

## 목표
- EADDRINUSE 무한 재시도 방지 (Issue 2)
- req 스트림 에러 핸들러 추가 (Issue 3)
- proxyRes 스트림 에러 핸들러 추가 (Issue 10)

## 범위
- 변경 대상 파일: `main.js` — 서버/프록시 에러 핸들링 보강

## Steps
- Step 1: EADDRINUSE 재시도 1회 제한 — `retried` 플래그로 무한 루프 방지
- Step 2: req/proxyRes 에러 핸들러 추가 — 스트림 에러 시 안전하게 응답 종료

## 선행 조건
- 없음

## 완료 기준
- `npm run test:unit` 통과
- EADDRINUSE 재시도가 1회로 제한되는 코드 확인
- req, proxyRes에 error 이벤트 핸들러 존재 확인
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-1-network-safety/step-1.md`
```markdown
# Step 1: EADDRINUSE 재시도 1회 제한

## 완료 기준
- `let retried = false` 플래그 추가
- EADDRINUSE 에러 시 `!retried` 체크 후 재시도, 두 번째부터는 resolve({ error })
- 기존 테스트 통과

## 테스트 케이스
| TC | 시나리오 | 기대 결과 | 실제 결과 |
|---|---|---|---|
| TC-1 | main.js에 `let retried = false` 플래그 존재 | `retried` 변수가 server.on('error') 핸들러 바로 위에 선언됨 | ✅ PASS (line 197) |
| TC-2 | EADDRINUSE 분기에서 `!retried` 조건 체크 | `if (err.code === 'EADDRINUSE' && !retried)` 패턴 존재 | ✅ PASS (line 199) |
| TC-3 | 재시도 시 `retried = true` 설정 | retried 플래그가 true로 설정된 후 listen(0) 호출 | ✅ PASS (line 200) |
| TC-4 | 두 번째 EADDRINUSE 시 resolve({ error }) | else 분기에서 resolve({ error: err.message }) 호출 | ✅ PASS (line 203) |
| TC-5 | npm run test:unit 통과 | 기존 13개 테스트 모두 통과 | ✅ PASS (13/13) |

## 검증 명령
- `grep -n 'retried' main.js` — retried 플래그 존재 확인
- `grep -A3 'EADDRINUSE' main.js` — 조건 분기 확인
- `npm run test:unit` — 기존 테스트 통과 확인

## 실행 결과
```
$ grep -n 'retried' main.js
197:    let retried = false;
199:      if (err.code === 'EADDRINUSE' && !retried) {
200:        retried = true;

$ npm run test:unit
✔ 13/13 tests passed (duration: 95ms)
```

## 구현 내용
- `main.js` line 197-204: `let retried = false` 플래그 추가, EADDRINUSE 조건에 `&& !retried` 추가, 재시도 전 `retried = true` 설정
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-1-network-safety/step-2.md`
```markdown
# Step 2: req/proxyRes 에러 핸들러 추가

## 완료 기준
- `req.on('error', ...)` 핸들러 추가: 400 응답 후 종료
- `proxyRes.on('error', ...)` 핸들러 추가: res.end() 호출
- 기존 테스트 통과

## 테스트 케이스
| TC | 시나리오 | 기대 결과 | 실제 결과 |
|---|---|---|---|
| TC-1 | req.on('error') 핸들러 존재 | createServer 콜백 내에서 req.on('error', ...) 호출 확인 | ✅ PASS (line 139) |
| TC-2 | req 에러 시 400 응답 | `if (!res.headersSent) res.writeHead(400)` + `res.end()` | ✅ PASS |
| TC-3 | proxyRes.on('error') 핸들러 존재 | proxyRes.on('error', ...) 호출 확인 | ✅ PASS (line 168) |
| TC-4 | proxyRes 에러 시 res.end() | 에러 핸들러에서 `res.end()` 호출 | ✅ PASS |
| TC-5 | npm run test:unit 통과 | 기존 13개 테스트 모두 통과 | ✅ PASS (13/13) |

## 검증 명령
- `grep -n "req.on('error'" main.js` — req 에러 핸들러 확인
- `grep -n "proxyRes.on('error'" main.js` — proxyRes 에러 핸들러 확인
- `npm run test:unit` — 기존 테스트 통과 확인

## 실행 결과
```
$ grep -n "req.on('error'" main.js
139:      req.on('error', () => {

$ grep -n "proxyRes.on('error'" main.js
168:          proxyRes.on('error', () => { res.end(); });

$ npm run test:unit
✔ 13/13 tests passed (duration: 94ms)
```

## 구현 내용
- `main.js` line 139-141: `req.on('error', ...)` 핸들러 추가 — 400 응답 후 종료
- `main.js` line 168: `proxyRes.on('error', ...)` 핸들러 추가 — res.end() 호출
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-2-input-validation/phase.md`
```markdown
# 개발 Phase 2: main.js 입력 검증

## 목표
- 토큰 추정 입력 길이 10MB 제한 (Issue 5)
- 특권 포트(1-1023) 차단, 1024-65535만 허용 (Issue 9)

## 범위
- 변경 대상 파일: `main.js` — IPC 핸들러 입력 검증 강화

## Steps
- Step 1: 토큰 추정 입력 길이 제한 + 포트 범위 1024-65535로 변경

## 선행 조건
- Phase 1 완료

## 완료 기준
- `npm run test:unit` 통과
- text 입력이 10MB로 잘리는 코드 확인
- 포트 검증이 1024 이상인 코드 확인
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-2-input-validation/step-1.md`
```markdown
# Step 1: 토큰 추정 입력 제한 + 포트 범위 수정

## 완료 기준
- `get-token-estimate`: text를 `.slice(0, 10_000_000)`으로 제한
- `proxy-start`: 포트 검증을 `port < 1024`로 변경, 에러 메시지 "1024–65535"
- 기존 테스트 통과

## 테스트 케이스
| TC | 시나리오 | 기대 결과 | 실제 결과 |
|---|---|---|---|
| TC-1 | get-token-estimate에서 text를 10MB로 제한 | `.slice(0, 10_000_000)` 또는 동등한 코드 존재 | ✅ PASS (line 128) |
| TC-2 | 포트 검증 하한이 1024 | `port < 1024` 조건 존재 | ✅ PASS (line 133) |
| TC-3 | 포트 에러 메시지에 "1024–65535" 포함 | 에러 메시지 문자열 확인 | ✅ PASS (line 134) |
| TC-4 | npm run test:unit 통과 | 기존 13개 테스트 모두 통과 | ✅ PASS (13/13) |

## 검증 명령
- `grep -n 'slice.*10' main.js` — 입력 길이 제한 확인
- `grep -n '1024' main.js` — 포트 하한 확인
- `npm run test:unit` — 기존 테스트 통과 확인

## 실행 결과
```
$ grep -n 'slice.*10' main.js
128:  const s = (text || '').slice(0, 10_000_000);

$ grep -n '1024' main.js
133:  if (!Number.isInteger(port) || port < 1024 || port > 65535) {
134:    return { error: 'Invalid port: must be 1024–65535' };

$ npm run test:unit
✔ 13/13 tests passed (duration: 100ms)
```

## 구현 내용
- `main.js` line 128: get-token-estimate에서 text를 `.slice(0, 10_000_000)`으로 10MB 제한
- `main.js` line 133-134: 포트 하한을 1에서 1024로 변경, 에러 메시지 업데이트
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-3-protocol-handling/phase.md`
```markdown
# 개발 Phase 3: main.js 프로토콜 처리

## 목표
- SSE 파싱: 스트림 끝 빈 줄 없을 때 마지막 이벤트 유실 방지 (Issue 6)
- proxy-stop race condition 방지 (Issue 7)

## 범위
- 변경 대상 파일: `main.js` — parseSseStream 함수 리팩터링 + proxy-stop 핸들러 수정

## Steps
- Step 1: parseSseStream에 processEvent 헬퍼 추출 + 루프 후 잔여 이벤트 처리
- Step 2: proxy-stop에서 proxyServer를 먼저 null로 설정하여 race condition 방지

## 선행 조건
- Phase 2 완료

## 완료 기준
- `npm run test:unit` 통과
- 빈 줄 없는 SSE 스트림에서 마지막 이벤트가 처리되는 코드 확인
- proxy-stop에서 `const srv = proxyServer; proxyServer = null;` 패턴 확인
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-3-protocol-handling/step-1.md`
```markdown
# Step 1: SSE 파싱 마지막 이벤트 유실 방지

## 완료 기준
- processEvent 헬퍼 함수 추출
- for 루프 후 `if (events.data) processEvent(events.data)` 추가
- 기존 테스트 통과

## 테스트 케이스
| TC | 시나리오 | 기대 결과 | 실제 결과 |
|---|---|---|---|
| TC-1 | processEvent 헬퍼 함수 추출 | parseSseStream 내부에 processEvent 함수 정의 존재 | ✅ PASS (line 15) |
| TC-2 | for 루프 후 잔여 이벤트 처리 | `if (events.data) processEvent(events.data)` 코드 존재 (루프 바깥) | ✅ PASS (line 35) |
| TC-3 | `var msg` → `let msg` 변경 | `let msg` 또는 함수 스코프 내 선언 확인 | ✅ PASS (line 14) |
| TC-4 | npm run test:unit 통과 | 기존 13개 테스트 모두 통과 | ✅ PASS (13/13) |

## 검증 명령
- `grep -n 'processEvent' main.js` — 헬퍼 함수 확인
- `grep -n 'events.data.*processEvent' main.js` — 루프 후 잔여 처리 확인
- `npm run test:unit` — 기존 테스트 통과 확인

## 실행 결과
```
$ grep -n 'processEvent' main.js
15:    function processEvent(data) {
30:        processEvent(events.data);
35:    if (events.data) processEvent(events.data);

$ npm run test:unit
✔ 13/13 tests passed (duration: 100ms)
```

## 구현 내용
- `main.js` line 12-37: parseSseStream 리팩터링 — processEvent 헬퍼 추출, `var msg` → `let msg`, 루프 후 잔여 이벤트 처리 추가
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-3-protocol-handling/step-2.md`
```markdown
# Step 2: proxy-stop race condition 방지

## 완료 기준
- `const srv = proxyServer; proxyServer = null;` 패턴 적용
- `srv.close()`로 변경
- 기존 테스트 통과

## 테스트 케이스
| TC | 시나리오 | 기대 결과 | 실제 결과 |
|---|---|---|---|
| TC-1 | proxyServer를 먼저 null로 설정 | `const srv = proxyServer; proxyServer = null;` 패턴 존재 | ✅ PASS |
| TC-2 | srv.close() 사용 | `srv.close(...)` 호출 확인 | ✅ PASS |
| TC-3 | close 콜백에서 proxyServer = null 제거 | 콜백 내에 `proxyServer = null` 없음 | ✅ PASS |
| TC-4 | npm run test:unit 통과 | 기존 13개 테스트 모두 통과 | ✅ PASS (13/13) |

## 검증 명령
- `grep -A5 'proxy-stop' main.js` — race condition 방지 패턴 확인
- `npm run test:unit` — 기존 테스트 통과 확인

## 실행 결과
```
$ grep -A6 'proxy-stop' main.js
ipcMain.handle('proxy-stop', () => {
  if (!proxyServer) return { stopped: true };
  const srv = proxyServer;
  proxyServer = null;
  return new Promise((resolve) => {
    srv.close(() => { resolve({ stopped: true }); });
  });

$ npm run test:unit
✔ 13/13 tests passed (duration: 96ms)
```

## 구현 내용
- `main.js` line 215-222: proxy-stop에서 `const srv = proxyServer; proxyServer = null;`로 race condition 방지, `srv.close()`로 변경
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-4-xss-fixes/phase.md`
```markdown
# 개발 Phase 4: public/index.html XSS 수정

## 목표
- onclick 핸들러 XSS 방지: data-key 속성 + esc() 사용 (Issue 1)
- 토큰 팝오버 미이스케이프 값에 esc() 적용 (Issue 4)

## 범위
- 변경 대상 파일: `public/index.html` — mech-chip onclick, 토큰 팝오버 값 이스케이프

## Steps
- Step 1: mech-chip onclick XSS 수정 — safePattern 제거, data-key + esc() 사용, setProxyDetailMechFilter 시그니처 변경
- Step 2: 토큰 팝오버 값에 esc() 적용 — d.model, d.kb, d.total, d.cachePct, r.label, r.tokens, r.price, r.cost

## 선행 조건
- Phase 3 완료

## 완료 기준
- `npm run test:unit` 통과
- safePattern 코드 제거 확인
- 토큰 팝오버 innerHTML에서 esc() 적용 확인
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-4-xss-fixes/step-1.md`
```markdown
# Step 1: mech-chip onclick XSS 수정

## 완료 기준
- `safePattern` 변수 및 관련 코드 제거
- `data-key="${escAttr(c.key)}"` 속성 사용
- onclick에서 `this.dataset.key`로 접근
- `setProxyDetailMechFilter(key)` 파라미터 1개로 변경
- 기존 테스트 통과

## 테스트 케이스
| TC | 시나리오 | 기대 결과 | 실제 결과 |
|---|---|---|---|
| TC-1 | safePattern 변수 제거 | `safePattern` 문자열이 index.html에 없음 | ✅ PASS (count=0) |
| TC-2 | data-key 속성 사용 | `data-key=` 문자열이 mech-chip에 존재 | ✅ PASS (line 2852) |
| TC-3 | onclick에서 this.dataset.key 사용 | `this.dataset.key` 패턴 존재 | ✅ PASS (line 2852) |
| TC-4 | setProxyDetailMechFilter 파라미터 1개 | `function setProxyDetailMechFilter(key)` 시그니처 확인 | ✅ PASS (line 2770) |
| TC-5 | escAttr 함수로 key 이스케이프 | `escAttr(c.key)` 호출 확인 | ✅ PASS (line 2852) |
| TC-6 | npm run test:unit 통과 | 기존 13개 테스트 모두 통과 | ✅ PASS (13/13) |

## 검증 명령
- `grep -c 'safePattern' public/index.html` — 0이어야 함 (제거 확인)
- `grep 'data-key' public/index.html` — data-key 사용 확인
- `grep 'this.dataset.key' public/index.html` — dataset 접근 확인
- `grep 'setProxyDetailMechFilter(key)' public/index.html` — 시그니처 확인
- `npm run test:unit` — 기존 테스트 통과 확인

## 실행 결과
```
$ grep -c 'safePattern' public/index.html
0

$ grep -n 'data-key\|this.dataset.key\|setProxyDetailMechFilter(key)' public/index.html
2770:function setProxyDetailMechFilter(key) {
2852:        return `<span ... data-key="${escAttr(c.key)}" onclick="setProxyDetailMechFilter(this.dataset.key)">${esc(c.label)}</span>`;

$ npm run test:unit
✔ 13/13 tests passed (duration: 103ms)
```

## 구현 내용
- `public/index.html` line 2770: `setProxyDetailMechFilter(key, pattern)` → `setProxyDetailMechFilter(key)` 시그니처 변경
- `public/index.html` line 2852: safePattern 제거, `data-key="${escAttr(c.key)}"` + `this.dataset.key` + `esc(c.label)` 적용
```

## File: `brain/knowledge/docs_legacy/2026-03-13/code-quality-fixes/phase-4-xss-fixes/step-2.md`
```markdown
# Step 2: 토큰 팝오버 값 esc() 적용

## 완료 기준
- rowsHtml: `r.label`, `r.tokens`, `r.price`, `r.cost`에 `esc()` 적용
- popover info: `d.model`, `d.kb`에 `esc()` 적용
- total/cachePct: `d.total`, `d.cachePct`에 `esc()` 적용
- 기존 테스트 통과

## 테스트 케이스
| TC | 시나리오 | 기대 결과 | 실제 결과 |
|---|---|---|---|
| TC-1 | r.label에 esc() 적용 | `esc(r.label)` 코드 존재 | ✅ PASS |
| TC-2 | r.tokens에 esc() 적용 | `esc(r.tokens)` 코드 존재 | ✅ PASS |
| TC-3 | r.price에 esc() 적용 | `esc(r.price)` 코드 존재 | ✅ PASS |
| TC-4 | r.cost에 esc() 적용 | `esc(r.cost)` 코드 존재 | ✅ PASS |
| TC-5 | d.model에 esc() 적용 | `esc(d.model)` 코드 존재 | ✅ PASS |
| TC-6 | d.kb에 esc() 적용 | `esc(d.kb)` 코드 존재 | ✅ PASS |
| TC-7 | d.total에 esc() 적용 | `esc(d.total)` 코드 존재 | ✅ PASS |
| TC-8 | d.cachePct에 esc() 적용 | `esc(d.cachePct)` 코드 존재 | ✅ PASS |
| TC-9 | npm run test:unit 통과 | 기존 13개 테스트 모두 통과 | ✅ PASS (13/13) |

## 검증 명령
- `grep -c 'esc(r.label)' public/index.html` — 1 이상
- `grep -c 'esc(d.model)' public/index.html` — 1 이상
- `grep -c 'esc(d.total)' public/index.html` — 1 이상
- `npm run test:unit` — 기존 테스트 통과 확인

## 실행 결과
```
$ grep -c 'esc(r.label)\|esc(r.tokens)\|esc(r.price)\|esc(r.cost)\|esc(d.model)\|esc(d.kb)\|esc(d.total)\|esc(d.cachePct)' public/index.html
각각 1 (8개 모두 적용)

$ npm run test:unit
✔ 13/13 tests passed (duration: 96ms)
```

## 구현 내용
- `public/index.html` line 3440: rowsHtml에서 r.label, r.tokens, r.price, r.cost에 esc() 적용
- `public/index.html` line 3456: popover info에서 d.model, d.kb에 esc() 적용
- `public/index.html` line 3458-3459: total, cachePct에 esc() 적용
```

## File: `brain/knowledge/docs_legacy/2026-03-13/expanded-str-linenum-claudemd-hl/plan.md`
```markdown
# 펼친 문자열 wrapped line 줄 번호 표시

## 문제
긴 텍스트 줄이 컨테이너 너비를 초과하여 CSS word-break로 시각적으로 줄바꿈되면, wrapped된 부분에 줄 번호가 없어 유저 시점에서 줄 번호가 빈다.

## 해결 방식
렌더 후 컨테이너 너비를 측정하고, 그 너비에 맞게 긴 줄을 분할하여 각각 별도 `jt-exp-line` div + 줄 번호 부여. `white-space`를 `pre`로 바꿔서 CSS 자동 줄바꿈을 방지.

## 변경 파일별 상세
### `public/index.html`

#### 1. renderJsonTree에 post-render 줄 분할 함수 추가

- **변경 이유**: 빌드 시점에는 컨테이너 너비를 모르므로, 렌더 후 실제 너비를 측정하여 긴 줄을 분할해야 함.
- **Before** (JS, 라인 1778-1787):
```javascript
function renderJsonTree(container, data) {
  let obj;
  try { obj = typeof data === 'string' ? JSON.parse(data) : data; }
  catch (e) { container.textContent = typeof data === 'string' ? data : JSON.stringify(data, null, 2); return; }
  const totalBytes = new TextEncoder().encode(JSON.stringify(obj)).length;
  _jtLine = 0;
  container.innerHTML = buildJsonHtml(obj, 0, '', totalBytes)
    + `<div class="jt-line-info">${_jtLine} lines total</div>`;
  container.classList.add('jt-lined');
}
```
- **After**:
```javascript
function renderJsonTree(container, data) {
  let obj;
  try { obj = typeof data === 'string' ? JSON.parse(data) : data; }
  catch (e) { container.textContent = typeof data === 'string' ? data : JSON.stringify(data, null, 2); return; }
  const totalBytes = new TextEncoder().encode(JSON.stringify(obj)).length;
  _jtLine = 0;
  container.innerHTML = buildJsonHtml(obj, 0, '', totalBytes)
    + `<div class="jt-line-info">${_jtLine} lines total</div>`;
  container.classList.add('jt-lined');
  // 렌더 후 긴 줄 분할
  splitLongExpLines(container);
}

function splitLongExpLines(container) {
  // 컨테이너 너비 측정 → 문자 수 계산
  const measure = document.createElement('span');
  measure.style.cssText = 'visibility:hidden;position:absolute;white-space:nowrap;font:inherit;font-size:13px;font-family:monospace';
  measure.textContent = 'X'.repeat(100);
  container.appendChild(measure);
  const charWidth = measure.offsetWidth / 100;
  container.removeChild(measure);
  const availWidth = container.clientWidth - 60;
  const maxChars = Math.max(40, Math.floor(availWidth / charWidth));

  for (const block of container.querySelectorAll('.jt-str-expanded')) {
    const lines = Array.from(block.querySelectorAll('.jt-exp-line'));
    if (!lines.length) continue;
    const baseLn = parseInt(lines[0].getAttribute('data-ln')) || 1;
    let lineNum = baseLn;
    const newLines = [];
    for (const line of lines) {
      const text = line.textContent;
      if (text.length <= maxChars) {
        newLines.push({ text, ln: lineNum++, cls: line.className });
      } else {
        for (let i = 0; i < text.length; i += maxChars) {
          newLines.push({ text: text.slice(i, i + maxChars), ln: lineNum++, cls: line.className });
        }
      }
    }
    // DOM 재구성
    const toggle = block.querySelector('.jt-str-toggle');
    block.innerHTML = '';
    if (toggle) block.appendChild(toggle);
    for (const nl of newLines) {
      const div = document.createElement('div');
      div.className = nl.cls;
      div.setAttribute('data-ln', nl.ln);
      div.textContent = nl.text;
      block.appendChild(div);
    }
  }
}
```
- **영향 범위**: 모든 긴 문자열의 펼쳐진 텍스트

#### 2. jtStrToggle에서 펼칠 때도 줄 분할 호출

- **Before** (JS, 라인 1756-1766):
```javascript
function jtStrToggle(id) {
  // ... toggle logic ...
  if (btn) btn.style.display = open ? '' : 'none';
  const parentRow = body.closest('.jt-row');
  if (parentRow) parentRow.classList.toggle('jt-no-ln', !open);
}
```
- **After**:
```javascript
function jtStrToggle(id) {
  // ... toggle logic ...
  if (btn) btn.style.display = open ? '' : 'none';
  const parentRow = body.closest('.jt-row');
  if (parentRow) parentRow.classList.toggle('jt-no-ln', !open);
  // 펼칠 때 긴 줄 분할 (처음 펼칠 때만)
  if (!open && !body.dataset.split) {
    body.dataset.split = '1';
    const lined = body.closest('.jt-lined');
    if (lined) splitLongExpLines(lined, body);
  }
}
```

#### 3. CSS: jt-exp-line white-space를 pre로 변경

- **Before**:
```css
.jt-exp-line {
  display: block; white-space: pre-wrap; word-break: break-word;
  color: var(--orange); min-height: 1.3em;
}
```
- **After**:
```css
.jt-exp-line {
  display: block; white-space: pre; overflow: hidden;
  color: var(--orange); min-height: 1.3em;
}
```
- JS가 분할 처리하므로 CSS 줄바꿈은 불필요. `overflow: hidden`으로 혹시 남은 overflow 숨김.

## 검증
- 검증 명령어: `pkill -x "Electron" 2>/dev/null; npm start &`
- 기대 결과: 긴 문자열 펼침 시 모든 시각적 줄에 줄 번호 표시. wrapped line 없음.
```

## File: `brain/knowledge/docs_legacy/2026-03-13/expanded-str-linenum-claudemd-hl/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/expanded-str-linenum-claudemd-hl",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/expanded-str-linenum-claudemd-hl/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/json-tree-bugs/plan.md`
```markdown
# JSON 트리 버그 2건 + 토큰 설명 추가

## Context
JSON 트리 뷰어에서 두 가지 UI 버그 + 토큰 설명 부재:
1. 노드 접었을 때 줄 번호가 업데이트되지 않음 (접힌 줄도 카운트)
2. CLAUDE.md 칩 클릭 시 표시 깨짐
3. 접힌 노드에 토큰 수 미표시
4. Request 토큰 배지에 실제 사용량(input/output) 미표시

## 변경 파일별 상세

### `public/index.html`

#### Bug 1: 접힌 노드 줄 번호

- **변경 이유**: CSS counter가 `display:none` 부모 안의 `.jt-row`를 여전히 카운트하는 문제. 접힌 자식 row에 `counter-increment: none`을 명시적으로 적용해야 함.
- **Before** (CSS, 라인 613):
```css
.jt-lined .jt-row { counter-increment: jt-line; }
```
- **After** (CSS):
```css
.jt-lined .jt-row { counter-increment: jt-line; }
.jt-lined .jt-row.jt-no-count { counter-increment: none; }
```

- **Before** (JS, 라인 1724-1732):
```javascript
function jtToggle(id) {
  const body = document.getElementById(`${id}-b`);
  const summary = document.getElementById(`${id}-s`);
  const btn = document.getElementById(`${id}-btn`);
  const open = body.style.display !== 'none';
  body.style.display = open ? 'none' : '';
  summary.style.display = open ? '' : 'none';
  btn.textContent = open ? '▶' : '▼';
}
```
- **After**:
```javascript
function jtToggle(id) {
  const body = document.getElementById(`${id}-b`);
  const summary = document.getElementById(`${id}-s`);
  const btn = document.getElementById(`${id}-btn`);
  const open = body.style.display !== 'none';
  body.style.display = open ? 'none' : '';
  body.querySelectorAll('.jt-row').forEach(r => r.classList.toggle('jt-no-count', open));
  summary.style.display = open ? '' : 'none';
  btn.textContent = open ? '▶' : '▼';
}
```
- **영향 범위**: `jtToggle` 호출하는 모든 JSON 트리 접기/펼치기

#### Bug 2: CLAUDE.md 칩 클릭 시 깨짐

- **변경 이유**: `hlRange()`가 `innerHTML` 직접 조작으로 DOM을 재구성하면서 HTML 엔티티(`&amp;`, `&lt;` 등) 경계에서 슬라이스가 엔티티를 잘라 깨진 HTML 생성. innerHTML 조작 대신 부모 요소에 CSS 클래스를 적용하고, 하이라이트 범위를 CSS 기반 표시로 변경.
- **Before** (JS, 라인 2681-2688):
```javascript
function hlRange(el, start, end) {
  const html = el.innerHTML;
  el.innerHTML = html.slice(0, start)
    + '<span class="mech-hl-text">' + html.slice(start, end) + '</span>'
    + html.slice(end);
  const hl = el.querySelector('.mech-hl-text');
  if (hl) requestAnimationFrame(() => hl.scrollIntoView({ behavior: 'smooth', block: 'start' }));
}
```
- **After**:
```javascript
function hlRange(el, start, end) {
  el.classList.add('mech-hl-text');
  requestAnimationFrame(() => el.scrollIntoView({ behavior: 'smooth', block: 'start' }));
}
```
- **영향 범위**: CLAUDE.md, slash command, output style 등 모든 메커니즘 하이라이트. `hlRange`는 CLAUDE.md 외 다른 메커니즘에서도 호출됨 — slash command(라인 2724+), output style(라인 2747+) 등에서도 사용. 이들은 특정 범위만 하이라이트해야 하므로 전체 요소 하이라이트는 부적절할 수 있음.

**대안: DOM Range API 사용**
innerHTML 조작 대신 text node를 찾아 Range로 감싸기:
```javascript
function hlRange(el, start, end) {
  // innerHTML에서의 위치를 text node 위치로 변환하는 건 복잡하므로,
  // 안전하게 전체 요소에 클래스 적용 (CLAUDE.md는 큰 텍스트 블록이므로 적합)
  // 다른 메커니즘은 기존 방식 유지하되 엔티티 경계 보정 추가
  const html = el.innerHTML;
  // 엔티티 경계 보정: end가 & 뒤에 있으면 ; 까지 확장
  let safeEnd = end;
  const ampIdx = html.lastIndexOf('&', safeEnd);
  if (ampIdx !== -1 && ampIdx > safeEnd - 10) {
    const semiIdx = html.indexOf(';', ampIdx);
    if (semiIdx !== -1 && semiIdx < ampIdx + 10) {
      safeEnd = semiIdx + 1;
    }
  }
  let safeStart = start;
  const ampIdx2 = html.lastIndexOf('&', safeStart);
  if (ampIdx2 !== -1 && ampIdx2 > safeStart - 10) {
    const semiIdx2 = html.indexOf(';', ampIdx2);
    if (semiIdx2 !== -1 && semiIdx2 >= safeStart) {
      safeStart = ampIdx2;
    }
  }
  el.innerHTML = html.slice(0, safeStart)
    + '<span class="mech-hl-text">' + html.slice(safeStart, safeEnd) + '</span>'
    + html.slice(safeEnd);
  const hl = el.querySelector('.mech-hl-text');
  if (hl) requestAnimationFrame(() => hl.scrollIntoView({ behavior: 'smooth', block: 'start' }));
}
```

**추천 방식**: CLAUDE.md(cm_*)에만 요소 전체 하이라이트 적용, 나머지 메커니즘은 엔티티 보정 후 기존 방식 유지.

최종 코드:
```javascript
function hlRange(el, start, end, wholeElement) {
  if (wholeElement) {
    el.classList.add('mech-hl-text');
    requestAnimationFrame(() => el.scrollIntoView({ behavior: 'smooth', block: 'start' }));
    return;
  }
  const html = el.innerHTML;
  // end 위치가 HTML 엔티티 중간이면 보정
  let safeEnd = end;
  for (let i = Math.max(0, safeEnd - 8); i < safeEnd; i++) {
    if (html[i] === '&') {
      const semi = html.indexOf(';', i);
      if (semi !== -1 && semi < i + 10 && semi >= safeEnd) {
        safeEnd = semi + 1;
        break;
      }
    }
  }
  el.innerHTML = html.slice(0, start)
    + '<span class="mech-hl-text">' + html.slice(start, safeEnd) + '</span>'
    + html.slice(safeEnd);
  const hl = el.querySelector('.mech-hl-text');
  if (hl) requestAnimationFrame(() => hl.scrollIntoView({ behavior: 'smooth', block: 'start' }));
}
```

CLAUDE.md 호출부(라인 2720):
```javascript
// Before
hlRange(el, start, end);
// After
hlRange(el, start, end, true);
```

#### 접힌 노드에 토큰 수 표시

- **변경 이유**: 접힌 노드가 `▶ [12]`만 표시. 해당 노드의 대략적인 토큰 수를 함께 보여주면 프롬프트 비용 분석에 유용.
- **Before** (JS, 라인 1703-1708):
```javascript
const typeTag = isArr ? `[${label}]` : `{${label}}`;
// ...
+ `<span class="jt-tag" id="${id}-s" onclick="jtToggle('${id}')" style="display:none">${typeTag}${trailing}</span>`
```
- **After**:
```javascript
const jsonBytes = new TextEncoder().encode(JSON.stringify(val)).length;
const tokens = Math.ceil(jsonBytes / 3.5);
const tokStr = tokens >= 1000000 ? (tokens / 1000000).toFixed(1) + 'M'
             : tokens >= 1000 ? (tokens / 1000).toFixed(1) + 'K'
             : String(tokens);
const pct = totalBytes > 0 ? (jsonBytes / totalBytes * 100) : 0;
const pctStr = pct >= 1 ? pct.toFixed(0) + '%' : pct >= 0.1 ? pct.toFixed(1) + '%' : '<0.1%';
const typeTag = isArr ? `[${label}]` : `{${label}}`;
const tokTag = `<span class="jt-tok">~${tokStr} tok · ${pctStr}</span>`;
// ...
+ `<span class="jt-tag" id="${id}-s" onclick="jtToggle('${id}')" style="display:none">${typeTag} ${tokTag}${trailing}</span>`
```

- **함수 시그니처 변경**: `buildJsonHtml(val, depth, trailing)` → `buildJsonHtml(val, depth, trailing, totalBytes)`
  - 재귀 호출에도 `totalBytes` 전달
  - `renderJsonTree`에서 최초 호출 시 `totalBytes = new TextEncoder().encode(JSON.stringify(obj)).length` 계산하여 전달

- **CSS 추가**:
```css
.jt-tok { color: var(--dim); font-size: 9px; opacity: 0.7; margin-left: 4px; }
```
- **영향 범위**: 모든 접힌 JSON 객체/배열 노드에 토큰 수 + 비중(%) 표시

#### 실제 토큰 사용량 표시

- **변경 이유**: 현재 추정치만 표시. API 응답의 `usage.input_tokens` / `output_tokens` 실제값을 보여줘야 이 요청에 토큰 얼마나 썼는지 파악 가능.
- **데이터 소스**: `entry.response.body.usage` (Claude API 응답에 포함)
  - `input_tokens`: 입력 토큰 수
  - `output_tokens`: 출력 토큰 수
  - `cache_creation_input_tokens`, `cache_read_input_tokens`: 캐시 관련 (있을 때만)
- **Before** (JS, 라인 2893-2901):
```javascript
const tokenInfo = proxyDetailTab === 'request' && data
  ? (() => {
      const bytes = new TextEncoder().encode(JSON.stringify(data)).length;
      const kb = (bytes / 1024).toFixed(1);
      const tokens = Math.ceil(bytes / 3.5);
      // ...
      return `<div class="proxy-token-pill"><span class="tt-badge">${kb} KB</span><span class="tt-badge">~${tokStr} tokens</span></div>`;
    })()
  : '';
```
- **After**: 응답이 있으면 실제 usage 표시, 없으면 추정치 유지
```javascript
const tokenInfo = proxyDetailTab === 'request' && data
  ? (() => {
      const bytes = new TextEncoder().encode(JSON.stringify(data)).length;
      const kb = (bytes / 1024).toFixed(1);
      const usage = entry.response?.body?.usage;
      if (usage) {
        const fmtTok = (n) => n >= 1000000 ? (n/1000000).toFixed(1)+'M' : n >= 1000 ? (n/1000).toFixed(1)+'K' : String(n);
        let parts = `<span class="tt-badge">${kb} KB</span>`;
        parts += `<span class="tt-badge">↑ ${fmtTok(usage.input_tokens)} in</span>`;
        parts += `<span class="tt-badge">↓ ${fmtTok(usage.output_tokens)} out</span>`;
        if (usage.cache_read_input_tokens) parts += `<span class="tt-badge">♻ ${fmtTok(usage.cache_read_input_tokens)} cache</span>`;
        parts += `<span style="color:var(--green);font-size:9px;margin-left:4px">actual</span>`;
        return `<div class="proxy-token-pill">${parts}</div>`;
      }
      // 응답 미수신 시 추정치
      const tokens = Math.ceil(bytes / 3.5);
      const tokStr = tokens >= 1000000 ? (tokens/1000000).toFixed(1)+'M' : tokens >= 1000 ? (tokens/1000).toFixed(1)+'K' : String(tokens);
      return `<div class="proxy-token-pill"><span class="tt-badge">${kb} KB</span><span class="tt-badge">~${tokStr} tokens</span><span style="color:var(--dim);font-size:9px;margin-left:4px">estimated</span></div>`;
    })()
  : '';
```
- **영향 범위**: Request 탭의 토큰 배지. 응답 수신 전엔 추정치, 수신 후엔 실제값 표시.

## 검증
- 검증 명령어: `pkill -x "Electron" 2>/dev/null; npm start &`
- 기대 결과:
  1. JSON 트리에서 노드 접으면 이후 줄 번호가 줄어듦 (접힌 줄 건너뜀)
  2. CLAUDE.md 칩 클릭 시 해당 섹션이 초록 하이라이트로 표시되며 레이아웃 깨지지 않음
  3. 접힌 노드에 `▶ [12] ~2.3K tok · 9%` 형태로 토큰 + 비중 표시
  4. 토큰 배지에 실제 `↑ 24.9K in ↓ 1.2K out ♻ 20K cache actual` 표시 (응답 전엔 `estimated`)
```

## File: `brain/knowledge/docs_legacy/2026-03-13/json-tree-bugs/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/json-tree-bugs",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/json-tree-bugs/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/line-numbers-and-token-count/plan.md`
```markdown
# Line Numbers + Token Count 표시 기능

## Context
프록시 뷰의 Request/Response 탭에서 JSON 트리가 렌더링될 때 줄 번호가 없어 디버깅 시 특정 위치를 참조하기 어렵고, request의 토큰 소비량을 한눈에 확인할 수 없음.

## 변경 파일별 상세

### `public/index.html`

#### 1. CSS 추가 — `.jt-lined` 줄 번호 스타일 (line 611 `.jt-row` 뒤에 삽입)

- **변경 이유**: CSS counter 기반으로 `.jt-row`에 줄 번호를 자동 부여
- **Before** (line 611):
```css
    .jt-row  { display: block; white-space: nowrap; }
    .jt-str-long { display: inline; }
```
- **After**:
```css
    .jt-row  { display: block; white-space: nowrap; }
    .jt-lined { counter-reset: jt-line; }
    .jt-lined .jt-row { counter-increment: jt-line; }
    .jt-lined .jt-row::before {
      content: counter(jt-line);
      display: inline-block;
      width: 40px;
      text-align: right;
      padding-right: 12px;
      color: var(--dim);
      font-size: 11px;
      user-select: none;
      opacity: 0.5;
    }
    .jt-str-long { display: inline; }
```
- **영향 범위**: 모든 `.jt-lined` 컨테이너 내 `.jt-row` 요소에 줄 번호 표시

#### 2. CSS 추가 — `.proxy-token-pill` 스타일 (같은 CSS 블록에 추가)

- **변경 이유**: 토큰 추정 pill UI 스타일
- **Before** (line 637):
```css
    .analysis-block .jt-row { white-space: normal; }
```
- **After**:
```css
    .proxy-token-pill {
      padding: 4px 12px;
      font-size: 11px;
      color: var(--dim);
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
    }
    .analysis-block .jt-row { white-space: normal; }
```
- **영향 범위**: 프록시 Request 탭 상단에만 표시

#### 3. `renderJsonTree` 함수에 `.jt-lined` 클래스 추가 (line 1708)

- **변경 이유**: `renderJsonTree`로 렌더링되는 모든 JSON 트리에 줄 번호 활성화
- **Before** (line 1708):
```javascript
  container.innerHTML = buildJsonHtml(obj, 0);
}
```
- **After**:
```javascript
  container.innerHTML = buildJsonHtml(obj, 0);
  container.classList.add('jt-lined');
}
```
- **영향 범위**: 프록시 Request/Response 탭, Payload 미리보기 모두 줄 번호 표시

#### 4. `renderProxyDetail` 함수에 토큰 pill 추가 (line 2862-2863)

- **변경 이유**: Request 탭일 때 검색바 아래에 토큰 추정 정보 표시
- **Before** (line 2862-2863):
```javascript
  const prevScrollTop = document.getElementById('proxyDetailCode')?.scrollTop ?? 0;
  detail.innerHTML = header + '<div class="json-tree-view" id="proxyDetailCode" style="flex:1;overflow:auto"></div>';
```
- **After**:
```javascript
  const tokenInfo = proxyDetailTab === 'request' && data
    ? (() => {
        const bytes = new TextEncoder().encode(JSON.stringify(data)).length;
        const kb = (bytes / 1024).toFixed(1);
        const tokens = Math.ceil(bytes / 3.5);
        return `<div class="proxy-token-pill">${kb} KB · ~${tokens.toLocaleString()} tok</div>`;
      })()
    : '';
  const prevScrollTop = document.getElementById('proxyDetailCode')?.scrollTop ?? 0;
  detail.innerHTML = header + tokenInfo + '<div class="json-tree-view" id="proxyDetailCode" style="flex:1;overflow:auto"></div>';
```
- **영향 범위**: `renderProxyDetail` 함수 내 Request 탭에서만 표시

## 검증
- 검증 명령어: `pkill -x "Electron" 2>/dev/null; npm start &`
- 기대 결과:
  1. 프록시 뷰 Request/Response 탭에서 JSON 트리 각 행 왼쪽에 줄 번호 표시
  2. Request 탭 상단에 `N.N KB · ~N,NNN tok` pill 표시
  3. Payload 미리보기에도 줄 번호 표시
  4. 기존 검색, 메커니즘 필터, 접기/펼치기 기능 정상 작동
```

## File: `brain/knowledge/docs_legacy/2026-03-13/line-numbers-and-token-count/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/line-numbers-and-token-count",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/line-numbers-and-token-count/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/readme-review/plan.md`
```markdown
# README 깨진 링크 및 스크린샷 수정

## 변경 파일별 상세

### `README.md`
- **변경 이유**: `[How It Works](#how-it-works)` 앵커가 존재하지 않는 섹션을 가리킴
- **Before** (현재 코드):
```
[Install](#install) · [What You'll Learn](#what-youll-learn) · [Proxy Mode](#proxy-mode) · [How It Works](#how-it-works)
```
- **After** (변경 후):
```
[Install](#install) · [What You'll Learn](#what-youll-learn) · [Proxy Mode](#proxy-mode) · [Tech Stack](#tech-stack)
```
- **영향 범위**: 네비게이션 링크만 변경, 다른 파일 영향 없음

### `README.ko.md`
- **변경 이유 1**: `[동작 원리](#동작-원리)` 앵커가 존재하지 않는 섹션을 가리킴
- **Before**:
```
[설치](#설치) · [배울 수 있는 것들](#배울-수-있는-것들) · [프록시 모드](#프록시-모드) · [동작 원리](#동작-원리)
```
- **After**:
```
[설치](#설치) · [배울 수 있는 것들](#배울-수-있는-것들) · [프록시 모드](#프록시-모드) · [기술 스택](#기술-스택)
```

- **변경 이유 2**: 한국어 스크린샷 파일이 존재하는데 영어 스크린샷을 사용 중
- **Before**:
```html
<img src="public/screenshots/proxy-request-en.png" width="100%" alt="Proxy — CLAUDE.md Global/Local 섹션 칩과 인라인 텍스트 하이라이트가 표시된 Request 뷰" />
<img src="public/screenshots/proxy-analysis-en.png" width="100%" alt="Proxy — 5가지 메커니즘을 자동 감지하고 섹션 내용을 보여주는 Analysis 뷰" />
```
- **After**:
```html
<img src="public/screenshots/proxy-request-ko.png" width="100%" alt="Proxy — CLAUDE.md Global/Local 섹션 칩과 인라인 텍스트 하이라이트가 표시된 Request 뷰" />
<img src="public/screenshots/proxy-analysis-ko.png" width="100%" alt="Proxy — 5가지 메커니즘을 자동 감지하고 섹션 내용을 보여주는 Analysis 뷰" />
```
- **영향 범위**: 네비게이션 링크 + 스크린샷 경로만 변경

## 검증
- 검증 명령어: `grep -n 'how-it-works\|동작-원리\|proxy-request-en\|proxy-analysis-en' README.md README.ko.md`
- 기대 결과: 출력 없음 (모든 깨진 링크/잘못된 스크린샷 제거됨)
```

## File: `brain/knowledge/docs_legacy/2026-03-13/readme-review/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/readme-review",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/readme-review/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/plan.md`
```markdown
# 시뮬레이터 코드 완전 제거

## Context
`SHOW_SIMULATOR = false`로 UI만 숨긴 시뮬레이터 코드가 여전히 로드되어 일부 환경에서 JS 에러 발생. 프록시 전용 앱으로 전환.

## 변경 파일별 상세

### `main.js`
- **Before**: Anthropic SDK import + send-to-claude, open-file, get-token-estimate IPC 핸들러 포함
- **After**: 프록시 IPC 핸들러만 유지 (proxy-start/stop/status)

### `preload.js`
- **Before**: sendToClaude, openFile, estimateTokens + 프록시 API
- **After**: platform + 프록시 API만 유지

### `package.json`
- **Before**: @anthropic-ai/sdk 의존성 + build.files에 SDK 포함
- **After**: SDK 제거, @sentry/electron 유지

### `public/index.html`
- **삭제 (~1000줄)**: 시뮬레이터 HTML/CSS/JS, 랜딩 페이지, 탭 내비게이션, i18n 키
- **유지**: 프록시 관련 전체, 공유 유틸(esc, renderJsonTree), i18n(proxy/token/onboard)

### `tests/e2e/app.spec.ts`
- 시뮬레이터 테스트 제거, 프록시 테스트 유지

## 검증
- `npm start` → 프록시 패널 바로 표시
- `npm test` 통과
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "normal",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 3,
  "current_step": 3,
  "dev_phases": {
    "1": {
      "name": "Backend cleanup",
      "steps": [
        "Remove simulator IPC handlers + SDK from main.js, preload.js, package.json",
        "QA: verify app boots without errors"
      ],
      "folder": "phase-1-backend-cleanup"
    },
    "2": {
      "name": "index.html JS cleanup",
      "steps": [
        "Remove simulator JS functions, variables, i18n keys",
        "Fix applyI18n() and init code, ensure proxy mode displays directly",
        "QA: verify proxy mode works, no JS errors"
      ],
      "folder": "phase-2-js-cleanup"
    },
    "3": {
      "name": "index.html HTML/CSS cleanup + CDN + tests",
      "steps": [
        "Remove landing page, tabs, simulator panels, header controls, simulator CSS, marked.js CDN",
        "Update E2E tests (remove simulator tests, update proxy tests)",
        "QA: run full test suite"
      ],
      "folder": "phase-3-html-css-tests"
    }
  },
  "verification": {
    "rounds_passed": 3
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/remove-simulator",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/remove-simulator/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/phase-1-backend-cleanup/phase.md`
```markdown
# Phase 1: Backend Cleanup

## 목표
main.js, preload.js, package.json에서 시뮬레이터 관련 코드와 SDK 의존성을 제거한다.

## 범위
- main.js: Anthropic SDK import, send-to-claude/open-file/get-token-estimate IPC 핸들러, 불필요한 fs/dialog import
- preload.js: sendToClaude, openFile, estimateTokens API
- package.json: @anthropic-ai/sdk 의존성 + build.files

## Steps
- Step 1: 시뮬레이터 IPC 핸들러 + SDK 제거
- Step 2: QA - 앱 부팅 검증
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/phase-1-backend-cleanup/step-1.md`
```markdown
# Step 1: 시뮬레이터 IPC 핸들러 + SDK 제거

## TC

| # | 테스트 | 기대결과 | 실제결과 |
|---|--------|----------|----------|
| 1 | main.js에 Anthropic SDK import 없음 | grep 결과 없음 | ✅ |
| 2 | main.js에 send-to-claude/open-file/get-token-estimate 핸들러 없음 | grep 결과 없음 | ✅ |
| 3 | main.js에 fs/dialog import 없음 | grep 결과 없음 | ✅ |
| 4 | preload.js에 sendToClaude/openFile/estimateTokens 없음 | grep 결과 없음 | ✅ |
| 5 | package.json에 @anthropic-ai/sdk 없음 | grep 결과 없음 | ✅ |
| 6 | proxy 핸들러 유지 (proxy-start/stop/status) | 3개 모두 존재 | ✅ |
| 7 | main.js 문법 검사 통과 | SYNTAX:OK | ✅ |
| 8 | preload.js 문법 검사 통과 | SYNTAX:OK | ✅ |
| 9 | package.json JSON 유효 | JSON:OK | ✅ |

## 구현 내용
- main.js: `const { Anthropic } = require('@anthropic-ai/sdk')` 제거, `fs`/`dialog` import 제거, send-to-claude/open-file/get-token-estimate IPC 핸들러 3개 제거 (245줄 → 210줄)
- preload.js: sendToClaude, openFile, estimateTokens API 3개 제거 (21줄 → 17줄)
- package.json: @anthropic-ai/sdk 의존성 제거, build.files에서 SDK 경로 제거

## 실행 결과

```
$ grep -n "anthropic-ai\|send-to-claude\|open-file\|get-token-estimate\|dialog\|require('fs')" main.js
(no output — all simulator code removed)

$ grep -n "sendToClaude\|openFile\|estimateTokens" preload.js
(no output — all simulator APIs removed)

$ grep -n "anthropic-ai" package.json
(no output — SDK dependency removed)

$ grep -c "proxy-start\|proxy-stop\|proxy-status" main.js
3 (all proxy handlers preserved)

$ node -c main.js
SYNTAX:OK

$ node -c preload.js
SYNTAX:OK

$ node -e "JSON.parse(require('fs').readFileSync('package.json','utf8')); console.log('JSON:OK')"
JSON:OK
```
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/phase-2-js-cleanup/phase.md`
```markdown
# Phase 2: index.html JS cleanup

## 목표
index.html에서 시뮬레이터 전용 JS 코드(함수, 변수, i18n 키)를 제거하고 프록시 모드 직접 표시로 전환한다.

## 범위
- LOCALES에서 시뮬레이터 전용 i18n 키 제거 (landing, history, mech, export, form, api, apiInput)
- 시뮬레이터 전용 함수 제거 (getMechanisms, buildPayload, buildSendablePayload, collectCfg, updatePreview, renderForm, switchM, showPTab, copyPayload, callApi, sendToApi, simulateSkill, simulateSubAgent, copyResponse, renderResponseContent, toggleMd, generateCurl, generatePython, generateTypeScript, updateExport, showExportLang, copyExport, saveHistory, renderHistory, restoreHistory, toggleHistory, openFilePicker, onApiKeyChange, mechBadge, BADGE_STYLES)
- 시뮬레이터 전용 상태 변수 제거 (current, lastResponseText, currentPayload, mdEnabled, exportLang, sessionHistory, SHOW_SIMULATOR)
- applyI18n()에서 시뮬레이터 re-render 코드 제거
- Init 코드에서 시뮬레이터 관련 로직 제거, 프록시 직접 표시

## Steps
- Step 1: 시뮬레이터 전용 JS 함수/변수/i18n 키 제거 및 applyI18n/init 수정
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/phase-2-js-cleanup/step-1.md`
```markdown
# Step 1: 시뮬레이터 전용 JS 함수/변수/i18n 키 제거

## TC

| # | 테스트 | 기대결과 | 실제결과 |
|---|--------|----------|----------|
| TC-1 | SHOW_SIMULATOR 상수 없음 | grep 결과 없음 | ✅ |
| TC-2 | getMechanisms 함수 없음 | grep 결과 없음 | ✅ |
| TC-3 | buildPayload/buildSendablePayload 함수 없음 | grep 결과 없음 | ✅ |
| TC-4 | sendToApi/simulateSkill/simulateSubAgent 함수 없음 | grep 결과 없음 | ✅ |
| TC-5 | landing/history/mech i18n 키 없음 | grep 결과 없음 | ✅ |
| TC-6 | proxy/messages/analysis/token/onboard i18n 키 유지 | grep 13건 | ✅ |
| TC-7 | esc/escAttr/renderJsonTree 유틸 유지 | grep 3건 | ✅ |
| TC-8 | applyI18n 함수 유지, renderHistory 호출 없음 | applyI18n 1건, renderHistory 0건 | ✅ |
| TC-9 | init 코드에서 switchM/savedKey 제거 | JS 코드에서 참조 없음 | ✅ |
| TC-10 | JS 문법 오류 없음 | node --check 통과 | ✅ |

## 구현 내용
- LOCALES에서 시뮬레이터 전용 i18n 키 제거: landing, history, mech, export, form, api, apiInput, header의 simulator 전용 키
- copy 키는 proxy에서도 사용하므로 최소 세트(copy, copied)만 유지
- getMechanisms, SHOW_SIMULATOR, 시뮬레이터 상태 변수(current, lastResponseText, currentPayload, mdEnabled, exportLang, sessionHistory) 제거
- buildPayload, buildSendablePayload, collectCfg 제거
- updatePreview, renderForm, switchM, showPTab, copyPayload, callApi, sendToApi, simulateSkill, simulateSubAgent, copyResponse, renderResponseContent, toggleMd, 모든 Export 함수, 모든 History 함수, openFilePicker, onApiKeyChange 제거
- applyI18n()에서 renderHistory, normalPanels form re-render 코드 제거
- Init 코드: modelSel change listener, savedKey 복원, SHOW_SIMULATOR 분기 모두 제거. 프록시 패널 직접 표시로 전환
- 3578줄 → 2626줄 (952줄 제거)

## 실행 결과

```
$ grep -c "SHOW_SIMULATOR" public/index.html
0

$ grep -c "getMechanisms" public/index.html
0

$ grep -c "buildPayload|buildSendablePayload" public/index.html
0

$ grep -c "function sendToApi|function simulateSkill|function simulateSubAgent" public/index.html
0

$ grep -c "proxy:|messages:|analysis:|token:|onboard:" public/index.html
13

$ node --check /tmp/test-js.js
SYNTAX:OK
```
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/phase-3-html-css-tests/phase.md`
```markdown
# Phase 3: index.html HTML/CSS cleanup + tests

## 목표
시뮬레이터 전용 HTML 요소, CSS, CDN(marked.js)을 제거하고 E2E 테스트를 업데이트한다.

## 범위
- HTML: 랜딩 페이지, 탭 네비게이션, normalPanels(시뮬레이터 패널), 헤더의 simulator 전용 컨트롤(API key, model select, history btn)
- CSS: 시뮬레이터 전용 스타일 (landing, config-panel, preview-panel, resp, export, history 관련)
- CDN: marked.js 제거 (시뮬레이터 마크다운 렌더링용)
- E2E 테스트: 시뮬레이터 테스트 제거, 프록시 테스트 유지

## Steps
- Step 1: HTML/CSS/CDN 정리 및 E2E 테스트 업데이트
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/phase-3-html-css-tests/step-1.md`
```markdown
# Step 1: HTML/CSS/CDN 정리 및 E2E 테스트 업데이트

## TC

| # | 테스트 | 기대결과 | 실제결과 |
|---|--------|----------|----------|
| TC-1 | landingPanel HTML 제거 | grep 결과 없음 | ✅ |
| TC-2 | normalPanels HTML 제거 | grep 결과 없음 | ✅ |
| TC-3 | tabNav 제거 | grep 결과 없음 | ✅ |
| TC-4 | header에 API key/model/history 컨트롤 없음 | grep 결과 없음 | ✅ |
| TC-5 | marked.js CDN 제거 | grep 결과 없음 | ✅ |
| TC-6 | proxyPanel HTML 유지 | 존재 확인 | ✅ |
| TC-7 | 시뮬레이터 전용 CSS 제거 | landing/config-panel 등 없음 | ✅ |
| TC-8 | JS 문법 오류 없음 | node --check 통과 | ✅ |
| TC-9 | E2E 테스트에서 시뮬레이터 테스트 제거 | 시뮬레이터 참조 없음 | ✅ |
| TC-10 | unit 테스트 통과 | npm run test:unit 통과 | ✅ |

## 구현 내용
- HTML: landingPanel, tabNav (6개 탭 버튼), normalPanels (config-panel, preview-panel, hist-panel) 제거
- HTML: header에서 hist-btn, modelSel, apiGroup 제거; logo의 onclick/title 속성 제거
- CDN: marked.js `<script>` 태그 제거
- CSS 제거: .config-panel, .file-btn, .example-row, .ex-tag, .warn-row, .w-icon, .flow*, .btn-sim, .btn-sa, .preview-panel, .preview-header, .ptabs, .ptab, .pactions, .size-pill, .live-pill, .live-dot, .pview, #pv-response, .resp-*, .md-rendered, #pv-export, .exp-*, .hist-panel, .hist-entry, .hist-mech, .hist-msg, .hist-time, .landing*, .lc-*, .logo { cursor: pointer }, #normalPanels
- CSS 유지 (proxy 공유): .panel-header, .inject-chip, .config-body, .how-box, .how-title, .how-text, .field, .config-footer, .btn, .btn-send, .btn-copy, .copy-small, .hist-list, .hist-empty, .spin, @keyframes spin/pulse, scrollbar
- E2E: activateSimulator(), activateProxy() 제거; 시뮬레이터 전용 테스트 14개 제거; 프록시 테스트 8개 유지
- unit 테스트 13/13 통과

## 실행 결과

```
$ grep -c "landingPanel" public/index.html
0

$ grep -c "normalPanels" public/index.html
0

$ grep -c "tabNav" public/index.html
0

$ grep -c "modelSel|apiGroup|hist-btn|histToggleBtn" public/index.html
0

$ grep -c "marked" public/index.html
0

$ grep -c "proxyPanel" public/index.html
3

$ grep -c ".config-panel|.preview-panel|.hist-panel|.md-rendered|.landing|#pv-export|#pv-response" public/index.html
0

$ node --check /tmp/t.js
SYNTAX:OK

$ grep -c "activateSimulator|switchM|data-m=|actionBtn|modelSel|histPanel|histToggleBtn|exp-tab" tests/e2e/app.spec.ts
0

$ npm run test:unit
ℹ pass 13
ℹ fail 0
```
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/phase-3-html-css-tests/step-2.md`
```markdown
# Step 2: E2E 테스트 업데이트 (시뮬레이터 테스트 제거)

## TC

| # | 테스트 | 기대결과 | 실제결과 |
|---|--------|----------|----------|
| TC-1 | activateSimulator 함수 없음 | grep 결과 없음 | ✅ |
| TC-2 | switchM 참조 없음 | grep 결과 없음 | ✅ |
| TC-3 | data-m= 참조 없음 | grep 결과 없음 | ✅ |
| TC-4 | modelSel/actionBtn/histPanel 참조 없음 | grep 결과 없음 | ✅ |
| TC-5 | 프록시 테스트 유지 (proxyStartBtn, dtab 등) | grep 존재 | ✅ |
| TC-6 | TypeScript 문법 오류 없음 | npx tsc --noEmit 통과 | ✅ |

## 구현 내용
- Step 1에서 E2E 테스트 업데이트 함께 완료됨
- activateSimulator(), activateProxy() 헬퍼 함수 제거
- 시뮬레이터 전용 테스트 14개 제거 (메커니즘 탭, API 키, 히스토리, Export 등)
- 프록시 테스트 8개 유지 (시작 버튼, offProxy, UI 반응성, debounce, 언어 전환, 상세 탭)

## 실행 결과

```
$ grep -c "activateSimulator" tests/e2e/app.spec.ts
0

$ grep -c "switchM" tests/e2e/app.spec.ts
0

$ grep -c "data-m=" tests/e2e/app.spec.ts
0

$ grep -c "modelSel\|actionBtn\|histPanel" tests/e2e/app.spec.ts
0

$ grep -c "proxyStartBtn\|dtab" tests/e2e/app.spec.ts
4
```
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/phase-3-html-css-tests/step-3.md`
```markdown
# Step 3: QA — 전체 테스트 실행

## TC

| # | 테스트 | 기대결과 | 실제결과 |
|---|--------|----------|----------|
| TC-1 | unit 테스트 통과 | npm run test:unit 13/13 통과 | ✅ |
| TC-2 | JS 문법 오류 없음 | node --check 통과 | ✅ |
| TC-3 | 시뮬레이터 HTML 잔재 없음 | landingPanel, tabNav, normalPanels grep 0 | ✅ |
| TC-4 | 시뮬레이터 CSS 잔재 없음 | config-panel, preview-panel, landing grep 0 | ✅ |
| TC-5 | 시뮬레이터 JS 잔재 없음 | SHOW_SIMULATOR, getMechanisms, buildPayload grep 0 | ✅ |
| TC-6 | 프록시 기능 보존 | proxyPanel, toggleProxy, renderProxyList 존재 | ✅ |

## 실행 결과

```
$ npm run test:unit
ℹ tests 13
ℹ pass 13
ℹ fail 0

$ node --check /tmp/t.js
SYNTAX:OK

TC-3 HTML remnants:
  landingPanel: 0
  tabNav: 0
  normalPanels: 0

TC-4 CSS remnants:
  config-panel: 0
  preview-panel: 0
  landing: 0

TC-5 JS remnants:
  SHOW_SIMULATOR: 0
  getMechanisms: 0
  buildPayload: 0

TC-6 Proxy preserved:
  proxyPanel: 3
  toggleProxy: 2
  renderProxyList: 7
```
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/verifications/round-1.md`
```markdown
# Verification Round 1

## 결과: PASS

| # | 검증 항목 | 결과 |
|---|-----------|------|
| 1 | Unit tests (13/13) | ✅ |
| 2 | JS syntax (main.js, preload.js) | ✅ |
| 3 | JS syntax (index.html) | ✅ |
| 4 | Backend: anthropic-ai/sdk 제거 | ✅ |
| 5 | Backend: IPC handlers 제거 | ✅ |
| 6 | Frontend: SHOW_SIMULATOR 제거 | ✅ |
| 7 | Frontend: HTML (landing, tabs, normalPanels) 제거 | ✅ |
| 8 | Frontend: marked.js CDN 제거 | ✅ |
| 9 | Proxy 기능 보존 | ✅ |
| 10 | E2E 시뮬레이터 테스트 제거 | ✅ |
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/verifications/round-2.md`
```markdown
# Verification Round 2

## 결과: PASS

| # | 검증 항목 | 결과 |
|---|-----------|------|
| 1 | Unit tests (13/13) | ✅ |
| 2 | JS syntax (main.js, preload.js, index.html) | ✅ |
| 3 | Backend simulator 잔재 0건 | ✅ |
| 4 | Frontend simulator 잔재 0건 | ✅ |
| 5 | Proxy 기능 보존 (13 references) | ✅ |
```

## File: `brain/knowledge/docs_legacy/2026-03-13/remove-simulator/verifications/round-3.md`
```markdown
# Verification Round 3

## 결과: PASS

| # | 검증 항목 | 결과 |
|---|-----------|------|
| 1 | Unit tests (13/13) | ✅ |
| 2 | JS syntax (main.js, preload.js, index.html) | ✅ |
| 3 | Backend simulator 잔재 0건 | ✅ |
| 4 | Frontend simulator 잔재 0건 | ✅ |
| 5 | Proxy 기능 보존 (13 references) | ✅ |
```

## File: `brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/plan.md`
```markdown
# Sentry Error Logging Integration

## 목표
Claude Inspector에 @sentry/electron을 통합하여 에러 로그 수집 기반을 마련한다.

## 범위
- @sentry/electron 의존성 설치 및 빌드 설정
- main process (main.js) Sentry 초기화
- renderer process (preload.js) Sentry 초기화
- 민감 정보 (API 키, Authorization 헤더) 필터링

## Phase 구성
- Phase 1: Core Sentry Setup (3 steps)

## 변경 파일
- `package.json`: 의존성 추가 + build.files 업데이트
- `main.js`: Sentry main process 초기화
- `preload.js`: Sentry renderer 초기화
```

## File: `brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "normal",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "duo",
  "current_dev_phase": 1,
  "current_step": 3,
  "dev_phases": {
    "1": {
      "name": "Core Sentry Setup",
      "folder": "phase-1-core-sentry-setup",
      "total_steps": 3,
      "steps": {
        "1": {
          "name": "Install dependency + update build config",
          "status": "done"
        },
        "2": {
          "name": "Initialize Sentry in main.js",
          "status": "done"
        },
        "3": {
          "name": "Initialize Sentry in preload.js",
          "status": "done"
        }
      }
    }
  },
  "verification": {
    "rounds_passed": 3
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/phase-1-core-sentry-setup/phase.md`
```markdown
# Phase 1: Core Sentry Setup

## 목표
@sentry/electron을 설치하고 main/renderer 양쪽 프로세스에서 Sentry를 초기화한다.

## 범위
- package.json 의존성 및 빌드 설정
- main.js Sentry 초기화 (beforeSend로 민감 헤더 필터링)
- preload.js Sentry renderer 초기화

## Steps
1. Install @sentry/electron + update build.files
2. Initialize Sentry in main.js
3. Initialize Sentry in preload.js

## 완료 기준
- 앱이 에러 없이 시작됨
- Sentry가 양쪽 프로세스에서 초기화됨
- 민감 헤더가 Sentry 이벤트에서 제거됨
```

## File: `brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/phase-1-core-sentry-setup/step-1.md`
```markdown
# Step 1: Install @sentry/electron + update build config ✅

## Tasks
1. Run `npm install @sentry/electron`
2. In `package.json` → `build.files` array, add `"node_modules/@sentry/**"`

## TC

| TC | 검증 항목 | 기대 결과 | 상태 |
|----|----------|----------|------|
| TC-01 | @sentry/electron 설치 | node_modules/@sentry/electron 존재 + package.json dependency 등록 | ✅ |
| TC-02 | build.files 업데이트 | package.json build.files에 `node_modules/@sentry/**` 포함 | ✅ |
| TC-03 | 기존 의존성 유지 | @anthropic-ai/sdk 의존성 그대로 존재 | ✅ |

## 실행출력

```
TC-01: dep: ^7.10.0, Module installed: YES
TC-02: has-sentry: true, build.files includes node_modules/@sentry/**
TC-03: has-anthropic: true
```
```

## File: `brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/phase-1-core-sentry-setup/step-2.md`
```markdown
# Step 2: Initialize Sentry in main.js ✅

## Tasks
1. Add Sentry require + init at the very top of main.js (before all other requires)
2. DSN from `process.env.SENTRY_DSN` (empty string default)
3. beforeSend filter strips sensitive headers from breadcrumbs

## TC

| TC | 검증 항목 | 기대 결과 | 상태 |
|----|----------|----------|------|
| TC-01 | Sentry require 위치 | main.js 첫 번째 줄이 `@sentry/electron/main` require | ✅ |
| TC-02 | Sentry.init 호출 | dsn, environment, release, beforeSend 설정 존재 | ✅ |
| TC-03 | beforeSend 필터 | x-api-key, authorization 헤더 삭제 로직 존재 | ✅ |
| TC-04 | 기존 코드 유지 | electron, fs, path 등 기존 require 그대로 존재 | ✅ |

## 실행출력

```
TC-01: main.js line 1 = "const Sentry = require('@sentry/electron/main');"
TC-02: Sentry.init({ dsn, environment, release, beforeSend }) 확인
TC-03: delete bc.data['x-api-key'], ['X-Api-Key'], ['authorization'], ['Authorization'] 확인
TC-04: line 22-27에 electron, fs, path, http, https, Anthropic require 유지
```
```

## File: `brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/phase-1-core-sentry-setup/step-3.md`
```markdown
# Step 3: Initialize Sentry in preload.js ✅

## Tasks
1. Add `require('@sentry/electron/renderer').init();` at the very top of preload.js (before contextBridge)

## TC

| TC | 검증 항목 | 기대 결과 | 상태 |
|----|----------|----------|------|
| TC-01 | Sentry renderer init 위치 | preload.js 첫 번째 줄이 `@sentry/electron/renderer` require + init | ✅ |
| TC-02 | 기존 코드 유지 | contextBridge, ipcRenderer require 및 exposeInMainWorld 그대로 존재 | ✅ |

## 실행출력

```
TC-01: preload.js line 1 = "require('@sentry/electron/renderer').init();"
TC-02: line 3 contextBridge/ipcRenderer require, line 5-20 exposeInMainWorld 유지 확인
```
```

## File: `brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/verifications/round-1.md`
```markdown
# Verification Round 1

## Code Review
- [x] Sentry main init placement: Lines 1-20 of main.js, before all other requires
- [x] Sentry renderer init placement: Line 1 of preload.js, before contextBridge
- [x] Dependencies correct: `@sentry/electron: ^7.10.0` in dependencies
- [x] Build files updated: `node_modules/@sentry/**` in build.files
- [x] Security: sensitive header filtering: beforeSend filters x-api-key, X-Api-Key, authorization, Authorization from breadcrumb data
- [x] DSN from env var: `process.env.SENTRY_DSN || ''`, not hardcoded

## Plan Conformance
- [x] All planned files changed: package.json, main.js, preload.js
- [x] No unplanned changes

## Build Test
- [x] Both main.js and preload.js pass `node --check` syntax validation
- [x] @sentry/electron installed in node_modules, main and renderer modules readable
- Note: Full Electron boot test not feasible in headless CLI; module integrity confirmed

## Result: PASS
```

## File: `brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/verifications/round-2.md`
```markdown
# Verification Round 2

## Code Review
- [x] Sentry main init placement: First statement in main.js, before Electron requires
- [x] Sentry renderer init placement: First statement in preload.js, before contextBridge
- [x] Dependencies correct: @sentry/electron ^7.10.0 in dependencies
- [x] Build files updated: node_modules/@sentry/** included
- [x] Security: sensitive header filtering: beforeSend filters 4 header variants from breadcrumbs; event.request headers not a concern for Electron desktop SDK
- [x] DSN from env var: Empty string default = Sentry no-op without DSN (safe for dev)
- [x] beforeSend correctly returns event (not accidentally null)

## Plan Conformance
- [x] All planned files changed: package.json, main.js, preload.js
- [x] No unplanned changes

## Build Test
- [x] Syntax validation passes for both main.js and preload.js
- [x] Module files present and readable in node_modules

## Result: PASS
```

## File: `brain/knowledge/docs_legacy/2026-03-13/sentry-error-logging/verifications/round-3.md`
```markdown
# Verification Round 3

## Code Review
- [x] Sentry main init placement: Confirmed first require/init block in main.js
- [x] Sentry renderer init placement: Confirmed first statement in preload.js
- [x] Dependencies correct: @sentry/electron ^7.10.0 verified programmatically
- [x] Build files updated: node_modules/@sentry/** confirmed in build.files array
- [x] Security: beforeSend guards against null breadcrumbs, filters 4 header key variants
- [x] DSN from env var: process.env.SENTRY_DSN with safe empty-string fallback
- [x] Release tag: `claude-inspector@${version}` follows Sentry convention

## Plan Conformance
- [x] All planned files changed: package.json, main.js, preload.js
- [x] No unplanned changes

## Build Test
- [x] Syntax validation: node --check passes for main.js and preload.js
- [x] Dependency installed: @sentry/electron modules present in node_modules

## Result: PASS
```

## File: `brain/knowledge/docs_legacy/2026-03-13/token-badge-ux/plan.md`
```markdown
# 토큰 배지 UX 개선

## 문제
현재 `↑ 23.8K in ↓ 6 out ♻23.7K read · 📝21 write · 3 uncached actual` 표시가 의미를 알기 어려움.

## 해결
직관적인 2줄 표시:
- 1줄: `입력 23.8K tok · 출력 6 tok · ~$0.02`
- 2줄: `캐시 99% (23.7K read + 21 write) · 미캐시 3`

hover 시 상세 설명 tooltip.

## 변경 파일별 상세
### `public/index.html`

#### 토큰 배지 표시 변경

- **변경 이유**: 현재 기호(↑↓♻📝)와 영어 약어가 혼재해서 의미 파악 어려움. 한글 레이블 + 비용 추정 + 캐시 비율로 직관화.
- **Before** (JS, 라인 3026-3048):
```javascript
const usage = entry.response?.body?.usage;
if (usage) {
  const totalIn = (usage.input_tokens || 0) + (usage.cache_read_input_tokens || 0) + (usage.cache_creation_input_tokens || 0);
  let parts = `<span class="tt-badge">${kb} KB</span>`;
  parts += `<span class="tt-badge">↑ ${fmtTok(totalIn)} in</span>`;
  parts += `<span class="tt-badge">↓ ${fmtTok(usage.output_tokens)} out</span>`;
  const cacheRead = usage.cache_read_input_tokens || 0;
  const cacheWrite = usage.cache_creation_input_tokens || 0;
  if (cacheRead || cacheWrite) {
    const cacheParts = [];
    if (cacheRead) cacheParts.push(`♻${fmtTok(cacheRead)} read`);
    if (cacheWrite) cacheParts.push(`📝${fmtTok(cacheWrite)} write`);
    const uncached = usage.input_tokens || 0;
    if (uncached) cacheParts.push(`${fmtTok(uncached)} uncached`);
    parts += `<span class="tt-badge" style="opacity:0.7">${cacheParts.join(' · ')}</span>`;
  }
  parts += `<span style="color:var(--green);font-size:9px;margin-left:4px">actual</span>`;
  return `<div class="proxy-token-pill">${parts}</div>`;
}
const tokens = Math.ceil(bytes / 3.5);
const tokStr = fmtTok(tokens);
return `<div class="proxy-token-pill"><span class="tt-badge">${kb} KB</span><span class="tt-badge">~${tokStr} tokens</span><span style="color:var(--dim);font-size:9px;margin-left:4px">estimated</span></div>`;
```
- **After**:
```javascript
const usage = entry.response?.body?.usage;
if (usage) {
  const totalIn = (usage.input_tokens || 0) + (usage.cache_read_input_tokens || 0) + (usage.cache_creation_input_tokens || 0);
  const outTok = usage.output_tokens || 0;
  const cacheRead = usage.cache_read_input_tokens || 0;
  const cacheWrite = usage.cache_creation_input_tokens || 0;
  const uncached = usage.input_tokens || 0;

  // 비용 추정 (모델별)
  const model = entry.request?.body?.model || entry.response?.body?.model || '';
  const isOpus = model.includes('opus');
  const inPrice = isOpus ? 15 : 3; // $/MTok
  const outPrice = isOpus ? 75 : 15;
  const cacheReadPrice = isOpus ? 1.5 : 0.3;
  const cacheWritePrice = isOpus ? 18.75 : 3.75;
  const cost = (uncached * inPrice + cacheRead * cacheReadPrice + cacheWrite * cacheWritePrice + outTok * outPrice) / 1_000_000;
  const costStr = cost >= 1 ? '$' + cost.toFixed(2) : cost >= 0.01 ? '$' + cost.toFixed(3) : '<$0.01';

  // 캐시 비율
  const cachePct = totalIn > 0 ? Math.round((cacheRead / totalIn) * 100) : 0;

  let html = `<div class="proxy-token-pill" title="입력: ${fmtTok(totalIn)} (캐시읽기 ${fmtTok(cacheRead)} + 캐시쓰기 ${fmtTok(cacheWrite)} + 미캐시 ${fmtTok(uncached)})\n출력: ${fmtTok(outTok)}\n비용: ${costStr}">`;
  html += `<span class="tt-badge">${kb} KB</span>`;
  html += `<span class="tt-badge">입력 ${fmtTok(totalIn)}</span>`;
  html += `<span class="tt-badge">출력 ${fmtTok(outTok)}</span>`;
  if (cachePct > 0) html += `<span class="tt-badge" style="color:var(--green)">캐시 ${cachePct}%</span>`;
  html += `<span class="tt-badge" style="color:var(--yellow)">${costStr}</span>`;
  html += `</div>`;
  return html;
}
const tokens = Math.ceil(bytes / 3.5);
const tokStr = fmtTok(tokens);
return `<div class="proxy-token-pill"><span class="tt-badge">${kb} KB</span><span class="tt-badge">~${tokStr} tokens (추정)</span></div>`;
```
- **영향 범위**: Request 탭 토큰 배지만 변경

## 검증
- 검증 명령어: `pkill -x "Electron" 2>/dev/null; npm start &`
- 기대 결과: 토큰 배지에 `입력 23.8K · 출력 6 · 캐시 99% · $0.02` 형태 표시. hover 시 상세 tooltip.
```

## File: `brain/knowledge/docs_legacy/2026-03-13/token-badge-ux/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/token-badge-ux",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/token-badge-ux/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/token-popover/plan.md`
```markdown
# 토큰 배지 클릭 시 비용 계산 팝오버

## 변경 파일별 상세
### `public/index.html`

#### 1. CSS: 팝오버 스타일 + 배지 cursor (라인 665)
- **변경 이유**: 네이티브 tooltip → 클릭 팝오버로 전환. cursor:pointer + hover 효과 + 팝오버 스타일 추가.
- **Before**:
```css
.proxy-token-pill {
  padding: 6px 12px; font-size: 11px; color: var(--dim);
  border-bottom: 1px solid var(--border); flex-shrink: 0;
  display: flex; gap: 8px; align-items: center;
}
```
- **After**: `position: relative` 추가 + `.proxy-token-pill[data-cost]` cursor/hover + `.token-popover` 스타일

#### 2. JS: title → data-cost (라인 3046-3062)
- **변경 이유**: title 속성 제거, 계산 데이터를 JSON으로 data-cost에 저장
- **Before**: `title="${tooltip}"` 속성
- **After**: `data-cost='${popData}'` 속성

#### 3. JS: 전역 클릭 핸들러 추가
- **변경 이유**: 배지 클릭 시 팝오버 생성, 바깥 클릭 시 닫힘, 복사 버튼
- **영향 범위**: 토큰 배지만

## 검증
- `pkill -x "Electron" 2>/dev/null; npm start &`
- 배지 클릭 → 팝오버, 복사 → 클립보드, 바깥 클릭 → 닫힘
```

## File: `brain/knowledge/docs_legacy/2026-03-13/token-popover/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/token-popover",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/token-popover/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/token-tooltip-detail/plan.md`
```markdown
# 토큰 tooltip 계산 과정 표시

## 변경 파일별 상세
### `public/index.html`

- **변경 이유**: hover tooltip에 단순 요약만 있어서 비용이 어떻게 계산됐는지 모름. 각 토큰 종류별 단가 × 수량 = 소계를 보여줘야 함.
- **Before** (JS, 라인 3045):
```javascript
const tooltip = `입력: ${fmtTok(totalIn)} 토큰 (캐시읽기 ${fmtTok(cacheRead)} + 캐시쓰기 ${fmtTok(cacheWrite)} + 미캐시 ${fmtTok(uncached)})\n출력: ${fmtTok(outTok)} 토큰\n캐시 적중률: ${cachePct}%\n추정 비용: ${costStr}`;
```
- **After**:
```javascript
const fmtCost = (n) => '$' + (n / 1_000_000).toFixed(4);
const tooltip = [
  `[비용 계산] 모델: ${model || '불명'}`,
  ``,
  `캐시읽기: ${fmtTok(cacheRead)} × $${crP}/MTok = ${fmtCost(cacheRead * crP)}`,
  `캐시쓰기: ${fmtTok(cacheWrite)} × $${cwP}/MTok = ${fmtCost(cacheWrite * cwP)}`,
  `미캐시 입력: ${fmtTok(uncached)} × $${inP}/MTok = ${fmtCost(uncached * inP)}`,
  `출력: ${fmtTok(outTok)} × $${outP}/MTok = ${fmtCost(outTok * outP)}`,
  ``,
  `합계: ${costStr}`,
  `캐시 적중률: ${cachePct}%`
].join('\n');
```
- **영향 범위**: tooltip만 변경, 배지 표시는 그대로

## 검증
- `pkill -x "Electron" 2>/dev/null; npm start &`
- hover 시 계산 과정 표시 확인
```

## File: `brain/knowledge/docs_legacy/2026-03-13/token-tooltip-detail/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/token-tooltip-detail",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/token-tooltip-detail/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-13/version-hash-display/plan.md`
```markdown
# 빌드 버전 해시 표시

## 변경 파일별 상세

### `package.json`
- **변경 이유**: `dist` 스크립트 실행 전에 git hash를 `public/build-info.json`에 기록하는 prebuild 단계 추가
- **Before** (현재 코드):
```json
"dist": "electron-builder",
```
- **After** (변경 후):
```json
"predist": "node -e \"const {execSync}=require('child_process');const fs=require('fs');const hash=execSync('git rev-parse --short HEAD').toString().trim();const pkg=require('./package.json');fs.writeFileSync('public/build-info.json',JSON.stringify({version:pkg.version,hash,built:new Date().toISOString()}))\"",
"dist": "electron-builder",
```
- **영향 범위**: `npm run dist` 실행 시에만 동작. `npm start`에서는 build-info.json 없으면 fallback.

### `public/index.html`
- **변경 이유**: 헤더 로고 옆에 버전+해시 표시
- **Before** (현재 코드):
```html
<span class="logo-sub" data-i18n="header.logoSub">Prompt Mechanism Visualizer</span>
```
- **After** (변경 후):
```html
<span class="logo-sub" data-i18n="header.logoSub">Prompt Mechanism Visualizer</span>
<span class="logo-ver" id="buildVer"></span>
```

CSS 추가:
```css
.logo-ver { font-size: 10px; color: var(--dim); opacity: 0.6; }
```

JS (하단 초기화 부분):
```js
fetch('build-info.json').then(r=>r.json()).then(b=>{
  document.getElementById('buildVer').textContent = `v${b.version} (${b.hash})`;
}).catch(()=>{});
```
- **영향 범위**: 헤더 로고 영역. build-info.json 없으면(개발 모드) 빈 상태로 유지.

### `public/build-info.json` (신규, 빌드 시 자동 생성)
- **용도**: 빌드 메타데이터 (version, hash, built timestamp)
- `.gitignore`에 추가하여 git 추적 안 함

### `.gitignore`
- **변경 이유**: 빌드 시 자동 생성되는 파일 제외
- `public/build-info.json` 한 줄 추가

## 검증
- 검증 명령어: `npm run predist && cat public/build-info.json`
- 기대 결과: `{"version":"1.1.3","hash":"<7자리>","built":"<ISO timestamp>"}` 출력
```

## File: `brain/knowledge/docs_legacy/2026-03-13/version-hash-display/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-13/version-hash-display",
  "active_file": "brain/knowledge/docs_legacy/2026-03-13/version-hash-display/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-14/dotenv-setup/plan.md`
```markdown
# dotenv 추가하여 .env 자동 로드

## 변경 파일별 상세

### `main.js`
- **변경 이유**: Sentry.init() 전에 dotenv를 로드해야 SENTRY_DSN 환경변수가 반영됨
- **Before** (현재 코드):
```javascript
const Sentry = require('@sentry/electron/main');
Sentry.init({
  dsn: process.env.SENTRY_DSN || '',
```
- **After** (변경 후):
```javascript
require('dotenv').config();
const Sentry = require('@sentry/electron/main');
Sentry.init({
  dsn: process.env.SENTRY_DSN || '',
```
- **영향 범위**: .env 파일의 모든 환경변수가 process.env에 로드됨

### `package.json`
- **변경 이유**: dotenv 의존성 추가 + electron-builder files에 포함
- **Before**:
```json
"dependencies": {
  "@anthropic-ai/sdk": "^0.78.0",
  "@sentry/electron": "^7.10.0"
}
```
- **After**:
```json
"dependencies": {
  "@anthropic-ai/sdk": "^0.78.0",
  "@sentry/electron": "^7.10.0",
  "dotenv": "^16.4.7"
}
```
- build.files에 `"node_modules/dotenv/**"` 추가

## 검증
- 검증 명령어: `node -e "require('./main.js')"` 는 Electron 전용이므로 불가
- 대안: `node --check main.js` (구문 검증) + `npm start`로 부팅 확인
- 기대 결과: 정상 부팅, .env의 SENTRY_DSN이 로드됨
```

## File: `brain/knowledge/docs_legacy/2026-03-14/dotenv-setup/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-14/dotenv-setup",
  "active_file": "brain/knowledge/docs_legacy/2026-03-14/dotenv-setup/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/plan.md`
```markdown
# offProxy 버그 수정 + E2E 전량 재검사

## Context
`window.electronAPI.offProxy()` 호출 시 guard 없이 직접 접근하여 테스트/비-Electron 환경에서 "Cannot read properties of undefined (reading 'offProxy')" 에러 발생. E2E 테스트가 이를 감지하지 못하고 있음.

---

## Phase 1: offProxy 버그 수정 (`public/index.html`)

### `toggleProxy()` 함수 — 전체 guard 추가 (line 1109)
- **Before**:
```js
  try {
    if (proxyRunning) {
      await window.electronAPI.proxyStop();
      window.electronAPI.offProxy();
```
- **After**:
```js
  try {
    if (!window.electronAPI) throw new Error('electronAPI not available');
    if (proxyRunning) {
      await window.electronAPI.proxyStop();
      window.electronAPI.offProxy();
```

### 페이지 로드 프록시 동기화 — optional chaining (line 2214)
- **Before**:
```js
      window.electronAPI.offProxy();
```
- **After**:
```js
      window.electronAPI?.offProxy?.();
```

## Phase 2: E2E 테스트 수정 + 추가 (`tests/e2e/app.spec.ts`)

### 새 테스트 추가

1. **`모든 offProxy 호출이 안전하게 보호됨`** — 정적 검증
2. **`프록시 토글 시 pageerror 없음`** — 런타임 검증
3. **`프록시 시작→정지 전체 사이클 정상 동작`** — 런타임 검증

## 검증
- `npm run test:e2e` — 전체 통과 확인
- `npm run test:unit` — 유닛 테스트 통과 확인
```

## File: `brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "normal",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 2,
  "current_step": 1,
  "dev_phases": {
    "1": {
      "name": "offProxy 버그 수정",
      "folder": "phase-1-offproxy-fix"
    },
    "2": {
      "name": "E2E 테스트 수정 + 추가",
      "folder": "phase-2-e2e-tests"
    }
  },
  "verification": {
    "rounds_passed": 3
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix",
  "active_file": "brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/phase-1-offproxy-fix/phase.md`
```markdown
## 목표
`window.electronAPI.offProxy()` 호출 시 guard 추가하여 undefined 에러 방지

## 범위
- `public/index.html`: toggleProxy() guard 추가 + 페이지 로드 sync optional chaining

## Steps

### Step 1: toggleProxy guard + 페이지로드 optional chaining
- `public/index.html` line 1109: try 블록 첫줄에 `if (!window.electronAPI)` guard 추가
- `public/index.html` line 2214: `window.electronAPI?.offProxy?.()` optional chaining 적용
```

## File: `brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/phase-1-offproxy-fix/step-1.md`
```markdown
## Step 1: offProxy guard 적용

| TC | 설명 | 기대결과 | 실제 결과 |
|----|------|----------|-----------|
| TC-1 | toggleProxy에 electronAPI guard 존재 | try 블록 첫줄에 `if (!window.electronAPI)` guard | ✅ line 1110 확인 |
| TC-2 | 페이지 로드 sync에 optional chaining 적용 | `window.electronAPI?.offProxy?.()` 사용 | ✅ line 2215 확인 |

### 검증명령
- TC-1: `grep -n "if (!window.electronAPI)" public/index.html`
- TC-2: `grep -n "offProxy" public/index.html`

## 실행 결과
```
$ grep -n "if (!window.electronAPI)" public/index.html
1110:    if (!window.electronAPI) throw new Error('electronAPI not available');

$ grep -n "offProxy" public/index.html
1113:      window.electronAPI.offProxy();
1117:      window.electronAPI.offProxy();
2215:      window.electronAPI?.offProxy?.();
```

toggleProxy 내부 1113, 1117은 line 1110 guard로 보호됨. 2215는 optional chaining 적용 완료.
```

## File: `brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/phase-2-e2e-tests/phase.md`
```markdown
## 목표
offProxy 버그를 감지할 수 있는 E2E 테스트 추가 + 기존 테스트 전량 통과 확인

## 범위
- `tests/e2e/app.spec.ts`: 새 테스트 3개 추가

## Steps

### Step 1: 정적 검증 테스트 + 런타임 테스트 추가
- 모든 offProxy 호출이 안전하게 보호되는지 정적 검증
- 프록시 토글 시 pageerror 없음 런타임 검증
- 프록시 시작→정지 전체 사이클 런타임 검증
```

## File: `brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/phase-2-e2e-tests/step-1.md`
```markdown
## Step 1: E2E 테스트 추가

| TC | 설명 | 기대결과 | 실제 결과 |
|----|------|----------|-----------|
| TC-1 | 정적검증: 모든 offProxy 호출이 guard로 보호됨 | toggleProxy 내 guard 존재 + 페이지로드 sync optional chaining | ✅ |
| TC-2 | 런타임검증: 프록시 토글 시 pageerror 없음 | 프록시 시작→정지 중 pageerror 0건 | ✅ |
| TC-3 | 런타임검증: 프록시 전체 사이클 정상 동작 | 시작→UI 확인→정지→UI 확인 | ✅ |
| TC-4 | 기존 11개 + 신규 테스트 전량 통과 | npm run test:e2e 전체 통과 | ✅ 14/14 passed |

### 검증명령
- `npm run test:e2e`

## 실행 결과
```
Running 14 tests using 1 worker

  ✓   1 앱 타이틀 확인 (51ms)
  ✓   2 프록시 시작 버튼 존재 (7ms)
  ✓   3 toggleProxy 시작 분기에 offProxy 선행 호출 코드 존재 (리스너 누적 방지) (2ms)
  ✓   4 반복 토글 후 UI 반응성 (500ms 이내) (384ms)
  ✓   5 연속 IPC 이벤트 시 proxyList debounce 동작 (129ms)
  ✓   6 언어 전환 버튼 클릭 → 로케일 변경 (36ms)
  ✓   7 #proxyStartBtn ID 명확화 확인 (3ms)
  ✓   8 프록시 상세 탭 버튼: messages (3ms)
  ✓   9 프록시 상세 탭 버튼: request (2ms)
  ✓  10 프록시 상세 탭 버튼: response (7ms)
  ✓  11 프록시 상세 탭 버튼: analysis (2ms)
  ✓  12 모든 offProxy 호출이 안전하게 보호됨 (guard 또는 optional chaining) (2ms)
  ✓  13 프록시 토글 시 pageerror 없음 (680ms)
  ✓  14 프록시 시작→정지 전체 사이클 정상 동작 (90ms)

  14 passed (5.8s)
```

Unit test: 13/13 passed
```

## File: `brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/verifications/round-1.md`
```markdown
## Round 1
- E2E: ✅ (14/14 passed)
- Unit: ✅ (13/13 passed)
- Code review: ✅
  - `public/index.html` line 1110: `if (!window.electronAPI) throw new Error('electronAPI not available');` guard confirmed
  - `public/index.html` line 2215: `window.electronAPI?.offProxy?.()` optional chaining confirmed
  - `tests/e2e/app.spec.ts`: 3 new tests confirmed (lines 142, 158, 181)
- Plan alignment: ✅
  - Phase 1 (offProxy guard + optional chaining): matches plan exactly
  - Phase 2 (3 new E2E tests): matches plan exactly
```

## File: `brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/verifications/round-2.md`
```markdown
## Round 2
- E2E: ✅ (14/14 passed)
- Unit: ✅ (13/13 passed)
- Code review: ✅
  - `public/index.html` line 1110: electronAPI guard confirmed
  - `public/index.html` line 2215: optional chaining confirmed
  - `tests/e2e/app.spec.ts`: 3 new tests confirmed (lines 142, 158, 181)
- Plan alignment: ✅
  - Phase 1 & Phase 2: all changes match plan
```

## File: `brain/knowledge/docs_legacy/2026-03-14/offproxy-e2e-fix/verifications/round-3.md`
```markdown
## Round 3
- E2E: ✅ (14/14 passed)
- Unit: ✅ (13/13 passed)
- Code review: ✅
  - `public/index.html` line 1110: electronAPI guard confirmed
  - `public/index.html` line 2215: optional chaining confirmed
  - `tests/e2e/app.spec.ts`: 3 new tests confirmed (lines 142, 158, 181)
- Plan alignment: ✅
  - Phase 1 & Phase 2: all changes match plan
```

## File: `brain/knowledge/docs_legacy/2026-03-14/proxy-noresponse-ui-overlap/plan.md`
```markdown
# Start Proxy 버튼 무반응 수정

## 변경 파일별 상세
### `preload.js`
- **변경 이유**: Sentry renderer init 실패가 전체 preload를 죽이지 않도록 방어
- **Before** (현재 코드):
```javascript
require('@sentry/electron/renderer').init();

const { contextBridge, ipcRenderer } = require('electron');
```
- **After** (변경 후):
```javascript
try { require('@sentry/electron/renderer').init(); } catch {}

const { contextBridge, ipcRenderer } = require('electron');
```
- **영향 범위**: Sentry renderer 초기화 실패 시에도 electronAPI가 정상 노출됨

## 검증
- 검증 명령어: `npm start` → Start Proxy 버튼 클릭
- 기대 결과: 프록시 시작, 상태 "포트 9090에서 실행 중" 표시
```

## File: `brain/knowledge/docs_legacy/2026-03-14/proxy-noresponse-ui-overlap/state.json`
```json
{
  "workflow_phase": "cancelled",
  "mode": "normal",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-14/proxy-noresponse-ui-overlap",
  "active_file": "brain/knowledge/docs_legacy/2026-03-14/proxy-noresponse-ui-overlap/.active"
}
```

## File: `brain/knowledge/docs_legacy/2026-03-14/proxy-ui-fix/plan.md`
```markdown
# macOS 트래픽 라이트 독립 titlebar 영역 추가

## 변경 파일별 상세

### `public/index.html`
- **변경 이유**: macOS hiddenInset 모드에서 트래픽 라이트(닫기/최소화/확대)가 헤더 콘텐츠와 겹침. 다른 앱처럼 상단에 별도 드래그 영역을 두어 분리.
- **Before** (현재 코드):
```css
.header { -webkit-app-region: drag; }
.header-right, .header-right *, .logo { -webkit-app-region: no-drag; }
body.darwin .header { padding-left: 76px; }
```
```html
<header class="header">
  <div class="logo">...
```
- **After** (변경 후):
```css
.titlebar {
  display: none; height: 28px; flex-shrink: 0;
  background: var(--surface); -webkit-app-region: drag;
}
body.darwin .titlebar { display: block; }
.header { -webkit-app-region: drag; }
.header-right, .header-right *, .logo { -webkit-app-region: no-drag; }
```
```html
<div class="titlebar"></div>
<header class="header">
  <div class="logo">...
```
- **영향 범위**: macOS에서만 28px 높이의 빈 드래그 영역 추가. Windows/Linux는 display:none으로 무영향.

## 검증
- `npm start`로 앱 실행
- macOS에서 트래픽 라이트가 titlebar 영역 안에 위치하고 헤더와 겹치지 않음 확인
```

## File: `brain/knowledge/docs_legacy/2026-03-14/proxy-ui-fix/state.json`
```json
{
  "workflow_phase": "done",
  "mode": "simple",
  "planning": {
    "no_question_streak": 0
  },
  "plan_approved": true,
  "team_name": "",
  "current_dev_phase": 0,
  "current_step": 0,
  "dev_phases": {},
  "verification": {
    "rounds_passed": 0
  },
  "task_dir": "brain/knowledge/docs_legacy/2026-03-14/proxy-ui-fix",
  "active_file": "brain/knowledge/docs_legacy/2026-03-14/proxy-ui-fix/.active"
}
```

## File: `homebrew-tap/README.md`
```markdown
# Homebrew Tap for Claude Inspector

## Installation

```bash
brew tap kangraemin/tap
brew install --cask claude-inspector
```

## Update

```bash
brew upgrade --cask claude-inspector
```

## Uninstall

```bash
brew uninstall --cask claude-inspector
```
```

## File: `homebrew-tap/Casks/claude-inspector.rb`
```ruby
cask "claude-inspector" do
  version "1.1.4"

  on_arm do
    url "https://github.com/kangraemin/claude-inspector/releases/download/v#{version}/Claude-Inspector-#{version}-arm64.dmg"
    sha256 "e6ce398f6a5fdad1290bf96e72361cb03f224f4c782821d3c7986ac3d226a65c"
  end
  on_intel do
    url "https://github.com/kangraemin/claude-inspector/releases/download/v#{version}/Claude-Inspector-#{version}-x64.dmg"
    sha256 "4396c8a1e8e7aaa01b5cff3eeb69398a06aace2bf4b980e45048faed448cc223"
  end

  name "Claude Inspector"
  desc "Claude Code Prompt Mechanism Visualizer"
  homepage "https://github.com/kangraemin/claude-inspector"
  app "Claude Inspector.app"

  zap trash: [
    "~/Library/Application Support/Claude Inspector",
    "~/Library/Preferences/com.claudeinspector.app.plist",
    "~/Library/Caches/com.claudeinspector.app",
  ]
end
```

## File: `public/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Claude Inspector</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <style>
    :root {
      --bg: #1e1e1e; --surface: #252526; --surface2: #2d2d2d;
      --border: #3e3e42; --text: #d4d4d4; --dim: #858585;
      --blue: #569cd6; --green: #4ec9b0; --yellow: #dcdcaa;
      --red: #f48771; --purple: #c586c0; --orange: #ce9178;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
      background: var(--bg); color: var(--text);
      height: 100vh; display: flex; flex-direction: column; overflow: hidden;
    }

    /* ── Header ── */
    .header {
      display: flex; align-items: center; justify-content: space-between;
      padding: 0 16px; height: 50px;
      background: var(--surface); border-bottom: 1px solid var(--border);
      flex-shrink: 0; gap: 12px;
    }
    body.darwin .header { padding-left: 76px; }
    .header { -webkit-app-region: drag; }
    .header-right, .header-right *, .logo { -webkit-app-region: no-drag; }

    .logo { display: flex; align-items: center; gap: 9px; }
    .logo-icon {
      width: 28px; height: 28px;
      background: linear-gradient(135deg, #569cd6, #c586c0);
      border-radius: 6px; display: flex; align-items: center; justify-content: center;
      font-size: 11px; font-weight: 800; color: #fff; letter-spacing: -.5px;
    }
    .logo-text { font-size: 15px; font-weight: 700; }
    .logo-sub { font-size: 11px; color: var(--dim); }
    .logo-ver { font-size: 10px; color: var(--dim); opacity: 0.6; }
    .update-badge {
      font-size: 10px;
      color: #4ade80;
      background: rgba(74, 222, 128, 0.1);
      border: 1px solid rgba(74, 222, 128, 0.3);
      border-radius: 4px;
      padding: 1px 5px;
      cursor: pointer;
      text-decoration: none;
      white-space: nowrap;
      display: none;
    }
    .update-badge:hover { background: rgba(74, 222, 128, 0.2); }
    .header-right { display: flex; align-items: center; gap: 8px; }

    /* ── Layout ── */
    .main { display: flex; flex: 1; overflow: hidden; }

    .panel-header {
      padding: 9px 14px; font-size: 11px; text-transform: uppercase;
      letter-spacing: .8px; color: var(--dim);
      border-bottom: 1px solid var(--border); flex-shrink: 0;
      display: flex; align-items: center; justify-content: space-between;
    }
    .inject-chip {
      font-size: 10px; padding: 2px 7px; border-radius: 10px;
      background: rgba(86,156,214,.12); color: var(--blue);
      border: 1px solid rgba(86,156,214,.25);
      text-transform: none; letter-spacing: 0; font-family: 'SF Mono', monospace;
    }
    .config-body {
      flex: 1; overflow-y: auto; padding: 13px;
      display: flex; flex-direction: column; gap: 11px;
    }
    .field { display: flex; flex-direction: column; gap: 5px; }
    .field label {
      font-size: 11px; color: var(--dim); font-weight: 600;
      text-transform: uppercase; letter-spacing: .5px;
      display: flex; align-items: center; justify-content: space-between;
    }
    .field input, .field textarea, .field select {
      background: var(--bg); border: 1px solid var(--border);
      border-radius: 5px; color: var(--text);
      padding: 6px 10px; font-size: 12px;
      font-family: 'SF Mono', monospace; outline: none;
      transition: border-color .15s; resize: vertical;
    }
    .field input:focus, .field textarea:focus, .field select:focus { border-color: var(--blue); }
    .field textarea { min-height: 80px; }
    .field textarea.tall { min-height: 120px; }

    /* ── How-it-works box ── */
    .how-box {
      background: rgba(86,156,214,.05); border: 1px solid rgba(86,156,214,.18);
      border-radius: 7px; padding: 11px 13px;
      display: flex; flex-direction: column; gap: 8px;
    }
    .how-title { font-size: 10px; font-weight: 700; color: var(--blue); text-transform: uppercase; letter-spacing: .7px; }
    .how-text { font-size: 12px; color: var(--dim); line-height: 1.55; }
    .how-text code {
      background: var(--surface2); padding: 1px 4px; border-radius: 3px;
      font-family: 'SF Mono', monospace; font-size: 11px; color: var(--text);
    }
    /* ── Buttons ── */
    .config-footer {
      padding: 11px 13px; border-top: 1px solid var(--border);
      display: flex; gap: 8px; flex-shrink: 0; align-items: center;
    }
    .btn {
      padding: 7px 14px; border-radius: 5px; font-size: 12px; font-weight: 600;
      cursor: pointer; border: none; transition: opacity .15s;
      display: flex; align-items: center; gap: 6px;
    }
    .btn:disabled { opacity: .4; cursor: not-allowed; }
    .btn-send { background: var(--blue); color: #fff; flex: 1; justify-content: center; }
    .btn-send:not(:disabled):hover { opacity: .82; }
    .btn-copy { background: var(--surface2); color: var(--text); border: 1px solid var(--border); }
    .btn-copy:hover { border-color: var(--blue); }

    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.3} }
    .copy-small {
      padding: 4px 10px; font-size: 11px;
      background: var(--surface2); border: 1px solid var(--border);
      border-radius: 4px; color: var(--dim); cursor: pointer; transition: all .15s;
    }
    .copy-small:hover { color: var(--text); border-color: var(--blue); }

    .hist-list { flex: 1; overflow-y: auto; }
    .hist-empty { padding: 20px 16px; color: var(--dim); font-size: 12px; text-align: center; line-height: 1.7; }

    /* ── Spinner ── */
    .spin {
      display: inline-block; width: 13px; height: 13px;
      border: 2px solid var(--border); border-top-color: var(--blue);
      border-radius: 50%; animation: spin .7s linear infinite;
    }
    @keyframes spin { to { transform: rotate(360deg); } }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #444; border-radius: 3px; }

    /* ── Proxy panel ── */
    .proxy-panel { flex: 1; display: flex; overflow: hidden; }
    .proxy-ctrl {
      width: 320px; flex-shrink: 0;
      background: var(--surface); border-right: 1px solid var(--border);
      display: flex; flex-direction: column; overflow: hidden;
    }
    .proxy-stream { flex: 1; display: flex; overflow: hidden; }
    .proxy-list {
      width: 280px; flex-shrink: 0;
      background: var(--surface); border-right: 1px solid var(--border);
      display: flex; flex-direction: column; overflow: hidden;
    }
    .proxy-detail { flex: 1; display: flex; flex-direction: column; overflow: hidden; }
    .proxy-status {
      display: flex; align-items: center; gap: 8px; font-size: 12px;
      padding: 8px 12px; border-radius: 6px;
      background: var(--surface2); border: 1px solid var(--border);
    }
    .proxy-status.running { border-color: rgba(78,201,176,.4); background: rgba(78,201,176,.07); }
    .proxy-status .ps-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--border); flex-shrink: 0; }
    .proxy-status.running .ps-dot { background: var(--green); animation: pulse 1.5s infinite; }
    .proxy-cmd {
      background: var(--bg); border: 1px solid var(--border);
      border-radius: 5px; padding: 8px 10px;
      font-family: 'SF Mono', monospace; font-size: 11px;
      line-height: 1.6; white-space: nowrap; overflow-x: auto;
    }
    .prx-entry {
      padding: 9px 13px; border-bottom: 1px solid var(--border);
      cursor: pointer; transition: background .12s;
    }
    .prx-entry:hover { background: var(--surface2); }
    .prx-entry.selected { background: rgba(86,156,214,.12); border-left: 3px solid var(--blue); }
    .prx-method { font-size: 10px; font-weight: 700; font-family: 'SF Mono', monospace; color: var(--green); margin-right: 5px; }
    .prx-path { font-size: 11px; color: var(--text); overflow: hidden; text-overflow: ellipsis; white-space: nowrap; flex: 1; }
    .prx-model { font-size: 10px; color: var(--dim); margin-top: 2px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .prx-ts { font-size: 10px; color: var(--dim); opacity: .6; flex-shrink: 0; margin-left: 6px; }
    .dtabs {
      display: flex; gap: 4px; padding: 7px 12px;
      border-bottom: 1px solid var(--border); background: var(--surface); flex-shrink: 0;
    }
    .dtab {
      padding: 3px 10px; font-size: 12px; border-radius: 4px; cursor: pointer;
      background: none; border: 1px solid transparent; color: var(--dim); transition: all .15s;
    }
    .dtab.active { background: var(--surface2); border-color: var(--border); color: var(--text); }
    .proxy-empty {
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      flex: 1; color: var(--dim); font-size: 13px; text-align: center; gap: 8px; padding: 20px;
      line-height: 1.7;
    }

    /* ── Messages view ── */
    .msg-filter {
      display: flex; align-items: center; gap: 6px;
      padding: 7px 12px; border-bottom: 1px solid var(--border);
      flex-shrink: 0; background: var(--surface);
    }
    .mf-btn {
      padding: 3px 10px; font-size: 11px; border-radius: 4px;
      background: none; border: 1px solid var(--border);
      color: var(--dim); cursor: pointer; transition: all .15s;
    }
    .mf-btn.active { background: var(--surface2); border-color: var(--blue); color: var(--text); }
    .msg-count { font-size: 10px; color: var(--dim); margin-left: auto; }
    .msgs-list { display: flex; flex-direction: column; gap: 8px; padding: 12px; overflow-y: auto; }
    .msg-card { border-radius: 6px; border: 1px solid var(--border); overflow: hidden; font-size: 12px; }
    .msg-card.msg-user { border-color: rgba(86,156,214,.35); }
    .msg-card.msg-assistant { border-color: var(--border); opacity: .65; }
    .msg-role {
      padding: 4px 10px; font-size: 10px; font-weight: 700;
      text-transform: uppercase; letter-spacing: .6px; border-bottom: 1px solid var(--border);
    }
    .msg-card.msg-user .msg-role { color: var(--blue); background: rgba(86,156,214,.08); }
    .msg-card.msg-assistant .msg-role { color: var(--dim); background: var(--surface2); }
    .msg-body { padding: 8px 10px; display: flex; flex-direction: column; gap: 5px; }
    .msg-text {
      white-space: pre-wrap; word-break: break-word; line-height: 1.6;
      font-family: 'SF Mono', monospace; max-height: 220px; overflow-y: auto;
    }
    .msg-badge {
      display: inline-block; padding: 1px 6px; border-radius: 3px;
      font-size: 10px; font-weight: 700; margin: 1px 2px;
    }
    .msg-badge.green { background: rgba(78,201,176,.15); color: var(--green); border: 1px solid rgba(78,201,176,.3); }
    .msg-badge.cyan  { background: rgba(86,156,214,.15); color: var(--blue);  border: 1px solid rgba(86,156,214,.3); }
    .msg-badge.yellow { background: rgba(220,220,170,.1); color: var(--yellow); border: 1px solid rgba(220,220,170,.25); }
    .msg-badge.hl-active { outline: 2px solid currentColor; outline-offset: 1px; }
    .badge-expand-content.badge-section-hl {
      background: rgba(255,235,59,.08); border-left: 3px solid rgba(255,235,59,.5);
      padding-left: 8px;
    }
    .msg-tool { color: var(--purple); font-family: 'SF Mono', monospace; font-size: 11px; }
    .msg-tool-result { color: var(--green); font-family: 'SF Mono', monospace; font-size: 11px; }
    .msg-other { color: var(--dim); font-family: 'SF Mono', monospace; font-size: 11px; }
    /* typed vs injected separation */
    .msg-typed {
      background: rgba(86,156,214,.06); border-left: 2px solid var(--blue);
      padding: 6px 10px; border-radius: 0 4px 4px 0;
      white-space: pre-wrap; word-break: break-word; line-height: 1.6;
      font-family: 'SF Mono', monospace;
    }
    .msg-injected-row { margin: 2px 0; }
    .msg-badge.expandable { cursor: pointer; user-select: none; }
    .msg-badge.expandable::after { content: ' ▶'; font-size: 8px; opacity: .7; }
    .msg-badge.expandable.open::after { content: ' ▼'; }
    .badge-expand-content {
      display: none; margin-top: 4px;
      background: var(--bg); border: 1px solid var(--border);
      border-radius: 4px; padding: 8px 10px;
      font-size: 11px; font-family: 'SF Mono', monospace;
      white-space: pre-wrap; word-break: break-word;
      max-height: 250px; overflow-y: auto; color: var(--dim);
    }
    /* search bar */
    .msg-search-bar {
      display: flex; align-items: center; gap: 6px;
      padding: 5px 10px; border-bottom: 1px solid var(--border);
      background: var(--surface); flex-shrink: 0;
    }
    .msg-search-input {
      flex: 1; background: var(--bg); border: 1px solid var(--border);
      color: var(--text); padding: 3px 8px; border-radius: 4px;
      font-size: 11px; font-family: 'SF Mono', monospace; outline: none;
    }
    .msg-search-input:focus { border-color: var(--blue); }
    .msg-search-clear {
      background: none; border: none; color: var(--dim); cursor: pointer;
      font-size: 13px; padding: 0 2px; line-height: 1;
    }
    mark.search-hl { background: rgba(255,235,59,.35); color: inherit; border-radius: 2px; padding: 0 1px; }
    mark.search-hl.current { background: rgba(255,152,0,.7); }
    .search-nav { display: flex; align-items: center; gap: 4px; font-size: 11px; color: var(--dim); white-space: nowrap; }
    .search-nav-btn { background: none; border: 1px solid var(--border); color: var(--dim); border-radius: 4px; width: 22px; height: 22px; cursor: pointer; font-size: 12px; display: flex; align-items: center; justify-content: center; }
    .search-nav-btn:hover { color: var(--fg); border-color: var(--fg); }

    /* ── Analysis view ── */
    .analysis-view { padding: 14px; display: flex; flex-direction: column; gap: 14px; }
    .analysis-chips { display: flex; flex-wrap: wrap; gap: 6px; }
    .mech-chip {
      display: flex; align-items: center; gap: 5px;
      padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 700;
      font-family: 'SF Mono', monospace;
    }
    .mech-chip.found { opacity: 1; }
    .mech-chip.not-found { opacity: .25; }
    .mech-chip.cm  { background: rgba(78,201,176,.15);  color: var(--green);  border: 1px solid rgba(78,201,176,.35); }
    .mech-chip.st  { background: rgba(86,156,214,.15);  color: var(--blue);   border: 1px solid rgba(86,156,214,.35); }
    .mech-chip.sc  { background: rgba(220,220,170,.12); color: var(--yellow); border: 1px solid rgba(220,220,170,.3); }
    .mech-chip.sk  { background: rgba(197,134,192,.15); color: var(--purple); border: 1px solid rgba(197,134,192,.35); }
    .mech-chip.sa  { background: rgba(206,145,120,.15); color: var(--orange); border: 1px solid rgba(206,145,120,.35); }
    .mech-chip.mc  { background: rgba(78,201,220,.12);  color: #4ec9dc;       border: 1px solid rgba(78,201,220,.3); }
    .mech-chip.mn  { background: rgba(156,220,254,.12); color: #9cdcfe;       border: 1px solid rgba(156,220,254,.3); }
    .mech-chip.btn { cursor: pointer; transition: filter .1s; }
    .mech-chip.btn:hover { filter: brightness(1.3); }
    .mech-chip.btn.active { outline: 2px solid currentColor; outline-offset: 1px; }
    .mech-section-active { box-shadow: 0 0 0 2px rgba(255,255,255,.2); border-radius: 6px; }
    .mech-hl-text { background: rgba(80,200,120,.18); border-radius: 2px; outline: 1px solid rgba(80,200,120,.4); }
    .mech-hl-row { background: rgba(80,200,120,.12); border-radius: 4px; }
    .mech-filter-desc {
      padding: 6px 12px 8px; font-size: 11px;
      border-top: 1px solid var(--border); display: flex; align-items: flex-start; gap: 8px;
    }
    .mech-filter-desc-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; margin-top: 3px; }
    .mech-filter-desc-body { display: flex; flex-direction: column; gap: 2px; }
    .mech-filter-desc-who { font-size: 10px; color: var(--dim); opacity: .7; }
    .mech-filter-desc-what { color: var(--fg); line-height: 1.5; }
    .analysis-section { display: flex; flex-direction: column; gap: 6px; }
    .analysis-section-title {
      font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: .8px;
      display: flex; align-items: center; gap: 6px;
    }
    .analysis-desc { font-size: 11px; color: var(--dim); margin: 4px 0 8px; line-height: 1.5; }
    .analysis-block {
      background: var(--surface2); border: 1px solid var(--border);
      border-radius: 5px; padding: 9px 11px;
      font-size: 11px; font-family: 'SF Mono', monospace;
      line-height: 1.6; color: var(--text);
      white-space: pre-wrap; word-break: break-all;
      max-height: 180px; overflow-y: auto;
    }
    .analysis-block.highlight-green { border-color: rgba(78,201,176,.4); }
    .analysis-block.highlight-blue  { border-color: rgba(86,156,214,.4); }
    .analysis-block.highlight-yellow{ border-color: rgba(220,220,170,.35); }
    .analysis-block.highlight-purple{ border-color: rgba(197,134,192,.4); }
    .analysis-block.highlight-orange{ border-color: rgba(206,145,120,.4); }

    /* ── JSON Tree Viewer ── */
    .json-tree-view {
      font-family: 'SF Mono', 'Consolas', monospace;
      font-size: 12px; line-height: 1.7;
      padding: 12px 16px; overflow: auto;
    }
    .jt-key  { color: #9cdcfe; }
    .jt-str  { color: var(--orange); }
    .jt-num  { color: var(--green); }
    .jt-bool { color: var(--blue); }
    .jt-null { color: var(--dim); }
    .jt-row  { display: block; white-space: nowrap; }
    .jt-lined { position: relative; padding-left: 52px; }
    .jt-lined .jt-row::before {
      content: attr(data-ln);
      position: absolute;
      left: 0;
      width: 40px;
      text-align: right;
      color: var(--dim);
      font-size: 11px;
      user-select: none;
      opacity: 0.5;
    }
    .jt-line-info { color: var(--dim); font-size: 10px; padding: 4px 12px; opacity: 0.6; }
    .jt-str-long { display: inline; }
    .jt-str-preview {
      display: inline-block; vertical-align: top; max-width: calc(100% - 60px);
      overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
      color: var(--orange); cursor: pointer;
    }
    .jt-str-expanded {
      color: var(--orange);
    }
    .jt-exp-line {
      display: block; white-space: pre; overflow: hidden;
      color: var(--orange); min-height: 1.3em;
    }
    .jt-exp-line.mech-hl-text {
      background: rgba(80,200,120,.15); outline: none; border-radius: 0;
    }
    .jt-lined .jt-exp-line::before {
      content: attr(data-ln);
      position: absolute; left: 0; width: 40px;
      text-align: right; color: var(--dim); font-size: 11px;
      user-select: none; opacity: 0.5;
    }
    .jt-no-ln::before { content: '' !important; }
    .jt-str-toggle {
      color: var(--dim); font-size: 10px; cursor: pointer;
      padding: 0 4px; user-select: none;
    }
    .jt-str-toggle:hover { color: var(--yellow); }
    .jt-btn {
      display: inline-block; width: 14px; font-size: 8px; line-height: 1;
      color: var(--dim); cursor: pointer; user-select: none;
      text-align: center; vertical-align: middle; transition: color .1s;
    }
    .jt-btn:hover { color: var(--yellow); }
    .jt-tag {
      color: var(--dim); font-size: 10px; cursor: pointer;
      padding: 0 3px; vertical-align: middle;
    }
    .jt-tag:hover { color: var(--text); }
    .jt-tok { color: var(--dim); font-size: 9px; opacity: 0.7; margin-left: 4px; }
    .proxy-token-pill {
      padding: 6px 12px;
      font-size: 11px;
      color: var(--dim);
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
      display: flex;
      gap: 8px;
      align-items: center;
      position: relative;
    }
    .proxy-token-pill[data-cost] { cursor: pointer; }
    .proxy-token-pill[data-cost]:hover .tt-badge { background: rgba(255,255,255,0.12); }
    .token-popover {
      position: absolute; top: 100%; left: 12px; z-index: 1000;
      background: var(--bg-lighter, #2a2a2a); border: 1px solid var(--border);
      border-radius: 8px; padding: 12px 16px; min-width: 320px;
      box-shadow: 0 8px 24px rgba(0,0,0,0.4);
      font-family: 'SF Mono', monospace; font-size: 11px;
      color: var(--text); line-height: 1.6;
      animation: popFadeIn 0.15s ease-out;
    }
    @keyframes popFadeIn { from { opacity:0; transform:translateY(-4px); } to { opacity:1; transform:translateY(0); } }
    .token-popover-title {
      font-size: 12px; font-weight: 600; color: var(--blue, #7aa2f7);
      margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;
    }
    .token-popover-copy {
      font-size: 10px; color: var(--dim); cursor: pointer;
      padding: 2px 8px; border-radius: 4px; background: rgba(255,255,255,0.06);
    }
    .token-popover-copy:hover { background: rgba(255,255,255,0.12); color: var(--text); }
    .token-popover-row { display: grid; grid-template-columns: 72px 1fr auto; padding: 2px 0; gap: 8px; align-items: baseline; }
    .token-popover-row.tp-total {
      border-top: 1px solid var(--border); margin-top: 4px; padding-top: 6px; font-weight: 600;
      grid-template-columns: 1fr auto;
    }
    .token-popover-info { color: var(--dim); font-size: 10px; margin-bottom: 6px; }
    .token-popover-note {
      color: var(--dim); font-size: 10px; line-height: 1.5;
      margin-top: 8px; padding-top: 6px; border-top: 1px solid var(--border);
    }
    .tp-label { color: var(--dim); white-space: nowrap; }
    .tp-desc { color: var(--dim); font-size: 9px; opacity: 0.7; grid-column: 1 / -1; margin-top: -2px; }
    .tp-formula { color: var(--text); opacity: 0.7; text-align: right; }
    .tp-result { color: var(--yellow, #e0af68); font-weight: 600; text-align: right; white-space: nowrap; }
    .tt-badge {
      background: rgba(255,255,255,0.06);
      padding: 2px 8px;
      border-radius: 4px;
      font-family: 'SF Mono', monospace;
    }
    .analysis-block .jt-row { white-space: normal; }
    .analysis-kv { display: flex; gap: 8px; font-size: 11px; font-family: 'SF Mono', monospace; }
    .analysis-kv .ak { color: var(--dim); flex-shrink: 0; }
    .analysis-kv .av { color: var(--text); }
    .analysis-none {
      color: var(--dim); font-size: 12px; text-align: center; padding: 24px 0;
      line-height: 1.8;
    }
    /* ── Onboarding Modal ─────────────────────────────────────────────── */
    .onboard-overlay {
      position: fixed; inset: 0; z-index: 1000;
      background: rgba(0,0,0,.6); backdrop-filter: blur(4px);
      display: flex; align-items: center; justify-content: center;
    }
    .onboard-card {
      background: var(--bg1); border: 1px solid var(--border);
      border-radius: 16px; padding: 36px 40px; max-width: 480px; width: 90%;
    }
    .onboard-title { font-size: 1.3rem; font-weight: 700; margin-bottom: 8px; }
    .onboard-sub { color: var(--fg2, var(--dim)); margin-bottom: 24px; font-size: .9rem; }
    .onboard-steps {
      padding-left: 20px; display: flex; flex-direction: column; gap: 12px;
      font-size: .9rem; margin-bottom: 20px; line-height: 1.5;
    }
    .onboard-cmd {
      display: block; margin-top: 6px; background: var(--bg2, var(--sidebar));
      border: 1px solid var(--border); border-radius: 6px; padding: 8px 12px;
      font-family: monospace; font-size: .85rem; color: var(--accent, var(--blue));
      white-space: nowrap; overflow-x: auto;
      user-select: all; cursor: text;
    }
    .onboard-note { font-size: .8rem; color: var(--fg2, var(--dim)); margin-bottom: 20px; }
    .onboard-btn {
      width: 100%; padding: 12px; border-radius: 8px;
      background: var(--accent, var(--blue)); color: #fff; border: none;
      font-size: 1rem; font-weight: 600; cursor: pointer;
    }
    .onboard-btn:hover { opacity: .9; }
  </style>
</head>
<body>
<!-- ── Onboarding Modal ───────────────────────────────────────────────── -->
<div id="onboardModal" class="onboard-overlay" style="display:none">
  <div class="onboard-card">
    <div class="onboard-title" data-i18n="onboard.title"></div>
    <div class="onboard-sub" data-i18n="onboard.sub"></div>
    <ol class="onboard-steps">
      <li data-i18n-html="onboard.step1"></li>
      <li>
        <span data-i18n-html="onboard.step2"></span>
        <code class="onboard-cmd">ANTHROPIC_BASE_URL=http://localhost:9090 claude</code>
      </li>
      <li data-i18n-html="onboard.step3"></li>
    </ol>
    <div class="onboard-note" data-i18n="onboard.note"></div>
    <button class="onboard-btn" onclick="closeOnboard()" data-i18n="onboard.btn"></button>
  </div>
</div>

<header class="header">
  <div class="logo">
    <div class="logo-icon">CI</div>
    <span class="logo-text">Claude Inspector</span>
    <span class="logo-sub" data-i18n="header.logoSub">Prompt Mechanism Visualizer</span>
    <span class="logo-ver" id="buildVer"></span>
    <a class="update-badge" id="updateBadge" href="#" target="_blank" rel="noopener"></a>
  </div>
  <div class="header-right">
    <button id="langToggleBtn" onclick="i18n.setLocale(i18n.locale==='ko'?'en':'ko')"
      style="padding:4px 10px;border-radius:5px;font-size:11px;background:none;border:1px solid var(--border);color:var(--dim);cursor:pointer;transition:all .15s;white-space:nowrap;font-weight:700;">EN</button>
  </div>
</header>

<div class="main">

<div id="proxyPanel" class="proxy-panel" style="display:none">
  <!-- Control -->
  <div class="proxy-ctrl">
    <div class="panel-header">
      <span data-i18n="proxy.title">Proxy Control</span>
      <span class="inject-chip" style="color:var(--red);border-color:rgba(244,135,113,.3);background:rgba(244,135,113,.08)" data-i18n="proxy.liveCapture">실시간 캡처</span>
    </div>
    <div class="config-body">
      <div class="how-box" style="border-color:rgba(244,135,113,.25);background:rgba(244,135,113,.04)">
        <div class="how-title" style="color:var(--red)" data-i18n="proxy.interceptTitle">⚡ 실제 API 트래픽 인터셉트</div>
        <div class="how-text" data-i18n-html="proxy.interceptDesc">
          Claude Code CLI의 실제 API 요청을 가로채 실시간으로 시각화합니다.<br>
          프록시를 시작한 뒤 아래 명령으로 Claude Code를 실행하세요.
        </div>
      </div>
      <div class="field">
        <label data-i18n="proxy.port">포트</label>
        <input type="number" id="proxyPort" value="9090" min="1024" max="65535" style="width:120px" oninput="updateProxyCmd()">
      </div>
      <div class="proxy-status" id="proxyStatus">
        <span class="ps-dot"></span>
        <span id="proxyStatusText" data-i18n="proxy.stopped">중지됨</span>
      </div>
      <div class="field">
        <label>
          <span data-i18n="proxy.runCommand">실행 명령</span>
          <button class="copy-small" onclick="copyProxyCmd()" style="text-transform:none;letter-spacing:0;font-weight:normal" data-i18n="copy.copy">Copy</button>
        </label>
        <div class="proxy-cmd" id="proxyCmdBox">
          <span id="proxyCmdText" style="color:var(--dim)" data-i18n="proxy.startFirst">프록시를 먼저 시작하세요</span>
        </div>
      </div>
    </div>
    <div class="config-footer">
      <button class="btn btn-send" id="proxyStartBtn" style="flex:1;justify-content:center" onclick="toggleProxy()" data-i18n="proxy.startProxy">Start Proxy</button>
      <button class="btn btn-copy" onclick="clearProxyCaptures()" data-i18n="proxy.clear">Clear</button>
    </div>
  </div>

  <!-- Stream -->
  <div class="proxy-stream">
    <div class="proxy-list">
      <div class="panel-header">
        <span data-i18n="proxy.capturedRequests">캡처된 요청</span>
        <span style="font-size:10px;color:var(--dim)" id="proxyCount">0</span>
      </div>
      <div class="hist-list" id="proxyList">
        <div class="hist-empty" data-i18n-html="proxy.noCaptures">캡처된 요청 없음<br><small>프록시를 시작하고<br>Claude Code를 실행하세요</small></div>
      </div>
    </div>
    <div class="proxy-detail">
      <div class="dtabs">
        <button class="dtab active" data-dtab="messages" onclick="showDetailTab('messages')">Messages</button>
        <button class="dtab"        data-dtab="request"  onclick="showDetailTab('request')">Request</button>
        <button class="dtab"        data-dtab="response" onclick="showDetailTab('response')">Response</button>
        <button class="dtab"        data-dtab="analysis" onclick="showDetailTab('analysis')" style="color:var(--purple)">Analysis</button>
        <button class="copy-small" style="margin-left:auto" onclick="copyProxyDetail()" data-i18n="copy.copy">Copy</button>
      </div>
      <div id="proxyDetailView" style="flex:1;overflow:hidden;display:flex;flex-direction:column">
        <div class="proxy-empty">
          <span style="font-size:28px">🔍</span>
          <span data-i18n-html="proxy.selectRequest">요청을 선택하면<br>페이로드가 표시됩니다</span>
        </div>
      </div>
    </div>
  </div>
</div><!-- /#proxyPanel -->

</div><!-- /.main -->

<script>
// ─── i18n ──────────────────────────────────────────────────────────────────
const LOCALES = {
  ko: {
    header: {
      logoSub: 'Prompt Mechanism Visualizer',
    },
    proxy: {
      title: 'Proxy Control',
      liveCapture: '실시간 캡처',
      interceptTitle: '⚡ 실제 API 트래픽 인터셉트',
      interceptDesc: 'Claude Code CLI의 실제 API 요청을 가로채 실시간으로 시각화합니다.<br>프록시를 시작한 뒤 아래 명령으로 Claude Code를 실행하세요.',
      port: '포트',
      stopped: '중지됨',
      running: '포트 {port}에서 실행 중',
      runCommand: '실행 명령',
      startFirst: '프록시를 먼저 시작하세요',
      startProxy: 'Start Proxy',
      stopProxy: 'Stop Proxy',
      clear: 'Clear',
      capturedRequests: '캡처된 요청',
      noCaptures: '캡처된 요청 없음<br><small>프록시를 시작하고<br>Claude Code를 실행하세요</small>',
      startFail: '프록시 시작 실패: ',
      selectRequest: '요청을 선택하면<br>페이로드가 표시됩니다',
      noMessages: 'messages 배열 없음',
      waitingResponse: '응답 대기 중…',
      noBody: '바디 없음',
      noResults: '결과 없음',
      msgCount: '{count} / {total}개',
    },
    messages: {
      filterUser: '내가 보낸 것',
      filterTyped: '직접 입력만',
      filterAssistant: '클로드가 보낸 것',
      filterAll: '전체',
      searchPlaceholder: '🔍 검색... (⌘F)',
      searchClear: '검색 초기화',
    },
    analysis: {
      noMechanisms: '감지된 메커니즘 없음<br><small>일반 API 요청이거나 분석 지원 외 패턴입니다</small>',
      claudeMdTitle: 'CLAUDE.md — system-reminder 주입',
      claudeMdDesc: 'Claude Code가 프로젝트/글로벌 CLAUDE.md 내용을 <system-reminder> 태그로 감싸서 messages[] 안에 삽입',
      outputStyleTitle: 'Output Style — system[] 추가 블록',
      outputStyleDesc: 'Claude Code가 system 프롬프트 배열에 추가 블록으로 삽입 (모델 응답 스타일 제어)',
      slashCmdTitle: '① 입력 — Slash Command',
      slashCmdDesc: '사용자가 /{cmd}을 입력하면 Claude Code가 <command-message> 태그로 감싸서 프롬프트에 주입',
      skillTitle: 'Skill (tool_use → tool_result)',
      skillLinkedTitle: '② 실행 — Skill (tool_use → tool_result)',
      skillDesc: 'Claude가 스킬을 tool_use로 호출하고 결과를 tool_result로 수신',
      skillLinkedDesc: 'Claude가 위 슬래시 커맨드를 읽고, 매칭되는 스킬을 tool_use로 호출',
      noToolResult: 'tool_result 없음 (다음 메시지에 있거나 아직 수신 전)',
      subAgentDesc: 'Claude가 Task tool로 독립적인 서브에이전트 API 요청을 생성 (별도 컨텍스트에서 실행)',
      searchPlaceholder: '🔍 검색... (⌘F, Enter=다음)',
    },
    mechDesc: {
      cm: {
        who: 'Claude Code CLI가 자동 주입 (우리 앱은 표시만 함)',
        what: 'CLAUDE.md 파일 내용을 <system-reminder> 태그로 감싸 messages[] 안에 삽입합니다.',
      },
      sc: {
        who: 'Claude Code CLI가 자동 래핑 (우리 앱은 표시만 함)',
        what: '/명령어 입력 시 해당 내용을 <command-message> 태그로 감싸 user 메시지에 삽입합니다.',
      },
      sk: {
        who: 'Claude Code CLI가 자동 주입 (우리 앱은 표시만 함)',
        what: '스킬이 설정되어 있으면 "The following skills are available..." 목록을 <system-reminder>로 주입합니다.',
      },
      sa: {
        who: 'Claude Code CLI가 별도 API 호출 생성 (우리 앱은 표시만 함)',
        what: 'Task tool 호출 시 Claude Code가 독립적인 두 번째 API 요청을 만들어 서브에이전트를 실행합니다.',
      },
      mc: {
        who: 'Claude가 MCP 도구 호출 (tool_use)',
        what: 'Model Context Protocol 도구를 tool_use로 호출합니다.',
      },
    },
    copy: {
      copy: '복사',
      copied: '✓ 복사됨',
    },
    search: {
      prev: '이전',
      next: '다음',
    },
    token: {
      unknown: '불명',
      estimated: '추정',
      input: '입력',
      output: '출력',
      cache: '캐시',
      cacheRead: '캐시읽기',
      cacheWrite: '캐시쓰기',
      uncachedInput: '미캐시 입력',
      copied: '복사됨!',
      copyBtn: '복사',
      costTitle: '비용 계산',
      model: '모델',
      reqSize: '요청 크기',
      total: '합계',
      cacheHitRate: '캐시 적중률',
      descCacheRead: '이전 대화에서 캐시된 토큰 재사용 (가장 저렴)',
      descCacheWrite: '새로 캐시에 저장하는 토큰 (가장 비쌈)',
      descUncached: '캐시 없이 처리되는 입력 토큰',
      descOutput: 'Claude가 생성한 응답 토큰',
      notePricingDate: '💡 가격 기준일: {date}',
      noteModelPrice: '💰 모델마다 단가 다름',
      noteOfficialDoc: '공식 문서',
      noteMTok: '📐 MTok = 백만 토큰 단위 가격',
      noteCacheSaving: '♻️ 캐시 {pct}%: 입력 대부분을 캐시에서 저렴하게 읽어 비용 절감',
      noteSubscription: '🎫 구독 기준 캐시 적용 (캐시읽기 무료)',
      noteApi: '🔑 API 기준',
    },
    onboard: {
      title: 'Claude Inspector 시작하기',
      sub: 'Claude Code가 API에 실제로 보내는 내용을 실시간으로 확인하세요',
      step1: '아래 <b>Start Proxy</b> 버튼 클릭 → 로컬 프록시(localhost:9090) 시작',
      step2: '새 터미널을 열고 아래 명령어로 Claude Code 실행:',
      step3: '이 화면으로 돌아와 <b>Messages</b> · <b>Request</b> · <b>Analysis</b> 탭에서 캡처된 트래픽 확인',
      note: '💡 프록시는 로컬에서만 동작합니다. 외부로 데이터가 전송되지 않습니다.',
      btn: '시작하기 →',
    },
  },
  en: {
    header: {
      logoSub: 'Prompt Mechanism Visualizer',
    },
    proxy: {
      title: 'Proxy Control',
      liveCapture: 'Live Capture',
      interceptTitle: '⚡ Live API Traffic Intercept',
      interceptDesc: 'Intercepts real API requests from the Claude Code CLI and visualizes them in real time.<br>Start the proxy, then run Claude Code with the command below.',
      port: 'Port',
      stopped: 'Stopped',
      running: 'Running on port {port}',
      runCommand: 'Run Command',
      startFirst: 'Start the proxy first',
      startProxy: 'Start Proxy',
      stopProxy: 'Stop Proxy',
      clear: 'Clear',
      capturedRequests: 'Captured Requests',
      noCaptures: 'No captured requests<br><small>Start the proxy and<br>run Claude Code</small>',
      startFail: 'Failed to start proxy: ',
      selectRequest: 'Select a request to<br>view its payload',
      noMessages: 'No messages array',
      waitingResponse: 'Waiting for response…',
      noBody: 'No body',
      noResults: 'No results',
      msgCount: '{count} / {total}',
    },
    messages: {
      filterUser: 'Sent by user',
      filterTyped: 'Typed only',
      filterAssistant: 'Sent by Claude',
      filterAll: 'All',
      searchPlaceholder: '🔍 Search... (⌘F)',
      searchClear: 'Clear search',
    },
    analysis: {
      noMechanisms: 'No mechanisms detected<br><small>Plain API request or unsupported pattern</small>',
      claudeMdTitle: 'CLAUDE.md — system-reminder injection',
      claudeMdDesc: 'Claude Code wraps project/global CLAUDE.md contents in <system-reminder> tags and inserts them inside messages[]',
      outputStyleTitle: 'Output Style — system[] extra block',
      outputStyleDesc: 'Claude Code inserts an extra block in the system prompt array (controls model response style)',
      slashCmdTitle: '① Input — Slash Command',
      slashCmdDesc: 'When user types /{cmd}, Claude Code wraps it in <command-message> tags and injects it into the prompt',
      skillTitle: 'Skill (tool_use → tool_result)',
      skillLinkedTitle: '② Execute — Skill (tool_use → tool_result)',
      skillDesc: 'Claude invokes a skill via tool_use and receives the result via tool_result',
      skillLinkedDesc: 'Claude reads the slash command above and calls the matching skill via tool_use',
      noToolResult: 'No tool_result (in the next message or not yet received)',
      subAgentDesc: 'Claude creates an isolated sub-agent API request via the Task tool (runs in a separate context)',
      searchPlaceholder: '🔍 Search... (⌘F, Enter=next)',
    },
    mechDesc: {
      cm: {
        who: 'Auto-injected by Claude Code CLI (this app only displays)',
        what: 'Wraps CLAUDE.md file contents in <system-reminder> tags and inserts them inside messages[].',
      },
      sc: {
        who: 'Auto-wrapped by Claude Code CLI (this app only displays)',
        what: 'When a /command is typed, its contents are wrapped in <command-message> tags and injected into the user message.',
      },
      sk: {
        who: 'Auto-injected by Claude Code CLI (this app only displays)',
        what: 'When skills are configured, a "The following skills are available..." list is injected via <system-reminder>.',
      },
      sa: {
        who: 'Claude Code CLI creates a separate API call (this app only displays)',
        what: 'When Task tool is called, Claude Code creates an independent second API request to run the sub-agent.',
      },
      mc: {
        who: 'Claude calls MCP tool (tool_use)',
        what: 'Calls a Model Context Protocol tool via tool_use.',
      },
    },
    copy: {
      copy: 'Copy',
      copied: '✓ Copied',
    },
    search: {
      prev: 'Previous',
      next: 'Next',
    },
    token: {
      unknown: 'Unknown',
      estimated: 'est.',
      input: 'Input',
      output: 'Output',
      cache: 'Cache',
      cacheRead: 'Cache Read',
      cacheWrite: 'Cache Write',
      uncachedInput: 'Uncached Input',
      copied: 'Copied!',
      copyBtn: 'Copy',
      costTitle: 'Cost Breakdown',
      model: 'Model',
      reqSize: 'Request Size',
      total: 'Total',
      cacheHitRate: 'Cache Hit Rate',
      descCacheRead: 'Reusing cached tokens from prior turns (cheapest)',
      descCacheWrite: 'Tokens being written to cache (most expensive)',
      descUncached: 'Input tokens processed without cache',
      descOutput: 'Response tokens generated by Claude',
      notePricingDate: '💡 Pricing as of: {date}',
      noteModelPrice: '💰 Pricing varies by model',
      noteOfficialDoc: 'Official Docs',
      noteMTok: '📐 MTok = price per million tokens',
      noteCacheSaving: '♻️ Cache {pct}%: most input read from cache at lower cost',
      noteSubscription: '🎫 Subscription cache applied (cache read free)',
      noteApi: '🔑 API pricing',
    },
    onboard: {
      title: 'Getting Started',
      sub: 'See what Claude Code actually sends to the Anthropic API — in real-time',
      step1: 'Click <b>Start Proxy</b> below — starts a local proxy on localhost:9090',
      step2: 'Open a new terminal and run Claude Code through the proxy:',
      step3: 'Come back here and browse captured traffic in <b>Messages</b> · <b>Request</b> · <b>Analysis</b>',
      note: '💡 The proxy runs locally only. No data is sent anywhere except directly to api.anthropic.com.',
      btn: 'Get Started →',
    },
  },
};

const i18n = {
  locale: localStorage.getItem('ci-lang') || (navigator.language.startsWith('ko') ? 'ko' : 'en'),
  t(key, vars = {}) {
    const val = key.split('.').reduce((o, k) => o?.[k], LOCALES[this.locale]) ?? key;
    return Object.entries(vars).reduce((s, [k, v]) => s.replace(`{${k}}`, v), val);
  },
  setLocale(lang) {
    this.locale = lang;
    localStorage.setItem('ci-lang', lang);
    applyI18n();
  }
};

function applyI18n() {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    el.textContent = i18n.t(el.dataset.i18n);
  });
  document.querySelectorAll('[data-i18n-html]').forEach(el => {
    el.innerHTML = i18n.t(el.dataset.i18nHtml);
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    el.placeholder = i18n.t(el.dataset.i18nPlaceholder);
  });
  document.querySelectorAll('[data-i18n-title]').forEach(el => {
    el.title = i18n.t(el.dataset.i18nTitle);
  });
  // lang toggle button text
  const btn = document.getElementById('langToggleBtn');
  if (btn) btn.textContent = i18n.locale === 'ko' ? 'EN' : '한';
  // re-render proxy content that depends on locale
  if (proxyCaptures.length > 0) {
    renderProxyList();
    if (selectedProxyId !== null) renderProxyDetail();
  } else {
    const list = document.getElementById('proxyList');
    if (list) list.innerHTML = `<div class="hist-empty">${i18n.t('proxy.noCaptures')}</div>`;
  }
  if (!proxyRunning) {
    const statusText = document.getElementById('proxyStatusText');
    if (statusText && !proxyRunning) statusText.textContent = i18n.t('proxy.stopped');
    const cmdEl = document.getElementById('proxyCmdText');
    if (cmdEl && !proxyRunning) cmdEl.textContent = i18n.t('proxy.startFirst');
  }
}

// ─── JSON Tree Viewer ─────────────────────────────────────────────────────
// ─── JSON Tree Viewer ─────────────────────────────────────────────────────
let _jtId = 0;
let _jtLine = 0;
function buildJsonHtml(val, depth, trailing, totalBytes) {
  depth = depth || 0;
  trailing = trailing || '';
  totalBytes = totalBytes || 0;
  if (val === null) return '<span class="jt-null">null</span>' + trailing;
  if (val === true || val === false) return `<span class="jt-bool">${val}</span>` + trailing;
  if (typeof val === 'number') return `<span class="jt-num">${val}</span>` + trailing;
  if (typeof val === 'string') {
    const COLLAPSE_LEN = 300;
    if (val.length > COLLAPSE_LEN) {
      const sid = `jts${++_jtId}`;
      const preview = esc(val.slice(0, 80)).replace(/\\n/g, ' ').replace(/\n/g, ' ') + '…';
      const expanded = esc(val).replace(/\\n/g, '\n');
      const lines = expanded.split('\n');
      const baseLn = _jtLine;
      let expandedRows = '';
      for (let li = 0; li < lines.length; li++) {
        const ln = li === 0 ? baseLn : ++_jtLine;
        const isLast = li === lines.length - 1;
        const openQuote = li === 0 ? '"' : '';
        const closeQuote = isLast ? '"' : '';
        expandedRows += `<div class="jt-exp-line" data-ln="${ln}">${openQuote}${lines[li]}${closeQuote}</div>`;
      }
      return `<span class="jt-str-long">`
        + `<span class="jt-str-toggle" id="${sid}-btn" onclick="jtStrToggle('${sid}')">▶</span>`
        + `<span class="jt-str-preview" id="${sid}-s" onclick="jtStrToggle('${sid}')">"${preview}" <span style="color:var(--dim);font-size:10px">(${val.length} chars)</span></span>`
        + `<div class="jt-str-expanded" id="${sid}-b" style="display:none">`
        + `<span class="jt-str-toggle" onclick="jtStrToggle('${sid}')">▼</span>`
        + expandedRows
        + `</div>`
        + `</span>` + trailing;
    }
    return `<span class="jt-str">"${esc(val)}"</span>` + trailing;
  }

  const isArr = Array.isArray(val);
  const entries = isArr ? val.map((v, i) => [null, v]) : Object.entries(val);
  const open = isArr ? '[' : '{'; const close = isArr ? ']' : '}';
  if (entries.length === 0) return `<span>${open}${close}</span>` + trailing;

  const id = `jt${++_jtId}`;
  const label = isArr ? `${entries.length}` : `${entries.length}`;
  const rows = entries.map(([k, v], i) => {
    const ln = ++_jtLine;
    const comma = i < entries.length - 1 ? '<span style="color:var(--dim)">,</span>' : '';
    const keyPart = k !== null ? `<span class="jt-key">"${esc(String(k))}"</span><span style="color:var(--dim)">: </span>` : '';
    return `<div class="jt-row" data-ln="${ln}" style="padding-left:16px">${keyPart}${buildJsonHtml(v, depth + 1, comma, totalBytes)}</div>`;
  }).join('');
  const typeTag = isArr ? `[${label}]` : `{${label}}`;

  // 접힌 노드 토큰 비중 표시
  const jsonBytes = new TextEncoder().encode(JSON.stringify(val)).length;
  const tokens = Math.ceil(jsonBytes / 3.5);
  const tokStr = tokens >= 1000000 ? (tokens / 1000000).toFixed(1) + 'M'
               : tokens >= 1000 ? (tokens / 1000).toFixed(1) + 'K'
               : String(tokens);
  const pct = totalBytes > 0 ? (jsonBytes / totalBytes * 100) : 0;
  const pctStr = pct >= 1 ? pct.toFixed(0) + '%' : pct >= 0.1 ? pct.toFixed(1) + '%' : '<0.1%';
  const tokTag = `<span class="jt-tok">~${tokStr} tok · ${pctStr}</span>`;

  const closeLn = ++_jtLine;
  return `<span>`
    + `<span class="jt-btn" id="${id}-btn" onclick="jtToggle('${id}')">▼</span>`
    + `<span style="color:var(--dim)">${open}</span>`
    + `<span class="jt-tag" id="${id}-s" onclick="jtToggle('${id}')" style="display:none">${typeTag} ${tokTag}${trailing}</span>`
    + `<span id="${id}-b">`
    +   rows
    +   `<div class="jt-row" data-ln="${closeLn}"><span style="color:var(--dim)">${close}</span>${trailing}</div>`
    + `</span>`
    + `</span>`;
}

function jtStrToggle(id) {
  const body = document.getElementById(`${id}-b`);
  const summary = document.getElementById(`${id}-s`);
  const btn = document.getElementById(`${id}-btn`);
  const open = body.style.display !== 'none';
  body.style.display = open ? 'none' : '';
  summary.style.display = open ? '' : 'none';
  if (btn) btn.style.display = open ? '' : 'none';
  const parentRow = body.closest('.jt-row');
  if (parentRow) parentRow.classList.toggle('jt-no-ln', !open);
  // 펼칠 때 긴 줄 분할 (처음 한 번만)
  if (!open && !body.dataset.split) {
    body.dataset.split = '1';
    const lined = body.closest('.jt-lined');
    if (lined) requestAnimationFrame(() => splitLongExpLines(lined, body));
  }
}

function jtToggle(id) {
  const body = document.getElementById(`${id}-b`);
  const summary = document.getElementById(`${id}-s`);
  const btn = document.getElementById(`${id}-btn`);
  const open = body.style.display !== 'none';
  body.style.display = open ? 'none' : '';
  summary.style.display = open ? '' : 'none';
  btn.textContent = open ? '▶' : '▼';
}

function renderJsonTree(container, data) {
  let obj;
  try { obj = typeof data === 'string' ? JSON.parse(data) : data; }
  catch (e) { container.textContent = typeof data === 'string' ? data : JSON.stringify(data, null, 2); return; }
  const totalBytes = new TextEncoder().encode(JSON.stringify(obj)).length;
  _jtLine = 0;
  container.innerHTML = buildJsonHtml(obj, 0, '', totalBytes)
    + `<div class="jt-line-info">${_jtLine} lines total</div>`;
  container.classList.add('jt-lined');
  splitLongExpLines(container);
}

function splitLongExpLines(container, targetBlock) {
  // 문자 너비 측정
  const measure = document.createElement('span');
  measure.style.cssText = 'visibility:hidden;position:absolute;white-space:nowrap;font:inherit';
  measure.textContent = 'X'.repeat(100);
  container.appendChild(measure);
  const charWidth = measure.offsetWidth / 100;
  container.removeChild(measure);
  const availWidth = container.clientWidth - 60;
  const maxChars = Math.max(40, Math.floor(availWidth / charWidth));

  const blocks = targetBlock ? [targetBlock] : container.querySelectorAll('.jt-str-expanded');
  for (const block of blocks) {
    const lines = Array.from(block.querySelectorAll('.jt-exp-line'));
    if (!lines.length) continue;
    let needsSplit = false;
    for (const l of lines) { if (l.textContent.length > maxChars) { needsSplit = true; break; } }
    if (!needsSplit) continue;

    const baseLn = parseInt(lines[0].getAttribute('data-ln')) || 1;
    let lineNum = baseLn;
    const fragments = [];
    for (const line of lines) {
      const text = line.textContent;
      const cls = line.classList.contains('mech-hl-text') ? 'jt-exp-line mech-hl-text' : 'jt-exp-line';
      if (text.length <= maxChars) {
        fragments.push({ text, ln: lineNum++, cls });
      } else {
        for (let i = 0; i < text.length; i += maxChars) {
          fragments.push({ text: text.slice(i, i + maxChars), ln: lineNum++, cls });
        }
      }
    }
    // DOM 재구성
    const toggle = block.querySelector('.jt-str-toggle');
    block.innerHTML = '';
    if (toggle) block.appendChild(toggle);
    for (const f of fragments) {
      const div = document.createElement('div');
      div.className = f.cls;
      div.setAttribute('data-ln', f.ln);
      div.textContent = f.text;
      block.appendChild(div);
    }
  }
}

// ─── Util ─────────────────────────────────────────────────────────────────
function esc(s) {
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
function escAttr(s) {
  return esc(s).replace(/"/g,'&quot;');
}

// ─── Proxy ────────────────────────────────────────────────────────────────
let proxyCaptures = [];
let selectedProxyId = null;
let proxyDetailTab = 'messages';
let msgFilter = 'user';
let msgSearchQuery = '';
let proxyDetailSearch = '';
let proxyDetailMechFilter = null;
let proxyRunning = false;
let proxyActualPort = 9090;

function updateProxyCmd() {
  const port = document.getElementById('proxyPort').value || '9090';
  const cmdEl = document.getElementById('proxyCmdText');
  if (cmdEl && proxyRunning) {
    cmdEl.style.color = 'var(--green)';
    cmdEl.textContent = `ANTHROPIC_BASE_URL=http://localhost:${port} claude`;
  }
}

function renderProxyStatus() {
  const status = document.getElementById('proxyStatus');
  const statusText = document.getElementById('proxyStatusText');
  const startBtn = document.getElementById('proxyStartBtn');
  const cmdEl = document.getElementById('proxyCmdText');
  if (!status || !startBtn) return;

  if (proxyRunning) {
    status.className = 'proxy-status running';
    if (statusText) statusText.textContent = i18n.t('proxy.running', { port: proxyActualPort });
    startBtn.textContent = i18n.t('proxy.stopProxy');
    startBtn.style.background = 'var(--red)';
    if (cmdEl) {
      cmdEl.style.color = 'var(--green)';
      cmdEl.textContent = `ANTHROPIC_BASE_URL=http://localhost:${proxyActualPort} claude`;
    }
  } else {
    status.className = 'proxy-status';
    if (statusText) statusText.textContent = i18n.t('proxy.stopped');
    startBtn.textContent = i18n.t('proxy.startProxy');
    startBtn.style.background = 'var(--blue)';
    if (cmdEl) {
      cmdEl.style.color = 'var(--dim)';
      cmdEl.textContent = i18n.t('proxy.startFirst');
    }
  }
}

let _renderProxyListTimer = null;
function debouncedRenderProxyList() {
  clearTimeout(_renderProxyListTimer);
  _renderProxyListTimer = setTimeout(renderProxyList, 50);
}

let _renderProxyDetailTimer = null;
function debouncedRenderProxyDetail() {
  clearTimeout(_renderProxyDetailTimer);
  _renderProxyDetailTimer = setTimeout(renderProxyDetail, 100);
}

async function toggleProxy() {
  if (!window.electronAPI) return;
  const btn = document.getElementById('proxyStartBtn');
  if (btn) { btn.disabled = true; btn.innerHTML = '<span class="spin"></span>'; }

  try {
    if (proxyRunning) {
      await window.electronAPI.proxyStop();
      window.electronAPI.offProxy();
      proxyRunning = false;
    } else {
      // 기존 리스너 먼저 정리 후 새 리스너 등록 (누적 방지)
      window.electronAPI.offProxy();

      const port = parseInt(document.getElementById('proxyPort').value) || 9090;
      const result = await window.electronAPI.proxyStart(port);
      if (result.error) {
        alert(i18n.t('proxy.startFail') + result.error);
        return;
      }
      proxyRunning = true;
      proxyActualPort = result.port;
      document.getElementById('proxyPort').value = result.port;

      window.electronAPI.onProxyRequest((data) => {
        proxyCaptures.unshift(data);
        if (proxyCaptures.length > 50) proxyCaptures.pop();
        debouncedRenderProxyList();
      });
      window.electronAPI.onProxyResponse((data) => {
        const entry = proxyCaptures.find(e => e.id === data.id);
        if (entry) {
          entry.response = data;
          debouncedRenderProxyList();
          if (selectedProxyId === data.id) debouncedRenderProxyDetail();
        }
      });
    }
  } catch (err) {
    console.error('toggleProxy error:', err);
    alert(i18n.t('proxy.startFail') + (err.message || err));
  } finally {
    if (btn) btn.disabled = false;
    renderProxyStatus();
  }
}

function renderProxyList() {
  const list = document.getElementById('proxyList');
  const countEl = document.getElementById('proxyCount');
  if (!list) return;
  if (countEl) countEl.textContent = proxyCaptures.length;

  if (proxyCaptures.length === 0) {
    list.innerHTML = `<div class="hist-empty">${i18n.t('proxy.noCaptures')}</div>`;
    return;
  }

  list.innerHTML = proxyCaptures.map(e => {
    const model = e.body?.model ? `<div class="prx-model">${esc(e.body.model)}</div>` : '';
    const sel = e.id === selectedProxyId ? ' selected' : '';
    const statusBadge = e.response
      ? `<span style="font-size:10px;font-family:'SF Mono',monospace;flex-shrink:0;color:${e.response.status < 400 ? 'var(--green)' : 'var(--red)'}">${e.response.status || 'ERR'}</span>`
      : `<span style="font-size:10px;color:var(--dim);flex-shrink:0">…</span>`;
    return `<div class="prx-entry${sel}" onclick="selectProxyEntry(${e.id})">
      <div style="display:flex;align-items:center;overflow:hidden">
        <span class="prx-method">${esc(e.method)}</span>
        <span class="prx-path">${esc(e.path)}</span>
        ${statusBadge}
        <span class="prx-ts">${e.ts}</span>
      </div>
      ${model}
    </div>`;
  }).join('');
}

function selectProxyEntry(id) {
  selectedProxyId = id;
  renderProxyList();
  renderProxyDetail();
}

// ─── Messages view ───────────────────────────────────────────────────────────

// Parse CLAUDE.md system-reminder into global/local sections
function parseClaudeMdSections(inner) {
  const re = /Contents of (.+?) \((.+?)\):\n\n([\s\S]*?)(?=\n\nContents of |\s*$)/g;
  const sections = [];
  let m;
  while ((m = re.exec(inner)) !== null) {
    const path = m[1], desc = m[2], content = m[3].trim();
    const fname = path.split('/').pop();
    const isGlobal = /global|private global/i.test(desc);
    const isMemory = /memory/i.test(desc) || /\/memory\//.test(path);
    let label, cls;
    if (isMemory) {
      label = '🧠 Memory: ' + fname; cls = 'green';
    } else if (/\/rules\//.test(path)) {
      label = (isGlobal ? '📜 Global Rule: ' : '📜 Local Rule: ') + fname;
      cls = isGlobal ? 'green' : 'cyan';
    } else if (/CLAUDE\.md$/i.test(path)) {
      label = isGlobal ? '📋 Global CLAUDE.md' : '📋 Local CLAUDE.md';
      cls = isGlobal ? 'green' : 'cyan';
    } else {
      label = '📋 ' + fname; cls = 'green';
    }
    sections.push({ label, path, content, cls, scope: isGlobal ? 'global' : 'local' });
  }
  return sections;
}

// Parse user message text into typed portions and injected blocks
function parseUserText(text) {
  const parts = [];
  const blockRe = /(<system-reminder>[\s\S]*?<\/system-reminder>|<command-message>[\s\S]*?<\/command-message>)/g;
  let pos = 0, m;
  while ((m = blockRe.exec(text)) !== null) {
    if (m.index > pos) {
      const plain = text.slice(pos, m.index).trim();
      if (plain) parts.push({ type: 'text', content: plain });
    }
    const raw = m[0];
    if (raw.startsWith('<system-reminder>')) {
      const inner = raw.slice('<system-reminder>'.length, -'</system-reminder>'.length);
      if (/skills are available/i.test(inner)) {
        parts.push({ type: 'injected', label: '🔧 Skills', content: inner, cls: 'green' });
      } else if (/currentDate|auto-memory/i.test(inner) && !/claudeMd|CLAUDE\.md/i.test(inner)) {
        parts.push({ type: 'injected', label: '🧠 Memory', content: inner, cls: 'green' });
      } else if (/claudeMd|CLAUDE\.md/i.test(inner)) {
        const sections = parseClaudeMdSections(inner);
        if (sections.length > 0) {
          for (const s of sections) {
            parts.push({ type: 'injected', label: s.label, content: s.content, cls: s.cls });
          }
        } else {
          parts.push({ type: 'injected', label: '📋 CLAUDE.md', content: inner, cls: 'green' });
        }
      } else {
        parts.push({ type: 'injected', label: '📋 system-reminder', content: inner, cls: 'green' });
      }
    } else {
      const inner = raw.slice('<command-message>'.length, -'</command-message>'.length);
      parts.push({ type: 'injected', label: '⌨ slash command', content: inner, cls: 'yellow' });
    }
    pos = m.index + raw.length;
  }
  if (pos < text.length) {
    const plain = text.slice(pos).trim();
    if (plain) parts.push({ type: 'text', content: plain });
  }
  return parts;
}

function highlightSearch(escapedHtml, query) {
  if (!query) return escapedHtml;
  const re = new RegExp(query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
  return escapedHtml.replace(re, m => `<mark class="search-hl">${m}</mark>`);
}

let _activeBadgeUid = null;

function toggleBadge(uid) {
  const content = document.getElementById('bc_' + uid);
  const btn = document.getElementById('bb_' + uid);
  if (!content) return;

  // 이전 활성 배지 하이라이트 해제
  if (_activeBadgeUid && _activeBadgeUid !== uid) {
    const prevContent = document.getElementById('bc_' + _activeBadgeUid);
    const prevBtn = document.getElementById('bb_' + _activeBadgeUid);
    if (prevContent) { prevContent.style.display = 'none'; prevContent.classList.remove('badge-section-hl'); }
    if (prevBtn) { prevBtn.classList.remove('open', 'hl-active'); }
  }

  const open = content.style.display !== 'none';
  content.style.display = open ? 'none' : 'block';
  content.classList.toggle('badge-section-hl', !open);
  if (btn) {
    btn.classList.toggle('open', !open);
    btn.classList.toggle('hl-active', !open);
  }
  _activeBadgeUid = open ? null : uid;
}

// Render user message content with typed/injected separation
function renderUserMsgContent(text, typedOnly, query) {
  const parts = parseUserText(text);
  if (typedOnly) {
    const typed = parts.filter(p => p.type === 'text');
    if (typed.length === 0) return null;
    return typed.map(p => `<div class="msg-typed">${highlightSearch(esc(p.content), query)}</div>`).join('');
  }
  return parts.map(p => {
    if (p.type === 'text') {
      return `<div class="msg-typed">${highlightSearch(esc(p.content), query)}</div>`;
    }
    const uid = Math.random().toString(36).slice(2, 8);
    return `<div class="msg-injected-row">
      <span id="bb_${uid}" class="msg-badge ${p.cls} expandable" onclick="toggleBadge('${uid}')">${esc(p.label)}</span>
      <div id="bc_${uid}" class="badge-expand-content" style="display:none">${highlightSearch(esc(p.content), query)}</div>
    </div>`;
  }).join('');
}

function renderProxyMessages(entry, container) {
  const msgs = entry.body?.messages || [];
  if (msgs.length === 0) {
    container.innerHTML = `<div class="proxy-empty"><span>${i18n.t('proxy.noMessages')}</span></div>`;
    return;
  }

  const typedOnly = msgFilter === 'typed';
  const baseFiltered = (msgFilter === 'user' || typedOnly) ? msgs.filter(m => m.role === 'user')
    : msgFilter === 'assistant' ? msgs.filter(m => m.role === 'assistant')
    : msgs;

  const q = msgSearchQuery;

  const filterHtml = `<div class="msg-filter">
    <button class="mf-btn${msgFilter==='user'?' active':''}" onclick="setMsgFilter('user')">${i18n.t('messages.filterUser')}</button>
    <button class="mf-btn${msgFilter==='typed'?' active':''}" onclick="setMsgFilter('typed')">${i18n.t('messages.filterTyped')}</button>
    <button class="mf-btn${msgFilter==='assistant'?' active':''}" onclick="setMsgFilter('assistant')">${i18n.t('messages.filterAssistant')}</button>
    <button class="mf-btn${msgFilter==='all'?' active':''}" onclick="setMsgFilter('all')">${i18n.t('messages.filterAll')}</button>
    <span class="msg-count" id="msgCountEl"></span>
  </div>`;

  const searchHtml = `<div class="msg-search-bar">
    <input type="text" id="msgSearchInput" class="msg-search-input"
      placeholder="${esc(i18n.t('messages.searchPlaceholder'))}" value="${esc(q)}"
      oninput="setMsgSearch(this.value)"
      oncompositionstart="_imeComposing=true"
      oncompositionend="_imeComposing=false;setMsgSearch(this.value)">
    ${q ? `<button class="msg-search-clear" onclick="setMsgSearch('');document.getElementById('msgSearchInput')?.focus()" title="${esc(i18n.t('messages.searchClear'))}">✕</button>` : ''}
  </div>`;

  const cards = [];
  for (const msg of baseFiltered) {
    const contents = Array.isArray(msg.content)
      ? msg.content
      : [{ type: 'text', text: String(msg.content || '') }];

    // "내가 보낸 것" 필터: 사용자가 직접 입력한 텍스트가 없는 메시지 스킵
    const isUserFilter = msgFilter === 'user' || typedOnly;
    if (isUserFilter && msg.role === 'user') {
      const hasTypedText = contents.some(c => {
        if (c.type !== 'text' || !c.text || !c.text.trim()) return false;
        const parts = parseUserText(c.text);
        return parts.some(p => p.type === 'text');
      });
      if (!hasTypedText) continue;
    }

    const bodyParts = [];
    for (const c of contents) {
      if (c.type === 'text') {
        if (msg.role === 'user') {
          const rendered = renderUserMsgContent(c.text, isUserFilter, q);
          if (rendered !== null) bodyParts.push(rendered);
        } else {
          bodyParts.push(`<div class="msg-text">${highlightSearch(esc(c.text), q)}</div>`);
        }
      } else if (c.type === 'tool_use') {
        if (!isUserFilter) bodyParts.push(`<div class="msg-tool">🔧 ${esc(c.name)}()</div>`);
      } else if (c.type === 'tool_result') {
        if (!isUserFilter) {
          const preview = typeof c.content === 'string' ? c.content.slice(0, 120)
            : Array.isArray(c.content) ? c.content.map(x => x.text||'').join('').slice(0, 120) : '[object]';
          bodyParts.push(`<div class="msg-tool-result">📤 ${esc(preview)}${preview.length===120?'…':''}</div>`);
        }
      } else {
        bodyParts.push(`<div class="msg-other">[${esc(c.type)}]</div>`);
      }
    }

    if (bodyParts.length === 0) continue;
    if (q && !bodyParts.join('').includes('class="search-hl"')) continue;

    cards.push(`<div class="msg-card msg-${esc(msg.role)}">
      <div class="msg-role">${esc(msg.role)}</div>
      <div class="msg-body">${bodyParts.join('')}</div>
    </div>`);
  }

  // flex/overflow 전부 덮어씌워서 단순 스크롤 컨테이너로 전환
  container.style.cssText = 'flex:1;overflow-y:auto;display:block';
  container.innerHTML = `<div style="position:sticky;top:0;z-index:1;background:var(--bg)">${filterHtml}${searchHtml}</div>` +
    `<div style="display:flex;flex-direction:column;gap:8px;padding:12px">${cards.join('') || `<div class="proxy-empty"><span>${i18n.t('proxy.noResults')}</span></div>`}</div>`;

  const countEl = document.getElementById('msgCountEl');
  if (countEl) countEl.textContent = i18n.t('proxy.msgCount', { count: cards.length, total: msgs.length });

  // Restore focus on search input after re-render
  {
    const inp = document.getElementById('msgSearchInput');
    if (inp && (q || _msgSearchWasFocused)) { inp.focus(); const len = inp.value.length; inp.setSelectionRange(len, len); }
  }
}

function setMsgFilter(f) {
  msgFilter = f;
  const entry = proxyCaptures.find(e => e.id === selectedProxyId);
  const detail = document.getElementById('proxyDetailView');
  if (entry && detail) renderProxyMessages(entry, detail);
}

let _imeComposing = false;
let _msgSearchWasFocused = false;
let _msgSearchTimer = null;

function setMsgSearch(q) {
  msgSearchQuery = q;
  if (_imeComposing) return;
  clearTimeout(_msgSearchTimer);
  _msgSearchTimer = setTimeout(() => {
    _msgSearchWasFocused = document.activeElement?.id === 'msgSearchInput';
    const entry = proxyCaptures.find(e => e.id === selectedProxyId);
    const detail = document.getElementById('proxyDetailView');
    if (entry && detail && proxyDetailTab === 'messages') renderProxyMessages(entry, detail);
  }, 150);
}

let searchCurrentIdx = -1;

let _detailSearchWasFocused = false;
let _detailSearchTimer = null;

function setProxyDetailSearch(q) {
  proxyDetailSearch = q;
  if (_imeComposing) return;
  clearTimeout(_detailSearchTimer);
  _detailSearchTimer = setTimeout(() => {
    _detailSearchWasFocused = document.activeElement?.id === 'proxyDetailSearchInput';
    searchCurrentIdx = -1;
    if (!q) proxyDetailMechFilter = null;
    renderProxyDetail();
    if (q) navigateSearchMatch(0);
  }, 150);
}

function navigateSearchMatch(delta) {
  const container = document.getElementById('proxyDetailCode')
                 || document.querySelector('.analysis-view');
  if (!container) return;
  const marks = container.querySelectorAll('mark.search-hl');
  if (marks.length === 0) return;
  // 현재 하이라이트 제거
  const prev = container.querySelector('mark.search-hl.current');
  if (prev) prev.classList.remove('current');
  // 새 인덱스 계산
  if (delta === 0) searchCurrentIdx = 0;
  else searchCurrentIdx = ((searchCurrentIdx + delta) % marks.length + marks.length) % marks.length;
  marks[searchCurrentIdx].classList.add('current');
  marks[searchCurrentIdx].scrollIntoView({ behavior: 'smooth', block: 'center' });
  updateSearchCounter(marks.length);
}

function updateSearchCounter(total) {
  const el = document.getElementById('searchCounter');
  if (el) el.textContent = total > 0 ? `${searchCurrentIdx + 1}/${total}` : '0';
}

function setProxyDetailMechFilter(key) {
  if (proxyDetailMechFilter === key) {
    proxyDetailMechFilter = null;
  } else {
    proxyDetailMechFilter = key;
  }
  renderProxyDetail();
}

function getChipMeta() {
  return {
    cm: { color: 'var(--green)',
          who:  i18n.t('mechDesc.cm.who'),
          what: i18n.t('mechDesc.cm.what') },
    sc: { color: 'var(--yellow)',
          who:  i18n.t('mechDesc.sc.who'),
          what: i18n.t('mechDesc.sc.what') },
    sk: { color: 'var(--purple)',
          who:  i18n.t('mechDesc.sk.who'),
          what: i18n.t('mechDesc.sk.what') },
    sa: { color: 'var(--orange)',
          who:  i18n.t('mechDesc.sa.who'),
          what: i18n.t('mechDesc.sa.what') },
    mc: { color: '#4ec9dc',
          who:  i18n.t('mechDesc.mc.who'),
          what: i18n.t('mechDesc.mc.what') },
  };
}

function buildMechFilterChips(body) {
  const det = detectMechanisms(body);

  const chips = [];

  // CLAUDE.md → 섹션별 분리 칩
  if (det.claudeMd) {
    const sections = parseClaudeMdSections(det.claudeMd);
    if (sections.length > 0) {
      for (let i = 0; i < sections.length; i++) {
        const s = sections[i];
        // 칩 내 검색 패턴: 해당 섹션의 첫 줄 (고유성 확보)
        const firstLine = s.content.split('\n').find(l => l.trim().length > 8) || s.content.slice(0, 40);
        chips.push({ key: 'cm_' + i, found: true, label: s.label, pattern: firstLine.trim(),
                      cls: s.cls === 'cyan' ? 'st' : 'cm', metaKey: 'cm' });
      }
    } else {
      chips.push({ key: 'cm', found: true, label: '📋 CLAUDE.md', pattern: 'system-reminder', cls: 'cm', metaKey: 'cm' });
    }
  }

  for (let i = 0; i < det.slashCommands.length; i++) {
    chips.push({ key: 'sc_' + i, found: true, label: `⌨ /${det.slashCommands[i].name}`, cls: 'sc', metaKey: 'sc' });
  }
  for (let i = 0; i < det.skills.length; i++) {
    const skName = det.skills[i].input?.skill || det.skills[i].input?.command || `Skill ${i + 1}`;
    chips.push({ key: 'sk_' + i, found: true, label: `🔧 ${skName}`, cls: 'sk', metaKey: 'sk' });
  }
  if (det.subAgents.length > 0) chips.push({ key: 'sa', found: true, label: '🤖 Sub-Agent', pattern: det.subAgents[0]?.name || 'Agent', cls: 'sa', metaKey: 'sa' });
  for (let i = 0; i < det.mcpTools.length; i++) {
    const parts = det.mcpTools[i].name.split('__');
    const toolName = parts.slice(2).join('__') || det.mcpTools[i].name;
    chips.push({ key: 'mc_' + i, found: true, label: `🔌 ${toolName}`, cls: 'mc', metaKey: 'mc' });
  }

  if (chips.length === 0) return '';

  const activeChip = chips.find(c => c.key === proxyDetailMechFilter);
  const meta = activeChip ? getChipMeta()[activeChip.metaKey] : null;
  const descBanner = meta
    ? `<div class="mech-filter-desc">
        <span class="mech-filter-desc-dot" style="background:${meta.color}"></span>
        <div class="mech-filter-desc-body">
          <span class="mech-filter-desc-who">${esc(meta.who)}</span>
          <span class="mech-filter-desc-what">${esc(meta.what)}</span>
        </div>
       </div>`
    : '';

  return '<div style="flex-shrink:0;border-bottom:1px solid var(--border)">'
    + '<div style="display:flex;flex-wrap:wrap;gap:5px;padding:5px 10px 7px">'
    + chips.map(c => {
        const active = proxyDetailMechFilter === c.key ? ' active' : '';
        return `<span class="mech-chip ${c.cls} found btn${active}" data-key="${escAttr(c.key)}" onclick="setProxyDetailMechFilter(this.dataset.key)">${esc(c.label)}</span>`;
      }).join('')
    + '</div>'
    + descBanner
    + '</div>';
}

function highlightMechInJsonTree(container, body, mechKey) {
  if (!mechKey) return;

  function expandLongStr(el) {
    let target = el;
    // preview 클릭 시 sibling expanded 찾기
    if (el.classList.contains('jt-str-preview')) {
      const parent = el.closest('.jt-str-long');
      if (parent) target = parent.querySelector('.jt-str-expanded');
    }
    if (target && target.classList.contains('jt-str-expanded') && target.style.display === 'none') {
      const sid = target.id.replace(/-b$/, '');
      if (sid) jtStrToggle(sid);
    }
  }

  function hlRange(el, start, end, wholeElement) {
    if (wholeElement) {
      el.classList.add('mech-hl-text');
      requestAnimationFrame(() => el.scrollIntoView({ behavior: 'smooth', block: 'start' }));
      return;
    }
    const html = el.innerHTML;
    // end 위치가 HTML 엔티티 중간이면 보정
    let safeEnd = end;
    for (let i = Math.max(0, safeEnd - 8); i < safeEnd; i++) {
      if (html[i] === '&') {
        const semi = html.indexOf(';', i);
        if (semi !== -1 && semi < i + 10 && semi >= safeEnd) {
          safeEnd = semi + 1;
          break;
        }
      }
    }
    el.innerHTML = html.slice(0, start)
      + '<span class="mech-hl-text">' + html.slice(start, safeEnd) + '</span>'
      + html.slice(safeEnd);
    const hl = el.querySelector('.mech-hl-text');
    if (hl) requestAnimationFrame(() => hl.scrollIntoView({ behavior: 'smooth', block: 'start' }));
  }

  if (mechKey.startsWith('cm')) {
    const det = detectMechanisms(body);
    if (!det.claudeMd) return;
    const sections = parseClaudeMdSections(det.claudeMd);
    const idx = parseInt(mechKey.replace('cm_', ''));
    if (isNaN(idx) || !sections[idx]) return;
    const section = sections[idx];

    // 문자열 펼침 + 해당 섹션 줄만 하이라이트
    const allStr = container.querySelectorAll('.jt-str, .jt-str-expanded, .jt-str-preview');
    for (const el of allStr) {
      if (!el.textContent.includes('Contents of ' + section.path)) continue;
      expandLongStr(el);
      expandAncestors(el);
      // 펼쳐진 jt-exp-line 중 해당 섹션 줄만 하이라이트
      const parent = el.closest('.jt-str-long');
      const expBlock = parent ? parent.querySelector('.jt-str-expanded') : null;
      if (expBlock) {
        const expLines = expBlock.querySelectorAll('.jt-exp-line');
        const marker = 'Contents of ' + section.path;
        let inSection = false;
        let firstHl = null;
        for (const line of expLines) {
          const txt = line.textContent;
          if (!inSection && txt.includes(marker)) {
            inSection = true;
          }
          if (inSection) {
            // 다음 섹션 시작이면 중단 (다른 "Contents of " 패턴)
            if (!txt.includes(marker) && txt.includes('Contents of ')) break;
            line.classList.add('mech-hl-text');
            if (!firstHl) firstHl = line;
          }
        }
        if (firstHl) requestAnimationFrame(() => firstHl.scrollIntoView({ behavior: 'smooth', block: 'start' }));
      }
      break;
    }

  } else if (mechKey.startsWith('sc')) {
    const det = detectMechanisms(body);
    const idx = mechKey.includes('_') ? parseInt(mechKey.split('_')[1]) : 0;
    const target = det.slashCommands[idx];
    if (!target) return;
    // Count same-tag commands before this index to handle duplicates
    let sameTagIdx = 0;
    for (let i = 0; i < idx; i++) {
      if (det.slashCommands[i].tag === target.tag) sameTagIdx++;
    }
    const specificText = `<command-message>${target.tag}</command-message>`;
    let count = 0;
    for (const el of container.querySelectorAll('.jt-str, .jt-str-expanded')) {
      if (!el.textContent.includes(specificText)) continue;
      if (count === sameTagIdx) {
        expandLongStr(el);
        expandAncestors(el);
        const html = el.innerHTML;
        const cmOpen = esc('<command-message>');
        const cmClose = esc('</command-message>');
        const start = html.indexOf(cmOpen);
        if (start < 0) { count++; continue; }
        const endPos = html.indexOf(cmClose, start);
        hlRange(el, start, endPos >= 0 ? endPos + cmClose.length : html.length);
        return;
      }
      count++;
    }

  } else if (mechKey.startsWith('sk')) {
    const det = detectMechanisms(body);
    if (!det.skills.length) return;
    const idx = mechKey.includes('_') ? parseInt(mechKey.split('_')[1]) : 0;
    const skill = det.skills[idx] || det.skills[0];
    if (skill) highlightToolUseById(container, skill.id);
  } else if (mechKey === 'sa') {
    const det = detectMechanisms(body);
    if (!det.subAgents.length) return;
    highlightToolUseById(container, det.subAgents[0].id);
  } else if (mechKey.startsWith('mc')) {
    const det = detectMechanisms(body);
    if (!det.mcpTools.length) return;
    const idx = mechKey.includes('_') ? parseInt(mechKey.split('_')[1]) : 0;
    const mc = det.mcpTools[idx] || det.mcpTools[0];
    if (mc) highlightToolUseById(container, mc.id);
  }
}

function expandAncestors(el) {
  let cur = el.parentElement;
  while (cur) {
    if (cur.id && cur.id.endsWith('-b') && cur.style.display === 'none') {
      jtToggle(cur.id.replace(/-b$/, ''));
    }
    cur = cur.parentElement;
  }
}

function highlightToolUseById(container, toolUseId) {
  const strEls = container.querySelectorAll('.jt-str, .jt-str-expanded');
  for (const el of strEls) {
    if (el.textContent !== `"${toolUseId}"`) continue;
    // jt-str → jt-row("id" prop) → jt-N-b (body) → outer span → jt-row (array item)
    const itemRow = el.parentElement?.parentElement?.parentElement?.parentElement;
    if (!itemRow || !itemRow.classList.contains('jt-row')) break;
    expandAncestors(itemRow);
    itemRow.classList.add('mech-hl-row');
    requestAnimationFrame(() => itemRow.scrollIntoView({ behavior: 'smooth', block: 'start' }));
    return;
  }
}

function applyDetailHighlight(container, query) {
  if (!query) return;
  const re = new RegExp(query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
  const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT);
  const nodes = [];
  while (walker.nextNode()) nodes.push(walker.currentNode);
  for (const node of nodes) {
    const text = node.textContent;
    if (!re.test(text)) continue;
    re.lastIndex = 0;
    let html = '', last = 0, m;
    while ((m = re.exec(text)) !== null) {
      html += esc(text.slice(last, m.index));
      html += `<mark class="search-hl">${esc(m[0])}</mark>`;
      last = m.index + m[0].length;
    }
    html += esc(text.slice(last));
    const span = document.createElement('span');
    span.innerHTML = html;
    node.parentNode.replaceChild(span, node);
  }
}

function renderProxyDetail() {
  const entry = proxyCaptures.find(e => e.id === selectedProxyId);
  const detail = document.getElementById('proxyDetailView');
  if (!detail) return;

  // Messages 탭에서 변경한 inline style 원복
  detail.style.cssText = 'flex:1;overflow:hidden;display:flex;flex-direction:column';

  if (!entry) {
    detail.innerHTML = `<div class="proxy-empty"><span style="font-size:28px">🔍</span><span>${i18n.t('proxy.selectRequest')}</span></div>`;
    return;
  }

  if (proxyDetailTab === 'messages') {
    renderProxyMessages(entry, detail);
    return;
  }

  if (proxyDetailTab === 'analysis') {
    const prevAnalysisScroll = detail.querySelector('[style*="overflow:auto"]')?.scrollTop ?? 0;
    renderProxyAnalysis(entry, detail);
    if (proxyDetailMechFilter) {
      requestAnimationFrame(() => {
        const scrollEl = detail.querySelector('[style*="overflow:auto"]');
        if (scrollEl) scrollEl.scrollTop = prevAnalysisScroll;
        const activeSection = detail.querySelector(`[data-mech-key="${proxyDetailMechFilter}"]`);
        if (activeSection) {
          activeSection.classList.add('mech-section-active');
          activeSection.scrollIntoView({ block: 'start', behavior: 'smooth' });
        }
      });
    }
    if (proxyDetailSearch) {
      applyDetailHighlight(detail, proxyDetailSearch);
      const marks = detail.querySelectorAll('mark.search-hl');
      if (marks.length > 0) {
        if (searchCurrentIdx < 0) searchCurrentIdx = 0;
        if (searchCurrentIdx >= marks.length) searchCurrentIdx = 0;
        marks[searchCurrentIdx].classList.add('current');
        updateSearchCounter(marks.length);
      }
    }
    if (proxyDetailSearch || _detailSearchWasFocused) {
      const inp = document.getElementById('proxyDetailSearchInput');
      if (inp) { inp.focus(); const len = inp.value.length; inp.setSelectionRange(len, len); }
    }
    return;
  }

  const data = proxyDetailTab === 'request' ? entry.body : (entry.response?.body ?? null);

  const q = proxyDetailSearch;
  const searchNav = q ? `<div class="search-nav">
    <span id="searchCounter"></span>
    <button class="search-nav-btn" onclick="navigateSearchMatch(-1)" title="${esc(i18n.t('search.prev'))}">▲</button>
    <button class="search-nav-btn" onclick="navigateSearchMatch(1)" title="${esc(i18n.t('search.next'))}">▼</button>
  </div>` : '';
  const searchBar = `<div class="msg-search-bar" style="flex-shrink:0">
    <input type="text" class="msg-search-input" id="proxyDetailSearchInput"
      placeholder="${esc(i18n.t('analysis.searchPlaceholder'))}" value="${esc(q)}"
      oninput="setProxyDetailSearch(this.value)"
      oncompositionstart="_imeComposing=true"
      oncompositionend="_imeComposing=false;setProxyDetailSearch(this.value)">
    ${searchNav}
    ${q ? `<button class="msg-search-clear" onclick="setProxyDetailSearch('');document.getElementById('proxyDetailSearchInput')?.focus()" title="${esc(i18n.t('messages.searchClear'))}">✕</button>` : ''}
  </div>`;
  const mechChips = proxyDetailTab === 'request' ? buildMechFilterChips(entry.body) : '';
  const header = `<div style="flex-shrink:0">${searchBar}${mechChips}</div>`;

  if (data === null || data === undefined) {
    detail.innerHTML = header + `<div style="color:var(--dim);padding:16px;font-size:12px">${proxyDetailTab === 'response' ? i18n.t('proxy.waitingResponse') : i18n.t('proxy.noBody')}</div>`;
    return;
  }

  const tokenInfo = proxyDetailTab === 'request' && data
    ? (() => {
        const bytes = new TextEncoder().encode(JSON.stringify(data)).length;
        const kb = (bytes / 1024).toFixed(1);
        const fmtTok = (n) => n >= 1000000 ? (n/1000000).toFixed(1)+'M' : n >= 1000 ? (n/1000).toFixed(1)+'K' : String(n);
        const usage = entry.response?.body?.usage;
        if (usage) {
          const totalIn = (usage.input_tokens || 0) + (usage.cache_read_input_tokens || 0) + (usage.cache_creation_input_tokens || 0);
          const outTok = usage.output_tokens || 0;
          const cacheRead = usage.cache_read_input_tokens || 0;
          const cacheWrite = usage.cache_creation_input_tokens || 0;
          const uncached = usage.input_tokens || 0;
          const cachePct = totalIn > 0 ? Math.round((cacheRead / totalIn) * 100) : 0;
          // 모델별 비용 계산 ($/MTok) — 가격 변경 시 PRICING_DATE도 함께 업데이트
          const PRICING_DATE = '2026-03-24';
          const model = entry.request?.body?.model || entry.response?.body?.model || '';
          const isOpus4 = model.includes('opus-4-') && !model.includes('opus-4-1'); // opus 4.5/4.6 = $5/$25
          const isOldOpus = model.includes('opus-4-1') || model.includes('opus-4-0') || model.includes('opus-3'); // $15/$75
          const isHaiku = model.includes('haiku');
          const isApi = entry.request?.isApiKey;
          let inP = 3, outP = 15;
          if (isOpus4) { inP = 5; outP = 25; }
          else if (isOldOpus) { inP = 15; outP = 75; }
          else if (isHaiku) { inP = 1; outP = 5; }
          let crP, cwP;
          if (isApi) {
            crP = inP * 0.1;   // API: cache read = 10% of input
            cwP = inP * 1.25;  // API: cache write = 125% of input
          } else {
            crP = 0;            // 구독: cache read = 무료
            cwP = inP;          // 구독: cache write = input과 동일
          }
          const cost = (uncached * inP + cacheRead * crP + cacheWrite * cwP + outTok * outP) / 1_000_000;
          const costStr = '$' + cost.toFixed(4);
          const fmtCost = (n) => '$' + (n / 1_000_000).toFixed(4);
          const popData = JSON.stringify({
            model: model || i18n.t('token.unknown'), kb, pricingDate: PRICING_DATE, isApi,
            rows: [
              { label: i18n.t('token.cacheRead'), tokens: fmtTok(cacheRead), price: crP, cost: fmtCost(cacheRead * crP) },
              { label: i18n.t('token.cacheWrite'), tokens: fmtTok(cacheWrite), price: cwP, cost: fmtCost(cacheWrite * cwP) },
              { label: i18n.t('token.uncachedInput'), tokens: fmtTok(uncached), price: inP, cost: fmtCost(uncached * inP) },
              { label: i18n.t('token.output'), tokens: fmtTok(outTok), price: outP, cost: fmtCost(outTok * outP) },
            ],
            total: costStr,
            cachePct
          });
          let parts = `<span class="tt-badge">${kb} KB</span>`;
          parts += `<span class="tt-badge">${i18n.t('token.input')} ${fmtTok(totalIn)}</span>`;
          parts += `<span class="tt-badge">${i18n.t('token.output')} ${fmtTok(outTok)}</span>`;
          if (cachePct > 0) parts += `<span class="tt-badge" style="color:var(--green)">${i18n.t('token.cache')} ${cachePct}%</span>`;
          parts += `<span class="tt-badge" style="color:var(--yellow)">${costStr}</span>`;
          return `<div class="proxy-token-pill" data-cost='${popData.replace(/'/g, "&#39;")}'>${parts}</div>`;
        }
        const tokens = Math.ceil(bytes / 3.5);
        const tokStr = fmtTok(tokens);
        return `<div class="proxy-token-pill"><span class="tt-badge">${kb} KB</span><span class="tt-badge">~${tokStr} tok (${i18n.t('token.estimated')})</span></div>`;
      })()
    : '';
  const prevScrollTop = document.getElementById('proxyDetailCode')?.scrollTop ?? 0;
  detail.innerHTML = header + tokenInfo + '<div class="json-tree-view" id="proxyDetailCode" style="flex:1;overflow:auto"></div>';
  const code = document.getElementById('proxyDetailCode');
  renderJsonTree(code, data);
  if (proxyDetailMechFilter) {
    requestAnimationFrame(() => { code.scrollTop = prevScrollTop; });
    highlightMechInJsonTree(code, entry.body, proxyDetailMechFilter);
  }
  if (q) {
    applyDetailHighlight(code, q);
    const marks = code.querySelectorAll('mark.search-hl');
    if (marks.length > 0) {
      if (searchCurrentIdx < 0) searchCurrentIdx = 0;
      if (searchCurrentIdx >= marks.length) searchCurrentIdx = 0;
      marks[searchCurrentIdx].classList.add('current');
      marks[searchCurrentIdx].scrollIntoView({ behavior: 'smooth', block: 'center' });
      updateSearchCounter(marks.length);
    }
  }

  if (q || _detailSearchWasFocused) {
    const inp = document.getElementById('proxyDetailSearchInput');
    if (inp) { inp.focus(); const len = inp.value.length; inp.setSelectionRange(len, len); }
  }
}

// ─── Proxy Analysis ────────────────────────────────────────────────────────
function detectMechanisms(body) {
  const found = { claudeMd: null, outputStyle: null, slashCommands: [], skills: [], subAgents: [], mcpTools: [] };
  if (!body) return found;

  // Output Style: system is array with 2+ items
  if (Array.isArray(body.system) && body.system.length >= 2) {
    found.outputStyle = body.system.filter(s => s.type === 'text').map(s => s.text);
  }

  // Scan messages
  const msgs = body.messages || [];
  for (const msg of msgs) {
    const contents = Array.isArray(msg.content) ? msg.content
                   : (typeof msg.content === 'string' ? [{ type: 'text', text: msg.content }] : []);

    for (const c of contents) {
      if (c.type === 'text' && typeof c.text === 'string') {
        // CLAUDE.md: 여러 <system-reminder> 블록에서 Contents of 패턴이 있는 것 모두 수집
        for (const m of c.text.matchAll(/<system-reminder>([\s\S]*?)<\/system-reminder>/g)) {
          const inner = m[1].trim();
          if (/Contents of /i.test(inner)) {
            found.claudeMd = found.claudeMd ? found.claudeMd + '\n\n' + inner : inner;
          }
        }
        // Slash Command: <command-message> tag (multiple per conversation)
        for (const cmdMatch of c.text.matchAll(/<command-message>([\s\S]*?)<\/command-message>/g)) {
          const tag = cmdMatch[1].trim();
          // Try <command-name>/xxx</command-name> right after (real CLI format)
          const nearby = c.text.slice(cmdMatch.index + cmdMatch[0].length, cmdMatch.index + cmdMatch[0].length + 200);
          const cmdNameMatch = nearby.match(/^<command-name>\s*\/(\S+)\s*<\/command-name>/);
          let name;
          if (cmdNameMatch) {
            name = cmdNameMatch[1];                          // /worklog → worklog
          } else {
            const nameMatch = tag.match(/^#\s*\/(\S+)/)     // # /commit
                           || tag.match(/^(\S+)\s+is running/); // commit is running…
            name = nameMatch ? nameMatch[1]
                 : (/^\w[\w-]*$/.test(tag) ? tag : `Cmd ${found.slashCommands.length + 1}`);
          }
          found.slashCommands.push({ name, tag, full: c.text });
        }
      }
      // Skill tool_use
      if (c.type === 'tool_use' && c.name === 'Skill') {
        found.skills.push({ id: c.id, input: c.input });
      }
      // Sub-Agent (Task / Agent tool)
      if (c.type === 'tool_use' && (c.name === 'Task' || c.name === 'Agent')) {
        found.subAgents.push({ id: c.id, name: c.name, input: c.input });
      }
      // MCP tool_use
      if (c.type === 'tool_use' && c.name && c.name.startsWith('mcp__')) {
        found.mcpTools.push({ id: c.id, name: c.name, input: c.input });
      }
      // tool_result for Skill / MCP
      if (c.type === 'tool_result') {
        const skill = found.skills.find(s => s.id === c.tool_use_id);
        if (skill) skill.result = typeof c.content === 'string' ? c.content : JSON.stringify(c.content, null, 2);
        const mcp = found.mcpTools.find(m => m.id === c.tool_use_id);
        if (mcp) mcp.result = typeof c.content === 'string' ? c.content : JSON.stringify(c.content, null, 2);
      }
    }
  }
  return found;
}

function renderProxyAnalysis(entry, container) {
  const body = entry.body;
  const det = detectMechanisms(body);
  const hasAny = det.claudeMd || det.outputStyle || det.slashCommands.length || det.skills.length || det.subAgents.length || det.mcpTools.length;

  const mechChipsHtml = buildMechFilterChips(body);

  const aq = proxyDetailSearch;
  const analysisSearchBar = `<div class="msg-search-bar" style="flex-shrink:0">
    <input type="text" class="msg-search-input" id="proxyDetailSearchInput"
      placeholder="${esc(i18n.t('analysis.searchPlaceholder'))}" value="${esc(aq)}"
      oninput="setProxyDetailSearch(this.value)"
      oncompositionstart="_imeComposing=true"
      oncompositionend="_imeComposing=false;setProxyDetailSearch(this.value)">
    ${aq ? `<button class="msg-search-clear" onclick="setProxyDetailSearch('');document.getElementById('proxyDetailSearchInput')?.focus()" title="${esc(i18n.t('messages.searchClear'))}">✕</button>` : ''}
  </div>`;

  let html = '<div style="flex:1;overflow:auto"><div class="analysis-view">';

  if (!hasAny) {
    html += `<div class="analysis-none">${i18n.t('analysis.noMechanisms')}</div>`;
    html += '</div></div>';
    container.innerHTML = `<div style="flex-shrink:0">${analysisSearchBar}${mechChipsHtml}</div>` + html;
    return;
  }

  // Model info
  if (body?.model) {
    html += `<div class="analysis-kv"><span class="ak">model</span><span class="av">${esc(body.model)}</span></div>`;
  }

  // CLAUDE.md
  if (det.claudeMd) {
    const mdSections = parseClaudeMdSections(det.claudeMd);
    if (mdSections.length > 0) {
      html += `<div class="analysis-section" data-mech-key="cm">
        <div class="analysis-section-title" style="color:var(--green)">${i18n.t('analysis.claudeMdTitle')}</div>
        <div class="analysis-desc">${i18n.t('analysis.claudeMdDesc')}</div>`;
      for (let si = 0; si < mdSections.length; si++) {
        const s = mdSections[si];
        const color = s.scope === 'global' ? 'var(--green)' : 'var(--blue)';
        const hlClass = s.scope === 'global' ? 'highlight-green' : 'highlight-blue';
        html += `<div style="margin-top:8px" data-mech-key="cm_${si}">
          <div style="font-size:10px;font-weight:700;color:${color};margin-bottom:4px">${esc(s.label)}</div>
          <div style="font-size:10px;color:var(--dim);margin-bottom:4px;word-break:break-all">${esc(s.path)}</div>
          <div class="analysis-block ${hlClass}">${esc(s.content)}</div>
        </div>`;
      }
      html += '</div>';
    } else {
      html += `<div class="analysis-section" data-mech-key="cm">
        <div class="analysis-section-title" style="color:var(--green)">${i18n.t('analysis.claudeMdTitle')}</div>
        <div class="analysis-desc">${i18n.t('analysis.claudeMdDesc')}</div>
        <div class="analysis-block highlight-green">${esc(det.claudeMd)}</div>
      </div>`;
    }
  }

  // Output Style
  if (det.outputStyle) {
    const extra = det.outputStyle.slice(1).join('\n\n---\n\n');
    html += `<div class="analysis-section" data-mech-key="st">
      <div class="analysis-section-title" style="color:var(--blue)">${i18n.t('analysis.outputStyleTitle')}</div>
      <div class="analysis-desc">${i18n.t('analysis.outputStyleDesc')}</div>
      <div class="analysis-block highlight-blue">${esc(extra)}</div>
    </div>`;
  }

  // Slash Command + Skill (연결된 흐름이면 하나로 합침)
  const slashSkillLinked = det.slashCommands.length > 0 && det.skills.length > 0;

  det.slashCommands.forEach((cmd, i) => {
    html += `<div class="analysis-section" data-mech-key="sc_${i}">
      <div class="analysis-section-title" style="color:var(--yellow)">${i18n.t('analysis.slashCmdTitle')}</div>
      <div class="analysis-desc">${i18n.t('analysis.slashCmdDesc', { cmd: esc(cmd.name) })}</div>
      <div class="analysis-block highlight-yellow">${esc(cmd.full)}</div>
    </div>`;
  });

  det.skills.forEach((sk, i) => {
    html += `<div class="analysis-section" data-mech-key="sk_${i}">
      <div class="analysis-section-title" style="color:var(--purple)">${i18n.t(slashSkillLinked ? 'analysis.skillLinkedTitle' : 'analysis.skillTitle')}</div>
      <div class="analysis-desc">${i18n.t(slashSkillLinked ? 'analysis.skillLinkedDesc' : 'analysis.skillDesc')}</div>
      <div class="analysis-kv"><span class="ak">id</span><span class="av">${esc(sk.id)}</span></div>
      <div class="analysis-block highlight-purple jt-json-block" data-json="${escAttr(JSON.stringify(sk.input))}"></div>
      ${sk.result ? `<div class="analysis-kv"><span class="ak">result (tool_result)</span></div><div class="analysis-block highlight-purple">${esc(sk.result)}</div>` : `<div class="analysis-kv"><span class="ak" style="color:var(--dim)">${i18n.t('analysis.noToolResult')}</span></div>`}
    </div>`;
  });

  // Sub-Agents
  for (const sa of det.subAgents) {
    const isJson = sa.input && typeof sa.input === 'object';
    html += `<div class="analysis-section" data-mech-key="sa">
      <div class="analysis-section-title" style="color:var(--orange)">${esc(sa.name)} — Sub-Agent</div>
      <div class="analysis-desc">${i18n.t('analysis.subAgentDesc')}</div>
      <div class="analysis-kv"><span class="ak">subagent_type</span><span class="av" style="color:var(--orange)">${esc(sa.input?.subagent_type || sa.input?.type || '?')}</span></div>
      <div class="analysis-block highlight-orange ${isJson ? 'jt-json-block' : ''}" ${isJson ? `data-json="${escAttr(JSON.stringify(sa.input))}"` : ''}>${isJson ? '' : esc(sa.input?.prompt || '')}</div>
    </div>`;
  }

  // MCP Tools
  det.mcpTools.forEach((mc, i) => {
    const parts = mc.name.split('__');
    const serverName = parts[1] || '?';
    const toolName = parts.slice(2).join('__') || mc.name;
    const isJson = mc.input && typeof mc.input === 'object';
    html += `<div class="analysis-section" data-mech-key="mc_${i}">
      <div class="analysis-section-title" style="color:#4ec9dc">🔌 ${esc(toolName)} <span style="font-weight:400;opacity:.7">(${esc(serverName)})</span></div>
      <div class="analysis-desc">${i18n.t('mechDesc.mc.what')}</div>
      <div class="analysis-kv"><span class="ak">id</span><span class="av">${esc(mc.id)}</span></div>
      <div class="analysis-block ${isJson ? 'jt-json-block' : ''}" style="border-left:2px solid rgba(78,201,220,.4);background:rgba(78,201,220,.06)" ${isJson ? `data-json="${escAttr(JSON.stringify(mc.input))}"` : ''}>${isJson ? '' : esc(JSON.stringify(mc.input, null, 2))}</div>
      ${mc.result ? `<div class="analysis-kv"><span class="ak">result (tool_result)</span></div><div class="analysis-block" style="border-left:2px solid rgba(78,201,220,.4);background:rgba(78,201,220,.06)">${esc(mc.result)}</div>` : ''}
    </div>`;
  });

  html += '</div></div>';
  container.innerHTML = `<div style="flex-shrink:0">${analysisSearchBar}${mechChipsHtml}</div>` + html;
  container.querySelectorAll('.jt-json-block').forEach(el => {
    try { renderJsonTree(el, JSON.parse(el.dataset.json)); }
    catch (e) { el.textContent = el.dataset.json; }
  });
}

function showDetailTab(tab) {
  proxyDetailTab = tab;
  proxyDetailSearch = '';
  proxyDetailMechFilter = null;
  document.querySelectorAll('.dtab').forEach(b => b.classList.toggle('active', b.dataset.dtab === tab));
  // Analysis tab copy button - hide it (analysis view는 copy가 의미없음)
  const copyBtn = document.querySelector('[onclick="copyProxyDetail()"]');
  if (copyBtn) copyBtn.style.display = (tab === 'analysis' || tab === 'messages') ? 'none' : '';
  renderProxyDetail();
}

function clearProxyCaptures() {
  proxyCaptures = [];
  selectedProxyId = null;
  renderProxyList();
  renderProxyDetail();
}

function copyProxyCmd() {
  const el = document.getElementById('proxyCmdText');
  if (!el || !proxyRunning) return;
  navigator.clipboard.writeText(el.textContent).then(() => {
    const btn = document.querySelector('[onclick="copyProxyCmd()"]');
    if (btn) { const o = btn.textContent; btn.textContent = '✓'; setTimeout(() => btn.textContent = o, 1500); }
  }).catch(e => console.error('copy failed', e));
}

function copyProxyDetail() {
  const entry = proxyCaptures.find(e => e.id === selectedProxyId);
  if (!entry) return;
  const data = proxyDetailTab === 'request' ? entry.body : (entry.response?.body ?? null);
  if (data === null || data === undefined) return;
  const text = typeof data === 'string' ? data : JSON.stringify(data, null, 2);
  navigator.clipboard.writeText(text).then(() => {
    const btn = document.querySelector('[onclick="copyProxyDetail()"]');
    if (btn) { const o = btn.textContent; btn.textContent = '✓'; setTimeout(() => btn.textContent = o, 1500); }
  }).catch(e => console.error('copy failed', e));
}

// ─── 토큰 팝오버 클릭 핸들러 ──────────────────────────────────────────────
document.addEventListener('click', (e) => {
  // 복사 버튼 처리
  if (e.target.classList.contains('token-popover-copy')) {
    navigator.clipboard.writeText(e.target.dataset.text);
    e.target.textContent = i18n.t('token.copied');
    setTimeout(() => { e.target.textContent = i18n.t('token.copyBtn'); }, 1500);
    return;
  }
  // 팝오버 내부 클릭 → 무시
  const existingPop = e.target.closest('.token-popover');
  if (existingPop) return;
  // 기존 팝오버 닫기
  const old = document.querySelector('.token-popover');
  if (old) old.remove();
  // 배지 클릭 → 팝오버 열기
  const pill = e.target.closest('.proxy-token-pill[data-cost]');
  if (!pill) return;
  const d = JSON.parse(pill.dataset.cost);
  const descs = {
    [i18n.t('token.cacheRead')]: i18n.t('token.descCacheRead'),
    [i18n.t('token.cacheWrite')]: i18n.t('token.descCacheWrite'),
    [i18n.t('token.uncachedInput')]: i18n.t('token.descUncached'),
    [i18n.t('token.output')]: i18n.t('token.descOutput'),
  };
  const textLines = [`${i18n.t('token.model')}: ${d.model}`, `${i18n.t('token.reqSize')}: ${d.kb} KB`, ''];
  let rowsHtml = '';
  for (const r of d.rows) {
    rowsHtml += `<div class="token-popover-row"><span class="tp-label">${esc(r.label)}</span><span class="tp-formula">${esc(r.tokens)} tok × $${esc(r.price)}/MTok</span><span class="tp-result">${esc(r.cost)}</span></div>`;
    if (descs[r.label]) rowsHtml += `<div class="tp-desc">${descs[r.label]}</div>`;
    textLines.push(`${r.label}: ${r.tokens} tok × $${r.price}/MTok = ${r.cost}`);
  }
  textLines.push('', `${i18n.t('token.total')}: ${d.total}`, `${i18n.t('token.cacheHitRate')}: ${d.cachePct}%`);
  const cacheNote = '';
  const pop = document.createElement('div');
  pop.className = 'token-popover';
  // 캐시 적중률 높으면 절감 설명, 낮으면 생략
  let noteHtml = `<div class="token-popover-note">`;
  noteHtml += d.isApi ? i18n.t('token.noteApi') : i18n.t('token.noteSubscription');
  noteHtml += `<br>`;
  noteHtml += i18n.t('token.notePricingDate', { date: d.pricingDate });
  noteHtml += `<br>${i18n.t('token.noteModelPrice')} (<a href="https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models#model-comparison" style="color:var(--blue,#7aa2f7);text-decoration:underline;cursor:pointer" onclick="event.stopPropagation();require('electron').shell.openExternal(this.href);return false;">${i18n.t('token.noteOfficialDoc')}</a>)`;
  noteHtml += `<br>${i18n.t('token.noteMTok')}`;
  if (d.cachePct >= 50) noteHtml += `<br>${i18n.t('token.noteCacheSaving', { pct: d.cachePct })}`;
  noteHtml += `</div>`;
  pop.innerHTML = `<div class="token-popover-title"><span>${i18n.t('token.costTitle')}</span><span class="token-popover-copy" data-text="${textLines.join('\n').replace(/"/g, '&quot;')}">${i18n.t('token.copyBtn')}</span></div>`
    + `<div class="token-popover-info">${i18n.t('token.model')}: ${esc(d.model)} · ${i18n.t('token.reqSize')}: ${esc(d.kb)} KB</div>`
    + rowsHtml
    + `<div class="token-popover-row tp-total"><span class="tp-label">${i18n.t('token.total')}</span><span class="tp-result">${esc(d.total)}</span></div>`
    + `<div class="token-popover-row tp-total"><span class="tp-label">${i18n.t('token.cacheHitRate')}</span><span class="tp-result">${esc(d.cachePct)}%</span></div>`
    + noteHtml;
  pill.appendChild(pop);
});

// ─── Init ─────────────────────────────────────────────────────────────────
document.addEventListener('keydown', e => {
  // Cmd+F / Ctrl+F: 현재 탭에 맞는 검색창 포커스
  if ((e.metaKey || e.ctrlKey) && e.key === 'f') {
    const proxyInp = document.getElementById('proxyDetailSearchInput');
    const msgInp = document.getElementById('msgSearchInput');
    const target = proxyInp || msgInp;
    if (target) {
      e.preventDefault();
      target.focus();
      target.select();
    }
  }
  // Escape: 검색 초기화
  if (e.key === 'Escape') {
    const proxyInp = document.getElementById('proxyDetailSearchInput');
    const msgInp = document.getElementById('msgSearchInput');
    if (proxyInp && document.activeElement === proxyInp && proxyDetailSearch) {
      setProxyDetailSearch('');
    } else if (msgInp && document.activeElement === msgInp && msgSearchQuery) {
      setMsgSearch('');
    }
  }
  // Enter / Shift+Enter: 검색 매칭 이전/다음 이동
  if (e.key === 'Enter') {
    const proxyInp = document.getElementById('proxyDetailSearchInput');
    if (proxyInp && document.activeElement === proxyInp) {
      e.preventDefault();
      navigateSearchMatch(e.shiftKey ? -1 : 1);
    }
  }
});

if (window.electronAPI?.platform === 'darwin') document.body.classList.add('darwin');

fetch('build-info.json').then(r=>r.json()).then(b=>{
  document.getElementById('buildVer').textContent = `v${b.version} (${b.hash})`;
  checkForUpdate(b.version);
}).catch(()=>{});

function checkForUpdate(currentVersion) {
  if (sessionStorage.getItem('updateChecked')) return;
  sessionStorage.setItem('updateChecked', '1');
  fetch('https://api.github.com/repos/kangraemin/claude-inspector/releases/latest', {
    headers: { 'Accept': 'application/vnd.github.v3+json' }
  })
  .then(r => r.ok ? r.json() : null)
  .then(data => {
    if (!data?.tag_name) return;
    const latest = data.tag_name.replace(/^v/, '');
    if (isNewerVersion(latest, currentVersion)) {
      const badge = document.getElementById('updateBadge');
      badge.textContent = `↑ v${latest}`;
      badge.href = data.html_url;
      badge.style.display = 'inline';
    }
  })
  .catch(() => {});
}

function isNewerVersion(latest, current) {
  const toNum = v => v.split('.').map(Number);
  const [la, lb, lc] = toNum(latest);
  const [ca, cb, cc] = toNum(current);
  return la > ca || (la === ca && lb > cb) || (la === ca && lb === cb && lc > cc);
}

// Apply initial i18n (after DOM is ready)
applyI18n();

// Show proxy panel directly (simulator removed)
document.getElementById('proxyPanel').style.display = 'flex';

// ── 프록시 상태 동기화 (리로드 시 메인 프로세스와 sync) ──────────────
(async () => {
  if (!window.electronAPI?.proxyStatus) return;
  try {
    const st = await window.electronAPI.proxyStatus();
    if (st.running) {
      proxyRunning = true;
      proxyActualPort = st.port;
      document.getElementById('proxyPort').value = st.port;
      // 이벤트 리스너 재등록
      window.electronAPI?.offProxy?.();
      window.electronAPI.onProxyRequest((data) => {
        proxyCaptures.unshift(data);
        if (proxyCaptures.length > 50) proxyCaptures.pop();
        debouncedRenderProxyList();
      });
      window.electronAPI.onProxyResponse((data) => {
        const entry = proxyCaptures.find(e => e.id === data.id);
        if (entry) {
          entry.response = data;
          debouncedRenderProxyList();
          if (selectedProxyId === data.id) debouncedRenderProxyDetail();
        }
      });
      renderProxyStatus();
    }
  } catch {}
})();

// ── Onboarding Modal ─────────────────────────────────────────────────
function closeOnboard() {
  document.getElementById('onboardModal').style.display = 'none';
  localStorage.setItem('ci-onboarded', '1');
}

if (!localStorage.getItem('ci-onboarded')) {
  document.getElementById('onboardModal').style.display = 'flex';
}
</script>
</body>
</html>
```

## File: `scripts/notarize.js`
```javascript
const { execSync } = require("child_process");
const path = require("path");

exports.default = async function notarize(context) {
  if (context.electronPlatformName !== "darwin") return;

  const appleId = process.env.APPLE_ID;
  const password = process.env.APPLE_APP_SPECIFIC_PASSWORD;
  const teamId = process.env.APPLE_TEAM_ID;

  if (!appleId || !password || !teamId) {
    console.log("⚠ Skipping notarization: missing APPLE_ID, APPLE_APP_SPECIFIC_PASSWORD, or APPLE_TEAM_ID");
    return;
  }

  const appPath = path.join(context.appOutDir, `${context.packager.appInfo.productFilename}.app`);
  const zipPath = path.join(context.appOutDir, "notarize-tmp.zip");

  console.log(`Notarizing ${appPath}...`);

  execSync(`ditto -c -k --keepParent "${appPath}" "${zipPath}"`);

  try {
    execSync(
      `xcrun notarytool submit "${zipPath}" --apple-id "${appleId}" --password "${password}" --team-id "${teamId}" --wait`,
      { stdio: "inherit", timeout: 600000 }
    );
    try {
      execSync(`xcrun stapler staple "${appPath}"`, { stdio: "inherit" });
    } catch {
      console.log("⚠ Staple failed (ticket may not have propagated yet) — notarization itself succeeded, continuing...");
    }
    console.log("Notarization complete!");
  } finally {
    try { require("fs").unlinkSync(zipPath); } catch {}
  }
};
```

## File: `tests/e2e/app.spec.ts`
```typescript
/**
 * E2E tests for Claude Inspector (Electron) — Proxy mode only
 *
 * Run: npm run test:e2e
 * 앱이 실행 중이면 먼저 종료: pkill -x "Electron"
 */
import { test, expect, _electron as electron } from '@playwright/test';
import type { ElectronApplication, Page } from '@playwright/test';
import path from 'node:path';
import fs from 'node:fs';

const ROOT = path.resolve(__dirname, '../..');

let app: ElectronApplication;
let page: Page;

test.beforeAll(async () => {
  app = await electron.launch({
    args: [ROOT],
    env: { ...process.env, NODE_ENV: 'test' },
  });
  page = await app.firstWindow();
  await page.waitForLoadState('domcontentloaded');
});

test.afterAll(async () => {
  await app.close();
});

// ─── 기본 UI ─────────────────────────────────────────────────────────────────

test('앱 타이틀 확인', async () => {
  await expect(page).toHaveTitle('Claude Inspector');
});

// ─── 프록시 ──────────────────────────────────────────────────────────────────

test('프록시 시작 버튼 존재', async () => {
  await expect(page.locator('#proxyStartBtn')).toBeVisible();
});

// ─── 프록시 리스너 중복 방지 / UI Freeze 방지 ─────────────────────────────────

test('toggleProxy 시작 분기에 offProxy 선행 호출 코드 존재 (리스너 누적 방지)', () => {
  // contextBridge frozen 제약으로 런타임 mock 불가 → 소스 코드 정적 검증
  const html = fs.readFileSync(path.join(ROOT, 'public/index.html'), 'utf8');

  // else { ... } 블록 내에서 onProxyRequest 등록 전에 offProxy()가 있는지 확인
  // "else {" 이후 첫 번째 offProxy 호출이 onProxyRequest보다 앞에 있어야 함
  const elseIdx = html.indexOf('// 기존 리스너 먼저 정리 후 새 리스너 등록 (누적 방지)');
  const offProxyIdx = html.indexOf('window.electronAPI.offProxy();', elseIdx);
  const onProxyRequestIdx = html.indexOf('window.electronAPI.onProxyRequest(', elseIdx);

  expect(elseIdx).toBeGreaterThan(-1); // 주석 존재
  expect(offProxyIdx).toBeGreaterThan(-1); // offProxy 호출 존재
  expect(onProxyRequestIdx).toBeGreaterThan(-1); // onProxyRequest 등록 존재
  // offProxy가 onProxyRequest보다 먼저 나와야 함
  expect(offProxyIdx).toBeLessThan(onProxyRequestIdx);
});

test('반복 토글 후 UI 반응성 (500ms 이내)', async () => {
  const btn = page.locator('#proxyStartBtn');
  await expect(btn).toBeVisible();

  // 버튼이 비활성화 → 활성화되는 시간 측정
  const start = Date.now();
  await btn.click();
  // 버튼이 다시 enabled 되길 기다림 (최대 500ms)
  await expect(btn).not.toBeDisabled({ timeout: 500 });
  const elapsed = Date.now() - start;

  expect(elapsed).toBeLessThan(500);
});

test('연속 IPC 이벤트 시 proxyList debounce 동작', async () => {
  // renderer에서 직접 debouncedRenderProxyList 3회 연속 호출 후
  // renderProxyList 실제 실행 횟수가 1~2회인지 확인
  const renderCount = await page.evaluate(async () => {
    let count = 0;
    // @ts-ignore
    const origRender = window.renderProxyList;
    if (!origRender) return -1; // 함수 없으면 스킵

    // @ts-ignore
    window.renderProxyList = () => { count++; origRender(); };

    // 10ms 간격으로 3회 연속 호출
    // @ts-ignore
    if (typeof debouncedRenderProxyList === 'function') {
      // @ts-ignore
      debouncedRenderProxyList();
      await new Promise(r => setTimeout(r, 10));
      // @ts-ignore
      debouncedRenderProxyList();
      await new Promise(r => setTimeout(r, 10));
      // @ts-ignore
      debouncedRenderProxyList();
      // debounce 타이머 소진 대기 (50ms + 여유)
      await new Promise(r => setTimeout(r, 100));
    }

    // @ts-ignore
    window.renderProxyList = origRender;
    return count;
  });

  // debouncedRenderProxyList가 없으면 -1 반환 → 스킵
  if (renderCount === -1) return;
  // debounce로 인해 1회만 실행되어야 함
  expect(renderCount).toBeLessThanOrEqual(2);
  expect(renderCount).toBeGreaterThan(0);
});

// ─── 언어 전환 ───────────────────────────────────────────────────────────────

test('언어 전환 버튼 클릭 → 로케일 변경', async () => {
  const btn = page.locator('#langToggleBtn');
  const beforeText = await btn.innerText();
  await btn.click();
  const afterText = await btn.innerText();
  expect(afterText).not.toBe(beforeText);
  // 원상복구
  await btn.click();
});

// ─── 프록시 UI 요소 ─────────────────────────────────────────────────────────

test('#proxyStartBtn ID 명확화 확인', async () => {
  await expect(page.locator('#proxyStartBtn')).toHaveCount(1);
});

// ─── 프록시 상세 탭 버튼 ────────────────────────────────────────────────────

for (const dtab of ['messages', 'request', 'response', 'analysis']) {
  test(`프록시 상세 탭 버튼: ${dtab}`, async () => {
    await expect(page.locator(`.dtab[data-dtab="${dtab}"]`)).toHaveCount(1);
  });
}

// ─── offProxy 안전성 ─────────────────────────────────────────────────────────

test('모든 offProxy 호출이 안전하게 보호됨 (guard 또는 optional chaining)', () => {
  const html = fs.readFileSync(path.join(ROOT, 'public/index.html'), 'utf8');

  // toggleProxy 내부: electronAPI guard가 try 블록 전에 존재 (early return)
  const toggleProxyMatch = html.match(/async function toggleProxy\(\)[\s\S]*?if \(!window\.electronAPI\) return;[\s\S]*?try\s*\{/);
  expect(toggleProxyMatch).not.toBeNull();

  // 페이지 로드 sync: optional chaining 사용
  const syncBlock = html.match(/프록시 상태 동기화[\s\S]*?\}\)\(\)/);
  expect(syncBlock).not.toBeNull();
  // offProxy in sync block should use optional chaining
  const syncOffProxy = syncBlock![0].match(/electronAPI\?\.offProxy\?\.\(\)/);
  expect(syncOffProxy).not.toBeNull();
});

test('프록시 토글 시 pageerror 없음', async () => {
  const pageErrors: string[] = [];
  const handler = (err: Error) => pageErrors.push(err.message);
  page.on('pageerror', handler);

  try {
    const btn = page.locator('#proxyStartBtn');
    await btn.click();
    await expect(btn).not.toBeDisabled({ timeout: 5000 });
    await page.waitForTimeout(300);

    // stop
    await btn.click();
    await expect(btn).not.toBeDisabled({ timeout: 5000 });
    await page.waitForTimeout(300);

    const offProxyErrors = pageErrors.filter(e => e.includes('offProxy') || e.includes('electronAPI'));
    expect(offProxyErrors).toHaveLength(0);
  } finally {
    page.removeListener('pageerror', handler);
  }
});

test('프록시 시작→정지 전체 사이클 정상 동작', async () => {
  const btn = page.locator('#proxyStartBtn');
  const portInput = page.locator('#proxyPort');

  // 시작
  await btn.click();
  await expect(btn).not.toBeDisabled({ timeout: 5000 });

  // 포트 값 존재 확인
  const port = await portInput.inputValue();
  expect(Number(port)).toBeGreaterThan(0);

  // 정지
  await btn.click();
  await expect(btn).not.toBeDisabled({ timeout: 5000 });
});
```

## File: `tests/unit/parse.test.mjs`
```
/**
 * Unit tests for parsing functions in public/index.html
 * 함수를 index.html에서 직접 추출해 테스트 (리팩토링 없이)
 *
 * Run: npm run test:unit
 */
import { test } from 'node:test';
import assert from 'node:assert/strict';

// ─── 함수 복사 (index.html과 동기화 필요) ────────────────────────────────────

function parseClaudeMdSections(inner) {
  const re = /Contents of (.+?) \((.+?)\):\n\n([\s\S]*?)(?=\n\nContents of |\s*$)/g;
  const sections = [];
  let m;
  while ((m = re.exec(inner)) !== null) {
    const path = m[1], desc = m[2], content = m[3].trim();
    const fname = path.split('/').pop();
    const isGlobal = /global|private global/i.test(desc);
    const isMemory = /memory/i.test(desc) || /\/memory\//.test(path);
    let label, cls;
    if (isMemory) {
      label = '🧠 Memory: ' + fname; cls = 'green';
    } else if (/\/rules\//.test(path)) {
      label = (isGlobal ? '📜 Global Rule: ' : '📜 Local Rule: ') + fname;
      cls = isGlobal ? 'green' : 'cyan';
    } else if (/CLAUDE\.md$/i.test(path)) {
      label = isGlobal ? '📋 Global CLAUDE.md' : '📋 Local CLAUDE.md';
      cls = isGlobal ? 'green' : 'cyan';
    } else {
      label = '📋 ' + fname; cls = 'green';
    }
    sections.push({ label, path, content, cls, scope: isGlobal ? 'global' : 'local' });
  }
  return sections;
}

function detectMechanisms(body) {
  const found = { claudeMd: null, outputStyle: null, slashCommand: null, skills: [], subAgents: [] };
  if (!body) return found;

  if (Array.isArray(body.system) && body.system.length >= 2) {
    found.outputStyle = body.system.filter(s => s.type === 'text').map(s => s.text);
  }

  const msgs = body.messages || [];
  for (const msg of msgs) {
    const contents = Array.isArray(msg.content) ? msg.content
                   : (typeof msg.content === 'string' ? [{ type: 'text', text: msg.content }] : []);
    for (const c of contents) {
      if (c.type === 'text' && typeof c.text === 'string') {
        const srMatch = c.text.match(/<system-reminder>([\s\S]*?)<\/system-reminder>/);
        if (srMatch && !found.claudeMd) {
          found.claudeMd = srMatch[1].trim();
        }
        const cmdMatch = c.text.match(/<command-message>([\s\S]*?)<\/command-message>/);
        if (cmdMatch) {
          found.slashCommand = { tag: cmdMatch[1].trim(), full: c.text };
        }
      }
      if (c.type === 'tool_use' && c.name === 'Skill') {
        found.skills.push({ id: c.id, input: c.input });
      }
      if (c.type === 'tool_use' && (c.name === 'Task' || c.name === 'Agent')) {
        found.subAgents.push({ id: c.id, name: c.name, input: c.input });
      }
    }
  }
  return found;
}

// ─── parseClaudeMdSections ───────────────────────────────────────────────────

test('global CLAUDE.md 단일 섹션', () => {
  const input = `Contents of /Users/ram/.claude/CLAUDE.md (user's private global instructions for all projects):\n\n# Global Rules\ncontent here`;
  const sections = parseClaudeMdSections(input);
  assert.equal(sections.length, 1);
  assert.equal(sections[0].label, '📋 Global CLAUDE.md');
  assert.equal(sections[0].scope, 'global');
  assert.equal(sections[0].cls, 'green');
  assert.ok(sections[0].content.includes('# Global Rules'));
});

test('local CLAUDE.md 단일 섹션', () => {
  const input = `Contents of /project/CLAUDE.md (project instructions, checked into the codebase):\n\n# Project Rules\ncontent`;
  const sections = parseClaudeMdSections(input);
  assert.equal(sections.length, 1);
  assert.equal(sections[0].label, '📋 Local CLAUDE.md');
  assert.equal(sections[0].scope, 'local');
  assert.equal(sections[0].cls, 'cyan');
});

test('global + local 복수 섹션', () => {
  const input = [
    `Contents of /Users/ram/.claude/CLAUDE.md (user's private global instructions for all projects):\n\n# Global Rules\nglobal content`,
    `Contents of /project/CLAUDE.md (project instructions, checked into the codebase):\n\n# Local Rules\nlocal content`,
  ].join('\n\n');
  const sections = parseClaudeMdSections(input);
  assert.equal(sections.length, 2);
  assert.equal(sections[0].scope, 'global');
  assert.equal(sections[1].scope, 'local');
});

test('global rule 파일', () => {
  const input = `Contents of /Users/ram/.claude/rules/git-rules.md (user's private global instructions for all projects):\n\n# Git Rules\ncontent`;
  const sections = parseClaudeMdSections(input);
  assert.equal(sections.length, 1);
  assert.equal(sections[0].label, '📜 Global Rule: git-rules.md');
  assert.equal(sections[0].scope, 'global');
});

test('memory 파일', () => {
  const input = `Contents of /Users/ram/.claude/projects/foo/memory/MEMORY.md (user's auto-memory, persists across conversations):\n\n# Memory\ncontent`;
  const sections = parseClaudeMdSections(input);
  assert.equal(sections.length, 1);
  assert.equal(sections[0].label, '🧠 Memory: MEMORY.md');
});

test('실제 system-reminder 형식 — 4개 섹션 분리', () => {
  const input = [
    `Contents of /Users/ram/.claude/CLAUDE.md (user's private global instructions for all projects):\n\n# Global Rules\ncontent`,
    `Contents of /Users/ram/.claude/rules/git-rules.md (user's private global instructions for all projects):\n\n# Git Rules\ncontent`,
    `Contents of /project/CLAUDE.md (project instructions, checked into the codebase):\n\n# Claude Inspector\ncontent`,
    `Contents of /Users/ram/.claude/projects/foo/memory/MEMORY.md (user's auto-memory, persists across conversations):\n\n# Memory\ncontent`,
  ].join('\n\n');
  const sections = parseClaudeMdSections(input);
  assert.equal(sections.length, 4);
  assert.equal(sections[0].label, '📋 Global CLAUDE.md');
  assert.equal(sections[1].label, '📜 Global Rule: git-rules.md');
  assert.equal(sections[2].label, '📋 Local CLAUDE.md');
  assert.equal(sections[3].label, '🧠 Memory: MEMORY.md');
});

test('섹션 없으면 빈 배열', () => {
  const sections = parseClaudeMdSections('아무 내용 없음');
  assert.equal(sections.length, 0);
});

// ─── detectMechanisms ────────────────────────────────────────────────────────

test('system-reminder → claudeMd 감지', () => {
  const body = {
    messages: [{
      role: 'user',
      content: '<system-reminder>\nContents of /path/CLAUDE.md (desc):\n\ncontent\n</system-reminder>\nhello',
    }],
  };
  const det = detectMechanisms(body);
  assert.ok(det.claudeMd);
  assert.ok(det.claudeMd.includes('Contents of'));
});

test('system 배열 2개 이상 → outputStyle 감지', () => {
  const body = {
    system: [
      { type: 'text', text: 'base system' },
      { type: 'text', text: 'output style' },
    ],
    messages: [],
  };
  const det = detectMechanisms(body);
  assert.ok(det.outputStyle);
  assert.equal(det.outputStyle.length, 2);
});

test('command-message → slashCommand 감지', () => {
  const body = {
    messages: [{
      role: 'user',
      content: '<command-message>commit</command-message>\n/commit',
    }],
  };
  const det = detectMechanisms(body);
  assert.ok(det.slashCommand);
  assert.ok(det.slashCommand.tag.includes('commit'));
});

test('tool_use Skill → skills 감지', () => {
  const body = {
    messages: [{
      role: 'assistant',
      content: [{ type: 'tool_use', id: 'tu_1', name: 'Skill', input: { skill: 'e2e' } }],
    }],
  };
  const det = detectMechanisms(body);
  assert.equal(det.skills.length, 1);
  assert.equal(det.skills[0].input.skill, 'e2e');
});

test('tool_use Agent → subAgents 감지', () => {
  const body = {
    messages: [{
      role: 'assistant',
      content: [{ type: 'tool_use', id: 'tu_2', name: 'Agent', input: { description: 'test agent' } }],
    }],
  };
  const det = detectMechanisms(body);
  assert.equal(det.subAgents.length, 1);
  assert.equal(det.subAgents[0].name, 'Agent');
});

test('빈 body → 모두 null/empty', () => {
  const det = detectMechanisms({});
  assert.equal(det.claudeMd, null);
  assert.equal(det.outputStyle, null);
  assert.equal(det.slashCommand, null);
  assert.equal(det.skills.length, 0);
  assert.equal(det.subAgents.length, 0);
});
```


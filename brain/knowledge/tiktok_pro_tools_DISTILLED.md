---
id: Tiktok-Pro-Tools
type: knowledge
owner: OA_Triage
---
# Tiktok-Pro-Tools
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# 🎵 TikTok Pro Tools - Chrome Extension

[![Download Extension](https://img.shields.io/badge/Download_Extension-Download_ZIP-success?style=for-the-badge&logo=googlechrome)](https://github.com/diepvantien/Tiktok-Pro-Tools/archive/refs/heads/main.zip)

A powerful Chrome extension that completely transforms your TikTok web experience with essential tools for audio formatting, video playback, auto-scrolling, and intelligent UI customization.

---

## ✨ Features

- ⏯ **Background Play**: Keep TikTok videos playing even when you switch to another tab or minimize the browser.
- ⏸ **Smart Auto-Pause**: Automatically pause TikTok when another tab starts playing media, and resume when it stops.
- 📺 **Auto PiP (Picture-in-Picture)**: Automatically pops the video out into a mini-player when you switch tabs so you never miss a moment.
- 🎛️ **Advanced Audio Equalizer (EQ)**: Customize your sound with presets like Bass Boost, Treble Boost, Vocal Boost. Includes an immersive **360° Audio (8D)** mode!
- 🔊 **Volume Normalizer**: Automatically balance loud and quiet videos so you don't get jump-scared by sudden volume spikes.
- ⚡ **Video Speed Controller**: Fine-tune playback speed from 0x to 4x.
- 🧹 **Clean Mode & UI Tools**: Enhance your viewing experience by hiding text overlays, descriptions, and UI elements.
- 🛒 **Unlock Regional Shop Videos**: Watch restricted or localized TikTok Shop videos that are normally blocked in your region.
- 🚫 **Auto Skip & Hide by Keywords**: Automatically skip videos and blur comments that contain specific keywords you define.
- 📥 **Media Downloader**: Easily download TikTok videos (without watermarks) and MP3 audio directly using the provided URL box.

---

## 🚀 Installation Guide

### Step 1: Download the Extension
Click the green **Download Extension** button above to download the `.zip` file, then extract it to a folder on your computer.

### Step 2: Open Chrome Extensions
Open Google Chrome and navigate to `chrome://extensions/`.

### Step 3: Enable Developer Mode
Toggle the **"Developer mode"** switch located in the top right corner of the page.

### Step 4: Load the Extension
Click **"Load unpacked"** and select the folder you extracted in Step 1.

### Step 5: Start Using!
Go to [TikTok.com](https://tiktok.com). Click on the extension icon in your toolbar to open the control panel, adjust the settings to your liking, and enjoy!

*(Note: If features don't apply immediately, please press F5 to refresh your TikTok tab).*

---

## ☕ Author & Support

Developed with ❤️ by **Diep Van Tien**. 

If this extension saves your life and improves your workflow every day, please consider supporting me! This helps me maintain the project and add more incredible features. 

[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/tixuno)
[![Donate Momo](https://img.shields.io/badge/Donate-Momo-AE2070?style=for-the-badge&logo=appveyor&logoColor=white)](https://me.momo.vn/OeIGiJsViJfDfntmiRId)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/diepvantien)

**Email:** dieptien290620@gmail.com

---

## 📝 Disclaimer

- **Privacy First**: This extension operates entirely on your device and does not collect, track, or share any personal user data.
- **Cross-Origin Audio**: EQ and 360 Audio modifications are securely injected and only active when you interact with the page.

---

## 📜 License

This project is licensed under a **Custom MIT License**. 
- **Personal Use:** Free and unrestricted.
- **Commercial Use:** Requires a paid commercial license. Please contact the author for details.

See the [LICENSE](LICENSE) file for more information.

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=diepvantien/Tiktok-Pro-Tools&type=Date)](https://star-history.com/#diepvantien/Tiktok-Pro-Tools&Date)

---

*Made with ❤️ for TikTok power users by Diep Van Tien*

```

### File: background.js
```js
// TikTok Pro Tools - Background v12

// ─── TikWM Download API (proxy to avoid CORS) ────────────────────────────────
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === 'TIKWM_FETCH') {
    fetchTikwm(msg.url)
      .then(data => sendResponse({ ok: true, data }))
      .catch(err => sendResponse({ ok: false, error: err.message }));
    return true; // async
  }
  if (msg.type === 'DOWNLOAD_FILE') {
    chrome.downloads.download({
      url: msg.url,
      filename: msg.filename || 'tiktok-download',
      saveAs: false
    });
    sendResponse({ ok: true });
    return true;
  }
});

async function fetchTikwm(tiktokUrl) {
  const body = new URLSearchParams({ url: tiktokUrl, hd: '1' });
  const res = await fetch('https://tikwm.com/api/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: body.toString()
  });
  if (!res.ok) throw new Error('HTTP ' + res.status);
  const json = await res.json();
  if (json.code !== 0) throw new Error(json.msg || 'API error');
  return json.data;
}


// Keep SW alive and emit autoScroll pings
chrome.alarms.create('keepAlive', { periodInMinutes: 0.4 });
chrome.alarms.create('autoScroll', { periodInMinutes: 0.05 }); // ~3 giây

chrome.alarms.onAlarm.addListener((alarm) => {
    if (alarm.name === 'autoScroll') {
        chrome.tabs.query({ url: '*://*.tiktok.com/*' }, (tabs) => {
            tabs.forEach(tab => {
                chrome.tabs.sendMessage(tab.id, { action: 'scroll' }).catch(() => {});
            });
        });
    }
});


// Auto pause TikTok when other tabs are audible
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.audible !== undefined) {
        checkAudibleTabs();
    }
});

chrome.tabs.onRemoved.addListener((tabId, removeInfo) => {
    checkAudibleTabs();
});

async function checkAudibleTabs() {
    const tabs = await chrome.tabs.query({ audible: true });
    // Có tab nào đag phát nhạc mà KHÔNG PHẢI TIKTOK hay không?
    const otherAudible = tabs.some(t => !(t.url || '').includes('.tiktok.com'));
    
    const { _lastAudibleState } = await chrome.storage.session.get({_lastAudibleState: false});
    
    if (otherAudible && !_lastAudibleState) {
        await chrome.storage.session.set({_lastAudibleState: true});
        notifyTikTokTabs('other_audio_start');
    } else if (!otherAudible && _lastAudibleState) {
        await chrome.storage.session.set({_lastAudibleState: false});
        notifyTikTokTabs('other_audio_stop');
    }
}

function notifyTikTokTabs(action) {
    chrome.tabs.query({ url: '*://*.tiktok.com/*' }, (tabs) => {
        tabs.forEach(tab => {
            chrome.tabs.sendMessage(tab.id, { action }).catch(() => {});
        });
    });
}

```

### File: content.css
```css
/* TikTok Pro Tools - v11 */
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap');

:root {
  --tpt-bg: rgba(255,255,255,0.95);
  --tpt-bd: rgba(0,0,0,0.1);
  --tpt-tx: #333;
  --tpt-hdr-bg: rgba(0,0,0,0.03);
  --tpt-logo: #333;
  --tpt-sec-bd: rgba(0,0,0,0.05);
  --tpt-sub: #666;
  --tpt-sw-bg: #e4e6eb;
  --tpt-sw-k: #fff;
  --tpt-sw-br: rgba(0,0,0,0.1);
  --tpt-ps-bg: #f0f2f5;
  --tpt-ps-tx: #555;
  --tpt-ps-bd: rgba(0,0,0,0.05);
  --tpt-btn-bg: #f0f2f5;
  --tpt-btn-tx: #333;
  --tpt-btn-bd: rgba(0,0,0,0.1);
  --tpt-input-bg: #fff;
  --tpt-input-tx: #333;
}

@media (prefers-color-scheme: dark) {
  :root {
    --tpt-bg: rgba(8,8,12,0.97);
    --tpt-bd: rgba(255,255,255,0.09);
    --tpt-tx: #ccc;
    --tpt-hdr-bg: transparent;
    --tpt-logo: #fff;
    --tpt-sec-bd: rgba(255,255,255,0.048);
    --tpt-sub: #aaa;
    --tpt-sw-bg: #1e1e1e;
    --tpt-sw-k: #484848;
    --tpt-sw-br: rgba(255,255,255,.06);
    --tpt-ps-bg: rgba(255,255,255,.04);
    --tpt-ps-tx: #888;
    --tpt-ps-bd: rgba(255,255,255,.07);
    --tpt-btn-bg: rgba(255,255,255,.05);
    --tpt-btn-tx: #ccc;
    --tpt-btn-bd: rgba(255,255,255,.1);
    --tpt-input-bg: rgba(255,255,255,.05);
    --tpt-input-tx: #ccc;
  }
}

#tpt-panel {
  position: fixed; top: 80px; right: 14px; z-index: 2147483647; width: 300px;
  background: var(--tpt-bg); border: 1px solid var(--tpt-bd);
  border-radius: 16px; backdrop-filter: blur(28px) saturate(170%);
  -webkit-backdrop-filter: blur(28px) saturate(170%);
  box-shadow: 0 24px 64px rgba(0,0,0,.15), 0 4px 12px rgba(0,0,0,.08);
  font-family: 'DM Sans', -apple-system, sans-serif; font-size: 12.5px; color: var(--tpt-tx); user-select: none;
}
@media (prefers-color-scheme: dark) {
  #tpt-panel { box-shadow: 0 24px 64px rgba(0,0,0,.72), 0 4px 12px rgba(0,0,0,.4), inset 0 1px 0 rgba(255,255,255,0.07); }
}

/* Header */
.tpt-hdr { display:flex; align-items:center; justify-content:space-between; padding:10px 13px 9px; border-bottom:1px solid var(--tpt-bd); cursor:grab; border-radius:16px 16px 0 0; background: var(--tpt-hdr-bg); }
.tpt-hdr:active { cursor:grabbing; }
.tpt-logo { display:flex; align-items:center; gap:7px; font-size:13px; font-weight:700; color:var(--tpt-logo); letter-spacing:-.2px; }
#tpt-min { background:var(--tpt-btn-bg); border:1px solid var(--tpt-btn-bd); border-radius:6px; color:var(--tpt-tx); width:24px; height:20px; display:flex; align-items:center; justify-content:center; font-size:12px; cursor:pointer; transition:background .15s,color .15s; }
#tpt-min:hover { background:rgba(128,128,128,0.2); }

/* Body */
#tpt-body { padding:1px 0 5px; }
.tpt-sec { padding:9px 13px; border-bottom:1px solid var(--tpt-sec-bd); }
.tpt-row { display:flex; align-items:center; justify-content:space-between; margin-bottom:2px; }
.tpt-row-hdr { display:flex; align-items:center; justify-content:space-between; margin-bottom:10px; }
.tpt-lbl { display:flex; align-items:center; gap:6px; font-weight:500; color:var(--tpt-tx); }
.tpt-lbl>span:first-child { font-size:12px; }
.tpt-sub { font-size:10px; color:var(--tpt-sub); margin-top:2px; line-height:1.4; }

/* Toggle */
.tpt-sw { cursor:pointer; }
.tpt-sw input { display:none; }
.sw-t { display:block; width:36px; height:20px; background:var(--tpt-sw-bg); border-radius:20px; position:relative; transition:background .2s; border:1px solid var(--tpt-sw-br); }
.sw-k { position:absolute; top:2px; left:3px; width:14px; height:14px; background:var(--tpt-sw-k); border-radius:50%; transition:transform .2s,background .2s; box-shadow: 0 1px 2px rgba(0,0,0,0.2); }
.tpt-sw input:checked + .sw-t { background:rgba(254,44,85,.75); border-color:transparent; }
.tpt-sw input:checked + .sw-t .sw-k { transform:translateX(16px); background:#fff; }

/* Sliders */
.tpt-bigval { font-size:22px; font-weight:700; letter-spacing:-1px; line-height:1; }
.tpt-red  { color:#fe2c55; text-shadow:0 0 18px rgba(254,44,85,.25); }
@media (prefers-color-scheme: dark) { .tpt-red { text-shadow:0 0 18px rgba(254,44,85,.45); } }
.tpt-cyan { color:#25f4ee; text-shadow:0 0 14px rgba(37,244,238,.35); }
.tpt-slwrap { margin-bottom:10px; }
.tpt-slider {
  -webkit-appearance:none; width:100%; height:6px; border-radius:6px; outline:none; cursor:pointer;
  background:linear-gradient(to right, var(--clr) 0%, var(--clr) var(--fill,0%), rgba(128,128,128,.2) var(--fill,0%), rgba(128,128,128,.2) 100%);
}
.tpt-slider::-webkit-slider-thumb { -webkit-appearance:none; width:20px; height:20px; border-radius:50%; background:#fff; box-shadow:0 0 0 3px var(--clr),0 2px 8px rgba(0,0,0,.35); cursor:grab; transition:transform .1s; }
@media (prefers-color-scheme: dark) { .tpt-slider::-webkit-slider-thumb { box-shadow:0 0 0 3px var(--clr),0 2px 8px rgba(0,0,0,.55); } }
.tpt-slider::-webkit-slider-thumb:active { cursor:grabbing; transform:scale(1.22); }
.tpt-slider::-webkit-slider-thumb:hover  { transform:scale(1.1); }
.tpt-ps-row { display:flex; gap:4px; }
.tpt-ps { flex:1; background:var(--tpt-ps-bg); border:1px solid var(--tpt-ps-bd); border-radius:6px; color:var(--tpt-ps-tx); font-size:10.5px; font-weight:600; padding:5px 0; cursor:pointer; font-family:inherit; transition:all .12s; }
.tpt-ps:hover { background:rgba(254,44,85,.11); border-color:rgba(254,44,85,.28); color:#fe2c55; }
.tpt-ps.on    { background:rgba(254,44,85,.18); border-color:rgba(254,44,85,.5);  color:#fe2c55; }

/* Capture button */
.tpt-capture-btn { width:100%; display:flex; align-items:center; justify-content:center; gap:6px; padding:8px 0; background:var(--tpt-btn-bg); border:1px solid var(--tpt-btn-bd); border-radius:9px; color:var(--tpt-tx); font-size:11.5px; font-weight:600; cursor:pointer; font-family:inherit; transition:all .15s; }
.tpt-capture-btn:hover { background:rgba(128,128,128,0.1); border-color:rgba(128,128,128,0.2); }

/* Download section */
.tpt-dl-sec { padding-bottom:10px; }
.tpt-sec-title { font-size:10.5px; font-weight:600; color:var(--tpt-sub); letter-spacing:.5px; text-transform:uppercase; margin-bottom:8px; }
.tpt-url-row { display:flex; gap:5px; margin-bottom:7px; }
.tpt-url-input { flex:1; background:var(--tpt-input-bg); border:1px solid var(--tpt-btn-bd); border-radius:8px; color:var(--tpt-input-tx); font-size:11px; padding:7px 10px; outline:none; font-family:inherit; transition:border-color .15s; }
.tpt-url-input:focus { border-color:rgba(37,244,238,.6); background:rgba(37,244,238,.05); }
.tpt-url-go { background:rgba(254,44,85,.12); border:1px solid rgba(254,44,85,.28); border-radius:8px; color:#fe2c55; font-size:15px; width:34px; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:all .15s; flex-shrink:0; }
.tpt-url-go:hover { background:rgba(254,44,85,.22); border-color:rgba(254,44,85,.5); }
.tpt-url-go:disabled { opacity:.4; cursor:default; }
.tpt-dl-bar { display:flex; align-items:center; justify-content:space-between; min-height:16px; margin-bottom:5px; }
.tpt-dl-status { font-size:10.5px; flex:1; line-height:1.4; color:var(--tpt-sub); }
.tpt-dl-status.ok      { color:#4caf50; }
.tpt-dl-status.error   { color:#ff5252; }
.tpt-dl-status.loading { color:var(--tpt-sub); }
.tpt-clear-btn { background:transparent; border:1px solid var(--tpt-bd); border-radius:5px; color:var(--tpt-tx); font-size:10px; padding:2px 7px; cursor:pointer; font-family:inherit; transition:all .15s; flex-shrink:0; }
.tpt-clear-btn:hover { background:rgba(255,80,80,.12); border-color:rgba(255,80,80,.25); color:#ff5252; }
#tpt-dl-result { display:flex; flex-direction:column; gap:4px; }
.dl-meta { font-size:10px; color:var(--tpt-sub); margin-bottom:5px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
.dl-link { display:flex; align-items:center; justify-content:space-between; padding:7px 10px; background:var(--tpt-btn-bg); border:1px solid var(--tpt-btn-bd); border-radius:8px; color:var(--tpt-tx); font-size:11.5px; font-weight:500; text-decoration:none; transition:all .14s; gap:8px; }
.dl-link:hover { background:rgba(37,244,238,.09); border-color:rgba(37,244,238,.28); color:#00aba3; }
@media (prefers-color-scheme: dark) { .dl-link:hover { color:#25f4ee; } }
.dl-label { flex:1; }
.dl-sz { font-size:10px; color:var(--tpt-sub); white-space:nowrap; flex-shrink:0; }

/* Toast */
#tpt-toast { position:absolute; bottom:-44px; left:50%; transform:translateX(-50%) translateY(6px); background:rgba(0,0,0,.85); border:1px solid rgba(255,255,255,.1); border-radius:20px; padding:6px 16px; font-size:11.5px; color:#fff; white-space:nowrap; opacity:0; pointer-events:none; transition:opacity .22s,transform .22s; backdrop-filter:blur(10px); }
@media (prefers-color-scheme: dark) { #tpt-toast { background:rgba(16,16,24,.97); color:#ccc; } }
#tpt-toast.show { opacity:1; transform:translateX(-50%) translateY(0); }

```

### File: content.js
```js

// TikTok Pro Tools - Content Script v12
  (function () {
    'use strict';
    if (window.__tptLoaded) return;
    window.__tptLoaded = true;

    // ─── INJECT AUDIO/PLAY HOOKS (WEB ACCESSIBLE) ──────────────────────────────
    const s = document.createElement('script');
    s.src = chrome.runtime.getURL('hook.js');
    s.onload = function() {
        this.remove();
    };
    (document.head || document.documentElement).appendChild(s);


  
  
    let cfg = {
      backgroundPlay: true,
      autoPauseAudio: true,
      autoScroll: false,
      speed: 1, 
      eq: 'normal',
      eqBass: 0,
      eqMid: 0,
      eqTreble: 0,
      cleanMode: false,
      unlockShop: false,
      blockKeywords: '',
      volNorm: false,
      autoPiP: true,
      audio360: false
    };

  // ─── CAPTURE ORIGINALS ───────────────────────────────────────────────────────
  


  const _origPause = HTMLVideoElement.prototype.pause;
  const _origPlay  = HTMLVideoElement.prototype.play;

  // Snapshot the real getter BEFORE we override it
  const _realHiddenGetter = (() => {
    const d = Object.getOwnPropertyDescriptor(Document.prototype, 'hidden');
    return d && d.get ? d.get : null;
  })();
  const _realVisGetter = (() => {
    const d = Object.getOwnPropertyDescriptor(Document.prototype, 'visibilityState');
    return d && d.get ? d.get : null;
  })();

  function _isReallyHidden() {
    return _realHiddenGetter ? _realHiddenGetter.call(document) : false;
  }

    // ─── BACKGROUND PLAY ─────────────────────────────────────────────────────────
  let _bgEnabled = false;

  const _stopEvent = (e) => {
      if (cfg.backgroundPlay && e.isTrusted) {
          e.stopImmediatePropagation();
      }
  };

  function enableBgPlay() {
    if (_bgEnabled) return;
    _bgEnabled = true;

    try {
      Object.defineProperty(document, 'hidden', {
        get() { return cfg.backgroundPlay ? false : (_realHiddenGetter ? _realHiddenGetter.call(document) : false); },
        configurable: true
      });
      Object.defineProperty(document, 'visibilityState', {
        get() { return cfg.backgroundPlay ? 'visible' : (_realVisGetter ? _realVisGetter.call(document) : 'visible'); },
        configurable: true
      });
    } catch (_) {}

    // Thay vì chặn pause() làm hỏng Auto-Scroll, ta chặn luôn không cho Tiktok biết người dùng rời Tab
    window.addEventListener('visibilitychange', _stopEvent, true);
    document.addEventListener('visibilitychange', _stopEvent, true);
    window.addEventListener('pagehide', _stopEvent, true);
    window.addEventListener('blur', _stopEvent, true);
  }

  function disableBgPlay() {
    cfg.backgroundPlay = false;
    _bgEnabled = false;
    window.removeEventListener('visibilitychange', _stopEvent, true);
    document.removeEventListener('visibilitychange', _stopEvent, true);
    window.removeEventListener('pagehide', _stopEvent, true);
    window.removeEventListener('blur', _stopEvent, true);
  }




  // ─── AUTO PAUSE ON OTHER AUDIO ────────────────────────────────────────────────

  // ─── SCREENSHOT ──────────────────────────────────────────────────────────────
  function captureFrame() {
    const v = _best(); if (!v || v.videoWidth === 0) return;
    const c = document.createElement('canvas'); c.width = v.videoWidth; c.height = v.videoHeight;
    c.getContext('2d').drawImage(v, 0, 0);
    c.toBlob(blob => {
      if (!blob) return;
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a'); a.href = url; a.download = 'tiktok-' + Date.now() + '.png';
      document.body.appendChild(a); a.click(); document.body.removeChild(a);
      setTimeout(() => URL.revokeObjectURL(url), 5000);
    }, 'image/png');
  }

  
// ─── BACKGROUND RAF MOCK ─────────────────────────────────────────────────────
// TikTok's native Auto Scroll usually relies on requestAnimationFrame.
// In background tabs, rAF stops completely. We proxy it to setTimeout so native features keep working!
const _origRaf = window.requestAnimationFrame;
const _origCancelRaf = window.cancelAnimationFrame;
let rafPolyfillActive = false;


let _fadeInterval = null;
let _origVolume = 1;
let _pausedByExtension = false;

function fadeToPause() {
    const video = document.querySelector('video');
    if (!video || video.paused) return;
    clearInterval(_fadeInterval);
    _origVolume = video.volume > 0 ? video.volume : 1;
    _pausedByExtension = true;
    let v = video.volume;
    _fadeInterval = setInterval(() => {
        v -= 0.1;
        if (v <= 0) {
            clearInterval(_fadeInterval);
            video.volume = 0;
            video.pause();
        } else {
            video.volume = v;
        }
    }, 50);
}

function fadeToResume() {
    const video = document.querySelector('video');
    if (!video || !_pausedByExtension) return;
    _pausedByExtension = false;
    clearInterval(_fadeInterval);
    video.play().then(() => {
        let v = 0;
        video.volume = 0;
        _fadeInterval = setInterval(() => {
            v += 0.1;
            if (v >= _origVolume) {
                clearInterval(_fadeInterval);
                video.volume = _origVolume;
            } else {
                video.volume = v;
            }
        }, 50);
    }).catch(e => console.error("Fade resume error:", e));
}


function activateBackgroundRaf() {
    if (rafPolyfillActive) return;
    rafPolyfillActive = true;
    window.requestAnimationFrame = function(cb) {
        if (_isReallyHidden()) {
            // Tab is in background, proxy to setTimeout so it doesn't freeze
            return setTimeout(() => cb(performance.now()), 16);
        }
        return _origRaf.call(window, cb);
    };
    window.cancelAnimationFrame = function(id) {
        if (_isReallyHidden()) {
            clearTimeout(id);
        } else {
            _origCancelRaf.call(window, id);
        }
    };
}
activateBackgroundRaf();

chrome.runtime.onMessage.addListener((msg) => {
    if (msg.action === 'other_audio_start' && cfg.autoPauseAudio) {
        fadeToPause();
    } else if (msg.action === 'other_audio_stop' && cfg.autoPauseAudio) {
        fadeToResume();
    }
});

// ─── AUDIO EQUALIZER ─────────────────────────────────────────────────────────
  const audioContextMap = new WeakMap();

  document.addEventListener('pointerdown', () => {
      document.querySelectorAll('video').forEach(v => {
          const nodes = audioContextMap.get(v);
          if (nodes && nodes.ctx && nodes.ctx.state === 'suspended') {
              nodes.ctx.resume().catch(()=>{});
          }
      });
  }, { capture: true });

  function applyEqToVideo(videoElement) {
    if (cfg.eq === 'normal' && !cfg.eqBass && !cfg.eqMid && !cfg.eqTreble && !cfg.volNorm && !cfg.audio360) return;

    if (!videoElement.hasAttribute('crossorigin')) {
        try { 
            videoElement.crossOrigin = "anonymous"; 
            // Cần force reload src nếu src đã chạy để nhận crossorigin (nếu không sẽ silence WebAudio)
            // Tuy nhiên reload sẽ giật khung hình, ta chỉ set trước. hook.js cũng có làm việc này.
        } catch(e){}
    }

    
    // Yêu cầu có tương tác người dùng mới bật AudioContext

    // Yêu cầu có tương tác người dùng mới bật AudioContext
    // Nhưng nếu return ở đây, nó sẽ không bao giờ khởi tạo cho video đang có!
    // -> Khởi tạo ở trạng thái suspended, khi click sẽ resume


    if (videoElement._audioContextCreated) {
        let audioNodes = audioContextMap.get(videoElement);
        if (audioNodes) {
             // Continue to update EQ gains
        } else {
             return;
        }
    }
    
    if (!audioContextMap.has(videoElement)) {
      try {
        videoElement._audioContextCreated = true;
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        const ctx = new AudioContext();
        const source = ctx.createMediaElementSource(videoElement);
        
        const bassNode = ctx.createBiquadFilter();
        bassNode.type = "lowshelf";
        bassNode.frequency.value = 250;
        
        const trebleNode = ctx.createBiquadFilter();
        trebleNode.type = "highshelf";
        trebleNode.frequency.value = 6000;
        
        const midNode = ctx.createBiquadFilter();
        midNode.type = "peaking";
        midNode.frequency.value = 1000;
        midNode.Q.value = 1;
        
        const compNode = ctx.createDynamicsCompressor();
        compNode.threshold.value = -24;
        compNode.knee.value = 30;
        compNode.ratio.value = 12;
        compNode.attack.value = 0.003;
        compNode.release.value = 0.25;

        // 360 Audio (8D) setup
        const pannerNode = ctx.createStereoPanner ? ctx.createStereoPanner() : null;
        if (pannerNode) {
            if (!window._tptPanners) window._tptPanners = [];
            window._tptPanners.push(pannerNode);
            
            // Re-route with panner
            source.connect(compNode);
            compNode.connect(bassNode);
            bassNode.connect(midNode);
            midNode.connect(trebleNode);
            trebleNode.connect(pannerNode);
            pannerNode.connect(ctx.destination);
            
            audioContextMap.set(videoElement, { ctx, bassNode, midNode, trebleNode, compNode, pannerNode });
        } else {
            source.connect(compNode);
            compNode.connect(bassNode);
            bassNode.connect(midNode);
            midNode.connect(trebleNode);
            trebleNode.connect(ctx.destination);

            audioContextMap.set(videoElement, { ctx, bassNode, midNode, trebleNode, compNode });
        }
      } catch (e) {
        // Silently ignore if AudioContext fails (e.g. InvalidStateError in background or already connected)
        // console.debug("EQ init skipped for this video element");
      }
    }

    const audioNodes = audioContextMap.get(videoElement);
    if (!audioNodes) return;
    
    if (audioNodes.ctx.state === 'suspended') {
        if (navigator.userActivation && navigator.userActivation.hasBeenActive) {
            audioNodes.ctx.resume().catch(() => {});
        }
    }

    audioNodes.bassNode.gain.value = 0;
    audioNodes.midNode.gain.value = 0;
    audioNodes.trebleNode.gain.value = 0;
    
    // Toggle dynamics compressor dynamically
    if (audioNodes.compNode) {
        if (cfg.volNorm) {
            audioNodes.compNode.threshold.value = -24; // Bắt đầu nén khi nguồn vượt âm lượng
            audioNodes.compNode.ratio.value = 8;
        } else {
            audioNodes.compNode.threshold.value = 0; // Bypass
            audioNodes.compNode.ratio.value = 1;
        }
    }

    switch (cfg.eq) {
      case 'bass':
        audioNodes.bassNode.gain.value = 12;
        audioNodes.trebleNode.gain.value = -3;
        break;
      case 'treble':
        audioNodes.trebleNode.gain.value = 12;
        audioNodes.bassNode.gain.value = -3;
        break;
      case 'vocal':
        audioNodes.midNode.gain.value = 8;
        audioNodes.bassNode.gain.value = -5;
        audioNodes.trebleNode.gain.value = 2;
        break;
      case 'advanced':
        audioNodes.bassNode.gain.value = cfg.eqBass || 0;
        audioNodes.midNode.gain.value = cfg.eqMid || 0;
        audioNodes.trebleNode.gain.value = cfg.eqTreble || 0;
        break;
      case 'normal':
      default:
        break;
    }
  }
  
  // ─── 360 AUDIO ANIMATION (8D) ────────────────────────────────────────────────
  let _panAngle = 0;
  setInterval(() => {
    if (!cfg.audio360 || !window._tptPanners) {
        if (window._tptPanners) {
            window._tptPanners.forEach(p => {
                if (p.pan.value !== 0) p.pan.value = 0;
            });
        }
        return;
    }
    _panAngle += 0.05; // speed of panning
    const panValue = Math.sin(_panAngle) * 0.8; // range -0.8 (left) to 0.8 (right)
    window._tptPanners.forEach(p => {
        try { p.pan.value = panValue; } catch(e){}
    });
  }, 50);

  // ─── CLEAN MODE ──────────────────────────────────────────────────────────────
  let tptStyleElement = null;

  function updateInjectedStyles() {
    if (!tptStyleElement) {
      tptStyleElement = document.createElement('style');
      tptStyleElement.id = 'tpt-injected-styles';
      document.head.appendChild(tptStyleElement);
    }
    
    let css = '';
    if (cfg.cleanMode) {
      css += `
        [data-e2e="video-desc"],
        [data-e2e="video-author-avatar"],
        [data-e2e="browser-nickname"],
        [data-e2e="video-music"],
        [class*="DivVideoInfoContainer"],
        [class*="DivMediaCardOverlayBottom"],
        [class*="DivActionItemContainer"],
        .tiktok-1vyw0v6-DivVideoInfoContainer,
        .tiktok-14bqk18-DivVideoContainer {
            opacity: 0 !important;
            pointer-events: none !important;
            transition: opacity 0.3s ease;
        }
      `;
    }
    
    tptStyleElement.textContent = css;
  }

  // ─── SHOP VIDEO UNBLOCKER ───────────────────────────────────────────────────
  let _shopFetching = new WeakSet();
  
  function checkShopVideos() {
    if (!cfg.unlockShop) return;
    
    // Tìm các container lớn có thể chứa video (bao gồm cả trường hợp TikTok xoá luôn thẻ video)
    const wrappers = document.querySelectorAll(
      '[class*="DivVideoWrapper"], [class*="DivVideoContainer"], [data-e2e="recommend-list-item-container"], .video-container'
    );
    
    wrappers.forEach(wrapper => {
      // Để tránh tìm trùng lớp cha-con, loại bỏ cha nếu có con tương tự
      if (wrapper.querySelector('[class*="DivVideoWrapper"]') && wrapper.className.includes('Container')) return;
      
      if (wrapper.dataset.tptShopFixed || _shopFetching.has(wrapper)) return;
      
      const rect = wrapper.getBoundingClientRect();
      const isVisible = rect.height > 0 && rect.top >= -500 && rect.bottom <= window.innerHeight + 500;
      if (!isVisible) return; 
      
      const vid = wrapper.querySelector('video');
      
      // Phát hiện video bị chặn (không có thẻ <video>, hoặc có nhưng không có source/không phát được)
      const isBlocked = !vid || (!vid.src && !vid.currentSrc && !vid.querySelector('source')) || 
                        (vid.readyState === 0 && (!vid.hasAttribute('src') || vid.getAttribute('src') === ''));
      
      // Loại hẳn bài đăng ảnh cuộn bị nhận diện nhầm
      if (wrapper.querySelector('[class*="DivImageContainer"]') || wrapper.innerHTML.includes('photo')) {
          if (!vid) return; 
      }

      // Tiêu chí bổ sung: Chữ "Xem video" hoặc icon báo lỗi của tiktok
      const hasErrorText = /TikTok Shop|(video|Nội dung|content).*?(không khả dụng|bị giới hạn|unavailable|restricted|not available)/i.test(wrapper.innerText || "");

      if (isBlocked || (!vid && hasErrorText)) {
        let targetUrl = window.location.href;
        
        // Tìm URL chuẩn trong feed nếu có
        const container = wrapper.closest('[data-e2e="recommend-list-item-container"], [class*="DivItemContainer"]');
        if (c
... [TRUNCATED]
```

### File: hook.js
```js

const _realCreateElement = document.createElement;
document.createElement = function(tagName, options) {
    const el = _realCreateElement.call(this, tagName, options);
    if (tagName.toLowerCase() === 'video') {
        el.crossOrigin = "anonymous";
    }
    return el;
};

// TikTok Pro Tools - Script Injected into Web Context
const _realPlay = HTMLVideoElement.prototype.play;
const _realVisGetter = Object.getOwnPropertyDescriptor(Document.prototype, 'visibilityState')?.get;

function getTrueVisibility() {
    return _realVisGetter ? _realVisGetter.call(document) : document.visibilityState;
}

HTMLVideoElement.prototype.play = function() {
    return _realPlay.call(this).catch(err => {
        // Only swallow and force-mute if we are in a background tab
        if (err.name === 'NotAllowedError' && getTrueVisibility() === 'hidden') {
            this.muted = true;
            this.dataset.tptAutoMuted = 'true';
            return _realPlay.call(this).catch(()=>{});
        }
        throw err; // Let TikTok's own UI handle foreground play-blocking
    });
};

/* Web Audio API Interceptor for EQ and 360 Audio */
const _realCreateMediaElementSource = AudioContext.prototype.createMediaElementSource || webkitAudioContext.prototype.createMediaElementSource;
const _tptAudioNodes = new WeakMap();

// Listen to custom events from content.js to update the EQ on the fly
window.addEventListener('tpt-eq-update', (e) => {
    const data = e.detail;
    // Apply changes to all our active injected audio contexts
    document.querySelectorAll('video').forEach(videoElement => {
         const nodes = _tptAudioNodes.get(videoElement);
         if (nodes) {
             if (nodes.ctx.state === 'suspended') {
                 nodes.ctx.resume().catch(()=>{});
             }
             // Map data setting to the nodes
             if (data.bass !== undefined && nodes.bassNode) nodes.bassNode.gain.value = +data.bass;
             if (data.mid !== undefined && nodes.midNode) nodes.midNode.gain.value = +data.mid;
             if (data.treble !== undefined && nodes.trebleNode) nodes.trebleNode.gain.value = +data.treble;
             
             if (data.eq !== undefined) {
                 // For presets like 'bbass', etc. If you want hardcoded values you'd map them here or in content.js
             }
         }
    });
});

AudioContext.prototype.createMediaElementSource = function(mediaElement) {
    const sourceNode = _realCreateMediaElementSource.call(this, mediaElement);
    
    try {
        const bassNode = this.createBiquadFilter();
        bassNode.type = "lowshelf";
        bassNode.frequency.value = 250;
        bassNode.gain.value = 0;
        
        const midNode = this.createBiquadFilter();
        midNode.type = "peaking";
        midNode.frequency.value = 1000;
        midNode.Q.value = 1;
        midNode.gain.value = 0;

        const trebleNode = this.createBiquadFilter();
        trebleNode.type = "highshelf";
        trebleNode.frequency.value = 6000;
        trebleNode.gain.value = 0;
        
        const pannerNode = this.createStereoPanner ? this.createStereoPanner() : null;

        // Create a custom shim for connect
        const realConnect = sourceNode.connect;
        
        // We hijack the first connect call to inject our nodes in the middle
        sourceNode.connect = function(destination, output=0, input=0) {
            // Disconnect old chain
            realConnect.call(this, bassNode);
            bassNode.connect(midNode);
            midNode.connect(trebleNode);
            
            let lastNode = trebleNode;
            if (pannerNode) {
                lastNode.connect(pannerNode);
                lastNode = pannerNode;
            }
            
            // Finally connect our last node to the REAL destination
            lastNode.connect(destination, output, input);
            
            _tptAudioNodes.set(mediaElement, {
                ctx: this.context,
                sourceNode: this,
                bassNode,
                midNode,
                trebleNode,
                pannerNode,
                isHooked: true
            });
            
            // Revert connect so subsequent calls just behave normally (but we might break complex graphs)
            // For now, return the destination for chaining
            return destination;
        };

        mediaElement._tptAudioHooked = true;

    } catch(e) {
        console.error("TPT Audio Hook failed:", e);
    }
    
    return sourceNode;
};
// Trigger custom event just in case content.js needs to know about this script
window.dispatchEvent(new CustomEvent('tpt-hook-ready'));

```

### File: manifest.json
```json
{
  "manifest_version": 3,
  "name": "TikTok Pro Tools",
  "version": "1.0.0",
  "description": "Background play, auto-pause, speed control, frame capture & video download for TikTok",
  "permissions": [
    "storage",
    "tabs",
    "scripting",
    "alarms",
    "downloads"
  ],
  "host_permissions": [
    "*://*.tiktok.com/*",
    "https://tikwm.com/*"
  ],
  "background": {
    "service_worker": "background.js",
    "type": "module"
  },
  "content_scripts": [
    {
      "matches": [
        "*://*.tiktok.com/*"
      ],
      "js": [
        "content.js"
      ],
      "css": [
        "content.css"
      ],
      "run_at": "document_idle",
      "all_frames": false
    }
  ],
  "action": {
    "default_popup": "popup.html",
    "default_icon": {
      "16": "icons/icon16.png",
      "32": "icons/icon32.png",
      "48": "icons/icon48.png",
      "128": "icons/icon128.png"
    }
  },
  "icons": {
    "16": "icons/icon16.png",
    "48": "icons/icon48.png",
    "128": "icons/icon128.png"
  },
  "web_accessible_resources": [
    {
      "resources": [
        "hook.js"
      ],
      "matches": [
        "*://*.tiktok.com/*",
        "https://*.tiktok.com/*"
      ]
    }
  ]
}
```

### File: popup.css
```css
* { box-sizing: border-box; margin: 0; padding: 0; }
:root {
  --red: #fe2c55; --cyan: #25f4ee;
  --bg: #f8f9fa; --s1: #ffffff; --s2: #f0f2f5;
  --bd: rgba(0,0,0,0.08); --tx: #111118; --mt: #65676b;
  --sw-bg: #e4e6eb; --sw-k: #fff;
  --logo-text: #111; --status-bg: #e4e6eb;
  --btn-bg: #f0f2f5; --btn-tx: #333; --btn-bd: rgba(0,0,0,0.1);
  --ps-on: rgba(254,44,85,.1); --ps-on-bd: rgba(254,44,85,.3);
}

:root.dark-theme {
  --bg: #090910; --s1: #111118; --s2: #17171f;
  --bd: rgba(255,255,255,0.07); --tx: #ddd; --mt: #888;
  --sw-bg: #222; --sw-k: #484848;
  --logo-text: #fff; --status-bg: #2a2a2a;
  --btn-bg: #222; --btn-tx: #ccc; --btn-bd: rgba(255,255,255,0.1);
  --ps-on: rgba(254,44,85,.18); --ps-on-bd: rgba(254,44,85,.5);
}

@media (prefers-color-scheme: dark) {
  :root:not(.light-theme) {
    --bg: #090910; --s1: #111118; --s2: #17171f;
    --bd: rgba(255,255,255,0.07); --tx: #ddd; --mt: #888;
    --sw-bg: #222; --sw-k: #484848;
    --logo-text: #fff; --status-bg: #2a2a2a;
    --btn-bg: #222; --btn-tx: #ccc; --btn-bd: rgba(255,255,255,0.1);
    --ps-on: rgba(254,44,85,.18); --ps-on-bd: rgba(254,44,85,.5);
  }
}

body { font-family:'DM Sans',-apple-system,sans-serif; background:var(--bg); color:var(--tx); width:500px; }

/* Header */
.hdr {
  display:flex; align-items:center; justify-content:space-between;
  padding:14px 16px 12px;
  border-bottom:1px solid var(--bd);
  background:linear-gradient(160deg,rgba(254,44,85,.07),transparent 60%);
}
.logo { display:flex; align-items:center; gap:10px; }
.logo h1 { font-size:13.5px; font-weight:700; color:var(--logo-text); letter-spacing:-.3px; }
.logo p { font-size:10px; color:var(--mt); margin-top:1px; }
.status { display:flex; align-items:center; gap:5px; font-size:11px; color:var(--mt); }
.dot { width:7px; height:7px; border-radius:50%; background:var(--status-bg); transition:background .3s; }
.status.on .dot { background:#4caf50; box-shadow:0 0 6px #4caf50; }
.status.on #stext { color:#81c784; }

/* Content */
.content { padding:14px; display:flex; flex-direction:column; gap:10px; }

/* Group */
.group { background:var(--s1); border:1px solid var(--bd); border-radius:10px; overflow:hidden; }
.gtitle { font-size:10.5px; font-weight:600; color:var(--mt); letter-spacing:.6px; text-transform:uppercase; padding:9px 13px 5px; }

/* Row */
.row { display:flex; align-items:center; justify-content:space-between; padding:9px 13px; border-top:1px solid var(--bd); }
.ri { flex:1; }
.rn { display:block; font-size:12.5px; font-weight:500; color:var(--tx); margin-bottom:2px; }
.rd { display:block; font-size:10.5px; color:var(--mt); }
.tpt-select {
  background: var(--btn-bg);
  color: var(--tx);
  border: 1px solid var(--btn-bd);
  border-radius: 6px;
  padding: 4px 8px;
  font-size: 11px;
  font-weight: 500;
  font-family: inherit;
  outline: none;
  cursor: pointer;
}
.tpt-select:hover { background: rgba(0,0,0,0.05); }
:root.dark-theme .tpt-select:hover { background: rgba(255,255,255,0.05); }

/* Switch */
.sw { flex-shrink:0; margin-left:10px; cursor:pointer; }
.sw input { display:none; }
.st { display:block; width:38px; height:21px; background:var(--sw-bg); border-radius:21px; position:relative; transition:background .2s; }
.sk { position:absolute; top:3px; left:3px; width:15px; height:15px; background:var(--sw-k); border-radius:50%; transition:transform .2s,background .2s; box-shadow:0 1px 3px rgba(0,0,0,.4); }
.sw input:checked + .st { background:rgba(254,44,85,.72); }
.sw input:checked + .st .sk { transform:translateX(17px); background:#fff; }

/* Mini slider */
.msl { flex-shrink:0; width:100%; margin-left:0; margin-top:4px; }
.mslider { -webkit-appearance:none; width:100%; height:6px; border-radius:6px; outline:none; cursor:pointer; background:rgba(0,0,0,.1); transition:background .2s; }
:root.dark-theme .mslider { background: rgba(255,255,255,.1); }
@media (prefers-color-scheme: dark) { :root:not(.light-theme) .mslider { background: rgba(255,255,255,.1); } }

/* Slider Tracks with Variables */
#s-speed { background: linear-gradient(to right, var(--red) var(--fill, 25%), rgba(0,0,0,.1) var(--fill, 25%)); }
#s-vol   { background: linear-gradient(to right, var(--cyan) var(--fill, 100%), rgba(0,0,0,.1) var(--fill, 100%)); }

:root.dark-theme #s-speed { background: linear-gradient(to right, var(--red) var(--fill, 25%), rgba(255,255,255,.1) var(--fill, 25%)); }
:root.dark-theme #s-vol   { background: linear-gradient(to right, var(--cyan) var(--fill, 100%), rgba(255,255,255,.1) var(--fill, 100%)); }

@media (prefers-color-scheme: dark) {
  :root:not(.light-theme) #s-speed { background: linear-gradient(to right, var(--red) var(--fill, 25%), rgba(255,255,255,.1) var(--fill, 25%)); }
  :root:not(.light-theme) #s-vol   { background: linear-gradient(to right, var(--cyan) var(--fill, 100%), rgba(255,255,255,.1) var(--fill, 100%)); }
}

.mslider::-webkit-slider-thumb { -webkit-appearance:none; width:16px; height:16px; border-radius:50%; background:#fff; border:1px solid rgba(0,0,0,.15); box-shadow:0 2px 4px rgba(0,0,0,.2); cursor:pointer; transition:transform .1s; }
.mslider:active::-webkit-slider-thumb { transform:scale(1.15); }
.msl-c::-webkit-slider-thumb { border-color:rgba(0,0,0,.1); }


/* Note */
.note { background:rgba(255,255,255,.03); border:1px solid var(--bd); border-radius:10px; padding:10px 12px; }
.note p { font-size:11px; color:#555; line-height:1.55; }
.note strong { color:#777; }

/* Toast */
.toast {
  position:fixed; bottom:12px; left:50%;
  transform:translateX(-50%) translateY(8px);
  background:rgba(0,0,0,0.8); border:1px solid rgba(0,0,0,0.1);
  backdrop-filter:blur(10px); border-radius:20px; padding:6px 16px;
  font-size:12px; color:#fff; opacity:0; transition:all .22s;
  pointer-events:none; white-space:nowrap;
}
@media (prefers-color-scheme: dark) {
  .toast {
    background:rgba(255,255,255,.09); border:1px solid rgba(255,255,255,.12);
  }
}
.toast.show { opacity:1; transform:translateX(-50%) translateY(0); }

/* New UI Elements */
.reload-warning { background:rgba(255,165,0,.15); color:#d98400; border:1px solid rgba(255,165,0,.3); border-radius:8px; padding:10px 14px; font-size:11px; font-weight:500; line-height:1.45; text-align:center; }
.hdr-row { padding-top:6px; padding-bottom:6px; border-top:none; }
.theme-btn { 
  cursor:pointer; display:flex; align-items:center; justify-content:center;
  width:26px; height:26px; border-radius:50%; background:var(--sw-bg);
  border:1px solid var(--btn-bd); color:var(--tx);
  transition:all .2s; outline:none; 
}
.theme-btn:hover { background:var(--btn-bg); transform:scale(1.05); }

/* Sun/Moon Toggle */
.sun-icon { display: none; }
.moon-icon { display: block; }
:root.dark-theme .sun-icon { display: block; }
:root.dark-theme .moon-icon { display: none; }

.sr-col { flex-direction:column; align-items:flex-start; gap:8px; }
.sr-top { display:flex; justify-content:space-between; width:100%; align-items:flex-end; }
.ps-row { display:flex; gap:6px; width:100%; }
.ps-btn { flex:1; background:var(--btn-bg); border:1px solid var(--btn-bd); border-radius:6px; color:var(--btn-tx); font-size:11px; font-weight:600; padding:6px 0; cursor:pointer; font-family:inherit; transition:all .15s; }
.ps-btn:hover { background:rgba(254,44,85,.08); border-color:rgba(254,44,85,.2); color:var(--red); }
.ps-btn.on { background:var(--ps-on); border-color:var(--ps-on-bd); color:var(--red); }

.btn-action { width:100%; background:var(--btn-bg); border:1px solid var(--btn-bd); border-radius:8px; color:var(--btn-tx); font-size:12px; font-weight:600; padding:9px 0; cursor:pointer; font-family:inherit; transition:all .15s; display:flex; align-items:center; justify-content:center; gap:6px; }
.btn-action:hover { background:rgba(254,44,85,.08); border-color:rgba(254,44,85,.2); color:var(--red); }



.features-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  border-top: 1px solid var(--bd);
}
.features-grid .row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  border-top: none;
  border-bottom: 1px solid var(--bd);
  border-right: 1px solid var(--bd);
  margin: 0;
}
.features-grid .row:nth-child(even) {
  border-right: none;
}
.features-grid .row:nth-last-child(-n+2) { /* If it has an even number, bottom rows shouldn't have bottom border, but let's keep it simple and just let it have one or remove later */
}
.features-grid .ri {
  flex: 1;
  padding-right: 10px;
}
.features-grid .rn {
  display: flex !important;
  align-items: center;
  font-size: 11.5px;
  font-weight: 600;
  margin-bottom: 2px;
  white-space: nowrap;
}
.features-grid .rd {
  font-size: 10px;
  line-height: 1.35;
  color: var(--mt);
}
.features-grid .txt {
  flex: 1;
  padding-right: 10px;
}
.features-grid .txt div:first-child {
  display: flex;
  align-items: center;
  font-size: 11.5px;
  font-weight: 600;
  margin-bottom: 2px;
}
.features-grid .txt div.sub {
  font-size: 10px;
  color: var(--mt);
  line-height: 1.35;
}

.mini-window-section {
    padding: 12px;
    border: 1px solid #333;
    border-radius: 8px;
    margin: 10px 0;
    background: #1a1a1a;
    font-size: 13px;
}
.mini-window-section h3 {
    margin: 0 0 8px 0;
    color: #fff;
    font-size: 14px;
}
.description {
    font-size: 12px;
    color: #aaa;
    margin-bottom: 12px;
}
.size-options, .position-options {
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.size-options label, .position-options label {
    color: #ccc;
    font-size: 13px;
}
.size-options select, .position-options select {
    padding: 4px 8px;
    border-radius: 4px;
    background: #2a2a2a;
    color: #fff;
    border: 1px solid #444;
}
.btn-primary {
    width: 100%;
    padding: 10px;
    margin: 8px 0 4px;
    border: none;
    border-radius: 6px;
    background: #fe2c55;
    color: white;
    font-size: 14px;
    font-weight: bold;
    cursor: pointer;
}
.btn-primary:hover {
    background: #e0284d;
}
.btn-secondary {
    width: 100%;
    padding: 8px;
    margin: 4px 0 0;
    border: 1px solid #555;
    border-radius: 6px;
    background: transparent;
    color: #ccc;
    font-size: 13px;
    cursor: pointer;
}
.btn-secondary:hover {
    background: #333;
}
.note {
    font-size: 11px;
    color: #888;
    margin-top: 8px;
    line-height: 1.4;
}

```

### File: popup.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>TikTok Pro Tools</title>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="popup.css">
</head>
<body>
<div class="wrap">
  <header class="hdr">
    <div class="logo">
      <svg width="22" height="22" viewBox="0 0 24 24">
        <path d="M19.59 6.69a4.83 4.83 0 0 1-3.77-4.25V2h-3.45v13.67a2.89 2.89 0 0 1-2.88 2.5 2.89 2.89 0 0 1-2.89-2.89 2.89 2.89 0 0 1 2.89-2.89c.28 0 .54.04.79.1V9.01a6.33 6.33 0 0 0-.79-.05 6.34 6.34 0 0 0-6.34 6.34 6.34 6.34 0 0 0 6.34 6.34 6.34 6.34 0 0 0 6.33-6.34V9.15a8.16 8.16 0 0 0 4.77 1.52V7.22a4.85 4.85 0 0 1-1-.53z" fill="#fe2c55"/>
      </svg>
      <div><h1>TikTok Pro Tools</h1><p>v1.0.0</p></div>
    </div>
    <div class="status" id="status">
      <span class="dot"></span><span id="stext">Checking…</span>
    </div>
  </header>

  <div class="content">
    <div class="reload-warning" style="display:none" id="reload-warning">
      ⚠ Please reload the TikTok page (F5) for changes to apply or to fix "Context Invalidated" errors.
    </div>
    
    <div class="group">
        <div class="row hdr-row" style="cursor: pointer;" id="features-toggle-row">
          <div style="display:flex; align-items:center; gap:6px;">
            <svg id="features-arrow" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="transition: transform 0.2s; transform: rotate(180deg);"><polyline points="6 9 12 15 18 9"></polyline></svg>
            <p class="gtitle" style="padding:0; margin:0">Features</p>
          </div>
          <button class="theme-btn" id="theme-toggle" aria-label="Toggle Dark Mode" onclick="event.stopPropagation();">
            <svg class="sun-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
            <svg class="moon-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
          </button>
        </div>
        
        <div class="features-grid" id="features-grid-content">
          <div class="row">
            <div class="ri">
               <span class="rn">
                 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
                 Background Play
               </span>
               <span class="rd">Keep playing when switching tabs</span>
            </div>
            <label class="sw"><input type="checkbox" id="c-bg"><span class="st"><span class="sk"></span></span></label>
          </div>
          
          <div class="row">
            <div class="ri">
               <span class="rn">
                 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><path d="M11 5L6 9H2v6h4l5 4zM22 9l-6 6M16 9l6 6"/></svg>
                 Auto-Pause
               </span>
               <span class="rd">Auto pause when other tab plays media</span>
            </div>
            <label class="sw"><input type="checkbox" id="c-autopause"><span class="st"><span class="sk"></span></span></label>
          </div>

          <div class="row" style="flex-wrap: wrap;">
            <div class="ri" style="flex: 1;">
               <span class="rn">
                 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><rect x="12" y="14" width="7" height="5" rx="1" ry="1"></rect></svg>
                 Auto PiP (Mini)
                 <span id="btn-pip-help" style="cursor:help; background:var(--mt); color:#fff; width:14px; height:14px; display:inline-flex; align-items:center; justify-content:center; border-radius:50%; font-size:9px; margin-left:4px; font-weight:bold;">?</span>
               </span>
               <span class="rd">Auto trigger PiP mini player</span>
            </div>
            <label class="sw"><input type="checkbox" id="c-pip"><span class="st"><span class="sk"></span></span></label>
            
            <div id="pip-help-box" style="display:none; width:100%; margin-top:8px; padding:10px; background:rgba(254,44,85,0.05); border:1px solid rgba(254,44,85,0.2); border-radius:8px; font-size:11px; align-items:flex-start; flex-direction:column; gap:6px;">
                <strong style="color:#fe2c55;">To enable Auto PiP fully:</strong>
                <ol style="margin:4px 0 4px 16px; padding:0; color:var(--tx);">
                    <li>Open <code style="background:var(--bg2); padding:2px 4px; border-radius:4px; user-select:all;">chrome://flags/#auto-picture-in-picture</code></li>
                    <li>Set <b>Auto Picture-in-Picture for video sites</b> to <code>Enabled</code>.</li>
                    <li>Relaunch Chrome.</li>
                </ol>
                <div style="font-size:10px; color:var(--mt); margin-top:2px;">
                    <i>Note: Now you can scroll the mouse wheel over the PiP window to change videos!</i>
                </div>
            </div>
          </div>
          
          <div class="row">
            <div class="ri">
               <span class="rn">
                 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
                 Clean Video Mode
               </span>
               <span class="rd">Hide text overlays and UI elements</span>
            </div>
            <label class="sw"><input type="checkbox" id="c-clean"><span class="st"><span class="sk"></span></span></label>
          </div>
          
          <div class="row">
            <div class="ri">
               <span class="rn">
                 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
                 Unlock Shop Video
               </span>
               <span class="rd">Unlock regional Shop videos</span>
            </div>
            <label class="sw"><input type="checkbox" id="c-shop"><span class="st"><span class="sk"></span></span></label>
          </div>
          
          <div class="row">
            <div class="ri">
               <span class="rn">
                 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                 Volume Normalizer
               </span>
               <span class="rd">Balance loud and quiet videos</span>
            </div>
            <label class="sw"><input type="checkbox" id="c-volnorm"><span class="st"><span class="sk"></span></span></label>
          </div>
        </div>
        
        <div class="row">
          <div class="ri">
             <span class="rn">
               <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><circle cx="12" cy="12" r="10"></circle><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line></svg>
               Block Keywords
             </span>
             <span class="rd">Auto skip & hide comments</span>
          </div>
        </div>
        <div class="row" style="padding-top:0; padding-bottom:12px; flex-direction:column; align-items:flex-start;">
          <input type="text" id="i-keywords" placeholder="ex: #drama, sad (Enter to add)" autocomplete="off" spellcheck="false" style="width:100%; padding:8px 10px; border-radius:8px; border:1px solid var(--btn-bd); background:var(--btn-bg); color:var(--tx); font-size:11px; outline:none; transition:background .2s, border-color .2s;">
          <div id="kw-tags-container" style="display:flex; flex-wrap:wrap; gap:4px; margin-top:8px; width:100%;"></div>
          <div id="kw-tags-more" style="display:none; font-size:10px; color:#fe2c55; cursor:pointer; margin-top:6px; width:100%; text-align:center; font-weight:600;">See more</div>
        </div>
      </div>
      
      <div class="group">
        <p class="gtitle">Playback</p>
      <div class="row sr-col">
        <div class="sr-top">
          <span class="rn">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
            Speed
          </span>
          <span class="rd" id="d-speed" style="font-weight:600; color:var(--tx)">1x</span>
        </div>
        <div class="msl" style="width:100%; margin:0; margin-bottom:4px"><input type="range" class="mslider" id="s-speed" min="0" max="4" step="0.05" value="1"></div>
        <div class="ps-row">
          <button class="ps-btn" data-v="0.5">0.5</button>
          <button class="ps-btn" data-v="1">1</button>
          <button class="ps-btn" data-v="1.5">1.5</button>
          <button class="ps-btn" data-v="2">2</button>
          <button class="ps-btn" data-v="3">3</button>
          <button class="ps-btn" data-v="4">4</button>
        </div>
      <div class="row">
        <div class="ri" style="display:flex; align-items:center; justify-content:space-between; width:100%;">
           <span class="rn" style="margin:0;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><line x1="4" y1="21" x2="4" y2="14"></line><line x1="4" y1="10" x2="4" y2="3"></line><line x1="12" y1="21" x2="12" y2="12"></line><line x1="12" y1="8" x2="12" y2="3"></line><line x1="20" y1="21" x2="20" y2="16"></line><line x1="20" y1="12" x2="20" y2="3"></line><line x1="1" y1="14" x2="7" y2="14"></line><line x1="9" y1="8" x2="15" y2="8"></line><line x1="17" y1="16" x2="23" y2="16"></line></svg>
             Equalizer (EQ)
           </span>
           <select id="s-eq" class="tpt-select">
             <option value="normal">Normal</option>
             <option value="bass">Bass Boost</option>
             <option value="treble">Treble Boost</option>
             <option value="vocal">Vocal Boost</option>
             <option value="advanced">Advanced</option>
           </select>
        </div>
      <div id="adv-eq-panel" style="display:none; padding:10px 14px; flex-direction:column; gap:8px; border-top:1px solid var(--bd);">
         <div class="sr-top" style="justify-content:space-between; font-size:11px; margin-bottom:2px;"><span>Bass</span><span id="d-bass">0</span></div>
         <input type="range" class="mslider" id="s-bass" min="-10" max="10" step="1" value="0">
         
         <div class="sr-top" style="justify-content:space-between; font-size:11px; margin-bottom:2px; margin-top:6px;"><span>Mid</span><span id="d-mid">0</span></div>
         <input type="range" class="mslider" id="s-mid" min="-10" max="10" step="1" value="0">
         
         <div class="sr-top" style="justify-content:space-between; font-size:11px; margin-bottom:2px; margin-top:6px;"><span>Treble</span><span id="d-treble">0</span></div>
         <input type="range" class="mslider" id="s-treble" min="-10" max="10" step="1" value="0">
      </div>
      <div class="row">
        <div class="ri">
           <span class="rn">
             <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 4px;"><path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm0 18a8 8 0 1 1 8-8 8 8 0 0 1-8 8zm0-12a4 4 0 1 0 4 4 4 4 0 0 0-4-4z"></path></svg>
             360 Audio (8D)
           </span>
        </div>
        <label class="sw"><input type="checkbox" id="c-audio360"><span class="st"><span class="sk"></span></span></label>
      </div>
    </div>


    <div class="group">
      <p class="gtitle">Actions</p>
      <div class="row" style="flex-direction:column; align-items:flex-start; padding-bottom: 12px; gap:8px;">
        <button class="btn-action" id="btn-screenshot">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>
          Capture Frame
        </button>
        <div style="width:100%; border-top:0.5px solid var(--bd); margin:4px 0;"></div>
        <p style="font-size:11.5px; font-weight:600; color:var(--tx); margin:0;">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="vertical-align:text-top; margin-right:2px"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
          Download Video/Audio
        </p>
        <div style="display:flex; width:100%; gap:6px;">
           <input type="text" id="f-url" autocomplete="off" spellcheck="false" placeholder="Paste TikTok URL…" style="flex:1; padding:8
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

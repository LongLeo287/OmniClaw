---
id: phuc-nt-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:21.153644
---

# KNOWLEDGE EXTRACT: phuc-nt
> **Extracted on:** 2026-03-30 17:51:01
> **Source:** phuc-nt

---

## File: `my-translator.md`
```markdown
# 📦 phuc-nt/my-translator [🔖 PENDING/APPROVE]
🔗 https://github.com/phuc-nt/my-translator


## Meta
- **Stars:** ⭐ 642 | **Forks:** 🍴 240
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Real-time speech translation — macOS & Windows, free TTS, no server, your API keys only

## README (trích đầu)
```
<p align="center">
  <img src="banner.png?v=2" alt="My Translator — Real-time Speech Translation">
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/phuc-nt/my-translator?color=green&label=release" alt="Latest Release">
  <img src="https://img.shields.io/badge/built_with-Tauri-orange?logo=tauri" alt="Built with Tauri">
  <img src="https://img.shields.io/badge/macOS-Apple%20Silicon%20%7C%20Intel-black?logo=apple" alt="macOS">
  <img src="https://img.shields.io/badge/Windows-10%2F11-blue?logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
  <img src="https://img.shields.io/github/stars/phuc-nt/my-translator?style=flat&color=yellow" alt="Stars">
</p>

**My Translator** is a real-time speech translation desktop app built with Tauri. It captures audio directly from your system or microphone, transcribes it, and displays translations in a minimal overlay — with no intermediary server involved.

> 📖 Installation guides: [macOS (EN)](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/scientific/markitdown/INSTALLATION_GUIDE.md) · [macOS (VI)](../../../vault/archives/archive_legacy/my-translator/docs/installation_guide_vi.md) · [Windows (EN)](../../../vault/archives/archive_legacy/my-translator/docs/installation_guide_win.md) · [Windows (VI)](../../../vault/archives/archive_legacy/my-translator/docs/installation_guide_win_vi.md)

---

## How It Works

```
System Audio / Mic → 16kHz PCM → Soniox API (STT + Translation) → Overlay UI
                                                                    ↓ (optional)
                                                            TTS (Edge/Google/ElevenLabs) → 🔊
```

| Feature | Detail |
|---------|--------|
| **Latency** | ~2–3s |
| **Languages** | 70+ (source) → any target, one-way & two-way |
| **Cost** | ~$0.12/hr (Soniox API) |
| **TTS** | 3 providers (Edge free, Google, ElevenLabs) |
| **Platform** | macOS (ARM + Intel) · Windows |
| **Signed** | ✅ macOS signed & notarized |
| **Auto-Update** | ✅ Built-in, check & install from Settings |

---

## Features

### 📖 Dual Panel View

Two display modes:
- **Single** (default) — Translation text only, clean and focused
- **Dual** — Source | Translation side-by-side, each panel scrolls independently

Toggle with the panel button (bottom-right on hover).

### 🔄 Smart Scroll

Auto-scroll only when you're at the bottom. Scroll up to read old content without being yanked back down.

### 🔤 Quick Font Size

A- / A+ floating controls (bottom-right on hover). Font size adjustable up to 140px — great for presentations.

### 🔄 Two-Way Translation

Translate conversations between two languages simultaneously — ideal for bilingual meetings.

- **One-way**: Source language → Target language (e.g., Japanese → Vietnamese)
- **Two-way**: Language A ↔ Language B (e.g., Vietnamese ↔ Japanese) — the app detects who is speaking and translates to the other language automatically

**Setup for video calls** (Zoom, Google Meet, MS Teams):
1. Audio Source: **Both** (System + Mic)
2. Translation Type: **Two-way**
3. Set Language A and Language B

> **Note**: TTS narration is automatically disabled in two-way mode to prevent audio feedback 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


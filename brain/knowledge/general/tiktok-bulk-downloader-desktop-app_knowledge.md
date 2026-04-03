---
id: tiktok-bulk-downloader-desktop-app-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.172833
---

# OmniClaw Knowledge Report: tiktok-bulk-downloader-desktop-app

## Tech Stack
Node.js/NPM

## File Statistics
```json
{
  "": 3,
  ".yaml": 1,
  ".yml": 2,
  ".ts": 21,
  ".mjs": 1,
  ".json": 8,
  ".md": 1,
  ".png": 2,
  ".icns": 1,
  ".sh": 1,
  ".html": 1,
  ".tsx": 9,
  ".css": 1,
  ".svg": 3,
  ".jpg": 1
}
```

## README Snippet
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

**Processed by OmniClaw Automated Intake**
---
id: upamune-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:26.175403
---

# KNOWLEDGE EXTRACT: upamune
> **Extracted on:** 2026-03-30 17:58:06
> **Source:** upamune

---

## File: `notebooklm-podcast-automator.md`
```markdown
# 📦 upamune/notebooklm-podcast-automator [🔖 PENDING/APPROVE]
🔗 https://github.com/upamune/notebooklm-podcast-automator


## Meta
- **Stars:** ⭐ 29 | **Forks:** 🍴 11
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-07
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Python tool to automate Google NotebookLM podcast creation with website/YouTube sources

## README (trích đầu)
```
# NotebookLM Automator

<img src="https://i.gyazo.com/0a9678c0bd80ac9577cbd2289885267d.png" width="500"/>

A Python tool that automates Google NotebookLM operations using Playwright and Chrome DevTools Protocol (CDP).

## Project Purpose and Features

NotebookLM Automator is designed to automate the following operations in Google NotebookLM:

- Creating new notebooks
- Adding website and YouTube URLs as sources to notebooks
- Starting Audio Overview (podcast) generation
- Uploading generated podcasts to Spotify

This tool uses Playwright for browser automation and connects to an existing Chrome browser via Chrome DevTools Protocol (CDP). It is based on [DataNath/notebooklm_source_automation](https://github.com/DataNath/notebooklm_source_automation) with enhancements including improved authentication method, Audio Overview generation capability, Spotify integration, and modernized project structure.

## Spotify Uploader Features

The Spotify Uploader feature allows you to automatically upload your generated podcasts to Spotify. Key features include:

- Automatic Spotify login using existing credentials
- Podcast metadata management (title, description, etc.)
- Cover art upload support
- Episode publishing with proper categorization
- Progress tracking and error handling

To use the Spotify Uploader, you'll need a Spotify for Podcasters account and the necessary permissions to publish podcasts.

## Setup Instructions

### Requirements

- uv
- Python 3.9 or higher
- Chrome or Chromium browser

### Installation

1. **Install `uv`**

   Follow the official installation instructions at [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv) or install with pip:

   ```bash
   pip install uv
   ```

2. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd notebooklm-automator
   ```

3. **Create and activate a virtual environment**

   ```bash
   uv venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\Scripts\activate    # Windows
   ```

4. **Install dependencies and the project in editable mode**

   ```bash
   uv pip install -e .
   ```

### Launching Chrome with Remote Debugging

**IMPORTANT**: Before running the script, you must launch Chrome/Chromium with remote debugging enabled.

**macOS**:
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=./chrome-user-data --window-size=1280,800
```

**Windows**:
```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir=./chrome-user-data --window-size=1280,800
```

**Linux**:
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir=./chrome-user-data --window-size=1280,800
```

The default port is `9222`, but you can use a different port and specify it with the `-p` flag when running the automator.

The `--user-data-dir=./chrome-user-data` parameter creates a separate Chrome profile for this automation, which helps avoid conflicts with your regular
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


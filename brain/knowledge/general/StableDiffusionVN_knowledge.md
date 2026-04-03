---
id: stablediffusionvn-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:16.855583
---

# KNOWLEDGE EXTRACT: StableDiffusionVN
> **Extracted on:** 2026-03-30 17:54:06
> **Source:** StableDiffusionVN

---

## File: `sdvn_apix_python.md`
```markdown
# 📦 StableDiffusionVN/sdvn_apix_python [🔖 PENDING/APPROVE]
🔗 https://github.com/StableDiffusionVN/sdvn_apix_python


## Meta
- **Stars:** ⭐ 32 | **Forks:** 🍴 22
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-02-27
- **Status in AI OS:** 🔖 PENDING/APPROVE

## Description:
apix - SDVN Banana Pro

## README (excerpt)
```
# aPix Image Workspace

## Tiếng Việt (Vietnamese)
### Introduction
aPix Image Workspace is a lightweight Flask interface that helps you create images using the Gemini Image 3 Pro API (Nano Banana Pro). You can send prompts, upload reference documents, and adjust aspect ratio/resolution.

![Preview](./preview.jpeg)

### Creator
- Creator: [Phạm Hưng](https://www.facebook.com/phamhungd/)
- Group: [SDVN - AI Art Community](https://www.facebook.com/groups/stablediffusion.vn/)
- Website: [sdvn.vn](https://www.sdvn.vn)
- Donate: [sdvn.vn/donate](https://stablediffusion.vn/donate/)

### Quick launch with `run_app`
1. Double-click `run_app.command` on macOS, `run_app.sh` on Linux, or `run_app.bat` on Windows to automatically find Python, create `.venv`, install `requirements.txt` and start `app.py`.
2. Open `http://127.0.0.1:8888`, enter prompt/options and press Generate.
3. New images are in `static/generated/`; `/gallery` shows history.

### Usage
1. Set environment variable `GOOGLE_API_KEY` with your Google GenAI API key or enter directly in the interface.
2. Open browser to `http://127.0.0.1:8888`, enter prompt, select options and press Generate.
3. Images: `static/generated` saves latest content, while `/gallery` returns URLs for history.

### Special syntax
The app supports placeholder syntax for creating multiple image variants or flexible content replacement:

*   **Placeholder:** Use `{text}` or `[text]` in prompt. Example: `A photo of a {animal} in the style of {style}`.
*   **Note field:** Content in Note field replaces placeholders:
    *   **Single replacement:** If Note is `cat`, prompt becomes `A photo of a cat...`.
    *   **Queue:** If Note contains `|` (Example: `cat|dog|bird`), app automatically generates 3 images sequentially with `cat`, `dog`, and `bird`.
    *   **Multi-line:** If Note has multiple lines, each line corresponds to one generation.
    *   **Default:** If Note is empty, placeholder remains or uses default if available (Example: `{cat|dog}` generates 2 images if Note empty).

```

---

*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

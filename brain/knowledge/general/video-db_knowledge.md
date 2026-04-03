---
id: video-db-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:41.089601
---

# KNOWLEDGE EXTRACT: video-db
> **Extracted on:** 2026-03-30 17:58:08
> **Source:** video-db

---

## File: `skills.md`
```markdown
# 📦 video-db/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/video-db/skills
🌐 https://docs.videodb.io

## Meta
- **Stars:** ⭐ 49 | **Forks:** 🍴 2
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Server-side video workflows for agents: ingest, understand, search, edit, stream.

## README (trích đầu)
```

[![GitHub stars](https://img.shields.io/github/stars/video-db/skills.svg?style=for-the-badge)](https://github.com/video-db/skills/stargazers)
[![Issues](https://img.shields.io/github/issues/video-db/videodb-python.svg?style=for-the-badge)](https://github.com/video-db/videodb-python/issues)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fvideodb.io%2F&style=for-the-badge&label=videodb.io)](https://videodb.io)

<div align="center">

<img width="1200" height="372" alt="banner" src="https://github.com/user-attachments/assets/fdbf3879-dcd6-443c-93e0-9a7e1bfdfa90" />


**The only perception skill your agent needs.**

Works with **Claude Code**, **Cursor**, **Copilot**, and other AI agents

**[📚 Explore the Docs](https://docs.videodb.io)** &emsp; **[ Watch Demos ](https://www.youtube.com/playlist?list=PLhxAMFLSSK01IONxpqtEqj0UUQyFswiaR)**

</div>



## Why add this Skill

This skill gives your agent one consistent interface to:

- **See**: Realtime desktop screen, mic and system audio, RTSP streams, ingest files, URLs, YouTube.

- **Understand**: Visual understanding, transcribe, index and search moments with playble clips

- **Act**: Stream results, trigger alerts on live feeds, edit timelines, generate subtitles and overlays, export clips.



## What it does

VideoDB Skills lets your AI coding agent run end to end, server-side video workflows in real time and batch:

- Capture desktop screen, mic, and system audio for real time processing.
- Upload and process RTSP streams, videos from YouTube, URLs, and local files.
- Create realtime context of visual and spoken information. 
- Index and search spoken words and visual scenes anytime.
- Generate transcripts, subtitles, and AI media.
- Edit clips, overlays, and exports server side.

Return playable HLS links for anything you build.


## Get Started

Get started in two quick steps. Open your AI coding agent (Requires **Python 3.9+**) and follow along.


### Step 1: Install the skill

```bash
npx skills add video-db/skills
```

Or install with Claude Code plugin:

```bash
/plugin marketplace add video-db/skills
/plugin install videodb@videodb-skills
```

### Step 2: Setup

```
/videodb setup
```

The agent will guide setup for your [VideoDB API key](https://console.videodb.io) ($20 free credits, no credit card required), install the SDK, and verify the connection.


> For Cursor, Copilot, and other agents, ask your agent to **"setup videodb"**

Set your API key using either method:

```bash
# Recommended: Export in terminal
export VIDEO_DB_API_KEY=sk-xxx

# Or add to your project's .env file
VIDEO_DB_API_KEY=sk-xxx
```

---
## Give your agent instructions

Ask your agent to run instructions like these. The skill loads automatically.

- "Upload https://www.youtube.com/watch?v=MnrJzXM7a6o and give me a sharable stream link"
- "Take clips from 10s-30s and 45s-60s and compile them"
- "Generate a background music, and add to this Clip"
- "Add subtitles to original video with white text on black 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


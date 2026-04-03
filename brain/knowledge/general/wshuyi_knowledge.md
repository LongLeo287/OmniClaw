---
id: wshuyi-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:47.058995
---

# KNOWLEDGE EXTRACT: wshuyi
> **Extracted on:** 2026-03-30 18:01:18
> **Source:** wshuyi

---

## File: `x-article-publisher-skill.md`
```markdown
# 📦 wshuyi/x-article-publisher-skill [🔖 PENDING/APPROVE]
🔗 https://github.com/wshuyi/x-article-publisher-skill


## Meta
- **Stars:** ⭐ 682 | **Forks:** 🍴 69
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Claude Code skill for publishing Markdown articles to X (Twitter) Articles

## README (trích đầu)
```
# X Article Publisher Skill

[English](README.md) | [中文](README_CN.md)

> Publish Markdown articles to X (Twitter) Articles with one command. Say goodbye to tedious rich text editing.

**v1.2.0** — Now with divider support, table-to-image, Mermaid support, and cross-platform clipboard

---

## The Problem

If you're used to writing in Markdown, publishing to X Articles is a **painful process**:

| Pain Point | Description |
|------------|-------------|
| **Format Loss** | Copy from Markdown editor → Paste to X → All formatting gone |
| **Manual Formatting** | Set each H2, bold, link manually — 15-20 min per article |
| **Tedious Image Upload** | 5 clicks per image: Add media → Media → Add photo → Select → Wait |
| **Position Errors** | Hard to remember where each image should go |

### Time Comparison

| Task | Manual | With This Skill |
|------|--------|-----------------|
| Format conversion | 15-20 min | 0 (automatic) |
| Cover image | 1-2 min | 10 sec |
| 5 content images | 5-10 min | 1 min |
| **Total** | **20-30 min** | **2-3 min** |

**10x efficiency improvement**

---

## The Solution

This skill automates the entire publishing workflow:

```
Markdown File
     ↓ Python parsing
Structured Data (title, images with block_index, HTML)
     ↓ Playwright MCP
X Articles Editor (browser automation)
     ↓
Draft Saved (never auto-publishes)
```

### Key Features

- **Rich Text Paste**: Convert Markdown to HTML, paste via clipboard — all formatting preserved
- **Block-Index Positioning** (v1.1): Precise image placement using element indices, not text matching
- **Reverse Insertion**: Insert images from highest to lowest index to avoid position shifts
- **Smart Wait Strategy**: Conditions return immediately when met, no wasted wait time
- **Safe by Design**: Only saves as draft, never publishes automatically

---

## What's New in v1.1.0

| Feature | Before | After |
|---------|--------|-------|
| Image positioning | Text matching (fragile) | Block index (precise) |
| Insertion order | Sequential | Reverse (high→low) |
| Wait behavior | Fixed delay | Immediate return on condition |

### Why Block-Index?

Previously, images were positioned by matching surrounding text — this failed when:
- Multiple paragraphs had similar content
- Text was too short to be unique

Now, each image has a `block_index` indicating exactly which block element it follows. This is deterministic and reliable.

---

## Requirements

| Requirement | Details |
|-------------|---------|
| Claude Code | [claude.ai/code](https://claude.ai/code) |
| Playwright MCP | Browser automation |
| X Premium Plus | Required for Articles feature |
| Python 3.9+ | With dependencies below |
| OS | macOS or Windows |

```bash
# macOS
pip install Pillow pyobjc-framework-Cocoa

# Windows
pip install Pillow pywin32 clip-util

# For Mermaid diagrams (optional)
npm install -g @mermaid-js/mermaid-cli
```

---

## Installation

### Method 1: Git Clone (Recommended)

```bash
git clone https://github.com/
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


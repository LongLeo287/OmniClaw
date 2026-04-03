---
id: fal-ai-community-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:23.351296
---

# KNOWLEDGE EXTRACT: fal-ai-community
> **Extracted on:** 2026-03-30 17:36:47
> **Source:** fal-ai-community

---

## File: `skills.md`
```markdown
# 📦 fal-ai-community/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/fal-ai-community/skills


## Meta
- **Stars:** ⭐ 42 | **Forks:** 🍴 6
- **Language:** Shell | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# fal.ai Skills

Agent skills for [fal.ai](https://fal.ai) — ready-to-use bash scripts that let AI agents generate images, videos, audio, 3D models, and more.

Compatible with [Claude.ai Projects](https://claude.ai), [Claude Code](https://claude.ai/claude-code), and any agent platform that supports the community skills format.

## Skills

### Core

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-generate](skills/claude.ai/fal-generate)** | Generate images and videos with queue support | `generate.sh`, `upload.sh`, `search-models.sh`, `get-schema.sh` |
| **[fal-image-edit](skills/claude.ai/fal-image-edit)** | Edit images — style transfer, object removal, background change, inpainting | `edit-image.sh` |
| **[fal-audio](skills/claude.ai/fal-audio)** | Text-to-speech and speech-to-text | `text-to-speech.sh`, `speech-to-text.sh` |
| **[fal-upscale](skills/claude.ai/fal-upscale)** | Upscale and enhance image resolution | `upscale.sh` |

### Specialized Models

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-kling-o3](skills/claude.ai/fal-kling-o3)** | Kling O3 — highest quality photorealistic images and video editing | `kling-generate.sh`, `kling-video.sh` |
| **[fal-realtime](skills/claude.ai/fal-realtime)** | Real-time/streaming generation (~0.3s per image) | `realtime.sh` |

### Video & Animation

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-video-edit](skills/claude.ai/fal-video-edit)** | Edit videos — remix, upscale, remove background, add audio | `edit-video.sh`, `video-audio.sh` |
| **[fal-lip-sync](skills/claude.ai/fal-lip-sync)** | Talking head, lip sync, live portrait | `talking-head.sh`, `lip-sync.sh` |

### Creative & Production

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-3d](skills/claude.ai/fal-3d)** | Text/image to 3D model generation | `generate-3d.sh` |
| **[fal-vision](skills/claude.ai/fal-vision)** | Image analysis — segment, detect, OCR, describe | `analyze.sh` |
| **[fal-restore](skills/claude.ai/fal-restore)** | Restore image quality — deblur, denoise, fix faces | `restore.sh` |
| **[fal-tryon](skills/claude.ai/fal-tryon)** | Virtual clothing try-on | `tryon.sh` |
| **[fal-train](skills/claude.ai/fal-train)** | Train custom LoRA models | `train.sh` |

### Platform & Utilities

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-platform](skills/claude.ai/fal-platform)** | Pricing, usage tracking, cost estimation, API key setup | `pricing.sh`, `usage.sh`, `estimate-cost.sh`, `setup.sh`, `requests.sh` |
| **[fal-workflow](skills/claude.ai/fal-workflow)** | Create multi-step model pipelines | `create-workflow.sh` |

## Setup

### 1. Get your API key

Sign up at [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys).

### 2. Set the key

```bash
export FAL_KEY=your_key_here
```

Or use the built-in setup:

```bash
bash scripts/generate.sh --add-fal-key
```

### 3. Use with Claude.ai

Upl
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


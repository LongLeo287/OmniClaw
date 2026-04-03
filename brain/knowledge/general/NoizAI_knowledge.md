---
id: noizai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:12.103272
---

# KNOWLEDGE EXTRACT: NoizAI
> **Extracted on:** 2026-03-30 17:49:14
> **Source:** NoizAI

---

## File: `skills.md`
```markdown
# 📦 NoizAI/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/NoizAI/skills


## Meta
- **Stars:** ⭐ 415 | **Forks:** 🍴 57
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Allow your 🦞 bot to Shout, Speak, with "human" vibe

## README (trích đầu)
```
# Unmute your intelligent bot
<img width="1760" height="608" alt="banner" src="https://github.com/user-attachments/assets/79efa5ae-e056-426c-ae67-362dd0f44963" />

English | [简体中文](./README.zh-CN.md)

Central repository for managing Skills to "human" vibe-talking.

## Install with `npx skills add`

```bash
# List skills from GitHub repository
npx skills add NoizAI/skills --list --full-depth

# Install a specific skill from GitHub repository
npx skills add NoizAI/skills --full-depth --skill tts -y

# Install from GitHub repository
npx skills add NoizAI/skills

# Local development (run in this repo directory)
npx skills add . --list --full-depth
```

## Highlights

- 🔒 Secure and local-first: run skills on your own machine to keep sensitive text and assets localized.
- 🧠 Character-style controls: tune fillers, emotion, and speaking presets for companion-like output.
- 🎙️ Production-ready voice: from quick TTS generation to timeline-aligned rendering.
- 📤 One-command delivery to chat platforms: generate speech and send it as a native voice message to Feishu, Telegram, or Discord — zero extra code.

## Available skills

| Name | Description | Documentation | Run command |
|------|-------------|---------------|-------------|
| tts | Convert text into speech with Kokoro or Noiz: simple mode, timeline-aligned rendering, precise duration control, and reference-audio voice cloning. | [SKILL.md](../bmad_repo/SKILL.md) | `npx skills add NoizAI/skills --full-depth --skill tts -y` |
| chat-with-anyone | Chat with any real person or fictional character in their own voice by automatically finding their speech online, extracting a clean reference sample, and generating audio replies. | [SKILL.md](../bmad_repo/SKILL.md) | `npx skills add NoizAI/skills --full-depth --skill chat-with-anyone -y` |
| characteristic-voice | Make generated speech feel companion-like with fillers, emotional tuning, and preset speaking styles. | [SKILL.md](../bmad_repo/SKILL.md) | `npx skills add NoizAI/skills --full-depth --skill characteristic-voice -y` |
| video-translation | Translate and dub videos from one language to another, replacing the original audio with TTS while keeping the video intact. | [SKILL.md](../bmad_repo/SKILL.md) | `npx skills add NoizAI/skills --full-depth --skill video-translation -y` |
| daily-news-caster | Fetch the latest real-time news and automatically generate a dual-host conversational podcast with audio. | [SKILL.md](../bmad_repo/SKILL.md) | `npx skills add NoizAI/skills --full-depth --skill daily-news-caster -y` |

## Quick Verify

For example, characteristic-voice
```bash
bash skills/characteristic-voice/scripts/speak.sh \
  --preset comfort -t "Hmm... I'm right here." -o comfort.wav
```

## English Audio Demos

Sample outputs for quick listening (MP4 for inline playback):

- Breaking news style


https://github.com/user-attachments/assets/e1e75371-49e2-4858-9993-428d999c3723




- Mindful calm 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


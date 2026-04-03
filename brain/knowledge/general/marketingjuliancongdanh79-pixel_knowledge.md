---
id: marketingjuliancongdanh79-pixel-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:06.654414
---

# KNOWLEDGE EXTRACT: marketingjuliancongdanh79-pixel
> **Extracted on:** 2026-03-30 17:42:05
> **Source:** marketingjuliancongdanh79-pixel

---

## File: `claude-code-ultimate-guide.md`
```markdown
# 📦 marketingjuliancongdanh79-pixel/claude-code-ultimate-guide [🔖 PENDING/APPROVE]
🔗 https://github.com/marketingjuliancongdanh79-pixel/claude-code-ultimate-guide
🌐 https://cc.bruniaux.com/

## Meta
- **Stars:** ⭐ 55 | **Forks:** 🍴 19
- **Language:** N/A | **License:** CC-BY-SA-4.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A tremendous feat of documentation, this guide covers Claude Code from beginner to power user, with production-ready templates for Claude Code features, guides on agentic workflows, and a lot of great learning materials, including quizzes and a handy "cheatsheet". Whether it's the "ultimate" guide to Claude Code will be up to the reader :)

## README (trích đầu)
```
# Claude Code Ultimate Guide

<p align="center">
  <a href="https://florianbruniaux.github.io/claude-code-ultimate-guide-landing/"><img src="https://img.shields.io/badge/🌐_Interactive_Guide-Visit_Website-ff6b35?style=for-the-badge&logoColor=white" alt="Website"/></a>
</p>

<p align="center">
  <a href="https://github.com/FlorianBruniaux/claude-code-ultimate-guide/stargazers"><img src="https://img.shields.io/github/stars/FlorianBruniaux/claude-code-ultimate-guide?style=for-the-badge" alt="Stars"/></a>
  <a href="./CHANGELOG.md"><img src="https://img.shields.io/badge/Updated-Mar_9,_2026_·_v3.32.2-brightgreen?style=for-the-badge" alt="Last Update"/></a>
  <a href="./quiz/"><img src="https://img.shields.io/badge/Quiz-271_questions-orange?style=for-the-badge" alt="Quiz"/></a>
  <a href="./examples/"><img src="https://img.shields.io/badge/Templates-222-green?style=for-the-badge" alt="Templates"/></a>
  <a href="./guide/security-hardening.md"><img src="https://img.shields.io/badge/🛡️_Threat_DB-15_vulnerabilities_·_655_malicious_skills-red?style=for-the-badge" alt="Threat Database"/></a>
  <a href="./mcp-server/"><img src="https://img.shields.io/badge/MCP_Server-npx_ready-blueviolet?style=for-the-badge" alt="MCP Server"/></a>
</p>

<p align="center">
  <a href="https://github.com/hesreallyhim/awesome-claude-code"><img src="https://awesome.re/mentioned-badge-flat.svg" alt="Mentioned in Awesome Claude Code"/></a>
  <a href="https://creativecommons.org/licenses/by-sa/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY--SA%204.0-blue.svg" alt="License: CC BY-SA 4.0"/></a>
  <a href="https://skills.palebluedot.live/owner/FlorianBruniaux"><img src="https://img.shields.io/badge/SkillHub-9_skills-8b5cf6.svg" alt="SkillHub Skills"/></a>
  <a href="https://zread.ai/FlorianBruniaux/claude-code-ultimate-guide"><img src="https://img.shields.io/badge/Ask_Zread-_.svg?style=flat&color=00b0aa&labelColor=000000&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTQuOTYxNTYgMS42MDAxSDIuMjQxNTZDMS44ODgxIDEuNjAwMSAxLjYwMTU2IDEuODg2NjQgMS42MDE1NiAyLjI0MDFWNC45NjAxQzEuNjAxNTYgNS4zMTM1NiAxLjg4ODEgNS42MDAxIDIuMjQxNTYgNS42MDAxSDQuOTYxNTZDNS4zMTUwMiA1LjYwMDEgNS42MDE1NiA1LjMxMzU2IDUuNjAxNTYgNC45NjAxVjIuMjQwMUM1LjYwMTU2IDEuODg2NjQgNS4zMTUwMiAxLjYwMDEgNC45NjE1NiAxLjYwMDFaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik00Ljk2MTU2IDEwLjM5OTlIMi4yNDE1NkMxLjg4ODEgMTAuMzk5OSAxLjYwMTU2IDEwLjY4NjQgMS42MDE1NiAxMS4wMzk5VjEzLjc1OTlDMS42MDE1NiAxNC4xMTM0IDEuODg4MSAxNC4zOTk5IDIuMjQxNTYgMTQuMzk5OUg0Ljk2MTU2QzUuMzE1MDIgMTQuMzk5OSA1LjYwMTU2IDE0LjExMzQgNS42MDE1NiAxMy43NTk5VjExLjAzOTlDNS42MDE1NiAxMC42ODY0IDUuMzE1MDIgMTAuMzk5OSA0Ljk2MTU2IDEwLjM5OTlaIiBmaWxsPSIjZmZmIi8%2BCjxwYXRoIGQ9Ik0xMy43NTg0IDEuNjAwMUgxMS4wMzg0QzEwLjY4NSAxLjYwMDEgMTAuMzk4NCAxLjg4NjY0IDEwLjM5ODQgMi4yNDAxVjQuOTYwMUMxMC4zOTg0IDUuMzEzNTYgMTAuNjg1IDUuNjAwMSAxMS4wMzg0IDUuNjAwMUgxMy43NTg0QzE0LjExMTkgNS42MDAxIDE0LjM
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `skill-generator.md`
```markdown
# 📦 marketingjuliancongdanh79-pixel/skill-generator [🔖 PENDING/APPROVE]
🔗 https://github.com/marketingjuliancongdanh79-pixel/skill-generator


## Meta
- **Stars:** ⭐ 311 | **Forks:** 🍴 83
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Bộ công cụ tạo AI Skill từ ý tưởng — Dành cho Antigravity, Claude Code, Cursor, Windsurf. Đánh giá 100/100 S-tier. 

## README (trích đầu)
```
<p align="center">
  <h1 align="center">🧠 Skill Generator Ultra</h1>
  <p align="center">
    <strong>The most comprehensive AI Skill creation toolkit on the market.</strong><br/>
    <em>Bộ công cụ tạo AI Skill toàn diện nhất trên thị trường.</em>
  </p>
  <a href="https://unikorn.vn/p/skillgenerator?ref=embed" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/skillgenerator?theme=light" alt="Skill Generator trên Unikorn.vn" style="width: 256px; height: 64px;" width="256" height="64" /></a>
<a href="https://unikorn.vn/p/skillgenerator?ref=embed" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/skillgenerator/rank?theme=light&type=daily" alt="Skill Generator - Hàng ngày" style="width: 250px; height: 64px;" width="250" height="64" /></a>
<a href="https://unikorn.vn/p/skillgenerator?ref=embed" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/skillgenerator/rank?theme=light&type=weekly" alt="Skill Generator - Hàng tuần" style="width: 250px; height: 64px;" width="250" height="64" /></a>
<a href="https://unikorn.vn/p/skillgenerator?ref=embed" target="_blank"><img src="https://unikorn.vn/api/widgets/badge/skillgenerator/rank?theme=light&type=monthly" alt="Skill Generator - Hàng tháng" style="width: 250px; height: 64px;" width="250" height="64" /></a>
  <p align="center">
    <img src="https://img.shields.io/badge/version-1.1.0-blue" alt="version"/>
    <img src="https://img.shields.io/badge/files-56-green" alt="files"/>
    <img src="https://img.shields.io/badge/scripts-9-orange" alt="scripts"/>
    <img src="https://img.shields.io/badge/platforms-7-purple" alt="platforms"/>
    <img src="https://img.shields.io/badge/tests-60%2F60-brightgreen" alt="tests"/>
    <img src="https://img.shields.io/badge/resources-193KB-yellow" alt="resources"/>
  </p>
</p>

---

## 🌍 Language / Ngôn ngữ

- [English](#english)
- [Tiếng Việt](#-phiên-bản-tiếng-việt-vietnamese-version)

---

# English

## 📋 Table of Contents

- [Introduction](#introduction)
- [Key Features](#-key-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Scripts & Tools](#-scripts--tools-9-utilities)
- [Slash Commands](#-slash-commands-8-commands)
- [Project Structure](#-project-structure)
- [Platform Compatibility](#-platform-compatibility)
- [Evaluation System](#-evaluation-system)
- [Documentation](#-documentation)
- [FAQ](#-faq)
- [Changelog](#-changelog-en)
- [Contributing](#-contributing)
- [License](#-license-en)

---

## Introduction

**Skill Creator Ultra** is a specialized AI Skill for **Google Antigravity** (and 7 other platforms). It helps you **create production-quality AI Skills** through an **8-phase pipeline** — even if you **DON'T know** what a skill is, what YAML is, or how to write SKILL.md.

**You only need:**

- ✅ An idea about what you want to automate
- ✅ A workflow / process / logic in your head

**AI handles the rest:**

- 🎤 Smart interview with 5 extraction techniques + Quick Mode
- 🔍 Auto-detect complexity → choose the 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


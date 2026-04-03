---
id: dream-num-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:20.923092
---

# KNOWLEDGE EXTRACT: dream-num
> **Extracted on:** 2026-03-30 17:36:10
> **Source:** dream-num

---

## File: `univer-mcp.md`
```markdown
# 📦 dream-num/univer-mcp [🔖 PENDING/APPROVE]
🔗 https://github.com/dream-num/univer-mcp
🌐 https://console.univer.ai

## Meta
- **Stars:** ⭐ 33 | **Forks:** 🍴 1
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
AI-powered spreadsheet automation through Model Context Protocol (MCP) server for Univer

## README (trích đầu)
```
# Univer MCP

> 🚀 AI-powered spreadsheet automation through Model Context Protocol (MCP)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-dream--num%2Funiver--mcp-blue)](https://github.com/dream-num/univer-mcp)

## Overview

Univer MCP is a Model Context Protocol (MCP) server that enables AI applications to interact with and automate spreadsheet operations using the powerful [Univer](https://github.com/dream-num/univer) framework. It bridges the gap between AI language models and spreadsheet functionality, allowing for intelligent spreadsheets processing and automation.

> ⚠️ **Early Stage**: Univer MCP is currently in early development. We welcome feedback, suggestions, and collaboration from the community to help shape its future direction.

## Key Features

- **📊 Spreadsheet Operations**: Full support for creating, editing, and manipulating spreadsheets
- **🔧 Extensible Architecture**: Built on Univer's plugin system for custom functionality
- **⚡ High Performance**: Leverages Univer's optimized rendering and calculation engines
- **📦 Advanced Features**: Formulas, conditional formatting, data validation, and more
- **🤖 AI Integration**: Seamless integration with MCP-compatible AI applications
- **📈 Chart Support[WIP]**: Creating and updating charts in spreadsheets
- **🔗 Pivot Table[WIP]**: Creating and updating pivot tables in spreadsheets
- **🌐 Cross-Platform[WIP]**: Works across web browsers and Node.js environments
- **🔄 Real-time Collaboration[WIP]**: Support for collaborative editing and real-time updates


https://github.com/user-attachments/assets/c77c7927-335e-47fd-9cf7-852d4880d4b9



## Requirements

**Multi-modal Model required**: Some Univer mcp tools support returning images for better understanding, so the model you choose should ideally support multimodality.

> Plain text mode is currently experimental(NOT supported yet); it may be supported in the future. Any suggestions in this regard are very welcome.


## How It Works

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/58626cac-831d-4aa0-9c44-b3d2ff5262d9" />


- MCP host: such as cursor, claude code, or the agents you built.  
- Univer MCP Server: provides the endpoint for univer mcp, which proxies tool calls to the univer instance for execution.
- mcp-bridge: this is a [univer plugin](https://docs.univer.ai/guides/recipes/architecture/univer#plugins) used to handle various spreadsheet commands in mcp.
- univer instance: the runtime environment of univer (spreadsheet).


## Quick Start

### Get API Key
First, you need to get an API key from the [API Keys page](https://console.univer.ai/apikeys). This key will be used to authenticate your MCP server connection.

### Start Univer Instance

Before you talk to LLM, you need to launch a univer instance, which is a spreadsheet runtime where you will see the contents of the spreadsheet and how it is being operated.

The
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `univer.md`
```markdown
# 📦 dream-num/univer [🔖 PENDING/APPROVE]
🔗 https://github.com/dream-num/univer
🌐 https://univer.ai

## Meta
- **Stars:** ⭐ 12650 | **Forks:** 🍴 1132
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Build AI-native spreadsheets. Univer is a full-stack framework for creating and editing spreadsheets on both web and server. With Univer Platform, Univer Spreadsheets is driven directly through natural language.

## README (trích đầu)
```
<div align="center">

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./brain/knowledge/docs_legacy/img/banner-light.png">
    <img src="./brain/knowledge/docs_legacy/img/banner-dark.png" alt="Univer" width="400" />
</picture>

An Isomorphic Full-Stack Framework for Creating and Editing Spreadsheets Across Web and Server.<br />
**Extensible. High-performance. Embedded to your application.**

**English** | [简体中文][readme-zh-link] | [日本語][readme-ja-link] | [Español][readme-es-link] <br />
[Official Site][official-site-link] | [Documentation][documentation-link] | [Online Playground][playground-link] | [Blog][blog-link]

[![][github-license-shield]][github-license-link]
[![][github-actions-shield]][github-actions-link]
[![][github-stars-shield]][github-stars-link]
[![][github-contributors-shield]][github-contributors-link] <br />
[![][github-forks-shield]][github-forks-link]
[![][github-issues-shield]][github-issues-link]
[![][codecov-shield]][codecov-link]
[![][codefactor-shield]][codefactor-link]
[![][discord-shield]][discord-link]

[![Trendshift][github-trending-shield]][github-trending-url]

</div>

## Use [Univer Platform](https://github.com/dream-num/univer-mcp) to drive Univer Spreadsheets with natural language and build AI-native spreadsheets.

https://github.com/user-attachments/assets/7429bd5f-d769-4057-9e67-353337531024

<details open>
<summary>
<strong>Table of contents</strong>
</summary>

- [🌈 Highlights](#-highlights)
- [✨ Features](#-features)
    - [📊 Univer Sheet](#-univer-sheet)
    - [📝 Univer Doc](#-univer-doc-under-development)
    - [📽️ Univer Slide](#%EF%B8%8F-univer-slide-under-development)
- [🌐 Internationalization](#-internationalization)
- [👾 Showcase](#-showcase)<!-- - [📦 Ecosystem](#-ecosystem) -->
- [💬 Community](#-community)
- [🤝 Contribution](#-contribution)
- [❤️ Sponsor](#%EF%B8%8F-sponsors)
- [📄 License](#-license)

</details>

## 🌈 Highlights

- 📈 Univer is designed to support **spreadsheets**, **documents** and **presentation**.
- 🧙‍♀️ Univer is **isomorphic**. It can run both on browsers and Node.js (in the future, mobile devices as well), with the same API.
- ⚙️ Univer is easily **embeddable**, allowing seamless integration into your applications.
- 🎇 Univer is **powerful**, offering a wide range of features including **formulas**, **conditional formatting**, **data validation**, **filtering**, **collaborative editing**, **printing**, **import & export** and more features on the horizon.
- 🔌 Univer is **highly extensible**, thanks to its *plug-in architecture* that makes it a delight for developers to implement their unique requirements on the top of Univer.
- 💄 Univer is **highly customizable**, allowing you to personalize its appearance using *themes*. It also provides support for internationalization (i18n).
- 🥤 Univer is **easy to work with**. The *Presets* & *Facade API* make it easy to hands on.
- ⚡ Univer in **performant**.
  - ✏️ Univer boasts an efficient *rendering engine* based on canvas, capable of rendering various document 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


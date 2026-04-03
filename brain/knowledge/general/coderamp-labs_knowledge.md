---
id: coderamp-labs-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:08.197432
---

# KNOWLEDGE EXTRACT: coderamp-labs
> **Extracted on:** 2026-03-30 17:34:53
> **Source:** coderamp-labs

---

## File: `gitingest-extension.md`
```markdown
# 📦 coderamp-labs/gitingest-extension [🔖 PENDING/APPROVE]
🔗 https://github.com/coderamp-labs/gitingest-extension
🌐 https://chromewebstore.google.com/detail/adfjahbijlkjfoicpjkhjicpjpjfaood

## Meta
- **Stars:** ⭐ 209 | **Forks:** 🍴 32
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
✨ A extension can help you open git ingest to turn any git repository into a prompt-friendly text ingest for LLMs.

## README (trích đầu)
```
![Prompt-friendly codebase
Turn any GitHub repository into a simple text ingest of its codebase.
This is useful for feeding a codebase into any LLM.](https://github.com/user-attachments/assets/e3b87d4f-5617-446f-90b3-035d5f7d5e1e)

<img width="64" height="64" src="https://github.com/user-attachments/assets/e6a0c74d-0548-4c76-8536-c613ded73430" alt="GitIngest Icon"><h1>GitIngest Extension 🔍</h1>
Turn any Git repository into a prompt-friendly text ingest for LLMs.

<a href="https://chromewebstore.google.com/detail/adfjahbijlkjfoicpjkhjicpjpjfaood" target="_blank" title="Get GitIngest Extension from Chrome Web Store"><img height="48" src="https://github.com/user-attachments/assets/20a6e44b-fd46-4e6c-8ea6-aad436035753" alt="Available in the Chrome Web Store" /></a>
<a href="https://addons.mozilla.org/firefox/addon/gitingest/" target="_blank" title="Get GitIngest Extension from Firefox Add-ons"><img height="48" src="https://github.com/user-attachments/assets/c0e99e6b-97cf-4af2-9737-099db7d3538b" alt="Get The Add-on for Firefox" /></a>
<a href="https://microsoftedge.microsoft.com/addons/detail/nfobhllgcekbmpifkjlopfdfdmljmipf" target="_blank" title="Get GitIngest Extension from Firefox Add-ons"><img height="48" src="https://github.com/user-attachments/assets/204157eb-4cae-4c0e-b2cb-db514419fd9e" alt="Get from the Edge Add-ons" /></a>

This extension is part of the GitIngest ecosystem. See [GitIngest.com](https://gitingest.com) or [cyclotruc/gitingest](https://github.com/cyclotruc/gitingest) for more information.

## ✨ Features

- 🚀 One-click access to GitIngest services to get a text ingest
- 📚 Prompt-friendly codebase ingestion
- 📝 Optimized output format for LLM prompts
- 🔍 Statistics about:
  - File and directory structure
  - Size of the extract
  - Token count  
- 🔒 Privacy-first, zero data collection (for the extension itself)
- 🤖 Open source, community-driven

## 📸 Screenshots

https://github.com/user-attachments/assets/fb831553-c55a-43e7-af91-7636e9084ae8
<!-- ![Screenshot 0](https://github.com/user-attachments/assets/cfe4b346-2c02-4aef-895d-39847938423f) -->
| ![Screenshot 1](https://github.com/user-attachments/assets/3a9ce50f-1cb1-4a02-9b45-ed0109c3e9f5) | ![Screenshot 2](https://github.com/user-attachments/assets/e723c81f-5b24-41c9-82c0-4b93293427e8) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

## 🛠️ Using
- [WXT](https://github.com/wxt-dev/wxt)
- [TailwindCSS](https://tailwindcss.com/)

## 🔒 Privacy Policy
> This privacy policy is for the extension only.
[Privacy Policy (26 December 2024)](PRIVACY.md)

## 🔧 Development

### Clone the repository
```bash
git clone https://github.com/lcandy2/gitingest-extension.git
```

### Install dependencies
```bash
pnpm install
```

### Run the development server
```bash
pnpm dev
```

### Build the extension
```bash
pnpm build
```

## 📄 License
[MIT](LICENSE.md)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `gitingest.md`
```markdown
# 📦 coderamp-labs/gitingest [🔖 PENDING/APPROVE]
🔗 https://github.com/coderamp-labs/gitingest
🌐 https://gitingest.com

## Meta
- **Stars:** ⭐ 14231 | **Forks:** 🍴 1046
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Replace 'hub' with 'ingest' in any GitHub URL to get a prompt-friendly extract of a codebase 

## README (trích đầu)
```
# Gitingest

[![Screenshot of Gitingest front page](https://raw.githubusercontent.com/coderamp-labs/gitingest/refs/heads/main/brain/knowledge/docs_legacy/frontpage.png)](https://gitingest.com)

<!-- Badges -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <!-- row 1 — install & compat -->
  <a href="https://pypi.org/project/gitingest"><img src="https://img.shields.io/pypi/v/gitingest.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/gitingest"><img src="https://img.shields.io/pypi/pyversions/gitingest.svg" alt="Python Versions"></a>
  <br>
  <!-- row 2 — quality & community -->
  <a href="https://github.com/coderamp-labs/gitingest/actions/workflows/ci.yml?query=branch%3Amain"><img src="https://github.com/coderamp-labs/gitingest/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>

  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/coderamp-labs/gitingest"><img src="https://api.scorecard.dev/projects/github.com/coderamp-labs/gitingest/badge" alt="OpenSSF Scorecard"></a>
  <br>
  <a href="https://github.com/coderamp-labs/gitingest/blob/main/LICENSE"><img src="https://img.shields.io/github/license/coderamp-labs/gitingest.svg" alt="License"></a>
  <a href="https://pepy.tech/project/gitingest"><img src="https://pepy.tech/badge/gitingest" alt="Downloads"></a>
  <a href="https://github.com/coderamp-labs/gitingest"><img src="https://img.shields.io/github/stars/coderamp-labs/gitingest" alt="GitHub Stars"></a>
  <a href="https://discord.com/invite/zerRaGK9EC"><img src="https://img.shields.io/badge/Discord-Join_chat-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
  <br>
  <a href="https://trendshift.io/repositories/13519"><img src="https://trendshift.io/api/badge/repositories/13519" alt="Trendshift" height="50"></a>
</p>
<!-- markdownlint-enable MD033 -->

Turn any Git repository into a prompt-friendly text ingest for LLMs.

You can also replace `hub` with `ingest` in any GitHub URL to access the corresponding digest.

<!-- Extensions -->
[gitingest.com](https://gitingest.com) · [Chrome Extension](https://chromewebstore.google.com/detail/adfjahbijlkjfoicpjkhjicpjpjfaood) · [Firefox Add-on](https://addons.mozilla.org/firefox/addon/gitingest)

<!-- Languages -->
[Deutsch](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=de) |
[Español](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=es) |
[Français](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=fr) |
[日本語](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=ja) |
[한국어](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=ko) |
[Português](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=pt) |
[Русский](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=ru) |
[中文](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=zh)

## 🚀 Features

- **Easy code context**
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


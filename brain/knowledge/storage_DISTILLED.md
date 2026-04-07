---
id: storage
type: knowledge
owner: OA_Triage
---
# storage
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: vault\ARCHIVE\ai_tagger_module\index.js
```js
/**
 * AI Tagger Plugin — Entry point
 * Status: PLANNED (Phase 2)
 *
 * This is a stub that will be fully implemented in Phase 2.
 * See: .ai/agents/ai-tagger-agent/ for full specification.
 */

/** @type {import('../types').Plugin} */
const AITaggerPlugin = {
  id: 'ai-tagger',
  name: 'AI Bookmark Tagger',
  version: '0.1.0',

  /** Called when plugin initializes */
  async onInit(api) {
    console.log('[AITagger] Plugin initialized (stub)');
    // TODO Phase 2: Initialize AI service, load tag cache
  },

  /** Called when a bookmark is created */
  async onBookmarkCreate(bookmark, api) {
    console.log('[AITagger] New bookmark:', bookmark.title);
    // TODO Phase 2: Classify and tag the new bookmark
  },

  /**
   * Classify a single bookmark
   * @param {Object} bookmark - { title, url }
   * @returns {Promise<Object>} - { category, tags, confidence, suggested_folder }
   */
  async classify(bookmark) {
    // TODO Phase 2: Call Claude Haiku API
    // For now: rule-based fallback
    return ruleBasedClassify(bookmark);
  },

  /**
   * Classify all bookmarks in batch
   * @param {Object[]} bookmarks
   * @returns {Promise<Object[]>}
   */
  async batchClassify(bookmarks) {
    // TODO Phase 2: Batch API calls (10 per call)
    return Promise.all(bookmarks.map(bm => this.classify(bm)));
  },
};

/**
 * Rule-based classifier (no API needed)
 * @param {Object} bookmark
 * @returns {Object}
 */
function ruleBasedClassify({ title = '', url = '' }) {
  const DOMAIN_MAP = {
    'github.com': { category: 'Development', tags: ['code', 'opensource'] },
    'stackoverflow.com': { category: 'Development', tags: ['code', 'qa'] },
    'youtube.com': { category: 'Entertainment', tags: ['video'] },
    'medium.com': { category: 'Learning', tags: ['article', 'blog'] },
    'twitter.com': { category: 'Social', tags: ['social'] },
    'x.com': { category: 'Social', tags: ['social'] },
    'linkedin.com': { category: 'Business', tags: ['professional'] },
    'amazon.com': { category: 'Shopping', tags: ['ecommerce'] },
    'notion.so': { category: 'Tools', tags: ['productivity', 'notes'] },
    'figma.com': { category: 'Design', tags: ['design', 'ui'] },
  };

  try {
    const domain = new URL(url).hostname.replace('www.', '');
    const rule = DOMAIN_MAP[domain];
    if (rule) {
      return { ...rule, confidence: 0.8, suggested_folder: rule.category };
    }
  } catch {
    // Invalid URL
  }

  return {
    category: 'Other',
    tags: [],
    confidence: 0.1,
    suggested_folder: 'Other',
  };
}

export default AITaggerPlugin;

```

### File: vault\ARCHIVE\alamofire_network_base\README.md
```md
![Alamofire: Elegant Networking in Swift](https://raw.githubusercontent.com/Alamofire/Alamofire/master/Resources/AlamofireLogo.png)

[![Swift](https://img.shields.io/badge/Swift-6.0_6.1_6.2-orange?style=flat-square)](https://img.shields.io/badge/Swift-6.0_6.1_6.2-Orange?style=flat-square)
[![Platforms](https://img.shields.io/badge/Platforms-macOS_iOS_tvOS_watchOS_visionOS_Linux_Windows_Android-yellowgreen?style=flat-square)](https://img.shields.io/badge/Platforms-macOS_iOS_tvOS_watchOS_vision_OS_Linux_Windows_Android-Green?style=flat-square)
[![CocoaPods Compatible](https://img.shields.io/cocoapods/v/Alamofire.svg?style=flat-square)](https://img.shields.io/cocoapods/v/Alamofire.svg)
[![Carthage Compatible](https://img.shields.io/badge/Carthage-compatible-4BC51D.svg?style=flat-square)](https://github.com/Carthage/Carthage)
[![Swift Package Manager](https://img.shields.io/badge/Swift_Package_Manager-compatible-orange?style=flat-square)](https://img.shields.io/badge/Swift_Package_Manager-

...(truncated for OmniClaw Ecosystem)...
```

### File: vault\ARCHIVE\antigravity_kit_base\package.json
```json
{
  "name": "antigravity-kit",
  "version": "2.0.0",
  "description": "AI Agent templates - Skills, Agents, and Workflows for enhanced coding assistance",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/vudovn/antigravity-kit.git"
  },
  "homepage": "https://github.com/vudovn/antigravity-kit#readme",
  "bugs": {
    "url": "https://github.com/vudovn/antigravity-kit/issues"
  },
  "keywords": [
    "antigravity",
    "ai",
    "agent",
    "gemini",
    "skills",
    "templates"
  ],
  "author": "vudovn",
  "license": "MIT"
}
```

### File: vault\ARCHIVE\antigravity_manager_core\package.json
```json
{
  "name": "antigravity-manager",
  "productName": "Antigravity Manager",
  "version": "0.10.0",
  "description": "Antigravity Manager - Electron App",
  "main": ".vite/build/main.js",
  "private": true,
  "scripts": {
    "start": "electron-forge start",
    "package": "electron-forge package",
    "make": "electron-forge make",
    "publish": "electron-forge publish",
    "lint": "eslint .",
    "format": "prettier --check .",
    "format:write": "prettier --write .",
    "test": "vitest run",
    "test:watch": "vitest watch",
    "test:unit": "vitest",
    "test:e2e": "playwright test",
    "test:all": "vitest run && playwright test",
    "type-check": "tsc --noEmit"
  },
  "author": "Draculabo",
  "license": "CC-BY-NC-SA-4.0",
  "devDependencies": {
    "@electron-forge/cli": "^7.10.2",
    "@electron-forge/maker-deb": "^7.10.2",
    "@electron-forge/maker-dmg": "^7.10.2",
    "@electron-forge/maker-rpm": "^7.10.2",
    "@electron-forge/maker-squirrel": "^7.10.2",
    "@electron-forge/maker-wix": "^7.10.2",
    "@electron-forge/maker-zip": "^7.10.2",
    "@electron-forge/plugin-auto-unpack-natives": "^7.10.2",
    "@electron-forge/plugin-fuses": "^7.10.2",
    "@electron-forge/plugin-vite": "^7.10.2",
    "@electron-forge/publisher-github": "^7.10.2",
    "@electron-forge/shared-types": "^7.8.1",
    "@electron/fuses": "~1.8.0",
    "@electron/rebuild": "^3.7.1",
    "@eslint/compat": "^1.4.1",
    "@eslint/js": "^9.39.0",
    "@pengx17/electron-forge-maker-appimage": "^1.2.1",
    "@playwright/test": "^1.56.1",
    "@semantic-release/changelog": "^6.0.3",
    "@semantic-release/git": "^10.0.1",
    "@semantic-release/github": "^12.0.2",
    "@sentry/vite-plugin": "^4.8.0",
    "@swc/core": "^1.15.8",
    "@tailwindcss/vite": "^4.1.17",
    "@tanstack/router-plugin": "^1.135.0",
    "@testing-library/jest-dom": "^6.9.1",
    "@testing-library/react": "^16.3.0",
    "@testing-library/user-event": "^14.6.1",
    "@types/better-sqlite3": "^7.6.12",
    "@types/electron-squirrel-startup": "^1.0.2",
    "@types/eslint-config-prettier": "^6.11.3",
    "@types/lodash-es": "^4.17.12",
    "@types/node": "^24.10.1",
    "@types/react": "^19.2.2",
    "@types/react-dom": "^19.2.2",
    "@vitejs/plugin-react": "^4.7.0",
    "babel-plugin-react-compiler": "1.0.0",
    "code-inspector-plugin": "^1.3.3",
    "conventional-changelog-conventionalcommits": "^9.1.0",
    "electron": "^37.3.1",
    "electron-devtools-installer": "^4.0.0",
    "electron-packager-languages": "^0.6.0",
    "electron-playwright-helpers": "^1.8.2",
    "eslint": "^9.39.1",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-prettier": "^5.5.4",
    "eslint-plugin-react": "^7.37.5",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-unused-imports": "^4.4.1",
    "globals": "^16.5.0",
    "icon-gen": "^5.0.0",
    "jsdom": "^27.1.0",
    "node-addon-api": "^8.3.1",
    "prettier": "^3.6.2",
    "prettier-plugin-tailwindcss": "^0.7.1",
    "semantic-release": "^25.0.2",
    "semantic-release-config-gitmoji": "^1.5.3",
    "sharp": "^0.34.5",
    "tailwindcss": "^4.1.16",
    "ts-node": "^10.9.2",
    "typescript": "^5.9.3",
    "typescript-eslint": "^8.46.3",
    "unplugin-swc": "^1.5.9",
    "vite": "^5.4.21",
    "vitest": "^4.0.8"
  },
  "dependencies": {
    "@grpc/grpc-js": "^1.14.3",
    "@grpc/proto-loader": "^0.8.0",
    "@icons-pack/react-simple-icons": "^13.8.0",
    "@nestjs/common": "^11.1.10",
    "@nestjs/core": "^11.1.10",
    "@nestjs/microservices": "^11.1.11",
    "@nestjs/platform-express": "^11.1.11",
    "@nestjs/platform-fastify": "^11.1.10",
    "@orpc/client": "^1.10.4",
    "@orpc/server": "^1.11.3",
    "@radix-ui/react-avatar": "^1.1.11",
    "@radix-ui/react-checkbox": "^1.3.3",
    "@radix-ui/react-dialog": "^1.1.15",
    "@radix-ui/react-dropdown-menu": "^2.1.16",
    "@radix-ui/react-icons": "^1.3.2",
    "@radix-ui/react-label": "^2.1.8",
    "@radix-ui/react-navigation-menu": "^1.2.14",
    "@radix-ui/react-select": "^2.2.6",
    "@radix-ui/react-slot": "^1.2.4",
    "@radix-ui/react-switch": "^1.2.6",
    "@radix-ui/react-tabs": "^1.1.13",
    "@radix-ui/react-toast": "^1.2.15",
    "@radix-ui/react-toggle": "^1.1.9",
    "@radix-ui/react-toggle-group": "^1.1.11",
    "@radix-ui/react-tooltip": "^1.2.8",
    "@sentry/electron": "^7.7.0",
    "@sentry/integrations": "^7.114.0",
    "@tanstack/react-query": "^5.90.7",
    "@tanstack/react-router": "^1.139.3",
    "@tanstack/react-router-devtools": "^1.135.0",
    "@types/uuid": "^11.0.0",
    "axios": "^1.13.2",
    "better-sqlite3": "^12.4.6",
    "class-transformer": "^0.5.1",
    "class-validator": "^0.14.3",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "date-fns": "^4.1.0",
    "drizzle-orm": "^0.39.1",
    "electron-squirrel-startup": "^1.0.1",
    "fastify": "^5.6.2",
    "find-process": "^2.0.0",
    "happy-dom": "^20.0.10",
    "i18next": "^25.6.3",
    "i18next-browser-languagedetector": "^8.2.0",
    "keytar": "^7.9.0",
    "lodash-es": "^4.17.22",
    "lucide-react": "^0.553.0",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-error-boundary": "^6.1.0",
    "react-i18next": "^16.2.4",
    "reflect-metadata": "^0.2.2",
    "rxjs": "^7.8.2",
    "tailwind-merge": "^3.4.0",
    "tailwindcss-animate": "^1.0.7",
    "undici": "^7.16.0",
    "update-electron-app": "^3.1.1",
    "uuid": "^13.0.0",
    "winston": "^3.19.0",
    "winston-daily-rotate-file": "^5.0.0",
    "yaml": "^2.8.2",
    "zod": "^4.1.12"
  }
}

```

### File: vault\ARCHIVE\claude_cookbooks\README.md
```md
# Claude Cookbooks

The Claude Cookbooks provide code and guides designed to help developers build with Claude, offering copy-able code snippets that you can easily integrate into your own projects.

## Prerequisites

To make the most of the examples in this cookbook, you'll need a Claude API key (sign up for free [here](https://www.anthropic.com)).

While the code examples are primarily written in Python, the concepts can be adapted to any programming language that supports interaction with the Claude API.

If you're new to working with the Claude API, we recommend starting with our [Claude API Fundamentals course](https://github.com/anthropics/courses/tree/master/anthropic_api_fundamentals) to get a solid foundation.

## Explore Further

Looking for more resources to enhance your experience with Claude and AI assistants? Check out these helpful links:

- [Anthropic developer documentation](https://docs.claude.com/claude/docs/guide-to-anthropics-prompt-engineering-resources)
- [Anthropic support docs](https://support.anthropic.com)
- [Anthropic Discord community](https://www.anthropic.com/discord)

## Contributing

The Claude Cookbooks thrives on the contributions of the developer community. We value your input, whether it's submitting an idea, fixing a typo, adding a new guide, or improving an existing one. By contributing, you help make this resource even more valuable for everyone.

To avoid duplication of efforts, please review the existing issues and pull requests before contributing.

If you have ideas for new examples or guides, share them on the [issues page](https://github.com/anthropics/anthropic-cookbook/issues).

## Table of recipes

### Capabilities
- [Classification](https://github.com/anthropics/anthropic-cookbook/tree/main/capabilities/classification): Explore techniques for text and data classification using Claude.
- [Retrieval Augmented Generation](https://github.com/anthropics/anthropic-cookbook/tree/main/capabilities/retrieval_augmented_generation): Learn how to enhance Claude's responses with external knowledge.
- [Summarization](https://github.com/anthropics/anthropic-cookbook/tree/main/capabilities/summarization): Discover techniques for effective text summarization with Claude.

### Tool Use and Integration
- [Tool use](https://github.com/anthropics/anthropic-cookbook/tree/main/tool_use): Learn how to integrate Claude with external tools and functions to extend its capabilities.
  - [Customer service agent](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/customer_service_agent.ipynb)
  - [Calculator integration](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/calculator_tool.ipynb)
  - [SQL queries](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/how_to_make_sql_queries.ipynb)

### Third-Party Integrations
- [Retrieval augmented generation](https://github.com/anthropics/anthropic-cookbook/tree/main/third_party): Supplement Claude's knowledge with external data sources.
  - [Vector databases (Pinecone)](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/Pinecone/rag_using_pinecone.ipynb)
  - [Wikipedia](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/Wikipedia/wikipedia-search-cookbook.ipynb/)
  - [Web pages](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/read_web_pages_with_haiku.ipynb)
- [Embeddings with Voyage AI](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/VoyageAI/how_to_create_embeddings.md)

### Multimodal Capabilities
- [Vision with Claude](https://github.com/anthropics/anthropic-cookbook/tree/main/multimodal): 
  - [Getting started with images](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/getting_started_with_vision.ipynb)
  - [Best practices for vision](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/best_practices_for_vision.ipynb)
  - [Interpreting charts and graphs](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/reading_charts_graphs_powerpoints.ipynb)
  - [Extracting content from forms](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/how_to_transcribe_text.ipynb)
- [Generate images with Claude](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/illustrated_responses.ipynb): Use Claude with Stable Diffusion for image generation.

### Advanced Techniques
- [Sub-agents](https://github.com/anthropics/anthropic-cookbook/blob/main/multimodal/using_sub_agents.ipynb): Learn how to use Haiku as a sub-agent in combination with Opus.
- [Upload PDFs to Claude](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/pdf_upload_summarization.ipynb): Parse and pass PDFs as text to Claude.
- [Automated evaluations](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_evals.ipynb): Use Claude to automate the prompt evaluation process.
- [Enable JSON mode](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/how_to_enable_json_mode.ipynb): Ensure consistent JSON output from Claude.
- [Create a moderation filter](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/building_moderation_filter.ipynb): Use Claude to create a content moderation filter for your application.
- [Prompt caching](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/prompt_caching.ipynb): Learn techniques for efficient prompt caching with Claude.

## Additional Resources

- [Anthropic on AWS](https://github.com/aws-samples/anthropic-on-aws): Explore examples and solutions for using Claude on AWS infrastructure.
- [AWS Samples](https://github.com/aws-samples/): A collection of code samples from AWS which can be adapted for use with Claude. Note that some samples may require modification to work optimally with Claude.

```

### File: vault\ARCHIVE\claude_usage_checker\README.md
```md
# Claude Usage Checker

<div align="center">
  <img src="icon128.png" alt="Claude Usage Checker" width="128" height="128">
  
  **Track your Claude.ai usage with a beautiful floating popup**
</div>

---

## ✨ Features

- 📊 **Real-time Usage** - Displays actual usage from Claude's API
- ⏱️ **Session & Weekly Limits** - Shows 5-hour and 7-day quotas
- 🎨 **Dark Theme** - Clean, modern glassmorphism design
- 🔒 **Privacy Focused** - No data collection, all local
- 🔄 **Auto Refresh** - Updates every 60 seconds

## 📸 Screenshot

<div align="center">
  <img src="Screenshot.png" alt="Screenshot" width="600">
</div>

## 🚀 Installation

1. Clone: `git clone https://github.com/0xAstroAlpha/Claude-Usage-Checker.git`
2. Go to `chrome://extensions/`
3. Enable **Developer mode**
4. Click **Load unpacked** → select the folder
5. Visit [claude.ai](https://claude.ai)

## 📁 Files

```
├── manifest.json       # Extension config
├── content.js          # Main script
├── tracker-styles.css  # Popup styling
├

...(truncated for OmniClaw Ecosystem)...
```

### File: vault\ARCHIVE\cloud_sync_engine\index.js
```js
/**
 * Cloud Sync Plugin — Entry point
 * Status: PLANNED (Phase 3)
 */

const CloudSyncPlugin = {
  id: 'cloud-sync',
  name: 'Cloud Sync',
  version: '0.1.0',

  async onInit(api) {
    console.log('[CloudSync] Plugin initialized (stub)');
  },

  /**
   * Export all bookmarks as JSON file download
   * @param {Object} api - BookMarkAPI
   */
  async exportToFile(api) {
    const tree = await api.bookmarks.getAll();
    const count = countBookmarks(tree[0]);

    const data = {
      version: '1.0',
      app: 'smart-bookmark-manager',
      exported: new Date().toISOString(),
      count,
      tree,
    };

    const blob = new Blob([JSON.stringify(data, null, 2)], {
      type: 'application/json',
    });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = `bookmarks_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();

    URL.revokeObjectURL(url);
    api.ui.showToast(`Exported ${count} bookmarks`, 'success');
  },

  /**
   * Import bookmarks from JSON file
   * @param {File} file
   * @param {Object} api - BookMarkAPI
   */
  async importFromFile(file, api) {
    const text = await file.text();
    const data = JSON.parse(text);

    if (!data.version || !data.tree) {
      throw new Error('Invalid bookmark file format');
    }

    // TODO Phase 3: Import with duplicate detection
    api.ui.showToast(`Import from file: ${file.name}`, 'info');
    console.log('[CloudSync] Import preview:', data.count, 'bookmarks');
  },
};

/** Count bookmarks in tree */
function countBookmarks(node) {
  if (!node) return 0;
  if (node.url) return 1;
  return (node.children || []).reduce((sum, c) => sum + countBookmarks(c), 0);
}

export default CloudSyncPlugin;

```

### File: vault\ARCHIVE\jsxer_transpiler_engine\README.md
```md
# Jsxer
A faster decompiler for Adobe's (Legacy) ExtendScript binary format (*.jsxbin).

> [!WARNING]
> This project is currently being rewritten in Rust. Development is occurring on the `rust-rewrite` branch.

## Features
* [x] Lifts JSXBIN back to JavaScript code.
* [x] Jsxblind deobfuscation (experimental).
* [x] Python bindings.
* [x] Dynamic library.
* [x] **Fast as hell.**

## What is ExtendScript?
ExtendScript is a scripting language and an associated toolkit developed by Adobe Systems, intended for use with Creative Suite and Technical Communication Suite products. It is a dialect of the ECMAScript 3 standard and therefore similar to JavaScript and ActionScript. The toolkit comes bundled with Creative Suite and Technical Communication Suite editions and can access tools within applications like Photoshop, FrameMaker, InDesign or After Effects for batch-processing projects.

## Please, do not use this project unethically.

#### yo, pirates, hear me out...

Look, I get that it's tempting– money doesn't grow on trees.

Many script authors are independent developers, and by stealing their work you make what they do unsustainable and their lives harder. Without income, they are not able to create and maintain what many people may depend on.  

Jsxer (in addition to simply being a fun and educational project to develop) was made for source code recovery and security research purposes. It is free and open-source software– and as such, I won't try to control what you can and can't do with it. 

Just remember that script authors are real humans! So if you like their work, show some love and fork over the dough. :)

Appreciate ya!

## Build (MacOS)

### [Video Tutorial](https://www.youtube.com/watch?v=939Bo5iTxo0)

Open the Terminal app to run the following commands. If you are unfamiliar with Terminal, you can find it in /Applications/Utilities/Terminal.app.

*Install CMake:*
```bash
brew install cmake
```

*Configure and build the project:*
```bash
cmake .
cmake --build . --config release 
```

*After a successful build, navigate to the folder with the executable:*
```bash
cd ./bin/release/
```

## Usage

> [!IMPORTANT]
> Make sure that the input file only contains the JSXBIN literal itself.<sup><a href="https://youtu.be/939Bo5iTxo0?lc=UgyPDxgsuRmbfd8MI-F4AaABAg.9gIEl4rxFVa9gIFW1EPzqO">\[1\]</a></sup>&ensp;(Usually starting with `@JSXBIN@`)

```bash
jsxer <jsxbin path>
```

The `--unblind` flag enables the experimental deobfuscation.

## Credits
  - Thanks to Andrin Meier ([@andrinpricemeier](https://github.com/andrinpricemeier), formerly `@autoboosh`) for his research on the format, and his project [jsxbin-to-jsx-converter](https://github.com/autoboosh/jsxbin-to-jsx-converter).
  - Thanks to [@codecopy](https://github.com/codecopy) for keeping a [fork](https://github.com/codecopy/jsxbin-to-jsx-converter) of `@autoboosh`'s project, where the original vanished as a consequence of a DMCA takedown from Adobe.


## Contributions
Contributions are welcome. Open an issue if you have a problem. Check contribution guidelines [here](CONTRIBUTING.md).

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=AngeloD2022/jsxer&type=Date)](https://star-history.com/#AngeloD2022/jsxer&Date)


```

### File: vault\ARCHIVE\kore_memory_base\README.md
```md
<div align="center">

<img src="assets/logo.svg" alt="Kore Memory" width="420"/>

<br/>

**The memory layer that thinks like a human.**
<br/>
Remembers what matters. Forgets what doesn't. Never calls home.

<br/>

[![CI](https://github.com/auriti-labs/kore-memory/actions/workflows/ci.yml/badge.svg)](https://github.com/auriti-labs/kore-memory/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/kore-memory.svg?style=flat-square&color=7c3aed)](https://pypi.org/project/kore-memory/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue?style=flat-square)](https://python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Zero Cloud](https://img.shields.io/badge/cloud-zero-orange?style=flat-square)]()
[![Multilingual](https://img.shields.io/badge/languages-50%2B-purple?style=flat-square)]()
[![Docs](https://img.shields.io/badge/docs-auritidesign.it-00b4d8?style=flat-square)](https://auritidesign.it/docs/kore-memory/)

<br/>

[**Docs**](https://auritidesign.it/docs/kore-memory/) · [**Install**](#-install) · [**Quickstart**](#-quickstart) · [**How it works**](#-how-it-works) · [**API**](#-api-reference) · [**Changelog**](CHANGELOG.md) · [**Roadmap**](#-roadmap)

</div>

---

## Why Kore?

Every AI agent memory tool has the same flaw: they remember everything forever, phone home to cloud APIs, or need an LLM just to decide what's worth storing.

**Kore is different.**

<div align="center">

| Feature | **Kore** | Mem0 | Letta | Memori |
|---|:---:|:---:|:---:|:---:|
| Runs fully offline | ✅ | ❌ | ❌ | ❌ |
| No LLM required | ✅ | ❌ | ❌ | ✅ |
| **Memory Decay** (Ebbinghaus) | ✅ | ❌ | ❌ | ❌ |
| Auto-importance scoring | ✅ local | ✅ via LLM | ❌ | ❌ |
| **Memory Compression** | ✅ | ❌ | ❌ | ❌ |
| Semantic search (50+ langs) | ✅ local | ✅ via API | ✅ | ✅ |
| Timeline API | ✅ | ❌ | ❌ | ❌ |
| Tags & Relations (graph) | ✅ | ❌ | ✅ | ❌ |
| TTL / Auto-expiration | ✅ | ❌ | ❌ | ❌ |
| MCP Server (Claude, Cursor) | ✅ | ❌ | ❌ | ❌ |
| Batch API | ✅ | ❌ | ❌ | ❌ |
| Export / Import (JSON) | ✅ | ❌ | ✅ | ❌ |
| Soft-delete / Archive | ✅ | ❌ | ❌ | ❌ |
| Prometheus Metrics | ✅ | ❌ | ❌ | ❌ |
| Agent namespace isolation | ✅ | ✅ | ✅ | ❌ |
| Install in 2 minutes | ✅ | ❌ | ❌ | ❌ |

</div>

---

## ✨ Key Features

### 📉 Memory Decay — The Ebbinghaus Engine
Memories fade over time using the [Ebbinghaus forgetting curve](https://en.wikipedia.org/wiki/Forgetting_curve). Critical memories persist for months. Casual notes fade in days.

```
decay = e^(-t · ln2 / half_life)
```

Every retrieval resets the clock and boosts the decay score — just like spaced repetition in human learning.

### 🤖 Auto-Importance Scoring
No LLM call needed. Kore scores importance locally using content analysis — keywords, category, length.

```python
"API token: sk-abc123"  →  importance: 5  (critical, never forget)
"Juan prefers dark mode"  →  importance: 4  (preference)
"Meeting at 3pm"  →  importance: 2  (general)
```

### 🔍 Semantic Search in 50+ Languages
Powered by local `sentence-transformers`. Find memories by meaning, not just keywords. Search in English, get results in Italian. Zero API calls.

### 🗜️ Memory Compression
Similar memories (cosine similarity > 0.88) are automatically merged into richer, deduplicated records. Your DB stays lean forever.

### 📅 Timeline API
"What did I know about project X last month?" — trace any subject chronologically.

### 🏷️ Tags & Relations
Organize memories with tags and build a knowledge graph by linking related memories together. Search by tag, traverse relations bidirectionally.

### ⏳ TTL — Time-to-Live
Set an expiration on any memory. Expired memories are automatically excluded from search, export, and timeline. Run `/cleanup` to purge them, or let the decay pass handle it.

### 📦 Batch API
Save up to 100 memories in a single request. Perfect for bulk imports and agent bootstrapping.

### 💾 Export / Import
Full JSON export of all active memories. Import from a previous backup or migrate between instances.

### 🔌 MCP Server (Model Context Protocol)
Native integration with Claude, Cursor, and any MCP-compatible client. Exposes save, search, timeline, decay, compress, and export as MCP tools.

### 🔐 Agent Namespace Isolation
Multi-agent safe. Each agent sees only its own memories, even on a shared server.

---

## 📦 Install

```bash
# Core (FTS5 search only)
pip install kore-memory

# With semantic search (50+ languages, local embeddings)
pip install kore-memory[semantic]

# With MCP server (Claude, Cursor integration)
pip install kore-memory[semantic,mcp]
```

---

## 🚀 Quickstart

```bash
# Start the server
kore
# → Kore running on http://localhost:8765
```

```bash
# Save a memory
curl -X POST http://localhost:8765/save \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"content": "User prefers concise responses in Italian", "category": "preference"}'

# → {"id": 1, "importance": 4, "message": "Memory saved"}
#   (importance auto-scored: preference category + keyword "prefers")
```

```bash
# Search — any language
curl "http://localhost:8765/search?q=user+preferences&limit=5" \
  -H "X-Agent-Id: my-agent"
```

```bash
# Save with TTL (auto-expires after 48 hours)
curl -X POST http://localhost:8765/save \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"content": "Deploy scheduled for Friday", "category": "task", "ttl_hours": 48}'
```

```bash
# Batch save (up to 100 per request)
curl -X POST http://localhost:8765/save/batch \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"memories": [
    {"content": "React 19 supports server components", "category": "project"},
    {"content": "Always use parameterized queries", "category": "decision", "importance": 5}
  ]}'
```

```bash
# Tag a memory
curl -X POST http://localhost:8765/memories/1/tags \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"tags": ["react", "frontend"]}'

# Search by tag
curl "http://localhost:8765/tags/react/memories" \
  -H "X-Agent-Id: my-agent"
```

```bash
# Link two related memories
curl -X POST http://localhost:8765/memories/1/relations \
  -H "Content-Type: application/json" \
  -H "X-Agent-Id: my-agent" \
  -d '{"target_id": 2, "relation": "depends_on"}'
```

```bash
# Timeline for a subject
curl "http://localhost:8765/timeline?subject=project+alpha" \
  -H "X-Agent-Id: my-agent"

# Run daily decay pass (cron this)
curl -X POST http://localhost:8765/decay/run \
  -H "X-Agent-Id: my-agent"

# Compress similar memories
curl -X POST http://localhost:8765/compress \
  -H "X-Agent-Id: my-agent"

# Export all memories (JSON backup)
curl "http://localhost:8765/export" \
  -H "X-Agent-Id: my-agent" > backup.json

# Cleanup expired memories
curl -X POST http://localhost:8765/cleanup \
  -H "X-Agent-Id: my-agent"
```

---

## 🧠 How It Works

```
Save memory
    │
    ▼
Auto-score importance (1–5)
    │
    ▼
Generate embedding (local, offline)
    │
    ▼
Store in SQLite with decay_score = 1.0
    │
    │   [time passes]
    │
    ▼
decay_score decreases (Ebbinghaus curve)
    │
    ▼
Search query arrives
    │
    ▼
Semantic similarity scored
    │
    ▼
Filter out forgotten memories (decay < 0.05)
    │
    ▼
Re-rank by effective_score = similarity × decay × importance
    │
    ▼
Access reinforcement: decay_score += 0.05
    │
    ▼
Return top-k results
```

### Memory Half-Lives

| Importance | Label | Half-life |
|:---:|:---:|:---:|
| 1 | Low | 7 days |
| 2 | Normal | 14 days |
| 3 | Important | 30 days |
| 4 | High | 90 days |
| 5 | Critical | 365 days |

Each retrieval extends the half-life by **+15%** (spaced repetition effect).

---

## 📡 API Reference

### Core

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/save` | Save a memory (auto-scored). Supports `ttl_hours` for auto-expiration |
| `POST` | `/save/batch` | Save up to 100 memories in one request |
| `GET` | `/search?q=...` | Semantic search with pagination (`limit`, `offset`) |
| `GET` | `/timeline?subject=...` | Chronological history with pagination |
| `DELETE` | `/memories/{id}` | Delete a memory |
| `PUT` | `/memories/{id}` | Update a memory (content, category, importance) |

### Tags

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/memories/{id}/tags` | Add tags to a memory |
| `DELETE` | `/memories/{id}/tags` | Remove tags from a memory |
| `GET` | `/memories/{id}/tags` | List tags for a memory |
| `GET` | `/tags/{tag}/memories` | Search memories by tag |

### Relations

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/memories/{id}/relations` | Create a relation to another memory |
| `GET` | `/memories/{id}/relations` | List all relations (bidirectional) |

### Maintenance

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/decay/run` | Recalculate decay scores + cleanup expired |
| `POST` | `/compress` | Merge similar memories |
| `POST` | `/cleanup` | Remove expired memories (TTL) |
| `GET` | `/metrics` | Prometheus metrics (memory counts, latency, decay stats) |

### Archive

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/memories/{id}/archive` | Soft-delete (archive) a memory |
| `POST` | `/memories/{id}/restore` | Restore an archived memory |
| `GET` | `/archive` | List archived memories |

### Backup

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/export` | Export all active memories (JSON) |
| `POST` | `/import` | Import memories from a previous export |

### Utility

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Health check + capabilities |
| `GET` | `/dashboard` | Web dashboard (HTML, no auth required) |

Interactive docs: **http://localhost:8765/docs**

### Headers

| Header | Required | Description |
|---|:---:|---|
| `X-Agent-Id` | No | Agent namespace (default: `"default"`) |
| `X-Kore-Key` | On non-localhost | API key (auto-generated on first run) |

### Categories

`general` · `project` · `trading` · `finance` · `person` · `preference` · `task` · `decision`

### Save Request Body

```json
{
  "content": "Memory content (3–4000 chars)",
  "category": "general",
  "importance": null,
  "ttl_hours": null
}
```

| Field | Type | Default | Description |
|---|---|---|---|
| `content` | string | *required* | Memory text (3–4000 chars) |
| `category` | string | `"general"` | One of the categories above |
| `importance` | int (1–5) \| null | `null` | null = auto-scored, 1–5 = explicit |
| `ttl_hours` | int \| null | `null` | Auto-expire after N hours (1–8760). Null = never expires |

---

## ⚙️ Configuration

| Env Var | Default | Description |
|---|---|---|
| `KORE_DB_PATH` | `data/memory.db` | Custom database path |
| `KORE_HOST` | `127.0.0.1` | Server bind address |
| `KORE_PORT` | `8765` | Server port |
| `KORE_LOCAL_ONLY` | `1` | Skip auth for localhost requests |
| `KORE_API_KEY` | auto-generated | Override API key |
| `KORE_CORS_ORIGINS` | *(empty)* | Comma-separated allowed origins |
| `KORE_EMBED_MODEL` | `paraphrase-multilingual-MiniLM-L12-v2` | Sentence-transformers model |
| `KORE_MAX_EMBED_CHARS` | `8000` | Max chars sent to embedder (OOM protection) |
| `KORE_SIMILARITY_THRESHOLD` | `0.88` | Cosine threshold for compression |

---

## 🔌 MCP Server

Kore ships with a native [Model Context Protocol](https://modelcontextprotocol.io) server for direct integration with Claude, Cursor, and any MCP-compatible client.

```bash
# Install with MCP support
pip install kore-memory[mcp]

# Run the MCP server (stdio transport, default)
kore-mcp
```

### Available MCP Tools

| Tool | Description |
|---|---|
| `memory_save` | Save a memory with auto-scoring |
| `memory_search` | Semantic or full-text search |
| `memory_delete` | Delete a memory |
| `memory_update` | Update memory content, category, or importance |
| `memory_save_batch` | Save up to 100 memories at once |
| `memory_add_tags` | Add tags to a memory |
| `memory_search_by_tag` | Search memories by tag |
| `memory_add_relation` | Link two related memories |
| `memory_timeline` | Chronological history for a subject |
| `memory_decay_run` | Recalculate decay scores |
| `memory_compress` | Merge similar memories |
| `memory_cleanup` | Remove expired memories |
| `memory_import` | Import memories from JSON |
| `memory_export` | Export all active memories |

### Claude Desktop Configuration

Add to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "kore-memory": {
      "command": "kore-mcp",
      "args": []
    }
  }
}
```

### Cursor / Claude Code Configuration

Add to your `.claude/settings.json` or MCP config:

```json
{
  "mcpServers": {
    "kore-memory": {
      "command": "kore-mcp"
    }
  }
}
```

---

## 📊 Web Dashboard

Kore includes a built-in web dashboard served directly from FastAPI — no build step, no npm, no extra dependencies.

```bash
# Start Kore
kore

# Open in browser
open http://localhost:8765/dashboard
```

### Features

| Tab | Description |
|---|---|
| **Overview** | Health status, total memories, categories breakdown |
| **Memories** | Search (FTS + semantic), save, delete, pagination |
| **Tags** | Search by tag, add/remove/list tags on any memory |
| **Relations** | View and create memory relations (knowledge graph) |
| **Timeline** | Chronological trace for any subject |
| **Maintenance** | Run decay, compress, and cleanup with one click |
| **Backup** | Export as JSON download, import from file |

- Dark theme with Kore purple accents
- Responsive (mobile-friendly with bottom nav)
- Agent selector in header — switch agent context instantly
- All interactions via the same REST API (no separate backend)

---

## 🟨 JavaScript/TypeScript SDK

Kore ships with a native JavaScript/TypeScript client — zero runtime dependencies, dual ESM/CJS output, full type safety.

```bash
npm install kore-memory-client
```

### Usage

```typescript
import { KoreClient } from 'kore-memory-client';

const kore = new KoreClient({
  baseUrl: 'http://localhost:8765',
  agentId: 'my-agent'
});

// Save
const result = await kore.save({
  content: 'User prefers dark mode',
  category: 'preference',
  importance: 4
});

// Search
const memories = await kore.search({
  q: 'dark mode',
  limit: 5,
  semantic: true
});

// Tags & Relations
await kore.addTags(result.id, ['ui', 'preference']);
await kore.addRelation(result.id, otherId, 'related');

// Update
await kore.update(result.id, { importance: 5 });

// Archive & Restore
await kore.archive(result.id);
await kore.restore(result.id);

// Maintenance
await kore.decayRun();
await kore.compress();

// Export
const backup = await kore.exportMemories();
```

### Error Handling

```typescript
import { KoreValidationError, KoreAuthError } from 'kore-memory-client';

try {
  await kore.save({ content: 'ab' }); // too short
} catch (error) {
  if (error instanceof KoreValidationError) {
    console.log('Validation failed:', error.detail);
  }
}
```

**Features:** Zer
... [TRUNCATED]
```

### File: vault\ARCHIVE\kore_memory_base\requirements.txt
```txt
fastapi>=0.115.0
uvicorn[standard]>=0.30.0
pydantic>=2.7.0
sentence-transformers>=3.0.0
httpx>=0.27.0

```

### File: vault\ARCHIVE\lobster_board_app\package.json
```json
{
  "name": "lobsterboard",
  "version": "0.6.3",
  "description": "Self-hosted drag-and-drop dashboard builder with 50 widgets, template gallery, and custom pages. Works standalone or with OpenClaw.",
  "keywords": [
    "dashboard",
    "widgets",
    "monitoring",
    "kpi",
    "builder",
    "homelab",
    "self-hosted",
    "openclaw"
  ],
  "author": "curbob",
  "license": "BSL-1.1",
  "homepage": "https://github.com/curbob/LobsterBoard#readme",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/curbob/LobsterBoard.git"
  },
  "bugs": {
    "url": "https://github.com/curbob/LobsterBoard/issues"
  },
  "type": "module",
  "main": "dist/lobsterboard.umd.js",
  "module": "dist/lobsterboard.esm.js",
  "unpkg": "dist/lobsterboard.umd.min.js",
  "jsdelivr": "dist/lobsterboard.umd.min.js",
  "browser": "dist/lobsterboard.umd.min.js",
  "exports": {
    ".": {
      "import": "./dist/lobsterboard.esm.js",
      "require": "./dist/lobsterboard.umd.js",
      "browser": "./dist/lobsterboard.umd.min.js"
    },
    "./css": "./dist/lobsterboard.css",
    "./widgets": {
      "import": "./src/widgets.js"
    },
    "./builder": {
      "import": "./src/builder.js"
    }
  },
  "bin": {
    "lobsterboard": "./bin/lobsterboard.mjs"
  },
  "files": [
    "server.cjs",
    "app.html",
    "js/",
    "css/",
    "dist",
    "src",
    "bin/",
    "templates/",
    "js/templates.js",
    "README.md",
    "CHANGELOG.md",
    "LICENSE"
  ],
  "scripts": {
    "build": "rollup -c",
    "build:watch": "rollup -c -w",
    "prebuild": "rm -rf dist",
    "start": "node server.cjs",
    "dev": "node server.cjs",
    "prepublishOnly": "npm run build"
  },
  "devDependencies": {
    "@rollup/plugin-terser": "^0.4.4",
    "rollup": "^4.9.6",
    "rollup-plugin-copy": "^3.5.0"
  },
  "engines": {
    "node": ">=16.0.0"
  },
  "dependencies": {
    "systeminformation": "^5.30.7"
  }
}

```

### File: vault\ARCHIVE\minimax_mcp_js_ext\package.json
```json
{
  "name": "minimax-mcp-js",
  "version": "0.0.17", 
  "description": "Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.",
  "main": "build/index.js",
  "type": "module",
  "bin": {
    "minimax-mcp-js": "./build/index.js"
  },
  "scripts": {
    "build": "tsc && chmod 755 build/index.js",
    "start": "node build/index.js",
    "dev": "tsc -w",
    "format": "prettier --write \"src/**/*.ts\"",
    "lint": "prettier --check \"src/**/*.ts\"",
    "prepare": "pnpm run build",
    "pretest": "pnpm run build",
    "inspector": "npx @modelcontextprotocol/inspector build/index.js"
  },
  "keywords": [
    "mcp",
    "minimax",
    "ai",
    "image-generation",
    "video-generation",
    "music-generation",
    "text-to-speech",
    "tts"
  ],
  "author": "Mark Yang <https://github.com/MaxYangyu>",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/MiniMax-AI/MiniMax-MCP-JS.git"
  },
  "bugs": {
    "url": "https://github.com/MiniMax-AI/MiniMax-MCP-JS/issues"
  },
  "homepage": "https://github.com/MiniMax-AI/MiniMax-MCP-JS#readme",
  "dependencies": {
    "@chatmcp/sdk": "^1.0.5",
    "@modelcontextprotocol/sdk": "^1.7.0",
    "axios": "^1.8.4",
    "cors": "^2.8.5",
    "dotenv": "^16.5.0",
    "express": "^4.18.2",
    "yargs": "18.0.0-candidate.4",
    "zod": "^3.24.2"
  },
  "devDependencies": {
    "@types/cors": "^2.8.17",
    "@types/express": "^5.0.1",
    "@types/node": "^22.14.1",
    "@types/yargs": "^17.0.33",
    "prettier": "^3.2.1",
    "typescript": "^5.8.3"
  },
  "engines": {
    "node": ">=20.0.0",
    "pnpm": ">=8.0.0"
  },
  "files": [
    "build",
    "README.md",
    "README.zh-CN.md"
  ],
  "publishConfig": {
    "access": "public"
  }
}
```

### File: vault\ARCHIVE\mirofish_app_base\README.md
```md
<div align="center">

<img src="./static/image/MiroFish_logo_compressed.jpeg" alt="MiroFish Logo" width="75%"/>

<a href="https://trendshift.io/repositories/16144" target="_blank"><img src="https://trendshift.io/api/badge/repositories/16144" alt="666ghj%2FMiroFish | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

简洁通用的群体智能引擎，预测万物
</br>
<em>A Simple and Universal Swarm Intelligence Engine, Predicting Anything</em>

<a href="https://www.shanda.com/" target="_blank"><img src="./static/image/shanda_logo.png" alt="666ghj%2MiroFish | Shanda" height="40"/></a>

[![GitHub Stars](https://img.shields.io/github/stars/666ghj/MiroFish?style=flat-square&color=DAA520)](https://github.com/666ghj/MiroFish/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/666ghj/MiroFish?style=flat-square)](https://github.com/666ghj/MiroFish/watchers)
[![GitHub Forks](https://img.shields.io/github/forks/666ghj/MiroFish?style=flat-square)](https://github.com/666ghj/Miro

...(truncated for OmniClaw Ecosystem)...
```

### File: vault\ARCHIVE\notebooklm_mcp_core\package.json
```json
{
  "name": "notebooklm-mcp",
  "version": "1.2.1",
  "description": "MCP server for NotebookLM API with session support and human-like behavior",
  "type": "module",
  "bin": {
    "notebooklm-mcp": "dist/index.js"
  },
  "scripts": {
    "build": "tsc",
    "postbuild": "chmod +x dist/index.js",
    "watch": "tsc --watch",
    "dev": "tsx watch src/index.ts",
    "prepare": "npm run build",
    "test": "tsx src/index.ts"
  },
  "keywords": [
    "mcp",
    "notebooklm",
    "gemini",
    "ai",
    "claude"
  ],
  "author": "Gérôme Dexheimer <hello@geromedexheimer.de> (https://github.com/PleasePrompto)",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/PleasePrompto/notebooklm-mcp.git"
  },
  "homepage": "https://github.com/PleasePrompto/notebooklm-mcp#readme",
  "bugs": {
    "url": "https://github.com/PleasePrompto/notebooklm-mcp/issues"
  },
  "files": [
    "dist",
    "README.md",
    "NOTEBOOKLM_USAGE.md",
    "LICENSE",
    "docs"
  ],
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0",
    "dotenv": "^16.4.0",
    "env-paths": "^3.0.0",
    "globby": "^14.1.0",
    "patchright": "^1.48.2",
    "zod": "^3.22.0"
  },
  "devDependencies": {
    "@types/node": "^20.11.0",
    "tsx": "^4.7.0",
    "typescript": "^5.3.3"
  },
  "engines": {
    "node": ">=18.0.0"
  }
}

```

### File: vault\ARCHIVE\notebooklm_skill_pack\requirements.txt
```txt
# NotebookLM Skill Dependencies
# These will be installed in the skill's local .venv

# Core browser automation with anti-detection
# Note: After installation, run: patchright install chrome
# (Chrome is required, not Chromium, for cross-platform reliability)
patchright==1.55.2

# Environment management
python-dotenv==1.0.0
```

### File: vault\ARCHIVE\openspace_framework\README.md
```md
<div align="center">

<picture>
    <img src="assets/logo.png" width="320px" style="border: none; box-shadow: none;" alt="OpenSpace Logo">
</picture>

## ✨ OpenSpace: Make Your Agents: Smarter, Low-Cost, Self-Evolving ✨

| 🔋 **46% Fewer Tokens** | **💰 $11K earned in 6 Hours** | 🧬 **Self-Evolving Skills** | 🌐 **Agents Experience Sharing** |

[![Agents](https://img.shields.io/badge/Agents-Claude_Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20nanobot%20%7C%20...-99C9BF.svg)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)
[![Feishu](https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=larksuite&logoColor=white)](./COMMUNICATION.md)
[![WeChat](https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white)](./COMMUNICATION.md)
[![中文文档](https://img.shields.io/badge/文档-中文版-F5C6C6?style=flat)](./README_CN.md)

**One Command to Evolve All Your AI Agents**: OpenClaw, nanobot, Claude Code, Codex, Cursor and etc.

<img src="assets/cli-typing.gif" width="500px" alt="openspace --query your task">

</div>

---

## The Problem with Today's AI Agents

Today's AI agents — [OpenClaw](https://github.com/openclaw/openclaw), [nanobot](https://github.com/HKUDS/nanobot), [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://github.com/openai/codex), [Cursor](https://cursor.com), etc. — are powerful, but they have a critical weakness: they never **Learn**, **Adapt**, and **Evolve** from real-world experience — let alone **Share** with each other.
- **❌ Massive Token Waste** - How to reuse successful task patterns instead of reasoning from scratch and burning tokens every time?
- **❌ Repeated Costly Failures** - How to share solutions across agents instead of repeating the same costly exploration and mistakes?
- **❌ Poor and Unreliable Skills** - How to maintain skill reliability as tools and APIs evolve — while ensuring community-contributed skills meet rigorous quality standards?

## 🎯 What is OpenSpace?

**🚀 🚀 The self-evolving engine where every task makes every agent smarter and more cost-efficient.**

https://github.com/user-attachments/assets/c50f70ab-f6db-47bf-9498-3210c0f0abae

OpenSpace plugs into any agent as skills and evolves it with three superpowers:

### 🧬 Self-Evolution
Skills that learn and improve themselves automatically
- ✅ **AUTO-FIX** — When a skill breaks, it fixes itself instantly
- ✅ **AUTO-IMPROVE** — Successful patterns become better skill versions
- ✅ **AUTO-LEARN** — Captures winning workflows from actual usage
- ✅ **Quality monitoring** — Tracks skill performance, error rates, and execution success across all tasks.

**Skills that continuously evolve — turning every failure into improvement, every success into optimization.**

### 🌐 Collective Agent Intelligence
Turn individual agents into a shared brain
- ✅ **Shared evolution**: One agent's improvement becomes every agent's upgrade
- ✅ **Network effects**: More agents → richer data → faster evolution for every agent
- ✅ **Easy sharing** — Upload and download evolved skills with one simple command
- ✅ **Access control** — Choose public, private, or team-only access for each skill

**One agent learns, all agents benefit — collective intelligence at scale.**

### 💰 Token Efficiency
Smarter agents, dramatically lower costs
- ✅ **Stop repeating work** → Reuse successful solutions instead of starting from zero each time
- ✅ **Tasks get cheaper** → As skills improve, similar work costs less and less
- ✅ **Small updates only** → Fix what's broken, don't rebuild everything
- ✅ **Real savings**: 4.2× better performance with 46% fewer tokens on real-world tasks, delivering measurable economic value. ([GDPVal](#-benchmark-gdpval))

Do more, spend less — agents that actually save you money over time.

---

### The Difference

**❌ Current Agents**
- Skills degrade silently as tools evolve
- Failed patterns repeat with no learning mechanism
- Knowledge remains trapped in individual agents

**✅ OpenSpace-Powered Agents**
- Multi-layer monitoring catches problems and auto-triggers repairs
- Successful workflows become reusable, shareable skills
- When one agent learns something useful, all agents get that knowledge instantly

### 📊 OpenSpace: Turn Your Agent into a Money-Making Coworker

**🎯 Real-World Results That Matter**
On 50 professional tasks (**📈 [GDPVal Economic Benchmark](#-benchmark-gdpval)**) across 6 industries, OpenSpace agents earn **4.2× more money** than baseline ([ClawWork](https://github.com/HKUDS/ClawWork)) agents using the same backbone LLM (Qwen 3.5-Plus). While cutting 46% of costly tokens through skill evolution.

<div align="center">
<img src="assets/benchmark_kpi.png" width="100%" alt="GDPVal Benchmark — Key Results" />
</div>

**💼 These Aren't Toy Problems**
- Building payroll calculators from complex union contracts
- Preparing tax returns from 15 scattered PDF documents
- Drafting legal memoranda on California privacy regulations
- Creating compliance forms and engineering specifications

**📈 Consistent Wins Across All Fields**
- Compliance work: +18.5% higher earnings
- Engineering projects: +8.7% better performance
- Professional documents: 56% fewer tokens needed
- Every category improved — no exceptions

<div align="center">
<img src="assets/benchmark_task_showcase.png" width="100%" alt="GDPVal Benchmark — Task Showcase by Category" />
</div>

**OpenSpace doesn't just make agents smarter** — it makes them economically viable. Real work, real money, measurable results.

## Use Case for Autonomous System Development with OpenSpace

**🖥️ [My Daily Monitor](showcase/README.md)** — OpenSpace empowers your agent to complete large-scale system development. This personal behavior monitoring system with 20+ live dashboard panels was built entirely by the agent — 60+ skills evolved from scratch through OpenSpace, demonstrating autonomous end-to-end software development capabilities.

<div align="center">
<img src="assets/my_daily_monitor_dark.png" width="100%" alt="My Daily Monitor – Dark Mode" />
</div>

---

## 📋 Table of Contents

- [⚡ Quick Start](#-quick-start)
  - [🤖 Path A: For Your Agent](#-path-a-for-your-agent)
  - [👤 Path B: As Your Co-Worker](#-path-b-as-your-co-worker)
  - [📊 Local Dashboard](#-local-dashboard)
- [📈 Benchmark: GDPVal](#-benchmark-gdpval)
- [📊 Showcase: My Daily Monitor](#-showcase-my-daily-monitor)
- [🏗️ Framework](#️-framework)
  - [🧬 Self-Evolution Engine](#-self-evolution-engine)
  - [🌐 Cloud Skill Community](#-cloud-skill-community)
- [🔧 Advanced Configuration](#-advanced-configuration)
- [📖 Code Structure](#-code-structure)
- [🤝 Contribute & Roadmap](#-contribute--roadmap)
- [🔗 Related Projects](#-related-projects)

---

## ⚡ Quick Start

🌐 **Just want to explore?** Browse community skills, evolution lineage at **[open-space.cloud](https://open-space.cloud)** — no installation needed.

```bash
git clone https://github.com/HKUDS/OpenSpace.git && cd OpenSpace
pip install -e .
openspace-mcp --help   # verify installation
```

> [!TIP]
> **Slow clone?** The `assets/` folder (~50 MB of images) makes the default clone large. Use this lightweight alternative to skip it:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/HKUDS/OpenSpace.git
> cd OpenSpace
> git sparse-checkout set '/*' '!assets/'
> pip install -e .
> ```

**Choose your path:**
- **[Path A](#-path-a-for-your-agent)** — Plug OpenSpace into your agent
- **[Path B](#-path-b-as-your-co-worker)** — Use OpenSpace directly as your AI co-worker

### 🤖 Path A: For Your Agent

Works with any agent that supports skills (`SKILL.md`) — [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Codex](https://github.com/openai/codex), [OpenClaw](https://github.com/openclaw/openclaw), [nanobot](https://github.com/HKUDS/nanobot), etc.

**① Add OpenSpace to your agent's MCP config:**

```json
{
  "mcpServers": {
    "openspace": {
      "command": "openspace-mcp",
      "toolTimeout": 600,
      "env": {
        "OPENSPACE_HOST_SKILL_DIRS": "/path/to/your/agent/skills",
        "OPENSPACE_WORKSPACE": "/path/to/OpenSpace",
        "OPENSPACE_API_KEY": "sk-xxx (optional, for cloud)"
      }
    }
  }
}
```

> [!TIP]
> Credentials (API key, model) are **auto-detected** from your agent's config; you usually don't need to set them manually.

**② Copy skills** into your agent's skills directory:

```bash
cp -r OpenSpace/openspace/host_skills/delegate-task/ /path/to/your/agent/skills/
cp -r OpenSpace/openspace/host_skills/skill-discovery/ /path/to/your/agent/skills/
```

Done. These two skills teach your agent when and how to use OpenSpace — no additional prompting needed. Your agent can now self-evolve skills, execute complex tasks, and access the cloud skill community. You can also add your own custom skills — see [`openspace/skills/README.md`](openspace/skills/README.md).

> [!NOTE]
> **Cloud community (optional):** Register at **[open-space.cloud](https://open-space.cloud)** to get a `OPENSPACE_API_KEY`, then add it to the `env` block above. Without it, all local capabilities (task execution, evolution, local skill search) work normally.

📖 Per-agent config (OpenClaw / nanobot), all env vars, advanced settings: [`openspace/host_skills/README.md`](openspace/host_skills/README.md)

### 👤 Path B: As Your Co-Worker

Use OpenSpace directly — coding, search, tool use, and more — with self-evolving skills and cloud community built in.

> [!NOTE]
> Create a `.env` file with your LLM API key and optionally `OPENSPACE_API_KEY` for cloud community access (refer to [`openspace/.env.example`](openspace/.env.example)).

```bash
# Interactive mode
openspace

# Execute task
openspace --model "anthropic/claude-sonnet-4-5" --query "Create a monitoring dashboard for my Docker containers"
```

Add your own custom skills: [`openspace/skills/README.md`](openspace/skills/README.md).

**Cloud CLI** — manage skills from the command line:

```bash
openspace-download-skill <skill_id>         # download a skill from the cloud
openspace-upload-skill /path/to/skill/dir   # upload a skill to the cloud
```

<details>
<summary><b>Python API</b></summary>

```python
import asyncio
from openspace import OpenSpace

async def main():
    async with OpenSpace() as cs:
        result = await cs.execute("Analyze GitHub trending repos and create a report")
        print(result["response"])

        for skill in result.get("evolved_skills", []):
            print(f"  Evolved: {skill['name']} ({skill['origin']})")

asyncio.run(main())
```

</details>

### 📊 Local Dashboard

See how your skills evolve — browse skills, track lineage, compare diffs.

> Requires **Node.js ≥ 20**.

```bash
# Terminal 1. Start backend API
openspace-dashboard --port 7788

# Terminal 2: Start frontend dev server
cd frontend
npm install        # only needed once
npm run dev    
```

📖 **Frontend setup guide**: [`frontend/README.md`](frontend/README.md)

<div align="center">
<table>
<tr>
<td width="50%"><img src="assets/frontend_1.gif" width="100%" alt="Skill Classes" /></td>
<td width="50%"><img src="assets/frontend_2.gif" width="100%" alt="Cloud Skill Records" /></td>
</tr>
<tr>
<td align="center"><sub>Skill Classes — Browse, Search & Sort</sub></td>
<td align="center"><sub>Cloud — Browse & Discover Skill Records</sub></td>
</tr>
<tr>
<td width="50%"><img src="assets/frontend_3.gif" width="100%" alt="Version Lineage" /></td>
<td width="50%"><img src="assets/frontend_4.gif" width="100%" alt="Workflow Sessions" /></td>
</tr>
<tr>
<td align="center"><sub>Version Lineage — Skill Evolution Graph</sub></td>
<td align="center"><sub>Workflow Sessions — Execution History & Metrics</sub></td>
</tr>
</table>
</div>

---

## 📈 Benchmark: GDPVal

We evaluate OpenSpace on [GDPVal](https://huggingface.co/datasets/openai/gdpval) — 220 real-world professional tasks spanning 44 occupations — using the [ClawWork](https://github.com/HKUDS/ClawWork) evaluation protocol with identical productivity tools and LLM-based scoring. Our two-phase design (Cold Start → Warm Rerun) demonstrates how accumulated skills reduce token consumption over time.

Fair Benchmark: OpenSpace uses Qwen 3.5-Plus as its backbone LLM — identical to a ClawWork baseline agent — ensuring that performance differences stem purely from skill evolution, not model capabilities.

Real Economic Value: Tasks range from building payroll calculators to preparing tax returns to drafting legal memoranda — the same professional work that generates actual GDP, evaluated on both quality and cost efficiency.

<div align="center">
<img src="assets/benchmark_income.png" width="100%" alt="GDPVal Benchmark — Income Comparison" />
</div>

- **4.2× Higher Income** vs ClawWork with the same backbone LLM (Qwen 3.5-Plus)
- **72.8% Value Capture** — $11,484 earned out of $15,764 task value, outperforming all agents
- **70.8% Average Quality** — +30pp above the best ClawWork agent (40.8%)
− **45.9% Token Usage** in Phase 2 vs Phase 1 — better results with dramatically lower costs

<div align="center">
<img src="assets/benchmark_quality_tokens.png" width="100%" alt="GDPVal Benchmark — Quality & Token Efficiency" />
</div>

### What Real-World Tasks Can OpenSpace Handle?

The 50 GDPVal tasks span 6 real-world work categories. 
- **Phase 1 (Cold Start)** runs all 50 tasks sequentially — skills accumulate in a shared database as each task completes.
- **Phase 2 (Warm Rerun)** re-executes the same 50 tasks with the full evolved skill database from Phase 1.

Income Capture = actual payment earned ÷ maximum possible task value

<div align="center">
<img src="assets/benchmark_task_showcase.png" width="100%" alt="GDPVal Benchmark — Task Showcase by Category" />
</div>

## 🎯 Where Evolution Delivers Maximum Impact — And Why:

| Category | Income Δ | Token Δ | Why |
|---|---|---|---|
| **📝 Documents & Correspondence** (7) | 71→74% (+3.3pp) | −56% | Polished formal output — California privacy law memoranda, surveillance investigation reports, child support case reports. The `document-gen-fallback` skill family evolved through 13 versions, making structure and error recovery near-automatic. |
| **📋 Compliance & Form** (11) | 51→70% (+18.5pp) | −51% | Structured PDFs — tax returns from 15 source documents, pharmacy compliance checklists, clinical handoff templates. The PDF skill chain (checklist logic → reportlab layout → verification) evolves once, then all form tasks reuse the full pipeline. |
| **🎬 Media Production** (3) | 53→58% (+5.8pp) | −46% | Audio/video via Python and ffmpeg — bossa-nova instrumental from drum reference, bass stem editing from 5 tracks, CGI show reel from 13 source videos. Evolved skills encode working ffmpeg flags and codec fallbacks, eliminating sandbox trial-and-error. |
| **🛠️ Engineering** (4) | 70→78% (+8.7pp) | −43% | Multi-deliverable technica
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

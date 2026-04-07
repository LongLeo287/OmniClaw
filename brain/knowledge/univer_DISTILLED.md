---
id: univer
type: knowledge
owner: OA_Triage
---
# univer
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
    "name": "univer",
    "type": "module",
    "version": "0.20.0",
    "private": true,
    "packageManager": "pnpm@10.32.1",
    "author": "DreamNum Co., Ltd. <developer@univer.ai>",
    "license": "Apache-2.0",
    "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/univer"
    },
    "homepage": "https://univer.ai",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer"
    },
    "bugs": {
        "url": "https://github.com/dream-num/univer/issues"
    },
    "devEngines": {
        "runtime": [
            {
                "name": "node",
                "version": ">=22.18"
            },
            {
                "name": "pnpm",
                "version": ">=10"
            }
        ]
    },
    "scripts": {
        "prepare": "husky",
        "pre-commit": "lint-staged",
        "dev": "pnpm --filter univer-examples dev:demo -- --host 0.0.0.0",
        "dev:umd": "serve .",
        "dev:e2e": "pnpm --filter univer-examples dev:e2e",
        "use:react16": "tsx ./scripts/react-version-manager.ts --react=16",
        "use:react19": "tsx ./scripts/react-version-manager.ts --react=19",
        "typecheck": "turbo typecheck",
        "serve:umd": "serve .",
        "test": "turbo test -- --passWithNoTests",
        "coverage": "turbo coverage -- --passWithNoTests",
        "analyze:build": "tsx ./scripts/build-analysis.ts",
        "build": "turbo build --filter=!./common/*",
        "build:ci": "turbo build --filter=!./common/*",
        "build:demo": "pnpm --filter univer-examples build:demo",
        "build:e2e": "pnpm --filter univer-examples build:e2e",
        "serve:e2e": "serve ./examples/local",
        "test:e2e": "playwright test",
        "lint": "eslint .",
        "storybook:dev": "pnpm --filter @univerjs/storybook dev:storybook",
        "storybook:build": "pnpm --filter @univerjs/storybook build:storybook",
        "release": "release-it"
    },
    "devDependencies": {
        "@antfu/eslint-config": "^7.7.3",
        "@commitlint/cli": "^20.5.0",
        "@commitlint/config-conventional": "^20.5.0",
        "@eslint-react/eslint-plugin": "^2.13.0",
        "@eslint/compat": "^2.0.3",
        "@playwright/test": "^1.57.0",
        "@release-it-plugins/workspaces": "^5.0.3",
        "@release-it/conventional-changelog": "^10.0.6",
        "@types/fs-extra": "^11.0.4",
        "@types/node": "^25.5.0",
        "@types/react": "19.2.14",
        "@types/react-dom": "19.2.3",
        "@univerjs-infra/shared": "workspace:*",
        "@univerjs/design": "workspace:*",
        "eslint": "10.1.0",
        "eslint-plugin-format": "^2.0.1",
        "eslint-plugin-react": "^7.37.5",
        "eslint-plugin-react-hooks": "7.0.1",
        "eslint-plugin-react-refresh": "^0.5.2",
        "fs-extra": "^11.3.4",
        "husky": "^9.1.7",
        "lint-staged": "^16.4.0",
        "posthog-node": "^5.28.5",
        "react": "19.2.4",
        "react-dom": "19.2.4",
        "release-it": "^19.2.4",
        "serve": "^14.2.6",
        "tailwindcss": "3.4.18",
        "tsx": "^4.21.0",
        "turbo": "^2.8.20",
        "typescript": "^6.0.2",
        "vitest": "^4.1.1"
    },
    "pnpm": {
        "overrides": {
            "@types/react": "19.2.14",
            "@types/react-dom": "19.2.3",
            "basic-ftp": "5.2.0",
            "react": "19.2.4",
            "react-dom": "19.2.4"
        }
    },
    "lint-staged": {
        "*": "eslint --fix"
    }
}

```

### File: README.md
```md
<div align="center">

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./docs/img/banner-light.png">
    <img src="./docs/img/banner-dark.png" alt="Univer" width="400" />
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
  - ✏️ Univer boasts an efficient *rendering engine* based on canvas, capable of rendering various document types flawlessly. The rendering engines supports advanced typesetting features such as *punctuation squeezing*, *text and image layout* and *scroll buffering*.
  - 🧮 Univer incorporates a lightning-fast *formula engine* that can operate in Web Workers or even on the server side.
- 🌌 Univer is a **highly integrated** system. Documents, spreadsheets and slides can interoperate with each others and even rendered on the same canvas, allowing information and data flow within Univer.

## ✨ Features

Univer provides a wide range of features for spreadsheets, documents and presentations. Here are some of the key features:

### 📊 Univer Sheets

- **Core Features**: Univer supports core spreadsheet functionality, including cells, rows, columns, worksheets, and workbooks.
- **Formulas**: Extensive support for various formulas, including mathematical, statistical, logical, text, date and time, lookup and reference, engineering, financial, and information formulas.
- **Permissions**: Allows restricting access to specific elements.
- **Number Formatting**: Supports formatting numbers based on specific criteria.
- **Hyperlinks**: Enables linking to external websites, email addresses, and other locations within a spreadsheet.
- **Floating Images**: Allows inserting images into a spreadsheet and positioning them anywhere on the sheet.
- **Find & Replace**: Provides the ability to search for specific text within a spreadsheet and replace it with other text.
- **Filtering**: Allows filtering data based on specific criteria.
- **Sorting**: Allows sorting data based on specific criteria.
- **Data Validation**: Supports restricting the type of data that can be entered into a cell.
- **Conditional Formatting**: Supports applying formatting to cells based on specific criteria.
- **Comments**: Enables adding comments to cells to provide additional information.
- **Cross-highlighting**: Supports displaying cross-highlighting in spreadsheets to help users quickly locate selected cells.
- **Zen Editor**: Provides a distraction-free editing experience with a clean interface and minimal distractions.
- **Pivot Tables**[^1]: Supports pivot tables, allowing users to summarize and analyze data.
- **Sparklines**[^1]: Supports sparklines, which are small charts that fit within a cell to provide a visual representation of data.
- **Printing**[^1]: Allows printing a spreadsheet or exporting it to PDF.
- **Import & Export**[^1]: Support for importing and exporting data in XLSX.
- **Charts**[^1]: Supports various types of charts, including bar charts, line charts, pie charts, scatter plots, and more.
- **Collaborative Editing**[^1]: Supports multiple users editing a spreadsheet simultaneously. File history and recovering are also provided.
- **Editing History**[^1]: Allows users to view and restore previous versions of a spreadsheet.

### 📝 Univer Docs (rc)

- **Core Features**: Univer supports core document features, including paragraphs, headings, lists, superscript, subscript, and more.
- **Lists**: Supports ordered lists, unordered lists, and task lists.
- **Hyperlinks**: Supports inserting links to external websites, email addresses, and other locations within a document.
- **Floating Images**: Allows inserting images into a document and supporting text and image layout.
- **Headers & Footers**: Allows adding headers and footers to a document.
- **Comments**: Enables adding comments to a document to provide additional information.
- **Printing**[^1]: Allows printing a document or exporting it to PDF.
- **Import & Export**[^1]: Supports importing and exporting data in DOCX format.
- **Collaborative Editing**[^1]: Supports multiple users editing a document simultaneously.

### 📽️ Univer Slides (Under Development)

- **Core Features**: Univer will support core presentation features, including slides, shapes, text, images, and more.

## 🌐 Internationalization

Univer supports multiple languages, including:

- `ca-ES`
- `en-US`
- `es-ES`
- `fa-IR`
- `ja-JP`
- `ko-KR`
- `ru-RU`
- `sk-SK`
- `vi-VN`
- `zh-CN`
- `zh-TW`

`zh-CN` and `en-US` are officially supported, while the others are contributed and maintained by the community.

You can add the language you want by [Using Custom Locales](https://docs.univer.ai/guides/sheets/getting-started/i18n#custom-language-packs). You can also help us add new language support by referring to the [contribution guide](./CONTRIBUTING.md).

## 👾 Showcase

Embed Univer in AI products as a data presentation tool.

[![][examples-preview-capalyze]][examples-link-capalyze]

You can find all the examples in the [Univer Examples](https://docs.univer.ai/showcase).

| **📊 Spreadsheets** | **📊 Multi-instance** | **📊 Uniscript** |
| :---: | :---: | :---: |
| [![][examples-preview-0]][examples-link-0] | [![][examples-preview-1]][examples-link-1] | [![][examples-preview-2]][examples-link-2] |
| **📊 Big data** | **📊 Collaboration** | **📊 Collaboration Playground** |
| [![][examples-preview-3]][examples-link-3] | [![][examples-preview-4]][examples-link-4] | [![][examples-preview-5]][examples-link-5] |
| **📊 Import & Export** | **📊 Printing** | **📝 Documents** |
| [![][examples-preview-6]][examples-link-6] | [![][examples-preview-7]][examples-link-7] | [![][examples-preview-8]][examples-link-8] |
| **📝 Multi-instance** | **📝 Uniscript** | **📝 Big data** |
| [![][examples-preview-9]][examples-link-9] | [![][examples-preview-10]][examples-link-10] | [![][examples-preview-11]][examples-link-11] |
| **📝 Collaboration** | **📝 Collaboration Playground** | **📽️ Presentations** |
| [![][examples-preview-12]][examples-link-12] | [![][examples-preview-13]][examples-link-13] | [![][examples-preview-14]][examples-link-14] |
| **📊 Zen Editor** | **Univer Workspace (SaaS version)** | &nbsp; |
| [![][examples-preview-15]][examples-link-15] | [![][examples-preview-16]][examples-link-16] | &nbsp; |

<!-- ## 📦 Ecosystem

Univer has a rich ecosystem that includes a wide range of tools and resources to help you get started with Univer: -->

## 🔗 Links

- [Latest Preview of the `dev` Branch](https://univer-preview.vercel.app/)
- [Official Site](https://univer.ai)
- [Presets Repository](https://github.com/dream-num/univer-presets)

## 🔒 Security

Univer is committed to maintaining a secure codebase. We follow best practices for security and regularly update our dependencies. For more information, please refer to our [Security Policy](./SECURITY.md).

## 💬 Community

[![][github-community-badge]][github-community-link] [![][discord-community-badge]][discord-community-link] [![][stackoverflow-community-badge]][stackoverflow-community-link]

Univer is an inclusive and welcoming project. Please read our [Code of Conduct](./CODE_OF_CONDUCT.md) before participating in the community.

Join the Univer community:

- Chat with us and other developers on [Discord][discord-community-link].
- Start a discussion on [GitHub Discussions][github-community-link].
- Open a topic on [Stack Overflow][stackoverflow-community-link] and tag it with `univer`.

You can also find Univer on:

[Twitter][twitter-community-link] | [YouTube][youtube-community-link]

## 🤝 Contribution

We appreciate any kinds of contributing. You can submit [issues or feature requests](https://github.com/dream-num/univer/issues) to us. Please read our [contributing guide](./CONTRIBUTING.md) first.

If you would like to contribute code to Univer, please refer to the contributing guide as well. It would guide you through the process of setting up the development environment and submitting a pull request.

## ❤️ Sponsors

The growth and development of the Univer project rely on the support of its backers and sponsors. If you are interested in supporting our project, we kindly invite you to consider becoming a sponsor. You can sponsor us through [Open Collective](https://opencollective.com/univer).

Thanks to our sponsors, just part of them are listed here because of the space limit, ranking is no particular order:

[![][sponsor-badge-0]][sponsor-link-0]
[![][sponsor-badge-1]][sponsor-link-1]
[![][sponsor-badge-2]][sponsor-link-2]
[![][sponsor-badge-3]][sponsor-link-3]
[![][sponsor-badge-4]][sponsor-link-4]
[![][sponsor-badge-5]][sponsor-link-5]
[![][sponsor-badge-6]][sponsor-link-6]

[![][backer-badge-0]][backer-link-0]
[![][backer-badge-1]][backer-link-1]
[![][backer-badge-2]][backer-link-2]
[![][backer-badge-3]][backer-link-3]
[![][backer-badge-4]][backer-link-4]
[![][backer-badge-5]][backer-link-5]
[![][backer-badge-6]][backer-link-6]

## 📄 License

Copyright © 2021-2025 DreamNum Co,Ltd. All Rights Reserved.

Licensed under the [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) license.

<!-- Footnotes -->
[^1]: These features are provided by the non-OSS version of Univer, which is free for commercial use and also includes paid upgrade plans.

<!-- Links -->
[github-license-shield]: https://img.shields.io/github/license/dream-num/univer?style=flat-square
[github-license-link]: ./LICENSE
[github-actions-shield]: https://img.shields.io/github/actions/workflow/status/dream-num/univer/build.yml?style=flat-square
[github-actions-link]: https://github.com/dream-num/univer/actions/workflows/build.yml
[github-stars-link]: https://github.com/dream-num/univer/stargazers
[github-stars-shield]: https://img.shields.io/github/stars/dream-num/univer?style=flat-square
[github-trending-shield]: https://trendshift.io/api/badge/repositories/4376
[github-trending-url]: https://trendshift.io/repositories/4376
[github-contributors-link]: https://github.com/dream-num/univer/graphs/contributors
[github-contributors-shield]: https://img.shields.io/github/contributors/dream-num/univer?style=flat-square
[github-forks-link]: https://github.com/dream-num/univer/network/members
[github-forks-shield]: https://img.shields.io/github/forks/dream-num/univer?style=flat-square
[github-issues-link]: https://github.com/dream-num/univer/issues
[github-issues-shield]: https://img.shields.io/github/issues/dream-num/univer?style=flat-square
[codecov-shield]: https://img.shields.io/codecov/c/gh/dream-num/univer?token=aPfyW2pIMN&style=flat-square
[codecov-link]: https://codecov.io/gh/dream-num/univer
[codefactor-shield]: https://www.codefactor.io/repository/github/dream-num/univer/badge/dev?style=flat-square
[codefactor-link]: https://www.codefactor.io/repository/github/dream-num/univer/overview/dev
[discord-shield]: https://img.shields.io/discord/1136129819961217077?logo=discord&logoColor=FFFFFF&label=discord&color=5865F2&style=flat-square
[discord-link]: https://discord.gg/z3NKNT6D2f

[readme-en-link]: ./README.md
[readme-zh-link]: ./README-zh.md
[readme-ja-link]: ./README-ja.md
[readme-es-link]: ./README-es.md

[official-site-link]: https://univer.ai
[documentation-link]: https://docs.univer.ai/en-US
[playground-link]: https://docs.univer.ai/en-US/showcase
[blog-link]: https://docs.univer.ai/en-US/blog

[stackoverflow-community-link]: https://stackoverflow.com/questions/tagged/univer
[stackoverflow-community-badge]: https://img.shields.io/badge/stackoverflow-univer-ef8236?labelColor=black&logo=stackoverflow&logoColor=white&style=for-the-badge
[github-community-link]: https://github.com/dream-num/univer/discussions
[github-community-badge]: https://img.shields.io/badge/github-univer-24292e?labelColor=black&logo=github&logoColor=white&style=for-the-badge
[discord-community-link]: https://discord.gg/z3NKNT6D2f
[discord-community-badge]: https://img.shields.io/discord/1136129819961217077?color=5865F2&label=discord&labelColor=black&logo=discord&logoColor=white&style=for-the-badge
[twitter-community-link]: https://twitter.com/univerhq
[youtube-community-link]: https://www.youtube.com/@dreamNum
[zhihu-community-link]: https://www.zhihu.com/org/meng-shu-ke-ji
[segmentfault-community-link]: https://segmentfault.com/u/congrongdehongjinyu
[juejin-community-link]: https://juejin.cn/user/4312146127850733

[sponsor-link-0]: https://opencollective.com/univer/sponsor/0/website
[sponsor-link-1]: https://opencolle
... [TRUNCATED]
```

### File: examples\package.json
```json
{
    "name": "univer-examples",
    "private": true,
    "description": "Univer vanilla ts demo project",
    "author": "DreamNum <developer@univer.ai>",
    "license": "Apache-2.0",
    "exports": {
        "./*": "./src/*"
    },
    "scripts": {
        "prepare": "tsx ./scripts/sync-demos.ts",
        "build:demo": "tsx ./esbuild.config.ts",
        "dev:demo": "tsx ./esbuild.config.ts --watch",
        "dev:e2e": "tsx ./esbuild.config.ts --watch --e2e",
        "build:e2e": "tsx ./esbuild.config.ts --e2e",
        "typecheck": "tsc --noEmit"
    },
    "dependencies": {
        "@lit/react": "^1.0.8",
        "@univerjs/action-recorder": "workspace:*",
        "@univerjs/core": "workspace:*",
        "@univerjs/data-validation": "workspace:*",
        "@univerjs/debugger": "workspace:*",
        "@univerjs/design": "workspace:*",
        "@univerjs/docs": "workspace:*",
        "@univerjs/docs-drawing": "workspace:*",
        "@univerjs/docs-drawing-ui": "workspace:*",
        "@univerjs/docs-hyper-link-ui": "workspace:*",
        "@univerjs/docs-mention-ui": "workspace:*",
        "@univerjs/docs-quick-insert-ui": "workspace:*",
        "@univerjs/docs-thread-comment-ui": "workspace:*",
        "@univerjs/docs-ui": "workspace:*",
        "@univerjs/drawing": "workspace:*",
        "@univerjs/drawing-ui": "workspace:*",
        "@univerjs/engine-formula": "workspace:*",
        "@univerjs/engine-render": "workspace:*",
        "@univerjs/find-replace": "workspace:*",
        "@univerjs/icons": "1.1.1",
        "@univerjs/mockdata": "workspace:*",
        "@univerjs/network": "workspace:*",
        "@univerjs/rpc": "workspace:*",
        "@univerjs/rpc-node": "workspace:*",
        "@univerjs/sheets": "workspace:*",
        "@univerjs/sheets-conditional-formatting": "workspace:*",
        "@univerjs/sheets-conditional-formatting-ui": "workspace:*",
        "@univerjs/sheets-crosshair-highlight": "workspace:*",
        "@univerjs/sheets-data-validation": "workspace:*",
        "@univerjs/sheets-data-validation-ui": "workspace:*",
        "@univerjs/sheets-drawing": "workspace:*",
        "@univerjs/sheets-drawing-ui": "workspace:*",
        "@univerjs/sheets-filter": "workspace:*",
        "@univerjs/sheets-filter-ui": "workspace:*",
        "@univerjs/sheets-find-replace": "workspace:*",
        "@univerjs/sheets-formula": "workspace:*",
        "@univerjs/sheets-formula-ui": "workspace:*",
        "@univerjs/sheets-hyper-link": "workspace:*",
        "@univerjs/sheets-hyper-link-ui": "workspace:*",
        "@univerjs/sheets-note": "workspace:*",
        "@univerjs/sheets-note-ui": "workspace:*",
        "@univerjs/sheets-numfmt": "workspace:*",
        "@univerjs/sheets-numfmt-ui": "workspace:*",
        "@univerjs/sheets-sort": "workspace:*",
        "@univerjs/sheets-sort-ui": "workspace:*",
        "@univerjs/sheets-table": "workspace:*",
        "@univerjs/sheets-table-ui": "workspace:*",
        "@univerjs/sheets-thread-comment": "workspace:*",
        "@univerjs/sheets-thread-comment-ui": "workspace:*",
        "@univerjs/sheets-ui": "workspace:*",
        "@univerjs/sheets-zen-editor": "workspace:*",
        "@univerjs/slides": "workspace:*",
        "@univerjs/slides-ui": "workspace:*",
        "@univerjs/themes": "workspace:*",
        "@univerjs/thread-comment": "workspace:*",
        "@univerjs/thread-comment-ui": "workspace:*",
        "@univerjs/ui": "workspace:*",
        "@univerjs/ui-adapter-vue3": "workspace:*",
        "@univerjs/ui-adapter-web-component": "workspace:*",
        "@univerjs/uniscript": "workspace:*",
        "@univerjs/watermark": "workspace:*",
        "lit": "^3.3.2",
        "monaco-editor": "0.55.1",
        "react": "19.2.4",
        "react-dom": "19.2.4",
        "react-mosaic-component": "^6.1.1",
        "rxjs": "^7.8.2"
    },
    "devDependencies": {
        "@types/fs-extra": "^11.0.4",
        "@types/minimist": "^1.2.5",
        "@univerjs-infra/shared": "workspace:*",
        "detect-port": "^2.1.0",
        "esbuild": "^0.27.3",
        "esbuild-plugin-alias": "^0.2.1",
        "esbuild-plugin-clean": "^1.0.1",
        "esbuild-plugin-copy": "^2.1.1",
        "esbuild-plugin-vue3": "^0.5.1",
        "esbuild-style-plugin": "^1.6.3",
        "fs-extra": "^11.3.4",
        "minimist": "^1.2.8",
        "postcss": "^8.5.8",
        "tailwindcss": "3.4.18",
        "tailwindcss-animate": "^1.0.7",
        "typescript": "^6.0.2"
    }
}

```

### File: common\shared\package.json
```json
{
    "name": "@univerjs-infra/shared",
    "type": "module",
    "version": "0.20.0",
    "private": true,
    "description": "Some infrastructures for univerjs",
    "author": "DreamNum <developer@univer.ai>",
    "license": "Apache-2.0",
    "homepage": "https://github.com/dream-num/univer",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer.git"
    },
    "keywords": [],
    "exports": {
        "./eslint": "./eslint/index.ts",
        "./tsconfigs/*": "./tsconfigs/*.json",
        "./vitest": "./vitest/index.ts",
        "./esbuild": "./esbuild/index.ts",
        "./tailwind": "./tailwind/tailwind.config.ts",
        "./postcss": "./postcss/postcss.config.mjs",
        "./tsdown": "./tsdown/index.ts"
    },
    "main": "bin/index.ts",
    "bin": {
        "univer-cli": "bin/index.ts"
    },
    "scripts": {
        "typecheck": "tsc --noEmit"
    },
    "dependencies": {
        "@tsdown/css": "^0.21.4",
        "@typescript-eslint/parser": "^8.57.2",
        "@vitest/coverage-istanbul": "^4.1.1",
        "autoprefixer": "^10.4.27",
        "eslint-plugin-better-tailwindcss": "^4.3.2",
        "eslint-plugin-header": "^3.1.1",
        "eslint-plugin-no-barrel-import": "^0.0.2",
        "eslint-plugin-no-penetrating-import": "^0.0.1",
        "fs-extra": "^11.3.4",
        "happy-dom": "20.8.7",
        "javascript-obfuscator": "^5.4.1",
        "postcss-preset-env": "^11.2.0",
        "postcss-replace": "^2.0.1",
        "sort-keys": "^6.0.0",
        "tailwind-scrollbar": "^3",
        "tailwindcss": "3.4.18",
        "tsdown": "^0.21.4",
        "unplugin-vue": "^7.1.1",
        "vitest": "^4.1.1"
    },
    "devDependencies": {
        "@types/fs-extra": "^11.0.4",
        "@univerjs/icons": "^1.1.1",
        "@univerjs/icons-svg": "^1.1.1",
        "@univerjs/protocol": "0.1.48",
        "typescript": "^6.0.2",
        "vue-tsc": "^3.2.6"
    }
}

```

### File: packages\core\package.json
```json
{
    "name": "@univerjs/core",
    "version": "0.20.0",
    "private": false,
    "description": "Core library for Univer.",
    "author": "DreamNum <developer@univer.ai>",
    "license": "Apache-2.0",
    "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/univer"
    },
    "homepage": "https://univer.ai",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer"
    },
    "bugs": {
        "url": "https://github.com/dream-num/univer/issues"
    },
    "keywords": [
        "univer"
    ],
    "exports": {
        ".": "./src/index.ts",
        "./*": "./src/*",
        "./facade": "./src/facade/index.ts"
    },
    "main": "./src/index.ts",
    "types": "./lib/types/index.d.ts",
    "publishConfig": {
        "access": "public",
        "main": "./lib/es/index.js",
        "module": "./lib/es/index.js",
        "exports": {
            ".": {
                "import": "./lib/es/index.js",
                "require": "./lib/cjs/index.js",
                "types": "./lib/types/index.d.ts"
            },
            "./*": {
                "import": "./lib/es/*",
                "require": "./lib/cjs/*",
                "types": "./lib/types/index.d.ts"
            },
            "./facade": {
                "import": "./lib/es/facade.js",
                "require": "./lib/cjs/facade.js",
                "types": "./lib/types/facade/index.d.ts"
            },
            "./lib/facade": {
                "import": "./lib/es/facade.js",
                "require": "./lib/cjs/facade.js",
                "types": "./lib/types/facade/index.d.ts"
            },
            "./lib/*": "./lib/*"
        }
    },
    "directories": {
        "lib": "lib"
    },
    "files": [
        "lib"
    ],
    "scripts": {
        "test": "vitest run",
        "test:watch": "vitest",
        "coverage": "vitest run --coverage",
        "typecheck": "tsc --noEmit",
        "build:bundle": "univer-cli build",
        "build:types": "tsc -p tsconfig.node.json",
        "build": "pnpm run build:bundle && pnpm run build:types"
    },
    "peerDependencies": {
        "rxjs": ">=7.0.0"
    },
    "dependencies": {
        "@univerjs/protocol": "0.1.48",
        "@univerjs/themes": "workspace:*",
        "@wendellhu/redi": "1.1.1",
        "async-lock": "^1.4.1",
        "dayjs": "^1.11.20",
        "fast-diff": "1.3.0",
        "kdbush": "^4.0.2",
        "lodash-es": "^4.17.23",
        "nanoid": "5.1.7",
        "numfmt": "^3.2.3",
        "ot-json1": "^1.0.2",
        "rbush": "^4.0.1"
    },
    "devDependencies": {
        "@types/async-lock": "^1.4.2",
        "@types/lodash-es": "^4.17.12",
        "@types/rbush": "^4.0.0",
        "@univerjs-infra/shared": "workspace:*",
        "rxjs": "^7.8.2",
        "typescript": "^6.0.2",
        "vitest": "^4.1.1"
    }
}

```

### File: packages\core\README.md
```md
# @univerjs/core

## Package Overview

| Package Name | UMD Namespace | Version | License | Downloads | Contains CSS | Contains i18n locales |
| --- | --- | --- | --- | --- | :---: | :---: |
| `@univerjs/core` | `UniverCore` | [![][npm-version-shield]][npm-version-link] | ![][npm-license-shield] | ![][npm-downloads-shield] | ❌ | ❌ |

## Introduction

`@univerjs/core` as its name shows, is the core package of Univer, and provides foundational capabilities including:

* Provision of the Univer type, which serves as the entry point for applications and a mounting point for other plugins, as well as the UniverDoc and UniverSheet types for managing different document types
* Basic models for each document type
* Definition or implementation of several fundamental services, such as:
  * Permission control
  * Command system
  * Undo/Redo
  * Configuration system
  * Logging system
  * Context system
  * Lifecycle
  * Local storage
  * Internationalization
  * Resource management

For more information about `@univerjs/core`'s API, please refer to the [API documentation](https://reference.univer.ai/).

## Usage

### Installation

```shell
# Using npm
npm install @univerjs/core

# Using pnpm
pnpm add @univerjs/core
```

### Configuration

```typescript
import { Univer } from '@univerjs/core';

new Univer({
    theme: defaultTheme,
    locale: LocaleType.EN_US,
    locales,
    logLevel: LogLevel.VERBOSE,
});
```

#### Options

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| theme | [Theme](https://docs.univer.ai/guides/sheets/ui/themes) | - | The theme of the application, which is used to control the appearance of the application. |
| locale | [LocaleType](https://docs.univer.ai/guides/sheets/getting-started/i18n) | `LocaleType.ZH_CN` | The locale of the application. The default value is `LocaleType.ZH_CN`.
| locales | [ILocales](https://docs.univer.ai/guides/sheets/getting-started/i18n) | - | The supported locales of the application. By default, the application supports Chinese.
| logLevel | [LogLevel](https://github.com/dream-num/univer/blob/dev/packages/core/src/services/log/log.service.ts#L22) | `LogLevel.SILENT` | The log level of the application. |

<!-- Links -->
[npm-version-shield]: https://img.shields.io/npm/v/@univerjs/core?style=flat-square
[npm-version-link]: https://npmjs.com/package/@univerjs/core
[npm-license-shield]: https://img.shields.io/npm/l/@univerjs/core?style=flat-square
[npm-downloads-shield]: https://img.shields.io/npm/dm/@univerjs/core?style=flat-square

```

### File: packages\design\package.json
```json
{
    "name": "@univerjs/design",
    "version": "0.20.0",
    "private": false,
    "description": "UI component library for building exceptional Univer.",
    "author": "DreamNum <developer@univer.ai>",
    "license": "Apache-2.0",
    "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/univer"
    },
    "homepage": "https://univer.ai",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer"
    },
    "bugs": {
        "url": "https://github.com/dream-num/univer/issues"
    },
    "keywords": [
        "univer"
    ],
    "exports": {
        ".": "./src/index.ts",
        "./*": "./src/*",
        "./locale/*": "./src/locale/*.ts"
    },
    "main": "./src/index.ts",
    "types": "./lib/types/index.d.ts",
    "publishConfig": {
        "access": "public",
        "main": "./lib/es/index.js",
        "module": "./lib/es/index.js",
        "exports": {
            ".": {
                "import": "./lib/es/index.js",
                "require": "./lib/cjs/index.js",
                "types": "./lib/types/index.d.ts"
            },
            "./*": {
                "import": "./lib/es/*",
                "require": "./lib/cjs/*",
                "types": "./lib/types/index.d.ts"
            },
            "./locale/*": {
                "import": "./lib/es/locale/*.js",
                "require": "./lib/cjs/locale/*.js",
                "types": "./lib/types/locale/*.d.ts"
            },
            "./lib/*": "./lib/*"
        }
    },
    "directories": {
        "lib": "lib"
    },
    "files": [
        "lib"
    ],
    "scripts": {
        "test": "vitest run",
        "test:watch": "vitest",
        "coverage": "vitest run --coverage",
        "typecheck": "tsc --noEmit",
        "build:bundle": "univer-cli build",
        "build:types": "tsc -p tsconfig.node.json",
        "build": "pnpm run build:bundle && pnpm run build:types"
    },
    "peerDependencies": {
        "react": "^16.9.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc",
        "react-dom": "^16.9.0 || ^17.0.0 || ^18.0.0 || ^19.0.0 || ^19.0.0-rc"
    },
    "dependencies": {
        "@radix-ui/react-dialog": "^1.1.15",
        "@radix-ui/react-dropdown-menu": "^2.1.16",
        "@radix-ui/react-hover-card": "^1.1.15",
        "@radix-ui/react-popover": "^1.1.15",
        "@radix-ui/react-separator": "^1.1.8",
        "@radix-ui/react-slot": "^1.2.4",
        "@univerjs/icons": "^1.1.1",
        "class-variance-authority": "^0.7.1",
        "clsx": "^2.1.1",
        "dayjs": "^1.11.20",
        "react-transition-group": "^4.4.5",
        "sonner": "^2.0.7",
        "tailwind-merge": "2.6.0"
    },
    "devDependencies": {
        "@testing-library/jest-dom": "6.9.1",
        "@testing-library/react": "^16.3.2",
        "@types/react-transition-group": "^4.4.12",
        "@univerjs-infra/shared": "workspace:*",
        "postcss": "^8.5.8",
        "react": "18.3.1",
        "react-dom": "18.3.1",
        "tailwindcss": "3.4.18",
        "tailwindcss-animate": "^1.0.7",
        "typescript": "^6.0.2",
        "vitest": "^4.1.1"
    }
}

```

### File: packages\design\README.md
```md
# @univerjs/design

## Package Overview

| Package Name | UMD Namespace | Version | License | Downloads | Contains CSS | Contains i18n locales |
| --- | --- | --- | --- | --- | :---: | :---: |
| `@univerjs/design` | `UniverDesign` | [![][npm-version-shield]][npm-version-link] | ![][npm-license-shield] | ![][npm-downloads-shield] | ⭕️ | ⭕️ |

## Introduction

To ensure better consistency in the UI of Univer plugins and to reduce the effort required for custom development, we provide some fundamental design guidelines and components.

The components are developed using React and less, and you can find out more information by visiting the [component library website](https://univer-design.vercel.app).

![](./assets/design.jpeg)

:::note
If you only need to extend the toolbar, context menu, and so on, you can directly use the extension interfaces provided by `@univerjs/ui` without implementing the UI yourself. For more information, please refer to [Extending UI](https://docs.univer.ai/guides/recipes/tutorials/custom-plugin).
:::

## Usage

### Installation

```shell
# Using npm
npm install @univerjs/design

# Using pnpm
pnpm add @univerjs/design
```

This package contains CSS and has the highest priority. Please import it before importing any other Univer style files.

<!-- Links -->
[npm-version-shield]: https://img.shields.io/npm/v/@univerjs/design?style=flat-square
[npm-version-link]: https://npmjs.com/package/@univerjs/design
[npm-license-shield]: https://img.shields.io/npm/l/@univerjs/design?style=flat-square
[npm-downloads-shield]: https://img.shields.io/npm/dm/@univerjs/design?style=flat-square

```

### File: packages\docs\package.json
```json
{
    "name": "@univerjs/docs",
    "version": "0.20.0",
    "private": false,
    "description": "UniverSheet normal base-docs",
    "author": "DreamNum <developer@univer.ai>",
    "license": "Apache-2.0",
    "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/univer"
    },
    "homepage": "https://univer.ai",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer"
    },
    "bugs": {
        "url": "https://github.com/dream-num/univer/issues"
    },
    "keywords": [
        "univer"
    ],
    "exports": {
        ".": "./src/index.ts",
        "./*": "./src/*"
    },
    "main": "./src/index.ts",
    "types": "./lib/types/index.d.ts",
    "publishConfig": {
        "access": "public",
        "main": "./lib/es/index.js",
        "module": "./lib/es/index.js",
        "exports": {
            ".": {
                "import": "./lib/es/index.js",
                "require": "./lib/cjs/index.js",
                "types": "./lib/types/index.d.ts"
            },
            "./*": {
                "import": "./lib/es/*",
                "require": "./lib/cjs/*",
                "types": "./lib/types/index.d.ts"
            },
            "./lib/*": "./lib/*"
        }
    },
    "directories": {
        "lib": "lib"
    },
    "files": [
        "lib"
    ],
    "scripts": {
        "test": "vitest run",
        "test:watch": "vitest",
        "coverage": "vitest run --coverage",
        "typecheck": "tsc --noEmit",
        "build:bundle": "univer-cli build",
        "build:types": "tsc -p tsconfig.node.json",
        "build": "pnpm run build:bundle && pnpm run build:types"
    },
    "peerDependencies": {
        "rxjs": ">=7.0.0"
    },
    "dependencies": {
        "@univerjs/core": "workspace:*",
        "@univerjs/engine-render": "workspace:*"
    },
    "devDependencies": {
        "@univerjs-infra/shared": "workspace:*",
        "rxjs": "^7.8.2",
        "typescript": "^6.0.2",
        "vitest": "^4.1.1"
    }
}

```

### File: packages\docs\README.md
```md
# @univerjs/docs

## Package Overview

| Package Name | UMD Namespace | Version | License | Downloads | Contains CSS | Contains i18n locales |
| --- | --- | --- | --- | --- | :---: | :---: |
| `@univerjs/docs` | `UniverDocs` | [![][npm-version-shield]][npm-version-link] | ![][npm-license-shield] | ![][npm-downloads-shield] | ❌ | ❌ |

## Introduction

`@univerjs/docs` package provides the fundamental operations for rich text models, including the following capabilities:

* Logic for selection areas
* Commands/mutations for altering rich text data
* Canvas rendering for document presentation

Additionally, `@univerjs/docs` offers support for editors in other domains, such as cell editors for spreadsheets and formula editors, among others.

## Usage

### Installation

```shell
# Using npm
npm install @univerjs/docs

# Using pnpm
pnpm add @univerjs/docs
```

<!-- Links -->
[npm-version-shield]: https://img.shields.io/npm/v/@univerjs/docs?style=flat-square
[npm-version-link]: https://npmjs.com/package/@univerjs/docs
[npm-license-shield]: https://img.shields.io/npm/l/@univerjs/docs?style=flat-square
[npm-downloads-shield]: https://img.shields.io/npm/dm/@univerjs/docs?style=flat-square

```

### File: packages\sheets\package.json
```json
{
    "name": "@univerjs/sheets",
    "version": "0.20.0",
    "private": false,
    "description": "UniverSheet normal base-sheets",
    "author": "DreamNum <developer@univer.ai>",
    "license": "Apache-2.0",
    "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/univer"
    },
    "homepage": "https://univer.ai",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer"
    },
    "bugs": {
        "url": "https://github.com/dream-num/univer/issues"
    },
    "keywords": [
        "univer"
    ],
    "exports": {
        ".": "./src/index.ts",
        "./*": "./src/*",
        "./locale/*": "./src/locale/*.ts",
        "./facade": "./src/facade/index.ts"
    },
    "main": "./src/index.ts",
    "types": "./lib/types/index.d.ts",
    "publishConfig": {
        "access": "public",
        "main": "./lib/es/index.js",
        "module": "./lib/es/index.js",
        "exports": {
            ".": {
                "import": "./lib/es/index.js",
                "require": "./lib/cjs/index.js",
                "types": "./lib/types/index.d.ts"
            },
            "./*": {
                "import": "./lib/es/*",
                "require": "./lib/cjs/*",
                "types": "./lib/types/index.d.ts"
            },
            "./locale/*": {
                "import": "./lib/es/locale/*.js",
                "require": "./lib/cjs/locale/*.js",
                "types": "./lib/types/locale/*.d.ts"
            },
            "./facade": {
                "import": "./lib/es/facade.js",
                "require": "./lib/cjs/facade.js",
                "types": "./lib/types/facade/index.d.ts"
            },
            "./lib/facade": {
                "import": "./lib/es/facade.js",
                "require": "./lib/cjs/facade.js",
                "types": "./lib/types/facade/index.d.ts"
            },
            "./lib/*": "./lib/*"
        }
    },
    "directories": {
        "lib": "lib"
    },
    "files": [
        "lib"
    ],
    "scripts": {
        "test": "vitest run",
        "test:watch": "vitest",
        "coverage": "vitest run --coverage",
        "typecheck": "tsc --noEmit",
        "build:bundle": "univer-cli build",
        "build:types": "tsc -p tsconfig.node.json",
        "build": "pnpm run build:bundle && pnpm run build:types"
    },
    "peerDependencies": {
        "rxjs": ">=7.0.0"
    },
    "dependencies": {
        "@univerjs/core": "workspace:*",
        "@univerjs/engine-formula": "workspace:*",
        "@univerjs/engine-render": "workspace:*",
        "@univerjs/protocol": "0.1.48",
        "@univerjs/rpc": "workspace:*"
    },
    "devDependencies": {
        "@univerjs-infra/shared": "workspace:*",
        "@univerjs/network": "workspace:*",
        "rxjs": "^7.8.2",
        "typescript": "^6.0.2",
        "vitest": "^4.1.1"
    }
}

```

### File: packages\sheets\README.md
```md
# @univerjs/sheets

## Package Overview

| Package Name | UMD Namespace | Version | License | Downloads | Contains CSS | Contains i18n locales |
| --- | --- | --- | --- | --- | :---: | :---: |
| `@univerjs/sheets` | `UniverSheets` | [![][npm-version-shield]][npm-version-link] | ![][npm-license-shield] | ![][npm-downloads-shield] | ❌ | ⭕️ |

## Introduction

`@univerjs/sheets` serves as the foundation for the core business logic of spreadsheets, with base-sheets designed to be UI-agnostic, allowing for functionality such as collaborative editing to be implemented in a Node.js environment.

`@univerjs/sheets` provides the following capabilities for Univer Sheet:

* Core functionality, including numerical formatting, selection management, permissions, etc.
* Commands/mutations for modifying spreadsheet data
* Formula core functionality
* Core numerical formatting functionality

## Usage

### Installation

```shell
# Using npm
npm install @univerjs/sheets

# Using pnpm
pnpm add @univerjs/sheets
```

### `SheetInterceptorService`

`SheetInterceptorService` is a more specialized service provided by `@univerjs/sheets` that allows higher-level business to modify the results of operations such as obtaining cell data, retrieving row/column hiding information from a Worksheet, and supplementing mutations or operations at specific command executions. This service's primary goal is to enable specific functionalities, including:

1. Sheet formulas
2. Sheet conditional formatting
3. Sheet data validation
4. Sheet pivot tables

For detailed usage, please refer to the API documentation.

#### When to use `SheetInterceptorService` and when not to?

Use `SheetInterceptorService` when multiple features need to operate on the same data or state, but do not have a clear dependency relationship. For example: pivot tables, formulas, conditional formatting, data validation, and raw cell data can all affect how other features retrieve a cell's value, but they do not depend on each other. In this case, using `SheetInterceptorService` to implement these features is appropriate.

However, if one feature relies explicitly on another feature, such as a formula needing to perform certain actions when the fill down or copy-paste functions are called, the formula module should directly depend on the fill down and copy-paste modules, instead of using `SheetInterceptorService` for implementation.

<!-- Links -->
[npm-version-shield]: https://img.shields.io/npm/v/@univerjs/sheets?style=flat-square
[npm-version-link]: https://npmjs.com/package/@univerjs/sheets
[npm-license-shield]: https://img.shields.io/npm/l/@univerjs/sheets?style=flat-square
[npm-downloads-shield]: https://img.shields.io/npm/dm/@univerjs/sheets?style=flat-square

```

### File: packages\slides\package.json
```json
{
    "name": "@univerjs/slides",
    "version": "0.20.0",
    "private": false,
    "description": "",
    "author": "DreamNum <developer@univer.ai>",
    "license": "Apache-2.0",
    "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/univer"
    },
    "homepage": "https://univer.ai",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer"
    },
    "bugs": {
        "url": "https://github.com/dream-num/univer/issues"
    },
    "keywords": [
        "univer"
    ],
    "exports": {
        ".": "./src/index.ts",
        "./*": "./src/*"
    },
    "main": "./src/index.ts",
    "types": "./lib/types/index.d.ts",
    "publishConfig": {
        "access": "public",
        "main": "./lib/es/index.js",
        "module": "./lib/es/index.js",
        "exports": {
            ".": {
                "import": "./lib/es/index.js",
                "require": "./lib/cjs/index.js",
                "types": "./lib/types/index.d.ts"
            },
            "./*": {
                "import": "./lib/es/*",
                "require": "./lib/cjs/*",
                "types": "./lib/types/index.d.ts"
            },
            "./lib/*": "./lib/*"
        }
    },
    "directories": {
        "lib": "lib"
    },
    "files": [
        "lib"
    ],
    "scripts": {
        "test": "vitest run",
        "test:watch": "vitest",
        "coverage": "vitest run --coverage",
        "typecheck": "tsc --noEmit",
        "build:bundle": "univer-cli build",
        "build:types": "tsc -p tsconfig.node.json",
        "build": "pnpm run build:bundle && pnpm run build:types"
    },
    "dependencies": {
        "@univerjs/core": "workspace:*",
        "@univerjs/engine-render": "workspace:*"
    },
    "devDependencies": {
        "@univerjs-infra/shared": "workspace:*",
        "typescript": "^6.0.2",
        "vitest": "^4.1.1"
    }
}

```

### File: packages\slides\README.md
```md
# @univerjs/slides

## Package Overview

| Package Name | UMD Namespace | Version | License | Downloads | Contains CSS | Contains i18n locales |
| --- | --- | --- | --- | --- | :---: | :---: |
| `@univerjs/slides` | `UniveSlides` | [![][npm-version-shield]][npm-version-link] | ![][npm-license-shield] | ![][npm-downloads-shield] | ❌ | ⭕️ |

## Introduction

TODO: Not written yet.

## Usage

### Installation

```shell
# Using npm
npm install @univerjs/slides

# Using pnpm
pnpm add @univerjs/slides
```

<!-- Links -->
[npm-version-shield]: https://img.shields.io/npm/v/@univerjs/slides?style=flat-square
[npm-version-link]: https://npmjs.com/package/@univerjs/slides
[npm-license-shield]: https://img.shields.io/npm/l/@univerjs/slides?style=flat-square
[npm-downloads-shield]: https://img.shields.io/npm/dm/@univerjs/slides?style=flat-square

```

### File: packages\telemetry\package.json
```json
{
    "name": "@univerjs/telemetry",
    "version": "0.20.0",
    "private": false,
    "description": "",
    "author": "DreamNum <developer@univer.ai>",
    "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/univer"
    },
    "homepage": "https://univer.ai",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer"
    },
    "bugs": {
        "url": "https://github.com/dream-num/univer/issues"
    },
    "keywords": [],
    "exports": {
        ".": "./src/index.ts",
        "./*": "./src/*"
    },
    "main": "./src/index.ts",
    "types": "./lib/types/index.d.ts",
    "publishConfig": {
        "access": "public",
        "main": "./lib/es/index.js",
        "module": "./lib/es/index.js",
        "exports": {
            ".": {
                "import": "./lib/es/index.js",
                "require": "./lib/cjs/index.js",
                "types": "./lib/types/index.d.ts"
            },
            "./*": {
                "import": "./lib/es/*",
                "require": "./lib/cjs/*",
                "types": "./lib/types/index.d.ts"
            },
            "./lib/*": "./lib/*"
        }
    },
    "directories": {
        "lib": "lib"
    },
    "files": [
        "lib"
    ],
    "scripts": {
        "test": "vitest run",
        "test:watch": "vitest",
        "coverage": "vitest run --coverage",
        "typecheck": "tsc --noEmit",
        "build:bundle": "univer-cli build",
        "build:types": "tsc -p tsconfig.node.json",
        "build": "pnpm run build:bundle && pnpm run build:types"
    },
    "dependencies": {
        "@univerjs/core": "workspace:*"
    },
    "devDependencies": {
        "@univerjs-infra/shared": "workspace:*",
        "typescript": "^6.0.2",
        "vitest": "^4.1.1"
    }
}

```

### File: packages\telemetry\README.md
```md
# @univerjs/telemetry

[![npm version](https://img.shields.io/npm/v/@univerjs/telemetry)](https://npmjs.org/packages/@univerjs/telemetry)
[![license](https://img.shields.io/npm/l/@univerjs/telemetry)](https://img.shields.io/npm/l/@univerjs/telemetry)

## Introduction

This plugin provides interface `ITelemetry` to track telemetry data. The first-party plugins of Univer would dependent on this interface. If you want to track telemetry data, you can implement this interface and register it to `Univer`'s injector.

## Usage

### Installation

```shell
npm i @univerjs/telemetry
```

```

### File: packages\themes\package.json
```json
{
    "name": "@univerjs/themes",
    "version": "0.20.0",
    "private": false,
    "description": "Themes package for Univer",
    "author": "DreamNum <developer@univer.ai>",
    "license": "Apache-2.0",
    "funding": {
        "type": "opencollective",
        "url": "https://opencollective.com/univer"
    },
    "homepage": "https://univer.ai",
    "repository": {
        "type": "git",
        "url": "https://github.com/dream-num/univer"
    },
    "bugs": {
        "url": "https://github.com/dream-num/univer/issues"
    },
    "keywords": [
        "univer",
        "theme"
    ],
    "exports": {
        ".": "./src/index.ts",
        "./*": "./src/*"
    },
    "main": "./src/index.ts",
    "types": "./lib/types/index.d.ts",
    "publishConfig": {
        "access": "public",
        "main": "./lib/es/index.js",
        "module": "./lib/es/index.js",
        "exports": {
            ".": {
                "import": "./lib/es/index.js",
                "require": "./lib/cjs/index.js",
                "types": "./lib/types/index.d.ts"
            },
            "./*": {
                "import": "./lib/es/*",
                "require": "./lib/cjs/*",
                "types": "./lib/types/index.d.ts"
            },
            "./lib/*": "./lib/*"
        }
    },
    "directories": {
        "lib": "lib"
    },
    "files": [
        "lib"
    ],
    "scripts": {
        "typecheck": "tsc --noEmit",
        "build:bundle": "univer-cli build",
        "build:types": "tsc -p tsconfig.node.json",
        "build": "pnpm run build:bundle && pnpm run build:types"
    },
    "devDependencies": {
        "@univerjs-infra/shared": "workspace:*"
    }
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

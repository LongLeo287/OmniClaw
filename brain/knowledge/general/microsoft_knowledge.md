---
id: microsoft-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:07.825002
---

# KNOWLEDGE EXTRACT: microsoft
> **Extracted on:** 2026-03-30 17:42:48
> **Source:** microsoft

---

## File: `autogen.md`
```markdown
# 📦 microsoft/autogen [🔖 PENDING]
🔗 https://github.com/microsoft/autogen
🌐 https://microsoft.github.io/autogen/

## Meta
- **Stars:** ⭐ 56255 | **Forks:** 🍴 8453
- **Language:** Python | **License:** CC-BY-4.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
A programming framework for agentic AI

## README (trích đầu)
```
<a name="readme-top"></a>

<div align="center">
<img src="https://microsoft.github.io/autogen/0.2/img/ag.svg" alt="AutoGen Logo" width="100">

[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20%40pyautogen)](https://twitter.com/pyautogen)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Company?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/105812540)
[![Discord](https://img.shields.io/badge/discord-chat-green?logo=discord)](https://aka.ms/autogen-discord)
[![Documentation](https://img.shields.io/badge/Documentation-AutoGen-blue?logo=read-the-docs)](https://microsoft.github.io/autogen/)
[![Blog](https://img.shields.io/badge/Blog-AutoGen-blue?logo=blogger)](https://devblogs.microsoft.com/autogen/)

</div>

# AutoGen

**AutoGen** is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans.

> **Important:** if you are new to AutoGen, please checkout [Microsoft Agent Framework](https://github.com/microsoft/agent-framework).
> AutoGen will still be maintained and continue to receive bug fixes and critical security patches.
> Read our [announcement](https://github.com/microsoft/autogen/discussions/7066).

## Installation

AutoGen requires **Python 3.10 or later**.

```bash
# Install AgentChat and OpenAI client from Extensions
pip install -U "autogen-agentchat" "autogen-ext[openai]"
```

The current stable version can be found in the [releases](https://github.com/microsoft/autogen/releases). If you are upgrading from AutoGen v0.2, please refer to the [Migration Guide](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/migration-guide.html) for detailed instructions on how to update your code and configurations.

```bash
# Install AutoGen Studio for no-code GUI
pip install -U "autogenstudio"
```

## Quickstart

The following samples call OpenAI API, so you first need to create an account and export your key as `export OPENAI_API_KEY='[REDACTED_API_KEY]'`.

### Hello World

Create an assistant agent using OpenAI's GPT-4o model. See [other supported models](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/tutorial/models.html).

```python
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main() -> None:
    model_client = OpenAIChatCompletionClient(model="gpt-4.1")
    agent = AssistantAgent("assistant", model_client=model_client)
    print(await agent.run(task="Say 'Hello World!'"))
    await model_client.close()

asyncio.run(main())
```

### MCP Server

Create a web browsing assistant agent that uses the Playwright MCP server.

```python
# First run `npm install -g @playwright/mcp@latest` to install the MCP server.
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from a
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `DevSkim.md`
```markdown
# 📦 microsoft/DevSkim [🔖 PENDING/APPROVE]
🔗 https://github.com/microsoft/DevSkim


## Meta
- **Stars:** ⭐ 976 | **Forks:** 🍴 123
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-03-13
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
DevSkim is a set of IDE plugins, language analyzers, and rules that provide security "linting" capabilities.

## README (trích đầu)
```
# DevSkim
[![Nuget](https://img.shields.io/nuget/v/Microsoft.CST.DevSkim.CLI?label=CLI&logo=NuGet)](https://www.nuget.org/packages/Microsoft.CST.DevSkim.CLI) 
[![Visual Studio 2022 Version](https://img.shields.io/visual-studio-marketplace/v/MS-CST-E.MicrosoftDevSkim?logo=Visual%20Studio&label=VS)](https://marketplace.visualstudio.com/items?itemName=MS-CST-E.vscode-devskim)
[![Visual Studio Code Version](https://img.shields.io/visual-studio-marketplace/v/MS-CST-E.vscode-devskim?logo=Visual%20Studio%20Code&label=VSCode)](https://marketplace.visualstudio.com/items?itemName=MS-CST-E.vscode-devskim)

[![Nuget CLI Installs](https://img.shields.io/nuget/dt/Microsoft.CST.DevSkim.CLI?logo=NuGet)](https://www.nuget.org/packages/Microsoft.CST.DevSkim.CLI) 
[![Visual Studio Installs](https://img.shields.io/visual-studio-marketplace/i/MS-CST-E.MicrosoftDevSkim?logo=Visual%20Studio)](https://marketplace.visualstudio.com/items?itemName=MS-CST-E.MicrosoftDevSkim) 
[![Visual Studio Code Installs](https://img.shields.io/visual-studio-marketplace/i/MS-CST-E.vscode-devskim?logo=Visual%20Studio%20Code)](https://marketplace.visualstudio.com/items?itemName=MS-CST-E.vscode-devskim)

DevSkim is a framework of IDE extensions and language analyzers that provide inline security analysis 
in the dev environment as the developer writes code. It has a flexible rule model that supports multiple programming
languages. The goal is to notify the developer as they are introducing a security
vulnerability in order to fix the issue at the point of introduction, and to help build awareness
for the developer.

![](./DevSkim-VSCode-Plugin/vsc-example.gif)

### Features

* Built-in rules, and support for writing custom rules
* Cross-platform CLI built on .NET for file analysis
* IDE plugins for Visual Studio and Visual Studio Code built on Language Server Protocol
* IntelliSense error "squiggly lines" for identified security issues
* Information and guidance provided for identified security issues
* Optional suppression of unwanted findings
* Support for JSONPath, XPATH and YmlPath based rules
* Broad language support including: C, C++, C#, Cobol, Go, Java, Javascript/Typescript, Python, and [more](https://github.com/Microsoft/DevSkim/wiki/Supported-Languages).

### Repository Structure

This repository contains DevSkim and its official supported plugins. Issues and contributions are accepted here for:

* DevSkim Library
  * Location: `./DevSkim-DotNet/`
* DevSkim CLI
  * Location: `./DevSkim-DotNet/Microsoft.DevSkim.CLI/`
* DevSkim Visual Studio Extension
  * Location: `./DevSkim-DotNet/Microsoft.DevSkim.VisualStudio/`
* DevSkim Visual Studio Code Plugin
  * Location: `./DevSkim-VSCode-Plugin/`
* Default Rules and Guidance
  * Location: `./rules/default/`

## Official Releases

The C# library is available on NuGet as [Microsoft.CST.DevSkim](https://www.nuget.org/packages/Microsoft.CST.DevSkim/).

The .NET Global Tool is available on NuGet as [Microsoft.CST.DevSkim.CLI](https://www.nuget
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `generative-ai-for-beginners.md`
```markdown
# 📦 microsoft/generative-ai-for-beginners [🔖 PENDING]
🔗 https://github.com/microsoft/generative-ai-for-beginners


## Meta
- **Stars:** ⭐ 108572 | **Forks:** 🍴 58197
- **Language:** Jupyter Notebook | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
21 Lessons, Get Started Building with Generative AI 

## README (trích đầu)
```
![Generative AI For Beginners](./images/repo-thumbnailv4-fixed.png?WT.mc_id=academic-105485-koreyst)

### 21 Lessons teaching everything you need to know to start building Generative AI applications

[![GitHub license](https://img.shields.io/github/license/microsoft/Generative-AI-For-Beginners.svg)](https://github.com/microsoft/Generative-AI-For-Beginners/blob/master/LICENSE?WT.mc_id=academic-105485-koreyst)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/Generative-AI-For-Beginners.svg)](https://GitHub.com/microsoft/Generative-AI-For-Beginners/graphs/contributors/?WT.mc_id=academic-105485-koreyst)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/Generative-AI-For-Beginners.svg)](https://GitHub.com/microsoft/Generative-AI-For-Beginners/issues/?WT.mc_id=academic-105485-koreyst)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/Generative-AI-For-Beginners.svg)](https://GitHub.com/microsoft/Generative-AI-For-Beginners/pulls/?WT.mc_id=academic-105485-koreyst)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=academic-105485-koreyst)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/Generative-AI-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/Generative-AI-For-Beginners/watchers/?WT.mc_id=academic-105485-koreyst)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/Generative-AI-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/Generative-AI-For-Beginners/network/?WT.mc_id=academic-105485-koreyst)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/Generative-AI-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/Generative-AI-For-Beginners/stargazers/?WT.mc_id=academic-105485-koreyst)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

### 🌐 Multi-Language Support

#### Supported via GitHub Action (Automated & Always Up-to-Date)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../../../README.md) | [Bengali](../../../README.md) | [Bulgarian](../../../README.md) | [Burmese (Myanmar)](../../../README.md) | [Chinese (Simplified)](../../../README.md) | [Chinese (Traditional, Hong Kong)](../../../README.md) | [Chinese (Traditional, Macau)](../../../README.md) | [Chinese (Traditional, Taiwan)](../../../README.md) | [Croatian](../../../README.md) | [Czech](../../../README.md) | [Danish](../../../README.md) | [Dutch](../../../README.md) | [Estonian](../../../README.md) | [Finnish](../../../README.md) | [French](../../../README.md) | [German](../../../README.md) | [Greek](../../../README.md) | [Hebrew](../../../README.md) | [Hindi](../../../README.md) |
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `markitdown.md`
```markdown
# 📦 microsoft/markitdown [🔖 PENDING]
🔗 https://github.com/microsoft/markitdown


## Meta
- **Stars:** ⭐ 92583 | **Forks:** 🍴 5549
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
Python tool for converting files and office documents to Markdown.

## README (trích đầu)
```
# MarkItDown

[![PyPI](https://img.shields.io/pypi/v/markitdown.svg)](https://pypi.org/project/markitdown/)
![PyPI - Downloads](https://img.shields.io/pypi/dd/markitdown)
[![Built by AutoGen Team](https://img.shields.io/badge/Built%20by-AutoGen%20Team-blue)](https://github.com/microsoft/autogen)

> [!TIP]
> MarkItDown now offers an MCP (Model Context Protocol) server for integration with LLM applications like Claude Desktop. See [markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) for more information.

> [!IMPORTANT]
> Breaking changes between 0.0.1 to 0.1.0:
> * Dependencies are now organized into optional feature-groups (further details below). Use `pip install 'markitdown[all]'` to have backward-compatible behavior.
> * convert\_stream() now requires a binary file-like object (e.g., a file opened in binary mode, or an io.BytesIO object). This is a breaking change from the previous version, where it previously also accepted text file-like objects, like io.StringIO.
> * The DocumentConverter class interface has changed to read from file-like streams rather than file paths. *No temporary files are created anymore*. If you are the maintainer of a plugin, or custom DocumentConverter, you likely need to update your code. Otherwise, if only using the MarkItDown class or CLI (as in these examples), you should not need to change anything.

MarkItDown is a lightweight Python utility for converting various files to Markdown for use with LLMs and related text analysis pipelines. To this end, it is most comparable to [textract](https://github.com/deanmalmgren/textract), but with a focus on preserving important document structure and content as Markdown (including: headings, lists, tables, links, etc.) While the output is often reasonably presentable and human-friendly, it is meant to be consumed by text analysis tools -- and may not be the best option for high-fidelity document conversions for human consumption.

MarkItDown currently supports the conversion from:

- PDF
- PowerPoint
- Word
- Excel
- Images (EXIF metadata and OCR)
- Audio (EXIF metadata and speech transcription)
- HTML
- Text-based formats (CSV, JSON, XML)
- ZIP files (iterates over contents)
- Youtube URLs
- EPubs
- ... and more!

## Why Markdown?

Markdown is extremely close to plain text, with minimal markup or formatting, but still
provides a way to represent important document structure. Mainstream LLMs, such as
OpenAI's GPT-4o, natively "_speak_" Markdown, and often incorporate Markdown into their
responses unprompted. This suggests that they have been trained on vast amounts of
Markdown-formatted text, and understand it well. As a side benefit, Markdown conventions
are also highly token-efficient.

## Prerequisites
MarkItDown requires Python 3.10 or higher. It is recommended to use a virtual environment to avoid dependency conflicts.

With the standard Python installation, you can create and activate a virtual environment using the following co
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mimalloc.md`
```markdown
# 📦 microsoft/mimalloc [🔖 PENDING/APPROVE]
🔗 https://github.com/microsoft/mimalloc
🌐 https://microsoft.github.io/mimalloc

## Meta
- **Stars:** ⭐ 12648 | **Forks:** 🍴 1072
- **Language:** C | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
mimalloc is a compact general purpose allocator with excellent performance.

## README (trích đầu)
```

<img align="left" width="100" height="100" src="doc/mimalloc-logo.png"/>

[<img align="right" src="https://dev.azure.com/Daan0324/mimalloc/_apis/build/status/microsoft.mimalloc?branchName=dev3"/>](https://dev.azure.com/Daan0324/mimalloc/_build?definitionId=1&_a=summary)

# mimalloc

&nbsp;

mimalloc (pronounced "me-malloc")
is a general purpose allocator with excellent [performance](#performance) characteristics.
Initially developed by Daan Leijen for the runtime systems of the
[Koka](https://koka-lang.github.io) and [Lean](https://github.com/leanprover/lean) languages.

Latest release   : `v3.2.8` (2026-02-03) release candidate 3, please report any issues.  
Latest v2 release: `v2.2.7` (2026-01-15).  
Latest v1 release: `v1.9.7` (2026-01-15).

mimalloc is a drop-in replacement for `malloc` and can be used in other programs
without code changes, for example, on dynamically linked ELF-based systems (Linux, BSD, etc.) you can use it as:
```
> LD_PRELOAD=/usr/lib/libmimalloc.so  myprogram
```
It also includes a way to dynamically override the default allocator in [Windows](#override_on_windows). 
Notable aspects of the design include:

- __small and consistent__: the library is about 10k LOC using simple and
  consistent data structures. This makes it very suitable
  to integrate and adapt in other projects. For runtime systems it
  provides hooks for a monotonic _heartbeat_ and deferred freeing (for
  bounded worst-case times with reference counting).
  Partly due to its simplicity, mimalloc has been ported to many systems (Windows, macOS,
  Linux, WASM, various BSD's, Haiku, MUSL, etc) and has excellent support for dynamic overriding.
  At the same time, it is an industrial strength allocator that runs (very) large scale
  distributed services on thousands of machines with excellent worst case latencies.
- __free list sharding__: instead of one big free list (per size class) we have
  many smaller lists per "mimalloc page" which reduces fragmentation and
  increases locality --
  things that are allocated close in time get allocated close in memory.
  (A mimalloc page contains blocks of one size class and is usually 64KiB on a 64-bit system).
- __free list multi-sharding__: the big idea! Not only do we shard the free list
  per mimalloc page, but for each page we have multiple free lists. In particular, there
  is one list for thread-local `free` operations, and another one for concurrent `free`
  operations. Free-ing from another thread can now be a single CAS without needing
  sophisticated coordination between threads. Since there will be
  thousands of separate free lists, contention is naturally distributed over the heap,
  and the chance of contending on a single location will be low -- this is quite
  similar to randomized algorithms like skip lists where adding
  a random oracle removes the need for a more complex algorithm.
- __eager page purging__: when a "page" becomes empty (with increased chance
  due to free list sharding) the memor
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `playwright-mcp.md`
```markdown
# 📦 microsoft/playwright-mcp [🔖 PENDING/APPROVE]
🔗 https://github.com/microsoft/playwright-mcp
🌐 https://www.npmjs.com/package/@playwright/mcp

## Meta
- **Stars:** ⭐ 29778 | **Forks:** 🍴 2402
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Playwright MCP server

## README (trích đầu)
```
## Playwright MCP

A Model Context Protocol (MCP) server that provides browser automation capabilities using [Playwright](https://playwright.dev). This server enables LLMs to interact with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models.

### Playwright MCP vs Playwright CLI

This package provides MCP interface into Playwright. If you are using a **coding agent**, you might benefit from using the [CLI+SKILLS](https://github.com/microsoft/playwright-cli) instead.

- **CLI**: Modern **coding agents** increasingly favor CLI–based workflows exposed as SKILLs over MCP because CLI invocations are more token-efficient: they avoid loading large tool schemas and verbose accessibility trees into the model context, allowing agents to act through concise, purpose-built commands. This makes CLI + SKILLs better suited for high-throughput coding agents that must balance browser automation with large codebases, tests, and reasoning within limited context windows.<br>**Learn more about [Playwright CLI with SKILLS](https://github.com/microsoft/playwright-cli)**.

- **MCP**: MCP remains relevant for specialized agentic loops that benefit from persistent state, rich introspection, and iterative reasoning over page structure, such as exploratory automation, self-healing tests, or long-running autonomous workflows where maintaining continuous browser context outweighs token cost concerns.

### Key Features

- **Fast and lightweight**. Uses Playwright's accessibility tree, not pixel-based input.
- **LLM-friendly**. No vision models needed, operates purely on structured data.
- **Deterministic tool application**. Avoids ambiguity common with screenshot-based approaches.

### Requirements
- Node.js 18 or newer
- VS Code, Cursor, Windsurf, Claude Desktop, Goose or any other MCP client

<!--
// Generate using:
node utils/generate-links.js
-->

### Getting started

First, install the Playwright MCP server with your client.

**Standard config** works in most of the tools:

```js
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

[<img src="https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=Install%20Server&color=0098FF" alt="Install in VS Code">](https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D) [<img alt="Install in VS Code Insiders" src="https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=Install%20Server&color=24bfa5">](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522playwright%2522%252C%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522%2540playwright%252Fmcp%2540latest%2522%255D%257D)

<details>
<summary>Amp</summ
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `playwright.md`
```markdown
# 📦 microsoft/playwright [🔖 PENDING]
🔗 https://github.com/microsoft/playwright
🌐 https://playwright.dev

## Meta
- **Stars:** ⭐ 85045 | **Forks:** 🍴 5366
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. 

## README (trích đầu)
```
# 🎭 Playwright

[![npm version](https://img.shields.io/npm/v/playwright.svg)](https://www.npmjs.com/package/playwright) <!-- GEN:chromium-version-badge -->[![Chromium version](https://img.shields.io/badge/chromium-146.0.7680.31-blue.svg?logo=google-chrome)](https://www.chromium.org/Home)<!-- GEN:stop --> <!-- GEN:firefox-version-badge -->[![Firefox version](https://img.shields.io/badge/firefox-148.0.2-blue.svg?logo=firefoxbrowser)](https://www.mozilla.org/en-US/firefox/new/)<!-- GEN:stop --> <!-- GEN:webkit-version-badge -->[![WebKit version](https://img.shields.io/badge/webkit-26.0-blue.svg?logo=safari)](https://webkit.org/)<!-- GEN:stop --> [![Join Discord](https://img.shields.io/badge/join-discord-informational)](https://aka.ms/playwright/discord)

## [Documentation](https://playwright.dev) | [API reference](https://playwright.dev/docs/api/class-playwright)

Playwright is a framework for Web Testing and Automation. It allows testing [Chromium](https://www.chromium.org/Home)<sup>1</sup>, [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [WebKit](https://webkit.org/) with a single API. Playwright is built to enable cross-browser web automation that is **ever-green**, **capable**, **reliable**, and **fast**.

|          | Linux | macOS | Windows |
|   :---   | :---: | :---: | :---:   |
| Chromium<sup>1</sup> <!-- GEN:chromium-version -->146.0.7680.31<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| WebKit <!-- GEN:webkit-version -->26.0<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Firefox <!-- GEN:firefox-version -->148.0.2<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |

Headless execution is supported for all browsers on all platforms. Check out [system requirements](https://playwright.dev/docs/intro#system-requirements) for details.

Looking for Playwright for [Python](https://playwright.dev/python/docs/intro), [.NET](https://playwright.dev/dotnet/docs/intro), or [Java](https://playwright.dev/java/docs/intro)?

<sup>1</sup> Playwright uses [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing) by default.

## Installation

Playwright has its own test runner for end-to-end tests, we call it Playwright Test.

### Using init command

The easiest way to get started with Playwright Test is to run the init command.

```Shell
# Run from your project's root directory
npm init playwright@latest
# Or create a new project
npm init playwright@latest new-project
```

This will create a configuration file, optionally add examples, a GitHub Action workflow and a first test example.spec.ts. You can now jump directly to writing assertions section.

### Manually

Add dependency and install browsers.

```Shell
npm i -D @playwright/test
# install supported browsers
npx playwright install
```

You can optionally install only selected browsers, see [install browsers](https://playwright.dev/docs/cli#install-browsers) for more detail
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `promptflow.md`
```markdown
# 📦 microsoft/promptflow [🔖 PENDING/APPROVE]
🔗 https://github.com/microsoft/promptflow
🌐 https://microsoft.github.io/promptflow/

## Meta
- **Stars:** ⭐ 11079 | **Forks:** 🍴 1084
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Build high-quality LLM apps - from prototyping, testing to production deployment and monitoring.

## README (trích đầu)
```
# Prompt flow

[![Python package](https://img.shields.io/pypi/v/promptflow)](https://pypi.org/project/promptflow/)
[![Python](https://img.shields.io/pypi/pyversions/promptflow.svg?maxAge=2592000)](https://pypi.python.org/pypi/promptflow/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/promptflow)](https://pypi.org/project/promptflow/)
[![CLI](https://img.shields.io/badge/CLI-reference-blue)](https://microsoft.github.io/promptflow/reference/pf-command-reference.html)
[![vsc extension](https://img.shields.io/visual-studio-marketplace/i/prompt-flow.prompt-flow?logo=Visual%20Studio&label=Extension%20)](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow)

[![Doc](https://img.shields.io/badge/Doc-online-green)](https://microsoft.github.io/promptflow/index.html)
[![Issue](https://img.shields.io/github/issues/microsoft/promptflow)](https://github.com/microsoft/promptflow/issues/new/choose)
[![Discussions](https://img.shields.io/github/discussions/microsoft/promptflow)](https://github.com/microsoft/promptflow/issues/new/choose)
[![CONTRIBUTING](https://img.shields.io/badge/Contributing-8A2BE2)](https://github.com/microsoft/promptflow/blob/main/CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/github/license/microsoft/promptflow)](https://github.com/microsoft/promptflow/blob/main/LICENSE)

> Welcome to join us to make prompt flow better by
> participating [discussions](https://github.com/microsoft/promptflow/discussions),
> opening [issues](https://github.com/microsoft/promptflow/issues/new/choose),
> submitting [PRs](https://github.com/microsoft/promptflow/pulls).

**Prompt flow** is a suite of development tools designed to streamline the end-to-end development cycle of LLM-based AI applications, from ideation, prototyping, testing, evaluation to production deployment and monitoring. It makes prompt engineering much easier and enables you to build LLM apps with production quality.

With prompt flow, you will be able to:

- **Create and iteratively develop flow**
    - Create executable [flows](https://microsoft.github.io/promptflow/concepts/concept-flows.html) that link LLMs, prompts, Python code and other [tools](https://microsoft.github.io/promptflow/concepts/concept-tools.html) together.
    - Debug and iterate your flows, especially [tracing interaction with LLMs](https://microsoft.github.io/promptflow/how-to-guides/tracing/index.html) with ease.
- **Evaluate flow quality and performance**
    - Evaluate your flow's quality and performance with larger datasets.
    - Integrate the testing and evaluation into your CI/CD system to ensure quality of your flow.
- **Streamlined development cycle for production**
    - Deploy your flow to the serving platform you choose or integrate into your app's code base easily.
    - (Optional but highly recommended) Collaborate with your team by leveraging the cloud version of [Prompt flow in Azure AI](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-wh
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pyright.md`
```markdown
# 📦 microsoft/pyright [🔖 PENDING/APPROVE]
🔗 https://github.com/microsoft/pyright


## Meta
- **Stars:** ⭐ 15336 | **Forks:** 🍴 1781
- **Language:** Python | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Static Type Checker for Python

## README (trích đầu)
```
![Pyright](https://github.com/microsoft/pyright/blob/main/docs/img/PyrightLarge.png)

# Static Type Checker for Python

Pyright is a full-featured, standards-based static type checker for Python. It is designed for high performance and can be used with large Python source bases.

Pyright includes both a [command-line tool](https://microsoft.github.io/pyright/#/command-line) and an [extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-pyright.pyright).


## Pyright Playground

Try Pyright in your browser using the [Pyright Playground](https://pyright-play.net/?code=MQAgKgFglgziMEMC2AHANgUxAEw0g9gHYwAuATgiRnBPgO4gDG%2BSBhIGZZ%2BZcjC7AEZZcVRlWzwSlKPzRoAniEFKUCslADmEEgDoAUPtwAzEAmzYAFAA8AXCGNp8lADQgF9x85IBKW-pBAkDIMEgBXMnZrEABqd0NQAAUEGBgoQk0zKTIQdNIBRiwUkBIILBgMZkJJBDJNMKQMQhJg6jC0Ejh0rLIw5qhGjmtClBIoIgNzKwBGNwAiOZ99IA).


## Documentation

Refer to [the documentation](https://microsoft.github.io/pyright) for installation, configuration, and usage details.


## Community
Do you have questions about Pyright or Python type annotations in general? Post your questions in [the discussion section](https://github.com/microsoft/pyright/discussions).

If you would like to report a bug or request an enhancement, file a new issue in either the [pyright](https://github.com/microsoft/pyright/issues) or [pylance-release](https://github.com/microsoft/pylance-release/issues) issue tracker. In general, core type checking functionality is associated with Pyright while language service functionality is associated with Pylance, but the same contributors monitor both repos. For best results, provide the information requested in the issue template.


## Contributing

This project welcomes contributions and suggestions. For feature and complex bug fix contributions, it is recommended that you first discuss the proposed change with Pyright’s maintainers before submitting the pull request. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `semantic-kernel.md`
```markdown
# 📦 microsoft/semantic-kernel [🔖 PENDING/APPROVE]
🔗 https://github.com/microsoft/semantic-kernel
🌐 https://aka.ms/semantic-kernel

## Meta
- **Stars:** ⭐ 27569 | **Forks:** 🍴 4525
- **Language:** C# | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Integrate cutting-edge LLM technology quickly and easily into your apps

## README (trích đầu)
```
# Semantic Kernel

**Build intelligent AI agents and multi-agent systems with this enterprise-ready orchestration framework**

[![License: MIT](https://img.shields.io/github/license/microsoft/semantic-kernel)](https://github.com/microsoft/semantic-kernel/blob/main/LICENSE)
[![Python package](https://img.shields.io/pypi/v/semantic-kernel)](https://pypi.org/project/semantic-kernel/)
[![Nuget package](https://img.shields.io/nuget/vpre/Microsoft.SemanticKernel)](https://www.nuget.org/packages/Microsoft.SemanticKernel/)
[![Discord](https://img.shields.io/discord/1063152441819942922?label=Discord&logo=discord&logoColor=white&color=d82679)](https://aka.ms/SKDiscord)


## What is Semantic Kernel?

Semantic Kernel is a model-agnostic SDK that empowers developers to build, orchestrate, and deploy AI agents and multi-agent systems. Whether you're building a simple chatbot or a complex multi-agent workflow, Semantic Kernel provides the tools you need with enterprise-grade reliability and flexibility.

## System Requirements

- **Python**: 3.10+
- **.NET**: .NET 10.0+ 
- **Java**: JDK 17+
- **OS Support**: Windows, macOS, Linux

## Key Features

- **Model Flexibility**: Connect to any LLM with built-in support for [OpenAI](https://platform.openai.com/docs/introduction), [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service), [Hugging Face](https://huggingface.co/), [NVidia](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/) and more
- **Agent Framework**: Build modular AI agents with access to tools/plugins, memory, and planning capabilities
- **Multi-Agent Systems**: Orchestrate complex workflows with collaborating specialist agents
- **Plugin Ecosystem**: Extend with native code functions, prompt templates, OpenAPI specs, or Model Context Protocol (MCP)
- **Vector DB Support**: Seamless integration with [Azure AI Search](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search), [Elasticsearch](https://www.elastic.co/), [Chroma](https://docs.trychroma.com/docs/overview/getting-started), and more
- **Multimodal Support**: Process text, vision, and audio inputs
- **Local Deployment**: Run with [Ollama](https://ollama.com/), [LMStudio](https://lmstudio.ai/), or [ONNX](https://onnx.ai/)
- **Process Framework**: Model complex business processes with a structured workflow approach
- **Enterprise Ready**: Built for observability, security, and stable APIs

## Installation

First, set the environment variable for your AI Services:

**Azure OpenAI:**
```bash
export AZURE_OPENAI_API_KEY=AAA....
```

**or OpenAI directly:**
```bash
export OPENAI_API_KEY=sk-...
```

### Python

```bash
pip install semantic-kernel
```

### .NET

```bash
dotnet add package Microsoft.SemanticKernel
dotnet add package Microsoft.SemanticKernel.Agents.Core
```

### Java

See [semantic-kernel-java build](https://github.com/microsoft/semantic-kernel-java/blob/main/BUILD.md) for instructions.

## Quickstart

### Basic Agent
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `skills.md`
```markdown
# 📦 microsoft/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/microsoft/skills
🌐 https://microsoft.github.io/skills/

## Meta
- **Stars:** ⭐ 1862 | **Forks:** 🍴 205
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents

## README (trích đầu)
```
# Agent Skills

[![Evals & Tests](https://img.shields.io/github/actions/workflow/status/microsoft/skills/test-harness.yml?branch=main&label=Evals%20%26%20Tests)](https://github.com/microsoft/skills/actions/workflows/test-harness.yml)
[![Copilot SDK Tests](https://img.shields.io/github/actions/workflow/status/microsoft/skills/skill-evaluation.yml?branch=main&label=Copilot%20SDK%20Tests)](https://github.com/microsoft/skills/actions/workflows/skill-evaluation.yml)
[![Install via skills.sh](https://img.shields.io/badge/skills.sh-install-blue)](https://skills.sh/microsoft/skills)
[![Documentation](https://img.shields.io/badge/docs-documentation-blue)](https://microsoft.github.io/skills/#documentation)

> [!NOTE]
> **Work in Progress** — This repository is under active development. More skills are being added, existing skills are being updated to use the latest SDK patterns, and tests are being expanded to ensure quality. Contributions welcome!

Skills, custom agents, AGENTS.md templates, and MCP configurations for AI coding agents working with Azure SDKs and Microsoft AI Foundry.

> **Blog post:** [Context-Driven Development: Agent Skills for Microsoft Foundry and Azure](https://devblogs.microsoft.com/all-things-azure/context-driven-development-agent-skills-for-microsoft-foundry-and-azure/)

> **🔍 Skill Explorer:** [Browse all 132 skills with 1-click install](https://microsoft.github.io/skills/)

## Quick Start

```bash
npx skills add microsoft/skills
```

Select the skills you need from the wizard. Skills are installed to your chosen agent's directory (e.g., `.github/skills/` for GitHub Copilot) and symlinked if you use multiple agents.

<details>
<summary>Alternative installation methods</summary>

**Manual installation (git clone)**

```bash
# Clone and copy specific skills
git clone https://github.com/microsoft/skills.git
cp -r agent-skills/.github/skills/azure-cosmos-db-py your-project/.github/skills/

# Or use symlinks for multi-project setups
ln -s /path/to/agent-skills/.github/skills/mcp-builder /path/to/your-project/.github/skills/mcp-builder

# Share skills across different agent configs in the same repo
ln -s ../.github/skills .opencode/skills
ln -s ../.github/skills .claude/skills
```

</details>

---

Coding agents like [Copilot CLI](https://github.com/features/copilot/cli) and [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills) are powerful, but they lack domain knowledge about your SDKs. The patterns are already in their weights from pretraining. All you need is the right activation context to surface them.

> [!IMPORTANT]
> **Use skills selectively.** Loading all skills causes context rot: diluted attention, wasted tokens, conflated patterns. Only copy skills essential for your current project.

---

![Context-Driven Development Architecture](https://raw.githubusercontent.com/microsoft/skills/main/.github/assets/agent-skills-image.png)

---

## What's Inside

| Resource | Description |
|--
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `vscode.md`
```markdown
# 📦 microsoft/vscode [🔖 PENDING]
🔗 https://github.com/microsoft/vscode
🌐 https://code.visualstudio.com

## Meta
- **Stars:** ⭐ 183108 | **Forks:** 🍴 38780
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING

## Description:
Visual Studio Code

## README (trích đầu)
```
# Visual Studio Code - Open Source ("Code - OSS")
[![Feature Requests](https://img.shields.io/github/issues/microsoft/vscode/feature-request.svg)](https://github.com/microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+label%3Afeature-request+sort%3Areactions-%2B1-desc)
[![Bugs](https://img.shields.io/github/issues/microsoft/vscode/bug.svg)](https://github.com/microsoft/vscode/issues?utf8=✓&q=is%3Aissue+is%3Aopen+label%3Abug)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-yellow.svg)](https://gitter.im/Microsoft/vscode)

## The Repository

This repository ("`Code - OSS`") is where we (Microsoft) develop the [Visual Studio Code](https://code.visualstudio.com) product together with the community. Not only do we work on code and issues here, we also publish our [roadmap](https://github.com/microsoft/vscode/wiki/Roadmap), [monthly iteration plans](https://github.com/microsoft/vscode/wiki/Iteration-Plans), and our [endgame plans](https://github.com/microsoft/vscode/wiki/Running-the-Endgame). This source code is available to everyone under the standard [MIT license](https://github.com/microsoft/vscode/blob/main/LICENSE.txt).

## Visual Studio Code

<p align="center">
  <img alt="VS Code in action" src="https://user-images.githubusercontent.com/35271042/118224532-3842c400-b438-11eb-923d-a5f66fa6785a.png">
</p>

[Visual Studio Code](https://code.visualstudio.com) is a distribution of the `Code - OSS` repository with Microsoft-specific customizations released under a traditional [Microsoft product license](https://code.visualstudio.com/License/).

[Visual Studio Code](https://code.visualstudio.com) combines the simplicity of a code editor with what developers need for their core edit-build-debug cycle. It provides comprehensive code editing, navigation, and understanding support along with lightweight debugging, a rich extensibility model, and lightweight integration with existing tools.

Visual Studio Code is updated monthly with new features and bug fixes. You can download it for Windows, macOS, and Linux on [Visual Studio Code's website](https://code.visualstudio.com/Download). To get the latest releases every day, install the [Insiders build](https://code.visualstudio.com/insiders).

## Contributing

There are many ways in which you can participate in this project, for example:

* [Submit bugs and feature requests](https://github.com/microsoft/vscode/issues), and help us verify as they are checked in
* Review [source code changes](https://github.com/microsoft/vscode/pulls)
* Review the [documentation](https://github.com/microsoft/vscode-docs) and make pull requests for anything from typos to additional and new content

If you are interested in fixing issues and contributing directly to the code base,
please see the document [How to Contribute](https://github.com/microsoft/vscode/wiki/How-to-Contribute), which covers the following:

* [How to build and run from source](https://github.com/microsoft/vscode/wiki/How-to-Contribute)
* [The development w
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `winget-pkgs.md`
```markdown
# 📦 microsoft/winget-pkgs [🔖 PENDING/APPROVE]
🔗 https://github.com/microsoft/winget-pkgs


## Meta
- **Stars:** ⭐ 10399 | **Forks:** 🍴 6482
- **Language:** PowerShell | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The Microsoft community Windows Package Manager manifest repository

## README (trích đầu)
```
# Windows Package Manager Community Repository

[![Gitter](https://img.shields.io/gitter/room/Microsoft/winget-pkgs)](https://gitter.im/Microsoft/winget-pkgs)
[![Validation Pipeline Badge](https://img.shields.io/endpoint?url=https://winget-validation-pme-f8gqfjhzacawbecy.z01.azurefd.net/api/GetServiceComponentStatusBadge?component=ValidationPipeline "Validation Pipeline Badge")](https://dev.azure.com/shine-oss/winget-pkgs/_build?definitionId=14)
[![Publish Pipeline Badge](https://img.shields.io/endpoint?url=https://winget-validation-pme-f8gqfjhzacawbecy.z01.azurefd.net/api/GetServiceComponentStatusBadge?component=PublishPipeline "Publish Pipeline Badge")](https://dev.azure.com/shine-oss/winget-pkgs/_build?definitionId=12)
[![GitHub Status](https://img.shields.io/endpoint?url=https://api.bittu.eu.org/github-status-badge-endpoint)](https://www.githubstatus.com)
[![Azure Pipelines Status](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fstatus.dev.azure.com%2F_apis%2Fstatus%2Fhealth%3Fservices%3DPipelines%26geographies%3DUS&query=%24.services%5B0%5D.geographies%5B0%5D.health&label=Azure%20Pipelines%20Status
)](https://status.dev.azure.com/)

This repository contains the manifest files for the **Windows Package Manager** default source. You are highly encouraged to submit manifests for your favorite application.

> [!IMPORTANT]
> At this time installers must be MSIX, MSI, APPX, MSIXBundle, APPXBundle, or .exe application installers. Font files (.ttf, .ttc, .otf, .otc, and .fnt) are also supported. Script-based installers are not currently supported.

The **Windows Package Manager** is an [open source client](https://github.com/microsoft/winget-cli) designed for command-line usage. If you are interested in exploring private repositories offering private WinGet package hosting, see [private repositories](../../../README.md).

# Documentation

Please check the [overview](../../../README.md) for detailed topics. Common topics for the WinGet Community repository are available below:
* [Authoring a manifest](../../../README.md#authoring-a-manifest)
* [Testing a manifest](../../../README.md#testing-a-manifest)
* [Submitting a manifest](../../../README.md#submitting-a-manifest)
* [Requesting a new package](../../../core/security/QUARANTINE/incoming/repos/AutoGPT/docs/integrations/block_integrations/github/issues.md#Request-a-New-Package)
* [Requesting a new package version](../../../core/security/QUARANTINE/incoming/repos/AutoGPT/docs/integrations/block_integrations/github/issues.md#Request-a-New-Package-Version)

# Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and do, grant us the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Follow the instructions provided by the bot. You will only need to do this once across all Microsoft repositories using our CLA.

This project has adopted the [Microsoft Open Source 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


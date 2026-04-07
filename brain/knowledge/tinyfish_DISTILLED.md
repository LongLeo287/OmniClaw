---
id: tinyfish
type: knowledge
owner: OA_Triage
---
# tinyfish
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# The TinyFish Cookbook

<a href="https://www.tinyfish.ai/accelerator">
  <img width="1920" height="1080" alt="Tinyfish Accelerator banner" src="https://github.com/user-attachments/assets/bc32bf8b-1a9e-41ea-b690-4bacf41ee132" />
</a>
---

<div align="center">

<table>
<tr>
<td align="center">

### ⛊ &nbsp;&nbsp; **The TinyFish Accelerator is now accepting applications**  &nbsp;&nbsp;  ⛊

*$2M investment seed pool💰* • *9-week program* • *Free credits* • *Engineering support* • *Business mentorship* 

### **[👉 Apply Now 👈](https://www.tinyfish.ai/accelerator)**

</td>
</tr>
</table>

</div>


<div align="center">

[![Website](https://img.shields.io/badge/Website-141414?style=for-the-badge&logo=googlechrome&logoColor=white)](https://tinyfish.ai/)
[![Docs](https://img.shields.io/badge/Docs-526CE5?style=for-the-badge&logo=readthedocs&logoColor=white)](https://docs.tinyfish.ai/)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/tinyfish)
[![License](https://img.shields.io/badge/License-View-green?style=for-the-badge)](LICENSE)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/Tiny_Fish)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/tinyfish-ai/)
[![Threads](https://img.shields.io/badge/Threads-000000?style=for-the-badge&logo=threads&logoColor=white)](https://www.threads.com/@tinyfish_ai)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/tinyfish_ai/)

</div>




## About This Repository

Welcome to the **TinyFish Cookbook!** This is a growing collection of recipes, demos, and automations built with TinyFish.

**🏆 We're SOTA!** — we just scored 90% on Mind2Web benchmark, outperforming Gemini by 21 points, OpenAI by 29, and Anthropic by 34. We ran all 300 tasks in parallel and published every single run publicly. [Read our benchmark results →](https://tinyfish.ai/blog/mind2web) | [View all runs →](https://docs.google.com/spreadsheets/d/1jgRESVlSYygPO4dKKqzPohGUX5b78Ay59422mM29CsU/edit?gid=436688783#gid=436688783)

## What is TinyFish?

**SOTA web agents in an API** that lets you treat real websites like programmable surfaces. Instead of juggling headless browsers, selectors, proxies, and weird edge cases, you call a single API with a goal and some URLs and get back clean JSON. It handles navigation, forms, filters, dynamic content, proxies, and multi-step flows across many sites at once.

The same infrastructure and agents used by big enterprises (like Google, Doordash and Classpass), now for everyone!


## Why TinyFish?
- 🕸️ **Fully managed browser and agent infra in one API**
- 🌐 **Any website → API** — Turn sites without APIs into programmable data sources
- 💬 **Natural language goals** — Send a URL + plain English, get structured JSON back
- 🤖 **Real browser automation** — Multi-step flows, forms, filters, calendars, dynamic content
- 🥷 **Built-in stealth mode** — Rotating proxies + stealth profiles included (no extra cost)
- 📊 **Production-grade logs** — Full observability and debugging for every run
- 🔌 **Flexible integration** — HTTP API, visual Playground, or MCP server for Claude/Cursor

## The Recipes

Each folder in this repo is a standalone project. Dive in to see how to solve real-world problems.

| Recipe | Description |
|--------|-------------|
| [anime-watch-hub](./anime-watch-hub) | Helps you find sites to read/watch your favorite manga/anime for free |
| [bestbet](./bestbet) | Sports betting odds comparison tool |
| [code-reference-finder](./code-reference-finder) | AI-powered code snippet analyzer that finds real-world usage examples from GitHub and Stack Overflow |
| [competitor-analysis](./competitor-analysis) | Live competitive pricing intelligence dashboard |
| [competitor-scout-cli](./competitor-scout-cli) | Natural language CLI tool for researching competitor feature decisions across multiple websites |
| [concept-discovery-system](./concept-discovery-system) | Project idea validator that discovers similar existing projects across GitHub, Dev.to, and Stack Overflow |
| [fast-qa](./fast-qa) | No-code QA testing platform with parallel test execution and live browser previews |
| [game-buying-guide](./game-buying-guide) | Video game buying decision tool comparing pricing and deals across 10 gaming platforms in parallel |
| [lego-hunter](./lego-hunter) | Global inventory search tool finding rare Lego sets across 15+ retailers with price and availability analysis |
| [loan-decision-copilot](./loan-decision-copilot) | AI-powered loan comparison tool across banks and regions |
| [logistics-sentry](./logistics-sentry) | Logistics intelligence platform for port congestion and carrier risk tracking |
| [Manga-Availability-Finder](./Manga-Availability-Finder) | Searches multiple reading platforms for manga/webtoon availability |
| [openbox-deals](./openbox-deals) | Real-time open-box and refurbished deal aggregator across 8 retailers |
| [research-sentry](./research-sentry) | Voice-first academic research co-pilot scanning ArXiv, PubMed, and more |
| [restaurant-comparison-tool](./restaurant-comparison-tool) | Pre-visit restaurant safety intelligence tool analyzing Google Maps reviews, menus, and allergen signals |
| [scholarship-finder](./scholarship-finder) | AI-powered scholarship discovery system pulling live data from official websites |
| [silicon-signal](./silicon-signal) | Semiconductor supply chain tracker for lifecycle, availability, and lead-time signals |
| [stay-scout-hub](./stay-scout-hub) | Searches across all sites for places to stay when traveling for conventions or events |
| [summer-school-finder](./summer-school-finder) | Discover and compare summer school programs from universities around the world |
| [tenders-finder](./tenders-finder) | AI-powered Singapore government tender discovery tool scraping multiple tender portals in parallel |
| [tinyskills](./tinyskills) | Multi-source AI skill guide generator |
| [tutor-finder](./tutor-finder) | AI-powered tutor discovery platform for competitive exams across multiple platforms |
| [viet-bike-scout](./viet-bike-scout) | Motorbike rental price comparison tool across Vietnamese cities using parallel browser agents |
| [waifu-deal-sniper](./waifu-deal-sniper) | Discord bot for anime figure collectors finding discounted pre-owned figures from AmiAmi, Mercari, and Solaris Japan |
| [wing-command](./wing-command) | Chicken wing tracker using AI-powered scraping to find the best wings near you by flavor preference |

### n8n Workflows

Pre-built n8n workflows using TinyFish — import the JSON and go.

| Workflow | Description |
|----------|-------------|
| [Competitor Scout](./N8N_WorkFlows/Competitor%20Scout%20CLI) | Research competitor feature decisions with OpenAI planning and TinyFish evidence collection |
| [Web Research Agent](./N8N_WorkFlows/Web%20Research%20Agent) | Chatbot that scrapes any website with TinyFish and saves summarized reports to Notion |
| [Daily Product Hunt Tracker](./N8N_WorkFlows/Daily%20Product%20Hunt%20Tracker) | Scheduled workflow delivering daily top 5 trending Product Hunt products to Telegram |

> More recipes added weekly!

## Getting Started with the API

You don't need to install heavy SDKs. TinyFish works with standard HTTP requests.

### 1. Get your API Key

Sign up on [tinyfish.ai](https://tinyfish.ai) and grab your API key.

### 2. Run a Command

Here is how to run a simple automation agent:

#### cURL

```bash
curl -N -X POST https://agent.tinyfish.ai/v1/automation/run-sse \
  -H "X-API-Key: $TINYFISH_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://agentql.com",
    "goal": "Find all AgentQL subscription plans and their prices. Return result in json format"
  }'
```

#### Python

```python
import json
import os
import requests

response = requests.post(
    "https://agent.tinyfish.ai/v1/automation/run-sse",
    headers={
        "X-API-Key": os.getenv("TINYFISH_API_KEY"),
        "Content-Type": "application/json",
    },
    json={
        "url": "https://agentql.com",
        "goal": "Find all AgentQL subscription plans and their prices. Return result in json format",
    },
    stream=True,
)

for line in response.iter_lines():
    if line:
        line_str = line.decode("utf-8")
        if line_str.startswith("data: "):
            event = json.loads(line_str[6:])
            print(event)
```

#### TypeScript

```typescript
const response = await fetch("https://agent.tinyfish.ai/v1/automation/run-sse", {
  method: "POST",
  headers: {
    "X-API-Key": process.env.TINYFISH_API_KEY,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    url: "https://agentql.com",
    goal: "Find all AgentQL subscription plans and their prices. Return result in json format",
  }),
});

const reader = response.body.getReader();
const decoder = new TextDecoder();

while (true) {
  const { done, value } = await reader.read();
  if (done) break;
  console.log(decoder.decode(value));
}
```

> By the way! If you want to expose your project on localhost to your friends to show them a demo, you can now use the [tinyfi.sh](https://tinyfi.sh) by us! Completely free and easy to use!


## Star History

<p align="center">
  <a href="https://www.star-history.com/#tinyfish-io/tinyfish-cookbook&type=date">
    <img src="https://api.star-history.com/svg?repos=tinyfish-io/tinyfish-cookbook&type=date&legend=top-left" alt="Star History Chart">
  </a>
</p>

## Contributors

<a href="https://github.com/tinyfish-io/TinyFish-cookbook/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=tinyfish-io/TinyFish-cookbook" />
</a>

Got something cool you built with TinyFish? We want it in here! Check out our [Contributing Guide](CONTRIBUTING.md) for the full rundown on how to submit your project.


## Community & Support

- [Join us on Discord](https://discord.gg/tinyfish) — ask questions, share what you're building, hang out
- Learn more at [tinyfish.ai](https://tinyfish.ai)

## Legal Disclaimer

This repository is a community-driven space for sharing derivatives, code samples, and best practices related to Tiny Fish products. By using the materials in this repository, you acknowledge and agree to the following:
- **"As-Is" Basis**: All code, scripts, and documentation shared here are provided "AS IS" and "AS AVAILABLE." TinyFish makes no warranties of any kind, whether express or implied, regarding the accuracy, reliability, or security of community-contributed content.
- **No Obligation to Maintain**: Tiny Fish is under no obligation to monitor, update, or fix bugs, errors, or security vulnerabilities found in community-contributed derivatives.
- **User Responsibility**: You are solely responsible for vetting and testing any code before implementing it in a production environment. Use of these derivatives is at your own risk.
- **Limitation of Liability**: In no event shall Tiny Fish be held liable for any claim, damages, or other liability—including but not limited to system failures, data loss, or security breaches—arising from the use of or inability to use the contents of this repository.

> Note: Contributions from the community do not represent the official views or supported products of Tiny Fish.
---

<img src="https://github.com/user-attachments/assets/2cf004f0-0065-4f21-9835-12ac693964f1" width="100%" />




```

### File: .tags.json
```json
{
  "repo-owner": "ENG",
  "vanta-dependabot-owner": "ENG",
  "vanta-ebs-inspector-owner": "ENG",
  "vanta-ecr-container-owner": "ENG"
}

```

### File: CONTRIBUTING.md
```md
# Contributing to the TinyFish Cookbook

Hello fellow coder! So you have chosen (or been compelled to) add your awesome mini use case to the TinyFish cookbook, here's some basics on how this cookbook is structured, and how to send in your Pull Request to make the process as smooth as possible.

## Repository Structure

Each project lives in its own folder at the root of this repo — no nesting, no hunting around. Just a flat collection of awesome things people have built with TinyFish.

```
TinyFish-cookbook/
├── .github/
├── brand-sentiment/
├── daily-briefing/
├── price-match/
├── sales-opportunity/
├── YOUR-NEW-PROJECT/        <--- This is you!
│
├── .gitignore
├── .semgrepignore
├── .tags.json
├── .yamllint
├── Makefile
├── README.md
├── CONTRIBUTING.md
└── renovate.json
```

> note: if your new to github, some of the steps below might seem a bit intimidating if your new to contributing to open source repos, but don't worry they become second nature after a while. And if this is your first time, we'd love to get one fo our engineers to hop on a call with you and guide you through! Hit us up on the [TinyFish Discord](https://discord.gg/tinyfish).

## Getting Started

1. Go ahead and fork the repo at https://github.com/tinyfish-io/TinyFish-cookbook
2. Clone this _forked version_ of the repo to your local computer
3. Create a new feature branch for your work (e.g., `git checkout -b {your-name}/cool-new-app`). **Avoid working directly on the `main` branch** to keep your fork clean.
4. Create a new folder at the root of the repo for your project and start coding!

> **Note:** If you need any help with the API, making the app, or anything at all, hit the TinyFish team up anytime at the [TinyFish Discord](https://discord.gg/tinyfish) (we'd love to help)

## Documentation!

Like Julius Caesar once [said](https://www.youtube.com/watch?v=xMHJGd3wwZk&list=RDxMHJGd3wwZk&start_radio=1), "I would have never conquered Rome if it wasn't for good documentation," hence, you too must write good documentation. To make things simple and consistent, we actually have a really easy template.

Each project folder **must** include a `README.md` with the following:

1. **Title**
2. **Live link**
3. **Short 2-3 liner about what your app is, and where the TinyFish API is used**
4. **Demo Video** *(gif or video format, whatever works best)*
5. **Snippet of your codebase that calls the TinyFish API** (the prompt can be truncated if its too long)
6. **How to Run the codebase** (declare any env vars that may be needed here)
7. **Architecture Diagram**

## Submitting Your Project

1. Remember to test your new app thoroughly, and make sure it's has a nice `README.md` as described in the above section
2. Push all your changes to your forked repo
3. Open a pull request, from your fork to the main TinyFish repo https://github.com/tinyfish-io/TinyFish-cookbook (main branch)
4. Sit tight! The very best TinyFish engineers will take a look, give you feedback and test your app!
5. If all's good! Your PR will be merged. Congrats! 🎉

Keep committing often and keep your code safe! And always remember, if you need anything or have any doubts, hit us up at the the [TinyFish Discord](https://discord.gg/tinyfish)

```

### File: golden_images.yaml
```yaml
# =============================================================================
# Golden Images Standard
# =============================================================================
# Managed by:    Infrastructure / DevOps Team
# Source:        https://github.com/tinyfish-io/github-control
# Linear ticket: https://linear.app/tinyfish/issue/INF-1097
#
# This file is automatically replicated to ALL active repositories.
# DO NOT edit this file locally — changes will be overwritten on next
# Terraform apply. To propose updates, open a PR in github-control.
#
# -----------------------------------------------------------------------------
# TIER DEFINITIONS
# -----------------------------------------------------------------------------
#   recommended:
#     DevOps-owned. The Infrastructure team handles OS-level CVE monitoring,
#     Vanta ticket triage, quarterly SHA digest updates, and patch coordination.
#
#   acceptable:
#     Developer-owned. Teams using this image are fully responsible for:
#       - Monitoring OS-level CVEs flagged by AWS Inspector / Vanta
#       - Filing and remediating their own security tickets
#       - Upgrading to the recommended tier before the image's EOL date
#     Using an acceptable-tier image does NOT exempt a team from Vanta SLAs.
#
# -----------------------------------------------------------------------------
# USAGE (Dockerfile)
# -----------------------------------------------------------------------------
#   Always reference the full URI with the SHA256 digest for build immutability.
#   Floating tags (:latest, :22, :3.12) are PROHIBITED in production Dockerfiles.
#
#   CORRECT:
#     FROM node:24-bookworm-slim@sha256:e8e2e91b1378f83c5b2dd15f0247f34110e2fe895f6ca7719dbb780f929368eb
#
#   WRONG:
#     FROM node:24-bookworm-slim
#     FROM node:latest
#     FROM node:22
#
# =============================================================================

golden_images:
  # ---------------------------------------------------------------------------
  # Node.js
  # ---------------------------------------------------------------------------
  nodejs:
    - tier: recommended
      alias: node-24-lts
      image: node:24-bookworm-slim
      uri: node:24-bookworm-slim@sha256:e8e2e91b1378f83c5b2dd15f0247f34110e2fe895f6ca7719dbb780f929368eb
      runtime_version: "24.14.0"
      base_os: Debian 12 (Bookworm) slim
      digest_updated: "2026-02-27"
      eol: "2029-04-30"
      description: >
        Node.js 24 LTS on Debian 12 Bookworm slim. DevOps-managed. Slim variant reduces attack surface vs the full image
        while retaining native-module compatibility (unlike Alpine/musl). Receives timely Debian security patches for
        OS-level packages.
      use_case: "All Node.js services, CI builds, tooling containers."

    - tier: acceptable
      alias: node-22-lts
      image: node:22-bookworm-slim
      uri: node:22-bookworm-slim@sha256:dd9d21971ec4395903fa6143c2b9267d048ae01ca6d3ea96f16cb30df6187d94
      runtime_version: "22.22.0"
      base_os: Debian 12 (Bookworm) slim
      digest_updated: "2026-02-27"
      eol: "2027-04-30"
      description: >
        Node.js 22 LTS on Debian 12 Bookworm slim. DEVELOPER-managed. Teams using this image are responsible for
        OS-level CVE monitoring, patching, and Vanta ticket remediation independently.
      use_case: "Teams not yet migrated to Node 24 LTS."
      caveats:
        - "Migrate to node-24-lts (recommended) before April 2027 EOL."
        - "Developer team owns OS-level CVE patching and all Vanta SLA obligations."

  # ---------------------------------------------------------------------------
  # Python
  # ---------------------------------------------------------------------------
  python:
    - tier: recommended
      alias: python-313
      image: python:3.13-slim-bookworm
      uri: python:3.13-slim-bookworm@sha256:1245b6c39d0b8e49e911c7d07b60cd9ed26016b0e439b6903d5e08730e417553
      runtime_version: "3.13.x"
      base_os: Debian 12 (Bookworm) slim
      digest_updated: "2026-02-27"
      eol: "2029-10-31"
      description: >
        Python 3.13 on Debian 12 Bookworm slim. DevOps-managed. Slim variant minimizes pre-installed packages, reducing
        the OS-level attack surface while remaining fully pip-compatible.
      use_case: "All Python services, ML workloads, data pipelines, Lambda containers."

    - tier: acceptable
      alias: python-312
      image: python:3.12-slim-bookworm
      uri: python:3.12-slim-bookworm@sha256:593bd06efe90efa80dc4eee3948be7c0fde4134606dd40d8dd8dbcade98e669c
      runtime_version: "3.12.12"
      base_os: Debian 12 (Bookworm) slim
      digest_updated: "2026-02-27"
      eol: "2028-10-31"
      description: >
        Python 3.12 on Debian 12 Bookworm slim. DEVELOPER-managed. Teams using this image are responsible for OS-level
        CVE monitoring, patching, and Vanta ticket remediation independently.
      use_case: "Teams not yet migrated to Python 3.13."
      caveats:
        - "Plan migration to python-313 (recommended) before October 2028 EOL."
        - "Developer team owns OS-level CVE patching and all Vanta SLA obligations."

  # ---------------------------------------------------------------------------
  # Microsoft Playwright (AI web automation)
  # ---------------------------------------------------------------------------
  playwright:
    - tier: recommended
      alias: playwright-latest
      image: mcr.microsoft.com/playwright:v1.58.2-noble
      uri: mcr.microsoft.com/playwright:v1.58.2-noble@sha256:65cefd09a5e943921ecd3a6e5414c603db2eb161e9eb48f2e2ccc63486dc7dc0
      runtime_version: "1.58.2"
      base_os: Ubuntu 24.04 LTS (Noble Numbat)
      digest_updated: "2026-02-27"
      description: >
        Microsoft Playwright v1.58.2 on Ubuntu 24.04 LTS (Noble). DevOps-managed. Pre-baked with all browser binaries
        (Chromium, Firefox, WebKit) and their system-level dependencies. Playwright is the backbone of our AI web
        automation workflows, enabling agents to interact with the web at scale.
      use_case: "AI web automation workflows, browser-based AI agents."

    - tier: acceptable
      alias: playwright-v154
      image: mcr.microsoft.com/playwright:v1.54.0-noble
      uri: mcr.microsoft.com/playwright:v1.54.0-noble@sha256:96b27b29220f99ef3205c4aa3a8b8e1b5beb6c3ebb2e9acbdef80cb944a03012
      runtime_version: "1.54.0"
      base_os: Ubuntu 24.04 LTS (Noble Numbat)
      digest_updated: "2026-02-27"
      description: >
        Microsoft Playwright v1.54.0 on Ubuntu 24.04 LTS (Noble). DEVELOPER-managed. Teams using this version are
        responsible for monitoring CVEs and upgrading to the recommended tier.
      use_case: "AI web automation workflows pinned to Playwright 1.54 pending migration."
      caveats:
        - "Upgrade to playwright-latest (recommended) once workflow compatibility with v1.58 is confirmed."
        - "Developer team owns OS-level CVE patching and all Vanta SLA obligations."
        - "4 minor versions behind recommended; bundled browser binaries may carry known CVEs."

# =============================================================================
# Metadata
# =============================================================================
metadata:
  last_reviewed: "2026-02-27"
  next_review_due: "2026-05-27"
  review_cadence: quarterly
  maintained_by: "Infrastructure / DevOps Team"
  linear_ticket: https://linear.app/tinyfish/issue/INF-1097
  policy: >
    All Dockerfiles MUST reference images from this file using the full URI with SHA256 digest (@sha256:...) for build
    immutability. Floating tags (e.g. :latest, :22, :3.12) are PROHIBITED in production Dockerfiles. This file is
    updated quarterly or upon critical CVE disclosure. To propose changes, open a PR in github-control referencing
    INF-1097.

```

### File: renovate.json
```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:recommended"
  ]
}

```

### File: .github\config\.pre-commit-config-template.yaml
```yaml
---
repos:
  - repo: "local"
    hooks:
      - id: "trufflehog"
        name: "TruffleHog"
        description: Detect secrets in your data.
        entry: bash -c 'trufflehog git file://. --since-commit HEAD --results=verified,unknown --fail'
        language: system
        stages: ["pre-commit", "pre-push"]

```


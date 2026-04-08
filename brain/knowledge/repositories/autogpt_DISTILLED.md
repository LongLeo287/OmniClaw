---
id: repo-fetched-autogpt-092954
type: knowledge
owner: OA
registered_at: 2026-04-05T03:38:21.766593
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_AutoGPT_092954

## Assimilation Report
Auto-cloned repository: FETCHED_AutoGPT_092954

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# AutoGPT: Build, Deploy, and Run AI Agents

[![Discord Follow](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdiscord.com%2Fapi%2Finvites%2Fautogpt%3Fwith_counts%3Dtrue&query=%24.approximate_member_count&label=total%20members&logo=discord&logoColor=white&color=7289da)](https://discord.gg/autogpt) &ensp;
[![Twitter Follow](https://img.shields.io/twitter/follow/Auto_GPT?style=social)](https://twitter.com/Auto_GPT) &ensp;

<!-- Keep these links. Translations will automatically update with the README. -->
[Deutsch](https://zdoc.app/de/Significant-Gravitas/AutoGPT) | 
[Español](https://zdoc.app/es/Significant-Gravitas/AutoGPT) | 
[français](https://zdoc.app/fr/Significant-Gravitas/AutoGPT) | 
[日本語](https://zdoc.app/ja/Significant-Gravitas/AutoGPT) | 
[한국어](https://zdoc.app/ko/Significant-Gravitas/AutoGPT) | 
[Português](https://zdoc.app/pt/Significant-Gravitas/AutoGPT) | 
[Русский](https://zdoc.app/ru/Significant-Gravitas/AutoGPT) | 
[中文](https://zdoc.app/zh/Significant-Gravitas/AutoGPT)

**AutoGPT** is a powerful platform that allows you to create, deploy, and manage continuous AI agents that automate complex workflows. 

## Hosting Options 
   - Download to self-host (Free!)
   - [Join the Waitlist](https://bit.ly/3ZDijAI) for the cloud-hosted beta (Closed Beta - Public release Coming Soon!)

## How to Self-Host the AutoGPT Platform
> [!NOTE]
> Setting up and hosting the AutoGPT Platform yourself is a technical process. 
> If you'd rather something that just works, we recommend [joining the waitlist](https://bit.ly/3ZDijAI) for the cloud-hosted beta.

### System Requirements

Before proceeding with the installation, ensure your system meets the following requirements:

#### Hardware Requirements
- CPU: 4+ cores recommended
- RAM: Minimum 8GB, 16GB recommended
- Storage: At least 10GB of free space

#### Software Requirements
- Operating Systems:
  - Linux (Ubuntu 20.04 or newer recommended)
  - macOS (10.15 or newer)
  - Windows 10/11 with WSL2
- Required Software (with minimum versions):
  - Docker Engine (20.10.0 or newer)
  - Docker Compose (2.0.0 or newer)
  - Git (2.30 or newer)
  - Node.js (16.x or newer)
  - npm (8.x or newer)
  - VSCode (1.60 or newer) or any modern code editor

#### Network Requirements
- Stable internet connection
- Access to required ports (will be configured in Docker)
- Ability to make outbound HTTPS connections

### Updated Setup Instructions:
We've moved to a fully maintained and regularly updated documentation site.

👉 [Follow the official self-hosting guide here](https://agpt.co/docs/platform/getting-started/getting-started)


This tutorial assumes you have Docker, VSCode, git and npm installed.

---

#### ⚡ Quick Setup with One-Line Script (Recommended for Local Hosting)

Skip the manual steps and get started in minutes using our automatic setup script.

For macOS/Linux:
```
curl -fsSL https://setup.agpt.co/install.sh -o install.sh && bash install.sh
```

For Windows (PowerShell):
```
powershell -c "iwr https://setup.agpt.co/install.bat -o install.bat; ./install.bat"
```

This will install dependencies, configure Docker, and launch your local instance — all in one go.

### 🧱 AutoGPT Frontend

The AutoGPT frontend is where users interact with our powerful AI automation platform. It offers multiple ways to engage with and leverage our AI agents. This is the interface where you'll bring your AI automation ideas to life:

   **Agent Builder:** For those who want to customize, our intuitive, low-code interface allows you to design and configure your own AI agents. 
   
   **Workflow Management:** Build, modify, and optimize your automation workflows with ease. You build your agent by connecting blocks, where each block     performs a single action.
   
   **Deployment Controls:** Manage the lifecycle of your agents, from testing to production.
   
   **Ready-to-Use Agents:** Don't want to build? Simply select from our library of pre-configured agents and put them to work immediately.
   
   **Agent Interaction:** Whether you've built your own or are using pre-configured agents, easily run and interact with them through our user-friendly      interface.

   **Monitoring and Analytics:** Keep track of your agents' performance and gain insights to continually improve your automation processes.

[Read this guide](https://docs.agpt.co/platform/new_blocks/) to learn how to build your own custom blocks.

### 💽 AutoGPT Server

The AutoGPT Server is the powerhouse of our platform This is where your agents run. Once deployed, agents can be triggered by external sources and can operate continuously. It contains all the essential components that make AutoGPT run smoothly.

   **Source Code:** The core logic that drives our agents and automation processes.
   
   **Infrastructure:** Robust systems that ensure reliable and scalable performance.
   
   **Marketplace:** A comprehensive marketplace where you can find and deploy a wide range of pre-built agents.

### 🐙 Example Agents

Here are two examples of what you can do with AutoGPT:

1. **Generate Viral Videos from Trending Topics**
   - This agent reads topics on Reddit.
   - It identifies trending topics.
   - It then automatically creates a short-form video based on the content. 

2. **Identify Top Quotes from Videos for Social Media**
   - This agent subscribes to your YouTube channel.
   - When you post a new video, it transcribes it.
   - It uses AI to identify the most impactful quotes to generate a summary.
   - Then, it writes a post to automatically publish to your social media. 

These examples show just a glimpse of what you can achieve with AutoGPT! You can create customized workflows to build agents for any use case.

---

### **License Overview:**

🛡️ **Polyform Shield License:**
All code and content within the `autogpt_platform` folder is licensed under the Polyform Shield License. This new project is our in-developlemt platform for building, deploying and managing agents.</br>_[Read more about this effort](https://agpt.co/blog/introducing-the-autogpt-platform)_

🦉 **MIT License:**
All other portions of the AutoGPT repository (i.e., everything outside the `autogpt_platform` folder) are licensed under the MIT License. This includes the original stand-alone AutoGPT Agent, along with projects such as [Forge](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/forge), [agbenchmark](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/benchmark) and the [AutoGPT Classic GUI](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/frontend).</br>We also publish additional work under the MIT Licence in other repositories, such as [GravitasML](https://github.com/Significant-Gravitas/gravitasml) which is developed for and used in the AutoGPT Platform. See also our MIT Licenced [Code Ability](https://github.com/Significant-Gravitas/AutoGPT-Code-Ability) project.

---
### Mission
Our mission is to provide the tools, so that you can focus on what matters:

- 🏗️ **Building** - Lay the foundation for something amazing.
- 🧪 **Testing** - Fine-tune your agent to perfection.
- 🤝 **Delegating** - Let AI work for you, and have your ideas come to life.

Be part of the revolution! **AutoGPT** is here to stay, at the forefront of AI innovation.

**📖 [Documentation](https://docs.agpt.co)**
&ensp;|&ensp;
**🚀 [Contributing](CONTRIBUTING.md)**

---
## 🤖 AutoGPT Classic
> Below is information about the classic version of AutoGPT.

**🛠️ [Build your own Agent - Quickstart](classic/FORGE-QUICKSTART.md)**

### 🏗️ Forge

**Forge your own agent!** &ndash; Forge is a ready-to-go toolkit to build your own agent application. It handles most of the boilerplate code, letting you channel all your creativity into the things that set *your* agent apart. All tutorials are located [here](https://medium.com/@aiedge/autogpt-forge-e3de53cc58ec). Components from [`forge`](/classic/forge/) can also be used individually to speed up development and reduce boilerplate in your agent project.

🚀 [**Getting Started with Forge**](https://github.com/Significant-Gravitas/AutoGPT/blob/master/classic/forge/tutorials/001_getting_started.md) &ndash;
This guide will walk you through the process of creating your own agent and using the benchmark and user interface.

📘 [Learn More](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/forge) about Forge

### 🎯 Benchmark

**Measure your agent's performance!** The `agbenchmark` can be used with any agent that supports the agent protocol, and the integration with the project's [CLI] makes it even easier to use with AutoGPT and forge-based agents. The benchmark offers a stringent testing environment. Our framework allows for autonomous, objective performance evaluations, ensuring your agents are primed for real-world action.

<!-- TODO: insert visual demonstrating the benchmark -->

📦 [`agbenchmark`](https://pypi.org/project/agbenchmark/) on Pypi
&ensp;|&ensp;
📘 [Learn More](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/benchmark) about the Benchmark

### 💻 UI

**Makes agents easy to use!** The `frontend` gives you a user-friendly interface to control and monitor your agents. It connects to agents through the [agent protocol](#-agent-protocol), ensuring compatibility with many agents from both inside and outside of our ecosystem.

<!-- TODO: insert screenshot of front end -->

The frontend works out-of-the-box with all agents in the repo. Just use the [CLI] to run your agent of choice!

📘 [Learn More](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/frontend) about the Frontend

### ⌨️ CLI

[CLI]: #-cli

To make it as easy as possible to use all of the tools offered by the repository, a CLI is included at the root of the repo:

```shell
$ ./run
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  agent      Commands to create, start and stop agents
  benchmark  Commands to start the benchmark and list tests and categories
  setup      Installs dependencies needed for your system.
```

Just clone the repo, install dependencies with `./run setup`, and you should be good to go!

## 🤔 Questions? Problems? Suggestions?

### Get help - [Discord 💬](https://discord.gg/autogpt)

[![Join us on Discord](https://invidget.switchblade.xyz/autogpt)](https://discord.gg/autogpt)

To report a bug or request a feature, create a [GitHub Issue](https://github.com/Significant-Gravitas/AutoGPT/issues/new/choose). Please ensure someone else hasn't created an issue for the same topic.

## 🤝 Sister projects

### 🔄 Agent Protocol

To maintain a uniform standard and ensure seamless compatibility with many current and future applications, AutoGPT employs the [agent protocol](https://agentprotocol.ai/) standard by the AI Engineer Foundation. This standardizes the communication pathways from your agent to the frontend and benchmark.

---

## Stars stats

<p align="center">
<a href="https://star-history.com/#Significant-Gravitas/AutoGPT">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Significant-Gravitas/AutoGPT&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Significant-Gravitas/AutoGPT&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Significant-Gravitas/AutoGPT&type=Date" />
  </picture>
</a>
</p>


## ⚡ Contributors

<a href="https://github.com/Significant-Gravitas/AutoGPT/graphs/contributors" alt="View Contributors">
  <img src="https://contrib.rocks/image?repo=Significant-Gravitas/AutoGPT&max=1000&columns=10" alt="Contributors" />
</a>

```

### File: AGENTS.md
```md
# AutoGPT Platform Contribution Guide

This guide provides context for Codex when updating the **autogpt_platform** folder.

## Directory overview

- `autogpt_platform/backend` – FastAPI based backend service.
- `autogpt_platform/autogpt_libs` – Shared Python libraries.
- `autogpt_platform/frontend` – Next.js + Typescript frontend.
- `autogpt_platform/docker-compose.yml` – development stack.

See `docs/content/platform/getting-started.md` for setup instructions.

## Code style

- Format Python code with `poetry run format`.
- Format frontend code using `pnpm format`.

## Frontend guidelines:

See `/frontend/CONTRIBUTING.md` for complete patterns. Quick reference:

1. **Pages**: Create in `src/app/(platform)/feature-name/page.tsx`
   - Add `usePageName.ts` hook for logic
   - Put sub-components in local `components/` folder
2. **Components**: Structure as `ComponentName/ComponentName.tsx` + `useComponentName.ts` + `helpers.ts`
   - Use design system components from `src/components/` (atoms, molecules, organisms)
   - Never use `src/components/__legacy__/*`
3. **Data fetching**: Use generated API hooks from `@/app/api/__generated__/endpoints/`
   - Regenerate with `pnpm generate:api`
   - Pattern: `use{Method}{Version}{OperationName}`
4. **Styling**: Tailwind CSS only, use design tokens, Phosphor Icons only
5. **Testing**: Add Storybook stories for new components, Playwright for E2E
6. **Code conventions**: Function declarations (not arrow functions) for components/handlers

- Component props should be `interface Props { ... }` (not exported) unless the interface needs to be used outside the component
- Separate render logic from business logic (component.tsx + useComponent.ts + helpers.ts)
- Colocate state when possible and avoid creating large components, use sub-components ( local `/components` folder next to the parent component ) when sensible
- Avoid large hooks, abstract logic into `helpers.ts` files when sensible
- Use function declarations for components, arrow functions only for callbacks
- No barrel files or `index.ts` re-exports
- Avoid comments at all times unless the code is very complex
- Do not use `useCallback` or `useMemo` unless asked to optimise a given function
- Do not type hook returns, let Typescript infer as much as possible
- Never type with `any`, if not types available use `unknown`

## Testing

- Backend: `poetry run test` (runs pytest with a docker based postgres + prisma).
- Frontend: `pnpm test` or `pnpm test-ui` for Playwright tests. See `docs/content/platform/contributing/tests.md` for tips.

Always run the relevant linters and tests before committing.
Use conventional commit messages for all commits (e.g. `feat(backend): add API`).
Types: - feat - fix - refactor - ci - dx (developer experience)
Scopes: - platform - platform/library - platform/marketplace - backend - backend/executor - frontend - frontend/library - frontend/marketplace - blocks

## Pull requests

- Use the template in `.github/PULL_REQUEST_TEMPLATE.md`.
- Rely on the pre-commit checks for linting and formatting
- Fill out the **Changes** section and the checklist.
- Use conventional commit titles with a scope (e.g. `feat(frontend): add feature`).
- Keep out-of-scope changes under 20% of the PR.
- Ensure PR descriptions are complete.
- For changes touching `data/*.py`, validate user ID checks or explain why not needed.
- If adding protected frontend routes, update `frontend/lib/supabase/middleware.ts`.
- Use the linear ticket branch structure if given codex/open-1668-resume-dropped-runs

```

### File: CODE_OF_CONDUCT.md
```md
# Code of Conduct for AutoGPT

## 1. Purpose

The purpose of this Code of Conduct is to provide guidelines for contributors to the AutoGPT projects on GitHub. We aim to create a positive and inclusive environment where all participants can contribute and collaborate effectively. By participating in this project, you agree to abide by this Code of Conduct.

## 2. Scope

This Code of Conduct applies to all contributors, maintainers, and users of the AutoGPT project. It extends to all project spaces, including but not limited to issues, pull requests, code reviews, comments, and other forms of communication within the project.

## 3. Our Standards

We encourage the following behavior:

* Being respectful and considerate to others
* Actively seeking diverse perspectives
* Providing constructive feedback and assistance
* Demonstrating empathy and understanding

We discourage the following behavior:

* Harassment or discrimination of any kind
* Disrespectful, offensive, or inappropriate language or content
* Personal attacks or insults
* Unwarranted criticism or negativity

## 4. Reporting and Enforcement

If you witness or experience any violations of this Code of Conduct, please report them to the project maintainers by email or other appropriate means. The maintainers will investigate and take appropriate action, which may include warnings, temporary or permanent bans, or other measures as necessary.

Maintainers are responsible for ensuring compliance with this Code of Conduct and may take action to address any violations.

## 5. Acknowledgements

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/version/2/0/code_of_conduct.html).

## 6. Contact

If you have any questions or concerns, please contact the project maintainers on Discord:
https://discord.gg/autogpt

```

### File: CONTRIBUTING.md
```md
# AutoGPT Contribution Guide
If you are reading this, you are probably looking for the full **[contribution guide]**,
which is part of our [wiki].

[contribution guide]: https://github.com/Significant-Gravitas/AutoGPT/wiki/Contributing
[wiki]: https://github.com/Significant-Gravitas/AutoGPT/wiki
[roadmap]: https://github.com/Significant-Gravitas/AutoGPT/discussions/6971
[kanban board]: https://github.com/orgs/Significant-Gravitas/projects/1

## Contributing to the AutoGPT Platform Folder
All contributions to [the autogpt_platform folder](https://github.com/Significant-Gravitas/AutoGPT/blob/master/autogpt_platform) will be under our [Contribution License Agreement](https://github.com/Significant-Gravitas/AutoGPT/blob/master/autogpt_platform/Contributor%20License%20Agreement%20(CLA).md). By making a pull request contributing to this folder, you agree to the terms of our CLA for your contribution. All contributions to other folders will be under the MIT license.

## In short
1. Avoid duplicate work, issues, PRs etc.
2. We encourage you to collaborate with fellow community members on some of our bigger
   [todo's][roadmap]!
   * We highly recommend to post your idea and discuss it in the [dev channel].
3. Create a draft PR when starting work on bigger changes.
4. Adhere to the [Code Guidelines]
5. Clearly explain your changes when submitting a PR.
6. Don't submit broken code: test/validate your changes.
7. Avoid making unnecessary changes, especially if they're purely based on your personal
   preferences. Doing so is the maintainers' job. ;-)
8. Please also consider contributing something other than code; see the
   [contribution guide] for options.

[dev channel]: https://discord.com/channels/1092243196446249134/1095817829405704305
[code guidelines]: https://github.com/Significant-Gravitas/AutoGPT/wiki/Contributing#code-guidelines

If you wish to involve with the project (beyond just contributing PRs), please read the
wiki page about [Catalyzing](https://github.com/Significant-Gravitas/AutoGPT/wiki/Catalyzing).

In fact, why not just look through the whole wiki (it's only a few pages) and
hop on our Discord. See you there! :-)

❤️ & 🔆
The team @ AutoGPT
https://discord.gg/autogpt

```

### File: SECURITY.md
```md
# Security Policy

## Reporting Security Issues

We take the security of our project seriously. If you believe you have found a security vulnerability, please report it to us privately. **Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**

> **Important Note**: Any code within the `classic/` folder is considered legacy, unsupported, and out of scope for security reports. We will not address security vulnerabilities in this deprecated code.

Instead, please report them via:
- [GitHub Security Advisory](https://github.com/Significant-Gravitas/AutoGPT/security/advisories/new)
<!--- [Huntr.dev](https://huntr.com/repos/significant-gravitas/autogpt) - where you may be eligible for a bounty-->

### Reporting Process
1. **Submit Report**: Use one of the above channels to submit your report
2. **Response Time**: Our team will acknowledge receipt of your report within 14 business days.
3. **Collaboration**: We will collaborate with you to understand and validate the issue
4. **Resolution**: We will work on a fix and coordinate the release process

### Disclosure Policy
- Please provide detailed reports with reproducible steps
- Include the version/commit hash where you discovered the vulnerability
- Allow us a 90-day security fix window before any public disclosure
- After patch is released, allow 30 days for users to update before public disclosure (for a total of 120 days max between update time and fix time)
- Share any potential mitigations or workarounds if known

## Supported Versions
Only the following versions are eligible for security updates:

| Version | Supported |
|---------|-----------|
| Latest release on master branch | ✅ |
| Development commits (pre-master) | ✅ |
| Classic folder (deprecated) | ❌ |
| All other versions | ❌ |

## Security Best Practices
When using this project:
1. Always use the latest stable version
2. Review security advisories before updating
3. Follow our security documentation and guidelines
4. Keep your dependencies up to date
5. Do not use code from the `classic/` folder as it is deprecated and unsupported

## Past Security Advisories
For a list of past security advisories, please visit our [Security Advisory Page](https://github.com/Significant-Gravitas/AutoGPT/security/advisories) and [Huntr Disclosures Page](https://huntr.com/repos/significant-gravitas/autogpt).

---
Last updated: November 2024

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for autogpt
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\copilot-instructions.md
```md
# GitHub Copilot Instructions for AutoGPT

This file provides comprehensive onboarding information for GitHub Copilot coding agent to work efficiently with the AutoGPT repository.

## Repository Overview

**AutoGPT** is a powerful platform for creating, deploying, and managing continuous AI agents that automate complex workflows. This is a large monorepo (~150MB) containing multiple components:

- **AutoGPT Platform** (`autogpt_platform/`) - Main focus: Modern AI agent platform (Polyform Shield License)
- **Classic AutoGPT** (`classic/`) - Legacy agent system (MIT License)
- **Documentation** (`docs/`) - MkDocs-based documentation site
- **Infrastructure** - Docker configurations, CI/CD, and development tools

**Primary Languages & Frameworks:**

- **Backend**: Python 3.10-3.13, FastAPI, Prisma ORM, PostgreSQL, RabbitMQ
- **Frontend**: TypeScript, Next.js 15, React, Tailwind CSS, Radix UI
- **Development**: Docker, Poetry, pnpm, Playwright, Storybook

## Build and Validation Instructions

### Essential Setup Commands

**Always run these commands in the correct directory and in this order:**

1. **Initial Setup** (required once):

   ```bash
   # Clone and enter repository
   git clone <repo> && cd AutoGPT

   # Start all services (database, redis, rabbitmq, clamav)
   cd autogpt_platform && docker compose --profile local up deps --build --detach
   ```

2. **Backend Setup** (always run before backend development):

   ```bash
   cd autogpt_platform/backend
   poetry install                    # Install dependencies
   poetry run prisma migrate dev     # Run database migrations
   poetry run prisma generate        # Generate Prisma client
   ```

3. **Frontend Setup** (always run before frontend development):
   ```bash
   cd autogpt_platform/frontend
   pnpm install                      # Install dependencies
   ```

### Runtime Requirements

**Critical:** Always ensure Docker services are running before starting development:

```bash
cd autogpt_platform && docker compose --profile local up deps --build --detach
```

**Python Version:** Use Python 3.11 (required; managed by Poetry via pyproject.toml)
**Node.js Version:** Use Node.js 21+ with pnpm package manager

### Development Commands

**Backend Development:**

```bash
cd autogpt_platform/backend
poetry run serve                     # Start development server (port 8000)
poetry run test                      # Run all tests (requires ~5 minutes)
poetry run pytest path/to/test.py    # Run specific test
poetry run format                    # Format code (Black + isort) - always run first
poetry run lint                      # Lint code (ruff) - run after format
```

**Frontend Development:**

```bash
cd autogpt_platform/frontend
pnpm dev                            # Start development server (port 3000) - use for active development
pnpm build                          # Build for production (only needed for E2E tests or deployment)
pnpm test                           # Run Playwright E2E tests (requires build first)
pnpm test-ui                        # Run tests with UI
pnpm format                         # Format and lint code
pnpm storybook                      # Start component development server
```

### Testing Strategy

**Backend Tests:**

- **Block Tests**: `poetry run pytest backend/blocks/test/test_block.py -xvs` (validates all blocks)
- **Specific Block**: `poetry run pytest 'backend/blocks/test/test_block.py::test_available_blocks[BlockName]' -xvs`
- **Snapshot Tests**: Use `--snapshot-update` when output changes, always review with `git diff`

**Frontend Tests:**

- **E2E Tests**: Always run `pnpm dev` before `pnpm test` (Playwright requires running instance)
- **Component Tests**: Use Storybook for isolated component development

### Critical Validation Steps

**Before committing changes:**

1. Run `poetry run format` (backend) and `pnpm format` (frontend)
2. Ensure all tests pass in modified areas
3. Verify Docker services are still running
4. Check that database migrations apply cleanly

**Common Issues & Workarounds:**

- **Prisma issues**: Run `poetry run prisma generate` after schema changes
- **Permission errors**: Ensure Docker has proper permissions
- **Port conflicts**: Check the `docker-compose.yml` file for the current list of exposed ports. You can list all mapped ports with:
- **Test timeouts**: Backend tests can take 5+ minutes, use `-x` flag to stop on first failure

## Project Layout & Architecture

### Core Architecture

**AutoGPT Platform** (`autogpt_platform/`):

- `backend/` - FastAPI server with async support
  - `backend/backend/` - Core API logic
  - `backend/blocks/` - Agent execution blocks
  - `backend/data/` - Database models and schemas
  - `schema.prisma` - Database schema definition
- `frontend/` - Next.js application
  - `src/app/` - App Router pages and layouts
  - `src/components/` - Reusable React components
  - `src/lib/` - Utilities and configurations
- `autogpt_libs/` - Shared Python utilities
- `docker-compose.yml` - Development stack orchestration

**Key Configuration Files:**

- `pyproject.toml` - Python dependencies and tooling
- `package.json` - Node.js dependencies and scripts
- `schema.prisma` - Database schema and migrations
- `next.config.mjs` - Next.js configuration
- `tailwind.config.ts` - Styling configuration

### Security & Middleware

**Cache Protection**: Backend includes middleware preventing sensitive data caching in browsers/proxies
**Authentication**: JWT-based with Supabase integration
**User ID Validation**: All data access requires user ID checks - verify this for any `data/*.py` changes

### Development Workflow

**GitHub Actions**: Multiple CI/CD workflows in `.github/workflows/`

- `platform-backend-ci.yml` - Backend testing and validation
- `platform-frontend-ci.yml` - Frontend testing and validation
- `platform-fullstack-ci.yml` - End-to-end integration tests

**Pre-commit Hooks**: Run linting and formatting checks
**Conventional Commits**: Use format `type(scope): description` (e.g., `feat(backend): add API`)

### Key Source Files

**Backend Entry Points:**

- `backend/backend/api/rest_api.py` - FastAPI application setup
- `backend/backend/data/` - Database models and user management
- `backend/blocks/` - Agent execution blocks and logic

**Frontend Entry Points:**

- `frontend/src/app/layout.tsx` - Root application layout
- `frontend/src/app/page.tsx` - Home page
- `frontend/src/lib/supabase/` - Authentication and database client

**Protected Routes**: Update `frontend/lib/supabase/middleware.ts` when adding protected routes

### Agent Block System

Agents are built using a visual block-based system where each block performs a single action. Blocks are defined in `backend/blocks/` and must include:

- Block definition with input/output schemas
- Execution logic with proper error handling
- Tests validating functionality

### Database & ORM

**Prisma ORM** with PostgreSQL backend including pgvector for embeddings:

- Schema in `schema.prisma`
- Migrations in `backend/migrations/`
- Always run `prisma migrate dev` and `prisma generate` after schema changes

## Environment Configuration

### Configuration Files Priority Order

1. **Backend**: `/backend/.env.default` → `/backend/.env` (user overrides)
2. **Frontend**: `/frontend/.env.default` → `/frontend/.env` (user overrides)
3. **Platform**: `/.env.default` (Supabase/shared) → `/.env` (user overrides)
4. Docker Compose `environment:` sections override file-based config
5. Shell environment variables have highest precedence

### Docker Environment Setup

- All services use hardcoded defaults (no `${VARIABLE}` substitutions)
- The `env_file` directive loads variables INTO containers at runtime
- Backend/Frontend services use YAML anchors for consistent configuration
- Copy `.env.default` files to `.env` for local development customization

## Advanced Development Patterns

### Adding New Blocks

1. Create file in `/backend/backend/blocks/`
2. Inherit from `Block` base class with input/output schemas
3. Implement `run` method with proper error handling
4. Generate block UUID using `uuid.uuid4()`
5. Register in block registry
6. Write tests alongside block implementation
7. Consider how inputs/outputs connect with other blocks in graph editor

### API Development

1. Update routes in `/backend/backend/api/features/`
2. Add/update Pydantic models in same directory
3. Write tests alongside route files
4. For `data/*.py` changes, validate user ID checks
5. Run `poetry run test` to verify changes

### Frontend Development

**📖 Complete Frontend Guide**: See `autogpt_platform/frontend/CONTRIBUTING.md` and `autogpt_platform/frontend/.cursorrules` for comprehensive patterns and conventions.

**Quick Reference:**

**Component Structure:**

- Separate render logic from data/behavior
- Structure: `ComponentName/ComponentName.tsx` + `useComponentName.ts` + `helpers.ts`
- Exception: Small components (3-4 lines of logic) can be inline
- Render-only components can be direct files without folders

**Data Fetching:**

- Use generated API hooks from `@/app/api/__generated__/endpoints/`
- Generated via Orval from backend OpenAPI spec
- Pattern: `use{Method}{Version}{OperationName}`
- Example: `useGetV2ListLibraryAgents`
- Regenerate with: `pnpm generate:api`
- **Never** use deprecated `BackendAPI` or `src/lib/autogpt-server-api/*`

**Code Conventions:**

- Use function declarations for components and handlers (not arrow functions)
- Only arrow functions for small inline lambdas (map, filter, etc.)
- Components: `PascalCase`, Hooks: `camelCase` with `use` prefix
- No barrel files or `index.ts` re-exports
- Minimal comments (code should be self-documenting)

**Styling:**

- Use Tailwind CSS utilities only
- Use design system components from `src/components/` (atoms, molecules, organisms)
- Never use `src/components/__legacy__/*`
- Only use Phosphor Icons (`@phosphor-icons/react`)
- Prefer design tokens over hardcoded values

**Error Handling:**

- Render errors: Use `<ErrorCard />` component
- Mutation errors: Display with toast notifications
- Manual exceptions: Use `Sentry.captureException()`
- Global error boundaries already configured

**Testing:**

- Add/update Storybook stories for UI components (`pnpm storybook`)
- Run Playwright E2E tests with `pnpm test`
- Verify in Chromatic after PR

**Architecture:**

- Default to client components ("use client")
- Server components only for SEO or extreme TTFB needs
- Use React Query for server state (via generated hooks)
- Co-locate UI state in components/hooks

### Security Guidelines

**Cache Protection Middleware** (`/backend/backend/api/middleware/security.py`):

- Default: Disables caching for ALL endpoints with `Cache-Control: no-store, no-cache, must-revalidate, private`
- Uses allow list approach for cacheable paths (static assets, health checks, public pages)
- Prevents sensitive data caching in browsers/proxies
- Add new cacheable endpoints to `CACHEABLE_PATHS`

### CI/CD Alignment

The repository has comprehensive CI workflows that test:

- **Backend**: Python 3.11-3.13, services (Redis/RabbitMQ/ClamAV), Prisma migrations, Poetry lock validation
- **Frontend**: Node.js 21, pnpm, Playwright with Docker Compose stack, API schema validation
- **Integration**: Full-stack type checking and E2E testing

Match these patterns when developing locally - the copilot setup environment mirrors these CI configurations.

## Collaboration with Other AI Assistants

This repository is actively developed with assistance from Claude (via CLAUDE.md files). When working on this codebase:

- Check for existing CLAUDE.md files that provide additional context
- Follow established patterns and conventions already in the codebase
- Maintain consistency with existing code style and architecture
- Consider that changes may be reviewed and extended by both human developers and AI assistants

## Trust These Instructions

These instructions are comprehensive and tested. Only perform additional searches if:

1. Information here is incomplete for your specific task
2. You encounter errors not covered by the workarounds
3. You need to understand implementation details not covered above

For detailed platform development patterns, refer to `autogpt_platform/CLAUDE.md` and `AGENTS.md` in the repository root.

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
### Why / What / How

<!-- Why: Why does this PR exist? What problem does it solve, or what's broken/missing without it? -->
<!-- What: What does this PR change? Summarize the changes at a high level. -->
<!-- How: How does it work? Describe the approach, key implementation details, or architecture decisions. -->

### Changes 🏗️

<!-- List the key changes. Keep it higher level than the diff but specific enough to highlight what's new/modified. -->

### Checklist 📋

#### For code changes:
- [ ] I have clearly listed my changes in the PR description
- [ ] I have made a test plan
- [ ] I have tested my changes according to the test plan:
  <!-- Put your test plan here: -->
  - [ ] ...

<details>
  <summary>Example test plan</summary>
  
  - [ ] Create from scratch and execute an agent with at least 3 blocks
  - [ ] Import an agent from file upload, and confirm it executes correctly
  - [ ] Upload agent to marketplace
  - [ ] Import an agent from marketplace and confirm it executes correctly
  - [ ] Edit an agent from monitor, and confirm it executes correctly
</details>

#### For configuration changes:

- [ ] `.env.default` is updated or already compatible with my changes
- [ ] `docker-compose.yml` is updated or already compatible with my changes
- [ ] I have included a list of my configuration changes in the PR description (under **Changes**)

<details>
  <summary>Examples of configuration changes</summary>

  - Changing ports
  - Adding new services that need to communicate with each other
  - Secrets or environment variable changes
  - New or infrastructure changes such as databases
</details>

```

### File: .claude\skills\pr-address\SKILL.md
```md
---
name: pr-address
description: Address PR review comments and loop until CI green and all comments resolved. TRIGGER when user asks to address comments, fix PR feedback, respond to reviewers, or babysit/monitor a PR.
user-invocable: true
argument-hint: "[PR number or URL] — if omitted, finds PR for current branch."
metadata:
  author: autogpt-team
  version: "1.0.0"
---

# PR Address

## Find the PR

```bash
gh pr list --head $(git branch --show-current) --repo Significant-Gravitas/AutoGPT
gh pr view {N}
```

## Read the PR description

Understand the **Why / What / How** before addressing comments — you need context to make good fixes:

```bash
gh pr view {N} --json body --jq '.body'
```

## Fetch comments (all sources)

### 1. Inline review threads — GraphQL (primary source of actionable items)

Use GraphQL to fetch inline threads. It natively exposes `isResolved`, returns threads already grouped with all replies, and paginates via cursor — no manual thread reconstruction needed.

```bash
gh api graphql -f query='
{
  repository(owner: "Significant-Gravitas", name: "AutoGPT") {
    pullRequest(number: {N}) {
      reviewThreads(first: 100) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          isResolved
          path
          comments(last: 1) {
            nodes { databaseId body author { login } createdAt }
          }
        }
      }
    }
  }
}'
```

If `pageInfo.hasNextPage` is true, fetch subsequent pages by adding `after: "<endCursor>"` to `reviewThreads(first: 100, after: "...")` and repeat until `hasNextPage` is false.

**Filter to unresolved threads only** — skip any thread where `isResolved: true`. `comments(last: 1)` returns the most recent comment in the thread — act on that; it reflects the reviewer's final ask. Use the thread `id` (Relay global ID) to track threads across polls.

### 2. Top-level reviews — REST (MUST paginate)

```bash
gh api repos/Significant-Gravitas/AutoGPT/pulls/{N}/reviews --paginate
```

**CRITICAL — always `--paginate`.** Reviews default to 30 per page. PRs can have 80–170+ reviews (mostly empty resolution events). Without pagination you miss reviews past position 30 — including `autogpt-reviewer`'s structured review which is typically posted after several CI runs and sits well beyond the first page.

Two things to extract:
- **Overall state**: look for `CHANGES_REQUESTED` or `APPROVED` reviews.
- **Actionable feedback**: non-empty bodies only. Empty-body reviews are thread-resolution events — they indicate progress but have no feedback to act on.

**Where each reviewer posts:**
- `autogpt-reviewer` — posts detailed structured reviews ("Blockers", "Should Fix", "Nice to Have") as **top-level reviews**. Not present on every PR. Address ALL items.
- `sentry[bot]` — posts bug predictions as **inline threads**. Fix real bugs, explain false positives.
- `coderabbitai[bot]` — posts summaries as **top-level reviews** AND actionable items as **inline threads**. Address actionable items.
- Human reviewers — can post in any source. Address ALL non-empty feedback.

### 3. PR conversation comments — REST

```bash
gh api repos/Significant-Gravitas/AutoGPT/issues/{N}/comments --paginate
```

Mostly contains: bot summaries (`coderabbitai[bot]`), CI/conflict detection (`github-actions[bot]`), and author status updates. Scan for non-empty messages from non-bot human reviewers that aren't the PR author — those are the ones that need a response.

## For each unaddressed comment

Address comments **one at a time**: fix → commit → push → inline reply → next.

1. Read the referenced code, make the fix (or reply explaining why it's not needed)
2. Commit and push the fix
3. Reply **inline** (not as a new top-level comment) referencing the fixing commit — this is what resolves the conversation for bot reviewers (coderabbitai, sentry):

| Comment type | How to reply |
|---|---|
| Inline review (`pulls/{N}/comments`) | `gh api repos/Significant-Gravitas/AutoGPT/pulls/{N}/comments/{ID}/replies -f body="🤖 Fixed in <commit-sha>: <description>"` |
| Conversation (`issues/{N}/comments`) | `gh api repos/Significant-Gravitas/AutoGPT/issues/{N}/comments -f body="🤖 Fixed in <commit-sha>: <description>"` |

## Format and commit

After fixing, format the changed code:

- **Backend** (from `autogpt_platform/backend/`): `poetry run format`
- **Frontend** (from `autogpt_platform/frontend/`): `pnpm format && pnpm lint && pnpm types`

If API routes changed, regenerate the frontend client:
```bash
cd autogpt_platform/backend && poetry run rest &
REST_PID=$!
trap "kill $REST_PID 2>/dev/null" EXIT
WAIT=0; until curl -sf http://localhost:8006/health > /dev/null 2>&1; do sleep 1; WAIT=$((WAIT+1)); [ $WAIT -ge 60 ] && echo "Timed out" && exit 1; done
cd ../frontend && pnpm generate:api:force
kill $REST_PID 2>/dev/null; trap - EXIT
```
Never manually edit files in `src/app/api/__generated__/`.

Then commit and **push immediately** — never batch commits without pushing. Each fix should be visible on GitHub right away so CI can start and reviewers can see progress.

**Never push empty commits** (`git commit --allow-empty`) to re-trigger CI or bot checks. When a check fails, investigate the root cause (unchecked PR checklist, unaddressed review comments, code issues) and fix those directly. Empty commits add noise to git history.

For backend commits in worktrees: `poetry run git commit` (pre-commit hooks).

## The loop

```text
address comments → format → commit → push
→ wait for CI (while addressing new comments) → fix failures → push
→ re-check comments after CI settles
→ repeat until: all comments addressed AND CI green AND no new comments arriving
```

### Polling for CI + new comments

After pushing, poll for **both** CI status and new comments in a single loop. Do not use `gh pr checks --watch` — it blocks the tool and prevents reacting to new comments while CI is running.

> **Note:** `gh pr checks --watch --fail-fast` is tempting but it blocks the entire Bash tool call, meaning the agent cannot check for or address new comments until CI fully completes. Always poll manually instead.

**Polling loop — repeat every 30 seconds:**

1. Check CI status:
```bash
gh pr checks {N} --repo Significant-Gravitas/AutoGPT --json bucket,name,link
```
   Parse the results: if every check has `bucket` of `"pass"` or `"skipping"`, CI is green. If any has `"fail"`, CI has failed. Otherwise CI is still pending.

2. Check for merge conflicts:
```bash
gh pr view {N} --repo Significant-Gravitas/AutoGPT --json mergeable --jq '.mergeable'
```
   If the result is `"CONFLICTING"`, the PR has a merge conflict — see "Resolving merge conflicts" below. If `"UNKNOWN"`, GitHub is still computing mergeability — wait and re-check next poll.

3. Check for new/changed comments (all three sources):

   **Inline threads** — re-run the GraphQL query from "Fetch comments". For each unresolved thread, record `{thread_id, last_comment_databaseId}` as your baseline. On each poll, action is needed if:
   - A new thread `id` appears that wasn't in the baseline (new thread), OR
   - An existing thread's `last_comment_databaseId` has changed (new reply on existing thread)

   **Conversation comments:**
   ```bash
   gh api repos/Significant-Gravitas/AutoGPT/issues/{N}/comments --paginate
   ```
   Compare total count and newest `id` against baseline. Filter to non-empty, non-bot, non-author-update messages.

   **Top-level reviews:**
   ```bash
   gh api repos/Significant-Gravitas/AutoGPT/pulls/{N}/reviews --paginate
   ```
   Watch for new non-empty reviews (`CHANGES_REQUESTED` or `COMMENTED` with body). Compare total count and newest `id` against baseline.

4. **React in this precedence order (first match wins):**

| What happened | Action |
|---|---|
| Merge conflict detected | See "Resolving merge conflicts" below. |
| Mergeability is `UNKNOWN` | GitHub is still computing mergeability. Sleep 30 seconds, then restart polling from the top. |
| New comments detected | Address them (fix → commit → push → reply). After pushing, re-fetch all comments to update your baseline, then restart this polling loop from the top (new commits invalidate CI status). |
| CI failed (bucket == "fail") | Get failed check links: `gh pr checks {N} --repo Significant-Gravitas/AutoGPT --json bucket,link --jq '.[] \| select(.bucket == "fail") \| .link'`. Extract run ID from link (format: `.../actions/runs/<run-id>/job/...`), read logs with `gh run view <run-id> --repo Significant-Gravitas/AutoGPT --log-failed`. Fix → commit → push → restart polling. |
| CI green + no new comments | **Do not exit immediately.** Bots (coderabbitai, sentry) often post reviews shortly after CI settles. Continue polling for **2 more cycles (60s)** after CI goes green. Only exit after 2 consecutive green+quiet polls. |
| CI pending + no new comments | Sleep 30 seconds, then poll again. |

**The loop ends when:** CI fully green + all comments addressed + **2 consecutive polls with no new comments after CI settled.**

### Resolving merge conflicts

1. Identify the PR's target branch and remote:
```bash
gh pr view {N} --repo Significant-Gravitas/AutoGPT --json baseRefName --jq '.baseRefName'
git remote -v   # find the remote pointing to Significant-Gravitas/AutoGPT (typically 'upstream' in forks, 'origin' for direct contributors)
```

2. Pull the latest base branch with a 3-way merge:
```bash
git pull {base-remote} {base-branch} --no-rebase
```

3. Resolve conflicting files, then verify no conflict markers remain:
```bash
if grep -R -n -E '^(<<<<<<<|=======|>>>>>>>)' <conflicted-files>; then
  echo "Unresolved conflict markers found — resolve before proceeding."
  exit 1
fi
```

4. Stage and push:
```bash
git add <conflicted-files>
git commit -m "Resolve merge conflicts with {base-branch}"
git push
```

5. Restart the polling loop from the top — new commits reset CI status.

```

### File: .claude\skills\pr-review\SKILL.md
```md
---
name: pr-review
description: Review a PR for correctness, security, code quality, and testing issues. TRIGGER when user asks to review a PR, check PR quality, or give feedback on a PR.
user-invocable: true
args: "[PR number or URL] — if omitted, finds PR for current branch."
metadata:
  author: autogpt-team
  version: "1.0.0"
---

# PR Review

## Find the PR

```bash
gh pr list --head $(git branch --show-current) --repo Significant-Gravitas/AutoGPT
gh pr view {N}
```

## Read the PR description

Before reading code, understand the **why**, **what**, and **how** from the PR description:

```bash
gh pr view {N} --json body --jq '.body'
```

Every PR should have a Why / What / How structure. If any of these are missing, note it as feedback.

## Read the diff

```bash
gh pr diff {N}
```

## Fetch existing review comments

Before posting anything, fetch existing inline comments to avoid duplicates:

```bash
gh api repos/Significant-Gravitas/AutoGPT/pulls/{N}/comments --paginate
gh api repos/Significant-Gravitas/AutoGPT/pulls/{N}/reviews
```

## What to check

**Description quality:** Does the PR description cover Why (motivation/problem), What (summary of changes), and How (approach/implementation details)? If any are missing, request them — you can't judge the approach without understanding the problem and intent.

**Correctness:** logic errors, off-by-one, missing edge cases, race conditions (TOCTOU in file access, credit charging), error handling gaps, async correctness (missing `await`, unclosed resources).

**Security:** input validation at boundaries, no injection (command, XSS, SQL), secrets not logged, file paths sanitized (`os.path.basename()` in error messages).

**Code quality:** apply rules from backend/frontend CLAUDE.md files.

**Architecture:** DRY, single responsibility, modular functions. `Security()` vs `Depends()` for FastAPI auth. `data:` for SSE events, `: comment` for heartbeats. `transaction=True` for Redis pipelines.

**Testing:** edge cases covered, colocated `*_test.py` (backend) / `__tests__/` (frontend), mocks target where symbol is **used** not defined, `AsyncMock` for async.

## Output format

Every comment **must** be prefixed with `🤖` and a criticality badge:

| Tier | Badge | Meaning |
|---|---|---|
| Blocker | `🔴 **Blocker**` | Must fix before merge |
| Should Fix | `🟠 **Should Fix**` | Important improvement |
| Nice to Have | `🟡 **Nice to Have**` | Minor suggestion |
| Nit | `🔵 **Nit**` | Style / wording |

Example: `🤖 🔴 **Blocker**: Missing error handling for X — suggest wrapping in try/except.`

## Post inline comments

For each finding, post an inline comment on the PR (do not just write a local report):

```bash
# Get the latest commit SHA for the PR
COMMIT_SHA=$(gh api repos/Significant-Gravitas/AutoGPT/pulls/{N} --jq '.head.sha')

# Post an inline comment on a specific file/line
gh api repos/Significant-Gravitas/AutoGPT/pulls/{N}/comments \
  -f body="🤖 🔴 **Blocker**: <description>" \
  -f commit_id="$COMMIT_SHA" \
  -f path="<file path>" \
  -F line=<line number>
```

```

### File: .claude\skills\pr-test\SKILL.md
```md
---
name: pr-test
description: "E2E manual testing of PRs/branches using docker compose, agent-browser, and API calls. TRIGGER when user asks to manually test a PR, test a feature end-to-end, or run integration tests against a running system."
user-invocable: true
argument-hint: "[worktree path or PR number] — tests the PR in the given worktree. Optional flags: --fix (auto-fix issues found)"
metadata:
  author: autogpt-team
  version: "2.0.0"
---

# Manual E2E Test

Test a PR/branch end-to-end by building the full platform, interacting via browser and API, capturing screenshots, and reporting results.

## Critical Requirements

These are NON-NEGOTIABLE. Every test run MUST satisfy ALL the following:

### 1. Screenshots at Every Step
- Take a screenshot at EVERY significant test step — not just at the end
- Every test scenario MUST have at least one BEFORE and one AFTER screenshot
- Name screenshots sequentially: `{NN}-{action}-{state}.png` (e.g., `01-credits-before.png`, `02-credits-after.png`)
- If a screenshot is missing for a scenario, the test is INCOMPLETE — go back and take it

### 2. Screenshots MUST Be Posted to PR
- Push ALL screenshots to a temp branch `test-screenshots/pr-{N}`
- Post a PR comment with ALL screenshots embedded inline using GitHub raw URLs
- This is NOT optional — every test run MUST end with a PR comment containing screenshots
- If screenshot upload fails, retry. If it still fails, list failed files and require manual drag-and-drop/paste attachment in the PR comment

### 3. State Verification with Before/After Evidence
- For EVERY state-changing operation (API call, user action), capture the state BEFORE and AFTER
- Log the actual API response values (e.g., `credits_before=100, credits_after=95`)
- Screenshot MUST show the relevant UI state change
- Compare expected vs actual values explicitly — do not just eyeball it

### 4. Negative Test Cases Are Mandatory
- Test at least ONE negative case per feature (e.g., insufficient credits, invalid input, unauthorized access)
- Verify error messages are user-friendly and accurate
- Verify the system state did NOT change after a rejected operation

### 5. Test Report Must Include Full Evidence
Each test scenario in the report MUST have:
- **Steps**: What was done (exact commands or UI actions)
- **Expected**: What should happen
- **Actual**: What actually happened
- **API Evidence**: Before/after API response values for state-changing operations
- **Screenshot Evidence**: Before/after screenshots with explanations

## State Manipulation for Realistic Testing

When testing features that depend on specific states (rate limits, credits, quotas):

1. **Use Redis CLI to set counters directly:**
   ```bash
   # Find the Redis container
   REDIS_CONTAINER=$(docker ps --format '{{.Names}}' | grep redis | head -1)
   # Set a key with expiry
   docker exec $REDIS_CONTAINER redis-cli SET key value EX ttl
   # Example: Set rate limit counter to near-limit
   docker exec $REDIS_CONTAINER redis-cli SET "rate_limit:user:test@test.com" 99 EX 3600
   # Example: Check current value
   docker exec $REDIS_CONTAINER redis-cli GET "rate_limit:user:test@test.com"
   ```

2. **Use API calls to check before/after state:**
   ```bash
   # BEFORE: Record current state
   BEFORE=$(curl -s -H "Authorization: Bearer $TOKEN" http://localhost:8006/api/credits | jq '.credits')
   echo "Credits BEFORE: $BEFORE"

   # Perform the action...

   # AFTER: Record new state and compare
   AFTER=$(curl -s -H "Authorization: Bearer $TOKEN" http://localhost:8006/api/credits | jq '.credits')
   echo "Credits AFTER: $AFTER"
   echo "Delta: $(( BEFORE - AFTER ))"
   ```

3. **Take screenshots BEFORE and AFTER state changes** — the UI must reflect the backend state change

4. **Never rely on mocked/injected browser state** — always use real backend state. Do NOT use `agent-browser eval` to fake UI state. The backend must be the source of truth.

5. **Use direct DB queries when needed:**
   ```bash
   # Query via Supabase's PostgREST or docker exec into the DB
   docker exec supabase-db psql -U supabase_admin -d postgres -c "SELECT credits FROM user_credits WHERE user_id = '...';"
   ```

6. **After every API test, verify the state change actually persisted:**
   ```bash
   # Example: After a credits purchase, verify DB matches API
   API_CREDITS=$(curl -s -H "Authorization: Bearer $TOKEN" http://localhost:8006/api/credits | jq '.credits')
   DB_CREDITS=$(docker exec supabase-db psql -U supabase_admin -d postgres -t -c "SELECT credits FROM user_credits WHERE user_id = '...';" | tr -d ' ')
   [ "$API_CREDITS" = "$DB_CREDITS" ] && echo "CONSISTENT" || echo "MISMATCH: API=$API_CREDITS DB=$DB_CREDITS"
   ```

## Arguments

- `$ARGUMENTS` — worktree path (e.g. `$REPO_ROOT`) or PR number
- If `--fix` flag is present, auto-fix bugs found and push fixes (like pr-address loop)

## Step 0: Resolve the target

```bash
# If argument is a PR number, find its worktree
gh pr view {N} --json headRefName --jq '.headRefName'
# If argument is a path, use it directly
```

Determine:
- `REPO_ROOT` — the root repo directory: `git -C "$WORKTREE_PATH" worktree list | head -1 | awk '{print $1}'` (or `git rev-parse --show-toplevel` if not a worktree)
- `WORKTREE_PATH` — the worktree directory
- `PLATFORM_DIR` — `$WORKTREE_PATH/autogpt_platform`
- `BACKEND_DIR` — `$PLATFORM_DIR/backend`
- `FRONTEND_DIR` — `$PLATFORM_DIR/frontend`
- `PR_NUMBER` — the PR number (from `gh pr list --head $(git branch --show-current)`)
- `PR_TITLE` — the PR title, slugified (e.g. "Add copilot permissions" → "add-copilot-permissions")
- `RESULTS_DIR` — `$REPO_ROOT/test-results/PR-{PR_NUMBER}-{slugified-title}`

Create the results directory:
```bash
PR_NUMBER=$(cd $WORKTREE_PATH && gh pr list --head $(git branch --show-current) --repo Significant-Gravitas/AutoGPT --json number --jq '.[0].number')
PR_TITLE=$(cd $WORKTREE_PATH && gh pr list --head $(git branch --show-current) --repo Significant-Gravitas/AutoGPT --json title --jq '.[0].title' | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-//;s/-$//' | head -c 50)
RESULTS_DIR="$REPO_ROOT/test-results/PR-${PR_NUMBER}-${PR_TITLE}"
mkdir -p $RESULTS_DIR
```

**Test user credentials** (for logging into the UI or verifying results manually):
- Email: `test@test.com`
- Password: `testtest123`

## Step 1: Understand the PR

Before testing, understand what changed:

```bash
cd $WORKTREE_PATH

# Read PR description to understand the WHY
gh pr view {N} --json body --jq '.body'

git log --oneline dev..HEAD | head -20
git diff dev --stat
```

Read the PR description (Why / What / How) and changed files to understand:
0. **Why** does this PR exist? What problem does it solve?
1. **What** feature/fix does this PR implement?
2. **How** does it work? What's the approach?
3. What components are affected? (backend, frontend, copilot, executor, etc.)
4. What are the key user-facing behaviors to test?

## Step 2: Write test scenarios

Based on the PR analysis, write a test plan to `$RESULTS_DIR/test-plan.md`:

```markdown
# Test Plan: PR #{N} — {title}

## Scenarios
1. [Scenario name] — [what to verify]
2. ...

## API Tests (if applicable)
1. [Endpoint] — [expected behavior]
   - Before state: [what to check before]
   - After state: [what to verify changed]

## UI Tests (if applicable)
1. [Page/component] — [interaction to test]
   - Screenshot before: [what to capture]
   - Screenshot after: [what to capture]

## Negative Tests (REQUIRED — at least one per feature)
1. [What should NOT happen] — [how to trigger it]
   - Expected error: [what error message/code]
   - State unchanged: [what to verify did NOT change]
```

**Be critical** — include edge cases, error paths, and security checks. Every scenario MUST specify what screenshots to take and what state to verify.

## Step 3: Environment setup

### 3a. Copy .env files from the root worktree

The root worktree (`$REPO_ROOT`) has the canonical `.env` files with all API keys. Copy them to the target worktree:

```bash
# CRITICAL: .env files are NOT checked into git. They must be copied manually.
cp $REPO_ROOT/autogpt_platform/.env $PLATFORM_DIR/.env
cp $REPO_ROOT/autogpt_platform/backend/.env $BACKEND_DIR/.env
cp $REPO_ROOT/autogpt_platform/frontend/.env $FRONTEND_DIR/.env
```

### 3b. Configure copilot authentication

The copilot needs an LLM API to function. Two approaches (try subscription first):

#### Option 1: Subscription mode (preferred — uses your Claude Max/Pro subscription)

The `claude_agent_sdk` Python package **bundles its own Claude CLI binary** — no need to install `@anthropic-ai/claude-code` via npm. The backend auto-provisions credentials from environment variables on startup.

Run the helper script to extract tokens from your host and auto-update `backend/.env` (works on macOS, Linux, and Windows/WSL):

```bash
# Extracts OAuth tokens and writes CLAUDE_CODE_OAUTH_TOKEN + CLAUDE_CODE_REFRESH_TOKEN into .env
bash $BACKEND_DIR/scripts/refresh_claude_token.sh --env-file $BACKEND_DIR/.env
```

**How it works:** The script reads the OAuth token from:
- **macOS**: system keychain (`"Claude Code-credentials"`)
- **Linux/WSL**: `~/.claude/.credentials.json`
- **Windows**: `%APPDATA%/claude/.credentials.json`

It sets `CLAUDE_CODE_OAUTH_TOKEN`, `CLAUDE_CODE_REFRESH_TOKEN`, and `CHAT_USE_CLAUDE_CODE_SUBSCRIPTION=true` in the `.env` file. On container startup, the backend auto-provisions `~/.claude/.credentials.json` inside the container from these env vars. The SDK's bundled CLI then authenticates using that file. No `claude login`, no npm install needed.

**Note:** The OAuth token expires (~24h). If copilot returns auth errors, re-run the script and restart: `$BACKEND_DIR/scripts/refresh_claude_token.sh --env-file $BACKEND_DIR/.env && docker compose up -d copilot_executor`

#### Option 2: OpenRouter API key mode (fallback)

If subscription mode doesn't work, switch to API key mode using OpenRouter:

```bash
# In $BACKEND_DIR/.env, ensure these are set:
CHAT_USE_CLAUDE_CODE_SUBSCRIPTION=false
CHAT_API_KEY=<value of OPEN_ROUTER_API_KEY from the same .env>
CHAT_BASE_URL=https://openrouter.ai/api/v1
CHAT_USE_CLAUDE_AGENT_SDK=true
```

Use `sed` to update these values:
```bash
ORKEY=$(grep "^OPEN_ROUTER_API_KEY=" $BACKEND_DIR/.env | cut -d= -f2)
[ -n "$ORKEY" ] || { echo "ERROR: OPEN_ROUTER_API_KEY is missing in $BACKEND_DIR/.env"; exit 1; }
perl -i -pe 's/CHAT_USE_CLAUDE_CODE_SUBSCRIPTION=true/CHAT_USE_CLAUDE_CODE_SUBSCRIPTION=false/' $BACKEND_DIR/.env
# Add or update CHAT_API_KEY and CHAT_BASE_URL
grep -q "^CHAT_API_KEY=" $BACKEND_DIR/.env && perl -i -pe "s|^CHAT_API_KEY=.*|CHAT_API_KEY=$ORKEY|" $BACKEND_DIR/.env || echo "CHAT_API_KEY=$ORKEY" >> $BACKEND_DIR/.env
grep -q "^CHAT_BASE_URL=" $BACKEND_DIR/.env && perl -i -pe 's|^CHAT_BASE_URL=.*|CHAT_BASE_URL=https://openrouter.ai/api/v1|' $BACKEND_DIR/.env || echo "CHAT_BASE_URL=https://openrouter.ai/api/v1" >> $BACKEND_DIR/.env
```

### 3c. Stop conflicting containers

```bash
# Stop any running app containers (keep infra: supabase, redis, rabbitmq, clamav)
docker ps --format "{{.Names}}" | grep -E "rest_server|executor|copilot|websocket|database_manager|scheduler|notification|frontend|migrate" | while read name; do
  docker stop "$name" 2>/dev/null
done
```

### 3e. Build and start

```bash
cd $PLATFORM_DIR && docker compose build --no-cache 2>&1 | tail -20
if [ ${PIPESTATUS[0]} -ne 0 ]; then echo "ERROR: Docker build failed"; exit 1; fi

cd $PLATFORM_DIR && docker compose up -d 2>&1 | tail -20
if [ ${PIPESTATUS[0]} -ne 0 ]; then echo "ERROR: Docker compose up failed"; exit 1; fi
```

**Note:** If the container appears to be running old code (e.g. missing PR changes), use `docker compose build --no-cache` to force a full rebuild. Docker BuildKit may sometimes reuse cached `COPY` layers from a previous build on a different branch.

**Expected time: 3-8 minutes** for build, 5-10 minutes with `--no-cache`.

### 3f. Wait for services to be ready

```bash
# Poll until backend and frontend respond
for i in $(seq 1 60); do
  BACKEND=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8006/docs 2>/dev/null)
  FRONTEND=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:3000 2>/dev/null)
  if [ "$BACKEND" = "200" ] && [ "$FRONTEND" = "200" ]; then
    echo "Services ready"
    break
  fi
  sleep 5
done
```


### 3h. Create test user and get auth token

```bash
ANON_KEY=$(grep "NEXT_PUBLIC_SUPABASE_ANON_KEY=" $FRONTEND_DIR/.env | sed 's/.*NEXT_PUBLIC_SUPABASE_ANON_KEY=//' | tr -d '[:space:]')

# Signup (idempotent — returns "User already registered" if exists)
RESULT=$(curl -s -X POST 'http://localhost:8000/auth/v1/signup' \
  -H "apikey: $ANON_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"email":"test@test.com","password":"testtest123"}')

# If "Database error finding user", restart supabase-auth and retry
if echo "$RESULT" | grep -q "Database error"; then
  docker restart supabase-auth && sleep 5
  curl -s -X POST 'http://localhost:8000/auth/v1/signup' \
    -H "apikey: $ANON_KEY" \
    -H 'Content-Type: application/json' \
    -d '{"email":"test@test.com","password":"testtest123"}'
fi

# Get auth token
TOKEN=$(curl -s -X POST 'http://localhost:8000/auth/v1/token?grant_type=password' \
  -H "apikey: $ANON_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"email":"test@test.com","password":"testtest123"}' | jq -r '.access_token // ""')
```

**Use this token for ALL API calls:**
```bash
curl -H "Authorization: Bearer $TOKEN" http://localhost:8006/api/...
```

## Step 4: Run tests

### Service ports reference

| Service | Port | URL |
|---------|------|-----|
| Frontend | 3000 | http://localhost:3000 |
| Backend REST | 8006 | http://localhost:8006 |
| Supabase Auth (via Kong) | 8000 | http://localhost:8000 |
| Executor | 8002 | http://localhost:8002 |
| Copilot Executor | 8008 | http://localhost:8008 |
| WebSocket | 8001 | http://localhost:8001 |
| Database Manager | 8005 | http://localhost:8005 |
| Redis | 6379 | localhost:6379 |
| RabbitMQ | 5672 | localhost:5672 |

### API testing

Use `curl` with the auth token for backend API tests. **For EVERY API call that changes state, record before/after values:**

```bash
# Example: List agents
curl -s -H "Authorization: Bearer $TOKEN" http://localhost:8006/api/graphs | jq . | head -20

# Example: Create an agent
curl -s -X POST http://localhost:8006/api/graphs \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{...}' | jq .

# Example: Run an agent
curl -s -X POST "http://localhost:8006/api/graphs/{graph_id}/execute" \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{"data": {...}}'

# Example: Get execution results
curl -s -H "Authorization: Bearer $TOKEN" \
  "http://localhost:8006/api/graphs/{graph_id}/executions/{exec_id}" | jq .
```

**State verification pattern (use for EVERY state-changing API call):**
```bash
# 1. Record BEFORE state
BEF
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

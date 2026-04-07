---
id: project
type: knowledge
owner: OA_Triage
---
# project
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "project-nomad",
  "version": "1.31.0",
  "description": "\"",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "Crosstalk Solutions, LLC",
  "license": "ISC"
}

```

### File: README.md
```md
<div align="center">
<img src="admin/public/project_nomad_logo.webp" width="200" height="200"/>

# Project N.O.M.A.D.
### Node for Offline Media, Archives, and Data

**Knowledge That Never Goes Offline**

[![Website](https://img.shields.io/badge/Website-projectnomad.us-blue)](https://www.projectnomad.us)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2)](https://discord.com/invite/crosstalksolutions)
[![Benchmark](https://img.shields.io/badge/Benchmark-Leaderboard-green)](https://benchmark.projectnomad.us)

</div>

---

Project N.O.M.A.D. is a self-contained, offline-first knowledge and education server packed with critical tools, knowledge, and AI to keep you informed and empowered—anytime, anywhere.

## Installation & Quickstart
Project N.O.M.A.D. can be installed on any Debian-based operating system (we recommend Ubuntu). Installation is completely terminal-based, and all tools and resources are designed to be accessed through the browser, so there's no need for a desktop environment if you'd rather setup N.O.M.A.D. as a "server" and access it through other clients.

*Note: sudo/root privileges are required to run the install script*

### Quick Install (Debian-based OS Only)
```bash
sudo apt-get update && \
sudo apt-get install -y curl && \
curl -fsSL https://raw.githubusercontent.com/Crosstalk-Solutions/project-nomad/refs/heads/main/install/install_nomad.sh \
  -o install_nomad.sh && \
sudo bash install_nomad.sh
```

Project N.O.M.A.D. is now installed on your device! Open a browser and navigate to `http://localhost:8080` (or `http://DEVICE_IP:8080`) to start exploring!

For a complete step-by-step walkthrough (including Ubuntu installation), see the [Installation Guide](https://www.projectnomad.us/install).

### Advanced Installation
For more control over the installation process, copy and paste the [Docker Compose template](https://raw.githubusercontent.com/Crosstalk-Solutions/project-nomad/refs/heads/main/install/management_compose.yaml) into a `docker-compose.yml` file and customize it to your liking (be sure to replace any placeholders with your actual values). Then, run `docker compose up -d` to start the Command Center and its dependencies. Note: this method is recommended for advanced users only, as it requires familiarity with Docker and manual configuration before starting.

## How It Works
N.O.M.A.D. is a management UI ("Command Center") and API that orchestrates a collection of containerized tools and resources via [Docker](https://www.docker.com/). It handles installation, configuration, and updates for everything — so you don't have to.

**Built-in capabilities include:**
- **AI Chat with Knowledge Base** — local AI chat powered by [Ollama](https://ollama.com/) or you can use OpenAI API compatible software such as LM Studio or llama.cpp, with document upload and semantic search (RAG via [Qdrant](https://qdrant.tech/))
- **Information Library** — offline Wikipedia, medical references, ebooks, and more via [Kiwix](https://kiwix.org/)
- **Education Platform** — Khan Academy courses with progress tracking via [Kolibri](https://learningequality.org/kolibri/)
- **Offline Maps** — downloadable regional maps via [ProtoMaps](https://protomaps.com)
- **Data Tools** — encryption, encoding, and analysis via [CyberChef](https://gchq.github.io/CyberChef/)
- **Notes** — local note-taking via [FlatNotes](https://github.com/dullage/flatnotes)
- **System Benchmark** — hardware scoring with a [community leaderboard](https://benchmark.projectnomad.us)
- **Easy Setup Wizard** — guided first-time configuration with curated content collections

N.O.M.A.D. also includes built-in tools like a Wikipedia content selector, ZIM library manager, and content explorer.

## What's Included

| Capability | Powered By | What You Get |
|-----------|-----------|-------------|
| Information Library | Kiwix | Offline Wikipedia, medical references, survival guides, ebooks |
| AI Assistant | Ollama + Qdrant | Built-in chat with document upload and semantic search |
| Education Platform | Kolibri | Khan Academy courses, progress tracking, multi-user support |
| Offline Maps | ProtoMaps | Downloadable regional maps with search and navigation |
| Data Tools | CyberChef | Encryption, encoding, hashing, and data analysis |
| Notes | FlatNotes | Local note-taking with markdown support |
| System Benchmark | Built-in | Hardware scoring, Builder Tags, and community leaderboard |

## Device Requirements
While many similar offline survival computers are designed to be run on bare-minimum, lightweight hardware, Project N.O.M.A.D. is quite the opposite. To install and run the
available AI tools, we highly encourage the use of a beefy, GPU-backed device to make the most of your install.

At it's core, however, N.O.M.A.D. is still very lightweight. For a barebones installation of the management application itself, the following minimal specs are required:

*Note: Project N.O.M.A.D. is not sponsored by any hardware manufacturer and is designed to be as hardware-agnostic as possible. The harware listed below is for example/comparison use only*

#### Minimum Specs
- Processor: 2 GHz dual-core processor or better
- RAM: 4GB system memory
- Storage: At least 5 GB free disk space
- OS: Debian-based (Ubuntu recommended)
- Stable internet connection (required during install only)

To run LLM's and other included AI tools:

#### Optimal Specs
- Processor: AMD Ryzen 7 or Intel Core i7 or better
- RAM: 32 GB system memory
- Graphics: NVIDIA RTX 3060 or AMD equivalent or better (more VRAM = run larger models)
- Storage: At least 250 GB free disk space (preferably on SSD)
- OS: Debian-based (Ubuntu recommended)
- Stable internet connection (required during install only)

**For detailed build recommendations at three price points ($150–$1,000+), see the [Hardware Guide](https://www.projectnomad.us/hardware).**

Again, Project N.O.M.A.D. itself is quite lightweight - it's the tools and resources you choose to install with N.O.M.A.D. that will determine the specs required for your unique deployment

#### Running AI models on a different host
By default, N.O.M.A.D.'s installer will attempt to setup Ollama on the host when the AI Assistant is installed. However, if you would like to run the AI model on a different host, you can go to the settings of of the AI assistant and input a URL for either an ollama or OpenAI-compatible API server (such as LM Studio).  
Note that if you use Ollama on a different host, you must start the server with this option `OLLAMA_HOST=0.0.0.0`.  
Ollama is the preferred way to use the AI assistant as it has features such as model download that OpenAI API does not support. So when using LM Studio for example, you will have to use LM Studio to download models.
You are responsible for the setup of Ollama/OpenAI server on the other host.

## Frequently Asked Questions (FAQ)
For answers to common questions about Project N.O.M.A.D., please see our [FAQ](FAQ.md) page.

## About Internet Usage & Privacy
Project N.O.M.A.D. is designed for offline usage. An internet connection is only required during the initial installation (to download dependencies) and if you (the user) decide to download additional tools and resources at a later time. Otherwise, N.O.M.A.D. does not require an internet connection and has ZERO built-in telemetry.

To test internet connectivity, N.O.M.A.D. attempts to make a request to Cloudflare's utility endpoint, `https://1.1.1.1/cdn-cgi/trace` and checks for a successful response.

## About Security
By design, Project N.O.M.A.D. is intended to be open and available without hurdles - it includes no authentication. If you decide to connect your device to a local network after install (e.g. for allowing other devices to access it's resources), you can block/open ports to control which services are exposed.

**Will authentication be added in the future?** Maybe. It's not currently a priority, but if there's enough demand for it, we may consider building in an optional authentication layer in a future release to support uses cases where multiple users need access to the same instance but with different permission levels (e.g. family use with parental controls, classroom use with teacher/admin accounts, etc.). We have a suggestion for this on our public roadmap, so if this is something you'd like to see, please upvote it here: https://roadmap.projectnomad.us/posts/1/user-authentication-please-build-in-user-auth-with-admin-user-roles

For now, we recommend using network-level controls to manage access if you're planning to expose your N.O.M.A.D. instance to other devices on a local network. N.O.M.A.D. is not designed to be exposed directly to the internet, and we strongly advise against doing so unless you really know what you're doing, have taken appropriate security measures, and understand the risks involved.

## Contributing
Contributions are welcome and appreciated! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to the project.

## Community & Resources

- **Website:** [www.projectnomad.us](https://www.projectnomad.us) - Learn more about the project
- **Discord:** [Join the Community](https://discord.com/invite/crosstalksolutions) - Get help, share your builds, and connect with other NOMAD users
- **Benchmark Leaderboard:** [benchmark.projectnomad.us](https://benchmark.projectnomad.us) - See how your hardware stacks up against other NOMAD builds
- **Troubleshooting Guide:** [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Find solutions to common issues
- **FAQ:** [FAQ.md](FAQ.md) - Find answers to frequently asked questions

## License

Project N.O.M.A.D. is licensed under the [Apache License 2.0](LICENSE).

## Helper Scripts
Once installed, Project N.O.M.A.D. has a few helper scripts should you ever need to troubleshoot issues or perform maintenance that can't be done through the Command Center. All of these scripts are found in Project N.O.M.A.D.'s install directory, `/opt/project-nomad`

###

###### Start Script - Starts all installed project containers
```bash
sudo bash /opt/project-nomad/start_nomad.sh
```
###

###### Stop Script - Stops all installed project containers
```bash
sudo bash /opt/project-nomad/stop_nomad.sh
```
###

###### Update Script - Attempts to pull the latest images for the Command Center and its dependencies (i.e. mysql) and recreate the containers. Note: this *only* updates the Command Center containers. It does not update the installable application containers - that should be done through the Command Center UI
```bash
sudo bash /opt/project-nomad/update_nomad.sh
```

###### Uninstall Script - Need to start fresh? Use the uninstall script to make your life easy. Note: this cannot be undone!
```bash
curl -fsSL https://raw.githubusercontent.com/Crosstalk-Solutions/project-nomad/refs/heads/main/install/uninstall_nomad.sh -o uninstall_nomad.sh && sudo bash uninstall_nomad.sh
```

```

### File: admin\package.json
```json
{
  "name": "project-nomad-admin",
  "version": "0.0.0",
  "private": true,
  "type": "module",
  "license": "ISC",
  "author": "Crosstalk Solutions, LLC",
  "scripts": {
    "start": "node bin/server.js",
    "build": "node ace build",
    "dev": "node ace serve --hmr",
    "test": "node ace test",
    "lint": "eslint .",
    "format": "prettier --write .",
    "typecheck": "tsc --noEmit",
    "work:downloads": "node ace queue:work --queue=downloads",
    "work:model-downloads": "node ace queue:work --queue=model-downloads",
    "work:benchmarks": "node ace queue:work --queue=benchmarks",
    "work:all": "node ace queue:work --all"
  },
  "imports": {
    "#controllers/*": "./app/controllers/*.js",
    "#exceptions/*": "./app/exceptions/*.js",
    "#models/*": "./app/models/*.js",
    "#mails/*": "./app/mails/*.js",
    "#services/*": "./app/services/*.js",
    "#listeners/*": "./app/listeners/*.js",
    "#events/*": "./app/events/*.js",
    "#middleware/*": "./app/middleware/*.js",
    "#validators/*": "./app/validators/*.js",
    "#providers/*": "./providers/*.js",
    "#policies/*": "./app/policies/*.js",
    "#abilities/*": "./app/abilities/*.js",
    "#database/*": "./database/*.js",
    "#tests/*": "./tests/*.js",
    "#start/*": "./start/*.js",
    "#config/*": "./config/*.js",
    "#jobs/*": "./app/jobs/*.js"
  },
  "devDependencies": {
    "@adonisjs/assembler": "^7.8.2",
    "@adonisjs/eslint-config": "^2.0.0",
    "@adonisjs/prettier-config": "^1.4.4",
    "@adonisjs/tsconfig": "^1.4.0",
    "@japa/assert": "^4.0.1",
    "@japa/plugin-adonisjs": "^4.0.0",
    "@japa/runner": "^4.2.0",
    "@swc/core": "1.11.24",
    "@tanstack/eslint-plugin-query": "^5.81.2",
    "@types/compression": "^1.8.1",
    "@types/dockerode": "^4.0.1",
    "@types/luxon": "^3.6.2",
    "@types/node": "^22.15.18",
    "@types/react": "^19.1.8",
    "@types/react-dom": "^19.1.6",
    "@types/stopword": "^2.0.3",
    "eslint": "^9.26.0",
    "hot-hook": "^0.4.0",
    "prettier": "^3.5.3",
    "ts-node-maintained": "^10.9.5",
    "typescript": "~5.8.3",
    "vite": "^6.4.1"
  },
  "dependencies": {
    "@adonisjs/auth": "^9.4.0",
    "@adonisjs/core": "^6.18.0",
    "@adonisjs/cors": "^2.2.1",
    "@adonisjs/inertia": "^3.1.1",
    "@adonisjs/lucid": "^21.8.2",
    "@adonisjs/session": "^7.5.1",
    "@adonisjs/shield": "^8.2.0",
    "@adonisjs/static": "^1.1.1",
    "@adonisjs/transmit": "^2.0.2",
    "@adonisjs/transmit-client": "^1.0.0",
    "@adonisjs/vite": "^4.0.0",
    "@chonkiejs/core": "^0.0.7",
    "@headlessui/react": "^2.2.4",
    "@inertiajs/react": "^2.0.13",
    "@markdoc/markdoc": "^0.5.2",
    "@openzim/libzim": "^4.0.0",
    "@protomaps/basemaps": "^5.7.0",
    "@qdrant/js-client-rest": "^1.16.2",
    "@tabler/icons-react": "^3.34.0",
    "@tailwindcss/vite": "^4.1.10",
    "@tanstack/react-query": "^5.81.5",
    "@tanstack/react-query-devtools": "^5.83.0",
    "@tanstack/react-virtual": "^3.13.12",
    "@uppy/core": "^5.2.0",
    "@uppy/dashboard": "^5.1.0",
    "@uppy/react": "^5.1.1",
    "@vinejs/vine": "^3.0.1",
    "@vitejs/plugin-react": "^4.6.0",
    "autoprefixer": "^10.4.21",
    "axios": "^1.13.5",
    "better-sqlite3": "^12.1.1",
    "bullmq": "^5.65.1",
    "cheerio": "^1.2.0",
    "compression": "^1.8.1",
    "dockerode": "^4.0.7",
    "edge.js": "^6.2.1",
    "fast-xml-parser": "^5.5.7",
    "fuse.js": "^7.1.0",
    "jszip": "^3.10.1",
    "luxon": "^3.6.1",
    "maplibre-gl": "^4.7.1",
    "mysql2": "^3.14.1",
    "ollama": "^0.6.3",
    "openai": "^6.27.0",
    "pdf-parse": "^2.4.5",
    "pdf2pic": "^3.2.0",
    "pino-pretty": "^13.0.0",
    "pmtiles": "^4.4.0",
    "postcss": "^8.5.6",
    "react": "^19.1.0",
    "react-adonis-transmit": "^1.0.1",
    "react-dom": "^19.1.0",
    "react-map-gl": "^8.1.0",
    "react-markdown": "^10.1.0",
    "reflect-metadata": "^0.2.2",
    "remark-gfm": "^4.0.1",
    "sharp": "^0.34.5",
    "stopword": "^3.1.5",
    "systeminformation": "^5.31.0",
    "tailwindcss": "^4.2.1",
    "tar": "^7.5.11",
    "tesseract.js": "^7.0.0",
    "url-join": "^5.0.0",
    "yaml": "^2.8.3"
  },
  "hotHook": {
    "boundaries": [
      "./app/controllers/**/*.ts",
      "./app/middleware/*.ts"
    ]
  },
  "prettier": "@adonisjs/prettier-config"
}

```

### File: .releaserc.json
```json
{
  "branches": [
    "main",
    { "name": "rc", "prerelease": "rc" }
  ],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    ["@semantic-release/npm", {
      "npmPublish": false
    }],
    ["@semantic-release/git", {
      "assets": ["package.json"],
      "message": "chore(release): ${nextRelease.version} [skip ci]"
    }],
    "@semantic-release/github"
  ]
}
```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
# Contributing to Project N.O.M.A.D.

Thank you for your interest in contributing to Project N.O.M.A.D.! Community contributions are what keep this project growing and improving. Please read this guide fully before getting started — it will save you (and the maintainers) a lot of time.

> **Note:** Acceptance of contributions is not guaranteed. All pull requests are evaluated based on quality, relevance, and alignment with the project's goals. The maintainers of Project N.O.M.A.D. ("Nomad") reserve the right accept, deny, or modify any pull request at their sole discretion.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Before You Start](#before-you-start)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Commit Messages](#commit-messages)
- [Release Notes](#release-notes)
- [Versioning](#versioning)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Feedback & Community](#feedback--community)

---

## Code of Conduct

Please read and review our full [Code of Conduct](https://github.com/Crosstalk-Solutions/project-nomad/blob/main/CODE_OF_CONDUCT.md) before contributing. In short: please be respectful and considerate in all interactions with maintainers and other contributors.

We are committed to providing a welcoming environment for everyone. Disrespectful or abusive behavior will not be tolerated. 

---

## Before You Start

**Open an issue first.** Before writing any code, please [open an issue](../../issues/new) to discuss your proposed change. This helps avoid duplicate work and ensures your contribution aligns with the project's direction.

When opening an issue:
- Use a clear, descriptive title
- Describe the problem you're solving or the feature you want to add
- If it's a bug, include steps to reproduce it and as much detail about your environment as possible
- Ensure you redact any personal or sensitive information in any logs, configs, etc.

---

## Getting Started with Contributing
**Please note**: this is the Getting Started guide for developing and contributing to Nomad, NOT [installing Nomad](https://github.com/Crosstalk-Solutions/project-nomad/blob/main/README.md) for regular use! 

### Prerequisites

- A Debian-based OS (Ubuntu recommended)
- `sudo`/root privileges
- Docker installed and running
- A stable internet connection (required for dependency downloads)
- Node.js (for frontend/admin work)

### Fork & Clone

1. Click **Fork** at the top right of this repository
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/project-nomad.git
   cd project-nomad
   ```
3. Add the upstream remote so you can stay in sync:
   ```bash
   git remote add upstream https://github.com/Crosstalk-Solutions/project-nomad.git
   ```

### Avoid Installing a Release Version Locally
Because Nomad relies heavily on Docker, we actually recommend against installing a release version of the project on the same local machine where you are developing. This can lead to conflicts with ports, volumes, and other resources. Instead, you can run your development version in a separate Docker environment while keeping your local machine clean. It certainly __can__ be done, but it adds complexity to your setup and workflow. If you choose to install a release version locally, please ensure you have a clear strategy for managing potential conflicts and resource usage.

---

## Development Workflow

1. **Sync with upstream** before starting any new work. We prefer rebasing over merge commits to keep a clean, linear git history as much as possible (this also makes it easier for maintainers to review and merge your changes). To sync with upstream:
   ```bash
   git fetch upstream
   git checkout dev
   git rebase upstream/dev
   ```

2. **Create a feature branch** off `dev` with a descriptive name:
   ```bash
   git checkout -b fix/issue-123
   # or
   git checkout -b feature/add-new-tool
   ```

3. **Make your changes.** Follow existing code style and conventions. Test your changes locally against a running N.O.M.A.D. instance before submitting.

4. **Add release notes** (see [Release Notes](#release-notes) below).

5. **Commit your changes** using [Conventional Commits](#commit-messages).

6. **Push your branch** and open a pull request.

---

## Commit Messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/). All commit messages must follow this format:

```
<type>(<scope>): <description>
```

**Common types:**

| Type | When to use |
|------|-------------|
| `feat` | A new user-facing feature |
| `fix` | A bug fix |
| `docs` | Documentation changes only |
| `refactor` | Code change that isn't a fix or feature and does not affect functionality |
| `chore` | Build process, dependency updates, tooling |
| `test` | Adding or updating tests |

**Scope** is optional but encouraged — use it to indicate the area of the codebase affected (e.g., `api`, `ui`, `maps`).

**Examples:**
```
feat(ui): add dark mode toggle to Command Center
fix(api): resolve container status not updating after restart
docs: update hardware requirements in README
chore(deps): bump docker-compose to v2.24
```

---

## Release Notes

Human-readable release notes live in [`admin/docs/release-notes.md`](admin/docs/release-notes.md) and are displayed directly in the Command Center UI.

If your PR is merged in, the maintainers will update the release notes with a summary of your contribution and credit you as the author. You do not need to add this yourself in the PR (please don't, as it may cause merge conflicts), but you can include a suggested note in the PR description if you like.

---

## Versioning

This project uses [Semantic Versioning](https://semver.org/). Versions are managed in the root `package.json` and updated automatically by `semantic-release`. The `project-nomad` Docker image uses this version. The `admin/package.json` version stays at `0.0.0` and should not be changed manually.

---

## Submitting a Pull Request

1. Push your branch to your fork:
   ```bash
   git push origin your-branch-name
   ```
2. Open a pull request against the `dev` branch of this repository
3. In the PR description:
   - Summarize what your changes do and why
   - Reference the related issue (e.g., `Closes #123`)
   - Note any relevant testing steps or environment details
4. Be responsive to feedback — maintainers may request changes. Pull requests with no activity for an extended period may be closed.

---

## Feedback & Community

Have questions or want to discuss ideas before opening an issue? Join the community:

- **Discord:** [Join the Crosstalk Solutions server](https://discord.com/invite/crosstalksolutions) — the best place to get help, share your builds, and talk with other N.O.M.A.D. users
- **Website:** [www.projectnomad.us](https://www.projectnomad.us)
- **Benchmark Leaderboard:** [benchmark.projectnomad.us](https://benchmark.projectnomad.us)

---

*Project N.O.M.A.D. is licensed under the [Apache License 2.0](LICENSE).*
```

### File: FAQ.md
```md
# Frequently Asked Questions (FAQ)

Find answers to some of the most common questions about Project N.O.M.A.D.

## Can I customize the port(s) that NOMAD uses?

Yes, you can customize the ports that NOMAD's core services (Command Center, MySQL, Redis) use. Please refer to the [Advanced Installation](README.md#advanced-installation) section of the README for more details on how to do this.

Note: As of 3/24/2026, only the core services defined in the `docker-compose.yml` file currently support port customization - the installable applications (e.g. Ollama, Kiwix, etc.) do not yet support this, but we have multiple PR's in the works to add this feature for all installable applications in a future release.

## Can I customize the storage location for NOMAD's data?

Yes, you can customize the storage location for NOMAD's content by modifying the `docker-compose.yml` file to adjust the appropriate bind mounts to point to your desired storage location on your host machine. Please refer to the [Advanced Installation](README.md#advanced-installation) section of the README for more details on how to do this.

## Can I store NOMAD's data on an external drive or network storage?

Short answer: yes, but we can't do it for you (and we recommend a local drive for best performance).

Long answer: Custom storage paths, mount points, and external drives (like iSCSI or SMB/NFS volumes) **are possible**, but this will be up to your individual configuration on the host before NOMAD starts, and then passed in via the compose.yml as this is a *host-level concern*, not a NOMAD-level concern (see above for details). NOMAD itself can't configure this for you, nor could we support all possible configurations in the install script.

## Can I run NOMAD on MAC, WSL2, or a non-Debian-based Distro?

See [Why does NOMAD require a Debian-based OS?](#why-does-nomad-require-a-debian-based-os)

## Why does NOMAD require a Debian-based OS?

Project N.O.M.A.D. is currently designed to run on Debian-based Linux distributions (with Ubuntu being the recommended distro) because our installation scripts and Docker configurations are optimized for this environment. While it's technically possible to run the Docker containers on other operating systems that support Docker, we have not tested or optimized the installation process for non-Debian-based systems, so we cannot guarantee a smooth experience on those platforms at this time.

Support for other operating systems will come in the future, but because our development resources are limited as a free and open-source project, we needed to prioritize our efforts and focus on a narrower set of supported platforms for the initial release. We chose Debian-based Linux as our starting point because it's widely used, easy to spin up, and provides a stable environment for running Docker containers.

Community members have provided guides for running N.O.M.A.D. on other platforms (e.g. WSL2, Mac, etc.) in our Discord community and [Github Discussions](https://github.com/Crosstalk-Solutions/project-nomad/discussions), so if you're interested in running N.O.M.A.D. on a non-Debian-based system, we recommend checking there for any available resources or guides. However, keep in mind that if you choose to run N.O.M.A.D. on a non-Debian-based system, you may encounter issues that we won't be able to provide support for, and you may need to have a higher level of technical expertise to troubleshoot and resolve any problems that arise.

## Can I run NOMAD on a Raspberry Pi or other ARM-based device?
Project N.O.M.A.D. is currently designed to run on x86-64 architecture, and we have not yet tested or optimized it for ARM-based devices like the Raspberry Pi (and have not published any official images for ARM architecture).

Support for ARM-based devices is on our roadmap, but our initial focus was on x86-64 hardware due to its widespread use and compatibility with a wide range of applications.

Community members have forked and published their own ARM-compatible images and installation guides for running N.O.M.A.D. on Raspberry Pi and other ARM-based devices in our Discord community and [Github Discussions](https://github.com/Crosstalk-Solutions/project-nomad/discussions), but these are not officially supported by the core development team, and we cannot guarantee their functionality or provide support for any issues that arise when using these community-created resources.

## What are the hardware requirements for running NOMAD?

Project N.O.M.A.D. itself is quite lightweight and can run on even modest x86-64 hardware, but the tools and resources you choose to install with N.O.M.A.D. will determine the specs required for your unique deployment. Please see the [Hardware Guide](https://www.projectnomad.us/hardware) for detailed build recommendations at various price points.

## Does NOMAD support languages other than English?

As of March 2026, Project N.O.M.A.D.'s UI is only available in English, and the majority of the tools and resources available through N.O.M.A.D. are also primarily in English. However, we have multi-language support on our roadmap for a future release, and we are actively working on adding support for additional languages both in the UI and in the available tools/resources. If you're interested in contributing to this effort, please check out our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to get involved.

## What technologies is NOMAD built with?

Project N.O.M.A.D. is built using a combination of technologies, including:
- **Docker:** for containerization of the Command Center and its dependencies
- **Node.js & TypeScript:** for the backend of the Command Center, particularly the [AdonisJS](https://adonisjs.com/) framework
- **React:** for the frontend of the Command Center, utilizing [Vite](https://vitejs.dev/) and [Inertia.js](https://inertiajs.com/) under the hood
- **MySQL:** for the Command Center's database
- **Redis:** for various caching, background jobs, "cron" tasks, and other internal processes within the Command Center

NOMAD makes use of the Docker-outside-of-Docker ("DooD") pattern, which allows the Command Center to manage and orchestrate other Docker containers on the host machine without needing to run Docker itself inside a container. This approach provides better performance and compatibility with a wider range of host environments while still allowing for powerful container management capabilities through the Command Center's UI.

## Can I run NOMAD if I have existing Docker containers on my machine?
Yes, you can safely run Project N.O.M.A.D. on a machine that already has existing Docker containers. NOMAD is designed to coexist with other Docker containers and will not interfere with them as long as there are no port conflicts or resource constraints.

All of NOMAD's containers are prefixed with `nomad_` in their names, so they can be easily identified and managed separately from any other containers you may have running. Just make sure to review the ports that NOMAD's core services (Command Center, MySQL, Redis) use during installation and adjust them if necessary to avoid conflicts with your existing containers.

## Why does NOMAD require access to the Docker socket?

See [What technologies is NOMAD built with?](#what-technologies-is-nomad-built-with)

## Can I use any AI models?
NOMAD by default uses Ollama inside of a docker container to run LLM Models for the AI Assistant. So if you find a model on HuggingFace for example, you won't be able to use that model in NOMAD. The list of available models in the AI Assistant settings (/settings/models) may not show all of the models you are looking for. If you found a model from https://ollama.com/search that you'd like to try and its not in the settings page, you can use a curl command to download the model.  
`curl -X POST -H "Content-Type: application/json" -d '{"model":"MODEL_NAME_HERE"}' http://localhost:8080/api/ollama/models` replacing MODEL_NAME_HERE with the model name from whats in the ollama website.

## Do I have to install the AI features in NOMAD?

No, the AI features in NOMAD (Ollama, Qdrant, custom RAG pipeline, etc.) are all optional and not required to use the core functionality of NOMAD.

## Is NOMAD actually free? Are there any hidden costs?
Yes, Project N.O.M.A.D. is completely free and open-source software licensed under the Apache License 2.0. There are no hidden costs or fees associated with using NOMAD itself, and we don't have any plans to introduce "premium" features or paid tiers.

Aside from the cost of the hardware you choose to run it on, there are no costs associated with using NOMAD.

## Do you sell hardware or pre-built devices with NOMAD pre-installed?

No, we do not sell hardware or pre-built devices with NOMAD pre-installed at this time. Project N.O.M.A.D. is a free and open-source software project, and we provide detailed installation instructions and hardware recommendations for users to set up their own NOMAD instances on compatible hardware of their choice. The tradeoff to this DIY approach is some additional setup time and technical know-how required on the user's end, but it also allows for greater flexibility and customization in terms of hardware selection and configuration to best suit each user's unique needs, budget, and preferences.

## How quickly are issues resolved when reported?

We strive to address and resolve issues as quickly as possible, but please keep in mind that Project N.O.M.A.D. is a free and open-source project maintained by a small team of volunteers. We prioritize issues based on their severity, impact on users, and the resources required to resolve them. Critical issues that affect a large number of users are typically addressed more quickly, while less severe issues may take longer to resolve. Aside from the development efforts needed to address the issue, we do our best to conduct thorough testing and validation to ensure that any fix we implement doesn't introduce new issues or regressions, which also adds to the time it takes to resolve an issue.

We also encourage community involvement in troubleshooting and resolving issues, so if you encounter a problem, please consider checking our Discord community and Github Discussions for potential solutions or workarounds while we work on an official fix.

## How often are new features added or updates released?

We aim to release updates and new features on a regular basis, but the exact timing can vary based on the complexity of the features being developed, the resources available to our volunteer development team, and the feedback and needs of our community. We typically release smaller "patch" versions more frequently to address bugs and make minor improvements, while larger feature releases may take more time to develop and test before they're ready for release.

## I opened a PR to contribute a new feature or fix a bug. How long does it usually take for PRs to be reviewed and merged?
We appreciate all contributions to the project and strive to review and merge pull requests (PRs) as quickly as possible. The time it takes for a PR to be reviewed and merged can vary based on several factors, including the complexity of the changes, the current workload of our maintainers, and the need for any additional testing or revisions.

Because NOMAD is still a young project, some PRs (particularly those for new features) may take longer to review and merge as we prioritize building out the core functionality and ensuring stability before adding new features. However, we do our best to provide timely feedback on all PRs and keep contributors informed about the status of their contributions.

## I have a question that isn't answered here. Where can I ask for help?

If you have a question that isn't answered in this FAQ, please feel free to ask for help in our Discord community (https://discord.com/invite/crosstalksolutions) or on our Github Discussions page (https://github.com/Crosstalk-Solutions/project-nomad/discussions).

## I have a suggestion for a new feature or improvement. How can I share it?

We welcome and encourage suggestions for new features and improvements! We highly encourage sharing your ideas (or upvoting existing suggestions) on our public roadmap at https://roadmap.projectnomad.us, where we track new feature requests. This is the best way to ensure that your suggestion is seen by the development team and the community, and it also allows other community members to upvote and show support for your idea, which can help prioritize it for future development.

```

### File: package-lock.json
```json
{
  "name": "project-nomad",
  "version": "1.27.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "project-nomad",
      "version": "1.27.0",
      "license": "ISC"
    }
  }
}

```

### File: .github\dependabot.yaml
```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/admin"
    schedule:
      interval: "weekly"
    target-branch: "rc"
```

### File: admin\ace.js
```js
/*
|--------------------------------------------------------------------------
| JavaScript entrypoint for running ace commands
|--------------------------------------------------------------------------
|
| DO NOT MODIFY THIS FILE AS IT WILL BE OVERRIDDEN DURING THE BUILD
| PROCESS.
|
| See docs.adonisjs.com/guides/typescript-build-process#creating-production-build
|
| Since, we cannot run TypeScript source code using "node" binary, we need
| a JavaScript entrypoint to run ace commands.
|
| This file registers the "ts-node/esm" hook with the Node.js module system
| and then imports the "bin/console.ts" file.
|
*/

/**
 * Register hook to process TypeScript files using ts-node-maintained
 */
import 'ts-node-maintained/register/esm'

/**
 * Import ace console entrypoint
 */
await import('./bin/console.js')

```

### File: admin\adonisrc.ts
```ts
import { defineConfig } from '@adonisjs/core/app'

export default defineConfig({
  /*
  |--------------------------------------------------------------------------
  | Experimental flags
  |--------------------------------------------------------------------------
  |
  | The following features will be enabled by default in the next major release
  | of AdonisJS. You can opt into them today to avoid any breaking changes
  | during upgrade.
  |
  */
  experimental: {
    mergeMultipartFieldsAndFiles: true,
    shutdownInReverseOrder: true,
  },

  /*
  |--------------------------------------------------------------------------
  | Commands
  |--------------------------------------------------------------------------
  |
  | List of ace commands to register from packages. The application commands
  | will be scanned automatically from the "./commands" directory.
  |
  */
  commands: [() => import('@adonisjs/core/commands'), () => import('@adonisjs/lucid/commands')],

  /*
  |--------------------------------------------------------------------------
  | Service providers
  |--------------------------------------------------------------------------
  |
  | List of service providers to import and register when booting the
  | application
  |
  */
  providers: [
    () => import('@adonisjs/core/providers/app_provider'),
    () => import('@adonisjs/core/providers/hash_provider'),
    {
      file: () => import('@adonisjs/core/providers/repl_provider'),
      environment: ['repl', 'test'],
    },
    () => import('@adonisjs/core/providers/vinejs_provider'),
    () => import('@adonisjs/core/providers/edge_provider'),
    () => import('@adonisjs/session/session_provider'),
    () => import('@adonisjs/vite/vite_provider'),
    () => import('@adonisjs/shield/shield_provider'),
    () => import('@adonisjs/static/static_provider'),
    () => import('@adonisjs/cors/cors_provider'),
    () => import('@adonisjs/lucid/database_provider'),
    () => import('@adonisjs/inertia/inertia_provider'),
    () => import('@adonisjs/transmit/transmit_provider'),
    () => import('#providers/map_static_provider'),
    () => import('#providers/kiwix_migration_provider'),
  ],

  /*
  |--------------------------------------------------------------------------
  | Preloads
  |--------------------------------------------------------------------------
  |
  | List of modules to import before starting the application.
  |
  */
  preloads: [() => import('#start/routes'), () => import('#start/kernel')],

  /*
  |--------------------------------------------------------------------------
  | Tests
  |--------------------------------------------------------------------------
  |
  | List of test suites to organize tests by their type. Feel free to remove
  | and add additional suites.
  |
  */
  tests: {
    suites: [
      {
        files: ['tests/unit/**/*.spec(.ts|.js)'],
        name: 'unit',
        timeout: 2000,
      },
      {
        files: ['tests/functional/**/*.spec(.ts|.js)'],
        name: 'functional',
        timeout: 30000,
      },
    ],
    forceExit: false,
  },

  /*
  |--------------------------------------------------------------------------
  | Metafiles
  |--------------------------------------------------------------------------
  |
  | A collection of files you want to copy to the build folder when creating
  | the production build.
  |
  */
  metaFiles: [
    {
      pattern: 'resources/views/**/*.edge',
      reloadServer: false,
    },
    {
      pattern: 'public/**',
      reloadServer: false,
    },
  ],

  assetsBundler: false,
  hooks: {
    onBuildStarting: [() => import('@adonisjs/vite/build_hook')],
  },
})

```

### File: admin\eslint.config.js
```js
import { configApp } from '@adonisjs/eslint-config'
import pluginQuery from '@tanstack/eslint-plugin-query'
export default configApp(...pluginQuery.configs['flat/recommended'])

```

### File: admin\tailwind.config.ts
```ts
/** @type {import('tailwindcss').Config} */

export default {
  content: ["./src/**/*.{js,jsx,ts,tsx}", "./index.html"],
  theme: {
    extend: {
      colors: {
        desert: "#EADAB9",
        "desert-green-light": "#BABAAA",
      },
    },
  },
};

```

### File: admin\tsconfig.json
```json
{
  "extends": "@adonisjs/tsconfig/tsconfig.app.json",
  "compilerOptions": {
    "rootDir": "./",
    "outDir": "./build"
  },
  "exclude": ["./inertia/**/*", "node_modules", "build"]
}

```

### File: admin\vite.config.ts
```ts
import { defineConfig } from 'vite'
import { getDirname } from '@adonisjs/core/helpers'
import inertia from '@adonisjs/inertia/client'
import react from '@vitejs/plugin-react'
import adonisjs from '@adonisjs/vite/client'
import tailwindcss from '@tailwindcss/vite'


export default defineConfig({
  plugins: [inertia({ ssr: { enabled: false } }), react(), tailwindcss(), adonisjs({ entrypoints: ['inertia/app/app.tsx'], reload: ['resources/views/**/*.edge'] })],

  /**
   * Define aliases for importing modules from
   * your frontend code
   */
  resolve: {
    alias: {
      '~/': `${getDirname(import.meta.url)}/inertia/`,
    },
  },
  server: {
    allowedHosts: true // This is for dev environments only. Can be overriden with `__VITE_ADDITIONAL_SERVER_ALLOWED_HOSTS` if needed.
  }
})

```

### File: collections\CATEGORIES-TODO.md
```md
# Kiwix Categories To-Do List

Potential categories to add to the tiered collections system in `kiwix-categories.json`.

## Current Categories (Completed)
- [x] Medicine - Medical references, first aid, emergency care
- [x] Survival & Preparedness - Food prep, prepper videos, repair guides
- [x] Education & Reference - Wikipedia, textbooks, TED talks

---

## High Priority

### Technology & Programming
Stack Overflow, developer documentation, coding tutorials
- Stack Overflow (multiple tags available)
- DevDocs documentation
- freeCodeCamp
- Programming language references

### Children & Family
Age-appropriate educational content for kids
- Wikipedia for Schools
- Wikibooks Children's Bookshelf
- Khan Academy Kids (via Kolibri - separate system)
- Storybooks, fairy tales

### Trades & Vocational
Practical skills for building, fixing, and maintaining
- Electrical wiring guides
- Plumbing basics
- Automotive repair
- Woodworking
- Welding fundamentals

### Agriculture & Gardening
Food production and farming (expand beyond what's in Survival)
- Practical Plants database
- Permaculture guides
- Seed saving
- Animal husbandry
- Composting and soil management

---

## Medium Priority

### Languages & Reference
Dictionaries, language learning, translation
- Wiktionary (multiple languages)
- Language learning resources
- Translation dictionaries
- Grammar guides

### History & Culture
Historical knowledge and cultural encyclopedias
- Wikipedia History portal content
- Historical documents
- Cultural archives
- Biographies

### Legal & Civic
Laws, rights, and civic procedures
- Legal references
- Constitutional documents
- Civic procedures
- Rights and responsibilities

### Communications
Emergency and amateur radio, networking
- Ham radio guides
- Emergency communication protocols
- Basic networking/IT
- Signal procedures

---

## Nice To Have

### Entertainment
Recreational reading and activities
- Project Gutenberg (fiction categories)
- Chess tutorials
- Puzzles and games
- Music theory

### Religion & Philosophy
Spiritual and philosophical texts
- Religious texts (various traditions)
- Philosophy references
- Ethics guides

### Regional/Non-English Bundles
Content in other languages
- Spanish language bundle
- French language bundle
- Other major languages

---

## Notes

- Each category should have 3 tiers: Essential, Standard, Comprehensive
- Higher tiers include all content from lower tiers via `includesTier`
- Check Kiwix catalog for available ZIM files: https://download.kiwix.org/zim/
- Consider storage constraints - Essential tiers should be <500MB ideally
- Mark one tier as `recommended: true` (usually Essential)

```

### File: collections\kiwix-categories.json
```json
{
  "spec_version": "2026-03-15",
  "categories": [
    {
      "name": "Medicine",
      "slug": "medicine",
      "icon": "IconStethoscope",
      "description": "Medical references, guides, and encyclopedias for healthcare information and emergency preparedness.",
      "language": "en",
      "tiers": [
        {
          "name": "Essential",
          "slug": "medicine-essential",
          "description": "Core medical references for first aid, medications, and emergency care. Start here.",
          "recommended": true,
          "resources": [
            {
              "id": "zimgit-medicine_en",
              "version": "2024-08",
              "title": "Medical Library",
              "description": "Field and emergency medicine books and guides",
              "url": "https://download.kiwix.org/zim/other/zimgit-medicine_en_2024-08.zim",
              "size_mb": 67
            },
            {
              "id": "nhs.uk_en_medicines",
              "version": "2025-12",
              "title": "NHS Medicines A to Z",
              "description": "How medicines work, dosages, side effects, and interactions",
              "url": "https://download.kiwix.org/zim/zimit/nhs.uk_en_medicines_2025-12.zim",
              "size_mb": 16
            },
            {
              "id": "fas-military-medicine_en",
              "version": "2025-06",
              "title": "Military Medicine",
              "description": "Tactical and field medicine manuals",
              "url": "https://download.kiwix.org/zim/zimit/fas-military-medicine_en_2025-06.zim",
              "size_mb": 78
            },
            {
              "id": "wwwnc.cdc.gov_en_all",
              "version": "2024-11",
              "title": "CDC Health Information",
              "description": "Disease prevention, travel health, and outbreak information",
              "url": "https://download.kiwix.org/zim/zimit/wwwnc.cdc.gov_en_all_2024-11.zim",
              "size_mb": 170
            }
          ]
        },
        {
          "name": "Standard",
          "slug": "medicine-standard",
          "description": "Comprehensive medical encyclopedia with detailed health information. Includes everything in Essential.",
          "includesTier": "medicine-essential",
          "resources": [
            {
              "id": "medlineplus.gov_en_all",
              "version": "2025-01",
              "title": "MedlinePlus",
              "description": "NIH's consumer health encyclopedia - diseases, conditions, drugs, supplements",
              "url": "https://download.kiwix.org/zim/zimit/medlineplus.gov_en_all_2025-01.zim",
              "size_mb": 1800
            }
          ]
        },
        {
          "name": "Comprehensive",
          "slug": "medicine-comprehensive",
          "description": "Professional-level medical references and textbooks. Includes everything in Standard.",
          "includesTier": "medicine-standard",
          "resources": [
            {
              "id": "wikipedia_en_medicine_maxi",
              "version": "2026-01",
              "title": "Wikipedia Medicine",
              "description": "Curated medical articles from Wikipedia with images",
              "url": "https://download.kiwix.org/zim/wikipedia/wikipedia_en_medicine_maxi_2026-01.zim",
              "size_mb": 2000
            },
            {
              "id": "libretexts.org_en_med",
              "version": "2025-01",
              "title": "LibreTexts Medicine",
              "description": "Open-source medical textbooks and educational content",
              "url": "https://download.kiwix.org/zim/libretexts/libretexts.org_en_med_2025-01.zim",
              "size_mb": 1100
            },
            {
              "id": "librepathology_en_all_maxi",
              "version": "2025-09",
              "title": "LibrePathology",
              "description": "Pathology reference for disease identification",
              "url": "https://download.kiwix.org/zim/other/librepathology_en_all_maxi_2025-09.zim",
              "size_mb": 76
            }
          ]
        }
      ]
    },
    {
      "name": "Survival & Preparedness",
      "slug": "survival",
      "icon": "IconShieldCheck",
      "description": "Emergency preparedness, bug-out planning, and tactical survival skills for crisis situations.",
      "language": "en",
      "tiers": [
        {
          "name": "Essential",
          "slug": "survival-essential",
          "description": "Core survival concepts and winter preparedness videos. Start here for emergency basics.",
          "recommended": true,
          "resources": [
            {
              "id": "canadian_prepper_winterprepping_en",
              "version": "2026-02",
              "title": "Canadian Prepper: Winter Prepping",
              "description": "Video guides for winter survival and cold weather emergencies",
              "url": "https://download.kiwix.org/zim/videos/canadian_prepper_winterprepping_en_2026-02.zim",
              "size_mb": 1340
            },
            {
              "id": "canadian_prepper_bugoutroll_en",
              "version": "2025-08",
              "title": "Canadian Prepper: Bug Out Roll",
              "description": "Essential gear selection for your bug-out bag",
              "url": "https://download.kiwix.org/zim/videos/canadian_prepper_bugoutroll_en_2025-08.zim",
              "size_mb": 975
            }
          ]
        },
        {
          "name": "Standard",
          "slug": "survival-standard",
          "description": "Bug-out strategies and urban survival techniques. Includes everything in Essential.",
          "includesTier": "survival-essential",
          "resources": [
            {
              "id": "canadian_prepper_bugoutconcepts_en",
              "version": "2026-02",
              "title": "Canadian Prepper: Bug Out Concepts",
              "description": "Strategies and planning for emergency evacuation",
              "url": "https://download.kiwix.org/zim/videos/canadian_prepper_bugoutconcepts_en_2026-02.zim",
              "size_mb": 2890
            },
            {
              "id": "urban-prepper_en_all",
              "version": "2026-02",
              "title": "Urban Prepper",
              "description": "Comprehensive urban emergency preparedness video series",
              "url": "https://download.kiwix.org/zim/videos/urban-prepper_en_all_2026-02.zim",
              "size_mb": 2240
            }
          ]
        },
        {
          "name": "Comprehensive",
          "slug": "survival-comprehensive",
          "description": "Complete prepper library with food storage strategies and classic military strategy. Includes everything in Standard.",
          "includesTier": "survival-standard",
          "resources": [
            {
              "id": "canadian_prepper_preppingfood_en",
              "version": "2025-09",
              "title": "Canadian Prepper: Prepping Food",
              "description": "Long-term food storage and survival meal preparation",
              "url": "https://download.kiwix.org/zim/videos/canadian_prepper_preppingfood_en_2025-09.zim",
              "size_mb": 2160
            },
            {
              "id": "gutenberg_en_lcc-u",
              "version": "2026-03",
              "title": "Project Gutenberg: Military Science",
              "description": "Classic military strategy, tactics, and field manuals",
              "url": "https://download.kiwix.org/zim/gutenberg/gutenberg_en_lcc-u_2026-03.zim",
              "size_mb": 1200
            }
          ]
        }
      ]
    },
    {
      "name": "Education & Reference",
      "slug": "education",
      "icon": "IconSchool",
      "description": "Encyclopedias, textbooks, tutorials, and educational videos for self-directed learning.",
      "language": "en",
      "tiers": [
        {
          "name": "Essential",
          "slug": "education-essential",
          "description": "Core reference materials - open textbooks and essential educational content. Lightweight, text-focused.",
          "recommended": true,
          "resources": [
            {
              "id": "wikibooks_en_all_nopic",
              "version": "2026-01",
              "title": "Wikibooks",
              "description": "Open-content textbooks covering math, science, computing, and more",
              "url": "https://download.kiwix.org/zim/wikibooks/wikibooks_en_all_nopic_2026-01.zim",
              "size_mb": 3100
            }
          ]
        },
        {
          "name": "Standard",
          "slug": "education-standard",
          "description": "Adds educational videos, university-level tutorials, and STEM textbooks. Includes Essential.",
          "includesTier": "education-essential",
          "resources": [
            {
              "id": "ted_mul_ted-ed",
              "version": "2026-01",
              "title": "TED-Ed",
              "description": "Educational video lessons on science, history, literature, and more",
              "url": "https://download.kiwix.org/zim/ted/ted_mul_ted-ed_2026-01.zim",
              "size_mb": 5610
            },
            {
              "id": "wikiversity_en_all_maxi",
              "version": "2026-02",
              "title": "Wikiversity",
              "description": "Tutorials, courses, and learning materials for all levels",
              "url": "https://download.kiwix.org/zim/wikiversity/wikiversity_en_all_maxi_2026-02.zim",
              "size_mb": 2370
            },
            {
              "id": "libretexts.org_en_math",
              "version": "2026-01",
              "title": "LibreTexts Mathematics",
              "description": "Open-source math textbooks from algebra to calculus",
              "url": "https://download.kiwix.org/zim/libretexts/libretexts.org_en_math_2026-01.zim",
              "size_mb": 792
            },
            {
              "id": "libretexts.org_en_phys",
              "version": "2026-01",
              "title": "LibreTexts Physics",
              "description": "Physics courses and textbooks",
              "url": "https://download.kiwix.org/zim/libretexts/libretexts.org_en_phys_2026-01.zim",
              "size_mb": 534
            },
            {
              "id": "libretexts.org_en_chem",
              "version": "2025-01",
              "title": "LibreTexts Chemistry",
              "description": "Chemistry courses and textbooks",
              "url": "https://download.kiwix.org/zim/libretexts/libretexts.org_en_chem_2025-01.zim",
              "size_mb": 2180
            },
            {
              "id": "libretexts.org_en_bio",
              "version": "2025-01",
              "title": "LibreTexts Biology",
              "description": "Biology courses and textbooks",
              "url": "https://download.kiwix.org/zim/libretexts/libretexts.org_en_bio_2025-01.zim",
              "size_mb": 2240
            }
          ]
        },
        {
          "name": "Comprehensive",
          "slug": "education-comprehensive",
          "description": "Complete educational library with enhanced textbooks and TED talks. Includes Standard.",
          "includesTier": "education-standard",
          "resources": [
            {
              "id": "wikibooks_en_all_maxi",
              "version": "2026-01",
              "title": "Wikibooks (With Images)",
              "description": "Open textbooks with full illustrations and diagrams",
              "url": "https://download.kiwix.org/zim/wikibooks/wikibooks_en_all_maxi_2026-01.zim",
              "size_mb": 5400
            },
            {
              "id": "ted_mul_ted-conference",
              "version": "2026-02",
              "title": "TED Conference",
              "description": "Main TED conference talks on ideas worth spreading",
              "url": "https://download.kiwix.org/zim/ted/ted_mul_ted-conference_2026-02.zim",
              "size_mb": 16500
            },
            {
              "id": "libretexts.org_en_human",
              "version": "2025-01",
              "title": "LibreTexts Humanities",
              "description": "Literature, philosophy, history, and social sciences",
              "url": "https://download.kiwix.org/zim/libretexts/libretexts.org_en_human_2025-01.zim",
              "size_mb": 3730
            },
            {
              "id": "libretexts.org_en_geo",
              "version": "2026-01",
              "title": "LibreTexts Geosciences",
              "description": "Earth science, geology, and environmental studies",
              "url": "https://download.kiwix.org/zim/libretexts/libretexts.org_en_geo_2026-01.zim",
              "size_mb": 1127
            },
            {
              "id": "libretexts.org_en_eng",
              "version": "2025-01",
              "title": "LibreTexts Engineering",
              "description": "Engineering courses and technical references",
              "url": "https://download.kiwix.org/zim/libretexts/libretexts.org_en_eng_2025-01.zim",
              "size_mb": 678
            },
            {
              "id": "libretexts.org_en_biz",
              "version": "2026-01",
              "title": "LibreTexts Business",
              "description": "Business, economics, and management textbooks",
              "url": "https://download.kiwix.org/zim/libretexts/libretexts.org_en_biz_2026-01.zim",
              "size_mb": 801
            }
          ]
        }
      ]
    },
    {
      "name": "DIY & Repair",
      "slug": "diy",
      "icon": "IconTool",
      "description": "Fix it yourself - repair guides, home improvement, woodworking, and vehicle maintenance.",
      "language": "en",
      "tiers": [
        {
          "name": "Essential",
          "slug": "diy-essential",
          "description": "Core repair knowledge - woodworking basics and vehicle maintenance Q&A.",
          "recommended": true,
          "resources": [
            {
              "id": "woodworking.stackexchange.com_en_all",
              "version": "2026-02",
              "title": "Woodworking Q&A",
              "description": "Stack Exchange Q&A for carpentry, joinery, and woodcraft",
              "url": "https://download.kiwix.org/zim/stack_exchange/woodworking.stackexchange.com_en_all_2026-02.zim",
              "size_mb": 99
            },
            {
              "id": "mechanics.stackexchange.com_en_all",
              "version": "2026-02",
              "title": "Motor Vehicle Maintenance Q&A",
              "description": "Stack Exchange Q&A for car and motorcycle repair",
              "url": "https://download.kiwix.org/zim/stack_exchange/mechanics.stackexchange.com_en_all_2026-02.zim",
              "size_mb": 321
            }
          ]
        },
        {
          "name": "Standard",
          "slug": "diy-standard",
          "description": "Home improvement expertise with thousands of Q&A threads. 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

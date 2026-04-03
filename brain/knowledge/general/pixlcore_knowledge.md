---
id: pixlcore-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:30:59.382717
---

# KNOWLEDGE EXTRACT: pixlcore
> **Extracted on:** 2026-03-30 17:51:02
> **Source:** pixlcore

---

## File: `xyops-healthcheck.md`
```markdown
# 📦 pixlcore/xyops-healthcheck [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xyops-healthcheck


## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2025-08-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A health check system for xyOps multi-master setups with Nginx.

## README (trích đầu)
```
# xyOps Health Check Daemon

> A lightweight health check daemon for xyOps deployments, designed for integration with Nginx and Docker.

The document covers the internal details of the xyOps multi-master health check system.

This daemon runs alongside your Nginx container, continuously monitoring a cluster of xyOps master servers. It determines which server is currently elected as the primary master, updates the Nginx configuration accordingly, and triggers a zero-downtime graceful reload.

If the master server goes down, the daemon automatically detects the change, waits for the cluster to elect a new master, and reconfigures Nginx to point to the new leader.

# Features

- Monitors a list of xyOps master servers for health and leadership.
- Automatically rewrites Nginx upstream config to point to the active master.
- Triggers `nginx -s reload` to apply changes without downtime.
- Runs as a simple background daemon inside your Nginx container.
- MIT Licensed, minimal dependencies.

# Installation

Add this to your Docker container that is also running Nginx:

```sh
npm install -g @pixlcore/xyops-healthcheck
```

# Usage

The daemon runs when invoked thusly:

```sh
/usr/bin/xyops-healthcheck
```

It forks into the background, reads its configuration, and begins monitoring.  You'll typically run this in the same container as your Nginx instance, typically via a shell script in the `RUN` directive:

```sh
#!/bin/sh

# Start healthcheck as a background daemon process (it does this itself)
/usr/bin/xyops-healthcheck

# Start nginx in the foreground
/usr/sbin/nginx -g 'daemon off;'
```

# Configuration

Configuration is stored in `config.json` (defaults shown):

```json
{
	"log_dir": "/var/log",
	"log_filename": "healthcheck.log",
	"log_columns": ["hires_epoch", "date", "hostname", "pid", "component", "category", "code", "msg", "data"],
	"log_crashes": true,
	"temp_dir": "/tmp",
	"pid_file": "/var/run/healthcheck.pid",
	"debug_level": 5,
	
	"masters": [],
	"port": 5522,
	
	"poll_freq_sec": 5,
	"poll_proto": "http:",
	
	"nginx_conf_file": "/etc/nginx/conf.d/backend.conf",
	"nginx_template": "upstream backend {\n\tserver [host]:[port];\n}\n",
	"nginx_reload_cmd": "/usr/sbin/nginx -s reload"
}
```

## Key settings

- `masters`: Array of xyOps conductor servers to monitor.
- `port`: Health check port (default 5522).
- `poll_freq_sec`: How often (in seconds) to poll servers.
- `poll_proto`: Protocol for health checks (http: or https:).
- `nginx_conf_file`: Path to the upstream config file Nginx uses.
- `nginx_template`: Template for generating the upstream block.
- `nginx_reload_cmd`: Command to gracefully reload Nginx.

# How It Works

1.	The daemon pings all configured masters at URI `/health`.
2.	When a server reports itself as the elected master, the daemon:
	- Rewrites the `nginx_conf_file` with that server as the upstream target.
	- Executes the `nginx_reload_cmd` to apply changes.
3.	If the current master fails, the daemon retries until a new leade
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `xyops-marketplace.md`
```markdown
# 📦 pixlcore/xyops-marketplace [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xyops-marketplace


## Meta
- **Stars:** ⭐ 7 | **Forks:** 🍴 3
- **Language:** N/A | **License:** BSD-3-Clause
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
An integrated plugin marketplace for the xyOps workflow automation and server monitoring platform.

## README (trích đầu)
```
# xyOps Plugin Marketplace

This repo is part of the [xyOps](https://github.com/pixlcore/xyops) workflow automation and server monitoring platform.

## Overview

xyOps has an integrated Plugin Marketplace, so you can expand the app's feature set by leveraging Plugins published both by PixlCore (the makers of xyOps), as well as the developer community.  To visit the marketplace, click the "**Marketplace**" link in the sidebar.

This document explains how to create and publish your own xyOps Plugins.  Marketplace Plugins are essentially cloud-hosted code libraries that self-download and self-execute, along with metadata to populate the marketplace listing, and define Plugin parameters for configuration.

The marketplace doesn't actually "host" Plugins -- it merely provides a search mechanism to discover them.  The Plugins themselves are hosted on package repositories like NPM, PyPI or GitHub, and the marketplace links to them.

> [!NOTE]
> For marketplace v1, your source code repository must be hosted on GitHub.  We will expand to support other hosts like GitLab and BitBucket in the future.

## Requirements

To publish your xyOps Plugin to the marketplace, it must:

- Be free to use
	- The Plugin may need to access a 3rd party paid service, which is fine.
	- By "free" we mean that the Plugin itself doesn't cost any money to install (our marketplace has no "buy" button).
- Be hosted publicly on GitHub.
	- We will expand to support other hosts in the future.
- Be able to execute using a self-contained download + launch combo command.
	- Examples of these include [npx](https://docs.npmjs.com/cli/commands/npx), [uvx](https://docs.astral.sh/uv/guides/tools/), [go run](https://pkg.go.dev/cmd/go#hdr-Compile_and_run_Go_program), and [docker run](https://docs.docker.com/reference/cli/docker/container/run/).
	- The command must download a specific tagged version or commit hash of the Plugin.
- Be fully open source using an [OSI-approved license](https://opensource.org/licenses).
	- All Plugin dependencies must also adhere to this requirement.
- Declare any user data or metrics collection.
	- If the Plugin collects user data for any reason, this must be declared in the [README](#readme).
	- An exception is when 3rd party services collect their own data, outside of the author's control.
- Be fully legal to use.
	- The Plugin must not violate any laws or terms of service, directly or indirectly.
- Be family friendly.
	- No adult content, bad language, etc.

PixlCore reserves the right to reject any Plugin submission it deems inappropriate for the marketplace.

## Launch Command

Your Plugin will need to be able to self-download and self-launch using a combo shell command.  These commands typically download software into a temporary cached directory, install all dependencies, and launch your Plugin all in one fell swoop.  Examples of these commands include:

- [npx](https://docs.npmjs.com/cli/commands/npx) - If your Plugin is written in Node.js, this is the perf
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `xyops-nginx-sso.md`
```markdown
# 📦 pixlcore/xyops-nginx-sso [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xyops-nginx-sso


## Meta
- **Stars:** ⭐ 1 | **Forks:** 🍴 0
- **Language:** Dockerfile | **License:** NOASSERTION
- **Last updated:** 2026-01-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
xyOps Multi-Master Nginx TLS/SSO

## README (trích đầu)
```
# xyOps Multi-Master Nginx TLS/SSO

This repo generates a custom Docker Image designed to be used with [xyOps](https://xyops.io).

This is a wrapper around the official [Nginx Docker Image](https://hub.docker.com/_/nginx), which layers in [Node.js](https://nodejs.org/) and a custom [Health Check Daemon](https://github.com/pixlcore/xyops-healthcheck) for [xyOps](https://xyops.io).  This is for use with xyOps multi-master setups, utilizing TLS, and [OAuth2-Proxy](https://github.com/oauth2-proxy/oauth2-proxy) for SSO integration.  For setup instructions, please see the [xyOps SSO Setup Guide](https://github.com/pixlcore/xyops/blob/main/docs/sso.md).

## Current Versions

- Nginx v1.28
- OAuth2-Proxy v7.12
- Node.js v22
- Health Check v1.0.5

# Usage

## Docker

This repo automatically publishes a Docker image on every tag, which is designed to run with [Nginx](https://nginx.org/) for xyOps mutli-master installs.  For usage instructions, see the [xyOps SSO Setup Guide](https://github.com/pixlcore/xyops/blob/main/docs/sso.md).  The Docker Image name is:

```
ghcr.io/pixlcore/xyops-nginx-sso
```

Example use:

```yaml
services:
  nginx:
    image: ghcr.io/pixlcore/xyops-nginx-sso:latest
    depends_on:
      - oauth2-proxy
    init: true
    environment:
      XYOPS_masters: xyops01.yourcompany.com,xyops02.yourcompany.com
      XYOPS_port: 5522
    volumes:
      - "./tls.crt:/etc/tls.crt:ro"
      - "./tls.key:/etc/tls.key:ro"
    ports:
      - "443:443"
    networks:
      xyops-net:

  oauth2-proxy:
    image: quay.io/oauth2-proxy/oauth2-proxy:latest
    ...
```

# License

**The MIT License (MIT)**

*Copyright (c) 2025 - 2026 PixlCore LLC.*

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `xyops-nginx.md`
```markdown
# 📦 pixlcore/xyops-nginx [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xyops-nginx


## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Dockerfile | **License:** NOASSERTION
- **Last updated:** 2025-12-07
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
xyOps Multi-Master Nginx with TLS

## README (trích đầu)
```
# xyOps Multi-Master Nginx with TLS

This repository generates a custom Docker Image designed to be used with [xyOps](https://xyops.io).

This is a wrapper around the official [Nginx Docker Image](https://hub.docker.com/_/nginx), which layers in [Node.js](https://nodejs.org/) and a custom [Health Check Daemon](https://github.com/pixlcore/xyops-healthcheck) for [xyOps](https://xyops.io).  This is for use with xyOps multi-master setups, utilizing TLS.  For setup instructions, please see the [xyOps Self-Hosting Guide](https://github.com/pixlcore/xyops/blob/main/docs/hosting.md).

## Current Versions

- Nginx v1.28
- Node.js v22
- Health Check v1.0.5

# Usage

## Docker

This repo automatically publishes a Docker image on every tag, which is designed to run with [Nginx](https://nginx.org/) for xyOps multi-master installs.  For complete usage instructions, see the [xyOps Self-Hosting Guide](https://github.com/pixlcore/xyops/blob/main/docs/hosting.md).  The official Docker image name is:

```
ghcr.io/pixlcore/xyops-nginx
```

Example use:

```yaml
services:
  nginx:
    image: ghcr.io/pixlcore/xyops-nginx:latest
    init: true
    environment:
      XYOPS_masters: xyops01.yourcompany.com,xyops02.yourcompany.com
      XYOPS_port: 5522
    volumes:
      - "./tls.crt:/etc/tls.crt:ro"
      - "./tls.key:/etc/tls.key:ro"
    ports:
      - "443:443"
    networks:
      xyops-net:
```

# License

**The MIT License (MIT)**

*Copyright (c) 2025 - 2026 PixlCore LLC.*

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `xyops-shell-image.md`
```markdown
# 📦 pixlcore/xyops-shell-image [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xyops-shell-image


## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** Dockerfile | **License:** NOASSERTION
- **Last updated:** 2026-03-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Base image for the xyOps Docker Event Plugin.

## README (trích đầu)
```
# xyOps Shell Image

This repository generates a Docker base image for the [xyOps](https://xyops.io) [Docker Plugin](https://xyops.io/docs/plugins/docker-plugin).  It uses the [xyRun](https://github.com/pixlcore/xyrun) utility to run custom xyOps job scripts inside the container, while handling things like monitoring system resources, and handling file upload/download.

You can use this image directly in your xyOps jobs, as it comes preinstalled with a variety of popular software, but more likely you will want to create your own Docker image based on this one, and pull in your own dependencies.  Instructions are below.

## Preinstalled

The image is based on `node:22-bookworm` (Debian 12) and contains the following preinstalled software:

- Node.js v22 + NPM + NPX
- Python v3 + UV + UVX
- Go v1.19
- Perl v5
- Docker CLI v29
- ffmpeg v5.1
- ImageMagick v6.9 +WebP +AVIF +HEIC +JPEG-XL
- [xyRun](https://github.com/pixlcore/xyrun)
- Also: zip, git, ssh, curl, wget, vim, less, sudo, jq, moreutils, net-tools, dnsutils, etc.

## Custom Image

To make your own custom image based on this one, set your Dockerfile `FROM` line to:

```
FROM ghcr.io/pixlcore/xyops-shell-image:latest
```

Or, you can use any base image you want.  Just make sure [xyRun](https://github.com/pixlcore/xyrun) is preinstalled and launched as your `CMD` or `ENTRYPOINT`.

In your Dockerfile, preinstall Node.js LTS if not already there (assuming Ubuntu / Debian base):

```
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash
RUN apt-get update && apt-get install -y nodejs
```

And preinstall xyRun like this:

```
RUN npm install -g @pixlcore/xyrun
```

Then set your `CMD` like this:

```
CMD ["xyrun"]
```

xyRun will then launch your custom script specified in your xyOps event, monitor all system resources during job runs, and handle uploading and downloading files for your jobs.

## License

MIT

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `xyops.md`
```markdown
# 📦 pixlcore/xyops [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xyops


## Meta
- **Stars:** ⭐ 3654 | **Forks:** 🍴 361
- **Language:** JavaScript | **License:** BSD-3-Clause
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A complete workflow automation and server monitoring system.

## README (trích đầu)
```
# xyOps™

![xyOps Screenshot](https://pixlcore.com/images/blog/xyops/workflow-edit.webp)

xyOps™ is a next-generation system for job scheduling, workflow automation, server monitoring, alerting, and incident response -- all combined into a single, cohesive platform. It's built for developers and operations teams who want to control their automation stack without surrendering data, freedom, or visibility. xyOps doesn't hide features behind paywalls or push telemetry back to anyone. It's open, extensible, and designed to run anywhere.

## The Idea Behind xyOps

Most automation platforms focus on workflow orchestration -- they run tasks, but they don't really help you see what's happening behind them. xyOps takes it further. It doesn't just schedule jobs; it connects them to real-time monitoring, alerts, server snapshots, and ticketing, creating a single, integrated feedback loop. When an alert fires, the email includes the running jobs on that server. One click opens a snapshot showing every process, CPU load, and network connection. If a job fails, xyOps can open a ticket with full context -- logs, history, and linked metrics. Everything in xyOps talks to everything else, so you can trace an issue from detection to resolution without ever leaving the system.

## Features at a Glance

- **Why xyOps?**
  - Schedule jobs across your fleet, track performance, set alerts, and view everything live, all in one place.
- **Job Scheduling Reimagined**
  - xyOps brings superpowers to job scheduling, way beyond cron.
- **Build Workflows Visually**
  - Use the graphical workflow editor to connect events, triggers, actions, and monitors into meaningful pipelines.
- **Monitor Everything**
  - Define exactly what you want to monitor, and get notified the moment things go wrong.
- **Smart Alerts**
  - Rich alerting with full customization and complex triggers.
- **Built for Fleets**
  - Whether you have five servers or five thousand, xyOps adapts to your needs.
- **Developer-Friendly**
  - Designed with you in mind. Yes, **you**!
- **Simple Setup**
  - From download to deployment in minutes.
- **Licensing**
  - xyOps is BSD-licensed for maximum flexibility.

# Installation

See our **[Self-Hosting Guide](https://docs.xyops.io/hosting)** for installation details.

Just want to test out xyOps locally really quick?  One-liner Docker command:

```sh
docker run --detach --init --restart unless-stopped -v xy-data:/opt/xyops/data -v /local/path/to/xyops-conf:/opt/xyops/conf -v /var/run/docker.sock:/var/run/docker.sock -e TZ="America/Los_Angeles" -e XYOPS_xysat_local="true" -p 5522:5522 -p 5523:5523 --name "xyops01" --hostname "xyops01" ghcr.io/pixlcore/xyops:latest
```

Please change `/local/path/to/xyops-conf` to a suitable location for the xyOps configuration to live on the host machine.

Then open http://localhost:5522 in your browser, and use username `admin` and password `admin`.

## Pricing

### Free Tier

For individuals looking to self-host xyOps:

- All app feat
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `xyplug-bluesky.md`
```markdown
# 📦 pixlcore/xyplug-bluesky [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xyplug-bluesky


## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-03-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A BlueSky Plugin for use in the xyOps workflow automation system.

## README (trích đầu)
```
<p align="center"><img src="logo.png" height="128" alt="Bluesky"/></p>
<h1 align="center">Bluesky Social Plugin</h1>

Bluesky event plugin for the [xyOps Workflow Automation System](https://xyops.io). This plugin is a pure Node.js implementation and talks directly to the Bluesky XRPC endpoints.

## Quick Start

Get your Bluesky app password at: https://bsky.app/settings/app-passwords

You will need the following environment variables (recommend storing them in a secret vault):

| Environment Variable | Description |
|----------------------|-------------|
| `BLUESKY_IDENTIFIER` | Your Bluesky identifier, e.g. `your-handle.bsky.social`. |
| `BLUESKY_APP_PASSWORD` | Your Bluesky App Password, which you can obtain [here](https://bsky.app/settings/app-passwords). |
| `BLUESKY_SERVICE_URL` | Optional service URL (defaults to `https://bsky.social`). |

## Requirements

- `npx`
- `git`

## What this plugin does

- Authenticates to Bluesky.
- Reads posts, profiles, followers, and timelines.
- Sends posts, images, and videos.
- Likes, reposts, follows, and mutes users.
- Returns the Bluesky API response as job output data.

### File Inputs

For `send_image`, `send_images`, and `send_video`, pass files into the xyOps job.

## Tools

All tools are selected via the Toolset parameter in `xyops.json`. When a tool is selected, its fields are flattened into `params` at the top level.

Notes on common fields:
- `cursor` is an opaque pagination token returned by Bluesky. Treat it as a string and pass it back verbatim to fetch the next page. Leave it empty for the first page.
- `limit` is the maximum number of items to return. Where applicable, Bluesky accepts `1-100`. If you leave it empty or `0`, the server default is used (often 50).

### Check Auth Status

Check if the current session is authenticated.  No parameters are used.

### Get Profile

Get a user profile. If you omit the handle, the authenticated user is used.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `handle` | text | No | Handle or DID to fetch (e.g. `user.bsky.social` or `did:plc:...`). | Current user |

### Get Follows

Get users followed by an account.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `handle` | text | No | Handle or DID to fetch follows for. | Current user |
| `limit` | number | No | Max results to return (1-100). | 50 |
| `cursor` | text | No | Pagination cursor returned from a previous call. | - |

### Get Followers

Get users who follow an account.

| Parameter | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `handle` | text | No | Handle or DID to fetch followers for. | Current user |
| `limit` | number | No | Max results to return (1-100). | 50 |
| `cursor` | text | No | Pagination cursor returned from a previous call. | - |

### Like Post

Like a post. Requires the target post URI and CI
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `xyplug-stagehand.md`
```markdown
# 📦 pixlcore/xyplug-stagehand [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xyplug-stagehand


## Meta
- **Stars:** ⭐ 0 | **Forks:** 🍴 0
- **Language:** JavaScript | **License:** NOASSERTION
- **Last updated:** 2026-01-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Stagehand Plugin for use in the xyOps workflow automation system.

## README (trích đầu)
```
<p align="center"><img src="https://raw.githubusercontent.com/pixlcore/xyplug-stagehand/refs/heads/main/logo.png" height="108" alt="Stagehand"/></p>
<h1 align="center">Stagehand Automation Plugin</h1>

A Stagehand event plugin for the [xyOps Workflow Automation System](https://xyops.io). This package provides an AI-powered browser automation framework for xyOps.  Using it you can drive a headless browser with simple English instructions, take actions, extract data, capture network requests, and even record a video of the whole session.

A headless Chromium is launched and automated locally in a Docker container.  This Plugin does not use any "cloud" browser environments.  Note that if you use any of the AI features, then you need to be careful with sensitive information, as they may be sent to the AI provider.  See below for discussion and mitigation techniques.

This Plugin relies heavily on the [Stagehand](https://github.com/browserbase/stagehand) and [Playwright](https://github.com/microsoft/playwright) libraries. See those repos for full documentation and low-level usage.

## Requirements

- **Docker**
	- This Plugin ships as a prebuilt Docker container, so your xyOps servers will need Docker installed for this to work.
- **AI Credentials**
	- If you intend to use any of the AI features, you will need an API Key for your chosen provider.

## Environment Variables

If you are going to use the AI features in Stagehand, create a [Secret Vault](https://xyops.io/docs/secrets) in xyOps and assign this Plugin to it.  Add your AI provider's API Key in a new variable named:

```
AI_API_KEY
```

Stagehand supports Google, OpenAI, Anthropic, xAI, DeepSeek, Perplexity, Azure, Ollama, or any other LLM model from the [Vercel AI SDK](https://sdk.vercel.ai/providers).

## Usage

### Script

The Plugin "Script" parameter is expected to be a list of instructions for the browser to perform, one per line.  It can be plain text or [JSON](#advanced).  This section will focus on the plain text format, which looks like this:

```
Navigate to https://mycompany.com/
Type "foo" into the Username text field.
Type "bar" into the Password text field.
Click the "Login" button.
Sleep for 3000
```

Each line should contain a simple instruction (i.e. one action).  For each line, the Plugin defaults to calling Stagehand [act()](https://docs.stagehand.dev/v3/basics/act) unless prefixed by a specific keyword.  See below for specific keywords.

### Perform Actions

The default behavior is to [act()](https://docs.stagehand.dev/v3/basics/act) (take action) on the instruction.  This expects commands such as:

| Action | Example instruction |
|--------|---------------------|
| Click | `click the button` |
| Fill | `fill the field with <value>` |
| Type | `type <text> into the search box` |
| Press | `press <key> in the search field` |
| Scroll | `scroll to <position>` |
| Select | `select <value> from the dropdown` |

### Browser Navigation

You can navigate to URLs at any time, by s
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `xyrun.md`
```markdown
# 📦 pixlcore/xyrun [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xyrun


## Meta
- **Stars:** ⭐ 6 | **Forks:** 🍴 0
- **Language:** JavaScript | **License:** BSD-3-Clause
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Remote job runner script for xyOps.

## README (trích đầu)
```
# Overview

**xyOps Remote Job Runner (xyRun)** is a companion to the [xyOps](https://xyops.io) workflow automation and server monitoring platform.  It is a wrapper for running remote jobs inside Docker containers, or over a remote SSH connection.

The idea is that when a job is running "remotely" (i.e. not a direct child process of [xySat](https://github.com/pixlcore/xysat)) then we cannot monitor system resources for the job.  Also, input and output files simply do not work in these cases (because xySat expects them to be on the local filesystem where it is running).  xyRun handles all these complexities for you by sitting "in between" your job and xySat.  xyRun should run *inside* the container or on the far end of the SSH connection, where your job process is running.

To use xyRun in a xyOps Event Plugin, make sure you set the Plugin's `runner` property to `true`.  This hint tells xyOps (and ultimately xySat) that the job is running remotely out if its reach, and it should not perform the usual process and network monitoring, and file management.  Those duties get delegated to xyRun.

## Features

- Handles monitoring processes, network connections, CPU and memory usage of remote jobs, and passing those metrics back to xyOps.
- Handles input files by creating a temporary directory for you job and pre-downloading all files from the xyOps master server.
- Handles output files by intercepting the `files` message and uploading them directly to the xyOps master server.

# Installation

xyRun requires both Node.js LTS and NPM.

## Docker

In your Dockerfile, preinstall Node.js LTS if needed (assuming Ubuntu / Debian base):

```
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash
RUN apt-get update && apt-get install -y nodejs
```

And preinstall xyRun like this:

```
RUN npm install -g @pixlcore/xyrun
```

Then wrap your `CMD` with a `xyrun` prefix like this:

```
CMD xyrun node /path/to/your-script.js
```

xyRun will directly launch whatever is passed to it on the CLI, including arguments.

## Other

For other uses (i.e. SSH) install the NPM module globally on the target machine where the remote job will be running:

```sh
npm install -g @pixlcore/xyrun
```

Then wrap your remote command with a `xyrun` prefix:

```sh
ssh user@target xyrun node /path/to/your-script.js
```

# Script Mode

When no sub-command is specified on the CLI, xyRun will look inside the job JSON data (passed in via STDIN) for a parameter named `script`.  If this is found, it is quickly written out to a temp file, made executable (775), and that is what it launches.  It is assumed that the provided `script` will contain a proper [Shebang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29) line.

This allows xyRun to act as a "Remote Shell Plugin" for certain xyOps jobs that require it.

# Development

You can install the source code by using [Git](https://en.wikipedia.org/wiki/Git) ([Node.js](https://nodejs.org/) is also required):

```sh
git clone https://github.com/pi
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `xysat.md`
```markdown
# 📦 pixlcore/xysat [🔖 PENDING/APPROVE]
🔗 https://github.com/pixlcore/xysat


## Meta
- **Stars:** ⭐ 11 | **Forks:** 🍴 2
- **Language:** JavaScript | **License:** BSD-3-Clause
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
xyOps Satellite (xySat)

## README (trích đầu)
```
# Overview

**xyOps Satellite (xySat)** is a companion to the [xyOps](https://xyops.io) workflow automation and server monitoring platform.  It is both a job runner, and a data collector for server monitoring and alerting.  xySat is designed to be installed on *all* of your servers, so it is lean and mean, and has zero dependencies.

# Installation

See the [xySat Installation Guide](https://docs.xyops.io/hosting/satellite) for details.

## Manual Installation

If you would like to install xySat manually (for e.g. to run it as a non-root user), see below for the steps.

### Linux

<details><summary>Manual Linux Installation</summary>

First, click the "Add Server" button in the sidebar in the xyOps UI.  Select "Linux" as the target platform, and copy the one-line installer command.  It will look something like this:

```sh
curl -s "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/install?t=AUTH_TOKEN" | sudo sh
```

We're not going to run this command as is, but we need the URL.  So copy the full URL, and create two new URLs by swapping out the word "install" like this:

- **Download Tarball:** `http://YOUR_XYOPS_SERVER:5522/api/app/satellite/core?t=AUTH_TOKEN&os=linux&arch=YOUR_ARCH`
- **Download Config:** `http://YOUR_XYOPS_SERVER:5522/api/app/satellite/config?t=AUTH_TOKEN`

Make sure you copy over the auth token *exactly* as it is shown.  In the tarball URL replace `YOUR_ARCH` with either `x64` or `arm64`, depending on your server's architecture.

Now, SSH to the Linux server you want to install xySat on.  Note that it needs to be installed in `/opt/xyops/satellite/` for everything to work correctly.  So you may need to become root to create this directory, but you can then `chown` it to another user before installing.  It is possible to run xySat in a different directory, but it is not recommended.

Here are the commands to get it installed and configured:

```sh
# create base directory and cd into it
mkdir -p /opt/xyops/satellite
cd /opt/xyops/satellite

# download tarball and extract
curl -fsSL "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/core?t=AUTH_TOKEN&os=linux&arch=YOUR_ARCH" | tar zxf -

# Fetch custom config file for satellite
curl -fsSL "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/config?t=AUTH_TOKEN" > config.json
chmod 600 config.json

# Set some permissions
chmod 775 *.sh bin/*

# Start it up (forks a background daemon)
./control.sh start
```

Notably, this installation method will not register xySat as a systemd service, so it is up to you to configure it to auto-start on boot if you want.

</details>

### macOS

<details><summary>Manual macOS Installation</summary>

First, click the "Add Server" button in the sidebar in the xyOps UI.  Select "macOS" as the target platform, and copy the one-line installer command.  It will look something like this:

```sh
curl -s "http://YOUR_XYOPS_SERVER:5522/api/app/satellite/install?t=AUTH_TOKEN&os=macos" | sudo sh
```

We're not going to run this command as is, but we need the URL.  S
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


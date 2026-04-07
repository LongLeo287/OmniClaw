---
id: n8n-mcp
type: knowledge
owner: OA_Triage
---
# n8n-mcp
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "n8n-mcp",
  "version": "2.47.1",
  "description": "Integration between n8n workflow automation and Model Context Protocol (MCP)",
  "main": "dist/index.js",
  "types": "dist/index.d.ts",
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "require": "./dist/index.js",
      "import": "./dist/index.js"
    }
  },
  "bin": {
    "n8n-mcp": "./dist/mcp/stdio-wrapper.js"
  },
  "scripts": {
    "build": "tsc -p tsconfig.build.json",
    "build:ui": "cd ui-apps && npm install && npm run build",
    "build:all": "npm run build:ui && npm run build",
    "rebuild": "node dist/scripts/rebuild.js",
    "rebuild:optimized": "node dist/scripts/rebuild-optimized.js",
    "validate": "node dist/scripts/validate.js",
    "test-nodes": "node dist/scripts/test-nodes.js",
    "start": "node dist/mcp/index.js",
    "start:http": "MCP_MODE=http node dist/mcp/index.js",
    "start:http:fixed:deprecated": "echo 'DEPRECATED: USE_FIXED_HTTP is deprecated. Use npm run start:http instead.' && MCP_MODE=http USE_FIXED_HTTP=true node dist/mcp/index.js",
    "start:n8n": "N8N_MODE=true MCP_MODE=http node dist/mcp/index.js",
    "http": "npm run build && npm run start:http",
    "dev": "npm run build && npm run rebuild && npm run validate",
    "dev:http": "MCP_MODE=http nodemon --watch src --ext ts --exec 'npm run build && npm run start:http'",
    "test:single-session": "./scripts/test-single-session.sh",
    "test:mcp-endpoint": "node scripts/test-mcp-endpoint.js",
    "test:mcp-endpoint:curl": "./scripts/test-mcp-endpoint.sh",
    "test:mcp-stdio": "npm run build && node scripts/test-mcp-stdio.js",
    "test": "vitest",
    "test:ui": "vitest --ui",
    "test:run": "vitest run",
    "test:coverage": "vitest run --coverage",
    "test:ci": "vitest run --coverage --coverage.thresholds.lines=0 --coverage.thresholds.functions=0 --coverage.thresholds.branches=0 --coverage.thresholds.statements=0 --reporter=default --reporter=junit",
    "test:watch": "vitest watch",
    "test:unit": "vitest run tests/unit",
    "test:integration": "vitest run --config vitest.config.integration.ts",
    "test:integration:n8n": "vitest run tests/integration/n8n-api",
    "test:cleanup:orphans": "tsx tests/integration/n8n-api/scripts/cleanup-orphans.ts",
    "test:e2e": "vitest run tests/e2e",
    "lint": "tsc --noEmit",
    "typecheck": "tsc --noEmit",
    "update:n8n": "node scripts/update-n8n-deps.js",
    "update:n8n:check": "node scripts/update-n8n-deps.js --dry-run",
    "fetch:templates": "node dist/scripts/fetch-templates.js",
    "fetch:templates:update": "node dist/scripts/fetch-templates.js --update",
    "fetch:templates:extract": "node dist/scripts/fetch-templates.js --extract-only",
    "fetch:templates:robust": "node dist/scripts/fetch-templates-robust.js",
    "fetch:community": "node dist/scripts/fetch-community-nodes.js",
    "fetch:community:verified": "node dist/scripts/fetch-community-nodes.js --verified-only",
    "fetch:community:update": "node dist/scripts/fetch-community-nodes.js --update",
    "generate:docs": "node dist/scripts/generate-community-docs.js",
    "generate:docs:readme-only": "node dist/scripts/generate-community-docs.js --readme-only",
    "generate:docs:summary-only": "node dist/scripts/generate-community-docs.js --summary-only",
    "generate:docs:incremental": "node dist/scripts/generate-community-docs.js --incremental",
    "generate:docs:stats": "node dist/scripts/generate-community-docs.js --stats",
    "migrate:readme-columns": "node dist/scripts/migrate-readme-columns.js",
    "prebuild:fts5": "npx tsx scripts/prebuild-fts5.ts",
    "test:templates": "node dist/scripts/test-templates.js",
    "test:protocol-negotiation": "npx tsx src/scripts/test-protocol-negotiation.ts",
    "test:workflow-validation": "node dist/scripts/test-workflow-validation.js",
    "test:template-validation": "node dist/scripts/test-template-validation.js",
    "test:essentials": "node dist/scripts/test-essentials.js",
    "test:enhanced-validation": "node dist/scripts/test-enhanced-validation.js",
    "test:ai-workflow-validation": "node dist/scripts/test-ai-workflow-validation.js",
    "test:mcp-tools": "node dist/scripts/test-mcp-tools.js",
    "test:n8n-manager": "node dist/scripts/test-n8n-manager-integration.js",
    "test:n8n-validate-workflow": "node dist/scripts/test-n8n-validate-workflow.js",
    "test:typeversion-validation": "node dist/scripts/test-typeversion-validation.js",
    "test:error-handling": "node dist/scripts/test-error-handling-validation.js",
    "test:workflow-diff": "node dist/scripts/test-workflow-diff.js",
    "test:transactional-diff": "node dist/scripts/test-transactional-diff.js",
    "test:tools-documentation": "node dist/scripts/test-tools-documentation.js",
    "test:structure-validation": "npx tsx scripts/test-structure-validation.ts",
    "test:url-configuration": "npm run build && ts-node scripts/test-url-configuration.ts",
    "test:search-improvements": "node dist/scripts/test-search-improvements.js",
    "test:fts5-search": "node dist/scripts/test-fts5-search.js",
    "migrate:fts5": "node dist/scripts/migrate-nodes-fts.js",
    "test:mcp:update-partial": "node dist/scripts/test-mcp-n8n-update-partial.js",
    "test:update-partial:debug": "node dist/scripts/test-update-partial-debug.js",
    "test:issue-45-fix": "node dist/scripts/test-issue-45-fix.js",
    "test:auth-logging": "tsx scripts/test-auth-logging.ts",
    "test:docker": "./scripts/test-docker-config.sh all",
    "test:docker:unit": "./scripts/test-docker-config.sh unit",
    "test:docker:integration": "./scripts/test-docker-config.sh integration",
    "test:docker:security": "./scripts/test-docker-config.sh security",
    "mine:patterns": "tsx src/scripts/mine-workflow-patterns.ts",
    "sanitize:templates": "node dist/scripts/sanitize-templates.js",
    "db:rebuild": "node dist/scripts/rebuild-database.js",
    "db:init": "node -e \"new (require('./dist/services/sqlite-storage-service').SQLiteStorageService)(); console.log('Database initialized')\"",
    "docs:rebuild": "ts-node src/scripts/rebuild-database.ts",
    "sync:runtime-version": "node scripts/sync-runtime-version.js",
    "update:readme-version": "node scripts/update-readme-version.js",
    "prepare:publish": "./scripts/publish-npm.sh",
    "update:all": "./scripts/update-and-publish-prep.sh",
    "test:release-automation": "node scripts/test-release-automation.js",
    "prepare:release": "node scripts/prepare-release.js"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/czlonkowski/n8n-mcp.git"
  },
  "keywords": [
    "n8n",
    "mcp",
    "model-context-protocol",
    "ai",
    "workflow",
    "automation"
  ],
  "author": "Romuald Czlonkowski @ www.aiadvisors.pl/en",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/czlonkowski/n8n-mcp/issues"
  },
  "homepage": "https://github.com/czlonkowski/n8n-mcp#readme",
  "files": [
    "dist/**/*",
    "ui-apps/dist/**/*",
    "data/nodes.db",
    "data/workflow-patterns.json",
    ".env.example",
    "README.md",
    "LICENSE",
    "package.runtime.json"
  ],
  "devDependencies": {
    "@faker-js/faker": "^9.9.0",
    "@testing-library/jest-dom": "^6.6.4",
    "@types/better-sqlite3": "^7.6.13",
    "@types/express": "^5.0.3",
    "@types/node": "^22.15.30",
    "@types/ws": "^8.18.1",
    "@vitest/coverage-v8": "^3.2.4",
    "@vitest/runner": "^3.2.4",
    "@vitest/ui": "^3.2.4",
    "axios": "^1.14.0",
    "axios-mock-adapter": "^2.1.0",
    "fishery": "^2.3.1",
    "msw": "^2.10.4",
    "nodemon": "^3.1.14",
    "ts-node": "^10.9.2",
    "typescript": "^5.8.3",
    "vitest": "^3.2.4"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "1.28.0",
    "@n8n/n8n-nodes-langchain": "^2.14.1",
    "@supabase/supabase-js": "^2.57.4",
    "dotenv": "^16.5.0",
    "express": "^5.1.0",
    "express-rate-limit": "^7.1.5",
    "form-data": "^4.0.5",
    "lru-cache": "^11.2.1",
    "n8n": "^2.14.2",
    "n8n-core": "^2.14.1",
    "n8n-workflow": "^2.14.1",
    "openai": "^4.77.0",
    "sql.js": "^1.13.0",
    "tslib": "^2.6.2",
    "uuid": "^10.0.0",
    "zod": "3.24.1"
  },
  "optionalDependencies": {
    "@rollup/rollup-darwin-arm64": "^4.50.0",
    "@rollup/rollup-linux-x64-gnu": "^4.50.0",
    "better-sqlite3": "^11.10.0"
  },
  "overrides": {
    "pyodide": "0.26.4",
    "isolated-vm": "npm:empty-npm-package@1.0.0"
  }
}

```

### File: README.md
```md
# n8n-MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/czlonkowski/n8n-mcp?style=social)](https://github.com/czlonkowski/n8n-mcp)
[![npm version](https://img.shields.io/npm/v/n8n-mcp.svg)](https://www.npmjs.com/package/n8n-mcp)
[![codecov](https://codecov.io/gh/czlonkowski/n8n-mcp/graph/badge.svg?token=YOUR_TOKEN)](https://codecov.io/gh/czlonkowski/n8n-mcp)
[![Tests](https://img.shields.io/badge/tests-3336%20passing-brightgreen.svg)](https://github.com/czlonkowski/n8n-mcp/actions)
[![n8n version](https://img.shields.io/badge/n8n-2.14.2-orange.svg)](https://github.com/n8n-io/n8n)
[![Docker](https://img.shields.io/badge/docker-ghcr.io%2Fczlonkowski%2Fn8n--mcp-green.svg)](https://github.com/czlonkowski/n8n-mcp/pkgs/container/n8n-mcp)
[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/n8n-mcp?referralCode=n8n-mcp)

A Model Context Protocol (MCP) server that provides AI assistants with comprehensive access to n8n node documentation, properties, and operations. Deploy in minutes to give Claude and other AI assistants deep knowledge about n8n's 1,396 workflow automation nodes (812 core + 584 community).

## Overview

n8n-MCP serves as a bridge between n8n's workflow automation platform and AI models, enabling them to understand and work with n8n nodes effectively. It provides structured access to:

- 📚 **1,396 n8n nodes** - 812 core nodes + 584 community nodes (516 verified)
- 🔧 **Node properties** - 99% coverage with detailed schemas
- ⚡ **Node operations** - 63.6% coverage of available actions
- 📄 **Documentation** - 87% coverage from official n8n docs (including AI nodes)
- 🤖 **AI tools** - 265 AI-capable tool variants detected with full documentation
- 💡 **Real-world examples** - 2,646 pre-extracted configurations from popular templates
- 🎯 **Template library** - 2,709 workflow templates with 100% metadata coverage
- 🌐 **Community nodes** - Search verified community integrations with `source` filter (NEW!)


## ⚠️ Important Safety Warning

**NEVER edit your production workflows directly with AI!** Always:
- 🔄 **Make a copy** of your workflow before using AI tools
- 🧪 **Test in development** environment first
- 💾 **Export backups** of important workflows
- ⚡ **Validate changes** before deploying to production

AI results can be unpredictable. Protect your work!

## 🚀 Quick Start

### Option 1: Hosted Service (Easiest - No Setup!) ☁️

**The fastest way to try n8n-MCP** - no installation, no configuration:

👉 **[dashboard.n8n-mcp.com](https://dashboard.n8n-mcp.com)**

- ✅ **Free tier**: 100 tool calls/day
- ✅ **Instant access**: Start building workflows immediately
- ✅ **Always up-to-date**: Latest n8n nodes and templates
- ✅ **No infrastructure**: We handle everything

Just sign up, get your API key, and connect your MCP client. 

---

## 🏠 Self-Hosting Options

Prefer to run n8n-MCP yourself? Choose your deployment method:

### Option A: npx (Quick Local Setup) 🚀

Get n8n-MCP running in minutes:

[![n8n-mcp Video Quickstart Guide](./thumbnail.png)](https://youtu.be/5CccjiLLyaY?si=Z62SBGlw9G34IQnQ&t=343)

**Prerequisites:** [Node.js](https://nodejs.org/) installed on your system

```bash
# Run directly with npx (no installation needed!)
npx n8n-mcp
```

Add to Claude Desktop config:

> ⚠️ **Important**: The `MCP_MODE: "stdio"` environment variable is **required** for Claude Desktop. Without it, you will see JSON parsing errors like `"Unexpected token..."` in the UI. This variable ensures that only JSON-RPC messages are sent to stdout, preventing debug logs from interfering with the protocol.

**Basic configuration (documentation tools only):**
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "npx",
      "args": ["n8n-mcp"],
      "env": {
        "MCP_MODE": "stdio",
        "LOG_LEVEL": "error",
        "DISABLE_CONSOLE_OUTPUT": "true"
      }
    }
  }
}
```

**Full configuration (with n8n management tools):**
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "npx",
      "args": ["n8n-mcp"],
      "env": {
        "MCP_MODE": "stdio",
        "LOG_LEVEL": "error",
        "DISABLE_CONSOLE_OUTPUT": "true",
        "N8N_API_URL": "https://your-n8n-instance.com",
        "N8N_API_KEY": "your-api-key"
      }
    }
  }
}
```

> **Note**: npx will download and run the latest version automatically. The package includes a pre-built database with all n8n node information.

**Configuration file locations:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Restart Claude Desktop after updating configuration** - That's it! 🎉

### Option B: Docker (Isolated & Reproducible) 🐳

**Prerequisites:** Docker installed on your system

<details>
<summary><strong>📦 Install Docker</strong> (click to expand)</summary>

**macOS:**
```bash
# Using Homebrew
brew install --cask docker

# Or download from https://www.docker.com/products/docker-desktop/
```

**Linux (Ubuntu/Debian):**
```bash
# Update package index
sudo apt-get update

# Install Docker
sudo apt-get install docker.io

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add your user to docker group (optional, to run without sudo)
sudo usermod -aG docker $USER
# Log out and back in for this to take effect
```

**Windows:**
```bash
# Option 1: Using winget (Windows Package Manager)
winget install Docker.DockerDesktop

# Option 2: Using Chocolatey
choco install docker-desktop

# Option 3: Download installer from https://www.docker.com/products/docker-desktop/
```

**Verify installation:**
```bash
docker --version
```
</details>

```bash
# Pull the Docker image (~280MB, no n8n dependencies!)
docker pull ghcr.io/czlonkowski/n8n-mcp:latest
```

> **⚡ Ultra-optimized:** Our Docker image is 82% smaller than typical n8n images because it contains NO n8n dependencies - just the runtime MCP server with a pre-built database!

Add to Claude Desktop config:

**Basic configuration (documentation tools only):**
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--init",
        "-e", "MCP_MODE=stdio",
        "-e", "LOG_LEVEL=error",
        "-e", "DISABLE_CONSOLE_OUTPUT=true",
        "ghcr.io/czlonkowski/n8n-mcp:latest"
      ]
    }
  }
}
```

**Full configuration (with n8n management tools):**
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--init",
        "-e", "MCP_MODE=stdio",
        "-e", "LOG_LEVEL=error",
        "-e", "DISABLE_CONSOLE_OUTPUT=true",
        "-e", "N8N_API_URL=https://your-n8n-instance.com",
        "-e", "N8N_API_KEY=your-api-key",
        "ghcr.io/czlonkowski/n8n-mcp:latest"
      ]
    }
  }
}
```

>💡 Tip: If you're running n8n locally on the same machine (e.g., via Docker), use http://host.docker.internal:5678 as the N8N_API_URL.

> **Note**: The n8n API credentials are optional. Without them, you'll have access to all documentation and validation tools. With them, you'll additionally get workflow management capabilities (create, update, execute workflows).

### 🏠 Local n8n Instance Configuration

If you're running n8n locally (e.g., `http://localhost:5678` or Docker), you need to allow localhost webhooks:

```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm", "--init",
        "-e", "MCP_MODE=stdio",
        "-e", "LOG_LEVEL=error",
        "-e", "DISABLE_CONSOLE_OUTPUT=true",
        "-e", "N8N_API_URL=http://host.docker.internal:5678",
        "-e", "N8N_API_KEY=your-api-key",
        "-e", "WEBHOOK_SECURITY_MODE=moderate",
        "ghcr.io/czlonkowski/n8n-mcp:latest"
      ]
    }
  }
}
```

> ⚠️ **Important:** Set `WEBHOOK_SECURITY_MODE=moderate` to allow webhooks to your local n8n instance. This is safe for local development while still blocking private networks and cloud metadata.

**Important:** The `-i` flag is required for MCP stdio communication.

> 🔧 If you encounter any issues with Docker, check our [Docker Troubleshooting Guide](./docs/DOCKER_TROUBLESHOOTING.md).

**Configuration file locations:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Restart Claude Desktop after updating configuration** - That's it! 🎉

## 🔐 Privacy & Telemetry

n8n-mcp collects anonymous usage statistics to improve the tool. [View our privacy policy](./PRIVACY.md).

### Opting Out

**For npx users:**
```bash
npx n8n-mcp telemetry disable
```

**For Docker users:**
Add the following environment variable to your Docker configuration:
```json
"-e", "N8N_MCP_TELEMETRY_DISABLED=true"
```

Example in Claude Desktop config:
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--init",
        "-e", "MCP_MODE=stdio",
        "-e", "LOG_LEVEL=error",
        "-e", "N8N_MCP_TELEMETRY_DISABLED=true",
        "ghcr.io/czlonkowski/n8n-mcp:latest"
      ]
    }
  }
}
```

**For docker-compose users:**
Set in your environment file or docker-compose.yml:
```yaml
environment:
  N8N_MCP_TELEMETRY_DISABLED: "true"
```

## ⚙️ Database & Memory Configuration

### Database Adapters

n8n-mcp uses SQLite for storing node documentation. Two adapters are available:

1. **better-sqlite3** (Default in Docker)
   - Native C++ bindings for best performance
   - Direct disk writes (no memory overhead)
   - **Now enabled by default** in Docker images (v2.20.2+)
   - Memory usage: ~100-120 MB stable

2. **sql.js** (Fallback)
   - Pure JavaScript implementation
   - In-memory database with periodic saves
   - Used when better-sqlite3 compilation fails
   - Memory usage: ~150-200 MB stable

### Memory Optimization (sql.js)

If using sql.js fallback, you can configure the save interval to balance between data safety and memory efficiency:

**Environment Variable:**
```bash
SQLJS_SAVE_INTERVAL_MS=5000  # Default: 5000ms (5 seconds)
```

**Usage:**
- Controls how long to wait after database changes before saving to disk
- Lower values = more frequent saves = higher memory churn
- Higher values = less frequent saves = lower memory usage
- Minimum: 100ms
- Recommended: 5000-10000ms for production

**Docker Configuration:**
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "--init",
        "-e", "SQLJS_SAVE_INTERVAL_MS=10000",
        "ghcr.io/czlonkowski/n8n-mcp:latest"
      ]
    }
  }
}
```

**docker-compose:**
```yaml
environment:
  SQLJS_SAVE_INTERVAL_MS: "10000"
```

## 💖 Support This Project

<div align="center">
  <a href="https://github.com/sponsors/czlonkowski">
    <img src="https://img.shields.io/badge/Sponsor-❤️-db61a2?style=for-the-badge&logo=github-sponsors" alt="Sponsor n8n-mcp" />
  </a>
</div>

**n8n-mcp** started as a personal tool but now helps tens of thousands of developers automate their workflows efficiently. Maintaining and developing this project competes with my paid work.

Your sponsorship helps me:
- 🚀 Dedicate focused time to new features
- 🐛 Respond quickly to issues
- 📚 Keep documentation up-to-date
- 🔄 Ensure compatibility with latest n8n releases

Every sponsorship directly translates to hours invested in making n8n-mcp better for everyone. **[Become a sponsor →](https://github.com/sponsors/czlonkowski)**

---

### Option C: Local Installation (For Development)

**Prerequisites:** [Node.js](https://nodejs.org/) installed on your system

```bash
# 1. Clone and setup
git clone https://github.com/czlonkowski/n8n-mcp.git
cd n8n-mcp
npm install
npm run build
npm run rebuild

# 2. Test it works
npm start
```

Add to Claude Desktop config:

**Basic configuration (documentation tools only):**
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "node",
      "args": ["/absolute/path/to/n8n-mcp/dist/mcp/index.js"],
      "env": {
        "MCP_MODE": "stdio",
        "LOG_LEVEL": "error",
        "DISABLE_CONSOLE_OUTPUT": "true"
      }
    }
  }
}
```

**Full configuration (with n8n management tools):**
```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "node",
      "args": ["/absolute/path/to/n8n-mcp/dist/mcp/index.js"],
      "env": {
        "MCP_MODE": "stdio",
        "LOG_LEVEL": "error",
        "DISABLE_CONSOLE_OUTPUT": "true",
        "N8N_API_URL": "https://your-n8n-instance.com",
        "N8N_API_KEY": "your-api-key"
      }
    }
  }
}
```

> **Note**: The n8n API credentials can be configured either in a `.env` file (create from `.env.example`) or directly in the Claude config as shown above.

> 💡 Tip: If you’re running n8n locally on the same machine (e.g., via Docker), use http://host.docker.internal:5678 as the N8N_API_URL.

### Option D: Railway Cloud Deployment (One-Click Deploy) ☁️

**Prerequisites:** Railway account (free tier available)

Deploy n8n-MCP to Railway's cloud platform with zero configuration:

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/deploy/n8n-mcp?referralCode=n8n-mcp)

**Benefits:**
- ☁️ **Instant cloud hosting** - No server setup required
- 🔒 **Secure by default** - HTTPS included, auth token warnings
- 🌐 **Global access** - Connect from any Claude Desktop
- ⚡ **Auto-scaling** - Railway handles the infrastructure
- 📊 **Built-in monitoring** - Logs and metrics included

**Quick Setup:**
1. Click the "Deploy on Railway" button above
2. Sign in to Railway (or create a free account)
3. Configure your deployment (project name, region)
4. Click "Deploy" and wait ~2-3 minutes
5. Copy your deployment URL and auth token
6. Add to Claude Desktop config using the HTTPS URL

> 📚 **For detailed setup instructions, troubleshooting, and configuration examples, see our [Railway Deployment Guide](./docs/RAILWAY_DEPLOYMENT.md)**

**Configuration file locations:**
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Restart Claude Desktop after updating configuration** - That's it! 🎉

## 🔧 n8n Integration

Want to use n8n-MCP with your n8n instance? Check out our comprehensive [n8n Deployment Guide](./docs/N8N_DEPLOYMENT.md) for:
- Local testing with the MCP Client Tool node
- Production deployment with Docker Compose
- Cloud deployment on Hetzner, AWS, and other providers
- Troubleshooting and security best practices

## 💻 Connect your IDE

n8n-MCP works with multiple AI-powered IDEs and tools. Choose your preferred development environment:

##
... [TRUNCATED]
```

### File: docker\README.md
```md
# Docker Usage Guide for n8n-mcp

## Running in HTTP Mode

The n8n-mcp Docker container can be run in HTTP mode using several methods:

### Method 1: Using Environment Variables (Recommended)

```bash
docker run -d -p 3000:3000 \
  --name n8n-mcp-server \
  -e MCP_MODE=http \
  -e AUTH_TOKEN=your-secure-token-here \
  ghcr.io/czlonkowski/n8n-mcp:latest
```

### Method 2: Using docker-compose

```bash
# Create a .env file
cat > .env << EOF
MCP_MODE=http
AUTH_TOKEN=your-secure-token-here
PORT=3000
EOF

# Run with docker-compose
docker-compose up -d
```

### Method 3: Using a Configuration File

Create a `config.json` file:
```json
{
  "MCP_MODE": "http",
  "AUTH_TOKEN": "your-secure-token-here",
  "PORT": "3000",
  "LOG_LEVEL": "info"
}
```

Run with the config file:
```bash
docker run -d -p 3000:3000 \
  --name n8n-mcp-server \
  -v $(pwd)/config.json:/app/config.json:ro \
  ghcr.io/czlonkowski/n8n-mcp:latest
```

### Method 4: Using the n8n-mcp serve Command

```bash
docker run -d -p 3000:3000 \
  --name n8n-mcp-server \
  -e AUTH_TOKEN=your-secure-token-here \
  ghcr.io/czlonkowski/n8n-mcp:latest \
  n8n-mcp serve
```

## Important Notes

1. **AUTH_TOKEN is required** for HTTP mode. Generate a secure token:
   ```bash
   openssl rand -base64 32
   ```

2. **Environment variables take precedence** over config file values

3. **Default mode is stdio** if MCP_MODE is not specified

4. **Health check endpoint** is available at `http://localhost:3000/health`

## Troubleshooting

### Container exits immediately
- Check logs: `docker logs n8n-mcp-server`
- Ensure AUTH_TOKEN is set for HTTP mode

### "n8n-mcp: not found" error
- This has been fixed in the latest version
- Use the full command: `node /app/dist/mcp/index.js` as a workaround

### Config file not working
- Ensure the file is valid JSON
- Mount as read-only: `-v $(pwd)/config.json:/app/config.json:ro`
- Check that the config parser is present: `docker exec n8n-mcp-server ls -la /app/docker/`
```

### File: docs\README.md
```md
# n8n-MCP Documentation

Welcome to the n8n-MCP documentation. This directory contains comprehensive guides for installation, configuration, and troubleshooting.

## 📚 Documentation Index

### Getting Started
- **[Installation Guide](./INSTALLATION.md)** - Comprehensive installation guide covering all methods
- **[Claude Desktop Setup](./README_CLAUDE_SETUP.md)** - Step-by-step guide for Claude Desktop configuration
- **[Quick Start Tutorial](../README.md)** - Basic overview and quick start instructions

### Deployment
- **[HTTP Deployment Guide](./HTTP_DEPLOYMENT.md)** - Deploy n8n-MCP as an HTTP server for remote access
- **[Docker Deployment](./DOCKER_README.md)** - Complete Docker deployment and configuration guide
- **[Release Guide](./RELEASE_GUIDE.md)** - How to create releases and manage Docker tags

### Reference
- **[Troubleshooting Guide](./TROUBLESHOOTING.md)** - Solutions for common issues and errors
- **[HTTP Server Fix Documentation](./HTTP_SERVER_FINAL_FIX.md)** - Technical details of v2.3.2 HTTP server fixes
- **[Docker Optimization Guide](./DOCKER_OPTIMIZATION_GUIDE.md)** - Reference for optimized Docker builds (~150MB)
- **[Changelog](./CHANGELOG.md)** - Version history and release notes

## 🚀 Quick Links

### For Users
- [Install n8n-MCP](./INSTALLATION.md)
- [Configure Claude Desktop](./README_CLAUDE_SETUP.md)
- [Deploy with Docker](./DOCKER_README.md)
- [Troubleshoot Issues](./TROUBLESHOOTING.md)

### For Developers
- [HTTP Server Architecture](./HTTP_SERVER_FINAL_FIX.md)
- [Docker Build Optimization](./DOCKER_OPTIMIZATION_GUIDE.md)
- [Release Process](./RELEASE_GUIDE.md)

## 📋 Environment Variables

Key configuration options:

| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_MODE` | Server mode: `stdio` or `http` | `stdio` |
| `AUTH_TOKEN` | Authentication token for HTTP mode | Required |
| `PORT` | HTTP server port | `3000` |
| `LOG_LEVEL` | Logging verbosity | `info` |

See [Installation Guide](./INSTALLATION.md#environment-configuration) for complete list.

## 🆘 Getting Help

1. Check the [Troubleshooting Guide](./TROUBLESHOOTING.md)
2. Review [HTTP Server Fix Documentation](./HTTP_SERVER_FINAL_FIX.md) for v2.3.2 issues
3. Open an issue on [GitHub](https://github.com/czlonkowski/n8n-mcp/issues)

## 📝 License

This project uses the Sustainable Use License. See [LICENSE](../LICENSE) for details.
```

### File: src\templates\README.md
```md
# n8n Templates Integration

This module provides integration with n8n.io's workflow templates, allowing AI agents to discover and use proven workflow patterns.

## Features

- **API Integration**: Connects to n8n.io's official template API
- **Fresh Templates**: Only includes templates updated within the last 6 months
- **Manual Fetch**: Templates are fetched separately from the main node database
- **Full Workflow JSON**: Complete workflow definitions ready for import
- **Smart Search**: Find templates by nodes, keywords, or task categories

## Usage

### Fetching Templates

```bash
npm run fetch:templates
```

This command will:
1. Connect to n8n.io API
2. Fetch all templates from the last 6 months
3. Download complete workflow JSON for each template
4. Store in local SQLite database
5. Display progress and statistics

### Testing

```bash
npm run test:templates
```

### MCP Tools

The following tools are available via MCP:

- `list_node_templates(nodeTypes, limit)` - Find templates using specific nodes
- `get_template(templateId)` - Get complete workflow JSON
- `search_templates(query, limit)` - Search by keywords
- `get_templates_for_task(task)` - Get templates for common tasks

### Task Categories

- `ai_automation` - AI-powered workflows
- `data_sync` - Database and spreadsheet synchronization
- `webhook_processing` - Webhook handling workflows
- `email_automation` - Email processing workflows
- `slack_integration` - Slack bots and notifications
- `data_transformation` - Data manipulation workflows
- `file_processing` - File handling workflows
- `scheduling` - Scheduled and recurring tasks
- `api_integration` - External API connections
- `database_operations` - Database CRUD operations

## Implementation Details

### Architecture

- `template-fetcher.ts` - Handles API communication and rate limiting
- `template-repository.ts` - Database operations and queries
- `template-service.ts` - Business logic and MCP integration

### Database Schema

Templates are stored in a dedicated table with:
- Workflow metadata (name, description, author)
- Node usage tracking
- View counts for popularity
- Complete workflow JSON
- Creation/update timestamps
- 6-month freshness constraint

### API Endpoints Used

- `/api/templates/workflows` - List all workflows
- `/api/templates/search` - Search with pagination
- `/api/templates/workflows/{id}` - Get specific workflow
- `/api/templates/search/filters` - Available filters

## Notes

- Templates are NOT fetched during regular database rebuilds
- Run `fetch:templates` manually when you need fresh templates
- API rate limiting is implemented (200-500ms between requests)
- Progress is shown during fetching for large datasets
```

### File: tests\mocks\README.md
```md
# MSW (Mock Service Worker) Setup for n8n API

This directory contains the MSW infrastructure for mocking n8n API responses in tests.

## Structure

```
mocks/
├── n8n-api/
│   ├── handlers.ts       # Default MSW handlers for n8n API endpoints
│   ├── data/            # Mock data for responses
│   │   ├── workflows.ts # Mock workflow data and factories
│   │   ├── executions.ts # Mock execution data and factories
│   │   └── credentials.ts # Mock credential data
│   └── index.ts         # Central exports
```

## Usage

### Basic Usage (Automatic)

MSW is automatically initialized for all tests via `vitest.config.ts`. The default handlers will intercept all n8n API requests.

```typescript
// Your test file
import { describe, it, expect } from 'vitest';
import { N8nApiClient } from '@/services/n8n-api-client';

describe('My Integration Test', () => {
  it('should work with mocked n8n API', async () => {
    const client = new N8nApiClient({ baseUrl: 'http://localhost:5678' });
    
    // This will hit the MSW mock, not the real API
    const workflows = await client.getWorkflows();
    
    expect(workflows).toBeDefined();
  });
});
```

### Custom Handlers for Specific Tests

```typescript
import { useHandlers, http, HttpResponse } from '@tests/setup/msw-setup';

it('should handle custom response', async () => {
  // Add custom handler for this test only
  useHandlers(
    http.get('*/api/v1/workflows', () => {
      return HttpResponse.json({
        data: [{ id: 'custom-workflow', name: 'Custom' }]
      });
    })
  );
  
  // Your test code here
});
```

### Using Factory Functions

```typescript
import { workflowFactory, executionFactory } from '@tests/mocks/n8n-api';

it('should test with factory data', async () => {
  const workflow = workflowFactory.simple('n8n-nodes-base.httpRequest', {
    method: 'POST',
    url: 'https://example.com/api'
  });
  
  useHandlers(
    http.get('*/api/v1/workflows/test-id', () => {
      return HttpResponse.json({ data: workflow });
    })
  );
  
  // Your test code here
});
```

### Integration Test Server

For integration tests that need more control:

```typescript
import { mswTestServer, n8nApiMock } from '@tests/integration/setup/msw-test-server';

describe('Integration Tests', () => {
  beforeAll(() => {
    mswTestServer.start({ onUnhandledRequest: 'error' });
  });
  
  afterAll(() => {
    mswTestServer.stop();
  });
  
  afterEach(() => {
    mswTestServer.reset();
  });
  
  it('should test workflow creation', async () => {
    // Use helper to mock workflow creation
    mswTestServer.use(
      n8nApiMock.mockWorkflowCreate({
        id: 'new-workflow',
        name: 'Created Workflow'
      })
    );
    
    // Your test code here
  });
});
```

### Debugging

Enable MSW debug logging:

```bash
MSW_DEBUG=true npm test
```

This will log all intercepted requests and responses.

### Best Practices

1. **Use factories for test data**: Don't hardcode test data, use the provided factories
2. **Reset handlers between tests**: This is done automatically, but be aware of it
3. **Be specific with handlers**: Use specific URLs/patterns to avoid conflicts
4. **Test error scenarios**: Use the error helpers to test error handling
5. **Verify unhandled requests**: In integration tests, verify no unexpected requests were made

### Common Patterns

#### Testing Success Scenarios
```typescript
useHandlers(
  http.get('*/api/v1/workflows/:id', ({ params }) => {
    return HttpResponse.json({
      data: workflowFactory.custom({ id: params.id as string })
    });
  })
);
```

#### Testing Error Scenarios
```typescript
useHandlers(
  http.get('*/api/v1/workflows/:id', () => {
    return HttpResponse.json(
      { message: 'Not found', code: 'NOT_FOUND' },
      { status: 404 }
    );
  })
);
```

#### Testing Pagination
```typescript
const workflows = Array.from({ length: 150 }, (_, i) => 
  workflowFactory.custom({ id: `workflow_${i}` })
);

useHandlers(
  http.get('*/api/v1/workflows', ({ request }) => {
    const url = new URL(request.url);
    const limit = parseInt(url.searchParams.get('limit') || '100');
    const cursor = url.searchParams.get('cursor');
    
    const start = cursor ? parseInt(cursor) : 0;
    const data = workflows.slice(start, start + limit);
    
    return HttpResponse.json({
      data,
      nextCursor: start + limit < workflows.length ? String(start + limit) : null
    });
  })
);
```
```

### File: tests\utils\README.md
```md
# Test Database Utilities

This directory contains comprehensive database testing utilities for the n8n-mcp project. These utilities simplify database setup, data seeding, and state management in tests.

## Overview

The `database-utils.ts` file provides a complete set of utilities for:
- Creating test databases (in-memory or file-based)
- Seeding test data (nodes and templates)
- Managing database state (snapshots, resets)
- Loading fixtures from JSON files
- Helper functions for common database operations

## Quick Start

```typescript
import { createTestDatabase, seedTestNodes, dbHelpers } from '../utils/database-utils';

describe('My Test', () => {
  let testDb;
  
  afterEach(async () => {
    if (testDb) await testDb.cleanup();
  });
  
  it('should test something', async () => {
    // Create in-memory database
    testDb = await createTestDatabase();
    
    // Seed test data
    await seedTestNodes(testDb.nodeRepository);
    
    // Run your tests
    const node = testDb.nodeRepository.getNode('nodes-base.httpRequest');
    expect(node).toBeDefined();
  });
});
```

## Main Functions

### createTestDatabase(options?)
Creates a test database with repositories.

Options:
- `inMemory` (boolean, default: true) - Use in-memory SQLite
- `dbPath` (string) - Custom path for file-based database
- `initSchema` (boolean, default: true) - Initialize database schema
- `enableFTS5` (boolean, default: false) - Enable full-text search

### seedTestNodes(repository, nodes?)
Seeds test nodes into the database. Includes 3 default nodes (httpRequest, webhook, slack) plus any custom nodes provided.

### seedTestTemplates(repository, templates?)
Seeds test templates into the database. Includes 2 default templates plus any custom templates provided.

### createTestNode(overrides?)
Creates a test node with sensible defaults that can be overridden.

### createTestTemplate(overrides?)
Creates a test template with sensible defaults that can be overridden.

### resetDatabase(adapter)
Drops all tables and reinitializes the schema.

### createDatabaseSnapshot(adapter)
Creates a snapshot of the current database state.

### restoreDatabaseSnapshot(adapter, snapshot)
Restores database to a previous snapshot state.

### loadFixtures(adapter, fixturePath)
Loads nodes and templates from a JSON fixture file.

## Database Helpers (dbHelpers)

- `countRows(adapter, table)` - Count rows in a table
- `nodeExists(adapter, nodeType)` - Check if a node exists
- `getAllNodeTypes(adapter)` - Get all node type strings
- `clearTable(adapter, table)` - Clear all rows from a table
- `executeSql(adapter, sql)` - Execute raw SQL

## Testing Patterns

### Unit Tests (In-Memory Database)
```typescript
const testDb = await createTestDatabase(); // Fast, isolated
```

### Integration Tests (File Database)
```typescript
const testDb = await createTestDatabase({
  inMemory: false,
  dbPath: './test.db'
});
```

### Using Fixtures
```typescript
await loadFixtures(testDb.adapter, './fixtures/complex-scenario.json');
```

### State Management with Snapshots
```typescript
// Save current state
const snapshot = await createDatabaseSnapshot(testDb.adapter);

// Do risky operations...

// Restore if needed
await restoreDatabaseSnapshot(testDb.adapter, snapshot);
```

### Transaction Testing
```typescript
await withTransaction(testDb.adapter, async () => {
  // Operations here will be rolled back
  testDb.nodeRepository.saveNode(node);
});
```

### Performance Testing
```typescript
const duration = await measureDatabaseOperation('Bulk Insert', async () => {
  // Insert many nodes
});
expect(duration).toBeLessThan(1000);
```

## Fixture Format

JSON fixtures should follow this format:

```json
{
  "nodes": [
    {
      "nodeType": "nodes-base.example",
      "displayName": "Example Node",
      "description": "Description",
      "category": "Category",
      "isAITool": false,
      "isTrigger": false,
      "isWebhook": false,
      "properties": [],
      "credentials": [],
      "operations": [],
      "version": "1",
      "isVersioned": false,
      "packageName": "n8n-nodes-base"
    }
  ],
  "templates": [
    {
      "id": 1001,
      "name": "Template Name",
      "description": "Template description",
      "workflow": { ... },
      "nodes": [ ... ],
      "categories": [ ... ]
    }
  ]
}
```

## Best Practices

1. **Always cleanup**: Use `afterEach` to call `testDb.cleanup()`
2. **Use in-memory for unit tests**: Faster and isolated
3. **Use snapshots for complex scenarios**: Easy rollback
4. **Seed minimal data**: Only what's needed for the test
5. **Use fixtures for complex scenarios**: Reusable test data
6. **Test both empty and populated states**: Edge cases matter

## TypeScript Support

All utilities are fully typed. Import types as needed:

```typescript
import type { 
  TestDatabase, 
  TestDatabaseOptions, 
  DatabaseSnapshot 
} from '../utils/database-utils';
```

## Examples

See `tests/examples/using-database-utils.test.ts` for comprehensive examples of all features.
```

### File: tests\unit\database\README.md
```md
# Database Layer Unit Tests

This directory contains comprehensive unit tests for the database layer components of n8n-mcp.

## Test Coverage

### node-repository.ts - 100% Coverage ✅
- `saveNode` method with JSON serialization
- `getNode` method with JSON deserialization  
- `getAITools` method
- `safeJsonParse` private method
- Edge cases: large JSON, boolean conversion, invalid JSON handling

### template-repository.ts - 80.31% Coverage ✅
- FTS5 initialization and fallback
- `saveTemplate` with sanitization
- `getTemplate` and `getTemplatesByNodes`
- `searchTemplates` with FTS5 and LIKE fallback
- `getTemplatesForTask` with task mapping
- Template statistics and maintenance operations
- Uncovered: Some error paths in FTS5 operations

### database-adapter.ts - Tested via Mocks
- Interface compliance tests
- PreparedStatement implementation
- Transaction support
- FTS5 detection logic
- Error handling patterns

## Test Strategy

The tests use a mock-based approach to:
1. Isolate database operations from actual database dependencies
2. Test business logic without requiring real SQLite/sql.js
3. Ensure consistent test execution across environments
4. Focus on behavior rather than implementation details

## Key Test Files

- `node-repository-core.test.ts` - Core NodeRepository functionality
- `template-repository-core.test.ts` - Core TemplateRepository functionality  
- `database-adapter-unit.test.ts` - DatabaseAdapter interface and patterns

## Running Tests

```bash
# Run all database tests
npm test -- tests/unit/database/

# Run with coverage
npm run test:coverage -- tests/unit/database/

# Run specific test file
npm test -- tests/unit/database/node-repository-core.test.ts
```

## Mock Infrastructure

The tests use custom mock implementations:
- `MockDatabaseAdapter` - Simulates database operations
- `MockPreparedStatement` - Simulates SQL statement execution
- Mock logger and template sanitizer for external dependencies

This approach ensures tests are fast, reliable, and maintainable.
```

### File: tests\unit\__mocks__\README.md
```md
# n8n-nodes-base Mock

This directory contains comprehensive mocks for n8n packages used in unit tests.

## n8n-nodes-base Mock

The `n8n-nodes-base.ts` mock provides a complete testing infrastructure for code that depends on n8n nodes.

### Features

1. **Pre-configured Node Types**
   - `webhook` - Trigger node with webhook functionality
   - `httpRequest` - HTTP request node with mock responses
   - `slack` - Slack integration with all resources and operations
   - `function` - JavaScript code execution node
   - `noOp` - Pass-through utility node
   - `merge` - Data stream merging node
   - `if` - Conditional branching node
   - `switch` - Multi-output routing node

2. **Flexible Mock Behavior**
   - Override node execution logic
   - Customize node descriptions
   - Add custom nodes dynamically
   - Reset all mocks between tests

### Basic Usage

```typescript
import { vi } from 'vitest';

// Mock the module
vi.mock('n8n-nodes-base', () => import('../__mocks__/n8n-nodes-base'));

// In your test
import { getNodeTypes, mockNodeBehavior, resetAllMocks } from '../__mocks__/n8n-nodes-base';

describe('Your test', () => {
  beforeEach(() => {
    resetAllMocks();
  });

  it('should get node description', () => {
    const registry = getNodeTypes();
    const slackNode = registry.getByName('slack');
    
    expect(slackNode?.description.name).toBe('slack');
  });
});
```

### Advanced Usage

#### Override Node Behavior

```typescript
mockNodeBehavior('httpRequest', {
  execute: async function(this: IExecuteFunctions) {
    return [[{ json: { custom: 'response' } }]];
  }
});
```

#### Add Custom Nodes

```typescript
import { registerMockNode } from '../__mocks__/n8n-nodes-base';

const customNode = {
  description: {
    displayName: 'Custom Node',
    name: 'customNode',
    group: ['transform'],
    version: 1,
    description: 'A custom test node',
    defaults: { name: 'Custom' },
    inputs: ['main'],
    outputs: ['main'],
    properties: []
  },
  execute: async function() {
    return [[{ json: { result: 'custom' } }]];
  }
};

registerMockNode('customNode', customNode);
```

#### Mock Execution Context

```typescript
const mockContext = {
  getInputData: vi.fn(() => [{ json: { test: 'data' } }]),
  getNodeParameter: vi.fn((name: string) => {
    const params = {
      method: 'POST',
      url: 'https://api.example.com'
    };
    return params[name];
  }),
  getCredentials: vi.fn(async () => ({ apiKey: 'test-key' })),
  helpers: {
    returnJsonArray: vi.fn(),
    httpRequest: vi.fn()
  }
};

const result = await node.execute.call(mockContext);
```

### Mock Structure

Each mock node implements the `INodeType` interface with:

- `description`: Complete node metadata including properties, inputs/outputs, credentials
- `execute`: Mock implementation for regular nodes (returns `INodeExecutionData[][]`)
- `webhook`: Mock implementation for trigger nodes (returns webhook data)

### Testing Patterns

1. **Unit Testing Node Logic**
   ```typescript
   const node = registry.getByName('slack');
   const result = await node.execute.call(mockContext);
   expect(result[0][0].json.ok).toBe(true);
   ```

2. **Testing Node Properties**
   ```typescript
   const node = registry.getByName('httpRequest');
   const methodProp = node.description.properties.find(p => p.name === 'method');
   expect(methodProp.options).toHaveLength(6);
   ```

3. **Testing Conditional Nodes**
   ```typescript
   const ifNode = registry.getByName('if');
   const [trueOutput, falseOutput] = await ifNode.execute.call(mockContext);
   expect(trueOutput).toHaveLength(2);
   expect(falseOutput).toHaveLength(1);
   ```

### Utilities

- `resetAllMocks()` - Clear all mock function calls
- `mockNodeBehavior(name, overrides)` - Override specific node behavior
- `registerMockNode(name, node)` - Add new mock nodes
- `getNodeTypes()` - Get the node registry with `getByName` and `getByNameAndVersion`

### See Also

- `tests/unit/examples/using-n8n-nodes-base-mock.test.ts` - Complete usage examples
- `tests/unit/__mocks__/n8n-nodes-base.test.ts` - Mock test coverage
```

### File: ANALYSIS_QUICK_REFERENCE.md
```md
# N8N-MCP Validation Analysis: Quick Reference

**Analysis Date**: November 8, 2025 | **Data Period**: 90 days | **Sample Size**: 29,218 events

---

## The Core Finding

**Validation is working perfectly. Guidance is the problem.**

- 29,218 validation events successfully prevented bad deployments
- 100% of agents fix errors same-day (proving feedback works)
- 12.6% error rate for advanced users (who attempt complex workflows)
- High error volume = high usage, not broken system

---

## Top 3 Problem Areas (75% of errors)

| Area | Errors | Root Cause | Quick Fix |
|------|--------|-----------|-----------|
| **Workflow Structure** | 1,268 (26%) | JSON malformation | Better error messages with examples |
| **Connections** | 676 (14%) | Syntax unintuitive | Create connections guide with diagrams |
| **Required Fields** | 378 (8%) | Not marked upfront | Add "⚠️ REQUIRED" to tool responses |

---

## Problem Nodes (By Frequency)

```
Webhook/Trigger ......... 127 failures (40 users)
Slack .................. 73 failures (2 users)
AI Agent ............... 36 failures (20 users)
HTTP Request ........... 31 failures (13 users)
OpenAI ................. 35 failures (8 users)
```

---

## Top 5 Validation Errors

1. **"Duplicate node ID: undefined"** (179)
   - Fix: Point to exact location + show example format

2. **"Single-node workflows only valid for webhooks"** (58)
   - Fix: Create webhook guide explaining rule

3. **"responseNode requires onError: continueRegularOutput"** (57)
   - Fix: Same guide + inline error context

4. **"Required property X cannot be empty"** (25)
   - Fix: Mark required fields before validation

5. **"Duplicate node name: undefined"** (61)
   - Fix: Related to structural issues, same solution as #1

---

## Success Indicators

✓ **Agents learn from errors**: 100% same-day correction rate
✓ **Validation catches issues**: Prevents bad deployments
✓ **Feedback is clear**: Quick fixes show error messages work
✓ **No systemic failures**: No "unfixable" errors

---

## What Works Well

- Error messages lead to immediate corrections
- Agents retry and succeed same-day
- Validation prevents broken workflows
- 9,021 users actively using system

---

## What Needs Improvement

1. Required fields not marked in tool responses
2. Error messages don't show valid options for enums
3. Workflow structure documentation lacks examples
4. Connection syntax unintuitive/undocumented
5. Some error messages too generic

---

## Implementation Plan

### Phase 1 (2 weeks): Quick Wins
- Enhanced error messages (location + example)
- Required field markers in tools
- Webhook configuration guide
- **Expected Impact**: 25-30% failure reduction

### Phase 2 (2 weeks): Documentation
- Enum value suggestions in validation
- Workflow connections guide
- Error handler configuration guide
- AI Agent validation improvements
- **Expected Impact**: Additional 15-20% reduction

### Phase 3 (2 weeks): Advanced Features
- Improved search with config hints
- Node type fuzzy matching
- KPI tracking setup
- Test coverage
- **Expected Impact**: Additional 10-15% reduction

**Total Impact**: 50-65% failure reduction (target: 6-7% error rate)

---

## Key Metrics

| Metric | Current | Target | Timeline |
|--------|---------|--------|----------|
| Validation failure rate | 12.6% | 6-7% | 6 weeks |
| First-attempt success | ~77% | 85%+ | 6 weeks |
| Retry success | 100% | 100% | N/A |
| Webhook failures | 127 | <30 | Week 2 |
| Connection errors | 676 | <270 | Week 4 |

---

## Files Delivered

1. **VALIDATION_ANALYSIS_REPORT.md** (27KB)
   - Complete analysis with 16 SQL queries
   - Detailed findings by category
   - 8 actionable recommendations

2. **VALIDATION_ANALYSIS_SUMMARY.md** (13KB)
   - Executive summary (one-page)
   - Key metrics scorecard
   - Top recommendations with ROI

3. **IMPLEMENTATION_ROADMAP.md** (4.3KB)
   - 6-week implementation plan
   - Phase-by-phase breakdown
   - Code locations and effort estimates

4. **ANALYSIS_QUICK_REFERENCE.md** (this file)
   - Quick lookup reference
   - Top problems at a glance
   - Decision-making summary

---

## Next Steps

1. **Week 1**: Review analysis + get team approval
2. **Week 2**: Start Phase 1 (error messages + markers)
3. **Week 4**: Deploy Phase 1 + start Phase 2
4. **Week 6**: Deploy Phase 2 + start Phase 3
5. **Week 8**: Deploy Phase 3 + measure impact
6. **Week 9+**: Monitor KPIs + iterate

---

## Key Recommendations Priority

### HIGH (Do First - Week 1-2)
1. Enhance structure error messages
2. Add required field markers to tools
3. Create webhook configuration guide

### MEDIUM (Do Next - Week 3-4)
4. Add enum suggestions to validation responses
5. Create workflow connections guide
6. Add AI Agent node validation

### LOW (Do Later - Week 5-6)
7. Enhance search with config hints
8. Build fuzzy node matcher
9. Setup KPI tracking

---

## Discussion Points

**Q: Why don't we just weaken validation?**
A: Validation prevents 29,218 bad deployments. That's its job. We improve guidance instead.

**Q: Are agents really learning from errors?**
A: Yes, 100% same-day recovery across 661 user-date pairs with errors.

**Q: Why do documentation readers have higher error rates?**
A: They attempt more complex workflows (6.8x more attempts). Success rate is still 87.4%.

**Q: Which node needs the most help?**
A: Webhook/Trigger configuration (127 failures). Most urgent fix.

**Q: Can we hit 50% reduction in 6 weeks?**
A: Yes, analysis shows 50-65% reduction is achievable with these changes.

---

## Contact & Questions

For detailed information:
- Full analysis: `VALIDATION_ANALYSIS_REPORT.md`
- Executive summary: `VALIDATION_ANALYSIS_SUMMARY.md`
- Implementation plan: `IMPLEMENTATION_ROADMAP.md`

---

**Report Status**: Complete and Ready for Action
**Confidence Level**: High (9,021 users, 29,218 events, comprehensive analysis)
**Generated**: November 8, 2025

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

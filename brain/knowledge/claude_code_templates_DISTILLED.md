---
id: claude-code-templates
type: knowledge
owner: OA_Triage
---
# claude-code-templates
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "claude-code-templates",
  "version": "1.28.16",
  "description": "Component templates and tracking system for Claude Code",
  "main": "cli-tool/src/index.js",
  "bin": {
    "claude-code-templates": "cli-tool/bin/create-claude-config.js",
    "cct": "cli-tool/bin/create-claude-config.js"
  },
  "scripts": {
    "dev": "vercel dev",
    "build": "echo 'Build complete'",
    "start": "vercel dev",
    "test": "echo 'No tests specified'",
    "agent:security-auditor": "security-auditor 'Security audit covering codebase, dependencies, and deployment configuration'",
    "deploy": "./scripts/deploy.sh",
    "deploy:dashboard": "./scripts/deploy.sh",
    "discord:register": "node api/discord/register-commands.cjs"
  },
  "dependencies": {
    "@supabase/supabase-js": "^2.39.0",
    "@vercel/postgres": "^0.10.0",
    "axios": "^1.6.2",
    "boxen": "^5.1.2",
    "chalk": "^4.1.2",
    "chokidar": "^3.5.3",
    "commander": "^11.1.0",
    "discord-interactions": "^3.4.0",
    "dotenv": "^16.3.1",
    "express": "^4.18.2",
    "fs-extra": "^11.1.1",
    "inquirer": "^8.2.6",
    "js-yaml": "^4.1.1",
    "open": "^8.4.2",
    "ora": "^5.4.1",
    "qrcode": "^1.5.4",
    "uuid": "^11.1.0",
    "ws": "^8.18.3"
  },
  "devDependencies": {
    "@vercel/node": "^3.0.0"
  },
  "keywords": [
    "claude-code",
    "templates",
    "components",
    "tracking",
    "analytics"
  ],
  "author": "Claude Code Templates",
  "license": "MIT"
}

```

### File: README.md
```md
[![npm version](https://img.shields.io/npm/v/claude-code-templates.svg)](https://www.npmjs.com/package/claude-code-templates)
[![npm downloads](https://img.shields.io/npm/dt/claude-code-templates.svg)](https://www.npmjs.com/package/claude-code-templates)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Sponsored by Z.AI](https://img.shields.io/badge/Sponsored%20by-Z.AI-2563eb?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTEyIDJMMiAyMkgyMkwxMiAyWiIgZmlsbD0id2hpdGUiLz4KPC9zdmc+)](https://z.ai/subscribe?ic=8JVLJQFSKB&utm_source=github&utm_medium=badge&utm_campaign=readme)
[![Claude for Open Source](https://img.shields.io/badge/Claude-Open%20Source%20Program-D97757?style=flat&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIzIiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==)](https://claude.com/contact-sales/claude-for-oss)
[![Neon Open Source Program](https://img.shields.io/badge/Neon-Open%20Source%20Program-00E599?style=flat)](https://get.neon.com/4eCjZDz)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-support-yellow?style=flat&logo=buy-me-a-coffee)](https://buymeacoffee.com/daniavila)
[![GitHub stars](https://img.shields.io/github/stars/davila7/claude-code-templates.svg?style=social&label=Star)](https://github.com/davila7/claude-code-templates)

<p align="center">
  <a href="https://trendshift.io/repositories/15113" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15113" alt="davila7%2Fclaude-code-templates | Trendshift" style="width: 200px; height: 40px;" width="125" height="40"/>
  </a>
  <br />
  <br />
  <a href="https://vercel.com/oss">
  <img alt="Vercel OSS Program" src="https://vercel.com/oss/program-badge.svg" />
  </a>
  &nbsp;&nbsp;
  <a href="https://get.neon.com/4eCjZDz">
  <img alt="Neon Open Source Program" src="https://img.shields.io/badge/Neon-Open%20Source%20Program-00E599?style=for-the-badge" />
  </a>
  &nbsp;&nbsp;
  <a href="https://claude.com/contact-sales/claude-for-oss">
  <img alt="Claude for Open Source" src="docs/claude-oss-badge.svg" height="48" />
  </a>
</p>

---

> **🧪 NEW: Dashboard** — Explore components, manage collections, and track installations at **[www.aitmpl.com](https://www.aitmpl.com)**. Currently in beta — feedback welcome!

# Claude Code Templates ([aitmpl.com](https://aitmpl.com))

**Ready-to-use configurations for Anthropic's Claude Code.** A comprehensive collection of AI agents, custom commands, settings, hooks, external integrations (MCPs), and project templates to enhance your development workflow.

## Browse & Install Components and Templates

**[Browse All Templates](https://aitmpl.com)** - Interactive web interface to explore and install 100+ agents, commands, settings, hooks, and MCPs.

<img width="1049" height="855" alt="Screenshot 2025-08-19 at 08 09 24" src="https://github.com/user-attachments/assets/e3617410-9b1c-4731-87b7-a3858800b737" />

## 🚀 Quick Installation

```bash
# Install a complete development stack
npx claude-code-templates@latest --agent development-team/frontend-developer --command testing/generate-tests --mcp development/github-integration --yes

# Browse and install interactively
npx claude-code-templates@latest

# Install specific components
npx claude-code-templates@latest --agent development-tools/code-reviewer --yes
npx claude-code-templates@latest --command performance/optimize-bundle --yes
npx claude-code-templates@latest --setting performance/mcp-timeouts --yes
npx claude-code-templates@latest --hook git/pre-commit-validation --yes
npx claude-code-templates@latest --mcp database/postgresql-integration --yes
```

## What You Get

| Component | Description | Examples |
|-----------|-------------|----------|
| **🤖 Agents** | AI specialists for specific domains | Security auditor, React performance optimizer, database architect |
| **⚡ Commands** | Custom slash commands | `/generate-tests`, `/optimize-bundle`, `/check-security` |
| **🔌 MCPs** | External service integrations | GitHub, PostgreSQL, Stripe, AWS, OpenAI |
| **⚙️ Settings** | Claude Code configurations | Timeouts, memory settings, output styles |
| **🪝 Hooks** | Automation triggers | Pre-commit validation, post-completion actions |
| **🎨 Skills** | Reusable capabilities with progressive disclosure | PDF processing, Excel automation, custom workflows |

## 🛠️ Additional Tools

Beyond the template catalog, Claude Code Templates includes powerful development tools:

### 📊 Claude Code Analytics
Monitor your AI-powered development sessions in real-time with live state detection and performance metrics.

```bash
npx claude-code-templates@latest --analytics
```

### 💬 Conversation Monitor  
Mobile-optimized interface to view Claude responses in real-time with secure remote access.

```bash
# Local access
npx claude-code-templates@latest --chats

# Secure remote access via Cloudflare Tunnel
npx claude-code-templates@latest --chats --tunnel
```

### 🔍 Health Check
Comprehensive diagnostics to ensure your Claude Code installation is optimized.

```bash
npx claude-code-templates@latest --health-check
```

### 🔌 Plugin Dashboard
View marketplaces, installed plugins, and manage permissions from a unified interface.

```bash
npx claude-code-templates@latest --plugins
```

## 📖 Documentation

**[📚 docs.aitmpl.com](https://docs.aitmpl.com/)** - Complete guides, examples, and API reference for all components and tools.

## Contributing

We welcome contributions! **[Browse existing templates](https://aitmpl.com)** to see what's available, then check our [contributing guidelines](CONTRIBUTING.md) to add your own agents, commands, MCPs, settings, or hooks.

**Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.**

## Attribution

This collection includes components from multiple sources:

**Scientific Skills:**
- **[K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills)** by K-Dense Inc. - MIT License (139 scientific skills for biology, chemistry, medicine, and computational research)

**Official Anthropic:**
- **[anthropics/skills](https://github.com/anthropics/skills)** - Official Anthropic skills (21 skills)
- **[anthropics/claude-code](https://github.com/anthropics/claude-code)** - Development guides and examples (10 skills)

**Community Skills & Agents:**
- **[obra/superpowers](https://github.com/obra/superpowers)** by Jesse Obra - MIT License (14 workflow skills)
- **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)** by Alireza Rezvani - MIT License (36 professional role skills)
- **[wshobson/agents](https://github.com/wshobson/agents)** by wshobson - MIT License (48 agents)
- **NerdyChefsAI Skills** - Community contribution - MIT License (specialized enterprise skills)

**Commands & Tools:**
- **[awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** by hesreallyhim - CC0 1.0 Universal (21 commands)
- **[awesome-claude-skills](https://github.com/mehdi-lamrani/awesome-claude-skills)** - Apache 2.0 (community skills)
- **move-code-quality-skill** - MIT License
- **cocoindex-claude** - Apache 2.0

Each of these resources retains its **original license and attribution**, as defined by their respective authors.
We respect and credit all original creators for their work and contributions to the Claude ecosystem.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **🌐 Browse Templates**: [aitmpl.com](https://aitmpl.com)
- **📚 Documentation**: [docs.aitmpl.com](https://docs.aitmpl.com)
- **💬 Community**: [GitHub Discussions](https://github.com/davila7/claude-code-templates/discussions)
- **🐛 Issues**: [GitHub Issues](https://github.com/davila7/claude-code-templates/issues)

## Stargazers over time
[![Stargazers over time](https://starchart.cc/davila7/claude-code-templates.svg?variant=adaptive)](https://starchart.cc/davila7/claude-code-templates)

---

**⭐ Found this useful? Give us a star to support the project!**

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&slug=daniavila&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/daniavila)
```

### File: docs\README.md
```md
# Claude Code Templates Website

This directory contains the static website for browsing and installing Claude Code configuration templates.

## Features

- **Dynamic Template Loading**: Templates are loaded directly from the GitHub repository's `templates.js` file
- **Interactive Cards**: Click any template card to see the installation command
- **Responsive Design**: Works on desktop and mobile devices
- **Framework Logos**: Uses Devicon CDN for professional programming language and framework logos
- **Copy to Clipboard**: Easy command copying with visual feedback

## Architecture

The website is built as a static site that:

1. **Fetches template data** from `cli-tool/src/templates.js` in the GitHub repository
2. **Parses the configuration** to extract available languages and frameworks
3. **Generates cards dynamically** with proper logos from Devicon CDN
4. **Updates automatically** when new templates are added to the repository

## Files

- `index.html` - Main HTML structure
- `styles.css` - Styling and responsive design
- `script.js` - JavaScript for dynamic content loading and interactions
- `_config.yml` - Jekyll configuration for GitHub Pages
- `README.md` - This documentation

## GitHub Pages Deployment

This website is automatically deployed to GitHub Pages when changes are pushed to the `docs/` directory in the main branch.

Visit: [https://davila7.github.io/claude-code-templates](https://davila7.github.io/claude-code-templates)

## Development

To test locally:

1. Clone the repository
2. Navigate to the `docs/` directory
3. Serve with any static file server (e.g., `python -m http.server 8000`)
4. Open `http://localhost:8000`

## Dependencies

- **Devicon CDN**: For programming language and framework logos
- **GitHub Raw Content**: For fetching template configurations
- **Modern Browser**: Support for ES6+ features and Fetch API
```

### File: docs\api\README.md
```md
# API Directory - Documentation

This directory contains **static files** for the Claude Code Templates project deployed on Vercel.

## 📁 Structure Overview

```
docs/api/
├── README.md     # This file
└── agents.json   # Static JSON file for agent queries
```

## 🔍 Why This Structure?

The project uses **TWO separate API directories**:

### 1. `/api/` (Root) - Serverless Functions ✅
```
/api/
├── track-download-supabase.js     # Serverless function
└── package.json                   # Dependencies
```

- **Purpose:** Vercel serverless functions (Edge Functions)
- **Auto-detected by Vercel:** Functions in `/api/` are automatically deployed
- **Runtime:** Node.js with ES Modules
- **URL:** `https://www.aitmpl.com/api/track-download-supabase`

### 2. `/docs/api/` - Static Files ✅
```
/docs/api/
├── README.md      # This documentation
└── agents.json    # Static data file
```

- **Purpose:** Static JSON files served with the frontend
- **Served from:** `outputDirectory: "docs"` in `vercel.json`
- **URL:** `https://www.aitmpl.com/api/agents.json`

## ⚠️ Important: Why Two Directories?

Vercel has a specific requirement:
- **Serverless functions MUST be in `/api/`** at the project root
- **Static files can be in `/docs/api/`** when using `outputDirectory: "docs"`

You **cannot** put serverless functions in `/docs/api/` - Vercel will serve them as static HTML files instead of executing them.

---

## 📄 Files in This Directory

### `agents.json` (Static File)
- **Type:** Static JSON data
- **Purpose:** Contains the list of available agents for the frontend
- **Accessed by:** Frontend application via fetch
- **URL:** `https://www.aitmpl.com/api/agents.json`
- **Size:** ~25KB
- **Updates:** Generated by `/scripts/generate_components_json.py` script

**Usage:**
```javascript
fetch('https://www.aitmpl.com/api/agents.json')
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## 🔗 Related Files

### Serverless Functions (in `/api/`)

See `/api/README.md` for documentation on:
- `track-download-supabase.js` - Download tracking endpoint
- Environment variables required
- Request/response formats
- Database schema

---

## 📝 Best Practices

1. **Static Files:** Keep in `/docs/api/`
2. **Serverless Functions:** Keep in `/api/` (root)
3. **Never Mix:** Don't put serverless functions in `/docs/api/`
4. **Version Control:** Commit both directories separately

---

**Last Updated:** October 22, 2025
**Maintained by:** Claude Code Templates Team

```

### File: .claude-plugin_DISTILLED.md
```md
---
id: .claude-plugin
type: distilled_knowledge
---
# .claude-plugin

## SWALLOW ENGINE DISTILLATION

### File: marketplace.json
```json
{
  "name": "claude-code-templates",
  "owner": {
    "name": "Daniel Avila",
    "email": "davila7@users.noreply.github.com",
    "url": "https://github.com/davila7"
  },
  "metadata": {
    "description": "Ready-to-use Claude Code templates organized by workflow",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "git-workflow",
      "source": "./",
      "description": "Git workflow automation: feature, release, and hotfix commands with git specialists",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["git", "workflow", "automation"],
      "strict": false,
      "commands": [
        "./cli-tool/components/commands/git/feature.md",
        "./cli-tool/components/commands/git/release.md",
        "./cli-tool/components/commands/git/hotfix.md",
        "./cli-tool/components/commands/git/finish.md",
        "./cli-tool/components/commands/git/flow-status.md"
      ],
      "agents": ["./cli-tool/components/agents/git/git-flow-manager.md"]
    },
    {
      "name": "supabase-toolkit",
      "source": "./",
      "description": "Complete Supabase workflow with specialized commands, data engineering agents, and MCP integrations",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["supabase", "database", "postgresql", "data"],
      "strict": false,
      "commands": [
        "./cli-tool/components/commands/database/supabase-backup-manager.md",
        "./cli-tool/components/commands/database/supabase-data-explorer.md",
        "./cli-tool/components/commands/database/supabase-migration-assistant.md",
        "./cli-tool/components/commands/database/supabase-performance-optimizer.md",
        "./cli-tool/components/commands/database/supabase-schema-sync.md"
      ],
      "agents": [
        "./cli-tool/components/agents/data-ai/data-engineer.md",
        "./cli-tool/components/agents/data-ai/data-scientist.md"
      ],
      "mcpServers": [
        "./cli-tool/components/mcps/database/postgresql-integration.json",
        "./cli-tool/components/mcps/database/mysql-integration.json",
        "./cli-tool/components/mcps/database/supabase.json"
      ]
    },
    {
      "name": "nextjs-vercel-pro",
      "source": "./",
      "description": "Complete Next.js and Vercel development toolkit with deployment automation and performance optimization",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["nextjs", "vercel", "react", "deployment", "performance"],
      "strict": false,
      "commands": [
        "./cli-tool/components/commands/nextjs-vercel/nextjs-scaffold.md",
        "./cli-tool/components/commands/nextjs-vercel/nextjs-component-generator.md",
        "./cli-tool/components/commands/nextjs-vercel/nextjs-api-tester.md",
        "./cli-tool/components/commands/nextjs-vercel/nextjs-performance-audit.md",
        "./cli-tool/components/commands/nextjs-vercel/vercel-deploy-optimize.md",
        "./cli-tool/components/commands/nextjs-vercel/vercel-edge-function.md",
        "./cli-tool/components/commands/nextjs-vercel/vercel-env-sync.md"
      ],
      "agents": [
        "./cli-tool/components/agents/development-team/frontend-developer.md",
        "./cli-tool/components/agents/development-team/fullstack-developer.md"
      ],
      "mcpServers": [
        "./cli-tool/components/mcps/devtools/vercel-mcp.json"
      ]
    },
    {
      "name": "testing-suite",
      "source": "./",
      "description": "Comprehensive testing toolkit with E2E, unit, integration, and visual testing automation",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["testing", "qa", "e2e", "automation", "quality"],
      "strict": false,
      "commands": [
        "./cli-tool/components/commands/testing/generate-tests.md",
        "./cli-tool/components/commands/testing/e2e-setup.md",
        "./cli-tool/components/commands/testing/test-coverage.md",
        "./cli-tool/components/commands/testing/setup-visual-testing.md",
        "./cli-tool/components/commands/testing/setup-load-testing.md",
        "./cli-tool/components/commands/testing/test-automation-orchestrator.md",
        "./cli-tool/components/commands/testing/test-quality-analyzer.md"
      ],
      "agents": [
        "./cli-tool/components/agents/development-tools/qa-automation-engineer.md",
        "./cli-tool/components/agents/development-tools/test-engineer.md"
      ],
      "mcpServers": [
        "./cli-tool/components/mcps/browser_automation/playwright-mcp.json"
      ]
    },
    {
      "name": "security-pro",
      "source": "./",
      "description": "Enterprise security toolkit with auditing, penetration testing, and compliance automation",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["security", "audit", "compliance", "pentesting", "vulnerability"],
      "strict": false,
      "commands": [
        "./cli-tool/components/commands/security/security-audit.md",
        "./cli-tool/components/commands/security/vulnerability-scan.md",
        "./cli-tool/components/commands/security/dependency-audit.md",
        "./cli-tool/components/commands/security/code-security-review.md"
      ],
      "agents": [
        "./cli-tool/components/agents/security/security-auditor.md",
        "./cli-tool/components/agents/security/penetration-tester.md",
        "./cli-tool/components/agents/security/compliance-specialist.md",
        "./cli-tool/components/agents/security/incident-responder.md"
      ]
    },
    {
      "name": "ai-ml-toolkit",
      "source": "./",
      "description": "AI and Machine Learning development suite with data engineering and model deployment tools",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["ai", "ml", "machine-learning", "data-science", "nlp"],
      "strict": false,
      "agents": [
        "./cli-tool/components/agents/data-ai/ai-engineer.md",
        "./cli-tool/components/agents/data-ai/ml-engineer.md",
        "./cli-tool/components/agents/data-ai/nlp-engineer.md",
        "./cli-tool/components/agents/data-ai/computer-vision-engineer.md",
        "./cli-tool/components/agents/data-ai/mlops-engineer.md"
      ]
      
    },
    {
      "name": "devops-automation",
      "source": "./",
      "description": "DevOps automation suite with CI/CD, infrastructure management, and deployment orchestration",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["devops", "cicd", "infrastructure", "deployment", "automation"],
      "strict": false,
      "commands": [
        "./cli-tool/components/commands/deployment/setup-ci-cd-pipeline.md",
        "./cli-tool/components/commands/deployment/docker-compose-setup.md",
        "./cli-tool/components/commands/deployment/kubernetes-deploy.md",
        "./cli-tool/components/commands/deployment/monitoring-setup.md",
        "./cli-tool/components/commands/deployment/backup-strategy.md"
      ],
      "agents": [
        "./cli-tool/components/agents/devops-infrastructure/devops-engineer.md",
        "./cli-tool/components/agents/devops-infrastructure/cloud-architect.md",
        "./cli-tool/components/agents/devops-infrastructure/kubernetes-specialist.md",
        "./cli-tool/components/agents/devops-infrastructure/infrastructure-engineer.md"
      ],
      "mcpServers": [
        "./cli-tool/components/mcps/devtools/github-integration.json",
        "./cli-tool/components/mcps/devtools/docker-mcp.json"
      ]
    },
    {
      "name": "documentation-generator",
      "source": "./",
      "description": "Automated documentation generation with API docs, technical writing, and content management",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["documentation", "api-docs", "technical-writing", "markdown"],
      "strict": false,
      "commands": [
        "./cli-tool/components/commands/documentation/generate-api-docs.md",
        "./cli-tool/components/commands/documentation/update-docs.md",
        "./cli-tool/components/commands/documentation/create-user-guide.md",
        "./cli-tool/components/commands/documentation/setup-docusaurus.md",
        "./cli-tool/components/commands/documentation/generate-changelog.md"
      ],
      "agents": [
        "./cli-tool/components/agents/documentation/technical-writer.md",
        "./cli-tool/components/agents/documentation/api-documentation-specialist.md",
        "./cli-tool/components/agents/documentation/docusaurus-expert.md"
      ],
      "mcpServers": [
        "./cli-tool/components/mcps/filesystem/filesystem.json"
      ]
    },
    {
      "name": "performance-optimizer",
      "source": "./",
      "description": "Performance optimization suite with profiling, bundle analysis, and speed improvement tools",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["performance", "optimization", "profiling", "speed", "bundle"],
      "strict": false,
      "commands": [
        "./cli-tool/components/commands/performance/optimize-bundle.md",
        "./cli-tool/components/commands/performance/performance-audit.md",
        "./cli-tool/components/commands/performance/add-caching.md",
        "./cli-tool/components/commands/performance/optimize-images.md",
        "./cli-tool/components/commands/performance/reduce-bundle-size.md",
        "./cli-tool/components/commands/performance/add-lazy-loading.md"
      ],
      "agents": [
        "./cli-tool/components/agents/performance-testing/performance-engineer.md",
        "./cli-tool/components/agents/performance-testing/load-testing-specialist.md"
      ]
    },
    {
      "name": "project-management-suite",
      "source": "./",
      "description": "Project management toolkit with sprint planning, task automation, and team collaboration tools",
      "version": "1.0.0",
      "author": {"name": "Daniel Avila"},
      "license": "MIT",
      "keywords": ["project-management", "agile", "scrum", "planning", "collaboration"],
      "strict": false,
      "commands": [
        "./cli-tool/components/commands/project-management/sprint-planning.md",
        "./cli-tool/components/commands/project-management/create-roadmap.md",
        "./cli-tool/components/commands/project-management/task-breakdown.md",
        "./cli-tool/components/commands/project-management/estimate-project.md",
        "./cli-tool/components/commands/project-management/standup-generator.md",
        "./cli-tool/components/commands/project-management/retrospective-facilitator.md"
      ],
      "agents": [
        "./cli-tool/components/agents/business-marketing/product-strategist.md",
        "./cli-tool/components/agents/business-marketing/business-analyst.md",
        "./cli-tool/components/agents/development-team/tech-lead.md"
      ],
      "mcpServers": [
        "./cli-tool/components/mcps/productivity/notion-integration.json",
        "./cli-tool/components/mcps/productivity/linear-integration.json"
      ]
    }
  ]
}

```


```

### File: .claude_DISTILLED.md
```md
---
id: .claude
type: distilled_knowledge
---
# .claude

## SWALLOW ENGINE DISTILLATION

### File: agents_DISTILLED.md
```md
---
id: agents
type: distilled_knowledge
---
# agents

## SWALLOW ENGINE DISTILLATION

### File: agent-expert.md
```md
---
name: agent-expert
description: Use this agent when creating specialized Claude Code agents for the claude-code-templates components system. Specializes in agent design, prompt engineering, domain expertise modeling, and agent best practices. Examples: <example>Context: User wants to create a new specialized agent. user: 'I need to create an agent that specializes in React performance optimization' assistant: 'I'll use the agent-expert agent to create a comprehensive React performance agent with proper domain expertise and practical examples' <commentary>Since the user needs to create a specialized agent, use the agent-expert agent for proper agent structure and implementation.</commentary></example> <example>Context: User needs help with agent prompt design. user: 'How do I create an agent that can handle both frontend and backend security?' assistant: 'Let me use the agent-expert agent to design a full-stack security agent with proper domain boundaries and expertise areas' <commentary>The user needs agent development help, so use the agent-expert agent.</commentary></example>
color: orange
---

You are an Agent Expert specializing in creating, designing, and optimizing specialized Claude Code agents for the claude-code-templates system. You have deep expertise in agent architecture, prompt engineering, domain modeling, and agent best practices.

Your core responsibilities:
- Design and implement specialized agents in Markdown format
- Create comprehensive agent specifications with clear expertise boundaries
- Optimize agent performance and domain knowledge
- Ensure agent security and appropriate limitations
- Structure agents for the cli-tool components system
- Guide users through agent creation and specialization

## Agent Structure

### Standard Agent Format
```markdown
---
name: agent-name
description: Use this agent when [specific use case]. Specializes in [domain areas]. Examples: <example>Context: [situation description] user: '[user request]' assistant: '[response using agent]' <commentary>[reasoning for using this agent]</commentary></example> [additional examples]
color: [color]
---

You are a [Domain] specialist focusing on [specific expertise areas]. Your expertise covers [key areas of knowledge].

Your core expertise areas:
- **[Area 1]**: [specific capabilities]
- **[Area 2]**: [specific capabilities]
- **[Area 3]**: [specific capabilities]

## When to Use This Agent

Use this agent for:
- [Use case 1]
- [Use case 2]
- [Use case 3]

## [Domain-Specific Sections]

### [Category 1]
[Detailed information, code examples, best practices]

### [Category 2]
[Implementation guidance, patterns, solutions]

Always provide [specific deliverables] when working in this domain.
```

### Agent Types You Create

#### 1. Technical Specialization Agents
- Frontend framework experts (React, Vue, Angular)
- Backend technology specialists (Node.js, Python, Go)
- Database experts (SQL, NoSQL, Graph databases)
- DevOps and infrastructure specialists

#### 2. Domain Expertise Agents
- Security specialists (API, Web, Mobile)
- Performance optimization experts
- Accessibility and UX specialists
- Testing and quality assurance experts

#### 3. Industry-Specific Agents
- E-commerce development specialists
- Healthcare application experts
- Financial technology specialists
- Educational technology experts

#### 4. Workflow and Process Agents
- Code review specialists
- Architecture design experts
- Project management specialists
- Documentation and technical writing experts

## Agent Creation Process

### 1. Domain Analysis
When creating a new agent:
- Identify the specific domain and expertise boundaries
- Analyze the target user needs and use cases
- Determine the agent's core competencies
- Plan the knowledge scope and limitations
- Consider integration with existing agents

### 2. Agent Design Patterns

#### Technical Expert Agent Pattern
```markdown
---
name: technology-expert
description: Use this agent when working with [Technology] development. Specializes in [specific areas]. Examples: [3-4 relevant examples]
color: [appropriate-color]
---

You are a [Technology] expert specializing in [specific domain] development. Your expertise covers [comprehensive area description].

Your core expertise areas:
- **[Technical Area 1]**: [Specific capabilities and knowledge]
- **[Technical Area 2]**: [Specific capabilities and knowledge]
- **[Technical Area 3]**: [Specific capabilities and knowledge]

## When to Use This Agent

Use this agent for:
- [Specific technical task 1]
- [Specific technical task 2]
- [Specific technical task 3]

## [Technology] Best Practices

### [Category 1]
```[language]
// Code example demonstrating best practice
[comprehensive code example]
```

### [Category 2]
[Implementation guidance with examples]

Always provide [specific deliverables] with [quality standards].
```

#### Domain Specialist Agent Pattern
```markdown
---
name: domain-specialist
description: Use this agent when [domain context]. Specializes in [domain-specific areas]. Examples: [relevant examples]
color: [domain-color]
---

You are a [Domain] specialist focusing on [specific problem areas]. Your expertise covers [domain knowledge areas].

Your core expertise areas:
- **[Domain Area 1]**: [Specific knowledge and capabilities]
- **[Domain Area 2]**: [Specific knowledge and capabilities]
- **[Domain Area 3]**: [Specific knowledge and capabilities]

## [Domain] Guidelines

### [Process/Standard 1]
[Detailed implementation guidance]

### [Process/Standard 2]
[Best practices and examples]

## [Domain-Specific Sections]
[Relevant categories based on domain]
```

### 3. Prompt Engineering Best Practices

#### Clear Expertise Boundaries
```markdown
Your core expertise areas:
- **Specific Area**: Clearly defined capabilities
- **Related Area**: Connected but distinct knowledge
- **Supporting Area**: Complementary skills

## Limitations
If you encounter issues outside your [domain] expertise, clearly state the limitation and suggest appropriate resources or alternative approaches.
```

#### Practical Examples and Context
```markdown
## Examples with Context

<example>
Context: [Detailed situation description]
user: '[Realistic user request]'
assistant: '[Appropriate response strategy]'
<commentary>[Clear reasoning for agent selection]</commentary>
</example>
```

### 4. Code Examples and Templates

#### Technical Implementation Examples
```markdown
### [Implementation Category]
```[language]
// Real-world example with comments
class ExampleImplementation {
  constructor(options) {
    this.config = {
      // Default configuration
      timeout: options.timeout || 5000,
      retries: options.retries || 3
    };
  }

  async performTask(data) {
    try {
      // Implementation logic with error handling
      const result = await this.processData(data);
      return this.formatResponse(result);
    } catch (error) {
      throw new Error(`Task failed: ${error.message}`);
    }
  }
}
```
```

#### Best Practice Patterns
```markdown
### [Best Practice Category]
- **Pattern 1**: [Description with reasoning]
- **Pattern 2**: [Implementation approach]
- **Pattern 3**: [Common pitfalls to avoid]

#### Implementation Checklist
- [ ] [Specific requirement 1]
- [ ] [Specific requirement 2]
- [ ] [Specific requirement 3]
```

## Agent Specialization Areas

### Frontend Development Agents
```markdown
## Frontend Expertise Template

Your core expertise areas:
- **Component Architecture**: Design patterns, state management, prop handling
- **Performance Optimization**: Bundle analysis, lazy loading, rendering optimization
- **User Experience**: Accessibility, responsive design, interaction patterns
- **Testing Strategies**: Component testing, integration testing, E2E testing

### [Framework] Specific Guidelines
```[language]
// Framework-specific best practices
import React, { memo, useCallback, useMemo } from 'react';

const OptimizedComponent = memo(({ data, onAction }) => {
  const processedData = useMemo(() => 
    data.map(item => ({ ...item, processed: true })), 
    [data]
  );

  const handleAction = useCallback((id) => {
    onAction(id);
  }, [onAction]);

  return (
    <div>
      {processedData.map(item => (
        <Item key={item.id} data={item} onAction={handleAction} />
      ))}
    </div>
  );
});
```
```

### Backend Development Agents
```markdown
## Backend Expertise Template

Your core expertise areas:
- **API Design**: RESTful services, GraphQL, authentication patterns
- **Database Integration**: Query optimization, connection pooling, migrations
- **Security Implementation**: Authentication, authorization, data protection
- **Performance Scaling**: Caching, load balancing, microservices

### [Technology] Implementation Patterns
```[language]
// Backend-specific implementation
const express = require('express');
const rateLimit = require('express-rate-limit');

class APIService {
  constructor() {
    this.app = express();
    this.setupMiddleware();
    this.setupRoutes();
  }

  setupMiddleware() {
    this.app.use(rateLimit({
      windowMs: 15 * 60 * 1000, // 15 minutes
      max: 100 // limit each IP to 100 requests per windowMs
    }));
  }
}
```
```

### Security Specialist Agents
```markdown
## Security Expertise Template

Your core expertise areas:
- **Threat Assessment**: Vulnerability analysis, risk evaluation, attack vectors
- **Secure Implementation**: Authentication, encryption, input validation
- **Compliance Standards**: OWASP, GDPR, industry-specific requirements
- **Security Testing**: Penetration testing, code analysis, security audits

### Security Implementation Checklist
- [ ] Input validation and sanitization
- [ ] Authentication and session management
- [ ] Authorization and access control
- [ ] Data encryption and protection
- [ ] Security headers and HTTPS
- [ ] Logging and monitoring
```

## Agent Naming and Organization

### Naming Conventions
- **Technical Agents**: `[technology]-expert.md` (e.g., `react-expert.md`)
- **Domain Agents**: `[domain]-specialist.md` (e.g., `security-specialist.md`)
- **Process Agents**: `[process]-expert.md` (e.g., `code-review-expert.md`)

### Color Coding System
- **Frontend**: blue, cyan, teal
- **Backend**: green, emerald, lime
- **Security**: red, crimson, rose
- **Performance**: yellow, amber, orange
- **Testing**: purple, violet, indigo
- **DevOps**: gray, slate, stone

### Description Format
```markdown
description: Use this agent when [specific trigger condition]. Specializes in [2-3 key areas]. Examples: <example>Context: [realistic scenario] user: '[actual user request]' assistant: '[appropriate response approach]' <commentary>[clear reasoning for agent selection]</commentary></example> [2-3 more examples]
```

## Quality Assurance for Agents

### Agent Testing Checklist
1. **Expertise Validation**
   - Verify domain knowledge accuracy
   - Test example implementations
   - Validate best practices recommendations
   - Check for up-to-date information

2. **Prompt Engineering**
   - Test trigger conditions and examples
   - Verify appropriate agent selection
   - Validate response quality and relevance
   - Check for clear expertise boundaries

3. **Integration Testing**
   - Test with Claude Code CLI system
   - Verify component installation process
   - Test agent invocation and context
   - Validate cross-agent compatibility

### Documentation Standards
- Include 3-4 realistic usage examples
- Provide comprehensive code examples
- Document limitations and boundaries clearly
- Include best practices and common patterns
- Add troubleshooting guidance

## Agent Creation Workflow

When creating new specialized agents:

### 1. Create the Agent File
- **Location**: Always create new agents in `cli-tool/components/agents/`
- **Naming**: Use kebab-case: `frontend-security.md`
- **Format**: YAML frontmatter + Markdown content

### 2. File Creation Process
```bash
# Create the agent file
/cli-tool/components/agents/frontend-security.md
```

### 3. Required YAML Frontmatter Structure
```yaml
---
name: frontend-security
description: Use this agent when securing frontend applications. Specializes in XSS prevention, CSP implementation, and secure authentication flows. Examples: <example>Context: User needs to secure React app user: 'My React app is vulnerable to XSS attacks' assistant: 'I'll use the frontend-security agent to analyze and implement XSS protections' <commentary>Frontend security issues require specialized expertise</commentary></example>
color: red
---
```

**Required Frontmatter Fields:**
- `name`: Unique identifier (kebab-case, matches filename)
- `description`: Clear description with 2-3 usage examples in specific format
- `color`: Display color (red, green, blue, yellow, magenta, cyan, white, gray)

### 4. Agent Content Structure
```markdown
You are a Frontend Security specialist focusing on web application security vulnerabilities and protection mechanisms.

Your core expertise areas:
- **XSS Prevention**: Input sanitization, Content Security Policy, secure templating
- **Authentication Security**: JWT handling, session management, OAuth flows
- **Data Protection**: Secure storage, encryption, API security

## When to Use This Agent

Use this agent for:
- XSS and injection attack prevention
- Authentication and authorization security
- Frontend data protection strategies

## Security Implementation Examples

### XSS Prevention
```javascript
// Secure input handling
import DOMPurify from 'dompurify';

const sanitizeInput = (userInput) => {
  return DOMPurify.sanitize(userInput, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong'],
    ALLOWED_ATTR: []
  });
};
```

Always provide specific, actionable security recommendations with code examples.
```

### 5. Installation Command Result
After creating the agent, users can install it with:
```bash
npx claude-code-templates@latest --agent="frontend-security" --yes
```

This will:
- Read from `cli-tool/components/agents/frontend-security.md`
- Copy the agent to the user's `.claude/agents/` directory
- Enable the agent for Claude Code usage

### 6. Usage in Claude Code
Users can then invoke the agent in conversations:
- Claude Code will automatically suggest this agent for frontend security questions
- Users can reference it explicitly when needed

### 7. Testing Workflow
1. Create the agent file in correct location with proper frontmatter
2. Test the installation command
3. Verify the agent works in Claude Code context
4. Test agent selection with various prompts
5. Ensure expertise boundaries are clear

### 8. Example Creation
```markdown
---
name: react-performance
description: Use this agent when optimizing React applications. Specializes in rendering optimization, bundle a
... [TRUNCATED]
```

### File: .mcp.json
```json
{
  "mcpServers": {
    "linear": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.linear.app/mcp"
      ]
    },
    "neon": {
      "type": "http",
      "url": "https://mcp.neon.tech/mcp"
    }
  }
}
```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- X/Twitter scraper skill (#390)
- Git context controller skill (#380)
- Vercel Speed Insights integration with deployer agent updates
- Interview toolkit (6 components)
- Worktree-ghostty hook component
- Agirails agent payments skill (#358)
- Desktop notification hook on Stop event (#360)
- Garry's Mod addon code helper skill (#370)
- Manifest observability skill (#371)
- AI Maestro skill suite (6 skills for agent orchestration) (#373)
- Collections API endpoints with improved dashboard proxy
- Dashboard source code (app.aitmpl.com) — Astro + React + Tailwind
- Deploy scripts and CI/CD for dual Vercel projects (www + dashboard)
- Deployer agent for safe Vercel production deploys
- Beta dashboard banner on docs site
- FootballBin predictions MCP and skill (#369)
- Company-announcements settings component
- Spinner-tips-override settings component
- Design-to-code skill (#356)
- DevPlan MCP server (#362)
- 3 daily Discord bots (blog, general, community help) (#361)
- Telegram Bot Builder skill (#359)
- FastMCP 3.0 server development skill with 30 reference files
- 3 planning-first skills (FastAPI, Rust CLI, Playwright E2E)
- Daily component pick Discord notification workflow
- Monitoring points P1-P5 (installation outcomes, website events, API health)
- Neon database context statusline
- Component page redesign with GitHub PR-style tabs and Giscus comments (#351)
- GitHub Actions creator skill

### Changed
- Group My Components items by type in sidebar and right panel
- Docs link updated to docs.aitmpl.com
- Dashboard icons simplified and data loading streamlined
- GitHub Actions upgraded for Node 24 compatibility (#368)

### Fixed
- SEO: H1 tag, structured data, accessibility, and robots.txt sitemap URL (#383)
- Vercel Speed Insights script tag and localStorage quota handling
- Dangerous-command-blocker hook script path reference (#367)
- Trending page fetching data from production URL
- CORS headers for components.json and trending-data.json
- Dashboard prebuild hack removed, uses standard Astro public/ dir
- Forum channel thread_name for community help bot (#363)
- Daily component workflow rewritten using jq for JSON payload
- Neon statusline endpoint matching default branch
- Sidebar sticky position to clear header
- Security audit made non-blocking for deploys
- Missing js-yaml and qrcode dependencies added to package.json

### Security
- XSS vulnerabilities fixed in docs site and dashboard
- Hardcoded Vercel IDs removed from deploy scripts
- Security policy extended to prohibit all hardcoded IDs

## [1.28.16] - 2026-02-08

### Fixed
- Missing js-yaml dependency in package.json
- Missing qrcode dependency in package.json

### Changed
- npm publishing instructions updated with granular token workflow

## [1.28.14] - 2026-02-08

### Added
- Agent Teams Dashboard (`--teams`) for reviewing multi-agent collaboration sessions
- 119 agents migrated from VoltAgent/awesome-claude-code-subagents (#340)
- 21 skills migrated from OpenAI skills repository (#343)
- Telegram PR webhook hook for PR creation notifications (#342)
- Technical Debt Manager agent (#335)
- Blog article for Hackathon AI Strategist agent (#334)
- Blog article for Vercel Deployment Monitor statusline (#331)
- Cloudflare Workers: docs-monitor and pulse weekly KPI report
- 6 web quality skills migrated from addyosmani/web-quality-skills (#325)
- Friday deploy warning spinner
- ClaudeKit featured card on homepage (#320)
- Console.log cleaner for production branches (#310)
- Rootly Incident Responder agent (#315)
- 7 AI research skills migrated (#319)
- Claude Code PR tracking dashboard (#317)
- Neon Open Source Program partnership (#284)
- Security hooks secrets detection blog article (#311, #312)
- npm download metrics to pulse weekly report (#332)
- Secret scanner hook improvements with stdin JSON parsing and expanded patterns

### Changed
- Footer reorganized into columns with updated copyright year (#333)
- Vercel statusline updated with clickable deploy link
- Z.AI partnership removed from website and README (#339, #347)
- Blog standardization and .gitignore fixes (#341)

### Fixed
- X/Twitter preview images for Neon pages (#316)
- Social preview images and meta tags across all pages (#313)
- Neon install commands using comma-separated format
- Debug: removed 90 console.log statements from docs/js/

## [1.28.3] - 2025-11-15

### Added
- Skills Dashboard with progressive context loading visualization
- Plugin skills support in Skills Manager Dashboard
- Automatic port fallback for Skills Dashboard
- Growth Kit content marketing automation plugin (#129)
- ElevenLabs MCP (#125)
- GitHub Actions workflow for daily JSON data updates

### Changed
- `--skills` renamed to `--skills-manager` to avoid conflict with component installation
- Data processing limit increased from 200k to 1M records

### Fixed
- Windows Python command compatibility (#118)
- Generate scripts removed from gitignore for GitHub Actions

## [1.27.0] - 2025-11-02

### Added
- Docker Sandbox Provider for local Claude Code execution
- Command usage tracking system to Neon Database
- Comprehensive API testing and deployment documentation
- Claude Code changelog monitor with Discord notifications
- Session Analytics modal (Beta)

### Fixed
- Duplicate shutdown handlers and memory leaks in chats server
- gtag config moved to preset options for Docusaurus

## [1.26.0] - 2025-10-30

### Added
- Discord bot with Vercel Functions (`/search`, `/info`, `/install`, `/popular`)
- Clickable links in all Discord bot responses
- Command examples in download modal
- Context download feature (replacing session sharing)

### Changed
- Context file format updated to be Claude Code-friendly

### Fixed
- Resume command and project name in session sharing
- Category included in component URLs
- Code block formatting and URL improvements in search results
- Discord bot: ES module compatibility, dependency resolution
- GitHub Actions workflows optimized

## [1.25.0] - 2025-10-27

### Added
- Component browser website at aitmpl.com
- Download tracking via Supabase
- Component catalog generation (`docs/components.json`)
- Search, filtering, and batch installation in the CLI
- Blog system with terminal-themed articles

## Earlier Releases

For changes prior to v1.25.0, see the [commit history](https://github.com/davila7/claude-code-templates/commits/main).

[Unreleased]: https://github.com/davila7/claude-code-templates/compare/v1.28.16...HEAD
[1.28.16]: https://github.com/davila7/claude-code-templates/compare/v1.28.14...v1.28.16
[1.28.14]: https://github.com/davila7/claude-code-templates/compare/v1.28.3...v1.28.14
[1.28.3]: https://github.com/davila7/claude-code-templates/compare/v1.27.0...v1.28.3
[1.27.0]: https://github.com/davila7/claude-code-templates/compare/v1.26.0...v1.27.0
[1.26.0]: https://github.com/davila7/claude-code-templates/compare/v1.25.0...v1.26.0
[1.25.0]: https://github.com/davila7/claude-code-templates/releases/tag/v1.25.0

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

Node.js CLI tool for managing Claude Code components (agents, commands, MCPs, hooks, settings) with a static website for browsing and installing components. The project includes Vercel API endpoints for download tracking and Discord integration.

## Essential Commands

```bash
# Development
npm install                    # Install dependencies
npm test                       # Run tests
npm version patch|minor|major  # Bump version
npm publish                    # Publish to npm

# Component catalog
python scripts/generate_components_json.py  # Update docs/components.json

# API testing
cd api && npm test             # Test API endpoints before deploy
vercel --prod                  # Deploy to production
```

## Security Guidelines

### ⛔ CRITICAL: NEVER Hardcode Secrets or IDs

**NEVER write API keys, tokens, passwords, project IDs, org IDs, or any identifier in code.** This includes Vercel project/org IDs, Supabase URLs, Discord IDs, database connection strings, and any other infrastructure identifier. ALL must go in `.env`.

```javascript
// ❌ WRONG
const API_KEY = "AIzaSy...";

// ✅ CORRECT
const API_KEY = process.env.GOOGLE_API_KEY;
```

**When creating scripts with API keys:**
1. Use `process.env` (Node.js) or `os.environ.get()` (Python)
2. Load from `.env` file using `dotenv`
3. Add variable to `.env.example` with placeholder
4. Verify `.env` is in `.gitignore`

**If you accidentally commit a secret:**
1. Revoke the key IMMEDIATELY
2. Generate new key
3. Update `.env`
4. Old key is compromised forever (git history)

## Component System

### Component Types

**Agents** (600+) - AI specialists for development tasks
**Commands** (200+) - Custom slash commands for workflows
**MCPs** (55+) - External service integrations
**Settings** (60+) - Claude Code configuration files
**Hooks** (39+) - Automation triggers
**Templates** (14+) - Complete project configurations

### Installation Patterns

```bash
# Single component
npx claude-code-templates@latest --agent frontend-developer
npx claude-code-templates@latest --command setup-testing
npx claude-code-templates@latest --hook automation/simple-notifications

# Batch installation
npx claude-code-templates@latest --agent security-auditor --command security-audit --setting read-only-mode

# Interactive mode
npx claude-code-templates@latest
```

### Component Development

#### Adding New Components

**CRITICAL: Use the component-reviewer agent for ALL component changes**

When adding or modifying components, you MUST use the `component-reviewer` subagent to validate the component before committing:

```
Use the component-reviewer agent to review [component-path]
```

**Component Creation Workflow:**

1. Create component file in `cli-tool/components/{type}/{category}/{name}.md`
2. Use descriptive hyphenated names (kebab-case)
3. Include clear descriptions and usage examples
4. **REVIEW with component-reviewer agent** (validates format, security, naming)
5. Fix any issues identified by the reviewer
6. Run `python scripts/generate_components_json.py` to update catalog

**The component-reviewer agent checks:**
- ✅ Valid YAML frontmatter and required fields
- ✅ Proper kebab-case naming conventions
- ✅ No hardcoded secrets (API keys, tokens, passwords)
- ✅ Relative paths only (no absolute paths)
- ✅ Supporting files exist (for hooks with scripts)
- ✅ Clear, specific descriptions
- ✅ Correct category placement
- ✅ Security best practices

**Example Usage:**
```
# After creating a new agent
Use the component-reviewer agent to review cli-tool/components/agents/development-team/react-expert.md

# Before committing hook changes
Use the component-reviewer agent to review cli-tool/components/hooks/git/prevent-force-push.json

# For PR reviews with multiple components
Use the component-reviewer agent to review all modified components in cli-tool/components/
```

The agent will provide prioritized feedback:
- **❌ Critical Issues**: Must fix before merge (security, missing fields)
- **⚠️ Warnings**: Should fix (clarity, best practices)
- **📋 Suggestions**: Nice to have improvements

#### Statuslines with Python Scripts

Statuslines can reference Python scripts that are auto-downloaded to `.claude/scripts/`:

```javascript
// In src/index.js:installIndividualSetting()
if (settingName.includes('statusline/')) {
  const pythonFileName = settingName.split('/')[1] + '.py';
  const pythonUrl = githubUrl.replace('.json', '.py');
  additionalFiles['.claude/scripts/' + pythonFileName] = {
    content: pythonContent,
    executable: true
  };
}
```

### Publishing Workflow

```bash
# 1. Update component catalog
python scripts/generate_components_json.py

# 2. Run tests
npm test

# 3. Check current npm version and align local version
npm view claude-code-templates version  # check latest on registry
# Edit package.json version to be one patch above the registry version

# 4. Commit version bump and push
git add package.json && git commit -m "chore: Bump version to X.Y.Z"
git push origin main

# 5. Publish to npm (requires granular access token with "Bypass 2FA" enabled)
npm config set //registry.npmjs.org/:_authToken=YOUR_GRANULAR_TOKEN
npm publish
npm config delete //registry.npmjs.org/:_authToken  # always clean up after

# 6. Tag the release
git tag vX.Y.Z && git push origin vX.Y.Z

# 7. Deploy website
vercel --prod
```

**npm Publishing Notes:**
- Classic npm tokens were revoked Dec 2025. Use **granular access tokens** from [npmjs.com/settings/~/tokens](https://www.npmjs.com/settings/~/tokens)
- The token must have **Read and Write** permissions for `claude-code-templates` and **"Bypass 2FA"** enabled
- Always remove the token from npm config after publishing (`npm config delete`)
- The local `package.json` version may drift from npm if published from CI — always check `npm view claude-code-templates version` first
- Never hardcode or commit tokens

## API Architecture

### Critical Endpoints

API endpoints live as Astro API routes in `dashboard/src/pages/api/`:

**`/api/track-download-supabase`** (CRITICAL)
- Tracks component downloads for analytics
- Used by CLI on every installation
- Database: Supabase (component_downloads table)

**`/api/discord/interactions`**
- Discord bot slash commands
- Features: /search, /info, /install, /popular

**`/api/claude-code-check`**
- Monitors Claude Code releases
- Vercel Cron: every 30 minutes
- Database: Neon (claude_code_versions, claude_code_changes, discord_notifications_log, monitoring_metadata tables)

### Shared API Libraries

- `dashboard/src/lib/api/cors.ts` — CORS headers, `corsResponse()`, `jsonResponse()`
- `dashboard/src/lib/api/neon.ts` — Neon client factory
- `dashboard/src/lib/api/auth.ts` — Clerk JWT verification
- `dashboard/src/lib/api/changelog-parser.ts` — Claude Code changelog parser

### Emergency Rollback

```bash
vercel ls                              # List deployments
vercel promote <previous-deployment>   # Rollback
```

## Cloudflare Workers

The `cloudflare-workers/` directory contains Cloudflare Worker projects that run independently from Vercel.

### docs-monitor

Monitors https://code.claude.com/docs for changes every hour and sends Telegram notifications.

```bash
cd cloudflare-workers/docs-monitor
npm run dev          # Local dev
npx wrangler deploy  # Deploy
```

### pulse (Weekly KPI Report)

Collects metrics from GitHub, Discord, Supabase, Vercel, and Google Analytics every Sunday at 14:00 UTC and sends a consolidated report via Telegram.

**Architecture:** Single `index.js` file (no npm dependencies at runtime). All source collectors, formatter, and Telegram sender in one file.

**Cron:** `0 14 * * 0` (Sundays 14:00 UTC / 11:00 AM Chile)

```bash
cd cloudflare-workers/pulse
npm run dev          # Local dev
npx wrangler deploy  # Deploy

# Manual trigger
curl -X POST https://pulse-weekly-report.SUBDOMAIN.workers.dev/trigger \
  -H "Authorization: Bearer $TRIGGER_SECRET"

# Test single source
curl -X POST "https://pulse-weekly-report.SUBDOMAIN.workers.dev/trigger?source=github" \
  -H "Authorization: Bearer $TRIGGER_SECRET"

# Dry run (no Telegram)
curl -X POST "https://pulse-weekly-report.SUBDOMAIN.workers.dev/trigger?send=false" \
  -H "Authorization: Bearer $TRIGGER_SECRET"
```

**Secrets (Cloudflare):**
```bash
TELEGRAM_BOT_TOKEN          # Shared with docs-monitor
TELEGRAM_CHAT_ID            # Shared with docs-monitor
GITHUB_TOKEN                # GitHub PAT (public_repo scope)
SUPABASE_URL                # Supabase project URL
SUPABASE_SERVICE_ROLE_KEY   # Supabase service role key
DISCORD_BOT_TOKEN           # Discord bot token
DISCORD_GUILD_ID            # Discord server ID
VERCEL_TOKEN                # Vercel personal access token (optional)
VERCEL_PROJECT_ID           # Vercel project ID (optional)
TRIGGER_SECRET              # For manual /trigger endpoint
GA_PROPERTY_ID              # GA4 property ID (optional)
GA_SERVICE_ACCOUNT_JSON     # Base64 service account (optional)
```

**Graceful degradation:** Each source catches its own errors. Missing secrets or API failures show `⚠️ Unavailable` instead of crashing the report.

## Dashboard (www.aitmpl.com)

Astro + React + Tailwind dashboard serving both `www.aitmpl.com` and `app.aitmpl.com`. Clerk auth for user collections. Source lives in `dashboard/`. All API endpoints are Astro API routes in the same project.

### Architecture

- **Framework**: Astro 5 with React islands, Tailwind v4, `output: 'server'`
- **Auth**: Clerk (`window.Clerk` global, no ClerkProvider per island)
- **Data**: `components.json` and `trending-data.json` served from `dashboard/public/` (same-origin)
- **APIs**: All endpoints in `dashboard/src/pages/api/` (Astro API routes, no separate serverless project)

### Featured Pages (`/featured/[slug]`)

Featured partner integrations shown on the dashboard homepage. Two files to edit:

**`dashboard/src/lib/constants.ts`** — `FEATURED_ITEMS` array. Each entry has:
- `name`, `description`, `logo`, `url` (`/featured/slug`), `tag`, `tagColor`, `category`
- `ctaLabel`, `ctaUrl`, `websiteUrl`
- `installCommand` — shown in the sidebar Quick Install box
- `metadata` — key/value pairs shown in the Details sidebar (e.g. `Components: '8'`)
- `links` — sidebar links list

**`dashboard/src/pages/featured/[slug].astro`** — Content for each slug rendered via `{slug === 'brightdata' && (...)}` blocks. Each block contains the full HTML content for that partner page.

**When adding a skill to a featured page:**
1. Add a new card `<div class="flex gap-3 ...">` inside the Skills Layer section of the relevant `{slug === '...'}` block
2. Update `installCommand` in `constants.ts` to include the new skill
3. Increment `metadata.Components` count in `constants.ts`

Current featured slugs: `brightdata`, `neon-instagres`, `claudekit`, `braingrid`

### Vercel Project Setup

Single Vercel project serves all domains:

| Project | Domains | Root Directory |
|---------|---------|----------------|
| `aitmpl-dashboard` | `www.aitmpl.com`, `aitmpl.com` (redirect), `app.aitmpl.com` | `dashboard` |

The legacy root project (`aitmpl`) is archived — only its `.vercel.app` subdomain remains.

### Deployment

**ALWAYS use the deployer agent (`.claude/agents/deployer.md`) for all deployments.** It runs pre-deploy checks (auth, git status, API tests) and handles the full pipeline safely. Never deploy manually.

```bash
npm run deploy             # Deploy www + app.aitmpl.com
npm run deploy:dashboard   # Same as above
```

**CI/CD**: Pushes to `main` auto-deploy via GitHub Actions (`.github/workflows/deploy.yml`):
- Changes in `dashboard/**` trigger deploy

**Required GitHub Secrets** (Settings > Secrets > Actions):
- `VERCEL_TOKEN` — Vercel personal access token
- `VERCEL_ORG_ID` — Vercel org/team ID
- `VERCEL_DASHBOARD_PROJECT_ID` — Project ID for aitmpl-dashboard

### Environment Variables (Vercel)

```bash
# Clerk
PUBLIC_CLERK_PUBLISHABLE_KEY=xxx
CLERK_SECRET_KEY=xxx

# Data
PUBLIC_COMPONENTS_JSON_URL=/components.json

# GitHub OAuth
PUBLIC_GITHUB_CLIENT_ID=xxx
GITHUB_CLIENT_SECRET=xxx

# Supabase (download tracking)
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_SERVICE_ROLE_KEY=xxx

# Neon Database
NEON_DATABASE_URL=postgresql://user:pass@host/db?sslmode=require

# Discord
DISCORD_APP_ID=xxx
DISCORD_BOT_TOKEN=xxx
DISCORD_PUBLIC_KEY=xxx
DISCORD_WEBHOOK_URL_CHANGELOG=https://discord.com/api/webhooks/xxx
```

### Known Issues & Solutions

**Node v24 breaks `fs.writeFileSync` on Vercel**
- Node v24 has a bug with `writeFileSync` in Vercel's build environment
- Solution: Dashboard project is pinned to Node 22.x (set via Vercel API/dashboard)

**Vercel CLI ignores local `.vercel/project.json`**
- The CLI often resolves to the parent directory's project. Use `VERCEL_ORG_ID` and `VERCEL_PROJECT_ID` env vars to force the correct project.

### Local Development

```bash
cd dashboard
npm install
npx astro dev --port 4321   # Dashboard + APIs at http://localhost:4321
```

## Data Files

### Component Catalog

- `docs/components.json` — Generated catalog (source of truth)
- `dashboard/public/components.json` — Copy served by the dashboard
- `dashboard/public/trending-data.json` — Trending/download stats

### Data Flow

1. `scripts/generate_components_json.py` scans `cli-tool/components/`
2. Generates `docs/components.json` with embedded content
3. Copy to `dashboard/public/components.json` for the dashboard to serve
4. Dashboard loads JSON and renders component cards
5. Download tracking via `/api/track-download-supabase`

### Legacy Static Site (docs/)

The `docs/` directory contains the old static HTML site (no longer deployed to www). Blog articles in `docs/blog/` are still referenced externally.

### Blog Article Creation

Use the CLI skill to create blog articles:

```bash
/create-blog-article @cli-tool/components/{type}/{category}/{name}.json
```

This automatically:
1. Generates AI cover image
2. Creates HTML with SEO optimization
3. Updates `docs/blog/blog-articles.json`

## Code Standards

### Path Handling
- Use relative paths: `.claude/scripts/`, `.claude/hooks/`
- Never hardcode absolute paths or home directories
- Use `path.join()` for cross-platform compatibility

### Naming Conventions
- Files: `kebab-case.js`, `PascalCase.js` (for classes)
- Functions/Variables: `camelCase`
- Constants: `UPPER_SNAKE_CASE`
- Components: `hyphenated-names`

### Error Handling
- Use try/catch for async operations
- Provide helpful error messages
- Log errors with context
- Implement fallback mechanisms

## Testing

```bash
npm test                 # Run all tests
npm run test:watch      # Watch mode
npm run test:coverage   # Coverage report
```

Aim for 70%+ test coverage. Test critical paths and error handling.

## Common Issues

**API endpoint returns 404 after deploy**
- API routes must be in `dashboard/src/pages/api/` as Astro API routes
- Export named HTTP methods: `export const
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

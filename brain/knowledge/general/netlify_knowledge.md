---
id: netlify-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:11.363264
---

# KNOWLEDGE EXTRACT: netlify
> **Extracted on:** 2026-03-30 17:49:10
> **Source:** netlify

---

## File: `context-and-tools.md`
```markdown
# 📦 netlify/context-and-tools [🔖 PENDING/APPROVE]
🔗 https://github.com/netlify/context-and-tools


## Meta
- **Stars:** ⭐ 10 | **Forks:** 🍴 4
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-22
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# Netlify Context and Tools

Public Netlify skills for AI coding agents. Each skill is a focused, factual reference for a Netlify platform primitive — designed to help agents build correctly on Netlify without needing to search docs.

## Skills

| Skill | What it covers |
|---|---|
| [netlify-functions](../bmad_repo/SKILL.md) | Serverless functions — modern syntax, routing, background/scheduled/streaming |
| [netlify-edge-functions](../bmad_repo/SKILL.md) | Edge compute — Deno runtime, middleware, geolocation |
| [netlify-blobs](../bmad_repo/SKILL.md) | Object storage — key-value and binary data |
| [netlify-db](../bmad_repo/SKILL.md) | Managed Postgres (Neon) with Drizzle ORM and migrations |
| [netlify-image-cdn](../bmad_repo/SKILL.md) | Image transformation and optimization via CDN |
| [netlify-forms](../bmad_repo/SKILL.md) | HTML form handling, AJAX submissions, spam filtering |
| [netlify-config](../bmad_repo/SKILL.md) | `netlify.toml` — redirects, headers, build settings, deploy contexts |
| [netlify-cli-and-deploy](../bmad_repo/SKILL.md) | CLI commands, Git vs manual deploys, environment variables |
| [netlify-frameworks](../bmad_repo/SKILL.md) | Framework adapters for Vite, Astro, TanStack, and Next.js |
| [netlify-caching](../bmad_repo/SKILL.md) | CDN cache control, cache tags, purge, stale-while-revalidate |
| [netlify-ai-gateway](../bmad_repo/SKILL.md) | AI Gateway proxy for OpenAI, Anthropic, and Google SDKs |
| [netlify-deploy](../bmad_repo/SKILL.md) | Deployment workflow — auth, site linking, preview/production deploys |

### References

Some skills include `references/` subdirectories with deeper content:

- [User-uploaded images pipeline](skills/netlify-image-cdn/references/user-uploads.md) — composing Functions + Blobs + Image CDN
- [Vite on Netlify](skills/netlify-frameworks/references/vite.md)
- [Astro on Netlify](skills/netlify-frameworks/references/astro.md)
- [TanStack Start on Netlify](skills/netlify-frameworks/references/tanstack.md)
- [Next.js on Netlify](../../../core/security/QUARANTINE/vetted/repos/developer_roadmap/src/data/roadmaps/nextjs/nextjs.md)
- [CLI commands reference](../../../vault/archives/archive_legacy/awesome-copilot/skills/codeql/references/cli-commands.md)
- [Deployment patterns](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/skills/development/netlify-deploy/references/deployment-patterns.md)
- [netlify.toml guide](../../../vault/archives/archive_legacy/claude-code-templates/cli-tool/components/skills/development/netlify-deploy/references/netlify-toml.md)

## Installation

### Claude Code

Add the marketplace and install the plugin:

```
/plugin marketplace add netlify/context-and-tools
/plugin install netlify-skills@netlify-context-and-tools
```

This installs all Netlify skills into Claude Code. The included `skills/CLAUDE.md` acts as a router — it tells the agent which skill to read based on what you're building.

### Cursor

Install from the [Cursor plugin marketplace](https://cursor.com/marketplace):

1. Open Cursor Settings (`Cmd+,` / `Ctrl+,`)
2. Go to **Plugins**
3. Search for **netlify-skills**
4. Click **Ins
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```


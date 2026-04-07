---
id: emdash
type: knowledge
owner: OA_Triage
---
# emdash
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
	"name": "emdash-workspace",
	"private": true,
	"type": "module",
	"version": "1.0.0",
	"description": "Agent-portable reimplementation of WordPress on Astro",
	"scripts": {
		"typecheck": "pnpm run --filter {./packages/**} typecheck",
		"typecheck:demos": "pnpm run --workspace-concurrency=1 --filter {./demos/*} --filter !@emdash-cms/demo-cloudflare typecheck",
		"typecheck:templates": "pnpm run --workspace-concurrency=1 --filter {./templates/*} typecheck",
		"check": "pnpm run typecheck && pnpm run --filter {./packages/*} check",
		"test": "pnpm run --filter {./packages/*} test",
		"test:unit": "pnpm run --filter emdash --filter @emdash-cms/auth --filter @emdash-cms/blocks --filter @emdash-cms/gutenberg-to-portable-text --filter @emdash-cms/marketplace test",
		"test:browser": "pnpm run --filter @emdash-cms/admin test",
		"test:e2e": "playwright test",
		"test:e2e:ui": "playwright test --ui",
		"build": "pnpm run --filter {./packages/**} build",
		"format": "oxfmt --ignore-path .gitignore && prettier --write .",
		"format:check": "oxfmt --ignore-path .gitignore --check && prettier --check .",
		"format:astro": "prettier --write .",
		"lint": "oxlint --type-aware",
		"lint:quick": "oxlint -f json",
		"lint:json": "oxlint --type-aware -f json",
		"lint:fix": "oxlint --type-aware --fix",
		"knip": "knip --no-exit-code --exclude unlisted,unresolved,exports,types,duplicates",
		"new": "create-emdash",
		"screenshots": "node scripts/screenshot-all-templates.mjs"
	},
	"keywords": [],
	"author": "Matt Kane",
	"license": "MIT",
	"devDependencies": {
		"@axe-core/playwright": "^4.11.1",
		"@changesets/changelog-github": "^0.5.2",
		"@changesets/cli": "^2.29.8",
		"@e18e/eslint-plugin": "^0.2.0",
		"@playwright/test": "^1.58.0",
		"@types/node": "catalog:",
		"@typescript/native-preview": "^7.0.0-dev",
		"emdash": "workspace:*",
		"knip": "^5.84.1",
		"oxfmt": "^0.34.0",
		"oxlint": "^1.49.0",
		"oxlint-tsgolint": "^0.15.0",
		"prettier": "^3.8.1",
		"prettier-plugin-astro": "^0.14.1",
		"typescript": "6.0.0-beta"
	},
	"packageManager": "pnpm@10.28.0",
	"pnpm": {
		"onlyBuiltDependencies": [
			"better-sqlite3",
			"esbuild",
			"workerd"
		]
	}
}

```

### File: README.md
```md
# EmDash

A full-stack TypeScript CMS built on [Astro](https://astro.build/) and [Cloudflare](https://www.cloudflare.com/). EmDash takes the ideas that made WordPress dominant -- extensibility, admin UX, a plugin ecosystem -- and rebuilds them on serverless, type-safe foundations. Plugins run in sandboxed Worker isolates, solving the fundamental security problem with WordPress's plugin architecture.

## Get Started

> [!IMPORTANT]
> EmDash depends on Dynamic Workers to run secure sandboxed plugins. Dynamic Workers are currently only available on paid accounts. [Upgrade your account](https://www.cloudflare.com/plans/developer-platform/) (starting at $5/mo) or comment out the `worker_loaders` block of your `wrangler.jsonc` configuration file to disable plugins.

```bash
npm create emdash@latest
```

Or deploy directly to your Cloudflare account:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/emdash-cms/templates/tree/main/blog-cloudflare)

EmDash runs on Cloudflare (D1 + R2 + Workers) or any Node.js server with SQLite. No PHP, no separate hosting tier -- just deploy your Astro site.

## Templates

EmDash ships with three starter templates:

<table>
<tr>
<td width="33%" valign="top">

### Blog

<a href="assets/templates/blog/latest/"><img src="assets/templates/blog/latest/homepage-light-desktop.jpg" alt="Blog template" width="100%"></a>

A classic blog with sidebar widgets, search, and RSS.

- Categories & tags
- Full-text search
- Comment-ready
- RSS feed
- Dark / light mode

</td>
<td width="33%" valign="top">

### Marketing

<a href="assets/templates/marketing/latest/"><img src="assets/templates/marketing/latest/homepage-light-desktop.jpg" alt="Marketing template" width="100%"></a>

A conversion-focused landing page with pricing and contact form.

- Hero with CTAs
- Feature grid
- Pricing cards
- FAQ and contact form
- Dark / light mode

</td>
<td width="33%" valign="top">

### Portfolio

<a href="assets/templates/portfolio/latest/"><img src="assets/templates/portfolio/latest/work-light-desktop.jpg" alt="Portfolio template" width="100%"></a>

A visual portfolio for showcasing creative work.

- Project grid
- Tag filtering
- Case study pages
- RSS feed
- Dark / light mode
<br /><br />
</td>
</tr>
</table>

## Why EmDash?

**WordPress was built for a different era.** Running WordPress today means managing PHP alongside JavaScript, layering caches to get acceptable performance, and knowing that [96% of WordPress security vulnerabilities come from plugins](https://patchstack.com/whitepaper/state-of-wordpress-security-in-2024/). EmDash is what WordPress would look like if you started from scratch with today's tools.

**Sandboxed plugins.** WordPress plugins have full access to the database, filesystem, and user data. A single vulnerable plugin can compromise the entire site. EmDash plugins run in isolated [Worker sandboxes](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) via Dynamic Worker Loaders, each with a declared capability manifest. A plugin that requests `read:content` and `email:send` can do exactly that and nothing else.

```typescript
export default () =>
	definePlugin({
		id: "notify-on-publish",
		capabilities: ["read:content", "email:send"],
		hooks: {
			"content:afterSave": async (event, ctx) => {
				if (event.content.status !== "published") return;
				await ctx.email.send({
					to: "editors@example.com",
					subject: `New post: ${event.content.title}`,
				});
			},
		},
	});
```

**Structured content, not serialized HTML.** WordPress stores rich text as HTML with metadata embedded in comments -- tying your content to its DOM representation. EmDash uses [Portable Text](https://www.portabletext.org/), a structured JSON format that decouples content from presentation. Your content can render as a web page, a mobile app, an email, or an API response without parsing HTML.

**Built for agents.** EmDash ships with agent skills for building plugins and themes, a CLI that lets agents manage content and schema programmatically, and a built-in [MCP server](https://modelcontextprotocol.io/) so AI tools like Claude and ChatGPT can interact with your site directly.

**Runs anywhere.** EmDash uses portable abstractions at every layer -- Kysely for SQL, S3 API for storage -- that work with SQLite, D1, Turso, PostgreSQL, R2, AWS S3, or local files. It runs best on Cloudflare, but it's not locked to it.

## How It Works

EmDash is an Astro integration. Add it to your config and you get a complete CMS: admin panel, REST API, authentication, media library, and plugin system.

```typescript
// astro.config.mjs
import emdash from "emdash/astro";
import { d1 } from "emdash/db";

export default defineConfig({
	integrations: [emdash({ database: d1() })],
});
```

Content types are defined in the database, not in code. Non-developers create and modify collections through the admin UI. Each collection gets a real SQL table with typed columns. Developers generate TypeScript types from the live schema:

```bash
npx emdash types
```

Query content using Astro's Live Collections -- no rebuilds, no separate API:

```astro
---
import { getEmDashCollection } from "emdash";
const { entries: posts } = await getEmDashCollection("posts");
---

{posts.map((post) => <article>{post.data.title}</article>)}
```

## Features

**Content** -- Blog posts, pages, custom content types. Rich text editing via TipTap with Portable Text storage. Revisions, drafts, scheduled publishing, full-text search (FTS5), inline visual editing.

**Admin** -- Full admin panel with visual schema builder, media library (drag-drop uploads via signed URLs), navigation menus, taxonomies, widgets, and a WordPress import wizard.

**Auth** -- Passkey-first (WebAuthn) with OAuth and magic link fallbacks. Role-based access control: Administrator, Editor, Author, Contributor.

**Plugins** -- `definePlugin()` API with lifecycle hooks, KV storage, settings, admin pages, dashboard widgets, custom block types, and API routes. Sandboxed execution on Cloudflare via Dynamic Worker Loaders.

**Agents** -- Skill files for AI-assisted plugin and theme development. CLI for programmatic site management. Built-in MCP server for direct AI tool integration.

**WordPress migration** -- Import posts, pages, media, and taxonomies from WXR exports, the WordPress REST API, or WordPress.com. Agent skills help port plugins and themes.

## Portable Platforms

| Layer    | Cloudflare                  | Also works with                                     |
| -------- | --------------------------- | --------------------------------------------------- |
| Database | D1                          | SQLite, Turso/libSQL, PostgreSQL                    |
| Storage  | R2                          | AWS S3, any S3-compatible service, local filesystem |
| Sessions | KV                          | Redis, file-based                                   |
| Plugins  | Worker isolates (sandboxed) | In-process (safe mode)                              |

## Status

EmDash is in **beta preview**. We welcome contributions, feedback, plugins, themes, and ideas.

```bash
npm create emdash@latest
```

See the [documentation](https://github.com/emdash-cms/emdash/tree/main/docs) for guides, API reference, and plugin development.

## Development

This is a pnpm monorepo. To contribute:

```bash
git clone https://github.com/emdash-cms/emdash.git && cd emdash
pnpm install
pnpm build
```

Run the demo (Node.js + SQLite, no Cloudflare account needed):

```bash
pnpm --filter emdash-demo seed
pnpm --filter emdash-demo dev
```

Open the admin at [http://localhost:4321/\_emdash/admin](http://localhost:4321/_emdash/admin).

```bash
pnpm test          # run all tests
pnpm typecheck     # type check
pnpm lint:quick    # fast lint (< 1s)
pnpm format        # format with oxfmt
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contributor guide.

## Repository Structure

```
packages/
  core/           Astro integration, APIs, admin UI, CLI
  auth/           Authentication library
  blocks/         Portable Text block definitions
  cloudflare/     Cloudflare adapter (D1, R2, Worker Loader)
  plugins/        First-party plugins (forms, embeds, SEO, audit-log, etc.)
  create-emdash/  npm create emdash scaffolding
  gutenberg-to-portable-text/  WordPress block converter

templates/        Starter templates (blog, marketing, portfolio, starter, blank)
demos/            Development and example sites
docs/             Documentation site (Starlight)
```

```

### File: .changeset\README.md
```md
# Changesets

Hello and welcome! This folder has been automatically generated by `@changesets/cli`, a build tool that works
with multi-package repos, or single-package repos to help you version and publish your code. You can
find the full documentation for it [in our repository](https://github.com/changesets/changesets)

We have a quick list of common questions to get you started engaging with this project in
[our documentation](https://github.com/changesets/changesets/blob/main/docs/common-questions.md)

```

### File: docs\package.json
```json
{
  "name": "docs",
  "private": true,
  "type": "module",
  "version": "0.0.1",
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro",
    "generate-types": "wrangler types"
  },
  "dependencies": {
    "@astrojs/cloudflare": "^13.1.7",
    "@astrojs/starlight": "^0.38.2",
    "@astrojs/starlight-tailwind": "^5.0.0",
    "astro": "^6.1.3",
    "sharp": "^0.34.5",
    "starlight-utils": "^1.0.0",
    "tailwindcss": "^4.1.18",
    "wrangler": "catalog:"
  },
  "overrides": {
    "vite": "^7"
  }
}
```

### File: docs\README.md
```md
# EmDash Docs

Documentation site for EmDash, built with [Starlight](https://starlight.astro.build).

## Development

```bash
pnpm dev
```

## Build

```bash
pnpm build
```

```

### File: packages\admin\package.json
```json
{
  "name": "@emdash-cms/admin",
  "version": "0.1.0",
  "description": "Admin UI for EmDash CMS",
  "type": "module",
  "main": "dist/index.js",
  "files": [
    "dist"
  ],
  "exports": {
    ".": {
      "types": "./dist/index.d.ts",
      "default": "./dist/index.js"
    },
    "./styles.css": "./dist/styles.css"
  },
  "scripts": {
    "build": "tsdown && npx @tailwindcss/cli -i src/styles.css -o dist/styles.css --minify",
    "dev": "tsdown src/index.ts --format esm --dts --watch",
    "prepublishOnly": "node --run build",
    "check": "publint && attw --pack --ignore-rules=cjs-resolves-to-esm --ignore-rules=no-resolution",
    "test": "vitest",
    "typecheck": "tsgo --noEmit"
  },
  "dependencies": {
    "@cloudflare/kumo": "^1.16.0",
    "@dnd-kit/core": "^6.3.1",
    "@dnd-kit/sortable": "^10.0.0",
    "@dnd-kit/utilities": "^3.2.2",
    "@emdash-cms/blocks": "workspace:*",
    "@floating-ui/react": "^0.27.16",
    "@phosphor-icons/react": "catalog:",
    "@tanstack/react-query": "catalog:",
    "@tanstack/react-router": "catalog:",
    "@tiptap/core": "catalog:",
    "@tiptap/extension-character-count": "catalog:",
    "@tiptap/extension-drag-handle": "catalog:",
    "@tiptap/extension-drag-handle-react": "catalog:",
    "@tiptap/extension-dropcursor": "catalog:",
    "@tiptap/extension-focus": "catalog:",
    "@tiptap/extension-link": "catalog:",
    "@tiptap/extension-node-range": "catalog:",
    "@tiptap/extension-placeholder": "catalog:",
    "@tiptap/extension-text-align": "catalog:",
    "@tiptap/extension-typography": "catalog:",
    "@tiptap/extension-underline": "catalog:",
    "@tiptap/pm": "catalog:",
    "@tiptap/react": "catalog:",
    "@tiptap/starter-kit": "catalog:",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "dompurify": "^3.3.2",
    "marked": "^17.0.3",
    "react": "catalog:",
    "react-dom": "catalog:",
    "react-hotkeys-hook": "^5.2.4",
    "tailwind-merge": "^3.3.0"
  },
  "devDependencies": {
    "@arethetypeswrong/cli": "catalog:",
    "@tailwindcss/cli": "^4.1.10",
    "@tailwindcss/typography": "^0.5.19",
    "@testing-library/react": "^16.3.0",
    "@tiptap/suggestion": "catalog:",
    "@types/react": "catalog:",
    "@types/react-dom": "catalog:",
    "@vitejs/plugin-react": "^4.6.0",
    "@vitest/browser-playwright": "^4.0.18",
    "jsdom": "^26.1.0",
    "playwright": "^1.58.2",
    "publint": "catalog:",
    "tailwindcss": "^4.1.10",
    "tsdown": "catalog:",
    "typescript": "catalog:",
    "vite": "^7.0.0",
    "vitest": "catalog:",
    "vitest-browser-react": "^2.0.5"
  },
  "peerDependencies": {
    "react": "^18.0.0 || ^19.0.0",
    "react-dom": "^18.0.0 || ^19.0.0"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/emdash-cms/emdash.git",
    "directory": "packages/admin"
  },
  "homepage": "https://github.com/emdash-cms/emdash",
  "keywords": [
    "astro",
    "cms",
    "admin",
    "react"
  ],
  "author": "Matt Kane",
  "license": "MIT"
}
```

### File: packages\auth\package.json
```json
{
  "name": "@emdash-cms/auth",
  "version": "0.1.0",
  "description": "Passkey-first authentication for EmDash",
  "type": "module",
  "main": "dist/index.mjs",
  "files": [
    "dist",
    "src"
  ],
  "exports": {
    ".": {
      "types": "./dist/index.d.mts",
      "default": "./dist/index.mjs"
    },
    "./passkey": {
      "types": "./dist/passkey/index.d.mts",
      "default": "./dist/passkey/index.mjs"
    },
    "./adapters/kysely": {
      "types": "./dist/adapters/kysely.d.mts",
      "default": "./dist/adapters/kysely.mjs"
    },
    "./oauth/github": {
      "types": "./dist/oauth/providers/github.d.mts",
      "default": "./dist/oauth/providers/github.mjs"
    },
    "./oauth/google": {
      "types": "./dist/oauth/providers/google.d.mts",
      "default": "./dist/oauth/providers/google.mjs"
    }
  },
  "scripts": {
    "build": "tsdown",
    "dev": "tsdown --watch",
    "check": "publint && attw --pack --ignore-rules=cjs-resolves-to-esm --ignore-rules=no-resolution",
    "test": "vitest",
    "typecheck": "tsgo --noEmit"
  },
  "dependencies": {
    "@oslojs/crypto": "^1.0.1",
    "@oslojs/encoding": "^1.1.0",
    "@oslojs/webauthn": "^1.0.0",
    "ulidx": "^2.4.1",
    "zod": "^4.3.5"
  },
  "peerDependencies": {
    "astro": ">=6.0.0-beta.0",
    "kysely": "^0.27.0"
  },
  "peerDependenciesMeta": {
    "kysely": {
      "optional": true
    }
  },
  "devDependencies": {
    "@arethetypeswrong/cli": "catalog:",
    "@types/node": "catalog:",
    "astro": "catalog:",
    "publint": "catalog:",
    "tsdown": "catalog:",
    "typescript": "catalog:",
    "vitest": "catalog:"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/emdash-cms/emdash.git",
    "directory": "packages/auth"
  },
  "author": "Matt Kane",
  "license": "MIT"
}
```

### File: packages\core\package.json
```json
{
  "name": "emdash",
  "version": "0.1.0",
  "description": "Astro-native CMS with WordPress migration support",
  "type": "module",
  "main": "dist/index.mjs",
  "bin": {
    "emdash": "./dist/cli/index.mjs",
    "em": "./dist/cli/index.mjs"
  },
  "files": [
    "dist",
    "src",
    "locals.d.ts"
  ],
  "exports": {
    ".": {
      "types": "./dist/index.d.mts",
      "default": "./dist/index.mjs"
    },
    "./astro": {
      "types": "./dist/astro/index.d.mts",
      "default": "./dist/astro/index.mjs"
    },
    "./middleware": {
      "types": "./dist/astro/middleware.d.mts",
      "default": "./dist/astro/middleware.mjs"
    },
    "./middleware/setup": {
      "types": "./dist/astro/middleware/setup.d.mts",
      "default": "./dist/astro/middleware/setup.mjs"
    },
    "./middleware/auth": {
      "types": "./dist/astro/middleware/auth.d.mts",
      "default": "./dist/astro/middleware/auth.mjs"
    },
    "./middleware/redirect": {
      "types": "./dist/astro/middleware/redirect.d.mts",
      "default": "./dist/astro/middleware/redirect.mjs"
    },
    "./ui": "./src/ui.ts",
    "./ui/search": "./src/components/LiveSearch.astro",
    "./cli": {
      "types": "./dist/cli/index.d.mts",
      "default": "./dist/cli/index.mjs"
    },
    "./routes/*": "./src/astro/routes/*",
    "./db": {
      "types": "./dist/db/index.d.mts",
      "default": "./dist/db/index.mjs"
    },
    "./db/sqlite": {
      "types": "./dist/db/sqlite.d.mts",
      "default": "./dist/db/sqlite.mjs"
    },
    "./db/libsql": {
      "types": "./dist/db/libsql.d.mts",
      "default": "./dist/db/libsql.mjs"
    },
    "./db/postgres": {
      "types": "./dist/db/postgres.d.mts",
      "default": "./dist/db/postgres.mjs"
    },
    "./storage/local": {
      "types": "./dist/storage/local.d.mts",
      "default": "./dist/storage/local.mjs"
    },
    "./storage/s3": {
      "types": "./dist/storage/s3.d.mts",
      "default": "./dist/storage/s3.mjs"
    },
    "./media": {
      "types": "./dist/media/index.d.mts",
      "default": "./dist/media/index.mjs"
    },
    "./media/local-runtime": {
      "types": "./dist/media/local-runtime.d.mts",
      "default": "./dist/media/local-runtime.mjs"
    },
    "./runtime": {
      "types": "./dist/runtime.d.mts",
      "default": "./dist/runtime.mjs"
    },
    "./request-context": {
      "types": "./dist/request-context.d.mts",
      "default": "./dist/request-context.mjs"
    },
    "./seed": {
      "types": "./dist/seed/index.d.mts",
      "default": "./dist/seed/index.mjs"
    },
    "./middleware/request-context": {
      "types": "./dist/astro/middleware/request-context.d.mts",
      "default": "./dist/astro/middleware/request-context.mjs"
    },
    "./locals": {
      "types": "./locals.d.ts"
    },
    "./client": {
      "types": "./dist/client/index.d.mts",
      "default": "./dist/client/index.mjs"
    },
    "./client/cf-access": {
      "types": "./dist/client/cf-access.d.mts",
      "default": "./dist/client/cf-access.mjs"
    },
    "./seo": {
      "types": "./dist/seo/index.d.mts",
      "default": "./dist/seo/index.mjs"
    },
    "./page": {
      "types": "./dist/page/index.d.mts",
      "default": "./dist/page/index.mjs"
    },
    "./plugin-utils": {
      "types": "./dist/plugin-utils.d.mts",
      "default": "./dist/plugin-utils.mjs"
    },
    "./plugins/adapt-sandbox-entry": {
      "types": "./dist/plugins/adapt-sandbox-entry.d.mts",
      "default": "./dist/plugins/adapt-sandbox-entry.mjs"
    }
  },
  "imports": {
    "#api/schemas.js": "./src/api/schemas/index.js",
    "#api/*": "./src/api/*",
    "#db/*": "./src/database/*",
    "#auth/*": "./src/auth/*",
    "#schema/*": "./src/schema/*",
    "#search/*": "./src/search/*",
    "#sections/*": "./src/sections/*",
    "#menus/*": "./src/menus/*",
    "#widgets/*": "./src/widgets/*",
    "#import/*": "./src/import/*",
    "#utils/*": "./src/utils/*",
    "#preview/*": "./src/preview/*",
    "#seed/*": "./src/seed/*",
    "#settings/*": "./src/settings/*",
    "#seo/*": "./src/seo/*",
    "#plugins/*": "./src/plugins/*",
    "#media/*": "./src/media/*",
    "#mcp/*": "./src/mcp/*",
    "#comments/*": "./src/comments/*",
    "#types": "./src/astro/types.js"
  },
  "scripts": {
    "build": "tsdown",
    "dev": "tsdown --watch",
    "prepublishOnly": "node --run build",
    "typecheck": "tsgo --noEmit",
    "check": "publint && attw --pack --ignore-rules=cjs-resolves-to-esm --ignore-rules=no-resolution --ignore-rules=internal-resolution-error",
    "test": "vitest",
    "test:smoke": "vitest run --config vitest.smoke.config.ts",
    "test:integration": "vitest run --config vitest.integration.config.ts"
  },
  "dependencies": {
    "@emdash-cms/admin": "workspace:*",
    "@emdash-cms/auth": "workspace:*",
    "@emdash-cms/gutenberg-to-portable-text": "workspace:*",
    "@floating-ui/react": "^0.27.16",
    "@modelcontextprotocol/sdk": "^1.26.0",
    "@portabletext/toolkit": "^5.0.1",
    "@tiptap/core": "catalog:",
    "@tiptap/extension-focus": "catalog:",
    "@tiptap/extension-image": "catalog:",
    "@tiptap/extension-link": "catalog:",
    "@tiptap/extension-placeholder": "catalog:",
    "@tiptap/extension-text-align": "catalog:",
    "@tiptap/extension-typography": "catalog:",
    "@tiptap/extension-underline": "catalog:",
    "@tiptap/react": "catalog:",
    "@tiptap/starter-kit": "catalog:",
    "@tiptap/suggestion": "catalog:",
    "@unpic/placeholder": "^0.1.2",
    "arctic": "^3.7.0",
    "astro-portabletext": "^0.11.0",
    "better-sqlite3": "catalog:",
    "blurhash": "^2.0.5",
    "citty": "^0.1.6",
    "consola": "^3.4.2",
    "croner": "^10.0.1",
    "image-size": "^2.0.2",
    "jose": "^6.1.3",
    "jpeg-js": "^0.4.4",
    "kysely": "^0.27.0",
    "mime": "^4.1.0",
    "modern-tar": "^0.7.5",
    "picocolors": "^1.1.1",
    "sanitize-html": "^2.17.1",
    "sax": "^1.4.1",
    "ulidx": "^2.4.1",
    "upng-js": "^2.1.0",
    "zod": "^4.3.5"
  },
  "optionalDependencies": {
    "@libsql/kysely-libsql": "^0.4.0",
    "pg": "^8.0.0"
  },
  "peerDependencies": {
    "@astrojs/react": ">=5.0.0-beta.0",
    "@tanstack/react-query": ">=5.0.0",
    "@tanstack/react-router": ">=1.100.0",
    "astro": ">=6.0.0-beta.0",
    "react": ">=18.0.0",
    "react-dom": ">=18.0.0"
  },
  "devDependencies": {
    "@apidevtools/swagger-parser": "^12.1.0",
    "@arethetypeswrong/cli": "catalog:",
    "@emdash-cms/blocks": "workspace:*",
    "@types/better-sqlite3": "^7.6.12",
    "@types/pg": "^8.16.0",
    "@types/sanitize-html": "^2.16.0",
    "@types/sax": "^1.2.7",
    "@vitest/ui": "^4.0.17",
    "publint": "catalog:",
    "tsdown": "catalog:",
    "typescript": "catalog:",
    "vite": "^6.0.0",
    "vitest": "catalog:",
    "zod-openapi": "^5.4.6"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/emdash-cms/emdash.git",
    "directory": "packages/core"
  },
  "homepage": "https://github.com/emdash-cms/emdash",
  "keywords": [
    "astro",
    "cms",
    "content",
    "wordpress"
  ],
  "author": "Matt Kane",
  "license": "MIT"
}

```

### File: packages\core\README.md
```md
# emdash

The core EmDash CMS package - an Astro-native, agent-portable reimplementation of WordPress.

## Installation

```shell
npm install emdash
```

## Features

- **Content Management** - Collections, fields, Live Collections integration
- **Media Library** - Upload via signed URLs, S3-compatible storage
- **Full-Text Search** - FTS5 with Porter stemming, per-collection config
- **Navigation Menus** - Hierarchical menus with URL resolution
- **Taxonomies** - Categories, tags, custom taxonomies
- **Widget Areas** - Content, menu, and component widgets
- **Sections** - Reusable content blocks
- **Plugin System** - Hooks, storage, settings, admin pages
- **WordPress Import** - WXR, REST API, WordPress.com

## Quick Start

```typescript
// astro.config.mjs
import { defineConfig } from "astro/config";
import emdash, { local } from "emdash/astro";
import { sqlite } from "emdash/db";

export default defineConfig({
	integrations: [
		emdash({
			database: sqlite({ url: "file:./data.db" }),
			storage: local({
				directory: "./uploads",
				baseUrl: "/_emdash/api/media/file",
			}),
		}),
	],
});
```

```typescript
// src/live.config.ts
import { defineLiveCollection } from "astro:content";
import { emdashLoader } from "emdash/runtime";

export const collections = {
	_emdash: defineLiveCollection({ loader: emdashLoader() }),
};
```

## API

```typescript
import {
	getEmDashCollection,
	getEmDashEntry,
	getSiteSettings,
	getMenu,
	getTaxonomyTerms,
	getWidgetArea,
	search,
} from "emdash";

// Content
const { entries } = await getEmDashCollection("posts");
const { entry } = await getEmDashEntry("posts", "hello-world");

// Site settings
const settings = await getSiteSettings();

// Navigation
const menu = await getMenu("primary");

// Taxonomies
const categories = await getTaxonomyTerms("categories");

// Widgets
const sidebar = await getWidgetArea("sidebar");

// Search
const results = await search("hello world", { collections: ["posts"] });
```

## Documentation

See the [documentation site](https://docs.emdashcms.com) for guides, API reference, and plugin development.

```

### File: packages\plugins\README.md
```md

```

### File: templates\blog\package.json
```json
{
  "name": "@emdash-cms/template-blog",
  "version": "0.0.3",
  "private": true,
  "type": "module",
  "emdash": {
    "seed": "seed/seed.json"
  },
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "start": "node ./dist/server/entry.mjs",
    "bootstrap": "emdash init && emdash seed",
    "seed": "emdash seed",
    "typecheck": "astro check"
  },
  "dependencies": {
    "@astrojs/node": "catalog:",
    "@astrojs/react": "catalog:",
    "@emdash-cms/plugin-audit-log": "workspace:*",
    "astro": "catalog:",
    "better-sqlite3": "catalog:",
    "emdash": "workspace:*",
    "react": "catalog:",
    "react-dom": "catalog:"
  },
  "devDependencies": {
    "@astrojs/check": "catalog:"
  },
  "peerDependencies": {},
  "optionalDependencies": {}
}
```

### File: templates\marketing\package.json
```json
{
	"name": "@emdash-cms/template-marketing",
	"version": "0.0.3",
	"private": true,
	"type": "module",
	"emdash": {
		"seed": "seed/seed.json"
	},
	"scripts": {
		"dev": "astro dev",
		"build": "astro build",
		"preview": "astro preview",
		"start": "node ./dist/server/entry.mjs",
		"bootstrap": "emdash init && emdash seed",
		"seed": "emdash seed",
		"typecheck": "astro check"
	},
	"dependencies": {
		"@astrojs/node": "catalog:",
		"@astrojs/react": "catalog:",
		"astro": "catalog:",
		"better-sqlite3": "catalog:",
		"emdash": "workspace:*",
		"react": "catalog:",
		"react-dom": "catalog:"
	},
	"devDependencies": {
		"@astrojs/check": "catalog:"
	}
}

```

### File: .oxfmtrc.json
```json
{
	"useTabs": true,
	"experimentalSortImports": {},
	"ignorePatterns": [
		"**/dist/**",
		"**/node_modules/**",
		"**/*.mdx",
		"**/package.json",
		"**/emdash-env.d.ts"
	]
}

```

### File: .oxlintrc.json
```json
{
	"$schema": "./node_modules/oxlint/configuration_schema.json",
	"plugins": ["typescript", "import", "unicorn", "promise"],
	"jsPlugins": ["@e18e/eslint-plugin"],
	"categories": {
		"correctness": "error",
		"suspicious": "warn",
		"perf": "warn"
	},
	"rules": {
		"no-await-in-loop": "off",
		"no-unused-vars": [
			"warn",
			{
				"argsIgnorePattern": "^_",
				"varsIgnorePattern": "^_"
			}
		],
		"unicorn/filename-case": "off",
		"unicorn/prevent-abbreviations": "off",
		"unicorn/no-null": "off",
		"unicorn/prefer-add-event-listener": "off",
		"typescript/no-unsafe-type-assertion": "warn",
		"typescript/unbound-method": "off",
		"typescript/no-unnecessary-boolean-literal-compare": "off",
		"import/no-named-as-default": "off",
		"import/no-unassigned-import": [
			"warn",
			{
				"allow": ["**/*.css", "@testing-library/react", "vitest-browser-react"]
			}
		],
		"e18e/prefer-array-at": "error",
		"e18e/prefer-array-fill": "error",
		"e18e/prefer-includes": "error",
		"e18e/prefer-array-to-reversed": "error",
		"e18e/prefer-array-to-sorted": "error",
		"e18e/prefer-array-to-spliced": "error",
		"e18e/prefer-nullish-coalescing": "error",
		"e18e/prefer-object-has-own": "error",
		"e18e/prefer-spread-syntax": "error",
		"e18e/prefer-url-canparse": "error",
		"e18e/ban-dependencies": "error",
		"e18e/prefer-array-from-map": "error",
		"e18e/prefer-timer-args": "error",
		"e18e/prefer-date-now": "error",
		"e18e/prefer-regex-test": "error",
		"e18e/prefer-array-some": "error",
		"e18e/prefer-static-regex": "error"
	},
	"overrides": [
		{
			"files": ["**/*.test.ts", "**/*.test.tsx", "**/tests/**/*.ts", "**/tests/**/*.tsx"],
			"rules": {
				"typescript/no-unsafe-type-assertion": "off",
				"typescript/no-unnecessary-type-assertion": "off",
				"unicorn/consistent-function-scoping": "off",
				"e18e(prefer-static-regex)": "off"
			}
		},
		{
			"files": [
				"**/database/repositories/content.ts",
				"**/database/repositories/comment.ts",
				"**/database/repositories/user.ts",
				"**/mcp/server.ts",
				"**/client/index.ts",
				"**/client/transport.ts",
				"**/client/portable-text.ts",
				"**/cli/**/*.ts",
				"**/api/handlers/api-tokens.ts",
				"**/api/handlers/device-flow.ts",
				"**/api/handlers/oauth-authorization.ts",
				"**/api/handlers/comments.ts",
				"**/routes/api/oauth/token.ts",
				"**/routes/api/comments/**/*.ts",
				"**/routes/api/admin/comments/**/*.ts",
				"**/routes/api/plugins/**/*.ts",
				"**/plugins/hooks.ts",
				"**/plugins/context.ts",
				"**/plugins/cron.ts",
				"**/plugins/define-plugin.ts",
				"**/plugins/request-meta.ts",
				"**/seed/load.ts",
				"**/comments/notifications.ts",
				"**/astro/integration/index.ts",
				"packages/plugins/**/*.ts",
				"packages/plugins/**/*.tsx",
				"packages/blocks/**/*.tsx",
				"packages/admin/**/*.tsx"
			],
			"rules": {
				"typescript/no-unsafe-type-assertion": "off"
			}
		}
	],
	"ignorePatterns": [
		"**/dist/**",
		"**/node_modules/**",
		"**/*.d.ts",
		"skills/**/scaffold/**",
		".opencode/skills/**/scaffold/**",
		".claude/skills/**/scaffold/**"
	]
}

```

### File: AGENTS.md
```md
This file provides guidance to agentic coding tools when working with code in this repository.

## Project Status

**Beta.** EmDash is published to npm. All development happens inside this monorepo using `workspace:*` links. See [CONTRIBUTING.md](CONTRIBUTING.md) for the human-readable contributor guide (setup, repo layout, "build your own site" workflow).

## Repository Structure

This is a monorepo using pnpm workspaces.

`CLAUDE.md` is a symlink to `AGENTS.md`. `.opencode/skills` and `.claude/skills` are symlinks to `skills/`. Don't try to sync between them.

- **Root**: Workspace configuration and shared tooling
- **packages/core**: Main `emdash` package - Astro integration and core APIs
- **demos/**: Demo applications and examples (`demos/simple/` is the primary dev target)
- **templates/**: Starter templates (blog, marketing, portfolio, starter, blank) -- contributors copy these into `demos/` to build their own sites
- **docs/**: Public documentation site (Starlight)

# Rules

This is a pre-release project. Do not add backwards compatibility or legacy patterns. Do not deprecate -- remove instead. Do not add migration paths.

**Build for the known future.** If we know we'll need something, build it now. Only defer things where there's genuine uncertainty about whether or how we'll need them. "We'll need it later" is a reason to do it now, not a reason to punt.

**TDD for bugs.** Write a failing test -> fix the bug -> verify the test passes. A bug without a reproducing test is not fixed.

## Contribution Rules (for AI agents and human contributors)

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR. Key rules:

- **You MUST use the PR template.** Every PR must include the PR template with all sections filled out. The template is loaded automatically when you create a PR via the GitHub UI. If you create a PR via the API or CLI, copy the template from `.github/PULL_REQUEST_TEMPLATE.md` into the PR body. **PRs that do not use the template will be closed automatically by CI.**
- **Features require a prior approved Discussion.** Do not open a feature PR without one. It will be closed. Open a [Discussion](https://github.com/emdash-cms/emdash/discussions/categories/ideas) in the Ideas category first.
- **Bug fixes and docs** can be PRed directly.
- **Check every applicable checkbox** in the PR template, including the "I have read CONTRIBUTING.md" box and the AI disclosure box if any part of the code was AI-generated.
- **Do not make bulk/spray changes** (e.g., "fix all lint warnings", "add types everywhere", "improve error handling across codebase"). If you see a systemic issue, open a Discussion.
- **Do not touch code outside the scope of your change.** No drive-by refactors, no "while I'm here" improvements, no added comments or logging in unrelated files.
- **All CI checks must pass.** Typecheck, lint, format, and tests. No exceptions.

## Workflow

### Before Starting

1. Run `pnpm --silent lint:json | jq '.diagnostics | length'` and fix any issues. Non-negotiable.

### During Work

- Run `pnpm --silent lint:quick` after every edit -- takes less than a second. Returns JSON with stderr redirected to /dev/null, so it won't break parsers. Fix any issues immediately.
- Run `pnpm typecheck` (packages) or `pnpm typecheck:demos` (Astro demos) after each round of edits.
- Format regularly. pnpm format in the root uses oxfmt with tabs for indentation and is very fast. Don't let formatting pile up.
- Commit regularly, and always format and quick lint beforehand.
- Update tasks.md when completing tasks. Write a journal entry when starting or finishing significant work, or if you learn anything interesting or useful that you'd like to remember.

### Before Committing

You verified linting and types were clean before starting. If they're failing now, your changes caused it -- even if the errors are in files you didn't touch. Don't dismiss failures as "unrelated". Don't assign blame. Just fix them.

### Changesets

If your change affects a published package's behavior, add a changeset. Without one, the change won't trigger a package release.

```bash
pnpm changeset --empty
```

This creates a blank changeset file in `.changeset/`. Edit it to add the affected package(s), bump type, and description:

```markdown
---
"emdash": patch
---

Fixes CLI `--json` flag so JSON output is clean.
```

Start descriptions with a present-tense verb (Adds, Fixes, Updates, Removes, Refactors). Focus on what changes for the user, not implementation details.

Skip changesets for docs-only, test-only, CI, or demo/template changes.

See [CONTRIBUTING.md § Changesets](CONTRIBUTING.md#changesets) for full guidance and examples.

### PR Flow

1. All tests pass: `pnpm test`
2. Full lint suite clean: `pnpm --silent lint:json | jq '.diagnostics | length'`. Returns JSON with stderr piped to /dev/null, so it won't break parsers. Fix any issues.
3. Format with `pnpm format` (oxfmt with tabs for indentation, configured in `.prettierrc`).
4. Add a changeset if the change affects a published package: `pnpm changeset`.
5. Open the PR with the `pr` skill. Fill out every section of the PR template. Check the AI disclosure box.

### Dev Servers

Use `bgproc` (not raw process management):

```bash
bgproc start -n devserver -w -- pnpm dev   # start and wait for port
bgproc stop devserver                       # stop
bgproc logs devserver                       # view logs
```

## Architecture Overview

EmDash is an Astro-native CMS that stores its schema in the database, not in code.

### Core Architecture

- **Schema in the database.** `_emdash_collections` and `_emdash_fields` are the source of truth. Each collection gets a real SQL table (`ec_posts`, `ec_products`) with typed columns -- not EAV.
- **Middleware chain** (in order): runtime init -> setup check -> auth -> request context (ALS). Auth middleware handles authentication; individual routes handle authorization.
- **Handler layer** (`api/handlers/*.ts`) -- Business logic returns `ApiResponse<T>` (`{ success, data?, error? }`). Route files are thin wrappers that parse input, call handlers, and format responses.
- **Storage abstraction** -- `Storage` interface with `upload/download/delete/exists/list/getSignedUploadUrl`. Implementations: `LocalStorage` (dev), `S3Storage` (R2/AWS). Access via `emdash.storage` from locals.

### Known Quality Patterns

**Index discipline.** Every content table gets indexes on: `status`, `slug`, `created_at`, `deleted_at`, `scheduled_at` (partial -- `WHERE scheduled_at IS NOT NULL`), `live_revision_id`, `draft_revision_id`, `author_id`, `primary_byline_id`, `updated_at`, `locale`, `translation_group`. Foreign key columns always get an index. Naming: `idx_{table}_{column}` for single-column, `idx_{table}_{purpose}` for multi-column.

**API envelope consistency.** Handlers return `ApiResponse<T>` wrapping data in `{ success, data }`. List endpoints return `{ items, nextCursor? }` inside `data`. The admin client's `parseApiResponse` unwraps `body.data`. Be aware of this layering when adding new endpoints.

## Commands

### Root-level commands (run from repository root):

- `pnpm build` - Build all packages
- `pnpm test` - Run tests for all packages
- `pnpm check` - Run type checking and linting for all packages
- `pnpm format` - Format code using oxfmt

### Package-level commands (run within individual packages):

- `pnpm build` - Build the package using tsdown (ESM + DTS output)
- `pnpm dev` - Watch mode for development
- `pnpm test` - Run vitest tests
- `pnpm check` - Run publint and @arethetypeswrong/cli checks

## Key Files

| File                                | Purpose                                               |
| ----------------------------------- | ----------------------------------------------------- |
| `src/live.config.ts`                | Collection schemas + admin config (user's site)       |
| `src/emdash-runtime.ts`             | Central runtime; orchestrates DB, plugins, storage    |
| `src/schema/registry.ts`            | Manages `ec_*` table creation/modification            |
| `src/database/migrations/runner.ts` | StaticMigrationProvider; register new migrations here |
| `src/plugins/manager.ts`            | Loads and orchestrates trusted plugins                |

## Code Patterns

### Database: Never Interpolate Into SQL

Kysely is the query builder. Use it properly:

- **Never** use `sql.raw()` with string interpolation or template literals containing variables.
- **Never** build SQL strings with `+` or backtick interpolation and pass them to `sql.raw()`.
- For **values**, use Kysely's `sql` tagged template: `` sql`SELECT * FROM t WHERE id = ${id}` `` -- interpolated values are automatically parameterized.
- For **identifiers** (table/column names), use `sql.ref()` which quotes them safely.
- If you absolutely must use `sql.raw()` for dynamic identifiers, validate them first with `validateIdentifier()` from `database/validate.ts` which asserts `/^[a-z][a-z0-9_]*$/`.
- The `json_extract(data, '$.${field}')` pattern is particularly dangerous -- always validate `field` before interpolation.

```typescript
// WRONG -- SQL injection via string interpolation
const query = `SELECT * FROM ${table} WHERE name = '${name}'`;
await sql.raw(query).execute(db);

// WRONG -- field name interpolated into sql.raw()
return sql.raw(`json_extract(data, '$.${field}')`);

// RIGHT -- parameterized value
await sql`SELECT * FROM ${sql.ref(table)} WHERE name = ${name}`.execute(db);

// RIGHT -- validated identifier in raw SQL
validateIdentifier(field);
return sql.raw(`json_extract(data, '$.${field}')`);
```

### API Routes: Use Shared Utilities

All API routes under `astro/routes/api/` must follow these patterns:

**Error responses** -- use `apiError()` from `api/error.ts`:

```typescript
// WRONG -- inline JSON.stringify with ad-hoc shape
return new Response(JSON.stringify({ error: "Not found" }), { status: 404 });

// RIGHT -- consistent shape: { error: { code, message } }
return apiError("NOT_FOUND", "Content not found", 404);
```

**Catch blocks** -- use `handleError()`, never expose `error.message` to clients:

```typescript
// WRONG -- leaks internal error details
catch (error) {
  return new Response(JSON.stringify({
    error: error instanceof Error ? error.message : "Unknown error"
  }), { status: 500 });
}

// RIGHT -- logs internally, returns generic message
catch (error) {
  return handleError(error, "Failed to update content", "CONTENT_UPDATE_ERROR");
}
```

**Input validation** -- use `parseBody()` / `parseQuery()` from `api/parse.ts`, never use `as` casts on `request.json()`:

```typescript
// WRONG -- no runtime validation, malformed input reaches the database
const body = (await request.json()) as CreateContentInput;

// RIGHT -- Zod validation, returns 400 on failure
const body = await parseBody(request, createContentSchema);
```

**Initialization checks** -- use a consistent message:

```typescript
if (!emdash) return apiError("NOT_CONFIGURED", "EmDash is not initialized", 500);
```

**Handler results** -- when using the handler layer (`api/handlers/*.ts`), always unwrap consistently:

```typescript
const result = await handler.handleContentGet(collection, id);
if (!result.success) {
	return apiError(result.error.code, result.error.message, mapErrorToStatus(result.error.code));
}
return Response.json(result.data);
```

### API Routes: Authorization

Every route that modifies state must check authorization. The auth middleware only checks authentication (is the user logged in); individual routes must check roles:

```typescript
import { requireRole, Role } from "../../auth/permissions.js";

// At the top of any state-changing handler:
const roleError = requireRole(user, Role.EDITOR);
if (roleError) return roleError;
```

Minimum roles:

- **ADMIN**: settings, schema, plugins, user management, imports, search rebuild
- **EDITOR**: all content CRUD, media, taxonomies, menus, widgets, publish/unpublish
- **AUTHOR**: own content CRUD, media upload
- **CONTRIBUTOR**: own content create/edit (no publish), media upload

### API Routes: CSRF Protection

All state-changing endpoints (POST/PUT/DELETE) require the `X-EmDash-Request: 1` header, enforced by auth middleware. The admin UI and visual editing client send this header automatically. Do not add GET handlers for state-changing operations.

### Pagination

All list endpoints must use cursor-based pagination with a consistent shape:

```typescript
// Return type for all list queries
interface FindManyResult<T> {
	items: T[];
	nextCursor?: string;
}
```

- Use `encodeCursor(orderValue, id)` / `decodeCursor(cursor)` utilities.
- Default limit: 50. Maximum limit: 100. Always clamp.
- The response array key is always `items` (not `results`, not a bare array).
- Never return a bare array from a list endpoint -- always wrap in `{ items, nextCursor? }`.

### Adding Database Tables or Columns

When creating tables or adding columns queried in WHERE or ORDER BY clauses, add indexes. Check existing patterns in `database/migrations/` and `schema/registry.ts`. Foreign key columns should always have an index.

Index naming: `idx_{table}_{column}` for single-column, `idx_{table}_{purpose}` for multi-column. Content tables get standard indexes on `status`, `slug`, `created_at`, `deleted_at`, `author_id`, and all foreign key columns.

### Migrations

Migrations live in `packages/core/src/database/migrations/`. Conventions:

- **Naming:** `NNN_descriptive_name.ts` -- zero-padded 3-digit sequential number.
- **Exports:** Each migration exports `up(db: Kysely<unknown>)` and `down(db: Kysely<unknown>)`.
- **System tables** use Kysely's schema builder (`db.schema.createTable(...)`).
- **Dynamic content tables** (`ec_*`) use `sql` tagged templates with `sql.ref()` for identifiers.
- **Column types:** SQLite types -- `"text"`, `"integer"`, `"real"`, `"blob"`. Booleans are `"integer"` with `defaultTo(0)`. Timestamps are `"text"` with ``defaultTo(sql`(datetime('now'))`)``. IDs are `"text"` primary keys (ULIDs from `ulidx`).
- **Index naming:** `idx_{table}_{column}` for single-column, `idx_{table}_{purpose}` for multi-column.
- **Foreign keys** must always have an accompanying index.
- **Registration:** Migrations are statically imported in `database/runner.ts` and added to the `StaticMigrationProvider`. They are NOT auto-discovered -- this is required for Workers bundler compatibility. When adding a migration: (1) create the file, (2) add a static import in `runner.ts`, (3) add it to `getMigrations()`.
- **Multi-table migrations:** When altering all content tables, query `_emdash_collections` to discover `ec_*` tables and loop. See `013_scheduled_publishing.ts` for the pattern.

### API Route Structure

Route files live in `packages/core/src/astro/routes/api/`. Conventions:

- Every route file starts with `export const prerender = false;`.
- Handlers are named exports: `export const GET: APIRoute`, `export const POST: APIRoute`, e
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# Contributing to EmDash

> **Beta.** EmDash is published to npm. During development you work inside the monorepo -- packages use `workspace:*` links, so everything "just works" without publishing.

## Prerequisites

- **Node.js** 22+
- **pnpm** 10+ (`corepack enable` if you don't have it)
- **Git**

## Quick Setup

```bash
git clone <repo-url> && cd emdash
pnpm install
pnpm build          # build all packages (required before first run)
```

### Run the Demo

The `demos/simple/` app is the primary development target. It is kept in sync with `templates/blog/` and uses Node.js + SQLite — no Cloudflare account needed.

```bash
pnpm --filter emdash-demo seed   # seed sample content
pnpm --filter emdash-demo dev    # http://localhost:4321
```

Open the admin at `http://localhost:4321/_emdash/admin`.

In dev mode, passkey auth is bypassed automatically. If you hit the login screen, visit:

```
http://localhost:4321/_emdash/api/setup/dev-bypass?redirect=/_emdash/admin
```

### Run with Cloudflare (optional)

`demos/cloudflare/` runs on the real `workerd` runtime with D1. See its [README](demos/cloudflare/README.md) for setup.

### Developing Templates

Templates in `templates/` are workspace members and can be run directly:

```bash
# First time: set up database and seed content
pnpm --filter @emdash-cms/template-portfolio bootstrap

# Run the dev server
pnpm --filter @emdash-cms/template-portfolio dev
```

Available templates:

| Template  | Filter Name                      |
| --------- | -------------------------------- |
| Blog      | `@emdash-cms/template-blog`      |
| Portfolio | `@emdash-cms/template-portfolio` |
| Marketing | `@emdash-cms/template-marketing` |

Edit files in `templates/{name}/src/` and changes hot reload.

**Cloudflare variants** (`*-cloudflare`) share source with their base templates via `scripts/sync-cloudflare-templates.sh`. Run that script after editing base template shared files.

Demo/template sync is handled by `scripts/sync-blog-demos.sh`:

- Full sync: `templates/blog` -> `demos/simple`
- Frontend sync (keep runtime-specific config/files):
  - `templates/blog-cloudflare` -> `demos/cloudflare`
  - `templates/blog-cloudflare` -> `demos/preview`
  - `templates/blog` -> `demos/postgres`

To start fresh, delete the database and re-bootstrap:

```bash
rm templates/portfolio/data.db
pnpm --filter @emdash-cms/template-portfolio bootstrap
```

## Development Workflow

### Watch Mode

For iterating on core packages alongside the demo, run two terminals:

```bash
# Terminal 1 — rebuild packages/core on change
pnpm --filter emdash dev

# Terminal 2 — run the demo
pnpm --filter emdash-demo dev
```

Changes to `packages/core/src/` will be picked up by the demo's dev server automatically.

### Checks

Run these before committing:

```bash
pnpm typecheck       # TypeScript (packages)
pnpm typecheck:demos # TypeScript (Astro demos)
pnpm --silent lint:quick   # fast lint (< 1s) — run often
pnpm --silent lint:json    # full type-aware lint (~10s) — run before commits
pnpm format          # auto-format with oxfmt
```

Type checking **must** pass. Lint **must** pass. Don't commit with known failures.

### Tests

```bash
pnpm test                              # all packages
pnpm --filter emdash test            # core only
pnpm --filter emdash test --watch    # watch mode
pnpm test:e2e                          # Playwright (requires demo running)
```

Tests use real in-memory SQLite — no mocking. Each test gets a fresh database.

## Repository Layout

```
emdash/
├── packages/
│   ├── core/              # emdash — the main package (Astro integration + APIs + admin)
│   ├── auth/              # @emdash-cms/auth — passkeys, OAuth, magic links
│   ├── admin/             # @emdash-cms/admin — React admin SPA
│   ├── cloudflare/        # @emdash-cms/cloudflare — CF adapter + plugin sandbox
│   ├── create-emdash/   # create-emdash — project scaffolder
│   ├── gutenberg-to-portable-text/  # WP block → Portable Text converter
│   └── plugins/           # first-party plugins (each dir = package)
├── demos/
│   ├── simple/            # emdash-demo — primary dev/test app (Node.js + SQLite)
│   ├── cloudflare/        # Cloudflare Workers demo (D1)
│   ├── plugins-demo/      # plugin development testbed
│   └── ...
├── templates/             # starter templates (blog, portfolio, marketing + cloudflare variants)
├── docs/                  # public documentation site (Starlight)
└── e2e/                   # Playwright test fixtures
```

The main package is **`packages/core`**. Most of your work will happen there.

## Building Your Own Site (Inside the Monorepo)

The easiest way to build a real site during development is to add it as a workspace member.

1. Copy `templates/blog/` (or `templates/blank/`) into `demos/`:

   ```bash
   cp -r templates/blog demos/my-site
   ```

2. Edit `demos/my-site/package.json` — set a unique `name` field.

3. Run `pnpm install` from the root to link workspace dependencies.

4. Start developing:

   ```bash
   pnpm --filter my-site dev
   ```

Your site will use `workspace:*` links to the local packages, so any changes you make to core will be reflected immediately (with watch mode).

## Key Architectural Concepts

- **Schema lives in the database**, not in code. `_emdash_collections` and `_emdash_fields` are the source of truth.
- **Real SQL tables** per collection (`ec_posts`, `ec_products`), not EAV.
- **Kysely** for all queries. Never interpolate into SQL -- see `AGENTS.md` for the full rules.
- **Handler layer** (`api/handlers/*.ts`) holds business logic. Route files are thin wrappers.
- **Middleware chain**: runtime init -> setup check -> auth -> request context.

## Adding a Migration

1. Create `packages/core/src/database/migrations/NNN_description.ts` (zero-padded sequence number).
2. Export `up(db)` and `down(db)` functions.
3. **Register it** in `packages/core/src/database/migrations/runner.ts` — migrations are statically imported, not auto-discovered (Workers bundler compatibility).

## Adding an API Route

1. Create the file in `packages/core/src/astro/routes/api/`.
2. Start with `export const prerender = false;`.
3. Use `apiError()`, `handleError()`, `parseBody()` from `#api/`.
4. Check authorization with `requirePerm()` on all state-changing routes.
5. Register the route in `packages/core/src/astro/integration/routes.ts`.

## Contribution Policy

### What we accept

| Type             | Process                                                                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Bug fixes**    | Open a PR directly. Include a failing test that reproduces the bug.                                                                  |
| **Docs / typos** | Open a PR directly.                                                                                                                  |
| **Features**     | Open a [Discussion](https://github.com/emdash-cms/emdash/discussions/categories/ideas) first. Wait for approval before writing code. |
| **Refactors**    | Open a Discussion first. Refactors are opinionated and need alignment.                                                               |
| **Performance**  | Open a Discussion first with benchmarks showing the improvement.                                                                     |

**PRs that add features without a prior approved Discussion will be closed.** This isn't about gatekeeping — it's about not wasting your time on work that might not align with the project's direction. Talk to us first and we'll figure out the right approach together.

### AI-generated PRs

We welcome AI-assisted contributions. They are held to the same quality bar as any other PR:

- The submitter is responsible for the code's correctness, not the AI tool.
- AI-generated PRs must pass all CI checks, follow the project's code patterns, and include tests.
- The PR template has an AI disclosure checkbox — please check it. This isn't punitive; it helps reviewers know to pay extra attention to edge cases that AI tools commonly miss.
- Bulk/spray PRs across the repo (e.g., "fix all lint warnings", "add types everywhere") will be closed. If you see a pattern worth fixing, open a Discussion first.

### What we don't accept

- **Drive-by feature additions.** If there's no Discussion, there's no PR.
- **Speculative refactors** that don't solve a concrete problem.
- **Dependency upgrades** outside of Renovate/Dependabot. We manage these centrally.
- **"Improvements"** to code you haven't been asked to change (added logging, extra error handling, style changes in unrelated files).

## Changesets

Every PR that changes the behavior of a published package needs a **changeset** — a small Markdown file that describes the change for the CHANGELOG and determines the version bump. Without a changeset, the change won't trigger a package release.

### When you need one

- Bug fixes, features, refactors, or any other change that affects a published package's behavior or API.
- Changes that span multiple packages need one changeset listing all affected packages.
- If a PR makes more than one distinct change, add a separate changeset for each. Each one becomes its own CHANGELOG entry.

### When you don't

- Docs-only changes, test-only changes, CI/tooling changes, or changes to demo apps and templates (these are in the changeset ignore list).

### How to add one

Run from the repo root:

```bash
pnpm changeset
```

This walks you through selecting the affected package(s), the semver bump type, and a description. It creates a randomly-named `.md` file in `.changeset/`.

You can also create one manually — see the existing files in `.changeset/` for the format.

### Writing the description

Start with a present-tense verb describing what the change does, as if completing "This PR...":

- **Adds** — a new feature or capability
- **Fixes** — a bug fix
- **Updates** — an enhancement to existing behavior
- **Removes** — removed functionality
- **Refactors** — internal restructuring with no behavior change

Focus on how the change affects someone **using** the package, not implementation details. The description ends up in the CHANGELOG, which people read once during upgrades.

**Patch** (bug fixes, refactors, small improvements):

```markdown
---
"emdash": patch
---

Fixes CLI `--json` flag so JSON output is clean. Log messages now go to stderr when `--json` is set.
```

**Minor** (new features, non-breaking additions):

```markdown
---
"emdash": minor
---

Adds `scheduled_at` field to content entries, enabling scheduled publishing via the admin UI.
```

**Major** (breaking changes) — include migration guidance:

```markdown
---
"emdash": major
---

Removes the `legacyAuth` option from the integration config. All sites must use passkey authentication.

To migrate, remove `legacyAuth: true` from your `emdash()` config in `astro.config.mjs`.
```

### Which packages?

Only published packages need changesets. Demos, templates, docs, and test fixtures are excluded. The main packages are:

- `emdash` (core)
- `@emdash-cms/admin`, `@emdash-cms/auth`, `@emdash-cms/cloudflare`, `@emdash-cms/blocks`
- `create-emdash`
- First-party plugins (`@emdash-cms/plugin-*`)

When in doubt, run `pnpm changeset` and it will only show packages that aren't ignored.

## Commits and PRs

- Branch from `main`.
- Commit messages: describe _why_, not just _what_.
- Fill out the PR template completely. PRs with an empty template will be closed.
- Ensure `pnpm typecheck` and `pnpm --silent lint:json` pass before pushing.
- Run relevant tests.

## What's Intentionally Missing (For Now)

These are known gaps -- don't try to fix them unless specifically asked:

- **Rate limiting** -- no brute-force protection on auth endpoints
- **Password auth** -- passkeys + magic links + OAuth only, by design
- **Plugin marketplace** -- architecture exists, runtime installation is post-beta
- **Real-time collaboration** -- planned for v1

## Getting Help

- Read `AGENTS.md` for architecture and code patterns
- Check the [documentation site](https://docs.emdashcms.com) for guides and API reference
- Open an issue or ask in the chat

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

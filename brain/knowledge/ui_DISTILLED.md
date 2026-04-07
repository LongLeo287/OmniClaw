---
id: ui
type: knowledge
owner: OA_Triage
---
# ui
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "Talos Pioneers",
  "type": "module",
  "private": true,
  "scripts": {
    "build": "nuxt build",
    "dev": "nuxt dev --dotenv .env.local",
    "generate": "nuxt generate",
    "preview": "npm run build && wrangler dev",
    "postinstall": "nuxt prepare",
    "deploy:staging": "export $(cat ../ui-stag-deployconfig/.env.staging | xargs) && nuxt build && wrangler deploy --config ../ui-stag-deployconfig/wrangler.jsonc",
    "deploy:production": "export $(cat .env.production | xargs) && nuxt build && wrangler deploy",
    "cf-typegen": "wrangler types",
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "format": "prettier --check .",
    "format:fix": "prettier --write . --fix"
  },
  "dependencies": {
    "@nuxt/content": "^3.8.2",
    "@nuxt/eslint": "^1.10.0",
    "@nuxt/fonts": "^0.12.1",
    "@nuxt/scripts": "^0.13.0",
    "@nuxtjs/i18n": "^10.2.0",
    "@nuxtjs/seo": "^3.2.2",
    "@sentry/nuxt": "^10.27.0",
    "@unhead/vue": "^2.0.19",
    "@vueuse/core": "^14.0.0",
    "better-sqlite3": "^12.5.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "embla-carousel-vue": "^8.6.0",
    "eslint": "^9.39.1",
    "lucide-vue-next": "^0.554.0",
    "nuxt": "^4.2.1",
    "nuxt-auth-sanctum": "^1.4.2",
    "nuxt-easy-lightbox": "^1.1.0",
    "nuxt-lottie": "^1.0.8",
    "nuxt-sanctum-precognition": "^0.0.12",
    "reka-ui": "^2.6.0",
    "shadcn-nuxt": "^2.3.3",
    "tailwind-merge": "^3.4.0",
    "usemods-nuxt": "^1.15.0",
    "vue": "^3.5.24",
    "vue-draggable-plus": "^0.6.0",
    "vue-router": "^4.6.3",
    "vue-sonner": "^2.0.9"
  },
  "devDependencies": {
    "@tailwindcss/vite": "^4.1.17",
    "nitro-cloudflare-dev": "^0.2.2",
    "nitropack": "^2.12.9",
    "prettier": "3.6.2",
    "shadcn-vue": "^2.3.3",
    "tailwindcss": "^4.1.17",
    "tw-animate-css": "^1.4.0",
    "typescript": "^5.9.3",
    "wrangler": "^4.59.3"
  }
}

```

### File: README.md
```md
# Talos Pioneers Frontend

Talos Pioneers is the frontend application for a blueprint sharing platform for **Arknights Endfield**. The platform allows players to create, share, like, and comment on game blueprints (base designs/builds) using shareable codes that can be pasted directly into the game. Users can organize blueprints into collections, manage game-related facilities and items, and interact with the community through comments and likes.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Environment Variables](#environment-variables)
- [Development](#development)
- [Features & Pages](#features--pages)
- [Components](#components)
- [Internationalization](#internationalization)
- [Deployment](#deployment)
- [Testing](#testing)
- [Additional Information](#additional-information)

## Tech Stack

- **Framework**: Nuxt 4
- **Language**: TypeScript
- **Styling**: Tailwind CSS 4
- **UI Components**: shadcn-nuxt
- **Authentication**: nuxt-auth-sanctum (Laravel Sanctum integration)
- **Form Validation**: nuxt-sanctum-precognition
- **Internationalization**: @nuxtjs/i18n (14 languages)
- **SEO**: @nuxtjs/seo
- **Icons**: lucide-vue-next
- **Deployment**: Cloudflare Workers (nitro-cloudflare-dev)
- **Package Manager**: npm/bun
- **Other Packages**:
  - class-variance-authority
  - clsx
  - tailwind-merge
  - @nuxt/fonts

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** 18 or higher
- **npm** or **bun** (package manager)
- **Backend API** running (see backend README for setup instructions)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd frontend
```

### 2. Install Dependencies

Install Node.js dependencies:

```bash
npm install
```

Or using bun:

```bash
bun install
```

### 3. Environment Configuration

Create an environment file:

```bash
cp .env.example .env
```

Edit the `.env` file with your configuration. See [Environment Variables](#environment-variables) section for details.

### 4. Development Server

Start the development server:

```bash
npm run dev
```

Or using bun:

```bash
bun run dev
```

The development server will start on `http://localhost:3000` (or the configured host in `nuxt.config.ts`).

## Environment Variables

### Required Variables

```env
API_URL=http://localhost:8000
```

The `API_URL` should point to your backend Laravel API server.

### Optional Variables

TBD

## Development

### Running the Development Server

Start the development server:

```bash
npm run dev
```

The server will be available at the configured host (default: `blueprints.test` as configured in `nuxt.config.ts`).

### Building for Production

Build the application for production:

```bash
npm run build
```

This creates an optimized production build in the `.output` directory.

### Preview Production Build

Preview the production build locally:

```bash
npm run preview
```

This builds the application and starts a local preview server using Wrangler.

### Code Structure

The application follows Nuxt 4 conventions:

- **Pages** (`app/pages/`): File-based routing
- **Components** (`app/components/`): Reusable Vue components
- **Layouts** (`app/layouts/`): Layout components
- **Assets** (`app/assets/`): CSS and other static assets
- **Plugins** (`app/plugins/`): Nuxt plugins
- **i18n** (`i18n/locales/`): Translation files
- **Public** (`public/`): Static files served as-is

### TypeScript

The project uses TypeScript for type safety. Type definitions are automatically generated by Nuxt.

### Styling

The application uses Tailwind CSS 4 with a CSS-first configuration approach. Styles are defined in `app/assets/css/tailwind.css`.

## Features & Pages

### Blueprints

- **List Page** (`/blueprints`): Browse and filter published blueprints
- **Detail Page** (`/blueprints/[id]`): View blueprint details, comments, and interactions
- **Create Page** (`/blueprints/create`): Create a new blueprint
- **Edit Page** (`/blueprints/[id]/edit`): Edit an existing blueprint

### Collections

- **List Page** (`/collections`): Browse blueprint collections
- **Detail Page** (`/collections/[id]`): View collection details and blueprints
- **Create Page** (`/collections/create`): Create a new collection
- **Edit Page** (`/collections/[id]/edit`): Edit an existing collection

### Profile

- **Profile Page** (`/profile`): View and edit user profile
- **My Blueprints** (`/profile/blueprints`): Manage user's blueprints
- **My Collections** (`/profile/collections`): Manage user's collections

### Authentication

- **Login** (`/login`): User login with email/password or OAuth
- **Register** (`/register`): User registration

### Additional Features

TBD

## Components

### Auth Components

- **LoginForm** (`app/components/auth/LoginForm.vue`): Login form component
- **RegisterForm** (`app/components/auth/RegisterForm.vue`): Registration form component
- **ProfileEdit** (`app/components/auth/ProfileEdit.vue`): Profile editing component

### Blueprint Components

- **BlueprintCard** (`app/components/blueprints/BlueprintCard.vue`): Blueprint card display
- **BlueprintForm** (`app/components/blueprints/BlueprintForm.vue`): Blueprint creation/edit form
- **BlueprintList** (`app/components/blueprints/BlueprintList.vue`): Blueprint list display

### Collection Components

- **CollectionCard** (`app/components/collections/CollectionCard.vue`): Collection card display
- **CollectionForm** (`app/components/collections/CollectionForm.vue`): Collection creation/edit form
- **CollectionList** (`app/components/collections/CollectionList.vue`): Collection list display

### UI Components

The application uses **shadcn-nuxt** for UI components. Components are located in `app/components/ui/`.

TBD - Document specific UI components as they are developed.

## Internationalization

The application supports 14 languages using `@nuxtjs/i18n`:

- English (en) - Default
- Japanese (ja)
- Korean (ko)
- Chinese Traditional (zh-TW)
- Chinese Simplified (zh-CN)
- Spanish (es)
- Portuguese (pt)
- French (fr)
- German (de)
- Russian (ru)
- Italian (it)
- Indonesian (id)
- Thai (th)
- Vietnamese (vi)

### Configuration

Internationalization is configured in `nuxt.config.ts` with:
- Strategy: `prefix` (language prefix in URL)
- Browser language detection with cookie support
- Translation files located in `i18n/locales/`

### Translation Files

Translation files are JSON format and located in `i18n/locales/`:
- `en.json` - English
- `ja.json` - Japanese
- `ko.json` - Korean
- `zh-TW.json` - Chinese Traditional
- `zh-CN.json` - Chinese Simplified
- `es.json` - Spanish
- `pt.json` - Portuguese
- `fr.json` - French
- `de.json` - German
- `ru.json` - Russian
- `it.json` - Italian
- `id.json` - Indonesian
- `th.json` - Thai
- `vi.json` - Vietnamese

## Deployment

The application is configured for deployment to **Cloudflare Workers** using Nitro.

### Build for Deployment

```bash
npm run build
```

### Deploy to Cloudflare

```bash
npm run deploy
```

This builds the application and deploys it using Wrangler.

### Wrangler Configuration

Deployment configuration is defined in `wrangler.jsonc`. The application uses:
- Cloudflare Workers runtime
- Static asset binding
- Observability enabled

### Environment Setup

TBD - Document production environment variables and configuration.

### Custom Domain

TBD - Document custom domain setup.

## Testing

TBD

## Additional Information

### Authentication

The frontend uses **nuxt-auth-sanctum** for authentication with the Laravel backend:
- Cookie-based authentication via Laravel Sanctum
- Automatic token management
- Protected routes support

### Form Validation

The application uses **nuxt-sanctum-precognition** for real-time form validation:
- Server-side validation feedback
- Real-time error display
- Integration with Laravel Precognition

### SEO

The application uses **@nuxtjs/seo** for SEO optimization:
- Meta tags management
- Open Graph tags
- Twitter Card tags
- Sitemap generation (TBD)

### Fonts

The application uses **@nuxt/fonts** for font optimization. Font files are located in `public/fonts/`.

### API Integration

The frontend communicates with the backend API via:
- RESTful API endpoints under `/api/v1/`
- Authentication handled by nuxt-auth-sanctum
- Form validation via nuxt-sanctum-precognition

## Contributing

TBD

## License

TBD

```

### File: bookmark-ux-patterns.md
```md
---
id: bookmark-ux-patterns
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:25.500829
---

# Bookmark UX Patterns — Knowledge Base

## Description
A collection of industry-standard UX patterns and competitive research for bookmark management, focused on navigation, search, and intuitive contextual actions.

## Industry Standards

### Tree Navigation
- Expand/collapse folders with click
- Visual indentation for nesting
- Folder icons vs bookmark icons
- Drag handle for reordering

### Search Patterns
- Always-visible search bar
- Instant search (debounced)
- Highlight matching text
- Show result count
- "No results" empty state

### Context Actions
- Right-click context menu
- Hover actions (icon buttons)
- Keyboard shortcuts
- Bulk selection with checkboxes

## UX Research Insights (from ktab, pinchtab references)

### What Users Want Most
1. Fast search (sub-100ms feel)
2. Visual organization (folders, colors, icons)
3. Quick add (keyboard shortcut)
4. Tag/label system
5. Recently visited sorting

### Pain Points with Current Bookmark Managers
- Chrome default: Too basic, no search within
- Raindrop.io: Needs account, paid features
- Current extension: Missing tags, AI, keyboard nav

## Competitor Analysis

| Feature | Chrome Native | Raindrop | Pocket | Our Target |
|---------|--------------|---------|--------|-----------|
| Search | Basic | Full-text | Full-text | Semantic AI |
| Tags | No | Yes | Yes | AI auto-tag |
| Folders | Yes | Yes | Collections | Smart folders |
| Keyboard | Minimal | Good | Basic | Full |
| AI | No | No | No | Yes |
| Offline | Yes | Partial | Yes | Yes |
| Price | Free | Freemium | Freemium | Free |

```

### File: components.json
```json
{
  "$schema": "https://shadcn-vue.com/schema.json",
  "style": "new-york",
  "typescript": true,
  "tailwind": {
    "config": "",
    "css": "app/assets/css/tailwind.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "iconLibrary": "lucide",
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "composables": "@/composables"
  },
  "registries": {}
}

```

### File: env.d.ts
```ts
/// <reference types="./worker-configuration.d.ts" />

declare module "h3" {
  interface H3EventContext {
    cf: CfProperties;
    cloudflare: {
      request: Request;
      env: Env;
      context: ExecutionContext;
    };
  }
}

export {};

```

### File: ki_2026_03_22_gaia_ui.md
```md
---
id: KI-2026-03-22-gaia-ui
source: https://github.com/theexperiencecompany/gaia-ui
type: REFERENCE
domain: ['ui', 'react', 'design']
dept: engineering
agents: ['visual_excellence']
created: 2026-03-22T22:37:16.443912
---

# Gaia UI

> AI-native React components: streaming chat, agent status, tool call displays, timeline. Shadcn/RadixUI based. 300★.

**Source:** [https://github.com/theexperiencecompany/gaia-ui](https://github.com/theexperiencecompany/gaia-ui)  
**Type:** REFERENCE | **Dept:** engineering  
**Relevant Agents:** visual_excellence

## OmniClaw Notes
Design reference for ClawTask UI upgrades. Key components: streaming response display, agent activity timeline. Use as inspiration not dependency.

## Install / Use
```
npm install @gaia/ui
```

## Key Concepts
_See source URL_

## Cross-links
- SKILL.md: `plugins/22-gaia-ui/SKILL.md`
- FAST_INDEX: keyword `gaia_ui`

```

### File: ki_2026_03_22_kerminal.md
```md
---
id: KI-2026-03-22-kerminal
source: https://github.com/klpod221/kerminal
type: REFERENCE
domain: ['ui', 'ide']
dept: engineering
agents: []
stars: 800
security_gate: PASS (community_vetted)
compatible_ai_os: True
created: 2026-03-22T23:02:23.338520
---

# Kerminal IDE

> Web-based terminal + IDE in browser. Docker-based.

**Source:** [https://github.com/klpod221/kerminal](https://github.com/klpod221/kerminal)  
**Stars:** 800 | **Type:** REFERENCE | **Dept:** engineering  
**OmniClaw Compatible:** ✅ Compatible

## Phase 3 Classification
- **knowledge_type:** `REFERENCE`
- **domains:** ui, ide
- **target_dept:** engineering
- **relevant_agents:** _(none assigned)_
- **security_gate:** PASS — community_vetted

## OmniClaw Notes
REFERENCE — similar to ClawTask terminal panel. Study for terminal UI improvements.

## Integration
📖 KI entry only — no plugin clone needed

---
*Ingested: 2026-03-22T23:02:23.338520 via knowledge-ingest.md Phase 1-3*

```

### File: ki_2026_03_22_ktab.md
```md
---
id: KI-2026-03-22-ktab
source: https://github.com/dunkbing/ktab
type: REFERENCE
domain: ['ui', 'browser-ext']
dept: engineering
agents: []
stars: 400
security_gate: PASS (community_vetted)
compatible_ai_os: False
created: 2026-03-22T23:02:23.338520
---

# kTab New Tab

> Custom new tab page with quick links, search, weather. Browser extension.

**Source:** [https://github.com/dunkbing/ktab](https://github.com/dunkbing/ktab)  
**Stars:** 400 | **Type:** REFERENCE | **Dept:** engineering  
**OmniClaw Compatible:** ❌ Not compatible

## Phase 3 Classification
- **knowledge_type:** `REFERENCE`
- **domains:** ui, browser-ext
- **target_dept:** engineering
- **relevant_agents:** _(none assigned)_
- **security_gate:** PASS — community_vetted

## OmniClaw Notes
REFERENCE — not relevant to OmniClaw operations directly.

## Integration
📖 KI entry only — no plugin clone needed

---
*Ingested: 2026-03-22T23:02:23.338520 via knowledge-ingest.md Phase 1-3*

```

### File: nuxt.config.ts
```ts
import tailwindcss from '@tailwindcss/vite'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	compatibilityDate: '2025-07-15',
	devtools: { enabled: false },

	devServer: {
		host: 'blueprints.test',
	},

	site: {
		name: 'Talos Pioneers',
		indexable: process.env.CLOUDFLARE_ENV === 'staging' ? false : true,
	},

	ssr: true,
	css: ['~/assets/css/tailwind.css'],

	vite: {
		plugins: [
			tailwindcss(),
			{
				name: 'suppress-known-warnings',
				apply: 'build',
				configResolved(config) {
					const originalOnWarn = config.build.rollupOptions.onwarn
					config.build.rollupOptions.onwarn = (warning, warn) => {
						if (
							warning.code === 'SOURCEMAP_BROKEN' &&
							warning.plugin === '@tailwindcss/vite:generate:build'
						)
							return
						if (warning.code === 'EVAL' && warning.id?.includes('lottie-web')) return
						if (originalOnWarn) {
							originalOnWarn(warning, warn)
						} else {
							warn(warning)
						}
					}
				},
			},
		],
		build: {
			chunkSizeWarningLimit: 4000,
		},
	},

	nitro: {
		preset: 'cloudflare_module',

		cloudflare: {
			wrangler: {
				name: `talos-pioneers${process.env.CLOUDFLARE_ENV === 'staging' ? '-staging' : ''}`,
				workers_dev: false,
				preview_urls: false,
				routes: [
					{
						pattern: process.env.BASE_DOMAIN,
						custom_domain: true,
					},
				],
				vars: {
					API_URL: process.env.API_URL,
					BASE_URL: process.env.BASE_URL,
				},
			},
			deployConfig: true,
			nodeCompat: true,
		},
	},

	modules: [
		'nitro-cloudflare-dev',
		'@nuxtjs/i18n',
		'nuxt-auth-sanctum',
		'nuxt-sanctum-precognition',
		'@nuxtjs/seo',
		'shadcn-nuxt',
		'@nuxt/fonts',
		'usemods-nuxt',
		'@sentry/nuxt/module',
		'@nuxt/eslint',
		'nuxt-lottie',
		'nuxt-easy-lightbox',
		'@nuxt/scripts',
	],

	runtimeConfig: {
		public: {
			sentry: {
				dsn: process.env.NUXT_PUBLIC_SENTRY_DSN,
			},
		},
	},

	i18n: {
		baseUrl: process.env.BASE_URL,
		strategy: 'prefix',
		detectBrowserLanguage: {
			useCookie: true,
			cookieKey: 'talos_i18n_redirected',
			redirectOn: 'root',
		},
		defaultLocale: 'en',
		locales: [
			{
				code: 'en',
				name: 'English',
				file: 'en.json',
				language: 'en',
			},
			{
				code: 'ja',
				name: '日本語',
				file: 'ja.json',
				language: 'ja',
			},
			{
				code: 'ko',
				name: '한국어',
				file: 'ko.json',
				language: 'ko',
			},
			{
				code: 'zh-TW',
				name: '繁體中文',
				file: 'zh-TW.json',
				language: 'zh-TW',
			},
			{
				code: 'zh-CN',
				name: '简体中文',
				file: 'zh-CN.json',
				language: 'zh-CN',
			},
			{
				code: 'es',
				name: 'Español',
				file: 'es.json',
				language: 'es',
			},
			{
				code: 'pt',
				name: 'Português',
				file: 'pt.json',
				language: 'pt',
			},
			{
				code: 'fr',
				name: 'Français',
				file: 'fr.json',
				language: 'fr',
			},
			{
				code: 'de',
				name: 'Deutsch',
				file: 'de.json',
				language: 'de',
			},
			{
				code: 'ru',
				name: 'Русский',
				file: 'ru.json',
				language: 'ru',
			},
			{
				code: 'it',
				name: 'Italiano',
				file: 'it.json',
				language: 'it',
			},
			{
				code: 'id',
				name: 'Indonesia',
				file: 'id.json',
				language: 'id',
			},
			{
				code: 'th',
				name: 'ภาษาไทย',
				file: 'th.json',
				language: 'th',
			},
			{
				code: 'vi',
				name: 'Tiếng Việt',
				file: 'vi.json',
				language: 'vi',
			},
		],
	},

	sanctum: {
		baseUrl: process.env.API_URL,
		redirectIfAuthenticated: false,
		redirect: {
			onLogin: false,
		},
	},

	fonts: {
		families: [
			{
				name: 'HarmonyOS_Sans',
				provider: 'local',
				weights: [100, 300, 400, 500, 700, 900, 1000],
				// fallbacks: ['sans-serif'],
			},
			{
				name: 'HarmonyOS_Sans_SC',
				provider: 'local',
				weights: [100, 300, 400, 500, 700, 900, 1000],
				// fallbacks: ['sans-serif'],
			},
			{
				name: 'HarmonyOS_Sans_TC',
				provider: 'local',
				weights: [100, 300, 400, 500, 700, 900, 1000],
				// fallbacks: ['sans-serif'],
			},
			{
				name: 'EndfieldByButan',
				provider: 'local',
				src: '/fonts/EndfieldByButan.ttf',
				fallbacks: ['sans-serif'],
			},
			{
				name: 'Noto Sans JP',
				provider: 'google',
				weights: [100, 300, 400, 500, 700, 900],
			},
			{
				name: 'DM Sans',
				provider: 'google',
				weights: [100, 300, 400, 500, 700, 900],
			},
		],
	},

	sentry: {
		sourceMapsUploadOptions: {
			org: 'talos-pioneers',
			project: 'talos-pioneers-frontend',
			authToken: process.env.SENTRY_AUTH_TOKEN,
		},
	},

	scripts: {
		registry: {
			googleTagManager: {
				id: 'GTM-MMCT5C3R',
			},
		},
	},

	sourcemap: {
		client: 'hidden',
	},
})

```

### File: sentry.client.config.ts
```ts
import * as Sentry from "@sentry/nuxt";

Sentry.init({
  // If set up, you can use your runtime config here
  // dsn: useRuntimeConfig().public.sentry.dsn,
  dsn: "https://b52f0ced6ca2217c58fd74ee4a77c8d5@o4510417268113408.ingest.us.sentry.io/4510423228940288",

  // We recommend adjusting this value in production, or using tracesSampler
  // for finer control
  tracesSampleRate: 1.0,

  // Enable logs to be sent to Sentry
  enableLogs: true,

  // Enable sending of user PII (Personally Identifiable Information)
  // https://docs.sentry.io/platforms/javascript/guides/nuxt/configuration/options/#sendDefaultPii
  sendDefaultPii: true,

  // Setting this option to true will print useful information to the console while you're setting up Sentry.
  debug: false,
});

```

### File: tsconfig.json
```json
{
  // https://nuxt.com/docs/guide/concepts/typescript
  "files": [],
  "references": [
    {
      "path": "./.nuxt/tsconfig.app.json"
    },
    {
      "path": "./.nuxt/tsconfig.server.json"
    },
    {
      "path": "./.nuxt/tsconfig.shared.json"
    },
    {
      "path": "./.nuxt/tsconfig.node.json"
    }
],
"compilerOptions": {
    "types": [
        "./worker-configuration.d.ts"
    ]
}
}

```

### File: .cursor\mcp.json
```json
{
  "mcpServers": {
    "shadcnVue": {
      "command": "npx",
      "args": [
        "shadcn-vue@latest",
        "mcp"
      ]
    },
    "Sentry": {
      "url": "https://mcp.sentry.dev/mcp/talos-pioneers/talos-pioneers-frontend"
    }
  }
}
```

### File: app\router.options.ts
```ts
import type { RouterConfig } from '@nuxt/schema'

// Only matches the main browse pages, not profile sub-pages
const isBrowsePage = (path: string) => {
	const clean = path.replace(/\/$/, '')
	const isRoot = /^\/[a-z]{2}(-[A-Z]{2,})?$/.test(clean)
	const isCollections = /^\/[a-z]{2}(-[A-Z]{2,})?\/collections$/.test(clean)
	return isRoot || isCollections
}

export default <RouterConfig>{
	scrollBehavior(to, from, savedPosition) {
		// Restore position on back/forward
		if (savedPosition) {
			return savedPosition
		}

		// Handle hash links
		if (to.hash) {
			return { el: to.hash }
		}

		// Same-path navigations (query-only changes like pagination): don't scroll
		if (to.path === from.path) {
			return false
		}

		// Browse page scroll is handled by browse-scroll.client.ts plugin
		// Return false to prevent default scroll-to-top
		if (from.name && isBrowsePage(to.path)) {
			return false
		}

		// Default: scroll to top
		return { top: 0 }
	},
}

```

### File: content\cookie-policy.md
```md
This Cookie Policy explains how Talos Pioneers ("**Company**," "**we**," "**us**," and "**our**") uses cookies and similar technologies to recognize you when you visit our website at [https://talospioneers.com](https://talospioneers.com) ("**Website**"). It explains what these technologies are and why we use them, as well as your rights to control our use of them.

  

In some cases we may use cookies to collect personal information, or that becomes personal information if we combine it with other information.

  

**

What are cookies?
-----------------

**

Cookies are small data files that are placed on your computer or mobile device when you visit a website. Cookies are widely used by website owners in order to make their websites work, or to work more efficiently, as well as to provide reporting information.

  

Cookies set by the website owner (in this case, Talos Pioneers) are called "first-party cookies." Cookies set by parties other than the website owner are called "third-party cookies." Third-party cookies enable third-party features or functionality to be provided on or through the website (e.g., advertising, interactive content, and analytics). The parties that set these third-party cookies can recognize your computer both when it visits the website in question and also when it visits certain other websites.

  

**

Why do we use cookies?
----------------------

**

We use first- and third-party cookies for several reasons. Some cookies are required for technical reasons in order for our Website to operate, and we refer to these as "essential" or "strictly necessary" cookies. Other cookies also enable us to track and target the interests of our users to enhance the experience on our Online Properties. Third parties serve cookies through our Website for advertising, analytics, and other purposes. This is described in more detail below.

  

**

How can I control cookies?
--------------------------

**

You have the right to decide whether to accept or reject cookies. You can exercise your cookie rights by setting your preferences in the Cookie Consent Manager. The Cookie Consent Manager allows you to select which categories of cookies you accept or reject. Essential cookies cannot be rejected as they are strictly necessary to provide you with services.

  

The Cookie Consent Manager can be found in the notification banner and on our Website. If you choose to reject cookies, you may still use our Website though your access to some functionality and areas of our Website may be restricted. You may also set or amend your web browser controls to accept or refuse cookies.

  

The specific types of first- and third-party cookies served through our Website and the purposes they perform are described in the table below (please note that the specific cookies served may vary depending on the specific Online Properties you visit):**  

### Essential website cookies:

**These cookies are strictly necessary to provide you with services available through our Website and to use some of its features, such as access to secure areas.

Name:

\_\_cf\_bm

Purpose:

Cloudflare places the cookie on end-user devices that access customer sites protected by Bot Management or Bot Fight Mode.

Provider:

.talospioneers.com

Service:

CloudFlare [View Service Privacy Policy](https://www.cloudflare.com/privacypolicy/)

Type:

server\_cookie

Expires in:

30 minutes

**  

### Performance and functionality cookies:

**These cookies are used to enhance the performance and functionality of our Website but are non-essential to their use. However, without these cookies, certain functionality (like videos) may become unavailable.

  

Name:

\_cfuvid

Purpose:

This cookie is set by Cloudflare to enhance security and performance. It helps identify trusted web traffic and ensures a secure browsing experience for users.

Provider:

.talospioneers.com

Service:

Cloudflare [View Service Privacy Policy](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/)

Type:

server\_cookie

Expires in:

session

Name:

XSRF-TOKEN

Purpose:

This cookie is written to help with site security in preventing Cross-Site Request Forgery attacks.

Provider:

.talospioneers.com

Service:

Advertiser's website domain [View Service Privacy Policy](None)

Type:

server\_cookie

Expires in:

2 hours

**  

### Analytics and customization cookies:

**These cookies collect information that is used either in aggregate form to help us understand how our Website is being used or how effective our marketing campaigns are, or to help us customize our Website for you.

  

Name:

s7

Purpose:

Gather data regarding site usage and user behavior on the website.

Provider:

.talospioneers.com

Service:

Adobe Analytics

Type:

server\_cookie

Expires in:

2 hours

Name:

s7

Purpose:

Gather data regarding site usage and user behavior on the website.

Provider:

talospioneers.com

Service:

Adobe Analytics

Type:

server\_cookie

Expires in:

11 months 30 days

**  

### Unclassified cookies:

**These are cookies that have not yet been categorized. We are in the process of classifying these cookies with the help of their providers.

  

Name:

qzldFuPoKzRdeQ2o5vIizpw7ztIgUcj7GexmvfIn

Provider:

.talospioneers.com

Type:

server\_cookie

Expires in:

2 hours

  

**

How can I control cookies on my browser?
----------------------------------------

**

As the means by which you can refuse cookies through your web browser controls vary from browser to browser, you should visit your browser's help menu for more information. The following is information about how to manage cookies on the most popular browsers:[](https://support.google.com/chrome/answer/95647#zippy=%2Callow-or-block-cookies)

*   [Chrome](https://support.google.com/chrome/answer/95647#zippy=%2Callow-or-block-cookies)
*   [Internet Explorer](https://support.microsoft.com/en-us/windows/delete-and-manage-cookies-168dab11-0753-043d-7c16-ede5947fc64d)
*   [Firefox](https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop?redirectslug=enable-and-disable-cookies-website-preferences&redirectlocale=en-US)
*   [Safari](https://support.apple.com/en-ie/guide/safari/sfri11471/mac)
*   [Edge](https://support.microsoft.com/en-us/windows/microsoft-edge-browsing-data-and-privacy-bb8174ba-9d73-dcf2-9b4a-c582b4e640dd)
*   [Opera](https://help.opera.com/en/latest/web-preferences/)

In addition, most advertising networks offer you a way to opt out of targeted advertising. If you would like to find out more information, please visit:[](http://www.aboutads.info/choices/)

*   [Digital Advertising Alliance](http://www.aboutads.info/choices/)[](https://youradchoices.ca/)
*   [Digital Advertising Alliance of Canada](https://youradchoices.ca/)[](http://www.youronlinechoices.com/)
*   [European Interactive Digital Advertising Alliance](http://www.youronlinechoices.com/)

  

**

What about other tracking technologies, like web beacons?
---------------------------------------------------------

**

Cookies are not the only way to recognize or track visitors to a website. We may use other, similar technologies from time to time, like web beacons (sometimes called "tracking pixels" or "clear gifs"). These are tiny graphics files that contain a unique identifier that enables us to recognize when someone has visited our Website or opened an email including them. This allows us, for example, to monitor the traffic patterns of users from one page within a website to another, to deliver or communicate with cookies, to understand whether you have come to the website from an online advertisement displayed on a third-party website, to improve site performance, and to measure the success of email marketing campaigns. In many instances, these technologies are reliant on cookies to function properly, and so declining cookies will impair their functioning.

  

**

Do you use Flash cookies or Local Shared Objects?
-------------------------------------------------

**

Websites may also use so-called "Flash Cookies" (also known as Local Shared Objects or "LSOs") to, among other things, collect and store information about your use of our services, fraud prevention, and for other site operations.

  

If you do not want Flash Cookies stored on your computer, you can adjust the settings of your Flash player to block Flash Cookies storage using the tools contained in the [Website Storage Settings Panel](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager07.html). You can also control Flash Cookies by going to the [Global Storage Settings Panel](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager03.html) and following the instructions (which may include instructions that explain, for example, how to delete existing Flash Cookies (referred to "information" on the Macromedia site), how to prevent Flash LSOs from being placed on your computer without your being asked, and (for Flash Player 8 and later) how to block Flash Cookies that are not being delivered by the operator of the page you are on at the time).

  

Please note that setting the Flash Player to restrict or limit acceptance of Flash Cookies may reduce or impede the functionality of some Flash applications, including, potentially, Flash applications used in connection with our services or online content.

  

**

Do you serve targeted advertising?
----------------------------------

**

Third parties may serve cookies on your computer or mobile device to serve advertising through our Website. These companies may use information about your visits to this and other websites in order to provide relevant advertisements about goods and services that you may be interested in. They may also employ technology that is used to measure the effectiveness of advertisements. They can accomplish this by using cookies or web beacons to collect information about your visits to this and other sites in order to provide relevant advertisements about goods and services of potential interest to you. The information collected through this process does not enable us or them to identify your name, contact details, or other details that directly identify you unless you choose to provide these.

  

**

How often will you update this Cookie Policy?
---------------------------------------------

**

We may update this Cookie Policy from time to time in order to reflect, for example, changes to the cookies we use or for other operational, legal, or regulatory reasons. Please therefore revisit this Cookie Policy regularly to stay informed about our use of cookies and related technologies.

  

The date at the top of this Cookie Policy indicates when it was last updated.

  

**

Where can I get further information?
------------------------------------

**

If you have any questions about our use of cookies or other technologies, please contact us at :

  

talospioneers@gmail.com

[](https://app.termly.io/dsar/2acfb562-dadb-451d-875b-1fd35820604f)
```

### File: content\privacy-policy.md
```md
This Privacy Notice for Talos Pioneers ("**we**," "**us**," or "**our**" ), describes how and why we might access, collect, store, use, and/or share ("**process**") your personal information when you use our services ( "**Services**"), including when you:

*   Visit our website at [https://talospioneers.com](https://talospioneers.com) or any website of ours that links to this Privacy Notice

*   Engage with us in other related ways, including any marketing or events

**Questions or concerns?** Reading this Privacy Notice will help you understand your privacy rights and choices. We are responsible for making decisions about how your personal information is processed. If you do not agree with our policies and practices, please do not use our Services.

  

  

**

SUMMARY OF KEY POINTS
---------------------

**

**_This summary provides key points from our Privacy Notice, but you can find out more details about any of these topics by clicking the link following each key point or by using our_** [**_table of contents_**](#toc) **_below to find the section you are looking for._**

  

**What personal information do we process?** When you visit, use, or navigate our Services, we may process personal information depending on how you interact with us and the Services, the choices you make, and the products and features you use. Learn more about [personal information you disclose to us](#personalinfo).

  

**Do we process any sensitive personal information?** Some of the information may be considered "special" or "sensitive" in certain jurisdictions, for example your racial or ethnic origins, sexual orientation, and religious beliefs. We do not process sensitive personal information.

  

**Do we collect any information from third parties?** We do not collect any information from third parties.

  

**How do we process your information?** We process your information to provide, improve, and administer our Services, communicate with you, for security and fraud prevention, and to comply with law. We may also process your information for other purposes with your consent. We process your information only when we have a valid legal reason to do so. Learn more about [how we process your information](#infouse).

  

**In what situations and with which types of parties do we share personal information?** We may share information in specific situations and with specific categories of third parties. Learn more about [when and with whom we share your personal information](#whoshare).

  

**How do we keep your information safe?** We have adequate organizational and technical processes and procedures in place to protect your personal information. However, no electronic transmission over the internet or information storage technology can be guaranteed to be 100% secure, so we cannot promise or guarantee that hackers, cybercriminals, or other unauthorized third parties will not be able to defeat our security and improperly collect, access, steal, or modify your information. Learn more about [how we keep your information safe](#infosafe).

  

**What are your rights?** Depending on where you are located geographically, the applicable privacy law may mean you have certain rights regarding your personal information. Learn more about [your privacy rights](#privacyrights).

  

**How do you exercise your rights?** The easiest way to exercise your rights is by visiting [talospioneers@gmail.com](mailto:talospioneers@gmail.com) , or by contacting us. We will consider and act upon any request in accordance with applicable data protection laws.

  

Want to learn more about what we do with any information we collect? [Review the Privacy Notice in full](#toc).

  

  

**

TABLE OF CONTENTS
-----------------

**   

[1\. WHAT INFORMATION DO WE COLLECT?](#infocollect)

[2\. HOW DO WE PROCESS YOUR INFORMATION?](#infouse)

[3\. WHAT LEGAL BASES DO WE RELY ON TO PROCESS YOUR PERSONAL INFORMATION?](#legalbases)

[4\. WHEN AND WITH WHOM DO WE SHARE YOUR PERSONAL INFORMATION?](#whoshare)

[5\. DO WE USE COOKIES AND OTHER TRACKING TECHNOLOGIES?](#cookies)

[6\. HOW DO WE HANDLE YOUR SOCIAL LOGINS?](#sociallogins)

[7\. IS YOUR INFORMATION TRANSFERRED INTERNATIONALLY?](#intltransfers)

[8\. HOW LONG DO WE KEEP YOUR INFORMATION?](#inforetain)

[9\. HOW DO WE KEEP YOUR INFORMATION SAFE?](#infosafe)

[10\. WHAT ARE YOUR PRIVACY RIGHTS?](#privacyrights)

[11\. CONTROLS FOR DO-NOT-TRACK FEATURES](#DNT)

[12\. DO UNITED STATES RESIDENTS HAVE SPECIFIC PRIVACY RIGHTS?](#uslaws)

[13\. DO OTHER REGIONS HAVE SPECIFIC PRIVACY RIGHTS?](#otherlaws)

[14\. DO WE MAKE UPDATES TO THIS NOTICE?](#policyupdates)

[15\. HOW CAN YOU CONTACT US ABOUT THIS NOTICE?](#contact)

[16\. HOW CAN YOU REVIEW, UPDATE, OR DELETE THE DATA WE COLLECT FROM YOU?](#request)

  

  

**

1\. WHAT INFORMATION DO WE COLLECT?
-----------------------------------

****

### Personal information you disclose to us

****_In Short:_** _We collect personal information that you provide to us._

  

We collect personal information that you voluntarily provide to us when you register on the Services,  express an interest in obtaining information about us or our products and Services, when you participate in activities on the Services, or otherwise when you contact us.

  

**Personal Information Provided by You.** The personal information that we collect depends on the context of your interactions with us and the Services, the choices you make, and the products and features you use. The personal information we collect may include the following:

*   email addresses

*   usernames

*   passwords

**Sensitive Information.** We do not process sensitive information.

  

**Social Media Login Data.** We may provide you with the option to register with us using your existing social media account details, like your Facebook, X, or other social media account. If you choose to register in this way, we will collect certain profile information about you from the social media provider, as described in the section called "[HOW DO WE HANDLE YOUR SOCIAL LOGINS?](#sociallogins) " below.

  

All personal information that you provide to us must be true, complete, and accurate, and you must notify us of any changes to such personal information.

**

### Information automatically collected

****_In Short:_** _Some information — such as your Internet Protocol (IP) address and/or browser and device characteristics — is collected automatically when you visit our Services._

  

We automatically collect certain information when you visit, use, or navigate the Services. This information does not reveal your specific identity (like your name or contact information) but may include device and usage information, such as your IP address, browser and device characteristics, operating system, language preferences, referring URLs, device name, country, location, information about how and when you use our Services, and other technical information. This information is primarily needed to maintain the security and operation of our Services, and for our internal analytics and reporting purposes.

  

Like many businesses, we also collect information through cookies and similar technologies.

  

The information we collect includes:

*   _Log and Usage Data._ Log and usage data is service-related, diagnostic, usage, and performance information our servers automatically collect when you access or use our Services and which we record in log files. Depending on how you interact with us, this log data may include your IP address, device information, browser type, and settings and information about your activity in the Services (such as the date/time stamps associated with your usage, pages and files viewed, searches, and other actions you take such as which features you use), device event information (such as system activity, error reports (sometimes called "crash dumps"), and hardware settings).

*   _Device Data._ We collect device data such as information about your computer, phone, tablet, or other device you use to access the Services. Depending on the device used, this device data may include information such as your IP address (or proxy server), device and application identification numbers, location, browser type, hardware model, Internet service provider and/or mobile carrier, operating system, and system configuration information.

*   _Location Data._ We collect location data such as information about your device's location, which can be either precise or imprecise. How much information we collect depends on the type and settings of the device you use to access the Services. For example, we may use GPS and other technologies to collect geolocation data that tells us your current location (based on your IP address). You can opt out of allowing us to collect this information either by refusing access to the information or by disabling your Location setting on your device. However, if you choose to opt out, you may not be able to use certain aspects of the Services.

  

**

2\. HOW DO WE PROCESS YOUR INFORMATION?
---------------------------------------

****_In Short:_** _We process your information to provide, improve, and administer our Services, communicate with you, for security and fraud prevention, and to comply with law. We process the personal information for the following purposes listed below. We may also process your information for other purposes only with your prior explicit consent._

  

**We process your personal information for a variety of reasons, depending on how you interact with our Services, including:**

*   **To facilitate account creation and authentication and otherwise manage user accounts.** We may process your information so you can create and log in to your account, as well as keep your account in working order.

*   **To deliver and facilitate delivery of services to the user.** We may process your information to provide you with the requested service.

*   **To respond to user inquiries/offer support to users.** We may process your information to respond to your inquiries and solve any potential issues you might have with the requested service.

*   **To send administrative information to you.** We may process your information to send you details about our products and services, changes to our terms and policies, and other similar information.

*   **To enable user-to-user communications.** We may process your information if you choose to use any of our offerings that allow for communication with another user.

*   **To request feedback.** We may process your information when necessary to request feedback and to contact you about your use of our Services.

*   **To send you marketing and promotional communications.** We may process the personal information you send to us for our marketing purposes, if this is in accordance with your marketing preferences. You can opt out of our marketing emails at any time. For more information, see " [WHAT ARE YOUR PRIVACY RIGHTS?](#privacyrights) " below.

*   **To protect our Services.** We may process your information as part of our efforts to keep our Services safe and secure, including fraud monitoring and prevention.

*   **To identify usage trends.** We may process information about how you use our Services to better understand how they are being used so we can improve them.

*   **To save or protect an individual's vital interest.** We may process your information when necessary to save or protect an individual’s vital interest, such as to prevent harm.

  

**

3\. WHAT LEGAL BASES DO WE RELY ON TO PROCESS YOUR INFORMATION?
---------------------------------------------------------------

**_**In Short:** We only process your personal information when we believe it is necessary and we have a valid legal reason (i.e. , legal basis) to do so under applicable law, like with your consent, to comply with laws, to provide you with services to enter into or fulfill our contractual obligations, to protect your rights, or to fulfill our legitimate business interests._

  

_**If you are located in the EU or UK, this section applies to you.**_

  

The General Data Protection Regulation (GDPR) and UK GDPR require us to explain the valid legal bases we rely on in order to process your personal information. As such, we may rely on the following legal bases to process your personal information:

*   **Consent.** We may process your information if you have given us permission (i.e. , consent) to use your personal information for a specific purpose. You can withdraw your consent at any time. Learn more about [withdrawing your consent](#withdrawconsent).

*   **Performance of a Contract.** We may process your personal information when we believe it is necessary to fulfill our contractual obligations to you, including providing our Services or at your request prior to entering into a contract with you.

*   **Legitimate Interests.** We may process your information when we believe it is reasonably necessary to achieve our legitimate business interests and those interests do not outweigh your interests and fundamental rights and freedoms. For example, we may process your personal information for some of the purposes described in order to:

*   Send users information about special offers and discounts on our products and services

*   Analyze how our Services are used so we can improve them to engage and retain users

*   Diagnose problems and/or prevent fraudulent activities

*   Understand how our users use our products and services so we can improve user experience

*   **Legal Obligations.** We may process your information where we believe it is necessary for compliance with our legal obligations, such as to cooperate with a law enforcement body or regulatory agency, exercise or defend our legal rights, or disclose your information as evidence in litigation in which we are involved.  
    

*   **Vital Interests.** We may process your information where we believe it is necessary to protect your vital interests or the vital interests of a third party, such as situations involving potential threats to the safety of any person.

  

**_If you are located in Canada, this section applies to you._**

  

We may process your information if you have given us specific permission (i.e. , express consent) to use your personal information for a specific purpose, or in situations where your permission can be inferred (i.e. , implied consent). You can [withdraw your consent](#withdrawconsent) at any time.

  

In some exceptional cases, we may be legally permitted under applicable law to process your information without your consent, including, for example:

*   If collection is clearly in the interests of an individual and consent cannot be obtained in a timely way

*   For investigations and fraud detection and prevention

*   For business transactions provided certain conditions are met

*   If it is contained in a witness statement and the collection is necessary to assess, process,
... [TRUNCATED]
```

### File: public\cookie-content.html
```html
<strong><span><span><h1>COOKIE POLICY</h1></span></span></strong></div><div><span><strong><span><span>Last updated 
 </span></span></strong></span></div><div></div><div></div><div></div><div><span><span><span>This Cookie Policy
 explains how ("<strong>Company</strong>,"
 "<strong>we</strong>," "<strong>us</strong>," and "<strong>our</strong>") uses cookies and similar
 technologies to recognize you when you visit our website at </span></span><span></span><span><span> ("<strong>Website</strong>"). It explains what these technologies are
 and why we use them, as well as your rights to control our use of them.</span></span></span></div><div></div><div><span><span><span>In some cases we
 may use cookies to collect personal information, or that becomes personal information if we combine
 it with other information.</span></span></span></div><div></div><div><span><span><strong><span><h2>What are cookies?</h2></span></strong></span></span></div><div><span><span><span>Cookies are small
 data files that are placed on your computer or mobile device when you visit a website. Cookies are
 widely used by website owners in order to make their websites work, or to work more efficiently, as
 well as to provide reporting information.</span></span></span></div><div></div><div><span><span><span>Cookies set by the
 website owner (in this case, ) are called "first-party
 cookies." Cookies set by parties other than the website owner are called "third-party cookies."
 Third-party cookies enable third-party features or functionality to be provided on or through the
 website (e.g., advertising, interactive content, and analytics). The parties that set these
 third-party cookies can recognize your computer both when it visits the website in question and also
 when it visits certain other websites.</span></span></span></div><div></div><div><span><span><strong><span><h2>Why do we use cookies?</h2></span></strong></span></span></div><div><span><span><span>We use first- and third-party
 cookies for several reasons. Some cookies are required for technical reasons in order for our
 Website to operate, and we refer to these as "essential" or "strictly necessary" cookies. Other
 cookies also enable us to track and target the interests of our users to enhance the experience on
 our Online Properties. Third parties serve cookies through our
 Website for advertising, analytics, and other purposes. This is described in more detail below.</span></span></span></div><div></div><div><span><span><span><span><span id="control"><strong><span><h2>How can I control cookies?</h2></span></strong></span></span></span></span></span></div><div><span><span><span>You have the right
 to decide whether to accept or reject cookies. You can exercise your cookie rights by setting your
 preferences in the Cookie Consent Manager. The Cookie Consent Manager allows you to select which
 categories of cookies you accept or reject. Essential cookies cannot be rejected as they are
 strictly necessary to provide you with services.</span></span></span></div><div></div><div><span><span><span>The Cookie Consent
 Manager can be found in the notification banner and on our Website. If you choose to reject cookies,
 you may still use our Website though your access to some functionality and areas of our Website may
 be restricted. You may also set or amend your web browser controls to accept or refuse
 cookies.</span></span></span></div><div></div><div><span><span><span>The specific types
 of first- and third-party cookies served through our Website and the purposes they perform are
 described in the table below (please note that the specific </span><span>cookies served may vary depending on the specific Online Properties
 you visit):</span></span></span><span><span><strong><u><h3>Essential website cookies:</h3></u></strong></span></span><span><span><span>These cookies are
 strictly necessary to provide you with services available through our Website and to use some of its
 features, such as access to secure areas.</span></span></span></div><div><section><div><table><tbody><tr><th>Name:
 </th><td><span>__cf_bm</span></td></tr><tr><th>
 Purpose:</th><td><span>Cloudflare places the cookie on
 end-user devices that access customer sites protected by Bot Management or Bot Fight
 Mode.</span></td></tr><tr><th>
 Provider:</th><td><span>.talospioneers.com</span></td></tr><tr><th>
 Service:</th><td><span>CloudFlare <a href="https://www.cloudflare.com/privacypolicy/" target="_blank"><span>View Service Privacy Policy</span></a></span></td></tr><tr><th>Type:
 </th><td><span>server_cookie</span></td></tr><tr><th>Expires
 in:</th><td><span>30 minutes</span></td></tr></tbody></table></div></section><span><span><strong><u><h3>Performance and functionality cookies:</h3></u></strong></span></span><span><span>These cookies are used to enhance the performance and functionality of our
 Website but are non-essential to their use. However, without these cookies, certain functionality (like
 videos) may become unavailable.</span></span></div><div><div></div><div><span><span><section><div><table><tbody><tr><th>
 Name:</th><td><span>_cfuvid</span></td></tr><tr><th>
 Purpose:</th><td><span>This cookie is set by
 Cloudflare to enhance security and performance. It helps identify
 trusted web traffic and ensures a secure browsing experience for
 users.</span></td></tr><tr><th>
 Provider:</th><td><span>.talospioneers.com</span></td></tr><tr><th>
 Service:</th><td><span>Cloudflare <a
 href="https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/" target="_blank"><span>View Service Privacy
 Policy</span></a></span></td></tr><tr><th>
 Type:</th><td><span>server_cookie</span></td></tr><tr><th>
 Expires in:</th><td><span>session</span></td></tr></tbody></table></div></section><section><div><table><tbody><tr><th>
 Name:</th><td><span>XSRF-TOKEN</span></td></tr><tr><th>
 Purpose:</th><td><span>This cookie is written to
 help with site security in preventing Cross-Site Request Forgery
 attacks.</span></td></tr><tr><th>
 Provider:</th><td><span>.talospioneers.com</span></td></tr><tr><th>
 Service:</th><td><span>Advertiser's website
 domain <a href="None" target="_blank"><span>View Service Privacy
 Policy</span></a></span></td></tr><tr><th>
 Type:</th><td><span>server_cookie</span></td></tr><tr><th>
 Expires in:</th><td><span>2 hours</span></td></tr></tbody></table></div></section></span></span><span><span><strong><u><h3>Analytics and customization cookies:</h3></u></strong></span></span><span><span><span>These cookies
 collect information that is used either in aggregate form to help us understand how our Website
 is being used or how effective our marketing campaigns are, or to help us customize our Website
 for you.</span></span></span></div><div></div><div><span><section><div><table><tbody><tr><th>
 Name:</th><td><span>s7</span></td></tr><tr><th>
 Purpose:</th><td><span>Gather data regarding site
 usage and user behavior on the website.</span></td></tr><tr><th>
 Provider:</th><td><span>.talospioneers.com</span></td></tr><tr><th>
 Service:</th><td><span>Adobe Analytics </span></td></tr><tr><th>
 Type:</th><td><span>server_cookie</span></td></tr><tr><th>
 Expires in:</th><td><span>2 hours</span></td></tr></tbody></table></div></section></span></span></span><span><section><div><table><tbody><tr><th>
 Name:</th><td><span>s7</span></td></tr><tr><th>
 Purpose:</th><td><span>Gather data regarding site
 usage and user behavior on the website.</span></td></tr><tr><th>
 Provider:</th><td><span>talospioneers.com</span></td></tr><tr><th>
 Service:</th><td><span>Adobe Analytics </span></td></tr><tr><th>
 Type:</th><td><span>server_cookie</span></td></tr><tr><th>
 Expires in:</th><td><span>11 months 30 days</span></td></tr></tbody></table></div></section></span><span><span><strong><u><h3>Unclassified cookies:</h3></u></strong></span></span><span><span><span>These are
 cookies that have not yet been categorized. We are in the process of classifying these cookies
 with the help of their providers.</span></span></span></div><div></div><div><span><section><div><table><tbody><tr><th>
 Name:</th><td><span>qzldFuPoKzRdeQ2o5vIizpw7ztIgUcj7GexmvfIn</span></td></tr><tr><th>
 Provider:</th><td><span>.talospioneers.com</span></td></tr><tr><th>
 Type:</th><td><span>server_cookie</span></td></tr><tr><th>
 Expires in:</th><td><span>2 hours</span></td></tr></tbody></table></div></section></span></div><div></div><div><span><span><strong><span><h2>How can I control cookies on my browser?</h2></span></strong></span></span></div><div><span>As the means by which you can refuse cookies
 through your web browser controls vary from browser to browser, you should visit your browser's help
 menu for more information. The following is information about how to manage cookies on the most popular
 browsers:</span><span><a
 href="https://support.google.com/chrome/answer/95647#zippy=%2Callow-or-block-cookies"
 rel="noopener noreferrer" target="_blank"></a></span></div><ul><li><span><a
 href="https://support.google.com/chrome/answer/95647#zippy=%2Callow-or-block-cookies"
 rel="noopener noreferrer" target="_blank"><span>Chrome</span></a></span></li><li><span><a
 href="https://support.microsoft.com/en-us/windows/delete-and-manage-cookies-168dab11-0753-043d-7c16-ede5947fc64d"
 rel="noopener noreferrer" target="_blank"><span>Internet
 Explorer</span></a></span></li><li><span><a
 href="https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop?redirectslug=enable-and-disable-cookies-website-preferences&redirectlocale=en-US"
 rel="noopener noreferrer" target="_blank"><span>Firefox</span></a></span></li><li><span><a
 href="https://support.apple.com/en-ie/guide/safari/sfri11471/mac" rel="noopener noreferrer"
 target="_blank"><span>Safari</span></a></span></li><li><span><a
 href="https://support.microsoft.com/en-us/windows/microsoft-edge-browsing-data-and-privacy-bb8174ba-9d73-dcf2-9b4a-c582b4e640dd"
 rel="noopener noreferrer" target="_blank"><span>Edge</span></a></span></li><li><span><a
 href="https://help.opera.com/en/latest/web-preferences/" rel="noopener noreferrer"
 target="_blank"><span>Opera</span></a></span></li></ul><div><span>In addition, most advertising networks offer
 you a way to opt out of targeted advertising. If you would like to find out more information, please
 visit:</span><span><a
 href="http://www.aboutads.info/choices/" rel="noopener noreferrer" target="_blank"></a></span></div><ul><li><span><a
 href="http://www.aboutads.info/choices/" rel="noopener noreferrer" target="_blank"><span>Digital Advertising Alliance</span></a></span><span><a href="https://youradchoices.ca/"
 rel="noopener noreferrer" target="_blank"></a></span></li><li><span><a
 href="https://youradchoices.ca/" rel="noopener noreferrer" target="_blank"><span>Digital Advertising Alliance of
 Canada</span></a></span><span><a
 href="http://www.youronlinechoices.com/" rel="noopener noreferrer" target="_blank"></a></span></li><li><span><a
 href="http://www.youronlinechoices.com/" rel="noopener noreferrer" target="_blank"><span>European Interactive Digital Advertising Alliance</span></a></span></li></ul><div></div><div><strong><span><h2>What about other tracking technologies, like web beacons?</h2></span></strong></div><div><span><span><span><span>Cookies are
 not the only way to recognize or track visitors to a website. We may use other, similar
 technologies from time to time, like web beacons (sometimes called "tracking pixels" or
 "clear gifs"). These are tiny graphics files that contain a unique identifier that enables
 us to recognize when someone has visited our Website or
 opened an email including them. This allows
 us, for example, to monitor </span><span><span><span>the traffic patterns of users from one page within a
 website to another, to deliver or communicate with cookies, to understand whether
 you have come to the website from an online advertisement displayed on a third-party
 website, to improve site performance, and to measure the success of email marketing
 campaigns. In many instances, these technologies are reliant on cookies to function
 properly, and so declining cookies will impair their functioning.</span></span></span></span></span></span></div><div></div><div><span><strong><h2>Do you use Flash cookies or Local Shared Objects?</h2></strong></span></div><div><span><span>Websites may also use so-called "Flash Cookies" (also known as Local
 Shared Objects or "LSOs") to, among other things, collect and store information about your use of
 our services, fraud prevention, and for other site operations.</span></span></div><div></div><div><span><span>If you do not want Flash Cookies stored on your computer, you can
 adjust the settings of your Flash player to block Flash Cookies storage using the tools contained in
 the </span></span><span><span><a
 href="http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager07.html"
 rel="noopener noreferrer" target="_blank"><span>Website Storage
 Settings Panel</span></a></span><span>. You
 can also control Flash Cookies by going to the </span><span><a
 href="http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager03.html"
 rel="noopener noreferrer" target="_blank"><span>Global Storage Settings
 Panel</span></a></span></span><span><span> and </span><span><span>following the
 instructions (which may include instructions that explain, for example, how to delete existing
 Flash Cookies (referred to "information" on the Macromedia site), how to prevent Flash LSOs from
 being placed on your computer without your being asked, and (for Flash Player 8 and later) how
 to block Flash Cookies that are not being delivered by the operator of the page you are on at
 the time).</span></span></span></div><div></div><div><span><span><span>Please note
 that setting the Flash Player to restrict or limit acceptance of Flash Cookies may reduce or
 impede the functionality of some Flash applications, including, potentially, Flash applications
 used in connection with our services or online content.</span></span></span><span><span></span></span></div><div></div><div><strong><span><h2>Do you serve targeted advertising?</h2></span></strong></div><div><span><span>Third parties may serve cookies on your computer or mobile device to
 serve advertising through our Website. These companies may use information about your visits to this
 and other websites in order to provide relevant advertisements about goods and services that you may
 be interested in. They may also employ technology that is used to measure the effectiveness of
 advertisements. They can accomplish this by using cookies or web beacons to collect information
 about your visits to this and other sites in order to provide relevant advertisements about goods
 and services of potential interest to you. The information collected through this process does not
 enable us or them to identify 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

---
id: prompts.chat
type: knowledge
owner: OA_Triage
---
# prompts.chat
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "prompts.chat-v2",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "prisma generate && next build",
    "db:deploy": "prisma migrate deploy",
    "start": "next start",
    "lint": "eslint",
    "db:generate": "prisma generate",
    "db:migrate": "prisma migrate dev",
    "db:push": "prisma db push",
    "db:studio": "prisma studio",
    "db:seed": "prisma db seed",
    "db:resetadmin": "npx tsx prisma/reset-admin.ts",
    "db:setup": "prisma generate && prisma migrate dev && prisma db seed",
    "setup": "node scripts/setup.js",
    "generate:examples": "npx tsx scripts/generate-examples.ts",
    "postinstall": "prisma generate",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:ui": "vitest --ui",
    "test:coverage": "vitest run --coverage",
    "lint:mdx": "node scripts/lint-mdx.js",
    "book:pdf": "npx tsx scripts/generate-book-pdf.ts",
    "book:pdf:all": "npx tsx scripts/generate-book-pdf.ts --all",
    "book:pdf:convert": "npx tsx scripts/html-to-pdf.ts",
    "book:pdf:print": "npx tsx scripts/generate-book-pdf.ts --print && npx tsx scripts/html-to-pdf.ts --print",
    "book:pdf:print:all": "npx tsx scripts/generate-book-pdf.ts --all --print && npx tsx scripts/html-to-pdf.ts --all --print"
  },
  "dependencies": {
    "@auth/prisma-adapter": "^2.11.1",
    "@aws-sdk/client-s3": "^3.948.0",
    "@hookform/resolvers": "^5.2.2",
    "@mdx-js/loader": "^3.1.1",
    "@mdx-js/react": "^3.1.1",
    "@modelcontextprotocol/sdk": "^1.24.3",
    "@monaco-editor/react": "^4.7.0",
    "@next/mdx": "^16.1.1",
    "@prisma/client": "^6.19.0",
    "@radix-ui/react-alert-dialog": "^1.1.15",
    "@radix-ui/react-avatar": "^1.1.11",
    "@radix-ui/react-checkbox": "^1.3.3",
    "@radix-ui/react-context-menu": "^2.2.16",
    "@radix-ui/react-dialog": "^1.1.15",
    "@radix-ui/react-dropdown-menu": "^2.1.16",
    "@radix-ui/react-label": "^2.1.8",
    "@radix-ui/react-popover": "^1.1.15",
    "@radix-ui/react-progress": "^1.1.8",
    "@radix-ui/react-scroll-area": "^1.2.10",
    "@radix-ui/react-select": "^2.2.6",
    "@radix-ui/react-separator": "^1.1.8",
    "@radix-ui/react-slot": "^1.2.4",
    "@radix-ui/react-switch": "^1.2.6",
    "@radix-ui/react-tabs": "^1.1.13",
    "@radix-ui/react-tooltip": "^1.2.8",
    "@sentry/nextjs": "^10.32.1",
    "@tailwindcss/typography": "^0.5.19",
    "@types/d3": "^7.4.3",
    "bcryptjs": "^3.0.3",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "cmdk": "^1.1.1",
    "d3": "^7.9.0",
    "date-fns": "^4.1.0",
    "jszip": "^3.10.1",
    "lucide-react": "^0.556.0",
    "next": "^16.0.10",
    "next-auth": "^5.0.0-beta.30",
    "next-intl": "^4.5.8",
    "next-themes": "^0.4.6",
    "openai": "^6.10.0",
    "pino": "^10.1.0",
    "prompts.chat": "^0.0.7",
    "react": "19.2.0",
    "react-dom": "19.2.0",
    "react-hook-form": "^7.68.0",
    "react-markdown": "^10.1.0",
    "remark-gfm": "^4.0.1",
    "sharp": "^0.33.5",
    "sonner": "^2.0.7",
    "tailwind-merge": "^3.4.0",
    "yaml": "^2.8.2",
    "zod": "^4.1.13"
  },
  "prisma": {
    "seed": "npx tsx prisma/seed.ts"
  },
  "devDependencies": {
    "@clack/prompts": "^0.11.0",
    "@tailwindcss/postcss": "^4",
    "@testing-library/jest-dom": "^6.6.3",
    "@testing-library/react": "^16.1.0",
    "@testing-library/user-event": "^14.5.2",
    "@types/bcryptjs": "^2.4.6",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@vitejs/plugin-react": "^4.3.4",
    "@vitest/coverage-v8": "^2.1.8",
    "@vitest/ui": "^2.1.8",
    "babel-plugin-react-compiler": "1.0.0",
    "eslint": "^9",
    "eslint-config-next": "16.0.7",
    "jsdom": "^25.0.1",
    "picocolors": "^1.1.1",
    "prisma": "^6.19.0",
    "puppeteer": "^24.37.1",
    "tailwindcss": "^4",
    "tsx": "^4.21.0",
    "tw-animate-css": "^1.4.0",
    "typescript": "^5",
    "vitest": "^2.1.8"
  },
  "engines": {
    "node": "24.x"
  }
}

```

### File: README.md
```md
<h1 align="center">
  <a href="https://prompts.chat">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://prompts.chat/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://prompts.chat/logo.svg">
      <img height="60" alt="prompts.chat" src="https://prompts.chat/logo.svg">
    </picture>
    <br>
    prompts.chat
  </a>
</h1>

<p align="center">
  <strong>The world's largest open-source prompt library for AI</strong><br>
  <sub>Works with ChatGPT, Claude, Gemini, Llama, Mistral, and more</sub>
</p>
<p align="center">
  <sub>formerly known as Awesome ChatGPT Prompts</sub>
</p>

<p align="center">
  <a href="https://prompts.chat"><img src="https://img.shields.io/badge/Website-prompts.chat-blue?style=flat-square" alt="Website"></a>
  <a href="https://github.com/sindresorhus/awesome"><img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome"></a>
  <a href="https://huggingface.co/datasets/fka/prompts.chat"><img src="https://img.shields.io/badge/🤗-Hugging_Face-yellow?style=flat-square" alt="Hugging Face"></a>
  <a href="https://deepwiki.com/f/prompts.chat"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

<p align="center">
  <a href="https://prompts.chat/prompts">🌐 Browse Prompts</a> •
  <a href="https://fka.gumroad.com/l/art-of-chatgpt-prompting">📖 Read the Book</a> •
  <a href="https://raw.githubusercontent.com/f/prompts.chat/main/PROMPTS.md">📄 View on GitHub</a> •
  <a href="#-self-hosting">🚀 Self-Host</a>
</p>

<p align="center">
  <sub>
    🏆 Featured in <a href="https://www.forbes.com/sites/tjmccue/2023/01/19/chatgpt-success-completely-depends-on-your-prompt/">Forbes</a> · 
    🎓 Referenced by <a href="https://www.huit.harvard.edu/news/ai-prompts">Harvard</a>, <a href="https://etc.cuit.columbia.edu/news/columbia-prompt-library-effective-academic-ai-use">Columbia</a> · 
    📄 <a href="https://scholar.google.com/citations?user=AZ0Dg8YAAAAJ&hl=en">40+ academic citations</a> · 
    ❤️ <a href="https://huggingface.co/datasets/fka/prompts.chat">Most liked dataset</a> on Hugging Face<br>
    ⭐ 143k+ GitHub stars · 
    🏅 <a href="https://spotlights-feed.github.com/spotlights/prompts-chat/index/">GitHub Staff Pick</a> · 
    🚀 First prompt library (Dec 2022)
  </sub>
</p>

<p align="center">
  <sub><strong>Loved by AI pioneers:</strong></sub><br>
  <sub>
    <a href="https://x.com/gdb/status/1602072566671110144"><strong>Greg Brockman</strong></a> (OpenAI Co-Founder) · 
    <a href="https://x.com/woj_zaremba/status/1601362952841760769"><strong>Wojciech Zaremba</strong></a> (OpenAI Co-Founder) · 
    <a href="https://x.com/clementdelangue/status/1830976369389642059"><strong>Clement Delangue</strong></a> (Hugging Face CEO) · 
    <a href="https://x.com/ashtom/status/1887250944427237816"><strong>Thomas Dohmke</strong></a> (Former GitHub CEO)
  </sub>
</p>

---

## What is this?

A curated collection of **prompt examples** for AI chat models. Originally created for ChatGPT, these prompts work great with any modern AI assistant.

| Browse Prompts | Data Formats |
|----------------|--------------|
| [prompts.chat](https://prompts.chat/prompts) | [prompts.csv](prompts.csv) |
| [PROMPTS.md](https://raw.githubusercontent.com/f/prompts.chat/main/PROMPTS.md) | [Hugging Face Dataset](https://huggingface.co/datasets/fka/prompts.chat) |

**Want to contribute?** Add prompts at [prompts.chat/prompts/new](https://prompts.chat/prompts/new) — they sync here automatically.

---

## 📖 The Interactive Book of Prompting

Learn prompt engineering with our **free, interactive guide** — 25+ chapters covering everything from basics to advanced techniques like chain-of-thought reasoning, few-shot learning, and AI agents.

**[Start Reading →](https://fka.gumroad.com/l/art-of-chatgpt-prompting)**

---

## 🎮 Prompting for Kids

<p>
  <a href="https://prompts.chat/kids">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://prompts.chat/promi-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://prompts.chat/promi.svg">
      <img height="60" alt="Promi" src="https://prompts.chat/promi.svg" align="left">
    </picture>
  </a>
</p>

An interactive, game-based adventure to teach children (ages 8-14) how to communicate with AI through fun puzzles and stories.

**[Start Playing →](https://prompts.chat/kids)**

<br clear="left">

---

## 🚀 Self-Hosting

Deploy your own private prompt library with custom branding, themes, and authentication.

**Quick Start:**
```bash
npx prompts.chat new my-prompt-library
cd my-prompt-library
```

**Manual Setup:**
```bash
git clone https://github.com/f/prompts.chat.git
cd prompts.chat
npm install && npm run setup
```

The setup wizard configures branding, theme, authentication (GitHub/Google/Azure AD), and features.

📖 **[Full Self-Hosting Guide](SELF-HOSTING.md)** • 🐳 **[Docker Guide](DOCKER.md)**

---

## 🔌 Integrations

### CLI
```bash
npx prompts.chat
```

### Claude Code Plugin
```
/plugin marketplace add f/prompts.chat
/plugin install prompts.chat@prompts.chat
```
📖 [Plugin Documentation](CLAUDE-PLUGIN.md)

### MCP Server
Use prompts.chat as an MCP server in your AI tools.

**Remote (recommended):**
```json
{
  "mcpServers": {
    "prompts.chat": {
      "url": "https://prompts.chat/api/mcp"
    }
  }
}
```

**Local:**
```json
{
  "mcpServers": {
    "prompts.chat": {
      "command": "npx",
      "args": ["-y", "prompts.chat", "mcp"]
    }
  }
}
```

📖 [MCP Documentation](https://prompts.chat/docs/api)

---

## 💖 Sponsors

<p align="center">
  <!-- Clemta -->
  <a href="https://clemta.com/?utm_source=prompts.chat">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/clemta-dark.webp">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/clemta.webp">
      <img height="35" alt="Clemta" src="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/clemta.webp">
    </picture>
  </a>&nbsp;&nbsp;
  <!-- Wiro (py-1) -->
  <a href="https://wiro.ai/?utm_source=prompts.chat">
    <img height="30" alt="Wiro" src="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/wiro.png">
  </a>&nbsp;&nbsp;
  <!-- Cognition -->
  <a href="https://wind.surf/prompts-chat">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/cognition-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/cognition.svg">
      <img height="35" alt="Cognition" src="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/cognition.svg">
    </picture>
  </a>&nbsp;&nbsp;
  <!-- CodeRabbit (py-1) -->
  <a href="https://coderabbit.link/fatih">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/coderabbit-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/coderabbit.svg">
      <img height="30" alt="CodeRabbit" src="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/coderabbit.svg">
    </picture>
  </a>&nbsp;&nbsp;
  <!-- Sentry (py-1) -->
  <a href="https://sentry.io/?utm_source=prompts.chat">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/sentry-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/sentry.svg">
      <img height="30" alt="Sentry" src="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/sentry.svg">
    </picture>
  </a>&nbsp;&nbsp;
  <!-- Each Labs (py-[6px]) -->
  <a href="https://www.eachlabs.ai/?utm_source=promptschat&utm_medium=referral">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/eachlabs-dark.png">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/eachlabs.png">
      <img height="28" alt="Each Labs" src="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/eachlabs.png">
    </picture>
  </a>&nbsp;&nbsp;
  <!-- CommandCode (py-1) -->
  <a href="https://commandcode.ai/?utm_source=prompts.chat">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/commandcode-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/commandcode.svg">
      <img height="30" alt="CommandCode" src="https://raw.githubusercontent.com/f/prompts.chat/main/public/sponsors/commandcode.svg">
    </picture>
  </a>
</p>

<p align="center">
  <sub>Built with <a href="https://wind.surf/prompts-chat">Windsurf</a> and <a href="https://devin.ai">Devin</a></sub><br>
  <a href="https://github.com/sponsors/f/sponsorships?sponsor=f&tier_id=558224&preview=false"><strong>Become a Sponsor →</strong></a>
</p>

---

## 👥 Contributors

<a href="https://github.com/f/prompts.chat/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=f/prompts.chat" />
</a>

---

## 📜 License

**[CC0 1.0 Universal (Public Domain)](https://creativecommons.org/publicdomain/zero/1.0/)** — Copy, modify, distribute, and use freely. No attribution required.

```

### File: public\sounds\README.md
```md
# Kids Game Background Music

Add an 8-bit dubstep/chiptune music file here named `8bit-game-music.mp3`.

## Recommended Sources (Royalty-Free)

- [OpenGameArt.org](https://opengameart.org/) - Free game assets including music
- [FreeMusicArchive.org](https://freemusicarchive.org/) - CC-licensed music
- [Incompetech.com](https://incompetech.com/) - Royalty-free music by Kevin MacLeod

## File Requirements

- **Filename:** `8bit-game-music.mp3`
- **Format:** MP3
- **Style:** 8-bit / Chiptune / Retro game music
- **Loop-friendly:** Ideally seamless loop for background music

```

### File: AGENTS.md
```md
# AGENTS.md

> Guidelines for AI coding agents working on this project.

## Project Overview

**prompts.chat** is a social platform for AI prompts built with Next.js 16. It allows users to share, discover, and collect prompts from the community. The project is open source and can be self-hosted with customizable branding, themes, and authentication.

### Tech Stack

- **Framework:** Next.js 16.0.7 (App Router) with React 19.2
- **Language:** TypeScript 5
- **Database:** PostgreSQL with Prisma ORM 6.19
- **Authentication:** NextAuth.js 5 (beta) with pluggable providers (credentials, GitHub, Google, Azure)
- **Styling:** Tailwind CSS 4 with Radix UI primitives
- **UI Components:** shadcn/ui pattern (components in `src/components/ui/`)
- **Internationalization:** next-intl with 11 supported locales
- **Icons:** Lucide React
- **Forms:** React Hook Form with Zod validation

## Project Structure

```
/
├── prisma/                 # Database schema and migrations
│   ├── schema.prisma       # Prisma schema definition
│   ├── migrations/         # Database migrations
│   └── seed.ts             # Database seeding script
├── public/                 # Static assets (logos, favicon)
├── messages/               # i18n translation files (en.json, es.json, etc.)
├── src/
│   ├── app/                # Next.js App Router pages
│   │   ├── (auth)/         # Auth pages (login, register)
│   │   ├── [username]/     # User profile pages
│   │   ├── admin/          # Admin dashboard
│   │   ├── api/            # API routes
│   │   ├── categories/     # Category pages
│   │   ├── prompts/        # Prompt CRUD pages
│   │   ├── feed/           # User feed
│   │   ├── discover/       # Discovery page
│   │   ├── settings/       # User settings
│   │   └── tags/           # Tag pages
│   ├── components/         # React components
│   │   ├── admin/          # Admin-specific components
│   │   ├── auth/           # Authentication components
│   │   ├── categories/     # Category components
│   │   ├── layout/         # Layout components (header, etc.)
│   │   ├── prompts/        # Prompt-related components
│   │   ├── providers/      # React context providers
│   │   ├── settings/       # Settings components
│   │   └── ui/             # shadcn/ui base components
│   ├── lib/                # Utility libraries
│   │   ├── ai/             # AI/OpenAI integration
│   │   ├── auth/           # NextAuth configuration
│   │   ├── config/         # Config type definitions
│   │   ├── i18n/           # Internationalization setup
│   │   ├── plugins/        # Plugin system (auth, storage)
│   │   ├── db.ts           # Prisma client instance
│   │   └── utils.ts        # Utility functions (cn)
│   └── i18n/               # i18n request handler
├── prompts.config.ts       # Main application configuration
├── prompts.csv             # Community prompts data source
└── package.json            # Dependencies and scripts
```

## Commands

```bash
# Development
npm run dev              # Start development server (localhost:3000)
npm run build            # Build for production (runs prisma generate first)
npm run start            # Start production server
npm run lint             # Run ESLint

# Database
npm run db:generate      # Generate Prisma client
npm run db:migrate       # Run database migrations
npm run db:push          # Push schema changes to database
npm run db:studio        # Open Prisma Studio
npm run db:seed          # Seed database with initial data

# Type checking
npx tsc --noEmit         # Check TypeScript types without emitting

# Translations
node scripts/check-translations.js  # Check for missing translations across locales
```

## Code Style Guidelines

### TypeScript

- Use TypeScript strict mode
- Prefer explicit types over `any`
- Use `interface` for object shapes, `type` for unions/intersections
- Functions: `camelCase` (e.g., `getUserData`, `handleSubmit`)
- Components: `PascalCase` (e.g., `PromptCard`, `AuthContent`)
- Constants: `UPPER_SNAKE_CASE` for true constants
- Files: `kebab-case.tsx` for components, `camelCase.ts` for utilities

### React/Next.js

- Use React Server Components by default
- Add `"use client"` directive only when client interactivity is needed
- Prefer server actions over API routes for mutations
- Use `next-intl` for all user-facing strings (never hardcode text)
- Import translations with `useTranslations()` or `getTranslations()`

### Component Pattern

```tsx
// Client component example
"use client";

import { useTranslations } from "next-intl";
import { Button } from "@/components/ui/button";

interface MyComponentProps {
  title: string;
  onAction: () => void;
}

export function MyComponent({ title, onAction }: MyComponentProps) {
  const t = useTranslations("namespace");
  
  return (
    <div className="space-y-4">
      <h2 className="text-lg font-semibold">{title}</h2>
      <Button onClick={onAction}>{t("actionLabel")}</Button>
    </div>
  );
}
```

### Styling

- Use Tailwind CSS utility classes
- Follow mobile-first responsive design (`sm:`, `md:`, `lg:` breakpoints)
- Use `cn()` utility from `@/lib/utils` for conditional classes
- Prefer Radix UI primitives via shadcn/ui components
- Keep component styling scoped and composable

### Database

- Use Prisma Client from `@/lib/db`
- Always include proper `select` or `include` for relations
- Use transactions for multi-step operations
- Add indexes for frequently queried fields

## Configuration

The main configuration file is `prompts.config.ts`:

- **branding:** Logo, name, and description
- **theme:** Colors, border radius, UI variant
- **auth:** Authentication providers array (credentials, github, google, azure)
- **i18n:** Supported locales and default locale
- **features:** Feature flags (privatePrompts, changeRequests, categories, tags, aiSearch)
- **homepage:** Homepage customization and sponsors

## Plugin System

Authentication and storage use a plugin architecture:

### Auth Plugins (`src/lib/plugins/auth/`)
- `credentials.ts` - Email/password authentication
- `github.ts` - GitHub OAuth
- `google.ts` - Google OAuth  
- `azure.ts` - Microsoft Entra ID

### Storage Plugins (`src/lib/plugins/storage/`)
- `url.ts` - URL-based media (default)
- `s3.ts` - AWS S3 storage

## Internationalization

- Translation files are in `messages/{locale}.json`
- Currently supported: en, tr, es, zh, ja, ar, pt, fr, de, ko, it
- Add new locales to `prompts.config.ts` i18n.locales array
- Create corresponding translation file in `messages/`
- Add language to selector in `src/components/layout/header.tsx`

## Key Files

| File | Purpose |
|------|---------|
| `prompts.config.ts` | Main app configuration |
| `prisma/schema.prisma` | Database schema |
| `src/lib/auth/index.ts` | NextAuth configuration |
| `src/lib/db.ts` | Prisma client singleton |
| `src/app/layout.tsx` | Root layout with providers |
| `src/components/ui/` | Base UI components (shadcn) |

## Boundaries

### Always Do
- Run `npm run lint` before committing
- Use existing UI components from `src/components/ui/`
- Add translations for all user-facing text
- Follow existing code patterns and file structure
- Use TypeScript strict types

### Ask First
- Database schema changes (require migrations)
- Adding new dependencies
- Modifying authentication flow
- Changes to `prompts.config.ts` structure

### Never Do
- Commit secrets or API keys (use `.env`)
- Modify `node_modules/` or generated files
- Delete existing translations
- Remove or weaken TypeScript types
- Hardcode user-facing strings (use i18n)

## Environment Variables

Required in `.env`:
```
DATABASE_URL=           # PostgreSQL connection string
AUTH_SECRET=            # NextAuth secret key
```

Optional OAuth (if using those providers):
```
AUTH_GITHUB_ID=
AUTH_GITHUB_SECRET=
AUTH_GOOGLE_ID=
AUTH_GOOGLE_SECRET=
AUTH_AZURE_AD_CLIENT_ID=
AUTH_AZURE_AD_CLIENT_SECRET=
AUTH_AZURE_AD_ISSUER=
```

Optional features:
```
OPENAI_API_KEY=         # For AI-powered semantic search
```

## Testing

Currently no automated tests. When implementing:
- Place tests adjacent to source files or in `__tests__/` directories
- Use descriptive test names
- Mock external services (database, OAuth)

## Common Tasks

### Adding a new page
1. Create route in `src/app/{route}/page.tsx`
2. Use server component for data fetching
3. Add translations to `messages/*.json`

### Adding a new component
1. Create in appropriate `src/components/{category}/` folder
2. Export from component file (no barrel exports needed)
3. Follow existing component patterns

### Adding a new API route
1. Create in `src/app/api/{route}/route.ts`
2. Export appropriate HTTP method handlers (GET, POST, etc.)
3. Use Zod for request validation
4. Return proper JSON responses with status codes

### Modifying database schema
1. Update `prisma/schema.prisma`
2. Run `npm run db:migrate` to create migration
3. Update related TypeScript types if needed

```

### File: CLAUDE-PLUGIN.md
```md
# Claude Code Plugin

Access prompts.chat directly in [Claude Code](https://code.claude.com) with our official plugin. Search prompts, discover skills, and improve your prompts without leaving your IDE.

## Installation

Add the prompts.chat marketplace to Claude Code:

```
/plugin marketplace add f/prompts.chat
```

Then install the plugin:

```
/plugin install prompts.chat@prompts.chat
```

## Features

| Feature | Description |
|---------|-------------|
| **MCP Server** | Connect to prompts.chat API for real-time prompt access |
| **Commands** | `/prompts.chat:prompts` and `/prompts.chat:skills` slash commands |
| **Agents** | Prompt Manager and Skill Manager agents for complex workflows |
| **Skills** | Auto-activating skills for prompt and skill discovery |

## Commands

### Search Prompts

```
/prompts.chat:prompts <query>
/prompts.chat:prompts <query> --type IMAGE
/prompts.chat:prompts <query> --category coding
/prompts.chat:prompts <query> --tag productivity
```

**Examples:**
```
/prompts.chat:prompts code review
/prompts.chat:prompts writing assistant --category writing
/prompts.chat:prompts midjourney --type IMAGE
/prompts.chat:prompts react developer --tag coding
```

### Search Skills

```
/prompts.chat:skills <query>
/prompts.chat:skills <query> --category coding
/prompts.chat:skills <query> --tag automation
```

**Examples:**
```
/prompts.chat:skills testing automation
/prompts.chat:skills documentation --category coding
/prompts.chat:skills api integration
```

## MCP Tools

The plugin provides these tools via the prompts.chat MCP server:

### Prompt Tools

| Tool | Description |
|------|-------------|
| `search_prompts` | Search prompts by keyword, category, tag, or type |
| `get_prompt` | Retrieve a prompt with variable substitution |
| `save_prompt` | Save a new prompt (requires API key) |
| `improve_prompt` | Enhance prompts using AI |

### Skill Tools

| Tool | Description |
|------|-------------|
| `search_skills` | Search for Agent Skills |
| `get_skill` | Get a skill with all its files |
| `save_skill` | Create multi-file skills (requires API key) |
| `add_file_to_skill` | Add a file to an existing skill |
| `update_skill_file` | Update a file in a skill |
| `remove_file_from_skill` | Remove a file from a skill |

## Agents

### Prompt Manager

The `prompt-manager` agent helps you:
- Search for prompts across prompts.chat
- Get and fill prompt variables
- Save new prompts to your account
- Improve prompts using AI

### Skill Manager

The `skill-manager` agent helps you:
- Search for Agent Skills
- Get and install skills to your workspace
- Create new skills with multiple files
- Manage skill file contents

## Skills (Auto-Activating)

### Prompt Lookup

Automatically activates when you:
- Ask for prompt templates
- Want to search for prompts
- Need to improve a prompt
- Mention prompts.chat

### Skill Lookup

Automatically activates when you:
- Ask for Agent Skills
- Want to extend Claude's capabilities
- Need to install a skill
- Mention skills for Claude

## Authentication

To save prompts and skills, you need an API key from [prompts.chat/settings](https://prompts.chat/settings).

### Option 1: Environment Variable

Set the `PROMPTS_API_KEY` environment variable:

```bash
export PROMPTS_API_KEY=your_api_key_here
```

### Option 2: MCP Header

Add the header when connecting to the MCP server:

```
PROMPTS_API_KEY: your_api_key_here
```

## Plugin Structure

```
plugins/claude/prompts.chat/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── .mcp.json                 # MCP server configuration
├── commands/
│   ├── prompts.md           # /prompts.chat:prompts command
│   └── skills.md            # /prompts.chat:skills command
├── agents/
│   ├── prompt-manager.md    # Prompt management agent
│   └── skill-manager.md     # Skill management agent
└── skills/
    ├── prompt-lookup/
    │   └── SKILL.md         # Prompt discovery skill
    └── skill-lookup/
        └── SKILL.md         # Skill discovery skill
```

## Links

- **[prompts.chat](https://prompts.chat)** - Browse all prompts and skills
- **[API Documentation](https://prompts.chat/api/mcp)** - MCP server endpoint
- **[Settings](https://prompts.chat/settings)** - Get your API key

```

### File: CLAUDE.md
```md
# CLAUDE.md

> Quick reference for Claude Code when working on prompts.chat

## Project Overview

**prompts.chat** is a social platform for AI prompts built with Next.js 16 App Router, React 19, TypeScript, and PostgreSQL/Prisma. It allows users to share, discover, and collect prompts.

For detailed agent guidelines, see [AGENTS.md](AGENTS.md).

## Quick Commands

```bash
# Development
npm run dev              # Start dev server at localhost:3000
npm run build            # Production build (runs prisma generate)
npm run lint             # Run ESLint

# Database
npm run db:migrate       # Run Prisma migrations
npm run db:push          # Push schema changes
npm run db:studio        # Open Prisma Studio
npm run db:seed          # Seed database

# Type checking
npx tsc --noEmit         # Check TypeScript types
```

## Key Files

| File | Purpose |
|------|---------|
| `prompts.config.ts` | Main app configuration (branding, theme, auth, features) |
| `prisma/schema.prisma` | Database schema |
| `src/lib/auth/index.ts` | NextAuth configuration |
| `src/lib/db.ts` | Prisma client singleton |
| `messages/*.json` | i18n translation files |

## Project Structure

```
src/
├── app/              # Next.js App Router pages
│   ├── (auth)/       # Login, register
│   ├── api/          # API routes
│   ├── prompts/      # Prompt CRUD pages
│   └── admin/        # Admin dashboard
├── components/       # React components
│   ├── ui/           # shadcn/ui base components
│   └── prompts/      # Prompt-related components
└── lib/              # Utilities and config
    ├── ai/           # OpenAI integration
    ├── auth/         # NextAuth setup
    └── plugins/      # Auth and storage plugins
```

## Code Patterns

- **Server Components** by default, `"use client"` only when needed
- **Translations:** Use `useTranslations()` or `getTranslations()` from next-intl
- **Styling:** Tailwind CSS with `cn()` utility for conditional classes
- **Forms:** React Hook Form + Zod validation
- **Database:** Prisma client from `@/lib/db`

## Before Committing

1. Run `npm run lint` to check for issues
2. Add translations for any user-facing text
3. Use existing UI components from `src/components/ui/`
4. Never commit secrets (use `.env`)

```

### File: claude_plugin.md
```md
# Claude Code Plugin

Access prompts.chat directly in [Claude Code](https://code.claude.com) with our official plugin. Search prompts, discover skills, and improve your prompts without leaving your IDE.

## Installation

Add the prompts.chat marketplace to Claude Code:

```
/plugin marketplace add f/prompts.chat
```

Then install the plugin:

```
/plugin install prompts.chat@prompts.chat
```

## Features

| Feature | Description |
|---------|-------------|
| **MCP Server** | Connect to prompts.chat API for real-time prompt access |
| **Commands** | `/prompts.chat:prompts` and `/prompts.chat:skills` slash commands |
| **Agents** | Prompt Manager and Skill Manager agents for complex workflows |
| **Skills** | Auto-activating skills for prompt and skill discovery |

## Commands

### Search Prompts

```
/prompts.chat:prompts <query>
/prompts.chat:prompts <query> --type IMAGE
/prompts.chat:prompts <query> --category coding
/prompts.chat:prompts <query> --tag productivity
```

**Examples:**
```
/prompts.chat:prompts code review
/prompts.chat:prompts writing assistant --category writing
/prompts.chat:prompts midjourney --type IMAGE
/prompts.chat:prompts react developer --tag coding
```

### Search Skills

```
/prompts.chat:skills <query>
/prompts.chat:skills <query> --category coding
/prompts.chat:skills <query> --tag automation
```

**Examples:**
```
/prompts.chat:skills testing automation
/prompts.chat:skills documentation --category coding
/prompts.chat:skills api integration
```

## MCP Tools

The plugin provides these tools via the prompts.chat MCP server:

### Prompt Tools

| Tool | Description |
|------|-------------|
| `search_prompts` | Search prompts by keyword, category, tag, or type |
| `get_prompt` | Retrieve a prompt with variable substitution |
| `save_prompt` | Save a new prompt (requires API key) |
| `improve_prompt` | Enhance prompts using AI |

### Skill Tools

| Tool | Description |
|------|-------------|
| `search_skills` | Search for Agent Skills |
| `get_skill` | Get a skill with all its files |
| `save_skill` | Create multi-file skills (requires API key) |
| `add_file_to_skill` | Add a file to an existing skill |
| `update_skill_file` | Update a file in a skill |
| `remove_file_from_skill` | Remove a file from a skill |

## Agents

### Prompt Manager

The `prompt-manager` agent helps you:
- Search for prompts across prompts.chat
- Get and fill prompt variables
- Save new prompts to your account
- Improve prompts using AI

### Skill Manager

The `skill-manager` agent helps you:
- Search for Agent Skills
- Get and install skills to your workspace
- Create new skills with multiple files
- Manage skill file contents

## Skills (Auto-Activating)

### Prompt Lookup

Automatically activates when you:
- Ask for prompt templates
- Want to search for prompts
- Need to improve a prompt
- Mention prompts.chat

### Skill Lookup

Automatically activates when you:
- Ask for Agent Skills
- Want to extend Claude's capabilities
- Need to install a skill
- Mention skills for Claude

## Authentication

To save prompts and skills, you need an API key from [prompts.chat/settings](https://prompts.chat/settings).

### Option 1: Environment Variable

Set the `PROMPTS_API_KEY` environment variable:

```bash
export PROMPTS_API_KEY=your_api_key_here
```

### Option 2: MCP Header

Add the header when connecting to the MCP server:

```
PROMPTS_API_KEY: your_api_key_here
```

## Plugin Structure

```
plugins/claude/prompts.chat/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── .mcp.json                 # MCP server configuration
├── commands/
│   ├── prompts.md           # /prompts.chat:prompts command
│   └── skills.md            # /prompts.chat:skills command
├── agents/
│   ├── prompt-manager.md    # Prompt management agent
│   └── skill-manager.md     # Skill management agent
└── skills/
    ├── prompt-lookup/
    │   └── SKILL.md         # Prompt discovery skill
    └── skill-lookup/
        └── SKILL.md         # Skill discovery skill
```

## Links

- **[prompts.chat](https://prompts.chat)** - Browse all prompts and skills
- **[API Documentation](https://prompts.chat/api/mcp)** - MCP server endpoint
- **[Settings](https://prompts.chat/settings)** - Get your API key

```

### File: components.json
```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "src/app/globals.css",
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
    "hooks": "@/hooks"
  },
  "registries": {}
}

```

### File: context7.json
```json
{
  "url": "https://context7.com/f/prompts.chat",
  "public_key": "pk_1VY7yEEijnbFIFVAIDEh2"
}

```

### File: CONTRIBUTING.md
```md
# Contribution Guidelines

Thank you for your interest in contributing to Awesome ChatGPT Prompts! 

## How to Contribute

The easiest way to contribute is through **[prompts.chat](https://prompts.chat)**:

1. Visit [prompts.chat](https://prompts.chat)
2. Sign in with your GitHub account
3. Create and submit your prompt
4. Your contribution will automatically sync to this repository

Your GitHub username will be credited as the contributor, and you'll appear in the repository's contributors list.

## Prompt Guidelines

When creating a new prompt:

- **Test your prompt** - Ensure it generates intended results and can be used by others
- **Be descriptive** - Give your prompt a clear, concise title
- **Be original** - Don't submit duplicates of existing prompts
- **Be appropriate** - Keep content suitable for all audiences

## Direct Contributions

For bug fixes, documentation improvements, or other non-prompt contributions:

1. Fork the repository
2. Create a branch for your changes
3. Submit a pull request with a descriptive title and explanation

## Questions & Issue Policy

Open an issue if you have questions about contributing. 

**Important:** This repository is strictly for AI prompts. 
- Do **not** post advertisements.
- Any off-topic issues will be closed immediately, and the posting user will be reported to GitHub for spam and malicious activity.
```

### File: DOCKER.md
```md
# Docker Deployment Guide

Run your own prompts.chat instance using Docker Compose.

## Quick Start

```bash
git clone https://github.com/f/prompts.chat.git
cd prompts.chat
docker compose up -d
```

Open http://localhost:4444 in your browser.

## Using a Pre-built Image

Edit `compose.yml` and replace the `build` block with the published image:

```yaml
services:
  app:
    # build:
    #   context: .
    #   dockerfile: docker/Dockerfile
    image: ghcr.io/f/prompts.chat:latest
```

Then run:

```bash
docker compose up -d
```

## Standalone (Bring Your Own Database)

If you already have a PostgreSQL instance, you can run just the app container:

```bash
docker build -f docker/Dockerfile -t prompts.chat .
docker run -d \
  --name prompts \
  -p 4444:3000 \
  -e DATABASE_URL="postgresql://user:pass@your-db-host:5432/prompts?schema=public" \
  -e AUTH_SECRET="$(openssl rand -base64 32)" \
  prompts.chat
```

## Custom Branding

All branding is configured via `PCHAT_*` environment variables at runtime -- no rebuild needed.

```yaml
# compose.yml
services:
  app:
    environment:
      # ... existing vars ...
      PCHAT_NAME: "Acme Prompts"
      PCHAT_DESCRIPTION: "Our team's AI prompt library"
      PCHAT_COLOR: "#ff6600"
      PCHAT_AUTH_PROVIDERS: "github,google"
      PCHAT_LOCALES: "en,es,fr"
```

Then restart: `docker compose up -d`

## Configuration Variables

All variables are prefixed with `PCHAT_` to avoid conflicts.

#### Branding (`branding.*` in prompts.config.ts)

| Env Variable | Config Path | Description | Default |
|--------------|-------------|-------------|---------|
| `PCHAT_NAME` | `branding.name` | App name shown in UI | `My Prompt Library` |
| `PCHAT_DESCRIPTION` | `branding.description` | App description | `Collect, organize...` |
| `PCHAT_LOGO` | `branding.logo` | Logo path (in public/) | `/logo.svg` |
| `PCHAT_LOGO_DARK` | `branding.logoDark` | Dark mode logo | Same as `PCHAT_LOGO` |
| `PCHAT_FAVICON` | `branding.favicon` | Favicon path | `/logo.svg` |

#### Theme (`theme.*` in prompts.config.ts)

| Env Variable | Config Path | Description | Default |
|--------------|-------------|-------------|---------|
| `PCHAT_COLOR` | `theme.colors.primary` | Primary color (hex) | `#6366f1` |
| `PCHAT_THEME_RADIUS` | `theme.radius` | Border radius: `none\|sm\|md\|lg` | `sm` |
| `PCHAT_THEME_VARIANT` | `theme.variant` | UI style: `default\|flat\|brutal` | `default` |
| `PCHAT_THEME_DENSITY` | `theme.density` | Spacing: `compact\|default\|comfortable` | `default` |

#### Authentication (`auth.*` in prompts.config.ts)

| Env Variable | Config Path | Description | Default |
|--------------|-------------|-------------|---------|
| `PCHAT_AUTH_PROVIDERS` | `auth.providers` | Providers: `github,google,credentials` | `credentials` |
| `PCHAT_ALLOW_REGISTRATION` | `auth.allowRegistration` | Allow public signup | `true` |

#### Internationalization (`i18n.*` in prompts.config.ts)

| Env Variable | Config Path | Description | Default |
|--------------|-------------|-------------|---------|
| `PCHAT_LOCALES` | `i18n.locales` | Supported locales (comma-separated) | `en` |
| `PCHAT_DEFAULT_LOCALE` | `i18n.defaultLocale` | Default locale | `en` |

#### Features (`features.*` in prompts.config.ts)

| Env Variable | Config Path | Description | Default |
|--------------|-------------|-------------|---------|
| `PCHAT_FEATURE_PRIVATE_PROMPTS` | `features.privatePrompts` | Enable private prompts | `true` |
| `PCHAT_FEATURE_CHANGE_REQUESTS` | `features.changeRequests` | Enable versioning | `true` |
| `PCHAT_FEATURE_CATEGORIES` | `features.categories` | Enable categories | `true` |
| `PCHAT_FEATURE_TAGS` | `features.tags` | Enable tags | `true` |
| `PCHAT_FEATURE_COMMENTS` | `features.comments` | Enable comments | `true` |
| `PCHAT_FEATURE_AI_SEARCH` | `features.aiSearch` | Enable AI search | `false` |
| `PCHAT_FEATURE_AI_GENERATION` | `features.aiGeneration` | Enable AI generation | `false` |
| `PCHAT_FEATURE_MCP` | `features.mcp` | Enable MCP features | `false` |

## System Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `AUTH_SECRET` | Secret for authentication tokens | Auto-generated (set explicitly for production) |
| `DATABASE_URL` | PostgreSQL connection string | Set in compose.yml |
| `DIRECT_URL` | Direct PostgreSQL URL (bypasses poolers) | Same as DATABASE_URL |
| `PORT` | Host port mapping | `4444` |

## Production Setup

For production, always set `AUTH_SECRET` explicitly:

```bash
# Generate a secret
export AUTH_SECRET=$(openssl rand -base64 32)

# Start with explicit secret
docker compose up -d
```

Or add it to a `.env` file next to `compose.yml`:

```env
AUTH_SECRET=your-secret-key-here
```

### With OAuth Providers

```yaml
# compose.yml
services:
  app:
    environment:
      # ... existing vars ...
      PCHAT_AUTH_PROVIDERS: "github,google"
      AUTH_GITHUB_ID: "your-github-client-id"
      AUTH_GITHUB_SECRET: "your-github-client-secret"
      AUTH_GOOGLE_ID: "your-google-client-id"
      AUTH_GOOGLE_SECRET: "your-google-client-secret"
```

### With AI Features (OpenAI)

```yaml
# compose.yml
services:
  app:
    environment:
      # ... existing vars ...
      PCHAT_FEATURE_AI_SEARCH: "true"
      OPENAI_API_KEY: "sk-..."
```

## Database Seeding

Seed the database with example prompts:

```bash
docker compose exec app npx prisma db seed
```

## Custom Logo

Mount your logo file into the app container:

```yaml
# compose.yml
services:
  app:
    volumes:
      - ./my-logo.svg:/app/public/logo.svg
    environment:
      PCHAT_LOGO: "/logo.svg"
```

## Data Persistence

PostgreSQL data is stored in the `postgres_data` named volume and persists across container restarts, rebuilds, and image updates.

### Backup

```bash
# Backup database
docker compose exec db pg_dump -U prompts prompts > backup.sql

# Restore database
docker compose exec -T db psql -U prompts prompts < backup.sql
```

## Building Locally

```bash
docker compose build
docker compose up -d
```

## Health Check

The app container includes a health check endpoint:

```bash
curl http://localhost:4444/api/health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T00:00:00.000Z",
  "database": "connected"
}
```

## Troubleshooting

### View Logs

```bash
# All services
docker compose logs

# Follow logs
docker compose logs -f

# App logs only
docker compose logs app

# Database logs only
docker compose logs db
```

### Database Access

```bash
# Connect to PostgreSQL
docker compose exec db psql -U prompts -d prompts

# Run a query
docker compose exec db psql -U prompts -d prompts -c "SELECT COUNT(*) FROM \"Prompt\""
```

### Container Shell

```bash
docker compose exec app sh
docker compose exec db bash
```

### Common Issues

**App container keeps restarting:**
- Check logs: `docker compose logs app`
- Database may not be ready yet -- the entrypoint retries for up to 60 seconds

**Database connection errors:**
- Verify the `db` service is healthy: `docker compose ps`
- Check database logs: `docker compose logs db`

**Authentication issues:**
- Set `AUTH_SECRET` explicitly for production
- For OAuth, verify callback URLs match your domain

## Updating

```bash
# If using pre-built images
docker compose pull
docker compose up -d

# If building locally
git pull
docker compose build
docker compose up -d
```

Data persists in the `postgres_data` volume across updates.

## Migrating from the Old Single-Image Setup

If you were using the previous all-in-one Docker image:

```bash
# 1. Export your database from the old container
docker exec prompts pg_dump -U prompts prompts > backup.sql

# 2. Stop and remove the old container
docker stop prompts && docker rm prompts

# 3. Start the new compose setup
docker compose up -d

# 4. Import your data
docker compose exec -T db psql -U prompts prompts < backup.sql
```

## Resource Requirements

**Runtime** (after first build):
- 1 CPU core
- 1GB RAM
- 2GB disk space

**First-run build** (Next.js compilation on startup):
- 1 CPU core
- Higher memory required (OOM may occur with low limits)
- 2GB disk space

> ⚠️ If you see `Killed` followed by `exited with code 137` during first startup,
> your Docker container likely ran out of memory during the build step.
> Increasing Docker's memory allocation (e.g., ~4GB or more) can help resolve this.
> On Docker Desktop: Settings → Resources → Memory.

**Recommended for production:**
- 2 CPU cores
- 2GB RAM (runtime)
- 10GB disk space

## Running Behind a Reverse Proxy

### Nginx

```nginx
server {
    listen 443 ssl http2;
    server_name prompts.example.com;

    ssl_certificate /etc/letsencrypt/live/prompts.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/prompts.example.com/privkey.pem;

    location / {
        proxy_pass http://localhost:4444;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
```

### Caddy

```caddyfile
prompts.example.com {
    reverse_proxy localhost:4444
}
```

## Security Considerations

1. **Always set AUTH_SECRET** in production
2. **Use HTTPS** -- put a reverse proxy (Nginx, Caddy, Traefik) in front
3. **Change default database password** -- update `POSTGRES_PASSWORD` in compose.yml and the connection strings
4. **Limit exposed ports** -- only expose what's needed
5. **Regular updates** -- pull the latest image regularly
6. **Backup data** -- regularly backup the database

## License

MIT

```

### File: next.config.ts
```ts
import { withSentryConfig } from "@sentry/nextjs";
import type { NextConfig } from "next";
import createNextIntlPlugin from "next-intl/plugin";
import createMDX from "@next/mdx";

const withNextIntl = createNextIntlPlugin("./src/i18n/request.ts");
const withMDX = createMDX({
  extension: /\.mdx?$/,
});

const nextConfig: NextConfig = {
  pageExtensions: ["js", "jsx", "md", "mdx", "ts", "tsx"],
  reactCompiler: true,
  // Configure webpack for raw imports
  webpack: (config) => {
    config.module.rules.push({
      resourceQuery: /raw/,
      type: 'asset/source',
    });
    return config;
  },
  // Enable standalone output for Docker
  output: "standalone",
  // Experimental features
  experimental: {
    // Enable server actions
    serverActions: {
      bodySizeLimit: "2mb",
    },
  },
  // Image optimization
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "**",
      },
    ],
  },
  // Redirects
  async redirects() {
    return [
      {
        source: "/vibe",
        destination: "/categories/vibe",
        permanent: true,
      },
      {
        source: "/sponsors",
        destination: "/categories/sponsors",
        permanent: true,
      },
      {
        source: "/embed-preview",
        destination: "/embed",
        permanent: true,
      },
      // Redirect book PDF downloads to GitHub raw to save Vercel edge bandwidth
      {
        source: "/book-pdf/:filename",
        destination: "https://raw.githubusercontent.com/f/prompts.chat/refs/heads/main/public/book-pdf/:filename",
        permanent: false,
      },
    ];
  },
};

export default withSentryConfig(withMDX(withNextIntl(nextConfig)), {
  // For all available options, see:
  // https://www.npmjs.com/package/@sentry/webpack-plugin#options

  org: "promptschat",

  project: "prompts-chat",

  // Only print logs for uploading source maps in CI
  silent: !process.env.CI,

  // For all available options, see:
  // https://docs.sentry.io/platforms/javascript/guides/nextjs/manual-setup/

  // Upload a larger set of source maps for prettier stack traces (increases build time)
  widenClientFileUpload: true,

  // tunnelRoute removed — was proxying all browser Sentry events through Vercel edge,
  // generating unnecessary edge requests ($2.45/M) and function invocations ($0.60/M).
  // Estimated savings: $100-400/month. Trade-off: some ad-blockers may block direct Sentry calls.
  // See: https://github.com/f/prompts.chat/issues/1085

  webpack: {
    // Enables automatic instrumentation of Vercel Cron Monitors. (Does not yet work with App Router route handlers.)
    // See the following for more information:
    // https://docs.sentry.io/product/crons/
    // https://vercel.com/docs/cron-jobs
    automaticVercelMonitors: true,

    // Tree-shaking options for reducing bundle size
    treeshake: {
      // Automatically tree-shake Sentry logger statements to reduce bundle size
      removeDebugLogging: true,
    },
  },
});

```

### File: prisma.config.ts
```ts

// This file was generated by Prisma and assumes you have installed the following:
// npm install --save-dev prisma dotenv
import "dotenv/config";
import { defineConfig, env } from "prisma/config";

export default defineConfig({
  schema: "prisma/schema.prisma",
  migrations: {
    path: "prisma/migrations",
  },
  engine: "classic",
  datasource: {
    url: env("DATABASE_URL"),
  },
});

```

### File: prompts.config.ts
```ts
import { defineConfig } from "@/lib/config";

// Set to true to use clone branding (hide prompts.chat repo branding)
const useCloneBranding = false;

export default defineConfig({
  // Branding - customize for white-label
  branding: {
    name: "prompts.chat",
    logo: "/logo.svg",
    logoDark: "/logo-dark.svg",
    favicon: "/logo.svg",
    description: "Collect, organize, and share AI prompts",

    // Delete this if useCloneBranding is true
    appStoreUrl: "https://apps.apple.com/tr/app/prompts-chat/id6756895736",
    chromeExtensionUrl: "https://chromewebstore.google.com/detail/promptschat/eemdohkhbaifiocagjlhibfbhamlbeej",
  },

  // Theme - design system configuration
  theme: {
    // Border radius: "none" | "sm" | "md" | "lg"
    radius: "sm",
    // UI style: "flat" | "default" | "brutal"
    variant: "default",
    // Spacing density: "compact" | "default" | "comfortable"
    density: "default",
    // Colors (hex or oklch)
    colors: {
      primary: "#6366f1", // Indigo
    },
  },

  // Authentication plugins
  auth: {
    // Available: "credentials" | "google" | "azure" | "github" | "apple" | custom
    // Use `providers` array to enable multiple auth providers
    providers: ["github", "google", "apple"],
    // Allow public registration (only applies to credentials provider)
    allowRegistration: false,
  },

  // Internationalization
  i18n: {
    locales: ["en", "tr", "es", "zh", "ja", "ar", "pt", "fr", "it", "de", "nl", "ko", "ru", "he", "el", "az", "fa"],
    defaultLocale: "en",
  },

  // Features
  features: {
    // Allow users to create private prompts
    privatePrompts: true,
    // Enable change request system for versioning
    changeRequests: true,
    // Enable categories
    categories: true,
    // Enable tags
    tags: true,
    // Enable AI-powered semantic search (requires OPENAI_API_KEY)
    aiSearch: true,
    // Enable AI-powered generation features (requires OPENAI_API_KEY)
    aiGeneration: true,
    // Enable MCP (Model Context Protocol) features including API key generation
    mcp: true,
    // Enable comments on prompts
    comments: true,
  },

  // Homepage customization
  homepage: {
    // Set to true to hide prompts.chat repo branding and use your own branding
    useCloneBranding,
    achievements: {
      enabled: !useCloneBranding,
    },
    sponsors: {
      enabled: !useCloneBranding,
      items: [
        // Add sponsors here
        { name: "Clemta", logo: '/sponsors/clemta.webp', url: "https://clemta.com/?utm_source=prompts.chat" },
        { name: "Wiro.ai", className: 'py-1', darkLogo: '/sponsors/wiro.png', logo: '/sponsors/wiro.png', url: "https://wiro.ai/?utm_source=prompts.chat" },
        { name: "Cognition", logo: "/sponsors/cognition.svg", url: "https://wind.surf/prompts-chat" },
        { name: "CodeRabbit", className: 'py-1', logo: '/sponsors/coderabbit.svg', darkLogo: '/sponsors/coderabbit-dark.svg', url: "https://coderabbit.link/fatih" },
        { name: "Sentry", className: 'py-1', logo: '/sponsors/sentry.svg', darkLogo: '/sponsors/sentry-dark.svg', url: "https://sentry.io/?utm_source=prompts.chat" },

        { name: "eachlabs", className: 'py-[6px]', logo: '/sponsors/eachlabs.png', darkLogo: '/sponsors/eachlabs-dark.png', url: "https://www.eachlabs.ai/?utm_source=promptschat&utm_medium=referral" },
        { name: "CommandCode", className: 'py-1', logo: '/sponsors/commandcode.svg', darkLogo: '/sponsors/commandcode-dark.svg', url: "https://commandcode.ai/?utm_source=prompts.chat" },
      ],
    },
  },
});

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

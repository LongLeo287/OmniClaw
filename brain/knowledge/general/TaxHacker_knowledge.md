---
id: taxhacker-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:21.143711
---

# KNOWLEDGE EXTRACT: TaxHacker
> **Extracted on:** 2026-03-30 13:51:12
> **Source:** TaxHacker

---

## File: `.dockerignore`
```
.git
.github
node_modules
.next
*.log
.env*
.DS_Store
upload
data
```

## File: `.env.example`
```
PORT=7331
SELF_HOSTED_MODE=true
DISABLE_SIGNUP=true

UPLOAD_PATH="./data/uploads"
DATABASE_URL="postgresql://user@localhost:5432/taxhacker"

# You can put it here or the app will ask you to enter it
OPENAI_MODEL_NAME="gpt-4o-mini"
OPENAI_API_KEY=""  # "sk-..."

GOOGLE_MODEL_NAME="gemini-2.5-flash"
GOOGLE_API_KEY=""

MISTRAL_MODEL_NAME="mistral-medium-latest"
MISTRAL_API_KEY=""

# Auth Config
BETTER_AUTH_SECRET="random-secret-key"  # please use any long random string here

# Stripe Configuration
STRIPE_SECRET_KEY=""  # "sk_live_..." or "sk_test_..."
STRIPE_WEBHOOK_SECRET=""  # "whsec_..."

# Resend Configuration (optional, use if you want to send emails)
RESEND_API_KEY=""  # "re_..."
RESEND_AUDIENCE_ID=""  # "aud_..."
RESEND_FROM_EMAIL="TaxHacker <user@localhost>"
```

## File: `.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# data directory
/data/*

# dependencies
/node_modules
/.pnp
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/versions

# testing
/coverage

# next.js
/.next/
/out/

# production
/build
/dist
/release

# misc
.DS_Store
*.pem
.vscode

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# env files
.env

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts

# databases
prisma/client
pgdata
*.db
*.sqlite
*.sqlite3
*.sqlite-journal
*.db-journal
# Sentry Config File
.env.sentry-build-plugin
```

## File: `.prettierrc`
```
{
  "tabWidth": 2,
  "useTabs": false,
  "semi": false,
  "singleQuote": false,
  "quoteProps": "as-needed",
  "jsxSingleQuote": false,
  "trailingComma": "es5",
  "bracketSpacing": true,
  "bracketSameLine": false,
  "arrowParens": "always",
  "printWidth": 120
}
```

## File: `components.json`
```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true,
    "prefix": ""
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "iconLibrary": "lucide"
}
```

## File: `docker-compose.build.yml`
```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "7331:7331"
    environment:
      - NODE_ENV=production
      - SELF_HOSTED_MODE=true
      - UPLOAD_PATH=/app/data/uploads
      - DATABASE_URL=postgresql://postgres:postgres@postgres:5432/taxhacker
    volumes:
      - ./data:/app/data
    restart: unless-stopped
    logging:
      driver: "local"
      options:
        max-size: "100M"
        max-file: "3"

  postgres:
    image: postgres:17-alpine
    container_name: taxhacker-postgres
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=taxhacker
    volumes:
      - ./pgdata:/var/lib/postgresql/data
    restart: unless-stopped
    ports:
      - "5432:5432"
    logging:
      driver: "local"
      options:
        max-size: "100M"
        max-file: "3"
```

## File: `docker-compose.production.yml`
```yaml
services:
  app:
    image: ghcr.io/vas3k/taxhacker:latest
    container_name: taxhacker_app
    networks:
      - taxhacker_network
    environment:
      - NODE_ENV=production
      - BASE_URL=https://taxhacker.app
      - SELF_HOSTED_MODE=false
      - UPLOAD_PATH=/app/data/uploads
    env_file:
      - .env
    volumes:
      - ./data:/app/data
    restart: unless-stopped
    extra_hosts:
      - "host.docker.internal:host-gateway"
    ports:
      - "127.0.0.1:7331:7331"
    logging:
      driver: "json-file"
      options:
        max-size: "100M"
        max-file: "3"

networks:
  taxhacker_network:
    driver: bridge
```

## File: `docker-compose.yml`
```yaml
services:
  app:
    image: ghcr.io/vas3k/taxhacker:latest
    ports:
      - "7331:7331"
    environment:
      - NODE_ENV=production
      - SELF_HOSTED_MODE=true
      - UPLOAD_PATH=/app/data/uploads
      - DATABASE_URL=postgresql://postgres:postgres@postgres:5432/taxhacker
    volumes:
      - ./data:/app/data
    restart: unless-stopped
    depends_on:
      - postgres
    logging:
      driver: "local"
      options:
        max-size: "100M"
        max-file: "3"

  postgres:
    image: postgres:17-alpine
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=taxhacker
    volumes:
      - ./pgdata:/var/lib/postgresql/data
    restart: unless-stopped
    logging:
      driver: "local"
      options:
        max-size: "100M"
        max-file: "3"
```

## File: `docker-entrypoint.sh`
```bash
#!/bin/sh
set -e

# Extract server part from DATABASE_URL (remove database name)
SERVER_URL=$(echo "$DATABASE_URL" | sed 's/\/[^/]*$//')

# Wait for database to be ready using psql and SERVER_URL
echo "Waiting for PostgreSQL server to be ready at $SERVER_URL..."
until psql "$SERVER_URL" -c '\q' >/dev/null 2>&1; do
  echo "PostgreSQL server is unavailable - sleeping"
  sleep 1
done
echo "PostgreSQL server is ready!"

# Run database migrations
echo "Running database migrations..."
npx prisma generate
npx prisma migrate deploy

# Start the application
echo "Starting the application..."
exec "$@"
```

## File: `Dockerfile`
```
FROM node:23-slim AS base

# Default environment variables
ENV PORT=7331
ENV NODE_ENV=production

# Build stage
FROM base AS builder

# Install dependencies required for Prisma
RUN apt-get update && apt-get install -y openssl

WORKDIR /app

# Copy package files
COPY package*.json ./
COPY prisma ./prisma/

# Install dependencies
RUN npm ci

# Copy source code
COPY . .

# Build the application
RUN npm run build

# Production stage
FROM base

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    ghostscript \
    graphicsmagick \
    openssl \
    libwebp-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create upload directory and set permissions
RUN mkdir -p /app/upload

# Copy built assets from builder
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/prisma ./prisma
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/app ./app
COPY --from=builder /app/next.config.ts ./

# Copy and set up entrypoint script
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Create directory for uploads
RUN mkdir -p /app/data

EXPOSE 7331

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["npm", "start"]
```

## File: `eslint.config.mjs`
```
import { dirname } from "path";
import { fileURLToPath } from "url";
import { FlatCompat } from "@eslint/eslintrc";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: __dirname,
});

const eslintConfig = [
  ...compat.extends("next/core-web-vitals", "next/typescript"),
];

export default eslintConfig;
```

## File: `instrumentation-client.ts`
```typescript
import * as Sentry from "@sentry/nextjs"

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
})
```

## File: `instrumentation.ts`
```typescript
import * as Sentry from '@sentry/nextjs';

export async function register() {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    await import('./sentry.server.config');
  }

  if (process.env.NEXT_RUNTIME === 'edge') {
    await import('./sentry.edge.config');
  }
}

export const onRequestError = Sentry.captureRequestError;
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Vasily Zubarev, me@vas3k.ru

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `middleware.ts`
```typescript
import { default as globalConfig } from "@/lib/config"
import { getSessionCookie } from "better-auth/cookies"
import { NextRequest, NextResponse } from "next/server"

export default async function middleware(request: NextRequest) {
  if (globalConfig.selfHosted.isEnabled) {
    return NextResponse.next()
  }

  const sessionCookie = getSessionCookie(request, { cookiePrefix: "taxhacker" })
  if (!sessionCookie) {
    return NextResponse.redirect(new URL(globalConfig.auth.loginUrl, request.url))
  }
  return NextResponse.next()
}

export const config = {
  matcher: [
    "/transactions/:path*",
    "/settings/:path*",
    "/export/:path*",
    "/import/:path*",
    "/unsorted/:path*",
    "/files/:path*",
    "/dashboard/:path*",
  ],
}
```

## File: `next.config.ts`
```typescript
import { withSentryConfig } from "@sentry/nextjs"
import type { NextConfig } from "next"

const nextConfig: NextConfig = {
  eslint: {
    ignoreDuringBuilds: true, // TODO: make me linting again
  },
  images: {
    unoptimized: true, // FIXME: bug on prod, images always empty, investigate later
  },
  experimental: {
    serverActions: {
      bodySizeLimit: "256mb",
    },
  },
}

const isSentryEnabled = process.env.NEXT_PUBLIC_SENTRY_DSN && process.env.SENTRY_ORG && process.env.SENTRY_PROJECT

export default isSentryEnabled
  ? withSentryConfig(nextConfig, {
      silent: !process.env.CI,
      org: process.env.SENTRY_ORG,
      project: process.env.SENTRY_PROJECT,
      disableLogger: true,
      widenClientFileUpload: true,
      tunnelRoute: "/monitoring",
    })
  : nextConfig
```

## File: `package.json`
```json
{
  "name": "taxhacker",
  "version": "0.5.5",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "next dev -p 7331 --turbopack",
    "build": "next build",
    "start": "prisma migrate deploy && next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@dnd-kit/core": "^6.3.1",
    "@dnd-kit/sortable": "^10.0.0",
    "@fast-csv/format": "^5.0.2",
    "@fast-csv/parse": "^5.0.2",
    "@langchain/google-genai": "^0.2.14",
    "@langchain/mistralai": "^0.2.1",
    "@langchain/openai": "^0.6.1",
    "@prisma/client": "^6.6.0",
    "@radix-ui/react-avatar": "^1.1.3",
    "@radix-ui/react-checkbox": "^1.1.4",
    "@radix-ui/react-collapsible": "^1.1.3",
    "@radix-ui/react-dialog": "^1.1.6",
    "@radix-ui/react-dropdown-menu": "^2.1.6",
    "@radix-ui/react-label": "^2.1.2",
    "@radix-ui/react-popover": "^1.1.6",
    "@radix-ui/react-select": "^2.1.6",
    "@radix-ui/react-separator": "^1.1.2",
    "@radix-ui/react-slot": "^1.2.0",
    "@radix-ui/react-tooltip": "^1.1.8",
    "@radix-ui/colors": "^3.0.0",
    "@react-pdf/renderer": "^4.3.0",
    "@sentry/nextjs": "^9.11.0",
    "@types/mime-types": "^2.1.4",
    "@types/sharp": "^0.31.1",
    "better-auth": "^1.2.10",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "date-fns": "^3.6.0",
    "jszip": "^3.10.1",
    "langchain": "^0.3.30",
    "lucide-react": "^0.475.0",
    "mime-types": "^3.0.1",
    "next": "^15.2.4",
    "next-themes": "^0.4.4",
    "pdf2pic": "^3.1.4",
    "react": "^19.0.0",
    "react-day-picker": "^8.10.1",
    "react-dom": "^19.0.0",
    "react-resizable-panels": "^2.1.7",
    "resend": "^4.2.0",
    "sharp": "^0.33.5",
    "slugify": "^1.6.6",
    "sonner": "^2.0.1",
    "stripe": "^18.0.0",
    "tailwind-merge": "^3.0.1",
    "tailwindcss-animate": "^1.0.7",
    "zod": "^3.24.2"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^9",
    "eslint-config-next": "15.1.7",
    "postcss": "^8",
    "prisma": "^6.6.0",
    "tailwindcss": "^3.4.1",
    "typescript": "^5"
  },
  "overrides": {
    "react-day-picker": {
      "react": "^19.0.0"
    }
  }
}
```

## File: `postcss.config.mjs`
```
/** @type {import('postcss-load-config').Config} */
const config = {
  plugins: {
    tailwindcss: {},
  },
};

export default config;
```

## File: `README.md`
```markdown
<div align="center"><a name="readme-top"></a>

<img src="public/logo/512.png" alt="" width="320">

<br>

# TaxHacker — self-hosted AI accountant

[![GitHub Stars](https://img.shields.io/github/stars/vas3k/TaxHacker?color=ffcb47&labelColor=black&style=flat-square)](https://github.com/vas3k/TaxHacker/stargazers)
[![License](https://img.shields.io/badge/license-MIT-ffcb47?labelColor=black&style=flat-square)](https://github.com/vas3k/TaxHacker/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/vas3k/TaxHacker?color=ff80eb&labelColor=black&style=flat-square)](https://github.com/vas3k/TaxHacker/issues)
[![Donate](https://img.shields.io/badge/-Donate-f04f88?logo=githubsponsors&logoColor=white&style=flat-square)](https://vas3k.com/donate/)

</div>

> 🙏 I'm currently looking for a job! Here's [my CV](https://raw.githubusercontent.com/vas3k/vas3k/master/cv.pdf) and my [Github profile](https://github.com/vas3k).

TaxHacker is a self-hosted accounting app designed for freelancers, indie hackers, and small businesses who want to save time and automate expense and income tracking using the power of modern AI.

Upload photos of receipts, invoices, or PDFs, and TaxHacker will automatically recognize and extract all the important data you need for accounting: product names, amounts, items, dates, merchants, taxes, and save it into a structured Excel-like database. You can even create custom fields with your own AI prompts to extract any specific information you need.

The app features automatic currency conversion (including crypto!) based on historical exchange rates from the transaction date. With built-in filtering, multi-project support, import/export capabilities, and custom categories, TaxHacker simplifies reporting and makes tax filing a bit easier.

> 🎥 [Watch demo video](https://taxhacker.app/landing/video.mp4)

![Dashboard](public/landing/main-page.webp)

> \[!IMPORTANT]
>
> This project is still in early development. Use at your own risk! **Star us** to get notified about new features and bugfixes ⭐️

## ✨ Features

### `1` Analyze photos and invoices with AI

![Currency Conversion](public/landing/ai-scanner-big.webp)

Snap a photo of any receipt or upload an invoice PDF, and TaxHacker will automatically recognize, extract, categorize, and store all the information in a structured database.

- **Upload and organize your docs**: Store multiple documents in "unsorted" until you're ready to process them manually or with AI assistance
- **AI data extraction**: Use AI to automatically pull key information like dates, amounts, vendors, and line items
- **Auto-categorization**: Transactions are automatically sorted into relevant categories based on their content
- **Item splitting**: Extract individual items from invoices and split them into separate transactions when needed
- **Structured storage**: Everything gets saved in an organized database for easy filtering and retrieval
- **Customizable AI providers**: Choose from OpenAI, Google Gemini, or Mistral (local LLM support coming soon)

TaxHacker works with a wide variety of documents, including store receipts, restaurant bills, invoices, bank statements, letters, even handwritten receipts. It handles any language and any currency with ease.

### `2` Multi-currency support with automatic conversion (even crypto!)

![Currency Conversion](public/landing/multi-currency.webp)

TaxHacker automatically detects currencies in your documents and converts them to your base currency using historical exchange rates.

- **Foreight currency detection**: Automatically identify the currency used in any document
- **Historical rates**: Get conversion rates from the actual transaction date
- **All-world coverage**: Support for 170+ world currencies and 14 popular cryptocurrencies (BTC, ETH, LTC, DOT, and more)
- **Flexible input**: Manual entry is always available when you need more control

### `3` Organize your transactions using fully customizable categories, projects and fields

![Transactions Table](public/landing/transactions-big.webp)

Adapt TaxHacker to your unique needs with unlimited customization options. Create custom fields, projects, and categories that better suit your specific needs, idustry standards or country.

- **Custom categories and projecst**: Create your own categories and projects to group your transactions in any convenient way
- **Custom fields**: You can create unlimited number of custom fields to extraxt more information from your invoices (it's like creating extra columns in Excel)
- **Full-text search**: Search through the actual content of recognized documents
- **Advanced filtering**: Find exactly what you need with search and filter options
- **AI-powered extraction**: Write your own prompts to extract any custom information from documents
- **Bulk operations**: Process multiple documents or transactions at once

### `4` Customize any LLM prompt. Even system ones

![Custom Categories](public/landing/custom-llm.webp)

Take full control of how TaxHacker's AI processes your documents. Write custom AI prompts for fields, categories, and projects, or modify the built-in ones to match your specific needs.

- **Customizable system prompts**: Modify the general prompt template in settings to suit your business
- **Field or project-specific prompts**: Create custom extraction rules for your industry-specific documents
- **Full control**: Adjust field extraction priorities and naming conventions to match your workflow
- **Industry optimization**: Fine-tune the AI to understand your specific type of business documents
- **Full transparency**: Every aspect of the AI extraction process is under your control and can be changed right in settings

TaxHacker is 100% adaptable and tunable to your unique requirements — whether you need to extract emails, addresses, project codes, or any other custom information from your documents.

### `5` Flexible data filtering and export

![Data Export](public/landing/export.webp)

Once your documents are processed, easily view, filter, and export your complete transaction history exactly how you need it.

- **Advanced filtering**: Filter by date ranges, categories, projects, amounts, and any custom fields
- **Flexible exports**: Export filtered transactions to CSV with all attached documents included
- **Tax-ready reports**: Generate comprehensive reports for your accountant or tax advisor
- **Data portability**: Download complete data archives to migrate to other services—your data stays yours

### `6` Self-hosted mode for data privacy

![Self-hosting](docs/screenshots/exported_archive.png)

Keep complete control over your financial data with local storage and self-hosting options. TaxHacker respects your privacy and gives you full ownership of your information.

- **Home server ready**: Host on your own infrastructure for maximum privacy and control
- **Docker native**: Simple setup with provided Docker containers and compose files
- **Data ownership**: Your financial documents never leaves your control
- **No vendor lock-in**: Export everything and migrate whenever you want
- **Transparent operations**: Full access to source code and complete operational transparency

## 🛳 Deployment and Self-hosting

TaxHacker can be easily self-hosted on your own infrastructure for complete control over your data and application environment. We provide a [Docker image](./Dockerfile) and [Docker Compose](./docker-compose.yml) setup that makes deployment simple:

```bash
curl -O https://raw.githubusercontent.com/vas3k/TaxHacker/main/docker-compose.yml

docker compose up
```

The Docker Compose setup includes:

- TaxHacker application container
- PostgreSQL 17 database (or connect to your existing database)
- Automatic database migrations on startup
- Volume mounts for persistent data storage
- Production-ready configuration

New Docker images are automatically built and published with every release. You can use specific version tags (e.g., `v1.0.0`) or `latest` for the most recent version.

For advanced setups, you can customize the Docker Compose configuration to fit your infrastructure. The default configuration uses the pre-built image from GitHub Container Registry, but you can also build locally using the provided [Dockerfile](./Dockerfile).

Example custom configuration:

```yaml
services:
  app:
    image: ghcr.io/vas3k/taxhacker:latest
    ports:
      - "7331:7331"
    environment:
      - SELF_HOSTED_MODE=true
      - UPLOAD_PATH=/app/data/uploads
      - DATABASE_URL=postgresql://postgres:postgres@localhost:5432/taxhacker
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

### Environment Variables

Configure TaxHacker for your specific needs with these environment variables:

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `UPLOAD_PATH` | Yes | Local directory for file uploads and storage | `./data/uploads` |
| `DATABASE_URL` | Yes | PostgreSQL connection string | `postgresql://user@localhost:5432/taxhacker` |
| `PORT` | No | Port to run the application on | `7331` (default) |
| `BASE_URL` | No | Base URL for the application | `http://localhost:7331` |
| `SELF_HOSTED_MODE` | No | Set to "true" for self-hosting: enables auto-login, custom API keys, and additional features | `true` |
| `DISABLE_SIGNUP` | No | Disable new user registration on your instance | `false` |
| `BETTER_AUTH_SECRET` | Yes | Secret key for authentication (minimum 16 characters) | `your-secure-random-key` |

You can also configure LLM provider settings in the application or via environment variables:

- **OpenAI**: `OPENAI_MODEL_NAME` and `OPENAI_API_KEY`
- **Google Gemini**: `GOOGLE_MODEL_NAME` and `GOOGLE_API_KEY`
- **Mistral**: `MISTRAL_MODEL_NAME` and `MISTRAL_API_KEY`

## ⌨️ Local Development

We use:

- **Next.js 15+** for the frontend and API
- **Prisma** for database models and migrations
- **PostgreSQL** as the database (PostgreSQL 17+ recommended)
- **Ghostscript and GraphicsMagick** for PDF processing (install on macOS via `brew install gs graphicsmagick`)

Set up your local development environment:

```bash
# Clone the repository
git clone https://github.com/vas3k/TaxHacker.git
cd TaxHacker

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env

# Edit .env with your configuration
# Make sure to set DATABASE_URL to your PostgreSQL connection string
# Example: postgresql://user@localhost:5432/taxhacker

# Initialize the database
npx prisma generate && npx prisma migrate dev

# Start the development server
npm run dev
```

Visit `http://localhost:7331` to see your local TaxHacker instance in action.

For a production build, instead of `npm run dev` use the following commands:

```bash
# Build the application
npm run build

# Start the production server
npm run start
```

## 🤝 Contributing

We welcome contributions to TaxHacker! Here's how you can help make it even better:

- **🐛 Bug Reports**: File detailed issues when you encounter problems
- **💡 Feature Requests**: Share your ideas for new features and improvements
- **🔧 Code Contributions**: Submit pull requests to improve the application
- **📚 Documentation**: Help improve documentation and guides
- **🎥 Content Creation**: Videos, tutorials, and reviews help us reach more users!

All development happens on GitHub through issues and pull requests. We appreciate any help.

[![PRs Welcome](https://img.shields.io/badge/🤯_PRs-welcome-ffcb47?labelColor=black&style=for-the-badge)](https://github.com/vas3k/TaxHacker/pulls)

## ❤️ Support the Project

If TaxHacker has helped you save time or manage your finances better, consider supporting its continued development! Your donations help us maintain the project, add new features, and keep it free and open source. Every contribution helps ensure we can keep improving and maintaining this tool for the community.

[![Thank the TaxHacker devs](https://img.shields.io/badge/❤️-donate%20to%20Taxhacker%20devs-f08080?labelColor=black&style=for-the-badge)](https://vas3k.com/donate/)

## 📄 License

TaxHacker is licensed under the [MIT License](LICENSE).
```

## File: `sentry.edge.config.ts`
```typescript
// This file configures the initialization of Sentry for edge features (middleware, edge routes, and so on).
// The config you add here will be used whenever one of the edge features is loaded.
// Note that this config is unrelated to the Vercel Edge Runtime and is also required when running locally.
// https://docs.sentry.io/platforms/javascript/guides/nextjs/

import * as Sentry from "@sentry/nextjs"

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,

  // Define how likely traces are sampled. Adjust this value in production, or use tracesSampler for greater control.
  tracesSampleRate: 1,

  // Setting this option to true will print useful information to the console while you're setting up Sentry.
  debug: false,
})
```

## File: `sentry.server.config.ts`
```typescript
// This file configures the initialization of Sentry on the server.
// The config you add here will be used whenever the server handles a request.
// https://docs.sentry.io/platforms/javascript/guides/nextjs/

import * as Sentry from "@sentry/nextjs"

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,

  // Define how likely traces are sampled. Adjust this value in production, or use tracesSampler for greater control.
  tracesSampleRate: 1,

  // Setting this option to true will print useful information to the console while you're setting up Sentry.
  debug: false,
})
```

## File: `tailwind.config.ts`
```typescript
import type { Config } from "tailwindcss"

export default {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        chart: {
          "1": "hsl(var(--chart-1))",
          "2": "hsl(var(--chart-2))",
          "3": "hsl(var(--chart-3))",
          "4": "hsl(var(--chart-4))",
          "5": "hsl(var(--chart-5))",
        },
        sidebar: {
          DEFAULT: "hsl(var(--sidebar-background))",
          foreground: "hsl(var(--sidebar-foreground))",
          primary: "hsl(var(--sidebar-primary))",
          "primary-foreground": "hsl(var(--sidebar-primary-foreground))",
          accent: "hsl(var(--sidebar-accent))",
          "accent-foreground": "hsl(var(--sidebar-accent-foreground))",
          border: "hsl(var(--sidebar-border))",
          ring: "hsl(var(--sidebar-ring))",
        },
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
} satisfies Config
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

## File: `ai/analyze.ts`
```typescript
"use server"

import { ActionState } from "@/lib/actions"
import { updateFile } from "@/models/files"
import { getLLMSettings, getSettings } from "@/models/settings"
import { AnalyzeAttachment } from "./attachments"
import { requestLLM } from "./providers/llmProvider"

export type AnalysisResult = {
  output: Record<string, string>
  tokensUsed: number
}

export async function analyzeTransaction(
  prompt: string,
  schema: Record<string, unknown>,
  attachments: AnalyzeAttachment[],
  fileId: string,
  userId: string
): Promise<ActionState<AnalysisResult>> {
  const settings = await getSettings(userId)
  const llmSettings = getLLMSettings(settings)

  try {
    const response = await requestLLM(llmSettings, {
      prompt,
      schema,
      attachments,
    })

    if (response.error) {
      throw new Error(response.error)
    }

    const result = response.output
    const tokensUsed = response.tokensUsed || 0

    console.log("LLM response:", result)
    console.log("LLM tokens used:", tokensUsed)

    await updateFile(fileId, userId, { cachedParseResult: result })

    return {
      success: true,
      data: {
        output: result,
        tokensUsed: tokensUsed,
      },
    }
  } catch (error) {
    console.error("AI Analysis error:", error)
    return {
      success: false,
      error: error instanceof Error ? error.message : "Failed to analyze invoice",
    }
  }
}
```

## File: `ai/attachments.ts`
```typescript
import { fileExists, fullPathForFile } from "@/lib/files"
import { generateFilePreviews } from "@/lib/previews/generate"
import { File, User } from "@/prisma/client"
import fs from "fs/promises"

const MAX_PAGES_TO_ANALYZE = 4

export type AnalyzeAttachment = {
  filename: string
  contentType: string
  base64: string
}

export const loadAttachmentsForAI = async (user: User, file: File): Promise<AnalyzeAttachment[]> => {
  const fullFilePath = fullPathForFile(user, file)
  const isFileExists = await fileExists(fullFilePath)
  if (!isFileExists) {
    throw new Error("File not found on disk")
  }

  const { contentType, previews } = await generateFilePreviews(user, fullFilePath, file.mimetype)

  return Promise.all(
    previews.slice(0, MAX_PAGES_TO_ANALYZE).map(async (preview) => ({
      filename: file.filename,
      contentType: contentType,
      base64: await loadFileAsBase64(preview),
    }))
  )
}

export const loadFileAsBase64 = async (filePath: string): Promise<string> => {
  const buffer = await fs.readFile(filePath)
  return Buffer.from(buffer).toString("base64")
}
```

## File: `ai/prompt.ts`
```typescript
import { Category, Field, Project } from "@/prisma/client"

export function buildLLMPrompt(
  promptTemplate: string,
  fields: Field[],
  categories: Category[] = [],
  projects: Project[] = []
) {
  let prompt = promptTemplate

  prompt = prompt.replace(
    "{fields}",
    fields
      .filter((field) => field.llm_prompt)
      .map((field) => `- ${field.code}: ${field.llm_prompt}`)
      .join("\n")
  )

  prompt = prompt.replace(
    "{categories}",
    categories
      .filter((category) => category.llm_prompt)
      .map((category) => `- ${category.code}: for ${category.llm_prompt}`)
      .join("\n")
  )

  prompt = prompt.replace(
    "{projects}",
    projects
      .filter((project) => project.llm_prompt)
      .map((project) => `- ${project.code}: for ${project.llm_prompt}`)
      .join("\n")
  )

  prompt = prompt.replace("{categories.code}", categories.map((category) => `${category.code}`).join(", "))
  prompt = prompt.replace("{projects.code}", projects.map((project) => `${project.code}`).join(", "))

  return prompt
}
```

## File: `ai/schema.ts`
```typescript
import { Field } from "@/prisma/client"

export const fieldsToJsonSchema = (fields: Field[]) => {
  const fieldsWithPrompt = fields.filter((field) => field.llm_prompt)
  const schemaProperties = fieldsWithPrompt.reduce(
    (acc, field) => {
      acc[field.code] = { type: field.type, description: field.llm_prompt || "" }
      return acc
    },
    {} as Record<string, { type: string; description: string }>
  )

  const schema = {
    type: "object",
    properties: {
      ...schemaProperties,
      items: {
        type: "array",
        description:
          "Separate items, products or transactions in the file which have own name and price or sum. Find all items!",
        items: {
          type: "object",
          properties: schemaProperties,
          required: [...Object.keys(schemaProperties)],
          additionalProperties: false,
        },
      },
    },
    required: [...Object.keys(schemaProperties), "items"],
    additionalProperties: false,
  }

  return schema
}
```

## File: `ai/providers/llmProvider.ts`
```typescript
import { ChatOpenAI } from "@langchain/openai"
import { ChatGoogleGenerativeAI } from "@langchain/google-genai"
import { ChatMistralAI } from "@langchain/mistralai"
import { BaseMessage, HumanMessage } from "@langchain/core/messages"

export type LLMProvider = "openai" | "google" | "mistral"

export interface LLMConfig {
  provider: LLMProvider
  apiKey: string
  model: string
}

export interface LLMSettings {
  providers: LLMConfig[]
}

export interface LLMRequest {
  prompt: string
  schema?: Record<string, unknown>
  attachments?: any[]
}

export interface LLMResponse {
  output: Record<string, string>
  tokensUsed?: number
  provider: LLMProvider
  error?: string
}

async function requestLLMUnified(config: LLMConfig, req: LLMRequest): Promise<LLMResponse> {
  try {
    const temperature = 0
    let model: any
    if (config.provider === "openai") {
      model = new ChatOpenAI({
        apiKey: config.apiKey,
        model: config.model,
        temperature: temperature,
      })
    } else if (config.provider === "google") {
      model = new ChatGoogleGenerativeAI({
        apiKey: config.apiKey,
        model: config.model,
        temperature: temperature,
      })
    } else if (config.provider === "mistral") {
      model = new ChatMistralAI({
        apiKey: config.apiKey,
        model: config.model,
        temperature: temperature,
      })
    } else {
      return {
        output: {},
        provider: config.provider,
        error: "Unknown provider",
      }
    }

    const structuredModel = model.withStructuredOutput(req.schema, { name: "transaction" })

    let message_content: any = [{ type: "text", text: req.prompt }]
    if (req.attachments && req.attachments.length > 0) {
      const images = req.attachments.map((att) => ({
        type: "image_url",
        image_url: {
          url: `data:${att.contentType};base64,${att.base64}`,
        },
      }))
      message_content.push(...images)
    }
    const messages: BaseMessage[] = [new HumanMessage({ content: message_content })]

    const response = await structuredModel.invoke(messages)

    return {
      output: response,
      provider: config.provider,
    }
  } catch (error: any) {
    return {
      output: {},
      provider: config.provider,
      error: error instanceof Error ? error.message : `${config.provider} request failed`,
    }
  }
}

export async function requestLLM(settings: LLMSettings, req: LLMRequest): Promise<LLMResponse> {
  for (const config of settings.providers) {
    if (!config.apiKey || !config.model) {
      console.info("Skipping provider:", config.provider)
      continue
    }
    console.info("Use provider:", config.provider)

    const response = await requestLLMUnified(config, req)

    if (!response.error) {
      return response
    } else {
      console.error(response.error)
    }
  }

  return {
    output: {},
    provider: settings.providers[0]?.provider || "openai",
    error: "All LLM providers failed or are not configured",
  }
}
```

## File: `app/global-error.tsx`
```tsx
"use client"

import { Button } from "@/components/ui/button"
import * as Sentry from "@sentry/nextjs"
import { Ghost } from "lucide-react"
import Link from "next/link"
import { useEffect } from "react"

export default function GlobalError({ error }: { error: Error }) {
  useEffect(() => {
    Sentry.captureException(error)
  }, [error])

  return (
    <html>
      <body>
        <div className="min-h-screen flex flex-col items-center justify-center bg-background p-4">
          <div className="text-center space-y-4">
            <Ghost className="w-24 h-24 text-destructive mx-auto" />
            <h1 className="text-4xl font-bold text-foreground">Oops! Something went wrong</h1>
            <p className="text-muted-foreground max-w-md mx-auto">
              We apologize for the inconvenience. Our team has been notified and is working to fix the issue.
            </p>
            <div className="pt-4">
              <Button asChild>
                <Link href="/">Go Home</Link>
              </Button>
            </div>
          </div>
        </div>
      </body>
    </html>
  )
}
```

## File: `app/globals.css`
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  :root {
    --background: 0 0% 100%;
    --foreground: 240 10% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 240 10% 3.9%;
    --popover: 0 0% 100%;
    --popover-foreground: 240 10% 3.9%;
    --primary: 240 5.9% 10%;
    --primary-foreground: 0 0% 98%;
    --secondary: 240 4.8% 95.9%;
    --secondary-foreground: 240 5.9% 10%;
    --muted: 240 4.8% 95.9%;
    --muted-foreground: 240 3.8% 46.1%;
    --accent: 240 4.8% 95.9%;
    --accent-foreground: 240 5.9% 10%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 0 0% 98%;
    --border: 240 5.9% 90%;
    --input: 240 5.9% 90%;
    --ring: 240 10% 3.9%;
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
    --chart-3: 197 37% 24%;
    --chart-4: 43 74% 66%;
    --chart-5: 27 87% 67%;
    --radius: 0.5rem;
    --sidebar-background: 200 13% 93%;
    --sidebar-foreground: 200 10% 30%;
    --sidebar-primary: 200 13% 80%;
    --sidebar-primary-foreground: 0 0% 98%;
    --sidebar-accent: 240 5.9% 10%;
    --sidebar-accent-foreground: 0 0% 98%;
    --sidebar-border: 200 13% 85%;
    --sidebar-ring: 200 13% 80%;
  }

  .dark {
    --background: 240 10% 3.9%;
    --foreground: 0 0% 98%;
    --card: 240 10% 3.9%;
    --card-foreground: 0 0% 98%;
    --popover: 240 10% 3.9%;
    --popover-foreground: 0 0% 98%;
    --primary: 0 0% 98%;
    --primary-foreground: 240 5.9% 10%;
    --secondary: 240 3.7% 15.9%;
    --secondary-foreground: 0 0% 98%;
    --muted: 240 3.7% 15.9%;
    --muted-foreground: 240 5% 64.9%;
    --accent: 240 3.7% 15.9%;
    --accent-foreground: 0 0% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 0 0% 98%;
    --border: 240 3.7% 15.9%;
    --input: 240 3.7% 15.9%;
    --ring: 240 4.9% 83.9%;
    --chart-1: 220 70% 50%;
    --chart-2: 160 60% 45%;
    --chart-3: 30 80% 55%;
    --chart-4: 280 65% 60%;
    --chart-5: 340 75% 55%;
    --sidebar-background: 200 13% 20%;
    --sidebar-foreground: 200 10% 90%;
    --sidebar-primary: 200 13% 60%;
    --sidebar-primary-foreground: 0 0% 100%;
    --sidebar-accent: 240 5.9% 10%;
    --sidebar-accent-foreground: 0 0% 98%;
    --sidebar-border: 200 13% 25%;
    --sidebar-ring: 200 13% 60%;
  }
}

@layer base {
  * {
    @apply border-border outline-ring/50;
  }
  body {
    @apply bg-background text-foreground;
  }
  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    appearance: none;
    margin: 0;
  }
  input[type="number"] {
    -moz-appearance: textfield;
  }
}
```

## File: `app/layout.tsx`
```tsx
import config from "@/lib/config"
import type { Metadata, Viewport } from "next"
import "./globals.css"

export const metadata: Metadata = {
  title: {
    template: "%s | TaxHacker",
    default: config.app.title,
  },
  description: config.app.description,
  icons: {
    icon: "/favicon.ico",
    shortcut: "/favicon.ico",
    apple: "/apple-touch-icon.png",
  },
  manifest: "/site.webmanifest",
  metadataBase: new URL(config.app.baseURL),
  openGraph: {
    type: "website",
    locale: "en_US",
    url: config.app.baseURL,
    title: config.app.title,
    description: config.app.description,
    siteName: config.app.title,
  },
  twitter: {
    card: "summary_large_image",
    title: config.app.title,
    description: config.app.description,
  },
  robots: {
    index: true,
    follow: true,
  },
}

export const viewport: Viewport = {
  themeColor: "#ffffff",
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
  userScalable: false,
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-white antialiased">{children}</body>
    </html>
  )
}
```

## File: `app/loading.tsx`
```tsx
import { Loader2 } from "lucide-react"

export default function AppLoading() {
  return (
    <div className="absolute inset-0 flex items-center justify-center h-full w-full">
      <Loader2 className="w-10 h-10 animate-spin text-muted-foreground" />
    </div>
  )
}
```

## File: `app/page.tsx`
```tsx
import LandingPage from "@/app/landing/landing"
import { getSession } from "@/lib/auth"
import config from "@/lib/config"
import { redirect } from "next/navigation"

export default async function Home() {
  const session = await getSession()
  if (!session) {
    if (config.selfHosted.isEnabled) {
      redirect(config.selfHosted.redirectUrl)
    }
    return <LandingPage />
  }

  redirect("/dashboard")
}

export const dynamic = "force-dynamic"
```

## File: `app/(app)/context.tsx`
```tsx
"use client"

import { Check, X, Trash2 } from "lucide-react"
import { createContext, ReactNode, useContext, useState } from "react"

type BannerType = "success" | "deleted" | "failed" | "default"

type Notification = {
  code: string
  message: string
  type?: BannerType
}

type NotificationContextType = {
  notification: Notification | null
  showNotification: (notification: Notification) => void
}

const NotificationContext = createContext<NotificationContextType>({
  notification: null,
  showNotification: () => {},
})

export function NotificationProvider({ children }: { children: ReactNode }) {
  const [notification, setNotification] = useState<Notification | null>(null)

  const showNotification = (notification: Notification) => {
    setNotification(notification)
    if (notification.code === "global.banner") {
      setTimeout(() => setNotification(null), 2000)
    }
  }

  const getBannerStyles = (type: BannerType = "default") => {
    switch (type) {
      case "success":
        return "bg-green-500 text-teal-50"
      case "deleted":
        return "bg-black text-white"
      case "failed":
        return "bg-red-500 text-white"
      case "default":
        return "bg-white text-black"
    }
  }

  const getBannerIcon = (type: BannerType = "default") => {
    switch (type) {
      case "success":
        return <Check className="h-10 w-10 animate-bounce" />
      case "deleted":
        return <Trash2 className="h-10 w-10 animate-bounce" />
      case "failed":
        return <X className="h-10 w-10 animate-bounce" />
      case "default":
        return null
    }
  }

  return (
    <NotificationContext.Provider value={{ notification, showNotification }}>
      {children}
      {notification?.code === "global.banner" && (
        <div className="fixed inset-0 flex items-center justify-center z-50">
          <div
            className={`border rounded-lg p-8 flex flex-col items-center justify-center gap-4 shadow-lg h-[160px] w-[160px] ${getBannerStyles(notification.type)}`}
          >
            {getBannerIcon(notification.type)}
            <p className="text-xl font-medium">{notification.message}</p>
          </div>
        </div>
      )}
    </NotificationContext.Provider>
  )
}

export const useNotification = () => useContext(NotificationContext)
```

## File: `app/(app)/layout.tsx`
```tsx
import { SubscriptionExpired } from "@/components/auth/subscription-expired"
import ScreenDropArea from "@/components/files/screen-drop-area"
import MobileMenu from "@/components/sidebar/mobile-menu"
import { AppSidebar } from "@/components/sidebar/sidebar"
import { SidebarInset, SidebarProvider } from "@/components/ui/sidebar"
import { Toaster } from "@/components/ui/sonner"
import { getCurrentUser, isSubscriptionExpired } from "@/lib/auth"
import config from "@/lib/config"
import { getUnsortedFilesCount } from "@/models/files"
import type { Metadata, Viewport } from "next"
import "../globals.css"
import { NotificationProvider } from "./context"

export const metadata: Metadata = {
  title: {
    template: "%s | TaxHacker",
    default: config.app.title,
  },
  description: config.app.description,
  icons: {
    icon: "/favicon.ico",
    shortcut: "/favicon.ico",
    apple: "/apple-touch-icon.png",
  },
  manifest: "/site.webmanifest",
}

export const viewport: Viewport = {
  themeColor: "#ffffff",
}

export default async function RootLayout({ children }: { children: React.ReactNode }) {
  const user = await getCurrentUser()
  const unsortedFilesCount = await getUnsortedFilesCount(user.id)

  const userProfile = {
    id: user.id,
    name: user.name || "",
    email: user.email,
    avatar: user.avatar ? user.avatar + "?" + user.id : undefined,
    membershipPlan: user.membershipPlan || "unlimited",
    storageUsed: user.storageUsed || 0,
    storageLimit: user.storageLimit || -1,
    aiBalance: user.aiBalance || 0,
  }

  return (
    <NotificationProvider>
      <ScreenDropArea>
        <SidebarProvider>
          <MobileMenu unsortedFilesCount={unsortedFilesCount} />
          <AppSidebar
            profile={userProfile}
            unsortedFilesCount={unsortedFilesCount}
            isSelfHosted={config.selfHosted.isEnabled}
          />
          <SidebarInset className="w-full h-full mt-[60px] md:mt-0 overflow-auto">
            {isSubscriptionExpired(user) && <SubscriptionExpired />}
            {children}
          </SidebarInset>
        </SidebarProvider>
        <Toaster />
      </ScreenDropArea>
    </NotificationProvider>
  )
}

export const dynamic = "force-dynamic"
```

## File: `app/(app)/apps/common.ts`
```typescript
import fs from "fs/promises"
import path from "path"

export type AppManifest = {
  name: string
  description: string
  icon: string
}

export async function getApps(): Promise<{ id: string; manifest: AppManifest }[]> {
  const appsDir = path.join(process.cwd(), "app/(app)/apps")
  const items = await fs.readdir(appsDir, { withFileTypes: true })

  const apps = await Promise.all(
    items
      .filter((item) => item.isDirectory() && item.name !== "apps")
      .map(async (item) => {
        const manifestModule = await import(`./${item.name}/manifest`)
        return {
          id: item.name,
          manifest: manifestModule.manifest as AppManifest,
        }
      })
  )

  return apps
}
```

## File: `app/(app)/apps/layout.tsx`
```tsx
export default async function AppsLayout({ children }: { children: React.ReactNode }) {
  return <div className="flex flex-col gap-4 p-4">{children}</div>
}
```

## File: `app/(app)/apps/page.tsx`
```tsx
import Link from "next/link"
import { getApps } from "./common"

export default async function AppsPage() {
  const apps = await getApps()

  return (
    <>
      <header className="flex flex-wrap items-center justify-between gap-2 mb-8">
        <h2 className="flex flex-row gap-3 md:gap-5">
          <span className="text-3xl font-bold tracking-tight">Apps</span>
          <span className="text-3xl tracking-tight opacity-20">{apps.length}</span>
        </h2>
      </header>

      <main className="flex flex-row gap-4 flex-wrap">
        {apps.map((app) => (
          <Link
            key={app.id}
            href={`/apps/${app.id}`}
            className="block shadow-xl max-w-[320px] p-6 bg-white rounded-lg hover:shadow-md transition-shadow border-4 border-gray-100"
          >
            <div className="flex flex-col gap-4">
              <div className="flex flex-row items-center gap-4">
                <div className="text-4xl">{app.manifest.icon}</div>
                <div className="text-2xl font-semibold">{app.manifest.name}</div>
              </div>
              <div className="text-sm">{app.manifest.description}</div>
            </div>
          </Link>
        ))}
      </main>
    </>
  )
}
```

## File: `app/(app)/apps/invoices/actions.ts`
```typescript
"use server"

import { getCurrentUser, isSubscriptionExpired } from "@/lib/auth"
import {
  getTransactionFileUploadPath,
  getUserUploadsDirectory,
  isEnoughStorageToUploadFile,
  safePathJoin,
} from "@/lib/files"
import { getAppData, setAppData } from "@/models/apps"
import { createFile } from "@/models/files"
import { createTransaction, updateTransactionFiles } from "@/models/transactions"
import { Transaction, User } from "@/prisma/client"
import { renderToBuffer } from "@react-pdf/renderer"
import { randomUUID } from "crypto"
import { mkdir, writeFile } from "fs/promises"
import { revalidatePath } from "next/cache"
import path from "path"
import { createElement } from "react"
import { InvoiceFormData } from "./components/invoice-page"
import { InvoicePDF } from "./components/invoice-pdf"
import { InvoiceTemplate } from "./default-templates"
import { InvoiceAppData } from "./page"

export async function generateInvoicePDF(data: InvoiceFormData): Promise<Uint8Array> {
  const pdfElement = createElement(InvoicePDF, { data })
  const buffer = await renderToBuffer(pdfElement as any)
  return new Uint8Array(buffer)
}

export async function addNewTemplateAction(user: User, template: InvoiceTemplate) {
  const appData = (await getAppData(user, "invoices")) as InvoiceAppData | null
  const updatedTemplates = [...(appData?.templates || []), template]
  const appDataResult = await setAppData(user, "invoices", { ...appData, templates: updatedTemplates })
  return { success: true, data: appDataResult }
}

export async function deleteTemplateAction(user: User, templateId: string) {
  const appData = (await getAppData(user, "invoices")) as InvoiceAppData | null
  if (!appData) return { success: false, error: "No app data found" }

  const updatedTemplates = appData.templates.filter((t) => t.id !== templateId)
  const appDataResult = await setAppData(user, "invoices", { ...appData, templates: updatedTemplates })
  return { success: true, data: appDataResult }
}

export async function saveInvoiceAsTransactionAction(
  formData: InvoiceFormData
): Promise<{ success: boolean; error?: string; data?: Transaction }> {
  try {
    const user = await getCurrentUser()

    // Generate PDF
    const pdfBuffer = await generateInvoicePDF(formData)

    // Calculate total amount from items
    const subtotal = formData.items.reduce((sum, item) => sum + item.subtotal, 0)
    const taxes = formData.additionalTaxes.reduce((sum, tax) => sum + tax.amount, 0)
    const fees = formData.additionalFees.reduce((sum, fee) => sum + fee.amount, 0)
    const totalAmount = (formData.taxIncluded ? subtotal : subtotal + taxes) + fees

    // Create transaction
    const transaction = await createTransaction(user.id, {
      name: `Invoice #${formData.invoiceNumber || "unknown"}`,
      merchant: `${formData.billTo.split("\n")[0]}`,
      total: totalAmount * 100,
      currencyCode: formData.currency,
      issuedAt: new Date(formData.date),
      categoryCode: null,
      projectCode: null,
      type: "income",
      status: "pending",
    })

    // Check storage limits
    if (!isEnoughStorageToUploadFile(user, pdfBuffer.length)) {
      return {
        success: false,
        error: "Insufficient storage to save invoice PDF",
      }
    }

    if (isSubscriptionExpired(user)) {
      return {
        success: false,
        error: "Your subscription has expired, please upgrade your account or buy new subscription plan",
      }
    }

    // Save PDF file
    const fileUuid = randomUUID()
    const fileName = `invoice-${formData.invoiceNumber}.pdf`
    const relativeFilePath = getTransactionFileUploadPath(fileUuid, fileName, transaction)
    const userUploadsDirectory = getUserUploadsDirectory(user)
    const fullFilePath = safePathJoin(userUploadsDirectory, relativeFilePath)

    await mkdir(path.dirname(fullFilePath), { recursive: true })
    await writeFile(fullFilePath, pdfBuffer)

    // Create file record in database
    const fileRecord = await createFile(user.id, {
      id: fileUuid,
      filename: fileName,
      path: relativeFilePath,
      mimetype: "application/pdf",
      isReviewed: true,
      metadata: {
        size: pdfBuffer.length,
        lastModified: Date.now(),
      },
    })

    // Update transaction with the file ID
    await updateTransactionFiles(transaction.id, user.id, [fileRecord.id])

    revalidatePath("/transactions")

    return { success: true, data: transaction }
  } catch (error) {
    console.error("Failed to save invoice as transaction:", error)
    return {
      success: false,
      error: `Failed to save invoice as transaction: ${error}`,
    }
  }
}
```

## File: `app/(app)/apps/invoices/default-templates.ts`
```typescript
import { SettingsMap } from "@/models/settings"
import { User } from "@/prisma/client"
import { addDays, format } from "date-fns"
import { InvoiceFormData } from "./components/invoice-page"

export interface InvoiceTemplate {
  id?: string
  name: string
  formData: InvoiceFormData
}

export default function defaultTemplates(user: User, settings: SettingsMap): InvoiceTemplate[] {
  const defaultTemplate: InvoiceFormData = {
    title: "INVOICE",
    businessLogo: user.businessLogo,
    invoiceNumber: "",
    date: format(new Date(), "yyyy-MM-dd"),
    dueDate: format(addDays(new Date(), 30), "yyyy-MM-dd"),
    currency: settings.default_currency || "EUR",
    companyDetails: `${user.businessName}\n${user.businessAddress || ""}`,
    companyDetailsLabel: "Bill From",
    billTo: "",
    billToLabel: "Bill To",
    items: [{ name: "", subtitle: "", showSubtitle: false, quantity: 1, unitPrice: 0, subtotal: 0 }],
    taxIncluded: true,
    additionalTaxes: [{ name: "VAT", rate: 0, amount: 0 }],
    additionalFees: [],
    notes: "",
    bankDetails: user.businessBankDetails || "",
    issueDateLabel: "Issue Date",
    dueDateLabel: "Due Date",
    itemLabel: "Item",
    quantityLabel: "Quantity",
    unitPriceLabel: "Unit Price",
    subtotalLabel: "Subtotal",
    summarySubtotalLabel: "Subtotal:",
    summaryTotalLabel: "Total:",
  }

  const germanTemplate: InvoiceFormData = {
    title: "RECHNUNG",
    businessLogo: user.businessLogo,
    invoiceNumber: "",
    date: format(new Date(), "yyyy-MM-dd"),
    dueDate: format(addDays(new Date(), 30), "yyyy-MM-dd"),
    currency: "EUR",
    companyDetails: `${user.businessName}\n${user.businessAddress || ""}`,
    companyDetailsLabel: "Rechnungssteller",
    billTo: "",
    billToLabel: "Rechnungsempfänger",
    items: [{ name: "", subtitle: "", showSubtitle: false, quantity: 1, unitPrice: 0, subtotal: 0 }],
    taxIncluded: true,
    additionalTaxes: [{ name: "MwSt", rate: 19, amount: 0 }],
    additionalFees: [],
    notes: "",
    bankDetails: user.businessBankDetails || "",
    issueDateLabel: "Rechnungsdatum",
    dueDateLabel: "Fälligkeitsdatum",
    itemLabel: "Position",
    quantityLabel: "Menge",
    unitPriceLabel: "Einzelpreis",
    subtotalLabel: "Zwischensumme",
    summarySubtotalLabel: "Zwischensumme:",
    summaryTotalLabel: "Gesamtbetrag:",
  }

  return [
    { name: "Default", formData: defaultTemplate },
    { name: "DE", formData: germanTemplate },
  ]
}
```

## File: `app/(app)/apps/invoices/manifest.ts`
```typescript
import { AppManifest } from "../common"

export const manifest: AppManifest = {
  name: "Invoice Generator",
  description: "Generate custom invoices and send them to your customers",
  icon: "🧾",
}
```

## File: `app/(app)/apps/invoices/page.tsx`
```tsx
import { getCurrentUser } from "@/lib/auth"
import { getAppData } from "@/models/apps"
import { getCurrencies } from "@/models/currencies"
import { getSettings } from "@/models/settings"
import { InvoiceGenerator } from "./components/invoice-generator"
import { InvoiceTemplate } from "./default-templates"
import { manifest } from "./manifest"

export type InvoiceAppData = {
  templates: InvoiceTemplate[]
}

export default async function InvoicesApp() {
  const user = await getCurrentUser()
  const settings = await getSettings(user.id)
  const currencies = await getCurrencies(user.id)
  const appData = (await getAppData(user, "invoices")) as InvoiceAppData | null

  return (
    <div>
      <header className="flex flex-wrap items-center justify-between gap-2 mb-8">
        <h2 className="flex flex-row gap-3 md:gap-5">
          <span className="text-3xl font-bold tracking-tight">
            {manifest.icon} {manifest.name}
          </span>
        </h2>
      </header>
      <InvoiceGenerator user={user} settings={settings} currencies={currencies} appData={appData} />
    </div>
  )
}
```

## File: `app/(app)/apps/invoices/components/invoice-generator.tsx`
```tsx
"use client"

import { Button } from "@/components/ui/button"
import { Dialog, DialogContent, DialogFooter, DialogHeader, DialogTitle } from "@/components/ui/dialog"
import { fetchAsBase64 } from "@/lib/utils"
import { SettingsMap } from "@/models/settings"
import { Currency, User } from "@/prisma/client"
import { FileDown, Loader2, Save, TextSelect, X } from "lucide-react"
import { useRouter } from "next/navigation"
import { startTransition, useMemo, useReducer, useState } from "react"
import {
  addNewTemplateAction,
  deleteTemplateAction,
  generateInvoicePDF,
  saveInvoiceAsTransactionAction,
} from "../actions"
import defaultTemplates, { InvoiceTemplate } from "../default-templates"
import { InvoiceAppData } from "../page"
import { InvoiceFormData, InvoicePage } from "./invoice-page"

function invoiceFormReducer(state: InvoiceFormData, action: any): InvoiceFormData {
  switch (action.type) {
    case "SET_FORM":
      return action.payload
    case "UPDATE_FIELD":
      return { ...state, [action.field]: action.value }
    case "ADD_ITEM":
      return {
        ...state,
        items: [
          ...state.items,
          { name: "", subtitle: "", showSubtitle: false, quantity: 1, unitPrice: 0, subtotal: 0 },
        ],
      }
    case "UPDATE_ITEM": {
      const items = [...state.items]
      items[action.index] = { ...items[action.index], [action.field]: action.value }
      if (action.field === "quantity" || action.field === "unitPrice") {
        items[action.index].subtotal = Number(items[action.index].quantity) * Number(items[action.index].unitPrice)
      }
      return { ...state, items }
    }
    case "REMOVE_ITEM":
      return { ...state, items: state.items.filter((_, i) => i !== action.index) }
    case "ADD_TAX":
      return { ...state, additionalTaxes: [...state.additionalTaxes, { name: "", rate: 0, amount: 0 }] }
    case "UPDATE_TAX": {
      const taxes = [...state.additionalTaxes]
      taxes[action.index] = { ...taxes[action.index], [action.field]: action.value }
      if (action.field === "rate") {
        const subtotal = state.items.reduce((sum, item) => sum + item.subtotal, 0)
        taxes[action.index].amount = (subtotal * Number(action.value)) / 100
      }
      return { ...state, additionalTaxes: taxes }
    }
    case "REMOVE_TAX":
      return { ...state, additionalTaxes: state.additionalTaxes.filter((_, i) => i !== action.index) }
    case "ADD_FEE":
      return { ...state, additionalFees: [...state.additionalFees, { name: "", amount: 0 }] }
    case "UPDATE_FEE": {
      const fees = [...state.additionalFees]
      fees[action.index] = { ...fees[action.index], [action.field]: action.value }
      return { ...state, additionalFees: fees }
    }
    case "REMOVE_FEE":
      return { ...state, additionalFees: state.additionalFees.filter((_, i) => i !== action.index) }
    default:
      return state
  }
}

export function InvoiceGenerator({
  user,
  settings,
  currencies,
  appData,
}: {
  user: User
  settings: SettingsMap
  currencies: Currency[]
  appData: InvoiceAppData | null
}) {
  const templates: InvoiceTemplate[] = useMemo(
    () => [...defaultTemplates(user, settings), ...(appData?.templates || [])],
    [appData]
  )

  const [selectedTemplate, setSelectedTemplate] = useState<string>(templates[0].name)
  const [isTemplateDialogOpen, setIsTemplateDialogOpen] = useState(false)
  const [newTemplateName, setNewTemplateName] = useState("")
  const [formData, dispatch] = useReducer(invoiceFormReducer, templates[0].formData)
  const [isPdfLoading, setIsPdfLoading] = useState(false)
  const [isSavingTransaction, setIsSavingTransaction] = useState(false)

  const router = useRouter()

  // Function to handle template selection
  const handleTemplateSelect = (templateName: string) => {
    const template = templates.find((t) => t.name === templateName)
    if (template) {
      setSelectedTemplate(templateName)
      dispatch({ type: "SET_FORM", payload: template.formData })
    }
  }

  const handleGeneratePDF = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsPdfLoading(true)

    try {
      if (formData.businessLogo) {
        formData.businessLogo = await fetchAsBase64(formData.businessLogo)
      }

      const pdfBuffer = await generateInvoicePDF(formData)

      // Create a blob from the buffer
      const blob = new Blob([pdfBuffer], { type: "application/pdf" })

      // Create a URL for the blob
      const url = URL.createObjectURL(blob)

      // Create a temporary link element
      const link = document.createElement("a")
      link.href = url
      link.download = `invoice-${formData.invoiceNumber}.pdf`

      // Append the link to the document, click it, and remove it
      document.body.appendChild(link)
      link.click()
      document.body.removeChild(link)

      // Clean up the URL
      URL.revokeObjectURL(url)
    } catch (error) {
      console.error("Error generating PDF:", error)
      alert("Failed to generate PDF. Please try again.")
    } finally {
      setIsPdfLoading(false)
    }
  }

  const handleSaveTemplate = async () => {
    if (!newTemplateName.trim()) {
      alert("Please enter a template name")
      return
    }

    if (templates.some((t) => t.name === newTemplateName)) {
      alert("A template with this name already exists")
      return
    }

    try {
      const result = await addNewTemplateAction(user, {
        id: `tmpl_${Math.random().toString(36).substring(2, 15)}`,
        name: newTemplateName,
        formData: formData,
      })

      if (result.success) {
        setIsTemplateDialogOpen(false)
        setNewTemplateName("")
        router.refresh()
      } else {
        alert("Failed to save template. Please try again.")
      }
    } catch (error) {
      console.error("Error saving template:", error)
      alert("Failed to save template. Please try again.")
    }
  }

  const handleDeleteTemplate = async (templateId: string | undefined, e: React.MouseEvent) => {
    e.stopPropagation()
    if (!templateId) return // Don't allow deleting default templates

    try {
      const result = await deleteTemplateAction(user, templateId)
      if (result.success) {
        router.refresh()
      }
    } catch (error) {
      console.error("Error deleting template:", error)
      alert("Failed to delete template. Please try again.")
    }
  }

  // Accept optional event, prevent default only if present
  const handleSaveAsTransaction = async (e?: React.FormEvent) => {
    if (e) e.preventDefault()
    setIsSavingTransaction(true)

    try {
      if (formData.businessLogo) {
        formData.businessLogo = await fetchAsBase64(formData.businessLogo)
      }

      const result = await saveInvoiceAsTransactionAction(formData)
      if (result.success && result.data?.id) {
        console.log("SUCCESS! REDIRECTING TO TRANSACTION", result.data?.id)
        startTransition(() => {
          router.push(`/transactions/${result.data?.id}`)
        })
      } else {
        alert(result.error || "Failed to save as transaction")
      }
    } catch (error) {
      console.error("Error saving as transaction:", error)
      alert("Failed to save as transaction. Please try again.")
    } finally {
      setIsSavingTransaction(false)
    }
  }

  return (
    <div className="flex flex-col gap-6">
      {/* Templates Section */}
      <div className="py-4 flex overflow-x-auto gap-2">
        {templates.map((template) => (
          <div key={template.name} className="relative group">
            <Button
              variant={selectedTemplate === template.name ? "default" : "outline"}
              className={`
                  whitespace-nowrap p-4 
                  ${selectedTemplate === template.name ? "bg-black hover:bg-gray-900" : "border-gray-300 text-gray-700 hover:bg-gray-100"}
                `}
              onClick={() => handleTemplateSelect(template.name)}
            >
              {template.name}
            </Button>
            {template.id && (
              <Button
                variant="destructive"
                size="icon"
                className="absolute -top-2 -right-2 h-5 w-5 rounded-full opacity-0 group-hover:opacity-100 transition-opacity"
                onClick={(e) => handleDeleteTemplate(template.id, e)}
              >
                <X className="h-3 w-3" />
              </Button>
            )}
          </div>
        ))}
      </div>

      <div className="flex flex-row flex-wrap justify-start items-start gap-4">
        <InvoicePage invoiceData={formData} dispatch={dispatch} currencies={currencies} />

        {/* Generate PDF Button */}
        <div className="flex flex-col gap-4">
          <Button onClick={handleGeneratePDF} disabled={isPdfLoading}>
            {isPdfLoading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Generating...
              </>
            ) : (
              <>
                <FileDown className="mr-2" />
                Download PDF
              </>
            )}
          </Button>
          <Button variant="secondary" onClick={() => setIsTemplateDialogOpen(true)}>
            <TextSelect />
            Make a Template
          </Button>
          <Button variant="secondary" onClick={handleSaveAsTransaction} disabled={isSavingTransaction}>
            {isSavingTransaction ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Saving...
              </>
            ) : (
              <>
                <Save className="mr-2" />
                Save as Transaction
              </>
            )}
          </Button>
        </div>
      </div>

      {/* New Template Dialog */}
      <Dialog open={isTemplateDialogOpen} onOpenChange={setIsTemplateDialogOpen}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Save as Template</DialogTitle>
          </DialogHeader>
          <div className="py-4">
            <input
              type="text"
              value={newTemplateName}
              onChange={(e) => setNewTemplateName(e.target.value)}
              placeholder="Enter template name"
              className="w-full px-3 py-2 border rounded-md"
            />
          </div>
          <DialogFooter>
            <Button variant="outline" onClick={() => setIsTemplateDialogOpen(false)}>
              Cancel
            </Button>
            <Button onClick={handleSaveTemplate}>Save Template</Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </div>
  )
}
```

## File: `app/(app)/apps/invoices/components/invoice-page.tsx`
```tsx
import { FormSelectCurrency } from "@/components/forms/select-currency"
import { FormAvatar, FormInput, FormTextarea } from "@/components/forms/simple"
import { Button } from "@/components/ui/button"
import { formatCurrency } from "@/lib/utils"
import { Currency } from "@/prisma/client"
import { X } from "lucide-react"
import { InputHTMLAttributes, memo, useCallback, useMemo } from "react"

export interface InvoiceItem {
  name: string
  subtitle: string
  showSubtitle: boolean
  quantity: number
  unitPrice: number
  subtotal: number
}

export interface AdditionalTax {
  name: string
  rate: number
  amount: number
}

export interface AdditionalFee {
  name: string
  amount: number
}

export interface InvoiceFormData {
  title: string
  businessLogo: string | null
  invoiceNumber: string
  date: string
  dueDate: string
  currency: string
  companyDetails: string
  companyDetailsLabel: string
  billTo: string
  billToLabel: string
  items: InvoiceItem[]
  taxIncluded: boolean
  additionalTaxes: AdditionalTax[]
  additionalFees: AdditionalFee[]
  notes: string
  bankDetails: string
  issueDateLabel: string
  dueDateLabel: string
  itemLabel: string
  quantityLabel: string
  unitPriceLabel: string
  subtotalLabel: string
  summarySubtotalLabel: string
  summaryTotalLabel: string
}

interface InvoicePageProps {
  invoiceData: InvoiceFormData
  dispatch: React.Dispatch<any>
  currencies: Currency[]
}

// Memoized row for invoice items
const ItemRow = memo(function ItemRow({
  item,
  index,
  onChange,
  onRemove,
  currency,
}: {
  item: InvoiceItem
  index: number
  onChange: (index: number, field: keyof InvoiceItem, value: string | number | boolean) => void
  onRemove: (index: number) => void
  currency: string
}) {
  return (
    <div className="flex flex-col sm:flex-row items-start py-3 px-4 bg-white hover:bg-gray-50">
      {/* Mobile view label (visible only on small screens) */}
      <div className="flex justify-between sm:hidden mb-2">
        <span className="text-xs font-medium text-gray-500 uppercase">Item</span>
        <Button variant="destructive" className="rounded-full p-1 h-5 w-5" onClick={() => onRemove(index)}>
          <X />
        </Button>
      </div>

      {/* Item name and subtitle */}
      <div className="flex-1 sm:px-0">
        <div className="flex flex-col">
          <FormInput
            type="text"
            value={item.name}
            onChange={(e) => onChange(index, "name", e.target.value)}
            className="w-full min-w-0 font-semibold"
            placeholder="Item name"
            required
          />
          <div>
            {!item.showSubtitle ? (
              <button
                type="button"
                className="text-xs text-gray-400 hover:text-gray-800 mt-1 ml-1"
                onClick={() => onChange(index, "showSubtitle", true)}
              >
                + Add Description
              </button>
            ) : (
              <FormInput
                type="text"
                value={item.subtitle}
                onChange={(e) => onChange(index, "subtitle", e.target.value)}
                className="w-full mt-1 text-xs text-muted-foreground"
                placeholder="Detailed description (optional)"
              />
            )}
          </div>
        </div>
      </div>

      {/* Mobile labels for small screens */}
      <div className="grid grid-cols-3 gap-2 mt-2 sm:hidden">
        <div className="text-xs font-medium text-gray-500 uppercase">Quantity</div>
        <div className="text-xs font-medium text-gray-500 uppercase">Unit Price</div>
        <div className="text-xs font-medium text-gray-500 uppercase">Subtotal</div>
      </div>

      {/* Quantity, Unit Price, Subtotal, and Remove button */}
      <div className="grid grid-cols-3 sm:flex gap-2 mt-1 sm:mt-0">
        <div className="sm:w-20 sm:px-4">
          <FormInput
            type="number"
            min="1"
            value={item.quantity}
            onChange={(e) => onChange(index, "quantity", Number(e.target.value))}
            className="w-full text-right"
            required
          />
        </div>
        <div className="sm:w-28 sm:px-4">
          <FormInput
            type="number"
            step="0.01"
            value={item.unitPrice}
            onChange={(e) => onChange(index, "unitPrice", Number(e.target.value))}
            className="w-full text-right"
            required
          />
        </div>
        <div className="sm:w-28 sm:px-4 flex items-center justify-end">
          <span className="text-sm text-right">{formatCurrency(item.subtotal * 100, currency)}</span>
        </div>
        <div className="hidden sm:flex sm:w-10 sm:px-2 items-center justify-center">
          <Button variant="destructive" className="rounded-full p-1 h-5 w-5" onClick={() => onRemove(index)}>
            <X />
          </Button>
        </div>
      </div>
    </div>
  )
})

// Memoized row for additional taxes
const TaxRow = memo(function TaxRow({
  tax,
  index,
  onChange,
  onRemove,
  currency,
}: {
  tax: AdditionalTax
  index: number
  onChange: (index: number, field: keyof AdditionalTax, value: string | number) => void
  onRemove: (index: number) => void
  currency: string
}) {
  return (
    <div className="flex justify-between items-center">
      <div className="w-full flex flex-row gap-2 items-center">
        <Button variant="destructive" className="rounded-full p-1 h-5 w-5" onClick={() => onRemove(index)}>
          <X />
        </Button>
        <FormInput
          type="text"
          value={tax.name}
          onChange={(e) => onChange(index, "name", e.target.value)}
          placeholder="Tax name"
        />
        <FormInput
          type="number"
          max="100"
          value={tax.rate}
          onChange={(e) => onChange(index, "rate", Number(e.target.value))}
          className="w-12 text-right"
        />
        <span className="text-sm text-gray-600">%</span>
        <span className="text-sm text-nowrap">{formatCurrency(tax.amount * 100, currency)}</span>
      </div>
    </div>
  )
})

// Memoized row for additional fees
const FeeRow = memo(function FeeRow({
  fee,
  index,
  onChange,
  onRemove,
  currency,
}: {
  fee: AdditionalFee
  index: number
  onChange: (index: number, field: keyof AdditionalFee, value: string | number) => void
  onRemove: (index: number) => void
  currency: string
}) {
  return (
    <div className="w-full flex justify-between items-center">
      <div className="w-full flex flex-row gap-2 items-center justify-between">
        <Button variant="destructive" className="rounded-full p-1 h-5 w-5" onClick={() => onRemove(index)}>
          <X />
        </Button>
        <FormInput
          type="text"
          value={fee.name}
          onChange={(e) => onChange(index, "name", e.target.value)}
          placeholder="Fee or discount name"
        />
        <FormInput
          type="number"
          step="0.01"
          value={fee.amount}
          onChange={(e) => onChange(index, "amount", Number(e.target.value))}
          className="w-16 text-right"
        />
        <span className="text-sm text-nowrap">{formatCurrency(fee.amount * 100, currency)}</span>
      </div>
    </div>
  )
})

export function InvoicePage({ invoiceData, dispatch, currencies }: InvoicePageProps) {
  const addItem = useCallback(() => dispatch({ type: "ADD_ITEM" }), [dispatch])
  const removeItem = useCallback((index: number) => dispatch({ type: "REMOVE_ITEM", index }), [dispatch])
  const updateItem = useCallback(
    (index: number, field: keyof InvoiceItem, value: string | number | boolean) =>
      dispatch({ type: "UPDATE_ITEM", index, field, value }),
    [dispatch]
  )

  const addAdditionalTax = useCallback(() => dispatch({ type: "ADD_TAX" }), [dispatch])
  const removeAdditionalTax = useCallback((index: number) => dispatch({ type: "REMOVE_TAX", index }), [dispatch])
  const updateAdditionalTax = useCallback(
    (index: number, field: keyof AdditionalTax, value: string | number) =>
      dispatch({ type: "UPDATE_TAX", index, field, value }),
    [dispatch]
  )

  const addAdditionalFee = useCallback(() => dispatch({ type: "ADD_FEE" }), [dispatch])
  const removeAdditionalFee = useCallback((index: number) => dispatch({ type: "REMOVE_FEE", index }), [dispatch])
  const updateAdditionalFee = useCallback(
    (index: number, field: keyof AdditionalFee, value: string | number) =>
      dispatch({ type: "UPDATE_FEE", index, field, value }),
    [dispatch]
  )

  const subtotal = useMemo(() => invoiceData.items.reduce((sum, item) => sum + item.subtotal, 0), [invoiceData.items])
  const taxes = useMemo(
    () => invoiceData.additionalTaxes.reduce((sum, tax) => sum + tax.amount, 0),
    [invoiceData.additionalTaxes]
  )
  const fees = useMemo(
    () => invoiceData.additionalFees.reduce((sum, fee) => sum + fee.amount, 0),
    [invoiceData.additionalFees]
  )
  const total = useMemo(
    () => (invoiceData.taxIncluded ? subtotal : subtotal + taxes) + fees,
    [invoiceData.taxIncluded, subtotal, taxes, fees]
  )

  return (
    <div className="relative w-full max-w-[794px] sm:w-[794px] min-h-[297mm] bg-white shadow-lg p-2 sm:p-8 mb-8">
      {/* Gradient Background */}
      <div className="absolute top-0 left-0 right-0 h-[25%] bg-gradient-to-b from-indigo-100 to-indigo-0 opacity-70" />

      {/* Invoice Header */}
      <div className="flex flex-col sm:flex-row gap-4 sm:gap-8 justify-between items-start mb-8 relative">
        <div className="w-full flex flex-col space-y-2">
          <ShadyFormInput
            type="text"
            value={invoiceData.title}
            onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "title", value: e.target.value })}
            className="text-2xl sm:text-4xl font-extrabold"
            placeholder="INVOICE"
            required
          />
          <FormInput
            placeholder="Invoice ID or subtitle"
            value={invoiceData.invoiceNumber}
            onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "invoiceNumber", value: e.target.value })}
            className="w-full sm:w-[200px] font-medium"
          />
        </div>

        <div className="flex flex-row items-center justify-end mt-4 sm:mt-0">
          <FormAvatar
            name="businessLogo"
            className="w-[60px] h-[60px] sm:w-[100px] sm:h-[100px]"
            defaultValue={invoiceData.businessLogo || ""}
            onChange={(e) => {
              const file = e.target.files?.[0]
              if (file) {
                const objectUrl = URL.createObjectURL(file)
                dispatch({ type: "UPDATE_FIELD", field: "businessLogo", value: objectUrl })
              } else {
                dispatch({ type: "UPDATE_FIELD", field: "businessLogo", value: null })
              }
            }}
          />
        </div>
      </div>

      {/* Company and Bill To */}
      <div className="relative grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-8 mb-8">
        <div className="flex flex-col gap-1">
          <ShadyFormInput
            type="text"
            value={invoiceData.companyDetailsLabel}
            onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "companyDetailsLabel", value: e.target.value })}
            className="text-xs sm:text-sm font-medium"
          />
          <FormTextarea
            value={invoiceData.companyDetails}
            onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "companyDetails", value: e.target.value })}
            rows={4}
            placeholder="Your Company Name, Address, City, State, ZIP, Country, Tax ID"
            required
          />
        </div>
        <div className="flex flex-col gap-1">
          <ShadyFormInput
            type="text"
            value={invoiceData.billToLabel}
            onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "billToLabel", value: e.target.value })}
            className="text-xs sm:text-sm font-medium"
          />
          <FormTextarea
            value={invoiceData.billTo}
            onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "billTo", value: e.target.value })}
            rows={4}
            placeholder="Client Name, Address, City, State, ZIP, Country, Tax ID"
            required
          />
        </div>
      </div>

      <div className="relative flex flex-col sm:flex-row items-start sm:items-end justify-between mb-8 gap-4">
        <div className="flex flex-row items-center gap-4 w-full sm:w-auto">
          <div className="flex flex-col gap-1 w-full">
            <ShadyFormInput
              type="text"
              value={invoiceData.issueDateLabel}
              onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "issueDateLabel", value: e.target.value })}
              className="text-xs sm:text-sm font-medium"
            />
            <FormInput
              type="date"
              value={invoiceData.date}
              onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "date", value: e.target.value })}
              className="w-full border-b border-gray-300 py-1"
              required
            />
          </div>

          <div className="flex flex-col gap-1 w-full">
            <ShadyFormInput
              type="text"
              value={invoiceData.dueDateLabel}
              onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "dueDateLabel", value: e.target.value })}
              className="text-xs sm:text-sm font-medium"
            />
            <FormInput
              type="date"
              value={invoiceData.dueDate}
              onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "dueDate", value: e.target.value })}
              required
            />
          </div>
        </div>

        <div className="w-full sm:w-auto flex justify-end">
          <FormSelectCurrency
            currencies={currencies}
            value={invoiceData.currency}
            onValueChange={(value) => dispatch({ type: "UPDATE_FIELD", field: "currency", value })}
          />
        </div>
      </div>

      {/* Items Section - Refactored to use only flex divs */}
      <div className="mb-8">
        <div className="border rounded-lg overflow-hidden">
          {/* Header row for column titles */}
          <div className="hidden sm:flex bg-gray-50 text-xs font-medium text-gray-500 uppercase tracking-wider border-b">
            <div className="flex-1 px-4 py-3">
              <ShadyFormInput
                type="text"
                value={invoiceData.itemLabel}
                onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "itemLabel", value: e.target.value })}
                className="text-xs font-medium text-gray-500 uppercase tracking-wider"
              />
            </div>
            <div className="w-20 px-4 py-3 text-right">
              <ShadyFormInput
                type="text"
                value={invoiceData.quantityLabel}
                onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "quantityLabel", value: e.target.value })}
                className="text-xs font-medium text-gray-500 uppercase tracking-wider text-right w-full"
              />
            </div>
            <div className="w-28 px-4 py-3 text-right">
              <ShadyFormInput
                type="text"
                value={invoiceData.unitPriceLabel}
                onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "unitPriceLabel", value: e.target.value })}
                className="text-xs font-medium text-gray-500 uppercase tracking-wider text-right w-full"
              />
            </div>
            <div className="w-28 px-4 py-3 text-right">
              <ShadyFormInput
                type="text"
                value={invoiceData.subtotalLabel}
                onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "subtotalLabel", value: e.target.value })}
                className="text-xs font-medium text-gray-500 uppercase tracking-wider text-right w-full"
              />
            </div>
            <div className="w-10 px-2 py-3"></div>
          </div>

          {/* Invoice items */}
          <div className="flex flex-col divide-y divide-gray-200">
            {invoiceData.items.map((item, index) => (
              <ItemRow
                key={index}
                item={item}
                index={index}
                onChange={updateItem}
                onRemove={removeItem}
                currency={invoiceData.currency}
              />
            ))}
          </div>

          <Button onClick={addItem} className="m-2 sm:m-3 w-full sm:w-auto">
            + Add Item
          </Button>
        </div>
      </div>

      {/* Notes */}
      <div className="mb-8">
        <FormTextarea
          value={invoiceData.notes}
          onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "notes", value: e.target.value })}
          className="w-full border border-gray-300 rounded p-2 text-xs sm:text-sm"
          rows={3}
          placeholder="Additional notes or terms"
        />
      </div>

      {/* Summary */}
      <div className="flex justify-end">
        <div className="w-full sm:w-72 space-y-2">
          <div className="flex justify-between">
            <ShadyFormInput
              type="text"
              value={invoiceData.summarySubtotalLabel}
              onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "summarySubtotalLabel", value: e.target.value })}
              className="text-xs sm:text-sm font-medium text-gray-600"
            />
            <span className="text-xs sm:text-sm">{formatCurrency(subtotal * 100, invoiceData.currency)}</span>
          </div>

          <div className="flex flex-col gap-2 items-start">
            {/* Additional Taxes */}
            {invoiceData.additionalTaxes.map((tax, index) => (
              <TaxRow
                key={index}
                tax={tax}
                index={index}
                onChange={updateAdditionalTax}
                onRemove={removeAdditionalTax}
                currency={invoiceData.currency}
              />
            ))}

            <div className="w-full flex justify-end">
              <Button onClick={addAdditionalTax} className="w-full sm:w-auto">
                + Add Tax
              </Button>
            </div>

            {invoiceData.additionalFees.map((fee, index) => (
              <FeeRow
                key={index}
                fee={fee}
                index={index}
                onChange={updateAdditionalFee}
                onRemove={removeAdditionalFee}
                currency={invoiceData.currency}
              />
            ))}

            <div className="w-full flex justify-end">
              <Button onClick={addAdditionalFee} className="w-full sm:w-auto">
                + Add Fee or Discount
              </Button>
            </div>
          </div>

          <label className="flex items-center space-x-1">
            <input
              type="checkbox"
              checked={invoiceData.taxIncluded}
              onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "taxIncluded", value: e.target.checked })}
              className="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
            />
            <span className="text-gray-600 text-xs sm:text-sm">Taxes are included in price</span>
          </label>
          <div className="flex justify-between border-t pt-2">
            <ShadyFormInput
              type="text"
              value={invoiceData.summaryTotalLabel}
              onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "summaryTotalLabel", value: e.target.value })}
              className="text-sm sm:text-md font-bold"
            />
            <span className="text-sm sm:text-md font-bold text-nowrap">
              {formatCurrency(total * 100, invoiceData.currency)}
            </span>
          </div>
        </div>
      </div>

      {/* Bank Details Footer */}
      <div className="mt-8 pt-8 border-t">
        <textarea
          value={invoiceData.bankDetails}
          onChange={(e) => dispatch({ type: "UPDATE_FIELD", field: "bankDetails", value: e.target.value })}
          className="text-center text-xs sm:text-sm text-muted-foreground w-full mx-auto border border-gray-300 rounded p-2"
          rows={3}
          placeholder="Bank and Payment Details: Account number, Bank name, IBAN, SWIFT/BIC, Your Email (optional)"
          required
        />
      </div>
    </div>
  )
}

function ShadyFormInput({ className = "", ...props }: { className?: string } & InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      className={`bg-transparent border border-transparent outline-none p-0 w-full hover:border-dashed hover:border-gray-200 hover:bg-gray-50 focus:bg-gray-50 hover:rounded-sm ${className}`}
      {...props}
    />
  )
}
```

## File: `app/(app)/apps/invoices/components/invoice-pdf.tsx`
```tsx
import { formatCurrency } from "@/lib/utils"
import { Document, Font, Image, Page, StyleSheet, Text, View } from "@react-pdf/renderer"
import { formatDate } from "date-fns"
import { ReactElement } from "react"
import { AdditionalFee, AdditionalTax, InvoiceFormData, InvoiceItem } from "./invoice-page"

Font.register({
  family: "Inter",
  fonts: [
    {
      src: "public/fonts/Inter/Inter-Regular.otf",
      fontWeight: 400,
      fontStyle: "normal",
    },
    {
      src: "public/fonts/Inter/Inter-Medium.otf",
      fontWeight: 500,
      fontStyle: "normal",
    },
    {
      src: "public/fonts/Inter/Inter-SemiBold.otf",
      fontWeight: 600,
      fontStyle: "normal",
    },
    {
      src: "public/fonts/Inter/Inter-Bold.otf",
      fontWeight: 700,
      fontStyle: "normal",
    },
    {
      src: "public/fonts/Inter/Inter-ExtraBold.otf",
      fontWeight: 800,
      fontStyle: "normal",
    },
    {
      src: "public/fonts/Inter/Inter-Black.otf",
      fontWeight: 900,
      fontStyle: "normal",
    },
    {
      src: "public/fonts/Inter-Italic.otf",
      fontWeight: 400,
      fontStyle: "italic",
    },
    {
      src: "public/fonts/Inter/Inter-MediumItalic.otf",
      fontWeight: 500,
      fontStyle: "italic",
    },
    {
      src: "public/fonts/Inter/Inter-SemiBoldItalic.otf",
      fontWeight: 600,
      fontStyle: "italic",
    },
    {
      src: "public/fonts/Inter/Inter-BoldItalic.otf",
      fontWeight: 700,
      fontStyle: "italic",
    },
    {
      src: "public/fonts/Inter/Inter-ExtraBoldItalic.otf",
      fontWeight: 800,
      fontStyle: "italic",
    },
    {
      src: "public/fonts/Inter/Inter-BlackItalic.otf",
      fontWeight: 900,
      fontStyle: "italic",
    },
  ],
})

Font.registerEmojiSource({
  format: "png",
  url: "https://cdnjs.cloudflare.com/ajax/libs/twemoji/14.0.2/72x72/",
})

const styles = StyleSheet.create({
  page: {
    fontFamily: "Inter",
    padding: 30,
    backgroundColor: "#ffffff",
  },
  header: {
    marginBottom: 30,
    position: "relative",
  },
  gradientBackground: {
    position: "absolute",
    top: 0,
    left: 0,
    right: 0,
    height: "120px",
    backgroundColor: "#eef2ff",
    opacity: 0.8,
  },
  headerContent: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "flex-start",
    marginBottom: 30,
  },
  headerLeft: {
    flex: 1,
  },
  headerRight: {
    width: 110,
    height: 60,
  },
  title: {
    fontSize: 28,
    marginBottom: 10,
    fontWeight: "extrabold",
    color: "#000000",
  },
  subtitle: {
    fontSize: 13,
    color: "#666666",
  },
  logo: {
    width: "100%",
    height: "100%",
    objectFit: "contain",
  },
  companyDetails: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginBottom: 30,
  },
  companySection: {
    flex: 1,
    marginRight: 30,
  },
  sectionLabel: {
    fontSize: 12,
    fontWeight: "bold",
    marginBottom: 8,
    color: "#000000",
  },
  sectionContent: {
    fontSize: 12,
    lineHeight: 1.3,
    color: "#000000",
  },
  datesAndCurrency: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "flex-end",
    marginBottom: 30,
  },
  dateGroup: {
    flexDirection: "row",
    gap: 20,
  },
  dateItem: {
    marginRight: 20,
  },
  dateLabel: {
    fontSize: 12,
    fontWeight: "bold",
    marginBottom: 8,
    color: "#000000",
  },
  dateValue: {
    fontSize: 12,
    color: "#000000",
  },
  itemsTable: {
    marginBottom: 30,
  },
  tableHeader: {
    flexDirection: "row",
    borderBottomWidth: 1,
    borderBottomColor: "#E5E7EB",
    paddingVertical: 8,
    backgroundColor: "#F9FAFB",
    textTransform: "uppercase",
  },
  tableRow: {
    flexDirection: "row",
    borderBottomWidth: 1,
    borderBottomColor: "#E5E7EB",
    paddingVertical: 8,
  },
  colDescription: {
    flex: 2,
    paddingHorizontal: 10,
  },
  colQuantity: {
    flex: 1,
    paddingHorizontal: 10,
    textAlign: "right",
  },
  colPrice: {
    flex: 1,
    paddingHorizontal: 10,
    textAlign: "right",
  },
  colSubtotal: {
    flex: 1,
    paddingHorizontal: 10,
    textAlign: "right",
  },
  colHeader: {
    fontSize: 10,
    fontWeight: "bold",
    color: "#6B7280",
  },
  colValue: {
    fontSize: 12,
    color: "#000000",
  },
  colName: {
    fontWeight: "semibold",
  },
  itemSubtitle: {
    fontSize: 10,
    color: "#6B7280",
    marginTop: 2,
  },
  notes: {
    marginBottom: 30,
    fontSize: 12,
  },
  notesLabel: {
    fontWeight: "bold",
    marginBottom: 5,
    color: "#000000",
  },
  summary: {
    width: "50%",
    alignSelf: "flex-end",
  },
  summaryRow: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginBottom: 5,
  },
  summaryLabel: {
    fontSize: 12,
    color: "#4B5563",
  },
  summaryValue: {
    fontSize: 12,
    color: "#000000",
  },
  taxRow: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginBottom: 5,
  },
  totalRow: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginTop: 10,
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: "#000000",
  },
  totalLabel: {
    fontSize: 14,
    fontWeight: "bold",
    color: "#000000",
  },
  totalValue: {
    fontSize: 14,
    fontWeight: "bold",
    color: "#000000",
  },
  bankDetails: {
    marginTop: 30,
    paddingTop: 20,
    borderTopWidth: 1,
    borderTopColor: "#E5E7EB",
    textAlign: "center",
    fontSize: 11,
    color: "#6B7280",
  },
})

export function InvoicePDF({ data }: { data: InvoiceFormData }): ReactElement {
  const calculateSubtotal = (): number => {
    return data.items.reduce((sum: number, item: InvoiceItem) => sum + item.subtotal, 0)
  }

  const calculateTaxes = (): number => {
    return data.additionalTaxes.reduce((sum: number, tax: AdditionalTax) => sum + tax.amount, 0)
  }

  const calculateTotal = (): number => {
    const subtotal = calculateSubtotal()
    const taxes = calculateTaxes()
    return data.taxIncluded ? subtotal : subtotal + taxes
  }

  return (
    <Document>
      <Page size="A4" style={styles.page}>
        <View style={styles.gradientBackground} />

        {/* Header */}
        <View style={styles.header}>
          <View style={styles.headerContent}>
            <View style={styles.headerLeft}>
              <Text style={styles.title}>{data.title}</Text>
              <Text style={styles.subtitle}>{data.invoiceNumber}</Text>
            </View>
            {data.businessLogo && (
              <View style={styles.headerRight}>
                <Image src={data.businessLogo} style={styles.logo} />
              </View>
            )}
          </View>
        </View>

        {/* Company Details and Bill To */}
        <View style={styles.companyDetails}>
          <View style={styles.companySection}>
            <Text style={styles.sectionLabel}>{data.companyDetailsLabel}</Text>
            <Text style={styles.sectionContent}>{data.companyDetails}</Text>
          </View>
          <View style={styles.companySection}>
            <Text style={styles.sectionLabel}>{data.billToLabel}</Text>
            <Text style={styles.sectionContent}>{data.billTo}</Text>
          </View>
        </View>

        {/* Dates and Currency */}
        <View style={styles.datesAndCurrency}>
          <View style={styles.dateGroup}>
            <View style={styles.dateItem}>
              <Text style={styles.dateLabel}>{data.issueDateLabel}</Text>
              <Text style={styles.dateValue}>{formatDate(data.date, "yyyy-MM-dd")}</Text>
            </View>
            <View style={styles.dateItem}>
              <Text style={styles.dateLabel}>{data.dueDateLabel}</Text>
              <Text style={styles.dateValue}>{formatDate(data.dueDate, "yyyy-MM-dd")}</Text>
            </View>
          </View>
        </View>

        {/* Items Table */}
        <View style={styles.itemsTable}>
          <View style={styles.tableHeader}>
            <Text style={[styles.colHeader, styles.colDescription]}>{data.itemLabel}</Text>
            <Text style={[styles.colHeader, styles.colQuantity]}>{data.quantityLabel}</Text>
            <Text style={[styles.colHeader, styles.colPrice]}>{data.unitPriceLabel}</Text>
            <Text style={[styles.colHeader, styles.colSubtotal]}>{data.subtotalLabel}</Text>
          </View>

          {data.items.map((item: InvoiceItem, index: number) => (
            <View key={index} style={styles.tableRow}>
              <View style={styles.colDescription}>
                <Text style={[styles.colValue, styles.colName]}>{item.name}</Text>
                {item.showSubtitle && item.subtitle && <Text style={styles.itemSubtitle}>{item.subtitle}</Text>}
              </View>
              <Text style={[styles.colValue, styles.colQuantity]}>{item.quantity}</Text>
              <Text style={[styles.colValue, styles.colPrice]}>
                {formatCurrency(item.unitPrice * 100, data.currency)}
              </Text>
              <Text style={[styles.colValue, styles.colSubtotal]}>
                {formatCurrency(item.subtotal * 100, data.currency)}
              </Text>
            </View>
          ))}
        </View>

        {/* Notes */}
        {data.notes && (
          <View style={styles.notes}>
            <Text style={styles.notesLabel}>Notes:</Text>
            <Text>{data.notes}</Text>
          </View>
        )}

        {/* Summary */}
        <View style={styles.summary}>
          <View style={styles.summaryRow}>
            <Text style={styles.summaryLabel}>{data.summarySubtotalLabel}</Text>
            <Text style={styles.summaryValue}>{formatCurrency(calculateSubtotal() * 100, data.currency)}</Text>
          </View>

          {data.additionalTaxes.map((tax: AdditionalTax, index: number) => (
            <View key={index} style={styles.taxRow}>
              <Text style={styles.summaryLabel}>
                {tax.name} ({tax.rate}%):
              </Text>
              <Text style={styles.summaryValue}>{formatCurrency(tax.amount * 100, data.currency)}</Text>
            </View>
          ))}

          {data.additionalFees.map((fee: AdditionalFee, index: number) => (
            <View key={index} style={styles.taxRow}>
              <Text style={styles.summaryLabel}>{fee.name}</Text>
              <Text style={styles.summaryValue}>{formatCurrency(fee.amount * 100, data.currency)}</Text>
            </View>
          ))}

          <View style={styles.totalRow}>
            <Text style={styles.totalLabel}>{data.summaryTotalLabel}</Text>
            <Text style={styles.totalValue}>{formatCurrency(calculateTotal() * 100, data.currency)}</Text>
          </View>
        </View>

        {/* Bank Details */}
        {data.bankDetails && (
          <View style={styles.bankDetails}>
            <Text>{data.bankDetails}</Text>
          </View>
        )}
      </Page>
    </Document>
  )
}
```

## File: `app/(app)/dashboard/page.tsx`
```tsx
import DashboardDropZoneWidget from "@/components/dashboard/drop-zone-widget"
import { StatsWidget } from "@/components/dashboard/stats-widget"
import DashboardUnsortedWidget from "@/components/dashboard/unsorted-widget"
import { WelcomeWidget } from "@/components/dashboard/welcome-widget"
import { Separator } from "@/components/ui/separator"
import { getCurrentUser } from "@/lib/auth"
import config from "@/lib/config"
import { getUnsortedFiles } from "@/models/files"
import { getSettings } from "@/models/settings"
import { TransactionFilters } from "@/models/transactions"
import { Metadata } from "next"

export const metadata: Metadata = {
  title: "Dashboard",
  description: config.app.description,
}

export default async function Dashboard({ searchParams }: { searchParams: Promise<TransactionFilters> }) {
  const filters = await searchParams
  const user = await getCurrentUser()
  const unsortedFiles = await getUnsortedFiles(user.id)
  const settings = await getSettings(user.id)

  return (
    <div className="flex flex-col gap-5 p-5 w-full max-w-7xl self-center">
      <div className="flex flex-col sm:flex-row gap-5 items-stretch h-full">
        <DashboardDropZoneWidget />

        <DashboardUnsortedWidget files={unsortedFiles} />
      </div>

      {settings.is_welcome_message_hidden !== "true" && <WelcomeWidget />}

      <Separator />

      <StatsWidget filters={filters} />
    </div>
  )
}
```

## File: `app/(app)/export/transactions/route.ts`
```typescript
import { getCurrentUser } from "@/lib/auth"
import { fileExists, fullPathForFile } from "@/lib/files"
import { EXPORT_AND_IMPORT_FIELD_MAP, ExportFields, ExportFilters } from "@/models/export_and_import"
import { getFields } from "@/models/fields"
import { getFilesByTransactionId } from "@/models/files"
import { updateProgress } from "@/models/progress"
import { getTransactions } from "@/models/transactions"
import { format } from "@fast-csv/format"
import { formatDate } from "date-fns"
import fs from "fs/promises"
import JSZip from "jszip"
import { NextResponse } from "next/server"
import path from "path"
import { Readable } from "stream"

const TRANSACTIONS_CHUNK_SIZE = 300
const FILES_CHUNK_SIZE = 50
const PROGRESS_UPDATE_INTERVAL_MS = 2000 // 2 seconds

export async function GET(request: Request) {
  const url = new URL(request.url)
  const filters = Object.fromEntries(url.searchParams.entries()) as ExportFilters
  const fields = (url.searchParams.get("fields")?.split(",") ?? []) as ExportFields
  const includeAttachments = url.searchParams.get("includeAttachments") === "true"
  const progressId = url.searchParams.get("progressId")

  const user = await getCurrentUser()
  const { transactions } = await getTransactions(user.id, filters)
  const existingFields = await getFields(user.id)

  try {
    const fieldKeys = fields.filter((field) => existingFields.some((f) => f.code === field))

    // Create a transform stream for CSV generation
    const csvStream = format({ headers: fieldKeys, writeBOM: true, writeHeaders: false })

    // Custom CSV headers
    const headers = fieldKeys.map((field) => existingFields.find((f) => f.code === field)?.name ?? "UNKNOWN")
    csvStream.write(headers)

    // Process transactions in chunks to avoid memory issues
    for (let i = 0; i < transactions.length; i += TRANSACTIONS_CHUNK_SIZE) {
      const chunk = transactions.slice(i, i + TRANSACTIONS_CHUNK_SIZE)
      console.log(
        `Processing transactions ${i + 1}-${Math.min(i + TRANSACTIONS_CHUNK_SIZE, transactions.length)} of ${transactions.length}`
      )

      for (const transaction of chunk) {
        const row: Record<string, unknown> = {}
        for (const field of existingFields) {
          let value
          if (field.isExtra) {
            value = transaction.extra?.[field.code as keyof typeof transaction.extra] ?? ""
          } else {
            value = transaction[field.code as keyof typeof transaction] ?? ""
          }

          const exportFieldSettings = EXPORT_AND_IMPORT_FIELD_MAP[field.code]
          if (exportFieldSettings && exportFieldSettings.export) {
            row[field.code] = await exportFieldSettings.export(user.id, value)
          } else {
            row[field.code] = value
          }
        }
        csvStream.write(row)
      }
    }
    csvStream.end()

    if (!includeAttachments) {
      const stream = Readable.from(csvStream)
      return new NextResponse(stream as any, {
        headers: {
          "Content-Type": "text/csv",
          "Content-Disposition": `attachment; filename="transactions.csv"`,
        },
      })
    }

    // For ZIP files, we'll use a more memory-efficient approach
    const zip = new JSZip()

    // Add CSV to zip
    const csvContent = await new Promise<string>((resolve) => {
      let content = ""
      csvStream.on("data", (chunk) => {
        content += chunk
      })
      csvStream.on("end", () => resolve(content))
    })
    zip.file("transactions.csv", csvContent)

    // Process files in chunks
    const filesFolder = zip.folder("files")
    if (!filesFolder) {
      throw new Error("Failed to create zip folder")
    }

    let totalFilesProcessed = 0
    let totalFilesToProcess = 0
    let lastProgressUpdate = Date.now()

    // First count total files to process
    for (const transaction of transactions) {
      const transactionFiles = await getFilesByTransactionId(transaction.id, user.id)
      totalFilesToProcess += transactionFiles.length
    }

    // Update progress with total files if progressId is provided
    if (progressId) {
      await updateProgress(user.id, progressId, { total: totalFilesToProcess })
    }

    console.log(`Starting to process ${totalFilesToProcess} files in total`)

    for (let i = 0; i < transactions.length; i += FILES_CHUNK_SIZE) {
      const chunk = transactions.slice(i, i + FILES_CHUNK_SIZE)
      console.log(
        `Processing files for transactions ${i + 1}-${Math.min(i + FILES_CHUNK_SIZE, transactions.length)} of ${transactions.length}`
      )

      for (const transaction of chunk) {
        const transactionFiles = await getFilesByTransactionId(transaction.id, user.id)

        const transactionFolder = filesFolder.folder(
          path.join(
            transaction.issuedAt ? formatDate(transaction.issuedAt, "yyyy/MM") : "",
            transactionFiles.length > 1 ? transaction.name || transaction.id : ""
          )
        )

        if (!transactionFolder) continue

        for (const file of transactionFiles) {
          const fullFilePath = fullPathForFile(user, file)
          if (await fileExists(fullFilePath)) {
            console.log(
              `Processing file ${++totalFilesProcessed}/${totalFilesToProcess}: ${file.filename} for transaction ${transaction.id}`
            )
            const fileData = await fs.readFile(fullFilePath)
            const fileExtension = path.extname(fullFilePath)
            transactionFolder.file(
              `${formatDate(transaction.issuedAt || new Date(), "yyyy-MM-dd")} - ${
                transaction.name || transaction.id
              }${fileExtension}`,
              fileData
            )

            // Update progress every PROGRESS_UPDATE_INTERVAL_MS milliseconds
            const now = Date.now()
            if (progressId && now - lastProgressUpdate >= PROGRESS_UPDATE_INTERVAL_MS) {
              await updateProgress(user.id, progressId, { current: totalFilesProcessed })
              lastProgressUpdate = now
            }
          } else {
            console.log(`Skipping missing file: ${file.filename} for transaction ${transaction.id}`)
          }
        }
      }
    }

    // Final progress update
    if (progressId) {
      await updateProgress(user.id, progressId, { current: totalFilesToProcess })
    }

    console.log(`Finished processing all ${totalFilesProcessed} files`)

    // Generate zip with progress tracking
    const zipContent = await zip.generateAsync({
      type: "uint8array",
      compression: "DEFLATE",
      compressionOptions: {
        level: 6,
      },
    })

    return new NextResponse(zipContent, {
      headers: {
        "Content-Type": "application/zip",
        "Content-Disposition": `attachment; filename="transactions.zip"`,
      },
    })
  } catch (error) {
    console.error("Error exporting transactions:", error)
    return new NextResponse("Internal Server Error", { status: 500 })
  }
}
```

## File: `app/(app)/files/actions.ts`
```typescript
"use server"

import { ActionState } from "@/lib/actions"
import { getCurrentUser, isSubscriptionExpired } from "@/lib/auth"
import {
  getDirectorySize,
  getUserUploadsDirectory,
  isEnoughStorageToUploadFile,
  safePathJoin,
  unsortedFilePath,
} from "@/lib/files"
import { createFile } from "@/models/files"
import { updateUser } from "@/models/users"
import { randomUUID } from "crypto"
import { mkdir, writeFile } from "fs/promises"
import { revalidatePath } from "next/cache"
import path from "path"

export async function uploadFilesAction(formData: FormData): Promise<ActionState<null>> {
  const user = await getCurrentUser()
  const files = formData.getAll("files") as File[]

  // Make sure upload dir exists
  const userUploadsDirectory = getUserUploadsDirectory(user)

  // Check limits
  const totalFileSize = files.reduce((acc, file) => acc + file.size, 0)
  if (!isEnoughStorageToUploadFile(user, totalFileSize)) {
    return { success: false, error: `Insufficient storage to upload these files` }
  }

  if (isSubscriptionExpired(user)) {
    return {
      success: false,
      error: "Your subscription has expired, please upgrade your account or buy new subscription plan",
    }
  }

  // Process each file
  const uploadedFiles = await Promise.all(
    files.map(async (file) => {
      if (!(file instanceof File)) {
        return { success: false, error: "Invalid file" }
      }

      // Save file to filesystem
      const fileUuid = randomUUID()
      const relativeFilePath = unsortedFilePath(fileUuid, file.name)
      const arrayBuffer = await file.arrayBuffer()
      const buffer = Buffer.from(arrayBuffer)

      const fullFilePath = safePathJoin(userUploadsDirectory, relativeFilePath)
      await mkdir(path.dirname(fullFilePath), { recursive: true })

      await writeFile(fullFilePath, buffer)

      // Create file record in database
      const fileRecord = await createFile(user.id, {
        id: fileUuid,
        filename: file.name,
        path: relativeFilePath,
        mimetype: file.type,
        metadata: {
          size: file.size,
          lastModified: file.lastModified,
        },
      })

      return fileRecord
    })
  )

  const storageUsed = await getDirectorySize(getUserUploadsDirectory(user))
  await updateUser(user.id, { storageUsed })

  console.log("uploadedFiles", uploadedFiles)

  revalidatePath("/unsorted")

  return { success: true, error: null }
}
```

## File: `app/(app)/files/page.tsx`
```tsx
import { Metadata } from "next"
import { notFound } from "next/navigation"

export const metadata: Metadata = {
  title: "Uploading...",
}

export default function UploadStatusPage() {
  notFound()
}
```

## File: `app/(app)/files/download/[fileId]/route.ts`
```typescript
import { getCurrentUser } from "@/lib/auth"
import { fileExists, fullPathForFile } from "@/lib/files"
import { encodeFilename } from "@/lib/utils"
import { getFileById } from "@/models/files"
import fs from "fs/promises"
import { NextResponse } from "next/server"

export async function GET(request: Request, { params }: { params: Promise<{ fileId: string }> }) {
  const { fileId } = await params
  const user = await getCurrentUser()

  if (!fileId) {
    return new NextResponse("No fileId provided", { status: 400 })
  }

  try {
    // Find file in database
    const file = await getFileById(fileId, user.id)

    if (!file || file.userId !== user.id) {
      return new NextResponse("File not found or does not belong to the user", { status: 404 })
    }

    // Check if file exists
    const fullFilePath = fullPathForFile(user, file)
    const isFileExists = await fileExists(fullFilePath)
    if (!isFileExists) {
      return new NextResponse(`File not found on disk: ${file.path}`, { status: 404 })
    }

    // Read file
    const fileBuffer = await fs.readFile(fullFilePath)

    // Return file with proper content type and encoded filename
    return new NextResponse(fileBuffer, {
      headers: {
        "Content-Type": file.mimetype,
          "Content-Disposition": `attachment; filename*=${encodeFilename(file.filename)}`,
        },
    })
  } catch (error) {
    console.error("Error serving file:", error)
    return new NextResponse("Internal Server Error", { status: 500 })
  }
}
```

## File: `app/(app)/files/preview/[fileId]/route.ts`
```typescript
import { getCurrentUser } from "@/lib/auth"
import { fileExists, fullPathForFile } from "@/lib/files"
import { generateFilePreviews } from "@/lib/previews/generate"
import { getFileById } from "@/models/files"
import fs from "fs/promises"
import { NextResponse } from "next/server"
import path from "path"
import { encodeFilename } from "@/lib/utils"

export async function GET(request: Request, { params }: { params: Promise<{ fileId: string }> }) {
  const { fileId } = await params
  const user = await getCurrentUser()

  if (!fileId) {
    return new NextResponse("No fileId provided", { status: 400 })
  }

  const url = new URL(request.url)
  const page = parseInt(url.searchParams.get("page") || "1", 10)

  try {
    // Find file in database
    const file = await getFileById(fileId, user.id)

    if (!file || file.userId !== user.id) {
      return new NextResponse("File not found or does not belong to the user", { status: 404 })
    }

    // Check if file exists on disk
    const fullFilePath = fullPathForFile(user, file)
    const isFileExists = await fileExists(fullFilePath)
    if (!isFileExists) {
      return new NextResponse(`File not found on disk: ${file.path}`, { status: 404 })
    }

    // Generate previews
    const { contentType, previews } = await generateFilePreviews(user, fullFilePath, file.mimetype)
    if (page > previews.length) {
      return new NextResponse("Page not found", { status: 404 })
    }
    const previewPath = previews[page - 1] || fullFilePath

    // Read file
    const fileBuffer = await fs.readFile(previewPath)

    // Return file with proper content type
    return new NextResponse(fileBuffer, {
      headers: {
        "Content-Type": contentType,
        "Content-Disposition": `inline; filename*=${encodeFilename(path.basename(previewPath))}`,
      },
    })
  } catch (error) {
    console.error("Error serving file:", error)
    return new NextResponse("Internal Server Error", { status: 500 })
  }
}
```

## File: `app/(app)/files/static/[filename]/route.ts`
```typescript
import { getCurrentUser } from "@/lib/auth"
import { fileExists, getStaticDirectory, safePathJoin } from "@/lib/files"
import fs from "fs/promises"
import lookup from "mime-types"
import { NextResponse } from "next/server"

export async function GET(request: Request, { params }: { params: Promise<{ filename: string }> }) {
  const { filename } = await params
  const user = await getCurrentUser()

  if (!filename) {
    return new NextResponse("No filename provided", { status: 400 })
  }

  const staticFilesDirectory = getStaticDirectory(user)

  try {
    const fullFilePath = safePathJoin(staticFilesDirectory, filename)
    const isFileExists = await fileExists(fullFilePath)
    if (!isFileExists) {
      return new NextResponse(`File not found for user: ${filename}`, { status: 404 })
    }

    const fileBuffer = await fs.readFile(fullFilePath)

    return new NextResponse(fileBuffer, {
      headers: {
        "Content-Type": lookup.lookup(filename) || "application/octet-stream",
      },
    })
  } catch (error) {
    console.error("Error serving file:", error)
    return new NextResponse("Internal Server Error", { status: 500 })
  }
}
```

## File: `app/(app)/import/csv/actions.tsx`
```tsx
"use server"

import { ActionState } from "@/lib/actions"
import { getCurrentUser } from "@/lib/auth"
import { EXPORT_AND_IMPORT_FIELD_MAP } from "@/models/export_and_import"
import { createTransaction } from "@/models/transactions"
import { Transaction } from "@/prisma/client"
import { parse } from "@fast-csv/parse"
import { revalidatePath } from "next/cache"

export async function parseCSVAction(
  _prevState: ActionState<string[][]> | null,
  formData: FormData
): Promise<ActionState<string[][]>> {
  const file = formData.get("file") as File
  if (!file) {
    return { success: false, error: "No file uploaded" }
  }

  if (!file.name.toLowerCase().endsWith(".csv")) {
    return { success: false, error: "Only CSV files are allowed" }
  }

  try {
    const buffer = Buffer.from(await file.arrayBuffer())
    const rows: string[][] = []

    const parser = parse()
      .on("data", (row) => rows.push(row))
      .on("error", (error) => {
        throw error
      })
    parser.write(buffer)
    parser.end()

    // Wait for parsing to complete
    await new Promise((resolve) => parser.on("end", resolve))

    return { success: true, data: rows }
  } catch (error) {
    console.error("Error parsing CSV:", error)
    return { success: false, error: "Failed to parse CSV file" }
  }
}

export async function saveTransactionsAction(
  _prevState: ActionState<Transaction> | null,
  formData: FormData
): Promise<ActionState<Transaction>> {
  const user = await getCurrentUser()
  try {
    const rows = JSON.parse(formData.get("rows") as string) as Record<string, unknown>[]

    for (const row of rows) {
      const transactionData: Record<string, unknown> = {}
      for (const [fieldCode, value] of Object.entries(row)) {
        const fieldDef = EXPORT_AND_IMPORT_FIELD_MAP[fieldCode]
        if (fieldDef?.import) {
          transactionData[fieldCode] = await fieldDef.import(user.id, value as string)
        } else {
          transactionData[fieldCode] = value as string
        }
      }

      await createTransaction(user.id, transactionData)
    }

    revalidatePath("/import/csv")
    revalidatePath("/transactions")

    return { success: true }
  } catch (error) {
    console.error("Error saving transactions:", error)
    return { success: false, error: "Failed to save transactions: " + error }
  }
}
```

## File: `app/(app)/import/csv/page.tsx`
```tsx
import { ImportCSVTable } from "@/components/import/csv"
import { getCurrentUser } from "@/lib/auth"
import { getFields } from "@/models/fields"

export default async function CSVImportPage() {
  const user = await getCurrentUser()
  const fields = await getFields(user.id)
  return (
    <div className="flex flex-col gap-4 p-4">
      <ImportCSVTable fields={fields} />
    </div>
  )
}
```

## File: `app/(app)/settings/actions.ts`
```typescript
"use server"

import {
  categoryFormSchema,
  currencyFormSchema,
  fieldFormSchema,
  projectFormSchema,
  settingsFormSchema,
} from "@/forms/settings"
import { userFormSchema } from "@/forms/users"
import { ActionState } from "@/lib/actions"
import { getCurrentUser } from "@/lib/auth"
import { uploadStaticImage } from "@/lib/uploads"
import { codeFromName, randomHexColor } from "@/lib/utils"
import { createCategory, deleteCategory, updateCategory } from "@/models/categories"
import { createCurrency, deleteCurrency, updateCurrency } from "@/models/currencies"
import { createField, deleteField, updateField } from "@/models/fields"
import { createProject, deleteProject, updateProject } from "@/models/projects"
import { SettingsMap, updateSettings } from "@/models/settings"
import { updateUser } from "@/models/users"
import { Prisma, User } from "@/prisma/client"
import { revalidatePath } from "next/cache"
import path from "path"

export async function saveSettingsAction(
  _prevState: ActionState<SettingsMap> | null,
  formData: FormData
): Promise<ActionState<SettingsMap>> {
  const user = await getCurrentUser()
  const validatedForm = settingsFormSchema.safeParse(Object.fromEntries(formData))

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  for (const key in validatedForm.data) {
    const value = validatedForm.data[key as keyof typeof validatedForm.data]
    if (value !== undefined) {
      await updateSettings(user.id, key, value)
    }
  }

  revalidatePath("/settings")
  return { success: true }
}

export async function saveProfileAction(
  _prevState: ActionState<User> | null,
  formData: FormData
): Promise<ActionState<User>> {
  const user = await getCurrentUser()
  const validatedForm = userFormSchema.safeParse(Object.fromEntries(formData))

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  // Upload avatar
  let avatarUrl = user.avatar
  const avatarFile = formData.get("avatar") as File | null
  if (avatarFile instanceof File && avatarFile.size > 0) {
    try {
      const uploadedAvatarPath = await uploadStaticImage(user, avatarFile, "avatar.webp", 500, 500)
      avatarUrl = `/files/static/${path.basename(uploadedAvatarPath)}`
    } catch (error) {
      return { success: false, error: "Failed to upload avatar: " + error }
    }
  }

  // Upload business logo
  let businessLogoUrl = user.businessLogo
  const businessLogoFile = formData.get("businessLogo") as File | null
  if (businessLogoFile instanceof File && businessLogoFile.size > 0) {
    try {
      const uploadedBusinessLogoPath = await uploadStaticImage(user, businessLogoFile, "businessLogo.png", 500, 500)
      businessLogoUrl = `/files/static/${path.basename(uploadedBusinessLogoPath)}`
    } catch (error) {
      return { success: false, error: "Failed to upload business logo: " + error }
    }
  }

  // Update user
  await updateUser(user.id, {
    name: validatedForm.data.name !== undefined ? validatedForm.data.name : user.name,
    avatar: avatarUrl,
    businessName: validatedForm.data.businessName !== undefined ? validatedForm.data.businessName : user.businessName,
    businessAddress:
      validatedForm.data.businessAddress !== undefined ? validatedForm.data.businessAddress : user.businessAddress,
    businessBankDetails:
      validatedForm.data.businessBankDetails !== undefined
        ? validatedForm.data.businessBankDetails
        : user.businessBankDetails,
    businessLogo: businessLogoUrl,
  })

  revalidatePath("/settings/profile")
  revalidatePath("/settings/business")
  return { success: true }
}

export async function addProjectAction(userId: string, data: Prisma.ProjectCreateInput) {
  const validatedForm = projectFormSchema.safeParse(data)

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  const project = await createProject(userId, {
    code: codeFromName(validatedForm.data.name),
    name: validatedForm.data.name,
    llm_prompt: validatedForm.data.llm_prompt || null,
    color: validatedForm.data.color || randomHexColor(),
  })
  revalidatePath("/settings/projects")

  return { success: true, project }
}

export async function editProjectAction(userId: string, code: string, data: Prisma.ProjectUpdateInput) {
  const validatedForm = projectFormSchema.safeParse(data)

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  const project = await updateProject(userId, code, {
    name: validatedForm.data.name,
    llm_prompt: validatedForm.data.llm_prompt,
    color: validatedForm.data.color || "",
  })
  revalidatePath("/settings/projects")

  return { success: true, project }
}

export async function deleteProjectAction(userId: string, code: string) {
  try {
    await deleteProject(userId, code)
  } catch (error) {
    return { success: false, error: "Failed to delete project" + error }
  }
  revalidatePath("/settings/projects")
  return { success: true }
}

export async function addCurrencyAction(userId: string, data: Prisma.CurrencyCreateInput) {
  const validatedForm = currencyFormSchema.safeParse(data)

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  const currency = await createCurrency(userId, {
    code: validatedForm.data.code,
    name: validatedForm.data.name,
  })
  revalidatePath("/settings/currencies")

  return { success: true, currency }
}

export async function editCurrencyAction(userId: string, code: string, data: Prisma.CurrencyUpdateInput) {
  const validatedForm = currencyFormSchema.safeParse(data)

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  const currency = await updateCurrency(userId, code, { name: validatedForm.data.name })
  revalidatePath("/settings/currencies")
  return { success: true, currency }
}

export async function deleteCurrencyAction(userId: string, code: string) {
  try {
    await deleteCurrency(userId, code)
  } catch (error) {
    return { success: false, error: "Failed to delete currency" + error }
  }
  revalidatePath("/settings/currencies")
  return { success: true }
}

export async function addCategoryAction(userId: string, data: Prisma.CategoryCreateInput) {
  const validatedForm = categoryFormSchema.safeParse(data)

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  const code = codeFromName(validatedForm.data.name)
  try {
    const category = await createCategory(userId, {
      code,
      name: validatedForm.data.name,
      llm_prompt: validatedForm.data.llm_prompt,
      color: validatedForm.data.color || "",
    })
    revalidatePath("/settings/categories")

    return { success: true, category }
  } catch (error: unknown) {
    if (error instanceof Prisma.PrismaClientKnownRequestError && error.code === "P2002") {
      return {
        success: false,
        error: `Category with the code "${code}" already exists. Try a different name.`,
      }
    }
    return { success: false, error: "Failed to create category" }
  }
}

export async function editCategoryAction(userId: string, code: string, data: Prisma.CategoryUpdateInput) {
  const validatedForm = categoryFormSchema.safeParse(data)

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  const category = await updateCategory(userId, code, {
    name: validatedForm.data.name,
    llm_prompt: validatedForm.data.llm_prompt,
    color: validatedForm.data.color || "",
  })
  revalidatePath("/settings/categories")

  return { success: true, category }
}

export async function deleteCategoryAction(userId: string, code: string) {
  try {
    await deleteCategory(userId, code)
  } catch (error) {
    return { success: false, error: "Failed to delete category" + error }
  }
  revalidatePath("/settings/categories")
  return { success: true }
}

export async function addFieldAction(userId: string, data: Prisma.FieldCreateInput) {
  const validatedForm = fieldFormSchema.safeParse(data)

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  const field = await createField(userId, {
    code: codeFromName(validatedForm.data.name),
    name: validatedForm.data.name,
    type: validatedForm.data.type,
    llm_prompt: validatedForm.data.llm_prompt,
    isVisibleInList: validatedForm.data.isVisibleInList,
    isVisibleInAnalysis: validatedForm.data.isVisibleInAnalysis,
    isRequired: validatedForm.data.isRequired,
    isExtra: true,
  })
  revalidatePath("/settings/fields")

  return { success: true, field }
}

export async function editFieldAction(userId: string, code: string, data: Prisma.FieldUpdateInput) {
  const validatedForm = fieldFormSchema.safeParse(data)

  if (!validatedForm.success) {
    return { success: false, error: validatedForm.error.message }
  }

  const field = await updateField(userId, code, {
    name: validatedForm.data.name,
    type: validatedForm.data.type,
    llm_prompt: validatedForm.data.llm_prompt,
    isVisibleInList: validatedForm.data.isVisibleInList,
    isVisibleInAnalysis: validatedForm.data.isVisibleInAnalysis,
    isRequired: validatedForm.data.isRequired,
  })
  revalidatePath("/settings/fields")

  return { success: true, field }
}

export async function deleteFieldAction(userId: string, code: string) {
  try {
    await deleteField(userId, code)
  } catch (error) {
    return { success: false, error: "Failed to delete field" + error }
  }
  revalidatePath("/settings/fields")
  return { success: true }
}
```

## File: `app/(app)/settings/layout.tsx`
```tsx
import { SideNav } from "@/components/settings/side-nav"
import { Separator } from "@/components/ui/separator"
import { Metadata } from "next"

export const metadata: Metadata = {
  title: "Settings",
  description: "Customize your settings here",
}

const settingsCategories = [
  {
    title: "General",
    href: "/settings",
  },
  {
    title: "Profile & Plan",
    href: "/settings/profile",
  },
  {
    title: "Business Details",
    href: "/settings/business",
  },
  {
    title: "LLM settings",
    href: "/settings/llm",
  },
  {
    title: "Fields",
    href: "/settings/fields",
  },
  {
    title: "Categories",
    href: "/settings/categories",
  },
  {
    title: "Projects",
    href: "/settings/projects",
  },
  {
    title: "Currencies",
    href: "/settings/currencies",
  },
  {
    title: "Backups",
    href: "/settings/backups",
  },
  {
    title: "Danger Zone",
    href: "/settings/danger",
  },
]

export default function SettingsLayout({ children }: { children: React.ReactNode }) {
  return (
    <>
      <div className="space-y-6 p-10 pb-16">
        <div className="space-y-0.5">
          <h2 className="text-2xl font-bold tracking-tight">Settings</h2>
          <p className="text-muted-foreground">Customize your settings here</p>
        </div>
        <Separator className="my-6" />
        <div className="flex flex-col space-y-8 lg:flex-row lg:space-x-12 lg:space-y-0">
          <aside className="-mx-4 lg:w-1/5">
            <SideNav items={settingsCategories} />
          </aside>
          <div className="flex w-full">{children}</div>
        </div>
      </div>
    </>
  )
}
```

## File: `app/(app)/settings/loading.tsx`
```tsx
import { Skeleton } from "@/components/ui/skeleton"

export default function Loading() {
  return (
    <div className="flex flex-col gap-4 w-full">
      <Skeleton className="h-10 w-56" />
      <Skeleton className="w-full h-[350px]" />
    </div>
  )
}
```

## File: `app/(app)/settings/page.tsx`
```tsx
import GlobalSettingsForm from "@/components/settings/global-settings-form"
import { getCurrentUser } from "@/lib/auth"
import { getCategories } from "@/models/categories"
import { getCurrencies } from "@/models/currencies"
import { getSettings } from "@/models/settings"

export default async function SettingsPage() {
  const user = await getCurrentUser()
  const settings = await getSettings(user.id)
  const currencies = await getCurrencies(user.id)
  const categories = await getCategories(user.id)

  return (
    <>
      <div className="w-full max-w-2xl">
        <GlobalSettingsForm settings={settings} currencies={currencies} categories={categories} />
      </div>
    </>
  )
}
```

## File: `app/(app)/settings/backups/actions.ts`
```typescript
"use server"

import { ActionState } from "@/lib/actions"
import { getCurrentUser } from "@/lib/auth"
import { prisma } from "@/lib/db"
import { getUserUploadsDirectory, safePathJoin } from "@/lib/files"
import { MODEL_BACKUP, modelFromJSON } from "@/models/backups"
import fs from "fs/promises"
import JSZip from "jszip"
import path from "path"

const SUPPORTED_BACKUP_VERSIONS = ["1.0"]
const REMOVE_EXISTING_DATA = true
const MAX_BACKUP_SIZE = 256 * 1024 * 1024 // 256MB

type BackupRestoreResult = {
  counters: Record<string, number>
}

export async function restoreBackupAction(
  _prevState: ActionState<BackupRestoreResult> | null,
  formData: FormData
): Promise<ActionState<BackupRestoreResult>> {
  const user = await getCurrentUser()
  const userUploadsDirectory = getUserUploadsDirectory(user)
  const file = formData.get("file") as File

  if (!file || file.size === 0) {
    return { success: false, error: "No file provided" }
  }

  if (file.size > MAX_BACKUP_SIZE) {
    return { success: false, error: `Backup file too large. Maximum size is ${MAX_BACKUP_SIZE / 1024 / 1024}MB` }
  }

  // Read zip archive
  let zip: JSZip
  try {
    const fileBuffer = await file.arrayBuffer()
    const fileData = Buffer.from(fileBuffer)
    zip = await JSZip.loadAsync(fileData)
  } catch (error) {
    return { success: false, error: "Bad zip archive: " + (error as Error).message }
  }

  // Check metadata and start restoring
  try {
    const metadataFile = zip.file("data/metadata.json")
    if (metadataFile) {
      const metadataContent = await metadataFile.async("string")
      try {
        const metadata = JSON.parse(metadataContent)
        if (!metadata.version || !SUPPORTED_BACKUP_VERSIONS.includes(metadata.version)) {
          return {
            success: false,
            error: `Incompatible backup version: ${
              metadata.version || "unknown"
            }. Supported versions: ${SUPPORTED_BACKUP_VERSIONS.join(", ")}`,
          }
        }
        console.log(`Restoring backup version ${metadata.version} created at ${metadata.timestamp}`)
      } catch (error) {
        console.warn("Could not parse backup metadata:", error)
      }
    } else {
      console.warn("No metadata found in backup, assuming legacy format")
    }

    // Remove existing data
    if (REMOVE_EXISTING_DATA) {
      await cleanupUserTables(user.id)
      await fs.rm(userUploadsDirectory, { recursive: true, force: true })
    }

    const counters: Record<string, number> = {}

    // Restore tables
    for (const backup of MODEL_BACKUP) {
      try {
        const jsonFile = zip.file(`data/${backup.filename}`)
        if (jsonFile) {
          const jsonContent = await jsonFile.async("string")
          const restoredCount = await modelFromJSON(user.id, backup, jsonContent)
          console.log(`Restored ${restoredCount} records from ${backup.filename}`)
          counters[backup.filename] = restoredCount
        }
      } catch (error) {
        console.error(`Error restoring model from ${backup.filename}:`, error)
      }
    }

    // Restore files
    try {
      let restoredFilesCount = 0
      const files = await prisma.file.findMany({
        where: {
          userId: user.id,
        },
      })

      const userUploadsDirectory = getUserUploadsDirectory(user)

      for (const file of files) {
        const filePathWithoutPrefix = path.normalize(file.path.replace(/^.*\/uploads\//, ""))
        const zipFilePath = path.join("data/uploads", filePathWithoutPrefix)
        const zipFile = zip.file(zipFilePath)
        if (!zipFile) {
          console.log(`File ${file.path} not found in backup`)
          continue
        }

        const fileContents = await zipFile.async("nodebuffer")
        const fullFilePath = safePathJoin(userUploadsDirectory, filePathWithoutPrefix)
        if (!fullFilePath.startsWith(path.normalize(userUploadsDirectory))) {
          console.error(`Attempted path traversal detected for file ${file.path}`)
          continue
        }

        try {
          await fs.mkdir(path.dirname(fullFilePath), { recursive: true })
          await fs.writeFile(fullFilePath, fileContents)
          restoredFilesCount++
        } catch (error) {
          console.error(`Error writing file ${fullFilePath}:`, error)
          continue
        }

        await prisma.file.update({
          where: { id: file.id },
          data: {
            path: filePathWithoutPrefix,
          },
        })
      }
      counters["Uploaded attachments"] = restoredFilesCount
    } catch (error) {
      console.error("Error restoring uploaded files:", error)
      return {
        success: false,
        error: `Error restoring uploaded files: ${error instanceof Error ? error.message : String(error)}`,
      }
    }

    return { success: true, data: { counters } }
  } catch (error) {
    console.error("Error restoring from backup:", error)
    return {
      success: false,
      error: `Error restoring from backup: ${error instanceof Error ? error.message : String(error)}`,
    }
  }
}

async function cleanupUserTables(userId: string) {
  // Delete in reverse order to handle foreign key constraints
  for (const { model } of [...MODEL_BACKUP].reverse()) {
    try {
      await model.deleteMany({ where: { userId } })
    } catch (error) {
      console.error(`Error clearing table:`, error)
    }
  }
}
```

## File: `app/(app)/settings/backups/page.tsx`
```tsx
"use client"

import { FormError } from "@/components/forms/error"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { useDownload } from "@/hooks/use-download"
import { useProgress } from "@/hooks/use-progress"
import { Download, Loader2 } from "lucide-react"
import { useActionState } from "react"
import { restoreBackupAction } from "./actions"

export default function BackupSettingsPage() {
  const [restoreState, restoreBackup, restorePending] = useActionState(restoreBackupAction, null)

  const { isLoading, startProgress, progress } = useProgress({
    onError: (error) => {
      console.error("Backup progress error:", error)
    },
  })

  const { download, isDownloading } = useDownload({
    onError: (error) => {
      console.error("Download error:", error)
    },
  })

  const handleDownload = async () => {
    try {
      const progressId = await startProgress("backup")
      const downloadUrl = `/settings/backups/data?progressId=${progressId || ""}`
      await download(downloadUrl, "taxhacker-backup.zip")
    } catch (error) {
      console.error("Failed to start backup:", error)
    }
  }

  return (
    <div className="container flex flex-col gap-4">
      <div className="flex flex-col gap-4">
        <h1 className="text-2xl font-bold">Download backup</h1>
        <div className="flex flex-row gap-4">
          <Button onClick={handleDownload} disabled={isLoading || isDownloading}>
            {isLoading ? (
              progress?.current ? (
                `Archiving ${progress.current}/${progress.total} files`
              ) : (
                "Preparing backup. Don't close the page..."
              )
            ) : isDownloading ? (
              "Archive is created. Downloading..."
            ) : (
              <>
                <Download className="mr-2" /> Download Data Archive
              </>
            )}
          </Button>
        </div>
        <div className="text-sm text-muted-foreground max-w-xl">
          Inside the archive you will find all the uploaded files, as well as JSON files for transactions, categories,
          projects, fields, currencies, and settings. You can view, edit or migrate your data to another service.
        </div>
      </div>

      <Card className="flex flex-col gap-2 mt-16 p-5 bg-red-100 max-w-xl">
        <h2 className="text-xl font-semibold">Restore from a backup</h2>
        <p className="text-sm text-muted-foreground">
          ⚠️ This action is irreversible. Restoring from a backup will delete all existing data from your current
          database and remove all uploaded files. Be careful and make a backup first!
        </p>
        <form action={restoreBackup}>
          <div className="flex flex-col gap-4 pt-4">
            <label>
              <input type="file" name="file" required />
            </label>
            <label className="flex flex-row gap-2 items-center">
              <input type="checkbox" name="removeExistingData" required />
              <span className="text-red-500">I undestand that it will permanently delete all existing data</span>
            </label>
            <Button type="submit" variant="destructive" disabled={restorePending}>
              {restorePending ? (
                <>
                  <Loader2 className="animate-spin" /> Restoring from backup... (it can take a while)
                </>
              ) : (
                "Restore from backup"
              )}
            </Button>
          </div>
        </form>
        {restoreState?.error && <FormError>{restoreState.error}</FormError>}
      </Card>

      {restoreState?.success && (
        <Card className="flex flex-col gap-2 p-5 bg-green-100 max-w-xl">
          <h2 className="text-xl font-semibold">Backup restored successfully</h2>
          <p className="text-sm text-muted-foreground">You can now continue using the app. Import stats:</p>
          <ul className="list-disc list-inside">
            {Object.entries(restoreState.data?.counters || {}).map(([key, value]) => (
              <li key={key}>
                <span className="font-bold">{key}</span>: {value} items
              </li>
            ))}
          </ul>
        </Card>
      )}
    </div>
  )
}
```

## File: `app/(app)/settings/backups/data/route.ts`
```typescript
import { getCurrentUser } from "@/lib/auth"
import { fileExists, getUserUploadsDirectory } from "@/lib/files"
import { MODEL_BACKUP, modelToJSON } from "@/models/backups"
import { updateProgress } from "@/models/progress"
import fs from "fs/promises"
import JSZip from "jszip"
import { NextResponse } from "next/server"
import path from "path"

const MAX_FILE_SIZE = 64 * 1024 * 1024 // 64MB
const BACKUP_VERSION = "1.0"
const PROGRESS_UPDATE_INTERVAL_MS = 2000 // 2 seconds

export async function GET(request: Request) {
  const user = await getCurrentUser()
  const userUploadsDirectory = getUserUploadsDirectory(user)
  const url = new URL(request.url)
  const progressId = url.searchParams.get("progressId")

  try {
    const zip = new JSZip()
    const rootFolder = zip.folder("data")
    if (!rootFolder) {
      console.error("Failed to create zip folder")
      return new NextResponse("Internal Server Error", { status: 500 })
    }

    // Add metadata with version information
    rootFolder.file(
      "metadata.json",
      JSON.stringify(
        {
          version: BACKUP_VERSION,
          timestamp: new Date().toISOString(),
          models: MODEL_BACKUP.map((m) => m.filename),
        },
        null,
        2
      )
    )

    // Backup models
    for (const backup of MODEL_BACKUP) {
      try {
        const jsonContent = await modelToJSON(user.id, backup)
        rootFolder.file(backup.filename, jsonContent)
      } catch (error) {
        console.error(`Error exporting table ${backup.filename}:`, error)
      }
    }

    const uploadsFolder = rootFolder.folder("uploads")
    if (!uploadsFolder) {
      console.error("Failed to create uploads folder")
      return new NextResponse("Internal Server Error", { status: 500 })
    }

    const uploadedFiles = await getAllFilePaths(userUploadsDirectory)

    // Update progress with total files if progressId is provided
    if (progressId) {
      await updateProgress(user.id, progressId, { total: uploadedFiles.length })
    }

    let processedFiles = 0
    let lastProgressUpdate = Date.now()

    for (const file of uploadedFiles) {
      try {
        // Check file size before reading
        const stats = await fs.stat(file)
        if (stats.size > MAX_FILE_SIZE) {
          console.warn(
            `Skipping large file ${file} (${Math.round(stats.size / 1024 / 1024)}MB > ${
              MAX_FILE_SIZE / 1024 / 1024
            }MB limit)`
          )
          continue
        }

        const fileContent = await fs.readFile(file)
        uploadsFolder.file(file.replace(userUploadsDirectory, ""), fileContent)

        processedFiles++

        // Update progress every PROGRESS_UPDATE_INTERVAL_MS milliseconds
        const now = Date.now()
        if (progressId && now - lastProgressUpdate >= PROGRESS_UPDATE_INTERVAL_MS) {
          await updateProgress(user.id, progressId, { current: processedFiles })
          lastProgressUpdate = now
        }
      } catch (error) {
        console.error(`Error reading file ${file}:`, error)
      }
    }

    // Final progress update
    if (progressId) {
      await updateProgress(user.id, progressId, { current: uploadedFiles.length })
    }

    const archive = await zip.generateAsync({ type: "blob" })

    return new NextResponse(archive, {
      headers: {
        "Content-Type": "application/octet-stream",
        "Content-Disposition": `attachment; filename="taxhacker-backup.zip"`,
      },
    })
  } catch (error) {
    console.error("Error exporting database:", error)
    return new NextResponse("Internal Server Error", { status: 500 })
  }
}

async function getAllFilePaths(dirPath: string): Promise<string[]> {
  const filePaths: string[] = []

  async function readDirectoryRecursively(currentPath: string) {
    const isDirExists = await fileExists(currentPath)
    if (!isDirExists) {
      return
    }

    const entries = await fs.readdir(currentPath, { withFileTypes: true })
    for (const entry of entries) {
      const fullPath = path.join(currentPath, entry.name)
      if (entry.isDirectory()) {
        await readDirectoryRecursively(fullPath)
      } else {
        filePaths.push(fullPath)
      }
    }
  }

  await readDirectoryRecursively(dirPath)

  return filePaths
}
```

## File: `app/(app)/settings/business/page.tsx`
```tsx
import BusinessSettingsForm from "@/components/settings/business-settings-form"
import { getCurrentUser } from "@/lib/auth"

export default async function BusinessSettingsPage() {
  const user = await getCurrentUser()

  return (
    <>
      <div className="w-full max-w-2xl">
        <BusinessSettingsForm user={user} />
      </div>
    </>
  )
}
```

## File: `app/(app)/settings/categories/page.tsx`
```tsx
import { addCategoryAction, deleteCategoryAction, editCategoryAction } from "@/app/(app)/settings/actions"
import { CrudTable } from "@/components/settings/crud"
import { getCurrentUser } from "@/lib/auth"
import { randomHexColor } from "@/lib/utils"
import { getCategories } from "@/models/categories"
import { Prisma } from "@/prisma/client"

export default async function CategoriesSettingsPage() {
  const user = await getCurrentUser()
  const categories = await getCategories(user.id)
  const categoriesWithActions = categories.map((category) => ({
    ...category,
    isEditable: true,
    isDeletable: true,
  }))

  return (
    <div className="container">
      <h1 className="text-2xl font-bold mb-2">Categories</h1>
      <p className="text-sm text-gray-500 mb-6 max-w-prose">
        Create your own categories that better reflect the type of income and expenses you have. Define an LLM Prompt so
        that AI can determine this category automatically.
      </p>

      <CrudTable
        items={categoriesWithActions}
        columns={[
          { key: "name", label: "Name", editable: true },
          { key: "llm_prompt", label: "LLM Prompt", editable: true },
          { key: "color", label: "Color", type: "color", defaultValue: randomHexColor(), editable: true },
        ]}
        onDelete={async (code) => {
          "use server"
          return await deleteCategoryAction(user.id, code)
        }}
        onAdd={async (data) => {
          "use server"
          return await addCategoryAction(user.id, data as Prisma.CategoryCreateInput)
        }}
        onEdit={async (code, data) => {
          "use server"
          return await editCategoryAction(user.id, code, data as Prisma.CategoryUpdateInput)
        }}
      />
    </div>
  )
}
```

## File: `app/(app)/settings/currencies/page.tsx`
```tsx
import { addCurrencyAction, deleteCurrencyAction, editCurrencyAction } from "@/app/(app)/settings/actions"
import { CrudTable } from "@/components/settings/crud"
import { getCurrentUser } from "@/lib/auth"
import { getCurrencies } from "@/models/currencies"

export default async function CurrenciesSettingsPage() {
  const user = await getCurrentUser()
  const currencies = await getCurrencies(user.id)
  const currenciesWithActions = currencies.map((currency) => ({
    ...currency,
    isEditable: true,
    isDeletable: true,
  }))

  return (
    <div className="container">
      <h1 className="text-2xl font-bold mb-2">Currencies</h1>
      <p className="text-sm text-gray-500 mb-6 max-w-prose">
        Custom currencies would not be automatically converted but you still can have them.
      </p>
      <CrudTable
        items={currenciesWithActions}
        columns={[
          { key: "code", label: "Code", editable: true },
          { key: "name", label: "Name", editable: true },
        ]}
        onDelete={async (code) => {
          "use server"
          return await deleteCurrencyAction(user.id, code)
        }}
        onAdd={async (data) => {
          "use server"
          return await addCurrencyAction(user.id, data as { code: string; name: string })
        }}
        onEdit={async (code, data) => {
          "use server"
          return await editCurrencyAction(user.id, code, data as { name: string })
        }}
      />
    </div>
  )
}
```

## File: `app/(app)/settings/danger/actions.ts`
```typescript
"use server"

import { prisma } from "@/lib/db"
import { DEFAULT_CATEGORIES, DEFAULT_CURRENCIES, DEFAULT_FIELDS, DEFAULT_SETTINGS } from "@/models/defaults"
import { User } from "@/prisma/client"
import { redirect } from "next/navigation"

export async function resetLLMSettings(user: User) {
  const llmSettings = DEFAULT_SETTINGS.filter((setting) => setting.code === "prompt_analyse_new_file")

  for (const setting of llmSettings) {
    await prisma.setting.upsert({
      where: { userId_code: { code: setting.code, userId: user.id } },
      update: { value: setting.value },
      create: { ...setting, userId: user.id },
    })
  }

  redirect("/settings/llm")
}

export async function resetFieldsAndCategories(user: User) {
  // Reset categories
  for (const category of DEFAULT_CATEGORIES) {
    await prisma.category.upsert({
      where: { userId_code: { code: category.code, userId: user.id } },
      update: { name: category.name, color: category.color, llm_prompt: category.llm_prompt, createdAt: new Date() },
      create: { ...category, userId: user.id, createdAt: new Date() },
    })
  }
  await prisma.category.deleteMany({
    where: { userId: user.id, code: { notIn: DEFAULT_CATEGORIES.map((category) => category.code) } },
  })

  // Reset currencies
  for (const currency of DEFAULT_CURRENCIES) {
    await prisma.currency.upsert({
      where: { userId_code: { code: currency.code, userId: user.id } },
      update: { name: currency.name },
      create: { ...currency, userId: user.id },
    })
  }
  await prisma.currency.deleteMany({
    where: { userId: user.id, code: { notIn: DEFAULT_CURRENCIES.map((currency) => currency.code) } },
  })

  // Reset fields
  for (const field of DEFAULT_FIELDS) {
    await prisma.field.upsert({
      where: { userId_code: { code: field.code, userId: user.id } },
      update: {
        name: field.name,
        type: field.type,
        llm_prompt: field.llm_prompt,
        createdAt: new Date(),
        isVisibleInList: field.isVisibleInList,
        isVisibleInAnalysis: field.isVisibleInAnalysis,
        isRequired: field.isRequired,
        isExtra: field.isExtra,
      },
      create: { ...field, userId: user.id, createdAt: new Date() },
    })
  }
  await prisma.field.deleteMany({
    where: { userId: user.id, code: { notIn: DEFAULT_FIELDS.map((field) => field.code) } },
  })

  redirect("/settings/fields")
}
```

## File: `app/(app)/settings/danger/page.tsx`
```tsx
import { Button } from "@/components/ui/button"
import { getCurrentUser } from "@/lib/auth"
import { resetFieldsAndCategories, resetLLMSettings } from "./actions"

export default async function DangerSettingsPage() {
  const user = await getCurrentUser()

  return (
    <div className="container">
      <h1 className="text-2xl font-bold mb-2 text-red-500">The Danger Zone</h1>
      <p className="text-sm text-red-400 mb-8 max-w-prose">
        The settings here will overwrite your existing fields, categories and prompts. Use them only if something is
        broken.
      </p>
      <div className="space-y-10">
        <div className="space-y-2">
          <h3 className="text-lg font-bold">LLM settings</h3>
          <p className="text-sm text-gray-500 mb-6 max-w-prose">
            This will reset the system prompt and other LLM settings to their default values
          </p>
          <form
            action={async () => {
              "use server"
              await resetLLMSettings(user)
            }}
          >
            <Button variant="destructive" type="submit">
              Reset main LLM prompt
            </Button>
          </form>
        </div>
        <div className="space-y-2">
          <h3 className="text-lg font-bold">Fields, currencies and categories</h3>
          <p className="text-sm text-gray-500 mb-6 max-w-prose">
            This will reset all fields, currencies and categories to their default values
          </p>
          <form
            action={async () => {
              "use server"
              await resetFieldsAndCategories(user)
            }}
          >
            <Button variant="destructive" type="submit">
              Reset fields, currencies and categories
            </Button>
          </form>
        </div>
      </div>
    </div>
  )
}
```

## File: `app/(app)/settings/fields/page.tsx`
```tsx
import { addFieldAction, deleteFieldAction, editFieldAction } from "@/app/(app)/settings/actions"
import { CrudTable } from "@/components/settings/crud"
import { getCurrentUser } from "@/lib/auth"
import { getFields } from "@/models/fields"
import { Prisma } from "@/prisma/client"

export default async function FieldsSettingsPage() {
  const user = await getCurrentUser()
  const fields = await getFields(user.id)
  const fieldsWithActions = fields.map((field) => ({
    ...field,
    isEditable: true,
    isDeletable: field.isExtra,
  }))

  return (
    <div className="container">
      <h1 className="text-2xl font-bold mb-2">Custom Fields</h1>
      <p className="text-sm text-gray-500 mb-6 max-w-prose">
        You can add new fields to your transactions. Standard fields can&apos;t be removed but you can tweak their
        prompts or hide them. If you don&apos;t want a field to be analyzed by AI but filled in by hand, leave the
        &quot;LLM prompt&quot; empty.
      </p>
      <CrudTable
        items={fieldsWithActions}
        columns={[
          { key: "name", label: "Name", editable: true },
          {
            key: "type",
            label: "Type",
            type: "select",
            options: ["string", "number", "boolean"],
            defaultValue: "string",
            editable: true,
          },
          { key: "llm_prompt", label: "LLM Prompt", editable: true },
          {
            key: "isVisibleInList",
            label: "Show in transactions table",
            type: "checkbox",
            defaultValue: false,
            editable: true,
          },
          {
            key: "isVisibleInAnalysis",
            label: "Show in analysis form",
            type: "checkbox",
            defaultValue: false,
            editable: true,
          },
          {
            key: "isRequired",
            label: "Is required",
            type: "checkbox",
            defaultValue: false,
            editable: true,
          },
        ]}
        onDelete={async (code) => {
          "use server"
          return await deleteFieldAction(user.id, code)
        }}
        onAdd={async (data) => {
          "use server"
          return await addFieldAction(user.id, data as Prisma.FieldCreateInput)
        }}
        onEdit={async (code, data) => {
          "use server"
          return await editFieldAction(user.id, code, data as Prisma.FieldUpdateInput)
        }}
      />
    </div>
  )
}
```

## File: `app/(app)/settings/llm/page.tsx`
```tsx
import LLMSettingsForm from "@/components/settings/llm-settings-form"
import { getCurrentUser } from "@/lib/auth"
import config from "@/lib/config"
import { getFields } from "@/models/fields"
import { getSettings } from "@/models/settings"

export default async function LlmSettingsPage() {
  const user = await getCurrentUser()
  const settings = await getSettings(user.id)
  const fields = await getFields(user.id)

  return (
    <>
      <div className="w-full max-w-2xl">
        <LLMSettingsForm settings={settings} fields={fields} showApiKey={config.selfHosted.isEnabled} />
      </div>
    </>
  )
}
```

## File: `app/(app)/settings/profile/page.tsx`
```tsx
import ProfileSettingsForm from "@/components/settings/profile-settings-form"
import { getCurrentUser } from "@/lib/auth"

export default async function ProfileSettingsPage() {
  const user = await getCurrentUser()

  return (
    <>
      <div className="w-full max-w-2xl">
        <ProfileSettingsForm user={user} />
      </div>
    </>
  )
}
```

## File: `app/(app)/settings/projects/page.tsx`
```tsx
import { addProjectAction, deleteProjectAction, editProjectAction } from "@/app/(app)/settings/actions"
import { CrudTable } from "@/components/settings/crud"
import { getCurrentUser } from "@/lib/auth"
import { randomHexColor } from "@/lib/utils"
import { getProjects } from "@/models/projects"
import { Prisma } from "@/prisma/client"

export default async function ProjectsSettingsPage() {
  const user = await getCurrentUser()
  const projects = await getProjects(user.id)
  const projectsWithActions = projects.map((project) => ({
    ...project,
    isEditable: true,
    isDeletable: true,
  }))

  return (
    <div className="container">
      <h1 className="text-2xl font-bold mb-2">Projects</h1>
      <p className="text-sm text-gray-500 mb-6 max-w-prose">
        Use projects to differentiate between the type of activities you do For example: Freelancing, YouTube channel,
        Blogging. Projects are just a convenient way to separate statistics.
      </p>
      <CrudTable
        items={projectsWithActions}
        columns={[
          { key: "name", label: "Name", editable: true },
          { key: "llm_prompt", label: "LLM Prompt", editable: true },
          { key: "color", label: "Color", type: "color", defaultValue: randomHexColor(), editable: true },
        ]}
        onDelete={async (code) => {
          "use server"
          return await deleteProjectAction(user.id, code)
        }}
        onAdd={async (data) => {
          "use server"
          return await addProjectAction(user.id, data as Prisma.ProjectCreateInput)
        }}
        onEdit={async (code, data) => {
          "use server"
          return await editProjectAction(user.id, code, data as Prisma.ProjectUpdateInput)
        }}
      />
    </div>
  )
}
```

## File: `app/(app)/transactions/actions.ts`
```typescript
"use server"

import { transactionFormSchema } from "@/forms/transactions"
import { ActionState } from "@/lib/actions"
import { getCurrentUser, isSubscriptionExpired } from "@/lib/auth"
import {
  getDirectorySize,
  getTransactionFileUploadPath,
  getUserUploadsDirectory,
  isEnoughStorageToUploadFile,
  safePathJoin,
} from "@/lib/files"
import { updateField } from "@/models/fields"
import { createFile, deleteFile } from "@/models/files"
import {
  bulkDeleteTransactions,
  createTransaction,
  deleteTransaction,
  getTransactionById,
  updateTransaction,
  updateTransactionFiles,
} from "@/models/transactions"
import { updateUser } from "@/models/users"
import { Transaction } from "@/prisma/client"
import { randomUUID } from "crypto"
import { mkdir, writeFile } from "fs/promises"
import { revalidatePath } from "next/cache"
import path from "path"

export async function createTransactionAction(
  _prevState: ActionState<Transaction> | null,
  formData: FormData
): Promise<ActionState<Transaction>> {
  try {
    const user = await getCurrentUser()
    const validatedForm = transactionFormSchema.safeParse(Object.fromEntries(formData.entries()))

    if (!validatedForm.success) {
      return { success: false, error: validatedForm.error.message }
    }

    const transaction = await createTransaction(user.id, validatedForm.data)

    revalidatePath("/transactions")
    return { success: true, data: transaction }
  } catch (error) {
    console.error("Failed to create transaction:", error)
    return { success: false, error: "Failed to create transaction" }
  }
}

export async function saveTransactionAction(
  _prevState: ActionState<Transaction> | null,
  formData: FormData
): Promise<ActionState<Transaction>> {
  try {
    const user = await getCurrentUser()
    const transactionId = formData.get("transactionId") as string
    const validatedForm = transactionFormSchema.safeParse(Object.fromEntries(formData.entries()))

    if (!validatedForm.success) {
      return { success: false, error: validatedForm.error.message }
    }

    const transaction = await updateTransaction(transactionId, user.id, validatedForm.data)

    revalidatePath("/transactions")
    return { success: true, data: transaction }
  } catch (error) {
    console.error("Failed to update transaction:", error)
    return { success: false, error: "Failed to save transaction" }
  }
}

export async function deleteTransactionAction(
  _prevState: ActionState<Transaction> | null,
  transactionId: string
): Promise<ActionState<Transaction>> {
  try {
    const user = await getCurrentUser()
    const transaction = await getTransactionById(transactionId, user.id)
    if (!transaction) throw new Error("Transaction not found")

    await deleteTransaction(transaction.id, user.id)

    revalidatePath("/transactions")

    return { success: true, data: transaction }
  } catch (error) {
    console.error("Failed to delete transaction:", error)
    return { success: false, error: "Failed to delete transaction" }
  }
}

export async function deleteTransactionFileAction(
  transactionId: string,
  fileId: string
): Promise<ActionState<Transaction>> {
  if (!fileId || !transactionId) {
    return { success: false, error: "File ID and transaction ID are required" }
  }

  const user = await getCurrentUser()
  const transaction = await getTransactionById(transactionId, user.id)
  if (!transaction) {
    return { success: false, error: "Transaction not found" }
  }

  await updateTransactionFiles(
    transactionId,
    user.id,
    transaction.files ? (transaction.files as string[]).filter((id) => id !== fileId) : []
  )

  await deleteFile(fileId, user.id)

  // Update user storage used
  const storageUsed = await getDirectorySize(getUserUploadsDirectory(user))
  await updateUser(user.id, { storageUsed })

  revalidatePath(`/transactions/${transactionId}`)
  return { success: true, data: transaction }
}

export async function uploadTransactionFilesAction(formData: FormData): Promise<ActionState<Transaction>> {
  try {
    const transactionId = formData.get("transactionId") as string
    const files = formData.getAll("files") as File[]

    if (!files || !transactionId) {
      return { success: false, error: "No files or transaction ID provided" }
    }

    const user = await getCurrentUser()
    const transaction = await getTransactionById(transactionId, user.id)
    if (!transaction) {
      return { success: false, error: "Transaction not found" }
    }

    const userUploadsDirectory = getUserUploadsDirectory(user)

    // Check limits
    const totalFileSize = files.reduce((acc, file) => acc + file.size, 0)
    if (!isEnoughStorageToUploadFile(user, totalFileSize)) {
      return { success: false, error: `Insufficient storage to upload new files` }
    }

    if (isSubscriptionExpired(user)) {
      return {
        success: false,
        error: "Your subscription has expired, please upgrade your account or buy new subscription plan",
      }
    }

    const fileRecords = await Promise.all(
      files.map(async (file) => {
        const fileUuid = randomUUID()
        const relativeFilePath = getTransactionFileUploadPath(fileUuid, file.name, transaction)
        const arrayBuffer = await file.arrayBuffer()
        const buffer = Buffer.from(arrayBuffer)

        const fullFilePath = safePathJoin(userUploadsDirectory, relativeFilePath)
        await mkdir(path.dirname(fullFilePath), { recursive: true })

        await writeFile(fullFilePath, buffer)

        // Create file record in database
        const fileRecord = await createFile(user.id, {
          id: fileUuid,
          filename: file.name,
          path: relativeFilePath,
          mimetype: file.type,
          isReviewed: true,
          metadata: {
            size: file.size,
            lastModified: file.lastModified,
          },
        })

        return fileRecord
      })
    )

    // Update invoice with the new file ID
    await updateTransactionFiles(
      transactionId,
      user.id,
      transaction.files
        ? [...(transaction.files as string[]), ...fileRecords.map((file) => file.id)]
        : fileRecords.map((file) => file.id)
    )

    // Update user storage used
    const storageUsed = await getDirectorySize(getUserUploadsDirectory(user))
    await updateUser(user.id, { storageUsed })

    revalidatePath(`/transactions/${transactionId}`)
    return { success: true }
  } catch (error) {
    console.error("Upload error:", error)
    return { success: false, error: `File upload failed: ${error}` }
  }
}

export async function bulkDeleteTransactionsAction(transactionIds: string[]) {
  try {
    const user = await getCurrentUser()
    await bulkDeleteTransactions(transactionIds, user.id)
    revalidatePath("/transactions")
    return { success: true }
  } catch (error) {
    console.error("Failed to delete transactions:", error)
    return { success: false, error: "Failed to delete transactions" }
  }
}

export async function updateFieldVisibilityAction(fieldCode: string, isVisible: boolean) {
  try {
    const user = await getCurrentUser()
    await updateField(user.id, fieldCode, {
      isVisibleInList: isVisible,
    })
    return { success: true }
  } catch (error) {
    console.error("Failed to update field visibility:", error)
    return { success: false, error: "Failed to update field visibility" }
  }
}
```

## File: `app/(app)/transactions/layout.tsx`
```tsx
export default async function TransactionsLayout({ children }: { children: React.ReactNode }) {
  return <div className="flex flex-col gap-4 p-4">{children}</div>
}
```

## File: `app/(app)/transactions/loading.tsx`
```tsx
import { Button } from "@/components/ui/button"
import { Skeleton } from "@/components/ui/skeleton"
import { Download, Loader2, Plus } from "lucide-react"

export default function Loading() {
  return (
    <>
      <header className="flex items-center justify-between mb-12">
        <h2 className="flex flex-row gap-3 md:gap-5">
          <span className="text-3xl font-bold tracking-tight">Transactions</span>
          <Loader2 className="h-10 w-10 animate-spin" />
        </h2>
        <div className="flex gap-2">
          <Button variant="outline">
            <Download />
            Export
          </Button>
          <Button>
            <Plus /> Add Transaction
          </Button>
        </div>
      </header>

      <div className="flex flex-row gap-2 w-full">
        <Skeleton className="h-8 w-full" />
        <Skeleton className="h-8 w-full" />
        <Skeleton className="h-8 w-full" />
        <Skeleton className="h-8 w-full" />
        <Skeleton className="h-8 w-full" />
      </div>

      <main>
        <div className="flex flex-col gap-3 w-full">
          {[...Array(15)].map((_, i) => (
            <Skeleton key={i} className="h-8" />
          ))}
        </div>
      </main>
    </>
  )
}
```

## File: `app/(app)/transactions/page.tsx`
```tsx
import { ExportTransactionsDialog } from "@/components/export/transactions"
import { UploadButton } from "@/components/files/upload-button"
import { TransactionSearchAndFilters } from "@/components/transactions/filters"
import { TransactionList } from "@/components/transactions/list"
import { NewTransactionDialog } from "@/components/transactions/new"
import { Pagination } from "@/components/transactions/pagination"
import { Button } from "@/components/ui/button"
import { getCurrentUser } from "@/lib/auth"
import { getCategories } from "@/models/categories"
import { getFields } from "@/models/fields"
import { getProjects } from "@/models/projects"
import { getTransactions, TransactionFilters } from "@/models/transactions"
import { Download, Plus, Upload } from "lucide-react"
import { Metadata } from "next"
import { redirect } from "next/navigation"

export const metadata: Metadata = {
  title: "Transactions",
  description: "Manage your transactions",
}

const TRANSACTIONS_PER_PAGE = 500

export default async function TransactionsPage({ searchParams }: { searchParams: Promise<TransactionFilters> }) {
  const { page, ...filters } = await searchParams
  const user = await getCurrentUser()
  const { transactions, total } = await getTransactions(user.id, filters, {
    limit: TRANSACTIONS_PER_PAGE,
    offset: ((page ?? 1) - 1) * TRANSACTIONS_PER_PAGE,
  })
  const categories = await getCategories(user.id)
  const projects = await getProjects(user.id)
  const fields = await getFields(user.id)

  // Reset page if user clicks a filter and no transactions are found
  if (page && page > 1 && transactions.length === 0) {
    const params = new URLSearchParams(filters as Record<string, string>)
    redirect(`?${params.toString()}`)
  }

  return (
    <>
      <header className="flex flex-wrap items-center justify-between gap-2 mb-8">
        <h2 className="flex flex-row gap-3 md:gap-5">
          <span className="text-3xl font-bold tracking-tight">Transactions</span>
          <span className="text-3xl tracking-tight opacity-20">{total}</span>
        </h2>
        <div className="flex gap-2">
          <ExportTransactionsDialog fields={fields} categories={categories} projects={projects} total={total}>
            <Download /> <span className="hidden md:block">Export</span>
          </ExportTransactionsDialog>
          <NewTransactionDialog>
            <Plus /> <span className="hidden md:block">Add Transaction</span>
          </NewTransactionDialog>
        </div>
      </header>

      <TransactionSearchAndFilters categories={categories} projects={projects} fields={fields} />

      <main>
        <TransactionList transactions={transactions} fields={fields} />

        {total > TRANSACTIONS_PER_PAGE && <Pagination totalItems={total} itemsPerPage={TRANSACTIONS_PER_PAGE} />}

        {transactions.length === 0 && (
          <div className="flex flex-col items-center justify-center gap-2 h-full min-h-[400px]">
            <p className="text-muted-foreground">
              You don&apos;t seem to have any transactions yet. Let&apos;s start and create the first one!
            </p>
            <div className="flex flex-row gap-5 mt-8">
              <UploadButton>
                <Upload /> Analyze New Invoice
              </UploadButton>
              <NewTransactionDialog>
                <Button variant="outline">
                  <Plus />
                  Add Manually
                </Button>
              </NewTransactionDialog>
            </div>
          </div>
        )}
      </main>
    </>
  )
}
```

## File: `app/(app)/transactions/[transactionId]/layout.tsx`
```tsx
import { getCurrentUser } from "@/lib/auth"
import { getTransactionById } from "@/models/transactions"
import { notFound } from "next/navigation"

export default async function TransactionLayout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ transactionId: string }>
}) {
  const { transactionId } = await params
  const user = await getCurrentUser()
  const transaction = await getTransactionById(transactionId, user.id)

  if (!transaction) {
    notFound()
  }

  return (
    <>
      <header className="flex items-center justify-between">
        <h2 className="text-3xl font-bold tracking-tight">Transaction Details</h2>
      </header>
      <main>
        <div className="flex flex-1 flex-col gap-4 pt-0">{children}</div>
      </main>
    </>
  )
}
```

## File: `app/(app)/transactions/[transactionId]/loading.tsx`
```tsx
import { Skeleton } from "@/components/ui/skeleton"

export default function Loading() {
  return (
    <div className="flex flex-wrap flex-row items-start justify-center gap-4 max-w-6xl">
      <Skeleton className="w-full h-[800px]" />
      <Skeleton className="w-1/3 max-w-[380px]" />
    </div>
  )
}
```

## File: `app/(app)/transactions/[transactionId]/page.tsx`
```tsx
import { FormTextarea } from "@/components/forms/simple"
import TransactionEditForm from "@/components/transactions/edit"
import TransactionFiles from "@/components/transactions/transaction-files"
import { Card } from "@/components/ui/card"
import { getCurrentUser } from "@/lib/auth"
import { incompleteTransactionFields } from "@/lib/stats"
import { getCategories } from "@/models/categories"
import { getCurrencies } from "@/models/currencies"
import { getFields } from "@/models/fields"
import { getFilesByTransactionId } from "@/models/files"
import { getProjects } from "@/models/projects"
import { getSettings } from "@/models/settings"
import { getTransactionById } from "@/models/transactions"
import Link from "next/link"
import { notFound } from "next/navigation"

export default async function TransactionPage({ params }: { params: Promise<{ transactionId: string }> }) {
  const { transactionId } = await params
  const user = await getCurrentUser()
  const transaction = await getTransactionById(transactionId, user.id)
  if (!transaction) {
    notFound()
  }

  const files = await getFilesByTransactionId(transactionId, user.id)
  const categories = await getCategories(user.id)
  const currencies = await getCurrencies(user.id)
  const settings = await getSettings(user.id)
  const fields = await getFields(user.id)
  const projects = await getProjects(user.id)
  const incompleteFields = incompleteTransactionFields(fields, transaction)

  return (
    <div className="flex flex-wrap flex-row items-start justify-center gap-4 max-w-6xl">
      <Card className="w-full flex-1 flex flex-col flex-wrap justify-center items-start overflow-hidden bg-gradient-to-br from-violet-50/80 via-indigo-50/80 to-white border-violet-200/60">
        {incompleteFields.length > 0 && (
          <div className="w-full flex flex-col gap-1 rounded-md bg-yellow-50 p-5">
            <span>
              Some fields are incomplete: <strong>{incompleteFields.map((field) => field.name).join(", ")}</strong>
            </span>
            <span className="text-xs text-muted-foreground">
              You can decide which fields are required for you in{" "}
              <Link href="/settings/fields" className="underline">
                Fields settings
              </Link>
              .
            </span>
          </div>
        )}
        <div className="w-full p-5">
          <TransactionEditForm
            transaction={transaction}
            categories={categories}
            currencies={currencies}
            settings={settings}
            fields={fields}
            projects={projects}
          />

          {transaction.text && (
            <details className="mt-10">
              <summary className="cursor-pointer text-sm font-medium">Recognized Text</summary>
              <Card className="flex items-stretch p-2 max-w-6xl">
                <div className="flex-1">
                  <FormTextarea
                    name="text"
                    defaultValue={transaction.text || ""}
                    hideIfEmpty={true}
                    className="w-full h-[400px]"
                  />
                </div>
              </Card>
            </details>
          )}
        </div>
      </Card>

      <div className="w-1/2 max-w-[400px] space-y-4">
        <TransactionFiles transaction={transaction} files={files} />
      </div>
    </div>
  )
}
```

## File: `app/(app)/unsorted/actions.ts`
```typescript
"use server"

import { AnalysisResult, analyzeTransaction } from "@/ai/analyze"
import { AnalyzeAttachment, loadAttachmentsForAI } from "@/ai/attachments"
import { buildLLMPrompt } from "@/ai/prompt"
import { fieldsToJsonSchema } from "@/ai/schema"
import { transactionFormSchema } from "@/forms/transactions"
import { ActionState } from "@/lib/actions"
import { getCurrentUser, isAiBalanceExhausted, isSubscriptionExpired } from "@/lib/auth"
import {
  getDirectorySize,
  getTransactionFileUploadPath,
  getUserUploadsDirectory,
  safePathJoin,
  unsortedFilePath,
} from "@/lib/files"
import { DEFAULT_PROMPT_ANALYSE_NEW_FILE } from "@/models/defaults"
import { createFile, deleteFile, getFileById, updateFile } from "@/models/files"
import { createTransaction, TransactionData, updateTransactionFiles } from "@/models/transactions"
import { updateUser } from "@/models/users"
import { Category, Field, File, Project, Transaction } from "@/prisma/client"
import { randomUUID } from "crypto"
import { mkdir, readFile, rename, writeFile } from "fs/promises"
import { revalidatePath } from "next/cache"
import path from "path"

export async function analyzeFileAction(
  file: File,
  settings: Record<string, string>,
  fields: Field[],
  categories: Category[],
  projects: Project[]
): Promise<ActionState<AnalysisResult>> {
  const user = await getCurrentUser()

  if (!file || file.userId !== user.id) {
    return { success: false, error: "File not found or does not belong to the user" }
  }

  if (isAiBalanceExhausted(user)) {
    return {
      success: false,
      error: "You used all of your pre-paid AI scans, please upgrade your account or buy new subscription plan",
    }
  }

  if (isSubscriptionExpired(user)) {
    return {
      success: false,
      error: "Your subscription has expired, please upgrade your account or buy new subscription plan",
    }
  }

  let attachments: AnalyzeAttachment[] = []
  try {
    attachments = await loadAttachmentsForAI(user, file)
  } catch (error) {
    console.error("Failed to retrieve files:", error)
    return { success: false, error: "Failed to retrieve files: " + error }
  }

  const prompt = buildLLMPrompt(
    settings.prompt_analyse_new_file || DEFAULT_PROMPT_ANALYSE_NEW_FILE,
    fields,
    categories,
    projects
  )

  const schema = fieldsToJsonSchema(fields)

  const results = await analyzeTransaction(prompt, schema, attachments, file.id, user.id)

  console.log("Analysis results:", results)

  if (results.data?.tokensUsed && results.data.tokensUsed > 0) {
    await updateUser(user.id, { aiBalance: { decrement: 1 } })
  }

  return results
}

export async function saveFileAsTransactionAction(
  _prevState: ActionState<Transaction> | null,
  formData: FormData
): Promise<ActionState<Transaction>> {
  try {
    const user = await getCurrentUser()
    const validatedForm = transactionFormSchema.safeParse(Object.fromEntries(formData.entries()))

    if (!validatedForm.success) {
      return { success: false, error: validatedForm.error.message }
    }

    // Get the file record
    const fileId = formData.get("fileId") as string
    const file = await getFileById(fileId, user.id)
    if (!file) throw new Error("File not found")

    // Create transaction
    const transaction = await createTransaction(user.id, validatedForm.data)

    // Move file to processed location
    const userUploadsDirectory = getUserUploadsDirectory(user)
    const originalFileName = path.basename(file.path)
    const newRelativeFilePath = getTransactionFileUploadPath(file.id, originalFileName, transaction)

    // Move file to new location and name
    const oldFullFilePath = safePathJoin(userUploadsDirectory, file.path)
    const newFullFilePath = safePathJoin(userUploadsDirectory, newRelativeFilePath)
    await mkdir(path.dirname(newFullFilePath), { recursive: true })
    await rename(path.resolve(oldFullFilePath), path.resolve(newFullFilePath))

    // Update file record
    await updateFile(file.id, user.id, {
      path: newRelativeFilePath,
      isReviewed: true,
    })

    await updateTransactionFiles(transaction.id, user.id, [file.id])

    revalidatePath("/unsorted")
    revalidatePath("/transactions")

    return { success: true, data: transaction }
  } catch (error) {
    console.error("Failed to save transaction:", error)
    return { success: false, error: `Failed to save transaction: ${error}` }
  }
}

export async function deleteUnsortedFileAction(
  _prevState: ActionState<Transaction> | null,
  fileId: string
): Promise<ActionState<Transaction>> {
  try {
    const user = await getCurrentUser()
    await deleteFile(fileId, user.id)
    revalidatePath("/unsorted")
    return { success: true }
  } catch (error) {
    console.error("Failed to delete file:", error)
    return { success: false, error: "Failed to delete file" }
  }
}

export async function splitFileIntoItemsAction(
  _prevState: ActionState<null> | null,
  formData: FormData
): Promise<ActionState<null>> {
  try {
    const user = await getCurrentUser()
    const fileId = formData.get("fileId") as string
    const items = JSON.parse(formData.get("items") as string) as TransactionData[]

    if (!fileId || !items || items.length === 0) {
      return { success: false, error: "File ID and items are required" }
    }

    // Get the original file
    const originalFile = await getFileById(fileId, user.id)
    if (!originalFile) {
      return { success: false, error: "Original file not found" }
    }

    // Get the original file's content
    const userUploadsDirectory = getUserUploadsDirectory(user)
    const originalFilePath = safePathJoin(userUploadsDirectory, originalFile.path)
    const fileContent = await readFile(originalFilePath)

    // Create a new file for each item
    for (const item of items) {
      const fileUuid = randomUUID()
      const fileName = `${originalFile.filename}-part-${item.name}`
      const relativeFilePath = unsortedFilePath(fileUuid, fileName)
      const fullFilePath = safePathJoin(userUploadsDirectory, relativeFilePath)

      // Create directory if it doesn't exist
      await mkdir(path.dirname(fullFilePath), { recursive: true })

      // Copy the original file content
      await writeFile(fullFilePath, fileContent)

      // Create file record in database with the item data cached
      await createFile(user.id, {
        id: fileUuid,
        filename: fileName,
        path: relativeFilePath,
        mimetype: originalFile.mimetype,
        metadata: originalFile.metadata,
        isSplitted: true,
        cachedParseResult: {
          name: item.name,
          merchant: item.merchant,
          description: item.description,
          total: item.total,
          currencyCode: item.currencyCode,
          categoryCode: item.categoryCode,
          projectCode: item.projectCode,
          type: item.type,
          issuedAt: item.issuedAt,
          note: item.note,
          text: item.text,
        },
      })
    }

    // Delete the original file
    await deleteFile(fileId, user.id)

    // Update user storage used
    const storageUsed = await getDirectorySize(getUserUploadsDirectory(user))
    await updateUser(user.id, { storageUsed })

    revalidatePath("/unsorted")
    return { success: true }
  } catch (error) {
    console.error("Failed to split file into items:", error)
    return { success: false, error: `Failed to split file into items: ${error}` }
  }
}
```

## File: `app/(app)/unsorted/layout.tsx`
```tsx
export default function UnsortedLayout({ children }: { children: React.ReactNode }) {
  return <div className="flex flex-col gap-4 p-4 w-full max-w-6xl">{children}</div>
}
```

## File: `app/(app)/unsorted/loading.tsx`
```tsx
import { Skeleton } from "@/components/ui/skeleton"
import { Loader2 } from "lucide-react"

export default function Loading() {
  return (
    <>
      <header className="flex items-center justify-between">
        <h2 className="text-3xl font-bold tracking-tight flex flex-row gap-2">
          <span>Loading unsorted files...</span>
          <Loader2 className="h-10 w-10 animate-spin" />
        </h2>
      </header>

      <Skeleton className="w-full h-[800px] flex flex-row flex-wrap md:flex-nowrap justify-center items-start gap-5 p-6">
        <Skeleton className="w-full h-full" />
        <div className="w-full flex flex-col gap-5">
          <Skeleton className="w-full h-12 mb-7" />
          {[...Array(4)].map((_, i) => (
            <div key={i} className="flex flex-col gap-2">
              <Skeleton className="w-[120px] h-4" />
              <Skeleton className="w-full h-9" />
            </div>
          ))}
          <div className="flex flex-row justify-end gap-2 mt-2">
            <Skeleton className="w-[80px] h-9" />
            <Skeleton className="w-[130px] h-9" />
          </div>
        </div>
      </Skeleton>
    </>
  )
}
```

## File: `app/(app)/unsorted/page.tsx`
```tsx
import { FilePreview } from "@/components/files/preview"
import { UploadButton } from "@/components/files/upload-button"
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import { AnalyzeAllButton } from "@/components/unsorted/analyze-all-button"
import AnalyzeForm from "@/components/unsorted/analyze-form"
import { getCurrentUser } from "@/lib/auth"
import config from "@/lib/config"
import { getCategories } from "@/models/categories"
import { getCurrencies } from "@/models/currencies"
import { getFields } from "@/models/fields"
import { getUnsortedFiles } from "@/models/files"
import { getProjects } from "@/models/projects"
import { getSettings } from "@/models/settings"
import { FileText, PartyPopper, Settings, Upload } from "lucide-react"
import { Metadata } from "next"
import Link from "next/link"

export const metadata: Metadata = {
  title: "Unsorted",
  description: "Analyze unsorted files",
}

export default async function UnsortedPage() {
  const user = await getCurrentUser()
  const files = await getUnsortedFiles(user.id)
  const categories = await getCategories(user.id)
  const projects = await getProjects(user.id)
  const currencies = await getCurrencies(user.id)
  const fields = await getFields(user.id)
  const settings = await getSettings(user.id)

  return (
    <>
      <header className="flex items-center justify-between">
        <h2 className="text-3xl font-bold tracking-tight">You have {files.length} unsorted files</h2>
        {files.length > 1 && <AnalyzeAllButton />}
      </header>

      {config.selfHosted.isEnabled &&
        !settings.openai_api_key &&
        !settings.google_api_key &&
        !settings.mistral_api_key && (
          <Alert>
            <Settings className="h-4 w-4 mt-2" />
            <div className="flex flex-row justify-between pt-2">
              <div className="flex flex-col">
                <AlertTitle>LLM provider API Key is required for analyzing files</AlertTitle>
                <AlertDescription>
                  Please set your LLM provider API key in the settings to use the analyze form.
                </AlertDescription>
              </div>
              <Link href="/settings/llm">
                <Button>Go to Settings</Button>
              </Link>
            </div>
          </Alert>
        )}

      <main className="flex flex-col gap-5">
        {files.map((file) => (
          <Card
            key={file.id}
            id={file.id}
            className="flex flex-row flex-wrap md:flex-nowrap justify-center items-start gap-5 p-5 bg-gradient-to-br from-violet-50/80 via-indigo-50/80 to-white border-violet-200/60 rounded-2xl"
          >
            <div className="w-full max-w-[500px]">
              <Card>
                <FilePreview file={file} />
              </Card>
            </div>

            <div className="w-full">
              <AnalyzeForm
                file={file}
                categories={categories}
                projects={projects}
                currencies={currencies}
                fields={fields}
                settings={settings}
              />
            </div>
          </Card>
        ))}
        {files.length == 0 && (
          <div className="flex flex-col items-center justify-center gap-2 h-full min-h-[600px]">
            <PartyPopper className="w-12 h-12 text-muted-foreground" />
            <p className="pt-4 text-muted-foreground">Everything is clear! Congrats!</p>
            <p className="flex flex-row gap-2 text-muted-foreground">
              <span>Drag and drop new files here to analyze</span>
              <Upload />
            </p>

            <div className="flex flex-row gap-5 mt-8">
              <UploadButton>
                <Upload /> Upload New File
              </UploadButton>
              <Button variant="outline" asChild>
                <Link href="/transactions">
                  <FileText />
                  Go to Transactions
                </Link>
              </Button>
            </div>
          </div>
        )}
      </main>
    </>
  )
}
```

## File: `app/(auth)/actions.ts`
```typescript
"use server"

import { createUserDefaults, isDatabaseEmpty } from "@/models/defaults"
import { updateSettings } from "@/models/settings"
import { getOrCreateSelfHostedUser } from "@/models/users"
import { revalidatePath } from "next/cache"
import { redirect } from "next/navigation"

export async function selfHostedGetStartedAction(formData: FormData) {
  const user = await getOrCreateSelfHostedUser()

  if (await isDatabaseEmpty(user.id)) {
    await createUserDefaults(user.id)
  }

  const apiKeys = [
    "openai_api_key",
    "google_api_key",
    "mistral_api_key"
  ]

  for (const key of apiKeys) {
    const value = formData.get(key)
    if (value) {
      await updateSettings(user.id, key, value as string)
    }
  }


  const defaultCurrency = formData.get("default_currency")
  if (defaultCurrency) {
    await updateSettings(user.id, "default_currency", defaultCurrency as string)
  }

  revalidatePath("/dashboard")
  redirect("/dashboard")
}
```

## File: `app/(auth)/layout.tsx`
```tsx
import { X } from "lucide-react"
import Link from "next/link"

export default function AuthLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gray-900 flex flex-col relative">
      <Link
        href="/"
        className="absolute top-4 right-4 flex items-center justify-center w-10 h-10 rounded-full bg-gray-800 hover:bg-gray-700 transition-colors"
      >
        <span className="text-gray-300 font-bold text-xl">
          <X />
        </span>
      </Link>
      <div className="flex-grow flex flex-col justify-center items-center py-12 px-4 sm:px-6 lg:px-8">{children}</div>
    </div>
  )
}

export const dynamic = "force-dynamic"
```

## File: `app/(auth)/cloud/page.tsx`
```tsx
import { Card, CardContent, CardTitle } from "@/components/ui/card"
import { ColoredText } from "@/components/ui/colored-text"
import config from "@/lib/config"
import { Mail } from "lucide-react"
import Link from "next/link"
import { redirect } from "next/navigation"

export default async function ChoosePlanPage() {
  if (config.selfHosted.isEnabled) {
    redirect(config.selfHosted.redirectUrl)
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <Card className="w-full max-w-4xl mx-auto p-8 flex flex-col items-center justify-center gap-8">
        <CardTitle className="text-4xl font-bold text-center">
          <ColoredText>TaxHacker Cloud Edition</ColoredText>
          <h2 className="mt-3 text-2xl font-semibold text-muted-foreground">Cloud plans are not available yet</h2>
        </CardTitle>
        <CardContent className="p-0 w-full">
          <div className="text-center text-md text-muted-foreground">
            Cloud plans are not available yet. Please use the self-hosted version or reach out for questions.
          </div>
        </CardContent>

        <div className="text-center text-muted-foreground">
          <Link
            href={`mailto:${config.app.supportEmail}`}
            className="flex flex-row gap-1 items-center hover:text-primary transition-colors underline"
          >
            <Mail className="w-4 h-4" />
            Contact us for custom plans
          </Link>
        </div>
      </Card>
    </div>
  )
}
```

## File: `app/(auth)/cloud/payment/success/page.tsx`
```tsx
import { LoginForm } from "@/components/auth/login-form"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardTitle } from "@/components/ui/card"
import { ColoredText } from "@/components/ui/colored-text"
import config from "@/lib/config"
import { PLANS, stripeClient } from "@/lib/stripe"
import { createUserDefaults, isDatabaseEmpty } from "@/models/defaults"
import { getOrCreateCloudUser } from "@/models/users"
import { Cake, Ghost } from "lucide-react"
import Link from "next/link"
import { redirect } from "next/navigation"
import Stripe from "stripe"

export default async function CloudPaymentSuccessPage({
  searchParams,
}: {
  searchParams: Promise<{ session_id: string }>
}) {
  const { session_id: sessionId } = await searchParams

  if (!stripeClient || !sessionId) {
    redirect(config.auth.loginUrl)
  }

  const session = await stripeClient.checkout.sessions.retrieve(sessionId)

  if (session.mode === "subscription" && session.status === "complete") {
    const subscription = (await stripeClient.subscriptions.retrieve(
      session.subscription as string
    )) as Stripe.Subscription

    const plan = Object.values(PLANS).find((p) => p.stripePriceId === subscription.items.data[0].price.id)
    const email = session.customer_details?.email || session.customer_email || ""
    const user = await getOrCreateCloudUser(email, {
      email: email,
      name: session.customer_details?.name || session.customer_details?.email || session.customer_email || "",
      stripeCustomerId: session.customer as string,
      membershipPlan: plan?.code,
      membershipExpiresAt: new Date(subscription.items.data[0].current_period_end * 1000),
      storageLimit: plan?.limits.storage,
      aiBalance: plan?.limits.ai,
    })

    return (
      <Card className="w-full max-w-xl mx-auto p-8 flex flex-col items-center justify-center gap-4">
        <Cake className="w-36 h-36" />
        <CardTitle className="text-3xl font-bold ">
          <ColoredText>Payment Successful</ColoredText>
        </CardTitle>
        <CardDescription className="text-center text-xl">
          Welcome to TaxHacker, {user.name}. You can login to your account now
        </CardDescription>
        <CardContent className="w-full">
          <LoginForm defaultEmail={user.email} />
        </CardContent>
      </Card>
    )
  } else {
    return (
      <Card className="w-full max-w-xl mx-auto p-8 flex flex-col items-center justify-center gap-4">
        <Ghost className="w-36 h-36" />
        <CardTitle className="text-3xl font-bold ">Payment Failed</CardTitle>
        <CardDescription className="text-center text-xl">Please try again...</CardDescription>
        <CardFooter>
          <Button asChild>
            <Link href="/">Go Home</Link>
          </Button>
        </CardFooter>
      </Card>
    )
  }
}
```

## File: `app/(auth)/enter/page.tsx`
```tsx
import { LoginForm } from "@/components/auth/login-form"
import { Card, CardContent, CardTitle } from "@/components/ui/card"
import { ColoredText } from "@/components/ui/colored-text"
import config from "@/lib/config"
import Image from "next/image"
import { redirect } from "next/navigation"

export default async function LoginPage() {
  if (config.selfHosted.isEnabled) {
    redirect(config.selfHosted.redirectUrl)
  }

  return (
    <Card className="w-full max-w-xl mx-auto p-8 flex flex-col items-center justify-center gap-4">
      <Image src="/logo/512.png" alt="Logo" width={144} height={144} className="w-36 h-36" />
      <CardTitle className="text-3xl font-bold ">
        <ColoredText>TaxHacker: Cloud Edition</ColoredText>
      </CardTitle>
      <CardContent className="w-full">
        <LoginForm />
      </CardContent>
    </Card>
  )
}
```

## File: `app/(auth)/self-hosted/page.tsx`
```tsx
import { Card, CardDescription, CardTitle } from "@/components/ui/card"
import { ColoredText } from "@/components/ui/colored-text"
import config from "@/lib/config"
import { PROVIDERS } from "@/lib/llm-providers"
import { getSelfHostedUser } from "@/models/users"
import { ShieldAlert } from "lucide-react"
import Image from "next/image"
import { redirect } from "next/navigation"
import SelfHostedSetupFormClient from "./setup-form-client"

export default async function SelfHostedWelcomePage() {
  if (!config.selfHosted.isEnabled) {
    return (
      <Card className="w-full max-w-xl mx-auto p-8 flex flex-col items-center justify-center gap-6">
        <CardTitle className="text-2xl font-bold flex items-center gap-2">
          <ShieldAlert className="w-6 h-6" />
          <span>Self-Hosted Mode is not enabled</span>
        </CardTitle>
        <CardDescription className="text-center text-lg flex flex-col gap-2">
          <p>
            To use TaxHacker in self-hosted mode, please set <code className="font-bold">SELF_HOSTED_MODE=true</code> in
            your environment.
          </p>
          <p>In self-hosted mode you can use your own ChatGPT API key and store your data on your own server.</p>
        </CardDescription>
      </Card>
    )
  }

  const user = await getSelfHostedUser()
  if (user) {
    redirect(config.selfHosted.redirectUrl)
  }

  const defaultProvider = PROVIDERS[0].key
  const defaultApiKeys: Record<string, string> = {
    openai: config.ai.openaiApiKey ?? "",
    google: config.ai.googleApiKey ?? "",
    mistral: config.ai.mistralApiKey ?? "",
  }

  return (
    <Card className="w-full max-w-xl mx-auto p-8 flex flex-col items-center justify-center gap-4">
      <Image src="/logo/512.png" alt="Logo" width={144} height={144} className="w-36 h-36" />
      <CardTitle className="text-3xl font-bold ">
        <ColoredText>TaxHacker: Self-Hosted Edition</ColoredText>
      </CardTitle>
      <CardDescription className="flex flex-col gap-4 text-center text-lg">
        <p>Welcome to your own instance of TaxHacker. Let&apos;s set up a couple of settings to get started.</p>
        <SelfHostedSetupFormClient defaultProvider={defaultProvider} defaultApiKeys={defaultApiKeys} />
      </CardDescription>
    </Card>
  )
}

export const dynamic = "force-dynamic"
```

## File: `app/(auth)/self-hosted/setup-form-client.tsx`
```tsx
"use client"
import { useState, useRef, useEffect, useCallback } from "react"
import { FormSelectCurrency } from "@/components/forms/select-currency"
import { FormInput } from "@/components/forms/simple"
import { Button } from "@/components/ui/button"
import { DEFAULT_CURRENCIES, DEFAULT_SETTINGS } from "@/models/defaults"
import { selfHostedGetStartedAction } from "../actions"
import { FormSelect } from "@/components/forms/simple"
import { PROVIDERS } from "@/lib/llm-providers"

type Props = {
  defaultProvider: string
  defaultApiKeys: Record<string, string>
}

export default function SelfHostedSetupFormClient({ defaultProvider, defaultApiKeys }: Props) {
  const [provider, setProvider] = useState(defaultProvider)
  const selected = PROVIDERS.find(p => p.key === provider)!
  const getDefaultApiKey = useCallback((providerKey: string) => defaultApiKeys[providerKey] ?? "", [defaultApiKeys])

  const [apiKey, setApiKey] = useState(getDefaultApiKey(provider))
  const userTyped = useRef(false)

  useEffect(() => {
    if (!userTyped.current) {
      setApiKey(getDefaultApiKey(provider))
    }
    userTyped.current = false
  }, [provider, getDefaultApiKey])

  return (
    <form action={selfHostedGetStartedAction} className="flex flex-col gap-8 pt-8">
      <div className="flex flex-row gap-4 items-center justify-center">
        <FormSelect
          title="LLM provider"
          name="provider"
          value={provider}
          onValueChange={setProvider}
          items={PROVIDERS.map(p => ({
            code: p.key,
            name: p.label,
            logo: p.logo
          }))}
        />
        <FormSelectCurrency
          title="Default Currency"
          name="default_currency"
          defaultValue={DEFAULT_SETTINGS.find((s) => s.code === "default_currency")?.value ?? "EUR"}
          currencies={DEFAULT_CURRENCIES}
        />
      </div>
      <div>
        <FormInput
          title={`${selected.label} API Key`}
          name={selected.apiKeyName}
          value={apiKey ?? ""}
          onChange={e => {
            setApiKey(e.target.value)
            userTyped.current = true
          }}
          placeholder={selected.placeholder}
        />
        <small className="text-xs text-muted-foreground flex justify-center mt-2">
          Get key from
          {"\u00A0"}
          <a href={selected.help.url} target="_blank" className="underline">
            {selected.help.label}
          </a>
        </small>
      </div>
      <Button type="submit" className="w-auto p-6">
        Get Started
      </Button>
    </form>
  )
}
```

## File: `app/(auth)/self-hosted/redirect/route.ts`
```typescript
import config from "@/lib/config"
import { createUserDefaults, isDatabaseEmpty } from "@/models/defaults"
import { getSelfHostedUser } from "@/models/users"
import { revalidatePath } from "next/cache"
import { redirect } from "next/navigation"

export async function GET() {
  if (!config.selfHosted.isEnabled) {
    redirect(config.auth.loginUrl)
  }

  const user = await getSelfHostedUser()
  if (!user) {
    redirect(config.selfHosted.welcomeUrl)
  }

  if (await isDatabaseEmpty(user.id)) {
    await createUserDefaults(user.id)
  }

  revalidatePath("/dashboard")
  redirect("/dashboard")
}
```

## File: `app/api/auth/[...all]/route.ts`
```typescript
import { auth } from "@/lib/auth"
import { toNextJsHandler } from "better-auth/next-js"

export const { POST, GET } = toNextJsHandler(auth)
```

## File: `app/api/currency/route.ts`
```typescript
import { getSession } from "@/lib/auth"
import { PoorManCache } from "@/lib/cache"
import { format, isSameDay, subDays } from "date-fns"
import { NextRequest, NextResponse } from "next/server"

type HistoricRate = {
  currency: string
  rate: number
  inverse: number
}

const currencyCache = new PoorManCache<number>(24 * 60 * 60 * 1000) // 24 hours

function generateCacheKey(fromCurrency: string, toCurrency: string, date: string): string {
  return `${fromCurrency},${toCurrency},${date}`
}

const CLEANUP_INTERVAL = 90 * 60 * 1000
if (typeof setInterval !== "undefined") {
  setInterval(() => currencyCache.cleanup(), CLEANUP_INTERVAL)
}

export async function GET(request: NextRequest) {
  const session = await getSession()
  if (!session || !session.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  try {
    const searchParams = request.nextUrl.searchParams
    const fromCurrency = searchParams.get("from")
    const toCurrency = searchParams.get("to")
    const dateParam = searchParams.get("date")

    if (!fromCurrency || !toCurrency || !dateParam) {
      return NextResponse.json({ error: "Missing required parameters: from, to, date" }, { status: 400 })
    }

    let date = new Date(dateParam)

    if (isNaN(date.getTime())) {
      return NextResponse.json({ error: "Invalid date format" }, { status: 400 })
    }

    // hack to get yesterday's rate if it's today
    if (isSameDay(date, new Date())) {
      date = subDays(date, 1)
    }

    const formattedDate = format(date, "yyyy-MM-dd")

    // Check cache first
    const cacheKey = generateCacheKey(fromCurrency, toCurrency, formattedDate)
    const cachedRate = currencyCache.get(cacheKey)

    if (cachedRate !== undefined) {
      return NextResponse.json({ rate: cachedRate, cached: true })
    }

    const url = `https://www.xe.com/currencytables/?from=${fromCurrency}&date=${formattedDate}`

    const response = await fetch(url)

    if (!response.ok) {
      return NextResponse.json(
        { error: `Failed to fetch currency data: ${response.status}` },
        { status: response.status }
      )
    }

    const html = await response.text()

    // Extract the JSON data from the __NEXT_DATA__ script tag
    const scriptTagRegex = /<script id="__NEXT_DATA__" type="application\/json">([\s\S]*?)<\/script>/
    const match = html.match(scriptTagRegex)

    if (!match || !match[1]) {
      return NextResponse.json({ error: "Could not find currency data in the page" }, { status: 500 })
    }

    const jsonData = JSON.parse(match[1])
    const historicRates = jsonData.props.pageProps.historicRates as HistoricRate[]

    if (!historicRates || historicRates.length === 0) {
      return NextResponse.json({ error: "No currency rates found for the specified date" }, { status: 404 })
    }

    const rate = historicRates.find((rate) => rate.currency === toCurrency)

    if (!rate) {
      return NextResponse.json({ error: `Currency rate not found for ${toCurrency}` }, { status: 404 })
    }

    // Store in cache
    currencyCache.set(cacheKey, rate.rate)

    return NextResponse.json({ rate: rate.rate, cached: false })
  } catch (error) {
    console.error("Currency API error:", error)
    return NextResponse.json({ error: "Internal server error" }, { status: 500 })
  }
}
```

## File: `app/api/progress/[progressId]/route.ts`
```typescript
import { getSession } from "@/lib/auth"
import { getOrCreateProgress, getProgressById } from "@/models/progress"
import { NextRequest, NextResponse } from "next/server"

const POLL_INTERVAL_MS = 2000 // 2 seconds

export async function GET(req: NextRequest, { params }: { params: Promise<{ progressId: string }> }) {
  const session = await getSession()
  if (!session || !session.user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  const userId = session.user.id
  const { progressId } = await params
  const url = new URL(req.url)
  const type = url.searchParams.get("type") || "unknown"

  await getOrCreateProgress(userId, progressId, type)

  const encoder = new TextEncoder()
  const stream = new ReadableStream({
    async start(controller) {
      let lastSent: any = null
      let stopped = false

      req.signal.addEventListener("abort", () => {
        stopped = true
        controller.close()
      })

      while (!stopped) {
        const progress = await getProgressById(userId, progressId)
        if (!progress) {
          controller.enqueue(encoder.encode(`event: error\ndata: {"error":"Not found"}\n\n`))
          controller.close()
          break
        }

        // Only send if progress has changed
        if (JSON.stringify(progress) !== JSON.stringify(lastSent)) {
          controller.enqueue(encoder.encode(`data: ${JSON.stringify(progress)}\n\n`))
          lastSent = progress

          // If progress is complete, close the connection
          if (progress.current === progress.total && progress.total > 0) {
            controller.close()
            break
          }
        }

        await new Promise((res) => setTimeout(res, POLL_INTERVAL_MS))
      }
    },
  })

  return new Response(stream, {
    headers: {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache, no-transform",
      Connection: "keep-alive",
      "Access-Control-Allow-Origin": "*",
    },
  })
}
```

## File: `app/api/stripe/checkout/route.ts`
```typescript
import config from "@/lib/config"
import { PLANS, stripeClient } from "@/lib/stripe"
import { NextRequest, NextResponse } from "next/server"

export async function POST(request: NextRequest) {
  const { searchParams } = new URL(request.url)
  const code = searchParams.get("code")

  if (!code) {
    return NextResponse.json({ error: "Missing plan code" }, { status: 400 })
  }

  if (!stripeClient) {
    return NextResponse.json({ error: "Stripe is not enabled" }, { status: 500 })
  }

  const plan = PLANS[code]
  if (!plan || !plan.isAvailable) {
    return NextResponse.json({ error: "Invalid or inactive plan" }, { status: 400 })
  }

  try {
    const session = await stripeClient.checkout.sessions.create({
      billing_address_collection: "auto",
      line_items: [
        {
          price: plan.stripePriceId,
          quantity: 1,
        },
      ],
      mode: "subscription",
      automatic_tax: {
        enabled: true,
      },
      allow_promotion_codes: true,
      success_url: config.stripe.paymentSuccessUrl,
      cancel_url: config.stripe.paymentCancelUrl,
    })

    if (!session.url) {
      console.log(session)
      return NextResponse.json({ error: `Failed to create checkout session: ${session}` }, { status: 500 })
    }

    return NextResponse.json({ session })
  } catch (error) {
    console.error(error)
    return NextResponse.json({ error: `Failed to create checkout session: ${error}` }, { status: 500 })
  }
}
```

## File: `app/api/stripe/portal/route.ts`
```typescript
import { getCurrentUser } from "@/lib/auth"
import { stripeClient } from "@/lib/stripe"
import { NextRequest, NextResponse } from "next/server"

export async function GET(request: NextRequest) {
  const user = await getCurrentUser()
  if (!user) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  if (!stripeClient) {
    return new NextResponse("Stripe client is not initialized", { status: 500 })
  }

  try {
    if (!user.stripeCustomerId) {
      return NextResponse.json({ error: "No Stripe customer ID found for this user" }, { status: 400 })
    }

    const portalSession = await stripeClient.billingPortal.sessions.create({
      customer: user.stripeCustomerId,
      return_url: `${request.nextUrl.origin}/settings/profile`,
    })

    return NextResponse.redirect(portalSession.url)
  } catch (error) {
    console.error("Stripe portal error:", error)
    return NextResponse.json({ error: "Failed to create Stripe portal session" }, { status: 500 })
  }
}
```

## File: `app/api/stripe/webhook/route.ts`
```typescript
import config from "@/lib/config"
import { PLANS, stripeClient } from "@/lib/stripe"
import { createUserDefaults, isDatabaseEmpty } from "@/models/defaults"
import { getOrCreateCloudUser, getUserByStripeCustomerId, updateUser } from "@/models/users"
import { NextResponse } from "next/server"
import Stripe from "stripe"

export async function POST(request: Request) {
  const signature = request.headers.get("stripe-signature")
  const body = await request.text()

  if (!signature || !config.stripe.webhookSecret) {
    return new NextResponse("Webhook signature or secret missing", { status: 400 })
  }

  if (!stripeClient) {
    return new NextResponse("Stripe client is not initialized", { status: 500 })
  }

  let event: Stripe.Event

  try {
    event = stripeClient.webhooks.constructEvent(body, signature, config.stripe.webhookSecret)
  } catch (err) {
    console.error(`Webhook signature verification failed:`, err)
    return new NextResponse("Webhook signature verification failed", { status: 400 })
  }

  console.log("Webhook event:", event)

  // Handle the event
  try {
    switch (event.type) {
      case "checkout.session.completed": {
        const session = event.data.object as Stripe.Checkout.Session
        const customerId = session.customer as string
        const subscriptionId = session.subscription as string
        const subscription = await stripeClient.subscriptions.retrieve(subscriptionId)

        for (const item of subscription.items.data) {
          await handleUserSubscriptionUpdate(customerId, item)
        }
        break
      }

      case "customer.subscription.created":
      case "customer.subscription.updated":
      case "customer.subscription.deleted": {
        const subscription = event.data.object as Stripe.Subscription
        const customerId = subscription.customer as string

        for (const item of subscription.items.data) {
          await handleUserSubscriptionUpdate(customerId, item)
        }
        break
      }

      default:
        console.log(`Unhandled event type ${event.type}`)
        return new NextResponse("No handler for event type", { status: 400 })
    }

    return new NextResponse("Webhook processed successfully", { status: 200 })
  } catch (error) {
    console.error("Error processing webhook:", error)
    return new NextResponse("Webhook processing failed", { status: 500 })
  }
}

async function handleUserSubscriptionUpdate(
  customerId: string,
  item: Stripe.SubscriptionItem
) {
  console.log(`Updating subscription for customer ${customerId}`)

  if (!stripeClient) {
    return new NextResponse("Stripe client is not initialized", { status: 500 })
  }

  const plan = Object.values(PLANS).find((p) => p.stripePriceId === item.price.id)
  if (!plan) {
    throw new Error(`Plan not found for price ID: ${item.price.id}`)
  }

  let user = await getUserByStripeCustomerId(customerId)
  if (!user) {
    const customer = (await stripeClient.customers.retrieve(customerId)) as Stripe.Customer
    console.log(`User not found for customer ${customerId}, creating new user with email ${customer.email}`)

    user = await getOrCreateCloudUser(customer.email as string, {
      email: customer.email as string,
      name: customer.name as string,
      stripeCustomerId: customer.id,
    })
  }

  const newMembershipExpiresAt = new Date(item.current_period_end * 1000)

  await updateUser(user.id, {
    membershipPlan: plan.code,
    membershipExpiresAt:
      user.membershipExpiresAt && user.membershipExpiresAt > newMembershipExpiresAt
        ? user.membershipExpiresAt
        : newMembershipExpiresAt,
    storageLimit: plan.limits.storage,
    aiBalance: plan.limits.ai,
    updatedAt: new Date(),
  })

  console.log(`Updated user ${user.id} with plan ${plan.code} and expires at ${newMembershipExpiresAt}`)
}
```

## File: `app/docs/layout.tsx`
```tsx
export default async function DocsLayout({ children }: { children: React.ReactNode }) {
  return <div className="mx-auto max-w-screen-md px-4 py-16">{children}</div>
}
```

## File: `app/docs/ai/page.tsx`
```tsx
import config from "@/lib/config"

export default async function AI() {
  return (
    <div className="prose prose-slate max-w-none">
      <h1 className="text-3xl font-bold tracking-tight text-gray-900 mb-6">AI Use Disclosure</h1>

      <p className="bg-slate-50 p-4 rounded-lg border border-slate-200 mb-6">
        <strong className="text-slate-700">Effective Date</strong>: April 22, 2025
        <br />
        <strong className="text-slate-700">Contact Email</strong>:{" "}
        <a href={`mailto:${config.app.supportEmail}`} className="text-blue-600 hover:text-blue-800">
          {config.app.supportEmail}
        </a>
        <br />
        <strong className="text-slate-700">Domain</strong>:{" "}
        <a href="https://taxhacker.app" className="text-blue-600 hover:text-blue-800">
          https://taxhacker.app
        </a>
      </p>

      <p className="text-gray-700 leading-relaxed mb-6">
        At TaxHacker, we use artificial intelligence (&quot;AI&quot;) to power the core features of our platform. This
        document outlines how and why we use AI technologies, what data is processed, and how it may affect you as a
        user.
      </p>

      <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">1. Purpose of AI in TaxHacker</h2>
      <p className="text-gray-700 leading-relaxed mb-3">AI is essential to the TaxHacker experience. It is used for:</p>
      <ul className="list-disc pl-6 space-y-2 mb-6 text-gray-700">
        <li>Optical Character Recognition (OCR) of scanned invoices and receipts</li>
        <li>Automatic categorization and tagging of financial transactions</li>
        <li>Summarization of expenses and vendor descriptions</li>
        <li>Smart field population and autofill within forms</li>
        <li>Custom prompt-driven workflows</li>
      </ul>
      <p className="text-gray-700 leading-relaxed mb-6">
        All AI-generated content is visible directly in the user interface and may be applied to your transactions,
        projects, and reports.
      </p>

      <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">2. AI Providers and Models</h2>
      <p className="text-gray-700 leading-relaxed mb-3">
        Our cloud-hosted version uses models provided by <strong>OpenAI</strong>, including:
      </p>
      <ul className="list-disc pl-6 space-y-2 mb-6 text-gray-700">
        <li>
          <strong>gpt-4o-mini</strong> and <strong>gpt-4.1-mini</strong>
        </li>
      </ul>
      <p className="text-gray-700 leading-relaxed mb-6">
        In the <strong>self-hosted version</strong>, users may choose to connect their own language models or AI
        backends. We do not monitor or vet these setups and assume no responsibility for their output.
      </p>

      <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">3. Data Sent for AI Processing</h2>
      <p className="text-gray-700 leading-relaxed mb-3">
        To deliver AI-powered features, we send selected user data to OpenAI&apos;s API, including:
      </p>
      <ul className="list-disc pl-6 space-y-2 mb-6 text-gray-700">
        <li>Uploaded documents (e.g., receipts, invoices)</li>
        <li>Associated transaction metadata and user-provided fields</li>
        <li>Historical context of past transactions (if required for analysis)</li>
      </ul>
      <p className="bg-amber-50 p-4 rounded-lg border border-amber-200 mb-4">
        <strong className="text-amber-600">⚠️ Note:</strong> This data is <strong>not anonymized or redacted</strong>{" "}
        before transmission. By using TaxHacker, you acknowledge and consent to this transfer.
      </p>
      <p className="text-gray-700 leading-relaxed mb-6">
        We store <strong>structured outputs</strong> from the AI (e.g., parsed fields, categorization) in your account
        for future use. We do <strong>not</strong> store raw AI prompts or responses beyond what's necessary to populate
        your data.
      </p>

      <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">4. Human Involvement</h2>
      <p className="text-gray-700 leading-relaxed mb-4">
        We do <strong>not</strong> manually review AI-generated content. There is currently no mechanism for human
        review, error flagging, or corrections.
      </p>
      <p className="text-gray-700 leading-relaxed mb-6">
        Users are solely responsible for verifying the accuracy of AI-processed outputs before using them for financial
        or reporting purposes.
      </p>

      <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">5. Opt-Out and Core Dependency</h2>
      <p className="text-gray-700 leading-relaxed mb-6">
        AI processing is a fundamental component of TaxHacker and cannot be disabled. If you do not consent to your data
        being processed via AI, you should not use the platform.
      </p>

      <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">6. Automated Decision-Making</h2>
      <p className="text-gray-700 leading-relaxed mb-4">
        Our AI systems do not make binding legal or financial decisions on your behalf. However, they may suggest
        categories, values, or summaries based on the data you provide.
      </p>
      <p className="text-gray-700 leading-relaxed mb-6">
        While these outputs may influence how your data is structured or interpreted, they are{" "}
        <strong>not used to make automated decisions with legal or significant effects</strong> as defined under GDPR
        Article 22.
      </p>

      <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">7. Risks and Limitations</h2>
      <p className="text-gray-700 leading-relaxed mb-4">
        AI-generated outputs are probabilistic and may contain errors, omissions, or misinterpretations. We make{" "}
        <strong>no guarantees of accuracy</strong>, completeness, or suitability for tax, legal, or financial purposes.
      </p>
      <p className="bg-red-50 p-4 rounded-lg border border-red-200 mb-6">
        <strong className="text-red-600">⚠️ Important:</strong> TaxHacker is <strong>not a substitute</strong> for a
        certified accountant, tax advisor, or legal counsel. Use at your own risk.
      </p>
    </div>
  )
}
```

## File: `app/docs/cookie/page.tsx`
```tsx
import config from "@/lib/config"

export default async function Cookie() {
  return (
    <div className="prose prose-slate max-w-none">
      <h1 className="text-3xl font-bold mb-6 text-slate-900 border-b pb-2">Cookie Policy</h1>
      <p className="bg-slate-50 p-4 rounded-lg border border-slate-200 mb-6">
        <strong className="text-slate-700">Effective Date:</strong> April 22, 2025
        <br />
        <strong className="text-slate-700">Service:</strong>{" "}
        <a href="https://taxhacker.app" className="text-blue-600 hover:text-blue-800">
          https://taxhacker.app
        </a>
        <br />
        <strong className="text-slate-700">Contact:</strong>{" "}
        <a href={`mailto:${config.app.supportEmail}`} className="text-blue-600 hover:text-blue-800">
          {config.app.supportEmail}
        </a>
      </p>

      <p className="text-slate-700 mb-6 leading-relaxed">
        This Cookie Policy explains how TaxHacker uses cookies and similar technologies when you visit our website or
        use our services.
      </p>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">1. What Are Cookies?</h2>
      <p className="text-slate-700 mb-6 leading-relaxed">
        Cookies are small text files stored on your device by your browser when you visit websites. They are widely used
        to make websites work more efficiently and to provide information to site owners.
      </p>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">2. How We Use Cookies</h2>
      <p className="text-slate-700 mb-3">
        We use cookies <strong className="text-slate-800">strictly for essential purposes</strong>, including:
      </p>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          Maintaining user <strong className="text-slate-800">sessions and authentication</strong>
        </li>
        <li>
          Enabling <strong className="text-slate-800">caching and performance improvements</strong>
        </li>
        <li>
          Ensuring <strong className="text-slate-800">security</strong>, including DDoS and bot protection through
          Cloudflare
        </li>
      </ul>
      <p className="text-slate-700 mb-3">
        We do <strong className="text-slate-800">not</strong> use cookies for:
      </p>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>Advertising or behavioral tracking</li>
        <li>Analytics or profiling</li>
        <li>Third-party ad services</li>
      </ul>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">3. Third-Party Infrastructure</h2>
      <p className="text-slate-700 mb-6 leading-relaxed">
        We rely on a limited number of third-party services that may set their own cookies or use related technologies:
      </p>

      <div className="overflow-x-auto mb-6">
        <table className="min-w-full border-collapse border border-slate-200 rounded-lg">
          <thead className="bg-slate-50">
            <tr>
              <th className="border border-slate-200 px-6 py-3 text-left text-sm font-semibold text-slate-700">
                Provider
              </th>
              <th className="border border-slate-200 px-6 py-3 text-left text-sm font-semibold text-slate-700">
                Purpose
              </th>
              <th className="border border-slate-200 px-6 py-3 text-left text-sm font-semibold text-slate-700">
                Cookie Usage
              </th>
            </tr>
          </thead>
          <tbody>
            <tr className="bg-white">
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">
                <strong className="text-slate-800">Cloudflare</strong>
              </td>
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">
                CDN, caching, security, bot protection
              </td>
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">Yes (essential)</td>
            </tr>
            <tr className="bg-slate-50">
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">
                <strong className="text-slate-800">Stripe</strong>
              </td>
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">
                Payment processing (subscriptions, billing)
              </td>
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">Yes (essential)</td>
            </tr>
            <tr className="bg-white">
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">
                <strong className="text-slate-800">GitHub</strong>
              </td>
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">
                Embedded resources or OAuth (if used)
              </td>
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">Possibly, if embedded</td>
            </tr>
            <tr className="bg-slate-50">
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">
                <strong className="text-slate-800">Sentry</strong>
              </td>
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">Application error monitoring</td>
              <td className="border border-slate-200 px-6 py-4 text-sm text-slate-700">
                No cookies, but may collect browser metadata
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">4. Your Cookie Choices</h2>
      <p className="text-slate-700 mb-4 leading-relaxed">
        We do not currently display a cookie banner because we only use cookies that are strictly necessary for the
        operation of the website.
      </p>
      <p className="text-slate-700 mb-6 leading-relaxed">
        If you prefer, you can block or delete cookies via your browser settings. However, doing so may affect the core
        functionality of the site, including login and session persistence.
      </p>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">5. Updates to This Policy</h2>
      <p className="text-slate-700 mb-6 leading-relaxed">
        We may update this Cookie Policy from time to time. The latest version will always be available on this page,
        with the "Effective Date" updated accordingly.
      </p>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">6. Contact</h2>
      <p className="text-slate-700 mb-6 leading-relaxed">
        For questions about our cookie usage, please contact us at{" "}
        <a href={`mailto:${config.app.supportEmail}`} className="text-blue-600 hover:text-blue-800">
          {config.app.supportEmail}
        </a>
        .
      </p>
    </div>
  )
}
```

## File: `app/docs/privacy_policy/page.tsx`
```tsx
import config from "@/lib/config"

export default async function PrivacyPolicy() {
  return (
    <div className="prose prose-slate max-w-none">
      <h2 className="text-3xl font-bold mb-6 text-slate-900 border-b pb-2">
        <strong>Privacy Policy</strong>
      </h2>

      <p className="text-slate-700 mb-6 leading-relaxed bg-yellow-50 p-3 border-l-4 border-yellow-400">
        <strong className="text-slate-800">TL;DR:</strong> If you really care about privacy of your data, use our
        self-hosted version instead. No cloud is safe. Use the platform is at your own risk.
      </p>

      <p className="bg-slate-50 p-4 rounded-lg border border-slate-200 mb-6">
        <strong className="text-slate-700">Effective Date</strong>: April 22, 2025
        <br />
        <strong className="text-slate-700">Contact Email</strong>:{" "}
        <a href={`mailto:${config.app.supportEmail}`} className="text-blue-600 hover:text-blue-800">
          {config.app.supportEmail}
        </a>
        <br />
        <strong className="text-slate-700">Domain</strong>:{" "}
        <a href="https://taxhacker.app" className="text-blue-600 hover:text-blue-800">
          https://taxhacker.app
        </a>
      </p>

      <p className="text-slate-700 mb-6 leading-relaxed">
        TaxHacker (&quot;we&quot;, &quot;our&quot;, &quot;us&quot;) is committed to protecting your privacy. This
        Privacy Policy describes how we collect, use, store, and protect your personal data when you use our services at{" "}
        <a href="https://taxhacker.app" className="text-blue-600 hover:text-blue-800">
          taxhacker.app
        </a>
        .
      </p>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        1. <strong>What Data We Collect</strong>
      </h3>
      <p className="text-slate-700 mb-3">We collect the following types of data when you use TaxHacker:</p>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          <strong className="text-slate-800">Account Data</strong>: Email address, display name, optional avatar image.
          No passwords are stored.
        </li>
        <li>
          <strong className="text-slate-800">Communication Data</strong>: Email messages we send for verification,
          updates, or newsletters.
        </li>
        <li>
          <strong className="text-slate-800">Uploaded Files</strong>: Invoices, receipts and any other files that you
          upload, which may contain sensitive personal or financial information.
        </li>
        <li>
          <strong className="text-slate-800">Session Metadata</strong>: IP address, browser type, and timestamps for
          session security.
        </li>
        <li>
          <strong className="text-slate-800">Service Usage Data</strong>: Metadata related to your activity within the
          platform (e.g. number of uploaded files, AI tokens usage).
        </li>
      </ul>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        2. <strong>How We Use Your Data</strong>
      </h3>
      <p className="text-slate-700 mb-3">We use your data to:</p>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>Create and manage your TaxHacker account</li>
        <li>Store and analyze your uploaded files</li>
        <li>Improve your financial organization through AI-powered insights</li>
        <li>Communicate with you about your account and service updates</li>
        <li>Comply with legal obligations</li>
      </ul>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        3. <strong>AI-Powered Processing</strong>
      </h3>
      <p className="text-slate-700 mb-3">
        We use external AI services, specifically <strong className="text-slate-800">OpenAI (ChatGPT)</strong>, to:
      </p>
      <ul className="list-disc pl-6 mb-4 space-y-2 text-slate-700">
        <li>Extract and interpret information from invoices using OCR</li>
        <li>Analyze financial data for better user insights</li>
      </ul>

      <p className="text-slate-700 mb-6 leading-relaxed">
        By using TaxHacker, you consent to the transfer of relevant data to these third-party providers for the purpose
        of processing. These providers may operate outside the EU, in compliance with appropriate safeguards under GDPR
        (e.g., SCCs).
      </p>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        4. <strong>Cookies and Tracking</strong>
      </h3>
      <p className="text-slate-700 mb-6 leading-relaxed">
        TaxHacker does <strong className="text-slate-800">not use tracking cookies</strong> or third-party analytics. We
        only collect aggregate access logs and usage statistics via{" "}
        <strong className="text-slate-800">Cloudflare</strong> for infrastructure performance and security.
      </p>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        5. <strong>Data Storage and Security</strong>
      </h3>
      <ul className="list-disc pl-6 mb-4 space-y-2 text-slate-700">
        <li>
          All data is stored on servers in <strong className="text-slate-800">Germany</strong>, hosted by{" "}
          <strong className="text-slate-800">Hetzner Cloud</strong>.
        </li>
        <li>Files and personal data are stored in an unencrypted form.</li>
        <li>Access to personal data is limited to authorized team members for debugging or support purposes only.</li>
      </ul>

      <p className="text-slate-700 mb-6 leading-relaxed bg-yellow-50 p-3 border-l-4 border-yellow-400">
        While we strive to maintain reasonable safeguards, no system is completely secure. Use the platform at your own
        risk.
      </p>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        6. <strong>Legal Basis for Processing</strong>
      </h3>
      <p className="text-slate-700 mb-3">We process personal data based on:</p>
      <ul className="list-disc pl-6 mb-4 space-y-2 text-slate-700">
        <li>
          <strong className="text-slate-800">Your consent</strong>, which you grant when you create an account or upload
          data
        </li>
        <li>
          <strong className="text-slate-800">Our contractual obligations</strong> to provide the services you signed up
          for
        </li>
      </ul>

      <p className="text-slate-700 mb-6 leading-relaxed">
        You can withdraw consent at any time by deleting your account or contacting us directly.
      </p>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        7. <strong>Data Retention</strong>
      </h3>
      <p className="text-slate-700 mb-3">We retain your data:</p>
      <ul className="list-disc pl-6 mb-4 space-y-2 text-slate-700">
        <li>As long as your account remains active</li>
        <li>Until you request deletion</li>
      </ul>

      <p className="text-slate-700 mb-6 leading-relaxed">
        Once deleted, your data is removed from our systems, though some residual logs may remain for a short time due
        to backups or operational needs.
      </p>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        8. <strong>Your Rights (under GDPR and similar laws)</strong>
      </h3>
      <p className="text-slate-700 mb-3">As a user, you have the right to:</p>
      <ul className="list-disc pl-6 mb-4 space-y-2 text-slate-700">
        <li>Access and review your personal data</li>
        <li>Correct or update inaccurate information</li>
        <li>Download a full backup of your data</li>
        <li>Request permanent deletion of your account and associated data</li>
        <li>Object to certain forms of processing</li>
        <li>Lodge a complaint with a data protection authority</li>
      </ul>

      <p className="text-slate-700 mb-6 leading-relaxed">
        To exercise your rights, contact us at{" "}
        <a href={`mailto:${config.app.supportEmail}`} className="text-blue-600 hover:text-blue-800">
          {config.app.supportEmail}
        </a>
        .
      </p>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        9. <strong>Children's Privacy</strong>
      </h3>
      <p className="text-slate-700 mb-6 leading-relaxed">
        TaxHacker is <strong className="text-slate-800">not intended for users under the age of 18</strong>. We do not
        knowingly collect or store data from minors.
      </p>

      <hr className="my-8 border-slate-200" />

      <h3 className="text-2xl font-semibold text-slate-800 mb-4">
        10. <strong>Changes to This Policy</strong>
      </h3>
      <p className="text-slate-700 mb-6 leading-relaxed">
        We may update this Privacy Policy from time to time. Any changes will be published on this page with an updated
        &quot;Effective Date.&quot; We encourage you to review the policy periodically.
      </p>
    </div>
  )
}
```

## File: `app/docs/terms/page.tsx`
```tsx
import config from "@/lib/config"

export default async function Terms() {
  return (
    <div className="prose prose-slate max-w-none">
      <h1 className="text-3xl font-bold mb-6 text-slate-900 border-b pb-2">Terms of Service</h1>
      <p className="bg-slate-50 p-4 rounded-lg border border-slate-200 mb-6">
        <strong className="text-slate-700">Effective Date:</strong> April 22, 2025
        <br />
        <strong className="text-slate-700">Service:</strong>{" "}
        <a href="https://taxhacker.app" className="text-blue-600 hover:text-blue-800">
          https://taxhacker.app
        </a>
        <br />
        <strong className="text-slate-700">Contact:</strong>{" "}
        <a href={`mailto:${config.app.supportEmail}`} className="text-blue-600 hover:text-blue-800">
          {config.app.supportEmail}
        </a>
      </p>

      <p className="text-slate-700 mb-6 leading-relaxed">
        These Terms of Service (&quot;Terms&quot;) govern your access to and use of TaxHacker, an automated invoice
        analyzer and expense tracker powered by artificial intelligence (AI). By accessing or using our services, you
        agree to be bound by these Terms.
      </p>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">1. Service Overview</h2>
      <p className="text-slate-700 mb-3">TaxHacker offers:</p>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          A <strong className="text-slate-800">cloud-based platform</strong> with paid subscription tiers
          (monthly/yearly)
        </li>
        <li>
          A <strong className="text-slate-800">self-hosted version</strong> available for free with no support
          guarantees
        </li>
      </ul>
      <p className="text-slate-700 mb-6 leading-relaxed">
        Users can upload invoices and receipts, analyze transactions, and manage expenses via AI-powered tools. The
        service is primarily designed for freelancers and small businesses.
      </p>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">2. Eligibility and Account Use</h2>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          You must be at least <strong className="text-slate-800">18 years old</strong> to use TaxHacker.
        </li>
        <li>
          You may register and maintain <strong className="text-slate-800">multiple accounts</strong>.
        </li>
        <li>
          You are responsible for maintaining the confidentiality of access credentials and for all activities under
          your account.
        </li>
      </ul>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">3. Subscriptions & Payments</h2>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          Paid plans are managed through <strong className="text-slate-800">Stripe</strong>, and all subscriptions{" "}
          <strong className="text-slate-800">renew automatically</strong> unless cancelled.
        </li>
        <li>You may cancel your subscription or delete your account at any time via your dashboard.</li>
        <li>
          We offer a <strong className="text-slate-800">no-questions-asked refund policy</strong>, but reserve the right
          to <strong className="text-slate-800">deduct costs</strong> for AI usage (e.g., token consumption) and
          third-party service charges already incurred.
        </li>
      </ul>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">4. User Responsibilities</h2>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          You may upload any invoice or receipt <strong className="text-slate-800">at your discretion</strong>, but{" "}
          <strong className="text-slate-800">you are solely responsible</strong> for the content you upload.
        </li>
        <li>
          <strong className="text-slate-800">Illegal, fraudulent, or copyrighted material</strong> without permission is
          strictly prohibited. Violations may lead to immediate account suspension or termination.
        </li>
        <li>
          You{" "}
          <strong className="text-slate-800">may not redistribute, resell, or offer our AI analysis or services</strong>{" "}
          to third parties without our written consent.
        </li>
      </ul>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">5. AI Usage and Third-Party Integrations</h2>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          TaxHacker uses <strong className="text-slate-800">OpenAI (ChatGPT)</strong> and other third-party APIs to
          process and analyze documents.
        </li>
        <li>
          By using the service, you grant us permission to process your data through these providers under appropriate
          GDPR safeguards.
        </li>
        <li>
          We may allow community-developed <strong className="text-slate-800">plugins and integrations</strong> for
          extended functionality.
        </li>
      </ul>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">6. Intellectual Property</h2>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          You retain <strong className="text-slate-800">full ownership</strong> of your uploaded content and all
          resulting analysis.
        </li>
        <li>
          TaxHacker does <strong className="text-slate-800">not claim any rights</strong> over your data.
        </li>
        <li>
          You are free to <strong className="text-slate-800">reuse, download, publish, or export</strong> any data
          processed by the service.
        </li>
      </ul>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">7. Limitations of Liability</h2>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          TaxHacker is provided <strong className="text-slate-800">&quot;as is&quot;</strong>, without warranties of any
          kind.
        </li>
        <li>
          We make <strong className="text-slate-800">no guarantees</strong> about the accuracy of AI-generated outputs
          or the suitability of our services for accounting, tax filing, or compliance purposes.
        </li>
        <li className="bg-yellow-50 p-3 border-l-4 border-yellow-400">
          <strong className="text-slate-800">⚠️ Important:</strong> TaxHacker is{" "}
          <strong className="text-slate-800">not a substitute</strong> for professional tax or legal advice. You use the
          service <strong className="text-slate-800">at your own risk</strong>.
        </li>
      </ul>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">8. Service Modifications and Termination</h2>
      <ul className="list-disc pl-6 mb-6 space-y-2 text-slate-700">
        <li>
          We reserve the right to <strong className="text-slate-800">modify or discontinue</strong> the service at any
          time, with or without notice.
        </li>
        <li>We may suspend or terminate your account if you violate these Terms or abuse the service.</li>
      </ul>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">9. Governing Law and Dispute Resolution</h2>
      <p className="text-slate-700 mb-6 leading-relaxed">
        These Terms are governed by the laws of <strong className="text-slate-800">Germany</strong>.<br />
        Any disputes shall be resolved exclusively in the courts located in{" "}
        <strong className="text-slate-800">Germany</strong>, unless otherwise required by applicable law.
      </p>

      <h2 className="text-2xl font-semibold text-slate-800 mb-4">10. Changes to These Terms</h2>
      <p className="text-slate-700 mb-6 leading-relaxed">
        We may revise these Terms at any time. If we make material changes, we'll notify users via email or in-app
        notification. Continued use after changes constitutes acceptance of the new Terms.
      </p>
    </div>
  )
}
```

## File: `app/landing/actions.ts`
```typescript
"use server"

import config from "@/lib/config"
import { resend, sendNewsletterWelcomeEmail } from "@/lib/email"

export async function subscribeToNewsletterAction(email: string) {
  try {
    if (!email || !email.includes("@")) {
      return { success: false, error: "Invalid email address" }
    }

    const existingContacts = await resend.contacts.list({
      audienceId: config.email.audienceId,
    })

    if (existingContacts.data) {
      const existingContact = existingContacts.data.data.find((contact: { email: string }) => contact.email === email)

      if (existingContact) {
        return { success: false, error: "You are already subscribed to the newsletter" }
      }
    }

    await resend.contacts.create({
      email,
      audienceId: config.email.audienceId,
      unsubscribed: false,
    })

    await sendNewsletterWelcomeEmail(email)

    return { success: true }
  } catch (error) {
    console.error("Newsletter subscription error:", error)
    return { error: "Failed to subscribe. Please try again later." }
  }
}
```

## File: `app/landing/landing.tsx`
```tsx
import { ColoredText } from "@/components/ui/colored-text"
import config from "@/lib/config"
import Image from "next/image"
import Link from "next/link"

export default function LandingPage() {
  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-br from-pink-50 via-purple-50 to-indigo-50">
      <header className="py-6 px-4 md:px-8 bg-white/90 backdrop-blur-xl shadow-lg border-b border-gradient-to-r from-pink-200 to-indigo-200 fixed w-full z-50">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <Link href="/" className="flex items-center gap-2 group">
            <div className="relative">
              <Image
                src="/logo/256.png"
                alt="Logo"
                width={32}
                height={32}
                className="h-8 group-hover:scale-110 transition-transform duration-300"
              />
              <div className="absolute inset-0 bg-gradient-to-r from-pink-600 to-indigo-600 rounded-full opacity-20 blur-md group-hover:opacity-40 transition-opacity duration-300" />
            </div>
            <ColoredText className="text-2xl font-bold">TaxHacker</ColoredText>
          </Link>
          <Link
            href="/enter"
            className="cursor-pointer font-medium px-4 py-2 rounded-full border-2 border-gradient-to-r from-pink-300 to-indigo-300 hover:from-pink-400 hover:to-indigo-400 bg-white/80 hover:bg-white transition-all duration-300 hover:scale-105 text-xs md:text-sm"
          >
            Log In
          </Link>
        </div>
      </header>

      {/* Hero Section */}
      <section className="pt-32 pb-16 px-8 relative overflow-hidden">
        {/* Background decoration */}
        <div className="absolute inset-0 bg-gradient-to-br from-pink-100/50 via-purple-100/30 to-indigo-100/50" />
        <div className="absolute top-20 left-10 w-72 h-72 bg-gradient-to-r from-pink-400 to-indigo-400 rounded-full opacity-10 blur-3xl animate-pulse" />
        <div className="absolute bottom-20 right-10 w-96 h-96 bg-gradient-to-r from-indigo-400 to-pink-400 rounded-full opacity-10 blur-3xl animate-pulse" />

        <div className="max-w-7xl mx-auto relative z-10">
          <div className="text-center mb-12">
            <div className="inline-block px-6 py-3 rounded-full border-2 border-pink-600/50 text-sm font-medium mb-6 shadow-lg hover:shadow-xl transition-all duration-300">
              🚀 Under Active Development
            </div>
            <h1 className="text-5xl font-bold tracking-tight sm:text-6xl mb-6 bg-gradient-to-r from-gray-900 via-pink-700 to-indigo-700 bg-clip-text text-transparent pb-2">
              Let AI finally care about your taxes, scan your receipts and analyze your expenses
            </h1>
            <p className="text-xl text-gray-700 mb-8 max-w-2xl mx-auto font-medium">
              Self-hosted accounting app crafted for freelancers, indie-hackers and small businesses
            </p>
            <div className="flex gap-4 justify-center text-sm md:text-lg">
              <Link
                href="#start"
                className="px-8 py-4 bg-gradient-to-r from-pink-600 to-indigo-600 text-white font-bold rounded-full hover:from-pink-700 hover:to-indigo-700 transition-all duration-300 shadow-xl hover:shadow-2xl hover:scale-110 border-2 border-white/20"
              >
                Get Started ✨
              </Link>
              <Link
                href="mailto:me@vas3k.com"
                className="px-8 py-4 border-2 border-gradient-to-r from-pink-300 to-indigo-300 text-gray-800 font-bold rounded-full hover:bg-gradient-to-r hover:from-pink-50 hover:to-indigo-50 transition-all duration-300 hover:scale-105 bg-white/80"
              >
                Contact Us 💌
              </Link>
            </div>
          </div>
          <div className="relative aspect-auto rounded-3xl overflow-hidden shadow-2xl ring-4 ring-gradient-to-r from-pink-200 to-indigo-200">
            <div className="absolute inset-0 bg-gradient-to-b from-pink-500/5 via-purple-500/5 to-indigo-500/10 z-10" />
            <video className="w-full h-auto" autoPlay loop muted playsInline poster="/landing/ai-scanner-big.webp">
              <source src="/landing/video.mp4" type="video/mp4" />
              <Image src="/landing/ai-scanner-big.webp" alt="TaxHacker" width={1728} height={1080} priority />
            </video>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 px-8 relative">
        <div className="absolute inset-0 bg-gradient-to-b from-white/50 to-indigo-50/50" />
        <div className="max-w-7xl mx-auto relative z-10">
          <div className="text-center mb-16">
            <h2 className="flex flex-col gap-3 mb-4">
              <span className="text-6xl font-bold bg-gradient-to-r from-pink-600 to-indigo-600 bg-clip-text text-transparent">
                F∗ck Taxes
              </span>
              <span className="text-4xl font-bold bg-gradient-to-r from-gray-900 to-gray-600 bg-clip-text text-transparent">
                TaxHacker saves you time, money and nerves
              </span>
            </h2>
          </div>

          {/* AI Scanner Feature */}
          <div className="flex flex-wrap items-center gap-12 mb-20 bg-gradient-to-br from-white via-pink-50/30 to-indigo-50/30 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-pink-200 to-indigo-200 hover:shadow-2xl transition-all duration-500 group">
            <div className="flex-1 min-w-60">
              <div className="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-blue-500 to-indigo-600 text-white text-sm font-bold mb-4 shadow-lg">
                🤖 LLM-Powered
              </div>
              <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-blue-700 to-indigo-700 bg-clip-text text-transparent">
                Analyze photos and invoices with AI
              </h3>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-blue-600 mr-3 text-lg">✨</span>
                  Upload your receipts or invoices in PDF for automatic recognition
                </li>
                <li className="flex items-center">
                  <span className="text-blue-600 mr-3 text-lg">✨</span>
                  Extract key information like dates, items, and vendors
                </li>
                <li className="flex items-center">
                  <span className="text-blue-600 mr-3 text-lg">✨</span>
                  Works with any language and any photo quality
                </li>
                <li className="flex items-center">
                  <span className="text-blue-600 mr-3 text-lg">✨</span>
                  Automatically organize everything into a structured database
                </li>
                <li className="flex items-center">
                  <span className="text-blue-600 mr-3 text-lg">✨</span>
                  Bulk upload and analyze multiple files at once
                </li>
              </ul>
            </div>
            <div className="flex-1 relative aspect-auto rounded-3xl overflow-hidden shadow-2xl ring-4 ring-gradient-to-r from-blue-200 to-indigo-200 hover:scale-105 transition-all duration-500">
              <Image src="/landing/ai-scanner.webp" alt="AI Document Analyzer" width={1900} height={1524} />
            </div>
          </div>

          {/* Multi-currency Feature */}
          <div className="flex flex-wrap items-center gap-12 mb-20 bg-gradient-to-br from-white via-green-50/30 to-emerald-50/30 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-green-200 to-emerald-200 hover:shadow-2xl transition-all duration-500 group flex-row-reverse">
            <div className="flex-1 min-w-60">
              <div className="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-green-500 to-emerald-600 text-white text-sm font-bold mb-4 shadow-lg">
                💱 Currency Converter
              </div>
              <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-green-700 to-emerald-700 bg-clip-text text-transparent">
                Automatically convert currencies (even crypto!)
              </h3>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-green-600 mr-3 text-lg">💰</span>
                  Detects foreign currencies and converts it to yours
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-3 text-lg">💰</span>
                  Knows historical exchange rates on a date of transaction
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-3 text-lg">💰</span>
                  Supports 170+ world currencies
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-3 text-lg">💰</span>
                  Works with popular cryptocurrencies (BTC, ETH, LTC, etc.)
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-3 text-lg">💰</span>
                  Still allows you to fill it manually
                </li>
              </ul>
            </div>
            <div className="flex-1 relative aspect-auto rounded-3xl overflow-hidden shadow-2xl ring-4 ring-gradient-to-r from-green-200 to-emerald-200 hover:scale-105 transition-all duration-500">
              <Image src="/landing/multi-currency.webp" alt="Currency Converter" width={1400} height={1005} />
            </div>
          </div>

          {/* Transaction Table Feature */}
          <div className="flex flex-wrap items-center gap-12 mb-20 bg-gradient-to-br from-white via-pink-50/30 to-rose-50/30 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-pink-200 to-rose-200 hover:shadow-2xl transition-all duration-500 group flex-row-reverse">
            <div className="flex-1 relative aspect-auto rounded-3xl overflow-hidden shadow-2xl ring-4 ring-gradient-to-r from-pink-200 to-rose-200 hover:scale-105 transition-all duration-500">
              <Image src="/landing/transactions.webp" alt="Transactions Table" width={2000} height={1279} />
            </div>
            <div className="flex-1  min-w-60">
              <div className="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-pink-500 to-rose-600 text-white text-sm font-bold mb-4 shadow-lg">
                🔍 Filters & Categories
              </div>
              <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-pink-700 to-rose-700 bg-clip-text text-transparent">
                Organize your transactions using fully customizable categories, projects and fields
              </h3>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-pink-600 mr-3 text-lg">📊</span>
                  Absolute freedom to create custom categories, projects and fields
                </li>
                <li className="flex items-center">
                  <span className="text-pink-600 mr-3 text-lg">📊</span>
                  Add, edit and manage your transactions
                </li>
                <li className="flex items-center">
                  <span className="text-pink-600 mr-3 text-lg">📊</span>
                  Filter by any column, category or date range
                </li>
                <li className="flex items-center">
                  <span className="text-pink-600 mr-3 text-lg">📊</span>
                  Customize which columns to show in the table
                </li>
                <li className="flex items-center">
                  <span className="text-pink-600 mr-3 text-lg">📊</span>
                  Import transactions from CSV
                </li>
              </ul>
            </div>
          </div>

          {/* Invoice Generator */}
          <div className="flex flex-wrap items-center gap-12 mb-20 bg-gradient-to-br from-white via-purple-50/30 to-indigo-50/30 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-purple-200 to-indigo-200 hover:shadow-2xl transition-all duration-500 group">
            <div className="max-w-sm flex-1 relative aspect-auto rounded-3xl overflow-hidden shadow-2xl ring-4 ring-gradient-to-r from-purple-200 to-indigo-200 hover:scale-105 transition-all duration-500">
              <Image src="/landing/invoice-generator.webp" alt="Invoice Generator" width={1800} height={1081} />
            </div>
            <div className="flex-1 min-w-60">
              <div className="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-purple-500 to-indigo-600 text-white text-sm font-bold mb-4 shadow-lg">
                📋 Invoice Generator
              </div>
              <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-purple-700 to-indigo-700 bg-clip-text text-transparent">
                Create custom invoices
              </h3>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">📄</span>
                  Advanced invoice generator to create any invoice in any language
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">📄</span>
                  Edit any field, even labels and titles
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">📄</span>
                  Export invoices to PDF or as transactions
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">📄</span>
                  Save invoices as templates to reuse them later
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">📄</span>
                  Native support for both included and excluded taxes (VAT, GST, etc.)
                </li>
              </ul>
            </div>
          </div>

          {/* Custom Fields & Categories */}
          <div className="flex flex-wrap items-center gap-12 mb-20 bg-gradient-to-br from-white via-violet-50/30 to-purple-50/30 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-violet-200 to-purple-200 hover:shadow-2xl transition-all duration-500 group">
            <div className="flex-1 min-w-60">
              <div className="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-violet-500 to-purple-600 text-white text-sm font-bold mb-4 shadow-lg">
                🎨 Control over AI
              </div>
              <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-violet-700 to-purple-700 bg-clip-text text-transparent">
                Tune any LLM prompt to extract anything you need
              </h3>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-violet-600 mr-3 text-lg">🔧</span>
                  Expand and improve your TaxHacker instance with custom LLM prompts
                </li>
                <li className="flex items-center">
                  <span className="text-violet-600 mr-3 text-lg">🔧</span>
                  Create custom fields and categories and tell AI how to parse them for you
                </li>
                <li className="flex items-center">
                  <span className="text-violet-600 mr-3 text-lg">🔧</span>
                  Extract any additional information you need
                </li>
                <li className="flex items-center">
                  <span className="text-violet-600 mr-3 text-lg">🔧</span>
                  Automatically categorize by project or category
                </li>
                <li className="flex items-center">
                  <span className="text-violet-600 mr-3 text-lg">🔧</span>
                  Ask AI to assess risk level or any other criteria
                </li>
              </ul>
            </div>
            <div className="flex-1 relative aspect-auto rounded-3xl overflow-hidden shadow-2xl ring-4 ring-gradient-to-r from-violet-200 to-purple-200 hover:scale-105 transition-all duration-500">
              <Image src="/landing/custom-llm.webp" alt="Custom LLM promts" width={1800} height={1081} />
            </div>
          </div>

          {/* Data Export */}
          <div className="flex flex-wrap items-center gap-12 mb-20 bg-gradient-to-br from-white via-orange-50/30 to-amber-50/30 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-orange-200 to-amber-200 hover:shadow-2xl transition-all duration-500 group flex-row-reverse">
            <div className="flex-1 min-w-60">
              <div className="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-orange-500 to-amber-600 text-white text-sm font-bold mb-4 shadow-lg">
                📦 Self-hosting & Data Export
              </div>
              <h3 className="text-2xl font-bold mb-4 bg-gradient-to-r from-orange-700 to-amber-700 bg-clip-text text-transparent">
                Your Data — Your Rules
              </h3>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-orange-600 mr-3 text-lg">📤</span>
                  Deploy your own instance of TaxHacker for 100% privacy
                </li>
                <li className="flex items-center">
                  <span className="text-orange-600 mr-3 text-lg">📤</span>
                  Export your transactions to CSV for tax prep
                </li>
                <li className="flex items-center">
                  <span className="text-orange-600 mr-3 text-lg">📤</span>
                  Full-text search across documents and invoices
                </li>
                <li className="flex items-center">
                  <span className="text-orange-600 mr-3 text-lg">📤</span>
                  Download full data archive to migrate to another service. We don't take away or limit what you do with
                  your data
                </li>
              </ul>
            </div>
            <div className="flex-1 relative aspect-auto rounded-3xl overflow-hidden shadow-2xl ring-4 ring-gradient-to-r from-orange-200 to-amber-200 hover:scale-105 transition-all duration-500">
              <Image src="/landing/export.webp" alt="Export" width={1200} height={1081} />
            </div>
          </div>
        </div>
      </section>

      {/* Deployment Options */}
      <section
        id="start"
        className="py-20 px-8 bg-gradient-to-br from-white via-pink-50/20 to-indigo-50/20 scroll-mt-20 relative"
      >
        <div className="absolute inset-0 bg-gradient-to-r from-pink-100/20 to-indigo-100/20" />
        <div className="max-w-7xl mx-auto relative z-10">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold mb-4 bg-gradient-to-r from-pink-600 to-indigo-600 bg-clip-text text-transparent">
              Choose Your Version of TaxHacker
            </h2>
          </div>
          <div className="grid md:grid-cols-2 gap-16">
            {/* Self-Hosted Version */}
            <div className="bg-gradient-to-br from-white via-violet-50/50 to-indigo-50/50 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-violet-200 to-indigo-200 hover:shadow-2xl transition-all duration-500 group">
              <div className="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-violet-500 to-indigo-600 text-white text-sm font-bold mb-6 shadow-lg">
                🏠 Use Your Own Server
              </div>
              <h3 className="text-2xl font-bold mb-4">
                <ColoredText>Self-Hosted Edition</ColoredText>
              </h3>
              <ul className="space-y-3 text-gray-700 mb-8">
                <li className="flex items-center">
                  <span className="text-indigo-600 mr-3 text-lg">🆓</span>
                  Free and Open Source
                </li>
                <li className="flex items-center">
                  <span className="text-indigo-600 mr-3 text-lg">🔒</span>
                  Complete control over your data
                </li>
                <li className="flex items-center">
                  <span className="text-indigo-600 mr-3 text-lg">🏗️</span>
                  Deploy at your own infrastructure or home server
                </li>
                <li className="flex items-center">
                  <span className="text-indigo-600 mr-3 text-lg">🔑</span>
                  Bring your own keys (OpenAI, Gemini, Mistral, etc.)
                </li>
              </ul>
              <Link
                href="https://github.com/vas3k/TaxHacker"
                target="_blank"
                className="block w-full text-center px-6 py-4 bg-gradient-to-r from-violet-600 to-indigo-600 text-white font-bold rounded-full hover:from-violet-700 hover:to-indigo-700 transition-all duration-300 shadow-xl hover:shadow-2xl hover:scale-110"
              >
                Github + Docker Compose 🐳
              </Link>
            </div>

            {/* Cloud Version */}
            <div className="bg-gradient-to-br from-white via-pink-50/50 to-purple-50/50 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-pink-200 to-purple-200 hover:shadow-2xl transition-all duration-500 group relative">
              <div className="inline-block px-4 py-2 rounded-full bg-gradient-to-r from-pink-500 to-purple-600 text-white text-sm font-bold mb-6 shadow-lg">
                ☁️ We Host It For You
              </div>
              <h3 className="text-2xl font-bold mb-4">
                <ColoredText>Cloud Edition</ColoredText>
              </h3>
              <ul className="space-y-3 text-gray-700 mb-8">
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">🎯</span>
                  SaaS version if you don't want to hassle with own servers and deployments
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">🤖</span>
                  We provide you with AI keys and storage
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">💳</span>
                  Yearly subscription plans. No hidden fees
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">🚀</span>
                  Automatic updates and new features
                </li>
              </ul>
              <button
                type="button"
                disabled
                className="block w-full text-center px-6 py-4 bg-gradient-to-r from-gray-300 to-gray-400 text-gray-700 font-bold rounded-full shadow-xl opacity-80 cursor-not-allowed"
              >
                Temporarily unavailable
              </button>
            </div>
          </div>
        </div>
      </section>

      {/* Upcoming Features */}
      <section className="py-20 px-8 bg-gradient-to-br from-indigo-50 via-purple-50 to-pink-50 mt-28 relative overflow-hidden">
        <div className="absolute top-10 left-10 w-64 h-64 bg-gradient-to-r from-pink-400 to-indigo-400 rounded-full opacity-5 blur-3xl" />
        <div className="absolute bottom-10 right-10 w-80 h-80 bg-gradient-to-r from-indigo-400 to-pink-400 rounded-full opacity-5 blur-3xl" />

        <div className="max-w-7xl mx-auto relative z-10">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold mb-4 bg-gradient-to-r from-pink-600 to-indigo-600 bg-clip-text text-transparent">
              Upcoming Features
            </h2>
            <p className="text-gray-700 max-w-2xl mx-auto font-medium">
              We&apos;re a small, indie project constantly improving. Here&apos;s what we&apos;re working on next.
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-8 mb-16">
            {/* AI Improvements */}
            <div className="bg-gradient-to-br from-white via-purple-50/50 to-indigo-50/50 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-purple-200 to-indigo-200 hover:shadow-2xl transition-all duration-500 hover:scale-105">
              <div className="flex items-center gap-3 mb-4">
                <span className="text-3xl">🤖</span>
                <h3 className="text-xl font-bold bg-gradient-to-r from-purple-700 to-indigo-700 bg-clip-text text-transparent">
                  Better AI Analytics & Agents
                </h3>
              </div>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">🔮</span>
                  Income & expense insights
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">🔮</span>
                  AI agents to automate your workflows
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">🔮</span>
                  Recommendations for tax optimization
                </li>
                <li className="flex items-center">
                  <span className="text-purple-600 mr-3 text-lg">🔮</span>
                  Custom and local LLM models
                </li>
              </ul>
            </div>

            {/* Smart Reports */}
            <div className="bg-gradient-to-br from-white via-pink-50/50 to-rose-50/50 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-pink-200 to-rose-200 hover:shadow-2xl transition-all duration-500 hover:scale-105">
              <div className="flex items-center gap-3 mb-4">
                <span className="text-3xl">📊</span>
                <h3 className="text-xl font-bold bg-gradient-to-r from-pink-700 to-rose-700 bg-clip-text text-transparent">
                  Smart Reports & Reminders
                </h3>
              </div>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-pink-600 mr-3 text-lg">📈</span>
                  Monthly or quarterly VAT reports
                </li>
                <li className="flex items-center">
                  <span className="text-pink-600 mr-3 text-lg">📈</span>
                  Tax reminders
                </li>
                <li className="flex items-center">
                  <span className="text-pink-600 mr-3 text-lg">📈</span>
                  Annual income & expense reports
                </li>
              </ul>
            </div>

            {/* Transaction Review */}
            <div className="bg-gradient-to-br from-white via-green-50/50 to-emerald-50/50 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-green-200 to-emerald-200 hover:shadow-2xl transition-all duration-500 hover:scale-105">
              <div className="flex items-center gap-3 mb-4">
                <span className="text-3xl">📥</span>
                <h3 className="text-xl font-bold bg-gradient-to-r from-green-700 to-emerald-700 bg-clip-text text-transparent">
                  Multiple Transaction Review
                </h3>
              </div>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-green-600 mr-3 text-lg">💳</span>
                  Bank statement analysis
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-3 text-lg">💳</span>
                  Automatic data completeness checks
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-3 text-lg">💳</span>
                  Unpaid invoice tracking
                </li>
              </ul>
            </div>

            {/* Custom Fields */}
            <div className="bg-gradient-to-br from-white via-orange-50/50 to-amber-50/50 p-8 rounded-3xl shadow-xl ring-2 ring-gradient-to-r from-orange-200 to-amber-200 hover:shadow-2xl transition-all duration-500 hover:scale-105">
              <div className="flex items-center gap-3 mb-4">
                <span className="text-3xl">🧩</span>
                <h3 className="text-xl font-bold bg-gradient-to-r from-orange-700 to-amber-700 bg-clip-text text-transparent">
                  Presets and Plugins
                </h3>
              </div>
              <ul className="space-y-3 text-gray-700">
                <li className="flex items-center">
                  <span className="text-orange-600 mr-3 text-lg">🌍</span>
                  Presets for different countries and industries
                </li>
                <li className="flex items-center">
                  <span className="text-orange-600 mr-3 text-lg">🌍</span>
                  Custom reports for various use-cases
                </li>
                <li className="flex items-center">
                  <span className="text-orange-600 mr-3 text-lg">🌍</span>
                  Community plugins and reports
                </li>
              </ul>
            </div>
          </div>

          {/* Stay Tuned / GitHub CTA */}
          <div className="bg-gradient-to-r from-purple-50 to-blue-50 p-8 rounded-2xl shadow-sm ring-1 ring-gray-100">
            <div className="max-w-2xl mx-auto text-center">
              <h3 className="text-2xl font-semibold mb-4">Stay Tuned</h3>
              <p className="text-gray-600 mb-6">
                We&apos;re working hard on making TaxHacker useful for everyone. Star and watch our GitHub repo to get
                notified about new features and releases.
              </p>
              <div className="flex flex-col gap-4 max-w-md mx-auto">
                <div className="flex flex-wrap items-center justify-center gap-4">
                  <a
                    href="https://github.com/vas3k/TaxHacker"
                    target="_blank"
                    rel="noreferrer"
                    className="px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white font-medium rounded-full hover:opacity-90 transition-all shadow-lg shadow-purple-500/20"
                  >
                    Open GitHub repo
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <footer className="py-8 px-8 bg-gradient-to-r from-pink-50 to-indigo-50 border-t-2 border-gradient-to-r from-pink-200 to-indigo-200">
        <div className="max-w-7xl mx-auto text-center text-sm text-gray-600">
          Made with ❤️ in Berlin by{" "}
          <Link
            href="https://github.com/vas3k"
            className="underline font-semibold hover:text-pink-600 transition-colors"
          >
            @vas3k
          </Link>
        </div>

        <section className="py-12 px-8">
          <div className="max-w-7xl mx-auto">
            <div className="flex flex-wrap gap-4 justify-center">
              <Link
                href={`mailto:${config.app.supportEmail}`}
                className="text-sm text-gray-600 hover:text-pink-600 font-medium transition-colors"
              >
                Contact Us
              </Link>
              <Link
                href="/docs/terms"
                className="text-sm text-gray-600 hover:text-pink-600 font-medium transition-colors"
              >
                Terms of Service
              </Link>
              <Link
                href="/docs/privacy_policy"
                className="text-sm text-gray-600 hover:text-pink-600 font-medium transition-colors"
              >
                Privacy Policy
              </Link>
              <Link href="/docs/ai" className="text-sm text-gray-600 hover:text-pink-600 font-medium transition-colors">
                AI Use Disclosure
              </Link>
              <Link
                href="/docs/cookie"
                className="text-sm text-gray-600 hover:text-pink-600 font-medium transition-colors"
              >
                Cookie Policy
              </Link>
              <Link
                href="https://github.com/vas3k/TaxHacker"
                target="_blank"
                className="text-sm text-gray-600 hover:text-pink-600 font-medium transition-colors"
              >
                Source Code
              </Link>
            </div>
          </div>
        </section>
      </footer>
    </div>
  )
}
```

## File: `app/landing/newsletter.tsx`
```tsx
"use client"

import { subscribeToNewsletterAction } from "@/app/landing/actions"
import { useState } from "react"

export function NewsletterForm() {
  const [email, setEmail] = useState("")
  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle")
  const [message, setMessage] = useState("")

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setStatus("loading")
    setMessage("")

    try {
      const result = await subscribeToNewsletterAction(email)

      if (result.error) {
        throw new Error(result.error)
      }

      setStatus("success")
      setMessage("Thanks for subscribing! Check your email for confirmation.")
      setEmail("")
    } catch (error) {
      setStatus("error")
      setMessage(error instanceof Error ? error.message : "Failed to subscribe. Please try again.")
    }
  }

  return (
    <div className="bg-gradient-to-r from-purple-50 to-blue-50 p-8 rounded-2xl shadow-sm ring-1 ring-gray-100">
      <div className="max-w-2xl mx-auto text-center">
        <h3 className="text-2xl font-semibold mb-4">Stay Tuned</h3>
        <p className="text-gray-600 mb-6">
          We&apos;re working hard on making TaxHacker useful for everyone. Subscribe to our emails to get notified about
          our plans and new features. No marketing, ads or spam.
        </p>
        <form onSubmit={handleSubmit} className="flex flex-col gap-4 max-w-md mx-auto">
          <div className="flex flex-wrap items-center justify-center gap-4">
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              className="flex-1 px-4 py-3 rounded-full border border-gray-200 focus:outline-none focus:ring-2 focus:ring-purple-500"
              required
            />
            <button
              type="submit"
              disabled={status === "loading"}
              className="px-6 py-3 bg-gradient-to-r from-purple-600 to-blue-600 text-white font-medium rounded-full hover:opacity-90 transition-all shadow-lg shadow-purple-500/20 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {status === "loading" ? "Subscribing..." : "Subscribe"}
            </button>
          </div>
          {message && (
            <p className={`text-sm ${status === "success" ? "text-green-600" : "text-red-600"}`}>{message}</p>
          )}
        </form>
      </div>
    </div>
  )
}
```

## File: `components/agents/currency-converter.tsx`
```tsx
import { FormError } from "@/components/forms/error"
import { formatCurrency } from "@/lib/utils"
import { format, startOfDay } from "date-fns"
import { Loader2 } from "lucide-react"
import { useEffect, useState } from "react"
import { Button } from "../ui/button"

async function getCurrencyRate(currencyCodeFrom: string, currencyCodeTo: string, date: Date): Promise<number> {
  const formattedDate = format(date, "yyyy-MM-dd")
  const response = await fetch(`/api/currency?from=${currencyCodeFrom}&to=${currencyCodeTo}&date=${formattedDate}`)

  if (!response.ok) {
    const errorData = await response.json()
    console.log("Currency API error:", errorData.error)
    throw new Error(errorData.error || "Failed to fetch currency rate")
  }

  const data = await response.json()
  return data.rate
}

export const CurrencyConverterTool = ({
  originalTotal,
  originalCurrencyCode,
  targetCurrencyCode,
  date,
  onChange,
}: {
  originalTotal: number
  originalCurrencyCode: string
  targetCurrencyCode: string
  date?: Date | undefined
  onChange?: (value: number) => void
}) => {
  const normalizedDate = startOfDay(date || new Date(Date.now() - 24 * 60 * 60 * 1000))
  const normalizedDateString = format(normalizedDate, "yyyy-MM-dd")
  const [exchangeRate, setExchangeRate] = useState(0)
  const [convertedTotal, setConvertedTotal] = useState(0)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const fetchAndUpdateRates = async () => {
    try {
      setIsLoading(true)
      setError(null)

      const rate = await getCurrencyRate(originalCurrencyCode, targetCurrencyCode, normalizedDate)
      setExchangeRate(rate)
      setConvertedTotal(Math.round(originalTotal * rate * 100) / 100)
    } catch (error) {
      console.error("Error fetching currency rates:", error)
      setExchangeRate(0)
      setConvertedTotal(0)
      setError(error instanceof Error ? error.message : "Failed to fetch currency rate")
    } finally {
      setIsLoading(false)
    }
  }

  const handleRestart = () => {
    setError(null)
    fetchAndUpdateRates()
  }

  useEffect(() => {
    fetchAndUpdateRates()
  }, [originalCurrencyCode, targetCurrencyCode, normalizedDateString, originalTotal])

  useEffect(() => {
    onChange?.(convertedTotal)
  }, [convertedTotal])

  if (!originalTotal || !originalCurrencyCode || !targetCurrencyCode || originalCurrencyCode === targetCurrencyCode) {
    return <></>
  }

  return (
    <div className="flex flex-row gap-2 items-center">
      {isLoading ? (
        <div className="flex flex-row items-center gap-2 text-sm text-muted-foreground">
          <Loader2 className="w-4 h-4 animate-spin" />
          <div className="font-semibold">Loading exchange rates...</div>
        </div>
      ) : (
        <div className="flex flex-col gap-2">
          <div className="flex items-center gap-2">
            <div>{formatCurrency(originalTotal * 100, originalCurrencyCode)}</div>
            <div>=</div>
            <div>{formatCurrency(originalTotal * 100 * exchangeRate, targetCurrencyCode).slice(0, 1)}</div>
            <input
              type="number"
              step="0.01"
              name="convertedTotal"
              value={convertedTotal}
              onChange={(e) => {
                const newValue = parseFloat(e.target.value || "0")
                !isNaN(newValue) && setConvertedTotal(Math.round(newValue * 100) / 100)
              }}
              className="w-32 rounded-md border border-input px-2 py-1"
            />
          </div>
          {!error && (
            <div className="text-xs text-muted-foreground">The exchange rate will be added to the transaction</div>
          )}
          {error && (
            <div className="flex flex-row gap-2">
              <FormError className="mt-0 text-sm">{error}</FormError>
              <Button variant="outline" size="sm" className="text-xs" onClick={handleRestart}>
                Retry
              </Button>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
```

## File: `components/agents/items-detect.tsx`
```tsx
import { formatCurrency } from "@/lib/utils"
import { Save, Split } from "lucide-react"
import { Button } from "../ui/button"
import { TransactionData } from "@/models/transactions"
import { splitFileIntoItemsAction } from "@/app/(app)/unsorted/actions"
import { useNotification } from "@/app/(app)/context"
import { useState } from "react"
import { Loader2 } from "lucide-react"
import { File } from "@/prisma/client"

export const ItemsDetectTool = ({ file, data }: { file?: File; data: TransactionData }) => {
  const { showNotification } = useNotification()
  const [isSplitting, setIsSplitting] = useState(false)

  const handleSplit = async () => {
    if (!file) {
      console.error("No file selected")
      return
    }

    setIsSplitting(true)
    try {
      const formData = new FormData()
      formData.append("fileId", file.id)
      formData.append("items", JSON.stringify(data.items))

      const result = await splitFileIntoItemsAction(null, formData)
      if (result.success) {
        showNotification({ code: "global.banner", message: "Split successful!", type: "success" })
        showNotification({ code: "sidebar.unsorted", message: "new" })
        setTimeout(() => showNotification({ code: "sidebar.unsorted", message: "" }), 3000)
      } else {
        showNotification({ code: "global.banner", message: result.error || "Failed to split", type: "failed" })
      }
    } catch (error) {
      console.error("Failed to split items:", error)
      showNotification({ code: "global.banner", message: "Failed to split items", type: "failed" })
    } finally {
      setIsSplitting(false)
    }
  }

  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-col divide-y divide-border">
        {data.items?.map((item, index) => (
          <div
            key={`${item.name || ""}-${item.merchant || ""}-${item.description || ""}-${index}`}
            className="flex flex-row items-start gap-10 py-2 hover:bg-muted/50 transition-colors"
          >
            <div className="flex flex-col flex-1">
              <div className="text-sm">{item.name}</div>
              <div className="text-xs text-muted-foreground">{item.description}</div>
            </div>
            <div className="font-medium">
              {formatCurrency((item.total || 0) * 100, item.currencyCode || data.currencyCode || "USD")}
            </div>
          </div>
        ))}
      </div>

      {file && data.items && data.items.length > 1 && (
        <Button variant="outline" onClick={handleSplit} className="mt-2 px-4 py-2" disabled={isSplitting}>
          {isSplitting ? (
            <>
              <Loader2 className="w-4 h-4 mr-2 animate-spin" />
              Splitting...
            </>
          ) : (
            <>
              <Split className="w-4 h-4 mr-2" />
              Split into {data.items.length} individual transactions
            </>
          )}
        </Button>
      )}
    </div>
  )
}
```

## File: `components/agents/tool-window.tsx`
```tsx
import { Bot } from "lucide-react"

export default function ToolWindow({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="border-2 border-purple-500 bg-purple-100 rounded-md overflow-hidden break-all">
      <div className="flex flex-row gap-1 items-center font-bold text-xs bg-purple-200 text-purple-800 p-1">
        <Bot className="w-4 h-4" />
        <span>{title}</span>
      </div>
      <div className="p-4">{children}</div>
    </div>
  )
}
```

## File: `components/auth/login-form.tsx`
```tsx
"use client"

import { FormError } from "@/components/forms/error"
import { FormInput } from "@/components/forms/simple"
import { Button } from "@/components/ui/button"
import { authClient } from "@/lib/auth-client"
import { useRouter } from "next/navigation"
import { useState } from "react"

export function LoginForm({ defaultEmail }: { defaultEmail?: string }) {
  const [email, setEmail] = useState(defaultEmail || "")
  const [otp, setOtp] = useState("")
  const [isOtpSent, setIsOtpSent] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const router = useRouter()

  const handleSendOtp = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError(null)

    try {
      const result = await authClient.emailOtp.sendVerificationOtp({
        email,
        type: "sign-in",
      })
      if (result.error) {
        setError(result.error.message || "Failed to send the code")
        return
      }
      setIsOtpSent(true)
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to send the code")
    } finally {
      setIsLoading(false)
    }
  }

  const handleVerifyOtp = async (e: React.FormEvent) => {
    e.preventDefault()
    setIsLoading(true)
    setError(null)

    try {
      const result = await authClient.signIn.emailOtp({
        email,
        otp,
      })
      if (result.error) {
        setError("The code is invalid or expired")
        return
      }

      router.push("/dashboard")
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to verify the code")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <form onSubmit={isOtpSent ? handleVerifyOtp : handleSendOtp} className="flex flex-col gap-4 w-full">
      <FormInput
        title="Email"
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
        disabled={isOtpSent}
      />

      {isOtpSent && (
        <FormInput
          title="Check your email for the verification code"
          type="text"
          value={otp}
          onChange={(e) => setOtp(e.target.value)}
          required
          maxLength={6}
          pattern="[0-9]{6}"
        />
      )}

      <Button type="submit" disabled={isLoading}>
        {isLoading ? "Loading..." : isOtpSent ? "Verify Code" : "Enter"}
      </Button>

      {error && <FormError className="text-center">{error}</FormError>}
    </form>
  )
}
```

## File: `components/auth/pricing-card.tsx`
```tsx
"use client"

import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Plan } from "@/lib/stripe"
import { Check, Loader2 } from "lucide-react"
import { useState } from "react"
import { FormError } from "../forms/error"

export function PricingCard({ plan, hideButton = false }: { plan: Plan; hideButton?: boolean }) {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleClick = async () => {
    setIsLoading(true)
    setError(null)
    try {
      const response = await fetch(`/api/stripe/checkout?code=${plan.code}`, {
        method: "POST",
      })
      const data = await response.json()
      if (data.error) {
        setError(data.error)
      } else {
        window.location.href = data.session.url
      }
    } catch (error) {
      setError(error instanceof Error ? error.message : "An unknown error occurred")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <Card className="w-full max-w-xs relative overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-br from-primary/10 to-secondary/10" />
      <CardHeader className="relative">
        <CardTitle className="text-3xl">{plan.name}</CardTitle>
        <CardDescription>{plan.description}</CardDescription>
        {plan.price && <div className="text-2xl font-bold mt-4">{plan.price}</div>}
      </CardHeader>
      <CardContent className="relative">
        <ul className="space-y-2">
          {plan.benefits.map((benefit, index) => (
            <li key={index} className="flex items-center gap-2">
              <Check className="h-4 w-4 text-primary" />
              <span>{benefit}</span>
            </li>
          ))}
        </ul>
      </CardContent>
      <CardFooter className="flex flex-col gap-2 relative">
        {!hideButton && (
          <Button className="w-full" onClick={handleClick} disabled={isLoading}>
            {isLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : "Get Started"}
          </Button>
        )}
        {error && <FormError>{error}</FormError>}
      </CardFooter>
    </Card>
  )
}
```

## File: `components/auth/subscription-expired.tsx`
```tsx
import Link from "next/link"

export function SubscriptionExpired() {
  return (
    <Link
      href="/settings/profile"
      className="w-full h-8 p-1 bg-red-500 text-white font-semibold text-center hover:bg-red-600 transition-colors"
    >
      Your subscription has expired. Click here to select a new plan. Otherwise, your account will be deleted.
    </Link>
  )
}
```

## File: `components/dashboard/drop-zone-widget.tsx`
```tsx
"use client"

import { useNotification } from "@/app/(app)/context"
import { uploadFilesAction } from "@/app/(app)/files/actions"
import { FormError } from "@/components/forms/error"
import config from "@/lib/config"
import { Camera, Loader2 } from "lucide-react"
import { useRouter } from "next/navigation"
import { startTransition, useState } from "react"

export default function DashboardDropZoneWidget() {
  const router = useRouter()
  const { showNotification } = useNotification()
  const [isUploading, setIsUploading] = useState(false)
  const [uploadError, setUploadError] = useState("")

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    setIsUploading(true)
    setUploadError("")
    if (e.target.files && e.target.files.length > 0) {
      const formData = new FormData()

      // Append all selected files to the FormData
      for (let i = 0; i < e.target.files.length; i++) {
        formData.append("files", e.target.files[i])
      }

      // Submit the files using the server action
      startTransition(async () => {
        const result = await uploadFilesAction(formData)
        if (result.success) {
          showNotification({ code: "sidebar.unsorted", message: "new" })
          setTimeout(() => showNotification({ code: "sidebar.unsorted", message: "" }), 3000)
          router.push("/unsorted")
        } else {
          setUploadError(result.error ? result.error : "Something went wrong...")
        }
        setIsUploading(false)
      })
    }
  }

  return (
    <div className="flex w-full h-full">
      <label className="relative w-full h-full border-2 border-dashed rounded-lg transition-colors hover:border-primary cursor-pointer">
        <input
          type="file"
          id="fileInput"
          className="hidden"
          multiple
          accept={config.upload.acceptedMimeTypes}
          onChange={handleFileChange}
        />
        <div className="flex flex-col items-center justify-center gap-4 p-8 text-center h-full">
          {isUploading ? (
            <Loader2 className="h-8 w-8 text-muted-foreground animate-spin" />
          ) : (
            <Camera className="h-8 w-8 text-muted-foreground" />
          )}
          <div>
            <p className="text-lg font-medium">
              {isUploading ? "Uploading..." : "Take a photo or drop your files here"}
            </p>
            {!uploadError && (
              <p className="text-sm text-muted-foreground">
                upload receipts, invoices and any other documents for me to scan
              </p>
            )}
            {uploadError && <FormError>{uploadError}</FormError>}
          </div>
        </div>
      </label>
    </div>
  )
}
```

## File: `components/dashboard/filters-widget.tsx`
```tsx
"use client"

import { DateRangePicker } from "@/components/forms/date-range-picker"
import { useTransactionFilters } from "@/hooks/use-transaction-filters"
import { TransactionFilters } from "@/models/transactions"
import { format } from "date-fns"

export function FiltersWidget({
  defaultFilters,
  defaultRange = "last-12-months",
}: {
  defaultFilters: TransactionFilters
  defaultRange?: string
}) {
  const [filters, setFilters] = useTransactionFilters(defaultFilters)

  return (
    <DateRangePicker
      defaultDate={{
        from: filters?.dateFrom ? new Date(filters.dateFrom) : undefined,
        to: filters?.dateTo ? new Date(filters.dateTo) : undefined,
      }}
      defaultRange={defaultRange}
      onChange={(date) => {
        setFilters({
          dateFrom: date && date.from ? format(date.from, "yyyy-MM-dd") : undefined,
          dateTo: date && date.to ? format(date.to, "yyyy-MM-dd") : undefined,
        })
      }}
    />
  )
}
```

## File: `components/dashboard/income-expense-graph-tooltip.tsx`
```tsx
import { formatCurrency, formatPeriodLabel } from "@/lib/utils"
import { DetailedTimeSeriesData } from "@/models/stats"

interface ChartTooltipProps {
  data: DetailedTimeSeriesData | null
  defaultCurrency: string
  position: { x: number; y: number }
  visible: boolean
  containerWidth?: number
}

export function IncomeExpenceGraphTooltip({ data, defaultCurrency, position, visible }: ChartTooltipProps) {
  if (!visible || !data) {
    return null
  }

  const incomeCategories = data.categories.filter((cat) => cat.income > 0)
  const expenseCategories = data.categories.filter((cat) => cat.expenses > 0)

  const tooltipWidth = 320 // estimated max width
  const spaceToRight = window.innerWidth - position.x
  const showToRight = spaceToRight >= tooltipWidth + 20 // 20px margin

  const horizontalOffset = showToRight ? 15 : -15 // distance from cursor
  const horizontalTransform = showToRight ? "0%" : "-100%"

  return (
    <div
      className="fixed z-50 bg-white border border-gray-200 rounded-lg shadow-lg p-4 max-w-xs pointer-events-none"
      style={{
        left: `${position.x + horizontalOffset}px`,
        top: `${position.y}px`,
        transform: `translate(${horizontalTransform}, -50%)`, // Center vertically, adjust horizontally
        width: "320px",
      }}
    >
      {/* Header */}
      <div className="mb-3 pb-2 border-b border-gray-100">
        <h3 className="font-bold text-gray-900 text-sm">{formatPeriodLabel(data.period, data.date)}</h3>
        <p className="text-xs text-gray-500">
          {data.totalTransactions} transaction{data.totalTransactions !== 1 ? "s" : ""}
        </p>
      </div>

      {/* Totals */}
      <div className="mb-3 space-y-1">
        {data.income > 0 && (
          <div className="flex justify-between items-center">
            <span className="text-sm font-medium text-green-600">Total Income:</span>
            <span className="text-sm font-bold text-green-600">{formatCurrency(data.income, defaultCurrency)}</span>
          </div>
        )}
        {data.expenses > 0 && (
          <div className="flex justify-between items-center">
            <span className="text-sm font-medium text-red-600">Total Expenses:</span>
            <span className="text-sm font-bold text-red-600">{formatCurrency(data.expenses, defaultCurrency)}</span>
          </div>
        )}
      </div>

      {/* Income Categories */}
      {incomeCategories.length > 0 && (
        <div className="mb-3">
          <h4 className="text-xs font-semibold text-green-600 mb-2 uppercase tracking-wide">Income by Category</h4>
          <div className="space-y-1">
            {incomeCategories.map((category) => (
              <div key={`income-${category.code}`} className="flex items-center justify-between">
                <div className="flex items-center gap-2 flex-1 min-w-0">
                  <div className="w-3 h-3 rounded-full flex-shrink-0" style={{ backgroundColor: category.color }} />
                  <span className="text-xs text-gray-700 truncate">{category.name}</span>
                </div>
                <span className="text-xs font-medium text-green-600 ml-2">
                  {formatCurrency(category.income, defaultCurrency)}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Expense Categories */}
      {expenseCategories.length > 0 && (
        <div>
          <h4 className="text-xs font-semibold text-red-600 mb-2 uppercase tracking-wide">Expenses by Category</h4>
          <div className="space-y-1">
            {expenseCategories.map((category) => (
              <div key={`expense-${category.code}`} className="flex items-center justify-between">
                <div className="flex items-center gap-2 flex-1 min-w-0">
                  <div className="w-3 h-3 rounded-full flex-shrink-0" style={{ backgroundColor: category.color }} />
                  <span className="text-xs text-gray-700 truncate">{category.name}</span>
                </div>
                <span className="text-xs font-medium text-red-600 ml-2">
                  {formatCurrency(category.expenses, defaultCurrency)}
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
```

## File: `components/dashboard/income-expense-graph.tsx`
```tsx
"use client"

import { formatCurrency, formatPeriodLabel } from "@/lib/utils"
import { DetailedTimeSeriesData } from "@/models/stats"
import { addDays, endOfMonth, format, startOfMonth } from "date-fns"
import { useRouter } from "next/navigation"
import { useEffect, useRef, useState } from "react"
import { IncomeExpenceGraphTooltip } from "./income-expense-graph-tooltip"

interface IncomeExpenseGraphProps {
  data: DetailedTimeSeriesData[]
  defaultCurrency: string
}

export function IncomeExpenseGraph({ data, defaultCurrency }: IncomeExpenseGraphProps) {
  const router = useRouter()
  const scrollContainerRef = useRef<HTMLDivElement>(null)
  const [tooltip, setTooltip] = useState<{
    data: DetailedTimeSeriesData | null
    position: { x: number; y: number }
    visible: boolean
  }>({
    data: null,
    position: { x: 0, y: 0 },
    visible: false,
  })

  // Auto-scroll to the right to show latest data
  useEffect(() => {
    if (scrollContainerRef.current) {
      scrollContainerRef.current.scrollLeft = scrollContainerRef.current.scrollWidth
    }
  }, [data])

  const handleBarHover = (item: DetailedTimeSeriesData, event: React.MouseEvent) => {
    const rect = event.currentTarget.getBoundingClientRect()
    const containerRect = scrollContainerRef.current?.getBoundingClientRect()

    setTooltip({
      data: item,
      position: {
        x: rect.left + rect.width / 2,
        y: containerRect ? containerRect.top + containerRect.height / 2 : rect.top,
      },
      visible: true,
    })
  }

  const handleBarLeave = () => {
    setTooltip((prev) => ({ ...prev, visible: false }))
  }

  const handleBarClick = (item: DetailedTimeSeriesData, type: "income" | "expense") => {
    // Calculate date range for the period
    const isDailyPeriod = item.period.includes("-") && item.period.split("-").length === 3

    let dateFrom: string
    let dateTo: string

    if (isDailyPeriod) {
      // Daily period: use the exact date, add 1 day to dateTo
      const date = new Date(item.period)
      dateFrom = item.period // YYYY-MM-DD format
      dateTo = format(addDays(date, 1), "yyyy-MM-dd")
    } else {
      // Monthly period: use first and last day of the month, add 1 day to dateTo
      const [year, month] = item.period.split("-")
      const monthDate = new Date(parseInt(year), parseInt(month) - 1, 1)

      dateFrom = format(startOfMonth(monthDate), "yyyy-MM-dd")
      dateTo = format(addDays(endOfMonth(monthDate), 1), "yyyy-MM-dd")
    }

    // Build URL parameters
    const params = new URLSearchParams({
      type,
      dateFrom,
      dateTo,
    })

    // Navigate to transactions page with filters
    router.push(`/transactions?${params.toString()}`)
  }

  if (!data.length) {
    return (
      <div className="w-full h-96 flex items-center justify-center text-muted-foreground">
        No data available for the selected period
      </div>
    )
  }

  const maxIncome = Math.max(...data.map((d) => d.income))
  const maxExpense = Math.max(...data.map((d) => d.expenses))
  const maxValue = Math.max(maxIncome, maxExpense)

  if (maxValue === 0) {
    return (
      <div className="w-full h-96 flex items-center justify-center text-muted-foreground">
        No transactions found for the selected period
      </div>
    )
  }

  return (
    <div className="w-full h-[400px]">
      {/* Chart container with horizontal scroll */}
      <div ref={scrollContainerRef} className="relative h-full overflow-x-auto">
        <div className="h-full flex flex-col" style={{ minWidth: `${Math.max(600, data.length * 94)}px` }}>
          {/* Income section (top half) */}
          <div className="h-1/2 flex justify-center gap-1 px-2">
            {data.map((item, index) => {
              const incomeHeight = maxValue > 0 ? (item.income / maxValue) * 100 : 0

              return (
                <div
                  key={`income-${item.period}`}
                  className="flex-1 min-w-[90px] h-full flex flex-col justify-end items-center cursor-pointer"
                  onMouseEnter={(e) => handleBarHover(item, e)}
                  onMouseLeave={handleBarLeave}
                  onClick={() => item.income > 0 && handleBarClick(item, "income")}
                >
                  {/* Period label above income bars */}
                  <div className="text-sm font-bold text-gray-700 break-words mb-2 text-center">
                    {formatPeriodLabel(item.period, item.date)}
                  </div>

                  {item.income > 0 && (
                    <>
                      {/* Income amount label */}
                      <div className="text-xs font-semibold text-green-600 mb-1 break-all text-center">
                        {formatCurrency(item.income, defaultCurrency)}
                      </div>
                      {/* Income bar growing upward from bottom */}
                      <div
                        className="w-full bg-gradient-to-t from-green-500 via-green-400 to-emerald-300 border border-green-500/50 rounded-t-lg shadow-sm hover:shadow-md transition-shadow duration-200 min-w-full"
                        style={{ height: `${incomeHeight}%` }}
                      />
                    </>
                  )}
                </div>
              )
            })}
          </div>

          {/* X-axis line (center) */}
          <div className="w-full border-t-2 border-gray-600" />

          {/* Expense section (bottom half) */}
          <div className="h-1/2 flex justify-center gap-1 px-2">
            {data.map((item, index) => {
              const expenseHeight = maxValue > 0 ? (item.expenses / maxValue) * 100 : 0

              return (
                <div
                  key={`expense-${item.period}`}
                  className="flex-1 min-w-[90px] h-full flex flex-col justify-start items-center cursor-pointer"
                  onMouseEnter={(e) => handleBarHover(item, e)}
                  onMouseLeave={handleBarLeave}
                  onClick={() => item.expenses > 0 && handleBarClick(item, "expense")}
                >
                  {item.expenses > 0 && (
                    <>
                      {/* Expense bar growing downward from top */}
                      <div
                        className="w-full bg-gradient-to-b from-red-500 via-red-400 to-rose-300 border border-red-500/50 rounded-b-lg shadow-sm hover:shadow-md transition-shadow duration-200 min-w-full"
                        style={{ height: `${expenseHeight}%` }}
                      />
                      {/* Expense amount label */}
                      <div className="text-xs font-semibold text-red-600 mt-1 break-all text-center">
                        {formatCurrency(item.expenses, defaultCurrency)}
                      </div>
                    </>
                  )}
                </div>
              )
            })}
          </div>
        </div>
      </div>

      {/* Tooltip */}
      <IncomeExpenceGraphTooltip
        data={tooltip.data}
        defaultCurrency={defaultCurrency}
        position={tooltip.position}
        visible={tooltip.visible}
      />
    </div>
  )
}
```

## File: `components/dashboard/projects-widget.tsx`
```tsx
import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { formatCurrency } from "@/lib/utils"
import { ProjectStats } from "@/models/stats"
import { Project } from "@/prisma/client"
import { Plus } from "lucide-react"
import Link from "next/link"

export function ProjectsWidget({
  projects,
  statsPerProject,
}: {
  projects: Project[]
  statsPerProject: Record<string, ProjectStats>
}) {
  return (
    <div className="grid gap-4 md:grid-cols-2">
      {projects.map((project) => (
        <Link key={project.code} href={`/transactions?projectCode=${project.code}`}>
          <Card className="bg-gradient-to-tr from-white via-slate-50/40 to-purple-50/30 border-slate-200/60 hover:shadow-xl transition-all duration-500 hover:scale-[1.01] group cursor-pointer">
            <CardHeader className="group-hover:translate-y-[-2px] transition-transform duration-300">
              <CardTitle>
                <Badge
                  className="text-lg shadow-md hover:shadow-lg transition-all duration-300"
                  style={{ backgroundColor: project.color }}
                >
                  {project.name}
                </Badge>
              </CardTitle>
            </CardHeader>
            <CardContent className="group-hover:translate-y-[-1px] transition-transform duration-300">
              <div className="flex flex-wrap gap-4 justify-between items-center">
                <div className="bg-gradient-to-br from-green-50/80 to-emerald-50/60 p-3 rounded-xl border border-green-100/50">
                  <div className="text-sm font-medium text-muted-foreground">Income</div>
                  <div className="text-2xl font-bold text-green-500">
                    {Object.entries(statsPerProject[project.code]?.totalIncomePerCurrency).map(([currency, total]) => (
                      <div
                        key={currency}
                        className="flex flex-col gap-2 font-bold text-green-500 text-base first:text-2xl"
                      >
                        {formatCurrency(total, currency)}
                      </div>
                    ))}
                    {!Object.entries(statsPerProject[project.code]?.totalIncomePerCurrency).length && (
                      <div className="font-bold text-base first:text-2xl">0.00</div>
                    )}
                  </div>
                </div>
                <div className="bg-gradient-to-br from-red-50/80 to-rose-50/60 p-3 rounded-xl border border-red-100/50">
                  <div className="text-sm font-medium text-muted-foreground">Expenses</div>
                  <div className="text-2xl font-bold text-red-500">
                    {Object.entries(statsPerProject[project.code]?.totalExpensesPerCurrency).map(
                      ([currency, total]) => (
                        <div
                          key={currency}
                          className="flex flex-col gap-2 font-bold text-red-500 text-base first:text-2xl"
                        >
                          {formatCurrency(total, currency)}
                        </div>
                      )
                    )}
                    {!Object.entries(statsPerProject[project.code]?.totalExpensesPerCurrency).length && (
                      <div className="font-bold text-base first:text-2xl">0.00</div>
                    )}
                  </div>
                </div>
                <div className="bg-gradient-to-br from-violet-50/80 to-indigo-50/60 p-3 rounded-xl border border-violet-100/50">
                  <div className="text-sm font-medium text-muted-foreground">Profit</div>
                  <div className="text-2xl font-bold">
                    {Object.entries(statsPerProject[project.code]?.profitPerCurrency).map(([currency, total]) => (
                      <div
                        key={currency}
                        className={`flex flex-col gap-2 items-center text-2xl font-bold ${
                          total >= 0 ? "text-green-500" : "text-red-500"
                        }`}
                      >
                        {formatCurrency(total, currency)}
                      </div>
                    ))}
                    {!Object.entries(statsPerProject[project.code]?.profitPerCurrency).length && (
                      <div className="text-2xl font-bold">0.00</div>
                    )}
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>
        </Link>
      ))}
      <Link
        href="/settings/projects"
        className="flex items-center justify-center gap-2 border-dashed border-2 border-gradient-to-r rounded-lg p-6 text-muted-foreground transition-all duration-300 hover:scale-[1.02] hover:shadow-lg group"
      >
        <Plus className="h-5 w-5 group-hover:rotate-90 transition-transform duration-300" />
        <span className="font-medium">Create New Project</span>
      </Link>
    </div>
  )
}
```

## File: `components/dashboard/stats-widget.tsx`
```tsx
import { FiltersWidget } from "@/components/dashboard/filters-widget"
import { IncomeExpenseGraph } from "@/components/dashboard/income-expense-graph"
import { ProjectsWidget } from "@/components/dashboard/projects-widget"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { getCurrentUser } from "@/lib/auth"
import { formatCurrency } from "@/lib/utils"
import { getProjects } from "@/models/projects"
import { getSettings } from "@/models/settings"
import { getDashboardStats, getDetailedTimeSeriesStats, getProjectStats } from "@/models/stats"
import { TransactionFilters } from "@/models/transactions"
import { ArrowDown, ArrowUp, BicepsFlexed } from "lucide-react"
import Link from "next/link"

export async function StatsWidget({ filters }: { filters: TransactionFilters }) {
  const user = await getCurrentUser()
  const projects = await getProjects(user.id)
  const settings = await getSettings(user.id)
  const defaultCurrency = settings.default_currency || "EUR"

  const stats = await getDashboardStats(user.id, filters)
  const statsTimeSeries = await getDetailedTimeSeriesStats(user.id, filters, defaultCurrency)
  const statsPerProject = Object.fromEntries(
    await Promise.all(
      projects.map((project) => getProjectStats(user.id, project.code, filters).then((stats) => [project.code, stats]))
    )
  )

  return (
    <div className="flex flex-col gap-5">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold">Overview</h2>

        <FiltersWidget defaultFilters={filters} defaultRange="last-12-months" />
      </div>

      {statsTimeSeries.length > 0 && <IncomeExpenseGraph data={statsTimeSeries} defaultCurrency={defaultCurrency} />}

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Link href="/transactions?type=income">
          <Card className="bg-gradient-to-br from-white via-green-50/30 to-emerald-50/40 border-green-200/50 hover:shadow-lg transition-all duration-300 hover:scale-[1.02] cursor-pointer">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Total Income</CardTitle>
              <ArrowUp className="h-4 w-4 text-green-500" />
            </CardHeader>
            <CardContent>
              {Object.entries(stats.totalIncomePerCurrency).map(([currency, total]) => (
                <div
                  key={currency}
                  className="flex gap-2 items-center font-bold text-base first:text-2xl text-green-500"
                >
                  {formatCurrency(total, currency)}
                </div>
              ))}
              {!Object.entries(stats.totalIncomePerCurrency).length && <div className="text-2xl font-bold">0.00</div>}
            </CardContent>
          </Card>
        </Link>
        <Link href="/transactions?type=expense">
          <Card className="bg-gradient-to-br from-white via-red-50/30 to-rose-50/40 border-red-200/50 hover:shadow-lg transition-all duration-300 hover:scale-[1.02] cursor-pointer">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Total Expenses</CardTitle>
              <ArrowDown className="h-4 w-4 text-red-500" />
            </CardHeader>
            <CardContent>
              {Object.entries(stats.totalExpensesPerCurrency).map(([currency, total]) => (
                <div key={currency} className="flex gap-2 items-center font-bold text-base first:text-2xl text-red-500">
                  {formatCurrency(total, currency)}
                </div>
              ))}
              {!Object.entries(stats.totalExpensesPerCurrency).length && <div className="text-2xl font-bold">0.00</div>}
            </CardContent>
          </Card>
        </Link>
        <Link href="/transactions">
          <Card className="bg-gradient-to-br from-white via-pink-50/30 to-indigo-50/40 border-pink-200/50 hover:shadow-lg transition-all duration-300 hover:scale-[1.02] cursor-pointer">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Net Profit</CardTitle>
              <BicepsFlexed className="h-4 w-4" />
            </CardHeader>
            <CardContent>
              {Object.entries(stats.profitPerCurrency).map(([currency, total]) => (
                <div
                  key={currency}
                  className={`flex gap-2 items-center font-bold text-base first:text-2xl ${
                    total >= 0 ? "text-green-500" : "text-red-500"
                  }`}
                >
                  {formatCurrency(total, currency)}
                </div>
              ))}
              {!Object.entries(stats.profitPerCurrency).length && <div className="text-2xl font-bold">0.00</div>}
            </CardContent>
          </Card>
        </Link>
        <Link href="/transactions">
          <Card className="bg-gradient-to-br from-white via-blue-50/30 to-indigo-50/40 border-blue-200/50 hover:shadow-lg transition-all duration-300 hover:scale-[1.02] cursor-pointer">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle className="text-sm font-medium">Processed Transactions</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{stats.invoicesProcessed}</div>
            </CardContent>
          </Card>
        </Link>
      </div>

      <div>
        <h2 className="text-2xl font-bold">Projects</h2>
      </div>

      <ProjectsWidget projects={projects} statsPerProject={statsPerProject} />
    </div>
  )
}
```

## File: `components/dashboard/unsorted-widget.tsx`
```tsx
"use client"

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { File } from "@/prisma/client"
import { Cake, FilePlus } from "lucide-react"
import Link from "next/link"

export default function DashboardUnsortedWidget({ files }: { files: File[] }) {
  return (
    <Card className="w-full h-full sm:max-w-xs bg-accent">
      <CardHeader>
        <CardTitle>
          <Link href="/unsorted">
            {files.length > 0 ? `${files.length} unsorted files` : "No unsorted files"} &rarr;
          </Link>
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex flex-col gap-2">
          {files.slice(0, 3).map((file) => (
            <Link
              href={`/unsorted/#${file.id}`}
              key={file.id}
              className="rounded-md p-2 bg-background hover:bg-black hover:text-white"
            >
              <div className="flex flex-row gap-2">
                <FilePlus className="w-8 h-8" />
                <div className="grid flex-1 text-left leading-tight">
                  <span className="truncate text-xs font-semibold">{file.filename}</span>
                  <span className="truncate text-xs">{file.mimetype}</span>
                </div>
              </div>
            </Link>
          ))}
          {files.length == 0 && (
            <div className="flex flex-col items-center justify-center gap-2 text-sm h-full min-h-[100px] opacity-30">
              <Cake className="w-8 h-8" />
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  )
}
```

## File: `components/dashboard/welcome-widget.tsx`
```tsx
import { Button } from "@/components/ui/button"
import { Card, CardDescription, CardTitle } from "@/components/ui/card"
import { ColoredText } from "@/components/ui/colored-text"
import { getCurrentUser } from "@/lib/auth"
import { getSettings, updateSettings } from "@/models/settings"
import { Banknote, ChartBarStacked, FolderOpenDot, Key, TextCursorInput, X } from "lucide-react"
import { revalidatePath } from "next/cache"
import Image from "next/image"
import Link from "next/link"

export async function WelcomeWidget() {
  const user = await getCurrentUser()
  const settings = await getSettings(user.id)

  return (
    <Card className="flex flex-col lg:flex-row items-start gap-10 p-10 w-full">
      <Image src="/logo/1024.png" alt="Logo" width={256} height={256} className="w-64 h-64" />
      <div className="flex flex-col">
        <CardTitle className="flex items-center justify-between">
          <span className="text-2xl font-bold">
            <ColoredText>Hey, I&apos;m TaxHacker 👋</ColoredText>
          </span>
          <Button
            variant="outline"
            size="icon"
            onClick={async () => {
              "use server"
              await updateSettings(user.id, "is_welcome_message_hidden", "true")
              revalidatePath("/")
            }}
          >
            <X className="h-4 w-4" />
          </Button>
        </CardTitle>
        <CardDescription className="mt-5">
          <p className="mb-3">
            I&apos;m a little accountant app that helps you deal with endless receipts, checks and invoices with (you
            guessed it) AI. Here&apos;s what I can do:
          </p>
          <ul className="mb-5 list-disc pl-5 space-y-1">
            <li>
              <strong>Upload me a photo or a PDF</strong> and I will recognize, categorize and save it as a transaction
              for your tax advisor.
            </li>
            <li>
              I can <strong>automatically convert currencies</strong> and look up exchange rates for a given date.
            </li>
            <li>
              I even <strong>support crypto!</strong> Historical exchange rates for staking too.
            </li>
            <li>
              All <strong>LLM prompts are configurable</strong>: for fields, categories and projects. You can go to
              settings and change them however you want.
            </li>
            <li>
              I save data in a <strong>local SQLite database</strong> and can export it to CSV and ZIP archives.
            </li>
            <li>
              You can even <strong>create your own new fields</strong> to be analyzed and they will be included in the
              CSV export for your tax advisor.
            </li>
            <li>
              I&apos;m still <strong>very young</strong> and can make mistakes. Use me at your own risk!
            </li>
          </ul>
          <p className="mb-3">
            While I can save you a lot of time in categorizing transactions and generating reports, I still highly
            recommend giving the results to a professional tax advisor for review when filing your taxes!
          </p>
        </CardDescription>
        <div className="mt-2">
          <Link href="https://github.com/vas3k/TaxHacker" className="text-blue-500 hover:underline">
            Source Code
          </Link>
          <span className="mx-2">|</span>
          <Link href="https://github.com/vas3k/TaxHacker/issues" className="text-blue-500 hover:underline">
            Request New Feature
          </Link>
          <span className="mx-2">|</span>
          <Link href="https://github.com/vas3k/TaxHacker/issues" className="text-blue-500 hover:underline">
            Report a Bug
          </Link>
          <span className="mx-2">|</span>
          <Link href="mailto:me@vas3k.ru" className="text-blue-500 hover:underline">
            Contact the Author
          </Link>
        </div>
        <div className="flex flex-wrap gap-2 mt-8">
          {settings.openai_api_key === "" && (
            <Link href="/settings/llm">
              <Button>
                <Key className="h-4 w-4" />
                Please give your ChatGPT key here
              </Button>
            </Link>
          )}
          <Link href="/settings">
            <Button variant="outline">
              <Banknote className="h-4 w-4" />
              Default Currency: {settings.default_currency}
            </Button>
          </Link>
          <Link href="/settings/categories">
            <Button variant="outline">
              <ChartBarStacked className="h-4 w-4" />
              Categories
            </Button>
          </Link>
          <Link href="/settings/projects">
            <Button variant="outline">
              <FolderOpenDot className="h-4 w-4" />
              Projects
            </Button>
          </Link>
          <Link href="/settings/fields">
            <Button variant="outline">
              <TextCursorInput className="h-4 w-4" />
              Custom Fields
            </Button>
          </Link>
        </div>
      </div>
    </Card>
  )
}
```

## File: `components/emails/email-layout.tsx`
```tsx
import Head from "next/head"
import React from "react"

interface EmailLayoutProps {
  children: React.ReactNode
  preview?: string
}

export const EmailLayout: React.FC<EmailLayoutProps> = ({ children, preview = "" }) => (
  <html>
    <Head>
      <meta charSet="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <meta name="color-scheme" content="light" />
      <meta name="supported-color-schemes" content="light" />
      {preview && <title>{preview}</title>}
      <style
        dangerouslySetInnerHTML={{
          __html: `
        body {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
          margin: 0;
          padding: 0;
          color: #333;
          background-color: #f9f9f9;
        }
        .container {
          max-width: 600px;
          margin: 40px auto;
          padding: 20px;
          background-color: #ffffff;
          border-radius: 8px;
          box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        .header {
          margin-bottom: 20px;
          text-align: left;
        }
        .logo {
          width: 60px;
          height: 60px;
          margin-bottom: 10px;
        }
        .footer {
          margin-top: 30px;
          text-align: center;
          font-size: 12px;
          color: #666;
        }
      `,
        }}
      />
    </Head>
    <body>
      <div className="container">{children}</div>
    </body>
  </html>
)
```

## File: `components/emails/newsletter-welcome-email.tsx`
```tsx
import React from "react"
import { EmailLayout } from "./email-layout"

export const NewsletterWelcomeEmail: React.FC = () => (
  <EmailLayout preview="Welcome to TaxHacker Newsletter!">
    <h2 style={{ color: "#4f46e5" }}>👋 Welcome to TaxHacker!</h2>

    <p style={{ fontSize: "16px", lineHeight: "1.5", color: "#333" }}>
      Thank you for subscribing to our updates. We&apos;ll keep you updated about:
    </p>
    <ul
      style={{
        paddingLeft: "20px",
        fontSize: "16px",
        lineHeight: "1.5",
        color: "#333",
      }}
    >
      <li>New features and improvements</li>
      <li>Our plans and timelines</li>
      <li>Updates about our SaaS version</li>
    </ul>
    <div style={{ marginTop: "30px", borderTop: "1px solid #eee", paddingTop: "20px" }}>
      <p style={{ fontSize: "16px", color: "#333" }}>
        Best regards,
        <br />
        The TaxHacker Team
      </p>
    </div>
  </EmailLayout>
)
```

## File: `components/emails/otp-email.tsx`
```tsx
import React from "react"
import { EmailLayout } from "./email-layout"

interface OTPEmailProps {
  otp: string
}

export const OTPEmail: React.FC<OTPEmailProps> = ({ otp }) => (
  <EmailLayout preview="Your TaxHacker verification code">
    <h2 style={{ textAlign: "center", color: "#4f46e5" }}>🔑 Your TaxHacker verification code</h2>
    <div
      style={{
        margin: "20px 0",
        padding: "20px",
        backgroundColor: "#f3f4f6",
        borderRadius: "6px",
        textAlign: "center",
      }}
    >
      <p style={{ fontSize: "16px", marginBottom: "10px" }}>Your verification code is:</p>
      <p
        style={{
          fontSize: "24px",
          fontWeight: "bold",
          color: "#4f46e5",
          letterSpacing: "2px",
          margin: "0",
        }}
      >
        {otp}
      </p>
    </div>
    <p style={{ fontSize: "14px", color: "#666", textAlign: "center" }}>This code will expire in 10 minutes.</p>
    <p style={{ fontSize: "14px", color: "#666", textAlign: "center" }}>
      If you didn&apos;t request this code, please ignore this email.
    </p>
  </EmailLayout>
)
```

## File: `components/export/transactions.tsx`
```tsx
"use client"

import { DateRangePicker } from "@/components/forms/date-range-picker"
import { FormSelectCategory } from "@/components/forms/select-category"
import { FormSelectProject } from "@/components/forms/select-project"
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Separator } from "@/components/ui/separator"
import { useDownload } from "@/hooks/use-download"
import { useProgress } from "@/hooks/use-progress"
import { useTransactionFilters } from "@/hooks/use-transaction-filters"
import { Category, Field, Project } from "@/prisma/client"
import { formatDate } from "date-fns"
import { useState } from "react"

const deselectedFields = ["files", "text"]

export function ExportTransactionsDialog({
  fields,
  categories,
  projects,
  total,
  children,
}: {
  fields: Field[]
  categories: Category[]
  projects: Project[]
  total: number
  children: React.ReactNode
}) {
  const [exportFilters, setExportFilters] = useTransactionFilters()
  const [exportFields, setExportFields] = useState<string[]>(
    fields.map((field) => (deselectedFields.includes(field.code) ? "" : field.code))
  )
  const [includeAttachments, setIncludeAttachments] = useState(true)
  const { isLoading, startProgress, progress } = useProgress({
    onError: (error) => {
      console.error("Export progress error:", error)
    },
  })

  const { download, isDownloading } = useDownload({
    onError: (error) => {
      console.error("Download error:", error)
    },
  })

  const handleSubmit = async () => {
    try {
      const progressId = await startProgress("transactions-export")

      const exportUrl = `/export/transactions?${new URLSearchParams({
        search: exportFilters?.search || "",
        dateFrom: exportFilters?.dateFrom || "",
        dateTo: exportFilters?.dateTo || "",
        ordering: exportFilters?.ordering || "",
        categoryCode: exportFilters?.categoryCode || "",
        projectCode: exportFilters?.projectCode || "",
        fields: exportFields.join(","),
        includeAttachments: includeAttachments.toString(),
        progressId: progressId || "",
      }).toString()}`
      await download(exportUrl, "transactions.zip")
    } catch (error) {
      console.error("Failed to start export:", error)
    }
  }

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button variant="outline">{children}</Button>
      </DialogTrigger>
      <DialogContent className="max-w-xl">
        <DialogHeader>
          <DialogTitle className="text-2xl font-bold">Export {total} Transactions</DialogTitle>
          <DialogDescription>Export selected transactions and files as a CSV file or a ZIP archive</DialogDescription>
        </DialogHeader>
        <div className="flex flex-col gap-4">
          <div className="flex flex-col gap-4">
            {exportFilters.search && (
              <div className="flex flex-row items-center gap-2">
                <span className="text-sm font-medium">Search query:</span>
                <span className="text-sm">{exportFilters.search}</span>
              </div>
            )}

            <div className="flex flex-row items-center gap-2">
              <span className="text-sm font-medium">Time range:</span>

              <DateRangePicker
                defaultDate={{
                  from: exportFilters?.dateFrom ? new Date(exportFilters.dateFrom) : undefined,
                  to: exportFilters?.dateTo ? new Date(exportFilters.dateTo) : undefined,
                }}
                defaultRange="all-time"
                onChange={(date) => {
                  setExportFilters({
                    ...exportFilters,
                    dateFrom: date?.from ? formatDate(date.from, "yyyy-MM-dd") : undefined,
                    dateTo: date?.to ? formatDate(date.to, "yyyy-MM-dd") : undefined,
                  })
                }}
              />
            </div>

            <div className="flex flex-row items-center gap-2">
              <FormSelectCategory
                title="Category"
                name="category"
                categories={categories}
                value={exportFilters.categoryCode}
                onValueChange={(value) => setExportFilters({ ...exportFilters, categoryCode: value })}
                placeholder="All Categories"
                emptyValue="All Categories"
              />

              <FormSelectProject
                title="Project"
                name="project"
                projects={projects}
                value={exportFilters.projectCode}
                onValueChange={(value) => setExportFilters({ ...exportFilters, projectCode: value })}
                placeholder="All Projects"
                emptyValue="All Projects"
              />
            </div>
          </div>

          <Separator />

          <div className="text-lg font-bold">Fields to be included in CSV</div>

          <div className="grid grid-cols-2 gap-2">
            {fields.map((field) => (
              <div key={field.code} className="inline-flex gap-2">
                <label className="flex items-center gap-1">
                  <input
                    type="checkbox"
                    name={field.code}
                    checked={exportFields.includes(field.code)}
                    onChange={(e) =>
                      setExportFields(
                        e.target.checked ? [...exportFields, field.code] : exportFields.filter((f) => f !== field.code)
                      )
                    }
                  />
                  <span>{field.name}</span>
                </label>
              </div>
            ))}
          </div>
          <Separator />
          <div>
            <label className="flex items-center gap-3 text-lg">
              <input
                type="checkbox"
                name="attachments"
                className="h-[20px] w-[20px]"
                checked={includeAttachments}
                onChange={(e) => setIncludeAttachments(e.target.checked)}
              />
              <span className="flex flex-col">
                <span className="font-medium">Include attached files</span>
                <span className="text-sm">(create a zip archive)</span>
              </span>
            </label>
          </div>
        </div>
        <DialogFooter className="sm:justify-end">
          <Button type="button" onClick={handleSubmit} disabled={isLoading || isDownloading}>
            {isLoading
              ? progress?.current
                ? `Archiving ${progress.current}/${progress.total} files`
                : "Exporting..."
              : isDownloading
                ? "Archive is created. Downloading..."
                : "Export Transactions"}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
```

## File: `components/files/preview.tsx`
```tsx
"use client"

import { formatBytes } from "@/lib/utils"
import { File } from "@/prisma/client"
import Image from "next/image"
import Link from "next/link"
import { useState } from "react"

export function FilePreview({ file }: { file: File }) {
  const [isEnlarged, setIsEnlarged] = useState(false)

  const fileSize =
    file.metadata && typeof file.metadata === "object" && "size" in file.metadata ? Number(file.metadata.size) : 0

  return (
    <>
      <div className="flex flex-col gap-2 p-4 overflow-hidden">
        <div className="aspect-[3/4]">
          <Image
            src={`/files/preview/${file.id}`}
            alt={file.filename}
            width={300}
            height={400}
            loading="lazy"
            className={`${
              isEnlarged
                ? "fixed inset-0 z-50 m-auto w-screen h-screen object-contain cursor-zoom-out"
                : "w-full h-full object-contain cursor-zoom-in"
            }`}
            onClick={() => setIsEnlarged(!isEnlarged)}
          />
          {isEnlarged && (
            <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-40" onClick={() => setIsEnlarged(false)} />
          )}
        </div>
        <div className="flex flex-col gap-2 mt-2 overflow-hidden">
          <h2 className="text-md underline font-semibold overflow-ellipsis">
            <Link href={`/files/download/${file.id}`}>{file.filename}</Link>
          </h2>
          <p className="text-sm overflow-ellipsis">
            <strong>Type:</strong> {file.mimetype}
          </p>
          {/* <p className="text-sm overflow-ellipsis">
            <strong>Uploaded:</strong> {format(file.createdAt, "MMM d, yyyy")}
          </p> */}
          <p className="text-sm">
            <strong>Size:</strong> {formatBytes(fileSize)}
          </p>
        </div>
      </div>
    </>
  )
}
```

## File: `components/files/screen-drop-area.tsx`
```tsx
"use client"

import { useNotification } from "@/app/(app)/context"
import { uploadFilesAction } from "@/app/(app)/files/actions"
import { uploadTransactionFilesAction } from "@/app/(app)/transactions/actions"
import { AlertCircle, CloudUpload, Loader2 } from "lucide-react"
import { useParams, useRouter } from "next/navigation"
import { useCallback, useEffect, useRef, useState } from "react"

export default function ScreenDropArea({ children }: { children: React.ReactNode }) {
  const router = useRouter()
  const { showNotification } = useNotification()
  const [isDragging, setIsDragging] = useState(false)
  const [isUploading, setIsUploading] = useState(false)
  const [uploadError, setUploadError] = useState("")
  const dragCounter = useRef(0)
  const { transactionId } = useParams()

  const handleDragEnter = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    e.stopPropagation()

    // Check if the dragged items are files
    const items = e.dataTransfer.items
    if (!items) return

    let hasFiles = false
    for (const item of items) {
      if (item.kind === "file") {
        hasFiles = true
        break
      }
    }
    if (!hasFiles) return

    dragCounter.current++
    if (dragCounter.current === 1) {
      setIsDragging(true)
    }
  }

  const handleDragOver = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    e.stopPropagation()
  }

  const handleDragLeave = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    e.stopPropagation()
    dragCounter.current--

    if (dragCounter.current === 0) {
      setIsDragging(false)
    }
  }

  const handleDrop = useCallback(
    async (e: React.DragEvent<HTMLDivElement>) => {
      e.preventDefault()
      e.stopPropagation()

      // Reset counter and dragging state
      dragCounter.current = 0
      setIsDragging(false)

      const files = e.dataTransfer.files
      if (files && files.length > 0) {
        setIsUploading(true)
        setUploadError("")

        try {
          const formData = new FormData()
          if (transactionId) {
            formData.append("transactionId", transactionId as string)
          }
          for (let i = 0; i < files.length; i++) {
            formData.append("files", files[i])
          }

          const result = transactionId
            ? await uploadTransactionFilesAction(formData)
            : await uploadFilesAction(formData)

          if (result.success) {
            showNotification({ code: "sidebar.unsorted", message: "new" })
            setTimeout(() => showNotification({ code: "sidebar.unsorted", message: "" }), 3000)
            if (!transactionId) {
              router.push("/unsorted")
            }
          } else {
            setUploadError(result.error ? result.error : "Something went wrong...")
          }
        } catch (error) {
          console.error("Upload error:", error)
          setUploadError(error instanceof Error ? error.message : "Something went wrong...")
        } finally {
          setIsUploading(false)
        }
      }
    },
    [transactionId, router, showNotification]
  )

  // Add event listeners to document body
  useEffect(() => {
    document.body.addEventListener("dragenter", handleDragEnter as unknown as EventListener)
    document.body.addEventListener("dragover", handleDragOver as unknown as EventListener)
    document.body.addEventListener("dragleave", handleDragLeave as unknown as EventListener)
    document.body.addEventListener("drop", handleDrop as unknown as EventListener)

    return () => {
      document.body.removeEventListener("dragenter", handleDragEnter as unknown as EventListener)
      document.body.removeEventListener("dragover", handleDragOver as unknown as EventListener)
      document.body.removeEventListener("dragleave", handleDragLeave as unknown as EventListener)
      document.body.removeEventListener("drop", handleDrop as unknown as EventListener)
    }
  }, [isDragging, handleDrop])

  return (
    <div className="relative min-h-screen w-full">
      {children}

      {isDragging && (
        <div
          className="fixed inset-0 bg-opacity-20 backdrop-blur-sm z-50 flex items-center justify-center"
          onDragEnter={handleDragEnter}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
        >
          <div className="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-xl text-center">
            <CloudUpload className="h-16 w-16 mx-auto mb-4 text-primary" />
            <h3 className="text-xl font-semibold mb-2">
              {transactionId ? "Drop Files to Add to Transaction" : "Drop Files to Upload"}
            </h3>
            <p className="text-gray-600 dark:text-gray-400">Drop anywhere on the screen</p>
          </div>
        </div>
      )}

      {isUploading && (
        <div className="fixed inset-0 bg-opacity-20 backdrop-blur-sm z-50 flex items-center justify-center">
          <div className="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-xl text-center">
            <Loader2 className="h-16 w-16 mx-auto mb-4 text-primary animate-spin" />
            <h3 className="text-xl font-semibold mb-2">
              {transactionId ? "Adding files to transaction..." : "Uploading..."}
            </h3>
          </div>
        </div>
      )}

      {uploadError && (
        <div className="fixed inset-0 bg-opacity-20 backdrop-blur-sm z-50 flex items-center justify-center">
          <div className="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-xl text-center">
            <AlertCircle className="h-16 w-16 mx-auto mb-4 text-red-500" />
            <h3 className="text-xl font-semibold mb-2">Upload Error</h3>
            <p className="text-gray-600 dark:text-gray-400">{uploadError}</p>
          </div>
        </div>
      )}
    </div>
  )
}
```

## File: `components/files/upload-button.tsx`
```tsx
"use client"

import { useNotification } from "@/app/(app)/context"
import { uploadFilesAction } from "@/app/(app)/files/actions"
import { Button } from "@/components/ui/button"
import config from "@/lib/config"
import { Loader2 } from "lucide-react"
import { useRouter } from "next/navigation"
import { ComponentProps, startTransition, useRef, useState } from "react"
import { FormError } from "../forms/error"

export function UploadButton({ children, ...props }: { children: React.ReactNode } & ComponentProps<typeof Button>) {
  const router = useRouter()
  const { showNotification } = useNotification()
  const fileInputRef = useRef<HTMLInputElement>(null)
  const [uploadError, setUploadError] = useState("")
  const [isUploading, setIsUploading] = useState(false)

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    setUploadError("")
    setIsUploading(true)
    if (e.target.files && e.target.files.length > 0) {
      const formData = new FormData()

      // Append all selected files to the FormData
      for (let i = 0; i < e.target.files.length; i++) {
        formData.append("files", e.target.files[i])
      }

      // Submit the files using the server action
      startTransition(async () => {
        const result = await uploadFilesAction(formData)
        if (result.success) {
          showNotification({ code: "sidebar.unsorted", message: "new" })
          setTimeout(() => showNotification({ code: "sidebar.unsorted", message: "" }), 3000)
          router.push("/unsorted")
        } else {
          setUploadError(result.error ? result.error : "Something went wrong...")
        }
        setIsUploading(false)
      })
    }
  }

  const handleButtonClick = (e: React.MouseEvent) => {
    e.preventDefault() // Prevent any form submission
    fileInputRef.current?.click()
  }

  return (
    <div>
      <input
        ref={fileInputRef}
        type="file"
        id="fileInput"
        className="hidden"
        multiple
        accept={config.upload.acceptedMimeTypes}
        onChange={handleFileChange}
      />

      <Button onClick={handleButtonClick} disabled={isUploading} type="button" {...props}>
        {isUploading ? (
          <>
            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            Uploading...
          </>
        ) : (
          <>{children}</>
        )}
      </Button>

      {uploadError && <FormError>{uploadError}</FormError>}
    </div>
  )
}
```

## File: `components/forms/date-range-picker.tsx`
```tsx
"use client"

import { format, startOfMonth, startOfQuarter, subMonths, subWeeks } from "date-fns"
import { CalendarIcon } from "lucide-react"
import { useEffect, useState } from "react"
import { DateRange } from "react-day-picker"

import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { cn } from "@/lib/utils"

export function DateRangePicker({
  defaultDate,
  defaultRange = "all-time",
  onChange,
}: {
  defaultDate?: DateRange
  defaultRange?: string
  onChange?: (date: DateRange | undefined) => void
}) {
  const predefinedRanges = [
    {
      code: "last-4-weeks",
      label: "Last 4 weeks",
      range: { from: subWeeks(new Date(), 4), to: new Date() },
    },
    {
      code: "last-12-months",
      label: "Last 12 months",
      range: { from: subMonths(new Date(), 12), to: new Date() },
    },
    {
      code: "month-to-date",
      label: "Month to date",
      range: { from: startOfMonth(new Date()), to: new Date() },
    },
    {
      code: "quarter-to-date",
      label: "Quarter to date",
      range: { from: startOfQuarter(new Date()), to: new Date() },
    },
    {
      code: `${new Date().getFullYear()}`,
      label: `${new Date().getFullYear()}`,
      range: {
        from: new Date(new Date().getFullYear(), 0, 1),
        to: new Date(),
      },
    },
    {
      code: `${new Date().getFullYear() - 1}`,
      label: `${new Date().getFullYear() - 1}`,
      range: {
        from: new Date(new Date().getFullYear() - 1, 0, 1),
        to: new Date(new Date().getFullYear(), 0, 1),
      },
    },
    {
      code: "all-time",
      label: "All time",
      range: { from: undefined, to: undefined },
    },
  ]

  const [rangeName, setRangeName] = useState<string>(defaultDate?.from ? "custom" : defaultRange)
  const [dateRange, setDateRange] = useState<DateRange | undefined>(defaultDate)

  useEffect(() => {
    if (!defaultDate?.from) {
      setRangeName(defaultRange)
      setDateRange(undefined)
    }
  }, [defaultDate, defaultRange])

  const getDisplayText = () => {
    if (rangeName === "custom") {
      if (dateRange?.from) {
        return dateRange.to
          ? `${format(dateRange.from, "LLL dd, y")} - ${format(dateRange.to, "LLL dd, y")}`
          : format(dateRange.from, "LLL dd, y")
      }
      return "Select dates"
    }
    return predefinedRanges.find((range) => range.code === rangeName)?.label || "Select dates"
  }

  return (
    <Popover>
      <PopoverTrigger asChild>
        <Button
          id="date"
          variant={"outline"}
          className={cn(
            "w-auto min-w-[130px] justify-start text-left font-normal",
            rangeName === "all-time" && "text-muted-foreground"
          )}
        >
          <CalendarIcon className="mr-2 h-4 w-4" />
          {getDisplayText()}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="flex flex-row gap-3 w-auto p-0" align="end">
        <div className="flex flex-col gap-3 p-3 border-r">
          {predefinedRanges.map(({ code, label }) => (
            <Button
              key={code}
              variant="ghost"
              className="justify-start pr-5"
              onClick={() => {
                setRangeName(code)
                const newDateRange = predefinedRanges.find((range) => range.code === code)?.range
                setDateRange(newDateRange)
                onChange?.(newDateRange)
              }}
            >
              {label}
            </Button>
          ))}
        </div>
        <Calendar
          initialFocus
          mode="range"
          defaultMonth={dateRange?.from}
          selected={dateRange}
          onSelect={(newDateRange) => {
            setRangeName("custom")
            setDateRange(newDateRange)
            onChange?.(newDateRange)
          }}
          numberOfMonths={2}
        />
      </PopoverContent>
    </Popover>
  )
}
```

## File: `components/forms/error.tsx`
```tsx
import { cn } from "@/lib/utils"
import { AlertCircle } from "lucide-react"

export function FormError({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <div
      className={cn(
        "inline-flex items-center gap-2 px-3 py-2 rounded-md bg-red-50 text-red-700 border border-red-200",
        className
      )}
    >
      <AlertCircle className="w-4 h-4 flex-shrink-0" />
      <p className="text-sm">{children}</p>
    </div>
  )
}
```

## File: `components/forms/select-category.tsx`
```tsx
"use client"

import { Category } from "@/prisma/client"
import { SelectProps } from "@radix-ui/react-select"
import { useMemo } from "react"
import { FormSelect } from "./simple"

export const FormSelectCategory = ({
  title,
  categories,
  emptyValue,
  placeholder,
  hideIfEmpty = false,
  isRequired = false,
  ...props
}: {
  title: string
  categories: Category[]
  emptyValue?: string
  placeholder?: string
  hideIfEmpty?: boolean
  isRequired?: boolean
} & SelectProps) => {
  const items = useMemo(
    () => categories.map((category) => ({ code: category.code, name: category.name, color: category.color })),
    [categories]
  )
  return (
    <FormSelect
      title={title}
      items={items}
      emptyValue={emptyValue}
      placeholder={placeholder}
      hideIfEmpty={hideIfEmpty}
      isRequired={isRequired}
      {...props}
    />
  )
}
```

## File: `components/forms/select-currency.tsx`
```tsx
import { SelectProps } from "@radix-ui/react-select"
import { useMemo } from "react"
import { FormSelect } from "./simple"

export const FormSelectCurrency = ({
  currencies,
  title,
  emptyValue,
  placeholder,
  hideIfEmpty = false,
  isRequired = false,
  ...props
}: {
  currencies: { code: string; name: string }[]
  title?: string
  emptyValue?: string
  placeholder?: string
  hideIfEmpty?: boolean
  isRequired?: boolean
} & SelectProps) => {
  const items = useMemo(
    () =>
      currencies.map((currency) => ({
        code: currency.code,
        name: `${currency.code}`,
        badge: currency.name,
      })),
    [currencies]
  )
  return (
    <FormSelect
      title={title}
      items={items}
      emptyValue={emptyValue}
      placeholder={placeholder}
      hideIfEmpty={hideIfEmpty}
      isRequired={isRequired}
      {...props}
    />
  )
}
```

## File: `components/forms/select-project.tsx`
```tsx
import { Project } from "@/prisma/client"
import { SelectProps } from "@radix-ui/react-select"
import { FormSelect } from "./simple"

export const FormSelectProject = ({
  title,
  projects,
  emptyValue,
  placeholder,
  hideIfEmpty = false,
  isRequired = false,
  ...props
}: {
  title: string
  projects: Project[]
  emptyValue?: string
  placeholder?: string
  hideIfEmpty?: boolean
  isRequired?: boolean
} & SelectProps) => {
  return (
    <FormSelect
      title={title}
      items={projects.map((project) => ({ code: project.code, name: project.name, color: project.color }))}
      emptyValue={emptyValue}
      placeholder={placeholder}
      hideIfEmpty={hideIfEmpty}
      isRequired={isRequired}
      {...props}
    />
  )
}
```

## File: `components/forms/select-type.tsx`
```tsx
import { SelectProps } from "@radix-ui/react-select"
import { FormSelect } from "./simple"

export const FormSelectType = ({
  title,
  emptyValue,
  placeholder,
  hideIfEmpty = false,
  isRequired = false,
  ...props
}: {
  title: string
  emptyValue?: string
  placeholder?: string
  hideIfEmpty?: boolean
  isRequired?: boolean
} & SelectProps) => {
  const items = [
    { code: "expense", name: "Expense", badge: "↓" },
    { code: "income", name: "Income", badge: "↑" },
    { code: "pending", name: "Pending", badge: "⏲︎" },
    { code: "other", name: "Other", badge: "?" },
  ]

  return (
    <FormSelect
      title={title}
      items={items}
      emptyValue={emptyValue}
      placeholder={placeholder}
      hideIfEmpty={hideIfEmpty}
      isRequired={isRequired}
      {...props}
    />
  )
}
```

## File: `components/forms/simple.tsx`
```tsx
"use client"
import Image from "next/image"

import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Calendar } from "@/components/ui/calendar"
import { Input } from "@/components/ui/input"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { Textarea } from "@/components/ui/textarea"
import { cn } from "@/lib/utils"
import { SelectProps } from "@radix-ui/react-select"
import { format } from "date-fns"
import { CalendarIcon, Upload } from "lucide-react"
import { InputHTMLAttributes, TextareaHTMLAttributes, useEffect, useRef, useState } from "react"

type FormInputProps = InputHTMLAttributes<HTMLInputElement> & {
  title?: string
  hideIfEmpty?: boolean
  isRequired?: boolean
}

export function FormInput({ title, hideIfEmpty = false, isRequired = false, ...props }: FormInputProps) {
  const isEmpty = (!props.defaultValue || props.defaultValue.toString().trim() === "") && !props.value

  if (hideIfEmpty && isEmpty) {
    return null
  }

  return (
    <label className="flex flex-col gap-1">
      {title && <span className="text-sm font-medium">{title}</span>}
      <Input
        {...props}
        id={props.id || (props as { name?: string }).name}
        className={cn("bg-background", isRequired && isEmpty && "bg-yellow-50", props.className)}
        data-1p-ignore
      />
    </label>
  )
}

type FormTextareaProps = TextareaHTMLAttributes<HTMLTextAreaElement> & {
  title?: string
  hideIfEmpty?: boolean
  isRequired?: boolean
}

export function FormTextarea({ title, hideIfEmpty = false, isRequired = false, ...props }: FormTextareaProps) {
  const textareaRef = useRef<HTMLTextAreaElement>(null)
  const isEmpty = (!props.defaultValue || props.defaultValue.toString().trim() === "") && !props.value

  useEffect(() => {
    const textarea = textareaRef.current
    if (!textarea) return

    const resize = () => {
      textarea.style.height = "auto"
      textarea.style.height = `${textarea.scrollHeight + 5}px`
    }

    resize() // initial resize

    textarea.addEventListener("input", resize)
    return () => textarea.removeEventListener("input", resize)
  }, [props.value, props.defaultValue])

  if (hideIfEmpty && isEmpty) {
    return null
  }

  return (
    <label className="flex flex-col gap-1">
      {title && <span className="text-sm font-medium">{title}</span>}
      <Textarea
        ref={textareaRef}
        {...props}
        id={props.id || (props as { name?: string }).name}
        className={cn("bg-background", isRequired && isEmpty && "bg-yellow-50", props.className)}
        data-1p-ignore
      />
    </label>
  )
}

export const FormSelect = ({
  items,
  title,
  emptyValue,
  placeholder,
  hideIfEmpty = false,
  isRequired = false,
  onValueChange,
  name,
  id,
  ...props
}: {
  items: Array<{ code: string; name: string; color?: string; badge?: string; logo?: string }>
  title?: string
  emptyValue?: string
  placeholder?: string
  hideIfEmpty?: boolean
  isRequired?: boolean
  name?: string
  id?: string
} & SelectProps) => {
  const [internalValue, setInternalValue] = useState<string | undefined>(
    (props.value as string | undefined) || (props.defaultValue as string | undefined)
  )
  const isControlled = props.value !== undefined
  const selectValue = (isControlled ? (props.value as string | undefined) : internalValue) || ""
  const isEmpty = !selectValue || selectValue.toString().trim() === ""

  const labelId = title ? `${id || name || "select"}-label` : undefined
  const controlId = id || name

  const handleChange = (v: string) => {
    if (!isControlled) setInternalValue(v)
    onValueChange?.(v)
  }

  if (hideIfEmpty && isEmpty) {
    return null
  }

  return (
    <span className="flex flex-col gap-1">
      {title && (
        <span className="text-sm font-medium" id={labelId}>
          {title}
        </span>
      )}
      {/* Hidden input to ensure form submissions include this value */}
      {name && <input type="hidden" name={name} value={selectValue} />}
      <Select
        {...props}
        onValueChange={handleChange}
        {...(isControlled ? { value: props.value as string } : { defaultValue: props.defaultValue as string })}
      >
        <SelectTrigger
          id={controlId}
          aria-labelledby={labelId}
          className={cn("w-full min-w-[150px] bg-background", isRequired && isEmpty && "bg-yellow-50")}
        >
          <SelectValue placeholder={placeholder} />
        </SelectTrigger>
        <SelectContent>
          {emptyValue && <SelectItem value="-">{emptyValue}</SelectItem>}
          {items.map((item) => (
            <SelectItem key={item.code} value={item.code}>
              <div className="flex items-center gap-2 text-base pr-2">
                {item.logo && <Image src={item.logo} alt={item.name} width={20} height={20} className="rounded-full" />}
                {item.badge && <Badge className="px-2">{item.badge}</Badge>}
                {!item.badge && item.color && (
                  <div className="w-2 h-2 rounded-full" style={{ backgroundColor: item.color }} />
                )}
                {item.name}
              </div>
            </SelectItem>
          ))}
        </SelectContent>
      </Select>
    </span>
  )
}

export const FormDate = ({
  name,
  title,
  placeholder = "Select date",
  defaultValue,
  ...props
}: {
  name: string
  title?: string
  placeholder?: string
  defaultValue?: Date
}) => {
  const [date, setDate] = useState<Date | undefined>(defaultValue)
  const [manualInput, setManualInput] = useState<string>(date ? format(date, "yyyy-MM-dd") : "")

  const handleDateSelect = (newDate: Date | undefined) => {
    setDate(newDate)
    setManualInput(newDate ? format(newDate, "yyyy-MM-dd") : "")
  }

  const handleManualInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setManualInput(e.target.value)
    setDate(undefined)
    try {
      const newDate = new Date(e.currentTarget.value)
      if (!isNaN(newDate.getTime())) {
        setDate(newDate)
      }
    } catch {}
  }

  return (
    <label className="flex flex-col gap-1">
      {title && <span className="text-sm font-medium">{title}</span>}
      <div className="relative">
        <Popover>
          <PopoverTrigger asChild>
            <Button
              type="button"
              variant={"outline"}
              className={cn(
                "w-full justify-start text-left font-normal bg-background",
                !date && "text-muted-foreground"
              )}
            >
              {date ? format(date, "PPP") : placeholder}
              <CalendarIcon className="ml-1 h-4 w-4 text-muted-foreground" />
            </Button>
          </PopoverTrigger>
          <PopoverContent className="w-auto p-1 flex flex-col gap-2" align="start">
            <Input
              type="text"
              name={name}
              value={manualInput}
              onChange={handleManualInputChange}
              className="text-center"
            />
            <Calendar mode="single" selected={date} onSelect={handleDateSelect} initialFocus {...props} />
          </PopoverContent>
        </Popover>
      </div>
    </label>
  )
}

export const FormAvatar = ({
  title,
  defaultValue,
  className,
  onChange,
  ...props
}: {
  title?: string
  defaultValue?: string
  className?: string
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void
} & InputHTMLAttributes<HTMLInputElement>) => {
  const [preview, setPreview] = useState<string | null>(defaultValue || null)

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) {
      const reader = new FileReader()
      reader.onloadend = () => {
        setPreview(reader.result as string)
      }
      reader.readAsDataURL(file)
    }

    // Call the original onChange if provided
    if (onChange) {
      onChange(e)
    }
  }

  return (
    <label className="inline-block">
      {title && <span className="text-sm font-medium">{title}</span>}
      <div className={cn("relative group", className)}>
        <div className="absolute inset-0 flex items-center justify-center bg-background rounded-lg overflow-hidden">
          {preview ? (
            <img src={preview} alt="Avatar preview" className="w-full h-full object-cover" />
          ) : (
            <div className="w-full h-full bg-muted flex items-center justify-center">
              <span className="text-muted-foreground">No image</span>
            </div>
          )}
        </div>
        <div className="absolute inset-0 flex items-center justify-center bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity rounded-lg">
          <input
            type="file"
            accept="image/*"
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
            onChange={handleFileChange}
            {...props}
          />
          <Upload className="z-10 bg-white/30 text-white p-1 rounded-sm h-7 w-8 cursor-pointer" />
        </div>
      </div>
    </label>
  )
}
```

## File: `components/import/csv.tsx`
```tsx
"use client"

import { parseCSVAction, saveTransactionsAction } from "@/app/(app)/import/csv/actions"
import { FormError } from "@/components/forms/error"
import { Button } from "@/components/ui/button"
import { Field } from "@/prisma/client"
import { Loader2, Play, Upload } from "lucide-react"
import { useRouter } from "next/navigation"
import { startTransition, useActionState, useEffect, useState } from "react"

const MAX_PREVIEW_ROWS = 100

export function ImportCSVTable({ fields }: { fields: Field[] }) {
  const router = useRouter()
  const [parseState, parseAction, isParsing] = useActionState(parseCSVAction, null)
  const [saveState, saveAction, isSaving] = useActionState(saveTransactionsAction, null)

  const [csvSettings, setCSVSettings] = useState({
    skipHeader: true,
  })
  const [csvData, setCSVData] = useState<string[][]>([])
  const [columnMappings, setColumnMappings] = useState<string[]>([])

  useEffect(() => {
    if (parseState?.success && parseState.data) {
      const parsedData = parseState.data as string[][]
      setCSVData(parsedData)
      if (parsedData.length > 0) {
        setColumnMappings(
          parsedData[0].map((value) => {
            const field = fields.find((field) => field.code === value || field.name === value)
            return field?.code || ""
          })
        )
      } else {
        setColumnMappings([])
      }
    }
  }, [parseState, fields])

  useEffect(() => {
    if (saveState?.success) {
      router.push("/transactions")
    }
  }, [saveState, router])

  const handleFileChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (!file) return

    const formData = new FormData()
    formData.append("file", file)

    startTransition(async () => {
      await parseAction(formData)
    })
  }

  const handleMappingChange = (columnIndex: number, fieldCode: string) => {
    setColumnMappings((prev) => {
      const state = [...prev]
      state[columnIndex] = fieldCode
      return state
    })
  }

  const handleSave = async () => {
    if (csvData.length === 0) return

    if (!isAtLeastOneFieldMapped(columnMappings)) {
      alert("Please map at least one column to a field")
      return
    }

    const startIndex = csvSettings.skipHeader ? 1 : 0
    const processedRows = csvData.slice(startIndex).map((row) => {
      const processedRow: Record<string, unknown> = {}

      columnMappings.forEach((fieldCode, columnIndex) => {
        if (!fieldCode || !row[columnIndex]) return
        processedRow[fieldCode] = row[columnIndex]
      })

      return processedRow
    })

    const formData = new FormData()
    formData.append("rows", JSON.stringify(processedRows))

    startTransition(async () => {
      await saveAction(formData)
    })
  }

  return (
    <>
      {csvData.length === 0 && (
        <div className="flex flex-col items-center justify-center gap-2 h-full min-h-[400px]">
          <p className="text-muted-foreground">Upload your CSV file to import transactions</p>
          <div className="flex flex-row gap-5 mt-8">
            <div>
              <input type="file" accept=".csv" className="hidden" id="csv-file" onChange={handleFileChange} />
              <Button type="button" onClick={() => document.getElementById("csv-file")?.click()}>
                {isParsing ? "Parsing..." : <Upload className="mr-2" />} Import from CSV
              </Button>
            </div>
          </div>
          {parseState?.error && <FormError>{parseState.error}</FormError>}
        </div>
      )}

      {csvData.length > 0 && (
        <div>
          <header className="flex flex-wrap items-center justify-between gap-2 mb-8">
            <h2 className="flex flex-row gap-3 md:gap-5">
              <span className="text-3xl font-bold tracking-tight">Import {csvData.length} items from CSV</span>
            </h2>
            <div className="flex gap-2">
              <Button onClick={handleSave} disabled={isSaving}>
                {isSaving ? (
                  <>
                    <Loader2 className="animate-spin" /> Importing...
                  </>
                ) : (
                  <>
                    <Play /> Import {csvData.length} transactions
                  </>
                )}
              </Button>
            </div>
          </header>

          {saveState?.error && <FormError>{saveState.error}</FormError>}

          <div className="flex items-center gap-4 mb-4">
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="checkbox"
                className="w-4 h-4"
                id="skip-header"
                defaultChecked={csvSettings.skipHeader}
                onChange={(e) => setCSVSettings({ ...csvSettings, skipHeader: e.target.checked })}
              />
              <span>First row is a header</span>
            </label>
          </div>

          <div className="rounded-md border">
            <div className="relative w-full overflow-auto">
              <table className="w-full caption-bottom text-sm">
                <thead className="[&_tr]:border-b">
                  <tr className="border-b transition-colors hover:bg-muted/50">
                    {csvData[0].map((_, index) => (
                      <th key={index} className="h-12 min-w-[200px] px-4 text-left align-middle font-medium">
                        <select
                          className="w-full p-2 border rounded-md"
                          value={columnMappings[index] || ""}
                          onChange={(e) => handleMappingChange(index, e.target.value)}
                        >
                          <option value="">Skip column</option>
                          {fields.map((field) => (
                            <option key={field.code} value={field.code}>
                              {field.name}
                            </option>
                          ))}
                        </select>
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody className="[&_tr:last-child]:border-0">
                  {csvData.slice(0, MAX_PREVIEW_ROWS).map((row, rowIndex) => (
                    <tr
                      key={rowIndex}
                      className={`border-b transition-colors hover:bg-muted/50 ${
                        rowIndex === 0 && csvSettings.skipHeader ? "line-through text-muted-foreground" : ""
                      }`}
                    >
                      {csvData[0].map((_, colIndex) => (
                        <td key={colIndex} className="p-4 align-middle">
                          {(row[colIndex] || "").toString().slice(0, 256)}
                        </td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {csvData.length > MAX_PREVIEW_ROWS && (
            <p className="text-muted-foreground mt-4">and {csvData.length - MAX_PREVIEW_ROWS} more entries...</p>
          )}
        </div>
      )}
    </>
  )
}

function isAtLeastOneFieldMapped(columnMappings: string[]) {
  return columnMappings.some((mapping) => mapping !== "")
}
```

## File: `components/settings/business-settings-form.tsx`
```tsx
"use client"

import { saveProfileAction } from "@/app/(app)/settings/actions"
import { FormError } from "@/components/forms/error"
import { FormAvatar, FormInput, FormTextarea } from "@/components/forms/simple"
import { Button } from "@/components/ui/button"
import { User } from "@/prisma/client"
import { CircleCheckBig } from "lucide-react"
import { useActionState } from "react"

export default function BusinessSettingsForm({ user }: { user: User }) {
  const [saveState, saveAction, pending] = useActionState(saveProfileAction, null)

  return (
    <div>
      <form action={saveAction} className="space-y-4">
        <FormInput
          title="Business Name"
          name="businessName"
          placeholder="Acme Inc."
          defaultValue={user.businessName ?? ""}
        />

        <FormTextarea
          title="Business Address"
          name="businessAddress"
          placeholder="Street, City, State, Zip Code, Country, Tax ID"
          defaultValue={user.businessAddress ?? ""}
        />

        <FormTextarea
          title="Bank Details"
          name="businessBankDetails"
          placeholder="Bank Name, Account Number, BIC, IBAN, details of payment, etc."
          defaultValue={user.businessBankDetails ?? ""}
        />

        <FormAvatar
          title="Business Logo"
          name="businessLogo"
          className="w-52 h-52"
          defaultValue={user.businessLogo ?? ""}
        />

        <div className="flex flex-row items-center gap-4">
          <Button type="submit" disabled={pending}>
            {pending ? "Saving..." : "Save"}
          </Button>
          {saveState?.success && (
            <p className="text-green-500 flex flex-row items-center gap-2">
              <CircleCheckBig />
              Saved!
            </p>
          )}
        </div>

        {saveState?.error && <FormError>{saveState.error}</FormError>}
      </form>
    </div>
  )
}
```

## File: `components/settings/crud.tsx`
```tsx
"use client"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { Check, Edit, Trash2 } from "lucide-react"
import { useOptimistic, useState } from "react"

interface CrudColumn<T> {
  key: keyof T
  label: string
  type?: "text" | "number" | "checkbox" | "select" | "color"
  options?: string[]
  defaultValue?: string | boolean
  editable?: boolean
}

interface CrudProps<T> {
  items: T[]
  columns: CrudColumn<T>[]
  onDelete: (id: string) => Promise<{ success: boolean; error?: string }>
  onAdd: (data: Partial<T>) => Promise<{ success: boolean; error?: string }>
  onEdit?: (id: string, data: Partial<T>) => Promise<{ success: boolean; error?: string }>
}

export function CrudTable<T extends { [key: string]: any }>({ items, columns, onDelete, onAdd, onEdit }: CrudProps<T>) {
  const [isAdding, setIsAdding] = useState(false)
  const [editingId, setEditingId] = useState<string | null>(null)
  const [newItem, setNewItem] = useState<Partial<T>>(itemDefaults(columns))
  const [editingItem, setEditingItem] = useState<Partial<T>>(itemDefaults(columns))
  const [optimisticItems, addOptimisticItem] = useOptimistic(items, (state, newItem: T) => [...state, newItem])

  const FormCell = (item: T, column: CrudColumn<T>) => {
    if (column.type === "checkbox") {
      return item[column.key] ? <Check /> : ""
    }
    if (column.type === "color" || column.key === "color") {
      const value = (item[column.key] as string) || ""
      return (
        <div className="flex items-center gap-2">
          <span className="w-4 h-4 rounded-full border" style={{ backgroundColor: value || "#ffffff" }} />
          <span>{value}</span>
        </div>
      )
    }
    return item[column.key]
  }

  const EditFormCell = (item: T, column: CrudColumn<T>) => {
    if (column.type === "checkbox") {
      return (
        <input
          type="checkbox"
          checked={editingItem[column.key]}
          aria-label={String(column.label)}
          onChange={(e) =>
            setEditingItem({
              ...editingItem,
              [column.key]: e.target.checked,
            })
          }
        />
      )
    } else if (column.type === "select") {
      return (
        <select
          value={editingItem[column.key]}
          className="p-2 rounded-md border bg-transparent"
          aria-label={String(column.label)}
          onChange={(e) =>
            setEditingItem({
              ...editingItem,
              [column.key]: e.target.value,
            })
          }
        >
          {column.options?.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      )
    } else if (column.type === "color" || column.key === "color") {
      return (
        <div className="flex items-center gap-2">
          <div className="relative">
            <span
              className="block h-4 w-4 rounded-full border"
              style={{ backgroundColor: (editingItem[column.key] as string) || "#000" }}
            />
            <input
              type="color"
              className="absolute inset-0 h-4 w-4 opacity-0 cursor-pointer"
              value={(editingItem[column.key] as string) || "#000"}
              onChange={(e) =>
                setEditingItem({
                  ...editingItem,
                  [column.key]: e.target.value,
                })
              }
            />
          </div>
          <Input
            type="text"
            value={(editingItem[column.key] as string) || ""}
            aria-label={String(column.label)}
            onChange={(e) =>
              setEditingItem({
                ...editingItem,
                [column.key]: e.target.value,
              })
            }
            placeholder="#FFFFFF"
          />
        </div>
      )
    }

    return (
      <Input
        type="text"
        value={editingItem[column.key] || ""}
        aria-label={String(column.label)}
        onChange={(e) =>
          setEditingItem({
            ...editingItem,
            [column.key]: e.target.value,
          })
        }
      />
    )
  }

  const AddFormCell = (column: CrudColumn<T>) => {
    if (column.type === "checkbox") {
      return (
        <input
          type="checkbox"
          checked={Boolean(newItem[column.key] || column.defaultValue)}
          aria-label={String(column.label)}
          onChange={(e) =>
            setNewItem({
              ...newItem,
              [column.key]: e.target.checked,
            })
          }
        />
      )
    } else if (column.type === "select") {
      return (
        <select
          value={String(newItem[column.key] || column.defaultValue || "")}
          className="p-2 rounded-md border bg-transparent"
          aria-label={String(column.label)}
          onChange={(e) =>
            setNewItem({
              ...newItem,
              [column.key]: e.target.value,
            })
          }
        >
          {column.options?.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
      )
    } else if (column.type === "color" || column.key === "color") {
      return (
        <div className="flex items-center gap-2">
          <div className="relative">
            <span
              className="block h-4 w-4 rounded-full border"
              style={{ backgroundColor: String(newItem[column.key] || column.defaultValue || "#000") }}
            />
            <input
              type="color"
              className="absolute inset-0 h-4 w-4 opacity-0 cursor-pointer"
              value={String(newItem[column.key] || column.defaultValue || "#000")}
              onChange={(e) =>
                setNewItem({
                  ...newItem,
                  [column.key]: e.target.value,
                })
              }
            />
          </div>
          <Input
            type="text"
            value={String(newItem[column.key] || column.defaultValue || "")}
            aria-label={String(column.label)}
            onChange={(e) =>
              setNewItem({
                ...newItem,
                [column.key]: e.target.value,
              })
            }
            placeholder="#FFFFFF"
          />
        </div>
      )
    }
    return (
      <Input
        type={column.type || "text"}
        value={String(newItem[column.key] || column.defaultValue || "")}
        aria-label={String(column.label)}
        onChange={(e) =>
          setNewItem({
            ...newItem,
            [column.key]: e.target.value,
          })
        }
      />
    )
  }

  const handleAdd = async () => {
    try {
      const result = await onAdd(newItem)
      if (result.success) {
        setIsAdding(false)
        setNewItem(itemDefaults(columns))
      } else {
        alert(result.error)
      }
    } catch (error) {
      console.error("Failed to add item:", error)
    }
  }

  const handleEdit = async (id: string) => {
    if (!onEdit) return
    try {
      const result = await onEdit(id, editingItem)
      if (result.success) {
        setEditingId(null)
        setEditingItem({})
      } else {
        alert(result.error)
      }
    } catch (error) {
      console.error("Failed to edit item:", error)
    }
  }

  const startEditing = (item: T) => {
    setEditingId(item.code || item.id)
    setEditingItem(item)
  }

  const handleDelete = async (id: string) => {
    try {
      const result = await onDelete(id)
      if (!result.success) {
        alert(result.error)
      }
    } catch (error) {
      console.error("Failed to delete item:", error)
    }
  }

  return (
    <div className="space-y-4">
      <Table>
        <TableHeader>
          <TableRow>
            {columns.map((column) => (
              <TableHead key={String(column.key)}>{column.label}</TableHead>
            ))}
            <TableHead className="w-[100px]">Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {optimisticItems.map((item, index) => (
            <TableRow key={index}>
              {columns.map((column) => (
                <TableCell key={String(column.key)} className="first:font-semibold">
                  {editingId === (item.code || item.id) && column.editable
                    ? EditFormCell(item, column)
                    : FormCell(item, column)}
                </TableCell>
              ))}
              <TableCell>
                <div className="flex gap-2">
                  {editingId === (item.code || item.id) ? (
                    <>
                      <Button size="sm" onClick={() => handleEdit(item.code || item.id)} aria-label="Save changes">
                        Save
                      </Button>
                      <Button size="sm" variant="outline" onClick={() => setEditingId(null)} aria-label="Cancel editing">
                        Cancel
                      </Button>
                    </>
                  ) : (
                    <>
                      {onEdit && (
                        <Button
                          variant="ghost"
                          size="icon"
                          onClick={() => {
                            startEditing(item)
                            setIsAdding(false)
                          }}
                          aria-label={`Edit ${String(item.name || item.code || 'item')}`}
                        >
                          <Edit />
                        </Button>
                      )}
                      {item.isDeletable && (
                        <Button 
                          variant="ghost" 
                          size="icon" 
                          onClick={() => handleDelete(item.code || item.id)}
                          aria-label={`Delete ${String(item.name || item.code || 'item')}`}
                        >
                          <Trash2 />
                        </Button>
                      )}
                    </>
                  )}
                </div>
              </TableCell>
            </TableRow>
          ))}
          {isAdding && (
            <TableRow>
              {columns.map((column) => (
                <TableCell key={String(column.key)} className="first:font-semibold">
                  {column.editable && AddFormCell(column)}
                </TableCell>
              ))}
              <TableCell>
                <div className="flex gap-2">
                  <Button size="sm" onClick={handleAdd} aria-label="Save new item">
                    Save
                  </Button>
                  <Button size="sm" variant="outline" onClick={() => setIsAdding(false)} aria-label="Cancel adding new item">
                    Cancel
                  </Button>
                </div>
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
      {!isAdding && (
        <Button
          onClick={() => {
            setIsAdding(true)
            setEditingId(null)
          }}
          aria-label="Add new item"
        >
          Add New
        </Button>
      )}
    </div>
  )
}
function itemDefaults<T>(columns: CrudColumn<T>[]) {
  return columns.reduce((acc, column) => {
    acc[column.key] = column.defaultValue as T[keyof T]
    return acc
  }, {} as Partial<T>)
}
```

## File: `components/settings/global-settings-form.tsx`
```tsx
"use client"

import { saveSettingsAction } from "@/app/(app)/settings/actions"
import { FormError } from "@/components/forms/error"
import { FormSelectCategory } from "@/components/forms/select-category"
import { FormSelectCurrency } from "@/components/forms/select-currency"
import { FormSelectType } from "@/components/forms/select-type"
import { Button } from "@/components/ui/button"
import { Category, Currency } from "@/prisma/client"
import { CircleCheckBig } from "lucide-react"
import { useActionState } from "react"

export default function GlobalSettingsForm({
  settings,
  currencies,
  categories,
}: {
  settings: Record<string, string>
  currencies: Currency[]
  categories: Category[]
}) {
  const [saveState, saveAction, pending] = useActionState(saveSettingsAction, null)

  return (
    <form action={saveAction} className="space-y-4">
      <FormSelectCurrency
        title="Default Currency"
        name="default_currency"
        defaultValue={settings.default_currency}
        currencies={currencies}
      />

      <FormSelectType title="Default Transaction Type" name="default_type" defaultValue={settings.default_type} />

      <FormSelectCategory
        title="Default Transaction Category"
        name="default_category"
        defaultValue={settings.default_category}
        categories={categories}
      />

      <div className="flex flex-row items-center gap-4">
        <Button type="submit" disabled={pending}>
          {pending ? "Saving..." : "Save Settings"}
        </Button>
        {saveState?.success && (
          <p className="text-green-500 flex flex-row items-center gap-2">
            <CircleCheckBig />
            Saved!
          </p>
        )}
      </div>

      {saveState?.error && <FormError>{saveState.error}</FormError>}
    </form>
  )
}
```

## File: `components/settings/llm-settings-form.tsx`
```tsx
"use client"

import { fieldsToJsonSchema } from "@/ai/schema"
import { saveSettingsAction } from "@/app/(app)/settings/actions"
import { FormError } from "@/components/forms/error"
import { FormTextarea } from "@/components/forms/simple"
import { Button } from "@/components/ui/button"
import { Card, CardTitle } from "@/components/ui/card"
import { Field } from "@/prisma/client"
import { CircleCheckBig, Edit, GripVertical } from "lucide-react"
import Link from "next/link"
import { useState, useActionState } from "react"
import {
  DndContext,
  closestCenter,
  PointerSensor,
  useSensor,
  useSensors
} from "@dnd-kit/core"
import type { DragEndEvent } from "@dnd-kit/core";
import {
  arrayMove,
  SortableContext,
  useSortable,
  verticalListSortingStrategy
} from "@dnd-kit/sortable"
import { PROVIDERS } from "@/lib/llm-providers";


function getInitialProviderOrder(settings: Record<string, string>) {
  let order: string[] = []
  if (!settings.llm_providers) {
    order = ['openai', 'google', 'mistral']
  } else {
    order = settings.llm_providers.split(",").map(p => p.trim())
  }
  // Remove duplicates and keep only valid providers
  return order.filter((key, idx) => PROVIDERS.some(p => p.key === key) && order.indexOf(key) === idx)
}

export default function LLMSettingsForm({
  settings,
  fields,
}: {
  settings: Record<string, string>
  fields: Field[]
  showApiKey?: boolean
}) {
  const [saveState, saveAction, pending] = useActionState(saveSettingsAction, null)
  const [providerOrder, setProviderOrder] = useState<string[]>(getInitialProviderOrder(settings))

  // Controlled values for each provider
  const [providerValues, setProviderValues] = useState(() => {
    const values: Record<string, { apiKey: string; model: string }> = {}
    PROVIDERS.forEach((provider) => {
      values[provider.key] = {
        apiKey: settings[provider.apiKeyName],
        model: settings[provider.modelName] || provider.defaultModelName,
      }
    })
    return values
  })

  function handleProviderValueChange(providerKey: string, field: "apiKey" | "model", value: string) {
    setProviderValues((prev) => ({
      ...prev,
      [providerKey]: {
        ...prev[providerKey],
        [field]: value,
      },
    }))
  }

  return (
    <>
      <form action={saveAction} className="space-y-4">

        <div className="space-y-2">
          <label className="text-sm font-medium">LLM providers</label>
          <DndProviderBlocks
            providerOrder={providerOrder}
            setProviderOrder={setProviderOrder}
            providerValues={providerValues}
            handleProviderValueChange={handleProviderValueChange}
          />
          <small className="text-muted-foreground">
            Drag provider blocks to reorder. First is highest priority.
          </small>
        </div>
        <input type="hidden" name="llm_providers" value={providerOrder.join(",")} />

        <FormTextarea
          title="Prompt for File Analysis Form"
          name="prompt_analyse_new_file"
          defaultValue={settings.prompt_analyse_new_file}
          className="h-96"
        />

        <div className="flex flex-row items-center gap-4">
          <Button type="submit" disabled={pending}>
            {pending ? "Saving..." : "Save Settings"}
          </Button>
          {saveState?.success && (
            <p className="text-green-500 flex flex-row items-center gap-2">
              <CircleCheckBig />
              Saved!
            </p>
          )}
        </div>

        {saveState?.error && <FormError>{saveState.error}</FormError>}
      </form>

      <Card className="flex flex-col gap-4 p-4 bg-accent mt-20">
        <CardTitle className="flex flex-row justify-between items-center gap-2">
          <span className="text-md font-medium">
            Current JSON Schema for{" "}
            <a
              href="https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses&lang=javascript"
              target="_blank"
              className="underline"
            >
              structured output
            </a>
          </span>
          <Link
            href="/settings/fields"
            className="text-xs underline inline-flex flex-row items-center gap-1 text-muted-foreground"
          >
            <Edit className="w-4 h-4" /> Edit Fields
          </Link>
        </CardTitle>
        <pre className="text-xs overflow-hidden text-ellipsis">
          {JSON.stringify(fieldsToJsonSchema(fields), null, 2)}
        </pre>
      </Card>
    </>
  )
}

type DndProviderBlocksProps = {
  providerOrder: string[];
  setProviderOrder: React.Dispatch<React.SetStateAction<string[]>>;
  providerValues: Record<string, { apiKey: string; model: string }>;
  handleProviderValueChange: (providerKey: string, field: "apiKey" | "model", value: string) => void;
};

function DndProviderBlocks({ providerOrder, setProviderOrder, providerValues, handleProviderValueChange }: DndProviderBlocksProps) {
  const sensors = useSensors(useSensor(PointerSensor))
  function handleDragEnd(event: DragEndEvent) {
    const { active, over } = event
    if (!over || active.id === over.id) return
    const oldIndex = providerOrder.indexOf(active.id as string)
    const newIndex = providerOrder.indexOf(over.id as string)
    setProviderOrder(arrayMove(providerOrder, oldIndex, newIndex))
  }
  return (
    <DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
      <SortableContext items={providerOrder} strategy={verticalListSortingStrategy}>
        {providerOrder.map((providerKey, idx) => (
          <SortableProviderBlock
            key={providerKey}
            id={providerKey}
            idx={idx}
            providerKey={providerKey}
            value={providerValues[providerKey]}
            handleValueChange={handleProviderValueChange}
          />
        ))}
      </SortableContext>
    </DndContext>
  )
}

type SortableProviderBlockProps = {
  id: string;
  idx: number;
  providerKey: string;
  value: { apiKey: string; model: string };
  handleValueChange: (providerKey: string, field: "apiKey" | "model", value: string) => void;
};

function SortableProviderBlock({ id, idx, providerKey, value, handleValueChange }: SortableProviderBlockProps) {
  const { attributes, listeners, setNodeRef, transform, transition, isDragging } = useSortable({ id })

  const provider = PROVIDERS.find(p => p.key === providerKey)
  if (!provider) return null
  return (
    <div
      ref={setNodeRef}
      style={{
        transform: transform ? `translateY(${transform.y}px)` : undefined,
        transition,
        opacity: isDragging ? 0.6 : 1,
      }}
      className={`bg-muted rounded-lg p-4 shadow flex flex-col gap-2 mb-2`}
    >
      <div className="flex flex-row items-center gap-2 mb-2">
        {/* Drag handle */}
        <span
          {...attributes}
          {...listeners}
          className="cursor-grab p-1 rounded hover:bg-accent transition inline-flex items-center"
          aria-label="Drag to reorder"
        >
          <GripVertical className="w-5 h-5 text-muted-foreground" />
        </span>
        <span className="font-semibold">{provider.label}</span>
      </div>
      <div className="flex flex-row gap-4 items-center">
        <input
          type="text"
          name={provider.apiKeyName}
          value={value.apiKey}
          onChange={e => handleValueChange(provider.key, "apiKey", e.target.value)}
          className="flex-1 border rounded px-2 py-1"
          placeholder="API key"
        />
        <input
          type="text"
          name={provider.modelName}
          value={value.model}
          onChange={e => handleValueChange(provider.key, "model", e.target.value)}
          className="flex-1 border rounded px-2 py-1"
          placeholder="Model name"
        />
      </div>
      {provider.apiDoc && (
        <small className="text-muted-foreground">
          Get your API key from{" "}
          <a
            href={provider.apiDoc}
            target="_blank"
            className="underline"
          >
            {provider.apiDocLabel}
          </a>
        </small>
      )}
    </div>
  )
}
```

## File: `components/settings/profile-settings-form.tsx`
```tsx
"use client"

import { saveProfileAction } from "@/app/(app)/settings/actions"
import { FormError } from "@/components/forms/error"
import { FormAvatar, FormInput } from "@/components/forms/simple"
import { Button } from "@/components/ui/button"
import { User } from "@/prisma/client"
import { CircleCheckBig } from "lucide-react"
import { useActionState } from "react"
import { SubscriptionPlan } from "./subscription-plan"

export default function ProfileSettingsForm({ user }: { user: User }) {
  const [saveState, saveAction, pending] = useActionState(saveProfileAction, null)

  return (
    <div>
      <form action={saveAction} className="space-y-4">
        <FormAvatar
          title="Avatar"
          name="avatar"
          className="w-24 h-24"
          defaultValue={user.avatar ? user.avatar + "?" + user.id : ""}
        />

        <FormInput title="Account Name" name="name" defaultValue={user.name || ""} />

        <div className="flex flex-row items-center gap-4">
          <Button type="submit" disabled={pending}>
            {pending ? "Saving..." : "Save"}
          </Button>
          {saveState?.success && (
            <p className="text-green-500 flex flex-row items-center gap-2">
              <CircleCheckBig />
              Saved!
            </p>
          )}
        </div>

        {saveState?.error && <FormError>{saveState.error}</FormError>}
      </form>

      <div className="mt-10">
        <SubscriptionPlan user={user} />
      </div>
    </div>
  )
}
```

## File: `components/settings/side-nav.tsx`
```tsx
"use client"

import { buttonVariants } from "@/components/ui/button"
import { cn } from "@/lib/utils"
import Link from "next/link"
import { usePathname } from "next/navigation"

interface SidebarNavProps extends React.HTMLAttributes<HTMLElement> {
  items: {
    href: string
    title: string
  }[]
}

export function SideNav({ className, items, ...props }: SidebarNavProps) {
  const pathname = usePathname()

  return (
    <nav className={cn("flex flex-wrap space-x-2 lg:flex-col lg:space-x-0 lg:space-y-1", className)} {...props}>
      {items.map((item) => (
        <Link
          key={item.href}
          href={item.href}
          className={cn(
            buttonVariants({ variant: "ghost" }),
            pathname === item.href ? "bg-muted hover:bg-muted" : "hover:bg-transparent hover:underline",
            "justify-start"
          )}
        >
          {item.title}
        </Link>
      ))}
    </nav>
  )
}
```

## File: `components/settings/subscription-plan.tsx`
```tsx
import { User } from "@/prisma/client"

import { PricingCard } from "@/components/auth/pricing-card"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import config from "@/lib/config"
import { PLANS } from "@/lib/stripe"
import { formatBytes, formatNumber } from "@/lib/utils"
import { formatDate } from "date-fns"
import { BrainCog, CalendarSync, HardDrive } from "lucide-react"
import Link from "next/link"
import { Badge } from "../ui/badge"

export function SubscriptionPlan({ user }: { user: User }) {
  const plan = PLANS[user.membershipPlan as keyof typeof PLANS] || PLANS.unlimited

  return (
    <div className="flex flex-wrap gap-5">
      <div className="flex flex-col gap-2 flex-1 items-center justify-center max-w-[300px]">
        <PricingCard plan={plan} hideButton={true} />
        <Badge variant="outline">Current Plan</Badge>
      </div>
      <div className="flex-1">
        <Card className="w-full p-4">
          <div className="space-y-2">
            <strong className="text-lg">Usage:</strong>
            <div className="flex items-center gap-2">
              <HardDrive className="h-4 w-4" />
              <span>
                <strong className="font-semibold">Storage:</strong> {formatBytes(user.storageUsed)} /{" "}
                {user.storageLimit > 0 ? formatBytes(user.storageLimit) : "Unlimited"}
              </span>
            </div>
            <div className="flex items-center gap-2">
              <BrainCog className="h-4 w-4" />
              <span>
                <strong className="font-semibold">AI Analyses:</strong> {formatNumber(plan.limits.ai - user.aiBalance)}{" "}
                / {plan.limits.ai > 0 ? formatNumber(plan.limits.ai) : "Unlimited"}
              </span>
            </div>
            <div className="flex items-center gap-2">
              <CalendarSync className="h-4 w-4" />
              <span>
                <strong className="font-semibold">Expiration Date:</strong>{" "}
                {user.membershipExpiresAt ? formatDate(user.membershipExpiresAt, "yyyy-MM-dd") : "Never"}
              </span>
            </div>
          </div>

          <div className="space-y-4 mt-6 text-center">
            {user.stripeCustomerId && (
              <Button asChild className="w-full">
                <Link href="/api/stripe/portal">Manage Subscription</Link>
              </Button>
            )}

            {!user.stripeCustomerId && user.membershipExpiresAt && (
              <Button asChild className="w-full">
                <Link href="/cloud">Buy Subscription</Link>
              </Button>
            )}

            <Link href={`mailto:${config.app.supportEmail}`} className="block text-sm text-muted-foreground">
              Contact Us
            </Link>
          </div>
        </Card>
      </div>
    </div>
  )
}
```

## File: `components/sidebar/blinker.tsx`
```tsx
export function Blinker() {
  return (
    <span className="relative flex size-3">
      <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-sky-400 opacity-75"></span>
      <span className="relative inline-flex size-3 rounded-full bg-sky-500"></span>
    </span>
  )
}
```

## File: `components/sidebar/mobile-menu.tsx`
```tsx
"use client"

import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { useSidebar } from "@/components/ui/sidebar"
import config from "@/lib/config"
import Link from "next/link"

export default function MobileMenu({ unsortedFilesCount }: { unsortedFilesCount: number }) {
  const { toggleSidebar } = useSidebar()

  return (
    <menu className="flex flex-row gap-2 p-2 items-center justify-between fixed top-0 left-0 w-full z-50 border-b-2 border-solid bg-background md:hidden">
      <Avatar className="h-10 w-10 rounded-lg cursor-pointer" onClick={toggleSidebar}>
        <AvatarImage src="/logo/256.png" />
        <AvatarFallback className="rounded-lg">AI</AvatarFallback>
      </Avatar>
      <Link href="/" className="text-lg font-bold">
        {config.app.title}
      </Link>
      <Link
        href="/unsorted"
        className="flex h-6 w-6 items-center justify-center rounded-full bg-primary text-sm font-medium text-primary-foreground"
      >
        {unsortedFilesCount}
      </Link>
    </menu>
  )
}
```

## File: `components/sidebar/sidebar-item.tsx`
```tsx
"use client"

import { SidebarMenuItem } from "@/components/ui/sidebar"
import { cn } from "@/lib/utils"
import { usePathname } from "next/navigation"
import { ComponentProps } from "react"

export function SidebarMenuItemWithHighlight({
  href,
  children,
  className,
  ...props
}: { href: string } & ComponentProps<typeof SidebarMenuItem>) {
  const pathname = usePathname()
  let isActive = false
  if (href === "/") {
    isActive = pathname === href
  } else {
    isActive = pathname.startsWith(href)
  }

  return (
    <SidebarMenuItem
      className={cn(
        isActive && "bg-sidebar-accent text-sidebar-accent-foreground",
        "font-medium rounded-md",
        className
      )}
      {...props}
    >
      {children}
    </SidebarMenuItem>
  )
}

// bg-primary text-primary-foreground
```

## File: `components/sidebar/sidebar-user.tsx`
```tsx
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { SidebarMenuButton } from "@/components/ui/sidebar"
import { UserProfile } from "@/lib/auth"
import { authClient } from "@/lib/auth-client"
import { PLANS } from "@/lib/stripe"
import { formatBytes } from "@/lib/utils"
import { CreditCard, LogOut, MoreVertical, Settings, Sparkles, User } from "lucide-react"
import Link from "next/link"
import { redirect } from "next/navigation"

export default function SidebarUser({ profile, isSelfHosted }: { profile: UserProfile; isSelfHosted: boolean }) {
  const signOut = async () => {
    await authClient.signOut({})
    redirect("/")
  }

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <SidebarMenuButton
          size="default"
          className="data-[state=open]:bg-sidebar-accent data-[state=open]:text-sidebar-accent-foreground"
        >
          <Avatar className="h-6 w-6 rounded-full bg-sidebar-accent">
            <AvatarImage src={profile.avatar} alt={profile.name || ""} />
            <AvatarFallback className="rounded-full bg-sidebar-accent text-sidebar-accent-foreground">
              <User className="h-4 w-4" />
            </AvatarFallback>
          </Avatar>
          <span className="truncate font-medium">{profile.name || profile.email}</span>
          <MoreVertical className="ml-auto size-4" />
        </SidebarMenuButton>
      </DropdownMenuTrigger>
      <DropdownMenuContent
        className="w-[--radix-dropdown-menu-trigger-width] min-w-56 rounded-lg"
        side="top"
        align="center"
        sideOffset={4}
      >
        <DropdownMenuLabel className="p-0 font-normal">
          <div className="flex items-center gap-2 px-1 py-1.5 text-left text-sm">
            <Avatar className="h-8 w-8 rounded-lg">
              <AvatarImage src={profile.avatar} alt={profile.name || ""} />
              <AvatarFallback className="rounded-lg">
                <User className="h-4 w-4" />
              </AvatarFallback>
            </Avatar>
            <div className="grid flex-1 text-left text-sm leading-tight">
              <span className="truncate font-semibold">{profile.name || profile.email}</span>
              <span className="truncate text-xs">{profile.email}</span>
            </div>
          </div>
        </DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuGroup>
          <DropdownMenuItem asChild>
            <Link href="/settings/profile" className="flex items-center gap-2">
              <Sparkles />
              <span className="truncate">{PLANS[profile.membershipPlan as keyof typeof PLANS].name}</span>
              <span className="ml-auto text-xs text-muted-foreground">{formatBytes(profile.storageUsed)} used</span>
            </Link>
          </DropdownMenuItem>
        </DropdownMenuGroup>
        <DropdownMenuSeparator />
        <DropdownMenuGroup>
          <DropdownMenuItem asChild>
            <Link href="/settings" className="flex items-center gap-2">
              <Settings className="h-4 w-4" />
              Settings
            </Link>
          </DropdownMenuItem>
          {!isSelfHosted && (
            <DropdownMenuItem asChild>
              <Link href="/api/stripe/portal" className="flex items-center gap-2">
                <CreditCard className="h-4 w-4" />
                Billing
              </Link>
            </DropdownMenuItem>
          )}
        </DropdownMenuGroup>
        {!isSelfHosted && (
          <>
            <DropdownMenuSeparator />
            <DropdownMenuItem asChild>
              <span onClick={signOut} className="flex items-center gap-2 text-red-600 cursor-pointer">
                <LogOut className="h-4 w-4" />
                Log out
              </span>
            </DropdownMenuItem>
          </>
        )}
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

## File: `components/sidebar/sidebar.tsx`
```tsx
"use client"

import { useNotification } from "@/app/(app)/context"
import { UploadButton } from "@/components/files/upload-button"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupContent,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarRail,
  SidebarTrigger,
  useSidebar,
} from "@/components/ui/sidebar"
import { UserProfile } from "@/lib/auth"
import config from "@/lib/config"
import { ClockArrowUp, FileText, Gift, House, Import, LayoutDashboard, Settings, Upload } from "lucide-react"
import Image from "next/image"
import Link from "next/link"
import { usePathname } from "next/navigation"
import { useEffect } from "react"
import { ColoredText } from "../ui/colored-text"
import { Blinker } from "./blinker"
import { SidebarMenuItemWithHighlight } from "./sidebar-item"
import SidebarUser from "./sidebar-user"

export function AppSidebar({
  profile,
  unsortedFilesCount,
  isSelfHosted,
}: {
  profile: UserProfile
  unsortedFilesCount: number
  isSelfHosted: boolean
}) {
  const { open, setOpenMobile } = useSidebar()
  const pathname = usePathname()
  const { notification } = useNotification()

  // Hide sidebar on mobile when clicking an item
  useEffect(() => {
    setOpenMobile(false)
  }, [pathname, setOpenMobile])

  return (
    <>
      <Sidebar variant="inset" collapsible="icon">
        <SidebarHeader>
          <Link href="/" className="flex items-center gap-2">
            <Image src="/logo/256.png" alt="Logo" className="h-10 w-10 rounded-lg" width={40} height={40} />
            <div className="grid flex-1 text-left leading-tight">
              <span className="truncate font-semibold text-lg">
                <ColoredText>{config.app.title}</ColoredText>
              </span>
            </div>
          </Link>
        </SidebarHeader>
        <SidebarContent>
          <SidebarGroup>
            <UploadButton className="w-full mt-4 mb-2">
              <Upload className="h-4 w-4" />
              {open ? <span>Upload</span> : ""}
            </UploadButton>
          </SidebarGroup>
          <SidebarGroup>
            <SidebarGroupContent>
              <SidebarMenu>
                <SidebarMenuItemWithHighlight href="/dashboard">
                  <SidebarMenuButton asChild>
                    <Link href="/dashboard">
                      <House />
                      <span>Home</span>
                    </Link>
                  </SidebarMenuButton>
                </SidebarMenuItemWithHighlight>

                <SidebarMenuItemWithHighlight href="/transactions">
                  <SidebarMenuButton asChild>
                    <Link href="/transactions">
                      <FileText />
                      <span>Transactions</span>
                      {notification && notification.code === "sidebar.transactions" && notification.message && (
                        <Blinker />
                      )}
                      <span></span>
                    </Link>
                  </SidebarMenuButton>
                </SidebarMenuItemWithHighlight>

                <SidebarMenuItemWithHighlight href="/unsorted">
                  <SidebarMenuButton asChild>
                    <Link href="/unsorted">
                      <ClockArrowUp />
                      <span>Unsorted</span>
                      {unsortedFilesCount > 0 && (
                        <span className="flex h-5 w-5 items-center justify-center rounded-full bg-primary text-xs font-medium text-primary-foreground">
                          {unsortedFilesCount}
                        </span>
                      )}
                      {notification && notification.code === "sidebar.unsorted" && notification.message && <Blinker />}
                      <span></span>
                    </Link>
                  </SidebarMenuButton>
                </SidebarMenuItemWithHighlight>
                <SidebarMenuItemWithHighlight href="/apps">
                  <SidebarMenuButton asChild>
                    <Link href="/apps">
                      <LayoutDashboard />
                      <span>Apps</span>
                    </Link>
                  </SidebarMenuButton>
                </SidebarMenuItemWithHighlight>
                <SidebarMenuItemWithHighlight href="/settings">
                  <SidebarMenuButton asChild>
                    <Link href="/settings">
                      <Settings />
                      <span>Settings</span>
                    </Link>
                  </SidebarMenuButton>
                </SidebarMenuItemWithHighlight>
              </SidebarMenu>
            </SidebarGroupContent>
          </SidebarGroup>
        </SidebarContent>
        <SidebarRail />
        <SidebarFooter>
          <SidebarGroup>
            <SidebarGroupContent>
              <SidebarMenu>
                <SidebarMenuItem>
                  <SidebarMenuButton asChild>
                    <Link href="/import/csv">
                      <Import />
                      Import from CSV
                    </Link>
                  </SidebarMenuButton>
                </SidebarMenuItem>
                {isSelfHosted && (
                  <SidebarMenuItem>
                    <SidebarMenuButton asChild>
                      <Link href="https://vas3k.com/donate/" target="_blank">
                        <Gift />
                        Thank the author
                      </Link>
                    </SidebarMenuButton>
                  </SidebarMenuItem>
                )}
                {!open && (
                  <SidebarMenuItem>
                    <SidebarTrigger />
                  </SidebarMenuItem>
                )}
              </SidebarMenu>
            </SidebarGroupContent>
          </SidebarGroup>
          <SidebarGroup>
            <SidebarGroupContent>
              <SidebarMenu>
                <SidebarMenuItem>
                  <SidebarUser profile={profile} isSelfHosted={isSelfHosted} />
                </SidebarMenuItem>
              </SidebarMenu>
            </SidebarGroupContent>
          </SidebarGroup>
        </SidebarFooter>
      </Sidebar>
    </>
  )
}
```

## File: `components/sidebar/theme-toggle.tsx`
```tsx
"use client"

import { Moon, Sun } from "lucide-react"
import { useTheme } from "next-themes"
import { useEffect, useState } from "react"

export const ThemeToggle = () => {
  const { theme, setTheme } = useTheme()
  const [mounted, setMounted] = useState(false)

  // Ensure component is mounted to avoid hydration mismatch
  useEffect(() => {
    setMounted(true)
  }, [])

  if (!mounted) {
    return null
  }

  const toggleTheme = () => {
    if (theme === "dark") {
      setTheme("light")
    } else {
      setTheme("dark")
    }
  }

  return (
    <div onClick={toggleTheme} className="flex items-center gap-2 cursor-pointer">
      {theme === "dark" ? (
        <>
          <Sun className="h-4 w-4" />
          Light Mode
        </>
      ) : (
        <>
          <Moon className="h-4 w-4" />
          Dark Mode
        </>
      )}
    </div>
  )
}
```

## File: `components/transactions/bulk-actions.tsx`
```tsx
"use client"

import { bulkDeleteTransactionsAction } from "@/app/(app)/transactions/actions"
import { Button } from "@/components/ui/button"
import { Trash2 } from "lucide-react"
import { useState } from "react"

interface BulkActionsMenuProps {
  selectedIds: string[]
  onActionComplete?: () => void
}

export function BulkActionsMenu({ selectedIds, onActionComplete }: BulkActionsMenuProps) {
  const [isLoading, setIsLoading] = useState(false)

  const handleDelete = async () => {
    const confirmMessage =
      "Are you sure you want to delete these transactions and all their files? This action cannot be undone."
    if (!confirm(confirmMessage)) return

    try {
      setIsLoading(true)
      const result = await bulkDeleteTransactionsAction(selectedIds)
      if (!result.success) {
        throw new Error(result.error)
      }
      onActionComplete?.()
    } catch (error) {
      console.error("Failed to delete transactions:", error)
      alert(`Failed to delete transactions: ${error}`)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="fixed bottom-4 right-4 z-50">
      <Button variant="destructive" className="min-w-48 gap-2" disabled={isLoading} onClick={handleDelete}>
        <Trash2 className="h-4 w-4" />
        Delete {selectedIds.length} transactions
      </Button>
    </div>
  )
}
```

## File: `components/transactions/create.tsx`
```tsx
"use client"

import { createTransactionAction } from "@/app/(app)/transactions/actions"
import { FormError } from "@/components/forms/error"
import { FormSelectCategory } from "@/components/forms/select-category"
import { FormSelectCurrency } from "@/components/forms/select-currency"
import { FormSelectProject } from "@/components/forms/select-project"
import { FormSelectType } from "@/components/forms/select-type"
import { FormInput, FormTextarea } from "@/components/forms/simple"
import { Button } from "@/components/ui/button"
import { Category, Currency, Project } from "@/prisma/client"
import { format } from "date-fns"
import { Import, Loader2 } from "lucide-react"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { useActionState, useEffect, useState } from "react"

export default function TransactionCreateForm({
  categories,
  projects,
  currencies,
  settings,
}: {
  categories: Category[]
  projects: Project[]
  currencies: Currency[]
  settings: Record<string, string>
}) {
  const router = useRouter()
  const [createState, createAction, isCreating] = useActionState(createTransactionAction, null)
  const [formData, setFormData] = useState({
    name: "",
    merchant: "",
    description: "",
    total: 0.0,
    convertedTotal: 0.0,
    currencyCode: settings.default_currency,
    convertedCurrencyCode: settings.default_currency,
    type: settings.default_type,
    categoryCode: settings.default_category,
    projectCode: settings.default_project,
    issuedAt: format(new Date(), "yyyy-MM-dd"),
    note: "",
  })

  useEffect(() => {
    if (createState?.success && createState.data) {
      router.push(`/transactions/${createState.data.id}`)
    }
  }, [createState, router])

  return (
    <form action={createAction} className="space-y-4">
      <FormInput title="Name" name="name" defaultValue={formData.name} />

      <FormInput title="Merchant" name="merchant" defaultValue={formData.merchant} />

      <FormInput title="Description" name="description" defaultValue={formData.description} />

      <div className="flex flex-row gap-4">
        <FormInput title="Total" type="number" step="0.01" name="total" defaultValue={formData.total.toFixed(2)} />

        <FormSelectCurrency
          title="Currency"
          name="currencyCode"
          currencies={currencies}
          placeholder="Select Currency"
          value={formData.currencyCode}
          onValueChange={(value) => {
            setFormData({ ...formData, currencyCode: value })
          }}
        />

        <FormSelectType title="Type" name="type" defaultValue={formData.type} />
      </div>

      {formData.currencyCode !== settings.default_currency ? (
        <div className="flex flex-row gap-4">
          <FormInput
            title={`Converted to ${settings.default_currency}`}
            type="number"
            step="0.01"
            name="convertedTotal"
            defaultValue={formData.convertedTotal.toFixed(2)}
          />
        </div>
      ) : (
        <></>
      )}

      <div className="flex flex-row flex-grow gap-4">
        <FormInput title="Issued At" type="date" name="issuedAt" defaultValue={formData.issuedAt} />
      </div>

      <div className="flex flex-row gap-4">
        <FormSelectCategory
          title="Category"
          categories={categories}
          name="categoryCode"
          defaultValue={formData.categoryCode}
          placeholder="Select Category"
        />

        <FormSelectProject
          title="Project"
          projects={projects}
          name="projectCode"
          defaultValue={formData.projectCode}
          placeholder="Select Project"
        />
      </div>

      <FormTextarea title="Note" name="note" defaultValue={formData.note} />

      <div className="flex justify-between space-x-4 pt-6">
        <Button type="button" variant="outline" className="aspect-square">
          <Link href="/import/csv">
            <Import className="h-4 w-4" />
          </Link>
        </Button>

        <Button type="submit" disabled={isCreating}>
          {isCreating ? (
            <>
              <Loader2 className="mr-2 h-4 w-4 animate-spin" />
              Creating...
            </>
          ) : (
            "Create and Add Files"
          )}
        </Button>
      </div>

      {createState?.error && <FormError>{createState.error}</FormError>}
    </form>
  )
}
```

## File: `components/transactions/edit.tsx`
```tsx
"use client"

import { deleteTransactionAction, saveTransactionAction } from "@/app/(app)/transactions/actions"
import { ItemsDetectTool } from "@/components/agents/items-detect"
import ToolWindow from "@/components/agents/tool-window"
import { FormError } from "@/components/forms/error"
import { FormSelectCategory } from "@/components/forms/select-category"
import { FormSelectCurrency } from "@/components/forms/select-currency"
import { FormSelectProject } from "@/components/forms/select-project"
import { FormSelectType } from "@/components/forms/select-type"
import { FormInput, FormTextarea } from "@/components/forms/simple"
import { Button } from "@/components/ui/button"
import { TransactionData } from "@/models/transactions"
import { Category, Currency, Field, Project, Transaction } from "@/prisma/client"
import { format } from "date-fns"
import { Loader2, Save, Trash2 } from "lucide-react"
import { useRouter } from "next/navigation"
import { startTransition, useActionState, useEffect, useMemo, useState } from "react"

export default function TransactionEditForm({
  transaction,
  categories,
  projects,
  currencies,
  fields,
  settings,
}: {
  transaction: Transaction
  categories: Category[]
  projects: Project[]
  currencies: Currency[]
  fields: Field[]
  settings: Record<string, string>
}) {
  const router = useRouter()
  const [deleteState, deleteAction, isDeleting] = useActionState(deleteTransactionAction, null)
  const [saveState, saveAction, isSaving] = useActionState(saveTransactionAction, null)

  const extraFields = fields.filter((field) => field.isExtra)
  const [formData, setFormData] = useState({
    name: transaction.name || "",
    merchant: transaction.merchant || "",
    description: transaction.description || "",
    total: transaction.total ? transaction.total / 100 : 0.0,
    currencyCode: transaction.currencyCode || settings.default_currency,
    convertedTotal: transaction.convertedTotal ? transaction.convertedTotal / 100 : 0.0,
    convertedCurrencyCode: transaction.convertedCurrencyCode,
    type: transaction.type || "expense",
    categoryCode: transaction.categoryCode || settings.default_category,
    projectCode: transaction.projectCode || settings.default_project,
    issuedAt: transaction.issuedAt ? format(transaction.issuedAt, "yyyy-MM-dd") : "",
    note: transaction.note || "",
    items: transaction.items || [],
    ...extraFields.reduce(
      (acc, field) => {
        acc[field.code] = transaction.extra?.[field.code as keyof typeof transaction.extra] || ""
        return acc
      },
      {} as Record<string, any>
    ),
  })

  const fieldMap = useMemo(() => {
    return fields.reduce(
      (acc, field) => {
        acc[field.code] = field
        return acc
      },
      {} as Record<string, Field>
    )
  }, [fields])

  const handleDelete = async () => {
    if (confirm("Are you sure? This will delete the transaction with all the files permanently")) {
      startTransition(async () => {
        await deleteAction(transaction.id)
        router.back()
      })
    }
  }

  useEffect(() => {
    if (saveState?.success) {
      router.back()
    }
  }, [saveState, router])

  return (
    <form action={saveAction} className="space-y-4">
      <input type="hidden" name="transactionId" value={transaction.id} />

      <FormInput
        title={fieldMap.name.name}
        name="name"
        defaultValue={formData.name}
        isRequired={fieldMap.name.isRequired}
      />

      <FormInput
        title={fieldMap.merchant.name}
        name="merchant"
        defaultValue={formData.merchant}
        isRequired={fieldMap.merchant.isRequired}
      />

      <FormInput
        title={fieldMap.description.name}
        name="description"
        defaultValue={formData.description}
        isRequired={fieldMap.description.isRequired}
      />

      <div className="flex flex-row gap-4">
        <FormInput
          title={fieldMap.total.name}
          type="number"
          step="0.01"
          name="total"
          defaultValue={formData.total.toFixed(2)}
          className="w-32"
          isRequired={fieldMap.total.isRequired}
        />

        <FormSelectCurrency
          title={fieldMap.currencyCode.name}
          name="currencyCode"
          value={formData.currencyCode}
          onValueChange={(value) => {
            setFormData({ ...formData, currencyCode: value })
          }}
          currencies={currencies}
          isRequired={fieldMap.currencyCode.isRequired}
        />

        <FormSelectType
          title={fieldMap.type.name}
          name="type"
          defaultValue={formData.type}
          isRequired={fieldMap.type.isRequired}
        />
      </div>

      <div className="flex flex-row flex-grow gap-4">
        <FormInput
          title={fieldMap.issuedAt.name}
          type="date"
          name="issuedAt"
          defaultValue={formData.issuedAt}
          isRequired={fieldMap.issuedAt.isRequired}
        />
        {formData.currencyCode !== settings.default_currency || formData.convertedTotal !== 0 ? (
          <>
            {formData.convertedTotal !== null && (
              <FormInput
                title={`Total converted to ${formData.convertedCurrencyCode || "UNKNOWN CURRENCY"}`}
                type="number"
                step="0.01"
                name="convertedTotal"
                defaultValue={formData.convertedTotal.toFixed(2)}
                isRequired={fieldMap.convertedTotal.isRequired}
                className="max-w-36"
              />
            )}
            {(!formData.convertedCurrencyCode || formData.convertedCurrencyCode !== settings.default_currency) && (
              <FormSelectCurrency
                title="Convert to"
                name="convertedCurrencyCode"
                defaultValue={formData.convertedCurrencyCode || settings.default_currency}
                currencies={currencies}
                isRequired={fieldMap.convertedCurrencyCode.isRequired}
              />
            )}
          </>
        ) : (
          <></>
        )}
      </div>

      <div className="flex flex-row gap-4">
        <FormSelectCategory
          title={fieldMap.categoryCode.name}
          categories={categories}
          name="categoryCode"
          defaultValue={formData.categoryCode}
          isRequired={fieldMap.categoryCode.isRequired}
        />

        <FormSelectProject
          title={fieldMap.projectCode.name}
          projects={projects}
          name="projectCode"
          defaultValue={formData.projectCode}
          isRequired={fieldMap.projectCode.isRequired}
        />
      </div>

      <FormTextarea
        title={fieldMap.note.name}
        name="note"
        defaultValue={formData.note}
        className="h-24"
        isRequired={fieldMap.note.isRequired}
      />

      <div className="flex flex-wrap gap-4">
        {extraFields.map((field) => (
          <FormInput
            key={field.code}
            type="text"
            title={field.name}
            name={field.code}
            defaultValue={(formData[field.code as keyof typeof formData] as string) || ""}
            isRequired={field.isRequired}
            className={field.type === "number" ? "max-w-36" : "max-w-full"}
          />
        ))}
      </div>

      {formData.items && Array.isArray(formData.items) && formData.items.length > 0 && (
        <ToolWindow title="Detected items">
          <ItemsDetectTool data={formData as TransactionData} />
        </ToolWindow>
      )}

      <div className="flex justify-between space-x-4 pt-6">
        <Button type="button" onClick={handleDelete} variant="destructive" disabled={isDeleting}>
          <>
            <Trash2 className="h-4 w-4" />
            {isDeleting ? "⏳ Deleting..." : "Delete "}
          </>
        </Button>

        <Button type="submit" disabled={isSaving}>
          {isSaving ? (
            <>
              <Loader2 className="h-4 w-4 animate-spin" />
              Saving...
            </>
          ) : (
            <>
              <Save className="h-4 w-4" />
              Save Transaction
            </>
          )}
        </Button>
      </div>

      <div>
        {deleteState?.error && <FormError>{deleteState.error}</FormError>}
        {saveState?.error && <FormError>{saveState.error}</FormError>}
      </div>
    </form>
  )
}
```

## File: `components/transactions/fields-selector.tsx`
```tsx
"use client"

import { updateFieldVisibilityAction } from "@/app/(app)/transactions/actions"
import { Button } from "@/components/ui/button"
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Field } from "@/prisma/client"
import { ColumnsIcon, Loader2 } from "lucide-react"
import { useRouter } from "next/navigation"
import { useState } from "react"

export function ColumnSelector({ fields, onChange }: { fields: Field[]; onChange?: () => void }) {
  const router = useRouter()
  const [isLoading, setIsLoading] = useState(false)

  const handleToggle = async (fieldCode: string, isCurrentlyVisible: boolean) => {
    setIsLoading(true)

    try {
      await updateFieldVisibilityAction(fieldCode, !isCurrentlyVisible)

      // Refresh the page to reflect changes
      if (onChange) {
        onChange()
      } else {
        router.refresh()
      }
    } catch (error) {
      console.error("Failed to toggle column visibility:", error)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="icon" title="Select table columns">
          {isLoading ? <Loader2 className="h-4 w-4 animate-spin" /> : <ColumnsIcon className="h-4 w-4" />}
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-56">
        <DropdownMenuLabel>Show Columns</DropdownMenuLabel>
        <DropdownMenuSeparator />
        {fields.map((field) => (
          <DropdownMenuCheckboxItem
            key={field.code}
            checked={field.isVisibleInList}
            onCheckedChange={() => handleToggle(field.code, field.isVisibleInList)}
            disabled={isLoading}
          >
            {field.name}
          </DropdownMenuCheckboxItem>
        ))}
      </DropdownMenuContent>
    </DropdownMenu>
  )
}
```

## File: `components/transactions/filters.tsx`
```tsx
"use client"

import { DateRangePicker } from "@/components/forms/date-range-picker"
import { ColumnSelector } from "@/components/transactions/fields-selector"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"
import { isFiltered, useTransactionFilters } from "@/hooks/use-transaction-filters"
import { TransactionFilters } from "@/models/transactions"
import { Category, Field, Project } from "@/prisma/client"
import { X } from "lucide-react"

export function TransactionSearchAndFilters({
  categories,
  projects,
  fields,
}: {
  categories: Category[]
  projects: Project[]
  fields: Field[]
}) {
  const [filters, setFilters] = useTransactionFilters()

  const handleFilterChange = (name: keyof TransactionFilters, value: any) => {
    setFilters((prev) => ({
      ...prev,
      [name]: value,
    }))
  }

  return (
    <div className="flex flex-col gap-4">
      <div className="flex flex-wrap gap-4">
        <div className="flex-1 min-w-[200px]">
          <Input
            placeholder="Search transactions..."
            defaultValue={filters.search}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleFilterChange("search", (e.target as HTMLInputElement).value)
              }
            }}
            className="w-full"
          />
        </div>

        <Select value={filters.categoryCode} onValueChange={(value) => handleFilterChange("categoryCode", value)}>
          <SelectTrigger className="w-[180px]">
            <SelectValue placeholder="All categories" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="-">All categories</SelectItem>
            {categories.map((category) => (
              <SelectItem key={category.code} value={category.code}>
                <div className="flex items-center gap-2">
                  <div className="w-2 h-2 rounded-full" style={{ backgroundColor: category.color }} />
                  {category.name}
                </div>
              </SelectItem>
            ))}
          </SelectContent>
        </Select>

        {projects.length > 1 && (
          <Select value={filters.projectCode} onValueChange={(value) => handleFilterChange("projectCode", value)}>
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="All projects" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="-">All projects</SelectItem>
              {projects.map((project) => (
                <SelectItem key={project.code} value={project.code}>
                  <div className="flex items-center gap-2">
                    <div className="w-2 h-2 rounded-full" style={{ backgroundColor: project.color }} />
                    {project.name}
                  </div>
                </SelectItem>
              ))}
            </SelectContent>
          </Select>
        )}

        <DateRangePicker
          defaultDate={{
            from: filters.dateFrom ? new Date(filters.dateFrom) : undefined,
            to: filters.dateTo ? new Date(filters.dateTo) : undefined,
          }}
          onChange={(date) => {
            handleFilterChange("dateFrom", date ? date.from : undefined)
            handleFilterChange("dateTo", date ? date.to : undefined)
          }}
        />

        {isFiltered(filters) && (
          <Button
            variant="ghost"
            size="icon"
            onClick={() => {
              setFilters({})
            }}
            className="text-muted-foreground hover:text-foreground"
            title="Clear all filters"
          >
            <X className="h-4 w-4" />
          </Button>
        )}

        <ColumnSelector fields={fields} />
      </div>
    </div>
  )
}
```

## File: `components/transactions/list.tsx`
```tsx
"use client"

import { BulkActionsMenu } from "@/components/transactions/bulk-actions"
import { Badge } from "@/components/ui/badge"
import { Checkbox } from "@/components/ui/checkbox"
import { Table, TableBody, TableCell, TableFooter, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { calcNetTotalPerCurrency, calcTotalPerCurrency, isTransactionIncomplete } from "@/lib/stats"
import { cn, formatCurrency } from "@/lib/utils"
import { Category, Field, Project, Transaction } from "@/prisma/client"
import { formatDate } from "date-fns"
import { ArrowDownIcon, ArrowUpIcon, File } from "lucide-react"
import { useRouter, useSearchParams } from "next/navigation"
import { useEffect, useMemo, useState } from "react"

type FieldRenderer = {
  name: string
  code: string
  classes?: string
  sortable: boolean
  formatValue?: (transaction: Transaction & any) => React.ReactNode
  footerValue?: (transactions: Transaction[]) => React.ReactNode
}

type FieldWithRenderer = Field & {
  renderer: FieldRenderer
}

export const standardFieldRenderers: Record<string, FieldRenderer> = {
  name: {
    name: "Name",
    code: "name",
    classes: "font-medium min-w-[120px] max-w-[300px] overflow-hidden",
    sortable: true,
  },
  merchant: {
    name: "Merchant",
    code: "merchant",
    classes: "min-w-[120px] max-w-[250px] overflow-hidden",
    sortable: true,
  },
  issuedAt: {
    name: "Date",
    code: "issuedAt",
    classes: "min-w-[100px]",
    sortable: true,
    formatValue: (transaction: Transaction) =>
      transaction.issuedAt ? formatDate(transaction.issuedAt, "yyyy-MM-dd") : "",
  },
  projectCode: {
    name: "Project",
    code: "projectCode",
    sortable: true,
    formatValue: (transaction: Transaction & { project: Project }) =>
      transaction.projectCode ? (
        <Badge className="whitespace-nowrap" style={{ backgroundColor: transaction.project?.color }}>
          {transaction.project?.name || ""}
        </Badge>
      ) : (
        "-"
      ),
  },
  categoryCode: {
    name: "Category",
    code: "categoryCode",
    sortable: true,
    formatValue: (transaction: Transaction & { category: Category }) =>
      transaction.categoryCode ? (
        <Badge className="whitespace-nowrap" style={{ backgroundColor: transaction.category?.color }}>
          {transaction.category?.name || ""}
        </Badge>
      ) : (
        "-"
      ),
  },
  files: {
    name: "Files",
    code: "files",
    sortable: false,
    formatValue: (transaction: Transaction) => (
      <div className="flex items-center gap-2 text-sm">
        <File className="w-4 h-4" />
        {(transaction.files as string[]).length}
      </div>
    ),
  },
  total: {
    name: "Total",
    code: "total",
    classes: "text-right",
    sortable: true,
    formatValue: (transaction: Transaction) => (
      <div className="text-right text-lg">
        <div
          className={cn(
            { income: "text-green-500", expense: "text-red-500", other: "text-black" }[transaction.type || "other"],
            "flex flex-col justify-end"
          )}
        >
          <span>
            {transaction.total && transaction.currencyCode
              ? formatCurrency(transaction.total, transaction.currencyCode)
              : transaction.total}
          </span>
          {transaction.convertedTotal &&
            transaction.convertedCurrencyCode &&
            transaction.convertedCurrencyCode !== transaction.currencyCode && (
              <span className="text-sm -mt-1">
                ({formatCurrency(transaction.convertedTotal, transaction.convertedCurrencyCode)})
              </span>
            )}
        </div>
      </div>
    ),
    footerValue: (transactions: Transaction[]) => {
      const netTotalPerCurrency = calcNetTotalPerCurrency(transactions)
      const turnoverPerCurrency = calcTotalPerCurrency(transactions)

      return (
        <div className="flex flex-col gap-3 text-right">
          <dl className="space-y-1">
            <dt className="text-xs font-semibold text-muted-foreground uppercase tracking-wide">Net Total</dt>
            {Object.entries(netTotalPerCurrency).map(([currency, total]) => (
              <dd
                key={`net-${currency}`}
                className={cn("text-sm first:text-base font-medium", total >= 0 ? "text-green-600" : "text-red-600")}
              >
                {formatCurrency(total, currency)}
              </dd>
            ))}
          </dl>
          <dl className="space-y-1">
            <dt className="text-xs font-semibold text-muted-foreground uppercase tracking-wide">Turnover</dt>
            {Object.entries(turnoverPerCurrency).map(([currency, total]) => (
              <dd key={`turnover-${currency}`} className="text-sm text-muted-foreground">
                {formatCurrency(total, currency)}
              </dd>
            ))}
          </dl>
        </div>
      )
    },
  },
  convertedTotal: {
    name: "Converted Total",
    code: "convertedTotal",
    classes: "text-right",
    sortable: true,
    formatValue: (transaction: Transaction) => (
      <div
        className={cn(
          { income: "text-green-500", expense: "text-red-500", other: "text-black" }[transaction.type || "other"],
          "flex flex-col justify-end text-right text-lg"
        )}
      >
        {transaction.convertedTotal && transaction.convertedCurrencyCode
          ? formatCurrency(transaction.convertedTotal, transaction.convertedCurrencyCode)
          : transaction.convertedTotal}
      </div>
    ),
  },
  currencyCode: {
    name: "Currency",
    code: "currencyCode",
    classes: "text-right",
    sortable: true,
  },
}

const getFieldRenderer = (field: Field): FieldRenderer => {
  if (standardFieldRenderers[field.code as keyof typeof standardFieldRenderers]) {
    return standardFieldRenderers[field.code as keyof typeof standardFieldRenderers]
  } else {
    return {
      name: field.name,
      code: field.code,
      classes: "",
      sortable: false,
    }
  }
}

export function TransactionList({ transactions, fields = [] }: { transactions: Transaction[]; fields?: Field[] }) {
  const [selectedIds, setSelectedIds] = useState<string[]>([])
  const router = useRouter()
  const searchParams = useSearchParams()

  const [sorting, setSorting] = useState<{ field: string | null; direction: "asc" | "desc" | null }>(() => {
    const ordering = searchParams.get("ordering")
    if (!ordering) return { field: null, direction: null }
    const isDesc = ordering.startsWith("-")
    return {
      field: isDesc ? ordering.slice(1) : ordering,
      direction: isDesc ? "desc" : "asc",
    }
  })

  const visibleFields = useMemo(
    (): FieldWithRenderer[] =>
      fields
        .filter((field) => field.isVisibleInList)
        .map((field) => ({
          ...field,
          renderer: getFieldRenderer(field),
        })),
    [fields]
  )

  const toggleAllRows = () => {
    if (selectedIds.length === transactions.length) {
      setSelectedIds([])
    } else {
      setSelectedIds(transactions.map((transaction) => transaction.id))
    }
  }

  const toggleOneRow = (e: React.MouseEvent, id: string) => {
    e.stopPropagation()
    if (selectedIds.includes(id)) {
      setSelectedIds(selectedIds.filter((item) => item !== id))
    } else {
      setSelectedIds([...selectedIds, id])
    }
  }

  const handleRowClick = (id: string) => {
    router.push(`/transactions/${id}`)
  }

  const handleSort = (field: string) => {
    let newDirection: "asc" | "desc" | null = "asc"

    if (sorting.field === field) {
      if (sorting.direction === "asc") newDirection = "desc"
      else if (sorting.direction === "desc") newDirection = null
    }

    setSorting({
      field: newDirection ? field : null,
      direction: newDirection,
    })
  }

  const renderFieldInTable = (transaction: Transaction, field: FieldWithRenderer): string | React.ReactNode => {
    if (field.isExtra) {
      return transaction.extra?.[field.code as keyof typeof transaction.extra] ?? ""
    } else if (field.renderer.formatValue) {
      return field.renderer.formatValue(transaction)
    } else {
      return String(transaction[field.code as keyof Transaction])
    }
  }

  useEffect(() => {
    const params = new URLSearchParams(searchParams.toString())
    if (sorting.field && sorting.direction) {
      const ordering = sorting.direction === "desc" ? `-${sorting.field}` : sorting.field
      params.set("ordering", ordering)
    } else {
      params.delete("ordering")
    }
    router.push(`/transactions?${params.toString()}`)
  }, [sorting])

  const getSortIcon = (field: string) => {
    if (sorting.field !== field) return null
    return sorting.direction === "asc" ? (
      <ArrowUpIcon className="w-4 h-4 ml-1 inline" />
    ) : sorting.direction === "desc" ? (
      <ArrowDownIcon className="w-4 h-4 ml-1 inline" />
    ) : null
  }

  return (
    <div className="rounded-md border">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead className="min-w-[30px] select-none">
              <Checkbox checked={selectedIds.length === transactions.length} onCheckedChange={toggleAllRows} />
            </TableHead>
            {visibleFields.map((field) => (
              <TableHead
                key={field.code}
                className={cn(
                  field.renderer.classes,
                  field.renderer.sortable && "hover:cursor-pointer hover:bg-accent select-none"
                )}
                onClick={() => field.renderer.sortable && handleSort(field.code)}
              >
                {field.name || field.renderer.name}
                {field.renderer.sortable && getSortIcon(field.code)}
              </TableHead>
            ))}
          </TableRow>
        </TableHeader>
        <TableBody>
          {transactions.map((transaction) => (
            <TableRow
              key={transaction.id}
              className={cn(
                isTransactionIncomplete(fields, transaction) && "bg-yellow-50",
                selectedIds.includes(transaction.id) && "bg-muted",
                "cursor-pointer hover:bg-muted/50"
              )}
              onClick={() => handleRowClick(transaction.id)}
            >
              <TableCell onClick={(e) => e.stopPropagation()}>
                <Checkbox
                  checked={selectedIds.includes(transaction.id)}
                  onCheckedChange={(checked) => {
                    if (checked !== "indeterminate") {
                      toggleOneRow({ stopPropagation: () => {} } as React.MouseEvent, transaction.id)
                    }
                  }}
                />
              </TableCell>
              {visibleFields.map((field) => (
                <TableCell key={field.code} className={field.renderer.classes}>
                  {renderFieldInTable(transaction, field)}
                </TableCell>
              ))}
            </TableRow>
          ))}
        </TableBody>
        <TableFooter>
          <TableRow>
            <TableCell></TableCell>
            {visibleFields.map((field) => (
              <TableCell key={field.code} className={field.renderer.classes}>
                {field.renderer.footerValue ? field.renderer.footerValue(transactions) : ""}
              </TableCell>
            ))}
          </TableRow>
        </TableFooter>
      </Table>
      {selectedIds.length > 0 && (
        <BulkActionsMenu selectedIds={selectedIds} onActionComplete={() => setSelectedIds([])} />
      )}
    </div>
  )
}
```

## File: `components/transactions/new.tsx`
```tsx
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { getCurrentUser } from "@/lib/auth"
import { getCategories } from "@/models/categories"
import { getCurrencies } from "@/models/currencies"
import { getProjects } from "@/models/projects"
import { getSettings } from "@/models/settings"
import { Button } from "../ui/button"
import TransactionCreateForm from "./create"

export async function NewTransactionDialog({ children }: { children: React.ReactNode }) {
  const user = await getCurrentUser()
  const categories = await getCategories(user.id)
  const currencies = await getCurrencies(user.id)
  const settings = await getSettings(user.id)
  const projects = await getProjects(user.id)

  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button>{children}</Button>
      </DialogTrigger>
      <DialogContent className="max-w-xl">
        <DialogHeader>
          <DialogTitle className="text-2xl font-bold">New Transaction</DialogTitle>
          <DialogDescription>Create a new transaction</DialogDescription>
        </DialogHeader>

        <TransactionCreateForm
          categories={categories}
          currencies={currencies}
          settings={settings}
          projects={projects}
        />
      </DialogContent>
    </Dialog>
  )
}
```

## File: `components/transactions/pagination.tsx`
```tsx
"use client"

import {
  PaginationContent,
  PaginationEllipsis,
  PaginationItem,
  PaginationLink,
  Pagination as PaginationRoot,
} from "@/components/ui/pagination"
import { useRouter, useSearchParams } from "next/navigation"

const MAX_VISIBLE_PAGES = 5

export function Pagination({ totalItems, itemsPerPage = 1000 }: { totalItems: number; itemsPerPage: number }) {
  const router = useRouter()
  const searchParams = useSearchParams()

  const totalPages = Math.ceil(totalItems / itemsPerPage)
  const currentPage = parseInt(searchParams.get("page") || "1")

  const onPageChange = (page: number) => {
    const params = new URLSearchParams(searchParams.toString())
    params.set("page", page.toString())
    router.push(`?${params.toString()}`)
  }

  const getPageNumbers = () => {
    const pageNumbers = []

    // Show all page numbers if total pages is small
    if (totalPages <= MAX_VISIBLE_PAGES) {
      for (let i = 1; i <= totalPages; i++) {
        pageNumbers.push(i)
      }
    } else {
      // Always include the first page
      pageNumbers.push(1)

      // Calculate the range around the current page
      let startPage = Math.max(2, currentPage - 1)
      let endPage = Math.min(totalPages - 1, currentPage + 1)

      // Adjust if we're near the start
      if (currentPage <= 3) {
        endPage = Math.min(totalPages - 1, 4)
      }

      // Adjust if we're near the end
      if (currentPage >= totalPages - 2) {
        startPage = Math.max(2, totalPages - 3)
      }

      // Add ellipsis after first page if needed
      if (startPage > 2) {
        pageNumbers.push("ellipsis-start")
      }

      // Add middle page numbers
      for (let i = startPage; i <= endPage; i++) {
        pageNumbers.push(i)
      }

      // Add ellipsis before last page if needed
      if (endPage < totalPages - 1) {
        pageNumbers.push("ellipsis-end")
      }

      // Always include the last page
      pageNumbers.push(totalPages)
    }

    return pageNumbers
  }

  return (
    <div className="flex justify-center w-full mt-4">
      <PaginationRoot>
        <PaginationContent>
          {/* <PaginationItem>
            <PaginationPrevious
              onClick={() => currentPage > 1 && onPageChange(currentPage - 1)}
              className={currentPage <= 1 ? "pointer-events-none opacity-50" : "cursor-pointer"}
            />
          </PaginationItem> */}

          {getPageNumbers().map((pageNumber, index) =>
            pageNumber === "ellipsis-start" || pageNumber === "ellipsis-end" ? (
              <PaginationItem key={`ellipsis-${index}`}>
                <PaginationEllipsis />
              </PaginationItem>
            ) : (
              <PaginationItem key={pageNumber}>
                <PaginationLink
                  isActive={currentPage === pageNumber}
                  onClick={() => onPageChange(pageNumber as number)}
                  className="cursor-pointer"
                >
                  {pageNumber}
                </PaginationLink>
              </PaginationItem>
            )
          )}

          {/* <PaginationItem>
            <PaginationNext
              onClick={() => currentPage < totalPages && onPageChange(currentPage + 1)}
              className={currentPage >= totalPages ? "pointer-events-none opacity-50" : "cursor-pointer"}
            />
          </PaginationItem> */}
        </PaginationContent>
      </PaginationRoot>
    </div>
  )
}
```

## File: `components/transactions/transaction-files.tsx`
```tsx
"use client"

import { deleteTransactionFileAction, uploadTransactionFilesAction } from "@/app/(app)/transactions/actions"
import { FilePreview } from "@/components/files/preview"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"
import config from "@/lib/config"
import { File, Transaction } from "@/prisma/client"
import { Loader2, Upload, X } from "lucide-react"
import { useState } from "react"

export default function TransactionFiles({ transaction, files }: { transaction: Transaction; files: File[] }) {
  const [isUploading, setIsUploading] = useState(false)

  const handleDeleteFile = async (fileId: string) => {
    await deleteTransactionFileAction(transaction.id, fileId)
  }

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    setIsUploading(true)
    if (e.target.files && e.target.files.length > 0) {
      const formData = new FormData()
      formData.append("transactionId", transaction.id)
      for (let i = 0; i < e.target.files.length; i++) {
        formData.append("files", e.target.files[i])
      }
      await uploadTransactionFilesAction(formData)
      setIsUploading(false)
    }
  }

  return (
    <>
      {files.map((file) => (
        <Card key={file.id} className="p-4 relative">
          <Button
            type="button"
            onClick={() => handleDeleteFile(file.id)}
            variant="destructive"
            size="icon"
            className="absolute -right-2 -top-2 rounded-full w-6 h-6 z-10"
          >
            <X className="h-4 w-4" />
          </Button>
          <FilePreview file={file} />
        </Card>
      ))}

      <Card className="relative min-h-32 p-4">
        <input type="hidden" name="transactionId" value={transaction.id} />
        <label
          className="h-full w-full flex flex-col gap-2 items-center justify-center p-4 border-2 border-dashed border-gray-300 rounded-lg cursor-pointer hover:border-primary transition-colors"
          onDragEnter={(e) => {
            e.currentTarget.classList.add("border-primary")
          }}
          onDragLeave={(e) => {
            e.currentTarget.classList.remove("border-primary")
          }}
        >
          {isUploading ? (
            <Loader2 className="w-8 h-8 text-gray-400 animate-spin" />
          ) : (
            <>
              <Upload className="w-8 h-8 text-gray-400" />
              <p className="text-sm text-gray-500">Add more files to this invoice</p>
              <p className="text-xs text-gray-500">(or just drop them on this page)</p>
            </>
          )}
          <input
            multiple
            type="file"
            name="file"
            className="absolute inset-0 top-0 left-0 w-full h-full opacity-0"
            onChange={handleFileChange}
            accept={config.upload.acceptedMimeTypes}
          />
        </label>
      </Card>
    </>
  )
}
```

## File: `components/ui/alert.tsx`
```tsx
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const alertVariants = cva(
  "relative w-full rounded-lg border px-4 py-3 text-sm [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4 [&>svg]:text-foreground [&>svg~*]:pl-7",
  {
    variants: {
      variant: {
        default: "bg-background text-foreground",
        destructive:
          "border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

const Alert = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement> & VariantProps<typeof alertVariants>
>(({ className, variant, ...props }, ref) => (
  <div
    ref={ref}
    role="alert"
    className={cn(alertVariants({ variant }), className)}
    {...props}
  />
))
Alert.displayName = "Alert"

const AlertTitle = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLHeadingElement>
>(({ className, ...props }, ref) => (
  <h5
    ref={ref}
    className={cn("mb-1 font-medium leading-none tracking-tight", className)}
    {...props}
  />
))
AlertTitle.displayName = "AlertTitle"

const AlertDescription = React.forwardRef<
  HTMLParagraphElement,
  React.HTMLAttributes<HTMLParagraphElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm [&_p]:leading-relaxed", className)}
    {...props}
  />
))
AlertDescription.displayName = "AlertDescription"

export { Alert, AlertTitle, AlertDescription }
```

## File: `components/ui/avatar.tsx`
```tsx
"use client"

import * as React from "react"
import * as AvatarPrimitive from "@radix-ui/react-avatar"

import { cn } from "@/lib/utils"

const Avatar = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Root>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Root
    ref={ref}
    className={cn(
      "relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full",
      className
    )}
    {...props}
  />
))
Avatar.displayName = AvatarPrimitive.Root.displayName

const AvatarImage = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Image>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Image>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Image
    ref={ref}
    className={cn("aspect-square h-full w-full", className)}
    {...props}
  />
))
AvatarImage.displayName = AvatarPrimitive.Image.displayName

const AvatarFallback = React.forwardRef<
  React.ElementRef<typeof AvatarPrimitive.Fallback>,
  React.ComponentPropsWithoutRef<typeof AvatarPrimitive.Fallback>
>(({ className, ...props }, ref) => (
  <AvatarPrimitive.Fallback
    ref={ref}
    className={cn(
      "flex h-full w-full items-center justify-center rounded-full bg-muted",
      className
    )}
    {...props}
  />
))
AvatarFallback.displayName = AvatarPrimitive.Fallback.displayName

export { Avatar, AvatarImage, AvatarFallback }
```

## File: `components/ui/badge.tsx`
```tsx
import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const badgeVariants = cva(
  "inline-flex items-center rounded-md border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2",
  {
    variants: {
      variant: {
        default:
          "border-transparent bg-primary text-primary-foreground shadow hover:bg-primary/80",
        secondary:
          "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
        destructive:
          "border-transparent bg-destructive text-destructive-foreground shadow hover:bg-destructive/80",
        outline: "text-foreground",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface BadgeProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof badgeVariants> {}

function Badge({ className, variant, ...props }: BadgeProps) {
  return (
    <div className={cn(badgeVariants({ variant }), className)} {...props} />
  )
}

export { Badge, badgeVariants }
```

## File: `components/ui/breadcrumb.tsx`
```tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { ChevronRight, MoreHorizontal } from "lucide-react"

import { cn } from "@/lib/utils"

const Breadcrumb = React.forwardRef<
  HTMLElement,
  React.ComponentPropsWithoutRef<"nav"> & {
    separator?: React.ReactNode
  }
>(({ ...props }, ref) => <nav ref={ref} aria-label="breadcrumb" {...props} />)
Breadcrumb.displayName = "Breadcrumb"

const BreadcrumbList = React.forwardRef<
  HTMLOListElement,
  React.ComponentPropsWithoutRef<"ol">
>(({ className, ...props }, ref) => (
  <ol
    ref={ref}
    className={cn(
      "flex flex-wrap items-center gap-1.5 break-words text-sm text-muted-foreground sm:gap-2.5",
      className
    )}
    {...props}
  />
))
BreadcrumbList.displayName = "BreadcrumbList"

const BreadcrumbItem = React.forwardRef<
  HTMLLIElement,
  React.ComponentPropsWithoutRef<"li">
>(({ className, ...props }, ref) => (
  <li
    ref={ref}
    className={cn("inline-flex items-center gap-1.5", className)}
    {...props}
  />
))
BreadcrumbItem.displayName = "BreadcrumbItem"

const BreadcrumbLink = React.forwardRef<
  HTMLAnchorElement,
  React.ComponentPropsWithoutRef<"a"> & {
    asChild?: boolean
  }
>(({ asChild, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "a"

  return (
    <Comp
      ref={ref}
      className={cn("transition-colors hover:text-foreground", className)}
      {...props}
    />
  )
})
BreadcrumbLink.displayName = "BreadcrumbLink"

const BreadcrumbPage = React.forwardRef<
  HTMLSpanElement,
  React.ComponentPropsWithoutRef<"span">
>(({ className, ...props }, ref) => (
  <span
    ref={ref}
    role="link"
    aria-disabled="true"
    aria-current="page"
    className={cn("font-normal text-foreground", className)}
    {...props}
  />
))
BreadcrumbPage.displayName = "BreadcrumbPage"

const BreadcrumbSeparator = ({
  children,
  className,
  ...props
}: React.ComponentProps<"li">) => (
  <li
    role="presentation"
    aria-hidden="true"
    className={cn("[&>svg]:w-3.5 [&>svg]:h-3.5", className)}
    {...props}
  >
    {children ?? <ChevronRight />}
  </li>
)
BreadcrumbSeparator.displayName = "BreadcrumbSeparator"

const BreadcrumbEllipsis = ({
  className,
  ...props
}: React.ComponentProps<"span">) => (
  <span
    role="presentation"
    aria-hidden="true"
    className={cn("flex h-9 w-9 items-center justify-center", className)}
    {...props}
  >
    <MoreHorizontal className="h-4 w-4" />
    <span className="sr-only">More</span>
  </span>
)
BreadcrumbEllipsis.displayName = "BreadcrumbElipssis"

export {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
  BreadcrumbEllipsis,
}
```

## File: `components/ui/button.tsx`
```tsx
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
  {
    variants: {
      variant: {
        default:
          "bg-primary text-primary-foreground shadow hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground shadow-sm hover:bg-destructive/90",
        outline:
          "border border-input bg-background shadow-sm hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground shadow-sm hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-9 px-4 py-2",
        sm: "h-8 rounded-md px-3 text-xs",
        lg: "h-10 rounded-md px-8",
        icon: "h-9 w-9",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
Button.displayName = "Button"

export { Button, buttonVariants }
```

## File: `components/ui/calendar.tsx`
```tsx
"use client"

import * as React from "react"
import { ChevronLeft, ChevronRight } from "lucide-react"
import { DayPicker } from "react-day-picker"

import { cn } from "@/lib/utils"
import { buttonVariants } from "@/components/ui/button"

export type CalendarProps = React.ComponentProps<typeof DayPicker>

function Calendar({
  className,
  classNames,
  showOutsideDays = true,
  ...props
}: CalendarProps) {
  return (
    <DayPicker
      showOutsideDays={showOutsideDays}
      className={cn("p-3", className)}
      classNames={{
        months: "flex flex-col sm:flex-row space-y-4 sm:space-x-4 sm:space-y-0",
        month: "space-y-4",
        caption: "flex justify-center pt-1 relative items-center",
        caption_label: "text-sm font-medium",
        nav: "space-x-1 flex items-center",
        nav_button: cn(
          buttonVariants({ variant: "outline" }),
          "h-7 w-7 bg-transparent p-0 opacity-50 hover:opacity-100"
        ),
        nav_button_previous: "absolute left-1",
        nav_button_next: "absolute right-1",
        table: "w-full border-collapse space-y-1",
        head_row: "flex",
        head_cell:
          "text-muted-foreground rounded-md w-8 font-normal text-[0.8rem]",
        row: "flex w-full mt-2",
        cell: cn(
          "relative p-0 text-center text-sm focus-within:relative focus-within:z-20 [&:has([aria-selected])]:bg-accent [&:has([aria-selected].day-outside)]:bg-accent/50 [&:has([aria-selected].day-range-end)]:rounded-r-md",
          props.mode === "range"
            ? "[&:has(>.day-range-end)]:rounded-r-md [&:has(>.day-range-start)]:rounded-l-md first:[&:has([aria-selected])]:rounded-l-md last:[&:has([aria-selected])]:rounded-r-md"
            : "[&:has([aria-selected])]:rounded-md"
        ),
        day: cn(
          buttonVariants({ variant: "ghost" }),
          "h-8 w-8 p-0 font-normal aria-selected:opacity-100"
        ),
        day_range_start: "day-range-start",
        day_range_end: "day-range-end",
        day_selected:
          "bg-primary text-primary-foreground hover:bg-primary hover:text-primary-foreground focus:bg-primary focus:text-primary-foreground",
        day_today: "bg-accent text-accent-foreground",
        day_outside:
          "day-outside text-muted-foreground aria-selected:bg-accent/50 aria-selected:text-muted-foreground",
        day_disabled: "text-muted-foreground opacity-50",
        day_range_middle:
          "aria-selected:bg-accent aria-selected:text-accent-foreground",
        day_hidden: "invisible",
        ...classNames,
      }}
      components={{
        IconLeft: ({ className, ...props }) => (
          <ChevronLeft className={cn("h-4 w-4", className)} {...props} />
        ),
        IconRight: ({ className, ...props }) => (
          <ChevronRight className={cn("h-4 w-4", className)} {...props} />
        ),
      }}
      {...props}
    />
  )
}
Calendar.displayName = "Calendar"

export { Calendar }
```

## File: `components/ui/card.tsx`
```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

const Card = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn(
      "rounded-xl border bg-card text-card-foreground shadow",
      className
    )}
    {...props}
  />
))
Card.displayName = "Card"

const CardHeader = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex flex-col space-y-1.5 p-6", className)}
    {...props}
  />
))
CardHeader.displayName = "CardHeader"

const CardTitle = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("font-semibold leading-none tracking-tight", className)}
    {...props}
  />
))
CardTitle.displayName = "CardTitle"

const CardDescription = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

const CardContent = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div ref={ref} className={cn("p-6 pt-0", className)} {...props} />
))
CardContent.displayName = "CardContent"

const CardFooter = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <div
    ref={ref}
    className={cn("flex items-center p-6 pt-0", className)}
    {...props}
  />
))
CardFooter.displayName = "CardFooter"

export { Card, CardHeader, CardFooter, CardTitle, CardDescription, CardContent }
```

## File: `components/ui/checkbox.tsx`
```tsx
"use client"

import * as CheckboxPrimitive from "@radix-ui/react-checkbox"
import { Check } from "lucide-react"
import * as React from "react"

import { cn } from "@/lib/utils"

const Checkbox = React.forwardRef<
  React.ElementRef<typeof CheckboxPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof CheckboxPrimitive.Root>
>(({ className, ...props }, ref) => (
  <CheckboxPrimitive.Root
    ref={ref}
    className={cn(
      "flex peer size-4 justify-center items-center shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground",
      className
    )}
    {...props}
  >
    <CheckboxPrimitive.Indicator className={cn("flex items-center justify-center text-current")}>
      <Check className="h-4 w-4" />
    </CheckboxPrimitive.Indicator>
  </CheckboxPrimitive.Root>
))
Checkbox.displayName = CheckboxPrimitive.Root.displayName

export { Checkbox }
```

## File: `components/ui/collapsible.tsx`
```tsx
"use client"

import * as CollapsiblePrimitive from "@radix-ui/react-collapsible"

const Collapsible = CollapsiblePrimitive.Root

const CollapsibleTrigger = CollapsiblePrimitive.CollapsibleTrigger

const CollapsibleContent = CollapsiblePrimitive.CollapsibleContent

export { Collapsible, CollapsibleTrigger, CollapsibleContent }
```

## File: `components/ui/colored-text.tsx`
```tsx
import { cn } from "@/lib/utils"

export function ColoredText({
  children,
  className,
}: { children: React.ReactNode } & React.HTMLAttributes<HTMLSpanElement>) {
  return (
    <span className={cn("bg-gradient-to-r from-pink-600 to-indigo-600 bg-clip-text text-transparent", className)}>
      {children}
    </span>
  )
}
```

## File: `components/ui/dialog.tsx`
```tsx
"use client"

import * as React from "react"
import * as DialogPrimitive from "@radix-ui/react-dialog"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const Dialog = DialogPrimitive.Root

const DialogTrigger = DialogPrimitive.Trigger

const DialogPortal = DialogPrimitive.Portal

const DialogClose = DialogPrimitive.Close

const DialogOverlay = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Overlay
    ref={ref}
    className={cn(
      "fixed inset-0 z-50 bg-black/80  data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
  />
))
DialogOverlay.displayName = DialogPrimitive.Overlay.displayName

const DialogContent = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Content>
>(({ className, children, ...props }, ref) => (
  <DialogPortal>
    <DialogOverlay />
    <DialogPrimitive.Content
      ref={ref}
      className={cn(
        "fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg",
        className
      )}
      {...props}
    >
      {children}
      <DialogPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </DialogPrimitive.Close>
    </DialogPrimitive.Content>
  </DialogPortal>
))
DialogContent.displayName = DialogPrimitive.Content.displayName

const DialogHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-1.5 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
DialogHeader.displayName = "DialogHeader"

const DialogFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
DialogFooter.displayName = "DialogFooter"

const DialogTitle = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Title>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Title
    ref={ref}
    className={cn(
      "text-lg font-semibold leading-none tracking-tight",
      className
    )}
    {...props}
  />
))
DialogTitle.displayName = DialogPrimitive.Title.displayName

const DialogDescription = React.forwardRef<
  React.ElementRef<typeof DialogPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof DialogPrimitive.Description>
>(({ className, ...props }, ref) => (
  <DialogPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
DialogDescription.displayName = DialogPrimitive.Description.displayName

export {
  Dialog,
  DialogPortal,
  DialogOverlay,
  DialogTrigger,
  DialogClose,
  DialogContent,
  DialogHeader,
  DialogFooter,
  DialogTitle,
  DialogDescription,
}
```

## File: `components/ui/dropdown-menu.tsx`
```tsx
"use client"

import * as DropdownMenuPrimitive from "@radix-ui/react-dropdown-menu"
import { Check, ChevronRight, Circle } from "lucide-react"
import * as React from "react"

import { cn } from "@/lib/utils"

const DropdownMenu = DropdownMenuPrimitive.Root

const DropdownMenuTrigger = DropdownMenuPrimitive.Trigger

const DropdownMenuGroup = DropdownMenuPrimitive.Group

const DropdownMenuPortal = DropdownMenuPrimitive.Portal

const DropdownMenuSub = DropdownMenuPrimitive.Sub

const DropdownMenuRadioGroup = DropdownMenuPrimitive.RadioGroup

const DropdownMenuSubTrigger = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubTrigger>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubTrigger> & {
    inset?: boolean
  }
>(({ className, inset, children, ...props }, ref) => (
  <DropdownMenuPrimitive.SubTrigger
    ref={ref}
    className={cn(
      "flex cursor-default gap-2 select-none items-center rounded-sm px-2 py-1.5 text-sm outline-none focus:bg-accent data-[state=open]:bg-accent [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0",
      inset && "pl-8",
      className
    )}
    {...props}
  >
    {children}
    <ChevronRight className="ml-auto" />
  </DropdownMenuPrimitive.SubTrigger>
))
DropdownMenuSubTrigger.displayName = DropdownMenuPrimitive.SubTrigger.displayName

const DropdownMenuSubContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.SubContent>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.SubContent>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.SubContent
    ref={ref}
    className={cn(
      "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-lg data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
      className
    )}
    {...props}
  />
))
DropdownMenuSubContent.displayName = DropdownMenuPrimitive.SubContent.displayName

const DropdownMenuContent = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <DropdownMenuPrimitive.Portal>
    <DropdownMenuPrimitive.Content
      ref={ref}
      sideOffset={sideOffset}
      className={cn(
        "z-50 min-w-[8rem] overflow-hidden rounded-md border bg-popover p-1 text-popover-foreground shadow-md",
        "data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className
      )}
      {...props}
    />
  </DropdownMenuPrimitive.Portal>
))
DropdownMenuContent.displayName = DropdownMenuPrimitive.Content.displayName

const DropdownMenuItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Item> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center gap-2 rounded-sm px-2 py-1.5 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50 [&>svg]:size-4 [&>svg]:shrink-0",
      inset && "pl-8",
      className
    )}
    {...props}
  />
))
DropdownMenuItem.displayName = DropdownMenuPrimitive.Item.displayName

const DropdownMenuCheckboxItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.CheckboxItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.CheckboxItem>
>(({ className, children, checked, ...props }, ref) => (
  <DropdownMenuPrimitive.CheckboxItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    checked={checked}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.CheckboxItem>
))
DropdownMenuCheckboxItem.displayName = DropdownMenuPrimitive.CheckboxItem.displayName

const DropdownMenuRadioItem = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.RadioItem>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.RadioItem>
>(({ className, children, ...props }, ref) => (
  <DropdownMenuPrimitive.RadioItem
    ref={ref}
    className={cn(
      "relative flex cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none transition-colors focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
      <DropdownMenuPrimitive.ItemIndicator>
        <Circle className="h-2 w-2 fill-current" />
      </DropdownMenuPrimitive.ItemIndicator>
    </span>
    {children}
  </DropdownMenuPrimitive.RadioItem>
))
DropdownMenuRadioItem.displayName = DropdownMenuPrimitive.RadioItem.displayName

const DropdownMenuLabel = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Label> & {
    inset?: boolean
  }
>(({ className, inset, ...props }, ref) => (
  <DropdownMenuPrimitive.Label
    ref={ref}
    className={cn("px-2 py-1.5 text-sm font-semibold", inset && "pl-8", className)}
    {...props}
  />
))
DropdownMenuLabel.displayName = DropdownMenuPrimitive.Label.displayName

const DropdownMenuSeparator = React.forwardRef<
  React.ElementRef<typeof DropdownMenuPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof DropdownMenuPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <DropdownMenuPrimitive.Separator ref={ref} className={cn("-mx-1 my-1 h-px bg-muted", className)} {...props} />
))
DropdownMenuSeparator.displayName = DropdownMenuPrimitive.Separator.displayName

const DropdownMenuShortcut = ({ className, ...props }: React.HTMLAttributes<HTMLSpanElement>) => {
  return <span className={cn("ml-auto text-xs tracking-widest opacity-60", className)} {...props} />
}
DropdownMenuShortcut.displayName = "DropdownMenuShortcut"

export {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuPortal,
  DropdownMenuRadioGroup,
  DropdownMenuRadioItem,
  DropdownMenuSeparator,
  DropdownMenuShortcut,
  DropdownMenuSub,
  DropdownMenuSubContent,
  DropdownMenuSubTrigger,
  DropdownMenuTrigger,
}
```

## File: `components/ui/input.tsx`
```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

const Input = React.forwardRef<HTMLInputElement, React.ComponentProps<"input">>(
  ({ className, type, ...props }, ref) => {
    return (
      <input
        type={type}
        className={cn(
          "flex h-9 w-full rounded-md border border-input bg-transparent px-3 py-1 text-base shadow-sm transition-colors file:border-0 file:bg-transparent file:text-sm file:font-medium file:text-foreground placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
          className
        )}
        ref={ref}
        {...props}
      />
    )
  }
)
Input.displayName = "Input"

export { Input }
```

## File: `components/ui/label.tsx`
```tsx
"use client"

import * as React from "react"
import * as LabelPrimitive from "@radix-ui/react-label"
import { cva, type VariantProps } from "class-variance-authority"

import { cn } from "@/lib/utils"

const labelVariants = cva(
  "text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
)

const Label = React.forwardRef<
  React.ElementRef<typeof LabelPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof LabelPrimitive.Root> &
    VariantProps<typeof labelVariants>
>(({ className, ...props }, ref) => (
  <LabelPrimitive.Root
    ref={ref}
    className={cn(labelVariants(), className)}
    {...props}
  />
))
Label.displayName = LabelPrimitive.Root.displayName

export { Label }
```

## File: `components/ui/pagination.tsx`
```tsx
import * as React from "react"
import { ChevronLeft, ChevronRight, MoreHorizontal } from "lucide-react"

import { cn } from "@/lib/utils"
import { ButtonProps, buttonVariants } from "@/components/ui/button"

const Pagination = ({ className, ...props }: React.ComponentProps<"nav">) => (
  <nav
    role="navigation"
    aria-label="pagination"
    className={cn("mx-auto flex w-full justify-center", className)}
    {...props}
  />
)
Pagination.displayName = "Pagination"

const PaginationContent = React.forwardRef<
  HTMLUListElement,
  React.ComponentProps<"ul">
>(({ className, ...props }, ref) => (
  <ul
    ref={ref}
    className={cn("flex flex-row items-center gap-1", className)}
    {...props}
  />
))
PaginationContent.displayName = "PaginationContent"

const PaginationItem = React.forwardRef<
  HTMLLIElement,
  React.ComponentProps<"li">
>(({ className, ...props }, ref) => (
  <li ref={ref} className={cn("", className)} {...props} />
))
PaginationItem.displayName = "PaginationItem"

type PaginationLinkProps = {
  isActive?: boolean
} & Pick<ButtonProps, "size"> &
  React.ComponentProps<"a">

const PaginationLink = ({
  className,
  isActive,
  size = "icon",
  ...props
}: PaginationLinkProps) => (
  <a
    aria-current={isActive ? "page" : undefined}
    className={cn(
      buttonVariants({
        variant: isActive ? "outline" : "ghost",
        size,
      }),
      className
    )}
    {...props}
  />
)
PaginationLink.displayName = "PaginationLink"

const PaginationPrevious = ({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) => (
  <PaginationLink
    aria-label="Go to previous page"
    size="default"
    className={cn("gap-1 pl-2.5", className)}
    {...props}
  >
    <ChevronLeft className="h-4 w-4" />
    <span>Previous</span>
  </PaginationLink>
)
PaginationPrevious.displayName = "PaginationPrevious"

const PaginationNext = ({
  className,
  ...props
}: React.ComponentProps<typeof PaginationLink>) => (
  <PaginationLink
    aria-label="Go to next page"
    size="default"
    className={cn("gap-1 pr-2.5", className)}
    {...props}
  >
    <span>Next</span>
    <ChevronRight className="h-4 w-4" />
  </PaginationLink>
)
PaginationNext.displayName = "PaginationNext"

const PaginationEllipsis = ({
  className,
  ...props
}: React.ComponentProps<"span">) => (
  <span
    aria-hidden
    className={cn("flex h-9 w-9 items-center justify-center", className)}
    {...props}
  >
    <MoreHorizontal className="h-4 w-4" />
    <span className="sr-only">More pages</span>
  </span>
)
PaginationEllipsis.displayName = "PaginationEllipsis"

export {
  Pagination,
  PaginationContent,
  PaginationLink,
  PaginationItem,
  PaginationPrevious,
  PaginationNext,
  PaginationEllipsis,
}
```

## File: `components/ui/popover.tsx`
```tsx
"use client"

import * as React from "react"
import * as PopoverPrimitive from "@radix-ui/react-popover"

import { cn } from "@/lib/utils"

const Popover = PopoverPrimitive.Root

const PopoverTrigger = PopoverPrimitive.Trigger

const PopoverAnchor = PopoverPrimitive.Anchor

const PopoverContent = React.forwardRef<
  React.ElementRef<typeof PopoverPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof PopoverPrimitive.Content>
>(({ className, align = "center", sideOffset = 4, ...props }, ref) => (
  <PopoverPrimitive.Portal>
    <PopoverPrimitive.Content
      ref={ref}
      align={align}
      sideOffset={sideOffset}
      className={cn(
        "z-50 w-72 rounded-md border bg-popover p-4 text-popover-foreground shadow-md outline-none data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className
      )}
      {...props}
    />
  </PopoverPrimitive.Portal>
))
PopoverContent.displayName = PopoverPrimitive.Content.displayName

export { Popover, PopoverTrigger, PopoverContent, PopoverAnchor }
```

## File: `components/ui/resizable.tsx`
```tsx
"use client"

import { GripVertical } from "lucide-react"
import * as ResizablePrimitive from "react-resizable-panels"

import { cn } from "@/lib/utils"

const ResizablePanelGroup = ({
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelGroup>) => (
  <ResizablePrimitive.PanelGroup
    className={cn(
      "flex h-full w-full data-[panel-group-direction=vertical]:flex-col",
      className
    )}
    {...props}
  />
)

const ResizablePanel = ResizablePrimitive.Panel

const ResizableHandle = ({
  withHandle,
  className,
  ...props
}: React.ComponentProps<typeof ResizablePrimitive.PanelResizeHandle> & {
  withHandle?: boolean
}) => (
  <ResizablePrimitive.PanelResizeHandle
    className={cn(
      "relative flex w-px items-center justify-center bg-border after:absolute after:inset-y-0 after:left-1/2 after:w-1 after:-translate-x-1/2 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring focus-visible:ring-offset-1 data-[panel-group-direction=vertical]:h-px data-[panel-group-direction=vertical]:w-full data-[panel-group-direction=vertical]:after:left-0 data-[panel-group-direction=vertical]:after:h-1 data-[panel-group-direction=vertical]:after:w-full data-[panel-group-direction=vertical]:after:-translate-y-1/2 data-[panel-group-direction=vertical]:after:translate-x-0 [&[data-panel-group-direction=vertical]>div]:rotate-90",
      className
    )}
    {...props}
  >
    {withHandle && (
      <div className="z-10 flex h-4 w-3 items-center justify-center rounded-sm border bg-border">
        <GripVertical className="h-2.5 w-2.5" />
      </div>
    )}
  </ResizablePrimitive.PanelResizeHandle>
)

export { ResizablePanelGroup, ResizablePanel, ResizableHandle }
```

## File: `components/ui/select.tsx`
```tsx
"use client"

import * as React from "react"
import * as SelectPrimitive from "@radix-ui/react-select"
import { Check, ChevronDown, ChevronUp } from "lucide-react"

import { cn } from "@/lib/utils"

const Select = SelectPrimitive.Root

const SelectGroup = SelectPrimitive.Group

const SelectValue = SelectPrimitive.Value

const SelectTrigger = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Trigger>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Trigger>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Trigger
    ref={ref}
    className={cn(
      "flex h-9 w-full items-center justify-between whitespace-nowrap rounded-md border border-input bg-transparent px-3 py-2 text-sm shadow-sm ring-offset-background data-[placeholder]:text-muted-foreground focus:outline-none focus:ring-1 focus:ring-ring disabled:cursor-not-allowed disabled:opacity-50 [&>span]:line-clamp-1",
      className
    )}
    {...props}
  >
    {children}
    <SelectPrimitive.Icon asChild>
      <ChevronDown className="h-4 w-4 opacity-50" />
    </SelectPrimitive.Icon>
  </SelectPrimitive.Trigger>
))
SelectTrigger.displayName = SelectPrimitive.Trigger.displayName

const SelectScrollUpButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollUpButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollUpButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollUpButton
    ref={ref}
    className={cn(
      "flex cursor-default items-center justify-center py-1",
      className
    )}
    {...props}
  >
    <ChevronUp className="h-4 w-4" />
  </SelectPrimitive.ScrollUpButton>
))
SelectScrollUpButton.displayName = SelectPrimitive.ScrollUpButton.displayName

const SelectScrollDownButton = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.ScrollDownButton>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.ScrollDownButton>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.ScrollDownButton
    ref={ref}
    className={cn(
      "flex cursor-default items-center justify-center py-1",
      className
    )}
    {...props}
  >
    <ChevronDown className="h-4 w-4" />
  </SelectPrimitive.ScrollDownButton>
))
SelectScrollDownButton.displayName =
  SelectPrimitive.ScrollDownButton.displayName

const SelectContent = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Content>
>(({ className, children, position = "popper", ...props }, ref) => (
  <SelectPrimitive.Portal>
    <SelectPrimitive.Content
      ref={ref}
      className={cn(
        "relative z-50 max-h-96 min-w-[8rem] overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        position === "popper" &&
          "data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1",
        className
      )}
      position={position}
      {...props}
    >
      <SelectScrollUpButton />
      <SelectPrimitive.Viewport
        className={cn(
          "p-1",
          position === "popper" &&
            "h-[var(--radix-select-trigger-height)] w-full min-w-[var(--radix-select-trigger-width)]"
        )}
      >
        {children}
      </SelectPrimitive.Viewport>
      <SelectScrollDownButton />
    </SelectPrimitive.Content>
  </SelectPrimitive.Portal>
))
SelectContent.displayName = SelectPrimitive.Content.displayName

const SelectLabel = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Label>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Label>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Label
    ref={ref}
    className={cn("px-2 py-1.5 text-sm font-semibold", className)}
    {...props}
  />
))
SelectLabel.displayName = SelectPrimitive.Label.displayName

const SelectItem = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Item>
>(({ className, children, ...props }, ref) => (
  <SelectPrimitive.Item
    ref={ref}
    className={cn(
      "relative flex w-full cursor-default select-none items-center rounded-sm py-1.5 pl-2 pr-8 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
      className
    )}
    {...props}
  >
    <span className="absolute right-2 flex h-3.5 w-3.5 items-center justify-center">
      <SelectPrimitive.ItemIndicator>
        <Check className="h-4 w-4" />
      </SelectPrimitive.ItemIndicator>
    </span>
    <SelectPrimitive.ItemText>{children}</SelectPrimitive.ItemText>
  </SelectPrimitive.Item>
))
SelectItem.displayName = SelectPrimitive.Item.displayName

const SelectSeparator = React.forwardRef<
  React.ElementRef<typeof SelectPrimitive.Separator>,
  React.ComponentPropsWithoutRef<typeof SelectPrimitive.Separator>
>(({ className, ...props }, ref) => (
  <SelectPrimitive.Separator
    ref={ref}
    className={cn("-mx-1 my-1 h-px bg-muted", className)}
    {...props}
  />
))
SelectSeparator.displayName = SelectPrimitive.Separator.displayName

export {
  Select,
  SelectGroup,
  SelectValue,
  SelectTrigger,
  SelectContent,
  SelectLabel,
  SelectItem,
  SelectSeparator,
  SelectScrollUpButton,
  SelectScrollDownButton,
}
```

## File: `components/ui/separator.tsx`
```tsx
"use client"

import * as React from "react"
import * as SeparatorPrimitive from "@radix-ui/react-separator"

import { cn } from "@/lib/utils"

const Separator = React.forwardRef<
  React.ElementRef<typeof SeparatorPrimitive.Root>,
  React.ComponentPropsWithoutRef<typeof SeparatorPrimitive.Root>
>(
  (
    { className, orientation = "horizontal", decorative = true, ...props },
    ref
  ) => (
    <SeparatorPrimitive.Root
      ref={ref}
      decorative={decorative}
      orientation={orientation}
      className={cn(
        "shrink-0 bg-border",
        orientation === "horizontal" ? "h-[1px] w-full" : "h-full w-[1px]",
        className
      )}
      {...props}
    />
  )
)
Separator.displayName = SeparatorPrimitive.Root.displayName

export { Separator }
```

## File: `components/ui/sheet.tsx`
```tsx
"use client"

import * as React from "react"
import * as SheetPrimitive from "@radix-ui/react-dialog"
import { cva, type VariantProps } from "class-variance-authority"
import { X } from "lucide-react"

import { cn } from "@/lib/utils"

const Sheet = SheetPrimitive.Root

const SheetTrigger = SheetPrimitive.Trigger

const SheetClose = SheetPrimitive.Close

const SheetPortal = SheetPrimitive.Portal

const SheetOverlay = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Overlay>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Overlay>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Overlay
    className={cn(
      "fixed inset-0 z-50 bg-black/80  data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0",
      className
    )}
    {...props}
    ref={ref}
  />
))
SheetOverlay.displayName = SheetPrimitive.Overlay.displayName

const sheetVariants = cva(
  "fixed z-50 gap-4 bg-background p-6 shadow-lg transition ease-in-out data-[state=closed]:duration-300 data-[state=open]:duration-500 data-[state=open]:animate-in data-[state=closed]:animate-out",
  {
    variants: {
      side: {
        top: "inset-x-0 top-0 border-b data-[state=closed]:slide-out-to-top data-[state=open]:slide-in-from-top",
        bottom:
          "inset-x-0 bottom-0 border-t data-[state=closed]:slide-out-to-bottom data-[state=open]:slide-in-from-bottom",
        left: "inset-y-0 left-0 h-full w-3/4 border-r data-[state=closed]:slide-out-to-left data-[state=open]:slide-in-from-left sm:max-w-sm",
        right:
          "inset-y-0 right-0 h-full w-3/4 border-l data-[state=closed]:slide-out-to-right data-[state=open]:slide-in-from-right sm:max-w-sm",
      },
    },
    defaultVariants: {
      side: "right",
    },
  }
)

interface SheetContentProps
  extends React.ComponentPropsWithoutRef<typeof SheetPrimitive.Content>,
    VariantProps<typeof sheetVariants> {}

const SheetContent = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Content>,
  SheetContentProps
>(({ side = "right", className, children, ...props }, ref) => (
  <SheetPortal>
    <SheetOverlay />
    <SheetPrimitive.Content
      ref={ref}
      className={cn(sheetVariants({ side }), className)}
      {...props}
    >
      <SheetPrimitive.Close className="absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-secondary">
        <X className="h-4 w-4" />
        <span className="sr-only">Close</span>
      </SheetPrimitive.Close>
      {children}
    </SheetPrimitive.Content>
  </SheetPortal>
))
SheetContent.displayName = SheetPrimitive.Content.displayName

const SheetHeader = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col space-y-2 text-center sm:text-left",
      className
    )}
    {...props}
  />
)
SheetHeader.displayName = "SheetHeader"

const SheetFooter = ({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) => (
  <div
    className={cn(
      "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2",
      className
    )}
    {...props}
  />
)
SheetFooter.displayName = "SheetFooter"

const SheetTitle = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Title>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Title>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Title
    ref={ref}
    className={cn("text-lg font-semibold text-foreground", className)}
    {...props}
  />
))
SheetTitle.displayName = SheetPrimitive.Title.displayName

const SheetDescription = React.forwardRef<
  React.ElementRef<typeof SheetPrimitive.Description>,
  React.ComponentPropsWithoutRef<typeof SheetPrimitive.Description>
>(({ className, ...props }, ref) => (
  <SheetPrimitive.Description
    ref={ref}
    className={cn("text-sm text-muted-foreground", className)}
    {...props}
  />
))
SheetDescription.displayName = SheetPrimitive.Description.displayName

export {
  Sheet,
  SheetPortal,
  SheetOverlay,
  SheetTrigger,
  SheetClose,
  SheetContent,
  SheetHeader,
  SheetFooter,
  SheetTitle,
  SheetDescription,
}
```

## File: `components/ui/sidebar.tsx`
```tsx
"use client"

import { Slot } from "@radix-ui/react-slot"
import { VariantProps, cva } from "class-variance-authority"
import { PanelLeft } from "lucide-react"
import * as React from "react"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Separator } from "@/components/ui/separator"
import { Sheet, SheetContent, SheetTitle } from "@/components/ui/sheet"
import { Skeleton } from "@/components/ui/skeleton"
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip"
import { useIsMobile } from "@/hooks/use-mobile"
import { cn } from "@/lib/utils"

const SIDEBAR_COOKIE_NAME = "sidebar_state"
const SIDEBAR_COOKIE_MAX_AGE = 60 * 60 * 24 * 7
const SIDEBAR_WIDTH = "16rem"
const SIDEBAR_WIDTH_MOBILE = "18rem"
const SIDEBAR_WIDTH_ICON = "3rem"
const SIDEBAR_KEYBOARD_SHORTCUT = "b"

type SidebarContext = {
  state: "expanded" | "collapsed"
  open: boolean
  setOpen: (open: boolean) => void
  openMobile: boolean
  setOpenMobile: (open: boolean) => void
  isMobile: boolean
  toggleSidebar: () => void
}

const SidebarContext = React.createContext<SidebarContext | null>(null)

function useSidebar() {
  const context = React.useContext(SidebarContext)
  if (!context) {
    throw new Error("useSidebar must be used within a SidebarProvider.")
  }

  return context
}

const SidebarProvider = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    defaultOpen?: boolean
    open?: boolean
    onOpenChange?: (open: boolean) => void
  }
>(({ defaultOpen = true, open: openProp, onOpenChange: setOpenProp, className, style, children, ...props }, ref) => {
  const isMobile = useIsMobile()
  const [openMobile, setOpenMobile] = React.useState(false)

  // This is the internal state of the sidebar.
  // We use openProp and setOpenProp for control from outside the component.
  const [_open, _setOpen] = React.useState(defaultOpen)
  const open = openProp ?? _open
  const setOpen = React.useCallback(
    (value: boolean | ((value: boolean) => boolean)) => {
      const openState = typeof value === "function" ? value(open) : value
      if (setOpenProp) {
        setOpenProp(openState)
      } else {
        _setOpen(openState)
      }

      // This sets the cookie to keep the sidebar state.
      document.cookie = `${SIDEBAR_COOKIE_NAME}=${openState}; path=/; max-age=${SIDEBAR_COOKIE_MAX_AGE}`
    },
    [setOpenProp, open]
  )

  // Helper to toggle the sidebar.
  const toggleSidebar = React.useCallback(() => {
    return isMobile ? setOpenMobile((open) => !open) : setOpen((open) => !open)
  }, [isMobile, setOpen, setOpenMobile])

  // Adds a keyboard shortcut to toggle the sidebar.
  React.useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === SIDEBAR_KEYBOARD_SHORTCUT && (event.metaKey || event.ctrlKey)) {
        event.preventDefault()
        toggleSidebar()
      }
    }

    window.addEventListener("keydown", handleKeyDown)
    return () => window.removeEventListener("keydown", handleKeyDown)
  }, [toggleSidebar])

  // We add a state so that we can do data-state="expanded" or "collapsed".
  // This makes it easier to style the sidebar with Tailwind classes.
  const state = open ? "expanded" : "collapsed"

  const contextValue = React.useMemo<SidebarContext>(
    () => ({
      state,
      open,
      setOpen,
      isMobile,
      openMobile,
      setOpenMobile,
      toggleSidebar,
    }),
    [state, open, setOpen, isMobile, openMobile, setOpenMobile, toggleSidebar]
  )

  return (
    <SidebarContext.Provider value={contextValue}>
      <TooltipProvider delayDuration={0}>
        <div
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH,
              "--sidebar-width-icon": SIDEBAR_WIDTH_ICON,
              ...style,
            } as React.CSSProperties
          }
          className={cn("group/sidebar-wrapper flex min-h-svh w-full has-[[data-variant=inset]]:bg-sidebar", className)}
          ref={ref}
          {...props}
        >
          {children}
        </div>
      </TooltipProvider>
    </SidebarContext.Provider>
  )
})
SidebarProvider.displayName = "SidebarProvider"

const Sidebar = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    side?: "left" | "right"
    variant?: "sidebar" | "floating" | "inset"
    collapsible?: "offcanvas" | "icon" | "none"
  }
>(({ side = "left", variant = "sidebar", collapsible = "offcanvas", className, children, ...props }, ref) => {
  const { isMobile, state, openMobile, setOpenMobile } = useSidebar()

  if (collapsible === "none") {
    return (
      <div
        className={cn("flex h-full w-[--sidebar-width] flex-col bg-sidebar text-sidebar-foreground", className)}
        ref={ref}
        {...props}
      >
        {children}
      </div>
    )
  }

  if (isMobile) {
    return (
      <Sheet open={openMobile} onOpenChange={setOpenMobile} {...props}>
        <SheetTitle></SheetTitle>
        <SheetContent
          data-sidebar="sidebar"
          data-mobile="true"
          className="w-[--sidebar-width] bg-sidebar p-0 text-sidebar-foreground [&>button]:hidden"
          style={
            {
              "--sidebar-width": SIDEBAR_WIDTH_MOBILE,
            } as React.CSSProperties
          }
          side={side}
        >
          <div className="flex h-full w-full flex-col">{children}</div>
        </SheetContent>
      </Sheet>
    )
  }

  return (
    <div
      ref={ref}
      className="group peer hidden text-sidebar-foreground md:block"
      data-state={state}
      data-collapsible={state === "collapsed" ? collapsible : ""}
      data-variant={variant}
      data-side={side}
    >
      {/* This is what handles the sidebar gap on desktop */}
      <div
        className={cn(
          "relative h-svh w-[--sidebar-width] bg-transparent transition-[width] duration-200 ease-linear",
          "group-data-[collapsible=offcanvas]:w-0",
          "group-data-[side=right]:rotate-180",
          variant === "floating" || variant === "inset"
            ? "group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)_+_theme(spacing.4))]"
            : "group-data-[collapsible=icon]:w-[--sidebar-width-icon]"
        )}
      />
      <div
        className={cn(
          "fixed inset-y-0 z-10 hidden h-svh w-[--sidebar-width] transition-[left,right,width] duration-200 ease-linear md:flex",
          side === "left"
            ? "left-0 group-data-[collapsible=offcanvas]:left-[calc(var(--sidebar-width)*-1)]"
            : "right-0 group-data-[collapsible=offcanvas]:right-[calc(var(--sidebar-width)*-1)]",
          // Adjust the padding for floating and inset variants.
          variant === "floating" || variant === "inset"
            ? "p-2 group-data-[collapsible=icon]:w-[calc(var(--sidebar-width-icon)_+_theme(spacing.4)_+2px)]"
            : "group-data-[collapsible=icon]:w-[--sidebar-width-icon] group-data-[side=left]:border-r group-data-[side=right]:border-l",
          className
        )}
        {...props}
      >
        <div
          data-sidebar="sidebar"
          className="flex h-full w-full flex-col bg-sidebar group-data-[variant=floating]:rounded-lg group-data-[variant=floating]:border group-data-[variant=floating]:border-sidebar-border group-data-[variant=floating]:shadow"
        >
          {children}
        </div>
      </div>
    </div>
  )
})
Sidebar.displayName = "Sidebar"

const SidebarTrigger = React.forwardRef<React.ElementRef<typeof Button>, React.ComponentProps<typeof Button>>(
  ({ className, onClick, ...props }, ref) => {
    const { toggleSidebar } = useSidebar()

    return (
      <Button
        ref={ref}
        data-sidebar="trigger"
        variant="ghost"
        size="icon"
        className={cn("h-7 w-7", className)}
        onClick={(event) => {
          onClick?.(event)
          toggleSidebar()
        }}
        {...props}
      >
        <PanelLeft />
        <span className="sr-only">Toggle Sidebar</span>
      </Button>
    )
  }
)
SidebarTrigger.displayName = "SidebarTrigger"

const SidebarRail = React.forwardRef<HTMLButtonElement, React.ComponentProps<"button">>(
  ({ className, ...props }, ref) => {
    const { toggleSidebar } = useSidebar()

    return (
      <button
        ref={ref}
        data-sidebar="rail"
        aria-label="Toggle Sidebar"
        tabIndex={-1}
        onClick={toggleSidebar}
        title="Toggle Sidebar"
        className={cn(
          "absolute inset-y-0 z-20 hidden w-4 -translate-x-1/2 transition-all ease-linear after:absolute after:inset-y-0 after:left-1/2 after:w-[2px] hover:after:bg-sidebar-border group-data-[side=left]:-right-4 group-data-[side=right]:left-0 sm:flex",
          "[[data-side=left]_&]:cursor-w-resize [[data-side=right]_&]:cursor-e-resize",
          "[[data-side=left][data-state=collapsed]_&]:cursor-e-resize [[data-side=right][data-state=collapsed]_&]:cursor-w-resize",
          "group-data-[collapsible=offcanvas]:translate-x-0 group-data-[collapsible=offcanvas]:after:left-full group-data-[collapsible=offcanvas]:hover:bg-sidebar",
          "[[data-side=left][data-collapsible=offcanvas]_&]:-right-2",
          "[[data-side=right][data-collapsible=offcanvas]_&]:-left-2",
          className
        )}
        {...props}
      />
    )
  }
)
SidebarRail.displayName = "SidebarRail"

const SidebarInset = React.forwardRef<HTMLDivElement, React.ComponentProps<"main">>(({ className, ...props }, ref) => {
  return (
    <main
      ref={ref}
      className={cn(
        "relative flex min-h-svh flex-1 flex-col bg-background",
        "peer-data-[variant=inset]:min-h-[calc(100svh-theme(spacing.4))] md:peer-data-[variant=inset]:m-2 md:peer-data-[state=collapsed]:peer-data-[variant=inset]:ml-2 md:peer-data-[variant=inset]:ml-0 md:peer-data-[variant=inset]:rounded-xl md:peer-data-[variant=inset]:shadow",
        className
      )}
      {...props}
    />
  )
})
SidebarInset.displayName = "SidebarInset"

const SidebarInput = React.forwardRef<React.ElementRef<typeof Input>, React.ComponentProps<typeof Input>>(
  ({ className, ...props }, ref) => {
    return (
      <Input
        ref={ref}
        data-sidebar="input"
        className={cn(
          "h-8 w-full bg-background shadow-none focus-visible:ring-2 focus-visible:ring-sidebar-ring",
          className
        )}
        {...props}
      />
    )
  }
)
SidebarInput.displayName = "SidebarInput"

const SidebarHeader = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(({ className, ...props }, ref) => {
  return <div ref={ref} data-sidebar="header" className={cn("flex flex-col gap-2 p-2", className)} {...props} />
})
SidebarHeader.displayName = "SidebarHeader"

const SidebarFooter = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(({ className, ...props }, ref) => {
  return <div ref={ref} data-sidebar="footer" className={cn("flex flex-col gap-2 p-2", className)} {...props} />
})
SidebarFooter.displayName = "SidebarFooter"

const SidebarSeparator = React.forwardRef<React.ElementRef<typeof Separator>, React.ComponentProps<typeof Separator>>(
  ({ className, ...props }, ref) => {
    return (
      <Separator
        ref={ref}
        data-sidebar="separator"
        className={cn("mx-2 w-auto bg-sidebar-border", className)}
        {...props}
      />
    )
  }
)
SidebarSeparator.displayName = "SidebarSeparator"

const SidebarContent = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(({ className, ...props }, ref) => {
  return (
    <div
      ref={ref}
      data-sidebar="content"
      className={cn(
        "flex min-h-0 flex-1 flex-col gap-2 overflow-auto group-data-[collapsible=icon]:overflow-hidden",
        className
      )}
      {...props}
    />
  )
})
SidebarContent.displayName = "SidebarContent"

const SidebarGroup = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(({ className, ...props }, ref) => {
  return (
    <div
      ref={ref}
      data-sidebar="group"
      className={cn("relative flex w-full min-w-0 flex-col p-2", className)}
      {...props}
    />
  )
})
SidebarGroup.displayName = "SidebarGroup"

const SidebarGroupLabel = React.forwardRef<HTMLDivElement, React.ComponentProps<"div"> & { asChild?: boolean }>(
  ({ className, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "div"

    return (
      <Comp
        ref={ref}
        data-sidebar="group-label"
        className={cn(
          "flex h-8 shrink-0 items-center rounded-md px-2 text-xs font-medium text-sidebar-foreground/70 outline-none ring-sidebar-ring transition-[margin,opa] duration-200 ease-linear focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
          "group-data-[collapsible=icon]:-mt-8 group-data-[collapsible=icon]:opacity-0",
          className
        )}
        {...props}
      />
    )
  }
)
SidebarGroupLabel.displayName = "SidebarGroupLabel"

const SidebarGroupAction = React.forwardRef<HTMLButtonElement, React.ComponentProps<"button"> & { asChild?: boolean }>(
  ({ className, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"

    return (
      <Comp
        ref={ref}
        data-sidebar="group-action"
        className={cn(
          "absolute right-3 top-3.5 flex aspect-square w-5 items-center justify-center rounded-md p-0 text-sidebar-foreground outline-none ring-sidebar-ring transition-transform hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 [&>svg]:size-4 [&>svg]:shrink-0",
          // Increases the hit area of the button on mobile.
          "after:absolute after:-inset-2 after:md:hidden",
          "group-data-[collapsible=icon]:hidden",
          className
        )}
        {...props}
      />
    )
  }
)
SidebarGroupAction.displayName = "SidebarGroupAction"

const SidebarGroupContent = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(
  ({ className, ...props }, ref) => (
    <div ref={ref} data-sidebar="group-content" className={cn("w-full text-sm", className)} {...props} />
  )
)
SidebarGroupContent.displayName = "SidebarGroupContent"

const SidebarMenu = React.forwardRef<HTMLUListElement, React.ComponentProps<"ul">>(({ className, ...props }, ref) => (
  <ul ref={ref} data-sidebar="menu" className={cn("flex w-full min-w-0 flex-col gap-1", className)} {...props} />
))
SidebarMenu.displayName = "SidebarMenu"

const SidebarMenuItem = React.forwardRef<HTMLLIElement, React.ComponentProps<"li">>(({ className, ...props }, ref) => (
  <li ref={ref} data-sidebar="menu-item" className={cn("group/menu-item relative", className)} {...props} />
))
SidebarMenuItem.displayName = "SidebarMenuItem"

const sidebarMenuButtonVariants = cva(
  "peer/menu-button flex w-full items-center gap-2 overflow-hidden rounded-md p-2 text-left text-sm outline-none ring-sidebar-ring transition-[width,height,padding] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 group-has-[[data-sidebar=menu-action]]/menu-item:pr-8 aria-disabled:pointer-events-none aria-disabled:opacity-50 data-[active=true]:bg-sidebar-accent data-[active=true]:font-medium data-[active=true]:text-sidebar-accent-foreground data-[state=open]:hover:bg-sidebar-accent data-[state=open]:hover:text-sidebar-accent-foreground group-data-[collapsible=icon]:!size-8 group-data-[collapsible=icon]:!p-2 [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0",
  {
    variants: {
      variant: {
        default: "hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
        outline:
          "bg-background shadow-[0_0_0_1px_hsl(var(--sidebar-border))] hover:bg-sidebar-accent hover:text-sidebar-accent-foreground hover:shadow-[0_0_0_1px_hsl(var(--sidebar-accent))]",
      },
      size: {
        default: "h-8 text-sm",
        sm: "h-7 text-xs",
        lg: "h-12 text-sm group-data-[collapsible=icon]:!p-0",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

const SidebarMenuButton = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<"button"> & {
    asChild?: boolean
    isActive?: boolean
    tooltip?: string | React.ComponentProps<typeof TooltipContent>
  } & VariantProps<typeof sidebarMenuButtonVariants>
>(({ asChild = false, isActive = false, variant = "default", size = "default", tooltip, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "button"
  const { isMobile, state } = useSidebar()

  const button = (
    <Comp
      ref={ref}
      data-sidebar="menu-button"
      data-size={size}
      data-active={isActive}
      className={cn(sidebarMenuButtonVariants({ variant, size }), className)}
      {...props}
    />
  )

  if (!tooltip) {
    return button
  }

  if (typeof tooltip === "string") {
    tooltip = {
      children: tooltip,
    }
  }

  return (
    <Tooltip>
      <TooltipTrigger asChild>{button}</TooltipTrigger>
      <TooltipContent side="right" align="center" hidden={state !== "collapsed" || isMobile} {...tooltip} />
    </Tooltip>
  )
})
SidebarMenuButton.displayName = "SidebarMenuButton"

const SidebarMenuAction = React.forwardRef<
  HTMLButtonElement,
  React.ComponentProps<"button"> & {
    asChild?: boolean
    showOnHover?: boolean
  }
>(({ className, asChild = false, showOnHover = false, ...props }, ref) => {
  const Comp = asChild ? Slot : "button"

  return (
    <Comp
      ref={ref}
      data-sidebar="menu-action"
      className={cn(
        "absolute right-1 top-1.5 flex aspect-square w-5 items-center justify-center rounded-md p-0 text-sidebar-foreground outline-none ring-sidebar-ring transition-transform hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 peer-hover/menu-button:text-sidebar-accent-foreground [&>svg]:size-4 [&>svg]:shrink-0",
        // Increases the hit area of the button on mobile.
        "after:absolute after:-inset-2 after:md:hidden",
        "peer-data-[size=sm]/menu-button:top-1",
        "peer-data-[size=default]/menu-button:top-1.5",
        "peer-data-[size=lg]/menu-button:top-2.5",
        "group-data-[collapsible=icon]:hidden",
        showOnHover &&
          "group-focus-within/menu-item:opacity-100 group-hover/menu-item:opacity-100 data-[state=open]:opacity-100 peer-data-[active=true]/menu-button:text-sidebar-accent-foreground md:opacity-0",
        className
      )}
      {...props}
    />
  )
})
SidebarMenuAction.displayName = "SidebarMenuAction"

const SidebarMenuBadge = React.forwardRef<HTMLDivElement, React.ComponentProps<"div">>(
  ({ className, ...props }, ref) => (
    <div
      ref={ref}
      data-sidebar="menu-badge"
      className={cn(
        "pointer-events-none absolute right-1 flex h-5 min-w-5 select-none items-center justify-center rounded-md px-1 text-xs font-medium tabular-nums text-sidebar-foreground",
        "peer-hover/menu-button:text-sidebar-accent-foreground peer-data-[active=true]/menu-button:text-sidebar-accent-foreground",
        "peer-data-[size=sm]/menu-button:top-1",
        "peer-data-[size=default]/menu-button:top-1.5",
        "peer-data-[size=lg]/menu-button:top-2.5",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
)
SidebarMenuBadge.displayName = "SidebarMenuBadge"

const SidebarMenuSkeleton = React.forwardRef<
  HTMLDivElement,
  React.ComponentProps<"div"> & {
    showIcon?: boolean
  }
>(({ className, showIcon = false, ...props }, ref) => {
  // Random width between 50 to 90%.
  const width = React.useMemo(() => {
    return `${Math.floor(Math.random() * 40) + 50}%`
  }, [])

  return (
    <div
      ref={ref}
      data-sidebar="menu-skeleton"
      className={cn("flex h-8 items-center gap-2 rounded-md px-2", className)}
      {...props}
    >
      {showIcon && <Skeleton className="size-4 rounded-md" data-sidebar="menu-skeleton-icon" />}
      <Skeleton
        className="h-4 max-w-[--skeleton-width] flex-1"
        data-sidebar="menu-skeleton-text"
        style={
          {
            "--skeleton-width": width,
          } as React.CSSProperties
        }
      />
    </div>
  )
})
SidebarMenuSkeleton.displayName = "SidebarMenuSkeleton"

const SidebarMenuSub = React.forwardRef<HTMLUListElement, React.ComponentProps<"ul">>(
  ({ className, ...props }, ref) => (
    <ul
      ref={ref}
      data-sidebar="menu-sub"
      className={cn(
        "mx-3.5 flex min-w-0 translate-x-px flex-col gap-1 border-l border-sidebar-border px-2.5 py-0.5",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
)
SidebarMenuSub.displayName = "SidebarMenuSub"

const SidebarMenuSubItem = React.forwardRef<HTMLLIElement, React.ComponentProps<"li">>(({ ...props }, ref) => (
  <li ref={ref} {...props} />
))
SidebarMenuSubItem.displayName = "SidebarMenuSubItem"

const SidebarMenuSubButton = React.forwardRef<
  HTMLAnchorElement,
  React.ComponentProps<"a"> & {
    asChild?: boolean
    size?: "sm" | "md"
    isActive?: boolean
  }
>(({ asChild = false, size = "md", isActive, className, ...props }, ref) => {
  const Comp = asChild ? Slot : "a"

  return (
    <Comp
      ref={ref}
      data-sidebar="menu-sub-button"
      data-size={size}
      data-active={isActive}
      className={cn(
        "flex h-7 min-w-0 -translate-x-px items-center gap-2 overflow-hidden rounded-md px-2 text-sidebar-foreground outline-none ring-sidebar-ring hover:bg-sidebar-accent hover:text-sidebar-accent-foreground focus-visible:ring-2 active:bg-sidebar-accent active:text-sidebar-accent-foreground disabled:pointer-events-none disabled:opacity-50 aria-disabled:pointer-events-none aria-disabled:opacity-50 [&>span:last-child]:truncate [&>svg]:size-4 [&>svg]:shrink-0 [&>svg]:text-sidebar-accent-foreground",
        "data-[active=true]:bg-sidebar-accent data-[active=true]:text-sidebar-accent-foreground",
        size === "sm" && "text-xs",
        size === "md" && "text-sm",
        "group-data-[collapsible=icon]:hidden",
        className
      )}
      {...props}
    />
  )
})
SidebarMenuSubButton.displayName = "SidebarMenuSubButton"

export {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupAction,
  SidebarGroupContent,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarInput,
  SidebarInset,
  SidebarMenu,
  SidebarMenuAction,
  SidebarMenuBadge,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarMenuSkeleton,
  SidebarMenuSub,
  SidebarMenuSubButton,
  SidebarMenuSubItem,
  SidebarProvider,
  SidebarRail,
  SidebarSeparator,
  SidebarTrigger,
  useSidebar,
}
```

## File: `components/ui/skeleton.tsx`
```tsx
import { cn } from "@/lib/utils"

function Skeleton({
  className,
  ...props
}: React.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      className={cn("animate-pulse rounded-md bg-primary/10", className)}
      {...props}
    />
  )
}

export { Skeleton }
```

## File: `components/ui/sonner.tsx`
```tsx
"use client"

import { useTheme } from "next-themes"
import { Toaster as Sonner } from "sonner"

type ToasterProps = React.ComponentProps<typeof Sonner>

const Toaster = ({ ...props }: ToasterProps) => {
  const { theme = "system" } = useTheme()

  return (
    <Sonner
      theme={theme as ToasterProps["theme"]}
      className="toaster group"
      toastOptions={{
        classNames: {
          toast:
            "group toast group-[.toaster]:bg-background group-[.toaster]:text-foreground group-[.toaster]:border-border group-[.toaster]:shadow-lg",
          description: "group-[.toast]:text-muted-foreground",
          actionButton:
            "group-[.toast]:bg-primary group-[.toast]:text-primary-foreground",
          cancelButton:
            "group-[.toast]:bg-muted group-[.toast]:text-muted-foreground",
        },
      }}
      {...props}
    />
  )
}

export { Toaster }
```

## File: `components/ui/table.tsx`
```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

const Table = React.forwardRef<
  HTMLTableElement,
  React.HTMLAttributes<HTMLTableElement>
>(({ className, ...props }, ref) => (
  <div className="relative w-full overflow-auto">
    <table
      ref={ref}
      className={cn("w-full caption-bottom text-sm", className)}
      {...props}
    />
  </div>
))
Table.displayName = "Table"

const TableHeader = React.forwardRef<
  HTMLTableSectionElement,
  React.HTMLAttributes<HTMLTableSectionElement>
>(({ className, ...props }, ref) => (
  <thead ref={ref} className={cn("[&_tr]:border-b", className)} {...props} />
))
TableHeader.displayName = "TableHeader"

const TableBody = React.forwardRef<
  HTMLTableSectionElement,
  React.HTMLAttributes<HTMLTableSectionElement>
>(({ className, ...props }, ref) => (
  <tbody
    ref={ref}
    className={cn("[&_tr:last-child]:border-0", className)}
    {...props}
  />
))
TableBody.displayName = "TableBody"

const TableFooter = React.forwardRef<
  HTMLTableSectionElement,
  React.HTMLAttributes<HTMLTableSectionElement>
>(({ className, ...props }, ref) => (
  <tfoot
    ref={ref}
    className={cn(
      "border-t bg-muted/50 font-medium [&>tr]:last:border-b-0",
      className
    )}
    {...props}
  />
))
TableFooter.displayName = "TableFooter"

const TableRow = React.forwardRef<
  HTMLTableRowElement,
  React.HTMLAttributes<HTMLTableRowElement>
>(({ className, ...props }, ref) => (
  <tr
    ref={ref}
    className={cn(
      "border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted",
      className
    )}
    {...props}
  />
))
TableRow.displayName = "TableRow"

const TableHead = React.forwardRef<
  HTMLTableCellElement,
  React.ThHTMLAttributes<HTMLTableCellElement>
>(({ className, ...props }, ref) => (
  <th
    ref={ref}
    className={cn(
      "h-10 px-2 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0 [&>[role=checkbox]]:translate-y-[2px]",
      className
    )}
    {...props}
  />
))
TableHead.displayName = "TableHead"

const TableCell = React.forwardRef<
  HTMLTableCellElement,
  React.TdHTMLAttributes<HTMLTableCellElement>
>(({ className, ...props }, ref) => (
  <td
    ref={ref}
    className={cn(
      "p-2 align-middle [&:has([role=checkbox])]:pr-0 [&>[role=checkbox]]:translate-y-[2px]",
      className
    )}
    {...props}
  />
))
TableCell.displayName = "TableCell"

const TableCaption = React.forwardRef<
  HTMLTableCaptionElement,
  React.HTMLAttributes<HTMLTableCaptionElement>
>(({ className, ...props }, ref) => (
  <caption
    ref={ref}
    className={cn("mt-4 text-sm text-muted-foreground", className)}
    {...props}
  />
))
TableCaption.displayName = "TableCaption"

export {
  Table,
  TableHeader,
  TableBody,
  TableFooter,
  TableHead,
  TableRow,
  TableCell,
  TableCaption,
}
```

## File: `components/ui/textarea.tsx`
```tsx
import * as React from "react"

import { cn } from "@/lib/utils"

const Textarea = React.forwardRef<
  HTMLTextAreaElement,
  React.ComponentProps<"textarea">
>(({ className, ...props }, ref) => {
  return (
    <textarea
      className={cn(
        "flex min-h-[60px] w-full rounded-md border border-input bg-transparent px-3 py-2 text-base shadow-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring disabled:cursor-not-allowed disabled:opacity-50 md:text-sm",
        className
      )}
      ref={ref}
      {...props}
    />
  )
})
Textarea.displayName = "Textarea"

export { Textarea }
```

## File: `components/ui/tooltip.tsx`
```tsx
"use client"

import * as React from "react"
import * as TooltipPrimitive from "@radix-ui/react-tooltip"

import { cn } from "@/lib/utils"

const TooltipProvider = TooltipPrimitive.Provider

const Tooltip = TooltipPrimitive.Root

const TooltipTrigger = TooltipPrimitive.Trigger

const TooltipContent = React.forwardRef<
  React.ElementRef<typeof TooltipPrimitive.Content>,
  React.ComponentPropsWithoutRef<typeof TooltipPrimitive.Content>
>(({ className, sideOffset = 4, ...props }, ref) => (
  <TooltipPrimitive.Portal>
    <TooltipPrimitive.Content
      ref={ref}
      sideOffset={sideOffset}
      className={cn(
        "z-50 overflow-hidden rounded-md bg-primary px-3 py-1.5 text-xs text-primary-foreground animate-in fade-in-0 zoom-in-95 data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2",
        className
      )}
      {...props}
    />
  </TooltipPrimitive.Portal>
))
TooltipContent.displayName = TooltipPrimitive.Content.displayName

export { Tooltip, TooltipTrigger, TooltipContent, TooltipProvider }
```

## File: `components/unsorted/analyze-all-button.tsx`
```tsx
"use client"

import { Button } from "@/components/ui/button"
import { Save, Swords } from "lucide-react"

export function AnalyzeAllButton() {
  const handleAnalyzeAll = () => {
    if (typeof document !== "undefined") {
      document.querySelectorAll("button[data-analyze-button]").forEach((button) => {
        ;(button as HTMLButtonElement).click()
      })
    }
  }

  const handleSaveAll = () => {
    if (typeof document !== "undefined") {
      document.querySelectorAll("button[data-save-button]").forEach((button) => {
        ;(button as HTMLButtonElement).click()
      })
    }
  }

  return (
    <div className="flex flex-row flex-wrap gap-2 justify-end">
      <Button variant="outline" className="flex items-center gap-2" onClick={handleSaveAll}>
        <Save className="h-4 w-4" />
        Save all
      </Button>
      <Button className="flex items-center gap-2" onClick={handleAnalyzeAll}>
        <Swords className="h-4 w-4" />
        Analyze all
      </Button>
    </div>
  )
}
```

## File: `components/unsorted/analyze-form.tsx`
```tsx
"use client"

import { useNotification } from "@/app/(app)/context"
import { analyzeFileAction, deleteUnsortedFileAction, saveFileAsTransactionAction } from "@/app/(app)/unsorted/actions"
import { CurrencyConverterTool } from "@/components/agents/currency-converter"
import { ItemsDetectTool } from "@/components/agents/items-detect"
import ToolWindow from "@/components/agents/tool-window"
import { FormError } from "@/components/forms/error"
import { FormSelectCategory } from "@/components/forms/select-category"
import { FormSelectCurrency } from "@/components/forms/select-currency"
import { FormSelectProject } from "@/components/forms/select-project"
import { FormSelectType } from "@/components/forms/select-type"
import { FormInput, FormTextarea } from "@/components/forms/simple"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Category, Currency, Field, File, Project } from "@/prisma/client"
import { format } from "date-fns"
import { ArrowDownToLine, Brain, Loader2, Trash2 } from "lucide-react"
import { startTransition, useActionState, useMemo, useState } from "react"

export default function AnalyzeForm({
  file,
  categories,
  projects,
  currencies,
  fields,
  settings,
}: {
  file: File
  categories: Category[]
  projects: Project[]
  currencies: Currency[]
  fields: Field[]
  settings: Record<string, string>
}) {
  const { showNotification } = useNotification()
  const [isAnalyzing, setIsAnalyzing] = useState(false)
  const [analyzeStep, setAnalyzeStep] = useState<string>("")
  const [analyzeError, setAnalyzeError] = useState<string>("")
  const [deleteState, deleteAction, isDeleting] = useActionState(deleteUnsortedFileAction, null)
  const [isSaving, setIsSaving] = useState(false)
  const [saveError, setSaveError] = useState("")

  const fieldMap = useMemo(() => {
    return fields.reduce(
      (acc, field) => {
        acc[field.code] = field
        return acc
      },
      {} as Record<string, Field>
    )
  }, [fields])

  const extraFields = useMemo(() => fields.filter((field) => field.isExtra), [fields])
  const initialFormState = useMemo(() => {
    const baseState = {
      name: file.filename,
      merchant: "",
      description: "",
      type: settings.default_type,
      total: 0.0,
      currencyCode: settings.default_currency,
      convertedTotal: 0.0,
      convertedCurrencyCode: settings.default_currency,
      categoryCode: settings.default_category,
      projectCode: settings.default_project,
      issuedAt: "",
      note: "",
      text: "",
      items: [],
    }

    // Add extra fields
    const extraFieldsState = extraFields.reduce(
      (acc, field) => {
        acc[field.code] = ""
        return acc
      },
      {} as Record<string, string>
    )

    // Load cached results if they exist
    const cachedResults = file.cachedParseResult
      ? Object.fromEntries(
          Object.entries(file.cachedParseResult as Record<string, string>).filter(
            ([_, value]) => value !== null && value !== undefined && value !== ""
          )
        )
      : {}

    return {
      ...baseState,
      ...extraFieldsState,
      ...cachedResults,
    }
  }, [file.filename, settings, extraFields, file.cachedParseResult])
  const [formData, setFormData] = useState(initialFormState)

  async function saveAsTransaction(formData: FormData) {
    setSaveError("")
    setIsSaving(true)
    startTransition(async () => {
      const result = await saveFileAsTransactionAction(null, formData)
      setIsSaving(false)

      if (result.success) {
        showNotification({ code: "global.banner", message: "Saved!", type: "success" })
        showNotification({ code: "sidebar.transactions", message: "new" })
        setTimeout(() => showNotification({ code: "sidebar.transactions", message: "" }), 3000)
      } else {
        setSaveError(result.error ? result.error : "Something went wrong...")
        showNotification({ code: "global.banner", message: "Failed to save", type: "failed" })
      }
    })
  }

  const startAnalyze = async () => {
    setIsAnalyzing(true)
    setAnalyzeError("")
    try {
      setAnalyzeStep("Analyzing...")
      const results = await analyzeFileAction(file, settings, fields, categories, projects)

      console.log("Analysis results:", results)

      if (!results.success) {
        setAnalyzeError(results.error ? results.error : "Something went wrong...")
      } else {
        const nonEmptyFields = Object.fromEntries(
          Object.entries(results.data?.output || {}).filter(
            ([_, value]) => value !== null && value !== undefined && value !== ""
          )
        )
        setFormData({ ...formData, ...nonEmptyFields })
      }
    } catch (error) {
      console.error("Analysis failed:", error)
      setAnalyzeError(error instanceof Error ? error.message : "Analysis failed")
    } finally {
      setIsAnalyzing(false)
      setAnalyzeStep("")
    }
  }

  return (
    <>
      {file.isSplitted ? (
        <div className="flex justify-end">
          <Badge variant="outline">This file has been split up</Badge>
        </div>
      ) : (
        <Button className="w-full mb-6 py-6 text-lg" onClick={startAnalyze} disabled={isAnalyzing} data-analyze-button>
          {isAnalyzing ? (
            <>
              <Loader2 className="mr-1 h-4 w-4 animate-spin" />
              <span>{analyzeStep}</span>
            </>
          ) : (
            <>
              <Brain className="mr-1 h-4 w-4" />
              <span>Analyze with AI</span>
            </>
          )}
        </Button>
      )}

      <div>{analyzeError && <FormError>{analyzeError}</FormError>}</div>

      <form className="space-y-4" action={saveAsTransaction}>
        <input type="hidden" name="fileId" value={file.id} />
        <FormInput
          title={fieldMap.name.name}
          name="name"
          value={formData.name}
          onChange={(e) => setFormData((prev) => ({ ...prev, name: e.target.value }))}
          required={fieldMap.name.isRequired}
        />

        <FormInput
          title={fieldMap.merchant.name}
          name="merchant"
          value={formData.merchant}
          onChange={(e) => setFormData((prev) => ({ ...prev, merchant: e.target.value }))}
          hideIfEmpty={!fieldMap.merchant.isVisibleInAnalysis}
          required={fieldMap.merchant.isRequired}
        />

        <FormInput
          title={fieldMap.description.name}
          name="description"
          value={formData.description}
          onChange={(e) => setFormData((prev) => ({ ...prev, description: e.target.value }))}
          hideIfEmpty={!fieldMap.description.isVisibleInAnalysis}
          required={fieldMap.description.isRequired}
        />

        <div className="flex flex-wrap gap-4">
          <FormInput
            title={fieldMap.total.name}
            name="total"
            type="number"
            step="0.01"
            value={formData.total || ""}
            onChange={(e) => {
              const newValue = parseFloat(e.target.value || "0")
              !isNaN(newValue) && setFormData((prev) => ({ ...prev, total: newValue }))
            }}
            className="w-32"
            required={fieldMap.total.isRequired}
          />

          <FormSelectCurrency
            title={fieldMap.currencyCode.name}
            currencies={currencies}
            name="currencyCode"
            value={formData.currencyCode}
            onValueChange={(value) => setFormData((prev) => ({ ...prev, currencyCode: value }))}
            hideIfEmpty={!fieldMap.currencyCode.isVisibleInAnalysis}
            required={fieldMap.currencyCode.isRequired}
          />

          <FormSelectType
            title={fieldMap.type.name}
            name="type"
            value={formData.type}
            onValueChange={(value) => setFormData((prev) => ({ ...prev, type: value }))}
            hideIfEmpty={!fieldMap.type.isVisibleInAnalysis}
            required={fieldMap.type.isRequired}
          />
        </div>

        {formData.total != 0 && formData.currencyCode && formData.currencyCode !== settings.default_currency && (
          <ToolWindow title={`Exchange rate on ${format(new Date(formData.issuedAt || Date.now()), "LLLL dd, yyyy")}`}>
            <CurrencyConverterTool
              originalTotal={formData.total}
              originalCurrencyCode={formData.currencyCode}
              targetCurrencyCode={settings.default_currency}
              date={new Date(formData.issuedAt || Date.now())}
              onChange={(value) => setFormData((prev) => ({ ...prev, convertedTotal: value }))}
            />
            <input type="hidden" name="convertedCurrencyCode" value={settings.default_currency} />
          </ToolWindow>
        )}

        <div className="flex flex-row gap-4">
          <FormInput
            title={fieldMap.issuedAt.name}
            type="date"
            name="issuedAt"
            value={formData.issuedAt}
            onChange={(e) => setFormData((prev) => ({ ...prev, issuedAt: e.target.value }))}
            hideIfEmpty={!fieldMap.issuedAt.isVisibleInAnalysis}
            required={fieldMap.issuedAt.isRequired}
          />
        </div>

        <div className="flex flex-row gap-4">
          <FormSelectCategory
            title={fieldMap.categoryCode.name}
            categories={categories}
            name="categoryCode"
            value={formData.categoryCode}
            onValueChange={(value) => setFormData((prev) => ({ ...prev, categoryCode: value }))}
            placeholder="Select Category"
            hideIfEmpty={!fieldMap.categoryCode.isVisibleInAnalysis}
            required={fieldMap.categoryCode.isRequired}
          />

          {projects.length > 0 && (
            <FormSelectProject
              title={fieldMap.projectCode.name}
              projects={projects}
              name="projectCode"
              value={formData.projectCode}
              onValueChange={(value) => setFormData((prev) => ({ ...prev, projectCode: value }))}
              placeholder="Select Project"
              hideIfEmpty={!fieldMap.projectCode.isVisibleInAnalysis}
              required={fieldMap.projectCode.isRequired}
            />
          )}
        </div>

        <FormInput
          title={fieldMap.note.name}
          name="note"
          value={formData.note}
          onChange={(e) => setFormData((prev) => ({ ...prev, note: e.target.value }))}
          hideIfEmpty={!fieldMap.note.isVisibleInAnalysis}
          required={fieldMap.note.isRequired}
        />

        {extraFields.map((field) => (
          <FormInput
            key={field.code}
            type="text"
            title={field.name}
            name={field.code}
            value={formData[field.code as keyof typeof formData]}
            onChange={(e) => setFormData((prev) => ({ ...prev, [field.code]: e.target.value }))}
            hideIfEmpty={!field.isVisibleInAnalysis}
            required={field.isRequired}
          />
        ))}

        {formData.items && formData.items.length > 0 && (
          <ToolWindow title="Detected items">
            <ItemsDetectTool file={file} data={formData} />
          </ToolWindow>
        )}

        <div className="hidden">
          <input type="text" name="items" value={JSON.stringify(formData.items)} readOnly />
          <FormTextarea
            title={fieldMap.text.name}
            name="text"
            value={formData.text}
            onChange={(e) => setFormData((prev) => ({ ...prev, text: e.target.value }))}
            hideIfEmpty={!fieldMap.text.isVisibleInAnalysis}
          />
        </div>

        <div className="flex justify-between gap-4 pt-6">
          <Button
            type="button"
            onClick={() => startTransition(() => deleteAction(file.id))}
            variant="destructive"
            disabled={isDeleting}
          >
            <Trash2 className="h-4 w-4" />
            {isDeleting ? "⏳ Deleting..." : "Delete"}
          </Button>

          <Button type="submit" disabled={isSaving} data-save-button>
            {isSaving ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Saving...
              </>
            ) : (
              <>
                <ArrowDownToLine className="h-4 w-4" />
                Save as Transaction
              </>
            )}
          </Button>
        </div>

        <div>
          {deleteState?.error && <FormError>{deleteState.error}</FormError>}
          {saveError && <FormError>{saveError}</FormError>}
        </div>
      </form>
    </>
  )
}
```

## File: `docs/migrate-0.3-0.5.md`
```markdown
# How to migrate data from v0.3 to v0.5

In v0.5 we changed the database from SQLite to Postgres. Because of this, it was not possible to seamlessly migrate data from one database to another and you will have to do it yourself.

Don't worry, even if you already upgraded — your data is not lost!

Here's how to migrate properly:

## Step 1: Update your docker-compose to v0.3.0

```yaml
services:
  app:
    image: ghcr.io/vas3k/taxhacker:v0.3.0
    ports:
      - "7331:7331"
      
// everything else stays the same
```

## Step 2: Restart your app and make a backup

```yaml
docker compose down
docker compose up -d
```

Go to your app -> Settings -> Backups -> Download Data Archive

Save .zip archive on your machine. 

## Step 3: Upgrade your TaxHacker instance

Update your docker compose to latest version again.

```yaml
services:
  app:
    image: ghcr.io/vas3k/taxhacker:latest
    ports:
      - "7331:7331"
      
// everything else stays the same
```

Restart again.

## Step 4: Upload your data to the new instance

Open your app -> Settings -> Backups -> Restore from a backup

Upload your zip archive and click restore. After couple of seconds it must show you import stats.

If import fails with an error about file size, go to [next.config.ts](./next.config.ts) and change `bodySizeLimit: "256mb"` to something bigger.
```

## File: `etc/nginx/taxhacker.app.conf`
```
server {
    listen 80;
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name taxhacker.app;

    charset utf-8;
    client_max_body_size 256M;

    set_real_ip_from 172.17.0.0/16;
    real_ip_header X-Forwarded-For;
    real_ip_recursive on;

    ssl_certificate     /home/vas3k/certs/pubkey.pem;
    ssl_certificate_key /home/vas3k/certs/privkey.pem;

    # Global security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header X-Frame-Options "DENY" always;
    add_header Permissions-Policy "accelerometer=(), camera=(), geolocation=(), gyroscope=(), magnetometer=(), microphone=(), payment=(), usb=()" always;
    add_header Content-Security-Policy "default-src 'self'; img-src 'self' data:; script-src 'self'; style-src 'self';" always;

    location / {
        # CORS headers (adjust if needed)
        add_header Access-Control-Allow-Origin "https://taxhacker.app";
        add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
        add_header Access-Control-Allow-Headers "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range";
        add_header Access-Control-Expose-Headers "Content-Length,Content-Range";

        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_redirect off;
        proxy_buffering off;

        proxy_pass http://127.0.0.1:7331;
    }
}
```

## File: `forms/settings.ts`
```typescript
import { randomHexColor } from "@/lib/utils"
import { z } from "zod"

export const settingsFormSchema = z.object({
  default_currency: z.string().max(5).optional(),
  default_type: z.string().optional(),
  default_category: z.string().optional(),
  default_project: z.string().optional(),
  openai_api_key: z.string().optional(),
  openai_model_name: z.string().default('gpt-4o-mini'),
  google_api_key: z.string().optional(),
  google_model_name: z.string().default("gemini-2.5-flash"),
  mistral_api_key: z.string().optional(),
  mistral_model_name: z.string().default("mistral-medium-latest"),
  llm_providers: z.string().default('openai,google,mistral'),
  prompt_analyse_new_file: z.string().optional(),
  is_welcome_message_hidden: z.string().optional(),
})

export const currencyFormSchema = z.object({
  code: z.string().max(5),
  name: z.string().max(32),
})

export const projectFormSchema = z.object({
  name: z.string().max(128),
  llm_prompt: z.string().max(512).nullable().optional(),
  color: z.string().max(7).default(randomHexColor()).nullable().optional(),
})

export const categoryFormSchema = z.object({
  name: z.string().max(128),
  llm_prompt: z.string().max(512).nullable().optional(),
  color: z.string().max(7).default(randomHexColor()).nullable().optional(),
})

export const fieldFormSchema = z.object({
  name: z.string().max(128),
  type: z.string().max(128).default("string"),
  llm_prompt: z.string().max(512).nullable().optional(),
  isVisibleInList: z.boolean().optional(),
  isVisibleInAnalysis: z.boolean().optional(),
  isRequired: z.boolean().optional(),
})
```

## File: `forms/transactions.ts`
```typescript
import { z } from "zod"

export const transactionFormSchema = z
  .object({
    name: z.string().max(128).optional(),
    merchant: z.string().max(128).optional(),
    description: z.string().max(256).optional(),
    type: z.string().optional(),
    total: z
      .string()
      .optional()
      .transform((val) => {
        if (!val || val.trim() === '') return null
        const num = parseFloat(val)
        if (isNaN(num)) {
          throw new z.ZodError([{ message: "Invalid total", path: ["total"], code: z.ZodIssueCode.custom }])
        }
        return Math.round(num * 100) // convert to cents
      }),
    currencyCode: z.string().max(5).optional(),
    convertedTotal: z
      .string()
      .optional()
      .transform((val) => {
        if (!val || val.trim() === '') return null
        const num = parseFloat(val)
        if (isNaN(num)) {
          throw new z.ZodError([
            { message: "Invalid coverted total", path: ["convertedTotal"], code: z.ZodIssueCode.custom },
          ])
        }
        return Math.round(num * 100) // convert to cents
      }),
    convertedCurrencyCode: z.string().max(5).optional(),
    categoryCode: z.string().optional(),
    projectCode: z.string().optional(),
    issuedAt: z
      .union([
        z.date(),
        z
          .string()
          .refine((val) => !isNaN(Date.parse(val)), {
            message: "Invalid date format",
          })
          .transform((val) => new Date(val)),
      ])
      .optional(),
    text: z.string().optional(),
    note: z.string().optional(),
    items: z
      .string()
      .optional()
      .transform((val) => {
        if (!val || val.trim() === '') return []
        try {
          return JSON.parse(val)
        } catch (e) {
          throw new z.ZodError([{ message: "Invalid items JSON", path: ["items"], code: z.ZodIssueCode.custom }])
        }
      }),
  })
  .catchall(z.string())
```

## File: `forms/users.ts`
```typescript
import { z } from "zod"

export const userFormSchema = z.object({
  name: z.string().max(128).optional(),
  avatar: z.instanceof(File).optional(),
  businessName: z.string().max(128).optional(),
  businessAddress: z.string().max(1024).optional(),
  businessBankDetails: z.string().max(1024).optional(),
  businessLogo: z.instanceof(File).optional(),
})
```

## File: `hooks/use-download.tsx`
```tsx
import { useState } from "react"

interface UseDownloadOptions {
  onSuccess?: () => void
  onError?: (error: Error) => void
}

export function useDownload(options: UseDownloadOptions = {}) {
  const [isDownloading, setIsDownloading] = useState(false)

  const download = async (url: string, defaultName: string) => {
    try {
      setIsDownloading(true)

      const response = await fetch(url)
      if (!response.ok) throw new Error("Download failed")

      // Get the filename from the Content-Disposition header
      const contentDisposition = response.headers.get("Content-Disposition")
      const filename = contentDisposition ? contentDisposition.split("filename=")[1].replace(/"/g, "") : defaultName

      // Create a blob from the response
      const blob = await response.blob()

      // Create a download link and trigger it
      const downloadLink = window.URL.createObjectURL(blob)
      const a = document.createElement("a")
      a.href = downloadLink
      a.download = filename
      document.body.appendChild(a)
      a.click()
      window.URL.revokeObjectURL(downloadLink)
      document.body.removeChild(a)

      options.onSuccess?.()
    } catch (error) {
      console.error("Download error:", error)
      options.onError?.(error instanceof Error ? error : new Error("Download failed"))
    } finally {
      setIsDownloading(false)
    }
  }

  return {
    download,
    isDownloading,
  }
}
```

## File: `hooks/use-mobile.tsx`
```tsx
import * as React from "react"

const MOBILE_BREAKPOINT = 768

export function useIsMobile() {
  const [isMobile, setIsMobile] = React.useState<boolean | undefined>(undefined)

  React.useEffect(() => {
    const mql = window.matchMedia(`(max-width: ${MOBILE_BREAKPOINT - 1}px)`)
    const onChange = () => {
      setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    }
    mql.addEventListener("change", onChange)
    setIsMobile(window.innerWidth < MOBILE_BREAKPOINT)
    return () => mql.removeEventListener("change", onChange)
  }, [])

  return !!isMobile
}
```

## File: `hooks/use-persistent-form-state.tsx`
```tsx
import { useEffect, useState } from "react"

export function usePersistentFormState(key: string, defaultState = {}) {
  const [formState, setFormState] = useState(defaultState)
  const [isLoaded, setIsLoaded] = useState(false)

  useEffect(() => {
    const saved = localStorage.getItem(key)
    if (saved) {
      setFormState(JSON.parse(saved))
    }
    setIsLoaded(true)
  }, [])

  useEffect(() => {
    if (isLoaded) {
      localStorage.setItem(key, JSON.stringify(formState))
    }
  }, [formState, isLoaded])

  return [formState, setFormState] as const
}
```

## File: `hooks/use-progress.tsx`
```tsx
import { generateUUID } from "@/lib/utils"
import { useEffect, useState } from "react"

interface Progress {
  id: string
  current: number
  total: number
  type: string
  data: any
  createdAt: string
}

interface UseProgressOptions {
  onSuccess?: (progress: Progress) => void
  onError?: (error: Error) => void
}

export function useProgress(options: UseProgressOptions = {}) {
  const [isLoading, setIsLoading] = useState(false)
  const [eventSource, setEventSource] = useState<EventSource | null>(null)
  const [progress, setProgress] = useState<Progress | null>(null)

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (eventSource) {
        eventSource.close()
      }
    }
  }, [eventSource])

  const startProgress = async (type: string) => {
    setIsLoading(true)
    setProgress(null)

    // Close any existing connection
    if (eventSource) {
      eventSource.close()
    }

    try {
      const progressId = generateUUID()
      const source = new EventSource(`/api/progress/${progressId}?type=${type}`)
      setEventSource(source)

      source.onmessage = (event) => {
        try {
          const progress = JSON.parse(event.data)
          setProgress(progress)
          options.onSuccess?.(progress)

          if (progress.current === progress.total && progress.total > 0) {
            source.close()
            setIsLoading(false)
          }
        } catch (error) {
          console.error("Failed to parse progress data:", error)
          source.close()
          setIsLoading(false)
        }
      }

      source.onerror = (error) => {
        source.close()
        setIsLoading(false)
        const err = new Error("Progress tracking failed")
        console.error("Progress tracking error:", err)
        options.onError?.(err)
      }

      return progressId
    } catch (error) {
      setIsLoading(false)
      const err = error instanceof Error ? error : new Error("Failed to start progress")
      console.error("Failed to start progress:", err)
      options.onError?.(err)
      return null
    }
  }

  return {
    isLoading,
    startProgress,
    progress,
  }
}
```

## File: `hooks/use-transaction-filters.tsx`
```tsx
import { TransactionFilters } from "@/models/transactions"
import { format } from "date-fns"
import { useRouter, useSearchParams } from "next/navigation"
import { useEffect, useState } from "react"

const filterKeys = ["search", "dateFrom", "dateTo", "ordering", "categoryCode", "projectCode"]

export function useTransactionFilters(defaultFilters?: TransactionFilters) {
  const router = useRouter()
  const searchParams = useSearchParams()
  const [filters, setFilters] = useState<TransactionFilters>({
    ...defaultFilters,
    ...searchParamsToFilters(searchParams),
  })

  useEffect(() => {
    const newSearchParams = filtersToSearchParams(filters, searchParams)
    router.push(`?${newSearchParams.toString()}`)
  }, [filters])

  useEffect(() => {
    setFilters(searchParamsToFilters(searchParams))
  }, [searchParams])

  return [filters, setFilters] as const
}

export function searchParamsToFilters(searchParams: URLSearchParams) {
  return filterKeys.reduce((acc, filter) => {
    acc[filter] = searchParams.get(filter) || ""
    return acc
  }, {} as Record<string, string>) as TransactionFilters
}

export function filtersToSearchParams(
  filters: TransactionFilters,
  currentSearchParams?: URLSearchParams
): URLSearchParams {
  // Copy of all non-filter parameters back to the URL
  const searchParams = new URLSearchParams()
  if (currentSearchParams) {
    currentSearchParams.forEach((value, key) => {
      if (!filterKeys.includes(key)) {
        searchParams.set(key, value)
      }
    })
  }

  if (filters.search) {
    searchParams.set("search", filters.search)
  } else {
    searchParams.delete("search")
  }

  if (filters.dateFrom) {
    searchParams.set("dateFrom", format(new Date(filters.dateFrom), "yyyy-MM-dd"))
  } else {
    searchParams.delete("dateFrom")
  }

  if (filters.dateTo) {
    searchParams.set("dateTo", format(new Date(filters.dateTo), "yyyy-MM-dd"))
  } else {
    searchParams.delete("dateTo")
  }

  if (filters.ordering) {
    searchParams.set("ordering", filters.ordering)
  } else {
    searchParams.delete("ordering")
  }

  if (filters.categoryCode && filters.categoryCode !== "-") {
    searchParams.set("categoryCode", filters.categoryCode)
  } else {
    searchParams.delete("categoryCode")
  }

  if (filters.projectCode && filters.projectCode !== "-") {
    searchParams.set("projectCode", filters.projectCode)
  } else {
    searchParams.delete("projectCode")
  }

  return searchParams
}

export function isFiltered(filters: TransactionFilters) {
  return Object.values(filters).some((value) => value !== "" && value !== "-")
}
```

## File: `lib/actions.ts`
```typescript
export type ActionState<T> = {
  success: boolean
  error?: string | null
  data?: T | null
}
```

## File: `lib/auth-client.ts`
```typescript
import { createAuthClient } from "better-auth/client"
import { emailOTPClient } from "better-auth/client/plugins"

export const authClient = createAuthClient({
  plugins: [emailOTPClient()],
})
```

## File: `lib/auth.ts`
```typescript
import config from "@/lib/config"
import { getSelfHostedUser, getUserByEmail, getUserById, SELF_HOSTED_USER } from "@/models/users"
import { User } from "@/prisma/client"
import { betterAuth } from "better-auth"
import { prismaAdapter } from "better-auth/adapters/prisma"
import { APIError } from "better-auth/api"
import { nextCookies } from "better-auth/next-js"
import { emailOTP } from "better-auth/plugins/email-otp"
import { headers } from "next/headers"
import { redirect } from "next/navigation"
import { prisma } from "./db"
import { resend, sendOTPCodeEmail } from "./email"

export type UserProfile = {
  id: string
  name: string
  email: string
  avatar?: string
  membershipPlan: string
  storageUsed: number
  storageLimit: number
  aiBalance: number
}

export const auth = betterAuth({
  database: prismaAdapter(prisma, { provider: "postgresql" }),
  appName: config.app.title,
  baseURL: config.app.baseURL,
  secret: config.auth.secret,
  email: {
    provider: "resend",
    from: config.email.from,
    resend,
  },
  session: {
    strategy: "jwt",
    expiresIn: 180 * 24 * 60 * 60, // 365 days
    updateAge: 24 * 60 * 60, // 24 hours
    cookieCache: {
      enabled: true,
      maxAge: 365 * 24 * 60 * 60, // 365 days
    },
  },
  advanced: {
    cookiePrefix: "taxhacker",
    database: {
      generateId: "uuid",
    },
  },
  plugins: [
    emailOTP({
      disableSignUp: config.auth.disableSignup,
      otpLength: 6,
      expiresIn: 10 * 60, // 10 minutes
      sendVerificationOTP: async ({ email, otp }) => {
        const user = await getUserByEmail(email)
        if (!user) {
          throw new APIError("NOT_FOUND", { message: "User with this email does not exist" })
        }
        await sendOTPCodeEmail({ email, otp })
      },
    }),
    nextCookies(), // make sure this is the last plugin in the array
  ],
})

export async function getSession() {
  if (config.selfHosted.isEnabled) {
    const user = await getSelfHostedUser()
    return user ? { user } : null
  }

  return await auth.api.getSession({
    headers: await headers(),
  })
}

export async function getCurrentUser(): Promise<User> {
  if (config.selfHosted.isEnabled) {
    const user = await getSelfHostedUser()
    if (user) {
      return user
    } else {
      redirect(config.selfHosted.redirectUrl)
    }
  }

  // Try to return user from session
  const session = await getSession()
  if (session && session.user) {
    const user = await getUserById(session.user.id)
    if (user) {
      return user
    }
  }

  // No session or user found
  redirect(config.auth.loginUrl)
}

export function isSubscriptionExpired(user: User) {
  if (config.selfHosted.isEnabled) {
    return false
  }
  return user.membershipExpiresAt && user.membershipExpiresAt < new Date()
}

export function isAiBalanceExhausted(user: User) {
  if (config.selfHosted.isEnabled || user.membershipPlan === SELF_HOSTED_USER.membershipPlan) {
    return false
  }
  return user.aiBalance <= 0
}
```

## File: `lib/cache.ts`
```typescript
export type CacheKey = string
export type CacheEntry<T> = {
  value: T
  timestamp: number
}

export class PoorManCache<T> {
  private cache: Map<CacheKey, CacheEntry<T>>
  private duration: number

  /**
   * Create a new cache instance
   * @param duration Cache duration in milliseconds
   */
  constructor(duration: number) {
    this.cache = new Map<CacheKey, CacheEntry<T>>()
    this.duration = duration
  }

  /**
   * Get a value from the cache
   * @param key Cache key
   * @returns The cached value or undefined if not found or expired
   */
  get(key: CacheKey): T | undefined {
    const entry = this.cache.get(key)

    if (!entry) {
      return undefined
    }

    // Check if entry is expired
    if (Date.now() - entry.timestamp > this.duration) {
      this.cache.delete(key)
      return undefined
    }

    return entry.value
  }

  /**
   * Set a value in the cache
   * @param key Cache key
   * @param value Value to cache
   */
  set(key: CacheKey, value: T): void {
    this.cache.set(key, {
      value,
      timestamp: Date.now(),
    })
  }

  /**
   * Check if a key exists in the cache and is not expired
   * @param key Cache key
   * @returns True if the key exists and is not expired
   */
  has(key: CacheKey): boolean {
    const entry = this.cache.get(key)

    if (!entry) {
      return false
    }

    // Check if entry is expired
    if (Date.now() - entry.timestamp > this.duration) {
      this.cache.delete(key)
      return false
    }

    return true
  }

  /**
   * Remove a key from the cache
   * @param key Cache key
   */
  delete(key: CacheKey): void {
    this.cache.delete(key)
  }

  /**
   * Clear all expired entries from the cache
   */
  cleanup(): void {
    const now = Date.now()
    for (const [key, entry] of this.cache.entries()) {
      if (now - entry.timestamp > this.duration) {
        this.cache.delete(key)
      }
    }
  }

  /**
   * Get the current size of the cache
   * @returns Number of entries in the cache
   */
  size(): number {
    return this.cache.size
  }

  /**
   * Clear all entries from the cache
   */
  clear(): void {
    this.cache.clear()
  }
}
```

## File: `lib/config.ts`
```typescript
import { z } from "zod"

const envSchema = z.object({
  BASE_URL: z.string().url().default("http://localhost:7331"),
  PORT: z.string().default("7331"),
  SELF_HOSTED_MODE: z.enum(["true", "false"]).default("true"),
  OPENAI_API_KEY: z.string().optional(),
  OPENAI_MODEL_NAME: z.string().default("gpt-4o-mini"),
  GOOGLE_API_KEY: z.string().optional(),
  GOOGLE_MODEL_NAME: z.string().default("gemini-2.5-flash"),
  MISTRAL_API_KEY: z.string().optional(),
  MISTRAL_MODEL_NAME: z.string().default("mistral-medium-latest"),
  BETTER_AUTH_SECRET: z
    .string()
    .min(16, "Auth secret must be at least 16 characters")
    .default("please-set-your-key-here"),
  DISABLE_SIGNUP: z.enum(["true", "false"]).default("false"),
  RESEND_API_KEY: z.string().default("please-set-your-resend-api-key-here"),
  RESEND_FROM_EMAIL: z.string().default("TaxHacker <user@localhost>"),
  RESEND_AUDIENCE_ID: z.string().default(""),
  STRIPE_SECRET_KEY: z.string().default(""),
  STRIPE_WEBHOOK_SECRET: z.string().default(""),
})

const env = envSchema.parse(process.env)

const config = {
  app: {
    title: "TaxHacker",
    description: "Your personal AI accountant",
    version: process.env.npm_package_version || "0.0.1",
    baseURL: env.BASE_URL || `http://localhost:${env.PORT || "7331"}`,
    supportEmail: "me@vas3k.com",
  },
  upload: {
    acceptedMimeTypes: "image/*,.pdf,.doc,.docx,.xls,.xlsx",
    images: {
      maxWidth: 1800,
      maxHeight: 1800,
      quality: 90,
    },
    pdfs: {
      maxPages: 10,
      dpi: 150,
      quality: 90,
      maxWidth: 1500,
      maxHeight: 1500,
    },
  },
  selfHosted: {
    isEnabled: env.SELF_HOSTED_MODE === "true",
    redirectUrl: "/self-hosted/redirect",
    welcomeUrl: "/self-hosted",
  },
  ai: {
    openaiApiKey: env.OPENAI_API_KEY,
    openaiModelName: env.OPENAI_MODEL_NAME,
    googleApiKey: env.GOOGLE_API_KEY,
    googleModelName: env.GOOGLE_MODEL_NAME,
    mistralApiKey: env.MISTRAL_API_KEY,
    mistralModelName: env.MISTRAL_MODEL_NAME,
  },
  auth: {
    secret: env.BETTER_AUTH_SECRET,
    loginUrl: "/enter",
    disableSignup: env.DISABLE_SIGNUP === "true" || env.SELF_HOSTED_MODE === "true",
  },
  stripe: {
    secretKey: env.STRIPE_SECRET_KEY,
    webhookSecret: env.STRIPE_WEBHOOK_SECRET,
    paymentSuccessUrl: `${env.BASE_URL}/cloud/payment/success?session_id={CHECKOUT_SESSION_ID}`,
    paymentCancelUrl: `${env.BASE_URL}/cloud`,
  },
  email: {
    apiKey: env.RESEND_API_KEY,
    from: env.RESEND_FROM_EMAIL,
    audienceId: env.RESEND_AUDIENCE_ID,
  },
} as const

export default config
```

## File: `lib/db.ts`
```typescript
import { PrismaClient } from "@/prisma/client"

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

export const prisma = globalForPrisma.prisma ?? new PrismaClient({ log: ["query", "info", "warn", "error"] })

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma
```

## File: `lib/email.ts`
```typescript
import { NewsletterWelcomeEmail } from "@/components/emails/newsletter-welcome-email"
import { OTPEmail } from "@/components/emails/otp-email"
import React from "react"
import { Resend } from "resend"
import config from "./config"

export const resend = new Resend(config.email.apiKey)

export async function sendOTPCodeEmail({ email, otp }: { email: string; otp: string }) {
  const html = React.createElement(OTPEmail, { otp })

  return await resend.emails.send({
    from: config.email.from,
    to: email,
    subject: "Your TaxHacker verification code",
    react: html,
  })
}

export async function sendNewsletterWelcomeEmail(email: string) {
  const html = React.createElement(NewsletterWelcomeEmail)

  return await resend.emails.send({
    from: config.email.from,
    to: email,
    subject: "Welcome to TaxHacker Newsletter!",
    react: html,
  })
}
```

## File: `lib/files.ts`
```typescript
import { File, Transaction, User } from "@/prisma/client"
import { access, constants, readdir, stat } from "fs/promises"
import path from "path"
import config from "./config"

export const FILE_UPLOAD_PATH = path.resolve(process.env.UPLOAD_PATH || "./uploads")
export const FILE_UNSORTED_DIRECTORY_NAME = "unsorted"
export const FILE_PREVIEWS_DIRECTORY_NAME = "previews"
export const FILE_STATIC_DIRECTORY_NAME = "static"
export const FILE_IMPORT_CSV_DIRECTORY_NAME = "csv"

export function getUserUploadsDirectory(user: User) {
  return safePathJoin(FILE_UPLOAD_PATH, user.email)
}

export function getStaticDirectory(user: User) {
  return safePathJoin(getUserUploadsDirectory(user), FILE_STATIC_DIRECTORY_NAME)
}

export function getUserPreviewsDirectory(user: User) {
  return safePathJoin(getUserUploadsDirectory(user), FILE_PREVIEWS_DIRECTORY_NAME)
}

export function unsortedFilePath(fileUuid: string, filename: string) {
  const fileExtension = path.extname(filename)
  return safePathJoin(FILE_UNSORTED_DIRECTORY_NAME, `${fileUuid}${fileExtension}`)
}

export function previewFilePath(fileUuid: string, page: number) {
  return safePathJoin(FILE_PREVIEWS_DIRECTORY_NAME, `${fileUuid}.${page}.webp`)
}

export function getTransactionFileUploadPath(fileUuid: string, filename: string, transaction: Transaction) {
  const fileExtension = path.extname(filename)
  const storedFileName = `${fileUuid}${fileExtension}`
  return formatFilePath(storedFileName, transaction.issuedAt || new Date())
}

export function fullPathForFile(user: User, file: File) {
  const userUploadsDirectory = getUserUploadsDirectory(user)
  return safePathJoin(userUploadsDirectory, file.path)
}

function formatFilePath(filename: string, date: Date, format = "{YYYY}/{MM}/{name}{ext}") {
  const year = date.getFullYear()
  const month = String(date.getMonth() + 1).padStart(2, "0")
  const ext = path.extname(filename)
  const name = path.basename(filename, ext)

  return format.replace("{YYYY}", String(year)).replace("{MM}", month).replace("{name}", name).replace("{ext}", ext)
}

export function safePathJoin(basePath: string, ...paths: string[]) {
  const joinedPath = path.join(basePath, path.normalize(path.join(...paths)))
  if (!joinedPath.startsWith(basePath)) {
    throw new Error("Path traversal detected")
  }
  return joinedPath
}

export async function fileExists(filePath: string) {
  try {
    await access(path.normalize(filePath), constants.F_OK)
    return true
  } catch {
    return false
  }
}

export async function getDirectorySize(directoryPath: string) {
  let totalSize = 0
  async function calculateSize(dir: string) {
    const files = await readdir(dir, { withFileTypes: true })
    for (const file of files) {
      const fullPath = path.join(dir, file.name)
      if (file.isDirectory()) {
        await calculateSize(fullPath)
      } else if (file.isFile()) {
        const stats = await stat(fullPath)
        totalSize += stats.size
      }
    }
  }
  await calculateSize(directoryPath)
  return totalSize
}

export function isEnoughStorageToUploadFile(user: User, fileSize: number) {
  if (config.selfHosted.isEnabled || user.storageLimit < 0) {
    return true
  }
  return user.storageUsed + fileSize <= user.storageLimit
}
```

## File: `lib/llm-providers.ts`
```typescript
export const PROVIDERS = [
  {
    key: "openai",
    label: "OpenAI",
    apiKeyName: "openai_api_key",
    modelName: "openai_model_name",
    defaultModelName: "gpt-4o-mini",
    apiDoc: "https://platform.openai.com/settings/organization/api-keys",
    apiDocLabel: "OpenAI Platform Console",
    placeholder: "sk-...",
    help: {
      url: "https://platform.openai.com/settings/organization/api-keys",
      label: "OpenAI Platform Console"
    },
    logo: "/logo/openai.svg"
  },
  {
    key: "google",
    label: "Google",
    apiKeyName: "google_api_key",
    modelName: "google_model_name",
    defaultModelName: "gemini-2.5-flash",
    apiDoc: "https://aistudio.google.com/apikey",
    apiDocLabel: "Google AI Studio",
    placeholder: "...",
    help: {
      url: "https://aistudio.google.com/apikey",
      label: "Google AI Studio"
    },
    logo: "/logo/google.svg"
  },
  {
    key: "mistral",
    label: "Mistral",
    apiKeyName: "mistral_api_key",
    modelName: "mistral_model_name",
    defaultModelName: "mistral-medium-latest",
    apiDoc: "https://admin.mistral.ai/organization/api-keys",
    apiDocLabel: "Mistral Admin Console",
    placeholder: "...",
    help: {
      url: "https://admin.mistral.ai/organization/api-keys",
      label: "Mistral Admin Console"
    },
    logo: "/logo/mistral.svg"
  },
]
```

## File: `lib/stats.ts`
```typescript
import { Field, Transaction } from "@/prisma/client"

export function calcTotalPerCurrency(transactions: Transaction[]): Record<string, number> {
  return transactions.reduce(
    (acc, transaction) => {
      if (transaction.convertedCurrencyCode) {
        acc[transaction.convertedCurrencyCode.toUpperCase()] =
          (acc[transaction.convertedCurrencyCode.toUpperCase()] || 0) + (transaction.convertedTotal || 0)
      } else if (transaction.currencyCode) {
        acc[transaction.currencyCode.toUpperCase()] =
          (acc[transaction.currencyCode.toUpperCase()] || 0) + (transaction.total || 0)
      }
      return acc
    },
    {} as Record<string, number>
  )
}

export function calcNetTotalPerCurrency(transactions: Transaction[]): Record<string, number> {
  return transactions.reduce(
    (acc, transaction) => {
      let amount = 0
      let currency: string | undefined
      if (
        transaction.convertedTotal !== null &&
        transaction.convertedTotal !== undefined &&
        transaction.convertedCurrencyCode
      ) {
        amount = transaction.convertedTotal
        currency = transaction.convertedCurrencyCode.toUpperCase()
      } else if (transaction.total !== null && transaction.total !== undefined && transaction.currencyCode) {
        amount = transaction.total
        currency = transaction.currencyCode.toUpperCase()
      }
      if (currency && amount !== 0) {
        const sign = transaction.type === "expense" ? -1 : 1
        acc[currency] = (acc[currency] || 0) + amount * sign
      }
      return acc
    },
    {} as Record<string, number>
  )
}

export const isTransactionIncomplete = (fields: Field[], transaction: Transaction): boolean => {
  const incompleteFields = incompleteTransactionFields(fields, transaction)

  return incompleteFields.length > 0
}

export const incompleteTransactionFields = (fields: Field[], transaction: Transaction): Field[] => {
  const requiredFields = fields.filter((field) => field.isRequired)

  return requiredFields.filter((field) => {
    const value = field.isExtra
      ? (transaction.extra as Record<string, any>)?.[field.code]
      : transaction[field.code as keyof Transaction]

    return value === undefined || value === null || value === ""
  })
}
```

## File: `lib/stripe.ts`
```typescript
import Stripe from "stripe"
import config from "./config"

export const stripeClient: Stripe | null = config.stripe.secretKey
  ? new Stripe(config.stripe.secretKey, {
      apiVersion: "2025-03-31.basil",
    })
  : null

export type Plan = {
  code: string
  name: string
  description: string
  benefits: string[]
  price: string
  stripePriceId: string
  limits: {
    storage: number
    ai: number
  }
  isAvailable: boolean
}

export const PLANS: Record<string, Plan> = {
  unlimited: {
    code: "unlimited",
    name: "Unlimited",
    description: "Special unlimited plan",
    benefits: ["Unlimited storage", "Unlimited AI analysis", "Unlimited everything"],
    price: "",
    stripePriceId: "",
    limits: {
      storage: -1,
      ai: -1,
    },
    isAvailable: false,
  },
  early: {
    code: "early",
    name: "Early Adopter",
    description: "Discounted plan for our first users who can forgive us bugs and childish problems :)",
    benefits: [
      "Special price for early adopters",
      "512 Mb of storage",
      "1000 AI file analyses",
      "Unlimited transactions",
      "Unlimited fields, categories and projects",
    ],
    price: "€35 for a year",
    stripePriceId: "price_1RHTj1As8DS4NhOzhejpTN3I",
    limits: {
      storage: 512 * 1024 * 1024,
      ai: 1000,
    },
    isAvailable: true,
  },
}
```

## File: `lib/uploads.ts`
```typescript
import { User } from "@/prisma/client"
import { mkdir } from "fs/promises"
import path from "path"
import sharp from "sharp"
import config from "./config"
import { getStaticDirectory, isEnoughStorageToUploadFile, safePathJoin } from "./files"

export async function uploadStaticImage(
  user: User,
  file: File,
  saveFileName: string,
  maxWidth: number = config.upload.images.maxWidth,
  maxHeight: number = config.upload.images.maxHeight,
  quality: number = config.upload.images.quality
) {
  const uploadDirectory = getStaticDirectory(user)

  if (!isEnoughStorageToUploadFile(user, file.size)) {
    throw Error("Not enough space to upload the file")
  }

  await mkdir(uploadDirectory, { recursive: true })

  // Get target format from saveFileName extension
  const targetFormat = path.extname(saveFileName).slice(1).toLowerCase()
  if (!targetFormat) {
    throw Error("Target filename must have an extension")
  }

  // Convert image and save to static folder
  const uploadFilePath = safePathJoin(uploadDirectory, saveFileName)
  const arrayBuffer = await file.arrayBuffer()
  const buffer = Buffer.from(arrayBuffer)

  const sharpInstance = sharp(buffer).rotate().resize(maxWidth, maxHeight, {
    fit: "inside",
    withoutEnlargement: true,
  })

  // Set output format and quality
  switch (targetFormat) {
    case "png":
      await sharpInstance.png().toFile(uploadFilePath)
      break
    case "jpg":
    case "jpeg":
      await sharpInstance.jpeg({ quality }).toFile(uploadFilePath)
      break
    case "webp":
      await sharpInstance.webp({ quality }).toFile(uploadFilePath)
      break
    case "avif":
      await sharpInstance.avif({ quality }).toFile(uploadFilePath)
      break
    default:
      throw Error(`Unsupported target format: ${targetFormat}`)
  }

  return uploadFilePath
}
```

## File: `lib/utils.ts`
```typescript
import { clsx, type ClassValue } from "clsx"
import slugify from "slugify"
import { twMerge } from "tailwind-merge"
import { violet, tomato, red, crimson, pink, plum, purple, indigo, blue, sky, cyan, teal, mint, grass, lime, yellow, amber, orange, brown } from "@radix-ui/colors"

const LOCALE = "en-US"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export function formatCurrency(total: number, currency: string) {
  try {
    return new Intl.NumberFormat(LOCALE, {
      style: "currency",
      currency: currency,
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
      useGrouping: true,
    }).format(total / 100)
  } catch (error) {
    // can happen with custom currencies and crypto
    return `${currency} ${total / 100}`
  }
}

export function formatBytes(bytes: number) {
  if (bytes === 0) return "0 Bytes"

  const sizes = ["Bytes", "KB", "MB", "GB"]
  const maxIndex = sizes.length - 1

  const i = Math.min(Math.floor(Math.log10(bytes) / Math.log10(1024)), maxIndex)
  const value = bytes / Math.pow(1024, i)

  return `${parseFloat(value.toFixed(2))} ${sizes[i]}`
}

export function formatNumber(number: number) {
  return new Intl.NumberFormat(LOCALE, {
    useGrouping: true,
  }).format(number)
}

export function codeFromName(name: string, maxLength: number = 16) {
  const code = slugify(name, {
    replacement: "_",
    lower: true,
    strict: true,
    trim: true,
  })
  return code.slice(0, maxLength)
}

export function randomHexColor() {
  const palette = [
    violet.violet9,
    indigo.indigo9,
    blue.blue9,
    cyan.cyan9,
    teal.teal9,
    grass.grass9,
    lime.lime9,
    yellow.yellow9,
    amber.amber9,
    orange.orange9,
    red.red9,
    crimson.crimson9,
    pink.pink9,
    purple.purple9,
    plum.plum9,
    mint.mint9,
    brown.brown9,
    sky.sky9,
    tomato.tomato9,
  ]
  return palette[Math.floor(Math.random() * palette.length)]
}

export async function fetchAsBase64(url: string): Promise<string | null> {
  try {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error(`Failed to fetch image: ${response.statusText}`)
    }

    const blob = await response.blob()

    return await new Promise((resolve, reject) => {
      const reader = new FileReader()
      reader.onloadend = () => resolve(reader.result as string)
      reader.onerror = reject
      reader.readAsDataURL(blob)
    })
  } catch (error) {
    console.error("Error fetching image as data URL:", error)
    return null
  }
}

export function encodeFilename(filename: string): string {
  const encoded = encodeURIComponent(filename)
  return `UTF-8''${encoded}`
}

export function generateUUID(): string {
  // Try to use crypto.randomUUID() if available (modern browsers and Node.js 14.17+)
  if (typeof crypto !== "undefined" && crypto.randomUUID) {
    try {
      return crypto.randomUUID()
    } catch (error) {
      // Fall through to next method
    }
  }

  // Fallback to crypto.getRandomValues() for UUID v4 generation
  if (typeof crypto !== "undefined" && crypto.getRandomValues) {
    try {
      const bytes = new Uint8Array(16)
      crypto.getRandomValues(bytes)

      // Set version (4) and variant bits according to RFC 4122
      bytes[6] = (bytes[6] & 0x0f) | 0x40 // Version 4
      bytes[8] = (bytes[8] & 0x3f) | 0x80 // Variant 10

      // Convert to UUID string format
      const hex = Array.from(bytes, (byte) => byte.toString(16).padStart(2, "0")).join("")
      return [hex.slice(0, 8), hex.slice(8, 12), hex.slice(12, 16), hex.slice(16, 20), hex.slice(20, 32)].join("-")
    } catch (error) {
      // Fall through to Math.random() fallback
    }
  }

  // Final fallback using Math.random() (RFC 4122 compliant UUID v4)
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
    const r = (Math.random() * 16) | 0
    const v = c === "x" ? r : (r & 0x3) | 0x8
    return v.toString(16)
  })
}

export function formatPeriodLabel(period: string, date: Date): string {
  if (period.includes("-") && period.split("-").length === 3) {
    // Daily format: show day/month/year
    return date.toLocaleDateString("en-US", {
      weekday: "short",
      month: "short",
      day: "numeric",
      year: "numeric",
    })
  } else {
    // Monthly format: show month/year with short month name
    return date.toLocaleDateString("en-US", {
      month: "short",
      year: "numeric",
    })
  }
}
```

## File: `lib/previews/generate.ts`
```typescript
import { resizeImage } from "@/lib/previews/images"
import { pdfToImages } from "@/lib/previews/pdf"
import { User } from "@/prisma/client"

export async function generateFilePreviews(
  user: User,
  filePath: string,
  mimetype: string
): Promise<{ contentType: string; previews: string[] }> {
  if (mimetype === "application/pdf") {
    const { contentType, pages } = await pdfToImages(user, filePath)
    return { contentType, previews: pages }
  } else if (mimetype.startsWith("image/")) {
    const { contentType, resizedPath } = await resizeImage(user, filePath)
    return { contentType, previews: [resizedPath] }
  } else {
    return { contentType: mimetype, previews: [filePath] }
  }
}
```

## File: `lib/previews/images.ts`
```typescript
"use server"

import { fileExists, getUserPreviewsDirectory, safePathJoin } from "@/lib/files"
import { User } from "@/prisma/client"
import fs from "fs/promises"
import path from "path"
import sharp from "sharp"
import config from "../config"

export async function resizeImage(
  user: User,
  origFilePath: string,
  maxWidth: number = config.upload.images.maxWidth,
  maxHeight: number = config.upload.images.maxHeight,
  quality: number = config.upload.images.quality
): Promise<{ contentType: string; resizedPath: string }> {
  try {
    const userPreviewsDirectory = getUserPreviewsDirectory(user)
    await fs.mkdir(userPreviewsDirectory, { recursive: true })

    const basename = path.basename(origFilePath, path.extname(origFilePath))
    const outputPath = safePathJoin(userPreviewsDirectory, `${basename}.webp`)

    if (await fileExists(outputPath)) {
      const metadata = await sharp(outputPath).metadata()
      return {
        contentType: `image/${metadata.format}`,
        resizedPath: outputPath,
      }
    }

    await sharp(origFilePath)
      .rotate()
      .resize(maxWidth, maxHeight, {
        fit: "inside",
        withoutEnlargement: true,
      })
      .webp({ quality: quality })
      .toFile(outputPath)

    return {
      contentType: "image/webp",
      resizedPath: outputPath,
    }
  } catch (error) {
    console.error("Error resizing image:", error)
    return {
      contentType: "image/unknown",
      resizedPath: origFilePath,
    }
  }
}
```

## File: `lib/previews/pdf.ts`
```typescript
"use server"

import { fileExists, getUserPreviewsDirectory, safePathJoin } from "@/lib/files"
import { User } from "@/prisma/client"
import fs from "fs/promises"
import path from "path"
import { fromPath } from "pdf2pic"
import config from "../config"

export async function pdfToImages(user: User, origFilePath: string): Promise<{ contentType: string; pages: string[] }> {
  const userPreviewsDirectory = getUserPreviewsDirectory(user)
  await fs.mkdir(userPreviewsDirectory, { recursive: true })

  const basename = path.basename(origFilePath, path.extname(origFilePath))
  // Check if converted pages already exist
  const existingPages: string[] = []
  for (let i = 1; i <= config.upload.pdfs.maxPages; i++) {
    const convertedFilePath = safePathJoin(userPreviewsDirectory, `${basename}.${i}.webp`)
    if (await fileExists(convertedFilePath)) {
      existingPages.push(convertedFilePath)
    } else {
      break
    }
  }

  if (existingPages.length > 0) {
    return { contentType: "image/webp", pages: existingPages }
  }

  // If not — convert the file as store in previews folder
  const pdf2picOptions = {
    density: config.upload.pdfs.dpi,
    saveFilename: basename,
    savePath: userPreviewsDirectory,
    format: "webp",
    quality: config.upload.pdfs.quality,
    width: config.upload.pdfs.maxWidth,
    height: config.upload.pdfs.maxHeight,
    preserveAspectRatio: true,
  }

  try {
    const convert = fromPath(origFilePath, pdf2picOptions)
    const results = await convert.bulk(-1, { responseType: "image" }) // TODO: respect MAX_PAGES here too
    const paths = results.filter((result) => result && result.path).map((result) => result.path) as string[]
    return {
      contentType: "image/webp",
      pages: paths,
    }
  } catch (error) {
    console.error("Error converting PDF to image:", error)
    throw error
  }
}
```

## File: `models/apps.ts`
```typescript
import { prisma } from "@/lib/db"
import { User } from "@/prisma/client"

export const getAppData = async (user: User, app: string) => {
  const appData = await prisma.appData.findUnique({
    where: { userId_app: { userId: user.id, app } },
  })

  return appData?.data
}

export const setAppData = async (user: User, app: string, data: any) => {
  await prisma.appData.upsert({
    where: { userId_app: { userId: user.id, app } },
    update: { data },
    create: { userId: user.id, app, data },
  })
}
```

## File: `models/backups.ts`
```typescript
import { prisma } from "@/lib/db"

type BackupSetting = {
  filename: string
  model: any
  backup: (userId: string, row: any) => Record<string, any>
  restore: (userId: string, json: Record<string, any>) => any
}

// Ordering is important here
export const MODEL_BACKUP: BackupSetting[] = [
  {
    filename: "settings.json",
    model: prisma.setting,
    backup: (userId: string, row: any) => {
      return {
        id: row.id,
        code: row.code,
        name: row.name,
        description: row.description,
        value: row.value,
      }
    },
    restore: (userId: string, json: any) => {
      return {
        code: json.code,
        name: json.name,
        description: json.description,
        value: json.value,
        user: {
          connect: {
            id: userId,
          },
        },
      }
    },
  },
  {
    filename: "currencies.json",
    model: prisma.currency,
    backup: (userId: string, row: any) => {
      return {
        id: row.id,
        code: row.code,
        name: row.name,
      }
    },
    restore: (userId: string, json: any) => {
      return {
        code: json.code,
        name: json.name,
        user: {
          connect: {
            id: userId,
          },
        },
      }
    },
  },
  {
    filename: "categories.json",
    model: prisma.category,
    backup: (userId: string, row: any) => {
      return {
        id: row.id,
        code: row.code,
        name: row.name,
        color: row.color,
        llm_prompt: row.llm_prompt,
        createdAt: row.createdAt,
      }
    },
    restore: (userId: string, json: any) => {
      return {
        code: json.code,
        name: json.name,
        color: json.color,
        llm_prompt: json.llm_prompt,
        createdAt: json.createdAt,
        user: {
          connect: {
            id: userId,
          },
        },
      }
    },
  },
  {
    filename: "projects.json",
    model: prisma.project,
    backup: (userId: string, row: any) => {
      return {
        id: row.id,
        code: row.code,
        name: row.name,
        color: row.color,
        llm_prompt: row.llm_prompt,
        createdAt: row.createdAt,
      }
    },
    restore: (userId: string, json: any) => {
      return {
        code: json.code,
        name: json.name,
        color: json.color,
        llm_prompt: json.llm_prompt,
        createdAt: json.createdAt,
        user: {
          connect: {
            id: userId,
          },
        },
      }
    },
  },
  {
    filename: "fields.json",
    model: prisma.field,
    backup: (userId: string, row: any) => {
      return {
        id: row.id,
        code: row.code,
        name: row.name,
        type: row.type,
        llm_prompt: row.llm_prompt,
        options: row.options,
        isVisibleInList: row.isVisibleInList,
        isVisibleInAnalysis: row.isVisibleInAnalysis,
        isRequired: row.isRequired,
        isExtra: row.isExtra,
      }
    },
    restore: (userId: string, json: any) => {
      return {
        code: json.code,
        name: json.name,
        type: json.type,
        llm_prompt: json.llm_prompt,
        options: json.options,
        isVisibleInList: json.isVisibleInList,
        isVisibleInAnalysis: json.isVisibleInAnalysis,
        isRequired: json.isRequired,
        isExtra: json.isExtra,
        user: {
          connect: {
            id: userId,
          },
        },
      }
    },
  },
  {
    filename: "files.json",
    model: prisma.file,
    backup: (userId: string, row: any) => {
      return {
        id: row.id,
        filename: row.filename,
        path: row.path,
        metadata: row.metadata,
        isReviewed: row.isReviewed,
        mimetype: row.mimetype,
        createdAt: row.createdAt,
      }
    },
    restore: (userId: string, json: any) => {
      return {
        id: json.id,
        filename: json.filename,
        path: json.path ? json.path.replace(/^.*\/uploads\//, "") : "",
        metadata: json.metadata,
        isReviewed: json.isReviewed,
        mimetype: json.mimetype,
        user: {
          connect: {
            id: userId,
          },
        },
      }
    },
  },
  {
    filename: "transactions.json",
    model: prisma.transaction,
    backup: (userId: string, row: any) => {
      return {
        id: row.id,
        name: row.name,
        description: row.description,
        merchant: row.merchant,
        total: row.total,
        currencyCode: row.currencyCode,
        convertedTotal: row.convertedTotal,
        convertedCurrencyCode: row.convertedCurrencyCode,
        type: row.type,
        note: row.note,
        files: row.files,
        extra: row.extra,
        categoryCode: row.categoryCode,
        projectCode: row.projectCode,
        issuedAt: row.issuedAt,
        createdAt: row.createdAt,
        updatedAt: row.updatedAt,
        text: row.text,
      }
    },
    restore: (userId: string, json: any) => {
      return {
        id: json.id,
        name: json.name,
        description: json.description,
        merchant: json.merchant,
        total: json.total,
        currencyCode: json.currencyCode,
        convertedTotal: json.convertedTotal,
        convertedCurrencyCode: json.convertedCurrencyCode,
        type: json.type,
        note: json.note,
        files: json.files,
        extra: json.extra,
        issuedAt: json.issuedAt,
        user: {
          connect: {
            id: userId,
          },
        },
        category: {
          connect: {
            userId_code: { userId, code: json.categoryCode },
          },
        },
        project: {
          connect: {
            userId_code: { userId, code: json.projectCode },
          },
        },
      }
    },
  },
]

export async function modelToJSON(userId: string, backupSettings: BackupSetting): Promise<string> {
  const data = await backupSettings.model.findMany({ where: { userId } })

  if (!data || data.length === 0) {
    return "[]"
  }

  return JSON.stringify(
    data.map((row: any) => backupSettings.backup(userId, row)),
    null,
    2
  )
}

export async function modelFromJSON(
  userId: string,
  backupSettings: BackupSetting,
  jsonContent: string
): Promise<number> {
  if (!jsonContent) return 0

  try {
    const records = JSON.parse(jsonContent)

    if (!records || records.length === 0) {
      return 0
    }

    let insertedCount = 0
    for (const rawRecord of records) {
      const record = preprocessRowData(rawRecord)

      try {
        const data = await backupSettings.restore(userId, record)
        await backupSettings.model.create({ data })
      } catch (error) {
        console.error(`Error importing record:`, error)
      }
      insertedCount++
    }

    return insertedCount
  } catch (error) {
    console.error(`Error parsing JSON content:`, error)
    return 0
  }
}

function preprocessRowData(row: Record<string, any>): Record<string, any> {
  const processedRow: Record<string, any> = {}

  for (const [key, value] of Object.entries(row)) {
    if (value === "" || value === "null" || value === undefined) {
      processedRow[key] = null
      continue
    }

    // Try to parse JSON for object fields
    if (typeof value === "string" && (value.startsWith("{") || value.startsWith("["))) {
      try {
        processedRow[key] = JSON.parse(value)
        continue
      } catch (e) {
        // Not valid JSON, continue with normal processing
      }
    }

    // Handle dates (checking for ISO date format)
    if (typeof value === "string" && /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?Z?$/.test(value)) {
      processedRow[key] = new Date(value)
      continue
    }

    // Handle numbers
    if (typeof value === "string" && !isNaN(Number(value)) && key !== "id" && !key.endsWith("Code")) {
      // Convert numbers but preserving string IDs
      processedRow[key] = Number(value)
      continue
    }

    // Default: keep as is
    processedRow[key] = value
  }

  return processedRow
}
```

## File: `models/categories.ts`
```typescript
import { prisma } from "@/lib/db"
import { codeFromName } from "@/lib/utils"
import { Prisma } from "@/prisma/client"
import { cache } from "react"

export type CategoryData = {
  [key: string]: unknown
}

export const getCategories = cache(async (userId: string) => {
  return await prisma.category.findMany({
    where: { userId },
    orderBy: {
      name: "asc",
    },
  })
})

export const getCategoryByCode = cache(async (userId: string, code: string) => {
  return await prisma.category.findUnique({
    where: { userId_code: { userId, code } },
  })
})

export const createCategory = async (userId: string, category: CategoryData) => {
  if (!category.code) {
    category.code = codeFromName(category.name as string)
  }
  return await prisma.category.create({
    data: {
      ...category,
      user: {
        connect: {
          id: userId,
        },
      },
    } as Prisma.CategoryCreateInput,
  })
}

export const updateCategory = async (userId: string, code: string, category: CategoryData) => {
  return await prisma.category.update({
    where: { userId_code: { userId, code } },
    data: category,
  })
}

export const deleteCategory = async (userId: string, code: string) => {
  await prisma.transaction.updateMany({
    where: {
      userId,
      categoryCode: code,
    },
    data: {
      categoryCode: null,
    },
  })

  return await prisma.category.delete({
    where: { userId_code: { userId, code } },
  })
}
```

## File: `models/currencies.ts`
```typescript
import { prisma } from "@/lib/db"
import { Prisma } from "@/prisma/client"
import { cache } from "react"

export const getCurrencies = cache(async (userId: string) => {
  return await prisma.currency.findMany({
    where: { userId },
    orderBy: {
      code: "asc",
    },
  })
})

export const createCurrency = async (userId: string, currency: Prisma.CurrencyCreateInput) => {
  return await prisma.currency.create({
    data: {
      ...currency,
      user: {
        connect: {
          id: userId,
        },
      },
    },
  })
}

export const updateCurrency = async (userId: string, code: string, currency: Prisma.CurrencyUpdateInput) => {
  return await prisma.currency.update({
    where: { userId_code: { code, userId } },
    data: currency,
  })
}

export const deleteCurrency = async (userId: string, code: string) => {
  return await prisma.currency.delete({
    where: { userId_code: { code, userId } },
  })
}
```

## File: `models/defaults.ts`
```typescript
import { prisma } from "@/lib/db"

export const DEFAULT_PROMPT_ANALYSE_NEW_FILE = `You are an accountant and invoice analysis assistant. Extract following information from the given invoice: 

{fields}

Also try to extract "items": all separate products or items from the invoice

Where categories are:

{categories}

And projects are:

{projects}

IMPORTANT RULES:
- Do not include any other text in your response!
- If you can't find something leave it blank, NEVER make up information
- Return only one object`

export const DEFAULT_SETTINGS = [
  {
    code: "default_currency",
    name: "Default Currency",
    description: "Don't change this setting if you already have multi-currency transactions. I won't recalculate them.",
    value: "EUR",
  },
  {
    code: "default_category",
    name: "Default Category",
    description: "",
    value: "other",
  },
  {
    code: "default_project",
    name: "Default Project",
    description: "",
    value: "personal",
  },
  {
    code: "default_type",
    name: "Default Type",
    description: "",
    value: "expense",
  },
  {
    code: "prompt_analyse_new_file",
    name: "Prompt for Analyze Transaction",
    description: "Allowed variables: {fields}, {categories}, {categories.code}, {projects}, {projects.code}",
    value: DEFAULT_PROMPT_ANALYSE_NEW_FILE,
  },
  {
    code: "is_welcome_message_hidden",
    name: "Do not show welcome message on dashboard",
    description: "",
    value: "false",
  },
]

export const DEFAULT_CATEGORIES = [
  {
    code: "ads",
    name: "Advertisement",
    color: "#882727",
    llm_prompt: "ads, promos, online ads, etc",
  },
  {
    code: "swag",
    name: "Swag and Goods",
    color: "#882727",
    llm_prompt: "swag, stickers, goods, etc",
  },
  { code: "donations", name: "Gifts and Donations", color: "#1e6359", llm_prompt: "donations, gifts, charity" },
  { code: "tools", name: "Equipment and Tools", color: "#c69713", llm_prompt: "equipment, tools" },
  { code: "events", name: "Events and Conferences", color: "#ff8b32", llm_prompt: "events, conferences" },
  { code: "food", name: "Food and Drinks", color: "#d40e70", llm_prompt: "food, drinks, business meals" },
  { code: "insurance", name: "Insurance", color: "#050942", llm_prompt: "insurance, health, life" },
  { code: "invoice", name: "Invoice", color: "#064e85", llm_prompt: "custom invoice, bill" },
  { code: "communication", name: "Mobile and Internet", color: "#0e7d86", llm_prompt: "mobile, internet, phone" },
  { code: "office", name: "Office Supplies", color: "#59b0b9", llm_prompt: "office, supplies, stationery" },
  { code: "online", name: "Online Services", color: "#8753fb", llm_prompt: "online services, saas, subscriptions" },
  { code: "rental", name: "Rental", color: "#050942", llm_prompt: "rental, lease" },
  {
    code: "education",
    name: "Education",
    color: "#ee5d6c",
    llm_prompt: "education, professional development, trainings",
  },
  { code: "salary", name: "Salary", color: "#ce4993", llm_prompt: "salary, wages, etc" },
  { code: "fees", name: "Fees", color: "#6a0d83", llm_prompt: "fees, charges, penalties, etc" },
  { code: "travel", name: "Travel Expenses", color: "#fb9062", llm_prompt: "travel, accommodation, etc" },
  { code: "utility_bills", name: "Utility Bills", color: "#af7e2e", llm_prompt: "bills, electricity, water, etc" },
  {
    code: "transport",
    name: "Transport",
    color: "#800000",
    llm_prompt: "transportation costs, fuel, car rental, vignettes, etc",
  },
  { code: "software", name: "Software", color: "#2b5a1d", llm_prompt: "software, licenses" },
  { code: "other", name: "Other", color: "#121216", llm_prompt: "other, miscellaneous," },
]

export const DEFAULT_PROJECTS = [{ code: "personal", name: "Personal", llm_prompt: "personal", color: "#1e202b" }]

export const DEFAULT_CURRENCIES = [
  { code: "USD", name: "$" },
  { code: "EUR", name: "€" },
  { code: "GBP", name: "£" },
  { code: "INR", name: "₹" },
  { code: "AUD", name: "$" },
  { code: "CAD", name: "$" },
  { code: "SGD", name: "$" },
  { code: "CHF", name: "Fr" },
  { code: "MYR", name: "RM" },
  { code: "JPY", name: "¥" },
  { code: "CNY", name: "¥" },
  { code: "NZD", name: "$" },
  { code: "THB", name: "฿" },
  { code: "HUF", name: "Ft" },
  { code: "AED", name: "د.إ" },
  { code: "HKD", name: "$" },
  { code: "MXN", name: "$" },
  { code: "ZAR", name: "R" },
  { code: "PHP", name: "₱" },
  { code: "SEK", name: "kr" },
  { code: "IDR", name: "Rp" },
  { code: "BRL", name: "R$" },
  { code: "SAR", name: "﷼" },
  { code: "TRY", name: "₺" },
  { code: "KES", name: "KSh" },
  { code: "KRW", name: "₩" },
  { code: "EGP", name: "£" },
  { code: "IQD", name: "ع.د" },
  { code: "NOK", name: "kr" },
  { code: "KWD", name: "د.ك" },
  { code: "RUB", name: "₽" },
  { code: "DKK", name: "kr" },
  { code: "PKR", name: "₨" },
  { code: "ILS", name: "₪" },
  { code: "PLN", name: "zł" },
  { code: "QAR", name: "﷼" },
  { code: "OMR", name: "﷼" },
  { code: "COP", name: "$" },
  { code: "CLP", name: "$" },
  { code: "TWD", name: "NT$" },
  { code: "ARS", name: "$" },
  { code: "CZK", name: "Kč" },
  { code: "VND", name: "₫" },
  { code: "MAD", name: "د.م." },
  { code: "JOD", name: "د.ا" },
  { code: "BHD", name: ".د.ب" },
  { code: "XOF", name: "CFA" },
  { code: "LKR", name: "₨" },
  { code: "UAH", name: "₴" },
  { code: "NGN", name: "₦" },
  { code: "TND", name: "د.ت" },
  { code: "UGX", name: "USh" },
  { code: "RON", name: "lei" },
  { code: "BDT", name: "৳" },
  { code: "PEN", name: "S/" },
  { code: "GEL", name: "₾" },
  { code: "XAF", name: "FCFA" },
  { code: "FJD", name: "$" },
  { code: "VEF", name: "Bs" },
  { code: "VES", name: "Bs.S" },
  { code: "BYN", name: "Br" },
  { code: "UZS", name: "лв" },
  { code: "BGN", name: "лв" },
  { code: "DZD", name: "د.ج" },
  { code: "IRR", name: "﷼" },
  { code: "DOP", name: "RD$" },
  { code: "ISK", name: "kr" },
  { code: "CRC", name: "₡" },
  { code: "SYP", name: "£" },
  { code: "JMD", name: "J$" },
  { code: "LYD", name: "ل.د" },
  { code: "GHS", name: "₵" },
  { code: "MUR", name: "₨" },
  { code: "AOA", name: "Kz" },
  { code: "UYU", name: "$U" },
  { code: "AFN", name: "؋" },
  { code: "LBP", name: "ل.ل" },
  { code: "XPF", name: "₣" },
  { code: "TTD", name: "TT$" },
  { code: "TZS", name: "TSh" },
  { code: "ALL", name: "Lek" },
  { code: "XCD", name: "$" },
  { code: "GTQ", name: "Q" },
  { code: "NPR", name: "₨" },
  { code: "BOB", name: "Bs." },
  { code: "ZWD", name: "Z$" },
  { code: "BBD", name: "$" },
  { code: "CUC", name: "$" },
  { code: "LAK", name: "₭" },
  { code: "BND", name: "$" },
  { code: "BWP", name: "P" },
  { code: "HNL", name: "L" },
  { code: "PYG", name: "₲" },
  { code: "ETB", name: "Br" },
  { code: "NAD", name: "$" },
  { code: "PGK", name: "K" },
  { code: "SDG", name: "ج.س." },
  { code: "MOP", name: "MOP$" },
  { code: "BMD", name: "$" },
  { code: "NIO", name: "C$" },
  { code: "BAM", name: "KM" },
  { code: "KZT", name: "₸" },
  { code: "PAB", name: "B/." },
  { code: "GYD", name: "$" },
  { code: "YER", name: "﷼" },
  { code: "MGA", name: "Ar" },
  { code: "KYD", name: "$" },
  { code: "MZN", name: "MT" },
  { code: "RSD", name: "дин." },
  { code: "SCR", name: "₨" },
  { code: "AMD", name: "֏" },
  { code: "AZN", name: "₼" },
  { code: "SBD", name: "$" },
  { code: "SLL", name: "Le" },
  { code: "TOP", name: "T$" },
  { code: "BZD", name: "BZ$" },
  { code: "GMD", name: "D" },
  { code: "MWK", name: "MK" },
  { code: "BIF", name: "FBu" },
  { code: "HTG", name: "G" },
  { code: "SOS", name: "S" },
  { code: "GNF", name: "FG" },
  { code: "MNT", name: "₮" },
  { code: "MVR", name: "Rf" },
  { code: "CDF", name: "FC" },
  { code: "STN", name: "Db" },
  { code: "TJS", name: "ЅМ" },
  { code: "KPW", name: "₩" },
  { code: "KGS", name: "лв" },
  { code: "LRD", name: "$" },
  { code: "LSL", name: "L" },
  { code: "MMK", name: "K" },
  { code: "GIP", name: "£" },
  { code: "MDL", name: "L" },
  { code: "CUP", name: "₱" },
  { code: "KHR", name: "៛" },
  { code: "MKD", name: "ден" },
  { code: "VUV", name: "VT" },
  { code: "ANG", name: "ƒ" },
  { code: "MRU", name: "UM" },
  { code: "SZL", name: "L" },
  { code: "CVE", name: "$" },
  { code: "SRD", name: "$" },
  { code: "SVC", name: "$" },
  { code: "BSD", name: "$" },
  { code: "RWF", name: "R₣" },
  { code: "AWG", name: "ƒ" },
  { code: "BTN", name: "Nu." },
  { code: "DJF", name: "Fdj" },
  { code: "KMF", name: "CF" },
  { code: "ERN", name: "Nfk" },
  { code: "FKP", name: "£" },
  { code: "SHP", name: "£" },
  { code: "WST", name: "WS$" },
  { code: "JEP", name: "£" },
  { code: "TMT", name: "m" },
  { code: "GGP", name: "£" },
  { code: "IMP", name: "£" },
  { code: "TVD", name: "$" },
  { code: "ZMW", name: "ZK" },
  { code: "ADA", name: "Crypto" },
  { code: "BCH", name: "Crypto" },
  { code: "BTC", name: "Crypto" },
  { code: "CLF", name: "UF" },
  { code: "CNH", name: "¥" },
  { code: "DOGE", name: "Crypto" },
  { code: "DOT", name: "Crypto" },
  { code: "ETH", name: "Crypto" },
  { code: "LINK", name: "Crypto" },
  { code: "LTC", name: "Crypto" },
  { code: "LUNA", name: "Crypto" },
  { code: "SLE", name: "Le" },
  { code: "UNI", name: "Crypto" },
  { code: "XBT", name: "Crypto" },
  { code: "XLM", name: "Crypto" },
  { code: "XRP", name: "Crypto" },
  { code: "ZWL", name: "$" },
]

export const DEFAULT_FIELDS = [
  {
    code: "name",
    name: "Name",
    type: "string",
    llm_prompt: "human readable name, summarize what is bought or paid for in the invoice",
    isVisibleInList: true,
    isVisibleInAnalysis: true,
    isRequired: true,
    isExtra: false,
  },
  {
    code: "description",
    name: "Description",
    type: "string",
    llm_prompt: "description of the transaction",
    isVisibleInList: false,
    isVisibleInAnalysis: false,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "merchant",
    name: "Merchant",
    type: "string",
    llm_prompt: "merchant name, use the original spelling and language",
    isVisibleInList: true,
    isVisibleInAnalysis: true,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "issuedAt",
    name: "Issued At",
    type: "string",
    llm_prompt: "issued at date (YYYY-MM-DD format)",
    isVisibleInList: true,
    isVisibleInAnalysis: true,
    isRequired: true,
    isExtra: false,
  },
  {
    code: "projectCode",
    name: "Project",
    type: "string",
    llm_prompt: "project code, one of: {projects.code}",
    isVisibleInList: true,
    isVisibleInAnalysis: true,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "categoryCode",
    name: "Category",
    type: "string",
    llm_prompt: "category code, one of: {categories.code}",
    isVisibleInList: true,
    isVisibleInAnalysis: true,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "files",
    name: "Files",
    type: "string",
    llm_prompt: "",
    isVisibleInList: true,
    isVisibleInAnalysis: true,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "total",
    name: "Total",
    type: "number",
    llm_prompt: "total total of the transaction",
    isVisibleInList: true,
    isVisibleInAnalysis: true,
    isRequired: true,
    isExtra: false,
  },
  {
    code: "currencyCode",
    name: "Currency",
    type: "string",
    llm_prompt: "currency code, ISO 4217 three letter code like USD, EUR, including crypto codes like BTC, ETH, etc",
    isVisibleInList: false,
    isVisibleInAnalysis: true,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "convertedTotal",
    name: "Converted Total",
    type: "number",
    llm_prompt: "",
    isVisibleInList: false,
    isVisibleInAnalysis: false,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "convertedCurrencyCode",
    name: "Converted Currency Code",
    type: "string",
    llm_prompt: "",
    isVisibleInList: false,
    isVisibleInAnalysis: false,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "type",
    name: "Type",
    type: "string",
    llm_prompt: "",
    isVisibleInList: false,
    isVisibleInAnalysis: true,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "note",
    name: "Note",
    type: "string",
    llm_prompt: "",
    isVisibleInList: false,
    isVisibleInAnalysis: false,
    isRequired: false,
    isExtra: false,
  },
  {
    code: "vat_rate",
    name: "VAT Rate",
    type: "number",
    llm_prompt: "VAT rate in percentage 0-100",
    isVisibleInList: false,
    isVisibleInAnalysis: false,
    isRequired: false,
    isExtra: true,
  },
  {
    code: "vat",
    name: "VAT Amount",
    type: "number",
    llm_prompt: "total VAT in currency of the invoice",
    isVisibleInList: false,
    isVisibleInAnalysis: false,
    isRequired: false,
    isExtra: true,
  },
  {
    code: "text",
    name: "Extracted Text",
    type: "string",
    llm_prompt: "extract all recognised text from the invoice",
    isVisibleInList: false,
    isVisibleInAnalysis: false,
    isRequired: false,
    isExtra: false,
  },
]

export async function createUserDefaults(userId: string) {
  // Default projects
  for (const project of DEFAULT_PROJECTS) {
    await prisma.project.upsert({
      where: { userId_code: { code: project.code, userId } },
      update: { name: project.name, color: project.color, llm_prompt: project.llm_prompt },
      create: { ...project, userId },
    })
  }

  // Default categories
  for (const category of DEFAULT_CATEGORIES) {
    await prisma.category.upsert({
      where: { userId_code: { code: category.code, userId } },
      update: { name: category.name, color: category.color, llm_prompt: category.llm_prompt },
      create: { ...category, userId },
    })
  }

  // Default currencies
  for (const currency of DEFAULT_CURRENCIES) {
    await prisma.currency.upsert({
      where: { userId_code: { code: currency.code, userId } },
      update: { name: currency.name },
      create: { ...currency, userId },
    })
  }

  // Default fields
  for (const field of DEFAULT_FIELDS) {
    await prisma.field.upsert({
      where: { userId_code: { code: field.code, userId } },
      update: {
        name: field.name,
        type: field.type,
        llm_prompt: field.llm_prompt,
        isVisibleInList: field.isVisibleInList,
        isVisibleInAnalysis: field.isVisibleInAnalysis,
        isRequired: field.isRequired,
        isExtra: field.isExtra,
      },
      create: { ...field, userId },
    })
  }

  // Default settings
  for (const setting of DEFAULT_SETTINGS) {
    await prisma.setting.upsert({
      where: { userId_code: { code: setting.code, userId } },
      update: { name: setting.name, description: setting.description, value: setting.value },
      create: { ...setting, userId },
    })
  }
}

export async function isDatabaseEmpty(userId: string) {
  const fieldsCount = await prisma.field.count({ where: { userId } })
  return fieldsCount === 0
}
```

## File: `models/export_and_import.ts`
```typescript
import { prisma } from "@/lib/db"
import { codeFromName } from "@/lib/utils"
import { formatDate } from "date-fns"
import { createCategory, getCategoryByCode } from "./categories"
import { createProject, getProjectByCode } from "./projects"
import { TransactionFilters } from "./transactions"

export type ExportFilters = TransactionFilters

export type ExportFields = string[]

export type ExportImportFieldSettings = {
  code: string
  type: string
  export?: (userId: string, value: any) => Promise<any>
  import?: (userId: string, value: any) => Promise<any>
}

export const EXPORT_AND_IMPORT_FIELD_MAP: Record<string, ExportImportFieldSettings> = {
  name: {
    code: "name",
    type: "string",
  },
  description: {
    code: "description",
    type: "string",
  },
  merchant: {
    code: "merchant",
    type: "string",
  },
  total: {
    code: "total",
    type: "number",
    export: async function (userId: string, value: number) {
      return value / 100
    },
    import: async function (userId: string, value: string) {
      const num = parseFloat(value)
      return isNaN(num) ? 0.0 : num * 100
    },
  },
  currencyCode: {
    code: "currencyCode",
    type: "string",
  },
  convertedTotal: {
    code: "convertedTotal",
    type: "number",
    export: async function (userId: string, value: number | null) {
      if (!value) {
        return null
      }
      return value / 100
    },
    import: async function (userId: string, value: string) {
      const num = parseFloat(value)
      return isNaN(num) ? 0.0 : num * 100
    },
  },
  convertedCurrencyCode: {
    code: "convertedCurrencyCode",
    type: "string",
  },
  type: {
    code: "type",
    type: "string",
    export: async function (userId: string, value: string | null) {
      return value ? value.toLowerCase() : ""
    },
    import: async function (userId: string, value: string) {
      return value.toLowerCase()
    },
  },
  note: {
    code: "note",
    type: "string",
  },
  categoryCode: {
    code: "categoryCode",
    type: "string",
    export: async function (userId: string, value: string | null) {
      if (!value) {
        return null
      }
      const category = await getCategoryByCode(userId, value)
      return category?.name
    },
    import: async function (userId: string, value: string) {
      const category = await importCategory(userId, value)
      return category?.code
    },
  },
  projectCode: {
    code: "projectCode",
    type: "string",
    export: async function (userId: string, value: string | null) {
      if (!value) {
        return null
      }
      const project = await getProjectByCode(userId, value)
      return project?.name
    },
    import: async function (userId: string, value: string) {
      const project = await importProject(userId, value)
      return project?.code
    },
  },
  issuedAt: {
    code: "issuedAt",
    type: "date",
    export: async function (userId: string, value: Date | null) {
      if (!value || isNaN(value.getTime())) {
        return null
      }

      try {
        return formatDate(value, "yyyy-MM-dd")
      } catch (error) {
        return null
      }
    },
    import: async function (userId: string, value: string) {
      try {
        return new Date(value)
      } catch (error) {
        return null
      }
    },
  },
}

export const importProject = async (userId: string, name: string) => {
  const code = codeFromName(name)

  const existingProject = await prisma.project.findFirst({
    where: {
      OR: [{ code }, { name }],
    },
  })

  if (existingProject) {
    return existingProject
  }

  return await createProject(userId, { code, name })
}

export const importCategory = async (userId: string, name: string) => {
  const code = codeFromName(name)

  const existingCategory = await prisma.category.findFirst({
    where: {
      OR: [{ code }, { name }],
    },
  })

  if (existingCategory) {
    return existingCategory
  }

  return await createCategory(userId, { code, name })
}
```

## File: `models/fields.ts`
```typescript
import { prisma } from "@/lib/db"
import { codeFromName } from "@/lib/utils"
import { Prisma } from "@/prisma/client"
import { cache } from "react"

export type FieldData = {
  [key: string]: unknown
}

export const getFields = cache(async (userId: string) => {
  return await prisma.field.findMany({
    where: { userId },
    orderBy: {
      createdAt: "asc",
    },
  })
})

export const createField = async (userId: string, field: FieldData) => {
  if (!field.code) {
    field.code = codeFromName(field.name as string)
  }
  return await prisma.field.create({
    data: {
      ...field,
      user: {
        connect: {
          id: userId,
        },
      },
    } as Prisma.FieldCreateInput,
  })
}

export const updateField = async (userId: string, code: string, field: FieldData) => {
  return await prisma.field.update({
    where: { userId_code: { code, userId } },
    data: field,
  })
}

export const deleteField = async (userId: string, code: string) => {
  return await prisma.field.delete({
    where: { userId_code: { code, userId } },
  })
}
```

## File: `models/files.ts`
```typescript
"use server"

import { prisma } from "@/lib/db"
import { unlink } from "fs/promises"
import path from "path"
import { cache } from "react"
import { getTransactionById } from "./transactions"

export const getUnsortedFiles = cache(async (userId: string) => {
  return await prisma.file.findMany({
    where: {
      isReviewed: false,
      userId,
    },
    orderBy: {
      createdAt: "desc",
    },
  })
})

export const getUnsortedFilesCount = cache(async (userId: string) => {
  return await prisma.file.count({
    where: {
      isReviewed: false,
      userId,
    },
  })
})

export const getFileById = cache(async (id: string, userId: string) => {
  return await prisma.file.findFirst({
    where: { id, userId },
  })
})

export const getFilesByTransactionId = cache(async (id: string, userId: string) => {
  const transaction = await getTransactionById(id, userId)
  if (transaction && transaction.files) {
    return await prisma.file.findMany({
      where: {
        id: {
          in: transaction.files as string[],
        },
        userId,
      },
      orderBy: {
        createdAt: "asc",
      },
    })
  }
  return []
})

export const createFile = async (userId: string, data: any) => {
  return await prisma.file.create({
    data: {
      ...data,
      userId,
    },
  })
}

export const updateFile = async (id: string, userId: string, data: any) => {
  return await prisma.file.update({
    where: { id, userId },
    data,
  })
}

export const deleteFile = async (id: string, userId: string) => {
  const file = await getFileById(id, userId)
  if (!file) {
    return
  }

  try {
    await unlink(path.resolve(path.normalize(file.path)))
  } catch (error) {
    console.error("Error deleting file:", error)
  }

  return await prisma.file.delete({
    where: { id, userId },
  })
}
```

## File: `models/progress.ts`
```typescript
import { prisma } from "@/lib/db"

export const getOrCreateProgress = async (
  userId: string,
  id: string,
  type: string | null = null,
  data: any = null,
  total: number = 0
) => {
  return await prisma.progress.upsert({
    where: { id },
    create: {
      id,
      user: { connect: { id: userId } },
      type: type || "unknown",
      data,
      total,
    },
    update: {
      // Don't update existing progress
    },
  })
}

export const getProgressById = async (userId: string, id: string) => {
  return await prisma.progress.findFirst({
    where: { id, userId },
  })
}

export const updateProgress = async (
  userId: string,
  id: string,
  fields: { current?: number; total?: number; data?: any }
) => {
  return await prisma.progress.updateMany({
    where: { id, userId },
    data: fields,
  })
}

export const incrementProgress = async (userId: string, id: string, amount: number = 1) => {
  return await prisma.progress.updateMany({
    where: { id, userId },
    data: {
      current: { increment: amount },
    },
  })
}

export const getAllProgressByUser = async (userId: string) => {
  return await prisma.progress.findMany({
    where: { userId },
    orderBy: { createdAt: "desc" },
  })
}

export const deleteProgress = async (userId: string, id: string) => {
  return await prisma.progress.deleteMany({
    where: { id, userId },
  })
}
```

## File: `models/projects.ts`
```typescript
import { prisma } from "@/lib/db"
import { codeFromName } from "@/lib/utils"
import { Prisma } from "@/prisma/client"
import { cache } from "react"

export type ProjectData = {
  [key: string]: unknown
}

export const getProjects = cache(async (userId: string) => {
  return await prisma.project.findMany({
    where: { userId },
    orderBy: {
      name: "asc",
    },
  })
})

export const getProjectByCode = cache(async (userId: string, code: string) => {
  return await prisma.project.findUnique({
    where: { userId_code: { code, userId } },
  })
})

export const createProject = async (userId: string, project: ProjectData) => {
  if (!project.code) {
    project.code = codeFromName(project.name as string)
  }
  return await prisma.project.create({
    data: {
      ...project,
      user: {
        connect: {
          id: userId,
        },
      },
    } as Prisma.ProjectCreateInput,
  })
}

export const updateProject = async (userId: string, code: string, project: ProjectData) => {
  return await prisma.project.update({
    where: { userId_code: { code, userId } },
    data: project,
  })
}

export const deleteProject = async (userId: string, code: string) => {
  await prisma.transaction.updateMany({
    where: {
      userId,
      projectCode: code,
    },
    data: {
      projectCode: null,
    },
  })

  return await prisma.project.delete({
    where: { userId_code: { code, userId } },
  })
}
```

## File: `models/settings.ts`
```typescript
import { prisma } from "@/lib/db"
import { PROVIDERS } from "@/lib/llm-providers"
import { cache } from "react"
import { LLMProvider } from "@/ai/providers/llmProvider"

export type SettingsMap = Record<string, string>

/**
 * Helper to extract LLM provider settings from SettingsMap.
 */
export function getLLMSettings(settings: SettingsMap) {
  const priorities = (settings.llm_providers || "openai,google,mistral").split(",").map(p => p.trim()).filter(Boolean)

  const providers = priorities.map((provider) => {
    if (provider === "openai") {
      return {
        provider: provider as LLMProvider,
        apiKey: settings.openai_api_key || "",
        model: settings.openai_model_name || PROVIDERS[0]['defaultModelName'],
      }
    }
    if (provider === "google") {
      return {
        provider: provider as LLMProvider,
        apiKey: settings.google_api_key || "",
        model: settings.google_model_name || PROVIDERS[1]['defaultModelName'],
      }
    }
    if (provider === "mistral") {
      return {
        provider: provider as LLMProvider,
        apiKey: settings.mistral_api_key || "",
        model: settings.mistral_model_name || PROVIDERS[2]['defaultModelName'],
      }
    }
    return null
  }).filter((provider): provider is NonNullable<typeof provider> => provider !== null)

  return {
    providers,
  }
}

export const getSettings = cache(async (userId: string): Promise<SettingsMap> => {
  const settings = await prisma.setting.findMany({
    where: { userId },
  })

  return settings.reduce((acc, setting) => {
    acc[setting.code] = setting.value || ""
    return acc
  }, {} as SettingsMap)
})

export const updateSettings = cache(async (userId: string, code: string, value: string | undefined) => {
  return await prisma.setting.upsert({
    where: { userId_code: { code, userId } },
    update: { value },
    create: {
      code,
      value,
      name: code,
      userId,
    },
  })
})
```

## File: `models/stats.ts`
```typescript
import { prisma } from "@/lib/db"
import { calcTotalPerCurrency } from "@/lib/stats"
import { Prisma } from "@/prisma/client"
import { cache } from "react"
import { TransactionFilters } from "./transactions"

export type DashboardStats = {
  totalIncomePerCurrency: Record<string, number>
  totalExpensesPerCurrency: Record<string, number>
  profitPerCurrency: Record<string, number>
  invoicesProcessed: number
}

export const getDashboardStats = cache(
  async (userId: string, filters: TransactionFilters = {}): Promise<DashboardStats> => {
    const where: Prisma.TransactionWhereInput = {}

    if (filters.dateFrom || filters.dateTo) {
      where.issuedAt = {
        gte: filters.dateFrom ? new Date(filters.dateFrom) : undefined,
        lte: filters.dateTo ? new Date(filters.dateTo) : undefined,
      }
    }

    const transactions = await prisma.transaction.findMany({ where: { ...where, userId } })
    const totalIncomePerCurrency = calcTotalPerCurrency(transactions.filter((t) => t.type === "income"))
    const totalExpensesPerCurrency = calcTotalPerCurrency(transactions.filter((t) => t.type === "expense"))
    const profitPerCurrency = Object.fromEntries(
      Object.keys(totalIncomePerCurrency).map((currency) => [
        currency,
        totalIncomePerCurrency[currency] - totalExpensesPerCurrency[currency],
      ])
    )
    const invoicesProcessed = transactions.length

    return {
      totalIncomePerCurrency,
      totalExpensesPerCurrency,
      profitPerCurrency,
      invoicesProcessed,
    }
  }
)

export type ProjectStats = {
  totalIncomePerCurrency: Record<string, number>
  totalExpensesPerCurrency: Record<string, number>
  profitPerCurrency: Record<string, number>
  invoicesProcessed: number
}

export const getProjectStats = cache(async (userId: string, projectId: string, filters: TransactionFilters = {}) => {
  const where: Prisma.TransactionWhereInput = {
    projectCode: projectId,
  }

  if (filters.dateFrom || filters.dateTo) {
    where.issuedAt = {
      gte: filters.dateFrom ? new Date(filters.dateFrom) : undefined,
      lte: filters.dateTo ? new Date(filters.dateTo) : undefined,
    }
  }

  const transactions = await prisma.transaction.findMany({ where: { ...where, userId } })
  const totalIncomePerCurrency = calcTotalPerCurrency(transactions.filter((t) => t.type === "income"))
  const totalExpensesPerCurrency = calcTotalPerCurrency(transactions.filter((t) => t.type === "expense"))
  const profitPerCurrency = Object.fromEntries(
    Object.keys(totalIncomePerCurrency).map((currency) => [
      currency,
      totalIncomePerCurrency[currency] - totalExpensesPerCurrency[currency],
    ])
  )

  const invoicesProcessed = transactions.length
  return {
    totalIncomePerCurrency,
    totalExpensesPerCurrency,
    profitPerCurrency,
    invoicesProcessed,
  }
})

export type TimeSeriesData = {
  period: string
  income: number
  expenses: number
  date: Date
}

export type CategoryBreakdown = {
  code: string
  name: string
  color: string
  income: number
  expenses: number
  transactionCount: number
}

export type DetailedTimeSeriesData = {
  period: string
  income: number
  expenses: number
  date: Date
  categories: CategoryBreakdown[]
  totalTransactions: number
}

export const getTimeSeriesStats = cache(
  async (
    userId: string,
    filters: TransactionFilters = {},
    defaultCurrency: string = "EUR"
  ): Promise<TimeSeriesData[]> => {
    const where: Prisma.TransactionWhereInput = { userId }

    if (filters.dateFrom || filters.dateTo) {
      where.issuedAt = {
        gte: filters.dateFrom ? new Date(filters.dateFrom) : undefined,
        lte: filters.dateTo ? new Date(filters.dateTo) : undefined,
      }
    }

    if (filters.categoryCode) {
      where.categoryCode = filters.categoryCode
    }

    if (filters.projectCode) {
      where.projectCode = filters.projectCode
    }

    if (filters.type) {
      where.type = filters.type
    }

    const transactions = await prisma.transaction.findMany({
      where,
      orderBy: { issuedAt: "asc" },
    })

    if (transactions.length === 0) {
      return []
    }

    // Determine if we should group by day or month
    const dateFrom = filters.dateFrom ? new Date(filters.dateFrom) : new Date(transactions[0].issuedAt!)
    const dateTo = filters.dateTo ? new Date(filters.dateTo) : new Date(transactions[transactions.length - 1].issuedAt!)
    const daysDiff = Math.ceil((dateTo.getTime() - dateFrom.getTime()) / (1000 * 60 * 60 * 24))
    const groupByDay = daysDiff <= 50

    // Group transactions by time period
    const grouped = transactions.reduce(
      (acc, transaction) => {
        if (!transaction.issuedAt) return acc

        const date = new Date(transaction.issuedAt)
        const period = groupByDay
          ? date.toISOString().split("T")[0] // YYYY-MM-DD
          : `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}` // YYYY-MM

        if (!acc[period]) {
          acc[period] = { period, income: 0, expenses: 0, date }
        }

        // Get amount in default currency
        const amount =
          transaction.convertedCurrencyCode?.toUpperCase() === defaultCurrency.toUpperCase()
            ? transaction.convertedTotal || 0
            : transaction.currencyCode?.toUpperCase() === defaultCurrency.toUpperCase()
              ? transaction.total || 0
              : 0 // Skip transactions not in default currency for simplicity

        if (transaction.type === "income") {
          acc[period].income += amount
        } else if (transaction.type === "expense") {
          acc[period].expenses += amount
        }

        return acc
      },
      {} as Record<string, TimeSeriesData>
    )

    return Object.values(grouped).sort((a, b) => a.date.getTime() - b.date.getTime())
  }
)

export const getDetailedTimeSeriesStats = cache(
  async (
    userId: string,
    filters: TransactionFilters = {},
    defaultCurrency: string = "EUR"
  ): Promise<DetailedTimeSeriesData[]> => {
    const where: Prisma.TransactionWhereInput = { userId }

    if (filters.dateFrom || filters.dateTo) {
      where.issuedAt = {
        gte: filters.dateFrom ? new Date(filters.dateFrom) : undefined,
        lte: filters.dateTo ? new Date(filters.dateTo) : undefined,
      }
    }

    if (filters.categoryCode) {
      where.categoryCode = filters.categoryCode
    }

    if (filters.projectCode) {
      where.projectCode = filters.projectCode
    }

    if (filters.type) {
      where.type = filters.type
    }

    const [transactions, categories] = await Promise.all([
      prisma.transaction.findMany({
        where,
        include: {
          category: true,
        },
        orderBy: { issuedAt: "asc" },
      }),
      prisma.category.findMany({
        where: { userId },
        orderBy: { name: "asc" },
      }),
    ])

    if (transactions.length === 0) {
      return []
    }

    // Determine if we should group by day or month
    const dateFrom = filters.dateFrom ? new Date(filters.dateFrom) : new Date(transactions[0].issuedAt!)
    const dateTo = filters.dateTo ? new Date(filters.dateTo) : new Date(transactions[transactions.length - 1].issuedAt!)
    const daysDiff = Math.ceil((dateTo.getTime() - dateFrom.getTime()) / (1000 * 60 * 60 * 24))
    const groupByDay = daysDiff <= 50

    // Create category lookup
    const categoryLookup = new Map(categories.map((cat) => [cat.code, cat]))

    // Group transactions by time period
    const grouped = transactions.reduce(
      (acc, transaction) => {
        if (!transaction.issuedAt) return acc

        const date = new Date(transaction.issuedAt)
        const period = groupByDay
          ? date.toISOString().split("T")[0] // YYYY-MM-DD
          : `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}` // YYYY-MM

        if (!acc[period]) {
          acc[period] = {
            period,
            income: 0,
            expenses: 0,
            date,
            categories: new Map<string, CategoryBreakdown>(),
            totalTransactions: 0,
          }
        }

        // Get amount in default currency
        const amount =
          transaction.convertedCurrencyCode?.toUpperCase() === defaultCurrency.toUpperCase()
            ? transaction.convertedTotal || 0
            : transaction.currencyCode?.toUpperCase() === defaultCurrency.toUpperCase()
              ? transaction.total || 0
              : 0 // Skip transactions not in default currency for simplicity

        const categoryCode = transaction.categoryCode || "other"
        const category = categoryLookup.get(categoryCode) || {
          code: "other",
          name: "Other",
          color: "#6b7280",
        }

        // Initialize category if not exists
        if (!acc[period].categories.has(categoryCode)) {
          acc[period].categories.set(categoryCode, {
            code: category.code,
            name: category.name,
            color: category.color || "#6b7280",
            income: 0,
            expenses: 0,
            transactionCount: 0,
          })
        }

        const categoryData = acc[period].categories.get(categoryCode)!
        categoryData.transactionCount++
        acc[period].totalTransactions++

        if (transaction.type === "income") {
          acc[period].income += amount
          categoryData.income += amount
        } else if (transaction.type === "expense") {
          acc[period].expenses += amount
          categoryData.expenses += amount
        }

        return acc
      },
      {} as Record<
        string,
        {
          period: string
          income: number
          expenses: number
          date: Date
          categories: Map<string, CategoryBreakdown>
          totalTransactions: number
        }
      >
    )

    return Object.values(grouped)
      .map((item) => ({
        ...item,
        categories: Array.from(item.categories.values()).filter((cat) => cat.income > 0 || cat.expenses > 0),
      }))
      .sort((a, b) => a.date.getTime() - b.date.getTime())
  }
)
```

## File: `models/transactions.ts`
```typescript
import { prisma } from "@/lib/db"
import { Field, Prisma, Transaction } from "@/prisma/client"
import { cache } from "react"
import { getFields } from "./fields"
import { deleteFile } from "./files"

export type TransactionData = {
  name?: string | null
  description?: string | null
  merchant?: string | null
  total?: number | null
  currencyCode?: string | null
  convertedTotal?: number | null
  convertedCurrencyCode?: string | null
  type?: string | null
  items?: TransactionData[] | undefined
  note?: string | null
  files?: string[] | undefined
  extra?: Record<string, unknown>
  categoryCode?: string | null
  projectCode?: string | null
  issuedAt?: Date | string | null
  text?: string | null
  [key: string]: unknown
}

export type TransactionFilters = {
  search?: string
  dateFrom?: string
  dateTo?: string
  ordering?: string
  categoryCode?: string
  projectCode?: string
  type?: string
  page?: number
}

export type TransactionPagination = {
  limit: number
  offset: number
}

export const getTransactions = cache(
  async (
    userId: string,
    filters?: TransactionFilters,
    pagination?: TransactionPagination
  ): Promise<{
    transactions: Transaction[]
    total: number
  }> => {
    const where: Prisma.TransactionWhereInput = { userId }
    let orderBy: Prisma.TransactionOrderByWithRelationInput = { issuedAt: "desc" }

    if (filters) {
      if (filters.search) {
        where.OR = [
          { name: { contains: filters.search, mode: "insensitive" } },
          { merchant: { contains: filters.search, mode: "insensitive" } },
          { description: { contains: filters.search, mode: "insensitive" } },
          { note: { contains: filters.search, mode: "insensitive" } },
          { text: { contains: filters.search, mode: "insensitive" } },
        ]
      }

      if (filters.dateFrom || filters.dateTo) {
        where.issuedAt = {
          gte: filters.dateFrom ? new Date(filters.dateFrom) : undefined,
          lte: filters.dateTo ? new Date(filters.dateTo) : undefined,
        }
      }

      if (filters.categoryCode) {
        where.categoryCode = filters.categoryCode
      }

      if (filters.projectCode) {
        where.projectCode = filters.projectCode
      }

      if (filters.type) {
        where.type = filters.type
      }

      if (filters.ordering) {
        const isDesc = filters.ordering.startsWith("-")
        const field = isDesc ? filters.ordering.slice(1) : filters.ordering
        orderBy = { [field]: isDesc ? "desc" : "asc" }
      }
    }

    if (pagination) {
      const total = await prisma.transaction.count({ where })
      const transactions = await prisma.transaction.findMany({
        where,
        include: {
          category: true,
          project: true,
        },
        orderBy,
        take: pagination?.limit,
        skip: pagination?.offset,
      })
      return { transactions, total }
    } else {
      const transactions = await prisma.transaction.findMany({
        where,
        include: {
          category: true,
          project: true,
        },
        orderBy,
      })
      return { transactions, total: transactions.length }
    }
  }
)

export const getTransactionById = cache(async (id: string, userId: string): Promise<Transaction | null> => {
  return await prisma.transaction.findUnique({
    where: { id, userId },
    include: {
      category: true,
      project: true,
    },
  })
})

export const getTransactionsByFileId = cache(async (fileId: string, userId: string): Promise<Transaction[]> => {
  return await prisma.transaction.findMany({
    where: { files: { array_contains: [fileId] }, userId },
  })
})

export const createTransaction = async (userId: string, data: TransactionData): Promise<Transaction> => {
  const { standard, extra } = await splitTransactionDataExtraFields(data, userId)

  return await prisma.transaction.create({
    data: {
      ...standard,
      extra: extra,
      items: data.items as Prisma.InputJsonValue,
      userId,
    },
  })
}

export const updateTransaction = async (id: string, userId: string, data: TransactionData): Promise<Transaction> => {
  const { standard, extra } = await splitTransactionDataExtraFields(data, userId)

  return await prisma.transaction.update({
    where: { id, userId },
    data: {
      ...standard,
      extra: extra,
      items: data.items ? (data.items as Prisma.InputJsonValue) : [],
    },
  })
}

export const updateTransactionFiles = async (id: string, userId: string, files: string[]): Promise<Transaction> => {
  return await prisma.transaction.update({
    where: { id, userId },
    data: { files },
  })
}

export const deleteTransaction = async (id: string, userId: string): Promise<Transaction | undefined> => {
  const transaction = await getTransactionById(id, userId)

  if (transaction) {
    const files = Array.isArray(transaction.files) ? transaction.files : []

    for (const fileId of files as string[]) {
      if ((await getTransactionsByFileId(fileId, userId)).length <= 1) {
        await deleteFile(fileId, userId)
      }
    }

    return await prisma.transaction.delete({
      where: { id, userId },
    })
  }
}

export const bulkDeleteTransactions = async (ids: string[], userId: string) => {
  return await prisma.transaction.deleteMany({
    where: { id: { in: ids }, userId },
  })
}

const splitTransactionDataExtraFields = async (
  data: TransactionData,
  userId: string
): Promise<{ standard: TransactionData; extra: Prisma.InputJsonValue }> => {
  const fields = await getFields(userId)
  const fieldMap = fields.reduce(
    (acc, field) => {
      acc[field.code] = field
      return acc
    },
    {} as Record<string, Field>
  )

  const standard: TransactionData = {}
  const extra: Record<string, unknown> = {}

  Object.entries(data).forEach(([key, value]) => {
    const fieldDef = fieldMap[key]
    if (fieldDef) {
      if (fieldDef.isExtra) {
        extra[key] = value
      } else {
        standard[key] = value
      }
    }
  })

  return { standard, extra: extra as Prisma.InputJsonValue }
}
```

## File: `models/users.ts`
```typescript
import { prisma } from "@/lib/db"
import { Prisma } from "@/prisma/client"
import { cache } from "react"
import { isDatabaseEmpty } from "./defaults"
import { createUserDefaults } from "./defaults"

export const SELF_HOSTED_USER = {
  email: "taxhacker@localhost",
  name: "Self-Hosted Mode",
  membershipPlan: "unlimited",
}

export const getSelfHostedUser = cache(async () => {
  if (!process.env.DATABASE_URL) {
    return null // fix for CI, do not remove
  }

  return await prisma.user.findFirst({
    where: { email: SELF_HOSTED_USER.email },
  })
})

export const getOrCreateSelfHostedUser = cache(async () => {
  return await prisma.user.upsert({
    where: { email: SELF_HOSTED_USER.email },
    update: SELF_HOSTED_USER,
    create: SELF_HOSTED_USER,
  })
})

export async function getOrCreateCloudUser(email: string, data: Prisma.UserCreateInput) {
  const user = await prisma.user.upsert({
    where: { email: email.toLowerCase() },
    update: data,
    create: data,
  })

  if (await isDatabaseEmpty(user.id)) {
    await createUserDefaults(user.id)
  }
  
  return user
}

export const getUserById = cache(async (id: string) => {
  return await prisma.user.findUnique({
    where: { id },
  })
})

export const getUserByEmail = cache(async (email: string) => {
  return await prisma.user.findUnique({
    where: { email: email.toLowerCase() },
  })
})

export const getUserByStripeCustomerId = cache(async (customerId: string) => {
  return await prisma.user.findFirst({
    where: { stripeCustomerId: customerId },
  })
})

export function updateUser(userId: string, data: Prisma.UserUpdateInput) {
  return prisma.user.update({
    where: { id: userId },
    data,
  })
}
```

## File: `prisma/schema.prisma`
```
// This is your Prisma schema file,
// learn more about it in the docs: https://pris.ly/d/prisma-schema

generator client {
  provider = "prisma-client-js"
  output   = "client"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id                  String        @id @default(uuid()) @db.Uuid
  email               String        @unique
  name                String
  avatar              String?
  settings            Setting[]
  categories          Category[]
  projects            Project[]
  fields              Field[]
  files               File[]
  currencies          Currency[]
  transactions        Transaction[]
  createdAt           DateTime      @default(now()) @map("created_at")
  updatedAt           DateTime      @updatedAt @map("updated_at")
  stripeCustomerId    String?       @map("stripe_customer_id")
  membershipPlan      String?       @map("membership_plan")
  membershipExpiresAt DateTime?     @map("membership_expires_at")
  emailVerified       Boolean       @default(false) @map("is_email_verified")
  storageUsed         Int           @default(0) @map("storage_used")
  storageLimit        Int           @default(-1) @map("storage_limit")
  aiBalance           Int           @default(0) @map("ai_balance")
  businessName        String?       @map("business_name")
  businessAddress     String?       @map("business_address")
  businessBankDetails String?       @map("business_bank_details")
  businessLogo        String?       @map("business_logo")
  accounts            Account[]
  sessions            Session[]
  appData             AppData[]
  progress            Progress[]

  @@map("users")
}

model Session {
  id        String   @id @default(uuid()) @db.Uuid
  token     String
  expiresAt DateTime @map("expires_at")
  createdAt DateTime @default(now()) @map("created_at")
  updatedAt DateTime @updatedAt @map("updated_at")
  ipAddress String?  @map("ip_address")
  userAgent String?  @map("user_agent")
  userId    String   @map("user_id") @db.Uuid
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@unique([token])
  @@map("sessions")
}

model Account {
  id                    String    @id
  accountId             String    @map("account_id")
  providerId            String    @map("provider_id")
  userId                String    @map("user_id") @db.Uuid
  user                  User      @relation(fields: [userId], references: [id], onDelete: Cascade)
  accessToken           String?   @map("access_token")
  refreshToken          String?   @map("refresh_token")
  idToken               String?   @map("id_token")
  accessTokenExpiresAt  DateTime? @map("access_token_expires_at")
  refreshTokenExpiresAt DateTime? @map("refresh_token_expires_at")
  scope                 String?
  password              String?
  createdAt             DateTime  @default(now()) @map("created_at")
  updatedAt             DateTime  @updatedAt @map("updated_at")

  @@map("account")
}

model Verification {
  id         String   @id @default(uuid()) @db.Uuid
  identifier String
  value      String
  expiresAt  DateTime @map("expires_at")
  createdAt  DateTime @default(now()) @map("created_at")
  updatedAt  DateTime @updatedAt @map("updated_at")

  @@map("verification")
}

model Setting {
  id          String  @id @default(uuid()) @db.Uuid
  userId      String  @map("user_id") @db.Uuid
  user        User    @relation(fields: [userId], references: [id], onDelete: Cascade)
  code        String
  name        String
  description String?
  value       String?

  @@unique([userId, code])
  @@map("settings")
}

model Category {
  id           String        @id @default(uuid()) @db.Uuid
  userId       String        @map("user_id") @db.Uuid
  user         User?         @relation(fields: [userId], references: [id], onDelete: Cascade)
  code         String
  name         String
  color        String        @default("#000000")
  llm_prompt   String?
  transactions Transaction[]
  createdAt    DateTime      @default(now()) @map("created_at")

  @@unique([userId, code])
  @@map("categories")
}

model Project {
  id           String        @id @default(uuid()) @db.Uuid
  userId       String        @map("user_id") @db.Uuid
  user         User          @relation(fields: [userId], references: [id], onDelete: Cascade)
  code         String
  name         String
  color        String        @default("#000000")
  llm_prompt   String?
  transactions Transaction[]
  createdAt    DateTime      @default(now()) @map("created_at")

  @@unique([userId, code])
  @@map("projects")
}

model Field {
  id                  String   @id @default(uuid()) @db.Uuid
  userId              String   @map("user_id") @db.Uuid
  user                User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  code                String
  name                String
  type                String   @default("string")
  llm_prompt          String?
  options             Json?
  createdAt           DateTime @default(now()) @map("created_at")
  isVisibleInList     Boolean  @default(false) @map("is_visible_in_list")
  isVisibleInAnalysis Boolean  @default(false) @map("is_visible_in_analysis")
  isRequired          Boolean  @default(false) @map("is_required")
  isExtra             Boolean  @default(true) @map("is_extra")

  @@unique([userId, code])
  @@map("fields")
}

model File {
  id                String   @id @default(uuid()) @db.Uuid
  userId            String   @map("user_id") @db.Uuid
  user              User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  filename          String
  path              String
  mimetype          String
  metadata          Json?
  isReviewed        Boolean  @default(false) @map("is_reviewed")
  isSplitted        Boolean  @default(false) @map("is_splitted")
  cachedParseResult Json?    @map("cached_parse_result")
  createdAt         DateTime @default(now()) @map("created_at")

  @@map("files")
}

model Transaction {
  id                    String    @id @default(uuid()) @db.Uuid
  userId                String    @map("user_id") @db.Uuid
  user                  User      @relation(fields: [userId], references: [id], onDelete: Cascade)
  name                  String?
  description           String?
  merchant              String?
  total                 Int?
  currencyCode          String?   @map("currency_code")
  convertedTotal        Int?      @map("converted_total")
  convertedCurrencyCode String?   @map("converted_currency_code")
  type                  String?   @default("expense")
  items                 Json      @default("[]")
  note                  String?
  files                 Json      @default("[]")
  extra                 Json?
  category              Category? @relation(fields: [categoryCode, userId], references: [code, userId])
  categoryCode          String?   @map("category_code")
  project               Project?  @relation(fields: [projectCode, userId], references: [code, userId])
  projectCode           String?   @map("project_code")
  issuedAt              DateTime? @map("issued_at")
  createdAt             DateTime  @default(now()) @map("created_at")
  updatedAt             DateTime  @updatedAt @map("updated_at")
  text                  String?

  @@index([userId])
  @@index([projectCode])
  @@index([categoryCode])
  @@index([issuedAt])
  @@index([name])
  @@index([merchant])
  @@index([total])
  @@map("transactions")
}

model Currency {
  id     String  @id @default(uuid()) @db.Uuid
  userId String? @map("user_id") @db.Uuid
  user   User?   @relation(fields: [userId], references: [id], onDelete: Cascade)
  code   String
  name   String

  @@unique([userId, code])
  @@map("currencies")
}

model AppData {
  id     String @id @default(uuid()) @db.Uuid
  app    String
  userId String @map("user_id") @db.Uuid
  user   User   @relation(fields: [userId], references: [id], onDelete: Cascade)
  data   Json

  @@unique([userId, app])
  @@map("app_data")
}

model Progress {
  id        String   @id @default(uuid()) @db.Uuid
  userId    String   @map("user_id") @db.Uuid
  user      User     @relation(fields: [userId], references: [id], onDelete: Cascade)
  type      String
  data      Json?
  current   Int      @default(0)
  total     Int      @default(0)
  createdAt DateTime @default(now()) @map("created_at")

  @@index([userId])
  @@map("progress")
}
```

## File: `prisma/migrations/migration_lock.toml`
```
# Please do not edit this file manually
# It should be added in your version-control system (e.g., Git)
provider = "postgresql"
```

## File: `prisma/migrations/20250403104933_init/migration.sql`
```sql
-- CreateTable
CREATE TABLE "users" (
    "id" UUID NOT NULL,
    "email" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "avatar" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "membership_plan" TEXT,
    "membership_expires_at" TIMESTAMP(3),
    "is_email_verified" BOOLEAN NOT NULL DEFAULT false,
    "image" TEXT,

    CONSTRAINT "users_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "sessions" (
    "id" UUID NOT NULL,
    "token" TEXT NOT NULL,
    "expires_at" TIMESTAMP(3) NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "ip_address" TEXT,
    "user_agent" TEXT,
    "user_id" UUID NOT NULL,

    CONSTRAINT "sessions_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "account" (
    "id" TEXT NOT NULL,
    "account_id" TEXT NOT NULL,
    "provider_id" TEXT NOT NULL,
    "user_id" UUID NOT NULL,
    "access_token" TEXT,
    "refresh_token" TEXT,
    "id_token" TEXT,
    "access_token_expires_at" TIMESTAMP(3),
    "refresh_token_expires_at" TIMESTAMP(3),
    "scope" TEXT,
    "password" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "account_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "verification" (
    "id" UUID NOT NULL,
    "identifier" TEXT NOT NULL,
    "value" TEXT NOT NULL,
    "expires_at" TIMESTAMP(3) NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "verification_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "settings" (
    "id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "code" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT,
    "value" TEXT,

    CONSTRAINT "settings_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "categories" (
    "id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "code" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "color" TEXT NOT NULL DEFAULT '#000000',
    "llm_prompt" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "categories_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "projects" (
    "id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "code" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "color" TEXT NOT NULL DEFAULT '#000000',
    "llm_prompt" TEXT,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "projects_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "fields" (
    "id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "code" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "type" TEXT NOT NULL DEFAULT 'string',
    "llm_prompt" TEXT,
    "options" JSONB,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "is_visible_in_list" BOOLEAN NOT NULL DEFAULT false,
    "is_visible_in_analysis" BOOLEAN NOT NULL DEFAULT false,
    "is_required" BOOLEAN NOT NULL DEFAULT false,
    "is_extra" BOOLEAN NOT NULL DEFAULT true,

    CONSTRAINT "fields_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "files" (
    "id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "filename" TEXT NOT NULL,
    "path" TEXT NOT NULL,
    "mimetype" TEXT NOT NULL,
    "metadata" JSONB,
    "is_reviewed" BOOLEAN NOT NULL DEFAULT false,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "files_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "transactions" (
    "id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "name" TEXT,
    "description" TEXT,
    "merchant" TEXT,
    "total" INTEGER,
    "currency_code" TEXT,
    "converted_total" INTEGER,
    "converted_currency_code" TEXT,
    "type" TEXT DEFAULT 'expense',
    "note" TEXT,
    "files" JSONB NOT NULL DEFAULT '[]',
    "extra" JSONB,
    "category_code" TEXT,
    "project_code" TEXT,
    "issued_at" TIMESTAMP(3),
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,
    "text" TEXT,

    CONSTRAINT "transactions_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "currencies" (
    "id" UUID NOT NULL,
    "user_id" UUID,
    "code" TEXT NOT NULL,
    "name" TEXT NOT NULL,

    CONSTRAINT "currencies_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "users_email_key" ON "users"("email");

-- CreateIndex
CREATE UNIQUE INDEX "sessions_token_key" ON "sessions"("token");

-- CreateIndex
CREATE UNIQUE INDEX "settings_user_id_code_key" ON "settings"("user_id", "code");

-- CreateIndex
CREATE UNIQUE INDEX "categories_user_id_code_key" ON "categories"("user_id", "code");

-- CreateIndex
CREATE UNIQUE INDEX "projects_user_id_code_key" ON "projects"("user_id", "code");

-- CreateIndex
CREATE UNIQUE INDEX "fields_user_id_code_key" ON "fields"("user_id", "code");

-- CreateIndex
CREATE INDEX "transactions_user_id_idx" ON "transactions"("user_id");

-- CreateIndex
CREATE INDEX "transactions_project_code_idx" ON "transactions"("project_code");

-- CreateIndex
CREATE INDEX "transactions_category_code_idx" ON "transactions"("category_code");

-- CreateIndex
CREATE INDEX "transactions_issued_at_idx" ON "transactions"("issued_at");

-- CreateIndex
CREATE INDEX "transactions_name_idx" ON "transactions"("name");

-- CreateIndex
CREATE INDEX "transactions_merchant_idx" ON "transactions"("merchant");

-- CreateIndex
CREATE INDEX "transactions_total_idx" ON "transactions"("total");

-- CreateIndex
CREATE UNIQUE INDEX "currencies_user_id_code_key" ON "currencies"("user_id", "code");

-- AddForeignKey
ALTER TABLE "sessions" ADD CONSTRAINT "sessions_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "account" ADD CONSTRAINT "account_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "settings" ADD CONSTRAINT "settings_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "categories" ADD CONSTRAINT "categories_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "projects" ADD CONSTRAINT "projects_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "fields" ADD CONSTRAINT "fields_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "files" ADD CONSTRAINT "files_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "transactions" ADD CONSTRAINT "transactions_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "transactions" ADD CONSTRAINT "transactions_category_code_user_id_fkey" FOREIGN KEY ("category_code", "user_id") REFERENCES "categories"("code", "user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "transactions" ADD CONSTRAINT "transactions_project_code_user_id_fkey" FOREIGN KEY ("project_code", "user_id") REFERENCES "projects"("code", "user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "currencies" ADD CONSTRAINT "currencies_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

## File: `prisma/migrations/20250410130313_add_storage/migration.sql`
```sql
/*
  Warnings:

  - You are about to drop the column `image` on the `users` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "users" DROP COLUMN "image",
ADD COLUMN     "storage_used" INTEGER DEFAULT 0,
ADD COLUMN     "token_balance" INTEGER DEFAULT 0;
```

## File: `prisma/migrations/20250421102306_token_limit/migration.sql`
```sql
-- AlterTable
ALTER TABLE "users" ADD COLUMN     "storage_limit" INTEGER DEFAULT -1;
```

## File: `prisma/migrations/20250421113343_limits_not_null/migration.sql`
```sql
/*
  Warnings:

  - Made the column `storage_used` on table `users` required. This step will fail if there are existing NULL values in that column.
  - Made the column `token_balance` on table `users` required. This step will fail if there are existing NULL values in that column.
  - Made the column `storage_limit` on table `users` required. This step will fail if there are existing NULL values in that column.

*/
-- AlterTable
ALTER TABLE "users" ALTER COLUMN "storage_used" SET NOT NULL,
ALTER COLUMN "token_balance" SET NOT NULL,
ALTER COLUMN "storage_limit" SET NOT NULL;
```

## File: `prisma/migrations/20250424103453_stripe_customer_id/migration.sql`
```sql
/*
  Warnings:

  - You are about to drop the column `token_balance` on the `users` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "users" DROP COLUMN "token_balance",
ADD COLUMN     "ai_balance" INTEGER NOT NULL DEFAULT 0,
ADD COLUMN     "stripe_customer_id" TEXT;
```

## File: `prisma/migrations/20250505101845_add_business_details/migration.sql`
```sql
-- AlterTable
ALTER TABLE "users" ADD COLUMN     "business_address" TEXT,
ADD COLUMN     "business_bank_details" TEXT,
ADD COLUMN     "business_logo" TEXT,
ADD COLUMN     "business_name" TEXT;
```

## File: `prisma/migrations/20250507100532_add_app_data/migration.sql`
```sql
-- CreateTable
CREATE TABLE "app_data" (
    "id" UUID NOT NULL,
    "app" TEXT NOT NULL,
    "user_id" UUID NOT NULL,
    "data" JSONB NOT NULL,

    CONSTRAINT "app_data_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "app_data_user_id_app_key" ON "app_data"("user_id", "app");

-- AddForeignKey
ALTER TABLE "app_data" ADD CONSTRAINT "app_data_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

## File: `prisma/migrations/20250519130610_progress/migration.sql`
```sql
-- CreateTable
CREATE TABLE "progress" (
    "id" UUID NOT NULL,
    "user_id" UUID NOT NULL,
    "type" TEXT NOT NULL,
    "data" JSONB,
    "current" INTEGER NOT NULL DEFAULT 0,
    "total" INTEGER NOT NULL DEFAULT 0,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "progress_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE INDEX "progress_user_id_idx" ON "progress"("user_id");

-- AddForeignKey
ALTER TABLE "progress" ADD CONSTRAINT "progress_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "users"("id") ON DELETE CASCADE ON UPDATE CASCADE;
```

## File: `prisma/migrations/20250520185247_add_cached_parse_result/migration.sql`
```sql
-- AlterTable
ALTER TABLE "files" ADD COLUMN     "cached_parse_result" JSONB;
```

## File: `prisma/migrations/20250523104130_split_tx_items/migration.sql`
```sql
-- AlterTable
ALTER TABLE "files" ADD COLUMN     "is_splitted" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "transactions" ADD COLUMN     "items" JSONB NOT NULL DEFAULT '[]';
```

## File: `public/site.webmanifest`
```
{"name":"","short_name":"","icons":[{"src":"/android-chrome-192x192.png","sizes":"192x192","type":"image/png"},{"src":"/android-chrome-512x512.png","sizes":"512x512","type":"image/png"}],"theme_color":"#ffffff","background_color":"#ffffff","display":"standalone"}
```


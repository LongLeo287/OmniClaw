---
id: TaxHacker
type: knowledge
owner: OA_Triage
---
# TaxHacker
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
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

### File: README.md
```md
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

### File: components.json
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

### File: docker-entrypoint.sh
```sh
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

### File: instrumentation-client.ts
```ts
import * as Sentry from "@sentry/nextjs"

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
})

```

### File: instrumentation.ts
```ts
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

### File: middleware.ts
```ts
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

### File: next.config.ts
```ts
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

### File: sentry.edge.config.ts
```ts
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

### File: sentry.server.config.ts
```ts
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

### File: tailwind.config.ts
```ts
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

### File: tsconfig.json
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

### File: ai\analyze.ts
```ts
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

### File: ai\attachments.ts
```ts
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

### File: ai\prompt.ts
```ts
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

### File: ai\schema.ts
```ts
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

### File: app\globals.css
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

### File: docs\migrate_0.3_0.5.md
```md
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

### File: forms\settings.ts
```ts
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

### File: forms\transactions.ts
```ts
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

### File: forms\users.ts
```ts
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

### File: lib\actions.ts
```ts
export type ActionState<T> = {
  success: boolean
  error?: string | null
  data?: T | null
}

```

### File: lib\auth-client.ts
```ts
import { createAuthClient } from "better-auth/client"
import { emailOTPClient } from "better-auth/client/plugins"

export const authClient = createAuthClient({
  plugins: [emailOTPClient()],
})

```

### File: lib\auth.ts
```ts
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

### File: lib\cache.ts
```ts
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

### File: lib\config.ts
```ts
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

### File: lib\db.ts
```ts
import { PrismaClient } from "@/prisma/client"

const globalForPrisma = globalThis as unknown as {
  prisma: PrismaClient | undefined
}

export const prisma = globalForPrisma.prisma ?? new PrismaClient({ log: ["query", "info", "warn", "error"] })

if (process.env.NODE_ENV !== "production") globalForPrisma.prisma = prisma

```

### File: lib\email.ts
```ts
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

### File: lib\files.ts
```ts
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

### File: lib\llm-providers.ts
```ts
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

### File: lib\stats.ts
```ts
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

### File: lib\stripe.ts
```ts
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



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.

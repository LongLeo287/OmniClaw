---
id: vane-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:40.382300
---

# KNOWLEDGE EXTRACT: Vane
> **Extracted on:** 2026-03-30 22:09:36
> **Source:** Vane

---

## File: `.dockerignore`
```
**/node_modules
```

## File: `.eslintrc.json`
```json
{
  "extends": "next/core-web-vitals"
}
```

## File: `.gitignore`
```
# Node.js
node_modules/
npm-debug.log
yarn-error.log

# Build output
.next/
out/
dist/

# IDE/Editor specific
.vscode/
.idea/
*.iml

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# Config files
config.toml

# Log files
logs/
*.log

# Testing
/coverage/

# Miscellaneous
.DS_Store
Thumbs.db

# Db
db.sqlite
/searxng

certificates
```

## File: `.prettierignore`
```
# Ignore all files in the node_modules directory
node_modules

# Ignore all files in the .next directory (Next.js build output)
.next

# Ignore all files in the .out directory (TypeScript build output)
.out

# Ignore all files in the .cache directory (Prettier cache)
.cache

# Ignore all files in the .vscode directory (Visual Studio Code settings)
.vscode

# Ignore all files in the .idea directory (IntelliJ IDEA settings)
.idea

# Ignore all files in the dist directory (build output)
dist

# Ignore all files in the build directory (build output)
build

# Ignore all files in the coverage directory (test coverage reports)
coverage

# Ignore all files with the .log extension
*.log

# Ignore all files with the .tmp extension
*.tmp

# Ignore all files with the .swp extension
*.swp

# Ignore all files with the .DS_Store extension (macOS specific)
.DS_Store

# Ignore all files in uploads directory
uploads
```

## File: `.prettierrc.js`
```javascript
/** @type {import("prettier").Config} */

const config = {
  printWidth: 80,
  trailingComma: 'all',
  endOfLine: 'auto',
  singleQuote: true,
  tabWidth: 2,
};

module.exports = config;
```

## File: `CONTRIBUTING.md`
```markdown
# How to Contribute to Vane

Thanks for your interest in contributing to Vane! Your help makes this project better. This guide explains how to contribute effectively.

Vane is a modern AI chat application with advanced search capabilities.

## Project Structure

Vane's codebase is organized as follows:

- **UI Components and Pages**:
  - **Components (`src/components`)**: Reusable UI components.
  - **Pages and Routes (`src/app`)**: Next.js app directory structure with page components.
    - Main app routes include: home (`/`), chat (`/c`), discover (`/discover`), and library (`/library`).
  - **API Routes (`src/app/api`)**: Server endpoints implemented with Next.js route handlers.
- **Backend Logic (`src/lib`)**: Contains all the backend functionality including search, database, and API logic.
  - The search system lives in `src/lib/agents/search`.
  - The search pipeline is split into classification, research, widgets, and writing.
  - Database functionality is in `src/lib/db`.
  - Chat model and embedding model providers are in `src/lib/models/providers`, and models are loaded via `src/lib/models/registry.ts`.
  - Prompt templates are in `src/lib/prompts`.
  - SearXNG integration is in `src/lib/searxng.ts`.
  - Upload search lives in `src/lib/uploads`.

### Where to make changes

If you are not sure where to start, use this section as a map.

- **Search behavior and reasoning**

  - `src/lib/agents/search` contains the core chat and search pipeline.
  - `classifier.ts` decides whether research is needed and what should run.
  - `researcher/` gathers information in the background.

- **Add or change a search capability**

  - Research tools (web, academic, discussions, uploads, scraping) live in `src/lib/agents/search/researcher/actions`.
  - Tools are registered in `src/lib/agents/search/researcher/actions/index.ts`.

- **Add or change widgets**

  - Widgets live in `src/lib/agents/search/widgets`.
  - Widgets run in parallel with research and show structured results in the UI.

- **Model integrations**

  - Providers live in `src/lib/models/providers`.
  - Add new providers there and wire them into the model registry so they show up in the app.

- **Architecture docs**
  - High level overview: `docs/architecture/README.md`
  - High level flow: `docs/architecture/WORKING.md`

## API Documentation

Vane includes API documentation for programmatic access.

- **Search API**: For detailed documentation, see `docs/API/SEARCH.md`.

## Setting Up Your Environment

Before diving into coding, setting up your local environment is key. Here's what you need to do:

1. Run `npm install` to install all dependencies.
2. Use `npm run dev` to start the application in development mode.
3. Open http://localhost:3000 and complete the setup in the UI (API keys, models, search backend URL, etc.).

Database migrations are applied automatically on startup.

For full installation options (Docker and non Docker), see the installation guide in the repository README.

**Please note**: Docker configurations are present for setting up production environments, whereas `npm run dev` is used for development purposes.

## Coding and Contribution Practices

Before committing changes:

1. Ensure that your code functions correctly by thorough testing.
2. Always run `npm run format:write` to format your code according to the project's coding standards. This helps maintain consistency and code quality.
3. We currently do not have a code of conduct, but it is in the works. In the meantime, please be mindful of how you engage with the project and its community.

Following these steps will help maintain the integrity of Vane's codebase and facilitate a smoother integration of your valuable contributions. Thank you for your support and commitment to improving Vane.
```

## File: `docker-compose.yaml`
```yaml
services:
  vane:
    image: itzcrazykns1337/vane:latest
    build:
      context: .
    ports:
      - '3000:3000'
    volumes:
      - data:/home/vane/data
    restart: unless-stopped

volumes:
  data:
    name: 'vane-data'
```

## File: `Dockerfile`
```
FROM node:24.5.0-slim AS builder

RUN apt-get update && apt-get install -y python3 python3-pip sqlite3 && rm -rf /var/lib/apt/lists/*

WORKDIR /home/vane

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile --network-timeout 600000

COPY tsconfig.json next.config.mjs next-env.d.ts postcss.config.js drizzle.config.ts tailwind.config.ts ./
COPY src ./src
COPY public ./public
COPY drizzle ./drizzle

RUN mkdir -p /home/vane/data
RUN yarn build

FROM node:24.5.0-slim

RUN apt-get update && apt-get install -y \
    python3-dev python3-babel python3-venv python-is-python3 \
    uwsgi uwsgi-plugin-python3 \
    git build-essential libxslt-dev zlib1g-dev libffi-dev libssl-dev \
    curl sudo \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/vane

COPY --from=builder /home/vane/public ./public
COPY --from=builder /home/vane/.next/static ./public/_next/static
COPY --from=builder /home/vane/.next/standalone ./
COPY --from=builder /home/vane/data ./data
COPY drizzle ./drizzle

RUN mkdir /home/vane/uploads

RUN useradd --shell /bin/bash --system \
    --home-dir "/usr/local/searxng" \
    --comment 'Privacy-respecting metasearch engine' \
    searxng

RUN mkdir "/usr/local/searxng"
RUN mkdir -p /etc/searxng
RUN chown -R "searxng:searxng" "/usr/local/searxng"

COPY searxng/settings.yml /etc/searxng/settings.yml
COPY searxng/limiter.toml /etc/searxng/limiter.toml
COPY searxng/uwsgi.ini /etc/searxng/uwsgi.ini
RUN chown -R searxng:searxng /etc/searxng

USER searxng

RUN git clone "https://github.com/searxng/searxng" \
                   "/usr/local/searxng/searxng-src"

RUN python3 -m venv "/usr/local/searxng/searx-pyenv"
RUN "/usr/local/searxng/searx-pyenv/bin/pip" install --upgrade pip setuptools wheel pyyaml msgspec typing_extensions
RUN cd "/usr/local/searxng/searxng-src" && \
    "/usr/local/searxng/searx-pyenv/bin/pip" install --use-pep517 --no-build-isolation -e .

USER root

WORKDIR /home/vane
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh
RUN sed -i 's/\r$//' ./entrypoint.sh || true

RUN echo "searxng ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

EXPOSE 3000 8080

ENV SEARXNG_API_URL=http://localhost:8080

CMD ["/home/vane/entrypoint.sh"]
```

## File: `Dockerfile.slim`
```
FROM node:24.5.0-slim AS builder

RUN apt-get update && apt-get install -y python3 python3-pip sqlite3 && rm -rf /var/lib/apt/lists/*

WORKDIR /home/vane

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile --network-timeout 600000

COPY tsconfig.json next.config.mjs next-env.d.ts postcss.config.js drizzle.config.ts tailwind.config.ts ./
COPY src ./src
COPY public ./public
COPY drizzle ./drizzle

RUN mkdir -p /home/vane/data
RUN yarn build

FROM node:24.5.0-slim

RUN apt-get update && apt-get install -y python3 python3-pip sqlite3 && rm -rf /var/lib/apt/lists/*

WORKDIR /home/vane

COPY --from=builder /home/vane/public ./public
COPY --from=builder /home/vane/.next/static ./public/_next/static

COPY --from=builder /home/vane/.next/standalone ./
COPY --from=builder /home/vane/data ./data
COPY drizzle ./drizzle

RUN mkdir /home/vane/uploads

EXPOSE 3000

CMD ["node", "server.js"]
```

## File: `drizzle.config.ts`
```typescript
import { defineConfig } from 'drizzle-kit';
import path from 'path';

export default defineConfig({
  dialect: 'sqlite',
  schema: './src/lib/db/schema.ts',
  out: './drizzle',
  dbCredentials: {
    url: path.join(process.cwd(), 'data', 'db.sqlite'),
  },
});
```

## File: `entrypoint.sh`
```bash
#!/bin/sh
set -e

echo "Starting SearXNG..."

sudo -H -u searxng bash -c "cd /usr/local/searxng/searxng-src && export SEARXNG_SETTINGS_PATH='/etc/searxng/settings.yml' && export FLASK_APP=searx/webapp.py && /usr/local/searxng/searx-pyenv/bin/python -m flask run --host=0.0.0.0 --port=8080" &
SEARXNG_PID=$!

echo "Waiting for SearXNG to be ready..."
sleep 5

COUNTER=0
MAX_TRIES=30
until curl -s http://localhost:8080 > /dev/null 2>&1; do
  COUNTER=$((COUNTER+1))
  if [ $COUNTER -ge $MAX_TRIES ]; then
    echo "Warning: SearXNG health check timeout, but continuing..."
    break
  fi
  sleep 1
done

if curl -s http://localhost:8080 > /dev/null 2>&1; then
  echo "SearXNG started successfully (PID: $SEARXNG_PID)"
else
  echo "SearXNG may not be fully ready, but continuing (PID: $SEARXNG_PID)"
fi

cd /home/vane
echo "Starting Vane..."

exec node server.js
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 ItzCrazyKns

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

## File: `next-env.d.ts`
```typescript
/// <reference types="next" />
/// <reference types="next/image-types/global" />
import './.next/dev/types/routes.d.ts';

// NOTE: This file should not be edited
// see https://nextjs.org/docs/app/api-reference/config/typescript for more information.
```

## File: `next.config.mjs`
```
import pkg from './package.json' with { type: 'json' };

/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone',
  images: {
    remotePatterns: [
      {
        hostname: 's2.googleusercontent.com',
      },
    ],
  },
  serverExternalPackages: ['pdf-parse'],
  outputFileTracingIncludes: {
    '/api/**': [
      './node_modules/@napi-rs/canvas/**',
      './node_modules/@napi-rs/canvas-linux-x64-gnu/**',
      './node_modules/@napi-rs/canvas-linux-x64-musl/**',
    ],
  },
  env: {
    NEXT_PUBLIC_VERSION: pkg.version,
  },
};

export default nextConfig;
```

## File: `package.json`
```json
{
  "name": "vane",
  "version": "1.12.1",
  "license": "MIT",
  "author": "ItzCrazyKns",
  "scripts": {
    "dev": "next dev --webpack",
    "build": "next build --webpack",
    "start": "next start",
    "lint": "next lint",
    "format:write": "prettier . --write"
  },
  "dependencies": {
    "@google/genai": "^1.34.0",
    "@headlessui/react": "^2.2.0",
    "@headlessui/tailwindcss": "^0.2.2",
    "@huggingface/transformers": "^3.8.1",
    "@icons-pack/react-simple-icons": "^12.3.0",
    "@phosphor-icons/react": "^2.1.10",
    "@radix-ui/react-tooltip": "^1.2.8",
    "@tailwindcss/typography": "^0.5.12",
    "@toolsycc/json-repair": "^0.1.22",
    "axios": "^1.8.3",
    "better-sqlite3": "^11.9.1",
    "clsx": "^2.1.0",
    "drizzle-orm": "^0.40.1",
    "js-tiktoken": "^1.0.21",
    "jspdf": "^3.0.4",
    "lightweight-charts": "^5.0.9",
    "lucide-react": "^0.556.0",
    "mammoth": "^1.9.1",
    "markdown-to-jsx": "^7.7.2",
    "mathjs": "^15.1.0",
    "motion": "^12.23.26",
    "next": "^16.0.7",
    "next-themes": "^0.3.0",
    "officeparser": "^5.2.2",
    "ollama": "^0.6.3",
    "openai": "^6.9.0",
    "partial-json": "^0.1.7",
    "pdf-parse": "^2.4.5",
    "react": "^18",
    "react-dom": "^18",
    "react-syntax-highlighter": "^16.1.0",
    "react-text-to-speech": "^0.14.5",
    "react-textarea-autosize": "^8.5.3",
    "rfc6902": "^5.1.2",
    "sonner": "^1.4.41",
    "tailwind-merge": "^2.2.2",
    "turndown": "^7.2.2",
    "yahoo-finance2": "^3.10.2",
    "yet-another-react-lightbox": "^3.17.2",
    "zod": "^4.1.12"
  },
  "devDependencies": {
    "@types/better-sqlite3": "^7.6.12",
    "@types/jspdf": "^2.0.0",
    "@types/node": "^24.8.1",
    "@types/pdf-parse": "^1.1.4",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "@types/react-syntax-highlighter": "^15.5.13",
    "@types/turndown": "^5.0.6",
    "autoprefixer": "^10.0.1",
    "drizzle-kit": "^0.30.5",
    "eslint": "^8",
    "eslint-config-next": "14.1.4",
    "postcss": "^8",
    "prettier": "^3.2.5",
    "tailwindcss": "^3.3.0",
    "typescript": "^5.9.3"
  },
  "optionalDependencies": {
    "@napi-rs/canvas": "^0.1.87"
  }
}
```

## File: `postcss.config.js`
```javascript
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

## File: `README.md`
```markdown
# Vane 🔍

[![GitHub Repo stars](https://img.shields.io/github/stars/ItzCrazyKns/Vane?style=social)](https://github.com/ItzCrazyKns/Vane/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ItzCrazyKns/Vane?style=social)](https://github.com/ItzCrazyKns/Vane/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/ItzCrazyKns/Vane?style=social)](https://github.com/ItzCrazyKns/Vane/watchers)
[![Docker Pulls](https://img.shields.io/docker/pulls/itzcrazykns1337/vane?color=blue)](https://hub.docker.com/r/itzcrazykns1337/vane)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ItzCrazyKns/Vane/blob/master/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/ItzCrazyKns/Vane?color=green)](https://github.com/ItzCrazyKns/Vane/commits/master)
[![Discord](https://dcbadge.limes.pink/api/server/26aArMy8tT?style=flat)](https://discord.gg/26aArMy8tT)

Vane is a **privacy-focused AI answering engine** that runs entirely on your own hardware. It combines knowledge from the vast internet with support for **local LLMs** (Ollama) and cloud providers (OpenAI, Claude, Groq), delivering accurate answers with **cited sources** while keeping your searches completely private.

![preview](.assets/vane-screenshot.png)

Want to know more about its architecture and how it works? You can read it [here](https://github.com/ItzCrazyKns/Vane/tree/master/docs/architecture/README.md).

## ✨ Features

🤖 **Support for all major AI providers** - Use local LLMs through Ollama or connect to OpenAI, Anthropic Claude, Google Gemini, Groq, and more. Mix and match models based on your needs.

⚡ **Smart search modes** - Choose Speed Mode when you need quick answers, Balanced Mode for everyday searches, or Quality Mode for deep research.

🧭 **Pick your sources** - Search the web, discussions, or academic papers. More sources and integrations are in progress.

🧩 **Widgets** - Helpful UI cards that show up when relevant, like weather, calculations, stock prices, and other quick lookups.

🔍 **Web search powered by SearxNG** - Access multiple search engines while keeping your identity private. Support for Tavily and Exa coming soon for even better results.

📷 **Image and video search** - Find visual content alongside text results. Search isn't limited to just articles anymore.

📄 **File uploads** - Upload documents and ask questions about them. PDFs, text files, images - Vane understands them all.

🌐 **Search specific domains** - Limit your search to specific websites when you know where to look. Perfect for technical documentation or research papers.

💡 **Smart suggestions** - Get intelligent search suggestions as you type, helping you formulate better queries.

📚 **Discover** - Browse interesting articles and trending content throughout the day. Stay informed without even searching.

🕒 **Search history** - Every search is saved locally so you can revisit your discoveries anytime. Your research is never lost.

✨ **More coming soon** - We're actively developing new features based on community feedback. Join our Discord to help shape Vane's future!

## Sponsors

Vane's development is powered by the generous support of our sponsors. Their contributions help keep this project free, open-source, and accessible to everyone.

<div align="center">
  
  
<a href="https://www.warp.dev/perplexica">
  <img alt="Warp Terminal" src=".assets/sponsers/warp.png" width="100%">
</a>

### **✨ [Try Warp - The AI-Powered Terminal →](https://www.warp.dev/vane)**

Warp is revolutionizing development workflows with AI-powered features, modern UX, and blazing-fast performance. Used by developers at top companies worldwide.

</div>

---

We'd also like to thank the following partners for their generous support:

<table>
  <tr>
    <td width="100" align="center">
      <a href="https://dashboard.exa.ai" target="_blank">
        <img src=".assets/sponsers/exa.png" alt="Exa" width="80" height="80" style="border-radius: .75rem;" />
      </a>
    </td>
    <td>
      <a href="https://dashboard.exa.ai">Exa</a> • The Perfect Web Search API for LLMs - web search, crawling, deep research, and answer APIs
    </td>
  </tr>
</table>

## Installation

There are mainly 2 ways of installing Vane - With Docker, Without Docker. Using Docker is highly recommended.

### Getting Started with Docker (Recommended)

Vane can be easily run using Docker. Simply run the following command:

```bash
docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest
```

This will pull and start the Vane container with the bundled SearxNG search engine. Once running, open your browser and navigate to http://localhost:3000. You can then configure your settings (API keys, models, etc.) directly in the setup screen.

**Note**: The image includes both Vane and SearxNG, so no additional setup is required. The `-v` flags create persistent volumes for your data and uploaded files.

#### Using Vane with Your Own SearxNG Instance

If you already have SearxNG running, you can use the slim version of Vane:

```bash
docker run -d -p 3000:3000 -e SEARXNG_API_URL=http://your-searxng-url:8080 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:slim-latest
```

**Important**: Make sure your SearxNG instance has:

- JSON format enabled in the settings
- Wolfram Alpha search engine enabled

Replace `http://your-searxng-url:8080` with your actual SearxNG URL. Then configure your AI provider settings in the setup screen at http://localhost:3000.

#### Advanced Setup (Building from Source)

If you prefer to build from source or need more control:

1. Ensure Docker is installed and running on your system.
2. Clone the Vane repository:

   ```bash
   git clone https://github.com/ItzCrazyKns/Vane.git
   ```

3. After cloning, navigate to the directory containing the project files.

4. Build and run using Docker:

   ```bash
   docker build -t vane .
   docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane vane
   ```

5. Access Vane at http://localhost:3000 and configure your settings in the setup screen.

**Note**: After the containers are built, you can start Vane directly from Docker without having to open a terminal.

### Non-Docker Installation

1. Install SearXNG and allow `JSON` format in the SearXNG settings. Make sure Wolfram Alpha search engine is also enabled.
2. Clone the repository:

   ```bash
   git clone https://github.com/ItzCrazyKns/Vane.git
   cd Vane
   ```

3. Install dependencies:

   ```bash
   npm i
   ```

4. Build the application:

   ```bash
   npm run build
   ```

5. Start the application:

   ```bash
   npm run start
   ```

6. Open your browser and navigate to http://localhost:3000 to complete the setup and configure your settings (API keys, models, SearxNG URL, etc.) in the setup screen.

**Note**: Using Docker is recommended as it simplifies the setup process, especially for managing environment variables and dependencies.

See the [installation documentation](https://github.com/ItzCrazyKns/Vane/tree/master/docs/installation) for more information like updating, etc.

### Troubleshooting

#### Local OpenAI-API-Compliant Servers

If Vane tells you that you haven't configured any chat model providers, ensure that:

1. Your server is running on `0.0.0.0` (not `127.0.0.1`) and on the same port you put in the API URL.
2. You have specified the correct model name loaded by your local LLM server.
3. You have specified the correct API key, or if one is not defined, you have put _something_ in the API key field and not left it empty.

#### Ollama Connection Errors

If you're encountering an Ollama connection error, it is likely due to the backend being unable to connect to Ollama's API. To fix this issue you can:

1. **Check your Ollama API URL:** Ensure that the API URL is correctly set in the settings menu.
2. **Update API URL Based on OS:**

   - **Windows:** Use `http://host.docker.internal:11434`
   - **Mac:** Use `http://host.docker.internal:11434`
   - **Linux:** Use `http://<private_ip_of_host>:11434`

   Adjust the port number if you're using a different one.

3. **Linux Users - Expose Ollama to Network:**

   - Inside `/etc/systemd/system/ollama.service`, you need to add `Environment="OLLAMA_HOST=0.0.0.0:11434"`. (Change the port number if you are using a different one.) Then reload the systemd manager configuration with `systemctl daemon-reload`, and restart Ollama by `systemctl restart ollama`. For more information see [Ollama docs](https://github.com/ollama/ollama/blob/main/docs/faq.md#setting-environment-variables-on-linux)

   - Ensure that the port (default is 11434) is not blocked by your firewall.

#### Lemonade Connection Errors

If you're encountering a Lemonade connection error, it is likely due to the backend being unable to connect to Lemonade's API. To fix this issue you can:

1. **Check your Lemonade API URL:** Ensure that the API URL is correctly set in the settings menu.
2. **Update API URL Based on OS:**

   - **Windows:** Use `http://host.docker.internal:8000`
   - **Mac:** Use `http://host.docker.internal:8000`
   - **Linux:** Use `http://<private_ip_of_host>:8000`

   Adjust the port number if you're using a different one.

3. **Ensure Lemonade Server is Running:**

   - Make sure your Lemonade server is running and accessible on the configured port (default is 8000).
   - Verify that Lemonade is configured to accept connections from all interfaces (`0.0.0.0`), not just localhost (`127.0.0.1`).
   - Ensure that the port (default is 8000) is not blocked by your firewall.

## Using as a Search Engine

If you wish to use Vane as an alternative to traditional search engines like Google or Bing, or if you want to add a shortcut for quick access from your browser's search bar, follow these steps:

1. Open your browser's settings.
2. Navigate to the 'Search Engines' section.
3. Add a new site search with the following URL: `http://localhost:3000/?q=%s`. Replace `localhost` with your IP address or domain name, and `3000` with the port number if Vane is not hosted locally.
4. Click the add button. Now, you can use Vane directly from your browser's search bar.

## Using Vane's API

Vane also provides an API for developers looking to integrate its powerful search engine into their own applications. You can run searches, use multiple models and get answers to your queries.

For more details, check out the full documentation [here](https://github.com/ItzCrazyKns/Vane/tree/master/docs/API/SEARCH.md).

## Expose Vane to network

Vane runs on Next.js and handles all API requests. It works right away on the same network and stays accessible even with port forwarding.

## One-Click Deployment

[![Deploy to Sealos](https://raw.githubusercontent.com/labring-actions/templates/main/Deploy-on-Sealos.svg)](https://usw.sealos.io/?openapp=system-template%3FtemplateName%3Dperplexica)
[![Deploy to RepoCloud](https://d16t0pc4846x52.cloudfront.net/deploylobe.svg)](https://repocloud.io/details/?app_id=267)
[![Run on ClawCloud](https://raw.githubusercontent.com/ClawCloud/Run-Template/refs/heads/main/Run-on-ClawCloud.svg)](https://template.run.claw.cloud/?referralCode=U11MRQ8U9RM4&openapp=system-fastdeploy%3FtemplateName%3Dperplexica)
[![Deploy on Hostinger](https://assets.hostinger.com/vps/deploy.svg)](https://www.hostinger.com/vps/docker-hosting?compose_url=https://raw.githubusercontent.com/ItzCrazyKns/Vane/refs/heads/master/docker-compose.yaml)

## Upcoming Features

- [ ] Adding more widgets, integrations, search sources
- [ ] Adding ability to create custom agents (name T.B.D.)
- [ ] Adding authentication

## Support Us

If you find Vane useful, consider giving us a star on GitHub. This helps more people discover Vane and supports the development of new features. Your support is greatly appreciated.

### Donations

We also accept donations to help sustain our project. If you would like to contribute, you can use the following options to donate. Thank you for your support!

| Ethereum                                              |
| ----------------------------------------------------- |
| Address: `0xB025a84b2F269570Eb8D4b05DEdaA41D8525B6DD` |

## Contribution

Vane is built on the idea that AI and large language models should be easy for everyone to use. If you find bugs or have ideas, please share them in via GitHub Issues. For more information on contributing to Vane you can read the [CONTRIBUTING.md](CONTRIBUTING.md) file to learn more about Vane and how you can contribute to it.

## Help and Support

If you have any questions or feedback, please feel free to reach out to us. You can create an issue on GitHub or join our Discord server. There, you can connect with other users, share your experiences and reviews, and receive more personalized help. [Click here](https://discord.gg/EFwsmQDgAu) to join the Discord server. To discuss matters outside of regular support, feel free to contact me on Discord at `itzcrazykns`.

Thank you for exploring Vane, the AI-powered search engine designed to enhance your search experience. We are constantly working to improve Vane and expand its capabilities. We value your feedback and contributions which help us make Vane even better. Don't forget to check back for updates and new features!
```

## File: `tailwind.config.ts`
```typescript
import type { Config } from 'tailwindcss';
import type { DefaultColors } from 'tailwindcss/types/generated/colors';

const themeDark = (colors: DefaultColors) => ({
  50: '#0d1117',
  100: '#161b22',
  200: '#21262d',
  300: '#30363d',
});

const themeLight = (colors: DefaultColors) => ({
  50: '#ffffff',
  100: '#f6f8fa',
  200: '#e8edf1',
  300: '#d0d7de',
});

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      borderColor: ({ colors }) => {
        return {
          light: themeLight(colors),
          dark: themeDark(colors),
        };
      },
      colors: ({ colors }) => {
        const colorsDark = themeDark(colors);
        const colorsLight = themeLight(colors);

        return {
          dark: {
            primary: colorsDark[50],
            secondary: colorsDark[100],
            ...colorsDark,
          },
          light: {
            primary: colorsLight[50],
            secondary: colorsLight[100],
            ...colorsLight,
          },
        };
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@headlessui/tailwindcss')({ prefix: 'headless' }),
  ],
};
export default config;
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
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
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    },
    "target": "ES2017"
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts"
  ],
  "exclude": ["node_modules"]
}
```

## File: `data/.gitignore`
```
*
!.gitignore
```

## File: `docs/API/SEARCH.md`
```markdown
# Vane Search API Documentation

## Overview

Vane's Search API makes it easy to use our AI-powered search engine. You can run different types of searches, pick the models you want to use, and get the most recent info. Follow the following headings to learn more about Vane's search API.

## Endpoints

### Get Available Providers and Models

Before making search requests, you'll need to get the available providers and their models.

#### **GET** `/api/providers`

**Full URL**: `http://localhost:3000/api/providers`

Returns a list of all active providers with their available chat and embedding models.

**Response Example:**

```json
{
  "providers": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "OpenAI",
      "chatModels": [
        {
          "name": "GPT 4 Omni Mini",
          "key": "gpt-4o-mini"
        },
        {
          "name": "GPT 4 Omni",
          "key": "gpt-4o"
        }
      ],
      "embeddingModels": [
        {
          "name": "Text Embedding 3 Large",
          "key": "text-embedding-3-large"
        }
      ]
    }
  ]
}
```

Use the `id` field as the `providerId` and the `key` field from the models arrays when making search requests.

### Search Query

#### **POST** `/api/search`

**Full URL**: `http://localhost:3000/api/search`

**Note**: Replace `localhost:3000` with your Vane instance URL if running on a different host or port

### Request

The API accepts a JSON object in the request body, where you define the enabled search `sources`, chat models, embedding models, and your query.

#### Request Body Structure

```json
{
  "chatModel": {
    "providerId": "550e8400-e29b-41d4-a716-446655440000",
    "key": "gpt-4o-mini"
  },
  "embeddingModel": {
    "providerId": "550e8400-e29b-41d4-a716-446655440000",
    "key": "text-embedding-3-large"
  },
  "optimizationMode": "speed",
  "sources": ["web"],
  "query": "What is Vane",
  "history": [
    ["human", "Hi, how are you?"],
    ["assistant", "I am doing well, how can I help you today?"]
  ],
  "systemInstructions": "Focus on providing technical details about Vane's architecture.",
  "stream": false
}
```

**Note**: The `providerId` must be a valid UUID obtained from the `/api/providers` endpoint. The example above uses a sample UUID for demonstration.

### Request Parameters

- **`chatModel`** (object, required): Defines the chat model to be used for the query. To get available providers and models, send a GET request to `http://localhost:3000/api/providers`.

  - `providerId` (string): The UUID of the provider. You can get this from the `/api/providers` endpoint response.
  - `key` (string): The model key/identifier (e.g., `gpt-4o-mini`, `llama3.1:latest`). Use the `key` value from the provider's `chatModels` array, not the display name.

- **`embeddingModel`** (object, required): Defines the embedding model for similarity-based searching. To get available providers and models, send a GET request to `http://localhost:3000/api/providers`.

  - `providerId` (string): The UUID of the embedding provider. You can get this from the `/api/providers` endpoint response.
  - `key` (string): The embedding model key (e.g., `text-embedding-3-large`, `nomic-embed-text`). Use the `key` value from the provider's `embeddingModels` array, not the display name.

- **`sources`** (array, required): Which search sources to enable. Available values:

  - `web`, `academic`, `discussions`.

- **`optimizationMode`** (string, optional): Specifies the optimization mode to control the balance between performance and quality. Available modes:

  - `speed`: Prioritize speed and return the fastest answer.
  - `balanced`: Provide a balanced answer with good speed and reasonable quality.
  - `quality`: Prioritize answer quality (may be slower).

- **`query`** (string, required): The search query or question.

- **`systemInstructions`** (string, optional): Custom instructions provided by the user to guide the AI's response. These instructions are treated as user preferences and have lower priority than the system's core instructions. For example, you can specify a particular writing style, format, or focus area.

- **`history`** (array, optional): An array of message pairs representing the conversation history. Each pair consists of a role (either 'human' or 'assistant') and the message content. This allows the system to use the context of the conversation to refine results. Example:

  ```json
  [
    ["human", "What is Vane?"],
    ["assistant", "Vane is an AI-powered search engine..."]
  ]
  ```

- **`stream`** (boolean, optional): When set to `true`, enables streaming responses. Default is `false`.

### Response

The response from the API includes both the final message and the sources used to generate that message.

#### Standard Response (stream: false)

```json
{
  "message": "Vane is an innovative, open-source AI-powered search engine designed to enhance the way users search for information online. Here are some key features and characteristics of Vane:\n\n- **AI-Powered Technology**: It utilizes advanced machine learning algorithms to not only retrieve information but also to understand the context and intent behind user queries, providing more relevant results [1][5].\n\n- **Open-Source**: Being open-source, Vane offers flexibility and transparency, allowing users to explore its functionalities without the constraints of proprietary software [3][10].",
  "sources": [
    {
      "content": "Vane is an innovative, open-source AI-powered search engine designed to enhance the way users search for information online.",
      "metadata": {
        "title": "What is Vane, and how does it function as an AI-powered search ...",
        "url": "https://askai.glarity.app/search/What-is-Vane--and-how-does-it-function-as-an-AI-powered-search-engine"
      }
    },
    {
      "content": "Vane is an open-source AI-powered search tool that dives deep into the internet to find precise answers.",
      "metadata": {
        "title": "Sahar Mor's Post",
        "url": "https://www.linkedin.com/posts/sahar-mor_a-new-open-source-project-called-vane-activity-7204489745668694016-ncja"
      }
    }
        ....
  ]
}
```

#### Streaming Response (stream: true)

When streaming is enabled, the API returns a stream of newline-delimited JSON objects using Server-Sent Events (SSE). Each line contains a complete, valid JSON object. The response has `Content-Type: text/event-stream`.

Example of streamed response objects:

```
{"type":"init","data":"Stream connected"}
{"type":"sources","data":[{"content":"...","metadata":{"title":"...","url":"..."}},...]}
{"type":"response","data":"Vane is an "}
{"type":"response","data":"innovative, open-source "}
{"type":"response","data":"AI-powered search engine..."}
{"type":"done"}
```

Clients should process each line as a separate JSON object. The different message types include:

- **`init`**: Initial connection message
- **`sources`**: All sources used for the response
- **`response`**: Chunks of the generated answer text
- **`done`**: Indicates the stream is complete

### Fields in the Response

- **`message`** (string): The search result, generated based on the query and enabled `sources`.
- **`sources`** (array): A list of sources that were used to generate the search result. Each source includes:
  - `content`: A snippet of the relevant content from the source.
  - `metadata`: Metadata about the source, including:
    - `title`: The title of the webpage.
    - `url`: The URL of the webpage.

### Error Handling

If an error occurs during the search process, the API will return an appropriate error message with an HTTP status code.

- **400**: If the request is malformed or missing required fields (e.g., no `sources` or `query`).
- **500**: If an internal server error occurs during the search.
```

## File: `docs/architecture/README.md`
```markdown
# Vane Architecture

Vane is a Next.js application that combines an AI chat experience with search.

For a high level flow, see [WORKING.md](WORKING.md). For deeper implementation details, see [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Key components

1. **User Interface**

   - A web based UI that lets users chat, search, and view citations.

2. **API Routes**

   - `POST /api/chat` powers the chat UI.
   - `POST /api/search` provides a programmatic search endpoint.
   - `GET /api/providers` lists available providers and model keys.

3. **Agents and Orchestration**

   - The system classifies the question first.
   - It can run research and widgets in parallel.
   - It generates the final answer and includes citations.

4. **Search Backend**

   - A meta search backend is used to fetch relevant web results when research is enabled.

5. **LLMs (Large Language Models)**

   - Used for classification, writing answers, and producing citations.

6. **Embedding Models**

   - Used for semantic search over user uploaded files.

7. **Storage**
   - Chats and messages are stored so conversations can be reloaded.
```

## File: `docs/architecture/WORKING.md`
```markdown
# How Vane Works

This is a high level overview of how Vane answers a question.

If you want a component level overview, see [README.md](README.md).

If you want implementation details, see [CONTRIBUTING.md](../../CONTRIBUTING.md).

## What happens when you ask a question

When you send a message in the UI, the app calls `POST /api/chat`.

At a high level, we do three things:

1. Classify the question and decide what to do next.
2. Run research and widgets in parallel.
3. Write the final answer and include citations.

## Classification

Before searching or answering, we run a classification step.

This step decides things like:

- Whether we should do research for this question
- Whether we should show any widgets
- How to rewrite the question into a clearer standalone form

## Widgets

Widgets are small, structured helpers that can run alongside research.

Examples include weather, stocks, and simple calculations.

If a widget is relevant, we show it in the UI while the answer is still being generated.

Widgets are helpful context for the answer, but they are not part of what the model should cite.

## Research

If research is needed, we gather information in the background while widgets can run.

Depending on configuration, research may include web lookup and searching user uploaded files.

## Answer generation

Once we have enough context, the chat model generates the final response.

You can control the tradeoff between speed and quality using `optimizationMode`:

- `speed`
- `balanced`
- `quality`

## How citations work

We prompt the model to cite the references it used. The UI then renders those citations alongside the supporting links.

## Search API

If you are integrating Vane into another product, you can call `POST /api/search`.

It returns:

- `message`: the generated answer
- `sources`: supporting references used for the answer

You can also enable streaming by setting `stream: true`.

## Image and video search

Image and video search use separate endpoints (`POST /api/images` and `POST /api/videos`). We generate a focused query using the chat model, then fetch matching results from a search backend.
```

## File: `docs/installation/UPDATING.md`
```markdown
# Update Vane to the latest version

To update Vane to the latest version, follow these steps:

## For Docker users (Using pre-built images)

Simply pull the latest image and restart your container:

```bash
docker pull itzcrazykns1337/vane:latest
docker stop vane
docker rm vane
docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest
```

For slim version:

```bash
docker pull itzcrazykns1337/vane:slim-latest
docker stop vane
docker rm vane
docker run -d -p 3000:3000 -e SEARXNG_API_URL=http://your-searxng-url:8080 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:slim-latest
```

Once updated, go to http://localhost:3000 and verify the latest changes. Your settings are preserved automatically.

## For Docker users (Building from source)

1. Navigate to your Vane directory and pull the latest changes:

   ```bash
   cd Vane
   git pull origin master
   ```

2. Rebuild the Docker image:

   ```bash
   docker build -t vane .
   ```

3. Stop and remove the old container, then start the new one:

   ```bash
   docker stop vane
   docker rm vane
   docker run -p 3000:3000 -p 8080:8080 --name vane vane
   ```

4. Once the command completes, go to http://localhost:3000 and verify the latest changes.

## For non-Docker users

1. Navigate to your Vane directory and pull the latest changes:

   ```bash
   cd Vane
   git pull origin master
   ```

2. Install any new dependencies:

   ```bash
   npm i
   ```

3. Rebuild the application:

   ```bash
   npm run build
   ```

4. Restart the application:

   ```bash
   npm run start
   ```

5. Go to http://localhost:3000 and verify the latest changes. Your settings are preserved automatically.

---
```

## File: `drizzle/0000_fuzzy_randall.sql`
```sql
CREATE TABLE IF NOT EXISTS `chats` (
	`id` text PRIMARY KEY NOT NULL,
	`title` text NOT NULL,
	`createdAt` text NOT NULL,
	`focusMode` text NOT NULL,
	`files` text DEFAULT '[]'
);
--> statement-breakpoint
CREATE TABLE IF NOT EXISTS `messages` (
	`id` integer PRIMARY KEY NOT NULL,
	`content` text NOT NULL,
	`chatId` text NOT NULL,
	`messageId` text NOT NULL,
	`type` text,
	`metadata` text
);
```

## File: `drizzle/0001_wise_rockslide.sql`
```sql
/* Do nothing */
```

## File: `drizzle/0002_daffy_wrecker.sql`
```sql
/* do nothing */
```

## File: `drizzle/meta/0000_snapshot.json`
```json
{
  "version": "6",
  "dialect": "sqlite",
  "id": "ef3a044b-0f34-40b5-babb-2bb3a909ba27",
  "prevId": "00000000-0000-0000-0000-000000000000",
  "tables": {
    "chats": {
      "name": "chats",
      "columns": {
        "id": {
          "name": "id",
          "type": "text",
          "primaryKey": true,
          "notNull": true,
          "autoincrement": false
        },
        "title": {
          "name": "title",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "createdAt": {
          "name": "createdAt",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "focusMode": {
          "name": "focusMode",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "files": {
          "name": "files",
          "type": "text",
          "primaryKey": false,
          "notNull": false,
          "autoincrement": false,
          "default": "'[]'"
        }
      },
      "indexes": {},
      "foreignKeys": {},
      "compositePrimaryKeys": {},
      "uniqueConstraints": {},
      "checkConstraints": {}
    },
    "messages": {
      "name": "messages",
      "columns": {
        "id": {
          "name": "id",
          "type": "integer",
          "primaryKey": true,
          "notNull": true,
          "autoincrement": false
        },
        "content": {
          "name": "content",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "chatId": {
          "name": "chatId",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "messageId": {
          "name": "messageId",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "type": {
          "name": "type",
          "type": "text",
          "primaryKey": false,
          "notNull": false,
          "autoincrement": false
        },
        "metadata": {
          "name": "metadata",
          "type": "text",
          "primaryKey": false,
          "notNull": false,
          "autoincrement": false
        }
      },
      "indexes": {},
      "foreignKeys": {},
      "compositePrimaryKeys": {},
      "uniqueConstraints": {},
      "checkConstraints": {}
    }
  },
  "views": {},
  "enums": {},
  "_meta": {
    "schemas": {},
    "tables": {},
    "columns": {}
  },
  "internal": {
    "indexes": {}
  }
}
```

## File: `drizzle/meta/0001_snapshot.json`
```json
{
  "version": "6",
  "dialect": "sqlite",
  "id": "6dedf55f-0e44-478f-82cf-14a21ac686f8",
  "prevId": "ef3a044b-0f34-40b5-babb-2bb3a909ba27",
  "tables": {
    "chats": {
      "name": "chats",
      "columns": {
        "id": {
          "name": "id",
          "type": "text",
          "primaryKey": true,
          "notNull": true,
          "autoincrement": false
        },
        "title": {
          "name": "title",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "createdAt": {
          "name": "createdAt",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "focusMode": {
          "name": "focusMode",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "files": {
          "name": "files",
          "type": "text",
          "primaryKey": false,
          "notNull": false,
          "autoincrement": false,
          "default": "'[]'"
        }
      },
      "indexes": {},
      "foreignKeys": {},
      "compositePrimaryKeys": {},
      "uniqueConstraints": {},
      "checkConstraints": {}
    },
    "messages": {
      "name": "messages",
      "columns": {
        "id": {
          "name": "id",
          "type": "integer",
          "primaryKey": true,
          "notNull": true,
          "autoincrement": false
        },
        "type": {
          "name": "type",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "chatId": {
          "name": "chatId",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "createdAt": {
          "name": "createdAt",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false,
          "default": "CURRENT_TIMESTAMP"
        },
        "messageId": {
          "name": "messageId",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "content": {
          "name": "content",
          "type": "text",
          "primaryKey": false,
          "notNull": false,
          "autoincrement": false
        },
        "sources": {
          "name": "sources",
          "type": "text",
          "primaryKey": false,
          "notNull": false,
          "autoincrement": false,
          "default": "'[]'"
        }
      },
      "indexes": {},
      "foreignKeys": {},
      "compositePrimaryKeys": {},
      "uniqueConstraints": {},
      "checkConstraints": {}
    }
  },
  "views": {},
  "enums": {},
  "_meta": {
    "schemas": {},
    "tables": {},
    "columns": {}
  },
  "internal": {
    "indexes": {}
  }
}
```

## File: `drizzle/meta/0002_snapshot.json`
```json
{
  "version": "6",
  "dialect": "sqlite",
  "id": "1c5eb804-d6b4-48ec-9a8f-75fb729c8e52",
  "prevId": "6dedf55f-0e44-478f-82cf-14a21ac686f8",
  "tables": {
    "chats": {
      "name": "chats",
      "columns": {
        "id": {
          "name": "id",
          "type": "text",
          "primaryKey": true,
          "notNull": true,
          "autoincrement": false
        },
        "title": {
          "name": "title",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "createdAt": {
          "name": "createdAt",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "sources": {
          "name": "sources",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "files": {
          "name": "files",
          "type": "text",
          "primaryKey": false,
          "notNull": false,
          "autoincrement": false,
          "default": "'[]'"
        }
      },
      "indexes": {},
      "foreignKeys": {},
      "compositePrimaryKeys": {},
      "uniqueConstraints": {},
      "checkConstraints": {}
    },
    "messages": {
      "name": "messages",
      "columns": {
        "id": {
          "name": "id",
          "type": "integer",
          "primaryKey": true,
          "notNull": true,
          "autoincrement": false
        },
        "messageId": {
          "name": "messageId",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "chatId": {
          "name": "chatId",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "backendId": {
          "name": "backendId",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "query": {
          "name": "query",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "createdAt": {
          "name": "createdAt",
          "type": "text",
          "primaryKey": false,
          "notNull": true,
          "autoincrement": false
        },
        "responseBlocks": {
          "name": "responseBlocks",
          "type": "text",
          "primaryKey": false,
          "notNull": false,
          "autoincrement": false,
          "default": "'[]'"
        },
        "status": {
          "name": "status",
          "type": "text",
          "primaryKey": false,
          "notNull": false,
          "autoincrement": false,
          "default": "'answering'"
        }
      },
      "indexes": {},
      "foreignKeys": {},
      "compositePrimaryKeys": {},
      "uniqueConstraints": {},
      "checkConstraints": {}
    }
  },
  "views": {},
  "enums": {},
  "_meta": {
    "schemas": {},
    "tables": {},
    "columns": {}
  },
  "internal": {
    "indexes": {}
  }
}
```

## File: `drizzle/meta/_journal.json`
```json
{
  "version": "7",
  "dialect": "sqlite",
  "entries": [
    {
      "idx": 0,
      "version": "6",
      "when": 1748405503809,
      "tag": "0000_fuzzy_randall",
      "breakpoints": true
    },
    {
      "idx": 1,
      "version": "6",
      "when": 1758863991284,
      "tag": "0001_wise_rockslide",
      "breakpoints": true
    },
    {
      "idx": 2,
      "version": "6",
      "when": 1763732708332,
      "tag": "0002_daffy_wrecker",
      "breakpoints": true
    }
  ]
}
```

## File: `searxng/limiter.toml`
```
[botdetection.ip_limit]
# activate link_token method in the ip_limit method
link_token = true
```

## File: `searxng/settings.yml`
```yaml
use_default_settings: true

general:
  instance_name: 'searxng'

search:
  autocomplete: 'google'
  formats:
    - html
    - json

server:
  secret_key: 'a2fb23f1b02e6ee83875b09826990de0f6bd908b6638e8c10277d415f6ab852b' # Is overwritten by ${SEARXNG_SECRET}

engines:
  - name: wolframalpha
    disabled: false
```

## File: `searxng/uwsgi.ini`
```
[uwsgi]
# Who will run the code
uid = searxng
gid = searxng

# Number of workers (usually CPU count)
# default value: %k (= number of CPU core, see Dockerfile)
workers = %k

# Number of threads per worker
# default value: 4 (see Dockerfile)
threads = 4

# The right granted on the created socket
chmod-socket = 666

# Plugin to use and interpreter config
single-interpreter = true
master = true
plugin = python3
lazy-apps = true
enable-threads = 4

# Module to import
module = searx.webapp

# Virtualenv and python path
pythonpath = /usr/local/searxng/
chdir = /usr/local/searxng/searx/

# automatically set processes name to something meaningful
auto-procname = true

# Disable request logging for privacy
disable-logging = true
log-5xx = true

# Set the max size of a request (request-body excluded)
buffer-size = 8192

# No keep alive
# See https://github.com/searx/searx-docker/issues/24
add-header = Connection: close

# uwsgi serves the static files
static-map = /static=/usr/local/searxng/searx/static
# expires set to one day
static-expires = /* 86400
static-gzip-all = True
offload-threads = 4
```

## File: `src/instrumentation.ts`
```typescript
export const register = async () => {
  if (process.env.NEXT_RUNTIME === 'nodejs') {
    try {
      console.log('Running database migrations...');
      await import('./lib/db/migrate');
      console.log('Database migrations completed successfully');
    } catch (error) {
      console.error('Failed to run database migrations:', error);
    }

    await import('./lib/config/index');
  }
};
```

## File: `src/app/globals.css`
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@font-face {
  font-family: 'PP Editorial';
  src: url('/fonts/pp-ed-ul.otf') format('opentype');
  font-weight: 300;
  font-style: normal;
  font-display: swap;
}

@layer base {
  .overflow-hidden-scrollable {
    -ms-overflow-style: none;
  }

  .overflow-hidden-scrollable::-webkit-scrollbar {
    display: none;
  }

  * {
    scrollbar-width: thin;
    scrollbar-color: #e8edf1 transparent; /* light-200 */
  }

  *::-webkit-scrollbar {
    width: 6px;
    height: 6px;
  }

  *::-webkit-scrollbar-track {
    background: transparent;
  }

  *::-webkit-scrollbar-thumb {
    background: #e8edf1; /* light-200 */
    border-radius: 3px;
    transition: background 0.2s ease;
  }

  *::-webkit-scrollbar-thumb:hover {
    background: #d0d7de; /* light-300 */
  }

  @media (prefers-color-scheme: dark) {
    * {
      scrollbar-color: #21262d transparent; /* dark-200 */
    }

    *::-webkit-scrollbar-thumb {
      background: #21262d; /* dark-200 */
    }

    *::-webkit-scrollbar-thumb:hover {
      background: #30363d; /* dark-300 */
    }
  }

  :root.dark *,
  html.dark *,
  body.dark * {
    scrollbar-color: #21262d transparent; /* dark-200 */
  }

  :root.dark *::-webkit-scrollbar-thumb,
  html.dark *::-webkit-scrollbar-thumb,
  body.dark *::-webkit-scrollbar-thumb {
    background: #21262d; /* dark-200 */
  }

  :root.dark *::-webkit-scrollbar-thumb:hover,
  html.dark *::-webkit-scrollbar-thumb:hover,
  body.dark *::-webkit-scrollbar-thumb:hover {
    background: #30363d; /* dark-300 */
  }

  html {
    scroll-behavior: smooth;
  }
}

@layer utilities {
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    overflow: hidden;
  }
}

@media screen and (-webkit-min-device-pixel-ratio: 0) {
  select,
  textarea,
  input {
    font-size: 16px !important;
  }
}
```

## File: `src/app/layout.tsx`
```tsx
export const dynamic = 'force-dynamic';

import type { Metadata } from 'next';
import { Montserrat } from 'next/font/google';
import './globals.css';
import { cn } from '@/lib/utils';
import Sidebar from '@/components/Sidebar';
import { Toaster } from 'sonner';
import ThemeProvider from '@/components/theme/Provider';
import configManager from '@/lib/config';
import SetupWizard from '@/components/Setup/SetupWizard';
import { ChatProvider } from '@/lib/hooks/useChat';

const montserrat = Montserrat({
  weight: ['300', '400', '500', '700'],
  subsets: ['latin'],
  display: 'swap',
  fallback: ['Arial', 'sans-serif'],
});

export const metadata: Metadata = {
  title: 'Vane - Direct your curiosity',
  description: 'Vane is an AI powered answering engine.',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const setupComplete = configManager.isSetupComplete();
  const configSections = configManager.getUIConfigSections();

  return (
    <html className="h-full" lang="en" suppressHydrationWarning>
      <body className={cn('h-full antialiased', montserrat.className)}>
        <ThemeProvider>
          {setupComplete ? (
            <ChatProvider>
              <Sidebar>{children}</Sidebar>
              <Toaster
                toastOptions={{
                  unstyled: true,
                  classNames: {
                    toast:
                      'bg-light-secondary dark:bg-dark-secondary dark:text-white/70 text-black-70 rounded-lg p-4 flex flex-row items-center space-x-2',
                  },
                }}
              />
            </ChatProvider>
          ) : (
            <SetupWizard configSections={configSections} />
          )}
        </ThemeProvider>
      </body>
    </html>
  );
}
```

## File: `src/app/manifest.ts`
```typescript
import type { MetadataRoute } from 'next';

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: 'Vane - Direct Your Curiosity',
    short_name: 'Vane',
    description: 'Vane is an AI powered answering engine.',
    start_url: '/',
    display: 'standalone',
    background_color: '#0a0a0a',
    theme_color: '#0a0a0a',
    screenshots: [
      {
        src: '/screenshots/p1.png',
        form_factor: 'wide',
        sizes: '2560x1600',
      },
      {
        src: '/screenshots/p2.png',
        form_factor: 'wide',
        sizes: '2560x1600',
      },
      {
        src: '/screenshots/p1_small.png',
        form_factor: 'narrow',
        sizes: '828x1792',
      },
      {
        src: '/screenshots/p2_small.png',
        form_factor: 'narrow',
        sizes: '828x1792',
      },
    ],
    icons: [
      {
        src: '/icon-50.png',
        sizes: '50x50',
        type: 'image/png' as const,
      },
      {
        src: '/icon-100.png',
        sizes: '100x100',
        type: 'image/png',
      },
      {
        src: '/icon.png',
        sizes: '440x440',
        type: 'image/png',
        purpose: 'any',
      },
    ],
  };
}
```

## File: `src/app/page.tsx`
```tsx
import ChatWindow from '@/components/ChatWindow';
import { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Chat - Vane',
  description: 'Chat with the internet, chat with Vane.',
};

const Home = () => {
  return <ChatWindow />;
};

export default Home;
```

## File: `src/app/api/chat/route.ts`
```typescript
import { z } from 'zod';
import ModelRegistry from '@/lib/models/registry';
import { ModelWithProvider } from '@/lib/models/types';
import SearchAgent from '@/lib/agents/search';
import SessionManager from '@/lib/session';
import { ChatTurnMessage } from '@/lib/types';
import { SearchSources } from '@/lib/agents/search/types';
import db from '@/lib/db';
import { eq } from 'drizzle-orm';
import { chats } from '@/lib/db/schema';
import UploadManager from '@/lib/uploads/manager';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';

const messageSchema = z.object({
  messageId: z.string().min(1, 'Message ID is required'),
  chatId: z.string().min(1, 'Chat ID is required'),
  content: z.string().min(1, 'Message content is required'),
});

const chatModelSchema: z.ZodType<ModelWithProvider> = z.object({
  providerId: z.string({ message: 'Chat model provider id must be provided' }),
  key: z.string({ message: 'Chat model key must be provided' }),
});

const embeddingModelSchema: z.ZodType<ModelWithProvider> = z.object({
  providerId: z.string({
    message: 'Embedding model provider id must be provided',
  }),
  key: z.string({ message: 'Embedding model key must be provided' }),
});

const bodySchema = z.object({
  message: messageSchema,
  optimizationMode: z.enum(['speed', 'balanced', 'quality'], {
    message: 'Optimization mode must be one of: speed, balanced, quality',
  }),
  sources: z.array(z.string()).optional().default([]),
  history: z
    .array(z.tuple([z.string(), z.string()]))
    .optional()
    .default([]),
  files: z.array(z.string()).optional().default([]),
  chatModel: chatModelSchema,
  embeddingModel: embeddingModelSchema,
  systemInstructions: z.string().nullable().optional().default(''),
});

type Body = z.infer<typeof bodySchema>;

const safeValidateBody = (data: unknown) => {
  const result = bodySchema.safeParse(data);

  if (!result.success) {
    return {
      success: false,
      error: result.error.issues.map((e: any) => ({
        path: e.path.join('.'),
        message: e.message,
      })),
    };
  }

  return {
    success: true,
    data: result.data,
  };
};

const ensureChatExists = async (input: {
  id: string;
  sources: SearchSources[];
  query: string;
  fileIds: string[];
}) => {
  try {
    const exists = await db.query.chats
      .findFirst({
        where: eq(chats.id, input.id),
      })
      .execute();

    if (!exists) {
      await db.insert(chats).values({
        id: input.id,
        createdAt: new Date().toISOString(),
        sources: input.sources,
        title: input.query,
        files: input.fileIds.map((id) => {
          return {
            fileId: id,
            name: UploadManager.getFile(id)?.name || 'Uploaded File',
          };
        }),
      });
    }
  } catch (err) {
    console.error('Failed to check/save chat:', err);
  }
};

export const POST = async (req: Request) => {
  try {
    const reqBody = (await req.json()) as Body;

    const parseBody = safeValidateBody(reqBody);

    if (!parseBody.success) {
      return Response.json(
        { message: 'Invalid request body', error: parseBody.error },
        { status: 400 },
      );
    }

    const body = parseBody.data as Body;
    const { message } = body;

    if (message.content === '') {
      return Response.json(
        {
          message: 'Please provide a message to process',
        },
        { status: 400 },
      );
    }

    const registry = new ModelRegistry();

    const [llm, embedding] = await Promise.all([
      registry.loadChatModel(body.chatModel.providerId, body.chatModel.key),
      registry.loadEmbeddingModel(
        body.embeddingModel.providerId,
        body.embeddingModel.key,
      ),
    ]);

    const history: ChatTurnMessage[] = body.history.map((msg) => {
      if (msg[0] === 'human') {
        return {
          role: 'user',
          content: msg[1],
        };
      } else {
        return {
          role: 'assistant',
          content: msg[1],
        };
      }
    });

    const agent = new SearchAgent();
    const session = SessionManager.createSession();

    const responseStream = new TransformStream();
    const writer = responseStream.writable.getWriter();
    const encoder = new TextEncoder();

    const disconnect = session.subscribe((event: string, data: any) => {
      if (event === 'data') {
        if (data.type === 'block') {
          writer.write(
            encoder.encode(
              JSON.stringify({
                type: 'block',
                block: data.block,
              }) + '\n',
            ),
          );
        } else if (data.type === 'updateBlock') {
          writer.write(
            encoder.encode(
              JSON.stringify({
                type: 'updateBlock',
                blockId: data.blockId,
                patch: data.patch,
              }) + '\n',
            ),
          );
        } else if (data.type === 'researchComplete') {
          writer.write(
            encoder.encode(
              JSON.stringify({
                type: 'researchComplete',
              }) + '\n',
            ),
          );
        }
      } else if (event === 'end') {
        writer.write(
          encoder.encode(
            JSON.stringify({
              type: 'messageEnd',
            }) + '\n',
          ),
        );
        writer.close();
        session.removeAllListeners();
      } else if (event === 'error') {
        writer.write(
          encoder.encode(
            JSON.stringify({
              type: 'error',
              data: data.data,
            }) + '\n',
          ),
        );
        writer.close();
        session.removeAllListeners();
      }
    });

    agent.searchAsync(session, {
      chatHistory: history,
      followUp: message.content,
      chatId: body.message.chatId,
      messageId: body.message.messageId,
      config: {
        llm,
        embedding: embedding,
        sources: body.sources as SearchSources[],
        mode: body.optimizationMode,
        fileIds: body.files,
        systemInstructions: body.systemInstructions || 'None',
      },
    });

    ensureChatExists({
      id: body.message.chatId,
      sources: body.sources as SearchSources[],
      fileIds: body.files,
      query: body.message.content,
    });

    req.signal.addEventListener('abort', () => {
      disconnect();
      writer.close();
    });

    return new Response(responseStream.readable, {
      headers: {
        'Content-Type': 'text/event-stream',
        Connection: 'keep-alive',
        'Cache-Control': 'no-cache, no-transform',
      },
    });
  } catch (err) {
    console.error('An error occurred while processing chat request:', err);
    return Response.json(
      { message: 'An error occurred while processing chat request' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/chats/route.ts`
```typescript
import db from '@/lib/db';

export const GET = async (req: Request) => {
  try {
    let chats = await db.query.chats.findMany();
    chats = chats.reverse();
    return Response.json({ chats: chats }, { status: 200 });
  } catch (err) {
    console.error('Error in getting chats: ', err);
    return Response.json(
      { message: 'An error has occurred.' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/chats/[id]/route.ts`
```typescript
import db from '@/lib/db';
import { chats, messages } from '@/lib/db/schema';
import { eq } from 'drizzle-orm';

export const GET = async (
  req: Request,
  { params }: { params: Promise<{ id: string }> },
) => {
  try {
    const { id } = await params;

    const chatExists = await db.query.chats.findFirst({
      where: eq(chats.id, id),
    });

    if (!chatExists) {
      return Response.json({ message: 'Chat not found' }, { status: 404 });
    }

    const chatMessages = await db.query.messages.findMany({
      where: eq(messages.chatId, id),
    });

    return Response.json(
      {
        chat: chatExists,
        messages: chatMessages,
      },
      { status: 200 },
    );
  } catch (err) {
    console.error('Error in getting chat by id: ', err);
    return Response.json(
      { message: 'An error has occurred.' },
      { status: 500 },
    );
  }
};

export const DELETE = async (
  req: Request,
  { params }: { params: Promise<{ id: string }> },
) => {
  try {
    const { id } = await params;

    const chatExists = await db.query.chats.findFirst({
      where: eq(chats.id, id),
    });

    if (!chatExists) {
      return Response.json({ message: 'Chat not found' }, { status: 404 });
    }

    await db.delete(chats).where(eq(chats.id, id)).execute();
    await db.delete(messages).where(eq(messages.chatId, id)).execute();

    return Response.json(
      { message: 'Chat deleted successfully' },
      { status: 200 },
    );
  } catch (err) {
    console.error('Error in deleting chat by id: ', err);
    return Response.json(
      { message: 'An error has occurred.' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/config/route.ts`
```typescript
import configManager from '@/lib/config';
import ModelRegistry from '@/lib/models/registry';
import { NextRequest, NextResponse } from 'next/server';
import { ConfigModelProvider } from '@/lib/config/types';

type SaveConfigBody = {
  key: string;
  value: string;
};

export const GET = async (req: NextRequest) => {
  try {
    const values = configManager.getCurrentConfig();
    const fields = configManager.getUIConfigSections();

    const modelRegistry = new ModelRegistry();
    const modelProviders = await modelRegistry.getActiveProviders();

    values.modelProviders = values.modelProviders.map(
      (mp: ConfigModelProvider) => {
        const activeProvider = modelProviders.find((p) => p.id === mp.id);

        return {
          ...mp,
          chatModels: activeProvider?.chatModels ?? mp.chatModels,
          embeddingModels:
            activeProvider?.embeddingModels ?? mp.embeddingModels,
        };
      },
    );

    return NextResponse.json({
      values,
      fields,
    });
  } catch (err) {
    console.error('Error in getting config: ', err);
    return Response.json(
      { message: 'An error has occurred.' },
      { status: 500 },
    );
  }
};

export const POST = async (req: NextRequest) => {
  try {
    const body: SaveConfigBody = await req.json();

    if (!body.key || !body.value) {
      return Response.json(
        {
          message: 'Key and value are required.',
        },
        {
          status: 400,
        },
      );
    }

    configManager.updateConfig(body.key, body.value);

    return Response.json(
      {
        message: 'Config updated successfully.',
      },
      {
        status: 200,
      },
    );
  } catch (err) {
    console.error('Error in getting config: ', err);
    return Response.json(
      { message: 'An error has occurred.' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/config/setup-complete/route.ts`
```typescript
import configManager from '@/lib/config';
import { NextRequest } from 'next/server';

export const POST = async (req: NextRequest) => {
  try {
    configManager.markSetupComplete();

    return Response.json(
      {
        message: 'Setup marked as complete.',
      },
      {
        status: 200,
      },
    );
  } catch (err) {
    console.error('Error marking setup as complete: ', err);
    return Response.json(
      { message: 'An error has occurred.' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/discover/route.ts`
```typescript
import { searchSearxng } from '@/lib/searxng';

const websitesForTopic = {
  tech: {
    query: ['technology news', 'latest tech', 'AI', 'science and innovation'],
    links: ['techcrunch.com', 'wired.com', 'theverge.com'],
  },
  finance: {
    query: ['finance news', 'economy', 'stock market', 'investing'],
    links: ['bloomberg.com', 'cnbc.com', 'marketwatch.com'],
  },
  art: {
    query: ['art news', 'culture', 'modern art', 'cultural events'],
    links: ['artnews.com', 'hyperallergic.com', 'theartnewspaper.com'],
  },
  sports: {
    query: ['sports news', 'latest sports', 'cricket football tennis'],
    links: ['espn.com', 'bbc.com/sport', 'skysports.com'],
  },
  entertainment: {
    query: ['entertainment news', 'movies', 'TV shows', 'celebrities'],
    links: ['hollywoodreporter.com', 'variety.com', 'deadline.com'],
  },
};

type Topic = keyof typeof websitesForTopic;

export const GET = async (req: Request) => {
  try {
    const params = new URL(req.url).searchParams;

    const mode: 'normal' | 'preview' =
      (params.get('mode') as 'normal' | 'preview') || 'normal';
    const topic: Topic = (params.get('topic') as Topic) || 'tech';

    const selectedTopic = websitesForTopic[topic];

    let data = [];

    if (mode === 'normal') {
      const seenUrls = new Set();

      data = (
        await Promise.all(
          selectedTopic.links.flatMap((link) =>
            selectedTopic.query.map(async (query) => {
              return (
                await searchSearxng(`site:${link} ${query}`, {
                  engines: ['bing news'],
                  pageno: 1,
                  language: 'en',
                })
              ).results;
            }),
          ),
        )
      )
        .flat()
        .filter((item) => {
          const url = item.url?.toLowerCase().trim();
          if (seenUrls.has(url)) return false;
          seenUrls.add(url);
          return true;
        })
        .sort(() => Math.random() - 0.5);
    } else {
      data = (
        await searchSearxng(
          `site:${selectedTopic.links[Math.floor(Math.random() * selectedTopic.links.length)]} ${selectedTopic.query[Math.floor(Math.random() * selectedTopic.query.length)]}`,
          {
            engines: ['bing news'],
            pageno: 1,
            language: 'en',
          },
        )
      ).results;
    }

    return Response.json(
      {
        blogs: data,
      },
      {
        status: 200,
      },
    );
  } catch (err) {
    console.error(`An error occurred in discover route: ${err}`);
    return Response.json(
      {
        message: 'An error has occurred',
      },
      {
        status: 500,
      },
    );
  }
};
```

## File: `src/app/api/images/route.ts`
```typescript
import searchImages from '@/lib/agents/media/image';
import ModelRegistry from '@/lib/models/registry';
import { ModelWithProvider } from '@/lib/models/types';

interface ImageSearchBody {
  query: string;
  chatHistory: any[];
  chatModel: ModelWithProvider;
}

export const POST = async (req: Request) => {
  try {
    const body: ImageSearchBody = await req.json();

    const registry = new ModelRegistry();

    const llm = await registry.loadChatModel(
      body.chatModel.providerId,
      body.chatModel.key,
    );

    const images = await searchImages(
      {
        chatHistory: body.chatHistory.map(([role, content]) => ({
          role: role === 'human' ? 'user' : 'assistant',
          content,
        })),
        query: body.query,
      },
      llm,
    );

    return Response.json({ images }, { status: 200 });
  } catch (err) {
    console.error(`An error occurred while searching images: ${err}`);
    return Response.json(
      { message: 'An error occurred while searching images' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/providers/route.ts`
```typescript
import ModelRegistry from '@/lib/models/registry';
import { NextRequest } from 'next/server';

export const GET = async (req: Request) => {
  try {
    const registry = new ModelRegistry();

    const activeProviders = await registry.getActiveProviders();

    const filteredProviders = activeProviders.filter((p) => {
      return !p.chatModels.some((m) => m.key === 'error');
    });

    return Response.json(
      {
        providers: filteredProviders,
      },
      {
        status: 200,
      },
    );
  } catch (err) {
    console.error('An error occurred while fetching providers', err);
    return Response.json(
      {
        message: 'An error has occurred.',
      },
      {
        status: 500,
      },
    );
  }
};

export const POST = async (req: NextRequest) => {
  try {
    const body = await req.json();
    const { type, name, config } = body;

    if (!type || !name || !config) {
      return Response.json(
        {
          message: 'Missing required fields.',
        },
        {
          status: 400,
        },
      );
    }

    const registry = new ModelRegistry();

    const newProvider = await registry.addProvider(type, name, config);

    return Response.json(
      {
        provider: newProvider,
      },
      {
        status: 200,
      },
    );
  } catch (err) {
    console.error('An error occurred while creating provider', err);
    return Response.json(
      {
        message: 'An error has occurred.',
      },
      {
        status: 500,
      },
    );
  }
};
```

## File: `src/app/api/providers/[id]/route.ts`
```typescript
import ModelRegistry from '@/lib/models/registry';
import { NextRequest } from 'next/server';

export const DELETE = async (
  req: NextRequest,
  { params }: { params: Promise<{ id: string }> },
) => {
  try {
    const { id } = await params;

    if (!id) {
      return Response.json(
        {
          message: 'Provider ID is required.',
        },
        {
          status: 400,
        },
      );
    }

    const registry = new ModelRegistry();
    await registry.removeProvider(id);

    return Response.json(
      {
        message: 'Provider deleted successfully.',
      },
      {
        status: 200,
      },
    );
  } catch (err: any) {
    console.error('An error occurred while deleting provider', err.message);
    return Response.json(
      {
        message: 'An error has occurred.',
      },
      {
        status: 500,
      },
    );
  }
};

export const PATCH = async (
  req: NextRequest,
  { params }: { params: Promise<{ id: string }> },
) => {
  try {
    const body = await req.json();
    const { name, config } = body;
    const { id } = await params;

    if (!id || !name || !config) {
      return Response.json(
        {
          message: 'Missing required fields.',
        },
        {
          status: 400,
        },
      );
    }

    const registry = new ModelRegistry();

    const updatedProvider = await registry.updateProvider(id, name, config);

    return Response.json(
      {
        provider: updatedProvider,
      },
      {
        status: 200,
      },
    );
  } catch (err: any) {
    console.error('An error occurred while updating provider', err.message);
    return Response.json(
      {
        message: 'An error has occurred.',
      },
      {
        status: 500,
      },
    );
  }
};
```

## File: `src/app/api/providers/[id]/models/route.ts`
```typescript
import ModelRegistry from '@/lib/models/registry';
import { Model } from '@/lib/models/types';
import { NextRequest } from 'next/server';

export const POST = async (
  req: NextRequest,
  { params }: { params: Promise<{ id: string }> },
) => {
  try {
    const { id } = await params;

    const body: Partial<Model> & { type: 'embedding' | 'chat' } =
      await req.json();

    if (!body.key || !body.name) {
      return Response.json(
        {
          message: 'Key and name must be provided',
        },
        {
          status: 400,
        },
      );
    }

    const registry = new ModelRegistry();

    await registry.addProviderModel(id, body.type, body);

    return Response.json(
      {
        message: 'Model added successfully',
      },
      {
        status: 200,
      },
    );
  } catch (err) {
    console.error('An error occurred while adding provider model', err);
    return Response.json(
      {
        message: 'An error has occurred.',
      },
      {
        status: 500,
      },
    );
  }
};

export const DELETE = async (
  req: NextRequest,
  { params }: { params: Promise<{ id: string }> },
) => {
  try {
    const { id } = await params;

    const body: { key: string; type: 'embedding' | 'chat' } = await req.json();

    if (!body.key) {
      return Response.json(
        {
          message: 'Key and name must be provided',
        },
        {
          status: 400,
        },
      );
    }

    const registry = new ModelRegistry();

    await registry.removeProviderModel(id, body.type, body.key);

    return Response.json(
      {
        message: 'Model added successfully',
      },
      {
        status: 200,
      },
    );
  } catch (err) {
    console.error('An error occurred while deleting provider model', err);
    return Response.json(
      {
        message: 'An error has occurred.',
      },
      {
        status: 500,
      },
    );
  }
};
```

## File: `src/app/api/reconnect/[id]/route.ts`
```typescript
import SessionManager from '@/lib/session';

export const POST = async (
  req: Request,
  { params }: { params: Promise<{ id: string }> },
) => {
  try {
    const { id } = await params;

    const session = SessionManager.getSession(id);

    if (!session) {
      return Response.json({ message: 'Session not found' }, { status: 404 });
    }

    const responseStream = new TransformStream();
    const writer = responseStream.writable.getWriter();
    const encoder = new TextEncoder();

    const disconnect = session.subscribe((event, data) => {
      if (event === 'data') {
        if (data.type === 'block') {
          writer.write(
            encoder.encode(
              JSON.stringify({
                type: 'block',
                block: data.block,
              }) + '\n',
            ),
          );
        } else if (data.type === 'updateBlock') {
          writer.write(
            encoder.encode(
              JSON.stringify({
                type: 'updateBlock',
                blockId: data.blockId,
                patch: data.patch,
              }) + '\n',
            ),
          );
        } else if (data.type === 'researchComplete') {
          writer.write(
            encoder.encode(
              JSON.stringify({
                type: 'researchComplete',
              }) + '\n',
            ),
          );
        }
      } else if (event === 'end') {
        writer.write(
          encoder.encode(
            JSON.stringify({
              type: 'messageEnd',
            }) + '\n',
          ),
        );
        writer.close();
        disconnect();
      } else if (event === 'error') {
        writer.write(
          encoder.encode(
            JSON.stringify({
              type: 'error',
              data: data.data,
            }) + '\n',
          ),
        );
        writer.close();
        disconnect();
      }
    });

    req.signal.addEventListener('abort', () => {
      disconnect();
      writer.close();
    });

    return new Response(responseStream.readable, {
      headers: {
        'Content-Type': 'text/event-stream',
        Connection: 'keep-alive',
        'Cache-Control': 'no-cache, no-transform',
      },
    });
  } catch (err) {
    console.error('Error in reconnecting to session stream: ', err);
    return Response.json(
      { message: 'An error has occurred.' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/search/route.ts`
```typescript
import ModelRegistry from '@/lib/models/registry';
import { ModelWithProvider } from '@/lib/models/types';
import SessionManager from '@/lib/session';
import { ChatTurnMessage } from '@/lib/types';
import { SearchSources } from '@/lib/agents/search/types';
import APISearchAgent from '@/lib/agents/search/api';

interface ChatRequestBody {
  optimizationMode: 'speed' | 'balanced' | 'quality';
  sources: SearchSources[];
  chatModel: ModelWithProvider;
  embeddingModel: ModelWithProvider;
  query: string;
  history: Array<[string, string]>;
  stream?: boolean;
  systemInstructions?: string;
}

export const POST = async (req: Request) => {
  try {
    const body: ChatRequestBody = await req.json();

    if (!body.sources || !body.query) {
      return Response.json(
        { message: 'Missing sources or query' },
        { status: 400 },
      );
    }

    body.history = body.history || [];
    body.optimizationMode = body.optimizationMode || 'speed';
    body.stream = body.stream || false;

    const registry = new ModelRegistry();

    const [llm, embeddings] = await Promise.all([
      registry.loadChatModel(body.chatModel.providerId, body.chatModel.key),
      registry.loadEmbeddingModel(
        body.embeddingModel.providerId,
        body.embeddingModel.key,
      ),
    ]);

    const history: ChatTurnMessage[] = body.history.map((msg) => {
      return msg[0] === 'human'
        ? { role: 'user', content: msg[1] }
        : { role: 'assistant', content: msg[1] };
    });

    const session = SessionManager.createSession();

    const agent = new APISearchAgent();

    agent.searchAsync(session, {
      chatHistory: history,
      config: {
        embedding: embeddings,
        llm: llm,
        sources: body.sources,
        mode: body.optimizationMode,
        fileIds: [],
        systemInstructions: body.systemInstructions || '',
      },
      followUp: body.query,
      chatId: crypto.randomUUID(),
      messageId: crypto.randomUUID(),
    });

    if (!body.stream) {
      return new Promise(
        (
          resolve: (value: Response) => void,
          reject: (value: Response) => void,
        ) => {
          let message = '';
          let sources: any[] = [];

          session.subscribe((event: string, data: Record<string, any>) => {
            if (event === 'data') {
              try {
                if (data.type === 'response') {
                  message += data.data;
                } else if (data.type === 'searchResults') {
                  sources = data.data;
                }
              } catch (error) {
                reject(
                  Response.json(
                    { message: 'Error parsing data' },
                    { status: 500 },
                  ),
                );
              }
            }

            if (event === 'end') {
              resolve(Response.json({ message, sources }, { status: 200 }));
            }

            if (event === 'error') {
              reject(
                Response.json(
                  { message: 'Search error', error: data },
                  { status: 500 },
                ),
              );
            }
          });
        },
      );
    }

    const encoder = new TextEncoder();

    const abortController = new AbortController();
    const { signal } = abortController;

    const stream = new ReadableStream({
      start(controller) {
        let sources: any[] = [];

        controller.enqueue(
          encoder.encode(
            JSON.stringify({
              type: 'init',
              data: 'Stream connected',
            }) + '\n',
          ),
        );

        signal.addEventListener('abort', () => {
          session.removeAllListeners();

          try {
            controller.close();
          } catch (error) {}
        });

        session.subscribe((event: string, data: Record<string, any>) => {
          if (event === 'data') {
            if (signal.aborted) return;

            try {
              if (data.type === 'response') {
                controller.enqueue(
                  encoder.encode(
                    JSON.stringify({
                      type: 'response',
                      data: data.data,
                    }) + '\n',
                  ),
                );
              } else if (data.type === 'searchResults') {
                sources = data.data;
                controller.enqueue(
                  encoder.encode(
                    JSON.stringify({
                      type: 'sources',
                      data: sources,
                    }) + '\n',
                  ),
                );
              }
            } catch (error) {
              controller.error(error);
            }
          }

          if (event === 'end') {
            if (signal.aborted) return;

            controller.enqueue(
              encoder.encode(
                JSON.stringify({
                  type: 'done',
                }) + '\n',
              ),
            );
            controller.close();
          }

          if (event === 'error') {
            if (signal.aborted) return;

            controller.error(data);
          }
        });
      },
      cancel() {
        abortController.abort();
      },
    });

    return new Response(stream, {
      headers: {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache, no-transform',
        Connection: 'keep-alive',
      },
    });
  } catch (err: any) {
    console.error(`Error in getting search results: ${err.message}`);
    return Response.json(
      { message: 'An error has occurred.' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/suggestions/route.ts`
```typescript
import generateSuggestions from '@/lib/agents/suggestions';
import ModelRegistry from '@/lib/models/registry';
import { ModelWithProvider } from '@/lib/models/types';

interface SuggestionsGenerationBody {
  chatHistory: any[];
  chatModel: ModelWithProvider;
}

export const POST = async (req: Request) => {
  try {
    const body: SuggestionsGenerationBody = await req.json();

    const registry = new ModelRegistry();

    const llm = await registry.loadChatModel(
      body.chatModel.providerId,
      body.chatModel.key,
    );

    const suggestions = await generateSuggestions(
      {
        chatHistory: body.chatHistory.map(([role, content]) => ({
          role: role === 'human' ? 'user' : 'assistant',
          content,
        })),
      },
      llm,
    );

    return Response.json({ suggestions }, { status: 200 });
  } catch (err) {
    console.error(`An error occurred while generating suggestions: ${err}`);
    return Response.json(
      { message: 'An error occurred while generating suggestions' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/uploads/route.ts`
```typescript
import { NextResponse } from 'next/server';
import ModelRegistry from '@/lib/models/registry';
import UploadManager from '@/lib/uploads/manager';

export async function POST(req: Request) {
  try {
    const formData = await req.formData();

    const files = formData.getAll('files') as File[];
    const embeddingModel = formData.get('embedding_model_key') as string;
    const embeddingModelProvider = formData.get('embedding_model_provider_id') as string;

    if (!embeddingModel || !embeddingModelProvider) {
      return NextResponse.json(
        { message: 'Missing embedding model or provider' },
        { status: 400 },
      );
    }

    const registry = new ModelRegistry();

    const model = await registry.loadEmbeddingModel(embeddingModelProvider, embeddingModel);
    
    const uploadManager = new UploadManager({
      embeddingModel: model,
    })

    const processedFiles = await uploadManager.processFiles(files);

    return NextResponse.json({
      files: processedFiles,
    });
  } catch (error) {
    console.error('Error uploading file:', error);
    return NextResponse.json(
      { message: 'An error has occurred.' },
      { status: 500 },
    );
  }
}
```

## File: `src/app/api/videos/route.ts`
```typescript
import handleVideoSearch from '@/lib/agents/media/video';
import ModelRegistry from '@/lib/models/registry';
import { ModelWithProvider } from '@/lib/models/types';

interface VideoSearchBody {
  query: string;
  chatHistory: any[];
  chatModel: ModelWithProvider;
}

export const POST = async (req: Request) => {
  try {
    const body: VideoSearchBody = await req.json();

    const registry = new ModelRegistry();

    const llm = await registry.loadChatModel(
      body.chatModel.providerId,
      body.chatModel.key,
    );

    const videos = await handleVideoSearch(
      {
        chatHistory: body.chatHistory.map(([role, content]) => ({
          role: role === 'human' ? 'user' : 'assistant',
          content,
        })),
        query: body.query,
      },
      llm,
    );

    return Response.json({ videos }, { status: 200 });
  } catch (err) {
    console.error(`An error occurred while searching videos: ${err}`);
    return Response.json(
      { message: 'An error occurred while searching videos' },
      { status: 500 },
    );
  }
};
```

## File: `src/app/api/weather/route.ts`
```typescript
export const POST = async (req: Request) => {
  try {
    const body: {
      lat: number;
      lng: number;
      measureUnit: 'Imperial' | 'Metric';
    } = await req.json();

    if (!body.lat || !body.lng) {
      return Response.json(
        {
          message: 'Invalid request.',
        },
        { status: 400 },
      );
    }

    const res = await fetch(
      `https://api.open-meteo.com/v1/forecast?latitude=${body.lat}&longitude=${body.lng}&current=weather_code,temperature_2m,is_day,relative_humidity_2m,wind_speed_10m&timezone=auto${
        body.measureUnit === 'Metric' ? '' : '&temperature_unit=fahrenheit'
      }${body.measureUnit === 'Metric' ? '' : '&wind_speed_unit=mph'}`,
    );

    const data = await res.json();

    if (data.error) {
      console.error(`Error fetching weather data: ${data.reason}`);
      return Response.json(
        {
          message: 'An error has occurred.',
        },
        { status: 500 },
      );
    }

    const weather: {
      temperature: number;
      condition: string;
      humidity: number;
      windSpeed: number;
      icon: string;
      temperatureUnit: 'C' | 'F';
      windSpeedUnit: 'm/s' | 'mph';
    } = {
      temperature: data.current.temperature_2m,
      condition: '',
      humidity: data.current.relative_humidity_2m,
      windSpeed: data.current.wind_speed_10m,
      icon: '',
      temperatureUnit: body.measureUnit === 'Metric' ? 'C' : 'F',
      windSpeedUnit: body.measureUnit === 'Metric' ? 'm/s' : 'mph',
    };

    const code = data.current.weather_code;
    const isDay = data.current.is_day === 1;
    const dayOrNight = isDay ? 'day' : 'night';

    switch (code) {
      case 0:
        weather.icon = `clear-${dayOrNight}`;
        weather.condition = 'Clear';
        break;

      case 1:
        weather.condition = 'Mainly Clear';
      case 2:
        weather.condition = 'Partly Cloudy';
      case 3:
        weather.icon = `cloudy-1-${dayOrNight}`;
        weather.condition = 'Cloudy';
        break;

      case 45:
        weather.condition = 'Fog';
      case 48:
        weather.icon = `fog-${dayOrNight}`;
        weather.condition = 'Fog';
        break;

      case 51:
        weather.condition = 'Light Drizzle';
      case 53:
        weather.condition = 'Moderate Drizzle';
      case 55:
        weather.icon = `rainy-1-${dayOrNight}`;
        weather.condition = 'Dense Drizzle';
        break;

      case 56:
        weather.condition = 'Light Freezing Drizzle';
      case 57:
        weather.icon = `frost-${dayOrNight}`;
        weather.condition = 'Dense Freezing Drizzle';
        break;

      case 61:
        weather.condition = 'Slight Rain';
      case 63:
        weather.condition = 'Moderate Rain';
      case 65:
        weather.condition = 'Heavy Rain';
        weather.icon = `rainy-2-${dayOrNight}`;
        break;

      case 66:
        weather.condition = 'Light Freezing Rain';
      case 67:
        weather.condition = 'Heavy Freezing Rain';
        weather.icon = 'rain-and-sleet-mix';
        break;

      case 71:
        weather.condition = 'Slight Snow Fall';
      case 73:
        weather.condition = 'Moderate Snow Fall';
      case 75:
        weather.condition = 'Heavy Snow Fall';
        weather.icon = `snowy-2-${dayOrNight}`;
        break;

      case 77:
        weather.condition = 'Snow';
        weather.icon = `snowy-1-${dayOrNight}`;
        break;

      case 80:
        weather.condition = 'Slight Rain Showers';
      case 81:
        weather.condition = 'Moderate Rain Showers';
      case 82:
        weather.condition = 'Heavy Rain Showers';
        weather.icon = `rainy-3-${dayOrNight}`;
        break;

      case 85:
        weather.condition = 'Slight Snow Showers';
      case 86:
        weather.condition = 'Moderate Snow Showers';
      case 87:
        weather.condition = 'Heavy Snow Showers';
        weather.icon = `snowy-3-${dayOrNight}`;
        break;

      case 95:
        weather.condition = 'Thunderstorm';
        weather.icon = `scattered-thunderstorms-${dayOrNight}`;
        break;

      case 96:
        weather.condition = 'Thunderstorm with Slight Hail';
      case 99:
        weather.condition = 'Thunderstorm with Heavy Hail';
        weather.icon = 'severe-thunderstorm';
        break;

      default:
        weather.icon = `clear-${dayOrNight}`;
        weather.condition = 'Clear';
        break;
    }

    return Response.json(weather);
  } catch (err) {
    console.error('An error occurred while getting home widgets', err);
    return Response.json(
      {
        message: 'An error has occurred.',
      },
      {
        status: 500,
      },
    );
  }
};
```

## File: `src/app/c/[chatId]/page.tsx`
```tsx
'use client';

import ChatWindow from '@/components/ChatWindow';

export default ChatWindow;
```

## File: `src/app/discover/page.tsx`
```tsx
'use client';

import { Globe2Icon } from 'lucide-react';
import { useEffect, useState } from 'react';
import { toast } from 'sonner';
import { cn } from '@/lib/utils';
import SmallNewsCard from '@/components/Discover/SmallNewsCard';
import MajorNewsCard from '@/components/Discover/MajorNewsCard';

export interface Discover {
  title: string;
  content: string;
  url: string;
  thumbnail: string;
}

const topics: { key: string; display: string }[] = [
  {
    display: 'Tech & Science',
    key: 'tech',
  },
  {
    display: 'Finance',
    key: 'finance',
  },
  {
    display: 'Art & Culture',
    key: 'art',
  },
  {
    display: 'Sports',
    key: 'sports',
  },
  {
    display: 'Entertainment',
    key: 'entertainment',
  },
];

const Page = () => {
  const [discover, setDiscover] = useState<Discover[] | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTopic, setActiveTopic] = useState<string>(topics[0].key);

  const fetchArticles = async (topic: string) => {
    setLoading(true);
    try {
      const res = await fetch(`/api/discover?topic=${topic}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      const data = await res.json();

      if (!res.ok) {
        throw new Error(data.message);
      }

      data.blogs = data.blogs.filter((blog: Discover) => blog.thumbnail);

      setDiscover(data.blogs);
    } catch (err: any) {
      console.error('Error fetching data:', err.message);
      toast.error('Error fetching data');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchArticles(activeTopic);
  }, [activeTopic]);

  return (
    <>
      <div>
        <div className="flex flex-col pt-10 border-b border-light-200/20 dark:border-dark-200/20 pb-6 px-2">
          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
            <div className="flex items-center justify-center">
              <Globe2Icon size={45} className="mb-2.5" />
              <h1
                className="text-5xl font-normal p-2"
                style={{ fontFamily: 'PP Editorial, serif' }}
              >
                Discover
              </h1>
            </div>
            <div className="flex flex-row items-center space-x-2 overflow-x-auto">
              {topics.map((t, i) => (
                <div
                  key={i}
                  className={cn(
                    'border-[0.1px] rounded-full text-sm px-3 py-1 text-nowrap transition duration-200 cursor-pointer',
                    activeTopic === t.key
                      ? 'text-cyan-700 dark:text-cyan-300 bg-cyan-300/20 border-cyan-700/60 dar:bg-cyan-300/30 dark:border-cyan-300/40'
                      : 'border-black/30 dark:border-white/30 text-black/70 dark:text-white/70 hover:text-black dark:hover:text-white hover:border-black/40 dark:hover:border-white/40 hover:bg-black/5 dark:hover:bg-white/5',
                  )}
                  onClick={() => setActiveTopic(t.key)}
                >
                  <span>{t.display}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {loading ? (
          <div className="flex flex-row items-center justify-center min-h-screen">
            <svg
              aria-hidden="true"
              className="w-8 h-8 text-light-200 fill-light-secondary dark:text-[#202020] animate-spin dark:fill-[#ffffff3b]"
              viewBox="0 0 100 101"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M100 50.5908C100.003 78.2051 78.1951 100.003 50.5908 100C22.9765 99.9972 0.997224 78.018 1 50.4037C1.00281 22.7993 22.8108 0.997224 50.4251 1C78.0395 1.00281 100.018 22.8108 100 50.4251ZM9.08164 50.594C9.06312 73.3997 27.7909 92.1272 50.5966 92.1457C73.4023 92.1642 92.1298 73.4365 92.1483 50.6308C92.1669 27.8251 73.4392 9.0973 50.6335 9.07878C27.8278 9.06026 9.10003 27.787 9.08164 50.594Z"
                fill="currentColor"
              />
              <path
                d="M93.9676 39.0409C96.393 38.4037 97.8624 35.9116 96.9801 33.5533C95.1945 28.8227 92.871 24.3692 90.0681 20.348C85.6237 14.1775 79.4473 9.36872 72.0454 6.45794C64.6435 3.54717 56.3134 2.65431 48.3133 3.89319C45.869 4.27179 44.3768 6.77534 45.014 9.20079C45.6512 11.6262 48.1343 13.0956 50.5786 12.717C56.5073 11.8281 62.5542 12.5399 68.0406 14.7911C73.527 17.0422 78.2187 20.7487 81.5841 25.4923C83.7976 28.5886 85.4467 32.059 86.4416 35.7474C87.1273 38.1189 89.5423 39.6781 91.9676 39.0409Z"
                fill="currentFill"
              />
            </svg>
          </div>
        ) : (
          <div className="flex flex-col gap-4 pb-28 pt-5 lg:pb-8 w-full">
            <div className="block lg:hidden">
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {discover?.map((item, i) => (
                  <SmallNewsCard key={`mobile-${i}`} item={item} />
                ))}
              </div>
            </div>

            <div className="hidden lg:block">
              {discover &&
                discover.length > 0 &&
                (() => {
                  const sections = [];
                  let index = 0;

                  while (index < discover.length) {
                    if (sections.length > 0) {
                      sections.push(
                        <hr
                          key={`sep-${index}`}
                          className="border-t border-light-200/20 dark:border-dark-200/20 my-3 w-full"
                        />,
                      );
                    }

                    if (index < discover.length) {
                      sections.push(
                        <MajorNewsCard
                          key={`major-${index}`}
                          item={discover[index]}
                          isLeft={false}
                        />,
                      );
                      index++;
                    }

                    if (index < discover.length) {
                      sections.push(
                        <hr
                          key={`sep-${index}-after`}
                          className="border-t border-light-200/20 dark:border-dark-200/20 my-3 w-full"
                        />,
                      );
                    }

                    if (index < discover.length) {
                      const smallCards = discover.slice(index, index + 3);
                      sections.push(
                        <div
                          key={`small-group-${index}`}
                          className="grid lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-4"
                        >
                          {smallCards.map((item, i) => (
                            <SmallNewsCard
                              key={`small-${index + i}`}
                              item={item}
                            />
                          ))}
                        </div>,
                      );
                      index += 3;
                    }

                    if (index < discover.length) {
                      sections.push(
                        <hr
                          key={`sep-${index}-after-small`}
                          className="border-t border-light-200/20 dark:border-dark-200/20 my-3 w-full"
                        />,
                      );
                    }

                    if (index < discover.length - 1) {
                      const twoMajorCards = discover.slice(index, index + 2);
                      twoMajorCards.forEach((item, i) => {
                        sections.push(
                          <MajorNewsCard
                            key={`double-${index + i}`}
                            item={item}
                            isLeft={i === 0}
                          />,
                        );
                        if (i === 0) {
                          sections.push(
                            <hr
                              key={`sep-double-${index + i}`}
                              className="border-t border-light-200/20 dark:border-dark-200/20 my-3 w-full"
                            />,
                          );
                        }
                      });
                      index += 2;
                    } else if (index < discover.length) {
                      sections.push(
                        <MajorNewsCard
                          key={`final-major-${index}`}
                          item={discover[index]}
                          isLeft={true}
                        />,
                      );
                      index++;
                    }

                    if (index < discover.length) {
                      sections.push(
                        <hr
                          key={`sep-${index}-after-major`}
                          className="border-t border-light-200/20 dark:border-dark-200/20 my-3 w-full"
                        />,
                      );
                    }

                    if (index < discover.length) {
                      const smallCards = discover.slice(index, index + 3);
                      sections.push(
                        <div
                          key={`small-group-2-${index}`}
                          className="grid lg:grid-cols-3 sm:grid-cols-2 grid-cols-1 gap-4"
                        >
                          {smallCards.map((item, i) => (
                            <SmallNewsCard
                              key={`small-2-${index + i}`}
                              item={item}
                            />
                          ))}
                        </div>,
                      );
                      index += 3;
                    }
                  }

                  return sections;
                })()}
            </div>
          </div>
        )}
      </div>
    </>
  );
};

export default Page;
```

## File: `src/app/library/layout.tsx`
```tsx
import { Metadata } from 'next';
import React from 'react';

export const metadata: Metadata = {
  title: 'Library - Vane',
};

const Layout = ({ children }: { children: React.ReactNode }) => {
  return <div>{children}</div>;
};

export default Layout;
```

## File: `src/app/library/page.tsx`
```tsx
'use client';

import DeleteChat from '@/components/DeleteChat';
import { formatTimeDifference } from '@/lib/utils';
import { BookOpenText, ClockIcon, FileText, Globe2Icon } from 'lucide-react';
import Link from 'next/link';
import { useEffect, useState } from 'react';

export interface Chat {
  id: string;
  title: string;
  createdAt: string;
  sources: string[];
  files: { fileId: string; name: string }[];
}

const Page = () => {
  const [chats, setChats] = useState<Chat[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchChats = async () => {
      setLoading(true);

      const res = await fetch(`/api/chats`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      const data = await res.json();

      setChats(data.chats);
      setLoading(false);
    };

    fetchChats();
  }, []);

  return (
    <div>
      <div className="flex flex-col pt-10 border-b border-light-200/20 dark:border-dark-200/20 pb-6 px-2">
        <div className="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-3">
          <div className="flex items-center justify-center">
            <BookOpenText size={45} className="mb-2.5" />
            <div className="flex flex-col">
              <h1
                className="text-5xl font-normal p-2 pb-0"
                style={{ fontFamily: 'PP Editorial, serif' }}
              >
                Library
              </h1>
              <div className="px-2 text-sm text-black/60 dark:text-white/60 text-center lg:text-left">
                Past chats, sources, and uploads.
              </div>
            </div>
          </div>

          <div className="flex items-center justify-center lg:justify-end gap-2 text-xs text-black/60 dark:text-white/60">
            <span className="inline-flex items-center gap-1 rounded-full border border-black/20 dark:border-white/20 px-2 py-0.5">
              <BookOpenText size={14} />
              {loading
                ? 'Loading…'
                : `${chats.length} ${chats.length === 1 ? 'chat' : 'chats'}`}
            </span>
          </div>
        </div>
      </div>

      {loading ? (
        <div className="flex flex-row items-center justify-center min-h-[60vh]">
          <svg
            aria-hidden="true"
            className="w-8 h-8 text-light-200 fill-light-secondary dark:text-[#202020] animate-spin dark:fill-[#ffffff3b]"
            viewBox="0 0 100 101"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M100 50.5908C100.003 78.2051 78.1951 100.003 50.5908 100C22.9765 99.9972 0.997224 78.018 1 50.4037C1.00281 22.7993 22.8108 0.997224 50.4251 1C78.0395 1.00281 100.018 22.8108 100 50.4251ZM9.08164 50.594C9.06312 73.3997 27.7909 92.1272 50.5966 92.1457C73.4023 92.1642 92.1298 73.4365 92.1483 50.6308C92.1669 27.8251 73.4392 9.0973 50.6335 9.07878C27.8278 9.06026 9.10003 27.787 9.08164 50.594Z"
              fill="currentColor"
            />
            <path
              d="M93.9676 39.0409C96.393 38.4037 97.8624 35.9116 96.9801 33.5533C95.1945 28.8227 92.871 24.3692 90.0681 20.348C85.6237 14.1775 79.4473 9.36872 72.0454 6.45794C64.6435 3.54717 56.3134 2.65431 48.3133 3.89319C45.869 4.27179 44.3768 6.77534 45.014 9.20079C45.6512 11.6262 48.1343 13.0956 50.5786 12.717C56.5073 11.8281 62.5542 12.5399 68.0406 14.7911C73.527 17.0422 78.2187 20.7487 81.5841 25.4923C83.7976 28.5886 85.4467 32.059 86.4416 35.7474C87.1273 38.1189 89.5423 39.6781 91.9676 39.0409Z"
              fill="currentFill"
            />
          </svg>
        </div>
      ) : chats.length === 0 ? (
        <div className="flex flex-col items-center justify-center min-h-[70vh] px-2 text-center">
          <div className="flex items-center justify-center w-12 h-12 rounded-2xl border border-light-200 dark:border-dark-200 bg-light-secondary dark:bg-dark-secondary">
            <BookOpenText className="text-black/70 dark:text-white/70" />
          </div>
          <p className="mt-2 text-black/70 dark:text-white/70 text-sm">
            No chats found.
          </p>
          <p className="mt-1 text-black/70 dark:text-white/70 text-sm">
            <Link href="/" className="text-sky-400">
              Start a new chat
            </Link>{' '}
            to see it listed here.
          </p>
        </div>
      ) : (
        <div className="pt-6 pb-28 px-2">
          <div className="rounded-2xl border border-light-200 dark:border-dark-200 overflow-hidden bg-light-primary dark:bg-dark-primary">
            {chats.map((chat, index) => {
              const sourcesLabel =
                chat.sources.length === 0
                  ? null
                  : chat.sources.length <= 2
                    ? chat.sources
                        .map((s) => s.charAt(0).toUpperCase() + s.slice(1))
                        .join(', ')
                    : `${chat.sources
                        .slice(0, 2)
                        .map((s) => s.charAt(0).toUpperCase() + s.slice(1))
                        .join(', ')} + ${chat.sources.length - 2}`;

              return (
                <div
                  key={chat.id}
                  className={
                    'group flex flex-col gap-2 p-4 hover:bg-light-secondary dark:hover:bg-dark-secondary transition-colors duration-200 ' +
                    (index !== chats.length - 1
                      ? 'border-b border-light-200 dark:border-dark-200'
                      : '')
                  }
                >
                  <div className="flex items-start justify-between gap-3">
                    <Link
                      href={`/c/${chat.id}`}
                      className="flex-1 text-black dark:text-white text-base lg:text-lg font-medium leading-snug line-clamp-2 group-hover:text-[#24A0ED] transition duration-200"
                      title={chat.title}
                    >
                      {chat.title}
                    </Link>
                    <div className="pt-0.5 shrink-0">
                      <DeleteChat
                        chatId={chat.id}
                        chats={chats}
                        setChats={setChats}
                      />
                    </div>
                  </div>

                  <div className="flex flex-wrap items-center gap-2 text-black/70 dark:text-white/70">
                    <span className="inline-flex items-center gap-1 text-xs">
                      <ClockIcon size={14} />
                      {formatTimeDifference(new Date(), chat.createdAt)} Ago
                    </span>

                    {sourcesLabel && (
                      <span className="inline-flex items-center gap-1 text-xs border border-black/20 dark:border-white/20 rounded-full px-2 py-0.5">
                        <Globe2Icon size={14} />
                        {sourcesLabel}
                      </span>
                    )}
                    {chat.files.length > 0 && (
                      <span className="inline-flex items-center gap-1 text-xs border border-black/20 dark:border-white/20 rounded-full px-2 py-0.5">
                        <FileText size={14} />
                        {chat.files.length}{' '}
                        {chat.files.length === 1 ? 'file' : 'files'}
                      </span>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};

export default Page;
```

## File: `src/components/AssistantSteps.tsx`
```tsx
'use client';

import {
  Brain,
  Search,
  FileText,
  ChevronDown,
  ChevronUp,
  BookSearch,
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { useEffect, useState } from 'react';
import { ResearchBlock, ResearchBlockSubStep } from '@/lib/types';
import { useChat } from '@/lib/hooks/useChat';

const getStepIcon = (step: ResearchBlockSubStep) => {
  if (step.type === 'reasoning') {
    return <Brain className="w-4 h-4" />;
  } else if (step.type === 'searching' || step.type === 'upload_searching') {
    return <Search className="w-4 h-4" />;
  } else if (
    step.type === 'search_results' ||
    step.type === 'upload_search_results'
  ) {
    return <FileText className="w-4 h-4" />;
  } else if (step.type === 'reading') {
    return <BookSearch className="w-4 h-4" />;
  }

  return null;
};

const getStepTitle = (
  step: ResearchBlockSubStep,
  isStreaming: boolean,
): string => {
  if (step.type === 'reasoning') {
    return isStreaming && !step.reasoning ? 'Thinking...' : 'Thinking';
  } else if (step.type === 'searching') {
    const queries = Array.isArray(step.searching) ? step.searching : [];
    return `Searching ${queries.length} ${queries.length === 1 ? 'query' : 'queries'}`;
  } else if (step.type === 'search_results') {
    return `Found ${step.reading.length} ${step.reading.length === 1 ? 'result' : 'results'}`;
  } else if (step.type === 'reading') {
    return `Reading ${step.reading.length} ${step.reading.length === 1 ? 'source' : 'sources'}`;
  } else if (step.type === 'upload_searching') {
    return 'Scanning your uploaded documents';
  } else if (step.type === 'upload_search_results') {
    return `Reading ${step.results.length} ${step.results.length === 1 ? 'document' : 'documents'}`;
  }

  return 'Processing';
};

const AssistantSteps = ({
  block,
  status,
  isLast,
}: {
  block: ResearchBlock;
  status: 'answering' | 'completed' | 'error';
  isLast: boolean;
}) => {
  const [isExpanded, setIsExpanded] = useState(
    isLast && status === 'answering' ? true : false,
  );
  const { researchEnded, loading } = useChat();

  useEffect(() => {
    if (researchEnded && isLast) {
      setIsExpanded(false);
    } else if (status === 'answering' && isLast) {
      setIsExpanded(true);
    }
  }, [researchEnded, status]);

  if (!block || block.data.subSteps.length === 0) return null;

  return (
    <div className="rounded-lg bg-light-secondary dark:bg-dark-secondary border border-light-200 dark:border-dark-200 overflow-hidden">
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="w-full flex items-center justify-between p-3 hover:bg-light-200 dark:hover:bg-dark-200 transition duration-200"
      >
        <div className="flex items-center gap-2">
          <Brain className="w-4 h-4 text-black dark:text-white" />
          <span className="text-sm font-medium text-black dark:text-white">
            Research Progress ({block.data.subSteps.length}{' '}
            {block.data.subSteps.length === 1 ? 'step' : 'steps'})
          </span>
        </div>
        {isExpanded ? (
          <ChevronUp className="w-4 h-4 text-black/70 dark:text-white/70" />
        ) : (
          <ChevronDown className="w-4 h-4 text-black/70 dark:text-white/70" />
        )}
      </button>

      <AnimatePresence>
        {isExpanded && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="border-t border-light-200 dark:border-dark-200"
          >
            <div className="p-3 space-y-2">
              {block.data.subSteps.map((step, index) => {
                const isLastStep = index === block.data.subSteps.length - 1;
                const isStreaming = loading && isLastStep && !researchEnded;

                return (
                  <motion.div
                    key={step.id}
                    initial={{ opacity: 0, x: -10 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ duration: 0.2, delay: 0 }}
                    className="flex gap-2"
                  >
                    <div className="flex flex-col items-center -mt-0.5">
                      <div
                        className={`rounded-full p-1.5 bg-light-100 dark:bg-dark-100 text-black/70 dark:text-white/70 ${isStreaming ? 'animate-pulse' : ''}`}
                      >
                        {getStepIcon(step)}
                      </div>
                      {index < block.data.subSteps.length - 1 && (
                        <div className="w-0.5 flex-1 min-h-[20px] bg-light-200 dark:bg-dark-200 mt-1.5" />
                      )}
                    </div>

                    <div className="flex-1 pb-1">
                      <span className="text-sm font-medium text-black dark:text-white">
                        {getStepTitle(step, isStreaming)}
                      </span>

                      {step.type === 'reasoning' && (
                        <>
                          {step.reasoning && (
                            <p className="text-xs text-black/70 dark:text-white/70 mt-0.5">
                              {step.reasoning}
                            </p>
                          )}
                          {isStreaming && !step.reasoning && (
                            <div className="flex items-center gap-1.5 mt-0.5">
                              <div
                                className="w-1.5 h-1.5 bg-black/40 dark:bg-white/40 rounded-full animate-bounce"
                                style={{ animationDelay: '0ms' }}
                              />
                              <div
                                className="w-1.5 h-1.5 bg-black/40 dark:bg-white/40 rounded-full animate-bounce"
                                style={{ animationDelay: '150ms' }}
                              />
                              <div
                                className="w-1.5 h-1.5 bg-black/40 dark:bg-white/40 rounded-full animate-bounce"
                                style={{ animationDelay: '300ms' }}
                              />
                            </div>
                          )}
                        </>
                      )}

                      {step.type === 'searching' &&
                        Array.isArray(step.searching) &&
                        step.searching.length > 0 && (
                          <div className="flex flex-wrap gap-1.5 mt-1.5">
                            {step.searching.map((query, idx) => (
                              <span
                                key={idx}
                                className="inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium bg-light-100 dark:bg-dark-100 text-black/70 dark:text-white/70 border border-light-200 dark:border-dark-200"
                              >
                                {query}
                              </span>
                            ))}
                          </div>
                        )}

                      {(step.type === 'search_results' ||
                        step.type === 'reading') &&
                        step.reading.length > 0 && (
                          <div className="flex flex-wrap gap-1.5 mt-1.5">
                            {step.reading.slice(0, 4).map((result, idx) => {
                              const url = result.metadata.url || '';
                              const title = result.metadata.title || 'Untitled';
                              const domain = url ? new URL(url).hostname : '';
                              const faviconUrl = domain
                                ? `https://s2.googleusercontent.com/s2/favicons?domain=${domain}&sz=128`
                                : '';

                              return (
                                <a
                                  key={idx}
                                  href={url}
                                  target="_blank"
                                  className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md text-xs font-medium bg-light-100 dark:bg-dark-100 text-black/70 dark:text-white/70 border border-light-200 dark:border-dark-200"
                                >
                                  {faviconUrl && (
                                    <img
                                      src={faviconUrl}
                                      alt=""
                                      className="w-3 h-3 rounded-sm flex-shrink-0"
                                      onError={(e) => {
                                        e.currentTarget.style.display = 'none';
                                      }}
                                    />
                                  )}
                                  <span className="line-clamp-1">{title}</span>
                                </a>
                              );
                            })}
                          </div>
                        )}

                      {step.type === 'upload_searching' &&
                        step.queries.length > 0 && (
                          <div className="flex flex-wrap gap-1.5 mt-1.5">
                            {step.queries.map((query, idx) => (
                              <span
                                key={idx}
                                className="inline-flex items-center px-2 py-0.5 rounded-md text-xs font-medium bg-light-100 dark:bg-dark-100 text-black/70 dark:text-white/70 border border-light-200 dark:border-dark-200"
                              >
                                {query}
                              </span>
                            ))}
                          </div>
                        )}

                      {step.type === 'upload_search_results' &&
                        step.results.length > 0 && (
                          <div className="mt-1.5 grid gap-3 lg:grid-cols-3">
                            {step.results.slice(0, 4).map((result, idx) => {
                              const title =
                                (result.metadata &&
                                  (result.metadata.title ||
                                    result.metadata.fileName)) ||
                                'Untitled document';

                              return (
                                <div
                                  key={idx}
                                  className="flex flex-row space-x-3 rounded-lg border border-light-200 dark:border-dark-200 bg-light-100 dark:bg-dark-100 p-2 cursor-pointer"
                                >
                                  <div className="mt-0.5 h-10 w-10 rounded-md bg-cyan-100 text-cyan-800 dark:bg-sky-500 dark:text-cyan-50 flex items-center justify-center">
                                    <FileText className="w-5 h-5" />
                                  </div>
                                  <div className="flex flex-col justify-center">
                                    <p className="text-[13px] text-black dark:text-white line-clamp-1">
                                      {title}
                                    </p>
                                  </div>
                                </div>
                              );
                            })}
                          </div>
                        )}
                    </div>
                  </motion.div>
                );
              })}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default AssistantSteps;
```

## File: `src/components/Chat.tsx`
```tsx
'use client';

import { Fragment, useEffect, useRef, useState } from 'react';
import MessageInput from './MessageInput';
import MessageBox from './MessageBox';
import MessageBoxLoading from './MessageBoxLoading';
import { useChat } from '@/lib/hooks/useChat';

const Chat = () => {
  const { sections, loading, messageAppeared, messages } = useChat();

  const [dividerWidth, setDividerWidth] = useState(0);
  const dividerRef = useRef<HTMLDivElement | null>(null);
  const messageEnd = useRef<HTMLDivElement | null>(null);
  const lastScrolledRef = useRef<number>(0);

  useEffect(() => {
    const updateDividerWidth = () => {
      if (dividerRef.current) {
        setDividerWidth(dividerRef.current.offsetWidth);
      }
    };

    updateDividerWidth();

    const resizeObserver = new ResizeObserver(() => {
      updateDividerWidth();
    });

    const currentRef = dividerRef.current;
    if (currentRef) {
      resizeObserver.observe(currentRef);
    }

    window.addEventListener('resize', updateDividerWidth);

    return () => {
      if (currentRef) {
        resizeObserver.unobserve(currentRef);
      }
      resizeObserver.disconnect();
      window.removeEventListener('resize', updateDividerWidth);
    };
  }, [sections.length]);

  useEffect(() => {
    const scroll = () => {
      messageEnd.current?.scrollIntoView({ behavior: 'auto' });
    };

    if (messages.length === 1) {
      document.title = `${messages[0].query.substring(0, 30)} - Vane`;
    }

    if (sections.length > lastScrolledRef.current) {
      scroll();
      lastScrolledRef.current = sections.length;
    }
  }, [messages]);

  return (
    <div className="flex flex-col space-y-6 pt-8 pb-44 lg:pb-28 sm:mx-4 md:mx-8">
      {sections.map((section, i) => {
        const isLast = i === sections.length - 1;

        return (
          <Fragment key={section.message.messageId}>
            <MessageBox
              section={section}
              sectionIndex={i}
              dividerRef={isLast ? dividerRef : undefined}
              isLast={isLast}
            />
            {!isLast && (
              <div className="h-px w-full bg-light-secondary dark:bg-dark-secondary" />
            )}
          </Fragment>
        );
      })}
      {loading && !messageAppeared && <MessageBoxLoading />}
      <div ref={messageEnd} className="h-0" />
      {dividerWidth > 0 && (
        <div
          className="fixed z-40 bottom-24 lg:bottom-6"
          style={{ width: dividerWidth }}
        >
          <div
            className="pointer-events-none absolute -bottom-6 left-0 right-0 h-[calc(100%+24px+24px)] dark:hidden"
            style={{
              background:
                'linear-gradient(to top, #ffffff 0%, #ffffff 35%, rgba(255,255,255,0.95) 45%, rgba(255,255,255,0.85) 55%, rgba(255,255,255,0.7) 65%, rgba(255,255,255,0.5) 75%, rgba(255,255,255,0.3) 85%, rgba(255,255,255,0.1) 92%, transparent 100%)',
            }}
          />
          <div
            className="pointer-events-none absolute -bottom-6 left-0 right-0 h-[calc(100%+24px+24px)] hidden dark:block"
            style={{
              background:
                'linear-gradient(to top, #0d1117 0%, #0d1117 35%, rgba(13,17,23,0.95) 45%, rgba(13,17,23,0.85) 55%, rgba(13,17,23,0.7) 65%, rgba(13,17,23,0.5) 75%, rgba(13,17,23,0.3) 85%, rgba(13,17,23,0.1) 92%, transparent 100%)',
            }}
          />
          <MessageInput />
        </div>
      )}
    </div>
  );
};

export default Chat;
```

## File: `src/components/ChatWindow.tsx`
```tsx
'use client';

import Navbar from './Navbar';
import Chat from './Chat';
import EmptyChat from './EmptyChat';
import NextError from 'next/error';
import { useChat } from '@/lib/hooks/useChat';
import SettingsButtonMobile from './Settings/SettingsButtonMobile';
import { Block } from '@/lib/types';
import Loader from './ui/Loader';

export interface BaseMessage {
  chatId: string;
  messageId: string;
  createdAt: Date;
}

export interface Message extends BaseMessage {
  backendId: string;
  query: string;
  responseBlocks: Block[];
  status: 'answering' | 'completed' | 'error';
}

export interface File {
  fileName: string;
  fileExtension: string;
  fileId: string;
}

export interface Widget {
  widgetType: string;
  params: Record<string, any>;
}

const ChatWindow = () => {
  const { hasError, notFound, messages, isReady } = useChat();

  if (hasError) {
    return (
      <div className="relative">
        <div className="absolute w-full flex flex-row items-center justify-end mr-5 mt-5">
          <SettingsButtonMobile />
        </div>
        <div className="flex flex-col items-center justify-center min-h-screen">
          <p className="dark:text-white/70 text-black/70 text-sm">
            Failed to connect to the server. Please try again later.
          </p>
        </div>
      </div>
    );
  }

  return isReady ? (
    notFound ? (
      <NextError statusCode={404} />
    ) : (
      <div>
        {messages.length > 0 ? (
          <>
            <Navbar />
            <Chat />
          </>
        ) : (
          <EmptyChat />
        )}
      </div>
    )
  ) : (
    <div className="flex items-center justify-center min-h-screen w-full">
      <Loader />
    </div>
  );
};

export default ChatWindow;
```

## File: `src/components/DeleteChat.tsx`
```tsx
import { Trash } from 'lucide-react';
import {
  Description,
  Dialog,
  DialogBackdrop,
  DialogPanel,
  DialogTitle,
  Transition,
  TransitionChild,
} from '@headlessui/react';
import { Fragment, useState } from 'react';
import { toast } from 'sonner';
import { Chat } from '@/app/library/page';

const DeleteChat = ({
  chatId,
  chats,
  setChats,
  redirect = false,
}: {
  chatId: string;
  chats: Chat[];
  setChats: (chats: Chat[]) => void;
  redirect?: boolean;
}) => {
  const [confirmationDialogOpen, setConfirmationDialogOpen] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleDelete = async () => {
    setLoading(true);
    try {
      const res = await fetch(`/api/chats/${chatId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (res.status != 200) {
        throw new Error('Failed to delete chat');
      }

      const newChats = chats.filter((chat) => chat.id !== chatId);

      setChats(newChats);

      if (redirect) {
        window.location.href = '/';
      }
    } catch (err: any) {
      toast.error(err.message);
    } finally {
      setConfirmationDialogOpen(false);
      setLoading(false);
    }
  };

  return (
    <>
      <button
        onClick={() => {
          setConfirmationDialogOpen(true);
        }}
        className="bg-transparent text-red-400 hover:scale-105 transition duration-200"
      >
        <Trash size={17} />
      </button>
      <Transition appear show={confirmationDialogOpen} as={Fragment}>
        <Dialog
          as="div"
          className="relative z-50"
          onClose={() => {
            if (!loading) {
              setConfirmationDialogOpen(false);
            }
          }}
        >
          <DialogBackdrop className="fixed inset-0 bg-black/30" />
          <div className="fixed inset-0 overflow-y-auto">
            <div className="flex min-h-full items-center justify-center p-4 text-center">
              <TransitionChild
                as={Fragment}
                enter="ease-out duration-200"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-100"
                leaveFrom="opacity-100 scale-200"
                leaveTo="opacity-0 scale-95"
              >
                <DialogPanel className="w-full max-w-md transform rounded-2xl bg-light-secondary dark:bg-dark-secondary border border-light-200 dark:border-dark-200 p-6 text-left align-middle shadow-xl transition-all">
                  <DialogTitle className="text-lg font-medium leading-6 dark:text-white">
                    Delete Confirmation
                  </DialogTitle>
                  <Description className="text-sm dark:text-white/70 text-black/70">
                    Are you sure you want to delete this chat?
                  </Description>
                  <div className="flex flex-row items-end justify-end space-x-4 mt-6">
                    <button
                      onClick={() => {
                        if (!loading) {
                          setConfirmationDialogOpen(false);
                        }
                      }}
                      className="text-black/50 dark:text-white/50 text-sm hover:text-black/70 hover:dark:text-white/70 transition duration-200"
                    >
                      Cancel
                    </button>
                    <button
                      onClick={handleDelete}
                      className="text-red-400 text-sm hover:text-red-500 transition duration200"
                    >
                      Delete
                    </button>
                  </div>
                </DialogPanel>
              </TransitionChild>
            </div>
          </div>
        </Dialog>
      </Transition>
    </>
  );
};

export default DeleteChat;
```

## File: `src/components/EmptyChat.tsx`
```tsx
'use client';

import { useEffect, useState } from 'react';
import { Settings } from 'lucide-react';
import EmptyChatMessageInput from './EmptyChatMessageInput';
import { File } from './ChatWindow';
import Link from 'next/link';
import WeatherWidget from './WeatherWidget';
import NewsArticleWidget from './NewsArticleWidget';
import SettingsButtonMobile from '@/components/Settings/SettingsButtonMobile';
import {
  getShowNewsWidget,
  getShowWeatherWidget,
} from '@/lib/config/clientRegistry';

const EmptyChat = () => {
  const [showWeather, setShowWeather] = useState(() =>
    typeof window !== 'undefined' ? getShowWeatherWidget() : true,
  );
  const [showNews, setShowNews] = useState(() =>
    typeof window !== 'undefined' ? getShowNewsWidget() : true,
  );

  useEffect(() => {
    const updateWidgetVisibility = () => {
      setShowWeather(getShowWeatherWidget());
      setShowNews(getShowNewsWidget());
    };

    updateWidgetVisibility();

    window.addEventListener('client-config-changed', updateWidgetVisibility);
    window.addEventListener('storage', updateWidgetVisibility);

    return () => {
      window.removeEventListener(
        'client-config-changed',
        updateWidgetVisibility,
      );
      window.removeEventListener('storage', updateWidgetVisibility);
    };
  }, []);

  return (
    <div className="relative">
      <div className="absolute w-full flex flex-row items-center justify-end mr-5 mt-5">
        <SettingsButtonMobile />
      </div>
      <div className="flex flex-col items-center justify-center min-h-screen max-w-screen-sm mx-auto p-2 space-y-4">
        <div className="flex flex-col items-center justify-center w-full space-y-8">
          <h2 className="text-black/70 dark:text-white/70 text-3xl font-medium -mt-8">
            Research begins here.
          </h2>
          <EmptyChatMessageInput />
        </div>
        {(showWeather || showNews) && (
          <div className="flex flex-col w-full gap-4 mt-2 sm:flex-row sm:justify-center">
            {showWeather && (
              <div className="flex-1 w-full">
                <WeatherWidget />
              </div>
            )}
            {showNews && (
              <div className="flex-1 w-full">
                <NewsArticleWidget />
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default EmptyChat;
```

## File: `src/components/EmptyChatMessageInput.tsx`
```tsx
import { ArrowRight } from 'lucide-react';
import { useEffect, useRef, useState } from 'react';
import TextareaAutosize from 'react-textarea-autosize';
import Sources from './MessageInputActions/Sources';
import Optimization from './MessageInputActions/Optimization';
import Attach from './MessageInputActions/Attach';
import { useChat } from '@/lib/hooks/useChat';
import ModelSelector from './MessageInputActions/ChatModelSelector';

const EmptyChatMessageInput = () => {
  const { sendMessage } = useChat();

  /* const [copilotEnabled, setCopilotEnabled] = useState(false); */
  const [message, setMessage] = useState('');

  const inputRef = useRef<HTMLTextAreaElement | null>(null);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      const activeElement = document.activeElement;

      const isInputFocused =
        activeElement?.tagName === 'INPUT' ||
        activeElement?.tagName === 'TEXTAREA' ||
        activeElement?.hasAttribute('contenteditable');

      if (e.key === '/' && !isInputFocused) {
        e.preventDefault();
        inputRef.current?.focus();
      }
    };

    document.addEventListener('keydown', handleKeyDown);

    inputRef.current?.focus();

    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        sendMessage(message);
        setMessage('');
      }}
      onKeyDown={(e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          sendMessage(message);
          setMessage('');
        }
      }}
      className="w-full"
    >
      <div className="flex flex-col bg-light-secondary dark:bg-dark-secondary px-3 pt-5 pb-3 rounded-2xl w-full border border-light-200 dark:border-dark-200 shadow-sm shadow-light-200/10 dark:shadow-black/20 transition-all duration-200 focus-within:border-light-300 dark:focus-within:border-dark-300">
        <TextareaAutosize
          ref={inputRef}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          minRows={2}
          className="px-2 bg-transparent placeholder:text-[15px] placeholder:text-black/50 dark:placeholder:text-white/50 text-sm text-black dark:text-white resize-none focus:outline-none w-full max-h-24 lg:max-h-36 xl:max-h-48"
          placeholder="Ask anything..."
        />
        <div className="flex flex-row items-center justify-between mt-4">
          <Optimization />
          <div className="flex flex-row items-center space-x-2">
            <div className="flex flex-row items-center space-x-1">
              <Sources />
              <ModelSelector />
              <Attach />
            </div>
            <button
              disabled={message.trim().length === 0}
              className="bg-sky-500 text-white disabled:text-black/50 dark:disabled:text-white/50 disabled:bg-[#e0e0dc] dark:disabled:bg-[#ececec21] hover:bg-opacity-85 transition duration-100 rounded-full p-2"
            >
              <ArrowRight className="bg-background" size={17} />
            </button>
          </div>
        </div>
      </div>
    </form>
  );
};

export default EmptyChatMessageInput;
```

## File: `src/components/Layout.tsx`
```tsx
const Layout = ({ children }: { children: React.ReactNode }) => {
  return (
    <main className="lg:pl-20 bg-light-primary dark:bg-dark-primary min-h-screen">
      <div className="max-w-screen-lg lg:mx-auto mx-4">{children}</div>
    </main>
  );
};

export default Layout;
```

## File: `src/components/MessageBox.tsx`
```tsx
'use client';

/* eslint-disable @next/next/no-img-element */
import React, { MutableRefObject } from 'react';
import { cn } from '@/lib/utils';
import {
  BookCopy,
  Disc3,
  Volume2,
  StopCircle,
  Layers3,
  Plus,
  CornerDownRight,
} from 'lucide-react';
import Markdown, { MarkdownToJSX, RuleType } from 'markdown-to-jsx';
import Copy from './MessageActions/Copy';
import Rewrite from './MessageActions/Rewrite';
import MessageSources from './MessageSources';
import SearchImages from './SearchImages';
import SearchVideos from './SearchVideos';
import { useSpeech } from 'react-text-to-speech';
import ThinkBox from './ThinkBox';
import { useChat, Section } from '@/lib/hooks/useChat';
import Citation from './MessageRenderer/Citation';
import AssistantSteps from './AssistantSteps';
import { ResearchBlock } from '@/lib/types';
import Renderer from './Widgets/Renderer';
import CodeBlock from './MessageRenderer/CodeBlock';

const ThinkTagProcessor = ({
  children,
  thinkingEnded,
}: {
  children: React.ReactNode;
  thinkingEnded: boolean;
}) => {
  return (
    <ThinkBox content={children as string} thinkingEnded={thinkingEnded} />
  );
};

const MessageBox = ({
  section,
  sectionIndex,
  dividerRef,
  isLast,
}: {
  section: Section;
  sectionIndex: number;
  dividerRef?: MutableRefObject<HTMLDivElement | null>;
  isLast: boolean;
}) => {
  const {
    loading,
    sendMessage,
    rewrite,
    messages,
    researchEnded,
    chatHistory,
  } = useChat();

  const parsedMessage = section.parsedTextBlocks.join('\n\n');
  const speechMessage = section.speechMessage || '';
  const thinkingEnded = section.thinkingEnded;

  const sourceBlocks = section.message.responseBlocks.filter(
    (block): block is typeof block & { type: 'source' } =>
      block.type === 'source',
  );

  const sources = sourceBlocks.flatMap((block) => block.data);

  const hasContent = section.parsedTextBlocks.length > 0;

  const { speechStatus, start, stop } = useSpeech({ text: speechMessage });

  const markdownOverrides: MarkdownToJSX.Options = {
    renderRule(next, node, renderChildren, state) {
      if (node.type === RuleType.codeInline) {
        return `\`${node.text}\``;
      }

      if (node.type === RuleType.codeBlock) {
        return (
          <CodeBlock key={state.key} language={node.lang || ''}>
            {node.text}
          </CodeBlock>
        );
      }

      return next();
    },
    overrides: {
      think: {
        component: ThinkTagProcessor,
        props: {
          thinkingEnded: thinkingEnded,
        },
      },
      citation: {
        component: Citation,
      },
    },
  };

  return (
    <div className="space-y-6">
      <div className={'w-full pt-8 break-words'}>
        <h2 className="text-black dark:text-white font-medium text-3xl lg:w-9/12">
          {section.message.query}
        </h2>
      </div>

      <div className="flex flex-col space-y-9 lg:space-y-0 lg:flex-row lg:justify-between lg:space-x-9">
        <div
          ref={dividerRef}
          className="flex flex-col space-y-6 w-full lg:w-9/12"
        >
          {sources.length > 0 && (
            <div className="flex flex-col space-y-2">
              <div className="flex flex-row items-center space-x-2">
                <BookCopy className="text-black dark:text-white" size={20} />
                <h3 className="text-black dark:text-white font-medium text-xl">
                  Sources
                </h3>
              </div>
              <MessageSources sources={sources} />
            </div>
          )}

          {section.message.responseBlocks
            .filter(
              (block): block is ResearchBlock =>
                block.type === 'research' && block.data.subSteps.length > 0,
            )
            .map((researchBlock) => (
              <div key={researchBlock.id} className="flex flex-col space-y-2">
                <AssistantSteps
                  block={researchBlock}
                  status={section.message.status}
                  isLast={isLast}
                />
              </div>
            ))}

          {isLast &&
            loading &&
            !researchEnded &&
            !section.message.responseBlocks.some(
              (b) => b.type === 'research' && b.data.subSteps.length > 0,
            ) && (
              <div className="flex items-center gap-2 p-3 rounded-lg bg-light-secondary dark:bg-dark-secondary border border-light-200 dark:border-dark-200">
                <Disc3 className="w-4 h-4 text-black dark:text-white animate-spin" />
                <span className="text-sm text-black/70 dark:text-white/70">
                  Brainstorming...
                </span>
              </div>
            )}

          {section.widgets.length > 0 && <Renderer widgets={section.widgets} />}

          <div className="flex flex-col space-y-2">
            {sources.length > 0 && (
              <div className="flex flex-row items-center space-x-2">
                <Disc3
                  className={cn(
                    'text-black dark:text-white',
                    isLast && loading ? 'animate-spin' : 'animate-none',
                  )}
                  size={20}
                />
                <h3 className="text-black dark:text-white font-medium text-xl">
                  Answer
                </h3>
              </div>
            )}

            {hasContent && (
              <>
                <Markdown
                  className={cn(
                    'prose prose-h1:mb-3 prose-h2:mb-2 prose-h2:mt-6 prose-h2:font-[800] prose-h3:mt-4 prose-h3:mb-1.5 prose-h3:font-[600] dark:prose-invert prose-p:leading-relaxed prose-pre:p-0 font-[400]',
                    'max-w-none break-words text-black dark:text-white',
                  )}
                  options={markdownOverrides}
                >
                  {parsedMessage}
                </Markdown>

                {loading && isLast ? null : (
                  <div className="flex flex-row items-center justify-between w-full text-black dark:text-white py-4">
                    <div className="flex flex-row items-center -ml-2">
                      <Rewrite
                        rewrite={rewrite}
                        messageId={section.message.messageId}
                      />
                    </div>
                    <div className="flex flex-row items-center -mr-2">
                      <Copy initialMessage={parsedMessage} section={section} />
                      <button
                        onClick={() => {
                          if (speechStatus === 'started') {
                            stop();
                          } else {
                            start();
                          }
                        }}
                        className="p-2 text-black/70 dark:text-white/70 rounded-full hover:bg-light-secondary dark:hover:bg-dark-secondary transition duration-200 hover:text-black dark:hover:text-white"
                      >
                        {speechStatus === 'started' ? (
                          <StopCircle size={16} />
                        ) : (
                          <Volume2 size={16} />
                        )}
                      </button>
                    </div>
                  </div>
                )}

                {isLast &&
                  section.suggestions &&
                  section.suggestions.length > 0 &&
                  hasContent &&
                  !loading && (
                    <div className="mt-6">
                      <div className="flex flex-row items-center space-x-2 mb-4">
                        <Layers3
                          className="text-black dark:text-white"
                          size={20}
                        />
                        <h3 className="text-black dark:text-white font-medium text-xl">
                          Related
                        </h3>
                      </div>
                      <div className="space-y-0">
                        {section.suggestions.map(
                          (suggestion: string, i: number) => (
                            <div key={i}>
                              <div className="h-px bg-light-200/40 dark:bg-dark-200/40" />
                              <button
                                onClick={() => sendMessage(suggestion)}
                                className="group w-full py-4 text-left transition-colors duration-200"
                              >
                                <div className="flex items-center justify-between gap-3">
                                  <div className="flex flex-row space-x-3 items-center">
                                    <CornerDownRight
                                      size={15}
                                      className="group-hover:text-sky-400 transition-colors duration-200 flex-shrink-0"
                                    />
                                    <p className="text-sm text-black/70 dark:text-white/70 group-hover:text-sky-400 transition-colors duration-200 leading-relaxed">
                                      {suggestion}
                                    </p>
                                  </div>
                                  <Plus
                                    size={16}
                                    className="text-black/40 dark:text-white/40 group-hover:text-sky-400 transition-colors duration-200 flex-shrink-0"
                                  />
                                </div>
                              </button>
                            </div>
                          ),
                        )}
                      </div>
                    </div>
                  )}
              </>
            )}
          </div>
        </div>

        {hasContent && (
          <div className="lg:sticky lg:top-20 flex flex-col items-center space-y-3 w-full lg:w-3/12 z-30 h-full pb-4">
            <SearchImages
              query={section.message.query}
              chatHistory={chatHistory}
              messageId={section.message.messageId}
            />
            <SearchVideos
              chatHistory={chatHistory}
              query={section.message.query}
              messageId={section.message.messageId}
            />
          </div>
        )}
      </div>
    </div>
  );
};

export default MessageBox;
```

## File: `src/components/MessageBoxLoading.tsx`
```tsx
const MessageBoxLoading = () => {
  return (
    <div className="flex flex-col space-y-2 w-full lg:w-9/12 bg-light-primary dark:bg-dark-primary animate-pulse rounded-lg py-3">
      <div className="h-2 rounded-full w-full bg-light-secondary dark:bg-dark-secondary" />
      <div className="h-2 rounded-full w-9/12 bg-light-secondary dark:bg-dark-secondary" />
      <div className="h-2 rounded-full w-10/12 bg-light-secondary dark:bg-dark-secondary" />
    </div>
  );
};

export default MessageBoxLoading;
```

## File: `src/components/MessageInput.tsx`
```tsx
import { cn } from '@/lib/utils';
import { ArrowUp } from 'lucide-react';
import { useEffect, useRef, useState } from 'react';
import TextareaAutosize from 'react-textarea-autosize';
import AttachSmall from './MessageInputActions/AttachSmall';
import { useChat } from '@/lib/hooks/useChat';

const MessageInput = () => {
  const { loading, sendMessage } = useChat();

  const [copilotEnabled, setCopilotEnabled] = useState(false);
  const [message, setMessage] = useState('');
  const [textareaRows, setTextareaRows] = useState(1);
  const [mode, setMode] = useState<'multi' | 'single'>('single');

  useEffect(() => {
    if (textareaRows >= 2 && message && mode === 'single') {
      setMode('multi');
    } else if (!message && mode === 'multi') {
      setMode('single');
    }
  }, [textareaRows, mode, message]);

  const inputRef = useRef<HTMLTextAreaElement | null>(null);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      const activeElement = document.activeElement;

      const isInputFocused =
        activeElement?.tagName === 'INPUT' ||
        activeElement?.tagName === 'TEXTAREA' ||
        activeElement?.hasAttribute('contenteditable');

      if (e.key === '/' && !isInputFocused) {
        e.preventDefault();
        inputRef.current?.focus();
      }
    };

    document.addEventListener('keydown', handleKeyDown);

    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  return (
    <form
      onSubmit={(e) => {
        if (loading) return;
        e.preventDefault();
        sendMessage(message);
        setMessage('');
      }}
      onKeyDown={(e) => {
        if (e.key === 'Enter' && !e.shiftKey && !loading) {
          e.preventDefault();
          sendMessage(message);
          setMessage('');
        }
      }}
      className={cn(
        'relative bg-light-secondary dark:bg-dark-secondary p-4 flex items-center overflow-visible border border-light-200 dark:border-dark-200 shadow-sm shadow-light-200/10 dark:shadow-black/20 transition-all duration-200 focus-within:border-light-300 dark:focus-within:border-dark-300',
        mode === 'multi' ? 'flex-col rounded-2xl' : 'flex-row rounded-full',
      )}
    >
      {mode === 'single' && <AttachSmall />}
      <TextareaAutosize
        ref={inputRef}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onHeightChange={(height, props) => {
          setTextareaRows(Math.ceil(height / props.rowHeight));
        }}
        className="transition bg-transparent dark:placeholder:text-white/50 placeholder:text-sm text-sm dark:text-white resize-none focus:outline-none w-full px-2 max-h-24 lg:max-h-36 xl:max-h-48 flex-grow flex-shrink"
        placeholder="Ask a follow-up"
      />
      {mode === 'single' && (
        <button
          disabled={message.trim().length === 0 || loading}
          className="bg-[#24A0ED] text-white disabled:text-black/50 dark:disabled:text-white/50 hover:bg-opacity-85 transition duration-100 disabled:bg-[#e0e0dc79] dark:disabled:bg-[#ececec21] rounded-full p-2"
        >
          <ArrowUp className="bg-background" size={17} />
        </button>
      )}
      {mode === 'multi' && (
        <div className="flex flex-row items-center justify-between w-full pt-2">
          <AttachSmall />
          <button
            disabled={message.trim().length === 0 || loading}
            className="bg-[#24A0ED] text-white disabled:text-black/50 dark:disabled:text-white/50 hover:bg-opacity-85 transition duration-100 disabled:bg-[#e0e0dc79] dark:disabled:bg-[#ececec21] rounded-full p-2"
          >
            <ArrowUp className="bg-background" size={17} />
          </button>
        </div>
      )}
    </form>
  );
};

export default MessageInput;
```

## File: `src/components/MessageSources.tsx`
```tsx
/* eslint-disable @next/next/no-img-element */
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  Transition,
  TransitionChild,
} from '@headlessui/react';
import { File } from 'lucide-react';
import { Fragment, useState } from 'react';
import { Chunk } from '@/lib/types';

const MessageSources = ({ sources }: { sources: Chunk[] }) => {
  const [isDialogOpen, setIsDialogOpen] = useState(false);

  const closeModal = () => {
    setIsDialogOpen(false);
    document.body.classList.remove('overflow-hidden-scrollable');
  };

  const openModal = () => {
    setIsDialogOpen(true);
    document.body.classList.add('overflow-hidden-scrollable');
  };

  return (
    <div className="grid grid-cols-2 lg:grid-cols-4 gap-2">
      {sources.slice(0, 3).map((source, i) => (
        <a
          className="bg-light-100 hover:bg-light-200 dark:bg-dark-100 dark:hover:bg-dark-200 transition duration-200 rounded-lg p-3 flex flex-col space-y-2 font-medium"
          key={i}
          href={source.metadata.url}
          target="_blank"
        >
          <p className="dark:text-white text-xs overflow-hidden whitespace-nowrap text-ellipsis">
            {source.metadata.title}
          </p>
          <div className="flex flex-row items-center justify-between">
            <div className="flex flex-row items-center space-x-1">
              {source.metadata.url.includes('file_id://') ? (
                <div className="bg-dark-200 hover:bg-dark-100 transition duration-200 flex items-center justify-center w-6 h-6 rounded-full">
                  <File size={12} className="text-white/70" />
                </div>
              ) : (
                <img
                  src={`https://s2.googleusercontent.com/s2/favicons?domain_url=${source.metadata.url}`}
                  width={16}
                  height={16}
                  alt="favicon"
                  className="rounded-lg h-4 w-4"
                />
              )}
              <p className="text-xs text-black/50 dark:text-white/50 overflow-hidden whitespace-nowrap text-ellipsis">
                {source.metadata.url.includes('file_id://')
                  ? 'Uploaded File'
                  : source.metadata.url.replace(/.+\/\/|www.|\..+/g, '')}
              </p>
            </div>
            <div className="flex flex-row items-center space-x-1 text-black/50 dark:text-white/50 text-xs">
              <div className="bg-black/50 dark:bg-white/50 h-[4px] w-[4px] rounded-full" />
              <span>{i + 1}</span>
            </div>
          </div>
        </a>
      ))}
      {sources.length > 3 && (
        <button
          onClick={openModal}
          className="bg-light-100 hover:bg-light-200 dark:bg-dark-100 dark:hover:bg-dark-200 transition duration-200 rounded-lg p-3 flex flex-col space-y-2 font-medium"
        >
          <div className="flex flex-row items-center space-x-1">
            {sources.slice(3, 6).map((source, i) => {
              return source.metadata.url === 'File' ? (
                <div
                  key={i}
                  className="bg-dark-200 hover:bg-dark-100 transition duration-200 flex items-center justify-center w-6 h-6 rounded-full"
                >
                  <File size={12} className="text-white/70" />
                </div>
              ) : (
                <img
                  key={i}
                  src={`https://s2.googleusercontent.com/s2/favicons?domain_url=${source.metadata.url}`}
                  width={16}
                  height={16}
                  alt="favicon"
                  className="rounded-lg h-4 w-4"
                />
              );
            })}
          </div>
          <p className="text-xs text-black/50 dark:text-white/50">
            View {sources.length - 3} more
          </p>
        </button>
      )}
      <Transition appear show={isDialogOpen} as={Fragment}>
        <Dialog as="div" className="relative z-50" onClose={closeModal}>
          <div className="fixed inset-0 overflow-y-auto">
            <div className="flex min-h-full items-center justify-center p-4 text-center">
              <TransitionChild
                as={Fragment}
                enter="ease-out duration-200"
                enterFrom="opacity-0 scale-95"
                enterTo="opacity-100 scale-100"
                leave="ease-in duration-100"
                leaveFrom="opacity-100 scale-200"
                leaveTo="opacity-0 scale-95"
              >
                <DialogPanel className="w-full max-w-md transform rounded-2xl bg-light-secondary dark:bg-dark-secondary border border-light-200 dark:border-dark-200 p-6 text-left align-middle shadow-xl transition-all">
                  <DialogTitle className="text-lg font-medium leading-6 dark:text-white">
                    Sources
                  </DialogTitle>
                  <div className="grid grid-cols-2 gap-2 overflow-auto max-h-[300px] mt-2 pr-2">
                    {sources.map((source, i) => (
                      <a
                        className="bg-light-secondary hover:bg-light-200 dark:bg-dark-secondary dark:hover:bg-dark-200 border border-light-200 dark:border-dark-200 transition duration-200 rounded-lg p-3 flex flex-col space-y-2 font-medium"
                        key={i}
                        href={source.metadata.url}
                        target="_blank"
                      >
                        <p className="dark:text-white text-xs overflow-hidden whitespace-nowrap text-ellipsis">
                          {source.metadata.title}
                        </p>
                        <div className="flex flex-row items-center justify-between">
                          <div className="flex flex-row items-center space-x-1">
                            {source.metadata.url === 'File' ? (
                              <div className="bg-dark-200 hover:bg-dark-100 transition duration-200 flex items-center justify-center w-6 h-6 rounded-full">
                                <File size={12} className="text-white/70" />
                              </div>
                            ) : (
                              <img
                                src={`https://s2.googleusercontent.com/s2/favicons?domain_url=${source.metadata.url}`}
                                width={16}
                                height={16}
                                alt="favicon"
                                className="rounded-lg h-4 w-4"
                              />
                            )}
                            <p className="text-xs text-black/50 dark:text-white/50 overflow-hidden whitespace-nowrap text-ellipsis">
                              {source.metadata.url.replace(
                                /.+\/\/|www.|\..+/g,
                                '',
                              )}
                            </p>
                          </div>
                          <div className="flex flex-row items-center space-x-1 text-black/50 dark:text-white/50 text-xs">
                            <div className="bg-black/50 dark:bg-white/50 h-[4px] w-[4px] rounded-full" />
                            <span>{i + 1}</span>
                          </div>
                        </div>
                      </a>
                    ))}
                  </div>
                </DialogPanel>
              </TransitionChild>
            </div>
          </div>
        </Dialog>
      </Transition>
    </div>
  );
};

export default MessageSources;
```

## File: `src/components/Navbar.tsx`
```tsx
import { Clock, Edit, Share, Trash, FileText, FileDown } from 'lucide-react';
import { Message } from './ChatWindow';
import { useEffect, useState, Fragment } from 'react';
import { formatTimeDifference } from '@/lib/utils';
import DeleteChat from './DeleteChat';
import {
  Popover,
  PopoverButton,
  PopoverPanel,
  Transition,
} from '@headlessui/react';
import jsPDF from 'jspdf';
import { useChat, Section } from '@/lib/hooks/useChat';
import { SourceBlock } from '@/lib/types';

const downloadFile = (filename: string, content: string, type: string) => {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }, 0);
};

const exportAsMarkdown = (sections: Section[], title: string) => {
  const date = new Date(
    sections[0].message.createdAt || Date.now(),
  ).toLocaleString();
  let md = `# 💬 Chat Export: ${title}\n\n`;
  md += `*Exported on: ${date}*\n\n---\n`;

  sections.forEach((section, idx) => {
    md += `\n---\n`;
    md += `**🧑 User**  
`;
    md += `*${new Date(section.message.createdAt).toLocaleString()}*\n\n`;
    md += `> ${section.message.query.replace(/\n/g, '\n> ')}\n`;

    if (section.message.responseBlocks.length > 0) {
      md += `\n---\n`;
      md += `**🤖 Assistant**  
`;
      md += `*${new Date(section.message.createdAt).toLocaleString()}*\n\n`;
      md += `> ${section.message.responseBlocks
        .filter((b) => b.type === 'text')
        .map((block) => block.data)
        .join('\n')
        .replace(/\n/g, '\n> ')}\n`;
    }

    const sourceResponseBlock = section.message.responseBlocks.find(
      (block) => block.type === 'source',
    ) as SourceBlock | undefined;

    if (
      sourceResponseBlock &&
      sourceResponseBlock.data &&
      sourceResponseBlock.data.length > 0
    ) {
      md += `\n**Citations:**\n`;
      sourceResponseBlock.data.forEach((src: any, i: number) => {
        const url = src.metadata?.url || '';
        md += `- [${i + 1}] [${url}](${url})\n`;
      });
    }
  });
  md += '\n---\n';
  downloadFile(`${title || 'chat'}.md`, md, 'text/markdown');
};

const exportAsPDF = (sections: Section[], title: string) => {
  const doc = new jsPDF();
  const date = new Date(
    sections[0]?.message?.createdAt || Date.now(),
  ).toLocaleString();
  let y = 15;
  const pageHeight = doc.internal.pageSize.height;
  doc.setFontSize(18);
  doc.text(`Chat Export: ${title}`, 10, y);
  y += 8;
  doc.setFontSize(11);
  doc.setTextColor(100);
  doc.text(`Exported on: ${date}`, 10, y);
  y += 8;
  doc.setDrawColor(200);
  doc.line(10, y, 200, y);
  y += 6;
  doc.setTextColor(30);

  sections.forEach((section, idx) => {
    if (y > pageHeight - 30) {
      doc.addPage();
      y = 15;
    }
    doc.setFont('helvetica', 'bold');
    doc.text('User', 10, y);
    doc.setFont('helvetica', 'normal');
    doc.setFontSize(10);
    doc.setTextColor(120);
    doc.text(`${new Date(section.message.createdAt).toLocaleString()}`, 40, y);
    y += 6;
    doc.setTextColor(30);
    doc.setFontSize(12);
    const userLines = doc.splitTextToSize(section.message.query, 180);
    for (let i = 0; i < userLines.length; i++) {
      if (y > pageHeight - 20) {
        doc.addPage();
        y = 15;
      }
      doc.text(userLines[i], 12, y);
      y += 6;
    }
    y += 6;
    doc.setDrawColor(230);
    if (y > pageHeight - 10) {
      doc.addPage();
      y = 15;
    }
    doc.line(10, y, 200, y);
    y += 4;

    if (section.message.responseBlocks.length > 0) {
      if (y > pageHeight - 30) {
        doc.addPage();
        y = 15;
      }
      doc.setFont('helvetica', 'bold');
      doc.text('Assistant', 10, y);
      doc.setFont('helvetica', 'normal');
      doc.setFontSize(10);
      doc.setTextColor(120);
      doc.text(
        `${new Date(section.message.createdAt).toLocaleString()}`,
        40,
        y,
      );
      y += 6;
      doc.setTextColor(30);
      doc.setFontSize(12);
      const assistantLines = doc.splitTextToSize(
        section.parsedTextBlocks.join('\n'),
        180,
      );
      for (let i = 0; i < assistantLines.length; i++) {
        if (y > pageHeight - 20) {
          doc.addPage();
          y = 15;
        }
        doc.text(assistantLines[i], 12, y);
        y += 6;
      }

      const sourceResponseBlock = section.message.responseBlocks.find(
        (block) => block.type === 'source',
      ) as SourceBlock | undefined;

      if (
        sourceResponseBlock &&
        sourceResponseBlock.data &&
        sourceResponseBlock.data.length > 0
      ) {
        doc.setFontSize(11);
        doc.setTextColor(80);
        if (y > pageHeight - 20) {
          doc.addPage();
          y = 15;
        }
        doc.text('Citations:', 12, y);
        y += 5;
        sourceResponseBlock.data.forEach((src: any, i: number) => {
          const url = src.metadata?.url || '';
          if (y > pageHeight - 15) {
            doc.addPage();
            y = 15;
          }
          doc.text(`- [${i + 1}] ${url}`, 15, y);
          y += 5;
        });
        doc.setTextColor(30);
      }
      y += 6;
      doc.setDrawColor(230);
      if (y > pageHeight - 10) {
        doc.addPage();
        y = 15;
      }
      doc.line(10, y, 200, y);
      y += 4;
    }
  });
  doc.save(`${title || 'chat'}.pdf`);
};

const Navbar = () => {
  const [title, setTitle] = useState<string>('');
  const [timeAgo, setTimeAgo] = useState<string>('');

  const { sections, chatId } = useChat();

  useEffect(() => {
    if (sections.length > 0 && sections[0].message) {
      const newTitle =
        sections[0].message.query.length > 30
          ? `${sections[0].message.query.substring(0, 30).trim()}...`
          : sections[0].message.query || 'New Conversation';

      setTitle(newTitle);
      const newTimeAgo = formatTimeDifference(
        new Date(),
        sections[0].message.createdAt,
      );
      setTimeAgo(newTimeAgo);
    }
  }, [sections]);

  useEffect(() => {
    const intervalId = setInterval(() => {
      if (sections.length > 0 && sections[0].message) {
        const newTimeAgo = formatTimeDifference(
          new Date(),
          sections[0].message.createdAt,
        );
        setTimeAgo(newTimeAgo);
      }
    }, 1000);

    return () => clearInterval(intervalId);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="sticky -mx-4 lg:mx-0 top-0 z-40 bg-light-primary/95 dark:bg-dark-primary/95 backdrop-blur-sm border-b border-light-200/50 dark:border-dark-200/30">
      <div className="px-4 lg:px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center min-w-0">
            <a
              href="/"
              className="lg:hidden mr-3 p-2 -ml-2 rounded-lg hover:bg-light-secondary dark:hover:bg-dark-secondary transition-colors duration-200"
            >
              <Edit size={18} className="text-black/70 dark:text-white/70" />
            </a>
            <div className="hidden lg:flex items-center gap-2 text-black/50 dark:text-white/50 min-w-0">
              <Clock size={14} />
              <span className="text-xs whitespace-nowrap">{timeAgo} ago</span>
            </div>
          </div>

          <div className="flex-1 mx-4 min-w-0">
            <h1 className="text-center text-sm font-medium text-black/80 dark:text-white/90 truncate">
              {title || 'New Conversation'}
            </h1>
          </div>

          <div className="flex items-center gap-1 min-w-0">
            <Popover className="relative">
              <PopoverButton className="p-2 rounded-lg hover:bg-light-secondary dark:hover:bg-dark-secondary transition-colors duration-200">
                <Share size={16} className="text-black/60 dark:text-white/60" />
              </PopoverButton>
              <Transition
                as={Fragment}
                enter="transition ease-out duration-200"
                enterFrom="opacity-0 translate-y-1"
                enterTo="opacity-100 translate-y-0"
                leave="transition ease-in duration-150"
                leaveFrom="opacity-100 translate-y-0"
                leaveTo="opacity-0 translate-y-1"
              >
                <PopoverPanel className="absolute right-0 mt-2 w-64 origin-top-right rounded-2xl bg-light-primary dark:bg-dark-primary border border-light-200 dark:border-dark-200 shadow-xl shadow-black/10 dark:shadow-black/30 z-50">
                  <div className="p-3">
                    <div className="mb-2">
                      <p className="text-xs font-medium text-black/40 dark:text-white/40 uppercase tracking-wide">
                        Export Chat
                      </p>
                    </div>
                    <div className="space-y-1">
                      <button
                        className="w-full flex items-center gap-3 px-3 py-2 text-left rounded-xl hover:bg-light-secondary dark:hover:bg-dark-secondary transition-colors duration-200"
                        onClick={() => exportAsMarkdown(sections, title || '')}
                      >
                        <FileText size={16} className="text-[#24A0ED]" />
                        <div>
                          <p className="text-sm font-medium text-black dark:text-white">
                            Markdown
                          </p>
                          <p className="text-xs text-black/50 dark:text-white/50">
                            .md format
                          </p>
                        </div>
                      </button>
                      <button
                        className="w-full flex items-center gap-3 px-3 py-2 text-left rounded-xl hover:bg-light-secondary dark:hover:bg-dark-secondary transition-colors duration-200"
                        onClick={() => exportAsPDF(sections, title || '')}
                      >
                        <FileDown size={16} className="text-[#24A0ED]" />
                        <div>
                          <p className="text-sm font-medium text-black dark:text-white">
                            PDF
                          </p>
                          <p className="text-xs text-black/50 dark:text-white/50">
                            Document format
                          </p>
                        </div>
                      </button>
                    </div>
                  </div>
                </PopoverPanel>
              </Transition>
            </Popover>
            <DeleteChat
              redirect
              chatId={chatId!}
              chats={[]}
              setChats={() => {}}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Navbar;
```

## File: `src/components/NewsArticleWidget.tsx`
```tsx
import { useEffect, useState } from 'react';

interface Article {
  title: string;
  content: string;
  url: string;
  thumbnail: string;
}

const NewsArticleWidget = () => {
  const [article, setArticle] = useState<Article | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch('/api/discover?mode=preview')
      .then((res) => res.json())
      .then((data) => {
        const articles = (data.blogs || []).filter((a: Article) => a.thumbnail);
        setArticle(articles[Math.floor(Math.random() * articles.length)]);
        setLoading(false);
      })
      .catch(() => {
        setError(true);
        setLoading(false);
      });
  }, []);

  return (
    <div className="bg-light-secondary dark:bg-dark-secondary rounded-2xl border border-light-200 dark:border-dark-200 shadow-sm shadow-light-200/10 dark:shadow-black/25 flex flex-row items-stretch w-full h-24 min-h-[96px] max-h-[96px] p-0 overflow-hidden">
      {loading ? (
        <div className="animate-pulse flex flex-row items-stretch w-full h-full">
          <div className="w-24 min-w-24 max-w-24 h-full bg-light-200 dark:bg-dark-200" />
          <div className="flex flex-col justify-center flex-1 px-3 py-2 gap-2">
            <div className="h-4 w-3/4 rounded bg-light-200 dark:bg-dark-200" />
            <div className="h-3 w-1/2 rounded bg-light-200 dark:bg-dark-200" />
          </div>
        </div>
      ) : error ? (
        <div className="w-full text-xs text-red-400">Could not load news.</div>
      ) : article ? (
        <a
          href={`/?q=Summary: ${article.url}`}
          className="flex flex-row items-stretch w-full h-full relative overflow-hidden group"
        >
          <div className="relative w-24 min-w-24 max-w-24 h-full overflow-hidden">
            <img
              className="object-cover w-full h-full bg-light-200 dark:bg-dark-200 group-hover:scale-110 transition-transform duration-300"
              src={
                new URL(article.thumbnail).origin +
                new URL(article.thumbnail).pathname +
                `?id=${new URL(article.thumbnail).searchParams.get('id')}`
              }
              alt={article.title}
            />
          </div>
          <div className="flex flex-col justify-center flex-1 px-3 py-2">
            <div className="font-semibold text-xs text-black dark:text-white leading-tight line-clamp-2 mb-1">
              {article.title}
            </div>
            <p className="text-black/60 dark:text-white/60 text-[10px] leading-relaxed line-clamp-2">
              {article.content}
            </p>
          </div>
        </a>
      ) : null}
    </div>
  );
};

export default NewsArticleWidget;
```

## File: `src/components/SearchImages.tsx`
```tsx
/* eslint-disable @next/next/no-img-element */
import { ImagesIcon, PlusIcon } from 'lucide-react';
import { useState } from 'react';
import Lightbox from 'yet-another-react-lightbox';
import 'yet-another-react-lightbox/styles.css';
import { Message } from './ChatWindow';

type Image = {
  url: string;
  img_src: string;
  title: string;
};

const SearchImages = ({
  query,
  chatHistory,
  messageId,
}: {
  query: string;
  chatHistory: [string, string][];
  messageId: string;
}) => {
  const [images, setImages] = useState<Image[] | null>(null);
  const [loading, setLoading] = useState(false);
  const [open, setOpen] = useState(false);
  const [slides, setSlides] = useState<any[]>([]);

  return (
    <>
      {!loading && images === null && (
        <button
          id={`search-images-${messageId}`}
          onClick={async () => {
            setLoading(true);

            const chatModelProvider = localStorage.getItem(
              'chatModelProviderId',
            );
            const chatModel = localStorage.getItem('chatModelKey');

            const res = await fetch(`/api/images`, {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                query: query,
                chatHistory: chatHistory,
                chatModel: {
                  providerId: chatModelProvider,
                  key: chatModel,
                },
              }),
            });

            const data = await res.json();

            const images = data.images ?? [];
            setImages(images);
            setSlides(
              images.map((image: Image) => {
                return {
                  src: image.img_src,
                };
              }),
            );
            setLoading(false);
          }}
          className="border border-dashed border-light-200 dark:border-dark-200 hover:bg-light-200 dark:hover:bg-dark-200 active:scale-95 duration-200 transition px-4 py-2 flex flex-row items-center justify-between rounded-lg dark:text-white text-sm w-full"
        >
          <div className="flex flex-row items-center space-x-2">
            <ImagesIcon size={17} />
            <p>Search images</p>
          </div>
          <PlusIcon className="text-[#24A0ED]" size={17} />
        </button>
      )}
      {loading && (
        <div className="grid grid-cols-2 gap-2">
          {[...Array(4)].map((_, i) => (
            <div
              key={i}
              className="bg-light-secondary dark:bg-dark-secondary h-32 w-full rounded-lg animate-pulse aspect-video object-cover"
            />
          ))}
        </div>
      )}
      {images !== null && images.length > 0 && (
        <>
          <div className="grid grid-cols-2 gap-2">
            {images.length > 4
              ? images.slice(0, 3).map((image, i) => (
                  <img
                    onClick={() => {
                      setOpen(true);
                      setSlides([
                        slides[i],
                        ...slides.slice(0, i),
                        ...slides.slice(i + 1),
                      ]);
                    }}
                    key={i}
                    src={image.img_src}
                    alt={image.title}
                    className="h-full w-full aspect-video object-cover rounded-lg transition duration-200 active:scale-95 hover:scale-[1.02] cursor-zoom-in"
                  />
                ))
              : images.map((image, i) => (
                  <img
                    onClick={() => {
                      setOpen(true);
                      setSlides([
                        slides[i],
                        ...slides.slice(0, i),
                        ...slides.slice(i + 1),
                      ]);
                    }}
                    key={i}
                    src={image.img_src}
                    alt={image.title}
                    className="h-full w-full aspect-video object-cover rounded-lg transition duration-200 active:scale-95 hover:scale-[1.02] cursor-zoom-in"
                  />
                ))}
            {images.length > 4 && (
              <button
                onClick={() => setOpen(true)}
                className="bg-light-100 hover:bg-light-200 dark:bg-dark-100 dark:hover:bg-dark-200 transition duration-200 active:scale-95 hover:scale-[1.02] h-auto w-full rounded-lg flex flex-col justify-between text-white p-2"
              >
                <div className="flex flex-row items-center space-x-1">
                  {images.slice(3, 6).map((image, i) => (
                    <img
                      key={i}
                      src={image.img_src}
                      alt={image.title}
                      className="h-6 w-12 rounded-md lg:h-3 lg:w-6 lg:rounded-sm aspect-video object-cover"
                    />
                  ))}
                </div>
                <p className="text-black/70 dark:text-white/70 text-xs">
                  View {images.length - 3} more
                </p>
              </button>
            )}
          </div>
          <Lightbox open={open} close={() => setOpen(false)} slides={slides} />
        </>
      )}
    </>
  );
};

export default SearchImages;
```

## File: `src/components/SearchVideos.tsx`
```tsx
/* eslint-disable @next/next/no-img-element */
import { PlayCircle, PlayIcon, PlusIcon, VideoIcon } from 'lucide-react';
import { useRef, useState } from 'react';
import Lightbox, { GenericSlide, VideoSlide } from 'yet-another-react-lightbox';
import 'yet-another-react-lightbox/styles.css';
import { Message } from './ChatWindow';

type Video = {
  url: string;
  img_src: string;
  title: string;
  iframe_src: string;
};

declare module 'yet-another-react-lightbox' {
  export interface VideoSlide extends GenericSlide {
    type: 'video-slide';
    src: string;
    iframe_src: string;
  }

  interface SlideTypes {
    'video-slide': VideoSlide;
  }
}

const Searchvideos = ({
  query,
  chatHistory,
  messageId,
}: {
  query: string;
  chatHistory: [string, string][];
  messageId: string;
}) => {
  const [videos, setVideos] = useState<Video[] | null>(null);
  const [loading, setLoading] = useState(false);
  const [open, setOpen] = useState(false);
  const [slides, setSlides] = useState<VideoSlide[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const videoRefs = useRef<(HTMLIFrameElement | null)[]>([]);

  return (
    <>
      {!loading && videos === null && (
        <button
          id={`search-videos-${messageId}`}
          onClick={async () => {
            setLoading(true);

            const chatModelProvider = localStorage.getItem(
              'chatModelProviderId',
            );
            const chatModel = localStorage.getItem('chatModelKey');

            const res = await fetch(`/api/videos`, {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({
                query: query,
                chatHistory: chatHistory,
                chatModel: {
                  providerId: chatModelProvider,
                  key: chatModel,
                },
              }),
            });

            const data = await res.json();

            const videos = data.videos ?? [];
            setVideos(videos);
            setSlides(
              videos.map((video: Video) => {
                return {
                  type: 'video-slide',
                  iframe_src: video.iframe_src,
                  src: video.img_src,
                };
              }),
            );
            setLoading(false);
          }}
          className="border border-dashed border-light-200 dark:border-dark-200 hover:bg-light-200 dark:hover:bg-dark-200 active:scale-95 duration-200 transition px-4 py-2 flex flex-row items-center justify-between rounded-lg dark:text-white text-sm w-full"
        >
          <div className="flex flex-row items-center space-x-2">
            <VideoIcon size={17} />
            <p>Search videos</p>
          </div>
          <PlusIcon className="text-[#24A0ED]" size={17} />
        </button>
      )}
      {loading && (
        <div className="grid grid-cols-2 gap-2">
          {[...Array(4)].map((_, i) => (
            <div
              key={i}
              className="bg-light-secondary dark:bg-dark-secondary h-32 w-full rounded-lg animate-pulse aspect-video object-cover"
            />
          ))}
        </div>
      )}
      {videos !== null && videos.length > 0 && (
        <>
          <div className="grid grid-cols-2 gap-2">
            {videos.length > 4
              ? videos.slice(0, 3).map((video, i) => (
                  <div
                    onClick={() => {
                      setOpen(true);
                      setSlides([
                        slides[i],
                        ...slides.slice(0, i),
                        ...slides.slice(i + 1),
                      ]);
                    }}
                    className="relative transition duration-200 active:scale-95 hover:scale-[1.02] cursor-pointer"
                    key={i}
                  >
                    <img
                      src={video.img_src}
                      alt={video.title}
                      className="relative h-full w-full aspect-video object-cover rounded-lg"
                    />
                    <div className="absolute bg-white/70 dark:bg-black/70 text-black/70 dark:text-white/70 px-2 py-1 flex flex-row items-center space-x-1 bottom-1 right-1 rounded-md">
                      <PlayCircle size={15} />
                      <p className="text-xs">Video</p>
                    </div>
                  </div>
                ))
              : videos.map((video, i) => (
                  <div
                    onClick={() => {
                      setOpen(true);
                      setSlides([
                        slides[i],
                        ...slides.slice(0, i),
                        ...slides.slice(i + 1),
                      ]);
                    }}
                    className="relative transition duration-200 active:scale-95 hover:scale-[1.02] cursor-pointer"
                    key={i}
                  >
                    <img
                      src={video.img_src}
                      alt={video.title}
                      className="relative h-full w-full aspect-video object-cover rounded-lg"
                    />
                    <div className="absolute bg-white/70 dark:bg-black/70 text-black/70 dark:text-white/70 px-2 py-1 flex flex-row items-center space-x-1 bottom-1 right-1 rounded-md">
                      <PlayCircle size={15} />
                      <p className="text-xs">Video</p>
                    </div>
                  </div>
                ))}
            {videos.length > 4 && (
              <button
                onClick={() => setOpen(true)}
                className="bg-light-100 hover:bg-light-200 dark:bg-dark-100 dark:hover:bg-dark-200 transition duration-200 active:scale-95 hover:scale-[1.02] h-auto w-full rounded-lg flex flex-col justify-between text-white p-2"
              >
                <div className="flex flex-row items-center space-x-1">
                  {videos.slice(3, 6).map((video, i) => (
                    <img
                      key={i}
                      src={video.img_src}
                      alt={video.title}
                      className="h-6 w-12 rounded-md lg:h-3 lg:w-6 lg:rounded-sm aspect-video object-cover"
                    />
                  ))}
                </div>
                <p className="text-black/70 dark:text-white/70 text-xs">
                  View {videos.length - 3} more
                </p>
              </button>
            )}
          </div>
          <Lightbox
            open={open}
            close={() => setOpen(false)}
            slides={slides}
            index={currentIndex}
            on={{
              view: ({ index }) => {
                const previousIframe = videoRefs.current[currentIndex];
                if (previousIframe?.contentWindow) {
                  previousIframe.contentWindow.postMessage(
                    '{"event":"command","func":"pauseVideo","args":""}',
                    '*',
                  );
                }

                setCurrentIndex(index);
              },
            }}
            render={{
              slide: ({ slide }) => {
                const index = slides.findIndex((s) => s === slide);
                return slide.type === 'video-slide' ? (
                  <div className="h-full w-full flex flex-row items-center justify-center">
                    <iframe
                      src={`${slide.iframe_src}${slide.iframe_src.includes('?') ? '&' : '?'}enablejsapi=1`}
                      ref={(el) => {
                        if (el) {
                          videoRefs.current[index] = el;
                        }
                      }}
                      className="aspect-video max-h-[95vh] w-[95vw] rounded-2xl md:w-[80vw]"
                      allowFullScreen
                      allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                    />
                  </div>
                ) : null;
              },
            }}
          />
        </>
      )}
    </>
  );
};

export default Searchvideos;
```

## File: `src/components/Sidebar.tsx`
```tsx
'use client';

import { cn } from '@/lib/utils';
import {
  BookOpenText,
  Home,
  Search,
  SquarePen,
  Settings,
  Plus,
  ArrowLeft,
} from 'lucide-react';
import Link from 'next/link';
import { useSelectedLayoutSegments } from 'next/navigation';
import React, { useState, type ReactNode } from 'react';
import Layout from './Layout';
import {
  Description,
  Dialog,
  DialogPanel,
  DialogTitle,
} from '@headlessui/react';
import SettingsButton from './Settings/SettingsButton';

const VerticalIconContainer = ({ children }: { children: ReactNode }) => {
  return <div className="flex flex-col items-center w-full">{children}</div>;
};

const Sidebar = ({ children }: { children: React.ReactNode }) => {
  const segments = useSelectedLayoutSegments();
  const [isOpen, setIsOpen] = useState<boolean>(true);

  const navLinks = [
    {
      icon: Home,
      href: '/',
      active: segments.length === 0 || segments.includes('c'),
      label: 'Home',
    },
    {
      icon: Search,
      href: '/discover',
      active: segments.includes('discover'),
      label: 'Discover',
    },
    {
      icon: BookOpenText,
      href: '/library',
      active: segments.includes('library'),
      label: 'Library',
    },
  ];

  return (
    <div>
      <div className="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-[72px] lg:flex-col border-r border-light-200 dark:border-dark-200">
        <div className="flex grow flex-col items-center justify-between gap-y-5 overflow-y-auto bg-light-secondary dark:bg-dark-secondary px-2 py-8 shadow-sm shadow-light-200/10 dark:shadow-black/25">
          <a
            className="p-2.5 rounded-full bg-light-200 text-black/70 dark:bg-dark-200 dark:text-white/70 hover:opacity-70 hover:scale-105 tansition duration-200"
            href="/"
          >
            <Plus size={19} className="cursor-pointer" />
          </a>
          <VerticalIconContainer>
            {navLinks.map((link, i) => (
              <Link
                key={i}
                href={link.href}
                className={cn(
                  'relative flex flex-col items-center justify-center space-y-0.5 cursor-pointer w-full py-2 rounded-lg',
                  link.active
                    ? 'text-black/70 dark:text-white/70 '
                    : 'text-black/60 dark:text-white/60',
                )}
              >
                <div
                  className={cn(
                    link.active && 'bg-light-200 dark:bg-dark-200',
                    'group rounded-lg hover:bg-light-200 hover:dark:bg-dark-200 transition duration-200',
                  )}
                >
                  <link.icon
                    size={25}
                    className={cn(
                      !link.active && 'group-hover:scale-105',
                      'transition duration:200 m-1.5',
                    )}
                  />
                </div>
                <p
                  className={cn(
                    link.active
                      ? 'text-black/80 dark:text-white/80'
                      : 'text-black/60 dark:text-white/60',
                    'text-[10px]',
                  )}
                >
                  {link.label}
                </p>
              </Link>
            ))}
          </VerticalIconContainer>

          <SettingsButton />
        </div>
      </div>

      <div className="fixed bottom-0 w-full z-50 flex flex-row items-center gap-x-6 bg-light-secondary dark:bg-dark-secondary px-4 py-4 shadow-sm lg:hidden">
        {navLinks.map((link, i) => (
          <Link
            href={link.href}
            key={i}
            className={cn(
              'relative flex flex-col items-center space-y-1 text-center w-full',
              link.active
                ? 'text-black dark:text-white'
                : 'text-black dark:text-white/70',
            )}
          >
            {link.active && (
              <div className="absolute top-0 -mt-4 h-1 w-full rounded-b-lg bg-black dark:bg-white" />
            )}
            <link.icon />
            <p className="text-xs">{link.label}</p>
          </Link>
        ))}
      </div>

      <Layout>{children}</Layout>
    </div>
  );
};

export default Sidebar;
```

## File: `src/components/ThinkBox.tsx`
```tsx
'use client';

import { useEffect, useState } from 'react';
import { ChevronDown, ChevronUp, BrainCircuit } from 'lucide-react';

interface ThinkBoxProps {
  content: string;
  thinkingEnded: boolean;
}

const ThinkBox = ({ content, thinkingEnded }: ThinkBoxProps) => {
  const [isExpanded, setIsExpanded] = useState(true);

  useEffect(() => {
    if (thinkingEnded) {
      setIsExpanded(false);
    } else {
      setIsExpanded(true);
    }
  }, [thinkingEnded]);

  return (
    <div className="my-4 bg-light-secondary/50 dark:bg-dark-secondary/50 rounded-xl border border-light-200 dark:border-dark-200 overflow-hidden">
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="w-full flex items-center justify-between px-4 py-1 text-black/90 dark:text-white/90 hover:bg-light-200 dark:hover:bg-dark-200 transition duration-200"
      >
        <div className="flex items-center space-x-2">
          <BrainCircuit
            size={20}
            className="text-[#9C27B0] dark:text-[#CE93D8]"
          />
          <p className="font-medium text-sm">Thinking Process</p>
        </div>
        {isExpanded ? (
          <ChevronUp size={18} className="text-black/70 dark:text-white/70" />
        ) : (
          <ChevronDown size={18} className="text-black/70 dark:text-white/70" />
        )}
      </button>

      {isExpanded && (
        <div className="px-4 py-3 text-black/80 dark:text-white/80 text-sm border-t border-light-200 dark:border-dark-200 bg-light-100/50 dark:bg-dark-100/50 whitespace-pre-wrap">
          {content}
        </div>
      )}
    </div>
  );
};

export default ThinkBox;
```

## File: `src/components/WeatherWidget.tsx`
```tsx
'use client';

import { Wind } from 'lucide-react';
import { useEffect, useState } from 'react';
import { getApproxLocation } from '@/lib/actions';

const WeatherWidget = () => {
  const [data, setData] = useState({
    temperature: 0,
    condition: '',
    location: '',
    humidity: 0,
    windSpeed: 0,
    icon: '',
    temperatureUnit: 'C',
    windSpeedUnit: 'm/s',
  });

  const [loading, setLoading] = useState(true);

  const getLocation = async (
    callback: (location: {
      latitude: number;
      longitude: number;
      city: string;
    }) => void,
  ) => {
    if (navigator.geolocation) {
      const result = await navigator.permissions.query({
        name: 'geolocation',
      });

      if (result.state === 'granted') {
        navigator.geolocation.getCurrentPosition(async (position) => {
          const res = await fetch(
            `https://api-bdc.io/data/reverse-geocode-client?latitude=${position.coords.latitude}&longitude=${position.coords.longitude}&localityLanguage=en`,
            {
              method: 'GET',
              headers: {
                'Content-Type': 'application/json',
              },
            },
          );

          const data = await res.json();

          callback({
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
            city: data.locality,
          });
        });
      } else if (result.state === 'prompt') {
        callback(await getApproxLocation());
        navigator.geolocation.getCurrentPosition((position) => {});
      } else if (result.state === 'denied') {
        callback(await getApproxLocation());
      }
    } else {
      callback(await getApproxLocation());
    }
  };

  const updateWeather = async () => {
    getLocation(async (location) => {
      const res = await fetch(`/api/weather`, {
        method: 'POST',
        body: JSON.stringify({
          lat: location.latitude,
          lng: location.longitude,
          measureUnit: localStorage.getItem('measureUnit') ?? 'Metric',
        }),
      });

      const data = await res.json();

      if (res.status !== 200) {
        console.error('Error fetching weather data');
        setLoading(false);
        return;
      }

      setData({
        temperature: data.temperature,
        condition: data.condition,
        location: location.city,
        humidity: data.humidity,
        windSpeed: data.windSpeed,
        icon: data.icon,
        temperatureUnit: data.temperatureUnit,
        windSpeedUnit: data.windSpeedUnit,
      });
      setLoading(false);
    });
  };

  useEffect(() => {
    updateWeather();
    const intervalId = setInterval(updateWeather, 30 * 1000);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="bg-light-secondary dark:bg-dark-secondary rounded-2xl border border-light-200 dark:border-dark-200 shadow-sm shadow-light-200/10 dark:shadow-black/25 flex flex-row items-center w-full h-24 min-h-[96px] max-h-[96px] px-3 py-2 gap-3">
      {loading ? (
        <>
          <div className="flex flex-col items-center justify-center w-16 min-w-16 max-w-16 h-full animate-pulse">
            <div className="h-10 w-10 rounded-full bg-light-200 dark:bg-dark-200 mb-2" />
            <div className="h-4 w-10 rounded bg-light-200 dark:bg-dark-200" />
          </div>
          <div className="flex flex-col justify-between flex-1 h-full py-1 animate-pulse">
            <div className="flex flex-row items-center justify-between">
              <div className="h-3 w-20 rounded bg-light-200 dark:bg-dark-200" />
              <div className="h-3 w-12 rounded bg-light-200 dark:bg-dark-200" />
            </div>
            <div className="h-3 w-16 rounded bg-light-200 dark:bg-dark-200 mt-1" />
            <div className="flex flex-row justify-between w-full mt-auto pt-1 border-t border-light-200 dark:border-dark-200">
              <div className="h-3 w-16 rounded bg-light-200 dark:bg-dark-200" />
              <div className="h-3 w-8 rounded bg-light-200 dark:bg-dark-200" />
            </div>
          </div>
        </>
      ) : (
        <>
          <div className="flex flex-col items-center justify-center w-16 min-w-16 max-w-16 h-full">
            <img
              src={`/weather-ico/${data.icon}.svg`}
              alt={data.condition}
              className="h-10 w-auto"
            />
            <span className="text-base font-semibold text-black dark:text-white">
              {data.temperature}°{data.temperatureUnit}
            </span>
          </div>
          <div className="flex flex-col justify-between flex-1 h-full py-2">
            <div className="flex flex-row items-center justify-between">
              <span className="text-sm font-semibold text-black dark:text-white">
                {data.location}
              </span>
              <span className="flex items-center text-xs text-black/60 dark:text-white/60 font-medium">
                <Wind className="w-3 h-3 mr-1" />
                {data.windSpeed} {data.windSpeedUnit}
              </span>
            </div>
            <span className="text-xs text-black/50 dark:text-white/50 italic">
              {data.condition}
            </span>
            <div className="flex flex-row justify-between w-full mt-auto pt-2 border-t border-light-200/50 dark:border-dark-200/50 text-xs text-black/50 dark:text-white/50 font-medium">
              <span>Humidity {data.humidity}%</span>
              <span className="font-semibold text-black/70 dark:text-white/70">
                Now
              </span>
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default WeatherWidget;
```

## File: `src/components/Discover/MajorNewsCard.tsx`
```tsx
import { Discover } from '@/app/discover/page';
import Link from 'next/link';

const MajorNewsCard = ({
  item,
  isLeft = true,
}: {
  item: Discover;
  isLeft?: boolean;
}) => (
  <Link
    href={`/?q=Summary: ${item.url}`}
    className="w-full group flex flex-row items-stretch gap-6 h-60 py-3"
    target="_blank"
  >
    {isLeft ? (
      <>
        <div className="relative w-80 h-full overflow-hidden rounded-2xl flex-shrink-0">
          <img
            className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-500"
            src={
              new URL(item.thumbnail).origin +
              new URL(item.thumbnail).pathname +
              `?id=${new URL(item.thumbnail).searchParams.get('id')}`
            }
            alt={item.title}
          />
        </div>
        <div className="flex flex-col justify-center flex-1 py-4">
          <h2
            className="text-3xl font-light mb-3 leading-tight line-clamp-3 group-hover:text-cyan-500 dark:group-hover:text-cyan-300 transition duration-200"
            style={{ fontFamily: 'PP Editorial, serif' }}
          >
            {item.title}
          </h2>
          <p className="text-black/60 dark:text-white/60 text-base leading-relaxed line-clamp-4">
            {item.content}
          </p>
        </div>
      </>
    ) : (
      <>
        <div className="flex flex-col justify-center flex-1 py-4">
          <h2
            className="text-3xl font-light mb-3 leading-tight line-clamp-3 group-hover:text-cyan-500 dark:group-hover:text-cyan-300 transition duration-200"
            style={{ fontFamily: 'PP Editorial, serif' }}
          >
            {item.title}
          </h2>
          <p className="text-black/60 dark:text-white/60 text-base leading-relaxed line-clamp-4">
            {item.content}
          </p>
        </div>
        <div className="relative w-80 h-full overflow-hidden rounded-2xl flex-shrink-0">
          <img
            className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-500"
            src={
              new URL(item.thumbnail).origin +
              new URL(item.thumbnail).pathname +
              `?id=${new URL(item.thumbnail).searchParams.get('id')}`
            }
            alt={item.title}
          />
        </div>
      </>
    )}
  </Link>
);

export default MajorNewsCard;
```

## File: `src/components/Discover/SmallNewsCard.tsx`
```tsx
import { Discover } from '@/app/discover/page';
import Link from 'next/link';

const SmallNewsCard = ({ item }: { item: Discover }) => (
  <Link
    href={`/?q=Summary: ${item.url}`}
    className="rounded-3xl overflow-hidden bg-light-secondary dark:bg-dark-secondary shadow-sm shadow-light-200/10 dark:shadow-black/25 group flex flex-col"
    target="_blank"
  >
    <div className="relative aspect-video overflow-hidden">
      <img
        className="object-cover w-full h-full group-hover:scale-105 transition-transform duration-300"
        src={
          new URL(item.thumbnail).origin +
          new URL(item.thumbnail).pathname +
          `?id=${new URL(item.thumbnail).searchParams.get('id')}`
        }
        alt={item.title}
      />
    </div>
    <div className="p-4">
      <h3 className="font-semibold text-sm mb-2 leading-tight line-clamp-2 group-hover:text-cyan-500 dark:group-hover:text-cyan-300 transition duration-200">
        {item.title}
      </h3>
      <p className="text-black/60 dark:text-white/60 text-xs leading-relaxed line-clamp-2">
        {item.content}
      </p>
    </div>
  </Link>
);

export default SmallNewsCard;
```

## File: `src/components/MessageActions/Copy.tsx`
```tsx
import { Check, ClipboardList } from 'lucide-react';
import { Message } from '../ChatWindow';
import { useState } from 'react';
import { Section } from '@/lib/hooks/useChat';
import { SourceBlock } from '@/lib/types';

const Copy = ({
  section,
  initialMessage,
}: {
  section: Section;
  initialMessage: string;
}) => {
  const [copied, setCopied] = useState(false);

  return (
    <button
      onClick={() => {
        const sources = section.message.responseBlocks.filter(
          (b) => b.type === 'source' && b.data.length > 0,
        ) as SourceBlock[];

        const contentToCopy = `${initialMessage}${
          sources.length > 0
            ? `\n\nCitations:\n${sources
                .map((source) => source.data)
                .flat()
                .map(
                  (s, i) =>
                    `[${i + 1}] ${s.metadata.url.startsWith('file_id://') ? s.metadata.fileName || 'Uploaded File' : s.metadata.url}`,
                )
                .join(`\n`)}`
            : ''
        }`;

        navigator.clipboard.writeText(contentToCopy);

        setCopied(true);
        setTimeout(() => setCopied(false), 1000);
      }}
      className="p-2 text-black/70 dark:text-white/70 rounded-full hover:bg-light-secondary dark:hover:bg-dark-secondary transition duration-200 hover:text-black dark:hover:text-white"
    >
      {copied ? <Check size={16} /> : <ClipboardList size={16} />}
    </button>
  );
};

export default Copy;
```

## File: `src/components/MessageActions/Rewrite.tsx`
```tsx
import { ArrowLeftRight, Repeat } from 'lucide-react';

const Rewrite = ({
  rewrite,
  messageId,
}: {
  rewrite: (messageId: string) => void;
  messageId: string;
}) => {
  return (
    <button
      onClick={() => rewrite(messageId)}
      className="p-2 text-black/70 dark:text-white/70 rounded-full hover:bg-light-secondary dark:hover:bg-dark-secondary transition duration-200 hover:text-black dark:hover:text-white flex flex-row items-center space-x-1"
    >
      <Repeat size={16} />
    </button>
  );
};
1;
export default Rewrite;
```

## File: `src/components/MessageInputActions/Attach.tsx`
```tsx
import { cn } from '@/lib/utils';
import {
  Popover,
  PopoverButton,
  PopoverPanel,
  Transition,
} from '@headlessui/react';
import {
  CopyPlus,
  File,
  Link,
  LoaderCircle,
  Paperclip,
  Plus,
  Trash,
} from 'lucide-react';
import { Fragment, useRef, useState } from 'react';
import { useChat } from '@/lib/hooks/useChat';
import { AnimatePresence } from 'motion/react';
import { motion } from 'framer-motion';
import { toast } from 'sonner';

const Attach = () => {
  const { files, setFiles, setFileIds, fileIds } = useChat();

  const [loading, setLoading] = useState(false);
  const fileInputRef = useRef<any>();

  const handleChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = e.target.files;

    if (!selectedFiles?.length) {
      return;
    }

    setLoading(true);

    try {
      const data = new FormData();

      for (let i = 0; i < selectedFiles.length; i++) {
        data.append('files', selectedFiles[i]);
      }

      const embeddingModelProvider = localStorage.getItem(
        'embeddingModelProviderId',
      );
      const embeddingModel = localStorage.getItem('embeddingModelKey');

      if (!embeddingModelProvider || !embeddingModel) {
        throw new Error('Please select an embedding model before uploading.');
      }

      data.append('embedding_model_provider_id', embeddingModelProvider);
      data.append('embedding_model_key', embeddingModel);

      const res = await fetch(`/api/uploads`, {
        method: 'POST',
        body: data,
      });

      const resData = await res.json().catch(() => ({}));

      if (!res.ok) {
        throw new Error(resData.message || 'Failed to upload file(s).');
      }

      if (!Array.isArray(resData.files)) {
        throw new Error('Invalid upload response from server.');
      }

      setFiles([...files, ...resData.files]);
      setFileIds([
        ...fileIds,
        ...resData.files.map((file: any) => file.fileId),
      ]);
    } catch (err: any) {
      toast(err?.message || 'Failed to upload file(s).');
    } finally {
      setLoading(false);
      e.target.value = '';
    }
  };

  return loading ? (
    <div className="active:border-none hover:bg-light-200 hover:dark:bg-dark-200 p-2 rounded-lg focus:outline-none text-black/50 dark:text-white/50 transition duration-200">
      <LoaderCircle size={16} className="text-sky-500 animate-spin" />
    </div>
  ) : files.length > 0 ? (
    <Popover className="relative w-full max-w-[15rem] md:max-w-md lg:max-w-lg">
      {({ open }) => (
        <>
          <PopoverButton
            type="button"
            className="active:border-none hover:bg-light-200 hover:dark:bg-dark-200 p-2 rounded-lg focus:outline-none headless-open:text-black dark:headless-open:text-white text-black/50 dark:text-white/50 active:scale-95 transition duration-200 hover:text-black dark:hover:text-white"
          >
            <File size={16} className="text-sky-500" />
          </PopoverButton>
          <AnimatePresence>
            {open && (
              <PopoverPanel
                className="absolute z-10 w-64 md:w-[350px] right-0"
                static
              >
                <motion.div
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ duration: 0.1, ease: 'easeOut' }}
                  className="origin-top-right bg-light-primary dark:bg-dark-primary border rounded-md border-light-200 dark:border-dark-200 w-full max-h-[200px] md:max-h-none overflow-y-auto flex flex-col"
                >
                  <div className="flex flex-row items-center justify-between px-3 py-2">
                    <h4 className="text-black/70 dark:text-white/70 text-sm">
                      Attached files
                    </h4>
                    <div className="flex flex-row items-center space-x-4">
                      <button
                        type="button"
                        onClick={() => fileInputRef.current.click()}
                        className="flex flex-row items-center space-x-1 text-black/70 dark:text-white/70 hover:text-black hover:dark:text-white transition duration-200 focus:outline-none"
                      >
                        <input
                          type="file"
                          onChange={handleChange}
                          ref={fileInputRef}
                          accept=".pdf,.docx,.txt"
                          multiple
                          hidden
                        />
                        <Plus size={16} />
                        <p className="text-xs">Add</p>
                      </button>
                      <button
                        onClick={() => {
                          setFiles([]);
                          setFileIds([]);
                        }}
                        className="flex flex-row items-center space-x-1 text-black/70 dark:text-white/70 hover:text-black hover:dark:text-white transition duration-200 focus:outline-none"
                      >
                        <Trash size={13} />
                        <p className="text-xs">Clear</p>
                      </button>
                    </div>
                  </div>
                  <div className="h-[0.5px] mx-2 bg-white/10" />
                  <div className="flex flex-col items-center">
                    {files.map((file, i) => (
                      <div
                        key={i}
                        className="flex flex-row items-center justify-start w-full space-x-3 p-3"
                      >
                        <div className="bg-light-100 dark:bg-dark-100 flex items-center justify-center w-9 h-9 rounded-md">
                          <File
                            size={16}
                            className="text-black/70 dark:text-white/70"
                          />
                        </div>
                        <p className="text-black/70 dark:text-white/70 text-xs">
                          {file.fileName.length > 25
                            ? file.fileName
                                .replace(/\.\w+$/, '')
                                .substring(0, 25) +
                              '...' +
                              file.fileExtension
                            : file.fileName}
                        </p>
                      </div>
                    ))}
                  </div>
                </motion.div>
              </PopoverPanel>
            )}
          </AnimatePresence>
        </>
      )}
    </Popover>
  ) : (
    <button
      type="button"
      onClick={() => fileInputRef.current.click()}
      className={cn(
        'flex items-center justify-center active:border-none hover:bg-light-200 hover:dark:bg-dark-200 p-2 rounded-lg focus:outline-none headless-open:text-black dark:headless-open:text-white text-black/50 dark:text-white/50 active:scale-95 transition duration-200 hover:text-black dark:hover:text-white',
      )}
    >
      <input
        type="file"
        onChange={handleChange}
        ref={fileInputRef}
        accept=".pdf,.docx,.txt"
        multiple
        hidden
      />
      <Paperclip size={16} />
    </button>
  );
};

export default Attach;
```

## File: `src/components/MessageInputActions/AttachSmall.tsx`
```tsx
import {
  Popover,
  PopoverButton,
  PopoverPanel,
  Transition,
} from '@headlessui/react';
import { File, LoaderCircle, Paperclip, Plus, Trash } from 'lucide-react';
import { Fragment, useRef, useState } from 'react';
import { useChat } from '@/lib/hooks/useChat';
import { AnimatePresence } from 'motion/react';
import { motion } from 'framer-motion';
import { toast } from 'sonner';

const AttachSmall = () => {
  const { files, setFiles, setFileIds, fileIds } = useChat();

  const [loading, setLoading] = useState(false);
  const fileInputRef = useRef<any>();

  const handleChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = e.target.files;

    if (!selectedFiles?.length) {
      return;
    }

    setLoading(true);

    try {
      const data = new FormData();

      for (let i = 0; i < selectedFiles.length; i++) {
        data.append('files', selectedFiles[i]);
      }

      const embeddingModelProvider = localStorage.getItem(
        'embeddingModelProviderId',
      );
      const embeddingModel = localStorage.getItem('embeddingModelKey');

      if (!embeddingModelProvider || !embeddingModel) {
        throw new Error('Please select an embedding model before uploading.');
      }

      data.append('embedding_model_provider_id', embeddingModelProvider);
      data.append('embedding_model_key', embeddingModel);

      const res = await fetch(`/api/uploads`, {
        method: 'POST',
        body: data,
      });

      const resData = await res.json().catch(() => ({}));

      if (!res.ok) {
        throw new Error(resData.message || 'Failed to upload file(s).');
      }

      if (!Array.isArray(resData.files)) {
        throw new Error('Invalid upload response from server.');
      }

      setFiles([...files, ...resData.files]);
      setFileIds([
        ...fileIds,
        ...resData.files.map((file: any) => file.fileId),
      ]);
    } catch (err: any) {
      toast(err?.message || 'Failed to upload file(s).');
    } finally {
      setLoading(false);
      e.target.value = '';
    }
  };

  return loading ? (
    <div className="flex flex-row items-center justify-between space-x-1 p-1 ">
      <LoaderCircle size={20} className="text-sky-500 animate-spin" />
    </div>
  ) : files.length > 0 ? (
    <Popover className="max-w-[15rem] md:max-w-md lg:max-w-lg">
      {({ open }) => (
        <>
          <PopoverButton
            type="button"
            className="flex flex-row items-center justify-between space-x-1 p-1 text-black/50 dark:text-white/50 rounded-xl hover:bg-light-secondary dark:hover:bg-dark-secondary active:scale-95 transition duration-200 hover:text-black dark:hover:text-white"
          >
            <File size={20} className="text-sky-500" />
          </PopoverButton>
          <AnimatePresence>
            {open && (
              <PopoverPanel
                className="absolute z-10 w-64 md:w-[350px] bottom-14"
                static
              >
                <motion.div
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ duration: 0.1, ease: 'easeOut' }}
                  className="origin-bottom-left bg-light-primary dark:bg-dark-primary border rounded-md border-light-200 dark:border-dark-200 w-full max-h-[200px] md:max-h-none overflow-y-auto flex flex-col"
                >
                  <div className="flex flex-row items-center justify-between px-3 py-2">
                    <h4 className="text-black/70 dark:text-white/70 font-medium text-sm">
                      Attached files
                    </h4>
                    <div className="flex flex-row items-center space-x-4">
                      <button
                        type="button"
                        onClick={() => fileInputRef.current.click()}
                        className="flex flex-row items-center space-x-1 text-black/70 dark:text-white/70 hover:text-black hover:dark:text-white transition duration-200"
                      >
                        <input
                          type="file"
                          onChange={handleChange}
                          ref={fileInputRef}
                          accept=".pdf,.docx,.txt"
                          multiple
                          hidden
                        />
                        <Plus size={16} />
                        <p className="text-xs">Add</p>
                      </button>
                      <button
                        onClick={() => {
                          setFiles([]);
                          setFileIds([]);
                        }}
                        className="flex flex-row items-center space-x-1 text-black/70 dark:text-white/70 hover:text-black hover:dark:text-white transition duration-200"
                      >
                        <Trash size={13} />
                        <p className="text-xs">Clear</p>
                      </button>
                    </div>
                  </div>
                  <div className="h-[0.5px] mx-2 bg-white/10" />
                  <div className="flex flex-col items-center">
                    {files.map((file, i) => (
                      <div
                        key={i}
                        className="flex flex-row items-center justify-start w-full space-x-3 p-3"
                      >
                        <div className="bg-light-100 dark:bg-dark-100 flex items-center justify-center w-9 h-9 rounded-md">
                          <File
                            size={16}
                            className="text-black/70 dark:text-white/70"
                          />
                        </div>
                        <p className="text-black/70 dark:text-white/70 text-xs">
                          {file.fileName.length > 25
                            ? file.fileName
                                .replace(/\.\w+$/, '')
                                .substring(0, 25) +
                              '...' +
                              file.fileExtension
                            : file.fileName}
                        </p>
                      </div>
                    ))}
                  </div>
                </motion.div>
              </PopoverPanel>
            )}
          </AnimatePresence>
        </>
      )}
    </Popover>
  ) : (
    <button
      type="button"
      onClick={() => fileInputRef.current.click()}
      className="flex flex-row items-center space-x-1 text-black/50 dark:text-white/50 rounded-xl hover:bg-light-secondary dark:hover:bg-dark-secondary transition duration-200 hover:text-black dark:hover:text-white p-1"
    >
      <input
        type="file"
        onChange={handleChange}
        ref={fileInputRef}
        accept=".pdf,.docx,.txt"
        multiple
        hidden
      />
      <Paperclip size={16} />
    </button>
  );
};

export default AttachSmall;
```

## File: `src/components/MessageInputActions/ChatModelSelector.tsx`
```tsx
'use client';

import { Cpu, Loader2, Search } from 'lucide-react';
import { cn } from '@/lib/utils';
import { Popover, PopoverButton, PopoverPanel } from '@headlessui/react';
import { useEffect, useMemo, useState } from 'react';
import { MinimalProvider } from '@/lib/models/types';
import { useChat } from '@/lib/hooks/useChat';
import { AnimatePresence, motion } from 'motion/react';

const ModelSelector = () => {
  const [providers, setProviders] = useState<MinimalProvider[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');

  const { setChatModelProvider, chatModelProvider } = useChat();

  useEffect(() => {
    const loadProviders = async () => {
      try {
        setIsLoading(true);
        const res = await fetch('/api/providers');

        if (!res.ok) {
          throw new Error('Failed to fetch providers');
        }

        const data: { providers: MinimalProvider[] } = await res.json();
        setProviders(data.providers);
      } catch (error) {
        console.error('Error loading providers:', error);
      } finally {
        setIsLoading(false);
      }
    };

    loadProviders();
  }, []);

  const orderedProviders = useMemo(() => {
    if (!chatModelProvider?.providerId) return providers;

    const currentProviderIndex = providers.findIndex(
      (p) => p.id === chatModelProvider.providerId,
    );

    if (currentProviderIndex === -1) {
      return providers;
    }

    const selectedProvider = providers[currentProviderIndex];
    const remainingProviders = providers.filter(
      (_, index) => index !== currentProviderIndex,
    );

    return [selectedProvider, ...remainingProviders];
  }, [providers, chatModelProvider]);

  const handleModelSelect = (providerId: string, modelKey: string) => {
    setChatModelProvider({ providerId, key: modelKey });
    localStorage.setItem('chatModelProviderId', providerId);
    localStorage.setItem('chatModelKey', modelKey);
  };

  const filteredProviders = orderedProviders
    .map((provider) => ({
      ...provider,
      chatModels: provider.chatModels.filter(
        (model) =>
          model.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
          provider.name.toLowerCase().includes(searchQuery.toLowerCase()),
      ),
    }))
    .filter((provider) => provider.chatModels.length > 0);

  return (
    <Popover className="relative w-full max-w-[15rem] md:max-w-md lg:max-w-lg">
      {({ open }) => (
        <>
          <PopoverButton
            type="button"
            className="active:border-none hover:bg-light-200  hover:dark:bg-dark-200 p-2 rounded-lg focus:outline-none headless-open:text-black dark:headless-open:text-white text-black/50 dark:text-white/50 active:scale-95 transition duration-200 hover:text-black dark:hover:text-white"
          >
            <Cpu size={16} className="text-sky-500" />
          </PopoverButton>
          <AnimatePresence>
            {open && (
              <PopoverPanel
                className="absolute z-10 w-[230px] sm:w-[270px] md:w-[300px] right-0"
                static
              >
                <motion.div
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ duration: 0.1, ease: 'easeOut' }}
                  className="origin-top-right bg-light-primary dark:bg-dark-primary max-h-[300px] sm:max-w-none border rounded-lg border-light-200 dark:border-dark-200 w-full flex flex-col shadow-lg overflow-hidden"
                >
                  <div className="p-2 border-b border-light-200 dark:border-dark-200">
                    <div className="relative">
                      <Search
                        size={16}
                        className="absolute left-3 top-1/2 -translate-y-1/2 text-black/40 dark:text-white/40"
                      />
                      <input
                        type="text"
                        placeholder="Search models..."
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                        className="w-full pl-8 pr-3 py-2 bg-light-secondary dark:bg-dark-secondary rounded-lg placeholder:text-xs placeholder:-translate-y-[1.5px] text-xs text-black dark:text-white placeholder:text-black/40 dark:placeholder:text-white/40 focus:outline-none border border-transparent transition duration-200"
                      />
                    </div>
                  </div>

                  <div className="max-h-[320px] overflow-y-auto">
                    {isLoading ? (
                      <div className="flex items-center justify-center py-16">
                        <Loader2
                          className="animate-spin text-black/40 dark:text-white/40"
                          size={24}
                        />
                      </div>
                    ) : filteredProviders.length === 0 ? (
                      <div className="text-center py-16 px-4 text-black/60 dark:text-white/60 text-sm">
                        {searchQuery
                          ? 'No models found'
                          : 'No chat models configured'}
                      </div>
                    ) : (
                      <div className="flex flex-col">
                        {filteredProviders.map((provider, providerIndex) => (
                          <div key={provider.id}>
                            <div className="px-4 py-2.5 sticky top-0 bg-light-primary dark:bg-dark-primary border-b border-light-200/50 dark:border-dark-200/50">
                              <p className="text-xs text-black/50 dark:text-white/50 uppercase tracking-wider">
                                {provider.name}
                              </p>
                            </div>

                            <div className="flex flex-col px-2 py-2 space-y-0.5">
                              {provider.chatModels.map((model) => (
                                <button
                                  key={model.key}
                                  onClick={() =>
                                    handleModelSelect(provider.id, model.key)
                                  }
                                  type="button"
                                  className={cn(
                                    'px-3 py-2 flex items-center justify-between text-start duration-200 cursor-pointer transition rounded-lg group',
                                    chatModelProvider?.providerId ===
                                      provider.id &&
                                      chatModelProvider?.key === model.key
                                      ? 'bg-light-secondary dark:bg-dark-secondary'
                                      : 'hover:bg-light-secondary dark:hover:bg-dark-secondary',
                                  )}
                                >
                                  <div className="flex items-center space-x-2.5 min-w-0 flex-1">
                                    <Cpu
                                      size={15}
                                      className={cn(
                                        'shrink-0',
                                        chatModelProvider?.providerId ===
                                          provider.id &&
                                          chatModelProvider?.key === model.key
                                          ? 'text-sky-500'
                                          : 'text-black/50 dark:text-white/50 group-hover:text-black/70 group-hover:dark:text-white/70',
                                      )}
                                    />
                                    <p
                                      className={cn(
                                        'text-xs truncate',
                                        chatModelProvider?.providerId ===
                                          provider.id &&
                                          chatModelProvider?.key === model.key
                                          ? 'text-sky-500 font-medium'
                                          : 'text-black/70 dark:text-white/70 group-hover:text-black dark:group-hover:text-white',
                                      )}
                                    >
                                      {model.name}
                                    </p>
                                  </div>
                                </button>
                              ))}
                            </div>

                            {providerIndex < filteredProviders.length - 1 && (
                              <div className="h-px bg-light-200 dark:bg-dark-200" />
                            )}
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                </motion.div>
              </PopoverPanel>
            )}
          </AnimatePresence>
        </>
      )}
    </Popover>
  );
};

export default ModelSelector;
```

## File: `src/components/MessageInputActions/Optimization.tsx`
```tsx
import { ChevronDown, Sliders, Star, Zap } from 'lucide-react';
import { cn } from '@/lib/utils';
import {
  Popover,
  PopoverButton,
  PopoverPanel,
  Transition,
} from '@headlessui/react';
import { Fragment } from 'react';
import { useChat } from '@/lib/hooks/useChat';
import { AnimatePresence, motion } from 'motion/react';

const OptimizationModes = [
  {
    key: 'speed',
    title: 'Speed',
    description: 'Prioritize speed and get the quickest possible answer.',
    icon: <Zap size={16} className="text-[#FF9800]" />,
  },
  {
    key: 'balanced',
    title: 'Balanced',
    description: 'Find the right balance between speed and accuracy',
    icon: <Sliders size={16} className="text-[#4CAF50]" />,
  },
  {
    key: 'quality',
    title: 'Quality',
    description: 'Get the most thorough and accurate answer',
    icon: (
      <Star
        size={16}
        className="text-[#2196F3] dark:text-[#BBDEFB] fill-[#BBDEFB] dark:fill-[#2196F3]"
      />
    ),
  },
];

const Optimization = () => {
  const { optimizationMode, setOptimizationMode } = useChat();

  return (
    <Popover className="relative w-full max-w-[15rem] md:max-w-md lg:max-w-lg">
      {({ open }) => (
        <>
          <PopoverButton
            type="button"
            className="p-2 text-black/50 dark:text-white/50 rounded-xl hover:bg-light-secondary dark:hover:bg-dark-secondary active:scale-95 transition duration-200 hover:text-black dark:hover:text-white focus:outline-none"
          >
            <div className="flex flex-row items-center space-x-1">
              {
                OptimizationModes.find((mode) => mode.key === optimizationMode)
                  ?.icon
              }
              <ChevronDown
                size={16}
                className={cn(
                  open ? 'rotate-180' : 'rotate-0',
                  'transition duration:200',
                )}
              />
            </div>
          </PopoverButton>
          <AnimatePresence>
            {open && (
              <PopoverPanel
                className="absolute z-10 w-64 md:w-[250px] left-0"
                static
              >
                <motion.div
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ duration: 0.1, ease: 'easeOut' }}
                  className="origin-top-left flex flex-col space-y-2 bg-light-primary dark:bg-dark-primary border rounded-lg border-light-200 dark:border-dark-200 w-full p-2 max-h-[200px] md:max-h-none overflow-y-auto"
                >
                  {OptimizationModes.map((mode, i) => (
                    <PopoverButton
                      onClick={() => setOptimizationMode(mode.key)}
                      key={i}
                      className={cn(
                        'p-2 rounded-lg flex flex-col items-start justify-start text-start space-y-1 duration-200 cursor-pointer transition focus:outline-none',
                        optimizationMode === mode.key
                          ? 'bg-light-secondary dark:bg-dark-secondary'
                          : 'hover:bg-light-secondary dark:hover:bg-dark-secondary',
                      )}
                    >
                      <div className="flex flex-row justify-between w-full text-black dark:text-white">
                        <div className="flex flex-row space-x-1">
                          {mode.icon}
                          <p className="text-xs font-medium">{mode.title}</p>
                        </div>
                        {mode.key === 'quality' && (
                          <span className="bg-sky-500/70 dark:bg-sky-500/40 border border-sky-600 px-1 rounded-full text-[10px] text-white">
                            Beta
                          </span>
                        )}
                      </div>
                      <p className="text-black/70 dark:text-white/70 text-xs">
                        {mode.description}
                      </p>
                    </PopoverButton>
                  ))}
                </motion.div>
              </PopoverPanel>
            )}
          </AnimatePresence>
        </>
      )}
    </Popover>
  );
};

export default Optimization;
```

## File: `src/components/MessageInputActions/Sources.tsx`
```tsx
import { useChat } from '@/lib/hooks/useChat';
import {
  Popover,
  PopoverButton,
  PopoverPanel,
  Switch,
} from '@headlessui/react';
import {
  GlobeIcon,
  GraduationCapIcon,
  NetworkIcon,
} from '@phosphor-icons/react';
import { AnimatePresence, motion } from 'motion/react';

const sourcesList = [
  {
    name: 'Web',
    key: 'web',
    icon: <GlobeIcon className="h-[16px] w-auto" />,
  },
  {
    name: 'Academic',
    key: 'academic',
    icon: <GraduationCapIcon className="h-[16px] w-auto" />,
  },
  {
    name: 'Social',
    key: 'discussions',
    icon: <NetworkIcon className="h-[16px] w-auto" />,
  },
];

const Sources = () => {
  const { sources, setSources } = useChat();

  return (
    <Popover className="relative">
      {({ open }) => (
        <>
          <PopoverButton className="flex items-center justify-center active:border-none hover:bg-light-200 hover:dark:bg-dark-200 p-2 rounded-lg focus:outline-none text-black/50 dark:text-white/50 active:scale-95 transition duration-200 hover:text-black dark:hover:text-white">
            <GlobeIcon className="h-[18px] w-auto" />
          </PopoverButton>
          <AnimatePresence>
            {open && (
              <PopoverPanel
                static
                className="absolute z-10 w-64 md:w-[225px] right-0"
              >
                <motion.div
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.9 }}
                  transition={{ duration: 0.1, ease: 'easeOut' }}
                  className="origin-top-right flex flex-col bg-light-primary dark:bg-dark-primary border rounded-lg border-light-200 dark:border-dark-200 w-full p-1 max-h-[200px] md:max-h-none overflow-y-auto shadow-lg"
                >
                  {sourcesList.map((source, i) => (
                    <div
                      key={i}
                      className="flex flex-row justify-between hover:bg-light-100 hover:dark:bg-dark-100 rounded-md py-3 px-2 cursor-pointer"
                      onClick={() => {
                        if (!sources.includes(source.key)) {
                          setSources([...sources, source.key]);
                        } else {
                          setSources(sources.filter((s) => s !== source.key));
                        }
                      }}
                    >
                      <div className="flex flex-row space-x-1.5 text-black/80 dark:text-white/80">
                        {source.icon}
                        <p className="text-xs">{source.name}</p>
                      </div>
                      <Switch
                        checked={sources.includes(source.key)}
                        className="group relative flex h-4 w-7 shrink-0 cursor-pointer rounded-full bg-light-200 dark:bg-white/10 p-0.5 duration-200 ease-in-out focus:outline-none transition-colors disabled:opacity-60 disabled:cursor-not-allowed data-[checked]:bg-sky-500 dark:data-[checked]:bg-sky-500"
                      >
                        <span
                          aria-hidden="true"
                          className="pointer-events-none inline-block size-3 translate-x-[1px] group-data-[checked]:translate-x-3 rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
                        />
                      </Switch>
                    </div>
                  ))}
                </motion.div>
              </PopoverPanel>
            )}
          </AnimatePresence>
        </>
      )}
    </Popover>
  );
};

export default Sources;
```

## File: `src/components/MessageRenderer/Citation.tsx`
```tsx
const Citation = ({
  href,
  children,
}: {
  href: string;
  children: React.ReactNode;
}) => {
  return (
    <a
      href={href}
      target="_blank"
      className="bg-light-secondary dark:bg-dark-secondary px-1 rounded ml-1 no-underline text-xs text-black/70 dark:text-white/70 relative"
    >
      {children}
    </a>
  );
};

export default Citation;
```

## File: `src/components/MessageRenderer/CodeBlock/CodeBlockDarkTheme.ts`
```typescript
import type { CSSProperties } from 'react';

const darkTheme = {
  'hljs-comment': {
    color: '#8b949e',
  },
  'hljs-quote': {
    color: '#8b949e',
  },
  'hljs-variable': {
    color: '#ff7b72',
  },
  'hljs-template-variable': {
    color: '#ff7b72',
  },
  'hljs-tag': {
    color: '#ff7b72',
  },
  'hljs-name': {
    color: '#ff7b72',
  },
  'hljs-selector-id': {
    color: '#ff7b72',
  },
  'hljs-selector-class': {
    color: '#ff7b72',
  },
  'hljs-regexp': {
    color: '#ff7b72',
  },
  'hljs-deletion': {
    color: '#ff7b72',
  },
  'hljs-number': {
    color: '#f2cc60',
  },
  'hljs-built_in': {
    color: '#f2cc60',
  },
  'hljs-builtin-name': {
    color: '#f2cc60',
  },
  'hljs-literal': {
    color: '#f2cc60',
  },
  'hljs-type': {
    color: '#f2cc60',
  },
  'hljs-params': {
    color: '#f2cc60',
  },
  'hljs-meta': {
    color: '#f2cc60',
  },
  'hljs-link': {
    color: '#f2cc60',
  },
  'hljs-attribute': {
    color: '#58a6ff',
  },
  'hljs-string': {
    color: '#7ee787',
  },
  'hljs-symbol': {
    color: '#7ee787',
  },
  'hljs-bullet': {
    color: '#7ee787',
  },
  'hljs-addition': {
    color: '#7ee787',
  },
  'hljs-title': {
    color: '#79c0ff',
  },
  'hljs-section': {
    color: '#79c0ff',
  },
  'hljs-keyword': {
    color: '#c297ff',
  },
  'hljs-selector-tag': {
    color: '#c297ff',
  },
  hljs: {
    display: 'block',
    overflowX: 'auto',
    background: '#0d1117',
    color: '#c9d1d9',
    padding: '0.75em',
    border: '1px solid #21262d',
    borderRadius: '10px',
  },
  'hljs-emphasis': {
    fontStyle: 'italic',
  },
  'hljs-strong': {
    fontWeight: 'bold',
  },
} satisfies Record<string, CSSProperties>;

export default darkTheme;
```

## File: `src/components/MessageRenderer/CodeBlock/CodeBlockLightTheme.ts`
```typescript
import type { CSSProperties } from 'react';

const lightTheme = {
  'hljs-comment': {
    color: '#6e7781',
  },
  'hljs-quote': {
    color: '#6e7781',
  },
  'hljs-variable': {
    color: '#d73a49',
  },
  'hljs-template-variable': {
    color: '#d73a49',
  },
  'hljs-tag': {
    color: '#d73a49',
  },
  'hljs-name': {
    color: '#d73a49',
  },
  'hljs-selector-id': {
    color: '#d73a49',
  },
  'hljs-selector-class': {
    color: '#d73a49',
  },
  'hljs-regexp': {
    color: '#d73a49',
  },
  'hljs-deletion': {
    color: '#d73a49',
  },
  'hljs-number': {
    color: '#b08800',
  },
  'hljs-built_in': {
    color: '#b08800',
  },
  'hljs-builtin-name': {
    color: '#b08800',
  },
  'hljs-literal': {
    color: '#b08800',
  },
  'hljs-type': {
    color: '#b08800',
  },
  'hljs-params': {
    color: '#b08800',
  },
  'hljs-meta': {
    color: '#b08800',
  },
  'hljs-link': {
    color: '#b08800',
  },
  'hljs-attribute': {
    color: '#0a64ae',
  },
  'hljs-string': {
    color: '#22863a',
  },
  'hljs-symbol': {
    color: '#22863a',
  },
  'hljs-bullet': {
    color: '#22863a',
  },
  'hljs-addition': {
    color: '#22863a',
  },
  'hljs-title': {
    color: '#005cc5',
  },
  'hljs-section': {
    color: '#005cc5',
  },
  'hljs-keyword': {
    color: '#6f42c1',
  },
  'hljs-selector-tag': {
    color: '#6f42c1',
  },
  hljs: {
    display: 'block',
    overflowX: 'auto',
    background: '#ffffff',
    color: '#24292f',
    padding: '0.75em',
    border: '1px solid #e8edf1',
    borderRadius: '10px',
  },
  'hljs-emphasis': {
    fontStyle: 'italic',
  },
  'hljs-strong': {
    fontWeight: 'bold',
  },
} satisfies Record<string, CSSProperties>;

export default lightTheme;
```

## File: `src/components/MessageRenderer/CodeBlock/index.tsx`
```tsx
'use client';

import { CheckIcon, CopyIcon } from '@phosphor-icons/react';
import React, { useEffect, useMemo, useState } from 'react';
import { useTheme } from 'next-themes';
import SyntaxHighlighter from 'react-syntax-highlighter';
import darkTheme from './CodeBlockDarkTheme';
import lightTheme from './CodeBlockLightTheme';

const CodeBlock = ({
  language,
  children,
}: {
  language: string;
  children: React.ReactNode;
}) => {
  const { resolvedTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  const [copied, setCopied] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  const syntaxTheme = useMemo(() => {
    if (!mounted) return lightTheme;
    return resolvedTheme === 'dark' ? darkTheme : lightTheme;
  }, [mounted, resolvedTheme]);

  return (
    <div className="relative">
      <button
        className="absolute top-2 right-2 p-1"
        onClick={() => {
          navigator.clipboard.writeText(children as string);
          setCopied(true);
          setTimeout(() => setCopied(false), 2000);
        }}
      >
        {copied ? (
          <CheckIcon
            size={16}
            className="absolute top-2 right-2 text-black/70 dark:text-white/70"
          />
        ) : (
          <CopyIcon
            size={16}
            className="absolute top-2 right-2 transition duration-200 text-black/70 dark:text-white/70 hover:text-gray-800/70 hover:dark:text-gray-300/70"
          />
        )}
      </button>
      <SyntaxHighlighter
        language={language}
        style={syntaxTheme}
        showInlineLineNumbers
      >
        {children as string}
      </SyntaxHighlighter>
    </div>
  );
};

export default CodeBlock;
```

## File: `src/components/Settings/SettingsButton.tsx`
```tsx
import { Settings } from 'lucide-react';
import { useState } from 'react';
import SettingsDialogue from './SettingsDialogue';
import { AnimatePresence } from 'framer-motion';

const SettingsButton = () => {
  const [isOpen, setIsOpen] = useState<boolean>(false);

  return (
    <>
      <div
        className="p-2.5 rounded-full bg-light-200 text-black/70 dark:bg-dark-200 dark:text-white/70 hover:opacity-70 hover:scale-105 transition duration-200 cursor-pointer active:scale-95"
        onClick={() => setIsOpen(true)}
      >
        <Settings size={19} className="cursor-pointer" />
      </div>
      <AnimatePresence>
        {isOpen && <SettingsDialogue isOpen={isOpen} setIsOpen={setIsOpen} />}
      </AnimatePresence>
    </>
  );
};

export default SettingsButton;
```

## File: `src/components/Settings/SettingsButtonMobile.tsx`
```tsx
import { Settings } from 'lucide-react';
import { useState } from 'react';
import SettingsDialogue from './SettingsDialogue';
import { AnimatePresence } from 'framer-motion';

const SettingsButtonMobile = () => {
  const [isOpen, setIsOpen] = useState<boolean>(false);

  return (
    <>
      <button className="lg:hidden" onClick={() => setIsOpen(true)}>
        <Settings size={18} />
      </button>
      <AnimatePresence>
        {isOpen && <SettingsDialogue isOpen={isOpen} setIsOpen={setIsOpen} />}
      </AnimatePresence>
    </>
  );
};

export default SettingsButtonMobile;
```

## File: `src/components/Settings/SettingsDialogue.tsx`
```tsx
import { Dialog, DialogPanel } from '@headlessui/react';
import {
  ArrowLeft,
  BrainCog,
  ChevronLeft,
  ExternalLink,
  Search,
  Sliders,
  ToggleRight,
} from 'lucide-react';
import Preferences from './Sections/Preferences';
import { motion } from 'framer-motion';
import { useEffect, useState } from 'react';
import { toast } from 'sonner';
import Loader from '../ui/Loader';
import { cn } from '@/lib/utils';
import Models from './Sections/Models/Section';
import SearchSection from './Sections/Search';
import Select from '@/components/ui/Select';
import Personalization from './Sections/Personalization';

const sections = [
  {
    key: 'preferences',
    name: 'Preferences',
    description: 'Customize your application preferences.',
    icon: Sliders,
    component: Preferences,
    dataAdd: 'preferences',
  },
  {
    key: 'personalization',
    name: 'Personalization',
    description: 'Customize the behavior and tone of the model.',
    icon: ToggleRight,
    component: Personalization,
    dataAdd: 'personalization',
  },
  {
    key: 'models',
    name: 'Models',
    description: 'Connect to AI services and manage connections.',
    icon: BrainCog,
    component: Models,
    dataAdd: 'modelProviders',
  },
  {
    key: 'search',
    name: 'Search',
    description: 'Manage search settings.',
    icon: Search,
    component: SearchSection,
    dataAdd: 'search',
  },
];

const SettingsDialogue = ({
  isOpen,
  setIsOpen,
}: {
  isOpen: boolean;
  setIsOpen: (active: boolean) => void;
}) => {
  const [isLoading, setIsLoading] = useState(true);
  const [config, setConfig] = useState<any>(null);
  const [activeSection, setActiveSection] = useState<string>(sections[0].key);
  const [selectedSection, setSelectedSection] = useState(sections[0]);

  useEffect(() => {
    setSelectedSection(sections.find((s) => s.key === activeSection)!);
  }, [activeSection]);

  useEffect(() => {
    if (isOpen) {
      const fetchConfig = async () => {
        try {
          const res = await fetch('/api/config', {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
            },
          });

          const data = await res.json();

          setConfig(data);
        } catch (error) {
          console.error('Error fetching config:', error);
          toast.error('Failed to load configuration.');
        } finally {
          setIsLoading(false);
        }
      };

      fetchConfig();
    }
  }, [isOpen]);

  return (
    <Dialog
      open={isOpen}
      onClose={() => setIsOpen(false)}
      className="relative z-50"
    >
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        transition={{ duration: 0.1 }}
        className="fixed inset-0 flex w-screen items-center justify-center p-4 bg-black/30 backdrop-blur-sm h-screen"
      >
        <DialogPanel className="space-y-4 border border-light-200 dark:border-dark-200 bg-light-primary dark:bg-dark-primary backdrop-blur-lg rounded-xl h-[calc(100vh-2%)] w-[calc(100vw-2%)] md:h-[calc(100vh-7%)] md:w-[calc(100vw-7%)] lg:h-[calc(100vh-20%)] lg:w-[calc(100vw-30%)] overflow-hidden flex flex-col">
          {isLoading ? (
            <div className="flex items-center justify-center h-full w-full">
              <Loader />
            </div>
          ) : (
            <div className="flex flex-1 inset-0 h-full overflow-hidden">
              <div className="hidden lg:flex flex-col justify-between w-[240px] border-r border-white-200 dark:border-dark-200 h-full px-3 pt-3 overflow-y-auto">
                <div className="flex flex-col">
                  <button
                    onClick={() => setIsOpen(false)}
                    className="group flex flex-row items-center hover:bg-light-200 hover:dark:bg-dark-200 p-2 rounded-lg"
                  >
                    <ChevronLeft
                      size={18}
                      className="text-black/50 dark:text-white/50 group-hover:text-black/70 group-hover:dark:text-white/70"
                    />
                    <p className="text-black/50 dark:text-white/50 group-hover:text-black/70 group-hover:dark:text-white/70 text-[14px]">
                      Back
                    </p>
                  </button>

                  <div className="flex flex-col items-start space-y-1 mt-8">
                    {sections.map((section) => (
                      <button
                        key={section.dataAdd}
                        className={cn(
                          `flex flex-row items-center space-x-2 px-2 py-1.5 rounded-lg w-full text-sm hover:bg-light-200 hover:dark:bg-dark-200 transition duration-200 active:scale-95`,
                          activeSection === section.key
                            ? 'bg-light-200 dark:bg-dark-200 text-black/90 dark:text-white/90'
                            : ' text-black/70 dark:text-white/70',
                        )}
                        onClick={() => setActiveSection(section.key)}
                      >
                        <section.icon size={17} />
                        <p>{section.name}</p>
                      </button>
                    ))}
                  </div>
                </div>
                <div className="flex flex-col space-y-1 py-[18px] px-2">
                  <p className="text-xs text-black/70 dark:text-white/70">
                    Version: {process.env.NEXT_PUBLIC_VERSION}
                  </p>
                  <a
                    href="https://github.com/itzcrazykns/vane"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-xs text-black/70 dark:text-white/70 flex flex-row space-x-1 items-center transition duration-200 hover:text-black/90 hover:dark:text-white/90"
                  >
                    <span>GitHub</span>
                    <ExternalLink size={12} />
                  </a>
                </div>
              </div>
              <div className="w-full flex flex-col overflow-hidden">
                <div className="flex flex-row lg:hidden w-full justify-between px-[20px] my-4 flex-shrink-0">
                  <button
                    onClick={() => setIsOpen(false)}
                    className="group flex flex-row items-center hover:bg-light-200 hover:dark:bg-dark-200 rounded-lg mr-[40%]"
                  >
                    <ArrowLeft
                      size={18}
                      className="text-black/50 dark:text-white/50 group-hover:text-black/70 group-hover:dark:text-white/70"
                    />
                  </button>
                  <Select
                    options={sections.map((section) => {
                      return {
                        value: section.key,
                        key: section.key,
                        label: section.name,
                      };
                    })}
                    value={activeSection}
                    onChange={(e) => {
                      setActiveSection(e.target.value);
                    }}
                    className="!text-xs lg:!text-sm"
                  />
                </div>
                {selectedSection.component && (
                  <div className="flex flex-1 flex-col overflow-hidden">
                    <div className="border-b border-light-200/60 px-6 pb-6 lg:pt-6 dark:border-dark-200/60 flex-shrink-0">
                      <div className="flex flex-col">
                        <h4 className="font-medium text-black dark:text-white text-sm lg:text-sm">
                          {selectedSection.name}
                        </h4>
                        <p className="text-[11px] lg:text-xs text-black/50 dark:text-white/50">
                          {selectedSection.description}
                        </p>
                      </div>
                    </div>
                    <div className="flex-1 overflow-y-auto">
                      <selectedSection.component
                        fields={config.fields[selectedSection.dataAdd]}
                        values={config.values[selectedSection.dataAdd]}
                      />
                    </div>
                  </div>
                )}
              </div>
            </div>
          )}
        </DialogPanel>
      </motion.div>
    </Dialog>
  );
};

export default SettingsDialogue;
```

## File: `src/components/Settings/SettingsField.tsx`
```tsx
import {
  SelectUIConfigField,
  StringUIConfigField,
  SwitchUIConfigField,
  TextareaUIConfigField,
  UIConfigField,
} from '@/lib/config/types';
import { useState } from 'react';
import Select from '../ui/Select';
import { toast } from 'sonner';
import { useTheme } from 'next-themes';
import { Loader2 } from 'lucide-react';
import { Switch } from '@headlessui/react';

const emitClientConfigChanged = () => {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new Event('client-config-changed'));
  }
};

const SettingsSelect = ({
  field,
  value,
  setValue,
  dataAdd,
}: {
  field: SelectUIConfigField;
  value?: any;
  setValue: (value: any) => void;
  dataAdd: string;
}) => {
  const [loading, setLoading] = useState(false);
  const { setTheme } = useTheme();

  const handleSave = async (newValue: any) => {
    setLoading(true);
    setValue(newValue);
    try {
      if (field.scope === 'client') {
        localStorage.setItem(field.key, newValue);
        if (field.key === 'theme') {
          setTheme(newValue);
        }
        emitClientConfigChanged();
      } else {
        const res = await fetch('/api/config', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            key: `${dataAdd}.${field.key}`,
            value: newValue,
          }),
        });

        if (!res.ok) {
          console.error('Failed to save config:', await res.text());
          throw new Error('Failed to save configuration');
        }
      }
    } catch (error) {
      console.error('Error saving config:', error);
      toast.error('Failed to save configuration.');
    } finally {
      setTimeout(() => setLoading(false), 150);
    }
  };

  return (
    <section className="rounded-xl border border-light-200 bg-light-primary/80 p-4 lg:p-6 transition-colors dark:border-dark-200 dark:bg-dark-primary/80">
      <div className="space-y-3 lg:space-y-5">
        <div>
          <h4 className="text-sm lg:text-sm text-black dark:text-white">
            {field.name}
          </h4>
          <p className="text-[11px] lg:text-xs text-black/50 dark:text-white/50">
            {field.description}
          </p>
        </div>
        <Select
          value={value}
          onChange={(event) => handleSave(event.target.value)}
          options={field.options.map((option) => ({
            value: option.value,
            label: option.name,
          }))}
          className="!text-xs lg:!text-sm"
          loading={loading}
          disabled={loading}
        />
      </div>
    </section>
  );
};

const SettingsInput = ({
  field,
  value,
  setValue,
  dataAdd,
}: {
  field: StringUIConfigField;
  value?: any;
  setValue: (value: any) => void;
  dataAdd: string;
}) => {
  const [loading, setLoading] = useState(false);

  const handleSave = async (newValue: any) => {
    setLoading(true);
    setValue(newValue);
    try {
      if (field.scope === 'client') {
        localStorage.setItem(field.key, newValue);
        emitClientConfigChanged();
      } else {
        const res = await fetch('/api/config', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            key: `${dataAdd}.${field.key}`,
            value: newValue,
          }),
        });

        if (!res.ok) {
          console.error('Failed to save config:', await res.text());
          throw new Error('Failed to save configuration');
        }
      }
    } catch (error) {
      console.error('Error saving config:', error);
      toast.error('Failed to save configuration.');
    } finally {
      setTimeout(() => setLoading(false), 150);
    }
  };

  return (
    <section className="rounded-xl border border-light-200 bg-light-primary/80 p-4 lg:p-6 transition-colors dark:border-dark-200 dark:bg-dark-primary/80">
      <div className="space-y-3 lg:space-y-5">
        <div>
          <h4 className="text-sm lg:text-sm text-black dark:text-white">
            {field.name}
          </h4>
          <p className="text-[11px] lg:text-xs text-black/50 dark:text-white/50">
            {field.description}
          </p>
        </div>
        <div className="relative">
          <input
            value={value ?? field.default ?? ''}
            onChange={(event) => setValue(event.target.value)}
            onBlur={(event) => handleSave(event.target.value)}
            className="w-full rounded-lg border border-light-200 dark:border-dark-200 bg-light-primary dark:bg-dark-primary px-3 py-2 lg:px-4 lg:py-3 pr-10 !text-xs lg:!text-[13px] text-black/80 dark:text-white/80 placeholder:text-black/40 dark:placeholder:text-white/40 focus-visible:outline-none focus-visible:border-light-300 dark:focus-visible:border-dark-300 transition-colors disabled:cursor-not-allowed disabled:opacity-60"
            placeholder={field.placeholder}
            type="text"
            disabled={loading}
          />
          {loading && (
            <span className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-black/40 dark:text-white/40">
              <Loader2 className="h-4 w-4 animate-spin" />
            </span>
          )}
        </div>
      </div>
    </section>
  );
};

const SettingsTextarea = ({
  field,
  value,
  setValue,
  dataAdd,
}: {
  field: TextareaUIConfigField;
  value?: any;
  setValue: (value: any) => void;
  dataAdd: string;
}) => {
  const [loading, setLoading] = useState(false);

  const handleSave = async (newValue: any) => {
    setLoading(true);
    setValue(newValue);
    try {
      if (field.scope === 'client') {
        localStorage.setItem(field.key, newValue);
        emitClientConfigChanged();
      } else {
        const res = await fetch('/api/config', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            key: `${dataAdd}.${field.key}`,
            value: newValue,
          }),
        });

        if (!res.ok) {
          console.error('Failed to save config:', await res.text());
          throw new Error('Failed to save configuration');
        }
      }
    } catch (error) {
      console.error('Error saving config:', error);
      toast.error('Failed to save configuration.');
    } finally {
      setTimeout(() => setLoading(false), 150);
    }
  };

  return (
    <section className="rounded-xl border border-light-200 bg-light-primary/80 p-4 lg:p-6 transition-colors dark:border-dark-200 dark:bg-dark-primary/80">
      <div className="space-y-3 lg:space-y-5">
        <div>
          <h4 className="text-sm lg:text-sm text-black dark:text-white">
            {field.name}
          </h4>
          <p className="text-[11px] lg:text-xs text-black/50 dark:text-white/50">
            {field.description}
          </p>
        </div>
        <div className="relative">
          <textarea
            value={value ?? field.default ?? ''}
            onChange={(event) => setValue(event.target.value)}
            onBlur={(event) => handleSave(event.target.value)}
            className="w-full rounded-lg border border-light-200 dark:border-dark-200 bg-light-primary dark:bg-dark-primary px-3 py-2 lg:px-4 lg:py-3 pr-10 !text-xs lg:!text-[13px] text-black/80 dark:text-white/80 placeholder:text-black/40 dark:placeholder:text-white/40 focus-visible:outline-none focus-visible:border-light-300 dark:focus-visible:border-dark-300 transition-colors disabled:cursor-not-allowed disabled:opacity-60"
            placeholder={field.placeholder}
            rows={4}
            disabled={loading}
          />
          {loading && (
            <span className="pointer-events-none absolute right-3 translate-y-3 text-black/40 dark:text-white/40">
              <Loader2 className="h-4 w-4 animate-spin" />
            </span>
          )}
        </div>
      </div>
    </section>
  );
};

const SettingsSwitch = ({
  field,
  value,
  setValue,
  dataAdd,
}: {
  field: SwitchUIConfigField;
  value?: any;
  setValue: (value: any) => void;
  dataAdd: string;
}) => {
  const [loading, setLoading] = useState(false);

  const handleSave = async (newValue: boolean) => {
    setLoading(true);
    setValue(newValue);
    try {
      if (field.scope === 'client') {
        localStorage.setItem(field.key, String(newValue));
        emitClientConfigChanged();
      } else {
        const res = await fetch('/api/config', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            key: `${dataAdd}.${field.key}`,
            value: newValue,
          }),
        });

        if (!res.ok) {
          console.error('Failed to save config:', await res.text());
          throw new Error('Failed to save configuration');
        }
      }
    } catch (error) {
      console.error('Error saving config:', error);
      toast.error('Failed to save configuration.');
    } finally {
      setTimeout(() => setLoading(false), 150);
    }
  };

  const isChecked = value === true || value === 'true';

  return (
    <section className="rounded-xl border border-light-200 bg-light-primary/80 p-4 lg:p-6 transition-colors dark:border-dark-200 dark:bg-dark-primary/80">
      <div className="flex flex-row items-center space-x-3 lg:space-x-5 w-full justify-between">
        <div>
          <h4 className="text-sm lg:text-sm text-black dark:text-white">
            {field.name}
          </h4>
          <p className="text-[11px] lg:text-xs text-black/50 dark:text-white/50">
            {field.description}
          </p>
        </div>
        <Switch
          checked={isChecked}
          onChange={handleSave}
          disabled={loading}
          className="group relative flex h-6 w-12 shrink-0 cursor-pointer rounded-full bg-light-200 dark:bg-white/10 p-1 duration-200 ease-in-out focus:outline-none transition-colors disabled:opacity-60 disabled:cursor-not-allowed data-[checked]:bg-sky-500 dark:data-[checked]:bg-sky-500"
        >
          <span
            aria-hidden="true"
            className="pointer-events-none inline-block size-4 translate-x-0 rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out group-data-[checked]:translate-x-6"
          />
        </Switch>
      </div>
    </section>
  );
};

const SettingsField = ({
  field,
  value,
  dataAdd,
}: {
  field: UIConfigField;
  value: any;
  dataAdd: string;
}) => {
  const [val, setVal] = useState(value);

  switch (field.type) {
    case 'select':
      return (
        <SettingsSelect
          field={field}
          value={val}
          setValue={setVal}
          dataAdd={dataAdd}
        />
      );
    case 'string':
      return (
        <SettingsInput
          field={field}
          value={val}
          setValue={setVal}
          dataAdd={dataAdd}
        />
      );
    case 'textarea':
      return (
        <SettingsTextarea
          field={field}
          value={val}
          setValue={setVal}
          dataAdd={dataAdd}
        />
      );
    case 'switch':
      return (
        <SettingsSwitch
          field={field}
          value={val}
          setValue={setVal}
          dataAdd={dataAdd}
        />
      );
    default:
      return <div>Unsupported field type: {field.type}</div>;
  }
};

export default SettingsField;
```

## File: `src/components/Settings/Sections/Personalization.tsx`
```tsx
import { UIConfigField } from '@/lib/config/types';
import SettingsField from '../SettingsField';

const Personalization = ({
  fields,
  values,
}: {
  fields: UIConfigField[];
  values: Record<string, any>;
}) => {
  return (
    <div className="flex-1 space-y-6 overflow-y-auto px-6 py-6">
      {fields.map((field) => (
        <SettingsField
          key={field.key}
          field={field}
          value={
            (field.scope === 'client'
              ? localStorage.getItem(field.key)
              : values[field.key]) ?? field.default
          }
          dataAdd="personalization"
        />
      ))}
    </div>
  );
};

export default Personalization;
```

## File: `src/components/Settings/Sections/Preferences.tsx`
```tsx
import { UIConfigField } from '@/lib/config/types';
import SettingsField from '../SettingsField';

const Preferences = ({
  fields,
  values,
}: {
  fields: UIConfigField[];
  values: Record<string, any>;
}) => {
  return (
    <div className="flex-1 space-y-6 overflow-y-auto px-6 py-6">
      {fields.map((field) => (
        <SettingsField
          key={field.key}
          field={field}
          value={
            (field.scope === 'client'
              ? localStorage.getItem(field.key)
              : values[field.key]) ?? field.default
          }
          dataAdd="preferences"
        />
      ))}
    </div>
  );
};

export default Preferences;
```

## File: `src/components/Settings/Sections/Search.tsx`
```tsx
import { UIConfigField } from '@/lib/config/types';
import SettingsField from '../SettingsField';

const Search = ({
  fields,
  values,
}: {
  fields: UIConfigField[];
  values: Record<string, any>;
}) => {
  return (
    <div className="flex-1 space-y-6 overflow-y-auto px-6 py-6">
      {fields.map((field) => (
        <SettingsField
          key={field.key}
          field={field}
          value={
            (field.scope === 'client'
              ? localStorage.getItem(field.key)
              : values[field.key]) ?? field.default
          }
          dataAdd="search"
        />
      ))}
    </div>
  );
};

export default Search;
```

## File: `src/components/Settings/Sections/Models/AddModelDialog.tsx`
```tsx
import { Dialog, DialogPanel } from '@headlessui/react';
import { Loader2, Plus } from 'lucide-react';
import { useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { ConfigModelProvider } from '@/lib/config/types';
import { toast } from 'sonner';

const AddModel = ({
  providerId,
  setProviders,
  type,
}: {
  providerId: string;
  setProviders: React.Dispatch<React.SetStateAction<ConfigModelProvider[]>>;
  type: 'chat' | 'embedding';
}) => {
  const [open, setOpen] = useState(false);
  const [modelName, setModelName] = useState('');
  const [modelKey, setModelKey] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch(`/api/providers/${providerId}/models`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: modelName,
          key: modelKey,
          type: type,
        }),
      });

      if (!res.ok) {
        throw new Error('Failed to add model');
      }

      setProviders((prev) =>
        prev.map((provider) => {
          if (provider.id === providerId) {
            const newModel = { name: modelName, key: modelKey };
            return {
              ...provider,
              chatModels:
                type === 'chat'
                  ? [...provider.chatModels, newModel]
                  : provider.chatModels,
              embeddingModels:
                type === 'embedding'
                  ? [...provider.embeddingModels, newModel]
                  : provider.embeddingModels,
            };
          }
          return provider;
        }),
      );

      toast.success('Model added successfully.');
      setModelName('');
      setModelKey('');
      setOpen(false);
    } catch (error) {
      console.error('Error adding model:', error);
      toast.error('Failed to add model.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <button
        onClick={() => setOpen(true)}
        className="text-xs text-black/70 dark:text-white/70 hover:text-black hover:dark:text-white flex flex-row items-center space-x-1 active:scale-95 transition duration-200"
      >
        <Plus size={12} />
        <span>Add</span>
      </button>
      <AnimatePresence>
        {open && (
          <Dialog
            static
            open={open}
            onClose={() => setOpen(false)}
            className="relative z-[60]"
          >
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.1 }}
              className="fixed inset-0 flex w-screen items-center justify-center p-4 bg-black/30 backdrop-blur-sm"
            >
              <DialogPanel className="w-full mx-4 lg:w-[600px] max-h-[85vh] flex flex-col border bg-light-primary dark:bg-dark-primary border-light-secondary dark:border-dark-secondary rounded-lg">
                <div className="px-6 pt-6 pb-4">
                  <h3 className="text-black/90 dark:text-white/90 font-medium text-sm">
                    Add new {type === 'chat' ? 'chat' : 'embedding'} model
                  </h3>
                </div>
                <div className="border-t border-light-200 dark:border-dark-200" />
                <div className="flex-1 overflow-y-auto px-6 py-4">
                  <form
                    onSubmit={handleSubmit}
                    className="flex flex-col h-full"
                  >
                    <div className="flex flex-col space-y-4 flex-1">
                      <div className="flex flex-col items-start space-y-2">
                        <label className="text-xs text-black/70 dark:text-white/70">
                          Model name*
                        </label>
                        <input
                          value={modelName}
                          onChange={(e) => setModelName(e.target.value)}
                          className="w-full rounded-lg border border-light-200 dark:border-dark-200 bg-light-primary dark:bg-dark-primary px-4 py-3 text-[13px] text-black/80 dark:text-white/80 placeholder:text-black/40 dark:placeholder:text-white/40 focus-visible:outline-none focus-visible:border-light-300 dark:focus-visible:border-dark-300 transition-colors disabled:cursor-not-allowed disabled:opacity-60"
                          placeholder="e.g., GPT-4"
                          type="text"
                          required
                        />
                      </div>
                      <div className="flex flex-col items-start space-y-2">
                        <label className="text-xs text-black/70 dark:text-white/70">
                          Model key*
                        </label>
                        <input
                          value={modelKey}
                          onChange={(e) => setModelKey(e.target.value)}
                          className="w-full rounded-lg border border-light-200 dark:border-dark-200 bg-light-primary dark:bg-dark-primary px-4 py-3 text-[13px] text-black/80 dark:text-white/80 placeholder:text-black/40 dark:placeholder:text-white/40 focus-visible:outline-none focus-visible:border-light-300 dark:focus-visible:border-dark-300 transition-colors disabled:cursor-not-allowed disabled:opacity-60"
                          placeholder="e.g., gpt-4"
                          type="text"
                          required
                        />
                      </div>
                    </div>
                    <div className="border-t border-light-200 dark:border-dark-200 -mx-6 my-4" />
                    <div className="flex justify-end">
                      <button
                        type="submit"
                        disabled={loading}
                        className="px-4 py-2 rounded-lg text-[13px] bg-sky-500 text-white font-medium disabled:opacity-85 hover:opacity-85 active:scale-95 transition duration-200"
                      >
                        {loading ? (
                          <Loader2 className="animate-spin" size={16} />
                        ) : (
                          'Add Model'
                        )}
                      </button>
                    </div>
                  </form>
                </div>
              </DialogPanel>
            </motion.div>
          </Dialog>
        )}
      </AnimatePresence>
    </>
  );
};

export default AddModel;
```

## File: `src/components/Settings/Sections/Models/AddProviderDialog.tsx`
```tsx
import {
  Description,
  Dialog,
  DialogPanel,
  DialogTitle,
} from '@headlessui/react';
import { Loader2, Plus } from 'lucide-react';
import { useMemo, useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import {
  ConfigModelProvider,
  ModelProviderUISection,
  StringUIConfigField,
  UIConfigField,
} from '@/lib/config/types';
import Select from '@/components/ui/Select';
import { toast } from 'sonner';

const AddProvider = ({
  modelProviders,
  setProviders,
}: {
  modelProviders: ModelProviderUISection[];
  setProviders: React.Dispatch<React.SetStateAction<ConfigModelProvider[]>>;
}) => {
  const [open, setOpen] = useState(false);
  const [selectedProvider, setSelectedProvider] = useState<null | string>(
    modelProviders[0]?.key || null,
  );
  const [config, setConfig] = useState<Record<string, any>>({});
  const [name, setName] = useState('');
  const [loading, setLoading] = useState(false);

  const providerConfigMap = useMemo(() => {
    const map: Record<string, { name: string; fields: UIConfigField[] }> = {};

    modelProviders.forEach((p) => {
      map[p.key] = {
        name: p.name,
        fields: p.fields,
      };
    });

    return map;
  }, [modelProviders]);

  const selectedProviderFields = useMemo(() => {
    if (!selectedProvider) return [];
    const providerFields = providerConfigMap[selectedProvider]?.fields || [];
    const config: Record<string, any> = {};

    providerFields.forEach((field) => {
      config[field.key] = field.default || '';
    });

    setConfig(config);

    return providerFields;
  }, [selectedProvider, providerConfigMap]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch('/api/providers', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          type: selectedProvider,
          name: name,
          config: config,
        }),
      });

      if (!res.ok) {
        throw new Error('Failed to add provider');
      }

      const data: ConfigModelProvider = (await res.json()).provider;

      setProviders((prev) => [...prev, data]);

      toast.success('Connection added successfully.');
    } catch (error) {
      console.error('Error adding provider:', error);
      toast.error('Failed to add connection.');
    } finally {
      setLoading(false);
      setOpen(false);
    }
  };

  return (
    <>
      <button
        onClick={() => setOpen(true)}
        className="px-3 md:px-4 py-1.5 md:py-2 rounded-lg text-xs sm:text-xs border border-light-200 dark:border-dark-200 text-black dark:text-white bg-light-secondary/50 dark:bg-dark-secondary/50 hover:bg-light-secondary hover:dark:bg-dark-secondary hover:border-light-300 hover:dark:border-dark-300 flex flex-row items-center space-x-1 active:scale-95 transition duration-200"
      >
        <Plus className="w-3.5 h-3.5 md:w-4 md:h-4" />
        <span>Add Connection</span>
      </button>
      <AnimatePresence>
        {open && (
          <Dialog
            static
            open={open}
            onClose={() => setOpen(false)}
            className="relative z-[60]"
          >
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.1 }}
              className="fixed inset-0 flex w-screen items-center justify-center p-4 bg-black/30 backdrop-blur-sm"
            >
              <DialogPanel className="w-full mx-4 lg:w-[600px] max-h-[85vh] flex flex-col border bg-light-primary dark:bg-dark-primary border-light-secondary dark:border-dark-secondary rounded-lg">
                <form onSubmit={handleSubmit} className="flex flex-col flex-1">
                  <div className="px-6 pt-6 pb-4">
                    <h3 className="text-black/90 dark:text-white/90 font-medium text-sm">
                      Add new connection
                    </h3>
                  </div>
                  <div className="border-t border-light-200 dark:border-dark-200" />
                  <div className="flex-1 overflow-y-auto px-6 py-4">
                    <div className="flex flex-col space-y-4">
                      <div className="flex flex-col items-start space-y-2">
                        <label className="text-xs text-black/70 dark:text-white/70">
                          Select connection type
                        </label>
                        <Select
                          value={selectedProvider ?? ''}
                          onChange={(e) => setSelectedProvider(e.target.value)}
                          options={Object.entries(providerConfigMap).map(
                            ([key, val]) => {
                              return {
                                label: val.name,
                                value: key,
                              };
                            },
                          )}
                        />
                      </div>

                      <div
                        key="name"
                        className="flex flex-col items-start space-y-2"
                      >
                        <label className="text-xs text-black/70 dark:text-white/70">
                          Connection Name*
                        </label>
                        <input
                          value={name}
                          onChange={(e) => setName(e.target.value)}
                          className="w-full rounded-lg border border-light-200 dark:border-dark-200 bg-light-primary dark:bg-dark-primary px-4 py-3 pr-10 text-sm text-black/80 dark:text-white/80 placeholder:text-black/40 dark:placeholder:text-white/40 focus-visible:outline-none focus-visible:border-light-300 dark:focus-visible:border-dark-300 transition-colors disabled:cursor-not-allowed disabled:opacity-60"
                          placeholder={'e.g., My OpenAI Connection'}
                          type="text"
                          required={true}
                        />
                      </div>

                      {selectedProviderFields.map((field: UIConfigField) => (
                        <div
                          key={field.key}
                          className="flex flex-col items-start space-y-2"
                        >
                          <label className="text-xs text-black/70 dark:text-white/70">
                            {field.name}
                            {field.required && '*'}
                          </label>
                          <input
                            value={config[field.key] ?? field.default ?? ''}
                            onChange={(event) =>
                              setConfig((prev) => ({
                                ...prev,
                                [field.key]: event.target.value,
                              }))
                            }
                            className="w-full rounded-lg border border-light-200 dark:border-dark-200 bg-light-primary dark:bg-dark-primary px-4 py-3 pr-10 text-[13px] text-black/80 dark:text-white/80 placeholder:text-black/40 dark:placeholder:text-white/40 focus-visible:outline-none focus-visible:border-light-300 dark:focus-visible:border-dark-300 transition-colors disabled:cursor-not-allowed disabled:opacity-60"
                            placeholder={
                              (field as StringUIConfigField).placeholder
                            }
                            type="text"
                            required={field.required}
                          />
                        </div>
                      ))}
                    </div>
                  </div>
                  <div className="border-t border-light-200 dark:border-dark-200" />
                  <div className="px-6 py-4 flex justify-end">
                    <button
                      type="submit"
                      disabled={loading}
                      className="px-4 py-2 rounded-lg text-[13px] bg-sky-500 text-white font-medium disabled:opacity-85 hover:opacity-85 active:scale-95 transition duration-200"
                    >
                      {loading ? (
                        <Loader2 className="animate-spin" size={16} />
                      ) : (
                        'Add Connection'
                      )}
                    </button>
                  </div>
                </form>
              </DialogPanel>
            </motion.div>
          </Dialog>
        )}
      </AnimatePresence>
    </>
  );
};

export default AddProvider;
```

## File: `src/components/Settings/Sections/Models/DeleteProviderDialog.tsx`
```tsx
import { Dialog, DialogPanel } from '@headlessui/react';
import { Loader2, Trash2 } from 'lucide-react';
import { useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { ConfigModelProvider } from '@/lib/config/types';
import { toast } from 'sonner';

const DeleteProvider = ({
  modelProvider,
  setProviders,
}: {
  modelProvider: ConfigModelProvider;
  setProviders: React.Dispatch<React.SetStateAction<ConfigModelProvider[]>>;
}) => {
  const [open, setOpen] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleDelete = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch(`/api/providers/${modelProvider.id}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!res.ok) {
        throw new Error('Failed to delete provider');
      }

      setProviders((prev) => {
        return prev.filter((p) => p.id !== modelProvider.id);
      });

      toast.success('Connection deleted successfully.');
    } catch (error) {
      console.error('Error deleting provider:', error);
      toast.error('Failed to delete connection.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <button
        onClick={(e) => {
          e.stopPropagation();
          setOpen(true);
        }}
        className="group p-1.5 rounded-md hover:bg-light-200 hover:dark:bg-dark-200 transition-colors group"
        title="Delete connection"
      >
        <Trash2
          size={14}
          className="text-black/60 dark:text-white/60 group-hover:text-red-500 group-hover:dark:text-red-400"
        />
      </button>
      <AnimatePresence>
        {open && (
          <Dialog
            static
            open={open}
            onClose={() => setOpen(false)}
            className="relative z-[60]"
          >
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.1 }}
              className="fixed inset-0 flex w-screen items-center justify-center p-4 bg-black/30 backdrop-blur-sm"
            >
              <DialogPanel className="w-full mx-4 lg:w-[600px] max-h-[85vh] flex flex-col border bg-light-primary dark:bg-dark-primary border-light-secondary dark:border-dark-secondary rounded-lg">
                <div className="px-6 pt-6 pb-4">
                  <h3 className="text-black/90 dark:text-white/90 font-medium">
                    Delete connection
                  </h3>
                </div>
                <div className="border-t border-light-200 dark:border-dark-200" />
                <div className="flex-1 overflow-y-auto px-6 py-4">
                  <p className="text-sm text-black/60 dark:text-white/60">
                    Are you sure you want to delete the connection &quot;
                    {modelProvider.name}&quot;? This action cannot be undone.
                    All associated models will also be removed.
                  </p>
                </div>
                <div className="px-6 py-6 flex justify-end space-x-2">
                  <button
                    disabled={loading}
                    onClick={() => setOpen(false)}
                    className="px-4 py-2 rounded-lg text-sm border border-light-200 dark:border-dark-200 text-black dark:text-white bg-light-secondary/50 dark:bg-dark-secondary/50 hover:bg-light-secondary hover:dark:bg-dark-secondary hover:border-light-300 hover:dark:border-dark-300 flex flex-row items-center space-x-1 active:scale-95 transition duration-200"
                  >
                    Cancel
                  </button>
                  <button
                    disabled={loading}
                    onClick={handleDelete}
                    className="px-4 py-2 rounded-lg text-sm bg-red-500 text-white font-medium disabled:opacity-85 hover:opacity-85 active:scale-95 transition duration-200"
                  >
                    {loading ? (
                      <Loader2 className="animate-spin" size={16} />
                    ) : (
                      'Delete'
                    )}
                  </button>
                </div>
              </DialogPanel>
            </motion.div>
          </Dialog>
        )}
      </AnimatePresence>
    </>
  );
};

export default DeleteProvider;
```

## File: `src/components/Settings/Sections/Models/ModelProvider.tsx`
```tsx
import { UIConfigField, ConfigModelProvider } from '@/lib/config/types';
import { cn } from '@/lib/utils';
import { AnimatePresence, motion } from 'framer-motion';
import { AlertCircle, Plug2, Plus, Pencil, Trash2, X } from 'lucide-react';
import { useState } from 'react';
import { toast } from 'sonner';
import AddModel from './AddModelDialog';
import UpdateProvider from './UpdateProviderDialog';
import DeleteProvider from './DeleteProviderDialog';

const ModelProvider = ({
  modelProvider,
  setProviders,
  fields,
}: {
  modelProvider: ConfigModelProvider;
  fields: UIConfigField[];
  setProviders: React.Dispatch<React.SetStateAction<ConfigModelProvider[]>>;
}) => {
  const [open, setOpen] = useState(true);

  const handleModelDelete = async (
    type: 'chat' | 'embedding',
    modelKey: string,
  ) => {
    try {
      const res = await fetch(`/api/providers/${modelProvider.id}/models`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ key: modelKey, type: type }),
      });

      if (!res.ok) {
        throw new Error('Failed to delete model: ' + (await res.text()));
      }

      setProviders(
        (prev) =>
          prev.map((provider) => {
            if (provider.id === modelProvider.id) {
              return {
                ...provider,
                ...(type === 'chat'
                  ? {
                      chatModels: provider.chatModels.filter(
                        (m) => m.key !== modelKey,
                      ),
                    }
                  : {
                      embeddingModels: provider.embeddingModels.filter(
                        (m) => m.key !== modelKey,
                      ),
                    }),
              };
            }
            return provider;
          }) as ConfigModelProvider[],
      );

      toast.success('Model deleted successfully.');
    } catch (err) {
      console.error('Failed to delete model', err);
      toast.error('Failed to delete model.');
    }
  };

  const modelCount =
    modelProvider.chatModels.filter((m) => m.key !== 'error').length +
    modelProvider.embeddingModels.filter((m) => m.key !== 'error').length;
  const hasError =
    modelProvider.chatModels.some((m) => m.key === 'error') ||
    modelProvider.embeddingModels.some((m) => m.key === 'error');

  return (
    <div
      key={modelProvider.id}
      className="border border-light-200 dark:border-dark-200 rounded-lg overflow-hidden bg-light-primary dark:bg-dark-primary"
    >
      <div className="px-5 py-3.5 flex flex-row justify-between w-full items-center border-b border-light-200 dark:border-dark-200 bg-light-secondary/30 dark:bg-dark-secondary/30">
        <div className="flex items-center gap-2.5">
          <div className="p-1.5 rounded-md bg-sky-500/10 dark:bg-sky-500/10">
            <Plug2 size={14} className="text-sky-500" />
          </div>
          <div className="flex flex-col">
            <p className="text-sm lg:text-sm text-black dark:text-white font-medium">
              {modelProvider.name}
            </p>
            {modelCount > 0 && (
              <p className="text-[10px] lg:text-[11px] text-black/50 dark:text-white/50">
                {modelCount} model{modelCount !== 1 ? 's' : ''} configured
              </p>
            )}
          </div>
        </div>
        <div className="flex flex-row items-center gap-1">
          <UpdateProvider
            fields={fields}
            modelProvider={modelProvider}
            setProviders={setProviders}
          />
          <DeleteProvider
            modelProvider={modelProvider}
            setProviders={setProviders}
          />
        </div>
      </div>
      <div className="flex flex-col gap-y-4 px-5 py-4">
        <div className="flex flex-col gap-y-2">
          <div className="flex flex-row w-full justify-between items-center">
            <p className="text-[11px] lg:text-[11px] font-medium text-black/70 dark:text-white/70 uppercase tracking-wide">
              Chat Models
            </p>
            {!modelProvider.chatModels.some((m) => m.key === 'error') && (
              <AddModel
                providerId={modelProvider.id}
                setProviders={setProviders}
                type="chat"
              />
            )}
          </div>
          <div className="flex flex-col gap-2">
            {modelProvider.chatModels.some((m) => m.key === 'error') ? (
              <div className="flex flex-row items-center gap-2 text-xs lg:text-xs text-red-500 dark:text-red-400 rounded-lg bg-red-50 dark:bg-red-950/20 px-3 py-2 border border-red-200 dark:border-red-900/30">
                <AlertCircle size={16} className="shrink-0" />
                <span className="break-words">
                  {
                    modelProvider.chatModels.find((m) => m.key === 'error')
                      ?.name
                  }
                </span>
              </div>
            ) : modelProvider.chatModels.filter((m) => m.key !== 'error')
                .length === 0 && !hasError ? (
              <div className="flex flex-col items-center justify-center py-4 px-4 rounded-lg border-2 border-dashed border-light-200 dark:border-dark-200 bg-light-secondary/20 dark:bg-dark-secondary/20">
                <p className="text-xs text-black/50 dark:text-white/50 text-center">
                  No chat models configured
                </p>
              </div>
            ) : modelProvider.chatModels.filter((m) => m.key !== 'error')
                .length > 0 ? (
              <div className="flex flex-row flex-wrap gap-2">
                {modelProvider.chatModels.map((model, index) => (
                  <div
                    key={`${modelProvider.id}-chat-${model.key}-${index}`}
                    className="flex flex-row items-center space-x-1.5 text-xs lg:text-xs text-black/70 dark:text-white/70 rounded-lg bg-light-secondary dark:bg-dark-secondary px-3 py-1.5 border border-light-200 dark:border-dark-200"
                  >
                    <span>{model.name}</span>
                    <button
                      onClick={() => {
                        handleModelDelete('chat', model.key);
                      }}
                      className="hover:text-red-500 dark:hover:text-red-400 transition-colors"
                    >
                      <X size={12} />
                    </button>
                  </div>
                ))}
              </div>
            ) : null}
          </div>
        </div>

        <div className="flex flex-col gap-y-2">
          <div className="flex flex-row w-full justify-between items-center">
            <p className="text-[11px] lg:text-[11px] font-medium text-black/70 dark:text-white/70 uppercase tracking-wide">
              Embedding Models
            </p>
            {!modelProvider.embeddingModels.some((m) => m.key === 'error') && (
              <AddModel
                providerId={modelProvider.id}
                setProviders={setProviders}
                type="embedding"
              />
            )}
          </div>
          <div className="flex flex-col gap-2">
            {modelProvider.embeddingModels.some((m) => m.key === 'error') ? (
              <div className="flex flex-row items-center gap-2 text-xs lg:text-xs text-red-500 dark:text-red-400 rounded-lg bg-red-50 dark:bg-red-950/20 px-3 py-2 border border-red-200 dark:border-red-900/30">
                <AlertCircle size={16} className="shrink-0" />
                <span className="break-words">
                  {
                    modelProvider.embeddingModels.find((m) => m.key === 'error')
                      ?.name
                  }
                </span>
              </div>
            ) : modelProvider.embeddingModels.filter((m) => m.key !== 'error')
                .length === 0 && !hasError ? (
              <div className="flex flex-col items-center justify-center py-4 px-4 rounded-lg border-2 border-dashed border-light-200 dark:border-dark-200 bg-light-secondary/20 dark:bg-dark-secondary/20">
                <p className="text-xs text-black/50 dark:text-white/50 text-center">
                  No embedding models configured
                </p>
              </div>
            ) : modelProvider.embeddingModels.filter((m) => m.key !== 'error')
                .length > 0 ? (
              <div className="flex flex-row flex-wrap gap-2">
                {modelProvider.embeddingModels.map((model, index) => (
                  <div
                    key={`${modelProvider.id}-embedding-${model.key}-${index}`}
                    className="flex flex-row items-center space-x-1.5 text-xs lg:text-xs text-black/70 dark:text-white/70 rounded-lg bg-light-secondary dark:bg-dark-secondary px-3 py-1.5 border border-light-200 dark:border-dark-200"
                  >
                    <span>{model.name}</span>
                    <button
                      onClick={() => {
                        handleModelDelete('embedding', model.key);
                      }}
                      className="hover:text-red-500 dark:hover:text-red-400 transition-colors"
                    >
                      <X size={12} />
                    </button>
                  </div>
                ))}
              </div>
            ) : null}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ModelProvider;
```

## File: `src/components/Settings/Sections/Models/ModelSelect.tsx`
```tsx
import Select from '@/components/ui/Select';
import { ConfigModelProvider } from '@/lib/config/types';
import { useChat } from '@/lib/hooks/useChat';
import { useState } from 'react';
import { toast } from 'sonner';

const ModelSelect = ({
  providers,
  type,
}: {
  providers: ConfigModelProvider[];
  type: 'chat' | 'embedding';
}) => {
  const [selectedModel, setSelectedModel] = useState<string>(
    type === 'chat'
      ? `${localStorage.getItem('chatModelProviderId')}/${localStorage.getItem('chatModelKey')}`
      : `${localStorage.getItem('embeddingModelProviderId')}/${localStorage.getItem('embeddingModelKey')}`,
  );
  const [loading, setLoading] = useState(false);
  const { setChatModelProvider, setEmbeddingModelProvider } = useChat();

  const handleSave = async (newValue: string) => {
    setLoading(true);
    setSelectedModel(newValue);

    try {
      if (type === 'chat') {
        const providerId = newValue.split('/')[0];
        const modelKey = newValue.split('/').slice(1).join('/');

        localStorage.setItem('chatModelProviderId', providerId);
        localStorage.setItem('chatModelKey', modelKey);

        setChatModelProvider({
          providerId: providerId,
          key: modelKey,
        });
      } else {
        const providerId = newValue.split('/')[0];
        const modelKey = newValue.split('/').slice(1).join('/');

        localStorage.setItem('embeddingModelProviderId', providerId);
        localStorage.setItem('embeddingModelKey', modelKey);

        setEmbeddingModelProvider({
          providerId: providerId,
          key: modelKey,
        });
      }
    } catch (error) {
      console.error('Error saving config:', error);
      toast.error('Failed to save configuration.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="rounded-xl border border-light-200 bg-light-primary/80 p-4 lg:p-6 transition-colors dark:border-dark-200 dark:bg-dark-primary/80">
      <div className="space-y-3 lg:space-y-5">
        <div>
          <h4 className="text-sm lg:text-sm text-black dark:text-white">
            Select {type === 'chat' ? 'Chat Model' : 'Embedding Model'}
          </h4>
          <p className="text-[11px] lg:text-xs text-black/50 dark:text-white/50">
            {type === 'chat'
              ? 'Choose which model to use for generating responses'
              : 'Choose which model to use for generating embeddings'}
          </p>
        </div>
        <Select
          value={selectedModel}
          onChange={(event) => handleSave(event.target.value)}
          options={
            type === 'chat'
              ? providers.flatMap((provider) =>
                  provider.chatModels.map((model) => ({
                    value: `${provider.id}/${model.key}`,
                    label: `${provider.name} - ${model.name}`,
                  })),
                )
              : providers.flatMap((provider) =>
                  provider.embeddingModels.map((model) => ({
                    value: `${provider.id}/${model.key}`,
                    label: `${provider.name} - ${model.name}`,
                  })),
                )
          }
          className="!text-xs lg:!text-[13px]"
          loading={loading}
          disabled={loading}
        />
      </div>
    </section>
  );
};

export default ModelSelect;
```

## File: `src/components/Settings/Sections/Models/Section.tsx`
```tsx
import React, { useState } from 'react';
import AddProvider from './AddProviderDialog';
import {
  ConfigModelProvider,
  ModelProviderUISection,
  UIConfigField,
} from '@/lib/config/types';
import ModelProvider from './ModelProvider';
import ModelSelect from './ModelSelect';

const Models = ({
  fields,
  values,
}: {
  fields: ModelProviderUISection[];
  values: ConfigModelProvider[];
}) => {
  const [providers, setProviders] = useState<ConfigModelProvider[]>(values);

  return (
    <div className="flex-1 space-y-6 overflow-y-auto py-6">
      <div className="flex flex-col px-6 gap-y-4">
        <h3 className="text-xs lg:text-xs text-black/70 dark:text-white/70">
          Select models
        </h3>
        <ModelSelect
          providers={values.filter((p) =>
            p.chatModels.some((m) => m.key != 'error'),
          )}
          type="chat"
        />
        <ModelSelect
          providers={values.filter((p) =>
            p.embeddingModels.some((m) => m.key != 'error'),
          )}
          type="embedding"
        />
      </div>
      <div className="border-t border-light-200 dark:border-dark-200" />
      <div className="flex flex-row justify-between items-center px-6 ">
        <p className="text-xs lg:text-xs text-black/70 dark:text-white/70">
          Manage connections
        </p>
        <AddProvider modelProviders={fields} setProviders={setProviders} />
      </div>
      <div className="flex flex-col px-6 gap-y-4">
        {providers.length === 0 ? (
          <div className="flex flex-col items-center justify-center py-12 px-4 rounded-lg border-2 border-dashed border-light-200 dark:border-dark-200 bg-light-secondary/10 dark:bg-dark-secondary/10">
            <div className="p-3 rounded-full bg-sky-500/10 dark:bg-sky-500/10 mb-3">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-8 h-8 text-sky-500"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                />
              </svg>
            </div>
            <p className="text-sm font-medium text-black/70 dark:text-white/70 mb-1">
              No connections yet
            </p>
            <p className="text-xs text-black/50 dark:text-white/50 text-center max-w-sm mb-4">
              Add your first connection to start using AI models. Connect to
              OpenAI, Anthropic, Ollama, and more.
            </p>
          </div>
        ) : (
          providers.map((provider) => (
            <ModelProvider
              key={`provider-${provider.id}`}
              fields={
                (fields.find((f) => f.key === provider.type)?.fields ??
                  []) as UIConfigField[]
              }
              modelProvider={provider}
              setProviders={setProviders}
            />
          ))
        )}
      </div>
    </div>
  );
};

export default Models;
```

## File: `src/components/Settings/Sections/Models/UpdateProviderDialog.tsx`
```tsx
import { Dialog, DialogPanel } from '@headlessui/react';
import { Loader2, Pencil } from 'lucide-react';
import { useEffect, useState } from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import {
  ConfigModelProvider,
  StringUIConfigField,
  UIConfigField,
} from '@/lib/config/types';
import { toast } from 'sonner';

const UpdateProvider = ({
  modelProvider,
  fields,
  setProviders,
}: {
  fields: UIConfigField[];
  modelProvider: ConfigModelProvider;
  setProviders: React.Dispatch<React.SetStateAction<ConfigModelProvider[]>>;
}) => {
  const [open, setOpen] = useState(false);
  const [config, setConfig] = useState<Record<string, any>>({});
  const [name, setName] = useState(modelProvider.name);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const config: Record<string, any> = {
      name: modelProvider.name,
    };

    fields.forEach((field) => {
      config[field.key] =
        modelProvider.config[field.key] || field.default || '';
    });

    setConfig(config);
  }, [fields]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch(`/api/providers/${modelProvider.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: name,
          config: config,
        }),
      });

      if (!res.ok) {
        throw new Error('Failed to update provider');
      }

      const data: ConfigModelProvider = (await res.json()).provider;

      setProviders((prev) => {
        return prev.map((p) => {
          if (p.id === modelProvider.id) {
            return data;
          }

          return p;
        });
      });

      toast.success('Connection updated successfully.');
    } catch (error) {
      console.error('Error updating provider:', error);
      toast.error('Failed to update connection.');
    } finally {
      setLoading(false);
      setOpen(false);
    }
  };

  return (
    <>
      <button
        onClick={(e) => {
          e.stopPropagation();
          setOpen(true);
        }}
        className="group p-1.5 rounded-md hover:bg-light-200 hover:dark:bg-dark-200 transition-colors group"
      >
        <Pencil
          size={14}
          className="text-black/60 dark:text-white/60 group-hover:text-black group-hover:dark:text-white"
        />
      </button>
      <AnimatePresence>
        {open && (
          <Dialog
            static
            open={open}
            onClose={() => setOpen(false)}
            className="relative z-[60]"
          >
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.1 }}
              className="fixed inset-0 flex w-screen items-center justify-center p-4 bg-black/30 backdrop-blur-sm"
            >
              <DialogPanel className="w-full mx-4 lg:w-[600px] max-h-[85vh] flex flex-col border bg-light-primary dark:bg-dark-primary border-light-secondary dark:border-dark-secondary rounded-lg">
                <form onSubmit={handleSubmit} className="flex flex-col flex-1">
                  <div className="px-6 pt-6 pb-4">
                    <h3 className="text-black/90 dark:text-white/90 font-medium text-sm">
                      Update connection
                    </h3>
                  </div>
                  <div className="border-t border-light-200 dark:border-dark-200" />
                  <div className="flex-1 overflow-y-auto px-6 py-4">
                    <div className="flex flex-col space-y-4">
                      <div
                        key="name"
                        className="flex flex-col items-start space-y-2"
                      >
                        <label className="text-xs text-black/70 dark:text-white/70">
                          Connection Name*
                        </label>
                        <input
                          value={name}
                          onChange={(event) => setName(event.target.value)}
                          className="w-full rounded-lg border border-light-200 dark:border-dark-200 bg-light-primary dark:bg-dark-primary px-4 py-3 pr-10 text-sm text-black/80 dark:text-white/80 placeholder:text-black/40 dark:placeholder:text-white/40 focus-visible:outline-none focus-visible:border-light-300 dark:focus-visible:border-dark-300 transition-colors disabled:cursor-not-allowed disabled:opacity-60"
                          placeholder={'Connection Name'}
                          type="text"
                          required={true}
                        />
                      </div>

                      {fields.map((field: UIConfigField) => (
                        <div
                          key={field.key}
                          className="flex flex-col items-start space-y-2"
                        >
                          <label className="text-xs text-black/70 dark:text-white/70">
                            {field.name}
                            {field.required && '*'}
                          </label>
                          <input
                            value={config[field.key] ?? field.default ?? ''}
                            onChange={(event) =>
                              setConfig((prev) => ({
                                ...prev,
                                [field.key]: event.target.value,
                              }))
                            }
                            className="w-full rounded-lg border border-light-200 dark:border-dark-200 bg-light-primary dark:bg-dark-primary px-4 py-3 pr-10 text-[13px] text-black/80 dark:text-white/80 placeholder:text-black/40 dark:placeholder:text-white/40 focus-visible:outline-none focus-visible:border-light-300 dark:focus-visible:border-dark-300 transition-colors disabled:cursor-not-allowed disabled:opacity-60"
                            placeholder={
                              (field as StringUIConfigField).placeholder
                            }
                            type="text"
                            required={field.required}
                          />
                        </div>
                      ))}
                    </div>
                  </div>
                  <div className="border-t border-light-200 dark:border-dark-200" />
                  <div className="px-6 py-4 flex justify-end">
                    <button
                      type="submit"
                      disabled={loading}
                      className="px-4 py-2 rounded-lg text-[13px] bg-sky-500 text-white font-medium disabled:opacity-85 hover:opacity-85 active:scale-95 transition duration-200"
                    >
                      {loading ? (
                        <Loader2 className="animate-spin" size={16} />
                      ) : (
                        'Update Connection'
                      )}
                    </button>
                  </div>
                </form>
              </DialogPanel>
            </motion.div>
          </Dialog>
        )}
      </AnimatePresence>
    </>
  );
};

export default UpdateProvider;
```

## File: `src/components/Setup/SetupConfig.tsx`
```tsx
import {
  ConfigModelProvider,
  UIConfigField,
  UIConfigSections,
} from '@/lib/config/types';
import { motion } from 'framer-motion';
import { ArrowLeft, ArrowRight, Check } from 'lucide-react';
import { useEffect, useState } from 'react';
import { toast } from 'sonner';
import AddProvider from '../Settings/Sections/Models/AddProviderDialog';
import ModelProvider from '../Settings/Sections/Models/ModelProvider';
import ModelSelect from '@/components/Settings/Sections/Models/ModelSelect';

const SetupConfig = ({
  configSections,
  setupState,
  setSetupState,
}: {
  configSections: UIConfigSections;
  setupState: number;
  setSetupState: (state: number) => void;
}) => {
  const [providers, setProviders] = useState<ConfigModelProvider[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isFinishing, setIsFinishing] = useState(false);

  useEffect(() => {
    const fetchProviders = async () => {
      try {
        setIsLoading(true);
        const res = await fetch('/api/providers');
        if (!res.ok) throw new Error('Failed to fetch providers');

        const data = await res.json();
        setProviders(data.providers || []);
      } catch (error) {
        console.error('Error fetching providers:', error);
        toast.error('Failed to load providers');
      } finally {
        setIsLoading(false);
      }
    };

    if (setupState === 2) {
      fetchProviders();
    }
  }, [setupState]);

  const handleFinish = async () => {
    try {
      setIsFinishing(true);
      const res = await fetch('/api/config/setup-complete', {
        method: 'POST',
      });

      if (!res.ok) throw new Error('Failed to complete setup');

      window.location.reload();
    } catch (error) {
      console.error('Error completing setup:', error);
      toast.error('Failed to complete setup');
      setIsFinishing(false);
    }
  };

  const visibleProviders = providers.filter(
    (p) => p.name.toLowerCase() !== 'transformers',
  );
  const hasProviders =
    visibleProviders.filter((p) => p.chatModels.length > 0).length > 0;

  return (
    <div className="w-[95vw] md:w-[80vw] lg:w-[65vw] mx-auto px-2 sm:px-4 md:px-6 flex flex-col space-y-6">
      {setupState === 2 && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{
            opacity: 1,
            y: 0,
            transition: { duration: 0.5, delay: 0.1 },
          }}
          className="w-full h-[calc(95vh-80px)] bg-light-primary dark:bg-dark-primary border border-light-200 dark:border-dark-200 rounded-xl shadow-sm flex flex-col overflow-hidden"
        >
          <div className="flex-1 overflow-y-auto px-3 sm:px-4 md:px-6 py-4 md:py-6">
            <div className="flex flex-row justify-between items-center mb-4 md:mb-6 pb-3 md:pb-4 border-b border-light-200 dark:border-dark-200">
              <div>
                <p className="text-xs sm:text-sm font-medium text-black dark:text-white">
                  Manage Connections
                </p>
                <p className="text-[10px] sm:text-xs text-black/50 dark:text-white/50 mt-0.5">
                  Add connections to access AI models
                </p>
              </div>
              <AddProvider
                modelProviders={configSections.modelProviders}
                setProviders={setProviders}
              />
            </div>

            <div className="space-y-3 md:space-y-4">
              {isLoading ? (
                <div className="flex items-center justify-center py-8 md:py-12">
                  <p className="text-xs sm:text-sm text-black/50 dark:text-white/50">
                    Loading providers...
                  </p>
                </div>
              ) : visibleProviders.length === 0 ? (
                <div className="flex flex-col items-center justify-center py-8 md:py-12 text-center">
                  <p className="text-xs sm:text-sm font-medium text-black/70 dark:text-white/70">
                    No connections configured
                  </p>
                  <p className="text-[10px] sm:text-xs text-black/50 dark:text-white/50 mt-1">
                    Click &quot;Add Connection&quot; above to get started
                  </p>
                </div>
              ) : (
                visibleProviders.map((provider) => (
                  <ModelProvider
                    key={`provider-${provider.id}`}
                    fields={
                      (configSections.modelProviders.find(
                        (f) => f.key === provider.type,
                      )?.fields ?? []) as UIConfigField[]
                    }
                    modelProvider={provider}
                    setProviders={setProviders}
                  />
                ))
              )}
            </div>
          </div>
        </motion.div>
      )}

      {setupState === 3 && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{
            opacity: 1,
            y: 0,
            transition: { duration: 0.5, delay: 0.1 },
          }}
          className="w-full h-[calc(95vh-80px)] bg-light-primary dark:bg-dark-primary border border-light-200 dark:border-dark-200 rounded-xl shadow-sm flex flex-col overflow-hidden"
        >
          <div className="flex-1 overflow-y-auto px-3 sm:px-4 md:px-6 py-4 md:py-6">
            <div className="flex flex-row justify-between items-center mb-4 md:mb-6 pb-3 md:pb-4 border-b border-light-200 dark:border-dark-200">
              <div>
                <p className="text-xs sm:text-sm font-medium text-black dark:text-white">
                  Select models
                </p>
                <p className="text-[10px] sm:text-xs text-black/50 dark:text-white/50 mt-0.5">
                  Select models which you wish to use.
                </p>
              </div>
            </div>

            <div className="space-y-3 md:space-y-4">
              <ModelSelect providers={providers} type="chat" />
              <ModelSelect providers={providers} type="embedding" />
            </div>
          </div>
        </motion.div>
      )}

      <div className="flex flex-row items-center justify-between pt-2">
        <a></a>
        {setupState === 2 && (
          <motion.button
            initial={{ opacity: 0, x: 10 }}
            animate={{
              opacity: 1,
              x: 0,
              transition: { duration: 0.5 },
            }}
            onClick={() => {
              setSetupState(3);
            }}
            disabled={!hasProviders || isLoading}
            className="flex flex-row items-center gap-1.5 md:gap-2 px-3 md:px-5 py-2 md:py-2.5 rounded-lg bg-[#24A0ED] text-white hover:bg-[#1e8fd1] active:scale-95 transition-all duration-200 font-medium text-xs sm:text-sm disabled:bg-light-200 dark:disabled:bg-dark-200 disabled:text-black/40 dark:disabled:text-white/40 disabled:cursor-not-allowed disabled:active:scale-100"
          >
            <span>Next</span>
            <ArrowRight className="w-4 h-4 md:w-[18px] md:h-[18px]" />
          </motion.button>
        )}
        {setupState === 3 && (
          <motion.button
            initial={{ opacity: 0, x: 10 }}
            animate={{
              opacity: 1,
              x: 0,
              transition: { duration: 0.5 },
            }}
            onClick={handleFinish}
            disabled={!hasProviders || isLoading || isFinishing}
            className="flex flex-row items-center gap-1.5 md:gap-2 px-3 md:px-5 py-2 md:py-2.5 rounded-lg bg-[#24A0ED] text-white hover:bg-[#1e8fd1] active:scale-95 transition-all duration-200 font-medium text-xs sm:text-sm disabled:bg-light-200 dark:disabled:bg-dark-200 disabled:text-black/40 dark:disabled:text-white/40 disabled:cursor-not-allowed disabled:active:scale-100"
          >
            <span>{isFinishing ? 'Finishing...' : 'Finish'}</span>
            <Check className="w-4 h-4 md:w-[18px] md:h-[18px]" />
          </motion.button>
        )}
      </div>
    </div>
  );
};

export default SetupConfig;
```

## File: `src/components/Setup/SetupWizard.tsx`
```tsx
'use client';

import { useEffect, useState } from 'react';
import { UIConfigSections } from '@/lib/config/types';
import { AnimatePresence, motion } from 'framer-motion';
import SetupConfig from './SetupConfig';

const SetupWizard = ({
  configSections,
}: {
  configSections: UIConfigSections;
}) => {
  const [showWelcome, setShowWelcome] = useState(true);
  const [showSetup, setShowSetup] = useState(false);
  const [setupState, setSetupState] = useState(1);

  const delay = (ms: number) =>
    new Promise((resolve) => setTimeout(resolve, ms));

  useEffect(() => {
    (async () => {
      await delay(2500);
      setShowWelcome(false);
      await delay(600);
      setShowSetup(true);
      setSetupState(1);
      await delay(1500);
      setSetupState(2);
    })();
  }, []);

  return (
    <div className="bg-light-primary dark:bg-dark-primary h-screen w-screen fixed inset-0 overflow-hidden">
      <AnimatePresence>
        {showWelcome && (
          <div className="absolute inset-0 flex items-center justify-center overflow-hidden">
            <motion.div
              className="absolute flex flex-col items-center justify-center h-full"
              initial={{ opacity: 1 }}
              exit={{ opacity: 0, scale: 1.1 }}
              transition={{ duration: 0.6 }}
            >
              <motion.h2
                transition={{ duration: 0.6 }}
                initial={{ opacity: 0, translateY: '30px' }}
                animate={{ opacity: 1, translateY: '0px' }}
                className="text-4xl md:text-6xl xl:text-8xl font-normal font-['Instrument_Serif'] tracking-tight"
              >
                Welcome to
                <span className="text-[#24A0ED] italic font-['PP_Editorial']">
                  Vane
                </span>
              </motion.h2>
              <motion.p
                transition={{ delay: 0.8, duration: 0.7 }}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                className="text-black/70 dark:text-white/70 text-sm md:text-lg xl:text-2xl mt-2"
              >
                <span className="font-light">Web search,</span>{' '}
                <span className="font-light font-['PP_Editorial'] italic">
                  reimagined
                </span>
              </motion.p>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, scale: 0.5 }}
              animate={{
                opacity: 0.2,
                scale: 1,
                transition: { delay: 0.8, duration: 0.7 },
              }}
              exit={{ opacity: 0, scale: 1.1, transition: { duration: 0.6 } }}
              className="bg-[#24A0ED] left-50 translate-x-[-50%] h-[250px] w-[250px] rounded-full relative z-40 blur-[100px]"
            />
          </div>
        )}
        {showSetup && (
          <div className="absolute inset-0 flex items-center justify-center overflow-hidden">
            <AnimatePresence mode="wait">
              {setupState === 1 && (
                <motion.p
                  key="setup-text"
                  transition={{ duration: 0.6 }}
                  initial={{ opacity: 0, translateY: '30px' }}
                  animate={{ opacity: 1, translateY: '0px' }}
                  exit={{
                    opacity: 0,
                    translateY: '-30px',
                    transition: { duration: 0.6 },
                  }}
                  className="text-2xl md:text-4xl xl:text-6xl font-normal font-['Instrument_Serif'] tracking-tight"
                >
                  Let us get
                  <span className="text-[#24A0ED] italic font-['PP_Editorial']">
                    Vane
                  </span>{' '}
                  set up for you
                </motion.p>
              )}
              {setupState > 1 && (
                <motion.div
                  key="setup-config"
                  initial={{ opacity: 0, translateY: '30px' }}
                  animate={{
                    opacity: 1,
                    translateY: '0px',
                    transition: { duration: 0.6 },
                  }}
                >
                  <SetupConfig
                    configSections={configSections}
                    setupState={setupState}
                    setSetupState={setSetupState}
                  />
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default SetupWizard;
```

## File: `src/components/theme/Provider.tsx`
```tsx
'use client';
import { ThemeProvider } from 'next-themes';

const ThemeProviderComponent = ({
  children,
}: {
  children: React.ReactNode;
}) => {
  return (
    <ThemeProvider attribute="class" enableSystem={false} defaultTheme="dark">
      {children}
    </ThemeProvider>
  );
};

export default ThemeProviderComponent;
```

## File: `src/components/theme/Switcher.tsx`
```tsx
'use client';
import { useTheme } from 'next-themes';
import { useCallback, useEffect, useState } from 'react';
import Select from '../ui/Select';

type Theme = 'dark' | 'light' | 'system';

const ThemeSwitcher = ({ className }: { className?: string }) => {
  const [mounted, setMounted] = useState(false);

  const { theme, setTheme } = useTheme();

  const isTheme = useCallback((t: Theme) => t === theme, [theme]);

  const handleThemeSwitch = (theme: Theme) => {
    setTheme(theme);
  };

  useEffect(() => {
    setMounted(true);
  }, []);

  useEffect(() => {
    if (isTheme('system')) {
      const preferDarkScheme = window.matchMedia(
        '(prefers-color-scheme: dark)',
      );

      const detectThemeChange = (event: MediaQueryListEvent) => {
        const theme: Theme = event.matches ? 'dark' : 'light';
        setTheme(theme);
      };

      preferDarkScheme.addEventListener('change', detectThemeChange);

      return () => {
        preferDarkScheme.removeEventListener('change', detectThemeChange);
      };
    }
  }, [isTheme, setTheme, theme]);

  // Avoid Hydration Mismatch
  if (!mounted) {
    return null;
  }

  return (
    <Select
      className={className}
      value={theme}
      onChange={(e) => handleThemeSwitch(e.target.value as Theme)}
      options={[
        { value: 'light', label: 'Light' },
        { value: 'dark', label: 'Dark' },
      ]}
    />
  );
};

export default ThemeSwitcher;
```

## File: `src/components/ui/Loader.tsx`
```tsx
const Loader = () => {
  return (
    <svg
      aria-hidden="true"
      className="w-8 h-8 text-light-200 fill-light-secondary dark:text-[#202020] animate-spin dark:fill-[#ffffff3b]"
      viewBox="0 0 100 101"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M100 50.5908C100.003 78.2051 78.1951 100.003 50.5908 100C22.9765 99.9972 0.997224 78.018 1 50.4037C1.00281 22.7993 22.8108 0.997224 50.4251 1C78.0395 1.00281 100.018 22.8108 100 50.4251ZM9.08164 50.594C9.06312 73.3997 27.7909 92.1272 50.5966 92.1457C73.4023 92.1642 92.1298 73.4365 92.1483 50.6308C92.1669 27.8251 73.4392 9.0973 50.6335 9.07878C27.8278 9.06026 9.10003 27.787 9.08164 50.594Z"
        fill="currentColor"
      />
      <path
        d="M93.9676 39.0409C96.393 38.4037 97.8624 35.9116 96.9801 33.5533C95.1945 28.8227 92.871 24.3692 90.0681 20.348C85.6237 14.1775 79.4473 9.36872 72.0454 6.45794C64.6435 3.54717 56.3134 2.65431 48.3133 3.89319C45.869 4.27179 44.3768 6.77534 45.014 9.20079C45.6512 11.6262 48.1343 13.0956 50.5786 12.717C56.5073 11.8281 62.5542 12.5399 68.0406 14.7911C73.527 17.0422 78.2187 20.7487 81.5841 25.4923C83.7976 28.5886 85.4467 32.059 86.4416 35.7474C87.1273 38.1189 89.5423 39.6781 91.9676 39.0409Z"
        fill="currentFill"
      />
    </svg>
  );
};

export default Loader;
```

## File: `src/components/ui/Select.tsx`
```tsx
import { cn } from '@/lib/utils';
import { Loader2, ChevronDown } from 'lucide-react';
import { SelectHTMLAttributes, forwardRef } from 'react';

interface SelectProps extends SelectHTMLAttributes<HTMLSelectElement> {
  options: { value: any; label: string; disabled?: boolean }[];
  loading?: boolean;
}

export const Select = forwardRef<HTMLSelectElement, SelectProps>(
  ({ className, options, loading = false, disabled, ...restProps }, ref) => {
    return (
      <div
        className={cn(
          'relative inline-flex w-full items-center',
          disabled && 'opacity-60',
        )}
      >
        <select
          {...restProps}
          ref={ref}
          disabled={disabled || loading}
          className={cn(
            'bg-light-secondary dark:bg-dark-secondary px-3 py-2 flex items-center overflow-hidden border border-light-200 dark:border-dark-200 dark:text-white rounded-lg appearance-none w-full pr-10 text-xs lg:text-sm',
            className,
          )}
        >
          {options.map(({ label, value, disabled: optionDisabled }) => {
            return (
              <option key={value} value={value} disabled={optionDisabled}>
                {label}
              </option>
            );
          })}
        </select>
        <span className="pointer-events-none absolute right-3 flex h-4 w-4 items-center justify-center text-black/50 dark:text-white/60">
          {loading ? (
            <Loader2 className="h-4 w-4 animate-spin" />
          ) : (
            <ChevronDown className="h-4 w-4" />
          )}
        </span>
      </div>
    );
  },
);

Select.displayName = 'Select';

export default Select;
```

## File: `src/components/Widgets/Calculation.tsx`
```tsx
'use client';

import { Calculator, Equal } from 'lucide-react';

type CalculationWidgetProps = {
  expression: string;
  result: number;
};

const Calculation = ({ expression, result }: CalculationWidgetProps) => {
  return (
    <div className="rounded-lg border border-light-200 dark:border-dark-200">
      <div className="p-4 space-y-4">
        <div className="space-y-2">
          <div className="flex items-center gap-2 text-black/60 dark:text-white/70">
            <Calculator className="w-4 h-4" />
            <span className="text-xs uppercase font-semibold tracking-wide">
              Expression
            </span>
          </div>
          <div className="rounded-lg border border-light-200 dark:border-dark-200 bg-light-secondary dark:bg-dark-secondary p-3">
            <code className="text-sm text-black dark:text-white font-mono break-all">
              {expression}
            </code>
          </div>
        </div>

        <div className="space-y-2">
          <div className="flex items-center gap-2 text-black/60 dark:text-white/70">
            <Equal className="w-4 h-4" />
            <span className="text-xs uppercase font-semibold tracking-wide">
              Result
            </span>
          </div>
          <div className="rounded-xl border border-light-200 dark:border-dark-200 bg-light-secondary dark:bg-dark-secondary p-5">
            <div className="text-4xl font-bold text-black dark:text-white font-mono tabular-nums">
              {result.toLocaleString()}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Calculation;
```

## File: `src/components/Widgets/Renderer.tsx`
```tsx
import React from 'react';
import { Widget } from '../ChatWindow';
import Weather from './Weather';
import Calculation from './Calculation';
import Stock from './Stock';

const Renderer = ({ widgets }: { widgets: Widget[] }) => {
  return widgets.map((widget, index) => {
    switch (widget.widgetType) {
      case 'weather':
        return (
          <Weather
            key={index}
            location={widget.params.location}
            current={widget.params.current}
            daily={widget.params.daily}
            timezone={widget.params.timezone}
          />
        );
      case 'calculation_result':
        return (
          <Calculation
            expression={widget.params.expression}
            result={widget.params.result}
            key={index}
          />
        );
      case 'stock':
        return (
          <Stock
            key={index}
            symbol={widget.params.symbol}
            shortName={widget.params.shortName}
            longName={widget.params.longName}
            exchange={widget.params.exchange}
            currency={widget.params.currency}
            marketState={widget.params.marketState}
            regularMarketPrice={widget.params.regularMarketPrice}
            regularMarketChange={widget.params.regularMarketChange}
            regularMarketChangePercent={
              widget.params.regularMarketChangePercent
            }
            regularMarketPreviousClose={
              widget.params.regularMarketPreviousClose
            }
            regularMarketOpen={widget.params.regularMarketOpen}
            regularMarketDayHigh={widget.params.regularMarketDayHigh}
            regularMarketDayLow={widget.params.regularMarketDayLow}
            regularMarketVolume={widget.params.regularMarketVolume}
            averageDailyVolume3Month={widget.params.averageDailyVolume3Month}
            marketCap={widget.params.marketCap}
            fiftyTwoWeekLow={widget.params.fiftyTwoWeekLow}
            fiftyTwoWeekHigh={widget.params.fiftyTwoWeekHigh}
            trailingPE={widget.params.trailingPE}
            forwardPE={widget.params.forwardPE}
            dividendYield={widget.params.dividendYield}
            earningsPerShare={widget.params.earningsPerShare}
            website={widget.params.website}
            postMarketPrice={widget.params.postMarketPrice}
            postMarketChange={widget.params.postMarketChange}
            postMarketChangePercent={widget.params.postMarketChangePercent}
            preMarketPrice={widget.params.preMarketPrice}
            preMarketChange={widget.params.preMarketChange}
            preMarketChangePercent={widget.params.preMarketChangePercent}
            chartData={widget.params.chartData}
            comparisonData={widget.params.comparisonData}
            error={widget.params.error}
          />
        );
      default:
        return <div key={index}>Unknown widget type: {widget.widgetType}</div>;
    }
  });
};

export default Renderer;
```

## File: `src/components/Widgets/Stock.tsx`
```tsx
'use client';

import { Clock, ArrowUpRight, ArrowDownRight, Minus } from 'lucide-react';
import { useEffect, useRef, useState } from 'react';
import {
  createChart,
  ColorType,
  LineStyle,
  BaselineSeries,
  LineSeries,
} from 'lightweight-charts';

type StockWidgetProps = {
  symbol: string;
  shortName: string;
  longName?: string;
  exchange?: string;
  currency?: string;
  marketState?: string;
  regularMarketPrice?: number;
  regularMarketChange?: number;
  regularMarketChangePercent?: number;
  regularMarketPreviousClose?: number;
  regularMarketOpen?: number;
  regularMarketDayHigh?: number;
  regularMarketDayLow?: number;
  regularMarketVolume?: number;
  averageDailyVolume3Month?: number;
  marketCap?: number;
  fiftyTwoWeekLow?: number;
  fiftyTwoWeekHigh?: number;
  trailingPE?: number;
  forwardPE?: number;
  dividendYield?: number;
  earningsPerShare?: number;
  website?: string;
  postMarketPrice?: number;
  postMarketChange?: number;
  postMarketChangePercent?: number;
  preMarketPrice?: number;
  preMarketChange?: number;
  preMarketChangePercent?: number;
  chartData?: {
    '1D'?: { timestamps: number[]; prices: number[] } | null;
    '5D'?: { timestamps: number[]; prices: number[] } | null;
    '1M'?: { timestamps: number[]; prices: number[] } | null;
    '3M'?: { timestamps: number[]; prices: number[] } | null;
    '6M'?: { timestamps: number[]; prices: number[] } | null;
    '1Y'?: { timestamps: number[]; prices: number[] } | null;
    MAX?: { timestamps: number[]; prices: number[] } | null;
  } | null;
  comparisonData?: Array<{
    ticker: string;
    name: string;
    chartData: {
      '1D'?: { timestamps: number[]; prices: number[] } | null;
      '5D'?: { timestamps: number[]; prices: number[] } | null;
      '1M'?: { timestamps: number[]; prices: number[] } | null;
      '3M'?: { timestamps: number[]; prices: number[] } | null;
      '6M'?: { timestamps: number[]; prices: number[] } | null;
      '1Y'?: { timestamps: number[]; prices: number[] } | null;
      MAX?: { timestamps: number[]; prices: number[] } | null;
    };
  }> | null;
  error?: string;
};

const formatNumber = (num: number | undefined, decimals = 2): string => {
  if (num === undefined || num === null) return 'N/A';
  return num.toLocaleString(undefined, {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
};

const formatLargeNumber = (num: number | undefined): string => {
  if (num === undefined || num === null) return 'N/A';
  if (num >= 1e12) return `$${(num / 1e12).toFixed(2)}T`;
  if (num >= 1e9) return `$${(num / 1e9).toFixed(2)}B`;
  if (num >= 1e6) return `$${(num / 1e6).toFixed(2)}M`;
  if (num >= 1e3) return `$${(num / 1e3).toFixed(2)}K`;
  return `$${num.toFixed(2)}`;
};

const Stock = (props: StockWidgetProps) => {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [selectedTimeframe, setSelectedTimeframe] = useState<
    '1D' | '5D' | '1M' | '3M' | '6M' | '1Y' | 'MAX'
  >('1M');
  const chartContainerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const checkDarkMode = () => {
      setIsDarkMode(document.documentElement.classList.contains('dark'));
    };

    checkDarkMode();

    const observer = new MutationObserver(checkDarkMode);
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class'],
    });

    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const currentChartData = props.chartData?.[selectedTimeframe];
    if (
      !chartContainerRef.current ||
      !currentChartData ||
      currentChartData.timestamps.length === 0
    ) {
      return;
    }

    const chart = createChart(chartContainerRef.current, {
      width: chartContainerRef.current.clientWidth,
      height: 280,
      layout: {
        background: { type: ColorType.Solid, color: 'transparent' },
        textColor: isDarkMode ? '#6b7280' : '#9ca3af',
        fontSize: 11,
        attributionLogo: false,
      },
      grid: {
        vertLines: {
          color: isDarkMode ? '#21262d' : '#e8edf1',
          style: LineStyle.Solid,
        },
        horzLines: {
          color: isDarkMode ? '#21262d' : '#e8edf1',
          style: LineStyle.Solid,
        },
      },
      crosshair: {
        vertLine: {
          color: isDarkMode ? '#30363d' : '#d0d7de',
          labelVisible: false,
        },
        horzLine: {
          color: isDarkMode ? '#30363d' : '#d0d7de',
          labelVisible: true,
        },
      },
      rightPriceScale: {
        borderVisible: false,
        visible: false,
      },
      leftPriceScale: {
        borderVisible: false,
        visible: true,
      },
      timeScale: {
        borderVisible: false,
        timeVisible: false,
      },
      handleScroll: false,
      handleScale: false,
    });

    const prices = currentChartData.prices;
    let baselinePrice: number;

    if (selectedTimeframe === '1D') {
      baselinePrice = props.regularMarketPreviousClose ?? prices[0];
    } else {
      baselinePrice = prices[0];
    }

    const baselineSeries = chart.addSeries(BaselineSeries);

    baselineSeries.applyOptions({
      baseValue: { type: 'price', price: baselinePrice },
      topLineColor: isDarkMode ? '#14b8a6' : '#0d9488',
      topFillColor1: isDarkMode
        ? 'rgba(20, 184, 166, 0.28)'
        : 'rgba(13, 148, 136, 0.24)',
      topFillColor2: isDarkMode
        ? 'rgba(20, 184, 166, 0.05)'
        : 'rgba(13, 148, 136, 0.05)',
      bottomLineColor: isDarkMode ? '#f87171' : '#dc2626',
      bottomFillColor1: isDarkMode
        ? 'rgba(248, 113, 113, 0.05)'
        : 'rgba(220, 38, 38, 0.05)',
      bottomFillColor2: isDarkMode
        ? 'rgba(248, 113, 113, 0.28)'
        : 'rgba(220, 38, 38, 0.24)',
      lineWidth: 2,
      crosshairMarkerVisible: true,
      crosshairMarkerRadius: 4,
      crosshairMarkerBorderColor: '',
      crosshairMarkerBackgroundColor: '',
    });

    const data = currentChartData.timestamps.map((timestamp, index) => {
      const price = currentChartData.prices[index];
      return {
        time: (timestamp / 1000) as any,
        value: price,
      };
    });

    baselineSeries.setData(data);

    const comparisonColors = ['#8b5cf6', '#f59e0b', '#ec4899'];
    if (props.comparisonData && props.comparisonData.length > 0) {
      props.comparisonData.forEach((comp, index) => {
        const compChartData = comp.chartData[selectedTimeframe];
        if (compChartData && compChartData.prices.length > 0) {
          const compData = compChartData.timestamps.map((timestamp, i) => ({
            time: (timestamp / 1000) as any,
            value: compChartData.prices[i],
          }));

          const compSeries = chart.addSeries(LineSeries);
          compSeries.applyOptions({
            color: comparisonColors[index] || '#6b7280',
            lineWidth: 2,
            crosshairMarkerVisible: true,
            crosshairMarkerRadius: 4,
            priceScaleId: 'left',
          });
          compSeries.setData(compData);
        }
      });
    }

    chart.timeScale().fitContent();

    const handleResize = () => {
      if (chartContainerRef.current) {
        chart.applyOptions({
          width: chartContainerRef.current.clientWidth,
        });
      }
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      chart.remove();
    };
  }, [
    props.chartData,
    props.comparisonData,
    selectedTimeframe,
    isDarkMode,
    props.regularMarketPreviousClose,
  ]);

  const isPositive = (props.regularMarketChange ?? 0) >= 0;
  const isMarketOpen = props.marketState === 'REGULAR';
  const isPreMarket = props.marketState === 'PRE';
  const isPostMarket = props.marketState === 'POST';

  const displayPrice = isPostMarket
    ? props.postMarketPrice ?? props.regularMarketPrice
    : isPreMarket
      ? props.preMarketPrice ?? props.regularMarketPrice
      : props.regularMarketPrice;

  const displayChange = isPostMarket
    ? props.postMarketChange ?? props.regularMarketChange
    : isPreMarket
      ? props.preMarketChange ?? props.regularMarketChange
      : props.regularMarketChange;

  const displayChangePercent = isPostMarket
    ? props.postMarketChangePercent ?? props.regularMarketChangePercent
    : isPreMarket
      ? props.preMarketChangePercent ?? props.regularMarketChangePercent
      : props.regularMarketChangePercent;

  const changeColor = isPositive
    ? 'text-green-600 dark:text-green-400'
    : 'text-red-600 dark:text-red-400';

  if (props.error) {
    return (
      <div className="rounded-lg bg-light-secondary dark:bg-dark-secondary border border-light-200 dark:border-dark-200 p-4">
        <p className="text-sm text-black dark:text-white">
          Error: {props.error}
        </p>
      </div>
    );
  }

  return (
    <div className="rounded-lg border border-light-200 dark:border-dark-200 overflow-hidden">
      <div className="p-4 space-y-4">
        <div className="flex items-start justify-between gap-4 pb-4 border-b border-light-200 dark:border-dark-200">
          <div className="flex-1">
            <div className="flex items-center gap-2 mb-1">
              {props.website && (
                <img
                  src={`https://logo.clearbit.com/${new URL(props.website).hostname}`}
                  alt={`${props.symbol} logo`}
                  className="w-8 h-8 rounded-lg"
                  onError={(e) => {
                    (e.target as HTMLImageElement).style.display = 'none';
                  }}
                />
              )}
              <h3 className="text-2xl font-bold text-black dark:text-white">
                {props.symbol}
              </h3>
              {props.exchange && (
                <span className="px-2 py-0.5 text-xs font-medium rounded bg-light-100 dark:bg-dark-100 text-black/60 dark:text-white/60">
                  {props.exchange}
                </span>
              )}
              {isMarketOpen && (
                <div className="flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-green-100 dark:bg-green-950/40 border border-green-300 dark:border-green-800">
                  <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse" />
                  <span className="text-xs font-medium text-green-700 dark:text-green-400">
                    Live
                  </span>
                </div>
              )}
              {isPreMarket && (
                <div className="flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-blue-100 dark:bg-blue-950/40 border border-blue-300 dark:border-blue-800">
                  <Clock className="w-3 h-3 text-blue-600 dark:text-blue-400" />
                  <span className="text-xs font-medium text-blue-700 dark:text-blue-400">
                    Pre-Market
                  </span>
                </div>
              )}
              {isPostMarket && (
                <div className="flex items-center gap-1.5 px-2 py-0.5 rounded-full bg-orange-100 dark:bg-orange-950/40 border border-orange-300 dark:border-orange-800">
                  <Clock className="w-3 h-3 text-orange-600 dark:text-orange-400" />
                  <span className="text-xs font-medium text-orange-700 dark:text-orange-400">
                    After Hours
                  </span>
                </div>
              )}
            </div>
            <p className="text-sm text-black/60 dark:text-white/60">
              {props.longName || props.shortName}
            </p>
          </div>

          <div className="text-right">
            <div className="flex items-baseline gap-2 mb-1">
              <span className="text-3xl font-medium text-black dark:text-white">
                {props.currency === 'USD' ? '$' : ''}
                {formatNumber(displayPrice)}
              </span>
            </div>
            <div
              className={`flex items-center justify-end gap-1 ${changeColor}`}
            >
              {isPositive ? (
                <ArrowUpRight className="w-4 h-4" />
              ) : displayChange === 0 ? (
                <Minus className="w-4 h-4" />
              ) : (
                <ArrowDownRight className="w-4 h-4" />
              )}
              <span className="text-lg font-normal">
                {displayChange !== undefined && displayChange >= 0 ? '+' : ''}
                {formatNumber(displayChange)}
              </span>
              <span className="text-sm font-normal">
                (
                {displayChangePercent !== undefined && displayChangePercent >= 0
                  ? '+'
                  : ''}
                {formatNumber(displayChangePercent)}%)
              </span>
            </div>
          </div>
        </div>

        {props.chartData && (
          <div className="bg-light-secondary dark:bg-dark-secondary rounded-lg overflow-hidden">
            <div className="flex items-center justify-between p-3 border-b border-light-200 dark:border-dark-200">
              <div className="flex items-center gap-1">
                {(['1D', '5D', '1M', '3M', '6M', '1Y', 'MAX'] as const).map(
                  (timeframe) => (
                    <button
                      key={timeframe}
                      onClick={() => setSelectedTimeframe(timeframe)}
                      disabled={!props.chartData?.[timeframe]}
                      className={`px-3 py-1.5 text-xs font-medium rounded transition-colors ${
                        selectedTimeframe === timeframe
                          ? 'bg-black/10 dark:bg-white/10 text-black dark:text-white'
                          : 'text-black/50 dark:text-white/50 hover:text-black/80 dark:hover:text-white/80'
                      } disabled:opacity-30 disabled:cursor-not-allowed`}
                    >
                      {timeframe}
                    </button>
                  ),
                )}
              </div>

              {props.comparisonData && props.comparisonData.length > 0 && (
                <div className="flex items-center gap-3 ml-auto">
                  <span className="text-xs text-black/50 dark:text-white/50">
                    {props.symbol}
                  </span>
                  {props.comparisonData.map((comp, index) => {
                    const colors = ['#8b5cf6', '#f59e0b', '#ec4899'];
                    return (
                      <div
                        key={comp.ticker}
                        className="flex items-center gap-1.5"
                      >
                        <div
                          className="w-2 h-2 rounded-full"
                          style={{ backgroundColor: colors[index] }}
                        />
                        <span className="text-xs text-black/70 dark:text-white/70">
                          {comp.ticker}
                        </span>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>

            <div className="p-4">
              <div ref={chartContainerRef} />
            </div>

            <div className="grid grid-cols-3 border-t border-light-200 dark:border-dark-200">
              <div className="flex justify-between p-3 border-r border-light-200 dark:border-dark-200">
                <span className="text-xs text-black/50 dark:text-white/50">
                  Prev Close
                </span>
                <span className="text-xs text-black dark:text-white font-medium">
                  ${formatNumber(props.regularMarketPreviousClose)}
                </span>
              </div>
              <div className="flex justify-between p-3 border-r border-light-200 dark:border-dark-200">
                <span className="text-xs text-black/50 dark:text-white/50">
                  52W Range
                </span>
                <span className="text-xs text-black dark:text-white font-medium">
                  ${formatNumber(props.fiftyTwoWeekLow, 2)}-$
                  {formatNumber(props.fiftyTwoWeekHigh, 2)}
                </span>
              </div>
              <div className="flex justify-between p-3">
                <span className="text-xs text-black/50 dark:text-white/50">
                  Market Cap
                </span>
                <span className="text-xs text-black dark:text-white font-medium">
                  {formatLargeNumber(props.marketCap)}
                </span>
              </div>
              <div className="flex justify-between p-3 border-t border-r border-light-200 dark:border-dark-200">
                <span className="text-xs text-black/50 dark:text-white/50">
                  Open
                </span>
                <span className="text-xs text-black dark:text-white font-medium">
                  ${formatNumber(props.regularMarketOpen)}
                </span>
              </div>
              <div className="flex justify-between p-3 border-t border-r border-light-200 dark:border-dark-200">
                <span className="text-xs text-black/50 dark:text-white/50">
                  P/E Ratio
                </span>
                <span className="text-xs text-black dark:text-white font-medium">
                  {props.trailingPE ? formatNumber(props.trailingPE, 2) : 'N/A'}
                </span>
              </div>
              <div className="flex justify-between p-3 border-t border-light-200 dark:border-dark-200">
                <span className="text-xs text-black/50 dark:text-white/50">
                  Dividend Yield
                </span>
                <span className="text-xs text-black dark:text-white font-medium">
                  {props.dividendYield
                    ? `${formatNumber(props.dividendYield * 100, 2)}%`
                    : 'N/A'}
                </span>
              </div>
              <div className="flex justify-between p-3 border-t border-r border-light-200 dark:border-dark-200">
                <span className="text-xs text-black/50 dark:text-white/50">
                  Day Range
                </span>
                <span className="text-xs text-black dark:text-white font-medium">
                  ${formatNumber(props.regularMarketDayLow, 2)}-$
                  {formatNumber(props.regularMarketDayHigh, 2)}
                </span>
              </div>
              <div className="flex justify-between p-3 border-t border-r border-light-200 dark:border-dark-200">
                <span className="text-xs text-black/50 dark:text-white/50">
                  Volume
                </span>
                <span className="text-xs text-black dark:text-white font-medium">
                  {formatLargeNumber(props.regularMarketVolume)}
                </span>
              </div>
              <div className="flex justify-between p-3 border-t border-light-200 dark:border-dark-200">
                <span className="text-xs text-black/50 dark:text-white/50">
                  EPS
                </span>
                <span className="text-xs text-black dark:text-white font-medium">
                  $
                  {props.earningsPerShare
                    ? formatNumber(props.earningsPerShare, 2)
                    : 'N/A'}
                </span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Stock;
```

## File: `src/components/Widgets/Weather.tsx`
```tsx
'use client';

import { getMeasurementUnit } from '@/lib/config/clientRegistry';
import { Wind, Droplets, Gauge } from 'lucide-react';
import { useMemo, useEffect, useState } from 'react';

type WeatherWidgetProps = {
  location: string;
  current: {
    time: string;
    temperature_2m: number;
    relative_humidity_2m: number;
    apparent_temperature: number;
    is_day: number;
    precipitation: number;
    weather_code: number;
    wind_speed_10m: number;
    wind_direction_10m: number;
    wind_gusts_10m?: number;
  };
  daily: {
    time: string[];
    weather_code: number[];
    temperature_2m_max: number[];
    temperature_2m_min: number[];
    precipitation_probability_max: number[];
  };
  timezone: string;
};

const getWeatherInfo = (code: number, isDay: boolean, isDarkMode: boolean) => {
  const dayNight = isDay ? 'day' : 'night';

  const weatherMap: Record<
    number,
    { icon: string; description: string; gradient: string }
  > = {
    0: {
      icon: `clear-${dayNight}.svg`,
      description: 'Clear',
      gradient: isDarkMode
        ? isDay
          ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #E8F1FA, #7A9DBF 35%, #4A7BA8 60%, #2F5A88)'
          : 'radial-gradient(ellipse 150% 100% at 50% 100%, #5A6A7E, #3E4E63 40%, #2A3544 65%, #1A2230)'
        : isDay
          ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #FFFFFF, #DBEAFE 30%, #93C5FD 60%, #60A5FA)'
          : 'radial-gradient(ellipse 150% 100% at 50% 100%, #7B8694, #475569 45%, #334155 70%, #1E293B)',
    },
    1: {
      icon: `clear-${dayNight}.svg`,
      description: 'Mostly Clear',
      gradient: isDarkMode
        ? isDay
          ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #E8F1FA, #7A9DBF 35%, #4A7BA8 60%, #2F5A88)'
          : 'radial-gradient(ellipse 150% 100% at 50% 100%, #5A6A7E, #3E4E63 40%, #2A3544 65%, #1A2230)'
        : isDay
          ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #FFFFFF, #DBEAFE 30%, #93C5FD 60%, #60A5FA)'
          : 'radial-gradient(ellipse 150% 100% at 50% 100%, #7B8694, #475569 45%, #334155 70%, #1E293B)',
    },
    2: {
      icon: `cloudy-1-${dayNight}.svg`,
      description: 'Partly Cloudy',
      gradient: isDarkMode
        ? isDay
          ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #D4E1ED, #8BA3B8 35%, #617A93 60%, #426070)'
          : 'radial-gradient(ellipse 150% 100% at 50% 100%, #6B7583, #4A5563 40%, #3A4450 65%, #2A3340)'
        : isDay
          ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #FFFFFF, #E0F2FE 28%, #BFDBFE 58%, #93C5FD)'
          : 'radial-gradient(ellipse 150% 100% at 50% 100%, #8B99AB, #64748B 45%, #475569 70%, #334155)',
    },
    3: {
      icon: `cloudy-1-${dayNight}.svg`,
      description: 'Cloudy',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #B8C3CF, #758190 38%, #546270 65%, #3D4A58)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #F5F8FA, #CBD5E1 32%, #94A3B8 65%, #64748B)',
    },
    45: {
      icon: `fog-${dayNight}.svg`,
      description: 'Foggy',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #C5CDD8, #8892A0 38%, #697380 65%, #4F5A68)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #FFFFFF, #E2E8F0 30%, #CBD5E1 62%, #94A3B8)',
    },
    48: {
      icon: `fog-${dayNight}.svg`,
      description: 'Rime Fog',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #C5CDD8, #8892A0 38%, #697380 65%, #4F5A68)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #FFFFFF, #E2E8F0 30%, #CBD5E1 62%, #94A3B8)',
    },
    51: {
      icon: `rainy-1-${dayNight}.svg`,
      description: 'Light Drizzle',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #B8D4E5, #6FA4C5 35%, #4A85AC 60%, #356A8E)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #E5FBFF, #A5F3FC 28%, #67E8F9 60%, #22D3EE)',
    },
    53: {
      icon: `rainy-1-${dayNight}.svg`,
      description: 'Drizzle',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #B8D4E5, #6FA4C5 35%, #4A85AC 60%, #356A8E)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #E5FBFF, #A5F3FC 28%, #67E8F9 60%, #22D3EE)',
    },
    55: {
      icon: `rainy-2-${dayNight}.svg`,
      description: 'Heavy Drizzle',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #A5C5D8, #5E92B0 35%, #3F789D 60%, #2A5F82)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #D4F3FF, #7DD3FC 30%, #38BDF8 62%, #0EA5E9)',
    },
    61: {
      icon: `rainy-2-${dayNight}.svg`,
      description: 'Light Rain',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #A5C5D8, #5E92B0 35%, #3F789D 60%, #2A5F82)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #D4F3FF, #7DD3FC 30%, #38BDF8 62%, #0EA5E9)',
    },
    63: {
      icon: `rainy-2-${dayNight}.svg`,
      description: 'Rain',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #8DB3C8, #4D819F 38%, #326A87 65%, #215570)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #B8E8FF, #38BDF8 32%, #0EA5E9 65%, #0284C7)',
    },
    65: {
      icon: `rainy-3-${dayNight}.svg`,
      description: 'Heavy Rain',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #7BA3B8, #3D6F8A 38%, #295973 65%, #1A455D)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #9CD9F5, #0EA5E9 32%, #0284C7 65%, #0369A1)',
    },
    71: {
      icon: `snowy-1-${dayNight}.svg`,
      description: 'Light Snow',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #E5F0FA, #9BB5CE 32%, #7496B8 58%, #527A9E)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #FFFFFF, #F0F9FF 25%, #E0F2FE 55%, #BAE6FD)',
    },
    73: {
      icon: `snowy-2-${dayNight}.svg`,
      description: 'Snow',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #D4E5F3, #85A1BD 35%, #6584A8 60%, #496A8E)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #FAFEFF, #E0F2FE 28%, #BAE6FD 60%, #7DD3FC)',
    },
    75: {
      icon: `snowy-3-${dayNight}.svg`,
      description: 'Heavy Snow',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #BDD8EB, #6F92AE 35%, #4F7593 60%, #365A78)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #F0FAFF, #BAE6FD 30%, #7DD3FC 62%, #38BDF8)',
    },
    77: {
      icon: `snowy-1-${dayNight}.svg`,
      description: 'Snow Grains',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #E5F0FA, #9BB5CE 32%, #7496B8 58%, #527A9E)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #FFFFFF, #F0F9FF 25%, #E0F2FE 55%, #BAE6FD)',
    },
    80: {
      icon: `rainy-2-${dayNight}.svg`,
      description: 'Light Showers',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #A5C5D8, #5E92B0 35%, #3F789D 60%, #2A5F82)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #D4F3FF, #7DD3FC 30%, #38BDF8 62%, #0EA5E9)',
    },
    81: {
      icon: `rainy-2-${dayNight}.svg`,
      description: 'Showers',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #8DB3C8, #4D819F 38%, #326A87 65%, #215570)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #B8E8FF, #38BDF8 32%, #0EA5E9 65%, #0284C7)',
    },
    82: {
      icon: `rainy-3-${dayNight}.svg`,
      description: 'Heavy Showers',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #7BA3B8, #3D6F8A 38%, #295973 65%, #1A455D)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #9CD9F5, #0EA5E9 32%, #0284C7 65%, #0369A1)',
    },
    85: {
      icon: `snowy-2-${dayNight}.svg`,
      description: 'Light Snow Showers',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #D4E5F3, #85A1BD 35%, #6584A8 60%, #496A8E)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #FAFEFF, #E0F2FE 28%, #BAE6FD 60%, #7DD3FC)',
    },
    86: {
      icon: `snowy-3-${dayNight}.svg`,
      description: 'Snow Showers',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #BDD8EB, #6F92AE 35%, #4F7593 60%, #365A78)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #F0FAFF, #BAE6FD 30%, #7DD3FC 62%, #38BDF8)',
    },
    95: {
      icon: `scattered-thunderstorms-${dayNight}.svg`,
      description: 'Thunderstorm',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #8A95A3, #5F6A7A 38%, #475260 65%, #2F3A48)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #C8D1DD, #94A3B8 32%, #64748B 65%, #475569)',
    },
    96: {
      icon: 'severe-thunderstorm.svg',
      description: 'Thunderstorm + Hail',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #7A8593, #515C6D 38%, #3A4552 65%, #242D3A)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #B0BBC8, #64748B 32%, #475569 65%, #334155)',
    },
    99: {
      icon: 'severe-thunderstorm.svg',
      description: 'Severe Thunderstorm',
      gradient: isDarkMode
        ? 'radial-gradient(ellipse 150% 100% at 50% 100%, #6A7583, #434E5D 40%, #2F3A47 68%, #1C2530)'
        : 'radial-gradient(ellipse 150% 100% at 50% 100%, #9BA8B8, #475569 35%, #334155 68%, #1E293B)',
    },
  };

  return weatherMap[code] || weatherMap[0];
};

const Weather = ({
  location,
  current,
  daily,
  timezone,
}: WeatherWidgetProps) => {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const unit = getMeasurementUnit();
  const isImperial = unit === 'imperial';
  const tempUnitLabel = isImperial ? '°F' : '°C';
  const windUnitLabel = isImperial ? 'mph' : 'km/h';

  const formatTemp = (celsius: number) => {
    if (!Number.isFinite(celsius)) return 0;
    return Math.round(isImperial ? (celsius * 9) / 5 + 32 : celsius);
  };

  const formatWind = (speedKmh: number) => {
    if (!Number.isFinite(speedKmh)) return 0;
    return Math.round(isImperial ? speedKmh * 0.621371 : speedKmh);
  };

  useEffect(() => {
    const checkDarkMode = () => {
      setIsDarkMode(document.documentElement.classList.contains('dark'));
    };

    checkDarkMode();

    const observer = new MutationObserver(checkDarkMode);
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class'],
    });

    return () => observer.disconnect();
  }, []);

  const weatherInfo = useMemo(
    () =>
      getWeatherInfo(
        current?.weather_code || 0,
        current?.is_day === 1,
        isDarkMode,
      ),
    [current?.weather_code, current?.is_day, isDarkMode],
  );

  const forecast = useMemo(() => {
    if (!daily?.time || daily.time.length === 0) return [];

    return daily.time.slice(1, 7).map((time, idx) => {
      const date = new Date(time);
      const dayName = date.toLocaleDateString('en-US', { weekday: 'short' });
      const isDay = true;
      const weatherCode = daily.weather_code[idx + 1];
      const info = getWeatherInfo(weatherCode, isDay, isDarkMode);

      return {
        day: dayName,
        icon: info.icon,
        high: formatTemp(daily.temperature_2m_max[idx + 1]),
        low: formatTemp(daily.temperature_2m_min[idx + 1]),
        precipitation: daily.precipitation_probability_max[idx + 1] || 0,
      };
    });
  }, [daily, isDarkMode, isImperial]);

  if (!current || !daily || !daily.time || daily.time.length === 0) {
    return (
      <div className="relative overflow-hidden rounded-lg shadow-md bg-gray-200 dark:bg-gray-800">
        <div className="p-4 text-black dark:text-white">
          <p className="text-sm">Weather data unavailable for {location}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="relative overflow-hidden rounded-lg shadow-md">
      <div
        className="absolute inset-0"
        style={{
          background: weatherInfo.gradient,
        }}
      />

      <div className="relative p-4 text-gray-800 dark:text-white">
        <div className="flex items-start justify-between mb-3">
          <div className="flex items-center gap-3">
            <img
              src={`/weather-ico/${weatherInfo.icon}`}
              alt={weatherInfo.description}
              className="w-16 h-16 drop-shadow-lg"
            />
            <div>
              <div className="flex items-baseline gap-1">
                <span className="text-4xl font-bold drop-shadow-md">
                  {formatTemp(current.temperature_2m)}°
                </span>
                <span className="text-lg">{tempUnitLabel}</span>
              </div>
              <p className="text-sm font-medium drop-shadow mt-0.5">
                {weatherInfo.description}
              </p>
            </div>
          </div>
          <div className="text-right">
            <p className="text-xs font-medium opacity-90">
              {formatTemp(daily.temperature_2m_max[0])}°{' '}
              {formatTemp(daily.temperature_2m_min[0])}°
            </p>
          </div>
        </div>

        <div className="mb-3 pb-3 border-b border-gray-800/20 dark:border-white/20">
          <h3 className="text-base font-semibold drop-shadow-md">{location}</h3>
          <p className="text-xs text-gray-700 dark:text-white/80 drop-shadow mt-0.5">
            {new Date(current.time).toLocaleString('en-US', {
              weekday: 'short',
              hour: 'numeric',
              minute: '2-digit',
            })}
          </p>
        </div>

        <div className="grid grid-cols-6 gap-2 mb-3 pb-3 border-b border-gray-800/20 dark:border-white/20">
          {forecast.map((day, idx) => (
            <div
              key={idx}
              className="flex flex-col items-center bg-gray-800/10 dark:bg-white/10 backdrop-blur-sm rounded-md p-2"
            >
              <p className="text-xs font-medium mb-1">{day.day}</p>
              <img
                src={`/weather-ico/${day.icon}`}
                alt=""
                className="w-8 h-8 mb-1"
              />
              <div className="flex items-center gap-1 text-xs">
                <span className="font-semibold">{day.high}°</span>
                <span className="text-gray-600 dark:text-white/60">
                  {day.low}°
                </span>
              </div>
              {day.precipitation > 0 && (
                <div className="flex items-center gap-0.5 mt-1">
                  <Droplets className="w-3 h-3 text-gray-600 dark:text-white/70" />
                  <span className="text-[10px] text-gray-600 dark:text-white/70">
                    {day.precipitation}%
                  </span>
                </div>
              )}
            </div>
          ))}
        </div>

        <div className="grid grid-cols-3 gap-2 text-xs">
          <div className="flex items-center gap-2 bg-gray-800/10 dark:bg-white/10 backdrop-blur-sm rounded-md p-2">
            <Wind className="w-4 h-4 text-gray-700 dark:text-white/80 flex-shrink-0" />
            <div>
              <p className="text-[10px] text-gray-600 dark:text-white/70">
                Wind
              </p>
              <p className="font-semibold">
                {formatWind(current.wind_speed_10m)} {windUnitLabel}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2 bg-gray-800/10 dark:bg-white/10 backdrop-blur-sm rounded-md p-2">
            <Droplets className="w-4 h-4 text-gray-700 dark:text-white/80 flex-shrink-0" />
            <div>
              <p className="text-[10px] text-gray-600 dark:text-white/70">
                Humidity
              </p>
              <p className="font-semibold">
                {Math.round(current.relative_humidity_2m)}%
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2 bg-gray-800/10 dark:bg-white/10 backdrop-blur-sm rounded-md p-2">
            <Gauge className="w-4 h-4 text-gray-700 dark:text-white/80 flex-shrink-0" />
            <div>
              <p className="text-[10px] text-gray-600 dark:text-white/70">
                Feels Like
              </p>
              <p className="font-semibold">
                {formatTemp(current.apparent_temperature)}
                {tempUnitLabel}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Weather;
```

## File: `src/lib/actions.ts`
```typescript
export const getSuggestions = async (chatHistory: [string, string][]) => {
  const chatModel = localStorage.getItem('chatModelKey');
  const chatModelProvider = localStorage.getItem('chatModelProviderId');

  const res = await fetch(`/api/suggestions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      chatHistory,
      chatModel: {
        providerId: chatModelProvider,
        key: chatModel,
      },
    }),
  });

  const data = (await res.json()) as { suggestions: string[] };

  return data.suggestions;
};

export const getApproxLocation = async () => {
  const res = await fetch('https://free.freeipapi.com/api/json', {
    method: 'GET',
  });

  const data = await res.json();

  return {
    latitude: data.latitude,
    longitude: data.longitude,
    city: data.cityName,
  };
};
```

## File: `src/lib/searxng.ts`
```typescript
import { getSearxngURL } from './config/serverRegistry';

interface SearxngSearchOptions {
  categories?: string[];
  engines?: string[];
  language?: string;
  pageno?: number;
}

interface SearxngSearchResult {
  title: string;
  url: string;
  img_src?: string;
  thumbnail_src?: string;
  thumbnail?: string;
  content?: string;
  author?: string;
  iframe_src?: string;
}

export const searchSearxng = async (
  query: string,
  opts?: SearxngSearchOptions,
) => {
  const searxngURL = getSearxngURL();

  const url = new URL(`${searxngURL}/search?format=json`);
  url.searchParams.append('q', query);

  if (opts) {
    Object.keys(opts).forEach((key) => {
      const value = opts[key as keyof SearxngSearchOptions];
      if (Array.isArray(value)) {
        url.searchParams.append(key, value.join(','));
        return;
      }
      url.searchParams.append(key, value as string);
    });
  }

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 10000);

  try {
    const res = await fetch(url, {
      signal: controller.signal,
    });

    if (!res.ok) {
      throw new Error(`SearXNG error: ${res.statusText}`);
    }

    const data = await res.json();

    const results: SearxngSearchResult[] = data.results;
    const suggestions: string[] = data.suggestions;

    return { results, suggestions };
  } catch (err: any) {
    if (err.name === 'AbortError') {
      throw new Error('SearXNG search timed out');
    }
    throw err;
  } finally {
    clearTimeout(timeoutId);
  }
};
```

## File: `src/lib/serverActions.ts`
```typescript
'use server';
```

## File: `src/lib/session.ts`
```typescript
import { EventEmitter } from 'stream';
import { applyPatch } from 'rfc6902';
import { Block } from './types';

const sessions =
  (global as any)._sessionManagerSessions || new Map<string, SessionManager>();
if (process.env.NODE_ENV !== 'production') {
  (global as any)._sessionManagerSessions = sessions;
}

class SessionManager {
  private static sessions: Map<string, SessionManager> = sessions;
  readonly id: string;
  private blocks = new Map<string, Block>();
  private events: { event: string; data: any }[] = [];
  private emitter = new EventEmitter();
  private TTL_MS = 30 * 60 * 1000;

  constructor(id?: string) {
    this.id = id ?? crypto.randomUUID();

    setTimeout(() => {
      SessionManager.sessions.delete(this.id);
    }, this.TTL_MS);
  }

  static getSession(id: string): SessionManager | undefined {
    return this.sessions.get(id);
  }

  static getAllSessions(): SessionManager[] {
    return Array.from(this.sessions.values());
  }

  static createSession(): SessionManager {
    const session = new SessionManager();
    this.sessions.set(session.id, session);
    return session;
  }

  removeAllListeners() {
    this.emitter.removeAllListeners();
  }

  emit(event: string, data: any) {
    this.emitter.emit(event, data);
    this.events.push({ event, data });
  }

  emitBlock(block: Block) {
    this.blocks.set(block.id, block);
    this.emit('data', {
      type: 'block',
      block: block,
    });
  }

  getBlock(blockId: string): Block | undefined {
    return this.blocks.get(blockId);
  }

  updateBlock(blockId: string, patch: any[]) {
    const block = this.blocks.get(blockId);

    if (block) {
      applyPatch(block, patch);
      this.blocks.set(blockId, block);
      this.emit('data', {
        type: 'updateBlock',
        blockId: blockId,
        patch: patch,
      });
    }
  }

  getAllBlocks() {
    return Array.from(this.blocks.values());
  }

  subscribe(listener: (event: string, data: any) => void): () => void {
    const currentEventsLength = this.events.length;

    const handler = (event: string) => (data: any) => listener(event, data);
    const dataHandler = handler('data');
    const endHandler = handler('end');
    const errorHandler = handler('error');

    this.emitter.on('data', dataHandler);
    this.emitter.on('end', endHandler);
    this.emitter.on('error', errorHandler);

    for (let i = 0; i < currentEventsLength; i++) {
      const { event, data } = this.events[i];
      listener(event, data);
    }

    return () => {
      this.emitter.off('data', dataHandler);
      this.emitter.off('end', endHandler);
      this.emitter.off('error', errorHandler);
    };
  }
}

export default SessionManager;
```

## File: `src/lib/types.ts`
```typescript
import { ToolCall } from './models/types';

export type SystemMessage = {
  role: 'system';
  content: string;
};

export type AssistantMessage = {
  role: 'assistant';
  content: string;
  tool_calls?: ToolCall[];
};

export type UserMessage = {
  role: 'user';
  content: string;
};

export type ToolMessage = {
  role: 'tool';
  id: string;
  name: string;
  content: string;
};

export type ChatTurnMessage = UserMessage | AssistantMessage;

export type Message =
  | UserMessage
  | AssistantMessage
  | SystemMessage
  | ToolMessage;

export type Chunk = {
  content: string;
  metadata: Record<string, any>;
};

export type TextBlock = {
  id: string;
  type: 'text';
  data: string;
};

export type SourceBlock = {
  id: string;
  type: 'source';
  data: Chunk[];
};

export type SuggestionBlock = {
  id: string;
  type: 'suggestion';
  data: string[];
};

export type WidgetBlock = {
  id: string;
  type: 'widget';
  data: {
    widgetType: string;
    params: Record<string, any>;
  };
};

export type ReasoningResearchBlock = {
  id: string;
  type: 'reasoning';
  reasoning: string;
};

export type SearchingResearchBlock = {
  id: string;
  type: 'searching';
  searching: string[];
};

export type SearchResultsResearchBlock = {
  id: string;
  type: 'search_results';
  reading: Chunk[];
};

export type ReadingResearchBlock = {
  id: string;
  type: 'reading';
  reading: Chunk[];
};

export type UploadSearchingResearchBlock = {
  id: string;
  type: 'upload_searching';
  queries: string[];
};

export type UploadSearchResultsResearchBlock = {
  id: string;
  type: 'upload_search_results';
  results: Chunk[];
};

export type ResearchBlockSubStep =
  | ReasoningResearchBlock
  | SearchingResearchBlock
  | SearchResultsResearchBlock
  | ReadingResearchBlock
  | UploadSearchingResearchBlock
  | UploadSearchResultsResearchBlock;

export type ResearchBlock = {
  id: string;
  type: 'research';
  data: {
    subSteps: ResearchBlockSubStep[];
  };
};

export type Block =
  | TextBlock
  | SourceBlock
  | SuggestionBlock
  | WidgetBlock
  | ResearchBlock;
```

## File: `src/lib/utils.ts`
```typescript
import clsx, { ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

export const cn = (...classes: ClassValue[]) => twMerge(clsx(...classes));

export const formatTimeDifference = (
  date1: Date | string,
  date2: Date | string,
): string => {
  date1 = new Date(date1);
  date2 = new Date(date2);

  const diffInSeconds = Math.floor(
    Math.abs(date2.getTime() - date1.getTime()) / 1000,
  );

  if (diffInSeconds < 60)
    return `${diffInSeconds} second${diffInSeconds !== 1 ? 's' : ''}`;
  else if (diffInSeconds < 3600)
    return `${Math.floor(diffInSeconds / 60)} minute${Math.floor(diffInSeconds / 60) !== 1 ? 's' : ''}`;
  else if (diffInSeconds < 86400)
    return `${Math.floor(diffInSeconds / 3600)} hour${Math.floor(diffInSeconds / 3600) !== 1 ? 's' : ''}`;
  else if (diffInSeconds < 31536000)
    return `${Math.floor(diffInSeconds / 86400)} day${Math.floor(diffInSeconds / 86400) !== 1 ? 's' : ''}`;
  else
    return `${Math.floor(diffInSeconds / 31536000)} year${Math.floor(diffInSeconds / 31536000) !== 1 ? 's' : ''}`;
};
```

## File: `src/lib/agents/media/image.ts`
```typescript
/* I don't think can be classified as agents but to keep the structure consistent i guess ill keep it here */

import { searchSearxng } from '@/lib/searxng';
import {
  imageSearchFewShots,
  imageSearchPrompt,
} from '@/lib/prompts/media/image';
import BaseLLM from '@/lib/models/base/llm';
import z from 'zod';
import { ChatTurnMessage } from '@/lib/types';
import formatChatHistoryAsString from '@/lib/utils/formatHistory';

type ImageSearchChainInput = {
  chatHistory: ChatTurnMessage[];
  query: string;
};

type ImageSearchResult = {
  img_src: string;
  url: string;
  title: string;
};

const searchImages = async (
  input: ImageSearchChainInput,
  llm: BaseLLM<any>,
) => {
  const schema = z.object({
    query: z.string().describe('The image search query.'),
  });

  const res = await llm.generateObject<typeof schema>({
    messages: [
      {
        role: 'system',
        content: imageSearchPrompt,
      },
      ...imageSearchFewShots,
      {
        role: 'user',
        content: `<conversation>\n${formatChatHistoryAsString(input.chatHistory)}\n</conversation>\n<follow_up>\n${input.query}\n</follow_up>`,
      },
    ],
    schema: schema,
  });

  const searchRes = await searchSearxng(res.query, {
    engines: ['bing images', 'google images'],
  });

  const images: ImageSearchResult[] = [];

  searchRes.results.forEach((result) => {
    if (result.img_src && result.url && result.title) {
      images.push({
        img_src: result.img_src,
        url: result.url,
        title: result.title,
      });
    }
  });

  return images.slice(0, 10);
};

export default searchImages;
```

## File: `src/lib/agents/media/video.ts`
```typescript
import formatChatHistoryAsString from '@/lib/utils/formatHistory';
import { searchSearxng } from '@/lib/searxng';
import {
  videoSearchFewShots,
  videoSearchPrompt,
} from '@/lib/prompts/media/videos';
import { ChatTurnMessage } from '@/lib/types';
import BaseLLM from '@/lib/models/base/llm';
import z from 'zod';

type VideoSearchChainInput = {
  chatHistory: ChatTurnMessage[];
  query: string;
};

type VideoSearchResult = {
  img_src: string;
  url: string;
  title: string;
  iframe_src: string;
};

const searchVideos = async (
  input: VideoSearchChainInput,
  llm: BaseLLM<any>,
) => {
  const schema = z.object({
    query: z.string().describe('The video search query.'),
  });

  const res = await llm.generateObject<typeof schema>({
    messages: [
      {
        role: 'system',
        content: videoSearchPrompt,
      },
      ...videoSearchFewShots,
      {
        role: 'user',
        content: `<conversation>\n${formatChatHistoryAsString(input.chatHistory)}\n</conversation>\n<follow_up>\n${input.query}\n</follow_up>`,
      },
    ],
    schema: schema,
  });

  const searchRes = await searchSearxng(res.query, {
    engines: ['youtube'],
  });

  const videos: VideoSearchResult[] = [];

  searchRes.results.forEach((result) => {
    if (result.thumbnail && result.url && result.title && result.iframe_src) {
      videos.push({
        img_src: result.thumbnail,
        url: result.url,
        title: result.title,
        iframe_src: result.iframe_src,
      });
    }
  });

  return videos.slice(0, 10);
};

export default searchVideos;
```

## File: `src/lib/agents/search/api.ts`
```typescript
import { ResearcherOutput, SearchAgentInput } from './types';
import SessionManager from '@/lib/session';
import { classify } from './classifier';
import Researcher from './researcher';
import { getWriterPrompt } from '@/lib/prompts/search/writer';
import { WidgetExecutor } from './widgets';

class APISearchAgent {
  async searchAsync(session: SessionManager, input: SearchAgentInput) {
    const classification = await classify({
      chatHistory: input.chatHistory,
      enabledSources: input.config.sources,
      query: input.followUp,
      llm: input.config.llm,
    });

    const widgetPromise = WidgetExecutor.executeAll({
      classification,
      chatHistory: input.chatHistory,
      followUp: input.followUp,
      llm: input.config.llm,
    }).catch((err) => {
      console.error(`Error executing widgets: ${err}`);
      return [];
    });

    let searchPromise: Promise<ResearcherOutput> | null = null;

    if (!classification.classification.skipSearch) {
      const researcher = new Researcher();
      searchPromise = researcher.research(SessionManager.createSession(), {
        chatHistory: input.chatHistory,
        followUp: input.followUp,
        classification: classification,
        config: input.config,
      });
    }

    const [widgetOutputs, searchResults] = await Promise.all([
      widgetPromise,
      searchPromise,
    ]);

    if (searchResults) {
      session.emit('data', {
        type: 'searchResults',
        data: searchResults.searchFindings,
      });
    }

    session.emit('data', {
      type: 'researchComplete',
    });

    const finalContext =
      searchResults?.searchFindings
        .map(
          (f, index) =>
            `<result index=${index + 1} title=${f.metadata.title}>${f.content}</result>`,
        )
        .join('\n') || '';

    const widgetContext = widgetOutputs
      .map((o) => {
        return `<result>${o.llmContext}</result>`;
      })
      .join('\n-------------\n');

    const finalContextWithWidgets = `<search_results note="These are the search results and assistant can cite these">\n${finalContext}\n</search_results>\n<widgets_result noteForAssistant="Its output is already showed to the user, assistant can use this information to answer the query but do not CITE this as a souce">\n${widgetContext}\n</widgets_result>`;

    const writerPrompt = getWriterPrompt(
      finalContextWithWidgets,
      input.config.systemInstructions,
      input.config.mode,
    );

    const answerStream = input.config.llm.streamText({
      messages: [
        {
          role: 'system',
          content: writerPrompt,
        },
        ...input.chatHistory,
        {
          role: 'user',
          content: input.followUp,
        },
      ],
    });

    for await (const chunk of answerStream) {
      session.emit('data', {
        type: 'response',
        data: chunk.contentChunk,
      });
    }

    session.emit('end', {});
  }
}

export default APISearchAgent;
```

## File: `src/lib/agents/search/classifier.ts`
```typescript
import z from 'zod';
import { ClassifierInput } from './types';
import { classifierPrompt } from '@/lib/prompts/search/classifier';
import formatChatHistoryAsString from '@/lib/utils/formatHistory';

const schema = z.object({
  classification: z.object({
    skipSearch: z
      .boolean()
      .describe('Indicates whether to skip the search step.'),
    personalSearch: z
      .boolean()
      .describe('Indicates whether to perform a personal search.'),
    academicSearch: z
      .boolean()
      .describe('Indicates whether to perform an academic search.'),
    discussionSearch: z
      .boolean()
      .describe('Indicates whether to perform a discussion search.'),
    showWeatherWidget: z
      .boolean()
      .describe('Indicates whether to show the weather widget.'),
    showStockWidget: z
      .boolean()
      .describe('Indicates whether to show the stock widget.'),
    showCalculationWidget: z
      .boolean()
      .describe('Indicates whether to show the calculation widget.'),
  }),
  standaloneFollowUp: z
    .string()
    .describe(
      "A self-contained, context-independent reformulation of the user's question.",
    ),
});

export const classify = async (input: ClassifierInput) => {
  const output = await input.llm.generateObject<typeof schema>({
    messages: [
      {
        role: 'system',
        content: classifierPrompt,
      },
      {
        role: 'user',
        content: `<conversation_history>\n${formatChatHistoryAsString(input.chatHistory)}\n</conversation_history>\n<user_query>\n${input.query}\n</user_query>`,
      },
    ],
    schema,
  });

  return output;
};
```

## File: `src/lib/agents/search/index.ts`
```typescript
import { ResearcherOutput, SearchAgentInput } from './types';
import SessionManager from '@/lib/session';
import { classify } from './classifier';
import Researcher from './researcher';
import { getWriterPrompt } from '@/lib/prompts/search/writer';
import { WidgetExecutor } from './widgets';
import db from '@/lib/db';
import { chats, messages } from '@/lib/db/schema';
import { and, eq, gt } from 'drizzle-orm';
import { TextBlock } from '@/lib/types';

class SearchAgent {
  async searchAsync(session: SessionManager, input: SearchAgentInput) {
    const exists = await db.query.messages.findFirst({
      where: and(
        eq(messages.chatId, input.chatId),
        eq(messages.messageId, input.messageId),
      ),
    });

    if (!exists) {
      await db.insert(messages).values({
        chatId: input.chatId,
        messageId: input.messageId,
        backendId: session.id,
        query: input.followUp,
        createdAt: new Date().toISOString(),
        status: 'answering',
        responseBlocks: [],
      });
    } else {
      await db
        .delete(messages)
        .where(
          and(eq(messages.chatId, input.chatId), gt(messages.id, exists.id)),
        )
        .execute();
      await db
        .update(messages)
        .set({
          status: 'answering',
          backendId: session.id,
          responseBlocks: [],
        })
        .where(
          and(
            eq(messages.chatId, input.chatId),
            eq(messages.messageId, input.messageId),
          ),
        )
        .execute();
    }

    const classification = await classify({
      chatHistory: input.chatHistory,
      enabledSources: input.config.sources,
      query: input.followUp,
      llm: input.config.llm,
    });

    const widgetPromise = WidgetExecutor.executeAll({
      classification,
      chatHistory: input.chatHistory,
      followUp: input.followUp,
      llm: input.config.llm,
    }).then((widgetOutputs) => {
      widgetOutputs.forEach((o) => {
        session.emitBlock({
          id: crypto.randomUUID(),
          type: 'widget',
          data: {
            widgetType: o.type,
            params: o.data,
          },
        });
      });
      return widgetOutputs;
    });

    let searchPromise: Promise<ResearcherOutput> | null = null;

    if (!classification.classification.skipSearch) {
      const researcher = new Researcher();
      searchPromise = researcher.research(session, {
        chatHistory: input.chatHistory,
        followUp: input.followUp,
        classification: classification,
        config: input.config,
      });
    }

    const [widgetOutputs, searchResults] = await Promise.all([
      widgetPromise,
      searchPromise,
    ]);

    session.emit('data', {
      type: 'researchComplete',
    });

    const finalContext =
      searchResults?.searchFindings
        .map(
          (f, index) =>
            `<result index=${index + 1} title=${f.metadata.title}>${f.content}</result>`,
        )
        .join('\n') || '';

    const widgetContext = widgetOutputs
      .map((o) => {
        return `<result>${o.llmContext}</result>`;
      })
      .join('\n-------------\n');

    const finalContextWithWidgets = `<search_results note="These are the search results and assistant can cite these">\n${finalContext}\n</search_results>\n<widgets_result noteForAssistant="Its output is already showed to the user, assistant can use this information to answer the query but do not CITE this as a souce">\n${widgetContext}\n</widgets_result>`;

    const writerPrompt = getWriterPrompt(
      finalContextWithWidgets,
      input.config.systemInstructions,
      input.config.mode,
    );
    const answerStream = input.config.llm.streamText({
      messages: [
        {
          role: 'system',
          content: writerPrompt,
        },
        ...input.chatHistory,
        {
          role: 'user',
          content: input.followUp,
        },
      ],
    });

    let responseBlockId = '';

    for await (const chunk of answerStream) {
      if (!responseBlockId) {
        const block: TextBlock = {
          id: crypto.randomUUID(),
          type: 'text',
          data: chunk.contentChunk,
        };

        session.emitBlock(block);

        responseBlockId = block.id;
      } else {
        const block = session.getBlock(responseBlockId) as TextBlock | null;

        if (!block) {
          continue;
        }

        block.data += chunk.contentChunk;

        session.updateBlock(block.id, [
          {
            op: 'replace',
            path: '/data',
            value: block.data,
          },
        ]);
      }
    }

    session.emit('end', {});

    await db
      .update(messages)
      .set({
        status: 'completed',
        responseBlocks: session.getAllBlocks(),
      })
      .where(
        and(
          eq(messages.chatId, input.chatId),
          eq(messages.messageId, input.messageId),
        ),
      )
      .execute();
  }
}

export default SearchAgent;
```

## File: `src/lib/agents/search/types.ts`
```typescript
import z from 'zod';
import BaseLLM from '../../models/base/llm';
import BaseEmbedding from '@/lib/models/base/embedding';
import SessionManager from '@/lib/session';
import { ChatTurnMessage, Chunk } from '@/lib/types';

export type SearchSources = 'web' | 'discussions' | 'academic';

export type SearchAgentConfig = {
  sources: SearchSources[];
  fileIds: string[];
  llm: BaseLLM<any>;
  embedding: BaseEmbedding<any>;
  mode: 'speed' | 'balanced' | 'quality';
  systemInstructions: string;
};

export type SearchAgentInput = {
  chatHistory: ChatTurnMessage[];
  followUp: string;
  config: SearchAgentConfig;
  chatId: string;
  messageId: string;
};

export type WidgetInput = {
  chatHistory: ChatTurnMessage[];
  followUp: string;
  classification: ClassifierOutput;
  llm: BaseLLM<any>;
};

export type Widget = {
  type: string;
  shouldExecute: (classification: ClassifierOutput) => boolean;
  execute: (input: WidgetInput) => Promise<WidgetOutput | void>;
};

export type WidgetOutput = {
  type: string;
  llmContext: string;
  data: any;
};

export type ClassifierInput = {
  llm: BaseLLM<any>;
  enabledSources: SearchSources[];
  query: string;
  chatHistory: ChatTurnMessage[];
};

export type ClassifierOutput = {
  classification: {
    skipSearch: boolean;
    personalSearch: boolean;
    academicSearch: boolean;
    discussionSearch: boolean;
    showWeatherWidget: boolean;
    showStockWidget: boolean;
    showCalculationWidget: boolean;
  };
  standaloneFollowUp: string;
};

export type AdditionalConfig = {
  llm: BaseLLM<any>;
  embedding: BaseEmbedding<any>;
  session: SessionManager;
};

export type ResearcherInput = {
  chatHistory: ChatTurnMessage[];
  followUp: string;
  classification: ClassifierOutput;
  config: SearchAgentConfig;
};

export type ResearcherOutput = {
  findings: ActionOutput[];
  searchFindings: Chunk[];
};

export type SearchActionOutput = {
  type: 'search_results';
  results: Chunk[];
};

export type DoneActionOutput = {
  type: 'done';
};

export type ReasoningResearchAction = {
  type: 'reasoning';
  reasoning: string;
};

export type ActionOutput =
  | SearchActionOutput
  | DoneActionOutput
  | ReasoningResearchAction;

export interface ResearchAction<
  TSchema extends z.ZodObject<any> = z.ZodObject<any>,
> {
  name: string;
  schema: z.ZodObject<any>;
  getToolDescription: (config: { mode: SearchAgentConfig['mode'] }) => string;
  getDescription: (config: { mode: SearchAgentConfig['mode'] }) => string;
  enabled: (config: {
    classification: ClassifierOutput;
    fileIds: string[];
    mode: SearchAgentConfig['mode'];
    sources: SearchSources[];
  }) => boolean;
  execute: (
    params: z.infer<TSchema>,
    additionalConfig: AdditionalConfig & {
      researchBlockId: string;
      fileIds: string[];
    },
  ) => Promise<ActionOutput>;
}
```

## File: `src/lib/agents/search/researcher/index.ts`
```typescript
import { ActionOutput, ResearcherInput, ResearcherOutput } from '../types';
import { ActionRegistry } from './actions';
import { getResearcherPrompt } from '@/lib/prompts/search/researcher';
import SessionManager from '@/lib/session';
import { Message, ReasoningResearchBlock } from '@/lib/types';
import formatChatHistoryAsString from '@/lib/utils/formatHistory';
import { ToolCall } from '@/lib/models/types';

class Researcher {
  async research(
    session: SessionManager,
    input: ResearcherInput,
  ): Promise<ResearcherOutput> {
    let actionOutput: ActionOutput[] = [];
    let maxIteration =
      input.config.mode === 'speed'
        ? 2
        : input.config.mode === 'balanced'
          ? 6
          : 25;

    const availableTools = ActionRegistry.getAvailableActionTools({
      classification: input.classification,
      fileIds: input.config.fileIds,
      mode: input.config.mode,
      sources: input.config.sources,
    });

    const availableActionsDescription =
      ActionRegistry.getAvailableActionsDescriptions({
        classification: input.classification,
        fileIds: input.config.fileIds,
        mode: input.config.mode,
        sources: input.config.sources,
      });

    const researchBlockId = crypto.randomUUID();

    session.emitBlock({
      id: researchBlockId,
      type: 'research',
      data: {
        subSteps: [],
      },
    });

    const agentMessageHistory: Message[] = [
      {
        role: 'user',
        content: `
          <conversation>
          ${formatChatHistoryAsString(input.chatHistory.slice(-10))}
           User: ${input.followUp} (Standalone question: ${input.classification.standaloneFollowUp})
           </conversation>
        `,
      },
    ];

    for (let i = 0; i < maxIteration; i++) {
      const researcherPrompt = getResearcherPrompt(
        availableActionsDescription,
        input.config.mode,
        i,
        maxIteration,
        input.config.fileIds,
      );

      const actionStream = input.config.llm.streamText({
        messages: [
          {
            role: 'system',
            content: researcherPrompt,
          },
          ...agentMessageHistory,
        ],
        tools: availableTools,
      });

      const block = session.getBlock(researchBlockId);

      let reasoningEmitted = false;
      let reasoningId = crypto.randomUUID();

      let finalToolCalls: ToolCall[] = [];

      for await (const partialRes of actionStream) {
        if (partialRes.toolCallChunk.length > 0) {
          partialRes.toolCallChunk.forEach((tc) => {
            if (
              tc.name === '__reasoning_preamble' &&
              tc.arguments['plan'] &&
              !reasoningEmitted &&
              block &&
              block.type === 'research'
            ) {
              reasoningEmitted = true;

              block.data.subSteps.push({
                id: reasoningId,
                type: 'reasoning',
                reasoning: tc.arguments['plan'],
              });

              session.updateBlock(researchBlockId, [
                {
                  op: 'replace',
                  path: '/data/subSteps',
                  value: block.data.subSteps,
                },
              ]);
            } else if (
              tc.name === '__reasoning_preamble' &&
              tc.arguments['plan'] &&
              reasoningEmitted &&
              block &&
              block.type === 'research'
            ) {
              const subStepIndex = block.data.subSteps.findIndex(
                (step: any) => step.id === reasoningId,
              );

              if (subStepIndex !== -1) {
                const subStep = block.data.subSteps[
                  subStepIndex
                ] as ReasoningResearchBlock;
                subStep.reasoning = tc.arguments['plan'];
                session.updateBlock(researchBlockId, [
                  {
                    op: 'replace',
                    path: '/data/subSteps',
                    value: block.data.subSteps,
                  },
                ]);
              }
            }

            const existingIndex = finalToolCalls.findIndex(
              (ftc) => ftc.id === tc.id,
            );

            if (existingIndex !== -1) {
              finalToolCalls[existingIndex].arguments = tc.arguments;
            } else {
              finalToolCalls.push(tc);
            }
          });
        }
      }

      if (finalToolCalls.length === 0) {
        break;
      }

      if (finalToolCalls[finalToolCalls.length - 1].name === 'done') {
        break;
      }

      agentMessageHistory.push({
        role: 'assistant',
        content: '',
        tool_calls: finalToolCalls,
      });

      const actionResults = await ActionRegistry.executeAll(finalToolCalls, {
        llm: input.config.llm,
        embedding: input.config.embedding,
        session: session,
        researchBlockId: researchBlockId,
        fileIds: input.config.fileIds,
      });

      actionOutput.push(...actionResults);

      actionResults.forEach((action, i) => {
        agentMessageHistory.push({
          role: 'tool',
          id: finalToolCalls[i].id,
          name: finalToolCalls[i].name,
          content: JSON.stringify(action),
        });
      });
    }

    const searchResults = actionOutput
      .filter((a) => a.type === 'search_results')
      .flatMap((a) => a.results);

    const seenUrls = new Map<string, number>();

    const filteredSearchResults = searchResults
      .map((result, index) => {
        if (result.metadata.url && !seenUrls.has(result.metadata.url)) {
          seenUrls.set(result.metadata.url, index);
          return result;
        } else if (result.metadata.url && seenUrls.has(result.metadata.url)) {
          const existingIndex = seenUrls.get(result.metadata.url)!;

          const existingResult = searchResults[existingIndex];

          existingResult.content += `\n\n${result.content}`;

          return undefined;
        }

        return result;
      })
      .filter((r) => r !== undefined);

    session.emitBlock({
      id: crypto.randomUUID(),
      type: 'source',
      data: filteredSearchResults,
    });

    return {
      findings: actionOutput,
      searchFindings: filteredSearchResults,
    };
  }
}

export default Researcher;
```

## File: `src/lib/agents/search/researcher/actions/academicSearch.ts`
```typescript
import z from 'zod';
import { ResearchAction } from '../../types';
import { Chunk, SearchResultsResearchBlock } from '@/lib/types';
import { searchSearxng } from '@/lib/searxng';

const schema = z.object({
  queries: z.array(z.string()).describe('List of academic search queries'),
});

const academicSearchDescription = `
Use this tool to perform academic searches for scholarly articles, papers, and research studies relevant to the user's query. Provide a list of concise search queries that will help gather comprehensive academic information on the topic at hand.
You can provide up to 3 queries at a time. Make sure the queries are specific and relevant to the user's needs.

For example, if the user is interested in recent advancements in renewable energy, your queries could be:
1. "Recent advancements in renewable energy 2024"
2. "Cutting-edge research on solar power technologies"
3. "Innovations in wind energy systems"

If this tool is present and no other tools are more relevant, you MUST use this tool to get the needed academic information.
`;

const academicSearchAction: ResearchAction<typeof schema> = {
  name: 'academic_search',
  schema: schema,
  getDescription: () => academicSearchDescription,
  getToolDescription: () =>
    "Use this tool to perform academic searches for scholarly articles, papers, and research studies relevant to the user's query. Provide a list of concise search queries that will help gather comprehensive academic information on the topic at hand.",
  enabled: (config) =>
    config.sources.includes('academic') &&
    config.classification.classification.skipSearch === false &&
    config.classification.classification.academicSearch === true,
  execute: async (input, additionalConfig) => {
    input.queries = (
      Array.isArray(input.queries) ? input.queries : [input.queries]
    ).slice(0, 3);

    const researchBlock = additionalConfig.session.getBlock(
      additionalConfig.researchBlockId,
    );

    if (researchBlock && researchBlock.type === 'research') {
      researchBlock.data.subSteps.push({
        type: 'searching',
        id: crypto.randomUUID(),
        searching: input.queries,
      });

      additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
        {
          op: 'replace',
          path: '/data/subSteps',
          value: researchBlock.data.subSteps,
        },
      ]);
    }

    const searchResultsBlockId = crypto.randomUUID();
    let searchResultsEmitted = false;

    let results: Chunk[] = [];

    const search = async (q: string) => {
      const res = await searchSearxng(q, {
        engines: ['arxiv', 'google scholar', 'pubmed'],
      });

      const resultChunks: Chunk[] = res.results.map((r) => ({
        content: r.content || r.title,
        metadata: {
          title: r.title,
          url: r.url,
        },
      }));

      results.push(...resultChunks);

      if (
        !searchResultsEmitted &&
        researchBlock &&
        researchBlock.type === 'research'
      ) {
        searchResultsEmitted = true;

        researchBlock.data.subSteps.push({
          id: searchResultsBlockId,
          type: 'search_results',
          reading: resultChunks,
        });

        additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
          {
            op: 'replace',
            path: '/data/subSteps',
            value: researchBlock.data.subSteps,
          },
        ]);
      } else if (
        searchResultsEmitted &&
        researchBlock &&
        researchBlock.type === 'research'
      ) {
        const subStepIndex = researchBlock.data.subSteps.findIndex(
          (step) => step.id === searchResultsBlockId,
        );

        const subStep = researchBlock.data.subSteps[
          subStepIndex
        ] as SearchResultsResearchBlock;

        subStep.reading.push(...resultChunks);

        additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
          {
            op: 'replace',
            path: '/data/subSteps',
            value: researchBlock.data.subSteps,
          },
        ]);
      }
    };

    await Promise.all(input.queries.map(search));

    return {
      type: 'search_results',
      results,
    };
  },
};

export default academicSearchAction;
```

## File: `src/lib/agents/search/researcher/actions/done.ts`
```typescript
import z from 'zod';
import { ResearchAction } from '../../types';

const actionDescription = `
Use this action ONLY when you have completed all necessary research and are ready to provide a final answer to the user. This indicates that you have gathered sufficient information from previous steps and are concluding the research process.
YOU MUST CALL THIS ACTION TO SIGNAL COMPLETION; DO NOT OUTPUT FINAL ANSWERS DIRECTLY TO THE USER.
IT WILL BE AUTOMATICALLY TRIGGERED IF MAXIMUM ITERATIONS ARE REACHED SO IF YOU'RE LOW ON ITERATIONS, DON'T CALL IT AND INSTEAD FOCUS ON GATHERING ESSENTIAL INFO FIRST.
`;

const doneAction: ResearchAction<any> = {
  name: 'done',
  schema: z.object({}),
  getToolDescription: () =>
    'Only call this after __reasoning_preamble AND after any other needed tool calls when you truly have enough to answer. Do not call if information is still missing.',
  getDescription: () => actionDescription,
  enabled: (_) => true,
  execute: async (params, additionalConfig) => {
    return {
      type: 'done',
    };
  },
};

export default doneAction;
```

## File: `src/lib/agents/search/researcher/actions/index.ts`
```typescript
import academicSearchAction from './academicSearch';
import doneAction from './done';
import planAction from './plan';
import ActionRegistry from './registry';
import scrapeURLAction from './scrapeURL';
import socialSearchAction from './socialSearch';
import uploadsSearchAction from './uploadsSearch';
import webSearchAction from './webSearch';

ActionRegistry.register(webSearchAction);
ActionRegistry.register(doneAction);
ActionRegistry.register(planAction);
ActionRegistry.register(scrapeURLAction);
ActionRegistry.register(uploadsSearchAction);
ActionRegistry.register(academicSearchAction);
ActionRegistry.register(socialSearchAction);

export { ActionRegistry };
```

## File: `src/lib/agents/search/researcher/actions/plan.ts`
```typescript
import z from 'zod';
import { ResearchAction } from '../../types';

const schema = z.object({
  plan: z
    .string()
    .describe(
      'A concise natural-language plan in one short paragraph. Open with a short intent phrase (e.g., "Okay, the user wants to...", "Searching for...", "Looking into...") and lay out the steps you will take.',
    ),
});

const actionDescription = `
Use this tool FIRST on every turn to state your plan in natural language before any other action. Keep it short, action-focused, and tailored to the current query.
Make sure to not include reference to any tools or actions you might take, just the plan itself. The user isn't aware about tools, but they love to see your thought process.

Here are some examples of good plans:
<examples>
- "Okay, the user wants to know the latest advancements in renewable energy. I will start by looking for recent articles and studies on this topic, then summarize the key points." -> "I have gathered enough information to provide a comprehensive answer."
- "The user is asking about the health benefits of a Mediterranean diet. I will search for scientific studies and expert opinions on this diet, then compile the findings into a clear summary." -> "I have gathered information about the Mediterranean diet and its health benefits, I will now look up for any recent studies to ensure the information is current."
</examples>

YOU CAN NEVER CALL ANY OTHER TOOL BEFORE CALLING THIS ONE FIRST, IF YOU DO, THAT CALL WOULD BE IGNORED.
`;

const planAction: ResearchAction<typeof schema> = {
  name: '__reasoning_preamble',
  schema: schema,
  getToolDescription: () =>
    'Use this FIRST on every turn to state your plan in natural language before any other action. Keep it short, action-focused, and tailored to the current query.',
  getDescription: () => actionDescription,
  enabled: (config) => config.mode !== 'speed',
  execute: async (input, _) => {
    return {
      type: 'reasoning',
      reasoning: input.plan,
    };
  },
};

export default planAction;
```

## File: `src/lib/agents/search/researcher/actions/registry.ts`
```typescript
import { Tool, ToolCall } from '@/lib/models/types';
import {
  ActionOutput,
  AdditionalConfig,
  ClassifierOutput,
  ResearchAction,
  SearchAgentConfig,
  SearchSources,
} from '../../types';

class ActionRegistry {
  private static actions: Map<string, ResearchAction> = new Map();

  static register(action: ResearchAction<any>) {
    this.actions.set(action.name, action);
  }

  static get(name: string): ResearchAction | undefined {
    return this.actions.get(name);
  }

  static getAvailableActions(config: {
    classification: ClassifierOutput;
    fileIds: string[];
    mode: SearchAgentConfig['mode'];
    sources: SearchSources[];
  }): ResearchAction[] {
    return Array.from(
      this.actions.values().filter((action) => action.enabled(config)),
    );
  }

  static getAvailableActionTools(config: {
    classification: ClassifierOutput;
    fileIds: string[];
    mode: SearchAgentConfig['mode'];
    sources: SearchSources[];
  }): Tool[] {
    const availableActions = this.getAvailableActions(config);

    return availableActions.map((action) => ({
      name: action.name,
      description: action.getToolDescription({ mode: config.mode }),
      schema: action.schema,
    }));
  }

  static getAvailableActionsDescriptions(config: {
    classification: ClassifierOutput;
    fileIds: string[];
    mode: SearchAgentConfig['mode'];
    sources: SearchSources[];
  }): string {
    const availableActions = this.getAvailableActions(config);

    return availableActions
      .map(
        (action) =>
          `<tool name="${action.name}">\n${action.getDescription({ mode: config.mode })}\n</tool>`,
      )
      .join('\n\n');
  }

  static async execute(
    name: string,
    params: any,
    additionalConfig: AdditionalConfig & {
      researchBlockId: string;
      fileIds: string[];
    },
  ) {
    const action = this.actions.get(name);

    if (!action) {
      throw new Error(`Action with name ${name} not found`);
    }

    return action.execute(params, additionalConfig);
  }

  static async executeAll(
    actions: ToolCall[],
    additionalConfig: AdditionalConfig & {
      researchBlockId: string;
      fileIds: string[];
    },
  ): Promise<ActionOutput[]> {
    const results: ActionOutput[] = [];

    await Promise.all(
      actions.map(async (actionConfig) => {
        const output = await this.execute(
          actionConfig.name,
          actionConfig.arguments,
          additionalConfig,
        );
        results.push(output);
      }),
    );

    return results;
  }
}

export default ActionRegistry;
```

## File: `src/lib/agents/search/researcher/actions/scrapeURL.ts`
```typescript
import z from 'zod';
import { ResearchAction } from '../../types';
import { Chunk, ReadingResearchBlock } from '@/lib/types';
import TurnDown from 'turndown';
import path from 'path';

const turndownService = new TurnDown();

const schema = z.object({
  urls: z.array(z.string()).describe('A list of URLs to scrape content from.'),
});

const actionDescription = `
Use this tool to scrape and extract content from the provided URLs. This is useful when you the user has asked you to extract or summarize information from specific web pages. You can provide up to 3 URLs at a time. NEVER CALL THIS TOOL EXPLICITLY YOURSELF UNLESS INSTRUCTED TO DO SO BY THE USER.
You should only call this tool when the user has specifically requested information from certain web pages, never call this yourself to get extra information without user instruction.

For example, if the user says "Please summarize the content of https://example.com/article", you can call this tool with that URL to get the content and then provide the summary or "What does X mean according to https://example.com/page", you can call this tool with that URL to get the content and provide the explanation.
`;

const scrapeURLAction: ResearchAction<typeof schema> = {
  name: 'scrape_url',
  schema: schema,
  getToolDescription: () =>
    'Use this tool to scrape and extract content from the provided URLs. This is useful when you the user has asked you to extract or summarize information from specific web pages. You can provide up to 3 URLs at a time. NEVER CALL THIS TOOL EXPLICITLY YOURSELF UNLESS INSTRUCTED TO DO SO BY THE USER.',
  getDescription: () => actionDescription,
  enabled: (_) => true,
  execute: async (params, additionalConfig) => {
    params.urls = params.urls.slice(0, 3);

    let readingBlockId = crypto.randomUUID();
    let readingEmitted = false;

    const researchBlock = additionalConfig.session.getBlock(
      additionalConfig.researchBlockId,
    );

    const results: Chunk[] = [];

    await Promise.all(
      params.urls.map(async (url) => {
        try {
          const res = await fetch(url);
          const text = await res.text();

          const title =
            text.match(/<title>(.*?)<\/title>/i)?.[1] || `Content from ${url}`;

          if (
            !readingEmitted &&
            researchBlock &&
            researchBlock.type === 'research'
          ) {
            readingEmitted = true;
            researchBlock.data.subSteps.push({
              id: readingBlockId,
              type: 'reading',
              reading: [
                {
                  content: '',
                  metadata: {
                    url,
                    title: title,
                  },
                },
              ],
            });

            additionalConfig.session.updateBlock(
              additionalConfig.researchBlockId,
              [
                {
                  op: 'replace',
                  path: '/data/subSteps',
                  value: researchBlock.data.subSteps,
                },
              ],
            );
          } else if (
            readingEmitted &&
            researchBlock &&
            researchBlock.type === 'research'
          ) {
            const subStepIndex = researchBlock.data.subSteps.findIndex(
              (step: any) => step.id === readingBlockId,
            );

            const subStep = researchBlock.data.subSteps[
              subStepIndex
            ] as ReadingResearchBlock;

            subStep.reading.push({
              content: '',
              metadata: {
                url,
                title: title,
              },
            });

            additionalConfig.session.updateBlock(
              additionalConfig.researchBlockId,
              [
                {
                  op: 'replace',
                  path: '/data/subSteps',
                  value: researchBlock.data.subSteps,
                },
              ],
            );
          }

          const markdown = turndownService.turndown(text);

          results.push({
            content: markdown,
            metadata: {
              url,
              title: title,
            },
          });
        } catch (error) {
          results.push({
            content: `Failed to fetch content from ${url}: ${error}`,
            metadata: {
              url,
              title: `Error fetching ${url}`,
            },
          });
        }
      }),
    );

    return {
      type: 'search_results',
      results,
    };
  },
};

export default scrapeURLAction;
```

## File: `src/lib/agents/search/researcher/actions/socialSearch.ts`
```typescript
import z from 'zod';
import { ResearchAction } from '../../types';
import { Chunk, SearchResultsResearchBlock } from '@/lib/types';
import { searchSearxng } from '@/lib/searxng';

const schema = z.object({
  queries: z.array(z.string()).describe('List of social search queries'),
});

const socialSearchDescription = `
Use this tool to perform social media searches for relevant posts, discussions, and trends related to the user's query. Provide a list of concise search queries that will help gather comprehensive social media information on the topic at hand.
You can provide up to 3 queries at a time. Make sure the queries are specific and relevant to the user's needs.

For example, if the user is interested in public opinion on electric vehicles, your queries could be:
1. "Electric vehicles public opinion 2024"
2. "Social media discussions on EV adoption"
3. "Trends in electric vehicle usage"

If this tool is present and no other tools are more relevant, you MUST use this tool to get the needed social media information.
`;

const socialSearchAction: ResearchAction<typeof schema> = {
  name: 'social_search',
  schema: schema,
  getDescription: () => socialSearchDescription,
  getToolDescription: () =>
    "Use this tool to perform social media searches for relevant posts, discussions, and trends related to the user's query. Provide a list of concise search queries that will help gather comprehensive social media information on the topic at hand.",
  enabled: (config) =>
    config.sources.includes('discussions') &&
    config.classification.classification.skipSearch === false &&
    config.classification.classification.discussionSearch === true,
  execute: async (input, additionalConfig) => {
    input.queries = (
      Array.isArray(input.queries) ? input.queries : [input.queries]
    ).slice(0, 3);

    const researchBlock = additionalConfig.session.getBlock(
      additionalConfig.researchBlockId,
    );

    if (researchBlock && researchBlock.type === 'research') {
      researchBlock.data.subSteps.push({
        type: 'searching',
        id: crypto.randomUUID(),
        searching: input.queries,
      });

      additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
        {
          op: 'replace',
          path: '/data/subSteps',
          value: researchBlock.data.subSteps,
        },
      ]);
    }

    const searchResultsBlockId = crypto.randomUUID();
    let searchResultsEmitted = false;

    let results: Chunk[] = [];

    const search = async (q: string) => {
      const res = await searchSearxng(q, {
        engines: ['reddit'],
      });

      const resultChunks: Chunk[] = res.results.map((r) => ({
        content: r.content || r.title,
        metadata: {
          title: r.title,
          url: r.url,
        },
      }));

      results.push(...resultChunks);

      if (
        !searchResultsEmitted &&
        researchBlock &&
        researchBlock.type === 'research'
      ) {
        searchResultsEmitted = true;

        researchBlock.data.subSteps.push({
          id: searchResultsBlockId,
          type: 'search_results',
          reading: resultChunks,
        });

        additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
          {
            op: 'replace',
            path: '/data/subSteps',
            value: researchBlock.data.subSteps,
          },
        ]);
      } else if (
        searchResultsEmitted &&
        researchBlock &&
        researchBlock.type === 'research'
      ) {
        const subStepIndex = researchBlock.data.subSteps.findIndex(
          (step) => step.id === searchResultsBlockId,
        );

        const subStep = researchBlock.data.subSteps[
          subStepIndex
        ] as SearchResultsResearchBlock;

        subStep.reading.push(...resultChunks);

        additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
          {
            op: 'replace',
            path: '/data/subSteps',
            value: researchBlock.data.subSteps,
          },
        ]);
      }
    };

    await Promise.all(input.queries.map(search));

    return {
      type: 'search_results',
      results,
    };
  },
};

export default socialSearchAction;
```

## File: `src/lib/agents/search/researcher/actions/uploadsSearch.ts`
```typescript
import z from 'zod';
import { ResearchAction } from '../../types';
import UploadStore from '@/lib/uploads/store';

const schema = z.object({
  queries: z
    .array(z.string())
    .describe(
      'A list of queries to search in user uploaded files. Can be a maximum of 3 queries.',
    ),
});

const uploadsSearchAction: ResearchAction<typeof schema> = {
  name: 'uploads_search',
  enabled: (config) =>
    (config.classification.classification.personalSearch &&
      config.fileIds.length > 0) ||
    config.fileIds.length > 0,
  schema,
  getToolDescription: () =>
    `Use this tool to perform searches over the user's uploaded files. This is useful when you need to gather information from the user's documents to answer their questions. You can provide up to 3 queries at a time. You will have to use this every single time if this is present and relevant.`,
  getDescription: () => `
  Use this tool to perform searches over the user's uploaded files. This is useful when you need to gather information from the user's documents to answer their questions. You can provide up to 3 queries at a time. You will have to use this every single time if this is present and relevant.
  Always ensure that the queries you use are directly relevant to the user's request and pertain to the content of their uploaded files.

  For example, if the user says "Please find information about X in my uploaded documents", you can call this tool with a query related to X to retrieve the relevant information from their files.
  Never use this tool to search the web or for information that is not contained within the user's uploaded files.
  `,
  execute: async (input, additionalConfig) => {
    input.queries = input.queries.slice(0, 3);

    const researchBlock = additionalConfig.session.getBlock(
      additionalConfig.researchBlockId,
    );

    if (researchBlock && researchBlock.type === 'research') {
      researchBlock.data.subSteps.push({
        id: crypto.randomUUID(),
        type: 'upload_searching',
        queries: input.queries,
      });

      additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
        {
          op: 'replace',
          path: '/data/subSteps',
          value: researchBlock.data.subSteps,
        },
      ]);
    }

    const uploadStore = new UploadStore({
      embeddingModel: additionalConfig.embedding,
      fileIds: additionalConfig.fileIds,
    });

    const results = await uploadStore.query(input.queries, 10);

    const seenIds = new Map<string, number>();

    const filteredSearchResults = results
      .map((result, index) => {
        if (result.metadata.url && !seenIds.has(result.metadata.url)) {
          seenIds.set(result.metadata.url, index);
          return result;
        } else if (result.metadata.url && seenIds.has(result.metadata.url)) {
          const existingIndex = seenIds.get(result.metadata.url)!;
          const existingResult = results[existingIndex];

          existingResult.content += `\n\n${result.content}`;

          return undefined;
        }

        return result;
      })
      .filter((r) => r !== undefined);

    if (researchBlock && researchBlock.type === 'research') {
      researchBlock.data.subSteps.push({
        id: crypto.randomUUID(),
        type: 'upload_search_results',
        results: filteredSearchResults,
      });

      additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
        {
          op: 'replace',
          path: '/data/subSteps',
          value: researchBlock.data.subSteps,
        },
      ]);
    }

    return {
      type: 'search_results',
      results: filteredSearchResults,
    };
  },
};

export default uploadsSearchAction;
```

## File: `src/lib/agents/search/researcher/actions/webSearch.ts`
```typescript
import z from 'zod';
import { ResearchAction } from '../../types';
import { searchSearxng } from '@/lib/searxng';
import { Chunk, SearchResultsResearchBlock } from '@/lib/types';

const actionSchema = z.object({
  type: z.literal('web_search'),
  queries: z
    .array(z.string())
    .describe('An array of search queries to perform web searches for.'),
});

const speedModePrompt = `
Use this tool to perform web searches based on the provided queries. This is useful when you need to gather information from the web to answer the user's questions. You can provide up to 3 queries at a time. You will have to use this every single time if this is present and relevant.
You are currently on speed mode, meaning you would only get to call this tool once. Make sure to prioritize the most important queries that are likely to get you the needed information in one go.

Your queries should be very targeted and specific to the information you need, avoid broad or generic queries.
Your queries shouldn't be sentences but rather keywords that are SEO friendly and can be used to search the web for information.

For example, if the user is asking about the features of a new technology, you might use queries like "GPT-5.1 features", "GPT-5.1 release date", "GPT-5.1 improvements" rather than a broad query like "Tell me about GPT-5.1".

You can search for 3 queries in one go, make sure to utilize all 3 queries to maximize the information you can gather. If a question is simple, then split your queries to cover different aspects or related topics to get a comprehensive understanding.
If this tool is present and no other tools are more relevant, you MUST use this tool to get the needed information.
`;

const balancedModePrompt = `
Use this tool to perform web searches based on the provided queries. This is useful when you need to gather information from the web to answer the user's questions. You can provide up to 3 queries at a time. You will have to use this every single time if this is present and relevant.

You can call this tool several times if needed to gather enough information.
Start initially with broader queries to get an overview, then narrow down with more specific queries based on the results you receive.

Your queries shouldn't be sentences but rather keywords that are SEO friendly and can be used to search the web for information.

For example if the user is asking about Tesla, your actions should be like:
1. __reasoning_preamble "The user is asking about Tesla. I will start with broader queries to get an overview of Tesla, then narrow down with more specific queries based on the results I receive." then
2. web_search ["Tesla", "Tesla latest news", "Tesla stock price"] then
3. __reasoning_preamble "Based on the previous search results, I will now narrow down my queries to focus on Tesla's recent developments and stock performance." then
4. web_search ["Tesla Q2 2025 earnings", "Tesla new model 2025", "Tesla stock analysis"] then done.
5. __reasoning_preamble "I have gathered enough information to provide a comprehensive answer."
6. done.

You can search for 3 queries in one go, make sure to utilize all 3 queries to maximize the information you can gather. If a question is simple, then split your queries to cover different aspects or related topics to get a comprehensive understanding.
If this tool is present and no other tools are more relevant, you MUST use this tool to get the needed information. You can call this tools, multiple times as needed.
`;

const qualityModePrompt = `
Use this tool to perform web searches based on the provided queries. This is useful when you need to gather information from the web to answer the user's questions. You can provide up to 3 queries at a time. You will have to use this every single time if this is present and relevant.

You have to call this tool several times to gather enough information unless the question is very simple (like greeting questions or basic facts).
Start initially with broader queries to get an overview, then narrow down with more specific queries based on the results you receive.
Never stop before at least 5-6 iterations of searches unless the user question is very simple.

Your queries shouldn't be sentences but rather keywords that are SEO friendly and can be used to search the web for information.

You can search for 3 queries in one go, make sure to utilize all 3 queries to maximize the information you can gather. If a question is simple, then split your queries to cover different aspects or related topics to get a comprehensive understanding.
If this tool is present and no other tools are more relevant, you MUST use this tool to get the needed information. You can call this tools, multiple times as needed.
`;

const webSearchAction: ResearchAction<typeof actionSchema> = {
  name: 'web_search',
  schema: actionSchema,
  getToolDescription: () =>
    "Use this tool to perform web searches based on the provided queries. This is useful when you need to gather information from the web to answer the user's questions. You can provide up to 3 queries at a time. You will have to use this every single time if this is present and relevant.",
  getDescription: (config) => {
    let prompt = '';

    switch (config.mode) {
      case 'speed':
        prompt = speedModePrompt;
        break;
      case 'balanced':
        prompt = balancedModePrompt;
        break;
      case 'quality':
        prompt = qualityModePrompt;
        break;
      default:
        prompt = speedModePrompt;
        break;
    }

    return prompt;
  },
  enabled: (config) =>
    config.sources.includes('web') &&
    config.classification.classification.skipSearch === false,
  execute: async (input, additionalConfig) => {
    input.queries = (
      Array.isArray(input.queries) ? input.queries : [input.queries]
    ).slice(0, 3);

    const researchBlock = additionalConfig.session.getBlock(
      additionalConfig.researchBlockId,
    );

    if (researchBlock && researchBlock.type === 'research') {
      researchBlock.data.subSteps.push({
        id: crypto.randomUUID(),
        type: 'searching',
        searching: input.queries,
      });

      additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
        {
          op: 'replace',
          path: '/data/subSteps',
          value: researchBlock.data.subSteps,
        },
      ]);
    }

    const searchResultsBlockId = crypto.randomUUID();
    let searchResultsEmitted = false;

    let results: Chunk[] = [];

    const search = async (q: string) => {
      const res = await searchSearxng(q);

      const resultChunks: Chunk[] = res.results.map((r) => ({
        content: r.content || r.title,
        metadata: {
          title: r.title,
          url: r.url,
        },
      }));

      results.push(...resultChunks);

      if (
        !searchResultsEmitted &&
        researchBlock &&
        researchBlock.type === 'research'
      ) {
        searchResultsEmitted = true;

        researchBlock.data.subSteps.push({
          id: searchResultsBlockId,
          type: 'search_results',
          reading: resultChunks,
        });

        additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
          {
            op: 'replace',
            path: '/data/subSteps',
            value: researchBlock.data.subSteps,
          },
        ]);
      } else if (
        searchResultsEmitted &&
        researchBlock &&
        researchBlock.type === 'research'
      ) {
        const subStepIndex = researchBlock.data.subSteps.findIndex(
          (step) => step.id === searchResultsBlockId,
        );

        const subStep = researchBlock.data.subSteps[
          subStepIndex
        ] as SearchResultsResearchBlock;

        subStep.reading.push(...resultChunks);

        additionalConfig.session.updateBlock(additionalConfig.researchBlockId, [
          {
            op: 'replace',
            path: '/data/subSteps',
            value: researchBlock.data.subSteps,
          },
        ]);
      }
    };

    await Promise.all(input.queries.map(search));

    return {
      type: 'search_results',
      results,
    };
  },
};

export default webSearchAction;
```

## File: `src/lib/agents/search/widgets/calculationWidget.ts`
```typescript
import z from 'zod';
import { Widget } from '../types';
import formatChatHistoryAsString from '@/lib/utils/formatHistory';
import { exp, evaluate as mathEval } from 'mathjs';

const schema = z.object({
  expression: z
    .string()
    .describe('Mathematical expression to calculate or evaluate.'),
  notPresent: z
    .boolean()
    .describe('Whether there is any need for the calculation widget.'),
});

const system = `
<role>
Assistant is a calculation expression extractor. You will recieve a user follow up and a conversation history.
Your task is to determine if there is a mathematical expression that needs to be calculated or evaluated. If there is, extract the expression and return it. If there is no need for any calculation, set notPresent to true.
</role>

<instructions>
Make sure that the extracted expression is valid and can be used to calculate the result with Math JS library (https://mathjs.org/). If the expression is not valid, set notPresent to true.
If you feel like you cannot extract a valid expression, set notPresent to true.
</instructions>

<output_format>
You must respond in the following JSON format without any extra text, explanations or filler sentences:
{
  "expression": string,
  "notPresent": boolean
}
</output_format>
`;

const calculationWidget: Widget = {
  type: 'calculationWidget',
  shouldExecute: (classification) =>
    classification.classification.showCalculationWidget,
  execute: async (input) => {
    const output = await input.llm.generateObject<typeof schema>({
      messages: [
        {
          role: 'system',
          content: system,
        },
        {
          role: 'user',
          content: `<conversation_history>\n${formatChatHistoryAsString(input.chatHistory)}\n</conversation_history>\n<user_follow_up>\n${input.followUp}\n</user_follow_up>`,
        },
      ],
      schema,
    });

    if (output.notPresent) {
      return;
    }

    const result = mathEval(output.expression);

    return {
      type: 'calculation_result',
      llmContext: `The result of the calculation for the expression "${output.expression}" is: ${result}`,
      data: {
        expression: output.expression,
        result,
      },
    };
  },
};

export default calculationWidget;
```

## File: `src/lib/agents/search/widgets/executor.ts`
```typescript
import { Widget, WidgetInput, WidgetOutput } from '../types';

class WidgetExecutor {
  static widgets = new Map<string, Widget>();

  static register(widget: Widget) {
    this.widgets.set(widget.type, widget);
  }

  static getWidget(type: string): Widget | undefined {
    return this.widgets.get(type);
  }

  static async executeAll(input: WidgetInput): Promise<WidgetOutput[]> {
    const results: WidgetOutput[] = [];

    await Promise.all(
      Array.from(this.widgets.values()).map(async (widget) => {
        try {
          if (widget.shouldExecute(input.classification)) {
            const output = await widget.execute(input);
            if (output) {
              results.push(output);
            }
          }
        } catch (e) {
          console.log(`Error executing widget ${widget.type}:`, e);
        }
      }),
    );

    return results;
  }
}

export default WidgetExecutor;
```

## File: `src/lib/agents/search/widgets/index.ts`
```typescript
import calculationWidget from './calculationWidget';
import WidgetExecutor from './executor';
import weatherWidget from './weatherWidget';
import stockWidget from './stockWidget';

WidgetExecutor.register(weatherWidget);
WidgetExecutor.register(calculationWidget);
WidgetExecutor.register(stockWidget);

export { WidgetExecutor };
```

## File: `src/lib/agents/search/widgets/stockWidget.ts`
```typescript
import z from 'zod';
import { Widget } from '../types';
import YahooFinance from 'yahoo-finance2';
import formatChatHistoryAsString from '@/lib/utils/formatHistory';

const yf = new YahooFinance({
  suppressNotices: ['yahooSurvey'],
});

const schema = z.object({
  name: z
    .string()
    .describe(
      "The stock name for example Nvidia, Google, Apple, Microsoft etc. You can also return ticker if you're aware of it otherwise just use the name.",
    ),
  comparisonNames: z
    .array(z.string())
    .max(3)
    .describe(
      "Optional array of up to 3 stock names to compare against the base name (e.g., ['Microsoft', 'GOOGL', 'Meta']). Charts will show percentage change comparison.",
    ),
  notPresent: z
    .boolean()
    .describe('Whether there is no need for the stock widget.'),
});

const systemPrompt = `
<role>
You are a stock ticker/name extractor. You will receive a user follow up and a conversation history.
Your task is to determine if the user is asking about stock information and extract the stock name(s) they want data for.
</role>

<instructions>
- If the user is asking about a stock, extract the primary stock name or ticker.
- If the user wants to compare stocks, extract up to 3 comparison stock names in comparisonNames.
- You can use either stock names (e.g., "Nvidia", "Apple") or tickers (e.g., "NVDA", "AAPL").
- If you cannot determine a valid stock or the query is not stock-related, set notPresent to true.
- If no comparison is needed, set comparisonNames to an empty array.
</instructions>

<output_format>
You must respond in the following JSON format without any extra text, explanations or filler sentences:
{
  "name": string,
  "comparisonNames": string[],
  "notPresent": boolean
}
</output_format>
`;

const stockWidget: Widget = {
  type: 'stockWidget',
  shouldExecute: (classification) =>
    classification.classification.showStockWidget,
  execute: async (input) => {
    const output = await input.llm.generateObject<typeof schema>({
      messages: [
        {
          role: 'system',
          content: systemPrompt,
        },
        {
          role: 'user',
          content: `<conversation_history>\n${formatChatHistoryAsString(input.chatHistory)}\n</conversation_history>\n<user_follow_up>\n${input.followUp}\n</user_follow_up>`,
        },
      ],
      schema,
    });

    if (output.notPresent) {
      return;
    }

    const params = output;
    try {
      const name = params.name;

      const findings = await yf.search(name);

      if (findings.quotes.length === 0)
        throw new Error(`Failed to find quote for name/symbol: ${name}`);

      const ticker = findings.quotes[0].symbol as string;

      const quote: any = await yf.quote(ticker);

      const chartPromises = {
        '1D': yf
          .chart(ticker, {
            period1: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000),
            period2: new Date(),
            interval: '5m',
          })
          .catch(() => null),
        '5D': yf
          .chart(ticker, {
            period1: new Date(Date.now() - 6 * 24 * 60 * 60 * 1000),
            period2: new Date(),
            interval: '15m',
          })
          .catch(() => null),
        '1M': yf
          .chart(ticker, {
            period1: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000),
            interval: '1d',
          })
          .catch(() => null),
        '3M': yf
          .chart(ticker, {
            period1: new Date(Date.now() - 90 * 24 * 60 * 60 * 1000),
            interval: '1d',
          })
          .catch(() => null),
        '6M': yf
          .chart(ticker, {
            period1: new Date(Date.now() - 180 * 24 * 60 * 60 * 1000),
            interval: '1d',
          })
          .catch(() => null),
        '1Y': yf
          .chart(ticker, {
            period1: new Date(Date.now() - 365 * 24 * 60 * 60 * 1000),
            interval: '1d',
          })
          .catch(() => null),
        MAX: yf
          .chart(ticker, {
            period1: new Date(Date.now() - 10 * 365 * 24 * 60 * 60 * 1000),
            interval: '1wk',
          })
          .catch(() => null),
      };

      const charts = await Promise.all([
        chartPromises['1D'],
        chartPromises['5D'],
        chartPromises['1M'],
        chartPromises['3M'],
        chartPromises['6M'],
        chartPromises['1Y'],
        chartPromises['MAX'],
      ]);

      const [chart1D, chart5D, chart1M, chart3M, chart6M, chart1Y, chartMAX] =
        charts;

      if (!quote) {
        throw new Error(`No data found for ticker: ${ticker}`);
      }

      let comparisonData: any = null;
      if (params.comparisonNames.length > 0) {
        const comparisonPromises = params.comparisonNames
          .slice(0, 3)
          .map(async (compName) => {
            try {
              const compFindings = await yf.search(compName);

              if (compFindings.quotes.length === 0) return null;

              const compTicker = compFindings.quotes[0].symbol as string;
              const compQuote = await yf.quote(compTicker);
              const compCharts = await Promise.all([
                yf
                  .chart(compTicker, {
                    period1: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000),
                    period2: new Date(),
                    interval: '5m',
                  })
                  .catch(() => null),
                yf
                  .chart(compTicker, {
                    period1: new Date(Date.now() - 6 * 24 * 60 * 60 * 1000),
                    period2: new Date(),
                    interval: '15m',
                  })
                  .catch(() => null),
                yf
                  .chart(compTicker, {
                    period1: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000),
                    interval: '1d',
                  })
                  .catch(() => null),
                yf
                  .chart(compTicker, {
                    period1: new Date(Date.now() - 90 * 24 * 60 * 60 * 1000),
                    interval: '1d',
                  })
                  .catch(() => null),
                yf
                  .chart(compTicker, {
                    period1: new Date(Date.now() - 180 * 24 * 60 * 60 * 1000),
                    interval: '1d',
                  })
                  .catch(() => null),
                yf
                  .chart(compTicker, {
                    period1: new Date(Date.now() - 365 * 24 * 60 * 60 * 1000),
                    interval: '1d',
                  })
                  .catch(() => null),
                yf
                  .chart(compTicker, {
                    period1: new Date(
                      Date.now() - 10 * 365 * 24 * 60 * 60 * 1000,
                    ),
                    interval: '1wk',
                  })
                  .catch(() => null),
              ]);
              return {
                ticker: compTicker,
                name: compQuote.shortName || compTicker,
                charts: compCharts,
              };
            } catch (error) {
              console.error(
                `Failed to fetch comparison ticker ${compName}:`,
                error,
              );
              return null;
            }
          });
        const compResults = await Promise.all(comparisonPromises);
        comparisonData = compResults.filter((r) => r !== null);
      }

      const stockData = {
        symbol: quote.symbol,
        shortName: quote.shortName || quote.longName || ticker,
        longName: quote.longName,
        exchange: quote.fullExchangeName || quote.exchange,
        currency: quote.currency,
        quoteType: quote.quoteType,

        marketState: quote.marketState,
        regularMarketTime: quote.regularMarketTime,
        postMarketTime: quote.postMarketTime,
        preMarketTime: quote.preMarketTime,

        regularMarketPrice: quote.regularMarketPrice,
        regularMarketChange: quote.regularMarketChange,
        regularMarketChangePercent: quote.regularMarketChangePercent,
        regularMarketPreviousClose: quote.regularMarketPreviousClose,
        regularMarketOpen: quote.regularMarketOpen,
        regularMarketDayHigh: quote.regularMarketDayHigh,
        regularMarketDayLow: quote.regularMarketDayLow,

        postMarketPrice: quote.postMarketPrice,
        postMarketChange: quote.postMarketChange,
        postMarketChangePercent: quote.postMarketChangePercent,
        preMarketPrice: quote.preMarketPrice,
        preMarketChange: quote.preMarketChange,
        preMarketChangePercent: quote.preMarketChangePercent,

        regularMarketVolume: quote.regularMarketVolume,
        averageDailyVolume3Month: quote.averageDailyVolume3Month,
        averageDailyVolume10Day: quote.averageDailyVolume10Day,
        bid: quote.bid,
        bidSize: quote.bidSize,
        ask: quote.ask,
        askSize: quote.askSize,

        fiftyTwoWeekLow: quote.fiftyTwoWeekLow,
        fiftyTwoWeekHigh: quote.fiftyTwoWeekHigh,
        fiftyTwoWeekChange: quote.fiftyTwoWeekChange,
        fiftyTwoWeekChangePercent: quote.fiftyTwoWeekChangePercent,

        marketCap: quote.marketCap,
        trailingPE: quote.trailingPE,
        forwardPE: quote.forwardPE,
        priceToBook: quote.priceToBook,
        bookValue: quote.bookValue,
        earningsPerShare: quote.epsTrailingTwelveMonths,
        epsForward: quote.epsForward,

        dividendRate: quote.dividendRate,
        dividendYield: quote.dividendYield,
        exDividendDate: quote.exDividendDate,
        trailingAnnualDividendRate: quote.trailingAnnualDividendRate,
        trailingAnnualDividendYield: quote.trailingAnnualDividendYield,

        beta: quote.beta,

        fiftyDayAverage: quote.fiftyDayAverage,
        fiftyDayAverageChange: quote.fiftyDayAverageChange,
        fiftyDayAverageChangePercent: quote.fiftyDayAverageChangePercent,
        twoHundredDayAverage: quote.twoHundredDayAverage,
        twoHundredDayAverageChange: quote.twoHundredDayAverageChange,
        twoHundredDayAverageChangePercent:
          quote.twoHundredDayAverageChangePercent,

        sector: quote.sector,
        industry: quote.industry,
        website: quote.website,

        chartData: {
          '1D': chart1D
            ? {
                timestamps: chart1D.quotes.map((q: any) => q.date.getTime()),
                prices: chart1D.quotes.map((q: any) => q.close),
              }
            : null,
          '5D': chart5D
            ? {
                timestamps: chart5D.quotes.map((q: any) => q.date.getTime()),
                prices: chart5D.quotes.map((q: any) => q.close),
              }
            : null,
          '1M': chart1M
            ? {
                timestamps: chart1M.quotes.map((q: any) => q.date.getTime()),
                prices: chart1M.quotes.map((q: any) => q.close),
              }
            : null,
          '3M': chart3M
            ? {
                timestamps: chart3M.quotes.map((q: any) => q.date.getTime()),
                prices: chart3M.quotes.map((q: any) => q.close),
              }
            : null,
          '6M': chart6M
            ? {
                timestamps: chart6M.quotes.map((q: any) => q.date.getTime()),
                prices: chart6M.quotes.map((q: any) => q.close),
              }
            : null,
          '1Y': chart1Y
            ? {
                timestamps: chart1Y.quotes.map((q: any) => q.date.getTime()),
                prices: chart1Y.quotes.map((q: any) => q.close),
              }
            : null,
          MAX: chartMAX
            ? {
                timestamps: chartMAX.quotes.map((q: any) => q.date.getTime()),
                prices: chartMAX.quotes.map((q: any) => q.close),
              }
            : null,
        },
        comparisonData: comparisonData
          ? comparisonData.map((comp: any) => ({
              ticker: comp.ticker,
              name: comp.name,
              chartData: {
                '1D': comp.charts[0]
                  ? {
                      timestamps: comp.charts[0].quotes.map((q: any) =>
                        q.date.getTime(),
                      ),
                      prices: comp.charts[0].quotes.map((q: any) => q.close),
                    }
                  : null,
                '5D': comp.charts[1]
                  ? {
                      timestamps: comp.charts[1].quotes.map((q: any) =>
                        q.date.getTime(),
                      ),
                      prices: comp.charts[1].quotes.map((q: any) => q.close),
                    }
                  : null,
                '1M': comp.charts[2]
                  ? {
                      timestamps: comp.charts[2].quotes.map((q: any) =>
                        q.date.getTime(),
                      ),
                      prices: comp.charts[2].quotes.map((q: any) => q.close),
                    }
                  : null,
                '3M': comp.charts[3]
                  ? {
                      timestamps: comp.charts[3].quotes.map((q: any) =>
                        q.date.getTime(),
                      ),
                      prices: comp.charts[3].quotes.map((q: any) => q.close),
                    }
                  : null,
                '6M': comp.charts[4]
                  ? {
                      timestamps: comp.charts[4].quotes.map((q: any) =>
                        q.date.getTime(),
                      ),
                      prices: comp.charts[4].quotes.map((q: any) => q.close),
                    }
                  : null,
                '1Y': comp.charts[5]
                  ? {
                      timestamps: comp.charts[5].quotes.map((q: any) =>
                        q.date.getTime(),
                      ),
                      prices: comp.charts[5].quotes.map((q: any) => q.close),
                    }
                  : null,
                MAX: comp.charts[6]
                  ? {
                      timestamps: comp.charts[6].quotes.map((q: any) =>
                        q.date.getTime(),
                      ),
                      prices: comp.charts[6].quotes.map((q: any) => q.close),
                    }
                  : null,
              },
            }))
          : null,
      };

      return {
        type: 'stock',
        llmContext: `Current price of ${stockData.shortName} (${stockData.symbol}) is ${stockData.regularMarketPrice} ${stockData.currency}. Other details: ${JSON.stringify(
          {
            marketState: stockData.marketState,
            regularMarketChange: stockData.regularMarketChange,
            regularMarketChangePercent: stockData.regularMarketChangePercent,
            marketCap: stockData.marketCap,
            peRatio: stockData.trailingPE,
            dividendYield: stockData.dividendYield,
          },
        )}`,
        data: stockData,
      };
    } catch (error: any) {
      return {
        type: 'stock',
        llmContext: 'Failed to fetch stock data.',
        data: {
          error: `Error fetching stock data: ${error.message || error}`,
          ticker: params.name,
        },
      };
    }
  },
};

export default stockWidget;
```

## File: `src/lib/agents/search/widgets/weatherWidget.ts`
```typescript
import z from 'zod';
import { Widget } from '../types';
import formatChatHistoryAsString from '@/lib/utils/formatHistory';

const schema = z.object({
  location: z
    .string()
    .describe(
      'Human-readable location name (e.g., "New York, NY, USA", "London, UK"). Use this OR lat/lon coordinates, never both. Leave empty string if providing coordinates.',
    ),
  lat: z
    .number()
    .describe(
      'Latitude coordinate in decimal degrees (e.g., 40.7128). Only use when location name is empty.',
    ),
  lon: z
    .number()
    .describe(
      'Longitude coordinate in decimal degrees (e.g., -74.0060). Only use when location name is empty.',
    ),
  notPresent: z
    .boolean()
    .describe('Whether there is no need for the weather widget.'),
});

const systemPrompt = `
<role>
You are a location extractor for weather queries. You will receive a user follow up and a conversation history.
Your task is to determine if the user is asking about weather and extract the location they want weather for.
</role>

<instructions>
- If the user is asking about weather, extract the location name OR coordinates (never both).
- If using location name, set lat and lon to 0.
- If using coordinates, set location to empty string.
- If you cannot determine a valid location or the query is not weather-related, set notPresent to true.
- Location should be specific (city, state/region, country) for best results.
- You have to give the location so that it can be used to fetch weather data, it cannot be left empty unless notPresent is true.
- Make sure to infer short forms of location names (e.g., "NYC" -> "New York City", "LA" -> "Los Angeles").
</instructions>

<output_format>
You must respond in the following JSON format without any extra text, explanations or filler sentences:
{
  "location": string,
  "lat": number,
  "lon": number,
  "notPresent": boolean
}
</output_format>
`;

const weatherWidget: Widget = {
  type: 'weatherWidget',
  shouldExecute: (classification) =>
    classification.classification.showWeatherWidget,
  execute: async (input) => {
    const output = await input.llm.generateObject<typeof schema>({
      messages: [
        {
          role: 'system',
          content: systemPrompt,
        },
        {
          role: 'user',
          content: `<conversation_history>\n${formatChatHistoryAsString(input.chatHistory)}\n</conversation_history>\n<user_follow_up>\n${input.followUp}\n</user_follow_up>`,
        },
      ],
      schema,
    });

    if (output.notPresent) {
      return;
    }

    const params = output;

    try {
      if (
        params.location === '' &&
        (params.lat === undefined || params.lon === undefined)
      ) {
        throw new Error(
          'Either location name or both latitude and longitude must be provided.',
        );
      }

      if (params.location !== '') {
        const openStreetMapUrl = `https://nominatim.openstreetmap.org/search?q=${encodeURIComponent(params.location)}&format=json&limit=1`;

        const locationRes = await fetch(openStreetMapUrl, {
          headers: {
            'User-Agent': 'Vane',
            'Content-Type': 'application/json',
          },
        });

        const data = await locationRes.json();

        const location = data[0];

        if (!location) {
          throw new Error(
            `Could not find coordinates for location: ${params.location}`,
          );
        }

        const weatherRes = await fetch(
          `https://api.open-meteo.com/v1/forecast?latitude=${location.lat}&longitude=${location.lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=temperature_2m,precipitation_probability,precipitation,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max&timezone=auto&forecast_days=7`,
          {
            headers: {
              'User-Agent': 'Vane',
              'Content-Type': 'application/json',
            },
          },
        );

        const weatherData = await weatherRes.json();

        return {
          type: 'weather',
          llmContext: `Weather in ${params.location} is ${JSON.stringify(weatherData.current)}`,
          data: {
            location: params.location,
            latitude: location.lat,
            longitude: location.lon,
            current: weatherData.current,
            hourly: {
              time: weatherData.hourly.time.slice(0, 24),
              temperature_2m: weatherData.hourly.temperature_2m.slice(0, 24),
              precipitation_probability:
                weatherData.hourly.precipitation_probability.slice(0, 24),
              precipitation: weatherData.hourly.precipitation.slice(0, 24),
              weather_code: weatherData.hourly.weather_code.slice(0, 24),
            },
            daily: weatherData.daily,
            timezone: weatherData.timezone,
          },
        };
      } else if (params.lat !== undefined && params.lon !== undefined) {
        const [weatherRes, locationRes] = await Promise.all([
          fetch(
            `https://api.open-meteo.com/v1/forecast?latitude=${params.lat}&longitude=${params.lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=temperature_2m,precipitation_probability,precipitation,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max&timezone=auto&forecast_days=7`,
            {
              headers: {
                'User-Agent': 'Vane',
                'Content-Type': 'application/json',
              },
            },
          ),
          fetch(
            `https://nominatim.openstreetmap.org/reverse?lat=${params.lat}&lon=${params.lon}&format=json`,
            {
              headers: {
                'User-Agent': 'Vane',
                'Content-Type': 'application/json',
              },
            },
          ),
        ]);

        const weatherData = await weatherRes.json();
        const locationData = await locationRes.json();

        return {
          type: 'weather',
          llmContext: `Weather in ${locationData.display_name} is ${JSON.stringify(weatherData.current)}`,
          data: {
            location: locationData.display_name,
            latitude: params.lat,
            longitude: params.lon,
            current: weatherData.current,
            hourly: {
              time: weatherData.hourly.time.slice(0, 24),
              temperature_2m: weatherData.hourly.temperature_2m.slice(0, 24),
              precipitation_probability:
                weatherData.hourly.precipitation_probability.slice(0, 24),
              precipitation: weatherData.hourly.precipitation.slice(0, 24),
              weather_code: weatherData.hourly.weather_code.slice(0, 24),
            },
            daily: weatherData.daily,
            timezone: weatherData.timezone,
          },
        };
      }

      return {
        type: 'weather',
        llmContext: 'No valid location or coordinates provided.',
        data: null,
      };
    } catch (err) {
      return {
        type: 'weather',
        llmContext: 'Failed to fetch weather data.',
        data: {
          error: `Error fetching weather data: ${err}`,
        },
      };
    }
  },
};
export default weatherWidget;
```

## File: `src/lib/agents/suggestions/index.ts`
```typescript
import formatChatHistoryAsString from '@/lib/utils/formatHistory';
import { suggestionGeneratorPrompt } from '@/lib/prompts/suggestions';
import { ChatTurnMessage } from '@/lib/types';
import z from 'zod';
import BaseLLM from '@/lib/models/base/llm';

type SuggestionGeneratorInput = {
  chatHistory: ChatTurnMessage[];
};

const schema = z.object({
  suggestions: z
    .array(z.string())
    .describe('List of suggested questions or prompts'),
});

const generateSuggestions = async (
  input: SuggestionGeneratorInput,
  llm: BaseLLM<any>,
) => {
  const res = await llm.generateObject<typeof schema>({
    messages: [
      {
        role: 'system',
        content: suggestionGeneratorPrompt,
      },
      {
        role: 'user',
        content: `<chat_history>\n${formatChatHistoryAsString(input.chatHistory)}\n</chat_history>`,
      },
    ],
    schema,
  });

  return res.suggestions;
};

export default generateSuggestions;
```

## File: `src/lib/config/clientRegistry.ts`
```typescript
'use client';

const getClientConfig = (key: string, defaultVal?: any) => {
  return localStorage.getItem(key) ?? defaultVal ?? undefined;
};

export const getTheme = () => getClientConfig('theme', 'dark');

export const getAutoMediaSearch = () =>
  getClientConfig('autoMediaSearch', 'true') === 'true';

export const getSystemInstructions = () =>
  getClientConfig('systemInstructions', '');

export const getShowWeatherWidget = () =>
  getClientConfig('showWeatherWidget', 'true') === 'true';

export const getShowNewsWidget = () =>
  getClientConfig('showNewsWidget', 'true') === 'true';

export const getMeasurementUnit = () => {
  const value =
    getClientConfig('measureUnit') ??
    getClientConfig('measurementUnit', 'metric');

  if (typeof value !== 'string') return 'metric';

  return value.toLowerCase();
};
```

## File: `src/lib/config/index.ts`
```typescript
import path from 'node:path';
import fs from 'fs';
import { Config, ConfigModelProvider, UIConfigSections } from './types';
import { hashObj } from '../utils/hash';
import { getModelProvidersUIConfigSection } from '../models/providers';

class ConfigManager {
  configPath: string = path.join(
    process.env.DATA_DIR || process.cwd(),
    '/data/config.json',
  );
  configVersion = 1;
  currentConfig: Config = {
    version: this.configVersion,
    setupComplete: false,
    preferences: {},
    personalization: {},
    modelProviders: [],
    search: {
      searxngURL: '',
    },
  };
  uiConfigSections: UIConfigSections = {
    preferences: [
      {
        name: 'Theme',
        key: 'theme',
        type: 'select',
        options: [
          {
            name: 'Light',
            value: 'light',
          },
          {
            name: 'Dark',
            value: 'dark',
          },
        ],
        required: false,
        description: 'Choose between light and dark layouts for the app.',
        default: 'dark',
        scope: 'client',
      },
      {
        name: 'Measurement Unit',
        key: 'measureUnit',
        type: 'select',
        options: [
          {
            name: 'Imperial',
            value: 'Imperial',
          },
          {
            name: 'Metric',
            value: 'Metric',
          },
        ],
        required: false,
        description: 'Choose between Metric  and Imperial measurement unit.',
        default: 'Metric',
        scope: 'client',
      },
      {
        name: 'Auto video & image search',
        key: 'autoMediaSearch',
        type: 'switch',
        required: false,
        description: 'Automatically search for relevant images and videos.',
        default: true,
        scope: 'client',
      },
      {
        name: 'Show weather widget',
        key: 'showWeatherWidget',
        type: 'switch',
        required: false,
        description: 'Display the weather card on the home screen.',
        default: true,
        scope: 'client',
      },
      {
        name: 'Show news widget',
        key: 'showNewsWidget',
        type: 'switch',
        required: false,
        description: 'Display the recent news card on the home screen.',
        default: true,
        scope: 'client',
      },
    ],
    personalization: [
      {
        name: 'System Instructions',
        key: 'systemInstructions',
        type: 'textarea',
        required: false,
        description: 'Add custom behavior or tone for the model.',
        placeholder:
          'e.g., "Respond in a friendly and concise tone" or "Use British English and format answers as bullet points."',
        scope: 'client',
      },
    ],
    modelProviders: [],
    search: [
      {
        name: 'SearXNG URL',
        key: 'searxngURL',
        type: 'string',
        required: false,
        description: 'The URL of your SearXNG instance',
        placeholder: 'http://localhost:4000',
        default: '',
        scope: 'server',
        env: 'SEARXNG_API_URL',
      },
    ],
  };

  constructor() {
    this.initialize();
  }

  private initialize() {
    this.initializeConfig();
    this.initializeFromEnv();
  }

  private saveConfig() {
    fs.writeFileSync(
      this.configPath,
      JSON.stringify(this.currentConfig, null, 2),
    );
  }

  private initializeConfig() {
    const exists = fs.existsSync(this.configPath);
    if (!exists) {
      fs.writeFileSync(
        this.configPath,
        JSON.stringify(this.currentConfig, null, 2),
      );
    } else {
      try {
        this.currentConfig = JSON.parse(
          fs.readFileSync(this.configPath, 'utf-8'),
        );
      } catch (err) {
        if (err instanceof SyntaxError) {
          console.error(
            `Error parsing config file at ${this.configPath}:`,
            err,
          );
          console.log(
            'Loading default config and overwriting the existing file.',
          );
          fs.writeFileSync(
            this.configPath,
            JSON.stringify(this.currentConfig, null, 2),
          );
          return;
        } else {
          console.log('Unknown error reading config file:', err);
        }
      }

      this.currentConfig = this.migrateConfig(this.currentConfig);
    }
  }

  private migrateConfig(config: Config): Config {
    /* TODO: Add migrations */
    return config;
  }

  private initializeFromEnv() {
    /* providers section*/
    const providerConfigSections = getModelProvidersUIConfigSection();

    this.uiConfigSections.modelProviders = providerConfigSections;

    const newProviders: ConfigModelProvider[] = [];

    providerConfigSections.forEach((provider) => {
      const newProvider: ConfigModelProvider & { required?: string[] } = {
        id: crypto.randomUUID(),
        name: `${provider.name}`,
        type: provider.key,
        chatModels: [],
        embeddingModels: [],
        config: {},
        required: [],
        hash: '',
      };

      provider.fields.forEach((field) => {
        newProvider.config[field.key] =
          process.env[field.env!] ||
          field.default ||
          ''; /* Env var must exist for providers */

        if (field.required) newProvider.required?.push(field.key);
      });

      let configured = true;

      newProvider.required?.forEach((r) => {
        if (!newProvider.config[r]) {
          configured = false;
        }
      });

      if (configured) {
        const hash = hashObj(newProvider.config);
        newProvider.hash = hash;
        delete newProvider.required;

        const exists = this.currentConfig.modelProviders.find(
          (p) => p.hash === hash,
        );

        if (!exists) {
          newProviders.push(newProvider);
        }
      }
    });

    this.currentConfig.modelProviders.push(...newProviders);

    /* search section */
    this.uiConfigSections.search.forEach((f) => {
      if (f.env && !this.currentConfig.search[f.key]) {
        this.currentConfig.search[f.key] =
          process.env[f.env] ?? f.default ?? '';
      }
    });

    this.saveConfig();
  }

  public getConfig(key: string, defaultValue?: any): any {
    const nested = key.split('.');
    let obj: any = this.currentConfig;

    for (let i = 0; i < nested.length; i++) {
      const part = nested[i];
      if (obj == null) return defaultValue;

      obj = obj[part];
    }

    return obj === undefined ? defaultValue : obj;
  }

  public updateConfig(key: string, val: any) {
    const parts = key.split('.');
    if (parts.length === 0) return;

    let target: any = this.currentConfig;
    for (let i = 0; i < parts.length - 1; i++) {
      const part = parts[i];
      if (target[part] === null || typeof target[part] !== 'object') {
        target[part] = {};
      }

      target = target[part];
    }

    const finalKey = parts[parts.length - 1];
    target[finalKey] = val;

    this.saveConfig();
  }

  public addModelProvider(type: string, name: string, config: any) {
    const newModelProvider: ConfigModelProvider = {
      id: crypto.randomUUID(),
      name,
      type,
      config,
      chatModels: [],
      embeddingModels: [],
      hash: hashObj(config),
    };

    this.currentConfig.modelProviders.push(newModelProvider);
    this.saveConfig();

    return newModelProvider;
  }

  public removeModelProvider(id: string) {
    const index = this.currentConfig.modelProviders.findIndex(
      (p) => p.id === id,
    );

    if (index === -1) return;

    this.currentConfig.modelProviders =
      this.currentConfig.modelProviders.filter((p) => p.id !== id);

    this.saveConfig();
  }

  public async updateModelProvider(id: string, name: string, config: any) {
    const provider = this.currentConfig.modelProviders.find((p) => {
      return p.id === id;
    });

    if (!provider) throw new Error('Provider not found');

    provider.name = name;
    provider.config = config;

    this.saveConfig();

    return provider;
  }

  public addProviderModel(
    providerId: string,
    type: 'embedding' | 'chat',
    model: any,
  ) {
    const provider = this.currentConfig.modelProviders.find(
      (p) => p.id === providerId,
    );

    if (!provider) throw new Error('Invalid provider id');

    delete model.type;

    if (type === 'chat') {
      provider.chatModels.push(model);
    } else {
      provider.embeddingModels.push(model);
    }

    this.saveConfig();

    return model;
  }

  public removeProviderModel(
    providerId: string,
    type: 'embedding' | 'chat',
    modelKey: string,
  ) {
    const provider = this.currentConfig.modelProviders.find(
      (p) => p.id === providerId,
    );

    if (!provider) throw new Error('Invalid provider id');

    if (type === 'chat') {
      provider.chatModels = provider.chatModels.filter(
        (m) => m.key !== modelKey,
      );
    } else {
      provider.embeddingModels = provider.embeddingModels.filter(
        (m) => m.key != modelKey,
      );
    }

    this.saveConfig();
  }

  public isSetupComplete() {
    return this.currentConfig.setupComplete;
  }

  public markSetupComplete() {
    if (!this.currentConfig.setupComplete) {
      this.currentConfig.setupComplete = true;
    }

    this.saveConfig();
  }

  public getUIConfigSections(): UIConfigSections {
    return this.uiConfigSections;
  }

  public getCurrentConfig(): Config {
    return JSON.parse(JSON.stringify(this.currentConfig));
  }
}

const configManager = new ConfigManager();

export default configManager;
```

## File: `src/lib/config/serverRegistry.ts`
```typescript
import configManager from './index';
import { ConfigModelProvider } from './types';

export const getConfiguredModelProviders = (): ConfigModelProvider[] => {
  return configManager.getConfig('modelProviders', []);
};

export const getConfiguredModelProviderById = (
  id: string,
): ConfigModelProvider | undefined => {
  return getConfiguredModelProviders().find((p) => p.id === id) ?? undefined;
};

export const getSearxngURL = () =>
  configManager.getConfig('search.searxngURL', '');
```

## File: `src/lib/config/types.ts`
```typescript
import { Model } from '../models/types';

type BaseUIConfigField = {
  name: string;
  key: string;
  required: boolean;
  description: string;
  scope: 'client' | 'server';
  env?: string;
};

type StringUIConfigField = BaseUIConfigField & {
  type: 'string';
  placeholder?: string;
  default?: string;
};

type SelectUIConfigFieldOptions = {
  name: string;
  value: string;
};

type SelectUIConfigField = BaseUIConfigField & {
  type: 'select';
  default?: string;
  options: SelectUIConfigFieldOptions[];
};

type PasswordUIConfigField = BaseUIConfigField & {
  type: 'password';
  placeholder?: string;
  default?: string;
};

type TextareaUIConfigField = BaseUIConfigField & {
  type: 'textarea';
  placeholder?: string;
  default?: string;
};

type SwitchUIConfigField = BaseUIConfigField & {
  type: 'switch';
  default?: boolean;
};

type UIConfigField =
  | StringUIConfigField
  | SelectUIConfigField
  | PasswordUIConfigField
  | TextareaUIConfigField
  | SwitchUIConfigField;

type ConfigModelProvider = {
  id: string;
  name: string;
  type: string;
  chatModels: Model[];
  embeddingModels: Model[];
  config: { [key: string]: any };
  hash: string;
};

type Config = {
  version: number;
  setupComplete: boolean;
  preferences: {
    [key: string]: any;
  };
  personalization: {
    [key: string]: any;
  };
  modelProviders: ConfigModelProvider[];
  search: {
    [key: string]: any;
  };
};

type EnvMap = {
  [key: string]: {
    fieldKey: string;
    providerKey: string;
  };
};

type ModelProviderUISection = {
  name: string;
  key: string;
  fields: UIConfigField[];
};

type UIConfigSections = {
  preferences: UIConfigField[];
  personalization: UIConfigField[];
  modelProviders: ModelProviderUISection[];
  search: UIConfigField[];
};

export type {
  UIConfigField,
  Config,
  EnvMap,
  UIConfigSections,
  SelectUIConfigField,
  StringUIConfigField,
  ModelProviderUISection,
  ConfigModelProvider,
  TextareaUIConfigField,
  SwitchUIConfigField,
};
```

## File: `src/lib/db/index.ts`
```typescript
import { drizzle } from 'drizzle-orm/better-sqlite3';
import Database from 'better-sqlite3';
import * as schema from './schema';
import path from 'path';

const DATA_DIR = process.env.DATA_DIR || process.cwd();
const sqlite = new Database(path.join(DATA_DIR, './data/db.sqlite'));
const db = drizzle(sqlite, {
  schema: schema,
});

export default db;
```

## File: `src/lib/db/migrate.ts`
```typescript
import Database from 'better-sqlite3';
import path from 'path';
import fs from 'fs';

const DATA_DIR = process.env.DATA_DIR || process.cwd();
const dbPath = path.join(DATA_DIR, './data/db.sqlite');

const db = new Database(dbPath);

const migrationsFolder = path.join(DATA_DIR, 'drizzle');

db.exec(`
  CREATE TABLE IF NOT EXISTS ran_migrations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    run_on DATETIME DEFAULT CURRENT_TIMESTAMP
  );
`);

function sanitizeSql(content: string) {
  const statements = content
    .split(/--> statement-breakpoint/g)
    .map((stmt) =>
      stmt
        .split(/\r?\n/)
        .filter((l) => !l.trim().startsWith('-->'))
        .join('\n')
        .trim(),
    )
    .filter((stmt) => stmt.length > 0);

  return statements;
}

fs.readdirSync(migrationsFolder)
  .filter((f) => f.endsWith('.sql'))
  .sort()
  .forEach((file) => {
    const filePath = path.join(migrationsFolder, file);
    let content = fs.readFileSync(filePath, 'utf-8');
    const statements = sanitizeSql(content);

    const migrationName = file.split('_')[0] || file;

    const already = db
      .prepare('SELECT 1 FROM ran_migrations WHERE name = ?')
      .get(migrationName);

    if (already) {
      console.log(`Skipping already-applied migration: ${file}`);
      return;
    }

    try {
      if (migrationName === '0001') {
        const messages = db
          .prepare(
            'SELECT id, type, metadata, content, chatId, messageId FROM messages',
          )
          .all();

        db.exec(`
                    CREATE TABLE IF NOT EXISTS messages_with_sources (
                        id INTEGER PRIMARY KEY,
                        type TEXT NOT NULL,
                        chatId TEXT NOT NULL,
                        createdAt TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        messageId TEXT NOT NULL,
                        content TEXT,
                        sources TEXT DEFAULT '[]'
                    );
                `);

        const insertMessage = db.prepare(`
                    INSERT INTO messages_with_sources (type, chatId, createdAt, messageId, content, sources)
                    VALUES (?, ?, ?, ?, ?, ?)
                `);

        messages.forEach((msg: any) => {
          while (typeof msg.metadata === 'string') {
            msg.metadata = JSON.parse(msg.metadata || '{}');
          }
          if (msg.type === 'user') {
            insertMessage.run(
              'user',
              msg.chatId,
              msg.metadata['createdAt'],
              msg.messageId,
              msg.content,
              '[]',
            );
          } else if (msg.type === 'assistant') {
            insertMessage.run(
              'assistant',
              msg.chatId,
              msg.metadata['createdAt'],
              msg.messageId,
              msg.content,
              '[]',
            );
            const sources = msg.metadata['sources'] || '[]';
            if (sources && sources.length > 0) {
              insertMessage.run(
                'source',
                msg.chatId,
                msg.metadata['createdAt'],
                `${msg.messageId}-source`,
                '',
                JSON.stringify(sources),
              );
            }
          }
        });

        db.exec('DROP TABLE messages;');
        db.exec('ALTER TABLE messages_with_sources RENAME TO messages;');
      } else if (migrationName === '0002') {
        /* Migrate chat */
        db.exec(`
          CREATE TABLE IF NOT EXISTS chats_new (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            createdAt TEXT NOT NULL,
            sources TEXT DEFAULT '[]',
            files TEXT DEFAULT '[]'
          );
        `);

        const chats = db
          .prepare('SELECT id, title, createdAt, files FROM chats')
          .all();

        const insertChat = db.prepare(`
            INSERT INTO chats_new (id, title, createdAt, sources, files)
            VALUES (?, ?, ?, ?, ?)
          `);

        chats.forEach((chat: any) => {
          let files = chat.files;
          while (typeof files === 'string') {
            files = JSON.parse(files || '[]');
          }

          insertChat.run(
            chat.id,
            chat.title,
            chat.createdAt,
            '["web"]',
            JSON.stringify(files),
          );
        });

        db.exec('DROP TABLE chats;');
        db.exec('ALTER TABLE chats_new RENAME TO chats;');

        /* Migrate messages */

        db.exec(`
          CREATE TABLE IF NOT EXISTS messages_new (
            id INTEGER PRIMARY KEY,
            messageId TEXT NOT NULL,
            chatId TEXT NOT NULL,
            backendId TEXT NOT NULL,
            query TEXT NOT NULL,
            createdAt TEXT NOT NULL,
            responseBlocks TEXT DEFAULT '[]',
            status TEXT DEFAULT 'answering'
          );
        `);

        const messages = db
          .prepare(
            'SELECT id, messageId, chatId, type, content, createdAt, sources FROM messages ORDER BY id ASC',
          )
          .all();

        const insertMessage = db.prepare(`
            INSERT INTO messages_new (messageId, chatId, backendId, query, createdAt, responseBlocks, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
          `);

        let currentMessageData: {
          sources?: any[];
          response?: string;
          query?: string;
          messageId?: string;
          chatId?: string;
          createdAt?: string;
        } = {};
        let lastCompleted = true;

        messages.forEach((msg: any) => {
          if (msg.type === 'user' && lastCompleted) {
            currentMessageData = {};
            currentMessageData.messageId = msg.messageId;
            currentMessageData.chatId = msg.chatId;
            currentMessageData.query = msg.content;
            currentMessageData.createdAt = msg.createdAt;
            lastCompleted = false;
          } else if (msg.type === 'source' && !lastCompleted) {
            let sources = msg.sources;

            while (typeof sources === 'string') {
              sources = JSON.parse(sources || '[]');
            }

            currentMessageData.sources = sources;
          } else if (msg.type === 'assistant' && !lastCompleted) {
            currentMessageData.response = msg.content;
            insertMessage.run(
              currentMessageData.messageId,
              currentMessageData.chatId,
              `${currentMessageData.messageId}-backend`,
              currentMessageData.query,
              currentMessageData.createdAt,
              JSON.stringify([
                {
                  id: crypto.randomUUID(),
                  type: 'text',
                  data: currentMessageData.response || '',
                },
                ...(currentMessageData.sources &&
                currentMessageData.sources.length > 0
                  ? [
                      {
                        id: crypto.randomUUID(),
                        type: 'source',
                        data: currentMessageData.sources,
                      },
                    ]
                  : []),
              ]),
              'completed',
            );

            lastCompleted = true;
          } else if (msg.type === 'user' && !lastCompleted) {
            /* Message wasn't completed so we'll just create the record with empty response */
            insertMessage.run(
              currentMessageData.messageId,
              currentMessageData.chatId,
              `${currentMessageData.messageId}-backend`,
              currentMessageData.query,
              currentMessageData.createdAt,
              JSON.stringify([
                {
                  id: crypto.randomUUID(),
                  type: 'text',
                  data: '',
                },
                ...(currentMessageData.sources &&
                currentMessageData.sources.length > 0
                  ? [
                      {
                        id: crypto.randomUUID(),
                        type: 'source',
                        data: currentMessageData.sources,
                      },
                    ]
                  : []),
              ]),
              'completed',
            );

            lastCompleted = true;
          }
        });

        db.exec('DROP TABLE messages;');
        db.exec('ALTER TABLE messages_new RENAME TO messages;');
      } else {
        // Execute each statement separately
        statements.forEach((stmt) => {
          if (stmt.trim()) {
            db.exec(stmt);
          }
        });
      }

      db.prepare('INSERT OR IGNORE INTO ran_migrations (name) VALUES (?)').run(
        migrationName,
      );
      console.log(`Applied migration: ${file}`);
    } catch (err) {
      console.error(`Failed to apply migration ${file}:`, err);
      throw err;
    }
  });
```

## File: `src/lib/db/schema.ts`
```typescript
import { sql } from 'drizzle-orm';
import { text, integer, sqliteTable } from 'drizzle-orm/sqlite-core';
import { Block } from '../types';
import { SearchSources } from '../agents/search/types';

export const messages = sqliteTable('messages', {
  id: integer('id').primaryKey(),
  messageId: text('messageId').notNull(),
  chatId: text('chatId').notNull(),
  backendId: text('backendId').notNull(),
  query: text('query').notNull(),
  createdAt: text('createdAt').notNull(),
  responseBlocks: text('responseBlocks', { mode: 'json' })
    .$type<Block[]>()
    .default(sql`'[]'`),
  status: text({ enum: ['answering', 'completed', 'error'] }).default(
    'answering',
  ),
});

interface DBFile {
  name: string;
  fileId: string;
}

export const chats = sqliteTable('chats', {
  id: text('id').primaryKey(),
  title: text('title').notNull(),
  createdAt: text('createdAt').notNull(),
  sources: text('sources', {
    mode: 'json',
  })
    .$type<SearchSources[]>()
    .default(sql`'[]'`),
  files: text('files', { mode: 'json' })
    .$type<DBFile[]>()
    .default(sql`'[]'`),
});
```

## File: `src/lib/hooks/useChat.tsx`
```tsx
'use client';

import { Message } from '@/components/ChatWindow';
import { Block } from '@/lib/types';
import {
  createContext,
  useContext,
  useEffect,
  useMemo,
  useRef,
  useState,
} from 'react';
import crypto from 'crypto';
import { useParams, useSearchParams } from 'next/navigation';
import { toast } from 'sonner';
import { getSuggestions } from '../actions';
import { MinimalProvider } from '../models/types';
import { getAutoMediaSearch } from '../config/clientRegistry';
import { applyPatch } from 'rfc6902';
import { Widget } from '@/components/ChatWindow';

export type Section = {
  message: Message;
  widgets: Widget[];
  parsedTextBlocks: string[];
  speechMessage: string;
  thinkingEnded: boolean;
  suggestions?: string[];
};

type ChatContext = {
  messages: Message[];
  sections: Section[];
  chatHistory: [string, string][];
  files: File[];
  fileIds: string[];
  sources: string[];
  chatId: string | undefined;
  optimizationMode: string;
  isMessagesLoaded: boolean;
  loading: boolean;
  notFound: boolean;
  messageAppeared: boolean;
  isReady: boolean;
  hasError: boolean;
  chatModelProvider: ChatModelProvider;
  embeddingModelProvider: EmbeddingModelProvider;
  researchEnded: boolean;
  setResearchEnded: (ended: boolean) => void;
  setOptimizationMode: (mode: string) => void;
  setSources: (sources: string[]) => void;
  setFiles: (files: File[]) => void;
  setFileIds: (fileIds: string[]) => void;
  sendMessage: (
    message: string,
    messageId?: string,
    rewrite?: boolean,
  ) => Promise<void>;
  rewrite: (messageId: string) => void;
  setChatModelProvider: (provider: ChatModelProvider) => void;
  setEmbeddingModelProvider: (provider: EmbeddingModelProvider) => void;
};

export interface File {
  fileName: string;
  fileExtension: string;
  fileId: string;
}

interface ChatModelProvider {
  key: string;
  providerId: string;
}

interface EmbeddingModelProvider {
  key: string;
  providerId: string;
}

const checkConfig = async (
  setChatModelProvider: (provider: ChatModelProvider) => void,
  setEmbeddingModelProvider: (provider: EmbeddingModelProvider) => void,
  setIsConfigReady: (ready: boolean) => void,
  setHasError: (hasError: boolean) => void,
) => {
  try {
    let chatModelKey = localStorage.getItem('chatModelKey');
    let chatModelProviderId = localStorage.getItem('chatModelProviderId');
    let embeddingModelKey = localStorage.getItem('embeddingModelKey');
    let embeddingModelProviderId = localStorage.getItem(
      'embeddingModelProviderId',
    );

    const res = await fetch(`/api/providers`, {
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!res.ok) {
      throw new Error(
        `Provider fetching failed with status code ${res.status}`,
      );
    }

    const data = await res.json();
    const providers: MinimalProvider[] = data.providers;

    if (providers.length === 0) {
      throw new Error(
        'No chat model providers found, please configure them in the settings page.',
      );
    }

    const chatModelProvider =
      providers.find((p) => p.id === chatModelProviderId) ??
      providers.find((p) => p.chatModels.length > 0);

    if (!chatModelProvider) {
      throw new Error(
        'No chat models found, pleae configure them in the settings page.',
      );
    }

    chatModelProviderId = chatModelProvider.id;

    const chatModel =
      chatModelProvider.chatModels.find((m) => m.key === chatModelKey) ??
      chatModelProvider.chatModels[0];
    chatModelKey = chatModel.key;

    const embeddingModelProvider =
      providers.find((p) => p.id === embeddingModelProviderId) ??
      providers.find((p) => p.embeddingModels.length > 0);

    if (!embeddingModelProvider) {
      throw new Error(
        'No embedding models found, pleae configure them in the settings page.',
      );
    }

    embeddingModelProviderId = embeddingModelProvider.id;

    const embeddingModel =
      embeddingModelProvider.embeddingModels.find(
        (m) => m.key === embeddingModelKey,
      ) ?? embeddingModelProvider.embeddingModels[0];
    embeddingModelKey = embeddingModel.key;

    localStorage.setItem('chatModelKey', chatModelKey);
    localStorage.setItem('chatModelProviderId', chatModelProviderId);
    localStorage.setItem('embeddingModelKey', embeddingModelKey);
    localStorage.setItem('embeddingModelProviderId', embeddingModelProviderId);

    setChatModelProvider({
      key: chatModelKey,
      providerId: chatModelProviderId,
    });

    setEmbeddingModelProvider({
      key: embeddingModelKey,
      providerId: embeddingModelProviderId,
    });

    setIsConfigReady(true);
  } catch (err: any) {
    console.error('An error occurred while checking the configuration:', err);
    toast.error(err.message);
    setIsConfigReady(false);
    setHasError(true);
  }
};

const loadMessages = async (
  chatId: string,
  setMessages: (messages: Message[]) => void,
  setIsMessagesLoaded: (loaded: boolean) => void,
  chatHistory: React.MutableRefObject<[string, string][]>,
  setSources: (sources: string[]) => void,
  setNotFound: (notFound: boolean) => void,
  setFiles: (files: File[]) => void,
  setFileIds: (fileIds: string[]) => void,
) => {
  const res = await fetch(`/api/chats/${chatId}`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  if (res.status === 404) {
    setNotFound(true);
    setIsMessagesLoaded(true);
    return;
  }

  const data = await res.json();

  const messages = data.messages as Message[];

  setMessages(messages);

  const history: [string, string][] = [];
  messages.forEach((msg) => {
    history.push(['human', msg.query]);

    const textBlocks = msg.responseBlocks
      .filter(
        (block): block is Block & { type: 'text' } => block.type === 'text',
      )
      .map((block) => block.data)
      .join('\n');

    if (textBlocks) {
      history.push(['assistant', textBlocks]);
    }
  });

  console.debug(new Date(), 'app:messages_loaded');

  if (messages.length > 0) {
    document.title = messages[0].query;
  }

  const files = data.chat.files.map((file: any) => {
    return {
      fileName: file.name,
      fileExtension: file.name.split('.').pop(),
      fileId: file.fileId,
    };
  });

  setFiles(files);
  setFileIds(files.map((file: File) => file.fileId));

  chatHistory.current = history;
  setSources(data.chat.sources);
  setIsMessagesLoaded(true);
};

export const chatContext = createContext<ChatContext>({
  chatHistory: [],
  chatId: '',
  fileIds: [],
  files: [],
  sources: [],
  hasError: false,
  isMessagesLoaded: false,
  isReady: false,
  loading: false,
  messageAppeared: false,
  messages: [],
  sections: [],
  notFound: false,
  optimizationMode: '',
  chatModelProvider: { key: '', providerId: '' },
  embeddingModelProvider: { key: '', providerId: '' },
  researchEnded: false,
  rewrite: () => {},
  sendMessage: async () => {},
  setFileIds: () => {},
  setFiles: () => {},
  setSources: () => {},
  setOptimizationMode: () => {},
  setChatModelProvider: () => {},
  setEmbeddingModelProvider: () => {},
  setResearchEnded: () => {},
});

export const ChatProvider = ({ children }: { children: React.ReactNode }) => {
  const params: { chatId: string } = useParams();

  const searchParams = useSearchParams();
  const initialMessage = searchParams.get('q');

  const [chatId, setChatId] = useState<string | undefined>(params.chatId);
  const [newChatCreated, setNewChatCreated] = useState(false);

  const [loading, setLoading] = useState(false);
  const [messageAppeared, setMessageAppeared] = useState(false);

  const [researchEnded, setResearchEnded] = useState(false);

  const chatHistory = useRef<[string, string][]>([]);
  const [messages, setMessages] = useState<Message[]>([]);

  const [files, setFiles] = useState<File[]>([]);
  const [fileIds, setFileIds] = useState<string[]>([]);

  const [sources, setSources] = useState<string[]>(['web']);
  const [optimizationMode, setOptimizationMode] = useState('speed');

  const [isMessagesLoaded, setIsMessagesLoaded] = useState(false);

  const [notFound, setNotFound] = useState(false);

  const [chatModelProvider, setChatModelProvider] = useState<ChatModelProvider>(
    {
      key: '',
      providerId: '',
    },
  );

  const [embeddingModelProvider, setEmbeddingModelProvider] =
    useState<EmbeddingModelProvider>({
      key: '',
      providerId: '',
    });

  const [isConfigReady, setIsConfigReady] = useState(false);
  const [hasError, setHasError] = useState(false);
  const [isReady, setIsReady] = useState(false);

  const messagesRef = useRef<Message[]>([]);

  const sections = useMemo<Section[]>(() => {
    return messages.map((msg) => {
      const textBlocks: string[] = [];
      let speechMessage = '';
      let thinkingEnded = false;
      let suggestions: string[] = [];

      const sourceBlocks = msg.responseBlocks.filter(
        (block): block is Block & { type: 'source' } => block.type === 'source',
      );
      const sources = sourceBlocks.flatMap((block) => block.data);

      const widgetBlocks = msg.responseBlocks
        .filter((b) => b.type === 'widget')
        .map((b) => b.data) as Widget[];

      msg.responseBlocks.forEach((block) => {
        if (block.type === 'text') {
          let processedText = block.data;
          const citationRegex = /\[([^\]]+)\]/g;
          const regex = /\[(\d+)\]/g;

          if (processedText.includes('<think>')) {
            const openThinkTag = processedText.match(/<think>/g)?.length || 0;
            const closeThinkTag =
              processedText.match(/<\/think>/g)?.length || 0;

            if (openThinkTag && !closeThinkTag) {
              processedText += '</think> <a> </a>';
            }
          }

          if (block.data.includes('</think>')) {
            thinkingEnded = true;
          }

          if (sources.length > 0) {
            processedText = processedText.replace(
              citationRegex,
              (_, capturedContent: string) => {
                const numbers = capturedContent
                  .split(',')
                  .map((numStr) => numStr.trim());

                const linksHtml = numbers
                  .map((numStr) => {
                    const number = parseInt(numStr);

                    if (isNaN(number) || number <= 0) {
                      return `[${numStr}]`;
                    }

                    const source = sources[number - 1];
                    const url = source?.metadata?.url;

                    if (url) {
                      return `<citation href="${url}">${numStr}</citation>`;
                    } else {
                      return ``;
                    }
                  })
                  .join('');

                return linksHtml;
              },
            );
            speechMessage += block.data.replace(regex, '');
          } else {
            processedText = processedText.replace(regex, '');
            speechMessage += block.data.replace(regex, '');
          }

          textBlocks.push(processedText);
        } else if (block.type === 'suggestion') {
          suggestions = block.data;
        }
      });

      return {
        message: msg,
        parsedTextBlocks: textBlocks,
        speechMessage,
        thinkingEnded,
        suggestions,
        widgets: widgetBlocks,
      };
    });
  }, [messages]);

  const isReconnectingRef = useRef(false);
  const handledMessageEndRef = useRef<Set<string>>(new Set());

  const checkReconnect = async () => {
    if (isReconnectingRef.current) return;

    setIsReady(true);
    console.debug(new Date(), 'app:ready');

    if (messages.length > 0) {
      const lastMsg = messages[messages.length - 1];

      if (lastMsg.status === 'answering') {
        setLoading(true);
        setResearchEnded(false);
        setMessageAppeared(false);

        isReconnectingRef.current = true;

        const res = await fetch(`/api/reconnect/${lastMsg.backendId}`, {
          method: 'POST',
        });

        if (!res.body) throw new Error('No response body');

        const reader = res.body?.getReader();
        const decoder = new TextDecoder('utf-8');

        let partialChunk = '';

        const messageHandler = getMessageHandler(lastMsg);

        try {
          while (true) {
            const { value, done } = await reader.read();
            if (done) break;

            partialChunk += decoder.decode(value, { stream: true });

            try {
              const messages = partialChunk.split('\n');
              for (const msg of messages) {
                if (!msg.trim()) continue;
                const json = JSON.parse(msg);
                messageHandler(json);
              }
              partialChunk = '';
            } catch (error) {
              console.warn('Incomplete JSON, waiting for next chunk...');
            }
          }
        } finally {
          isReconnectingRef.current = false;
        }
      }
    }
  };

  useEffect(() => {
    checkConfig(
      setChatModelProvider,
      setEmbeddingModelProvider,
      setIsConfigReady,
      setHasError,
    );
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    if (params.chatId && params.chatId !== chatId) {
      setChatId(params.chatId);
      setMessages([]);
      chatHistory.current = [];
      setFiles([]);
      setFileIds([]);
      setIsMessagesLoaded(false);
      setNotFound(false);
      setNewChatCreated(false);
    }
  }, [params.chatId, chatId]);

  useEffect(() => {
    if (
      chatId &&
      !newChatCreated &&
      !isMessagesLoaded &&
      messages.length === 0
    ) {
      loadMessages(
        chatId,
        setMessages,
        setIsMessagesLoaded,
        chatHistory,
        setSources,
        setNotFound,
        setFiles,
        setFileIds,
      );
    } else if (!chatId) {
      setNewChatCreated(true);
      setIsMessagesLoaded(true);
      setChatId(crypto.randomBytes(20).toString('hex'));
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [chatId, isMessagesLoaded, newChatCreated, messages.length]);

  useEffect(() => {
    messagesRef.current = messages;
  }, [messages]);

  useEffect(() => {
    if (isMessagesLoaded && isConfigReady && newChatCreated) {
      setIsReady(true);
      console.debug(new Date(), 'app:ready');
    } else if (isMessagesLoaded && isConfigReady && !newChatCreated) {
      checkReconnect();
    } else {
      setIsReady(false);
    }
  }, [isMessagesLoaded, isConfigReady, newChatCreated]);

  const rewrite = (messageId: string) => {
    const index = messages.findIndex((msg) => msg.messageId === messageId);

    if (index === -1) return;

    setMessages((prev) => prev.slice(0, index));

    chatHistory.current = chatHistory.current.slice(0, index * 2);

    const messageToRewrite = messages[index];
    sendMessage(messageToRewrite.query, messageToRewrite.messageId, true);
  };

  useEffect(() => {
    if (isReady && initialMessage && isConfigReady) {
      if (!isConfigReady) {
        toast.error('Cannot send message before the configuration is ready');
        return;
      }
      sendMessage(initialMessage);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [isConfigReady, isReady, initialMessage]);

  const getMessageHandler = (message: Message) => {
    const messageId = message.messageId;

    return async (data: any) => {
      if (data.type === 'error') {
        toast.error(data.data);
        setLoading(false);
        setMessages((prev) =>
          prev.map((msg) =>
            msg.messageId === messageId
              ? { ...msg, status: 'error' as const }
              : msg,
          ),
        );
        return;
      }

      if (data.type === 'researchComplete') {
        setResearchEnded(true);
        if (
          message.responseBlocks.find(
            (b) => b.type === 'source' && b.data.length > 0,
          )
        ) {
          setMessageAppeared(true);
        }
      }

      if (data.type === 'block') {
        setMessages((prev) =>
          prev.map((msg) => {
            if (msg.messageId === messageId) {
              const exists = msg.responseBlocks.findIndex(
                (b) => b.id === data.block.id,
              );

              if (exists !== -1) {
                const existingBlocks = [...msg.responseBlocks];
                existingBlocks[exists] = data.block;

                return {
                  ...msg,
                  responseBlocks: existingBlocks,
                };
              }

              return {
                ...msg,
                responseBlocks: [...msg.responseBlocks, data.block],
              };
            }
            return msg;
          }),
        );

        if (
          (data.block.type === 'source' && data.block.data.length > 0) ||
          data.block.type === 'text'
        ) {
          setMessageAppeared(true);
        }
      }

      if (data.type === 'updateBlock') {
        setMessages((prev) =>
          prev.map((msg) => {
            if (msg.messageId === messageId) {
              const updatedBlocks = msg.responseBlocks.map((block) => {
                if (block.id === data.blockId) {
                  const updatedBlock = { ...block };
                  applyPatch(updatedBlock, data.patch);
                  return updatedBlock;
                }
                return block;
              });
              return { ...msg, responseBlocks: updatedBlocks };
            }
            return msg;
          }),
        );
      }

      if (data.type === 'messageEnd') {
        if (handledMessageEndRef.current.has(messageId)) {
          return;
        }

        handledMessageEndRef.current.add(messageId);

        const currentMsg = messagesRef.current.find(
          (msg) => msg.messageId === messageId,
        );

        const newHistory: [string, string][] = [
          ...chatHistory.current,
          ['human', message.query],
          [
            'assistant',
            currentMsg?.responseBlocks.find((b) => b.type === 'text')?.data ||
              '',
          ],
        ];

        chatHistory.current = newHistory;

        setMessages((prev) =>
          prev.map((msg) =>
            msg.messageId === messageId
              ? { ...msg, status: 'completed' as const }
              : msg,
          ),
        );

        setLoading(false);

        const lastMsg = messagesRef.current[messagesRef.current.length - 1];

        const autoMediaSearch = getAutoMediaSearch();

        if (autoMediaSearch) {
          setTimeout(() => {
            document
              .getElementById(`search-images-${lastMsg.messageId}`)
              ?.click();

            document
              .getElementById(`search-videos-${lastMsg.messageId}`)
              ?.click();
          }, 200);
        }

        // Check if there are sources and no suggestions

        const hasSourceBlocks = currentMsg?.responseBlocks.some(
          (block) => block.type === 'source' && block.data.length > 0,
        );
        const hasSuggestions = currentMsg?.responseBlocks.some(
          (block) => block.type === 'suggestion',
        );

        if (hasSourceBlocks && !hasSuggestions) {
          const suggestions = await getSuggestions(newHistory);
          const suggestionBlock: Block = {
            id: crypto.randomBytes(7).toString('hex'),
            type: 'suggestion',
            data: suggestions,
          };

          setMessages((prev) =>
            prev.map((msg) => {
              if (msg.messageId === messageId) {
                return {
                  ...msg,
                  responseBlocks: [...msg.responseBlocks, suggestionBlock],
                };
              }
              return msg;
            }),
          );
        }
      }
    };
  };

  const sendMessage: ChatContext['sendMessage'] = async (
    message,
    messageId,
    rewrite = false,
  ) => {
    if (loading || !message) return;
    setLoading(true);
    setResearchEnded(false);
    setMessageAppeared(false);

    if (messages.length <= 1) {
      window.history.replaceState(null, '', `/c/${chatId}`);
    }

    messageId = messageId ?? crypto.randomBytes(7).toString('hex');
    const backendId = crypto.randomBytes(20).toString('hex');

    const newMessage: Message = {
      messageId,
      chatId: chatId!,
      backendId,
      query: message,
      responseBlocks: [],
      status: 'answering',
      createdAt: new Date(),
    };

    setMessages((prevMessages) => [...prevMessages, newMessage]);

    const messageIndex = messages.findIndex((m) => m.messageId === messageId);

    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        content: message,
        message: {
          messageId: messageId,
          chatId: chatId!,
          content: message,
        },
        chatId: chatId!,
        files: fileIds,
        sources: sources,
        optimizationMode: optimizationMode,
        history: rewrite
          ? chatHistory.current.slice(
              0,
              messageIndex === -1 ? undefined : messageIndex,
            )
          : chatHistory.current,
        chatModel: {
          key: chatModelProvider.key,
          providerId: chatModelProvider.providerId,
        },
        embeddingModel: {
          key: embeddingModelProvider.key,
          providerId: embeddingModelProvider.providerId,
        },
        systemInstructions: localStorage.getItem('systemInstructions'),
      }),
    });

    if (!res.body) throw new Error('No response body');

    const reader = res.body?.getReader();
    const decoder = new TextDecoder('utf-8');

    let partialChunk = '';

    const messageHandler = getMessageHandler(newMessage);

    while (true) {
      const { value, done } = await reader.read();
      if (done) break;

      partialChunk += decoder.decode(value, { stream: true });

      try {
        const messages = partialChunk.split('\n');
        for (const msg of messages) {
          if (!msg.trim()) continue;
          const json = JSON.parse(msg);
          messageHandler(json);
        }
        partialChunk = '';
      } catch (error) {
        console.warn('Incomplete JSON, waiting for next chunk...');
      }
    }
  };

  return (
    <chatContext.Provider
      value={{
        messages,
        sections,
        chatHistory: chatHistory.current,
        files,
        fileIds,
        sources,
        chatId,
        hasError,
        isMessagesLoaded,
        isReady,
        loading,
        messageAppeared,
        notFound,
        optimizationMode,
        setFileIds,
        setFiles,
        setSources,
        setOptimizationMode,
        rewrite,
        sendMessage,
        setChatModelProvider,
        chatModelProvider,
        embeddingModelProvider,
        setEmbeddingModelProvider,
        researchEnded,
        setResearchEnded,
      }}
    >
      {children}
    </chatContext.Provider>
  );
};

export const useChat = () => {
  const ctx = useContext(chatContext);
  return ctx;
};
```

## File: `src/lib/models/registry.ts`
```typescript
import { ConfigModelProvider } from '../config/types';
import BaseModelProvider, { createProviderInstance } from './base/provider';
import { getConfiguredModelProviders } from '../config/serverRegistry';
import { providers } from './providers';
import { MinimalProvider, ModelList } from './types';
import configManager from '../config';

class ModelRegistry {
  activeProviders: (ConfigModelProvider & {
    provider: BaseModelProvider<any>;
  })[] = [];

  constructor() {
    this.initializeActiveProviders();
  }

  private initializeActiveProviders() {
    const configuredProviders = getConfiguredModelProviders();

    configuredProviders.forEach((p) => {
      try {
        const provider = providers[p.type];
        if (!provider) throw new Error('Invalid provider type');

        this.activeProviders.push({
          ...p,
          provider: createProviderInstance(provider, p.id, p.name, p.config),
        });
      } catch (err) {
        console.error(
          `Failed to initialize provider. Type: ${p.type}, ID: ${p.id}, Config: ${JSON.stringify(p.config)}, Error: ${err}`,
        );
      }
    });
  }

  async getActiveProviders() {
    const providers: MinimalProvider[] = [];

    await Promise.all(
      this.activeProviders.map(async (p) => {
        let m: ModelList = { chat: [], embedding: [] };

        try {
          m = await p.provider.getModelList();
        } catch (err: any) {
          console.error(
            `Failed to get model list. Type: ${p.type}, ID: ${p.id}, Error: ${err.message}`,
          );

          m = {
            chat: [
              {
                key: 'error',
                name: err.message,
              },
            ],
            embedding: [],
          };
        }

        providers.push({
          id: p.id,
          name: p.name,
          chatModels: m.chat,
          embeddingModels: m.embedding,
        });
      }),
    );

    return providers;
  }

  async loadChatModel(providerId: string, modelName: string) {
    const provider = this.activeProviders.find((p) => p.id === providerId);

    if (!provider) throw new Error('Invalid provider id');

    const model = await provider.provider.loadChatModel(modelName);

    return model;
  }

  async loadEmbeddingModel(providerId: string, modelName: string) {
    const provider = this.activeProviders.find((p) => p.id === providerId);

    if (!provider) throw new Error('Invalid provider id');

    const model = await provider.provider.loadEmbeddingModel(modelName);

    return model;
  }

  async addProvider(
    type: string,
    name: string,
    config: Record<string, any>,
  ): Promise<ConfigModelProvider> {
    const provider = providers[type];
    if (!provider) throw new Error('Invalid provider type');

    const newProvider = configManager.addModelProvider(type, name, config);

    const instance = createProviderInstance(
      provider,
      newProvider.id,
      newProvider.name,
      newProvider.config,
    );

    let m: ModelList = { chat: [], embedding: [] };

    try {
      m = await instance.getModelList();
    } catch (err: any) {
      console.error(
        `Failed to get model list for newly added provider. Type: ${type}, ID: ${newProvider.id}, Error: ${err.message}`,
      );

      m = {
        chat: [
          {
            key: 'error',
            name: err.message,
          },
        ],
        embedding: [],
      };
    }

    this.activeProviders.push({
      ...newProvider,
      provider: instance,
    });

    return {
      ...newProvider,
      chatModels: m.chat || [],
      embeddingModels: m.embedding || [],
    };
  }

  async removeProvider(providerId: string): Promise<void> {
    configManager.removeModelProvider(providerId);
    this.activeProviders = this.activeProviders.filter(
      (p) => p.id !== providerId,
    );

    return;
  }

  async updateProvider(
    providerId: string,
    name: string,
    config: any,
  ): Promise<ConfigModelProvider> {
    const updated = await configManager.updateModelProvider(
      providerId,
      name,
      config,
    );
    const instance = createProviderInstance(
      providers[updated.type],
      providerId,
      name,
      config,
    );

    let m: ModelList = { chat: [], embedding: [] };

    try {
      m = await instance.getModelList();
    } catch (err: any) {
      console.error(
        `Failed to get model list for updated provider. Type: ${updated.type}, ID: ${updated.id}, Error: ${err.message}`,
      );

      m = {
        chat: [
          {
            key: 'error',
            name: err.message,
          },
        ],
        embedding: [],
      };
    }

    this.activeProviders.push({
      ...updated,
      provider: instance,
    });

    return {
      ...updated,
      chatModels: m.chat || [],
      embeddingModels: m.embedding || [],
    };
  }

  /* Using async here because maybe in the future we might want to add some validation?? */
  async addProviderModel(
    providerId: string,
    type: 'embedding' | 'chat',
    model: any,
  ): Promise<any> {
    const addedModel = configManager.addProviderModel(providerId, type, model);
    return addedModel;
  }

  async removeProviderModel(
    providerId: string,
    type: 'embedding' | 'chat',
    modelKey: string,
  ): Promise<void> {
    configManager.removeProviderModel(providerId, type, modelKey);
    return;
  }
}

export default ModelRegistry;
```

## File: `src/lib/models/types.ts`
```typescript
import z from 'zod';
import { Message } from '../types';

type Model = {
  name: string;
  key: string;
};

type ModelList = {
  embedding: Model[];
  chat: Model[];
};

type ProviderMetadata = {
  name: string;
  key: string;
};

type MinimalProvider = {
  id: string;
  name: string;
  chatModels: Model[];
  embeddingModels: Model[];
};

type ModelWithProvider = {
  key: string;
  providerId: string;
};

type GenerateOptions = {
  temperature?: number;
  maxTokens?: number;
  topP?: number;
  stopSequences?: string[];
  frequencyPenalty?: number;
  presencePenalty?: number;
};

type Tool = {
  name: string;
  description: string;
  schema: z.ZodObject<any>;
};

type ToolCall = {
  id: string;
  name: string;
  arguments: Record<string, any>;
};

type GenerateTextInput = {
  messages: Message[];
  tools?: Tool[];
  options?: GenerateOptions;
};

type GenerateTextOutput = {
  content: string;
  toolCalls: ToolCall[];
  additionalInfo?: Record<string, any>;
};

type StreamTextOutput = {
  contentChunk: string;
  toolCallChunk: ToolCall[];
  additionalInfo?: Record<string, any>;
  done?: boolean;
};

type GenerateObjectInput = {
  schema: z.ZodTypeAny;
  messages: Message[];
  options?: GenerateOptions;
};

type GenerateObjectOutput<T> = {
  object: T;
  additionalInfo?: Record<string, any>;
};

type StreamObjectOutput<T> = {
  objectChunk: Partial<T>;
  additionalInfo?: Record<string, any>;
  done?: boolean;
};

export type {
  Model,
  ModelList,
  ProviderMetadata,
  MinimalProvider,
  ModelWithProvider,
  GenerateOptions,
  GenerateTextInput,
  GenerateTextOutput,
  StreamTextOutput,
  GenerateObjectInput,
  GenerateObjectOutput,
  StreamObjectOutput,
  Tool,
  ToolCall,
};
```

## File: `src/lib/models/base/embedding.ts`
```typescript
import { Chunk } from '@/lib/types';

abstract class BaseEmbedding<CONFIG> {
  constructor(protected config: CONFIG) {}
  abstract embedText(texts: string[]): Promise<number[][]>;
  abstract embedChunks(chunks: Chunk[]): Promise<number[][]>;
}

export default BaseEmbedding;
```

## File: `src/lib/models/base/llm.ts`
```typescript
import z from 'zod';
import {
  GenerateObjectInput,
  GenerateOptions,
  GenerateTextInput,
  GenerateTextOutput,
  StreamTextOutput,
} from '../types';

abstract class BaseLLM<CONFIG> {
  constructor(protected config: CONFIG) {}
  abstract generateText(input: GenerateTextInput): Promise<GenerateTextOutput>;
  abstract streamText(
    input: GenerateTextInput,
  ): AsyncGenerator<StreamTextOutput>;
  abstract generateObject<T>(input: GenerateObjectInput): Promise<z.infer<T>>;
  abstract streamObject<T>(
    input: GenerateObjectInput,
  ): AsyncGenerator<Partial<z.infer<T>>>;
}

export default BaseLLM;
```

## File: `src/lib/models/base/provider.ts`
```typescript
import { ModelList, ProviderMetadata } from '../types';
import { UIConfigField } from '@/lib/config/types';
import BaseLLM from './llm';
import BaseEmbedding from './embedding';

abstract class BaseModelProvider<CONFIG> {
  constructor(
    protected id: string,
    protected name: string,
    protected config: CONFIG,
  ) {}
  abstract getDefaultModels(): Promise<ModelList>;
  abstract getModelList(): Promise<ModelList>;
  abstract loadChatModel(modelName: string): Promise<BaseLLM<any>>;
  abstract loadEmbeddingModel(modelName: string): Promise<BaseEmbedding<any>>;
  static getProviderConfigFields(): UIConfigField[] {
    throw new Error('Method not implemented.');
  }
  static getProviderMetadata(): ProviderMetadata {
    throw new Error('Method not Implemented.');
  }
  static parseAndValidate(raw: any): any {
    /* Static methods can't access class type parameters */
    throw new Error('Method not Implemented.');
  }
}

export type ProviderConstructor<CONFIG> = {
  new (id: string, name: string, config: CONFIG): BaseModelProvider<CONFIG>;
  parseAndValidate(raw: any): CONFIG;
  getProviderConfigFields: () => UIConfigField[];
  getProviderMetadata: () => ProviderMetadata;
};

export const createProviderInstance = <P extends ProviderConstructor<any>>(
  Provider: P,
  id: string,
  name: string,
  rawConfig: unknown,
): InstanceType<P> => {
  const cfg = Provider.parseAndValidate(rawConfig);
  return new Provider(id, name, cfg) as InstanceType<P>;
};

export default BaseModelProvider;
```

## File: `src/lib/models/providers/index.ts`
```typescript
import { ModelProviderUISection } from '@/lib/config/types';
import { ProviderConstructor } from '../base/provider';
import OpenAIProvider from './openai';
import OllamaProvider from './ollama';
import GeminiProvider from './gemini';
import TransformersProvider from './transformers';
import GroqProvider from './groq';
import LemonadeProvider from './lemonade';
import AnthropicProvider from './anthropic';
import LMStudioProvider from './lmstudio';

export const providers: Record<string, ProviderConstructor<any>> = {
  openai: OpenAIProvider,
  ollama: OllamaProvider,
  gemini: GeminiProvider,
  transformers: TransformersProvider,
  groq: GroqProvider,
  lemonade: LemonadeProvider,
  anthropic: AnthropicProvider,
  lmstudio: LMStudioProvider,
};

export const getModelProvidersUIConfigSection =
  (): ModelProviderUISection[] => {
    return Object.entries(providers).map(([k, p]) => {
      const configFields = p.getProviderConfigFields();
      const metadata = p.getProviderMetadata();

      return {
        fields: configFields,
        key: k,
        name: metadata.name,
      };
    });
  };
```

## File: `src/lib/models/providers/anthropic/anthropicLLM.ts`
```typescript
import OpenAILLM from '../openai/openaiLLM';

class AnthropicLLM extends OpenAILLM {}

export default AnthropicLLM;
```

## File: `src/lib/models/providers/anthropic/index.ts`
```typescript
import { UIConfigField } from '@/lib/config/types';
import { getConfiguredModelProviderById } from '@/lib/config/serverRegistry';
import { Model, ModelList, ProviderMetadata } from '../../types';
import BaseEmbedding from '../../base/embedding';
import BaseModelProvider from '../../base/provider';
import BaseLLM from '../../base/llm';
import AnthropicLLM from './anthropicLLM';

interface AnthropicConfig {
  apiKey: string;
}

const providerConfigFields: UIConfigField[] = [
  {
    type: 'password',
    name: 'API Key',
    key: 'apiKey',
    description: 'Your Anthropic API key',
    required: true,
    placeholder: 'Anthropic API Key',
    env: 'ANTHROPIC_API_KEY',
    scope: 'server',
  },
];

class AnthropicProvider extends BaseModelProvider<AnthropicConfig> {
  constructor(id: string, name: string, config: AnthropicConfig) {
    super(id, name, config);
  }

  async getDefaultModels(): Promise<ModelList> {
    const res = await fetch('https://api.anthropic.com/v1/models?limit=999', {
      method: 'GET',
      headers: {
        'x-api-key': this.config.apiKey,
        'anthropic-version': '2023-06-01',
        'Content-type': 'application/json',
      },
    });

    if (!res.ok) {
      throw new Error(`Failed to fetch Anthropic models: ${res.statusText}`);
    }

    const data = (await res.json()).data;

    const models: Model[] = data.map((m: any) => {
      return {
        key: m.id,
        name: m.display_name,
      };
    });

    return {
      embedding: [],
      chat: models,
    };
  }

  async getModelList(): Promise<ModelList> {
    const defaultModels = await this.getDefaultModels();
    const configProvider = getConfiguredModelProviderById(this.id)!;

    return {
      embedding: [],
      chat: [...defaultModels.chat, ...configProvider.chatModels],
    };
  }

  async loadChatModel(key: string): Promise<BaseLLM<any>> {
    const modelList = await this.getModelList();

    const exists = modelList.chat.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading Anthropic Chat Model. Invalid Model Selected',
      );
    }

    return new AnthropicLLM({
      apiKey: this.config.apiKey,
      model: key,
      baseURL: 'https://api.anthropic.com/v1',
    });
  }

  async loadEmbeddingModel(key: string): Promise<BaseEmbedding<any>> {
    throw new Error('Anthropic provider does not support embedding models.');
  }

  static parseAndValidate(raw: any): AnthropicConfig {
    if (!raw || typeof raw !== 'object')
      throw new Error('Invalid config provided. Expected object');
    if (!raw.apiKey)
      throw new Error('Invalid config provided. API key must be provided');

    return {
      apiKey: String(raw.apiKey),
    };
  }

  static getProviderConfigFields(): UIConfigField[] {
    return providerConfigFields;
  }

  static getProviderMetadata(): ProviderMetadata {
    return {
      key: 'anthropic',
      name: 'Anthropic',
    };
  }
}

export default AnthropicProvider;
```

## File: `src/lib/models/providers/gemini/geminiEmbedding.ts`
```typescript
import OpenAIEmbedding from '../openai/openaiEmbedding';

class GeminiEmbedding extends OpenAIEmbedding {}

export default GeminiEmbedding;
```

## File: `src/lib/models/providers/gemini/geminiLLM.ts`
```typescript
import OpenAILLM from '../openai/openaiLLM';

class GeminiLLM extends OpenAILLM {}

export default GeminiLLM;
```

## File: `src/lib/models/providers/gemini/index.ts`
```typescript
import { UIConfigField } from '@/lib/config/types';
import { getConfiguredModelProviderById } from '@/lib/config/serverRegistry';
import { Model, ModelList, ProviderMetadata } from '../../types';
import GeminiEmbedding from './geminiEmbedding';
import BaseEmbedding from '../../base/embedding';
import BaseModelProvider from '../../base/provider';
import BaseLLM from '../../base/llm';
import GeminiLLM from './geminiLLM';

interface GeminiConfig {
  apiKey: string;
}

const providerConfigFields: UIConfigField[] = [
  {
    type: 'password',
    name: 'API Key',
    key: 'apiKey',
    description: 'Your Gemini API key',
    required: true,
    placeholder: 'Gemini API Key',
    env: 'GEMINI_API_KEY',
    scope: 'server',
  },
];

class GeminiProvider extends BaseModelProvider<GeminiConfig> {
  constructor(id: string, name: string, config: GeminiConfig) {
    super(id, name, config);
  }

  async getDefaultModels(): Promise<ModelList> {
    const res = await fetch(
      `https://generativelanguage.googleapis.com/v1beta/models?key=${this.config.apiKey}`,
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      },
    );

    const data = await res.json();

    let defaultEmbeddingModels: Model[] = [];
    let defaultChatModels: Model[] = [];

    data.models.forEach((m: any) => {
      if (
        m.supportedGenerationMethods.some(
          (genMethod: string) =>
            genMethod === 'embedText' || genMethod === 'embedContent',
        )
      ) {
        defaultEmbeddingModels.push({
          key: m.name,
          name: m.displayName,
        });
      } else if (m.supportedGenerationMethods.includes('generateContent')) {
        defaultChatModels.push({
          key: m.name,
          name: m.displayName,
        });
      }
    });

    return {
      embedding: defaultEmbeddingModels,
      chat: defaultChatModels,
    };
  }

  async getModelList(): Promise<ModelList> {
    const defaultModels = await this.getDefaultModels();
    const configProvider = getConfiguredModelProviderById(this.id)!;

    return {
      embedding: [
        ...defaultModels.embedding,
        ...configProvider.embeddingModels,
      ],
      chat: [...defaultModels.chat, ...configProvider.chatModels],
    };
  }

  async loadChatModel(key: string): Promise<BaseLLM<any>> {
    const modelList = await this.getModelList();

    const exists = modelList.chat.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading Gemini Chat Model. Invalid Model Selected',
      );
    }

    return new GeminiLLM({
      apiKey: this.config.apiKey,
      model: key,
      baseURL: 'https://generativelanguage.googleapis.com/v1beta/openai',
    });
  }

  async loadEmbeddingModel(key: string): Promise<BaseEmbedding<any>> {
    const modelList = await this.getModelList();
    const exists = modelList.embedding.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading Gemini Embedding Model. Invalid Model Selected.',
      );
    }

    return new GeminiEmbedding({
      apiKey: this.config.apiKey,
      model: key,
      baseURL: 'https://generativelanguage.googleapis.com/v1beta/openai',
    });
  }

  static parseAndValidate(raw: any): GeminiConfig {
    if (!raw || typeof raw !== 'object')
      throw new Error('Invalid config provided. Expected object');
    if (!raw.apiKey)
      throw new Error('Invalid config provided. API key must be provided');

    return {
      apiKey: String(raw.apiKey),
    };
  }

  static getProviderConfigFields(): UIConfigField[] {
    return providerConfigFields;
  }

  static getProviderMetadata(): ProviderMetadata {
    return {
      key: 'gemini',
      name: 'Gemini',
    };
  }
}

export default GeminiProvider;
```

## File: `src/lib/models/providers/groq/groqLLM.ts`
```typescript
import OpenAILLM from '../openai/openaiLLM';

class GroqLLM extends OpenAILLM {}

export default GroqLLM;
```

## File: `src/lib/models/providers/groq/index.ts`
```typescript
import { UIConfigField } from '@/lib/config/types';
import { getConfiguredModelProviderById } from '@/lib/config/serverRegistry';
import { Model, ModelList, ProviderMetadata } from '../../types';
import BaseEmbedding from '../../base/embedding';
import BaseModelProvider from '../../base/provider';
import BaseLLM from '../../base/llm';
import GroqLLM from './groqLLM';

interface GroqConfig {
  apiKey: string;
}

const providerConfigFields: UIConfigField[] = [
  {
    type: 'password',
    name: 'API Key',
    key: 'apiKey',
    description: 'Your Groq API key',
    required: true,
    placeholder: 'Groq API Key',
    env: 'GROQ_API_KEY',
    scope: 'server',
  },
];

class GroqProvider extends BaseModelProvider<GroqConfig> {
  constructor(id: string, name: string, config: GroqConfig) {
    super(id, name, config);
  }

  async getDefaultModels(): Promise<ModelList> {
    const res = await fetch(`https://api.groq.com/openai/v1/models`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${this.config.apiKey}`,
      },
    });

    const data = await res.json();

    const defaultChatModels: Model[] = [];

    data.data.forEach((m: any) => {
      defaultChatModels.push({
        key: m.id,
        name: m.id,
      });
    });

    return {
      embedding: [],
      chat: defaultChatModels,
    };
  }

  async getModelList(): Promise<ModelList> {
    const defaultModels = await this.getDefaultModels();
    const configProvider = getConfiguredModelProviderById(this.id)!;

    return {
      embedding: [
        ...defaultModels.embedding,
        ...configProvider.embeddingModels,
      ],
      chat: [...defaultModels.chat, ...configProvider.chatModels],
    };
  }

  async loadChatModel(key: string): Promise<BaseLLM<any>> {
    const modelList = await this.getModelList();

    const exists = modelList.chat.find((m) => m.key === key);

    if (!exists) {
      throw new Error('Error Loading Groq Chat Model. Invalid Model Selected');
    }

    return new GroqLLM({
      apiKey: this.config.apiKey,
      model: key,
      baseURL: 'https://api.groq.com/openai/v1',
    });
  }

  async loadEmbeddingModel(key: string): Promise<BaseEmbedding<any>> {
    throw new Error('Groq Provider does not support embedding models.');
  }

  static parseAndValidate(raw: any): GroqConfig {
    if (!raw || typeof raw !== 'object')
      throw new Error('Invalid config provided. Expected object');
    if (!raw.apiKey)
      throw new Error('Invalid config provided. API key must be provided');

    return {
      apiKey: String(raw.apiKey),
    };
  }

  static getProviderConfigFields(): UIConfigField[] {
    return providerConfigFields;
  }

  static getProviderMetadata(): ProviderMetadata {
    return {
      key: 'groq',
      name: 'Groq',
    };
  }
}

export default GroqProvider;
```

## File: `src/lib/models/providers/lemonade/index.ts`
```typescript
import { UIConfigField } from '@/lib/config/types';
import { getConfiguredModelProviderById } from '@/lib/config/serverRegistry';
import BaseModelProvider from '../../base/provider';
import { Model, ModelList, ProviderMetadata } from '../../types';
import BaseLLM from '../../base/llm';
import LemonadeLLM from './lemonadeLLM';
import BaseEmbedding from '../../base/embedding';
import LemonadeEmbedding from './lemonadeEmbedding';

interface LemonadeConfig {
  baseURL: string;
  apiKey?: string;
}

const providerConfigFields: UIConfigField[] = [
  {
    type: 'string',
    name: 'Base URL',
    key: 'baseURL',
    description: 'The base URL for Lemonade API',
    required: true,
    placeholder: 'https://api.lemonade.ai/v1',
    env: 'LEMONADE_BASE_URL',
    scope: 'server',
  },
  {
    type: 'password',
    name: 'API Key',
    key: 'apiKey',
    description: 'Your Lemonade API key (optional)',
    required: false,
    placeholder: 'Lemonade API Key',
    env: 'LEMONADE_API_KEY',
    scope: 'server',
  },
];

class LemonadeProvider extends BaseModelProvider<LemonadeConfig> {
  constructor(id: string, name: string, config: LemonadeConfig) {
    super(id, name, config);
  }

  async getDefaultModels(): Promise<ModelList> {
    try {
      const res = await fetch(`${this.config.baseURL}/models`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          ...(this.config.apiKey
            ? { Authorization: `Bearer ${this.config.apiKey}` }
            : {}),
        },
      });

      const data = await res.json();

      const models: Model[] = data.data
        .filter((m: any) => m.recipe === 'llamacpp')
        .map((m: any) => {
          return {
            name: m.id,
            key: m.id,
          };
        });

      return {
        embedding: models,
        chat: models,
      };
    } catch (err) {
      if (err instanceof TypeError) {
        throw new Error(
          'Error connecting to Lemonade API. Please ensure the base URL is correct and the service is available.',
        );
      }

      throw err;
    }
  }

  async getModelList(): Promise<ModelList> {
    const defaultModels = await this.getDefaultModels();
    const configProvider = getConfiguredModelProviderById(this.id)!;

    return {
      embedding: [
        ...defaultModels.embedding,
        ...configProvider.embeddingModels,
      ],
      chat: [...defaultModels.chat, ...configProvider.chatModels],
    };
  }

  async loadChatModel(key: string): Promise<BaseLLM<any>> {
    const modelList = await this.getModelList();

    const exists = modelList.chat.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading Lemonade Chat Model. Invalid Model Selected',
      );
    }

    return new LemonadeLLM({
      apiKey: this.config.apiKey || 'not-needed',
      model: key,
      baseURL: this.config.baseURL,
    });
  }

  async loadEmbeddingModel(key: string): Promise<BaseEmbedding<any>> {
    const modelList = await this.getModelList();
    const exists = modelList.embedding.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading Lemonade Embedding Model. Invalid Model Selected.',
      );
    }

    return new LemonadeEmbedding({
      apiKey: this.config.apiKey || 'not-needed',
      model: key,
      baseURL: this.config.baseURL,
    });
  }

  static parseAndValidate(raw: any): LemonadeConfig {
    if (!raw || typeof raw !== 'object')
      throw new Error('Invalid config provided. Expected object');
    if (!raw.baseURL)
      throw new Error('Invalid config provided. Base URL must be provided');

    return {
      baseURL: String(raw.baseURL),
      apiKey: raw.apiKey ? String(raw.apiKey) : undefined,
    };
  }

  static getProviderConfigFields(): UIConfigField[] {
    return providerConfigFields;
  }

  static getProviderMetadata(): ProviderMetadata {
    return {
      key: 'lemonade',
      name: 'Lemonade',
    };
  }
}

export default LemonadeProvider;
```

## File: `src/lib/models/providers/lemonade/lemonadeEmbedding.ts`
```typescript
import OpenAIEmbedding from '../openai/openaiEmbedding';

class LemonadeEmbedding extends OpenAIEmbedding {}

export default LemonadeEmbedding;
```

## File: `src/lib/models/providers/lemonade/lemonadeLLM.ts`
```typescript
import OpenAILLM from '../openai/openaiLLM';

class LemonadeLLM extends OpenAILLM {}

export default LemonadeLLM;
```

## File: `src/lib/models/providers/lmstudio/index.ts`
```typescript
import { UIConfigField } from '@/lib/config/types';
import { getConfiguredModelProviderById } from '@/lib/config/serverRegistry';
import BaseModelProvider from '../../base/provider';
import { Model, ModelList, ProviderMetadata } from '../../types';
import LMStudioLLM from './lmstudioLLM';
import BaseLLM from '../../base/llm';
import BaseEmbedding from '../../base/embedding';
import LMStudioEmbedding from './lmstudioEmbedding';

interface LMStudioConfig {
  baseURL: string;
}

const providerConfigFields: UIConfigField[] = [
  {
    type: 'string',
    name: 'Base URL',
    key: 'baseURL',
    description: 'The base URL for LM Studio server',
    required: true,
    placeholder: 'http://localhost:1234',
    env: 'LM_STUDIO_BASE_URL',
    scope: 'server',
  },
];

class LMStudioProvider extends BaseModelProvider<LMStudioConfig> {
  constructor(id: string, name: string, config: LMStudioConfig) {
    super(id, name, config);
  }

  private normalizeBaseURL(url: string): string {
    const trimmed = url.trim().replace(/\/+$/, '');
    return trimmed.endsWith('/v1') ? trimmed : `${trimmed}/v1`;
  }

  async getDefaultModels(): Promise<ModelList> {
    try {
      const baseURL = this.normalizeBaseURL(this.config.baseURL);

      const res = await fetch(`${baseURL}/models`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      const data = await res.json();

      const models: Model[] = data.data.map((m: any) => {
        return {
          name: m.id,
          key: m.id,
        };
      });

      return {
        embedding: models,
        chat: models,
      };
    } catch (err) {
      if (err instanceof TypeError) {
        throw new Error(
          'Error connecting to LM Studio. Please ensure the base URL is correct and the LM Studio server is running.',
        );
      }

      throw err;
    }
  }

  async getModelList(): Promise<ModelList> {
    const defaultModels = await this.getDefaultModels();
    const configProvider = getConfiguredModelProviderById(this.id)!;

    return {
      embedding: [
        ...defaultModels.embedding,
        ...configProvider.embeddingModels,
      ],
      chat: [...defaultModels.chat, ...configProvider.chatModels],
    };
  }

  async loadChatModel(key: string): Promise<BaseLLM<any>> {
    const modelList = await this.getModelList();

    const exists = modelList.chat.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading LM Studio Chat Model. Invalid Model Selected',
      );
    }

    return new LMStudioLLM({
      apiKey: 'lm-studio',
      model: key,
      baseURL: this.normalizeBaseURL(this.config.baseURL),
    });
  }

  async loadEmbeddingModel(key: string): Promise<BaseEmbedding<any>> {
    const modelList = await this.getModelList();
    const exists = modelList.embedding.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading LM Studio Embedding Model. Invalid Model Selected.',
      );
    }

    return new LMStudioEmbedding({
      apiKey: 'lm-studio',
      model: key,
      baseURL: this.normalizeBaseURL(this.config.baseURL),
    });
  }

  static parseAndValidate(raw: any): LMStudioConfig {
    if (!raw || typeof raw !== 'object')
      throw new Error('Invalid config provided. Expected object');
    if (!raw.baseURL)
      throw new Error('Invalid config provided. Base URL must be provided');

    return {
      baseURL: String(raw.baseURL),
    };
  }

  static getProviderConfigFields(): UIConfigField[] {
    return providerConfigFields;
  }

  static getProviderMetadata(): ProviderMetadata {
    return {
      key: 'lmstudio',
      name: 'LM Studio',
    };
  }
}

export default LMStudioProvider;
```

## File: `src/lib/models/providers/lmstudio/lmstudioEmbedding.ts`
```typescript
import OpenAIEmbedding from '../openai/openaiEmbedding';

class LMStudioEmbedding extends OpenAIEmbedding {}

export default LMStudioEmbedding;
```

## File: `src/lib/models/providers/lmstudio/lmstudioLLM.ts`
```typescript
import OpenAILLM from '../openai/openaiLLM';

class LMStudioLLM extends OpenAILLM {}

export default LMStudioLLM;
```

## File: `src/lib/models/providers/ollama/index.ts`
```typescript
import { UIConfigField } from '@/lib/config/types';
import { getConfiguredModelProviderById } from '@/lib/config/serverRegistry';
import BaseModelProvider from '../../base/provider';
import { Model, ModelList, ProviderMetadata } from '../../types';
import BaseLLM from '../../base/llm';
import BaseEmbedding from '../../base/embedding';
import OllamaLLM from './ollamaLLM';
import OllamaEmbedding from './ollamaEmbedding';

interface OllamaConfig {
  baseURL: string;
}

const providerConfigFields: UIConfigField[] = [
  {
    type: 'string',
    name: 'Base URL',
    key: 'baseURL',
    description: 'The base URL for the Ollama',
    required: true,
    placeholder: process.env.DOCKER
      ? 'http://host.docker.internal:11434'
      : 'http://localhost:11434',
    env: 'OLLAMA_BASE_URL',
    scope: 'server',
  },
];

class OllamaProvider extends BaseModelProvider<OllamaConfig> {
  constructor(id: string, name: string, config: OllamaConfig) {
    super(id, name, config);
  }

  async getDefaultModels(): Promise<ModelList> {
    try {
      const res = await fetch(`${this.config.baseURL}/api/tags`, {
        method: 'GET',
        headers: {
          'Content-type': 'application/json',
        },
      });

      const data = await res.json();

      const models: Model[] = data.models.map((m: any) => {
        return {
          name: m.name,
          key: m.model,
        };
      });

      return {
        embedding: models,
        chat: models,
      };
    } catch (err) {
      if (err instanceof TypeError) {
        throw new Error(
          'Error connecting to Ollama API. Please ensure the base URL is correct and the Ollama server is running.',
        );
      }

      throw err;
    }
  }

  async getModelList(): Promise<ModelList> {
    const defaultModels = await this.getDefaultModels();
    const configProvider = getConfiguredModelProviderById(this.id)!;

    return {
      embedding: [
        ...defaultModels.embedding,
        ...configProvider.embeddingModels,
      ],
      chat: [...defaultModels.chat, ...configProvider.chatModels],
    };
  }

  async loadChatModel(key: string): Promise<BaseLLM<any>> {
    const modelList = await this.getModelList();

    const exists = modelList.chat.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading Ollama Chat Model. Invalid Model Selected',
      );
    }

    return new OllamaLLM({
      baseURL: this.config.baseURL,
      model: key,
    });
  }

  async loadEmbeddingModel(key: string): Promise<BaseEmbedding<any>> {
    const modelList = await this.getModelList();
    const exists = modelList.embedding.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading Ollama Embedding Model. Invalid Model Selected.',
      );
    }

    return new OllamaEmbedding({
      model: key,
      baseURL: this.config.baseURL,
    });
  }

  static parseAndValidate(raw: any): OllamaConfig {
    if (!raw || typeof raw !== 'object')
      throw new Error('Invalid config provided. Expected object');
    if (!raw.baseURL)
      throw new Error('Invalid config provided. Base URL must be provided');

    return {
      baseURL: String(raw.baseURL),
    };
  }

  static getProviderConfigFields(): UIConfigField[] {
    return providerConfigFields;
  }

  static getProviderMetadata(): ProviderMetadata {
    return {
      key: 'ollama',
      name: 'Ollama',
    };
  }
}

export default OllamaProvider;
```

## File: `src/lib/models/providers/ollama/ollamaEmbedding.ts`
```typescript
import { Ollama } from 'ollama';
import BaseEmbedding from '../../base/embedding';
import { Chunk } from '@/lib/types';

type OllamaConfig = {
  model: string;
  baseURL?: string;
};

class OllamaEmbedding extends BaseEmbedding<OllamaConfig> {
  ollamaClient: Ollama;

  constructor(protected config: OllamaConfig) {
    super(config);

    this.ollamaClient = new Ollama({
      host: this.config.baseURL || 'http://localhost:11434',
    });
  }

  async embedText(texts: string[]): Promise<number[][]> {
    const response = await this.ollamaClient.embed({
      input: texts,
      model: this.config.model,
    });

    return response.embeddings;
  }

  async embedChunks(chunks: Chunk[]): Promise<number[][]> {
    const response = await this.ollamaClient.embed({
      input: chunks.map((c) => c.content),
      model: this.config.model,
    });

    return response.embeddings;
  }
}

export default OllamaEmbedding;
```

## File: `src/lib/models/providers/ollama/ollamaLLM.ts`
```typescript
import z from 'zod';
import BaseLLM from '../../base/llm';
import {
  GenerateObjectInput,
  GenerateOptions,
  GenerateTextInput,
  GenerateTextOutput,
  StreamTextOutput,
} from '../../types';
import { Ollama, Tool as OllamaTool, Message as OllamaMessage } from 'ollama';
import { parse } from 'partial-json';
import crypto from 'crypto';
import { Message } from '@/lib/types';
import { repairJson } from '@toolsycc/json-repair';

type OllamaConfig = {
  baseURL: string;
  model: string;
  options?: GenerateOptions;
};

const reasoningModels = [
  'gpt-oss',
  'deepseek-r1',
  'qwen3',
  'deepseek-v3.1',
  'magistral',
  'nemotron-3',
  'nemotron-cascade-2',
  'glm-4.7-flash',
];

class OllamaLLM extends BaseLLM<OllamaConfig> {
  ollamaClient: Ollama;

  constructor(protected config: OllamaConfig) {
    super(config);

    this.ollamaClient = new Ollama({
      host: this.config.baseURL || 'http://localhost:11434',
    });
  }

  convertToOllamaMessages(messages: Message[]): OllamaMessage[] {
    return messages.map((msg) => {
      if (msg.role === 'tool') {
        return {
          role: 'tool',
          tool_name: msg.name,
          content: msg.content,
        } as OllamaMessage;
      } else if (msg.role === 'assistant') {
        return {
          role: 'assistant',
          content: msg.content,
          tool_calls:
            msg.tool_calls?.map((tc, i) => ({
              function: {
                index: i,
                name: tc.name,
                arguments: tc.arguments,
              },
            })) || [],
        };
      }

      return msg;
    });
  }

  async generateText(input: GenerateTextInput): Promise<GenerateTextOutput> {
    const ollamaTools: OllamaTool[] = [];

    input.tools?.forEach((tool) => {
      ollamaTools.push({
        type: 'function',
        function: {
          name: tool.name,
          description: tool.description,
          parameters: z.toJSONSchema(tool.schema).properties,
        },
      });
    });

    const res = await this.ollamaClient.chat({
      model: this.config.model,
      messages: this.convertToOllamaMessages(input.messages),
      tools: ollamaTools.length > 0 ? ollamaTools : undefined,
      ...(reasoningModels.find((m) => this.config.model.includes(m))
        ? { think: false }
        : {}),
      options: {
        top_p: input.options?.topP ?? this.config.options?.topP,
        temperature:
          input.options?.temperature ?? this.config.options?.temperature ?? 0.7,
        num_predict: input.options?.maxTokens ?? this.config.options?.maxTokens,
        num_ctx: 32000,
        frequency_penalty:
          input.options?.frequencyPenalty ??
          this.config.options?.frequencyPenalty,
        presence_penalty:
          input.options?.presencePenalty ??
          this.config.options?.presencePenalty,
        stop:
          input.options?.stopSequences ?? this.config.options?.stopSequences,
      },
    });

    return {
      content: res.message.content,
      toolCalls:
        res.message.tool_calls?.map((tc) => ({
          id: crypto.randomUUID(),
          name: tc.function.name,
          arguments: tc.function.arguments,
        })) || [],
      additionalInfo: {
        reasoning: res.message.thinking,
      },
    };
  }

  async *streamText(
    input: GenerateTextInput,
  ): AsyncGenerator<StreamTextOutput> {
    const ollamaTools: OllamaTool[] = [];

    input.tools?.forEach((tool) => {
      ollamaTools.push({
        type: 'function',
        function: {
          name: tool.name,
          description: tool.description,
          parameters: z.toJSONSchema(tool.schema) as any,
        },
      });
    });

    const stream = await this.ollamaClient.chat({
      model: this.config.model,
      messages: this.convertToOllamaMessages(input.messages),
      stream: true,
      ...(reasoningModels.find((m) => this.config.model.includes(m))
        ? { think: false }
        : {}),
      tools: ollamaTools.length > 0 ? ollamaTools : undefined,
      options: {
        top_p: input.options?.topP ?? this.config.options?.topP,
        temperature:
          input.options?.temperature ?? this.config.options?.temperature ?? 0.7,
        num_ctx: 32000,
        num_predict: input.options?.maxTokens ?? this.config.options?.maxTokens,
        frequency_penalty:
          input.options?.frequencyPenalty ??
          this.config.options?.frequencyPenalty,
        presence_penalty:
          input.options?.presencePenalty ??
          this.config.options?.presencePenalty,
        stop:
          input.options?.stopSequences ?? this.config.options?.stopSequences,
      },
    });

    for await (const chunk of stream) {
      yield {
        contentChunk: chunk.message.content,
        toolCallChunk:
          chunk.message.tool_calls?.map((tc, i) => ({
            id: crypto
              .createHash('sha256')
              .update(
                `${i}-${tc.function.name}`,
              ) /* Ollama currently doesn't return a tool call ID so we're creating one based on the index and tool call name */
              .digest('hex'),
            name: tc.function.name,
            arguments: tc.function.arguments,
          })) || [],
        done: chunk.done,
        additionalInfo: {
          reasoning: chunk.message.thinking,
        },
      };
    }
  }

  async generateObject<T>(input: GenerateObjectInput): Promise<T> {
    const response = await this.ollamaClient.chat({
      model: this.config.model,
      messages: this.convertToOllamaMessages(input.messages),
      format: z.toJSONSchema(input.schema),
      ...(reasoningModels.find((m) => this.config.model.includes(m))
        ? { think: false }
        : {}),
      options: {
        top_p: input.options?.topP ?? this.config.options?.topP,
        temperature:
          input.options?.temperature ?? this.config.options?.temperature ?? 0.7,
        num_predict: input.options?.maxTokens ?? this.config.options?.maxTokens,
        frequency_penalty:
          input.options?.frequencyPenalty ??
          this.config.options?.frequencyPenalty,
        presence_penalty:
          input.options?.presencePenalty ??
          this.config.options?.presencePenalty,
        stop:
          input.options?.stopSequences ?? this.config.options?.stopSequences,
      },
    });

    try {
      return input.schema.parse(
        JSON.parse(
          repairJson(response.message.content, {
            extractJson: true,
          }) as string,
        ),
      ) as T;
    } catch (err) {
      throw new Error(`Error parsing response from Ollama: ${err}`);
    }
  }

  async *streamObject<T>(input: GenerateObjectInput): AsyncGenerator<T> {
    let recievedObj: string = '';

    const stream = await this.ollamaClient.chat({
      model: this.config.model,
      messages: this.convertToOllamaMessages(input.messages),
      format: z.toJSONSchema(input.schema),
      stream: true,
      ...(reasoningModels.find((m) => this.config.model.includes(m))
        ? { think: false }
        : {}),
      options: {
        top_p: input.options?.topP ?? this.config.options?.topP,
        temperature:
          input.options?.temperature ?? this.config.options?.temperature ?? 0.7,
        num_predict: input.options?.maxTokens ?? this.config.options?.maxTokens,
        frequency_penalty:
          input.options?.frequencyPenalty ??
          this.config.options?.frequencyPenalty,
        presence_penalty:
          input.options?.presencePenalty ??
          this.config.options?.presencePenalty,
        stop:
          input.options?.stopSequences ?? this.config.options?.stopSequences,
      },
    });

    for await (const chunk of stream) {
      recievedObj += chunk.message.content;

      try {
        yield parse(recievedObj) as T;
      } catch (err) {
        console.log('Error parsing partial object from Ollama:', err);
        yield {} as T;
      }
    }
  }
}

export default OllamaLLM;
```

## File: `src/lib/models/providers/openai/index.ts`
```typescript
import { UIConfigField } from '@/lib/config/types';
import { getConfiguredModelProviderById } from '@/lib/config/serverRegistry';
import { Model, ModelList, ProviderMetadata } from '../../types';
import OpenAIEmbedding from './openaiEmbedding';
import BaseEmbedding from '../../base/embedding';
import BaseModelProvider from '../../base/provider';
import BaseLLM from '../../base/llm';
import OpenAILLM from './openaiLLM';

interface OpenAIConfig {
  apiKey: string;
  baseURL: string;
}

const defaultChatModels: Model[] = [
  {
    name: 'GPT-3.5 Turbo',
    key: 'gpt-3.5-turbo',
  },
  {
    name: 'GPT-4',
    key: 'gpt-4',
  },
  {
    name: 'GPT-4 turbo',
    key: 'gpt-4-turbo',
  },
  {
    name: 'GPT-4 omni',
    key: 'gpt-4o',
  },
  {
    name: 'GPT-4o (2024-05-13)',
    key: 'gpt-4o-2024-05-13',
  },
  {
    name: 'GPT-4 omni mini',
    key: 'gpt-4o-mini',
  },
  {
    name: 'GPT 4.1 nano',
    key: 'gpt-4.1-nano',
  },
  {
    name: 'GPT 4.1 mini',
    key: 'gpt-4.1-mini',
  },
  {
    name: 'GPT 4.1',
    key: 'gpt-4.1',
  },
  {
    name: 'GPT 5 nano',
    key: 'gpt-5-nano',
  },
  {
    name: 'GPT 5',
    key: 'gpt-5',
  },
  {
    name: 'GPT 5 Mini',
    key: 'gpt-5-mini',
  },
  {
    name: 'GPT 5 Pro',
    key: 'gpt-5-pro',
  },
  {
    name: 'GPT 5.1',
    key: 'gpt-5.1',
  },
  {
    name: 'GPT 5.2',
    key: 'gpt-5.2',
  },
  {
    name: 'GPT 5.2 Pro',
    key: 'gpt-5.2-pro',
  },
  {
    name: 'o1',
    key: 'o1',
  },
  {
    name: 'o3',
    key: 'o3',
  },
  {
    name: 'o3 Mini',
    key: 'o3-mini',
  },
  {
    name: 'o4 Mini',
    key: 'o4-mini',
  },
];

const defaultEmbeddingModels: Model[] = [
  {
    name: 'Text Embedding 3 Small',
    key: 'text-embedding-3-small',
  },
  {
    name: 'Text Embedding 3 Large',
    key: 'text-embedding-3-large',
  },
];

const providerConfigFields: UIConfigField[] = [
  {
    type: 'password',
    name: 'API Key',
    key: 'apiKey',
    description: 'Your OpenAI API key',
    required: true,
    placeholder: 'OpenAI API Key',
    env: 'OPENAI_API_KEY',
    scope: 'server',
  },
  {
    type: 'string',
    name: 'Base URL',
    key: 'baseURL',
    description: 'The base URL for the OpenAI API',
    required: true,
    placeholder: 'OpenAI Base URL',
    default: 'https://api.openai.com/v1',
    env: 'OPENAI_BASE_URL',
    scope: 'server',
  },
];

class OpenAIProvider extends BaseModelProvider<OpenAIConfig> {
  constructor(id: string, name: string, config: OpenAIConfig) {
    super(id, name, config);
  }

  async getDefaultModels(): Promise<ModelList> {
    if (this.config.baseURL === 'https://api.openai.com/v1') {
      return {
        embedding: defaultEmbeddingModels,
        chat: defaultChatModels,
      };
    }

    return {
      embedding: [],
      chat: [],
    };
  }

  async getModelList(): Promise<ModelList> {
    const defaultModels = await this.getDefaultModels();
    const configProvider = getConfiguredModelProviderById(this.id)!;

    return {
      embedding: [
        ...defaultModels.embedding,
        ...configProvider.embeddingModels,
      ],
      chat: [...defaultModels.chat, ...configProvider.chatModels],
    };
  }

  async loadChatModel(key: string): Promise<BaseLLM<any>> {
    const modelList = await this.getModelList();

    const exists = modelList.chat.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading OpenAI Chat Model. Invalid Model Selected',
      );
    }

    return new OpenAILLM({
      apiKey: this.config.apiKey,
      model: key,
      baseURL: this.config.baseURL,
    });
  }

  async loadEmbeddingModel(key: string): Promise<BaseEmbedding<any>> {
    const modelList = await this.getModelList();
    const exists = modelList.embedding.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading OpenAI Embedding Model. Invalid Model Selected.',
      );
    }

    return new OpenAIEmbedding({
      apiKey: this.config.apiKey,
      model: key,
      baseURL: this.config.baseURL,
    });
  }

  static parseAndValidate(raw: any): OpenAIConfig {
    if (!raw || typeof raw !== 'object')
      throw new Error('Invalid config provided. Expected object');
    if (!raw.apiKey || !raw.baseURL)
      throw new Error(
        'Invalid config provided. API key and base URL must be provided',
      );

    return {
      apiKey: String(raw.apiKey),
      baseURL: String(raw.baseURL),
    };
  }

  static getProviderConfigFields(): UIConfigField[] {
    return providerConfigFields;
  }

  static getProviderMetadata(): ProviderMetadata {
    return {
      key: 'openai',
      name: 'OpenAI',
    };
  }
}

export default OpenAIProvider;
```

## File: `src/lib/models/providers/openai/openaiEmbedding.ts`
```typescript
import OpenAI from 'openai';
import BaseEmbedding from '../../base/embedding';
import { Chunk } from '@/lib/types';

type OpenAIConfig = {
  apiKey: string;
  model: string;
  baseURL?: string;
};

class OpenAIEmbedding extends BaseEmbedding<OpenAIConfig> {
  openAIClient: OpenAI;

  constructor(protected config: OpenAIConfig) {
    super(config);

    this.openAIClient = new OpenAI({
      apiKey: config.apiKey,
      baseURL: config.baseURL,
    });
  }

  async embedText(texts: string[]): Promise<number[][]> {
    const response = await this.openAIClient.embeddings.create({
      model: this.config.model,
      input: texts,
    });

    return response.data.map((embedding) => embedding.embedding);
  }

  async embedChunks(chunks: Chunk[]): Promise<number[][]> {
    const response = await this.openAIClient.embeddings.create({
      model: this.config.model,
      input: chunks.map((c) => c.content),
    });

    return response.data.map((embedding) => embedding.embedding);
  }
}

export default OpenAIEmbedding;
```

## File: `src/lib/models/providers/openai/openaiLLM.ts`
```typescript
import OpenAI from 'openai';
import BaseLLM from '../../base/llm';
import { zodTextFormat, zodResponseFormat } from 'openai/helpers/zod';
import {
  GenerateObjectInput,
  GenerateOptions,
  GenerateTextInput,
  GenerateTextOutput,
  StreamTextOutput,
  ToolCall,
} from '../../types';
import { parse } from 'partial-json';
import z from 'zod';
import {
  ChatCompletionAssistantMessageParam,
  ChatCompletionMessageParam,
  ChatCompletionTool,
  ChatCompletionToolMessageParam,
} from 'openai/resources/index.mjs';
import { Message } from '@/lib/types';
import { repairJson } from '@toolsycc/json-repair';

type OpenAIConfig = {
  apiKey: string;
  model: string;
  baseURL?: string;
  options?: GenerateOptions;
};

class OpenAILLM extends BaseLLM<OpenAIConfig> {
  openAIClient: OpenAI;

  constructor(protected config: OpenAIConfig) {
    super(config);

    this.openAIClient = new OpenAI({
      apiKey: this.config.apiKey,
      baseURL: this.config.baseURL || 'https://api.openai.com/v1',
    });
  }

  convertToOpenAIMessages(messages: Message[]): ChatCompletionMessageParam[] {
    return messages.map((msg) => {
      if (msg.role === 'tool') {
        return {
          role: 'tool',
          tool_call_id: msg.id,
          content: msg.content,
        } as ChatCompletionToolMessageParam;
      } else if (msg.role === 'assistant') {
        return {
          role: 'assistant',
          content: msg.content,
          ...(msg.tool_calls &&
            msg.tool_calls.length > 0 && {
              tool_calls: msg.tool_calls?.map((tc) => ({
                id: tc.id,
                type: 'function',
                function: {
                  name: tc.name,
                  arguments: JSON.stringify(tc.arguments),
                },
              })),
            }),
        } as ChatCompletionAssistantMessageParam;
      }

      return msg;
    });
  }

  async generateText(input: GenerateTextInput): Promise<GenerateTextOutput> {
    const openaiTools: ChatCompletionTool[] = [];

    input.tools?.forEach((tool) => {
      openaiTools.push({
        type: 'function',
        function: {
          name: tool.name,
          description: tool.description,
          parameters: z.toJSONSchema(tool.schema),
        },
      });
    });

    const response = await this.openAIClient.chat.completions.create({
      model: this.config.model,
      tools: openaiTools.length > 0 ? openaiTools : undefined,
      messages: this.convertToOpenAIMessages(input.messages),
      temperature:
        input.options?.temperature ?? this.config.options?.temperature ?? 1.0,
      top_p: input.options?.topP ?? this.config.options?.topP,
      max_completion_tokens:
        input.options?.maxTokens ?? this.config.options?.maxTokens,
      stop: input.options?.stopSequences ?? this.config.options?.stopSequences,
      frequency_penalty:
        input.options?.frequencyPenalty ??
        this.config.options?.frequencyPenalty,
      presence_penalty:
        input.options?.presencePenalty ?? this.config.options?.presencePenalty,
    });

    if (response.choices && response.choices.length > 0) {
      return {
        content: response.choices[0].message.content!,
        toolCalls:
          response.choices[0].message.tool_calls
            ?.map((tc) => {
              if (tc.type === 'function') {
                return {
                  name: tc.function.name,
                  id: tc.id,
                  arguments: JSON.parse(tc.function.arguments),
                };
              }
            })
            .filter((tc) => tc !== undefined) || [],
        additionalInfo: {
          finishReason: response.choices[0].finish_reason,
        },
      };
    }

    throw new Error('No response from OpenAI');
  }

  async *streamText(
    input: GenerateTextInput,
  ): AsyncGenerator<StreamTextOutput> {
    const openaiTools: ChatCompletionTool[] = [];

    input.tools?.forEach((tool) => {
      openaiTools.push({
        type: 'function',
        function: {
          name: tool.name,
          description: tool.description,
          parameters: z.toJSONSchema(tool.schema),
        },
      });
    });

    const stream = await this.openAIClient.chat.completions.create({
      model: this.config.model,
      messages: this.convertToOpenAIMessages(input.messages),
      tools: openaiTools.length > 0 ? openaiTools : undefined,
      temperature:
        input.options?.temperature ?? this.config.options?.temperature ?? 1.0,
      top_p: input.options?.topP ?? this.config.options?.topP,
      max_completion_tokens:
        input.options?.maxTokens ?? this.config.options?.maxTokens,
      stop: input.options?.stopSequences ?? this.config.options?.stopSequences,
      frequency_penalty:
        input.options?.frequencyPenalty ??
        this.config.options?.frequencyPenalty,
      presence_penalty:
        input.options?.presencePenalty ?? this.config.options?.presencePenalty,
      stream: true,
    });

    let recievedToolCalls: { name: string; id: string; arguments: string }[] =
      [];

    for await (const chunk of stream) {
      if (chunk.choices && chunk.choices.length > 0) {
        const toolCalls = chunk.choices[0].delta.tool_calls;
        yield {
          contentChunk: chunk.choices[0].delta.content || '',
          toolCallChunk:
            toolCalls?.map((tc) => {
              if (!recievedToolCalls[tc.index]) {
                const call = {
                  name: tc.function?.name!,
                  id: tc.id!,
                  arguments: tc.function?.arguments || '',
                };
                recievedToolCalls.push(call);
                return { ...call, arguments: parse(call.arguments || '{}') };
              } else {
                const existingCall = recievedToolCalls[tc.index];
                existingCall.arguments += tc.function?.arguments || '';
                return {
                  ...existingCall,
                  arguments: parse(existingCall.arguments),
                };
              }
            }) || [],
          done: chunk.choices[0].finish_reason !== null,
          additionalInfo: {
            finishReason: chunk.choices[0].finish_reason,
          },
        };
      }
    }
  }

  async generateObject<T>(input: GenerateObjectInput): Promise<T> {
    const response = await this.openAIClient.chat.completions.parse({
      messages: this.convertToOpenAIMessages(input.messages),
      model: this.config.model,
      temperature:
        input.options?.temperature ?? this.config.options?.temperature ?? 1.0,
      top_p: input.options?.topP ?? this.config.options?.topP,
      max_completion_tokens:
        input.options?.maxTokens ?? this.config.options?.maxTokens,
      stop: input.options?.stopSequences ?? this.config.options?.stopSequences,
      frequency_penalty:
        input.options?.frequencyPenalty ??
        this.config.options?.frequencyPenalty,
      presence_penalty:
        input.options?.presencePenalty ?? this.config.options?.presencePenalty,
      response_format: zodResponseFormat(input.schema, 'object'),
    });

    if (response.choices && response.choices.length > 0) {
      try {
        return input.schema.parse(
          JSON.parse(
            repairJson(response.choices[0].message.content!, {
              extractJson: true,
            }) as string,
          ),
        ) as T;
      } catch (err) {
        throw new Error(`Error parsing response from OpenAI: ${err}`);
      }
    }

    throw new Error('No response from OpenAI');
  }

  async *streamObject<T>(input: GenerateObjectInput): AsyncGenerator<T> {
    let recievedObj: string = '';

    const stream = this.openAIClient.responses.stream({
      model: this.config.model,
      input: input.messages,
      temperature:
        input.options?.temperature ?? this.config.options?.temperature ?? 1.0,
      top_p: input.options?.topP ?? this.config.options?.topP,
      max_completion_tokens:
        input.options?.maxTokens ?? this.config.options?.maxTokens,
      stop: input.options?.stopSequences ?? this.config.options?.stopSequences,
      frequency_penalty:
        input.options?.frequencyPenalty ??
        this.config.options?.frequencyPenalty,
      presence_penalty:
        input.options?.presencePenalty ?? this.config.options?.presencePenalty,
      text: {
        format: zodTextFormat(input.schema, 'object'),
      },
    });

    for await (const chunk of stream) {
      if (chunk.type === 'response.output_text.delta' && chunk.delta) {
        recievedObj += chunk.delta;

        try {
          yield parse(recievedObj) as T;
        } catch (err) {
          console.log('Error parsing partial object from OpenAI:', err);
          yield {} as T;
        }
      } else if (chunk.type === 'response.output_text.done' && chunk.text) {
        try {
          yield parse(chunk.text) as T;
        } catch (err) {
          throw new Error(`Error parsing response from OpenAI: ${err}`);
        }
      }
    }
  }
}

export default OpenAILLM;
```

## File: `src/lib/models/providers/transformers/index.ts`
```typescript
import { UIConfigField } from '@/lib/config/types';
import { getConfiguredModelProviderById } from '@/lib/config/serverRegistry';
import { Model, ModelList, ProviderMetadata } from '../../types';
import BaseModelProvider from '../../base/provider';
import BaseLLM from '../../base/llm';
import BaseEmbedding from '../../base/embedding';
import TransformerEmbedding from './transformerEmbedding';

interface TransformersConfig {}

const defaultEmbeddingModels: Model[] = [
  {
    name: 'all-MiniLM-L6-v2',
    key: 'Xenova/all-MiniLM-L6-v2',
  },
  {
    name: 'mxbai-embed-large-v1',
    key: 'mixedbread-ai/mxbai-embed-large-v1',
  },
  {
    name: 'nomic-embed-text-v1',
    key: 'Xenova/nomic-embed-text-v1',
  },
];

const providerConfigFields: UIConfigField[] = [];

class TransformersProvider extends BaseModelProvider<TransformersConfig> {
  constructor(id: string, name: string, config: TransformersConfig) {
    super(id, name, config);
  }

  async getDefaultModels(): Promise<ModelList> {
    return {
      embedding: [...defaultEmbeddingModels],
      chat: [],
    };
  }

  async getModelList(): Promise<ModelList> {
    const defaultModels = await this.getDefaultModels();
    const configProvider = getConfiguredModelProviderById(this.id)!;

    return {
      embedding: [
        ...defaultModels.embedding,
        ...configProvider.embeddingModels,
      ],
      chat: [],
    };
  }

  async loadChatModel(key: string): Promise<BaseLLM<any>> {
    throw new Error('Transformers Provider does not support chat models.');
  }

  async loadEmbeddingModel(key: string): Promise<BaseEmbedding<any>> {
    const modelList = await this.getModelList();
    const exists = modelList.embedding.find((m) => m.key === key);

    if (!exists) {
      throw new Error(
        'Error Loading OpenAI Embedding Model. Invalid Model Selected.',
      );
    }

    return new TransformerEmbedding({
      model: key,
    });
  }

  static parseAndValidate(raw: any): TransformersConfig {
    return {};
  }

  static getProviderConfigFields(): UIConfigField[] {
    return providerConfigFields;
  }

  static getProviderMetadata(): ProviderMetadata {
    return {
      key: 'transformers',
      name: 'Transformers',
    };
  }
}

export default TransformersProvider;
```

## File: `src/lib/models/providers/transformers/transformerEmbedding.ts`
```typescript
import { Chunk } from '@/lib/types';
import BaseEmbedding from '../../base/embedding';
import { FeatureExtractionPipeline } from '@huggingface/transformers';

type TransformerConfig = {
  model: string;
};

class TransformerEmbedding extends BaseEmbedding<TransformerConfig> {
  private pipelinePromise: Promise<FeatureExtractionPipeline> | null = null;

  constructor(protected config: TransformerConfig) {
    super(config);
  }

  async embedText(texts: string[]): Promise<number[][]> {
    return this.embed(texts);
  }

  async embedChunks(chunks: Chunk[]): Promise<number[][]> {
    return this.embed(chunks.map((c) => c.content));
  }

  private async embed(texts: string[]) {
    if (!this.pipelinePromise) {
      this.pipelinePromise = (async () => {
        const { pipeline } = await import('@huggingface/transformers');
        const result = await pipeline('feature-extraction', this.config.model, {
          dtype: 'fp32',
        });
        return result as FeatureExtractionPipeline;
      })();
    }

    const pipe = await this.pipelinePromise;
    const output = await pipe(texts, { pooling: 'mean', normalize: true });
    return output.tolist() as number[][];
  }
}

export default TransformerEmbedding;
```

## File: `src/lib/prompts/media/image.ts`
```typescript
import { ChatTurnMessage } from '@/lib/types';

export const imageSearchPrompt = `
You will be given a conversation below and a follow up question. You need to rephrase the follow-up question so it is a standalone question that can be used by the LLM to search the web for images.
You need to make sure the rephrased question agrees with the conversation and is relevant to the conversation.
Make sure to make the querey standalone and not something very broad, use context from the answers in the conversation to make it specific so user can get best image search results.
Output only the rephrased query in query key JSON format. Do not include any explanation or additional text.
`;

export const imageSearchFewShots: ChatTurnMessage[] = [
  {
    role: 'user',
    content:
      '<conversation>\n</conversation>\n<follow_up>\nWhat is a cat?\n</follow_up>',
  },
  { role: 'assistant', content: '{"query":"A cat"}' },

  {
    role: 'user',
    content:
      '<conversation>\n</conversation>\n<follow_up>\nWhat is a car? How does it work?\n</follow_up>',
  },
  { role: 'assistant', content: '{"query":"Car working"}' },
  {
    role: 'user',
    content:
      '<conversation>\n</conversation>\n<follow_up>\nHow does an AC work?\n</follow_up>',
  },
  { role: 'assistant', content: '{"query":"AC working"}' },
];
```

## File: `src/lib/prompts/media/videos.ts`
```typescript
import { ChatTurnMessage } from '@/lib/types';

export const videoSearchPrompt = `
You will be given a conversation below and a follow up question. You need to rephrase the follow-up question so it is a standalone question that can be used by the LLM to search Youtube for videos.
You need to make sure the rephrased question agrees with the conversation and is relevant to the conversation.
Make sure to make the querey standalone and not something very broad, use context from the answers in the conversation to make it specific so user can get best video search results.
Output only the rephrased query in query key JSON format. Do not include any explanation or additional text.
`;

export const videoSearchFewShots: ChatTurnMessage[] = [
  {
    role: 'user',
    content:
      '<conversation>\n</conversation>\n<follow_up>\nHow does a car work?\n</follow_up>',
  },
  { role: 'assistant', content: '{"query":"How does a car work?"}' },
  {
    role: 'user',
    content:
      '<conversation>\n</conversation>\n<follow_up>\nWhat is the theory of relativity?\n</follow_up>',
  },
  { role: 'assistant', content: '{"query":"Theory of relativity"}' },
  {
    role: 'user',
    content:
      '<conversation>\n</conversation>\n<follow_up>\nHow does an AC work?\n</follow_up>',
  },
  { role: 'assistant', content: '{"query":"AC working"}' },
];
```

## File: `src/lib/prompts/search/classifier.ts`
```typescript
export const classifierPrompt = `
<role>
Assistant is an advanced AI system designed to analyze the user query and the conversation history to determine the most appropriate classification for the search operation.
It will be shared a detailed conversation history and a user query and it has to classify the query based on the guidelines and label definitions provided. You also have to generate a standalone follow-up question that is self-contained and context-independent.
</role>

<labels>
NOTE: BY GENERAL KNOWLEDGE WE MEAN INFORMATION THAT IS OBVIOUS, WIDELY KNOWN, OR CAN BE INFERRED WITHOUT EXTERNAL SOURCES FOR EXAMPLE MATHEMATICAL FACTS, BASIC SCIENTIFIC KNOWLEDGE, COMMON HISTORICAL EVENTS, ETC.
1. skipSearch (boolean): Deeply analyze whether the user's query can be answered without performing any search.
   - Set it to true if the query is straightforward, factual, or can be answered based on general knowledge.
   - Set it to true for writing tasks or greeting messages that do not require external information.
   - Set it to true if weather, stock, or similar widgets can fully satisfy the user's request.
   - Set it to false if the query requires up-to-date information, specific details, or context that cannot be inferred from general knowledge.
   - ALWAYS SET SKIPSEARCH TO FALSE IF YOU ARE UNCERTAIN OR IF THE QUERY IS AMBIGUOUS OR IF YOU'RE NOT SURE.
2. personalSearch (boolean): Determine if the query requires searching through user uploaded documents.
   - Set it to true if the query explicitly references or implies the need to access user-uploaded documents for example "Determine the key points from the document I uploaded about..." or "Who is the author?", "Summarize the content of the document"
   - Set it to false if the query does not reference user-uploaded documents or if the information can be obtained through general web search.
   - ALWAYS SET PERSONALSEARCH TO FALSE IF YOU ARE UNCERTAIN OR IF THE QUERY IS AMBIGUOUS OR IF YOU'RE NOT SURE. AND SET SKIPSEARCH TO FALSE AS WELL.
3. academicSearch (boolean): Assess whether the query requires searching academic databases or scholarly articles.
   - Set it to true if the query explicitly requests scholarly information, research papers, academic articles, or citations for example "Find recent studies on...", "What does the latest research say about...", or "Provide citations for..."
   - Set it to false if the query can be answered through general web search or does not specifically request academic sources.
4. discussionSearch (boolean): Evaluate if the query necessitates searching through online forums, discussion boards, or community Q&A platforms.
   - Set it to true if the query seeks opinions, personal experiences, community advice, or discussions for example "What do people think about...", "Are there any discussions on...", or "What are the common issues faced by..."
   - Set it to true if they're asking for reviews or feedback from users on products, services, or experiences.
   - Set it to false if the query can be answered through general web search or does not specifically request information from discussion platforms.
5. showWeatherWidget (boolean): Decide if displaying a weather widget would adequately address the user's query.
   - Set it to true if the user's query is specifically about current weather conditions, forecasts, or any weather-related information for a particular location.
   - Set it to true for queries like "What's the weather like in [Location]?" or "Will it rain tomorrow in [Location]?" or "Show me the weather" (Here they mean weather of their current location).
   - If it can fully answer the user query without needing additional search, set skipSearch to true as well.
6. showStockWidget (boolean): Determine if displaying a stock market widget would sufficiently fulfill the user's request.
   - Set it to true if the user's query is specifically about current stock prices or stock related information for particular companies. Never use it for a market analysis or news about stock market.
   - Set it to true for queries like "What's the stock price of [Company]?" or "How is the [Stock] performing today?" or "Show me the stock prices" (Here they mean stocks of companies they are interested in).
   - If it can fully answer the user query without needing additional search, set skipSearch to true as well.
7. showCalculationWidget (boolean): Decide if displaying a calculation widget would adequately address the user's query.
   - Set it to true if the user's query involves mathematical calculations, conversions, or any computation-related tasks.
   - Set it to true for queries like "What is 25% of 80?" or "Convert 100 USD to EUR" or "Calculate the square root of 256" or "What is 2 * 3 + 5?" or other mathematical expressions.
   - If it can fully answer the user query without needing additional search, set skipSearch to true as well.
</labels>

<standalone_followup>
For the standalone follow up, you have to generate a self contained, context independant reformulation of the user's query.
You basically have to rephrase the user's query in a way that it can be understood without any prior context from the conversation history.
Say for example the converastion is about cars and the user says "How do they work" then the standalone follow up should be "How do cars work?"

Do not contain excess information or everything that has been discussed before, just reformulate the user's last query in a self contained manner.
The standalone follow-up should be concise and to the point.
</standalone_followup>

<output_format>
You must respond in the following JSON format without any extra text, explanations or filler sentences:
{
  "classification": {
    "skipSearch": boolean,
    "personalSearch": boolean,
    "academicSearch": boolean,
    "discussionSearch": boolean,
    "showWeatherWidget": boolean,
    "showStockWidget": boolean,
    "showCalculationWidget": boolean,
  },
  "standaloneFollowUp": string
}
</output_format>
`;
```

## File: `src/lib/prompts/search/researcher.ts`
```typescript
import BaseEmbedding from '@/lib/models/base/embedding';
import UploadStore from '@/lib/uploads/store';

const getSpeedPrompt = (
  actionDesc: string,
  i: number,
  maxIteration: number,
  fileDesc: string,
) => {
  const today = new Date().toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  return `
  Assistant is an action orchestrator. Your job is to fulfill user requests by selecting and executing the available tools—no free-form replies.
  You will be shared with the conversation history between user and an AI, along with the user's latest follow-up question. Based on this, you must use the available tools to fulfill the user's request.

  Today's date: ${today}

  You are currently on iteration ${i + 1} of your research process and have ${maxIteration} total iterations so act efficiently.
  When you are finished, you must call the \`done\` tool. Never output text directly.

  <goal>
  Fulfill the user's request as quickly as possible using the available tools.
  Call tools to gather information or perform tasks as needed.
  </goal>

  <core_principle>
  Your knowledge is outdated; if you have web search, use it to ground answers even for seemingly basic facts.
  </core_principle>

  <examples>

  ## Example 1: Unknown Subject
  User: "What is Kimi K2?"
  Action: web_search ["Kimi K2", "Kimi K2 AI"] then done.

  ## Example 2: Subject You're Uncertain About
  User: "What are the features of GPT-5.1?"
  Action: web_search ["GPT-5.1", "GPT-5.1 features", "GPT-5.1 release"] then done.

  ## Example 3: After Tool calls Return Results
  User: "What are the features of GPT-5.1?"
  [Previous tool calls returned the needed info]
  Action: done.

  </examples>

  <available_tools>
  ${actionDesc}
  </available_tools>

  <mistakes_to_avoid>

1. **Over-assuming**: Don't assume things exist or don't exist - just look them up

2. **Verification obsession**: Don't waste tool calls "verifying existence" - just search for the thing directly

3. **Endless loops**: If 2-3 tool calls don't find something, it probably doesn't exist - report that and move on

4. **Ignoring task context**: If user wants a calendar event, don't just search - create the event

5. **Overthinking**: Keep reasoning simple and tool calls focused

</mistakes_to_avoid>

  <response_protocol>
- NEVER output normal text to the user. ONLY call tools.
- Choose the appropriate tools based on the action descriptions provided above.
- Default to web_search when information is missing or stale; keep queries targeted (max 3 per call).
- Call done when you have gathered enough to answer or performed the required actions.
- Do not invent tools. Do not return JSON.
  </response_protocol>

  ${
    fileDesc.length > 0
      ? `<user_uploaded_files>
  The user has uploaded the following files which may be relevant to their request:
  ${fileDesc}
  You can use the uploaded files search tool to look for information within these documents if needed.
  </user_uploaded_files>`
      : ''
  }
  `;
};

const getBalancedPrompt = (
  actionDesc: string,
  i: number,
  maxIteration: number,
  fileDesc: string,
) => {
  const today = new Date().toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  return `
  Assistant is an action orchestrator. Your job is to fulfill user requests by reasoning briefly and executing the available tools—no free-form replies.
  You will be shared with the conversation history between user and an AI, along with the user's latest follow-up question. Based on this, you must use the available tools to fulfill the user's request.

  Today's date: ${today}

  You are currently on iteration ${i + 1} of your research process and have ${maxIteration} total iterations so act efficiently.
  When you are finished, you must call the \`done\` tool. Never output text directly.

  <goal>
  Fulfill the user's request with concise reasoning plus focused actions.
  You must call the __reasoning_preamble tool before every tool call in this assistant turn. Alternate: __reasoning_preamble → tool → __reasoning_preamble → tool ... and finish with __reasoning_preamble → done. Open each __reasoning_preamble with a brief intent phrase (e.g., "Okay, the user wants to...", "Searching for...", "Looking into...") and lay out your reasoning for the next step. Keep it natural language, no tool names.
  </goal>

  <core_principle>
  Your knowledge is outdated; if you have web search, use it to ground answers even for seemingly basic facts.
  You can call at most 6 tools total per turn: up to 2 reasoning (__reasoning_preamble counts as reasoning), 2-3 information-gathering calls, and 1 done. If you hit the cap, stop after done.
  Aim for at least two information-gathering calls when the answer is not already obvious; only skip the second if the question is trivial or you already have sufficient context.
  Do not spam searches—pick the most targeted queries.
  </core_principle>

  <done_usage>
  Call done only after the reasoning plus the necessary tool calls are completed and you have enough to answer. If you call done early, stop. If you reach the tool cap, call done to conclude.
  </done_usage>

  <examples>

  ## Example 1: Unknown Subject
  User: "What is Kimi K2?"
  Reason: "Okay, the user wants to know about Kimi K2. I will start by looking for what Kimi K2 is and its key details, then summarize the findings."
  Action: web_search ["Kimi K2", "Kimi K2 AI"] then reasoning then done.

  ## Example 2: Subject You're Uncertain About
  User: "What are the features of GPT-5.1?"
  Reason: "The user is asking about GPT-5.1 features. I will search for current feature and release information, then compile a summary."
  Action: web_search ["GPT-5.1", "GPT-5.1 features", "GPT-5.1 release"] then reasoning then done.

  ## Example 3: After Tool calls Return Results
  User: "What are the features of GPT-5.1?"
  [Previous tool calls returned the needed info]
  Reason: "I have gathered enough information about GPT-5.1 features; I will now wrap up."
  Action: done.

  </examples>

  <available_tools>
  YOU MUST CALL __reasoning_preamble BEFORE EVERY TOOL CALL IN THIS ASSISTANT TURN. IF YOU DO NOT CALL IT, THE TOOL CALL WILL BE IGNORED.
  ${actionDesc}
  </available_tools>

  <mistakes_to_avoid>

1. **Over-assuming**: Don't assume things exist or don't exist - just look them up

2. **Verification obsession**: Don't waste tool calls "verifying existence" - just search for the thing directly

3. **Endless loops**: If 2-3 tool calls don't find something, it probably doesn't exist - report that and move on

4. **Ignoring task context**: If user wants a calendar event, don't just search - create the event

5. **Overthinking**: Keep reasoning simple and tool calls focused

6. **Skipping the reasoning step**: Always call __reasoning_preamble first to outline your approach before other actions

</mistakes_to_avoid>

  <response_protocol>
- NEVER output normal text to the user. ONLY call tools.
- Start with __reasoning_preamble and call __reasoning_preamble before every tool call (including done): open with intent phrase ("Okay, the user wants to...", "Looking into...", etc.) and lay out your reasoning for the next step. No tool names.
- Choose tools based on the action descriptions provided above.
- Default to web_search when information is missing or stale; keep queries targeted (max 3 per call).
- Use at most 6 tool calls total (__reasoning_preamble + 2-3 info calls + __reasoning_preamble + done). If done is called early, stop.
- Do not stop after a single information-gathering call unless the task is trivial or prior results already cover the answer.
- Call done only after you have the needed info or actions completed; do not call it early.
- Do not invent tools. Do not return JSON.
  </response_protocol>

  ${
    fileDesc.length > 0
      ? `<user_uploaded_files>
  The user has uploaded the following files which may be relevant to their request:
  ${fileDesc}
  You can use the uploaded files search tool to look for information within these documents if needed.
  </user_uploaded_files>`
      : ''
  }
  `;
};

const getQualityPrompt = (
  actionDesc: string,
  i: number,
  maxIteration: number,
  fileDesc: string,
) => {
  const today = new Date().toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  return `
  Assistant is a deep-research orchestrator. Your job is to fulfill user requests with the most thorough, comprehensive research possible—no free-form replies.
  You will be shared with the conversation history between user and an AI, along with the user's latest follow-up question. Based on this, you must use the available tools to fulfill the user's request with depth and rigor.

  Today's date: ${today}

  You are currently on iteration ${i + 1} of your research process and have ${maxIteration} total iterations. Use every iteration wisely to gather comprehensive information.
  When you are finished, you must call the \`done\` tool. Never output text directly.

  <goal>
  Conduct the deepest, most thorough research possible. Leave no stone unturned.
  Follow an iterative reason-act loop: call __reasoning_preamble before every tool call to outline the next step, then call the tool, then __reasoning_preamble again to reflect and decide the next step. Repeat until you have exhaustive coverage.
  Open each __reasoning_preamble with a brief intent phrase (e.g., "Okay, the user wants to know about...", "From the results, it looks like...", "Now I need to dig into...") and describe what you'll do next. Keep it natural language, no tool names.
  Finish with done only when you have comprehensive, multi-angle information.
  </goal>

  <core_principle>
  Your knowledge is outdated; always use the available tools to ground answers.
  This is DEEP RESEARCH mode—be exhaustive. Explore multiple angles: definitions, features, comparisons, recent news, expert opinions, use cases, limitations, and alternatives.
  You can call up to 10 tools total per turn. Use an iterative loop: __reasoning_preamble → tool call(s) → __reasoning_preamble → tool call(s) → ... → __reasoning_preamble → done.
  Never settle for surface-level answers. If results hint at more depth, reason about your next step and follow up. Cross-reference information from multiple queries.
  </core_principle>

  <done_usage>
  Call done only after you have gathered comprehensive, multi-angle information. Do not call done early—exhaust your research budget first. If you reach the tool cap, call done to conclude.
  </done_usage>

  <examples>

  ## Example 1: Unknown Subject - Deep Dive
  User: "What is Kimi K2?"
  Reason: "Okay, the user wants to know about Kimi K2. I'll start by finding out what it is and its key capabilities."
  [calls info-gathering tool]
  Reason: "From the results, Kimi K2 is an AI model by Moonshot. Now I need to dig into how it compares to competitors and any recent news."
  [calls info-gathering tool]
  Reason: "Got comparison info. Let me also check for limitations or critiques to give a balanced view."
  [calls info-gathering tool]
  Reason: "I now have comprehensive coverage—definition, capabilities, comparisons, and critiques. Wrapping up."
  Action: done.

  ## Example 2: Feature Research - Comprehensive
  User: "What are the features of GPT-5.1?"
  Reason: "The user wants comprehensive GPT-5.1 feature information. I'll start with core features and specs."
  [calls info-gathering tool]
  Reason: "Got the basics. Now I should look into how it compares to GPT-4 and benchmark performance."
  [calls info-gathering tool]
  Reason: "Good comparison data. Let me also gather use cases and expert opinions for depth."
  [calls info-gathering tool]
  Reason: "I have exhaustive coverage across features, comparisons, benchmarks, and reviews. Done."
  Action: done.

  ## Example 3: Iterative Refinement
  User: "Tell me about quantum computing applications in healthcare."
  Reason: "Okay, the user wants to know about quantum computing in healthcare. I'll start with an overview of current applications."
  [calls info-gathering tool]
  Reason: "Results mention drug discovery and diagnostics. Let me dive deeper into drug discovery use cases."
  [calls info-gathering tool]
  Reason: "Now I'll explore the diagnostics angle and any recent breakthroughs."
  [calls info-gathering tool]
  Reason: "Comprehensive coverage achieved. Wrapping up."
  Action: done.

  </examples>

  <available_tools>
  YOU MUST CALL __reasoning_preamble BEFORE EVERY TOOL CALL IN THIS ASSISTANT TURN. IF YOU DO NOT CALL IT, THE TOOL CALL WILL BE IGNORED.
  ${actionDesc}
  </available_tools>

  <research_strategy>
  For any topic, consider searching:
  1. **Core definition/overview** - What is it?
  2. **Features/capabilities** - What can it do?
  3. **Comparisons** - How does it compare to alternatives?
  4. **Recent news/updates** - What's the latest?
  5. **Reviews/opinions** - What do experts say?
  6. **Use cases** - How is it being used?
  7. **Limitations/critiques** - What are the downsides?
  </research_strategy>

  <mistakes_to_avoid>

1. **Shallow research**: Don't stop after one or two searches—dig deeper from multiple angles

2. **Over-assuming**: Don't assume things exist or don't exist - just look them up

3. **Missing perspectives**: Search for both positive and critical viewpoints

4. **Ignoring follow-ups**: If results hint at interesting sub-topics, explore them

5. **Premature done**: Don't call done until you've exhausted reasonable research avenues

6. **Skipping the reasoning step**: Always call __reasoning_preamble first to outline your research strategy

</mistakes_to_avoid>

  <response_protocol>
- NEVER output normal text to the user. ONLY call tools.
- Follow an iterative loop: __reasoning_preamble → tool call → __reasoning_preamble → tool call → ... → __reasoning_preamble → done.
- Each __reasoning_preamble should reflect on previous results (if any) and state the next research step. No tool names in the reasoning.
- Choose tools based on the action descriptions provided above—use whatever tools are available to accomplish the task.
- Aim for 4-7 information-gathering calls covering different angles; cross-reference and follow up on interesting leads.
- Call done only after comprehensive, multi-angle research is complete.
- Do not invent tools. Do not return JSON.
  </response_protocol>

  ${
    fileDesc.length > 0
      ? `<user_uploaded_files>
  The user has uploaded the following files which may be relevant to their request:
  ${fileDesc}
  You can use the uploaded files search tool to look for information within these documents if needed.
  </user_uploaded_files>`
      : ''
  }
  `;
};

export const getResearcherPrompt = (
  actionDesc: string,
  mode: 'speed' | 'balanced' | 'quality',
  i: number,
  maxIteration: number,
  fileIds: string[],
) => {
  let prompt = '';

  const filesData = UploadStore.getFileData(fileIds);

  const fileDesc = filesData
    .map(
      (f) =>
        `<file><name>${f.fileName}</name><initial_content>${f.initialContent}</initial_content></file>`,
    )
    .join('\n');

  switch (mode) {
    case 'speed':
      prompt = getSpeedPrompt(actionDesc, i, maxIteration, fileDesc);
      break;
    case 'balanced':
      prompt = getBalancedPrompt(actionDesc, i, maxIteration, fileDesc);
      break;
    case 'quality':
      prompt = getQualityPrompt(actionDesc, i, maxIteration, fileDesc);
      break;
    default:
      prompt = getSpeedPrompt(actionDesc, i, maxIteration, fileDesc);
      break;
  }

  return prompt;
};
```

## File: `src/lib/prompts/search/writer.ts`
```typescript
export const getWriterPrompt = (
  context: string,
  systemInstructions: string,
  mode: 'speed' | 'balanced' | 'quality',
) => {
  return `
You are Vane, an AI model skilled in web search and crafting detailed, engaging, and well-structured answers. You excel at summarizing web pages and extracting relevant information to create professional, blog-style responses.

    Your task is to provide answers that are:
    - **Informative and relevant**: Thoroughly address the user's query using the given context.
    - **Well-structured**: Include clear headings and subheadings, and use a professional tone to present information concisely and logically.
    - **Engaging and detailed**: Write responses that read like a high-quality blog post, including extra details and relevant insights.
    - **Cited and credible**: Use inline citations with [number] notation to refer to the context source(s) for each fact or detail included.
    - **Explanatory and Comprehensive**: Strive to explain the topic in depth, offering detailed analysis, insights, and clarifications wherever applicable.

    ### Formatting Instructions
    - **Structure**: Use a well-organized format with proper headings (e.g., "## Example heading 1" or "## Example heading 2"). Present information in paragraphs or concise bullet points where appropriate.
    - **Tone and Style**: Maintain a neutral, journalistic tone with engaging narrative flow. Write as though you're crafting an in-depth article for a professional audience.
    - **Markdown Usage**: Format your response with Markdown for clarity. Use headings, subheadings, bold text, and italicized words as needed to enhance readability.
    - **Length and Depth**: Provide comprehensive coverage of the topic. Avoid superficial responses and strive for depth without unnecessary repetition. Expand on technical or complex topics to make them easier to understand for a general audience.
    - **No main heading/title**: Start your response directly with the introduction unless asked to provide a specific title.
    - **Conclusion or Summary**: Include a concluding paragraph that synthesizes the provided information or suggests potential next steps, where appropriate.

    ### Citation Requirements
    - Cite every single fact, statement, or sentence using [number] notation corresponding to the source from the provided \`context\`.
    - Integrate citations naturally at the end of sentences or clauses as appropriate. For example, "The Eiffel Tower is one of the most visited landmarks in the world[1]."
    - Ensure that **every sentence in your response includes at least one citation**, even when information is inferred or connected to general knowledge available in the provided context.
    - Use multiple sources for a single detail if applicable, such as, "Paris is a cultural hub, attracting millions of visitors annually[1][2]."
    - Always prioritize credibility and accuracy by linking all statements back to their respective context sources.
    - Avoid citing unsupported assumptions or personal interpretations; if no source supports a statement, clearly indicate the limitation.

    ### Special Instructions
    - If the query involves technical, historical, or complex topics, provide detailed background and explanatory sections to ensure clarity.
    - If the user provides vague input or if relevant information is missing, explain what additional details might help refine the search.
    - If no relevant information is found, say: "Hmm, sorry I could not find any relevant information on this topic. Would you like me to search again or ask something else?" Be transparent about limitations and suggest alternatives or ways to reframe the query.
    ${mode === 'quality' ? "- YOU ARE CURRENTLY SET IN QUALITY MODE, GENERATE VERY DEEP, DETAILED AND COMPREHENSIVE RESPONSES USING THE FULL CONTEXT PROVIDED. ASSISTANT'S RESPONSES SHALL NOT BE LESS THAN AT LEAST 2000 WORDS, COVER EVERYTHING AND FRAME IT LIKE A RESEARCH REPORT." : ''}
    
    ### User instructions
    These instructions are shared to you by the user and not by the system. You will have to follow them but give them less priority than the above instructions. If the user has provided specific instructions or preferences, incorporate them into your response while adhering to the overall guidelines.
    ${systemInstructions}

    ### Example Output
    - Begin with a brief introduction summarizing the event or query topic.
    - Follow with detailed sections under clear headings, covering all aspects of the query if possible.
    - Provide explanations or historical context as needed to enhance understanding.
    - End with a conclusion or overall perspective if relevant.

    <context>
    ${context}
    </context>

    Current date & time in ISO format (UTC timezone) is: ${new Date().toISOString()}.
`;
};
```

## File: `src/lib/prompts/suggestions/index.ts`
```typescript
export const suggestionGeneratorPrompt = `
You are an AI suggestion generator for an AI powered search engine. You will be given a conversation below. You need to generate 4-5 suggestions based on the conversation. The suggestion should be relevant to the conversation that can be used by the user to ask the chat model for more information.
You need to make sure the suggestions are relevant to the conversation and are helpful to the user. Keep a note that the user might use these suggestions to ask a chat model for more information. 
Make sure the suggestions are medium in length and are informative and relevant to the conversation.

Sample suggestions for a conversation about Elon Musk:
{
    "suggestions": [
        "What are Elon Musk's plans for SpaceX in the next decade?",
        "How has Tesla's stock performance been influenced by Elon Musk's leadership?",
        "What are the key innovations introduced by Elon Musk in the electric vehicle industry?",
        "How does Elon Musk's vision for renewable energy impact global sustainability efforts?"
    ]
}

Today's date is ${new Date().toISOString()}
`;
```

## File: `src/lib/uploads/manager.ts`
```typescript
import path from "path";
import BaseEmbedding from "../models/base/embedding"
import crypto from "crypto"
import fs from 'fs';
import { splitText } from "../utils/splitText";
import { PDFParse } from 'pdf-parse';
import { CanvasFactory } from 'pdf-parse/worker';
import officeParser from 'officeparser'

const supportedMimeTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'] as const

type SupportedMimeType = typeof supportedMimeTypes[number];

type UploadManagerParams = {
    embeddingModel: BaseEmbedding<any>;
}

type RecordedFile = {
    id: string;
    name: string;
    filePath: string;
    contentPath: string;
    uploadedAt: string;
}

type FileRes = {
    fileName: string;
    fileExtension: string;
    fileId: string;
}

class UploadManager {
    private embeddingModel: BaseEmbedding<any>;
    static uploadsDir = path.join(process.cwd(), 'data', 'uploads');
    static uploadedFilesRecordPath = path.join(this.uploadsDir, 'uploaded_files.json');

    constructor(private params: UploadManagerParams) {
        this.embeddingModel = params.embeddingModel;

        if (!fs.existsSync(UploadManager.uploadsDir)) {
            fs.mkdirSync(UploadManager.uploadsDir, { recursive: true });
        }

        if (!fs.existsSync(UploadManager.uploadedFilesRecordPath)) {
            const data = {
                files: []
            }

            fs.writeFileSync(UploadManager.uploadedFilesRecordPath, JSON.stringify(data, null, 2));
        }
    }

    private static getRecordedFiles(): RecordedFile[] {
        const data = fs.readFileSync(UploadManager.uploadedFilesRecordPath, 'utf-8');
        return JSON.parse(data).files;
    }

    private static addNewRecordedFile(fileRecord: RecordedFile) {
        const currentData = this.getRecordedFiles()

        currentData.push(fileRecord);

        fs.writeFileSync(UploadManager.uploadedFilesRecordPath, JSON.stringify({ files: currentData }, null, 2));
    }

    static getFile(fileId: string): RecordedFile | null {
        const recordedFiles = this.getRecordedFiles();

        return recordedFiles.find(f => f.id === fileId) || null;
    }

    static getFileChunks(fileId: string): { content: string; embedding: number[] }[] {
        try {
            const recordedFile = this.getFile(fileId);

            if (!recordedFile) {
                throw new Error(`File with ID ${fileId} not found`);
            }

            const contentData = JSON.parse(fs.readFileSync(recordedFile.contentPath, 'utf-8'))

            return contentData.chunks;
        } catch (err) {
            console.log('Error getting file chunks:', err);
            return [];
        }
    }

    private async extractContentAndEmbed(filePath: string, fileType: SupportedMimeType): Promise<string> {
        switch (fileType) {
            case 'text/plain':
                const content = fs.readFileSync(filePath, 'utf-8');

                const splittedText = splitText(content, 512, 128)
                const embeddings = await this.embeddingModel.embedText(splittedText)

                if (embeddings.length !== splittedText.length) {
                    throw new Error('Embeddings and text chunks length mismatch');
                }

                const contentPath = filePath.split('.').slice(0, -1).join('.') + '.content.json';

                const data = {
                    chunks: splittedText.map((text, i) => {
                        return {
                            content: text,
                            embedding: embeddings[i],
                        }
                    })
                }

                fs.writeFileSync(contentPath, JSON.stringify(data, null, 2));

                return contentPath;
            case 'application/pdf':
                const pdfBuffer = fs.readFileSync(filePath);

                const parser = new PDFParse({
                    data: pdfBuffer,
                    CanvasFactory
                })

                const pdfText = await parser.getText().then(res => res.text)

                const pdfSplittedText = splitText(pdfText, 512, 128)
                const pdfEmbeddings = await this.embeddingModel.embedText(pdfSplittedText)

                if (pdfEmbeddings.length !== pdfSplittedText.length) {
                    throw new Error('Embeddings and text chunks length mismatch');
                }

                const pdfContentPath = filePath.split('.').slice(0, -1).join('.') + '.content.json';

                const pdfData = {
                    chunks: pdfSplittedText.map((text, i) => {
                        return {
                            content: text,
                            embedding: pdfEmbeddings[i],
                        }
                    })
                }

                fs.writeFileSync(pdfContentPath, JSON.stringify(pdfData, null, 2));

                return pdfContentPath;
            case 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                const docBuffer = fs.readFileSync(filePath);

                const docText = await officeParser.parseOfficeAsync(docBuffer)

                const docSplittedText = splitText(docText, 512, 128)
                const docEmbeddings = await this.embeddingModel.embedText(docSplittedText)

                if (docEmbeddings.length !== docSplittedText.length) {
                    throw new Error('Embeddings and text chunks length mismatch');
                }

                const docContentPath = filePath.split('.').slice(0, -1).join('.') + '.content.json';

                const docData = {
                    chunks: docSplittedText.map((text, i) => {
                        return {
                            content: text,
                            embedding: docEmbeddings[i],
                        }
                    })
                }

                fs.writeFileSync(docContentPath, JSON.stringify(docData, null, 2));

                return docContentPath;
            default:
                throw new Error(`Unsupported file type: ${fileType}`);
        }
    }

    async processFiles(files: File[]): Promise<FileRes[]> {
        const processedFiles: FileRes[] = [];

        await Promise.all(files.map(async (file) => {
            if (!(supportedMimeTypes as unknown as string[]).includes(file.type)) {
                throw new Error(`File type ${file.type} not supported`);
            }

            const fileId = crypto.randomBytes(16).toString('hex');

            const fileExtension = file.name.split('.').pop();
            const fileName = `${crypto.randomBytes(16).toString('hex')}.${fileExtension}`;
            const filePath = path.join(UploadManager.uploadsDir, fileName);

            const buffer = Buffer.from(await file.arrayBuffer())

            fs.writeFileSync(filePath, buffer);

            const contentFilePath = await this.extractContentAndEmbed(filePath, file.type as SupportedMimeType);

            const fileRecord: RecordedFile = {
                id: fileId,
                name: file.name,
                filePath: filePath,
                contentPath: contentFilePath,
                uploadedAt: new Date().toISOString(),
            }

            UploadManager.addNewRecordedFile(fileRecord);

            processedFiles.push({
                fileExtension: fileExtension || '',
                fileId,
                fileName: file.name
            });
        }))

        return processedFiles;
    }
}

export default UploadManager;
```

## File: `src/lib/uploads/store.ts`
```typescript
import BaseEmbedding from "../models/base/embedding";
import UploadManager from "./manager";
import computeSimilarity from "../utils/computeSimilarity";
import { Chunk } from "../types";
import { hashObj } from '../utils/hash';

type UploadStoreParams = {
    embeddingModel: BaseEmbedding<any>;
    fileIds: string[];
}

type StoreRecord = {
    embedding: number[];
    content: string;
    fileId: string;
    metadata: Record<string, any>
}

class UploadStore {
    embeddingModel: BaseEmbedding<any>;
    fileIds: string[];
    records: StoreRecord[] = [];

    constructor(private params: UploadStoreParams) {
        this.embeddingModel = params.embeddingModel;
        this.fileIds = params.fileIds;
        this.initializeStore()
    }

    initializeStore() {
        this.fileIds.forEach((fileId) => {
            const file = UploadManager.getFile(fileId)

            if (!file) {
                throw new Error(`File with ID ${fileId} not found`);
            }

            const chunks = UploadManager.getFileChunks(fileId);

            this.records.push(...chunks.map((chunk) => ({
                embedding: chunk.embedding,
                content: chunk.content,
                fileId: fileId,
                metadata: {
                    fileName: file.name,
                    title: file.name,
                    url: `file_id://${file.id}`,
                }
            })))
        })
    }

    async query(queries: string[], topK: number): Promise<Chunk[]> {
        const queryEmbeddings = await this.embeddingModel.embedText(queries)

        const results: { chunk: Chunk; score: number; }[][] = [];
        const hashResults: string[][] = []

        await Promise.all(queryEmbeddings.map(async (query) => {
            const similarities = this.records.map((record, idx) => {
                return {
                    chunk: {
                        content: record.content,
                        metadata: {
                            ...record.metadata,
                            fileId: record.fileId,
                        }
                    },
                    score: computeSimilarity(query, record.embedding)
                } as { chunk: Chunk; score: number; };
            }).sort((a, b) => b.score - a.score)

            results.push(similarities)
            hashResults.push(similarities.map(s => hashObj(s)))
        }))

        const chunkMap: Map<string, Chunk> = new Map();
        const scoreMap: Map<string, number> = new Map();
        const k = 60;

        for (let i = 0; i < results.length; i++) {
            for (let j = 0; j < results[i].length; j++) {
                const chunkHash = hashResults[i][j]

                chunkMap.set(chunkHash, results[i][j].chunk);
                scoreMap.set(chunkHash, (scoreMap.get(chunkHash) || 0) + results[i][j].score / (j + 1 + k));
            }
        }

        const finalResults = Array.from(scoreMap.entries())
            .sort((a, b) => b[1] - a[1])
            .map(([chunkHash, _score]) => {
                return chunkMap.get(chunkHash)!;
            })

        return finalResults.slice(0, topK);
    }

    static getFileData(fileIds: string[]): { fileName: string; initialContent: string }[] {
        const filesData: { fileName: string; initialContent: string }[] = [];

        fileIds.forEach((fileId) => {
            const file = UploadManager.getFile(fileId)

            if (!file) {
                throw new Error(`File with ID ${fileId} not found`);
            }

            const chunks = UploadManager.getFileChunks(fileId);

            filesData.push({
                fileName: file.name,
                initialContent: chunks.slice(0, 3).map(c => c.content).join('\n---\n'),
            })
        })

        return filesData
    }
}

export default UploadStore
```

## File: `src/lib/utils/computeSimilarity.ts`
```typescript
const computeSimilarity = (x: number[], y: number[]): number => {
  if (x.length !== y.length)
    throw new Error('Vectors must be of the same length');

  let dotProduct = 0;
  let normA = 0;
  let normB = 0;

  for (let i = 0; i < x.length; i++) {
    dotProduct += x[i] * y[i];
    normA += x[i] * x[i];
    normB += y[i] * y[i];
  }

  if (normA === 0 || normB === 0) {
    return 0;
  }

  return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
};

export default computeSimilarity;
```

## File: `src/lib/utils/files.ts`
```typescript
import path from 'path';
import fs from 'fs';

export const getFileDetails = (fileId: string) => {
  const fileLoc = path.join(
    process.cwd(),
    './uploads',
    fileId + '-extracted.json',
  );

  const parsedFile = JSON.parse(fs.readFileSync(fileLoc, 'utf8'));

  return {
    name: parsedFile.title,
    fileId: fileId,
  };
};
```

## File: `src/lib/utils/formatHistory.ts`
```typescript
import { ChatTurnMessage } from '../types';

const formatChatHistoryAsString = (history: ChatTurnMessage[]) => {
  return history
    .map(
      (message) =>
        `${message.role === 'assistant' ? 'AI' : 'User'}: ${message.content}`,
    )
    .join('\n');
};

export default formatChatHistoryAsString;
```

## File: `src/lib/utils/hash.ts`
```typescript
import crypto from 'crypto';

export const hashObj = (obj: { [key: string]: any }) => {
  const json = JSON.stringify(obj, Object.keys(obj).sort());
  const hash = crypto.createHash('sha256').update(json).digest('hex');
  return hash;
};
```

## File: `src/lib/utils/splitText.ts`
```typescript
import { getEncoding } from 'js-tiktoken';

const splitRegex = /(?<=\. |\n|! |\? |; |:\s|\d+\.\s|- |\* )/g;

const enc = getEncoding('cl100k_base');

const getTokenCount = (text: string): number => {
  try {
    return enc.encode(text).length;
  } catch {
    return Math.ceil(text.length / 4);
  }
};

export const splitText = (
  text: string,
  maxTokens = 512,
  overlapTokens = 64,
): string[] => {
  const segments = text.split(splitRegex).filter(Boolean);

  if (segments.length === 0) {
    return [];
  }

  const segmentTokenCounts = segments.map(getTokenCount);

  const result: string[] = [];

  let chunkStart = 0;

  while (chunkStart < segments.length) {
    let chunkEnd = chunkStart;
    let currentTokenCount = 0;

    while (chunkEnd < segments.length && currentTokenCount < maxTokens) {
      if (currentTokenCount + segmentTokenCounts[chunkEnd] > maxTokens) {
        break;
      }

      currentTokenCount += segmentTokenCounts[chunkEnd];
      chunkEnd++;
    }

    let overlapBeforeStart = Math.max(0, chunkStart - 1);
    let overlapBeforeTokenCount = 0;

    while (overlapBeforeStart >= 0 && overlapBeforeTokenCount < overlapTokens) {
      if (
        overlapBeforeTokenCount + segmentTokenCounts[overlapBeforeStart] >
        overlapTokens
      ) {
        break;
      }

      overlapBeforeTokenCount += segmentTokenCounts[overlapBeforeStart];
      overlapBeforeStart--;
    }

    const overlapStartIndex = Math.max(0, overlapBeforeStart + 1);

    const overlapBeforeContent = segments
      .slice(overlapStartIndex, chunkStart)
      .join('');

    const chunkContent = segments.slice(chunkStart, chunkEnd).join('');

    result.push(overlapBeforeContent + chunkContent);

    chunkStart = chunkEnd;
  }

  return result;
};
```


---
id: firecrawl-discord-bot
type: knowledge
owner: OA_Triage
---
# firecrawl-discord-bot
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "firecrawl-discord-bot",
  "version": "1.0.0",
  "description": "Firecrawl Discord Bot to turn websites into LLM-ready data",
  "main": "dist/index.js",
  "scripts": {
    "start": "ts-node src/index.ts",
    "build": "tsc",
    "lint": "eslint . --ext .ts",
    "lint:fix": "eslint . --ext .ts --fix",
    "format": "prettier --write \"src/**/*.ts\"",
    "format:check": "prettier --check \"src/**/*.ts\""
  },
  "dependencies": {
    "@mendable/firecrawl-js": "^1.23.9",
    "discord.js": "^14.13.0",
    "dotenv": "^16.3.1"
  },
  "devDependencies": {
    "@typescript-eslint/eslint-plugin": "^8.30.1",
    "@typescript-eslint/parser": "^8.30.1",
    "eslint": "^8.57.0",
    "lint-staged": "^15.5.1",
    "prettier": "^3.5.3",
    "ts-node": "^10.9.2",
    "typescript": "^5.3.3"
  },
  "packageManager": "pnpm@10.5.2",
  "keywords": [
    "firecrawl",
    "scrape",
    "sideguide",
    "mendable",
    "discord",
    "bot",
    "crawler",
    "web",
    "scraper"
  ],
  "license": "MIT",
  "homepage": "https://www.firecrawl.dev",
  "author": {
    "name": "Ademílson Tonato",
    "email": "ademilsonft@outlook.com"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/mendableai/firecrawl-discord-bot.git"
  },
  "engines": {
    "node": ">=18.x"
  },
  "lint-staged": {
    "*.ts": [
      "prettier --write",
      "eslint --fix"
    ]
  }
}

```

### File: README.md
```md
# Firecrawl Discord Bot

A Discord bot to turn websites into LLM-ready data using the Firecrawl API.

🔥 _Add Firecrawl Bot to your channel_ - https://firecrawl.link/discord-bot

## Features

- Scrape websites with advanced options
- Map URLs from a starting point
- Extract structured data from web pages
- Support for custom actions and parameters
- Beautiful JSON responses

## Prerequisites

- Node.js 18 or higher
- pnpm
- A Discord bot token
- A Firecrawl API key (Get yours by creating an account at [Firecrawl Dashboard](https://www.firecrawl.dev/app/api-keys))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mendableai/firecrawl-discord-bot.git
cd firecrawl-discord-bot
```

2. Install dependencies:
```bash
pnpm install
```

3. Build the TypeScript code:
```bash
pnpm build
```

## Usage

1. Start the bot:
```bash
pnpm start
```

2. For development with linting and formatting:
```bash
pnpm lint      # Check for linting issues
pnpm lint:fix  # Fix linting issues
pnpm format    # Format code
```

## Available Commands

### /set-api-key
Set your Firecrawl API key (required before using other commands).
```
/set-api-key key YOUR_API_KEY
```

### /scrape
Scrape a webpage with various options. [Documentation](https://docs.firecrawl.dev/api-reference/endpoint/scrape)

Example:
```json
{
  "url": "https://example.com",
  "formats": ["markdown", "html"],
  "onlyMainContent": true,
  "waitFor": 1000,
  "includeTags": ["article", "main"],
  "excludeTags": ["nav", "footer"],
  "mobile": false,
  "removeBase64Images": true,
  "skipTlsVerification": false,
  "timeout": 30000,
  "agent": {
    "model": "FIRE-1",
    "prompt": "Your custom prompt here"
  }
}
```

### /map
Map URLs from a starting point. [Documentation](https://docs.firecrawl.dev/api-reference/endpoint/map)

Example:
```json
{
  "url": "https://example.com",
  "search": "optional search term",
  "ignoreSitemap": true,
  "sitemapOnly": false,
  "includeSubdomains": false,
  "limit": 5000
}
```

### /extract
Extract structured data from webpages. [Documentation](https://docs.firecrawl.dev/api-reference/endpoint/extract)

Example:
```json
{
  "urls": ["https://example.com"],
  "prompt": "Extract product information",
  "schema": {
    "name": "string",
    "price": "number",
    "description": "string"
  },
  "agent": {
    "model": "FIRE-1"
  }
}
```

### /docs
Get the link to the Firecrawl documentation.

### /help
Display help information about available commands and their usage.

## Configuration

The bot uses the following environment variables:

- `DISCORD_TOKEN`: Your Discord bot token
- `CLIENT_ID`: Your Discord application client ID

To set up the environment variables:

1. Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```

2. Edit the `.env` file and replace the placeholder values with your actual tokens:
```
DISCORD_TOKEN=your_discord_bot_token
CLIENT_ID=your_discord_client_id
```

## License

MIT 

```

### File: .eslintrc.json
```json
{
  "env": {
    "node": true,
    "es2021": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "plugins": ["@typescript-eslint"],
  "rules": {
    "@typescript-eslint/no-explicit-any": "warn",
    "@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_" }]
  }
} 
```

### File: LICENSE.md
```md
MIT License

Copyright (c) 2025 Firecrawl

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

### File: pnpm-lock.yaml
```yaml
lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    dependencies:
      '@mendable/firecrawl-js':
        specifier: ^1.23.9
        version: 1.23.9
      discord.js:
        specifier: ^14.13.0
        version: 14.18.0
      dotenv:
        specifier: ^16.3.1
        version: 16.5.0
    devDependencies:
      '@typescript-eslint/eslint-plugin':
        specifier: ^8.30.1
        version: 8.30.1(@typescript-eslint/parser@8.30.1(eslint@8.57.1)(typescript@5.8.3))(eslint@8.57.1)(typescript@5.8.3)
      '@typescript-eslint/parser':
        specifier: ^8.30.1
        version: 8.30.1(eslint@8.57.1)(typescript@5.8.3)
      eslint:
        specifier: ^8.57.0
        version: 8.57.1
      lint-staged:
        specifier: ^15.5.1
        version: 15.5.1
      prettier:
        specifier: ^3.5.3
        version: 3.5.3
      ts-node:
        specifier: ^10.9.2
        version: 10.9.2(@types/node@22.14.1)(typescript@5.8.3)
      typescript:
        specifier: ^5.3.3
        version: 5.8.3

packages:

  '@cspotcode/source-map-support@0.8.1':
    resolution: {integrity: sha512-IchNf6dN4tHoMFIn/7OE8LWZ19Y6q/67Bmf6vnGREv8RSbBVb9LPJxEcnwrcwX6ixSvaiGoomAUvu4YSxXrVgw==}
    engines: {node: '>=12'}

  '@discordjs/builders@1.10.1':
    resolution: {integrity: sha512-OWo1fY4ztL1/M/DUyRPShB4d/EzVfuUvPTRRHRIt/YxBrUYSz0a+JicD5F5zHFoNs2oTuWavxCOVFV1UljHTng==}
    engines: {node: '>=16.11.0'}

  '@discordjs/collection@1.5.3':
    resolution: {integrity: sha512-SVb428OMd3WO1paV3rm6tSjM4wC+Kecaa1EUGX7vc6/fddvw/6lg90z4QtCqm21zvVe92vMMDt9+DkIvjXImQQ==}
    engines: {node: '>=16.11.0'}

  '@discordjs/collection@2.1.1':
    resolution: {integrity: sha512-LiSusze9Tc7qF03sLCujF5iZp7K+vRNEDBZ86FT9aQAv3vxMLihUvKvpsCWiQ2DJq1tVckopKm1rxomgNUc9hg==}
    engines: {node: '>=18'}

  '@discordjs/formatters@0.6.0':
    resolution: {integrity: sha512-YIruKw4UILt/ivO4uISmrGq2GdMY6EkoTtD0oS0GvkJFRZbTSdPhzYiUILbJ/QslsvC9H9nTgGgnarnIl4jMfw==}
    engines: {node: '>=16.11.0'}

  '@discordjs/rest@2.4.3':
    resolution: {integrity: sha512-+SO4RKvWsM+y8uFHgYQrcTl/3+cY02uQOH7/7bKbVZsTfrfpoE62o5p+mmV+s7FVhTX82/kQUGGbu4YlV60RtA==}
    engines: {node: '>=18'}

  '@discordjs/util@1.1.1':
    resolution: {integrity: sha512-eddz6UnOBEB1oITPinyrB2Pttej49M9FZQY8NxgEvc3tq6ZICZ19m70RsmzRdDHk80O9NoYN/25AqJl8vPVf/g==}
    engines: {node: '>=18'}

  '@discordjs/ws@1.2.1':
    resolution: {integrity: sha512-PBvenhZG56a6tMWF/f4P6f4GxZKJTBG95n7aiGSPTnodmz4N5g60t79rSIAq7ywMbv8A4jFtexMruH+oe51aQQ==}
    engines: {node: '>=16.11.0'}

  '@eslint-community/eslint-utils@4.6.0':
    resolution: {integrity: sha512-WhCn7Z7TauhBtmzhvKpoQs0Wwb/kBcy4CwpuI0/eEIr2Lx2auxmulAzLr91wVZJaz47iUZdkXOK7WlAfxGKCnA==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}
    peerDependencies:
      eslint: ^6.0.0 || ^7.0.0 || >=8.0.0

  '@eslint-community/regexpp@4.12.1':
    resolution: {integrity: sha512-CCZCDJuduB9OUkFkY2IgppNZMi2lBQgD2qzwXkEia16cge2pijY/aXi96CJMquDMn3nJdlPV1A5KrJEXwfLNzQ==}
    engines: {node: ^12.0.0 || ^14.0.0 || >=16.0.0}

  '@eslint/eslintrc@2.1.4':
    resolution: {integrity: sha512-269Z39MS6wVJtsoUl10L60WdkhJVdPG24Q4eZTH3nnF6lpvSShEK3wQjDX9JRWAUPvPh7COouPpU9IrqaZFvtQ==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}

  '@eslint/js@8.57.1':
    resolution: {integrity: sha512-d9zaMRSTIKDLhctzH12MtXvJKSSUhaHcjV+2Z+GK+EEY7XKpP5yR4x+N3TAcHTcu963nIr+TMcCb4DBCYX1z6Q==}
    engines: {node: ^12.22.0 || ^14.17.0 || >=16.0.0}

  '@humanwhocodes/config-array@0.13.0':
    resolution: {integrity: sha512-DZLEEqFWQFiyK6h5YIeynKx7JlvCYWL0cImfSRXZ9l4Sg2efkFGTuFf6vzXjK1cq6IYkU+Eg/JizXw+TD2vRNw==}
    engines: {node: '>=10.10.0'}
    deprecated: Use @eslint/config-array instead

  '@humanwhocodes/module-importer@1.0.1':
    resolution: {integrity: sha512-bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==}
    engines: {node: '>=12.22'}

  '@humanwhocodes/object-schema@2.0.3':
    resolution: {integrity: sha512-93zYdMES/c1D69yZiKDBj0V24vqNzB/koF26KPaagAfd3P/4gUlh3Dys5ogAK+Exi9QyzlD8x/08Zt7wIKcDcA==}
    deprecated: Use @eslint/object-schema instead

  '@jridgewell/resolve-uri@3.1.2':
    resolution: {integrity: sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==}
    engines: {node: '>=6.0.0'}

  '@jridgewell/sourcemap-codec@1.5.0':
    resolution: {integrity: sha512-gv3ZRaISU3fjPAgNsriBRqGWQL6quFx04YMPW/zD8XMLsU32mhCCbfbO6KZFLjvYpCZ8zyDEgqsgf+PwPaM7GQ==}

  '@jridgewell/trace-mapping@0.3.9':
    resolution: {integrity: sha512-3Belt6tdc8bPgAtbcmdtNJlirVoTmEb5e2gC94PnkwEW9jI6CAHUeoG85tjWP5WquqfavoMtMwiG4P926ZKKuQ==}

  '@mendable/firecrawl-js@1.23.9':
    resolution: {integrity: sha512-Hk/6uqA+R0QWCIzRHbhJHuOdypwVvwsRVeuG7c1EL3GXvNEAnh0WJdw4/EoBUl2H/7t6mhjC4+9atEWgd9LUyA==}
    engines: {node: '>=22.0.0'}

  '@nodelib/fs.scandir@2.1.5':
    resolution: {integrity: sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==}
    engines: {node: '>= 8'}

  '@nodelib/fs.stat@2.0.5':
    resolution: {integrity: sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==}
    engines: {node: '>= 8'}

  '@nodelib/fs.walk@1.2.8':
    resolution: {integrity: sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==}
    engines: {node: '>= 8'}

  '@sapphire/async-queue@1.5.5':
    resolution: {integrity: sha512-cvGzxbba6sav2zZkH8GPf2oGk9yYoD5qrNWdu9fRehifgnFZJMV+nuy2nON2roRO4yQQ+v7MK/Pktl/HgfsUXg==}
    engines: {node: '>=v14.0.0', npm: '>=7.0.0'}

  '@sapphire/shapeshift@4.0.0':
    resolution: {integrity: sha512-d9dUmWVA7MMiKobL3VpLF8P2aeanRTu6ypG2OIaEv/ZHH/SUQ2iHOVyi5wAPjQ+HmnMuL0whK9ez8I/raWbtIg==}
    engines: {node: '>=v16'}

  '@sapphire/snowflake@3.5.3':
    resolution: {integrity: sha512-jjmJywLAFoWeBi1W7994zZyiNWPIiqRRNAmSERxyg93xRGzNYvGjlZ0gR6x0F4gPRi2+0O6S71kOZYyr3cxaIQ==}
    engines: {node: '>=v14.0.0', npm: '>=7.0.0'}

  '@tsconfig/node10@1.0.11':
    resolution: {integrity: sha512-DcRjDCujK/kCk/cUe8Xz8ZSpm8mS3mNNpta+jGCA6USEDfktlNvm1+IuZ9eTcDbNk41BHwpHHeW+N1lKCz4zOw==}

  '@tsconfig/node12@1.0.11':
    resolution: {integrity: sha512-cqefuRsh12pWyGsIoBKJA9luFu3mRxCA+ORZvA4ktLSzIuCUtWVxGIuXigEwO5/ywWFMZ2QEGKWvkZG1zDMTag==}

  '@tsconfig/node14@1.0.3':
    resolution: {integrity: sha512-ysT8mhdixWK6Hw3i1V2AeRqZ5WfXg1G43mqoYlM2nc6388Fq5jcXyr5mRsqViLx/GJYdoL0bfXD8nmF+Zn/Iow==}

  '@tsconfig/node16@1.0.4':
    resolution: {integrity: sha512-vxhUy4J8lyeyinH7Azl1pdd43GJhZH/tP2weN8TntQblOY+A0XbT8DJk1/oCPuOOyg/Ja757rG0CgHcWC8OfMA==}

  '@types/node@22.14.1':
    resolution: {integrity: sha512-u0HuPQwe/dHrItgHHpmw3N2fYCR6x4ivMNbPHRkBVP4CvN+kiRrKHWk3i8tXiO/joPwXLMYvF9TTF0eqgHIuOw==}

  '@types/ws@8.18.1':
    resolution: {integrity: sha512-ThVF6DCVhA8kUGy+aazFQ4kXQ7E1Ty7A3ypFOe0IcJV8O/M511G99AW24irKrW56Wt44yG9+ij8FaqoBGkuBXg==}

  '@typescript-eslint/eslint-plugin@8.30.1':
    resolution: {integrity: sha512-v+VWphxMjn+1t48/jO4t950D6KR8JaJuNXzi33Ve6P8sEmPr5k6CEXjdGwT6+LodVnEa91EQCtwjWNUCPweo+Q==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      '@typescript-eslint/parser': ^8.0.0 || ^8.0.0-alpha.0
      eslint: ^8.57.0 || ^9.0.0
      typescript: '>=4.8.4 <5.9.0'

  '@typescript-eslint/parser@8.30.1':
    resolution: {integrity: sha512-H+vqmWwT5xoNrXqWs/fesmssOW70gxFlgcMlYcBaWNPIEWDgLa4W9nkSPmhuOgLnXq9QYgkZ31fhDyLhleCsAg==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      eslint: ^8.57.0 || ^9.0.0
      typescript: '>=4.8.4 <5.9.0'

  '@typescript-eslint/scope-manager@8.30.1':
    resolution: {integrity: sha512-+C0B6ChFXZkuaNDl73FJxRYT0G7ufVPOSQkqkpM/U198wUwUFOtgo1k/QzFh1KjpBitaK7R1tgjVz6o9HmsRPg==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@typescript-eslint/type-utils@8.30.1':
    resolution: {integrity: sha512-64uBF76bfQiJyHgZISC7vcNz3adqQKIccVoKubyQcOnNcdJBvYOILV1v22Qhsw3tw3VQu5ll8ND6hycgAR5fEA==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      eslint: ^8.57.0 || ^9.0.0
      typescript: '>=4.8.4 <5.9.0'

  '@typescript-eslint/types@8.30.1':
    resolution: {integrity: sha512-81KawPfkuulyWo5QdyG/LOKbspyyiW+p4vpn4bYO7DM/hZImlVnFwrpCTnmNMOt8CvLRr5ojI9nU1Ekpw4RcEw==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@typescript-eslint/typescript-estree@8.30.1':
    resolution: {integrity: sha512-kQQnxymiUy9tTb1F2uep9W6aBiYODgq5EMSk6Nxh4Z+BDUoYUSa029ISs5zTzKBFnexQEh71KqwjKnRz58lusQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      typescript: '>=4.8.4 <5.9.0'

  '@typescript-eslint/utils@8.30.1':
    resolution: {integrity: sha512-T/8q4R9En2tcEsWPQgB5BQ0XJVOtfARcUvOa8yJP3fh9M/mXraLxZrkCfGb6ChrO/V3W+Xbd04RacUEqk1CFEQ==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}
    peerDependencies:
      eslint: ^8.57.0 || ^9.0.0
      typescript: '>=4.8.4 <5.9.0'

  '@typescript-eslint/visitor-keys@8.30.1':
    resolution: {integrity: sha512-aEhgas7aJ6vZnNFC7K4/vMGDGyOiqWcYZPpIWrTKuTAlsvDNKy2GFDqh9smL+iq069ZvR0YzEeq0B8NJlLzjFA==}
    engines: {node: ^18.18.0 || ^20.9.0 || >=21.1.0}

  '@ungap/structured-clone@1.3.0':
    resolution: {integrity: sha512-WmoN8qaIAo7WTYWbAZuG8PYEhn5fkz7dZrqTBZ7dtt//lL2Gwms1IcnQ5yHqjDfX8Ft5j4YzDM23f87zBfDe9g==}

  '@vladfrangu/async_event_emitter@2.4.6':
    resolution: {integrity: sha512-RaI5qZo6D2CVS6sTHFKg1v5Ohq/+Bo2LZ5gzUEwZ/WkHhwtGTCB/sVLw8ijOkAUxasZ+WshN/Rzj4ywsABJ5ZA==}
    engines: {node: '>=v14.0.0', npm: '>=7.0.0'}

  acorn-jsx@5.3.2:
    resolution: {integrity: sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==}
    peerDependencies:
      acorn: ^6.0.0 || ^7.0.0 || ^8.0.0

  acorn-walk@8.3.4:
    resolution: {integrity: sha512-ueEepnujpqee2o5aIYnvHU6C0A42MNdsIDeqy5BydrkuC5R1ZuUFnm27EeFJGoEHJQgn3uleRvmTXaJgfXbt4g==}
    engines: {node: '>=0.4.0'}

  acorn@8.14.1:
    resolution: {integrity: sha512-OvQ/2pUDKmgfCg++xsTX1wGxfTaszcHVcTctW4UJB4hibJx2HXxxO5UmVgyjMa+ZDsiaf5wWLXYpRWMmBI0QHg==}
    engines: {node: '>=0.4.0'}
    hasBin: true

  ajv@6.12.6:
    resolution: {integrity: sha512-j3fVLgvTo527anyYyJOGTYJbG+vnnQYvE0m5mmkc1TK+nxAppkCLMIL0aZ4dblVCNoGShhm+kzE4ZUykBoMg4g==}

  ansi-escapes@7.0.0:
    resolution: {integrity: sha512-GdYO7a61mR0fOlAsvC9/rIHf7L96sBc6dEWzeOu+KAea5bZyQRPIpojrVoI4AXGJS/ycu/fBTdLrUkA4ODrvjw==}
    engines: {node: '>=18'}

  ansi-regex@5.0.1:
    resolution: {integrity: sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==}
    engines: {node: '>=8'}

  ansi-regex@6.1.0:
    resolution: {integrity: sha512-7HSX4QQb4CspciLpVFwyRe79O3xsIZDDLER21kERQ71oaPodF8jL725AgJMFAYbooIqolJoRLuM81SpeUkpkvA==}
    engines: {node: '>=12'}

  ansi-styles@4.3.0:
    resolution: {integrity: sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==}
    engines: {node: '>=8'}

  ansi-styles@6.2.1:
    resolution: {integrity: sha512-bN798gFfQX+viw3R7yrGWRqnrN2oRkEkUjjl4JNn4E8GxxbjtG3FbrEIIY3l8/hrwUwIeCZvi4QuOTP4MErVug==}
    engines: {node: '>=12'}

  arg@4.1.3:
    resolution: {integrity: sha512-58S9QDqG0Xx27YwPSt9fJxivjYl432YCwfDMfZ+71RAqUrZef7LrKQZ3LHLOwCS4FLNBplP533Zx895SeOCHvA==}

  argparse@2.0.1:
    resolution: {integrity: sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==}

  asynckit@0.4.0:
    resolution: {integrity: sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==}

  axios@1.8.4:
    resolution: {integrity: sha512-eBSYY4Y68NNlHbHBMdeDmKNtDgXWhQsJcGqzO3iLUM0GraQFSS9cVgPX5I9b3lbdFKyYoAEGAZF1DwhTaljNAw==}

  balanced-match@1.0.2:
    resolution: {integrity: sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==}

  brace-expansion@1.1.11:
    resolution: {integrity: sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==}

  brace-expansion@2.0.1:
    resolution: {integrity: sha512-XnAIvQ8eM+kC6aULx6wuQiwVsnzsi9d3WxzV3FpWTGA19F621kwdbsAcFKXgKUHZWsy+mY6iL1sHTxWEFCytDA==}

  braces@3.0.3:
    resolution: {integrity: sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==}
    engines: {node: '>=8'}

  call-bind-apply-helpers@1.0.2:
    resolution: {integrity: sha512-Sp1ablJ0ivDkSzjcaJdxEunN5/XvksFJ2sMBFfq6x0ryhQV/2b/KwFe21cMpmHtPOSij8K99/wSfoEuTObmuMQ==}
    engines: {node: '>= 0.4'}

  callsites@3.1.0:
    resolution: {integrity: sha512-P8BjAsXvZS+VIDUI11hHCQEv74YT67YUi5JJFNWIqL235sBmjX4+qx9Muvls5ivyNENctx46xQLQ3aTuE7ssaQ==}
    engines: {node: '>=6'}

  chalk@4.1.2:
    resolution: {integrity: sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==}
    engines: {node: '>=10'}

  chalk@5.4.1:
    resolution: {integrity: sha512-zgVZuo2WcZgfUEmsn6eO3kINexW8RAE4maiQ8QNs8CtpPCSyMiYsULR3HQYkm3w8FIA3SberyMJMSldGsW+U3w==}
    engines: {node: ^12.17.0 || ^14.13 || >=16.0.0}

  cli-cursor@5.0.0:
    resolution: {integrity: sha512-aCj4O5wKyszjMmDT4tZj93kxyydN/K5zPWSCe6/0AV/AA1pqe5ZBIw0a2ZfPQV7lL5/yb5HsUreJ6UFAF1tEQw==}
    engines: {node: '>=18'}

  cli-truncate@4.0.0:
    resolution: {integrity: sha512-nPdaFdQ0h/GEigbPClz11D0v/ZJEwxmeVZGeMo3Z5StPtUTkA9o1lD6QwoirYiSDzbcwn2XcjwmCp68W1IS4TA==}
    engines: {node: '>=18'}

  color-convert@2.0.1:
    resolution: {integrity: sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==}
    engines: {node: '>=7.0.0'}

  color-name@1.1.4:
    resolution: {integrity: sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==}

  colorette@2.0.20:
    resolution: {integrity: sha512-IfEDxwoWIjkeXL1eXcDiow4UbKjhLdq6/EuSVR9GMN7KVH3r9gQ83e73hsz1Nd1T3ijd5xv1wcWRYO+D6kCI2w==}

  combined-stream@1.0.8:
    resolution: {integrity: sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==}
    engines: {node: '>= 0.8'}

  commander@13.1.0:
    resolution: {integrity: sha512-/rFeCpNJQbhSZjGVwO9RFV3xPqbnERS8MmIQzCtD/zl6gpJuV/bMLuN92oG3F7d8oDEHHRrujSXNUr8fpjntKw==}
    engines: {node: '>=18'}

  concat-map@0.0.1:
    resolution: {integrity: sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==}

  create-require@1.1.1:
    resolution: {integrity: sha512-dcKFX3jn0MpIaXjisoRvexIJVEKzaq7z2rZKxf+MSr9TkdmHmsU4m2lcLojrj/FHl8mk5VxMmYA+ftRkP/3oKQ==}

  cross-spawn@7.0.6:
    resolution: {integrity: sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==}
    engines: {node: '>= 8'}

  debug@4.4.0:
    resolution: {integrity: sha512-6WTZ/IxCY/T6BALoZHaE4ctp9xm+Z5kY/pzYaCHRFeyVhojxlrm+46y68HA6hr0TcwEssoxNiDEUJQjfPZ/RYA==}
    engines: {node: '>=6.0'}
    peerDependencies:
      supports-color: '*'
    peerDependenciesMeta:
      supports-color:
        optional: true

  deep-is@0.1.4:
  
... [TRUNCATED]
```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "esModuleInterop": true,
    "outDir": "dist",
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true
  },
  "include": ["src"]
}
```

### File: src\index.ts
```ts
import {
  Client,
  Events,
  GatewayIntentBits,
  REST,
  Routes,
  SlashCommandBuilder,
  MessageFlags,
  AttachmentBuilder,
  Interaction,
} from 'discord.js';
import dotenv from 'dotenv';
import FirecrawlApp, {
  type ScrapeParams,
  type MapParams,
  type ExtractParams,
  type Action,
} from '@mendable/firecrawl-js';
import { writeFile } from 'fs/promises';
import { join } from 'path';
import { tmpdir } from 'os';

dotenv.config();

// Store API keys per user
const userApiKeys = new Map<string, string>();

// Initialize Discord client
const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

// Define commands
const commands = [
  new SlashCommandBuilder()
    .setName('set-api-key')
    .setDescription('Set your Firecrawl API key')
    .addStringOption((option) =>
      option.setName('key').setDescription('Your Firecrawl API key').setRequired(true)
    ),
  new SlashCommandBuilder()
    .setName('update-api-key')
    .setDescription('Update your existing Firecrawl API key')
    .addStringOption((option) =>
      option.setName('key').setDescription('Your new Firecrawl API key').setRequired(true)
    ),
  new SlashCommandBuilder()
    .setName('scrape')
    .setDescription('Scrape a webpage')
    .addStringOption((option) =>
      option.setName('params').setDescription('JSON parameters for scraping').setRequired(true)
    ),
  new SlashCommandBuilder()
    .setName('map')
    .setDescription('Map URLs from a starting point')
    .addStringOption((option) =>
      option.setName('params').setDescription('JSON parameters for mapping').setRequired(true)
    ),
  new SlashCommandBuilder()
    .setName('extract')
    .setDescription('Extract structured data from webpages')
    .addStringOption((option) =>
      option.setName('params').setDescription('JSON parameters for extraction').setRequired(true)
    ),
  new SlashCommandBuilder().setName('docs').setDescription('Get the documentation URL'),
  new SlashCommandBuilder().setName('help').setDescription('Get help with using the bot'),
];

// Register commands
const rest = new REST().setToken(process.env.DISCORD_TOKEN!);

async function registerCommands() {
  try {
    await rest.put(Routes.applicationCommands(process.env.CLIENT_ID!), { body: commands });
    console.log('✅ Successfully registered application commands.');
  } catch (error) {
    console.error('Error registering commands:', error);
  }
}

// Helper function to validate JSON parameters
function validateAndParseJSON(jsonString: string): {
  valid: boolean;
  data?: unknown;
  error?: string;
} {
  try {
    const data = JSON.parse(jsonString);
    return { valid: true, data };
  } catch {
    return { valid: false, error: 'Invalid JSON format. Please check your input.' };
  }
}

// Helper function to check if user has API key
function checkApiKey(userId: string): boolean {
  return userApiKeys.has(userId);
}

// Helper function to handle large responses
async function handleLargeResponse(data: unknown, filename: string): Promise<AttachmentBuilder> {
  const tempDir = tmpdir();
  const tempFilePath = join(tempDir, filename);
  const jsonContent = JSON.stringify(data, null, 2);
  await writeFile(tempFilePath, jsonContent, 'utf-8');
  return new AttachmentBuilder(tempFilePath, { name: filename });
}

// Helper function to send response
async function sendResponse(interaction: Interaction, data: unknown, commandName: string) {
  const jsonString = JSON.stringify(data, null, 2);

  if (jsonString.length < 1900) {
    // @ts-expect-error editReply exists on ChatInputCommandInteraction
    await interaction.editReply(`\`\`\`json\n${jsonString}\n\`\`\``);
  } else {
    const attachment = await handleLargeResponse(data, `${commandName}-response.json`);
    // @ts-expect-error editReply exists on ChatInputCommandInteraction
    await interaction.editReply({
      content: '📎 The response was too large to display directly. Please find it attached below:',
      files: [attachment],
    });
  }
}

// Helper function to check for unsupported parameters
function checkUnsupportedParams(
  command: string,
  params: Record<string, unknown>
): { isValid: boolean; unsupportedParams: string[] } {
  const supportedParams = {
    scrape: [
      'url',
      'formats',
      'onlyMainContent',
      'includeTags',
      'excludeTags',
      'headers',
      'waitFor',
      'mobile',
      'skipTlsVerification',
      'timeout',
      'extract',
      'actions',
      'location',
      'removeBase64Images',
      'jsonOptions',
      'agent',
    ],
    map: ['url', 'search', 'ignoreSitemap', 'sitemapOnly', 'includeSubdomains', 'limit'],
    extract: ['urls', 'prompt', 'schema', 'agent'],
  };

  const unsupportedParams = Object.keys(params).filter(
    (param) => !supportedParams[command as keyof typeof supportedParams]?.includes(param)
  );

  return {
    isValid: unsupportedParams.length === 0,
    unsupportedParams,
  };
}

// Command handlers
client.on(Events.InteractionCreate, async (interaction) => {
  if (!interaction.isChatInputCommand()) return;

  const { commandName, user } = interaction;

  // Create Firecrawl instance with user's API key
  const getFirecrawlInstance = (userId: string) => {
    const apiKey = userApiKeys.get(userId);
    return apiKey ? new FirecrawlApp({ apiKey }) : null;
  };

  try {
    switch (commandName) {
      case 'set-api-key': {
        const key = interaction.options.getString('key', true);
        if (checkApiKey(user.id)) {
          await interaction.reply({
            content: 'You already have an API key set. Use /update-api-key to change it.',
            flags: MessageFlags.Ephemeral,
          });
          return;
        }
        userApiKeys.set(user.id, key);
        await interaction.reply({
          content: '✅ API key set successfully!',
          flags: MessageFlags.Ephemeral,
        });
        break;
      }

      case 'update-api-key': {
        const key = interaction.options.getString('key', true);
        if (!checkApiKey(user.id)) {
          await interaction.reply({
            content:
              'You must add your API key before using these commands. To do that, use /set-api-key key value.',
            flags: MessageFlags.Ephemeral,
          });
          return;
        }
        userApiKeys.set(user.id, key);
        await interaction.reply({
          content: '✅ API key updated successfully!',
          flags: MessageFlags.Ephemeral,
        });
        break;
      }

      case 'scrape': {
        if (!checkApiKey(user.id)) {
          await interaction.reply({
            content:
              'You must add your API key before using these commands. To do that, use /set-api-key key value.',
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        const paramsStr = interaction.options.getString('params', true);
        const { valid, data, error } = validateAndParseJSON(paramsStr);

        if (!valid) {
          await interaction.reply({
            content: error,
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        const typedData = data as Record<string, unknown>;
        const { isValid, unsupportedParams } = checkUnsupportedParams('scrape', typedData);
        if (!isValid) {
          await interaction.reply({
            content: `⚠️ The following parameters are not supported in the bot yet: \`${unsupportedParams.join('`, `')}\``,
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        if (!typedData.url) {
          await interaction.reply({
            content: 'The "url" parameter is required for the scrape command.',
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        const app = getFirecrawlInstance(user.id)!;
        await interaction.deferReply();

        try {
          const scrapeParams = {
            formats: (typedData.formats as Array<
              | 'markdown'
              | 'html'
              | 'rawHtml'
              | 'links'
              | 'screenshot'
              | 'screenshot@fullPage'
              | 'json'
              | 'changeTracking'
            >) || ['markdown'],
            onlyMainContent: (typedData.onlyMainContent as boolean) ?? true,
            includeTags: typedData.includeTags as string[] | undefined,
            excludeTags: typedData.excludeTags as string[] | undefined,
            headers: typedData.headers as Record<string, string> | undefined,
            waitFor: typedData.waitFor as number | undefined,
            mobile: (typedData.mobile as boolean) ?? false,
            skipTlsVerification: (typedData.skipTlsVerification as boolean) ?? false,
            timeout: (typedData.timeout as number) ?? 30000,
            extract: typedData.extract as
              | { prompt?: string; schema?: unknown; systemPrompt?: string }
              | undefined,
            actions: typedData.actions as Action[] | undefined,
            location: typedData.location as { country?: string; languages?: string[] } | undefined,
            agent: typedData.agent,
            jsonOptions: typedData.jsonOptions as Record<string, unknown> | undefined,
          } as ScrapeParams;

          const response = await app.scrapeUrl(typedData.url as string, scrapeParams);
          await sendResponse(interaction, response, 'scrape');
        } catch (error) {
          console.error('Scrape command error:', error);
          await interaction.editReply(
            '⚠️ Error executing scrape command. Please check your parameters and try again.'
          );
        }
        break;
      }

      case 'map': {
        if (!checkApiKey(user.id)) {
          await interaction.reply({
            content:
              'You must add your API key before using these commands. To do that, use /set-api-key key value.',
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        const paramsStr = interaction.options.getString('params', true);
        const { valid, data, error } = validateAndParseJSON(paramsStr);

        if (!valid) {
          await interaction.reply({
            content: error,
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        const typedData = data as Record<string, unknown>;
        const { isValid, unsupportedParams } = checkUnsupportedParams('map', typedData);
        if (!isValid) {
          await interaction.reply({
            content: `⚠️ The following parameters are not supported in the bot yet: \`${unsupportedParams.join('`, `')}\``,
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        if (!typedData.url) {
          await interaction.reply({
            content: 'The "url" parameter is required for the map command.',
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        const app = getFirecrawlInstance(user.id)!;
        await interaction.deferReply();

        try {
          const mapParams: MapParams = {
            search: typedData.search as string | undefined,
            ignoreSitemap: (typedData.ignoreSitemap as boolean) ?? true,
            sitemapOnly: (typedData.sitemapOnly as boolean) ?? false,
            includeSubdomains: (typedData.includeSubdomains as boolean) ?? false,
            limit: (typedData.limit as number) ?? 5000,
          };

          const response = await app.mapUrl(typedData.url as string, mapParams);
          await sendResponse(interaction, response, 'map');
        } catch (error) {
          console.error('Map command error:', error);
          await interaction.editReply(
            '⚠️ Error executing map command. Please check your parameters and try again.'
          );
        }
        break;
      }

      case 'extract': {
        if (!checkApiKey(user.id)) {
          await interaction.reply({
            content:
              'You must add your API key before using these commands. To do that, use /set-api-key key value.',
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        const paramsStr = interaction.options.getString('params', true);
        const { valid, data, error } = validateAndParseJSON(paramsStr);

        if (!valid) {
          await interaction.reply({
            content: error,
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        const typedData = data as Record<string, unknown>;
        const { isValid, unsupportedParams } = checkUnsupportedParams('extract', typedData);
        if (!isValid) {
          await interaction.reply({
            content: `⚠️ The following parameters are not supported in the bot yet: \`${unsupportedParams.join('`, `')}\``,
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        if (!typedData.urls || !Array.isArray(typedData.urls) || typedData.urls.length === 0) {
          await interaction.reply({
            content: 'The "urls" parameter is required and must be a non-empty array.',
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        if (!typedData.prompt) {
          await interaction.reply({
            content: 'The "prompt" parameter is required for the extract command.',
            flags: MessageFlags.Ephemeral,
          });
          return;
        }

        const app = getFirecrawlInstance(user.id)!;
        await interaction.deferReply();

        try {
          const extractParams: Omit<ExtractParams, 'agent'> & { agent?: Record<string, unknown> } =
            {
              prompt: typedData.prompt as string,
              schema: typedData.schema as Record<string, unknown> | undefined,
              agent: typedData.agent as Record<string, unknown> | undefined,
            };

          const response = await app.extract(typedData.urls as string[], extractParams);
          await sendResponse(interaction, response, 'extract');
        } catch (error) {
          console.error('Extract command error:', error);
          await interaction.editReply(
            '⚠️ Error executing extract command. Please check your parameters and try again.'
          );
        }
        break;
      }

      case 'docs': {
        await interaction.reply('📚 Documentation: https://docs.firecrawl.dev');
        break;
      }

      case 'help': {
        const helpMessage = `
🤖 **Firecrawl Discord Bot Help**

Before using any commands, set your API key using \`/set-api-key\`.

Available commands:
• \`/set-api-key <key>\` - Set your Firecrawl API key
• \`/update-api-key <key>\` - Update your existing API key
• \`/scrape\` - Scrape a webpage. Example:
  \`\`\`json
  {
    "url": "https://example.com",
    "formats": ["markdown", "html"],
    "onlyMainContent": true,
    "waitFor": 1000,
    "includeTags": ["articl
... [TRUNCATED]
```


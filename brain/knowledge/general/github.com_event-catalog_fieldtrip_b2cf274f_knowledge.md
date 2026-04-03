---
id: github.com-event-catalog-fieldtrip-b2cf274f-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:46.528514
---

# KNOWLEDGE EXTRACT: github.com_event-catalog_fieldtrip_b2cf274f
> **Extracted on:** 2026-04-01 12:51:23
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007522066/github.com_event-catalog_fieldtrip_b2cf274f

---

## File: `.gitignore`
```
node_modules/
dist/
test-schemas/
*.tsbuildinfo
.DS_Store
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 FieldTrip Contributors

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

## File: `README.md`
```markdown
<div align="center">

# FieldTrip

**Instantly search, explore, and visualize every field across your schemas.**

Point it at a directory. It finds your OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files, indexes every property, and launches a local UI to explore them.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![npm version](https://img.shields.io/npm/v/@eventcatalog/fieldtrip.svg)](https://www.npmjs.com/package/@eventcatalog/fieldtrip)

</div>

---

![FieldTrip Table View](images/table.png)

## Why FieldTrip?

Schema sprawl is real. When your system has dozens of services each with their own schema definitions, it becomes impossible to answer simple questions:

- *"Which schemas use a `customerId` field?"*
- *"Is `email` required everywhere it appears?"*
- *"What fields does `Order` share with `Payment`?"*

FieldTrip answers these in seconds. One command, zero config.

## Quick Start

```bash
npx @eventcatalog/fieldtrip --dir ./schemas
```

That's it. FieldTrip scans the directory, indexes every property, and opens a local UI at `http://localhost:3200`.

## Features

### Table View — Search & Filter

Full-text search across all property names, types, and descriptions. Filter by schema type, sort by name/schema/type, and click any property to view it in context with syntax highlighting.

- Prefix and fuzzy matching
- Exact match with `"quoted strings"`
- Filter by schema type (OpenAPI, AsyncAPI, Proto, Avro, JSON)
- Filter by specific schema files via the sidebar
- Click any row to view the full schema with the property highlighted

![FieldTrip Table View](images/table.png)

### Matrix View — Property x Schema

See which properties appear in which schemas at a glance. A heatmap-style grid where rows are properties and columns are schemas.

- Green cells = required, Blue cells = optional
- Hover to see type, schema, and required status
- Sort by frequency, alphabetical, or required count
- Instantly spot shared fields across your architecture

![FieldTrip Matrix View](images/matrix.png)

### Graph View — Force-Directed Relationships

Visualize how schemas are connected through shared properties. Schema nodes cluster with their properties, and shared fields create visible bridges between schemas.

- D3.js force-directed simulation
- Click a property to highlight all schemas sharing that field
- Click a schema to highlight all its properties
- "Shared only" toggle to reduce noise
- Drag, zoom, and pan

![FieldTrip Graph View](images/graph.png)

## Supported Schemas

| Format | Extensions | What's indexed |
|--------|-----------|---------------|
| **OpenAPI** | `.yaml` `.yml` `.json` | Components, definitions, inline request/response bodies |
| **AsyncAPI** | `.yaml` `.yml` `.json` | Components, messages, channel payloads (v2 & v3) |
| **Protobuf** | `.proto` | Messages, enums, nested types |
| **Avro** | `.avsc` | Records, nested records, unions, arrays, maps |
| **JSON Schema** | `.json` | Properties, nested objects, allOf/oneOf/anyOf |

## CLI Options

```
Usage: fieldtrip [options]

Options:
  --dir <path>     Directory to scan for schema files (required)
  --port <number>  Port for the web UI (default: 3200)
  --no-open        Do not auto-open browser
  -h, --help       Display help
```

## Development

```bash
# Install dependencies
npm install

# Run in dev mode
npm run dev

# Build for production
npm run build
```

## How It Works

1. **Scan** — Recursively finds schema files by extension and content detection
2. **Parse** — Extracts every property with its name, type, description, path, and required status
3. **Index** — Builds a MiniSearch full-text index with prefix search and fuzzy matching
4. **Serve** — Launches an Express server with a Vite-built frontend

## License

[MIT](LICENSE)
```

## File: `package.json`
```json
{
  "name": "@eventcatalog/fieldtrip",
  "version": "0.0.1",
  "description": "Search across OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files",
  "bin": {
    "fieldtrip": "./bin/cli.js"
  },
  "files": [
    "bin",
    "dist"
  ],
  "scripts": {
    "build": "npm run build:ui && npm run build:cli",
    "build:ui": "vite build",
    "build:cli": "tsc -p tsconfig.cli.json",
    "dev": "tsx src/cli/index.ts --dir ./test-schemas",
    "changeset": "changeset",
    "version-packages": "changeset version",
    "release": "npm run build && changeset publish"
  },
  "keywords": [
    "schema",
    "search",
    "openapi",
    "asyncapi",
    "protobuf",
    "avro"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "@types/d3": "^7.4.3",
    "commander": "^12.0.0",
    "d3": "^7.9.0",
    "express": "^4.18.0",
    "glob": "^10.3.0",
    "minisearch": "^7.0.0",
    "monaco-editor": "^0.55.1",
    "open": "^10.0.0",
    "protobufjs": "^7.2.0",
    "yaml": "^2.4.0"
  },
  "devDependencies": {
    "@changesets/changelog-github": "^0.6.0",
    "@changesets/cli": "^2.30.0",
    "@types/express": "^4.17.21",
    "@types/node": "^20.11.0",
    "tsx": "^4.7.0",
    "typescript": "^5.4.0",
    "vite": "^5.2.0"
  }
}
```

## File: `tsconfig.cli.json`
```json
{
  "extends": "./tsconfig.json"
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "lib": ["ES2022"],
    "outDir": "./dist/cli",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": false,
    "sourceMap": false
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules", "ui", "dist"]
}
```

## File: `vite.config.ts`
```typescript
import { defineConfig } from 'vite';

export default defineConfig({
  root: 'ui',
  build: {
    outDir: '../dist/ui',
    emptyOutDir: true,
  },
});
```

## File: `src/cli/index.ts`
```typescript
import { Command } from 'commander';
import { scanDirectory } from '../scanner';
import { parseFile } from '../parsers';
import { createIndex } from '../indexer';
import { createServer } from './server';
import { SchemaProperty } from '../parsers/types';

const program = new Command();

program
  .name('fieldtrip')
  .description('Search across OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files')
  .requiredOption('--dir <path>', 'Directory to scan for schema files')
  .option('--port <number>', 'Port for the web UI', '3200')
  .option('--no-open', 'Do not auto-open browser')
  .action(async (opts) => {
    const dir = opts.dir;
    const port = parseInt(opts.port, 10);
    const shouldOpen = opts.open !== false;

    console.log(`\nScanning ${dir} for schema files...\n`);

    // 1. Scan for files
    const files = await scanDirectory(dir);
    console.log(`Found ${files.length} potential schema files`);

    if (files.length === 0) {
      console.log('No schema files found. Check the --dir path and try again.');
      process.exit(1);
    }

    // 2. Parse all files
    const allProperties: SchemaProperty[] = [];
    let parsedCount = 0;

    for (const file of files) {
      try {
        const properties = await parseFile(file.absolutePath, file.relativePath);
        allProperties.push(...properties);
        if (properties.length > 0) parsedCount++;
      } catch (err: any) {
        console.warn(`Warning: Failed to process ${file.relativePath}: ${err.message}`);
      }
    }

    console.log(`Parsed ${parsedCount} schema files, extracted ${allProperties.length} properties\n`);

    if (allProperties.length === 0) {
      console.log('No schema properties were extracted. The files may not contain recognizable schemas.');
      process.exit(1);
    }

    // 3. Build search index
    const index = createIndex(allProperties);
    console.log('Search index built successfully');

    // 4. Start server
    await createServer(index, allProperties, port, dir);
    console.log(`\nFieldTrip is running at http://localhost:${port}\n`);

    // 5. Open browser
    if (shouldOpen) {
      try {
        const open = (await import('open')).default;
        await open(`http://localhost:${port}`);
      } catch {
        // Silently fail if browser can't be opened
      }
    }
  });

program.parse();
```

## File: `src/cli/server.ts`
```typescript
import express from 'express';
import * as path from 'path';
import * as fs from 'fs';
import MiniSearch from 'minisearch';
import { SchemaProperty, SchemaType } from '../parsers/types';

interface Stats {
  totalProperties: number;
  totalFiles: number;
  schemaTypes: Record<string, number>;
}

export function createServer(
  miniSearch: MiniSearch<SchemaProperty>,
  properties: SchemaProperty[],
  port: number,
  scanDir: string
): Promise<void> {
  const app = express();

  // Compute stats
  const fileSet = new Set(properties.map((p) => p.filePath));
  const schemaTypes: Record<string, number> = {};
  for (const p of properties) {
    schemaTypes[p.schemaType] = (schemaTypes[p.schemaType] || 0) + 1;
  }
  const stats: Stats = {
    totalProperties: properties.length,
    totalFiles: fileSet.size,
    schemaTypes,
  };

  // Serve built UI — find dist/ui which contains the Vite-built assets
  // Priority: dist/ui from project root (works for both tsx dev and compiled)
  const candidates = [
    path.resolve(__dirname, '..', '..', 'ui'),       // from dist/cli/cli/ → dist/ui
    path.resolve(__dirname, '..', '..', 'dist', 'ui'), // from src/cli/ → dist/ui (tsx dev)
    path.join(__dirname, '..', 'ui'),                  // fallback
  ];
  let uiPath = candidates[0];
  for (const candidate of candidates) {
    const indexPath = path.join(candidate, 'assets');
    if (fs.existsSync(indexPath)) {
      uiPath = candidate;
      break;
    }
  }
  app.use(express.static(uiPath));

  // Search API — supports "exact match" with quotes
  app.get('/api/search', (req, res) => {
    const rawQuery = (req.query.q as string || '').trim();
    const schemaType = req.query.schemaType as string | undefined;

    if (!rawQuery) {
      res.json({ results: [], total: 0 });
      return;
    }

    // Check for quoted exact-match phrases
    const exactMatch = /^"(.+)"$/.exec(rawQuery);

    const typeFilter = schemaType
      ? (result: any) => result.schemaType === schemaType
      : undefined;

    if (exactMatch) {
      // Exact match: search without fuzzy/prefix, then post-filter to only
      // keep results where a stored field exactly contains the quoted term
      const term = exactMatch[1];
      const searchOpts: any = {
        prefix: false,
        fuzzy: false,
        boost: { name: 3, description: 1 },
        ...(typeFilter ? { filter: typeFilter } : {}),
      };
      const candidates = miniSearch.search(term, searchOpts);
      const termLower = term.toLowerCase();
      const results = candidates.filter((r: any) =>
        r.name?.toLowerCase() === termLower ||
        r.type?.toLowerCase() === termLower ||
        r.description?.toLowerCase().includes(termLower)
      );
      res.json({ results, total: results.length });
    } else {
      const searchOpts: any = {
        prefix: true,
        fuzzy: 0.2,
        boost: { name: 3, description: 1 },
        ...(typeFilter ? { filter: typeFilter } : {}),
      };
      const results = miniSearch.search(rawQuery, searchOpts);
      res.json({ results, total: results.length });
    }
  });

  // All properties endpoint (for browsing)
  app.get('/api/properties', (req, res) => {
    const schemaType = req.query.schemaType as string | undefined;
    let filtered = properties;
    if (schemaType) {
      filtered = properties.filter((p) => p.schemaType === schemaType);
    }
    res.json({ properties: filtered, total: filtered.length });
  });

  // File content endpoint — returns raw schema file
  app.get('/api/file', (req, res) => {
    const filePath = req.query.path as string;
    if (!filePath) {
      res.status(400).json({ error: 'path is required' });
      return;
    }

    const absolutePath = path.resolve(scanDir, filePath);
    // Prevent directory traversal
    if (!absolutePath.startsWith(path.resolve(scanDir))) {
      res.status(403).json({ error: 'forbidden' });
      return;
    }

    try {
      const content = fs.readFileSync(absolutePath, 'utf-8');
      res.json({ content, filePath });
    } catch {
      res.status(404).json({ error: 'file not found' });
    }
  });

  // Schemas list endpoint — grouped by file
  const schemasMap = new Map<string, { filePath: string; schemaType: string; count: number }>();
  for (const p of properties) {
    const existing = schemasMap.get(p.filePath);
    if (existing) {
      existing.count++;
    } else {
      schemasMap.set(p.filePath, { filePath: p.filePath, schemaType: p.schemaType, count: 0 });
      schemasMap.get(p.filePath)!.count = 1;
    }
  }
  const schemasList = Array.from(schemasMap.values());

  app.get('/api/schemas', (_req, res) => {
    res.json({ schemas: schemasList });
  });

  // Stats API
  app.get('/api/stats', (_req, res) => {
    res.json(stats);
  });

  // SPA fallback
  app.get('*', (_req, res) => {
    res.sendFile(path.join(uiPath, 'index.html'));
  });

  return new Promise((resolve) => {
    app.listen(port, () => {
      resolve();
    });
  });
}
```

## File: `src/indexer/index.ts`
```typescript
import MiniSearch from 'minisearch';
import { SchemaProperty } from '../parsers/types';

export function createIndex(properties: SchemaProperty[]): MiniSearch<SchemaProperty> {
  const miniSearch = new MiniSearch<SchemaProperty>({
    fields: ['name', 'type', 'description'],
    storeFields: [
      'name', 'type', 'description', 'schemaPath', 'filePath',
      'schemaType', 'parentName', 'required', 'format', 'ref',
    ],
    idField: 'id',
    searchOptions: {
      boost: { name: 3, description: 1 },
      prefix: true,
      fuzzy: 0.2,
    },
  });

  miniSearch.addAll(properties);
  return miniSearch;
}
```

## File: `src/parsers/asyncapi.ts`
```typescript
import { SchemaProperty } from './types';
import { walkJsonSchemaObject } from './jsonschema';

export function parseAsyncAPI(content: any, filePath: string): SchemaProperty[] {
  const results: SchemaProperty[] = [];

  // components.schemas
  const schemas = content.components?.schemas;
  if (schemas) {
    for (const [schemaName, schemaDef] of Object.entries<any>(schemas)) {
      walkJsonSchemaObject(
        schemaDef,
        schemaName,
        `components.schemas.${schemaName}`,
        filePath,
        'asyncapi',
        results
      );
    }
  }

  // components.messages — extract payload schemas
  const messages = content.components?.messages;
  if (messages) {
    for (const [msgName, msgDef] of Object.entries<any>(messages)) {
      if (msgDef.payload) {
        walkJsonSchemaObject(
          msgDef.payload,
          msgName,
          `components.messages.${msgName}.payload`,
          filePath,
          'asyncapi',
          results
        );
      }
    }
  }

  // channels — inline message payloads
  const channels = content.channels;
  if (channels) {
    for (const [channelName, channelDef] of Object.entries<any>(channels)) {
      // AsyncAPI 2.x
      for (const op of ['publish', 'subscribe']) {
        const message = channelDef[op]?.message;
        if (message?.payload) {
          walkJsonSchemaObject(
            message.payload,
            `${channelName} ${op}`,
            `channels.${channelName}.${op}.message.payload`,
            filePath,
            'asyncapi',
            results
          );
        }
      }

      // AsyncAPI 3.x — channels have messages directly
      if (channelDef.messages) {
        for (const [msgName, msgDef] of Object.entries<any>(channelDef.messages)) {
          if (msgDef.payload) {
            walkJsonSchemaObject(
              msgDef.payload,
              `${channelName}.${msgName}`,
              `channels.${channelName}.messages.${msgName}.payload`,
              filePath,
              'asyncapi',
              results
            );
          }
        }
      }
    }
  }

  return results;
}
```

## File: `src/parsers/avro.ts`
```typescript
import { SchemaProperty } from './types';

function resolveAvroType(type: any): string {
  if (typeof type === 'string') return type;
  if (Array.isArray(type)) return type.map(resolveAvroType).join(' | ');
  if (typeof type === 'object') {
    if (type.type === 'array') return `${resolveAvroType(type.items)}[]`;
    if (type.type === 'map') return `map<${resolveAvroType(type.values)}>`;
    if (type.type === 'record') return type.name || 'record';
    if (type.type === 'enum') return type.name || 'enum';
    if (type.type === 'fixed') return type.name || 'fixed';
    return type.type || 'unknown';
  }
  return 'unknown';
}

function walkAvroRecord(
  schema: any,
  filePath: string,
  results: SchemaProperty[],
  pathPrefix: string = '',
  visited: Set<string> = new Set()
): void {
  if (!schema || schema.type !== 'record' || !schema.fields) return;

  const recordName = schema.name || 'unknown';
  const key = `${filePath}#${pathPrefix}.${recordName}`;
  if (visited.has(key)) return;
  visited.add(key);

  const currentPath = pathPrefix ? `${pathPrefix}.${recordName}` : recordName;

  for (const field of schema.fields) {
    results.push({
      id: `${filePath}#${currentPath}.${field.name}`,
      name: field.name,
      type: resolveAvroType(field.type),
      description: field.doc || '',
      schemaPath: `${currentPath}.${field.name}`,
      filePath,
      schemaType: 'avro',
      parentName: recordName,
      required: !isNullable(field.type),
      format: undefined,
    });

    // Recurse into nested records
    const nestedType = getNestedRecord(field.type);
    if (nestedType) {
      walkAvroRecord(nestedType, filePath, results, currentPath, visited);
    }
  }
}

function isNullable(type: any): boolean {
  if (Array.isArray(type)) return type.includes('null');
  return false;
}

function getNestedRecord(type: any): any | null {
  if (typeof type === 'object' && !Array.isArray(type) && type.type === 'record') return type;
  if (Array.isArray(type)) {
    for (const t of type) {
      if (typeof t === 'object' && t.type === 'record') return t;
    }
  }
  if (typeof type === 'object' && type.type === 'array' && typeof type.items === 'object' && type.items.type === 'record') {
    return type.items;
  }
  return null;
}

export function parseAvro(content: any, filePath: string): SchemaProperty[] {
  const results: SchemaProperty[] = [];
  walkAvroRecord(content, filePath, results);
  return results;
}
```

## File: `src/parsers/index.ts`
```typescript
import * as fs from 'fs';
import * as path from 'path';
import * as YAML from 'yaml';
import { SchemaProperty, SchemaType } from './types';
import { parseOpenAPI } from './openapi';
import { parseAsyncAPI } from './asyncapi';
import { parseProtobuf } from './protobuf';
import { parseAvro } from './avro';
import { parseJsonSchema } from './jsonschema';

function detectSchemaType(content: any, ext: string): SchemaType | null {
  if (ext === '.proto') return 'protobuf';
  if (ext === '.avsc') return 'avro';
  if (typeof content === 'object' && content !== null) {
    if (content.openapi || content.swagger) return 'openapi';
    if (content.asyncapi) return 'asyncapi';
    if (content.type === 'record' && content.fields) return 'avro';
    if (content.$schema || content.properties || content.type || content.definitions || content.$defs) return 'jsonschema';
  }
  return null;
}

export async function parseFile(absolutePath: string, relativePath: string): Promise<SchemaProperty[]> {
  const ext = path.extname(absolutePath).toLowerCase();

  // Proto files need special handling (protobufjs loads from file path)
  if (ext === '.proto') {
    return parseProtobuf(relativePath, absolutePath);
  }

  // Read and parse file content
  const raw = fs.readFileSync(absolutePath, 'utf-8');
  let content: any;

  try {
    if (ext === '.yaml' || ext === '.yml') {
      content = YAML.parse(raw);
    } else {
      content = JSON.parse(raw);
    }
  } catch (err: any) {
    console.warn(`Warning: Failed to parse ${relativePath}: ${err.message}`);
    return [];
  }

  if (!content || typeof content !== 'object') return [];

  const schemaType = detectSchemaType(content, ext);
  if (!schemaType) return [];

  switch (schemaType) {
    case 'openapi':
      return parseOpenAPI(content, relativePath);
    case 'asyncapi':
      return parseAsyncAPI(content, relativePath);
    case 'avro':
      return parseAvro(content, relativePath);
    case 'jsonschema':
      return parseJsonSchema(content, relativePath);
    default:
      return [];
  }
}
```

## File: `src/parsers/jsonschema.ts`
```typescript
import { SchemaProperty, SchemaType } from './types';

function resolveType(propDef: any): string {
  if (!propDef) return 'unknown';
  if (propDef.$ref) return propDef.$ref.split('/').pop() || '$ref';
  if (propDef.type === 'array' && propDef.items) {
    const itemType = resolveType(propDef.items);
    return `${itemType}[]`;
  }
  if (Array.isArray(propDef.type)) return propDef.type.join(' | ');
  if (propDef.type) return propDef.type;
  if (propDef.enum) return 'enum';
  if (propDef.oneOf) return 'oneOf';
  if (propDef.anyOf) return 'anyOf';
  if (propDef.allOf) return 'allOf';
  return 'unknown';
}

export function walkJsonSchemaObject(
  obj: any,
  parentName: string,
  currentPath: string,
  filePath: string,
  schemaType: SchemaType,
  results: SchemaProperty[],
  visited: Set<string> = new Set()
): void {
  const key = `${filePath}#${currentPath}`;
  if (visited.has(key)) return;
  visited.add(key);

  if (obj.properties) {
    const requiredSet = new Set<string>(obj.required || []);
    for (const [propName, propDef] of Object.entries<any>(obj.properties)) {
      const propPath = `${currentPath}.properties.${propName}`;
      results.push({
        id: `${filePath}#${propPath}`,
        name: propName,
        type: resolveType(propDef),
        description: propDef.description || '',
        schemaPath: propPath,
        filePath,
        schemaType,
        parentName,
        required: requiredSet.has(propName),
        format: propDef.format,
        ref: propDef.$ref,
      });

      if (propDef.properties || propDef.items?.properties) {
        walkJsonSchemaObject(
          propDef.properties ? propDef : propDef.items,
          propName,
          propPath,
          filePath,
          schemaType,
          results,
          visited
        );
      }
    }
  }

  // Handle allOf/oneOf/anyOf
  for (const keyword of ['allOf', 'oneOf', 'anyOf']) {
    if (Array.isArray(obj[keyword])) {
      obj[keyword].forEach((subSchema: any, i: number) => {
        walkJsonSchemaObject(
          subSchema,
          parentName,
          `${currentPath}.${keyword}[${i}]`,
          filePath,
          schemaType,
          results,
          visited
        );
      });
    }
  }

  // Handle array items
  if (obj.items && typeof obj.items === 'object' && !Array.isArray(obj.items)) {
    walkJsonSchemaObject(
      obj.items,
      parentName,
      `${currentPath}.items`,
      filePath,
      schemaType,
      results,
      visited
    );
  }
}

export function parseJsonSchema(content: any, filePath: string): SchemaProperty[] {
  const results: SchemaProperty[] = [];

  // Walk top-level schema
  const name = content.title || 'root';
  walkJsonSchemaObject(content, name, name, filePath, 'jsonschema', results);

  // Walk definitions/$defs
  const defs = content.definitions || content.$defs;
  if (defs) {
    for (const [defName, defSchema] of Object.entries<any>(defs)) {
      walkJsonSchemaObject(defSchema, defName, `definitions.${defName}`, filePath, 'jsonschema', results);
    }
  }

  return results;
}
```

## File: `src/parsers/openapi.ts`
```typescript
import { SchemaProperty } from './types';
import { walkJsonSchemaObject } from './jsonschema';

export function parseOpenAPI(content: any, filePath: string): SchemaProperty[] {
  const results: SchemaProperty[] = [];

  // OpenAPI 3.x: components.schemas
  const schemas = content.components?.schemas;
  if (schemas) {
    for (const [schemaName, schemaDef] of Object.entries<any>(schemas)) {
      walkJsonSchemaObject(
        schemaDef,
        schemaName,
        `components.schemas.${schemaName}`,
        filePath,
        'openapi',
        results
      );
    }
  }

  // Swagger 2.0: definitions
  const definitions = content.definitions;
  if (definitions) {
    for (const [defName, defSchema] of Object.entries<any>(definitions)) {
      walkJsonSchemaObject(
        defSchema,
        defName,
        `definitions.${defName}`,
        filePath,
        'openapi',
        results
      );
    }
  }

  // Also walk request/response bodies inline in paths
  if (content.paths) {
    for (const [pathStr, pathItem] of Object.entries<any>(content.paths)) {
      for (const [method, operation] of Object.entries<any>(pathItem)) {
        if (['get', 'post', 'put', 'patch', 'delete', 'options', 'head'].includes(method)) {
          // OpenAPI 3.x requestBody
          const requestBody = operation.requestBody?.content;
          if (requestBody) {
            for (const [mediaType, mediaObj] of Object.entries<any>(requestBody)) {
              if (mediaObj.schema) {
                walkJsonSchemaObject(
                  mediaObj.schema,
                  `${method.toUpperCase()} ${pathStr} request`,
                  `paths.${pathStr}.${method}.requestBody.${mediaType}`,
                  filePath,
                  'openapi',
                  results
                );
              }
            }
          }

          // Responses
          if (operation.responses) {
            for (const [statusCode, response] of Object.entries<any>(operation.responses)) {
              const responseContent = response.content;
              if (responseContent) {
                for (const [mediaType, mediaObj] of Object.entries<any>(responseContent)) {
                  if (mediaObj.schema) {
                    walkJsonSchemaObject(
                      mediaObj.schema,
                      `${method.toUpperCase()} ${pathStr} ${statusCode}`,
                      `paths.${pathStr}.${method}.responses.${statusCode}.${mediaType}`,
                      filePath,
                      'openapi',
                      results
                    );
                  }
                }
              }
              // Swagger 2.0 response schema
              if (response.schema) {
                walkJsonSchemaObject(
                  response.schema,
                  `${method.toUpperCase()} ${pathStr} ${statusCode}`,
                  `paths.${pathStr}.${method}.responses.${statusCode}`,
                  filePath,
                  'openapi',
                  results
                );
              }
            }
          }
        }
      }
    }
  }

  return results;
}
```

## File: `src/parsers/protobuf.ts`
```typescript
import * as protobuf from 'protobufjs';
import { SchemaProperty } from './types';

function walkType(
  type: protobuf.ReflectionObject,
  filePath: string,
  results: SchemaProperty[],
  pathPrefix: string = ''
): void {
  if (type instanceof protobuf.Type) {
    const parentName = type.name;
    const currentPath = pathPrefix ? `${pathPrefix}.${parentName}` : parentName;

    for (const field of type.fieldsArray) {
      results.push({
        id: `${filePath}#${currentPath}.${field.name}`,
        name: field.name,
        type: field.repeated ? `${field.type}[]` : field.type,
        description: field.comment || '',
        schemaPath: `${currentPath}.${field.name}`,
        filePath,
        schemaType: 'protobuf',
        parentName,
        required: field.required,
        format: field.repeated ? 'repeated' : undefined,
      });
    }

    // Recurse into nested types
    if (type.nestedArray) {
      for (const nested of type.nestedArray) {
        walkType(nested, filePath, results, currentPath);
      }
    }
  } else if (type instanceof protobuf.Namespace) {
    const currentPath = pathPrefix ? `${pathPrefix}.${type.name}` : type.name;
    if (type.nestedArray) {
      for (const nested of type.nestedArray) {
        walkType(nested, filePath, results, currentPath);
      }
    }
  }
}

export async function parseProtobuf(filePath: string, absolutePath: string): Promise<SchemaProperty[]> {
  const results: SchemaProperty[] = [];

  try {
    const root = await protobuf.load(absolutePath);
    if (root.nestedArray) {
      for (const nested of root.nestedArray) {
        walkType(nested, filePath, results);
      }
    }
  } catch (err: any) {
    console.warn(`Warning: Failed to parse proto file ${filePath}: ${err.message}`);
  }

  return results;
}
```

## File: `src/parsers/types.ts`
```typescript
export type SchemaType = 'openapi' | 'asyncapi' | 'protobuf' | 'avro' | 'jsonschema';

export interface SchemaProperty {
  id: string;
  name: string;
  type: string;
  description: string;
  schemaPath: string;
  filePath: string;
  schemaType: SchemaType;
  parentName: string;
  required: boolean;
  format?: string;
  ref?: string;
}

export interface ParseResult {
  properties: SchemaProperty[];
  filePath: string;
  schemaType: SchemaType;
}
```

## File: `src/scanner/index.ts`
```typescript
import { glob } from 'glob';
import * as path from 'path';

const SCHEMA_EXTENSIONS = [
  '**/*.yaml',
  '**/*.yml',
  '**/*.json',
  '**/*.proto',
  '**/*.avsc',
];

const IGNORE_PATTERNS = [
  '**/node_modules/**',
  '**/dist/**',
  '**/build/**',
  '**/.git/**',
  '**/package.json',
  '**/package-lock.json',
  '**/tsconfig.json',
  '**/tsconfig.*.json',
];

export async function scanDirectory(dir: string): Promise<{ absolutePath: string; relativePath: string }[]> {
  const absoluteDir = path.resolve(dir);
  const files: { absolutePath: string; relativePath: string }[] = [];

  for (const pattern of SCHEMA_EXTENSIONS) {
    const matches = await glob(pattern, {
      cwd: absoluteDir,
      absolute: false,
      ignore: IGNORE_PATTERNS,
      nodir: true,
    });

    for (const match of matches) {
      files.push({
        absolutePath: path.join(absoluteDir, match),
        relativePath: match,
      });
    }
  }

  // Deduplicate (a file could match multiple patterns)
  const seen = new Set<string>();
  return files.filter((f) => {
    if (seen.has(f.absolutePath)) return false;
    seen.add(f.absolutePath);
    return true;
  });
}
```

## File: `ui/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>FieldTrip</title>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="/src/main.ts"></script>
</body>
</html>
```

## File: `ui/src/main.ts`
```typescript
import './styles/main.css';
import * as monaco from 'monaco-editor';
import * as d3 from 'd3';

import editorWorker from 'monaco-editor/esm/vs/editor/editor.worker?worker';
import jsonWorker from 'monaco-editor/esm/vs/language/json/json.worker?worker';

self.MonacoEnvironment = {
  getWorker(_: any, label: string) {
    if (label === 'json') return new jsonWorker();
    return new editorWorker();
  },
};

// ─── Types ───

interface Property {
  id: string;
  name: string;
  type: string;
  description: string;
  schemaPath: string;
  filePath: string;
  schemaType: string;
  parentName: string;
  required: boolean;
  format?: string;
  ref?: string;
  score?: number;
}

interface SchemaInfo { filePath: string; schemaType: string; count: number; }
interface Stats { totalProperties: number; totalFiles: number; schemaTypes: Record<string, number>; }

interface GraphNode extends d3.SimulationNodeDatum {
  id: string;
  label: string;
  nodeType: 'schema' | 'property';
  schemaType?: string;
  filePath?: string;
  propertyName?: string;
  propertyType?: string;
  parentName?: string;
  count?: number;
}

interface GraphLink extends d3.SimulationLinkDatum<GraphNode> {
  linkType: 'belongs-to' | 'shared-name';
}

// ─── Constants ───

const TYPE_COLORS: Record<string, string> = {
  openapi: '#3b82f6', asyncapi: '#8b5cf6', protobuf: '#10b981',
  avro: '#f59e0b', jsonschema: '#6366f1',
};

const TYPE_LABELS: Record<string, string> = {
  openapi: 'OPENAPI', asyncapi: 'ASYNCAPI', protobuf: 'PROTO',
  avro: 'AVRO', jsonschema: 'JSON',
};

const TYPE_BG: Record<string, string> = {
  openapi: 'rgba(59,130,246,0.15)', asyncapi: 'rgba(139,92,246,0.15)',
  protobuf: 'rgba(16,185,129,0.15)', avro: 'rgba(245,158,11,0.15)',
  jsonschema: 'rgba(99,102,241,0.15)',
};

const DATA_TYPE_COLORS: Record<string, string> = {
  string: '#22d3ee', integer: '#a78bfa', int32: '#a78bfa', int64: '#a78bfa',
  number: '#a78bfa', double: '#f472b6', float: '#f472b6',
  boolean: '#fb923c', object: '#94a3b8', array: '#34d399',
};

const FILE_LANGUAGES: Record<string, string> = {
  '.yaml': 'yaml', '.yml': 'yaml', '.json': 'json', '.avsc': 'json', '.proto': 'protobuf',
};

// ─── State ───

let allProperties: Property[] = [];
let filteredProperties: Property[] = [];
let schemas: SchemaInfo[] = [];
let activeSchemaFilters: Set<string> = new Set();
let activeTypeFilter: string | null = null;
let sortField: 'name' | 'schema' | 'type' = 'name';
let sortAsc = true;
let searchQuery = '';
let debounceTimer: ReturnType<typeof setTimeout>;
let activeView: 'table' | 'graph' | 'matrix' = 'table';

// Monaco state
let editorInstance: monaco.editor.IStandaloneCodeEditor | null = null;
let currentDecorations: monaco.editor.IEditorDecorationsCollection | null = null;
let currentFilePath: string | null = null;
let showingDetail = false;

// Graph state
let simulation: d3.Simulation<GraphNode, GraphLink> | null = null;
let graphOnlyShared = true;

// Matrix state
let matrixSortField: 'alpha' | 'count' | 'required' = 'count';
let matrixSortAsc = false;

const app = document.getElementById('app')!;

// ─── Init ───

async function init() {
  const [stats, propsData, schemasData] = await Promise.all([
    fetch('/api/stats').then(r => r.json()) as Promise<Stats>,
    fetch('/api/properties').then(r => r.json()),
    fetch('/api/schemas').then(r => r.json()),
  ]);

  allProperties = propsData.properties;
  filteredProperties = [...allProperties];
  schemas = schemasData.schemas;
  sortProperties();

  app.innerHTML = `
    <nav class="topbar">
      <div class="topbar-left">
        <div class="logo">
          <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#3b82f6"/><path d="M10 12h12M10 16h8M10 20h10" stroke="#fff" stroke-width="2" stroke-linecap="round"/></svg>
        </div>
        <div class="topbar-title">
          <h1>FieldTrip</h1>
          <span class="topbar-stats">${stats.totalFiles} SCHEMAS &middot; ${stats.totalProperties} PROPERTIES</span>
        </div>
      </div>
      <div class="view-tabs" id="view-tabs">
        <button class="view-tab active" data-view="table">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
          Table
        </button>
        <button class="view-tab" data-view="matrix">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="4" height="4"/><rect x="10" y="3" width="4" height="4"/><rect x="17" y="3" width="4" height="4"/><rect x="3" y="10" width="4" height="4"/><rect x="10" y="10" width="4" height="4"/><rect x="3" y="17" width="4" height="4"/><rect x="17" y="17" width="4" height="4"/></svg>
          Matrix
        </button>
        <button class="view-tab" data-view="graph">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><line x1="7" y1="6" x2="17" y2="6"/><line x1="6" y1="8" x2="11" y2="16"/><line x1="18" y1="8" x2="13" y2="16"/></svg>
          Graph
        </button>
      </div>
    </nav>

    <div class="main-layout">
      <aside class="sidebar" id="sidebar">
        <div class="sidebar-section">
          <div class="sidebar-heading">SCHEMAS<button class="clear-btn" id="clear-schemas">clear all</button></div>
          <div class="schema-list" id="schema-list"></div>
        </div>
      </aside>

      <main class="content" id="content">
        <div class="content-top">
          <div class="search-bar">
            <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
            <input type="text" id="search-input" placeholder="Search properties, types, descriptions..." autofocus />
          </div>
          <div class="type-filters" id="type-filters"></div>
        </div>

        <div id="table-view">
          <div class="table-toolbar" id="table-toolbar"></div>
          <div class="table-wrapper" id="table-wrapper"></div>
        </div>

        <div id="detail-view" class="detail-view hidden">
          <button class="back-btn" id="back-btn">&larr; Back to results</button>
          <div class="detail-header" id="detail-header"></div>
          <div class="detail-editor" id="editor-container"></div>
        </div>

        <div id="matrix-view" class="matrix-view hidden">
          <div class="matrix-toolbar" id="matrix-toolbar"></div>
          <div class="matrix-container" id="matrix-container"></div>
        </div>

        <div id="graph-view" class="graph-view hidden">
          <div class="graph-toolbar" id="graph-toolbar"></div>
          <div class="graph-container" id="graph-container"></div>
        </div>
      </main>
    </div>
  `;

  // Create Monaco (hidden initially)
  editorInstance = monaco.editor.create(document.getElementById('editor-container')!, {
    value: '', language: 'yaml', theme: 'vs-dark', readOnly: true,
    minimap: { enabled: false }, scrollBeyondLastLine: false, fontSize: 13,
    lineNumbers: 'on', renderLineHighlight: 'none', automaticLayout: true,
    padding: { top: 12 }, scrollbar: { verticalScrollbarSize: 8, horizontalScrollbarSize: 8 },
  });

  renderSidebar();
  renderTable();
  bindEvents();
}

// ─── Sidebar ───

function renderSidebar() {
  document.getElementById('schema-list')!.innerHTML = schemas.map(s => {
    const color = TYPE_COLORS[s.schemaType] || '#666';
    const label = TYPE_LABELS[s.schemaType] || s.schemaType.toUpperCase();
    const active = activeSchemaFilters.has(s.filePath);
    const name = s.filePath.replace(/\.[^.]+$/, '');
    return `
      <div class="schema-item${active ? ' active' : ''}" data-file="${esc(s.filePath)}">
        <span class="schema-badge" style="background:${TYPE_BG[s.schemaType]};color:${color}">${label}</span>
        <div class="schema-info">
          <span class="schema-name">${esc(name)}</span>
          <span class="schema-filepath">${esc(s.filePath)}</span>
        </div>
        <span class="schema-count">${s.count}</span>
      </div>
    `;
  }).join('');

  const allTypes = ['all types', ...Object.keys(TYPE_LABELS)];
  document.getElementById('type-filters')!.innerHTML = allTypes.map(t => {
    const isAll = t === 'all types';
    const active = isAll ? !activeTypeFilter : activeTypeFilter === t;
    const label = isAll ? 'all types' : TYPE_LABELS[t]?.toLowerCase() || t;
    return `<button class="type-chip${active ? ' active' : ''}" data-type="${t}">${label}</button>`;
  }).join('');
}

// ─── View Switching ───

function switchView(view: 'table' | 'graph' | 'matrix') {
  if (activeView === view) return;
  activeView = view;

  if (showingDetail) hideDetail();

  document.getElementById('table-view')!.classList.toggle('hidden', view !== 'table');
  document.getElementById('graph-view')!.classList.toggle('hidden', view !== 'graph');
  document.getElementById('matrix-view')!.classList.toggle('hidden', view !== 'matrix');

  document.querySelectorAll('.view-tab').forEach(tab => {
    tab.classList.toggle('active', (tab as HTMLElement).dataset.view === view);
  });

  if (view === 'graph') {
    renderGraph();
  } else if (view === 'matrix') {
    if (simulation) { simulation.stop(); simulation = null; }
    renderMatrix();
  } else {
    if (simulation) { simulation.stop(); simulation = null; }
    renderTable();
  }
}

// ─── Table ───

function renderTable() {
  const toolbar = document.getElementById('table-toolbar')!;
  const wrapper = document.getElementById('table-wrapper')!;

  toolbar.innerHTML = `
    <span class="table-count"><strong>${filteredProperties.length}</strong> of ${allProperties.length} properties</span>
    <div class="sort-controls">
      <button class="sort-btn${sortField === 'name' ? ' active' : ''}" data-sort="name">name ${sortField === 'name' ? (sortAsc ? '&uarr;' : '&darr;') : ''}</button>
      <button class="sort-btn${sortField === 'schema' ? ' active' : ''}" data-sort="schema">schema ${sortField === 'schema' ? (sortAsc ? '&uarr;' : '&darr;') : ''}</button>
      <button class="sort-btn${sortField === 'type' ? ' active' : ''}" data-sort="type">type ${sortField === 'type' ? (sortAsc ? '&uarr;' : '&darr;') : ''}</button>
    </div>
  `;

  if (filteredProperties.length === 0) {
    wrapper.innerHTML = '<div class="table-empty">No properties match your filters</div>';
    return;
  }

  wrapper.innerHTML = `
    <table class="prop-table">
      <thead><tr><th>PROPERTY</th><th>TYPE</th><th>SCHEMA</th><th>REQUIRED</th><th>DESCRIPTION</th></tr></thead>
      <tbody>${filteredProperties.map(p => renderRow(p)).join('')}</tbody>
    </table>
  `;
}

function renderRow(p: Property): string {
  const typeColor = getDataTypeColor(p.type);
  const schemaColor = TYPE_COLORS[p.schemaType] || '#666';
  const schemaLabel = TYPE_LABELS[p.schemaType] || p.schemaType.toUpperCase();
  const schemaBg = TYPE_BG[p.schemaType] || 'rgba(100,100,100,0.15)';
  const schemaName = p.filePath.replace(/\.[^.]+$/, '');
  const reqText = p.required
    ? '<span class="req-yes"><span class="req-dot"></span>required</span>'
    : '<span class="req-no">optional</span>';

  return `
    <tr class="prop-row" data-id="${esc(p.id)}" data-file="${esc(p.filePath)}">
      <td class="col-property"><span class="prop-name">${esc(p.name)}</span><span class="prop-parent">${esc(p.parentName)}</span></td>
      <td class="col-type"><span class="type-badge" style="color:${typeColor};background:${typeColor}15">${esc(p.type)}</span></td>
      <td class="col-schema"><span class="schema-badge-sm" style="background:${schemaBg};color:${schemaColor}">${schemaLabel}</span><span class="schema-file">${esc(schemaName)}</span></td>
      <td class="col-required">${reqText}</td>
      <td class="col-desc">${p.description ? esc(p.description) : '<span class="no-desc">&mdash;</span>'}</td>
    </tr>
  `;
}

function getDataTypeColor(type: string): string {
  return DATA_TYPE_COLORS[type.replace(/\[\]$/, '').toLowerCase()] || '#94a3b8';
}

// ─── Detail View (Monaco) ───

async function showDetail(property: Property) {
  showingDetail = true;
  document.getElementById('table-view')!.classList.add('hidden');
  document.getElementById('detail-view')!.classList.remove('hidden');

  const color = TYPE_COLORS[property.schemaType] || '#666';
  const label = TYPE_LABELS[property.schemaType] || property.schemaType.toUpperCase();
  const bg = TYPE_BG[property.schemaType] || 'rgba(100,100,100,0.15)';
  const typeColor = getDataTypeColor(property.type);

  document.getElementById('detail-header')!.innerHTML = `
    <div class="detail-title-row">
      <span class="detail-name">${esc(property.name)}</span>
      <span class="type-badge" style="color:${typeColor};background:${typeColor}15">${esc(property.type)}</span>
      ${property.required ? '<span class="req-yes"><span class="req-dot"></span>required</span>' : ''}
      ${property.format ? `<span class="detail-format">${esc(property.format)}</span>` : ''}
      <span class="schema-badge-sm" style="background:${bg};color:${color}">${label}</span>
    </div>
    ${property.description ? `<p class="detail-desc">${esc(property.description)}</p>` : ''}
    <div class="detail-path">${esc(property.filePath)} &middot; ${esc(property.schemaPath)}</div>
  `;

  if (currentFilePath !== property.filePath) {
    try {
      const data = await fetch(`/api/file?path=${encodeURIComponent(property.filePath)}`).then(r => r.json());
      currentFilePath = property.filePath;
      const ext = '.' + property.filePath.split('.').pop()?.toLowerCase();
      const model = editorInstance!.getModel()!;
      monaco.editor.setModelLanguage(model, FILE_LANGUAGES[ext] || 'plaintext');
      model.setValue(data.content);
    } catch {
      editorInstance!.getModel()!.setValue('// Failed to load file');
      currentFilePath = null;
    }
  }

  editorInstance!.layout();
  highlightProperty(property);
}

function hideDetail() {
  showingDetail = false;
  document.getElementById('detail-view')!.classList.add('hidden');
  document.getElementById('table-view')!.classList.remove('hidden');
}

function highlightProperty(property: Property) {
  if (!editorInstance) return;
  const model = editorInstance.getModel();
  if (!model) return;

  const lines = model.getLinesContent();
  const matchLines = findPropertyLines(lines, property);
  if (currentDecorations) currentDecorations.clear();
  if (matchLines.length > 0) {
    currentDecorations = editorInstance.createDecorationsCollection(
      matchLines.map(i => ({ range: new monaco.Range(i + 1, 1, i + 1, 1), options: { isWholeLine: true, className: 'highlighted-line' } }))
    );
    editorInstance.revealLineInCenter(matchLines[0] + 1);
  }
}

function findPropertyLines(lines: string[], result: Property): number[] {
  const matches: number[] = [];
  const propName = result.name;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (result.schemaType === 'protobuf') {
      if (new RegExp(`\\b${escRegex(propName)}\\s*=\\s*\\d+`).test(line)) matches.push(i);
    } else {
      if (new RegExp(`^\\s*${escRegex(propName)}\\s*:`).test(line) ||
          new RegExp(`"${escRegex(propName)}"\\s*:`).test(line)) matches.push(i);
    }
  }
  return matches;
}

// ─── Matrix View ───

interface MatrixRow {
  name: string;
  primaryType: string;
  occurrences: Map<string, { required: boolean; type: string; property: Property }>;
  totalSchemas: number;
  requiredCount: number;
}

function buildMatrixData(properties: Property[]): { rows: MatrixRow[]; schemaColumns: SchemaInfo[] } {
  // Group properties by lowercase name
  const nameMap = new Map<string, MatrixRow>();
  for (const p of properties) {
    const key = p.name.toLowerCase();
    if (!nameMap.has(key)) {
      nameMap.set(key, { name: p.name, primaryType: p.type, occurrences: new Map(), totalSchemas: 0, requiredCount: 0 });
    }
    const row = nameMap.get(key)!;
    // Prefer the casing from first occurrence
    if (!row.occurrences.has(p.filePath)) {
      row.occurrences.set(p.filePath, { required: p.required, type: p.type, property: p });
    }
  }

  // Compute counts
  for (const row of nameMap.values()) {
    row.totalSchemas = row.occurrences.size;
    row.requiredCount = Array.from(row.occurrences.values()).filter(o => o.required).length;
  }

  let rows = Array.from(nameMap.values());

  // Sort rows
  rows.sort((a, b) => {
    let cmp: number;
    switch (matrixSortField) {
      case 'alpha': cmp = a.name.localeCompare(b.name); break;
      case 'count': cmp = b.totalSchemas - a.totalSchemas; break;
      case 'required': cmp = b.requiredCount - a.requiredCount; break;
      default: cmp = 0;
    }
    return matrixSortAsc ? -cmp : cmp;
  });

  // Only include schemas that appear in the filtered properties
  const schemaFileSet = new Set(properties.map(p => p.filePath));
  const schemaColumns = schemas.filter(s => schemaFileSet.has(s.filePath));

  return { rows, schemaColumns };
}

function renderMatrix() {
  const toolbar = document.getElementById('matrix-toolbar')!;
  const container = document.getElementById('matrix-container')!;

  const { rows, schemaColumns } = buildMatrixData(filteredProperties);

  // Filter to only rows that appear in 2+ schemas by default (can show all)
  const sharedRows = rows.filter(r => r.totalSchemas >= 2);
  const displayRows = sharedRows.length > 0 ? sharedRows : rows;

  const sortBtns = (['alpha', 'count', 'required'] as const).map(f => {
    const labels: Record<string, string> = { alpha: 'A-Z', count: 'frequency', required: 'required' };
    const active = matrixSortField === f;
    return `<button class="sort-btn${active ? ' active' : ''}" data-msort="${f}">${labels[f]}</button>`;
  }).join('');

  toolbar.innerHTML = `
    <span class="matrix-stats"><strong>${displayRows.length}</strong> properties &times; <strong>${schemaColumns.length}</strong> schemas</span>
    <div class="matrix-controls">
      <span class="matrix-sort-label">Sort:</span>
      <div class="sort-controls">${sortBtns}</div>
      <div class="matrix-legend">
        <span class="legend-item"><span class="legend-dot" style="background:#22c55e"></span>required</span>
        <span class="legend-item"><span class="legend-dot" style="background:#3b82f6"></span>optional</span>
        <span class="legend-item"><span class="legend-dot" style="background:transparent;border:1px solid var(--border)"></span>absent</span>
      </div>
    </div>
  `;

  if (displayRows.length === 0 || schemaColumns.length === 0) {
    container.innerHTML = '<div class="matrix-empty">No data to display in the matrix</div>';
    return;
  }

  // Build the matrix grid using a scrollable div with sticky headers
  const CELL_SIZE = 28;
  const PROP_COL_WIDTH = 180;
  const COUNT_COL_WIDTH = 50;
  const HEADER_HEIGHT = 120;

  // We'll render a virtualized approach: render all rows but use CSS grid
  let html = `<div class="matrix-grid" style="grid-template-columns: ${PROP_COL_WIDTH}px ${COUNT_COL_WIDTH}px repeat(${schemaColumns.length}, ${CELL_SIZE}px);">`;

  // Header row — property label + count + schema names (rotated)
  html += `<div class="matrix-header-cell matrix-corner">Property</div>`;
  html += `<div class="matrix-header-cell matrix-count-header">#</div>`;
  for (let ci = 0; ci < schemaColumns.length; ci++) {
    const s = schemaColumns[ci];
    const color = TYPE_COLORS[s.schemaType] || '#666';
    const name = s.filePath.replace(/\.[^.]+$/, '').split('/').pop()!;
    html += `<div class="matrix-header-cell matrix-schema-header" data-col="${ci}" data-file="${esc(s.filePath)}" title="${esc(s.filePath)}"><span class="matrix-schema-label" style="color:${color}">${esc(name)}</span></div>`;
  }

  // Data rows
  for (let ri = 0; ri < displayRows.length; ri++) {
    const row = displayRows[ri];
    const isShared = row.totalSchemas >= 2;

    const typeColor = getDataTypeColor(row.primaryType);
    html += `<div class="matrix-prop-cell" data-row="${ri}" data-name="${esc(row.name)}">${esc(row.name)} <span class="matrix-prop-type" style="color:${typeColor}">(${esc(row.primaryType)})</span>${isShared ? `<span class="matrix-shared-badge">${row.totalSchemas}</span>` : ''}</div>`;
    html += `<div class="matrix-count-cell" data-row="${ri}">${row.totalSchemas}</div>`;

    for (let ci = 0; ci < schemaColumns.length; ci++) {
      const s = schemaColumns[ci];
      const occ = row.occurrences.get(s.filePath);
      let cls = 'matrix-cell';
      let title = '';
      if (occ) {
        cls += occ.required ? ' matrix-cell-required' : ' matrix-cell-optional';
        title = `${row.name} (${occ.type}) in ${s.filePath.replace(/\.[^.]+$/, '').split('/').pop()} — ${occ.required ? 'required' : 'optional'}`;
      } else {
        cls += ' matrix-cell-empty';
      }
      html += `<div class="${cls}" data-row="${ri}" data-col="${ci}" data-name="${esc(row.name)}" data-file="${esc(s.filePath)}" title="${esc(title)}"></div>`;
    }
  }

  html += '</div>';
  container.innerHTML = html;

  // ─── Matrix interactions ───
  const grid = container.querySelector('.matrix-grid') as HTMLElement;

  // Tooltip
  let matrixTooltip = container.querySelector('.matrix-tooltip') as HTMLElement;
  if (!matrixTooltip) {
    matrixTooltip = document.createElement('div');
    matrixTooltip.className = 'matrix-tooltip';
    container.appendChild(matrixTooltip);
  }

  // Hover cells — show tooltip + highlight row/col
  grid.addEventListener('mouseover', (e) => {
    const cell = (e.target as HTMLElement).closest('.matrix-cell, .matrix-prop-cell, .matrix-schema-header') as HTMLElement | null;
    if (!cell) return;

    const rowIdx = cell.dataset.row;
    const colIdx = cell.dataset.col;
    const propName = cell.dataset.name;
    const filePath = cell.dataset.file;

    // Highlight row
    if (rowIdx !== undefined) {
      grid.querySelectorAll(`[data-row="${rowIdx}"]`).forEach(el => el.classList.add('matrix-highlight-row'));
    }
    // Highlight column
    if (colIdx !== undefined) {
      grid.querySelectorAll(`[data-col="${colIdx}"]`).forEach(el => el.classList.add('matrix-highlight-col'));
    }

    // Show tooltip for data cells
    if (cell.classList.contains('matrix-cell') && !cell.classList.contains('matrix-cell-empty')) {
      const row = displayRows[Number(rowIdx)];
      const schema = schemaColumns[Number(colIdx)];
      if (row && schema) {
        const occ = row.occurrences.get(schema.filePath);
        if (occ) {
          const schemaName = schema.filePath.replace(/\.[^.]+$/, '').split('/').pop()!;
          const schemaColor = TYPE_COLORS[schema.schemaType] || '#666';
          matrixTooltip.innerHTML = `
            <div class="tt-label">${esc(row.name)}</div>
            <div class="tt-detail">Type: <span style="color:${getDataTypeColor(occ.type)}">${esc(occ.type)}</span></div>
            <div class="tt-detail">Schema: <span style="color:${schemaColor}">${esc(schemaName)}</span></div>
            <div class="tt-detail">${occ.required ? '<span style="color:#22c55e">required</span>' : '<span style="color:#3b82f6">optional</span>'}</div>
          `;
          const rect = container.getBoundingClientRect();
          const cellRect = cell.getBoundingClientRect();
          matrixTooltip.style.left = (cellRect.left - rect.left + cellRect.width + 8) + 'px';
          matrixTooltip.style.top = (cellRect.top - rect.top - 10) + 'px';
          matrixTooltip.style.opacity = '1';
        }
      }
    }

    // Hovering a property row header — highlight all schemas containing it
    if (cell.classList.contains('matrix-prop-cell') && propName) {
      const row = displayRows[Number(rowIdx)];
      if (row) {
        for (let ci = 0; ci < schemaColumns.length; ci++) {
          if (row.occurrences.has(schemaColumns[ci].filePath)) {
            grid.querySelectorAll(`[data-col="${ci}"]`).forEach(el => el.classList.add('matrix-highlight-col'));
          }
        }
      }
    }

    // Hovering a schema column header — highlight all properties in it
    if (cell.classList.contains('matrix-schema-header') && filePath) {
      for (let ri = 0; ri < displayRows.length; ri++) {
        if (displayRows[ri].occurrences.has(filePath)) {
          grid.querySelectorAll(`[data-row="${ri}"]`).forEach(el => el.classList.add('matrix-highlight-row'));
        }
      }
    }
  });

  grid.addEventListener('mouseout', (e) => {
    const cell = (e.target as HTMLElement).closest('.matrix-cell, .matrix-prop-cell, .matrix-schema-header') as HTMLElement | null;
    if (!cell) return;
    grid.querySelectorAll('.matrix-highlight-row').forEach(el => el.classList.remove('matrix-highlight-row'));
    grid.querySelectorAll('.matrix-highlight-col').forEach(el => el.classList.remove('matrix-highlight-col'));
    matrixTooltip.style.opacity = '0';
  });

  // Click a property row — show detail for first occurrence
  grid.addEventListener('click', (e) => {
    const cell = (e.target as HTMLElement).closest('.matrix-prop-cell') as HTMLElement | null;
    if (cell) {
      const row = displayRows[Number(cell.dataset.row)];
      if (row) {
        const firstOcc = Array.from(row.occurrences.values())[0];
        if (firstOcc) showDetail(firstOcc.property);
      }
      return;
    }

    // Click a schema column header — filter sidebar to that schema
    const header = (e.target as HTMLElement).closest('.matrix-schema-header') as HTMLElement | null;
    if (header && header.dataset.file) {
      const file = header.dataset.file;
      activeSchemaFilters.clear();
      activeSchemaFilters.add(file);
      renderSidebar();
      applyFilters();
    }
  });
}

// ─── Graph View ───

function buildGraphData(properties: Property[]): { nodes: GraphNode[]; links: GraphLink[] } {
  const nodes: GraphNode[] = [];
  const links: GraphLink[] = [];

  // Find shared property names (appear in 2+ different files)
  const nameGroups = new Map<string, Property[]>();
  for (const p of properties) {
    const key = p.name.toLowerCase();
    if (!nameGroups.has(key)) nameGroups.set(key, []);
    nameGroups.get(key)!.push(p);
  }

  const sharedNames = new Set<string>();
  for (const [key, group] of nameGroups) {
    const uniqueFiles = new Set(group.map(p => p.filePath));
    if (uniqueFiles.size >= 2) sharedNames.add(key);
  }

  // Filter properties to only shared if toggle is on
  const graphProperties = graphOnlyShared
    ? properties.filter(p => sharedNames.has(p.name.toLowerCase()))
    : properties;

  // Schema nodes (only include schemas that have properties in the graph)
  const schemaMap = new Map<string, Property[]>();
  for (const p of graphProperties) {
    if (!schemaMap.has(p.filePath)) schemaMap.set(p.filePath, []);
    schemaMap.get(p.filePath)!.push(p);
  }

  for (const [filePath, props] of schemaMap) {
    nodes.push({
      id: `schema:${filePath}`,
      label: filePath.replace(/\.[^.]+$/, '').split('/').pop()!,
      nodeType: 'schema',
      schemaType: props[0].schemaType,
      filePath,
      count: props.length,
    });
  }

  // Property nodes + belongs-to links
  for (const p of graphProperties) {
    nodes.push({
      id: `prop:${p.id}`,
      label: p.name,
      nodeType: 'property',
      schemaType: p.schemaType,
      propertyName: p.name,
      propertyType: p.type,
      parentName: p.parentName,
      filePath: p.filePath,
    });
    links.push({
      source: `prop:${p.id}`,
      target: `schema:${p.filePath}`,
      linkType: 'belongs-to',
    });
  }

  // Shared-name links — connect properties with same name across different schemas
  for (const [, group] of nameGroups) {
    const crossFile = group.filter(p => graphProperties.includes(p));
    const uniqueFiles = new Set(crossFile.map(p => p.filePath));
    if (uniqueFiles.size < 2) continue;

    // Chain pattern to avoid O(n^2) links
    for (let i = 1; i < crossFile.length; i++) {
      if (crossFile[i].filePath !== crossFile[i - 1].filePath) {
        links.push({
          source: `prop:${crossFile[i - 1].id}`,
          target: `prop:${crossFile[i].id}`,
          linkType: 'shared-name',
        });
      }
    }
  }

  return { nodes, links };
}

function renderGraph() {
  const container = document.getElementById('graph-container')!;
  const toolbar = document.getElementById('graph-toolbar')!;
  container.innerHTML = '';

  if (simulation) { simulation.stop(); simulation = null; }

  const props = filteredProperties;
  const { nodes, links } = buildGraphData(props);

  // Stats for toolbar
  const nameGroups = new Map<string, Set<string>>();
  for (const p of props) {
    const key = p.name.toLowerCase();
    if (!nameGroups.has(key)) nameGroups.set(key, new Set());
    nameGroups.get(key)!.add(p.filePath);
  }
  let sharedCount = 0;
  for (const [, files] of nameGroups) { if (files.size >= 2) sharedCount++; }

  const schemaNodes = nodes.filter(n => n.nodeType === 'schema').length;
  const propNodes = nodes.filter(n => n.nodeType === 'property').length;
  const sharedLinks = links.filter(l => l.linkType === 'shared-name').length;

  toolbar.innerHTML = `
    <span class="graph-stats"><strong>${propNodes}</strong> properties &middot; <strong>${schemaNodes}</strong> schemas &middot; <strong>${sharedCount}</strong> shared names &middot; <strong>${sharedLinks}</strong> connections</span>
    <div class="graph-controls">
      <label class="graph-toggle">
        <input type="checkbox" id="shared-toggle" ${graphOnlyShared ? 'checked' : ''} />
        Shared only
      </label>
      <div class="graph-legend">
        ${Object.entries(TYPE_COLORS).map(([k, c]) => `<span class="legend-item"><span class="legend-dot" style="background:${c}"></span>${TYPE_LABELS[k]}</span>`).join('')}
        <span class="legend-item"><span class="legend-dot" style="background:#f59e0b;border-radius:0;width:16px;height:2px"></span>shared link</span>
      </div>
    </div>
  `;

  if (nodes.length === 0) {
    container.innerHTML = '<div class="graph-empty">No shared properties to display. Uncheck "Shared only" to see all properties.</div>';
    return;
  }

  let width = container.clientWidth || 800;
  let height = container.clientHeight || 600;

  const svg = d3.select(container)
    .append('svg')
    .attr('width', width)
    .attr('height', height)
    .attr('viewBox', `0 0 ${width} ${height}`);

  const g = svg.append('g');

  const zoom = d3.zoom<SVGSVGElement, unknown>()
    .scaleExtent([0.1, 8])
    .on('zoom', (event) => g.attr('transform', event.transform));
  svg.call(zoom);

  // Tooltip
  const tooltip = d3.select(container)
    .append('div')
    .attr('class', 'graph-tooltip');

  // Force simulation
  simulation = d3.forceSimulation<GraphNode, GraphLink>(nodes)
    .force('link', d3.forceLink<GraphNode, GraphLink>(links)
      .id(d => d.id)
      .distance(d => d.linkType === 'belongs-to' ? 15 : 140)
      .strength(d => d.linkType === 'belongs-to' ? 1.8 : 0.06))
    .force('charge', d3.forceManyBody<GraphNode>()
      .strength(d => d.nodeType === 'schema' ? -700 : -5))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collision', d3.forceCollide<GraphNode>()
      .radius(d => d.nodeType === 'schema' ? 35 : 8))
    .force('x', d3.forceX(width / 2).strength(0.03))
    .force('y', d3.forceY(height / 2).strength(0.03))
    .alphaDecay(0.02);

  // Links
  const link = g.append('g')
    .attr('class', 'graph-links')
    .selectAll('line')
    .data(links)
    .join('line')
    .attr('stroke', d => d.linkType === 'shared-name' ? '#f59e0b' : '#2a2f42')
    .attr('stroke-width', d => d.linkType === 'shared-name' ? 2 : 0.8)
    .attr('stroke-opacity', d => d.linkType === 'shared-name' ? 0.7 : 0.25)
    .attr('stroke-dasharray', d => d.linkType === 'shared-name' ? '6,3' : 'none');

  // Node groups (circle + label together for dragging)
  const nodeGroup = g.append('g')
    .attr('class', 'graph-nodes')
    .selectAll<SVGGElement, GraphNode>('g')
    .data(nodes)
    .join('g')
    .attr('cursor', 'pointer')
    .call(d3.drag<SVGGElement, GraphNode>()
      .on('start', (event, d) => {
        if (!event.active) simulation!.alphaTarget(0.3).restart();
        d.fx = d.x; d.fy = d.y;
      })
      .on('drag', (event, d) => { d.fx = event.x; d.fy = event.y; })
      .on('end', (event, d) => {
        if (!event.active) simulation!.alphaTarget(0);
        d.fx = null; d.fy = null;
      }));

  // Circles within node groups
  nodeGroup.append('circle')
    .attr('r', d => d.nodeType === 'schema' ? 22 : 6)
    .attr('fill', d => {
      const color = TYPE_COLORS[d.schemaType!] || '#666';
      return d.nodeType === 'schema' ? color : color;
    })
    .attr('fill-opacity', d => d.nodeType === 'schema' ? 0.85 : 0.65)
    .attr('stroke', d => d.nodeType === 'schema' ? 'rgba(255,255,255,0.25)' : 'rgba(255,255,255,0.1)')
    .attr('stroke-width', d => d.nodeType === 'schema' ? 2.5 : 1);

  // Labels for ALL nodes
  nodeGroup.append('text')
    .text(d => d.label)
    .attr('font-size', d => d.nodeType === 'schema' ? '11px' : '8px')
    .attr('font-weight', d => d.nodeType === 'schema' ? '600' : '400')
    .attr('fill', d => d.nodeType === 'schema' ? '#c8d0e0' : '#6b7280')
    .attr('text-anchor', 'middle')
    .attr('dy', d => d.nodeType === 'schema' ? -28 : -10)
    .attr('pointer-events', 'none')
    .attr('class', d => `node-label node-label-${d.nodeType}`);

  // Hover — show tooltip
  nodeGroup.on('mouseenter', (event, d) => {
    const color = TYPE_COLORS[d.schemaType!] || '#666';
    const typeLabel = TYPE_LABELS[d.schemaType!] || d.schemaType || '';
    let content: string;
    if (d.nodeType === 'schema') {
      content = `<div class="tt-label">${esc(d.label)}</div><div class="tt-detail"><span style="color:${color}">${typeLabel}</span> &middot; ${d.count} properties</div><div class="tt-detail">${esc(d.filePath || '')}</div>`;
    } else {
      content = `<div class="tt-label">${esc(d.label)} <span style="color:${getDataTypeColor(d.propertyType || 'string')}">${esc(d.propertyType || '')}</span></div><div class="tt-detail">${esc(d.parentName || '')} &middot; <span style="color:${color}">${typeLabel}</span></div>`;
    }

    // Position relative to the container
    const rect = container.getBoundingClientRect();
    tooltip.html(content)
      .style('left', (event.clientX - rect.left + 14) + 'px')
      .style('top', (event.clientY - rect.top - 14) + 'px')
      .style('opacity', '1');

    // Subtle hover glow
    d3.select(event.currentTarget).select('circle')
      .attr('stroke', 'rgba(255,255,255,0.6)')
      .attr('stroke-width', d.nodeType === 'schema' ? 3 : 2);
  })
  .on('mousemove', (event) => {
    const rect = container.getBoundingClientRect();
    tooltip
      .style('left', (event.clientX - rect.left + 14) + 'px')
      .style('top', (event.clientY - rect.top - 14) + 'px');
  })
  .on('mouseleave', (event, d) => {
    tooltip.style('opacity', '0');
    d3.select(event.currentTarget).select('circle')
      .attr('stroke', d.nodeType === 'schema' ? 'rgba(255,255,255,0.25)' : 'rgba(255,255,255,0.1)')
      .attr('stroke-width', d.nodeType === 'schema' ? 2.5 : 1);
  });

  // Click to highlight shared properties
  nodeGroup.on('click', (event, d) => {
    event.stopPropagation();
    if (d.nodeType === 'property') {
      const name = d.propertyName!.toLowerCase();
      // Find connected schemas
      const connectedSchemas = new Set<string>();
      links.forEach(l => {
        const s = l.source as GraphNode;
        const t = l.target as GraphNode;
        if (s.propertyName?.toLowerCase() === name && t.nodeType === 'schema') connectedSchemas.add(t.id);
        if (t.propertyName?.toLowerCase() === name && s.nodeType === 'schema') connectedSchemas.add(s.id);
      });

      nodeGroup.attr('opacity', n =>
        n.propertyName?.toLowerCase() === name || connectedSchemas.has(n.id) ? 1 : 0.06);
      nodeGroup.selectAll('.node-label').attr('opacity', function() {
        const n = d3.select(this.parentNode as SVGGElement).datum() as GraphNode;
        return n.propertyName?.toLowerCase() === name || connectedSchemas.has(n.id) ? 1 : 0.06;
      });
      link.attr('opacity', l => {
        const s = l.source as GraphNode;
        const t = l.target as GraphNode;
        return (s.propertyName?.toLowerCase() === name || t.propertyName?.toLowerCase() === name) ? 0.9 : 0.02;
      });
    } else if (d.nodeType === 'schema') {
      // Highlight all properties belonging to this schema
      const schemaProps = new Set<string>();
      links.forEach(l => {
        const s = l.source as GraphNode;
        const t = l.target as GraphNode;
        if (t.id === d.id && s.nodeType === 'property') schemaProps.add(s.id);
        if (s.id === d.id && t.nodeType === 'property') schemaProps.add(t.id);
      });

      nodeGroup.attr('opacity', n =>
        n.id === d.id || schemaProps.has(n.id) ? 1 : 0.06);
      nodeGroup.selectAll('.node-label').attr('opacity', function() {
        const n = d3.select(this.parentNode as SVGGElement).datum() as GraphNode;
        return n.id === d.id || schemaProps.has(n.id) ? 1 : 0.06;
      });
      link.attr('opacity', l => {
        const s = l.source as GraphNode;
        const t = l.target as GraphNode;
        return (s.id === d.id || t.id === d.id || schemaProps.has(s.id) || schemaProps.has(t.id)) ? 0.9 : 0.02;
      });
    }
  });

  // Click background to reset
  svg.on('click', () => {
    nodeGroup.attr('opacity', 1);
    nodeGroup.selectAll('.node-label').attr('opacity', 1);
    link.attr('opacity', d => (d as GraphLink).linkType === 'shared-name' ? 0.7 : 0.25);
  });

  // Tick — update positions
  simulation.on('tick', () => {
    link
      .attr('x1', d => (d.source as GraphNode).x!)
      .attr('y1', d => (d.source as GraphNode).y!)
      .attr('x2', d => (d.target as GraphNode).x!)
      .attr('y2', d => (d.target as GraphNode).y!);
    nodeGroup
      .attr('transform', d => `translate(${d.x},${d.y})`);
  });

  // Responsive: resize on window resize
  const resizeObserver = new ResizeObserver(() => {
    if (activeView !== 'graph') return;
    const newW = container.clientWidth;
    const newH = container.clientHeight;
    if (newW === width && newH === height) return;
    width = newW;
    height = newH;
    svg.attr('width', width).attr('height', height).attr('viewBox', `0 0 ${width} ${height}`);
    simulation?.force('center', d3.forceCenter(width / 2, height / 2));
    simulation?.force('x', d3.forceX(width / 2).strength(0.03));
    simulation?.force('y', d3.forceY(height / 2).strength(0.03));
    simulation?.alpha(0.3).restart();
  });
  resizeObserver.observe(container);
}

// ─── Filtering & Sorting ───

function applyFilters() {
  if (searchQuery) {
    const params = new URLSearchParams({ q: searchQuery });
    if (activeTypeFilter) params.set('schemaType', activeTypeFilter);
    fetch(`/api/search?${params}`).then(r => r.json()).then(data => {
      let results: Property[] = data.results;
      if (activeSchemaFilters.size > 0) {
        results = results.filter(r => activeSchemaFilters.has(r.filePath));
      }
      filteredProperties = results;
      if (activeView === 'table') renderTable();
      else if (activeView === 'matrix') renderMatrix();
      else renderGraph();
    });
  } else {
    filteredProperties = allProperties.filter(p => {
      if (activeTypeFilter && p.schemaType !== activeTypeFilter) return false;
      if (activeSchemaFilters.size > 0 && !activeSchemaFilters.has(p.filePath)) return false;
      return true;
    });
    sortProperties();
    if (activeView === 'table') renderTable();
    else if (activeView === 'matrix') renderMatrix();
    else renderGraph();
  }
}

function sortProperties() {
  filteredProperties.sort((a, b) => {
    let va: string, vb: string;
    switch (sortField) {
      case 'name': va = a.name; vb = b.name; break;
      case 'schema': va = a.filePath; vb = b.filePath; break;
      case 'type': va = a.type; vb = b.type; break;
      default: va = a.name; vb = b.name;
    }
    return sortAsc ? va.localeCompare(vb) : vb.localeCompare(va);
  });
}

// ─── Events ───

function bindEvents() {
  const input = document.getElementById('search-input') as HTMLInputElement;
  input.addEventListener('input', () => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => { searchQuery = input.value.trim(); applyFilters(); }, 200);
  });

  // View tabs
  document.getElementById('view-tabs')!.addEventListener('click', (e) => {
    const tab = (e.target as HTMLElement).closest('.view-tab') as HTMLElement | null;
    if (!tab) return;
    switchView(tab.dataset.view as 'table' | 'graph' | 'matrix');
  });

  // Schema list clicks
  document.getElementById('schema-list')!.addEventListener('click', (e) => {
    const item = (e.target as HTMLElement).closest('.schema-item') as HTMLElement | null;
    if (!item) return;
    const file = item.dataset.file!;
    if (activeSchemaFilters.has(file)) activeSchemaFilters.delete(file);
    else activeSchemaFilters.add(file);
    renderSidebar();
    applyFilters();
  });

  document.getElementById('clear-schemas')!.addEventListener('click', () => {
    activeSchemaFilters.clear();
    renderSidebar();
    applyFilters();
  });

  document.getElementById('type-filters')!.addEventListener('click', (e) => {
    const chip = (e.target as HTMLElement).closest('.type-chip') as HTMLElement | null;
    if (!chip) return;
    activeTypeFilter = chip.dataset.type === 'all types' ? null : chip.dataset.type!;
    renderSidebar();
    applyFilters();
  });

  document.getElementById('table-toolbar')!.addEventListener('click', (e) => {
    const btn = (e.target as HTMLElement).closest('.sort-btn') as HTMLElement | null;
    if (!btn) return;
    const field = btn.dataset.sort as 'name' | 'schema' | 'type';
    if (sortField === field) sortAsc = !sortAsc;
    else { sortField = field; sortAsc = true; }
    sortProperties();
    renderTable();
  });

  document.getElementById('table-wrapper')!.addEventListener('click', (e) => {
    const row = (e.target as HTMLElement).closest('.prop-row') as HTMLElement | null;
    if (!row) return;
    const id = row.dataset.id!;
    const prop = filteredProperties.find(p => p.id === id) || allProperties.find(p => p.id === id);
    if (prop) showDetail(prop);
  });

  document.getElementById('back-btn')!.addEventListener('click', hideDetail);

  // Matrix sort
  document.getElementById('matrix-toolbar')!.addEventListener('click', (e) => {
    const btn = (e.target as HTMLElement).closest('[data-msort]') as HTMLElement | null;
    if (!btn) return;
    const field = btn.dataset.msort as 'alpha' | 'count' | 'required';
    if (matrixSortField === field) matrixSortAsc = !matrixSortAsc;
    else { matrixSortField = field; matrixSortAsc = field === 'alpha'; }
    renderMatrix();
  });

  // Graph shared toggle
  document.getElementById('graph-toolbar')!.addEventListener('change', (e) => {
    const target = e.target as HTMLInputElement;
    if (target.id === 'shared-toggle') {
      graphOnlyShared = target.checked;
      renderGraph();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && showingDetail) hideDetail();
  });
}

// ─── Helpers ───

function esc(s: string): string {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function escRegex(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

init();
```

## File: `ui/src/styles/main.css`
```css
/* ─── Reset & Base ─── */
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --bg: #0c0e14;
  --bg-surface: #12151e;
  --bg-elevated: #181c28;
  --bg-hover: #1e2235;
  --border: #1e2235;
  --border-subtle: #161a26;
  --text: #e2e8f0;
  --text-secondary: #8891a5;
  --text-muted: #555d73;
  --accent: #3b82f6;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Inter', sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.5;
  height: 100vh;
  overflow: hidden;
  -webkit-font-smoothing: antialiased;
}

#app { height: 100vh; display: flex; flex-direction: column; }

/* ─── Top Bar ─── */
.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1.5rem;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.topbar-title h1 {
  font-size: 1.125rem;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.01em;
}

.topbar-stats {
  font-size: 0.6875rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

/* ─── Main Layout ─── */
.main-layout {
  display: flex;
  flex: 1;
  overflow: hidden;
}

/* ─── Sidebar ─── */
.sidebar {
  width: 300px;
  min-width: 260px;
  background: var(--bg);
  border-right: 1px solid var(--border);
  overflow-y: auto;
  padding: 1rem 0;
  flex-shrink: 0;
}

.sidebar-section {
  padding: 0 1rem;
  margin-bottom: 1.5rem;
}

.sidebar-heading {
  font-size: 0.6875rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.clear-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 0.6875rem;
  cursor: pointer;
  padding: 0;
  transition: color 0.15s;
}
.clear-btn:hover { color: var(--text-secondary); }

/* Schema list */
.schema-list {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.schema-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.625rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: background 0.1s;
}
.schema-item:hover { background: var(--bg-hover); }
.schema-item.active {
  background: rgba(59, 130, 246, 0.08);
  outline: 1px solid rgba(59, 130, 246, 0.25);
}

.schema-badge {
  font-size: 0.5625rem;
  font-weight: 700;
  padding: 0.125rem 0.375rem;
  border-radius: 0.25rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
  flex-shrink: 0;
}

.schema-info {
  flex: 1;
  overflow: hidden;
  min-width: 0;
}

.schema-name {
  font-size: 0.8125rem;
  font-weight: 500;
  color: var(--text);
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.schema-filepath {
  font-size: 0.625rem;
  color: var(--text-muted);
  display: block;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
  margin-top: 0.0625rem;
}

.schema-count {
  font-size: 0.75rem;
  color: var(--text-muted);
  flex-shrink: 0;
}

/* Type filter chips */
.type-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 0.375rem;
}

.type-chip {
  font-size: 0.75rem;
  padding: 0.3125rem 0.625rem;
  border-radius: 0.375rem;
  border: 1px solid var(--border);
  background: var(--bg-surface);
  color: var(--text-secondary);
  cursor: pointer;
  transition: all 0.15s;
}
.type-chip:hover { background: var(--bg-hover); border-color: #2a2f42; }
.type-chip.active {
  background: rgba(59, 130, 246, 0.12);
  border-color: rgba(59, 130, 246, 0.35);
  color: #93bbfc;
}

/* ─── Content ─── */
.content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.content-top {
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}

/* Search bar */
.search-bar {
  position: relative;
  padding: 1rem 1.5rem 0.75rem;
}

.content-top .type-filters {
  padding: 0 1.5rem 0.75rem;
}

.search-bar .search-icon {
  position: absolute;
  left: 2.25rem;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  pointer-events: none;
}

#search-input {
  width: 100%;
  padding: 0.75rem 1rem 0.75rem 2.5rem;
  font-size: 0.9375rem;
  border: 1px solid var(--border);
  border-radius: 0.5rem;
  outline: none;
  background: var(--bg-elevated);
  color: var(--text);
  transition: border-color 0.15s;
}
#search-input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}
#search-input::placeholder { color: var(--text-muted); }

/* ─── Table ─── */
.table-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1.5rem;
  border-bottom: 1px solid var(--border-subtle);
  flex-shrink: 0;
}

.table-count {
  font-size: 0.8125rem;
  color: var(--text-secondary);
}
.table-count strong {
  color: var(--text);
}

.sort-controls {
  display: flex;
  gap: 0.75rem;
}

.sort-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 0.75rem;
  cursor: pointer;
  transition: color 0.15s;
  padding: 0;
}
.sort-btn:hover { color: var(--text-secondary); }
.sort-btn.active { color: var(--accent); }

.table-wrapper {
  flex: 1;
  overflow-y: auto;
}

.table-empty {
  text-align: center;
  padding: 4rem 1rem;
  color: var(--text-muted);
  font-size: 0.875rem;
}

.prop-table {
  width: 100%;
  border-collapse: collapse;
}

.prop-table thead th {
  position: sticky;
  top: 0;
  background: var(--bg-surface);
  font-size: 0.6875rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  text-align: left;
  padding: 0.625rem 1rem;
  border-bottom: 1px solid var(--border);
  z-index: 1;
}

.prop-row {
  cursor: pointer;
  transition: background 0.1s;
  border-bottom: 1px solid var(--border-subtle);
}
.prop-row:hover { background: var(--bg-hover); }

.prop-row td {
  padding: 0.75rem 1rem;
  vertical-align: middle;
}

/* Column: Property */
.col-property {
  min-width: 160px;
}

.col-property .prop-name {
  font-weight: 600;
  font-size: 0.9375rem;
  color: var(--text);
  display: block;
  font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
}

.col-property .prop-parent {
  font-size: 0.6875rem;
  color: var(--text-muted);
}

/* Column: Type */
.type-badge {
  font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.1875rem 0.5rem;
  border-radius: 0.25rem;
  white-space: nowrap;
}

/* Column: Schema */
.col-schema {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.schema-badge-sm {
  font-size: 0.5rem;
  font-weight: 700;
  padding: 0.125rem 0.3125rem;
  border-radius: 0.1875rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  white-space: nowrap;
}

.schema-file {
  font-size: 0.8125rem;
  color: var(--text-secondary);
}

/* Column: Required */
.req-yes {
  display: inline-flex;
  align-items: center;
  gap: 0.3125rem;
  font-size: 0.75rem;
  color: #f87171;
}

.req-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #f87171;
  display: inline-block;
}

.req-no {
  font-size: 0.75rem;
  color: var(--text-muted);
}

/* Column: Description */
.col-desc {
  font-size: 0.8125rem;
  color: var(--text-secondary);
  max-width: 300px;
}

.no-desc { color: var(--text-muted); }

/* ─── Detail View ─── */
.detail-view {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.detail-view.hidden { display: none; }
#table-view.hidden { display: none; }
#table-view {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.back-btn {
  background: none;
  border: none;
  color: var(--accent);
  font-size: 0.8125rem;
  cursor: pointer;
  padding: 0.75rem 1.5rem;
  text-align: left;
  transition: color 0.15s;
  flex-shrink: 0;
  border-bottom: 1px solid var(--border-subtle);
}
.back-btn:hover { color: #60a5fa; }

.detail-header {
  padding: 1rem 1.5rem;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border);
  flex-shrink: 0;
}

.detail-title-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.detail-name {
  font-weight: 700;
  font-size: 1.25rem;
  color: var(--text);
  font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
}

.detail-format {
  font-size: 0.6875rem;
  padding: 0.125rem 0.375rem;
  border-radius: 9999px;
  background: rgba(16, 185, 129, 0.12);
  color: #34d399;
}

.detail-desc {
  font-size: 0.8125rem;
  color: var(--text-secondary);
  margin-top: 0.5rem;
}

.detail-path {
  font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
  font-size: 0.6875rem;
  color: var(--text-muted);
  margin-top: 0.375rem;
  word-break: break-all;
}

.detail-editor {
  flex: 1;
  overflow: hidden;
}

/* Monaco highlight */
.highlighted-line {
  background: rgba(250, 204, 21, 0.1) !important;
  border-left: 3px solid #facc15 !important;
}

/* ─── Scrollbar ─── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #2a2f42; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #3a4058; }

/* ─── View Tabs ─── */
.view-tabs {
  display: flex;
  gap: 0.25rem;
}

.view-tab {
  background: none;
  border: 1px solid transparent;
  color: var(--text-muted);
  font-size: 0.75rem;
  font-weight: 500;
  padding: 0.375rem 0.75rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.15s;
}
.view-tab:hover { color: var(--text-secondary); background: var(--bg-hover); }
.view-tab.active {
  background: rgba(59, 130, 246, 0.12);
  border-color: rgba(59, 130, 246, 0.35);
  color: #93bbfc;
}

/* ─── Matrix View ─── */
.matrix-view {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.matrix-view.hidden { display: none; }

.matrix-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1.5rem;
  border-bottom: 1px solid var(--border-subtle);
  flex-shrink: 0;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.matrix-stats {
  font-size: 0.8125rem;
  color: var(--text-secondary);
}
.matrix-stats strong { color: var(--text); }

.matrix-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.matrix-sort-label {
  font-size: 0.6875rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.matrix-legend {
  display: flex;
  gap: 0.75rem;
}

.matrix-container {
  flex: 1;
  overflow: auto;
  position: relative;
  background: var(--bg);
}

.matrix-empty {
  text-align: center;
  padding: 4rem 1rem;
  color: var(--text-muted);
  font-size: 0.875rem;
}

/* Grid layout */
.matrix-grid {
  display: grid;
  width: fit-content;
  min-width: 100%;
}

/* Corner cell */
.matrix-corner {
  position: sticky;
  left: 0;
  top: 0;
  z-index: 4;
  background: var(--bg-surface);
  font-size: 0.6875rem;
  font-weight: 600;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  display: flex;
  align-items: flex-end;
  padding: 0 0.75rem 0.5rem;
  border-bottom: 1px solid var(--border);
  border-right: 1px solid var(--border-subtle);
}

.matrix-count-header {
  position: sticky;
  left: 180px;
  top: 0;
  z-index: 4;
  background: var(--bg-surface);
  font-size: 0.6875rem;
  font-weight: 600;
  color: var(--text-muted);
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding: 0 0.25rem 0.5rem;
  border-bottom: 1px solid var(--border);
  border-right: 1px solid var(--border-subtle);
}

/* Schema column headers — rotated text */
.matrix-schema-header {
  position: sticky;
  top: 0;
  z-index: 3;
  background: var(--bg-surface);
  border-bottom: 1px solid var(--border);
  height: 110px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 0.375rem;
  cursor: pointer;
  transition: background 0.1s;
}
.matrix-schema-header:hover { background: var(--bg-hover); }

.matrix-schema-label {
  writing-mode: vertical-rl;
  text-orientation: mixed;
  transform: rotate(180deg);
  font-size: 0.625rem;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-height: 100px;
  letter-spacing: 0.02em;
}

/* Property row header — sticky left column */
.matrix-prop-cell {
  position: sticky;
  left: 0;
  z-index: 2;
  background: var(--bg);
  font-size: 0.75rem;
  font-weight: 500;
  color: var(--text);
  font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
  padding: 0.25rem 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.375rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  border-bottom: 1px solid var(--border-subtle);
  border-right: 1px solid var(--border-subtle);
  cursor: pointer;
  transition: background 0.1s;
}
.matrix-prop-cell:hover { background: var(--bg-hover); }

.matrix-prop-type {
  font-size: 0.625rem;
  font-weight: 400;
  opacity: 0.6;
}

.matrix-shared-badge {
  font-size: 0.5625rem;
  font-weight: 700;
  background: rgba(59, 130, 246, 0.15);
  color: #93bbfc;
  padding: 0.0625rem 0.3125rem;
  border-radius: 0.1875rem;
  flex-shrink: 0;
}

/* Count column */
.matrix-count-cell {
  position: sticky;
  left: 180px;
  z-index: 2;
  background: var(--bg);
  font-size: 0.6875rem;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid var(--border-subtle);
  border-right: 1px solid var(--border-subtle);
}

/* Data cells */
.matrix-cell {
  width: 28px;
  height: 28px;
  border-bottom: 1px solid var(--border-subtle);
  border-right: 1px solid rgba(22, 26, 38, 0.5);
  transition: transform 0.1s, box-shadow 0.1s;
}

.matrix-cell-required {
  background: rgba(34, 197, 94, 0.5);
}

.matrix-cell-optional {
  background: rgba(59, 130, 246, 0.4);
}

.matrix-cell-empty {
  background: transparent;
}

.matrix-cell:not(.matrix-cell-empty):hover {
  transform: scale(1.3);
  z-index: 5;
  box-shadow: 0 0 8px rgba(255, 255, 255, 0.15);
  border-radius: 2px;
}

/* Hover highlighting */
.matrix-highlight-row {
  background: var(--bg-hover) !important;
}
.matrix-highlight-row.matrix-cell-required {
  background: rgba(34, 197, 94, 0.7) !important;
}
.matrix-highlight-row.matrix-cell-optional {
  background: rgba(59, 130, 246, 0.6) !important;
}
.matrix-highlight-col {
  background: var(--bg-hover) !important;
}
.matrix-highlight-col.matrix-cell-required {
  background: rgba(34, 197, 94, 0.7) !important;
}
.matrix-highlight-col.matrix-cell-optional {
  background: rgba(59, 130, 246, 0.6) !important;
}

/* Matrix tooltip */
.matrix-tooltip {
  position: absolute;
  pointer-events: none;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: 0.5rem;
  padding: 0.5rem 0.75rem;
  font-size: 0.75rem;
  color: var(--text);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
  z-index: 100;
  max-width: 250px;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.1s;
}

/* ─── Graph View ─── */
.graph-view {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.graph-view.hidden { display: none; }

.graph-toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1.5rem;
  border-bottom: 1px solid var(--border-subtle);
  flex-shrink: 0;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.graph-stats {
  font-size: 0.8125rem;
  color: var(--text-secondary);
}
.graph-stats strong { color: var(--text); }

.graph-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.graph-toggle {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.75rem;
  color: var(--text-secondary);
  cursor: pointer;
}

.graph-toggle input[type="checkbox"] {
  accent-color: var(--accent);
}

.graph-legend {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  font-size: 0.6875rem;
  color: var(--text-muted);
}

.legend-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.graph-container {
  flex: 1;
  overflow: hidden;
  background: var(--bg);
  position: relative;
}

.graph-container svg {
  width: 100%;
  height: 100%;
  display: block;
}

.graph-nodes text {
  user-select: none;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
}

.graph-links line {
  shape-rendering: geometricPrecision;
}

.graph-empty {
  text-align: center;
  padding: 4rem 1rem;
  color: var(--text-muted);
  font-size: 0.875rem;
}

/* Graph tooltip */
.graph-tooltip {
  position: absolute;
  pointer-events: none;
  background: var(--bg-elevated);
  border: 1px solid var(--border);
  border-radius: 0.5rem;
  padding: 0.5rem 0.75rem;
  font-size: 0.75rem;
  color: var(--text);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
  z-index: 100;
  max-width: 250px;
  white-space: nowrap;
  opacity: 0;
  transition: opacity 0.1s;
}

.graph-tooltip.visible { opacity: 1; }

.graph-tooltip .tt-label {
  font-weight: 600;
  margin-bottom: 0.125rem;
}

.graph-tooltip .tt-detail {
  color: var(--text-muted);
  font-size: 0.6875rem;
}

/* ─── Responsive ─── */
@media (max-width: 900px) {
  .sidebar { display: none; }
}
```

## File: `website/astro.config.mjs`
```
import { defineConfig } from 'astro/config';

export default defineConfig({});
```

## File: `website/package.json`
```json
{
  "name": "@eventcatalog/fieldtrip-website",
  "type": "module",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "dependencies": {
    "astro": "^5.9.3"
  }
}
```

## File: `website/tsconfig.json`
```json
{
  "extends": "astro/tsconfigs/strict"
}
```

## File: `website/public/og.html`
```html
<!DOCTYPE html>
<html>
<head>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1200px;
    height: 630px;
    background: #0b0d11;
    font-family: 'Inter', -apple-system, sans-serif;
    display: flex;
    overflow: hidden;
    position: relative;
  }
  .grid-bg {
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black 20%, transparent 70%);
  }
  .content {
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 80px;
    flex: 1;
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 32px;
  }
  .brand svg { width: 40px; height: 40px; }
  .brand span {
    font-size: 18px;
    font-weight: 600;
    color: #8b8fa3;
  }
  .brand .by { color: #4a4f63; font-weight: 400; }
  h1 {
    font-size: 56px;
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.03em;
    color: #e8eaed;
    max-width: 600px;
  }
  h1 .highlight {
    background: linear-gradient(135deg, #3b82f6, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .sub {
    font-size: 18px;
    color: #8b8fa3;
    margin-top: 20px;
    max-width: 480px;
    line-height: 1.6;
  }
  .chips {
    display: flex;
    gap: 8px;
    margin-top: 32px;
  }
  .chip {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 14px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 999px;
    font-size: 12px;
    color: #8b8fa3;
    font-weight: 500;
  }
  .chip-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
  }
  .preview {
    position: absolute;
    right: -40px;
    top: 50%;
    transform: translateY(-50%);
    width: 580px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.08);
    overflow: hidden;
    box-shadow: 0 32px 80px rgba(0,0,0,0.6);
  }
  .preview img { width: 100%; display: block; }
</style>
</head>
<body>
  <div class="grid-bg"></div>
  <div class="content">
    <div class="brand">
      <svg viewBox="0 0 32 32" fill="none">
        <rect width="32" height="32" rx="8" fill="#3b82f6"/>
        <path d="M10 12h12M10 16h8M10 20h10" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
      </svg>
      <span>FieldTrip <span class="by">by EventCatalog</span></span>
    </div>
    <h1>Search every field across <span class="highlight">all your schemas.</span></h1>
    <p class="sub">OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema — indexed and visualized instantly.</p>
    <div class="chips">
      <div class="chip"><div class="chip-dot" style="background:#3b82f6"></div>OpenAPI</div>
      <div class="chip"><div class="chip-dot" style="background:#8b5cf6"></div>AsyncAPI</div>
      <div class="chip"><div class="chip-dot" style="background:#10b981"></div>Protobuf</div>
      <div class="chip"><div class="chip-dot" style="background:#f59e0b"></div>Avro</div>
      <div class="chip"><div class="chip-dot" style="background:#6366f1"></div>JSON Schema</div>
    </div>
  </div>
  <div class="preview">
    <img src="images/matrix.png" alt="" />
  </div>
</body>
</html>
```

## File: `website/src/layouts/Layout.astro`
```
---
interface Props {
  title: string;
}

const { title } = Astro.props;
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <meta name="description" content="Search, explore, and visualize every field across your OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files." />
  <meta property="og:type" content="website" />
  <meta property="og:title" content={title} />
  <meta property="og:description" content="Search, explore, and visualize every field across your OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files." />
  <meta property="og:image" content="/og.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content={title} />
  <meta name="twitter:description" content="Search, explore, and visualize every field across your OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files." />
  <meta name="twitter:image" content="/og.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <title>{title}</title>
</head>
<body>
  <slot />
</body>
</html>
```

## File: `website/src/pages/index.astro`
```
---
import Layout from '../layouts/Layout.astro';
import '../styles/landing.css';
---

<Layout title="FieldTrip — Search every field across your schemas">

  <!-- Nav -->
  <nav>
    <div class="nav-left">
      <a href="/" class="nav-brand">
        <svg viewBox="0 0 32 32" fill="none">
          <rect width="32" height="32" rx="8" fill="#3b82f6"/>
          <path d="M10 12h12M10 16h8M10 20h10" stroke="#fff" stroke-width="2" stroke-linecap="round"/>
        </svg>
        FieldTrip
        <span class="nav-by">by EventCatalog</span>
      </a>
    </div>
    <div class="nav-links">
      <a href="#features">Features</a>
      <a href="#schemas">Schemas</a>
      <a href="#how">How It Works</a>
      <a href="https://github.com/event-catalog/fieldtrip" target="_blank" rel="noreferrer">GitHub</a>
    </div>
  </nav>

  <!-- Hero -->
  <section class="hero">
    <h1>
      Search every field.<br/>
      Across <span class="highlight">all your schemas.</span>
    </h1>
    <p class="hero-sub">
      Point FieldTrip at a directory. It finds your OpenAPI, AsyncAPI, Protobuf, Avro, and JSON Schema files, indexes every property, and lets you explore them instantly.
    </p>
    <div class="install-block" id="hero-install">
      <span>$</span>
      <code>npx @eventcatalog/fieldtrip --dir ./schemas</code>
      <button class="copy-btn" aria-label="Copy to clipboard" data-copy="npx @eventcatalog/fieldtrip --dir ./schemas">
        <svg class="copy-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
        <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16"><polyline points="20 6 9 17 4 12"/></svg>
      </button>
    </div>
    <p class="hero-oss">Open source &middot; MIT License</p>

    <div class="hero-screenshot">
      <img src="/images/matrix.png" alt="FieldTrip matrix view showing property coverage across schemas" />
    </div>
  </section>

  <div class="divider"></div>

  <!-- Features -->
  <section class="section section-center" id="features">
    <div class="section-label">Features</div>
    <h2 class="section-title">Three ways to explore your schemas</h2>
    <p class="section-desc">
      Search by property name, see which schemas share the same fields, and visualize how everything connects.
    </p>

    <div class="features-stack">
      <!-- Table: text left, image right -->
      <div class="feature-row">
        <div class="feature-text">
          <div class="feature-card-icon" style="background: rgba(59,130,246,0.12);">
            <svg viewBox="0 0 24 24" fill="none" stroke="#3b82f6" stroke-width="2" stroke-linecap="round">
              <rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/>
              <rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/>
            </svg>
          </div>
          <h3>Table View</h3>
          <p>Full-text search across property names, types, and descriptions. Filter by schema type, sort columns, and click any row to view the source with syntax highlighting.</p>
        </div>
        <div class="feature-img">
          <img src="/images/table.png" alt="Table view showing schema properties" />
        </div>
      </div>

      <!-- Matrix: image left, text right -->
      <div class="feature-row feature-row-reverse">
        <div class="feature-text">
          <div class="feature-card-icon" style="background: rgba(139,92,246,0.12);">
            <svg viewBox="0 0 24 24" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round">
              <rect x="3" y="3" width="4" height="4"/><rect x="10" y="3" width="4" height="4"/>
              <rect x="17" y="3" width="4" height="4"/><rect x="3" y="10" width="4" height="4"/>
              <rect x="10" y="10" width="4" height="4"/><rect x="3" y="17" width="4" height="4"/>
              <rect x="17" y="17" width="4" height="4"/>
            </svg>
          </div>
          <h3>Property Matrix</h3>
          <p>A heatmap-style grid showing which properties appear in which schemas. Green for required, blue for optional. Instantly spot shared fields across your architecture.</p>
        </div>
        <div class="feature-img">
          <img src="/images/matrix.png" alt="Matrix view showing property coverage" />
        </div>
      </div>

      <!-- Graph: text left, image right -->
      <div class="feature-row">
        <div class="feature-text">
          <div class="feature-card-icon" style="background: rgba(16,185,129,0.12);">
            <svg viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2" stroke-linecap="round">
              <circle cx="5" cy="6" r="2"/><circle cx="19" cy="6" r="2"/><circle cx="12" cy="18" r="2"/>
              <line x1="7" y1="6" x2="17" y2="6"/><line x1="6" y1="8" x2="11" y2="16"/>
              <line x1="18" y1="8" x2="13" y2="16"/>
            </svg>
          </div>
          <h3>Force-Directed Graph</h3>
          <p>Visualize how schemas connect through shared properties. Click any node to highlight relationships. Drag, zoom, and explore the architecture.</p>
        </div>
        <div class="feature-img">
          <img src="/images/graph.png" alt="Graph view showing schema relationships" />
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- Schemas -->
  <section class="section section-center" id="schemas">
    <div class="section-label">Supported Formats</div>
    <h2 class="section-title">Works with what you already have</h2>
    <p class="section-desc">
      FieldTrip auto-detects schema types from file extensions and content. No configuration needed.
    </p>

    <div class="schemas-grid">
      <div class="schema-chip">
        <span class="chip-dot" style="background: #3b82f6;"></span>
        OpenAPI
      </div>
      <div class="schema-chip">
        <span class="chip-dot" style="background: #8b5cf6;"></span>
        AsyncAPI
      </div>
      <div class="schema-chip">
        <span class="chip-dot" style="background: #10b981;"></span>
        Protobuf
      </div>
      <div class="schema-chip">
        <span class="chip-dot" style="background: #f59e0b;"></span>
        Avro
      </div>
      <div class="schema-chip">
        <span class="chip-dot" style="background: #6366f1;"></span>
        JSON Schema
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- How It Works -->
  <section class="section section-center" id="how">
    <div class="section-label">How It Works</div>
    <h2 class="section-title">One command. Zero config.</h2>
    <p class="section-desc">
      FieldTrip scans, parses, indexes, and serves — all locally, in seconds.
    </p>

    <div class="steps">
      <div class="step">
        <div class="step-number">Step 1</div>
        <h3>Scan</h3>
        <p>Recursively finds schema files by extension and content detection in your directory.</p>
      </div>
      <div class="step">
        <div class="step-number">Step 2</div>
        <h3>Parse</h3>
        <p>Extracts every property with its name, type, description, path, and required status.</p>
      </div>
      <div class="step">
        <div class="step-number">Step 3</div>
        <h3>Index</h3>
        <p>Builds an index with prefix matching and fuzzy search.</p>
      </div>
      <div class="step">
        <div class="step-number">Step 4</div>
        <h3>Serve</h3>
        <p>Opens a local web UI with table, matrix, and graph views to explore everything.</p>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- CTA -->
  <section class="cta-section">
    <h2>Start exploring your schemas</h2>
    <p>FieldTrip is free, open source, and runs entirely on your machine. Nothing is uploaded anywhere.</p>
    <div class="install-block" id="cta-install">
      <span>$</span>
      <code>npx @eventcatalog/fieldtrip --dir ./schemas</code>
      <button class="copy-btn" aria-label="Copy to clipboard" data-copy="npx @eventcatalog/fieldtrip --dir ./schemas">
        <svg class="copy-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
        <svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="16" height="16"><polyline points="20 6 9 17 4 12"/></svg>
      </button>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-links">
      <a href="https://github.com/event-catalog/fieldtrip">GitHub</a>
      <a href="https://www.npmjs.com/package/@eventcatalog/fieldtrip">npm</a>
      <a href="https://eventcatalog.dev">EventCatalog</a>
    </div>
    <p>MIT License &middot; Built by <a href="https://eventcatalog.dev">EventCatalog</a></p>
  </footer>

  <script>
    document.querySelectorAll('.copy-btn').forEach(btn => {
      btn.addEventListener('click', async (e) => {
        e.stopPropagation();
        const text = (btn as HTMLElement).dataset.copy || '';
        await navigator.clipboard.writeText(text);
        btn.classList.add('copied');
        setTimeout(() => btn.classList.remove('copied'), 2000);
      });
    });

    document.querySelectorAll('.install-block').forEach(block => {
      block.addEventListener('click', () => {
        const btn = block.querySelector('.copy-btn') as HTMLElement;
        if (btn) btn.click();
      });
    });
  </script>

</Layout>
```

## File: `website/src/styles/landing.css`
```css
/* ─── Variables ─── */
:root {
  --bg-deep: #0b0d11;
  --bg-surface: #12151b;
  --bg-elevated: #1a1e27;
  --accent: #3b82f6;
  --accent-soft: rgba(59, 130, 246, 0.12);
  --accent-border: rgba(59, 130, 246, 0.25);
  --green: #34d399;
  --purple: #8b5cf6;
  --orange: #fb923c;
  --cyan: #22d3ee;
  --text-primary: #e8eaed;
  --text-secondary: #8b8fa3;
  --text-muted: #4a4f63;
  --border: rgba(255,255,255,0.06);
  --border-hover: rgba(255,255,255,0.12);
}

/* ─── Reset ─── */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

html { scroll-behavior: smooth; }

body {
  background: var(--bg-deep);
  color: var(--text-primary);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
  line-height: 1.5;
}

a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }

/* ─── Nav ─── */
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 0 40px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(11, 13, 17, 0.85);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  font-size: 15px;
  color: var(--text-primary);
}

.nav-brand svg { width: 28px; height: 28px; flex-shrink: 0; }

.nav-by {
  font-weight: 400;
  font-size: 13px;
  color: var(--text-muted);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 28px;
}

.nav-links a {
  color: var(--text-secondary);
  font-size: 13px;
  font-weight: 400;
  transition: color 0.15s;
}
.nav-links a:hover { color: var(--text-primary); }

.nav-cta {
  background: var(--text-primary) !important;
  color: var(--bg-deep) !important;
  padding: 6px 16px !important;
  border-radius: 6px;
  font-weight: 600 !important;
  font-size: 13px !important;
  transition: opacity 0.15s !important;
}
.nav-cta:hover { opacity: 0.9; }

/* ─── Hero ─── */
.hero {
  position: relative;
  padding: 140px 40px 60px;
  text-align: center;
  max-width: 1200px;
  margin: 0 auto;
}

.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
  background-size: 48px 48px;
  mask-image: radial-gradient(ellipse 70% 60% at 50% 40%, black 20%, transparent 70%);
  -webkit-mask-image: radial-gradient(ellipse 70% 60% at 50% 40%, black 20%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

.hero > * { position: relative; z-index: 1; }

.hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: var(--text-secondary);
  margin-bottom: 24px;
  animation: fadeIn 0.6s ease-out;
}

.hero-eyebrow .dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--green);
  animation: pulse 2.5s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}

.hero h1 {
  font-size: clamp(36px, 5.5vw, 60px);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.03em;
  max-width: 900px;
  margin: 0 auto 20px;
  animation: fadeUp 0.7s ease-out;
}

.hero h1 .highlight {
  background: linear-gradient(135deg, var(--accent), var(--cyan));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-sub {
  font-size: 17px;
  color: var(--text-secondary);
  max-width: 640px;
  margin: 0 auto 36px;
  line-height: 1.65;
  font-weight: 400;
  animation: fadeUp 0.7s ease-out 0.1s both;
}

.hero-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
  animation: fadeUp 0.7s ease-out 0.2s both;
}

.btn-primary {
  background: var(--text-primary);
  color: var(--bg-deep);
  padding: 10px 24px;
  border-radius: 8px;
  font-weight: 600;
  font-size: 14px;
  transition: opacity 0.15s;
}
.btn-primary:hover { opacity: 0.9; }

.btn-ghost {
  background: transparent;
  color: var(--text-secondary);
  padding: 10px 24px;
  border-radius: 8px;
  font-weight: 500;
  font-size: 14px;
  border: 1px solid var(--border-hover);
  transition: all 0.15s;
}
.btn-ghost:hover { color: var(--text-primary); border-color: rgba(255,255,255,0.2); }

/* ─── Install ─── */
.install-block {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: var(--bg-surface);
  border: 1px solid var(--border-hover);
  border-radius: 8px;
  padding: 10px 20px;
  margin-top: 28px;
  font-family: 'SF Mono', 'Fira Code', 'Cascadia Code', monospace;
  font-size: 14px;
  color: var(--text-secondary);
  animation: fadeUp 0.7s ease-out 0.3s both;
}

.install-block {
  cursor: pointer;
  transition: border-color 0.15s, background 0.15s;
}

.install-block:hover {
  border-color: rgba(255,255,255,0.18);
  background: var(--bg-elevated);
}

.install-block code {
  color: var(--green);
  font-weight: 500;
}

.copy-btn {
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.15s, background 0.15s;
  margin-left: 4px;
  flex-shrink: 0;
}

.copy-btn:hover {
  color: var(--text-secondary);
  background: rgba(255,255,255,0.06);
}

.copy-btn .check-icon { display: none; }
.copy-btn.copied .copy-icon { display: none; }
.copy-btn.copied .check-icon { display: block; color: var(--green); }

.hero-oss {
  margin-top: 14px;
  font-size: 13px;
  color: var(--text-muted);
  animation: fadeUp 0.7s ease-out 0.35s both;
}

/* ─── Hero Screenshot ─── */
.hero-screenshot {
  margin-top: 56px;
  border-radius: 12px;
  border: 1px solid var(--border-hover);
  overflow: hidden;
  box-shadow: 0 24px 80px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.04);
  animation: fadeUp 0.8s ease-out 0.35s both;
}

.hero-screenshot img {
  width: 100%;
  display: block;
}

/* ─── Section ─── */
.section {
  padding: 100px 40px;
  max-width: 1200px;
  margin: 0 auto;
}

.section-center { text-align: center; }

.section-label {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--accent);
  margin-bottom: 16px;
}

.section-title {
  font-size: clamp(28px, 3.5vw, 42px);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.02em;
  margin-bottom: 16px;
}

.section-desc {
  font-size: 16px;
  color: var(--text-secondary);
  max-width: 600px;
  line-height: 1.6;
}

.section-center .section-desc { margin: 0 auto 56px; }

/* ─── Divider ─── */
.divider {
  height: 1px;
  background: var(--border);
  max-width: 1200px;
  margin: 0 auto;
}

/* ─── Feature Rows (alternating) ─── */
.features-stack {
  display: flex;
  flex-direction: column;
  gap: 80px;
  margin-top: 64px;
}

.feature-row {
  display: grid;
  grid-template-columns: 1fr 1.6fr;
  gap: 48px;
  align-items: center;
}

.feature-row-reverse {
  grid-template-columns: 1.6fr 1fr;
}

.feature-row-reverse .feature-text {
  order: 2;
}

.feature-row-reverse .feature-img {
  order: 1;
}

.feature-text {
  text-align: left;
}

.feature-card-icon {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.feature-card-icon svg {
  width: 20px;
  height: 20px;
}

.feature-text h3 {
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 12px;
  letter-spacing: -0.01em;
}

.feature-text p {
  font-size: 15px;
  color: var(--text-secondary);
  line-height: 1.7;
}

.feature-img {
  border-radius: 12px;
  border: 1px solid var(--border-hover);
  overflow: hidden;
  box-shadow: 0 16px 64px rgba(0,0,0,0.4), 0 0 0 1px rgba(255,255,255,0.04);
  transition: box-shadow 0.3s, transform 0.3s;
}

.feature-img:hover {
  box-shadow: 0 20px 80px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.06);
  transform: translateY(-2px);
}

.feature-img img {
  width: 100%;
  display: block;
}

/* ─── Schema Types ─── */
.schemas-grid {
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  margin-top: 48px;
}

.schema-chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  background: var(--bg-surface);
  border: 1px solid var(--border);
  border-radius: 999px;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-secondary);
  transition: border-color 0.15s;
}

.schema-chip:hover { border-color: var(--border-hover); }

.schema-chip .chip-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

/* ─── How It Works ─── */
.steps {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2px;
  margin-top: 48px;
  background: var(--border);
  border-radius: 12px;
  overflow: hidden;
}

.step {
  background: var(--bg-surface);
  padding: 32px 28px;
}

.step-number {
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent);
  margin-bottom: 16px;
}

.step h3 {
  font-size: 15px;
  font-weight: 600;
  margin-bottom: 8px;
}

.step p {
  font-size: 13px;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* ─── CTA ─── */
.cta-section {
  text-align: center;
  padding: 100px 40px;
  max-width: 700px;
  margin: 0 auto;
}

.cta-section h2 {
  font-size: clamp(28px, 3.5vw, 40px);
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 16px;
}

.cta-section p {
  color: var(--text-secondary);
  font-size: 16px;
  margin-bottom: 32px;
  line-height: 1.6;
}

.cta-section .install-block {
  padding: 14px 28px;
  font-size: 15px;
}

/* ─── Footer ─── */
footer {
  padding: 40px;
  text-align: center;
  color: var(--text-muted);
  font-size: 13px;
  border-top: 1px solid var(--border);
}

footer a {
  color: var(--text-secondary);
  transition: color 0.15s;
}
footer a:hover { color: var(--text-primary); }

.footer-links {
  display: flex;
  justify-content: center;
  gap: 24px;
  margin-bottom: 16px;
}

/* ─── Responsive ─── */
@media (max-width: 900px) {
  nav { padding: 0 20px; }
  .nav-links { display: none; }
  .hero { padding: 120px 20px 40px; }
  .feature-row,
  .feature-row-reverse { grid-template-columns: 1fr; gap: 32px; }
  .feature-row-reverse .feature-text { order: 0; }
  .feature-row-reverse .feature-img { order: 0; }
  .steps { grid-template-columns: 1fr; }
  .section { padding: 60px 20px; }
}

@media (max-width: 600px) {
  .hero h1 { font-size: 32px; }
  .hero-sub { font-size: 15px; }
  .schemas-grid { gap: 8px; }
  .schema-chip { padding: 8px 14px; font-size: 12px; }
}
```

